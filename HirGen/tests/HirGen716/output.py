import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_31 = relay.var("var_31", dtype = "float64", shape = (11, 6, 5))#candidate|31|(11, 6, 5)|var|float64
uop_32 = relay.tan(var_31.astype('float64')) # shape=(11, 6, 5)
output = relay.Tuple([uop_32,])
output2 = relay.Tuple([uop_32,])
func_42 = relay.Function([var_31,], output)
mod['func_42'] = func_42
mod = relay.transform.InferType()(mod)
mutated_mod['func_42'] = func_42
mutated_mod = relay.transform.InferType()(mutated_mod)
var_43 = relay.var("var_43", dtype = "float64", shape = (11, 6, 5))#candidate|43|(11, 6, 5)|var|float64
func_42_call = mutated_mod.get_global_var('func_42')
call_44 = func_42_call(var_43)
output = call_44
func_45 = relay.Function([var_43], output)
mutated_mod['func_45'] = func_45
mutated_mod = relay.transform.InferType()(mutated_mod)
var_94 = relay.var("var_94", dtype = "float32", shape = (12, 11, 5))#candidate|94|(12, 11, 5)|var|float32
uop_95 = relay.sinh(var_94.astype('float32')) # shape=(12, 11, 5)
bop_99 = relay.equal(uop_95.astype('bool'), relay.reshape(var_94.astype('bool'), relay.shape_of(uop_95))) # shape=(12, 11, 5)
output = relay.Tuple([bop_99,])
output2 = relay.Tuple([bop_99,])
func_102 = relay.Function([var_94,], output)
mod['func_102'] = func_102
mod = relay.transform.InferType()(mod)
mutated_mod['func_102'] = func_102
mutated_mod = relay.transform.InferType()(mutated_mod)
var_103 = relay.var("var_103", dtype = "float32", shape = (12, 11, 5))#candidate|103|(12, 11, 5)|var|float32
func_102_call = mutated_mod.get_global_var('func_102')
call_104 = func_102_call(var_103)
output = call_104
func_105 = relay.Function([var_103], output)
mutated_mod['func_105'] = func_105
mutated_mod = relay.transform.InferType()(mutated_mod)
var_232 = relay.var("var_232", dtype = "int32", shape = (14, 12, 2))#candidate|232|(14, 12, 2)|var|int32
var_233 = relay.var("var_233", dtype = "int32", shape = (14, 12, 2))#candidate|233|(14, 12, 2)|var|int32
bop_234 = relay.not_equal(var_232.astype('bool'), relay.reshape(var_233.astype('bool'), relay.shape_of(var_232))) # shape=(14, 12, 2)
output = relay.Tuple([bop_234,])
output2 = relay.Tuple([bop_234,])
func_237 = relay.Function([var_232,var_233,], output)
mod['func_237'] = func_237
mod = relay.transform.InferType()(mod)
var_238 = relay.var("var_238", dtype = "int32", shape = (14, 12, 2))#candidate|238|(14, 12, 2)|var|int32
var_239 = relay.var("var_239", dtype = "int32", shape = (14, 12, 2))#candidate|239|(14, 12, 2)|var|int32
output = func_237(var_238,var_239,)
func_240 = relay.Function([var_238,var_239,], output)
mutated_mod['func_240'] = func_240
mutated_mod = relay.transform.InferType()(mutated_mod)
const_440 = relay.const([[[-3.293031,3.755997],[-9.856779,1.386006],[9.688385,3.154392],[-1.011971,4.039769],[-6.203159,9.182282],[3.290794,0.627967],[3.820713,-5.122565],[4.011038,-1.372198],[8.983791,-7.796336],[5.147214,-6.321930],[3.190243,-5.459681],[9.813481,8.364426]]], dtype = "float64")#candidate|440|(1, 12, 2)|const|float64
uop_441 = relay.asin(const_440.astype('float64')) # shape=(1, 12, 2)
output = relay.Tuple([uop_441,])
output2 = relay.Tuple([uop_441,])
func_444 = relay.Function([], output)
mod['func_444'] = func_444
mod = relay.transform.InferType()(mod)
mutated_mod['func_444'] = func_444
mutated_mod = relay.transform.InferType()(mutated_mod)
func_444_call = mutated_mod.get_global_var('func_444')
call_445 = func_444_call()
output = call_445
func_446 = relay.Function([], output)
mutated_mod['func_446'] = func_446
mutated_mod = relay.transform.InferType()(mutated_mod)
var_468 = relay.var("var_468", dtype = "float64", shape = (4, 13, 3))#candidate|468|(4, 13, 3)|var|float64
uop_469 = relay.log(var_468.astype('float64')) # shape=(4, 13, 3)
output = relay.Tuple([uop_469,])
output2 = relay.Tuple([uop_469,])
func_472 = relay.Function([var_468,], output)
mod['func_472'] = func_472
mod = relay.transform.InferType()(mod)
mutated_mod['func_472'] = func_472
mutated_mod = relay.transform.InferType()(mutated_mod)
var_473 = relay.var("var_473", dtype = "float64", shape = (4, 13, 3))#candidate|473|(4, 13, 3)|var|float64
func_472_call = mutated_mod.get_global_var('func_472')
call_474 = func_472_call(var_473)
output = call_474
func_475 = relay.Function([var_473], output)
mutated_mod['func_475'] = func_475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_444_call = mod.get_global_var('func_444')
func_446_call = mutated_mod.get_global_var('func_446')
call_513 = relay.TupleGetItem(func_444_call(), 0)
call_514 = relay.TupleGetItem(func_446_call(), 0)
output = call_513
output2 = call_514
func_517 = relay.Function([], output)
mod['func_517'] = func_517
mod = relay.transform.InferType()(mod)
output = func_517()
func_518 = relay.Function([], output)
mutated_mod['func_518'] = func_518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_444_call = mod.get_global_var('func_444')
func_446_call = mutated_mod.get_global_var('func_446')
call_546 = relay.TupleGetItem(func_444_call(), 0)
call_547 = relay.TupleGetItem(func_446_call(), 0)
func_517_call = mod.get_global_var('func_517')
func_518_call = mutated_mod.get_global_var('func_518')
call_554 = func_517_call()
call_555 = func_517_call()
output = relay.Tuple([call_546,call_554,])
output2 = relay.Tuple([call_547,call_555,])
func_585 = relay.Function([], output)
mod['func_585'] = func_585
mod = relay.transform.InferType()(mod)
output = func_585()
func_586 = relay.Function([], output)
mutated_mod['func_586'] = func_586
mutated_mod = relay.transform.InferType()(mutated_mod)
var_712 = relay.var("var_712", dtype = "int8", shape = (9, 10, 16))#candidate|712|(9, 10, 16)|var|int8
var_713 = relay.var("var_713", dtype = "int8", shape = (9, 10, 16))#candidate|713|(9, 10, 16)|var|int8
bop_714 = relay.right_shift(var_712.astype('int8'), relay.reshape(var_713.astype('int8'), relay.shape_of(var_712))) # shape=(9, 10, 16)
func_444_call = mod.get_global_var('func_444')
func_446_call = mutated_mod.get_global_var('func_446')
call_720 = relay.TupleGetItem(func_444_call(), 0)
call_721 = relay.TupleGetItem(func_446_call(), 0)
output = relay.Tuple([bop_714,call_720,])
output2 = relay.Tuple([bop_714,call_721,])
func_729 = relay.Function([var_712,var_713,], output)
mod['func_729'] = func_729
mod = relay.transform.InferType()(mod)
var_730 = relay.var("var_730", dtype = "int8", shape = (9, 10, 16))#candidate|730|(9, 10, 16)|var|int8
var_731 = relay.var("var_731", dtype = "int8", shape = (9, 10, 16))#candidate|731|(9, 10, 16)|var|int8
output = func_729(var_730,var_731,)
func_732 = relay.Function([var_730,var_731,], output)
mutated_mod['func_732'] = func_732
mutated_mod = relay.transform.InferType()(mutated_mod)
func_517_call = mod.get_global_var('func_517')
func_518_call = mutated_mod.get_global_var('func_518')
call_739 = func_517_call()
call_740 = func_517_call()
output = relay.Tuple([call_739,])
output2 = relay.Tuple([call_740,])
func_741 = relay.Function([], output)
mod['func_741'] = func_741
mod = relay.transform.InferType()(mod)
output = func_741()
func_742 = relay.Function([], output)
mutated_mod['func_742'] = func_742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_741_call = mod.get_global_var('func_741')
func_742_call = mutated_mod.get_global_var('func_742')
call_774 = relay.TupleGetItem(func_741_call(), 0)
call_775 = relay.TupleGetItem(func_742_call(), 0)
var_803 = relay.var("var_803", dtype = "float64", shape = (3, 12, 2))#candidate|803|(3, 12, 2)|var|float64
bop_804 = relay.floor_mod(call_774.astype('float32'), var_803.astype('float32')) # shape=(3, 12, 2)
bop_807 = relay.floor_mod(call_775.astype('float32'), var_803.astype('float32')) # shape=(3, 12, 2)
output = relay.Tuple([bop_804,])
output2 = relay.Tuple([bop_807,])
func_810 = relay.Function([var_803,], output)
mod['func_810'] = func_810
mod = relay.transform.InferType()(mod)
mutated_mod['func_810'] = func_810
mutated_mod = relay.transform.InferType()(mutated_mod)
var_811 = relay.var("var_811", dtype = "float64", shape = (3, 12, 2))#candidate|811|(3, 12, 2)|var|float64
func_810_call = mutated_mod.get_global_var('func_810')
call_812 = func_810_call(var_811)
output = call_812
func_813 = relay.Function([var_811], output)
mutated_mod['func_813'] = func_813
mutated_mod = relay.transform.InferType()(mutated_mod)
var_827 = relay.var("var_827", dtype = "float32", shape = (13, 8, 3))#candidate|827|(13, 8, 3)|var|float32
uop_828 = relay.cosh(var_827.astype('float32')) # shape=(13, 8, 3)
func_237_call = mod.get_global_var('func_237')
func_240_call = mutated_mod.get_global_var('func_240')
const_839 = relay.const([-8,4,8,-3,-7,-1,-9,-2,2,4,5,-9,2,-7,3,4,4,5,-3,-4,5,1,-8,1,-8,-9,9,-9,3,-5,-7,-8,-4,3,-3,-8,-6,-6,-1,-6,2,-1,3,-9,5,3,-2,4,-5,-3,-6,9,-9,6,-2,10,-8,-2,-2,-9,6,10,-4,3,-3,-8,-7,-3,-1,-8,-3,-6,1,6,-2,2,-7,-5,-9,10,5,3,2,8,-6,8,-7,2,4,-3,3,4,6,-2,-6,-8,-8,-2,-8,-6,9,6,10,-3,-6,-1,-10,10,4,2,4,-2,-1,-5,-7,3,-4,-9,7,-9,8,3,-6,-5,-6,-4,-9,3,1,8,6,1,10,-4,-3,1,4,-1,-8,-5,-7,3,3,5,1,-3,5,-8,-5,-4,-7,2,-1,-4,-1,-3,5,-4,3,6,3,2,-3,-4,5,9,-5,3,-5,-6,7,-7,-7,-3,-10,-6,-8,8,-1,10,-2,-7,-9,2,-9,-10,-10,-1,8,7,2,-9,-2,-2,1,8,-2,-10,-7,-4,-3,-5,3,-9,-9,-7,2,1,-4,8,6,1,-2,8,-3,6,-9,8,8,-1,6,7,-7,-3,-3,8,-8,5,10,-9,-6,-9,-7,-6,-4,1,-8,-9,7,6,2,9,-3,-10,-10,3,4,-2,1,-6,-7,-5,5,8,6,4,-5,10,9,-10,6,4,7,3,-4,-3,7,-3,-1,-8,4,7,-5,9,4,1,-3,4,-3,-6,-9,7,6,-10,-3,-6,-10,-8,9,-7,5,4,4,-7,-6,-3,3,-1,-2,-10,1,5,10,-4,-1,1,-10,-5,7,-1,-9,8,-6,5,-1,-6,10,4,3,8,-1,-3,7,7,-1,7,-5,-4,-3,1,-1,-6,6,-2,8,-6], dtype = "int32")#candidate|839|(336,)|const|int32
call_838 = relay.TupleGetItem(func_237_call(relay.reshape(const_839.astype('int32'), [14, 12, 2]), relay.reshape(const_839.astype('int32'), [14, 12, 2]), ), 0)
call_840 = relay.TupleGetItem(func_240_call(relay.reshape(const_839.astype('int32'), [14, 12, 2]), relay.reshape(const_839.astype('int32'), [14, 12, 2]), ), 0)
func_102_call = mod.get_global_var('func_102')
func_105_call = mutated_mod.get_global_var('func_105')
const_879 = relay.const([8.412619,-7.259340,6.514041,-7.965405,-0.220193,7.588779,4.151675,8.148237,-8.667979,-9.442008,-6.917331,9.468594,-1.164590,-5.564627,3.645651,-0.391451,-3.101063,-2.354442,5.361442,-0.441427,4.784534,-4.010374,5.522501,8.035164,-4.353348,6.642848,8.288669,9.183871,-1.889973,-4.238908,7.565860,-6.970201,0.020690,7.720721,3.747007,-3.311991,-2.728968,-1.887801,-7.102665,7.139017,4.030151,6.853540,1.538826,-3.667161,-3.820838,6.100411,9.263268,-0.275328,-6.192936,-8.763751,5.120930,0.638965,0.050450,-1.466832,4.546785,-8.234204,-6.209257,9.419509,-9.866127,5.067726,-4.287631,-0.136973,8.140339,-4.541670,3.291974,7.725862,7.448696,-2.894150,-5.963474,-9.421801,-1.156329,-3.613237,-2.988445,6.344618,-2.384005,-3.685478,6.811387,-3.384382,2.751017,9.815260,3.719792,8.809384,4.552756,1.668476,-2.077184,5.116219,-2.912168,-6.476277,7.328435,2.064661,-9.501048,3.061365,7.942084,-6.282176,-9.466774,4.376374,5.828732,0.721277,-2.731437,-8.583283,-3.552433,7.351318,-8.531444,-0.440764,6.109755,7.735037,2.987058,-7.420876,-8.886693,2.388328,-7.530113,5.047268,0.946110,-9.879873,0.585077,4.449534,-8.332088,2.863027,-4.135345,-0.434484,0.152601,5.695421,-3.654670,7.658545,5.358914,-7.157517,6.140618,4.356422,-2.681797,-2.329972,-7.220464,1.047652,5.654003,4.997393,-4.369266,3.086559,5.986041,-5.653764,-5.492885,4.952730,-3.169540,8.204973,4.445311,0.285999,-2.292638,7.755355,2.558814,8.774719,1.791859,-5.311785,8.856979,-9.282954,-1.315607,-0.849223,-5.996352,-8.962571,2.767938,9.552718,-1.174268,-2.360240,-5.332776,-4.805491,2.656097,-0.853083,-5.861148,-2.819760,9.575922,6.334891,-8.741837,-5.041844,6.876883,7.091240,7.218666,1.686886,1.098530,-6.596635,4.435580,2.314869,8.581947,-9.235368,-1.954067,9.261262,1.067712,-5.161481,-8.421847,-6.182627,0.372859,0.392742,-1.518178,8.644702,-0.265923,-1.190915,-4.403961,-8.214965,8.177113,4.723685,-8.766384,7.529630,0.863839,2.428394,8.057310,5.339355,1.558677,1.617205,5.662253,-0.580635,-7.558699,-0.002475,-9.850068,-8.646389,8.350637,-1.186352,-4.529635,2.545385,2.914755,-6.154019,-8.869068,3.593413,-9.855853,-6.436105,9.696456,0.810006,7.844985,-2.530104,2.623650,4.104765,8.082595,-2.505783,-5.914208,1.675244,-6.147138,-6.955171,-3.527828,-9.951011,-4.412447,-2.692731,5.887413,3.409313,8.476840,1.849287,3.611317,3.710671,-6.902488,-5.570563,7.375615,-7.863417,0.267601,6.077598,-3.451839,-3.546114,-6.380400,2.274813,7.537477,-8.806643,-0.861619,0.332485,-3.566823,-8.703732,-7.629158,4.451865,2.768311,9.117427,-9.529138,-1.740493,-7.298891,6.243197,2.251177,2.406925,-8.397816,-7.379409,6.517955,-8.541454,-2.803250,-1.486849,1.580129,3.875425,4.689356,-3.929138,6.742629,-2.230730,3.191784,-1.276930,-9.852809,0.991014,6.379978,-5.725839,1.122366,-6.045013,6.161480,-4.800001,0.286522,2.931595,-1.932949,-9.418392,-9.744693,-0.605984,0.803632,5.093559,-1.655018,-6.304637,-6.541181,-9.128871,1.148514,3.936385,3.931150,0.552031,7.901760,5.513938,-3.574463,3.708282,-4.433943,2.085708,-8.596868,-9.245836,2.545157,-0.195488,2.922996,-8.273516,-4.122804,6.966480,3.074544,-0.802287,-6.467497,2.980649,5.580910,6.078987,-1.842359,1.735816,7.799844,3.276232,-6.246229,-3.780747,-6.190287,-6.795179,6.574186,-5.374629,1.099007,0.180131,-1.270812,-0.730925,-6.940963,1.971882,-3.424357,1.460261,-2.272467,0.246995,0.410548,-3.190491,-6.682230,-7.267166,5.135902,-3.460182,1.314558,-7.067561,-9.354725,8.703170,-1.130419,1.138184,-1.156915,9.222444,1.655682,2.644259,-6.724887,-9.742435,0.022124,-5.807630,2.708025,4.116027,0.031795,-1.138271,-9.856531,-4.374557,2.946792,-5.914752,-5.722567,-7.903421,-8.249342,-6.733088,-0.961704,2.111999,7.649680,-0.008640,-4.956090,2.052601,0.484790,-1.953871,-9.598362,-5.784083,-9.592817,2.735937,-0.113535,0.521270,2.140800,-7.580590,-9.049993,3.988184,1.099824,8.827515,9.130258,3.046448,-2.508545,1.266224,-5.200035,-3.549750,-8.395227,-8.085020,-8.273612,1.081019,4.759442,0.431136,9.001524,-3.556680,-6.844470,-8.672801,-6.250165,-2.776499,1.504276,6.546764,1.319307,0.516507,2.465619,1.546147,1.556152,-5.690773,-9.762885,-2.666486,-3.298924,-8.212237,-2.378303,0.399236,0.818773,-2.695331,1.252609,-7.872118,1.872716,-2.573998,8.360071,-0.550529,-7.438086,-4.814547,-8.562891,-3.790169,7.240248,7.094254,9.898778,-5.695511,-6.665180,-9.024486,2.112403,8.701998,-8.715024,2.490412,8.427935,-5.219564,-9.205053,-2.138063,2.797349,-5.563317,8.024216,3.917779,-0.432321,3.691982,-4.241345,-7.742052,2.811928,-1.224360,1.515798,1.952810,-3.891129,-7.757283,-8.625055,3.041667,0.599896,-4.513323,-7.296738,4.127658,-7.178887,4.683335,-5.674045,-4.910371,0.998625,2.855398,-8.466516,6.404033,-9.111304,-8.662229,-5.684738,1.693510,6.476494,8.251662,9.451721,-0.987517,1.061437,-4.732945,1.852164,9.873477,8.339244,0.696691,-3.843088,-5.809639,-1.090569,5.047245,2.721021,-8.143441,6.422608,-5.418073,-1.706628,-6.894006,-4.326345,-8.867876,3.439922,0.748572,-0.893716,-4.373508,8.743433,-2.637577,5.210694,3.923825,-6.992035,2.400509,4.620446,-5.345724,-9.153936,6.982697,1.201518,-0.728983,-3.800076,3.411950,-1.197531,3.096826,2.187196,5.024307,8.786408,0.705770,-3.167625,1.463372,-5.328439,-3.194962,-1.124926,1.292324,8.020252,-2.026782,2.704012,-1.674004,-8.780284,-7.961158,2.076642,-8.268683,-0.799709,-5.382769,5.877846,-7.975328,1.712956,-7.218751,-7.681245,5.144351,-8.258454,3.581932,-9.860208,5.387864,3.861825,-0.094024,-2.354664,-4.927703,-4.281453,6.443266,-5.009598,2.194201,-4.785541,-2.314894,0.830052,-8.471272,6.170211,-0.544963,-2.002765,-4.268781,1.487384,-2.074594,-0.558595,-1.836523,-6.295258,-1.514723,9.652850,-5.813639,9.596152,-4.794375,5.453415,-9.484144,0.466649,-2.754114,9.377724,0.920123,0.272728,-5.287537,-8.254638,-6.209263,-1.476727,-7.243919,-4.696851,-5.447179,2.563896,-2.429220,2.178157,6.320394,3.811648,-3.694891,8.722048,9.554769,-1.747324,-3.628083,-4.060350,3.497325,9.429054,-3.555327,-9.019327,2.189033,-6.442096,-8.318195,0.541398,-1.760266,8.769697,1.450672,-8.215925,6.921347,-5.537010,-8.479482,-6.070110,9.298214,5.004321,0.588252,-6.340441,2.970957,2.979991,3.849032,9.027971,5.889621,-8.283751,0.088124,-2.560913,3.696415,-0.793624,3.246762,3.177964,-4.697593,7.922181,6.695292,5.998143,-4.413953,-6.982651,4.074995,8.147481,3.491324,5.615330,-1.736256,1.001109,-6.429274,2.220940,3.350302,-1.896088,4.482499], dtype = "float32")#candidate|879|(660,)|const|float32
call_878 = relay.TupleGetItem(func_102_call(relay.reshape(const_879.astype('float32'), [12, 11, 5])), 0)
call_880 = relay.TupleGetItem(func_105_call(relay.reshape(const_879.astype('float32'), [12, 11, 5])), 0)
output = relay.Tuple([uop_828,call_838,const_839,call_878,const_879,])
output2 = relay.Tuple([uop_828,call_840,const_839,call_880,const_879,])
func_884 = relay.Function([var_827,], output)
mod['func_884'] = func_884
mod = relay.transform.InferType()(mod)
var_885 = relay.var("var_885", dtype = "float32", shape = (13, 8, 3))#candidate|885|(13, 8, 3)|var|float32
output = func_884(var_885)
func_886 = relay.Function([var_885], output)
mutated_mod['func_886'] = func_886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_444_call = mod.get_global_var('func_444')
func_446_call = mutated_mod.get_global_var('func_446')
call_938 = relay.TupleGetItem(func_444_call(), 0)
call_939 = relay.TupleGetItem(func_446_call(), 0)
output = relay.Tuple([call_938,])
output2 = relay.Tuple([call_939,])
func_958 = relay.Function([], output)
mod['func_958'] = func_958
mod = relay.transform.InferType()(mod)
mutated_mod['func_958'] = func_958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_958_call = mutated_mod.get_global_var('func_958')
call_959 = func_958_call()
output = call_959
func_960 = relay.Function([], output)
mutated_mod['func_960'] = func_960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_517_call = mod.get_global_var('func_517')
func_518_call = mutated_mod.get_global_var('func_518')
call_1012 = func_517_call()
call_1013 = func_517_call()
func_958_call = mod.get_global_var('func_958')
func_960_call = mutated_mod.get_global_var('func_960')
call_1046 = relay.TupleGetItem(func_958_call(), 0)
call_1047 = relay.TupleGetItem(func_960_call(), 0)
bop_1050 = relay.right_shift(call_1046.astype('int8'), relay.reshape(call_1012.astype('int8'), relay.shape_of(call_1046))) # shape=(1, 12, 2)
bop_1053 = relay.right_shift(call_1047.astype('int8'), relay.reshape(call_1013.astype('int8'), relay.shape_of(call_1047))) # shape=(1, 12, 2)
uop_1056 = relay.atanh(call_1012.astype('float32')) # shape=(1, 12, 2)
uop_1058 = relay.atanh(call_1013.astype('float32')) # shape=(1, 12, 2)
output = relay.Tuple([bop_1050,uop_1056,])
output2 = relay.Tuple([bop_1053,uop_1058,])
func_1067 = relay.Function([], output)
mod['func_1067'] = func_1067
mod = relay.transform.InferType()(mod)
mutated_mod['func_1067'] = func_1067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1067_call = mutated_mod.get_global_var('func_1067')
call_1068 = func_1067_call()
output = call_1068
func_1069 = relay.Function([], output)
mutated_mod['func_1069'] = func_1069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_741_call = mod.get_global_var('func_741')
func_742_call = mutated_mod.get_global_var('func_742')
call_1109 = relay.TupleGetItem(func_741_call(), 0)
call_1110 = relay.TupleGetItem(func_742_call(), 0)
uop_1124 = relay.tan(call_1109.astype('float32')) # shape=(1, 12, 2)
uop_1126 = relay.tan(call_1110.astype('float32')) # shape=(1, 12, 2)
output = relay.Tuple([uop_1124,])
output2 = relay.Tuple([uop_1126,])
func_1127 = relay.Function([], output)
mod['func_1127'] = func_1127
mod = relay.transform.InferType()(mod)
mutated_mod['func_1127'] = func_1127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1127_call = mutated_mod.get_global_var('func_1127')
call_1128 = func_1127_call()
output = call_1128
func_1129 = relay.Function([], output)
mutated_mod['func_1129'] = func_1129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_585_call = mod.get_global_var('func_585')
func_586_call = mutated_mod.get_global_var('func_586')
call_1175 = relay.TupleGetItem(func_585_call(), 1)
call_1176 = relay.TupleGetItem(func_586_call(), 1)
output = relay.Tuple([call_1175,])
output2 = relay.Tuple([call_1176,])
func_1202 = relay.Function([], output)
mod['func_1202'] = func_1202
mod = relay.transform.InferType()(mod)
output = func_1202()
func_1203 = relay.Function([], output)
mutated_mod['func_1203'] = func_1203
mutated_mod = relay.transform.InferType()(mutated_mod)
func_741_call = mod.get_global_var('func_741')
func_742_call = mutated_mod.get_global_var('func_742')
call_1252 = relay.TupleGetItem(func_741_call(), 0)
call_1253 = relay.TupleGetItem(func_742_call(), 0)
uop_1276 = relay.sin(call_1252.astype('float64')) # shape=(1, 12, 2)
uop_1278 = relay.sin(call_1253.astype('float64')) # shape=(1, 12, 2)
output = uop_1276
output2 = uop_1278
func_1285 = relay.Function([], output)
mod['func_1285'] = func_1285
mod = relay.transform.InferType()(mod)
mutated_mod['func_1285'] = func_1285
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1285_call = mutated_mod.get_global_var('func_1285')
call_1286 = func_1285_call()
output = call_1286
func_1287 = relay.Function([], output)
mutated_mod['func_1287'] = func_1287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1127_call = mod.get_global_var('func_1127')
func_1129_call = mutated_mod.get_global_var('func_1129')
call_1306 = relay.TupleGetItem(func_1127_call(), 0)
call_1307 = relay.TupleGetItem(func_1129_call(), 0)
func_729_call = mod.get_global_var('func_729')
func_732_call = mutated_mod.get_global_var('func_732')
var_1309 = relay.var("var_1309", dtype = "int8", shape = (1440,))#candidate|1309|(1440,)|var|int8
call_1308 = relay.TupleGetItem(func_729_call(relay.reshape(var_1309.astype('int8'), [9, 10, 16]), relay.reshape(var_1309.astype('int8'), [9, 10, 16]), ), 0)
call_1310 = relay.TupleGetItem(func_732_call(relay.reshape(var_1309.astype('int8'), [9, 10, 16]), relay.reshape(var_1309.astype('int8'), [9, 10, 16]), ), 0)
output = relay.Tuple([call_1306,call_1308,var_1309,])
output2 = relay.Tuple([call_1307,call_1310,var_1309,])
func_1327 = relay.Function([var_1309,], output)
mod['func_1327'] = func_1327
mod = relay.transform.InferType()(mod)
var_1328 = relay.var("var_1328", dtype = "int8", shape = (1440,))#candidate|1328|(1440,)|var|int8
output = func_1327(var_1328)
func_1329 = relay.Function([var_1328], output)
mutated_mod['func_1329'] = func_1329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_741_call = mod.get_global_var('func_741')
func_742_call = mutated_mod.get_global_var('func_742')
call_1331 = relay.TupleGetItem(func_741_call(), 0)
call_1332 = relay.TupleGetItem(func_742_call(), 0)
func_237_call = mod.get_global_var('func_237')
func_240_call = mutated_mod.get_global_var('func_240')
const_1356 = relay.const([7,8,9,8,-6,5,-3,-10,-4,8,5,8,6,-1,7,-5,-10,-8,-8,2,-5,10,1,4,8,-7,-9,-6,2,10,-3,-4,10,1,2,-4,2,4,3,9,4,-2,-5,-10,6,-8,6,4,-6,8,10,-5,-5,6,-9,-9,2,-5,-2,6,4,-6,6,8,5,-9,7,7,-3,2,-7,4,-4,8,4,5,8,8,-1,7,4,3,2,-5,-1,8,10,7,8,2,-9,-10,10,2,-8,-9,7,-2,-2,-5,-4,10,2,9,-5,4,10,3,-3,9,-6,-4,10,1,2,4,-8,1,-6,-9,-1,-6,-8,9,6,5,-8,-6,-4,2,-4,4,-3,-9,5,-1,-3,-9,6,4,-8,5,-7,-6,-9,-9,-7,2,-9,-10,-10,-3,5,-6,2,4,-1,5,9,9,2,-10,2,-8,4,-5,6,-1,-2,4,9,3,9,5,1,-8,3,-1,-2,6,-6,2,1,-5,-10,-6,-8,-6,8,5,-9,-2,10,9,-4,-8,6,-2,-3,1,-7,4,-7,-10,-4,-4,-7,7,-2,9,-9,-6,-7,5,7,-5,4,-2,10,6,7,8,6,3,-10,-6,7,8,-10,6,-9,-6,2,2,7,7,7,2,-1,-3,-5,-1,-9,-8,2,-10,7,-1,-1,-1,2,6,3,3,3,4,3,10,-6,2,-4,-8,8,2,-6,-10,10,6,-4,-5,4,-2,-5,-8,-5,-9,-5,-2,8,-4,6,1,-10,7,-7,-8,2,-8,4,-7,8,-8,3,-10,3,-3,8,4,2,-9,-6,10,8,-6,-3,1,-9,8,10,-2,2,3,1,7,9,-2,4,2,9,-4,8,-4,8,-10,-10,3,-10,-1,4,-6,-5,-5,-10,10,-2,2], dtype = "int32")#candidate|1356|(336,)|const|int32
call_1355 = relay.TupleGetItem(func_237_call(relay.reshape(const_1356.astype('int32'), [14, 12, 2]), relay.reshape(const_1356.astype('int32'), [14, 12, 2]), ), 0)
call_1357 = relay.TupleGetItem(func_240_call(relay.reshape(const_1356.astype('int32'), [14, 12, 2]), relay.reshape(const_1356.astype('int32'), [14, 12, 2]), ), 0)
output = relay.Tuple([call_1331,call_1355,const_1356,])
output2 = relay.Tuple([call_1332,call_1357,const_1356,])
func_1360 = relay.Function([], output)
mod['func_1360'] = func_1360
mod = relay.transform.InferType()(mod)
output = func_1360()
func_1361 = relay.Function([], output)
mutated_mod['func_1361'] = func_1361
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1380 = relay.var("var_1380", dtype = "float64", shape = (10, 6, 7))#candidate|1380|(10, 6, 7)|var|float64
uop_1381 = relay.log10(var_1380.astype('float64')) # shape=(10, 6, 7)
output = relay.Tuple([uop_1381,])
output2 = relay.Tuple([uop_1381,])
func_1393 = relay.Function([var_1380,], output)
mod['func_1393'] = func_1393
mod = relay.transform.InferType()(mod)
mutated_mod['func_1393'] = func_1393
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1394 = relay.var("var_1394", dtype = "float64", shape = (10, 6, 7))#candidate|1394|(10, 6, 7)|var|float64
func_1393_call = mutated_mod.get_global_var('func_1393')
call_1395 = func_1393_call(var_1394)
output = call_1395
func_1396 = relay.Function([var_1394], output)
mutated_mod['func_1396'] = func_1396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1202_call = mod.get_global_var('func_1202')
func_1203_call = mutated_mod.get_global_var('func_1203')
call_1440 = relay.TupleGetItem(func_1202_call(), 0)
call_1441 = relay.TupleGetItem(func_1203_call(), 0)
uop_1450 = relay.acosh(call_1440.astype('float32')) # shape=(1, 12, 2)
uop_1452 = relay.acosh(call_1441.astype('float32')) # shape=(1, 12, 2)
bop_1458 = relay.less(call_1440.astype('bool'), relay.reshape(uop_1450.astype('bool'), relay.shape_of(call_1440))) # shape=(1, 12, 2)
bop_1461 = relay.less(call_1441.astype('bool'), relay.reshape(uop_1452.astype('bool'), relay.shape_of(call_1441))) # shape=(1, 12, 2)
output = bop_1458
output2 = bop_1461
func_1462 = relay.Function([], output)
mod['func_1462'] = func_1462
mod = relay.transform.InferType()(mod)
output = func_1462()
func_1463 = relay.Function([], output)
mutated_mod['func_1463'] = func_1463
mutated_mod = relay.transform.InferType()(mutated_mod)
func_585_call = mod.get_global_var('func_585')
func_586_call = mutated_mod.get_global_var('func_586')
call_1469 = relay.TupleGetItem(func_585_call(), 0)
call_1470 = relay.TupleGetItem(func_586_call(), 0)
output = call_1469
output2 = call_1470
func_1472 = relay.Function([], output)
mod['func_1472'] = func_1472
mod = relay.transform.InferType()(mod)
output = func_1472()
func_1473 = relay.Function([], output)
mutated_mod['func_1473'] = func_1473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1472_call = mod.get_global_var('func_1472')
func_1473_call = mutated_mod.get_global_var('func_1473')
call_1526 = func_1472_call()
call_1527 = func_1472_call()
output = relay.Tuple([call_1526,])
output2 = relay.Tuple([call_1527,])
func_1537 = relay.Function([], output)
mod['func_1537'] = func_1537
mod = relay.transform.InferType()(mod)
mutated_mod['func_1537'] = func_1537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1537_call = mutated_mod.get_global_var('func_1537')
call_1538 = func_1537_call()
output = call_1538
func_1539 = relay.Function([], output)
mutated_mod['func_1539'] = func_1539
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1472_call = mod.get_global_var('func_1472')
func_1473_call = mutated_mod.get_global_var('func_1473')
call_1564 = func_1472_call()
call_1565 = func_1472_call()
func_741_call = mod.get_global_var('func_741')
func_742_call = mutated_mod.get_global_var('func_742')
call_1589 = relay.TupleGetItem(func_741_call(), 0)
call_1590 = relay.TupleGetItem(func_742_call(), 0)
output = relay.Tuple([call_1564,call_1589,])
output2 = relay.Tuple([call_1565,call_1590,])
func_1592 = relay.Function([], output)
mod['func_1592'] = func_1592
mod = relay.transform.InferType()(mod)
mutated_mod['func_1592'] = func_1592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1592_call = mutated_mod.get_global_var('func_1592')
call_1593 = func_1592_call()
output = call_1593
func_1594 = relay.Function([], output)
mutated_mod['func_1594'] = func_1594
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1360_call = mod.get_global_var('func_1360')
func_1361_call = mutated_mod.get_global_var('func_1361')
call_1634 = relay.TupleGetItem(func_1360_call(), 1)
call_1635 = relay.TupleGetItem(func_1361_call(), 1)
func_1327_call = mod.get_global_var('func_1327')
func_1329_call = mutated_mod.get_global_var('func_1329')
const_1647 = relay.const([2,-8,-1,6,7,4,-6,-6,-6,6,9,3,-3,5,9,-8,1,5,2,9,-9,-3,-3,5,9,7,1,9,9,6,10,-10,-9,-3,6,-10,-5,10,-1,9,-8,9,-8,-3,-6,4,4,-9,9,-6,1,10,9,6,-6,-2,-3,6,-1,6,-10,7,4,-9,-5,-8,10,-4,9,-1,-7,1,-3,-3,8,6,-2,3,7,7,-6,-8,-4,-7,2,-9,-10,1,9,-10,3,-4,6,-1,9,5,-4,4,-5,10,-9,-8,-1,-2,3,7,7,1,9,8,-9,-3,-8,-10,8,-2,-10,5,9,4,-1,-8,-2,-6,2,-7,9,-3,-7,-1,4,1,4,-5,-7,-5,-2,9,-3,-5,8,-5,3,7,-2,6,-4,9,-7,2,-5,-10,-1,1,3,8,-7,10,2,2,6,1,-7,9,-9,5,2,-1,4,9,-7,1,-2,5,-8,10,-5,5,3,3,9,-6,-3,3,10,-7,1,-2,-10,-6,6,-4,5,2,-5,10,4,4,2,7,1,10,5,-2,-10,1,2,-6,5,7,-2,-6,2,4,-9,-5,-8,-10,-8,7,-3,-2,4,-4,-6,10,9,-4,6,-4,-2,5,5,-4,10,-8,2,7,-10,6,5,5,2,4,1,4,6,-7,5,-3,5,-9,5,-2,1,2,3,-8,7,4,-10,3,-8,-9,2,-9,7,-1,-5,7,10,-2,7,10,1,-3,-2,9,7,-2,-3,-3,8,3,8,1,-9,2,2,1,-6,6,-1,8,6,6,-1,-10,-4,6,2,1,-8,-9,-3,-4,7,8,7,-7,-6,-2,3,-7,4,-10,-1,-8,-3,9,-9,6,-5,3,10,4,-10,-2,8,-1,-5,9,-3,-6,5,-4,-10,-8,5,-6,-9,1,-7,-6,6,-7,8,8,-4,8,2,2,2,-7,-3,-2,-3,4,7,7,7,4,-2,7,-9,-3,-6,-2,-7,5,-2,-2,1,-7,8,-2,9,-2,-2,-5,5,1,5,10,-2,1,2,-1,3,-1,-1,8,1,-1,1,6,-3,7,-10,-9,-2,8,-6,-6,6,-10,10,-9,9,6,7,6,-8,-6,-10,5,-7,-3,-2,2,6,-9,1,1,-9,10,8,-5,-10,7,8,-1,4,8,5,-6,-3,9,-4,-5,-7,10,-2,-2,-6,2,10,8,7,2,5,3,2,1,-4,10,3,7,-2,8,9,-1,1,-4,5,-2,-3,-10,9,-10,10,-4,-9,6,9,1,-4,-8,-4,-5,8,1,4,-6,-5,-8,8,5,1,1,7,-2,4,6,-4,-7,8,-6,9,7,-10,-8,5,6,-7,9,-8,-3,-1,-8,-9,9,-3,2,-5,-8,4,-3,-1,8,-7,2,-8,-8,5,3,-1,3,-7,9,-6,9,5,10,5,4,4,7,-2,-10,3,10,8,-9,8,7,5,3,-9,5,-10,-6,-8,8,-10,-6,-4,6,-10,6,-2,-2,-10,8,8,1,-4,-4,-2,2,-1,-4,5,-6,6,2,5,-7,-9,-4,8,-8,-2,5,-7,5,-5,2,8,4,-9,4,-10,-9,-5,9,8,-6,-2,-4,9,-4,8,-2,-5,10,3,-8,-4,6,-9,3,-2,10,3,10,3,4,-1,10,5,10,6,2,6,-1,3,-4,4,-1,-8,-9,-7,6,3,6,8,7,5,-3,-9,5,8,-9,5,-1,2,-8,5,1,-10,6,-4,-9,2,9,8,-3,5,-3,3,5,-6,-4,-7,-8,1,-4,-7,-3,6,-8,6,-3,5,-3,-9,-4,3,5,5,6,7,1,2,-1,-6,5,4,6,3,8,2,-7,1,5,-5,-2,-1,-4,-8,1,6,9,3,9,-7,-8,-2,1,6,9,-7,4,3,10,5,-7,-7,-2,4,-6,10,-9,8,-6,-8,-6,6,-2,7,4,5,-2,-8,5,-8,2,-7,-2,10,1,-3,-2,8,1,10,-9,5,-9,8,6,7,3,8,10,3,6,2,-6,4,10,-1,8,10,10,3,3,-3,-5,10,-8,1,-9,-4,5,-10,-3,-4,6,10,4,-1,5,-3,-6,-8,-6,-10,3,-9,3,5,-10,-7,-5,-2,2,7,-1,8,3,-2,6,-3,-6,-9,-10,3,3,6,-8,-10,4,-8,8,-2,5,-10,-6,1,-5,-8,-5,7,-2,-10,3,-1,-9,-4,8,-8,10,5,4,7,-8,-6,-6,3,-8,-8,-4,8,9,-10,7,-1,9,4,-4,3,-6,7,2,9,4,10,6,1,9,-6,3,-7,5,-6,-2,3,7,-9,-1,-10,-6,2,8,9,9,6,-3,4,4,-9,10,4,1,8,-2,6,9,-9,-3,4,2,-4,5,-2,-10,5,2,-7,3,-6,6,-10,-2,-9,7,-7,-5,5,10,9,10,-10,-3,9,4,10,9,-2,9,8,-7,7,7,-2,-1,7,-4,6,-5,7,10,1,7,4,7,2,-8,-5,-10,4,-7,3,-7,3,3,3,-5,-5,-8,-8,3,-8,-10,-6,10,-2,-10,-8,-3,10,1,1,6,8,-7,8,8,-10,10,1,-7,-5,-9,5,6,-9,-7,-2,-6,-8,9,-2,-5,-9,10,3,2,-4,2,2,5,4,-10,6,9,1,-1,8,7,8,-5,5,-10,-8,-10,-2,-2,6,5,7,5,5,-1,3,10,5,4,-7,-1,-7,-5,-6,7,6,4,-7,3,7,7,-2,-1,6,-1,10,-6,-4,7,-8,4,6,9,-6,-7,6,5,3,-9,1,-2,1,-9,-8,7,-9,-2,-6,10,5,9,3,1,9,-5,-1,1,-4,9,7,2,4,2,-4,5,2,-1,7,-3,6,-7,6,9,10,-3,-5,-6,-8,-10,-3,-2,-1,3,6,4,-3,-9,3,-10,7,2,10,-2,8,-1,-8,-7,-7,-9,-6,7,6,-10,-5,3,-4,5,-5,-2,-8,4,-9,7,1,1,8,9,-3,4,7,-3,4,-7,-4,4,6,-9,10,9,9,1,9,1,6,1,3,-8,-1,-8,6,8,-9,-4,-3,2,-4,-9,-2,-6,-4,-6,10,-3,-9,-9,-2,-6,4,-2,7,-8,7,-6,8,9,-7,-10,-9,2,-4,4,8,9,-3,10,4,-1,-7,-2,-6,-6,8,-4,9,-8,6,2,-3,7,-1,4,-9,10,1,-1,-5,-4,3,3,-5,-6,2,-7,9,8,5,9,8,-9,1,8,7,10,-1,3,-3,-10,-6,-7,3,7,9,3,5,-6,2,-2,-7,8,-7,-7,1,-7,-4,-4,-2,-6,-8,8,-1,-8,8,9,-6,5,-9,6,-10,6,7,-1,-2,-10,6,-2,2,-9,3,8,-8,-1,-7,-4,9,-9,2,5,-6,2,3,-2,-7,-9,-10,8,-2,-4,7,8,-10,10,8,3,10,-8,3,-10,-1,-9,-6,9,-7,8,3,-7,2,4,-3,-4,6,8,3,10,-6,7,7,9,10,-7,5,5,-5,7,-8,3,-6,3,-8,3,3,4,-5,5,2,8,8,-5,4,1,5,-6,-4,8,4,-3,-1,-7,2,4,6,1,7,8,-8,-3,-4,1,10,9,-3,8,-3,-4,9,-9,4,-10,6,4,7,-4,-8,9,8,-9,2,9,-6,-10,-3,-1,-9,-7,7,6,9,-2,-6,-3,9,-7,3,6,-9,6,5,6,-6,-8,4,-6,-3,8,-1,6,-6,3,-9,9,-7,-9,-2,-8,-9,1,8,4,8,-5,-4,-9,5,10,-4,3,5,4,6,8,-8,-9,-8,10,-7,-5,7,3,-9,-8], dtype = "int8")#candidate|1647|(1440,)|const|int8
call_1646 = relay.TupleGetItem(func_1327_call(relay.reshape(const_1647.astype('int8'), [1440,])), 1)
call_1648 = relay.TupleGetItem(func_1329_call(relay.reshape(const_1647.astype('int8'), [1440,])), 1)
func_1360_call = mod.get_global_var('func_1360')
func_1361_call = mutated_mod.get_global_var('func_1361')
call_1650 = relay.TupleGetItem(func_1360_call(), 0)
call_1651 = relay.TupleGetItem(func_1361_call(), 0)
func_1067_call = mod.get_global_var('func_1067')
func_1069_call = mutated_mod.get_global_var('func_1069')
call_1654 = relay.TupleGetItem(func_1067_call(), 0)
call_1655 = relay.TupleGetItem(func_1069_call(), 0)
func_585_call = mod.get_global_var('func_585')
func_586_call = mutated_mod.get_global_var('func_586')
call_1656 = relay.TupleGetItem(func_585_call(), 1)
call_1657 = relay.TupleGetItem(func_586_call(), 1)
func_884_call = mod.get_global_var('func_884')
func_886_call = mutated_mod.get_global_var('func_886')
var_1663 = relay.var("var_1663", dtype = "float32", shape = (312,))#candidate|1663|(312,)|var|float32
call_1662 = relay.TupleGetItem(func_884_call(relay.reshape(var_1663.astype('float32'), [13, 8, 3])), 2)
call_1664 = relay.TupleGetItem(func_886_call(relay.reshape(var_1663.astype('float32'), [13, 8, 3])), 2)
uop_1674 = relay.erf(call_1656.astype('float32')) # shape=(1, 12, 2)
uop_1676 = relay.erf(call_1657.astype('float32')) # shape=(1, 12, 2)
bop_1685 = relay.left_shift(uop_1674.astype('uint16'), relay.reshape(call_1650.astype('uint16'), relay.shape_of(uop_1674))) # shape=(1, 12, 2)
bop_1688 = relay.left_shift(uop_1676.astype('uint16'), relay.reshape(call_1651.astype('uint16'), relay.shape_of(uop_1676))) # shape=(1, 12, 2)
func_1537_call = mod.get_global_var('func_1537')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_1689 = relay.TupleGetItem(func_1537_call(), 0)
call_1690 = relay.TupleGetItem(func_1539_call(), 0)
output = relay.Tuple([call_1634,call_1646,const_1647,call_1654,call_1662,var_1663,bop_1685,call_1689,])
output2 = relay.Tuple([call_1635,call_1648,const_1647,call_1655,call_1664,var_1663,bop_1688,call_1690,])
func_1695 = relay.Function([var_1663,], output)
mod['func_1695'] = func_1695
mod = relay.transform.InferType()(mod)
mutated_mod['func_1695'] = func_1695
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1696 = relay.var("var_1696", dtype = "float32", shape = (312,))#candidate|1696|(312,)|var|float32
func_1695_call = mutated_mod.get_global_var('func_1695')
call_1697 = func_1695_call(var_1696)
output = call_1697
func_1698 = relay.Function([var_1696], output)
mutated_mod['func_1698'] = func_1698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1592_call = mod.get_global_var('func_1592')
func_1594_call = mutated_mod.get_global_var('func_1594')
call_1711 = relay.TupleGetItem(func_1592_call(), 0)
call_1712 = relay.TupleGetItem(func_1594_call(), 0)
var_1746 = relay.var("var_1746", dtype = "float64", shape = (13, 12, 2))#candidate|1746|(13, 12, 2)|var|float64
bop_1747 = relay.bitwise_or(call_1711.astype('int64'), var_1746.astype('int64')) # shape=(13, 12, 2)
bop_1750 = relay.bitwise_or(call_1712.astype('int64'), var_1746.astype('int64')) # shape=(13, 12, 2)
func_1472_call = mod.get_global_var('func_1472')
func_1473_call = mutated_mod.get_global_var('func_1473')
call_1757 = func_1472_call()
call_1758 = func_1472_call()
func_444_call = mod.get_global_var('func_444')
func_446_call = mutated_mod.get_global_var('func_446')
call_1768 = relay.TupleGetItem(func_444_call(), 0)
call_1769 = relay.TupleGetItem(func_446_call(), 0)
func_810_call = mod.get_global_var('func_810')
func_813_call = mutated_mod.get_global_var('func_813')
const_1774 = relay.const([0.896067,1.637736,-4.945165,-3.274156,5.092462,-0.685802,9.575031,2.461912,-8.233818,-7.009619,8.351898,-1.530932,6.920701,-2.919631,-9.330237,3.238281,3.016939,3.291239,8.202764,0.762310,6.168537,2.191939,-5.462819,4.995607,6.835574,-2.461290,-9.966180,-1.600281,-9.761323,4.461874,1.646569,-6.283604,0.408178,0.736197,0.619458,9.526023,-1.434873,3.041912,9.084597,8.666829,-2.256768,-9.441845,0.058247,1.450341,9.999458,-1.314306,4.122247,-3.371457,-2.394740,-6.507279,-0.355246,-4.232278,-4.127104,4.082451,0.533077,5.571909,-5.550489,-8.351745,-1.463993,-1.603573,-5.361090,2.102027,5.489609,-3.184209,7.168348,-1.139993,-7.165524,-3.328716,-0.832424,1.452231,-3.923561,-1.778240], dtype = "float64")#candidate|1774|(72,)|const|float64
call_1773 = relay.TupleGetItem(func_810_call(relay.reshape(const_1774.astype('float64'), [3, 12, 2])), 0)
call_1775 = relay.TupleGetItem(func_813_call(relay.reshape(const_1774.astype('float64'), [3, 12, 2])), 0)
output = relay.Tuple([bop_1747,call_1757,call_1768,call_1773,const_1774,])
output2 = relay.Tuple([bop_1750,call_1758,call_1769,call_1775,const_1774,])
func_1790 = relay.Function([var_1746,], output)
mod['func_1790'] = func_1790
mod = relay.transform.InferType()(mod)
mutated_mod['func_1790'] = func_1790
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1791 = relay.var("var_1791", dtype = "float64", shape = (13, 12, 2))#candidate|1791|(13, 12, 2)|var|float64
func_1790_call = mutated_mod.get_global_var('func_1790')
call_1792 = func_1790_call(var_1791)
output = call_1792
func_1793 = relay.Function([var_1791], output)
mutated_mod['func_1793'] = func_1793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1537_call = mod.get_global_var('func_1537')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_1838 = relay.TupleGetItem(func_1537_call(), 0)
call_1839 = relay.TupleGetItem(func_1539_call(), 0)
uop_1842 = relay.rsqrt(call_1838.astype('float64')) # shape=(1, 12, 2)
uop_1844 = relay.rsqrt(call_1839.astype('float64')) # shape=(1, 12, 2)
func_472_call = mod.get_global_var('func_472')
func_475_call = mutated_mod.get_global_var('func_475')
var_1854 = relay.var("var_1854", dtype = "float64", shape = (156,))#candidate|1854|(156,)|var|float64
call_1853 = relay.TupleGetItem(func_472_call(relay.reshape(var_1854.astype('float64'), [4, 13, 3])), 0)
call_1855 = relay.TupleGetItem(func_475_call(relay.reshape(var_1854.astype('float64'), [4, 13, 3])), 0)
func_1285_call = mod.get_global_var('func_1285')
func_1287_call = mutated_mod.get_global_var('func_1287')
call_1863 = func_1285_call()
call_1864 = func_1285_call()
func_517_call = mod.get_global_var('func_517')
func_518_call = mutated_mod.get_global_var('func_518')
call_1865 = func_517_call()
call_1866 = func_517_call()
bop_1867 = relay.maximum(uop_1842.astype('int8'), relay.reshape(call_1838.astype('int8'), relay.shape_of(uop_1842))) # shape=(1, 12, 2)
bop_1870 = relay.maximum(uop_1844.astype('int8'), relay.reshape(call_1839.astype('int8'), relay.shape_of(uop_1844))) # shape=(1, 12, 2)
func_42_call = mod.get_global_var('func_42')
func_45_call = mutated_mod.get_global_var('func_45')
var_1886 = relay.var("var_1886", dtype = "float64", shape = (330,))#candidate|1886|(330,)|var|float64
call_1885 = relay.TupleGetItem(func_42_call(relay.reshape(var_1886.astype('float64'), [11, 6, 5])), 0)
call_1887 = relay.TupleGetItem(func_45_call(relay.reshape(var_1886.astype('float64'), [11, 6, 5])), 0)
func_1360_call = mod.get_global_var('func_1360')
func_1361_call = mutated_mod.get_global_var('func_1361')
call_1889 = relay.TupleGetItem(func_1360_call(), 1)
call_1890 = relay.TupleGetItem(func_1361_call(), 1)
func_585_call = mod.get_global_var('func_585')
func_586_call = mutated_mod.get_global_var('func_586')
call_1898 = relay.TupleGetItem(func_585_call(), 0)
call_1899 = relay.TupleGetItem(func_586_call(), 0)
func_472_call = mod.get_global_var('func_472')
func_475_call = mutated_mod.get_global_var('func_475')
call_1900 = relay.TupleGetItem(func_472_call(relay.reshape(var_1854.astype('float64'), [4, 13, 3])), 0)
call_1901 = relay.TupleGetItem(func_475_call(relay.reshape(var_1854.astype('float64'), [4, 13, 3])), 0)
uop_1914 = relay.sqrt(bop_1867.astype('float64')) # shape=(1, 12, 2)
uop_1916 = relay.sqrt(bop_1870.astype('float64')) # shape=(1, 12, 2)
func_1127_call = mod.get_global_var('func_1127')
func_1129_call = mutated_mod.get_global_var('func_1129')
call_1929 = relay.TupleGetItem(func_1127_call(), 0)
call_1930 = relay.TupleGetItem(func_1129_call(), 0)
func_1327_call = mod.get_global_var('func_1327')
func_1329_call = mutated_mod.get_global_var('func_1329')
var_1933 = relay.var("var_1933", dtype = "int8", shape = (10, 144))#candidate|1933|(10, 144)|var|int8
call_1932 = relay.TupleGetItem(func_1327_call(relay.reshape(var_1933.astype('int8'), [1440,])), 1)
call_1934 = relay.TupleGetItem(func_1329_call(relay.reshape(var_1933.astype('int8'), [1440,])), 1)
output = relay.Tuple([call_1853,var_1854,call_1863,call_1865,call_1885,var_1886,call_1889,call_1898,call_1900,uop_1914,call_1929,call_1932,var_1933,])
output2 = relay.Tuple([call_1855,var_1854,call_1864,call_1866,call_1887,var_1886,call_1890,call_1899,call_1901,uop_1916,call_1930,call_1934,var_1933,])
func_1935 = relay.Function([var_1854,var_1886,var_1933,], output)
mod['func_1935'] = func_1935
mod = relay.transform.InferType()(mod)
var_1936 = relay.var("var_1936", dtype = "float64", shape = (156,))#candidate|1936|(156,)|var|float64
var_1937 = relay.var("var_1937", dtype = "float64", shape = (330,))#candidate|1937|(330,)|var|float64
var_1938 = relay.var("var_1938", dtype = "int8", shape = (10, 144))#candidate|1938|(10, 144)|var|int8
output = func_1935(var_1936,var_1937,var_1938,)
func_1939 = relay.Function([var_1936,var_1937,var_1938,], output)
mutated_mod['func_1939'] = func_1939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_585_call = mod.get_global_var('func_585')
func_586_call = mutated_mod.get_global_var('func_586')
call_2015 = relay.TupleGetItem(func_585_call(), 1)
call_2016 = relay.TupleGetItem(func_586_call(), 1)
func_1462_call = mod.get_global_var('func_1462')
func_1463_call = mutated_mod.get_global_var('func_1463')
call_2017 = func_1462_call()
call_2018 = func_1462_call()
func_1360_call = mod.get_global_var('func_1360')
func_1361_call = mutated_mod.get_global_var('func_1361')
call_2033 = relay.TupleGetItem(func_1360_call(), 2)
call_2034 = relay.TupleGetItem(func_1361_call(), 2)
bop_2044 = relay.add(call_2015.astype('int32'), relay.reshape(call_2017.astype('int32'), relay.shape_of(call_2015))) # shape=(1, 12, 2)
bop_2047 = relay.add(call_2016.astype('int32'), relay.reshape(call_2018.astype('int32'), relay.shape_of(call_2016))) # shape=(1, 12, 2)
func_1327_call = mod.get_global_var('func_1327')
func_1329_call = mutated_mod.get_global_var('func_1329')
var_2059 = relay.var("var_2059", dtype = "int8", shape = (360, 4))#candidate|2059|(360, 4)|var|int8
call_2058 = relay.TupleGetItem(func_1327_call(relay.reshape(var_2059.astype('int8'), [1440,])), 0)
call_2060 = relay.TupleGetItem(func_1329_call(relay.reshape(var_2059.astype('int8'), [1440,])), 0)
func_810_call = mod.get_global_var('func_810')
func_813_call = mutated_mod.get_global_var('func_813')
const_2069 = relay.const([[8.923063,2.606344,0.491289,-2.476777,-4.809131,-8.761071,-8.589357,-4.933003,-5.300928,4.367158,1.172995,6.478135],[1.905444,-1.263677,8.628313,8.747848,7.915096,7.575139,4.997672,1.902028,-4.053356,0.681515,-2.394040,9.446667],[-6.070517,-4.755622,-0.317214,-0.060229,-4.317060,3.148622,-0.882894,2.422683,3.128429,8.779026,-6.184877,-6.627622],[-9.212191,6.631016,3.079402,4.525428,5.459417,7.914152,9.322727,7.664681,-5.365145,-4.918310,-0.615305,0.122021],[-9.912697,-0.068061,6.125959,5.707592,-2.535554,-4.319413,8.570655,-4.317553,4.049574,4.807921,3.964560,-2.820877],[6.675171,-7.432629,-0.534691,-1.335994,-2.181695,-3.966416,7.267802,0.198661,-3.558387,-9.100788,-1.159290,3.971376]], dtype = "float64")#candidate|2069|(6, 12)|const|float64
call_2068 = relay.TupleGetItem(func_810_call(relay.reshape(const_2069.astype('float64'), [3, 12, 2])), 0)
call_2070 = relay.TupleGetItem(func_813_call(relay.reshape(const_2069.astype('float64'), [3, 12, 2])), 0)
output = relay.Tuple([call_2033,bop_2044,call_2058,var_2059,call_2068,const_2069,])
output2 = relay.Tuple([call_2034,bop_2047,call_2060,var_2059,call_2070,const_2069,])
func_2078 = relay.Function([var_2059,], output)
mod['func_2078'] = func_2078
mod = relay.transform.InferType()(mod)
mutated_mod['func_2078'] = func_2078
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2079 = relay.var("var_2079", dtype = "int8", shape = (360, 4))#candidate|2079|(360, 4)|var|int8
func_2078_call = mutated_mod.get_global_var('func_2078')
call_2080 = func_2078_call(var_2079)
output = call_2080
func_2081 = relay.Function([var_2079], output)
mutated_mod['func_2081'] = func_2081
mutated_mod = relay.transform.InferType()(mutated_mod)
func_517_call = mod.get_global_var('func_517')
func_518_call = mutated_mod.get_global_var('func_518')
call_2118 = func_517_call()
call_2119 = func_517_call()
func_810_call = mod.get_global_var('func_810')
func_813_call = mutated_mod.get_global_var('func_813')
var_2133 = relay.var("var_2133", dtype = "float64", shape = (1, 72))#candidate|2133|(1, 72)|var|float64
call_2132 = relay.TupleGetItem(func_810_call(relay.reshape(var_2133.astype('float64'), [3, 12, 2])), 0)
call_2134 = relay.TupleGetItem(func_813_call(relay.reshape(var_2133.astype('float64'), [3, 12, 2])), 0)
output = relay.Tuple([call_2118,call_2132,var_2133,])
output2 = relay.Tuple([call_2119,call_2134,var_2133,])
func_2135 = relay.Function([var_2133,], output)
mod['func_2135'] = func_2135
mod = relay.transform.InferType()(mod)
mutated_mod['func_2135'] = func_2135
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2136 = relay.var("var_2136", dtype = "float64", shape = (1, 72))#candidate|2136|(1, 72)|var|float64
func_2135_call = mutated_mod.get_global_var('func_2135')
call_2137 = func_2135_call(var_2136)
output = call_2137
func_2138 = relay.Function([var_2136], output)
mutated_mod['func_2138'] = func_2138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_585_call = mod.get_global_var('func_585')
func_586_call = mutated_mod.get_global_var('func_586')
call_2140 = relay.TupleGetItem(func_585_call(), 0)
call_2141 = relay.TupleGetItem(func_586_call(), 0)
output = relay.Tuple([call_2140,])
output2 = relay.Tuple([call_2141,])
func_2149 = relay.Function([], output)
mod['func_2149'] = func_2149
mod = relay.transform.InferType()(mod)
output = func_2149()
func_2150 = relay.Function([], output)
mutated_mod['func_2150'] = func_2150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_444_call = mod.get_global_var('func_444')
func_446_call = mutated_mod.get_global_var('func_446')
call_2162 = relay.TupleGetItem(func_444_call(), 0)
call_2163 = relay.TupleGetItem(func_446_call(), 0)
var_2169 = relay.var("var_2169", dtype = "float64", shape = (14, 12, 2))#candidate|2169|(14, 12, 2)|var|float64
bop_2170 = relay.bitwise_or(call_2162.astype('int8'), var_2169.astype('int8')) # shape=(14, 12, 2)
bop_2173 = relay.bitwise_or(call_2163.astype('int8'), var_2169.astype('int8')) # shape=(14, 12, 2)
func_729_call = mod.get_global_var('func_729')
func_732_call = mutated_mod.get_global_var('func_732')
const_2177 = relay.const([2,-5,-3,-3,8,-5,2,-4,-6,-4,-5,-5,-4,-2,-8,9,2,-7,9,-1,3,1,-3,8,5,10,-3,-5,-4,6,-8,1,10,-5,8,-5,2,-8,3,4,6,-8,-1,-9,-1,-6,-1,9,5,-10,1,-5,1,10,1,-2,10,-7,-4,-5,-1,-6,-9,6,10,-10,1,-4,1,6,7,-9,9,-7,2,10,2,8,8,9,9,-8,5,5,-5,-7,1,1,-2,1,-8,-9,-6,6,-8,3,-2,-8,-5,2,5,4,5,-4,-2,3,7,-4,7,-6,-3,-4,9,4,6,4,7,-5,-3,-1,5,7,-4,-2,9,9,6,10,7,9,-2,-5,3,5,-1,1,10,8,8,-6,8,2,-9,9,-8,1,1,1,8,-10,-2,-4,8,6,-2,7,-10,-3,-1,6,1,9,3,-4,8,7,4,2,-3,-1,3,-4,5,1,-10,-7,-4,10,8,6,9,-6,9,6,6,-7,-5,1,8,8,-1,-6,-1,4,-2,5,-6,-6,-7,-6,-2,-2,-6,7,-7,4,1,-4,-8,-4,-9,-4,10,-1,-4,9,-4,3,6,-5,-6,-2,1,-9,-6,-1,-2,1,7,-8,-1,-7,10,6,-9,-2,10,-3,-1,9,-5,-2,5,8,7,3,3,-4,9,10,1,-4,-7,3,9,-5,2,1,5,9,5,2,9,2,8,-7,-5,1,10,-10,-5,5,-4,-5,8,-1,-6,-1,-2,5,5,6,-5,-2,10,3,-6,-3,5,-9,3,-5,6,-4,-1,6,-10,-7,-1,1,-10,-9,3,7,1,2,-8,1,-5,2,-3,-1,5,10,-7,-9,3,1,9,5,-6,2,-6,-9,9,8,-2,-4,6,-4,5,10,-9,-6,-1,-8,2,10,-6,-10,2,4,-6,2,-4,-7,-10,-7,-9,9,7,-6,9,4,5,-10,-1,-3,-5,-1,9,-8,-4,-8,-9,3,-6,3,-5,1,-5,6,-7,3,2,-1,-1,-2,5,7,8,-1,9,10,-5,1,-5,-5,8,2,-1,2,3,8,5,5,-5,10,10,-7,4,-4,7,-9,7,-6,6,4,-4,-1,-8,-4,1,-9,5,-10,4,-6,-3,-7,-8,-1,-2,6,-7,-5,-3,10,-5,9,-4,9,-10,2,-1,4,-3,6,9,-9,10,3,-7,7,1,1,2,-7,4,6,10,5,-6,-9,4,5,-4,-5,-1,-2,-8,-2,-3,-5,-10,-4,-2,4,-1,-6,2,7,10,-8,6,-5,-5,7,6,8,-2,4,3,-5,-2,-7,4,2,-8,5,2,-8,-5,-6,-6,4,-5,3,10,-2,3,-9,-5,-9,1,9,-3,10,-2,8,-9,8,-3,-3,1,7,7,8,-7,7,2,1,4,3,10,-4,6,-4,-2,-3,-4,-6,-4,-3,5,9,5,-3,3,-5,-1,-3,-2,7,-6,9,-1,-9,3,-8,-1,6,-8,6,-6,6,3,-4,6,9,2,-2,-6,9,-2,-6,3,2,2,3,-1,5,8,-9,3,-6,7,-7,8,2,3,6,9,-5,6,-9,9,-10,-5,1,8,-2,-5,8,5,7,8,-3,-1,-8,-8,-5,2,4,-4,-7,2,7,-8,-3,5,-2,5,-9,-6,3,-5,3,-4,9,1,10,5,3,2,-8,-7,-9,-6,9,7,-7,10,4,-6,2,10,3,1,9,-3,2,7,-4,-2,-6,5,-5,-3,1,-3,9,8,9,7,3,-4,1,6,6,-6,-1,6,-10,-7,8,-5,-3,10,-2,-1,8,10,9,-3,-6,-7,-2,4,-2,4,-1,9,-1,8,-6,8,4,-1,6,8,-5,-10,10,10,3,1,2,-9,-9,-8,-8,8,4,7,-5,1,-9,-10,3,10,5,-1,5,2,1,-8,-6,-10,-8,-8,1,-7,-10,-1,7,2,-7,9,-5,6,10,-4,2,7,-3,5,6,-6,8,-3,3,7,8,-9,-6,8,9,-4,-8,-3,8,4,-1,-4,10,-2,-1,-10,-4,4,4,-9,6,5,6,4,7,10,8,5,-1,8,7,-3,-9,-2,-8,7,6,-7,-2,-6,9,-5,10,-3,-8,-3,9,7,-2,10,-1,6,-2,10,6,-3,2,9,9,-2,-5,5,2,1,-2,-4,9,-2,4,5,6,4,5,1,-7,4,-2,7,10,8,10,-6,-3,-2,-8,9,-4,-3,8,6,9,-7,-6,4,2,-9,-3,3,-1,5,9,-7,-6,-3,-6,-10,-8,7,3,9,1,-8,-3,2,-6,-5,-10,-10,-3,-9,-2,6,-5,-4,-2,4,3,10,4,9,-1,-5,-9,5,9,-2,2,1,-1,-8,9,8,5,-7,-2,-1,5,3,-2,-7,-2,-2,-7,6,9,10,-5,10,-8,10,-7,4,6,5,6,7,-1,6,1,3,-3,7,-3,9,6,-3,8,-3,5,-2,-10,-10,-9,8,-8,9,-5,-9,-5,-2,-8,2,-4,-2,-6,1,5,-8,10,4,6,9,-10,-10,9,-6,8,-6,-6,1,-5,8,6,4,-2,5,-2,9,-5,8,2,-4,3,-3,8,-9,-8,5,-2,1,-7,-2,-1,2,-2,1,-6,6,-4,-8,-3,-7,5,7,1,3,-4,-9,-6,4,-3,3,9,9,-6,-6,-6,-2,-5,10,6,-5,8,7,5,3,-6,7,6,9,-7,-3,-9,3,1,-1,-9,-7,-8,-3,8,3,4,9,10,-4,-4,9,3,7,-7,2,3,-5,6,6,-5,7,-10,3,-6,-4,-5,6,-5,1,1,8,-5,-9,-10,-4,-3,-8,9,3,-8,8,10,-1,-6,6,8,-3,6,3,-6,-5,-9,-4,-4,-6,3,-8,-7,-7,5,-10,7,7,5,3,8,10,3,-8,10,3,-9,8,2,-10,-9,2,-4,-3,-1,-10,-6,-6,6,-10,-1,2,4,5,5,4,6,2,-7,8,-3,6,-1,-10,8,3,-3,-9,-7,4,10,10,6,-7,-8,10,3,3,-8,-1,3,6,-3,2,9,-3,-3,-6,-6,-1,-8,-8,-7,-7,3,3,-5,3,-6,-7,-8,6,5,10,7,-8,4,-7,6,-8,-3,-7,10,4,5,-2,4,-6,-2,-4,10,3,7,-5,-4,-4,-3,-5,2,-10,-3,-2,2,7,4,4,-3,-8,-9,-3,-7,9,-7,3,-6,-6,7,5,6,5,5,-6,8,-9,8,-9,-1,4,-5,-7,4,-9,1,-10,7,-7,-7,-3,6,2,-7,2,3,4,-5,-10,-6,9,2,2,-7,6,-1,-8,4,-4,3,7,-2,-4,3,7,3,-7,-7,6,10,-7,2,10,5,7,2,4,6,-2,-1,10,-6,9,-8,7,-1,-8,10,-1,6,7,-3,-1,-10,-1,1,-7,10,10,4,-3,4,10,-1,-2,-8,-4,-9,-1,7,2,-3,5,-6,9,-4,5,-6,-3,5,-6,4,5,5,4,7,-10,-6,2,-3,2,-5,-7,-3,10,6,2,-5,3,2,-4,3,9,-2,-1,-2,-2,3,8,2,3,-3,9,-1,-10,2,-4,-9,-6,2,5,2,10,9,-1,-5,10,-1,-6,5,-7,-1,4,4,2,-7,1,-4,-5,1,5,-2,4,8,-6,-7,10,6,1,-1,-7,9,10,-10,-8,2,-7,-10,8,2,-1,-6,8,-2,-1,9,3,-5,1,7,8,-5,-4,7,-1,5,-7,-2,5,1,8,6,-10,-6,8,-2,-5,-1,-10,-8,-5,-4,3,5,-1,-6,8,4,-10,-1,-6,-5,10,7,-2,2,9,8,-5,2,1,8,-7,-9,3,-7,1,-9], dtype = "int8")#candidate|2177|(1440,)|const|int8
call_2176 = relay.TupleGetItem(func_729_call(relay.reshape(const_2177.astype('int8'), [9, 10, 16]), relay.reshape(const_2177.astype('int8'), [9, 10, 16]), ), 1)
call_2178 = relay.TupleGetItem(func_732_call(relay.reshape(const_2177.astype('int8'), [9, 10, 16]), relay.reshape(const_2177.astype('int8'), [9, 10, 16]), ), 1)
func_42_call = mod.get_global_var('func_42')
func_45_call = mutated_mod.get_global_var('func_45')
var_2180 = relay.var("var_2180", dtype = "float64", shape = (330,))#candidate|2180|(330,)|var|float64
call_2179 = relay.TupleGetItem(func_42_call(relay.reshape(var_2180.astype('float64'), [11, 6, 5])), 0)
call_2181 = relay.TupleGetItem(func_45_call(relay.reshape(var_2180.astype('float64'), [11, 6, 5])), 0)
uop_2193 = relay.log2(call_2176.astype('float64')) # shape=(1, 12, 2)
uop_2195 = relay.log2(call_2178.astype('float64')) # shape=(1, 12, 2)
func_884_call = mod.get_global_var('func_884')
func_886_call = mutated_mod.get_global_var('func_886')
const_2197 = relay.const([4.746227,-7.148251,4.381713,2.399904,-4.129527,-8.682419,-7.056108,-7.882091,7.959949,2.748477,6.983108,-8.063961,9.754279,-3.986861,-9.233851,0.282352,7.856683,-5.978798,-6.172590,-5.752595,-0.974178,-5.523110,-6.445244,-8.549554,9.473575,-6.625251,-1.074817,-7.883472,5.159488,-8.892227,4.934290,-8.176347,-9.171059,8.913694,-2.191534,5.573472,-6.421055,9.427438,-0.395117,0.953969,8.980278,-4.167467,-4.248896,5.754016,5.356707,-4.383003,0.256558,8.379695,4.361305,9.479252,7.800426,1.579164,-7.831239,-9.158769,-4.451975,-2.454319,9.254685,8.098397,3.191250,-0.583659,-4.993450,8.979101,7.157170,4.136961,2.332007,-9.965002,7.237807,7.472297,-4.433398,-5.266515,7.341413,0.460818,-3.389557,-7.228867,5.634988,-8.218402,0.181751,-1.134299,6.074562,-6.813947,-3.168628,3.811023,-8.234724,3.727524,-5.805380,7.623938,-0.920843,2.300782,3.287558,-2.592163,-5.291575,-3.763705,0.264767,-1.549935,9.283490,5.214332,0.009281,7.348830,3.704797,-7.362891,5.291058,8.182046,-8.584312,-9.373937,1.423766,8.377036,9.870593,2.966095,-5.574118,1.145358,-8.948664,8.897103,4.005060,1.755905,1.743488,2.337075,2.089378,-6.036815,1.302420,5.816837,4.455694,-9.007417,3.037490,1.512736,1.106875,8.221457,-8.328043,1.940082,1.120672,-0.632538,-7.074325,0.207257,8.809822,-1.730460,-5.232665,2.517243,-2.583664,3.990936,5.338977,7.927853,8.463838,3.464131,8.225859,-8.162271,7.978372,6.040455,-1.946766,-8.322855,-3.635815,-8.836083,-7.427109,-8.004552,6.714634,-9.237364,9.359514,4.506937,-8.514463,-2.314897,9.114838,7.863636,1.830140,-2.106085,6.461525,0.933841,1.699663,3.673567,1.927619,-9.783469,8.800111,-6.775730,-6.404535,4.794112,-7.900996,-1.571020,-5.100610,-5.672578,-7.658246,8.943047,1.526770,6.633498,-8.456893,5.811847,3.175873,-1.767900,-5.120196,0.254003,-7.469146,-1.697767,-2.935953,-5.127152,-8.090359,-1.346509,-7.480917,-6.414649,3.130611,-6.747377,-7.121567,0.265495,-5.265741,-7.143834,-8.838668,7.434484,6.100384,0.534208,1.938855,-2.674600,5.696498,-1.734240,4.483218,3.787965,4.211386,-3.438111,5.375532,3.153165,-4.627518,4.931633,0.101448,1.976275,-4.861634,-4.068963,5.507846,2.614211,0.581849,-3.083197,-0.023560,7.850260,0.876423,-9.897192,-3.934865,-7.572669,5.336738,3.492105,1.138029,9.167719,-1.593277,8.905433,5.351950,-3.338104,-3.227053,2.710041,-7.746085,-8.280739,-7.548523,6.271823,-6.690810,7.329047,4.413232,-1.843552,-1.853063,-9.098846,5.834919,-0.585668,-5.050339,-1.591865,8.139272,6.240168,-1.457086,5.483939,-5.399357,0.563211,0.593988,4.678773,-0.388365,3.798132,0.355031,9.037428,9.402071,9.810624,-5.680202,-5.916532,8.026827,5.784502,-7.478455,8.676836,4.143969,8.382666,0.422516,8.334686,3.364758,-7.957816,-6.038865,7.686274,8.187225,9.417495,-2.346497,1.537541,-3.926684,-0.907512,-2.248937,9.724126,-3.441485,-6.463351,1.217719,9.559033,-2.165257,-8.627278,9.759501,-5.594287,-2.543920,-2.707538,2.792051,0.921003,1.932986,-7.294803,4.154051,8.910523,5.541385,7.923012,-6.234631,9.270894,4.968249,2.817151], dtype = "float32")#candidate|2197|(312,)|const|float32
call_2196 = relay.TupleGetItem(func_884_call(relay.reshape(const_2197.astype('float32'), [13, 8, 3])), 2)
call_2198 = relay.TupleGetItem(func_886_call(relay.reshape(const_2197.astype('float32'), [13, 8, 3])), 2)
output = relay.Tuple([bop_2170,const_2177,call_2179,var_2180,uop_2193,call_2196,const_2197,])
output2 = relay.Tuple([bop_2173,const_2177,call_2181,var_2180,uop_2195,call_2198,const_2197,])
func_2209 = relay.Function([var_2169,var_2180,], output)
mod['func_2209'] = func_2209
mod = relay.transform.InferType()(mod)
mutated_mod['func_2209'] = func_2209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2209_call = mutated_mod.get_global_var('func_2209')
var_2211 = relay.var("var_2211", dtype = "float64", shape = (14, 12, 2))#candidate|2211|(14, 12, 2)|var|float64
var_2212 = relay.var("var_2212", dtype = "float64", shape = (330,))#candidate|2212|(330,)|var|float64
call_2210 = func_2209_call(var_2211,var_2212,)
output = call_2210
func_2213 = relay.Function([var_2211,var_2212,], output)
mutated_mod['func_2213'] = func_2213
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1462_call = mod.get_global_var('func_1462')
func_1463_call = mutated_mod.get_global_var('func_1463')
call_2242 = func_1462_call()
call_2243 = func_1462_call()
var_2257 = relay.var("var_2257", dtype = "bool", shape = (7, 12, 2))#candidate|2257|(7, 12, 2)|var|bool
bop_2258 = relay.bitwise_or(call_2242.astype('int32'), var_2257.astype('int32')) # shape=(7, 12, 2)
bop_2261 = relay.bitwise_or(call_2243.astype('int32'), var_2257.astype('int32')) # shape=(7, 12, 2)
output = relay.Tuple([bop_2258,])
output2 = relay.Tuple([bop_2261,])
func_2275 = relay.Function([var_2257,], output)
mod['func_2275'] = func_2275
mod = relay.transform.InferType()(mod)
var_2276 = relay.var("var_2276", dtype = "bool", shape = (7, 12, 2))#candidate|2276|(7, 12, 2)|var|bool
output = func_2275(var_2276)
func_2277 = relay.Function([var_2276], output)
mutated_mod['func_2277'] = func_2277
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2298 = relay.var("var_2298", dtype = "int8", shape = (3, 9, 2))#candidate|2298|(3, 9, 2)|var|int8
var_2299 = relay.var("var_2299", dtype = "int8", shape = (3, 9, 2))#candidate|2299|(3, 9, 2)|var|int8
bop_2300 = relay.less(var_2298.astype('bool'), relay.reshape(var_2299.astype('bool'), relay.shape_of(var_2298))) # shape=(3, 9, 2)
uop_2314 = relay.acosh(var_2298.astype('float32')) # shape=(3, 9, 2)
output = relay.Tuple([bop_2300,uop_2314,])
output2 = relay.Tuple([bop_2300,uop_2314,])
func_2342 = relay.Function([var_2298,var_2299,], output)
mod['func_2342'] = func_2342
mod = relay.transform.InferType()(mod)
var_2343 = relay.var("var_2343", dtype = "int8", shape = (3, 9, 2))#candidate|2343|(3, 9, 2)|var|int8
var_2344 = relay.var("var_2344", dtype = "int8", shape = (3, 9, 2))#candidate|2344|(3, 9, 2)|var|int8
output = func_2342(var_2343,var_2344,)
func_2345 = relay.Function([var_2343,var_2344,], output)
mutated_mod['func_2345'] = func_2345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1285_call = mod.get_global_var('func_1285')
func_1287_call = mutated_mod.get_global_var('func_1287')
call_2358 = func_1285_call()
call_2359 = func_1285_call()
output = relay.Tuple([call_2358,])
output2 = relay.Tuple([call_2359,])
func_2361 = relay.Function([], output)
mod['func_2361'] = func_2361
mod = relay.transform.InferType()(mod)
output = func_2361()
func_2362 = relay.Function([], output)
mutated_mod['func_2362'] = func_2362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1067_call = mod.get_global_var('func_1067')
func_1069_call = mutated_mod.get_global_var('func_1069')
call_2404 = relay.TupleGetItem(func_1067_call(), 1)
call_2405 = relay.TupleGetItem(func_1069_call(), 1)
func_472_call = mod.get_global_var('func_472')
func_475_call = mutated_mod.get_global_var('func_475')
var_2409 = relay.var("var_2409", dtype = "float64", shape = (156, 1))#candidate|2409|(156, 1)|var|float64
call_2408 = relay.TupleGetItem(func_472_call(relay.reshape(var_2409.astype('float64'), [4, 13, 3])), 0)
call_2410 = relay.TupleGetItem(func_475_call(relay.reshape(var_2409.astype('float64'), [4, 13, 3])), 0)
func_1462_call = mod.get_global_var('func_1462')
func_1463_call = mutated_mod.get_global_var('func_1463')
call_2416 = func_1462_call()
call_2417 = func_1462_call()
var_2444 = relay.var("var_2444", dtype = "bool", shape = (14, 12, 2))#candidate|2444|(14, 12, 2)|var|bool
bop_2445 = relay.greater_equal(call_2416.astype('bool'), var_2444.astype('bool')) # shape=(14, 12, 2)
bop_2448 = relay.greater_equal(call_2417.astype('bool'), var_2444.astype('bool')) # shape=(14, 12, 2)
output = relay.Tuple([call_2404,call_2408,var_2409,bop_2445,])
output2 = relay.Tuple([call_2405,call_2410,var_2409,bop_2448,])
func_2449 = relay.Function([var_2409,var_2444,], output)
mod['func_2449'] = func_2449
mod = relay.transform.InferType()(mod)
var_2450 = relay.var("var_2450", dtype = "float64", shape = (156, 1))#candidate|2450|(156, 1)|var|float64
var_2451 = relay.var("var_2451", dtype = "bool", shape = (14, 12, 2))#candidate|2451|(14, 12, 2)|var|bool
output = func_2449(var_2450,var_2451,)
func_2452 = relay.Function([var_2450,var_2451,], output)
mutated_mod['func_2452'] = func_2452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1067_call = mod.get_global_var('func_1067')
func_1069_call = mutated_mod.get_global_var('func_1069')
call_2572 = relay.TupleGetItem(func_1067_call(), 1)
call_2573 = relay.TupleGetItem(func_1069_call(), 1)
output = relay.Tuple([call_2572,])
output2 = relay.Tuple([call_2573,])
func_2577 = relay.Function([], output)
mod['func_2577'] = func_2577
mod = relay.transform.InferType()(mod)
output = func_2577()
func_2578 = relay.Function([], output)
mutated_mod['func_2578'] = func_2578
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1472_call = mod.get_global_var('func_1472')
func_1473_call = mutated_mod.get_global_var('func_1473')
call_2681 = func_1472_call()
call_2682 = func_1472_call()
output = call_2681
output2 = call_2682
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
func_1067_call = mod.get_global_var('func_1067')
func_1069_call = mutated_mod.get_global_var('func_1069')
call_2763 = relay.TupleGetItem(func_1067_call(), 0)
call_2764 = relay.TupleGetItem(func_1069_call(), 0)
output = relay.Tuple([call_2763,])
output2 = relay.Tuple([call_2764,])
func_2773 = relay.Function([], output)
mod['func_2773'] = func_2773
mod = relay.transform.InferType()(mod)
mutated_mod['func_2773'] = func_2773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2773_call = mutated_mod.get_global_var('func_2773')
call_2774 = func_2773_call()
output = call_2774
func_2775 = relay.Function([], output)
mutated_mod['func_2775'] = func_2775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1285_call = mod.get_global_var('func_1285')
func_1287_call = mutated_mod.get_global_var('func_1287')
call_2807 = func_1285_call()
call_2808 = func_1285_call()
func_1067_call = mod.get_global_var('func_1067')
func_1069_call = mutated_mod.get_global_var('func_1069')
call_2810 = relay.TupleGetItem(func_1067_call(), 1)
call_2811 = relay.TupleGetItem(func_1069_call(), 1)
func_517_call = mod.get_global_var('func_517')
func_518_call = mutated_mod.get_global_var('func_518')
call_2812 = func_517_call()
call_2813 = func_517_call()
bop_2814 = relay.floor_mod(call_2812.astype('float32'), relay.reshape(call_2807.astype('float32'), relay.shape_of(call_2812))) # shape=(1, 12, 2)
bop_2817 = relay.floor_mod(call_2813.astype('float32'), relay.reshape(call_2808.astype('float32'), relay.shape_of(call_2813))) # shape=(1, 12, 2)
func_2135_call = mod.get_global_var('func_2135')
func_2138_call = mutated_mod.get_global_var('func_2138')
var_2819 = relay.var("var_2819", dtype = "float64", shape = (72,))#candidate|2819|(72,)|var|float64
call_2818 = relay.TupleGetItem(func_2135_call(relay.reshape(var_2819.astype('float64'), [1, 72])), 1)
call_2820 = relay.TupleGetItem(func_2138_call(relay.reshape(var_2819.astype('float64'), [1, 72])), 1)
output = relay.Tuple([call_2810,bop_2814,call_2818,var_2819,])
output2 = relay.Tuple([call_2811,bop_2817,call_2820,var_2819,])
func_2824 = relay.Function([var_2819,], output)
mod['func_2824'] = func_2824
mod = relay.transform.InferType()(mod)
mutated_mod['func_2824'] = func_2824
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2825 = relay.var("var_2825", dtype = "float64", shape = (72,))#candidate|2825|(72,)|var|float64
func_2824_call = mutated_mod.get_global_var('func_2824')
call_2826 = func_2824_call(var_2825)
output = call_2826
func_2827 = relay.Function([var_2825], output)
mutated_mod['func_2827'] = func_2827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_585_call = mod.get_global_var('func_585')
func_586_call = mutated_mod.get_global_var('func_586')
call_2874 = relay.TupleGetItem(func_585_call(), 0)
call_2875 = relay.TupleGetItem(func_586_call(), 0)
output = relay.Tuple([call_2874,])
output2 = relay.Tuple([call_2875,])
func_2882 = relay.Function([], output)
mod['func_2882'] = func_2882
mod = relay.transform.InferType()(mod)
output = func_2882()
func_2883 = relay.Function([], output)
mutated_mod['func_2883'] = func_2883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1285_call = mod.get_global_var('func_1285')
func_1287_call = mutated_mod.get_global_var('func_1287')
call_2910 = func_1285_call()
call_2911 = func_1285_call()
func_2683_call = mod.get_global_var('func_2683')
func_2685_call = mutated_mod.get_global_var('func_2685')
call_2913 = func_2683_call()
call_2914 = func_2683_call()
func_2773_call = mod.get_global_var('func_2773')
func_2775_call = mutated_mod.get_global_var('func_2775')
call_2916 = relay.TupleGetItem(func_2773_call(), 0)
call_2917 = relay.TupleGetItem(func_2775_call(), 0)
output = relay.Tuple([call_2910,call_2913,call_2916,])
output2 = relay.Tuple([call_2911,call_2914,call_2917,])
func_2920 = relay.Function([], output)
mod['func_2920'] = func_2920
mod = relay.transform.InferType()(mod)
mutated_mod['func_2920'] = func_2920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2920_call = mutated_mod.get_global_var('func_2920')
call_2921 = func_2920_call()
output = call_2921
func_2922 = relay.Function([], output)
mutated_mod['func_2922'] = func_2922
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3060 = relay.var("var_3060", dtype = "float32", shape = (8, 3, 4))#candidate|3060|(8, 3, 4)|var|float32
var_3061 = relay.var("var_3061", dtype = "float32", shape = (8, 3, 4))#candidate|3061|(8, 3, 4)|var|float32
bop_3062 = relay.mod(var_3060.astype('float32'), relay.reshape(var_3061.astype('float32'), relay.shape_of(var_3060))) # shape=(8, 3, 4)
func_1360_call = mod.get_global_var('func_1360')
func_1361_call = mutated_mod.get_global_var('func_1361')
call_3081 = relay.TupleGetItem(func_1360_call(), 0)
call_3082 = relay.TupleGetItem(func_1361_call(), 0)
var_3089 = relay.var("var_3089", dtype = "float32", shape = (8, 3, 4))#candidate|3089|(8, 3, 4)|var|float32
bop_3090 = relay.bitwise_or(var_3061.astype('int32'), relay.reshape(var_3089.astype('int32'), relay.shape_of(var_3061))) # shape=(8, 3, 4)
func_444_call = mod.get_global_var('func_444')
func_446_call = mutated_mod.get_global_var('func_446')
call_3094 = relay.TupleGetItem(func_444_call(), 0)
call_3095 = relay.TupleGetItem(func_446_call(), 0)
output = relay.Tuple([bop_3062,call_3081,bop_3090,call_3094,])
output2 = relay.Tuple([bop_3062,call_3082,bop_3090,call_3095,])
func_3096 = relay.Function([var_3060,var_3061,var_3089,], output)
mod['func_3096'] = func_3096
mod = relay.transform.InferType()(mod)
mutated_mod['func_3096'] = func_3096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3096_call = mutated_mod.get_global_var('func_3096')
var_3098 = relay.var("var_3098", dtype = "float32", shape = (8, 3, 4))#candidate|3098|(8, 3, 4)|var|float32
var_3099 = relay.var("var_3099", dtype = "float32", shape = (8, 3, 4))#candidate|3099|(8, 3, 4)|var|float32
var_3100 = relay.var("var_3100", dtype = "float32", shape = (8, 3, 4))#candidate|3100|(8, 3, 4)|var|float32
call_3097 = func_3096_call(var_3098,var_3099,var_3100,)
output = call_3097
func_3101 = relay.Function([var_3098,var_3099,var_3100,], output)
mutated_mod['func_3101'] = func_3101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2920_call = mod.get_global_var('func_2920')
func_2922_call = mutated_mod.get_global_var('func_2922')
call_3117 = relay.TupleGetItem(func_2920_call(), 1)
call_3118 = relay.TupleGetItem(func_2922_call(), 1)
output = call_3117
output2 = call_3118
func_3138 = relay.Function([], output)
mod['func_3138'] = func_3138
mod = relay.transform.InferType()(mod)
mutated_mod['func_3138'] = func_3138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3138_call = mutated_mod.get_global_var('func_3138')
call_3139 = func_3138_call()
output = call_3139
func_3140 = relay.Function([], output)
mutated_mod['func_3140'] = func_3140
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3187 = relay.const([[[-3],[5],[7],[-1],[1],[7],[-6],[-7],[2],[7],[1],[-8]],[[2],[9],[-6],[-3],[-9],[10],[10],[-1],[5],[-3],[2],[3]],[[5],[4],[8],[6],[5],[-8],[-8],[-2],[1],[-5],[5],[10]],[[-5],[1],[4],[-1],[-6],[5],[-9],[5],[-8],[7],[-6],[-3]],[[10],[8],[3],[5],[2],[5],[-2],[4],[-5],[3],[4],[10]],[[-3],[-8],[-5],[-5],[-6],[-10],[10],[6],[3],[-9],[10],[-4]],[[-6],[1],[-5],[10],[7],[6],[-8],[4],[-6],[4],[2],[-10]],[[-3],[-2],[4],[-10],[-5],[8],[1],[9],[-7],[-7],[-7],[-2]],[[7],[-9],[-8],[-4],[7],[6],[5],[4],[6],[-9],[2],[-2]],[[-2],[8],[9],[-2],[-6],[5],[-1],[-4],[8],[2],[7],[-3]],[[-7],[-7],[-10],[-2],[9],[-4],[7],[-3],[9],[6],[-9],[-8]],[[2],[8],[5],[-10],[4],[3],[-8],[8],[4],[6],[-10],[-6]]], dtype = "int64")#candidate|3187|(12, 12, 1)|const|int64
var_3188 = relay.var("var_3188", dtype = "int64", shape = (12, 12, 8))#candidate|3188|(12, 12, 8)|var|int64
bop_3189 = relay.bitwise_xor(const_3187.astype('int64'), var_3188.astype('int64')) # shape=(12, 12, 8)
func_1360_call = mod.get_global_var('func_1360')
func_1361_call = mutated_mod.get_global_var('func_1361')
call_3198 = relay.TupleGetItem(func_1360_call(), 2)
call_3199 = relay.TupleGetItem(func_1361_call(), 2)
output = relay.Tuple([bop_3189,call_3198,])
output2 = relay.Tuple([bop_3189,call_3199,])
func_3221 = relay.Function([var_3188,], output)
mod['func_3221'] = func_3221
mod = relay.transform.InferType()(mod)
mutated_mod['func_3221'] = func_3221
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3222 = relay.var("var_3222", dtype = "int64", shape = (12, 12, 8))#candidate|3222|(12, 12, 8)|var|int64
func_3221_call = mutated_mod.get_global_var('func_3221')
call_3223 = func_3221_call(var_3222)
output = call_3223
func_3224 = relay.Function([var_3222], output)
mutated_mod['func_3224'] = func_3224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_585_call = mod.get_global_var('func_585')
func_586_call = mutated_mod.get_global_var('func_586')
call_3265 = relay.TupleGetItem(func_585_call(), 0)
call_3266 = relay.TupleGetItem(func_586_call(), 0)
func_3138_call = mod.get_global_var('func_3138')
func_3140_call = mutated_mod.get_global_var('func_3140')
call_3291 = func_3138_call()
call_3292 = func_3138_call()
func_1327_call = mod.get_global_var('func_1327')
func_1329_call = mutated_mod.get_global_var('func_1329')
const_3309 = relay.const([[4,8,1,-3,-6,10,7,-6],[6,-10,6,-7,-6,2,-6,4],[-8,3,2,4,-4,8,2,8],[9,-4,-10,5,7,-8,2,2],[6,-9,1,8,10,1,-9,1],[6,3,4,4,5,-8,-3,9],[8,-8,3,-8,-10,-4,5,7],[1,-7,-7,-8,-2,1,7,-3],[-8,-5,8,4,2,7,5,9],[3,1,-9,-4,5,4,-5,-8],[1,4,7,-7,9,-6,-9,8],[-3,4,8,-10,-3,-7,-3,-3],[-8,-2,-6,6,5,10,7,8],[9,-9,-1,-9,3,-5,1,-1],[-7,-6,1,8,1,2,8,-7],[3,3,7,10,-10,-8,-3,1],[-1,-2,-6,10,2,5,-3,6],[-10,-10,5,-7,-5,7,6,-7],[-5,-1,1,8,5,-3,8,2],[10,-5,2,-1,10,4,-6,-3],[1,-1,5,-8,-5,-9,-2,-10],[-5,-7,-10,-5,-6,4,-1,2],[1,6,3,8,-5,-10,2,-9],[-7,-5,5,-7,2,-5,-8,-6],[-10,-7,-8,-2,4,2,-2,-4],[-9,7,-10,7,6,4,6,-7],[4,-3,10,5,-5,-1,-8,-9],[-3,-1,9,-4,7,-2,-10,3],[-2,-6,10,-6,6,6,-10,1],[9,8,-9,6,-2,10,7,8],[10,10,3,4,3,5,5,9],[-9,4,9,3,8,5,-7,-5],[-5,6,2,1,-2,-9,4,2],[4,1,-6,7,8,-9,5,3],[-8,-1,-2,4,-1,-2,-4,8],[8,1,6,8,-2,-2,-1,-8],[-5,-9,-1,1,-9,-7,-7,1],[6,9,-2,7,-8,-10,3,9],[-4,5,3,-7,10,3,9,-3],[8,9,3,-3,-3,9,10,4],[-6,9,-8,2,-10,-7,9,-6],[-4,-6,-8,-7,3,-7,-5,6],[3,-1,-2,10,7,3,-7,-4],[1,-9,10,-2,-3,-3,3,10],[-5,-6,3,10,-5,-6,9,3],[-10,3,-10,3,7,2,5,5],[-4,-8,-8,6,9,-6,-4,10],[-3,5,9,7,-4,-3,2,1],[-10,-2,5,-4,2,5,-10,1],[10,-9,4,3,6,8,-6,5],[-6,-6,6,7,9,5,9,-3],[10,5,9,-1,-8,4,-8,1],[7,-6,7,-1,5,6,-10,2],[10,-5,9,-5,-6,10,7,7],[1,6,-7,4,3,-6,8,6],[-7,-8,-6,3,1,6,-7,1],[4,-5,4,-3,-9,3,-8,9],[9,-4,-10,9,-2,-9,-5,6],[8,2,-3,3,5,3,-3,3],[-10,7,3,9,-10,-6,-1,-8],[-6,-2,-5,-4,1,4,-10,7],[3,7,-1,-3,9,8,2,8],[6,8,7,10,1,-3,2,-10],[6,-10,6,-10,3,-4,3,4],[3,9,-5,-1,6,7,6,2],[7,-8,7,9,-5,-4,4,-8],[-1,-1,9,-3,6,2,1,3],[-5,-2,-9,2,-3,-2,6,6],[-10,-4,-6,3,-10,3,6,9],[7,4,10,9,2,-2,5,6],[4,-4,10,2,10,-1,-1,8],[2,1,-7,7,4,-8,5,4],[-7,-10,6,8,9,-4,10,6],[5,-5,-10,2,10,-4,-7,6],[7,-2,10,-10,-1,-9,8,4],[7,-6,10,4,1,4,-6,-3],[-8,7,6,9,2,8,-5,3],[-2,10,6,-1,-2,4,-7,3],[3,3,9,-7,-10,-1,9,-1],[-3,-4,-7,-8,2,-8,-1,4],[3,5,9,-3,9,6,-9,1],[-9,3,-10,4,-4,-10,-5,3],[4,-10,-10,-2,8,-6,-6,-1],[2,1,-4,5,-7,-7,1,-10],[7,-6,4,5,7,-1,10,9],[5,-5,5,8,-5,4,-4,1],[-6,-8,6,-4,-7,-7,6,-9],[6,-1,2,-2,-4,-4,-5,-10],[1,-1,1,3,8,-5,8,7],[-5,-4,8,5,6,-2,4,10],[-2,-4,4,-3,7,-1,1,6],[4,5,8,6,1,3,-2,1],[-3,8,-10,4,-10,-2,-10,-9],[10,8,5,-4,-2,10,-1,9],[-5,5,-10,5,-1,1,7,8],[3,7,-10,4,9,7,6,8],[-4,9,10,-2,-10,2,2,-5],[6,2,-5,1,10,-6,5,-10],[-4,3,-10,5,-9,-7,9,-5],[-4,-4,-1,2,4,-10,9,7],[6,9,4,-7,-3,3,4,8],[3,6,-6,9,-6,8,-8,3],[5,-3,-6,-2,-5,-2,1,9],[-3,-1,-5,8,9,9,8,-5],[-3,-2,7,9,-6,-10,-10,-2],[6,-1,-4,-4,-2,-2,6,5],[-6,-8,8,-6,8,-3,7,-1],[-1,-3,3,9,2,-8,-1,-8],[8,1,-3,2,4,-10,-3,3],[-7,-2,-6,6,6,-8,6,5],[2,-2,2,-6,1,7,-9,9],[-9,-4,2,6,-5,5,10,5],[-6,1,-1,4,5,6,-4,-9],[6,9,-5,-7,9,2,-2,3],[2,-7,3,4,5,-1,5,-1],[5,-8,-4,1,-9,-3,9,-10],[-2,-3,10,-2,-7,3,2,2],[1,8,-7,9,3,8,1,-3],[6,-9,-5,-1,-3,6,-8,3],[-2,-7,3,6,1,7,1,7],[6,-4,-7,7,9,7,4,9],[2,-5,-3,10,3,5,7,-9],[-8,-6,-8,-4,6,6,-3,6],[-4,-10,-9,2,10,-6,-9,-2],[10,9,10,-8,-7,8,1,5],[2,2,-10,5,-2,-8,8,8],[-7,9,-4,-8,1,-1,8,8],[3,-3,-6,4,-1,-1,-10,8],[-7,7,-2,-2,-10,5,-1,10],[-5,-9,-3,-3,5,3,4,-3],[8,2,-6,1,9,6,1,6],[-2,10,-7,-10,-6,8,-4,-1],[-4,2,-9,-7,-1,10,10,-9],[-10,8,2,10,10,-8,-8,9],[-3,-1,4,-3,-1,-8,-7,-3],[-7,-4,8,-7,-1,-5,5,2],[-4,2,-3,4,8,-6,10,1],[8,-4,-1,-5,7,1,3,-2],[6,-5,-1,-2,-1,-5,8,6],[-3,-2,-5,-5,8,-6,9,8],[-4,-4,-1,5,5,-3,-5,-8],[-1,-3,1,9,-5,-2,5,-2],[2,5,4,-5,1,3,7,6],[-6,-6,-6,8,-10,-8,10,-3],[5,6,-9,10,9,7,5,-5],[10,-7,8,10,6,2,-7,8],[6,-1,7,6,5,3,5,-2],[-1,5,-6,7,4,-8,6,-3],[2,-7,5,6,-7,1,-8,10],[2,1,2,-10,7,9,5,-8],[-6,-7,-10,-3,1,10,-5,-1],[6,6,9,-6,5,-4,7,-9],[-6,-6,-9,-5,2,-10,-6,7],[2,-3,1,-9,-5,9,4,-7],[-4,9,1,-4,9,-4,-6,10],[4,10,3,2,-4,-9,6,-9],[8,-4,1,-6,3,-9,10,-6],[3,8,7,3,8,8,-10,6],[6,-1,-9,1,-6,10,8,-10],[4,-6,-7,-2,4,1,-8,4],[-9,3,3,-2,4,4,-10,4],[2,4,-10,-4,-6,-8,4,-10],[-6,-4,1,-7,2,7,-6,7],[-1,-7,9,3,8,2,3,8],[-9,8,10,4,-9,-5,2,-2],[3,1,-3,-9,-6,-5,-7,8],[-7,5,-4,-9,-10,9,-6,-2],[-2,-3,9,-8,-5,4,7,-9],[10,2,-2,8,-7,3,-8,2],[-2,-5,-9,8,5,9,5,6],[1,-1,3,9,6,1,1,-4],[-2,-3,-1,6,-6,9,2,-9],[7,10,-1,8,-10,-3,-6,-3],[-7,9,9,7,-2,-9,6,-9],[-9,-3,-7,10,-1,10,2,-6],[-2,-1,2,-8,-6,1,2,3],[1,4,8,-7,8,8,1,-3],[1,-5,1,1,8,-7,4,-4],[7,-4,3,-6,1,1,8,-6],[-7,3,-2,-5,-8,5,-4,6]], dtype = "int8")#candidate|3309|(180, 8)|const|int8
call_3308 = relay.TupleGetItem(func_1327_call(relay.reshape(const_3309.astype('int8'), [1440,])), 2)
call_3310 = relay.TupleGetItem(func_1329_call(relay.reshape(const_3309.astype('int8'), [1440,])), 2)
func_585_call = mod.get_global_var('func_585')
func_586_call = mutated_mod.get_global_var('func_586')
call_3316 = relay.TupleGetItem(func_585_call(), 1)
call_3317 = relay.TupleGetItem(func_586_call(), 1)
output = relay.Tuple([call_3265,call_3291,call_3308,const_3309,call_3316,])
output2 = relay.Tuple([call_3266,call_3292,call_3310,const_3309,call_3317,])
func_3326 = relay.Function([], output)
mod['func_3326'] = func_3326
mod = relay.transform.InferType()(mod)
mutated_mod['func_3326'] = func_3326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3326_call = mutated_mod.get_global_var('func_3326')
call_3327 = func_3326_call()
output = call_3327
func_3328 = relay.Function([], output)
mutated_mod['func_3328'] = func_3328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2920_call = mod.get_global_var('func_2920')
func_2922_call = mutated_mod.get_global_var('func_2922')
call_3346 = relay.TupleGetItem(func_2920_call(), 1)
call_3347 = relay.TupleGetItem(func_2922_call(), 1)
output = call_3346
output2 = call_3347
func_3356 = relay.Function([], output)
mod['func_3356'] = func_3356
mod = relay.transform.InferType()(mod)
output = func_3356()
func_3357 = relay.Function([], output)
mutated_mod['func_3357'] = func_3357
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2773_call = mod.get_global_var('func_2773')
func_2775_call = mutated_mod.get_global_var('func_2775')
call_3412 = relay.TupleGetItem(func_2773_call(), 0)
call_3413 = relay.TupleGetItem(func_2775_call(), 0)
output = relay.Tuple([call_3412,])
output2 = relay.Tuple([call_3413,])
func_3419 = relay.Function([], output)
mod['func_3419'] = func_3419
mod = relay.transform.InferType()(mod)
output = func_3419()
func_3420 = relay.Function([], output)
mutated_mod['func_3420'] = func_3420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1127_call = mod.get_global_var('func_1127')
func_1129_call = mutated_mod.get_global_var('func_1129')
call_3432 = relay.TupleGetItem(func_1127_call(), 0)
call_3433 = relay.TupleGetItem(func_1129_call(), 0)
output = relay.Tuple([call_3432,])
output2 = relay.Tuple([call_3433,])
func_3449 = relay.Function([], output)
mod['func_3449'] = func_3449
mod = relay.transform.InferType()(mod)
output = func_3449()
func_3450 = relay.Function([], output)
mutated_mod['func_3450'] = func_3450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1472_call = mod.get_global_var('func_1472')
func_1473_call = mutated_mod.get_global_var('func_1473')
call_3559 = func_1472_call()
call_3560 = func_1472_call()
func_2577_call = mod.get_global_var('func_2577')
func_2578_call = mutated_mod.get_global_var('func_2578')
call_3585 = relay.TupleGetItem(func_2577_call(), 0)
call_3586 = relay.TupleGetItem(func_2578_call(), 0)
bop_3589 = relay.not_equal(call_3585.astype('bool'), relay.reshape(call_3559.astype('bool'), relay.shape_of(call_3585))) # shape=(1, 12, 2)
bop_3592 = relay.not_equal(call_3586.astype('bool'), relay.reshape(call_3560.astype('bool'), relay.shape_of(call_3586))) # shape=(1, 12, 2)
func_3356_call = mod.get_global_var('func_3356')
func_3357_call = mutated_mod.get_global_var('func_3357')
call_3598 = func_3356_call()
call_3599 = func_3356_call()
var_3600 = relay.var("var_3600", dtype = "float32", shape = (11, 12, 2))#candidate|3600|(11, 12, 2)|var|float32
bop_3601 = relay.greater_equal(call_3585.astype('bool'), var_3600.astype('bool')) # shape=(11, 12, 2)
bop_3604 = relay.greater_equal(call_3586.astype('bool'), var_3600.astype('bool')) # shape=(11, 12, 2)
output = relay.Tuple([bop_3589,call_3598,bop_3601,])
output2 = relay.Tuple([bop_3592,call_3599,bop_3604,])
func_3626 = relay.Function([var_3600,], output)
mod['func_3626'] = func_3626
mod = relay.transform.InferType()(mod)
var_3627 = relay.var("var_3627", dtype = "float32", shape = (11, 12, 2))#candidate|3627|(11, 12, 2)|var|float32
output = func_3626(var_3627)
func_3628 = relay.Function([var_3627], output)
mutated_mod['func_3628'] = func_3628
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3637 = relay.const([[[4.292069,3.635135,4.489433,-2.900121,-5.771733,-8.812928,6.600635,-9.957502,2.307165,-1.201954,2.759660,8.753447],[1.535110,5.241588,-8.289129,4.129865,8.882211,9.863340,6.882849,4.478045,-7.940801,6.114274,8.541547,5.726932],[2.534110,7.033431,-9.394370,-7.447275,-8.507236,4.991413,-4.402304,1.223547,2.821199,-6.530085,-0.075318,-8.570237],[4.780983,-3.965034,-6.434209,7.129675,-5.612033,-8.895830,-3.026535,-7.164581,7.926969,1.535641,-0.255260,2.429456],[2.154413,-5.098763,0.880319,-9.399884,9.414149,6.101246,-5.883754,8.650330,-2.355291,-7.290229,-4.279712,7.383271],[-5.363109,-8.813735,1.541056,3.772360,7.577451,-8.976442,-2.611102,-4.069762,-9.735341,2.434695,-8.448135,2.995225],[5.896476,9.564471,-9.893151,1.691360,-4.683169,-2.028757,9.348355,-3.154144,1.704192,-9.469981,-8.684176,8.597857],[-5.024199,3.165518,-6.539583,4.551502,-2.083691,1.845278,-4.376417,-1.757823,-0.238917,-3.839852,-5.640241,2.879224]]], dtype = "float64")#candidate|3637|(1, 8, 12)|const|float64
uop_3638 = relay.log2(const_3637.astype('float64')) # shape=(1, 8, 12)
bop_3649 = relay.multiply(uop_3638.astype('int64'), relay.reshape(const_3637.astype('int64'), relay.shape_of(uop_3638))) # shape=(1, 8, 12)
output = bop_3649
output2 = bop_3649
func_3660 = relay.Function([], output)
mod['func_3660'] = func_3660
mod = relay.transform.InferType()(mod)
mutated_mod['func_3660'] = func_3660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3660_call = mutated_mod.get_global_var('func_3660')
call_3661 = func_3660_call()
output = call_3661
func_3662 = relay.Function([], output)
mutated_mod['func_3662'] = func_3662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3356_call = mod.get_global_var('func_3356')
func_3357_call = mutated_mod.get_global_var('func_3357')
call_3678 = func_3356_call()
call_3679 = func_3356_call()
output = call_3678
output2 = call_3679
func_3715 = relay.Function([], output)
mod['func_3715'] = func_3715
mod = relay.transform.InferType()(mod)
mutated_mod['func_3715'] = func_3715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3715_call = mutated_mod.get_global_var('func_3715')
call_3716 = func_3715_call()
output = call_3716
func_3717 = relay.Function([], output)
mutated_mod['func_3717'] = func_3717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3419_call = mod.get_global_var('func_3419')
func_3420_call = mutated_mod.get_global_var('func_3420')
call_3766 = relay.TupleGetItem(func_3419_call(), 0)
call_3767 = relay.TupleGetItem(func_3420_call(), 0)
func_3660_call = mod.get_global_var('func_3660')
func_3662_call = mutated_mod.get_global_var('func_3662')
call_3768 = func_3660_call()
call_3769 = func_3660_call()
var_3776 = relay.var("var_3776", dtype = "int64", shape = (12, 8, 12))#candidate|3776|(12, 8, 12)|var|int64
bop_3777 = relay.add(call_3768.astype('int8'), var_3776.astype('int8')) # shape=(12, 8, 12)
bop_3780 = relay.add(call_3769.astype('int8'), var_3776.astype('int8')) # shape=(12, 8, 12)
uop_3786 = relay.sigmoid(bop_3777.astype('float64')) # shape=(12, 8, 12)
uop_3788 = relay.sigmoid(bop_3780.astype('float64')) # shape=(12, 8, 12)
func_3449_call = mod.get_global_var('func_3449')
func_3450_call = mutated_mod.get_global_var('func_3450')
call_3795 = relay.TupleGetItem(func_3449_call(), 0)
call_3796 = relay.TupleGetItem(func_3450_call(), 0)
func_1537_call = mod.get_global_var('func_1537')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_3804 = relay.TupleGetItem(func_1537_call(), 0)
call_3805 = relay.TupleGetItem(func_1539_call(), 0)
func_1462_call = mod.get_global_var('func_1462')
func_1463_call = mutated_mod.get_global_var('func_1463')
call_3806 = func_1462_call()
call_3807 = func_1462_call()
func_3221_call = mod.get_global_var('func_3221')
func_3224_call = mutated_mod.get_global_var('func_3224')
call_3821 = relay.TupleGetItem(func_3221_call(relay.reshape(var_3776.astype('int64'), [12, 12, 8])), 1)
call_3822 = relay.TupleGetItem(func_3224_call(relay.reshape(var_3776.astype('int64'), [12, 12, 8])), 1)
func_1067_call = mod.get_global_var('func_1067')
func_1069_call = mutated_mod.get_global_var('func_1069')
call_3826 = relay.TupleGetItem(func_1067_call(), 0)
call_3827 = relay.TupleGetItem(func_1069_call(), 0)
func_1202_call = mod.get_global_var('func_1202')
func_1203_call = mutated_mod.get_global_var('func_1203')
call_3831 = relay.TupleGetItem(func_1202_call(), 0)
call_3832 = relay.TupleGetItem(func_1203_call(), 0)
output = relay.Tuple([call_3766,uop_3786,call_3795,call_3804,call_3806,call_3821,call_3826,call_3831,])
output2 = relay.Tuple([call_3767,uop_3788,call_3796,call_3805,call_3807,call_3822,call_3827,call_3832,])
func_3843 = relay.Function([var_3776,], output)
mod['func_3843'] = func_3843
mod = relay.transform.InferType()(mod)
mutated_mod['func_3843'] = func_3843
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3844 = relay.var("var_3844", dtype = "int64", shape = (12, 8, 12))#candidate|3844|(12, 8, 12)|var|int64
func_3843_call = mutated_mod.get_global_var('func_3843')
call_3845 = func_3843_call(var_3844)
output = call_3845
func_3846 = relay.Function([var_3844], output)
mutated_mod['func_3846'] = func_3846
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3449_call = mod.get_global_var('func_3449')
func_3450_call = mutated_mod.get_global_var('func_3450')
call_3853 = relay.TupleGetItem(func_3449_call(), 0)
call_3854 = relay.TupleGetItem(func_3450_call(), 0)
const_3855 = relay.const([[[-8.627008,6.627061],[-3.334802,-3.861008],[-9.236521,8.079362],[-3.151471,-6.688811],[-0.517120,2.393362],[-2.593668,7.889355],[0.082469,5.127601],[3.663462,8.059119],[1.948519,-7.804536],[-6.510673,-6.807093],[-9.080580,2.931207],[7.120930,3.773562]],[[8.315495,-7.959870],[9.215332,-1.530021],[6.831503,0.635611],[-9.788407,-8.215536],[0.489162,7.503554],[-6.793476,8.993947],[-3.901293,3.750496],[-8.761803,4.696616],[6.739681,7.768607],[3.818157,-9.692883],[8.413388,5.719543],[-5.358241,-1.376487]],[[-2.114278,5.561738],[3.192017,1.828289],[-2.088481,9.343128],[-6.900371,-4.700723],[2.033151,-9.814180],[5.150225,4.113583],[-7.681947,8.555516],[8.364825,6.341227],[9.394520,-9.219822],[0.440757,-5.500220],[-5.647205,-8.806908],[3.312601,-9.071034]],[[8.715369,6.961093],[7.424384,2.504418],[-0.382548,1.662586],[-2.568215,1.036722],[1.914778,-5.727530],[-8.108273,-3.390823],[2.667457,8.584367],[9.442573,9.450914],[-2.087893,-0.017270],[7.686872,9.408301],[-0.972241,8.416776],[1.083225,-0.329479]],[[-8.007838,0.160707],[-6.239434,7.749624],[2.235441,-0.197611],[1.879287,8.324794],[-2.157447,7.192641],[9.900227,5.796258],[9.154607,2.867222],[-2.039011,-0.830532],[-8.507716,8.241591],[9.955579,-6.206203],[0.262647,-3.215334],[-7.055497,-5.710173]]], dtype = "float32")#candidate|3855|(5, 12, 2)|const|float32
bop_3856 = relay.bitwise_xor(call_3853.astype('uint16'), const_3855.astype('uint16')) # shape=(5, 12, 2)
bop_3859 = relay.bitwise_xor(call_3854.astype('uint16'), const_3855.astype('uint16')) # shape=(5, 12, 2)
func_2275_call = mod.get_global_var('func_2275')
func_2277_call = mutated_mod.get_global_var('func_2277')
const_3890 = relay.const([False,True,False,False,True,False,False,False,True,False,False,False,False,True,True,False,False,False,False,True,True,False,False,True,False,True,False,True,False,False,True,True,False,True,True,True,False,True,True,True,True,True,True,True,False,False,False,True,False,False,False,True,False,True,False,False,False,False,False,True,True,True,False,True,False,True,False,False,True,True,True,False,False,True,False,False,True,False,True,False,False,False,True,False,True,False,True,True,False,True,False,True,False,False,False,False,False,False,True,True,True,False,True,True,True,True,False,True,True,True,True,True,True,False,False,False,False,True,False,True,False,False,False,False,True,True,False,True,True,True,False,True,False,True,False,True,True,False,False,False,False,True,False,True,False,False,False,False,True,False,True,True,False,False,True,True,True,True,False,False,True,False,True,True,False,False,False,True], dtype = "bool")#candidate|3890|(168,)|const|bool
call_3889 = relay.TupleGetItem(func_2275_call(relay.reshape(const_3890.astype('bool'), [7, 12, 2])), 0)
call_3891 = relay.TupleGetItem(func_2277_call(relay.reshape(const_3890.astype('bool'), [7, 12, 2])), 0)
output = relay.Tuple([bop_3856,call_3889,const_3890,])
output2 = relay.Tuple([bop_3859,call_3891,const_3890,])
func_3895 = relay.Function([], output)
mod['func_3895'] = func_3895
mod = relay.transform.InferType()(mod)
mutated_mod['func_3895'] = func_3895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3895_call = mutated_mod.get_global_var('func_3895')
call_3896 = func_3895_call()
output = call_3896
func_3897 = relay.Function([], output)
mutated_mod['func_3897'] = func_3897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3419_call = mod.get_global_var('func_3419')
func_3420_call = mutated_mod.get_global_var('func_3420')
call_3956 = relay.TupleGetItem(func_3419_call(), 0)
call_3957 = relay.TupleGetItem(func_3420_call(), 0)
var_3971 = relay.var("var_3971", dtype = "int8", shape = (3, 12, 2))#candidate|3971|(3, 12, 2)|var|int8
bop_3972 = relay.add(call_3956.astype('uint8'), var_3971.astype('uint8')) # shape=(3, 12, 2)
bop_3975 = relay.add(call_3957.astype('uint8'), var_3971.astype('uint8')) # shape=(3, 12, 2)
func_2149_call = mod.get_global_var('func_2149')
func_2150_call = mutated_mod.get_global_var('func_2150')
call_3994 = relay.TupleGetItem(func_2149_call(), 0)
call_3995 = relay.TupleGetItem(func_2150_call(), 0)
output = relay.Tuple([bop_3972,call_3994,])
output2 = relay.Tuple([bop_3975,call_3995,])
func_4005 = relay.Function([var_3971,], output)
mod['func_4005'] = func_4005
mod = relay.transform.InferType()(mod)
mutated_mod['func_4005'] = func_4005
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4006 = relay.var("var_4006", dtype = "int8", shape = (3, 12, 2))#candidate|4006|(3, 12, 2)|var|int8
func_4005_call = mutated_mod.get_global_var('func_4005')
call_4007 = func_4005_call(var_4006)
output = call_4007
func_4008 = relay.Function([var_4006], output)
mutated_mod['func_4008'] = func_4008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3419_call = mod.get_global_var('func_3419')
func_3420_call = mutated_mod.get_global_var('func_3420')
call_4063 = relay.TupleGetItem(func_3419_call(), 0)
call_4064 = relay.TupleGetItem(func_3420_call(), 0)
func_3449_call = mod.get_global_var('func_3449')
func_3450_call = mutated_mod.get_global_var('func_3450')
call_4086 = relay.TupleGetItem(func_3449_call(), 0)
call_4087 = relay.TupleGetItem(func_3450_call(), 0)
func_2078_call = mod.get_global_var('func_2078')
func_2081_call = mutated_mod.get_global_var('func_2081')
const_4097 = relay.const([-7,-1,-5,-7,-7,1,-9,-7,7,5,1,-3,8,1,1,5,-1,7,3,9,8,-5,2,-5,10,-6,-9,8,-1,7,1,10,-6,-9,4,8,1,8,-7,-2,-2,8,9,1,4,-2,7,10,2,4,-9,-7,-6,-4,9,-2,4,2,-7,-3,-10,8,8,1,-7,-3,7,-9,-6,-8,8,-8,9,4,-5,-6,2,10,-2,-8,-8,-9,5,-8,10,-8,3,1,-7,7,-1,-5,-5,-3,-8,7,-3,10,4,-1,-3,5,6,-9,8,-3,9,4,-2,10,-7,5,3,10,-5,-4,-1,-8,2,7,3,10,7,5,-10,-9,-4,-7,-2,-4,9,5,6,4,-1,9,1,6,-3,7,-8,10,-1,-8,-5,9,-2,-1,-8,-6,6,-2,5,2,1,-3,6,-2,10,1,6,-9,-4,7,-5,-8,-8,-7,10,-3,1,-3,-9,5,7,-5,5,1,4,1,1,-10,10,4,-9,5,10,8,-3,1,10,-4,9,4,5,5,-7,-7,-4,-8,-7,-2,9,8,-2,3,-4,7,-6,9,8,-9,8,-3,8,-7,4,-2,9,6,-7,-5,10,4,-5,-5,-8,-10,-2,-1,4,-5,-5,-1,5,10,-10,4,-7,4,-3,6,5,8,-9,-10,-6,1,-10,-8,2,10,2,-2,4,10,-6,1,-4,-3,-7,-6,-7,-4,9,-5,-1,5,-9,-2,-2,2,-1,-1,1,8,8,3,-10,4,1,10,-4,-5,3,-8,2,-5,3,9,-2,4,-10,-5,3,10,9,-6,-7,6,8,5,3,4,7,-2,10,-1,2,-3,-5,9,-4,-7,-5,3,8,-5,9,9,-3,-7,8,7,3,-4,-4,-4,-7,-1,3,-8,-3,2,-2,-10,-3,-2,-6,-8,7,-1,5,9,-6,4,6,2,3,-5,-4,-2,3,-7,-2,-2,-7,10,-10,-3,3,6,7,1,2,7,-3,7,4,7,-9,5,-5,9,7,-10,7,-10,-5,-6,-8,-7,1,-7,7,9,6,-1,10,-4,2,-5,-1,-3,7,5,2,6,-7,-8,-8,10,2,3,-1,-7,3,2,-1,10,6,-5,1,-2,6,-3,-9,-8,-4,3,10,-8,3,6,-7,-4,-6,-1,-2,-5,5,3,-1,-4,-6,10,-6,10,6,-3,-4,8,-6,7,4,-6,-2,-2,4,7,1,-7,-6,6,4,-7,-8,10,-3,-4,3,-5,-3,-9,3,6,-3,-10,-1,-1,10,5,2,-6,4,-10,-1,1,2,-10,8,-8,10,-10,-8,8,-10,6,2,-6,1,5,-1,-8,8,7,-6,7,-6,-9,-9,-10,3,2,9,2,-4,-4,5,7,1,-7,2,3,2,-2,-10,-9,-10,8,9,-1,-9,5,6,7,-9,-4,-10,-8,-10,1,-3,-5,-3,2,7,4,-8,-9,-2,-4,3,-1,9,-3,-8,-3,9,3,2,-4,1,-4,7,-5,-2,-2,-1,7,-10,10,-7,10,10,-7,-1,1,1,2,1,-10,10,-7,3,-2,-2,-3,-5,6,6,-10,-6,-10,-8,-8,-2,1,10,-3,-2,8,-7,-5,-3,2,4,-8,-4,-1,3,-5,-8,4,-4,1,-4,-10,-1,5,-5,5,10,-2,-6,-9,2,1,-10,-8,-4,2,9,10,8,3,-4,-5,-6,9,9,8,-1,1,-5,-8,9,8,-2,7,-4,5,3,-2,-6,10,6,9,6,-9,-1,2,6,8,-8,10,-7,10,5,-8,1,-6,-5,-6,-5,4,3,7,-7,7,-2,-7,-10,-1,-9,5,7,8,-8,-7,-1,-10,8,-4,-4,10,6,7,4,-2,-8,-2,-10,-1,9,1,8,6,9,-10,-1,-9,6,6,5,-3,-4,-2,-9,3,8,8,7,1,-4,-9,9,-3,-7,7,6,6,6,4,-8,1,-3,1,5,-6,-3,7,4,-9,8,2,5,-3,6,6,6,-2,-8,-9,-7,5,9,-3,1,-3,-9,10,2,7,-1,-2,10,-6,-8,-5,-1,4,2,2,-9,-10,-9,-4,-4,-1,-4,1,-8,4,5,9,-10,5,-10,3,3,10,6,5,5,-4,-8,2,-6,-9,6,7,5,-7,-9,4,6,4,-8,-1,-2,1,-3,-5,1,-2,-6,-2,8,-5,10,9,-5,-9,9,-7,6,-2,-3,8,2,1,-6,8,4,3,5,1,2,-3,7,-5,-8,-2,5,-4,-9,-7,-10,2,-10,-8,-6,3,7,10,-7,-9,-3,5,2,-5,4,7,-8,-6,2,3,2,-8,3,-5,5,5,-6,4,-10,8,-2,10,3,-8,9,-5,-7,-2,-10,-3,2,3,-8,5,-7,-4,1,10,-9,1,10,-2,10,9,10,7,8,9,6,-4,10,-5,-3,5,3,-1,-3,-10,-7,-2,-1,-7,8,4,2,8,-9,1,8,-3,1,4,9,6,2,-2,-7,-1,7,-9,-7,-2,-2,6,10,-10,7,6,9,1,10,-4,4,-1,1,3,9,-4,-8,-10,2,-1,8,-5,9,-6,-1,7,-6,-10,8,-6,-9,-7,-1,-7,-1,-3,8,-5,6,-6,-2,4,-1,6,8,-8,2,-3,-4,-7,-1,-5,-8,5,-10,1,-6,-1,-9,-8,-8,-3,-2,3,-9,1,3,-10,-6,5,8,9,2,2,-8,-10,7,-9,2,-4,-4,-2,3,-6,-8,5,10,3,6,5,6,-2,-1,-1,-3,-5,-10,-2,10,9,2,8,-10,1,-6,1,4,-4,-4,-9,10,4,2,2,-7,-3,-7,-8,-10,4,-7,-8,10,-7,9,-3,-1,-10,4,-6,4,-9,-8,9,-8,-4,2,8,-3,8,3,2,10,-7,-3,7,-2,-10,3,-10,6,8,5,-10,4,-2,-9,1,8,4,-2,-1,-7,-7,-10,-3,-1,4,10,-6,-10,-1,5,-8,9,4,-3,6,-6,10,9,4,-6,-6,2,9,10,-3,-2,-6,3,2,5,-3,2,8,-9,-1,-1,-1,9,-5,2,4,8,-6,-1,6,8,-6,-5,2,-9,8,2,-2,-3,-1,-4,-8,-4,3,3,-1,9,3,-4,-9,-10,2,8,4,-1,-6,-8,7,-9,7,-10,-6,8,4,-4,6,9,7,-1,9,-4,7,9,3,-6,3,1,-6,9,-10,4,9,3,3,7,-8,-6,2,-8,-5,-7,2,-6,-4,10,-7,1,10,-4,-10,4,9,-2,5,-5,-6,-9,-8,-9,-1,8,5,-6,5,-7,-8,-4,1,9,10,8,-6,-6,-1,9,-4,-2,10,4,-5,-2,-2,-1,4,8,-3,10,3,-6,-1,-8,5,3,-7,1,-8,6,-9,2,8,7,-8,3,-5,10,5,2,-8,-5,4,7,-7,3,-4,9,-6,-5,7,8,8,-1,-5,-5,10,8,-6,-5,1,-8,2,7,8,-2,2,9,9,-5,3,-9,-9,-4,-3,-7,6,9,5,-7,2,9,1,-3,8,-5,7,-1,-1,1,-5,-10,4,-2,-7,-3,8,2,10,10,-5,-6,-10,-1,5,7,-10,2,6,6,-10,-2,-1,-10,10,-8,6,7,4,-9,10,8,10,-8,3,-10,3,1,-6,6,10,1,1,-4,-6,3,-6,9,-8,-4,1,3,-8,9,-7,2,-2,-5,-2,5,1,-7,-8,5,-3,6,-7,-9,5,-10,6,10,-4,-8,-4,-6,10,2,-10,-3,-7,7,10,-8,-6,9,-10,-10,4,5,-1,-10,4,1,8,7,7,-9,1,-3,-8,9,-1,-4,-6,-10,-10,2,-4,-8,-8,-8,-8,-1,-4,8,-7,10,7,-1,-5,-2,3,10,6], dtype = "int8")#candidate|4097|(1440,)|const|int8
call_4096 = relay.TupleGetItem(func_2078_call(relay.reshape(const_4097.astype('int8'), [360, 4])), 4)
call_4098 = relay.TupleGetItem(func_2081_call(relay.reshape(const_4097.astype('int8'), [360, 4])), 4)
func_3626_call = mod.get_global_var('func_3626')
func_3628_call = mutated_mod.get_global_var('func_3628')
const_4124 = relay.const([4.025794,3.704598,2.741031,2.431429,6.348925,2.716253,-5.771022,7.330145,5.049951,-9.003879,0.339112,-9.609916,-2.941530,-5.702043,2.798995,6.434940,9.199786,7.700379,4.790493,7.824049,2.671929,-3.711116,0.097624,-5.959959,5.095091,1.511541,1.680946,-3.479151,5.172000,0.096440,6.270925,-1.763668,-5.290588,9.855477,-9.548822,-9.287368,5.129805,7.673903,-4.597860,1.105563,0.899685,-8.708778,-1.927136,-1.477001,1.830157,1.575918,7.572881,-5.839107,7.825552,1.786925,-7.313970,2.448180,-8.883526,-6.059371,-2.402416,4.289324,-8.490519,0.731240,-0.764796,0.726405,7.673628,-8.397483,-5.536717,-1.740726,-1.181467,9.870960,3.674342,-0.857241,0.304567,-7.473811,-7.437696,4.158162,5.537802,-4.342398,1.128537,-8.546676,-3.434504,3.520781,1.684394,-5.153059,6.132494,-1.724435,-5.385988,6.286935,-2.972546,2.779741,5.908182,0.274818,2.339200,-6.142388,7.664796,-6.856209,9.058618,-3.413215,6.258887,-8.161833,-4.987275,-5.954375,7.442444,8.879102,2.803207,-4.430867,9.227786,-6.507313,2.056812,1.046110,2.836950,-7.152275,5.413303,5.898110,5.668177,-8.025493,-9.165913,-8.103745,-8.747456,6.764495,8.489995,-2.101719,-5.381288,3.852182,3.383205,-5.982663,-4.604460,1.619107,-6.288344,7.725124,-6.335207,7.258313,-9.694190,-8.408536,1.368275,-2.374793,0.473955,-4.935355,5.868128,-1.125656,-5.715816,6.313615,0.386854,2.973845,8.624570,-9.143666,-4.156152,0.713312,8.801590,9.919971,7.174332,8.489880,-0.747903,-8.318935,-6.650931,-0.219661,-8.759141,4.770715,-6.335487,0.042551,4.014506,6.227497,1.223220,-4.841637,-9.572509,-1.816400,-5.996686,-2.274327,1.445648,-0.053838,3.361920,-9.429771,2.652737,-4.736948,-3.966849,8.580682,0.701845,6.126138,9.372559,5.865488,1.093239,-2.258471,-7.578475,-8.743188,1.851489,4.268680,3.715965,-3.861878,8.590485,-2.847839,-2.442537,-8.704538,-1.021099,0.399952,8.908542,4.778373,-8.017248,-1.372058,4.754954,-1.932299,-3.417706,7.029115,9.437844,-7.823127,-1.295986,7.617358,-4.829931,-7.567786,0.573310,4.771854,7.123331,-2.928011,-0.050796,-4.273684,0.098586,-7.821813,-3.905404,-8.943470,-6.086665,-4.335291,1.545756,3.154045,9.193303,9.410471,0.904114,-0.971240,1.072902,-0.949575,0.494493,3.824516,3.415704,-4.710352,-5.387168,-8.242420,0.055032,0.831243,-3.899001,0.165206,9.822725,-1.582748,3.430813,0.368736,8.180648,-9.533012,-6.613902,-5.214729,8.970568,6.842666,0.946799,-8.111656,-7.105851,1.624923,0.176445,5.150281,6.050713,8.025349,-0.726084,-9.657311,6.582234,-6.369651,-3.562371,0.548449,-2.949275,2.754838,-0.131101,-2.763151,-5.596809,5.615581], dtype = "float32")#candidate|4124|(264,)|const|float32
call_4123 = relay.TupleGetItem(func_3626_call(relay.reshape(const_4124.astype('float32'), [11, 12, 2])), 2)
call_4125 = relay.TupleGetItem(func_3628_call(relay.reshape(const_4124.astype('float32'), [11, 12, 2])), 2)
output = relay.Tuple([call_4063,call_4086,call_4096,const_4097,call_4123,const_4124,])
output2 = relay.Tuple([call_4064,call_4087,call_4098,const_4097,call_4125,const_4124,])
func_4128 = relay.Function([], output)
mod['func_4128'] = func_4128
mod = relay.transform.InferType()(mod)
output = func_4128()
func_4129 = relay.Function([], output)
mutated_mod['func_4129'] = func_4129
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4164 = relay.var("var_4164", dtype = "float64", shape = (16, 1, 3))#candidate|4164|(16, 1, 3)|var|float64
var_4165 = relay.var("var_4165", dtype = "float64", shape = (16, 3, 3))#candidate|4165|(16, 3, 3)|var|float64
bop_4166 = relay.power(var_4164.astype('float64'), var_4165.astype('float64')) # shape=(16, 3, 3)
func_1592_call = mod.get_global_var('func_1592')
func_1594_call = mutated_mod.get_global_var('func_1594')
call_4173 = relay.TupleGetItem(func_1592_call(), 1)
call_4174 = relay.TupleGetItem(func_1594_call(), 1)
func_3096_call = mod.get_global_var('func_3096')
func_3101_call = mutated_mod.get_global_var('func_3101')
const_4182 = relay.const([7.957894,-0.557527,2.183687,-3.198444,5.185129,8.373968,7.554581,-7.034894,-9.868988,5.827998,-0.589157,-8.670398,8.033713,-9.319966,-3.329888,-4.413983,-2.210853,1.429291,6.533466,0.461187,-2.744171,-4.820383,-9.316481,3.277340,3.991729,-1.011441,4.295747,-7.092727,-5.250323,2.208438,4.257691,-8.246489,4.069451,-8.370696,-5.899316,2.966259,-0.613884,-9.172670,7.724326,-1.238171,-4.627608,-6.715780,2.781703,-5.359720,2.399602,7.830243,-1.898372,-7.116766,9.443509,-0.398433,-0.591351,-9.330333,2.456049,-7.131696,-4.229835,0.320995,5.036404,0.503361,-2.174144,2.866810,0.060856,7.786218,-3.334127,0.772144,-1.282101,8.802271,-4.019786,4.923212,-0.916521,-8.635207,-1.132797,-5.832686,9.611141,5.911039,1.467650,-9.327015,8.719424,-2.216737,2.456179,2.058677,3.885575,2.022070,-5.901132,9.777951,-4.878269,-6.929976,-3.722523,-0.634671,-2.622542,5.703494,-0.705536,-1.501106,4.358882,-4.104348,4.725904,-4.294716], dtype = "float32")#candidate|4182|(96,)|const|float32
call_4181 = relay.TupleGetItem(func_3096_call(relay.reshape(const_4182.astype('float32'), [8, 3, 4]), relay.reshape(const_4182.astype('float32'), [8, 3, 4]), relay.reshape(const_4182.astype('float32'), [8, 3, 4]), ), 2)
call_4183 = relay.TupleGetItem(func_3101_call(relay.reshape(const_4182.astype('float32'), [8, 3, 4]), relay.reshape(const_4182.astype('float32'), [8, 3, 4]), relay.reshape(const_4182.astype('float32'), [8, 3, 4]), ), 2)
uop_4194 = relay.atanh(var_4164.astype('float32')) # shape=(16, 1, 3)
output = relay.Tuple([bop_4166,call_4173,call_4181,const_4182,uop_4194,])
output2 = relay.Tuple([bop_4166,call_4174,call_4183,const_4182,uop_4194,])
func_4200 = relay.Function([var_4164,var_4165,], output)
mod['func_4200'] = func_4200
mod = relay.transform.InferType()(mod)
mutated_mod['func_4200'] = func_4200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4200_call = mutated_mod.get_global_var('func_4200')
var_4202 = relay.var("var_4202", dtype = "float64", shape = (16, 1, 3))#candidate|4202|(16, 1, 3)|var|float64
var_4203 = relay.var("var_4203", dtype = "float64", shape = (16, 3, 3))#candidate|4203|(16, 3, 3)|var|float64
call_4201 = func_4200_call(var_4202,var_4203,)
output = call_4201
func_4204 = relay.Function([var_4202,var_4203,], output)
mutated_mod['func_4204'] = func_4204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3356_call = mod.get_global_var('func_3356')
func_3357_call = mutated_mod.get_global_var('func_3357')
call_4223 = func_3356_call()
call_4224 = func_3356_call()
func_3096_call = mod.get_global_var('func_3096')
func_3101_call = mutated_mod.get_global_var('func_3101')
var_4238 = relay.var("var_4238", dtype = "float32", shape = (96,))#candidate|4238|(96,)|var|float32
call_4237 = relay.TupleGetItem(func_3096_call(relay.reshape(var_4238.astype('float32'), [8, 3, 4]), relay.reshape(var_4238.astype('float32'), [8, 3, 4]), relay.reshape(var_4238.astype('float32'), [8, 3, 4]), ), 3)
call_4239 = relay.TupleGetItem(func_3101_call(relay.reshape(var_4238.astype('float32'), [8, 3, 4]), relay.reshape(var_4238.astype('float32'), [8, 3, 4]), relay.reshape(var_4238.astype('float32'), [8, 3, 4]), ), 3)
output = relay.Tuple([call_4223,call_4237,var_4238,])
output2 = relay.Tuple([call_4224,call_4239,var_4238,])
func_4241 = relay.Function([var_4238,], output)
mod['func_4241'] = func_4241
mod = relay.transform.InferType()(mod)
var_4242 = relay.var("var_4242", dtype = "float32", shape = (96,))#candidate|4242|(96,)|var|float32
output = func_4241(var_4242)
func_4243 = relay.Function([var_4242], output)
mutated_mod['func_4243'] = func_4243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1472_call = mod.get_global_var('func_1472')
func_1473_call = mutated_mod.get_global_var('func_1473')
call_4280 = func_1472_call()
call_4281 = func_1472_call()
var_4308 = relay.var("var_4308", dtype = "float64", shape = (16, 12, 2))#candidate|4308|(16, 12, 2)|var|float64
bop_4309 = relay.maximum(call_4280.astype('int64'), var_4308.astype('int64')) # shape=(16, 12, 2)
bop_4312 = relay.maximum(call_4281.astype('int64'), var_4308.astype('int64')) # shape=(16, 12, 2)
func_1360_call = mod.get_global_var('func_1360')
func_1361_call = mutated_mod.get_global_var('func_1361')
call_4316 = relay.TupleGetItem(func_1360_call(), 2)
call_4317 = relay.TupleGetItem(func_1361_call(), 2)
output = relay.Tuple([bop_4309,call_4316,])
output2 = relay.Tuple([bop_4312,call_4317,])
func_4318 = relay.Function([var_4308,], output)
mod['func_4318'] = func_4318
mod = relay.transform.InferType()(mod)
mutated_mod['func_4318'] = func_4318
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4319 = relay.var("var_4319", dtype = "float64", shape = (16, 12, 2))#candidate|4319|(16, 12, 2)|var|float64
func_4318_call = mutated_mod.get_global_var('func_4318')
call_4320 = func_4318_call(var_4319)
output = call_4320
func_4321 = relay.Function([var_4319], output)
mutated_mod['func_4321'] = func_4321
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4330 = relay.const([[[-9.627225,-8.045855,1.520409,-3.084008,5.289093,-0.406204,7.241859,6.443355,8.360734,2.086281,7.185737],[-0.766827,-1.446160,1.489969,-8.020266,-8.435490,4.530032,7.502997,-4.398540,-8.175430,-2.508388,9.898276],[2.042891,-7.388678,-8.293869,-6.500493,5.961500,-1.058565,-1.324709,-6.383653,-5.785606,2.626734,8.354818],[-8.580857,-0.163710,1.332854,5.169474,-0.119156,9.028334,-9.662205,-8.495611,1.508387,6.898625,-2.027201],[-5.261973,5.961313,4.820114,-0.867055,0.225492,-7.215555,-0.752469,3.561057,8.929510,-0.412510,-5.465773],[-3.775738,6.102987,-4.513381,7.289270,-0.978762,6.846033,2.436542,-1.447195,7.477131,-7.947174,0.409293],[8.827663,7.736355,-3.384279,-0.595697,-8.354001,-0.005019,-6.622445,-9.240680,0.548633,0.292844,-6.489719],[6.345751,6.973461,2.119784,3.056228,-3.895048,7.646018,3.709123,1.552824,-9.207349,-0.631229,4.521425],[3.815821,-3.245858,-2.672212,-8.780380,-1.563611,2.906724,-3.730866,-9.305028,8.362283,3.853198,-8.987849],[-0.716872,-6.935256,6.694808,5.012132,3.364707,-8.837674,2.264471,-1.376020,-8.839388,-5.607221,-8.316056],[-0.432914,-4.217324,7.306183,-6.754585,-0.473401,9.579111,7.499110,4.993860,8.820511,2.087934,-8.426519],[-9.208884,-5.823692,-7.187703,-8.368410,-6.489082,2.122958,-7.312517,-1.913173,-0.711853,5.143045,7.347945],[-3.307123,-2.354833,9.865800,4.996099,-9.877984,-9.768742,-4.589113,8.015539,1.582925,9.191151,-1.886244]],[[3.817809,-6.403090,0.297143,3.076192,-5.147049,6.322987,2.112090,5.186394,3.989525,-2.157103,-9.258967],[-6.774468,8.587405,2.878994,-6.539270,-3.230859,-0.658004,2.549671,5.112304,-2.365801,-8.968480,-1.596479],[7.422374,-9.257414,3.721425,-0.586716,-7.456786,-7.668343,4.019389,-4.485833,8.795986,4.220863,-9.720564],[-3.782023,-5.854093,9.295083,-7.266207,-3.131578,0.392612,-5.686720,-3.915495,6.344109,5.933122,-0.009845],[8.143628,-9.271996,-9.292300,8.753881,-6.309506,-5.556071,-3.331545,3.132236,4.943283,-4.935696,6.863982],[4.335940,-1.361585,-9.807451,-8.635218,-2.318280,1.037097,8.125362,-1.520284,-7.990956,-4.119433,4.787467],[6.098852,3.416733,6.685606,5.155674,5.412413,-4.143846,3.167368,1.823658,5.572021,-8.025841,7.130138],[-3.001523,-6.622218,-9.208692,3.556869,0.006879,5.020808,1.555477,6.903605,5.546527,-0.326351,-1.295292],[-7.263536,7.135029,9.092604,-7.435959,8.093146,-7.876573,-6.806823,-5.087371,7.072118,-5.564691,4.303196],[0.951329,-3.979279,3.983293,-1.626022,0.612463,7.921989,-7.160074,-3.308718,7.747075,-7.791144,6.570880],[3.838031,-8.364035,7.913706,3.411995,1.029311,5.157745,9.888193,-7.021240,-9.952768,-6.955708,-6.496985],[-7.361151,9.481703,9.009302,-3.136128,-3.296206,-4.609207,-9.410182,7.144872,-3.382887,-7.239627,6.654530],[-7.019228,2.361523,4.577125,1.604673,-8.843914,-1.346439,4.000598,5.019248,-7.256476,1.865601,0.378796]],[[-4.033894,7.538698,6.547729,8.660860,3.295331,-8.344569,-6.621503,-8.145971,9.196032,-0.386078,4.469116],[1.208138,5.776146,-0.840760,9.259799,-0.421831,6.363418,-4.991085,7.932745,5.621217,-4.875378,9.302641],[3.724554,-0.313834,-9.513360,-5.759930,-1.732071,1.309234,1.771788,5.321215,0.796611,-5.463186,5.515623],[9.592334,-0.928556,-7.895895,-0.585072,-0.673493,1.993495,-3.402055,2.068045,3.434579,7.710108,2.488770],[7.298215,0.183790,-5.682840,6.551796,-5.157787,-5.089635,9.736370,7.088544,-8.020798,9.196965,-9.778345],[4.461981,-8.210792,-8.076878,6.628566,-0.554841,-9.983001,2.740076,5.792863,-2.788435,2.048385,7.034556],[7.012336,-1.160285,-4.090703,-2.833590,-8.887702,-9.262635,-9.431511,-0.556220,-2.785558,-9.305335,-7.517316],[9.523134,-7.230570,2.647765,-9.813940,-8.987646,-2.725233,8.976660,-4.402570,7.586773,0.059966,9.350847],[-2.371395,-0.051210,-5.094854,2.453100,-9.077247,3.310196,7.305843,0.708314,1.916460,0.080958,-0.879716],[-5.311884,-5.061348,8.709673,1.132771,-2.005076,-0.361729,-2.527555,0.222505,7.255243,-7.494524,8.363150],[-2.291262,0.356334,-0.206616,3.031881,2.611271,-9.492158,7.346295,2.887769,-0.162365,8.123901,-9.784597],[-0.033859,0.317044,-4.729638,-6.831371,6.902931,-0.602130,-8.606005,-5.004930,9.735744,0.225850,7.339178],[-5.236279,9.581966,-0.518147,2.983502,-3.716630,0.797199,-4.062609,1.994340,6.339394,2.125407,6.526051]],[[-7.860659,0.793877,4.088965,9.726558,2.937971,9.761641,1.811855,3.914537,0.180325,-2.927793,-8.965012],[-1.288775,7.998980,-5.862720,1.932996,-7.504387,0.794854,2.706203,-7.559139,-2.851185,-3.450410,-2.796536],[9.408509,2.307136,8.462824,3.822483,-0.853436,8.662509,1.459832,-5.665916,5.657793,6.019347,-8.101788],[9.876678,8.588281,-6.627589,6.154635,2.699942,6.029844,7.479602,-9.373173,-8.769797,-7.209339,-4.376724],[7.393852,-2.570957,9.148895,-6.890972,6.123581,-6.897603,5.409897,-6.744512,1.559709,5.334034,-1.934885],[9.590666,-6.118217,0.211082,9.214022,-0.844752,-1.137840,1.569225,-6.790478,1.789576,2.644470,8.657212],[7.106435,-0.350718,9.965204,2.574573,-7.704218,9.851763,-2.509240,-0.276762,-2.123027,-7.979473,9.967314],[3.971629,4.482605,3.205255,-7.460729,7.832855,9.135901,4.045407,-6.894963,-9.323456,8.210108,7.736918],[3.057705,-6.710751,-8.102564,-8.414887,-2.446779,-9.586053,8.832311,6.046763,-1.488768,5.867181,-3.223940],[-6.666700,4.418096,2.917984,-0.465885,-5.684349,-7.278983,-4.199428,9.518741,3.345936,-6.517738,-1.327065],[9.028036,2.629477,-9.435106,8.501278,3.466680,8.751161,1.716736,-5.438207,0.666767,2.287350,5.060473],[9.016584,-4.218641,-2.644828,-9.778096,-7.560962,-3.645932,0.551697,-5.913576,5.448888,-1.757519,-4.853616],[-4.760782,-4.790017,1.447629,2.306990,0.090477,-9.949739,4.649758,-1.017597,4.126500,-2.163542,-4.839320]],[[-5.655489,-7.587435,0.642994,7.683431,-4.195523,-3.176931,3.524843,-5.202886,-5.458251,6.364123,-1.712899],[4.306823,-0.347715,4.507685,2.613670,-3.362205,7.197805,4.981620,-0.394734,-6.169938,-4.943750,4.058067],[8.442755,3.271736,4.537423,-3.031318,1.466512,-1.286271,-6.635713,-8.518366,3.454971,1.625223,-8.150077],[9.500986,6.113533,3.367954,-8.304700,-6.833921,4.252520,5.544247,-0.363405,-1.694201,-0.137363,-2.680904],[-5.550079,-3.433829,7.041238,-4.841332,-6.838010,-5.083267,-3.148643,-6.374729,-2.412980,-9.540351,-5.652781],[-4.439631,8.024484,-1.739771,9.919819,-8.524513,-4.116292,-4.127402,-3.564115,5.709528,-6.400302,9.329719],[9.598028,-8.225411,-6.238777,3.253270,-9.510346,3.669728,-5.028865,9.371571,-1.690817,-7.342197,-2.022911],[1.759761,1.965457,-7.496625,-7.432674,-3.917101,3.497951,-1.559602,7.012397,-5.907460,6.692359,1.180296],[9.841018,-4.712366,-6.661899,-2.040914,6.568588,-9.827905,-8.138336,-3.341819,-7.136801,5.689236,5.967577],[5.236207,5.823270,6.956237,0.860406,4.646668,0.055350,5.323026,-8.747150,1.094936,3.650389,-0.184933],[-4.709174,-2.951106,-0.359078,-3.200563,6.839561,-9.565061,5.010783,-0.959976,2.290230,0.780710,0.086536],[-4.262137,9.129971,1.426237,4.373601,-2.829386,-5.708669,-8.477339,-6.166192,4.692883,-1.578468,5.914427],[9.283396,3.435849,9.992081,3.569004,4.939476,-3.594681,3.811436,8.963825,4.600057,-3.864136,-9.850118]],[[-8.418313,1.038933,1.239442,-3.605129,4.188064,-3.040462,-4.580787,-9.446786,-3.050480,9.158503,-1.432699],[-3.593150,-3.109554,9.054975,9.646178,7.253147,4.843960,1.521700,5.834340,1.090444,7.078539,0.291230],[3.997972,-0.702037,9.510609,-4.213447,-4.922280,5.840726,-2.871597,-6.377620,-2.756672,-2.395527,-7.934430],[-1.948596,4.293006,2.367355,7.401341,-5.534748,-0.374832,-2.178110,-6.710052,2.451506,4.736204,7.705201],[1.925894,-8.501185,-0.218396,4.257502,-6.633296,-3.936683,8.014792,5.998430,-7.522749,8.329255,-2.317625],[-8.587890,-9.930868,9.697430,-1.061591,-3.683085,-2.407193,2.609008,3.222647,-6.708878,7.023228,6.407244],[-4.554231,7.280909,-1.185890,8.367632,1.003782,4.227982,4.284761,0.502975,-6.962034,3.735174,-1.330253],[8.821663,-5.651484,-6.217983,-9.135281,-4.702800,-3.579314,6.095374,6.634792,6.189949,-0.755599,-1.035382],[6.417328,6.961354,3.896683,3.841441,8.593633,5.861832,-3.989224,6.620620,4.335620,0.725614,-1.877689],[-8.472391,7.236046,-2.010837,5.831129,4.258068,-1.540811,-4.212818,0.721268,-9.488893,-8.043121,-3.333275],[7.194677,2.820732,-9.428582,-8.775641,9.590162,-0.477180,-5.744887,-9.779795,3.979874,-3.601359,-1.354575],[-8.591651,-6.832077,-0.268688,-5.428359,3.035361,5.385383,6.941778,8.210326,-5.162827,-8.996227,7.135694],[3.422956,-2.315154,1.195180,-9.106837,3.897760,-3.071296,7.106733,-1.357248,2.502883,9.643497,-8.902452]],[[-4.464158,-9.724720,-2.966134,5.330347,8.136040,2.319468,-1.655600,8.996758,-7.959114,5.161102,-1.382671],[-3.370901,-5.319960,7.724894,-3.400760,-4.464927,7.936775,0.222609,-5.440116,-7.588959,9.503173,9.031119],[-5.022436,-9.800168,-0.206044,2.890002,0.812485,9.642375,-0.683402,0.405775,1.352507,5.600731,7.398945],[-6.746174,-4.921904,9.988857,7.040115,7.503689,6.687730,-0.803121,1.326666,2.193867,7.350214,-8.981016],[8.976694,-0.284060,-9.361307,7.144117,-1.648521,6.281088,-3.677462,-4.441079,2.098902,-3.300641,-3.586676],[-0.086935,-1.684270,-1.278854,5.092036,6.487791,-4.820566,8.671805,-9.287996,-8.221153,-4.843718,9.031947],[1.393499,-1.333789,2.279174,2.909560,-4.736647,7.576394,4.073960,-2.604745,-9.627689,6.246376,-2.423710],[7.164430,-2.426868,1.793396,0.549221,3.717509,0.103095,-3.797575,-5.501636,-5.372932,8.238758,-0.030530],[4.881882,0.176434,-1.559148,-5.787097,5.294183,1.509573,-2.145627,4.852498,7.822112,-2.453918,-5.808790],[9.388408,-2.972162,5.216317,1.412876,6.771840,3.881772,9.628358,9.923225,-7.903100,0.083420,-3.965337],[-7.332986,-1.849444,2.096553,-8.254598,7.887770,-7.280776,5.316685,7.198525,8.817246,3.424785,-9.627525],[5.920099,6.873752,-7.103721,1.431942,-6.053098,-5.658529,-1.554431,0.137017,-2.619183,-1.201519,-5.581847],[-4.992456,8.582727,-7.845805,-6.922443,5.079837,1.261334,7.211213,2.242375,-7.417608,0.935825,-5.004917]],[[-2.611024,-9.985906,-5.603852,-6.113057,0.484951,6.782545,-2.796657,7.640922,-7.180386,-8.134451,0.155962],[5.232713,8.110937,-5.977838,7.100510,-7.202138,-7.584062,-6.070896,3.761512,-6.098091,7.720208,1.294110],[7.674675,4.069376,3.905877,3.723596,7.855612,-6.331648,1.197682,1.318307,4.584935,-4.836542,2.325258],[7.952160,1.712915,9.331970,6.881577,9.363153,6.080988,-8.150310,-8.261216,-5.284174,-6.233354,-5.205673],[5.193881,-2.464951,3.423476,5.213381,9.388443,-5.772749,-7.302199,-1.155423,-8.404017,-2.893756,-6.732534],[8.665930,2.824303,-9.355566,-5.198149,8.113542,1.232932,-0.820659,-2.742583,6.229159,-0.739171,2.890568],[6.338850,-5.506916,0.210058,3.009370,0.087552,-6.200593,-6.952269,5.657142,-6.514967,5.850176,-5.089957],[-9.970641,8.984244,6.959514,0.657092,-9.784008,-8.351494,8.975072,5.426954,2.248726,5.320561,2.949773],[-5.069888,-6.197800,5.749664,-4.362329,2.286726,9.391707,-1.317877,8.191231,2.269995,-0.185313,-0.668302],[4.276127,8.778573,6.848801,-0.134703,-9.730924,6.309898,3.855139,-0.063193,-5.786065,8.630048,-9.329251],[-5.688659,8.249352,0.065406,2.872718,4.449917,-4.813574,5.719013,0.811316,-2.847236,0.150537,-3.768334],[5.991934,-8.006276,7.874277,6.927976,-8.558885,6.642741,9.788602,4.245412,-3.235023,8.442912,8.671934],[-5.130690,-1.959683,8.196908,-4.882680,0.244919,-3.915354,-4.513234,6.425855,-4.817603,6.455260,5.742710]],[[-7.258480,-4.910043,-0.824146,4.917497,-9.178014,-5.049400,0.869206,-2.652629,-5.739309,9.860794,-8.241258],[-7.470552,5.823699,4.572585,-9.551283,6.045707,0.353145,6.405823,6.416682,-8.565536,3.737248,-4.125824],[-3.785587,-5.248193,-7.126292,3.173576,8.336172,-2.212688,-1.642037,-2.185660,5.551542,-6.832058,3.610849],[-3.685763,-2.612598,-6.477168,5.639439,-5.636525,-7.507105,-1.350920,-4.572994,3.481553,0.467701,-6.190757],[8.653250,-4.255798,-2.219935,6.844748,7.728797,-3.084686,-2.334586,9.847245,-7.091857,1.481277,-6.990119],[6.363195,-4.257015,5.401537,5.074810,2.924987,-4.317292,4.776439,-8.388475,-5.212609,-0.958905,-5.429923],[6.686491,-5.254583,5.105152,-4.758496,-1.800606,1.117602,-9.687641,-0.381047,-1.639802,-3.970865,-0.533603],[-5.367762,8.619211,-7.458513,1.620017,-5.070380,-7.483817,-8.827097,0.436280,0.157977,9.959784,-9.512822],[2.520245,6.607410,-8.104915,-5.414569,9.677007,-9.550898,7.822734,-8.603262,9.926676,-6.253360,9.970041],[7.528052,7.392997,-9.263702,1.765483,9.169515,-4.680667,1.568598,-0.578797,7.449092,-5.679513,-3.037577],[-3.435102,-8.895785,-5.342770,5.374610,-8.014969,-9.145383,0.177897,-4.595592,7.661794,-9.787490,-0.029112],[-2.517879,8.189895,-0.383516,6.084461,-1.312963,4.295669,7.411353,0.875979,4.202980,-6.065216,3.014757],[6.534362,-9.950656,3.691335,-2.483748,-5.520402,8.721529,-5.921815,1.801930,-7.345166,1.238624,8.108941]]], dtype = "float32")#candidate|4330|(9, 13, 11)|const|float32
uop_4331 = relay.cosh(const_4330.astype('float32')) # shape=(9, 13, 11)
output = relay.Tuple([uop_4331,])
output2 = relay.Tuple([uop_4331,])
func_4336 = relay.Function([], output)
mod['func_4336'] = func_4336
mod = relay.transform.InferType()(mod)
mutated_mod['func_4336'] = func_4336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4336_call = mutated_mod.get_global_var('func_4336')
call_4337 = func_4336_call()
output = call_4337
func_4338 = relay.Function([], output)
mutated_mod['func_4338'] = func_4338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2577_call = mod.get_global_var('func_2577')
func_2578_call = mutated_mod.get_global_var('func_2578')
call_4344 = relay.TupleGetItem(func_2577_call(), 0)
call_4345 = relay.TupleGetItem(func_2578_call(), 0)
var_4346 = relay.var("var_4346", dtype = "float32", shape = (11, 12, 2))#candidate|4346|(11, 12, 2)|var|float32
bop_4347 = relay.minimum(call_4344.astype('uint8'), var_4346.astype('uint8')) # shape=(11, 12, 2)
bop_4350 = relay.minimum(call_4345.astype('uint8'), var_4346.astype('uint8')) # shape=(11, 12, 2)
func_884_call = mod.get_global_var('func_884')
func_886_call = mutated_mod.get_global_var('func_886')
const_4352 = relay.const([9.040065,-0.682377,-1.279891,-8.570080,9.639652,-0.260836,9.624546,-6.628404,4.929089,2.589804,2.242144,-9.508328,-4.055058,-6.082994,-5.833355,7.923038,5.936540,-9.014765,-9.803814,-1.399710,-8.943643,4.937894,-8.559687,-6.879892,-5.569123,1.963784,0.241242,5.743790,8.421006,-5.202931,5.314480,-1.776981,9.270442,8.201330,8.191616,8.908180,-0.309505,7.096231,-0.851121,-0.807822,2.863012,-1.036957,8.394884,-1.877034,2.216985,-1.432973,-1.511549,2.054191,-0.184368,1.386462,1.583780,9.173878,-4.867436,-0.049485,-1.521256,7.149730,6.512035,8.001801,1.315422,9.660855,-3.637811,-8.110299,-4.420356,-0.377776,-2.574935,-6.937680,-7.994896,7.465067,-8.769244,8.328474,-9.845588,-5.419944,-9.432589,-5.521794,1.483501,-1.236426,-7.363883,-0.002094,-9.854629,3.959024,2.727192,-6.649772,9.949145,-6.281570,-7.434594,-1.684405,-6.751416,-7.807181,-2.595224,7.181122,-6.883935,8.035371,-7.839490,-3.889462,-8.125855,0.585464,8.204982,7.295637,0.468070,9.900436,7.308201,-5.825476,-7.774536,-6.568192,6.344542,0.408907,5.769594,-7.620243,-8.136712,5.506751,-4.681433,-7.871413,-6.983747,-5.200690,6.774238,0.843155,-8.939970,5.711359,-4.094210,8.201364,7.450974,-7.060953,-7.329718,-5.483805,5.265101,6.728809,-1.297121,7.163577,-6.293288,-5.180305,2.909602,-3.237411,3.434174,0.167621,-1.643641,6.461556,4.605999,-5.692658,3.618070,-2.284565,-2.776755,-9.260581,-0.303314,-8.372265,-3.029712,-2.856365,-1.363044,7.485703,-0.186228,-8.910759,9.963066,-9.592290,0.015179,-0.444087,9.256813,2.400018,6.531642,-0.619589,5.994304,-3.590216,6.802712,-8.206894,2.287082,6.221662,-1.352460,-2.173995,-3.212506,-6.034560,-8.256547,-0.850142,6.550671,4.994863,1.297698,-0.094665,-0.797494,-9.819493,-4.318102,-6.798817,-3.868166,0.469627,9.284792,1.941182,0.067133,4.253689,-0.343697,5.564625,2.510579,-7.321860,1.693257,2.691844,1.240845,5.319041,-4.808729,-7.050186,-1.595114,8.230973,6.070616,9.618923,-0.648420,-8.944376,-4.660758,0.713848,0.128037,-1.798555,-8.721197,-6.288215,-2.594658,5.342977,4.749111,7.295007,-8.858546,9.097707,7.113582,-0.434843,0.560210,6.447633,-0.545291,3.350282,-6.453212,-8.190358,-0.885639,5.299039,1.048949,2.524352,-5.505850,-1.871952,-3.717012,-1.545010,-0.670851,8.268558,-4.691870,7.294400,3.119357,-5.422747,-6.894187,6.067017,0.102615,6.621654,1.331045,-9.277615,-3.007917,-5.055015,-9.066122,-9.583343,4.777913,2.135929,-6.229525,1.835106,6.932505,-3.196396,-6.293345,-3.719467,-2.722505,-3.640711,8.043890,1.599740,4.245825,-8.838755,-4.766323,-0.823028,-6.281231,6.558297,-9.758993,1.097852,-9.785068,-6.065103,3.398772,0.319413,-9.145708,8.113152,-5.607990,8.410033,8.897153,7.094276,9.614482,7.531181,9.190672,-5.108055,1.371229,-3.551563,8.178776,1.024736,4.951669,-9.469410,-2.503434,9.457488,-3.488889,4.190833,-9.902476,-8.221557,-7.886665,-3.664721,-6.943417,-0.453788,-0.656034,-2.496987,5.923296,-5.830292,-8.837054,-4.990558,-1.211274,8.979529,5.079502,-1.301961,0.866590,1.737100,6.381691,-8.387361,-9.573093,2.361491,5.813189,3.938764], dtype = "float32")#candidate|4352|(312,)|const|float32
call_4351 = relay.TupleGetItem(func_884_call(relay.reshape(const_4352.astype('float32'), [13, 8, 3])), 4)
call_4353 = relay.TupleGetItem(func_886_call(relay.reshape(const_4352.astype('float32'), [13, 8, 3])), 4)
uop_4387 = relay.erf(call_4351.astype('float64')) # shape=(660,)
uop_4389 = relay.erf(call_4353.astype('float64')) # shape=(660,)
output = relay.Tuple([bop_4347,const_4352,uop_4387,])
output2 = relay.Tuple([bop_4350,const_4352,uop_4389,])
func_4394 = relay.Function([var_4346,], output)
mod['func_4394'] = func_4394
mod = relay.transform.InferType()(mod)
mutated_mod['func_4394'] = func_4394
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4395 = relay.var("var_4395", dtype = "float32", shape = (11, 12, 2))#candidate|4395|(11, 12, 2)|var|float32
func_4394_call = mutated_mod.get_global_var('func_4394')
call_4396 = func_4394_call(var_4395)
output = call_4396
func_4397 = relay.Function([var_4395], output)
mutated_mod['func_4397'] = func_4397
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1360_call = mod.get_global_var('func_1360')
func_1361_call = mutated_mod.get_global_var('func_1361')
call_4406 = relay.TupleGetItem(func_1360_call(), 1)
call_4407 = relay.TupleGetItem(func_1361_call(), 1)
func_2149_call = mod.get_global_var('func_2149')
func_2150_call = mutated_mod.get_global_var('func_2150')
call_4413 = relay.TupleGetItem(func_2149_call(), 0)
call_4414 = relay.TupleGetItem(func_2150_call(), 0)
func_2683_call = mod.get_global_var('func_2683')
func_2685_call = mutated_mod.get_global_var('func_2685')
call_4430 = func_2683_call()
call_4431 = func_2683_call()
output = relay.Tuple([call_4406,call_4413,call_4430,])
output2 = relay.Tuple([call_4407,call_4414,call_4431,])
func_4447 = relay.Function([], output)
mod['func_4447'] = func_4447
mod = relay.transform.InferType()(mod)
output = func_4447()
func_4448 = relay.Function([], output)
mutated_mod['func_4448'] = func_4448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3660_call = mod.get_global_var('func_3660')
func_3662_call = mutated_mod.get_global_var('func_3662')
call_4494 = func_3660_call()
call_4495 = func_3660_call()
func_2361_call = mod.get_global_var('func_2361')
func_2362_call = mutated_mod.get_global_var('func_2362')
call_4523 = relay.TupleGetItem(func_2361_call(), 0)
call_4524 = relay.TupleGetItem(func_2362_call(), 0)
func_4200_call = mod.get_global_var('func_4200')
func_4204_call = mutated_mod.get_global_var('func_4204')
var_4555 = relay.var("var_4555", dtype = "float64", shape = (48,))#candidate|4555|(48,)|var|float64
const_4556 = relay.const([-1.320781,-9.540266,-0.606440,8.672013,-2.427832,-7.232998,9.753692,-9.951912,-3.886002,3.857880,3.224502,-9.501390,2.891164,-9.126844,-6.240585,8.297186,-2.740566,0.308409,2.110637,5.873693,6.691656,-1.155929,-8.625405,-5.533254,1.990571,-9.365130,8.693133,-8.437709,8.039091,-4.046138,-7.225681,-7.987369,8.273500,4.455977,-8.562330,-6.795763,-8.059899,-2.790620,-5.212051,0.077770,-5.694589,-8.972524,-4.921109,-8.050959,1.012220,1.162037,-2.843073,1.494853,-4.784690,-4.782600,8.926204,-2.990117,-2.676079,-0.555470,2.109412,-5.620764,7.902793,5.291640,-0.269306,2.784256,-4.104081,5.881059,-9.024101,-1.625061,6.697062,7.685832,-1.030786,-7.526276,-5.932492,4.778938,-2.168850,7.784395,-6.239455,3.309110,-1.887717,6.501369,1.078364,-4.833592,4.212504,-7.915544,8.847180,5.678611,5.312939,-4.512146,-4.967032,2.746754,-7.460482,-8.279236,-5.355484,3.871332,3.366060,8.423526,8.153750,-6.040879,3.991609,7.890020,4.711536,-5.654093,-4.245411,-7.360242,-7.386214,8.009240,9.831960,0.279896,5.557030,-2.024385,0.577353,8.433376,7.519069,8.733779,7.755955,-8.454272,4.420165,4.803282,4.186505,-8.889691,-3.818994,-7.764148,-7.131677,3.382991,-8.275694,-5.003831,2.755493,-3.100979,0.008304,3.421431,-0.472141,4.025272,-7.966066,5.664659,9.423400,4.697581,6.288091,2.958344,-2.080711,4.258032,-0.712705,-5.961141,-9.541811,0.296027,6.868177,-5.907033,-1.936974,2.053770], dtype = "float64")#candidate|4556|(144,)|const|float64
call_4554 = relay.TupleGetItem(func_4200_call(relay.reshape(var_4555.astype('float64'), [16, 1, 3]), relay.reshape(const_4556.astype('float64'), [16, 3, 3]), ), 2)
call_4557 = relay.TupleGetItem(func_4204_call(relay.reshape(var_4555.astype('float64'), [16, 1, 3]), relay.reshape(const_4556.astype('float64'), [16, 3, 3]), ), 2)
func_2683_call = mod.get_global_var('func_2683')
func_2685_call = mutated_mod.get_global_var('func_2685')
call_4564 = func_2683_call()
call_4565 = func_2683_call()
func_585_call = mod.get_global_var('func_585')
func_586_call = mutated_mod.get_global_var('func_586')
call_4579 = relay.TupleGetItem(func_585_call(), 0)
call_4580 = relay.TupleGetItem(func_586_call(), 0)
func_2361_call = mod.get_global_var('func_2361')
func_2362_call = mutated_mod.get_global_var('func_2362')
call_4581 = relay.TupleGetItem(func_2361_call(), 0)
call_4582 = relay.TupleGetItem(func_2362_call(), 0)
output = relay.Tuple([call_4494,call_4523,call_4554,var_4555,const_4556,call_4564,call_4579,call_4581,])
output2 = relay.Tuple([call_4495,call_4524,call_4557,var_4555,const_4556,call_4565,call_4580,call_4582,])
func_4583 = relay.Function([var_4555,], output)
mod['func_4583'] = func_4583
mod = relay.transform.InferType()(mod)
var_4584 = relay.var("var_4584", dtype = "float64", shape = (48,))#candidate|4584|(48,)|var|float64
output = func_4583(var_4584)
func_4585 = relay.Function([var_4584], output)
mutated_mod['func_4585'] = func_4585
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3356_call = mod.get_global_var('func_3356')
func_3357_call = mutated_mod.get_global_var('func_3357')
call_4611 = func_3356_call()
call_4612 = func_3356_call()
func_517_call = mod.get_global_var('func_517')
func_518_call = mutated_mod.get_global_var('func_518')
call_4631 = func_517_call()
call_4632 = func_517_call()
var_4640 = relay.var("var_4640", dtype = "float64", shape = (5, 12, 2))#candidate|4640|(5, 12, 2)|var|float64
bop_4641 = relay.add(call_4631.astype('uint64'), var_4640.astype('uint64')) # shape=(5, 12, 2)
bop_4644 = relay.add(call_4632.astype('uint64'), var_4640.astype('uint64')) # shape=(5, 12, 2)
var_4650 = relay.var("var_4650", dtype = "uint64", shape = (5, 12, 2))#candidate|4650|(5, 12, 2)|var|uint64
bop_4651 = relay.greater(bop_4641.astype('bool'), relay.reshape(var_4650.astype('bool'), relay.shape_of(bop_4641))) # shape=(5, 12, 2)
bop_4654 = relay.greater(bop_4644.astype('bool'), relay.reshape(var_4650.astype('bool'), relay.shape_of(bop_4644))) # shape=(5, 12, 2)
output = relay.Tuple([call_4611,bop_4651,])
output2 = relay.Tuple([call_4612,bop_4654,])
func_4657 = relay.Function([var_4640,var_4650,], output)
mod['func_4657'] = func_4657
mod = relay.transform.InferType()(mod)
mutated_mod['func_4657'] = func_4657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4657_call = mutated_mod.get_global_var('func_4657')
var_4659 = relay.var("var_4659", dtype = "float64", shape = (5, 12, 2))#candidate|4659|(5, 12, 2)|var|float64
var_4660 = relay.var("var_4660", dtype = "uint64", shape = (5, 12, 2))#candidate|4660|(5, 12, 2)|var|uint64
call_4658 = func_4657_call(var_4659,var_4660,)
output = call_4658
func_4661 = relay.Function([var_4659,var_4660,], output)
mutated_mod['func_4661'] = func_4661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3895_call = mod.get_global_var('func_3895')
func_3897_call = mutated_mod.get_global_var('func_3897')
call_4696 = relay.TupleGetItem(func_3895_call(), 2)
call_4697 = relay.TupleGetItem(func_3897_call(), 2)
output = relay.Tuple([call_4696,])
output2 = relay.Tuple([call_4697,])
func_4729 = relay.Function([], output)
mod['func_4729'] = func_4729
mod = relay.transform.InferType()(mod)
output = func_4729()
func_4730 = relay.Function([], output)
mutated_mod['func_4730'] = func_4730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3449_call = mod.get_global_var('func_3449')
func_3450_call = mutated_mod.get_global_var('func_3450')
call_4752 = relay.TupleGetItem(func_3449_call(), 0)
call_4753 = relay.TupleGetItem(func_3450_call(), 0)
output = call_4752
output2 = call_4753
func_4756 = relay.Function([], output)
mod['func_4756'] = func_4756
mod = relay.transform.InferType()(mod)
mutated_mod['func_4756'] = func_4756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4756_call = mutated_mod.get_global_var('func_4756')
call_4757 = func_4756_call()
output = call_4757
func_4758 = relay.Function([], output)
mutated_mod['func_4758'] = func_4758
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4768 = relay.var("var_4768", dtype = "int32", shape = (9, 4, 16))#candidate|4768|(9, 4, 16)|var|int32
const_4769 = relay.const([[[-3,7,-8,5,-4,-2,-7,10,-4,3,-2,1,-8,5,-9,-3],[10,10,-3,-3,-8,-3,2,8,4,5,2,5,2,2,-9,-4],[7,6,-1,-8,-6,5,6,5,-9,-5,10,-8,10,-6,9,7],[-5,7,-3,-4,5,8,5,1,-8,2,6,10,4,-6,-5,-8]],[[-7,-6,-9,9,2,-7,-5,-10,3,-2,-5,-7,-8,3,-6,-4],[7,3,-10,4,-4,-10,9,3,-5,-1,5,1,-10,9,-7,-1],[4,-2,8,8,-7,2,-10,8,-8,-6,-8,10,-1,-6,-3,3],[-10,-6,1,4,-2,-3,-1,-8,1,-6,10,9,-5,10,-9,-7]],[[-7,1,7,-7,-10,-3,-1,-2,4,-3,3,6,4,-6,-6,-6],[-8,-3,10,5,-8,3,-1,6,-2,-10,1,-1,-1,-10,1,-9],[10,-3,-2,2,-9,3,-7,-7,-6,-4,-4,-1,-3,1,-6,-5],[4,9,-8,-6,-4,-7,6,2,3,-2,-10,-10,-6,8,-3,10]],[[-9,-3,-2,4,-8,8,8,-9,-7,-8,3,-9,10,1,-10,-1],[4,8,1,-1,-6,4,-3,3,-1,7,10,1,5,3,6,6],[8,-5,5,-9,-7,3,5,9,8,7,6,-7,-3,8,-6,9],[-8,2,-10,-4,-3,8,6,3,-7,-3,-2,8,3,-5,10,-1]],[[-10,-4,6,-1,9,-9,9,1,4,-1,-4,-2,-4,-6,-4,-5],[-3,-7,8,-10,-7,2,-10,-2,-6,-1,-1,-9,-1,-1,5,-9],[8,-7,-2,-5,-5,5,-9,10,-1,6,-5,8,2,-10,9,3],[-5,-6,-7,-6,-8,-8,7,10,10,-9,-3,-10,8,9,-1,-5]],[[-5,3,-9,-4,9,4,9,-3,2,-3,-9,-9,5,4,-4,-2],[9,-1,-6,5,-7,1,-5,-7,8,-1,5,4,1,5,9,2],[-5,-6,10,-6,2,-4,-4,3,3,9,-7,-7,2,-2,1,9],[-7,-5,-8,-3,-8,9,-10,-4,-8,2,-5,-2,10,6,-7,7]],[[1,2,-3,-10,-4,5,-1,8,9,7,-8,10,4,-9,-2,7],[-8,-1,-6,4,-1,-5,-5,6,-10,9,-1,-5,-5,-5,3,-10],[-1,-2,3,-6,-4,-1,-3,-4,-7,2,-1,2,-3,3,-9,7],[-4,-8,6,5,6,-10,10,-3,-8,-4,3,-5,3,2,-2,3]],[[-7,-5,6,2,4,2,-5,-1,-9,2,-1,8,-6,3,9,-4],[-6,9,10,5,-3,-10,-9,3,-7,1,1,-9,2,-5,-9,-9],[-9,-8,-2,-3,-9,5,-5,7,-3,-8,-10,3,3,2,4,-1],[-8,2,-2,-6,9,9,10,-3,-6,1,-2,-5,10,-6,-9,-9]],[[-6,8,7,10,-5,-9,-7,-10,-5,-9,3,1,3,10,-4,8],[10,-1,8,-3,10,-8,2,2,-10,4,6,9,-5,-9,7,-1],[3,-4,-3,6,6,-2,3,-10,6,-6,-1,2,-3,-3,8,7],[-7,-4,7,4,5,6,2,1,-9,-10,2,-4,-3,-5,-4,4]]], dtype = "int32")#candidate|4769|(9, 4, 16)|const|int32
bop_4770 = relay.bitwise_and(var_4768.astype('int32'), relay.reshape(const_4769.astype('int32'), relay.shape_of(var_4768))) # shape=(9, 4, 16)
bop_4778 = relay.less(bop_4770.astype('bool'), relay.reshape(const_4769.astype('bool'), relay.shape_of(bop_4770))) # shape=(9, 4, 16)
output = bop_4778
output2 = bop_4778
func_4782 = relay.Function([var_4768,], output)
mod['func_4782'] = func_4782
mod = relay.transform.InferType()(mod)
var_4783 = relay.var("var_4783", dtype = "int32", shape = (9, 4, 16))#candidate|4783|(9, 4, 16)|var|int32
output = func_4782(var_4783)
func_4784 = relay.Function([var_4783], output)
mutated_mod['func_4784'] = func_4784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2577_call = mod.get_global_var('func_2577')
func_2578_call = mutated_mod.get_global_var('func_2578')
call_4802 = relay.TupleGetItem(func_2577_call(), 0)
call_4803 = relay.TupleGetItem(func_2578_call(), 0)
output = call_4802
output2 = call_4803
func_4804 = relay.Function([], output)
mod['func_4804'] = func_4804
mod = relay.transform.InferType()(mod)
output = func_4804()
func_4805 = relay.Function([], output)
mutated_mod['func_4805'] = func_4805
mutated_mod = relay.transform.InferType()(mutated_mod)
func_517_call = mod.get_global_var('func_517')
func_518_call = mutated_mod.get_global_var('func_518')
call_4863 = func_517_call()
call_4864 = func_517_call()
output = relay.Tuple([call_4863,])
output2 = relay.Tuple([call_4864,])
func_4868 = relay.Function([], output)
mod['func_4868'] = func_4868
mod = relay.transform.InferType()(mod)
output = func_4868()
func_4869 = relay.Function([], output)
mutated_mod['func_4869'] = func_4869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4128_call = mod.get_global_var('func_4128')
func_4129_call = mutated_mod.get_global_var('func_4129')
call_4877 = relay.TupleGetItem(func_4128_call(), 0)
call_4878 = relay.TupleGetItem(func_4129_call(), 0)
func_472_call = mod.get_global_var('func_472')
func_475_call = mutated_mod.get_global_var('func_475')
const_4891 = relay.const([[2.403535],[-9.577360],[-4.071104],[-1.044859],[-6.980244],[-0.389609],[8.861416],[-1.004528],[-2.223412],[0.805480],[4.496086],[4.271775],[-3.570686],[4.887354],[5.193663],[0.543919],[0.336605],[-4.975120],[-2.280838],[6.433394],[8.817787],[-8.892439],[4.390582],[-2.171926],[6.387054],[-3.052905],[5.818330],[4.640500],[-2.226754],[-6.692932],[3.925320],[6.215691],[-2.745900],[4.795619],[-4.381867],[0.251594],[-0.582478],[-9.827530],[-2.940327],[0.084174],[-9.459614],[-2.647718],[7.121434],[0.752465],[-4.695360],[-1.641393],[3.750454],[-5.010479],[1.291215],[-8.909427],[-9.899530],[3.134178],[-6.247430],[-5.997814],[-1.531462],[-5.841262],[3.871349],[2.519508],[-7.742701],[2.452022],[-9.347504],[-7.999786],[4.313370],[1.515703],[-2.539978],[-4.282095],[1.360432],[3.849987],[9.896566],[-0.601880],[3.729779],[-3.984325],[8.297827],[-2.942298],[-0.807171],[-3.146665],[9.457163],[2.924120],[8.942165],[1.112905],[-3.000479],[-1.503269],[2.892608],[7.963813],[-0.973563],[0.980010],[-2.541796],[-6.085423],[2.878515],[2.335419],[-4.953799],[-6.024040],[4.466125],[-5.448175],[6.589239],[-1.776435],[9.543227],[9.987372],[5.263298],[7.506886],[8.057004],[3.906167],[-2.305126],[7.758661],[-9.857727],[-6.041479],[5.347753],[-4.534740],[-6.517614],[1.466723],[-2.719384],[9.795062],[4.696761],[7.695474],[-9.690052],[-6.094903],[5.224696],[6.875090],[8.715867],[2.554583],[-5.695100],[4.990970],[-3.189709],[-9.385576],[-8.838296],[-5.894176],[4.112171],[1.119257],[4.020938],[6.588853],[3.898069],[4.250159],[-0.736364],[8.107444],[9.500903],[6.157246],[-7.851068],[4.216950],[2.045476],[0.091028],[-4.214997],[-4.977041],[3.397183],[-7.652002],[-8.519637],[-2.926245],[7.625720],[-8.292723],[4.570710],[8.438535],[-1.344506],[-4.217094],[4.017355],[-0.820454],[8.082208],[0.346342]], dtype = "float64")#candidate|4891|(156, 1)|const|float64
call_4890 = relay.TupleGetItem(func_472_call(relay.reshape(const_4891.astype('float64'), [4, 13, 3])), 0)
call_4892 = relay.TupleGetItem(func_475_call(relay.reshape(const_4891.astype('float64'), [4, 13, 3])), 0)
func_3843_call = mod.get_global_var('func_3843')
func_3846_call = mutated_mod.get_global_var('func_3846')
const_4895 = relay.const([4,-2,-1,9,-5,-6,-8,8,3,-5,5,-5,1,-9,6,4,-7,-6,1,10,10,-3,-2,4,-9,6,-9,8,-7,-2,-4,10,5,10,5,4,-3,6,5,5,-10,-8,4,-9,-3,-3,-1,8,10,4,5,-3,-2,-8,-10,1,-3,-9,4,-7,2,4,4,-9,-2,-2,-8,7,-5,-9,7,-4,-10,7,-2,-1,-6,-6,-8,9,-8,7,5,8,-1,4,8,8,3,-1,4,9,-8,-2,-2,6,-1,7,-9,7,-5,-7,1,2,3,-10,5,8,-6,10,1,-9,-9,10,5,-7,10,-3,3,8,-9,4,-8,9,-1,2,-5,6,-9,-3,4,5,5,-7,-3,6,-1,-8,-1,5,-8,-5,9,-6,-6,3,8,-3,7,-3,3,4,8,-5,1,-2,-6,-1,-8,5,7,-5,-7,-1,-8,-5,-4,7,3,10,3,-2,-10,-5,-1,2,8,6,-6,10,-1,-7,3,4,7,9,-7,8,-5,6,3,5,-7,-9,-8,-9,3,2,9,4,-2,-5,-4,-8,5,-7,2,-2,-5,-2,-1,1,-6,-1,-1,-2,-8,5,1,2,-5,-6,3,6,10,-2,-10,4,8,-2,8,3,10,-9,1,-6,-10,-5,-10,-4,10,1,9,-5,-1,-7,10,5,7,-10,-5,5,9,-2,-1,-9,-2,-3,6,-9,7,-7,7,-7,-8,-3,3,10,-7,1,7,-3,2,2,-5,8,9,9,7,-10,-2,8,10,7,8,-7,2,6,5,-6,10,-2,-7,-5,-8,-9,-6,6,-3,-5,-5,-8,2,2,3,-8,10,-2,-3,-1,-1,-1,-7,5,4,-3,-2,-7,-6,-2,7,-3,-3,5,-1,-9,9,3,9,-8,-10,3,1,-6,8,-7,1,-1,-5,2,-5,10,1,1,-1,-2,-7,3,-6,6,-1,9,1,6,-10,-1,7,8,5,7,-6,7,5,-3,10,-5,4,-3,-7,10,9,-2,-5,4,10,7,2,1,-5,10,-8,8,-10,7,-2,-5,-10,-7,7,-8,5,-5,1,-6,-2,4,3,2,-3,-3,5,3,-6,4,-4,-10,-10,-5,1,-9,-2,-5,-5,10,-3,2,-2,-7,7,-4,4,7,-9,6,8,4,-10,-4,-5,4,7,8,-3,2,4,9,9,3,2,1,5,-9,4,10,6,-7,-10,-4,8,10,-1,-2,-7,-10,4,-9,9,-2,9,-2,5,-10,6,5,2,-10,6,-3,8,-2,-7,1,-6,8,-4,2,4,2,6,4,5,-10,7,-4,9,5,-4,3,-9,7,5,-5,-1,-7,-6,-4,-6,-10,10,-7,-9,-6,-1,4,1,-5,3,5,7,-3,-6,4,1,-4,7,9,-6,-8,5,-4,7,5,1,6,-2,1,-5,-10,8,-9,-7,-10,7,-7,3,-1,5,2,5,-2,-6,7,-7,-2,-2,1,-1,-2,2,-1,3,5,9,1,-5,3,7,5,-4,10,-9,-7,1,-7,9,6,-1,1,8,3,9,5,5,-10,8,-7,9,7,3,3,-3,7,1,5,-2,-3,6,6,1,-2,-8,-5,-5,8,-8,2,-1,-7,-9,-4,-3,-3,-8,-10,-7,-7,3,3,-8,-6,2,-10,-8,-9,-9,7,1,-3,-1,9,7,-2,-10,10,5,-4,7,2,-1,2,6,-4,-1,6,-1,-1,-3,-1,-7,-2,-9,1,-2,-1,6,5,-3,8,7,8,-1,8,-2,-6,10,-3,-6,-6,7,-1,9,4,-6,-9,-6,-3,-6,10,8,6,4,8,4,-6,1,6,3,3,-2,-4,-9,-5,6,2,-1,-3,-10,5,-6,8,10,7,-6,5,-5,8,4,1,-9,5,3,-5,10,10,-2,-3,-2,6,-3,6,7,-3,7,2,-9,6,-4,7,-2,10,-3,6,5,1,-2,7,-1,2,-6,-4,1,5,2,9,-8,9,4,-7,9,9,9,1,-8,-5,-7,-7,8,6,-5,5,-8,7,2,-2,-5,2,-7,-1,-6,-9,-7,5,-10,7,-8,1,9,-7,-5,1,10,-4,-6,3,-3,-9,9,-8,-5,-6,-7,10,-8,-6,5,-1,-9,-3,-1,-9,9,7,-9,10,-9,-8,5,4,-4,6,-6,-6,3,-9,8,-1,5,-6,4,-10,-4,3,8,-5,-6,4,10,-6,-1,-7,5,5,-7,-4,-9,-8,-5,-2,-6,5,-8,3,-1,10,6,-1,7,-10,-9,7,-1,8,-6,10,9,-2,-6,-4,-4,7,4,-10,3,7,-6,-7,1,-6,-10,-9,-2,8,7,-3,8,10,9,3,2,4,-8,9,-10,6,-9,-9,-5,-9,8,-3,3,8,-5,-3,-3,-9,8,2,-10,6,-3,-2,-1,-1,4,-5,9,-8,6,-3,6,2,7,2,2,9,-6,-6,-4,7,-10,5,-8,4,-4,-5,-9,6,2,-3,9,-10,5,-3,-2,6,-5,-3,-4,8,-4,-10,-3,8,6,10,5,10,5,-8,-4,-10,7,-3,-10,1,-6,-6,-9,4,8,-3,-3,5,-6,6,-9,-10,-10,9,6,4,3,2,-8,7,10,9,3,-1,6,1,-4,4,-6,3,-3,5,-1,-5,-3,3,2,-7,7,-4,-5,-10,5,-2,5,2,-4,-1,6,-4,-10,-4,-10,-5,-9,9,3,-1,-3,1,10,-5,2,1,-6,7,-9,-6,2,-5,-10,2,-6,-2,-8,7,6,-4,2,8,-8,1,6,8,9,-6,10,2,5,-4,-7,-2,-5,-5,4,4,-6,1,2,-1,-7,-10,7,2,6,-6,9,9,-6,2,6,2,-10,-6,-6,-3,-6,-9,-5,-6,7,5,7,1,-6,3,-6,4,10,8,8,9,6,-8,9,1,5,-3,8,8,-4,6,8,7,3,-5,9,-7,-2,-6,-1,6,-3,-10,2,4,1,-7,1,6,-1,7,7,-5,-10,-9,-9,9,-5,-2,-7,2,-8,6,2,5,4,-3,7,9,2,10,-4,-1,8,-7,-2,4,7,3,-3,-5,2,8,-10,7,-7,-1,-6,2,-8,10,10,-3,-5,8], dtype = "int64")#candidate|4895|(1152,)|const|int64
call_4894 = relay.TupleGetItem(func_3843_call(relay.reshape(const_4895.astype('int64'), [12, 8, 12])), 0)
call_4896 = relay.TupleGetItem(func_3846_call(relay.reshape(const_4895.astype('int64'), [12, 8, 12])), 0)
uop_4900 = relay.cos(const_4891.astype('float64')) # shape=(156, 1)
output = relay.Tuple([call_4877,call_4890,call_4894,const_4895,uop_4900,])
output2 = relay.Tuple([call_4878,call_4892,call_4896,const_4895,uop_4900,])
func_4904 = relay.Function([], output)
mod['func_4904'] = func_4904
mod = relay.transform.InferType()(mod)
output = func_4904()
func_4905 = relay.Function([], output)
mutated_mod['func_4905'] = func_4905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_444_call = mod.get_global_var('func_444')
func_446_call = mutated_mod.get_global_var('func_446')
call_4951 = relay.TupleGetItem(func_444_call(), 0)
call_4952 = relay.TupleGetItem(func_446_call(), 0)
func_4394_call = mod.get_global_var('func_4394')
func_4397_call = mutated_mod.get_global_var('func_4397')
var_4959 = relay.var("var_4959", dtype = "float32", shape = (264,))#candidate|4959|(264,)|var|float32
call_4958 = relay.TupleGetItem(func_4394_call(relay.reshape(var_4959.astype('float32'), [11, 12, 2])), 0)
call_4960 = relay.TupleGetItem(func_4397_call(relay.reshape(var_4959.astype('float32'), [11, 12, 2])), 0)
output = relay.Tuple([call_4951,call_4958,var_4959,])
output2 = relay.Tuple([call_4952,call_4960,var_4959,])
func_4962 = relay.Function([var_4959,], output)
mod['func_4962'] = func_4962
mod = relay.transform.InferType()(mod)
mutated_mod['func_4962'] = func_4962
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4963 = relay.var("var_4963", dtype = "float32", shape = (264,))#candidate|4963|(264,)|var|float32
func_4962_call = mutated_mod.get_global_var('func_4962')
call_4964 = func_4962_call(var_4963)
output = call_4964
func_4965 = relay.Function([var_4963], output)
mutated_mod['func_4965'] = func_4965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3419_call = mod.get_global_var('func_3419')
func_3420_call = mutated_mod.get_global_var('func_3420')
call_4995 = relay.TupleGetItem(func_3419_call(), 0)
call_4996 = relay.TupleGetItem(func_3420_call(), 0)
func_3356_call = mod.get_global_var('func_3356')
func_3357_call = mutated_mod.get_global_var('func_3357')
call_4998 = func_3356_call()
call_4999 = func_3356_call()
output = relay.Tuple([call_4995,call_4998,])
output2 = relay.Tuple([call_4996,call_4999,])
func_5002 = relay.Function([], output)
mod['func_5002'] = func_5002
mod = relay.transform.InferType()(mod)
mutated_mod['func_5002'] = func_5002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5002_call = mutated_mod.get_global_var('func_5002')
call_5003 = func_5002_call()
output = call_5003
func_5004 = relay.Function([], output)
mutated_mod['func_5004'] = func_5004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3715_call = mod.get_global_var('func_3715')
func_3717_call = mutated_mod.get_global_var('func_3717')
call_5009 = func_3715_call()
call_5010 = func_3715_call()
func_102_call = mod.get_global_var('func_102')
func_105_call = mutated_mod.get_global_var('func_105')
const_5016 = relay.const([[-5.308372,0.731434,6.478287,5.719524,-3.766827,7.046703],[1.768701,-4.316200,-3.656885,9.456994,6.615926,7.568091],[6.559251,8.525824,7.761636,0.143043,1.902978,-3.214236],[-9.509057,-5.731582,-3.670917,-4.774518,-9.918597,-4.212416],[-2.089583,3.238994,3.324707,7.225464,8.085267,-3.931733],[-7.268165,-0.081102,-7.622812,5.176954,-0.930089,-9.247107],[2.544251,-0.902491,1.403406,-4.711936,-1.413029,2.906547],[-7.418953,4.775171,5.158862,5.075082,4.039389,4.771441],[-0.602489,-1.138275,7.604504,9.915489,8.100352,-1.725352],[1.490282,-3.004625,-9.830362,6.490287,-6.448001,-0.498419],[5.952823,-1.140197,6.891648,-3.601658,-0.785333,-1.495217],[7.855423,-9.376768,2.468878,9.942568,0.547029,0.945798],[-9.049628,-1.892172,7.295421,-0.796200,-2.418704,2.624504],[8.335283,2.669880,7.523434,2.282746,-7.261427,1.130596],[-5.609576,-8.382320,4.771969,-2.442156,-3.027118,-1.008950],[2.304741,-6.302419,8.924053,-1.682603,-4.414403,-0.153698],[6.572414,-6.825224,8.141185,-4.520041,8.207768,8.047585],[-3.536025,-4.851854,7.668063,-0.296368,0.974403,-6.624304],[-1.824937,3.754292,2.704731,-9.226782,9.862625,-8.638064],[5.267320,3.616528,4.967687,0.251792,-0.099073,-5.478687],[-7.026464,-0.676864,-9.520577,0.546920,2.355656,3.287138],[-2.962848,-0.073800,-8.929328,8.048289,9.585578,-5.687561],[0.209944,-9.750656,4.188809,2.497929,3.623275,-9.268426],[7.862598,-2.820286,-3.873283,7.316924,-4.250607,4.758345],[-2.592846,-9.993606,2.832400,-5.984890,-1.787585,-5.566815],[4.679550,9.596549,3.440641,-4.290342,4.146668,-5.684217],[-6.669045,1.190849,9.132433,-4.167023,4.690824,1.712289],[6.716237,4.901528,-8.141285,-4.483375,-8.657098,-8.981143],[2.899340,-6.495962,3.935781,-2.492415,-1.759843,-3.606809],[-5.812096,8.096238,5.984127,-4.005622,-6.918563,-3.677929],[5.472068,-8.487259,5.497501,-2.483732,-2.324271,2.550705],[5.416997,7.504492,5.901678,0.958618,-2.656808,4.943009],[8.197013,8.441863,-8.972919,-1.977852,-9.051843,8.750055],[5.431548,-5.522478,-4.927190,1.247882,9.325461,3.037530],[2.520903,9.361184,9.387395,4.640001,-8.051684,-2.397201],[4.346857,2.599367,9.773526,4.999500,-3.548341,-2.798720],[1.701071,-2.804924,9.042639,-7.137625,-9.951886,-5.946274],[-8.014403,-1.276019,-4.893227,4.492873,1.963732,3.267824],[9.833274,8.305467,-6.509014,-0.176095,7.962113,1.308315],[-0.006681,6.012187,9.145924,-6.311030,-1.257614,-6.283519],[7.370426,-0.114099,-5.339053,-4.021830,-8.239785,5.366159],[8.975844,-9.422947,-5.913126,1.295705,8.089929,5.734855],[8.623225,4.222937,-1.215299,-7.306698,3.162351,-9.489813],[0.984595,-6.052026,-3.813109,-7.608069,6.658235,5.333545],[-6.320996,7.896602,0.578268,-0.540094,-3.194632,-3.143912],[-9.479787,8.836111,9.205352,3.683470,-1.422023,-4.620127],[-1.253560,-4.976408,-6.448995,9.042451,5.062347,-6.708033],[-9.494103,9.367712,-4.724793,1.911112,-1.171093,5.935728],[3.735081,-1.852851,-4.043597,-3.711778,-8.817934,-5.650267],[-6.308590,8.780341,-1.690291,8.206912,7.125226,-4.138784],[-0.181096,-7.942009,-4.196894,9.403671,-7.525688,8.590462],[-9.189539,0.776322,-4.711783,6.891741,-0.890661,-5.956181],[5.796032,7.118178,-2.508033,-8.479251,7.922239,-8.298125],[-9.859512,4.334799,4.153732,2.601210,4.506678,-9.021314],[5.146223,-7.077106,9.929799,-2.062058,-6.163106,8.017458],[0.350918,-1.883285,-8.249939,-0.564674,-4.617023,1.567857],[-5.295054,8.037391,-2.665674,-0.730632,-4.453679,8.185295],[0.515122,-3.733102,3.823096,1.020711,6.473501,1.912193],[-1.169959,9.581301,-2.424312,-5.288318,5.703643,-2.579869],[-7.328923,3.828608,2.824763,-8.968667,4.518909,8.189243],[-6.774030,4.347993,-4.801428,8.349485,5.834614,1.904422],[6.075793,-9.906192,5.165713,-0.013848,0.984225,-4.828542],[-4.315685,-1.230627,7.583339,-4.833680,-8.688888,-1.603214],[8.820476,4.816237,-5.522415,-9.792532,-2.187911,-5.118695],[9.689173,4.620550,7.986333,9.325588,-4.871224,8.334696],[1.516626,8.664216,5.318870,-7.267024,9.693017,2.357249],[-0.122346,-1.201203,6.147085,7.924171,4.429396,9.739317],[-3.275853,3.414526,-4.936023,5.694214,-5.984855,7.001250],[-8.634395,-8.080831,3.496971,9.893011,2.976662,8.980934],[-3.966451,0.772845,1.200579,-4.601835,-6.429427,4.166651],[-6.524050,-6.629314,5.796687,7.382629,-5.996558,-2.917041],[4.754992,0.298583,5.966596,6.570430,2.737910,9.246430],[-4.820059,1.620153,6.191274,2.363827,7.701672,6.396320],[-0.778612,-3.786836,-0.880773,-3.866133,-5.230588,6.614251],[-8.682899,5.396671,1.816430,9.804667,3.241678,-6.629256],[7.674224,-7.159170,-2.211415,5.779185,-7.318093,2.572880],[-4.072763,7.581143,3.519295,-3.011570,4.247428,-5.957701],[6.411488,-0.413111,-1.830454,1.199897,2.675293,-6.273436],[5.250477,-4.255841,1.762489,8.443707,9.136509,-0.839956],[8.577936,2.642376,-2.814922,1.721772,9.476638,-7.090484],[4.779156,8.738290,-2.858338,-7.405007,0.315492,3.762623],[-1.785195,3.694099,9.177637,-1.753226,-9.196303,-8.660721],[0.336511,-8.462655,9.081552,-5.893428,9.404198,7.843101],[8.951847,3.511507,-8.425692,6.218672,4.903409,9.512743],[-6.287007,6.567979,0.178311,-8.680844,-3.947301,9.199781],[4.776912,-3.867146,1.252271,-4.427458,1.463479,4.790888],[2.746137,-5.099854,9.696078,2.260738,8.966222,2.493999],[-6.695149,-8.456399,-8.369436,0.971938,7.077654,-2.275859],[3.700723,-2.963341,7.711741,3.523997,-0.477366,4.072531],[1.455956,-3.704553,-5.387934,8.881446,9.601949,9.371314],[0.834300,3.882263,-2.829570,0.184262,4.138121,-0.716125],[7.309887,4.249482,9.251961,-2.304440,5.285235,1.134292],[-3.076951,7.588188,-0.545036,6.732889,3.014982,0.954680],[1.231647,8.686313,-1.835957,3.313324,1.451762,5.261876],[4.171067,4.305890,-7.011356,-2.570807,2.464681,-1.472025],[-0.060492,4.313730,0.504220,2.183257,8.578260,2.764694],[-3.451754,-9.447599,9.450720,-9.560972,8.107717,5.253752],[4.862840,-3.618455,5.018989,-5.726226,-9.102097,1.649615],[-4.336541,-8.384229,-7.061795,0.853669,-8.176920,-7.074375],[-7.119216,9.320126,9.454509,8.685804,-5.743822,1.965800],[9.628782,-0.443095,-3.814228,0.849146,-8.201993,-9.937947],[4.555463,-3.830517,5.488738,1.833969,3.946608,5.173355],[0.635154,0.002606,-7.630636,-4.653208,2.382688,-1.711672],[-7.501470,-5.052912,8.131190,1.462902,2.112614,9.124847],[9.359178,-5.943967,4.193356,5.050781,-6.116274,-9.531009],[4.114735,-2.077882,5.743743,-8.600444,-7.922179,2.793916],[-6.425835,-8.315012,-4.575091,-7.933089,-4.463347,-0.064288],[3.636193,5.570068,9.144935,-8.317014,-8.299793,9.455123],[3.326164,7.397948,-1.714506,-2.091031,-9.163835,-2.878568],[-4.571663,-2.045222,4.755170,-1.448928,-0.462562,3.285405]], dtype = "float32")#candidate|5016|(110, 6)|const|float32
call_5015 = relay.TupleGetItem(func_102_call(relay.reshape(const_5016.astype('float32'), [12, 11, 5])), 0)
call_5017 = relay.TupleGetItem(func_105_call(relay.reshape(const_5016.astype('float32'), [12, 11, 5])), 0)
output = relay.Tuple([call_5009,call_5015,const_5016,])
output2 = relay.Tuple([call_5010,call_5017,const_5016,])
func_5026 = relay.Function([], output)
mod['func_5026'] = func_5026
mod = relay.transform.InferType()(mod)
mutated_mod['func_5026'] = func_5026
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5026_call = mutated_mod.get_global_var('func_5026')
call_5027 = func_5026_call()
output = call_5027
func_5028 = relay.Function([], output)
mutated_mod['func_5028'] = func_5028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3356_call = mod.get_global_var('func_3356')
func_3357_call = mutated_mod.get_global_var('func_3357')
call_5040 = func_3356_call()
call_5041 = func_3356_call()
output = call_5040
output2 = call_5041
func_5051 = relay.Function([], output)
mod['func_5051'] = func_5051
mod = relay.transform.InferType()(mod)
output = func_5051()
func_5052 = relay.Function([], output)
mutated_mod['func_5052'] = func_5052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_585_call = mod.get_global_var('func_585')
func_586_call = mutated_mod.get_global_var('func_586')
call_5066 = relay.TupleGetItem(func_585_call(), 1)
call_5067 = relay.TupleGetItem(func_586_call(), 1)
func_4447_call = mod.get_global_var('func_4447')
func_4448_call = mutated_mod.get_global_var('func_4448')
call_5104 = relay.TupleGetItem(func_4447_call(), 2)
call_5105 = relay.TupleGetItem(func_4448_call(), 2)
output = relay.Tuple([call_5066,call_5104,])
output2 = relay.Tuple([call_5067,call_5105,])
func_5106 = relay.Function([], output)
mod['func_5106'] = func_5106
mod = relay.transform.InferType()(mod)
mutated_mod['func_5106'] = func_5106
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5106_call = mutated_mod.get_global_var('func_5106')
call_5107 = func_5106_call()
output = call_5107
func_5108 = relay.Function([], output)
mutated_mod['func_5108'] = func_5108
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5175 = relay.var("var_5175", dtype = "float32", shape = (12, 4, 5))#candidate|5175|(12, 4, 5)|var|float32
uop_5176 = relay.atanh(var_5175.astype('float32')) # shape=(12, 4, 5)
var_5181 = relay.var("var_5181", dtype = "float32", shape = (12, 4, 5))#candidate|5181|(12, 4, 5)|var|float32
bop_5182 = relay.not_equal(uop_5176.astype('bool'), relay.reshape(var_5181.astype('bool'), relay.shape_of(uop_5176))) # shape=(12, 4, 5)
func_472_call = mod.get_global_var('func_472')
func_475_call = mutated_mod.get_global_var('func_475')
const_5187 = relay.const([-6.572672,4.464725,2.962965,-7.537071,3.766279,-9.544270,-6.737544,-1.138432,9.757563,-1.490857,-1.168656,-2.648642,-3.281359,2.782276,-5.209115,-6.638106,-3.489277,7.038701,4.678122,-4.428175,-5.673413,-8.531591,-8.918787,1.730823,8.829127,4.011494,5.472619,4.163427,-5.941928,7.838507,-8.369138,9.177865,5.746523,6.101682,-0.624171,2.773052,-1.520834,4.905826,-4.825762,-6.433467,4.479211,6.822555,3.808534,-6.524591,9.334962,-1.626622,5.488718,-5.405727,1.318543,-8.682398,1.237715,-3.175819,2.594282,-4.179452,-8.039693,1.853005,-2.607315,-8.648663,-0.434230,1.377425,1.470516,3.989155,1.098578,7.825659,0.749705,3.656257,-2.863201,0.453348,4.257830,7.428450,-0.787837,4.328211,-0.552772,6.992543,7.831789,-1.382198,-7.740774,8.946640,-0.199391,-2.238784,-2.669937,-1.229490,-0.686086,5.972681,-3.533488,2.955058,6.356746,8.198538,8.400776,-7.113862,-5.509395,0.833725,0.916789,-5.796584,4.099264,7.016412,-0.740656,-3.755599,5.603695,6.817438,7.598475,8.584982,5.464327,-4.821208,2.484772,1.591690,2.865523,-6.710653,-6.098997,-2.266194,-6.650935,3.340422,-0.920831,0.668465,5.908633,3.951878,8.869418,-1.974066,8.654728,4.531983,4.222273,-1.078149,7.587389,9.243216,-5.213763,-4.255025,-2.061119,5.187783,0.751016,-1.086227,6.759856,9.357357,-1.366768,-4.392501,-7.863558,-1.297562,-1.005217,6.617511,-4.551136,4.282401,-3.535593,4.440901,-7.650776,5.717812,0.945322,-4.535129,3.551442,6.829484,3.574916,-5.355411,-2.942701,-1.353097,2.873281,-4.558284,-0.928066,-7.623578], dtype = "float64")#candidate|5187|(156,)|const|float64
call_5186 = relay.TupleGetItem(func_472_call(relay.reshape(const_5187.astype('float64'), [4, 13, 3])), 0)
call_5188 = relay.TupleGetItem(func_475_call(relay.reshape(const_5187.astype('float64'), [4, 13, 3])), 0)
output = relay.Tuple([bop_5182,call_5186,const_5187,])
output2 = relay.Tuple([bop_5182,call_5188,const_5187,])
func_5194 = relay.Function([var_5175,var_5181,], output)
mod['func_5194'] = func_5194
mod = relay.transform.InferType()(mod)
mutated_mod['func_5194'] = func_5194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5194_call = mutated_mod.get_global_var('func_5194')
var_5196 = relay.var("var_5196", dtype = "float32", shape = (12, 4, 5))#candidate|5196|(12, 4, 5)|var|float32
var_5197 = relay.var("var_5197", dtype = "float32", shape = (12, 4, 5))#candidate|5197|(12, 4, 5)|var|float32
call_5195 = func_5194_call(var_5196,var_5197,)
output = call_5195
func_5198 = relay.Function([var_5196,var_5197,], output)
mutated_mod['func_5198'] = func_5198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3419_call = mod.get_global_var('func_3419')
func_3420_call = mutated_mod.get_global_var('func_3420')
call_5300 = relay.TupleGetItem(func_3419_call(), 0)
call_5301 = relay.TupleGetItem(func_3420_call(), 0)
func_1360_call = mod.get_global_var('func_1360')
func_1361_call = mutated_mod.get_global_var('func_1361')
call_5319 = relay.TupleGetItem(func_1360_call(), 2)
call_5320 = relay.TupleGetItem(func_1361_call(), 2)
output = relay.Tuple([call_5300,call_5319,])
output2 = relay.Tuple([call_5301,call_5320,])
func_5325 = relay.Function([], output)
mod['func_5325'] = func_5325
mod = relay.transform.InferType()(mod)
output = func_5325()
func_5326 = relay.Function([], output)
mutated_mod['func_5326'] = func_5326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3356_call = mod.get_global_var('func_3356')
func_3357_call = mutated_mod.get_global_var('func_3357')
call_5332 = func_3356_call()
call_5333 = func_3356_call()
func_741_call = mod.get_global_var('func_741')
func_742_call = mutated_mod.get_global_var('func_742')
call_5334 = relay.TupleGetItem(func_741_call(), 0)
call_5335 = relay.TupleGetItem(func_742_call(), 0)
func_3715_call = mod.get_global_var('func_3715')
func_3717_call = mutated_mod.get_global_var('func_3717')
call_5340 = func_3715_call()
call_5341 = func_3715_call()
bop_5352 = relay.divide(call_5334.astype('float32'), relay.reshape(call_5340.astype('float32'), relay.shape_of(call_5334))) # shape=(1, 12, 2)
bop_5355 = relay.divide(call_5335.astype('float32'), relay.reshape(call_5341.astype('float32'), relay.shape_of(call_5335))) # shape=(1, 12, 2)
output = relay.Tuple([call_5332,bop_5352,])
output2 = relay.Tuple([call_5333,bop_5355,])
func_5356 = relay.Function([], output)
mod['func_5356'] = func_5356
mod = relay.transform.InferType()(mod)
output = func_5356()
func_5357 = relay.Function([], output)
mutated_mod['func_5357'] = func_5357
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2361_call = mod.get_global_var('func_2361')
func_2362_call = mutated_mod.get_global_var('func_2362')
call_5451 = relay.TupleGetItem(func_2361_call(), 0)
call_5452 = relay.TupleGetItem(func_2362_call(), 0)
output = call_5451
output2 = call_5452
func_5468 = relay.Function([], output)
mod['func_5468'] = func_5468
mod = relay.transform.InferType()(mod)
mutated_mod['func_5468'] = func_5468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5468_call = mutated_mod.get_global_var('func_5468')
call_5469 = func_5468_call()
output = call_5469
func_5470 = relay.Function([], output)
mutated_mod['func_5470'] = func_5470
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4447_call = mod.get_global_var('func_4447')
func_4448_call = mutated_mod.get_global_var('func_4448')
call_5510 = relay.TupleGetItem(func_4447_call(), 0)
call_5511 = relay.TupleGetItem(func_4448_call(), 0)
output = relay.Tuple([call_5510,])
output2 = relay.Tuple([call_5511,])
func_5548 = relay.Function([], output)
mod['func_5548'] = func_5548
mod = relay.transform.InferType()(mod)
mutated_mod['func_5548'] = func_5548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5548_call = mutated_mod.get_global_var('func_5548')
call_5549 = func_5548_call()
output = call_5549
func_5550 = relay.Function([], output)
mutated_mod['func_5550'] = func_5550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5106_call = mod.get_global_var('func_5106')
func_5108_call = mutated_mod.get_global_var('func_5108')
call_5551 = relay.TupleGetItem(func_5106_call(), 0)
call_5552 = relay.TupleGetItem(func_5108_call(), 0)
output = relay.Tuple([call_5551,])
output2 = relay.Tuple([call_5552,])
func_5561 = relay.Function([], output)
mod['func_5561'] = func_5561
mod = relay.transform.InferType()(mod)
mutated_mod['func_5561'] = func_5561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5561_call = mutated_mod.get_global_var('func_5561')
call_5562 = func_5561_call()
output = call_5562
func_5563 = relay.Function([], output)
mutated_mod['func_5563'] = func_5563
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5626 = relay.var("var_5626", dtype = "float32", shape = (3, 13, 6))#candidate|5626|(3, 13, 6)|var|float32
var_5627 = relay.var("var_5627", dtype = "float32", shape = (3, 13, 6))#candidate|5627|(3, 13, 6)|var|float32
bop_5628 = relay.floor_divide(var_5626.astype('float32'), relay.reshape(var_5627.astype('float32'), relay.shape_of(var_5626))) # shape=(3, 13, 6)
output = bop_5628
output2 = bop_5628
func_5653 = relay.Function([var_5626,var_5627,], output)
mod['func_5653'] = func_5653
mod = relay.transform.InferType()(mod)
var_5654 = relay.var("var_5654", dtype = "float32", shape = (3, 13, 6))#candidate|5654|(3, 13, 6)|var|float32
var_5655 = relay.var("var_5655", dtype = "float32", shape = (3, 13, 6))#candidate|5655|(3, 13, 6)|var|float32
output = func_5653(var_5654,var_5655,)
func_5656 = relay.Function([var_5654,var_5655,], output)
mutated_mod['func_5656'] = func_5656
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5703 = relay.var("var_5703", dtype = "float64", shape = (10, 9, 11))#candidate|5703|(10, 9, 11)|var|float64
uop_5704 = relay.log(var_5703.astype('float64')) # shape=(10, 9, 11)
func_1462_call = mod.get_global_var('func_1462')
func_1463_call = mutated_mod.get_global_var('func_1463')
call_5707 = func_1462_call()
call_5708 = func_1462_call()
output = relay.Tuple([uop_5704,call_5707,])
output2 = relay.Tuple([uop_5704,call_5708,])
func_5711 = relay.Function([var_5703,], output)
mod['func_5711'] = func_5711
mod = relay.transform.InferType()(mod)
mutated_mod['func_5711'] = func_5711
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5712 = relay.var("var_5712", dtype = "float64", shape = (10, 9, 11))#candidate|5712|(10, 9, 11)|var|float64
func_5711_call = mutated_mod.get_global_var('func_5711')
call_5713 = func_5711_call(var_5712)
output = call_5713
func_5714 = relay.Function([var_5712], output)
mutated_mod['func_5714'] = func_5714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4804_call = mod.get_global_var('func_4804')
func_4805_call = mutated_mod.get_global_var('func_4805')
call_5816 = func_4804_call()
call_5817 = func_4804_call()
var_5824 = relay.var("var_5824", dtype = "float32", shape = (16, 12, 2))#candidate|5824|(16, 12, 2)|var|float32
bop_5825 = relay.mod(call_5816.astype('float64'), var_5824.astype('float64')) # shape=(16, 12, 2)
bop_5828 = relay.mod(call_5817.astype('float64'), var_5824.astype('float64')) # shape=(16, 12, 2)
output = relay.Tuple([bop_5825,])
output2 = relay.Tuple([bop_5828,])
func_5830 = relay.Function([var_5824,], output)
mod['func_5830'] = func_5830
mod = relay.transform.InferType()(mod)
var_5831 = relay.var("var_5831", dtype = "float32", shape = (16, 12, 2))#candidate|5831|(16, 12, 2)|var|float32
output = func_5830(var_5831)
func_5832 = relay.Function([var_5831], output)
mutated_mod['func_5832'] = func_5832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_958_call = mod.get_global_var('func_958')
func_960_call = mutated_mod.get_global_var('func_960')
call_5913 = relay.TupleGetItem(func_958_call(), 0)
call_5914 = relay.TupleGetItem(func_960_call(), 0)
func_2773_call = mod.get_global_var('func_2773')
func_2775_call = mutated_mod.get_global_var('func_2775')
call_5916 = relay.TupleGetItem(func_2773_call(), 0)
call_5917 = relay.TupleGetItem(func_2775_call(), 0)
output = relay.Tuple([call_5913,call_5916,])
output2 = relay.Tuple([call_5914,call_5917,])
func_5934 = relay.Function([], output)
mod['func_5934'] = func_5934
mod = relay.transform.InferType()(mod)
output = func_5934()
func_5935 = relay.Function([], output)
mutated_mod['func_5935'] = func_5935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_958_call = mod.get_global_var('func_958')
func_960_call = mutated_mod.get_global_var('func_960')
call_6091 = relay.TupleGetItem(func_958_call(), 0)
call_6092 = relay.TupleGetItem(func_960_call(), 0)
uop_6127 = relay.atan(call_6091.astype('float64')) # shape=(1, 12, 2)
uop_6129 = relay.atan(call_6092.astype('float64')) # shape=(1, 12, 2)
output = relay.Tuple([uop_6127,])
output2 = relay.Tuple([uop_6129,])
func_6133 = relay.Function([], output)
mod['func_6133'] = func_6133
mod = relay.transform.InferType()(mod)
output = func_6133()
func_6134 = relay.Function([], output)
mutated_mod['func_6134'] = func_6134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4336_call = mod.get_global_var('func_4336')
func_4338_call = mutated_mod.get_global_var('func_4338')
call_6191 = relay.TupleGetItem(func_4336_call(), 0)
call_6192 = relay.TupleGetItem(func_4338_call(), 0)
output = call_6191
output2 = call_6192
func_6193 = relay.Function([], output)
mod['func_6193'] = func_6193
mod = relay.transform.InferType()(mod)
mutated_mod['func_6193'] = func_6193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6193_call = mutated_mod.get_global_var('func_6193')
call_6194 = func_6193_call()
output = call_6194
func_6195 = relay.Function([], output)
mutated_mod['func_6195'] = func_6195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2920_call = mod.get_global_var('func_2920')
func_2922_call = mutated_mod.get_global_var('func_2922')
call_6199 = relay.TupleGetItem(func_2920_call(), 1)
call_6200 = relay.TupleGetItem(func_2922_call(), 1)
output = relay.Tuple([call_6199,])
output2 = relay.Tuple([call_6200,])
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
func_5002_call = mod.get_global_var('func_5002')
func_5004_call = mutated_mod.get_global_var('func_5004')
call_6260 = relay.TupleGetItem(func_5002_call(), 0)
call_6261 = relay.TupleGetItem(func_5004_call(), 0)
const_6267 = relay.const([[[6,9],[-3,-3],[5,-8],[-9,-2],[-3,-2],[5,1],[5,-7],[6,-2],[-8,-4],[-4,-10],[1,1],[9,9]]], dtype = "int8")#candidate|6267|(1, 12, 2)|const|int8
bop_6268 = relay.bitwise_xor(call_6260.astype('uint64'), relay.reshape(const_6267.astype('uint64'), relay.shape_of(call_6260))) # shape=(1, 12, 2)
bop_6271 = relay.bitwise_xor(call_6261.astype('uint64'), relay.reshape(const_6267.astype('uint64'), relay.shape_of(call_6261))) # shape=(1, 12, 2)
func_6133_call = mod.get_global_var('func_6133')
func_6134_call = mutated_mod.get_global_var('func_6134')
call_6272 = relay.TupleGetItem(func_6133_call(), 0)
call_6273 = relay.TupleGetItem(func_6134_call(), 0)
func_5548_call = mod.get_global_var('func_5548')
func_5550_call = mutated_mod.get_global_var('func_5550')
call_6277 = relay.TupleGetItem(func_5548_call(), 0)
call_6278 = relay.TupleGetItem(func_5550_call(), 0)
func_5561_call = mod.get_global_var('func_5561')
func_5563_call = mutated_mod.get_global_var('func_5563')
call_6281 = relay.TupleGetItem(func_5561_call(), 0)
call_6282 = relay.TupleGetItem(func_5563_call(), 0)
func_1127_call = mod.get_global_var('func_1127')
func_1129_call = mutated_mod.get_global_var('func_1129')
call_6283 = relay.TupleGetItem(func_1127_call(), 0)
call_6284 = relay.TupleGetItem(func_1129_call(), 0)
var_6289 = relay.var("var_6289", dtype = "uint64", shape = (2, 12, 2))#candidate|6289|(2, 12, 2)|var|uint64
bop_6290 = relay.greater_equal(bop_6268.astype('bool'), var_6289.astype('bool')) # shape=(2, 12, 2)
bop_6293 = relay.greater_equal(bop_6271.astype('bool'), var_6289.astype('bool')) # shape=(2, 12, 2)
var_6299 = relay.var("var_6299", dtype = "float64", shape = (16, 12, 2))#candidate|6299|(16, 12, 2)|var|float64
bop_6300 = relay.floor_mod(call_6272.astype('float32'), var_6299.astype('float32')) # shape=(16, 12, 2)
bop_6303 = relay.floor_mod(call_6273.astype('float32'), var_6299.astype('float32')) # shape=(16, 12, 2)
output = relay.Tuple([call_6277,call_6281,call_6283,bop_6290,bop_6300,])
output2 = relay.Tuple([call_6278,call_6282,call_6284,bop_6293,bop_6303,])
func_6322 = relay.Function([var_6289,var_6299,], output)
mod['func_6322'] = func_6322
mod = relay.transform.InferType()(mod)
mutated_mod['func_6322'] = func_6322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6322_call = mutated_mod.get_global_var('func_6322')
var_6324 = relay.var("var_6324", dtype = "uint64", shape = (2, 12, 2))#candidate|6324|(2, 12, 2)|var|uint64
var_6325 = relay.var("var_6325", dtype = "float64", shape = (16, 12, 2))#candidate|6325|(16, 12, 2)|var|float64
call_6323 = func_6322_call(var_6324,var_6325,)
output = call_6323
func_6326 = relay.Function([var_6324,var_6325,], output)
mutated_mod['func_6326'] = func_6326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5325_call = mod.get_global_var('func_5325')
func_5326_call = mutated_mod.get_global_var('func_5326')
call_6367 = relay.TupleGetItem(func_5325_call(), 0)
call_6368 = relay.TupleGetItem(func_5326_call(), 0)
var_6371 = relay.var("var_6371", dtype = "int8", shape = (10, 12, 2))#candidate|6371|(10, 12, 2)|var|int8
bop_6372 = relay.logical_and(call_6367.astype('bool'), var_6371.astype('bool')) # shape=(10, 12, 2)
bop_6375 = relay.logical_and(call_6368.astype('bool'), var_6371.astype('bool')) # shape=(10, 12, 2)
uop_6384 = relay.asin(bop_6372.astype('float64')) # shape=(10, 12, 2)
uop_6386 = relay.asin(bop_6375.astype('float64')) # shape=(10, 12, 2)
func_3449_call = mod.get_global_var('func_3449')
func_3450_call = mutated_mod.get_global_var('func_3450')
call_6403 = relay.TupleGetItem(func_3449_call(), 0)
call_6404 = relay.TupleGetItem(func_3450_call(), 0)
func_2683_call = mod.get_global_var('func_2683')
func_2685_call = mutated_mod.get_global_var('func_2685')
call_6405 = func_2683_call()
call_6406 = func_2683_call()
bop_6409 = relay.multiply(uop_6384.astype('float32'), call_6367.astype('float32')) # shape=(10, 12, 2)
bop_6412 = relay.multiply(uop_6386.astype('float32'), call_6368.astype('float32')) # shape=(10, 12, 2)
bop_6414 = relay.bitwise_xor(uop_6384.astype('uint64'), relay.reshape(bop_6409.astype('uint64'), relay.shape_of(uop_6384))) # shape=(10, 12, 2)
bop_6417 = relay.bitwise_xor(uop_6386.astype('uint64'), relay.reshape(bop_6412.astype('uint64'), relay.shape_of(uop_6386))) # shape=(10, 12, 2)
var_6434 = relay.var("var_6434", dtype = "uint64", shape = (10, 12, 2))#candidate|6434|(10, 12, 2)|var|uint64
bop_6435 = relay.subtract(bop_6414.astype('float32'), relay.reshape(var_6434.astype('float32'), relay.shape_of(bop_6414))) # shape=(10, 12, 2)
bop_6438 = relay.subtract(bop_6417.astype('float32'), relay.reshape(var_6434.astype('float32'), relay.shape_of(bop_6417))) # shape=(10, 12, 2)
var_6451 = relay.var("var_6451", dtype = "float64", shape = (10, 12, 2))#candidate|6451|(10, 12, 2)|var|float64
bop_6452 = relay.greater(uop_6384.astype('bool'), relay.reshape(var_6451.astype('bool'), relay.shape_of(uop_6384))) # shape=(10, 12, 2)
bop_6455 = relay.greater(uop_6386.astype('bool'), relay.reshape(var_6451.astype('bool'), relay.shape_of(uop_6386))) # shape=(10, 12, 2)
output = relay.Tuple([call_6403,call_6405,bop_6435,bop_6452,])
output2 = relay.Tuple([call_6404,call_6406,bop_6438,bop_6455,])
func_6456 = relay.Function([var_6371,var_6434,var_6451,], output)
mod['func_6456'] = func_6456
mod = relay.transform.InferType()(mod)
mutated_mod['func_6456'] = func_6456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6456_call = mutated_mod.get_global_var('func_6456')
var_6458 = relay.var("var_6458", dtype = "int8", shape = (10, 12, 2))#candidate|6458|(10, 12, 2)|var|int8
var_6459 = relay.var("var_6459", dtype = "uint64", shape = (10, 12, 2))#candidate|6459|(10, 12, 2)|var|uint64
var_6460 = relay.var("var_6460", dtype = "float64", shape = (10, 12, 2))#candidate|6460|(10, 12, 2)|var|float64
call_6457 = func_6456_call(var_6458,var_6459,var_6460,)
output = call_6457
func_6461 = relay.Function([var_6458,var_6459,var_6460,], output)
mutated_mod['func_6461'] = func_6461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3449_call = mod.get_global_var('func_3449')
func_3450_call = mutated_mod.get_global_var('func_3450')
call_6594 = relay.TupleGetItem(func_3449_call(), 0)
call_6595 = relay.TupleGetItem(func_3450_call(), 0)
var_6611 = relay.var("var_6611", dtype = "float32", shape = (15, 12, 2))#candidate|6611|(15, 12, 2)|var|float32
bop_6612 = relay.bitwise_or(call_6594.astype('uint16'), var_6611.astype('uint16')) # shape=(15, 12, 2)
bop_6615 = relay.bitwise_or(call_6595.astype('uint16'), var_6611.astype('uint16')) # shape=(15, 12, 2)
output = bop_6612
output2 = bop_6615
func_6624 = relay.Function([var_6611,], output)
mod['func_6624'] = func_6624
mod = relay.transform.InferType()(mod)
var_6625 = relay.var("var_6625", dtype = "float32", shape = (15, 12, 2))#candidate|6625|(15, 12, 2)|var|float32
output = func_6624(var_6625)
func_6626 = relay.Function([var_6625], output)
mutated_mod['func_6626'] = func_6626
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4756_call = mod.get_global_var('func_4756')
func_4758_call = mutated_mod.get_global_var('func_4758')
call_6648 = func_4756_call()
call_6649 = func_4756_call()
output = relay.Tuple([call_6648,])
output2 = relay.Tuple([call_6649,])
func_6659 = relay.Function([], output)
mod['func_6659'] = func_6659
mod = relay.transform.InferType()(mod)
output = func_6659()
func_6660 = relay.Function([], output)
mutated_mod['func_6660'] = func_6660
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6661 = relay.var("var_6661", dtype = "uint16", shape = (14, 5, 6))#candidate|6661|(14, 5, 6)|var|uint16
const_6662 = relay.const([[[8,3,3,1,6,-5],[2,1,10,-5,6,7],[-6,-4,9,-6,4,-6],[9,-1,7,-4,-1,-7],[2,9,7,1,8,-2]],[[-1,-3,8,-2,-9,1],[-8,-4,-7,-9,-3,5],[6,-3,3,-1,-4,1],[-8,-10,-3,-2,4,-9],[-7,10,-7,-1,-2,7]],[[-10,2,-7,-9,-4,-1],[-1,-8,-8,-8,5,4],[2,7,10,9,-4,-7],[4,5,6,-4,8,-2],[3,1,9,-2,-1,-4]],[[2,-2,-4,7,-4,5],[8,-6,5,3,9,6],[1,8,-6,4,6,4],[4,8,-6,7,6,10],[-1,-7,-9,8,-10,2]],[[7,-4,4,4,3,-8],[-7,-3,-8,2,8,-2],[4,-6,6,-2,4,7],[6,-5,-3,10,-10,3],[-5,-9,-8,-9,3,-9]],[[-3,-6,-7,-6,6,3],[-6,1,5,-4,-1,-3],[-6,-1,10,-9,-9,2],[10,10,-1,5,-6,-1],[-2,-1,-8,4,-9,-4]],[[-5,1,-10,1,-3,5],[-5,-1,-9,-2,-7,-6],[7,10,4,-4,9,-4],[-10,-6,-7,-9,1,3],[-2,3,-8,-8,-8,3]],[[-4,-1,-4,-9,-2,-9],[6,-3,-8,9,1,-3],[10,6,-2,1,5,7],[9,-4,-1,-1,-1,-5],[1,2,7,-3,-7,-6]],[[7,2,-1,3,-7,2],[10,-6,-10,-3,-5,4],[-8,-1,-7,3,4,10],[-4,-5,10,8,3,-2],[-5,5,-9,1,8,-4]],[[9,-1,-1,-10,3,-8],[5,2,2,-2,-10,6],[-9,-7,-1,4,-8,-4],[-7,6,2,-1,-1,-4],[9,-7,-4,-8,-4,-10]],[[8,8,10,-5,-8,4],[-4,-4,10,-6,-5,-5],[10,2,10,10,7,-2],[-9,1,-7,-7,2,3],[-9,-10,-6,3,-10,-9]],[[-8,-6,8,-1,4,-4],[9,-1,-3,4,7,-6],[8,-8,-8,-9,-7,-1],[-5,-2,4,-2,-7,5],[-9,-2,2,-9,1,1]],[[4,6,-6,-8,9,10],[6,-8,4,5,-2,-2],[-6,7,6,-7,-9,-4],[9,-6,2,2,9,-4],[-3,8,5,10,-1,-1]],[[6,-9,-2,-1,-7,-9],[-4,-10,3,8,3,1],[-8,-1,9,-5,-1,-1],[-9,2,-3,6,4,-2],[8,-2,8,10,4,6]]], dtype = "uint16")#candidate|6662|(14, 5, 6)|const|uint16
bop_6663 = relay.bitwise_or(var_6661.astype('uint16'), relay.reshape(const_6662.astype('uint16'), relay.shape_of(var_6661))) # shape=(14, 5, 6)
output = relay.Tuple([bop_6663,])
output2 = relay.Tuple([bop_6663,])
func_6666 = relay.Function([var_6661,], output)
mod['func_6666'] = func_6666
mod = relay.transform.InferType()(mod)
var_6667 = relay.var("var_6667", dtype = "uint16", shape = (14, 5, 6))#candidate|6667|(14, 5, 6)|var|uint16
output = func_6666(var_6667)
func_6668 = relay.Function([var_6667], output)
mutated_mod['func_6668'] = func_6668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4729_call = mod.get_global_var('func_4729')
func_4730_call = mutated_mod.get_global_var('func_4730')
call_6676 = relay.TupleGetItem(func_4729_call(), 0)
call_6677 = relay.TupleGetItem(func_4730_call(), 0)
output = relay.Tuple([call_6676,])
output2 = relay.Tuple([call_6677,])
func_6683 = relay.Function([], output)
mod['func_6683'] = func_6683
mod = relay.transform.InferType()(mod)
mutated_mod['func_6683'] = func_6683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6683_call = mutated_mod.get_global_var('func_6683')
call_6684 = func_6683_call()
output = call_6684
func_6685 = relay.Function([], output)
mutated_mod['func_6685'] = func_6685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1127_call = mod.get_global_var('func_1127')
func_1129_call = mutated_mod.get_global_var('func_1129')
call_6741 = relay.TupleGetItem(func_1127_call(), 0)
call_6742 = relay.TupleGetItem(func_1129_call(), 0)
func_4868_call = mod.get_global_var('func_4868')
func_4869_call = mutated_mod.get_global_var('func_4869')
call_6752 = relay.TupleGetItem(func_4868_call(), 0)
call_6753 = relay.TupleGetItem(func_4869_call(), 0)
bop_6781 = relay.greater_equal(call_6741.astype('bool'), relay.reshape(call_6752.astype('bool'), relay.shape_of(call_6741))) # shape=(1, 12, 2)
bop_6784 = relay.greater_equal(call_6742.astype('bool'), relay.reshape(call_6753.astype('bool'), relay.shape_of(call_6742))) # shape=(1, 12, 2)
output = bop_6781
output2 = bop_6784
func_6789 = relay.Function([], output)
mod['func_6789'] = func_6789
mod = relay.transform.InferType()(mod)
mutated_mod['func_6789'] = func_6789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6789_call = mutated_mod.get_global_var('func_6789')
call_6790 = func_6789_call()
output = call_6790
func_6791 = relay.Function([], output)
mutated_mod['func_6791'] = func_6791
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1067_call = mod.get_global_var('func_1067')
func_1069_call = mutated_mod.get_global_var('func_1069')
call_6821 = relay.TupleGetItem(func_1067_call(), 0)
call_6822 = relay.TupleGetItem(func_1069_call(), 0)
func_3660_call = mod.get_global_var('func_3660')
func_3662_call = mutated_mod.get_global_var('func_3662')
call_6829 = func_3660_call()
call_6830 = func_3660_call()
output = relay.Tuple([call_6821,call_6829,])
output2 = relay.Tuple([call_6822,call_6830,])
func_6831 = relay.Function([], output)
mod['func_6831'] = func_6831
mod = relay.transform.InferType()(mod)
mutated_mod['func_6831'] = func_6831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6831_call = mutated_mod.get_global_var('func_6831')
call_6832 = func_6831_call()
output = call_6832
func_6833 = relay.Function([], output)
mutated_mod['func_6833'] = func_6833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5356_call = mod.get_global_var('func_5356')
func_5357_call = mutated_mod.get_global_var('func_5357')
call_6874 = relay.TupleGetItem(func_5356_call(), 1)
call_6875 = relay.TupleGetItem(func_5357_call(), 1)
output = relay.Tuple([call_6874,])
output2 = relay.Tuple([call_6875,])
func_6883 = relay.Function([], output)
mod['func_6883'] = func_6883
mod = relay.transform.InferType()(mod)
mutated_mod['func_6883'] = func_6883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6883_call = mutated_mod.get_global_var('func_6883')
call_6884 = func_6883_call()
output = call_6884
func_6885 = relay.Function([], output)
mutated_mod['func_6885'] = func_6885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1285_call = mod.get_global_var('func_1285')
func_1287_call = mutated_mod.get_global_var('func_1287')
call_6939 = func_1285_call()
call_6940 = func_1285_call()
var_6961 = relay.var("var_6961", dtype = "float64", shape = (5, 12, 2))#candidate|6961|(5, 12, 2)|var|float64
bop_6962 = relay.maximum(call_6939.astype('uint8'), var_6961.astype('uint8')) # shape=(5, 12, 2)
bop_6965 = relay.maximum(call_6940.astype('uint8'), var_6961.astype('uint8')) # shape=(5, 12, 2)
func_2824_call = mod.get_global_var('func_2824')
func_2827_call = mutated_mod.get_global_var('func_2827')
const_6967 = relay.const([2.707805,-9.635138,-5.968003,-0.778776,5.807879,-8.336617,8.658238,-3.092277,9.601376,-5.714748,-0.099608,-5.382973,6.154559,-7.008817,5.260086,8.431713,3.527678,0.971256,5.691795,-0.103450,5.306935,4.706759,-0.616214,7.611494,-6.651830,-8.583718,2.556390,2.013267,9.634425,9.229686,-6.666723,1.193975,-3.243597,4.186178,5.133166,0.137395,7.573077,4.908628,-2.884764,2.209747,-3.309924,2.666783,-2.786054,8.076545,-7.180287,-5.385590,7.862492,-1.641207,9.208496,4.494670,1.928098,7.759718,-0.252985,-7.521983,6.058077,6.123386,-8.706723,8.776939,-7.917232,-5.686910,2.917288,2.678212,-0.419224,3.989574,8.991464,-3.535866,5.766525,1.434471,-4.472046,-6.720235,1.740297,-5.941561], dtype = "float64")#candidate|6967|(72,)|const|float64
call_6966 = relay.TupleGetItem(func_2824_call(relay.reshape(const_6967.astype('float64'), [72,])), 2)
call_6968 = relay.TupleGetItem(func_2827_call(relay.reshape(const_6967.astype('float64'), [72,])), 2)
output = relay.Tuple([bop_6962,call_6966,const_6967,])
output2 = relay.Tuple([bop_6965,call_6968,const_6967,])
func_6979 = relay.Function([var_6961,], output)
mod['func_6979'] = func_6979
mod = relay.transform.InferType()(mod)
var_6980 = relay.var("var_6980", dtype = "float64", shape = (5, 12, 2))#candidate|6980|(5, 12, 2)|var|float64
output = func_6979(var_6980)
func_6981 = relay.Function([var_6980], output)
mutated_mod['func_6981'] = func_6981
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7005 = relay.var("var_7005", dtype = "float32", shape = (15, 5, 6))#candidate|7005|(15, 5, 6)|var|float32
const_7006 = relay.const([[[-9.444089,-6.679826,7.396100,-5.438527,3.387893,-4.439813],[3.798378,-1.857632,-5.095589,5.041075,-6.857735,6.490898],[-0.667978,0.100840,1.675730,8.205762,8.126425,0.696532],[0.308237,4.459810,1.593470,5.054681,1.622354,3.406979],[3.384977,-8.832850,-3.014657,5.776822,-9.580406,3.032429]],[[6.889999,4.076671,1.850306,2.210579,-3.275639,5.410665],[-6.842854,-4.166424,-7.509907,9.132372,9.438450,9.418823],[9.908021,-3.577800,2.716248,-3.919486,-5.203183,-9.081708],[-8.971435,-5.187998,-7.240126,5.333252,-6.592808,-7.780112],[0.166752,-7.754680,-3.362583,-6.172773,-2.112876,1.450469]],[[7.141529,-8.966057,2.297300,6.960621,-6.887226,-7.051494],[5.372920,1.347241,-2.257007,-2.257041,-0.175225,-8.415976],[-0.509638,-9.331333,2.070804,5.099419,9.934265,-6.915924],[-3.159608,8.868881,8.774537,9.206662,1.242214,-9.682457],[8.911372,2.222772,-9.814281,-3.572521,9.703733,1.373506]],[[-3.178239,0.313856,3.632805,-2.691086,7.154558,-5.385416],[5.932659,6.625953,5.373971,-5.947107,-8.168896,-1.448883],[5.896002,1.592470,9.511439,9.533742,1.301503,-0.068962],[-0.155167,-3.840245,-7.506894,-2.469448,3.892480,-1.126019],[-4.469018,1.172953,-1.542308,4.287266,-3.249068,-3.078779]],[[6.682396,6.206405,-9.764130,9.358626,-6.294187,-1.829122],[0.279904,-6.514501,-9.158183,5.114090,-9.794808,2.702626],[-1.352147,-2.445662,-4.586948,-7.998203,8.803331,-1.225419],[8.217089,-7.344592,-3.599023,-8.246840,-6.206375,-2.127535],[8.076061,3.730490,-6.695790,5.642885,1.809345,9.306205]],[[-0.111093,4.419545,5.679842,-3.153374,-9.821599,-9.219004],[7.928154,-8.741495,3.311586,7.953269,-5.462351,-7.280383],[4.682499,4.528068,-7.155342,-8.460363,-8.971911,-8.457272],[-7.967119,9.040662,4.029654,6.383447,-4.616112,-5.280877],[-6.822591,6.439215,-6.973828,5.849312,4.268528,-6.941593]],[[2.172438,-0.916534,6.977391,7.615723,6.446335,-0.470179],[-0.153140,-2.771371,2.888993,-8.645686,-9.729128,-4.930273],[-8.118755,-2.833491,-1.540155,4.780570,-5.716127,9.660095],[-2.703649,0.114015,7.857067,-5.402080,6.841320,1.509100],[-7.747195,-2.321709,6.155557,5.499263,-4.836314,5.461140]],[[6.929155,-7.610146,-9.953719,2.209472,-1.243889,0.182628],[-8.108552,0.229544,-0.805689,-2.675068,-0.319583,9.487158],[7.627173,2.413478,-3.352519,-1.346994,9.142688,4.942672],[-8.071250,-9.991276,4.108480,9.712511,-0.886784,7.358832],[8.446908,1.928181,-5.205226,9.957697,7.686284,4.902504]],[[6.320346,5.747765,-8.024168,-5.958035,5.070720,2.191940],[-2.565835,-0.086624,8.230483,9.036628,7.550633,8.998484],[9.749390,8.264675,5.565893,5.145904,-4.495612,-7.723633],[1.959792,-2.900188,1.638493,-7.236516,-7.179865,-1.027469],[-8.072118,-3.627464,-3.747670,-9.204663,-4.670012,9.742535]],[[-6.789052,-3.718836,0.352991,-0.601387,7.015325,-9.340252],[-8.970300,6.709877,0.614351,3.964869,6.663658,-0.587339],[6.413234,-1.481608,-6.523263,0.264159,-7.186584,-7.124224],[-2.016726,-8.228996,0.290979,1.699932,1.472250,-5.398725],[-4.324726,7.461490,3.733348,-9.724813,-4.085716,-5.072235]],[[-9.208183,6.370217,2.922493,-1.102161,-5.081312,9.201619],[0.893924,-4.007694,1.169542,-9.656764,-1.332733,-6.176913],[3.448921,-4.751027,3.012517,-4.098488,-5.631579,-4.691267],[1.484373,-8.078147,2.092323,8.620417,-3.596307,-6.626874],[-4.890132,5.799835,-1.799380,-5.313481,-1.745876,5.251469]],[[0.752911,7.463124,1.732985,6.533825,2.399820,2.484695],[-5.881413,2.796483,-0.444597,-9.225714,-7.849926,7.153871],[4.240202,-4.189625,-4.373071,9.612007,-8.225790,1.190696],[-0.068667,-3.510644,-2.676448,1.329049,3.127342,6.043209],[-1.054787,-3.382576,-3.095996,1.080348,-6.154886,6.583808]],[[0.367774,-0.522007,-6.036428,4.239985,6.805775,-6.463216],[0.989890,-6.512491,-5.385249,-9.627394,1.084686,-1.276096],[-1.303303,-2.568569,8.983776,5.861964,-4.640380,-1.959905],[-2.497083,-4.113979,-2.738691,9.176295,-3.749362,-0.459812],[-9.616186,2.346507,9.662257,0.074780,6.708692,-3.418358]],[[6.335325,4.924167,-0.204115,-5.969377,8.396404,-6.647839],[8.460916,-4.274372,8.255895,7.923981,7.375863,8.204856],[-6.362158,0.480471,-9.336521,-8.400932,1.760724,-0.114206],[-5.189162,-8.433291,7.229238,9.185432,4.615496,-9.502776],[-8.257865,-2.996554,-2.160448,-1.880765,-0.626279,-2.908605]],[[-3.065158,-6.041142,-1.160662,0.689896,-2.590985,-6.851781],[-7.502788,-1.291247,5.060926,-0.702360,-4.991859,-4.045987],[-1.814522,3.872458,-9.029744,-4.254608,7.468385,-1.260891],[1.401682,-9.654131,-5.439914,6.290355,-6.234060,-2.471013],[-9.440232,3.759323,5.842623,1.417076,-9.658380,-0.702955]]], dtype = "float32")#candidate|7006|(15, 5, 6)|const|float32
bop_7007 = relay.floor_divide(var_7005.astype('float32'), relay.reshape(const_7006.astype('float32'), relay.shape_of(var_7005))) # shape=(15, 5, 6)
func_4336_call = mod.get_global_var('func_4336')
func_4338_call = mutated_mod.get_global_var('func_4338')
call_7023 = relay.TupleGetItem(func_4336_call(), 0)
call_7024 = relay.TupleGetItem(func_4338_call(), 0)
const_7027 = relay.const([[[5.040160,2.546301,6.021390,-8.976593,-3.032854,-8.870361],[-9.890057,9.412987,2.815460,4.929248,-9.877945,5.870007],[-0.306002,-6.290649,8.705426,0.332308,0.074859,9.318306],[-0.443209,-3.466368,3.003039,-9.197787,-1.656775,-2.069636],[0.208982,-7.669237,4.766946,5.574625,-5.244068,-4.233261]],[[9.208574,6.218894,-8.527647,9.965282,-9.444080,-9.723289],[2.890431,-0.908788,-6.580293,1.109529,-4.369375,4.157663],[5.248326,3.032388,9.606755,-5.114897,-8.003120,2.104609],[-6.327882,2.851381,-3.907135,5.908466,-0.783782,9.932671],[-2.809906,1.766264,-3.184210,-5.511595,5.988499,-3.023675]],[[0.185646,4.684008,-4.474030,7.701325,-4.222969,8.055237],[-0.051235,-6.709097,-3.651034,0.870831,-3.350691,3.738612],[2.666534,-8.170475,-1.547267,7.301701,3.993848,5.771690],[1.275114,0.706659,0.617414,-1.050416,9.546575,3.679340],[3.351157,-2.212858,9.505814,-3.693342,-8.723242,2.537763]],[[0.111772,-6.853588,8.984197,-2.004998,-1.745438,-2.877327],[5.655575,7.713970,2.238665,-5.071975,4.138467,-0.322650],[9.769242,-0.628888,-3.346657,-1.443244,-4.918952,-6.218989],[-4.184341,5.097479,-3.674014,-4.148025,-4.764366,-8.151259],[-2.221351,-5.336657,-5.797865,-5.586348,-8.466563,5.023592]],[[-6.238283,-9.465055,-1.367985,9.596836,-5.326430,-2.575380],[-1.206074,-0.636528,-4.030866,4.915939,3.577725,8.645329],[-6.660290,9.694023,-7.509023,2.787440,-0.741315,4.118540],[9.441547,5.635797,2.909100,-2.627886,0.643680,0.279612],[-8.302541,-3.676337,-2.015462,0.303150,-1.606587,7.118898]],[[6.384830,4.972694,8.422440,-6.694661,6.779247,-0.586926],[6.797151,3.037659,3.809011,3.864274,9.427568,2.100027],[4.292979,-3.097302,-7.516581,-7.912986,3.476543,6.497979],[-1.206704,1.326218,-1.265415,8.802614,-8.307562,-7.465006],[9.122577,9.337563,5.352350,-6.672449,8.464226,-0.169308]],[[3.929507,8.648537,3.843643,3.176453,0.771194,8.692226],[-5.628117,9.181135,1.200474,-8.878421,7.768326,9.707183],[-6.138919,9.563386,2.986704,7.046179,-5.982547,4.088037],[-9.376872,-0.592193,8.680494,7.465724,-6.666012,-4.847595],[-3.224590,-7.158412,9.734315,-7.281818,2.311615,6.149975]],[[-0.408268,1.841205,-8.463917,-0.759950,8.247061,-7.935886],[-0.950772,-7.750443,-4.881936,6.681358,1.213363,4.574559],[5.962251,0.860461,2.093122,7.478671,1.740707,4.913506],[1.813192,-8.469600,-7.146773,7.549124,-5.000265,5.823557],[3.412847,9.023473,-2.384967,2.334117,7.123348,-8.686402]],[[4.759910,-7.187965,8.612091,-7.494334,1.901348,6.062587],[3.017834,-3.175493,6.807991,5.464584,-1.857676,8.398439],[9.270791,2.972300,4.839968,1.572798,6.936859,-8.314897],[0.886782,-8.201475,5.390816,-1.659429,-0.327324,7.914101],[-6.238765,-8.322829,1.283465,8.778092,-6.081552,6.807785]],[[7.045787,1.621117,-1.080414,9.690862,-2.322355,-1.543941],[0.336930,1.709039,-4.338761,3.780141,0.269485,3.275827],[-3.107837,0.854956,0.228878,-3.017703,3.387172,-0.797472],[8.928721,-3.380818,9.697746,-2.835629,1.209171,-4.385564],[-1.078341,3.455032,-6.878697,-7.381320,5.746624,1.812295]],[[2.847539,0.835850,5.440522,-4.253643,9.563105,6.850287],[-7.813057,-4.208645,2.903695,4.202348,-1.248641,3.232735],[8.885026,2.973921,8.435352,-9.973511,7.778450,5.216563],[4.527499,8.534743,-3.033218,8.248376,-5.755536,1.024574],[-1.955445,1.801367,4.831182,0.148536,2.859738,3.123530]],[[-5.718005,2.923151,-5.784746,-3.802216,-8.999333,-3.597061],[-1.117874,1.899876,0.130724,-3.880307,6.099718,1.096632],[-3.750003,-9.633854,3.860630,-5.713189,5.446103,1.165488],[7.211691,6.944271,-6.609229,-9.595934,8.553274,9.683344],[-5.235110,-1.094181,-4.699429,-4.896759,9.468601,-0.034199]],[[6.635110,-8.967692,-4.731005,-0.570526,9.434230,4.769021],[2.650383,2.937744,-3.082778,-2.010399,-8.699582,-3.864032],[-0.111823,-9.962836,2.202666,-8.609900,3.583111,4.583436],[2.524908,6.300163,3.014284,-5.673040,8.306381,9.923125],[-7.037350,-1.154636,9.472285,1.658273,-6.455608,7.130784]],[[-4.451837,-4.268286,-7.923827,5.572816,4.077087,-0.749802],[-1.024082,8.107994,-8.247588,8.480808,-8.397161,-1.195353],[-5.609190,5.264788,0.038813,0.708205,7.199552,3.170417],[6.486506,2.139840,-6.669683,-1.804933,-5.778815,-5.222574],[-0.371003,8.406073,9.378884,-4.886576,-2.429023,-2.332241]],[[-4.128557,3.789842,0.143986,2.275423,-1.408841,3.484135],[5.611751,9.402896,-4.311345,-5.893392,1.147824,2.297545],[4.800959,-6.622118,-1.940982,6.513564,-0.809290,-6.602546],[-3.122656,9.002043,-2.732718,7.887221,-0.968265,2.926286],[-5.323136,3.994702,4.341030,-2.635100,5.185859,-0.693104]]], dtype = "float32")#candidate|7027|(15, 5, 6)|const|float32
bop_7028 = relay.maximum(bop_7007.astype('int8'), relay.reshape(const_7027.astype('int8'), relay.shape_of(bop_7007))) # shape=(15, 5, 6)
const_7057 = relay.const([[[6.710863,1.082051,-5.790913,-8.340618,-2.378847,5.464765],[9.463401,-2.482171,-1.949781,-7.778935,3.744185,-0.729748],[-7.829389,-4.874234,-3.091827,-9.172247,-2.054275,-8.375348],[-7.689121,3.299601,7.629007,6.520833,-0.942246,2.362856],[-9.359734,4.325014,-2.590730,-8.265824,7.265711,4.319027]],[[-6.844298,3.842854,-4.468614,8.936413,9.960082,6.422799],[-6.088885,8.551493,6.011762,1.310480,-6.506200,8.006238],[6.657668,3.130945,-3.708264,-9.560817,-0.211195,7.938360],[4.192461,4.491204,3.478928,3.343301,-4.391347,8.520074],[0.584646,0.552865,7.361470,-2.922606,-2.826699,8.764351]],[[0.356560,3.011022,-6.302348,-6.899647,-6.875039,-9.731212],[-3.965911,0.870225,-9.679270,-7.413994,6.636297,8.483900],[-8.851339,1.855171,9.253399,8.764549,-3.600646,-4.289629],[6.996271,-0.279689,7.155773,-7.953736,-3.739959,-1.085182],[-3.794920,-0.325690,-0.290403,-1.737360,-8.840536,-9.866394]],[[-0.723994,-0.924656,-4.372755,8.760785,3.870282,6.086422],[-8.833416,-4.759524,0.471056,9.012507,-3.450606,-8.477109],[8.541848,5.108627,-6.062179,0.555596,-6.500739,-8.076247],[5.666555,-3.905553,8.423490,4.504444,4.537566,3.567744],[-0.233567,-6.890338,-2.260664,5.685943,7.064190,8.164013]],[[-0.931992,0.068388,-7.769285,-6.069745,5.965313,-2.327494],[-5.986711,1.445682,-3.042475,3.115418,2.358462,5.594045],[-3.509046,-2.443728,1.554131,5.242107,-0.518702,-6.945280],[-7.660300,-9.854086,-6.402350,3.115124,-0.944256,-1.852225],[6.918069,9.232915,-5.663579,-2.774928,-7.526883,-8.671647]],[[1.942367,1.377308,-9.249215,-9.851049,-4.666250,6.063837],[-2.252896,-1.935378,9.005789,8.440840,-3.389119,3.160445],[4.544803,1.207227,-1.297764,3.766710,1.463382,-0.133090],[6.433921,9.899968,8.797026,-1.041655,4.516302,1.933350],[0.788529,5.914752,0.986323,-7.175589,-3.868285,-0.300308]],[[-1.788400,-6.970018,9.089570,1.057920,-5.037440,-4.981278],[1.216254,1.807270,2.510855,1.014670,6.978301,-9.358894],[-0.307787,8.671406,-0.675832,2.982945,9.790704,7.935533],[-3.258132,5.995691,9.444579,3.519021,-9.205507,9.632844],[1.230426,0.710780,8.174401,6.969083,-8.374691,-7.279293]],[[1.435913,3.399949,-3.653100,5.073178,-5.065162,2.766044],[-3.843957,-2.413196,9.187940,5.968984,3.779512,9.847805],[-3.124665,-8.673336,1.263026,-9.560794,-9.594929,5.822590],[-5.029445,-0.291390,-2.760298,-3.539140,-0.305053,5.789823],[-8.993119,-2.889605,5.840302,-1.406894,-1.095475,2.034028]],[[6.284469,-8.737097,3.404090,-9.557859,-3.275278,-1.163218],[-6.531704,-8.329436,-8.181017,-6.514981,-4.081503,-6.228303],[-3.485263,2.680873,4.182572,-3.860576,-4.160176,-2.708013],[1.045216,4.578098,4.943826,-1.048113,-1.702836,-1.790111],[-6.036529,8.957030,6.595268,0.886340,-6.837532,0.500745]],[[2.667886,7.116585,-0.104741,3.006262,-0.649038,-3.057426],[4.525949,-3.974934,4.314731,-1.725631,2.472072,-1.923145],[2.663611,6.415145,-9.657342,8.898939,-7.109577,-6.846555],[-5.115695,-6.502828,-6.807156,9.597187,1.407466,-0.156971],[-7.457427,3.338132,-0.334831,6.502811,5.395674,-3.193117]],[[0.154396,1.732437,-4.297208,-9.987058,1.755051,2.838045],[3.156412,8.754373,-3.421613,1.600803,-3.494685,6.931771],[-7.184593,-6.105564,4.465456,-8.782104,-8.922329,-7.510140],[8.711424,-2.964632,-4.017680,-2.525276,-6.203838,-4.808808],[6.550815,9.620542,-8.143283,9.557840,5.687108,-4.607960]],[[-0.232961,0.834967,-6.916884,0.136301,1.584666,3.981023],[4.937413,8.143085,4.560704,0.018864,-3.100383,2.969395],[9.273784,7.100788,-0.877858,7.960368,-4.932312,-0.260668],[-1.969095,-0.259170,2.060177,3.511635,-1.813143,-6.889721],[6.106847,-0.086305,-6.053383,-1.224584,-9.222394,6.660580]],[[-1.273727,6.391349,0.012025,2.962387,8.851895,1.811772],[8.405814,-8.372462,-5.178570,-0.884507,-1.143290,1.223257],[-2.898076,-1.228301,7.203503,2.443229,-7.710133,5.845680],[-0.173405,2.990506,-9.212167,-8.316363,-6.101360,0.669005],[7.905706,-4.095316,7.626360,4.420527,6.729658,-6.140851]],[[5.568059,-5.518175,0.607548,6.443377,1.195345,1.778927],[-7.404915,6.217413,-2.154017,7.739823,-5.295283,3.011310],[9.636584,7.368405,-9.945550,3.179486,-6.635898,6.863756],[5.407887,0.855665,-1.277753,8.977415,1.362485,0.786335],[3.979529,5.106956,-6.908431,7.966106,8.569266,-8.585659]],[[7.272620,7.959581,-6.848543,0.269950,-8.242740,-1.874723],[4.361876,6.125406,-4.812393,7.072582,8.920433,-3.477598],[4.754303,0.798968,-8.412915,9.213722,4.853594,3.503938],[3.784960,-8.399163,-2.261657,-4.929260,-1.324736,-6.860197],[-9.838011,-3.003804,-5.086532,4.499905,1.860600,4.847662]]], dtype = "float32")#candidate|7057|(15, 5, 6)|const|float32
bop_7058 = relay.logical_and(const_7027.astype('bool'), relay.reshape(const_7057.astype('bool'), relay.shape_of(const_7027))) # shape=(15, 5, 6)
bop_7073 = relay.less(const_7027.astype('bool'), relay.reshape(const_7006.astype('bool'), relay.shape_of(const_7027))) # shape=(15, 5, 6)
output = relay.Tuple([call_7023,bop_7028,bop_7058,bop_7073,])
output2 = relay.Tuple([call_7024,bop_7028,bop_7058,bop_7073,])
func_7082 = relay.Function([var_7005,], output)
mod['func_7082'] = func_7082
mod = relay.transform.InferType()(mod)
mutated_mod['func_7082'] = func_7082
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7083 = relay.var("var_7083", dtype = "float32", shape = (15, 5, 6))#candidate|7083|(15, 5, 6)|var|float32
func_7082_call = mutated_mod.get_global_var('func_7082')
call_7084 = func_7082_call(var_7083)
output = call_7084
func_7085 = relay.Function([var_7083], output)
mutated_mod['func_7085'] = func_7085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5106_call = mod.get_global_var('func_5106')
func_5108_call = mutated_mod.get_global_var('func_5108')
call_7094 = relay.TupleGetItem(func_5106_call(), 0)
call_7095 = relay.TupleGetItem(func_5108_call(), 0)
var_7099 = relay.var("var_7099", dtype = "float64", shape = (16, 12, 2))#candidate|7099|(16, 12, 2)|var|float64
bop_7100 = relay.multiply(call_7094.astype('int16'), var_7099.astype('int16')) # shape=(16, 12, 2)
bop_7103 = relay.multiply(call_7095.astype('int16'), var_7099.astype('int16')) # shape=(16, 12, 2)
func_1127_call = mod.get_global_var('func_1127')
func_1129_call = mutated_mod.get_global_var('func_1129')
call_7109 = relay.TupleGetItem(func_1127_call(), 0)
call_7110 = relay.TupleGetItem(func_1129_call(), 0)
output = relay.Tuple([bop_7100,call_7109,])
output2 = relay.Tuple([bop_7103,call_7110,])
func_7114 = relay.Function([var_7099,], output)
mod['func_7114'] = func_7114
mod = relay.transform.InferType()(mod)
var_7115 = relay.var("var_7115", dtype = "float64", shape = (16, 12, 2))#candidate|7115|(16, 12, 2)|var|float64
output = func_7114(var_7115)
func_7116 = relay.Function([var_7115], output)
mutated_mod['func_7116'] = func_7116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5468_call = mod.get_global_var('func_5468')
func_5470_call = mutated_mod.get_global_var('func_5470')
call_7121 = func_5468_call()
call_7122 = func_5468_call()
output = relay.Tuple([call_7121,])
output2 = relay.Tuple([call_7122,])
func_7123 = relay.Function([], output)
mod['func_7123'] = func_7123
mod = relay.transform.InferType()(mod)
mutated_mod['func_7123'] = func_7123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7123_call = mutated_mod.get_global_var('func_7123')
call_7124 = func_7123_call()
output = call_7124
func_7125 = relay.Function([], output)
mutated_mod['func_7125'] = func_7125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1592_call = mod.get_global_var('func_1592')
func_1594_call = mutated_mod.get_global_var('func_1594')
call_7157 = relay.TupleGetItem(func_1592_call(), 0)
call_7158 = relay.TupleGetItem(func_1594_call(), 0)
output = call_7157
output2 = call_7158
func_7174 = relay.Function([], output)
mod['func_7174'] = func_7174
mod = relay.transform.InferType()(mod)
mutated_mod['func_7174'] = func_7174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7174_call = mutated_mod.get_global_var('func_7174')
call_7175 = func_7174_call()
output = call_7175
func_7176 = relay.Function([], output)
mutated_mod['func_7176'] = func_7176
mutated_mod = relay.transform.InferType()(mutated_mod)
func_958_call = mod.get_global_var('func_958')
func_960_call = mutated_mod.get_global_var('func_960')
call_7187 = relay.TupleGetItem(func_958_call(), 0)
call_7188 = relay.TupleGetItem(func_960_call(), 0)
func_4904_call = mod.get_global_var('func_4904')
func_4905_call = mutated_mod.get_global_var('func_4905')
call_7231 = relay.TupleGetItem(func_4904_call(), 4)
call_7232 = relay.TupleGetItem(func_4905_call(), 4)
func_585_call = mod.get_global_var('func_585')
func_586_call = mutated_mod.get_global_var('func_586')
call_7237 = relay.TupleGetItem(func_585_call(), 0)
call_7238 = relay.TupleGetItem(func_586_call(), 0)
output = relay.Tuple([call_7187,call_7231,call_7237,])
output2 = relay.Tuple([call_7188,call_7232,call_7238,])
func_7243 = relay.Function([], output)
mod['func_7243'] = func_7243
mod = relay.transform.InferType()(mod)
output = func_7243()
func_7244 = relay.Function([], output)
mutated_mod['func_7244'] = func_7244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5468_call = mod.get_global_var('func_5468')
func_5470_call = mutated_mod.get_global_var('func_5470')
call_7245 = func_5468_call()
call_7246 = func_5468_call()
output = call_7245
output2 = call_7246
func_7263 = relay.Function([], output)
mod['func_7263'] = func_7263
mod = relay.transform.InferType()(mod)
mutated_mod['func_7263'] = func_7263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7263_call = mutated_mod.get_global_var('func_7263')
call_7264 = func_7263_call()
output = call_7264
func_7265 = relay.Function([], output)
mutated_mod['func_7265'] = func_7265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4804_call = mod.get_global_var('func_4804')
func_4805_call = mutated_mod.get_global_var('func_4805')
call_7278 = func_4804_call()
call_7279 = func_4804_call()
output = call_7278
output2 = call_7279
func_7292 = relay.Function([], output)
mod['func_7292'] = func_7292
mod = relay.transform.InferType()(mod)
mutated_mod['func_7292'] = func_7292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7292_call = mutated_mod.get_global_var('func_7292')
call_7293 = func_7292_call()
output = call_7293
func_7294 = relay.Function([], output)
mutated_mod['func_7294'] = func_7294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7292_call = mod.get_global_var('func_7292')
func_7294_call = mutated_mod.get_global_var('func_7294')
call_7384 = func_7292_call()
call_7385 = func_7292_call()
func_5711_call = mod.get_global_var('func_5711')
func_5714_call = mutated_mod.get_global_var('func_5714')
const_7396 = relay.const([-6.456660,9.758838,9.816847,-3.655417,-2.710511,4.571112,-3.707993,-4.108860,-8.868575,9.769368,-3.697127,-4.343926,-1.433468,7.073172,2.395374,1.919533,-7.968914,-1.285616,-5.922395,-3.243603,7.687235,-5.060097,-7.029191,-3.110311,-9.778664,-4.741786,-3.448277,1.324784,-1.309528,-0.375618,-5.589707,6.470927,-4.747485,2.889446,-2.632627,-6.569208,1.699162,7.240802,2.314966,-1.452126,4.820973,4.256474,-5.461734,-2.098195,0.852362,-6.503173,-1.467095,-0.563309,0.410935,2.164929,-5.942651,-8.954490,-4.309613,0.178467,0.857547,-2.177726,-6.904102,-7.076151,-0.857450,8.281842,-5.991972,3.657405,-7.807107,3.124095,4.745231,5.214705,-3.847066,-6.017466,-1.034203,0.515297,6.967457,-8.139823,2.682360,-4.091276,-3.265954,9.711419,-2.942377,4.381534,5.172261,-3.731673,-1.404915,-2.546369,7.401328,4.192548,-8.142974,7.157362,-0.609451,-9.305920,8.605006,2.208313,-4.804351,-2.255954,-5.261640,2.619799,-2.561776,-7.928971,-5.941247,-9.498148,5.646128,6.159082,-0.846013,-6.121530,-0.711922,-4.921393,1.449218,4.811289,-2.075500,-2.148303,-2.304881,-7.079730,-7.699833,0.308843,2.857717,-9.920799,3.295539,3.965408,5.779966,6.368167,-1.860206,4.902918,6.820154,6.432155,-2.699359,-5.082835,-0.005067,0.715907,-6.409632,6.280450,-0.485488,-5.667539,7.307363,0.438004,4.707972,-5.866139,-2.465309,-3.424431,7.264332,-9.572755,6.253781,-8.673248,8.235620,-6.632461,-9.190774,-3.759417,-7.276029,-5.723369,-6.815871,-5.982882,-3.027518,9.195842,-4.338117,6.808979,8.865196,8.566128,-3.861767,-2.976338,2.703918,6.142699,-7.208960,8.316973,8.509469,-5.199353,6.480545,0.543009,-5.183843,9.872556,-6.504173,-7.881029,-3.340444,6.944039,6.344888,-1.565841,-1.143076,-4.808379,0.077332,4.017236,3.752936,-6.348438,-6.144962,9.529563,-2.710416,6.532085,8.041336,1.333782,7.816461,-3.729545,-3.364778,-4.652051,0.390442,-3.788976,-1.937403,3.340265,7.021600,-5.447988,2.908361,-2.265834,-9.451840,8.691730,9.216670,5.129498,5.435889,4.105945,8.249377,-2.793925,-6.900960,9.294796,2.349902,2.363101,7.336410,-7.939077,6.444834,-4.342434,8.225319,0.253851,-8.740570,4.553296,-1.253190,-2.018739,-1.550919,-1.525977,6.524646,9.272977,-1.140915,6.490356,0.703023,0.450134,5.237433,-0.080979,3.439473,3.084990,3.465115,1.029999,-7.670658,4.947322,-2.074439,4.681358,4.616432,-1.395861,8.982138,5.197849,-9.525692,3.023702,8.843757,-8.991295,2.053306,-1.809269,-2.059128,1.968619,4.002279,-0.575997,-2.104150,9.828521,-3.416931,-2.616067,-2.094837,-7.767939,-1.115613,-9.480055,-0.855173,-2.108558,-9.776767,-0.004947,-8.362766,1.335846,-2.314057,4.256898,-1.836894,-0.131207,4.906560,-8.505958,7.010567,-0.573565,5.264266,5.219961,9.917134,2.223238,-4.065493,-5.269435,3.046560,9.250293,2.767652,1.347365,5.781366,0.125284,-0.154769,-6.806457,-1.500894,8.882310,4.490624,2.842717,-1.318938,9.425136,-1.765484,7.809395,0.343034,9.099513,9.229248,-9.912138,8.811439,5.037579,-4.580309,4.002503,-6.390891,-3.230221,7.075933,-9.731675,-7.251757,-5.691890,-4.969684,9.899707,-7.598581,-9.651850,3.528534,5.284895,-4.506143,-0.958789,-6.629352,-1.916566,-5.710050,1.542338,-2.335803,7.211915,2.028595,-2.237525,4.404896,2.135810,-4.236111,4.046489,9.796722,-4.074158,-3.445814,-0.611219,-7.946593,3.107223,6.435813,-5.620795,3.419850,-3.979599,-7.341652,-5.565611,-5.700257,3.937388,9.514967,-3.395297,4.186299,2.310500,7.102129,6.899553,-4.479745,-4.792002,0.924954,5.810320,-6.157133,3.980361,-8.177012,-6.803978,1.065432,-1.729752,8.658878,8.145991,0.076440,-9.140271,-3.579302,9.744898,-7.141994,-0.779360,-3.746618,-9.180914,-8.353213,6.235891,9.526348,3.373981,-1.727690,-6.481939,6.765693,-0.862317,-6.923749,9.487139,-9.380556,1.362358,3.310380,-5.184362,2.499426,-1.230236,-0.752381,2.503805,-1.875097,6.305493,-7.767713,-2.320210,4.199116,-7.145911,7.733366,6.915237,-0.127253,-5.070889,-8.106656,-7.099722,-0.752441,7.877340,-3.770901,-3.646879,-3.431439,6.081434,0.829512,-3.545412,8.229093,-8.708042,-4.404536,-5.060048,-3.008380,-8.499316,-3.243794,0.590064,-2.990981,8.705004,7.540099,5.486487,8.158845,-9.533329,-8.344175,-4.764281,1.969281,-8.466288,-6.253213,5.536722,2.400814,2.871151,-4.733122,-8.804926,-3.991119,4.835837,-9.237874,8.765672,-8.513116,-2.600972,-5.128058,-6.900008,-2.184818,2.735254,2.237289,4.479451,5.246968,-8.330730,3.298591,-1.524765,7.288114,8.081494,-0.776937,1.044161,-5.323176,4.329959,-0.854741,4.565603,-3.192109,7.994874,5.330225,-7.399921,-3.188696,-9.886310,-0.338336,7.960356,-1.703756,0.683572,1.993337,8.521413,-7.058836,-2.641934,-5.906116,3.062723,-2.684204,7.922029,-0.760987,-6.891453,-4.893396,-6.717196,7.978551,-3.904176,3.951428,-0.518826,8.675716,-5.861071,-0.923850,-9.415139,-8.587201,1.819021,6.062099,-2.842287,1.847108,-9.697291,3.691466,-1.687098,-8.029453,0.797245,-7.862869,-2.826210,0.114326,5.033214,0.292927,7.965078,-9.142730,-8.799858,2.819122,2.923600,-3.818981,-0.931849,-1.944396,-6.291985,-4.426903,-8.089673,-6.521609,-9.817303,-5.575676,9.436493,0.225422,5.907335,-0.705946,6.574700,1.240799,-0.050566,-4.087506,9.634620,9.687778,8.803843,3.566327,-4.341046,-5.784177,-0.731927,-0.629252,-6.940995,-6.837052,7.176365,-6.113981,-5.340637,9.638809,4.432476,7.295348,9.234717,-8.111701,-1.742831,-0.452124,3.929937,8.948637,2.318874,-4.307816,-7.347975,-1.547385,8.208682,-5.588191,-7.323507,-2.231051,-8.360777,-1.439084,-8.852212,-0.833492,8.219620,2.550450,-0.657821,-4.588156,-8.453740,7.754630,3.122483,0.022371,-6.612369,-8.524398,6.109269,-8.772486,-8.456156,3.315725,-3.703917,-5.683581,8.485614,-9.420117,-8.000227,8.407578,0.018472,8.294035,-8.960898,1.667180,5.074390,8.269018,-6.633878,-6.387695,0.294780,4.567053,3.181698,2.029814,0.952671,-4.829269,-7.334683,5.019837,2.756142,-5.973746,3.151108,-4.572172,9.287634,5.132052,-9.500581,-3.010471,-2.877494,4.076746,5.968579,-4.052743,-9.412580,7.821007,-8.777399,3.324740,7.909112,-1.258140,5.108250,3.852624,-2.932138,7.467595,-8.541589,-9.126517,3.501503,1.905888,-0.498139,-9.421715,-8.729005,9.938949,-5.748412,-1.506105,-9.275495,-2.850310,-0.009182,-5.310068,-2.973527,4.564880,-3.606575,9.929492,5.553934,-7.703788,-9.763863,-9.643971,-9.735167,-6.375744,-2.106867,6.897779,4.646936,9.252055,0.182173,-0.763351,8.831004,8.265627,-8.060322,8.667442,7.867447,9.268360,-3.811828,-5.146644,-2.548604,7.304831,-2.923607,8.308592,-4.459997,0.058674,1.544322,-2.255367,0.267860,-0.133664,-5.579948,6.119174,0.875444,-7.079826,-8.587391,6.113738,8.024614,-6.128838,6.596078,4.713962,-1.024311,5.239677,-9.444554,-6.397534,1.150844,1.813193,-2.987335,6.067683,-4.263724,-1.388324,2.957838,7.298896,-1.432479,-2.752455,1.442358,-9.759806,-9.924166,1.423304,1.616312,-4.283151,-6.367654,-4.111325,-7.857557,9.672628,4.734533,9.666083,4.371647,2.451537,-4.881467,3.774510,6.616371,3.404891,4.676575,4.978645,-6.507208,-0.872263,8.704552,-5.186585,-9.969042,-1.557288,9.926949,-9.381120,-0.410942,-5.529133,4.328233,5.444988,4.105729,-7.503805,9.498350,7.894680,0.656091,9.755400,2.729151,-9.719123,9.611618,0.844971,9.536154,3.755905,-3.185346,-1.839988,2.388794,-6.971946,9.989196,6.015962,-5.414485,-0.842501,-7.289109,4.983370,9.978486,-8.127807,-9.875493,5.761245,8.986179,-7.791678,5.181268,-8.231390,-5.127739,7.134290,1.783344,-8.692759,-9.996691,-9.411701,-9.612558,-9.787160,5.581625,-8.622803,-5.028432,0.412017,-4.460003,9.403282,7.465634,-1.537195,5.086611,6.365222,9.701052,-9.632184,-7.507210,-0.379678,-4.199134,6.957731,4.427468,-9.306872,1.807348,-6.159143,1.997609,0.889465,0.569929,-5.882670,-3.665148,2.430784,1.484153,4.187327,-9.162083,0.206999,-1.714150,9.925230,-5.603880,4.205726,7.576259,-9.338648,-2.837576,6.555684,3.303035,-5.022611,0.618494,3.823363,0.410551,9.151716,9.372558,6.004889,3.009318,8.606735,-7.757746,0.746136,-3.854802,-2.133309,-1.021680,-0.416198,5.144841,3.841748,4.322485,6.573595,6.626331,-8.595205,6.240305,-0.099807,-4.763668,7.889351,-6.853777,0.660954,-4.605372,0.627514,0.017972,-0.293004,-4.725061,-9.758630,0.249411,6.311006,-6.677904,3.035864,3.644035,-2.900510,7.020490,-7.021404,-2.381113,7.810718,7.175252,3.822929,-8.827062,9.815847,3.730530,-1.491308,3.768210,3.253768,-6.928160,-6.237115,-4.636875,7.553928,-4.917450,-0.722840,6.629930,2.351136,-7.194873,-6.545647,-1.149597,-0.353593,0.725117,-8.047325,-8.333454,-0.073019,-4.509090,-8.802465,0.374696,8.232003,7.224856,-2.499068,1.675900,4.748027,1.499492,-3.090353,8.252484,5.763252,-3.195300,1.085683,-3.722859,6.487947,-2.794092,8.594652,9.248909,7.368810,-0.293525,-7.082606,4.031363,-6.851521,6.756584,2.900317,7.092759,6.134088,-7.524726,-2.278046,-0.785522,-0.044043,4.242057,-5.497155,-7.913723,3.454123,0.348213,-4.625172,6.725645,0.487320,8.972857,1.966485,-0.007647,-4.469221,2.571917,1.081657,-3.672896,2.101097,7.828062,2.172463,8.217575,3.898676,-6.434160,-8.895822,-9.548654,-7.477090,-9.475182,-7.668370,-5.711287,6.210418,9.274638,7.526473,-7.469281,4.440272,-6.639794,2.797394,7.364510,-5.906976,-6.137912,4.345358,1.198563,6.791701,2.877969,-9.833506,-6.025888,4.444684,-1.618088,-0.215604,8.289843,-4.019898,-0.623432,-6.199235,-9.271910,9.282237,9.381613,3.579003,-8.426009,-0.921600,-8.224667,7.457242,-7.012825,-0.881705,0.790108,-0.967104,-4.302160,-9.317747,-8.335016,-8.027372,3.075680,-4.425526,-5.099442,3.990479,-3.412387,-4.889719,-8.329106,6.953249,0.657406,5.720277,-1.994503,6.297093,9.838310,9.106517,-4.082052,-9.237414,0.246646,-8.963015,1.327160,-5.569395,0.776597,-8.028490,-8.531217,4.179415,-5.103888,-8.424940,-4.784806,0.814037,9.304068,0.516596,4.306375], dtype = "float64")#candidate|7396|(990,)|const|float64
call_7395 = relay.TupleGetItem(func_5711_call(relay.reshape(const_7396.astype('float64'), [10, 9, 11])), 0)
call_7397 = relay.TupleGetItem(func_5714_call(relay.reshape(const_7396.astype('float64'), [10, 9, 11])), 0)
output = relay.Tuple([call_7384,call_7395,const_7396,])
output2 = relay.Tuple([call_7385,call_7397,const_7396,])
func_7405 = relay.Function([], output)
mod['func_7405'] = func_7405
mod = relay.transform.InferType()(mod)
mutated_mod['func_7405'] = func_7405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7405_call = mutated_mod.get_global_var('func_7405')
call_7406 = func_7405_call()
output = call_7406
func_7407 = relay.Function([], output)
mutated_mod['func_7407'] = func_7407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7243_call = mod.get_global_var('func_7243')
func_7244_call = mutated_mod.get_global_var('func_7244')
call_7507 = relay.TupleGetItem(func_7243_call(), 1)
call_7508 = relay.TupleGetItem(func_7244_call(), 1)
const_7535 = relay.const([[-5.806282,8.540466,-0.641425],[-9.477059,-8.368848,-2.884473],[7.319037,8.532150,0.611517],[1.876802,-9.790433,9.207756],[2.226379,9.903409,-5.164343],[7.627084,-2.919878,8.219646],[-2.144521,5.994869,-5.661057],[-8.901226,5.950825,2.362613],[9.007789,-5.752851,-4.220942],[-1.459080,-7.689791,-7.020654],[-3.427486,1.068121,-3.735786],[-2.215407,-9.661794,8.808810],[2.630195,-0.643049,7.588390],[-9.636472,-1.155780,-4.660863],[-1.691674,-6.046494,-7.254327],[4.844507,-9.525432,-9.879799],[6.819122,0.342583,-4.365753],[-0.066465,8.306565,-5.278401],[-5.086047,3.635164,7.297691],[2.981788,3.412678,-4.990230],[-1.468759,-6.486059,-4.920703],[4.443455,8.206778,9.254124],[9.357223,-2.069223,-0.838437],[6.150168,9.789653,0.100288],[0.380903,-1.434270,-1.369279],[-6.738811,-8.491580,-2.945589],[4.015873,-0.030928,-9.165967],[6.057341,9.644027,-6.046254],[-8.320056,-6.427846,7.027867],[9.508810,-3.561768,0.162795],[-5.297731,5.360140,-1.802018],[-7.802766,1.761294,5.408766],[-6.794351,3.442535,-3.981040],[-9.228640,9.709319,-5.498952],[-8.443535,5.731537,4.690443],[-3.310803,6.816475,-4.345998],[3.513845,5.395114,6.072682],[-8.396152,6.111222,5.388091],[-7.879013,9.754808,-2.793649],[-4.822136,9.072207,4.201065],[-4.119036,-9.961240,2.582843],[9.758460,1.128522,1.640116],[0.260800,8.164099,1.358452],[-0.785816,-6.941786,8.289150],[9.241801,0.026805,-6.605855],[7.819613,-0.193274,-1.817885],[-3.803655,-4.588220,-6.102410],[-8.360621,-5.812495,3.581345],[-5.988656,1.751449,1.084690],[4.189144,-9.797524,5.824156],[7.598025,5.969352,-5.711773],[0.402139,6.288340,0.349409],[4.837695,-4.506934,5.089182],[3.279039,6.693256,-1.934240],[-7.538399,-5.890161,-7.639376],[0.904735,-9.301107,-5.850697],[-3.438922,-4.485728,6.397701],[3.108959,7.100355,-4.935779],[0.697161,0.656893,-6.692329],[9.847482,5.745746,6.579172],[8.110484,-3.669580,8.875063],[8.343355,-4.960039,-2.457221],[2.565984,0.628407,5.183918],[4.333846,3.998356,7.061083],[-4.189351,-3.090648,-5.962979],[6.680262,-7.062591,-2.705304],[-9.319501,8.716063,8.592954],[4.915057,-3.577016,7.760301],[-8.111775,-8.548248,4.113854],[-7.438938,5.298886,-5.906101],[-4.878958,3.424954,8.846636],[0.988342,2.873365,-4.902956],[-3.579531,9.619344,-1.804120],[-3.923173,7.242548,6.265175],[-4.866509,-3.697982,-1.971272],[-3.718213,2.793429,-9.707232],[5.548086,-4.684708,-7.325436],[1.242084,-5.117128,0.780683],[8.448977,-6.880958,1.763863],[-7.443682,2.709813,4.618905],[5.545563,-5.228904,2.095373],[0.497162,-3.393975,-8.231949],[-1.293283,5.982086,-0.637913],[-1.273448,-5.762249,9.967560],[-6.917988,-6.572582,-9.478944],[1.096752,0.288115,-7.718505],[-4.729047,3.404408,-6.591308],[-2.599892,6.287005,9.276442],[-1.260194,2.331916,-1.968656],[-1.333450,-8.562858,-2.535652],[-1.833774,-2.874781,-1.161557],[9.780272,-2.883641,1.089805],[-1.426682,-2.116600,-5.837249],[5.066422,2.369124,1.611799],[4.158929,-3.202311,-4.012597],[8.675283,-7.226865,-4.626569],[-7.326350,-3.283991,-4.278761],[2.515042,8.181788,-8.481620],[-7.648896,-7.048881,1.911601],[3.254753,-8.971979,-8.609623],[6.059253,0.491985,-6.423281],[-2.782315,4.312438,0.176447],[-8.883820,-6.323774,-3.079391],[8.147272,2.476817,-8.845818],[-7.417221,3.994949,4.063854],[2.905888,9.141136,4.165093],[1.995361,6.806624,-7.175948],[-9.657244,1.878036,-3.754595],[-2.774804,-6.737809,5.248171],[-4.282676,2.309809,-9.661639],[6.224615,1.092066,9.184750],[-5.617365,-8.722160,4.037412],[2.592622,3.074658,2.405146],[-1.762534,-0.217228,3.377991],[-4.524293,0.173613,1.897586],[-6.809563,5.337895,-7.594773],[-6.459316,7.436455,-7.851909],[7.332512,8.889999,-3.678690],[-2.110155,-5.882221,-5.962838],[2.459836,8.844653,-2.601643],[-4.284447,4.448770,-3.502810],[-1.326144,1.531940,4.841446],[0.413296,3.506413,1.017596],[3.070659,-5.327348,-8.689164],[9.759463,4.081855,-8.111698],[3.836508,6.484857,6.051967],[-7.678540,-4.144229,7.566119],[4.126421,5.892338,0.276387],[4.616678,-7.395410,-7.255100],[-6.403016,-5.825924,-2.830629],[6.958928,-9.513283,9.636016],[-1.438823,0.096286,4.263505],[-2.763581,4.262116,5.495449],[-4.938297,3.899982,-2.401883],[-7.862839,3.024318,5.124618],[9.248260,-8.810045,0.681658],[9.681454,3.108347,-9.676556],[-2.610089,-3.947092,-7.244680],[-4.633362,-1.052848,-3.206383],[-3.906558,1.604352,6.084395],[2.613707,3.418306,-4.023421],[9.982829,-6.434554,6.101930],[5.772658,5.914024,2.124773],[8.345472,-4.123553,-1.505010],[1.371325,5.942630,-0.255083],[5.474239,-5.546525,7.985894],[1.311440,-2.966867,-6.413930],[-2.458914,7.403316,7.585781],[-0.357319,9.992952,-4.196630],[3.001505,-7.746304,-9.336554],[6.974443,-0.710745,-3.653952],[7.234651,1.111334,5.135955],[2.116004,4.943021,3.330943],[1.339388,-1.819198,-7.603135],[-0.365167,-5.743721,1.361396],[-1.856458,-1.111899,-4.204310]], dtype = "float64")#candidate|7535|(156, 3)|const|float64
bop_7536 = relay.bitwise_and(call_7507.astype('uint64'), const_7535.astype('uint64')) # shape=(156, 3)
bop_7539 = relay.bitwise_and(call_7508.astype('uint64'), const_7535.astype('uint64')) # shape=(156, 3)
bop_7545 = relay.minimum(call_7507.astype('int32'), const_7535.astype('int32')) # shape=(156, 3)
bop_7548 = relay.minimum(call_7508.astype('int32'), const_7535.astype('int32')) # shape=(156, 3)
bop_7552 = relay.maximum(bop_7536.astype('uint64'), call_7507.astype('uint64')) # shape=(156, 3)
bop_7555 = relay.maximum(bop_7539.astype('uint64'), call_7508.astype('uint64')) # shape=(156, 3)
func_1592_call = mod.get_global_var('func_1592')
func_1594_call = mutated_mod.get_global_var('func_1594')
call_7561 = relay.TupleGetItem(func_1592_call(), 0)
call_7562 = relay.TupleGetItem(func_1594_call(), 0)
output = relay.Tuple([bop_7545,bop_7552,call_7561,])
output2 = relay.Tuple([bop_7548,bop_7555,call_7562,])
func_7563 = relay.Function([], output)
mod['func_7563'] = func_7563
mod = relay.transform.InferType()(mod)
mutated_mod['func_7563'] = func_7563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7563_call = mutated_mod.get_global_var('func_7563')
call_7564 = func_7563_call()
output = call_7564
func_7565 = relay.Function([], output)
mutated_mod['func_7565'] = func_7565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_444_call = mod.get_global_var('func_444')
func_446_call = mutated_mod.get_global_var('func_446')
call_7600 = relay.TupleGetItem(func_444_call(), 0)
call_7601 = relay.TupleGetItem(func_446_call(), 0)
output = call_7600
output2 = call_7601
func_7602 = relay.Function([], output)
mod['func_7602'] = func_7602
mod = relay.transform.InferType()(mod)
mutated_mod['func_7602'] = func_7602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7602_call = mutated_mod.get_global_var('func_7602')
call_7603 = func_7602_call()
output = call_7603
func_7604 = relay.Function([], output)
mutated_mod['func_7604'] = func_7604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1067_call = mod.get_global_var('func_1067')
func_1069_call = mutated_mod.get_global_var('func_1069')
call_7637 = relay.TupleGetItem(func_1067_call(), 0)
call_7638 = relay.TupleGetItem(func_1069_call(), 0)
var_7639 = relay.var("var_7639", dtype = "int8", shape = (7, 12, 2))#candidate|7639|(7, 12, 2)|var|int8
bop_7640 = relay.left_shift(call_7637.astype('uint16'), var_7639.astype('uint16')) # shape=(7, 12, 2)
bop_7643 = relay.left_shift(call_7638.astype('uint16'), var_7639.astype('uint16')) # shape=(7, 12, 2)
func_2078_call = mod.get_global_var('func_2078')
func_2081_call = mutated_mod.get_global_var('func_2081')
const_7647 = relay.const([[1,-2,4,7,10,3,9,2,4,3,-4,-5,10,-4,5,-2,6,9,2,3,-6,-1,-8,10,-3,-5,1,-5,-2,-5,7,-5,-1,-10,-2,5,1,-5,-9,1,8,-8,10,10,-6,-10,2,3,-10,8,-8,-2,-1,10,-1,-1,-10,8,6,-1,2,-3,-9,-10,3,-10,3,2,10,1,4,10,2,-6,-5,1,8,-4,2,5,3,6,9,9,1,-1,-3,3,-9,4,-5,1,-8,-10,10,6,5,9,-2,-3,8,2,-7,7,-1,9,-3,-9,5,1,-7,9,1,-5,-4,-7,-4,-4,-1,6,9,8,-6,-2,8,-8,-10,-8,3,-3,-4,1,-7,-9,-7,2,10,9,9,-1,-5,-2,4,-8],[-3,-7,-1,-5,5,-9,-8,-8,3,8,-9,6,6,2,10,-10,-3,10,-5,-4,-8,5,-8,-6,-2,-10,3,-6,-8,2,10,-10,9,7,-4,8,-8,8,6,4,2,9,-1,-6,-5,4,-2,-6,-4,-7,-6,10,8,7,-6,9,4,-3,5,4,10,3,4,-5,4,9,-6,1,9,-7,-10,2,8,-1,-7,-1,4,-8,-5,9,4,-9,-8,-6,10,-3,4,4,-3,5,7,8,1,-2,-9,-8,-10,7,7,9,1,-6,9,6,-5,3,-8,5,-9,8,9,-2,10,9,5,3,-9,-10,2,-2,9,-9,8,-6,3,4,-7,1,8,-5,7,10,10,4,-7,7,4,3,-1,7,-3,8,-9,-7],[10,-3,-9,-2,-4,1,3,-7,3,8,-1,2,6,-3,-8,6,-2,4,4,2,-2,-9,-8,-3,8,-9,-6,2,10,9,-6,5,-5,-9,4,-7,4,-3,-4,-5,8,3,4,6,-1,-1,1,4,6,-7,7,-9,9,3,-8,8,-10,-8,6,-8,10,-5,9,8,-7,8,-8,4,8,-3,-6,2,1,2,-5,-6,2,-5,5,8,10,-5,-10,-8,-6,5,-1,10,7,1,4,7,3,9,-7,7,1,-6,2,-1,4,-2,5,8,4,3,9,4,-4,-7,7,10,7,-1,1,-9,10,-1,3,-6,-1,3,-3,-9,9,9,1,6,-5,-10,2,3,-1,6,6,-9,3,4,-10,-2,-2,-6,10,2],[10,-2,-3,6,-9,-8,-4,-1,-10,4,9,-8,9,-5,-6,4,1,2,-5,6,9,-1,2,4,7,1,-4,-9,4,3,3,10,7,7,-8,-6,-6,2,6,-9,3,-3,2,-1,-7,8,4,-3,-10,1,-1,7,-1,-9,-6,-2,-10,-8,-8,-1,-5,-3,7,-8,-6,4,-5,9,1,-4,6,-6,2,1,4,3,10,-10,3,5,8,-7,2,8,-3,8,8,-6,-9,10,-6,5,-2,3,3,-5,9,4,9,3,-4,-1,-7,5,-1,-3,10,5,5,7,7,-10,5,6,-6,8,-1,6,-6,-8,-8,4,-9,7,-8,-1,-8,1,-5,-1,-5,-2,-8,8,1,-10,7,4,4,9,10,7,2,-3],[-5,9,3,-10,-2,-4,-4,-10,10,-8,-9,-8,-10,-7,3,1,-2,7,4,8,-6,8,9,-3,-6,-5,10,4,-8,-2,10,-10,6,10,5,-5,-10,-2,-5,-10,-8,5,-10,-7,1,1,5,-8,9,10,-5,6,9,6,5,-4,3,-8,-10,1,-6,-5,-4,-1,-10,-6,7,-2,-1,10,-6,-8,4,2,-3,-5,5,-10,-2,3,-2,-9,-2,5,3,1,2,10,5,1,-5,5,-6,-3,5,-2,-5,-6,-4,-2,8,8,-3,7,-8,-6,-5,-7,7,1,3,1,-6,7,-7,9,-4,-7,-5,5,-3,8,-3,10,4,1,9,-7,8,7,5,-5,4,6,-6,-3,-3,8,-6,5,2,-7,-10,7],[10,-5,1,4,2,5,2,-1,-10,10,-9,-8,-2,3,-1,10,-4,4,7,-5,7,-8,-9,-3,-6,-5,-7,6,-9,-3,-9,10,10,-3,4,-5,-7,2,-10,2,-8,-2,1,-6,9,9,-2,3,6,8,-3,3,-4,3,9,-1,-4,4,3,4,-9,9,-5,-3,8,1,4,1,-10,-3,10,6,9,9,-9,-1,7,8,-2,-3,4,-2,-9,-6,7,-7,-7,3,2,5,7,10,8,8,-2,-2,8,-3,-7,7,2,1,9,-3,-9,4,8,4,3,8,4,2,-2,-8,-7,2,-8,-9,10,10,2,-5,-8,-8,10,8,6,5,-6,8,9,1,5,-4,1,4,8,8,8,-10,-2,2,8,-7],[-2,8,-4,-9,-8,-6,1,-6,1,6,8,8,4,-9,9,9,-8,5,3,-5,-10,-3,10,9,-3,-1,-1,-2,-8,9,6,1,2,-8,-1,-9,-3,-2,-2,-4,-4,-6,3,1,-1,-3,8,-1,-1,7,-3,4,1,-8,-5,-7,-9,-5,3,8,-6,-8,-6,-7,9,8,2,-5,8,-5,-10,-1,7,5,-1,1,3,-4,-10,5,-4,-1,-7,-1,-2,7,9,2,3,6,-10,3,-6,-4,7,6,-6,-10,-3,-7,7,8,-3,2,10,2,-4,-7,2,-9,-3,-10,1,-2,-9,1,5,4,2,4,5,-3,-10,9,4,-1,-4,7,-3,2,-10,-9,-4,4,8,-9,-5,2,-5,-7,1,-7,3,10],[3,-7,5,-9,-7,-5,3,10,10,-3,-2,-5,10,-8,4,-8,-10,-1,1,3,2,-4,6,3,3,1,6,-10,8,1,8,10,-4,-4,-10,2,-5,-9,2,6,-7,3,-5,-10,-3,-8,2,-8,10,1,8,-3,4,5,3,-1,10,-4,7,1,-8,-10,6,7,1,-7,-5,-4,-4,5,10,-10,10,-7,-1,-8,7,7,7,1,-4,-8,1,-8,-1,-6,8,3,-1,6,1,9,1,1,-2,7,5,6,7,2,-6,-1,4,2,-6,-9,10,3,6,9,-8,-5,-2,-8,-3,-7,1,-3,1,2,2,2,-9,-3,-1,-4,-1,-4,8,-3,6,-1,-7,-2,8,8,5,-1,-7,1,9,10,2,2],[-10,2,5,3,-8,4,10,7,2,-2,-2,-8,8,-8,2,2,-5,7,2,5,4,-7,9,-2,1,1,-8,-4,-7,-7,-4,-2,-7,-10,9,-8,-5,9,-8,9,4,-3,-7,7,9,4,6,4,-4,-2,-4,-8,-7,4,-6,5,3,10,-6,3,-4,-1,-2,6,1,-9,-10,3,1,-3,2,-9,-7,-4,-8,8,-5,-4,6,-1,8,4,-4,-7,8,-4,-9,5,1,-9,-6,3,-10,6,-7,-4,6,4,9,-7,-3,-5,-3,8,-10,5,8,7,6,-3,-2,-9,7,10,-9,10,9,2,-8,8,-9,-3,-2,2,-6,3,4,-6,-7,8,7,-8,5,-10,10,10,4,4,-4,4,-1,-7,10,7],[-4,-5,-3,7,1,-3,-9,10,-6,9,-1,9,-1,9,2,1,3,6,7,5,3,10,-1,-5,-5,9,7,-9,6,2,-6,-3,6,-6,-3,2,-7,7,-1,6,-5,1,3,-2,10,7,6,-6,9,5,2,-7,-10,-8,-5,8,-9,5,10,1,3,7,-9,-2,-6,-10,4,7,2,-4,10,-8,-2,-3,10,4,3,3,-8,-8,-1,1,6,9,5,-4,7,6,-6,-4,2,-10,-3,6,-7,4,-3,-3,-4,8,6,-6,5,-4,10,5,-10,-6,-9,4,7,4,-4,-10,7,-10,9,10,6,2,4,8,6,6,-6,-1,-8,-4,2,-3,-3,6,6,5,9,-10,9,-8,-1,10,7,-2,-8,7]], dtype = "int8")#candidate|7647|(10, 144)|const|int8
call_7646 = relay.TupleGetItem(func_2078_call(relay.reshape(const_7647.astype('int8'), [360, 4])), 0)
call_7648 = relay.TupleGetItem(func_2081_call(relay.reshape(const_7647.astype('int8'), [360, 4])), 0)
var_7650 = relay.var("var_7650", dtype = "uint16", shape = (7, 12, 2))#candidate|7650|(7, 12, 2)|var|uint16
bop_7651 = relay.bitwise_and(bop_7640.astype('uint32'), relay.reshape(var_7650.astype('uint32'), relay.shape_of(bop_7640))) # shape=(7, 12, 2)
bop_7654 = relay.bitwise_and(bop_7643.astype('uint32'), relay.reshape(var_7650.astype('uint32'), relay.shape_of(bop_7643))) # shape=(7, 12, 2)
output = relay.Tuple([call_7646,const_7647,bop_7651,])
output2 = relay.Tuple([call_7648,const_7647,bop_7654,])
func_7672 = relay.Function([var_7639,var_7650,], output)
mod['func_7672'] = func_7672
mod = relay.transform.InferType()(mod)
mutated_mod['func_7672'] = func_7672
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7672_call = mutated_mod.get_global_var('func_7672')
var_7674 = relay.var("var_7674", dtype = "int8", shape = (7, 12, 2))#candidate|7674|(7, 12, 2)|var|int8
var_7675 = relay.var("var_7675", dtype = "uint16", shape = (7, 12, 2))#candidate|7675|(7, 12, 2)|var|uint16
call_7673 = func_7672_call(var_7674,var_7675,)
output = call_7673
func_7676 = relay.Function([var_7674,var_7675,], output)
mutated_mod['func_7676'] = func_7676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6224_call = mod.get_global_var('func_6224')
func_6226_call = mutated_mod.get_global_var('func_6226')
call_7687 = relay.TupleGetItem(func_6224_call(), 0)
call_7688 = relay.TupleGetItem(func_6226_call(), 0)
func_1472_call = mod.get_global_var('func_1472')
func_1473_call = mutated_mod.get_global_var('func_1473')
call_7710 = func_1472_call()
call_7711 = func_1472_call()
bop_7714 = relay.logical_and(call_7687.astype('bool'), relay.reshape(call_7710.astype('bool'), relay.shape_of(call_7687))) # shape=(1, 12, 2)
bop_7717 = relay.logical_and(call_7688.astype('bool'), relay.reshape(call_7711.astype('bool'), relay.shape_of(call_7688))) # shape=(1, 12, 2)
output = relay.Tuple([bop_7714,])
output2 = relay.Tuple([bop_7717,])
func_7723 = relay.Function([], output)
mod['func_7723'] = func_7723
mod = relay.transform.InferType()(mod)
mutated_mod['func_7723'] = func_7723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7723_call = mutated_mod.get_global_var('func_7723')
call_7724 = func_7723_call()
output = call_7724
func_7725 = relay.Function([], output)
mutated_mod['func_7725'] = func_7725
mutated_mod = relay.transform.InferType()(mutated_mod)
func_517_call = mod.get_global_var('func_517')
func_518_call = mutated_mod.get_global_var('func_518')
call_7788 = func_517_call()
call_7789 = func_517_call()
output = call_7788
output2 = call_7789
func_7791 = relay.Function([], output)
mod['func_7791'] = func_7791
mod = relay.transform.InferType()(mod)
output = func_7791()
func_7792 = relay.Function([], output)
mutated_mod['func_7792'] = func_7792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7723_call = mod.get_global_var('func_7723')
func_7725_call = mutated_mod.get_global_var('func_7725')
call_7796 = relay.TupleGetItem(func_7723_call(), 0)
call_7797 = relay.TupleGetItem(func_7725_call(), 0)
func_7174_call = mod.get_global_var('func_7174')
func_7176_call = mutated_mod.get_global_var('func_7176')
call_7816 = func_7174_call()
call_7817 = func_7174_call()
output = relay.Tuple([call_7796,call_7816,])
output2 = relay.Tuple([call_7797,call_7817,])
func_7835 = relay.Function([], output)
mod['func_7835'] = func_7835
mod = relay.transform.InferType()(mod)
mutated_mod['func_7835'] = func_7835
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7835_call = mutated_mod.get_global_var('func_7835')
call_7836 = func_7835_call()
output = call_7836
func_7837 = relay.Function([], output)
mutated_mod['func_7837'] = func_7837
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5356_call = mod.get_global_var('func_5356')
func_5357_call = mutated_mod.get_global_var('func_5357')
call_7909 = relay.TupleGetItem(func_5356_call(), 1)
call_7910 = relay.TupleGetItem(func_5357_call(), 1)
output = call_7909
output2 = call_7910
func_7911 = relay.Function([], output)
mod['func_7911'] = func_7911
mod = relay.transform.InferType()(mod)
output = func_7911()
func_7912 = relay.Function([], output)
mutated_mod['func_7912'] = func_7912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5934_call = mod.get_global_var('func_5934')
func_5935_call = mutated_mod.get_global_var('func_5935')
call_7950 = relay.TupleGetItem(func_5934_call(), 0)
call_7951 = relay.TupleGetItem(func_5935_call(), 0)
func_7791_call = mod.get_global_var('func_7791')
func_7792_call = mutated_mod.get_global_var('func_7792')
call_7963 = func_7791_call()
call_7964 = func_7791_call()
output = relay.Tuple([call_7950,call_7963,])
output2 = relay.Tuple([call_7951,call_7964,])
func_7971 = relay.Function([], output)
mod['func_7971'] = func_7971
mod = relay.transform.InferType()(mod)
output = func_7971()
func_7972 = relay.Function([], output)
mutated_mod['func_7972'] = func_7972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1462_call = mod.get_global_var('func_1462')
func_1463_call = mutated_mod.get_global_var('func_1463')
call_7973 = func_1462_call()
call_7974 = func_1462_call()
output = relay.Tuple([call_7973,])
output2 = relay.Tuple([call_7974,])
func_7975 = relay.Function([], output)
mod['func_7975'] = func_7975
mod = relay.transform.InferType()(mod)
mutated_mod['func_7975'] = func_7975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7975_call = mutated_mod.get_global_var('func_7975')
call_7976 = func_7975_call()
output = call_7976
func_7977 = relay.Function([], output)
mutated_mod['func_7977'] = func_7977
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8027 = relay.var("var_8027", dtype = "int32", shape = (5, 10, 14))#candidate|8027|(5, 10, 14)|var|int32
var_8028 = relay.var("var_8028", dtype = "int32", shape = (5, 10, 14))#candidate|8028|(5, 10, 14)|var|int32
bop_8029 = relay.add(var_8027.astype('int32'), relay.reshape(var_8028.astype('int32'), relay.shape_of(var_8027))) # shape=(5, 10, 14)
output = relay.Tuple([bop_8029,])
output2 = relay.Tuple([bop_8029,])
func_8032 = relay.Function([var_8027,var_8028,], output)
mod['func_8032'] = func_8032
mod = relay.transform.InferType()(mod)
mutated_mod['func_8032'] = func_8032
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8032_call = mutated_mod.get_global_var('func_8032')
var_8034 = relay.var("var_8034", dtype = "int32", shape = (5, 10, 14))#candidate|8034|(5, 10, 14)|var|int32
var_8035 = relay.var("var_8035", dtype = "int32", shape = (5, 10, 14))#candidate|8035|(5, 10, 14)|var|int32
call_8033 = func_8032_call(var_8034,var_8035,)
output = call_8033
func_8036 = relay.Function([var_8034,var_8035,], output)
mutated_mod['func_8036'] = func_8036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6789_call = mod.get_global_var('func_6789')
func_6791_call = mutated_mod.get_global_var('func_6791')
call_8087 = func_6789_call()
call_8088 = func_6789_call()
output = relay.Tuple([call_8087,])
output2 = relay.Tuple([call_8088,])
func_8101 = relay.Function([], output)
mod['func_8101'] = func_8101
mod = relay.transform.InferType()(mod)
output = func_8101()
func_8102 = relay.Function([], output)
mutated_mod['func_8102'] = func_8102
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5051_call = mod.get_global_var('func_5051')
func_5052_call = mutated_mod.get_global_var('func_5052')
call_8139 = func_5051_call()
call_8140 = func_5051_call()
output = relay.Tuple([call_8139,])
output2 = relay.Tuple([call_8140,])
func_8149 = relay.Function([], output)
mod['func_8149'] = func_8149
mod = relay.transform.InferType()(mod)
mutated_mod['func_8149'] = func_8149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8149_call = mutated_mod.get_global_var('func_8149')
call_8150 = func_8149_call()
output = call_8150
func_8151 = relay.Function([], output)
mutated_mod['func_8151'] = func_8151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1472_call = mod.get_global_var('func_1472')
func_1473_call = mutated_mod.get_global_var('func_1473')
call_8154 = func_1472_call()
call_8155 = func_1472_call()
output = relay.Tuple([call_8154,])
output2 = relay.Tuple([call_8155,])
func_8193 = relay.Function([], output)
mod['func_8193'] = func_8193
mod = relay.transform.InferType()(mod)
mutated_mod['func_8193'] = func_8193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8193_call = mutated_mod.get_global_var('func_8193')
call_8194 = func_8193_call()
output = call_8194
func_8195 = relay.Function([], output)
mutated_mod['func_8195'] = func_8195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1592_call = mod.get_global_var('func_1592')
func_1594_call = mutated_mod.get_global_var('func_1594')
call_8199 = relay.TupleGetItem(func_1592_call(), 1)
call_8200 = relay.TupleGetItem(func_1594_call(), 1)
output = call_8199
output2 = call_8200
func_8206 = relay.Function([], output)
mod['func_8206'] = func_8206
mod = relay.transform.InferType()(mod)
mutated_mod['func_8206'] = func_8206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8206_call = mutated_mod.get_global_var('func_8206')
call_8207 = func_8206_call()
output = call_8207
func_8208 = relay.Function([], output)
mutated_mod['func_8208'] = func_8208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8193_call = mod.get_global_var('func_8193')
func_8195_call = mutated_mod.get_global_var('func_8195')
call_8227 = relay.TupleGetItem(func_8193_call(), 0)
call_8228 = relay.TupleGetItem(func_8195_call(), 0)
output = relay.Tuple([call_8227,])
output2 = relay.Tuple([call_8228,])
func_8253 = relay.Function([], output)
mod['func_8253'] = func_8253
mod = relay.transform.InferType()(mod)
mutated_mod['func_8253'] = func_8253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8253_call = mutated_mod.get_global_var('func_8253')
call_8254 = func_8253_call()
output = call_8254
func_8255 = relay.Function([], output)
mutated_mod['func_8255'] = func_8255
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4804_call = mod.get_global_var('func_4804')
func_4805_call = mutated_mod.get_global_var('func_4805')
call_8256 = func_4804_call()
call_8257 = func_4804_call()
func_884_call = mod.get_global_var('func_884')
func_886_call = mutated_mod.get_global_var('func_886')
var_8281 = relay.var("var_8281", dtype = "float32", shape = (156, 2))#candidate|8281|(156, 2)|var|float32
call_8280 = relay.TupleGetItem(func_884_call(relay.reshape(var_8281.astype('float32'), [13, 8, 3])), 4)
call_8282 = relay.TupleGetItem(func_886_call(relay.reshape(var_8281.astype('float32'), [13, 8, 3])), 4)
func_2135_call = mod.get_global_var('func_2135')
func_2138_call = mutated_mod.get_global_var('func_2138')
const_8292 = relay.const([-9.231568,4.311557,-8.365679,-2.049732,-9.510913,9.122371,-2.682204,-8.141821,-0.305961,-6.599728,8.491291,3.459801,-9.133993,-3.000276,9.705666,-7.890089,-5.570580,-3.787925,2.316124,-9.736713,-2.042646,-3.152020,6.654598,-5.686080,3.327023,-8.452115,1.534674,-2.681673,-5.622550,5.861055,0.936824,8.920166,8.399334,-8.885761,-6.065454,-7.748064,-3.719901,3.658580,-1.339723,3.678164,-4.992012,-9.791925,1.960952,4.681641,-9.919621,-9.863830,3.012638,0.430818,9.271367,7.929936,-1.897759,-0.476669,-9.622655,-5.167388,-9.789452,4.529135,5.207222,-6.701729,-5.717713,-0.477826,6.541571,-7.206602,7.953448,0.768825,-3.712778,-0.340145,5.260750,7.468113,6.592929,-9.774648,-8.520919,-5.650534], dtype = "float64")#candidate|8292|(72,)|const|float64
call_8291 = relay.TupleGetItem(func_2135_call(relay.reshape(const_8292.astype('float64'), [1, 72])), 2)
call_8293 = relay.TupleGetItem(func_2138_call(relay.reshape(const_8292.astype('float64'), [1, 72])), 2)
output = relay.Tuple([call_8256,call_8280,var_8281,call_8291,const_8292,])
output2 = relay.Tuple([call_8257,call_8282,var_8281,call_8293,const_8292,])
func_8294 = relay.Function([var_8281,], output)
mod['func_8294'] = func_8294
mod = relay.transform.InferType()(mod)
var_8295 = relay.var("var_8295", dtype = "float32", shape = (156, 2))#candidate|8295|(156, 2)|var|float32
output = func_8294(var_8295)
func_8296 = relay.Function([var_8295], output)
mutated_mod['func_8296'] = func_8296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5325_call = mod.get_global_var('func_5325')
func_5326_call = mutated_mod.get_global_var('func_5326')
call_8378 = relay.TupleGetItem(func_5325_call(), 1)
call_8379 = relay.TupleGetItem(func_5326_call(), 1)
func_7602_call = mod.get_global_var('func_7602')
func_7604_call = mutated_mod.get_global_var('func_7604')
call_8382 = func_7602_call()
call_8383 = func_7602_call()
output = relay.Tuple([call_8378,call_8382,])
output2 = relay.Tuple([call_8379,call_8383,])
func_8401 = relay.Function([], output)
mod['func_8401'] = func_8401
mod = relay.transform.InferType()(mod)
output = func_8401()
func_8402 = relay.Function([], output)
mutated_mod['func_8402'] = func_8402
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4447_call = mod.get_global_var('func_4447')
func_4448_call = mutated_mod.get_global_var('func_4448')
call_8460 = relay.TupleGetItem(func_4447_call(), 0)
call_8461 = relay.TupleGetItem(func_4448_call(), 0)
func_8253_call = mod.get_global_var('func_8253')
func_8255_call = mutated_mod.get_global_var('func_8255')
call_8468 = relay.TupleGetItem(func_8253_call(), 0)
call_8469 = relay.TupleGetItem(func_8255_call(), 0)
output = relay.Tuple([call_8460,call_8468,])
output2 = relay.Tuple([call_8461,call_8469,])
func_8470 = relay.Function([], output)
mod['func_8470'] = func_8470
mod = relay.transform.InferType()(mod)
mutated_mod['func_8470'] = func_8470
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8470_call = mutated_mod.get_global_var('func_8470')
call_8471 = func_8470_call()
output = call_8471
func_8472 = relay.Function([], output)
mutated_mod['func_8472'] = func_8472
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7563_call = mod.get_global_var('func_7563')
func_7565_call = mutated_mod.get_global_var('func_7565')
call_8487 = relay.TupleGetItem(func_7563_call(), 2)
call_8488 = relay.TupleGetItem(func_7565_call(), 2)
func_7123_call = mod.get_global_var('func_7123')
func_7125_call = mutated_mod.get_global_var('func_7125')
call_8523 = relay.TupleGetItem(func_7123_call(), 0)
call_8524 = relay.TupleGetItem(func_7125_call(), 0)
output = relay.Tuple([call_8487,call_8523,])
output2 = relay.Tuple([call_8488,call_8524,])
func_8536 = relay.Function([], output)
mod['func_8536'] = func_8536
mod = relay.transform.InferType()(mod)
mutated_mod['func_8536'] = func_8536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8536_call = mutated_mod.get_global_var('func_8536')
call_8537 = func_8536_call()
output = call_8537
func_8538 = relay.Function([], output)
mutated_mod['func_8538'] = func_8538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4447_call = mod.get_global_var('func_4447')
func_4448_call = mutated_mod.get_global_var('func_4448')
call_8548 = relay.TupleGetItem(func_4447_call(), 2)
call_8549 = relay.TupleGetItem(func_4448_call(), 2)
func_1285_call = mod.get_global_var('func_1285')
func_1287_call = mutated_mod.get_global_var('func_1287')
call_8554 = func_1285_call()
call_8555 = func_1285_call()
func_1695_call = mod.get_global_var('func_1695')
func_1698_call = mutated_mod.get_global_var('func_1698')
const_8591 = relay.const([[-7.767661,3.090528],[7.780016,6.314541],[7.587607,8.969850],[-3.683050,4.324216],[1.044764,-2.112143],[-6.228796,8.316099],[-0.685512,-9.711407],[2.744462,4.892239],[-2.419960,-7.608313],[3.231899,-3.261887],[-0.269593,1.566566],[-5.347088,9.394454],[-4.856211,-1.038988],[-7.128935,-1.645094],[6.540675,4.597194],[9.223619,-7.467368],[1.242204,7.753577],[-7.269386,-4.922761],[1.179476,6.604029],[-3.598956,1.646134],[-3.456680,-4.515377],[-5.798793,6.205622],[2.020344,-0.871793],[2.332202,9.204419],[-7.973359,-0.545794],[-2.349346,8.060411],[-4.488478,6.479364],[-4.071453,2.412898],[-6.928677,4.776460],[-4.134865,-2.207837],[4.891109,-6.359027],[8.988664,-0.006168],[-4.105660,-9.591263],[7.667216,8.993317],[-8.473660,-4.541856],[3.001580,-3.498372],[7.381411,-2.054579],[-5.370147,-6.481209],[-3.721569,6.164738],[-5.522153,6.009897],[-2.883774,8.110389],[2.109912,0.636595],[4.038609,-2.123492],[8.652239,-0.794903],[-2.088338,-4.432247],[-3.193700,8.711570],[-8.831876,-3.582968],[-5.985100,4.785444],[-8.872511,-7.988558],[6.072490,6.426912],[5.786529,-2.467420],[-2.812655,-1.305595],[3.583544,-2.288784],[4.262119,-2.179636],[-3.710841,-3.768287],[-5.817180,3.338196],[-1.667088,6.457838],[0.814700,-9.139032],[-6.180315,7.731050],[7.372408,-3.832725],[-2.411205,-0.815987],[-6.295694,2.120461],[-3.566645,5.412142],[-8.466407,9.963977],[-3.779283,-3.366395],[3.966788,-1.839230],[8.013815,1.489446],[3.393671,-8.793455],[-4.980656,5.105827],[5.836959,1.952758],[-4.761518,9.075412],[6.480832,4.560442],[0.134331,4.633204],[-3.977383,-2.060939],[6.114315,7.208915],[3.001959,-0.290203],[-6.887848,-8.606302],[1.588923,7.569447],[-5.658297,-9.381557],[3.673951,9.961241],[6.118120,-4.799829],[7.375627,-9.177857],[-9.778415,0.421979],[1.917955,9.739049],[-6.968262,9.315760],[4.464304,2.614218],[4.209140,3.744894],[-1.662506,5.532827],[4.174380,3.231829],[0.188227,9.003933],[5.002312,7.199312],[-0.604103,8.525166],[3.809575,-0.087233],[8.608480,-0.512116],[3.049133,-7.313556],[8.045252,-4.787318],[3.442189,4.182127],[7.804284,-9.202345],[5.667579,3.313762],[-1.419383,-5.122368],[6.605302,-7.716453],[5.798291,-3.288972],[-4.848947,-6.442776],[-1.442462,-8.039269],[-0.620457,-1.275842],[-4.471969,0.689064],[1.291595,7.180871],[7.803483,1.507398],[1.124138,3.125700],[-0.709834,1.234501],[-3.890037,-1.208915],[-9.782133,-7.112393],[-5.233960,-5.821978],[1.291268,8.569060],[-8.084553,-1.376116],[-0.776242,3.577460],[0.145380,-8.468818],[-1.399625,-7.554660],[6.732528,1.625974],[8.189183,2.476621],[9.300557,-3.588379],[1.053415,5.939922],[1.500946,1.155349],[1.803145,1.221548],[3.677116,-4.049426],[1.998907,6.604012],[-9.788961,8.105170],[-9.653262,9.803210],[-1.354318,4.817602],[3.614736,-4.963922],[-5.698735,7.732004],[-1.059474,4.872630],[-0.867613,7.162868],[-0.921119,7.433077],[9.662970,5.115086],[5.828997,4.068391],[-1.576159,6.044562],[5.050876,-9.330203],[8.482412,0.440661],[-2.387875,6.071473],[2.281950,6.341709],[6.110711,-5.915755],[7.662842,3.641821],[-9.408028,-9.535131],[7.129686,4.334664],[8.553108,-1.870995],[0.724051,-8.616261],[-8.278017,-3.313172],[-8.245523,-3.942546],[-0.805210,8.641976],[-3.533816,-2.556980],[6.975566,8.623777],[-9.788164,-5.465136],[0.053278,-0.266369],[-0.248462,-2.718189],[6.344938,-4.138612]], dtype = "float32")#candidate|8591|(156, 2)|const|float32
call_8590 = relay.TupleGetItem(func_1695_call(relay.reshape(const_8591.astype('float32'), [312,])), 6)
call_8592 = relay.TupleGetItem(func_1698_call(relay.reshape(const_8591.astype('float32'), [312,])), 6)
func_3449_call = mod.get_global_var('func_3449')
func_3450_call = mutated_mod.get_global_var('func_3450')
call_8598 = relay.TupleGetItem(func_3449_call(), 0)
call_8599 = relay.TupleGetItem(func_3450_call(), 0)
output = relay.Tuple([call_8548,call_8554,call_8590,const_8591,call_8598,])
output2 = relay.Tuple([call_8549,call_8555,call_8592,const_8591,call_8599,])
func_8601 = relay.Function([], output)
mod['func_8601'] = func_8601
mod = relay.transform.InferType()(mod)
mutated_mod['func_8601'] = func_8601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8601_call = mutated_mod.get_global_var('func_8601')
call_8602 = func_8601_call()
output = call_8602
func_8603 = relay.Function([], output)
mutated_mod['func_8603'] = func_8603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8536_call = mod.get_global_var('func_8536')
func_8538_call = mutated_mod.get_global_var('func_8538')
call_8613 = relay.TupleGetItem(func_8536_call(), 1)
call_8614 = relay.TupleGetItem(func_8538_call(), 1)
func_7174_call = mod.get_global_var('func_7174')
func_7176_call = mutated_mod.get_global_var('func_7176')
call_8621 = func_7174_call()
call_8622 = func_7174_call()
func_3096_call = mod.get_global_var('func_3096')
func_3101_call = mutated_mod.get_global_var('func_3101')
var_8626 = relay.var("var_8626", dtype = "float32", shape = (4, 24))#candidate|8626|(4, 24)|var|float32
call_8625 = relay.TupleGetItem(func_3096_call(relay.reshape(var_8626.astype('float32'), [8, 3, 4]), relay.reshape(var_8626.astype('float32'), [8, 3, 4]), relay.reshape(var_8626.astype('float32'), [8, 3, 4]), ), 2)
call_8627 = relay.TupleGetItem(func_3101_call(relay.reshape(var_8626.astype('float32'), [8, 3, 4]), relay.reshape(var_8626.astype('float32'), [8, 3, 4]), relay.reshape(var_8626.astype('float32'), [8, 3, 4]), ), 2)
output = relay.Tuple([call_8613,call_8621,call_8625,var_8626,])
output2 = relay.Tuple([call_8614,call_8622,call_8627,var_8626,])
func_8633 = relay.Function([var_8626,], output)
mod['func_8633'] = func_8633
mod = relay.transform.InferType()(mod)
var_8634 = relay.var("var_8634", dtype = "float32", shape = (4, 24))#candidate|8634|(4, 24)|var|float32
output = func_8633(var_8634)
func_8635 = relay.Function([var_8634], output)
mutated_mod['func_8635'] = func_8635
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8660 = relay.const([[[6.584202,1.247635,-3.901665,-0.501210],[-7.014222,-2.100818,6.171697,-1.602402],[7.921110,9.428921,-7.313755,1.914544],[8.063975,5.728203,-7.796479,4.508393],[0.533654,7.163674,3.243911,-2.926914]],[[0.311067,-2.299707,6.924244,8.184378],[2.951634,1.039634,-3.248021,4.914081],[0.415444,9.829602,2.483608,-3.018881],[9.413554,9.166405,4.002731,-9.483061],[-9.247554,5.236481,4.460769,2.408067]],[[-8.049313,-6.710812,6.412944,-8.365897],[6.477189,0.115808,-5.296023,0.324859],[2.639238,-6.388221,3.472943,-2.491541],[9.737729,2.622633,-8.866468,1.744814],[4.605651,1.030456,-2.784406,-3.566343]],[[3.338886,-6.891891,9.429522,4.306132],[-0.517633,1.906096,-2.642152,-6.472813],[3.330614,2.753231,-9.125182,-6.438222],[-2.461945,-8.852296,0.585468,-9.198007],[-6.945502,9.836050,4.698005,1.000110]],[[-3.089825,0.284134,-5.419333,6.486501],[1.979174,6.096999,6.155754,-0.314526],[0.408232,-3.133265,1.554979,5.382772],[-3.385142,8.629474,4.154730,4.866061],[2.635725,-9.263556,-6.031868,8.521803]],[[-2.912154,0.948138,1.790345,-4.501376],[5.772154,9.400043,2.727179,-5.958157],[5.703903,4.142928,-6.672731,1.834224],[6.244605,0.046289,9.518423,-2.741051],[3.201758,9.237555,6.988926,6.823928]],[[1.803157,1.472110,7.068520,-1.257469],[8.070790,0.887469,-4.140657,8.713909],[3.086016,-9.344626,1.607810,-2.684019],[-3.520611,3.544848,1.109122,-9.971714],[-4.458826,-1.426711,-4.024884,-5.870342]],[[-2.095786,2.904120,-2.746003,2.391831],[-9.073602,-8.695337,-8.478739,-2.452117],[4.682156,-6.150231,2.760622,4.068561],[-0.960427,0.952588,-3.960308,-5.220262],[-6.131931,6.449191,-2.844244,-0.319892]],[[-7.186305,-7.979285,7.328672,-1.634218],[2.942460,-4.636391,9.574603,-4.138961],[2.078138,-6.924576,4.063625,-5.019904],[0.488748,4.558286,-9.987593,-0.865812],[-3.862023,7.496428,5.140210,-0.532417]],[[-4.177123,3.484828,-4.474644,4.015590],[-5.129411,6.978298,-2.622091,8.539453],[-5.006893,0.113043,-3.344733,7.872052],[4.390188,-3.148090,-2.439854,1.876158],[2.407536,4.122665,-0.055770,7.676398]],[[-3.657238,-6.466764,1.469724,-6.114398],[-7.348801,-7.208134,8.673754,-3.270737],[5.067159,-9.648681,7.245401,-1.993777],[-2.364959,6.139247,5.905888,9.194737],[4.084551,-3.899509,5.768363,-5.639643]]], dtype = "float32")#candidate|8660|(11, 5, 4)|const|float32
uop_8661 = relay.acos(const_8660.astype('float32')) # shape=(11, 5, 4)
func_42_call = mod.get_global_var('func_42')
func_45_call = mutated_mod.get_global_var('func_45')
const_8670 = relay.const([-4.593110,3.479663,9.395139,4.820509,-7.312528,8.054972,-4.678522,0.747309,5.056583,3.218423,0.334372,0.215503,-5.035408,-4.683621,-1.429989,-9.354165,1.947358,4.450441,1.707977,2.531037,-8.884038,4.399629,9.670902,6.384674,-2.399633,-4.174098,6.861978,-4.826911,-7.335798,-3.847465,1.444795,8.497904,-2.001385,6.939260,5.003148,-3.328522,-2.852448,2.781821,-1.409846,-8.933900,6.469303,-5.457575,-7.753003,-5.182270,0.894281,-3.895860,4.455695,2.514736,-6.248558,4.311263,7.172806,-9.571371,-9.097644,4.589192,-6.728587,3.893509,3.839771,-8.067685,-7.344083,-8.673561,5.470790,-9.936954,-0.290936,2.843195,-6.656426,-6.246279,-6.365290,9.995166,-1.520770,3.733759,8.200363,-2.301857,-3.925533,-1.391074,2.881645,-2.526143,0.220659,4.804344,-4.927952,9.602876,-0.144362,6.321299,-5.368315,0.553894,0.727527,1.157286,3.131665,0.131321,-6.665682,-8.273794,-9.436630,6.357920,9.623712,8.458504,5.091146,-1.396323,9.483989,-8.372553,0.535690,-7.321794,-0.734082,3.834236,-6.624910,4.121266,-0.112721,-6.494255,-6.328289,6.866846,2.327674,6.272909,7.175893,-5.090114,6.589938,-5.603919,-0.612872,-7.412028,-8.934919,-3.597125,-2.392273,7.633242,0.775099,-2.213526,7.004218,8.758854,-5.627524,7.055297,-4.009648,-6.537618,-9.257910,-2.540021,-5.957558,2.938456,-4.912094,1.805279,0.781960,-3.867712,-2.819403,-8.660405,-5.548928,-4.739189,2.128016,-6.396100,4.134056,2.653302,0.290083,-2.842395,-7.161274,-7.097899,2.198159,-9.522248,-8.755208,0.925397,6.854958,9.056369,0.683901,-1.802966,9.137164,9.192537,-8.653335,3.672665,-8.587006,3.897263,2.743248,-5.771654,1.251814,-8.727324,6.322296,-5.065825,3.374499,-2.875816,-0.752824,9.874037,6.157318,-5.261406,-3.963874,0.231097,-8.767287,8.133587,-4.443803,-5.151523,-3.906391,1.289955,4.909645,-3.752008,6.920184,3.240539,-2.796247,-9.806358,7.252111,4.831091,-9.066063,2.366068,4.360997,-2.413060,-0.533285,9.193614,7.676182,-2.912762,-2.485380,-8.977899,1.572684,1.504886,-8.535981,2.101564,5.730375,0.479186,7.121964,-5.384026,-6.708828,-7.716104,8.219727,1.184427,-5.009309,4.064456,7.348920,9.320129,-6.267543,-2.546613,-9.076511,-7.865227,-9.187843,0.282500,-6.036804,-4.563866,-3.182947,4.617826,-4.560892,1.061319,-5.867175,1.588330,-5.763038,-2.774058,-5.708927,6.504139,-4.605688,-3.027790,-5.351843,-0.280740,6.039312,7.242885,8.410679,7.555905,3.506351,9.367546,-9.937288,3.288420,3.013662,8.936804,-3.292873,-0.811875,-7.469238,9.230042,-4.830867,-3.308329,-6.298791,4.939424,-9.632659,3.874352,9.037872,-5.702713,-3.988799,-9.282731,7.245786,0.265546,9.913200,4.784857,-7.642562,-9.224182,-1.766063,-8.410670,-4.731144,2.853912,-6.733496,-5.161762,8.904541,8.305471,6.476353,9.370997,6.977588,-7.113285,-9.221713,9.245135,8.336630,0.427609,-7.028577,-5.150288,7.455449,8.436588,0.560957,-2.449132,-5.546853,-5.261017,1.061208,9.028002,-8.304109,0.206220,2.007061,9.325892,-7.550549,-9.859820,-5.919819,7.022803,-2.348868,9.354546,1.606433,-8.826930,-1.297226,9.777724,-3.782356,-7.653315,-1.871088,6.988293,-5.305663,-4.151920,9.613273,3.271985,-1.502620,-8.413028,-0.275167,-8.082020,8.517410,6.916666,9.675566,1.975952,4.195234,-4.537336,-5.017506,1.256543,-4.014622,3.604946], dtype = "float64")#candidate|8670|(330,)|const|float64
call_8669 = relay.TupleGetItem(func_42_call(relay.reshape(const_8670.astype('float64'), [11, 6, 5])), 0)
call_8671 = relay.TupleGetItem(func_45_call(relay.reshape(const_8670.astype('float64'), [11, 6, 5])), 0)
func_2342_call = mod.get_global_var('func_2342')
func_2345_call = mutated_mod.get_global_var('func_2345')
var_8673 = relay.var("var_8673", dtype = "int8", shape = (54,))#candidate|8673|(54,)|var|int8
call_8672 = relay.TupleGetItem(func_2342_call(relay.reshape(var_8673.astype('int8'), [3, 9, 2]), relay.reshape(var_8673.astype('int8'), [3, 9, 2]), ), 1)
call_8674 = relay.TupleGetItem(func_2345_call(relay.reshape(var_8673.astype('int8'), [3, 9, 2]), relay.reshape(var_8673.astype('int8'), [3, 9, 2]), ), 1)
output = relay.Tuple([uop_8661,call_8669,const_8670,call_8672,var_8673,])
output2 = relay.Tuple([uop_8661,call_8671,const_8670,call_8674,var_8673,])
func_8700 = relay.Function([var_8673,], output)
mod['func_8700'] = func_8700
mod = relay.transform.InferType()(mod)
var_8701 = relay.var("var_8701", dtype = "int8", shape = (54,))#candidate|8701|(54,)|var|int8
output = func_8700(var_8701)
func_8702 = relay.Function([var_8701], output)
mutated_mod['func_8702'] = func_8702
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8706 = relay.var("var_8706", dtype = "float32", shape = (5, 14, 11))#candidate|8706|(5, 14, 11)|var|float32
uop_8707 = relay.erf(var_8706.astype('float32')) # shape=(5, 14, 11)
bop_8714 = relay.left_shift(uop_8707.astype('int64'), relay.reshape(var_8706.astype('int64'), relay.shape_of(uop_8707))) # shape=(5, 14, 11)
bop_8717 = relay.greater(uop_8707.astype('bool'), relay.reshape(bop_8714.astype('bool'), relay.shape_of(uop_8707))) # shape=(5, 14, 11)
output = bop_8717
output2 = bop_8717
func_8728 = relay.Function([var_8706,], output)
mod['func_8728'] = func_8728
mod = relay.transform.InferType()(mod)
var_8729 = relay.var("var_8729", dtype = "float32", shape = (5, 14, 11))#candidate|8729|(5, 14, 11)|var|float32
output = func_8728(var_8729)
func_8730 = relay.Function([var_8729], output)
mutated_mod['func_8730'] = func_8730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5934_call = mod.get_global_var('func_5934')
func_5935_call = mutated_mod.get_global_var('func_5935')
call_8827 = relay.TupleGetItem(func_5934_call(), 1)
call_8828 = relay.TupleGetItem(func_5935_call(), 1)
output = call_8827
output2 = call_8828
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
func_1592_call = mod.get_global_var('func_1592')
func_1594_call = mutated_mod.get_global_var('func_1594')
call_8868 = relay.TupleGetItem(func_1592_call(), 1)
call_8869 = relay.TupleGetItem(func_1594_call(), 1)
output = relay.Tuple([call_8868,])
output2 = relay.Tuple([call_8869,])
func_8871 = relay.Function([], output)
mod['func_8871'] = func_8871
mod = relay.transform.InferType()(mod)
mutated_mod['func_8871'] = func_8871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8871_call = mutated_mod.get_global_var('func_8871')
call_8872 = func_8871_call()
output = call_8872
func_8873 = relay.Function([], output)
mutated_mod['func_8873'] = func_8873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1067_call = mod.get_global_var('func_1067')
func_1069_call = mutated_mod.get_global_var('func_1069')
call_8897 = relay.TupleGetItem(func_1067_call(), 0)
call_8898 = relay.TupleGetItem(func_1069_call(), 0)
output = relay.Tuple([call_8897,])
output2 = relay.Tuple([call_8898,])
func_8908 = relay.Function([], output)
mod['func_8908'] = func_8908
mod = relay.transform.InferType()(mod)
output = func_8908()
func_8909 = relay.Function([], output)
mutated_mod['func_8909'] = func_8909
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8908_call = mod.get_global_var('func_8908')
func_8909_call = mutated_mod.get_global_var('func_8909')
call_8919 = relay.TupleGetItem(func_8908_call(), 0)
call_8920 = relay.TupleGetItem(func_8909_call(), 0)
output = call_8919
output2 = call_8920
func_8934 = relay.Function([], output)
mod['func_8934'] = func_8934
mod = relay.transform.InferType()(mod)
mutated_mod['func_8934'] = func_8934
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8934_call = mutated_mod.get_global_var('func_8934')
call_8935 = func_8934_call()
output = call_8935
func_8936 = relay.Function([], output)
mutated_mod['func_8936'] = func_8936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8908_call = mod.get_global_var('func_8908')
func_8909_call = mutated_mod.get_global_var('func_8909')
call_8937 = relay.TupleGetItem(func_8908_call(), 0)
call_8938 = relay.TupleGetItem(func_8909_call(), 0)
func_810_call = mod.get_global_var('func_810')
func_813_call = mutated_mod.get_global_var('func_813')
var_8947 = relay.var("var_8947", dtype = "float64", shape = (36, 2))#candidate|8947|(36, 2)|var|float64
call_8946 = relay.TupleGetItem(func_810_call(relay.reshape(var_8947.astype('float64'), [3, 12, 2])), 0)
call_8948 = relay.TupleGetItem(func_813_call(relay.reshape(var_8947.astype('float64'), [3, 12, 2])), 0)
func_1592_call = mod.get_global_var('func_1592')
func_1594_call = mutated_mod.get_global_var('func_1594')
call_8961 = relay.TupleGetItem(func_1592_call(), 0)
call_8962 = relay.TupleGetItem(func_1594_call(), 0)
var_8971 = relay.var("var_8971", dtype = "float64", shape = (36, 2))#candidate|8971|(36, 2)|var|float64
bop_8972 = relay.multiply(var_8947.astype('float64'), relay.reshape(var_8971.astype('float64'), relay.shape_of(var_8947))) # shape=(36, 2)
uop_8983 = relay.acosh(var_8971.astype('float32')) # shape=(36, 2)
output = relay.Tuple([call_8937,call_8946,call_8961,bop_8972,uop_8983,])
output2 = relay.Tuple([call_8938,call_8948,call_8962,bop_8972,uop_8983,])
func_8986 = relay.Function([var_8947,var_8971,], output)
mod['func_8986'] = func_8986
mod = relay.transform.InferType()(mod)
var_8987 = relay.var("var_8987", dtype = "float64", shape = (36, 2))#candidate|8987|(36, 2)|var|float64
var_8988 = relay.var("var_8988", dtype = "float64", shape = (36, 2))#candidate|8988|(36, 2)|var|float64
output = func_8986(var_8987,var_8988,)
func_8989 = relay.Function([var_8987,var_8988,], output)
mutated_mod['func_8989'] = func_8989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8934_call = mod.get_global_var('func_8934')
func_8936_call = mutated_mod.get_global_var('func_8936')
call_9078 = func_8934_call()
call_9079 = func_8934_call()
output = call_9078
output2 = call_9079
func_9100 = relay.Function([], output)
mod['func_9100'] = func_9100
mod = relay.transform.InferType()(mod)
mutated_mod['func_9100'] = func_9100
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9100_call = mutated_mod.get_global_var('func_9100')
call_9101 = func_9100_call()
output = call_9101
func_9102 = relay.Function([], output)
mutated_mod['func_9102'] = func_9102
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5002_call = mod.get_global_var('func_5002')
func_5004_call = mutated_mod.get_global_var('func_5004')
call_9112 = relay.TupleGetItem(func_5002_call(), 1)
call_9113 = relay.TupleGetItem(func_5004_call(), 1)
output = call_9112
output2 = call_9113
func_9123 = relay.Function([], output)
mod['func_9123'] = func_9123
mod = relay.transform.InferType()(mod)
output = func_9123()
func_9124 = relay.Function([], output)
mutated_mod['func_9124'] = func_9124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8101_call = mod.get_global_var('func_8101')
func_8102_call = mutated_mod.get_global_var('func_8102')
call_9162 = relay.TupleGetItem(func_8101_call(), 0)
call_9163 = relay.TupleGetItem(func_8102_call(), 0)
output = relay.Tuple([call_9162,])
output2 = relay.Tuple([call_9163,])
func_9178 = relay.Function([], output)
mod['func_9178'] = func_9178
mod = relay.transform.InferType()(mod)
mutated_mod['func_9178'] = func_9178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9178_call = mutated_mod.get_global_var('func_9178')
call_9179 = func_9178_call()
output = call_9179
func_9180 = relay.Function([], output)
mutated_mod['func_9180'] = func_9180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7723_call = mod.get_global_var('func_7723')
func_7725_call = mutated_mod.get_global_var('func_7725')
call_9225 = relay.TupleGetItem(func_7723_call(), 0)
call_9226 = relay.TupleGetItem(func_7725_call(), 0)
output = relay.Tuple([call_9225,])
output2 = relay.Tuple([call_9226,])
func_9230 = relay.Function([], output)
mod['func_9230'] = func_9230
mod = relay.transform.InferType()(mod)
mutated_mod['func_9230'] = func_9230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9230_call = mutated_mod.get_global_var('func_9230')
call_9231 = func_9230_call()
output = call_9231
func_9232 = relay.Function([], output)
mutated_mod['func_9232'] = func_9232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8536_call = mod.get_global_var('func_8536')
func_8538_call = mutated_mod.get_global_var('func_8538')
call_9280 = relay.TupleGetItem(func_8536_call(), 1)
call_9281 = relay.TupleGetItem(func_8538_call(), 1)
func_4318_call = mod.get_global_var('func_4318')
func_4321_call = mutated_mod.get_global_var('func_4321')
const_9287 = relay.const([-4.031187,7.604747,5.318206,-0.197810,-9.442965,9.910212,7.900488,4.018934,6.120849,-7.179218,-9.656509,-2.654722,1.293549,-0.094793,-9.367144,4.333620,9.447399,-7.167444,8.205818,-9.836942,-1.765724,5.182966,6.264166,-4.323853,-3.757460,-6.203506,-4.458221,-1.014487,-5.300083,-3.507848,-3.109438,7.446615,-4.674611,-9.693503,-6.978036,3.438710,6.553158,-0.659982,-5.957030,9.298323,6.804086,5.539188,-0.400230,4.201457,0.268123,-6.191686,-5.083255,0.836068,3.750194,-4.445552,1.690114,3.823212,-7.423258,5.587339,-4.490775,8.728736,-5.766581,-8.023143,-8.270912,2.441910,0.827292,3.593029,9.588778,0.501285,8.286427,-1.843008,1.612405,0.327972,-1.002144,-2.315570,8.081621,-3.150331,8.533255,-1.710913,8.496406,8.535471,6.218889,-1.549571,4.937426,-1.414013,9.109112,2.156149,-4.583519,9.910692,-7.774717,6.514585,9.136632,8.801146,-3.087863,7.756075,-6.964322,1.476948,2.311247,-4.911399,4.552264,4.052297,-7.284427,8.148927,6.380724,5.390733,3.286676,5.700787,-1.339264,0.393756,3.762336,-8.775130,7.667017,6.311788,8.009131,6.673698,-2.141282,-1.387024,-3.518990,9.365856,-3.851793,4.593527,-7.244688,-0.793754,4.326894,7.468447,-3.956285,-3.895606,8.972517,7.481223,-0.337865,4.332787,1.514390,0.662346,-3.189281,-4.013667,7.373631,-7.077137,-3.521990,-1.647587,-1.308078,-2.256153,-5.004917,-8.924288,7.991504,-2.698822,-8.867020,-0.218039,9.202801,6.034954,4.751852,-4.405732,7.218536,-2.668771,-6.778298,-5.751361,-3.053827,3.676575,7.914406,7.187878,3.068735,-9.465335,9.032285,-1.241541,-0.558692,-7.687738,4.636316,-7.217820,0.569603,-0.205814,-4.699966,-8.612577,-0.856261,0.857452,8.173541,-5.759063,-5.529653,7.583811,1.625605,1.593744,1.066131,6.620716,-2.212170,-2.889850,-3.181554,3.207995,4.063952,-0.269624,-2.463827,9.233298,-0.386560,-2.059032,8.521390,-1.126602,8.439542,-0.809470,-9.193150,5.606503,-5.655410,-8.492790,7.184209,3.861585,-3.414751,-1.803206,8.557953,-1.795781,8.787425,-0.342222,-0.868482,4.349595,-6.988037,5.655391,-3.971683,-6.632007,-0.324378,1.922466,-2.531121,-1.012235,-7.753314,6.488427,-3.089591,0.851096,1.432859,-5.503746,4.382362,2.576878,-9.901100,-2.909592,-8.777492,0.230605,8.207197,-8.244804,1.554464,-0.247684,4.743049,3.952401,-2.138888,2.423920,-6.906418,0.501364,0.734938,-7.238587,2.129373,-9.259419,0.375946,-5.293286,2.935047,-9.371493,9.729412,-9.253045,3.992186,0.061595,4.411959,1.448518,-3.600596,7.635980,2.378992,5.938661,-0.736828,-8.862163,4.246652,-6.171050,9.836764,4.157768,-3.626113,5.376023,6.243982,2.771851,7.781424,7.108850,8.474209,-7.717475,-9.048588,-8.177013,8.401114,-1.996548,0.724555,7.719152,5.889026,-1.113160,9.057785,0.486853,-6.654343,4.588022,0.364002,3.604351,4.306786,-7.606114,-4.752602,-5.762067,3.978623,-2.756344,3.046401,-5.402766,0.165636,-4.749464,-2.864101,1.943870,-6.242894,5.605397,9.041560,0.679846,-3.522511,-1.280335,-0.617770,-9.517330,6.457783,-5.543468,5.160726,-5.661024,5.682465,9.360123,-1.284166,-6.081724,4.837295,5.918913,1.162005,6.957600,-4.413047,-5.481902,-0.693068,-5.627320,5.628260,-6.192438,0.951236,2.749632,-6.352035,8.151111,-9.163012,4.966955,6.252642,-4.659449,8.648270,-9.703035,-4.993101,-4.925423,9.497218,-2.725311,-9.936354,1.060550,7.920173,-8.247181,0.923722,9.212453,-0.300071,7.079136,9.216219,-5.249784,3.974463,-5.907731,5.483908,-4.858027,2.150828,4.449005,-7.702291,-1.385058,-6.569498,9.959391,-2.197686,5.342188,4.413820,-5.935163,-4.431330,-6.061772,1.127636,5.596471,0.184356,5.258738,8.925436,-8.508889,-3.693753,9.936042,-5.523357,-0.798495,8.141199,0.957593,7.393315,5.747905,-7.414319,9.959887,-3.155727,-0.190513,7.397027,3.394645,-7.742611,-0.764150,-6.182703,2.137988,-6.969508,3.946707], dtype = "float64")#candidate|9287|(384,)|const|float64
call_9286 = relay.TupleGetItem(func_4318_call(relay.reshape(const_9287.astype('float64'), [16, 12, 2])), 0)
call_9288 = relay.TupleGetItem(func_4321_call(relay.reshape(const_9287.astype('float64'), [16, 12, 2])), 0)
output = relay.Tuple([call_9280,call_9286,const_9287,])
output2 = relay.Tuple([call_9281,call_9288,const_9287,])
func_9293 = relay.Function([], output)
mod['func_9293'] = func_9293
mod = relay.transform.InferType()(mod)
output = func_9293()
func_9294 = relay.Function([], output)
mutated_mod['func_9294'] = func_9294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7405_call = mod.get_global_var('func_7405')
func_7407_call = mutated_mod.get_global_var('func_7407')
call_9310 = relay.TupleGetItem(func_7405_call(), 1)
call_9311 = relay.TupleGetItem(func_7407_call(), 1)
output = relay.Tuple([call_9310,])
output2 = relay.Tuple([call_9311,])
func_9312 = relay.Function([], output)
mod['func_9312'] = func_9312
mod = relay.transform.InferType()(mod)
mutated_mod['func_9312'] = func_9312
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9312_call = mutated_mod.get_global_var('func_9312')
call_9313 = func_9312_call()
output = call_9313
func_9314 = relay.Function([], output)
mutated_mod['func_9314'] = func_9314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6193_call = mod.get_global_var('func_6193')
func_6195_call = mutated_mod.get_global_var('func_6195')
call_9330 = func_6193_call()
call_9331 = func_6193_call()
func_8253_call = mod.get_global_var('func_8253')
func_8255_call = mutated_mod.get_global_var('func_8255')
call_9344 = relay.TupleGetItem(func_8253_call(), 0)
call_9345 = relay.TupleGetItem(func_8255_call(), 0)
uop_9350 = relay.exp(call_9330.astype('float32')) # shape=(9, 13, 11)
uop_9352 = relay.exp(call_9331.astype('float32')) # shape=(9, 13, 11)
func_8601_call = mod.get_global_var('func_8601')
func_8603_call = mutated_mod.get_global_var('func_8603')
call_9357 = relay.TupleGetItem(func_8601_call(), 2)
call_9358 = relay.TupleGetItem(func_8603_call(), 2)
output = relay.Tuple([call_9344,uop_9350,call_9357,])
output2 = relay.Tuple([call_9345,uop_9352,call_9358,])
func_9370 = relay.Function([], output)
mod['func_9370'] = func_9370
mod = relay.transform.InferType()(mod)
output = func_9370()
func_9371 = relay.Function([], output)
mutated_mod['func_9371'] = func_9371
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4336_call = mod.get_global_var('func_4336')
func_4338_call = mutated_mod.get_global_var('func_4338')
call_9426 = relay.TupleGetItem(func_4336_call(), 0)
call_9427 = relay.TupleGetItem(func_4338_call(), 0)
output = relay.Tuple([call_9426,])
output2 = relay.Tuple([call_9427,])
func_9445 = relay.Function([], output)
mod['func_9445'] = func_9445
mod = relay.transform.InferType()(mod)
mutated_mod['func_9445'] = func_9445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9445_call = mutated_mod.get_global_var('func_9445')
call_9446 = func_9445_call()
output = call_9446
func_9447 = relay.Function([], output)
mutated_mod['func_9447'] = func_9447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1202_call = mod.get_global_var('func_1202')
func_1203_call = mutated_mod.get_global_var('func_1203')
call_9457 = relay.TupleGetItem(func_1202_call(), 0)
call_9458 = relay.TupleGetItem(func_1203_call(), 0)
output = relay.Tuple([call_9457,])
output2 = relay.Tuple([call_9458,])
func_9466 = relay.Function([], output)
mod['func_9466'] = func_9466
mod = relay.transform.InferType()(mod)
output = func_9466()
func_9467 = relay.Function([], output)
mutated_mod['func_9467'] = func_9467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7835_call = mod.get_global_var('func_7835')
func_7837_call = mutated_mod.get_global_var('func_7837')
call_9545 = relay.TupleGetItem(func_7835_call(), 0)
call_9546 = relay.TupleGetItem(func_7837_call(), 0)
output = call_9545
output2 = call_9546
func_9558 = relay.Function([], output)
mod['func_9558'] = func_9558
mod = relay.transform.InferType()(mod)
mutated_mod['func_9558'] = func_9558
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9558_call = mutated_mod.get_global_var('func_9558')
call_9559 = func_9558_call()
output = call_9559
func_9560 = relay.Function([], output)
mutated_mod['func_9560'] = func_9560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7292_call = mod.get_global_var('func_7292')
func_7294_call = mutated_mod.get_global_var('func_7294')
call_9561 = func_7292_call()
call_9562 = func_7292_call()
output = relay.Tuple([call_9561,])
output2 = relay.Tuple([call_9562,])
func_9568 = relay.Function([], output)
mod['func_9568'] = func_9568
mod = relay.transform.InferType()(mod)
mutated_mod['func_9568'] = func_9568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9568_call = mutated_mod.get_global_var('func_9568')
call_9569 = func_9568_call()
output = call_9569
func_9570 = relay.Function([], output)
mutated_mod['func_9570'] = func_9570
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9445_call = mod.get_global_var('func_9445')
func_9447_call = mutated_mod.get_global_var('func_9447')
call_9614 = relay.TupleGetItem(func_9445_call(), 0)
call_9615 = relay.TupleGetItem(func_9447_call(), 0)
output = call_9614
output2 = call_9615
func_9616 = relay.Function([], output)
mod['func_9616'] = func_9616
mod = relay.transform.InferType()(mod)
output = func_9616()
func_9617 = relay.Function([], output)
mutated_mod['func_9617'] = func_9617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1592_call = mod.get_global_var('func_1592')
func_1594_call = mutated_mod.get_global_var('func_1594')
call_9678 = relay.TupleGetItem(func_1592_call(), 0)
call_9679 = relay.TupleGetItem(func_1594_call(), 0)
output = relay.Tuple([call_9678,])
output2 = relay.Tuple([call_9679,])
func_9688 = relay.Function([], output)
mod['func_9688'] = func_9688
mod = relay.transform.InferType()(mod)
mutated_mod['func_9688'] = func_9688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9688_call = mutated_mod.get_global_var('func_9688')
call_9689 = func_9688_call()
output = call_9689
func_9690 = relay.Function([], output)
mutated_mod['func_9690'] = func_9690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7975_call = mod.get_global_var('func_7975')
func_7977_call = mutated_mod.get_global_var('func_7977')
call_9771 = relay.TupleGetItem(func_7975_call(), 0)
call_9772 = relay.TupleGetItem(func_7977_call(), 0)
output = call_9771
output2 = call_9772
func_9780 = relay.Function([], output)
mod['func_9780'] = func_9780
mod = relay.transform.InferType()(mod)
mutated_mod['func_9780'] = func_9780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9780_call = mutated_mod.get_global_var('func_9780')
call_9781 = func_9780_call()
output = call_9781
func_9782 = relay.Function([], output)
mutated_mod['func_9782'] = func_9782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2920_call = mod.get_global_var('func_2920')
func_2922_call = mutated_mod.get_global_var('func_2922')
call_9802 = relay.TupleGetItem(func_2920_call(), 0)
call_9803 = relay.TupleGetItem(func_2922_call(), 0)
output = call_9802
output2 = call_9803
func_9818 = relay.Function([], output)
mod['func_9818'] = func_9818
mod = relay.transform.InferType()(mod)
mutated_mod['func_9818'] = func_9818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9818_call = mutated_mod.get_global_var('func_9818')
call_9819 = func_9818_call()
output = call_9819
func_9820 = relay.Function([], output)
mutated_mod['func_9820'] = func_9820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1360_call = mod.get_global_var('func_1360')
func_1361_call = mutated_mod.get_global_var('func_1361')
call_9864 = relay.TupleGetItem(func_1360_call(), 0)
call_9865 = relay.TupleGetItem(func_1361_call(), 0)
output = call_9864
output2 = call_9865
func_9880 = relay.Function([], output)
mod['func_9880'] = func_9880
mod = relay.transform.InferType()(mod)
output = func_9880()
func_9881 = relay.Function([], output)
mutated_mod['func_9881'] = func_9881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5026_call = mod.get_global_var('func_5026')
func_5028_call = mutated_mod.get_global_var('func_5028')
call_9938 = relay.TupleGetItem(func_5026_call(), 0)
call_9939 = relay.TupleGetItem(func_5028_call(), 0)
func_7405_call = mod.get_global_var('func_7405')
func_7407_call = mutated_mod.get_global_var('func_7407')
call_9968 = relay.TupleGetItem(func_7405_call(), 2)
call_9969 = relay.TupleGetItem(func_7407_call(), 2)
output = relay.Tuple([call_9938,call_9968,])
output2 = relay.Tuple([call_9939,call_9969,])
func_9974 = relay.Function([], output)
mod['func_9974'] = func_9974
mod = relay.transform.InferType()(mod)
output = func_9974()
func_9975 = relay.Function([], output)
mutated_mod['func_9975'] = func_9975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7791_call = mod.get_global_var('func_7791')
func_7792_call = mutated_mod.get_global_var('func_7792')
call_10063 = func_7791_call()
call_10064 = func_7791_call()
output = call_10063
output2 = call_10064
func_10068 = relay.Function([], output)
mod['func_10068'] = func_10068
mod = relay.transform.InferType()(mod)
mutated_mod['func_10068'] = func_10068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10068_call = mutated_mod.get_global_var('func_10068')
call_10069 = func_10068_call()
output = call_10069
func_10070 = relay.Function([], output)
mutated_mod['func_10070'] = func_10070
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4128_call = mod.get_global_var('func_4128')
func_4129_call = mutated_mod.get_global_var('func_4129')
call_10173 = relay.TupleGetItem(func_4128_call(), 1)
call_10174 = relay.TupleGetItem(func_4129_call(), 1)
output = call_10173
output2 = call_10174
func_10192 = relay.Function([], output)
mod['func_10192'] = func_10192
mod = relay.transform.InferType()(mod)
output = func_10192()
func_10193 = relay.Function([], output)
mutated_mod['func_10193'] = func_10193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_585_call = mod.get_global_var('func_585')
func_586_call = mutated_mod.get_global_var('func_586')
call_10196 = relay.TupleGetItem(func_585_call(), 1)
call_10197 = relay.TupleGetItem(func_586_call(), 1)
output = call_10196
output2 = call_10197
func_10206 = relay.Function([], output)
mod['func_10206'] = func_10206
mod = relay.transform.InferType()(mod)
output = func_10206()
func_10207 = relay.Function([], output)
mutated_mod['func_10207'] = func_10207
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7292_call = mod.get_global_var('func_7292')
func_7294_call = mutated_mod.get_global_var('func_7294')
call_10224 = func_7292_call()
call_10225 = func_7292_call()
output = relay.Tuple([call_10224,])
output2 = relay.Tuple([call_10225,])
func_10231 = relay.Function([], output)
mod['func_10231'] = func_10231
mod = relay.transform.InferType()(mod)
output = func_10231()
func_10232 = relay.Function([], output)
mutated_mod['func_10232'] = func_10232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2683_call = mod.get_global_var('func_2683')
func_2685_call = mutated_mod.get_global_var('func_2685')
call_10321 = func_2683_call()
call_10322 = func_2683_call()
func_7602_call = mod.get_global_var('func_7602')
func_7604_call = mutated_mod.get_global_var('func_7604')
call_10331 = func_7602_call()
call_10332 = func_7602_call()
func_2920_call = mod.get_global_var('func_2920')
func_2922_call = mutated_mod.get_global_var('func_2922')
call_10339 = relay.TupleGetItem(func_2920_call(), 1)
call_10340 = relay.TupleGetItem(func_2922_call(), 1)
func_3356_call = mod.get_global_var('func_3356')
func_3357_call = mutated_mod.get_global_var('func_3357')
call_10343 = func_3356_call()
call_10344 = func_3356_call()
func_10231_call = mod.get_global_var('func_10231')
func_10232_call = mutated_mod.get_global_var('func_10232')
call_10346 = relay.TupleGetItem(func_10231_call(), 0)
call_10347 = relay.TupleGetItem(func_10232_call(), 0)
output = relay.Tuple([call_10321,call_10331,call_10339,call_10343,call_10346,])
output2 = relay.Tuple([call_10322,call_10332,call_10340,call_10344,call_10347,])
func_10355 = relay.Function([], output)
mod['func_10355'] = func_10355
mod = relay.transform.InferType()(mod)
output = func_10355()
func_10356 = relay.Function([], output)
mutated_mod['func_10356'] = func_10356
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8601_call = mod.get_global_var('func_8601')
func_8603_call = mutated_mod.get_global_var('func_8603')
call_10359 = relay.TupleGetItem(func_8601_call(), 4)
call_10360 = relay.TupleGetItem(func_8603_call(), 4)
var_10361 = relay.var("var_10361", dtype = "float32", shape = (10, 12, 2))#candidate|10361|(10, 12, 2)|var|float32
bop_10362 = relay.equal(call_10359.astype('bool'), var_10361.astype('bool')) # shape=(10, 12, 2)
bop_10365 = relay.equal(call_10360.astype('bool'), var_10361.astype('bool')) # shape=(10, 12, 2)
output = bop_10362
output2 = bop_10365
func_10372 = relay.Function([var_10361,], output)
mod['func_10372'] = func_10372
mod = relay.transform.InferType()(mod)
var_10373 = relay.var("var_10373", dtype = "float32", shape = (10, 12, 2))#candidate|10373|(10, 12, 2)|var|float32
output = func_10372(var_10373)
func_10374 = relay.Function([var_10373], output)
mutated_mod['func_10374'] = func_10374
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6789_call = mod.get_global_var('func_6789')
func_6791_call = mutated_mod.get_global_var('func_6791')
call_10380 = func_6789_call()
call_10381 = func_6789_call()
output = call_10380
output2 = call_10381
func_10397 = relay.Function([], output)
mod['func_10397'] = func_10397
mod = relay.transform.InferType()(mod)
mutated_mod['func_10397'] = func_10397
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10397_call = mutated_mod.get_global_var('func_10397')
call_10398 = func_10397_call()
output = call_10398
func_10399 = relay.Function([], output)
mutated_mod['func_10399'] = func_10399
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8536_call = mod.get_global_var('func_8536')
func_8538_call = mutated_mod.get_global_var('func_8538')
call_10422 = relay.TupleGetItem(func_8536_call(), 0)
call_10423 = relay.TupleGetItem(func_8538_call(), 0)
var_10424 = relay.var("var_10424", dtype = "float64", shape = (12, 12, 2))#candidate|10424|(12, 12, 2)|var|float64
bop_10425 = relay.divide(call_10422.astype('float32'), var_10424.astype('float32')) # shape=(12, 12, 2)
bop_10428 = relay.divide(call_10423.astype('float32'), var_10424.astype('float32')) # shape=(12, 12, 2)
output = relay.Tuple([bop_10425,])
output2 = relay.Tuple([bop_10428,])
func_10432 = relay.Function([var_10424,], output)
mod['func_10432'] = func_10432
mod = relay.transform.InferType()(mod)
mutated_mod['func_10432'] = func_10432
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10433 = relay.var("var_10433", dtype = "float64", shape = (12, 12, 2))#candidate|10433|(12, 12, 2)|var|float64
func_10432_call = mutated_mod.get_global_var('func_10432')
call_10434 = func_10432_call(var_10433)
output = call_10434
func_10435 = relay.Function([var_10433], output)
mutated_mod['func_10435'] = func_10435
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7723_call = mod.get_global_var('func_7723')
func_7725_call = mutated_mod.get_global_var('func_7725')
call_10524 = relay.TupleGetItem(func_7723_call(), 0)
call_10525 = relay.TupleGetItem(func_7725_call(), 0)
func_10355_call = mod.get_global_var('func_10355')
func_10356_call = mutated_mod.get_global_var('func_10356')
call_10550 = relay.TupleGetItem(func_10355_call(), 3)
call_10551 = relay.TupleGetItem(func_10356_call(), 3)
output = relay.Tuple([call_10524,call_10550,])
output2 = relay.Tuple([call_10525,call_10551,])
func_10553 = relay.Function([], output)
mod['func_10553'] = func_10553
mod = relay.transform.InferType()(mod)
mutated_mod['func_10553'] = func_10553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10553_call = mutated_mod.get_global_var('func_10553')
call_10554 = func_10553_call()
output = call_10554
func_10555 = relay.Function([], output)
mutated_mod['func_10555'] = func_10555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6133_call = mod.get_global_var('func_6133')
func_6134_call = mutated_mod.get_global_var('func_6134')
call_10569 = relay.TupleGetItem(func_6133_call(), 0)
call_10570 = relay.TupleGetItem(func_6134_call(), 0)
func_6322_call = mod.get_global_var('func_6322')
func_6326_call = mutated_mod.get_global_var('func_6326')
const_10580 = relay.const([[-1],[1],[4],[10],[-2],[3],[-5],[1],[-7],[-4],[-8],[-10],[-6],[10],[2],[1],[5],[-1],[-7],[7],[5],[7],[7],[8],[6],[8],[4],[-4],[10],[-4],[-10],[-8],[-5],[3],[10],[-3],[2],[-5],[-9],[-4],[4],[10],[9],[10],[-8],[4],[7],[2]], dtype = "uint64")#candidate|10580|(48, 1)|const|uint64
var_10581 = relay.var("var_10581", dtype = "float64", shape = (384, 1))#candidate|10581|(384, 1)|var|float64
call_10579 = relay.TupleGetItem(func_6322_call(relay.reshape(const_10580.astype('uint64'), [2, 12, 2]), relay.reshape(var_10581.astype('float64'), [16, 12, 2]), ), 0)
call_10582 = relay.TupleGetItem(func_6326_call(relay.reshape(const_10580.astype('uint64'), [2, 12, 2]), relay.reshape(var_10581.astype('float64'), [16, 12, 2]), ), 0)
output = relay.Tuple([call_10569,call_10579,const_10580,var_10581,])
output2 = relay.Tuple([call_10570,call_10582,const_10580,var_10581,])
func_10585 = relay.Function([var_10581,], output)
mod['func_10585'] = func_10585
mod = relay.transform.InferType()(mod)
var_10586 = relay.var("var_10586", dtype = "float64", shape = (384, 1))#candidate|10586|(384, 1)|var|float64
output = func_10585(var_10586)
func_10587 = relay.Function([var_10586], output)
mutated_mod['func_10587'] = func_10587
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6831_call = mod.get_global_var('func_6831')
func_6833_call = mutated_mod.get_global_var('func_6833')
call_10596 = relay.TupleGetItem(func_6831_call(), 1)
call_10597 = relay.TupleGetItem(func_6833_call(), 1)
output = call_10596
output2 = call_10597
func_10601 = relay.Function([], output)
mod['func_10601'] = func_10601
mod = relay.transform.InferType()(mod)
output = func_10601()
func_10602 = relay.Function([], output)
mutated_mod['func_10602'] = func_10602
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10723 = relay.var("var_10723", dtype = "float32", shape = (5, 14, 2))#candidate|10723|(5, 14, 2)|var|float32
uop_10724 = relay.sqrt(var_10723.astype('float32')) # shape=(5, 14, 2)
output = relay.Tuple([uop_10724,])
output2 = relay.Tuple([uop_10724,])
func_10730 = relay.Function([var_10723,], output)
mod['func_10730'] = func_10730
mod = relay.transform.InferType()(mod)
var_10731 = relay.var("var_10731", dtype = "float32", shape = (5, 14, 2))#candidate|10731|(5, 14, 2)|var|float32
output = func_10730(var_10731)
func_10732 = relay.Function([var_10731], output)
mutated_mod['func_10732'] = func_10732
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3419_call = mod.get_global_var('func_3419')
func_3420_call = mutated_mod.get_global_var('func_3420')
call_10742 = relay.TupleGetItem(func_3419_call(), 0)
call_10743 = relay.TupleGetItem(func_3420_call(), 0)
func_8536_call = mod.get_global_var('func_8536')
func_8538_call = mutated_mod.get_global_var('func_8538')
call_10748 = relay.TupleGetItem(func_8536_call(), 1)
call_10749 = relay.TupleGetItem(func_8538_call(), 1)
output = relay.Tuple([call_10742,call_10748,])
output2 = relay.Tuple([call_10743,call_10749,])
func_10763 = relay.Function([], output)
mod['func_10763'] = func_10763
mod = relay.transform.InferType()(mod)
output = func_10763()
func_10764 = relay.Function([], output)
mutated_mod['func_10764'] = func_10764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9293_call = mod.get_global_var('func_9293')
func_9294_call = mutated_mod.get_global_var('func_9294')
call_10852 = relay.TupleGetItem(func_9293_call(), 0)
call_10853 = relay.TupleGetItem(func_9294_call(), 0)
func_1537_call = mod.get_global_var('func_1537')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_10859 = relay.TupleGetItem(func_1537_call(), 0)
call_10860 = relay.TupleGetItem(func_1539_call(), 0)
func_5356_call = mod.get_global_var('func_5356')
func_5357_call = mutated_mod.get_global_var('func_5357')
call_10894 = relay.TupleGetItem(func_5356_call(), 1)
call_10895 = relay.TupleGetItem(func_5357_call(), 1)
func_8032_call = mod.get_global_var('func_8032')
func_8036_call = mutated_mod.get_global_var('func_8036')
var_10920 = relay.var("var_10920", dtype = "int32", shape = (700,))#candidate|10920|(700,)|var|int32
call_10919 = relay.TupleGetItem(func_8032_call(relay.reshape(var_10920.astype('int32'), [5, 10, 14]), relay.reshape(var_10920.astype('int32'), [5, 10, 14]), ), 0)
call_10921 = relay.TupleGetItem(func_8036_call(relay.reshape(var_10920.astype('int32'), [5, 10, 14]), relay.reshape(var_10920.astype('int32'), [5, 10, 14]), ), 0)
output = relay.Tuple([call_10852,call_10859,call_10894,call_10919,var_10920,])
output2 = relay.Tuple([call_10853,call_10860,call_10895,call_10921,var_10920,])
func_10935 = relay.Function([var_10920,], output)
mod['func_10935'] = func_10935
mod = relay.transform.InferType()(mod)
mutated_mod['func_10935'] = func_10935
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10936 = relay.var("var_10936", dtype = "int32", shape = (700,))#candidate|10936|(700,)|var|int32
func_10935_call = mutated_mod.get_global_var('func_10935')
call_10937 = func_10935_call(var_10936)
output = call_10937
func_10938 = relay.Function([var_10936], output)
mutated_mod['func_10938'] = func_10938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8871_call = mod.get_global_var('func_8871')
func_8873_call = mutated_mod.get_global_var('func_8873')
call_10959 = relay.TupleGetItem(func_8871_call(), 0)
call_10960 = relay.TupleGetItem(func_8873_call(), 0)
output = call_10959
output2 = call_10960
func_10961 = relay.Function([], output)
mod['func_10961'] = func_10961
mod = relay.transform.InferType()(mod)
output = func_10961()
func_10962 = relay.Function([], output)
mutated_mod['func_10962'] = func_10962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4756_call = mod.get_global_var('func_4756')
func_4758_call = mutated_mod.get_global_var('func_4758')
call_10992 = func_4756_call()
call_10993 = func_4756_call()
func_8908_call = mod.get_global_var('func_8908')
func_8909_call = mutated_mod.get_global_var('func_8909')
call_11015 = relay.TupleGetItem(func_8908_call(), 0)
call_11016 = relay.TupleGetItem(func_8909_call(), 0)
func_5051_call = mod.get_global_var('func_5051')
func_5052_call = mutated_mod.get_global_var('func_5052')
call_11022 = func_5051_call()
call_11023 = func_5051_call()
output = relay.Tuple([call_10992,call_11015,call_11022,])
output2 = relay.Tuple([call_10993,call_11016,call_11023,])
func_11029 = relay.Function([], output)
mod['func_11029'] = func_11029
mod = relay.transform.InferType()(mod)
output = func_11029()
func_11030 = relay.Function([], output)
mutated_mod['func_11030'] = func_11030
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2882_call = mod.get_global_var('func_2882')
func_2883_call = mutated_mod.get_global_var('func_2883')
call_11077 = relay.TupleGetItem(func_2882_call(), 0)
call_11078 = relay.TupleGetItem(func_2883_call(), 0)
output = relay.Tuple([call_11077,])
output2 = relay.Tuple([call_11078,])
func_11079 = relay.Function([], output)
mod['func_11079'] = func_11079
mod = relay.transform.InferType()(mod)
mutated_mod['func_11079'] = func_11079
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11079_call = mutated_mod.get_global_var('func_11079')
call_11080 = func_11079_call()
output = call_11080
func_11081 = relay.Function([], output)
mutated_mod['func_11081'] = func_11081
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1285_call = mod.get_global_var('func_1285')
func_1287_call = mutated_mod.get_global_var('func_1287')
call_11084 = func_1285_call()
call_11085 = func_1285_call()
output = relay.Tuple([call_11084,])
output2 = relay.Tuple([call_11085,])
func_11091 = relay.Function([], output)
mod['func_11091'] = func_11091
mod = relay.transform.InferType()(mod)
mutated_mod['func_11091'] = func_11091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11091_call = mutated_mod.get_global_var('func_11091')
call_11092 = func_11091_call()
output = call_11092
func_11093 = relay.Function([], output)
mutated_mod['func_11093'] = func_11093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_517_call = mod.get_global_var('func_517')
func_518_call = mutated_mod.get_global_var('func_518')
call_11138 = func_517_call()
call_11139 = func_517_call()
func_2135_call = mod.get_global_var('func_2135')
func_2138_call = mutated_mod.get_global_var('func_2138')
var_11161 = relay.var("var_11161", dtype = "float64", shape = (72,))#candidate|11161|(72,)|var|float64
call_11160 = relay.TupleGetItem(func_2135_call(relay.reshape(var_11161.astype('float64'), [1, 72])), 0)
call_11162 = relay.TupleGetItem(func_2138_call(relay.reshape(var_11161.astype('float64'), [1, 72])), 0)
func_4904_call = mod.get_global_var('func_4904')
func_4905_call = mutated_mod.get_global_var('func_4905')
call_11168 = relay.TupleGetItem(func_4904_call(), 1)
call_11169 = relay.TupleGetItem(func_4905_call(), 1)
func_9445_call = mod.get_global_var('func_9445')
func_9447_call = mutated_mod.get_global_var('func_9447')
call_11173 = relay.TupleGetItem(func_9445_call(), 0)
call_11174 = relay.TupleGetItem(func_9447_call(), 0)
output = relay.Tuple([call_11138,call_11160,var_11161,call_11168,call_11173,])
output2 = relay.Tuple([call_11139,call_11162,var_11161,call_11169,call_11174,])
func_11176 = relay.Function([var_11161,], output)
mod['func_11176'] = func_11176
mod = relay.transform.InferType()(mod)
mutated_mod['func_11176'] = func_11176
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11177 = relay.var("var_11177", dtype = "float64", shape = (72,))#candidate|11177|(72,)|var|float64
func_11176_call = mutated_mod.get_global_var('func_11176')
call_11178 = func_11176_call(var_11177)
output = call_11178
func_11179 = relay.Function([var_11177], output)
mutated_mod['func_11179'] = func_11179
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10961_call = mod.get_global_var('func_10961')
func_10962_call = mutated_mod.get_global_var('func_10962')
call_11272 = func_10961_call()
call_11273 = func_10961_call()
output = call_11272
output2 = call_11273
func_11276 = relay.Function([], output)
mod['func_11276'] = func_11276
mod = relay.transform.InferType()(mod)
output = func_11276()
func_11277 = relay.Function([], output)
mutated_mod['func_11277'] = func_11277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9370_call = mod.get_global_var('func_9370')
func_9371_call = mutated_mod.get_global_var('func_9371')
call_11297 = relay.TupleGetItem(func_9370_call(), 1)
call_11298 = relay.TupleGetItem(func_9371_call(), 1)
func_8193_call = mod.get_global_var('func_8193')
func_8195_call = mutated_mod.get_global_var('func_8195')
call_11312 = relay.TupleGetItem(func_8193_call(), 0)
call_11313 = relay.TupleGetItem(func_8195_call(), 0)
func_10397_call = mod.get_global_var('func_10397')
func_10399_call = mutated_mod.get_global_var('func_10399')
call_11332 = func_10397_call()
call_11333 = func_10397_call()
func_10553_call = mod.get_global_var('func_10553')
func_10555_call = mutated_mod.get_global_var('func_10555')
call_11348 = relay.TupleGetItem(func_10553_call(), 1)
call_11349 = relay.TupleGetItem(func_10555_call(), 1)
output = relay.Tuple([call_11297,call_11312,call_11332,call_11348,])
output2 = relay.Tuple([call_11298,call_11313,call_11333,call_11349,])
func_11354 = relay.Function([], output)
mod['func_11354'] = func_11354
mod = relay.transform.InferType()(mod)
mutated_mod['func_11354'] = func_11354
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11354_call = mutated_mod.get_global_var('func_11354')
call_11355 = func_11354_call()
output = call_11355
func_11356 = relay.Function([], output)
mutated_mod['func_11356'] = func_11356
mutated_mod = relay.transform.InferType()(mutated_mod)
const_11445 = relay.const([[[-3.509647,-2.275835,7.425271,-9.094801,6.532308,-2.018788,-9.564842,9.329445,8.056954,5.561243],[-8.732756,1.010766,-5.725151,2.304698,-3.462946,-6.675019,-8.910464,-6.990584,-1.828944,-0.247640],[-8.733555,-7.755928,8.172984,8.400662,5.560390,-1.373880,-8.562960,9.053104,2.131633,4.737407],[5.114763,1.797995,-1.547764,3.381589,-7.611458,-8.282847,-0.918158,5.370384,-7.334782,-2.875895]],[[0.344529,2.098187,1.801519,-3.459450,9.249255,-1.925342,-5.156194,-3.243508,8.770779,5.602625],[-9.331711,9.205301,8.814911,-2.878798,9.383977,3.848680,9.577102,-3.312330,9.765120,-0.617139],[-0.583473,6.901722,-4.932349,5.150471,1.346014,8.385521,-8.382534,-4.968599,2.481984,0.544364],[0.347653,8.256077,8.756773,8.450298,-7.100352,9.855830,-7.542391,8.074491,-3.117268,5.079390]],[[-7.669176,3.264544,1.100179,-7.363595,0.470966,9.042647,-3.039548,0.178694,-5.527240,-6.139991],[-8.131451,1.494046,-3.903167,0.525273,8.041505,-9.916897,7.150741,-6.026833,8.828820,2.448336],[-2.284005,4.562310,7.717582,-4.329353,-3.903954,5.226169,-1.757689,8.726380,0.108797,8.943573],[1.064054,-1.771099,-6.078111,4.213696,4.537864,-6.354178,1.030416,-2.240943,-8.220847,-7.505624]],[[1.521437,-9.542217,-3.100954,-6.858634,-0.942489,-7.078040,0.684921,6.069011,7.958484,3.306267],[0.812189,-7.315419,-0.707157,-6.409290,8.780162,1.075331,-2.348527,-8.381287,3.267809,-5.976823],[2.325937,-3.053680,-6.640312,-8.083228,-5.268793,-7.230321,3.596753,1.833607,-3.299025,-4.304518],[-2.615127,-7.495560,9.634483,-2.009026,-6.622310,6.101419,9.540148,-0.881352,7.996576,-5.023270]],[[5.746898,3.907244,3.721462,-0.379642,-2.986816,-6.343325,-1.522877,5.473861,9.135777,-7.443877],[5.573677,2.044314,2.961004,-4.799743,-2.881406,1.014953,0.249036,-0.003069,4.510789,-4.608728],[-0.197601,-0.715852,-1.859700,-1.978964,4.304787,9.320189,-1.752569,-5.876981,-5.080478,-0.611662],[1.120990,-1.443959,6.713428,6.165306,6.185628,-6.583829,-7.185830,-6.457155,1.026703,7.620197]]], dtype = "float64")#candidate|11445|(5, 4, 10)|const|float64
uop_11446 = relay.cos(const_11445.astype('float64')) # shape=(5, 4, 10)
output = uop_11446
output2 = uop_11446
func_11451 = relay.Function([], output)
mod['func_11451'] = func_11451
mod = relay.transform.InferType()(mod)
output = func_11451()
func_11452 = relay.Function([], output)
mutated_mod['func_11452'] = func_11452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11029_call = mod.get_global_var('func_11029')
func_11030_call = mutated_mod.get_global_var('func_11030')
call_11481 = relay.TupleGetItem(func_11029_call(), 0)
call_11482 = relay.TupleGetItem(func_11030_call(), 0)
func_10961_call = mod.get_global_var('func_10961')
func_10962_call = mutated_mod.get_global_var('func_10962')
call_11487 = func_10961_call()
call_11488 = func_10961_call()
func_8700_call = mod.get_global_var('func_8700')
func_8702_call = mutated_mod.get_global_var('func_8702')
const_11500 = relay.const([-10,7,8,-5,-2,3,-1,-1,-4,-4,5,6,-3,-8,-7,-4,5,6,7,-6,-2,-6,-7,-2,7,5,-3,-8,7,9,-2,4,-4,-1,-2,9,-5,8,3,-10,-4,-4,7,5,7,10,5,-7,4,10,-6,-1,6,-10], dtype = "int8")#candidate|11500|(54,)|const|int8
call_11499 = relay.TupleGetItem(func_8700_call(relay.reshape(const_11500.astype('int8'), [54,])), 0)
call_11501 = relay.TupleGetItem(func_8702_call(relay.reshape(const_11500.astype('int8'), [54,])), 0)
func_2773_call = mod.get_global_var('func_2773')
func_2775_call = mutated_mod.get_global_var('func_2775')
call_11508 = relay.TupleGetItem(func_2773_call(), 0)
call_11509 = relay.TupleGetItem(func_2775_call(), 0)
func_9100_call = mod.get_global_var('func_9100')
func_9102_call = mutated_mod.get_global_var('func_9102')
call_11515 = func_9100_call()
call_11516 = func_9100_call()
func_6624_call = mod.get_global_var('func_6624')
func_6626_call = mutated_mod.get_global_var('func_6626')
var_11545 = relay.var("var_11545", dtype = "float32", shape = (6, 60))#candidate|11545|(6, 60)|var|float32
call_11544 = func_6624_call(relay.reshape(var_11545.astype('float32'), [15, 12, 2]))
call_11546 = func_6624_call(relay.reshape(var_11545.astype('float32'), [15, 12, 2]))
func_8934_call = mod.get_global_var('func_8934')
func_8936_call = mutated_mod.get_global_var('func_8936')
call_11556 = func_8934_call()
call_11557 = func_8934_call()
output = relay.Tuple([call_11481,call_11487,call_11499,const_11500,call_11508,call_11515,call_11544,var_11545,call_11556,])
output2 = relay.Tuple([call_11482,call_11488,call_11501,const_11500,call_11509,call_11516,call_11546,var_11545,call_11557,])
func_11578 = relay.Function([var_11545,], output)
mod['func_11578'] = func_11578
mod = relay.transform.InferType()(mod)
var_11579 = relay.var("var_11579", dtype = "float32", shape = (6, 60))#candidate|11579|(6, 60)|var|float32
output = func_11578(var_11579)
func_11580 = relay.Function([var_11579], output)
mutated_mod['func_11580'] = func_11580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8101_call = mod.get_global_var('func_8101')
func_8102_call = mutated_mod.get_global_var('func_8102')
call_11590 = relay.TupleGetItem(func_8101_call(), 0)
call_11591 = relay.TupleGetItem(func_8102_call(), 0)
output = relay.Tuple([call_11590,])
output2 = relay.Tuple([call_11591,])
func_11633 = relay.Function([], output)
mod['func_11633'] = func_11633
mod = relay.transform.InferType()(mod)
mutated_mod['func_11633'] = func_11633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11633_call = mutated_mod.get_global_var('func_11633')
call_11634 = func_11633_call()
output = call_11634
func_11635 = relay.Function([], output)
mutated_mod['func_11635'] = func_11635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2577_call = mod.get_global_var('func_2577')
func_2578_call = mutated_mod.get_global_var('func_2578')
call_11702 = relay.TupleGetItem(func_2577_call(), 0)
call_11703 = relay.TupleGetItem(func_2578_call(), 0)
func_10763_call = mod.get_global_var('func_10763')
func_10764_call = mutated_mod.get_global_var('func_10764')
call_11704 = relay.TupleGetItem(func_10763_call(), 1)
call_11705 = relay.TupleGetItem(func_10764_call(), 1)
output = relay.Tuple([call_11702,call_11704,])
output2 = relay.Tuple([call_11703,call_11705,])
func_11706 = relay.Function([], output)
mod['func_11706'] = func_11706
mod = relay.transform.InferType()(mod)
output = func_11706()
func_11707 = relay.Function([], output)
mutated_mod['func_11707'] = func_11707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7263_call = mod.get_global_var('func_7263')
func_7265_call = mutated_mod.get_global_var('func_7265')
call_11731 = func_7263_call()
call_11732 = func_7263_call()
func_1592_call = mod.get_global_var('func_1592')
func_1594_call = mutated_mod.get_global_var('func_1594')
call_11743 = relay.TupleGetItem(func_1592_call(), 0)
call_11744 = relay.TupleGetItem(func_1594_call(), 0)
func_5106_call = mod.get_global_var('func_5106')
func_5108_call = mutated_mod.get_global_var('func_5108')
call_11752 = relay.TupleGetItem(func_5106_call(), 1)
call_11753 = relay.TupleGetItem(func_5108_call(), 1)
output = relay.Tuple([call_11731,call_11743,call_11752,])
output2 = relay.Tuple([call_11732,call_11744,call_11753,])
func_11762 = relay.Function([], output)
mod['func_11762'] = func_11762
mod = relay.transform.InferType()(mod)
mutated_mod['func_11762'] = func_11762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11762_call = mutated_mod.get_global_var('func_11762')
call_11763 = func_11762_call()
output = call_11763
func_11764 = relay.Function([], output)
mutated_mod['func_11764'] = func_11764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7723_call = mod.get_global_var('func_7723')
func_7725_call = mutated_mod.get_global_var('func_7725')
call_11765 = relay.TupleGetItem(func_7723_call(), 0)
call_11766 = relay.TupleGetItem(func_7725_call(), 0)
output = call_11765
output2 = call_11766
func_11767 = relay.Function([], output)
mod['func_11767'] = func_11767
mod = relay.transform.InferType()(mod)
mutated_mod['func_11767'] = func_11767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11767_call = mutated_mod.get_global_var('func_11767')
call_11768 = func_11767_call()
output = call_11768
func_11769 = relay.Function([], output)
mutated_mod['func_11769'] = func_11769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3895_call = mod.get_global_var('func_3895')
func_3897_call = mutated_mod.get_global_var('func_3897')
call_11791 = relay.TupleGetItem(func_3895_call(), 0)
call_11792 = relay.TupleGetItem(func_3897_call(), 0)
uop_11809 = relay.exp(call_11791.astype('float32')) # shape=(5, 12, 2)
uop_11811 = relay.exp(call_11792.astype('float32')) # shape=(5, 12, 2)
var_11817 = relay.var("var_11817", dtype = "float32", shape = (5, 12, 2))#candidate|11817|(5, 12, 2)|var|float32
bop_11818 = relay.bitwise_and(uop_11809.astype('int16'), relay.reshape(var_11817.astype('int16'), relay.shape_of(uop_11809))) # shape=(5, 12, 2)
bop_11821 = relay.bitwise_and(uop_11811.astype('int16'), relay.reshape(var_11817.astype('int16'), relay.shape_of(uop_11811))) # shape=(5, 12, 2)
output = bop_11818
output2 = bop_11821
func_11823 = relay.Function([var_11817,], output)
mod['func_11823'] = func_11823
mod = relay.transform.InferType()(mod)
var_11824 = relay.var("var_11824", dtype = "float32", shape = (5, 12, 2))#candidate|11824|(5, 12, 2)|var|float32
output = func_11823(var_11824)
func_11825 = relay.Function([var_11824], output)
mutated_mod['func_11825'] = func_11825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3660_call = mod.get_global_var('func_3660')
func_3662_call = mutated_mod.get_global_var('func_3662')
call_11836 = func_3660_call()
call_11837 = func_3660_call()
func_6133_call = mod.get_global_var('func_6133')
func_6134_call = mutated_mod.get_global_var('func_6134')
call_11838 = relay.TupleGetItem(func_6133_call(), 0)
call_11839 = relay.TupleGetItem(func_6134_call(), 0)
output = relay.Tuple([call_11836,call_11838,])
output2 = relay.Tuple([call_11837,call_11839,])
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
func_9445_call = mod.get_global_var('func_9445')
func_9447_call = mutated_mod.get_global_var('func_9447')
call_11885 = relay.TupleGetItem(func_9445_call(), 0)
call_11886 = relay.TupleGetItem(func_9447_call(), 0)
output = relay.Tuple([call_11885,])
output2 = relay.Tuple([call_11886,])
func_11887 = relay.Function([], output)
mod['func_11887'] = func_11887
mod = relay.transform.InferType()(mod)
output = func_11887()
func_11888 = relay.Function([], output)
mutated_mod['func_11888'] = func_11888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4128_call = mod.get_global_var('func_4128')
func_4129_call = mutated_mod.get_global_var('func_4129')
call_11899 = relay.TupleGetItem(func_4128_call(), 0)
call_11900 = relay.TupleGetItem(func_4129_call(), 0)
func_1537_call = mod.get_global_var('func_1537')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_11903 = relay.TupleGetItem(func_1537_call(), 0)
call_11904 = relay.TupleGetItem(func_1539_call(), 0)
func_8934_call = mod.get_global_var('func_8934')
func_8936_call = mutated_mod.get_global_var('func_8936')
call_11905 = func_8934_call()
call_11906 = func_8934_call()
func_6883_call = mod.get_global_var('func_6883')
func_6885_call = mutated_mod.get_global_var('func_6885')
call_11908 = relay.TupleGetItem(func_6883_call(), 0)
call_11909 = relay.TupleGetItem(func_6885_call(), 0)
output = relay.Tuple([call_11899,call_11903,call_11905,call_11908,])
output2 = relay.Tuple([call_11900,call_11904,call_11906,call_11909,])
func_11916 = relay.Function([], output)
mod['func_11916'] = func_11916
mod = relay.transform.InferType()(mod)
output = func_11916()
func_11917 = relay.Function([], output)
mutated_mod['func_11917'] = func_11917
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9123_call = mod.get_global_var('func_9123')
func_9124_call = mutated_mod.get_global_var('func_9124')
call_11940 = func_9123_call()
call_11941 = func_9123_call()
func_10730_call = mod.get_global_var('func_10730')
func_10732_call = mutated_mod.get_global_var('func_10732')
const_11956 = relay.const([[-4.575554,2.653359,5.352392,3.330875,7.383282,-8.580203,3.990085,-4.910308,5.509919,-6.447794,4.631997,3.140300,-2.044272,3.616523,-6.096086,-9.132163,-8.368679,4.863969,5.084492,8.630850,5.129565,-2.402527,9.277735,2.886143,-5.393928,9.870401,-7.866366,-5.485601,2.229994,7.756334,4.226037,-0.518542,7.325444,2.110955,4.770842,4.328605,-7.527346,8.957274,6.175492,-7.986368,-3.989667,1.314768,3.578195,-3.934474,-1.837548,-5.687787,3.170530,3.572060,-9.373067,0.436933,4.938712,6.860287,-9.035215,2.624840,6.851479,6.454240,2.064841,-0.018608,6.137584,7.282897,6.905359,2.992626,9.816780,1.661218,4.439188,5.682422,-8.810232,-2.078104,6.270468,-4.600179,-6.308206,-2.690247,-9.200992,-3.863669,8.689791,3.961774,3.560529,5.465237,5.827789,-1.857528,5.295312,8.679487,-4.808653,1.421018,3.611215,5.023690,0.611532,5.522210,-4.939520,3.837621,-2.712854,-9.671014,1.652805,-4.525646,8.679997,7.896994,-6.982275,-7.422600,3.486183,-1.274698,9.227357,-7.456370,9.088689,-6.078980,6.294403,-0.034958,9.603831,0.486179,-1.209569,2.330154,-4.580001,7.331649,-1.971380,-7.632459,2.119226,-9.153522,-2.383197,7.780207,7.173620,9.334025,-4.927497,-3.416017,1.654983,-0.232567,8.685774,6.981618,5.762927,-2.735788,-9.095958,4.953212,2.951865,-4.913972,-9.138818,2.026650,7.511290,-7.026514,-4.020323,5.655595,-8.815622,-8.098727]], dtype = "float32")#candidate|11956|(1, 140)|const|float32
call_11955 = relay.TupleGetItem(func_10730_call(relay.reshape(const_11956.astype('float32'), [5, 14, 2])), 0)
call_11957 = relay.TupleGetItem(func_10732_call(relay.reshape(const_11956.astype('float32'), [5, 14, 2])), 0)
output = relay.Tuple([call_11940,call_11955,const_11956,])
output2 = relay.Tuple([call_11941,call_11957,const_11956,])
func_11965 = relay.Function([], output)
mod['func_11965'] = func_11965
mod = relay.transform.InferType()(mod)
output = func_11965()
func_11966 = relay.Function([], output)
mutated_mod['func_11966'] = func_11966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11451_call = mod.get_global_var('func_11451')
func_11452_call = mutated_mod.get_global_var('func_11452')
call_11967 = func_11451_call()
call_11968 = func_11451_call()
output = relay.Tuple([call_11967,])
output2 = relay.Tuple([call_11968,])
func_11969 = relay.Function([], output)
mod['func_11969'] = func_11969
mod = relay.transform.InferType()(mod)
mutated_mod['func_11969'] = func_11969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11969_call = mutated_mod.get_global_var('func_11969')
call_11970 = func_11969_call()
output = call_11970
func_11971 = relay.Function([], output)
mutated_mod['func_11971'] = func_11971
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12067 = relay.var("var_12067", dtype = "float64", shape = (13, 14, 15))#candidate|12067|(13, 14, 15)|var|float64
uop_12068 = relay.log2(var_12067.astype('float64')) # shape=(13, 14, 15)
output = uop_12068
output2 = uop_12068
func_12070 = relay.Function([var_12067,], output)
mod['func_12070'] = func_12070
mod = relay.transform.InferType()(mod)
var_12071 = relay.var("var_12071", dtype = "float64", shape = (13, 14, 15))#candidate|12071|(13, 14, 15)|var|float64
output = func_12070(var_12071)
func_12072 = relay.Function([var_12071], output)
mutated_mod['func_12072'] = func_12072
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12091 = relay.var("var_12091", dtype = "float32", shape = (4, 2, 1))#candidate|12091|(4, 2, 1)|var|float32
uop_12092 = relay.atanh(var_12091.astype('float32')) # shape=(4, 2, 1)
output = uop_12092
output2 = uop_12092
func_12099 = relay.Function([var_12091,], output)
mod['func_12099'] = func_12099
mod = relay.transform.InferType()(mod)
mutated_mod['func_12099'] = func_12099
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12100 = relay.var("var_12100", dtype = "float32", shape = (4, 2, 1))#candidate|12100|(4, 2, 1)|var|float32
func_12099_call = mutated_mod.get_global_var('func_12099')
call_12101 = func_12099_call(var_12100)
output = call_12101
func_12102 = relay.Function([var_12100], output)
mutated_mod['func_12102'] = func_12102
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5026_call = mod.get_global_var('func_5026')
func_5028_call = mutated_mod.get_global_var('func_5028')
call_12129 = relay.TupleGetItem(func_5026_call(), 2)
call_12130 = relay.TupleGetItem(func_5028_call(), 2)
var_12137 = relay.var("var_12137", dtype = "float32", shape = (110, 6))#candidate|12137|(110, 6)|var|float32
bop_12138 = relay.logical_and(call_12129.astype('bool'), relay.reshape(var_12137.astype('bool'), relay.shape_of(call_12129))) # shape=(110, 6)
bop_12141 = relay.logical_and(call_12130.astype('bool'), relay.reshape(var_12137.astype('bool'), relay.shape_of(call_12130))) # shape=(110, 6)
output = relay.Tuple([bop_12138,])
output2 = relay.Tuple([bop_12141,])
F = relay.Function([var_12137,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_12137,], output2)
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
