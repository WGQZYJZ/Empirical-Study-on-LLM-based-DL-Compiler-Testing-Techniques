import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_254 = relay.var("var_254", dtype = "uint16", shape = ())#candidate|254|()|var|uint16
const_255 = relay.const([[[6],[-6]],[[-6],[1]],[[-4],[5]],[[-4],[-5]],[[1],[5]],[[-6],[6]],[[-10],[-6]],[[-3],[-10]],[[5],[-8]],[[-7],[-10]],[[-3],[-4]],[[-2],[-2]]], dtype = "uint16")#candidate|255|(12, 2, 1)|const|uint16
bop_256 = relay.less(var_254.astype('bool'), const_255.astype('bool')) # shape=(12, 2, 1)
output = bop_256
output2 = bop_256
func_274 = relay.Function([var_254,], output)
mod['func_274'] = func_274
mod = relay.transform.InferType()(mod)
mutated_mod['func_274'] = func_274
mutated_mod = relay.transform.InferType()(mutated_mod)
var_275 = relay.var("var_275", dtype = "uint16", shape = ())#candidate|275|()|var|uint16
func_274_call = mutated_mod.get_global_var('func_274')
call_276 = func_274_call(var_275)
output = call_276
func_277 = relay.Function([var_275], output)
mutated_mod['func_277'] = func_277
mutated_mod = relay.transform.InferType()(mutated_mod)
var_430 = relay.var("var_430", dtype = "float64", shape = (16, 6, 5))#candidate|430|(16, 6, 5)|var|float64
uop_431 = relay.tan(var_430.astype('float64')) # shape=(16, 6, 5)
output = uop_431
output2 = uop_431
func_446 = relay.Function([var_430,], output)
mod['func_446'] = func_446
mod = relay.transform.InferType()(mod)
mutated_mod['func_446'] = func_446
mutated_mod = relay.transform.InferType()(mutated_mod)
var_447 = relay.var("var_447", dtype = "float64", shape = (16, 6, 5))#candidate|447|(16, 6, 5)|var|float64
func_446_call = mutated_mod.get_global_var('func_446')
call_448 = func_446_call(var_447)
output = call_448
func_449 = relay.Function([var_447], output)
mutated_mod['func_449'] = func_449
mutated_mod = relay.transform.InferType()(mutated_mod)
var_790 = relay.var("var_790", dtype = "uint8", shape = ())#candidate|790|()|var|uint8
var_791 = relay.var("var_791", dtype = "uint8", shape = (15, 11, 13))#candidate|791|(15, 11, 13)|var|uint8
bop_792 = relay.greater_equal(var_790.astype('bool'), var_791.astype('bool')) # shape=(15, 11, 13)
uop_804 = relay.rsqrt(var_791.astype('float64')) # shape=(15, 11, 13)
bop_814 = relay.minimum(uop_804.astype('int16'), relay.reshape(bop_792.astype('int16'), relay.shape_of(uop_804))) # shape=(15, 11, 13)
bop_820 = relay.logical_and(uop_804.astype('bool'), relay.reshape(bop_792.astype('bool'), relay.shape_of(uop_804))) # shape=(15, 11, 13)
output = relay.Tuple([bop_814,bop_820,])
output2 = relay.Tuple([bop_814,bop_820,])
func_828 = relay.Function([var_790,var_791,], output)
mod['func_828'] = func_828
mod = relay.transform.InferType()(mod)
mutated_mod['func_828'] = func_828
mutated_mod = relay.transform.InferType()(mutated_mod)
func_828_call = mutated_mod.get_global_var('func_828')
var_830 = relay.var("var_830", dtype = "uint8", shape = ())#candidate|830|()|var|uint8
var_831 = relay.var("var_831", dtype = "uint8", shape = (15, 11, 13))#candidate|831|(15, 11, 13)|var|uint8
call_829 = func_828_call(var_830,var_831,)
output = call_829
func_832 = relay.Function([var_830,var_831,], output)
mutated_mod['func_832'] = func_832
mutated_mod = relay.transform.InferType()(mutated_mod)
var_845 = relay.var("var_845", dtype = "int16", shape = (11, 10, 3))#candidate|845|(11, 10, 3)|var|int16
var_846 = relay.var("var_846", dtype = "int16", shape = (11, 10, 3))#candidate|846|(11, 10, 3)|var|int16
bop_847 = relay.add(var_845.astype('int16'), relay.reshape(var_846.astype('int16'), relay.shape_of(var_845))) # shape=(11, 10, 3)
output = relay.Tuple([bop_847,])
output2 = relay.Tuple([bop_847,])
func_857 = relay.Function([var_845,var_846,], output)
mod['func_857'] = func_857
mod = relay.transform.InferType()(mod)
var_858 = relay.var("var_858", dtype = "int16", shape = (11, 10, 3))#candidate|858|(11, 10, 3)|var|int16
var_859 = relay.var("var_859", dtype = "int16", shape = (11, 10, 3))#candidate|859|(11, 10, 3)|var|int16
output = func_857(var_858,var_859,)
func_860 = relay.Function([var_858,var_859,], output)
mutated_mod['func_860'] = func_860
mutated_mod = relay.transform.InferType()(mutated_mod)
var_882 = relay.var("var_882", dtype = "bool", shape = (8, 15, 11))#candidate|882|(8, 15, 11)|var|bool
var_883 = relay.var("var_883", dtype = "bool", shape = (8, 15, 11))#candidate|883|(8, 15, 11)|var|bool
bop_884 = relay.logical_and(var_882.astype('bool'), relay.reshape(var_883.astype('bool'), relay.shape_of(var_882))) # shape=(8, 15, 11)
bop_897 = relay.maximum(var_882.astype('int8'), relay.reshape(bop_884.astype('int8'), relay.shape_of(var_882))) # shape=(8, 15, 11)
var_926 = relay.var("var_926", dtype = "bool", shape = (8, 15, 11))#candidate|926|(8, 15, 11)|var|bool
bop_927 = relay.floor_mod(var_883.astype('float64'), relay.reshape(var_926.astype('float64'), relay.shape_of(var_883))) # shape=(8, 15, 11)
output = relay.Tuple([bop_897,bop_927,])
output2 = relay.Tuple([bop_897,bop_927,])
func_933 = relay.Function([var_882,var_883,var_926,], output)
mod['func_933'] = func_933
mod = relay.transform.InferType()(mod)
var_934 = relay.var("var_934", dtype = "bool", shape = (8, 15, 11))#candidate|934|(8, 15, 11)|var|bool
var_935 = relay.var("var_935", dtype = "bool", shape = (8, 15, 11))#candidate|935|(8, 15, 11)|var|bool
var_936 = relay.var("var_936", dtype = "bool", shape = (8, 15, 11))#candidate|936|(8, 15, 11)|var|bool
output = func_933(var_934,var_935,var_936,)
func_937 = relay.Function([var_934,var_935,var_936,], output)
mutated_mod['func_937'] = func_937
mutated_mod = relay.transform.InferType()(mutated_mod)
var_972 = relay.var("var_972", dtype = "uint32", shape = ())#candidate|972|()|var|uint32
const_973 = relay.const([[[-5,-3,-9,-2,7,-8,-4,-7,-8],[-6,-2,2,10,3,10,-4,-1,1],[-5,-8,3,-9,6,4,10,1,-8],[2,-2,-4,10,-7,-4,-8,3,3],[1,-5,-7,5,10,9,-10,3,-5],[6,6,6,-4,-1,2,5,8,-2],[-10,2,4,5,4,8,7,-5,-7],[-5,7,2,-1,-5,-8,6,6,7],[1,4,1,5,5,-3,2,5,-5],[1,5,-7,-2,10,-10,8,8,7],[3,9,3,-10,1,4,-4,4,-10],[-10,-1,-2,7,4,-1,7,4,-2]],[[8,-10,9,5,-1,-1,-9,5,3],[-2,-9,-8,-9,4,10,8,10,-9],[4,-2,-4,-7,-8,-2,4,-3,-2],[1,7,3,-3,-7,1,-4,1,-1],[1,-7,-4,9,-5,-9,3,-8,-7],[-8,-4,-5,-3,9,7,9,9,6],[-5,9,7,-8,-10,-3,-7,-9,-9],[5,5,6,-7,-9,-2,-10,-2,-8],[-9,-3,3,5,-8,3,1,9,-4],[-10,-1,7,-6,2,-8,-8,7,3],[9,9,6,-5,10,5,-1,6,3],[-7,2,6,-10,-4,-8,-8,-9,-4]],[[-9,-2,-3,6,9,5,-7,1,-10],[7,3,-10,10,-8,4,-4,1,5],[-10,-5,3,2,-10,7,-2,-3,-8],[8,10,-9,-7,9,-6,1,5,6],[6,6,-1,-6,-9,-9,-2,7,2],[6,8,9,-10,-1,-4,1,-4,-6],[1,-9,-2,9,5,4,5,-1,5],[-6,-8,-10,-3,4,9,2,3,2],[2,-9,-1,-6,-5,9,5,-7,-4],[9,9,5,-3,-1,10,2,-7,1],[-6,-4,4,-2,-1,-3,-5,2,-6],[-3,-6,5,-8,-10,-10,4,-5,-8]],[[4,-7,-9,7,3,-2,-6,7,-9],[-10,1,-3,10,-8,8,6,-8,-8],[-5,2,6,-6,9,4,6,-5,3],[-8,7,-8,4,8,6,8,1,-9],[4,-9,9,-10,-9,-3,-5,5,-9],[-9,-8,-2,3,8,-9,-10,4,-5],[3,9,-2,-4,5,1,6,-4,4],[-1,-5,-10,-5,9,-2,-4,2,6],[-6,-3,4,5,-3,-4,-9,6,1],[-10,8,8,4,4,-5,-1,3,-4],[-7,6,-1,7,-5,-4,8,-5,-3],[-6,-6,2,1,2,7,-10,6,6]],[[-8,5,-5,10,-3,2,9,-3,-6],[-6,-8,10,6,-2,10,10,-1,9],[-6,-1,-5,6,-1,-1,-6,6,7],[3,-8,8,3,3,-4,9,-3,-10],[-5,6,-7,-5,-6,-1,6,8,7],[3,-5,3,1,1,4,4,-10,-7],[7,-2,-2,-8,4,-4,4,-10,-4],[-8,7,-8,-1,-4,5,5,-3,7],[-9,4,10,4,-5,-1,-9,3,8],[-1,-8,-7,-6,4,-1,-5,-5,6],[8,9,6,4,1,-3,3,-8,-1],[-3,-1,-6,-10,-5,-3,10,10,-7]],[[-3,2,-2,-5,-1,7,9,-10,-7],[-3,9,-1,8,4,-5,2,3,2],[-1,10,9,5,-7,8,-1,-2,8],[3,-9,4,7,1,-2,-5,1,6],[-5,8,5,-8,9,-9,3,5,-8],[-5,-8,6,3,-4,9,4,2,7],[-10,-6,-3,7,6,10,-2,-8,5],[-10,-5,1,-6,-9,-9,-8,1,9],[8,2,10,7,-10,4,-10,4,-1],[-1,-1,7,-7,8,-8,2,5,-1],[7,-8,-4,-2,7,10,-10,6,3],[9,10,-10,6,-6,7,7,5,2]],[[-8,-4,10,-4,6,2,-5,9,-10],[-4,10,-9,-5,-2,-2,2,9,-4],[1,-9,-7,-4,4,8,2,-2,1],[-1,10,9,-8,-3,-8,-7,-4,-3],[9,-3,-3,-7,-2,9,-2,10,-4],[7,1,-10,-4,5,3,-9,7,5],[5,-7,3,-10,6,9,10,-1,-6],[7,8,-10,-2,-5,-2,-3,4,-6],[7,2,-8,3,-8,1,5,-4,2],[4,-2,4,-1,1,-6,10,2,9],[4,-10,-6,8,8,6,5,-5,1],[3,8,-5,10,10,-9,4,10,-8]],[[6,10,10,-6,-8,-4,-2,-8,2],[7,-1,5,-7,-5,-4,3,-1,-4],[3,-5,-2,-9,-7,-7,2,-2,10],[-3,6,-3,-1,2,3,10,-7,6],[-6,-6,-4,4,4,9,3,2,-7],[2,3,-7,-2,-10,-4,10,3,-6],[8,1,6,-7,-1,6,4,-6,-4],[3,2,8,-2,-9,-6,-2,-3,-6],[4,-5,4,2,3,-7,3,-4,-5],[-10,-1,-4,3,1,10,4,5,-8],[3,9,10,-5,-7,-5,-1,9,-5],[1,8,4,1,1,-9,3,1,-10]],[[-1,1,1,-10,4,-6,-2,-6,9],[8,10,-4,-8,-1,-2,-9,5,8],[-7,-10,-8,1,3,10,-9,-2,10],[8,-6,9,1,10,10,-1,6,10],[-10,-6,8,7,-6,6,6,4,-4],[-1,-10,8,8,-9,-3,-8,9,5],[10,5,-2,10,7,-1,6,4,2],[-8,-3,3,-5,10,7,-3,9,4],[1,9,-9,-6,4,-3,-4,-5,7],[5,-2,-7,-2,7,8,-1,5,-4],[-4,-1,10,5,4,-3,9,-2,2],[-2,-10,6,-10,7,-8,-10,-3,1]],[[5,-7,5,10,7,6,3,-4,5],[-3,6,10,2,8,-3,9,4,-6],[8,-4,-8,-6,6,-6,-1,-8,10],[3,-10,-9,10,10,6,5,-10,10],[-7,10,8,8,6,6,-6,10,-10],[8,9,-5,3,-10,7,2,-10,-1],[10,-8,7,-6,7,-8,7,8,-3],[-10,1,9,1,5,-6,2,6,-4],[-7,6,8,-10,10,-8,1,9,-9],[-1,2,4,2,5,5,3,-4,6],[10,5,-4,-3,1,8,-4,10,6],[-5,-9,10,-4,8,1,7,9,-3]],[[7,9,-2,7,7,2,-3,-6,1],[-8,1,2,9,-5,-3,1,-6,7],[-7,-4,4,-10,6,3,3,2,-9],[-8,-6,-5,3,9,6,9,-10,8],[10,-3,5,6,9,-2,4,5,2],[9,5,7,3,5,-9,-9,2,-7],[-10,-4,1,-5,5,7,1,-5,5],[10,-7,1,-7,-7,4,5,-7,3],[5,4,-10,-9,6,-1,-3,-9,5],[6,-2,-2,-7,2,-6,-5,-5,-10],[2,7,-3,-1,9,-7,-1,8,-8],[-2,7,-10,-9,1,5,-10,-3,5]],[[7,-4,-5,1,-6,9,-9,-8,3],[9,-4,-5,-4,-4,-3,-4,-4,-7],[9,-4,8,6,4,-4,-1,-8,-5],[-2,9,-7,8,1,10,-2,5,-4],[9,10,4,-10,-1,10,3,-5,1],[-3,5,-10,1,8,7,-10,-1,-2],[6,-2,10,3,5,4,-1,-2,2],[-5,-3,10,4,8,2,-10,2,5],[3,5,-5,-3,-9,-5,8,-5,-3],[-3,-7,-2,-3,-7,-6,6,10,7],[-2,6,-5,2,2,-4,-2,-2,10],[-6,-6,-7,-5,2,-6,-5,-9,-10]],[[1,-10,9,6,1,-2,1,5,3],[10,6,-5,2,3,-8,-8,6,2],[1,1,-7,6,-1,5,-2,-1,-10],[-5,6,-4,2,3,-9,7,4,-4],[1,7,1,-7,1,-3,6,-3,-7],[-7,8,-9,7,-7,-6,-2,-10,-10],[-4,-4,-4,-6,-7,3,6,3,1],[1,9,-1,-10,1,-1,-3,-7,10],[5,2,-6,4,-6,-6,-8,-5,6],[2,-8,-7,6,-3,-6,6,8,-3],[-4,6,3,-7,10,10,9,-3,-6],[5,10,-9,-9,-10,-5,-1,10,-1]],[[9,6,9,3,-7,-4,-7,-7,4],[-7,-10,-2,-2,6,-10,6,4,-7],[7,10,8,-7,2,6,-1,-3,-10],[6,7,5,-8,7,5,4,5,6],[-9,-8,10,-10,-7,-9,-9,-2,-8],[6,-9,9,-6,-6,8,-4,-8,1],[8,-6,-6,5,-2,6,3,-8,-4],[6,10,2,-7,-9,3,-10,3,10],[-1,-7,-2,-4,4,9,9,-1,-9],[-8,-1,9,7,7,-7,1,1,-2],[-2,10,-8,-3,4,5,9,2,-10],[-6,-2,7,9,7,8,5,-6,4]],[[-3,1,3,5,-9,3,-7,6,-1],[1,3,-2,-9,-8,3,1,3,7],[7,-9,8,6,1,7,7,4,5],[-10,6,-1,4,-6,1,-2,-5,5],[-2,-1,4,-7,-5,2,8,6,2],[2,9,-2,9,-1,6,10,-10,3],[10,-5,-10,8,-1,-1,-2,-10,10],[3,7,-6,1,-4,-8,3,8,4],[8,-7,6,1,-2,-1,4,-2,8],[-5,5,-8,-8,-2,2,6,7,9],[3,3,3,-8,8,10,-9,4,6],[-10,4,3,-7,8,-4,9,-8,-3]],[[-6,10,2,-9,4,-8,3,7,9],[5,-8,-1,-9,10,-5,-8,5,-5],[7,1,-5,-4,-6,-8,-10,2,-6],[-10,5,2,-2,-1,8,5,7,-9],[-4,1,-3,-6,3,-10,-3,6,8],[-8,-8,-5,-2,-4,-6,-1,3,2],[-2,8,6,-4,6,-9,-10,5,5],[-6,2,-7,-10,-1,-2,-8,1,10],[4,8,-6,6,-3,3,3,-8,9],[3,6,2,-7,2,8,5,10,6],[10,3,3,3,5,-10,7,-4,9],[10,-8,-4,-8,2,4,-3,10,-8]]], dtype = "uint32")#candidate|973|(16, 12, 9)|const|uint32
bop_974 = relay.bitwise_and(var_972.astype('uint32'), const_973.astype('uint32')) # shape=(16, 12, 9)
func_857_call = mod.get_global_var('func_857')
func_860_call = mutated_mod.get_global_var('func_860')
const_991 = relay.const([7,6,10,-2,-7,10,9,-6,2,7,-1,-6,-1,-9,-3,6,8,-7,9,5,-10,-9,-8,4,-4,-4,9,8,-6,8,7,7,-7,-4,-4,2,5,-1,-6,-1,-9,7,-4,-9,-4,-8,-1,6,1,-6,-10,-9,10,6,-8,-8,3,-4,-2,5,-9,9,-10,-10,7,-8,-4,2,8,10,6,-2,3,5,-6,-3,3,-7,-7,8,2,-10,2,10,1,-5,-10,-5,-2,10,1,4,-3,1,-7,5,4,6,7,-7,8,7,-10,10,-5,1,-2,-1,6,-9,2,4,9,-3,6,7,5,-1,-8,-6,-1,-8,2,10,-3,2,-2,1,-6,2,-6,7,4,-6,-9,3,1,-3,-3,2,-3,-3,-3,-10,1,-5,2,-8,-2,-9,9,2,-5,7,-1,6,-5,1,-3,9,3,-1,-7,-3,3,3,6,-6,-2,1,-1,-7,5,-4,-9,2,-8,6,2,-8,3,-9,-7,-2,-5,2,1,2,-9,6,-1,9,1,-9,-5,8,-6,-7,-1,2,3,3,5,-1,2,-2,6,-6,-5,10,2,9,4,-3,-4,-2,-8,2,10,8,9,-9,-1,1,-2,7,-8,3,2,-8,10,-5,7,-4,9,1,3,-4,-2,10,8,7,-4,8,6,-4,8,-5,-7,3,10,-5,-1,5,5,-9,-3,-9,-9,-4,-4,1,10,-8,2,4,-3,-5,9,10,-7,9,7,10,-4,9,5,-10,6,3,-9,-2,-5,9,-10,9,9,-9,5,-2,-6,-7,-3,-9,4,6,8,-8,-6,-8,-7,6,-7,4,-4,1,9,4,-4,2,-2,3,-8,-4,5,3,-1,10,3,9,4,9,1,-7,6,-5,8,10,-7,2], dtype = "int16")#candidate|991|(330,)|const|int16
call_990 = relay.TupleGetItem(func_857_call(relay.reshape(const_991.astype('int16'), [11, 10, 3]), relay.reshape(const_991.astype('int16'), [11, 10, 3]), ), 0)
call_992 = relay.TupleGetItem(func_860_call(relay.reshape(const_991.astype('int16'), [11, 10, 3]), relay.reshape(const_991.astype('int16'), [11, 10, 3]), ), 0)
func_274_call = mod.get_global_var('func_274')
func_277_call = mutated_mod.get_global_var('func_277')
call_994 = func_274_call(relay.reshape(var_972.astype('uint16'), []))
call_995 = func_274_call(relay.reshape(var_972.astype('uint16'), []))
func_446_call = mod.get_global_var('func_446')
func_449_call = mutated_mod.get_global_var('func_449')
const_1002 = relay.const([[7.794347,-8.470498,3.254235,-1.369938],[-4.939664,-0.750830,-2.640801,-2.123299],[-9.613254,-9.975326,9.696821,1.739809],[-8.615260,-2.712728,-6.873223,4.692472],[-6.869844,-1.003703,-7.335864,9.648998],[-1.773589,-1.616376,-8.465869,-0.383256],[-2.093003,-6.586531,-1.161140,2.394973],[-6.060368,-2.784044,-9.650901,1.463206],[4.816248,5.577065,-6.245982,-7.460299],[-6.925684,3.463302,4.907769,4.531681],[-3.352040,-8.740213,-7.486209,2.588619],[0.901206,5.832916,9.387838,-3.886105],[6.158467,3.179829,9.167774,-0.588672],[-0.010168,-6.895277,6.161870,5.271285],[7.608124,0.054088,6.254307,5.859860],[-9.624253,2.683664,3.348616,-5.217653],[3.423427,-3.078051,2.023424,-1.139326],[-5.333287,0.548294,5.491632,4.906334],[-2.011859,-8.017674,6.026356,-2.427274],[-8.447030,-8.630185,-4.067159,-6.693279],[-4.326070,-9.755313,5.558787,1.752582],[4.418862,-6.985518,-5.175527,-8.894333],[-9.898505,-6.645087,-8.787715,6.446641],[-1.384095,-4.243637,-6.865102,-4.333137],[4.677909,-9.009450,-4.256865,-2.056510],[-1.055755,-7.011317,-4.314628,-5.155805],[7.293910,-3.137745,0.830225,-0.344584],[2.455771,-4.945260,-2.397924,-1.323412],[1.355328,-8.182768,9.390799,-5.666251],[3.415834,-9.874121,4.719750,-5.510513],[4.509336,-4.733115,-1.890806,1.032415],[4.012807,2.019318,-0.935971,8.151182],[-2.256607,7.296645,-6.086584,-6.659933],[-4.982350,0.068191,6.061815,-3.768404],[-6.540297,3.900085,-0.810564,7.120298],[4.753457,2.558792,-5.477316,4.150197],[-7.396755,-5.712279,-9.458856,7.942501],[1.986419,-6.959565,-1.547298,-9.723521],[7.448873,-6.206074,-4.014153,0.559678],[-3.595169,1.746362,9.239822,-6.485179],[-1.558328,-6.745002,1.441265,7.151324],[-8.411849,5.642297,2.587435,-2.475557],[0.029784,-7.625364,-5.165223,3.861401],[-7.044225,5.582151,-0.373146,4.235449],[2.486042,1.802606,2.266359,5.769421],[8.731893,7.186879,-8.599253,5.479401],[-5.806653,4.022428,-9.555848,7.746748],[-9.359490,-7.408577,-7.682783,3.134320],[-1.683238,-5.203742,7.081262,5.665279],[-5.304754,0.777574,-0.638820,9.679193],[-0.221743,0.362431,6.367565,8.826122],[-2.677231,-4.516440,-0.596857,-4.206260],[6.600514,-3.343447,-1.462729,8.715399],[-3.525675,-6.291133,6.883164,7.690949],[-7.789529,-4.560903,-2.569447,9.267302],[-5.260317,8.229327,3.125026,7.930136],[2.830935,-3.914263,3.928572,-5.656977],[-2.579002,2.307328,-7.847290,-8.463535],[6.193859,1.083852,-4.704746,-6.443516],[-5.254935,4.632242,7.360220,-3.505679],[5.675525,5.932803,-7.464551,-8.075350],[-1.334368,6.871427,3.289287,7.308809],[-7.950978,-2.986695,-2.713636,6.168220],[-0.091813,-1.442183,1.797632,-4.205007],[4.128135,-5.061296,-3.108513,7.904028],[-3.609430,6.113558,-7.243145,-1.798441],[1.091961,4.244372,-8.752251,7.107282],[-8.775100,-7.351940,-2.304952,-8.440669],[-0.020365,-5.044819,1.553443,8.577170],[-5.120244,8.609364,-8.642032,1.337452],[-9.226038,6.012899,-1.981101,-9.250205],[-1.934322,-7.966848,1.422948,3.897359],[1.795013,-8.985513,0.608263,-8.204681],[8.505626,-5.531821,-9.386273,8.114999],[-3.580575,1.741697,3.578027,8.099669],[-0.381760,6.509154,-2.823263,-0.366750],[-5.595410,9.912915,-3.591978,4.867213],[0.906836,3.623033,3.279514,4.990521],[8.754093,-7.477423,-2.374288,9.327494],[-0.542027,-5.880479,5.479637,-8.696754],[-7.826980,3.812617,-0.084376,-6.188248],[-4.219245,9.226864,-3.849373,8.655999],[3.304131,6.757382,-6.276739,-4.556569],[1.081996,7.524637,1.557013,-6.635762],[8.082753,3.344736,-6.381727,-0.381356],[5.532566,-4.587934,-1.714521,-6.958851],[-5.461593,0.359831,-5.046704,3.033997],[-6.131732,-3.474480,-1.704210,1.116020],[-4.133811,5.090510,-1.953353,2.007321],[7.638220,-3.353667,3.174274,1.760527],[-4.261394,-0.832135,0.161603,-8.181299],[3.972452,1.906931,6.499149,8.131640],[2.241802,-2.267861,-6.192691,-2.917634],[4.844559,6.198185,7.033105,-7.917806],[2.196610,-2.288546,-5.057060,3.966969],[7.723866,-7.496282,7.922538,-7.117289],[-6.721746,2.509171,-8.166415,0.722857],[-2.109832,-4.947875,1.742410,8.085332],[-8.766528,1.028005,-5.521582,-7.135867],[-9.176232,-0.735009,-1.765329,-5.717690],[3.573545,-3.071171,6.422583,7.665712],[-8.946958,7.693795,7.651295,9.811363],[-1.391093,-8.374633,5.754684,-3.926815],[6.571272,1.198588,4.083311,2.147071],[7.432913,-0.059077,4.881932,-7.938233],[-0.990459,9.854204,-8.598231,1.055492],[-7.924327,0.101856,-7.046598,6.407222],[-1.106593,3.270042,-3.454181,-7.071619],[-4.442486,8.422596,1.572833,-5.253160],[1.463088,1.682455,-3.289332,3.139813],[-4.746754,-2.513813,-0.226347,6.028730],[-4.481331,4.599558,6.750168,4.133083],[-1.739388,9.587450,-0.860782,2.473962],[2.507194,-5.431748,4.789255,-5.272451],[-1.783101,-6.446920,-9.557705,-1.275570],[7.208709,-5.679439,4.351296,-6.065945],[-5.378391,6.604156,3.504202,-4.981942],[3.976054,-2.395828,-6.960451,5.041478],[0.240835,-5.385309,0.645154,9.773219],[-0.332109,5.556736,2.849402,0.237046]], dtype = "float64")#candidate|1002|(120, 4)|const|float64
call_1001 = func_446_call(relay.reshape(const_1002.astype('float64'), [16, 6, 5]))
call_1003 = func_446_call(relay.reshape(const_1002.astype('float64'), [16, 6, 5]))
output = relay.Tuple([bop_974,call_990,const_991,call_994,call_1001,const_1002,])
output2 = relay.Tuple([bop_974,call_992,const_991,call_995,call_1003,const_1002,])
func_1005 = relay.Function([var_972,], output)
mod['func_1005'] = func_1005
mod = relay.transform.InferType()(mod)
var_1006 = relay.var("var_1006", dtype = "uint32", shape = ())#candidate|1006|()|var|uint32
output = func_1005(var_1006)
func_1007 = relay.Function([var_1006], output)
mutated_mod['func_1007'] = func_1007
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1233 = relay.var("var_1233", dtype = "float64", shape = (9, 12, 1))#candidate|1233|(9, 12, 1)|var|float64
uop_1234 = relay.tan(var_1233.astype('float64')) # shape=(9, 12, 1)
output = relay.Tuple([uop_1234,])
output2 = relay.Tuple([uop_1234,])
func_1239 = relay.Function([var_1233,], output)
mod['func_1239'] = func_1239
mod = relay.transform.InferType()(mod)
var_1240 = relay.var("var_1240", dtype = "float64", shape = (9, 12, 1))#candidate|1240|(9, 12, 1)|var|float64
output = func_1239(var_1240)
func_1241 = relay.Function([var_1240], output)
mutated_mod['func_1241'] = func_1241
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1471 = relay.const([[[0.102572,1.425627,-2.454573,-7.812764,8.363350,6.056514,1.768873,9.856256,-7.447085,1.457516],[1.710616,-7.018580,-8.519678,-0.113062,7.342574,-5.747527,-5.187886,5.498010,9.971454,8.979094],[8.398955,-4.705206,4.810561,2.224727,-3.719305,0.244968,-4.090580,2.299600,-8.760923,0.627237]],[[-6.161227,-2.082380,-7.386666,4.242318,0.952568,-2.946543,5.195549,-9.565945,-3.183464,-4.568735],[-0.261661,-5.310065,-0.585713,-8.306973,-1.762682,-1.975335,8.056969,8.710710,3.739845,8.966193],[5.203787,9.835515,5.759276,6.389691,-9.750434,-8.135229,-0.491698,6.759100,-5.007462,5.294782]],[[-5.814528,8.854477,-6.436679,2.506146,2.258248,3.482127,-5.546079,-2.289985,-0.232931,9.182557],[6.506080,7.791857,9.285419,-0.622932,-4.690464,-3.192019,-0.778736,0.671000,-5.446726,-6.261565],[4.004016,-4.739103,-1.985973,6.227066,-8.422035,8.358494,-1.721917,7.149425,-6.309661,-5.424539]],[[2.895244,6.442324,-7.954355,1.324360,3.057092,1.120724,5.274108,-8.118969,-0.345845,-9.028710],[-2.857223,-8.807981,-8.130752,-3.874653,-3.131132,-4.886572,4.382690,0.367764,-4.683233,-9.616918],[-8.321271,-2.136214,8.578338,9.065818,9.181626,4.641223,-9.544432,-1.803808,9.794550,4.629022]],[[2.067606,-4.385970,3.656337,1.289152,-3.363945,0.020112,6.258934,-9.421245,-1.175140,-0.401695],[2.898699,9.818697,7.924366,-9.483214,0.265705,-4.613181,8.143400,8.286913,-8.064031,-7.192016],[8.051201,6.457529,-0.440230,5.229354,-2.798980,-8.051236,4.759926,9.363299,4.435588,-0.064292]],[[3.848029,-4.590831,2.785258,2.781272,-2.949595,-0.552161,0.903736,-3.931902,3.573140,-4.401254],[3.660951,4.769199,-5.181797,2.244559,-4.284475,-7.486542,7.357951,7.611711,1.187070,-2.146842],[-7.196103,1.915764,0.622242,3.567903,4.330675,-0.807498,-3.790531,-9.025429,-9.008225,8.525647]],[[1.400225,-6.832962,-0.167335,8.511645,-1.659148,2.627215,-8.123375,-7.905514,-9.932111,-2.102351],[8.344139,-6.713330,-6.731658,-2.802633,-0.792749,1.961004,-0.803806,-5.020439,9.433436,-4.313169],[-6.670655,8.061162,-3.888901,-0.703307,3.455363,-7.405667,7.991406,1.372034,2.166233,-9.964060]],[[5.938987,6.617669,0.989292,-1.849667,6.582889,-0.259374,-5.534206,-9.641775,1.547020,3.552621],[4.419795,5.053765,-9.401032,-2.960429,-1.548989,1.704811,2.732778,9.655250,2.051763,0.764729],[-4.083957,-2.163601,1.041610,9.086294,6.000683,-8.818135,9.069285,2.399120,-4.615574,2.878395]]], dtype = "float64")#candidate|1471|(8, 3, 10)|const|float64
uop_1472 = relay.cos(const_1471.astype('float64')) # shape=(8, 3, 10)
output = relay.Tuple([uop_1472,])
output2 = relay.Tuple([uop_1472,])
func_1474 = relay.Function([], output)
mod['func_1474'] = func_1474
mod = relay.transform.InferType()(mod)
output = func_1474()
func_1475 = relay.Function([], output)
mutated_mod['func_1475'] = func_1475
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1498 = relay.var("var_1498", dtype = "int32", shape = (1, 10, 11))#candidate|1498|(1, 10, 11)|var|int32
var_1499 = relay.var("var_1499", dtype = "int32", shape = (9, 10, 11))#candidate|1499|(9, 10, 11)|var|int32
bop_1500 = relay.equal(var_1498.astype('bool'), var_1499.astype('bool')) # shape=(9, 10, 11)
uop_1511 = relay.asin(var_1498.astype('float32')) # shape=(1, 10, 11)
func_1474_call = mod.get_global_var('func_1474')
func_1475_call = mutated_mod.get_global_var('func_1475')
call_1521 = relay.TupleGetItem(func_1474_call(), 0)
call_1522 = relay.TupleGetItem(func_1475_call(), 0)
output = relay.Tuple([bop_1500,uop_1511,call_1521,])
output2 = relay.Tuple([bop_1500,uop_1511,call_1522,])
func_1523 = relay.Function([var_1498,var_1499,], output)
mod['func_1523'] = func_1523
mod = relay.transform.InferType()(mod)
var_1524 = relay.var("var_1524", dtype = "int32", shape = (1, 10, 11))#candidate|1524|(1, 10, 11)|var|int32
var_1525 = relay.var("var_1525", dtype = "int32", shape = (9, 10, 11))#candidate|1525|(9, 10, 11)|var|int32
output = func_1523(var_1524,var_1525,)
func_1526 = relay.Function([var_1524,var_1525,], output)
mutated_mod['func_1526'] = func_1526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1474_call = mod.get_global_var('func_1474')
func_1475_call = mutated_mod.get_global_var('func_1475')
call_1566 = relay.TupleGetItem(func_1474_call(), 0)
call_1567 = relay.TupleGetItem(func_1475_call(), 0)
func_828_call = mod.get_global_var('func_828')
func_832_call = mutated_mod.get_global_var('func_832')
const_1569 = relay.const(9, dtype = "uint8")#candidate|1569|()|const|uint8
const_1570 = relay.const([-10,-7,-2,-8,2,7,10,-1,5,-5,-4,10,-7,-1,2,3,4,10,9,-5,8,2,5,-10,7,-3,6,-10,-8,1,-10,-3,6,-4,-1,-8,1,8,-3,6,4,10,5,-2,2,-2,-10,1,-8,1,-2,-10,-6,10,-7,-9,8,-10,1,7,-7,-8,-5,1,3,-7,-10,9,5,9,-6,2,10,-8,-6,-8,5,10,-4,5,4,2,9,3,-1,-8,1,-10,4,5,6,-2,7,10,2,1,-9,3,-4,-2,9,1,-9,-2,-2,2,-8,6,-6,-1,6,-6,2,-1,-4,-1,-4,-4,5,6,2,-5,2,-8,-10,7,-8,10,-2,8,5,-10,4,-4,9,8,9,2,7,-2,-8,2,3,7,5,3,7,-1,-7,-3,4,-8,7,6,9,-10,6,2,-5,5,6,-10,-1,-3,-5,-5,-10,-3,2,-10,5,7,-3,1,9,10,3,-8,2,-3,10,7,10,6,7,-4,-5,4,-1,9,-10,-5,8,5,5,-8,-7,-4,3,10,5,4,4,-9,2,5,7,-5,5,7,-10,-6,8,-4,9,2,-10,3,6,-9,2,-2,-5,-3,9,-2,-3,-5,-8,3,-5,-3,-3,8,-2,10,10,10,9,8,1,6,-10,-6,-10,-8,-4,-1,-9,6,8,5,8,-5,-9,4,5,-4,10,5,-9,-8,-6,-1,10,8,3,-5,-9,9,-5,7,-4,-7,1,8,-5,-4,-7,-7,2,4,1,8,10,-7,2,-9,5,3,-7,7,-7,-4,3,1,9,3,-5,-9,8,-3,7,7,5,-7,10,6,-2,4,-2,-3,10,-10,-6,-3,-4,-5,6,3,3,-6,4,2,2,5,3,-4,3,10,-4,6,-9,7,4,-9,-1,-1,8,-3,1,4,-8,-7,-4,-2,9,-6,-8,4,-2,10,9,-10,-7,9,1,-10,-4,1,3,8,-1,2,7,3,8,-5,-7,6,-8,-1,-8,9,7,2,3,-6,6,4,-4,5,4,-9,-6,6,9,4,-8,9,-5,9,-5,-10,3,-6,-3,-8,-2,-8,3,-4,-1,10,-3,5,4,-6,9,9,10,-8,6,-1,-5,9,-3,10,1,-3,3,-4,2,-7,4,4,1,10,-7,8,-10,-2,9,-6,4,-5,-7,-5,9,-3,-7,-8,8,8,10,9,-2,-4,-3,-9,2,-5,5,10,-9,6,10,4,5,-3,-5,-5,-3,8,-9,-2,-3,2,4,-3,-4,1,-4,-2,-7,3,7,-1,-7,6,-5,9,-5,7,2,4,-8,10,10,-2,6,10,-5,6,7,-2,-2,2,1,-1,-9,10,10,3,3,8,3,5,-7,2,4,-8,-4,-8,-10,-9,-3,-6,9,4,7,1,10,-7,-8,-2,-2,3,-1,-2,-9,9,8,-5,-7,10,1,-1,9,9,-1,-2,-1,1,-5,10,2,5,5,8,9,5,1,-2,-5,10,1,-9,8,-4,-2,8,-4,-3,-1,2,-1,1,-4,-4,5,7,7,-8,-7,-9,-9,-3,10,-3,-9,2,-5,-1,7,7,1,-9,1,5,-2,-5,1,-3,3,1,-4,-1,-5,5,2,-5,-8,-1,-2,7,3,4,-1,7,4,8,-1,4,-5,-2,-4,10,-1,-1,9,6,9,6,-6,3,-10,-7,-2,-1,-1,2,9,-7,2,3,5,1,-1,3,-9,9,-9,-4,-7,-6,7,-6,-1,-7,1,4,9,-10,-4,10,-1,-5,-5,-1,-6,-1,-6,-9,9,10,6,-6,9,7,-10,7,6,-2,-2,3,10,1,2,5,-6,1,-6,8,4,-9,2,6,9,-1,10,9,10,8,-1,-5,-7,-10,-5,10,-4,4,4,-6,-9,-4,-2,9,-4,-6,-1,2,9,-10,-10,4,9,2,9,8,6,6,-8,2,3,7,-10,1,2,-2,4,-8,5,8,-7,-3,-10,-3,-6,-10,-4,5,9,3,-9,-6,2,-6,6,-4,-2,-8,-8,1,-5,-4,-10,-4,7,2,4,-1,-4,7,2,-2,8,7,10,-7,10,5,2,-1,-9,-9,3,-1,-8,8,8,6,-2,10,-4,-9,2,-6,-5,5,2,-9,5,-3,-8,5,-10,4,8,4,-4,-6,-8,1,1,-9,10,-9,8,8,-10,-4,7,-2,1,-5,-8,-1,5,-10,-6,9,-7,-2,10,-2,4,3,-5,4,-1,-1,2,-7,-4,3,-8,-7,-3,-1,-9,-3,1,4,-1,2,-9,-4,6,8,-10,9,3,2,-5,9,8,-6,-8,-4,9,4,10,-1,-1,6,7,-7,1,8,-4,9,1,-10,-6,-1,-2,-4,-2,9,-3,-5,2,3,-3,9,-2,-7,4,1,4,6,6,8,-5,3,6,8,-10,-1,-6,8,9,-10,-5,-2,2,4,-7,9,-3,-10,10,5,3,-3,-6,-6,8,-9,-6,3,6,9,4,-5,-10,-4,-5,2,-6,-6,8,9,-7,-1,9,2,-3,-1,8,-2,3,9,-8,5,-6,6,4,-9,6,-5,-4,-10,-7,-2,7,3,1,-7,3,-2,-6,4,-6,10,-5,-6,-1,5,-5,2,2,-9,7,3,9,-10,6,4,1,5,-10,-4,-5,-10,-6,10,6,-3,7,-3,-3,-3,1,10,-3,5,-6,-4,-7,-1,7,-3,3,5,3,-8,3,3,9,5,10,5,8,-9,6,-10,-1,5,8,-8,8,-5,-7,4,-4,8,-6,2,-4,10,10,10,-2,9,-3,-9,3,1,-4,8,1,-6,10,-2,10,2,-4,3,-7,6,-1,2,-10,-6,5,4,3,-4,7,-7,10,9,4,-1,-6,5,-1,1,-10,-8,2,-1,-2,-8,-3,-8,-6,8,-10,-5,4,-4,-6,8,6,1,8,5,-8,-10,9,5,-4,-9,10,3,-3,2,-5,-5,6,9,1,1,6,-2,9,2,10,2,-5,-5,1,10,-10,7,3,8,-9,-5,2,1,7,-9,-5,7,3,10,1,-1,5,5,-3,3,-3,6,10,-9,1,1,6,-7,10,-4,-7,10,-1,1,-9,6,5,-7,9,1,3,-9,-8,7,-6,-8,6,-5,2,-2,2,-3,2,-3,6,-3,6,8,-8,1,-8,7,9,-2,7,4,-2,8,6,4,-3,-3,-9,-4,-9,-3,6,-2,9,5,-8,7,5,3,-5,7,6,-9,-2,5,10,10,-5,10,-4,2,-4,-1,4,-2,5,-9,1,7,2,7,-10,-5,-7,1,-10,5,-1,4,-2,-4,-8,-7,2,-4,-8,4,8,-2,-4,8,5,-9,10,4,2,1,3,-10,-4,7,3,-9,-3,-6,4,-1,7,-7,-5,-1,9,6,-9,-4,1,6,-5,7,-8,4,-8,10,7,2,-8,-9,-4,6,-3,10,-6,-10,-1,-10,1,-10,-1,2,-8,9,9,3,-5,9,-3,-4,5,-9,-2,-5,3,1,6,3,10,-1,2,-2,-5,8,2,-5,7,-3,-5,3,-4,1,8,5,5,-6,-10,-5,1,-10,-7,-10,-1,5,-1,-3,3,-4,-9,10,5,-3,8,9,-3,-4,6,-5,7,4,-8,-5,-2,-3,-8,-6,-3,-9,9,2,-8,2,-10,-2,9,-5,4,10,-8,8,-8,-2,-3,1,10,-6,10,2,-7,7,2,-4,1,-4,-7,-9,-7,7,4,6,3,-2,-9,1,1,-3,9,9,1,2,-6,-4,-4,6,9,1,1,-5,8,-10,3,1,-3,5,-4,4,8,4,9,9,2,-9,3,-7,1,9,-1,9,1,-9,-9,-6,1,8,-1,-7,6,6,-2,-10,10,-9,2,-6,2,-9,-8,-9,-4,-6,-5,-8,9,-10,-6,-5,10,7,4,4,-9,-6,-9,-6,3,7,-5,8,-10,-8,-9,-5,9,-2,7,8,10,-5,-10,-1,2,-10,7,-4,6,-3,5,5,-10,-6,2,5,9,-2,-10,1,-3,9,-8,-6,5,1,-9,-1,-3,8,-2,-9,2,9,6,-1,10,8,-5,4,6,-9,10,-4,8,10,4,8,-1,-5,6,6,10,-5,10,4,-5,-1,-2,9,6,9,-9,5,3,-6,7,-6,-8,1,-2,-6,-7,-3,-1,-8,-4,-8,-3,4,4,-6,4,8,-5,-3,-2,-6,-5,8,5,-4,3,1,-6,4,7,-1,-4,-6,-5,-5,-8,-8,2,-1,-3,6,-9,-4,6,-5,7,-5,-2,-9,-7,-6,7,-10,-9,8,7,8,2,3,7,10,-3,-5,5,-3,-8,9,-2,-4,7,-1,-5,2,-10,-7,2,-2,-4,1,-1,-2,-3,4,-8,-6,-10,1,7,-7,8,-3,3,5,-2,-7,-1,2,1,-3,6,-6,-8,4,-2,-4,6,9,5,-9,10,-2,6,-9,1,6,1,4,10,-7,-10,3,8,-7,7,10,1,-2,-5,4,3,3,-3,-3,6,7,9,-4,-3,-10,9,10,3,9,-3,5,-2,-9,-7,7,-4,-1,-4,2,8,-8,3,8,-9,3,9,-9,-8,7,-3,-9,9,-10,7,-10,3,3,-7,-9,8,-10,1,2,-8,-5,1,7,-5,3,-6,-6,-3,2,-2,6,-6,8,6,7,7,6,-9,10,-8,6,9,5,-3,-2,2,4,6,5,2,-9,-5,8,8,8,2,1,5,3,-5,-2,5,-2,8,7,9,-10,1,-10,6,6,-1,-9,-5,6,-9,6,6,7,7,-5,-1,3,-3,-2,1,6,5,10,-10,-1,-7,-3,6,9,5,2,-9,10,7,10,8,-2,1,-4,-10,-10,-3,-10,-6,-2,2,-8,8,2,8,7,-8,-10,3,-4,10,-8,8,1,6,6,7,1,-2,3,7,-7,-9,5,-2,2,4,4,-9,-7,-8,5,7,-3,10,-10,-7,3,-3,-9,9,6,3,-5,-4,-9,3,8,-9,10,8,-6,8,-3,10,-5,-3,-10,2,-9,8,-9,-2,-3,-9,-2,-5,-3,10,4,-8,-6,-2,9,4,10,-6,2,-5,10,-10,-4,1,-7,-5,-10,2,6,-4,9,3,-7,10,8,6,1,10,-2,5,1,-2,3,-7,-9,-3,9,10,6,7,7,-4,1,6,-5,5,-8,-7,1,1,-4,-10,4,-1,10,-4,3,-5,-2,-10,-9,2,-3,2,4,-4,2,3,4,6,-2,-2,8,1,-8,6,-5,-9,-9,2,6,4,-2,4,1,-1,-10,-9,-10,-10,-9,-8,-7,5,-7,1,-5,-3,-4,-4,-5,-9,7,3,8,8,2,-4,-2,-6,7,6,6,8,6,-6,-6,6,-3,-3,-4,10,6,6,-4,10,-4,3,6,10,3,3,-1,3,9,6,-6,1,2,-9,-2,8,-5,-3,-2,1,9,5,4,-3,-3,-8,5,10,-7,-4,7,-4,-4,-3,10,-2,-9,-8,-6,-6,1,-7,-3,6,7,10,3,-8,3,-3,-7,-3,-1,-1,-3,5,1,10,2,-6,7,3,-2,-9,4,9,7,10,-2,-7,8,-8,-8,4,6,7,8,5,4,-6,-4,-2,6,10,-4,2,3,-2,-10,-8,-6,10,-8,-5,-9,-9,-5,-5,-4,8,6,-2,2,7,-10,-8,2,10,5,10,-8,8,-3,-2,-9,-7,-10,3,2,-2,7,-7,-10,-8,-6,-8,1,-6,8,-1,8,-4,-6,-10,5,9,4,10,4,-8], dtype = "uint8")#candidate|1570|(2145,)|const|uint8
call_1568 = relay.TupleGetItem(func_828_call(relay.reshape(const_1569.astype('uint8'), []), relay.reshape(const_1570.astype('uint8'), [15, 11, 13]), ), 1)
call_1571 = relay.TupleGetItem(func_832_call(relay.reshape(const_1569.astype('uint8'), []), relay.reshape(const_1570.astype('uint8'), [15, 11, 13]), ), 1)
output = relay.Tuple([call_1566,call_1568,const_1569,const_1570,])
output2 = relay.Tuple([call_1567,call_1571,const_1569,const_1570,])
func_1575 = relay.Function([], output)
mod['func_1575'] = func_1575
mod = relay.transform.InferType()(mod)
mutated_mod['func_1575'] = func_1575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1575_call = mutated_mod.get_global_var('func_1575')
call_1576 = func_1575_call()
output = call_1576
func_1577 = relay.Function([], output)
mutated_mod['func_1577'] = func_1577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1474_call = mod.get_global_var('func_1474')
func_1475_call = mutated_mod.get_global_var('func_1475')
call_1592 = relay.TupleGetItem(func_1474_call(), 0)
call_1593 = relay.TupleGetItem(func_1475_call(), 0)
output = call_1592
output2 = call_1593
func_1596 = relay.Function([], output)
mod['func_1596'] = func_1596
mod = relay.transform.InferType()(mod)
output = func_1596()
func_1597 = relay.Function([], output)
mutated_mod['func_1597'] = func_1597
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1614 = relay.var("var_1614", dtype = "bool", shape = ())#candidate|1614|()|var|bool
var_1615 = relay.var("var_1615", dtype = "bool", shape = (7, 10, 12))#candidate|1615|(7, 10, 12)|var|bool
bop_1616 = relay.logical_and(var_1614.astype('bool'), var_1615.astype('bool')) # shape=(7, 10, 12)
output = relay.Tuple([bop_1616,])
output2 = relay.Tuple([bop_1616,])
func_1642 = relay.Function([var_1614,var_1615,], output)
mod['func_1642'] = func_1642
mod = relay.transform.InferType()(mod)
var_1643 = relay.var("var_1643", dtype = "bool", shape = ())#candidate|1643|()|var|bool
var_1644 = relay.var("var_1644", dtype = "bool", shape = (7, 10, 12))#candidate|1644|(7, 10, 12)|var|bool
output = func_1642(var_1643,var_1644,)
func_1645 = relay.Function([var_1643,var_1644,], output)
mutated_mod['func_1645'] = func_1645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1575_call = mod.get_global_var('func_1575')
func_1577_call = mutated_mod.get_global_var('func_1577')
call_1672 = relay.TupleGetItem(func_1575_call(), 3)
call_1673 = relay.TupleGetItem(func_1577_call(), 3)
func_274_call = mod.get_global_var('func_274')
func_277_call = mutated_mod.get_global_var('func_277')
const_1690 = relay.const(-3, dtype = "uint16")#candidate|1690|()|const|uint16
call_1689 = func_274_call(relay.reshape(const_1690.astype('uint16'), []))
call_1691 = func_274_call(relay.reshape(const_1690.astype('uint16'), []))
func_1523_call = mod.get_global_var('func_1523')
func_1526_call = mutated_mod.get_global_var('func_1526')
var_1693 = relay.var("var_1693", dtype = "int32", shape = (110,))#candidate|1693|(110,)|var|int32
var_1694 = relay.var("var_1694", dtype = "int32", shape = (990,))#candidate|1694|(990,)|var|int32
call_1692 = relay.TupleGetItem(func_1523_call(relay.reshape(var_1693.astype('int32'), [1, 10, 11]), relay.reshape(var_1694.astype('int32'), [9, 10, 11]), ), 0)
call_1695 = relay.TupleGetItem(func_1526_call(relay.reshape(var_1693.astype('int32'), [1, 10, 11]), relay.reshape(var_1694.astype('int32'), [9, 10, 11]), ), 0)
func_857_call = mod.get_global_var('func_857')
func_860_call = mutated_mod.get_global_var('func_860')
var_1708 = relay.var("var_1708", dtype = "int16", shape = (55, 6))#candidate|1708|(55, 6)|var|int16
call_1707 = relay.TupleGetItem(func_857_call(relay.reshape(var_1708.astype('int16'), [11, 10, 3]), relay.reshape(var_1708.astype('int16'), [11, 10, 3]), ), 0)
call_1709 = relay.TupleGetItem(func_860_call(relay.reshape(var_1708.astype('int16'), [11, 10, 3]), relay.reshape(var_1708.astype('int16'), [11, 10, 3]), ), 0)
func_1642_call = mod.get_global_var('func_1642')
func_1645_call = mutated_mod.get_global_var('func_1645')
const_1726 = relay.const([True,False,True,True,False,True,True,True,True,False,True,True,True,True,True,False,True,True,False,False,True,True,False,False,True,True,True,False,False,True,False,True,False,True,True,False,True,False,True,False,False,True,True,False,False,False,False,True,True,False,False,False,True,False,True,False,True,False,False,True,False,False,True,False,False,False,False,True,False,True,True,False,False,False,False,True,True,False,False,False,False,False,True,True,True,False,True,False,False,True,False,False,False,True,False,False,True,False,True,True,False,False,True,False,False,False,True,True,False,False,False,True,False,True,False,True,True,False,False,True,True,False,False,True,True,False,True,False,True,False,True,True,False,False,True,True,False,True,False,True,True,False,False,True,True,False,True,False,False,True,False,False,True,False,True,False,False,True,False,True,True,True,False,False,True,False,True,False,True,True,True,False,False,True,True,True,True,False,False,False,True,False,False,False,False,True,False,False,False,False,False,False,True,False,False,True,False,True,True,True,False,False,True,False,True,True,False,False,True,False,False,True,False,False,True,False,False,False,False,False,False,False,False,False,True,False,True,True,True,False,True,False,False,False,False,True,True,False,True,True,False,False,False,False,False,True,False,False,True,True,True,False,True,True,False,False,False,True,False,True,True,True,True,True,True,False,False,True,False,True,False,True,True,False,True,False,True,False,False,True,True,True,True,False,True,True,True,True,False,True,False,True,False,False,False,True,False,False,False,False,True,False,True,True,False,True,True,False,True,True,True,False,True,False,False,False,True,True,True,True,False,True,False,False,True,False,False,True,False,False,False,True,True,True,False,True,False,True,True,True,True,False,True,False,False,False,False,True,True,True,False,False,False,False,False,False,False,False,True,False,True,True,False,False,True,False,True,True,False,True,True,True,True,False,True,False,False,True,True,False,False,False,False,False,False,False,False,True,True,False,True,False,True,True,False,False,False,True,False,False,False,True,True,False,True,False,False,False,True,True,False,True,True,False,True,False,False,False,True,True,False,False,True,True,False,True,False,False,True,False,False,True,True,True,True,False,True,True,False,False,True,False,True,False,False,False,False,True,False,True,False,False,False,False,False,False,True,False,False,False,False,False,False,True,True,True,True,False,True,False,False,False,False,True,False,True,True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,True,False,True,True,True,True,True,True,True,False,True,False,False,False,False,False,True,True,False,True,True,True,False,True,True,False,False,False,True,False,True,False,False,False,False,True,True,True,False,True,False,False,True,False,False,False,False,True,True,False,True,False,True,True,False,True,True,False,True,False,False,False,True,True,True,True,False,False,False,True,True,False,True,True,False,True,True,False,True,False,True,False,False,False,True,False,True,False,False,False,True,True,True,False,False,False,True,False,False,True,True,False,False,False,True,False,False,False,True,True,False,False,True,False,False,False,True,False,False,True,False,True,False,True,True,False,True,False,True,False,False,False,False,False,True,True,False,True,True,True,False,True,True,True,True,False,True,False,False,True,False,False,True,False,False,False,True,True,True,False,True,True,False,True,True,True,False,True,False,True,True,False,False,False,True,False,False,False,False,False,False,False,True,True,True,True,True,False,False,False,False,False,True,False,True,False,False,False,False,False,True,True,True,False,True,False,False,False,True,False,False,True,True,True,False,False,False,True,False,True,False,False,True,True,False,False,False,False,False,False,True,False,True,False,False,False,False,False,False,True,False,True,False,True,False,False,True,True,False,True,False,False,True,True,True,False,True,True,False,False,True,True,False,False,True,False,True,False,False,True,True,False,False,False,False,True,False,True,False,False,True,False,False,False,True,False,False,False,True,True,False,True,False,False,True,False,False,False,False,False,False,True,True,False,True,True,True,False,False,True,False,True,True,True,False,False,True,False,True,False,True,True,True,False,False,True,False,False,True,False,True,True,True,False,False,True,True,True,True,True,True,True,True,False,False], dtype = "bool")#candidate|1726|(840,)|const|bool
call_1725 = relay.TupleGetItem(func_1642_call(relay.reshape(const_1690.astype('bool'), []), relay.reshape(const_1726.astype('bool'), [7, 10, 12]), ), 0)
call_1727 = relay.TupleGetItem(func_1645_call(relay.reshape(const_1690.astype('bool'), []), relay.reshape(const_1726.astype('bool'), [7, 10, 12]), ), 0)
func_828_call = mod.get_global_var('func_828')
func_832_call = mutated_mod.get_global_var('func_832')
call_1736 = relay.TupleGetItem(func_828_call(relay.reshape(const_1690.astype('uint8'), []), relay.reshape(call_1672.astype('uint8'), [15, 11, 13]), ), 0)
call_1737 = relay.TupleGetItem(func_832_call(relay.reshape(const_1690.astype('uint8'), []), relay.reshape(call_1672.astype('uint8'), [15, 11, 13]), ), 0)
var_1745 = relay.var("var_1745", dtype = "int16", shape = (11, 10, 3))#candidate|1745|(11, 10, 3)|var|int16
bop_1746 = relay.power(call_1707.astype('float64'), relay.reshape(var_1745.astype('float64'), relay.shape_of(call_1707))) # shape=(11, 10, 3)
bop_1749 = relay.power(call_1709.astype('float64'), relay.reshape(var_1745.astype('float64'), relay.shape_of(call_1709))) # shape=(11, 10, 3)
output = relay.Tuple([call_1672,call_1689,const_1690,call_1692,var_1693,var_1694,var_1708,call_1725,const_1726,call_1736,bop_1746,])
output2 = relay.Tuple([call_1673,call_1691,const_1690,call_1695,var_1693,var_1694,var_1708,call_1727,const_1726,call_1737,bop_1749,])
func_1760 = relay.Function([var_1693,var_1694,var_1708,var_1745,], output)
mod['func_1760'] = func_1760
mod = relay.transform.InferType()(mod)
mutated_mod['func_1760'] = func_1760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1760_call = mutated_mod.get_global_var('func_1760')
var_1762 = relay.var("var_1762", dtype = "int32", shape = (110,))#candidate|1762|(110,)|var|int32
var_1763 = relay.var("var_1763", dtype = "int32", shape = (990,))#candidate|1763|(990,)|var|int32
var_1764 = relay.var("var_1764", dtype = "int16", shape = (55, 6))#candidate|1764|(55, 6)|var|int16
var_1765 = relay.var("var_1765", dtype = "int16", shape = (11, 10, 3))#candidate|1765|(11, 10, 3)|var|int16
call_1761 = func_1760_call(var_1762,var_1763,var_1764,var_1765,)
output = call_1761
func_1766 = relay.Function([var_1762,var_1763,var_1764,var_1765,], output)
mutated_mod['func_1766'] = func_1766
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1474_call = mod.get_global_var('func_1474')
func_1475_call = mutated_mod.get_global_var('func_1475')
call_1791 = relay.TupleGetItem(func_1474_call(), 0)
call_1792 = relay.TupleGetItem(func_1475_call(), 0)
var_1798 = relay.var("var_1798", dtype = "float64", shape = (8, 3, 10))#candidate|1798|(8, 3, 10)|var|float64
bop_1799 = relay.floor_mod(call_1791.astype('float64'), relay.reshape(var_1798.astype('float64'), relay.shape_of(call_1791))) # shape=(8, 3, 10)
bop_1802 = relay.floor_mod(call_1792.astype('float64'), relay.reshape(var_1798.astype('float64'), relay.shape_of(call_1792))) # shape=(8, 3, 10)
uop_1803 = relay.log(call_1791.astype('float32')) # shape=(8, 3, 10)
uop_1805 = relay.log(call_1792.astype('float32')) # shape=(8, 3, 10)
output = relay.Tuple([bop_1799,uop_1803,])
output2 = relay.Tuple([bop_1802,uop_1805,])
func_1808 = relay.Function([var_1798,], output)
mod['func_1808'] = func_1808
mod = relay.transform.InferType()(mod)
var_1809 = relay.var("var_1809", dtype = "float64", shape = (8, 3, 10))#candidate|1809|(8, 3, 10)|var|float64
output = func_1808(var_1809)
func_1810 = relay.Function([var_1809], output)
mutated_mod['func_1810'] = func_1810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1575_call = mod.get_global_var('func_1575')
func_1577_call = mutated_mod.get_global_var('func_1577')
call_1854 = relay.TupleGetItem(func_1575_call(), 2)
call_1855 = relay.TupleGetItem(func_1577_call(), 2)
output = call_1854
output2 = call_1855
func_1861 = relay.Function([], output)
mod['func_1861'] = func_1861
mod = relay.transform.InferType()(mod)
mutated_mod['func_1861'] = func_1861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1861_call = mutated_mod.get_global_var('func_1861')
call_1862 = func_1861_call()
output = call_1862
func_1863 = relay.Function([], output)
mutated_mod['func_1863'] = func_1863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1596_call = mod.get_global_var('func_1596')
func_1597_call = mutated_mod.get_global_var('func_1597')
call_1895 = func_1596_call()
call_1896 = func_1596_call()
output = call_1895
output2 = call_1896
func_1910 = relay.Function([], output)
mod['func_1910'] = func_1910
mod = relay.transform.InferType()(mod)
output = func_1910()
func_1911 = relay.Function([], output)
mutated_mod['func_1911'] = func_1911
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1928 = relay.var("var_1928", dtype = "float32", shape = (12, 13, 2))#candidate|1928|(12, 13, 2)|var|float32
uop_1929 = relay.rsqrt(var_1928.astype('float32')) # shape=(12, 13, 2)
func_1596_call = mod.get_global_var('func_1596')
func_1597_call = mutated_mod.get_global_var('func_1597')
call_1939 = func_1596_call()
call_1940 = func_1596_call()
output = relay.Tuple([uop_1929,call_1939,])
output2 = relay.Tuple([uop_1929,call_1940,])
func_1948 = relay.Function([var_1928,], output)
mod['func_1948'] = func_1948
mod = relay.transform.InferType()(mod)
var_1949 = relay.var("var_1949", dtype = "float32", shape = (12, 13, 2))#candidate|1949|(12, 13, 2)|var|float32
output = func_1948(var_1949)
func_1950 = relay.Function([var_1949], output)
mutated_mod['func_1950'] = func_1950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1910_call = mod.get_global_var('func_1910')
func_1911_call = mutated_mod.get_global_var('func_1911')
call_1966 = func_1910_call()
call_1967 = func_1910_call()
output = relay.Tuple([call_1966,])
output2 = relay.Tuple([call_1967,])
func_1975 = relay.Function([], output)
mod['func_1975'] = func_1975
mod = relay.transform.InferType()(mod)
output = func_1975()
func_1976 = relay.Function([], output)
mutated_mod['func_1976'] = func_1976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1975_call = mod.get_global_var('func_1975')
func_1976_call = mutated_mod.get_global_var('func_1976')
call_2038 = relay.TupleGetItem(func_1975_call(), 0)
call_2039 = relay.TupleGetItem(func_1976_call(), 0)
func_828_call = mod.get_global_var('func_828')
func_832_call = mutated_mod.get_global_var('func_832')
var_2044 = relay.var("var_2044", dtype = "uint8", shape = ())#candidate|2044|()|var|uint8
const_2045 = relay.const([5,4,-10,4,5,4,-9,-6,10,-1,-9,1,1,-3,4,6,-6,9,-1,9,-10,-5,-4,7,-10,-7,7,-10,-3,9,3,-5,6,-4,6,6,-6,4,9,4,-2,-10,-10,-5,-5,8,-2,8,-8,6,8,1,2,-6,7,-2,-2,7,-5,4,-9,-10,9,10,2,5,-9,-6,10,-3,1,-5,10,-6,6,-6,6,7,-6,7,2,-10,6,1,-5,4,-10,2,5,-4,1,6,-8,5,10,1,-3,3,6,-7,8,8,4,-7,-9,-8,3,-8,-8,2,-4,-2,-4,8,8,-1,-9,-4,1,10,4,-8,3,-7,-8,3,-2,9,-9,-7,2,-5,9,2,3,-9,1,6,-3,8,-2,3,3,3,9,-1,8,-2,7,6,-9,1,-2,5,-9,-7,2,-6,-4,-9,9,-3,-7,-3,-2,-8,-5,10,-5,-5,6,5,1,-4,-10,-7,-2,5,9,6,10,2,-3,5,5,-2,1,8,-3,-9,5,2,-8,9,-7,-9,-8,-4,-1,-9,-6,-7,10,-9,6,-6,3,8,-6,-1,1,2,10,10,-3,-8,-2,6,-10,5,-4,-9,-2,10,-4,-3,-10,-4,-2,-10,5,-6,2,-9,8,10,-6,10,-4,5,9,4,-6,-8,7,5,-7,-7,4,3,9,-7,10,4,-6,-5,9,-4,2,-5,-3,8,-1,3,10,-1,-9,5,-4,7,-8,-6,-4,3,-4,4,9,9,7,-7,-10,-8,-9,-2,10,4,4,6,-10,-5,-5,4,-10,-4,-7,-4,1,7,4,4,9,-1,-6,10,-6,-2,3,-5,-1,10,1,-6,-5,-6,-2,-3,6,3,-3,-10,7,9,8,-3,-4,6,6,-2,4,-1,6,-7,-2,-6,3,-3,8,2,-8,4,9,-9,-1,-9,-9,-1,-6,9,9,4,-3,-2,-1,-6,3,-2,9,9,-2,-7,9,-6,-6,-5,-10,7,-8,-4,-7,-7,-2,3,10,-3,8,-3,-8,4,-6,1,9,-1,8,5,6,6,-3,-9,-8,-5,-2,3,-1,-4,-5,-3,4,3,-9,-9,-2,-3,1,8,-4,-8,-5,-4,8,-3,6,9,-10,-4,-3,-6,-6,-2,10,-8,6,1,-7,-6,-7,-9,-5,-3,-3,5,-9,-2,1,6,5,8,-10,-3,-5,3,7,5,4,-8,8,-4,-6,4,2,9,-3,-1,5,1,10,-2,-10,1,-8,1,-4,-2,1,8,-3,-3,5,9,-5,-9,-8,3,1,-10,-3,-6,-7,-7,-4,4,-3,6,-10,-7,-9,1,9,-5,-10,-1,7,-9,-8,3,-1,-3,-3,-10,6,-7,4,-2,3,-5,-2,5,-6,4,-1,7,-3,6,-9,-8,-4,2,4,-2,1,10,-4,5,-1,3,5,6,10,3,-10,6,5,-1,2,-5,-1,-8,-2,-2,-1,9,-4,-3,8,-4,6,-2,8,7,-7,2,-7,-2,3,-4,-10,10,9,-10,1,3,6,8,9,1,-8,-5,-5,-6,10,3,-4,-5,6,7,-1,-5,-6,-8,-8,2,-6,-3,-3,-7,10,4,-3,-4,-6,8,-3,-4,-8,7,-5,-4,-7,10,-5,-4,7,8,9,-8,-6,4,-1,-10,3,5,-8,9,-5,5,7,4,5,3,5,-1,-10,-10,-3,10,-10,8,-1,1,-7,5,-6,-10,-2,-7,8,7,2,1,-8,3,-5,5,-7,1,5,-10,6,1,4,-6,-5,10,-8,3,9,5,-9,9,1,2,9,-6,-1,-4,7,7,1,-9,6,9,2,-1,-6,-6,2,2,1,6,-7,9,10,-3,-3,4,-8,7,8,-8,-10,-3,6,4,3,9,2,-3,-6,-5,-1,-8,-1,9,-7,-6,-3,9,-4,7,5,-9,-8,1,-9,2,-5,-10,-9,8,6,-1,2,-10,-5,4,-7,-8,5,6,6,-5,8,7,-2,3,8,-9,-6,-5,-8,-4,3,-9,-1,-4,2,-8,-3,-10,-2,5,9,-8,-4,7,-5,-8,-4,9,-1,4,4,-8,9,-4,-10,-10,-4,3,5,-2,2,-1,9,4,4,-5,-2,-5,-8,-3,-7,-9,-3,-9,-6,-9,2,-7,-9,-1,8,1,-9,-10,-5,-7,-6,-5,3,-7,6,-7,3,1,4,-7,10,-10,-6,5,-3,-6,-1,8,-5,-2,1,1,-5,8,-6,2,2,-4,4,10,2,-6,4,-6,9,2,-1,-3,-7,8,5,1,3,8,5,-3,-3,-9,-3,10,6,1,6,4,5,9,1,1,-5,1,8,-6,-5,10,1,9,1,-3,-3,10,-8,-2,-9,2,4,6,7,3,-7,9,4,-5,7,-3,6,2,2,-2,-9,-7,-10,-4,-4,-1,1,-9,8,-3,-2,9,10,2,5,5,10,6,-6,7,7,-9,5,-5,-3,-2,-5,-5,-10,6,-10,-9,2,10,-4,-8,-2,1,-6,-4,5,4,-5,-4,5,-10,1,-7,5,-3,-2,-1,-7,-4,9,1,-4,-5,-5,3,6,-7,5,10,-9,8,-3,8,1,2,-1,-5,10,-3,-6,-5,2,-9,-5,-6,3,8,4,5,-9,7,-2,7,10,-8,-8,1,6,6,1,8,9,10,-1,1,2,3,10,-7,-2,9,10,10,1,9,-2,-8,2,-4,-2,4,3,-9,7,-5,1,-9,-3,-8,8,8,4,-1,-5,9,2,-1,-1,9,-6,-7,8,1,4,10,7,-2,-6,-7,-9,-8,10,-9,-10,6,-5,-7,8,6,5,6,6,5,2,-2,-8,6,-10,6,-5,7,7,3,-10,-9,-5,-1,4,2,7,1,-2,3,3,-3,-2,-8,-6,4,10,-3,10,-5,-9,4,-10,-3,-3,-6,4,7,-2,6,-6,4,-8,2,-2,-4,-5,-8,3,-9,8,5,9,-1,-6,8,9,-7,-10,5,-7,4,-9,-9,6,1,5,7,7,-4,-4,3,4,-10,-1,6,-6,-10,-5,-7,6,6,-3,7,10,3,4,7,9,2,-4,8,3,7,6,10,4,-5,-8,9,4,9,-9,5,4,6,8,-2,-3,-8,4,2,3,-5,10,6,-5,1,3,-9,-5,-7,-10,-5,-7,-3,10,-9,3,-3,-7,8,-8,-7,6,8,-3,-6,5,8,-4,-2,-6,-9,-4,-3,-5,-6,-1,4,9,1,-6,-6,8,-2,7,-9,5,-4,-2,4,10,-10,3,10,-3,-3,-10,1,-7,10,-7,6,9,-4,9,-8,-10,-7,10,4,-8,4,7,6,8,-5,9,8,-5,6,-10,10,3,-2,7,-6,-2,5,-8,1,-10,-3,-2,-4,-3,1,-5,5,10,-10,-3,4,-1,-5,1,-4,-6,8,8,-5,4,-8,6,-8,-3,3,-7,3,7,6,6,9,-7,-8,-10,-9,8,5,1,10,4,-9,-10,6,10,5,1,6,10,-6,10,7,1,1,7,-5,3,-1,-8,-10,10,4,7,1,7,-2,-1,2,2,5,5,10,3,2,-10,-10,8,-2,-6,-4,2,-8,4,-6,-5,8,8,9,1,5,-4,2,8,6,-8,-5,-8,-3,4,1,-10,-9,-6,4,-2,7,-3,-7,-4,5,7,2,4,10,-7,-5,-9,-7,-5,-10,-9,2,-7,-3,5,-3,-7,-10,2,-6,10,-8,-8,-1,6,-1,-10,7,5,8,-7,4,8,4,1,-9,-3,-7,-3,-7,2,4,-10,-1,2,-7,-2,2,3,10,-5,-5,7,1,-4,9,-6,-10,-5,-3,10,-5,-9,2,10,-7,2,-5,-6,9,7,-6,10,-1,-6,-1,6,-1,-10,6,7,-8,5,-10,-4,-3,-6,5,-6,2,-3,-10,-8,4,8,-1,-3,-5,-4,1,5,-10,4,8,2,-4,2,3,-9,-9,7,1,9,-10,3,3,-7,9,-6,3,-7,-4,5,1,6,-8,-10,-5,-4,-3,8,7,9,-9,4,-5,-3,10,-8,-9,-10,7,5,-10,7,-8,-1,2,-8,7,5,3,-2,-5,5,-3,10,-7,-2,-3,-4,5,3,-5,8,-5,3,2,-4,-6,-2,5,10,6,3,-2,2,2,5,-10,-9,-8,4,10,9,-6,4,3,-5,8,2,-3,-7,2,4,3,-9,-8,2,-1,-1,-2,-10,10,5,3,8,-4,5,-7,7,2,2,9,5,5,-10,-4,-1,8,-2,5,-1,5,4,4,-1,-7,4,6,-9,9,7,2,8,4,-4,-2,-8,10,-10,-3,-9,-5,-10,6,2,-1,-9,-7,-4,6,9,-3,-6,9,7,6,-4,-3,-2,4,-2,-4,-7,-7,3,-8,-3,1,6,-5,2,1,4,10,2,-3,8,-5,-8,5,8,-4,-6,10,5,-7,1,-4,-3,-1,8,-7,-1,1,-5,-3,-2,3,3,2,-1,6,-6,-6,-7,-3,-1,5,-5,3,5,-2,-2,6,8,-3,6,2,-4,-4,7,9,-8,-2,-1,2,3,-4,8,-10,8,9,7,-10,2,-3,1,-9,-6,-1,-7,2,6,-5,-6,3,2,-1,-3,-1,5,4,-6,7,5,9,-1,-2,-9,-1,5,8,-6,-8,10,-6,3,-4,-4,-3,7,10,4,-4,2,5,-9,-7,-4,6,6,2,1,-8,-5,5,-4,-9,-1,-1,-8,2,-1,-2,6,10,7,3,6,-6,-4,-4,-8,-5,3,1,2,9,-4,10,-9,4,-2,6,8,-10,5,-1,6,9,3,3,3,1,-2,-9,-3,7,-10,5,6,-2,-1,3,8,7,4,-7,3,-6,8,6,-8,7,7,-6,9,-8,-1,-8,-5,-10,-6,-9,4,-3,-1,-6,-3,9,-4,7,-2,-4,5,2,8,8,1,-2,-3,9,-4,-6,-7,9,9,7,-8,-6,2,3,-2,-3,-10,-7,-9,-10,-1,-2,-1,-10,-8,4,7,-10,-8,10,-6,10,-7,1,-3,-3,-9,-3,-7,-1,-9,2,4,8,5,-9,-10,-8,-8,-6,-2,-5,3,9,10,-6,6,-8,10,-2,3,-5,-2,3,2,9,8,4,2,3,5,3,-7,-2,9,9,5,7,9,-7,9,6,4,7,3,-7,9,-2,5,3,-7,-5,8,-4,-10,-7,-1,-6,-3,8,-3,8,9,10,3,-7,6,5,-2,9,9,2,-1,4,1,1,9,8,9,-3,9,-3,9,-9,8,-6,-5,9,-9,9,-3,6,2,-1,1,-3,3,7,5,-5,-1,-10,-1,2,1,10,4,7,9,6,3,10,7,-8,-3,-5,-7,-3,-5,-8,6,2,5,5,9,-4,3,8,1,-4,2,1,6,8,8,-10,8,-4,1,-5,-5,5,-2,7,1,-10,-1,-2,4,2,10,6,-4,-8,-4,-7,3,6,-5,1,-4,-10,-3,-6,4,8,-10,9,7,-10,2,9,-9,1,7,1,4,-8,6,5,-4,4,-9,7,-2,-8,-6,2,-9,-1,-6,8,6,8,-2,1,-5,-9,10,2,-4,-8,7,-8,-2,1,-3,-7,-6,2,7,-3,8,9,-7,2,3,-2,8,5,8,8,-8,2,-8,-2,-8,9,7,6,1,5,-5,-4,-6,-5,-6,6,7,-10,2,10,-6,-6,9,7,9,3,9,-1,6,-9,-8,-8,5,-10,9,7,-10,-10,-6,-6,1,8,-7,-4,4,7,10,-7,-3,-2,-6,10,3,-3,-7,1,-8,-7,-10], dtype = "uint8")#candidate|2045|(2145,)|const|uint8
call_2043 = relay.TupleGetItem(func_828_call(relay.reshape(var_2044.astype('uint8'), []), relay.reshape(const_2045.astype('uint8'), [15, 11, 13]), ), 1)
call_2046 = relay.TupleGetItem(func_832_call(relay.reshape(var_2044.astype('uint8'), []), relay.reshape(const_2045.astype('uint8'), [15, 11, 13]), ), 1)
bop_2054 = relay.multiply(const_2045.astype('uint32'), var_2044.astype('uint32')) # shape=(2145,)
func_274_call = mod.get_global_var('func_274')
func_277_call = mutated_mod.get_global_var('func_277')
call_2060 = func_274_call(relay.reshape(var_2044.astype('uint16'), []))
call_2061 = func_274_call(relay.reshape(var_2044.astype('uint16'), []))
output = relay.Tuple([call_2038,call_2043,bop_2054,call_2060,])
output2 = relay.Tuple([call_2039,call_2046,bop_2054,call_2061,])
func_2063 = relay.Function([var_2044,], output)
mod['func_2063'] = func_2063
mod = relay.transform.InferType()(mod)
mutated_mod['func_2063'] = func_2063
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2064 = relay.var("var_2064", dtype = "uint8", shape = ())#candidate|2064|()|var|uint8
func_2063_call = mutated_mod.get_global_var('func_2063')
call_2065 = func_2063_call(var_2064)
output = call_2065
func_2066 = relay.Function([var_2064], output)
mutated_mod['func_2066'] = func_2066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1861_call = mod.get_global_var('func_1861')
func_1863_call = mutated_mod.get_global_var('func_1863')
call_2078 = func_1861_call()
call_2079 = func_1861_call()
func_828_call = mod.get_global_var('func_828')
func_832_call = mutated_mod.get_global_var('func_832')
var_2102 = relay.var("var_2102", dtype = "uint8", shape = (2145,))#candidate|2102|(2145,)|var|uint8
call_2101 = relay.TupleGetItem(func_828_call(relay.reshape(call_2078.astype('uint8'), []), relay.reshape(var_2102.astype('uint8'), [15, 11, 13]), ), 1)
call_2103 = relay.TupleGetItem(func_832_call(relay.reshape(call_2078.astype('uint8'), []), relay.reshape(var_2102.astype('uint8'), [15, 11, 13]), ), 1)
func_1948_call = mod.get_global_var('func_1948')
func_1950_call = mutated_mod.get_global_var('func_1950')
const_2108 = relay.const([-2.761033,2.583890,0.403373,-6.509884,-4.916494,0.862297,-8.156547,2.942728,-1.888976,-1.188599,6.677741,1.877841,4.225000,-5.144807,5.889439,4.215498,1.380994,8.057888,4.854647,-2.838183,-0.200023,2.120511,-2.654835,4.913163,-8.250552,-9.455243,0.548719,6.944823,-2.250252,7.822003,-7.050239,2.289206,-6.450269,-4.197067,7.416471,8.384267,-2.499271,-0.952342,-3.172428,-7.222981,0.247539,-6.829429,-9.645371,-1.400173,6.345755,8.893043,-5.008864,-5.332330,8.970477,-4.798894,6.288228,-3.734489,-4.210846,-9.459854,-4.370699,-6.609198,-8.932273,-6.400690,-8.304429,6.860596,2.281808,9.459913,-5.272994,-2.651459,6.434256,-9.282339,-1.165879,-8.728024,0.368075,8.000478,1.567930,-5.084050,-6.939435,2.357557,7.176547,5.349618,5.833703,-3.617589,-1.114918,2.835353,-6.684132,-2.490778,-7.895410,0.900440,-0.176137,-6.019809,-2.328547,0.734974,4.617775,9.400499,2.150176,8.369496,-7.961149,-4.812873,-0.719501,-2.484850,8.874760,-8.218134,2.857055,-5.564876,-6.059742,-9.045502,4.666221,-1.408140,-0.279484,0.470281,-6.459436,-0.907976,-2.697815,7.435129,-0.467366,2.404038,-4.697979,2.987692,-8.771857,4.035159,-4.978210,0.672208,8.756832,7.832187,-7.018844,-4.819129,2.289581,3.011013,7.261905,1.931563,-6.714082,-0.110035,-9.847051,-3.994432,7.638375,9.883002,0.077266,1.134201,-8.068648,-8.840567,3.063242,6.118692,2.203233,-6.602946,7.012215,-1.365332,0.553841,5.491857,8.842872,-5.657290,7.287508,-5.767117,-8.135537,-5.451791,-9.661688,4.369477,1.576881,4.917743,7.012761,5.809017,2.461605,-6.207412,-3.347316,-1.652897,-3.774089,-5.733709,-0.569463,-8.405573,-0.214561,-0.069730,-9.679136,-7.711331,-8.524531,-7.143847,-2.486186,4.317464,-2.068307,-0.625042,3.826697,-9.112666,0.220375,0.380606,6.758108,-2.328071,-1.235872,6.874621,0.007309,-6.939463,8.452232,0.398524,2.804777,4.302441,9.680736,-8.979185,-3.170021,-0.178446,-6.636101,7.716701,2.141949,3.647240,-4.536099,-7.423787,7.235250,-1.624198,-4.944201,-5.292338,-2.298954,8.402620,6.598284,-3.904893,-1.176360,9.578015,-1.102396,-2.559228,-8.469084,-1.617101,-2.428852,-7.594116,9.359119,-0.798277,5.773383,8.407709,-3.644018,7.234335,4.745830,6.140208,-7.725811,-1.675482,-2.924348,-9.805279,-7.934112,9.016778,-8.953938,-7.391530,-8.189153,8.183801,4.541252,3.572037,9.585725,4.237836,-8.821683,-0.413570,0.355830,-2.876683,5.213018,1.653980,9.099468,1.260905,-8.978510,5.786269,-2.681754,-3.202875,-5.831952,-0.953606,-6.418121,-1.503837,-5.157981,4.159630,7.970020,7.827050,6.938926,-5.507337,-4.442415,-4.809384,-4.219197,2.847728,-3.796170,-4.388332,-4.116437,-1.472050,7.498864,3.660069,4.223154,2.116493,-7.439866,7.453233,8.881060,-3.522728,4.168876,1.937420,4.730976,1.352904,-8.141144,-4.947996,-2.968168,-7.631751,6.231249,0.783928,-2.944523,0.574115,-6.348681,-1.636120,-1.196664,8.796912,3.336108,5.943628,9.404172,-0.758020,5.621433,-7.203640,0.133534,0.551000,2.624257,8.228712,5.167253,-5.281529,-1.363350,-0.200186,-5.354555,-3.127978,-6.832937,-2.181494,-4.956804,9.499190,2.440849,3.381344], dtype = "float32")#candidate|2108|(312,)|const|float32
call_2107 = relay.TupleGetItem(func_1948_call(relay.reshape(const_2108.astype('float32'), [12, 13, 2])), 0)
call_2109 = relay.TupleGetItem(func_1950_call(relay.reshape(const_2108.astype('float32'), [12, 13, 2])), 0)
func_2063_call = mod.get_global_var('func_2063')
func_2066_call = mutated_mod.get_global_var('func_2066')
call_2110 = relay.TupleGetItem(func_2063_call(relay.reshape(call_2078.astype('uint8'), [])), 3)
call_2111 = relay.TupleGetItem(func_2066_call(relay.reshape(call_2078.astype('uint8'), [])), 3)
bop_2135 = relay.minimum(call_2110.astype('uint8'), call_2078.astype('uint8')) # shape=(12, 2, 1)
bop_2138 = relay.minimum(call_2111.astype('uint8'), call_2079.astype('uint8')) # shape=(12, 2, 1)
func_1596_call = mod.get_global_var('func_1596')
func_1597_call = mutated_mod.get_global_var('func_1597')
call_2146 = func_1596_call()
call_2147 = func_1596_call()
output = relay.Tuple([call_2101,var_2102,call_2107,const_2108,bop_2135,call_2146,])
output2 = relay.Tuple([call_2103,var_2102,call_2109,const_2108,bop_2138,call_2147,])
func_2150 = relay.Function([var_2102,], output)
mod['func_2150'] = func_2150
mod = relay.transform.InferType()(mod)
var_2151 = relay.var("var_2151", dtype = "uint8", shape = (2145,))#candidate|2151|(2145,)|var|uint8
output = func_2150(var_2151)
func_2152 = relay.Function([var_2151], output)
mutated_mod['func_2152'] = func_2152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1861_call = mod.get_global_var('func_1861')
func_1863_call = mutated_mod.get_global_var('func_1863')
call_2159 = func_1861_call()
call_2160 = func_1861_call()
output = call_2159
output2 = call_2160
func_2166 = relay.Function([], output)
mod['func_2166'] = func_2166
mod = relay.transform.InferType()(mod)
output = func_2166()
func_2167 = relay.Function([], output)
mutated_mod['func_2167'] = func_2167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1975_call = mod.get_global_var('func_1975')
func_1976_call = mutated_mod.get_global_var('func_1976')
call_2238 = relay.TupleGetItem(func_1975_call(), 0)
call_2239 = relay.TupleGetItem(func_1976_call(), 0)
uop_2247 = relay.erf(call_2238.astype('float32')) # shape=(8, 3, 10)
uop_2249 = relay.erf(call_2239.astype('float32')) # shape=(8, 3, 10)
output = uop_2247
output2 = uop_2249
func_2256 = relay.Function([], output)
mod['func_2256'] = func_2256
mod = relay.transform.InferType()(mod)
mutated_mod['func_2256'] = func_2256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2256_call = mutated_mod.get_global_var('func_2256')
call_2257 = func_2256_call()
output = call_2257
func_2258 = relay.Function([], output)
mutated_mod['func_2258'] = func_2258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2256_call = mod.get_global_var('func_2256')
func_2258_call = mutated_mod.get_global_var('func_2258')
call_2274 = func_2256_call()
call_2275 = func_2256_call()
output = relay.Tuple([call_2274,])
output2 = relay.Tuple([call_2275,])
func_2276 = relay.Function([], output)
mod['func_2276'] = func_2276
mod = relay.transform.InferType()(mod)
mutated_mod['func_2276'] = func_2276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2276_call = mutated_mod.get_global_var('func_2276')
call_2277 = func_2276_call()
output = call_2277
func_2278 = relay.Function([], output)
mutated_mod['func_2278'] = func_2278
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2285 = relay.var("var_2285", dtype = "uint32", shape = (9, 5, 2))#candidate|2285|(9, 5, 2)|var|uint32
const_2286 = relay.const([[[-1,10],[-4,-5],[-4,10],[-5,8],[4,-6]],[[-10,5],[8,-3],[6,-3],[-6,-2],[3,-9]],[[6,-1],[-8,10],[-4,-3],[9,-4],[-1,-4]],[[-10,-4],[1,5],[3,-3],[5,10],[4,5]],[[10,2],[6,-8],[4,-4],[10,-9],[5,-7]],[[1,-7],[-5,-10],[-1,-4],[-3,-10],[-2,-7]],[[-10,-1],[2,3],[7,4],[-1,6],[10,-2]],[[-3,9],[5,-6],[-8,5],[8,8],[9,7]],[[-3,-6],[2,10],[-8,-2],[-3,8],[10,6]]], dtype = "uint32")#candidate|2286|(9, 5, 2)|const|uint32
bop_2287 = relay.left_shift(var_2285.astype('uint32'), relay.reshape(const_2286.astype('uint32'), relay.shape_of(var_2285))) # shape=(9, 5, 2)
output = relay.Tuple([bop_2287,])
output2 = relay.Tuple([bop_2287,])
func_2301 = relay.Function([var_2285,], output)
mod['func_2301'] = func_2301
mod = relay.transform.InferType()(mod)
var_2302 = relay.var("var_2302", dtype = "uint32", shape = (9, 5, 2))#candidate|2302|(9, 5, 2)|var|uint32
output = func_2301(var_2302)
func_2303 = relay.Function([var_2302], output)
mutated_mod['func_2303'] = func_2303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2276_call = mod.get_global_var('func_2276')
func_2278_call = mutated_mod.get_global_var('func_2278')
call_2307 = relay.TupleGetItem(func_2276_call(), 0)
call_2308 = relay.TupleGetItem(func_2278_call(), 0)
output = relay.Tuple([call_2307,])
output2 = relay.Tuple([call_2308,])
func_2318 = relay.Function([], output)
mod['func_2318'] = func_2318
mod = relay.transform.InferType()(mod)
output = func_2318()
func_2319 = relay.Function([], output)
mutated_mod['func_2319'] = func_2319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2256_call = mod.get_global_var('func_2256')
func_2258_call = mutated_mod.get_global_var('func_2258')
call_2404 = func_2256_call()
call_2405 = func_2256_call()
func_2276_call = mod.get_global_var('func_2276')
func_2278_call = mutated_mod.get_global_var('func_2278')
call_2409 = relay.TupleGetItem(func_2276_call(), 0)
call_2410 = relay.TupleGetItem(func_2278_call(), 0)
uop_2438 = relay.sinh(call_2404.astype('float64')) # shape=(8, 3, 10)
uop_2440 = relay.sinh(call_2405.astype('float64')) # shape=(8, 3, 10)
func_274_call = mod.get_global_var('func_274')
func_277_call = mutated_mod.get_global_var('func_277')
const_2445 = relay.const(1, dtype = "uint16")#candidate|2445|()|const|uint16
call_2444 = func_274_call(relay.reshape(const_2445.astype('uint16'), []))
call_2446 = func_274_call(relay.reshape(const_2445.astype('uint16'), []))
func_828_call = mod.get_global_var('func_828')
func_832_call = mutated_mod.get_global_var('func_832')
var_2451 = relay.var("var_2451", dtype = "uint8", shape = (2145,))#candidate|2451|(2145,)|var|uint8
call_2450 = relay.TupleGetItem(func_828_call(relay.reshape(const_2445.astype('uint8'), []), relay.reshape(var_2451.astype('uint8'), [15, 11, 13]), ), 1)
call_2452 = relay.TupleGetItem(func_832_call(relay.reshape(const_2445.astype('uint8'), []), relay.reshape(var_2451.astype('uint8'), [15, 11, 13]), ), 1)
func_1239_call = mod.get_global_var('func_1239')
func_1241_call = mutated_mod.get_global_var('func_1241')
const_2464 = relay.const([[4.740574],[-8.840542],[-6.791018],[-0.587924],[-1.199505],[7.143789],[-5.736740],[6.930395],[-1.106294],[-0.241228],[0.717963],[7.050357],[8.911514],[-3.119191],[0.381489],[3.608503],[0.267848],[0.741699],[5.419226],[-2.557677],[6.928309],[-0.310408],[-8.662893],[-2.676440],[-5.258392],[3.576697],[8.774399],[-1.199351],[1.620117],[0.010800],[-7.524207],[1.011912],[-4.179478],[5.489518],[5.323603],[7.362701],[1.902085],[-2.681534],[2.845123],[0.017794],[-8.995829],[4.835581],[7.426268],[-5.842879],[-0.869618],[-9.368537],[-3.796978],[-8.427050],[-5.954206],[-7.982409],[2.706479],[2.240926],[0.102027],[-4.956429],[-2.513794],[-8.031115],[7.110850],[1.034448],[-7.058212],[5.234286],[5.365843],[0.298915],[-8.925477],[-2.434036],[6.705804],[-4.997432],[-4.587358],[8.406727],[6.518065],[-0.121797],[7.018927],[-0.197824],[8.499656],[-6.040956],[6.992695],[-7.490822],[7.899303],[-3.367354],[-4.973605],[-9.163628],[5.776125],[-0.912826],[-2.339401],[5.857131],[-0.524460],[-0.904743],[9.907819],[-7.915343],[-3.132544],[-5.415407],[-7.379503],[-0.995104],[-7.081464],[7.742540],[3.921349],[-9.570242],[-4.295417],[-1.968359],[-4.372220],[8.777377],[7.985469],[7.891777],[-2.259233],[4.931029],[-5.260816],[2.241214],[6.638111],[-7.180136]], dtype = "float64")#candidate|2464|(108, 1)|const|float64
call_2463 = relay.TupleGetItem(func_1239_call(relay.reshape(const_2464.astype('float64'), [9, 12, 1])), 0)
call_2465 = relay.TupleGetItem(func_1241_call(relay.reshape(const_2464.astype('float64'), [9, 12, 1])), 0)
func_2256_call = mod.get_global_var('func_2256')
func_2258_call = mutated_mod.get_global_var('func_2258')
call_2470 = func_2256_call()
call_2471 = func_2256_call()
func_1910_call = mod.get_global_var('func_1910')
func_1911_call = mutated_mod.get_global_var('func_1911')
call_2472 = func_1910_call()
call_2473 = func_1910_call()
func_828_call = mod.get_global_var('func_828')
func_832_call = mutated_mod.get_global_var('func_832')
call_2480 = relay.TupleGetItem(func_828_call(relay.reshape(const_2445.astype('uint8'), []), relay.reshape(var_2451.astype('uint8'), [15, 11, 13]), ), 1)
call_2481 = relay.TupleGetItem(func_832_call(relay.reshape(const_2445.astype('uint8'), []), relay.reshape(var_2451.astype('uint8'), [15, 11, 13]), ), 1)
func_1239_call = mod.get_global_var('func_1239')
func_1241_call = mutated_mod.get_global_var('func_1241')
call_2487 = relay.TupleGetItem(func_1239_call(relay.reshape(call_2463.astype('float64'), [9, 12, 1])), 0)
call_2488 = relay.TupleGetItem(func_1241_call(relay.reshape(call_2463.astype('float64'), [9, 12, 1])), 0)
func_2276_call = mod.get_global_var('func_2276')
func_2278_call = mutated_mod.get_global_var('func_2278')
call_2491 = relay.TupleGetItem(func_2276_call(), 0)
call_2492 = relay.TupleGetItem(func_2278_call(), 0)
output = relay.Tuple([call_2409,uop_2438,call_2444,const_2445,call_2450,var_2451,call_2463,const_2464,call_2470,call_2472,call_2480,call_2487,call_2491,])
output2 = relay.Tuple([call_2410,uop_2440,call_2446,const_2445,call_2452,var_2451,call_2465,const_2464,call_2471,call_2473,call_2481,call_2488,call_2492,])
func_2501 = relay.Function([var_2451,], output)
mod['func_2501'] = func_2501
mod = relay.transform.InferType()(mod)
mutated_mod['func_2501'] = func_2501
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2502 = relay.var("var_2502", dtype = "uint8", shape = (2145,))#candidate|2502|(2145,)|var|uint8
func_2501_call = mutated_mod.get_global_var('func_2501')
call_2503 = func_2501_call(var_2502)
output = call_2503
func_2504 = relay.Function([var_2502], output)
mutated_mod['func_2504'] = func_2504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2166_call = mod.get_global_var('func_2166')
func_2167_call = mutated_mod.get_global_var('func_2167')
call_2586 = func_2166_call()
call_2587 = func_2166_call()
output = relay.Tuple([call_2586,])
output2 = relay.Tuple([call_2587,])
func_2593 = relay.Function([], output)
mod['func_2593'] = func_2593
mod = relay.transform.InferType()(mod)
output = func_2593()
func_2594 = relay.Function([], output)
mutated_mod['func_2594'] = func_2594
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1975_call = mod.get_global_var('func_1975')
func_1976_call = mutated_mod.get_global_var('func_1976')
call_2600 = relay.TupleGetItem(func_1975_call(), 0)
call_2601 = relay.TupleGetItem(func_1976_call(), 0)
uop_2611 = relay.cosh(call_2600.astype('float64')) # shape=(8, 3, 10)
uop_2613 = relay.cosh(call_2601.astype('float64')) # shape=(8, 3, 10)
func_1861_call = mod.get_global_var('func_1861')
func_1863_call = mutated_mod.get_global_var('func_1863')
call_2616 = func_1861_call()
call_2617 = func_1861_call()
uop_2623 = relay.atanh(uop_2611.astype('float64')) # shape=(8, 3, 10)
uop_2625 = relay.atanh(uop_2613.astype('float64')) # shape=(8, 3, 10)
func_2276_call = mod.get_global_var('func_2276')
func_2278_call = mutated_mod.get_global_var('func_2278')
call_2626 = relay.TupleGetItem(func_2276_call(), 0)
call_2627 = relay.TupleGetItem(func_2278_call(), 0)
output = relay.Tuple([call_2616,uop_2623,call_2626,])
output2 = relay.Tuple([call_2617,uop_2625,call_2627,])
func_2663 = relay.Function([], output)
mod['func_2663'] = func_2663
mod = relay.transform.InferType()(mod)
output = func_2663()
func_2664 = relay.Function([], output)
mutated_mod['func_2664'] = func_2664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1474_call = mod.get_global_var('func_1474')
func_1475_call = mutated_mod.get_global_var('func_1475')
call_2694 = relay.TupleGetItem(func_1474_call(), 0)
call_2695 = relay.TupleGetItem(func_1475_call(), 0)
output = relay.Tuple([call_2694,])
output2 = relay.Tuple([call_2695,])
func_2706 = relay.Function([], output)
mod['func_2706'] = func_2706
mod = relay.transform.InferType()(mod)
mutated_mod['func_2706'] = func_2706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2706_call = mutated_mod.get_global_var('func_2706')
call_2707 = func_2706_call()
output = call_2707
func_2708 = relay.Function([], output)
mutated_mod['func_2708'] = func_2708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2256_call = mod.get_global_var('func_2256')
func_2258_call = mutated_mod.get_global_var('func_2258')
call_2709 = func_2256_call()
call_2710 = func_2256_call()
output = call_2709
output2 = call_2710
func_2723 = relay.Function([], output)
mod['func_2723'] = func_2723
mod = relay.transform.InferType()(mod)
mutated_mod['func_2723'] = func_2723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2723_call = mutated_mod.get_global_var('func_2723')
call_2724 = func_2723_call()
output = call_2724
func_2725 = relay.Function([], output)
mutated_mod['func_2725'] = func_2725
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2771 = relay.var("var_2771", dtype = "float32", shape = (8, 8, 10))#candidate|2771|(8, 8, 10)|var|float32
uop_2772 = relay.acos(var_2771.astype('float32')) # shape=(8, 8, 10)
func_857_call = mod.get_global_var('func_857')
func_860_call = mutated_mod.get_global_var('func_860')
var_2777 = relay.var("var_2777", dtype = "int16", shape = (330,))#candidate|2777|(330,)|var|int16
call_2776 = relay.TupleGetItem(func_857_call(relay.reshape(var_2777.astype('int16'), [11, 10, 3]), relay.reshape(var_2777.astype('int16'), [11, 10, 3]), ), 0)
call_2778 = relay.TupleGetItem(func_860_call(relay.reshape(var_2777.astype('int16'), [11, 10, 3]), relay.reshape(var_2777.astype('int16'), [11, 10, 3]), ), 0)
output = relay.Tuple([uop_2772,call_2776,var_2777,])
output2 = relay.Tuple([uop_2772,call_2778,var_2777,])
func_2779 = relay.Function([var_2771,var_2777,], output)
mod['func_2779'] = func_2779
mod = relay.transform.InferType()(mod)
mutated_mod['func_2779'] = func_2779
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2779_call = mutated_mod.get_global_var('func_2779')
var_2781 = relay.var("var_2781", dtype = "float32", shape = (8, 8, 10))#candidate|2781|(8, 8, 10)|var|float32
var_2782 = relay.var("var_2782", dtype = "int16", shape = (330,))#candidate|2782|(330,)|var|int16
call_2780 = func_2779_call(var_2781,var_2782,)
output = call_2780
func_2783 = relay.Function([var_2781,var_2782,], output)
mutated_mod['func_2783'] = func_2783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1975_call = mod.get_global_var('func_1975')
func_1976_call = mutated_mod.get_global_var('func_1976')
call_2791 = relay.TupleGetItem(func_1975_call(), 0)
call_2792 = relay.TupleGetItem(func_1976_call(), 0)
func_1575_call = mod.get_global_var('func_1575')
func_1577_call = mutated_mod.get_global_var('func_1577')
call_2799 = relay.TupleGetItem(func_1575_call(), 2)
call_2800 = relay.TupleGetItem(func_1577_call(), 2)
output = relay.Tuple([call_2791,call_2799,])
output2 = relay.Tuple([call_2792,call_2800,])
func_2801 = relay.Function([], output)
mod['func_2801'] = func_2801
mod = relay.transform.InferType()(mod)
mutated_mod['func_2801'] = func_2801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2801_call = mutated_mod.get_global_var('func_2801')
call_2802 = func_2801_call()
output = call_2802
func_2803 = relay.Function([], output)
mutated_mod['func_2803'] = func_2803
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2801_call = mod.get_global_var('func_2801')
func_2803_call = mutated_mod.get_global_var('func_2803')
call_2804 = relay.TupleGetItem(func_2801_call(), 1)
call_2805 = relay.TupleGetItem(func_2803_call(), 1)
func_1760_call = mod.get_global_var('func_1760')
func_1766_call = mutated_mod.get_global_var('func_1766')
const_2828 = relay.const([[-9],[2],[-3],[-7],[6],[9],[-9],[3],[1],[-7],[5],[3],[-8],[9],[3],[6],[10],[-3],[4],[3],[9],[2],[-4],[1],[2],[4],[-5],[-1],[10],[-4],[-1],[-6],[-8],[-6],[-7],[10],[3],[-6],[-6],[-2],[-7],[6],[-3],[-7],[-6],[5],[-9],[8],[10],[-10],[3],[2],[4],[2],[-5],[8],[3],[3],[10],[-9],[9],[6],[7],[-7],[-8],[-1],[-9],[-6],[3],[2],[-6],[-9],[6],[-3],[2],[-5],[-7],[2],[4],[10],[-8],[-2],[8],[-7],[8],[6],[-10],[3],[8],[2],[-9],[2],[-7],[2],[6],[1],[7],[-9],[1],[-3],[-5],[-5],[5],[-3],[-3],[5],[-4],[-9],[-3],[-10]], dtype = "int32")#candidate|2828|(110, 1)|const|int32
const_2829 = relay.const([3,7,6,-9,-9,9,3,1,8,-1,-5,2,-5,5,6,-1,1,-2,-7,5,7,-1,9,-6,-5,10,5,-4,-6,8,-10,-10,6,-5,3,9,3,2,-2,-8,9,-7,-9,5,-1,-5,1,-1,7,9,7,4,8,3,-8,6,-9,2,-5,3,-9,8,-4,-6,-6,-5,-3,-4,-6,-2,8,-2,1,2,2,-4,4,2,1,-2,-2,-10,5,7,-1,-6,5,5,-1,-3,-4,5,-7,7,4,6,8,3,2,-5,-7,1,6,-9,2,-1,7,4,2,3,-3,-3,7,-4,-6,-1,9,-4,-9,-3,4,-7,9,-6,-5,10,10,-10,-9,-5,5,-5,-1,9,-5,10,6,2,-1,8,-9,-5,-2,-7,3,-4,-1,3,2,-9,2,-4,-7,6,5,3,2,7,6,5,-8,-8,-9,-3,10,-6,1,3,-8,-7,2,-1,9,10,-1,-5,-3,-10,-5,-1,-6,9,9,-7,-2,-2,-2,3,-10,-9,6,-2,8,-9,-6,7,-9,9,-2,-7,-9,-1,3,-6,-4,3,-8,9,8,10,2,6,-6,1,9,2,-8,-3,-6,-5,-2,10,-5,10,1,-7,-1,-4,8,-7,-3,7,2,4,8,8,-8,-4,1,6,5,-3,-6,3,2,1,9,-9,-7,-10,-4,7,-1,5,-4,-2,-4,-5,-1,2,-10,-9,10,-9,2,-4,-10,-8,-1,-2,6,5,-8,10,-1,-3,7,8,-1,-8,10,1,4,-2,-4,1,-6,-10,7,6,-4,8,2,-1,-7,-9,-1,-7,-10,2,-3,4,9,6,1,5,2,7,3,8,-6,-7,7,-4,4,1,-8,9,-8,-5,-8,4,-6,-5,-8,-1,1,-3,-3,-7,2,-6,-4,8,-1,-1,-3,-2,-6,10,-3,-10,8,-5,10,-9,2,3,-4,8,-3,-8,-3,-7,-7,-5,-9,-7,10,-9,-5,-5,6,5,-6,-7,1,5,-4,-3,1,-3,6,-7,-3,-9,7,-5,1,-4,2,-5,-5,-5,5,1,-7,-6,8,9,2,-10,-3,3,-5,-10,6,-2,-8,-1,-6,-6,-9,-5,-10,8,4,10,-3,1,7,6,9,-6,4,7,-10,-2,9,-5,2,10,1,5,-2,1,10,-5,-5,7,6,9,8,4,9,-6,-7,6,6,-2,-10,10,-4,10,-5,1,10,7,3,7,5,2,-2,7,-10,8,6,1,-2,9,5,-1,10,-4,1,5,-5,-5,-5,-4,-3,-6,-10,-7,7,2,-6,8,-10,8,-4,-5,-10,-7,-5,2,5,7,5,10,1,-4,2,2,-4,1,-3,-10,-9,8,10,-1,7,2,3,-4,1,-1,9,5,4,-5,6,-2,4,8,1,1,-7,-2,5,5,1,9,9,-5,-1,10,6,2,-3,4,-8,-3,-9,7,8,-8,-8,-1,2,-10,8,2,-3,6,5,-1,6,-9,-9,-9,-10,8,-5,-7,-6,-3,8,-10,10,-8,-7,-7,2,-8,-2,-8,3,2,-4,6,-5,-8,-2,5,-4,4,-1,4,7,-4,8,-3,7,-8,2,3,-3,-2,1,7,-10,7,-4,-7,-5,-1,-5,2,8,5,4,-9,10,1,7,-7,1,-10,-6,-5,10,-4,8,6,-5,-6,-8,-5,-6,-10,-4,-2,2,1,1,-1,-4,3,-8,-10,10,2,-2,-8,3,3,-6,6,9,8,-5,-8,-1,-1,-1,-3,-8,1,-4,-8,7,-8,-8,-1,-10,-6,7,4,-6,10,-5,-8,-10,4,-8,-2,-4,9,5,-9,-10,-1,-9,-6,9,4,-1,-8,-3,-6,5,-7,-8,-2,-8,-9,-6,-7,5,-1,9,10,-10,-10,3,6,-4,10,3,7,5,-10,-6,7,10,6,7,-1,8,-2,7,-10,4,5,4,-9,-7,9,5,5,-7,-7,10,-1,-1,-9,2,-9,9,-4,-7,-3,3,8,-9,-5,7,-1,2,-3,-7,-1,-2,-7,-6,6,-5,6,3,6,-10,-10,-5,-1,-3,9,-9,-8,3,-3,-8,2,10,-1,-3,-6,-10,-9,-7,3,7,9,6,-6,-5,-8,2,6,10,-6,6,6,-8,4,-5,5,-3,-7,-6,-8,6,3,5,-1,-1,-8,8,-5,-10,4,-8,-9,-5,-9,-1,-1,-10,4,-8,-2,1,5,5,8,1,-3,2,1,8,10,5,-6,-8,2,-5,-4,-4,8,1,5,9,-2,-1,8,-2,-1,-10,2,9,-3,-8,-3,-5,4,-6,-9,-8,-5,5,8,-4,2,8,-3,10,1,4,-2,4,7,6,6,9,5,-7,-9,4,6,-5,-6,6,5,-3,8,-5,-7,1,7,5,1,-6,6,2,-9,10,4,-7,5,-7,7,-8,-5,8,-6,-5,-8,9,-1,5,-10,9,2,-4,-4,-9,-7,5,-3,-7,7,-8,-4,-8,-8,7,7,-3,-2,5,-1,6,9,-1,6,5,-9,10,-10,10,-1,-9,5,-7,-10,-2,7,9,1,2,8,-3,-10,10,-3,-9,7,5,9,-8,6,-10,-8,-1,-10,8,-10,-3,-4,-10,5,-3,7,-4,-2,5,-2,1,3,1,-6,-1,10,5,-9,2,4,8,-3,-8,-7,-1,8,-1,7,-6,2,9,3], dtype = "int32")#candidate|2829|(990,)|const|int32
const_2830 = relay.const([1,-6,3,8,8,-1,9,-4,-7,9,10,6,3,6,-3,8,10,-1,-9,1,7,10,5,2,-10,5,-6,-2,8,5,-8,-5,8,-5,7,4,-9,9,-10,-5,3,10,3,-10,-9,2,9,-8,-7,4,9,7,4,-2,-8,7,-9,5,-9,2,-10,-5,-6,-8,6,-7,1,10,10,4,-9,3,7,9,-3,-6,-9,-3,-4,6,-2,2,6,3,-6,-8,-7,2,-9,2,3,-6,-8,7,-10,1,-7,7,9,-3,-6,-9,-4,-7,-5,6,6,10,10,6,-10,2,-2,-3,1,-3,7,-10,-4,-3,-7,-6,-8,4,4,6,7,-3,10,-9,2,-8,3,-9,6,-7,-8,5,-1,-3,-9,3,10,-4,-2,9,-4,-4,-8,7,2,6,-8,5,10,-6,-9,-4,5,-7,-2,2,7,4,-6,7,4,7,6,3,3,4,8,-1,7,-9,-8,4,8,9,6,3,1,4,-3,-5,6,-8,-7,-7,-9,-5,9,10,-5,1,-7,5,-4,7,-6,6,2,-4,5,5,-8,-2,-8,-4,3,8,10,8,-2,3,-7,-8,5,8,-3,-5,-3,-10,9,-8,9,-2,9,5,5,7,-9,1,-7,3,1,-3,-4,7,-8,8,9,8,-2,-9,-3,2,-1,5,1,-10,-7,-7,7,-8,7,4,-8,5,-7,10,3,3,5,2,7,8,-8,-7,-9,9,3,-5,6,-2,6,-3,3,3,-6,-4,8,9,7,10,-2,-1,4,5,-7,5,10,2,-5,-3,-9,-4,-7,2,10,9,5,-7,7,9,1,-7,1,6,4,7,-6,-2,-3,-6,-8,-4,-6,-2,-5,9,4,-8,-5,2,-4,5,-9,3], dtype = "int16")#candidate|2830|(330,)|const|int16
call_2827 = relay.TupleGetItem(func_1760_call(relay.reshape(const_2828.astype('int32'), [110,]), relay.reshape(const_2829.astype('int32'), [990,]), relay.reshape(const_2830.astype('int16'), [55, 6]), relay.reshape(const_2830.astype('int16'), [11, 10, 3]), ), 0)
call_2831 = relay.TupleGetItem(func_1766_call(relay.reshape(const_2828.astype('int32'), [110,]), relay.reshape(const_2829.astype('int32'), [990,]), relay.reshape(const_2830.astype('int16'), [55, 6]), relay.reshape(const_2830.astype('int16'), [11, 10, 3]), ), 0)
bop_2836 = relay.maximum(const_2830.astype('uint8'), const_2828.astype('uint8')) # shape=(110, 330)
func_2150_call = mod.get_global_var('func_2150')
func_2152_call = mutated_mod.get_global_var('func_2152')
call_2840 = relay.TupleGetItem(func_2150_call(relay.reshape(call_2827.astype('uint8'), [2145,])), 1)
call_2841 = relay.TupleGetItem(func_2152_call(relay.reshape(call_2827.astype('uint8'), [2145,])), 1)
output = relay.Tuple([call_2804,call_2827,const_2829,bop_2836,call_2840,])
output2 = relay.Tuple([call_2805,call_2831,const_2829,bop_2836,call_2841,])
func_2848 = relay.Function([], output)
mod['func_2848'] = func_2848
mod = relay.transform.InferType()(mod)
mutated_mod['func_2848'] = func_2848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2848_call = mutated_mod.get_global_var('func_2848')
call_2849 = func_2848_call()
output = call_2849
func_2850 = relay.Function([], output)
mutated_mod['func_2850'] = func_2850
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2869 = relay.const([[[6],[7],[-1],[-5],[-9],[3],[8],[-6],[-8],[9],[-2],[-10],[5]],[[1],[8],[4],[-5],[6],[-7],[6],[-1],[-9],[-6],[-3],[-8],[2]],[[3],[2],[-6],[6],[3],[7],[-4],[-6],[5],[7],[1],[-5],[3]],[[-3],[10],[-4],[5],[-5],[-8],[-4],[4],[9],[-4],[8],[-6],[-7]],[[3],[6],[-10],[8],[4],[5],[7],[-2],[-2],[6],[-10],[3],[-9]],[[-5],[-6],[-2],[2],[4],[6],[-2],[-5],[2],[8],[6],[2],[7]],[[8],[-6],[-8],[10],[3],[2],[9],[-7],[-7],[7],[-7],[-1],[5]],[[-8],[-3],[1],[-4],[-6],[9],[-8],[-9],[8],[-4],[5],[6],[-3]],[[-3],[2],[4],[-8],[-7],[-6],[-7],[-5],[10],[7],[-4],[9],[1]]], dtype = "int32")#candidate|2869|(9, 13, 1)|const|int32
var_2870 = relay.var("var_2870", dtype = "int32", shape = (9, 13, 13))#candidate|2870|(9, 13, 13)|var|int32
bop_2871 = relay.greater_equal(const_2869.astype('bool'), var_2870.astype('bool')) # shape=(9, 13, 13)
func_1239_call = mod.get_global_var('func_1239')
func_1241_call = mutated_mod.get_global_var('func_1241')
const_2876 = relay.const([5.533807,8.873093,4.863969,5.294105,1.736566,-8.453004,2.390393,-9.639268,9.155330,0.148832,-7.830023,4.425425,-6.895415,1.738145,-9.702757,6.380676,-8.437819,-8.349620,8.795364,6.821673,7.046215,-1.422206,-0.478409,-1.694691,-0.319542,-6.269903,9.618231,1.489071,0.743876,-9.165379,-0.125837,2.922877,-0.648526,-6.532101,1.892396,-5.063584,1.022439,-0.282907,-4.668436,0.812771,-3.794298,5.136469,-6.879634,-8.751902,-0.871609,7.908985,-6.491551,7.891646,-5.083947,-4.260363,5.356494,2.173449,-1.448777,0.789250,-9.812548,2.431034,-8.896783,8.084455,-7.121412,-0.282353,-4.442003,0.486100,9.196336,3.521752,-2.989523,4.827911,-3.009891,-3.785254,-3.623142,0.332328,-3.889309,-9.944871,-9.472930,3.055862,5.304466,7.797417,1.531525,-9.682360,1.933094,0.253721,5.085611,4.105391,5.357654,-7.998342,9.214443,-6.792280,3.950253,3.559317,-7.129384,-4.022626,-4.562326,2.602572,-1.603233,-8.866604,0.161150,1.137053,1.177997,3.322585,-3.069318,-2.125283,7.139206,2.243103,7.118703,-9.069540,-1.133764,7.354095,-8.819809,-1.930122], dtype = "float64")#candidate|2876|(108,)|const|float64
call_2875 = relay.TupleGetItem(func_1239_call(relay.reshape(const_2876.astype('float64'), [9, 12, 1])), 0)
call_2877 = relay.TupleGetItem(func_1241_call(relay.reshape(const_2876.astype('float64'), [9, 12, 1])), 0)
func_1642_call = mod.get_global_var('func_1642')
func_1645_call = mutated_mod.get_global_var('func_1645')
const_2888 = relay.const(False, dtype = "bool")#candidate|2888|()|const|bool
const_2889 = relay.const([False,True,False,True,True,True,True,True,False,True,False,True,False,False,True,False,True,False,False,True,False,False,False,True,True,True,False,True,True,True,True,True,False,True,True,True,True,False,False,True,True,True,False,True,True,False,False,False,False,False,True,False,False,False,False,True,True,False,False,False,True,False,True,False,True,False,True,False,True,False,False,False,True,False,False,False,False,False,False,True,False,True,True,False,True,True,True,False,False,True,False,True,True,False,True,True,False,True,True,True,True,True,False,False,False,False,False,False,False,False,True,False,True,True,False,True,False,True,True,False,False,False,False,False,False,True,True,False,False,False,False,True,False,False,True,False,False,True,False,False,True,False,False,True,True,False,False,True,True,True,False,True,True,False,True,True,True,False,False,False,True,False,True,True,False,True,True,False,False,True,False,False,True,False,True,False,False,True,False,True,False,False,False,False,False,False,True,True,False,True,True,True,True,True,False,True,False,True,True,False,True,True,False,False,True,True,True,True,False,True,False,True,True,True,True,True,True,False,False,True,False,False,True,True,True,True,True,True,True,False,True,False,False,False,False,True,True,True,True,False,False,True,True,True,False,False,False,True,False,True,True,False,True,False,False,False,True,True,True,False,True,False,False,True,False,True,True,False,False,False,False,True,True,True,False,False,True,True,True,True,False,False,False,True,False,False,True,False,True,False,False,False,False,True,False,True,False,True,True,False,True,True,True,False,False,False,False,True,True,False,False,True,False,False,False,True,False,True,True,True,True,True,False,True,False,False,False,False,True,True,True,False,False,False,False,False,False,True,True,True,True,False,False,True,False,False,False,True,True,True,False,False,True,False,False,True,False,False,False,True,False,True,True,False,True,False,True,False,True,False,True,False,False,False,True,True,False,False,False,False,True,False,False,False,True,False,False,True,True,False,True,True,True,False,True,False,False,False,False,True,True,False,True,True,False,True,False,False,True,False,False,False,True,True,True,False,True,True,True,False,True,False,True,False,True,True,False,True,True,True,True,False,True,False,False,True,True,False,True,False,True,False,True,False,True,False,False,False,True,True,True,False,False,False,False,True,True,False,False,True,True,True,True,False,False,True,True,True,False,True,False,True,True,True,True,False,True,True,False,False,False,True,False,False,False,False,True,True,False,False,False,False,True,False,False,True,True,False,True,True,True,True,False,False,False,True,False,True,False,False,True,True,False,True,True,False,True,True,True,True,True,False,True,False,False,False,False,True,False,True,True,True,False,True,True,False,True,True,True,True,True,False,False,True,True,False,True,False,True,True,True,False,True,True,False,True,True,False,False,True,True,True,False,True,True,True,True,False,False,False,True,True,False,False,True,True,False,False,True,True,True,True,True,False,False,True,True,True,False,False,False,True,True,False,True,False,True,False,False,True,True,False,False,True,False,True,True,False,False,False,True,True,True,False,False,True,True,True,False,True,True,False,True,True,False,False,True,True,False,False,False,True,False,True,True,False,False,False,False,False,False,True,False,False,True,False,True,False,True,False,False,True,False,True,False,True,True,True,False,True,True,True,True,True,False,False,True,False,False,True,True,False,False,True,False,True,True,False,False,False,False,False,True,False,True,True,True,False,True,False,True,False,True,False,False,True,False,True,True,False,True,False,True,True,True,True,True,False,True,True,True,True,True,False,False,False,False,True,False,True,True,True,True,False,False,True,True,False,True,True,True,False,True,False,True,True,True,False,True,True,True,False,False,False,True,False,False,True,False,False,False,True,False,True,False,False,True,True,False,False,False,True,False,False,True,True,True,True,False,False,False,True,True,False,False,False,True,False,True,True,True,True,False,True,False,False,True,True,False,True,True,False,True,True,False,False,True,True,True,True,False,True,False,True,False,False,True,True,True,False,False,False,True,False,True,True,True,False,True,True,True,False,True,False,False,False,True,True,True,False,False,True,False,False,False,False,True,True,True,False], dtype = "bool")#candidate|2889|(840,)|const|bool
call_2887 = relay.TupleGetItem(func_1642_call(relay.reshape(const_2888.astype('bool'), []), relay.reshape(const_2889.astype('bool'), [7, 10, 12]), ), 0)
call_2890 = relay.TupleGetItem(func_1645_call(relay.reshape(const_2888.astype('bool'), []), relay.reshape(const_2889.astype('bool'), [7, 10, 12]), ), 0)
func_828_call = mod.get_global_var('func_828')
func_832_call = mutated_mod.get_global_var('func_832')
const_2902 = relay.const([-10,1,2,9,8,9,-6,-1,7,-3,9,-2,-9,-4,-4,5,6,1,-3,-5,-6,10,-9,4,2,-8,9,-5,-1,-9,8,9,3,-1,-10,-7,1,2,-6,-5,6,-3,-5,3,-9,-1,10,10,9,10,-8,-10,6,-8,-8,3,6,9,6,1,6,-2,-1,-2,4,4,10,-10,5,9,10,-9,1,2,-2,3,-5,4,7,-8,9,4,3,-6,-3,4,-8,-2,3,-6,-4,-2,-4,-5,-4,4,5,1,-2,-8,3,-10,7,1,5,4,6,10,-2,-1,-8,-10,-10,10,-9,9,-2,-4,-1,8,10,-5,6,6,-10,4,9,2,-6,-3,3,-6,1,4,5,-5,-2,3,6,7,4,8,7,5,2,-8,-2,-10,4,-4,-3,-6,-1,-2,6,-5,-1,8,-2,-1,10,9,-6,4,2,1,-7,10,-5,7,4,-4,6,4,4,2,7,-6,2,-4,-8,-10,1,-2,-4,10,10,4,-5,-4,6,-4,7,5,-2,2,4,-4,1,3,-5,-3,6,-1,-6,1,10,4,-7,-9,-9,-8,4,-10,-8,-10,6,9,3,-3,6,-2,1,-6,-6,-7,7,-8,7,-5,10,7,-1,8,-10,-6,8,5,-3,-8,-7,1,-8,4,-6,-10,4,-2,6,10,2,-2,-3,10,7,4,10,-7,-6,-4,10,7,-3,-1,-1,-5,-9,3,-4,-10,8,-7,1,7,-7,-8,-6,10,-5,8,-2,-7,2,2,3,-10,-6,-9,3,4,8,-8,6,4,9,-5,7,-3,-4,-6,9,-5,-5,1,2,-1,-5,3,-6,-3,10,-9,2,5,-9,2,-1,2,-3,5,8,6,-4,7,7,-9,9,-4,-10,-6,2,-6,7,10,-8,-5,-10,10,-9,5,8,-3,-2,8,5,-10,4,-1,-3,-2,5,-9,-8,10,7,-5,1,-2,2,6,5,-4,3,3,6,9,3,-6,-7,10,6,-1,-1,10,2,-1,-2,-10,-10,-3,6,-8,9,10,4,2,-3,-7,-3,-10,-4,5,-5,3,6,4,5,3,-9,10,4,3,4,-4,6,-5,2,-6,-3,-4,2,-2,-1,-1,-7,4,-4,9,-5,-6,-6,1,8,-6,-6,-9,8,7,6,10,10,5,10,-9,-6,8,-5,9,-8,-4,5,7,5,-5,-2,4,-10,6,-4,7,-10,-3,5,8,-9,2,-8,-7,2,5,8,8,10,-10,-8,6,1,5,-1,3,-7,-2,-3,9,-3,-3,-6,1,-4,-10,-7,10,-4,-5,-10,-5,-3,-4,-9,6,-7,-5,8,9,-6,-4,-7,-10,-1,-8,-5,-8,1,7,-4,4,-1,-4,-6,1,-4,-6,9,-4,2,1,-4,-8,-2,-6,9,10,10,9,9,-9,-6,5,-10,-8,-10,10,10,2,-2,-10,10,-2,-4,-8,2,-7,10,-6,3,-1,-4,1,-10,8,3,4,8,6,7,-6,-9,7,-6,-8,-8,-6,-3,-8,9,-4,6,6,3,5,-3,-9,5,-10,1,-4,10,-3,4,-5,-7,-5,-8,-6,-2,3,3,8,9,3,-9,-1,4,1,3,-2,4,3,10,-4,-2,10,8,5,7,9,4,4,-2,-7,10,7,-1,-7,-2,5,-8,9,-2,-3,-4,-2,2,6,10,1,7,7,8,10,5,-4,-10,-8,9,1,4,10,9,2,-3,3,-10,-7,2,-8,5,-9,5,7,-9,-7,-2,-10,5,2,4,-8,-6,3,-6,-7,3,6,-5,3,-9,-10,-9,2,4,-4,1,-3,10,-7,6,-7,-3,-8,4,-4,-6,-6,7,-1,-3,-9,10,5,7,6,7,-4,-4,1,-8,3,-1,8,-6,-1,5,-7,-4,-5,-4,6,-4,-6,-5,-8,-1,-4,1,-10,-3,8,-3,-5,7,7,2,-7,-6,-7,-7,3,-8,-2,-10,-8,5,5,2,2,9,-3,7,-9,2,-3,1,-8,-4,9,-3,1,2,-6,5,6,-9,6,10,8,-9,2,8,10,10,-8,-4,-1,-4,-5,-4,2,1,-9,1,-4,10,-2,-3,2,2,6,-8,6,-5,10,1,5,8,-4,3,3,1,-4,10,10,6,9,7,8,6,1,10,9,10,-8,1,-8,7,-1,-8,10,-8,-1,-4,-7,9,-8,-2,6,2,6,-5,8,-4,10,9,-7,-9,-2,-7,3,-6,4,10,1,6,-5,-2,5,-9,10,-7,5,-5,-8,7,-10,-4,1,4,4,-1,-1,2,-1,-2,-9,9,-6,-2,-9,-10,1,3,6,6,-5,8,2,-3,1,7,8,-5,-2,-1,-7,2,-4,10,2,9,4,7,-9,2,-6,1,5,-8,-4,-10,1,7,-8,-5,-4,10,-6,-8,7,-7,9,7,-6,4,8,-1,7,4,8,6,6,3,-4,6,-3,6,-3,-7,-10,8,-5,4,-8,7,-10,7,-2,-7,-1,10,8,-5,9,-9,-5,6,8,3,-10,4,-5,5,3,-4,9,-10,9,7,9,6,4,7,-2,2,1,2,-8,3,-1,6,2,6,-3,-1,10,8,7,-10,6,-3,-5,-2,3,4,4,-5,-8,-2,-5,-3,8,1,-9,-6,-10,-1,-3,-9,10,-2,5,-3,-8,6,-5,10,-2,-1,-1,-7,8,-7,-1,-1,4,-5,1,-4,4,4,-8,-5,5,-3,-6,9,-8,-7,7,-2,-1,7,-9,-5,-10,-2,-5,-9,4,-9,2,-4,-6,-3,-1,1,-4,-6,-1,5,9,-8,-6,-7,8,-1,-3,3,10,-2,9,-4,4,-7,2,6,9,6,-10,-8,-8,-1,5,-2,-7,5,8,10,-1,8,-9,5,-8,-5,-5,-9,1,-3,1,3,-10,6,10,-1,-3,4,-3,1,-9,2,-1,-6,10,-1,7,-10,2,6,-2,-3,-5,-6,-6,-2,5,-1,-4,1,6,-8,5,9,-4,1,1,-10,3,-9,-2,7,4,6,-5,-3,-8,-6,-8,4,10,-7,-1,1,2,-4,8,4,9,9,6,5,-2,-8,-5,-4,8,-6,-10,-5,-7,-1,-10,5,6,3,8,7,-8,2,-9,-8,2,8,-3,6,-1,2,-1,-1,3,-10,-2,10,-4,-3,1,-2,5,6,-2,-5,1,-4,-6,-9,1,-9,8,2,4,-7,-7,1,-8,10,-1,-2,-4,-5,1,1,-5,4,-2,7,4,-4,-2,4,1,-7,1,-5,6,-7,-3,-1,-9,-4,-3,-8,5,-9,6,-5,9,1,3,-5,5,-8,-10,-9,-3,-9,-3,5,-10,5,2,-7,5,-1,4,-9,-9,7,5,-8,10,9,6,-3,10,4,-9,-3,9,-3,1,9,-9,9,4,-6,-7,-10,-9,-9,1,3,4,-2,-1,5,-9,3,-3,-5,2,-1,-6,-9,-4,-6,-4,2,-4,-1,3,8,-10,-1,-5,-10,-8,3,-4,9,-5,-10,3,-6,-10,1,-5,-5,-9,-10,5,-1,-4,6,-1,3,-9,4,9,-8,-1,2,7,-4,6,-3,5,5,-10,-7,-8,-8,5,9,-2,-1,-6,-10,2,3,8,-2,-2,4,8,5,-2,-2,-5,-9,6,1,-4,-4,6,8,-3,-9,-7,-9,4,2,-6,-1,3,-9,1,-10,-10,-5,4,-2,-6,-4,-6,10,8,6,-4,7,8,-8,-4,5,-5,-2,-6,7,-5,-4,3,-1,-8,5,3,-1,5,-1,10,-7,-6,5,5,-3,1,3,5,-5,10,-5,1,5,7,-7,2,3,2,10,-8,-8,-2,6,-5,-10,-2,-10,-5,9,1,-1,9,-8,2,8,3,-2,7,6,-9,-8,3,4,-1,10,-8,-4,4,7,2,-5,-1,3,3,1,6,-2,7,5,-8,1,-5,-2,7,-5,5,5,5,8,-5,-1,-10,10,-1,-5,-1,5,-1,6,-6,-6,-9,9,-7,3,7,3,-8,-3,9,10,-6,7,-3,5,4,-2,-10,-8,-7,-9,4,2,-8,-1,-4,-8,-5,10,-7,-9,6,-3,-10,3,1,-4,7,-9,10,1,-10,-8,3,-6,5,-3,-5,-5,-9,-4,2,5,3,-4,3,-9,-4,1,7,8,-3,10,9,-2,-8,9,6,9,10,-4,-9,-10,-4,-10,10,-10,1,8,-9,-8,-1,-7,3,-8,-1,7,-7,-5,-8,1,-7,1,-3,9,3,9,6,-1,-1,-3,-1,-2,-7,-1,-4,-5,3,8,-6,8,-4,-3,10,-9,-3,3,3,4,4,7,6,-6,7,-5,-1,-2,9,-5,-9,1,-9,8,2,1,9,-4,9,6,-6,-1,-5,1,-10,4,-3,3,-1,-3,5,9,-2,-9,-2,7,7,2,10,-5,-2,-10,-5,-6,-6,-9,2,2,-10,-7,7,8,-3,-5,8,5,-10,4,10,2,-10,6,1,-8,-1,1,10,-4,-4,9,-9,-9,-1,-2,6,6,7,9,-2,-6,3,-2,9,-9,-5,2,-3,10,-7,-5,-8,-10,-3,-2,-6,-9,-8,-6,-9,9,-3,7,-5,8,-3,6,1,8,-2,10,-9,-1,-2,-3,1,-4,-4,-8,9,-2,8,4,3,-5,2,-7,6,7,4,-8,1,-9,4,7,-5,6,6,-3,3,8,-5,4,2,1,1,-10,3,1,-9,3,-7,5,10,-4,6,-8,-6,6,6,-3,9,3,-5,1,3,7,-4,5,10,1,-3,1,-3,-7,-4,-8,-6,-5,5,6,-4,10,-5,4,-6,5,3,-1,3,-5,-10,10,-4,-6,2,9,-5,4,5,7,-4,-1,8,-1,-1,6,9,-5,10,2,-7,10,9,2,-3,-3,3,1,-7,-10,1,10,-3,-1,-8,7,-3,7,-10,-3,-10,-7,4,4,-4,-10,2,3,4,-8,-8,-10,-3,-10,-8,5,1,2,-2,7,-3,-1,8,10,-9,-6,5,-7,-5,-1,-3,-4,8,10,-6,-8,-5,-4,2,-4,-2,9,8,-6,-6,-9,-3,3,-1,-3,-1,6,7,-8,-3,9,5,-5,-5,-8,-9,-8,-2,-4,-6,-9,-6,-7,-4,2,-9,3,1,9,-10,-5,-5,-3,-7,-9,-4,2,-3,4,3,-5,9,8,-7,-5,3,-9,-4,5,-7,-4,3,2,-6,5,2,-4,9,10,9,4,5,2,4,-1,-10,-4,5,-8,2,-10,1,-5,8,-8,-1,8,-6,5,8,4,5,8,6,10,-7,-2,4,3,-3,8,-3,-9,-9,-10,-4,-2,2,8,-7,-6,9,-7,7,7,-8,3,-3,10,-1,-6,3,-4,9,-3,-10,-1,8,2,-7,-5,-3,-6,-3,8,-7,8,4,4,-6,2,-9,5,-2,-3,5,3,8,-6,-6,-4,-9,-2,8,8,5,10,-4,1,3,4,4,7,5,-3,-8,-3,-1,1,10,-5,-1,9,1,3,8,3,-3,3,6,10,-3,2,-5,-5,-2,10,-5,-1,2,10,9,9,-6,3,-8,-7,-5,7,9,5,-4,9,5,-6,3,-7,1,-6,10,-2,-2,1,5,-7,4,10,-10,-5,-6,-4,-9,3,6,-1,-1,-7,10,-2,10,3,-3,1,-1,-10,9,8,-4,-2,-10,-9,3,-6,7,-10,-7,-2,6,-6,10,-4,8,1,-2,-4,-3,3,-10,1,-5,6,-5,-4,10,8,6,2,-3,-7,3,7,-4,-4,-9,2,7,8,4,3,-2,7,2,-1,2,9], dtype = "uint8")#candidate|2902|(2145,)|const|uint8
call_2901 = relay.TupleGetItem(func_828_call(relay.reshape(const_2888.astype('uint8'), []), relay.reshape(const_2902.astype('uint8'), [15, 11, 13]), ), 1)
call_2903 = relay.TupleGetItem(func_832_call(relay.reshape(const_2888.astype('uint8'), []), relay.reshape(const_2902.astype('uint8'), [15, 11, 13]), ), 1)
output = relay.Tuple([bop_2871,call_2875,const_2876,call_2887,const_2888,const_2889,call_2901,const_2902,])
output2 = relay.Tuple([bop_2871,call_2877,const_2876,call_2890,const_2888,const_2889,call_2903,const_2902,])
func_2909 = relay.Function([var_2870,], output)
mod['func_2909'] = func_2909
mod = relay.transform.InferType()(mod)
mutated_mod['func_2909'] = func_2909
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2910 = relay.var("var_2910", dtype = "int32", shape = (9, 13, 13))#candidate|2910|(9, 13, 13)|var|int32
func_2909_call = mutated_mod.get_global_var('func_2909')
call_2911 = func_2909_call(var_2910)
output = call_2911
func_2912 = relay.Function([var_2910], output)
mutated_mod['func_2912'] = func_2912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2593_call = mod.get_global_var('func_2593')
func_2594_call = mutated_mod.get_global_var('func_2594')
call_2954 = relay.TupleGetItem(func_2593_call(), 0)
call_2955 = relay.TupleGetItem(func_2594_call(), 0)
func_1975_call = mod.get_global_var('func_1975')
func_1976_call = mutated_mod.get_global_var('func_1976')
call_2975 = relay.TupleGetItem(func_1975_call(), 0)
call_2976 = relay.TupleGetItem(func_1976_call(), 0)
func_1910_call = mod.get_global_var('func_1910')
func_1911_call = mutated_mod.get_global_var('func_1911')
call_2977 = func_1910_call()
call_2978 = func_1910_call()
output = relay.Tuple([call_2954,call_2975,call_2977,])
output2 = relay.Tuple([call_2955,call_2976,call_2978,])
func_2991 = relay.Function([], output)
mod['func_2991'] = func_2991
mod = relay.transform.InferType()(mod)
mutated_mod['func_2991'] = func_2991
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2991_call = mutated_mod.get_global_var('func_2991')
call_2992 = func_2991_call()
output = call_2992
func_2993 = relay.Function([], output)
mutated_mod['func_2993'] = func_2993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1975_call = mod.get_global_var('func_1975')
func_1976_call = mutated_mod.get_global_var('func_1976')
call_2996 = relay.TupleGetItem(func_1975_call(), 0)
call_2997 = relay.TupleGetItem(func_1976_call(), 0)
uop_3028 = relay.asinh(call_2996.astype('float32')) # shape=(8, 3, 10)
uop_3030 = relay.asinh(call_2997.astype('float32')) # shape=(8, 3, 10)
output = relay.Tuple([uop_3028,])
output2 = relay.Tuple([uop_3030,])
func_3052 = relay.Function([], output)
mod['func_3052'] = func_3052
mod = relay.transform.InferType()(mod)
mutated_mod['func_3052'] = func_3052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3052_call = mutated_mod.get_global_var('func_3052')
call_3053 = func_3052_call()
output = call_3053
func_3054 = relay.Function([], output)
mutated_mod['func_3054'] = func_3054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2848_call = mod.get_global_var('func_2848')
func_2850_call = mutated_mod.get_global_var('func_2850')
call_3081 = relay.TupleGetItem(func_2848_call(), 2)
call_3082 = relay.TupleGetItem(func_2850_call(), 2)
uop_3108 = relay.atan(call_3081.astype('float32')) # shape=(990,)
uop_3110 = relay.atan(call_3082.astype('float32')) # shape=(990,)
output = relay.Tuple([uop_3108,])
output2 = relay.Tuple([uop_3110,])
func_3114 = relay.Function([], output)
mod['func_3114'] = func_3114
mod = relay.transform.InferType()(mod)
output = func_3114()
func_3115 = relay.Function([], output)
mutated_mod['func_3115'] = func_3115
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3133 = relay.var("var_3133", dtype = "float32", shape = (1, 4, 10))#candidate|3133|(1, 4, 10)|var|float32
var_3134 = relay.var("var_3134", dtype = "float32", shape = (8, 4, 10))#candidate|3134|(8, 4, 10)|var|float32
bop_3135 = relay.divide(var_3133.astype('float32'), var_3134.astype('float32')) # shape=(8, 4, 10)
output = relay.Tuple([bop_3135,])
output2 = relay.Tuple([bop_3135,])
func_3142 = relay.Function([var_3133,var_3134,], output)
mod['func_3142'] = func_3142
mod = relay.transform.InferType()(mod)
mutated_mod['func_3142'] = func_3142
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3142_call = mutated_mod.get_global_var('func_3142')
var_3144 = relay.var("var_3144", dtype = "float32", shape = (1, 4, 10))#candidate|3144|(1, 4, 10)|var|float32
var_3145 = relay.var("var_3145", dtype = "float32", shape = (8, 4, 10))#candidate|3145|(8, 4, 10)|var|float32
call_3143 = func_3142_call(var_3144,var_3145,)
output = call_3143
func_3146 = relay.Function([var_3144,var_3145,], output)
mutated_mod['func_3146'] = func_3146
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2593_call = mod.get_global_var('func_2593')
func_2594_call = mutated_mod.get_global_var('func_2594')
call_3167 = relay.TupleGetItem(func_2593_call(), 0)
call_3168 = relay.TupleGetItem(func_2594_call(), 0)
output = relay.Tuple([call_3167,])
output2 = relay.Tuple([call_3168,])
func_3177 = relay.Function([], output)
mod['func_3177'] = func_3177
mod = relay.transform.InferType()(mod)
output = func_3177()
func_3178 = relay.Function([], output)
mutated_mod['func_3178'] = func_3178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2276_call = mod.get_global_var('func_2276')
func_2278_call = mutated_mod.get_global_var('func_2278')
call_3229 = relay.TupleGetItem(func_2276_call(), 0)
call_3230 = relay.TupleGetItem(func_2278_call(), 0)
func_446_call = mod.get_global_var('func_446')
func_449_call = mutated_mod.get_global_var('func_449')
const_3242 = relay.const([-5.676369,-8.678449,5.874202,9.447057,-8.508096,-5.734545,3.219856,-0.708679,7.013199,-4.077045,2.627046,0.292896,0.639786,6.504567,-3.899975,-4.398435,-2.831853,1.613857,-7.763391,-2.294187,5.366423,0.442698,-2.543600,7.118106,-3.917332,8.997414,-9.978819,7.902805,-8.817302,-1.856959,8.529570,7.573727,2.389445,-0.753167,-5.832177,-4.517363,4.397013,-3.290698,-7.577132,-8.055883,-9.556158,-8.610851,-2.885843,-7.105944,-4.779941,3.469083,-9.891113,5.751909,-8.400742,6.087569,-1.997103,-0.857952,1.792212,-8.223282,-6.289864,-3.183594,-3.143095,2.719200,9.837065,-4.072847,-6.037394,8.904332,-8.398859,-0.213409,-1.729470,6.137763,-4.461333,9.017523,5.457187,1.183843,-7.427705,-5.426547,-8.046173,2.212215,9.384860,2.358227,9.706407,-1.998732,4.392880,-7.362166,-9.280275,0.976397,7.506469,8.967236,-0.284808,-7.669423,-3.170757,8.935766,-9.529940,-1.050559,-7.756298,0.958820,5.123729,-8.393118,5.471302,-8.689850,-6.203524,-4.588654,-6.234778,-5.986989,-7.362774,0.855246,0.660648,0.979915,9.197870,-8.165673,0.576976,-9.604931,9.095871,9.595177,1.621428,4.305696,3.931260,-3.137328,4.906115,-9.124898,1.031975,-9.823241,7.277569,0.145723,-5.876407,-0.494840,6.830974,-3.353106,6.206711,9.108116,6.864733,6.101840,-8.016162,9.013469,-0.644797,1.585375,1.692527,3.052799,8.413785,-6.924706,-3.545748,4.821088,0.897329,-6.832931,-2.044509,5.520786,-6.876975,-5.455760,-6.711642,-2.596133,-8.459071,3.251145,-0.511207,-2.104216,8.789763,0.948711,6.626046,9.330333,-6.041438,-0.148382,-8.844245,-7.546157,-5.934644,3.138747,-0.009196,8.460116,-5.322021,6.505714,8.703231,-0.160727,-7.444880,-4.553309,2.572675,-3.694141,-4.849891,-8.759088,-3.332082,6.140641,4.952650,-5.528656,0.877295,-2.643275,-1.458016,-8.731805,7.220196,-3.949456,-1.408941,-0.848866,-6.664742,0.419116,5.291969,3.425218,-0.765720,-2.293702,-9.839262,-7.406660,-6.553754,2.077481,-3.582968,2.521298,-4.971751,4.755185,-7.119059,-0.659524,-1.699966,5.385774,5.179008,1.871726,-5.490117,-5.409036,-2.604112,-2.306967,3.979349,2.613311,1.717094,-2.717613,-2.966335,-3.752339,2.897805,-2.161644,-2.237200,4.524841,-4.478254,5.714402,-2.212662,7.467231,-3.441561,7.162256,7.042610,7.916235,1.936046,6.011288,0.437496,1.385068,-0.696724,-1.544463,8.993067,9.267770,8.201625,-2.529536,-9.738557,-8.932486,5.593338,-9.341176,0.145378,6.540721,2.258102,-8.721387,-7.076446,9.779517,4.419404,6.451319,2.954314,6.780544,-5.289763,-0.735311,5.126065,4.177873,1.532958,-8.672784,-0.128575,2.432864,-3.418995,-8.161437,5.236589,3.644698,-1.479330,-5.527848,7.958874,-7.548258,9.477234,-0.475436,7.692522,-3.979545,-1.888021,8.380222,-2.677002,-5.255200,7.917975,-1.595587,3.692517,8.719761,-8.385932,9.618417,3.363993,5.224909,9.018312,-0.629288,-5.755003,5.340094,5.616499,2.038457,1.584119,-7.334924,-9.488639,-5.413194,-6.828150,5.772397,9.893938,6.117341,-8.913125,4.807450,-9.449902,5.504942,-8.752981,5.243044,4.307105,-2.698213,7.325869,4.052970,0.646044,5.223667,-7.236630,-3.425530,7.534595,-4.233215,6.740201,2.487329,9.170348,-1.801168,0.362210,5.857670,-7.117428,-5.957387,-9.421608,4.254810,3.037685,-8.341144,-9.796202,2.634666,-2.328982,9.451019,5.002637,8.682949,1.613694,2.364387,-9.309822,-4.061326,-0.433710,-5.716092,-0.529158,-5.771937,-3.776766,2.659595,0.338091,-1.455649,2.528970,0.874755,1.944920,1.432338,-2.706534,3.747468,-9.672163,2.595744,-2.630217,2.267741,-9.549582,-9.197256,-3.737051,8.104228,-4.359671,4.737547,3.411812,9.275292,-8.267330,-9.541995,1.054139,9.503624,1.216916,-8.106036,-0.446228,-2.303956,8.637891,1.949883,4.104215,1.638273,-0.574796,1.669349,-6.711905,-9.604906,9.840882,5.584360,6.063281,-4.193788,-5.030121,-2.970262,4.727411,4.986450,-2.482049,-8.383200,4.740265,6.305132,2.910832,9.104968,1.432775,-4.968239,-7.792676,1.656612,-7.084100,-3.757859,-5.780229,7.531275,-3.168393,-6.541971,3.099199,-2.580105,6.318793,-3.546419,-7.289461,-4.559578,-3.622277,-0.500968,-7.407272,-5.360566,-8.978288,2.233922,4.569909,-9.823681,6.022692,-8.470726,8.489809,4.216992,4.837961,5.376346,-0.195421,3.742180,-8.975156,8.735147,-9.418224,1.883419,6.216788,0.287084,8.905899,-6.564983,4.861007,6.439638,4.807719,2.019061,9.202121,-4.363408,-9.696629,-7.228215,8.646672,4.017956,6.209015,-6.457998,-5.998592,0.679443,0.955052,-0.148202,2.337070,-2.536875,6.982119,7.099469,-8.240148,-7.791510,1.308950,-5.643170,-7.272941,-3.716358,-7.177765,-8.478525,8.015246,9.993643,5.216648,3.140709,0.110893,9.594586,9.705336,4.500889,-7.572595,-1.019963,-2.438925,7.940058,-6.996027,-7.048459,-2.976627,6.401150,5.358183,5.202634,8.198931,2.815854,-1.092538,0.165521], dtype = "float64")#candidate|3242|(480,)|const|float64
call_3241 = func_446_call(relay.reshape(const_3242.astype('float64'), [16, 6, 5]))
call_3243 = func_446_call(relay.reshape(const_3242.astype('float64'), [16, 6, 5]))
func_1861_call = mod.get_global_var('func_1861')
func_1863_call = mutated_mod.get_global_var('func_1863')
call_3244 = func_1861_call()
call_3245 = func_1861_call()
func_857_call = mod.get_global_var('func_857')
func_860_call = mutated_mod.get_global_var('func_860')
const_3253 = relay.const([[-8,7],[2,1],[-7,-4],[10,-1],[-8,7],[-9,-9],[9,2],[10,2],[9,-7],[1,1],[-2,8],[-8,8],[-9,7],[10,-1],[-5,-9],[-2,-4],[-10,2],[-1,-1],[9,-7],[-10,10],[-4,9],[4,-2],[-2,-6],[2,5],[-3,5],[-9,8],[-8,4],[2,9],[-2,9],[-8,-7],[-2,5],[4,-9],[-9,4],[-3,-8],[7,-10],[6,4],[-8,6],[-4,8],[-7,-3],[5,2],[6,-3],[-6,1],[1,-4],[-3,-6],[3,-8],[-6,-4],[-9,6],[7,-9],[-3,2],[-1,5],[-4,-2],[-9,-7],[2,-1],[2,-3],[-2,-7],[6,4],[8,9],[8,-5],[4,1],[-8,10],[-6,10],[6,-8],[-2,-9],[-5,-8],[-10,-4],[2,3],[7,-3],[-6,6],[-2,9],[8,8],[4,-8],[10,-2],[4,9],[7,4],[-9,10],[-10,5],[-3,-1],[4,2],[-7,-7],[-8,-7],[8,10],[1,-1],[3,-4],[-8,-6],[-5,-3],[-8,-5],[5,4],[-4,8],[9,7],[-4,-10],[10,9],[-3,10],[-3,5],[5,-8],[5,-8],[5,10],[5,-3],[6,3],[7,5],[-8,8],[-7,5],[-4,-4],[9,9],[-9,-7],[8,1],[-3,-9],[8,-10],[8,-10],[-10,7],[-9,4],[-5,1],[4,8],[8,-4],[-6,9],[9,-10],[7,4],[-4,3],[5,1],[-2,6],[10,8],[3,-7],[6,-3],[-7,-6],[1,-4],[-2,-8],[6,-9],[-4,4],[8,2],[-3,10],[-8,6],[6,-10],[3,-1],[10,-2],[-1,-5],[-3,-10],[1,2],[-4,-5],[7,-8],[5,-9],[-9,-3],[-10,-5],[5,7],[-1,1],[-1,-7],[-9,-7],[-8,-9],[-2,-3],[-9,-2],[-1,-1],[7,6],[-6,-1],[2,-4],[-2,7],[-6,7],[3,9],[-6,10],[-7,6],[8,3],[1,-3],[-2,3],[-7,-8],[-7,9],[2,-3],[-8,-8],[5,-1]], dtype = "int16")#candidate|3253|(165, 2)|const|int16
call_3252 = relay.TupleGetItem(func_857_call(relay.reshape(const_3253.astype('int16'), [11, 10, 3]), relay.reshape(const_3253.astype('int16'), [11, 10, 3]), ), 0)
call_3254 = relay.TupleGetItem(func_860_call(relay.reshape(const_3253.astype('int16'), [11, 10, 3]), relay.reshape(const_3253.astype('int16'), [11, 10, 3]), ), 0)
output = relay.Tuple([call_3229,call_3241,const_3242,call_3244,call_3252,const_3253,])
output2 = relay.Tuple([call_3230,call_3243,const_3242,call_3245,call_3254,const_3253,])
func_3272 = relay.Function([], output)
mod['func_3272'] = func_3272
mod = relay.transform.InferType()(mod)
mutated_mod['func_3272'] = func_3272
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3272_call = mutated_mod.get_global_var('func_3272')
call_3273 = func_3272_call()
output = call_3273
func_3274 = relay.Function([], output)
mutated_mod['func_3274'] = func_3274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2706_call = mod.get_global_var('func_2706')
func_2708_call = mutated_mod.get_global_var('func_2708')
call_3311 = relay.TupleGetItem(func_2706_call(), 0)
call_3312 = relay.TupleGetItem(func_2708_call(), 0)
func_1861_call = mod.get_global_var('func_1861')
func_1863_call = mutated_mod.get_global_var('func_1863')
call_3328 = func_1861_call()
call_3329 = func_1861_call()
output = relay.Tuple([call_3311,call_3328,])
output2 = relay.Tuple([call_3312,call_3329,])
func_3334 = relay.Function([], output)
mod['func_3334'] = func_3334
mod = relay.transform.InferType()(mod)
output = func_3334()
func_3335 = relay.Function([], output)
mutated_mod['func_3335'] = func_3335
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3402 = relay.var("var_3402", dtype = "float32", shape = (2, 10, 7))#candidate|3402|(2, 10, 7)|var|float32
uop_3403 = relay.acosh(var_3402.astype('float32')) # shape=(2, 10, 7)
func_2848_call = mod.get_global_var('func_2848')
func_2850_call = mutated_mod.get_global_var('func_2850')
call_3408 = relay.TupleGetItem(func_2848_call(), 1)
call_3409 = relay.TupleGetItem(func_2850_call(), 1)
uop_3416 = relay.acos(var_3402.astype('float32')) # shape=(2, 10, 7)
uop_3418 = relay.sin(uop_3403.astype('float32')) # shape=(2, 10, 7)
func_2318_call = mod.get_global_var('func_2318')
func_2319_call = mutated_mod.get_global_var('func_2319')
call_3438 = relay.TupleGetItem(func_2318_call(), 0)
call_3439 = relay.TupleGetItem(func_2319_call(), 0)
bop_3444 = relay.floor_mod(uop_3418.astype('float64'), relay.reshape(uop_3403.astype('float64'), relay.shape_of(uop_3418))) # shape=(2, 10, 7)
bop_3459 = relay.less(bop_3444.astype('bool'), relay.reshape(uop_3403.astype('bool'), relay.shape_of(bop_3444))) # shape=(2, 10, 7)
func_1523_call = mod.get_global_var('func_1523')
func_1526_call = mutated_mod.get_global_var('func_1526')
const_3465 = relay.const([4,8,9,7,-7,9,1,-10,2,9,-10,-8,-6,4,-5,-1,-5,4,-6,3,2,-1,-10,1,2,7,-6,6,-10,-4,-7,1,-5,-10,-5,-4,-5,-10,-5,-6,-3,-10,-6,5,-9,8,-5,10,5,10,-2,-9,-9,-1,-1,3,8,7,2,-1,-10,-6,9,6,7,7,10,6,6,4,-6,3,10,9,1,-2,-8,-5,-6,2,7,-3,-7,6,10,-1,7,-10,2,-9,-9,4,-7,8,-2,-7,2,-5,10,-10,-3,7,-5,-7,8,1,-4,7,-6,7], dtype = "int32")#candidate|3465|(110,)|const|int32
const_3466 = relay.const([-6,-5,-8,6,5,9,9,1,-2,-9,6,-10,7,10,-3,-7,6,3,6,3,7,5,7,-2,-5,-4,4,-6,9,4,-4,2,-2,-5,-2,-2,-2,7,-5,10,7,2,7,4,-5,7,-9,9,-4,10,3,-7,10,-4,-2,-6,-8,4,-8,3,-7,1,1,-7,-4,-1,10,-10,3,-7,8,-7,4,4,-8,-3,9,-10,4,3,4,-3,-5,3,10,-4,5,-7,-3,-1,9,-5,-8,9,10,-9,8,-7,8,-3,-1,-7,10,-5,6,-3,2,5,1,-3,6,5,6,6,-3,-2,-8,3,4,9,6,7,10,-7,6,1,-1,-5,-10,1,-2,10,-4,7,2,8,-8,7,8,8,-5,-3,7,3,1,-1,-9,-2,-5,-10,5,-7,6,-2,10,-6,8,1,-9,3,10,-2,6,-3,5,7,5,2,8,4,3,-2,1,-8,-10,10,-6,1,8,-10,9,-2,1,-6,7,6,-1,-3,-6,1,-2,7,3,10,4,-4,-7,-9,-10,7,6,1,4,8,-5,-5,9,-4,10,6,2,-6,6,-7,-2,-8,-8,4,1,1,10,-2,9,-3,-10,2,-9,-2,8,3,-4,6,10,-3,1,-8,1,2,-5,-1,-6,-6,-3,-1,-8,1,-7,-3,7,9,-3,1,-4,5,1,-4,-9,3,-1,-3,3,10,-10,-9,10,-5,3,-6,-2,-8,-5,10,-7,5,7,6,3,2,-10,2,-6,-4,4,8,2,-7,-2,-2,9,-6,9,-8,9,-8,10,-2,9,-5,-9,9,3,-10,-4,-4,2,-1,4,-5,-1,4,5,8,-4,-6,-10,-4,-10,5,-9,-7,9,-5,-1,-7,-5,4,9,-5,6,5,6,-6,6,-10,-2,-9,9,5,-4,2,5,1,-9,6,6,1,3,-8,-1,-5,9,6,-7,8,3,-1,6,-2,-8,10,10,-8,1,1,6,6,1,3,-3,9,3,-6,-4,5,7,-10,9,9,3,3,-7,7,1,5,-5,3,8,6,-10,-8,8,-3,5,8,-3,9,2,-7,8,-8,-10,-10,2,2,8,-8,-5,5,4,-8,-6,6,-5,-8,7,-5,-9,-5,10,3,-7,-6,6,4,5,-7,-1,7,-6,-8,-3,1,-5,-4,-6,-2,-2,7,10,-7,3,5,7,-9,-9,7,7,7,-4,8,-10,3,1,-9,1,-5,2,-8,4,-1,2,6,-5,3,3,-9,6,-4,-2,-7,1,-7,3,-3,1,-1,-3,4,9,-7,-3,-7,8,5,6,-5,5,1,9,7,7,5,-3,6,-10,-6,9,1,5,-1,7,10,-2,-2,-5,1,4,-2,8,-1,-4,3,-10,-3,2,10,4,3,-2,-6,-1,1,-4,-2,-4,3,2,1,10,-9,-2,2,-10,1,-8,-1,4,4,-8,4,-1,-9,-3,-5,6,5,-4,3,2,5,1,-2,-9,-6,-5,6,7,9,8,3,1,-4,-7,-10,-3,10,1,10,8,-5,-6,1,8,3,7,2,6,-2,4,-1,-6,-10,4,-9,8,7,6,-9,-9,4,8,3,-3,6,-8,-4,-9,3,8,6,-5,10,-1,10,1,6,-10,-5,4,10,-8,6,3,-1,-3,-7,-1,2,7,-2,5,-10,-4,10,6,-10,6,-4,-7,-10,-3,9,-5,6,4,-2,5,-6,9,-9,-5,1,-6,10,1,2,-10,-10,5,-9,-3,7,-5,10,-8,8,7,5,-4,7,-9,-1,-3,4,-6,-4,-3,8,-6,1,7,-7,9,-10,-7,10,9,4,4,-7,-10,9,5,-1,-8,-5,2,-3,-4,-5,1,8,7,-1,10,1,-2,3,-10,8,-7,-4,7,-1,10,3,-9,3,-2,9,6,-2,-10,6,9,9,1,6,-3,-8,-3,6,1,-10,-8,7,-8,-2,3,-2,6,-8,-7,2,1,2,-10,-6,10,5,6,1,10,4,-3,-4,8,-3,-8,4,6,3,-4,10,8,3,-7,8,8,-1,-10,8,-8,-4,8,8,-4,2,4,4,-7,-4,9,-4,-7,6,1,-7,4,7,-1,-6,8,3,-9,-1,-1,-1,-8,7,-9,5,6,-10,5,-2,4,9,5,-1,-8,1,9,10,-10,-5,2,10,1,-10,-9,3,2,3,-4,4,-1,1,-10,9,10,8,3,-1,7,-1,4,10,-5,-5,-9,3,5,-2,-7,-2,7,10,-7,-4,-2,3,-6,4,-5,-10,-10,-6,9,10,1,6,4,-7,6,-7,6,-4,10,6,7,-2,1,1,-8,-7,-3,-8,-8,7,-6,-10,-2,-7,-2,-10,8,-7,-1,-10,-9,9,-9,-8,2,9,-8,2,-5,4,1,8,5,-10,-4,-5,-7,-7,-1,-3,10,1,-3,10,4,-7,10,-6,-1,-1,-7,9,1,10,1,-5,7,1,-10,10,-6,9,-10,-1,1,7,-10,-2,4,-5,7,-8,-5,-4,9,-9,9,-1,4,2,-5,5,-5,8,-1,4,10,-2,-10,-2,-10,-4,-10,8,8,-1,-8,8,-5,5,-7,4,3,-6,10,-2,10,9,-2,6,-8,-10,-5,-10,-5,4,3,1,4,9,-5,4,8,5,-10,-1,-10,-5,-1,5], dtype = "int32")#candidate|3466|(990,)|const|int32
call_3464 = relay.TupleGetItem(func_1523_call(relay.reshape(const_3465.astype('int32'), [1, 10, 11]), relay.reshape(const_3466.astype('int32'), [9, 10, 11]), ), 2)
call_3467 = relay.TupleGetItem(func_1526_call(relay.reshape(const_3465.astype('int32'), [1, 10, 11]), relay.reshape(const_3466.astype('int32'), [9, 10, 11]), ), 2)
output = relay.Tuple([call_3408,uop_3416,call_3438,bop_3459,call_3464,const_3465,const_3466,])
output2 = relay.Tuple([call_3409,uop_3416,call_3439,bop_3459,call_3467,const_3465,const_3466,])
func_3468 = relay.Function([var_3402,], output)
mod['func_3468'] = func_3468
mod = relay.transform.InferType()(mod)
mutated_mod['func_3468'] = func_3468
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3469 = relay.var("var_3469", dtype = "float32", shape = (2, 10, 7))#candidate|3469|(2, 10, 7)|var|float32
func_3468_call = mutated_mod.get_global_var('func_3468')
call_3470 = func_3468_call(var_3469)
output = call_3470
func_3471 = relay.Function([var_3469], output)
mutated_mod['func_3471'] = func_3471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3177_call = mod.get_global_var('func_3177')
func_3178_call = mutated_mod.get_global_var('func_3178')
call_3517 = relay.TupleGetItem(func_3177_call(), 0)
call_3518 = relay.TupleGetItem(func_3178_call(), 0)
func_2318_call = mod.get_global_var('func_2318')
func_2319_call = mutated_mod.get_global_var('func_2319')
call_3519 = relay.TupleGetItem(func_2318_call(), 0)
call_3520 = relay.TupleGetItem(func_2319_call(), 0)
func_1239_call = mod.get_global_var('func_1239')
func_1241_call = mutated_mod.get_global_var('func_1241')
var_3527 = relay.var("var_3527", dtype = "float64", shape = (108,))#candidate|3527|(108,)|var|float64
call_3526 = relay.TupleGetItem(func_1239_call(relay.reshape(var_3527.astype('float64'), [9, 12, 1])), 0)
call_3528 = relay.TupleGetItem(func_1241_call(relay.reshape(var_3527.astype('float64'), [9, 12, 1])), 0)
func_1005_call = mod.get_global_var('func_1005')
func_1007_call = mutated_mod.get_global_var('func_1007')
call_3533 = relay.TupleGetItem(func_1005_call(relay.reshape(call_3517.astype('uint32'), [])), 3)
call_3534 = relay.TupleGetItem(func_1007_call(relay.reshape(call_3517.astype('uint32'), [])), 3)
output = relay.Tuple([call_3517,call_3519,call_3526,var_3527,call_3533,])
output2 = relay.Tuple([call_3518,call_3520,call_3528,var_3527,call_3534,])
func_3538 = relay.Function([var_3527,], output)
mod['func_3538'] = func_3538
mod = relay.transform.InferType()(mod)
var_3539 = relay.var("var_3539", dtype = "float64", shape = (108,))#candidate|3539|(108,)|var|float64
output = func_3538(var_3539)
func_3540 = relay.Function([var_3539], output)
mutated_mod['func_3540'] = func_3540
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3554 = relay.var("var_3554", dtype = "float32", shape = (5, 13, 3))#candidate|3554|(5, 13, 3)|var|float32
uop_3555 = relay.erf(var_3554.astype('float32')) # shape=(5, 13, 3)
func_2706_call = mod.get_global_var('func_2706')
func_2708_call = mutated_mod.get_global_var('func_2708')
call_3560 = relay.TupleGetItem(func_2706_call(), 0)
call_3561 = relay.TupleGetItem(func_2708_call(), 0)
output = relay.Tuple([uop_3555,call_3560,])
output2 = relay.Tuple([uop_3555,call_3561,])
func_3564 = relay.Function([var_3554,], output)
mod['func_3564'] = func_3564
mod = relay.transform.InferType()(mod)
var_3565 = relay.var("var_3565", dtype = "float32", shape = (5, 13, 3))#candidate|3565|(5, 13, 3)|var|float32
output = func_3564(var_3565)
func_3566 = relay.Function([var_3565], output)
mutated_mod['func_3566'] = func_3566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2723_call = mod.get_global_var('func_2723')
func_2725_call = mutated_mod.get_global_var('func_2725')
call_3629 = func_2723_call()
call_3630 = func_2723_call()
const_3637 = relay.const([[[-0.433394,-9.449905,9.858712,-0.169016,1.448973,-8.808910,-7.205402,6.537192,-6.027612,-7.500399],[8.221700,-9.309094,0.244010,0.166301,8.140803,5.317452,6.691263,-5.904402,-8.222993,-6.956690],[-7.771641,0.505667,9.002332,1.030444,8.323038,3.042460,-1.706983,-2.247604,1.553996,0.726593]],[[6.708912,-0.689011,7.506529,0.923583,-9.136431,4.683543,-0.634854,6.796840,1.524931,9.544076],[-1.349376,5.546809,4.018158,8.027862,1.237310,1.063615,5.352983,5.954378,-2.905730,0.774795],[1.135102,7.420624,9.954715,3.307338,-2.541573,6.739702,-3.246209,0.521618,-5.765069,-6.179403]],[[1.453916,-7.063657,-4.219713,3.461233,-3.030939,1.309369,6.795218,-6.697760,2.121439,5.714150],[-7.632642,-3.291975,3.645071,-6.886407,-5.121145,0.038072,-1.400876,0.469169,-4.255294,-1.532867],[7.606288,-0.871399,-7.894747,9.157292,-8.645913,2.948544,4.656708,9.701513,4.265878,-7.968931]],[[6.439521,-4.331822,-3.073427,-6.263595,-9.441111,6.125216,-8.213170,0.309664,-8.842072,-0.297722],[0.471199,-5.046244,3.976894,-8.089865,4.555324,4.494297,-5.859076,4.687998,1.174423,9.542132],[-1.619599,2.771266,-7.584618,6.010986,8.820498,-0.080287,-1.125564,5.783245,-8.688924,-9.741425]],[[-1.346894,-2.148579,5.420410,5.294910,0.170991,9.408494,-7.722596,-8.703963,9.492773,9.604890],[7.606960,2.472764,-7.577187,-8.275056,-4.157784,4.270399,-3.319519,-2.502119,2.649486,-5.039763],[-1.786209,-6.781582,-9.849085,-8.866274,-2.734196,-1.860491,9.737532,7.805215,-8.409827,-1.930360]],[[7.228069,2.256630,-0.901148,7.699474,-9.547793,-8.930665,9.218207,9.743948,-4.622133,5.243022],[3.141779,-6.206902,-2.711750,6.063293,6.005572,0.598412,8.277600,-8.626384,-1.751527,5.648181],[5.051844,-4.409312,-6.467159,-9.082907,6.352565,6.117518,2.191172,3.610251,-3.247190,-1.135294]],[[-7.071166,-2.907856,1.389551,5.881982,-8.284428,-9.790276,3.811469,8.622550,-3.704263,-8.141394],[2.304852,-8.896281,2.824840,-7.362497,-4.553551,-9.717892,4.237631,-5.582191,7.183381,-1.105657],[-5.872181,-2.510689,5.400287,5.929350,6.458954,6.779204,-7.198210,-8.502630,4.556599,8.859769]],[[4.161240,2.422390,-9.566787,5.212466,8.278894,4.840942,-5.073708,8.137254,7.944547,3.450128],[-7.435462,-7.476781,9.816756,5.988787,3.295913,-6.350634,-9.340132,7.650017,-7.289238,-8.463794],[1.958845,2.330105,6.791973,9.308326,-5.384137,-0.803421,-0.407158,8.484727,2.655717,-4.864273]]], dtype = "float32")#candidate|3637|(8, 3, 10)|const|float32
bop_3638 = relay.power(call_3629.astype('float64'), relay.reshape(const_3637.astype('float64'), relay.shape_of(call_3629))) # shape=(8, 3, 10)
bop_3641 = relay.power(call_3630.astype('float64'), relay.reshape(const_3637.astype('float64'), relay.shape_of(call_3630))) # shape=(8, 3, 10)
output = relay.Tuple([bop_3638,])
output2 = relay.Tuple([bop_3641,])
func_3642 = relay.Function([], output)
mod['func_3642'] = func_3642
mod = relay.transform.InferType()(mod)
output = func_3642()
func_3643 = relay.Function([], output)
mutated_mod['func_3643'] = func_3643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2318_call = mod.get_global_var('func_2318')
func_2319_call = mutated_mod.get_global_var('func_2319')
call_3647 = relay.TupleGetItem(func_2318_call(), 0)
call_3648 = relay.TupleGetItem(func_2319_call(), 0)
func_2276_call = mod.get_global_var('func_2276')
func_2278_call = mutated_mod.get_global_var('func_2278')
call_3675 = relay.TupleGetItem(func_2276_call(), 0)
call_3676 = relay.TupleGetItem(func_2278_call(), 0)
func_1474_call = mod.get_global_var('func_1474')
func_1475_call = mutated_mod.get_global_var('func_1475')
call_3683 = relay.TupleGetItem(func_1474_call(), 0)
call_3684 = relay.TupleGetItem(func_1475_call(), 0)
func_3114_call = mod.get_global_var('func_3114')
func_3115_call = mutated_mod.get_global_var('func_3115')
call_3685 = relay.TupleGetItem(func_3114_call(), 0)
call_3686 = relay.TupleGetItem(func_3115_call(), 0)
output = relay.Tuple([call_3647,call_3675,call_3683,call_3685,])
output2 = relay.Tuple([call_3648,call_3676,call_3684,call_3686,])
func_3690 = relay.Function([], output)
mod['func_3690'] = func_3690
mod = relay.transform.InferType()(mod)
mutated_mod['func_3690'] = func_3690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3690_call = mutated_mod.get_global_var('func_3690')
call_3691 = func_3690_call()
output = call_3691
func_3692 = relay.Function([], output)
mutated_mod['func_3692'] = func_3692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2318_call = mod.get_global_var('func_2318')
func_2319_call = mutated_mod.get_global_var('func_2319')
call_3699 = relay.TupleGetItem(func_2318_call(), 0)
call_3700 = relay.TupleGetItem(func_2319_call(), 0)
func_3114_call = mod.get_global_var('func_3114')
func_3115_call = mutated_mod.get_global_var('func_3115')
call_3733 = relay.TupleGetItem(func_3114_call(), 0)
call_3734 = relay.TupleGetItem(func_3115_call(), 0)
func_1005_call = mod.get_global_var('func_1005')
func_1007_call = mutated_mod.get_global_var('func_1007')
const_3743 = relay.const(-3, dtype = "uint32")#candidate|3743|()|const|uint32
call_3742 = relay.TupleGetItem(func_1005_call(relay.reshape(const_3743.astype('uint32'), [])), 0)
call_3744 = relay.TupleGetItem(func_1007_call(relay.reshape(const_3743.astype('uint32'), [])), 0)
output = relay.Tuple([call_3699,call_3733,call_3742,const_3743,])
output2 = relay.Tuple([call_3700,call_3734,call_3744,const_3743,])
func_3759 = relay.Function([], output)
mod['func_3759'] = func_3759
mod = relay.transform.InferType()(mod)
mutated_mod['func_3759'] = func_3759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3759_call = mutated_mod.get_global_var('func_3759')
call_3760 = func_3759_call()
output = call_3760
func_3761 = relay.Function([], output)
mutated_mod['func_3761'] = func_3761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3052_call = mod.get_global_var('func_3052')
func_3054_call = mutated_mod.get_global_var('func_3054')
call_3781 = relay.TupleGetItem(func_3052_call(), 0)
call_3782 = relay.TupleGetItem(func_3054_call(), 0)
var_3784 = relay.var("var_3784", dtype = "float32", shape = (8, 3, 10))#candidate|3784|(8, 3, 10)|var|float32
bop_3785 = relay.right_shift(call_3781.astype('int32'), relay.reshape(var_3784.astype('int32'), relay.shape_of(call_3781))) # shape=(8, 3, 10)
bop_3788 = relay.right_shift(call_3782.astype('int32'), relay.reshape(var_3784.astype('int32'), relay.shape_of(call_3782))) # shape=(8, 3, 10)
output = bop_3785
output2 = bop_3788
func_3793 = relay.Function([var_3784,], output)
mod['func_3793'] = func_3793
mod = relay.transform.InferType()(mod)
mutated_mod['func_3793'] = func_3793
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3794 = relay.var("var_3794", dtype = "float32", shape = (8, 3, 10))#candidate|3794|(8, 3, 10)|var|float32
func_3793_call = mutated_mod.get_global_var('func_3793')
call_3795 = func_3793_call(var_3794)
output = call_3795
func_3796 = relay.Function([var_3794], output)
mutated_mod['func_3796'] = func_3796
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3690_call = mod.get_global_var('func_3690')
func_3692_call = mutated_mod.get_global_var('func_3692')
call_3857 = relay.TupleGetItem(func_3690_call(), 1)
call_3858 = relay.TupleGetItem(func_3692_call(), 1)
output = relay.Tuple([call_3857,])
output2 = relay.Tuple([call_3858,])
func_3863 = relay.Function([], output)
mod['func_3863'] = func_3863
mod = relay.transform.InferType()(mod)
output = func_3863()
func_3864 = relay.Function([], output)
mutated_mod['func_3864'] = func_3864
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2801_call = mod.get_global_var('func_2801')
func_2803_call = mutated_mod.get_global_var('func_2803')
call_3895 = relay.TupleGetItem(func_2801_call(), 1)
call_3896 = relay.TupleGetItem(func_2803_call(), 1)
output = call_3895
output2 = call_3896
func_3905 = relay.Function([], output)
mod['func_3905'] = func_3905
mod = relay.transform.InferType()(mod)
mutated_mod['func_3905'] = func_3905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3905_call = mutated_mod.get_global_var('func_3905')
call_3906 = func_3905_call()
output = call_3906
func_3907 = relay.Function([], output)
mutated_mod['func_3907'] = func_3907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2991_call = mod.get_global_var('func_2991')
func_2993_call = mutated_mod.get_global_var('func_2993')
call_3978 = relay.TupleGetItem(func_2991_call(), 1)
call_3979 = relay.TupleGetItem(func_2993_call(), 1)
uop_3980 = relay.log2(call_3978.astype('float32')) # shape=(8, 3, 10)
uop_3982 = relay.log2(call_3979.astype('float32')) # shape=(8, 3, 10)
output = relay.Tuple([uop_3980,])
output2 = relay.Tuple([uop_3982,])
func_3984 = relay.Function([], output)
mod['func_3984'] = func_3984
mod = relay.transform.InferType()(mod)
output = func_3984()
func_3985 = relay.Function([], output)
mutated_mod['func_3985'] = func_3985
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4030 = relay.const([[[6,5,4,-10,-6,4,-1,-7,-6,6,2,3,-3,10],[-2,1,2,10,5,7,-10,-9,7,-1,1,-2,7,-8],[10,-8,-8,10,8,6,-1,5,7,10,2,-6,-1,9],[-6,8,4,-10,-6,-2,4,10,-4,-7,-10,4,-10,-6],[-9,-3,-1,4,-7,-8,7,-9,-10,6,-5,3,-10,7],[7,3,10,4,-6,-7,-3,8,-6,10,-8,-10,-7,-8],[1,-7,1,-6,-7,-2,-9,8,5,9,-4,7,-5,-5],[-9,-9,8,-9,-7,10,7,9,-1,5,4,7,-5,10],[-1,-2,7,1,9,-6,8,10,-8,-1,-5,-6,2,-7]],[[-8,-1,-3,9,6,5,3,10,7,-5,1,5,4,-7],[3,-5,10,-9,-9,-2,10,10,9,3,2,-1,5,10],[-7,6,-8,2,9,10,-10,4,-10,-1,4,4,-3,-8],[-3,10,3,2,8,-1,5,-6,-4,5,5,-2,2,-5],[-3,5,-1,-7,-10,-8,-1,5,10,1,4,-7,-3,-7],[7,2,-7,5,4,4,9,2,1,-7,1,-5,5,-3],[3,3,-2,-9,2,8,-5,9,4,-7,-3,8,-4,8],[-6,-8,-10,8,-6,4,-10,5,5,-9,-9,6,1,-5],[-6,6,5,1,-9,-1,6,4,-8,-9,-4,3,-7,3]]], dtype = "uint8")#candidate|4030|(2, 9, 14)|const|uint8
var_4031 = relay.var("var_4031", dtype = "uint8", shape = (2, 9, 14))#candidate|4031|(2, 9, 14)|var|uint8
bop_4032 = relay.not_equal(const_4030.astype('bool'), relay.reshape(var_4031.astype('bool'), relay.shape_of(const_4030))) # shape=(2, 9, 14)
output = bop_4032
output2 = bop_4032
func_4035 = relay.Function([var_4031,], output)
mod['func_4035'] = func_4035
mod = relay.transform.InferType()(mod)
mutated_mod['func_4035'] = func_4035
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4036 = relay.var("var_4036", dtype = "uint8", shape = (2, 9, 14))#candidate|4036|(2, 9, 14)|var|uint8
func_4035_call = mutated_mod.get_global_var('func_4035')
call_4037 = func_4035_call(var_4036)
output = call_4037
func_4038 = relay.Function([var_4036], output)
mutated_mod['func_4038'] = func_4038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3759_call = mod.get_global_var('func_3759')
func_3761_call = mutated_mod.get_global_var('func_3761')
call_4093 = relay.TupleGetItem(func_3759_call(), 3)
call_4094 = relay.TupleGetItem(func_3761_call(), 3)
func_1642_call = mod.get_global_var('func_1642')
func_1645_call = mutated_mod.get_global_var('func_1645')
var_4096 = relay.var("var_4096", dtype = "bool", shape = (840, 1))#candidate|4096|(840, 1)|var|bool
call_4095 = relay.TupleGetItem(func_1642_call(relay.reshape(call_4093.astype('bool'), []), relay.reshape(var_4096.astype('bool'), [7, 10, 12]), ), 0)
call_4097 = relay.TupleGetItem(func_1645_call(relay.reshape(call_4093.astype('bool'), []), relay.reshape(var_4096.astype('bool'), [7, 10, 12]), ), 0)
bop_4098 = relay.logical_and(var_4096.astype('bool'), call_4093.astype('bool')) # shape=(840, 1)
bop_4101 = relay.logical_and(var_4096.astype('bool'), call_4094.astype('bool')) # shape=(840, 1)
func_2663_call = mod.get_global_var('func_2663')
func_2664_call = mutated_mod.get_global_var('func_2664')
call_4102 = relay.TupleGetItem(func_2663_call(), 0)
call_4103 = relay.TupleGetItem(func_2664_call(), 0)
func_1975_call = mod.get_global_var('func_1975')
func_1976_call = mutated_mod.get_global_var('func_1976')
call_4106 = relay.TupleGetItem(func_1975_call(), 0)
call_4107 = relay.TupleGetItem(func_1976_call(), 0)
func_3052_call = mod.get_global_var('func_3052')
func_3054_call = mutated_mod.get_global_var('func_3054')
call_4108 = relay.TupleGetItem(func_3052_call(), 0)
call_4109 = relay.TupleGetItem(func_3054_call(), 0)
bop_4116 = relay.less(call_4095.astype('bool'), relay.reshape(var_4096.astype('bool'), relay.shape_of(call_4095))) # shape=(7, 10, 12)
bop_4119 = relay.less(call_4097.astype('bool'), relay.reshape(var_4096.astype('bool'), relay.shape_of(call_4097))) # shape=(7, 10, 12)
bop_4134 = relay.logical_or(call_4102.astype('bool'), var_4096.astype('bool')) # shape=(840, 1)
bop_4137 = relay.logical_or(call_4103.astype('bool'), var_4096.astype('bool')) # shape=(840, 1)
output = relay.Tuple([bop_4098,call_4106,call_4108,bop_4116,bop_4134,])
output2 = relay.Tuple([bop_4101,call_4107,call_4109,bop_4119,bop_4137,])
func_4155 = relay.Function([var_4096,], output)
mod['func_4155'] = func_4155
mod = relay.transform.InferType()(mod)
var_4156 = relay.var("var_4156", dtype = "bool", shape = (840, 1))#candidate|4156|(840, 1)|var|bool
output = func_4155(var_4156)
func_4157 = relay.Function([var_4156], output)
mutated_mod['func_4157'] = func_4157
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1596_call = mod.get_global_var('func_1596')
func_1597_call = mutated_mod.get_global_var('func_1597')
call_4182 = func_1596_call()
call_4183 = func_1596_call()
uop_4192 = relay.acosh(call_4182.astype('float32')) # shape=(8, 3, 10)
uop_4194 = relay.acosh(call_4183.astype('float32')) # shape=(8, 3, 10)
func_2801_call = mod.get_global_var('func_2801')
func_2803_call = mutated_mod.get_global_var('func_2803')
call_4207 = relay.TupleGetItem(func_2801_call(), 1)
call_4208 = relay.TupleGetItem(func_2803_call(), 1)
output = relay.Tuple([uop_4192,call_4207,])
output2 = relay.Tuple([uop_4194,call_4208,])
func_4214 = relay.Function([], output)
mod['func_4214'] = func_4214
mod = relay.transform.InferType()(mod)
output = func_4214()
func_4215 = relay.Function([], output)
mutated_mod['func_4215'] = func_4215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2276_call = mod.get_global_var('func_2276')
func_2278_call = mutated_mod.get_global_var('func_2278')
call_4238 = relay.TupleGetItem(func_2276_call(), 0)
call_4239 = relay.TupleGetItem(func_2278_call(), 0)
func_446_call = mod.get_global_var('func_446')
func_449_call = mutated_mod.get_global_var('func_449')
const_4252 = relay.const([[-3.670360],[8.019797],[7.637959],[7.241884],[0.439468],[7.403060],[2.839827],[-9.864332],[9.334361],[3.630092],[6.667321],[0.348490],[6.434488],[-8.133154],[-8.662108],[7.155038],[0.199500],[-1.343727],[-6.699407],[-2.125717],[7.734999],[-3.946792],[-6.227325],[-9.560280],[5.655569],[-4.957599],[3.224950],[-6.789914],[-2.996062],[-5.776291],[-0.152962],[4.838263],[-3.995522],[-4.362402],[0.439531],[-2.330675],[-4.565844],[-4.364589],[-4.944941],[-3.894202],[-1.640756],[-0.677056],[7.966078],[-4.844997],[1.970305],[-1.298629],[-8.555747],[1.972693],[-5.531017],[6.607375],[-3.599490],[-7.761043],[-9.904472],[2.319508],[5.626934],[-3.414649],[-5.262310],[7.827806],[-0.108521],[5.097112],[-7.497084],[2.941167],[-1.194948],[-3.096061],[-9.826056],[-6.088751],[7.433422],[3.129919],[5.054405],[-0.554288],[9.412926],[-6.002519],[8.644144],[8.829345],[8.346453],[0.280137],[-8.899515],[-2.235700],[-5.747641],[9.369013],[-4.809039],[4.586422],[-3.717165],[-5.749523],[-3.767997],[7.045600],[9.528265],[1.186160],[4.145368],[-2.780039],[-2.925741],[3.029612],[-6.651472],[4.455216],[-8.296445],[1.070727],[-4.456609],[-8.588343],[-8.287049],[0.763919],[-0.292421],[-7.349702],[-9.327124],[-3.988419],[-2.896397],[5.129524],[0.413950],[2.149604],[-1.044519],[-7.598947],[-2.751107],[-8.867685],[-9.826648],[5.611139],[8.105319],[2.003044],[3.951314],[6.873312],[-5.293986],[-7.735639],[4.607438],[3.333644],[-9.879752],[-4.741522],[4.585266],[9.573377],[6.901834],[-6.278810],[-6.724603],[-3.299219],[-1.199030],[2.742287],[2.960752],[-0.220699],[9.974337],[-3.063808],[-7.644580],[6.404573],[-5.989854],[1.817385],[-8.971824],[1.530508],[-7.647200],[9.999242],[-6.437449],[-2.125161],[-5.953519],[-3.304345],[0.183648],[6.977768],[2.648315],[7.335357],[1.653187],[-5.045567],[-0.960356],[8.193210],[-7.026318],[-3.256749],[-1.118195],[-1.317668],[1.198547],[-8.101874],[-9.547704],[4.982996],[9.644166],[-7.890911],[-9.236025],[-5.395494],[-6.354811],[-2.842921],[-7.706956],[5.049023],[-0.399218],[-4.416042],[-6.422860],[7.158385],[4.763003],[9.513676],[6.593590],[8.789580],[3.094253],[8.616010],[7.874219],[5.749930],[4.580473],[0.977790],[7.429624],[-3.435443],[-1.985337],[-2.895078],[7.450869],[8.957570],[1.185055],[0.612555],[0.640751],[9.714953],[-1.547583],[1.374554],[-6.302330],[-8.336727],[-2.343569],[-5.440899],[-8.965441],[0.770178],[7.650152],[4.567780],[-5.022573],[3.652190],[1.742334],[-0.406293],[-1.325473],[8.218339],[-5.844644],[-5.197860],[6.602319],[-8.598484],[-2.905535],[6.580312],[-6.893494],[-7.777112],[7.307948],[-8.145515],[-6.054414],[4.110660],[-1.961397],[-8.849320],[-2.476178],[-9.174052],[-9.290596],[3.416535],[0.850095],[8.821927],[-4.117942],[-4.865777],[-0.569926],[-9.551771],[4.931597],[6.762417],[8.856924],[8.054163],[-1.799859],[-4.030797],[-1.169431],[7.496427],[1.523208],[-5.125410],[7.898602],[4.422915],[3.765685],[-0.223167],[-0.597999],[1.151607],[4.789661],[8.804606],[6.935603],[4.358002],[-4.598424],[-8.340448],[-8.544188],[-2.891847],[5.056457],[-1.487543],[-6.431274],[-2.302525],[3.920430],[4.041374],[-3.378868],[9.982493],[8.836335],[-0.463068],[-6.318619],[-3.626805],[2.983628],[0.425608],[4.368755],[4.689943],[-7.461853],[0.572390],[3.364835],[-9.728938],[-2.493035],[-9.115092],[-1.415853],[-6.877305],[-8.402206],[0.888953],[-2.942172],[-4.633617],[-4.296017],[6.539579],[4.475779],[-3.716482],[-5.379971],[-1.612019],[-4.887743],[3.157296],[7.384889],[0.729032],[0.297666],[3.592928],[-9.041116],[-7.336087],[7.399226],[-9.293894],[-4.349218],[4.124219],[-8.854937],[-7.143648],[6.345478],[0.053375],[2.899357],[-1.921323],[-1.125207],[8.231266],[0.834583],[-6.735528],[0.056221],[7.699255],[4.585602],[-4.802718],[1.547611],[8.796157],[-0.919229],[0.977050],[-8.681083],[2.757592],[0.279307],[-9.466908],[4.007878],[4.223834],[9.873470],[-7.856058],[0.554245],[5.291168],[9.606314],[-4.357098],[6.865894],[-7.359846],[8.471511],[2.085639],[-5.845189],[-2.368738],[-4.350702],[-8.174273],[-9.783290],[-4.409978],[2.588448],[-8.604288],[-2.594896],[5.581536],[2.963200],[5.659867],[7.560831],[-5.897329],[1.468380],[-7.310794],[-1.374810],[6.300066],[-1.147608],[-1.119206],[3.717067],[-4.537816],[6.629479],[3.116977],[-8.016206],[1.940676],[3.370207],[-6.019599],[1.116807],[2.200459],[-0.858176],[-0.691539],[-5.862433],[9.236514],[3.779376],[8.758616],[-7.984166],[6.141789],[-5.554789],[-4.499864],[2.252151],[3.607047],[-1.143858],[6.789921],[-6.255144],[-8.503719],[1.211685],[-7.482481],[-9.598522],[-0.768696],[7.261720],[-1.047666],[7.162881],[-1.580599],[1.197042],[-2.238295],[-9.404382],[2.178937],[7.882343],[-8.288939],[5.221700],[-5.712204],[-5.801222],[3.533625],[-5.145165],[-3.043556],[7.345776],[9.569266],[8.345432],[1.690789],[-0.973226],[9.800755],[6.547544],[4.332676],[-6.485327],[-5.356365],[-0.024038],[-3.723418],[5.482713],[9.690227],[0.331046],[-1.825493],[0.146387],[7.071887],[0.791497],[2.778058],[-9.674505],[-1.809922],[2.520456],[-7.612698],[-9.798448],[7.003093],[7.507621],[1.447542],[4.356673],[-2.797436],[-4.279174],[-6.398340],[-2.086081],[-3.422342],[-9.915536],[-5.815266],[1.382910],[-2.624688],[-2.545114],[-9.957307],[4.831028],[-1.546908],[8.068211],[-4.155844],[-4.340040],[9.450049],[7.399916],[-4.927783],[5.628444],[9.378796],[-1.944715],[-5.986520],[-2.810752],[-4.456674],[8.701016],[9.654712],[8.826079],[3.608250],[7.651130],[6.112590],[-5.686026],[6.687260],[-2.699430],[2.658069],[-2.872944],[4.978727],[-4.626078],[-1.758887],[-9.482343],[-0.761697],[6.294248],[3.017251],[4.091941],[9.799595]], dtype = "float64")#candidate|4252|(480, 1)|const|float64
call_4251 = func_446_call(relay.reshape(const_4252.astype('float64'), [16, 6, 5]))
call_4253 = func_446_call(relay.reshape(const_4252.astype('float64'), [16, 6, 5]))
output = relay.Tuple([call_4238,call_4251,const_4252,])
output2 = relay.Tuple([call_4239,call_4253,const_4252,])
func_4255 = relay.Function([], output)
mod['func_4255'] = func_4255
mod = relay.transform.InferType()(mod)
output = func_4255()
func_4256 = relay.Function([], output)
mutated_mod['func_4256'] = func_4256
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4291 = relay.var("var_4291", dtype = "float32", shape = (4, 1, 4))#candidate|4291|(4, 1, 4)|var|float32
var_4292 = relay.var("var_4292", dtype = "float32", shape = (4, 15, 4))#candidate|4292|(4, 15, 4)|var|float32
bop_4293 = relay.divide(var_4291.astype('float32'), var_4292.astype('float32')) # shape=(4, 15, 4)
output = bop_4293
output2 = bop_4293
func_4297 = relay.Function([var_4291,var_4292,], output)
mod['func_4297'] = func_4297
mod = relay.transform.InferType()(mod)
var_4298 = relay.var("var_4298", dtype = "float32", shape = (4, 1, 4))#candidate|4298|(4, 1, 4)|var|float32
var_4299 = relay.var("var_4299", dtype = "float32", shape = (4, 15, 4))#candidate|4299|(4, 15, 4)|var|float32
output = func_4297(var_4298,var_4299,)
func_4300 = relay.Function([var_4298,var_4299,], output)
mutated_mod['func_4300'] = func_4300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1975_call = mod.get_global_var('func_1975')
func_1976_call = mutated_mod.get_global_var('func_1976')
call_4386 = relay.TupleGetItem(func_1975_call(), 0)
call_4387 = relay.TupleGetItem(func_1976_call(), 0)
func_2501_call = mod.get_global_var('func_2501')
func_2504_call = mutated_mod.get_global_var('func_2504')
var_4402 = relay.var("var_4402", dtype = "uint8", shape = (2145,))#candidate|4402|(2145,)|var|uint8
call_4401 = relay.TupleGetItem(func_2501_call(relay.reshape(var_4402.astype('uint8'), [2145,])), 10)
call_4403 = relay.TupleGetItem(func_2504_call(relay.reshape(var_4402.astype('uint8'), [2145,])), 10)
func_1005_call = mod.get_global_var('func_1005')
func_1007_call = mutated_mod.get_global_var('func_1007')
const_4416 = relay.const(8, dtype = "uint32")#candidate|4416|()|const|uint32
call_4415 = relay.TupleGetItem(func_1005_call(relay.reshape(const_4416.astype('uint32'), [])), 0)
call_4417 = relay.TupleGetItem(func_1007_call(relay.reshape(const_4416.astype('uint32'), [])), 0)
func_2166_call = mod.get_global_var('func_2166')
func_2167_call = mutated_mod.get_global_var('func_2167')
call_4436 = func_2166_call()
call_4437 = func_2166_call()
func_2166_call = mod.get_global_var('func_2166')
func_2167_call = mutated_mod.get_global_var('func_2167')
call_4454 = func_2166_call()
call_4455 = func_2166_call()
func_4155_call = mod.get_global_var('func_4155')
func_4157_call = mutated_mod.get_global_var('func_4157')
const_4458 = relay.const([True,False,False,False,True,False,False,False,True,False,False,True,True,True,False,True,False,True,False,False,True,False,True,False,True,False,False,True,False,False,True,True,False,False,False,False,False,False,False,True,False,False,False,True,True,True,True,True,False,True,True,True,True,True,False,False,True,False,False,True,False,True,True,False,True,True,False,False,True,False,True,True,False,False,True,True,True,False,False,True,True,False,True,False,True,True,True,False,True,True,False,True,False,True,True,False,False,False,False,True,False,True,False,True,True,True,False,False,True,True,False,False,True,True,True,False,False,False,False,True,True,False,False,True,True,True,True,True,True,True,False,False,True,True,True,False,False,True,True,False,False,True,False,True,False,True,True,False,True,False,True,False,False,True,False,False,False,True,True,False,True,False,False,False,True,True,False,True,False,True,True,True,False,False,False,False,True,False,False,True,False,True,True,False,False,True,False,True,True,False,True,False,False,True,False,True,False,False,False,False,False,False,True,False,False,False,True,True,False,True,False,False,True,False,False,True,True,True,False,False,True,True,False,True,False,False,False,False,True,False,True,True,False,False,True,False,False,False,False,False,False,False,False,True,False,True,False,False,False,True,False,True,False,True,False,True,True,False,True,False,False,False,True,True,True,True,True,True,True,True,False,True,False,False,False,False,True,True,False,True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,False,False,False,True,False,False,True,False,True,True,False,False,True,False,True,False,True,True,True,False,True,True,False,True,False,True,False,False,False,True,False,False,False,False,True,False,False,False,False,False,True,False,False,True,False,True,True,False,False,False,False,True,True,False,False,True,True,False,False,True,False,False,True,False,False,True,False,True,True,False,True,True,False,True,False,True,False,True,True,False,True,True,True,False,True,False,True,True,False,True,False,False,True,False,False,False,True,False,True,False,False,False,True,True,True,True,False,True,False,True,True,True,False,False,True,True,False,True,False,True,False,True,True,False,True,False,False,False,False,True,False,True,True,False,False,False,True,False,True,False,True,False,True,True,False,True,False,True,False,True,False,False,False,True,False,True,True,False,True,False,True,True,True,False,True,True,False,True,True,True,True,False,True,False,True,False,True,True,True,True,False,True,False,False,False,False,True,False,True,False,False,False,False,True,True,True,False,True,False,True,True,True,True,False,False,False,False,True,True,True,True,False,False,True,False,True,True,False,True,False,False,True,True,False,False,False,False,False,True,False,True,False,False,False,True,False,False,True,True,True,True,False,True,True,True,False,False,True,False,True,True,False,False,False,True,False,False,True,False,False,True,True,False,True,True,True,True,True,True,True,True,False,True,False,True,True,False,False,False,False,True,True,True,False,False,False,False,False,True,True,False,False,False,True,False,False,False,True,True,True,False,False,True,False,True,True,True,True,True,True,False,False,False,True,False,False,True,True,True,False,False,True,False,False,False,False,False,True,False,False,False,False,False,False,False,True,True,True,True,False,False,True,False,True,False,True,True,True,False,False,True,False,False,True,False,False,False,True,True,False,True,False,False,True,False,True,True,True,False,False,True,True,True,True,False,True,False,True,False,False,False,True,False,False,False,True,False,False,False,False,False,True,False,True,False,False,False,True,True,False,True,False,True,False,True,True,True,False,True,True,False,True,False,True,True,True,False,True,True,False,True,False,True,True,True,True,True,True,True,False,True,False,False,True,True,False,False,False,False,True,False,False,False,False,True,True,True,True,True,True,True,False,True,False,False,False,False,True,True,True,False,False,True,False,True,False,False,False,True,False,True,True,True,False,True,False,True,True,False,False,False,True,True,True,False,True,True,False,False,False,True,False,False,False,True,False,True,True,False,False,False,True,True,True,True,False,True,True,True,True,True,True,True,False,False,True,True,True,True,False,True,False,False,False,False,True,False,True,True,False,True,True,True,False,False,True,True,True,False,False,True,True,False,False,False,False], dtype = "bool")#candidate|4458|(840,)|const|bool
call_4457 = relay.TupleGetItem(func_4155_call(relay.reshape(const_4458.astype('bool'), [840, 1])), 0)
call_4459 = relay.TupleGetItem(func_4157_call(relay.reshape(const_4458.astype('bool'), [840, 1])), 0)
var_4462 = relay.var("var_4462", dtype = "uint8", shape = (8, 2, 15))#candidate|4462|(8, 2, 15)|var|uint8
bop_4463 = relay.greater(call_4454.astype('bool'), var_4462.astype('bool')) # shape=(8, 2, 15)
bop_4466 = relay.greater(call_4455.astype('bool'), var_4462.astype('bool')) # shape=(8, 2, 15)
func_3272_call = mod.get_global_var('func_3272')
func_3274_call = mutated_mod.get_global_var('func_3274')
call_4468 = relay.TupleGetItem(func_3272_call(), 5)
call_4469 = relay.TupleGetItem(func_3274_call(), 5)
output = relay.Tuple([call_4386,call_4401,var_4402,call_4415,const_4416,call_4436,call_4457,const_4458,bop_4463,call_4468,])
output2 = relay.Tuple([call_4387,call_4403,var_4402,call_4417,const_4416,call_4437,call_4459,const_4458,bop_4466,call_4469,])
func_4479 = relay.Function([var_4402,var_4462,], output)
mod['func_4479'] = func_4479
mod = relay.transform.InferType()(mod)
var_4480 = relay.var("var_4480", dtype = "uint8", shape = (2145,))#candidate|4480|(2145,)|var|uint8
var_4481 = relay.var("var_4481", dtype = "uint8", shape = (8, 2, 15))#candidate|4481|(8, 2, 15)|var|uint8
output = func_4479(var_4480,var_4481,)
func_4482 = relay.Function([var_4480,var_4481,], output)
mutated_mod['func_4482'] = func_4482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2256_call = mod.get_global_var('func_2256')
func_2258_call = mutated_mod.get_global_var('func_2258')
call_4486 = func_2256_call()
call_4487 = func_2256_call()
output = relay.Tuple([call_4486,])
output2 = relay.Tuple([call_4487,])
func_4513 = relay.Function([], output)
mod['func_4513'] = func_4513
mod = relay.transform.InferType()(mod)
mutated_mod['func_4513'] = func_4513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4513_call = mutated_mod.get_global_var('func_4513')
call_4514 = func_4513_call()
output = call_4514
func_4515 = relay.Function([], output)
mutated_mod['func_4515'] = func_4515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1910_call = mod.get_global_var('func_1910')
func_1911_call = mutated_mod.get_global_var('func_1911')
call_4560 = func_1910_call()
call_4561 = func_1910_call()
output = relay.Tuple([call_4560,])
output2 = relay.Tuple([call_4561,])
func_4566 = relay.Function([], output)
mod['func_4566'] = func_4566
mod = relay.transform.InferType()(mod)
output = func_4566()
func_4567 = relay.Function([], output)
mutated_mod['func_4567'] = func_4567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1575_call = mod.get_global_var('func_1575')
func_1577_call = mutated_mod.get_global_var('func_1577')
call_4581 = relay.TupleGetItem(func_1575_call(), 3)
call_4582 = relay.TupleGetItem(func_1577_call(), 3)
output = call_4581
output2 = call_4582
func_4591 = relay.Function([], output)
mod['func_4591'] = func_4591
mod = relay.transform.InferType()(mod)
mutated_mod['func_4591'] = func_4591
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4591_call = mutated_mod.get_global_var('func_4591')
call_4592 = func_4591_call()
output = call_4592
func_4593 = relay.Function([], output)
mutated_mod['func_4593'] = func_4593
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4699 = relay.var("var_4699", dtype = "bool", shape = (10, 11, 16))#candidate|4699|(10, 11, 16)|var|bool
const_4700 = relay.const([[[False,False,False,True,True,True,False,True,False,True,True,False,True,True,True,False],[True,False,True,True,True,True,True,False,True,False,False,True,True,True,True,False],[True,True,True,True,True,True,False,True,False,True,True,False,True,False,False,False],[True,True,True,False,False,False,False,True,False,False,False,True,False,True,True,True],[True,False,False,False,False,True,True,False,False,True,False,True,True,False,True,False],[True,False,False,False,False,True,True,False,True,False,False,True,True,True,True,False],[False,True,False,False,False,False,False,True,True,True,False,False,True,False,True,True],[False,True,True,True,False,False,True,False,False,True,True,False,True,False,False,True],[False,True,True,False,True,True,True,False,False,False,False,False,False,True,True,False],[True,False,True,True,False,True,True,True,False,True,True,True,True,True,False,True],[False,True,False,True,True,True,True,True,True,False,True,True,True,False,False,False]],[[False,True,False,True,False,True,False,True,False,True,False,False,False,True,True,True],[False,True,False,True,True,False,True,False,False,False,False,True,True,False,False,True],[True,False,False,False,True,False,True,False,True,True,False,False,False,True,True,True],[True,True,False,False,True,True,False,True,False,False,True,True,False,True,False,False],[True,True,False,False,True,True,False,True,False,False,True,True,False,False,False,True],[True,False,True,True,False,True,False,False,False,True,True,False,False,True,False,True],[False,False,False,False,True,False,True,False,True,False,True,True,False,True,False,True],[True,True,False,True,False,True,True,False,False,False,True,True,False,True,False,False],[False,False,False,True,True,True,True,False,True,False,True,True,True,True,True,True],[False,True,False,False,False,False,True,True,False,False,False,False,True,False,True,True],[True,True,True,False,True,False,False,False,True,True,False,False,False,True,True,False]],[[False,False,False,True,False,True,False,False,True,False,True,True,False,False,False,True],[True,True,True,False,False,True,True,True,False,True,True,False,False,True,False,False],[True,True,True,True,False,True,True,False,True,False,True,False,False,True,True,False],[True,True,False,True,False,True,False,True,False,True,True,False,False,False,True,True],[True,False,False,True,False,False,True,True,False,False,True,True,False,True,True,True],[False,True,False,False,True,False,True,True,True,True,False,False,True,True,True,False],[True,False,True,True,False,True,True,False,True,False,True,True,True,False,False,True],[False,False,False,True,False,True,False,False,False,False,False,True,True,True,True,True],[True,True,False,True,False,True,False,True,False,True,True,True,False,True,True,False],[False,True,True,False,False,True,False,True,False,False,False,True,False,False,False,True],[True,True,True,True,False,True,False,False,False,True,False,False,True,True,False,True]],[[False,True,True,False,True,False,True,True,False,False,False,False,False,True,False,True],[False,True,False,False,False,False,True,False,False,True,True,True,False,True,False,False],[True,True,False,False,True,False,True,False,False,True,False,False,False,False,True,False],[True,True,True,True,True,False,False,True,True,True,False,True,False,False,True,True],[False,True,True,True,True,False,True,True,False,False,True,False,False,False,True,False],[True,False,True,True,False,True,False,True,False,True,False,True,True,True,False,True],[False,False,True,False,False,False,True,False,False,True,True,True,True,False,True,True],[False,False,False,False,False,False,True,False,True,True,True,True,False,False,False,False],[False,True,False,False,False,False,True,False,True,False,True,False,False,False,True,False],[True,True,False,True,False,True,True,True,False,True,False,False,True,True,False,True],[False,True,True,False,True,False,True,False,False,False,False,False,True,False,False,False]],[[True,False,True,True,True,False,True,True,True,True,True,False,False,False,True,True],[True,True,True,False,True,False,False,False,True,False,False,False,False,True,False,False],[True,True,True,True,True,False,False,True,False,False,True,False,False,True,True,True],[False,True,True,True,True,True,True,False,True,False,False,False,True,False,False,False],[True,True,True,True,False,False,False,False,False,True,False,False,False,False,True,False],[True,False,False,False,True,True,True,False,True,True,False,False,False,False,True,True],[False,False,False,False,False,False,False,False,False,False,False,False,False,True,True,True],[True,True,False,False,False,True,True,False,False,True,False,False,False,True,False,False],[False,False,False,False,True,False,True,True,False,True,True,True,True,False,False,False],[True,False,True,False,True,False,False,False,True,False,False,True,False,False,True,False],[True,True,False,False,True,True,True,False,True,False,True,False,True,True,False,False]],[[False,True,False,True,True,False,True,True,True,False,False,True,False,False,True,True],[True,True,True,True,True,False,True,False,True,False,False,False,True,False,False,True],[False,True,True,True,True,False,False,False,False,True,True,True,True,False,False,False],[False,False,True,True,False,False,True,True,False,True,True,False,True,False,True,True],[True,False,True,False,True,True,True,True,False,False,False,True,True,True,False,True],[True,True,False,True,False,True,True,False,False,False,False,True,False,False,True,True],[False,False,False,True,True,True,True,False,True,True,True,False,False,True,True,True],[True,True,True,True,False,False,True,False,False,False,False,True,False,True,False,False],[True,False,False,False,True,True,False,True,False,False,True,True,True,True,False,False],[False,True,True,True,True,True,True,False,True,True,True,True,False,True,True,True],[False,True,False,True,False,False,False,True,False,False,False,False,True,False,False,True]],[[False,False,False,True,True,False,True,False,True,False,True,False,False,False,True,False],[False,True,True,False,False,False,True,False,False,True,False,True,False,True,False,False],[True,True,True,False,True,True,False,False,True,True,False,True,True,False,True,True],[True,True,False,True,True,True,False,True,True,False,False,True,True,False,True,False],[True,False,False,False,True,False,True,True,True,True,False,True,True,False,False,True],[True,False,False,False,False,False,True,True,True,True,False,False,True,True,True,True],[True,True,True,True,False,False,False,True,False,False,False,True,False,True,False,True],[True,True,True,True,True,False,False,False,True,False,True,True,True,False,False,True],[True,True,False,True,False,False,True,False,False,True,True,True,False,False,False,False],[True,False,True,False,False,False,True,False,False,False,True,False,False,True,True,True],[False,True,True,False,True,False,False,True,True,False,False,False,False,True,False,True]],[[True,True,True,True,True,False,True,False,False,False,False,False,True,True,False,False],[False,True,False,True,True,True,False,False,True,True,False,True,False,False,False,True],[False,True,False,True,False,False,True,False,False,True,True,False,False,True,False,False],[False,False,True,True,True,False,True,False,True,False,True,True,False,True,False,False],[True,False,False,True,False,True,True,True,True,False,True,True,True,True,False,True],[True,True,False,True,True,False,True,False,False,True,True,False,False,True,True,True],[False,True,False,False,False,False,True,True,False,False,True,False,True,True,True,True],[False,False,False,False,False,True,False,False,False,False,False,True,True,True,False,True],[False,True,False,True,True,True,False,True,False,True,True,True,False,True,False,True],[True,False,True,True,False,True,True,False,True,True,True,True,True,False,False,True],[True,False,False,False,False,True,True,False,False,True,True,True,False,False,False,True]],[[False,True,False,False,False,True,True,False,False,False,True,True,False,True,True,True],[False,True,True,False,False,True,False,True,False,True,False,False,True,False,True,False],[True,True,False,True,False,True,True,False,False,False,False,False,False,True,False,False],[False,True,False,True,False,False,False,False,True,False,False,True,False,True,True,True],[False,True,False,False,True,False,True,True,False,True,True,False,False,True,False,False],[True,False,True,True,False,True,False,False,True,False,True,True,False,False,False,False],[True,True,True,False,True,False,True,True,True,True,False,True,False,False,True,True],[True,True,True,True,False,True,True,False,True,False,True,True,False,False,False,False],[True,True,False,False,True,False,True,False,True,True,True,True,False,False,True,True],[True,False,False,False,True,False,False,False,False,True,False,True,True,False,True,False],[True,True,False,False,True,False,False,False,True,True,False,True,True,True,False,True]],[[True,True,True,False,True,True,False,True,False,False,False,False,False,True,False,True],[True,True,True,False,True,True,True,False,False,True,False,False,False,False,True,True],[True,False,True,False,True,True,False,True,False,False,True,False,False,False,False,True],[True,True,True,False,True,False,False,True,True,False,True,True,True,False,False,False],[False,True,True,True,True,True,True,True,True,False,True,True,False,True,False,True],[True,False,True,False,False,False,True,False,False,True,True,True,True,False,False,False],[True,True,True,False,False,False,True,True,True,True,True,True,False,True,True,True],[True,False,True,False,False,True,False,True,False,True,False,True,True,False,True,True],[True,True,True,True,True,True,True,False,False,False,False,False,True,True,False,True],[True,True,True,False,False,True,True,False,False,True,False,False,False,True,True,True],[False,False,True,False,True,False,False,True,False,False,False,True,True,False,False,True]]], dtype = "bool")#candidate|4700|(10, 11, 16)|const|bool
bop_4701 = relay.logical_and(var_4699.astype('bool'), relay.reshape(const_4700.astype('bool'), relay.shape_of(var_4699))) # shape=(10, 11, 16)
func_3142_call = mod.get_global_var('func_3142')
func_3146_call = mutated_mod.get_global_var('func_3146')
const_4709 = relay.const([[-0.636192,-9.688088,2.916931,-2.034459],[-3.152125,-4.002595,3.082737,8.715465],[4.966836,1.347596,2.945072,9.213664],[-0.326168,7.318191,7.569044,-5.221014],[-6.334294,7.531409,-5.080331,6.900110],[7.219661,-1.258573,-1.238857,-0.130880],[1.291334,1.030797,-6.929183,3.978088],[3.584872,3.744488,0.896359,-4.026836],[-8.835703,5.377468,9.888780,9.674346],[-3.781348,-2.069955,5.134807,-6.424958]], dtype = "float32")#candidate|4709|(10, 4)|const|float32
var_4710 = relay.var("var_4710", dtype = "float32", shape = (320,))#candidate|4710|(320,)|var|float32
call_4708 = relay.TupleGetItem(func_3142_call(relay.reshape(const_4709.astype('float32'), [1, 4, 10]), relay.reshape(var_4710.astype('float32'), [8, 4, 10]), ), 0)
call_4711 = relay.TupleGetItem(func_3146_call(relay.reshape(const_4709.astype('float32'), [1, 4, 10]), relay.reshape(var_4710.astype('float32'), [8, 4, 10]), ), 0)
output = relay.Tuple([bop_4701,call_4708,const_4709,var_4710,])
output2 = relay.Tuple([bop_4701,call_4711,const_4709,var_4710,])
func_4717 = relay.Function([var_4699,var_4710,], output)
mod['func_4717'] = func_4717
mod = relay.transform.InferType()(mod)
mutated_mod['func_4717'] = func_4717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4717_call = mutated_mod.get_global_var('func_4717')
var_4719 = relay.var("var_4719", dtype = "bool", shape = (10, 11, 16))#candidate|4719|(10, 11, 16)|var|bool
var_4720 = relay.var("var_4720", dtype = "float32", shape = (320,))#candidate|4720|(320,)|var|float32
call_4718 = func_4717_call(var_4719,var_4720,)
output = call_4718
func_4721 = relay.Function([var_4719,var_4720,], output)
mutated_mod['func_4721'] = func_4721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2318_call = mod.get_global_var('func_2318')
func_2319_call = mutated_mod.get_global_var('func_2319')
call_4774 = relay.TupleGetItem(func_2318_call(), 0)
call_4775 = relay.TupleGetItem(func_2319_call(), 0)
output = relay.Tuple([call_4774,])
output2 = relay.Tuple([call_4775,])
func_4786 = relay.Function([], output)
mod['func_4786'] = func_4786
mod = relay.transform.InferType()(mod)
output = func_4786()
func_4787 = relay.Function([], output)
mutated_mod['func_4787'] = func_4787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3905_call = mod.get_global_var('func_3905')
func_3907_call = mutated_mod.get_global_var('func_3907')
call_4803 = func_3905_call()
call_4804 = func_3905_call()
func_274_call = mod.get_global_var('func_274')
func_277_call = mutated_mod.get_global_var('func_277')
call_4811 = func_274_call(relay.reshape(call_4803.astype('uint16'), []))
call_4812 = func_274_call(relay.reshape(call_4803.astype('uint16'), []))
output = relay.Tuple([call_4803,call_4811,])
output2 = relay.Tuple([call_4804,call_4812,])
func_4814 = relay.Function([], output)
mod['func_4814'] = func_4814
mod = relay.transform.InferType()(mod)
output = func_4814()
func_4815 = relay.Function([], output)
mutated_mod['func_4815'] = func_4815
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1575_call = mod.get_global_var('func_1575')
func_1577_call = mutated_mod.get_global_var('func_1577')
call_4839 = relay.TupleGetItem(func_1575_call(), 3)
call_4840 = relay.TupleGetItem(func_1577_call(), 3)
output = call_4839
output2 = call_4840
func_4841 = relay.Function([], output)
mod['func_4841'] = func_4841
mod = relay.transform.InferType()(mod)
mutated_mod['func_4841'] = func_4841
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4841_call = mutated_mod.get_global_var('func_4841')
call_4842 = func_4841_call()
output = call_4842
func_4843 = relay.Function([], output)
mutated_mod['func_4843'] = func_4843
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2801_call = mod.get_global_var('func_2801')
func_2803_call = mutated_mod.get_global_var('func_2803')
call_4844 = relay.TupleGetItem(func_2801_call(), 1)
call_4845 = relay.TupleGetItem(func_2803_call(), 1)
func_3272_call = mod.get_global_var('func_3272')
func_3274_call = mutated_mod.get_global_var('func_3274')
call_4856 = relay.TupleGetItem(func_3272_call(), 1)
call_4857 = relay.TupleGetItem(func_3274_call(), 1)
func_2663_call = mod.get_global_var('func_2663')
func_2664_call = mutated_mod.get_global_var('func_2664')
call_4876 = relay.TupleGetItem(func_2663_call(), 1)
call_4877 = relay.TupleGetItem(func_2664_call(), 1)
output = relay.Tuple([call_4844,call_4856,call_4876,])
output2 = relay.Tuple([call_4845,call_4857,call_4877,])
func_4882 = relay.Function([], output)
mod['func_4882'] = func_4882
mod = relay.transform.InferType()(mod)
mutated_mod['func_4882'] = func_4882
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4882_call = mutated_mod.get_global_var('func_4882')
call_4883 = func_4882_call()
output = call_4883
func_4884 = relay.Function([], output)
mutated_mod['func_4884'] = func_4884
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1596_call = mod.get_global_var('func_1596')
func_1597_call = mutated_mod.get_global_var('func_1597')
call_4926 = func_1596_call()
call_4927 = func_1596_call()
func_1523_call = mod.get_global_var('func_1523')
func_1526_call = mutated_mod.get_global_var('func_1526')
var_4929 = relay.var("var_4929", dtype = "int32", shape = (110,))#candidate|4929|(110,)|var|int32
const_4930 = relay.const([-6,6,9,6,-2,-4,5,6,-8,-3,2,-7,9,-6,-8,4,1,9,-7,3,-4,-6,-4,4,1,4,-3,4,10,-6,2,-4,7,-5,8,4,5,-3,-4,1,-8,1,-10,5,7,-8,-9,-2,-6,3,-6,-10,-8,-10,-3,10,-7,-3,7,5,-9,-3,-5,-7,3,-9,-6,10,3,8,10,-7,10,4,-10,-1,1,-7,8,-1,3,-2,8,-3,-1,-7,1,-7,-8,10,9,-6,5,9,9,-6,10,9,9,9,5,10,3,-8,-8,8,-10,-8,-10,-8,-8,1,-4,6,-4,-3,4,-6,-3,-6,3,-8,10,5,6,-1,2,2,2,-1,-6,9,10,-5,-10,-3,4,-5,1,4,-5,-10,7,-5,2,9,-10,8,-4,4,3,-8,-1,1,4,7,-2,-8,-3,-8,-9,-2,5,-1,-2,-4,2,-4,-6,-5,2,-10,3,3,-3,10,8,-10,-4,4,6,1,-10,1,9,6,9,6,-6,-5,-10,8,9,-4,9,-8,-6,2,-3,-3,8,4,5,-9,-10,9,-3,9,7,4,-1,-2,1,-4,9,-7,-5,6,2,3,2,-2,-1,7,-4,5,-3,-4,-10,-1,6,-6,10,2,-7,-1,-9,6,-6,7,1,-7,8,1,10,9,-9,-6,8,8,-5,6,4,3,4,1,-1,-2,-2,6,-4,-7,-9,9,-2,-3,-9,-2,-3,-2,4,-2,4,1,8,5,4,4,-6,1,3,-9,-6,-5,6,6,1,-3,4,8,-3,6,8,1,5,5,9,-8,5,-4,1,10,-9,-8,1,7,-2,1,2,-3,5,5,-2,-9,-8,-7,-4,-2,2,-8,-7,-6,7,-8,-1,-8,-9,-2,-7,7,5,-6,-10,4,8,4,-8,-4,-8,-5,-3,5,7,-4,-10,2,4,-6,8,-8,-3,-4,3,-5,-10,9,-5,-9,4,9,-4,-9,10,-5,-7,-5,-3,1,-6,-6,9,4,-10,8,-6,-7,-1,9,2,-10,-6,9,-5,-5,9,1,-7,-3,8,2,-2,4,-3,-5,-6,-6,-1,4,-5,8,2,-3,-4,7,-10,4,8,-3,3,-8,4,-3,-8,2,-6,9,-2,9,9,-6,7,-10,9,5,-3,1,6,-4,-3,-10,-1,-8,-1,6,5,8,-3,-4,-4,-4,-4,6,-3,6,9,4,5,10,9,8,10,-3,-6,7,7,-9,-8,-1,-5,6,3,3,-10,-5,-1,-10,-3,-5,-1,1,4,9,4,5,-6,-3,-1,-6,1,9,-6,-6,3,8,-4,1,8,1,9,9,-9,4,-1,10,-2,6,7,5,-3,-5,1,-4,8,-10,3,4,-4,-9,-7,-6,7,4,-4,-5,3,2,10,2,-3,-4,-4,6,7,2,6,10,10,9,-7,10,6,4,10,-3,10,7,6,-9,-3,-6,9,-2,3,2,6,10,6,8,-1,8,8,3,-3,8,3,4,-9,-2,6,2,8,3,-7,-1,-10,8,-8,-4,3,-6,-4,-10,-5,-9,8,4,-5,-1,6,9,-3,-5,-9,-4,9,-3,-10,-9,-7,7,-2,-1,-8,9,4,-1,6,10,5,10,-3,10,-5,-2,9,-8,-10,6,-9,1,3,-2,10,-4,7,-10,6,6,10,4,7,8,10,7,-9,5,-2,2,-1,8,2,-10,7,2,6,-5,-9,-4,9,8,-2,1,-2,-8,9,2,-4,-10,2,6,-9,3,-6,-4,-8,2,-7,-6,5,-1,9,-8,10,4,1,10,-1,-5,-1,1,-1,-1,-5,7,-2,6,6,4,1,5,-8,-9,9,-7,3,2,-2,-4,10,8,-2,5,6,1,9,-7,-3,7,10,-4,3,-9,-1,-1,4,4,2,1,9,5,-10,-5,9,-6,-8,-4,-10,-6,-5,3,6,5,-7,6,-8,5,3,2,-4,3,-1,-2,1,2,-3,-7,-2,-7,-9,-6,3,-5,-1,-10,-5,8,-9,9,-6,-10,-7,10,-9,10,-1,5,6,-2,-8,6,5,-1,2,-6,2,9,-3,1,-9,10,-5,-6,6,2,10,7,-9,10,8,-10,-2,-2,-2,-8,1,-1,-4,9,-2,-6,-6,6,1,5,-1,-4,7,-9,6,-8,-5,3,-5,-3,-3,9,-2,-3,2,6,6,-6,3,-2,5,8,-10,-1,-5,-1,-3,-8,-7,2,10,1,-8,-8,6,-2,1,-1,2,3,-6,6,5,6,4,1,6,9,-1,-6,9,8,-9,1,10,-1,-10,-8,2,9,4,1,2,-5,-8,-1,-9,9,5,1,5,4,10,2,-7,-7,9,-2,-7,3,8,-4,-3,6,4,5,-9,5,-10,9,-6,-10,-4,5,9,-9,-3,5,8,8,-9,1,2,5,-1,-1,1,-1,4,-8,-7,2,-2,8,8,-3,-8,3,10,-4,-4,-7,8,2,7,5,-7,-4,1,2,-7,-6,-9,5,-9,-10,7,10,7,-5,9,6,6,8,1,9,-7,1,8,-7,8,-1,-5,8,10,8,-5,9,4,3,9,3,8,6,-3,-4,10,-6,6,-9,-9,-10,-1,8,-8,3,2,5,-2,-8,4,4,9,1,3,-4,6,9,-2,-5,7,-8,-3,-8,6,8], dtype = "int32")#candidate|4930|(990,)|const|int32
call_4928 = relay.TupleGetItem(func_1523_call(relay.reshape(var_4929.astype('int32'), [1, 10, 11]), relay.reshape(const_4930.astype('int32'), [9, 10, 11]), ), 1)
call_4931 = relay.TupleGetItem(func_1526_call(relay.reshape(var_4929.astype('int32'), [1, 10, 11]), relay.reshape(const_4930.astype('int32'), [9, 10, 11]), ), 1)
func_3905_call = mod.get_global_var('func_3905')
func_3907_call = mutated_mod.get_global_var('func_3907')
call_4933 = func_3905_call()
call_4934 = func_3905_call()
func_1975_call = mod.get_global_var('func_1975')
func_1976_call = mutated_mod.get_global_var('func_1976')
call_4937 = relay.TupleGetItem(func_1975_call(), 0)
call_4938 = relay.TupleGetItem(func_1976_call(), 0)
output = relay.Tuple([call_4926,call_4928,var_4929,const_4930,call_4933,call_4937,])
output2 = relay.Tuple([call_4927,call_4931,var_4929,const_4930,call_4934,call_4938,])
func_4942 = relay.Function([var_4929,], output)
mod['func_4942'] = func_4942
mod = relay.transform.InferType()(mod)
mutated_mod['func_4942'] = func_4942
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4943 = relay.var("var_4943", dtype = "int32", shape = (110,))#candidate|4943|(110,)|var|int32
func_4942_call = mutated_mod.get_global_var('func_4942')
call_4944 = func_4942_call(var_4943)
output = call_4944
func_4945 = relay.Function([var_4943], output)
mutated_mod['func_4945'] = func_4945
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4882_call = mod.get_global_var('func_4882')
func_4884_call = mutated_mod.get_global_var('func_4884')
call_5001 = relay.TupleGetItem(func_4882_call(), 0)
call_5002 = relay.TupleGetItem(func_4884_call(), 0)
func_1760_call = mod.get_global_var('func_1760')
func_1766_call = mutated_mod.get_global_var('func_1766')
const_5024 = relay.const([5,-7,-7,5,-9,6,6,1,-9,-5,9,-3,5,-10,-8,6,-2,6,-10,-1,-10,5,6,4,-7,6,9,2,5,6,-3,-9,-7,-4,-5,-6,-2,1,-6,-5,5,10,1,8,6,-1,8,3,4,4,2,4,-2,-4,-1,-3,2,-2,7,-9,4,3,-10,1,4,3,9,4,4,2,-8,-6,10,3,8,2,10,5,-2,5,-4,-3,-8,4,6,-7,-3,-5,1,-10,-8,2,-10,9,5,-9,2,2,1,-2,-2,-1,4,-7,4,5,-2,1,3,-3], dtype = "int32")#candidate|5024|(110,)|const|int32
const_5025 = relay.const([9,-7,5,-7,-5,8,5,4,6,-1,-9,7,6,-1,10,2,1,-2,-7,5,-9,10,4,8,-1,10,-6,1,1,-1,-5,-2,-4,5,3,-5,-3,-8,10,-9,-9,-2,-8,-4,-6,9,10,10,-6,-5,-6,-3,5,8,-9,6,-5,-2,-3,1,-1,-3,-4,5,7,-10,10,4,5,1,-6,-2,7,-4,-2,2,-7,-6,-7,2,-1,-8,6,-6,-1,-4,4,-8,2,3,-8,7,1,6,-4,-1,1,-6,9,-7,-7,-9,-1,-3,-10,-8,3,-4,1,-2,10,-10,3,9,5,4,9,4,2,-2,6,-3,-5,5,8,-1,-1,1,-6,-7,8,-7,-9,-6,10,5,8,-7,6,-1,7,5,2,3,-8,-2,-6,-3,10,5,-7,-6,-8,-8,-2,9,10,9,-1,3,-5,-8,-4,3,10,5,-8,-2,3,3,10,7,7,5,10,-9,-5,-3,10,4,-4,9,8,-10,-3,8,-4,-7,-3,-9,10,-6,-7,-3,-5,-8,6,2,-1,6,-3,9,-9,8,-7,-5,-7,4,-7,10,6,2,-5,7,-5,10,-7,-7,5,10,-2,-1,-3,-2,5,-4,-10,-4,-9,3,-4,-3,-1,-1,8,10,-4,9,-7,-10,3,-3,10,-9,10,6,4,7,2,4,7,9,5,1,-9,4,6,-8,-7,-9,1,-1,5,-4,7,-4,-2,-8,-1,8,-1,-5,-2,-5,-9,5,10,-7,-5,-1,-9,-9,-9,7,-5,1,9,-4,10,9,-6,1,2,10,-9,2,-7,10,-7,8,-1,-9,-7,-1,-4,6,7,-5,-5,10,5,5,-2,-10,1,-10,-6,-5,6,8,8,-10,-1,-6,10,-4,8,1,-4,7,-6,8,-10,5,-10,-3,-8,3,-10,8,5,-8,-3,2,-9,-5,-8,9,7,-1,6,3,-1,-3,-7,2,7,6,-9,1,7,-5,8,-2,-7,-2,-1,6,3,-2,4,-4,-3,3,9,4,-10,1,-2,-3,-6,-3,-1,-8,10,-7,-3,7,3,2,4,8,-2,1,1,-4,-10,5,-5,8,-2,-4,-9,-3,-3,-4,8,10,-10,5,-7,-8,7,2,6,-9,-8,3,6,-10,10,5,-8,7,7,9,2,-3,-3,-1,7,-7,-5,-2,8,-9,8,4,8,-5,-5,9,2,-6,-8,-5,-1,2,5,-8,-6,1,8,1,9,8,-10,3,10,-8,10,-5,-6,-6,1,-5,-8,2,-4,-3,8,-10,10,-10,-5,-9,4,4,1,2,-4,8,3,-10,-4,1,4,-10,-5,5,1,-6,9,4,10,3,-2,7,-2,4,10,8,7,10,-8,-5,-8,3,-9,-1,-10,-6,-5,8,2,5,-7,7,1,-7,2,-10,-3,10,-8,4,5,-10,2,2,-10,-5,-10,-3,10,3,-4,-4,4,8,5,1,9,-2,9,-7,1,-6,-4,3,8,8,9,-8,6,-4,-5,2,-6,7,6,-6,5,7,10,-7,-8,-2,-7,-1,-6,3,-9,7,7,3,-9,-2,1,-8,-3,-3,8,-9,6,7,4,3,-4,1,6,7,-4,-2,10,8,-2,4,4,6,-1,2,-2,-1,5,10,-7,-9,-7,6,8,9,-4,-2,6,10,1,-5,9,1,-7,7,9,-6,4,2,-7,4,5,4,5,1,8,-3,9,10,7,3,-3,10,3,1,-6,5,-4,3,3,-9,7,7,-6,-5,6,8,-6,-9,2,-1,7,-10,-5,2,6,-8,-3,-10,-3,1,10,1,8,7,1,8,3,1,-10,5,-4,8,9,-6,2,4,-9,-10,-6,-8,-4,-5,6,-5,8,-2,-5,8,8,-6,3,4,8,10,-10,9,7,-9,9,-9,5,9,-2,4,3,2,-2,2,2,-4,-10,-6,-8,-10,-10,3,-10,5,-1,2,9,-2,4,-10,5,9,-6,4,2,2,3,-7,-8,-3,-1,5,-2,-2,-10,-1,6,-2,-6,8,-10,-10,-6,6,-1,-4,-5,-4,-5,-1,9,-10,5,9,8,-9,-8,1,-6,-9,-5,1,2,-7,2,-2,4,-5,-5,8,4,4,-6,7,2,-1,10,9,7,-9,-5,-9,-4,-6,1,-4,1,8,-5,-9,2,5,4,-4,-1,-10,-5,-3,-5,9,5,10,3,3,-2,4,2,4,5,-7,-2,-1,7,-7,5,8,-1,-5,-6,-2,-1,-10,8,-1,5,-9,6,-5,8,-7,2,-2,-6,9,5,10,-10,9,6,2,9,-8,3,-7,-7,-3,-4,2,-2,-1,2,1,4,1,1,3,5,4,-7,1,9,-3,-9,-2,5,5,7,-1,-9,2,6,-1,-7,2,-8,-7,5,8,4,4,-3,1,7,2,-6,8,-10,-6,-4,2,-9,6,9,-9,-6,-6,-4,-9,-1,-6,7,-1,-1,-5,-5,-6,8,-10,8,1,4,10,-6,-6,-2,-4,-6,-8,-3,-3,-2,5,-1,-6,-4,-10,6,-4,-3,-9,-5,-5,-9,-10,-8,3,10,-9,-2,-9,-1,5,-10,-10,-1,9,-2,-9,-9,-7,1,-4,-7,1,7,-6,-10,-8,1,-5,-8,10,-9,3,7,-5,-10,-9,-4,-8,2,-1,-6,3,8,-2,2,-8], dtype = "int32")#candidate|5025|(990,)|const|int32
const_5026 = relay.const([1,1,-6,6,9,8,1,3,4,-3,-7,-5,-9,10,-10,-6,-1,-8,9,-4,4,-10,-4,8,-2,-5,4,-9,8,8,-10,-10,5,-8,2,5,-4,2,7,5,3,-10,1,9,9,-9,4,-10,7,-3,9,-6,4,10,10,-3,-7,-9,2,-10,-5,-10,10,8,-7,8,-1,-9,-6,8,-6,8,-4,4,5,7,-2,-9,-6,-2,9,6,-6,-7,-6,8,-8,7,-3,9,2,-10,-2,9,-7,8,-2,-6,-3,-3,-7,-3,9,-8,1,-2,5,9,10,-5,10,-3,-2,-5,1,6,-10,5,-8,-2,2,4,-8,7,3,-5,7,-9,4,-4,1,4,-10,1,-4,7,-8,5,3,4,-2,-1,4,8,4,-4,5,-6,-9,-2,-1,8,1,-5,-5,-2,-7,-8,3,-10,9,1,6,-8,4,7,-1,5,10,6,-7,2,9,7,-7,8,5,-1,-7,-5,9,4,-8,-9,9,6,2,-1,10,-5,-5,3,4,-10,-3,10,6,1,5,4,5,-9,8,10,-8,-4,-1,4,3,4,8,7,10,-9,7,-10,-3,-1,-10,10,-7,-2,3,4,1,-9,4,4,3,-10,7,5,10,1,-7,8,7,-2,8,-4,6,10,1,-5,-9,7,6,6,-7,3,-9,-6,3,-5,-8,1,-6,3,9,4,-2,4,4,-3,8,-3,-7,3,10,2,-1,-1,6,-4,9,-2,10,10,-5,-7,1,10,-10,9,-5,8,-5,-10,-3,7,2,-5,-3,-10,-2,-3,-6,10,-8,-6,1,6,4,-9,2,-1,3,-9,-2,7,4,6,3,-6,8,-3,-9,-5,6,-2,-7,-3,8,9,2,6,5,8,2,8], dtype = "int16")#candidate|5026|(330,)|const|int16
call_5023 = relay.TupleGetItem(func_1760_call(relay.reshape(const_5024.astype('int32'), [110,]), relay.reshape(const_5025.astype('int32'), [990,]), relay.reshape(const_5026.astype('int16'), [55, 6]), relay.reshape(const_5026.astype('int16'), [11, 10, 3]), ), 2)
call_5027 = relay.TupleGetItem(func_1766_call(relay.reshape(const_5024.astype('int32'), [110,]), relay.reshape(const_5025.astype('int32'), [990,]), relay.reshape(const_5026.astype('int16'), [55, 6]), relay.reshape(const_5026.astype('int16'), [11, 10, 3]), ), 2)
output = relay.Tuple([call_5001,call_5023,const_5024,const_5025,const_5026,])
output2 = relay.Tuple([call_5002,call_5027,const_5024,const_5025,const_5026,])
func_5028 = relay.Function([], output)
mod['func_5028'] = func_5028
mod = relay.transform.InferType()(mod)
mutated_mod['func_5028'] = func_5028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5028_call = mutated_mod.get_global_var('func_5028')
call_5029 = func_5028_call()
output = call_5029
func_5030 = relay.Function([], output)
mutated_mod['func_5030'] = func_5030
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2318_call = mod.get_global_var('func_2318')
func_2319_call = mutated_mod.get_global_var('func_2319')
call_5071 = relay.TupleGetItem(func_2318_call(), 0)
call_5072 = relay.TupleGetItem(func_2319_call(), 0)
func_2663_call = mod.get_global_var('func_2663')
func_2664_call = mutated_mod.get_global_var('func_2664')
call_5083 = relay.TupleGetItem(func_2663_call(), 2)
call_5084 = relay.TupleGetItem(func_2664_call(), 2)
output = relay.Tuple([call_5071,call_5083,])
output2 = relay.Tuple([call_5072,call_5084,])
func_5092 = relay.Function([], output)
mod['func_5092'] = func_5092
mod = relay.transform.InferType()(mod)
mutated_mod['func_5092'] = func_5092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5092_call = mutated_mod.get_global_var('func_5092')
call_5093 = func_5092_call()
output = call_5093
func_5094 = relay.Function([], output)
mutated_mod['func_5094'] = func_5094
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5098 = relay.var("var_5098", dtype = "float32", shape = (7, 2, 9))#candidate|5098|(7, 2, 9)|var|float32
uop_5099 = relay.rsqrt(var_5098.astype('float32')) # shape=(7, 2, 9)
uop_5109 = relay.sin(uop_5099.astype('float32')) # shape=(7, 2, 9)
output = relay.Tuple([uop_5109,])
output2 = relay.Tuple([uop_5109,])
func_5112 = relay.Function([var_5098,], output)
mod['func_5112'] = func_5112
mod = relay.transform.InferType()(mod)
var_5113 = relay.var("var_5113", dtype = "float32", shape = (7, 2, 9))#candidate|5113|(7, 2, 9)|var|float32
output = func_5112(var_5113)
func_5114 = relay.Function([var_5113], output)
mutated_mod['func_5114'] = func_5114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2318_call = mod.get_global_var('func_2318')
func_2319_call = mutated_mod.get_global_var('func_2319')
call_5122 = relay.TupleGetItem(func_2318_call(), 0)
call_5123 = relay.TupleGetItem(func_2319_call(), 0)
output = relay.Tuple([call_5122,])
output2 = relay.Tuple([call_5123,])
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
func_4841_call = mod.get_global_var('func_4841')
func_4843_call = mutated_mod.get_global_var('func_4843')
call_5154 = func_4841_call()
call_5155 = func_4841_call()
uop_5168 = relay.acos(call_5154.astype('float32')) # shape=(2145,)
uop_5170 = relay.acos(call_5155.astype('float32')) # shape=(2145,)
output = relay.Tuple([uop_5168,])
output2 = relay.Tuple([uop_5170,])
func_5178 = relay.Function([], output)
mod['func_5178'] = func_5178
mod = relay.transform.InferType()(mod)
mutated_mod['func_5178'] = func_5178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5178_call = mutated_mod.get_global_var('func_5178')
call_5179 = func_5178_call()
output = call_5179
func_5180 = relay.Function([], output)
mutated_mod['func_5180'] = func_5180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2276_call = mod.get_global_var('func_2276')
func_2278_call = mutated_mod.get_global_var('func_2278')
call_5196 = relay.TupleGetItem(func_2276_call(), 0)
call_5197 = relay.TupleGetItem(func_2278_call(), 0)
func_274_call = mod.get_global_var('func_274')
func_277_call = mutated_mod.get_global_var('func_277')
const_5224 = relay.const(-4, dtype = "uint16")#candidate|5224|()|const|uint16
call_5223 = func_274_call(relay.reshape(const_5224.astype('uint16'), []))
call_5225 = func_274_call(relay.reshape(const_5224.astype('uint16'), []))
output = relay.Tuple([call_5196,call_5223,const_5224,])
output2 = relay.Tuple([call_5197,call_5225,const_5224,])
func_5228 = relay.Function([], output)
mod['func_5228'] = func_5228
mod = relay.transform.InferType()(mod)
output = func_5228()
func_5229 = relay.Function([], output)
mutated_mod['func_5229'] = func_5229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2848_call = mod.get_global_var('func_2848')
func_2850_call = mutated_mod.get_global_var('func_2850')
call_5232 = relay.TupleGetItem(func_2848_call(), 0)
call_5233 = relay.TupleGetItem(func_2850_call(), 0)
func_3863_call = mod.get_global_var('func_3863')
func_3864_call = mutated_mod.get_global_var('func_3864')
call_5239 = relay.TupleGetItem(func_3863_call(), 0)
call_5240 = relay.TupleGetItem(func_3864_call(), 0)
func_5092_call = mod.get_global_var('func_5092')
func_5094_call = mutated_mod.get_global_var('func_5094')
call_5241 = relay.TupleGetItem(func_5092_call(), 1)
call_5242 = relay.TupleGetItem(func_5094_call(), 1)
output = relay.Tuple([call_5232,call_5239,call_5241,])
output2 = relay.Tuple([call_5233,call_5240,call_5242,])
func_5250 = relay.Function([], output)
mod['func_5250'] = func_5250
mod = relay.transform.InferType()(mod)
output = func_5250()
func_5251 = relay.Function([], output)
mutated_mod['func_5251'] = func_5251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4255_call = mod.get_global_var('func_4255')
func_4256_call = mutated_mod.get_global_var('func_4256')
call_5359 = relay.TupleGetItem(func_4255_call(), 0)
call_5360 = relay.TupleGetItem(func_4256_call(), 0)
func_2723_call = mod.get_global_var('func_2723')
func_2725_call = mutated_mod.get_global_var('func_2725')
call_5376 = func_2723_call()
call_5377 = func_2723_call()
output = relay.Tuple([call_5359,call_5376,])
output2 = relay.Tuple([call_5360,call_5377,])
func_5378 = relay.Function([], output)
mod['func_5378'] = func_5378
mod = relay.transform.InferType()(mod)
output = func_5378()
func_5379 = relay.Function([], output)
mutated_mod['func_5379'] = func_5379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2848_call = mod.get_global_var('func_2848')
func_2850_call = mutated_mod.get_global_var('func_2850')
call_5380 = relay.TupleGetItem(func_2848_call(), 1)
call_5381 = relay.TupleGetItem(func_2850_call(), 1)
output = relay.Tuple([call_5380,])
output2 = relay.Tuple([call_5381,])
func_5404 = relay.Function([], output)
mod['func_5404'] = func_5404
mod = relay.transform.InferType()(mod)
output = func_5404()
func_5405 = relay.Function([], output)
mutated_mod['func_5405'] = func_5405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1474_call = mod.get_global_var('func_1474')
func_1475_call = mutated_mod.get_global_var('func_1475')
call_5447 = relay.TupleGetItem(func_1474_call(), 0)
call_5448 = relay.TupleGetItem(func_1475_call(), 0)
func_3984_call = mod.get_global_var('func_3984')
func_3985_call = mutated_mod.get_global_var('func_3985')
call_5456 = relay.TupleGetItem(func_3984_call(), 0)
call_5457 = relay.TupleGetItem(func_3985_call(), 0)
output = relay.Tuple([call_5447,call_5456,])
output2 = relay.Tuple([call_5448,call_5457,])
func_5458 = relay.Function([], output)
mod['func_5458'] = func_5458
mod = relay.transform.InferType()(mod)
mutated_mod['func_5458'] = func_5458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5458_call = mutated_mod.get_global_var('func_5458')
call_5459 = func_5458_call()
output = call_5459
func_5460 = relay.Function([], output)
mutated_mod['func_5460'] = func_5460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4882_call = mod.get_global_var('func_4882')
func_4884_call = mutated_mod.get_global_var('func_4884')
call_5530 = relay.TupleGetItem(func_4882_call(), 2)
call_5531 = relay.TupleGetItem(func_4884_call(), 2)
output = call_5530
output2 = call_5531
func_5535 = relay.Function([], output)
mod['func_5535'] = func_5535
mod = relay.transform.InferType()(mod)
output = func_5535()
func_5536 = relay.Function([], output)
mutated_mod['func_5536'] = func_5536
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5539 = relay.const([[[-6],[3]],[[10],[2]],[[2],[-1]],[[-2],[-5]],[[-6],[6]],[[8],[7]],[[5],[-4]],[[-10],[8]],[[7],[-10]],[[1],[-10]]], dtype = "uint8")#candidate|5539|(10, 2, 1)|const|uint8
var_5540 = relay.var("var_5540", dtype = "uint8", shape = (10, 2, 15))#candidate|5540|(10, 2, 15)|var|uint8
bop_5541 = relay.equal(const_5539.astype('bool'), var_5540.astype('bool')) # shape=(10, 2, 15)
output = bop_5541
output2 = bop_5541
func_5560 = relay.Function([var_5540,], output)
mod['func_5560'] = func_5560
mod = relay.transform.InferType()(mod)
mutated_mod['func_5560'] = func_5560
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5561 = relay.var("var_5561", dtype = "uint8", shape = (10, 2, 15))#candidate|5561|(10, 2, 15)|var|uint8
func_5560_call = mutated_mod.get_global_var('func_5560')
call_5562 = func_5560_call(var_5561)
output = call_5562
func_5563 = relay.Function([var_5561], output)
mutated_mod['func_5563'] = func_5563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3114_call = mod.get_global_var('func_3114')
func_3115_call = mutated_mod.get_global_var('func_3115')
call_5574 = relay.TupleGetItem(func_3114_call(), 0)
call_5575 = relay.TupleGetItem(func_3115_call(), 0)
func_1523_call = mod.get_global_var('func_1523')
func_1526_call = mutated_mod.get_global_var('func_1526')
const_5587 = relay.const([3,-9,-3,-2,-5,7,-1,-5,-9,-5,5,4,-5,6,6,-3,9,-5,-10,-7,-1,-7,5,7,10,-1,-7,10,-5,-9,10,-9,-5,9,-1,-2,-5,7,2,6,-5,9,-1,-4,-3,-7,-7,2,-3,9,9,8,-2,-6,10,-6,-8,-7,-4,-9,-5,10,5,4,-2,1,6,-7,-6,-3,-4,1,6,5,10,6,10,-7,-7,2,6,3,3,-8,-3,-5,-2,1,6,-7,-1,2,-3,6,-10,1,2,-5,6,-3,-6,7,7,-7,7,-9,-1,10,8,3], dtype = "int32")#candidate|5587|(110,)|const|int32
call_5586 = relay.TupleGetItem(func_1523_call(relay.reshape(const_5587.astype('int32'), [1, 10, 11]), relay.reshape(call_5574.astype('int32'), [9, 10, 11]), ), 0)
call_5588 = relay.TupleGetItem(func_1526_call(relay.reshape(const_5587.astype('int32'), [1, 10, 11]), relay.reshape(call_5574.astype('int32'), [9, 10, 11]), ), 0)
output = relay.Tuple([call_5574,call_5586,const_5587,])
output2 = relay.Tuple([call_5575,call_5588,const_5587,])
func_5590 = relay.Function([], output)
mod['func_5590'] = func_5590
mod = relay.transform.InferType()(mod)
output = func_5590()
func_5591 = relay.Function([], output)
mutated_mod['func_5591'] = func_5591
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5601 = relay.var("var_5601", dtype = "int32", shape = (16, 16, 13))#candidate|5601|(16, 16, 13)|var|int32
var_5602 = relay.var("var_5602", dtype = "int32", shape = (16, 16, 13))#candidate|5602|(16, 16, 13)|var|int32
bop_5603 = relay.greater_equal(var_5601.astype('bool'), relay.reshape(var_5602.astype('bool'), relay.shape_of(var_5601))) # shape=(16, 16, 13)
var_5616 = relay.var("var_5616", dtype = "int32", shape = (16, 16, 13))#candidate|5616|(16, 16, 13)|var|int32
bop_5617 = relay.equal(var_5601.astype('bool'), relay.reshape(var_5616.astype('bool'), relay.shape_of(var_5601))) # shape=(16, 16, 13)
output = relay.Tuple([bop_5603,bop_5617,])
output2 = relay.Tuple([bop_5603,bop_5617,])
func_5621 = relay.Function([var_5601,var_5602,var_5616,], output)
mod['func_5621'] = func_5621
mod = relay.transform.InferType()(mod)
var_5622 = relay.var("var_5622", dtype = "int32", shape = (16, 16, 13))#candidate|5622|(16, 16, 13)|var|int32
var_5623 = relay.var("var_5623", dtype = "int32", shape = (16, 16, 13))#candidate|5623|(16, 16, 13)|var|int32
var_5624 = relay.var("var_5624", dtype = "int32", shape = (16, 16, 13))#candidate|5624|(16, 16, 13)|var|int32
output = func_5621(var_5622,var_5623,var_5624,)
func_5625 = relay.Function([var_5622,var_5623,var_5624,], output)
mutated_mod['func_5625'] = func_5625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1910_call = mod.get_global_var('func_1910')
func_1911_call = mutated_mod.get_global_var('func_1911')
call_5633 = func_1910_call()
call_5634 = func_1910_call()
func_4255_call = mod.get_global_var('func_4255')
func_4256_call = mutated_mod.get_global_var('func_4256')
call_5658 = relay.TupleGetItem(func_4255_call(), 2)
call_5659 = relay.TupleGetItem(func_4256_call(), 2)
output = relay.Tuple([call_5633,call_5658,])
output2 = relay.Tuple([call_5634,call_5659,])
func_5664 = relay.Function([], output)
mod['func_5664'] = func_5664
mod = relay.transform.InferType()(mod)
mutated_mod['func_5664'] = func_5664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5664_call = mutated_mod.get_global_var('func_5664')
call_5665 = func_5664_call()
output = call_5665
func_5666 = relay.Function([], output)
mutated_mod['func_5666'] = func_5666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2801_call = mod.get_global_var('func_2801')
func_2803_call = mutated_mod.get_global_var('func_2803')
call_5691 = relay.TupleGetItem(func_2801_call(), 1)
call_5692 = relay.TupleGetItem(func_2803_call(), 1)
output = call_5691
output2 = call_5692
func_5694 = relay.Function([], output)
mod['func_5694'] = func_5694
mod = relay.transform.InferType()(mod)
mutated_mod['func_5694'] = func_5694
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5694_call = mutated_mod.get_global_var('func_5694')
call_5695 = func_5694_call()
output = call_5695
func_5696 = relay.Function([], output)
mutated_mod['func_5696'] = func_5696
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2801_call = mod.get_global_var('func_2801')
func_2803_call = mutated_mod.get_global_var('func_2803')
call_5700 = relay.TupleGetItem(func_2801_call(), 1)
call_5701 = relay.TupleGetItem(func_2803_call(), 1)
const_5721 = relay.const([[[9],[-3],[7],[-3],[5],[-2],[7],[2],[2]],[[1],[3],[-10],[2],[8],[-9],[9],[7],[1]],[[7],[-9],[-8],[-7],[-10],[5],[3],[5],[-10]],[[8],[2],[-7],[-3],[1],[8],[5],[5],[-10]],[[-6],[10],[-3],[9],[-8],[5],[9],[1],[-7]],[[4],[-5],[-1],[-8],[2],[2],[-8],[6],[6]],[[2],[-9],[-2],[-10],[8],[-4],[-10],[-9],[5]],[[1],[8],[-9],[-3],[9],[-7],[-1],[10],[9]]], dtype = "uint8")#candidate|5721|(8, 9, 1)|const|uint8
bop_5722 = relay.not_equal(call_5700.astype('bool'), const_5721.astype('bool')) # shape=(8, 9, 1)
bop_5725 = relay.not_equal(call_5701.astype('bool'), const_5721.astype('bool')) # shape=(8, 9, 1)
output = relay.Tuple([bop_5722,])
output2 = relay.Tuple([bop_5725,])
func_5741 = relay.Function([], output)
mod['func_5741'] = func_5741
mod = relay.transform.InferType()(mod)
output = func_5741()
func_5742 = relay.Function([], output)
mutated_mod['func_5742'] = func_5742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3114_call = mod.get_global_var('func_3114')
func_3115_call = mutated_mod.get_global_var('func_3115')
call_5793 = relay.TupleGetItem(func_3114_call(), 0)
call_5794 = relay.TupleGetItem(func_3115_call(), 0)
const_5809 = relay.const([9.526195,-1.775970,7.274227,-4.927964,-5.916488,9.896719,9.062781,-6.393706,-0.031007,7.578198,8.723498,8.644364,9.143943,-1.924646,6.688365,-3.991815,3.750648,-1.441921,-5.145326,-7.288565,-5.458234,7.556502,3.141367,1.071028,-2.684390,1.034218,1.961328,-9.098849,-2.019170,8.507240,-2.881170,-2.742331,0.464232,-7.777480,-6.652079,-5.030699,-4.059084,-0.451289,-2.477475,-1.578059,1.494477,-3.488484,-7.072688,9.454877,4.591581,2.136092,4.367701,3.699991,-0.366096,-6.051203,-8.838037,2.481413,7.882799,-5.902550,6.762446,-4.680442,-6.529745,0.147916,6.535177,-9.322660,-2.213213,4.779707,1.992074,-7.569159,-3.091462,-0.434379,4.600307,-1.281353,-1.390192,-8.574448,0.019003,-1.747510,-8.390625,-1.464070,-7.965014,-6.086164,-8.909096,-8.360524,0.335901,-2.224467,-8.595727,-0.624356,-1.698793,-8.033447,-1.519354,0.095647,2.388521,4.904766,6.379213,-3.595005,-7.934650,-0.717261,-9.739079,4.628654,7.068415,7.771935,-4.628758,-3.241334,-3.621080,4.753041,1.893921,-1.760070,-3.230186,-1.944336,-4.760262,-2.068074,-2.508164,2.956710,3.063428,-9.802729,-7.457222,-2.006052,8.917042,-3.617695,1.068094,-9.561013,-4.885308,-8.571424,7.823936,-1.426196,0.688850,-9.269950,-4.759412,-1.488205,-6.761347,-1.925888,-1.293266,-4.424371,9.437781,-5.550924,-4.052846,-6.564920,7.025650,-1.203225,1.963180,-1.820672,3.943614,-6.204928,0.450240,3.539002,5.692757,-7.107581,6.532095,-2.060738,5.765471,7.474570,9.903158,-5.465143,-0.790380,2.499205,-8.756927,-6.886305,9.556834,8.985250,0.945275,-2.798119,-2.569576,5.482512,3.795634,9.953172,-8.366489,2.856613,-7.258769,-2.717989,-5.896049,-4.338462,-7.761215,-3.518528,-0.115346,-3.728942,-5.722134,-8.614257,3.572654,-1.365138,9.883764,-5.715568,4.614785,-0.814771,6.745632,-0.665828,-8.420642,-6.057331,-7.549513,-7.463945,-8.507403,-8.965191,-3.637704,-5.685850,-6.873285,-3.369323,-2.852970,1.671911,-0.462004,6.287846,5.227367,9.745582,-2.926614,-3.463728,-0.988856,1.047567,9.873263,-9.409335,5.417877,9.471491,1.318935,6.583316,-6.036316,0.802959,-0.550786,5.166548,2.063802,-1.382078,-4.748374,-1.955334,2.469212,-4.340740,3.729492,-0.814960,4.416564,4.239195,-9.654439,-0.258336,4.254003,1.005007,-3.057393,6.495109,-5.219331,1.459654,-4.971236,2.096004,-3.871080,-2.783372,-5.584860,-8.637026,2.498705,2.494577,-8.844026,-8.584623,5.200002,-0.535898,-6.748738,6.802207,1.081102,-3.866734,-0.525634,8.626486,3.467573,9.690011,5.411129,4.025846,4.424705,-6.548327,-3.434247,0.865834,-7.101402,8.920094,-3.665290,2.565279,7.208569,4.487792,-6.589166,-4.463783,8.358482,2.731355,3.087649,3.684274,4.128983,7.455310,-5.439841,-9.129128,-8.473845,-9.370369,-6.849638,-1.824292,9.416196,-6.041271,-6.955163,4.071088,-1.085785,-5.756263,2.215382,-2.775529,6.582274,-1.982462,-8.493971,8.440276,-3.059716,5.841876,0.330008,-6.149896,-2.067657,-5.976514,-9.322368,-2.271380,5.436088,-7.969654,-9.684692,1.604797,-0.367485,1.739699,-0.867230,9.030788,-6.502430,-2.577770,-7.708065,-5.623136,6.361515,-4.751976,-8.960422,-2.574477,0.991946,-0.206141,7.533882,-0.490946,1.334957,-4.153454,-4.793872,-9.096335,2.529738,-5.741882,-4.714365,-1.583344,-7.983253,8.303895,9.583006,-1.499452,-9.831004,-9.578740,-0.114514,-8.652053,-0.815763,-2.282881,-9.978449,-0.366679,5.958547,-6.402943,1.425570,7.206204,6.123003,4.595430,-4.937993,4.366226,-0.537983,-5.944771,-7.352674,4.614463,6.842902,0.455234,-3.853208,3.545723,7.864156,3.493465,-7.430397,-9.345709,0.229878,-8.563820,6.887759,7.306776,4.433643,-8.665463,-4.958510,2.028168,0.879811,4.498469,-3.116663,8.202125,-1.494560,-4.788521,0.857204,-5.435958,-3.861589,-5.928842,6.358674,-7.290075,2.860158,-3.146857,-6.869638,-3.558642,6.434878,1.116188,-2.502938,6.179432,-0.770358,-5.686180,-7.579191,-3.308751,2.565762,-5.841617,-3.638545,-4.247304,9.481400,0.447949,-9.334946,-8.392401,-9.781264,0.430936,-1.713688,4.627129,-6.101071,7.454268,8.553614,-8.046468,-4.056193,5.569644,5.493095,4.420231,-7.278515,-6.952668,-8.829520,-1.753436,-2.749949,6.488098,-9.696703,8.627343,-0.264765,2.595037,6.218660,8.167723,-4.988000,-2.755342,-3.726389,5.440222,1.488443,9.502939,-5.148875,-0.334266,8.303454,0.509033,-3.294571,-3.299565,9.391284,-3.286511,5.834479,6.587809,-9.748854,6.880816,1.829269,-0.487455,-1.872432,-1.602397,7.319105,-9.503482,-5.961981,1.937397,-5.174217,-1.930067,8.492979,-6.362384,-9.936513,3.236035,-3.902409,8.240286,3.655633,-4.985431,0.935245,-0.607850,4.133155,1.784787,-6.532193,-7.712549,-9.008280,2.176071,-2.287218,9.811368,2.038573,0.673329,5.258472,6.421465,-5.083724,0.602058,-1.468930,7.198552,-0.704878,7.880618,6.101782,2.878079,-8.458485,0.913861,5.651316,8.335643,2.736367,-6.515631,1.470169,0.435815,6.441205,0.315748,-8.987105,1.178787,4.442189,-5.040821,-0.222721,2.746141,-7.337285,2.408576,0.540588,-6.296129,-9.960942,6.144019,-8.890727,2.241131,7.504276,4.655564,7.355430,-4.560851,6.412188,6.695917,6.365512,3.959901,-7.038201,8.106201,6.421317,-4.799531,-5.978904,-2.062288,5.296427,-5.631307,-9.950493,-8.435019,-9.515086,7.826389,8.849874,8.402256,5.278611,-3.869362,-1.406953,7.605046,6.032302,1.380052,1.683234,-7.616119,5.593160,-9.994278,-1.707496,-7.242585,5.548688,7.052922,-0.979182,6.615722,0.325646,7.761998,5.308895,2.797595,9.211465,-2.638373,-2.058512,6.330870,9.820556,-4.045727,-2.220269,-2.695752,-3.477376,0.973086,9.042493,-6.060223,-4.383814,-2.786145,-6.890855,6.068015,-4.649776,-5.367346,-0.361250,-0.151214,0.888007,-2.757700,3.163844,-5.724526,-7.402355,7.543017,-9.550211,-9.011284,4.787651,1.717452,-7.828379,0.295319,-6.683934,-7.514159,1.330514,1.931253,9.588432,0.729260,-0.802750,-3.999395,2.500747,-7.510197,4.490251,-6.162858,6.254243,-4.104828,-1.952879,-9.828638,5.867432,-6.042565,-8.028885,-3.262263,7.612082,-0.877901,1.004871,-5.706288,-1.674654,-4.051212,6.808524,9.926817,-6.400876,-3.680133,4.130952,-1.035502,5.837911,-9.986929,-1.760481,2.911422,-2.874640,0.992977,-0.174463,-5.806825,8.798542,-2.532795,2.899886,4.341352,0.286131,1.170671,0.610228,-6.345760,-8.966748,-4.933763,7.839897,-8.279919,1.294007,3.554479,7.395460,0.274361,-5.155925,4.833605,8.862674,-5.461069,-2.036175,3.401331,2.820511,3.275977,-6.366049,-8.267553,0.395893,6.759166,-8.646626,2.907952,-5.009683,-7.318173,-4.790344,8.883981,1.699717,4.389025,9.921355,9.117549,-3.518302,-3.619657,-4.282951,-9.160528,6.595968,-4.578164,-4.649908,7.955781,-1.301739,7.364975,3.715148,-6.302239,-1.524871,-4.353927,9.288170,-2.417019,-6.040618,-9.349081,8.141827,3.448376,0.469636,2.428717,8.336133,-7.785769,-0.769098,-0.158333,-7.749409,-7.444459,-9.213811,-9.346562,-2.888753,2.324855,2.359294,8.040851,-7.739434,7.611858,9.771015,6.386574,8.342178,-7.179276,-8.511911,4.137982,-2.211591,3.106158,0.980056,-0.610646,2.548491,-9.228728,7.035255,2.670254,-4.379520,3.894766,7.749897,-6.568087,4.779540,1.701528,-6.565545,-2.916830,-1.397109,3.426107,-2.121202,-2.642584,-7.036899,-2.867328,-4.361782,0.601873,5.821949,-1.407317,-9.089836,5.587287,-7.894536,3.771007,-3.387285,6.962159,7.371083,-3.319777,-2.147753,5.061748,5.165232,-4.952426,-2.250994,4.115916,4.604781,-3.443938,-6.145244,9.768539,-0.868932,7.187749,-6.336444,-7.131923,-7.087724,7.666501,2.073360,3.367250,0.952481,-4.138488,5.126715,8.536202,-2.611039,-9.503543,7.785929,6.533963,-4.869409,-2.685026,9.924697,2.654569,5.391418,-6.110743,7.917355,-5.899423,5.476836,-8.790243,-8.346141,0.270122,-6.191383,9.367881,7.025185,9.675373,-9.815053,6.331939,-9.431108,6.313330,1.558264,-2.091389,7.017061,8.689677,-1.933988,5.734148,2.442935,7.446461,3.099937,-6.049019,3.355447,-0.517674,2.271388,7.575755,-1.698137,-7.488930,-2.962181,9.122532,2.301448,-3.849697,-3.319697,-7.218070,5.405244,9.392902,-9.640981,5.682628,-0.754527,0.213970,5.400057,1.311579,3.604328,-6.025541,9.764068,0.333109,-0.330881,-1.253027,-0.713681,3.262489,-3.864070,-4.162696,-0.663410,-7.855904,2.097177,-1.037226,-5.571552,3.906642,7.060767,6.069398,6.651161,4.196162,-9.067072,-8.475057,-3.366752,-6.066054,2.882381,-4.225240,5.940811,-8.328083,-2.987975,4.860865,-8.923620,2.490558,-1.071296,-9.490556,5.266842,-0.806441,9.911658,-2.927614,-7.733186,-9.312337,0.954686,0.350979,7.565949,-5.818097,-1.865211,-9.808610,-9.824849,3.711584,-3.762577,-4.883065,7.477980,-9.253547,8.141225,4.817081,4.771010,2.674603,-1.658564,6.493675,-0.678237,5.336413,-7.624706,-7.057954,9.980295,3.921783,8.007296,-5.903707,-9.232238,-5.563840,9.132347,1.127088,2.000469,-7.593506,3.725978,-8.198263,9.929797,7.520166,3.211635,-1.659620,8.585071,7.355929,1.130236,4.103391,-8.279264,0.617239,7.633987,-9.123894,-7.164203,-9.760936,3.842905,8.480663,3.432456,-1.285176,-0.500650,3.584574,-4.149778,4.874511,-6.484228,-0.259101,-7.642407,4.624566,-5.415203,-0.136796,-1.270141,4.088066,2.634409,-0.901783,8.458726,-0.815572,6.318642,6.523806,-9.867145,0.326403,5.830755,0.272690,0.711497,-5.553233,-4.816739,-0.755186,8.127441,-5.428163,1.957044,7.190559,4.312528,-5.678153,-9.241140,8.608377,-9.257045,8.986728,-2.690975,8.268869,2.322862,6.572760,3.149530,-3.611300,1.168381,1.701241,5.492041,8.090241,-3.487528,2.251806,9.503990,5.125022,2.081520,-2.592820,1.653728,-8.153266,6.571220,8.772474,2.585832,0.112106,-1.151007,9.164216,-0.123949,1.258694,6.760468,7.009333,5.561311,-6.181458,1.365881,-3.400666,1.567726,-5.380123,-9.666761,2.983838,4.910769,2.474383,5.093811,-8.350705,4.920992,7.271310,-3.405350,-1.474195,1.267457,9.334072,0.618815,-4.690188,-4.634696,3.461311,-9.903380,-6.256949,6.919378,7.982694,1.400247,-2.634159,9.259128,1.179827], dtype = "float32")#candidate|5809|(990,)|const|float32
bop_5810 = relay.right_shift(call_5793.astype('int32'), relay.reshape(const_5809.astype('int32'), relay.shape_of(call_5793))) # shape=(990,)
bop_5813 = relay.right_shift(call_5794.astype('int32'), relay.reshape(const_5809.astype('int32'), relay.shape_of(call_5794))) # shape=(990,)
output = relay.Tuple([bop_5810,])
output2 = relay.Tuple([bop_5813,])
func_5815 = relay.Function([], output)
mod['func_5815'] = func_5815
mod = relay.transform.InferType()(mod)
output = func_5815()
func_5816 = relay.Function([], output)
mutated_mod['func_5816'] = func_5816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5250_call = mod.get_global_var('func_5250')
func_5251_call = mutated_mod.get_global_var('func_5251')
call_5846 = relay.TupleGetItem(func_5250_call(), 2)
call_5847 = relay.TupleGetItem(func_5251_call(), 2)
output = relay.Tuple([call_5846,])
output2 = relay.Tuple([call_5847,])
func_5852 = relay.Function([], output)
mod['func_5852'] = func_5852
mod = relay.transform.InferType()(mod)
output = func_5852()
func_5853 = relay.Function([], output)
mutated_mod['func_5853'] = func_5853
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3759_call = mod.get_global_var('func_3759')
func_3761_call = mutated_mod.get_global_var('func_3761')
call_5882 = relay.TupleGetItem(func_3759_call(), 1)
call_5883 = relay.TupleGetItem(func_3761_call(), 1)
func_3863_call = mod.get_global_var('func_3863')
func_3864_call = mutated_mod.get_global_var('func_3864')
call_5888 = relay.TupleGetItem(func_3863_call(), 0)
call_5889 = relay.TupleGetItem(func_3864_call(), 0)
func_4591_call = mod.get_global_var('func_4591')
func_4593_call = mutated_mod.get_global_var('func_4593')
call_5897 = func_4591_call()
call_5898 = func_4591_call()
output = relay.Tuple([call_5882,call_5888,call_5897,])
output2 = relay.Tuple([call_5883,call_5889,call_5898,])
func_5911 = relay.Function([], output)
mod['func_5911'] = func_5911
mod = relay.transform.InferType()(mod)
output = func_5911()
func_5912 = relay.Function([], output)
mutated_mod['func_5912'] = func_5912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4786_call = mod.get_global_var('func_4786')
func_4787_call = mutated_mod.get_global_var('func_4787')
call_5948 = relay.TupleGetItem(func_4786_call(), 0)
call_5949 = relay.TupleGetItem(func_4787_call(), 0)
output = call_5948
output2 = call_5949
func_5952 = relay.Function([], output)
mod['func_5952'] = func_5952
mod = relay.transform.InferType()(mod)
mutated_mod['func_5952'] = func_5952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5952_call = mutated_mod.get_global_var('func_5952')
call_5953 = func_5952_call()
output = call_5953
func_5954 = relay.Function([], output)
mutated_mod['func_5954'] = func_5954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2663_call = mod.get_global_var('func_2663')
func_2664_call = mutated_mod.get_global_var('func_2664')
call_5970 = relay.TupleGetItem(func_2663_call(), 2)
call_5971 = relay.TupleGetItem(func_2664_call(), 2)
const_5972 = relay.const([[[-0.529118,6.200105,3.879722,-1.123102,1.046416,1.884367,-5.375647,8.460742,-3.165403,5.388514],[-3.524800,8.391947,-3.829499,-1.687744,-3.658337,1.090170,5.226291,9.677705,4.096415,4.685339],[7.511414,2.988257,-8.112122,9.862352,-6.264606,-6.723071,-4.662469,3.362016,4.658177,9.400819]],[[7.810245,-8.581524,5.204486,6.311834,2.150663,3.940844,0.643561,-5.695177,7.114900,2.356921],[0.557164,5.590782,2.338477,-4.568622,-6.362354,-7.703180,-7.831842,-7.619163,-3.699148,6.554210],[-5.945146,0.155007,5.049742,3.289384,0.127782,-6.631635,8.784102,4.092525,8.831999,3.897251]],[[5.180290,3.499565,7.826088,0.764068,-9.874689,3.096143,-7.575606,-7.929804,1.115178,-6.270540],[-8.794519,9.864251,-1.180395,-6.303037,-3.627366,-3.392611,-8.250491,4.856849,0.123003,7.132379],[8.793023,5.168073,4.525757,-0.725248,6.510067,-8.856270,5.209625,7.739715,-8.232117,7.852034]],[[-9.226489,-2.047534,-3.464311,-4.092812,-8.563094,4.139737,-0.168137,7.455837,-6.605798,-1.094655],[3.031985,-5.019538,-5.982039,-8.158207,3.111330,1.502296,1.558098,-8.522473,-4.773541,-7.498307],[2.196836,-2.419049,-7.119272,0.101656,5.285754,-4.715870,-9.200846,-3.457138,9.478872,8.640735]],[[-8.725648,-3.054246,-1.294471,1.562922,3.349187,-0.053833,7.950734,-5.283806,-9.704490,5.581236],[-9.261232,-4.370845,-3.259445,0.856474,-8.519804,-5.138597,-6.614563,-8.714702,-3.702753,7.055198],[5.256352,-5.638453,-8.190746,-1.651926,-4.413921,9.760500,-5.574547,-7.726957,-1.190254,-4.793367]],[[-1.044381,1.761467,0.371675,-2.518021,-6.551334,1.902696,2.984063,-6.989842,-4.748745,-3.259498],[-2.752100,0.872788,-4.846706,7.859963,-3.735998,6.519595,1.030486,5.230784,-8.014314,-2.067622],[4.897389,4.144075,7.541257,-6.106183,-2.959056,-9.612639,-1.225881,6.723846,6.572312,8.672528]],[[-2.661466,9.433621,-3.515388,-6.972471,-9.426301,5.107613,-7.895480,-2.636666,-1.517560,-8.446835],[6.626358,-2.102323,-1.996202,-8.036317,-7.381478,1.996755,-5.062071,-5.837467,2.003976,-4.510926],[9.109890,4.231816,-4.525077,2.677935,4.377255,2.183472,1.221163,-6.186617,-1.128305,2.544682]],[[2.930314,4.081148,1.686594,-4.891198,8.411936,-6.993422,-1.076278,-2.280210,1.429232,0.693172],[5.654126,-6.582451,-1.507958,1.523236,5.213424,-3.295744,5.362729,1.359881,3.803136,-9.052326],[-3.344049,-2.084187,-5.258531,8.370831,-0.961033,-8.449519,2.498412,-9.367291,-9.684432,-1.802728]]], dtype = "float32")#candidate|5972|(8, 3, 10)|const|float32
bop_5973 = relay.greater_equal(call_5970.astype('bool'), relay.reshape(const_5972.astype('bool'), relay.shape_of(call_5970))) # shape=(8, 3, 10)
bop_5976 = relay.greater_equal(call_5971.astype('bool'), relay.reshape(const_5972.astype('bool'), relay.shape_of(call_5971))) # shape=(8, 3, 10)
func_3052_call = mod.get_global_var('func_3052')
func_3054_call = mutated_mod.get_global_var('func_3054')
call_6002 = relay.TupleGetItem(func_3052_call(), 0)
call_6003 = relay.TupleGetItem(func_3054_call(), 0)
output = relay.Tuple([bop_5973,call_6002,])
output2 = relay.Tuple([bop_5976,call_6003,])
func_6017 = relay.Function([], output)
mod['func_6017'] = func_6017
mod = relay.transform.InferType()(mod)
output = func_6017()
func_6018 = relay.Function([], output)
mutated_mod['func_6018'] = func_6018
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6026 = relay.var("var_6026", dtype = "float64", shape = (16, 11, 8))#candidate|6026|(16, 11, 8)|var|float64
var_6027 = relay.var("var_6027", dtype = "float64", shape = (16, 11, 8))#candidate|6027|(16, 11, 8)|var|float64
bop_6028 = relay.divide(var_6026.astype('float64'), relay.reshape(var_6027.astype('float64'), relay.shape_of(var_6026))) # shape=(16, 11, 8)
output = relay.Tuple([bop_6028,])
output2 = relay.Tuple([bop_6028,])
func_6031 = relay.Function([var_6026,var_6027,], output)
mod['func_6031'] = func_6031
mod = relay.transform.InferType()(mod)
mutated_mod['func_6031'] = func_6031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6031_call = mutated_mod.get_global_var('func_6031')
var_6033 = relay.var("var_6033", dtype = "float64", shape = (16, 11, 8))#candidate|6033|(16, 11, 8)|var|float64
var_6034 = relay.var("var_6034", dtype = "float64", shape = (16, 11, 8))#candidate|6034|(16, 11, 8)|var|float64
call_6032 = func_6031_call(var_6033,var_6034,)
output = call_6032
func_6035 = relay.Function([var_6033,var_6034,], output)
mutated_mod['func_6035'] = func_6035
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6107 = relay.const([[[-10,-8,-5,7,8,-2,-1,-5,7],[4,7,1,-4,10,-9,-7,5,3],[-2,8,10,-4,-8,-4,8,-1,9],[6,6,-1,-8,6,-4,5,-7,-3],[-4,-8,7,-1,1,7,4,3,-1],[5,-3,-5,9,-10,-5,-3,-9,5],[-4,-8,-6,7,10,10,-6,-1,5],[5,-5,10,7,1,6,-1,-10,-7],[6,6,6,7,10,-1,3,-1,-1],[8,-8,-6,-5,-7,8,1,10,9]],[[-5,5,6,2,-2,-6,6,2,3],[10,-5,-2,1,-8,-3,4,-5,3],[7,-1,-8,3,-10,-10,3,2,-7],[2,8,-6,8,8,10,-7,7,-7],[4,1,-5,9,-2,-7,-3,-4,10],[1,3,3,1,2,7,-2,-1,5],[5,5,4,6,-2,8,2,2,-1],[9,-7,9,-2,7,6,-1,-7,-10],[-10,-8,-7,-6,8,-6,-5,2,-6],[9,5,-3,-9,4,5,-7,-10,-9]],[[3,-8,5,3,-7,-5,-7,-4,10],[3,-6,-7,1,-7,-1,8,4,-7],[7,3,5,10,-2,-2,4,4,-2],[-2,-5,2,5,-9,3,10,-4,-6],[10,-10,-2,7,-10,5,-1,3,-6],[-1,-4,-8,4,8,10,8,-10,4],[-3,-8,-1,-2,-2,8,1,-6,8],[3,3,-4,5,-5,-2,-9,-10,-5],[1,-5,4,10,-3,-10,4,6,5],[4,-2,7,10,7,2,-2,1,6]],[[1,3,-4,-6,6,-8,2,3,1],[-5,3,-10,6,-9,-9,4,-3,-3],[-10,7,-3,-9,5,8,-9,6,7],[-10,-7,-3,4,-6,4,3,-2,-10],[-3,9,-10,-5,-2,-2,8,5,10],[2,5,8,1,3,-10,-6,3,-3],[4,1,-1,-6,-6,-6,7,8,-8],[-1,-10,2,-9,-4,-6,5,-9,6],[1,10,-3,4,4,3,-2,3,-1],[1,3,-10,4,-1,-2,-2,-10,-2]],[[9,-4,2,9,4,-4,-6,4,-2],[-10,-2,9,9,8,-6,-4,-8,1],[8,2,9,6,2,-7,-6,3,10],[-3,5,-10,-4,9,-5,-4,8,4],[3,-7,3,1,10,9,-8,-3,-8],[8,-7,5,-7,4,4,-7,9,-4],[-5,-4,-3,-9,7,-3,-4,6,8],[-5,10,-2,-9,-3,-10,-3,-6,-4],[-9,-7,4,1,3,-9,-9,-7,6],[-3,-8,-5,5,-7,-2,7,1,-10]],[[-8,-3,6,-3,10,6,-1,1,7],[-10,-2,3,-8,-7,-6,6,-8,4],[-4,-1,-7,8,-9,-7,-3,-9,6],[10,4,-4,6,2,-10,-10,-3,9],[-9,8,-6,-4,-6,5,-7,-7,-4],[-9,3,-4,10,-7,6,-3,-3,-1],[-5,-7,10,-4,-6,-5,-2,-3,-6],[7,-3,-8,-10,-2,-9,-9,9,-7],[7,3,-2,4,-3,-8,3,6,8],[5,-5,1,1,2,6,-9,3,-6]],[[2,-9,-8,7,-10,7,7,8,-8],[-7,10,9,9,1,-1,6,-9,-2],[2,8,2,-2,7,2,2,4,-9],[10,-2,1,-9,9,-2,7,-8,-7],[-2,1,2,5,-5,6,2,3,6],[-9,2,5,9,-7,-6,-9,-5,8],[-4,-9,-3,-2,-10,1,10,3,8],[-6,-9,-3,-1,-5,-3,-2,-7,-5],[-8,7,5,-6,-8,6,6,-10,-9],[1,-7,6,1,-8,-1,-1,1,10]],[[8,10,-4,1,-10,-6,5,-9,-6],[-2,-3,5,3,-4,6,8,-10,1],[7,-6,2,-8,-9,-9,1,2,-2],[-9,-5,-9,9,-8,-8,-6,8,1],[-4,-6,3,-10,7,-2,10,-1,-6],[-9,-10,7,3,-10,-3,-2,-8,-4],[2,-9,7,-7,3,-2,-10,6,-8],[-7,-6,6,8,10,4,8,7,6],[-9,1,-3,-2,5,-3,3,-6,7],[-8,-9,2,2,1,9,3,2,-9]],[[6,8,-9,6,10,-1,-5,-3,-9],[8,-5,1,8,-10,-8,5,-10,7],[5,3,5,-4,3,3,-10,-3,1],[7,-8,10,-7,1,-10,-1,10,-2],[-8,-3,4,2,6,9,9,-7,-4],[-2,3,-2,-10,10,7,-4,8,5],[-3,8,-4,9,2,10,-4,-10,-8],[2,3,9,-3,4,-10,5,-6,5],[9,-3,9,-8,-8,1,-1,3,2],[6,4,-1,1,-8,-1,6,6,-1]],[[-5,-9,1,8,-1,-8,2,2,-5],[10,9,2,-8,9,10,-8,-3,7],[-7,4,5,-2,-7,2,-5,8,8],[-3,-10,2,-2,-4,-9,7,-7,3],[4,-8,-8,-4,3,-7,2,9,2],[-2,4,-9,9,7,8,8,5,-6],[-6,-6,-2,10,-2,-4,2,9,3],[9,4,8,7,-8,1,5,-2,-6],[1,8,7,-8,-9,-7,4,2,3],[2,5,-2,1,4,8,10,8,-5]],[[-10,-5,9,-1,9,3,-5,-2,2],[-9,-3,10,4,1,6,6,8,-6],[7,-1,3,8,8,10,-6,-7,-3],[10,-5,-9,6,10,1,4,3,2],[-1,4,2,1,5,9,-5,3,-10],[2,10,-4,7,-6,-5,-8,1,-8],[-8,-5,7,8,2,1,-6,2,2],[-6,3,-1,2,-5,-1,-10,-1,9],[6,9,1,-2,2,2,7,3,9],[10,-3,-6,7,-1,-8,8,10,-4]],[[7,5,-7,3,4,-7,10,-6,-4],[7,-8,-2,1,-2,9,-1,9,6],[-4,3,-7,-2,-8,1,-1,-5,-9],[7,7,10,-3,-2,8,2,9,1],[-8,4,-3,9,-3,5,9,1,-1],[-2,3,-9,-2,-4,-8,6,10,-1],[-4,7,3,9,-3,-10,5,-9,5],[-1,8,-9,-10,10,4,-1,2,-8],[-1,8,9,-8,-7,-3,2,-1,-9],[9,-5,9,10,10,1,8,-6,4]],[[2,2,-9,-6,-8,3,7,-9,1],[-4,10,-7,-3,-1,-1,6,8,-7],[-2,-10,-9,-10,-7,9,-4,10,-8],[-5,2,-3,2,6,-7,9,-5,-2],[1,9,8,5,2,8,-2,4,-10],[7,-6,3,6,-5,-8,5,8,7],[-3,-1,-8,6,1,-6,-7,-2,5],[-8,-7,4,-1,-5,3,6,6,1],[-6,6,9,10,-4,-8,-10,-4,9],[-2,-8,-1,1,-9,5,-3,-8,-8]],[[-10,2,-1,-4,7,5,5,8,6],[-6,-5,6,-6,-10,-7,-1,5,10],[4,-6,-2,-8,-10,-2,-4,-7,-3],[10,1,4,-8,-4,8,10,8,4],[-1,-8,-1,-9,-9,5,-9,-1,-6],[-10,-10,9,10,4,9,9,2,-1],[8,-9,8,10,10,-10,8,3,6],[-8,3,-6,1,10,-5,-8,3,-1],[-1,10,4,-10,-2,10,4,4,-1],[-8,6,-8,1,3,3,-6,-6,-8]]], dtype = "int64")#candidate|6107|(14, 10, 9)|const|int64
var_6108 = relay.var("var_6108", dtype = "int64", shape = (14, 10, 9))#candidate|6108|(14, 10, 9)|var|int64
bop_6109 = relay.logical_xor(const_6107.astype('int64'), relay.reshape(var_6108.astype('int64'), relay.shape_of(const_6107))) # shape=(14, 10, 9)
output = bop_6109
output2 = bop_6109
func_6140 = relay.Function([var_6108,], output)
mod['func_6140'] = func_6140
mod = relay.transform.InferType()(mod)
mutated_mod['func_6140'] = func_6140
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6141 = relay.var("var_6141", dtype = "int64", shape = (14, 10, 9))#candidate|6141|(14, 10, 9)|var|int64
func_6140_call = mutated_mod.get_global_var('func_6140')
call_6142 = func_6140_call(var_6141)
output = call_6142
func_6143 = relay.Function([var_6141], output)
mutated_mod['func_6143'] = func_6143
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6153 = relay.var("var_6153", dtype = "uint16", shape = ())#candidate|6153|()|var|uint16
const_6154 = relay.const([[[-3,-3,4,3,-8,3,3,-5,-9,-10,-7,-7,-2,9,2,-7]],[[4,3,-8,3,3,5,-6,-10,9,9,2,-2,3,-8,1,-10]],[[-5,-4,-9,-8,5,-10,-6,-7,2,-3,-1,9,-8,-9,-2,3]],[[-3,-10,-4,-5,-4,9,9,6,-1,4,-6,6,-1,3,3,3]],[[-5,-8,-3,-7,2,-6,-1,2,3,-3,-10,5,1,7,5,2]],[[2,8,-5,-2,-10,-9,3,10,7,5,2,9,7,1,-5,-4]],[[5,4,-5,-8,-7,6,8,5,1,3,1,7,7,2,1,8]],[[-7,7,-7,9,-1,5,10,5,10,-3,9,1,-7,5,-8,-3]]], dtype = "uint16")#candidate|6154|(8, 1, 16)|const|uint16
bop_6155 = relay.multiply(var_6153.astype('uint16'), const_6154.astype('uint16')) # shape=(8, 1, 16)
func_6140_call = mod.get_global_var('func_6140')
func_6143_call = mutated_mod.get_global_var('func_6143')
const_6160 = relay.const([-9,1,1,-3,7,2,2,-7,-2,-5,3,6,-1,2,-1,3,3,2,-1,5,-1,-7,3,-3,4,-3,-4,-3,-1,2,-7,-6,6,-4,-2,-4,-8,-7,-6,7,-2,9,1,-10,8,-8,6,7,9,10,2,8,6,2,8,4,-2,-6,6,9,10,10,9,-10,9,-4,6,5,-7,-6,8,5,-6,7,8,5,-1,-4,2,-1,-3,-4,-6,1,-5,8,-10,5,3,7,6,-7,-4,-9,4,9,-4,-6,-1,-2,5,-2,-1,10,-1,-5,-6,-5,-3,1,4,-5,-3,9,-8,-2,2,-8,3,7,3,-2,-4,3,3,5,4,-8,-10,10,-9,-1,-8,-4,-6,-6,4,-2,-5,8,-9,-5,-4,9,-9,4,-1,7,-5,-10,-3,-2,4,-5,-8,-7,7,-1,5,5,-7,2,-5,9,1,8,6,10,3,9,10,2,7,8,-1,4,3,10,-4,-7,8,10,7,-4,-7,4,8,-7,-9,-5,-10,-2,4,3,1,-6,5,-3,-5,-3,-9,-4,-6,1,7,-8,6,2,-4,-1,-4,1,10,2,-10,-10,3,-7,-4,-4,4,-8,4,2,6,2,-8,-1,-9,-6,7,10,-9,-1,-7,3,-1,-4,4,2,7,2,-8,-4,6,-8,5,7,8,8,-4,-7,-6,9,-4,2,6,-7,-6,3,-2,-7,2,-4,1,-4,-4,10,-1,-2,2,6,-7,-4,5,-7,10,-5,-9,1,-10,-6,5,6,7,-10,-9,8,-1,-3,10,5,-5,2,-9,3,-9,6,7,9,8,-4,6,-7,4,3,-9,6,1,5,1,1,-8,-6,-9,-8,6,7,4,9,3,4,2,-5,7,3,9,10,1,10,-10,-8,-2,8,-9,6,3,-4,-9,8,-9,4,6,-5,7,-10,6,3,5,6,10,-7,-1,8,10,-5,-10,8,10,-7,-9,-8,-5,4,4,-3,3,7,-1,-5,-2,1,-7,10,-10,-8,1,5,7,-7,3,-5,-10,-2,9,3,8,-3,-10,-4,-9,-1,-8,-10,10,-4,-7,-9,3,-9,9,-4,-3,1,2,-6,-8,3,7,-1,-1,10,-5,-7,10,-9,-8,-3,-9,-6,10,2,-3,5,8,-9,-10,9,7,2,-1,-6,5,10,6,5,-10,-5,3,4,-6,2,-9,-9,-4,8,5,4,5,-4,-2,10,-7,6,7,-3,1,8,4,-10,10,6,2,-5,-6,2,9,1,-9,8,-8,-8,6,-3,-3,1,-1,-1,6,3,-7,9,7,2,8,-1,-10,-7,4,7,3,3,4,8,-1,2,-6,-4,3,-8,-7,-9,-9,-3,6,-10,-7,-2,8,1,-1,-9,-5,9,-10,-1,9,6,-8,-8,-9,3,3,9,5,3,4,-2,-5,-9,9,4,1,5,8,-4,-4,-7,2,10,-5,-3,7,9,6,8,9,-5,-1,2,4,10,-4,-6,-10,-6,-1,5,-4,-9,2,8,-9,-4,1,-4,3,-2,-9,-5,-7,6,-10,6,-5,4,2,9,-5,6,10,-3,-3,1,-5,3,-7,-10,1,-1,-10,-4,-9,8,7,-3,3,9,5,8,-4,4,9,8,-9,-6,6,-3,-4,-10,-4,-5,1,1,-4,5,-9,1,2,-9,10,10,-7,2,6,10,7,5,1,-3,6,-5,9,-6,-7,4,10,5,8,9,-9,2,-6,5,6,4,-8,-10,7,9,-10,-1,-6,-10,-4,-8,9,9,10,5,-4,9,-8,-10,-4,-8,2,7,-8,4,-7,4,-6,-1,7,-4,5,-2,4,-9,-2,3,8,4,8,-7,4,-10,4,-7,-7,3,-6,-8,-10,-7,6,8,3,-4,-2,5,-2,-6,-6,1,-6,9,1,10,-4,4,10,-8,6,3,2,-3,3,-3,4,4,10,10,1,-5,-9,-7,-2,10,-6,5,-1,2,-2,4,-3,-6,2,-6,-9,7,1,5,-10,1,-9,4,9,-5,5,8,8,8,-3,-10,-5,-8,-3,-10,-1,-9,-1,2,10,-2,-7,-10,-6,2,3,10,10,-6,5,6,-1,6,-9,-4,6,-2,8,-5,-10,-6,10,5,-5,5,-9,4,7,1,-8,2,3,-6,-6,7,-9,-3,8,9,8,-3,-6,-4,1,-8,10,-5,-6,6,-2,-9,6,10,-9,7,-2,2,-1,10,2,1,7,-7,-6,4,3,-1,-7,-3,9,-2,4,10,10,7,5,6,-5,5,-5,3,4,9,6,-6,3,7,-1,5,6,-5,-2,-5,3,2,2,-8,-1,10,8,-2,5,10,-8,-9,-9,-7,5,-1,5,6,9,4,8,7,9,9,-1,-1,-6,-5,-5,7,6,6,-1,7,-6,-4,-6,-2,-2,-10,-4,4,-1,6,-1,4,2,7,4,-7,-8,7,-2,10,4,9,-10,9,-9,-7,-9,-6,-3,-6,8,1,4,9,-9,-10,-8,2,-1,9,-5,10,9,4,-10,3,4,3,2,-4,2,5,-4,-8,-7,4,-5,-5,-10,-10,-9,-8,5,-9,-7,9,8,7,-10,-6,2,-10,-4,-3,3,-5,-6,-5,8,9,10,5,1,-9,-9,-7,-7,-9,-1,-7,6,9,9,-3,2,4,-10,-10,-3,2,-8,-2,-6,-7,-5,-3,6,-5,10,4,1,-5,-5,2,6,9,-2,8,-5,-7,9,1,4,2,5,-7,2,-7,-7,-6,-2,-6,9,2,-10,2,9,-5,-1,-10,-3,-3,8,-5,-1,-7,-7,5,6,-9,8,-6,-9,1,-1,8,-7,10,-3,8,5,6,8,-7,-1,-3,-10,-6,-1,8,-10,-6,7,2,-1,3,6,8,-1,8,-3,-10,9,9,5,-2,4,-1,5,1,4,2,5,3,4,9,4,10,7,5,-9,-8,6,3,5,-7,-10,-8,-8,-1,6,-2,1,-6,-3,2,-10,6,4,-9,-3,-5,-5,6,-5,10,6,2,5,-8,8,2,-2,4,-8,-4,-9,-2,3,-10,6,2,1,3,-1,-6,-1,-7,-9,-1,-3,-5,-4,-7,-8,7,-6,-10,-4,-6,-2,-4,-3,7,3,6,-3,-6,-10,5,-1,-2,1,5,4,10,6,-8,6,-10,5,5,-8,6,6,-6,6,-4,-1,-2,-2,1,-10,-6,6,5,1,3,3,-7,-3,-3,-10,-5,6,6,-2,6,7,8,8,-9,5,8,1,4,6,-10,4,9,-3,-10,3,-6,-9,-6,-10,-6,4,3,-7,9,6,-2,-5,4,8,-2,1,-1,-6,5,-1,3,5,3,4,-5,-3,5,-8,5,-3,6,7,-4,6,9,2,-5,9,-9,1,-5,1,-10,9,6], dtype = "int64")#candidate|6160|(1260,)|const|int64
call_6159 = func_6140_call(relay.reshape(const_6160.astype('int64'), [14, 10, 9]))
call_6161 = func_6140_call(relay.reshape(const_6160.astype('int64'), [14, 10, 9]))
output = relay.Tuple([bop_6155,call_6159,const_6160,])
output2 = relay.Tuple([bop_6155,call_6161,const_6160,])
func_6163 = relay.Function([var_6153,], output)
mod['func_6163'] = func_6163
mod = relay.transform.InferType()(mod)
mutated_mod['func_6163'] = func_6163
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6164 = relay.var("var_6164", dtype = "uint16", shape = ())#candidate|6164|()|var|uint16
func_6163_call = mutated_mod.get_global_var('func_6163')
call_6165 = func_6163_call(var_6164)
output = call_6165
func_6166 = relay.Function([var_6164], output)
mutated_mod['func_6166'] = func_6166
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3272_call = mod.get_global_var('func_3272')
func_3274_call = mutated_mod.get_global_var('func_3274')
call_6171 = relay.TupleGetItem(func_3272_call(), 5)
call_6172 = relay.TupleGetItem(func_3274_call(), 5)
uop_6175 = relay.rsqrt(call_6171.astype('float32')) # shape=(165, 2)
uop_6177 = relay.rsqrt(call_6172.astype('float32')) # shape=(165, 2)
func_2301_call = mod.get_global_var('func_2301')
func_2303_call = mutated_mod.get_global_var('func_2303')
var_6181 = relay.var("var_6181", dtype = "uint32", shape = (90,))#candidate|6181|(90,)|var|uint32
call_6180 = relay.TupleGetItem(func_2301_call(relay.reshape(var_6181.astype('uint32'), [9, 5, 2])), 0)
call_6182 = relay.TupleGetItem(func_2303_call(relay.reshape(var_6181.astype('uint32'), [9, 5, 2])), 0)
var_6184 = relay.var("var_6184", dtype = "float32", shape = (165, 2))#candidate|6184|(165, 2)|var|float32
bop_6185 = relay.greater(uop_6175.astype('bool'), relay.reshape(var_6184.astype('bool'), relay.shape_of(uop_6175))) # shape=(165, 2)
bop_6188 = relay.greater(uop_6177.astype('bool'), relay.reshape(var_6184.astype('bool'), relay.shape_of(uop_6177))) # shape=(165, 2)
func_1239_call = mod.get_global_var('func_1239')
func_1241_call = mutated_mod.get_global_var('func_1241')
const_6190 = relay.const([4.010992,9.963400,-4.004870,7.206995,6.895853,-2.843650,-3.230402,8.429201,9.561360,-3.504322,8.844267,1.129149,4.590554,-3.711286,-3.160531,8.479459,1.342006,-7.647501,-6.287049,-5.461513,-9.911206,4.951963,2.585688,-0.877111,8.736066,-7.509214,0.063577,6.688969,6.929309,2.481598,5.807560,6.064957,1.300287,-8.508520,-6.240763,5.160490,6.171751,8.270043,4.051074,7.368243,-2.312043,7.850774,4.729652,-5.837013,6.621683,-4.211781,2.874229,3.548872,2.613065,-4.078302,-0.653214,2.202452,-4.281867,3.576464,-3.480236,-9.235153,-8.000479,-3.377746,-1.377212,-9.992124,-1.355762,1.321473,-3.189532,2.661868,-5.522965,1.248253,8.245341,7.210591,4.460851,-4.317281,1.805107,9.288951,-6.391879,-4.626219,-6.582707,-8.553146,5.965544,-0.428798,-2.972856,-7.396859,7.434152,-7.596260,-3.124353,-6.070217,-4.626207,5.780837,-3.573379,8.250702,-6.961215,9.445176,-3.924283,5.768154,8.129331,2.219195,0.993728,1.575101,-3.858887,-2.626048,6.428587,-0.537299,2.139643,2.962168,-5.363244,-3.277225,-1.504118,-2.456299,-5.376035,1.008320], dtype = "float64")#candidate|6190|(108,)|const|float64
call_6189 = relay.TupleGetItem(func_1239_call(relay.reshape(const_6190.astype('float64'), [9, 12, 1])), 0)
call_6191 = relay.TupleGetItem(func_1241_call(relay.reshape(const_6190.astype('float64'), [9, 12, 1])), 0)
uop_6193 = relay.acos(uop_6175.astype('float64')) # shape=(165, 2)
uop_6195 = relay.acos(uop_6177.astype('float64')) # shape=(165, 2)
output = relay.Tuple([call_6180,var_6181,bop_6185,call_6189,const_6190,uop_6193,])
output2 = relay.Tuple([call_6182,var_6181,bop_6188,call_6191,const_6190,uop_6195,])
func_6205 = relay.Function([var_6181,var_6184,], output)
mod['func_6205'] = func_6205
mod = relay.transform.InferType()(mod)
var_6206 = relay.var("var_6206", dtype = "uint32", shape = (90,))#candidate|6206|(90,)|var|uint32
var_6207 = relay.var("var_6207", dtype = "float32", shape = (165, 2))#candidate|6207|(165, 2)|var|float32
output = func_6205(var_6206,var_6207,)
func_6208 = relay.Function([var_6206,var_6207,], output)
mutated_mod['func_6208'] = func_6208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5852_call = mod.get_global_var('func_5852')
func_5853_call = mutated_mod.get_global_var('func_5853')
call_6212 = relay.TupleGetItem(func_5852_call(), 0)
call_6213 = relay.TupleGetItem(func_5853_call(), 0)
func_5694_call = mod.get_global_var('func_5694')
func_5696_call = mutated_mod.get_global_var('func_5696')
call_6221 = func_5694_call()
call_6222 = func_5694_call()
output = relay.Tuple([call_6212,call_6221,])
output2 = relay.Tuple([call_6213,call_6222,])
func_6232 = relay.Function([], output)
mod['func_6232'] = func_6232
mod = relay.transform.InferType()(mod)
output = func_6232()
func_6233 = relay.Function([], output)
mutated_mod['func_6233'] = func_6233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1596_call = mod.get_global_var('func_1596')
func_1597_call = mutated_mod.get_global_var('func_1597')
call_6254 = func_1596_call()
call_6255 = func_1596_call()
func_3468_call = mod.get_global_var('func_3468')
func_3471_call = mutated_mod.get_global_var('func_3471')
var_6266 = relay.var("var_6266", dtype = "float32", shape = (1, 140))#candidate|6266|(1, 140)|var|float32
call_6265 = relay.TupleGetItem(func_3468_call(relay.reshape(var_6266.astype('float32'), [2, 10, 7])), 2)
call_6267 = relay.TupleGetItem(func_3471_call(relay.reshape(var_6266.astype('float32'), [2, 10, 7])), 2)
output = relay.Tuple([call_6254,call_6265,var_6266,])
output2 = relay.Tuple([call_6255,call_6267,var_6266,])
func_6268 = relay.Function([var_6266,], output)
mod['func_6268'] = func_6268
mod = relay.transform.InferType()(mod)
mutated_mod['func_6268'] = func_6268
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6269 = relay.var("var_6269", dtype = "float32", shape = (1, 140))#candidate|6269|(1, 140)|var|float32
func_6268_call = mutated_mod.get_global_var('func_6268')
call_6270 = func_6268_call(var_6269)
output = call_6270
func_6271 = relay.Function([var_6269], output)
mutated_mod['func_6271'] = func_6271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5458_call = mod.get_global_var('func_5458')
func_5460_call = mutated_mod.get_global_var('func_5460')
call_6276 = relay.TupleGetItem(func_5458_call(), 1)
call_6277 = relay.TupleGetItem(func_5460_call(), 1)
func_5911_call = mod.get_global_var('func_5911')
func_5912_call = mutated_mod.get_global_var('func_5912')
call_6279 = relay.TupleGetItem(func_5911_call(), 1)
call_6280 = relay.TupleGetItem(func_5912_call(), 1)
output = relay.Tuple([call_6276,call_6279,])
output2 = relay.Tuple([call_6277,call_6280,])
func_6292 = relay.Function([], output)
mod['func_6292'] = func_6292
mod = relay.transform.InferType()(mod)
mutated_mod['func_6292'] = func_6292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6292_call = mutated_mod.get_global_var('func_6292')
call_6293 = func_6292_call()
output = call_6293
func_6294 = relay.Function([], output)
mutated_mod['func_6294'] = func_6294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5092_call = mod.get_global_var('func_5092')
func_5094_call = mutated_mod.get_global_var('func_5094')
call_6295 = relay.TupleGetItem(func_5092_call(), 0)
call_6296 = relay.TupleGetItem(func_5094_call(), 0)
output = relay.Tuple([call_6295,])
output2 = relay.Tuple([call_6296,])
func_6297 = relay.Function([], output)
mod['func_6297'] = func_6297
mod = relay.transform.InferType()(mod)
mutated_mod['func_6297'] = func_6297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6297_call = mutated_mod.get_global_var('func_6297')
call_6298 = func_6297_call()
output = call_6298
func_6299 = relay.Function([], output)
mutated_mod['func_6299'] = func_6299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5815_call = mod.get_global_var('func_5815')
func_5816_call = mutated_mod.get_global_var('func_5816')
call_6321 = relay.TupleGetItem(func_5815_call(), 0)
call_6322 = relay.TupleGetItem(func_5816_call(), 0)
const_6329 = relay.const([2,1,-10,-10,-9,-2,2,10,1,6,-10,-8,4,4,10,-7,-2,8,1,6,4,9,-7,-5,8,4,6,4,6,2,-6,10,7,7,-5,-10,-5,7,9,-10,3,2,6,9,-5,-9,10,-8,-7,-5,-10,-3,5,8,-2,-10,10,4,9,1,-6,5,-10,-1,8,1,-4,-4,6,2,10,-5,-5,8,2,-7,10,4,-5,-8,2,2,8,6,7,4,-1,8,5,9,-7,-8,8,-8,-7,-5,-8,7,-2,9,-1,7,-1,-8,-2,6,5,8,-5,8,5,-1,10,-10,-10,-4,-6,-5,-7,-3,-3,-10,-6,4,7,3,7,8,3,4,10,6,-8,-1,5,-7,7,-7,-8,-4,4,10,1,-1,-7,-8,2,1,5,8,-9,8,-2,9,-3,8,10,1,5,8,8,9,1,1,-3,8,3,10,-9,9,3,1,3,-7,-7,-10,-10,-4,-8,-9,-5,-7,-2,-6,-7,5,10,3,10,-4,4,2,3,-7,5,6,-4,8,9,7,9,-5,-9,-4,10,-8,2,-2,-7,7,-6,10,5,8,-2,-9,-6,-9,5,-6,1,-3,3,7,-6,-2,9,-4,1,-10,6,5,-6,-1,-10,-7,-10,-4,-6,2,7,-4,-5,-1,-2,-1,-2,2,-1,-10,9,-1,-10,9,6,-7,7,-9,2,9,1,-2,-6,-3,-7,-9,-10,3,-7,-5,-8,-8,-6,7,7,1,6,2,-10,-1,6,3,-2,6,-1,-2,3,-3,-7,6,8,3,-3,-8,-10,9,-8,-3,-9,10,2,-10,-6,-6,5,6,-1,7,-5,-6,3,10,8,-4,4,8,9,-3,-2,7,-10,1,3,-5,3,1,9,-7,-9,-3,-6,1,8,10,2,9,2,3,-8,-4,-2,-4,10,-5,4,-2,-8,8,8,9,-7,1,-8,5,-3,-6,-5,5,4,2,7,-8,8,4,-8,-5,-3,4,-1,7,1,-8,-4,10,2,-3,10,7,-1,-6,-3,-4,7,8,-9,3,-8,6,3,-9,-10,3,8,-9,-10,8,8,-2,9,5,8,-10,9,10,4,7,4,5,2,10,9,-7,-9,-3,10,-10,6,-5,-6,6,-4,5,5,-9,3,8,9,-10,4,-9,-1,-5,9,-3,6,-8,-2,-8,10,-3,9,7,-7,-6,-2,9,6,-2,5,3,-5,-2,1,-6,-9,5,2,-6,1,-2,-9,-8,-5,9,6,-1,-2,-1,-3,3,8,2,2,-1,-9,5,3,2,-4,8,-4,2,-10,-6,-2,6,9,-9,5,-1,2,4,-9,-3,-9,4,10,7,9,-6,4,-10,-10,-1,1,-1,10,-8,2,-4,4,4,4,-5,-5,-5,-3,-2,-5,9,-7,-9,-8,5,-8,-2,-7,-6,8,-5,2,-3,-6,-9,-8,-5,1,-1,10,-2,5,1,-10,4,-10,-4,8,9,-2,4,-9,4,-4,-2,1,3,7,9,-2,-9,1,-7,9,-4,4,-3,-9,-4,2,-7,7,-10,-3,4,-1,10,-4,-2,10,-6,-5,9,5,-7,9,-1,-4,-3,-9,2,9,3,-8,-8,4,5,2,3,7,-4,4,3,6,4,-2,-9,-10,-4,-9,7,4,-3,5,-4,8,1,3,9,-9,-7,1,1,10,10,-6,3,8,-8,1,-5,10,-10,-9,2,-4,-10,7,-8,5,-6,-4,4,-4,5,4,4,-8,-5,-3,-7,-10,-4,8,-5,2,7,2,-8,-4,2,6,10,-8,3,3,-8,8,-1,-6,1,-10,3,-10,6,5,1,-4,7,5,-3,9,5,-5,-6,-5,-8,5,-6,-4,8,2,5,10,8,-10,-8,-4,10,9,2,-3,8,-4,5,-9,-1,4,-5,-8,2,3,8,-2,9,-4,-7,1,-5,2,-7,4,-1,6,5,-8,1,-6,9,7,9,-8,10,-4,8,-6,-6,-5,-1,1,-2,-10,2,-3,-5,-8,-4,3,-8,9,-2,9,5,2,-4,1,-6,10,-8,9,-3,-10,-3,-1,9,-5,4,8,9,-5,-7,-8,7,8,-10,1,-6,-10,-1,10,-10,-2,2,-6,-1,5,-7,-10,-2,2,-7,-3,1,2,6,-3,-10,1,-4,-4,-7,-3,-1,-1,-3,-2,5,3,-1,-1,10,3,10,3,-10,10,-3,4,-8,-6,-9,3,-6,-3,3,3,-7,-5,-10,-10,3,-2,3,-2,-4,-3,-7,-8,-1,1,4,-9,-10,-5,-3,5,-4,-4,-4,9,-5,10,7,6,-8,3,-10,-2,-9,3,3,-7,4,6,-8,-5,-5,6,2,1,-8,1,-1,8,-9,1,8,8,9,-7,9,1,-6,8,-10,7,5,8,10,-3,7,-2,-2,-5,6,-2,-6,9,-2,10,-5,-2,7,-4,5,10,3,-9,4,-8,7,-5,2,9,-2,6,7,8,9,1,-1,-8,-2,-9,-10,-7,4,-4,-8,2,1,7,-7,10,-7,10,3,-10,2,3,6,-10,4,9,-4,-3,-1,3,-5,4,5,10,1,-4,1,6,9,-10,-10,6,1,1,10,-10,6,-9,-5,8,10,10,1,-9,-3,-3,7,7,1,-10,1,-9,3,5,-6,-5,-6,8,-10,-8,-5,6,-4], dtype = "int32")#candidate|6329|(990,)|const|int32
bop_6330 = relay.mod(call_6321.astype('float64'), relay.reshape(const_6329.astype('float64'), relay.shape_of(call_6321))) # shape=(990,)
bop_6333 = relay.mod(call_6322.astype('float64'), relay.reshape(const_6329.astype('float64'), relay.shape_of(call_6322))) # shape=(990,)
func_5228_call = mod.get_global_var('func_5228')
func_5229_call = mutated_mod.get_global_var('func_5229')
call_6347 = relay.TupleGetItem(func_5228_call(), 2)
call_6348 = relay.TupleGetItem(func_5229_call(), 2)
output = relay.Tuple([bop_6330,call_6347,])
output2 = relay.Tuple([bop_6333,call_6348,])
func_6361 = relay.Function([], output)
mod['func_6361'] = func_6361
mod = relay.transform.InferType()(mod)
output = func_6361()
func_6362 = relay.Function([], output)
mutated_mod['func_6362'] = func_6362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2166_call = mod.get_global_var('func_2166')
func_2167_call = mutated_mod.get_global_var('func_2167')
call_6397 = func_2166_call()
call_6398 = func_2166_call()
func_3538_call = mod.get_global_var('func_3538')
func_3540_call = mutated_mod.get_global_var('func_3540')
const_6404 = relay.const([-8.752971,2.985526,-9.154331,7.580397,6.558964,4.749893,-7.412519,-4.497049,-8.980961,1.813981,-0.561841,8.225123,-5.740543,9.403449,7.718641,0.466859,9.852055,-9.240964,-2.373600,1.151893,-6.807209,6.668672,3.568160,-7.139349,3.614180,-1.620850,-7.233784,-0.148997,6.919229,9.970171,-9.601484,-7.611193,5.514843,-0.852837,-3.228893,6.260345,-4.881521,2.781755,-4.758957,0.635383,6.433442,-8.090662,-6.503879,7.477572,-4.268890,-9.734978,1.896795,0.097548,-6.229358,0.727425,5.446581,0.772739,2.370358,-4.543242,-0.400787,4.185019,1.930809,8.997783,-8.613306,8.915357,3.885332,-6.580102,7.190493,9.260415,6.346432,-2.263176,8.379841,-3.270216,0.021584,4.560749,4.284899,9.899612,-8.353105,-9.114839,1.051402,1.582548,5.607676,-2.774655,8.270079,-8.597118,-7.473349,-7.233909,-5.891347,-7.440093,0.974589,0.961495,-9.113860,2.988162,-8.160137,-8.458443,-4.880792,-9.750209,1.830269,-7.902711,6.781949,8.971419,1.151335,2.553483,-4.615159,2.378609,8.397784,-6.934072,-4.182758,-0.443186,4.461274,-6.042339,2.561712,-2.118701], dtype = "float64")#candidate|6404|(108,)|const|float64
call_6403 = relay.TupleGetItem(func_3538_call(relay.reshape(const_6404.astype('float64'), [108,])), 1)
call_6405 = relay.TupleGetItem(func_3540_call(relay.reshape(const_6404.astype('float64'), [108,])), 1)
output = relay.Tuple([call_6397,call_6403,const_6404,])
output2 = relay.Tuple([call_6398,call_6405,const_6404,])
func_6430 = relay.Function([], output)
mod['func_6430'] = func_6430
mod = relay.transform.InferType()(mod)
output = func_6430()
func_6431 = relay.Function([], output)
mutated_mod['func_6431'] = func_6431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3690_call = mod.get_global_var('func_3690')
func_3692_call = mutated_mod.get_global_var('func_3692')
call_6432 = relay.TupleGetItem(func_3690_call(), 3)
call_6433 = relay.TupleGetItem(func_3692_call(), 3)
func_1005_call = mod.get_global_var('func_1005')
func_1007_call = mutated_mod.get_global_var('func_1007')
var_6435 = relay.var("var_6435", dtype = "uint32", shape = ())#candidate|6435|()|var|uint32
call_6434 = relay.TupleGetItem(func_1005_call(relay.reshape(var_6435.astype('uint32'), [])), 1)
call_6436 = relay.TupleGetItem(func_1007_call(relay.reshape(var_6435.astype('uint32'), [])), 1)
func_2150_call = mod.get_global_var('func_2150')
func_2152_call = mutated_mod.get_global_var('func_2152')
var_6446 = relay.var("var_6446", dtype = "uint8", shape = (2145,))#candidate|6446|(2145,)|var|uint8
call_6445 = relay.TupleGetItem(func_2150_call(relay.reshape(var_6446.astype('uint8'), [2145,])), 1)
call_6447 = relay.TupleGetItem(func_2152_call(relay.reshape(var_6446.astype('uint8'), [2145,])), 1)
output = relay.Tuple([call_6432,call_6434,var_6435,call_6445,var_6446,])
output2 = relay.Tuple([call_6433,call_6436,var_6435,call_6447,var_6446,])
func_6450 = relay.Function([var_6435,var_6446,], output)
mod['func_6450'] = func_6450
mod = relay.transform.InferType()(mod)
mutated_mod['func_6450'] = func_6450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6450_call = mutated_mod.get_global_var('func_6450')
var_6452 = relay.var("var_6452", dtype = "uint32", shape = ())#candidate|6452|()|var|uint32
var_6453 = relay.var("var_6453", dtype = "uint8", shape = (2145,))#candidate|6453|(2145,)|var|uint8
call_6451 = func_6450_call(var_6452,var_6453,)
output = call_6451
func_6454 = relay.Function([var_6452,var_6453,], output)
mutated_mod['func_6454'] = func_6454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6017_call = mod.get_global_var('func_6017')
func_6018_call = mutated_mod.get_global_var('func_6018')
call_6492 = relay.TupleGetItem(func_6017_call(), 1)
call_6493 = relay.TupleGetItem(func_6018_call(), 1)
const_6494 = relay.const([[[5.050384,-8.288099,3.461333,-6.202525,-1.356493,-8.294149,-1.043644,5.961558,-5.773417,6.651094],[8.720947,0.917756,8.276101,-0.352777,-0.845983,-1.473560,6.111529,8.090705,3.931701,-7.533864],[5.455703,9.043991,-8.592048,2.304543,-7.910834,7.903956,-0.930946,9.144125,-6.167080,-9.889582]],[[-4.942814,-4.285858,2.249971,-2.248212,2.413882,0.370409,-4.908186,-0.021317,9.838787,3.690407],[-6.054294,1.013382,9.622194,-5.192757,2.890373,-7.512255,4.808289,7.403817,6.063025,5.308854],[-2.609664,7.537084,-0.113462,3.772307,0.018060,4.164192,8.207798,-5.555700,-3.184362,-1.335414]],[[1.875543,1.662110,0.960718,-4.741365,-9.146363,-3.062303,-9.141103,4.727629,7.632434,-9.387476],[-8.652421,4.576834,-3.845294,-1.357750,-1.943617,-8.475887,-5.748132,0.539016,8.799809,-7.688100],[0.024554,-0.264548,-3.748548,-3.838638,4.671846,2.647910,2.330813,1.097397,-6.093953,-9.213383]],[[4.280248,1.532931,-0.189910,0.901943,-6.546392,7.247437,-8.808176,6.130416,-7.947192,6.387515],[-6.882946,8.581476,3.076974,6.106719,-7.551207,-3.057392,9.609767,8.041093,-6.560060,3.092697],[-9.954775,2.847339,-6.591184,-2.088372,-7.771823,-2.269222,-9.004746,-3.058280,6.273240,1.427314]],[[3.851410,6.931822,9.696872,-2.294876,8.530117,-8.899442,0.707279,6.389827,-4.450570,-2.324276],[6.858242,7.411980,-1.506708,3.065113,-5.635773,3.858286,-8.360996,-4.734542,-2.073190,-1.807455],[-1.830717,8.446672,-9.825105,2.426150,-8.475253,9.833649,0.062205,0.238686,0.077484,6.578149]],[[-2.413863,2.294088,4.159288,-2.148302,2.505909,1.764506,-5.795653,1.463797,2.408032,1.861355],[-3.352396,9.758558,-1.646145,8.073817,9.191386,6.544914,4.071456,4.701401,-7.793234,-1.353884],[-4.275507,6.403453,2.526316,3.435545,1.437505,-7.628522,8.541670,5.168086,4.063863,2.318628]],[[1.755860,-8.595725,-2.182281,4.174514,9.298682,-4.943112,-5.533921,-5.307387,-6.493954,-2.316277],[2.117132,7.508267,2.917485,-9.530092,9.379640,6.329330,-4.045478,2.401727,6.227180,0.317397],[9.902297,-3.673140,0.791532,8.235797,-4.575038,1.961431,-9.812383,5.339069,-8.978299,-4.328973]],[[9.084987,-0.030094,1.871864,-6.673086,3.998991,-4.948945,4.087880,-3.631153,1.099098,-2.690170],[1.636838,0.668573,-0.726563,6.090513,-0.021626,-9.291070,-9.922203,5.716098,7.166455,-0.109948],[2.256430,9.002624,-3.173874,2.666449,9.741899,6.601195,-4.714877,-4.259647,7.410073,6.069286]]], dtype = "float32")#candidate|6494|(8, 3, 10)|const|float32
bop_6495 = relay.greater(call_6492.astype('bool'), relay.reshape(const_6494.astype('bool'), relay.shape_of(call_6492))) # shape=(8, 3, 10)
bop_6498 = relay.greater(call_6493.astype('bool'), relay.reshape(const_6494.astype('bool'), relay.shape_of(call_6493))) # shape=(8, 3, 10)
output = relay.Tuple([bop_6495,])
output2 = relay.Tuple([bop_6498,])
func_6499 = relay.Function([], output)
mod['func_6499'] = func_6499
mod = relay.transform.InferType()(mod)
output = func_6499()
func_6500 = relay.Function([], output)
mutated_mod['func_6500'] = func_6500
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6505 = relay.var("var_6505", dtype = "float64", shape = (6, 8, 1))#candidate|6505|(6, 8, 1)|var|float64
uop_6506 = relay.atanh(var_6505.astype('float64')) # shape=(6, 8, 1)
func_2909_call = mod.get_global_var('func_2909')
func_2912_call = mutated_mod.get_global_var('func_2912')
const_6510 = relay.const([-5,-6,8,1,-8,2,-3,-4,5,4,-7,-6,-4,-3,3,9,-4,-4,-9,-10,5,-10,6,3,-9,3,-1,6,3,4,-9,5,8,-6,6,3,-10,10,-8,7,2,-5,9,8,3,10,-5,-5,-4,-9,7,-4,8,4,8,3,-3,1,-2,-6,1,6,10,-8,-10,-7,-2,5,4,3,-5,2,-7,-4,3,5,-5,-9,-10,-1,5,-1,-8,6,8,-4,8,-2,10,-5,5,7,10,-7,3,5,8,7,-2,6,4,6,-5,-10,-2,7,6,-9,10,-9,6,4,-9,9,-4,5,6,-2,10,5,-9,-1,-6,1,8,2,-3,-9,-7,-8,-5,1,-4,2,6,-6,-2,8,-7,6,9,1,-4,6,1,2,-7,-7,7,3,-9,-6,5,-8,3,10,-4,5,1,9,5,8,-4,5,4,-5,-8,-3,7,5,-7,-3,6,-1,9,-1,-3,8,-3,1,10,2,6,-1,7,2,-3,-7,1,7,7,-6,-8,10,-9,1,-4,9,6,-3,-8,-9,10,-1,1,2,-8,10,5,5,8,5,-9,-4,-4,10,-1,-4,-2,-3,5,-4,-6,-6,4,-6,9,6,6,5,-6,4,3,-10,5,1,-1,-2,9,9,-1,-6,6,10,-10,2,1,5,7,10,-1,3,-6,-10,-3,8,3,6,-4,1,-1,-1,-10,6,-4,-1,-9,-8,9,10,8,-8,2,10,8,3,6,-2,2,6,-4,4,9,-8,1,-10,6,10,2,7,3,9,-5,6,7,-5,6,4,-3,-6,10,3,-6,7,5,5,-3,-5,-5,6,-10,-5,-10,4,1,8,-7,-9,-6,-8,10,8,2,-10,6,-1,6,-5,-6,2,8,-1,4,8,8,-10,-3,-2,4,2,-9,-6,-10,5,-9,-5,8,-4,10,2,-1,-8,3,-9,-3,6,-5,-9,5,-3,1,-3,-4,3,10,1,8,-6,-9,-9,-8,-6,-9,-10,-1,9,10,2,1,-9,-1,-2,2,-1,3,-5,6,5,-8,-2,-7,10,-4,-3,-10,-8,3,-9,8,-7,-1,-5,6,4,7,5,-8,-3,-9,-9,-9,9,7,-8,-9,9,7,-9,-3,9,9,-4,-8,1,-5,4,7,5,-3,-10,-8,-2,-10,10,-4,-5,-10,1,-8,-3,1,7,3,2,7,-8,-9,-1,-1,-6,7,-9,-10,3,3,3,5,3,-1,6,7,2,4,8,-2,2,4,6,-2,-6,-5,10,-8,-10,8,-7,-9,2,4,-9,-2,8,2,4,3,8,10,1,-1,-6,-6,3,-6,1,4,-8,10,-4,10,-6,-9,-2,-2,-6,-4,3,7,-9,2,-3,-7,3,-7,-10,9,1,-10,-9,-7,-9,-7,-3,8,-7,2,-5,3,8,8,-8,-6,7,3,2,10,3,2,2,-9,-8,-1,2,4,-3,-8,1,9,1,3,1,3,-9,-9,-4,-1,9,-9,5,1,-8,-8,-4,-7,8,10,-1,3,-9,4,3,8,-9,-5,2,4,-6,9,1,8,-7,-1,1,-10,-8,-4,2,-7,8,-5,9,-2,-4,-6,8,4,-10,4,9,-2,10,2,-5,-3,2,-5,9,-7,-10,-10,6,-4,1,10,3,8,7,7,10,8,10,-2,-1,-4,1,9,-9,8,2,9,1,3,7,1,-10,9,2,-10,10,6,-7,-3,-10,6,10,-9,3,2,-2,7,-1,3,-10,8,7,3,1,-2,-8,2,6,-10,3,-10,4,8,-6,1,-4,-5,-5,4,-6,-6,7,-2,-1,-3,-6,-1,2,8,-10,3,-1,4,-9,-3,-7,7,9,8,-4,4,3,2,5,-5,-10,9,-7,5,-3,10,7,5,-9,-6,3,-4,-7,4,-4,-9,7,4,-10,1,9,-5,-1,4,1,-2,2,-5,-10,-3,9,-1,-9,-4,7,-4,7,5,-8,-7,-1,-7,6,-3,10,3,9,8,10,-9,-7,3,2,3,7,3,10,-10,-2,3,1,3,-1,-8,-3,9,-9,6,-2,-5,9,-8,10,5,3,3,-5,5,-9,10,9,-2,4,2,-6,-7,-7,-6,-5,8,-9,5,9,-2,1,10,1,-10,9,3,1,8,8,-6,5,2,-4,9,-5,2,5,9,4,-5,3,6,-9,-3,-10,-2,2,-2,9,2,4,-3,7,-9,1,-4,1,8,8,-8,10,-7,2,-1,-1,-8,-6,-8,-2,6,8,-8,1,10,7,2,-8,4,-6,-4,5,-4,4,5,-6,1,-2,4,5,5,-5,-3,-3,6,9,8,3,-8,1,-5,6,-2,5,4,-3,-1,-5,1,1,-1,7,-6,-9,-7,10,7,8,-4,7,-2,-8,-9,9,-3,7,-3,-3,-7,5,-5,8,1,-3,-10,5,-1,6,6,-9,-6,-4,5,9,-10,-5,-9,8,10,7,2,-9,4,4,-1,-2,-1,7,4,7,-10,10,5,7,9,-5,-7,3,-10,-3,10,-9,4,9,3,5,-6,1,2,9,6,-2,8,4,4,10,-5,-7,6,8,-9,3,7,-9,5,-2,-9,2,4,5,5,10,-4,-10,2,-10,-2,-6,-6,-2,2,10,10,9,9,-2,9,6,-8,4,6,-10,-4,9,-1,10,5,-5,1,-1,-7,-5,-4,10,9,3,-7,-4,-9,-10,4,-6,-8,-5,6,-1,8,9,-9,5,2,-1,-9,9,-10,2,9,-4,-10,7,-5,-9,6,-7,7,-3,8,-10,-1,-8,-8,-6,10,-3,8,-6,-10,-10,-5,3,6,2,10,-4,-3,-5,-3,-7,10,3,1,3,-6,-2,-9,-4,-1,-1,-2,-5,7,5,10,3,3,-9,7,8,6,-6,-4,-10,-1,-5,7,-6,-9,-4,-3,8,5,2,9,7,9,8,8,-8,2,1,-5,-6,10,-1,9,10,-5,5,-10,9,8,5,-9,4,-8,3,-2,8,-8,-4,8,-8,4,-9,6,8,-7,-9,-7,8,-9,-1,-7,-2,7,2,2,2,-3,-2,1,4,-4,4,7,-7,2,-7,6,-4,5,-10,-5,-5,-3,9,9,-2,6,2,-10,10,-8,1,-4,7,-2,-8,-9,-7,-2,-6,10,3,8,9,-6,-7,4,6,-4,9,10,-5,2,1,10,4,7,-6,-3,-2,2,3,9,5,-4,3,6,5,2,2,3,-2,3,7,2,7,1,1,-1,5,-3,-3,6,6,2,-2,4,-9,-1,-5,6,-9,3,-6,6,-4,-10,7,3,-4,1,-3,-9,4,-9,-2,-2,-1,-1,-1,-10,8,-10,-6,8,1,5,6,4,-3,-10,7,8,-9,9,-9,-5,-9,-4,9,4,-5,1,4,-1,8,3,-5,7,3,-2,-5,1,-1,10,1,9,4,5,-7,6,-10,-5,4,-7,-8,-1,-5,10,9,7,5,-4,-7,-8,7,-2,-4,2,-8,5,7,2,6,9,1,5,-1,4,8,-4,5,2,2,-5,2,-8,-4,2,-10,7,-6,-7,1,-6,-3,-6,6,-8,-1,-7,-3,-1,-5,10,3,-7,2,-7,-7,-4,5,9,-5,8,-1,10,-1,-4,-3,2,-4,6,-4,10,9,-2,-1,4,9,5,-10,-6,5,7,-4,5,-7,5,5,-3,-9,-9,-5,8,6,3,-8,6,7,-1,-2,1,7,-3,1,-9,2,-1,-2,10,-4,-5,-2,-4,-6,-1,1,-10,-8,-5,10,7,3,-6,9,-2,-10,5,-7,2,6,-2,5,-9,4,2,-9,3,-9,6,6,8,4,10,2,5,-5,-7,6,5,-10,-3,8,-1,-8,2,3,-1,-5,8,-1,7,7,-6,10,6,-8,6,-6,10,2,-7,-6,-3,9,10,4,8,1,-6,-5,10,-1,1,3,-1,-5,-3,-7,4,8,8,1,-5,9,-5,4,-10,-4,-4,2,4,-6,-10,5,-10,6,-7,3,-1,-5,-7,-2,6,7,2,7,-9,-7,5,1,-7,5,-5,-5,-1,5,-9,-4,-4,7,2,-4,-5,8,-2,-7,-7], dtype = "int32")#candidate|6510|(1521,)|const|int32
call_6509 = relay.TupleGetItem(func_2909_call(relay.reshape(const_6510.astype('int32'), [9, 13, 13])), 5)
call_6511 = relay.TupleGetItem(func_2912_call(relay.reshape(const_6510.astype('int32'), [9, 13, 13])), 5)
bop_6513 = relay.multiply(uop_6506.astype('int8'), relay.reshape(var_6505.astype('int8'), relay.shape_of(uop_6506))) # shape=(6, 8, 1)
uop_6520 = relay.acos(bop_6513.astype('float32')) # shape=(6, 8, 1)
bop_6522 = relay.logical_or(bop_6513.astype('bool'), relay.reshape(uop_6520.astype('bool'), relay.shape_of(bop_6513))) # shape=(6, 8, 1)
bop_6526 = relay.not_equal(bop_6513.astype('bool'), call_6509.astype('bool')) # shape=(6, 8, 840)
bop_6529 = relay.not_equal(bop_6513.astype('bool'), call_6511.astype('bool')) # shape=(6, 8, 840)
bop_6539 = relay.less_equal(uop_6520.astype('bool'), relay.reshape(bop_6522.astype('bool'), relay.shape_of(uop_6520))) # shape=(6, 8, 1)
func_3468_call = mod.get_global_var('func_3468')
func_3471_call = mutated_mod.get_global_var('func_3471')
const_6557 = relay.const([-7.595573,4.434061,1.959945,-1.497352,-9.782265,1.884911,-1.460193,9.881579,4.079817,2.950421,9.181667,1.075222,-4.037050,2.066738,3.122301,-9.911411,0.227003,5.692185,-1.301174,7.600375,7.627584,1.503166,5.451337,0.963763,7.386592,-7.779232,9.843268,-0.492865,2.115395,0.587472,3.575887,-5.052674,4.877994,1.717073,1.461754,-5.574127,-2.999967,9.721107,0.948152,-7.257364,0.068938,9.278729,-4.404492,-7.320551,9.173219,-9.358134,3.096344,7.256157,-3.312574,7.857428,-2.298137,-0.829381,3.887314,-7.673798,-5.893903,1.437724,-5.646632,-1.645383,-6.672943,-9.029883,2.897562,-6.664542,2.718182,0.871799,-1.833985,7.563565,8.043923,8.823000,6.928008,7.716680,-1.962554,7.867090,6.347386,6.618430,-6.611446,2.346320,4.621626,3.069665,7.152717,-2.220007,4.498816,-2.232981,-8.103709,4.509108,-4.083153,0.115551,8.232921,4.808099,3.218569,-4.946484,-5.043606,4.482252,5.192589,-1.734113,1.664125,-6.082934,-8.344978,3.663887,1.283106,7.867851,9.750592,-1.171281,9.791861,2.761413,5.070490,1.859306,0.662734,4.390013,1.976589,-4.212621,-9.632504,6.638254,0.446753,7.518107,8.088192,-7.945432,-0.885112,8.927187,-7.062249,-0.795391,-9.563705,8.994980,-2.205834,-1.431474,-6.144397,-1.273290,8.098597,-2.031371,5.999774,4.952306,-1.903913,5.769052,6.861370,-1.848171,-2.988553,1.695700,-4.324971,-3.361147,4.271565,-1.797971], dtype = "float32")#candidate|6557|(140,)|const|float32
call_6556 = relay.TupleGetItem(func_3468_call(relay.reshape(const_6557.astype('float32'), [2, 10, 7])), 3)
call_6558 = relay.TupleGetItem(func_3471_call(relay.reshape(const_6557.astype('float32'), [2, 10, 7])), 3)
func_6163_call = mod.get_global_var('func_6163')
func_6166_call = mutated_mod.get_global_var('func_6166')
const_6563 = relay.const(10, dtype = "uint16")#candidate|6563|()|const|uint16
call_6562 = relay.TupleGetItem(func_6163_call(relay.reshape(const_6563.astype('uint16'), [])), 1)
call_6564 = relay.TupleGetItem(func_6166_call(relay.reshape(const_6563.astype('uint16'), [])), 1)
func_3863_call = mod.get_global_var('func_3863')
func_3864_call = mutated_mod.get_global_var('func_3864')
call_6569 = relay.TupleGetItem(func_3863_call(), 0)
call_6570 = relay.TupleGetItem(func_3864_call(), 0)
output = relay.Tuple([const_6510,bop_6526,bop_6539,call_6556,const_6557,call_6562,const_6563,call_6569,])
output2 = relay.Tuple([const_6510,bop_6529,bop_6539,call_6558,const_6557,call_6564,const_6563,call_6570,])
func_6571 = relay.Function([var_6505,], output)
mod['func_6571'] = func_6571
mod = relay.transform.InferType()(mod)
mutated_mod['func_6571'] = func_6571
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6572 = relay.var("var_6572", dtype = "float64", shape = (6, 8, 1))#candidate|6572|(6, 8, 1)|var|float64
func_6571_call = mutated_mod.get_global_var('func_6571')
call_6573 = func_6571_call(var_6572)
output = call_6573
func_6574 = relay.Function([var_6572], output)
mutated_mod['func_6574'] = func_6574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6017_call = mod.get_global_var('func_6017')
func_6018_call = mutated_mod.get_global_var('func_6018')
call_6613 = relay.TupleGetItem(func_6017_call(), 1)
call_6614 = relay.TupleGetItem(func_6018_call(), 1)
output = call_6613
output2 = call_6614
func_6650 = relay.Function([], output)
mod['func_6650'] = func_6650
mod = relay.transform.InferType()(mod)
output = func_6650()
func_6651 = relay.Function([], output)
mutated_mod['func_6651'] = func_6651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4214_call = mod.get_global_var('func_4214')
func_4215_call = mutated_mod.get_global_var('func_4215')
call_6652 = relay.TupleGetItem(func_4214_call(), 0)
call_6653 = relay.TupleGetItem(func_4215_call(), 0)
func_4155_call = mod.get_global_var('func_4155')
func_4157_call = mutated_mod.get_global_var('func_4157')
const_6676 = relay.const([False,True,False,True,False,False,True,False,False,True,False,True,False,True,False,False,True,True,False,False,True,True,False,True,False,True,False,False,False,False,True,True,True,True,False,True,False,False,False,False,True,False,True,True,True,True,True,True,True,False,True,False,True,True,True,False,False,True,False,True,True,False,False,True,True,False,False,True,False,False,True,False,False,False,True,False,False,True,True,True,True,False,True,False,True,False,False,True,False,True,False,True,True,False,False,False,True,True,False,True,True,True,True,False,False,True,False,False,False,True,True,True,True,False,True,False,False,False,True,False,True,False,False,False,False,False,False,True,True,False,True,True,False,False,True,False,True,True,False,True,False,True,False,True,True,False,True,True,False,False,False,True,False,False,True,True,False,True,False,False,False,True,True,False,False,False,False,True,True,False,True,True,True,True,False,False,True,True,True,True,True,True,False,False,True,True,True,False,True,True,False,True,True,True,True,True,True,True,False,False,True,True,True,False,True,True,False,False,False,True,False,True,True,False,True,False,False,False,False,True,False,False,False,True,True,True,False,False,False,False,False,True,False,True,True,True,False,True,True,False,False,True,False,True,False,True,False,False,False,False,True,False,True,True,True,False,False,True,True,False,True,True,True,True,True,False,False,True,True,False,False,True,True,False,True,True,True,True,True,True,True,False,True,False,True,False,True,True,True,False,True,True,True,False,False,False,False,True,False,True,True,False,True,False,False,False,False,True,True,True,True,False,False,False,True,True,True,False,True,False,False,False,True,True,True,False,False,True,True,False,True,False,False,False,False,False,False,False,True,True,False,False,True,False,True,False,True,False,False,False,False,False,True,False,False,False,False,False,True,True,False,False,True,False,False,True,False,False,False,True,True,False,False,True,False,True,True,True,True,False,False,True,False,True,True,False,True,True,False,False,False,False,True,True,False,True,True,False,False,True,False,True,True,False,False,True,True,False,False,False,False,False,True,False,True,True,True,False,False,True,True,True,False,False,False,False,True,True,True,True,False,True,True,True,True,True,False,False,True,True,False,True,True,True,False,True,False,True,True,True,False,False,False,False,False,False,True,False,False,False,True,False,True,False,False,False,False,False,False,True,True,False,True,True,True,True,False,False,False,True,True,False,False,True,True,False,True,False,False,True,False,False,False,True,False,False,True,False,False,True,False,False,True,True,True,False,False,True,False,False,False,True,False,False,False,True,True,False,True,True,True,True,True,True,False,False,True,True,False,False,False,False,False,True,True,True,False,True,False,False,True,False,False,False,True,False,True,False,False,True,True,False,False,True,True,True,True,True,False,True,True,True,False,True,False,True,False,False,True,False,True,False,False,True,False,True,True,False,True,False,True,True,False,True,False,True,False,True,False,True,False,True,False,False,False,False,False,False,True,True,False,False,True,True,True,False,False,False,False,False,False,True,True,False,False,True,False,True,False,False,False,False,False,False,True,False,False,True,True,True,False,True,True,True,False,False,True,True,True,True,True,True,False,False,False,True,True,False,False,True,False,False,True,False,False,False,True,False,True,False,False,True,True,True,True,False,False,False,True,True,False,False,False,False,False,False,True,True,False,True,False,True,True,True,True,True,False,False,False,True,False,False,True,False,True,False,False,True,False,True,False,False,True,True,True,True,True,False,False,False,False,False,True,True,True,False,True,True,True,True,True,True,True,False,True,False,False,True,False,False,False,False,True,True,True,False,False,True,False,False,True,False,False,False,False,False,False,True,True,True,False,False,True,True,False,False,True,False,False,True,True,False,False,False,False,True,False,False,False,False,True,True,True,True,True,True,True,False,False,True,True,False,True,False,True,False,True,False,False,True,False,True,True,False,True,True,True,True,False,False,False,True,True,True,False,True,False,False,True,False,True,False,False,False,True,True,False,False,True,True,True,True,False,False,True,False,False,True,True,False,True,True,True,False,False,True,True,False,True,False], dtype = "bool")#candidate|6676|(840,)|const|bool
call_6675 = relay.TupleGetItem(func_4155_call(relay.reshape(const_6676.astype('bool'), [840, 1])), 0)
call_6677 = relay.TupleGetItem(func_4157_call(relay.reshape(const_6676.astype('bool'), [840, 1])), 0)
output = relay.Tuple([call_6652,call_6675,const_6676,])
output2 = relay.Tuple([call_6653,call_6677,const_6676,])
func_6678 = relay.Function([], output)
mod['func_6678'] = func_6678
mod = relay.transform.InferType()(mod)
mutated_mod['func_6678'] = func_6678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6678_call = mutated_mod.get_global_var('func_6678')
call_6679 = func_6678_call()
output = call_6679
func_6680 = relay.Function([], output)
mutated_mod['func_6680'] = func_6680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6292_call = mod.get_global_var('func_6292')
func_6294_call = mutated_mod.get_global_var('func_6294')
call_6738 = relay.TupleGetItem(func_6292_call(), 0)
call_6739 = relay.TupleGetItem(func_6294_call(), 0)
func_5664_call = mod.get_global_var('func_5664')
func_5666_call = mutated_mod.get_global_var('func_5666')
call_6747 = relay.TupleGetItem(func_5664_call(), 0)
call_6748 = relay.TupleGetItem(func_5666_call(), 0)
func_4882_call = mod.get_global_var('func_4882')
func_4884_call = mutated_mod.get_global_var('func_4884')
call_6751 = relay.TupleGetItem(func_4882_call(), 0)
call_6752 = relay.TupleGetItem(func_4884_call(), 0)
output = relay.Tuple([call_6738,call_6747,call_6751,])
output2 = relay.Tuple([call_6739,call_6748,call_6752,])
func_6758 = relay.Function([], output)
mod['func_6758'] = func_6758
mod = relay.transform.InferType()(mod)
output = func_6758()
func_6759 = relay.Function([], output)
mutated_mod['func_6759'] = func_6759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4255_call = mod.get_global_var('func_4255')
func_4256_call = mutated_mod.get_global_var('func_4256')
call_6760 = relay.TupleGetItem(func_4255_call(), 1)
call_6761 = relay.TupleGetItem(func_4256_call(), 1)
output = relay.Tuple([call_6760,])
output2 = relay.Tuple([call_6761,])
func_6768 = relay.Function([], output)
mod['func_6768'] = func_6768
mod = relay.transform.InferType()(mod)
mutated_mod['func_6768'] = func_6768
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6768_call = mutated_mod.get_global_var('func_6768')
call_6769 = func_6768_call()
output = call_6769
func_6770 = relay.Function([], output)
mutated_mod['func_6770'] = func_6770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6650_call = mod.get_global_var('func_6650')
func_6651_call = mutated_mod.get_global_var('func_6651')
call_6800 = func_6650_call()
call_6801 = func_6650_call()
func_2663_call = mod.get_global_var('func_2663')
func_2664_call = mutated_mod.get_global_var('func_2664')
call_6802 = relay.TupleGetItem(func_2663_call(), 1)
call_6803 = relay.TupleGetItem(func_2664_call(), 1)
func_2301_call = mod.get_global_var('func_2301')
func_2303_call = mutated_mod.get_global_var('func_2303')
const_6817 = relay.const([8,-2,3,-4,-6,-5,-5,7,8,3,9,7,6,3,4,1,-5,6,5,-5,3,4,-8,9,10,-7,-1,8,-4,3,8,-9,-6,-10,-7,4,4,-9,10,2,2,-8,6,10,-8,7,8,-8,4,-7,-5,-2,-10,3,9,-1,-5,-3,8,2,-8,-1,-6,1,9,3,-9,-4,4,-3,3,5,5,-2,3,9,4,8,-1,1,6,-5,-7,-8,-6,-7,2,-8,1,-10], dtype = "uint32")#candidate|6817|(90,)|const|uint32
call_6816 = relay.TupleGetItem(func_2301_call(relay.reshape(const_6817.astype('uint32'), [9, 5, 2])), 0)
call_6818 = relay.TupleGetItem(func_2303_call(relay.reshape(const_6817.astype('uint32'), [9, 5, 2])), 0)
func_4882_call = mod.get_global_var('func_4882')
func_4884_call = mutated_mod.get_global_var('func_4884')
call_6820 = relay.TupleGetItem(func_4882_call(), 1)
call_6821 = relay.TupleGetItem(func_4884_call(), 1)
output = relay.Tuple([call_6800,call_6802,call_6816,const_6817,call_6820,])
output2 = relay.Tuple([call_6801,call_6803,call_6818,const_6817,call_6821,])
func_6822 = relay.Function([], output)
mod['func_6822'] = func_6822
mod = relay.transform.InferType()(mod)
output = func_6822()
func_6823 = relay.Function([], output)
mutated_mod['func_6823'] = func_6823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4814_call = mod.get_global_var('func_4814')
func_4815_call = mutated_mod.get_global_var('func_4815')
call_6835 = relay.TupleGetItem(func_4814_call(), 1)
call_6836 = relay.TupleGetItem(func_4815_call(), 1)
func_4882_call = mod.get_global_var('func_4882')
func_4884_call = mutated_mod.get_global_var('func_4884')
call_6843 = relay.TupleGetItem(func_4882_call(), 1)
call_6844 = relay.TupleGetItem(func_4884_call(), 1)
output = relay.Tuple([call_6835,call_6843,])
output2 = relay.Tuple([call_6836,call_6844,])
func_6845 = relay.Function([], output)
mod['func_6845'] = func_6845
mod = relay.transform.InferType()(mod)
output = func_6845()
func_6846 = relay.Function([], output)
mutated_mod['func_6846'] = func_6846
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6768_call = mod.get_global_var('func_6768')
func_6770_call = mutated_mod.get_global_var('func_6770')
call_6855 = relay.TupleGetItem(func_6768_call(), 0)
call_6856 = relay.TupleGetItem(func_6770_call(), 0)
output = relay.Tuple([call_6855,])
output2 = relay.Tuple([call_6856,])
func_6857 = relay.Function([], output)
mod['func_6857'] = func_6857
mod = relay.transform.InferType()(mod)
output = func_6857()
func_6858 = relay.Function([], output)
mutated_mod['func_6858'] = func_6858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5135_call = mod.get_global_var('func_5135')
func_5137_call = mutated_mod.get_global_var('func_5137')
call_6872 = relay.TupleGetItem(func_5135_call(), 0)
call_6873 = relay.TupleGetItem(func_5137_call(), 0)
output = relay.Tuple([call_6872,])
output2 = relay.Tuple([call_6873,])
func_6876 = relay.Function([], output)
mod['func_6876'] = func_6876
mod = relay.transform.InferType()(mod)
mutated_mod['func_6876'] = func_6876
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6876_call = mutated_mod.get_global_var('func_6876')
call_6877 = func_6876_call()
output = call_6877
func_6878 = relay.Function([], output)
mutated_mod['func_6878'] = func_6878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5135_call = mod.get_global_var('func_5135')
func_5137_call = mutated_mod.get_global_var('func_5137')
call_6961 = relay.TupleGetItem(func_5135_call(), 0)
call_6962 = relay.TupleGetItem(func_5137_call(), 0)
output = call_6961
output2 = call_6962
func_6966 = relay.Function([], output)
mod['func_6966'] = func_6966
mod = relay.transform.InferType()(mod)
mutated_mod['func_6966'] = func_6966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6966_call = mutated_mod.get_global_var('func_6966')
call_6967 = func_6966_call()
output = call_6967
func_6968 = relay.Function([], output)
mutated_mod['func_6968'] = func_6968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6822_call = mod.get_global_var('func_6822')
func_6823_call = mutated_mod.get_global_var('func_6823')
call_6969 = relay.TupleGetItem(func_6822_call(), 2)
call_6970 = relay.TupleGetItem(func_6823_call(), 2)
func_6450_call = mod.get_global_var('func_6450')
func_6454_call = mutated_mod.get_global_var('func_6454')
var_6978 = relay.var("var_6978", dtype = "uint32", shape = ())#candidate|6978|()|var|uint32
var_6979 = relay.var("var_6979", dtype = "uint8", shape = (1, 2145))#candidate|6979|(1, 2145)|var|uint8
call_6977 = relay.TupleGetItem(func_6450_call(relay.reshape(var_6978.astype('uint32'), []), relay.reshape(var_6979.astype('uint8'), [2145,]), ), 3)
call_6980 = relay.TupleGetItem(func_6454_call(relay.reshape(var_6978.astype('uint32'), []), relay.reshape(var_6979.astype('uint8'), [2145,]), ), 3)
bop_6984 = relay.add(var_6978.astype('int8'), var_6979.astype('int8')) # shape=(1, 2145)
uop_6988 = relay.sigmoid(call_6969.astype('float32')) # shape=(9, 5, 2)
uop_6990 = relay.sigmoid(call_6970.astype('float32')) # shape=(9, 5, 2)
output = relay.Tuple([call_6977,bop_6984,uop_6988,])
output2 = relay.Tuple([call_6980,bop_6984,uop_6990,])
func_6991 = relay.Function([var_6978,var_6979,], output)
mod['func_6991'] = func_6991
mod = relay.transform.InferType()(mod)
mutated_mod['func_6991'] = func_6991
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6991_call = mutated_mod.get_global_var('func_6991')
var_6993 = relay.var("var_6993", dtype = "uint32", shape = ())#candidate|6993|()|var|uint32
var_6994 = relay.var("var_6994", dtype = "uint8", shape = (1, 2145))#candidate|6994|(1, 2145)|var|uint8
call_6992 = func_6991_call(var_6993,var_6994,)
output = call_6992
func_6995 = relay.Function([var_6993,var_6994,], output)
mutated_mod['func_6995'] = func_6995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6650_call = mod.get_global_var('func_6650')
func_6651_call = mutated_mod.get_global_var('func_6651')
call_7042 = func_6650_call()
call_7043 = func_6650_call()
func_2150_call = mod.get_global_var('func_2150')
func_2152_call = mutated_mod.get_global_var('func_2152')
var_7054 = relay.var("var_7054", dtype = "uint8", shape = (2145,))#candidate|7054|(2145,)|var|uint8
call_7053 = relay.TupleGetItem(func_2150_call(relay.reshape(var_7054.astype('uint8'), [2145,])), 3)
call_7055 = relay.TupleGetItem(func_2152_call(relay.reshape(var_7054.astype('uint8'), [2145,])), 3)
output = relay.Tuple([call_7042,call_7053,var_7054,])
output2 = relay.Tuple([call_7043,call_7055,var_7054,])
func_7058 = relay.Function([var_7054,], output)
mod['func_7058'] = func_7058
mod = relay.transform.InferType()(mod)
var_7059 = relay.var("var_7059", dtype = "uint8", shape = (2145,))#candidate|7059|(2145,)|var|uint8
output = func_7058(var_7059)
func_7060 = relay.Function([var_7059], output)
mutated_mod['func_7060'] = func_7060
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1575_call = mod.get_global_var('func_1575')
func_1577_call = mutated_mod.get_global_var('func_1577')
call_7078 = relay.TupleGetItem(func_1575_call(), 3)
call_7079 = relay.TupleGetItem(func_1577_call(), 3)
uop_7080 = relay.erf(call_7078.astype('float64')) # shape=(2145,)
uop_7082 = relay.erf(call_7079.astype('float64')) # shape=(2145,)
bop_7083 = relay.right_shift(uop_7080.astype('uint8'), relay.reshape(call_7078.astype('uint8'), relay.shape_of(uop_7080))) # shape=(2145,)
bop_7086 = relay.right_shift(uop_7082.astype('uint8'), relay.reshape(call_7079.astype('uint8'), relay.shape_of(uop_7082))) # shape=(2145,)
output = relay.Tuple([bop_7083,])
output2 = relay.Tuple([bop_7086,])
func_7096 = relay.Function([], output)
mod['func_7096'] = func_7096
mod = relay.transform.InferType()(mod)
mutated_mod['func_7096'] = func_7096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7096_call = mutated_mod.get_global_var('func_7096')
call_7097 = func_7096_call()
output = call_7097
func_7098 = relay.Function([], output)
mutated_mod['func_7098'] = func_7098
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7132 = relay.const([[[-8]]], dtype = "int16")#candidate|7132|(1, 1, 1)|const|int16
var_7133 = relay.var("var_7133", dtype = "int16", shape = (11, 3, 15))#candidate|7133|(11, 3, 15)|var|int16
bop_7134 = relay.subtract(const_7132.astype('int16'), var_7133.astype('int16')) # shape=(11, 3, 15)
output = relay.Tuple([bop_7134,])
output2 = relay.Tuple([bop_7134,])
func_7137 = relay.Function([var_7133,], output)
mod['func_7137'] = func_7137
mod = relay.transform.InferType()(mod)
mutated_mod['func_7137'] = func_7137
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7138 = relay.var("var_7138", dtype = "int16", shape = (11, 3, 15))#candidate|7138|(11, 3, 15)|var|int16
func_7137_call = mutated_mod.get_global_var('func_7137')
call_7139 = func_7137_call(var_7138)
output = call_7139
func_7140 = relay.Function([var_7138], output)
mutated_mod['func_7140'] = func_7140
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5694_call = mod.get_global_var('func_5694')
func_5696_call = mutated_mod.get_global_var('func_5696')
call_7165 = func_5694_call()
call_7166 = func_5694_call()
output = relay.Tuple([call_7165,])
output2 = relay.Tuple([call_7166,])
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
var_7208 = relay.var("var_7208", dtype = "float64", shape = (12, 3, 12))#candidate|7208|(12, 3, 12)|var|float64
uop_7209 = relay.log2(var_7208.astype('float64')) # shape=(12, 3, 12)
output = uop_7209
output2 = uop_7209
func_7221 = relay.Function([var_7208,], output)
mod['func_7221'] = func_7221
mod = relay.transform.InferType()(mod)
mutated_mod['func_7221'] = func_7221
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7222 = relay.var("var_7222", dtype = "float64", shape = (12, 3, 12))#candidate|7222|(12, 3, 12)|var|float64
func_7221_call = mutated_mod.get_global_var('func_7221')
call_7223 = func_7221_call(var_7222)
output = call_7223
func_7224 = relay.Function([var_7222], output)
mutated_mod['func_7224'] = func_7224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3759_call = mod.get_global_var('func_3759')
func_3761_call = mutated_mod.get_global_var('func_3761')
call_7279 = relay.TupleGetItem(func_3759_call(), 0)
call_7280 = relay.TupleGetItem(func_3761_call(), 0)
output = call_7279
output2 = call_7280
func_7281 = relay.Function([], output)
mod['func_7281'] = func_7281
mod = relay.transform.InferType()(mod)
output = func_7281()
func_7282 = relay.Function([], output)
mutated_mod['func_7282'] = func_7282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3863_call = mod.get_global_var('func_3863')
func_3864_call = mutated_mod.get_global_var('func_3864')
call_7312 = relay.TupleGetItem(func_3863_call(), 0)
call_7313 = relay.TupleGetItem(func_3864_call(), 0)
output = relay.Tuple([call_7312,])
output2 = relay.Tuple([call_7313,])
func_7314 = relay.Function([], output)
mod['func_7314'] = func_7314
mod = relay.transform.InferType()(mod)
mutated_mod['func_7314'] = func_7314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7314_call = mutated_mod.get_global_var('func_7314')
call_7315 = func_7314_call()
output = call_7315
func_7316 = relay.Function([], output)
mutated_mod['func_7316'] = func_7316
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7322 = relay.var("var_7322", dtype = "float64", shape = (7, 4, 10))#candidate|7322|(7, 4, 10)|var|float64
var_7323 = relay.var("var_7323", dtype = "float64", shape = (7, 4, 10))#candidate|7323|(7, 4, 10)|var|float64
bop_7324 = relay.floor_mod(var_7322.astype('float64'), relay.reshape(var_7323.astype('float64'), relay.shape_of(var_7322))) # shape=(7, 4, 10)
uop_7338 = relay.tan(var_7322.astype('float64')) # shape=(7, 4, 10)
output = relay.Tuple([bop_7324,uop_7338,])
output2 = relay.Tuple([bop_7324,uop_7338,])
func_7343 = relay.Function([var_7322,var_7323,], output)
mod['func_7343'] = func_7343
mod = relay.transform.InferType()(mod)
var_7344 = relay.var("var_7344", dtype = "float64", shape = (7, 4, 10))#candidate|7344|(7, 4, 10)|var|float64
var_7345 = relay.var("var_7345", dtype = "float64", shape = (7, 4, 10))#candidate|7345|(7, 4, 10)|var|float64
output = func_7343(var_7344,var_7345,)
func_7346 = relay.Function([var_7344,var_7345,], output)
mutated_mod['func_7346'] = func_7346
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2848_call = mod.get_global_var('func_2848')
func_2850_call = mutated_mod.get_global_var('func_2850')
call_7400 = relay.TupleGetItem(func_2848_call(), 1)
call_7401 = relay.TupleGetItem(func_2850_call(), 1)
output = call_7400
output2 = call_7401
func_7403 = relay.Function([], output)
mod['func_7403'] = func_7403
mod = relay.transform.InferType()(mod)
output = func_7403()
func_7404 = relay.Function([], output)
mutated_mod['func_7404'] = func_7404
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3863_call = mod.get_global_var('func_3863')
func_3864_call = mutated_mod.get_global_var('func_3864')
call_7420 = relay.TupleGetItem(func_3863_call(), 0)
call_7421 = relay.TupleGetItem(func_3864_call(), 0)
func_6991_call = mod.get_global_var('func_6991')
func_6995_call = mutated_mod.get_global_var('func_6995')
const_7426 = relay.const(8, dtype = "uint32")#candidate|7426|()|const|uint32
const_7427 = relay.const([[2,-1,-10],[5,-5,10],[-1,3,-1],[-10,10,-1],[3,9,-9],[8,6,6],[-10,-1,-10],[-8,-8,-5],[-1,-10,-6],[-1,1,4],[-3,-9,-6],[5,8,2],[1,-10,-8],[-7,-10,9],[8,-5,-9],[8,3,-3],[4,6,7],[1,5,-4],[4,3,8],[10,-1,-6],[-3,-4,-2],[7,6,10],[-1,-1,10],[-1,-9,-10],[6,5,-2],[10,5,-6],[-3,-5,-6],[4,5,6],[-3,4,1],[2,-2,7],[-8,-1,-2],[-10,-10,6],[1,5,-7],[5,-8,-3],[3,-8,-2],[8,3,3],[-8,2,1],[6,-8,-9],[-2,7,3],[8,-5,10],[-3,-7,2],[4,6,-8],[4,8,6],[8,-4,-5],[5,5,-10],[-7,-5,-1],[-6,-7,-9],[-7,2,4],[7,-4,-7],[9,4,3],[-9,9,5],[-3,5,1],[-8,6,8],[-5,-3,5],[2,3,-8],[-2,-7,2],[-10,-2,6],[10,6,3],[-7,-8,-1],[-10,6,7],[-2,-10,-1],[-2,7,8],[9,-9,-4],[-10,1,1],[10,-5,7],[-10,-2,-1],[-3,3,-6],[5,-9,-2],[-5,3,-10],[-9,8,-9],[-5,-7,1],[9,-10,4],[-5,3,1],[8,10,3],[-8,4,-6],[2,-4,-8],[6,9,-2],[-1,-9,-3],[-4,6,6],[7,2,1],[-6,9,3],[-7,9,-4],[6,-9,2],[7,5,-1],[3,-5,9],[2,9,7],[1,1,-9],[-10,-10,2],[-3,9,2],[-8,-8,-9],[9,4,5],[1,5,-5],[-7,-1,-5],[9,2,5],[10,9,6],[-4,-9,4],[10,-9,7],[1,-10,1],[5,-3,-9],[-1,2,6],[-7,-5,-1],[-2,6,7],[-7,9,1],[5,1,-3],[8,9,5],[2,-8,-8],[-7,9,2],[-9,4,-8],[-8,-1,3],[-9,-9,3],[-6,5,1],[2,-4,1],[6,-6,-8],[7,7,4],[3,3,6],[7,-2,-5],[-8,2,5],[-7,-5,-3],[-7,-8,-8],[6,-10,7],[-6,5,9],[-2,-6,-6],[-8,-3,-7],[-6,7,-1],[-8,8,6],[3,2,-10],[9,-5,-6],[5,-7,7],[-7,8,-8],[-10,-6,6],[6,5,-9],[-6,-7,-1],[-3,7,7],[3,8,9],[-2,6,-7],[-3,-2,-10],[1,9,-10],[-1,9,2],[3,-1,1],[-6,-8,5],[7,-8,-4],[9,-8,-5],[9,1,5],[5,3,8],[-7,-8,-9],[8,-9,-4],[-9,-10,3],[5,-3,-1],[2,-6,-5],[8,1,7],[-9,3,-3],[10,-1,-9],[8,-6,10],[1,7,-8],[4,-4,-2],[-2,-6,-8],[3,3,2],[8,-5,3],[6,-1,3],[-7,5,-1],[-2,9,-1],[9,9,-10],[5,1,4],[7,-7,-5],[8,-7,-3],[2,-3,-5],[10,-8,5],[9,6,10],[-3,-2,-5],[-1,10,6],[8,9,10],[6,8,-10],[2,3,-9],[-7,-1,-5],[9,9,-5],[3,4,-7],[-7,-6,-6],[10,-8,-5],[-7,1,3],[-4,3,-2],[-10,-4,-10],[-3,-5,-4],[5,-9,8],[-2,-6,2],[-1,2,10],[2,2,8],[-10,-2,10],[-6,-1,-10],[8,-3,4],[-4,2,7],[-3,-3,9],[-8,2,4],[6,-9,-4],[8,-10,6],[8,7,7],[1,-6,-4],[8,6,2],[4,-1,-6],[1,-8,-7],[-4,-6,5],[6,-3,2],[1,-9,-2],[10,-8,-8],[-7,10,-9],[-2,2,-4],[3,-2,-6],[6,-2,6],[-6,9,-7],[-10,-5,2],[7,-5,-3],[-5,8,-5],[-10,2,5],[-8,-4,7],[-4,-4,9],[-3,9,7],[-8,2,-10],[2,7,-3],[-2,5,8],[5,-1,2],[-6,-6,4],[1,-6,10],[10,-5,6],[1,-9,-5],[-8,-10,1],[9,-9,-6],[-10,7,-10],[3,10,8],[6,-5,-6],[1,-1,5],[2,-1,10],[-6,-4,6],[9,-3,7],[-7,1,-9],[10,-4,-2],[-5,2,-5],[-5,3,-3],[3,-6,3],[8,-8,1],[7,-7,4],[-10,4,-7],[6,-2,-1],[-6,9,3],[-7,1,1],[1,3,10],[7,-8,-4],[2,7,7],[-8,-4,-6],[10,-7,9],[3,7,7],[-5,7,-5],[-8,-1,8],[-5,-2,5],[6,-1,8],[-3,9,-9],[9,-1,9],[7,1,-4],[-5,-7,-8],[3,8,8],[-6,-7,3],[1,1,-8],[6,-6,3],[-7,-9,-3],[7,-10,2],[2,-9,2],[4,3,5],[-6,9,9],[-1,8,1],[6,9,-4],[4,-10,-5],[-4,-8,-6],[2,-8,-3],[-3,-5,6],[-4,3,-10],[6,-3,6],[1,-6,-1],[-3,-2,4],[-10,-10,7],[1,10,-5],[-1,4,-7],[1,-4,-8],[9,8,4],[7,-10,-9],[4,-8,-3],[5,-6,-7],[3,3,-3],[2,2,-3],[3,-2,-8],[-10,2,9],[3,-9,-4],[3,2,-5],[-5,-9,7],[7,4,3],[-2,-6,-2],[-8,-8,-5],[-3,2,-4],[-2,-3,8],[-5,-2,-4],[-2,-7,-9],[-3,6,-5],[-6,1,4],[4,-4,7],[9,-7,-8],[5,7,8],[2,4,3],[-3,8,8],[1,5,10],[-7,1,-1],[3,1,-9],[8,2,-3],[1,-3,-2],[-10,4,-8],[7,-5,-9],[1,2,4],[5,-5,3],[-2,-6,5],[8,10,-3],[4,6,-10],[6,7,-5],[9,2,-7],[-4,9,-3],[-9,-10,-1],[-9,-2,-4],[10,-6,-10],[-7,-3,5],[-3,-6,-8],[-9,-8,-7],[-3,-3,1],[-7,-1,-7],[6,-10,-6],[8,3,-4],[-10,7,3],[8,10,10],[1,2,2],[1,-7,8],[5,3,-7],[8,-9,7],[10,-7,-7],[2,4,-9],[5,-6,-2],[-6,-8,2],[5,5,6],[-7,9,7],[-10,-5,-4],[3,-6,-4],[1,3,10],[-5,7,10],[-5,-10,-2],[2,5,-10],[-2,10,10],[-6,5,-10],[-5,9,-8],[5,-7,-8],[9,5,-5],[-5,-6,5],[-1,8,-10],[-9,5,9],[9,7,-7],[7,2,2],[-4,6,-3],[7,4,10],[-4,-1,8],[-4,-3,3],[5,8,9],[-5,-8,-5],[4,5,-7],[-3,3,-2],[3,-8,-9],[6,10,-9],[3,-3,7],[-2,-2,-8],[-3,2,5],[8,1,2],[-8,2,-2],[8,7,6],[3,-6,8],[-4,4,-6],[-1,7,-10],[-2,9,6],[-8,-5,-10],[-10,3,-8],[9,10,9],[4,-10,-1],[-2,-9,-8],[-10,-3,-3],[10,-6,7],[-3,-7,2],[1,-5,7],[-1,1,-9],[7,7,-8],[3,-2,-10],[6,-7,-8],[-10,-5,10],[-2,-2,-3],[2,-2,-9],[9,-6,-4],[10,-2,4],[6,-7,-10],[-4,9,5],[-6,-1,-8],[-7,-4,-8],[1,-10,-4],[1,10,-2],[6,-3,1],[5,9,-4],[-8,-3,-5],[-3,-8,-9],[7,6,-7],[-8,-6,8],[-2,-5,-8],[-5,-1,9],[9,2,6],[2,1,-3],[-6,-1,-3],[-8,-3,4],[-3,10,-9],[-9,2,8],[5,1,5],[4,4,-2],[6,2,6],[-1,-8,2],[-1,-6,6],[-10,3,5],[-7,7,-6],[-10,2,2],[-9,6,5],[5,-1,-8],[6,-6,-1],[-6,3,10],[4,-4,2],[-4,-10,-10],[-8,-2,9],[-6,1,-5],[6,-1,-5],[-8,2,9],[7,-9,-4],[3,-6,-1],[-8,10,-10],[2,-6,-4],[-7,-2,-4],[3,4,8],[10,2,-10],[-1,-1,-10],[7,8,6],[-4,6,-1],[7,-10,5],[1,-3,1],[7,2,4],[2,5,-3],[-3,5,5],[8,10,-4],[-7,-2,9],[4,7,5],[-9,3,6],[6,-4,-9],[-4,10,-4],[-1,-1,-3],[-6,10,4],[-5,2,-8],[5,-10,-2],[-8,5,-2],[-2,1,-6],[8,3,5],[3,2,-9],[6,2,-3],[-4,-3,-8],[-7,8,6],[4,5,-9],[-7,-2,10],[9,7,1],[-8,-2,-3],[7,-1,-9],[10,10,-3],[8,3,-8],[5,-6,-1],[-4,-3,9],[5,3,-1],[-2,8,-8],[10,2,8],[-6,-9,5],[1,-6,-6],[-8,1,8],[6,4,-3],[-6,10,8],[-9,-1,9],[8,-7,-4],[-1,7,-8],[7,8,-9],[-4,6,4],[-2,-8,-1],[10,7,-4],[-4,5,-9],[8,-6,-7],[-7,-1,-5],[-7,-8,-1],[-2,-6,10],[-9,-7,6],[7,1,-10],[10,1,10],[-8,4,-2],[3,-6,10],[-3,10,5],[-7,2,8],[6,1,1],[3,10,5],[2,5,-1],[6,6,-3],[4,3,-7],[7,-1,3],[2,3,-5],[4,-8,-7],[-4,10,-1],[-10,2,2],[-4,-5,9],[-9,3,-3],[-2,-6,-3],[-9,8,-6],[-4,-3,-10],[8,-3,-1],[8,-3,3],[7,-10,8],[-8,10,-10],[-4,-3,-3],[-1,6,-1],[-8,10,9],[-9,1,-1],[-5,-7,4],[1,2,-4],[-6,-5,1],[-3,6,-2],[7,3,-1],[8,-5,10],[4,9,7],[10,-10,-8],[-2,2,4],[-3,5,10],[4,3,5],[-1,7,7],[-5,9,-4],[6,8,4],[-4,-3,-4],[-9,3,8],[-7,8,-2],[8,-2,3],[-4,3,-9],[-5,5,3],[3,8,4],[-3,-8,5],[-6,5,1],[-7,9,8],[7,2,-1],[1,-7,-9],[6,1,5],[-2,-10,2],[-5,6,-8],[-1,-8,-9],[7,5,1],[-4,8,-1],[-3,5,-9],[7,-5,-9],[9,-2,-4],[8,-2,-5],[4,8,-9],[4,-1,7],[7,8,-9],[7,-9,-5],[-9,-4,5],[-4,1,3],[-2,-3,-8],[-4,4,-7],[1,1,4],[-2,-10,-5],[-6,-3,2],[8,-3,-8],[-1,5,6],[-10,-9,-4],[-8,7,-3],[-10,3,7],[-1,9,5],[-6,2,4],[7,-3,-5],[-9,-5,9],[-3,8,-6],[1,-9,-3],[10,3,-3],[9,8,-6],[1,6,-4],[-6,7,2],[9,1,8],[4,-3,9],[1,6,10],[-4,9,-8],[6,1,6],[-5,1,-2],[-9,-6,-3],[-8,2,6],[8,-2,-2],[2,-2,1],[6,-4,-3],[-5,-3,7],[-5,10,1],[-9,8,5],[-4,9,-10],[6,8,5],[6,-6,-1],[3,-9,3],[-1,-10,6],[10,-4,5],[-9,2,-3],[-1,-6,-8],[-1,3,5],[4,10,4],[1,5,-3],[1,-3,3],[1,7,-2],[-6,-7,7],[-7,-8,4],[1,8,-1],[8,6,5],[9,5,5],[10,-4,-10],[-9,-1,2],[-2,1,10],[-2,-3,2],[-8,-6,-7],[-2,-10,-4],[-5,-7,-1],[-2,-5,5],[-4,-6,5],[-5,-8,-8],[1,2,4],[2,-10,-8],[2,-5,2],[4,5,2],[-7,5,-9],[-2,10,-2],[1,-6,6],[1,-5,-5],[-6,-4,9],[3,5,5],[10,6,1],[-6,5,3],[-7,1,5],[-10,5,4],[-10,-3,-6],[10,-4,-7],[6,9,-7],[-5,9,8],[-2,-4,2],[2,-6,8],[-3,-7,-7],[-6,-10,-6],[-7,5,7],[-1,2,5],[-5,6,3],[-3,-2,-5],[-9,-4,6],[-7,-3,1],[6,8,-1],[-3,-3,10],[-5,-2,7],[10,8,4],[5,7,4],[7,-3,-9],[1,1,-5],[10,5,-8],[1,6,-1],[-3,2,4],[1,-5,8],[9,9,5],[-10,-3,9],[7,1,-1],[-4,1,-8],[1,6,-2],[-1,6,-10],[4,-6,-6],[2,4,9],[-8,-2,8],[-1,9,-6],[-4,1,-8],[10,2,-1],[-8,-2,-8],[10,3,-4],[3,-3,-5],[-3,-7,-8],[5,9,2],[6,6,-6],[10,-10,-9],[-5,2,-5],[6,-7,-2],[1,4,7],[-3,8,2],[4,2,-4],[-10,3,6],[2,-6,8],[-5,7,9],[5,-6,1],[-9,-9,-9],[-9,-3,-3],[-2,2,4],[-6,-7,8],[7,-7,-8],[-3,1,5],[-9,1,9],[-1,-10,9],[-3,5,-9],[5,8,-1],[10,1,-7],[5,3,8],[-1,2,-1],[7,5,-3],[7,-10,-2],[1,-6,5],[-9,9,-6],[3,-5,-1],[6,-10,2]], dtype = "uint8")#candidate|7427|(715, 3)|const|uint8
call_7425 = relay.TupleGetItem(func_6991_call(relay.reshape(const_7426.astype('uint32'), []), relay.reshape(const_7427.astype('uint8'), [1, 2145]), ), 0)
call_7428 = relay.TupleGetItem(func_6995_call(relay.reshape(const_7426.astype('uint32'), []), relay.reshape(const_7427.astype('uint8'), [1, 2145]), ), 0)
func_1239_call = mod.get_global_var('func_1239')
func_1241_call = mutated_mod.get_global_var('func_1241')
var_7435 = relay.var("var_7435", dtype = "float64", shape = (108,))#candidate|7435|(108,)|var|float64
call_7434 = relay.TupleGetItem(func_1239_call(relay.reshape(var_7435.astype('float64'), [9, 12, 1])), 0)
call_7436 = relay.TupleGetItem(func_1241_call(relay.reshape(var_7435.astype('float64'), [9, 12, 1])), 0)
uop_7442 = relay.sin(const_7427.astype('float32')) # shape=(715, 3)
const_7446 = relay.const([[0.808385,1.686679,0.485306],[-1.579646,-1.104935,-5.612202],[7.808272,-1.224817,-3.485621],[-3.855493,7.129647,-1.576593],[-7.902890,-0.832515,-2.821085],[-1.478223,7.826763,2.298691],[6.497986,-5.888469,4.398524],[-2.979246,-7.182747,7.775327],[0.421272,6.983756,2.850306],[-7.672525,-6.328515,-4.666629],[-7.606589,-8.890277,-5.152235],[5.316652,2.135105,9.074444],[-8.481966,-8.308232,5.172434],[-3.578030,5.059243,3.605967],[6.787022,-3.090444,7.591124],[-7.983085,-7.590209,4.117627],[-1.030285,-8.309493,0.455150],[6.453156,2.222897,-3.215057],[5.172782,4.147826,-8.549487],[-9.625605,4.808994,-0.409276],[3.327492,-0.695860,6.285405],[7.689805,-1.270345,-5.946180],[7.576786,-6.153882,8.775265],[4.512482,2.014168,4.610312],[-8.944770,1.343198,5.938321],[-6.847360,-1.163443,-9.028508],[-0.163347,1.783385,0.710301],[-4.940267,9.665798,6.799775],[-3.623897,-7.329546,-3.438719],[6.610048,8.221848,-6.227832],[-3.474521,0.173870,5.296034],[4.810917,2.149733,9.092922],[-7.007715,-8.053980,-0.990805],[-2.205014,-2.662092,-5.618346],[-5.839530,9.404466,-4.619634],[-2.119910,-4.765656,2.914615],[8.041128,-0.250941,5.030806],[0.565334,7.117791,-6.202794],[-3.512222,-0.362279,5.270279],[7.686088,5.069676,8.781913],[-4.299093,-1.020497,3.658761],[-5.497807,-9.470040,-7.629476],[-0.559859,9.702241,8.313574],[0.650627,-8.550247,-2.648818],[-0.211686,-9.438322,3.401223],[9.795875,0.408081,-1.104435],[6.647155,-0.190899,3.392384],[-1.414159,-5.537993,-5.544887],[6.227461,7.513511,4.063758],[4.651484,3.551922,4.746318],[9.985622,-0.351996,8.495220],[0.452122,-6.824830,-7.047636],[-6.950501,8.251319,0.283532],[-8.339011,-2.183868,-2.149723],[-3.236324,2.778620,8.180197],[-5.428020,-0.779831,-5.991840],[8.277879,-4.506159,6.197754],[-8.366366,9.615301,-7.951578],[6.547228,7.597746,0.220816],[8.172633,1.516190,4.579164],[-9.943265,3.437783,4.298039],[-7.196914,-9.777271,-0.835593],[8.925441,0.165208,-2.573668],[7.995037,9.663061,0.025438],[9.198009,-1.236350,-0.707401],[7.331430,7.311447,4.697819],[-4.636200,8.960918,-2.973990],[-7.148157,-6.926748,0.960937],[-4.940969,-4.866417,3.975592],[-7.269540,7.539717,-4.349842],[-2.204929,-2.484538,-0.489735],[-5.394521,8.908843,3.298738],[6.148728,8.611579,-5.271667],[7.503911,-6.355331,-4.353963],[0.040977,-1.035780,3.684587],[-8.774031,-1.503188,9.155196],[-9.288917,-0.309322,7.475127],[-5.592024,8.238372,9.418966],[-6.124046,-9.979724,-5.597159],[-9.101423,4.202900,-8.422422],[6.669689,4.106160,9.685735],[5.839460,-6.359794,6.979988],[0.860700,5.759658,-1.739184],[-4.659521,1.377240,4.643549],[5.891289,9.199805,-3.710782],[6.528070,6.909522,2.101045],[0.036454,-2.409203,-9.510385],[-2.328539,3.848599,4.223136],[-7.166361,-8.622527,-9.344630],[1.031445,-1.956538,7.569055],[0.285390,-3.918243,6.217042],[4.233318,-6.075786,-6.035817],[-4.426800,6.094227,-3.620682],[1.117998,-3.645054,-0.004558],[0.272646,8.814495,1.748525],[-6.538046,8.336444,3.477138],[-3.700043,-5.757814,-7.148340],[-6.899216,9.695410,5.850859],[-5.609013,-7.507963,-0.203386],[9.137393,-7.592610,6.392677],[4.356314,-3.115763,4.888653],[2.523774,0.995741,-4.912330],[0.708513,-0.440216,-1.215821],[-4.431343,-0.591657,-0.759224],[-4.078594,-1.098814,-8.701988],[-5.161195,0.065357,-0.181784],[-3.083601,-4.060996,1.507298],[9.112279,3.936746,2.033130],[8.440859,-0.985628,-6.904930],[6.828344,8.898773,-1.050108],[6.615025,4.341381,0.028691],[8.055411,-8.666396,4.444341],[0.386872,-1.224112,-2.584952],[-8.713769,9.575417,5.328066],[0.607686,-7.460662,-0.629609],[-6.107786,9.958129,-1.301123],[-6.651437,-0.162474,-6.301434],[-6.148708,3.335613,-4.507300],[2.828966,0.811978,-6.040748],[-4.228463,9.795005,-9.166260],[4.286804,-3.366076,-6.324514],[-6.459871,-9.723252,7.272668],[-8.641280,-6.030085,-0.767162],[-8.626369,-3.871976,0.539244],[-2.772568,-0.500706,-8.292072],[-3.237545,-9.357889,5.047652],[4.286068,2.117546,-2.576682],[-1.717482,-7.188982,-8.441072],[-6.842187,-4.566271,2.508906],[2.958090,-8.502082,2.590364],[-0.614272,-9.384770,-1.396620],[6.832507,0.812767,-0.101045],[-3.303873,7.993044,1.519065],[1.988949,-0.913304,-6.760440],[7.075248,7.022606,-0.279276],[5.614699,-3.552360,3.442205],[1.553184,4.667645,4.427087],[-0.178024,-2.173373,-2.859141],[-6.800861,6.132427,-1.234651],[-6.388303,6.971215,1.695034],[-0.305946,-0.519315,-8.622395],[-4.421896,3.564820,5.161198],[4.233589,-4.991142,7.297734],[5.711336,-2.516348,-2.078163],[8.964022,5.278881,-8.452061],[-1.512209,9.513424,-2.039398],[-6.290787,2.138110,-7.855406],[-0.504865,-0.192209,8.661722],[1.647689,8.453215,-1.261619],[-4.045639,-4.683513,-3.716084],[-7.449781,-9.156178,-6.084014],[-6.272631,9.897417,-3.516412],[-1.130252,0.097860,7.150115],[-8.793689,8.432692,-0.012185],[7.736283,4.305024,-8.707935],[-8.415853,-9.605232,-0.944088],[1.556023,3.232977,-7.152710],[-7.242116,-8.675687,-6.139288],[5.864187,9.693759,-2.411695],[-7.731127,-6.233681,-9.969581],[9.251457,-1.153123,2.883471],[-8.089333,6.980403,6.610693],[3.992228,-9.845678,0.599811],[8.249276,4.197071,6.252154],[7.373644,4.465678,-8.357641],[-2.488759,-6.788933,9.542665],[-4.857449,3.919731,-3.989050],[2.678463,-2.214886,0.873120],[-3.974840,-5.267065,2.265685],[-5.035857,6.577433,6.240467],[2.878281,-3.831135,-9.264827],[3.690710,3.401909,-3.049607],[2.902473,-1.972317,9.285627],[4.190318,-4.536540,9.677318],[8.216520,-4.136826,3.976779],[-9.161226,-2.768364,-3.104075],[8.734942,2.164821,-6.127611],[-7.537801,6.361335,-1.000957],[-1.868557,5.083400,8.968041],[6.790321,-5.864676,-4.953679],[8.960493,-5.140773,3.584080],[-0.195136,-2.994911,4.669559],[9.615236,-5.543230,-4.326449],[1.300757,-1.206119,-0.542464],[5.210630,-2.125517,9.433321],[8.280576,-8.776423,-0.328853],[-0.049058,-4.420636,-5.923554],[-0.022255,3.804092,9.022619],[3.750809,-5.603664,8.357703],[6.579960,-1.994658,-2.601867],[-7.873120,-7.270012,9.958150],[-6.533758,3.797641,-2.481130],[5.823824,3.308998,2.032369],[-9.281714,5.859103,-4.763556],[8.563961,1.574567,1.399772],[-2.912325,0.668837,-7.244680],[8.960474,5.988907,2.304553],[5.197338,-8.382038,1.317041],[3.418436,-9.947570,5.280879],[3.531283,-1.071138,-5.129433],[-0.170220,-4.481684,-7.503210],[-0.997334,9.681515,-5.642229],[1.987946,0.139561,3.912503],[2.587412,6.695084,7.175893],[-8.060510,5.657822,-1.953353],[-1.071066,-3.120203,-1.689632],[-1.150329,6.280038,-6.625690],[-0.645069,6.372170,2.251197],[2.175489,1.904998,-5.383636],[2.344915,2.760968,-6.808499],[-9.424099,-0.315732,8.088042],[8.601923,1.682778,2.540579],[5.951521,6.214381,-9.637740],[6.574190,9.093491,-1.636913],[7.819826,-3.903795,-0.621009],[-0.661947,2.386109,-8.437574],[-3.103644,-8.191448,-4.321659],[3.056563,-2.635567,-1.943958],[-0.080452,-7.014863,-2.610142],[2.403066,-2.205205,-0.263243],[-2.163068,4.422076,9.631395],[-7.581532,-3.061436,8.665231],[8.281053,-1.028193,9.599894],[-1.084482,-6.004068,4.196065],[6.056376,-6.471122,-2.004500],[-6.118003,-3.433139,-5.188844],[7.974620,6.781529,-6.516188],[-4.832115,5.327574,8.226271],[6.223456,-5.914358,-7.814026],[-6.275800,1.274135,8.397839],[5.735779,-0.068662,7.286976],[1.632239,-3.324319,-9.433749],[2.242886,-2.907690,0.454642],[5.577037,9.052429,-2.410856],[0.988785,4.163134,-2.466351],[-8.458588,-3.121237,1.304466],[-9.923620,8.779663,5.573228],[0.904880,-7.341976,7.516427],[0.111514,0.262476,0.148270],[-3.682732,-5.627793,1.265510],[-8.890235,4.273557,-6.271179],[-1.270594,3.801131,0.216902],[-3.911750,-9.617230,-9.478803],[-7.819823,-7.904474,-6.022227],[-5.036094,3.217403,-1.668544],[0.372743,-3.056116,-1.581726],[1.342451,1.261628,-9.739633],[2.237166,4.461812,3.733488],[6.261097,2.064251,6.004912],[5.168990,-4.038091,3.098847],[6.227199,7.100278,3.702807],[8.310531,7.588508,3.595190],[5.146095,-9.420480,-9.788420],[0.401337,2.416577,-8.263124],[-9.975475,-5.087558,-9.862735],[-4.223888,-8.549175,5.891198],[4.187017,-4.461698,-1.481199],[-9.306139,-9.244829,-0.376570],[-2.020335,6.744474,1.256922],[0.497429,7.179254,-0.170477],[8.284838,-0.674750,1.859156],[9.719934,-9.281569,7.631821],[7.847276,-8.635031,-5.945894],[2.492501,-8.655124,-7.187032],[-7.687932,-4.442402,-3.736842],[7.859837,5.156346,3.946607],[6.932485,4.221186,9.959087],[-6.159087,-1.809829,-6.951695],[-1.546448,2.480582,-7.464110],[-3.312652,9.053395,2.599083],[1.432823,1.812882,-8.297088],[4.153446,7.412033,8.290290],[3.394759,-1.324981,-6.241236],[-0.537782,-2.189529,-7.791462],[-1.974497,3.556475,4.631060],[5.523505,3.784978,8.666772],[2.563505,6.552095,2.327998],[4.798113,0.679771,-0.330737],[0.074555,-5.727887,-9.428874],[-5.302160,9.173630,3.222455],[-7.766106,6.448222,8.821494],[6.069705,-6.849109,-1.910610],[3.830614,-6.785617,5.166504],[8.735489,-1.533423,-9.295552],[-1.816664,4.999706,-4.903498],[-9.006098,7.688161,-7.753860],[-5.137113,4.358316,-4.514897],[-7.024250,-9.028336,-1.079384],[4.240144,-3.744587,0.531062],[-2.519993,9.449556,1.529438],[-6.459748,4.802992,-7.707578],[3.253967,9.754892,3.886860],[-4.887260,-5.592158,-1.929701],[-1.851032,-1.088124,2.240850],[5.356597,2.775715,1.172577],[-5.612374,-0.975861,5.580447],[1.509815,0.963366,-9.724890],[-6.433275,-3.337762,9.374319],[-6.448826,-6.295980,-6.084552],[-2.520543,1.962744,-0.025433],[4.045654,8.176044,-0.485525],[-7.542272,0.496041,5.450997],[-0.981442,-6.757817,-3.373070],[6.670730,0.605586,1.577261],[-2.460698,3.456963,9.222237],[-0.366427,-2.042804,-3.626587],[4.281329,-0.078369,-3.483884],[-9.376023,4.487718,0.086853],[-9.814141,-7.456091,-5.392133],[7.440913,-0.715211,-0.309077],[-8.313133,-1.470228,-6.677301],[-8.864798,4.774170,-3.577532],[-2.451428,-8.860061,7.535754],[0.797390,-4.445277,2.880324],[4.885809,4.356030,4.129944],[8.966296,3.635746,-3.776658],[-1.153120,6.912254,5.212429],[0.970217,-0.096284,-7.598497],[1.111479,3.982561,4.265898],[-7.932673,7.419930,-5.270839],[4.269864,-2.982607,7.059833],[3.096774,1.341422,3.659880],[-1.470924,-6.991726,-3.147422],[2.219221,-9.695256,-7.293310],[4.390683,-0.803264,-8.378740],[-7.091615,-6.736374,-7.388718],[3.188526,8.320521,-5.431146],[-1.579831,3.836519,0.525193],[8.734201,6.158162,2.086804],[7.320991,-0.599704,1.797875],[1.989904,4.035775,1.392588],[3.056088,7.147285,7.189943],[-9.782231,-3.042333,7.087933],[7.432804,-9.306331,-0.394180],[-1.473843,6.952243,-7.396831],[-2.779676,-1.281752,3.119612],[6.377182,-2.521264,-9.487424],[1.441923,3.585006,-7.523509],[2.441795,1.853817,4.057649],[-5.027419,-6.424519,-6.465141],[-4.587997,-3.173576,-3.380275],[-2.673714,-5.065086,-6.737522],[1.495211,6.802187,-9.642381],[7.845524,-3.433709,3.078800],[-1.633335,9.719691,9.631284],[5.737798,-6.222738,-4.124237],[-2.377137,7.932861,-0.780936],[3.681657,1.653540,-6.718136],[-9.970960,7.055912,1.246025],[-6.504893,-0.592846,-7.421538],[-5.983555,-1.610150,2.135657],[6.546575,3.860529,-0.789902],[5.476536,3.473637,8.524397],[-9.209433,2.592228,-3.071825],[-3.381244,2.885653,-4.184500],[7.392865,2.531985,-3.836863],[-4.863453,-8.510348,-9.186973],[1.177711,-8.984272,-6.140215],[6.577268,-8.174097,-9.171245],[1.918360,8.275021,-6.478530],[-7.517342,-0.463918,6.628608],[-6.214520,7.339720,3.554047],[2.662099,3.669244,-1.443698],[2.071628,-3.912408,-5.284043],[-3.870145,5.838815,-5.172267],[-3.682499,2.547272,9.986533],[1.484246,0.144764,-2.242872],[-6.048196,2.242202,-9.243983],[2.243787,3.680601,6.238358],[-4.759079,5.274319,5.519241],[4.688166,-7.977173,0.471609],[0.876496,1.574030,6.569995],[-8.654325,-0.571540,4.544878],[5.113501,-5.462929,-8.626674],[-3.050363,-2.248650,-2.287347],[-6.886051,0.997377,7.340513],[-0.044107,5.208982,3.072332],[5.632777,-8.989482,2.449268],[-2.625496,-0.475053,-0.664772],[-0.943471,1.708405,-6.566293],[9.654680,-8.164251,-9.980668],[3.806644,-7.444953,-5.729944],[1.079187,8.484801,6.792961],[7.252692,5.882207,1.701284],[-2.735317,5.379944,-6.048013],[2.570111,-5.287816,-8.816618],[2.581014,0.352694,-2.528129],[0.272087,6.183977,3.167526],[-2.226443,8.615632,-8.413831],[6.825352,-0.930663,-5.883066],[-8.066417,-6.870832,3.568906],[8.885802,-6.601260,7.097148],[8.008803,-5.758576,0.717139],[0.821822,-3.127014,-8.818700],[3.486098,8.172979,-2.112813],[-7.218420,-6.918362,3.561586],[7.247962,-4.535210,6.173887],[-2.190201,0.645186,1.657964],[-2.975265,-4.054044,4.350780],[1.586659,-2.496566,4.186213],[4.110776,1.927890,-8.094230],[5.985533,-4.970924,-5.687300],[2.125032,-9.193609,0.483572],[-8.902156,-0.917143,5.111864],[2.302571,8.933546,5.796208],[-3.468230,-5.724137,-7.710768],[-6.112501,9.754941,-7.885683],[-6.577995,-5.379049,-3.654787],[-8.480022,-3.060226,7.612071],[3.014141,-8.062753,-2.051994],[7.295046,-1.671456,-0.811498],[-5.940705,8.811204,5.339903],[7.962614,5.627148,-7.592802],[-1.085301,-5.610781,-4.710419],[-1.409390,-4.208894,-6.019967],[-0.305886,6.416303,4.154380],[-4.637840,-0.013154,9.193983],[4.616670,2.671485,7.823175],[-3.567463,5.547883,-5.542848],[-5.452084,1.894955,8.522270],[8.827743,3.175552,5.839713],[-6.338782,-4.235388,9.788367],[6.532445,2.006589,4.594547],[-2.130155,-4.254099,7.923191],[4.367027,7.164646,-4.659211],[-3.560468,-7.394627,3.181513],[1.261605,9.209809,-9.899269],[3.774824,8.324653,4.051782],[3.761306,-0.092200,5.378010],[-9.738110,5.408504,6.147824],[8.970455,7.411437,0.232195],[0.604235,0.584988,-9.370380],[1.158315,5.819980,-0.889121],[2.657883,-2.399811,9.116672],[5.938920,3.529237,7.904213],[1.854046,-2.891543,1.128356],[6.031472,-8.641007,5.197076],[-8.043548,1.071032,-3.020716],[-1.364047,9.179515,2.955062],[-6.407772,5.972605,-5.909371],[-0.592066,1.519532,-7.760279],[-1.887993,1.150045,-8.601958],[-5.022153,1.427187,-3.926665],[0.174451,1.119620,-0.343975],[-5.045464,-4.038749,-8.720692],[-3.446406,-1.615067,9.142241],[-7.841263,-5.879458,5.332724],[9.135547,1.826472,5.458148],[-7.846242,8.913767,0.161330],[-7.281427,-1.719310,0.724270],[6.533822,-4.614035,8.541928],[7.402257,9.004763,1.698549],[-5.473375,-1.774322,8.380713],[-1.943945,4.737013,-4.797962],[8.279532,-5.115809,6.285917],[-3.798811,4.668085,-4.366094],[-3.948418,9.058511,7.174984],[-8.336124,8.720088,4.967523],[-2.456880,-2.541712,0.550869],[3.638681,6.131372,5.958526],[6.009752,-4.096463,-5.429520],[-6.466876,-0.633944,-7.400829],[-2.978446,5.640633,-7.501215],[5.785885,-7.766711,-1.008808],[-5.193559,-0.974558,5.245814],[-7.968652,7.393136,0.958632],[7.811831,9.939315,4.767634],[5.972722,-9.637046,7.459648],[5.406801,-8.087703,-1.164988],[-5.839419,-4.890709,5.847725],[-0.583833,-4.248273,-8.904173],[1.840877,6.442038,1.379936],[-9.336317,7.257461,7.910663],[2.008005,9.182646,7.895041],[-5.835726,-1.295892,-5.117484],[-7.666078,9.116053,2.199159],[1.935881,3.665471,0.810317],[8.126154,6.904810,-7.010348],[-9.625634,2.140177,3.913961],[0.622049,-1.162887,-2.006676],[7.319650,9.959883,-1.094742],[-5.478325,9.462509,-4.274703],[-4.121526,1.561402,-5.906251],[8.317821,2.862779,-3.985400],[0.648998,1.138343,8.049544],[-7.241658,-0.425526,2.822049],[-4.906855,-3.549711,7.556964],[-9.607396,9.402403,6.493992],[-0.599871,-3.264760,-7.373183],[-1.068960,-9.721815,4.162065],[-3.446337,6.177966,-7.392780],[1.948897,-8.451537,-2.971015],[-5.526957,-2.448065,-2.228157],[-2.976077,-8.423487,8.924125],[7.950556,-9.549082,4.360719],[-7.631312,7.683440,-6.436493],[-3.475130,1.764798,-2.713663],[7.042724,-2.937838,-0.973894],[3.146019,8.159709,2.462783],[-7.300827,4.933360,-5.283116],[1.892460,-4.697824,-6.146116],[-9.931300,-7.683749,-9.937216],[6.437081,7.890528,1.162759],[3.537410,-0.656973,-3.061460],[8.938955,1.069265,4.081000],[7.091956,-6.452367,0.239689],[-6.873835,5.081199,4.498495],[3.105448,2.885312,4.672685],[-9.248000,-3.887572,0.933620],[-5.413965,3.951990,0.840749],[-0.912449,0.051874,-9.462897],[0.549266,-2.598625,3.756297],[-6.169307,2.976847,-8.025174],[-8.065198,2.889854,7.529620],[8.718171,3.953081,5.251279],[7.594948,4.236362,-2.643975],[-6.347167,-7.700931,0.972733],[-4.679092,9.809886,4.269393],[-9.960429,-9.528259,-1.014563],[2.863675,-8.727043,5.850488],[7.509292,8.382990,6.800463],[5.785083,5.567838,5.079343],[2.966316,7.199385,4.626270],[-0.365714,-4.829442,0.140798],[4.361666,0.022856,3.574663],[3.447714,6.589027,7.930488],[7.904099,-5.208251,-8.839065],[9.691780,-3.694818,-9.164677],[4.437612,7.136249,-5.481734],[9.396676,7.282337,7.733651],[7.901435,-8.034831,9.863547],[2.301309,-0.407490,6.374907],[4.270048,-4.722792,8.460730],[8.836896,-0.291567,6.470347],[2.232465,-9.784326,6.848797],[7.486576,-6.793006,9.976758],[8.770979,-1.706626,6.051701],[9.316921,-2.571464,-4.147210],[-4.961878,9.707044,-0.819090],[2.808167,8.162462,9.959353],[5.357633,9.340288,-9.164507],[7.384536,3.032366,5.216435],[-4.179806,-8.334978,-9.131991],[-5.260889,-6.571179,9.285473],[-6.574554,1.252574,-9.275388],[-3.666580,2.776155,-6.526975],[9.512517,-9.394502,4.067618],[0.636050,-1.447964,6.309137],[-4.772761,6.032413,7.608084],[5.930407,-0.686814,4.497451],[3.780762,-9.519215,9.040431],[-5.786729,8.449615,8.328796],[-0.133778,-3.723731,-8.898232],[-7.032442,2.498863,-5.604016],[-2.310035,2.151008,-1.733631],[-8.964091,-7.729513,-5.333143],[7.828563,-5.714931,9.185785],[9.138118,-7.734881,-9.393166],[9.054081,0.666241,7.786251],[0.895001,-4.059385,-7.298942],[9.373939,-8.760385,4.027438],[7.901382,-3.304148,9.536282],[-6.287759,1.934288,-2.506880],[7.910470,-0.316136,9.423841],[-1.656500,-8.816140,1.152958],[6.483396,5.653062,-7.283045],[1.147930,2.703475,-7.930940],[9.440522,7.602745,5.959984],[2.715874,-4.128993,-2.892964],[4.616360,-6.762386,8.063714],[-7.238318,4.375960,-6.278817],[-9.106445,1.865909,2.317796],[2.837287,-7.245740,-6.260539],[-9.467721,4.479434,6.117856],[-7.986692,-0.569737,-8.417553],[-1.875384,3.269067,-3.937468],[-8.695315,5.563982,-1.154786],[2.829127,2.095628,6.585273],[7.929668,2.237356,-8.238566],[-1.749981,0.052241,6.447694],[-1.068953,-5.663108,1.179988],[-7.673201,-0.504916,-2.118953],[-4.534747,-0.290864,7.321576],[0.676715,8.886383,1.307160],[-2.496542,8.497263,2.379306],[7.260763,-7.119144,8.017715],[8.252953,8.367531,3.146367],[-3.863772,3.460770,6.050860],[-6.799694,-8.666628,-5.308296],[0.161613,3.523095,-1.002026],[-7.663550,9.718016,-9.012160],[-6.068479,-1.440206,9.406350],[6.991876,2.658219,-4.740372],[-6.301394,-2.410773,-7.027284],[-8.822678,5.746288,-6.805834],[-4.828531,7.353998,-5.688283],[-9.177896,6.140987,-5.356157],[-7.305587,9.780087,2.004080],[1.398202,-4.411052,-5.170432],[-7.567137,8.928331,-0.177321],[5.412416,-1.326195,-5.712291],[-9.835384,8.080463,4.195503],[-8.755122,-4.123768,-2.504757],[6.469209,0.974431,5.696488],[7.322102,-1.412236,6.915224],[-2.591809,-4.383299,5.811404],[3.974556,1.943972,-4.600687],[9.879957,5.892149,-6.195731],[1.779000,2.602960,0.799948],[-5.192292,-8.927235,8.866662],[2.778757,-8.258182,-5.039607],[2.317848,-5.799546,3.357181],[4.193091,5.716427,-7.514572],[-8.253692,-4.618867,-6.113172],[-0.990135,-7.968956,6.742923],[-5.746205,5.135986,-3.327005],[8.143271,-8.147073,4.238064],[-7.198403,-7.373580,8.503575],[7.167807,-4.963587,0.544555],[3.684839,2.485567,-4.166376],[-6.613980,6.804212,1.943323],[4.303755,5.376606,-1.239176],[1.788003,-4.984395,8.005369],[-6.753763,8.044540,-4.300876],[6.195261,7.107642,2.924304],[-8.282300,-0.603419,5.849337],[4.944277,-7.770643,-4.943683],[0.940740,2.307030,8.640757],[0.986053,3.635620,-4.811552],[0.746322,-1.224853,-9.090129],[-3.634051,3.789842,5.309780],[8.787938,0.306967,8.025148],[-7.243626,-7.684118,-9.200196],[-6.173345,0.871917,4.306240],[3.684562,-6.198327,3.166243],[1.997716,7.584865,-3.669788],[-4.195587,9.023789,-2.885778],[8.686144,-3.489796,-7.479242],[-4.841401,-9.269635,7.550311],[9.409027,5.063687,-0.283897],[3.266439,-8.762250,-5.885492],[6.887944,-6.862089,-1.720204],[0.905808,-3.612016,6.024015],[2.327448,3.768446,-8.762035],[2.047716,-9.937161,2.279826],[5.187834,-0.075463,0.898850],[-6.244618,3.556659,9.935784],[2.738396,-9.956059,-9.273875],[8.683254,8.268030,-6.171179],[7.926027,5.317158,-4.385555],[-4.438264,9.541513,1.484125],[1.889728,5.781880,6.623357],[-1.192548,-7.908143,-2.754001],[3.209468,-9.295834,-9.340442],[-1.867498,-4.964293,1.253485],[-1.853618,-5.289466,0.068110],[-6.528296,6.483696,9.127381],[-9.410499,-8.190610,-3.053909],[-0.146814,-7.556109,-0.453467],[4.465641,-0.413501,0.798642],[-3.961665,2.752890,6.721926],[-5.563254,0.636272,-2.804793],[-1.417186,-9.803390,3.705488],[1.784819,-4.906637,-8.704643],[1.686237,7.634934,1.513943],[2.011960,-8.313249,-2.729588],[4.821786,0.948829,-8.861934],[-4.705339,7.956373,4.612891],[2.488550,-3.643850,-7.908312],[9.854665,-6.008523,1.725037],[9.084363,8.768890,2.749730],[9.999213,-8.414354,6.041328],[-1.783401,-8.698643,4.412191],[-0.219914,-0.954696,-6.488568],[4.365239,-5.218352,7.946530],[2.746158,2.728079,-9.651452],[-0.205984,0.747871,6.254641],[-2.970902,-4.999495,0.786927],[-6.861510,8.185474,-2.884614],[-9.932242,6.472578,9.233619],[-7.079898,8.212449,2.242270],[2.238302,2.971759,-8.865744],[5.549886,2.044443,2.974453],[1.016148,-6.156872,1.369876],[7.351376,2.051081,-0.475764],[0.026081,9.678461,-5.921402],[-4.787226,2.361370,6.447317],[-4.698905,-2.176033,-6.410810],[-8.257608,2.032796,-2.888788],[6.682237,-1.339897,-2.626297],[2.298433,-9.239031,-4.372232],[9.390543,-2.776390,9.428710],[8.847395,-2.717366,8.515271],[6.278964,8.533622,-1.613693],[3.152597,7.020713,-9.496312],[4.649265,3.938815,6.209984],[-8.895240,-3.622084,2.066728],[-9.684472,-7.366102,-7.361432],[-7.487659,7.302166,-1.440764],[0.583347,-8.344107,-5.183490],[8.437290,-8.461998,8.987532],[-6.631715,6.630931,-8.193237],[-4.389081,8.148617,9.051744],[-4.482375,8.792951,3.374111],[-3.133928,-7.253306,1.555047],[7.257313,-3.542441,0.215107],[2.382894,1.717818,8.701076],[7.233325,1.809676,-8.462396],[-9.348695,-7.595799,-5.002005],[-5.834618,-2.252707,1.528670],[4.995745,-6.926542,9.708146],[2.914993,-9.148748,6.621136],[-1.391251,4.548124,2.665640],[-8.048510,5.635460,7.613793],[5.272145,-2.934434,-0.535218]], dtype = "float32")#candidate|7446|(715, 3)|const|float32
bop_7447 = relay.minimum(uop_7442.astype('int16'), relay.reshape(const_7446.astype('int16'), relay.shape_of(uop_7442))) # shape=(715, 3)
var_7450 = relay.var("var_7450", dtype = "float32", shape = (715, 3))#candidate|7450|(715, 3)|var|float32
bop_7451 = relay.right_shift(uop_7442.astype('int64'), relay.reshape(var_7450.astype('int64'), relay.shape_of(uop_7442))) # shape=(715, 3)
bop_7456 = relay.subtract(bop_7451.astype('uint64'), relay.reshape(var_7450.astype('uint64'), relay.shape_of(bop_7451))) # shape=(715, 3)
output = relay.Tuple([call_7420,call_7425,const_7426,call_7434,var_7435,bop_7447,bop_7456,])
output2 = relay.Tuple([call_7421,call_7428,const_7426,call_7436,var_7435,bop_7447,bop_7456,])
func_7459 = relay.Function([var_7435,var_7450,], output)
mod['func_7459'] = func_7459
mod = relay.transform.InferType()(mod)
mutated_mod['func_7459'] = func_7459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7459_call = mutated_mod.get_global_var('func_7459')
var_7461 = relay.var("var_7461", dtype = "float64", shape = (108,))#candidate|7461|(108,)|var|float64
var_7462 = relay.var("var_7462", dtype = "float32", shape = (715, 3))#candidate|7462|(715, 3)|var|float32
call_7460 = func_7459_call(var_7461,var_7462,)
output = call_7460
func_7463 = relay.Function([var_7461,var_7462,], output)
mutated_mod['func_7463'] = func_7463
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7491 = relay.var("var_7491", dtype = "float32", shape = (8, 2, 13))#candidate|7491|(8, 2, 13)|var|float32
uop_7492 = relay.acos(var_7491.astype('float32')) # shape=(8, 2, 13)
var_7494 = relay.var("var_7494", dtype = "float32", shape = (8, 2, 13))#candidate|7494|(8, 2, 13)|var|float32
bop_7495 = relay.not_equal(uop_7492.astype('bool'), relay.reshape(var_7494.astype('bool'), relay.shape_of(uop_7492))) # shape=(8, 2, 13)
uop_7503 = relay.exp(var_7491.astype('float64')) # shape=(8, 2, 13)
bop_7506 = relay.logical_xor(var_7491.astype('uint8'), relay.reshape(uop_7492.astype('uint8'), relay.shape_of(var_7491))) # shape=(8, 2, 13)
uop_7514 = relay.atanh(uop_7492.astype('float32')) # shape=(8, 2, 13)
output = relay.Tuple([bop_7495,uop_7503,bop_7506,uop_7514,])
output2 = relay.Tuple([bop_7495,uop_7503,bop_7506,uop_7514,])
func_7520 = relay.Function([var_7491,var_7494,], output)
mod['func_7520'] = func_7520
mod = relay.transform.InferType()(mod)
mutated_mod['func_7520'] = func_7520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7520_call = mutated_mod.get_global_var('func_7520')
var_7522 = relay.var("var_7522", dtype = "float32", shape = (8, 2, 13))#candidate|7522|(8, 2, 13)|var|float32
var_7523 = relay.var("var_7523", dtype = "float32", shape = (8, 2, 13))#candidate|7523|(8, 2, 13)|var|float32
call_7521 = func_7520_call(var_7522,var_7523,)
output = call_7521
func_7524 = relay.Function([var_7522,var_7523,], output)
mutated_mod['func_7524'] = func_7524
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3905_call = mod.get_global_var('func_3905')
func_3907_call = mutated_mod.get_global_var('func_3907')
call_7574 = func_3905_call()
call_7575 = func_3905_call()
output = relay.Tuple([call_7574,])
output2 = relay.Tuple([call_7575,])
func_7578 = relay.Function([], output)
mod['func_7578'] = func_7578
mod = relay.transform.InferType()(mod)
mutated_mod['func_7578'] = func_7578
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7578_call = mutated_mod.get_global_var('func_7578')
call_7579 = func_7578_call()
output = call_7579
func_7580 = relay.Function([], output)
mutated_mod['func_7580'] = func_7580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7281_call = mod.get_global_var('func_7281')
func_7282_call = mutated_mod.get_global_var('func_7282')
call_7604 = func_7281_call()
call_7605 = func_7281_call()
func_5404_call = mod.get_global_var('func_5404')
func_5405_call = mutated_mod.get_global_var('func_5405')
call_7609 = relay.TupleGetItem(func_5404_call(), 0)
call_7610 = relay.TupleGetItem(func_5405_call(), 0)
func_3468_call = mod.get_global_var('func_3468')
func_3471_call = mutated_mod.get_global_var('func_3471')
var_7633 = relay.var("var_7633", dtype = "float32", shape = (140,))#candidate|7633|(140,)|var|float32
call_7632 = relay.TupleGetItem(func_3468_call(relay.reshape(var_7633.astype('float32'), [2, 10, 7])), 5)
call_7634 = relay.TupleGetItem(func_3471_call(relay.reshape(var_7633.astype('float32'), [2, 10, 7])), 5)
func_6876_call = mod.get_global_var('func_6876')
func_6878_call = mutated_mod.get_global_var('func_6878')
call_7639 = relay.TupleGetItem(func_6876_call(), 0)
call_7640 = relay.TupleGetItem(func_6878_call(), 0)
output = relay.Tuple([call_7604,call_7609,call_7632,var_7633,call_7639,])
output2 = relay.Tuple([call_7605,call_7610,call_7634,var_7633,call_7640,])
func_7641 = relay.Function([var_7633,], output)
mod['func_7641'] = func_7641
mod = relay.transform.InferType()(mod)
var_7642 = relay.var("var_7642", dtype = "float32", shape = (140,))#candidate|7642|(140,)|var|float32
output = func_7641(var_7642)
func_7643 = relay.Function([var_7642], output)
mutated_mod['func_7643'] = func_7643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2256_call = mod.get_global_var('func_2256')
func_2258_call = mutated_mod.get_global_var('func_2258')
call_7682 = func_2256_call()
call_7683 = func_2256_call()
output = relay.Tuple([call_7682,])
output2 = relay.Tuple([call_7683,])
func_7696 = relay.Function([], output)
mod['func_7696'] = func_7696
mod = relay.transform.InferType()(mod)
output = func_7696()
func_7697 = relay.Function([], output)
mutated_mod['func_7697'] = func_7697
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7768 = relay.var("var_7768", dtype = "float32", shape = (7, 14, 6))#candidate|7768|(7, 14, 6)|var|float32
uop_7769 = relay.erf(var_7768.astype('float32')) # shape=(7, 14, 6)
bop_7772 = relay.floor_mod(var_7768.astype('float32'), relay.reshape(uop_7769.astype('float32'), relay.shape_of(var_7768))) # shape=(7, 14, 6)
output = relay.Tuple([bop_7772,])
output2 = relay.Tuple([bop_7772,])
func_7791 = relay.Function([var_7768,], output)
mod['func_7791'] = func_7791
mod = relay.transform.InferType()(mod)
mutated_mod['func_7791'] = func_7791
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7792 = relay.var("var_7792", dtype = "float32", shape = (7, 14, 6))#candidate|7792|(7, 14, 6)|var|float32
func_7791_call = mutated_mod.get_global_var('func_7791')
call_7793 = func_7791_call(var_7792)
output = call_7793
func_7794 = relay.Function([var_7792], output)
mutated_mod['func_7794'] = func_7794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4814_call = mod.get_global_var('func_4814')
func_4815_call = mutated_mod.get_global_var('func_4815')
call_7820 = relay.TupleGetItem(func_4814_call(), 1)
call_7821 = relay.TupleGetItem(func_4815_call(), 1)
output = relay.Tuple([call_7820,])
output2 = relay.Tuple([call_7821,])
func_7832 = relay.Function([], output)
mod['func_7832'] = func_7832
mod = relay.transform.InferType()(mod)
mutated_mod['func_7832'] = func_7832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7832_call = mutated_mod.get_global_var('func_7832')
call_7833 = func_7832_call()
output = call_7833
func_7834 = relay.Function([], output)
mutated_mod['func_7834'] = func_7834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5815_call = mod.get_global_var('func_5815')
func_5816_call = mutated_mod.get_global_var('func_5816')
call_7857 = relay.TupleGetItem(func_5815_call(), 0)
call_7858 = relay.TupleGetItem(func_5816_call(), 0)
var_7869 = relay.var("var_7869", dtype = "int32", shape = (990,))#candidate|7869|(990,)|var|int32
bop_7870 = relay.not_equal(call_7857.astype('bool'), relay.reshape(var_7869.astype('bool'), relay.shape_of(call_7857))) # shape=(990,)
bop_7873 = relay.not_equal(call_7858.astype('bool'), relay.reshape(var_7869.astype('bool'), relay.shape_of(call_7858))) # shape=(990,)
func_3538_call = mod.get_global_var('func_3538')
func_3540_call = mutated_mod.get_global_var('func_3540')
const_7878 = relay.const([-8.012241,-9.624244,-6.887417,-9.965060,1.254260,3.781171,3.348990,-8.347090,3.130655,-4.621073,-0.142340,6.311745,-6.428227,0.469059,8.100627,5.219600,-2.393038,5.900584,7.022412,-5.347818,-2.944360,7.982826,1.399129,5.476498,0.420566,5.380350,1.898990,-9.142270,7.299477,4.717390,-5.718126,-1.249288,-7.813700,-7.156109,-5.959420,-7.080622,-9.021713,-5.144302,3.758956,-6.098448,4.761579,-9.075270,9.784528,-2.166539,2.826295,3.054200,-3.465465,-7.690284,1.549393,-3.612641,4.150470,5.541826,-4.909506,3.983836,6.291801,-1.636091,0.652747,6.370923,7.355008,-6.447483,8.275652,7.439068,1.807024,3.348546,-6.095323,-4.765129,-3.559194,0.693424,2.405394,5.487167,7.706045,8.143105,-2.166298,6.239310,-9.339546,-5.581667,6.762896,2.263350,3.461839,5.114430,-5.513428,7.128750,2.464603,2.801474,1.728794,1.015704,-2.244129,-8.348534,9.764517,2.140928,7.113735,-6.036627,9.840814,2.157374,-8.751822,-3.923721,7.774023,1.172851,-5.814386,1.855649,5.491992,-1.822619,-9.980889,4.965124,-4.530084,8.198223,-6.671497,-9.209228], dtype = "float64")#candidate|7878|(108,)|const|float64
call_7877 = relay.TupleGetItem(func_3538_call(relay.reshape(const_7878.astype('float64'), [108,])), 3)
call_7879 = relay.TupleGetItem(func_3540_call(relay.reshape(const_7878.astype('float64'), [108,])), 3)
output = relay.Tuple([bop_7870,call_7877,const_7878,])
output2 = relay.Tuple([bop_7873,call_7879,const_7878,])
func_7881 = relay.Function([var_7869,], output)
mod['func_7881'] = func_7881
mod = relay.transform.InferType()(mod)
mutated_mod['func_7881'] = func_7881
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7882 = relay.var("var_7882", dtype = "int32", shape = (990,))#candidate|7882|(990,)|var|int32
func_7881_call = mutated_mod.get_global_var('func_7881')
call_7883 = func_7881_call(var_7882)
output = call_7883
func_7884 = relay.Function([var_7882], output)
mutated_mod['func_7884'] = func_7884
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2801_call = mod.get_global_var('func_2801')
func_2803_call = mutated_mod.get_global_var('func_2803')
call_7916 = relay.TupleGetItem(func_2801_call(), 1)
call_7917 = relay.TupleGetItem(func_2803_call(), 1)
output = call_7916
output2 = call_7917
func_7924 = relay.Function([], output)
mod['func_7924'] = func_7924
mod = relay.transform.InferType()(mod)
mutated_mod['func_7924'] = func_7924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7924_call = mutated_mod.get_global_var('func_7924')
call_7925 = func_7924_call()
output = call_7925
func_7926 = relay.Function([], output)
mutated_mod['func_7926'] = func_7926
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7978 = relay.var("var_7978", dtype = "float64", shape = ())#candidate|7978|()|var|float64
const_7979 = relay.const([[[-9.845999,-9.737931],[4.843383,-5.528736],[-2.095537,3.042301],[-3.728924,-9.100013],[2.377312,-3.361961]],[[1.028737,9.411163],[-6.519312,-8.366078],[-5.229656,-7.709363],[4.203701,-3.863345],[7.897237,-8.675277]],[[-9.120410,0.100186],[0.109387,4.290463],[-2.751841,-0.453790],[-1.387255,2.408667],[0.518330,-9.908073]],[[0.517674,-9.208316],[6.465890,-6.230345],[-0.812089,-9.124798],[-1.618260,5.124968],[2.546426,-0.015876]],[[7.911221,-7.068119],[-9.570076,-7.320271],[1.383456,6.762040],[-8.841311,2.299324],[-4.384734,-5.442787]],[[-8.880200,-2.975095],[-4.132936,-8.162099],[-3.898150,1.873468],[2.990205,4.640508],[-5.742329,3.550317]],[[-8.879731,-9.229937],[4.945924,1.276803],[4.163015,-6.454565],[-7.404691,-7.477780],[-3.604267,1.549242]],[[3.988383,-3.183849],[-6.184849,4.361125],[-2.721816,-0.672046],[3.788838,5.602929],[-8.116798,6.614437]],[[-5.452113,8.873820],[-6.920085,4.329435],[-5.361452,4.822183],[-2.190780,-1.032011],[7.045722,7.706052]],[[7.803110,1.424080],[-4.754120,7.477496],[3.590573,4.735674],[-4.630957,-1.968823],[-4.965805,7.621475]],[[-6.691626,9.201292],[3.366155,3.635465],[5.051195,-0.061122],[-4.386304,9.645312],[-1.929113,7.531798]],[[8.791802,6.520034],[2.495970,-8.646997],[8.033927,-7.803862],[-9.415074,-9.694754],[-8.840608,6.654627]],[[-6.399768,-7.514098],[9.522331,-8.549903],[-0.559190,8.243989],[-0.736521,4.786417],[-7.745982,1.381749]],[[7.404982,-3.527829],[2.248114,8.666631],[-4.196659,8.608726],[-2.925094,-4.093513],[-6.537412,0.266141]]], dtype = "float64")#candidate|7979|(14, 5, 2)|const|float64
bop_7980 = relay.floor_mod(var_7978.astype('float64'), const_7979.astype('float64')) # shape=(14, 5, 2)
output = bop_7980
output2 = bop_7980
func_7995 = relay.Function([var_7978,], output)
mod['func_7995'] = func_7995
mod = relay.transform.InferType()(mod)
var_7996 = relay.var("var_7996", dtype = "float64", shape = ())#candidate|7996|()|var|float64
output = func_7995(var_7996)
func_7997 = relay.Function([var_7996], output)
mutated_mod['func_7997'] = func_7997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6966_call = mod.get_global_var('func_6966')
func_6968_call = mutated_mod.get_global_var('func_6968')
call_8082 = func_6966_call()
call_8083 = func_6966_call()
output = relay.Tuple([call_8082,])
output2 = relay.Tuple([call_8083,])
func_8110 = relay.Function([], output)
mod['func_8110'] = func_8110
mod = relay.transform.InferType()(mod)
output = func_8110()
func_8111 = relay.Function([], output)
mutated_mod['func_8111'] = func_8111
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5092_call = mod.get_global_var('func_5092')
func_5094_call = mutated_mod.get_global_var('func_5094')
call_8136 = relay.TupleGetItem(func_5092_call(), 0)
call_8137 = relay.TupleGetItem(func_5094_call(), 0)
func_3142_call = mod.get_global_var('func_3142')
func_3146_call = mutated_mod.get_global_var('func_3146')
const_8143 = relay.const([-6.828875,3.966944,2.804542,-0.456012,-7.102016,-8.754402,-2.680550,-3.773763,9.984971,0.289674,-8.457293,-5.925983,1.840788,-2.457395,2.943162,8.799930,-0.556487,8.604713,4.240531,-5.768120,0.762598,-1.695783,2.970400,-8.429403,-3.471095,5.527443,-8.356214,-8.845389,-5.418135,-6.874523,9.882919,0.739725,-3.362176,1.585619,-9.026137,-0.853095,-6.924297,-8.326941,6.062716,-9.312349], dtype = "float32")#candidate|8143|(40,)|const|float32
var_8144 = relay.var("var_8144", dtype = "float32", shape = (320,))#candidate|8144|(320,)|var|float32
call_8142 = relay.TupleGetItem(func_3142_call(relay.reshape(const_8143.astype('float32'), [1, 4, 10]), relay.reshape(var_8144.astype('float32'), [8, 4, 10]), ), 0)
call_8145 = relay.TupleGetItem(func_3146_call(relay.reshape(const_8143.astype('float32'), [1, 4, 10]), relay.reshape(var_8144.astype('float32'), [8, 4, 10]), ), 0)
func_2301_call = mod.get_global_var('func_2301')
func_2303_call = mutated_mod.get_global_var('func_2303')
var_8154 = relay.var("var_8154", dtype = "uint32", shape = (90,))#candidate|8154|(90,)|var|uint32
call_8153 = relay.TupleGetItem(func_2301_call(relay.reshape(var_8154.astype('uint32'), [9, 5, 2])), 0)
call_8155 = relay.TupleGetItem(func_2303_call(relay.reshape(var_8154.astype('uint32'), [9, 5, 2])), 0)
func_2723_call = mod.get_global_var('func_2723')
func_2725_call = mutated_mod.get_global_var('func_2725')
call_8156 = func_2723_call()
call_8157 = func_2723_call()
func_6822_call = mod.get_global_var('func_6822')
func_6823_call = mutated_mod.get_global_var('func_6823')
call_8158 = relay.TupleGetItem(func_6822_call(), 1)
call_8159 = relay.TupleGetItem(func_6823_call(), 1)
output = relay.Tuple([call_8136,call_8142,const_8143,var_8144,call_8153,var_8154,call_8156,call_8158,])
output2 = relay.Tuple([call_8137,call_8145,const_8143,var_8144,call_8155,var_8154,call_8157,call_8159,])
func_8163 = relay.Function([var_8144,var_8154,], output)
mod['func_8163'] = func_8163
mod = relay.transform.InferType()(mod)
mutated_mod['func_8163'] = func_8163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8163_call = mutated_mod.get_global_var('func_8163')
var_8165 = relay.var("var_8165", dtype = "float32", shape = (320,))#candidate|8165|(320,)|var|float32
var_8166 = relay.var("var_8166", dtype = "uint32", shape = (90,))#candidate|8166|(90,)|var|uint32
call_8164 = func_8163_call(var_8165,var_8166,)
output = call_8164
func_8167 = relay.Function([var_8165,var_8166,], output)
mutated_mod['func_8167'] = func_8167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3905_call = mod.get_global_var('func_3905')
func_3907_call = mutated_mod.get_global_var('func_3907')
call_8175 = func_3905_call()
call_8176 = func_3905_call()
output = relay.Tuple([call_8175,])
output2 = relay.Tuple([call_8176,])
func_8188 = relay.Function([], output)
mod['func_8188'] = func_8188
mod = relay.transform.InferType()(mod)
mutated_mod['func_8188'] = func_8188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8188_call = mutated_mod.get_global_var('func_8188')
call_8189 = func_8188_call()
output = call_8189
func_8190 = relay.Function([], output)
mutated_mod['func_8190'] = func_8190
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8200 = relay.const([[[0.079082,3.747059,-6.953096,-4.349631,-2.412635,-9.621091,0.972063,-6.612484,5.062235,2.255783,3.090059,-1.000563,-6.274352,3.655927,-0.955250,1.765046],[-2.406877,-8.558688,-7.096230,6.138523,-4.524984,-3.529903,8.196285,7.190918,4.068710,-6.523002,-9.723245,9.771629,4.536610,-5.158937,-6.487643,7.900158],[-9.654665,2.273060,-7.027853,8.540920,6.969186,8.065989,-6.947878,2.609173,9.162700,-5.664046,-3.803886,-2.398230,9.491716,-8.774175,-0.293442,-1.301238],[5.300921,-1.368533,-2.449478,-7.761075,4.578094,-0.529357,-7.096833,7.215789,8.206218,-7.182564,-8.529287,7.259218,1.044199,5.780084,1.351334,-0.472161],[5.712452,2.087225,-4.826831,7.849731,9.458580,-4.458965,-4.023324,9.527633,9.467728,0.031368,-9.431615,8.691244,-0.367506,4.548121,2.694630,-3.987368],[-2.988566,-6.769406,2.334628,9.924765,-4.590994,9.187593,8.271020,-6.177497,-4.186043,-7.803911,3.249195,-2.150607,-2.766543,0.952240,6.178266,9.586191],[2.470260,-6.619500,3.986885,4.510728,1.051321,-1.043408,8.356724,-8.696117,6.640675,-7.264070,-7.227352,-4.381262,3.787586,-2.653425,-6.345354,-5.351142],[-4.565881,-7.201414,-6.279848,2.147469,-0.045006,2.702774,-3.039747,8.801708,-0.094617,-6.879208,-2.792743,-8.078353,8.646967,-5.539132,-3.408152,3.870250],[-9.050254,-7.024979,-2.551813,-0.492150,-9.764584,-8.790467,1.486750,-7.413384,-6.108776,4.622096,3.913834,-8.786388,-4.309510,-9.862327,0.557467,0.462952],[-9.874255,8.369501,3.570361,0.325619,5.899229,0.012814,-8.866220,-2.867175,-2.020482,8.101759,7.373291,-4.648094,9.672996,-9.314260,5.664325,-2.522356],[-2.820260,-3.059613,7.765503,8.914962,9.326696,-7.390589,-2.700776,-1.372483,-8.275845,-0.300327,1.224799,3.707596,-1.119281,-6.974444,-0.413320,7.992666],[-8.434749,-9.272453,1.612688,-9.981055,-5.287598,-4.579367,4.650241,-6.225952,0.894119,-2.623743,8.699564,1.427688,5.328130,9.212700,-7.483849,-7.243761],[-3.878273,-0.349101,-5.127312,0.913599,4.256422,6.758252,-1.694869,-2.395371,7.505876,0.821785,3.321137,-4.848347,-7.510330,-2.994029,-1.985603,0.351014],[1.140315,-9.591843,-2.450880,6.758651,-0.582209,-4.480473,-1.320946,-3.979028,2.894507,-6.408981,-4.762729,-7.697380,8.401935,6.273895,8.569000,-2.553297],[-2.998631,1.976638,-6.057058,5.701075,8.746470,-2.467614,-1.553850,6.958073,-9.483336,-8.728329,-6.038785,7.278282,7.756691,1.248361,7.874686,-9.339945],[9.038008,-4.808191,-9.863287,-8.638438,5.405753,3.276260,5.509628,-8.767982,-7.177441,-5.365964,2.422494,-8.764080,-6.272884,6.516179,-1.616128,0.264565]]], dtype = "float32")#candidate|8200|(1, 16, 16)|const|float32
var_8201 = relay.var("var_8201", dtype = "float32", shape = (5, 16, 16))#candidate|8201|(5, 16, 16)|var|float32
bop_8202 = relay.floor_divide(const_8200.astype('float32'), var_8201.astype('float32')) # shape=(5, 16, 16)
output = relay.Tuple([bop_8202,])
output2 = relay.Tuple([bop_8202,])
func_8205 = relay.Function([var_8201,], output)
mod['func_8205'] = func_8205
mod = relay.transform.InferType()(mod)
mutated_mod['func_8205'] = func_8205
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8206 = relay.var("var_8206", dtype = "float32", shape = (5, 16, 16))#candidate|8206|(5, 16, 16)|var|float32
func_8205_call = mutated_mod.get_global_var('func_8205')
call_8207 = func_8205_call(var_8206)
output = call_8207
func_8208 = relay.Function([var_8206], output)
mutated_mod['func_8208'] = func_8208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5694_call = mod.get_global_var('func_5694')
func_5696_call = mutated_mod.get_global_var('func_5696')
call_8216 = func_5694_call()
call_8217 = func_5694_call()
output = relay.Tuple([call_8216,])
output2 = relay.Tuple([call_8217,])
func_8224 = relay.Function([], output)
mod['func_8224'] = func_8224
mod = relay.transform.InferType()(mod)
output = func_8224()
func_8225 = relay.Function([], output)
mutated_mod['func_8225'] = func_8225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3114_call = mod.get_global_var('func_3114')
func_3115_call = mutated_mod.get_global_var('func_3115')
call_8258 = relay.TupleGetItem(func_3114_call(), 0)
call_8259 = relay.TupleGetItem(func_3115_call(), 0)
uop_8289 = relay.rsqrt(call_8258.astype('float32')) # shape=(990,)
uop_8291 = relay.rsqrt(call_8259.astype('float32')) # shape=(990,)
output = relay.Tuple([uop_8289,])
output2 = relay.Tuple([uop_8291,])
func_8293 = relay.Function([], output)
mod['func_8293'] = func_8293
mod = relay.transform.InferType()(mod)
output = func_8293()
func_8294 = relay.Function([], output)
mutated_mod['func_8294'] = func_8294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6758_call = mod.get_global_var('func_6758')
func_6759_call = mutated_mod.get_global_var('func_6759')
call_8295 = relay.TupleGetItem(func_6758_call(), 1)
call_8296 = relay.TupleGetItem(func_6759_call(), 1)
var_8328 = relay.var("var_8328", dtype = "float64", shape = (8, 3, 10))#candidate|8328|(8, 3, 10)|var|float64
bop_8329 = relay.left_shift(call_8295.astype('uint16'), relay.reshape(var_8328.astype('uint16'), relay.shape_of(call_8295))) # shape=(8, 3, 10)
bop_8332 = relay.left_shift(call_8296.astype('uint16'), relay.reshape(var_8328.astype('uint16'), relay.shape_of(call_8296))) # shape=(8, 3, 10)
output = relay.Tuple([bop_8329,])
output2 = relay.Tuple([bop_8332,])
func_8335 = relay.Function([var_8328,], output)
mod['func_8335'] = func_8335
mod = relay.transform.InferType()(mod)
mutated_mod['func_8335'] = func_8335
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8336 = relay.var("var_8336", dtype = "float64", shape = (8, 3, 10))#candidate|8336|(8, 3, 10)|var|float64
func_8335_call = mutated_mod.get_global_var('func_8335')
call_8337 = func_8335_call(var_8336)
output = call_8337
func_8338 = relay.Function([var_8336], output)
mutated_mod['func_8338'] = func_8338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5741_call = mod.get_global_var('func_5741')
func_5742_call = mutated_mod.get_global_var('func_5742')
call_8401 = relay.TupleGetItem(func_5741_call(), 0)
call_8402 = relay.TupleGetItem(func_5742_call(), 0)
func_3793_call = mod.get_global_var('func_3793')
func_3796_call = mutated_mod.get_global_var('func_3796')
var_8427 = relay.var("var_8427", dtype = "float32", shape = (240,))#candidate|8427|(240,)|var|float32
call_8426 = func_3793_call(relay.reshape(var_8427.astype('float32'), [8, 3, 10]))
call_8428 = func_3793_call(relay.reshape(var_8427.astype('float32'), [8, 3, 10]))
func_4841_call = mod.get_global_var('func_4841')
func_4843_call = mutated_mod.get_global_var('func_4843')
call_8430 = func_4841_call()
call_8431 = func_4841_call()
func_3177_call = mod.get_global_var('func_3177')
func_3178_call = mutated_mod.get_global_var('func_3178')
call_8435 = relay.TupleGetItem(func_3177_call(), 0)
call_8436 = relay.TupleGetItem(func_3178_call(), 0)
output = relay.Tuple([call_8401,call_8426,var_8427,call_8430,call_8435,])
output2 = relay.Tuple([call_8402,call_8428,var_8427,call_8431,call_8436,])
func_8449 = relay.Function([var_8427,], output)
mod['func_8449'] = func_8449
mod = relay.transform.InferType()(mod)
var_8450 = relay.var("var_8450", dtype = "float32", shape = (240,))#candidate|8450|(240,)|var|float32
output = func_8449(var_8450)
func_8451 = relay.Function([var_8450], output)
mutated_mod['func_8451'] = func_8451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5664_call = mod.get_global_var('func_5664')
func_5666_call = mutated_mod.get_global_var('func_5666')
call_8463 = relay.TupleGetItem(func_5664_call(), 0)
call_8464 = relay.TupleGetItem(func_5666_call(), 0)
output = call_8463
output2 = call_8464
func_8475 = relay.Function([], output)
mod['func_8475'] = func_8475
mod = relay.transform.InferType()(mod)
output = func_8475()
func_8476 = relay.Function([], output)
mutated_mod['func_8476'] = func_8476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1596_call = mod.get_global_var('func_1596')
func_1597_call = mutated_mod.get_global_var('func_1597')
call_8487 = func_1596_call()
call_8488 = func_1596_call()
func_5112_call = mod.get_global_var('func_5112')
func_5114_call = mutated_mod.get_global_var('func_5114')
var_8491 = relay.var("var_8491", dtype = "float32", shape = (126,))#candidate|8491|(126,)|var|float32
call_8490 = relay.TupleGetItem(func_5112_call(relay.reshape(var_8491.astype('float32'), [7, 2, 9])), 0)
call_8492 = relay.TupleGetItem(func_5114_call(relay.reshape(var_8491.astype('float32'), [7, 2, 9])), 0)
var_8503 = relay.var("var_8503", dtype = "float64", shape = (8, 3, 10))#candidate|8503|(8, 3, 10)|var|float64
bop_8504 = relay.not_equal(call_8487.astype('bool'), relay.reshape(var_8503.astype('bool'), relay.shape_of(call_8487))) # shape=(8, 3, 10)
bop_8507 = relay.not_equal(call_8488.astype('bool'), relay.reshape(var_8503.astype('bool'), relay.shape_of(call_8488))) # shape=(8, 3, 10)
func_4214_call = mod.get_global_var('func_4214')
func_4215_call = mutated_mod.get_global_var('func_4215')
call_8510 = relay.TupleGetItem(func_4214_call(), 1)
call_8511 = relay.TupleGetItem(func_4215_call(), 1)
func_5250_call = mod.get_global_var('func_5250')
func_5251_call = mutated_mod.get_global_var('func_5251')
call_8515 = relay.TupleGetItem(func_5250_call(), 1)
call_8516 = relay.TupleGetItem(func_5251_call(), 1)
bop_8519 = relay.logical_xor(call_8490.astype('uint32'), call_8510.astype('uint32')) # shape=(7, 2, 9)
bop_8522 = relay.logical_xor(call_8492.astype('uint32'), call_8511.astype('uint32')) # shape=(7, 2, 9)
output = relay.Tuple([var_8491,bop_8504,call_8515,bop_8519,])
output2 = relay.Tuple([var_8491,bop_8507,call_8516,bop_8522,])
func_8524 = relay.Function([var_8491,var_8503,], output)
mod['func_8524'] = func_8524
mod = relay.transform.InferType()(mod)
var_8525 = relay.var("var_8525", dtype = "float32", shape = (126,))#candidate|8525|(126,)|var|float32
var_8526 = relay.var("var_8526", dtype = "float64", shape = (8, 3, 10))#candidate|8526|(8, 3, 10)|var|float64
output = func_8524(var_8525,var_8526,)
func_8527 = relay.Function([var_8525,var_8526,], output)
mutated_mod['func_8527'] = func_8527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3642_call = mod.get_global_var('func_3642')
func_3643_call = mutated_mod.get_global_var('func_3643')
call_8542 = relay.TupleGetItem(func_3642_call(), 0)
call_8543 = relay.TupleGetItem(func_3643_call(), 0)
output = relay.Tuple([call_8542,])
output2 = relay.Tuple([call_8543,])
func_8548 = relay.Function([], output)
mod['func_8548'] = func_8548
mod = relay.transform.InferType()(mod)
mutated_mod['func_8548'] = func_8548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8548_call = mutated_mod.get_global_var('func_8548')
call_8549 = func_8548_call()
output = call_8549
func_8550 = relay.Function([], output)
mutated_mod['func_8550'] = func_8550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3334_call = mod.get_global_var('func_3334')
func_3335_call = mutated_mod.get_global_var('func_3335')
call_8593 = relay.TupleGetItem(func_3334_call(), 1)
call_8594 = relay.TupleGetItem(func_3335_call(), 1)
output = relay.Tuple([call_8593,])
output2 = relay.Tuple([call_8594,])
func_8610 = relay.Function([], output)
mod['func_8610'] = func_8610
mod = relay.transform.InferType()(mod)
output = func_8610()
func_8611 = relay.Function([], output)
mutated_mod['func_8611'] = func_8611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7174_call = mod.get_global_var('func_7174')
func_7176_call = mutated_mod.get_global_var('func_7176')
call_8652 = relay.TupleGetItem(func_7174_call(), 0)
call_8653 = relay.TupleGetItem(func_7176_call(), 0)
func_8475_call = mod.get_global_var('func_8475')
func_8476_call = mutated_mod.get_global_var('func_8476')
call_8658 = func_8475_call()
call_8659 = func_8475_call()
output = relay.Tuple([call_8652,call_8658,])
output2 = relay.Tuple([call_8653,call_8659,])
func_8666 = relay.Function([], output)
mod['func_8666'] = func_8666
mod = relay.transform.InferType()(mod)
mutated_mod['func_8666'] = func_8666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8666_call = mutated_mod.get_global_var('func_8666')
call_8667 = func_8666_call()
output = call_8667
func_8668 = relay.Function([], output)
mutated_mod['func_8668'] = func_8668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8188_call = mod.get_global_var('func_8188')
func_8190_call = mutated_mod.get_global_var('func_8190')
call_8672 = relay.TupleGetItem(func_8188_call(), 0)
call_8673 = relay.TupleGetItem(func_8190_call(), 0)
output = relay.Tuple([call_8672,])
output2 = relay.Tuple([call_8673,])
func_8677 = relay.Function([], output)
mod['func_8677'] = func_8677
mod = relay.transform.InferType()(mod)
output = func_8677()
func_8678 = relay.Function([], output)
mutated_mod['func_8678'] = func_8678
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8691 = relay.var("var_8691", dtype = "float64", shape = (15, 1, 12))#candidate|8691|(15, 1, 12)|var|float64
uop_8692 = relay.sqrt(var_8691.astype('float64')) # shape=(15, 1, 12)
output = relay.Tuple([uop_8692,])
output2 = relay.Tuple([uop_8692,])
F = relay.Function([var_8691,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_8691,], output2)
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
