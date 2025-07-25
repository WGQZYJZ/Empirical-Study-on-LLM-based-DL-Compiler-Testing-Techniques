import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_273 = relay.const([[[4.584622,-4.268123,9.501514,5.954739,4.809308,9.502032,-5.013002,5.797398,9.791002,9.550334],[8.662208,-6.884049,-7.433337,7.080151,-8.431700,7.797517,-2.818371,-0.538661,6.507686,-3.084153],[-9.302673,5.029408,-7.403277,0.164152,-8.911733,-6.464225,-6.163105,-9.654265,-5.508253,9.669195],[-9.721202,4.183954,-1.892416,-8.221925,2.538691,0.057390,-7.855504,-7.900013,8.675091,-5.430108],[-9.753579,8.700871,-7.314684,-2.424641,8.762069,1.036260,-1.435293,-5.671595,7.743435,-2.330662],[-0.601165,-3.778435,9.257724,6.417298,-3.877657,-1.449057,7.212467,3.482153,6.927181,-4.503805],[4.694282,-6.451498,-1.889613,3.031798,-9.277800,-6.587432,0.862894,4.959990,-3.230617,5.605299],[3.524281,5.832032,-3.281222,-1.249719,-7.207966,-4.119757,-1.302953,1.773770,-2.949538,-4.059940],[1.123057,7.244846,6.459238,7.733043,4.988968,-8.219149,-4.805503,9.775696,-1.655632,-9.068701],[4.133699,5.433350,4.091581,-8.120237,6.096943,-6.541320,-3.062035,3.469683,0.605245,1.166945],[1.680768,9.727201,8.922548,-8.849989,-7.228752,8.922872,-0.750078,9.748335,4.770119,6.010404]]], dtype = "float64")#candidate|273|(1, 11, 10)|const|float64
uop_274 = relay.asinh(const_273.astype('float64')) # shape=(1, 11, 10)
bop_292 = relay.left_shift(uop_274.astype('uint16'), relay.reshape(const_273.astype('uint16'), relay.shape_of(uop_274))) # shape=(1, 11, 10)
output = bop_292
output2 = bop_292
func_298 = relay.Function([], output)
mod['func_298'] = func_298
mod = relay.transform.InferType()(mod)
mutated_mod['func_298'] = func_298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_298_call = mutated_mod.get_global_var('func_298')
call_299 = func_298_call()
output = call_299
func_300 = relay.Function([], output)
mutated_mod['func_300'] = func_300
mutated_mod = relay.transform.InferType()(mutated_mod)
var_307 = relay.var("var_307", dtype = "float64", shape = (8, 14, 4))#candidate|307|(8, 14, 4)|var|float64
const_308 = relay.const([[[-2.126119,9.139945,1.845245,1.296635],[5.216917,6.699304,-0.923039,0.934149],[-3.317616,-2.006647,5.324417,-1.214729],[-6.147586,-3.239625,4.474711,-8.488889],[9.511598,-6.833630,4.343357,-0.185111],[7.085852,-3.882357,1.275676,-6.760642],[-8.806371,-5.023476,3.000929,4.765124],[-2.912066,-6.150269,2.843206,8.812358],[-0.218356,-5.892528,5.834463,-8.535311],[-5.718533,-7.446763,-9.398661,7.185744],[-9.803297,6.529513,2.159291,1.263223],[-5.332588,5.427995,-1.067357,-4.496549],[-7.217195,-8.985930,-3.227664,4.527094],[7.646954,-7.647615,-2.985309,-2.246052]],[[-9.855345,-5.706892,8.199477,8.960702],[1.485311,3.692108,5.238078,-2.195339],[-3.562854,0.132378,-2.557265,-0.744031],[-2.574623,5.088610,-9.258480,9.649566],[4.148061,-9.482106,3.994494,-0.040864],[5.640171,5.368474,-8.044541,-5.651846],[-6.463135,7.431373,-2.074804,6.003960],[-4.109577,0.341308,-8.472453,7.032625],[-1.620552,-6.840773,6.066418,-3.117820],[5.298535,4.819058,-2.967621,-1.796779],[8.668243,9.968652,1.240074,3.141649],[1.418953,7.464364,3.002608,-2.145324],[-4.443466,-5.771333,1.771103,-2.025032],[-8.815156,-8.724503,-0.612690,0.079822]],[[-9.920267,0.375217,1.375195,-3.178826],[-0.791490,7.831278,-5.418259,2.914006],[-5.236391,6.054835,9.400991,-2.135816],[4.979446,-1.778127,-2.897851,-0.248599],[-8.645417,-1.821806,-3.686848,-9.718928],[-4.939141,-5.052401,7.931501,-2.545631],[9.629829,-6.842615,4.798409,-3.889467],[4.334027,-6.796820,6.715050,6.539888],[5.861438,8.472875,-1.683348,-7.867568],[1.688404,0.048748,-5.896999,9.516905],[7.573129,-9.837471,-6.571085,-0.035404],[1.031010,1.614516,2.480799,-4.707682],[4.062886,-7.270360,-2.497854,-4.901227],[1.913899,-8.699098,8.399150,-9.570799]],[[3.316408,-0.538925,7.975430,-9.755145],[5.044033,8.167286,-5.662276,7.762365],[-0.796624,8.166588,-7.328167,-4.930391],[0.835870,-0.047476,-8.048999,-1.485416],[4.208275,-7.352903,8.657873,-3.380779],[-9.206520,0.742699,8.533710,-2.354463],[-1.335177,-3.106862,-8.533513,-1.265756],[-6.915123,-8.041694,7.816352,-7.307709],[2.724952,-9.843160,6.766087,-2.281591],[-1.312457,-6.368475,-1.724855,9.070553],[-8.517028,-8.402443,6.215291,5.599799],[9.013224,-8.835678,-9.577480,0.852215],[1.209209,-3.381961,-2.162747,3.578122],[-7.905841,5.583539,-1.878701,2.670595]],[[-9.818164,1.298501,-3.973252,8.802555],[6.246191,9.444994,8.752532,1.498527],[-6.567284,0.626154,-0.105811,1.891537],[5.618499,-1.315881,-1.235521,-2.170232],[6.586288,-0.824435,-3.389128,1.758214],[2.392631,9.709036,7.468861,-1.862556],[-1.874701,8.763896,-8.386362,6.989825],[2.163147,7.121342,1.540253,-3.413219],[-3.419199,2.155542,0.731633,-6.217457],[9.287956,2.851654,-3.313875,-5.654193],[7.052251,-4.944128,-8.595706,3.040801],[0.710854,4.225386,0.463199,9.272263],[-7.876787,-7.676095,2.385257,9.137065],[3.456981,7.605284,-0.347970,-2.192924]],[[0.957817,8.636176,4.654206,2.257248],[4.145220,1.586604,2.461366,-9.834817],[9.923759,1.079904,5.047791,7.189912],[3.562609,4.988227,-0.875618,6.024453],[-6.408811,-4.804946,-9.168441,-9.785736],[-8.185227,-8.510288,-9.255153,-7.178894],[2.880906,-0.575460,-3.633244,2.840727],[-6.353498,3.181727,8.810638,1.792833],[4.529896,5.477812,0.485173,4.755826],[2.264274,2.416592,0.426185,-6.604001],[2.332611,8.272314,-5.558981,5.424382],[6.248632,-5.204565,-7.510848,-9.966220],[1.137288,9.072401,0.312738,-4.432609],[-2.175464,-9.765731,2.469355,-4.694202]],[[2.567941,-6.267023,8.300043,9.690175],[-0.440257,4.114197,4.539196,-8.150242],[8.945838,7.162332,8.119918,6.511409],[-8.607356,9.424178,-9.912308,-5.277915],[5.653297,-6.473227,6.326464,-7.815492],[6.074209,-6.603001,3.926039,9.723703],[-6.397929,-2.632494,-3.559682,4.277477],[6.867339,8.001501,-1.702776,-4.518079],[-4.316983,-3.289367,-5.980391,-6.533068],[-5.627499,-5.047501,7.944139,-2.345974],[-3.540849,6.186939,8.204063,5.305792],[3.297382,-7.988307,8.098560,-1.600703],[4.641030,6.657662,7.485194,0.147608],[-6.711348,8.480780,4.207539,0.679411]],[[-4.105414,6.651779,1.249227,0.267725],[0.361703,-4.188185,-2.499225,-1.821245],[-6.281825,6.876752,8.169409,2.242244],[-1.270612,-5.949615,9.004803,9.849712],[-9.307309,9.588493,-8.202582,0.899981],[-5.287956,-3.776150,-3.453554,2.072735],[-7.726500,-1.182212,0.021338,0.482512],[-0.020576,-7.183341,5.607957,-2.442156],[-9.677404,1.233446,-5.008825,-5.788015],[-7.558245,4.148021,9.720172,9.440478],[0.191072,-3.118691,-1.880103,-6.381323],[0.267018,-6.860486,-8.259721,-0.234399],[-7.227672,8.758140,-3.906494,3.471741],[-2.553355,7.828616,3.839575,0.583897]]], dtype = "float64")#candidate|308|(8, 14, 4)|const|float64
bop_309 = relay.floor_divide(var_307.astype('float64'), relay.reshape(const_308.astype('float64'), relay.shape_of(var_307))) # shape=(8, 14, 4)
func_298_call = mod.get_global_var('func_298')
func_300_call = mutated_mod.get_global_var('func_300')
call_316 = func_298_call()
call_317 = func_298_call()
uop_318 = relay.rsqrt(var_307.astype('float64')) # shape=(8, 14, 4)
bop_322 = relay.right_shift(uop_318.astype('int64'), relay.reshape(var_307.astype('int64'), relay.shape_of(uop_318))) # shape=(8, 14, 4)
output = relay.Tuple([bop_309,call_316,bop_322,])
output2 = relay.Tuple([bop_309,call_317,bop_322,])
func_330 = relay.Function([var_307,], output)
mod['func_330'] = func_330
mod = relay.transform.InferType()(mod)
var_331 = relay.var("var_331", dtype = "float64", shape = (8, 14, 4))#candidate|331|(8, 14, 4)|var|float64
output = func_330(var_331)
func_332 = relay.Function([var_331], output)
mutated_mod['func_332'] = func_332
mutated_mod = relay.transform.InferType()(mutated_mod)
func_298_call = mod.get_global_var('func_298')
func_300_call = mutated_mod.get_global_var('func_300')
call_358 = func_298_call()
call_359 = func_298_call()
output = call_358
output2 = call_359
func_364 = relay.Function([], output)
mod['func_364'] = func_364
mod = relay.transform.InferType()(mod)
mutated_mod['func_364'] = func_364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_364_call = mutated_mod.get_global_var('func_364')
call_365 = func_364_call()
output = call_365
func_366 = relay.Function([], output)
mutated_mod['func_366'] = func_366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_364_call = mod.get_global_var('func_364')
func_366_call = mutated_mod.get_global_var('func_366')
call_391 = func_364_call()
call_392 = func_364_call()
func_298_call = mod.get_global_var('func_298')
func_300_call = mutated_mod.get_global_var('func_300')
call_404 = func_298_call()
call_405 = func_298_call()
output = relay.Tuple([call_391,call_404,])
output2 = relay.Tuple([call_392,call_405,])
func_408 = relay.Function([], output)
mod['func_408'] = func_408
mod = relay.transform.InferType()(mod)
mutated_mod['func_408'] = func_408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_408_call = mutated_mod.get_global_var('func_408')
call_409 = func_408_call()
output = call_409
func_410 = relay.Function([], output)
mutated_mod['func_410'] = func_410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_298_call = mod.get_global_var('func_298')
func_300_call = mutated_mod.get_global_var('func_300')
call_425 = func_298_call()
call_426 = func_298_call()
uop_436 = relay.sinh(call_425.astype('float32')) # shape=(1, 11, 10)
uop_438 = relay.sinh(call_426.astype('float32')) # shape=(1, 11, 10)
func_364_call = mod.get_global_var('func_364')
func_366_call = mutated_mod.get_global_var('func_366')
call_439 = func_364_call()
call_440 = func_364_call()
output = relay.Tuple([uop_436,call_439,])
output2 = relay.Tuple([uop_438,call_440,])
func_448 = relay.Function([], output)
mod['func_448'] = func_448
mod = relay.transform.InferType()(mod)
output = func_448()
func_449 = relay.Function([], output)
mutated_mod['func_449'] = func_449
mutated_mod = relay.transform.InferType()(mutated_mod)
const_479 = relay.const([[[1.687102,2.536907,-3.364373,-7.477837,-8.302979,5.874919,-7.603202,-3.954120,0.626283,-6.837370]],[[5.705960,-1.931912,-7.260373,9.705346,1.717779,2.959229,9.356433,-8.160796,2.767563,6.652804]]], dtype = "float64")#candidate|479|(2, 1, 10)|const|float64
uop_480 = relay.acos(const_479.astype('float64')) # shape=(2, 1, 10)
output = relay.Tuple([uop_480,])
output2 = relay.Tuple([uop_480,])
func_497 = relay.Function([], output)
mod['func_497'] = func_497
mod = relay.transform.InferType()(mod)
output = func_497()
func_498 = relay.Function([], output)
mutated_mod['func_498'] = func_498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_448_call = mod.get_global_var('func_448')
func_449_call = mutated_mod.get_global_var('func_449')
call_606 = relay.TupleGetItem(func_448_call(), 1)
call_607 = relay.TupleGetItem(func_449_call(), 1)
func_497_call = mod.get_global_var('func_497')
func_498_call = mutated_mod.get_global_var('func_498')
call_613 = relay.TupleGetItem(func_497_call(), 0)
call_614 = relay.TupleGetItem(func_498_call(), 0)
output = relay.Tuple([call_606,call_613,])
output2 = relay.Tuple([call_607,call_614,])
func_620 = relay.Function([], output)
mod['func_620'] = func_620
mod = relay.transform.InferType()(mod)
mutated_mod['func_620'] = func_620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_620_call = mutated_mod.get_global_var('func_620')
call_621 = func_620_call()
output = call_621
func_622 = relay.Function([], output)
mutated_mod['func_622'] = func_622
mutated_mod = relay.transform.InferType()(mutated_mod)
const_625 = relay.const([[[-7,-5,9,-4,-6,9,-1,-5,-10,-8,-5],[-3,-1,4,-1,2,-2,-10,2,4,-4,7],[-5,-2,3,2,-10,5,-5,1,-3,-5,-1],[-4,3,-1,10,-2,2,2,8,3,10,1],[-8,3,-7,-6,5,9,7,-5,-8,4,1],[-5,-1,-6,8,-6,2,-10,8,-7,-6,-3],[6,2,4,-6,-3,5,9,4,-1,-6,10],[1,-9,-10,-5,-8,10,-7,-9,1,-3,-5],[-8,-2,9,-9,1,6,-8,-7,-1,4,-6],[-6,-5,6,-3,-10,1,-7,9,9,8,10]]], dtype = "int64")#candidate|625|(1, 10, 11)|const|int64
var_626 = relay.var("var_626", dtype = "int64", shape = (10, 10, 11))#candidate|626|(10, 10, 11)|var|int64
bop_627 = relay.right_shift(const_625.astype('int64'), var_626.astype('int64')) # shape=(10, 10, 11)
func_364_call = mod.get_global_var('func_364')
func_366_call = mutated_mod.get_global_var('func_366')
call_637 = func_364_call()
call_638 = func_364_call()
output = relay.Tuple([bop_627,call_637,])
output2 = relay.Tuple([bop_627,call_638,])
func_645 = relay.Function([var_626,], output)
mod['func_645'] = func_645
mod = relay.transform.InferType()(mod)
mutated_mod['func_645'] = func_645
mutated_mod = relay.transform.InferType()(mutated_mod)
var_646 = relay.var("var_646", dtype = "int64", shape = (10, 10, 11))#candidate|646|(10, 10, 11)|var|int64
func_645_call = mutated_mod.get_global_var('func_645')
call_647 = func_645_call(var_646)
output = call_647
func_648 = relay.Function([var_646], output)
mutated_mod['func_648'] = func_648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_448_call = mod.get_global_var('func_448')
func_449_call = mutated_mod.get_global_var('func_449')
call_655 = relay.TupleGetItem(func_448_call(), 0)
call_656 = relay.TupleGetItem(func_449_call(), 0)
uop_658 = relay.log(call_655.astype('float64')) # shape=(1, 11, 10)
uop_660 = relay.log(call_656.astype('float64')) # shape=(1, 11, 10)
output = uop_658
output2 = uop_660
func_661 = relay.Function([], output)
mod['func_661'] = func_661
mod = relay.transform.InferType()(mod)
mutated_mod['func_661'] = func_661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_661_call = mutated_mod.get_global_var('func_661')
call_662 = func_661_call()
output = call_662
func_663 = relay.Function([], output)
mutated_mod['func_663'] = func_663
mutated_mod = relay.transform.InferType()(mutated_mod)
func_408_call = mod.get_global_var('func_408')
func_410_call = mutated_mod.get_global_var('func_410')
call_696 = relay.TupleGetItem(func_408_call(), 1)
call_697 = relay.TupleGetItem(func_410_call(), 1)
var_698 = relay.var("var_698", dtype = "uint16", shape = (14, 11, 10))#candidate|698|(14, 11, 10)|var|uint16
bop_699 = relay.add(call_696.astype('uint64'), var_698.astype('uint64')) # shape=(14, 11, 10)
bop_702 = relay.add(call_697.astype('uint64'), var_698.astype('uint64')) # shape=(14, 11, 10)
output = relay.Tuple([bop_699,])
output2 = relay.Tuple([bop_702,])
func_709 = relay.Function([var_698,], output)
mod['func_709'] = func_709
mod = relay.transform.InferType()(mod)
var_710 = relay.var("var_710", dtype = "uint16", shape = (14, 11, 10))#candidate|710|(14, 11, 10)|var|uint16
output = func_709(var_710)
func_711 = relay.Function([var_710], output)
mutated_mod['func_711'] = func_711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_497_call = mod.get_global_var('func_497')
func_498_call = mutated_mod.get_global_var('func_498')
call_718 = relay.TupleGetItem(func_497_call(), 0)
call_719 = relay.TupleGetItem(func_498_call(), 0)
output = call_718
output2 = call_719
func_726 = relay.Function([], output)
mod['func_726'] = func_726
mod = relay.transform.InferType()(mod)
mutated_mod['func_726'] = func_726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_726_call = mutated_mod.get_global_var('func_726')
call_727 = func_726_call()
output = call_727
func_728 = relay.Function([], output)
mutated_mod['func_728'] = func_728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_448_call = mod.get_global_var('func_448')
func_449_call = mutated_mod.get_global_var('func_449')
call_747 = relay.TupleGetItem(func_448_call(), 1)
call_748 = relay.TupleGetItem(func_449_call(), 1)
output = relay.Tuple([call_747,])
output2 = relay.Tuple([call_748,])
func_749 = relay.Function([], output)
mod['func_749'] = func_749
mod = relay.transform.InferType()(mod)
mutated_mod['func_749'] = func_749
mutated_mod = relay.transform.InferType()(mutated_mod)
func_749_call = mutated_mod.get_global_var('func_749')
call_750 = func_749_call()
output = call_750
func_751 = relay.Function([], output)
mutated_mod['func_751'] = func_751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_448_call = mod.get_global_var('func_448')
func_449_call = mutated_mod.get_global_var('func_449')
call_769 = relay.TupleGetItem(func_448_call(), 0)
call_770 = relay.TupleGetItem(func_449_call(), 0)
output = call_769
output2 = call_770
func_773 = relay.Function([], output)
mod['func_773'] = func_773
mod = relay.transform.InferType()(mod)
output = func_773()
func_774 = relay.Function([], output)
mutated_mod['func_774'] = func_774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_448_call = mod.get_global_var('func_448')
func_449_call = mutated_mod.get_global_var('func_449')
call_798 = relay.TupleGetItem(func_448_call(), 1)
call_799 = relay.TupleGetItem(func_449_call(), 1)
func_709_call = mod.get_global_var('func_709')
func_711_call = mutated_mod.get_global_var('func_711')
const_811 = relay.const([-2,-8,-3,4,8,1,-1,8,2,-2,3,-8,-6,-1,3,-7,-3,10,9,-5,5,-2,2,-8,9,3,-10,4,5,4,-9,3,-7,7,4,-1,-9,7,-3,8,-7,-4,4,-4,3,-5,1,4,8,2,-5,-4,5,8,8,-10,6,3,-1,-9,5,5,-3,-3,-2,6,9,-2,3,2,5,-8,7,-5,6,-1,9,8,6,-6,8,6,1,-2,9,8,8,-8,-5,1,6,-6,-9,8,10,6,5,-7,-1,1,-5,-5,-4,7,-6,5,-2,9,-7,-9,-9,3,6,-10,-9,8,-9,8,-7,-5,5,7,10,1,10,-2,-4,5,-7,8,8,-1,-10,-2,-3,-2,-6,-4,-4,2,4,5,9,9,-8,3,2,5,-10,-8,6,1,-8,8,1,-6,-4,-4,-4,10,-9,-6,-6,4,-9,-10,2,-7,-6,4,5,-2,-2,3,-9,-8,7,-1,6,-8,8,8,-9,2,-9,1,-8,-2,-7,-8,9,5,9,-8,9,-10,6,-7,-2,-10,-7,7,-2,-8,6,-7,4,-3,-8,-8,9,-6,-5,-1,3,-1,10,8,7,-5,3,-9,4,10,3,10,5,10,-8,10,-10,-4,9,6,-9,8,-3,-1,-9,10,10,-5,-6,8,5,7,-8,-10,4,-2,7,9,7,6,2,9,7,-6,10,-9,1,-4,9,-8,10,-10,-10,-6,10,6,-9,3,-8,9,4,-4,-3,5,-2,7,-3,-6,5,-3,-5,6,-1,-10,-7,-10,4,-5,2,-1,3,6,-4,-10,-6,5,-9,5,-9,2,3,-4,-5,4,-8,-2,2,6,2,-6,-6,-2,-3,6,4,-5,-9,-4,9,-2,4,6,3,3,-8,6,3,9,-8,5,5,7,-8,-6,10,1,-1,-1,1,-2,4,-2,-9,-10,-8,-7,4,6,-8,8,-10,1,10,-10,5,-9,-1,5,-4,6,-1,-6,8,6,4,-3,2,8,5,4,-9,10,-6,1,-1,3,-2,6,8,-6,-5,9,-5,1,4,-10,8,6,-7,5,5,-2,4,-7,-2,-9,3,6,4,6,5,-4,7,9,6,-4,2,8,-3,-10,-7,4,6,6,9,9,-9,9,2,2,3,-1,-1,1,-1,9,-2,5,-4,10,-4,-9,2,9,-7,-2,-6,-5,1,10,-9,-9,3,2,5,-1,1,-2,-8,-6,3,-5,-2,-5,-6,-4,-6,-9,7,6,-1,2,5,-6,-6,-7,-2,-7,1,-9,9,-4,-4,-3,2,4,-6,-7,10,-3,-6,5,-1,4,8,-8,7,-1,-5,-4,4,10,4,-1,1,-1,4,-6,-2,-8,-6,-7,-10,-3,-5,-2,5,-10,-9,3,7,-10,-2,8,7,-4,4,-5,10,-9,-5,5,-3,8,8,-4,5,-7,-10,-9,-3,-1,4,1,-4,-10,-9,10,4,4,1,-6,-3,3,10,-2,7,-7,-7,-9,-9,1,-6,10,1,1,-5,10,1,-3,9,3,-9,9,1,9,6,7,-1,3,2,-5,4,5,9,8,5,4,-2,-10,-10,10,-8,-2,-4,2,1,-3,1,10,-9,-9,-10,6,7,-4,6,-5,-2,5,3,4,-5,9,-6,-7,7,-9,9,8,3,3,7,6,-6,-5,-10,-1,7,-2,-8,8,-7,2,-2,3,10,7,-5,-7,7,10,-3,4,-2,3,-7,5,7,1,-8,7,2,7,8,-10,10,-2,-2,2,-5,4,-7,-8,-8,6,-5,6,-6,7,-7,-8,-7,-9,-7,3,-10,-5,-9,3,-2,-5,-3,-6,-4,-2,-10,-9,1,7,2,1,8,1,9,-5,5,7,3,-7,-8,7,9,6,5,-9,3,9,6,-9,5,5,5,8,-9,4,-3,-5,8,-4,7,2,-3,-5,2,-5,9,-7,-6,-4,-1,2,1,8,-1,4,6,-1,-8,10,-2,7,7,-8,10,-7,2,6,-7,5,-9,-9,7,-3,-8,-3,2,-2,5,-3,5,5,-9,3,7,7,6,-10,10,8,-10,8,2,-10,-3,-9,5,6,-8,4,-6,3,9,-7,-9,-6,-7,-1,-8,3,6,-10,9,-6,6,2,1,7,1,8,10,-10,-2,-5,4,2,1,2,1,-7,-8,-10,-6,-8,3,-6,-1,10,-7,-4,3,2,1,6,-2,10,3,8,6,-6,-3,2,9,7,-6,-9,-8,-5,-5,-10,3,6,9,7,1,6,8,-7,-9,2,-7,4,-2,-6,-9,5,-6,10,-6,-3,-2,8,-9,6,-9,-5,9,-4,8,1,6,-9,-6,10,-8,8,3,10,1,10,-4,8,4,-6,4,10,-3,4,10,1,8,7,-5,3,-3,-8,8,2,-10,4,8,-3,5,-10,3,2,-1,3,8,-4,1,-9,9,-10,-10,2,10,-8,-5,9,-10,-9,4,10,10,-4,-7,-9,-4,5,7,1,3,2,8,5,-4,10,8,1,-4,-10,-10,7,-2,-10,-10,-6,-2,2,-2,7,-1,8,-7,-9,6,1,-10,1,-1,-9,-2,5,-5,-4,-5,-7,-8,-8,-3,-5,8,-4,4,-8,-6,7,6,-4,10,10,-10,2,3,2,-6,-5,-3,-1,-6,-2,-10,2,1,-6,3,4,4,-3,5,3,4,-6,-8,-4,9,-7,-2,-2,-3,4,4,-1,-6,-5,2,2,5,3,-8,6,-2,4,-9,9,-7,-2,-10,1,-9,-7,-4,5,9,-1,-4,4,-1,9,9,4,10,-8,8,8,-6,8,-6,-9,10,1,8,-1,-6,-9,-10,-10,10,3,-7,-5,6,7,6,-6,-8,4,4,5,6,4,8,6,-2,-5,-10,4,-6,7,-6,2,-1,10,-2,7,10,5,7,-7,10,10,4,5,6,4,4,6,10,5,2,9,-5,-3,6,3,-9,8,-8,3,-5,-6,3,-6,-9,-5,5,6,-10,4,6,-4,2,-10,2,-2,2,-6,1,8,-5,2,8,-9,6,4,3,-9,-9,3,2,-8,5,-9,-10,-6,-1,4,-6,-8,10,-6,-2,-8,-4,2,-10,10,8,2,8,2,6,-7,-3,-5,-8,6,6,9,-8,-5,3,4,7,-9,3,4,-9,2,-7,5,-9,-5,8,4,5,4,7,9,-7,-10,-10,-10,5,-1,10,-8,-8,6,7,1,1,1,-7,-3,9,-3,-6,-7,6,5,-5,-4,6,-8,10,-6,-7,9,9,6,-3,-6,3,-2,-3,-4,-10,3,8,8,3,1,2,1,1,-9,10,5,-1,2,-6,4,7,-1,-1,5,4,3,5,9,-3,2,4,-7,-6,10,-7,7,4,-1,6,8,-1,8,-6,3,7,-3,3,-7,10,3,4,3,6,2,9,4,2,7,-10,7,6,-8,1,1,5,-9,4,6,8,-3,-9,-9,10,-10,8,10,9,-6,5,10,-3,-6,2,8,9,9,8,-10,-5,1,-10,-1,8,7,-7,3,7,7,-3,-1,4,-4,-7,-5,7,-6,-8,3,-4,-1,-9,-1,8,-8,-10,-5,9,9,4,-8,1,-7,1,-4,2,8,-2,8,4,2,6,-10,-9,-3,-4,-3,5,3,9,2,5,-3,-8,8,8,8,7,1,7,-8,-4,-4,-2,4,-4,-5,6,-7,-10,6,5,5,10,-8,1,7,-9,-2,-10,4,-5,-5,8,5,7,7,-7,-3,-8,5,-9,3,-3,-8,-3,9,1,1,5,5,-9,-5,-5,-3,-1,10,-9,5,10,-7,6,-3,9,6,9,-8,-6,-5,3,-1,6,-2,4,9,3,-7,3,5,1,5,-3,-8,-8,-9,1,-3,9,4,-5,7,10,-6,-1,2,-2,-4,2,3,5,8,10,-4,1,6,10,3,-7,-4,9,2,5,-6,6,-6,1,-8,9,4,10,5,3,-4,8,9,-4,-1,-5,-5,-8,3,-6,2,4,5,-6,-8,10,-7,7,-6,-7,9,3,2,-6,-1,-9,-10,-9,-9,-5,3,-10,-4,8,-8,-6,-6,3,-2,-4,-1,-6,-6,-6,-1,5,-8,8,-1,-3,-1,6,-10,5,5,-5,-2,9,-7,6,-8], dtype = "uint16")#candidate|811|(1540,)|const|uint16
call_810 = relay.TupleGetItem(func_709_call(relay.reshape(const_811.astype('uint16'), [14, 11, 10])), 0)
call_812 = relay.TupleGetItem(func_711_call(relay.reshape(const_811.astype('uint16'), [14, 11, 10])), 0)
func_364_call = mod.get_global_var('func_364')
func_366_call = mutated_mod.get_global_var('func_366')
call_813 = func_364_call()
call_814 = func_364_call()
output = relay.Tuple([call_798,call_810,const_811,call_813,])
output2 = relay.Tuple([call_799,call_812,const_811,call_814,])
func_815 = relay.Function([], output)
mod['func_815'] = func_815
mod = relay.transform.InferType()(mod)
mutated_mod['func_815'] = func_815
mutated_mod = relay.transform.InferType()(mutated_mod)
func_815_call = mutated_mod.get_global_var('func_815')
call_816 = func_815_call()
output = call_816
func_817 = relay.Function([], output)
mutated_mod['func_817'] = func_817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_620_call = mod.get_global_var('func_620')
func_622_call = mutated_mod.get_global_var('func_622')
call_850 = relay.TupleGetItem(func_620_call(), 1)
call_851 = relay.TupleGetItem(func_622_call(), 1)
func_364_call = mod.get_global_var('func_364')
func_366_call = mutated_mod.get_global_var('func_366')
call_859 = func_364_call()
call_860 = func_364_call()
uop_869 = relay.tan(call_850.astype('float64')) # shape=(2, 1, 10)
uop_871 = relay.tan(call_851.astype('float64')) # shape=(2, 1, 10)
const_872 = relay.const([[[-8.650606,-7.122401,7.449926,-5.467862,-3.413790,-2.029398,-4.919359,7.669234,-0.841461,9.588242]],[[1.067006,-5.099080,1.789878,-1.456646,-9.665398,8.065223,-3.657160,7.123985,1.133967,-6.406494]]], dtype = "float64")#candidate|872|(2, 1, 10)|const|float64
bop_873 = relay.logical_xor(uop_869.astype('int64'), relay.reshape(const_872.astype('int64'), relay.shape_of(uop_869))) # shape=(2, 1, 10)
bop_876 = relay.logical_xor(uop_871.astype('int64'), relay.reshape(const_872.astype('int64'), relay.shape_of(uop_871))) # shape=(2, 1, 10)
uop_883 = relay.cos(call_859.astype('float32')) # shape=(1, 11, 10)
uop_885 = relay.cos(call_860.astype('float32')) # shape=(1, 11, 10)
output = relay.Tuple([bop_873,uop_883,])
output2 = relay.Tuple([bop_876,uop_885,])
func_898 = relay.Function([], output)
mod['func_898'] = func_898
mod = relay.transform.InferType()(mod)
mutated_mod['func_898'] = func_898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_898_call = mutated_mod.get_global_var('func_898')
call_899 = func_898_call()
output = call_899
func_900 = relay.Function([], output)
mutated_mod['func_900'] = func_900
mutated_mod = relay.transform.InferType()(mutated_mod)
func_364_call = mod.get_global_var('func_364')
func_366_call = mutated_mod.get_global_var('func_366')
call_923 = func_364_call()
call_924 = func_364_call()
var_946 = relay.var("var_946", dtype = "uint16", shape = (12, 11, 10))#candidate|946|(12, 11, 10)|var|uint16
bop_947 = relay.greater(call_923.astype('bool'), var_946.astype('bool')) # shape=(12, 11, 10)
bop_950 = relay.greater(call_924.astype('bool'), var_946.astype('bool')) # shape=(12, 11, 10)
bop_952 = relay.logical_xor(var_946.astype('uint8'), call_923.astype('uint8')) # shape=(12, 11, 10)
bop_955 = relay.logical_xor(var_946.astype('uint8'), call_924.astype('uint8')) # shape=(12, 11, 10)
func_773_call = mod.get_global_var('func_773')
func_774_call = mutated_mod.get_global_var('func_774')
call_957 = func_773_call()
call_958 = func_773_call()
uop_972 = relay.erf(call_957.astype('float32')) # shape=(1, 11, 10)
uop_974 = relay.erf(call_958.astype('float32')) # shape=(1, 11, 10)
bop_977 = relay.bitwise_and(bop_947.astype('int64'), relay.reshape(bop_952.astype('int64'), relay.shape_of(bop_947))) # shape=(12, 11, 10)
bop_980 = relay.bitwise_and(bop_950.astype('int64'), relay.reshape(bop_955.astype('int64'), relay.shape_of(bop_950))) # shape=(12, 11, 10)
func_645_call = mod.get_global_var('func_645')
func_648_call = mutated_mod.get_global_var('func_648')
const_995 = relay.const([-4,-9,-4,10,5,7,-5,-3,-3,6,-10,-7,4,-8,-2,10,-7,6,-2,-3,4,-6,-1,7,-4,7,6,5,-6,6,6,-5,-5,-6,9,-5,-9,3,9,-8,-5,-7,1,-4,-6,6,-6,-5,-1,-9,2,3,-4,3,-6,-8,-8,-5,8,-7,-10,4,-1,9,2,4,2,5,-6,3,1,-5,6,-9,9,-7,-6,-5,4,3,-1,-9,-6,1,3,6,-5,3,10,6,-6,8,-7,-1,6,6,2,-10,-8,-2,7,4,-6,-3,-9,-6,5,-8,-7,-3,4,-8,-3,-7,-9,5,-7,-8,-8,-9,-4,-1,-9,9,-10,6,-2,-2,-3,7,10,-8,10,9,-8,4,-5,9,6,1,10,1,4,-6,-2,10,6,-8,5,4,-6,-5,5,-5,6,8,5,-8,3,-7,1,-9,-7,-3,2,6,-8,-9,9,-6,1,-10,3,7,-6,-3,2,-3,-6,-1,-4,6,-10,-4,8,5,-2,-8,-5,-1,9,-7,5,-10,-6,1,10,1,2,-2,-3,-2,9,2,-4,4,-8,-6,3,-3,-9,-9,2,10,5,-6,8,-5,-9,3,-3,-9,-10,-3,-1,9,3,-8,8,-8,-1,-1,-4,5,7,-9,5,-1,-10,-7,3,10,6,10,7,4,6,-6,4,-6,-9,1,-10,10,-7,1,-5,-5,-9,4,6,-4,5,-3,-1,-2,-1,-8,-3,2,-7,1,6,-2,4,-10,6,-1,2,-2,10,-5,6,5,-2,-1,-2,3,-10,-2,3,-5,4,1,-7,-10,6,-1,9,-4,-2,1,9,1,-1,6,-3,-2,-4,-4,6,1,1,6,5,-2,7,1,7,7,-3,1,-3,-4,8,1,1,-7,1,2,-5,3,8,-6,-3,3,6,-3,-9,-8,-4,2,-1,10,4,8,-8,9,-2,-1,8,3,9,4,5,-6,3,8,7,-5,-2,8,1,-6,-2,10,-4,-5,10,-3,-5,8,7,1,-8,4,-9,-1,-10,3,-5,-2,-7,4,-10,6,5,3,-2,5,1,9,2,10,7,3,-8,3,-4,3,-3,9,-3,-2,-7,4,-6,9,2,-1,-7,-3,9,-10,-2,-9,2,-4,10,-1,-5,-4,9,-1,7,10,-4,8,-10,10,-1,-8,7,-9,10,-4,6,-5,3,6,8,1,2,7,8,-3,-6,-4,-4,10,5,-8,1,-6,1,-4,1,-1,5,-2,-7,1,-5,-8,8,-3,-3,-3,-4,1,-2,-4,-2,-5,-5,9,-3,5,5,-7,3,-7,-10,-3,1,2,10,-8,1,9,-10,5,-1,3,6,-1,9,5,8,8,3,3,-3,4,-4,-9,-1,8,-9,-8,-1,3,-6,-3,-6,4,-8,3,-7,9,-1,-6,5,4,6,-8,-2,-1,9,3,-5,-7,5,8,8,-5,-6,-1,6,-4,9,1,2,10,-6,-7,1,3,3,-9,-7,-7,-5,5,-4,-4,-10,4,7,-3,6,-3,3,2,7,6,6,-8,-4,2,3,-2,-3,7,10,-4,-10,-3,4,3,-7,-7,4,3,10,7,5,6,-6,9,-5,-10,1,9,9,7,1,-10,-9,5,2,3,-1,-5,-4,-3,-1,-3,8,-10,-6,-4,2,3,1,-3,10,-10,6,8,-4,-8,-3,9,-7,-8,-7,1,10,-1,4,4,9,-4,1,-5,-4,10,-8,-9,-8,-9,1,2,-5,-2,6,-10,-2,-10,-10,-8,9,-10,-8,1,7,-1,-7,-2,8,1,2,9,-8,6,3,10,3,7,2,7,6,-10,3,-7,-9,-6,-10,4,-5,7,6,10,-1,9,4,3,-4,-5,8,-9,-2,8,4,-1,-4,-7,-8,-8,-3,-2,-2,7,1,-4,-7,6,2,1,-7,4,-3,-2,7,1,8,7,8,8,9,8,7,-5,-1,-4,3,10,1,8,-1,-10,-10,-10,4,-10,10,-10,6,-5,-4,-5,-8,-4,6,-9,-8,-7,7,-9,-3,-3,-10,9,8,3,4,-10,3,-3,3,6,-10,-2,-10,7,3,-8,5,-9,3,7,-9,2,-1,1,-7,-5,-1,6,-9,9,-7,5,6,4,-7,9,-6,-10,-7,10,9,3,-4,3,5,7,9,-1,7,4,-6,2,3,-8,-10,-6,-6,10,9,-7,-3,6,6,5,-3,-9,-2,-1,-10,7,9,-10,-2,9,4,-6,10,-9,9,2,-4,1,10,5,2,4,5,8,-4,1,-3,-5,8,1,-9,-1,2,1,5,5,-7,-1,-3,-4,-8,-7,3,-5,-5,8,7,-8,-3,-4,4,6,-8,-8,5,-10,-6,-5,-8,-9,5,8,9,1,-5,-8,6,-2,10,5,-1,-8,1,-7,-2,-1,-6,-8,-5,6,-6,8,-8,-6,2,4,8,4,5,-10,8,5,10,-8,6,2,-6,-4,3,-5,-5,10,-10,5,-6,6,6,-7,-7,-1,6,-5,-6,-1,2,5,2,1,2,1,8,-3,1,1,4,10,-5,-6,-7,1,-2,7,6,8,-3,-7,6,-7,9,-6,-10,-6,-3,-10,-1,2,-9,-7,-6,-2,-4,9,-8,-9,-4,1,3,-1,-2,-9,-1,-6,9,-5,8,3,6,-4,-8,-1,-9,-8,-4,9,1,-8,-8,-5,6,1,9,8,5,10,-8,-8,7,-9,5,6,-7,-8,-9,-3,5,10,9,-9,-1,-10,4,-6,-3,2,5,6,4,-1,9,9,10,-5,-9,-5,-5,-9,-10,10,10,-1,-9,10,-3,6,5,-3,5,5,-4,6,3,8,10,7,7,-6,-7,10,7,9,3,6,1,4,2,-5,-3,8,-1,5,5,6,10,-1,4,-9,-3,7,-8,1,10,3,-1,9,6,-1,5,-2,-5,-2,-4,-8,-5,2,5,-3,1,10,-7,-5,-1,5,-4,-1], dtype = "int64")#candidate|995|(1100,)|const|int64
call_994 = relay.TupleGetItem(func_645_call(relay.reshape(const_995.astype('int64'), [10, 10, 11])), 0)
call_996 = relay.TupleGetItem(func_648_call(relay.reshape(const_995.astype('int64'), [10, 10, 11])), 0)
func_620_call = mod.get_global_var('func_620')
func_622_call = mutated_mod.get_global_var('func_622')
call_997 = relay.TupleGetItem(func_620_call(), 1)
call_998 = relay.TupleGetItem(func_622_call(), 1)
var_999 = relay.var("var_999", dtype = "uint8", shape = (12, 11, 10))#candidate|999|(12, 11, 10)|var|uint8
bop_1000 = relay.logical_or(bop_952.astype('bool'), relay.reshape(var_999.astype('bool'), relay.shape_of(bop_952))) # shape=(12, 11, 10)
bop_1003 = relay.logical_or(bop_955.astype('bool'), relay.reshape(var_999.astype('bool'), relay.shape_of(bop_955))) # shape=(12, 11, 10)
func_661_call = mod.get_global_var('func_661')
func_663_call = mutated_mod.get_global_var('func_663')
call_1008 = func_661_call()
call_1009 = func_661_call()
output = relay.Tuple([uop_972,bop_977,call_994,const_995,call_997,bop_1000,call_1008,])
output2 = relay.Tuple([uop_974,bop_980,call_996,const_995,call_998,bop_1003,call_1009,])
func_1018 = relay.Function([var_946,var_999,], output)
mod['func_1018'] = func_1018
mod = relay.transform.InferType()(mod)
mutated_mod['func_1018'] = func_1018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1018_call = mutated_mod.get_global_var('func_1018')
var_1020 = relay.var("var_1020", dtype = "uint16", shape = (12, 11, 10))#candidate|1020|(12, 11, 10)|var|uint16
var_1021 = relay.var("var_1021", dtype = "uint8", shape = (12, 11, 10))#candidate|1021|(12, 11, 10)|var|uint8
call_1019 = func_1018_call(var_1020,var_1021,)
output = call_1019
func_1022 = relay.Function([var_1020,var_1021,], output)
mutated_mod['func_1022'] = func_1022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_898_call = mod.get_global_var('func_898')
func_900_call = mutated_mod.get_global_var('func_900')
call_1052 = relay.TupleGetItem(func_898_call(), 1)
call_1053 = relay.TupleGetItem(func_900_call(), 1)
output = relay.Tuple([call_1052,])
output2 = relay.Tuple([call_1053,])
func_1055 = relay.Function([], output)
mod['func_1055'] = func_1055
mod = relay.transform.InferType()(mod)
output = func_1055()
func_1056 = relay.Function([], output)
mutated_mod['func_1056'] = func_1056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1055_call = mod.get_global_var('func_1055')
func_1056_call = mutated_mod.get_global_var('func_1056')
call_1254 = relay.TupleGetItem(func_1055_call(), 0)
call_1255 = relay.TupleGetItem(func_1056_call(), 0)
func_364_call = mod.get_global_var('func_364')
func_366_call = mutated_mod.get_global_var('func_366')
call_1256 = func_364_call()
call_1257 = func_364_call()
func_1018_call = mod.get_global_var('func_1018')
func_1022_call = mutated_mod.get_global_var('func_1022')
var_1265 = relay.var("var_1265", dtype = "uint16", shape = (1320,))#candidate|1265|(1320,)|var|uint16
call_1264 = relay.TupleGetItem(func_1018_call(relay.reshape(var_1265.astype('uint16'), [12, 11, 10]), relay.reshape(var_1265.astype('uint8'), [12, 11, 10]), ), 1)
call_1266 = relay.TupleGetItem(func_1022_call(relay.reshape(var_1265.astype('uint16'), [12, 11, 10]), relay.reshape(var_1265.astype('uint8'), [12, 11, 10]), ), 1)
output = relay.Tuple([call_1254,call_1256,call_1264,var_1265,])
output2 = relay.Tuple([call_1255,call_1257,call_1266,var_1265,])
func_1267 = relay.Function([var_1265,], output)
mod['func_1267'] = func_1267
mod = relay.transform.InferType()(mod)
var_1268 = relay.var("var_1268", dtype = "uint16", shape = (1320,))#candidate|1268|(1320,)|var|uint16
output = func_1267(var_1268)
func_1269 = relay.Function([var_1268], output)
mutated_mod['func_1269'] = func_1269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_661_call = mod.get_global_var('func_661')
func_663_call = mutated_mod.get_global_var('func_663')
call_1301 = func_661_call()
call_1302 = func_661_call()
func_298_call = mod.get_global_var('func_298')
func_300_call = mutated_mod.get_global_var('func_300')
call_1305 = func_298_call()
call_1306 = func_298_call()
uop_1330 = relay.sigmoid(call_1301.astype('float64')) # shape=(1, 11, 10)
uop_1332 = relay.sigmoid(call_1302.astype('float64')) # shape=(1, 11, 10)
output = relay.Tuple([call_1305,uop_1330,])
output2 = relay.Tuple([call_1306,uop_1332,])
func_1350 = relay.Function([], output)
mod['func_1350'] = func_1350
mod = relay.transform.InferType()(mod)
output = func_1350()
func_1351 = relay.Function([], output)
mutated_mod['func_1351'] = func_1351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_497_call = mod.get_global_var('func_497')
func_498_call = mutated_mod.get_global_var('func_498')
call_1377 = relay.TupleGetItem(func_497_call(), 0)
call_1378 = relay.TupleGetItem(func_498_call(), 0)
func_620_call = mod.get_global_var('func_620')
func_622_call = mutated_mod.get_global_var('func_622')
call_1381 = relay.TupleGetItem(func_620_call(), 1)
call_1382 = relay.TupleGetItem(func_622_call(), 1)
bop_1396 = relay.subtract(call_1381.astype('int64'), relay.reshape(call_1377.astype('int64'), relay.shape_of(call_1381))) # shape=(2, 1, 10)
bop_1399 = relay.subtract(call_1382.astype('int64'), relay.reshape(call_1378.astype('int64'), relay.shape_of(call_1382))) # shape=(2, 1, 10)
bop_1400 = relay.not_equal(call_1377.astype('bool'), relay.reshape(bop_1396.astype('bool'), relay.shape_of(call_1377))) # shape=(2, 1, 10)
bop_1403 = relay.not_equal(call_1378.astype('bool'), relay.reshape(bop_1399.astype('bool'), relay.shape_of(call_1378))) # shape=(2, 1, 10)
const_1415 = relay.const([[[False,True,True,False,False,False,True,False,True,True],[True,True,True,True,False,False,True,False,False,False],[False,False,False,False,True,False,False,False,True,False],[False,True,True,True,True,True,True,False,True,False],[True,False,False,False,False,False,False,True,False,False],[True,False,False,True,True,True,True,True,False,False],[False,False,True,True,False,False,True,True,False,False],[False,True,True,False,True,True,False,True,False,False],[False,True,True,False,True,False,False,False,True,False]],[[True,True,False,False,True,False,True,False,False,True],[False,False,True,True,False,False,False,False,False,False],[False,False,False,True,False,True,True,False,True,True],[False,False,False,True,True,True,True,False,True,True],[True,False,True,False,True,True,True,False,True,True],[False,False,True,False,True,True,True,True,False,True],[False,False,True,False,True,False,False,True,False,True],[False,False,True,False,False,True,True,True,True,True],[False,True,True,True,False,False,True,True,True,True]]], dtype = "bool")#candidate|1415|(2, 9, 10)|const|bool
bop_1416 = relay.bitwise_or(bop_1400.astype('int16'), const_1415.astype('int16')) # shape=(2, 9, 10)
bop_1419 = relay.bitwise_or(bop_1403.astype('int16'), const_1415.astype('int16')) # shape=(2, 9, 10)
output = bop_1416
output2 = bop_1419
func_1429 = relay.Function([], output)
mod['func_1429'] = func_1429
mod = relay.transform.InferType()(mod)
output = func_1429()
func_1430 = relay.Function([], output)
mutated_mod['func_1430'] = func_1430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_448_call = mod.get_global_var('func_448')
func_449_call = mutated_mod.get_global_var('func_449')
call_1440 = relay.TupleGetItem(func_448_call(), 0)
call_1441 = relay.TupleGetItem(func_449_call(), 0)
func_645_call = mod.get_global_var('func_645')
func_648_call = mutated_mod.get_global_var('func_648')
var_1445 = relay.var("var_1445", dtype = "int64", shape = (1100,))#candidate|1445|(1100,)|var|int64
call_1444 = relay.TupleGetItem(func_645_call(relay.reshape(var_1445.astype('int64'), [10, 10, 11])), 0)
call_1446 = relay.TupleGetItem(func_648_call(relay.reshape(var_1445.astype('int64'), [10, 10, 11])), 0)
func_898_call = mod.get_global_var('func_898')
func_900_call = mutated_mod.get_global_var('func_900')
call_1449 = relay.TupleGetItem(func_898_call(), 0)
call_1450 = relay.TupleGetItem(func_900_call(), 0)
output = relay.Tuple([call_1440,call_1444,var_1445,call_1449,])
output2 = relay.Tuple([call_1441,call_1446,var_1445,call_1450,])
func_1466 = relay.Function([var_1445,], output)
mod['func_1466'] = func_1466
mod = relay.transform.InferType()(mod)
mutated_mod['func_1466'] = func_1466
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1467 = relay.var("var_1467", dtype = "int64", shape = (1100,))#candidate|1467|(1100,)|var|int64
func_1466_call = mutated_mod.get_global_var('func_1466')
call_1468 = func_1466_call(var_1467)
output = call_1468
func_1469 = relay.Function([var_1467], output)
mutated_mod['func_1469'] = func_1469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_620_call = mod.get_global_var('func_620')
func_622_call = mutated_mod.get_global_var('func_622')
call_1474 = relay.TupleGetItem(func_620_call(), 0)
call_1475 = relay.TupleGetItem(func_622_call(), 0)
output = relay.Tuple([call_1474,])
output2 = relay.Tuple([call_1475,])
func_1490 = relay.Function([], output)
mod['func_1490'] = func_1490
mod = relay.transform.InferType()(mod)
mutated_mod['func_1490'] = func_1490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1490_call = mutated_mod.get_global_var('func_1490')
call_1491 = func_1490_call()
output = call_1491
func_1492 = relay.Function([], output)
mutated_mod['func_1492'] = func_1492
mutated_mod = relay.transform.InferType()(mutated_mod)
func_898_call = mod.get_global_var('func_898')
func_900_call = mutated_mod.get_global_var('func_900')
call_1566 = relay.TupleGetItem(func_898_call(), 0)
call_1567 = relay.TupleGetItem(func_900_call(), 0)
uop_1581 = relay.log2(call_1566.astype('float64')) # shape=(2, 1, 10)
uop_1583 = relay.log2(call_1567.astype('float64')) # shape=(2, 1, 10)
bop_1586 = relay.floor_mod(uop_1581.astype('float64'), relay.reshape(call_1566.astype('float64'), relay.shape_of(uop_1581))) # shape=(2, 1, 10)
bop_1589 = relay.floor_mod(uop_1583.astype('float64'), relay.reshape(call_1567.astype('float64'), relay.shape_of(uop_1583))) # shape=(2, 1, 10)
bop_1591 = relay.maximum(uop_1581.astype('uint32'), relay.reshape(bop_1586.astype('uint32'), relay.shape_of(uop_1581))) # shape=(2, 1, 10)
bop_1594 = relay.maximum(uop_1583.astype('uint32'), relay.reshape(bop_1589.astype('uint32'), relay.shape_of(uop_1583))) # shape=(2, 1, 10)
const_1595 = relay.const([[[1.218330,7.457883,-6.746570,1.465636,4.349039,-1.441520,6.616608,-6.388804,-7.395794,8.721174],[-4.647860,8.126998,-5.239550,9.754593,-7.584776,1.815119,5.230224,-6.005622,-5.067014,4.318406],[5.540730,1.085017,-7.437010,-5.733653,3.276693,7.320687,-7.684125,-1.237315,-1.348774,-1.876259],[-5.860329,2.828861,-5.967341,-3.720394,1.429845,-3.182330,1.462871,0.472260,4.991498,8.408336],[-8.129559,-6.342131,8.890219,0.089324,-3.044414,-5.048633,1.889839,-5.856901,-0.627507,-4.153174],[8.766524,-3.058496,-8.042009,-6.485854,5.487075,-8.442182,-4.277093,-4.690009,6.041498,0.194798],[1.481599,9.970302,5.369577,-1.874646,-0.439033,-0.391872,1.274677,-4.984516,-0.898362,-6.921456],[-6.668531,6.071155,5.404415,4.078752,8.164586,1.212210,-7.123883,-3.531559,-3.771904,2.416292]],[[5.689977,-3.719193,-6.326530,8.239437,1.388133,-4.563062,-0.855003,-0.511808,-5.326832,4.304601],[6.439730,-0.116526,8.652086,1.156981,-2.445513,-6.182442,-9.929256,-5.681122,9.578294,-4.627442],[7.431996,8.793193,-5.443654,-6.003067,2.036289,8.745266,-3.690527,-3.263819,-5.216648,1.990632],[3.783393,-2.527860,2.348682,-1.569194,-4.515905,5.440015,-2.948143,-9.660039,5.367419,2.545382],[-6.016283,4.203812,-3.003837,-1.447271,8.888480,3.186452,7.584596,4.602902,5.374689,9.468087],[-4.198726,1.986669,3.571875,2.265099,-0.519841,4.521530,0.120014,1.119691,7.094529,-8.332672],[-8.854368,3.824062,-7.809362,-9.085340,-1.670698,6.298260,-4.635829,7.047233,-1.229486,-7.986658],[5.098308,5.732866,-6.811903,2.824024,-2.336034,4.452108,4.807942,-8.814396,6.854052,2.524299]]], dtype = "float64")#candidate|1595|(2, 8, 10)|const|float64
bop_1596 = relay.logical_xor(uop_1581.astype('uint8'), const_1595.astype('uint8')) # shape=(2, 8, 10)
bop_1599 = relay.logical_xor(uop_1583.astype('uint8'), const_1595.astype('uint8')) # shape=(2, 8, 10)
output = relay.Tuple([bop_1591,bop_1596,])
output2 = relay.Tuple([bop_1594,bop_1599,])
func_1600 = relay.Function([], output)
mod['func_1600'] = func_1600
mod = relay.transform.InferType()(mod)
output = func_1600()
func_1601 = relay.Function([], output)
mutated_mod['func_1601'] = func_1601
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1675 = relay.const([[-1.139474,-7.928053,0.054681,0.402554,6.015735,9.137054],[-9.441308,-0.025954,-2.702537,-3.164029,-6.081434,-2.640852],[-6.451922,9.853840,-1.177572,-8.444544,-5.836661,3.531261]], dtype = "float64")#candidate|1675|(3, 6)|const|float64
uop_1676 = relay.asin(const_1675.astype('float64')) # shape=(3, 6)
output = uop_1676
output2 = uop_1676
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
func_1600_call = mod.get_global_var('func_1600')
func_1601_call = mutated_mod.get_global_var('func_1601')
call_1704 = relay.TupleGetItem(func_1600_call(), 1)
call_1705 = relay.TupleGetItem(func_1601_call(), 1)
func_448_call = mod.get_global_var('func_448')
func_449_call = mutated_mod.get_global_var('func_449')
call_1706 = relay.TupleGetItem(func_448_call(), 1)
call_1707 = relay.TupleGetItem(func_449_call(), 1)
func_1698_call = mod.get_global_var('func_1698')
func_1700_call = mutated_mod.get_global_var('func_1700')
call_1711 = func_1698_call()
call_1712 = func_1698_call()
output = relay.Tuple([call_1704,call_1706,call_1711,])
output2 = relay.Tuple([call_1705,call_1707,call_1712,])
func_1714 = relay.Function([], output)
mod['func_1714'] = func_1714
mod = relay.transform.InferType()(mod)
mutated_mod['func_1714'] = func_1714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1714_call = mutated_mod.get_global_var('func_1714')
call_1715 = func_1714_call()
output = call_1715
func_1716 = relay.Function([], output)
mutated_mod['func_1716'] = func_1716
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1490_call = mod.get_global_var('func_1490')
func_1492_call = mutated_mod.get_global_var('func_1492')
call_1737 = relay.TupleGetItem(func_1490_call(), 0)
call_1738 = relay.TupleGetItem(func_1492_call(), 0)
output = call_1737
output2 = call_1738
func_1739 = relay.Function([], output)
mod['func_1739'] = func_1739
mod = relay.transform.InferType()(mod)
output = func_1739()
func_1740 = relay.Function([], output)
mutated_mod['func_1740'] = func_1740
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1490_call = mod.get_global_var('func_1490')
func_1492_call = mutated_mod.get_global_var('func_1492')
call_1752 = relay.TupleGetItem(func_1490_call(), 0)
call_1753 = relay.TupleGetItem(func_1492_call(), 0)
func_330_call = mod.get_global_var('func_330')
func_332_call = mutated_mod.get_global_var('func_332')
var_1756 = relay.var("var_1756", dtype = "float64", shape = (448,))#candidate|1756|(448,)|var|float64
call_1755 = relay.TupleGetItem(func_330_call(relay.reshape(var_1756.astype('float64'), [8, 14, 4])), 1)
call_1757 = relay.TupleGetItem(func_332_call(relay.reshape(var_1756.astype('float64'), [8, 14, 4])), 1)
func_773_call = mod.get_global_var('func_773')
func_774_call = mutated_mod.get_global_var('func_774')
call_1768 = func_773_call()
call_1769 = func_773_call()
func_815_call = mod.get_global_var('func_815')
func_817_call = mutated_mod.get_global_var('func_817')
call_1773 = relay.TupleGetItem(func_815_call(), 2)
call_1774 = relay.TupleGetItem(func_817_call(), 2)
const_1798 = relay.const([[[-8.870690,-0.158824,7.698766,-9.508269,2.027484,2.607848,6.721747,8.831685,-6.694133,-6.356644],[6.192634,3.893966,-2.267574,-4.297680,3.787151,6.328686,-6.214927,-9.938763,4.931859,-3.133481],[7.215330,7.237907,8.039451,-8.280852,-7.816767,-9.080940,4.064948,-5.686414,-7.878551,6.497240],[3.763644,-5.619888,-2.735651,9.950092,5.515871,-4.731593,8.976339,-1.078580,-4.754101,-1.103719],[7.641075,4.847213,-3.864724,-4.499122,-1.392816,-2.410414,-5.994410,7.444618,-6.087653,8.990596],[-7.408358,-8.293395,1.393088,8.364581,-2.149522,8.348530,-8.895999,-4.367963,-4.656773,-5.148285],[3.791083,-9.937136,0.502044,-0.186078,-9.711129,7.969814,-0.440720,-6.525702,-7.288996,1.813240],[7.595295,-4.090457,4.433318,3.620320,-0.599700,-2.332278,-0.961614,3.173337,6.692384,6.470786],[8.204464,-2.581788,8.702218,-9.988756,-5.863745,-3.008136,-1.944181,-6.659016,1.293286,1.535111],[0.471527,7.990459,5.432210,6.289939,3.463558,-1.345771,8.839669,-1.922848,-9.741296,0.438287],[-9.434655,-0.498554,-4.779065,2.998798,-6.736754,7.577409,-2.174958,-9.613874,-8.911072,-0.201816]],[[-3.343965,-6.251071,-3.256952,-4.848500,0.584669,6.713430,5.173190,-9.431168,-4.376544,-1.709750],[5.278590,-7.381901,-0.060785,7.467258,-2.262328,-1.000197,-9.912076,6.082977,0.158503,7.502120],[3.626429,5.064308,8.676738,-2.323103,4.870909,-7.872212,6.838216,-1.612890,4.508560,-2.360808],[-2.931521,4.539881,4.407215,1.785624,-4.040380,-9.463565,2.292895,7.756068,0.711583,4.536142],[-4.108054,6.888516,-8.469724,2.345352,3.858555,-6.090463,3.337737,8.223409,-1.471556,4.396716],[9.994608,-1.700546,1.817018,7.633631,1.058751,5.286598,7.280930,9.774541,7.739084,7.690364],[-8.442023,-0.379581,6.813865,1.767797,-4.298047,2.608752,-9.812055,-8.797256,3.389821,-2.791870],[-4.790244,-8.003632,3.327293,-1.446770,-9.638729,1.736201,2.002218,-6.548869,1.417222,-5.640913],[8.025163,-5.455415,7.514393,7.731637,-9.765863,1.725381,-9.172277,-6.888564,-6.869632,-0.727123],[4.300431,3.568675,3.782101,7.632013,5.685931,-9.319114,5.541360,-3.946497,0.071196,8.060246],[-6.314920,7.001393,-2.485764,-9.256499,-4.676220,-3.544571,-6.940106,-4.108675,4.109399,7.993086]],[[7.676080,2.491339,-8.809121,3.739949,-8.472815,4.969638,6.037098,1.533637,1.602997,-7.796044],[-8.912922,8.937086,9.600067,-2.874238,8.210642,6.325535,2.959269,-4.805896,1.526464,7.296561],[-5.016706,-8.801911,1.361346,-4.417544,2.429399,-1.271638,6.063048,-0.055371,4.301275,0.135106],[-1.802559,5.505002,-8.800271,2.455760,3.576659,3.011495,-2.553484,-6.637054,4.497160,-9.414833],[9.493089,-9.745983,-7.552250,2.427384,8.680736,-9.882110,-6.291464,8.215286,6.339627,-0.322757],[4.526083,4.063337,3.085312,-3.075392,-5.997883,6.821023,5.081070,-3.881410,-6.279015,-5.172138],[-6.450324,-3.284893,-9.281872,3.550163,-3.301037,0.624105,9.342838,5.234071,-3.081832,7.708766],[-2.756218,-6.352011,-3.624298,9.893478,9.386330,-1.743878,6.383076,-0.672076,-3.134708,8.374286],[5.748525,6.413856,5.391680,0.416859,-2.353328,-5.138226,5.621650,-3.094973,0.374989,-9.174400],[4.185436,4.905742,1.234344,2.769454,0.256686,8.148245,0.093256,-8.613050,4.386972,-8.834658],[-6.465424,3.675205,3.168904,-4.324557,9.966437,0.397300,1.173098,1.262618,-0.277976,8.354631]],[[-7.897222,-3.352015,1.083307,-5.917513,-6.590096,-3.895445,-6.823529,-4.430461,7.270599,-8.468896],[-5.469376,-9.153157,-0.008193,-0.656084,-3.808059,2.494208,-9.807730,-6.473594,-2.093390,0.556014],[3.065419,5.221882,0.134934,3.588259,-5.770413,8.405235,-2.790965,9.132314,-6.461045,4.914858],[4.701619,2.267438,0.669936,1.778342,-4.649309,-3.426778,-8.045505,6.277259,-5.994607,-7.841105],[0.014834,5.350192,4.916070,-9.524850,-5.408717,-0.099494,-1.654068,-6.123342,3.502071,9.754930],[-2.901062,8.563284,-3.359689,-5.804104,-0.256891,4.120373,-5.122666,6.562598,5.206674,1.028621],[6.514402,9.591150,6.040407,6.698323,4.739975,9.169665,2.159609,-5.883458,1.442549,-9.931157],[-2.736081,9.059648,-9.505261,-3.488045,6.882260,9.465763,-7.692859,-0.682077,-0.261155,-9.501679],[1.254553,2.076498,3.606011,-6.331553,-6.829071,-2.016132,-3.679901,-0.877918,-2.328471,8.767696],[-3.608699,-8.148409,7.277202,1.500644,4.571199,-1.141794,8.338310,3.729008,1.009777,5.479784],[-2.219076,-8.553295,-0.632404,6.918176,-8.533526,-0.170230,2.572095,6.555669,0.580187,1.394232]],[[-7.314494,4.405207,0.647817,-7.920007,-1.045813,6.630273,0.019598,-2.135005,-6.408325,-7.389976],[-9.903460,2.681385,-6.102406,-5.131235,4.900962,-7.585201,6.224622,4.951813,-1.085177,-6.163672],[-5.937711,2.837278,6.256356,7.125974,6.972608,-0.840427,-9.284054,0.465564,-6.307656,-3.770238],[8.818859,-9.612653,5.325647,-7.763550,1.101584,-3.821204,-9.796662,-7.499873,8.262219,8.994643],[5.711753,-2.827941,3.931085,-2.959609,-4.893649,-6.299628,6.722970,-7.056735,-3.243648,-7.790314],[2.414575,6.592063,-2.881955,-2.166111,6.952818,-6.812803,7.527145,-8.846226,5.905935,8.431290],[-4.012035,4.421830,-8.739545,-3.901484,-0.708537,-1.775693,6.793933,7.165099,8.986590,-7.799081],[9.779015,-7.066650,3.935317,-5.711082,6.675207,-3.027743,1.610181,-2.188300,-4.243201,-0.069533],[2.351860,-0.390439,0.377766,9.354577,6.354088,4.743168,-6.235361,-6.744671,6.920325,-5.104002],[-2.300191,-1.697284,8.734383,7.761047,5.889688,-0.034143,-2.896928,8.278861,1.380369,9.465702],[-1.027784,9.216592,-0.528887,3.900349,-0.457162,-1.413886,-8.460432,-1.316103,1.298340,8.281619]],[[-6.116155,-3.407256,3.784580,-0.823550,-5.161302,8.890156,-2.645904,4.217164,-5.683581,-5.527430],[9.185975,4.917863,2.690448,4.338079,8.139940,2.920508,-4.359929,8.076092,-1.154127,-3.647225],[9.433512,1.102830,7.387836,-8.061148,9.104593,-0.195010,7.429915,3.477123,-1.175079,-2.998331],[4.593735,6.876351,0.214215,3.315137,-5.061727,-5.350781,-8.084220,0.263388,-8.651568,3.489386],[3.912908,-1.981161,-0.092262,4.034758,-2.650310,-4.773879,-8.177938,-0.740323,-1.439419,9.292117],[4.921548,-5.349462,8.432020,3.224779,2.869317,-9.489735,4.476093,-5.126056,-1.618290,-4.463716],[3.167147,-6.340396,-7.768783,4.389639,2.621574,2.564630,-6.073985,-6.684362,3.812459,1.560155],[-0.256647,3.544341,0.790869,7.993739,-6.737604,-0.888655,3.985467,1.514924,2.798993,-3.209236],[8.051895,-3.930772,-6.668523,3.085982,-0.207255,-3.066378,-9.387752,-6.127015,5.645822,8.792056],[8.351180,9.385523,6.020698,-0.089728,8.846664,7.161739,-5.201590,-5.710666,-4.196900,3.254437],[2.626901,8.686537,0.668586,5.502166,-7.684554,-8.122577,-2.454430,-6.610743,-7.545842,5.236121]],[[0.915194,-1.363824,-7.781136,-6.726424,4.064934,3.076929,-4.677102,-8.134063,5.660267,-8.913048],[0.415759,5.994657,8.829132,3.544502,2.450788,5.021839,8.297768,-2.105178,4.447536,-2.287843],[-6.004334,3.143189,-8.010505,0.750577,9.865549,0.469113,-3.312364,-9.013325,-8.725570,-0.334307],[-6.231063,8.427413,9.127103,7.912312,-2.816456,0.375229,-6.126690,9.220638,1.081983,-8.815893],[5.772663,4.771523,-9.715021,0.256874,3.132335,-5.023791,9.630067,8.725133,-4.093368,2.570414],[-0.467464,2.568149,5.208490,0.095726,0.591482,0.029352,-0.043896,6.914587,4.374914,0.877223],[-9.624547,-3.103640,1.950707,-9.198335,8.072400,3.393581,0.337386,-9.285756,2.545658,3.593421],[7.533947,6.982001,6.806542,-5.633493,5.130360,5.210559,-2.763693,-3.629248,8.322269,2.762748],[-0.616066,-9.061794,0.387598,0.520402,-9.788588,-9.583454,6.525160,0.550432,-2.751771,0.607611],[-2.062835,2.157375,5.020414,-7.172131,-6.935259,8.395186,-1.675893,-5.303368,-7.792260,3.668185],[-3.941599,-4.419744,4.073779,-3.438015,3.427934,-1.289215,-1.163618,-5.253546,9.895640,-6.080852]],[[-8.192744,-1.830824,6.818826,1.466660,-8.091822,5.394219,-4.501427,2.239462,3.270589,1.277098],[6.238232,-5.568305,5.716485,0.938917,-7.491569,-5.780059,2.123198,6.047715,-0.858975,-2.268692],[4.629966,4.704399,7.998681,-3.917681,4.929939,-3.591830,9.100307,-7.695119,2.457694,2.296673],[-6.853354,5.832255,-1.669653,-5.811025,4.094611,-5.299253,-2.610124,-1.413238,-5.569398,5.354950],[-8.412361,-2.345297,-0.688539,-2.672747,7.083649,6.300153,3.510704,9.126609,-8.952972,-0.574535],[9.632080,-2.680585,4.165021,6.164198,1.738626,3.569217,-8.727541,6.184180,-8.951079,3.938673],[4.483035,2.497694,4.359659,3.911399,7.968701,6.665149,-4.211499,-1.463922,-1.973105,1.215125],[-2.203275,4.007733,-3.434987,-0.303059,-9.418427,-0.975199,-4.117869,-9.223198,8.223064,6.355245],[-4.900855,5.622824,1.149404,-0.282756,1.841304,3.994355,-6.648114,6.176623,-4.227213,2.630729],[1.899805,-5.032269,-9.364220,1.622441,-1.355909,-3.120990,9.471992,4.534283,6.131114,-2.137299],[9.136113,6.350605,-7.087891,4.011288,-2.889808,3.064659,-8.379425,7.644671,-0.854754,-5.550453]],[[-2.514700,0.027403,-5.840434,-1.164153,-0.070123,3.855979,-1.902720,6.365181,1.558330,8.488528],[-9.154053,5.064800,8.493236,8.232064,7.989304,-2.690805,-2.020842,7.217590,3.748108,-5.605219],[-3.477410,1.190755,-5.237884,8.066515,6.146410,9.674574,1.473219,0.188923,-3.834794,-6.314635],[-9.486593,4.922413,9.761063,-9.728735,-2.251612,-7.497286,-2.772354,8.797511,5.459012,-5.782112],[-5.369468,-4.493311,-8.113535,-4.248436,-1.481580,-7.307162,6.957242,2.367719,-0.665976,9.380764],[-7.358883,2.804038,-5.946842,-8.036942,9.973709,-6.712243,-1.186869,1.130173,-4.753285,2.701233],[-4.265018,-2.439357,0.382049,-7.226702,1.488763,-1.102393,-8.987205,-2.503531,2.302272,-4.128841],[8.095263,-7.186943,0.538336,-9.419272,2.977511,-2.007441,6.558218,2.320325,-0.423208,-1.075117],[-8.191232,3.323331,-0.292440,6.766706,-5.066203,-6.068254,-5.259302,-2.699238,-2.247160,-9.579124],[-5.085523,1.323158,8.915749,1.989684,9.383181,4.647622,-9.974201,-4.714594,-7.491551,-1.977011],[7.838072,-8.889242,1.151946,5.007915,4.792239,7.116904,-1.539108,2.078262,-8.807435,9.993852]],[[-1.097456,6.370154,7.063650,4.478880,1.865817,4.546207,-5.502608,-3.754098,-8.881518,0.114753],[0.476842,1.334786,8.606908,9.725166,3.378578,6.014007,3.855561,3.891151,-0.819538,-8.023097],[-2.925461,-3.047811,2.929429,6.312274,-0.677059,7.167166,6.432071,5.420852,8.071802,-1.955388],[7.106521,-5.067555,-5.489356,-9.688200,-5.791841,-1.882838,-8.156168,2.864132,-8.700409,2.017774],[0.530214,-8.086974,2.194649,-1.841405,8.120807,-8.729036,-5.829583,0.910171,-1.058944,-6.330606],[7.961188,7.844310,2.788500,8.127831,2.526532,6.899094,-6.866363,-9.813986,0.968419,-2.890672],[3.294237,-2.194800,-3.247327,3.716136,0.799984,1.687709,-0.501518,-4.241727,-0.731737,4.406065],[-6.752672,-3.077703,5.048883,-3.805171,1.283847,6.540403,2.939093,0.045755,7.132025,-5.149663],[-2.523599,7.046254,2.300220,-8.043924,-9.351373,6.756706,-5.103890,3.481003,-2.597252,6.512425],[-6.129524,0.617721,-3.523666,8.438402,8.896537,-1.799022,-4.158554,-5.209749,2.624231,1.412367],[7.605665,-0.384159,-7.448240,1.365137,4.312228,7.690260,6.532258,-3.172620,6.462324,4.531716]],[[8.871192,-8.267189,-3.641042,7.024644,2.942254,1.849421,-0.494703,4.988882,6.452137,5.043068],[4.914485,-3.979784,8.419716,-1.781308,9.202392,6.828778,6.877822,-8.293591,5.880652,0.903734],[-1.086731,0.160271,-7.272512,3.670823,3.600364,-8.877219,6.360212,6.109482,2.021035,8.979719],[5.679815,-2.970648,-4.069441,-5.856268,-0.999004,0.541967,-8.917627,6.701992,5.420653,-1.159025],[-8.576208,7.764359,-2.493764,-2.529549,-5.490588,-6.779787,3.818264,-5.812538,5.685378,9.112107],[-6.690459,-4.375233,7.698838,7.218911,-9.273022,3.542662,-6.289688,5.832260,1.250826,4.050615],[9.069668,7.158752,-7.656238,8.173385,3.721123,1.381392,9.255413,-7.545557,-1.601540,7.374219],[-3.509904,9.111767,6.742190,8.524120,-4.676643,-8.953414,-4.359818,-5.711664,6.986650,-3.925814],[-5.903266,-4.608440,0.648220,-8.829568,-9.008967,-8.692293,-5.852546,5.629021,-6.489079,-3.254809],[8.950472,1.742684,9.050244,-4.097269,0.249215,5.141326,4.871454,5.076007,-9.639681,-4.494376],[7.175272,8.132128,-6.167305,4.570870,7.739668,4.974518,-8.527954,-3.422016,0.141828,-1.707342]],[[3.772669,-4.134261,0.843799,9.016519,-3.217351,-2.574197,5.993540,8.405514,-6.681534,-5.197009],[1.355180,1.045556,-2.308441,3.890845,-3.970163,-2.528815,3.008497,-0.887944,-6.330217,-1.634936],[0.521636,-7.721566,4.721301,-8.279750,-2.228011,5.943721,3.400131,1.058845,2.515158,3.116838],[-0.555780,7.972490,-7.607000,-2.162776,-8.413622,5.889648,4.648229,-1.863015,-5.145915,8.607177],[1.643368,-1.788534,2.719578,9.432642,-3.019151,-8.461651,-0.001265,-6.213116,-7.289041,-8.728638],[0.821500,-2.259159,0.275056,3.955235,-5.039078,7.487147,-9.178757,-3.406359,9.441190,-7.126272],[-5.311289,3.941113,-6.469056,3.759837,-1.307722,6.983158,-3.131356,5.866809,-2.895424,7.057929],[7.735404,4.534867,-2.415265,6.509870,5.218358,9.371593,-5.521180,-1.568561,-9.093767,3.591358],[2.283718,-4.334512,3.137193,-0.288924,2.404822,-9.075686,-6.793339,-0.462376,5.530572,-0.243681],[2.240504,-3.112170,-9.417766,-3.717816,-6.204124,-0.667955,0.145502,1.700699,-4.127885,-7.338840],[2.812549,-7.957993,-6.951410,-2.118293,-1.553489,-8.194194,-2.008456,2.921913,-6.366216,6.609381]],[[-4.532852,-4.213718,1.081456,-7.058458,1.363725,8.025266,9.111973,-6.531374,-6.243674,3.052010],[-5.508947,-9.671944,-2.183314,2.222737,5.557196,5.192763,-5.895691,3.428019,-7.052626,7.124445],[4.760009,-3.892161,-6.242350,-2.525472,-5.344785,5.322148,-6.740791,9.335677,-0.889826,4.864617],[-2.433774,8.249612,-3.230941,-0.254638,-6.283450,4.312155,-9.462353,-2.000829,-6.347162,7.934835],[-6.641462,9.982009,-1.946149,6.100887,-0.189520,-5.203073,4.916146,0.793366,1.384857,-5.461385],[-7.060587,1.924860,-5.946824,8.498122,-2.454851,0.823833,-7.421230,0.543888,3.355617,8.542428],[0.444143,-5.330140,0.550959,7.416768,8.852475,-2.160958,4.848515,-2.220599,8.217906,-6.518998],[-6.208896,-9.103488,2.884695,0.527507,-5.768272,-7.780708,5.029825,-2.647638,-3.559214,2.586747],[-5.015639,3.065804,4.045639,9.388269,-8.678924,-1.538961,0.044157,0.655497,0.742416,7.095573],[3.098727,0.220146,8.724504,6.281503,9.352325,4.793365,-6.743555,7.903614,1.596797,-2.064909],[2.285390,-4.321090,2.662715,2.086930,8.159208,-7.104955,-3.551488,2.577279,7.474983,9.879602]],[[3.594738,-0.118548,-9.972110,3.221474,-7.074880,8.224224,-8.101532,-9.707866,3.343688,-6.978403],[7.915990,7.174749,1.422751,6.878981,9.020594,6.646099,0.929266,-5.007757,-8.410716,8.734204],[2.634426,-8.996324,9.660764,5.430583,-7.073560,8.013445,-8.611496,7.154000,2.197584,-6.161966],[3.124927,1.759485,-4.209654,-9.223399,7.030601,5.846142,-8.519903,-9.968815,6.008381,-4.641770],[-8.391361,6.766365,-9.106929,-8.797226,7.525487,-3.206906,-5.673580,8.834054,5.596500,9.575150],[-2.075168,5.114756,-0.616010,-7.029742,5.837137,9.350403,-6.589136,-3.337884,6.307109,-0.042458],[-0.157282,-0.306126,-4.467716,3.765999,9.878971,-2.673875,7.826831,5.446615,7.012746,8.121546],[-6.776311,-9.026648,0.565157,-8.057491,1.865006,7.114730,7.682841,6.744124,-7.962370,-3.557794],[5.078654,6.553684,-0.062664,8.221903,-6.130354,5.215661,0.638888,7.781995,-1.628500,-6.184716],[-3.149382,9.401643,8.312502,8.296326,7.005712,4.110496,-4.481468,-2.504004,2.839292,-5.087899],[-2.106174,9.307193,-8.572410,2.186765,-5.713339,-0.180772,3.927754,-6.129411,-5.175520,-8.168460]],[[9.130541,1.008441,-5.641882,3.779759,6.885170,5.271546,3.714689,4.930753,7.336880,-1.118339],[-9.598870,-5.412920,3.111464,-1.664290,-9.497069,5.159408,5.442050,3.668342,-7.921002,7.810788],[2.714780,-1.784326,8.021643,-7.644838,-7.854066,-5.520273,4.501986,-3.308306,-9.380996,2.384031],[-1.771636,-4.629469,1.537698,1.093081,-2.230114,7.853842,-2.388405,-6.180675,4.277774,-2.186569],[-8.201642,3.726664,-3.894620,-7.854239,-7.287530,1.805719,-0.731872,-6.516891,-1.051226,-4.809098],[9.483913,-5.428757,6.673457,8.592235,5.974460,-3.395433,8.645011,8.793760,7.204148,-4.170592],[7.161173,-1.891782,7.091604,5.313268,1.879546,0.152527,8.848400,-9.322731,-5.828858,-3.608104],[6.486164,4.225225,-4.364842,-8.111018,-6.182992,7.987512,1.080064,-0.465771,2.962747,-5.024603],[2.183604,9.431393,3.397728,0.616375,4.525448,4.553025,-2.416230,4.986756,7.327792,-3.044364],[-3.137541,-6.049758,-5.956766,2.012294,-1.263989,-3.080438,2.649506,0.295281,3.754280,-9.770915],[-9.328239,8.765334,1.648538,4.055786,9.929925,-7.027868,4.018960,3.390319,2.433218,6.597869]]], dtype = "float32")#candidate|1798|(15, 11, 10)|const|float32
bop_1799 = relay.bitwise_or(call_1768.astype('uint8'), const_1798.astype('uint8')) # shape=(15, 11, 10)
bop_1802 = relay.bitwise_or(call_1769.astype('uint8'), const_1798.astype('uint8')) # shape=(15, 11, 10)
func_1018_call = mod.get_global_var('func_1018')
func_1022_call = mutated_mod.get_global_var('func_1022')
var_1811 = relay.var("var_1811", dtype = "uint16", shape = (1320,))#candidate|1811|(1320,)|var|uint16
call_1810 = relay.TupleGetItem(func_1018_call(relay.reshape(var_1811.astype('uint16'), [12, 11, 10]), relay.reshape(var_1811.astype('uint8'), [12, 11, 10]), ), 3)
call_1812 = relay.TupleGetItem(func_1022_call(relay.reshape(var_1811.astype('uint16'), [12, 11, 10]), relay.reshape(var_1811.astype('uint8'), [12, 11, 10]), ), 3)
output = relay.Tuple([call_1752,call_1755,var_1756,call_1773,bop_1799,call_1810,var_1811,])
output2 = relay.Tuple([call_1753,call_1757,var_1756,call_1774,bop_1802,call_1812,var_1811,])
func_1819 = relay.Function([var_1756,var_1811,], output)
mod['func_1819'] = func_1819
mod = relay.transform.InferType()(mod)
var_1820 = relay.var("var_1820", dtype = "float64", shape = (448,))#candidate|1820|(448,)|var|float64
var_1821 = relay.var("var_1821", dtype = "uint16", shape = (1320,))#candidate|1821|(1320,)|var|uint16
output = func_1819(var_1820,var_1821,)
func_1822 = relay.Function([var_1820,var_1821,], output)
mutated_mod['func_1822'] = func_1822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_749_call = mod.get_global_var('func_749')
func_751_call = mutated_mod.get_global_var('func_751')
call_1845 = relay.TupleGetItem(func_749_call(), 0)
call_1846 = relay.TupleGetItem(func_751_call(), 0)
uop_1851 = relay.sin(call_1845.astype('float32')) # shape=(1, 11, 10)
uop_1853 = relay.sin(call_1846.astype('float32')) # shape=(1, 11, 10)
output = uop_1851
output2 = uop_1853
func_1862 = relay.Function([], output)
mod['func_1862'] = func_1862
mod = relay.transform.InferType()(mod)
output = func_1862()
func_1863 = relay.Function([], output)
mutated_mod['func_1863'] = func_1863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_298_call = mod.get_global_var('func_298')
func_300_call = mutated_mod.get_global_var('func_300')
call_1867 = func_298_call()
call_1868 = func_298_call()
func_815_call = mod.get_global_var('func_815')
func_817_call = mutated_mod.get_global_var('func_817')
call_1883 = relay.TupleGetItem(func_815_call(), 2)
call_1884 = relay.TupleGetItem(func_817_call(), 2)
output = relay.Tuple([call_1867,call_1883,])
output2 = relay.Tuple([call_1868,call_1884,])
func_1890 = relay.Function([], output)
mod['func_1890'] = func_1890
mod = relay.transform.InferType()(mod)
output = func_1890()
func_1891 = relay.Function([], output)
mutated_mod['func_1891'] = func_1891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1600_call = mod.get_global_var('func_1600')
func_1601_call = mutated_mod.get_global_var('func_1601')
call_1955 = relay.TupleGetItem(func_1600_call(), 1)
call_1956 = relay.TupleGetItem(func_1601_call(), 1)
func_364_call = mod.get_global_var('func_364')
func_366_call = mutated_mod.get_global_var('func_366')
call_1969 = func_364_call()
call_1970 = func_364_call()
output = relay.Tuple([call_1955,call_1969,])
output2 = relay.Tuple([call_1956,call_1970,])
func_1981 = relay.Function([], output)
mod['func_1981'] = func_1981
mod = relay.transform.InferType()(mod)
mutated_mod['func_1981'] = func_1981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1981_call = mutated_mod.get_global_var('func_1981')
call_1982 = func_1981_call()
output = call_1982
func_1983 = relay.Function([], output)
mutated_mod['func_1983'] = func_1983
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1739_call = mod.get_global_var('func_1739')
func_1740_call = mutated_mod.get_global_var('func_1740')
call_2054 = func_1739_call()
call_2055 = func_1739_call()
var_2072 = relay.var("var_2072", dtype = "uint16", shape = (2, 11, 10))#candidate|2072|(2, 11, 10)|var|uint16
bop_2073 = relay.floor_divide(call_2054.astype('float32'), var_2072.astype('float32')) # shape=(2, 11, 10)
bop_2076 = relay.floor_divide(call_2055.astype('float32'), var_2072.astype('float32')) # shape=(2, 11, 10)
func_1714_call = mod.get_global_var('func_1714')
func_1716_call = mutated_mod.get_global_var('func_1716')
call_2087 = relay.TupleGetItem(func_1714_call(), 0)
call_2088 = relay.TupleGetItem(func_1716_call(), 0)
func_1698_call = mod.get_global_var('func_1698')
func_1700_call = mutated_mod.get_global_var('func_1700')
call_2096 = func_1698_call()
call_2097 = func_1698_call()
func_1490_call = mod.get_global_var('func_1490')
func_1492_call = mutated_mod.get_global_var('func_1492')
call_2098 = relay.TupleGetItem(func_1490_call(), 0)
call_2099 = relay.TupleGetItem(func_1492_call(), 0)
func_1819_call = mod.get_global_var('func_1819')
func_1822_call = mutated_mod.get_global_var('func_1822')
const_2103 = relay.const([[3.500046],[0.886674],[4.659015],[6.996794],[6.957877],[1.329714],[3.349359],[-6.799948],[-8.711310],[-0.675104],[-7.598485],[-5.201061],[9.484929],[-2.201868],[-5.752042],[1.596603],[5.949459],[2.614075],[5.798635],[3.887951],[6.887386],[5.506959],[-5.353657],[-7.693260],[-0.555371],[-3.885524],[3.926192],[-6.397698],[-9.344039],[-5.175299],[2.678413],[4.673547],[-3.982048],[3.048928],[0.530883],[-5.117198],[7.611734],[7.009633],[6.771829],[5.623661],[-0.900610],[-9.138058],[-0.052270],[-8.140342],[-5.884579],[3.119280],[-3.708070],[-1.553681],[-1.251011],[-1.709027],[-6.301342],[-3.379424],[5.299561],[0.019010],[1.540938],[-5.035421],[-4.662080],[5.731153],[7.200201],[-7.298531],[-1.423083],[7.918945],[-7.758227],[3.709911],[-9.300800],[-9.349693],[-6.427220],[-0.514103],[-4.281128],[-3.531893],[-4.278583],[7.384033],[-6.600992],[-9.721471],[-0.931273],[4.637993],[-3.528438],[-5.024594],[-8.358022],[7.141497],[8.703049],[2.213089],[-5.476105],[9.572007],[-8.567948],[2.836803],[-7.068371],[0.829206],[4.609736],[-0.036766],[-5.130176],[8.742094],[2.781066],[7.334333],[5.067982],[-1.507346],[-2.948384],[6.019875],[6.163366],[1.514089],[-8.124481],[9.670705],[2.266028],[4.306277],[-4.053982],[5.792568],[7.542017],[9.210860],[-0.392347],[-6.146258],[-3.749283],[-3.553057],[0.027478],[9.220756],[8.035288],[-9.535721],[9.905071],[-7.108791],[-2.643436],[-7.375700],[-8.523193],[-9.317521],[-8.750999],[-6.453978],[-7.874470],[-7.738904],[3.616013],[-3.730702],[-5.065338],[5.349130],[-3.559803],[-4.563504],[1.898846],[5.001918],[-0.462398],[-0.920173],[9.578725],[7.812154],[3.380359],[-0.026282],[-6.280721],[-9.758218],[3.953022],[-0.922345],[-4.624529],[5.972472],[7.432263],[8.618920],[0.479784],[5.476296],[-3.679582],[-9.971583],[-8.744741],[5.913658],[7.533939],[2.966902],[-1.631272],[6.557436],[-9.224277],[-6.843901],[1.989333],[-2.803840],[0.087693],[-2.274371],[-2.859464],[-8.240289],[9.488097],[-9.784056],[-3.719239],[3.225609],[3.871021],[-4.112512],[-0.050888],[7.056840],[1.233818],[-2.389405],[-6.975084],[-2.144850],[-6.693773],[-1.419601],[-2.348302],[1.459067],[1.168687],[3.532134],[1.962625],[9.503849],[7.910732],[-7.103777],[8.206412],[0.183434],[2.247580],[5.733473],[-5.152687],[7.598962],[-9.924636],[4.621020],[8.329913],[2.362463],[-3.248254],[-2.461649],[0.918590],[-1.705910],[3.553334],[9.850731],[-1.757781],[-9.963460],[-5.766946],[9.131426],[6.009026],[2.178783],[-2.423227],[-1.692657],[8.245540],[-6.935276],[-5.040054],[8.952783],[-6.177394],[-3.279060],[-0.954371],[-9.040472],[-4.407983],[4.899450],[9.984262],[3.648734],[9.348623],[-4.299313],[0.392851],[1.988409],[-4.488773],[-7.414120],[9.891896],[7.195220],[0.791396],[4.527369],[8.732131],[4.259419],[-9.547588],[-6.183824],[2.834256],[-7.790726],[-0.131484],[1.781758],[7.745256],[-8.919225],[-6.672685],[-8.269733],[-5.938315],[-9.568900],[-7.607627],[1.486272],[1.291229],[1.680289],[5.389208],[2.021640],[-6.362268],[-5.739020],[7.013158],[-1.311004],[-0.429186],[-5.353175],[-2.847917],[-1.140893],[-2.912684],[-0.626694],[4.948485],[-9.025182],[-2.235066],[-5.354123],[6.120449],[3.721550],[-2.692256],[-3.720369],[5.384148],[-9.658402],[4.180915],[-6.554003],[-6.947203],[-1.527437],[7.949193],[3.402480],[0.414040],[-4.159152],[7.737098],[5.736085],[-1.438914],[-3.824040],[-2.441497],[-7.530834],[-0.429722],[-9.436607],[-4.705169],[7.883129],[0.926138],[0.324241],[-1.155973],[7.723212],[2.118461],[-9.197818],[1.841809],[6.751677],[-1.391621],[-3.923154],[7.349123],[-0.776112],[1.150589],[5.433627],[1.229634],[-1.222055],[4.225567],[-3.837493],[-4.301547],[5.809346],[5.912295],[3.660571],[7.268819],[-0.248484],[-5.585741],[2.412410],[-5.150090],[5.682399],[-0.231897],[6.055664],[0.658017],[-0.860778],[4.563137],[3.425855],[9.183386],[3.200549],[-1.869045],[2.637885],[-5.382942],[5.199125],[-2.570385],[-1.278687],[-9.961666],[-4.045211],[-8.210016],[-3.827779],[-0.551482],[-9.329199],[5.937945],[3.430685],[-3.606115],[5.604802],[5.733443],[8.846062],[8.762563],[8.814889],[1.463863],[-6.385937],[9.289794],[-5.654982],[-9.382298],[-6.962496],[2.692757],[-4.296675],[-2.241589],[5.356796],[8.394220],[3.183118],[4.684708],[-8.966861],[6.378795],[-5.119108],[5.027751],[-9.590602],[-7.066554],[-9.090829],[7.902653],[0.742607],[-0.139091],[-2.620059],[4.794711],[6.331582],[-7.609853],[-0.298507],[7.382649],[-3.296634],[-3.527373],[6.625198],[9.092961],[-4.711266],[-3.870690],[-0.278804],[1.526936],[4.952895],[-1.651658],[-3.167713],[8.777314],[-3.355545],[-7.874169],[-2.999616],[6.725053],[-1.934034],[9.033545],[2.874526],[4.185119],[-2.433450],[-6.940962],[-3.131007],[-2.138177],[3.247044],[7.143120],[9.764695],[-1.834502],[-9.225343],[-3.272698],[-5.644720],[-6.510945],[7.244963],[5.477875],[-9.493674],[-9.820758],[-9.746412],[-3.797329],[6.068080],[-6.239357],[0.042344],[-4.931298],[6.002847],[-0.506663],[-4.723614],[-7.105733],[-6.623792],[0.570258],[-2.300916],[-2.580413],[-3.104957],[-1.296218],[2.387921],[8.992229],[6.046120],[-4.573324],[1.767842],[8.260082],[2.928366],[-0.493213],[-4.973227],[-4.508754],[9.026221],[-5.011556],[-7.472746],[1.938490],[-4.716983],[-7.442074],[-2.516838],[-2.386186],[7.619350]], dtype = "float64")#candidate|2103|(448, 1)|const|float64
var_2104 = relay.var("var_2104", dtype = "uint16", shape = (1320,))#candidate|2104|(1320,)|var|uint16
call_2102 = relay.TupleGetItem(func_1819_call(relay.reshape(const_2103.astype('float64'), [448,]), relay.reshape(var_2104.astype('uint16'), [1320,]), ), 2)
call_2105 = relay.TupleGetItem(func_1822_call(relay.reshape(const_2103.astype('float64'), [448,]), relay.reshape(var_2104.astype('uint16'), [1320,]), ), 2)
output = relay.Tuple([bop_2073,call_2087,call_2096,call_2098,call_2102,const_2103,var_2104,])
output2 = relay.Tuple([bop_2076,call_2088,call_2097,call_2099,call_2105,const_2103,var_2104,])
func_2106 = relay.Function([var_2072,var_2104,], output)
mod['func_2106'] = func_2106
mod = relay.transform.InferType()(mod)
mutated_mod['func_2106'] = func_2106
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2106_call = mutated_mod.get_global_var('func_2106')
var_2108 = relay.var("var_2108", dtype = "uint16", shape = (2, 11, 10))#candidate|2108|(2, 11, 10)|var|uint16
var_2109 = relay.var("var_2109", dtype = "uint16", shape = (1320,))#candidate|2109|(1320,)|var|uint16
call_2107 = func_2106_call(var_2108,var_2109,)
output = call_2107
func_2110 = relay.Function([var_2108,var_2109,], output)
mutated_mod['func_2110'] = func_2110
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2112 = relay.const([[[True,False,False,True,False,True,True,True,True,False,False,True,True,False],[False,True,True,True,False,False,False,True,False,False,True,False,False,False],[False,True,False,True,True,False,False,True,False,True,False,True,True,True],[False,False,True,True,True,False,False,True,False,False,False,False,True,True],[False,True,True,False,False,True,True,True,False,True,False,False,False,True]],[[True,False,False,False,False,True,True,False,True,True,True,True,False,False],[True,True,True,False,False,True,False,False,False,False,True,False,True,True],[False,False,False,False,False,False,False,False,True,True,False,False,False,False],[True,False,False,True,True,True,True,True,False,True,True,True,True,False],[True,True,False,False,True,False,False,True,True,False,True,False,True,False]],[[True,True,False,False,False,False,True,True,True,False,True,False,False,False],[True,True,True,False,False,True,False,True,True,False,False,False,False,False],[True,True,False,False,True,False,False,True,False,False,False,True,False,True],[True,False,False,False,False,True,True,False,False,True,False,True,False,False],[False,False,False,True,False,False,True,True,False,True,False,False,True,False]],[[False,False,False,True,False,False,False,False,True,True,True,True,False,True],[False,False,True,False,True,False,True,True,False,False,False,True,False,False],[True,True,False,True,True,False,True,False,False,True,False,True,False,True],[False,False,False,True,True,False,True,False,False,True,True,False,True,True],[True,True,True,True,True,True,False,False,False,True,False,False,False,True]],[[False,False,False,False,True,True,True,False,True,True,False,True,False,True],[True,True,False,True,True,True,False,False,False,False,False,False,False,True],[True,False,False,True,True,False,True,False,True,True,False,False,False,False],[True,False,True,True,True,True,False,False,False,False,False,False,False,True],[True,False,False,False,True,False,True,False,False,False,False,False,True,False]],[[False,True,False,False,True,True,True,True,False,True,True,False,True,False],[False,True,True,True,False,True,True,True,True,False,True,True,True,True],[True,False,True,False,False,True,False,True,False,True,False,False,False,False],[False,True,False,False,False,True,False,False,False,True,True,True,False,False],[False,True,True,False,True,False,False,True,True,False,True,True,True,True]],[[True,True,True,True,False,True,False,False,False,False,True,False,True,False],[True,True,True,False,False,False,False,False,True,False,True,False,False,False],[False,True,False,True,False,True,True,False,True,True,False,True,True,True],[False,False,False,True,False,True,True,False,True,True,False,False,True,False],[True,True,False,True,False,False,False,False,False,True,False,True,False,True]],[[False,True,False,False,False,False,False,False,True,True,False,True,True,True],[True,False,True,False,False,True,True,False,False,False,True,False,True,True],[True,False,False,True,True,True,False,True,True,False,True,True,True,False],[False,False,True,True,True,False,False,True,True,True,True,True,True,False],[True,True,False,False,True,False,False,False,True,False,False,True,False,True]],[[False,True,True,False,False,False,True,True,False,True,False,False,True,True],[True,False,False,True,True,False,True,False,False,True,True,False,True,True],[True,True,False,True,True,False,True,True,False,False,False,True,False,False],[True,True,True,False,True,True,True,True,True,True,True,False,False,False],[False,False,True,True,True,False,False,False,False,True,True,False,True,True]],[[True,True,True,False,False,True,True,False,False,False,True,False,True,False],[False,False,True,False,False,False,True,True,False,True,False,False,False,True],[True,True,True,False,True,False,True,True,True,False,True,False,False,False],[False,False,True,False,False,False,False,False,False,True,True,True,False,True],[True,False,True,False,True,False,True,False,False,False,False,False,False,True]],[[False,False,False,False,False,True,False,False,True,False,False,True,True,False],[False,True,True,False,True,False,False,False,False,True,True,True,True,True],[True,True,False,True,False,False,True,False,True,True,True,False,True,True],[False,False,True,False,True,True,False,False,True,True,False,False,False,True],[True,False,False,False,True,True,True,True,True,False,False,True,True,True]],[[True,False,False,True,False,False,False,True,True,False,True,False,True,True],[False,False,True,True,False,True,True,True,False,False,True,False,False,True],[True,True,False,False,True,False,False,True,False,False,False,True,False,True],[False,False,True,False,False,False,False,False,True,True,True,False,False,False],[False,False,True,True,False,True,True,True,False,True,True,False,True,True]],[[False,False,True,False,False,False,False,False,False,False,False,True,False,True],[True,False,False,True,False,True,False,False,True,False,False,True,True,True],[True,True,False,True,True,True,True,True,True,False,True,True,False,True],[True,False,False,False,False,False,False,True,False,False,True,True,False,True],[False,False,False,True,True,True,True,False,False,False,True,False,False,False]],[[True,True,True,False,True,True,True,False,False,True,True,False,True,False],[True,False,False,True,False,False,False,True,True,True,True,False,False,False],[False,False,False,True,True,True,False,True,False,True,True,False,False,False],[False,True,False,True,True,False,False,True,True,True,False,False,False,True],[False,False,True,False,True,True,False,False,False,False,True,True,True,False]]], dtype = "bool")#candidate|2112|(14, 5, 14)|const|bool
var_2113 = relay.var("var_2113", dtype = "bool", shape = (14, 5, 14))#candidate|2113|(14, 5, 14)|var|bool
bop_2114 = relay.logical_and(const_2112.astype('bool'), relay.reshape(var_2113.astype('bool'), relay.shape_of(const_2112))) # shape=(14, 5, 14)
output = bop_2114
output2 = bop_2114
func_2123 = relay.Function([var_2113,], output)
mod['func_2123'] = func_2123
mod = relay.transform.InferType()(mod)
var_2124 = relay.var("var_2124", dtype = "bool", shape = (14, 5, 14))#candidate|2124|(14, 5, 14)|var|bool
output = func_2123(var_2124)
func_2125 = relay.Function([var_2124], output)
mutated_mod['func_2125'] = func_2125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1429_call = mod.get_global_var('func_1429')
func_1430_call = mutated_mod.get_global_var('func_1430')
call_2149 = func_1429_call()
call_2150 = func_1429_call()
output = relay.Tuple([call_2149,])
output2 = relay.Tuple([call_2150,])
func_2155 = relay.Function([], output)
mod['func_2155'] = func_2155
mod = relay.transform.InferType()(mod)
output = func_2155()
func_2156 = relay.Function([], output)
mutated_mod['func_2156'] = func_2156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_497_call = mod.get_global_var('func_497')
func_498_call = mutated_mod.get_global_var('func_498')
call_2205 = relay.TupleGetItem(func_497_call(), 0)
call_2206 = relay.TupleGetItem(func_498_call(), 0)
func_408_call = mod.get_global_var('func_408')
func_410_call = mutated_mod.get_global_var('func_410')
call_2217 = relay.TupleGetItem(func_408_call(), 0)
call_2218 = relay.TupleGetItem(func_410_call(), 0)
func_1018_call = mod.get_global_var('func_1018')
func_1022_call = mutated_mod.get_global_var('func_1022')
var_2230 = relay.var("var_2230", dtype = "uint16", shape = (1320,))#candidate|2230|(1320,)|var|uint16
call_2229 = relay.TupleGetItem(func_1018_call(relay.reshape(var_2230.astype('uint16'), [12, 11, 10]), relay.reshape(var_2230.astype('uint8'), [12, 11, 10]), ), 1)
call_2231 = relay.TupleGetItem(func_1022_call(relay.reshape(var_2230.astype('uint16'), [12, 11, 10]), relay.reshape(var_2230.astype('uint8'), [12, 11, 10]), ), 1)
uop_2240 = relay.atan(var_2230.astype('float64')) # shape=(1320,)
uop_2249 = relay.asin(call_2229.astype('float32')) # shape=(12, 11, 10)
uop_2251 = relay.asin(call_2231.astype('float32')) # shape=(12, 11, 10)
func_1490_call = mod.get_global_var('func_1490')
func_1492_call = mutated_mod.get_global_var('func_1492')
call_2253 = relay.TupleGetItem(func_1490_call(), 0)
call_2254 = relay.TupleGetItem(func_1492_call(), 0)
func_661_call = mod.get_global_var('func_661')
func_663_call = mutated_mod.get_global_var('func_663')
call_2257 = func_661_call()
call_2258 = func_661_call()
output = relay.Tuple([call_2205,call_2217,uop_2240,uop_2249,call_2253,call_2257,])
output2 = relay.Tuple([call_2206,call_2218,uop_2240,uop_2251,call_2254,call_2258,])
func_2266 = relay.Function([var_2230,], output)
mod['func_2266'] = func_2266
mod = relay.transform.InferType()(mod)
mutated_mod['func_2266'] = func_2266
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2267 = relay.var("var_2267", dtype = "uint16", shape = (1320,))#candidate|2267|(1320,)|var|uint16
func_2266_call = mutated_mod.get_global_var('func_2266')
call_2268 = func_2266_call(var_2267)
output = call_2268
func_2269 = relay.Function([var_2267], output)
mutated_mod['func_2269'] = func_2269
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2290 = relay.var("var_2290", dtype = "uint32", shape = ())#candidate|2290|()|var|uint32
const_2291 = relay.const([[[-1,-7,4,-9,-6],[1,-3,5,-7,-7],[1,-5,-7,5,-7],[4,-1,-1,10,5]],[[4,-5,1,6,-5],[6,-1,9,5,-6],[6,-2,-2,-1,4],[8,4,-5,-3,2]],[[4,-4,-9,2,8],[-10,-7,1,-7,2],[10,9,3,-8,5],[-6,10,-3,-2,-4]],[[-3,7,7,9,-10],[-5,-1,4,-8,-2],[-4,1,8,-4,-9],[3,3,1,-7,5]],[[-3,10,3,-10,8],[-6,-10,-8,-3,1],[9,3,5,3,6],[1,-6,-7,-7,-4]],[[9,-9,6,-9,8],[-10,-5,10,-9,-2],[-10,-8,4,-9,-10],[-7,-10,-10,-6,7]],[[9,2,10,-6,8],[6,2,6,7,8],[8,-8,4,7,5],[5,-1,1,-2,2]]], dtype = "uint32")#candidate|2291|(7, 4, 5)|const|uint32
bop_2292 = relay.bitwise_or(var_2290.astype('uint32'), const_2291.astype('uint32')) # shape=(7, 4, 5)
uop_2322 = relay.atan(const_2291.astype('float32')) # shape=(7, 4, 5)
func_364_call = mod.get_global_var('func_364')
func_366_call = mutated_mod.get_global_var('func_366')
call_2332 = func_364_call()
call_2333 = func_364_call()
uop_2336 = relay.cos(uop_2322.astype('float32')) # shape=(7, 4, 5)
func_1055_call = mod.get_global_var('func_1055')
func_1056_call = mutated_mod.get_global_var('func_1056')
call_2341 = relay.TupleGetItem(func_1055_call(), 0)
call_2342 = relay.TupleGetItem(func_1056_call(), 0)
output = relay.Tuple([bop_2292,call_2332,uop_2336,call_2341,])
output2 = relay.Tuple([bop_2292,call_2333,uop_2336,call_2342,])
func_2357 = relay.Function([var_2290,], output)
mod['func_2357'] = func_2357
mod = relay.transform.InferType()(mod)
mutated_mod['func_2357'] = func_2357
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2358 = relay.var("var_2358", dtype = "uint32", shape = ())#candidate|2358|()|var|uint32
func_2357_call = mutated_mod.get_global_var('func_2357')
call_2359 = func_2357_call(var_2358)
output = call_2359
func_2360 = relay.Function([var_2358], output)
mutated_mod['func_2360'] = func_2360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_815_call = mod.get_global_var('func_815')
func_817_call = mutated_mod.get_global_var('func_817')
call_2380 = relay.TupleGetItem(func_815_call(), 2)
call_2381 = relay.TupleGetItem(func_817_call(), 2)
var_2384 = relay.var("var_2384", dtype = "uint16", shape = (1540,))#candidate|2384|(1540,)|var|uint16
bop_2385 = relay.logical_xor(call_2380.astype('int32'), relay.reshape(var_2384.astype('int32'), relay.shape_of(call_2380))) # shape=(1540,)
bop_2388 = relay.logical_xor(call_2381.astype('int32'), relay.reshape(var_2384.astype('int32'), relay.shape_of(call_2381))) # shape=(1540,)
output = bop_2385
output2 = bop_2388
func_2391 = relay.Function([var_2384,], output)
mod['func_2391'] = func_2391
mod = relay.transform.InferType()(mod)
var_2392 = relay.var("var_2392", dtype = "uint16", shape = (1540,))#candidate|2392|(1540,)|var|uint16
output = func_2391(var_2392)
func_2393 = relay.Function([var_2392], output)
mutated_mod['func_2393'] = func_2393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_298_call = mod.get_global_var('func_298')
func_300_call = mutated_mod.get_global_var('func_300')
call_2409 = func_298_call()
call_2410 = func_298_call()
func_1466_call = mod.get_global_var('func_1466')
func_1469_call = mutated_mod.get_global_var('func_1469')
var_2416 = relay.var("var_2416", dtype = "int64", shape = (550, 2))#candidate|2416|(550, 2)|var|int64
call_2415 = relay.TupleGetItem(func_1466_call(relay.reshape(var_2416.astype('int64'), [1100,])), 3)
call_2417 = relay.TupleGetItem(func_1469_call(relay.reshape(var_2416.astype('int64'), [1100,])), 3)
output = relay.Tuple([call_2409,call_2415,var_2416,])
output2 = relay.Tuple([call_2410,call_2417,var_2416,])
func_2447 = relay.Function([var_2416,], output)
mod['func_2447'] = func_2447
mod = relay.transform.InferType()(mod)
mutated_mod['func_2447'] = func_2447
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2448 = relay.var("var_2448", dtype = "int64", shape = (550, 2))#candidate|2448|(550, 2)|var|int64
func_2447_call = mutated_mod.get_global_var('func_2447')
call_2449 = func_2447_call(var_2448)
output = call_2449
func_2450 = relay.Function([var_2448], output)
mutated_mod['func_2450'] = func_2450
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2452 = relay.var("var_2452", dtype = "uint32", shape = ())#candidate|2452|()|var|uint32
var_2453 = relay.var("var_2453", dtype = "uint32", shape = (16, 3, 1))#candidate|2453|(16, 3, 1)|var|uint32
bop_2454 = relay.right_shift(var_2452.astype('uint32'), var_2453.astype('uint32')) # shape=(16, 3, 1)
func_2155_call = mod.get_global_var('func_2155')
func_2156_call = mutated_mod.get_global_var('func_2156')
call_2458 = relay.TupleGetItem(func_2155_call(), 0)
call_2459 = relay.TupleGetItem(func_2156_call(), 0)
func_2123_call = mod.get_global_var('func_2123')
func_2125_call = mutated_mod.get_global_var('func_2125')
const_2462 = relay.const([False,False,True,False,False,True,False,False,True,True,True,True,True,False,False,False,True,True,True,True,False,True,False,False,True,False,True,True,False,True,True,False,True,False,False,True,True,False,True,False,True,False,True,True,False,True,True,True,True,False,False,True,True,True,False,False,True,True,True,True,False,False,True,True,False,True,False,True,False,True,True,True,True,True,False,True,False,False,True,True,False,True,True,False,False,True,False,True,False,False,False,False,False,True,True,True,True,True,False,True,False,False,False,True,True,True,False,True,True,True,True,True,True,False,True,True,True,False,True,True,False,True,True,False,True,False,True,False,True,False,True,True,False,True,False,True,False,False,False,True,False,True,True,True,True,False,False,False,False,True,True,False,True,False,True,False,False,False,False,True,False,True,False,False,False,False,True,True,True,False,False,True,True,True,False,True,False,False,True,False,False,True,True,True,True,False,True,False,False,True,True,True,False,False,True,False,False,True,True,True,True,False,False,False,True,False,True,True,True,True,False,True,False,True,False,True,True,True,True,True,False,True,False,False,True,False,False,True,True,False,True,False,False,True,False,True,False,False,True,True,True,True,False,True,False,False,False,True,True,False,False,True,True,True,True,False,True,True,True,False,True,False,False,True,False,False,True,False,False,False,True,True,True,True,False,True,True,True,False,False,True,False,True,False,True,False,False,False,True,True,False,True,False,False,False,False,True,True,False,True,True,True,True,False,False,True,True,True,False,True,True,True,False,False,True,True,False,True,False,True,True,False,False,True,True,True,True,False,False,True,True,False,False,False,False,False,False,False,True,False,True,False,False,True,False,True,True,False,True,True,True,False,True,False,True,False,True,False,False,True,True,False,True,True,False,False,True,False,False,False,True,True,False,True,True,False,False,False,False,True,True,True,True,False,True,False,True,False,False,True,False,True,True,True,False,False,True,True,False,True,True,True,True,True,False,False,True,True,False,True,False,True,True,False,True,False,False,False,True,True,False,True,False,True,False,True,True,False,False,False,True,False,True,False,True,False,False,True,True,False,False,True,True,True,True,True,False,False,True,True,True,True,False,True,True,False,False,False,False,True,False,False,True,False,False,False,False,True,True,True,True,False,False,True,True,False,False,True,False,True,False,True,True,False,False,False,True,True,False,True,False,True,True,True,True,False,True,True,True,True,False,False,True,False,True,False,False,True,False,False,True,False,True,False,True,False,False,False,True,False,True,True,True,True,False,False,True,True,True,False,False,True,False,True,False,False,False,False,True,False,True,False,False,False,False,True,False,False,True,True,True,True,False,False,False,False,True,True,False,False,True,False,False,True,False,False,True,False,False,True,False,True,True,False,False,False,False,False,False,True,False,True,False,False,False,False,True,True,True,True,True,False,True,True,False,True,True,True,True,False,False,True,True,False,False,True,False,False,False,False,True,False,False,False,False,False,False,True,True,False,False,False,False,False,False,False,True,True,False,True,True,False,False,True,False,False,False,False,False,False,True,False,False,True,False,True,True,False,False,False,False,True,False,True,True,False,True,False,False,True,True,True,False,False,False,False,False,True,True,True,True,False,True,False,True,True,True,False,True,True,False,False,False,False,True,True,True,False,False,True,False,True,False,False,True,True,False,False,False,True,True,True,True,False,True,False,True,False,False,False,False,False,False,False,True,True,False,False,False,False,True,False,True,True,False,True,False,False,True,False,False,False,False,True,False,True,False,True,False,False,True,False,True,False,False,False,True,False,False,True,False,True,True,False,False,True,True,True,False,False,True,False,False,True,True,False,True,True,True,True,False,False,True,True,False,True,True,False,False,True,True,False,False,True,False,False,False,True,True,False,True,True,False,True,False,False,True,True,True,False,False,True,True,True,False,True,True,True,True,True,False,True,True,False,False,False,True,False,True,False,True,True,True,True,False,False,True,False,True,True,False,False,False,True,True,True,True,False,False,False,True,True,True,True,True,True,True,False,False,False,True,True,True,False,False,False,False,False,False,False,True,False,False,True,False,True,False,True,False,True,True,True,False,True,False,True,False,True,False,False,False,True,True,True,True,False,True,False,False,True,False,True,False,False,False,False,True,True,True,True,False,False,True,False,True,True,True,False,True,True,False,True,False,False,False,False,False,False,False,False,True,False,True,True,False,True,True,True,False,False,True,False,True,False,False,False,True,False,False,False,True,True,True,False,True,False,False,True,False,False,True,True,False,False,True,False,True,False,True,False,True,False,False,False,False,True,False,False,True,True,False,False,False,False,False,True,False,False,False,False], dtype = "bool")#candidate|2462|(980,)|const|bool
call_2461 = func_2123_call(relay.reshape(const_2462.astype('bool'), [14, 5, 14]))
call_2463 = func_2123_call(relay.reshape(const_2462.astype('bool'), [14, 5, 14]))
uop_2469 = relay.log2(call_2461.astype('float32')) # shape=(14, 5, 14)
uop_2471 = relay.log2(call_2463.astype('float32')) # shape=(14, 5, 14)
bop_2477 = relay.subtract(bop_2454.astype('int8'), relay.reshape(var_2453.astype('int8'), relay.shape_of(bop_2454))) # shape=(16, 3, 1)
bop_2484 = relay.bitwise_xor(uop_2469.astype('int8'), relay.reshape(const_2462.astype('int8'), relay.shape_of(uop_2469))) # shape=(14, 5, 14)
bop_2487 = relay.bitwise_xor(uop_2471.astype('int8'), relay.reshape(const_2462.astype('int8'), relay.shape_of(uop_2471))) # shape=(14, 5, 14)
output = relay.Tuple([call_2458,bop_2477,bop_2484,])
output2 = relay.Tuple([call_2459,bop_2477,bop_2487,])
func_2491 = relay.Function([var_2452,var_2453,], output)
mod['func_2491'] = func_2491
mod = relay.transform.InferType()(mod)
mutated_mod['func_2491'] = func_2491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2491_call = mutated_mod.get_global_var('func_2491')
var_2493 = relay.var("var_2493", dtype = "uint32", shape = ())#candidate|2493|()|var|uint32
var_2494 = relay.var("var_2494", dtype = "uint32", shape = (16, 3, 1))#candidate|2494|(16, 3, 1)|var|uint32
call_2492 = func_2491_call(var_2493,var_2494,)
output = call_2492
func_2495 = relay.Function([var_2493,var_2494,], output)
mutated_mod['func_2495'] = func_2495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_298_call = mod.get_global_var('func_298')
func_300_call = mutated_mod.get_global_var('func_300')
call_2572 = func_298_call()
call_2573 = func_298_call()
output = call_2572
output2 = call_2573
func_2585 = relay.Function([], output)
mod['func_2585'] = func_2585
mod = relay.transform.InferType()(mod)
mutated_mod['func_2585'] = func_2585
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2585_call = mutated_mod.get_global_var('func_2585')
call_2586 = func_2585_call()
output = call_2586
func_2587 = relay.Function([], output)
mutated_mod['func_2587'] = func_2587
mutated_mod = relay.transform.InferType()(mutated_mod)
func_661_call = mod.get_global_var('func_661')
func_663_call = mutated_mod.get_global_var('func_663')
call_2591 = func_661_call()
call_2592 = func_661_call()
func_1267_call = mod.get_global_var('func_1267')
func_1269_call = mutated_mod.get_global_var('func_1269')
const_2600 = relay.const([[7,6,-7,-7,-2,4,2,-4,-8,-4,3,-7,-8,-2,7,1,-10,-5,8,1,-1,-1,-6,1,7,-9,5,9,4,-10,-9,-6,-2,5,5,1,10,8,6,-2,-9,5,-6,5,-8,-1,-8,6,-10,-1,5,-10,3,-1,-9,3,-5,-10,-3,-2,-2,7,-10,1,4,-4,3,5,1,-4,-10,-8,3,5,5,-6,2,8,-8,1,-2,-2,10,10,3,2,8,10,8,-9,5,-1,-3,-9,9,-3,-7,-5,-10,8,8,1,-10,9,-6,-2,-8,-8,-1,9,8,-2,-7,-4,1,-4,-2,4,4,3,-6,3,-7,2,-9,-1,-5,2,7,10,-9,-6,9,-4,-5,-5,3,2,10,-9,7,5,-2,-7,-4,8,3,-4,-4,-7,9,-10,1,-2,8,-1,-3,10,-5,4,-3,-3,-4,1,9,-9,-10,-1,-2,4,-4,8,1,-3,-4,6,-7,6,-7,-3,2,5,2,-5,-8,-6,-5,-2,-2,-3,-9,-4,7,2,-4,10,-7,-2,-2,-3,7,7,-2,8,-1,10,9,10,3,-10,5,5,-7,-10,3,3,3,-3,6,-8],[-2,1,-2,5,-1,2,-7,9,-3,4,2,-7,-7,9,2,4,-8,5,-4,-5,5,2,-6,7,9,7,-1,6,7,-3,3,-4,2,10,10,-2,3,-9,6,10,7,9,-4,-8,-10,-1,-10,-5,4,10,-3,1,8,-4,-5,-2,-4,2,5,10,-3,-10,5,7,1,3,2,9,-1,-4,9,-1,-8,10,3,9,-8,10,2,-5,5,-6,-2,-6,-8,-1,8,-10,3,10,-8,3,-7,3,2,-2,-6,3,3,-10,10,8,1,6,7,-1,4,5,1,-1,-6,10,-3,-7,-2,7,-8,2,4,3,-4,8,-2,-1,1,-6,5,8,-6,-4,3,2,6,-9,4,2,10,-7,-3,7,-10,-2,6,-5,-4,-3,-10,-8,-1,-5,-1,-2,-6,-3,-7,4,3,6,-3,-6,-10,6,5,6,-1,8,9,2,9,4,-6,-5,2,10,4,6,4,4,6,-5,3,6,1,7,3,-8,-2,2,6,-1,8,4,9,-3,-10,-9,-2,-8,3,5,-9,-9,-7,4,2,4,3,6,-8,5,9,-4,1,6,-7,3,5,6,-2,-7],[-8,-6,9,-2,-3,6,5,3,-9,-1,1,2,-6,9,-1,-2,-7,9,-2,-6,10,-9,1,-10,-2,-9,-2,10,-1,6,5,-10,-10,-2,-10,9,10,6,1,-4,-4,7,-5,-6,6,-8,-3,7,7,-6,-10,8,5,3,-9,-9,9,-1,-5,-1,-2,-5,-7,-8,4,3,9,3,-5,-9,3,-7,8,-7,6,5,6,3,-2,8,-5,9,-2,9,7,2,-10,2,-7,-10,-6,-3,4,-8,6,-2,8,-4,-2,-8,3,-10,-10,-8,1,2,-4,2,2,4,-5,-9,-8,5,-8,-10,4,-3,-2,1,-10,1,-9,-1,2,-1,10,1,-4,7,-1,4,-8,-10,-9,-4,-8,-4,9,-8,-1,-1,8,10,-8,6,5,-7,-9,3,-9,-1,-3,4,10,-4,-10,1,-7,-3,-7,6,-1,5,9,-9,5,5,-5,-10,10,6,-9,1,-10,-2,-3,1,3,-5,-5,3,6,-8,7,-8,5,9,2,1,4,1,6,-1,-9,1,3,-4,2,-2,3,5,5,-2,-4,1,10,5,-5,3,3,7,-10,4,4,-2,-5,5,-1,-7],[3,10,1,7,2,-7,8,2,7,-1,-4,-10,-7,9,3,2,-7,7,-10,1,6,6,5,1,5,-3,-4,8,-7,9,6,-5,-6,8,-1,-5,-10,-1,2,-7,4,4,2,-9,-10,8,-2,8,9,3,8,7,10,4,-9,-8,10,3,5,-10,2,2,3,1,7,-2,-1,-4,-6,-4,-9,10,-4,3,6,-6,-3,2,10,8,7,-4,-8,1,9,8,8,9,-2,-1,6,-7,-8,5,-4,7,2,2,-4,-3,-8,10,1,-8,-4,9,8,8,-7,-6,-7,-2,6,10,-9,-2,-6,-5,-6,7,-1,9,-4,-7,-2,-2,6,8,10,-4,3,-5,2,5,2,5,10,-5,3,-7,-5,-3,-3,-6,1,1,8,2,-6,8,-8,-3,9,5,8,-8,-9,3,-4,-4,-9,-10,10,8,6,4,-7,2,-3,-9,-9,5,1,-9,-6,-1,-7,-5,10,1,-7,2,1,1,3,6,-10,9,8,-6,10,-3,-10,-1,10,-8,8,1,8,-3,6,2,-10,-7,8,7,3,-2,-6,5,7,-5,5,-2,9,-5,-7,-1,7,-9],[1,2,6,9,9,10,-7,-8,-2,-5,-10,-8,-7,-7,-6,1,2,3,9,2,4,-3,6,3,-4,10,1,2,-4,-2,5,8,-7,5,-3,-4,-8,9,-10,3,3,7,-1,1,8,-8,9,10,8,-3,-2,-7,-4,4,9,8,-3,3,6,9,-7,8,-2,-3,-4,1,-3,-6,-5,3,-2,-5,9,-8,3,-10,-6,-8,9,-1,8,-10,-10,-10,-9,-10,-5,7,-6,9,-2,-2,9,9,3,-2,-9,4,1,8,-8,-2,-7,8,-3,5,-8,-6,-8,7,-4,-4,1,4,-5,-3,-3,7,3,-1,2,2,2,-7,4,6,2,10,-10,-7,-7,8,-7,-7,-10,-7,-6,-10,-10,3,-10,-9,-8,6,-3,3,-3,-1,-5,1,9,-8,8,5,7,-1,6,-9,-6,2,-10,-1,-7,-3,1,10,3,-6,7,10,-1,3,10,-4,9,-8,-1,1,-1,10,10,3,7,-8,-3,8,-9,5,-3,6,3,10,-2,3,7,5,-3,-5,-10,-5,-1,-8,6,-2,2,-2,1,-10,4,8,7,1,4,2,-8,6,2,2,9,6],[1,8,-9,-6,-4,-6,-10,2,-4,-5,-9,-4,8,8,1,1,-3,5,-7,-7,-7,-1,10,8,-8,-8,5,10,9,1,4,-3,10,1,1,8,10,5,-5,-6,8,-9,-8,-8,-7,-9,10,-7,10,-8,5,10,-7,7,-10,4,7,-2,-2,-1,9,1,-2,2,6,4,7,-7,9,-8,-7,6,8,10,-8,1,3,-9,-10,-6,2,-10,-3,5,10,-10,6,4,6,3,7,1,6,4,2,2,1,3,8,-6,1,-9,6,10,7,3,-9,-1,-8,-1,-6,-6,-7,-1,-9,7,-6,7,-8,-1,-4,9,3,-8,-7,-3,4,-10,-10,-9,-1,-1,3,-9,6,-5,8,-4,6,-4,-3,-5,-8,-9,7,9,4,-7,7,7,-7,6,8,6,1,6,9,-2,-6,5,-1,-5,4,2,-7,-5,-5,2,10,-9,8,-7,-7,-3,-10,-8,5,-5,-5,-10,-8,-9,-5,-8,8,8,-1,4,1,-10,-8,-1,-2,-1,5,-1,8,8,10,-10,1,4,-2,1,6,8,2,6,-8,-2,10,-8,3,4,1,-2,4,6,4,1]], dtype = "uint16")#candidate|2600|(6, 220)|const|uint16
call_2599 = relay.TupleGetItem(func_1267_call(relay.reshape(const_2600.astype('uint16'), [1320,])), 3)
call_2601 = relay.TupleGetItem(func_1269_call(relay.reshape(const_2600.astype('uint16'), [1320,])), 3)
func_1055_call = mod.get_global_var('func_1055')
func_1056_call = mutated_mod.get_global_var('func_1056')
call_2627 = relay.TupleGetItem(func_1055_call(), 0)
call_2628 = relay.TupleGetItem(func_1056_call(), 0)
output = relay.Tuple([call_2591,call_2599,const_2600,call_2627,])
output2 = relay.Tuple([call_2592,call_2601,const_2600,call_2628,])
func_2632 = relay.Function([], output)
mod['func_2632'] = func_2632
mod = relay.transform.InferType()(mod)
mutated_mod['func_2632'] = func_2632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2632_call = mutated_mod.get_global_var('func_2632')
call_2633 = func_2632_call()
output = call_2633
func_2634 = relay.Function([], output)
mutated_mod['func_2634'] = func_2634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_661_call = mod.get_global_var('func_661')
func_663_call = mutated_mod.get_global_var('func_663')
call_2637 = func_661_call()
call_2638 = func_661_call()
func_448_call = mod.get_global_var('func_448')
func_449_call = mutated_mod.get_global_var('func_449')
call_2649 = relay.TupleGetItem(func_448_call(), 1)
call_2650 = relay.TupleGetItem(func_449_call(), 1)
output = relay.Tuple([call_2637,call_2649,])
output2 = relay.Tuple([call_2638,call_2650,])
func_2668 = relay.Function([], output)
mod['func_2668'] = func_2668
mod = relay.transform.InferType()(mod)
mutated_mod['func_2668'] = func_2668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2668_call = mutated_mod.get_global_var('func_2668')
call_2669 = func_2668_call()
output = call_2669
func_2670 = relay.Function([], output)
mutated_mod['func_2670'] = func_2670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1429_call = mod.get_global_var('func_1429')
func_1430_call = mutated_mod.get_global_var('func_1430')
call_2677 = func_1429_call()
call_2678 = func_1429_call()
func_1055_call = mod.get_global_var('func_1055')
func_1056_call = mutated_mod.get_global_var('func_1056')
call_2679 = relay.TupleGetItem(func_1055_call(), 0)
call_2680 = relay.TupleGetItem(func_1056_call(), 0)
uop_2683 = relay.asinh(call_2677.astype('float64')) # shape=(2, 9, 10)
uop_2685 = relay.asinh(call_2678.astype('float64')) # shape=(2, 9, 10)
bop_2688 = relay.floor_mod(uop_2683.astype('float64'), relay.reshape(call_2677.astype('float64'), relay.shape_of(uop_2683))) # shape=(2, 9, 10)
bop_2691 = relay.floor_mod(uop_2685.astype('float64'), relay.reshape(call_2678.astype('float64'), relay.shape_of(uop_2685))) # shape=(2, 9, 10)
output = relay.Tuple([call_2679,bop_2688,])
output2 = relay.Tuple([call_2680,bop_2691,])
func_2697 = relay.Function([], output)
mod['func_2697'] = func_2697
mod = relay.transform.InferType()(mod)
output = func_2697()
func_2698 = relay.Function([], output)
mutated_mod['func_2698'] = func_2698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_408_call = mod.get_global_var('func_408')
func_410_call = mutated_mod.get_global_var('func_410')
call_2711 = relay.TupleGetItem(func_408_call(), 0)
call_2712 = relay.TupleGetItem(func_410_call(), 0)
func_898_call = mod.get_global_var('func_898')
func_900_call = mutated_mod.get_global_var('func_900')
call_2721 = relay.TupleGetItem(func_898_call(), 1)
call_2722 = relay.TupleGetItem(func_900_call(), 1)
var_2740 = relay.var("var_2740", dtype = "uint16", shape = (15, 11, 10))#candidate|2740|(15, 11, 10)|var|uint16
bop_2741 = relay.maximum(call_2711.astype('int16'), var_2740.astype('int16')) # shape=(15, 11, 10)
bop_2744 = relay.maximum(call_2712.astype('int16'), var_2740.astype('int16')) # shape=(15, 11, 10)
func_661_call = mod.get_global_var('func_661')
func_663_call = mutated_mod.get_global_var('func_663')
call_2770 = func_661_call()
call_2771 = func_661_call()
output = relay.Tuple([call_2721,bop_2741,call_2770,])
output2 = relay.Tuple([call_2722,bop_2744,call_2771,])
func_2780 = relay.Function([var_2740,], output)
mod['func_2780'] = func_2780
mod = relay.transform.InferType()(mod)
mutated_mod['func_2780'] = func_2780
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2781 = relay.var("var_2781", dtype = "uint16", shape = (15, 11, 10))#candidate|2781|(15, 11, 10)|var|uint16
func_2780_call = mutated_mod.get_global_var('func_2780')
call_2782 = func_2780_call(var_2781)
output = call_2782
func_2783 = relay.Function([var_2781], output)
mutated_mod['func_2783'] = func_2783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1429_call = mod.get_global_var('func_1429')
func_1430_call = mutated_mod.get_global_var('func_1430')
call_2811 = func_1429_call()
call_2812 = func_1429_call()
output = relay.Tuple([call_2811,])
output2 = relay.Tuple([call_2812,])
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
func_1055_call = mod.get_global_var('func_1055')
func_1056_call = mutated_mod.get_global_var('func_1056')
call_2934 = relay.TupleGetItem(func_1055_call(), 0)
call_2935 = relay.TupleGetItem(func_1056_call(), 0)
output = relay.Tuple([call_2934,])
output2 = relay.Tuple([call_2935,])
func_2938 = relay.Function([], output)
mod['func_2938'] = func_2938
mod = relay.transform.InferType()(mod)
mutated_mod['func_2938'] = func_2938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2938_call = mutated_mod.get_global_var('func_2938')
call_2939 = func_2938_call()
output = call_2939
func_2940 = relay.Function([], output)
mutated_mod['func_2940'] = func_2940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_773_call = mod.get_global_var('func_773')
func_774_call = mutated_mod.get_global_var('func_774')
call_2955 = func_773_call()
call_2956 = func_773_call()
output = call_2955
output2 = call_2956
func_2957 = relay.Function([], output)
mod['func_2957'] = func_2957
mod = relay.transform.InferType()(mod)
mutated_mod['func_2957'] = func_2957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2957_call = mutated_mod.get_global_var('func_2957')
call_2958 = func_2957_call()
output = call_2958
func_2959 = relay.Function([], output)
mutated_mod['func_2959'] = func_2959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1862_call = mod.get_global_var('func_1862')
func_1863_call = mutated_mod.get_global_var('func_1863')
call_2963 = func_1862_call()
call_2964 = func_1862_call()
output = relay.Tuple([call_2963,])
output2 = relay.Tuple([call_2964,])
func_2978 = relay.Function([], output)
mod['func_2978'] = func_2978
mod = relay.transform.InferType()(mod)
mutated_mod['func_2978'] = func_2978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2978_call = mutated_mod.get_global_var('func_2978')
call_2979 = func_2978_call()
output = call_2979
func_2980 = relay.Function([], output)
mutated_mod['func_2980'] = func_2980
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2994 = relay.var("var_2994", dtype = "float64", shape = (9, 14, 5))#candidate|2994|(9, 14, 5)|var|float64
var_2995 = relay.var("var_2995", dtype = "float64", shape = (9, 14, 5))#candidate|2995|(9, 14, 5)|var|float64
bop_2996 = relay.less(var_2994.astype('bool'), relay.reshape(var_2995.astype('bool'), relay.shape_of(var_2994))) # shape=(9, 14, 5)
func_2491_call = mod.get_global_var('func_2491')
func_2495_call = mutated_mod.get_global_var('func_2495')
const_3000 = relay.const(7, dtype = "uint32")#candidate|3000|()|const|uint32
const_3001 = relay.const([[2],[-4],[-2],[8],[-2],[3],[4],[5],[-8],[10],[-5],[-6],[-6],[-8],[3],[-10],[10],[8],[6],[5],[-10],[-9],[4],[6],[5],[4],[1],[-2],[2],[-1],[-10],[2],[3],[-1],[-5],[-7],[5],[-7],[2],[-9],[-9],[4],[-2],[8],[8],[1],[-8],[-9]], dtype = "uint32")#candidate|3001|(48, 1)|const|uint32
call_2999 = relay.TupleGetItem(func_2491_call(relay.reshape(const_3000.astype('uint32'), []), relay.reshape(const_3001.astype('uint32'), [16, 3, 1]), ), 2)
call_3002 = relay.TupleGetItem(func_2495_call(relay.reshape(const_3000.astype('uint32'), []), relay.reshape(const_3001.astype('uint32'), [16, 3, 1]), ), 2)
uop_3007 = relay.sigmoid(var_2994.astype('float32')) # shape=(9, 14, 5)
func_2123_call = mod.get_global_var('func_2123')
func_2125_call = mutated_mod.get_global_var('func_2125')
call_3010 = func_2123_call(relay.reshape(call_2999.astype('bool'), [14, 5, 14]))
call_3011 = func_2123_call(relay.reshape(call_2999.astype('bool'), [14, 5, 14]))
uop_3020 = relay.atanh(const_3001.astype('float64')) # shape=(48, 1)
func_497_call = mod.get_global_var('func_497')
func_498_call = mutated_mod.get_global_var('func_498')
call_3034 = relay.TupleGetItem(func_497_call(), 0)
call_3035 = relay.TupleGetItem(func_498_call(), 0)
func_815_call = mod.get_global_var('func_815')
func_817_call = mutated_mod.get_global_var('func_817')
call_3045 = relay.TupleGetItem(func_815_call(), 1)
call_3046 = relay.TupleGetItem(func_817_call(), 1)
output = relay.Tuple([bop_2996,call_2999,const_3000,uop_3007,call_3010,uop_3020,call_3034,call_3045,])
output2 = relay.Tuple([bop_2996,call_3002,const_3000,uop_3007,call_3011,uop_3020,call_3035,call_3046,])
func_3047 = relay.Function([var_2994,var_2995,], output)
mod['func_3047'] = func_3047
mod = relay.transform.InferType()(mod)
mutated_mod['func_3047'] = func_3047
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3047_call = mutated_mod.get_global_var('func_3047')
var_3049 = relay.var("var_3049", dtype = "float64", shape = (9, 14, 5))#candidate|3049|(9, 14, 5)|var|float64
var_3050 = relay.var("var_3050", dtype = "float64", shape = (9, 14, 5))#candidate|3050|(9, 14, 5)|var|float64
call_3048 = func_3047_call(var_3049,var_3050,)
output = call_3048
func_3051 = relay.Function([var_3049,var_3050,], output)
mutated_mod['func_3051'] = func_3051
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3056 = relay.const([[[4.945228,8.844950],[-8.186350,6.779245],[6.779698,-8.514487],[-9.173035,1.825357],[6.169677,-4.538161],[-3.607648,4.796348],[6.713936,-1.106951]],[[3.469718,-9.553336],[-6.504485,-1.542986],[-4.146132,-2.779489],[-4.766198,6.389617],[8.183159,-5.285590],[9.408546,-4.014131],[7.135954,2.834842]],[[-0.941616,7.332422],[5.326164,-2.183940],[0.461981,-1.091512],[3.923717,1.670813],[0.349138,-3.322809],[6.228632,-5.265920],[1.229846,-6.853637]],[[-3.184181,-3.196442],[-7.459556,-9.098369],[3.706356,7.872340],[1.781772,-7.270199],[-2.074700,7.106721],[-6.753570,-1.121424],[-0.254729,-4.966953]],[[9.448996,2.709784],[-6.645814,1.729369],[1.967402,6.365029],[-8.263476,4.827990],[-9.015384,-5.518515],[-3.010724,5.873996],[4.433750,-4.429147]],[[-2.662487,-0.650968],[-6.909880,5.554021],[6.637214,9.322294],[3.380472,4.628962],[5.266594,7.792405],[-6.259728,-3.307934],[6.895029,6.271463]],[[1.223413,6.221482],[2.649896,-6.082487],[8.454580,-8.163150],[-3.274048,5.266199],[-7.950317,2.261217],[0.094699,-5.764289],[6.139941,-5.624466]],[[-1.504549,2.803751],[-2.683897,5.524923],[-7.715460,3.878368],[2.534242,-9.262306],[7.274059,1.375236],[-1.223436,3.582218],[-1.578176,6.098970]],[[-3.945458,-8.918700],[-9.643752,-9.439634],[-2.321847,-7.332900],[4.302899,-7.777994],[6.680135,-0.760492],[-5.325913,6.664245],[0.705801,0.833639]]], dtype = "float64")#candidate|3056|(9, 7, 2)|const|float64
uop_3057 = relay.log2(const_3056.astype('float64')) # shape=(9, 7, 2)
output = relay.Tuple([uop_3057,])
output2 = relay.Tuple([uop_3057,])
func_3059 = relay.Function([], output)
mod['func_3059'] = func_3059
mod = relay.transform.InferType()(mod)
mutated_mod['func_3059'] = func_3059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3059_call = mutated_mod.get_global_var('func_3059')
call_3060 = func_3059_call()
output = call_3060
func_3061 = relay.Function([], output)
mutated_mod['func_3061'] = func_3061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1739_call = mod.get_global_var('func_1739')
func_1740_call = mutated_mod.get_global_var('func_1740')
call_3115 = func_1739_call()
call_3116 = func_1739_call()
output = call_3115
output2 = call_3116
func_3131 = relay.Function([], output)
mod['func_3131'] = func_3131
mod = relay.transform.InferType()(mod)
mutated_mod['func_3131'] = func_3131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3131_call = mutated_mod.get_global_var('func_3131')
call_3132 = func_3131_call()
output = call_3132
func_3133 = relay.Function([], output)
mutated_mod['func_3133'] = func_3133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1350_call = mod.get_global_var('func_1350')
func_1351_call = mutated_mod.get_global_var('func_1351')
call_3161 = relay.TupleGetItem(func_1350_call(), 1)
call_3162 = relay.TupleGetItem(func_1351_call(), 1)
uop_3164 = relay.cosh(call_3161.astype('float32')) # shape=(1, 11, 10)
uop_3166 = relay.cosh(call_3162.astype('float32')) # shape=(1, 11, 10)
output = relay.Tuple([uop_3164,])
output2 = relay.Tuple([uop_3166,])
func_3169 = relay.Function([], output)
mod['func_3169'] = func_3169
mod = relay.transform.InferType()(mod)
output = func_3169()
func_3170 = relay.Function([], output)
mutated_mod['func_3170'] = func_3170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2155_call = mod.get_global_var('func_2155')
func_2156_call = mutated_mod.get_global_var('func_2156')
call_3223 = relay.TupleGetItem(func_2155_call(), 0)
call_3224 = relay.TupleGetItem(func_2156_call(), 0)
func_620_call = mod.get_global_var('func_620')
func_622_call = mutated_mod.get_global_var('func_622')
call_3233 = relay.TupleGetItem(func_620_call(), 0)
call_3234 = relay.TupleGetItem(func_622_call(), 0)
output = relay.Tuple([call_3223,call_3233,])
output2 = relay.Tuple([call_3224,call_3234,])
func_3237 = relay.Function([], output)
mod['func_3237'] = func_3237
mod = relay.transform.InferType()(mod)
mutated_mod['func_3237'] = func_3237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3237_call = mutated_mod.get_global_var('func_3237')
call_3238 = func_3237_call()
output = call_3238
func_3239 = relay.Function([], output)
mutated_mod['func_3239'] = func_3239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1981_call = mod.get_global_var('func_1981')
func_1983_call = mutated_mod.get_global_var('func_1983')
call_3247 = relay.TupleGetItem(func_1981_call(), 1)
call_3248 = relay.TupleGetItem(func_1983_call(), 1)
output = call_3247
output2 = call_3248
func_3250 = relay.Function([], output)
mod['func_3250'] = func_3250
mod = relay.transform.InferType()(mod)
mutated_mod['func_3250'] = func_3250
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3250_call = mutated_mod.get_global_var('func_3250')
call_3251 = func_3250_call()
output = call_3251
func_3252 = relay.Function([], output)
mutated_mod['func_3252'] = func_3252
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3266 = relay.var("var_3266", dtype = "float64", shape = (1, 9, 3))#candidate|3266|(1, 9, 3)|var|float64
uop_3267 = relay.erf(var_3266.astype('float64')) # shape=(1, 9, 3)
uop_3271 = relay.asinh(uop_3267.astype('float32')) # shape=(1, 9, 3)
output = uop_3271
output2 = uop_3271
func_3276 = relay.Function([var_3266,], output)
mod['func_3276'] = func_3276
mod = relay.transform.InferType()(mod)
var_3277 = relay.var("var_3277", dtype = "float64", shape = (1, 9, 3))#candidate|3277|(1, 9, 3)|var|float64
output = func_3276(var_3277)
func_3278 = relay.Function([var_3277], output)
mutated_mod['func_3278'] = func_3278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1862_call = mod.get_global_var('func_1862')
func_1863_call = mutated_mod.get_global_var('func_1863')
call_3283 = func_1862_call()
call_3284 = func_1862_call()
output = call_3283
output2 = call_3284
func_3293 = relay.Function([], output)
mod['func_3293'] = func_3293
mod = relay.transform.InferType()(mod)
output = func_3293()
func_3294 = relay.Function([], output)
mutated_mod['func_3294'] = func_3294
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3362 = relay.var("var_3362", dtype = "float64", shape = (8, 16, 15))#candidate|3362|(8, 16, 15)|var|float64
var_3363 = relay.var("var_3363", dtype = "float64", shape = (8, 16, 15))#candidate|3363|(8, 16, 15)|var|float64
bop_3364 = relay.divide(var_3362.astype('float64'), relay.reshape(var_3363.astype('float64'), relay.shape_of(var_3362))) # shape=(8, 16, 15)
func_2447_call = mod.get_global_var('func_2447')
func_2450_call = mutated_mod.get_global_var('func_2450')
const_3378 = relay.const([3,7,-1,7,-8,-10,-9,7,3,-5,2,-10,-5,2,-3,2,9,7,4,-2,4,-3,-10,-4,-10,-2,8,-3,-4,-5,-8,-4,-8,-6,4,7,1,2,2,-8,8,5,4,9,2,7,-10,-6,-2,3,2,6,1,9,-8,6,-7,-10,-8,10,-2,8,8,10,-6,-7,-2,6,-3,-9,-9,4,3,-8,-2,10,7,-8,2,4,3,-10,4,-10,-8,5,3,7,5,8,-6,-3,-6,8,1,8,5,8,-2,8,9,-1,-5,8,-6,9,-5,-6,5,9,-10,-9,2,6,-8,-8,-10,-7,9,-6,4,-8,-10,-9,10,3,2,-7,-9,-2,9,-4,-1,5,8,9,-9,-2,3,5,9,5,10,-8,5,8,2,-3,4,-6,-1,6,-2,-8,10,-10,3,-10,7,4,10,6,-3,-8,8,9,7,-9,4,3,5,2,-9,3,-2,10,8,-5,-6,7,-5,5,-2,2,-6,-3,-10,-8,-9,7,-5,-3,-2,3,-1,3,-7,-1,-5,-8,-10,9,-5,-9,8,-8,-10,8,-1,-9,3,10,10,-10,4,5,10,2,-3,-2,8,5,-10,9,8,-4,9,3,-5,4,5,-3,-3,10,7,-8,3,2,-10,5,-10,1,4,1,-8,-1,4,6,9,5,10,-1,-9,-6,-6,7,3,5,1,-1,1,-2,5,4,5,-10,-7,10,5,-4,-9,5,10,-1,6,-2,3,-1,3,10,9,5,-2,9,-10,-8,-6,3,5,-9,-6,-5,6,-7,3,8,-1,5,7,3,-9,-8,-6,-2,-7,-1,3,-3,-3,-7,10,-8,8,4,-9,5,-8,6,-6,-6,-1,-7,4,-3,-10,5,6,9,-7,9,10,6,9,-3,-10,9,5,-8,-5,7,-1,-7,4,-3,1,-8,8,-10,-6,3,9,9,-9,4,-6,-1,-1,-6,-6,-7,2,9,-1,-8,-9,5,4,-5,-9,-7,8,-3,-8,-6,-9,3,-2,3,1,-10,-4,-10,7,1,4,2,-8,3,-8,-2,3,10,8,-9,-7,-1,4,-1,-9,-8,10,5,8,4,8,-3,-1,-8,-8,-10,-6,6,-4,-2,9,8,-3,-7,-2,5,7,2,-10,-9,-5,-3,-1,10,6,-10,3,6,10,5,6,-1,9,-3,4,-7,-2,-2,9,-8,-6,-4,6,-5,5,8,1,6,-7,-8,10,1,-6,-5,-7,-4,5,3,7,-10,9,4,9,9,9,-6,3,-3,2,-7,-4,1,-8,1,-2,8,8,1,-3,5,10,-1,9,-3,3,-10,-3,-6,-7,6,7,1,7,-5,6,2,-1,8,-8,-3,-3,8,3,-6,-1,10,-8,3,6,-8,6,-6,-5,-7,7,4,2,-7,5,7,-8,4,-9,3,-5,-8,3,9,10,10,7,-9,-5,-6,-10,6,2,-3,-1,8,1,8,-10,1,3,7,-5,-1,-3,-1,-1,-8,-1,6,9,-7,-10,4,1,1,-9,6,-7,4,-3,2,6,-5,-2,6,-4,2,7,5,-3,4,7,6,4,-3,-9,-8,-4,9,-5,9,-9,3,-9,5,-7,6,6,9,5,6,-8,6,-9,-9,-1,2,-9,5,-5,4,9,5,3,5,5,-2,8,-4,3,1,-2,-4,-10,-3,-1,-5,6,-8,-4,-8,6,4,8,-1,1,-6,5,-8,-3,9,7,-4,6,3,-7,-10,3,-9,2,-3,-1,10,1,2,8,-7,5,-7,5,10,-10,-7,6,3,5,3,-7,4,10,1,5,-10,-1,-1,6,8,-4,9,10,-8,-10,-1,-7,-4,-10,4,2,6,-2,10,10,5,5,-4,8,10,-6,-6,5,-9,-4,2,8,9,-7,-7,9,1,-8,8,10,7,-8,-8,-10,8,1,-9,-8,-6,-9,3,8,3,10,3,9,7,-10,10,3,5,-8,2,5,4,-4,-4,-1,-8,8,5,1,5,-9,3,-3,-8,5,8,10,5,-8,-4,-8,2,-4,-3,10,-8,3,3,-4,-6,2,8,-7,-6,2,6,4,5,-6,5,-8,-5,8,6,10,8,7,6,9,-1,-3,2,-4,5,7,7,5,-8,-1,-3,-6,5,-7,7,4,-8,2,4,6,9,-1,1,-8,9,3,10,-4,-3,7,-8,6,8,5,8,-3,-7,3,2,-10,1,-2,-3,6,-9,5,-2,3,-1,-3,-2,-7,-3,-8,2,-6,1,1,-6,1,-10,3,7,3,6,8,4,-8,6,4,4,-8,-9,1,8,3,8,9,3,5,9,9,9,-4,3,-2,7,-6,-10,2,-10,-7,2,-4,-9,-6,10,-6,3,5,-6,-5,-6,-9,-9,-6,7,-5,-9,-4,8,1,-5,9,4,6,-9,-5,3,3,9,10,5,7,-6,6,-10,2,-1,5,-2,-9,3,8,-2,-9,4,-6,-7,-7,-3,5,-10,-1,7,-10,7,4,5,-8,-4,-7,6,-1,6,6,-3,-5,9,7,3,8,7,2,3,7,6,-10,-7,7,-1,7,5,8,-9,1,2,-2,1,-1,3,-6,1,-3,-8,-6,-3,-4,6,-4,9,-6,7,2,-3,4,2,-7,7,3,-2,4,-3,-4,10,-1,5,2,5,-10,6,4,-6,-10,3,-8,-4,8,1,-4,2,-2,5,9,-7,-10,-4,8,7,3,-1,3,-5,3,-7,-9,-6,-7,4,-3,-4,-1,-7,-8,-6,4,-4,-5,10,-5,8,-7,6,7,10,10,-3,2,-1,-6,-1,-8,-7,-6,-2,-5,6,7,6,1,-2,-9,1,6,-10,-10,-5,8,1,1,4,6,-10,1,4,3,2,-2,-1,-4,5,6,10,1,7,-5,-2,2,-1,-9,6,3,-1,-10,7,7,-9,1,-6,-1,6,5,-6,-9,1,-5,7], dtype = "int64")#candidate|3378|(1100,)|const|int64
call_3377 = relay.TupleGetItem(func_2447_call(relay.reshape(const_3378.astype('int64'), [550, 2])), 1)
call_3379 = relay.TupleGetItem(func_2450_call(relay.reshape(const_3378.astype('int64'), [550, 2])), 1)
func_1018_call = mod.get_global_var('func_1018')
func_1022_call = mutated_mod.get_global_var('func_1022')
var_3382 = relay.var("var_3382", dtype = "uint16", shape = (1320,))#candidate|3382|(1320,)|var|uint16
call_3381 = relay.TupleGetItem(func_1018_call(relay.reshape(var_3382.astype('uint16'), [12, 11, 10]), relay.reshape(var_3382.astype('uint8'), [12, 11, 10]), ), 0)
call_3383 = relay.TupleGetItem(func_1022_call(relay.reshape(var_3382.astype('uint16'), [12, 11, 10]), relay.reshape(var_3382.astype('uint8'), [12, 11, 10]), ), 0)
output = relay.Tuple([bop_3364,call_3377,const_3378,call_3381,var_3382,])
output2 = relay.Tuple([bop_3364,call_3379,const_3378,call_3383,var_3382,])
func_3384 = relay.Function([var_3362,var_3363,var_3382,], output)
mod['func_3384'] = func_3384
mod = relay.transform.InferType()(mod)
var_3385 = relay.var("var_3385", dtype = "float64", shape = (8, 16, 15))#candidate|3385|(8, 16, 15)|var|float64
var_3386 = relay.var("var_3386", dtype = "float64", shape = (8, 16, 15))#candidate|3386|(8, 16, 15)|var|float64
var_3387 = relay.var("var_3387", dtype = "uint16", shape = (1320,))#candidate|3387|(1320,)|var|uint16
output = func_3384(var_3385,var_3386,var_3387,)
func_3388 = relay.Function([var_3385,var_3386,var_3387,], output)
mutated_mod['func_3388'] = func_3388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3293_call = mod.get_global_var('func_3293')
func_3294_call = mutated_mod.get_global_var('func_3294')
call_3398 = func_3293_call()
call_3399 = func_3293_call()
func_1267_call = mod.get_global_var('func_1267')
func_1269_call = mutated_mod.get_global_var('func_1269')
var_3426 = relay.var("var_3426", dtype = "uint16", shape = (6, 220))#candidate|3426|(6, 220)|var|uint16
call_3425 = relay.TupleGetItem(func_1267_call(relay.reshape(var_3426.astype('uint16'), [1320,])), 0)
call_3427 = relay.TupleGetItem(func_1269_call(relay.reshape(var_3426.astype('uint16'), [1320,])), 0)
func_2668_call = mod.get_global_var('func_2668')
func_2670_call = mutated_mod.get_global_var('func_2670')
call_3445 = relay.TupleGetItem(func_2668_call(), 1)
call_3446 = relay.TupleGetItem(func_2670_call(), 1)
output = relay.Tuple([call_3398,call_3425,var_3426,call_3445,])
output2 = relay.Tuple([call_3399,call_3427,var_3426,call_3446,])
func_3448 = relay.Function([var_3426,], output)
mod['func_3448'] = func_3448
mod = relay.transform.InferType()(mod)
mutated_mod['func_3448'] = func_3448
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3449 = relay.var("var_3449", dtype = "uint16", shape = (6, 220))#candidate|3449|(6, 220)|var|uint16
func_3448_call = mutated_mod.get_global_var('func_3448')
call_3450 = func_3448_call(var_3449)
output = call_3450
func_3451 = relay.Function([var_3449], output)
mutated_mod['func_3451'] = func_3451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_497_call = mod.get_global_var('func_497')
func_498_call = mutated_mod.get_global_var('func_498')
call_3496 = relay.TupleGetItem(func_497_call(), 0)
call_3497 = relay.TupleGetItem(func_498_call(), 0)
output = relay.Tuple([call_3496,])
output2 = relay.Tuple([call_3497,])
func_3516 = relay.Function([], output)
mod['func_3516'] = func_3516
mod = relay.transform.InferType()(mod)
mutated_mod['func_3516'] = func_3516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3516_call = mutated_mod.get_global_var('func_3516')
call_3517 = func_3516_call()
output = call_3517
func_3518 = relay.Function([], output)
mutated_mod['func_3518'] = func_3518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1055_call = mod.get_global_var('func_1055')
func_1056_call = mutated_mod.get_global_var('func_1056')
call_3525 = relay.TupleGetItem(func_1055_call(), 0)
call_3526 = relay.TupleGetItem(func_1056_call(), 0)
output = relay.Tuple([call_3525,])
output2 = relay.Tuple([call_3526,])
func_3531 = relay.Function([], output)
mod['func_3531'] = func_3531
mod = relay.transform.InferType()(mod)
output = func_3531()
func_3532 = relay.Function([], output)
mutated_mod['func_3532'] = func_3532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1350_call = mod.get_global_var('func_1350')
func_1351_call = mutated_mod.get_global_var('func_1351')
call_3593 = relay.TupleGetItem(func_1350_call(), 0)
call_3594 = relay.TupleGetItem(func_1351_call(), 0)
uop_3595 = relay.acosh(call_3593.astype('float32')) # shape=(1, 11, 10)
uop_3597 = relay.acosh(call_3594.astype('float32')) # shape=(1, 11, 10)
output = uop_3595
output2 = uop_3597
func_3598 = relay.Function([], output)
mod['func_3598'] = func_3598
mod = relay.transform.InferType()(mod)
mutated_mod['func_3598'] = func_3598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3598_call = mutated_mod.get_global_var('func_3598')
call_3599 = func_3598_call()
output = call_3599
func_3600 = relay.Function([], output)
mutated_mod['func_3600'] = func_3600
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3531_call = mod.get_global_var('func_3531')
func_3532_call = mutated_mod.get_global_var('func_3532')
call_3714 = relay.TupleGetItem(func_3531_call(), 0)
call_3715 = relay.TupleGetItem(func_3532_call(), 0)
func_2813_call = mod.get_global_var('func_2813')
func_2815_call = mutated_mod.get_global_var('func_2815')
call_3727 = relay.TupleGetItem(func_2813_call(), 0)
call_3728 = relay.TupleGetItem(func_2815_call(), 0)
output = relay.Tuple([call_3714,call_3727,])
output2 = relay.Tuple([call_3715,call_3728,])
func_3734 = relay.Function([], output)
mod['func_3734'] = func_3734
mod = relay.transform.InferType()(mod)
output = func_3734()
func_3735 = relay.Function([], output)
mutated_mod['func_3735'] = func_3735
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3885 = relay.var("var_3885", dtype = "float32", shape = (11, 7, 13))#candidate|3885|(11, 7, 13)|var|float32
const_3886 = relay.const([[[1.208424,-0.231089,-7.124142,0.554912,6.148295,9.975473,6.085363,7.173474,5.640041,-7.361484,-6.137647,0.867299,-0.208800],[2.122367,5.372326,-8.721338,3.504345,-7.128533,-7.212327,1.983741,0.349569,-0.684030,8.987866,7.349944,5.387099,-7.711647],[6.992949,3.659213,9.171132,9.801304,-0.942495,3.218976,-5.688222,4.302557,-0.164038,2.672949,3.898070,-0.917008,9.886482],[6.557559,3.583329,-4.600855,-6.338478,8.989870,-8.667020,-3.274520,-6.818665,9.580400,5.146586,-0.216621,8.955716,9.784311],[3.572310,7.862833,1.148236,-2.919785,3.110476,7.273815,-2.975226,4.929828,-9.757091,5.785271,5.962556,0.015406,-6.882583],[-8.136256,0.794510,-4.325951,7.985115,-0.058893,2.717564,-2.457934,6.297705,-7.049830,-6.737914,5.755629,8.380199,7.237730],[4.837279,1.058700,-2.822342,7.587283,-6.699678,7.328062,1.070324,-9.004600,-6.894972,9.402729,2.795988,6.689028,3.191138]],[[-6.483288,-6.179244,-5.620761,-1.413355,4.601241,3.679621,9.366156,-0.446612,-8.543806,-2.142159,-0.097801,7.261426,-7.215955],[9.214538,-7.287821,-9.402677,4.468233,-0.901553,-0.909624,-1.686131,-8.034184,-8.181901,8.087893,-6.135335,3.695235,-0.664324],[9.020378,9.163916,-2.162677,7.035572,-2.960492,3.448739,-6.897929,8.800356,1.962630,-4.873724,3.085561,9.133881,-6.634554],[-7.544632,-4.700895,0.840946,-6.007384,8.149111,-9.066397,7.265971,5.786745,-6.859290,6.596152,-8.622006,7.822934,-9.284632],[-6.146787,5.848436,2.322222,-1.186448,6.834516,2.921636,-5.384781,-0.967286,6.105866,6.465028,6.397455,1.239729,8.061037],[1.667489,-0.942897,-5.261543,0.447970,2.196753,0.676527,-3.096525,-2.586997,3.700327,-4.562653,9.012498,2.024234,-5.348587],[-5.065947,1.583913,-3.368456,6.950351,-2.195932,5.187787,9.054786,-4.726364,-8.853254,2.580595,-0.160031,1.767287,2.101633]],[[0.835726,-4.349230,5.509887,8.241772,-5.412862,4.442269,-7.825013,8.419827,9.644963,6.985156,-7.341927,-7.609811,-3.510608],[-6.772289,9.257998,-4.741557,-3.112429,8.173325,0.088739,5.953887,-4.604359,2.356533,-7.762034,-9.260132,-7.727706,-2.737088],[4.403884,-9.812892,9.017621,2.263177,-9.056794,4.884820,-9.104654,-3.628540,7.145458,-6.669124,-2.470491,5.084457,-3.497715],[-1.133182,8.880766,5.310753,1.477557,-0.974621,-9.564626,-2.945389,4.294688,-2.086485,-9.287417,7.824524,-6.490864,7.093031],[-6.469760,0.977941,-4.746241,2.325794,-9.896864,-9.612724,-1.428558,9.312939,-8.271339,-2.428197,4.041843,-3.615458,0.186330],[-0.589083,4.553664,1.953286,-6.894031,-1.276224,-3.102381,-2.279320,2.096117,4.188351,0.489569,-8.740907,-8.193676,5.151748],[0.178519,7.459420,8.226202,-3.588757,1.871182,-5.294250,9.789056,-7.440935,-5.327673,-2.192750,2.561973,-0.368731,-3.450808]],[[-7.475154,1.546981,0.613756,0.571203,6.911604,-1.193333,1.933789,9.846507,1.260264,0.534276,7.642187,-5.883397,1.430648],[2.060117,-2.811437,-6.251469,-8.347829,-9.713856,6.363330,-3.102454,-7.790375,-1.914089,-8.275857,-3.381501,-4.061911,5.000703],[5.207855,-9.050949,7.638305,-1.819037,2.363909,-5.959847,-0.301750,4.541406,0.058336,2.904031,-4.379726,5.572315,6.357359],[-3.816845,0.135819,9.657652,5.599633,7.585254,0.864200,-4.930348,9.482855,-8.169681,5.605381,0.618208,0.893245,6.053083],[-1.478946,-5.823415,-8.179785,-5.076078,-2.238846,-3.559375,7.618772,-9.840896,-3.118471,7.927664,-0.566489,1.697490,-7.766901],[-9.469064,9.812615,7.322232,-6.053008,-1.991460,0.581222,7.065420,-1.681615,1.119403,7.110037,9.867507,0.295075,1.028743],[-4.424951,5.316342,9.392199,9.309221,0.678365,3.007943,-7.178526,-8.100683,-4.222569,-2.367145,-2.359648,-7.824774,0.075016]],[[7.374140,-6.994128,-5.517836,2.321932,9.792904,1.508526,-0.474866,-6.812717,0.527240,2.071718,-5.367734,4.997912,-4.759554],[-6.265980,9.905561,-4.061993,-6.972448,-9.732149,-5.823077,8.773599,-1.121015,-0.866559,1.583525,-3.778468,7.645578,9.174599],[4.782179,-1.783762,-5.750738,-0.187447,0.594435,-1.434688,-6.314881,-5.169412,-6.804912,-1.799498,0.148382,5.575893,9.955112],[2.452604,1.323626,-6.143530,2.042002,2.019950,-0.053821,6.419099,-6.549407,2.180465,-2.825263,9.386031,8.133338,-0.429230],[-2.986499,-2.616667,0.415476,6.545033,-0.236052,-2.717612,-8.494139,9.881997,5.505488,-3.399395,-2.887760,-9.961624,-0.414228],[0.675192,-1.727033,-3.708348,-4.507182,-7.914693,-8.567018,-1.713535,-3.491890,-4.279383,-8.230578,1.139058,-4.744495,-7.283114],[1.444354,-4.053860,-3.467689,-3.976469,2.016055,-3.998386,2.779883,0.055919,-7.779541,-4.713641,-9.871774,5.529775,-9.724111]],[[0.701147,1.199012,1.376447,-8.454990,-4.005936,4.736437,5.850189,3.752785,-2.330310,4.954535,-2.419918,-2.777579,-5.671450],[5.931171,1.230824,-8.312138,-2.682971,-5.307289,-4.697592,4.102446,-7.108354,8.756939,9.535430,1.725855,3.422659,-6.641526],[-4.554767,-6.387555,2.485271,-9.373388,7.961378,6.493636,-7.360191,5.205760,5.940852,8.663623,-7.713725,5.042267,3.001048],[6.636194,5.416189,-4.077010,-8.539834,-9.449209,-2.240243,9.174487,0.774140,-4.943407,-6.361702,3.081396,-0.525932,1.377089],[6.772028,1.796343,9.653292,-6.958675,-3.415058,-2.697273,5.779296,-9.104199,-6.317178,-1.729079,4.212989,7.567089,-8.401173],[1.342301,-4.132874,2.892849,6.763508,-8.640339,-9.841720,-7.144636,-8.866173,3.197551,3.522130,3.436075,3.361928,-5.152800],[-3.348789,8.463238,-2.923270,-3.039929,8.109253,-7.412678,-7.777757,-0.807465,0.150856,0.279525,3.858260,-1.140999,-8.785833]],[[-1.443444,7.791575,-5.068834,1.947517,-2.226906,-9.137626,-4.298845,1.653589,2.335258,4.805246,-9.873660,-7.481437,-2.171921],[-3.852195,-4.206481,5.736325,8.104277,6.382114,-4.862495,4.544543,-3.427042,6.453780,9.364076,-0.323718,-7.083303,-0.010687],[-0.622649,-0.969059,6.140507,0.930165,-1.517047,-5.012436,9.237175,7.630175,-9.857103,0.852483,6.019592,1.419880,4.897771],[3.492387,-5.905096,-1.681736,-5.176755,2.524815,3.331241,0.685576,6.595147,4.045278,-9.787417,3.246193,9.304875,2.425946],[9.782779,-6.697774,-2.984217,6.548215,3.605032,-9.349198,-0.451631,8.404384,-3.522125,3.988403,0.059219,2.713857,-8.275852],[-0.287780,2.815521,-1.945710,8.827530,0.856921,-7.253923,-2.747284,-0.300138,9.946503,-2.310273,-0.921898,6.468606,9.337225],[0.221520,-9.280231,1.918702,3.247479,5.294702,7.732066,-5.668022,-8.670152,1.384138,9.794514,4.922653,4.778808,2.564384]],[[0.015069,5.651130,0.118470,9.496115,-4.432575,9.348794,9.546859,3.235578,3.510526,0.378764,-2.407106,-6.154351,-8.974258],[-8.831297,5.154890,1.713260,8.560469,5.985490,1.893938,-3.757153,6.494500,-7.153821,-6.093142,-1.066714,0.068043,-0.493101],[-1.267739,6.026917,-0.743267,-0.196660,-0.122036,-8.037567,3.729558,-7.572780,-6.157524,-0.047295,-3.521644,-0.942763,5.653475],[-2.494340,-5.896222,-2.732446,4.332102,9.621506,-6.427734,-6.906556,-3.417410,-0.335435,-9.090653,-0.373582,5.653197,6.791756],[9.431698,3.692378,-3.824577,-1.946839,-0.442891,7.440142,-6.516382,7.472983,7.950262,0.604706,7.418912,7.226344,5.146040],[-0.758758,-8.380840,-2.764759,-7.320761,-5.801931,-0.954595,5.605262,-5.882856,-4.675723,-2.703444,9.152199,4.825849,4.385072],[-2.628525,6.428342,-5.441038,-5.226781,3.315218,0.708009,-9.870747,-8.880252,-4.018400,2.898553,-8.537721,2.681926,-5.203976]],[[-2.907404,-4.796899,-4.142266,-3.157233,-4.720521,2.900799,-6.833448,6.087462,-6.083206,3.301735,-2.719400,7.698536,-7.037205],[-0.100050,-3.338944,-9.411469,-5.521857,-5.891435,7.484912,-8.516420,4.335060,2.502252,-0.414145,5.252203,-0.357833,6.625236],[-6.086159,6.441887,6.516007,6.541050,-4.442075,-7.382980,-7.840899,1.482230,-8.398577,4.246032,2.258076,6.420477,8.698538],[5.083610,8.064897,7.631103,0.594428,9.610358,-3.346815,-4.611498,-3.097387,8.315255,7.862869,5.845228,9.648579,0.333147],[8.192139,-6.451203,-6.533215,-7.678046,2.947257,1.373113,-9.078954,3.887692,1.310118,2.615073,-6.653005,-5.164027,0.864322],[2.247501,-5.114171,-3.401668,9.327760,5.132030,-1.230030,-5.384733,8.787723,-0.159304,-9.416103,-6.734292,7.799073,2.750685],[-9.370033,6.801450,7.537790,-7.549299,2.112432,1.593666,-3.733446,-9.408324,1.522130,-4.468816,7.709088,-1.399758,-1.041712]],[[0.981748,0.173535,9.146092,3.468384,4.796889,-6.883671,-5.435740,-5.882052,-1.124279,-4.476981,0.515373,1.589709,-7.682230],[-5.274060,-4.459901,0.662632,-4.778413,6.242624,4.977913,-4.165166,1.503311,-3.865355,7.624184,-7.187776,1.072035,-5.078827],[-2.218612,-3.543374,-9.022916,2.385349,8.604482,8.300191,2.536551,-7.303081,8.011015,-6.893352,9.594586,-0.647903,0.616349],[-8.092686,-8.357949,-6.652719,0.370445,1.010438,3.143541,-9.749696,-1.146588,7.144536,-5.345362,-2.509788,-1.862802,7.062931],[6.794105,-3.473333,-5.935176,-1.885890,-2.700734,9.074627,8.324943,8.838208,7.733489,-4.786429,1.010234,-3.817922,9.042655],[9.514660,3.697716,4.288857,8.646420,2.273652,-4.478236,-9.587037,-4.582723,-8.471473,-4.996031,8.371547,-4.287579,6.373396],[8.192087,3.886544,-3.282345,-2.386255,5.126730,0.393032,-1.158667,-9.257451,-0.423742,0.730773,-0.818663,-4.311407,0.725912]],[[4.930061,6.978607,-7.897204,-2.515466,2.233576,-2.346984,-8.606755,9.723266,-2.172790,-6.583028,5.780438,9.967989,-4.942704],[-2.089694,9.755998,-3.636282,7.072941,5.693868,-5.520060,-2.584384,6.768119,3.559075,-3.774364,5.744196,-9.618136,-7.735812],[-4.346093,-7.757688,9.693053,1.911473,0.454850,1.033761,-5.877565,-4.797424,-6.537568,-7.329462,1.410020,1.145849,0.294775],[2.341868,5.841280,7.521092,2.126959,-9.510595,-1.653683,7.883651,5.452575,4.820903,-3.161364,-7.475741,-5.876234,-5.835419],[-5.022486,6.101053,-7.743116,-0.184350,-6.983042,4.533911,3.312092,8.140141,5.777880,3.838054,2.684729,-9.307909,-5.552698],[1.928634,-9.867771,5.209496,6.027343,-9.827649,2.288808,4.526172,-8.173312,8.975460,-4.605784,8.454785,-2.464052,-9.369072],[0.433613,9.491193,0.698779,-6.689849,-8.883519,7.264913,2.381408,1.867044,-7.298941,-5.153069,3.208213,-0.009261,-6.443225]]], dtype = "float32")#candidate|3886|(11, 7, 13)|const|float32
bop_3887 = relay.floor_divide(var_3885.astype('float32'), relay.reshape(const_3886.astype('float32'), relay.shape_of(var_3885))) # shape=(11, 7, 13)
func_2123_call = mod.get_global_var('func_2123')
func_2125_call = mutated_mod.get_global_var('func_2125')
var_3892 = relay.var("var_3892", dtype = "bool", shape = (7, 140))#candidate|3892|(7, 140)|var|bool
call_3891 = func_2123_call(relay.reshape(var_3892.astype('bool'), [14, 5, 14]))
call_3893 = func_2123_call(relay.reshape(var_3892.astype('bool'), [14, 5, 14]))
func_620_call = mod.get_global_var('func_620')
func_622_call = mutated_mod.get_global_var('func_622')
call_3895 = relay.TupleGetItem(func_620_call(), 1)
call_3896 = relay.TupleGetItem(func_622_call(), 1)
output = relay.Tuple([bop_3887,call_3891,var_3892,call_3895,])
output2 = relay.Tuple([bop_3887,call_3893,var_3892,call_3896,])
func_3901 = relay.Function([var_3885,var_3892,], output)
mod['func_3901'] = func_3901
mod = relay.transform.InferType()(mod)
mutated_mod['func_3901'] = func_3901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3901_call = mutated_mod.get_global_var('func_3901')
var_3903 = relay.var("var_3903", dtype = "float32", shape = (11, 7, 13))#candidate|3903|(11, 7, 13)|var|float32
var_3904 = relay.var("var_3904", dtype = "bool", shape = (7, 140))#candidate|3904|(7, 140)|var|bool
call_3902 = func_3901_call(var_3903,var_3904,)
output = call_3902
func_3905 = relay.Function([var_3903,var_3904,], output)
mutated_mod['func_3905'] = func_3905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_497_call = mod.get_global_var('func_497')
func_498_call = mutated_mod.get_global_var('func_498')
call_4052 = relay.TupleGetItem(func_497_call(), 0)
call_4053 = relay.TupleGetItem(func_498_call(), 0)
func_898_call = mod.get_global_var('func_898')
func_900_call = mutated_mod.get_global_var('func_900')
call_4057 = relay.TupleGetItem(func_898_call(), 1)
call_4058 = relay.TupleGetItem(func_900_call(), 1)
output = relay.Tuple([call_4052,call_4057,])
output2 = relay.Tuple([call_4053,call_4058,])
func_4059 = relay.Function([], output)
mod['func_4059'] = func_4059
mod = relay.transform.InferType()(mod)
mutated_mod['func_4059'] = func_4059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4059_call = mutated_mod.get_global_var('func_4059')
call_4060 = func_4059_call()
output = call_4060
func_4061 = relay.Function([], output)
mutated_mod['func_4061'] = func_4061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3598_call = mod.get_global_var('func_3598')
func_3600_call = mutated_mod.get_global_var('func_3600')
call_4062 = func_3598_call()
call_4063 = func_3598_call()
func_3250_call = mod.get_global_var('func_3250')
func_3252_call = mutated_mod.get_global_var('func_3252')
call_4070 = func_3250_call()
call_4071 = func_3250_call()
uop_4093 = relay.exp(call_4062.astype('float64')) # shape=(1, 11, 10)
uop_4095 = relay.exp(call_4063.astype('float64')) # shape=(1, 11, 10)
output = relay.Tuple([call_4070,uop_4093,])
output2 = relay.Tuple([call_4071,uop_4095,])
func_4098 = relay.Function([], output)
mod['func_4098'] = func_4098
mod = relay.transform.InferType()(mod)
mutated_mod['func_4098'] = func_4098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4098_call = mutated_mod.get_global_var('func_4098')
call_4099 = func_4098_call()
output = call_4099
func_4100 = relay.Function([], output)
mutated_mod['func_4100'] = func_4100
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4059_call = mod.get_global_var('func_4059')
func_4061_call = mutated_mod.get_global_var('func_4061')
call_4116 = relay.TupleGetItem(func_4059_call(), 0)
call_4117 = relay.TupleGetItem(func_4061_call(), 0)
output = call_4116
output2 = call_4117
func_4132 = relay.Function([], output)
mod['func_4132'] = func_4132
mod = relay.transform.InferType()(mod)
output = func_4132()
func_4133 = relay.Function([], output)
mutated_mod['func_4133'] = func_4133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2632_call = mod.get_global_var('func_2632')
func_2634_call = mutated_mod.get_global_var('func_2634')
call_4140 = relay.TupleGetItem(func_2632_call(), 3)
call_4141 = relay.TupleGetItem(func_2634_call(), 3)
func_1714_call = mod.get_global_var('func_1714')
func_1716_call = mutated_mod.get_global_var('func_1716')
call_4167 = relay.TupleGetItem(func_1714_call(), 1)
call_4168 = relay.TupleGetItem(func_1716_call(), 1)
bop_4170 = relay.add(call_4167.astype('int8'), relay.reshape(call_4140.astype('int8'), relay.shape_of(call_4167))) # shape=(1, 11, 10)
bop_4173 = relay.add(call_4168.astype('int8'), relay.reshape(call_4141.astype('int8'), relay.shape_of(call_4168))) # shape=(1, 11, 10)
uop_4179 = relay.sqrt(call_4140.astype('float32')) # shape=(1, 11, 10)
uop_4181 = relay.sqrt(call_4141.astype('float32')) # shape=(1, 11, 10)
bop_4182 = relay.less(uop_4179.astype('bool'), relay.reshape(call_4167.astype('bool'), relay.shape_of(uop_4179))) # shape=(1, 11, 10)
bop_4185 = relay.less(uop_4181.astype('bool'), relay.reshape(call_4168.astype('bool'), relay.shape_of(uop_4181))) # shape=(1, 11, 10)
output = relay.Tuple([bop_4170,bop_4182,])
output2 = relay.Tuple([bop_4173,bop_4185,])
func_4196 = relay.Function([], output)
mod['func_4196'] = func_4196
mod = relay.transform.InferType()(mod)
mutated_mod['func_4196'] = func_4196
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4196_call = mutated_mod.get_global_var('func_4196')
call_4197 = func_4196_call()
output = call_4197
func_4198 = relay.Function([], output)
mutated_mod['func_4198'] = func_4198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4196_call = mod.get_global_var('func_4196')
func_4198_call = mutated_mod.get_global_var('func_4198')
call_4217 = relay.TupleGetItem(func_4196_call(), 0)
call_4218 = relay.TupleGetItem(func_4198_call(), 0)
output = call_4217
output2 = call_4218
func_4231 = relay.Function([], output)
mod['func_4231'] = func_4231
mod = relay.transform.InferType()(mod)
mutated_mod['func_4231'] = func_4231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4231_call = mutated_mod.get_global_var('func_4231')
call_4232 = func_4231_call()
output = call_4232
func_4233 = relay.Function([], output)
mutated_mod['func_4233'] = func_4233
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4243 = relay.var("var_4243", dtype = "float32", shape = (14, 13, 9))#candidate|4243|(14, 13, 9)|var|float32
uop_4244 = relay.exp(var_4243.astype('float32')) # shape=(14, 13, 9)
output = uop_4244
output2 = uop_4244
func_4250 = relay.Function([var_4243,], output)
mod['func_4250'] = func_4250
mod = relay.transform.InferType()(mod)
mutated_mod['func_4250'] = func_4250
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4251 = relay.var("var_4251", dtype = "float32", shape = (14, 13, 9))#candidate|4251|(14, 13, 9)|var|float32
func_4250_call = mutated_mod.get_global_var('func_4250')
call_4252 = func_4250_call(var_4251)
output = call_4252
func_4253 = relay.Function([var_4251], output)
mutated_mod['func_4253'] = func_4253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4132_call = mod.get_global_var('func_4132')
func_4133_call = mutated_mod.get_global_var('func_4133')
call_4281 = func_4132_call()
call_4282 = func_4132_call()
output = call_4281
output2 = call_4282
func_4287 = relay.Function([], output)
mod['func_4287'] = func_4287
mod = relay.transform.InferType()(mod)
output = func_4287()
func_4288 = relay.Function([], output)
mutated_mod['func_4288'] = func_4288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3598_call = mod.get_global_var('func_3598')
func_3600_call = mutated_mod.get_global_var('func_3600')
call_4330 = func_3598_call()
call_4331 = func_3598_call()
func_2938_call = mod.get_global_var('func_2938')
func_2940_call = mutated_mod.get_global_var('func_2940')
call_4335 = relay.TupleGetItem(func_2938_call(), 0)
call_4336 = relay.TupleGetItem(func_2940_call(), 0)
output = relay.Tuple([call_4330,call_4335,])
output2 = relay.Tuple([call_4331,call_4336,])
func_4341 = relay.Function([], output)
mod['func_4341'] = func_4341
mod = relay.transform.InferType()(mod)
output = func_4341()
func_4342 = relay.Function([], output)
mutated_mod['func_4342'] = func_4342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1350_call = mod.get_global_var('func_1350')
func_1351_call = mutated_mod.get_global_var('func_1351')
call_4392 = relay.TupleGetItem(func_1350_call(), 0)
call_4393 = relay.TupleGetItem(func_1351_call(), 0)
output = call_4392
output2 = call_4393
func_4403 = relay.Function([], output)
mod['func_4403'] = func_4403
mod = relay.transform.InferType()(mod)
output = func_4403()
func_4404 = relay.Function([], output)
mutated_mod['func_4404'] = func_4404
mutated_mod = relay.transform.InferType()(mutated_mod)
func_898_call = mod.get_global_var('func_898')
func_900_call = mutated_mod.get_global_var('func_900')
call_4429 = relay.TupleGetItem(func_898_call(), 0)
call_4430 = relay.TupleGetItem(func_900_call(), 0)
func_898_call = mod.get_global_var('func_898')
func_900_call = mutated_mod.get_global_var('func_900')
call_4433 = relay.TupleGetItem(func_898_call(), 1)
call_4434 = relay.TupleGetItem(func_900_call(), 1)
uop_4454 = relay.log2(call_4433.astype('float32')) # shape=(1, 11, 10)
uop_4456 = relay.log2(call_4434.astype('float32')) # shape=(1, 11, 10)
output = relay.Tuple([call_4429,uop_4454,])
output2 = relay.Tuple([call_4430,uop_4456,])
func_4457 = relay.Function([], output)
mod['func_4457'] = func_4457
mod = relay.transform.InferType()(mod)
output = func_4457()
func_4458 = relay.Function([], output)
mutated_mod['func_4458'] = func_4458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4132_call = mod.get_global_var('func_4132')
func_4133_call = mutated_mod.get_global_var('func_4133')
call_4461 = func_4132_call()
call_4462 = func_4132_call()
func_2357_call = mod.get_global_var('func_2357')
func_2360_call = mutated_mod.get_global_var('func_2360')
var_4470 = relay.var("var_4470", dtype = "uint32", shape = ())#candidate|4470|()|var|uint32
call_4469 = relay.TupleGetItem(func_2357_call(relay.reshape(var_4470.astype('uint32'), [])), 1)
call_4471 = relay.TupleGetItem(func_2360_call(relay.reshape(var_4470.astype('uint32'), [])), 1)
func_4457_call = mod.get_global_var('func_4457')
func_4458_call = mutated_mod.get_global_var('func_4458')
call_4473 = relay.TupleGetItem(func_4457_call(), 1)
call_4474 = relay.TupleGetItem(func_4458_call(), 1)
output = relay.Tuple([call_4461,call_4469,var_4470,call_4473,])
output2 = relay.Tuple([call_4462,call_4471,var_4470,call_4474,])
func_4476 = relay.Function([var_4470,], output)
mod['func_4476'] = func_4476
mod = relay.transform.InferType()(mod)
mutated_mod['func_4476'] = func_4476
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4477 = relay.var("var_4477", dtype = "uint32", shape = ())#candidate|4477|()|var|uint32
func_4476_call = mutated_mod.get_global_var('func_4476')
call_4478 = func_4476_call(var_4477)
output = call_4478
func_4479 = relay.Function([var_4477], output)
mutated_mod['func_4479'] = func_4479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3250_call = mod.get_global_var('func_3250')
func_3252_call = mutated_mod.get_global_var('func_3252')
call_4549 = func_3250_call()
call_4550 = func_3250_call()
var_4558 = relay.var("var_4558", dtype = "uint16", shape = (14, 11, 10))#candidate|4558|(14, 11, 10)|var|uint16
bop_4559 = relay.power(call_4549.astype('float64'), var_4558.astype('float64')) # shape=(14, 11, 10)
bop_4562 = relay.power(call_4550.astype('float64'), var_4558.astype('float64')) # shape=(14, 11, 10)
bop_4563 = relay.subtract(call_4549.astype('float32'), bop_4559.astype('float32')) # shape=(14, 11, 10)
bop_4566 = relay.subtract(call_4550.astype('float32'), bop_4562.astype('float32')) # shape=(14, 11, 10)
bop_4573 = relay.minimum(bop_4563.astype('float32'), relay.reshape(bop_4559.astype('float32'), relay.shape_of(bop_4563))) # shape=(14, 11, 10)
bop_4576 = relay.minimum(bop_4566.astype('float32'), relay.reshape(bop_4562.astype('float32'), relay.shape_of(bop_4566))) # shape=(14, 11, 10)
uop_4580 = relay.asin(bop_4573.astype('float64')) # shape=(14, 11, 10)
uop_4582 = relay.asin(bop_4576.astype('float64')) # shape=(14, 11, 10)
output = uop_4580
output2 = uop_4582
func_4597 = relay.Function([var_4558,], output)
mod['func_4597'] = func_4597
mod = relay.transform.InferType()(mod)
var_4598 = relay.var("var_4598", dtype = "uint16", shape = (14, 11, 10))#candidate|4598|(14, 11, 10)|var|uint16
output = func_4597(var_4598)
func_4599 = relay.Function([var_4598], output)
mutated_mod['func_4599'] = func_4599
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2697_call = mod.get_global_var('func_2697')
func_2698_call = mutated_mod.get_global_var('func_2698')
call_4638 = relay.TupleGetItem(func_2697_call(), 1)
call_4639 = relay.TupleGetItem(func_2698_call(), 1)
uop_4649 = relay.log2(call_4638.astype('float32')) # shape=(2, 9, 10)
uop_4651 = relay.log2(call_4639.astype('float32')) # shape=(2, 9, 10)
output = uop_4649
output2 = uop_4651
func_4661 = relay.Function([], output)
mod['func_4661'] = func_4661
mod = relay.transform.InferType()(mod)
output = func_4661()
func_4662 = relay.Function([], output)
mutated_mod['func_4662'] = func_4662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1350_call = mod.get_global_var('func_1350')
func_1351_call = mutated_mod.get_global_var('func_1351')
call_4663 = relay.TupleGetItem(func_1350_call(), 0)
call_4664 = relay.TupleGetItem(func_1351_call(), 0)
var_4665 = relay.var("var_4665", dtype = "uint16", shape = (4, 11, 10))#candidate|4665|(4, 11, 10)|var|uint16
bop_4666 = relay.bitwise_xor(call_4663.astype('uint8'), var_4665.astype('uint8')) # shape=(4, 11, 10)
bop_4669 = relay.bitwise_xor(call_4664.astype('uint8'), var_4665.astype('uint8')) # shape=(4, 11, 10)
output = relay.Tuple([bop_4666,])
output2 = relay.Tuple([bop_4669,])
func_4670 = relay.Function([var_4665,], output)
mod['func_4670'] = func_4670
mod = relay.transform.InferType()(mod)
mutated_mod['func_4670'] = func_4670
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4671 = relay.var("var_4671", dtype = "uint16", shape = (4, 11, 10))#candidate|4671|(4, 11, 10)|var|uint16
func_4670_call = mutated_mod.get_global_var('func_4670')
call_4672 = func_4670_call(var_4671)
output = call_4672
func_4673 = relay.Function([var_4671], output)
mutated_mod['func_4673'] = func_4673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3237_call = mod.get_global_var('func_3237')
func_3239_call = mutated_mod.get_global_var('func_3239')
call_4738 = relay.TupleGetItem(func_3237_call(), 1)
call_4739 = relay.TupleGetItem(func_3239_call(), 1)
uop_4744 = relay.log10(call_4738.astype('float32')) # shape=(1, 11, 10)
uop_4746 = relay.log10(call_4739.astype('float32')) # shape=(1, 11, 10)
func_1714_call = mod.get_global_var('func_1714')
func_1716_call = mutated_mod.get_global_var('func_1716')
call_4749 = relay.TupleGetItem(func_1714_call(), 1)
call_4750 = relay.TupleGetItem(func_1716_call(), 1)
output = relay.Tuple([uop_4744,call_4749,])
output2 = relay.Tuple([uop_4746,call_4750,])
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
const_4763 = relay.const([[[-4.519436,0.574788,2.818063,1.190804,-0.056237,-9.922695,1.673353,-2.710135,-1.189877,3.725615,-7.376064,2.426418,-4.304163],[9.849097,6.191299,-8.230997,-0.012284,0.508535,-1.068913,2.016831,-8.501619,-1.024454,-6.727909,9.784851,-2.974445,2.733621],[-1.607908,-3.782887,8.602080,-1.866893,9.520943,-8.437370,-1.415820,7.198968,-4.976853,0.068014,-2.556634,2.686987,-9.040345]],[[-1.074522,6.358408,0.971852,-0.399554,-0.251027,7.996999,-1.923871,1.403154,-0.435838,-4.183964,-8.384662,-8.530589,7.580695],[4.096003,-0.337446,5.921575,0.645867,-8.078104,-7.746237,-0.134918,4.406953,4.165096,-0.056653,-0.645782,-2.848678,5.032912],[-2.071018,-9.472651,-0.053280,-7.845613,4.544184,1.801508,-8.290156,7.881672,-8.528879,0.311607,-0.746090,5.682719,2.292285]],[[9.640421,2.389442,-7.819198,4.107888,7.561093,-9.997079,-6.994570,-9.166346,-6.786502,2.721162,3.440950,-6.956698,4.134826],[-0.666933,9.168438,6.557261,9.149778,1.067392,-3.490802,9.756315,8.065223,5.803543,1.905698,7.143531,-1.401348,-1.925024],[5.639059,-2.961457,4.465087,8.072193,-6.170104,1.136986,0.754073,3.972614,6.393657,-1.959049,-0.134348,-7.635625,4.498967]],[[-9.591599,5.425875,9.269356,1.197326,3.577067,-3.683157,2.993690,8.312905,6.485301,-5.847148,-4.027546,7.673675,-6.839189],[-9.330983,1.964839,-7.211052,1.909272,-4.281796,-8.335311,-6.025279,-4.683185,8.437631,1.458157,1.521474,1.956107,4.616874],[0.108557,-6.345075,8.780248,5.556708,-1.918005,-1.995456,6.007513,4.278063,-8.149972,8.439465,-5.543364,-3.634922,-3.145604]],[[-2.987320,0.815116,1.534171,-7.442562,-0.721149,3.393537,8.423069,-2.183219,9.490348,-3.568653,6.206701,4.333197,-8.841830],[7.352138,3.282560,-2.899854,-3.171043,-3.446731,-5.807665,9.713578,-2.351034,-1.630008,4.862228,2.827428,-9.237484,8.775776],[-3.069485,9.933692,-7.424823,2.481409,-6.716867,-8.643496,-7.809231,-9.476140,1.554950,8.679442,-4.160886,6.843506,-8.544656]],[[8.157370,6.891085,0.017419,2.021389,-6.933469,7.539851,5.793412,8.091951,-5.640810,-9.976329,-7.239051,1.281626,1.276180],[-9.468102,1.432965,2.474334,8.519340,0.066000,-5.609075,4.520772,-3.488933,5.128653,-0.418764,2.328370,-0.168816,-2.737496],[-4.459803,-8.083438,3.333425,-8.406488,-0.671469,8.726478,-8.012733,-7.391227,1.920474,3.887183,-5.793060,-8.642836,9.895656]],[[-9.555738,9.316409,3.368563,-6.452725,-7.082651,-5.396615,-4.580866,-8.804444,-5.064463,-5.238868,-0.665189,7.266080,5.426416],[-2.517888,-0.595314,-3.755165,1.118482,4.260734,3.262700,-7.425940,-3.249269,-5.551788,1.532565,-4.373902,-8.151005,-8.821554],[4.031001,-7.027762,-2.246519,-5.142914,5.379626,2.438162,-4.466448,2.190360,-1.731373,8.843377,-5.560442,8.161164,2.750536]],[[7.300187,-1.506432,-2.132081,5.803377,-1.041831,8.326674,0.234352,1.564817,5.874090,2.374740,1.536448,-1.961949,-3.413993],[9.350748,2.244767,-8.348800,-5.944671,-8.518441,-1.754854,5.794712,2.888291,6.553140,7.347936,6.612231,-4.828252,2.607718],[-1.717432,6.499541,-7.532562,-9.532091,2.316940,7.751517,0.011112,-8.927955,7.441962,9.312693,-2.881899,0.360704,2.986643]],[[-5.934570,-3.343202,-2.582695,6.577892,3.228672,-8.912754,5.433495,-8.935321,4.559269,9.144917,3.351459,5.183622,7.762494],[2.135767,-1.884199,-5.126932,5.575775,-4.907488,4.568095,3.847026,-5.057685,6.770093,3.260151,-2.571651,0.766206,-7.188461],[-7.615647,0.674038,9.735321,1.517878,-1.243355,-0.592663,-0.940984,4.852016,-7.662267,-9.260897,-9.118107,7.678085,-9.224448]],[[-4.198368,0.601132,-9.112152,-3.347849,9.003745,8.348377,9.577514,-4.418219,8.051298,9.709305,0.710434,0.974035,-7.452655],[2.288933,3.284018,5.071199,6.635932,-2.813402,-7.230127,-5.406585,-5.079952,-3.100216,5.680586,2.876452,5.867581,4.590126],[-2.939272,1.744834,-6.385888,-0.032398,-2.067039,1.583777,-3.429822,0.142158,-1.132563,2.296027,3.843888,6.599091,-6.747113]],[[8.528914,2.552450,-6.699276,8.416889,-7.168871,-0.266193,0.616158,-3.874365,5.375285,-9.307791,0.675714,-6.634432,5.310475],[2.589132,-7.705583,9.417073,7.778069,-3.477636,5.647763,1.177206,9.243161,-8.294833,-1.070942,9.642362,-8.842058,2.306635],[-7.080675,-8.925022,2.001852,-5.045568,1.717932,-0.057459,-1.990845,3.524691,-5.354327,0.216323,-2.225956,2.090050,-5.473392]]], dtype = "float32")#candidate|4763|(11, 3, 13)|const|float32
uop_4764 = relay.acosh(const_4763.astype('float32')) # shape=(11, 3, 13)
output = uop_4764
output2 = uop_4764
func_4784 = relay.Function([], output)
mod['func_4784'] = func_4784
mod = relay.transform.InferType()(mod)
output = func_4784()
func_4785 = relay.Function([], output)
mutated_mod['func_4785'] = func_4785
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4800 = relay.var("var_4800", dtype = "float32", shape = (9, 11, 4))#candidate|4800|(9, 11, 4)|var|float32
const_4801 = relay.const([[[1.312928,0.915450,2.629785,-0.202643],[-1.076062,-6.826022,-4.182228,-6.546094],[1.413447,-9.395867,-2.658627,-9.083959],[-4.875628,2.054941,-3.427683,3.290436],[-2.560671,1.401183,-3.499742,2.035843],[6.211093,2.339592,-1.198350,-7.161358],[-9.434677,-0.809839,-2.374263,5.681914],[6.141368,-7.981015,7.930057,5.286524],[-6.005168,6.835441,4.941460,5.907546],[-4.888918,-0.455728,-2.004496,-9.073620],[5.571742,-0.762870,-1.988778,-4.030825]],[[-8.942894,5.700941,-2.640794,4.250758],[3.468977,-2.988264,9.660042,-1.738904],[-2.227282,6.064700,9.144142,7.054579],[-7.197074,-4.160351,8.934414,-8.714381],[0.231372,0.021156,-2.903910,-5.490850],[0.875252,-8.595528,-6.149011,-3.072738],[3.534288,-0.653247,-6.999420,-9.469745],[0.329176,2.347886,9.598614,-9.480872],[1.854614,7.111761,6.338153,9.166211],[-6.351423,7.977208,-5.475654,2.867251],[4.900893,-1.241136,3.363567,-7.402786]],[[-8.725368,-3.090360,1.570284,-9.144282],[-9.169796,1.109665,-4.236696,9.054671],[-6.486646,4.080269,-8.630884,3.581074],[-9.878892,2.010109,-4.179284,-2.190205],[4.270962,-1.359183,-9.933635,1.729575],[-2.676906,-8.779426,-1.033410,5.706916],[-3.218185,9.547131,4.852818,0.510697],[2.748837,-4.389513,-2.149856,-2.884237],[2.384900,3.538326,1.643819,-9.879770],[9.761318,-0.211016,-3.404544,-4.904191],[8.781713,-9.202126,-8.110460,-2.757776]],[[-1.114870,3.426679,-8.859632,2.621199],[7.338042,2.593679,1.036310,-4.699996],[-1.832469,-5.643843,7.119436,5.761539],[4.828823,1.480837,8.470398,5.239434],[-0.082184,7.941424,-1.055190,-3.768877],[6.287387,-4.765919,-8.376612,3.619576],[-3.988161,8.459663,-6.906894,-6.544858],[-4.946203,-4.484699,1.950350,-1.909977],[-8.285823,-1.282656,-6.073264,-3.377227],[-8.509972,-2.446490,-6.455004,8.969087],[-5.063300,-6.001460,-8.422377,-1.311213]],[[-9.353247,-0.526315,-9.546053,-6.418059],[-8.931339,1.694507,3.023787,-6.244248],[-7.292275,-8.893481,-1.672985,7.827686],[5.357390,-1.871167,-4.543268,-4.848411],[0.421672,8.481883,4.342611,-1.717565],[-7.536272,-0.791708,-5.893730,-2.361996],[-6.689367,2.971214,-5.365583,5.942359],[-3.792192,9.805535,-1.869040,5.654977],[1.295323,2.785921,-5.792120,-9.813140],[1.747114,1.082421,-7.656711,-2.468616],[-3.437474,9.783461,6.021840,-6.350136]],[[-6.192089,-9.052592,-9.123044,-0.855079],[-0.483486,-0.707906,-5.050208,-6.903349],[-2.743325,3.956137,1.475047,1.838343],[9.121171,-2.824463,0.760328,-2.254775],[2.117177,-3.177061,-8.562049,7.604053],[-6.004519,-9.531727,-7.050747,-4.497851],[-5.887907,4.715501,0.637337,1.865653],[-0.887007,6.478007,3.334270,6.277158],[8.695294,-7.624021,9.777622,-3.145096],[5.460043,-9.728570,6.498961,-3.416751],[-4.634394,9.139039,-6.978033,-2.406240]],[[9.549566,-0.772624,8.483152,5.099889],[1.379224,-5.494227,1.801200,-9.108570],[6.156266,-2.177804,9.608259,-7.772083],[8.300998,-7.897864,4.634773,-9.396373],[-4.560048,2.064946,-8.043119,-1.163693],[-6.836416,-6.048900,-0.118034,-3.140670],[1.915843,-9.919908,-0.881672,-7.535884],[2.569822,5.209904,2.803782,2.437329],[4.209652,5.537076,6.810282,5.214877],[4.748736,1.100315,0.206814,7.357307],[-4.348718,3.379892,8.946461,-2.527686]],[[-9.800432,2.609291,0.995197,-3.483722],[4.326525,9.982194,2.771458,-3.964440],[-2.725272,-9.650983,3.642081,2.243686],[-7.710414,-4.017182,-3.099767,-2.776926],[2.318188,8.060609,-9.691876,3.347320],[1.626805,-9.875141,6.830430,2.369711],[-3.155311,8.847870,-1.551918,5.784918],[-2.550572,-4.379348,9.233920,9.981096],[-6.211780,1.121963,-0.135241,-5.806464],[3.318437,3.947724,1.728097,3.446505],[-7.656385,9.363651,9.173395,3.305104]],[[0.274686,-5.078164,-0.116048,4.344608],[-0.924384,0.369802,6.296653,5.029529],[-5.326243,5.108225,0.538081,7.666011],[-4.131821,-2.001653,-6.034066,5.655218],[5.739030,-6.334389,8.382102,-5.714986],[-3.755718,5.951518,7.471596,0.725800],[2.903091,0.750987,8.491864,-8.127935],[-5.892708,8.497558,1.667622,-9.628035],[-7.982788,-3.466074,-6.016213,-1.220622],[5.201769,-9.618684,-1.222408,-4.583524],[-6.271517,-4.384806,3.604788,9.451575]]], dtype = "float32")#candidate|4801|(9, 11, 4)|const|float32
bop_4802 = relay.divide(var_4800.astype('float32'), relay.reshape(const_4801.astype('float32'), relay.shape_of(var_4800))) # shape=(9, 11, 4)
output = relay.Tuple([bop_4802,])
output2 = relay.Tuple([bop_4802,])
func_4814 = relay.Function([var_4800,], output)
mod['func_4814'] = func_4814
mod = relay.transform.InferType()(mod)
var_4815 = relay.var("var_4815", dtype = "float32", shape = (9, 11, 4))#candidate|4815|(9, 11, 4)|var|float32
output = func_4814(var_4815)
func_4816 = relay.Function([var_4815], output)
mutated_mod['func_4816'] = func_4816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3169_call = mod.get_global_var('func_3169')
func_3170_call = mutated_mod.get_global_var('func_3170')
call_4840 = relay.TupleGetItem(func_3169_call(), 0)
call_4841 = relay.TupleGetItem(func_3170_call(), 0)
output = call_4840
output2 = call_4841
func_4842 = relay.Function([], output)
mod['func_4842'] = func_4842
mod = relay.transform.InferType()(mod)
output = func_4842()
func_4843 = relay.Function([], output)
mutated_mod['func_4843'] = func_4843
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4403_call = mod.get_global_var('func_4403')
func_4404_call = mutated_mod.get_global_var('func_4404')
call_4892 = func_4403_call()
call_4893 = func_4403_call()
output = relay.Tuple([call_4892,])
output2 = relay.Tuple([call_4893,])
func_4896 = relay.Function([], output)
mod['func_4896'] = func_4896
mod = relay.transform.InferType()(mod)
output = func_4896()
func_4897 = relay.Function([], output)
mutated_mod['func_4897'] = func_4897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2155_call = mod.get_global_var('func_2155')
func_2156_call = mutated_mod.get_global_var('func_2156')
call_4910 = relay.TupleGetItem(func_2155_call(), 0)
call_4911 = relay.TupleGetItem(func_2156_call(), 0)
func_364_call = mod.get_global_var('func_364')
func_366_call = mutated_mod.get_global_var('func_366')
call_4912 = func_364_call()
call_4913 = func_364_call()
var_4914 = relay.var("var_4914", dtype = "uint16", shape = (12, 11, 10))#candidate|4914|(12, 11, 10)|var|uint16
bop_4915 = relay.logical_and(call_4912.astype('bool'), var_4914.astype('bool')) # shape=(12, 11, 10)
bop_4918 = relay.logical_and(call_4913.astype('bool'), var_4914.astype('bool')) # shape=(12, 11, 10)
output = relay.Tuple([call_4910,bop_4915,])
output2 = relay.Tuple([call_4911,bop_4918,])
func_4922 = relay.Function([var_4914,], output)
mod['func_4922'] = func_4922
mod = relay.transform.InferType()(mod)
mutated_mod['func_4922'] = func_4922
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4923 = relay.var("var_4923", dtype = "uint16", shape = (12, 11, 10))#candidate|4923|(12, 11, 10)|var|uint16
func_4922_call = mutated_mod.get_global_var('func_4922')
call_4924 = func_4922_call(var_4923)
output = call_4924
func_4925 = relay.Function([var_4923], output)
mutated_mod['func_4925'] = func_4925
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4341_call = mod.get_global_var('func_4341')
func_4342_call = mutated_mod.get_global_var('func_4342')
call_4930 = relay.TupleGetItem(func_4341_call(), 0)
call_4931 = relay.TupleGetItem(func_4342_call(), 0)
func_3598_call = mod.get_global_var('func_3598')
func_3600_call = mutated_mod.get_global_var('func_3600')
call_4945 = func_3598_call()
call_4946 = func_3598_call()
output = relay.Tuple([call_4930,call_4945,])
output2 = relay.Tuple([call_4931,call_4946,])
func_4955 = relay.Function([], output)
mod['func_4955'] = func_4955
mod = relay.transform.InferType()(mod)
output = func_4955()
func_4956 = relay.Function([], output)
mutated_mod['func_4956'] = func_4956
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3598_call = mod.get_global_var('func_3598')
func_3600_call = mutated_mod.get_global_var('func_3600')
call_5035 = func_3598_call()
call_5036 = func_3598_call()
func_1490_call = mod.get_global_var('func_1490')
func_1492_call = mutated_mod.get_global_var('func_1492')
call_5037 = relay.TupleGetItem(func_1490_call(), 0)
call_5038 = relay.TupleGetItem(func_1492_call(), 0)
func_448_call = mod.get_global_var('func_448')
func_449_call = mutated_mod.get_global_var('func_449')
call_5039 = relay.TupleGetItem(func_448_call(), 0)
call_5040 = relay.TupleGetItem(func_449_call(), 0)
output = relay.Tuple([call_5035,call_5037,call_5039,])
output2 = relay.Tuple([call_5036,call_5038,call_5040,])
func_5063 = relay.Function([], output)
mod['func_5063'] = func_5063
mod = relay.transform.InferType()(mod)
mutated_mod['func_5063'] = func_5063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5063_call = mutated_mod.get_global_var('func_5063')
call_5064 = func_5063_call()
output = call_5064
func_5065 = relay.Function([], output)
mutated_mod['func_5065'] = func_5065
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5080 = relay.var("var_5080", dtype = "float64", shape = (3, 3, 4))#candidate|5080|(3, 3, 4)|var|float64
uop_5081 = relay.asin(var_5080.astype('float64')) # shape=(3, 3, 4)
output = uop_5081
output2 = uop_5081
func_5084 = relay.Function([var_5080,], output)
mod['func_5084'] = func_5084
mod = relay.transform.InferType()(mod)
mutated_mod['func_5084'] = func_5084
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5085 = relay.var("var_5085", dtype = "float64", shape = (3, 3, 4))#candidate|5085|(3, 3, 4)|var|float64
func_5084_call = mutated_mod.get_global_var('func_5084')
call_5086 = func_5084_call(var_5085)
output = call_5086
func_5087 = relay.Function([var_5085], output)
mutated_mod['func_5087'] = func_5087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4231_call = mod.get_global_var('func_4231')
func_4233_call = mutated_mod.get_global_var('func_4233')
call_5093 = func_4231_call()
call_5094 = func_4231_call()
output = relay.Tuple([call_5093,])
output2 = relay.Tuple([call_5094,])
func_5098 = relay.Function([], output)
mod['func_5098'] = func_5098
mod = relay.transform.InferType()(mod)
mutated_mod['func_5098'] = func_5098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5098_call = mutated_mod.get_global_var('func_5098')
call_5099 = func_5098_call()
output = call_5099
func_5100 = relay.Function([], output)
mutated_mod['func_5100'] = func_5100
mutated_mod = relay.transform.InferType()(mutated_mod)
func_497_call = mod.get_global_var('func_497')
func_498_call = mutated_mod.get_global_var('func_498')
call_5124 = relay.TupleGetItem(func_497_call(), 0)
call_5125 = relay.TupleGetItem(func_498_call(), 0)
output = call_5124
output2 = call_5125
func_5149 = relay.Function([], output)
mod['func_5149'] = func_5149
mod = relay.transform.InferType()(mod)
output = func_5149()
func_5150 = relay.Function([], output)
mutated_mod['func_5150'] = func_5150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4757_call = mod.get_global_var('func_4757')
func_4759_call = mutated_mod.get_global_var('func_4759')
call_5161 = relay.TupleGetItem(func_4757_call(), 1)
call_5162 = relay.TupleGetItem(func_4759_call(), 1)
uop_5165 = relay.asin(call_5161.astype('float32')) # shape=(1, 11, 10)
uop_5167 = relay.asin(call_5162.astype('float32')) # shape=(1, 11, 10)
func_448_call = mod.get_global_var('func_448')
func_449_call = mutated_mod.get_global_var('func_449')
call_5188 = relay.TupleGetItem(func_448_call(), 1)
call_5189 = relay.TupleGetItem(func_449_call(), 1)
func_4661_call = mod.get_global_var('func_4661')
func_4662_call = mutated_mod.get_global_var('func_4662')
call_5194 = func_4661_call()
call_5195 = func_4661_call()
uop_5206 = relay.sigmoid(call_5194.astype('float32')) # shape=(2, 9, 10)
uop_5208 = relay.sigmoid(call_5195.astype('float32')) # shape=(2, 9, 10)
func_2106_call = mod.get_global_var('func_2106')
func_2110_call = mutated_mod.get_global_var('func_2110')
var_5217 = relay.var("var_5217", dtype = "uint16", shape = (220,))#candidate|5217|(220,)|var|uint16
const_5218 = relay.const([-10,7,-3,-5,-2,3,1,-8,2,5,9,-5,-8,6,-1,-7,7,2,-2,10,-5,-4,8,7,-6,-8,-2,7,-4,-2,-3,-5,-5,-4,-6,-1,-9,7,-6,9,-9,-4,-2,10,5,-10,-3,1,-1,-4,-1,-8,-9,10,-9,7,8,8,-4,7,-2,-10,-1,2,-7,-1,-3,-9,-3,-2,-9,-10,-2,-6,-7,-8,1,4,10,-6,-4,7,5,4,6,10,-4,-10,-1,5,-1,-8,10,6,10,6,10,-5,-9,5,-6,-9,-9,9,9,-9,6,5,-1,-5,-5,-9,4,4,-3,-1,5,-1,2,4,3,-2,-3,4,-9,7,10,3,-9,9,7,3,1,6,-4,-3,-6,-4,3,4,-7,-8,-6,10,7,7,1,-5,2,8,-4,2,7,10,6,-3,-3,-9,-1,2,10,3,-9,-6,2,6,-4,-7,-6,2,-10,-4,-6,-2,2,9,5,-5,-2,5,4,1,2,10,4,-8,5,-7,-5,-9,5,8,10,6,4,-6,-5,-6,-5,-2,8,-5,-4,-5,-3,5,-4,10,6,-6,7,9,-8,-6,-3,4,-10,8,1,-2,-10,4,2,10,10,-10,-9,-9,-6,-2,5,4,-6,9,6,4,10,1,-2,2,8,-10,-1,-6,4,-7,5,-4,4,10,9,-5,2,3,-9,-7,-4,-4,6,1,-9,8,-10,6,-8,-3,2,5,7,9,10,-3,-3,-9,-8,-6,1,-2,8,4,-6,-2,6,-2,5,9,7,2,-10,6,5,6,10,6,7,2,8,2,1,-9,5,-4,1,-2,-10,10,4,1,5,10,9,7,-7,-3,3,7,-1,2,-8,6,7,-5,-3,5,-4,-2,-8,-10,8,-5,7,-2,-4,4,-1,2,-6,10,-1,-1,-7,-8,2,10,-1,-2,7,-1,-10,-5,-5,10,-3,-3,3,-1,-7,-7,-7,10,4,-10,-7,3,6,-8,-6,2,-1,6,-9,6,8,-4,4,6,-7,10,7,-1,3,2,2,-1,-9,6,-5,-3,-10,1,10,-2,4,-2,7,-2,5,-10,-9,9,-9,5,9,-9,4,3,-7,-2,-6,10,8,-4,7,3,4,-4,-8,8,-7,-8,-9,7,-5,7,-3,-5,-10,-5,2,2,1,10,5,9,-5,2,-10,-7,6,-6,-2,10,-9,-8,-5,8,6,-5,4,-10,-3,-10,-1,-9,5,-8,8,1,-6,-8,-1,9,4,6,-10,-6,3,7,7,3,-1,8,-10,5,-8,-9,1,6,-1,-3,1,5,7,7,6,-5,10,6,-4,8,-6,-3,-4,-4,1,6,-7,7,-3,-10,-4,-7,2,-8,6,10,-2,1,-10,-1,-10,-5,9,3,-6,-2,9,9,-3,-8,3,-1,1,-1,6,-3,10,-7,2,1,-4,10,-2,-7,-6,-6,-4,-3,10,7,-7,-4,10,8,-3,2,1,3,1,-8,6,5,2,7,6,-8,6,-2,5,-10,8,-6,-4,-2,-8,1,6,-5,5,-8,8,6,10,-2,-7,-1,-4,3,5,-10,-6,8,8,10,-9,-6,4,3,-9,9,7,2,7,9,3,-7,-10,-2,-10,4,9,-6,-2,-9,4,-1,-7,4,10,-8,-1,-1,9,3,-4,-7,-7,-9,2,1,5,-8,-5,-10,4,-6,-4,9,-10,3,9,8,4,4,5,-3,7,7,-4,7,-7,-6,-1,4,-7,-9,8,-2,-5,10,4,-4,-7,-3,6,-2,4,-3,2,10,6,-8,7,9,-6,5,6,-1,8,5,-5,-8,6,-7,1,-2,9,3,7,9,3,-5,3,2,-1,7,8,6,7,4,3,4,5,-9,9,8,-1,-1,-1,6,-3,-8,8,-7,-1,4,-9,7,8,-6,3,-1,9,9,-8,-1,-9,4,-5,6,-3,2,-1,-4,3,7,6,-10,-9,-4,-7,-8,4,-6,4,-6,4,-9,-5,5,-4,5,8,4,8,4,3,-2,3,-7,-9,4,-3,10,5,-7,6,9,-9,3,1,3,-9,-2,-2,-1,-3,6,-7,3,2,1,4,-3,-10,-10,-4,-6,7,-7,-6,2,3,-7,-6,2,-2,7,-2,-9,-7,-5,2,-5,-9,10,3,7,3,8,-4,-7,-5,2,-5,2,-10,4,-10,2,3,7,5,-4,7,8,-4,10,1,7,-5,-1,-7,8,6,-9,4,-5,-9,9,-2,-1,-6,-6,-5,5,3,4,1,-7,3,-5,1,8,-10,-6,-8,9,-8,-10,-7,2,1,9,-9,8,-4,9,-5,-5,-7,-9,10,6,-2,-2,1,10,1,5,-10,1,8,-1,-10,7,-1,-2,-4,-10,5,9,9,10,-1,-9,-8,8,2,-8,-8,-10,3,4,10,-6,-8,-3,-4,-7,7,-9,10,-10,7,-5,-5,7,-6,-5,-5,-3,8,1,6,9,8,8,-5,8,-10,-6,9,5,4,-4,-3,-1,-3,-2,-2,4,-1,6,5,-6,9,2,-7,7,-10,-10,10,-5,6,5,10,-8,4,-5,-7,7,-4,8,-7,3,-6,10,6,10,-3,-10,4,4,-9,8,1,-6,4,8,-6,9,-6,7,-4,-2,10,2,7,2,4,-3,-7,9,2,-5,8,10,4,-4,4,7,-7,10,2,1,3,-10,5,-4,-5,-7,2,5,-5,-4,4,-5,-10,-6,-6,-10,-4,-1,-8,-10,-3,-5,2,-3,-8,10,-10,-6,9,-5,-10,-5,-5,-7,-3,-7,-2,3,2,-5,-5,-6,-7,7,4,-2,-9,3,3,-9,7,-3,8,-4,-4,-5,-3,5,-3,7,-6,-4,-6,-9,6,-5,3,1,6,4,-6,8,-9,-9,-5,8,5,-6,-10,10,-2,9,5,-7,-7,10,9,3,2,10,8,9,-1,-6,8,7,3,5,5,-8,2,-8,-7,-1,-2,-6,-9,6,10,1,8,-7,-3,8,4,-2,3,1,10,-8,-3,5,-9,-3,2,6,3,10,6,6,3,10,8,7,5,10,-8,-1,-5,6,2,7,5,-1,-7,-5,-5,-8,6,2,-1,-1,-5,-7,-9,-8,-5,6,4,1,6,-4,10,-5,9,10,-10,-2,1,5,-2,-1,-10,7,4,-7,-1,-3,-7,7,-6,8,6,-10,9,9,10,8,-6,-4,-2,-1,4,-4,-4,6,10,5,4,-4,-3,-4,-4,-3,-9,1,7,-4,7,1,3,-1,-1,-8,4,-10,9,-9,8,1,8,1,-5,-10,7,4,-9,2,1,-9,-3,1,-2,-3,4,-10,-8,-10,5,7,-1,1,-6,-4,-2,4,-9,-7,7,1,-8,4,9,-10,3,-8,8,6,2,-5,-10,-10,-7,-8,-9,-6,10,-2,5,7,1,2,-7,-5,6,-3,-10,5,-4,-2,4,9,-9,2,4,1,5,5,2,10,4,4,10,1,-2,6,-2,-9,7,6,1,9,1,-7,-5,-10,-2,-3,4,4,-1,-4,-5,-6,4,-4,-9,10,-8,-2,-4,2,-5,-8], dtype = "uint16")#candidate|5218|(1320,)|const|uint16
call_5216 = relay.TupleGetItem(func_2106_call(relay.reshape(var_5217.astype('uint16'), [2, 11, 10]), relay.reshape(const_5218.astype('uint16'), [1320,]), ), 3)
call_5219 = relay.TupleGetItem(func_2110_call(relay.reshape(var_5217.astype('uint16'), [2, 11, 10]), relay.reshape(const_5218.astype('uint16'), [1320,]), ), 3)
output = relay.Tuple([uop_5165,call_5188,uop_5206,call_5216,var_5217,const_5218,])
output2 = relay.Tuple([uop_5167,call_5189,uop_5208,call_5219,var_5217,const_5218,])
func_5227 = relay.Function([var_5217,], output)
mod['func_5227'] = func_5227
mod = relay.transform.InferType()(mod)
var_5228 = relay.var("var_5228", dtype = "uint16", shape = (220,))#candidate|5228|(220,)|var|uint16
output = func_5227(var_5228)
func_5229 = relay.Function([var_5228], output)
mutated_mod['func_5229'] = func_5229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4457_call = mod.get_global_var('func_4457')
func_4458_call = mutated_mod.get_global_var('func_4458')
call_5272 = relay.TupleGetItem(func_4457_call(), 1)
call_5273 = relay.TupleGetItem(func_4458_call(), 1)
func_4132_call = mod.get_global_var('func_4132')
func_4133_call = mutated_mod.get_global_var('func_4133')
call_5282 = func_4132_call()
call_5283 = func_4132_call()
uop_5284 = relay.rsqrt(call_5282.astype('float64')) # shape=(2, 1, 10)
uop_5286 = relay.rsqrt(call_5283.astype('float64')) # shape=(2, 1, 10)
output = relay.Tuple([call_5272,uop_5284,])
output2 = relay.Tuple([call_5273,uop_5286,])
func_5290 = relay.Function([], output)
mod['func_5290'] = func_5290
mod = relay.transform.InferType()(mod)
mutated_mod['func_5290'] = func_5290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5290_call = mutated_mod.get_global_var('func_5290')
call_5291 = func_5290_call()
output = call_5291
func_5292 = relay.Function([], output)
mutated_mod['func_5292'] = func_5292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_497_call = mod.get_global_var('func_497')
func_498_call = mutated_mod.get_global_var('func_498')
call_5369 = relay.TupleGetItem(func_497_call(), 0)
call_5370 = relay.TupleGetItem(func_498_call(), 0)
output = call_5369
output2 = call_5370
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
var_5425 = relay.var("var_5425", dtype = "float64", shape = (5, 13, 2))#candidate|5425|(5, 13, 2)|var|float64
uop_5426 = relay.atan(var_5425.astype('float64')) # shape=(5, 13, 2)
func_4661_call = mod.get_global_var('func_4661')
func_4662_call = mutated_mod.get_global_var('func_4662')
call_5430 = func_4661_call()
call_5431 = func_4661_call()
output = relay.Tuple([uop_5426,call_5430,])
output2 = relay.Tuple([uop_5426,call_5431,])
func_5460 = relay.Function([var_5425,], output)
mod['func_5460'] = func_5460
mod = relay.transform.InferType()(mod)
var_5461 = relay.var("var_5461", dtype = "float64", shape = (5, 13, 2))#candidate|5461|(5, 13, 2)|var|float64
output = func_5460(var_5461)
func_5462 = relay.Function([var_5461], output)
mutated_mod['func_5462'] = func_5462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5376_call = mod.get_global_var('func_5376')
func_5378_call = mutated_mod.get_global_var('func_5378')
call_5537 = func_5376_call()
call_5538 = func_5376_call()
func_5098_call = mod.get_global_var('func_5098')
func_5100_call = mutated_mod.get_global_var('func_5100')
call_5546 = relay.TupleGetItem(func_5098_call(), 0)
call_5547 = relay.TupleGetItem(func_5100_call(), 0)
func_1429_call = mod.get_global_var('func_1429')
func_1430_call = mutated_mod.get_global_var('func_1430')
call_5549 = func_1429_call()
call_5550 = func_1429_call()
func_2266_call = mod.get_global_var('func_2266')
func_2269_call = mutated_mod.get_global_var('func_2269')
const_5552 = relay.const([-1,3,6,-8,7,5,-4,4,-9,-10,-4,-4,2,7,-4,-8,9,6,7,-8,-8,2,-3,1,-1,-4,-3,-2,-6,1,-1,-7,-2,6,7,-6,6,8,-4,-1,9,-10,6,9,2,4,-1,-4,1,6,3,-4,10,10,10,1,-7,-6,-2,6,7,7,-8,2,-2,-1,10,6,9,4,-7,3,-5,-6,-3,8,10,-9,8,-2,-2,7,-8,2,9,9,2,-8,8,-1,-6,-3,6,-9,-5,-5,1,9,-5,9,6,1,-7,-4,-5,-7,5,9,10,-8,-8,2,-6,-1,1,-6,7,6,6,-8,-6,-4,-5,-4,1,-1,-6,-8,-3,3,8,-10,7,-8,7,-8,3,4,4,-2,-10,6,6,-6,5,-1,-1,8,9,4,2,-7,-3,2,8,2,6,4,4,-9,1,9,-2,-1,3,-7,7,-1,-6,8,6,2,10,2,-7,-10,-2,10,8,-5,9,7,7,-6,10,6,4,7,-5,-5,-1,-1,-3,-9,4,-3,7,9,-9,-8,7,-6,4,-4,-2,1,3,8,-3,-9,10,-2,-10,-2,5,8,6,4,7,10,4,-5,-3,5,2,5,-3,-1,-9,4,5,-6,7,-10,8,4,-1,-9,5,-2,-7,9,5,5,-4,-8,2,-9,-5,-1,-1,5,7,-6,-9,9,5,-5,9,4,10,2,5,-9,2,-1,9,5,-9,8,9,-3,-7,-7,-10,-10,1,2,-3,6,3,8,-5,-7,6,-2,3,3,6,6,9,8,-10,-5,3,10,-1,5,-3,-10,-8,-8,-10,2,-9,5,6,7,6,-9,-3,3,7,-10,2,1,-2,2,-8,-9,-5,-4,-8,7,2,10,-4,1,-3,-2,-1,-7,-10,7,7,4,10,3,10,9,7,-1,-4,-10,5,4,-5,-1,3,-4,3,10,-7,-1,-4,-10,2,2,4,-5,-6,-7,3,7,-7,4,-8,-5,-9,3,-9,-6,2,8,-10,7,5,6,-1,2,3,-9,-2,7,1,5,-2,-10,9,-2,-5,4,2,-8,4,-2,7,1,6,-1,9,-6,8,-5,5,5,-4,-2,10,9,1,4,-3,-7,2,-7,-3,2,-8,-6,2,-7,-2,-5,8,-8,-7,6,7,10,-1,-10,9,-4,9,-2,-3,1,7,-8,2,-3,-8,9,-2,5,-6,-8,1,4,5,-2,4,-4,9,-7,9,10,-8,-3,9,-6,6,-2,7,6,-1,-10,2,-7,7,-4,3,-4,-4,-3,-6,2,4,-7,-9,3,-1,-6,-7,4,6,-2,1,-9,-2,1,-5,10,-6,-10,-1,-6,6,-5,-4,10,-8,-8,8,-5,-4,-10,9,6,-8,10,-9,-4,-8,-1,10,2,-2,7,2,2,-10,2,-2,-5,-5,4,3,3,6,4,3,-4,-10,5,-4,-5,9,4,-6,-4,5,-8,-5,-10,5,7,-1,3,1,-1,-6,9,-6,9,-3,-6,2,-9,-5,7,10,-7,4,-2,1,10,-2,5,4,-1,-8,7,10,-6,-2,6,9,-7,-7,-10,4,8,-8,5,10,1,2,-7,-6,1,7,4,-5,9,-9,10,8,9,-4,2,-10,-1,2,9,2,8,9,7,10,-4,4,10,6,2,4,4,-6,8,-5,-8,9,8,7,-10,1,5,9,-9,-7,-5,-4,8,-3,10,5,7,-5,10,8,8,-3,5,2,-7,7,-1,10,-3,-6,-3,2,-5,-2,-8,4,-10,-8,-8,-10,-9,-6,8,-2,9,3,-10,-1,-1,-1,-5,-2,3,9,2,8,-6,6,8,-4,-7,-8,-9,4,-4,-8,4,-4,-4,8,-4,-9,-1,-6,-2,-6,5,-8,7,-6,-10,9,-4,1,-6,4,-7,2,-10,7,-7,3,-8,-8,-6,5,-9,-10,-7,-1,-9,-5,-7,-4,-7,9,3,8,4,8,10,-3,-8,-2,-3,-2,-5,1,-5,-9,8,-6,1,-4,-10,2,-6,9,-10,-2,3,7,10,1,5,-8,9,5,8,2,2,9,1,-3,-10,-5,-7,-10,2,-2,1,-1,-6,8,-4,3,6,-5,2,9,-2,-3,-7,-8,4,8,-2,4,3,-1,4,-4,-7,-9,-6,-1,3,9,-8,-8,9,-8,5,8,-3,9,-6,-10,-4,4,-7,8,10,9,6,-2,5,7,-1,-10,-5,-4,3,-4,2,7,-2,9,-4,-1,8,-7,-5,-5,-9,-3,-5,5,-10,3,6,3,-4,-9,-1,-1,6,-3,4,7,4,-8,-6,7,2,10,-1,-6,-5,5,7,-6,8,6,-7,5,-3,-10,-6,7,-8,-7,-9,-6,-8,-10,-1,-10,4,-10,8,-4,-8,2,-3,3,-5,2,3,-6,-1,8,3,-2,5,-9,5,6,8,-9,-6,-2,-5,4,-2,-1,-9,6,8,-8,-10,-5,-10,10,10,9,-4,-8,-5,6,-5,4,-7,-5,-10,9,-9,7,-7,7,8,3,9,8,-4,-3,3,-2,-8,7,-9,10,-1,9,-3,3,-4,-1,10,7,6,-4,7,-9,-2,-5,-1,8,1,7,-4,5,-1,-9,8,6,5,-2,5,-7,8,-5,-6,-10,-10,1,1,10,-4,2,4,-7,7,9,-1,-8,-8,-7,-8,1,5,-10,10,8,-10,10,-10,2,6,-1,10,5,6,4,10,2,9,-2,1,-5,-4,-6,1,4,-3,-6,6,-3,-5,6,4,1,-9,2,-4,-2,3,-3,-6,-4,1,2,-3,-10,3,4,-4,-1,-7,-5,-4,-9,5,-1,-6,1,-7,5,-9,-8,2,10,-4,-1,7,-2,-4,-8,-1,-9,-6,-6,-3,-4,-7,5,-6,-7,9,1,-5,7,-6,-8,5,-5,8,-5,2,3,4,9,4,-10,6,-9,8,2,-10,-10,8,6,-7,-6,2,8,-9,6,3,-6,-1,9,10,1,2,5,-9,5,-1,4,-2,1,-1,5,-7,2,8,5,-5,-10,-10,-6,-5,4,1,3,-2,5,1,7,4,6,-1,2,9,-2,8,-9,-6,-2,1,-2,-8,-6,8,-9,-3,4,5,-9,-7,-7,-6,9,7,8,-5,-3,-7,3,2,-6,6,8,-6,-10,-5,-8,-1,-2,-8,-10,-3,5,-2,5,-2,-9,-3,-4,4,-3,-10,2,8,4,6,-9,7,-1,4,-4,-1,9,-10,4,-8,4,8,1,-10,3,9,7,8,4,5,10,-1,-9,-1,-8,2,7,8,7,5,7,2,9,-3,-1,10,-4,2,5,-10,2,-5,-9,9,2,-8,5,3,1,8,6,-5,1,6,1,-9,8,-2,-8,5,-2,-8,-2,-2,9,-4,7,7,-7,6,-1,-8,10,5,10,7,-2,10,8,-4,-1,-3,-8,-8,3,2,2,2,10,9,9,10,3,-5,2,-7,10,3,8,4,7,7,5,-3,-9,3,-10,-1,-4,1,8,9,8,7,-5,-1,-6,-4,-10,-4,-9,8,1,-10,6,1,1,-1,1,-7,8,9], dtype = "uint16")#candidate|5552|(1320,)|const|uint16
call_5551 = relay.TupleGetItem(func_2266_call(relay.reshape(const_5552.astype('uint16'), [1320,])), 0)
call_5553 = relay.TupleGetItem(func_2269_call(relay.reshape(const_5552.astype('uint16'), [1320,])), 0)
uop_5554 = relay.erf(call_5551.astype('float32')) # shape=(2, 1, 10)
uop_5556 = relay.erf(call_5553.astype('float32')) # shape=(2, 1, 10)
output = relay.Tuple([call_5537,call_5546,call_5549,const_5552,uop_5554,])
output2 = relay.Tuple([call_5538,call_5547,call_5550,const_5552,uop_5556,])
func_5562 = relay.Function([], output)
mod['func_5562'] = func_5562
mod = relay.transform.InferType()(mod)
mutated_mod['func_5562'] = func_5562
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5562_call = mutated_mod.get_global_var('func_5562')
call_5563 = func_5562_call()
output = call_5563
func_5564 = relay.Function([], output)
mutated_mod['func_5564'] = func_5564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_661_call = mod.get_global_var('func_661')
func_663_call = mutated_mod.get_global_var('func_663')
call_5573 = func_661_call()
call_5574 = func_661_call()
const_5582 = relay.const([[[3.535448,0.426159,8.614045,-2.965134,2.275364,0.765146,-0.056439,-0.513614,6.616687,2.609615],[3.700841,0.542883,2.851319,-8.226778,7.498858,2.057950,-1.335761,-9.930471,9.736160,-1.060595],[-5.351087,-0.540983,7.214033,-3.942332,-4.869454,-0.056592,-5.211514,-2.173563,-4.949244,-6.143987],[-8.543351,7.647957,-7.477162,-9.800836,-2.906143,6.326639,6.259958,9.103519,-8.367353,3.108560],[8.391004,-5.373188,4.843488,0.720469,-2.222345,-0.055499,-5.403479,2.248990,3.447413,-2.371658],[-0.137141,8.464526,9.912724,9.709780,-8.369371,-8.309432,-8.563054,-7.271131,8.539468,-5.095475],[3.670910,0.743338,-4.212382,-9.547916,-9.287334,3.141159,-0.572998,-7.481207,7.942480,-5.980791],[-8.207032,9.435659,2.931114,5.040521,7.459441,-5.635353,-8.808453,-8.934023,3.095239,-2.502511],[-6.215340,-8.352795,-4.666785,-3.221317,-6.767746,-8.369444,-0.001128,-5.495287,9.126662,-2.577798],[9.549164,1.521484,-1.632943,-0.241393,-2.995186,-5.495075,-7.152808,-5.760511,5.489722,-8.092449],[8.660255,1.696804,-1.572038,0.359694,4.997068,-0.559484,0.481917,-7.271833,-4.854996,6.630760]],[[0.307216,9.284718,-2.422311,0.579743,-1.319190,-6.266728,-4.817838,4.411302,3.891439,-8.180601],[2.476350,7.191092,-2.394683,-2.548394,-9.323115,0.431923,3.497702,4.555935,-6.506851,-3.519686],[-9.126409,-2.701723,-4.863503,3.510655,5.579544,-5.519306,-2.380047,7.591556,2.263211,1.885343],[6.319767,0.383617,2.633296,-9.710518,3.624504,3.895374,5.269978,-8.078094,1.212559,9.938952],[6.185267,3.458643,7.175786,-3.811839,4.692261,-7.994621,6.353266,8.364004,-3.286864,-6.444096],[-6.411043,7.386585,-7.113375,2.272012,8.966713,-6.523923,-1.206167,5.754260,-9.733787,-2.251019],[2.813746,-4.428719,2.736378,-1.641277,5.115852,9.497553,-2.062639,-6.473420,6.759484,-9.034998],[-7.102214,1.329344,6.598731,9.321567,9.258552,9.948327,-1.634284,4.159118,5.061603,-6.024822],[-1.359849,7.071917,-5.429873,1.948644,3.921938,9.743237,-1.551331,5.105457,2.355555,5.230563],[-0.338182,0.519572,-7.985291,-4.879659,-9.864168,4.280448,7.536078,4.721412,-5.066315,5.126832],[0.370365,5.798094,6.100376,9.122979,8.058854,0.224713,6.327307,4.308292,4.166686,5.665753]],[[-6.263548,5.477924,2.170927,5.657613,1.843422,-5.057094,9.930224,1.790354,-9.059623,6.361549],[7.685152,6.962045,-5.946056,1.090244,9.609608,2.310049,4.152788,8.748587,-5.915903,-6.699408],[3.380427,-3.652946,-1.573401,6.706390,-3.098950,2.158352,-3.497649,-9.010208,5.406839,-4.821541],[-0.337087,-7.583925,-8.466064,5.447554,-3.025769,2.159680,-0.360592,4.905162,7.079133,3.725939],[7.226272,5.504914,7.349456,-7.173608,8.551777,6.739291,8.566697,2.050634,3.808468,-5.131371],[-0.919370,4.450931,6.579920,-5.079903,-0.958614,-0.934447,-3.737805,5.522282,3.192018,-4.655500],[-2.715616,-5.903630,1.396113,-0.432541,-2.114903,-9.158099,-8.252877,8.343450,-1.960006,-2.145203],[6.459777,5.565909,-8.624524,-4.526041,-8.031657,1.316228,-7.064403,-6.283516,8.940905,8.331708],[4.572392,3.161895,4.978680,3.805493,-4.103024,-1.624719,-4.371702,3.442540,-1.179604,-3.195675],[-9.821566,-6.510974,-2.414892,-0.432975,6.678990,2.564841,6.624756,-3.167910,-1.480141,9.429709],[4.097124,-4.294957,1.552905,-0.041717,0.424323,-1.098235,-2.029039,3.007944,-2.196810,0.267879]],[[8.510333,-9.095944,5.231666,5.665495,9.576371,-5.372110,0.144135,-4.402205,-3.736477,-8.440345],[-1.541687,2.555343,2.595867,6.938988,-6.410639,4.660016,0.187537,-5.816101,-5.764610,-0.704092],[-1.275499,-0.630149,-8.029877,-9.699794,-1.507783,-7.596117,-2.687234,5.336646,-5.335786,4.298088],[1.949624,-6.886015,-2.689778,9.462195,6.361340,-6.934961,-6.738826,4.903516,-3.672163,4.440842],[-0.007962,0.511626,2.569463,9.293977,5.922946,-3.700469,5.103845,4.330407,-7.848701,8.733982],[4.034527,7.540150,-5.516139,-1.353326,1.009864,1.421088,8.349865,-4.036242,-3.297550,4.582516],[-0.503216,-5.332156,-7.336930,8.419098,1.305773,-9.275607,1.327263,-9.735081,-5.912907,-7.891782],[9.590637,-6.720714,-6.638439,4.864455,-4.873241,-0.723150,2.542283,-7.161498,-8.431518,-5.938105],[-4.841205,-6.855834,-7.605538,-9.047202,5.050416,-0.905129,-0.120322,-1.465425,1.386522,1.406029],[-8.855228,-0.473214,6.035931,1.634072,6.627036,5.292231,0.026914,1.670746,-2.796759,-3.775199],[-8.239213,-1.645814,8.660634,7.542411,0.796579,-5.081983,-9.702430,1.391391,-6.490486,3.431369]],[[-7.192814,2.376964,2.427449,7.638665,-4.396190,0.205588,1.222378,-0.073355,-6.944589,3.166047],[-4.142080,4.007034,4.631066,-1.264350,-3.476240,1.375137,-5.184819,-7.946624,8.596589,-7.230720],[9.945697,-2.110684,0.942310,-5.358421,-0.450158,9.169645,3.136083,3.522019,3.521701,-7.007572],[1.053956,-2.054788,5.587035,4.419520,9.139624,-0.621613,-0.060198,5.859158,5.952942,6.419639],[8.561833,6.429510,-1.160636,1.454253,-9.627463,2.470338,8.857966,-5.426448,-2.305894,3.799958],[4.732111,-2.066832,-7.068613,3.647230,0.400318,2.399367,-8.692841,-2.786159,7.320661,-8.037413],[5.461483,-8.838526,-6.077502,4.740587,-9.406447,-7.746505,6.319502,4.128741,-2.612531,6.732668],[-2.947823,-9.490369,6.287929,9.779580,8.160899,7.604624,5.710510,1.643649,-1.824587,-5.368367],[-7.196359,-8.747499,9.601394,7.013796,-0.355862,-9.966408,-2.932260,3.852552,0.773423,-8.799792],[7.641993,7.089985,7.750210,-4.566640,-0.352167,3.078757,1.807036,-1.338147,0.441912,-2.919926],[-8.224678,-9.330439,2.658252,3.947385,-6.603586,0.896947,0.883195,-7.959006,-3.478058,-7.339731]],[[7.673780,0.283019,8.095503,-9.695193,2.862033,-2.243346,6.381712,-8.911512,0.768655,0.216328],[-4.095352,1.644253,1.715405,-7.420207,-1.049700,-1.168151,-0.694676,-8.187470,2.460671,6.921837],[2.067676,9.002046,-8.854437,5.816859,2.691105,-9.052009,-3.697929,5.234912,5.451795,4.857898],[-3.147572,-7.468165,2.519283,-2.265908,2.818492,5.337349,4.768550,1.693615,0.623513,5.757700],[5.024500,-6.178677,7.438479,9.093767,3.890148,-4.357151,9.474658,5.840869,4.955108,9.404211],[0.182366,2.948527,2.401380,-6.092765,-6.938089,6.022906,3.020581,1.460466,5.413649,-2.156681],[1.033617,-7.340245,0.690126,5.004013,5.273267,4.129334,5.027905,-7.419109,3.695238,7.109769],[-2.277104,9.105353,-4.083952,9.593878,6.254531,1.446236,-3.713202,6.517887,2.410381,0.697027],[-4.290134,9.651514,1.677526,-8.625519,-3.816850,-5.553449,4.541942,2.148036,-4.050859,5.091061],[-7.280508,-0.693317,7.390941,-6.963024,-9.077668,3.140277,-1.059036,7.414337,-5.270980,-3.137066],[7.814873,-6.685813,-3.402869,6.001860,-6.661415,-3.465011,3.951003,9.583610,8.104712,7.878649]],[[0.195702,-4.510890,2.871205,-6.026622,1.611109,-5.465618,8.308255,2.245528,-1.240385,6.273594],[-7.472164,6.988509,-2.484527,-1.969817,-2.203329,-5.038600,-0.033958,4.300276,-2.810089,-6.784822],[-0.787456,-3.903129,3.909461,2.232338,-8.528100,-1.316835,9.170534,-0.206488,-2.691671,3.485222],[-4.763313,9.542205,-3.433538,-2.051987,-3.934343,-4.608469,-6.746300,-3.604360,3.831443,9.744655],[-9.504484,-0.673494,-7.933784,-3.874397,9.399747,9.497849,7.103350,-9.155270,-2.321759,-0.652389],[2.725174,2.959665,5.634580,2.075811,-7.636171,5.772539,-8.169184,-9.591371,-8.793345,-2.422610],[-6.852745,-2.046415,-3.955814,7.448495,1.920008,0.776017,-5.299587,-7.822834,-3.764046,-4.519207],[6.696653,-1.809856,6.385022,-4.180470,7.694330,2.578547,-4.836976,9.089590,1.237654,6.308656],[-9.651685,4.080541,-8.411160,-4.236898,-0.078194,8.137926,-4.307175,1.029816,-0.688100,-3.536099],[-9.914201,6.896889,0.872926,6.537649,8.439498,7.395146,7.858267,-7.626661,3.028489,4.799845],[-7.992630,1.788071,-0.944270,-9.935843,-2.791069,-4.520804,4.491707,9.743992,-0.475957,7.084724]],[[-6.349778,5.052283,8.339732,2.927772,-4.392442,-6.969214,3.465963,-9.690241,0.603132,-6.565638],[7.514660,-7.611919,-0.745624,2.952445,9.978305,-8.487762,5.995804,9.576026,1.737398,9.004022],[1.566311,-4.442682,7.239095,-1.213118,-0.581322,-5.045503,8.846676,-8.119414,0.395746,-8.133769],[-5.343768,-2.491132,-2.494549,-8.066826,-0.041256,-7.134372,-3.533025,-5.566104,5.474946,-4.191948],[2.241125,2.400089,4.990848,-1.347422,2.228489,1.660844,3.771256,9.029661,-6.263696,3.766456],[-2.640273,-6.540073,0.973742,-3.220253,-3.753550,-1.074753,-9.843511,-8.505501,5.224331,-4.386609],[-6.765245,-1.635048,9.271537,9.637597,3.544985,-3.542433,-6.042763,-5.782131,5.017344,-8.320291],[8.651936,8.583883,-4.361985,-5.882893,-7.238466,-1.370492,-1.129016,-4.778776,8.038808,9.901661],[-2.796397,-8.431578,5.014593,-2.697651,4.090060,-0.584939,7.180857,-5.586613,5.230425,9.066943],[0.449669,-3.664729,-5.726183,0.944877,9.144737,0.235916,-1.969703,-0.190283,-9.100984,-2.642755],[-9.520700,3.930736,-2.392415,8.915580,-6.320415,7.993712,5.663297,4.346682,-7.759298,1.086496]],[[-7.076096,-5.363367,-5.966852,-0.661406,7.076866,-8.168684,7.606276,-9.732366,-9.556891,4.155101],[-9.970104,-0.510533,8.076888,-9.225453,8.372600,3.041616,-1.313114,-3.820814,-3.259213,5.304705],[-3.967752,7.451083,2.551905,4.037092,-5.819036,-5.597442,-4.062275,-9.470197,9.635313,6.516529],[-2.794126,-7.689977,-3.862404,2.370498,9.552537,1.437122,-0.614988,4.542221,-6.529481,3.563854],[7.218904,0.891956,7.771287,7.308859,-5.327853,5.809528,5.254865,6.108907,-5.271858,0.565089],[-3.204217,3.147833,6.680666,-0.905402,-7.485552,-8.623171,-7.191512,0.415417,3.643206,-3.365642],[5.257227,-0.368136,9.911623,5.438397,-0.403309,5.077463,3.272516,-7.583807,8.754707,-8.382370],[-8.283235,4.669736,-8.982186,-1.846072,-5.346810,-3.967170,-7.341503,-4.698230,-8.950888,-9.886277],[-4.934496,5.308101,-1.520364,8.303718,9.089288,8.222394,-8.256832,-3.428171,9.874544,3.506935],[5.890780,-1.398438,-5.575743,3.081974,-7.488065,-3.860100,6.499924,-4.049729,1.005953,3.476909],[5.600879,-6.487634,3.464967,-1.979896,-7.565247,-6.475494,8.510661,9.010231,-6.565169,2.333681]],[[-5.682223,5.016698,2.418387,-5.014435,7.766114,0.877382,-5.874609,7.137191,-1.243423,2.792789],[4.912000,-2.634457,-3.482282,-9.105381,-7.444987,8.092260,0.472099,-0.172724,-6.492037,5.985481],[-8.571592,-2.999706,3.202178,8.306457,9.151042,-6.118819,-4.666415,-0.884774,-2.235278,4.261267],[-9.563416,-1.926590,-1.673934,-8.034860,0.555428,-7.579153,8.886565,-3.582643,-3.301424,-4.076263],[-7.101129,-0.887243,-8.371973,8.774462,-3.509228,1.582388,2.277847,-7.958879,2.570167,-3.859458],[8.682532,-4.365047,5.742452,0.978999,-9.512475,-7.350998,-0.055740,-2.866330,7.074986,0.113975],[-4.957150,-8.921996,-2.987667,1.603037,0.425783,-9.371577,8.350575,4.738879,-2.972920,-7.410297],[9.893173,0.877073,-0.827422,-0.216843,-7.012021,2.712378,-7.450102,-8.047593,-3.114967,-5.388941],[-2.064922,-1.064431,-1.225112,-9.373258,-0.310782,7.265775,7.883157,0.062604,-6.199532,8.770327],[-0.926008,-8.068838,-5.771813,1.742164,-9.167905,1.964201,6.416586,-4.579852,8.018384,-5.743614],[-5.119589,1.073015,-1.377435,7.853172,-7.577691,2.703034,1.193726,-4.493716,6.231976,-8.805193]],[[9.377786,-7.735414,-0.039937,-9.207551,5.028736,9.719779,2.399478,-0.486190,-3.713436,-2.635800],[-1.777920,7.767686,6.357074,-0.847160,9.810908,0.679717,-9.612576,8.219923,-2.769654,-0.070523],[-9.969247,4.286585,2.124524,-0.322023,4.083229,-6.388552,-4.259211,7.719022,3.979926,-4.266770],[1.303851,-7.926901,4.976385,-8.532950,3.968421,-3.648156,-1.526424,1.108477,2.300319,3.952573],[9.743802,-9.859515,2.169999,7.984565,9.229934,-5.947118,4.797674,-9.472773,-9.586744,8.076290],[-0.973416,-4.503877,2.884700,-1.204441,7.986951,-9.989706,9.523139,-0.273782,-4.841887,-0.816531],[-7.457105,-9.840813,5.992552,-4.082925,0.255929,8.920718,1.475025,4.366686,-3.661738,5.818798],[2.672043,-0.042260,1.735341,-2.434165,-7.667721,2.407049,0.145167,4.030520,7.784350,-9.379997],[3.770913,-2.411471,7.326118,0.651436,7.222025,9.015507,-0.755937,6.699737,8.002532,-3.323216],[-8.909873,-3.844340,5.458402,-8.632644,6.936846,-3.011945,8.962452,-6.684210,-6.663716,-4.298401],[-2.680751,-5.128120,7.303001,-7.401539,0.508648,-5.969248,3.668467,2.138028,-2.914941,1.961576]],[[9.628415,-0.423534,-3.866289,1.430818,0.948864,-6.678842,-8.010260,-1.241958,-1.321251,-9.001489],[9.602749,-6.539181,4.895441,-0.727590,8.161294,1.433396,5.935417,6.329319,-1.738403,-9.832407],[-4.887747,-8.471335,7.588459,-6.652131,6.728809,-5.207558,-3.289825,4.480541,-6.257131,3.966442],[7.991029,-5.763618,6.856193,-9.452036,6.841558,6.531231,4.309548,-4.565758,-5.078242,5.717663],[9.820301,3.280051,-7.643753,6.693201,-5.591529,-1.241031,0.123730,-2.155582,3.619127,3.235466],[0.038129,-4.738228,-1.587632,6.058783,-1.416377,-4.789512,-7.852401,3.469784,7.717498,-3.571254],[9.914852,3.949533,5.908702,5.869517,7.137251,4.355806,0.286979,2.845900,-4.112393,3.930293],[1.359779,-9.623800,4.017789,-0.271126,-6.886937,-5.363426,-5.185813,6.612023,9.238451,-2.049540],[2.839515,2.287039,5.303873,-9.136695,0.197414,-1.036031,9.502094,6.705867,-2.780525,3.294617],[-4.891674,3.781258,-8.290112,-7.308474,0.581581,-8.980972,7.390855,-9.522097,-5.612357,-5.634904],[-7.425066,9.025864,-0.632953,-4.097705,-8.992896,1.118455,6.402647,3.633532,8.512312,7.857009]]], dtype = "float64")#candidate|5582|(12, 11, 10)|const|float64
bop_5583 = relay.greater_equal(call_5573.astype('bool'), const_5582.astype('bool')) # shape=(12, 11, 10)
bop_5586 = relay.greater_equal(call_5574.astype('bool'), const_5582.astype('bool')) # shape=(12, 11, 10)
output = bop_5583
output2 = bop_5586
func_5587 = relay.Function([], output)
mod['func_5587'] = func_5587
mod = relay.transform.InferType()(mod)
mutated_mod['func_5587'] = func_5587
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5587_call = mutated_mod.get_global_var('func_5587')
call_5588 = func_5587_call()
output = call_5588
func_5589 = relay.Function([], output)
mutated_mod['func_5589'] = func_5589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3059_call = mod.get_global_var('func_3059')
func_3061_call = mutated_mod.get_global_var('func_3061')
call_5615 = relay.TupleGetItem(func_3059_call(), 0)
call_5616 = relay.TupleGetItem(func_3061_call(), 0)
const_5618 = relay.const([[[-6.510642,-3.612373],[-7.277081,9.988096],[-8.071651,-0.656949],[9.272882,8.065777],[-1.930935,5.916856],[0.735516,6.715028],[7.421801,3.699282]],[[4.582474,0.587507],[7.245146,-2.190788],[0.746282,9.772530],[3.935565,4.860250],[-6.782220,6.382056],[-6.428607,8.441921],[6.621793,4.932800]],[[-6.767594,-9.680292],[4.001450,7.139755],[4.886126,-8.982798],[6.699109,-4.885148],[-9.785807,-4.085203],[7.182361,2.133618],[-9.667044,5.742108]],[[9.215994,-9.812923],[-9.900108,1.012662],[8.566652,-3.260652],[-3.186325,3.300758],[-9.888513,-5.477506],[-0.111328,9.171365],[-8.704973,0.340032]],[[1.944967,4.177775],[7.447758,1.769466],[-7.282590,-2.651452],[1.101455,-1.447635],[6.985449,-5.048482],[-2.091009,-2.542752],[7.379918,-4.195951]],[[-3.027853,-1.909981],[-5.902879,-7.004727],[5.828400,3.385207],[8.803477,6.741362],[6.047986,-5.744104],[-4.117418,-3.056153],[-1.907404,8.433933]],[[3.954947,0.067642],[6.049101,4.224332],[5.257531,5.254214],[0.523469,-6.856932],[-6.827560,-7.134590],[-7.476933,5.819621],[5.979510,9.405689]],[[-6.069153,2.247408],[-6.354339,-3.522509],[-8.111537,0.123841],[0.888591,-6.446944],[-4.327150,5.220266],[2.690397,-9.897351],[4.267752,-9.235082]],[[1.159645,-6.345752],[-6.365736,2.322990],[-4.730433,-4.421578],[-5.990072,7.078788],[-5.679257,-6.724156],[-7.330514,-7.901622],[8.565213,2.203383]]], dtype = "float64")#candidate|5618|(9, 7, 2)|const|float64
bop_5619 = relay.minimum(call_5615.astype('int16'), relay.reshape(const_5618.astype('int16'), relay.shape_of(call_5615))) # shape=(9, 7, 2)
bop_5622 = relay.minimum(call_5616.astype('int16'), relay.reshape(const_5618.astype('int16'), relay.shape_of(call_5616))) # shape=(9, 7, 2)
uop_5634 = relay.sigmoid(const_5618.astype('float32')) # shape=(9, 7, 2)
func_3047_call = mod.get_global_var('func_3047')
func_3051_call = mutated_mod.get_global_var('func_3051')
const_5644 = relay.const([-1.739950,-1.884445,5.929667,1.338064,-8.796762,6.495327,-8.931968,6.095613,-4.518491,-0.578768,1.103414,2.524409,-3.401520,8.875632,4.409435,9.629431,-5.227955,-6.202602,-4.285321,-6.499026,-4.633710,-3.558512,3.683908,7.219465,-2.997017,-2.081854,4.429506,-3.884562,4.624081,1.105925,-5.404779,-3.582791,9.611745,-1.345749,-0.811892,-4.747300,-3.725579,-9.711144,9.939258,7.285931,2.169866,0.936968,-7.574520,-9.795643,3.239971,-6.186688,0.444472,3.411450,6.743438,-1.349250,-1.361927,-9.640014,5.686469,-0.792528,-9.708366,9.983252,7.638152,-9.805729,-8.630462,6.742463,9.074488,2.020600,-5.792281,3.521525,-4.682593,3.964391,-9.892448,4.363606,-5.290758,-5.383277,7.127674,6.543381,2.239715,-1.531571,-8.604518,7.772355,-7.764362,-8.466211,3.876467,-2.661921,4.655615,-3.274904,-3.022963,-7.901885,3.941927,1.658407,-0.398405,5.471253,3.974028,7.018930,9.228691,8.530523,1.701055,-0.801218,0.449462,-1.467916,0.601707,-4.292974,-3.020261,-7.420623,-3.486480,-7.484997,-8.529172,-6.721187,-9.020469,-8.015244,-4.584523,7.636653,7.336676,1.779074,-5.582471,-6.702341,-0.620095,7.987527,1.465711,8.003726,-6.837771,-6.533065,3.443897,-1.739795,-3.865632,-2.274881,-1.353875,-5.586818,6.595440,-1.584817,7.526894,9.315855,3.998463,-4.607903,5.613422,-6.202802,2.466437,-0.448755,9.813061,-2.552905,7.973358,1.974233,-9.856796,-2.888307,4.700165,-1.343273,5.809515,-0.905185,-2.696199,8.911573,-0.963062,5.674924,-9.276214,3.390627,-2.849727,5.750315,-5.740369,8.906669,-9.222364,-2.932866,-6.693576,-1.257010,5.162424,9.416922,3.417453,8.889473,-4.177220,8.522899,-4.267485,7.165277,6.682876,7.285324,0.313814,-1.535589,-5.877345,8.016669,5.761273,-7.444975,-4.083953,1.863858,-6.853327,-5.543535,8.537899,6.226639,-9.432155,2.012640,2.928200,5.349586,6.986050,-8.757013,-6.452772,4.236619,0.034840,-4.692052,3.588419,9.850569,-4.746291,-9.686385,1.937349,-7.026992,-0.640527,2.111820,-0.124715,-0.674479,5.406638,1.974869,-0.730152,0.039288,-2.735983,-6.449438,3.883353,3.669535,0.489287,-7.387176,7.888378,-7.282583,-9.970683,4.573689,-4.744302,-1.452426,-4.121317,6.946944,-7.511577,-8.863696,3.273482,-9.186604,-3.765013,-1.284703,-5.519904,-0.553470,8.569498,6.601615,1.469089,-5.055916,0.972689,9.332950,-5.095148,-5.928911,0.048275,9.737893,6.443480,-8.965298,1.491438,5.557828,1.662626,5.361047,-1.320679,-5.463996,8.815322,6.096050,5.345307,-4.589822,-9.311084,9.404574,6.621780,-9.280558,-0.623502,-7.286144,7.178924,4.673826,-6.240787,-3.115115,-8.355401,-1.919676,6.242925,-7.455228,-4.570548,7.494721,1.127248,-0.952532,3.963913,-2.340576,2.958379,-0.119064,-3.042758,7.203074,-2.464497,-6.976218,-9.311958,3.707690,-7.186928,3.204773,-7.655508,9.132250,0.590608,3.930625,-2.268990,-6.001305,-5.175398,6.269180,5.364142,9.774817,-4.539443,-8.147258,-3.532645,-4.582659,5.161887,2.283683,-6.672702,2.971764,6.353568,3.568238,-9.758055,5.143478,-0.707315,-6.517296,-9.751034,5.254008,1.884917,1.914351,6.601571,-6.017372,3.614935,1.369587,6.855015,4.861627,8.101982,-7.641210,9.080196,-6.590308,-4.157043,5.654299,0.995197,7.911152,-9.953217,-4.995998,8.117049,-8.537717,8.155277,-8.257808,-1.071816,4.635938,-4.366907,-5.967109,3.957533,9.116306,7.531357,-8.359329,-6.330297,2.867590,7.134656,-8.245302,-8.191922,0.038978,-8.774710,-6.054414,-1.352063,-9.906963,-5.439853,-6.093455,-3.898881,0.742087,-1.233036,-6.942436,-2.137620,8.089946,5.121911,-1.237646,-5.353207,4.609190,0.751098,6.330511,6.511130,0.318813,-1.910165,-0.642122,2.748200,-4.924117,0.880155,-6.858697,-1.967075,0.802956,-2.536654,-2.697821,-1.619050,5.619328,4.785597,2.962942,2.398914,-2.064058,-4.048509,-6.599517,2.722128,2.884530,5.547239,-3.791397,2.719578,3.355664,3.300821,-3.188420,-8.237603,2.722376,-0.144775,-1.638095,3.367693,-9.005162,6.156161,-0.161043,7.042030,-3.311785,0.011227,9.766444,-6.938164,-1.152246,-2.946603,4.543750,7.528201,-8.265252,1.159347,1.118662,-1.515931,-3.994133,-0.487627,-7.444626,-5.174767,-1.246441,6.022694,-6.321231,-9.319756,5.040924,3.547014,8.117928,6.567943,2.175093,2.271423,-3.921834,-7.787974,6.608176,8.421121,-7.821345,-3.453454,3.961177,-1.323251,-7.487869,2.817406,6.213555,-2.334812,4.015547,3.433140,1.538011,9.201065,-8.003268,-8.913087,-7.146835,2.408743,-8.023095,2.955246,4.729052,7.890991,-5.312815,3.965550,-4.779007,5.342108,2.671836,-9.689923,3.586358,-8.542300,2.299987,8.194953,-0.252541,-0.814577,6.288696,0.163191,-8.838485,-1.173575,0.954112,-9.570592,9.658920,0.096491,-2.315955,8.048066,2.900334,8.382038,3.666235,-0.354017,4.050851,-1.098481,-9.667003,6.095786,-2.472612,5.472461,4.338595,9.506564,1.946501,-3.013280,-9.335224,3.609747,5.587385,-2.328382,-2.358507,5.623337,-0.642691,-1.281982,5.071780,8.725312,6.944235,6.399875,-5.693737,0.436215,0.425770,-3.911011,-6.360536,0.077176,-3.188988,-0.399279,-5.691783,6.188373,0.899404,5.041002,5.060678,-2.465265,0.669262,-2.616428,9.617509,-1.156293,7.793481,-2.445337,-2.123839,6.693508,-7.844061,0.073947,8.102615,8.417708,-3.214495,4.535484,7.899973,-3.762777,7.811648,-6.393022,8.387894,4.793155,5.078704,-5.146729,8.563642,5.121912,2.451250,-6.274244,0.514700,2.713533,-5.044732,3.750103,-9.314147,6.550989,-0.567415,-8.073841,-0.683594,-1.277387,-9.464230,7.584095,1.136686,6.453584,-6.852260,7.162350,5.067842,4.242805,-9.597636,6.759011,7.901289,-3.168097,-3.523229,1.959732,1.576031,6.849470,-1.271863,1.850881,4.454509,-7.682963,5.002782,4.456084,-2.799764,-1.739461,9.925244,6.182012,-4.712743,1.301105,3.445294,0.515826,-7.840097,-1.864164,-9.429751,-2.632423,-2.099412,1.837292,4.149326,-1.437673,1.509166,-7.034855,-0.345481,6.406568,8.553883,1.765696,5.361952,6.276057,6.849448,-4.756115,-3.068858,5.797649,5.280863,-4.407431,2.736277,-1.559124,6.974847,-0.482664,6.254045,6.072191,-4.437970,0.784456,4.678635,5.425507,-4.508943,-0.582623,6.900671,9.034517,-3.700679,7.323344,-2.878979,3.356791,-8.154014,4.940432,2.902172,-7.373693,6.363626,-7.006642,0.080462,-4.743270,6.076909,-0.940602,-8.846821,-0.387799,7.186657,6.860585,4.573245,4.247045,-1.955424], dtype = "float64")#candidate|5644|(630,)|const|float64
call_5643 = relay.TupleGetItem(func_3047_call(relay.reshape(const_5644.astype('float64'), [9, 14, 5]), relay.reshape(const_5644.astype('float64'), [9, 14, 5]), ), 1)
call_5645 = relay.TupleGetItem(func_3051_call(relay.reshape(const_5644.astype('float64'), [9, 14, 5]), relay.reshape(const_5644.astype('float64'), [9, 14, 5]), ), 1)
uop_5654 = relay.exp(uop_5634.astype('float32')) # shape=(9, 7, 2)
func_1600_call = mod.get_global_var('func_1600')
func_1601_call = mutated_mod.get_global_var('func_1601')
call_5661 = relay.TupleGetItem(func_1600_call(), 1)
call_5662 = relay.TupleGetItem(func_1601_call(), 1)
output = relay.Tuple([bop_5619,call_5643,const_5644,uop_5654,call_5661,])
output2 = relay.Tuple([bop_5622,call_5645,const_5644,uop_5654,call_5662,])
func_5663 = relay.Function([], output)
mod['func_5663'] = func_5663
mod = relay.transform.InferType()(mod)
output = func_5663()
func_5664 = relay.Function([], output)
mutated_mod['func_5664'] = func_5664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4842_call = mod.get_global_var('func_4842')
func_4843_call = mutated_mod.get_global_var('func_4843')
call_5678 = func_4842_call()
call_5679 = func_4842_call()
output = relay.Tuple([call_5678,])
output2 = relay.Tuple([call_5679,])
func_5687 = relay.Function([], output)
mod['func_5687'] = func_5687
mod = relay.transform.InferType()(mod)
output = func_5687()
func_5688 = relay.Function([], output)
mutated_mod['func_5688'] = func_5688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_364_call = mod.get_global_var('func_364')
func_366_call = mutated_mod.get_global_var('func_366')
call_5719 = func_364_call()
call_5720 = func_364_call()
output = relay.Tuple([call_5719,])
output2 = relay.Tuple([call_5720,])
func_5722 = relay.Function([], output)
mod['func_5722'] = func_5722
mod = relay.transform.InferType()(mod)
output = func_5722()
func_5723 = relay.Function([], output)
mutated_mod['func_5723'] = func_5723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1600_call = mod.get_global_var('func_1600')
func_1601_call = mutated_mod.get_global_var('func_1601')
call_5770 = relay.TupleGetItem(func_1600_call(), 1)
call_5771 = relay.TupleGetItem(func_1601_call(), 1)
func_4784_call = mod.get_global_var('func_4784')
func_4785_call = mutated_mod.get_global_var('func_4785')
call_5777 = func_4784_call()
call_5778 = func_4784_call()
func_1018_call = mod.get_global_var('func_1018')
func_1022_call = mutated_mod.get_global_var('func_1022')
var_5806 = relay.var("var_5806", dtype = "uint16", shape = (1320,))#candidate|5806|(1320,)|var|uint16
call_5805 = relay.TupleGetItem(func_1018_call(relay.reshape(var_5806.astype('uint16'), [12, 11, 10]), relay.reshape(var_5806.astype('uint8'), [12, 11, 10]), ), 4)
call_5807 = relay.TupleGetItem(func_1022_call(relay.reshape(var_5806.astype('uint16'), [12, 11, 10]), relay.reshape(var_5806.astype('uint8'), [12, 11, 10]), ), 4)
func_4287_call = mod.get_global_var('func_4287')
func_4288_call = mutated_mod.get_global_var('func_4288')
call_5810 = func_4287_call()
call_5811 = func_4287_call()
uop_5825 = relay.sinh(call_5805.astype('float32')) # shape=(2, 1, 10)
uop_5827 = relay.sinh(call_5807.astype('float32')) # shape=(2, 1, 10)
func_645_call = mod.get_global_var('func_645')
func_648_call = mutated_mod.get_global_var('func_648')
var_5840 = relay.var("var_5840", dtype = "int64", shape = (1100,))#candidate|5840|(1100,)|var|int64
call_5839 = relay.TupleGetItem(func_645_call(relay.reshape(var_5840.astype('int64'), [10, 10, 11])), 0)
call_5841 = relay.TupleGetItem(func_648_call(relay.reshape(var_5840.astype('int64'), [10, 10, 11])), 0)
uop_5844 = relay.exp(var_5840.astype('float32')) # shape=(1100,)
uop_5846 = relay.asinh(uop_5844.astype('float64')) # shape=(1100,)
func_3531_call = mod.get_global_var('func_3531')
func_3532_call = mutated_mod.get_global_var('func_3532')
call_5848 = relay.TupleGetItem(func_3531_call(), 0)
call_5849 = relay.TupleGetItem(func_3532_call(), 0)
uop_5851 = relay.sigmoid(uop_5846.astype('float32')) # shape=(1100,)
func_1890_call = mod.get_global_var('func_1890')
func_1891_call = mutated_mod.get_global_var('func_1891')
call_5868 = relay.TupleGetItem(func_1890_call(), 1)
call_5869 = relay.TupleGetItem(func_1891_call(), 1)
const_5876 = relay.const([-1.311135,-5.297182,-5.479695,0.986692,6.179745,6.024681,4.748061,-0.574838,5.019955,0.685831,1.478426,-5.129135,9.437237,-2.059396,-1.331549,-6.186534,7.368772,-5.636685,-7.381187,2.415451,6.273870,-6.169004,-7.864719,0.116070,6.773192,0.691908,5.541780,9.910696,8.520990,-0.488716,1.734887,-7.206435,-3.139098,3.906545,-9.938929,-3.773457,7.009053,-4.448791,6.403229,2.305222,-4.212291,8.928237,-1.085126,-5.730838,2.346182,-6.464248,1.270261,5.268975,7.500169,9.449701,9.247186,9.314289,-8.744586,-2.049365,5.331858,-4.159539,-5.948152,3.924177,-5.850245,-1.403634,7.002460,4.329327,4.715080,-4.849309,3.527725,-3.381803,4.474341,1.861817,-5.743693,8.096281,8.523906,4.176006,-1.503752,7.414612,8.644043,-4.952730,-2.066577,4.079226,-5.212502,-6.433877,5.713969,-2.227314,3.795603,-3.242334,4.973427,3.548577,-7.132779,4.624489,-8.974868,3.552881,-1.344137,-9.522380,1.741702,8.224728,4.912572,1.222325,-3.934768,4.416610,3.250763,4.583084,7.027893,-0.034449,-1.906042,-1.302993,-7.530778,-2.832645,7.921480,3.851077,-9.918758,-4.799788,-4.566472,7.567253,2.233627,-4.801592,-3.186645,-8.096424,3.665477,4.774180,-7.710750,-9.305763,-7.582449,5.441911,1.113660,-0.873091,3.074190,3.355414,8.551504,2.979378,2.258357,1.412571,8.678726,7.269207,-2.126347,-0.992157,8.960446,8.760437,0.406079,5.702214,4.735798,7.545455,1.287063,5.995840,1.698694,5.560778,-0.230782,-7.045981,-4.498209,-8.730858,0.802956,2.260933,0.131011,-5.737971,-8.345931,7.533135,6.599407,-7.712919,7.386365,4.180285,-9.129664,8.201597,-3.004298,6.864409,-2.644504,4.482857,-6.507894,-0.229384,-2.479714,5.492492,-1.090002,-4.708377,8.329925,-1.791514,-5.228737,4.258270,6.179987,-7.689807,-9.277317,-9.360707,7.705200,-5.036819,2.569999,-9.336985,9.433765,-2.607550,-4.132220,-0.591703,4.577694,5.690990,-8.373749,9.590033,7.162436,3.531957,7.974755,-2.740178,-4.759980,-3.738042,2.390349,2.394113,-0.705741,8.955641,-1.213201,-0.556188,-1.336913,-0.310960,-6.522368,-7.470930,3.281493,-2.739769,-2.994834,9.719554,0.141303,-1.958592,-6.233024,-6.309091,3.569436,-6.658010,0.474514,6.195595,-1.689738,-3.790316,0.379511,-2.560737,9.768772,7.402384,-5.988445,-2.905714,9.407986,-0.322475,-8.066331,-7.430741,-1.821304,1.150026,-1.773578,-0.625385,-6.618853,5.641000,4.344782,-0.002708,-0.171014,-1.834787,9.551160,1.987115,2.371045,-9.852555,-3.102713,2.737714,9.467253,-8.549172,-0.157736,-7.393432,8.171444,-9.357815,-6.962677,4.105477,3.408652,8.830847,-8.909956,0.506647,-4.223705,1.236859,-5.598754,-5.244510,-7.369090,6.490537,1.470625,2.783696,-7.907212,9.010064,8.120137,8.703453,1.152837,8.417046,0.086716,7.199024,-0.477642,-1.829874,-0.517689,5.612349,8.238262,0.353233,-3.106106,-2.999024,-6.252454,9.647687,-8.316779,-4.964800,6.579209,-9.971003,-1.491337,6.653527,-3.214612,-6.974063,-2.951752,8.532495,-4.044445,-9.559527,-0.591902,9.979731,-9.326214,-3.699971,-0.626301,-6.886547,-1.994828,-6.221273,4.693662,3.934120,-0.497304,-7.594210,6.715032,-9.418396,-4.294022,7.950631,2.751599,3.743308,7.364028,6.122522,1.214428,-8.953878,-0.325669,-6.183036,-5.754583,6.188681,1.690683,8.343423,-2.183148,0.169115,-5.428937,4.621029,6.402692,2.938904,-8.966388,-3.602066,4.843663,5.514448,-7.808078,6.825876,4.154273,7.558009,-7.095366,-9.619885,-2.015380,7.306522,-7.721919,1.966803,2.622388,-2.083751,8.809253,4.967822,0.259397,-9.128119,7.977498,-1.746700,-6.006647,6.431641,-0.489804,5.495011,4.812553,0.259975,5.030320,-9.458428,-3.725430,-6.263596,5.920354,-3.734930,-0.115702,-4.146056,-8.399103,0.751168,-8.132232,3.298176,-9.703363,-1.221132,0.912993,7.901732,-2.761956,9.679391,-4.004193,-1.888268,-3.554771,0.886372,8.591733,-3.382695,-4.669291,-6.295163,-3.077892,-7.776635,3.395751,1.908065,-6.371821,7.413268,-3.808107,7.086850,9.300556,-4.955085,-2.820200,-3.116476,-1.804259,1.377394,-2.727635,3.849226,9.436096,9.829960,-0.398071,1.669418,7.385387,6.416251,-5.720566,5.523952,-2.900444,2.203749,0.307730,-9.014101,-1.691190,-2.280809,-7.092166,5.361127,9.008211,-8.103738,9.543667,4.771682,-9.448576,-0.988339,3.645089,-2.104650,-8.787966,0.034009,-9.797308,9.003967,1.271102,9.381906,0.753958,-2.057338,-7.244673,8.118734,-2.982987,-8.251503,5.420002,0.978861,-4.391331,9.556060,7.533360,-2.975180,-6.717291,-3.518335,-5.469790,4.129185,6.810202,-2.777215,-1.684540,9.893298,-3.835955,-8.491098,7.450751,3.289385,7.870773,-7.262806,8.123106,-4.510833,-8.669351,3.972714,9.946436,-8.737350,-6.690222,-7.415829,-3.482860,-2.974516,6.433755,1.254060,-1.129140,8.581500,6.176730,8.040936,-0.315752,-8.750657,-0.575814,7.325975,7.168746,-0.953514,9.574481,-3.264900,0.771612,-7.707445,9.851494,8.937277,-1.634919,-1.322035,-1.614551,-7.142620,3.566214,4.285534,3.814455,5.090067,-7.903512,-0.577957,-6.863654,-1.894381,1.131096,1.732760,-8.371470,6.145623,7.521109,-8.762873,5.549012,-2.683393,0.587431,-8.132782,5.524661,0.570006,-6.659987,6.738699,3.601427,-1.789212,-5.824815,5.711137,-9.717671,-6.720086,-9.021537,4.684176,5.258506,8.237056,2.030223,2.477537,6.048024,-4.356880,4.192694,6.574462,5.326679,9.871459,3.146482,-3.208661,8.000413,3.587878,7.503281,2.351022,-5.994960,-8.516370,8.626139,-2.375537,-9.147751,-5.612288,-2.815766,-1.918787,2.377173,-6.652274,9.317496,-2.886120,4.098208,-5.165109,-3.513489,3.984615,-8.303995,-6.856600,-9.756195,4.702583,1.209830,-4.336362,1.573428,-3.340407,-9.465077,5.726895,8.183590,2.311659,0.675511,-0.067865,8.928824,-1.780635,1.781033,4.079655,-6.320494,-0.914255,-6.467582,0.568593,-3.369830,-8.248671,-4.293931,-7.685315,1.502998,-1.763671,6.582659,-8.457703,0.280330,0.312529,1.889905,-8.367676,1.356496,-9.468075,1.003817,0.725043,6.507722,-4.326028,7.234782,5.411509,-0.762077,2.390789,-5.405967,1.984074,-9.183785,-2.056892,6.257415,9.746464,-5.448326,0.014913,-5.294291,6.814312,-4.462436,4.483750,-1.836445,4.911624,9.447761,-2.670198,-1.510700,6.226429,-9.567440,0.076770,-3.069748,-8.717924,-2.947468,-2.872919,-0.243389,-1.216627,8.756605,-3.312363,-3.142059,5.816252,-1.249446,-9.854018,5.306973,-3.159403,4.128051,7.794886,-3.873172,-8.018524,3.394210,0.522615,-7.290223,9.277974,-7.595201,2.608122,6.430218,-1.186416,9.182815,-8.705067,-4.192604,-0.745826,-3.963750,6.933596,-5.193210,5.035851,-5.234663,8.726563,-5.361222,-0.911226,6.768795,-3.373296,-4.287188,-9.131648,7.750768,-2.266342,6.877972,6.700500,5.427169,8.385575,6.327725,2.715677,8.857867,-4.337241,9.744260,-6.825665,0.386376,9.043307,3.400084,5.788281,3.399889,-1.345668,-2.603572,-4.809532,-5.306359,1.659411,8.761127,5.414879,-3.395179,-1.714641,5.332209,-4.680276,7.746335,-0.864924,2.104719,4.546220,-2.822124,-6.118221,-7.895879,-6.200246,-3.106786,-2.531670,-1.386615,-7.083647,4.363600,2.933409,-4.771372,1.240109,7.557559,-7.818723,5.498311,7.537094,-6.365227,1.203111,9.227671,0.694801,3.200769,6.097271,-3.499143,-6.796635,-8.845034,-6.030574,3.033682,9.168570,7.673801,-3.237123,1.350813,-5.716756,8.917203,-6.951113,3.974671,-6.979149,8.895333,1.713314,9.661097,-5.441558,6.852607,-1.078690,-7.314728,0.578713,-4.740285,3.280533,-8.420232,3.398670,7.733123,-1.512689,3.040117,3.253021,-1.542974,-9.418073,8.407931,6.801648,4.431511,9.154035,4.974971,-2.326856,-0.695851,-5.207099,9.247739,-1.987378,3.512083,-5.329278,4.075818,-8.954652,-2.905604,-9.956094,6.466677,-5.165172,8.660342,-2.272372,-6.013977,-3.068734,-3.183189,3.717941,-0.342880,-5.438614,-7.811129,0.257458,2.388718,5.692197,-8.445895,3.658071,-3.099509,7.006679,6.485372,-2.680482,-4.982325,5.630330,2.738839,-8.988856,-9.089834,-5.766558,2.346651,7.531582,2.725275,-4.405534,-0.960925,1.702634,7.231606,-0.663979,-2.513688,6.283989,-0.673554,-1.719785,2.910311,0.073441,7.135422,5.675210,3.678654,2.959272,3.673674,5.796496,5.000848,-8.986040,7.268963,-3.185262,-8.341859,-0.953743,-5.613904,-1.362844,3.115572,9.240851,0.404772,-4.667845,6.571392,5.876029,1.085781,-6.672937,2.552809,-1.201682,-8.367982,6.293637,-3.522034,3.242877,-8.226470,-6.317030,6.181253,-8.069606,-3.817897,-9.640456,1.953166,2.970686,-8.437692,3.431286,-8.267668,-2.572359,-6.647053,4.808001,8.381760,2.281763,8.447245,9.337681,-3.734567,9.074320,-7.763634,-1.117067,-7.251739,2.748664,-1.460112,-9.358636,-8.544881,0.358121,-5.592571,0.609240,1.009682,0.509463,-9.488135,2.588155,9.159393,-6.953059,-4.157008,7.991505,-9.530483,8.999741,3.342014,2.556576,-2.624147,6.995471,-4.195524,-2.297860,1.925873,-6.156487,0.436103,-3.224527,-2.583541,-7.519238,-1.072386,7.153052,-4.701792,5.772839,6.523985,8.909591,9.143664,-7.987031,5.856426,8.079135,4.828367,6.387179,1.366785,9.811612,-1.661875,4.431801,8.214650,6.479747,3.368601,3.741529,2.956675,1.597929,3.783043,-7.912193,-0.070983,-9.474994,7.742085,-0.058616,0.012760,3.169284,-1.052476,-7.224119,5.794835,9.496511,-3.503625,6.758410,-4.340811,-7.581272,8.979708,-0.681748,-2.347570,9.683588,-1.821244,8.343991,4.950090,1.727796,8.350464,7.327446,9.576162,1.580682,7.103616,-6.183084,6.139548,-7.540433,2.816745,4.410250,3.513802,-6.336579,-1.723411,6.618383,-5.859586,7.883212,3.045033,-3.629959,-4.098387,-4.495667,7.778371,4.054907,-6.696581,3.971628,-7.255428,9.695784,3.424923,-2.262330,9.717395,7.553250,-8.474677,9.233321,0.068033,3.071708,-5.455365,5.268357,-3.144720,-8.466561,-9.809340,-5.074665,-2.555708,-1.956427,2.882724,-1.795597,7.283068,-4.911898,-1.901321,3.943617,-3.365049,9.136318,-4.322034,-6.732737,0.490067,2.275695,-5.175393,8.728014,-5.836903,-9.230409,-0.634356,-9.743960,-9.321856,2.882058,4.185367,-1.376063,6.892803,-3.451175,-2.684214,-4.753377,9.003490,-9.751947,-3.370136,0.906623,5.743520,-3.374428,-9.990016,4.129700,-2.459077,8.529755,6.708264,5.803806,-2.682018,3.213079,-1.230177,-1.487788,8.189006,3.551621,-1.252053,-6.494298,-9.835769,2.700379,-3.056467,9.187760,-8.002685,-0.080535,-8.655384,-5.143256,8.563920,2.497725,-4.579352,2.625441,-9.146409,7.050364,8.573309,0.230787,-7.989375,-2.110246,1.672631,5.579316,5.576965,-3.006799,9.458025,-4.202396,-2.450608,-5.126550,5.875630,-1.050053,-8.963887,5.305982,-5.966215,7.171454,2.820961,1.359239,7.853434,-2.577679,-5.001053,-2.029401,-1.134923,-4.325307,4.275368,2.040551,-5.952946,-2.355223,6.630911,3.183560,-8.416939,-2.595837,-8.248039,6.357122,4.698301,-6.225923,-1.185353,3.677862,1.323050,3.679244,6.841672,-5.126851,-2.849393,-3.394280,-5.347576,4.328924,5.616380,-6.945762,4.302648,3.092869,-8.382254,-9.318171,5.955342,3.064419,9.785456,5.119560,2.053973,0.768079,-9.094150,8.905022,7.638663,-9.365331,-7.387933,-2.262706,-0.305072,-2.187074,-9.132658,8.636924,2.510301,-9.268792,6.919339,1.515354], dtype = "float32")#candidate|5876|(1100,)|const|float32
bop_5877 = relay.not_equal(uop_5851.astype('bool'), relay.reshape(const_5876.astype('bool'), relay.shape_of(uop_5851))) # shape=(1100,)
func_408_call = mod.get_global_var('func_408')
func_410_call = mutated_mod.get_global_var('func_410')
call_5885 = relay.TupleGetItem(func_408_call(), 1)
call_5886 = relay.TupleGetItem(func_410_call(), 1)
func_1018_call = mod.get_global_var('func_1018')
func_1022_call = mutated_mod.get_global_var('func_1022')
call_5897 = relay.TupleGetItem(func_1018_call(relay.reshape(var_5806.astype('uint16'), [12, 11, 10]), relay.reshape(var_5806.astype('uint8'), [12, 11, 10]), ), 4)
call_5898 = relay.TupleGetItem(func_1022_call(relay.reshape(var_5806.astype('uint16'), [12, 11, 10]), relay.reshape(var_5806.astype('uint8'), [12, 11, 10]), ), 4)
func_4098_call = mod.get_global_var('func_4098')
func_4100_call = mutated_mod.get_global_var('func_4100')
call_5904 = relay.TupleGetItem(func_4098_call(), 1)
call_5905 = relay.TupleGetItem(func_4100_call(), 1)
uop_5911 = relay.log(bop_5877.astype('float32')) # shape=(1100,)
func_4896_call = mod.get_global_var('func_4896')
func_4897_call = mutated_mod.get_global_var('func_4897')
call_5914 = relay.TupleGetItem(func_4896_call(), 0)
call_5915 = relay.TupleGetItem(func_4897_call(), 0)
output = relay.Tuple([call_5770,call_5777,var_5806,call_5810,uop_5825,call_5839,call_5848,call_5868,call_5885,call_5897,call_5904,uop_5911,call_5914,])
output2 = relay.Tuple([call_5771,call_5778,var_5806,call_5811,uop_5827,call_5841,call_5849,call_5869,call_5886,call_5898,call_5905,uop_5911,call_5915,])
func_5922 = relay.Function([var_5806,var_5840,], output)
mod['func_5922'] = func_5922
mod = relay.transform.InferType()(mod)
mutated_mod['func_5922'] = func_5922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5922_call = mutated_mod.get_global_var('func_5922')
var_5924 = relay.var("var_5924", dtype = "uint16", shape = (1320,))#candidate|5924|(1320,)|var|uint16
var_5925 = relay.var("var_5925", dtype = "int64", shape = (1100,))#candidate|5925|(1100,)|var|int64
call_5923 = func_5922_call(var_5924,var_5925,)
output = call_5923
func_5926 = relay.Function([var_5924,var_5925,], output)
mutated_mod['func_5926'] = func_5926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4457_call = mod.get_global_var('func_4457')
func_4458_call = mutated_mod.get_global_var('func_4458')
call_5934 = relay.TupleGetItem(func_4457_call(), 1)
call_5935 = relay.TupleGetItem(func_4458_call(), 1)
func_4922_call = mod.get_global_var('func_4922')
func_4925_call = mutated_mod.get_global_var('func_4925')
var_5937 = relay.var("var_5937", dtype = "uint16", shape = (1320,))#candidate|5937|(1320,)|var|uint16
call_5936 = relay.TupleGetItem(func_4922_call(relay.reshape(var_5937.astype('uint16'), [12, 11, 10])), 1)
call_5938 = relay.TupleGetItem(func_4925_call(relay.reshape(var_5937.astype('uint16'), [12, 11, 10])), 1)
output = relay.Tuple([call_5934,call_5936,var_5937,])
output2 = relay.Tuple([call_5935,call_5938,var_5937,])
func_5955 = relay.Function([var_5937,], output)
mod['func_5955'] = func_5955
mod = relay.transform.InferType()(mod)
mutated_mod['func_5955'] = func_5955
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5956 = relay.var("var_5956", dtype = "uint16", shape = (1320,))#candidate|5956|(1320,)|var|uint16
func_5955_call = mutated_mod.get_global_var('func_5955')
call_5957 = func_5955_call(var_5956)
output = call_5957
func_5958 = relay.Function([var_5956], output)
mutated_mod['func_5958'] = func_5958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1429_call = mod.get_global_var('func_1429')
func_1430_call = mutated_mod.get_global_var('func_1430')
call_5967 = func_1429_call()
call_5968 = func_1429_call()
func_4059_call = mod.get_global_var('func_4059')
func_4061_call = mutated_mod.get_global_var('func_4061')
call_5969 = relay.TupleGetItem(func_4059_call(), 0)
call_5970 = relay.TupleGetItem(func_4061_call(), 0)
bop_5971 = relay.right_shift(call_5967.astype('int32'), call_5969.astype('int32')) # shape=(2, 9, 10)
bop_5974 = relay.right_shift(call_5968.astype('int32'), call_5970.astype('int32')) # shape=(2, 9, 10)
func_3531_call = mod.get_global_var('func_3531')
func_3532_call = mutated_mod.get_global_var('func_3532')
call_5980 = relay.TupleGetItem(func_3531_call(), 0)
call_5981 = relay.TupleGetItem(func_3532_call(), 0)
func_3598_call = mod.get_global_var('func_3598')
func_3600_call = mutated_mod.get_global_var('func_3600')
call_5982 = func_3598_call()
call_5983 = func_3598_call()
uop_5984 = relay.asin(bop_5971.astype('float32')) # shape=(2, 9, 10)
uop_5986 = relay.asin(bop_5974.astype('float32')) # shape=(2, 9, 10)
func_4287_call = mod.get_global_var('func_4287')
func_4288_call = mutated_mod.get_global_var('func_4288')
call_5994 = func_4287_call()
call_5995 = func_4287_call()
uop_6002 = relay.atanh(uop_5984.astype('float64')) # shape=(2, 9, 10)
uop_6004 = relay.atanh(uop_5986.astype('float64')) # shape=(2, 9, 10)
bop_6016 = relay.mod(call_5982.astype('float32'), relay.reshape(call_5980.astype('float32'), relay.shape_of(call_5982))) # shape=(1, 11, 10)
bop_6019 = relay.mod(call_5983.astype('float32'), relay.reshape(call_5981.astype('float32'), relay.shape_of(call_5983))) # shape=(1, 11, 10)
output = relay.Tuple([call_5994,uop_6002,bop_6016,])
output2 = relay.Tuple([call_5995,uop_6004,bop_6019,])
func_6022 = relay.Function([], output)
mod['func_6022'] = func_6022
mod = relay.transform.InferType()(mod)
mutated_mod['func_6022'] = func_6022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6022_call = mutated_mod.get_global_var('func_6022')
call_6023 = func_6022_call()
output = call_6023
func_6024 = relay.Function([], output)
mutated_mod['func_6024'] = func_6024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_298_call = mod.get_global_var('func_298')
func_300_call = mutated_mod.get_global_var('func_300')
call_6040 = func_298_call()
call_6041 = func_298_call()
output = call_6040
output2 = call_6041
func_6043 = relay.Function([], output)
mod['func_6043'] = func_6043
mod = relay.transform.InferType()(mod)
output = func_6043()
func_6044 = relay.Function([], output)
mutated_mod['func_6044'] = func_6044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_726_call = mod.get_global_var('func_726')
func_728_call = mutated_mod.get_global_var('func_728')
call_6055 = func_726_call()
call_6056 = func_726_call()
func_4955_call = mod.get_global_var('func_4955')
func_4956_call = mutated_mod.get_global_var('func_4956')
call_6064 = relay.TupleGetItem(func_4955_call(), 0)
call_6065 = relay.TupleGetItem(func_4956_call(), 0)
uop_6066 = relay.sigmoid(call_6055.astype('float32')) # shape=(2, 1, 10)
uop_6068 = relay.sigmoid(call_6056.astype('float32')) # shape=(2, 1, 10)
output = relay.Tuple([call_6064,uop_6066,])
output2 = relay.Tuple([call_6065,uop_6068,])
func_6073 = relay.Function([], output)
mod['func_6073'] = func_6073
mod = relay.transform.InferType()(mod)
output = func_6073()
func_6074 = relay.Function([], output)
mutated_mod['func_6074'] = func_6074
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6111 = relay.var("var_6111", dtype = "uint8", shape = (3, 3, 9))#candidate|6111|(3, 3, 9)|var|uint8
var_6112 = relay.var("var_6112", dtype = "uint8", shape = (3, 3, 9))#candidate|6112|(3, 3, 9)|var|uint8
bop_6113 = relay.equal(var_6111.astype('bool'), relay.reshape(var_6112.astype('bool'), relay.shape_of(var_6111))) # shape=(3, 3, 9)
func_4476_call = mod.get_global_var('func_4476')
func_4479_call = mutated_mod.get_global_var('func_4479')
var_6119 = relay.var("var_6119", dtype = "uint32", shape = ())#candidate|6119|()|var|uint32
call_6118 = relay.TupleGetItem(func_4476_call(relay.reshape(var_6119.astype('uint32'), [])), 0)
call_6120 = relay.TupleGetItem(func_4479_call(relay.reshape(var_6119.astype('uint32'), [])), 0)
func_4842_call = mod.get_global_var('func_4842')
func_4843_call = mutated_mod.get_global_var('func_4843')
call_6121 = func_4842_call()
call_6122 = func_4842_call()
func_3059_call = mod.get_global_var('func_3059')
func_3061_call = mutated_mod.get_global_var('func_3061')
call_6130 = relay.TupleGetItem(func_3059_call(), 0)
call_6131 = relay.TupleGetItem(func_3061_call(), 0)
output = relay.Tuple([bop_6113,call_6118,var_6119,call_6121,call_6130,])
output2 = relay.Tuple([bop_6113,call_6120,var_6119,call_6122,call_6131,])
func_6133 = relay.Function([var_6111,var_6112,var_6119,], output)
mod['func_6133'] = func_6133
mod = relay.transform.InferType()(mod)
var_6134 = relay.var("var_6134", dtype = "uint8", shape = (3, 3, 9))#candidate|6134|(3, 3, 9)|var|uint8
var_6135 = relay.var("var_6135", dtype = "uint8", shape = (3, 3, 9))#candidate|6135|(3, 3, 9)|var|uint8
var_6136 = relay.var("var_6136", dtype = "uint32", shape = ())#candidate|6136|()|var|uint32
output = func_6133(var_6134,var_6135,var_6136,)
func_6137 = relay.Function([var_6134,var_6135,var_6136,], output)
mutated_mod['func_6137'] = func_6137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4784_call = mod.get_global_var('func_4784')
func_4785_call = mutated_mod.get_global_var('func_4785')
call_6195 = func_4784_call()
call_6196 = func_4784_call()
func_5955_call = mod.get_global_var('func_5955')
func_5958_call = mutated_mod.get_global_var('func_5958')
var_6198 = relay.var("var_6198", dtype = "uint16", shape = (1320,))#candidate|6198|(1320,)|var|uint16
call_6197 = relay.TupleGetItem(func_5955_call(relay.reshape(var_6198.astype('uint16'), [1320,])), 0)
call_6199 = relay.TupleGetItem(func_5958_call(relay.reshape(var_6198.astype('uint16'), [1320,])), 0)
output = relay.Tuple([call_6195,call_6197,var_6198,])
output2 = relay.Tuple([call_6196,call_6199,var_6198,])
func_6208 = relay.Function([var_6198,], output)
mod['func_6208'] = func_6208
mod = relay.transform.InferType()(mod)
mutated_mod['func_6208'] = func_6208
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6209 = relay.var("var_6209", dtype = "uint16", shape = (1320,))#candidate|6209|(1320,)|var|uint16
func_6208_call = mutated_mod.get_global_var('func_6208')
call_6210 = func_6208_call(var_6209)
output = call_6210
func_6211 = relay.Function([var_6209], output)
mutated_mod['func_6211'] = func_6211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2155_call = mod.get_global_var('func_2155')
func_2156_call = mutated_mod.get_global_var('func_2156')
call_6215 = relay.TupleGetItem(func_2155_call(), 0)
call_6216 = relay.TupleGetItem(func_2156_call(), 0)
func_1819_call = mod.get_global_var('func_1819')
func_1822_call = mutated_mod.get_global_var('func_1822')
const_6219 = relay.const([-0.298737,-4.704595,-6.451808,8.850326,-4.527379,0.204955,-8.983556,4.451214,-4.498256,-6.092403,-0.974010,1.878406,4.242298,9.676888,-2.939910,-9.396158,-4.948520,5.763914,3.384558,-9.367679,-6.329002,5.144431,0.577624,0.358222,-6.535944,5.881060,-2.367397,-7.941859,-7.012531,3.617162,-1.599658,0.184033,-1.656941,1.789431,2.594401,8.986828,-3.893431,7.186031,-4.937103,9.677184,-6.087240,8.649891,-8.225790,-1.383823,-2.572813,5.357839,-8.651730,1.027629,-3.015230,-8.795813,-7.485402,4.407528,-1.839879,-2.695072,1.477010,5.185296,-1.971767,5.342191,-5.669730,7.158201,2.437789,9.109414,-0.630258,-6.733183,8.706411,-5.866822,-2.725482,-7.882780,-7.876651,4.617122,9.961573,-3.189047,-0.057906,-5.274700,5.180927,9.970734,-5.163996,-2.877728,5.415179,0.639149,7.217907,6.294208,-0.263358,-3.624928,-2.101646,-3.101698,-2.889604,-4.413498,-7.935782,0.065570,-4.714830,-9.805181,1.464881,3.673745,3.374483,-6.850876,7.733267,8.509104,5.190337,-9.884225,9.750756,1.238605,8.048369,-2.357689,-3.690971,-2.848364,-0.705700,-1.789416,3.313742,1.389762,-3.090574,-2.449997,1.636943,5.078639,5.759984,-7.597941,2.534715,4.856585,4.770435,-2.990393,8.799646,5.944381,-1.110063,-3.924272,0.449120,-4.577215,9.344591,5.232644,-7.455940,4.545841,1.577790,3.205909,-4.461746,4.926122,-8.033060,2.380263,-2.829253,-6.924305,-1.595369,8.540183,-0.323551,-9.634477,-3.599344,-0.239160,-5.115675,-8.547125,5.014104,-9.384059,-9.399222,-6.570603,-3.203735,7.718299,-7.501599,7.111582,-4.026423,-3.960320,-5.874042,-6.086887,3.744900,-8.528829,-3.976059,8.037271,-3.808005,2.445552,1.194695,9.071147,-4.853526,0.641289,-4.123107,1.597535,1.253553,6.484566,-3.545642,-0.088126,-6.029539,-1.493249,3.304102,1.999021,4.870069,2.199760,-5.756612,-3.504791,6.467960,5.752473,-8.935822,-1.972849,-9.736631,-5.635503,7.264528,-2.579754,5.146411,-3.428522,-4.376167,-3.319886,0.552609,3.378846,-0.629873,-0.038076,9.476351,-3.956238,-0.611733,0.188038,-2.957002,-7.381748,-4.400131,-3.910422,8.405826,-2.047691,-8.344485,4.066209,-7.869074,1.457979,6.596260,-9.505536,2.749919,-7.104857,8.386383,-3.519445,7.883818,1.916161,-4.385381,6.716064,1.512196,0.749055,-7.990297,9.449136,5.296222,-8.414888,-0.478188,4.267703,0.263577,3.627749,1.089631,-3.291743,-1.105268,-9.027565,6.901360,-3.397555,-2.833246,-5.509375,6.150546,4.416216,-0.261424,6.985621,4.516157,-1.183157,-1.806541,4.452345,-9.265946,9.320552,-6.493067,9.886774,1.812975,-5.364072,8.965786,2.060755,-2.780121,-7.844977,-1.295391,9.074271,-6.298210,-7.500608,9.298328,1.689380,5.165548,5.562326,-1.609470,-8.765883,-0.912230,2.689280,6.678497,-4.981443,-9.107093,5.384912,-6.069194,-2.190301,-4.655764,-7.017842,-3.094254,9.243905,-7.376987,6.313292,9.067658,-2.134087,-3.096026,-1.949186,-9.389069,3.848001,3.447312,0.373472,4.792711,-9.015602,-9.242136,-0.119177,-7.064427,8.553605,-4.102724,-8.281216,-0.395505,0.403847,-6.228788,-6.065676,7.557524,1.010070,-6.632670,-8.581713,-6.239314,-7.263436,6.267735,-1.956741,-7.862769,-8.807857,-5.666722,9.367256,-0.973091,-4.086399,-6.620232,8.805205,-2.352046,-0.741617,-0.859521,0.582300,9.648744,2.960412,-4.246007,4.873396,5.138916,6.957194,-3.092118,-9.246768,2.285592,9.262007,-1.360716,7.989542,-1.111860,3.542822,7.074649,2.438213,-1.157551,7.463792,-6.434446,-7.602378,0.472488,-2.035990,-7.686584,-1.262396,9.591827,8.463796,-0.249735,-5.729400,-6.858629,5.620846,-5.102774,-7.778078,-2.580801,3.321945,-1.137718,-4.661697,8.419962,4.463356,-6.237974,-4.481489,-3.534624,1.106721,-1.887329,0.952567,3.544806,-1.531420,1.560279,9.179929,3.177008,2.548014,-0.160617,5.820311,-0.028666,3.840224,-0.471263,-5.740582,4.228511,2.983762,4.115471,-8.322147,-5.586043,4.798183,1.441773,3.029272,8.813868,8.826590,-2.162061,-6.282614,1.700165,4.575055,4.458727,-5.813606,2.278081,-5.722855,-3.794034,-9.729259,-2.771891,4.930019,-5.320537,-9.534280,7.386771,2.159991,-3.763374,-4.141186,1.442897,1.065497,8.730646,5.905061,5.344775,3.410771,-6.764359,-0.449479,4.148565,-5.599084,-2.756650,-0.716654,-2.042693,-2.286649,4.974457,4.622999,-3.344054,3.189506,-7.129737,6.479528,-9.009735,-5.970652,-3.542531,1.201003,-2.237611,2.121981,-9.554106,-5.887160,6.740154,8.617480,5.603959,6.222977,7.857256,6.289821,3.543936,-5.587554,8.516811,-4.591738,9.027803,-8.773997,4.330086,3.178456], dtype = "float64")#candidate|6219|(448,)|const|float64
const_6220 = relay.const([6,3,-9,-3,-9,-1,-6,-9,7,10,-7,-8,9,-7,7,-6,-5,8,3,-8,-4,-7,-2,-3,6,2,-6,2,-8,-10,6,-7,-6,-4,8,-9,-5,-3,5,-3,-9,2,5,-1,-2,7,8,2,1,-10,10,-1,8,-1,10,-3,8,6,-9,4,7,-3,7,8,-1,-9,2,7,4,2,-1,4,-10,1,-7,-5,8,3,3,-5,2,7,-4,3,-4,3,-1,3,9,-5,10,-3,7,-6,-9,-7,7,-4,-10,-10,-5,-8,-9,-2,-8,5,4,-8,5,-3,7,5,2,6,10,6,6,-4,6,3,2,2,7,-8,4,-7,9,-6,3,3,-7,-9,-5,-9,-10,5,-2,7,-6,2,-4,4,10,4,-3,7,8,-6,2,3,10,3,6,-1,-4,-4,-1,4,8,5,7,-3,1,-9,5,-4,-2,6,8,10,-10,2,3,-3,4,-2,1,9,3,6,1,-2,8,3,-7,7,7,1,5,-1,-1,1,10,-5,-9,-2,10,5,4,-3,1,10,-9,-8,-4,-3,-3,8,-6,6,-3,-8,-4,10,-1,1,-1,9,-2,4,5,-1,-6,2,2,-9,-8,-8,2,-10,-9,4,-2,1,10,-7,5,-5,-7,-2,5,-3,-8,5,7,2,6,7,9,-9,-3,5,-6,-6,-7,1,-8,7,5,6,9,9,6,-1,-4,-5,1,-3,-2,10,-7,-5,9,-3,-8,-6,8,10,1,-10,-4,-10,-7,-1,-1,-2,6,-5,3,-9,6,-6,1,8,-9,-7,-3,9,-1,3,-3,-10,4,4,-3,8,8,-6,2,-3,4,6,-6,-9,7,-8,-9,-9,-6,-10,-6,10,4,3,10,9,-5,-1,-1,-9,-4,-9,9,-8,3,-6,8,-2,-10,10,-2,-3,-5,-9,7,-7,7,4,5,1,-9,6,-2,10,5,3,-1,6,1,4,-5,8,8,8,-3,-9,5,-10,6,-9,1,8,-8,-8,2,-6,-3,-1,-6,4,7,2,1,-10,-3,7,1,-8,2,8,7,2,-8,-1,-1,4,10,-3,7,7,-10,-5,-10,10,6,7,-3,5,4,-6,3,-5,5,6,-9,3,9,-2,9,-2,-1,-10,8,6,3,8,-3,1,-3,3,9,-3,3,7,9,-9,-8,5,-8,9,4,-7,10,-8,-4,5,4,-2,-5,-9,10,-7,10,-4,4,8,-1,-6,3,-4,-4,10,8,4,-3,-10,-4,-1,8,1,-1,9,-7,2,2,7,-6,-3,-3,10,4,8,4,2,-9,3,5,-1,-10,2,-3,-7,8,-3,-10,6,2,2,7,9,9,3,5,-6,-1,6,-9,-10,2,-9,-8,-6,1,8,4,-4,-9,-8,-3,9,5,5,-8,-3,2,-3,-7,3,-9,-7,-8,5,-8,-2,-9,4,-6,-8,-5,5,2,-8,-6,-10,1,7,8,7,-9,8,9,2,10,10,-10,3,-4,1,-1,7,8,-1,10,-4,-8,4,2,-5,-5,-10,-1,-7,7,4,-8,-1,-7,-5,-2,-3,-1,10,-5,8,1,5,4,-8,9,-8,-5,5,3,6,-1,8,7,5,-4,-10,-4,8,6,-8,7,1,-9,3,-10,-7,-7,-3,2,4,3,-10,10,5,-3,-8,3,4,10,3,-4,1,7,6,1,7,6,3,5,-10,2,-3,-1,-6,2,-1,10,-10,5,8,7,-2,-3,9,-2,8,-10,1,-8,2,-6,6,4,-5,-1,-5,-6,-1,1,-7,-10,-6,-8,10,2,5,5,-6,-7,-8,-3,7,1,10,-10,2,4,8,5,-9,2,-6,3,-5,-4,1,9,1,-7,-3,-8,5,-5,5,3,-6,5,-9,6,1,1,9,1,2,-9,-3,10,-10,-2,-2,8,-7,9,-3,2,-5,7,4,4,-6,-9,-1,-8,3,-5,-5,4,-5,-10,8,-4,6,8,9,-4,-8,-3,-3,1,1,2,10,7,-8,6,8,10,-1,-4,4,-3,-2,-3,-7,10,4,-3,-5,-2,7,9,-7,-9,-9,9,10,6,-10,6,5,7,-7,2,3,7,3,7,-6,10,-1,9,-1,-5,3,-8,9,-6,8,-2,-3,10,6,-7,6,-10,-4,-10,5,6,9,6,1,-4,-1,7,5,1,-7,-6,4,1,6,-5,-9,8,-6,5,8,6,6,-5,-3,6,5,-4,-9,-8,-8,-5,3,2,10,7,-7,-7,-6,-7,7,10,5,-10,9,-9,-1,2,2,3,3,9,-3,-4,7,10,5,7,-2,-6,6,-7,-4,1,5,7,6,-10,2,-9,-7,4,-9,-4,7,3,5,-10,-1,4,-5,-5,-7,-1,9,8,9,10,1,10,-3,-1,2,-7,2,-10,2,-7,8,-8,10,-5,-5,6,8,-4,-8,9,-8,-3,-10,7,-6,-1,-4,5,2,-2,4,3,-5,-3,3,1,10,2,-6,-2,-5,9,3,-3,4,1,5,-2,-2,3,8,-9,-9,8,9,-10,-4,-6,-4,1,-6,8,8,-4,-6,8,-3,10,-7,9,-10,-2,9,1,-7,-3,-7,-6,2,5,-9,10,9,5,-10,-4,7,-7,2,-2,-2,-3,8,4,-9,8,2,-1,-9,9,-5,4,-8,10,8,-10,9,-9,-3,6,10,2,-3,-6,-1,6,9,8,10,9,10,-8,5,5,-8,3,-9,1,10,-6,4,7,-3,-1,4,9,-3,2,-2,-7,-10,-10,5,-10,-1,-6,-10,8,-9,-6,-1,7,-4,2,-6,8,-9,-4,4,-1,-2,-1,3,8,8,-5,1,-3,-10,2,-5,-1,-1,-3,9,-9,3,3,-7,8,-7,6,-4,2,5,-10,-4,-7,8,-7,3,9,-6,-2,3,10,-2,7,-9,-1,-3,-7,6,2,-1,2,-5,-10,1,-3,1,-6,4,-10,-2,-7,4,2,7,3,-2,-4,3,-7,-7,3,-8,2,2,-4,4,7,-7,-9,2,-2,6,9,-1,6,-1,-5,-7,10,10,-4,-7,-6,2,7,-7,6,7,3,-6,-4,-1,5,-8,7,-10,4,-4,2,-4,-9,9,4,-3,-4,9,7,10,8,-8,6,8,7,-8,9,7,-5,-5,4,8,-8,-9,7,-6,5,-1,-6,-1,-2,-2,-5,1,7,8,6,1,-5,9,-10,-8,-3,-8,-8,1,-9,3,4,-3,9,-4,9,9,8,7,-4,-4,2,5,-10,1,1,-1,-7,-8,6,-1,1,-9,9,8,-1,-4,4,-4,-8,-2,-9,4,7,-4,5,-8,-7,-7,2,-4,10,7,-7,-8,8,-2,5,4,-9,5,-4,-2,9,-7,-9,-6,-9,4,-6,9,-4,-10,6,-1,2,10,-8,-7,6,-1,-5,3,-2,7,1,1,-6,4,-6,-8,-2,4,-5,-8,5,7,8,3,8,9,8,5,-2,-8,4,9,-6,-8,4,-3,7,10,-9,5,-4,7,4,-4,8,7,7,10,8,8,5,-2,1,-10,-4,-10], dtype = "uint16")#candidate|6220|(1320,)|const|uint16
call_6218 = relay.TupleGetItem(func_1819_call(relay.reshape(const_6219.astype('float64'), [448,]), relay.reshape(const_6220.astype('uint16'), [1320,]), ), 2)
call_6221 = relay.TupleGetItem(func_1822_call(relay.reshape(const_6219.astype('float64'), [448,]), relay.reshape(const_6220.astype('uint16'), [1320,]), ), 2)
func_4341_call = mod.get_global_var('func_4341')
func_4342_call = mutated_mod.get_global_var('func_4342')
call_6248 = relay.TupleGetItem(func_4341_call(), 0)
call_6249 = relay.TupleGetItem(func_4342_call(), 0)
func_4842_call = mod.get_global_var('func_4842')
func_4843_call = mutated_mod.get_global_var('func_4843')
call_6254 = func_4842_call()
call_6255 = func_4842_call()
output = relay.Tuple([call_6215,call_6218,const_6219,const_6220,call_6248,call_6254,])
output2 = relay.Tuple([call_6216,call_6221,const_6219,const_6220,call_6249,call_6255,])
func_6263 = relay.Function([], output)
mod['func_6263'] = func_6263
mod = relay.transform.InferType()(mod)
mutated_mod['func_6263'] = func_6263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6263_call = mutated_mod.get_global_var('func_6263')
call_6264 = func_6263_call()
output = call_6264
func_6265 = relay.Function([], output)
mutated_mod['func_6265'] = func_6265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4059_call = mod.get_global_var('func_4059')
func_4061_call = mutated_mod.get_global_var('func_4061')
call_6273 = relay.TupleGetItem(func_4059_call(), 0)
call_6274 = relay.TupleGetItem(func_4061_call(), 0)
output = relay.Tuple([call_6273,])
output2 = relay.Tuple([call_6274,])
func_6275 = relay.Function([], output)
mod['func_6275'] = func_6275
mod = relay.transform.InferType()(mod)
mutated_mod['func_6275'] = func_6275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6275_call = mutated_mod.get_global_var('func_6275')
call_6276 = func_6275_call()
output = call_6276
func_6277 = relay.Function([], output)
mutated_mod['func_6277'] = func_6277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2957_call = mod.get_global_var('func_2957')
func_2959_call = mutated_mod.get_global_var('func_2959')
call_6325 = func_2957_call()
call_6326 = func_2957_call()
var_6342 = relay.var("var_6342", dtype = "float32", shape = (11, 11, 10))#candidate|6342|(11, 11, 10)|var|float32
bop_6343 = relay.bitwise_or(call_6325.astype('int32'), var_6342.astype('int32')) # shape=(11, 11, 10)
bop_6346 = relay.bitwise_or(call_6326.astype('int32'), var_6342.astype('int32')) # shape=(11, 11, 10)
output = bop_6343
output2 = bop_6346
func_6350 = relay.Function([var_6342,], output)
mod['func_6350'] = func_6350
mod = relay.transform.InferType()(mod)
var_6351 = relay.var("var_6351", dtype = "float32", shape = (11, 11, 10))#candidate|6351|(11, 11, 10)|var|float32
output = func_6350(var_6351)
func_6352 = relay.Function([var_6351], output)
mutated_mod['func_6352'] = func_6352
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4287_call = mod.get_global_var('func_4287')
func_4288_call = mutated_mod.get_global_var('func_4288')
call_6376 = func_4287_call()
call_6377 = func_4287_call()
output = call_6376
output2 = call_6377
func_6378 = relay.Function([], output)
mod['func_6378'] = func_6378
mod = relay.transform.InferType()(mod)
output = func_6378()
func_6379 = relay.Function([], output)
mutated_mod['func_6379'] = func_6379
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6402 = relay.var("var_6402", dtype = "float32", shape = (4, 11, 3))#candidate|6402|(4, 11, 3)|var|float32
var_6403 = relay.var("var_6403", dtype = "float32", shape = (4, 11, 3))#candidate|6403|(4, 11, 3)|var|float32
bop_6404 = relay.power(var_6402.astype('float32'), relay.reshape(var_6403.astype('float32'), relay.shape_of(var_6402))) # shape=(4, 11, 3)
output = relay.Tuple([bop_6404,])
output2 = relay.Tuple([bop_6404,])
func_6408 = relay.Function([var_6402,var_6403,], output)
mod['func_6408'] = func_6408
mod = relay.transform.InferType()(mod)
mutated_mod['func_6408'] = func_6408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6408_call = mutated_mod.get_global_var('func_6408')
var_6410 = relay.var("var_6410", dtype = "float32", shape = (4, 11, 3))#candidate|6410|(4, 11, 3)|var|float32
var_6411 = relay.var("var_6411", dtype = "float32", shape = (4, 11, 3))#candidate|6411|(4, 11, 3)|var|float32
call_6409 = func_6408_call(var_6410,var_6411,)
output = call_6409
func_6412 = relay.Function([var_6410,var_6411,], output)
mutated_mod['func_6412'] = func_6412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6275_call = mod.get_global_var('func_6275')
func_6277_call = mutated_mod.get_global_var('func_6277')
call_6426 = relay.TupleGetItem(func_6275_call(), 0)
call_6427 = relay.TupleGetItem(func_6277_call(), 0)
func_5562_call = mod.get_global_var('func_5562')
func_5564_call = mutated_mod.get_global_var('func_5564')
call_6441 = relay.TupleGetItem(func_5562_call(), 4)
call_6442 = relay.TupleGetItem(func_5564_call(), 4)
func_1739_call = mod.get_global_var('func_1739')
func_1740_call = mutated_mod.get_global_var('func_1740')
call_6448 = func_1739_call()
call_6449 = func_1739_call()
bop_6451 = relay.mod(call_6441.astype('float32'), call_6448.astype('float32')) # shape=(2, 11, 10)
bop_6454 = relay.mod(call_6442.astype('float32'), call_6449.astype('float32')) # shape=(2, 11, 10)
output = relay.Tuple([call_6426,bop_6451,])
output2 = relay.Tuple([call_6427,bop_6454,])
func_6460 = relay.Function([], output)
mod['func_6460'] = func_6460
mod = relay.transform.InferType()(mod)
output = func_6460()
func_6461 = relay.Function([], output)
mutated_mod['func_6461'] = func_6461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5290_call = mod.get_global_var('func_5290')
func_5292_call = mutated_mod.get_global_var('func_5292')
call_6482 = relay.TupleGetItem(func_5290_call(), 0)
call_6483 = relay.TupleGetItem(func_5292_call(), 0)
func_4287_call = mod.get_global_var('func_4287')
func_4288_call = mutated_mod.get_global_var('func_4288')
call_6488 = func_4287_call()
call_6489 = func_4287_call()
output = relay.Tuple([call_6482,call_6488,])
output2 = relay.Tuple([call_6483,call_6489,])
func_6492 = relay.Function([], output)
mod['func_6492'] = func_6492
mod = relay.transform.InferType()(mod)
output = func_6492()
func_6493 = relay.Function([], output)
mutated_mod['func_6493'] = func_6493
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6536 = relay.var("var_6536", dtype = "float64", shape = (9, 8, 8))#candidate|6536|(9, 8, 8)|var|float64
uop_6537 = relay.erf(var_6536.astype('float64')) # shape=(9, 8, 8)
output = uop_6537
output2 = uop_6537
func_6546 = relay.Function([var_6536,], output)
mod['func_6546'] = func_6546
mod = relay.transform.InferType()(mod)
mutated_mod['func_6546'] = func_6546
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6547 = relay.var("var_6547", dtype = "float64", shape = (9, 8, 8))#candidate|6547|(9, 8, 8)|var|float64
func_6546_call = mutated_mod.get_global_var('func_6546')
call_6548 = func_6546_call(var_6547)
output = call_6548
func_6549 = relay.Function([var_6547], output)
mutated_mod['func_6549'] = func_6549
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6560 = relay.var("var_6560", dtype = "uint64", shape = (11, 15, 11))#candidate|6560|(11, 15, 11)|var|uint64
var_6561 = relay.var("var_6561", dtype = "uint64", shape = (11, 15, 11))#candidate|6561|(11, 15, 11)|var|uint64
bop_6562 = relay.less_equal(var_6560.astype('bool'), relay.reshape(var_6561.astype('bool'), relay.shape_of(var_6560))) # shape=(11, 15, 11)
func_620_call = mod.get_global_var('func_620')
func_622_call = mutated_mod.get_global_var('func_622')
call_6577 = relay.TupleGetItem(func_620_call(), 1)
call_6578 = relay.TupleGetItem(func_622_call(), 1)
func_4287_call = mod.get_global_var('func_4287')
func_4288_call = mutated_mod.get_global_var('func_4288')
call_6580 = func_4287_call()
call_6581 = func_4287_call()
output = relay.Tuple([bop_6562,call_6577,call_6580,])
output2 = relay.Tuple([bop_6562,call_6578,call_6581,])
func_6583 = relay.Function([var_6560,var_6561,], output)
mod['func_6583'] = func_6583
mod = relay.transform.InferType()(mod)
var_6584 = relay.var("var_6584", dtype = "uint64", shape = (11, 15, 11))#candidate|6584|(11, 15, 11)|var|uint64
var_6585 = relay.var("var_6585", dtype = "uint64", shape = (11, 15, 11))#candidate|6585|(11, 15, 11)|var|uint64
output = func_6583(var_6584,var_6585,)
func_6586 = relay.Function([var_6584,var_6585,], output)
mutated_mod['func_6586'] = func_6586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1350_call = mod.get_global_var('func_1350')
func_1351_call = mutated_mod.get_global_var('func_1351')
call_6658 = relay.TupleGetItem(func_1350_call(), 1)
call_6659 = relay.TupleGetItem(func_1351_call(), 1)
func_6460_call = mod.get_global_var('func_6460')
func_6461_call = mutated_mod.get_global_var('func_6461')
call_6668 = relay.TupleGetItem(func_6460_call(), 0)
call_6669 = relay.TupleGetItem(func_6461_call(), 0)
output = relay.Tuple([call_6658,call_6668,])
output2 = relay.Tuple([call_6659,call_6669,])
func_6684 = relay.Function([], output)
mod['func_6684'] = func_6684
mod = relay.transform.InferType()(mod)
output = func_6684()
func_6685 = relay.Function([], output)
mutated_mod['func_6685'] = func_6685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3531_call = mod.get_global_var('func_3531')
func_3532_call = mutated_mod.get_global_var('func_3532')
call_6709 = relay.TupleGetItem(func_3531_call(), 0)
call_6710 = relay.TupleGetItem(func_3532_call(), 0)
output = relay.Tuple([call_6709,])
output2 = relay.Tuple([call_6710,])
func_6715 = relay.Function([], output)
mod['func_6715'] = func_6715
mod = relay.transform.InferType()(mod)
output = func_6715()
func_6716 = relay.Function([], output)
mutated_mod['func_6716'] = func_6716
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4196_call = mod.get_global_var('func_4196')
func_4198_call = mutated_mod.get_global_var('func_4198')
call_6741 = relay.TupleGetItem(func_4196_call(), 1)
call_6742 = relay.TupleGetItem(func_4198_call(), 1)
var_6746 = relay.var("var_6746", dtype = "bool", shape = (12, 11, 10))#candidate|6746|(12, 11, 10)|var|bool
bop_6747 = relay.floor_mod(call_6741.astype('float32'), var_6746.astype('float32')) # shape=(12, 11, 10)
bop_6750 = relay.floor_mod(call_6742.astype('float32'), var_6746.astype('float32')) # shape=(12, 11, 10)
func_4842_call = mod.get_global_var('func_4842')
func_4843_call = mutated_mod.get_global_var('func_4843')
call_6758 = func_4842_call()
call_6759 = func_4842_call()
var_6764 = relay.var("var_6764", dtype = "float32", shape = (12, 11, 10))#candidate|6764|(12, 11, 10)|var|float32
bop_6765 = relay.bitwise_xor(call_6758.astype('uint16'), var_6764.astype('uint16')) # shape=(12, 11, 10)
bop_6768 = relay.bitwise_xor(call_6759.astype('uint16'), var_6764.astype('uint16')) # shape=(12, 11, 10)
output = relay.Tuple([bop_6747,bop_6765,])
output2 = relay.Tuple([bop_6750,bop_6768,])
func_6778 = relay.Function([var_6746,var_6764,], output)
mod['func_6778'] = func_6778
mod = relay.transform.InferType()(mod)
var_6779 = relay.var("var_6779", dtype = "bool", shape = (12, 11, 10))#candidate|6779|(12, 11, 10)|var|bool
var_6780 = relay.var("var_6780", dtype = "float32", shape = (12, 11, 10))#candidate|6780|(12, 11, 10)|var|float32
output = func_6778(var_6779,var_6780,)
func_6781 = relay.Function([var_6779,var_6780,], output)
mutated_mod['func_6781'] = func_6781
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6813 = relay.var("var_6813", dtype = "uint32", shape = ())#candidate|6813|()|var|uint32
const_6814 = relay.const([[[9,5,2,8,6,1,-6,-5],[9,9,-5,-8,10,-7,-5,8],[4,-4,5,4,-1,-5,5,1],[-1,-3,3,7,-5,10,1,4],[1,-4,3,-8,-3,9,-2,4],[-3,2,-10,1,-5,-7,-9,2]],[[2,6,3,8,-6,-4,9,4],[8,-10,-4,6,-4,-8,6,2],[-5,1,-2,-4,8,-9,-9,-9],[-6,5,-3,-1,-4,9,8,-5],[-10,3,-7,-2,-8,-2,-3,-1],[-1,1,7,-1,3,-10,3,-6]],[[-4,-7,-9,-8,2,-3,2,-4],[-10,6,-8,-8,-9,4,6,7],[10,-4,4,5,1,-1,-1,5],[1,-1,-10,-10,9,-3,3,-8],[-5,-3,4,5,7,10,10,-3],[9,-9,-7,10,-4,-3,-2,-1]],[[1,7,5,3,-7,-4,-10,-9],[-3,10,1,5,4,4,9,4],[-1,-7,3,10,5,-1,3,4],[2,5,5,-9,-8,-6,8,10],[2,-8,9,7,4,-9,-9,2],[-8,-5,6,5,-6,-4,-2,8]],[[2,-9,5,-7,5,7,-10,7],[5,4,-5,7,9,-10,6,4],[-3,10,-2,-1,4,3,9,5],[-2,-5,-7,10,6,6,-7,9],[-7,2,-6,8,-10,-4,-1,-3],[8,-1,2,1,-9,-9,9,-8]],[[5,-6,2,-10,7,1,5,-2],[-4,7,2,6,-5,10,1,10],[8,8,2,-4,4,-6,1,-1],[8,-3,-6,-4,3,4,-3,-1],[-4,5,-7,-4,4,9,7,10],[-7,-10,1,-3,9,8,4,7]]], dtype = "uint32")#candidate|6814|(6, 6, 8)|const|uint32
bop_6815 = relay.right_shift(var_6813.astype('uint32'), const_6814.astype('uint32')) # shape=(6, 6, 8)
output = bop_6815
output2 = bop_6815
F = relay.Function([var_6813,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_6813,], output2)
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
