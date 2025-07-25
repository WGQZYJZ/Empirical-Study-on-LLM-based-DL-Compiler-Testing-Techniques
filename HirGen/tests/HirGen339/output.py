import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_21 = relay.const([[[True,True,False,True,True,True,True,False,True,True,False,True,False],[True,True,True,True,False,False,False,False,False,False,False,True,False],[False,False,True,False,True,True,True,True,False,False,True,True,True],[False,True,True,True,True,False,True,False,False,True,True,False,True],[True,True,False,False,True,False,False,True,False,True,False,True,True],[False,False,False,True,True,False,False,False,False,True,True,True,False],[True,False,True,True,False,False,False,False,False,False,False,False,True],[False,False,True,True,True,True,True,True,False,False,True,True,True],[True,False,False,False,False,True,True,True,False,True,True,True,True],[True,True,True,False,False,True,False,True,False,True,False,False,False],[False,False,True,True,True,True,False,True,True,False,False,False,False],[True,True,True,False,False,True,True,True,True,True,False,True,False]],[[True,False,False,True,False,False,True,True,False,True,False,False,False],[False,False,True,False,False,False,False,False,False,False,True,True,False],[False,False,False,True,False,True,True,False,False,True,False,False,False],[False,True,True,False,True,True,True,False,True,True,False,True,True],[False,False,False,True,False,False,True,False,True,True,False,False,True],[False,True,False,False,False,False,True,True,True,True,False,False,True],[True,True,False,True,True,False,True,True,False,True,False,True,True],[True,True,True,False,False,False,True,False,False,True,True,False,False],[False,True,False,False,False,False,True,False,True,False,True,False,False],[True,True,False,False,False,True,True,False,True,False,False,True,False],[False,False,True,False,True,True,True,True,True,False,True,True,False],[False,True,True,False,True,False,True,True,True,False,True,False,False]]], dtype = "bool")#candidate|21|(2, 12, 13)|const|bool
var_22 = relay.var("var_22", dtype = "bool", shape = (2, 12, 13))#candidate|22|(2, 12, 13)|var|bool
bop_23 = relay.logical_and(const_21.astype('bool'), relay.reshape(var_22.astype('bool'), relay.shape_of(const_21))) # shape=(2, 12, 13)
output = bop_23
output2 = bop_23
func_29 = relay.Function([var_22,], output)
mod['func_29'] = func_29
mod = relay.transform.InferType()(mod)
mutated_mod['func_29'] = func_29
mutated_mod = relay.transform.InferType()(mutated_mod)
var_30 = relay.var("var_30", dtype = "bool", shape = (2, 12, 13))#candidate|30|(2, 12, 13)|var|bool
func_29_call = mutated_mod.get_global_var('func_29')
call_31 = func_29_call(var_30)
output = call_31
func_32 = relay.Function([var_30], output)
mutated_mod['func_32'] = func_32
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1081 = relay.var("var_1081", dtype = "float32", shape = (10, 1, 16))#candidate|1081|(10, 1, 16)|var|float32
uop_1082 = relay.sigmoid(var_1081.astype('float32')) # shape=(10, 1, 16)
func_29_call = mod.get_global_var('func_29')
func_32_call = mutated_mod.get_global_var('func_32')
const_1088 = relay.const([True,False,True,False,True,False,False,False,True,True,False,False,True,True,False,True,True,False,True,False,True,False,False,True,False,True,False,False,True,True,True,True,True,False,True,False,False,False,False,True,True,False,True,False,True,False,True,True,False,True,True,True,True,False,False,True,True,False,True,False,True,False,True,False,True,True,False,True,True,True,True,False,True,False,False,True,False,True,False,False,False,True,True,True,True,True,False,False,False,True,True,True,False,False,False,True,True,False,False,False,True,True,False,True,False,False,False,False,False,False,True,False,True,False,False,True,False,False,True,False,False,False,True,False,True,True,True,False,False,True,True,True,True,True,False,True,False,False,True,False,False,False,False,False,True,False,True,True,True,False,True,True,True,False,True,False,False,False,False,False,True,True,True,False,True,False,True,True,False,True,True,True,True,True,True,False,False,False,True,True,False,False,False,True,True,True,True,True,True,False,True,False,True,False,True,False,False,False,True,True,True,False,False,True,False,True,True,False,True,True,True,True,True,True,True,False,False,False,True,True,False,False,True,False,True,False,False,True,True,False,False,False,False,False,True,False,True,True,False,False,False,True,False,True,False,True,False,False,True,True,True,False,False,True,False,True,True,False,False,False,False,True,True,True,True,False,True,True,True,False,True,True,True,True,True,False,False,True,False,False,False,False,False,False,True,False,True,False,False,False,True,True,True,False,False,False,False,True,True,False,True,True,True,True,False,False,True,True,True,True,True,False], dtype = "bool")#candidate|1088|(312,)|const|bool
call_1087 = func_29_call(relay.reshape(const_1088.astype('bool'), [2, 12, 13]))
call_1089 = func_29_call(relay.reshape(const_1088.astype('bool'), [2, 12, 13]))
output = relay.Tuple([uop_1082,call_1087,const_1088,])
output2 = relay.Tuple([uop_1082,call_1089,const_1088,])
func_1109 = relay.Function([var_1081,], output)
mod['func_1109'] = func_1109
mod = relay.transform.InferType()(mod)
mutated_mod['func_1109'] = func_1109
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1110 = relay.var("var_1110", dtype = "float32", shape = (10, 1, 16))#candidate|1110|(10, 1, 16)|var|float32
func_1109_call = mutated_mod.get_global_var('func_1109')
call_1111 = func_1109_call(var_1110)
output = call_1111
func_1112 = relay.Function([var_1110], output)
mutated_mod['func_1112'] = func_1112
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1365 = relay.var("var_1365", dtype = "float32", shape = (11, 12, 4))#candidate|1365|(11, 12, 4)|var|float32
var_1366 = relay.var("var_1366", dtype = "float32", shape = (11, 12, 4))#candidate|1366|(11, 12, 4)|var|float32
bop_1367 = relay.power(var_1365.astype('float32'), relay.reshape(var_1366.astype('float32'), relay.shape_of(var_1365))) # shape=(11, 12, 4)
func_29_call = mod.get_global_var('func_29')
func_32_call = mutated_mod.get_global_var('func_32')
var_1373 = relay.var("var_1373", dtype = "bool", shape = (312,))#candidate|1373|(312,)|var|bool
call_1372 = func_29_call(relay.reshape(var_1373.astype('bool'), [2, 12, 13]))
call_1374 = func_29_call(relay.reshape(var_1373.astype('bool'), [2, 12, 13]))
output = relay.Tuple([bop_1367,call_1372,var_1373,])
output2 = relay.Tuple([bop_1367,call_1374,var_1373,])
func_1376 = relay.Function([var_1365,var_1366,var_1373,], output)
mod['func_1376'] = func_1376
mod = relay.transform.InferType()(mod)
var_1377 = relay.var("var_1377", dtype = "float32", shape = (11, 12, 4))#candidate|1377|(11, 12, 4)|var|float32
var_1378 = relay.var("var_1378", dtype = "float32", shape = (11, 12, 4))#candidate|1378|(11, 12, 4)|var|float32
var_1379 = relay.var("var_1379", dtype = "bool", shape = (312,))#candidate|1379|(312,)|var|bool
output = func_1376(var_1377,var_1378,var_1379,)
func_1380 = relay.Function([var_1377,var_1378,var_1379,], output)
mutated_mod['func_1380'] = func_1380
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1565 = relay.const([[[-8.243827,-7.220974,-8.631659,-5.372780,7.589231,-7.420432,-2.455323,3.177860,-2.972666,0.991375],[4.195482,3.143089,9.730346,4.592050,-7.799488,-2.508343,8.799628,3.114657,-6.774454,7.158166]],[[7.616460,9.477143,-6.435329,-1.709344,-4.843049,1.059818,0.884749,3.415484,-4.508755,1.743414],[4.389112,7.469406,-9.579452,2.315252,5.036228,4.516379,-7.472033,-5.279354,4.748541,-0.468028]]], dtype = "float32")#candidate|1565|(2, 2, 10)|const|float32
uop_1566 = relay.log2(const_1565.astype('float32')) # shape=(2, 2, 10)
var_1568 = relay.var("var_1568", dtype = "float32", shape = (2, 2, 10))#candidate|1568|(2, 2, 10)|var|float32
bop_1569 = relay.mod(uop_1566.astype('float32'), relay.reshape(var_1568.astype('float32'), relay.shape_of(uop_1566))) # shape=(2, 2, 10)
output = bop_1569
output2 = bop_1569
func_1576 = relay.Function([var_1568,], output)
mod['func_1576'] = func_1576
mod = relay.transform.InferType()(mod)
mutated_mod['func_1576'] = func_1576
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1577 = relay.var("var_1577", dtype = "float32", shape = (2, 2, 10))#candidate|1577|(2, 2, 10)|var|float32
func_1576_call = mutated_mod.get_global_var('func_1576')
call_1578 = func_1576_call(var_1577)
output = call_1578
func_1579 = relay.Function([var_1577], output)
mutated_mod['func_1579'] = func_1579
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2530 = relay.var("var_2530", dtype = "float64", shape = (16, 1, 7))#candidate|2530|(16, 1, 7)|var|float64
uop_2531 = relay.sigmoid(var_2530.astype('float64')) # shape=(16, 1, 7)
output = relay.Tuple([uop_2531,])
output2 = relay.Tuple([uop_2531,])
func_2536 = relay.Function([var_2530,], output)
mod['func_2536'] = func_2536
mod = relay.transform.InferType()(mod)
mutated_mod['func_2536'] = func_2536
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2537 = relay.var("var_2537", dtype = "float64", shape = (16, 1, 7))#candidate|2537|(16, 1, 7)|var|float64
func_2536_call = mutated_mod.get_global_var('func_2536')
call_2538 = func_2536_call(var_2537)
output = call_2538
func_2539 = relay.Function([var_2537], output)
mutated_mod['func_2539'] = func_2539
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2805 = relay.var("var_2805", dtype = "float32", shape = (10, 5, 9))#candidate|2805|(10, 5, 9)|var|float32
uop_2806 = relay.atanh(var_2805.astype('float32')) # shape=(10, 5, 9)
bop_2812 = relay.right_shift(var_2805.astype('uint64'), relay.reshape(uop_2806.astype('uint64'), relay.shape_of(var_2805))) # shape=(10, 5, 9)
func_1376_call = mod.get_global_var('func_1376')
func_1380_call = mutated_mod.get_global_var('func_1380')
var_2819 = relay.var("var_2819", dtype = "float32", shape = (528,))#candidate|2819|(528,)|var|float32
const_2820 = relay.const([[False,True,False,False,False,False,True,True,False,False,True,True,True,False,True,True,False,False,False,True,False,True,False,False,False,True,False,False,True,False,False,True,True,False,True,True,False,True,False,False,True,False,True,False,False,True,True,True,True,True,False,False],[False,True,False,True,False,True,True,False,True,True,True,False,True,True,True,False,False,True,False,True,True,False,False,False,True,True,True,False,True,True,False,True,False,True,False,True,False,True,True,True,False,False,True,False,True,False,False,True,True,False,True,True],[False,True,True,True,False,False,False,True,True,False,True,False,True,True,True,True,True,False,False,True,False,True,True,False,True,True,True,True,False,False,False,False,True,True,False,False,True,False,True,False,False,False,False,False,False,True,True,True,True,False,False,False],[True,False,False,True,True,True,False,True,False,False,False,True,True,False,True,False,False,True,False,False,True,True,False,True,False,False,False,False,False,True,False,True,True,False,False,False,True,False,False,True,False,False,True,True,False,False,True,False,True,False,False,True],[True,True,False,True,True,True,True,True,False,True,False,True,True,True,True,True,True,True,False,False,True,True,True,True,False,True,True,True,True,False,False,False,True,True,True,False,False,True,True,False,False,True,True,False,False,False,True,False,False,True,False,True],[True,True,True,True,False,False,False,True,False,True,True,True,False,True,True,False,False,False,False,False,False,True,False,False,True,True,False,True,True,False,True,False,False,False,True,False,False,True,False,True,False,True,False,False,False,False,False,False,False,False,True,False]], dtype = "bool")#candidate|2820|(6, 52)|const|bool
call_2818 = relay.TupleGetItem(func_1376_call(relay.reshape(var_2819.astype('float32'), [11, 12, 4]), relay.reshape(var_2819.astype('float32'), [11, 12, 4]), relay.reshape(const_2820.astype('bool'), [312,]), ), 1)
call_2821 = relay.TupleGetItem(func_1380_call(relay.reshape(var_2819.astype('float32'), [11, 12, 4]), relay.reshape(var_2819.astype('float32'), [11, 12, 4]), relay.reshape(const_2820.astype('bool'), [312,]), ), 1)
func_1576_call = mod.get_global_var('func_1576')
func_1579_call = mutated_mod.get_global_var('func_1579')
const_2827 = relay.const([3.290413,-4.542941,1.722852,4.755848,6.300505,0.775506,1.007020,-9.023341,-4.624310,-2.875362,3.311349,-1.249100,-9.025809,6.117037,-6.697798,-0.249798,4.423578,-1.953536,9.940486,-3.222177,-4.059642,2.637174,0.585263,0.160013,-7.121933,-0.550448,6.381294,-7.932580,4.573429,5.047107,2.650496,3.002188,-6.658062,6.932759,-4.226680,-8.321739,-7.397053,-5.473912,-2.019088,6.623907], dtype = "float32")#candidate|2827|(40,)|const|float32
call_2826 = func_1576_call(relay.reshape(const_2827.astype('float32'), [2, 2, 10]))
call_2828 = func_1576_call(relay.reshape(const_2827.astype('float32'), [2, 2, 10]))
uop_2830 = relay.asinh(bop_2812.astype('float64')) # shape=(10, 5, 9)
var_2835 = relay.var("var_2835", dtype = "float32", shape = (10, 5, 9))#candidate|2835|(10, 5, 9)|var|float32
bop_2836 = relay.power(uop_2806.astype('float64'), relay.reshape(var_2835.astype('float64'), relay.shape_of(uop_2806))) # shape=(10, 5, 9)
output = relay.Tuple([call_2818,var_2819,const_2820,call_2826,const_2827,uop_2830,bop_2836,])
output2 = relay.Tuple([call_2821,var_2819,const_2820,call_2828,const_2827,uop_2830,bop_2836,])
func_2842 = relay.Function([var_2805,var_2819,var_2835,], output)
mod['func_2842'] = func_2842
mod = relay.transform.InferType()(mod)
mutated_mod['func_2842'] = func_2842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2842_call = mutated_mod.get_global_var('func_2842')
var_2844 = relay.var("var_2844", dtype = "float32", shape = (10, 5, 9))#candidate|2844|(10, 5, 9)|var|float32
var_2845 = relay.var("var_2845", dtype = "float32", shape = (528,))#candidate|2845|(528,)|var|float32
var_2846 = relay.var("var_2846", dtype = "float32", shape = (10, 5, 9))#candidate|2846|(10, 5, 9)|var|float32
call_2843 = func_2842_call(var_2844,var_2845,var_2846,)
output = call_2843
func_2847 = relay.Function([var_2844,var_2845,var_2846,], output)
mutated_mod['func_2847'] = func_2847
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3104 = relay.var("var_3104", dtype = "float64", shape = (1, 2, 11))#candidate|3104|(1, 2, 11)|var|float64
uop_3105 = relay.cos(var_3104.astype('float64')) # shape=(1, 2, 11)
output = relay.Tuple([uop_3105,])
output2 = relay.Tuple([uop_3105,])
func_3115 = relay.Function([var_3104,], output)
mod['func_3115'] = func_3115
mod = relay.transform.InferType()(mod)
mutated_mod['func_3115'] = func_3115
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3116 = relay.var("var_3116", dtype = "float64", shape = (1, 2, 11))#candidate|3116|(1, 2, 11)|var|float64
func_3115_call = mutated_mod.get_global_var('func_3115')
call_3117 = func_3115_call(var_3116)
output = call_3117
func_3118 = relay.Function([var_3116], output)
mutated_mod['func_3118'] = func_3118
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3143 = relay.const([[[8.624503],[9.488357],[8.756965],[0.190969],[0.096601],[7.539208],[-4.223229],[4.707438],[6.252431],[9.809343],[-9.509493],[5.271645],[-2.392993],[-5.742733]],[[6.827254],[6.759596],[5.593161],[3.759069],[-2.696546],[-1.037052],[-1.816346],[3.686391],[-8.084839],[7.099435],[-4.327628],[-6.643417],[0.236215],[7.384099]],[[5.476144],[9.907370],[2.473809],[7.299054],[2.771012],[2.316655],[2.134863],[1.545334],[-6.456115],[-2.857843],[-7.422190],[-5.397858],[-3.303365],[9.709398]],[[-3.595163],[-1.385109],[-4.187697],[3.856787],[-8.855696],[0.606351],[1.163551],[3.414430],[-0.062425],[-8.296880],[1.386646],[4.656460],[7.886892],[3.418500]],[[-2.766582],[4.122996],[8.905797],[-2.334864],[1.947983],[3.406339],[7.308748],[2.957648],[-5.288887],[9.784631],[-6.156850],[0.536749],[7.073052],[4.059874]],[[-7.138964],[-6.147410],[8.667494],[-2.737566],[9.170243],[3.209414],[-8.964597],[-7.075573],[5.173975],[-1.559627],[1.445690],[-0.568717],[-0.872884],[3.741674]],[[-8.759101],[-2.424318],[4.878198],[-3.845199],[-3.068477],[6.110589],[2.733113],[-0.545690],[-1.644201],[9.783113],[-0.128740],[3.971916],[-2.775059],[5.371366]],[[4.583697],[-3.180160],[3.312253],[-0.376055],[2.342698],[-3.407831],[2.179435],[-8.885842],[-8.012604],[-7.601370],[1.631943],[-5.037143],[-3.418464],[0.418835]],[[2.640365],[5.219727],[-0.272259],[-0.383895],[-9.231441],[-6.443016],[8.355769],[5.523817],[4.666021],[-7.022999],[-9.542627],[-3.310454],[-4.342965],[8.734161]],[[-5.155958],[3.940061],[-7.837464],[-6.919565],[-4.711273],[-6.965424],[2.201413],[7.437926],[8.152023],[-5.064024],[-9.101185],[-1.602574],[6.176919],[-8.599363]],[[1.871363],[-0.484269],[9.160746],[7.255533],[-7.164062],[-6.170470],[8.122426],[8.825858],[5.957661],[7.117732],[6.832524],[6.547728],[-1.662457],[-4.303176]]], dtype = "float32")#candidate|3143|(11, 14, 1)|const|float32
uop_3144 = relay.atan(const_3143.astype('float32')) # shape=(11, 14, 1)
func_3115_call = mod.get_global_var('func_3115')
func_3118_call = mutated_mod.get_global_var('func_3118')
var_3148 = relay.var("var_3148", dtype = "float64", shape = (22,))#candidate|3148|(22,)|var|float64
call_3147 = relay.TupleGetItem(func_3115_call(relay.reshape(var_3148.astype('float64'), [1, 2, 11])), 0)
call_3149 = relay.TupleGetItem(func_3118_call(relay.reshape(var_3148.astype('float64'), [1, 2, 11])), 0)
var_3152 = relay.var("var_3152", dtype = "float32", shape = (11, 14, 2))#candidate|3152|(11, 14, 2)|var|float32
bop_3153 = relay.subtract(const_3143.astype('uint32'), var_3152.astype('uint32')) # shape=(11, 14, 2)
func_3115_call = mod.get_global_var('func_3115')
func_3118_call = mutated_mod.get_global_var('func_3118')
call_3177 = relay.TupleGetItem(func_3115_call(relay.reshape(call_3147.astype('float64'), [1, 2, 11])), 0)
call_3178 = relay.TupleGetItem(func_3118_call(relay.reshape(call_3147.astype('float64'), [1, 2, 11])), 0)
output = relay.Tuple([uop_3144,call_3147,var_3148,bop_3153,call_3177,])
output2 = relay.Tuple([uop_3144,call_3149,var_3148,bop_3153,call_3178,])
func_3179 = relay.Function([var_3148,var_3152,], output)
mod['func_3179'] = func_3179
mod = relay.transform.InferType()(mod)
var_3180 = relay.var("var_3180", dtype = "float64", shape = (22,))#candidate|3180|(22,)|var|float64
var_3181 = relay.var("var_3181", dtype = "float32", shape = (11, 14, 2))#candidate|3181|(11, 14, 2)|var|float32
output = func_3179(var_3180,var_3181,)
func_3182 = relay.Function([var_3180,var_3181,], output)
mutated_mod['func_3182'] = func_3182
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3194 = relay.const([[[-6,1,8,10,-8,1,-6,6,-6,-9,-2,-8,5,-9,3],[6,9,-7,-1,-7,5,-4,8,8,-2,1,-7,-5,4,7],[-10,-9,4,-5,4,-5,-7,10,9,-9,5,7,8,-4,-5],[-2,-8,5,-8,7,10,10,1,5,10,-2,-4,8,-10,6],[5,-2,2,5,6,3,3,7,5,-3,8,9,4,-3,2]],[[-10,7,2,-9,-9,-10,-5,6,-7,6,6,-5,3,6,6],[5,-7,-9,-4,-5,-5,7,-7,6,6,6,-5,8,-4,5],[-2,-5,-5,-7,3,3,-10,10,3,-3,-7,2,-4,1,7],[-6,-8,-10,-3,3,-3,-6,9,10,1,3,-4,1,5,4],[9,3,-10,4,9,1,-6,-5,-2,-10,-8,-2,-8,-10,6]],[[7,7,7,-2,-1,8,5,9,-10,-4,-4,3,-5,-9,-8],[-3,4,-6,7,2,8,-2,-4,2,-9,-4,9,9,10,2],[-4,-2,5,9,-5,2,1,-8,-6,-10,-7,8,-4,1,-6],[2,10,-10,2,-8,10,-10,-5,-5,1,6,10,5,4,5],[-10,1,1,-6,-9,-9,4,10,-8,-10,8,8,-1,-9,-2]],[[4,3,4,5,6,2,-4,5,-8,7,-3,-6,-3,5,-4],[10,10,3,7,2,5,9,2,3,8,-10,7,3,2,3],[6,4,-9,10,7,1,7,1,-5,-1,-4,-3,4,-10,3],[-4,9,3,-7,5,-6,-7,-6,4,3,-4,6,-8,1,-9],[-5,3,3,3,-10,7,5,-9,-4,-4,-8,-6,6,-5,5]],[[-3,-8,-6,4,-2,-8,-10,-5,-5,2,10,8,2,-1,2],[10,-8,-4,9,2,2,-4,-4,-3,-10,8,5,-5,9,6],[3,9,-6,4,10,-1,-9,-7,4,1,7,3,5,-10,5],[10,-6,9,-1,-7,2,-3,3,-3,-10,-10,-4,-8,10,-7],[-8,4,5,3,-8,-7,10,-1,-2,7,-9,-10,9,-3,-9]],[[-5,7,-8,3,-8,-4,1,-7,-7,7,2,3,10,-1,1],[5,-5,-5,5,-6,9,10,-6,-2,-7,-8,-4,2,-5,9],[10,-3,-6,-10,6,-6,6,7,-4,-6,8,1,-7,6,-3],[-7,8,-10,10,-5,-7,-3,8,6,7,-2,-6,-6,5,4],[-8,-3,-2,-1,4,-1,7,-6,4,-9,-6,7,-6,-6,7]],[[-9,2,1,4,8,-8,-10,3,-1,10,7,1,-5,-6,-5],[10,10,-5,-7,3,-6,-6,-7,2,5,6,-5,7,3,2],[8,4,-5,-9,8,10,2,-10,-5,6,4,6,-10,-1,10],[-5,-5,-8,-7,-5,-8,9,-10,-8,-1,9,-8,-3,9,3],[7,-10,6,5,5,-10,-6,3,-6,-3,7,2,-8,-4,-1]],[[8,5,-2,-6,-6,-6,3,5,-8,-7,8,4,9,-5,10],[-10,-3,8,7,2,-4,10,-2,3,6,2,6,-5,7,6],[7,-6,10,-6,8,2,8,-1,-7,-2,-8,8,-10,7,-3],[5,-10,10,4,10,-8,8,-2,-8,-5,1,-5,-7,2,-4],[-10,4,-1,3,2,9,-4,8,8,-5,6,-8,7,-6,1]],[[5,-9,3,-5,7,-8,9,-5,-7,3,-6,10,-10,1,-9],[7,6,-4,6,-3,-9,1,-2,7,7,-1,-6,9,9,3],[-4,1,6,9,5,7,3,-3,2,2,7,6,-4,1,-7],[-3,-5,-1,10,-3,1,10,-5,7,-5,9,-2,-7,-10,-2],[-7,9,7,-2,-9,-5,-4,2,-10,-9,10,6,2,8,6]],[[-10,3,4,9,-1,1,-9,-1,-4,-2,5,-10,-3,8,8],[-1,8,10,-8,-6,-9,2,-9,1,-5,6,-6,-3,-9,-2],[7,-5,-9,-5,-4,-5,9,1,10,3,4,5,6,-8,-1],[3,-4,-2,-5,-2,-9,2,-4,-6,-4,10,-8,9,-5,10],[7,-5,-2,-8,2,-6,4,-9,-2,3,-7,5,9,1,2]],[[3,5,-2,5,-3,-9,9,8,2,-4,5,9,7,5,6],[-9,7,-7,10,9,8,-2,-3,-5,-10,1,2,-5,-2,7],[8,-8,-2,3,8,5,4,-3,8,2,-10,-3,-5,-1,1],[-4,6,3,7,-9,-10,1,2,10,5,-9,-5,7,-3,4],[8,2,-9,3,-10,1,7,-5,9,2,-7,8,5,9,-6]],[[3,-10,2,-9,7,9,3,-1,6,4,-3,9,3,1,-2],[-5,-2,10,-6,1,10,3,-8,4,4,2,-10,-3,4,5],[10,3,-8,-8,-1,8,-8,9,-5,10,2,9,4,5,5],[-6,-3,-8,9,5,-6,-5,6,-10,6,10,-3,-2,-2,-5],[-8,-5,7,3,-1,7,-3,-2,8,-8,4,-4,1,-4,-2]],[[2,-9,4,10,1,6,-7,-4,-8,2,9,-5,3,-9,-9],[-5,5,-7,9,6,9,9,3,-6,6,-6,-4,-7,7,3],[9,8,-3,4,-2,-1,4,-8,3,-7,-4,3,-6,-6,-6],[-10,8,-2,-10,-2,-7,-5,2,8,-1,-2,8,4,6,8],[10,1,-3,-10,7,7,-4,-7,-8,-10,9,-4,9,-4,8]],[[7,7,10,10,5,4,3,4,4,4,9,-8,-4,-10,2],[-8,8,8,7,9,-3,-2,1,-6,-6,-9,-6,7,-5,-8],[-5,-7,-4,-2,-3,1,-2,-4,-8,5,3,-8,-4,10,-4],[-8,5,-1,-2,-7,3,-1,-10,-7,-5,2,-10,-8,-7,-4],[5,9,9,8,-4,6,-3,-4,2,-1,4,9,-6,-8,5]],[[6,-6,-1,-7,-8,-4,-10,-3,-9,-4,4,-6,3,9,-4],[7,-6,5,10,6,2,-4,8,5,-2,10,10,-10,7,-8],[4,3,8,7,9,-10,5,1,3,3,-8,3,2,-1,-5],[-1,4,-10,1,2,3,9,8,-5,10,6,2,4,-5,4],[5,10,9,-4,9,8,-10,4,-1,-6,-7,-6,4,-5,-8]]], dtype = "uint32")#candidate|3194|(15, 5, 15)|const|uint32
var_3195 = relay.var("var_3195", dtype = "uint32", shape = (15, 5, 15))#candidate|3195|(15, 5, 15)|var|uint32
bop_3196 = relay.bitwise_and(const_3194.astype('uint32'), relay.reshape(var_3195.astype('uint32'), relay.shape_of(const_3194))) # shape=(15, 5, 15)
output = bop_3196
output2 = bop_3196
func_3213 = relay.Function([var_3195,], output)
mod['func_3213'] = func_3213
mod = relay.transform.InferType()(mod)
var_3214 = relay.var("var_3214", dtype = "uint32", shape = (15, 5, 15))#candidate|3214|(15, 5, 15)|var|uint32
output = func_3213(var_3214)
func_3215 = relay.Function([var_3214], output)
mutated_mod['func_3215'] = func_3215
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3402 = relay.var("var_3402", dtype = "float64", shape = (11, 6, 11))#candidate|3402|(11, 6, 11)|var|float64
uop_3403 = relay.cos(var_3402.astype('float64')) # shape=(11, 6, 11)
output = relay.Tuple([uop_3403,])
output2 = relay.Tuple([uop_3403,])
func_3418 = relay.Function([var_3402,], output)
mod['func_3418'] = func_3418
mod = relay.transform.InferType()(mod)
mutated_mod['func_3418'] = func_3418
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3419 = relay.var("var_3419", dtype = "float64", shape = (11, 6, 11))#candidate|3419|(11, 6, 11)|var|float64
func_3418_call = mutated_mod.get_global_var('func_3418')
call_3420 = func_3418_call(var_3419)
output = call_3420
func_3421 = relay.Function([var_3419], output)
mutated_mod['func_3421'] = func_3421
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3457 = relay.const([[[6.925465,2.953037,3.226458,1.943574,5.862819,-5.117919,-9.819826,-1.402115,5.764186,-0.940426,6.476582,1.703158,7.356132,3.867739,9.675200,-7.849173],[2.849405,6.810570,0.066849,-2.795106,-0.678250,3.047250,9.977724,-6.042028,5.662405,6.766319,7.577914,-1.894824,5.607476,-7.343598,-5.837286,-5.008517],[1.571687,2.267557,-0.725910,8.783237,-1.582616,-9.005958,-1.505735,-1.143272,6.693356,5.976272,-9.329648,3.548565,5.344728,3.454924,-9.138606,6.256801],[4.827260,-9.234125,-8.944278,9.452858,7.773137,2.367827,-2.738995,5.934776,8.905484,-5.682155,-0.929891,-0.149967,-4.254525,7.879753,7.279953,-4.675389],[9.449733,-1.799870,-6.451255,-1.123712,5.413425,1.878787,-3.175857,-0.153493,4.694004,4.316655,-0.052773,8.185671,7.975084,-1.211818,0.983331,-5.663422],[0.047592,8.118523,-9.669726,4.721476,3.866530,0.530974,3.017595,9.456338,-0.780868,-7.970044,-6.169028,0.140735,3.292913,-2.148528,-0.393381,2.399542],[-3.429751,9.067418,4.063836,-2.840223,-6.907720,-6.336783,1.452763,-1.655975,-6.220360,2.950524,7.311848,2.643465,-0.231031,3.388059,-6.773270,-1.277545]],[[0.457248,9.168772,1.797978,8.897061,8.396437,8.993185,-6.957884,-6.559477,9.257879,1.094354,1.761378,1.107064,9.876839,-9.024809,0.295535,-7.307450],[6.359408,6.078182,1.493501,-5.610919,-3.156625,-4.735075,5.020435,-6.601826,-8.958954,9.975859,-3.894580,5.662193,-7.061749,7.647191,-8.813961,-9.916417],[6.642618,-4.005437,6.798228,5.452698,6.503421,-6.654241,-7.434596,1.493260,-1.817024,-7.078792,6.950474,-8.829793,-5.528226,1.650815,8.030315,-6.902977],[-9.746696,-0.040998,3.284755,3.968183,2.960873,1.389732,-3.936294,-5.952819,-5.528429,9.196453,-9.262674,6.735196,8.624509,0.022510,-2.270976,7.748751],[1.195752,-2.227272,3.726271,5.115806,8.979799,7.426422,6.061356,9.298545,-1.478893,1.397609,-8.720974,1.771288,4.955254,3.759271,-1.846467,-3.607520],[-6.448744,-3.114075,4.732774,-6.749089,3.636536,-1.599993,9.792498,-1.337097,9.302514,-0.592078,-0.917566,5.908694,-8.626962,8.282824,-0.214395,-4.064080],[6.581819,-1.280189,-2.983827,4.158752,-7.134404,-1.786292,2.368412,-5.980737,-3.492185,1.252109,-1.621928,8.404686,8.241752,-3.902516,-5.689039,-6.532077]]], dtype = "float64")#candidate|3457|(2, 7, 16)|const|float64
uop_3458 = relay.sinh(const_3457.astype('float64')) # shape=(2, 7, 16)
bop_3471 = relay.logical_xor(uop_3458.astype('uint8'), relay.reshape(const_3457.astype('uint8'), relay.shape_of(uop_3458))) # shape=(2, 7, 16)
func_3179_call = mod.get_global_var('func_3179')
func_3182_call = mutated_mod.get_global_var('func_3182')
const_3479 = relay.const([-5.157011,7.683702,5.085644,0.029791,9.338079,-9.490106,0.344522,-8.944993,1.189933,5.252361,-1.609212,-0.213017,-7.139054,-3.362274,-9.204534,-2.886012,-0.390572,9.495660,-3.025912,-3.388048,0.993141,6.731441], dtype = "float64")#candidate|3479|(22,)|const|float64
var_3480 = relay.var("var_3480", dtype = "float32", shape = (308, 1))#candidate|3480|(308, 1)|var|float32
call_3478 = relay.TupleGetItem(func_3179_call(relay.reshape(const_3479.astype('float64'), [22,]), relay.reshape(var_3480.astype('float32'), [11, 14, 2]), ), 0)
call_3481 = relay.TupleGetItem(func_3182_call(relay.reshape(const_3479.astype('float64'), [22,]), relay.reshape(var_3480.astype('float32'), [11, 14, 2]), ), 0)
func_3179_call = mod.get_global_var('func_3179')
func_3182_call = mutated_mod.get_global_var('func_3182')
call_3493 = relay.TupleGetItem(func_3179_call(relay.reshape(const_3479.astype('float64'), [22,]), relay.reshape(var_3480.astype('float32'), [11, 14, 2]), ), 3)
call_3494 = relay.TupleGetItem(func_3182_call(relay.reshape(const_3479.astype('float64'), [22,]), relay.reshape(var_3480.astype('float32'), [11, 14, 2]), ), 3)
output = relay.Tuple([bop_3471,call_3478,const_3479,var_3480,call_3493,])
output2 = relay.Tuple([bop_3471,call_3481,const_3479,var_3480,call_3494,])
func_3501 = relay.Function([var_3480,], output)
mod['func_3501'] = func_3501
mod = relay.transform.InferType()(mod)
mutated_mod['func_3501'] = func_3501
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3502 = relay.var("var_3502", dtype = "float32", shape = (308, 1))#candidate|3502|(308, 1)|var|float32
func_3501_call = mutated_mod.get_global_var('func_3501')
call_3503 = func_3501_call(var_3502)
output = call_3503
func_3504 = relay.Function([var_3502], output)
mutated_mod['func_3504'] = func_3504
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3552 = relay.var("var_3552", dtype = "float64", shape = (10, 4, 2))#candidate|3552|(10, 4, 2)|var|float64
uop_3553 = relay.asin(var_3552.astype('float64')) # shape=(10, 4, 2)
output = uop_3553
output2 = uop_3553
func_3555 = relay.Function([var_3552,], output)
mod['func_3555'] = func_3555
mod = relay.transform.InferType()(mod)
mutated_mod['func_3555'] = func_3555
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3556 = relay.var("var_3556", dtype = "float64", shape = (10, 4, 2))#candidate|3556|(10, 4, 2)|var|float64
func_3555_call = mutated_mod.get_global_var('func_3555')
call_3557 = func_3555_call(var_3556)
output = call_3557
func_3558 = relay.Function([var_3556], output)
mutated_mod['func_3558'] = func_3558
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3840 = relay.const([[[-9,-5,-9],[8,-10,8],[-10,-3,6],[-3,-4,-3],[-6,-10,-2],[-7,5,4],[9,-2,7],[-10,-6,5],[8,2,-8],[2,7,-3],[4,9,-9],[3,-7,8],[4,2,-10],[3,-7,-9],[1,9,5]],[[8,9,9],[10,-10,7],[-10,6,3],[9,6,-3],[10,-8,4],[10,-5,9],[1,-5,6],[-6,5,10],[-10,5,6],[-2,-6,5],[8,-1,-6],[-6,-2,5],[5,6,-5],[-9,9,2],[-6,2,-5]],[[-9,4,-5],[-2,7,-3],[4,6,-7],[8,6,2],[3,-2,-7],[1,9,9],[6,-6,5],[-5,-7,-1],[-2,2,6],[-5,1,3],[-6,7,-8],[1,8,-6],[9,4,-2],[2,-5,1],[-10,10,6]],[[1,-8,7],[-5,-1,-8],[-7,-6,-2],[-7,-2,1],[-4,2,4],[9,-9,-4],[-2,-5,-3],[10,9,-1],[6,-5,2],[4,9,-2],[-5,8,6],[10,-2,-3],[-9,5,8],[-9,5,3],[-2,-3,-2]],[[-3,4,10],[-3,1,7],[-10,-4,-2],[-10,5,7],[-1,4,9],[9,-2,3],[-4,-2,2],[7,-6,7],[-3,1,10],[-7,-6,-7],[8,8,6],[4,8,4],[-7,-1,2],[-3,5,-5],[3,-8,-5]],[[-5,-10,3],[-4,7,-2],[1,-2,4],[-2,-10,-2],[-2,7,3],[6,2,-1],[-1,1,7],[8,5,-4],[-5,6,3],[-8,-1,6],[8,-4,-7],[7,-9,5],[4,-6,5],[-7,-6,6],[1,6,-1]],[[-7,-4,9],[-5,-9,-5],[-2,10,-9],[8,7,-9],[3,7,1],[2,8,9],[7,-6,-10],[-3,-1,10],[1,-5,4],[-1,3,8],[7,2,-8],[-5,-4,-3],[5,5,-10],[7,5,-10],[-6,-9,9]],[[1,-9,-3],[1,-2,-10],[-9,3,-10],[-1,4,7],[-6,-3,1],[2,7,-4],[-8,8,-2],[-9,3,5],[4,-10,-3],[-2,-9,-5],[8,2,-1],[-8,3,-3],[4,4,-1],[-1,-6,-5],[8,-9,4]],[[-9,3,10],[8,-7,1],[6,9,5],[10,8,4],[6,-1,-1],[10,7,-1],[-1,4,2],[5,3,7],[-7,3,-4],[9,1,6],[4,1,-3],[-10,-3,-10],[2,-10,-1],[-2,-3,-4],[-3,8,2]],[[5,-4,-9],[9,9,6],[7,-7,2],[4,-8,10],[-6,6,9],[10,6,-2],[-10,6,5],[1,7,-6],[5,2,7],[-7,7,8],[3,-1,3],[6,6,-3],[4,-10,-9],[2,6,-9],[-8,-7,2]],[[-2,-5,-4],[6,-10,-3],[-1,6,-10],[10,10,5],[-1,8,9],[-5,-6,4],[9,-1,-2],[3,-3,-7],[-5,-4,4],[-6,4,7],[5,4,4],[-3,-8,1],[1,5,4],[-5,-10,-4],[10,-1,8]]], dtype = "uint16")#candidate|3840|(11, 15, 3)|const|uint16
var_3841 = relay.var("var_3841", dtype = "uint16", shape = (11, 15, 3))#candidate|3841|(11, 15, 3)|var|uint16
bop_3842 = relay.add(const_3840.astype('uint16'), relay.reshape(var_3841.astype('uint16'), relay.shape_of(const_3840))) # shape=(11, 15, 3)
func_2842_call = mod.get_global_var('func_2842')
func_2847_call = mutated_mod.get_global_var('func_2847')
const_3851 = relay.const([-9.794701,-2.613743,3.999755,7.854563,-0.110605,7.465357,4.076512,4.699046,-3.852199,3.184243,-9.723056,3.969475,-0.758055,-6.593508,0.779483,-1.594236,5.002901,2.914659,2.838416,-9.786839,-1.630095,9.677951,3.055351,-1.758528,7.458936,-8.051535,-4.264230,-3.499645,2.828281,-3.277881,-9.821014,-9.689786,-0.238180,7.107819,-9.838670,7.822237,9.534610,-9.210606,-4.964421,-5.908450,-7.718384,6.757555,-2.422940,-0.938292,-3.737995,7.377297,4.843037,2.777716,2.960400,0.117778,-7.476146,3.491829,7.070145,-3.121689,-4.975015,8.802345,-4.069516,9.917619,2.860891,-2.116605,7.559625,-2.653826,5.868203,-8.409019,-6.475216,-4.585262,-6.223283,7.481448,0.733785,0.042921,-8.768847,-7.588560,-5.746032,-1.993604,4.269584,3.322347,-1.287438,9.234623,7.127190,-9.952302,8.301275,1.495569,-5.571689,2.220087,-7.455170,8.085794,-3.253896,1.188745,-3.598395,-7.965399,-9.363199,-8.958257,5.870688,-5.640302,5.156658,7.307828,1.856107,-3.736701,3.364226,6.532390,2.992761,-0.582033,5.971971,-4.461568,3.582906,2.677852,-3.326758,-4.073398,-8.187097,9.093925,-6.782993,-7.719225,5.267517,3.211649,4.044357,-7.738267,-0.793209,-0.767496,3.288648,9.570840,8.708491,-9.605178,-0.725210,6.417238,-4.835289,-5.175643,0.337061,-1.279334,9.890832,3.645907,4.660774,4.701755,0.532785,3.339357,-8.332313,7.530908,8.310921,-4.425514,5.771969,-0.518529,-9.918317,-1.979821,-6.704801,-6.872175,-9.891922,-3.661327,8.816777,4.939055,7.953565,8.800707,1.065852,3.354058,6.392348,-0.947835,7.814812,-1.062379,8.251471,-9.900032,7.671124,-0.656535,-7.896438,6.213519,-9.955378,-2.315063,6.625993,-1.933521,5.842257,-5.065399,9.686846,9.761502,2.452876,-9.714179,-6.476503,-2.603328,9.751161,7.795002,5.886140,7.556547,-7.690244,3.161764,-4.845699,-5.611018,5.452280,-5.887059,-4.996534,-2.244597,2.355297,-9.953667,3.691911,3.829980,3.342710,-4.544717,-2.780122,8.483687,-5.856646,-2.396674,-3.640116,-6.264393,8.481110,-9.038947,-0.711473,-9.160896,0.283495,6.087965,0.600531,0.223548,3.511053,-8.048331,9.130760,-3.412954,-1.568715,-3.555747,-6.079775,1.385094,2.459269,5.137804,-7.776086,3.482989,-1.189547,-8.116188,-9.241206,9.875891,4.441172,9.670236,3.939364,-5.252140,-9.005530,-1.458580,0.483975,2.848929,8.206695,-7.550670,-5.492929,6.139024,-3.492491,-3.312974,8.754838,8.955144,5.637737,7.803559,-4.261703,0.955462,4.824838,9.127659,8.478805,4.097645,5.747872,-0.106416,-3.800017,6.980833,2.582025,1.413972,9.051209,1.079157,9.175909,7.227198,9.515368,-0.617360,-8.956208,1.994265,-4.479084,-5.536387,6.008669,0.914039,-0.720615,-0.876901,8.795933,-9.656801,-6.020641,6.712787,-0.170562,-3.359244,5.903197,-3.783173,-7.616556,4.871943,8.056229,9.642861,-1.284830,-5.364350,3.032989,-8.061746,-7.261763,1.097854,4.733860,-9.725577,5.374749,5.444061,6.508470,-7.577577,4.618072,5.481135,7.503153,2.904000,4.896151,-6.202136,2.931316,6.200262,3.142480,-0.222703,-2.398099,-8.856553,6.695168,-4.614951,-2.064497,5.089454,9.305675,-3.760836,3.552454,-8.638771,7.925792,2.113361,-9.660470,-4.895908,5.178984,-1.571666,7.368485,5.135987,-4.316870,8.278518,-7.176334,-6.240774,6.462120,-7.091231,7.478206,-9.642611,4.431337,7.050354,-7.023943,0.968950,-7.625407,0.276684,-9.506017,8.004010,3.483611,9.487231,6.009225,9.552840,-2.678952,9.868688,-5.419427,-9.158602,3.147054,8.024337,8.948434,5.945129,-2.855961,6.352564,8.679966,4.333329,-7.819046,-3.335634,8.592819,-6.366460,7.339458,7.004263,5.860170,0.798407,0.942126,0.338899,9.561533,-4.388037,4.695143,-6.658520,-2.198582,0.122813,8.625305,-8.046160,7.768604,-4.888124,-5.607195,6.678036,-3.346343,-6.854196,2.647285,-8.828173,-9.799124,8.543350,5.152205,-5.474148,5.778499,-6.138552,2.781049,4.873595,4.669388,6.158268,8.950820,-4.111816,6.139792,8.612637,-1.319196,5.183422,9.893226,-4.877854,8.214673,-9.039114,2.002878,1.540192,-4.880585,9.759755,-5.081180,8.859079,9.048782,6.219155,0.833902,-4.113867,7.878081,-5.003303,-5.973541,9.453969,-3.164362,-9.399071,-0.243164,-8.387197,0.737094,-7.810111,9.327968,4.185094,1.625205,2.638366,-7.724290,-0.288628,-5.023437,-2.952248,-8.211414,-5.687631,3.379206,-4.778215,-8.930716,-5.434688,-7.022880,2.323913,9.704721,2.195578,-9.894595,4.509256,-6.671517,-8.470418,-0.774299,6.506554,-9.063406,8.286753,-5.343761,0.768987,3.631971,-5.082876,-8.903857,2.213450,7.953613,1.186044], dtype = "float32")#candidate|3851|(450,)|const|float32
const_3852 = relay.const([[-0.708696,5.993409,5.716638,5.120283,1.065759,-8.676600,-3.655489,4.287019,-5.389491,8.322832,8.283158,-3.185231,-7.612405,4.146051,0.399710,8.543037,-4.544432,9.352137,-1.564097,3.833893,-0.026348,-5.967495,7.602081,-1.916529,1.872355,3.770401,-1.430584,6.650074,9.862701,9.109400,6.947137,3.893876,5.561691,8.311425,2.540271,0.782525,4.270472,8.804478,8.760659,-1.883340,2.059209,0.933219,0.328115,-3.382062,9.753110,6.389500,-3.702342,9.895114,8.170531,5.641796,8.294181,-0.938071,-1.309947,3.264348,2.047046,-9.678814,3.619714,-0.443815,3.376135,3.747964,-4.219707,0.994060,9.948269,-8.827580,8.403046,-6.395432,4.174098,8.205251,-2.964521,3.239031,-8.567397,-5.805115,-2.100293,-7.178105,8.299045,-3.671846,-0.329560,-4.169307,-7.866021,-9.608765,-6.241572,-3.678931,-5.554030,1.439833,-4.506898,-3.585876,-3.344292,-7.429292,-7.392274,-5.517406,8.025489,4.339493,-2.772765,6.763530,0.205466,4.573343,-7.850449,1.441231,1.936774,7.975278,2.029381,6.132221,-3.633065,-2.946000,-9.507669,-4.905002,-7.547374,-8.402816,1.871115,4.298989,5.308489,-3.303691,9.465452,-6.627083,-4.794996,-8.800572,-0.921613,-5.945562,-2.504541,6.934669,5.816009,-5.986260,8.074692,8.886498,-3.660156,2.044335,8.905418,-5.110147,6.730370,1.057542,-5.544502,-9.163738,5.256083,-6.202649,7.236155,3.899250,4.706229,-8.121247,-7.767611,-9.806430,9.659876,-5.086786,8.279871,5.525943,-6.145826,8.863813,-6.298866,6.417295,-2.257363,1.515849,1.520124,-9.705984,-1.595660,4.695202,-4.989624,-7.937748,-0.161393,-1.886914,9.343943,-4.000391,5.558642,-5.026356,6.744662,5.986942,2.815238,-1.631651,8.338411,-3.631134,1.014260,-5.923535,3.965174,9.679269,-6.035718,3.882146,8.708126,2.975353,9.384264,7.216611,0.681437,-5.096775,2.668774,9.967420,-9.348226,0.807720,0.505365,4.503974,-5.246211,-4.190029,6.495406,-1.938666,-6.804970,9.463774,9.820161,-9.915154,2.938633,-1.930529,3.692418,-1.052025,8.917489,-3.481741,7.056474,1.266281,-2.914172,-4.551416,1.638205,0.966294,-8.204463,-8.927272,5.899284,-3.662654,9.352357,9.710758,-6.204744,-2.898653,4.440798,1.864886,1.007936,-1.778250,-6.324240,0.271203,7.021565,5.827976,3.467305,-0.942063,6.741201,6.951125,3.227911,9.774829,-6.820252,7.203813,-6.667798,1.128821,5.755010,-6.925625,-9.403947,2.957114,-1.520858,-0.560173,-9.881147,-5.255323,6.337565,5.243165,-7.148870,4.685877,-5.558873,0.622469,8.144537,-2.286781,-1.447806,-9.667494,-8.817675,0.363776,6.846707,-3.157458,-5.621992,7.260830,7.141725,-1.634253,2.093232,-9.530442,-7.923545,0.758280,-4.362604,-5.217702],[-1.307592,-9.649163,-6.319680,7.023155,7.555059,-9.328781,-6.400393,8.564885,-2.372982,3.839617,2.235838,3.603458,6.531994,8.725617,7.092975,6.295304,7.965929,-8.172509,0.018586,4.708912,-1.562840,-6.094284,2.911404,-0.190402,2.243780,0.481383,7.239093,-4.186908,8.165208,3.189487,9.578500,-5.003641,-4.619294,-9.518211,-0.519583,-2.992741,4.474835,3.630245,-0.336125,-5.345650,-8.440211,8.281585,6.520752,-3.816490,9.936068,3.630296,-5.487151,5.876158,-0.611617,-4.705915,9.651060,4.201942,7.153353,3.799105,-6.819472,0.707895,-7.847786,5.042156,-2.602769,-1.175530,5.138498,-4.930177,-6.488096,-7.436774,-3.902295,1.498858,1.849536,-7.677066,-1.821596,-1.779554,-7.656238,7.916241,-7.686683,-3.013468,-6.016395,1.795805,-6.319687,-0.840758,3.716195,4.911673,2.002508,-8.693001,-2.906136,-0.555998,-8.661974,8.622687,-0.216347,6.927666,0.846995,-2.799256,0.718121,2.313913,3.059133,-2.418507,-4.250659,-1.661457,-7.862395,-8.874899,-7.108250,5.317037,-0.990409,5.518869,9.878093,8.153461,-1.947615,9.161652,2.889460,0.152269,-9.609780,-4.336374,6.637761,-1.019876,1.761359,-2.878801,4.676662,-2.112038,7.775244,2.076217,7.907485,9.672262,-8.857046,8.413292,-2.151766,-7.183292,-2.198148,6.780671,-1.174664,5.118994,0.917139,1.293038,-1.274914,-6.553716,8.390732,-5.926339,-8.683105,-8.207450,-0.313971,2.846257,-4.823595,4.097298,-8.942553,-0.800472,2.498207,-1.511007,-7.704257,5.764289,0.055640,-3.964986,7.320709,0.685284,-9.485942,-8.782205,1.600281,8.131452,-1.762262,-8.791458,-5.329724,7.812338,0.613467,-6.624710,2.787114,-3.594623,8.620248,2.537457,3.126478,-4.664705,-4.782662,0.176507,-1.429172,5.721518,7.173112,4.014789,-6.864682,6.790246,-9.163234,6.783475,-1.915190,3.090175,-8.377874,-2.304586,1.387757,-4.700705,-6.876678,-3.711332,-1.585937,4.745384,0.038024,3.286151,3.400455,0.211873,-7.173316,0.929440,-1.792848,-0.999417,1.574246,3.762177,-8.364755,-0.369264,6.086418,7.937606,-8.897303,1.420161,-7.839940,0.405194,-5.432064,3.630736,-8.291256,6.522473,2.172203,4.130425,-3.552711,-4.510629,-0.697535,2.748421,1.880123,-4.709355,5.690849,4.908994,-3.482424,2.713308,-6.841742,-0.228785,3.979276,7.655558,0.071433,9.859939,0.966168,-9.614582,-6.272847,4.271523,6.046759,1.834261,-4.734067,-9.679591,-2.501108,6.352176,-7.266046,1.627190,9.128884,9.403724,6.768698,-2.613909,-0.218137,2.685801,5.495913,-5.047783,-4.347874,0.566939,-4.533656,5.825756,-0.042532,5.086301,-9.907165,-9.082189,-6.829179,3.448064,0.714516,-3.960417,-2.451196,-7.527677,5.608313,-5.703979,7.770099,-7.986589]], dtype = "float32")#candidate|3852|(2, 264)|const|float32
call_3850 = relay.TupleGetItem(func_2842_call(relay.reshape(const_3851.astype('float32'), [10, 5, 9]), relay.reshape(const_3852.astype('float32'), [528,]), relay.reshape(const_3851.astype('float32'), [10, 5, 9]), ), 0)
call_3853 = relay.TupleGetItem(func_2847_call(relay.reshape(const_3851.astype('float32'), [10, 5, 9]), relay.reshape(const_3852.astype('float32'), [528,]), relay.reshape(const_3851.astype('float32'), [10, 5, 9]), ), 0)
output = relay.Tuple([bop_3842,call_3850,const_3851,const_3852,])
output2 = relay.Tuple([bop_3842,call_3853,const_3851,const_3852,])
func_3856 = relay.Function([var_3841,], output)
mod['func_3856'] = func_3856
mod = relay.transform.InferType()(mod)
mutated_mod['func_3856'] = func_3856
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3857 = relay.var("var_3857", dtype = "uint16", shape = (11, 15, 3))#candidate|3857|(11, 15, 3)|var|uint16
func_3856_call = mutated_mod.get_global_var('func_3856')
call_3858 = func_3856_call(var_3857)
output = call_3858
func_3859 = relay.Function([var_3857], output)
mutated_mod['func_3859'] = func_3859
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3998 = relay.var("var_3998", dtype = "int64", shape = ())#candidate|3998|()|var|int64
var_3999 = relay.var("var_3999", dtype = "int64", shape = (16, 5, 15))#candidate|3999|(16, 5, 15)|var|int64
bop_4000 = relay.bitwise_and(var_3998.astype('int64'), var_3999.astype('int64')) # shape=(16, 5, 15)
output = relay.Tuple([bop_4000,])
output2 = relay.Tuple([bop_4000,])
func_4003 = relay.Function([var_3998,var_3999,], output)
mod['func_4003'] = func_4003
mod = relay.transform.InferType()(mod)
var_4004 = relay.var("var_4004", dtype = "int64", shape = ())#candidate|4004|()|var|int64
var_4005 = relay.var("var_4005", dtype = "int64", shape = (16, 5, 15))#candidate|4005|(16, 5, 15)|var|int64
output = func_4003(var_4004,var_4005,)
func_4006 = relay.Function([var_4004,var_4005,], output)
mutated_mod['func_4006'] = func_4006
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4295 = relay.var("var_4295", dtype = "uint32", shape = ())#candidate|4295|()|var|uint32
var_4296 = relay.var("var_4296", dtype = "uint32", shape = (10, 2, 15))#candidate|4296|(10, 2, 15)|var|uint32
bop_4297 = relay.bitwise_xor(var_4295.astype('uint32'), var_4296.astype('uint32')) # shape=(10, 2, 15)
func_2842_call = mod.get_global_var('func_2842')
func_2847_call = mutated_mod.get_global_var('func_2847')
var_4313 = relay.var("var_4313", dtype = "float32", shape = (450,))#candidate|4313|(450,)|var|float32
const_4314 = relay.const([8.771190,3.749082,1.538369,0.536874,-5.662673,-5.160392,7.203021,3.359811,7.798163,-2.535619,-0.268662,-8.623970,-3.924896,0.697597,-3.302206,-4.078180,-0.645174,9.199083,-9.549174,6.696593,-6.230045,-2.357350,-7.034684,-9.280656,4.389422,-7.665307,3.177307,-6.873891,-2.990522,4.854058,-4.203850,-8.116993,3.896099,7.005947,-4.907028,-3.394575,-5.524244,-2.207475,8.310816,-3.603842,-8.370554,-6.618325,-5.580367,7.426963,-9.298838,7.265081,-6.520837,1.418905,3.084628,1.074135,2.523123,5.174889,6.209021,7.934872,-9.000257,8.854520,-3.635817,-3.116124,-2.777125,0.012071,-3.642845,8.415219,9.449080,-3.343430,5.407782,-5.376524,-5.624186,2.098949,-5.677842,-6.273682,-8.189040,0.422556,7.546028,2.629105,3.872146,-0.068510,8.946386,-9.153945,-9.892969,-3.733675,-2.465662,8.442980,-2.847074,-2.054093,7.158768,9.374837,-1.899852,-3.730203,6.325180,5.996622,-5.717062,-9.185090,-8.978687,-5.082775,-2.827068,-4.906077,-0.860238,2.678766,-6.693704,8.041694,-3.941812,-1.532066,3.533051,-1.570132,-4.730789,5.332033,9.902290,0.702820,-4.930202,-1.267362,-4.349024,2.955302,-8.746550,5.689323,3.677696,-4.716069,8.489910,-4.474500,5.103242,3.474981,6.220864,6.866327,9.915508,-6.199368,-4.366419,-6.313129,7.316149,7.749019,-1.572495,9.890694,6.848198,5.162421,-1.389961,2.200820,-0.211549,6.082345,6.342103,-6.290391,8.240459,-4.841179,5.154561,-9.660209,2.550108,4.851019,-4.406947,8.569885,-3.004542,0.740742,-4.906262,3.999664,4.005536,-2.686486,7.039251,7.826332,2.909098,-0.904520,-0.721342,-5.108679,0.604063,2.655394,-5.824386,9.307270,3.368778,8.901615,-9.547290,-2.559595,0.518361,-0.166315,9.655847,-3.496350,-6.932514,-2.484226,3.159007,-2.346539,-3.656557,2.465504,-8.508286,6.066094,4.120283,3.149926,2.772025,9.921592,1.166571,5.322830,-7.019659,6.215041,3.550344,6.627805,-5.311050,6.921258,-5.628825,2.597583,3.190614,-8.880487,7.947804,-1.884400,-2.932678,-8.875575,-8.749393,-6.629166,5.739528,8.400735,1.917148,6.590735,-2.357367,-3.210594,3.427756,0.293691,8.365990,1.367063,2.746047,7.177744,-2.161784,3.196908,-4.656691,1.329925,-4.391096,-9.666674,4.635743,6.632916,-0.146409,-2.068801,-3.016828,-4.842742,-3.037501,-8.643216,-6.118267,1.496390,1.228204,1.853927,-6.568389,4.929124,4.770651,1.154743,-8.086669,-7.971470,-1.492806,-5.118756,-0.425461,-6.429339,2.579176,-3.813558,2.665413,-2.196684,7.251130,-5.155905,-7.147328,-4.067192,6.929756,-8.260027,-6.339117,-1.003504,-7.871511,3.097720,6.610044,5.983928,0.833417,-5.832906,8.856941,7.944211,-6.651819,-2.191031,-3.461328,-8.025907,-4.624272,7.253463,6.689589,-1.214299,-4.688803,-8.062016,6.298814,-9.999548,-6.768076,0.514233,2.473007,-9.118550,-3.993526,-5.094110,5.866436,-2.540713,-9.081544,-8.255588,2.728305,8.316224,1.451511,-4.184010,3.553123,5.259277,0.142873,6.781949,2.247329,1.962669,-6.511918,-5.590240,-1.024047,-1.481370,-3.734651,4.467462,6.854593,-9.760282,-3.166589,1.707627,5.983968,2.632846,-4.801241,-2.932418,-9.640238,2.538120,2.344974,-1.650574,1.978718,-1.805141,-7.213056,7.157383,-3.260734,-8.421679,-6.758059,-7.906703,-9.891142,9.999574,-9.489840,-8.388548,6.772975,-6.677660,-3.822771,-6.169202,2.162516,2.602198,-2.021760,5.002292,-2.495838,-0.451074,2.279193,7.745273,-5.264517,-9.527517,-8.897809,-0.395804,4.161699,-0.642363,5.082148,2.869195,-2.181634,-3.350800,5.350129,4.995105,9.879355,4.636714,1.306126,-5.210651,3.566635,-7.315559,-4.847170,0.706474,4.286287,0.267637,-8.003167,0.852672,5.878345,-8.462549,0.770549,7.709230,2.388916,-8.764276,0.878061,-0.040160,3.381224,-9.986023,1.118424,1.396191,4.697300,-8.172113,6.607938,-0.287765,1.665733,-1.587193,2.137801,-3.614776,-9.807216,2.527551,6.655868,-1.956155,-3.497649,-2.995479,-2.913876,9.608496,-2.845253,0.399711,7.672967,9.160469,-3.700941,-3.238248,6.082292,-2.227086,6.149091,2.634863,-2.321464,6.070618,-6.594428,-8.123771,-8.806091,-0.660392,4.632142,-1.123684,-6.425500,-4.721532,3.189845,-8.612167,1.980895,-9.206749,-3.672724,4.964627,5.757633,5.021817,3.159243,-2.280607,5.550423,-0.449955,8.474498,-8.394948,-5.134310,-0.653849,9.566281,-0.712945,-3.133974,2.590680,-9.662686,6.394124,0.302526,5.038151,-9.622204,-3.697213,8.471519,3.949006,-6.350473,-9.377982,-5.631963,-2.745985,5.724518,-2.231523,-1.614304,-7.598095,-3.136394,-2.615691,-5.037478,-8.788599,-1.156452,7.732209,-0.536893,-2.723072,-1.726199,0.036090,7.641437,-8.119332,8.771186,-9.894490,-9.694152,-0.059357,-1.319075,-8.717000,2.503558,-7.999731,-9.725822,8.762376,-6.436544,0.376504,-7.683008,4.985055,-0.839036,-9.085873,-9.786410,8.825737,7.245526,2.838307,4.929546,-7.950022,6.258930,-2.001518,-5.424947,-0.348573,8.728190,7.574067,-6.818518,4.801467,-4.128195,-5.471449,4.555497,6.217106,-1.226091,-0.397984,0.249733,-7.698401,8.595399,-1.396542,-8.257680,-7.088603,-3.333045,7.547308,-6.617171,3.542357,-7.443199,6.235429,-2.241834,-6.107421,-6.732691,-2.537213,2.810641,-3.393339,9.828101,6.911701,4.640310,2.988454,9.003707,-5.087232,0.430857,4.458836,-3.784382,5.375316,9.563927,8.273393,7.341480,2.982061,-0.333812,4.882087,-1.141825,6.315827,3.751161,3.017970], dtype = "float32")#candidate|4314|(528,)|const|float32
call_4312 = relay.TupleGetItem(func_2842_call(relay.reshape(var_4313.astype('float32'), [10, 5, 9]), relay.reshape(const_4314.astype('float32'), [528,]), relay.reshape(var_4313.astype('float32'), [10, 5, 9]), ), 6)
call_4315 = relay.TupleGetItem(func_2847_call(relay.reshape(var_4313.astype('float32'), [10, 5, 9]), relay.reshape(const_4314.astype('float32'), [528,]), relay.reshape(var_4313.astype('float32'), [10, 5, 9]), ), 6)
func_2536_call = mod.get_global_var('func_2536')
func_2539_call = mutated_mod.get_global_var('func_2539')
const_4321 = relay.const([[2.910974,1.375133,-9.729778,9.123060,-5.272893,0.808468,0.328248,-0.545034,8.047941,-0.373614,5.206152,-0.952174,-7.582385,-3.515831,-8.475662,-5.116911,5.982733,5.396210,0.265384,-6.293240,-2.648094,-6.002358,-4.387099,-1.375366,-1.812450,-9.379890,-6.487452,-6.860187,8.898944,1.160756,7.895626,1.328446,9.111914,8.489490,6.535482,-3.139255,9.062846,7.202481,0.615851,-0.675335,-8.188523,8.447647,7.138396,7.970473,-3.209844,-5.300193,-1.859252,-1.423252,3.532961,1.589390,-2.708050,-5.480523,-8.269927,2.992460,9.287456,9.716464],[4.181771,-6.036481,-0.238397,7.922384,9.041886,2.321744,8.445981,9.537546,5.515254,-6.409014,0.165357,8.680072,-8.192452,3.220341,-5.669210,-6.264665,-0.766233,-0.126185,-0.509415,8.186855,-5.779310,-4.085208,2.501248,-2.093613,-9.550724,-3.691942,5.572050,3.603322,-7.046650,-4.365000,8.039809,-8.550246,2.223149,0.453659,-9.562718,5.646947,4.933152,2.084532,-3.339410,9.188841,-0.453415,-8.240315,0.615961,4.719001,-3.671070,1.137096,-1.432417,4.681777,-1.343892,-2.639556,-1.262873,1.277077,3.135861,-2.272899,-4.068052,-0.147170]], dtype = "float64")#candidate|4321|(2, 56)|const|float64
call_4320 = relay.TupleGetItem(func_2536_call(relay.reshape(const_4321.astype('float64'), [16, 1, 7])), 0)
call_4322 = relay.TupleGetItem(func_2539_call(relay.reshape(const_4321.astype('float64'), [16, 1, 7])), 0)
output = relay.Tuple([bop_4297,call_4312,var_4313,const_4314,call_4320,const_4321,])
output2 = relay.Tuple([bop_4297,call_4315,var_4313,const_4314,call_4322,const_4321,])
func_4325 = relay.Function([var_4295,var_4296,var_4313,], output)
mod['func_4325'] = func_4325
mod = relay.transform.InferType()(mod)
var_4326 = relay.var("var_4326", dtype = "uint32", shape = ())#candidate|4326|()|var|uint32
var_4327 = relay.var("var_4327", dtype = "uint32", shape = (10, 2, 15))#candidate|4327|(10, 2, 15)|var|uint32
var_4328 = relay.var("var_4328", dtype = "float32", shape = (450,))#candidate|4328|(450,)|var|float32
output = func_4325(var_4326,var_4327,var_4328,)
func_4329 = relay.Function([var_4326,var_4327,var_4328,], output)
mutated_mod['func_4329'] = func_4329
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4402 = relay.var("var_4402", dtype = "float32", shape = (3, 16, 2))#candidate|4402|(3, 16, 2)|var|float32
uop_4403 = relay.acosh(var_4402.astype('float32')) # shape=(3, 16, 2)
output = uop_4403
output2 = uop_4403
func_4406 = relay.Function([var_4402,], output)
mod['func_4406'] = func_4406
mod = relay.transform.InferType()(mod)
mutated_mod['func_4406'] = func_4406
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4407 = relay.var("var_4407", dtype = "float32", shape = (3, 16, 2))#candidate|4407|(3, 16, 2)|var|float32
func_4406_call = mutated_mod.get_global_var('func_4406')
call_4408 = func_4406_call(var_4407)
output = call_4408
func_4409 = relay.Function([var_4407], output)
mutated_mod['func_4409'] = func_4409
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4528 = relay.var("var_4528", dtype = "float32", shape = (9, 8, 5))#candidate|4528|(9, 8, 5)|var|float32
uop_4529 = relay.log10(var_4528.astype('float32')) # shape=(9, 8, 5)
func_3856_call = mod.get_global_var('func_3856')
func_3859_call = mutated_mod.get_global_var('func_3859')
var_4552 = relay.var("var_4552", dtype = "uint16", shape = (495,))#candidate|4552|(495,)|var|uint16
call_4551 = relay.TupleGetItem(func_3856_call(relay.reshape(var_4552.astype('uint16'), [11, 15, 3])), 1)
call_4553 = relay.TupleGetItem(func_3859_call(relay.reshape(var_4552.astype('uint16'), [11, 15, 3])), 1)
func_1576_call = mod.get_global_var('func_1576')
func_1579_call = mutated_mod.get_global_var('func_1579')
const_4570 = relay.const([3.658368,5.350516,-4.646546,0.971294,9.121798,9.070641,-6.026070,5.225750,5.488304,-8.298349,-9.502721,-8.798197,1.091328,9.278306,-2.304729,8.121856,-3.033975,-2.907167,-9.572124,2.028456,5.045384,-5.572150,-4.996172,-9.805886,-0.279286,-4.853356,-1.015609,3.099712,5.985993,-4.488795,0.049302,-8.334016,-5.449711,-5.286376,-6.313153,-3.953553,-9.392638,1.163363,-5.123793,-7.168088], dtype = "float32")#candidate|4570|(40,)|const|float32
call_4569 = func_1576_call(relay.reshape(const_4570.astype('float32'), [2, 2, 10]))
call_4571 = func_1576_call(relay.reshape(const_4570.astype('float32'), [2, 2, 10]))
const_4585 = relay.const([[[2.873105,0.718420,5.792008,7.600933,-5.073392],[6.941012,-2.768024,3.367921,-2.251270,-7.590776],[6.909431,-3.290719,1.567894,6.317643,-9.392941],[5.911834,-7.655573,1.809172,0.692484,-5.357441],[5.871454,9.849859,2.591960,1.248493,2.645888],[-7.434133,5.333122,-1.085165,-9.936268,-2.517077],[0.299515,-9.100990,-6.186453,9.874121,0.650911],[5.882320,7.643647,-2.164442,7.229176,-7.528346]],[[9.987354,-8.721080,-5.621431,6.788180,-1.499539],[6.360288,-2.687390,-5.264224,3.567393,-2.594705],[3.091679,-2.432199,-6.385086,-9.970226,-5.921362],[-9.218198,3.242035,-7.721980,8.129943,4.541575],[2.769993,7.416385,-0.879967,-4.110956,7.172977],[-8.035901,-7.682497,-8.370135,9.676796,5.698156],[3.962609,9.952213,-7.531749,-2.502668,-0.451064],[3.011452,-0.273736,5.741916,-8.672013,5.159576]],[[-7.625896,1.568148,-8.811623,3.181648,-1.367104],[1.167250,-0.163269,-6.466511,-2.577470,-7.073032],[-4.159666,-3.897877,6.730383,-8.805856,4.400734],[1.458185,1.880630,-2.721690,-9.354488,-4.752319],[-9.695377,9.253508,-9.444447,2.282452,-8.193682],[8.027509,-3.659523,-8.753086,5.570801,7.006400],[-6.251368,-0.782379,4.583461,2.072294,-5.376148],[-2.246259,9.915683,7.574594,-2.832984,-8.512262]],[[5.176854,0.167732,3.907441,9.835000,-0.101533],[3.270662,1.036074,8.019720,-3.329959,1.634282],[-0.351239,-7.044111,5.714673,1.898636,-8.839945],[-2.474099,-8.099696,5.444343,6.622768,-0.373550],[-1.781088,-2.383455,-3.342497,-4.492612,-1.472489],[8.398998,-5.471138,-1.585915,-7.470592,5.201997],[9.981250,-2.414812,4.021329,2.406370,-4.353532],[9.560438,3.863681,-7.396501,4.143522,8.746889]],[[-7.411942,-8.700008,-7.466629,-1.849624,-1.577476],[7.621477,-1.064427,9.974717,-8.605159,-3.707738],[2.957859,3.087936,-3.246744,-5.911371,-4.682003],[8.400812,-1.573650,8.534431,8.223185,6.374882],[9.674163,3.585072,-9.434388,-3.387187,-2.822078],[2.549694,-0.119133,-4.389891,9.949639,-4.943851],[-7.957583,-4.133415,5.275617,0.058790,-5.491216],[-3.966765,-5.964958,2.558024,1.516572,8.387179]],[[-5.316747,8.903212,7.129744,0.429605,-0.834795],[-6.131034,-9.811824,2.292249,4.016391,-5.199553],[-6.904693,4.438125,-7.372645,7.799324,-4.666239],[3.103090,-6.182935,7.929259,7.620174,-5.817835],[-2.773408,-6.649793,6.261345,-9.898212,2.452735],[-0.614202,-0.737864,-6.414458,-0.396648,-0.114152],[-6.810117,-8.235349,-2.911454,-6.012603,-6.315564],[9.792023,5.118208,4.981303,1.165526,0.700631]],[[-1.398896,-2.698626,-5.554069,-4.777301,8.848112],[1.016302,-1.462394,-3.398500,-1.668890,-4.579770],[4.719384,4.159329,-6.429181,8.057194,3.018368],[-8.315367,1.493861,-7.478265,5.066477,-8.696518],[7.759071,-5.686846,0.990535,-8.940402,3.232139],[3.884635,-5.419042,4.581245,8.288645,-2.149717],[-2.326311,9.404056,-3.623181,4.225602,-6.561287],[-3.649367,7.178870,6.158723,0.783143,-2.774802]],[[4.281809,8.665272,9.812945,-4.017847,6.535677],[1.684462,5.259551,2.032666,-8.365826,2.606986],[6.587619,-4.227368,-9.143791,4.453406,2.261262],[-3.106073,7.623168,-3.057137,-3.418368,-7.228165],[4.440298,7.316666,-2.888682,-1.927468,5.955514],[0.743747,3.649476,-3.400453,8.775733,3.137546],[9.359064,0.768507,3.377697,9.758640,-1.910827],[-9.361896,7.517607,-3.208036,-6.133042,-9.160877]],[[-3.687894,-9.240450,5.749463,9.543064,7.325693],[5.274236,-7.860581,0.057962,-1.771500,-9.987105],[-7.064921,6.674192,-2.311781,5.089656,-2.110886],[3.324190,3.238366,9.955850,-8.562727,-0.701397],[3.328921,-9.213629,-2.531778,-4.369267,6.487784],[-7.801231,2.461917,6.950371,8.279184,-2.421572],[5.646482,7.634829,-9.993866,7.365054,7.741733],[-0.117106,-5.371797,9.007771,-4.244427,9.359307]]], dtype = "float32")#candidate|4585|(9, 8, 5)|const|float32
bop_4586 = relay.minimum(uop_4529.astype('int64'), relay.reshape(const_4585.astype('int64'), relay.shape_of(uop_4529))) # shape=(9, 8, 5)
func_3501_call = mod.get_global_var('func_3501')
func_3504_call = mutated_mod.get_global_var('func_3504')
var_4590 = relay.var("var_4590", dtype = "float32", shape = (308,))#candidate|4590|(308,)|var|float32
call_4589 = relay.TupleGetItem(func_3501_call(relay.reshape(var_4590.astype('float32'), [308, 1])), 1)
call_4591 = relay.TupleGetItem(func_3504_call(relay.reshape(var_4590.astype('float32'), [308, 1])), 1)
output = relay.Tuple([call_4551,var_4552,call_4569,const_4570,bop_4586,call_4589,var_4590,])
output2 = relay.Tuple([call_4553,var_4552,call_4571,const_4570,bop_4586,call_4591,var_4590,])
func_4593 = relay.Function([var_4528,var_4552,var_4590,], output)
mod['func_4593'] = func_4593
mod = relay.transform.InferType()(mod)
mutated_mod['func_4593'] = func_4593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4593_call = mutated_mod.get_global_var('func_4593')
var_4595 = relay.var("var_4595", dtype = "float32", shape = (9, 8, 5))#candidate|4595|(9, 8, 5)|var|float32
var_4596 = relay.var("var_4596", dtype = "uint16", shape = (495,))#candidate|4596|(495,)|var|uint16
var_4597 = relay.var("var_4597", dtype = "float32", shape = (308,))#candidate|4597|(308,)|var|float32
call_4594 = func_4593_call(var_4595,var_4596,var_4597,)
output = call_4594
func_4598 = relay.Function([var_4595,var_4596,var_4597,], output)
mutated_mod['func_4598'] = func_4598
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4624 = relay.var("var_4624", dtype = "float64", shape = (13, 11, 1))#candidate|4624|(13, 11, 1)|var|float64
var_4625 = relay.var("var_4625", dtype = "float64", shape = (13, 11, 15))#candidate|4625|(13, 11, 15)|var|float64
bop_4626 = relay.floor_divide(var_4624.astype('float64'), var_4625.astype('float64')) # shape=(13, 11, 15)
output = relay.Tuple([bop_4626,])
output2 = relay.Tuple([bop_4626,])
func_4631 = relay.Function([var_4624,var_4625,], output)
mod['func_4631'] = func_4631
mod = relay.transform.InferType()(mod)
var_4632 = relay.var("var_4632", dtype = "float64", shape = (13, 11, 1))#candidate|4632|(13, 11, 1)|var|float64
var_4633 = relay.var("var_4633", dtype = "float64", shape = (13, 11, 15))#candidate|4633|(13, 11, 15)|var|float64
output = func_4631(var_4632,var_4633,)
func_4634 = relay.Function([var_4632,var_4633,], output)
mutated_mod['func_4634'] = func_4634
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4970 = relay.var("var_4970", dtype = "float32", shape = (5, 12, 3))#candidate|4970|(5, 12, 3)|var|float32
var_4971 = relay.var("var_4971", dtype = "float32", shape = (5, 12, 3))#candidate|4971|(5, 12, 3)|var|float32
bop_4972 = relay.mod(var_4970.astype('float32'), relay.reshape(var_4971.astype('float32'), relay.shape_of(var_4970))) # shape=(5, 12, 3)
output = bop_4972
output2 = bop_4972
func_4987 = relay.Function([var_4970,var_4971,], output)
mod['func_4987'] = func_4987
mod = relay.transform.InferType()(mod)
mutated_mod['func_4987'] = func_4987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4987_call = mutated_mod.get_global_var('func_4987')
var_4989 = relay.var("var_4989", dtype = "float32", shape = (5, 12, 3))#candidate|4989|(5, 12, 3)|var|float32
var_4990 = relay.var("var_4990", dtype = "float32", shape = (5, 12, 3))#candidate|4990|(5, 12, 3)|var|float32
call_4988 = func_4987_call(var_4989,var_4990,)
output = call_4988
func_4991 = relay.Function([var_4989,var_4990,], output)
mutated_mod['func_4991'] = func_4991
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5108 = relay.var("var_5108", dtype = "int64", shape = ())#candidate|5108|()|var|int64
var_5109 = relay.var("var_5109", dtype = "int64", shape = (4, 9, 1))#candidate|5109|(4, 9, 1)|var|int64
bop_5110 = relay.bitwise_and(var_5108.astype('int64'), var_5109.astype('int64')) # shape=(4, 9, 1)
func_3856_call = mod.get_global_var('func_3856')
func_3859_call = mutated_mod.get_global_var('func_3859')
const_5115 = relay.const([-4,-4,6,-3,-10,6,-10,-6,-4,-10,1,8,6,-7,7,-8,8,5,-2,2,9,-10,1,-3,5,7,5,-3,7,4,5,-6,-6,9,-7,7,-1,7,3,8,-3,-3,2,-9,-8,-4,7,-8,-9,8,-1,4,-2,-3,-2,4,-4,6,-4,5,-10,-7,-7,9,-5,3,-1,-6,-7,9,-8,7,-1,7,7,-9,3,3,2,-5,8,1,-5,4,5,-3,8,4,2,7,5,6,4,7,3,3,10,-3,-2,-6,2,-8,9,2,-5,-1,-6,8,10,6,-7,-9,4,1,8,-10,1,3,-2,-1,5,-7,3,-1,-1,8,-7,-7,8,-6,7,9,6,8,-6,-4,5,1,7,10,-10,-7,5,5,-4,-10,-7,-1,-10,10,9,6,-5,1,1,-1,-10,-6,-4,6,4,-9,6,5,-10,-3,-8,5,8,-7,-7,-7,-7,-10,6,9,4,2,-9,-8,-1,-9,10,4,10,-6,-8,-4,10,7,1,-5,-5,7,-5,2,5,-4,-5,-6,10,2,7,-4,-9,2,-7,5,7,6,6,-7,-1,-10,1,-3,-8,-8,2,-3,-3,1,3,1,-9,-9,9,7,-8,8,3,-8,-10,-7,8,-3,4,-8,3,6,-10,-8,10,1,-2,-7,2,-7,2,5,1,-9,-4,-1,-10,-9,-1,-9,2,-1,9,-1,-3,-1,2,3,4,10,10,-6,-10,1,10,2,-8,-8,1,7,-8,9,6,7,5,-9,1,-7,10,2,-10,2,9,4,-9,-6,-1,1,6,-9,-7,9,-6,1,-6,6,9,-3,-7,-10,10,-5,10,10,6,-10,2,3,6,1,-6,6,-4,6,6,10,-4,8,-3,-2,2,1,1,-9,7,7,-9,-1,-3,-6,4,6,-5,4,7,-8,-9,-10,-5,5,10,-7,6,2,6,-8,-8,-10,3,10,1,-6,8,-1,4,5,10,3,-10,5,4,6,-2,-4,4,2,1,8,-3,-2,-6,2,-7,-2,-1,2,-4,9,9,-10,7,-10,9,10,8,-10,-1,8,9,-6,9,-10,-8,-9,-2,2,1,2,10,4,5,2,-8,3,-2,-10,9,-6,-8,-6,3,2,7,-4,7,7,-1,8,-1,7,-2,-4,6,7,-4,4,8,3,-1,6,-6,8,4,-7,10,8,-2,2,4,-1,4,-8,-3,-2,10,10,3,-3,7,1,5,-9,4,8,3,-8,7,9,-9,-4,-7,4,4,8,-7,-7,10,3,7,4,1,5,2,-5,5,9,-4,3,-10,9,9,2,-4,-3,-4,-1,3], dtype = "uint16")#candidate|5115|(495,)|const|uint16
call_5114 = relay.TupleGetItem(func_3856_call(relay.reshape(const_5115.astype('uint16'), [11, 15, 3])), 2)
call_5116 = relay.TupleGetItem(func_3859_call(relay.reshape(const_5115.astype('uint16'), [11, 15, 3])), 2)
bop_5124 = relay.logical_and(call_5114.astype('bool'), var_5108.astype('bool')) # shape=(450,)
bop_5127 = relay.logical_and(call_5116.astype('bool'), var_5108.astype('bool')) # shape=(450,)
output = relay.Tuple([bop_5110,const_5115,bop_5124,])
output2 = relay.Tuple([bop_5110,const_5115,bop_5127,])
func_5128 = relay.Function([var_5108,var_5109,], output)
mod['func_5128'] = func_5128
mod = relay.transform.InferType()(mod)
mutated_mod['func_5128'] = func_5128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5128_call = mutated_mod.get_global_var('func_5128')
var_5130 = relay.var("var_5130", dtype = "int64", shape = ())#candidate|5130|()|var|int64
var_5131 = relay.var("var_5131", dtype = "int64", shape = (4, 9, 1))#candidate|5131|(4, 9, 1)|var|int64
call_5129 = func_5128_call(var_5130,var_5131,)
output = call_5129
func_5132 = relay.Function([var_5130,var_5131,], output)
mutated_mod['func_5132'] = func_5132
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5153 = relay.const([[[-5.789413,1.354518,-7.708510,-9.343168,0.872238,-7.946458,-4.072199,4.414798,-4.757255,6.981851,2.486018,2.471649,8.639308,-0.233688,8.175387],[-1.890077,-5.204290,-3.584195,7.385100,-8.993679,-7.306746,9.716534,-0.132402,-8.829088,6.513536,7.487498,8.109485,-2.092247,-6.863440,-2.384022],[-8.519671,5.813895,-7.537724,-2.295350,-8.210775,-2.233994,9.254559,7.279177,2.407893,-6.925506,0.793700,0.035488,-0.214265,-6.326353,-9.884462],[-8.551947,5.869392,0.495660,-9.881701,-8.358720,8.659255,6.627327,-2.509546,-5.348543,-9.426669,8.359563,-2.042235,5.633164,-6.049844,0.778799],[-6.142524,8.834197,2.336007,4.569780,-3.842426,-1.294104,5.424696,-0.190577,-3.151682,0.094898,-6.112748,6.010603,0.099962,7.869577,-8.300442],[9.338029,9.007736,-7.381644,4.638941,-8.314365,0.011971,5.136260,-7.241491,4.845309,-0.581387,-6.247145,3.477011,9.660788,-6.951284,-7.766329],[8.246714,6.079548,-1.093336,1.102639,9.436552,-7.739807,-5.255639,2.987945,6.452886,-5.982026,6.115115,-6.893480,-1.756442,-8.321660,2.557878],[2.935382,-1.410023,9.352623,-3.935014,-6.389090,-6.051022,6.592322,4.590085,0.269857,5.618023,-3.711670,-6.133897,6.659049,6.951113,8.026164],[-3.286703,2.227010,1.133536,8.002141,-5.430030,-0.950028,-6.594890,2.888971,-7.322844,2.982685,-1.579818,5.027323,-9.950120,8.202325,-3.981661],[-0.533860,9.241406,4.637734,-5.331615,2.069340,-6.748474,6.000265,3.508677,-6.498404,-6.133336,8.420492,-8.517741,6.063332,9.327847,-0.447872],[-1.788672,-3.004819,-7.780402,-3.212752,-5.307035,6.096820,5.364482,-0.046111,-4.704997,4.477033,-2.798004,5.600465,2.281930,9.261994,-1.792016],[-7.592574,9.317782,-2.083695,-7.265083,-0.735184,-4.273709,8.364583,4.319357,-3.613253,4.677105,-4.046641,-2.542376,-6.678595,-1.406073,-8.607174]]], dtype = "float32")#candidate|5153|(1, 12, 15)|const|float32
uop_5154 = relay.asinh(const_5153.astype('float32')) # shape=(1, 12, 15)
output = uop_5154
output2 = uop_5154
func_5156 = relay.Function([], output)
mod['func_5156'] = func_5156
mod = relay.transform.InferType()(mod)
output = func_5156()
func_5157 = relay.Function([], output)
mutated_mod['func_5157'] = func_5157
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5156_call = mod.get_global_var('func_5156')
func_5157_call = mutated_mod.get_global_var('func_5157')
call_5158 = func_5156_call()
call_5159 = func_5156_call()
output = relay.Tuple([call_5158,])
output2 = relay.Tuple([call_5159,])
func_5164 = relay.Function([], output)
mod['func_5164'] = func_5164
mod = relay.transform.InferType()(mod)
mutated_mod['func_5164'] = func_5164
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5164_call = mutated_mod.get_global_var('func_5164')
call_5165 = func_5164_call()
output = call_5165
func_5166 = relay.Function([], output)
mutated_mod['func_5166'] = func_5166
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5156_call = mod.get_global_var('func_5156')
func_5157_call = mutated_mod.get_global_var('func_5157')
call_5175 = func_5156_call()
call_5176 = func_5156_call()
func_3213_call = mod.get_global_var('func_3213')
func_3215_call = mutated_mod.get_global_var('func_3215')
var_5182 = relay.var("var_5182", dtype = "uint32", shape = (1125,))#candidate|5182|(1125,)|var|uint32
call_5181 = func_3213_call(relay.reshape(var_5182.astype('uint32'), [15, 5, 15]))
call_5183 = func_3213_call(relay.reshape(var_5182.astype('uint32'), [15, 5, 15]))
output = relay.Tuple([call_5175,call_5181,var_5182,])
output2 = relay.Tuple([call_5176,call_5183,var_5182,])
func_5185 = relay.Function([var_5182,], output)
mod['func_5185'] = func_5185
mod = relay.transform.InferType()(mod)
var_5186 = relay.var("var_5186", dtype = "uint32", shape = (1125,))#candidate|5186|(1125,)|var|uint32
output = func_5185(var_5186)
func_5187 = relay.Function([var_5186], output)
mutated_mod['func_5187'] = func_5187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5156_call = mod.get_global_var('func_5156')
func_5157_call = mutated_mod.get_global_var('func_5157')
call_5206 = func_5156_call()
call_5207 = func_5156_call()
func_1576_call = mod.get_global_var('func_1576')
func_1579_call = mutated_mod.get_global_var('func_1579')
const_5209 = relay.const([-9.186435,-1.109447,-2.575586,-0.412337,-5.899183,8.019763,-9.458294,-5.891235,9.772301,-6.727841,7.327354,7.961168,-3.385631,3.935460,-6.766890,2.266483,7.974290,6.430666,8.579532,-9.597300,-8.108884,-7.434472,5.226743,-2.117155,-6.086033,0.055397,3.832284,7.001559,2.761580,3.969046,-2.363126,-3.579319,-6.506947,9.365055,-3.412365,5.152557,0.041278,9.897395,-2.921544,-2.845772], dtype = "float32")#candidate|5209|(40,)|const|float32
call_5208 = func_1576_call(relay.reshape(const_5209.astype('float32'), [2, 2, 10]))
call_5210 = func_1576_call(relay.reshape(const_5209.astype('float32'), [2, 2, 10]))
uop_5250 = relay.atanh(call_5206.astype('float64')) # shape=(1, 12, 15)
uop_5252 = relay.atanh(call_5207.astype('float64')) # shape=(1, 12, 15)
uop_5253 = relay.log2(call_5206.astype('float32')) # shape=(1, 12, 15)
uop_5255 = relay.log2(call_5207.astype('float32')) # shape=(1, 12, 15)
func_5128_call = mod.get_global_var('func_5128')
func_5132_call = mutated_mod.get_global_var('func_5132')
const_5262 = relay.const(-9, dtype = "int64")#candidate|5262|()|const|int64
var_5263 = relay.var("var_5263", dtype = "int64", shape = (36,))#candidate|5263|(36,)|var|int64
call_5261 = relay.TupleGetItem(func_5128_call(relay.reshape(const_5262.astype('int64'), []), relay.reshape(var_5263.astype('int64'), [4, 9, 1]), ), 2)
call_5264 = relay.TupleGetItem(func_5132_call(relay.reshape(const_5262.astype('int64'), []), relay.reshape(var_5263.astype('int64'), [4, 9, 1]), ), 2)
func_1576_call = mod.get_global_var('func_1576')
func_1579_call = mutated_mod.get_global_var('func_1579')
call_5265 = func_1576_call(relay.reshape(call_5208.astype('float32'), [2, 2, 10]))
call_5266 = func_1576_call(relay.reshape(call_5208.astype('float32'), [2, 2, 10]))
func_3856_call = mod.get_global_var('func_3856')
func_3859_call = mutated_mod.get_global_var('func_3859')
var_5274 = relay.var("var_5274", dtype = "uint16", shape = (495,))#candidate|5274|(495,)|var|uint16
call_5273 = relay.TupleGetItem(func_3856_call(relay.reshape(var_5274.astype('uint16'), [11, 15, 3])), 3)
call_5275 = relay.TupleGetItem(func_3859_call(relay.reshape(var_5274.astype('uint16'), [11, 15, 3])), 3)
output = relay.Tuple([call_5208,const_5209,uop_5250,uop_5253,call_5261,const_5262,var_5263,call_5265,call_5273,var_5274,])
output2 = relay.Tuple([call_5210,const_5209,uop_5252,uop_5255,call_5264,const_5262,var_5263,call_5266,call_5275,var_5274,])
func_5278 = relay.Function([var_5263,var_5274,], output)
mod['func_5278'] = func_5278
mod = relay.transform.InferType()(mod)
mutated_mod['func_5278'] = func_5278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5278_call = mutated_mod.get_global_var('func_5278')
var_5280 = relay.var("var_5280", dtype = "int64", shape = (36,))#candidate|5280|(36,)|var|int64
var_5281 = relay.var("var_5281", dtype = "uint16", shape = (495,))#candidate|5281|(495,)|var|uint16
call_5279 = func_5278_call(var_5280,var_5281,)
output = call_5279
func_5282 = relay.Function([var_5280,var_5281,], output)
mutated_mod['func_5282'] = func_5282
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5359 = relay.var("var_5359", dtype = "uint32", shape = (11, 5, 1))#candidate|5359|(11, 5, 1)|var|uint32
var_5360 = relay.var("var_5360", dtype = "uint32", shape = (11, 5, 7))#candidate|5360|(11, 5, 7)|var|uint32
bop_5361 = relay.right_shift(var_5359.astype('uint32'), var_5360.astype('uint32')) # shape=(11, 5, 7)
func_4987_call = mod.get_global_var('func_4987')
func_4991_call = mutated_mod.get_global_var('func_4991')
var_5367 = relay.var("var_5367", dtype = "float32", shape = (30, 6))#candidate|5367|(30, 6)|var|float32
call_5366 = func_4987_call(relay.reshape(var_5367.astype('float32'), [5, 12, 3]), relay.reshape(var_5367.astype('float32'), [5, 12, 3]), )
call_5368 = func_4987_call(relay.reshape(var_5367.astype('float32'), [5, 12, 3]), relay.reshape(var_5367.astype('float32'), [5, 12, 3]), )
func_4003_call = mod.get_global_var('func_4003')
func_4006_call = mutated_mod.get_global_var('func_4006')
const_5374 = relay.const(9, dtype = "int64")#candidate|5374|()|const|int64
const_5375 = relay.const([-2,8,-5,-5,7,-4,-4,3,-2,-10,1,3,-9,1,8,-6,9,4,-5,2,2,2,-4,7,1,-10,-3,6,-4,1,-4,-4,3,6,6,9,-6,6,-5,-8,10,9,-1,-7,-1,-4,-5,10,6,-5,6,2,2,1,-1,-4,-7,4,7,2,2,-4,6,-5,10,7,-2,5,7,3,-9,8,-9,3,-6,5,2,-4,-1,-1,7,-4,-6,-6,9,8,-6,1,1,-3,-10,4,6,-10,-5,6,6,-2,1,5,7,5,10,-9,1,-7,-10,4,-6,-3,-3,2,10,-4,-2,-10,-2,2,-2,-2,-5,-5,7,1,4,-2,-2,8,10,3,-1,-1,-8,3,-8,-5,4,-7,9,-2,-1,-2,3,-5,2,-5,2,3,2,2,-3,-10,6,7,5,-10,8,-9,10,1,3,4,-3,9,-5,3,7,6,-1,1,-4,2,3,-2,5,-6,1,-6,-8,-2,-6,-2,10,-6,-3,-9,-8,-1,-10,5,-8,6,10,6,6,1,-2,-5,-5,5,8,6,-5,-8,-2,2,1,-9,-9,8,-4,-7,4,-1,3,-8,10,-10,1,-1,10,-2,1,-3,-10,-8,-10,1,7,4,7,-2,5,3,-9,-10,-10,-9,6,3,-2,10,-4,-7,-10,2,2,6,5,3,8,2,-8,8,2,1,10,8,-2,-6,6,2,1,7,-9,-1,-6,4,-3,-9,4,1,-1,2,3,-6,8,-9,7,-7,8,3,1,9,2,3,6,-1,-2,-10,1,-6,-3,-7,2,-7,4,-6,9,-10,-1,-8,6,6,2,-3,-2,-1,-5,-5,6,7,4,-6,-9,8,1,9,-3,5,2,8,6,-1,10,8,-10,6,10,-8,8,3,2,-7,8,10,-10,4,-8,9,-10,3,-5,3,1,-6,-9,-10,-10,6,9,-8,4,6,-6,1,-3,-6,-3,4,2,5,-1,-10,2,-1,-2,9,-2,10,-2,-5,-5,-5,-2,4,-1,3,4,4,-1,-6,-3,-1,-9,-4,9,-8,-2,5,-2,-8,-8,6,6,9,-3,2,-9,5,-3,-9,-10,-9,7,-8,4,1,-7,-5,7,4,-8,-7,9,-5,3,-9,10,-7,3,-6,-1,9,6,-3,-10,2,-3,-7,3,9,5,-8,5,3,-1,6,-8,2,-9,-6,1,-8,-8,-1,6,-4,-7,7,-8,-1,-9,-2,2,-2,8,1,-7,8,-2,4,-8,-9,3,-6,-6,1,-3,-4,-7,-5,6,8,3,-9,-4,2,-3,4,7,-6,-6,8,-10,-4,9,-3,5,8,-7,2,-10,-3,5,9,-9,5,-10,5,-5,6,-8,1,-10,1,8,1,8,-10,-3,-5,4,10,-2,3,-5,1,7,7,1,-7,1,-6,1,-4,-7,-9,-8,4,-5,7,-7,5,10,-3,10,-1,-7,-2,5,5,6,10,4,-5,-10,-10,3,-10,9,-4,-5,-2,2,-3,1,-8,3,-2,-1,-9,-9,7,-6,5,-2,4,5,-10,-1,5,-10,-10,2,-1,7,5,8,-10,-1,-10,5,10,2,-9,10,7,-9,-2,-7,4,-10,-3,-1,5,-7,4,-10,2,-4,-9,6,-4,-2,-6,9,4,8,-2,-10,10,-3,-9,-9,-9,5,7,1,-8,8,-4,3,8,5,10,-8,-3,3,6,-7,4,10,-3,3,-3,-5,-9,5,10,9,7,8,-6,4,-4,-6,2,8,-6,5,1,8,-8,7,-5,8,4,4,1,-4,8,1,-4,5,9,9,10,2,-10,-6,7,-7,-1,1,-8,7,2,7,-7,6,-2,10,4,-2,10,9,3,8,-8,6,-3,5,-10,-1,-7,-7,-4,3,-8,10,2,-5,9,10,2,5,-8,-1,3,7,9,-10,-2,10,-7,-8,-2,-5,8,-8,1,6,-4,-2,-8,-8,5,-1,1,7,-2,9,9,6,-9,-8,10,4,10,2,4,-5,5,4,-5,-4,-5,4,-6,1,-7,-10,4,2,7,-2,-3,8,10,6,4,-6,-2,4,3,7,-6,-8,8,-4,5,6,2,-5,-7,-10,2,3,-8,-4,-4,-10,8,3,-9,1,-3,-1,-10,-7,-7,9,7,-5,-8,-6,2,5,6,-5,6,-9,4,4,-4,2,-2,-5,4,-3,-9,-7,7,-10,-1,-7,5,-8,4,3,-6,3,8,6,6,-6,-10,-7,-6,-9,-3,6,10,7,7,-4,-4,9,-3,-4,6,-5,3,-5,-8,-8,1,-9,7,5,-5,-4,-3,3,-10,6,-8,-6,10,2,6,-9,3,7,5,5,-10,10,-4,1,1,1,6,-2,9,-6,-5,1,4,-9,10,8,-5,-3,-3,-2,-10,6,4,-6,-4,-9,9,9,8,4,-2,-9,-3,5,-7,-2,3,4,-8,10,5,10,-9,-7,7,-6,6,-7,8,-6,-10,-1,-6,2,-5,5,2,-4,-4,-10,4,3,1,-10,-3,-1,3,-8,7,3,2,2,1,5,-8,-10,10,2,-3,-8,7,9,-1,10,-7,-10,9,1,9,-7,10,7,9,1,2,-8,1,10,2,-2,3,8,-7,1,-6,2,6,-7,-1,-8,-10,-5,-4,6,6,-5,-3,8,1,-5,8,4,-7,2,9,-2,-6,1,1,-6,-7,-4,5,10,1,-4,1,4,8,7,-6,6,5,2,7,4,2,-4,-2,-4,8,-2,7,-8,-2,2,-5,9,-8,-9,-2,8,-1,-10,7,-5,-3,5,-7,-5,-9,6,-7,-7,10,9,6,-4,2,-1,-10,-3,7,5,10,-2,8,6,-5,-2,6,4,9,-1,4,9,10,8,-7,-1,6,-9,-1,2,7,-8,-5,6,-2,6,-3,-1,6,-2,6,-3,5,7,-6,-2,4,7,4,-3,2,-4,6,-8,7,-5,-3,3,10,-6,2,-1,-7,6,-2,2,10,-1,-1,7,10,1,2,-1,-6,9,4,4,8,5,-9,-6,-2,5,5,-1,6,8,6,8,-6,-1,7,-2,-7,5,-5,-7,7,10,4,6,-5,-7,6,4,4,-2,3,8,-2,-6,-5,6,4,3,-9,-7,-5,-9,2,3,-1,9,-3,-3,-9,4,1,5,5,-3,-6,3,7,-2,-5,6,-4,-9,-9,1,-1,-3,4,10,-3,6,-7,3,-8,4,-2,9,-5,-2,-1,4,10], dtype = "int64")#candidate|5375|(1200,)|const|int64
call_5373 = relay.TupleGetItem(func_4003_call(relay.reshape(const_5374.astype('int64'), []), relay.reshape(const_5375.astype('int64'), [16, 5, 15]), ), 0)
call_5376 = relay.TupleGetItem(func_4006_call(relay.reshape(const_5374.astype('int64'), []), relay.reshape(const_5375.astype('int64'), [16, 5, 15]), ), 0)
output = relay.Tuple([bop_5361,call_5366,var_5367,call_5373,const_5374,const_5375,])
output2 = relay.Tuple([bop_5361,call_5368,var_5367,call_5376,const_5374,const_5375,])
func_5378 = relay.Function([var_5359,var_5360,var_5367,], output)
mod['func_5378'] = func_5378
mod = relay.transform.InferType()(mod)
var_5379 = relay.var("var_5379", dtype = "uint32", shape = (11, 5, 1))#candidate|5379|(11, 5, 1)|var|uint32
var_5380 = relay.var("var_5380", dtype = "uint32", shape = (11, 5, 7))#candidate|5380|(11, 5, 7)|var|uint32
var_5381 = relay.var("var_5381", dtype = "float32", shape = (30, 6))#candidate|5381|(30, 6)|var|float32
output = func_5378(var_5379,var_5380,var_5381,)
func_5382 = relay.Function([var_5379,var_5380,var_5381,], output)
mutated_mod['func_5382'] = func_5382
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5156_call = mod.get_global_var('func_5156')
func_5157_call = mutated_mod.get_global_var('func_5157')
call_5416 = func_5156_call()
call_5417 = func_5156_call()
output = relay.Tuple([call_5416,])
output2 = relay.Tuple([call_5417,])
func_5418 = relay.Function([], output)
mod['func_5418'] = func_5418
mod = relay.transform.InferType()(mod)
mutated_mod['func_5418'] = func_5418
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5418_call = mutated_mod.get_global_var('func_5418')
call_5419 = func_5418_call()
output = call_5419
func_5420 = relay.Function([], output)
mutated_mod['func_5420'] = func_5420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5156_call = mod.get_global_var('func_5156')
func_5157_call = mutated_mod.get_global_var('func_5157')
call_5459 = func_5156_call()
call_5460 = func_5156_call()
func_2536_call = mod.get_global_var('func_2536')
func_2539_call = mutated_mod.get_global_var('func_2539')
var_5464 = relay.var("var_5464", dtype = "float64", shape = (112, 1))#candidate|5464|(112, 1)|var|float64
call_5463 = relay.TupleGetItem(func_2536_call(relay.reshape(var_5464.astype('float64'), [16, 1, 7])), 0)
call_5465 = relay.TupleGetItem(func_2539_call(relay.reshape(var_5464.astype('float64'), [16, 1, 7])), 0)
output = relay.Tuple([call_5459,call_5463,var_5464,])
output2 = relay.Tuple([call_5460,call_5465,var_5464,])
func_5469 = relay.Function([var_5464,], output)
mod['func_5469'] = func_5469
mod = relay.transform.InferType()(mod)
var_5470 = relay.var("var_5470", dtype = "float64", shape = (112, 1))#candidate|5470|(112, 1)|var|float64
output = func_5469(var_5470)
func_5471 = relay.Function([var_5470], output)
mutated_mod['func_5471'] = func_5471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5164_call = mod.get_global_var('func_5164')
func_5166_call = mutated_mod.get_global_var('func_5166')
call_5485 = relay.TupleGetItem(func_5164_call(), 0)
call_5486 = relay.TupleGetItem(func_5166_call(), 0)
var_5490 = relay.var("var_5490", dtype = "float32", shape = (8, 12, 15))#candidate|5490|(8, 12, 15)|var|float32
bop_5491 = relay.logical_xor(call_5485.astype('uint16'), var_5490.astype('uint16')) # shape=(8, 12, 15)
bop_5494 = relay.logical_xor(call_5486.astype('uint16'), var_5490.astype('uint16')) # shape=(8, 12, 15)
output = relay.Tuple([bop_5491,])
output2 = relay.Tuple([bop_5494,])
func_5504 = relay.Function([var_5490,], output)
mod['func_5504'] = func_5504
mod = relay.transform.InferType()(mod)
var_5505 = relay.var("var_5505", dtype = "float32", shape = (8, 12, 15))#candidate|5505|(8, 12, 15)|var|float32
output = func_5504(var_5505)
func_5506 = relay.Function([var_5505], output)
mutated_mod['func_5506'] = func_5506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5156_call = mod.get_global_var('func_5156')
func_5157_call = mutated_mod.get_global_var('func_5157')
call_5672 = func_5156_call()
call_5673 = func_5156_call()
func_5128_call = mod.get_global_var('func_5128')
func_5132_call = mutated_mod.get_global_var('func_5132')
const_5685 = relay.const(8, dtype = "int64")#candidate|5685|()|const|int64
var_5686 = relay.var("var_5686", dtype = "int64", shape = (9, 4))#candidate|5686|(9, 4)|var|int64
call_5684 = relay.TupleGetItem(func_5128_call(relay.reshape(const_5685.astype('int64'), []), relay.reshape(var_5686.astype('int64'), [4, 9, 1]), ), 0)
call_5687 = relay.TupleGetItem(func_5132_call(relay.reshape(const_5685.astype('int64'), []), relay.reshape(var_5686.astype('int64'), [4, 9, 1]), ), 0)
func_4631_call = mod.get_global_var('func_4631')
func_4634_call = mutated_mod.get_global_var('func_4634')
const_5689 = relay.const([-4.939076,-7.094075,-3.646172,-7.917203,-8.187356,-0.792775,-9.458062,7.212415,-9.499478,-9.363611,-7.806338,6.026759,2.465217,0.614485,-1.152717,8.079697,2.706389,-2.443659,6.217470,9.044967,-3.471892,-7.461089,-9.467726,-7.319483,7.897936,-6.672720,4.134131,5.114488,-6.771367,6.373082,8.269338,-8.336173,-7.234290,2.999036,6.360683,1.842275,-5.458609,-7.102377,2.614891,-6.948571,-8.721809,-0.654000,-5.993952,-9.787995,-9.270842,4.439220,8.292608,4.339245,2.854598,4.102801,6.555234,-2.610309,-5.609400,-0.612605,9.949308,-5.071992,-9.381444,0.443174,-9.830517,9.793007,5.622728,3.015805,-4.419800,-7.126870,2.232063,-7.473494,5.190030,-2.647656,-7.310594,6.678974,0.597210,2.974228,3.011342,6.146559,-3.192920,-8.069596,2.974947,-3.097983,-8.291161,6.557421,-7.838583,2.701537,4.628100,8.443051,-4.749939,3.051107,9.171788,1.519126,-1.332429,-5.963167,-3.271458,-2.761605,-0.976926,1.578106,-7.464845,-6.132097,4.293646,-3.448327,-2.605569,-8.765809,-6.009960,-1.545492,-8.315461,-4.248782,-7.507411,2.850939,-7.851179,6.828761,2.583838,4.976763,6.082606,-0.909563,4.939129,8.711634,1.875671,4.658019,-1.683222,3.882348,2.811785,3.585131,-8.496622,-5.802403,-9.102732,-3.078566,2.809948,6.110836,5.387169,0.144840,-8.000643,-1.913577,-8.220848,-6.853358,-4.058567,3.352742,0.717943,8.967474,6.203734,-5.058069,9.595901,9.111257,4.260079,-0.485478,0.824134], dtype = "float64")#candidate|5689|(143,)|const|float64
const_5690 = relay.const([[7.879243,7.778233,2.255428,-3.015141,3.693579,-8.127166,0.256544,4.774752,2.289363,9.664323,5.598334,-7.171350,9.273512,0.517959,7.708537,-5.196602,-5.510589,-2.989988,-8.847194,-4.428526,8.073594,8.945720,-0.475837,4.004909,5.029456,-6.502484,-9.228921,3.057690,-2.639850,-0.775458,8.472151,1.563425,-7.645402,7.790708,-7.228151,5.893264,4.169078,-4.695745,2.763037,3.896635,3.669099,6.763665,-5.665286,0.385936,1.831640,3.175579,8.376983,-9.310125,-7.045089,-5.308018,-3.798307,-1.632409,-5.477759,0.865211,5.046871,9.064211,-2.962682,-9.705367,1.064834,3.996952,7.323471,-7.565336,9.470418,7.834690,-1.706219,-7.022260,1.747521,-2.344894,-0.250522,2.096027,9.432696,-3.445863,0.676568,-6.655993,-9.727376,-3.809759,-9.365332,-7.459118,3.259191,-3.733907,-4.340898,-0.305292,7.309911,2.097568,-1.859674,4.473895,9.037904,0.483705,6.015283,-4.386606,-3.754223,0.993319,6.934917,-3.077024,5.528790,-8.321533,-7.013373,4.099443,-4.954929,1.129134,5.024311,-1.034388,-1.057475,-7.588856,0.823779,9.783063,3.725358,3.156388,7.099822,6.794169,-8.205503,-2.627590,6.099341,-1.708828,-7.077112,-1.091559,3.947833,8.227202,1.880090,2.106725,-7.992376,-3.690977,6.199495,-6.455817,8.270665,-4.802486,4.291220,-6.170869,-9.249581,-6.070700,-8.493665,9.489375,6.427767,8.318889,-5.669842,-8.738054,-0.173807,-4.169827,-5.805418,-7.666865,-4.633411,9.401678,6.448963,-7.000675,-1.219197,-5.624712,-3.921898,-6.019114,-9.964966,-8.669683,-2.922935,5.466017,3.798012,2.794299,-0.007268,3.660902,-1.025458,8.973643,1.581233,9.272355,-7.417983,-9.088451,7.664312,7.366173,4.316180,-1.633297,-5.935924,-2.474823,1.446326,5.293602,5.251947,3.916719,5.299733,4.784231,-3.806294,-5.800284,-9.243196,8.999212,-5.001621,-2.836180,-2.958918,8.894737,-6.802109,-5.836926,1.226428,-8.771821,1.233090,-3.954259,-4.254703,7.080955,7.828068,9.973938,-3.385484,7.255615,9.074017,-5.378988,1.730241,-1.654997,4.903469,0.658576,-9.523818,1.976290,5.496080,-6.594586,6.285075,5.149719,-0.987113,8.205875,2.747310,0.205533,-7.508870,5.578348,9.358672,5.762119,-5.418587,-1.227308,-7.584511,-0.455938,5.494963,8.695767,-6.341503,5.427388,-7.239809,-0.468727,-9.424808,-4.046163,7.007382,-3.903916,-9.855824,-4.071727,-9.809346,6.803236,-7.828120,3.509784,0.650360,1.770102,7.456377,-3.735066,3.660876,1.395160,-2.014117,-2.198861,0.631930,-3.128167,-3.247051,0.634134,3.700971,-0.383214,-3.621651,-3.824795,-6.548373,-6.225204,-7.749283,2.415125,0.010812,1.160469,2.079769,6.348740,-9.557896,-5.878023,-3.806685,-6.379444,-3.862095,-8.289043,-0.312902,-1.920259,-2.621425,-2.130765,0.753770,-3.084990,-7.687824,-0.839620,6.653397,6.895347,-0.873875,-2.763728,9.150671,-7.084925,8.564186,-6.327460,4.635059,8.098984,6.885472,8.902270,9.151054,3.645572,0.734922,2.904380,-0.646552,5.684726,-5.002062,8.111793,-8.684329,-4.338103,-4.083759,4.593338,0.225955,6.534993,-3.933611,-1.664101,-6.403628,5.494650,5.434616,-4.398207,0.493190,-4.440760,-8.779443,4.030684,-0.282620,-1.007402,8.786363,-2.410938,-7.992206,7.885429,-8.442873,3.576802,-7.158429,1.461666,4.483806,0.372189,4.749601,5.197419,4.213166,-0.341368,-6.069395,3.891451,-0.968318,-7.086988,9.848232,0.371398,8.992030,6.119036,3.266212,-9.429066,-7.741515,-2.764581,5.754014,0.407841,-6.331895,-3.148439,7.447809,-2.346091,-1.307504,-1.768522,4.253611,5.086469,-1.030496,-2.101257,5.617972,5.570212,-5.458299,4.672783,0.630265,-8.388024,-5.965915,-5.270284,-7.275364,5.485081,4.269312,0.281839,1.917440,-1.845106,3.382953,-4.591450,8.512690,-0.804630,5.224467,1.709636,8.998416,-1.870865,6.082369,6.961954,-6.919250,-9.594666,-1.051566,-7.640894,-8.599849,-9.799954,6.349891,5.074953,-3.851986,-6.158940,1.996665,-4.441707,8.135841,7.098098,6.506263,6.186465,0.032366,8.758029,0.156138,-1.437664,-1.674960,9.668821,5.938373,-8.778238,-0.501152,6.975696,9.304649,-2.204906,-4.574563,9.797950,-7.977245,2.845964,-0.021698,-6.922964,-0.328278,0.184858,8.197993,-8.432645,3.698232,-6.221087,6.576884,-6.829549,3.809170,-2.282311,-3.069457,8.319607,-2.231179,-0.126424,9.319353,-9.069391,5.125659,0.982454,-2.843194,9.458597,-6.037294,4.794696,8.794655,-9.533118,8.789527,3.079671,-7.905792,-7.808430,5.783604,0.928207,5.319650,4.964922,-3.331900,1.750057,-9.571812,-0.214769,-1.556914,6.426655,2.271360,-9.938224,-4.906276,-5.986401,-0.512292,7.000107,-8.771255,8.913820,-1.642303,-8.640756,2.684934,8.854998,4.241681,-2.027832,1.166569,9.834930,-9.701076,8.920821,6.618113,7.525543,5.667553,-5.763644,-1.114229,7.846702,-2.845668,9.730720,-8.191505,3.429931,-7.543626,2.916172,4.585507,9.561489,8.716014,-6.089975,-4.588375,-5.993096,-3.858864,2.293334,-0.043990,3.901672,8.814410,-7.682070,0.610512,7.416623,-4.894756,-4.454658,3.597515,9.961138,-0.935577,-4.237745,7.490161,-1.591233,8.213760,-1.681954,7.517371,-5.778208,-6.295445,-3.371651,-9.542056,-9.663870,-0.869782,0.768077,-8.905448,-9.746152,-8.160935,9.329051,-8.762747,-4.100806,-7.039168,5.007985,-1.429311,-9.895580,7.321255,2.942394,-3.989507,-8.032295,-7.394017,-0.213813,-9.984571,6.381215,6.075168,-4.321648,4.280346,6.780978,-4.342344,9.588659,-2.252225,0.801086,-9.800150,-2.904838,-1.143158,2.217335,-3.476157,7.200079,8.035325,3.429362,-8.708723,-6.366054,-9.843342,8.907407,-9.038177,-4.697431,-8.295430,-7.833170,-0.176673,9.960340,9.571875,0.734145,-2.445267,-6.609847,3.854860,6.031702,-4.382841,1.535499,5.084220,8.240545,8.180035,8.597561,7.075378,-8.201733,-9.632253,1.620014,5.356957,1.962223,3.411557,6.536616,2.727574,-7.710225,-3.057603,9.768487,-3.944927,7.293533,-5.839904,8.959409,8.456473,9.209273,2.560454,6.701242,2.798543,5.469208,4.321431,1.223863,8.221039,-7.973979,-2.973882,5.349324,-0.671993,-4.771203,6.546938,-9.850737,-5.457974,-4.495893,-7.746543,-4.733794,-0.722297,9.155382,-9.814056,3.507850,-3.267339,8.298715,2.377493,-7.243718,6.168471,-1.776322,-1.400428,0.866809,-7.691638,0.574944,-1.057402,-6.605168,4.256286,-0.817282,-0.532312,7.038790,0.605312,5.356219,1.377703,-5.841202,0.819354,-7.400799,5.681310,-8.031183,0.291832,5.095695,4.470422,6.173987,0.737134,-2.801987,9.529747,-5.725607,-9.414297,6.154342,0.212316,-2.129350,-8.938473,9.617878,3.163471,1.681751,6.461627,-6.628965,-8.049434,7.899226,5.877676,6.113701,1.843238,0.933219,-2.115247,0.091252,-1.377754,-0.955631,-0.344345,-5.655280,2.065424,9.904767,-4.348786,2.239012,6.851913,-7.768667,-6.068849,1.519628,-6.141530,0.383744,9.515279,-4.793821,-1.575550,-3.083393,-2.657521,-2.777174,-6.234784,-4.072373,3.023894,8.337568,-1.870674,8.262462,4.860941,-9.325726,7.198938,-3.733045,7.921772,-1.519225,2.835862,-3.685571,-1.132128,9.964387,-6.015070,9.376208,3.842281,-2.503702,5.638834,-9.275468,-0.492632,-8.115628,-9.129807,-4.142721,3.377421,-1.466322,5.912388,4.203978,4.737989,-9.576780,-6.041537,-8.421384,-2.412988,-7.249495,-6.498578,5.344235,7.252213,6.445104,-7.398694,4.794159,-5.681855,5.912470,3.696938,6.723156,9.483621,-4.775094,-3.823296,-1.020442,-7.389809,-6.907506,2.477648,4.899744,1.841715,1.882418,4.267092,5.090553,-1.775646,4.115278,4.928146,-6.864435,1.931396,4.871426,0.384852,-0.407725,-9.000670,8.346703,-4.116592,-4.800988,1.587422,-0.964140,0.455089,-5.405140,-8.506435,0.364980,0.791060,-2.675853,-4.127159,-5.383394,2.659532,9.976772,9.024479,-3.938078,-8.227696,5.580465,-9.501527,-3.256140,8.673990,3.564326,-0.663933,-6.644003,-8.840259,-4.899455,-0.067888,0.774479,-5.388050,5.817458,7.882625,9.497234,-2.137440,2.597243,-9.524029,-3.532271,-0.530450,6.254017,-0.065759,-6.099305,3.269733,-1.599947,6.277414,7.984437,-8.898763,3.990415,-3.263203,4.155282,8.900004,5.885972,-2.465199,-0.661983,1.426690,-0.205552,4.493963,1.668198,7.488825,-5.959332,8.889492,-9.392579,-2.622741,8.501179,6.253119,2.904905,5.311877,-6.972911,5.949524,-7.331488,0.606367,-0.984042,-3.469890,6.300423,8.739736,-2.700503,6.825193,1.126577,7.684753,8.628127,4.310516,9.426861,0.649062,7.587728,-2.314214,-9.739779,-3.012947,-8.506902,-4.703976,-9.044203,4.818264,-6.997914,-8.833889,-7.108658,-0.380818,-3.926629,8.277924,-4.120471,9.455406,8.649708,7.202200,1.658650,-6.706675,-3.540975,0.019164,9.194819,-4.565297,-2.307252,4.064975,-2.341641,-9.332547,7.108655,-1.223210,-7.967358,5.527865,-2.142566,8.747048,-7.465643,4.897516,-6.017269,-1.914484,-2.548499,5.906940,7.765092,7.657184,-1.857759,-6.160970,0.648975,2.120287,-9.747177,4.032344,-0.378735,8.448341,2.671367,8.180855,8.323920,0.363853,-5.579484,-4.656855,5.486906,2.327976,9.385674,7.557047,1.294165,9.941522,-8.207901,-5.113894,6.492745,8.436686,-0.100736,9.167851,-7.431182,1.071558,5.913102,-6.406524,-8.981602,2.736927,8.025372,-6.452564,7.038389,1.480253,2.253908,-6.274433,9.946812,5.820225,6.132770,8.318453,7.123461,-5.258833,0.440930,9.438406,4.661407,1.982968,9.770406,1.286325,2.002417,-0.197474,-8.370763,-6.823292,9.643574,1.801233,-8.119809,-0.087430,-8.307250,-2.244989,-0.123687,6.645037,-4.604709,-5.915805,-0.181895,1.952284,-5.371239,-1.886181,-6.613885,-1.652488,-4.784466,-0.512162,2.335126,-6.778874,-0.778568,8.915191,-3.168341,-0.983364,7.094667,3.113555,-4.984670,-7.406756,-4.399627,6.413283,2.647833,-2.111081,9.408475,-6.734679,-6.160193,-0.044028,8.979436,0.746821,-3.183875,7.757421,-2.021113,-8.848524,6.264219,-5.522603,2.719495,-3.364492,5.715443,6.765600,-1.043489,2.736745,-5.946099,4.879011,2.720418,-1.595694,-1.735052,-8.640420,-5.894311,8.469506,4.980222,1.023122,7.635823,0.588635,8.223975,7.166097,-1.747326,-0.123837,1.848000,-8.895214,-2.812351,-6.350123,-5.094376,3.717252,7.769110,-1.298678,-1.504114,-8.164325,-4.889556,0.231146,-1.062673,7.257211,0.565390,0.693248,0.114495,-6.097271,-9.407822,-1.755371,9.741852,9.721732,-4.017498,2.894788,-6.278406,-8.562293,7.048646,-7.008031,-3.148530,-1.508791,4.355139,-7.459717,7.631402,-4.559847,-5.611714,3.521978,-8.531686,-8.692841,-4.891523,-1.958521,1.346248,2.138975,-9.404935,-3.057854,5.024326,-8.405222,0.389999,8.163277,6.391330,-9.230825,-4.933147,5.308404,0.757179,9.661784,7.099773,-4.604196,-9.638141,6.205686,4.933038,-1.250729,-2.664312,9.136102,1.549932,0.367864,-8.885358,-0.500219,0.143955,6.119094,-1.649506,-7.827472,-5.238056,-0.424560,3.179220,1.572114,-1.101005,8.406322,1.605713,-2.842265,-7.318342,1.296542,8.591550,3.591901,-8.986855,6.446731,-8.819777,-6.156950,-9.184219,6.550634,0.912701,-1.965712,-5.008170,-8.920535,-9.982545,4.066008,-8.185574,9.441531,-3.128603,-5.556516,-7.353240,7.780895,-4.495011,9.726632,0.144434,-2.815757,-4.297028,-4.906910,-5.138669,-4.043131,4.116003,4.389086,-5.865780,5.140634,-6.836586,6.535923,-3.861331,4.586396,5.621602,7.613828,4.201318,6.415398,7.905875,5.446234,-6.527076,-5.411312,8.513003,-3.885553,7.148456,-0.132564,5.662706,-6.090117,4.091349,-9.409959,-0.424247,4.200450,1.888133,3.137305,-1.030789,8.938678,-9.334777,-7.926163,4.662677,-0.082542,-9.372132,-5.908219,-1.192272,9.788025,-3.022670,-4.106610,-2.949166,4.738896,-9.182337,-4.365287,9.509568,-1.160845,9.473465,6.985354,3.704536,5.115659,-9.766616,5.438959,-3.098385,-3.121617,2.312762,-8.855812,-3.662679,7.545148,-7.581327,8.239763,5.051404,-2.466931,-6.829810,-0.393695,3.413683,-6.198296,1.707119,-1.967244,-3.765759,5.874409,-1.492637,9.922052,8.898486,1.918282,-1.161610,0.459741,-7.972847,3.882850,3.304981,-1.002754,5.225219,-6.029899,6.887376,3.394575,-7.492000,1.444877,-4.662485,2.386949,3.116050,9.449674,-9.980893,-0.285146,-8.534680,2.993784,2.947306,-6.780432,-8.680363,6.968919,-7.034814,-3.400122,2.291127,3.290332,-8.654710,8.788476,1.191465,-6.984373,2.185396,9.592681,-8.736619,9.517590,-1.733240,-1.558173,4.250579,-5.373296,-7.852457,-2.335598,-1.813665,5.572492,-5.161490,6.930105,-1.562089,5.494000,-5.676896,0.474881,-7.407583,-3.800357,8.521196,1.537759,-2.710211,-0.384747,-8.464458,0.949078,-4.987769,-9.292438,1.377794,-0.746613,3.570383,-8.582274,-0.874529,-8.804559,-8.250409,-8.068201,7.500666,-1.382397,7.294287,9.694730,3.961187,2.586445,6.164826,5.258923,4.237194,-7.883649,6.662601,-2.555754,8.440218,-4.758192,5.431073,4.982368,2.384409,-3.268424,-9.300085,-7.800218,-0.899620,7.869521,3.074410,7.967664,-5.174733,3.846641,-3.284672,-6.368946,-9.484590,4.017549,4.802062,2.641629,3.484343,7.665457,3.257568,5.824272,5.577398,0.237889,6.767629,3.545817,3.589210,-9.643420,-6.827081,0.297932,2.696984,-9.128564,3.244820,3.974632,-3.285997,-6.582520,0.200597,1.750452,-6.068742,4.530762,2.998158,6.564789,-7.629298,-1.417572,-7.883908,2.811194,4.485849,-0.268221,2.420632,6.624167,2.534521,7.012668,8.147057,3.288138,-1.385249,-7.897176,-5.648607,-9.074512,6.983670,0.152948,-3.880715,3.831180,6.773471,-4.377383,-7.026709,-8.757795,1.571492,-5.071758,-9.361567,-0.511071,-3.021321,5.157993,-4.915973,0.023027,-0.873482,-8.187897,-5.779179,-7.005903,0.385759,-0.343343,-5.725047,6.458719,4.824343,4.124562,-0.171058,-4.592137,-6.635344,2.141642,2.878685,-3.333063,1.991966,-7.190437,-3.755560,8.948874,2.436871,0.534936,-5.396337,5.407192,-2.751993,-7.120970,-0.696019,-0.943599,-5.260039,7.422368,-3.359131,6.952340,-7.974277,5.908268,9.703718,5.806736,4.160257,-3.959296,6.633579,7.069997,-2.472788,-2.544699,-6.518530,0.177306,-3.249602,-0.014302,-7.588188,0.886729,0.436629,-8.454858,0.226872,1.811845,-2.035446,2.835531,6.917509,-4.554492,-2.906808,-0.031842,6.836637,6.406290,-4.521433,-9.470999,7.750775,-3.726236,0.051105,0.497859,-4.822052,4.588295,2.220338,-4.058962,4.566937,-5.841426,-3.056967,-9.156057,0.785569,3.477610,7.834296,-4.564378,3.778097,1.706031,4.446680,-3.277287,7.486831,5.801669,-4.076942,3.790170,-1.041678,0.084524,-3.802331,-4.096647,6.454162,2.670146,2.794902,6.453295,-1.096438,8.820159,-9.269049,4.884724,7.343612,-8.708660,4.219556,7.053502,8.046134,-4.106801,-6.660739,4.181654,-5.843285,-4.157155,0.453106,4.598660,-3.092670,4.268137,-7.290833,-2.951601,6.252610,7.249600,-4.707431,-5.014279,4.803307,1.919155,2.995182,4.665965,-4.101627,-0.158626,1.850334,2.093368,-9.585545,-3.053360,-4.361985,3.794614,5.468065,-9.827819,7.204640,-9.953839,2.059293,9.460893,-1.530737,-8.300026,-2.547582,-3.202402,-6.552299,-6.560066,1.641815,0.856396,5.486066,6.330928,7.104128,9.232292,6.528724,7.644259,0.910474,4.217326,2.360228,-0.281216,-2.454457,-7.327607,0.833538,-3.286803,1.362941,-9.962007,-4.288896,-3.094282,7.296784,-9.228490,7.765084,9.143735,-1.571874,-2.580168,-8.834114,-6.987509,-8.335389,-0.882914,9.360651,-1.859030,-9.738262,8.592261,-2.010122,3.675430,7.472143,-3.381913,8.677172,-2.512512,7.068339,-9.672224,6.089740,-6.575024,6.194282,3.606279,9.387793,4.201647,-3.649332,-3.012625,-7.745872,-1.699641,-1.667707,-2.363173,-0.192756,4.368006,-5.642369,-9.183947,-1.716457,0.903775,8.240199,-6.880595,-5.649707,-2.632860,4.190390,7.033056,-8.022257,8.401772,6.118066,2.442734,-4.255534,9.509422,-5.808873,2.094231,-5.495662,-9.157193,9.569703,6.389935,-9.072075,6.624220,-0.717879,-2.892553,-9.060892,1.237084,1.267315,-3.478653,-2.028880,-3.367858,4.503774,4.434133,-8.392988,1.513259,8.517073,3.875406,-2.070286,7.148456,-9.781510,-7.754417,5.238765,-9.588566,-3.214089,3.670048,-5.882328,3.678760,6.831671,3.233019,-0.581218,4.260861,2.841751,4.458155,1.902658,1.876207,-8.690926,4.177977,9.877179,1.915561,-3.117074,-6.466629,-9.324364,-4.898212,5.879301,-8.736528,-7.580870,4.005037,-1.616711,8.156332,3.149279,5.885909,-9.687077,9.607679,-5.853418,7.411023,4.035783,0.901173,1.448724,4.226952,-0.431927,-7.836994,-6.491722,-0.135381,6.569759,-6.950384,-6.481810,-1.452577,-1.237101,0.688138,-3.706181,0.815509,-2.779584,-6.011541,-4.925384,-6.281878,6.268389,3.001189,-1.057183,-4.479589,-2.810150,-3.510374,7.920289,1.889890,2.869158,-9.540414,-8.688400,3.774759,3.266830,-4.081263,-2.588031,-6.958978,-1.623480,3.313260,4.562822,-0.471093,-3.760898,2.212156,9.610975,-3.113429,7.066853,6.604755,-6.155901,-9.179585,-3.064969,-2.087216,-4.477632,-0.088655,-5.416764,5.964668,3.266312,4.650345,5.294388,1.094779,-1.702363,8.100831,0.604484,2.512143,4.165242,8.256910,-0.386704,-3.591473,-5.417714,1.609563,-4.514818,-9.349086,-9.735148,-4.383465,-0.223348,7.882419,8.580649,-3.977318,0.072134,-5.698445,-9.614045,-9.145786,7.904845,9.611566,7.731230,2.422913,4.965304,2.693810,4.796441,1.899425,-8.335342,-8.307308,2.550967,-9.200998,-3.573080,-1.338204,-0.787199,-2.545093,5.461977,4.562457,-3.599397,3.498770,-3.129699,-0.695802,-3.314576,-7.495168,-0.555531,-2.784335,0.102181,-5.827432,5.213779,-0.232630,8.064227,-7.480651,-0.099470,8.583432,-8.753827,8.690541,8.027464,-6.662613,5.186034,-5.690571,-3.922012,-7.989116,0.580191,7.565458,3.510883,-5.290768,-9.992837,0.790112,-0.905219,-5.473836,6.046863,-5.816489,3.728300,-5.214309,1.215772,-4.399388,9.312128,2.386501,3.299291,-9.510480,5.186033,1.198569,7.468460,-5.305403,5.243800,-2.901029,-3.886124,3.620536,5.514486,6.804908,1.402236,-6.958060,-1.775396,6.215152,0.397117,-5.738763,7.597226,-6.564570,-0.772316,-1.840452,1.238497,8.818924,6.323881,6.288972,-1.758307,7.375249,-6.337910,1.171708,-1.627846,-0.887378,-7.202361,-6.346855,-9.319500,-5.425719,9.859247,-9.977285,5.557784,8.198313,0.718874,8.689658,5.750640,0.157586,9.506811,-3.138514,2.056041,6.391425,2.760967,7.860275,-4.430904,-6.404028,5.584043,5.673753,-6.617893,6.367401,0.084949,-6.847252,-3.474586,4.965796,-7.375874,5.084579,-0.537795,9.509479,-6.668387,-0.977850,-6.524441,-0.937411,6.560270,-7.563463,-8.188631,5.469137,-2.014387,-1.922532,6.058144,-1.487308,3.662338,-4.927747,-2.519903,7.612644,-2.312921,-7.679035,2.242236,-3.882310,-3.282667,-1.960006,0.678527,-0.639582,6.988829,-9.101250,-6.985683,-5.958523,-6.482837,-2.102662,-6.727133,1.364654,8.682627,2.316299,-8.746423,7.258031,-6.303904,-2.919901,-9.128356,-6.736341,3.230610,-6.315382,3.470544,-2.637630,0.209916,2.797200,-1.564501,8.736738,-8.282149,-1.007243,-1.734054,1.354834,-7.288315,-7.050397,-4.188055,-5.294761,2.208461,-2.046681,-5.596095,-5.042001,9.635806,9.047162,-5.842358,5.020222,-8.080427,-2.591813,3.846017,2.452851,5.048793,-4.339830,-3.381604,4.186720,-1.786517,2.450882,-8.491681,-2.193342,3.146878,-9.151717,-7.236553,-7.032042,8.704407,-1.857216,-4.045080,-3.594880,9.157097,4.321999,-6.853870,-8.302877,-1.435106,9.710508,4.768668,-3.859210,9.979501,0.962791,-9.763972,-0.432139,-8.929016,2.815137,6.237851,-0.307278,-2.215434,-4.904762,-7.762449,6.450321,-2.993451,-4.426008,6.895863,-6.962425,4.025832,-5.147270,7.608616,2.270346,1.072354,-7.928978,9.359004,-6.480230,2.116320,-2.586003,5.761511,-7.688329,-8.715673,3.861059,-7.011224,-9.765339,4.938203,4.789956,-9.834855,-1.562015,5.849822,-6.983383,6.499851,4.785716,6.788367,8.233809,5.822807,1.064540,-4.118409,8.955829,-4.965917,-3.732832,6.090574,0.842297,-9.119476,0.901741,-1.388740,-3.406942,-0.285654,-0.238708,2.837037,-0.385113,-2.647214,-3.352451,2.296456,2.717823,-4.785585,0.045219,2.650898,9.085190,5.419860,-5.452264,-8.330358,7.287086,-1.622087,-0.654667,7.209105,-0.753457,-4.874309,-0.597159,8.998333,-6.973599,9.595477,7.407205,-0.051739,4.479822,5.049761,4.463657,-4.432791,1.216293,0.473679,6.302598,-3.335648,-1.025068,-6.371723,-9.938951,-3.398675,4.555503,6.391169,-3.242250,9.879722,8.895312,9.657840,-9.591177,0.651124,-3.068328,-7.183709,-6.290771,-2.876593,2.046877,7.542776,-6.463305,-9.609013,-0.457307,-5.416557,6.187795,-4.995705,-8.913037,-5.418023,7.798725,-7.579009,-8.953878,7.673069,-3.458062,3.316565,1.999491,0.441006,-9.894698,8.314079,3.246434,3.071790,-9.507077,6.885700,-9.947194,9.760558,-0.066954,3.452607,-6.107080,0.534358,-7.413474,3.498794,6.330984,9.214557,-8.581442,-4.932622,-3.266465,4.646561,4.739140,-3.749527,-4.262615,-1.437964,2.383732,9.929590,-8.514346,-4.675034,1.620864,-5.823994,1.452720,-4.090838,2.201911,1.640470,-6.497718,-8.719435,-6.316845,4.580912,-5.188629,4.758540,-9.332996,-9.472947,2.425929,4.198643,-7.813435,4.111351,-6.061673,1.055476,3.085084,1.048813,7.936034,3.610724,-7.124095,-9.315485,-4.315136,2.411001,-3.723204,-8.780861,-0.611683,-2.501414,8.041525,-5.575295,5.153300,4.033735,3.172536,3.996817,-9.092855,-9.312466,5.126560,-3.693138,-8.301089,-7.809320,5.920098,-0.364095,0.315254,-7.401773,-9.277354,-4.615919,-7.582536,-8.792405,-9.925858,9.753101,2.209176,-2.253831,-6.181546,-7.960294,-5.030935,-4.110068,5.771818,8.677548,0.560046,-7.465016,1.098457,-3.998448,-0.926075,7.805272,-2.740347,-9.988019,-7.735959,-0.269504,1.939719,2.998227,-8.543610,3.059444,-0.201739,-6.368169,-5.105493,4.654576,6.436418,8.865277,7.322305,-7.445072,0.685721,4.226778,6.440144,2.840318,-3.567882,-9.719494,-6.582002,8.992994,3.423125,-5.533605,-2.583885,1.235993,2.672881,3.165332,5.240655,-9.454692,-7.563647,-6.681598,-9.354378,-5.099951,-3.289807]], dtype = "float64")#candidate|5690|(1, 2145)|const|float64
call_5688 = relay.TupleGetItem(func_4631_call(relay.reshape(const_5689.astype('float64'), [13, 11, 1]), relay.reshape(const_5690.astype('float64'), [13, 11, 15]), ), 0)
call_5691 = relay.TupleGetItem(func_4634_call(relay.reshape(const_5689.astype('float64'), [13, 11, 1]), relay.reshape(const_5690.astype('float64'), [13, 11, 15]), ), 0)
output = relay.Tuple([call_5672,call_5684,const_5685,var_5686,call_5688,const_5689,const_5690,])
output2 = relay.Tuple([call_5673,call_5687,const_5685,var_5686,call_5691,const_5689,const_5690,])
func_5699 = relay.Function([var_5686,], output)
mod['func_5699'] = func_5699
mod = relay.transform.InferType()(mod)
mutated_mod['func_5699'] = func_5699
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5700 = relay.var("var_5700", dtype = "int64", shape = (9, 4))#candidate|5700|(9, 4)|var|int64
func_5699_call = mutated_mod.get_global_var('func_5699')
call_5701 = func_5699_call(var_5700)
output = call_5701
func_5702 = relay.Function([var_5700], output)
mutated_mod['func_5702'] = func_5702
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5156_call = mod.get_global_var('func_5156')
func_5157_call = mutated_mod.get_global_var('func_5157')
call_5723 = func_5156_call()
call_5724 = func_5156_call()
output = relay.Tuple([call_5723,])
output2 = relay.Tuple([call_5724,])
func_5736 = relay.Function([], output)
mod['func_5736'] = func_5736
mod = relay.transform.InferType()(mod)
output = func_5736()
func_5737 = relay.Function([], output)
mutated_mod['func_5737'] = func_5737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5418_call = mod.get_global_var('func_5418')
func_5420_call = mutated_mod.get_global_var('func_5420')
call_5925 = relay.TupleGetItem(func_5418_call(), 0)
call_5926 = relay.TupleGetItem(func_5420_call(), 0)
output = relay.Tuple([call_5925,])
output2 = relay.Tuple([call_5926,])
func_5929 = relay.Function([], output)
mod['func_5929'] = func_5929
mod = relay.transform.InferType()(mod)
mutated_mod['func_5929'] = func_5929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5929_call = mutated_mod.get_global_var('func_5929')
call_5930 = func_5929_call()
output = call_5930
func_5931 = relay.Function([], output)
mutated_mod['func_5931'] = func_5931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5736_call = mod.get_global_var('func_5736')
func_5737_call = mutated_mod.get_global_var('func_5737')
call_5954 = relay.TupleGetItem(func_5736_call(), 0)
call_5955 = relay.TupleGetItem(func_5737_call(), 0)
func_5736_call = mod.get_global_var('func_5736')
func_5737_call = mutated_mod.get_global_var('func_5737')
call_5963 = relay.TupleGetItem(func_5736_call(), 0)
call_5964 = relay.TupleGetItem(func_5737_call(), 0)
output = relay.Tuple([call_5954,call_5963,])
output2 = relay.Tuple([call_5955,call_5964,])
func_5971 = relay.Function([], output)
mod['func_5971'] = func_5971
mod = relay.transform.InferType()(mod)
output = func_5971()
func_5972 = relay.Function([], output)
mutated_mod['func_5972'] = func_5972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5971_call = mod.get_global_var('func_5971')
func_5972_call = mutated_mod.get_global_var('func_5972')
call_6028 = relay.TupleGetItem(func_5971_call(), 1)
call_6029 = relay.TupleGetItem(func_5972_call(), 1)
func_4593_call = mod.get_global_var('func_4593')
func_4598_call = mutated_mod.get_global_var('func_4598')
const_6031 = relay.const([-9.234236,2.589876,-4.842770,-4.922687,-8.201412,-1.620704,9.691480,-8.427447,3.666601,-2.454722,3.105174,-3.994411,-1.767638,-8.486271,-6.143404,-2.525018,1.006838,6.880389,-6.035792,9.229960,-9.328812,5.322840,9.670105,5.946158,4.883191,-4.732262,2.926465,4.200543,-1.624773,1.929695,7.906157,9.491873,2.486320,3.866548,-8.314169,-1.853044,-5.697573,-1.351261,1.365977,-2.873917,3.977326,9.703439,-7.547748,-6.558599,-7.568241,1.061663,-6.284580,-1.162941,3.075275,2.538687,2.686876,0.299862,-5.505063,6.388493,5.655479,-4.332313,4.645349,1.167230,-3.736952,-9.344025,7.638975,9.746367,-8.789948,6.170836,8.668717,-6.071568,8.996885,-5.028611,7.073142,7.977024,-3.845267,-5.042046,-1.019262,6.427837,5.048030,7.871528,6.293052,-6.436132,9.377149,-7.293776,5.203634,6.631448,-5.918322,-1.291413,8.962913,-3.738143,8.327126,5.372855,2.338721,-1.867117,-2.976363,8.418955,-5.105406,-4.741769,-7.818053,-4.798644,0.042256,-2.657315,-0.895374,2.306394,-2.064043,1.512392,-7.498525,1.161406,1.278667,3.424196,-0.243987,2.102735,-2.515308,-2.713895,-6.513625,-8.988041,-6.876300,4.696647,3.131526,-2.465513,7.781023,9.611537,2.180629,2.873726,2.196805,-9.780237,1.715713,-4.263275,8.395177,-5.271066,-3.849784,8.161637,4.504984,1.508655,-7.941701,2.651360,3.134016,0.632845,1.980102,6.330924,7.842527,-4.754453,2.041349,4.217111,1.232423,3.538908,-0.499977,-8.396376,7.173753,1.126535,-6.991154,4.300614,0.084475,-7.881409,5.237068,0.618881,7.694788,-5.508247,8.368949,-0.383101,1.462262,-3.444441,-0.522898,-5.171165,-1.904960,1.433575,-7.803547,-4.616162,-0.180579,-5.966667,-9.942464,-5.737875,-0.204011,-2.651062,-6.512632,-7.129231,-3.149801,-3.188615,-2.559251,4.726288,-7.355519,1.869299,8.860110,-4.009597,-4.306503,-1.129496,7.808140,-8.880617,8.663386,0.605700,4.662331,2.248530,-1.045453,5.446171,-3.124867,0.779470,4.289290,5.806794,-1.904033,-3.280369,0.452607,7.815723,-7.272938,-4.722225,-2.279950,1.362379,6.132374,-5.543425,-6.040053,-1.421843,-9.302993,0.613272,-7.065033,-3.465806,4.078189,8.092333,7.980754,4.892163,6.888712,1.582130,8.422827,4.520059,-5.990677,-5.878109,1.822695,8.060653,-7.171250,-7.041644,-4.072752,8.451700,2.758490,-9.267739,6.104853,-9.107991,8.005496,-1.344604,9.782746,4.154190,9.200352,-6.665089,6.090088,-0.439231,4.146609,-3.913304,-5.217346,1.606836,7.744740,-4.303187,4.560734,2.505366,0.011500,6.756543,8.955521,-8.354518,-1.540700,-3.965490,-4.779654,3.585636,4.227087,5.398741,6.692938,3.838120,-8.851758,2.038138,9.173591,-2.092378,-6.539046,0.145864,9.262351,4.261833,-2.139907,1.020340,-0.822524,-6.403020,-7.746812,5.369744,-4.689792,-3.472047,3.665814,-4.468307,-0.711669,4.079160,-1.252892,3.202471,-1.033736,3.099620,-6.007632,4.283270,6.629934,-4.582738,-0.611838,3.265464,-9.731502,5.852986,8.273679,-4.567021,4.273075,2.125459,-7.375876,4.296505,8.460657,-5.672746,8.847367,-8.954522,2.830382,-3.223663,4.718816,8.192685,-9.068888,3.644377,-1.676515,7.817300,6.703953,-0.348805,8.439271,-7.690692,-7.276673,-9.634407,-1.933003,5.581768,0.232792,8.846028,6.494488,1.215434,-2.003799,-5.870696,-8.610663,-1.920208,-9.069691,-4.630694,-2.689391,-7.527789,9.931753,-6.289673,8.989316,0.949908,9.805557,9.096424,2.118885,-3.828258,9.661395,0.971429,4.084498,0.790208,-2.878171,0.388529,-3.089670,1.730464,1.932323,-7.771503,7.641454,7.483990,-7.874049,-5.189535,8.097973,2.618379,6.026071,1.156293,-8.181198,-1.878024,-0.583145,7.812208,2.797369,-1.621817], dtype = "float32")#candidate|6031|(360,)|const|float32
var_6032 = relay.var("var_6032", dtype = "uint16", shape = (495,))#candidate|6032|(495,)|var|uint16
var_6033 = relay.var("var_6033", dtype = "float32", shape = (308,))#candidate|6033|(308,)|var|float32
call_6030 = relay.TupleGetItem(func_4593_call(relay.reshape(const_6031.astype('float32'), [9, 8, 5]), relay.reshape(var_6032.astype('uint16'), [495,]), relay.reshape(var_6033.astype('float32'), [308,]), ), 3)
call_6034 = relay.TupleGetItem(func_4598_call(relay.reshape(const_6031.astype('float32'), [9, 8, 5]), relay.reshape(var_6032.astype('uint16'), [495,]), relay.reshape(var_6033.astype('float32'), [308,]), ), 3)
func_3856_call = mod.get_global_var('func_3856')
func_3859_call = mutated_mod.get_global_var('func_3859')
call_6037 = relay.TupleGetItem(func_3856_call(relay.reshape(var_6032.astype('uint16'), [11, 15, 3])), 1)
call_6038 = relay.TupleGetItem(func_3859_call(relay.reshape(var_6032.astype('uint16'), [11, 15, 3])), 1)
func_5971_call = mod.get_global_var('func_5971')
func_5972_call = mutated_mod.get_global_var('func_5972')
call_6051 = relay.TupleGetItem(func_5971_call(), 0)
call_6052 = relay.TupleGetItem(func_5972_call(), 0)
output = relay.Tuple([call_6028,call_6030,const_6031,var_6032,var_6033,call_6037,call_6051,])
output2 = relay.Tuple([call_6029,call_6034,const_6031,var_6032,var_6033,call_6038,call_6052,])
func_6077 = relay.Function([var_6032,var_6033,], output)
mod['func_6077'] = func_6077
mod = relay.transform.InferType()(mod)
var_6078 = relay.var("var_6078", dtype = "uint16", shape = (495,))#candidate|6078|(495,)|var|uint16
var_6079 = relay.var("var_6079", dtype = "float32", shape = (308,))#candidate|6079|(308,)|var|float32
output = func_6077(var_6078,var_6079,)
func_6080 = relay.Function([var_6078,var_6079,], output)
mutated_mod['func_6080'] = func_6080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5164_call = mod.get_global_var('func_5164')
func_5166_call = mutated_mod.get_global_var('func_5166')
call_6090 = relay.TupleGetItem(func_5164_call(), 0)
call_6091 = relay.TupleGetItem(func_5166_call(), 0)
uop_6099 = relay.sin(call_6090.astype('float32')) # shape=(1, 12, 15)
uop_6101 = relay.sin(call_6091.astype('float32')) # shape=(1, 12, 15)
func_5971_call = mod.get_global_var('func_5971')
func_5972_call = mutated_mod.get_global_var('func_5972')
call_6103 = relay.TupleGetItem(func_5971_call(), 1)
call_6104 = relay.TupleGetItem(func_5972_call(), 1)
output = relay.Tuple([uop_6099,call_6103,])
output2 = relay.Tuple([uop_6101,call_6104,])
func_6107 = relay.Function([], output)
mod['func_6107'] = func_6107
mod = relay.transform.InferType()(mod)
mutated_mod['func_6107'] = func_6107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6107_call = mutated_mod.get_global_var('func_6107')
call_6108 = func_6107_call()
output = call_6108
func_6109 = relay.Function([], output)
mutated_mod['func_6109'] = func_6109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5971_call = mod.get_global_var('func_5971')
func_5972_call = mutated_mod.get_global_var('func_5972')
call_6125 = relay.TupleGetItem(func_5971_call(), 1)
call_6126 = relay.TupleGetItem(func_5972_call(), 1)
output = relay.Tuple([call_6125,])
output2 = relay.Tuple([call_6126,])
func_6138 = relay.Function([], output)
mod['func_6138'] = func_6138
mod = relay.transform.InferType()(mod)
mutated_mod['func_6138'] = func_6138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6138_call = mutated_mod.get_global_var('func_6138')
call_6139 = func_6138_call()
output = call_6139
func_6140 = relay.Function([], output)
mutated_mod['func_6140'] = func_6140
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5156_call = mod.get_global_var('func_5156')
func_5157_call = mutated_mod.get_global_var('func_5157')
call_6148 = func_5156_call()
call_6149 = func_5156_call()
func_5378_call = mod.get_global_var('func_5378')
func_5382_call = mutated_mod.get_global_var('func_5382')
var_6163 = relay.var("var_6163", dtype = "uint32", shape = (1, 55))#candidate|6163|(1, 55)|var|uint32
var_6164 = relay.var("var_6164", dtype = "uint32", shape = (385,))#candidate|6164|(385,)|var|uint32
call_6162 = relay.TupleGetItem(func_5378_call(relay.reshape(var_6163.astype('uint32'), [11, 5, 1]), relay.reshape(var_6164.astype('uint32'), [11, 5, 7]), relay.reshape(call_6148.astype('float32'), [30, 6]), ), 3)
call_6165 = relay.TupleGetItem(func_5382_call(relay.reshape(var_6163.astype('uint32'), [11, 5, 1]), relay.reshape(var_6164.astype('uint32'), [11, 5, 7]), relay.reshape(call_6148.astype('float32'), [30, 6]), ), 3)
func_2536_call = mod.get_global_var('func_2536')
func_2539_call = mutated_mod.get_global_var('func_2539')
const_6177 = relay.const([-8.650827,5.888313,2.903659,-0.888833,4.697298,-5.443871,-5.705062,-1.189381,-9.884680,8.580291,5.499153,5.733906,9.086443,1.824083,0.698557,2.785775,0.519713,-7.976221,-9.226105,-2.452290,-7.325070,5.343537,4.987630,-0.481489,-5.799302,-5.639826,-3.163631,-7.496046,-2.254898,-5.749179,-7.204211,1.667079,9.233723,8.531076,-8.772174,8.203554,-9.436189,9.844287,-6.469868,-9.424643,0.645160,-1.751149,-0.823372,-1.136162,9.439238,-2.292901,-0.350955,9.203431,2.953968,-9.745788,2.510461,7.599505,-1.654547,7.551106,-3.116224,5.625625,-7.057652,-2.190690,5.561760,7.036627,1.296628,-3.644054,6.869869,1.562705,-9.857893,-5.731344,2.344456,-1.843428,6.271156,-6.502857,0.303932,7.391527,-8.309625,-3.624870,-1.512862,-8.057487,7.001393,-5.294825,-2.224348,-9.938741,6.292825,-8.732219,-1.351743,-6.317506,9.732807,1.497833,7.720576,-0.129581,-5.605977,9.522052,0.214481,4.217672,-9.925387,2.836959,2.082003,-8.177475,8.941523,-0.981123,9.924931,7.244695,3.406476,4.724667,1.201266,-7.551715,-8.219463,1.697871,3.558228,-0.923256,-8.765003,0.100476,4.599065,-2.279419], dtype = "float64")#candidate|6177|(112,)|const|float64
call_6176 = relay.TupleGetItem(func_2536_call(relay.reshape(const_6177.astype('float64'), [16, 1, 7])), 0)
call_6178 = relay.TupleGetItem(func_2539_call(relay.reshape(const_6177.astype('float64'), [16, 1, 7])), 0)
func_5469_call = mod.get_global_var('func_5469')
func_5471_call = mutated_mod.get_global_var('func_5471')
call_6182 = relay.TupleGetItem(func_5469_call(relay.reshape(call_6176.astype('float64'), [112, 1])), 0)
call_6183 = relay.TupleGetItem(func_5471_call(relay.reshape(call_6176.astype('float64'), [112, 1])), 0)
func_2536_call = mod.get_global_var('func_2536')
func_2539_call = mutated_mod.get_global_var('func_2539')
call_6202 = relay.TupleGetItem(func_2536_call(relay.reshape(call_6176.astype('float64'), [16, 1, 7])), 0)
call_6203 = relay.TupleGetItem(func_2539_call(relay.reshape(call_6176.astype('float64'), [16, 1, 7])), 0)
output = relay.Tuple([call_6148,call_6162,var_6163,var_6164,call_6176,const_6177,call_6182,call_6202,])
output2 = relay.Tuple([call_6149,call_6165,var_6163,var_6164,call_6178,const_6177,call_6183,call_6203,])
func_6204 = relay.Function([var_6163,var_6164,], output)
mod['func_6204'] = func_6204
mod = relay.transform.InferType()(mod)
var_6205 = relay.var("var_6205", dtype = "uint32", shape = (1, 55))#candidate|6205|(1, 55)|var|uint32
var_6206 = relay.var("var_6206", dtype = "uint32", shape = (385,))#candidate|6206|(385,)|var|uint32
output = func_6204(var_6205,var_6206,)
func_6207 = relay.Function([var_6205,var_6206,], output)
mutated_mod['func_6207'] = func_6207
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5156_call = mod.get_global_var('func_5156')
func_5157_call = mutated_mod.get_global_var('func_5157')
call_6223 = func_5156_call()
call_6224 = func_5156_call()
const_6226 = relay.const([[[0.118355,4.098179,-7.807096,-9.026365,-0.143853,-7.003087,8.096108,-3.470991,-1.827823,1.315385,-3.344577,9.514657,8.445815,-7.249192,-3.585087],[-5.135551,9.286051,-3.021294,-5.579197,2.971579,2.948698,9.736934,7.339343,-3.143498,-8.020437,-3.267662,3.186588,9.501074,-1.481628,2.567894],[-4.096848,-1.601237,-7.751306,6.745447,-9.628167,4.149253,-9.421803,-7.364729,-2.619902,7.981410,-4.215710,-1.456632,7.821559,-3.486257,0.701752],[-8.631821,2.597541,6.480892,6.089833,-8.263034,-1.353740,9.489928,-1.237504,-0.681993,1.009384,2.888154,-2.769836,5.289883,-4.005269,0.676815],[-1.150728,5.586361,-0.939895,9.385478,5.951984,7.741194,8.357673,-1.993512,-1.167734,7.849293,-8.646429,-5.097090,-2.336362,-3.328949,3.133738],[-0.830362,-2.402465,-7.417226,-1.588851,-3.146759,2.494907,2.473399,8.130901,0.869967,5.224602,6.866179,3.044165,-5.898934,9.134919,-6.641085],[-3.255402,-3.389833,-3.493174,8.918801,-7.496374,-2.245287,-6.305646,3.098844,0.235025,7.240956,8.965186,-6.843021,-4.230701,-1.965897,-7.805828],[2.852390,4.818437,8.422311,-5.264952,-8.430204,-7.961885,-9.382127,2.817622,-3.308200,-2.532107,9.556919,-9.563688,1.228469,-0.869985,0.317458],[-3.159484,5.915158,-2.517150,-9.318800,3.079844,-1.735115,9.083643,-0.828497,-1.240051,-4.001738,8.911858,-6.125882,8.750570,-1.455400,6.813454],[-9.802481,-6.840702,0.261887,-3.704162,7.626456,-7.265081,-4.340061,9.097841,-6.678132,3.666844,-4.613414,-5.297012,1.426209,-7.533402,6.370260],[0.529357,-7.215996,2.643077,-2.305464,3.990836,-3.173185,8.922882,8.803997,5.467005,-2.499989,-0.154402,3.202824,0.744699,6.149239,9.437981],[9.336359,-6.859155,-3.198238,3.097022,-5.574187,5.394285,3.372838,2.777823,8.058576,-0.462038,2.574294,-6.380322,-5.347266,1.287776,-1.836773]],[[-5.307175,2.066481,5.181930,4.853358,9.795920,2.316415,-5.616525,6.333484,0.762284,-3.563308,8.136256,4.985071,2.039546,3.789012,9.008877],[9.034627,-4.666316,-0.032219,-2.597701,-8.189678,8.972359,-7.562179,-1.516867,1.751531,-8.348427,-9.525121,-9.472433,-2.665053,1.850979,-3.735618],[1.174082,-8.084741,7.215157,5.724001,-5.658943,4.493286,7.093669,8.220765,9.787898,2.392524,5.958752,4.924991,0.185976,3.023107,-1.128429],[1.266148,4.363449,5.935784,1.522066,-0.259881,-6.725018,9.022367,-4.040719,-5.193600,-2.533498,3.540407,7.337920,8.008208,-8.537020,3.133059],[-4.193245,-9.602203,-3.641144,-2.456898,-2.311623,-4.474593,-2.365320,-4.195203,-5.881824,8.960056,7.916882,-1.388519,5.295918,0.406032,-7.029619],[-8.014378,-3.836052,-2.307344,-7.963613,-5.616153,-8.220702,-3.090476,-5.330182,2.556542,2.732291,3.770309,9.733266,3.951709,7.991434,6.724021],[6.985130,6.377337,-5.392057,-6.504159,-1.567642,-7.383434,5.904862,-5.166947,3.693866,7.865833,-2.817744,8.734794,-7.081363,-6.378130,-7.739833],[-9.111705,-1.082426,6.148964,3.923502,2.490052,-0.483265,-7.643402,-2.709711,2.260060,-5.180281,-0.904045,-3.841664,4.492848,-6.756298,-3.445919],[7.918171,-3.724418,-5.541324,-8.836293,-3.929571,-9.908798,6.958604,-1.510209,3.436864,-5.240859,-9.283573,-1.224976,-4.406624,-6.719907,1.835599],[7.759419,1.115060,-1.593580,4.509873,2.792028,1.861005,-8.611082,7.141352,-4.165874,1.552233,-9.843700,-3.730019,-0.808954,-8.006717,7.407559],[5.325119,-7.953359,9.661641,2.567752,-2.082936,-5.001738,-1.356915,-6.459795,2.178199,-3.924074,8.115964,4.583096,4.829668,0.945089,-5.000721],[6.095066,2.779068,-0.323600,0.154560,-1.275624,-4.537125,1.737251,3.913521,-7.570254,-5.366084,8.185925,-4.913800,9.490497,-6.514063,3.930811]],[[-6.919582,9.363249,2.991705,-4.150014,3.954539,-6.965249,1.001405,-4.119641,7.994325,9.471747,7.059485,-4.583090,2.625765,5.438560,-1.392023],[-2.183936,2.045379,-5.574226,0.290563,1.057272,3.020554,1.063754,8.714390,-0.508282,-6.729862,8.781159,-3.936290,6.612817,6.368298,-1.125036],[-5.096612,-0.578890,-2.352798,-9.503029,3.697290,-3.042335,9.655306,4.674387,9.724422,4.499850,-0.245700,5.189849,-3.019566,-4.494163,6.357877],[8.990173,-0.019477,9.265274,2.118842,-5.799351,-7.156575,1.492840,-6.912940,-6.325104,-1.477859,-4.570486,-7.864840,-4.681057,-1.274233,0.719009],[4.042260,5.492711,-3.015250,-6.519054,-2.460122,8.183938,2.717459,-3.406605,6.203938,1.439276,0.047667,-5.446262,7.642049,-4.357853,-2.195303],[1.331840,1.369141,8.977632,9.804718,8.485293,-8.155559,-4.030915,4.290787,-0.470505,-7.658384,3.851737,2.751453,9.073246,-0.501383,-0.138994],[8.718846,-4.716686,6.538985,2.743606,6.367929,-3.961341,7.356175,8.048264,-7.163761,6.484948,9.789566,-6.827864,0.300715,5.850219,1.494040],[-8.553524,7.869389,4.299046,-4.350398,2.731464,1.475662,6.837524,7.523145,-0.725442,-5.897046,-9.727103,-9.233247,-3.953601,-5.525722,4.733068],[-5.956411,3.654272,-4.304380,-6.366044,2.435951,-7.391225,5.668438,6.364510,-9.189181,-0.323141,6.654421,-7.826131,0.704887,1.682301,-0.782743],[-6.156061,-3.356288,-6.620682,-9.787349,3.431464,-4.475827,1.894914,-9.253676,-3.932146,-7.216831,6.052182,1.709111,0.063181,8.491958,6.840718],[4.964167,-8.063623,3.605320,-3.683773,3.926541,5.604141,5.963172,4.709699,9.464639,-7.931314,2.251578,2.211596,1.882292,9.878600,-1.563491],[-5.521243,-2.098406,2.002505,0.469633,-6.886444,-5.837993,-8.325770,-3.083455,1.432508,-1.192144,8.522874,5.139599,-2.550035,8.970679,8.607981]],[[-9.026236,6.978814,-8.328726,-6.459846,-5.394317,-1.179428,-7.256658,-1.201406,6.069589,-3.734003,1.311284,6.703692,9.933741,4.625406,9.872203],[-2.446605,-9.495651,0.125045,-9.744424,-8.306163,-4.901617,4.352897,8.747395,0.800571,2.410654,-3.060716,8.193443,-3.426252,-4.010380,5.049988],[-5.740516,8.394371,1.325397,-8.670865,6.936307,-5.782157,1.025235,-3.773858,3.578544,5.942830,-1.452012,1.425555,6.914954,-9.601332,6.071739],[-5.827310,6.494542,-7.127770,-8.061253,-5.628619,9.959701,5.019208,9.778583,2.933926,2.332114,5.671555,8.282916,6.265170,-9.709684,-9.266796],[3.746837,-3.135728,-9.102524,2.645950,3.036416,-5.639576,-2.073948,8.032621,-3.231190,-7.170746,-2.139026,4.766179,-9.783440,-5.768849,-3.115285],[-8.538812,5.961463,-8.718178,2.028914,-0.726055,6.407021,9.535763,-9.635719,7.124978,6.484185,-5.747110,-2.793853,0.862196,-8.370818,2.173568],[-9.243874,-6.873205,-9.251760,-0.687111,-3.923430,-4.916562,3.961156,2.129200,6.810588,-5.444981,-7.539995,-0.155605,-3.325239,8.847066,0.489087],[0.558229,-8.805964,-3.962840,-3.767305,-0.725487,9.634446,0.393108,-1.069811,7.790967,8.978990,4.105828,-9.182604,-9.788182,8.800662,-7.702334],[2.322740,1.445489,9.010924,-8.628497,-2.998166,2.130212,-3.038640,-7.610878,9.428665,-4.239785,-6.511160,4.798026,9.162320,8.563526,7.027855],[1.980420,-7.925860,9.063978,-5.771186,2.146321,-1.369647,5.027469,9.437797,-6.515694,9.773681,-8.005088,-6.404471,-6.032163,6.638960,-4.071911],[4.576868,0.297420,-2.621080,-2.623068,3.623532,8.229598,-2.183017,-3.241973,1.367140,-3.052264,3.826682,-3.624369,-0.308451,6.891934,-7.027204],[2.890560,7.135817,4.218192,8.174397,9.439088,-6.696850,-8.114894,7.484317,-9.860660,1.082542,5.934664,6.022278,-0.680878,-0.196525,-7.622937]],[[-3.115128,6.471516,-0.264701,5.764612,-3.194990,-5.387485,-5.968540,6.427299,8.822387,-1.207371,-0.503135,9.467352,9.696501,-8.249959,3.312069],[-6.362169,-1.784445,-7.675814,7.882379,-8.446595,-1.361065,-1.786028,5.422955,-8.711087,0.667194,-3.127327,-1.349645,-6.450314,7.895395,5.802768],[1.908349,-8.206958,1.558451,-1.668869,8.686258,-1.247755,-9.829030,-8.178007,-3.295922,-3.818021,7.632409,-8.863797,1.614783,3.984853,9.875856],[2.184240,-9.766053,-8.262687,-7.506920,-2.802687,3.581800,0.003581,7.687849,7.956277,-2.919429,-8.379218,-0.458278,6.710722,5.973405,8.046077],[-8.285373,9.305216,-2.731410,-1.305010,-5.062458,-6.200500,-5.123330,6.336493,0.016285,9.469537,3.543718,6.880759,-9.650365,8.937923,4.753614],[-5.785898,9.571408,8.085139,7.253273,9.846028,-0.317051,5.018036,0.724779,7.048191,-0.610420,0.361214,-7.795092,4.508317,0.057619,-1.627942],[2.770178,-0.380732,-9.065489,6.595038,-1.700164,6.959337,-3.084746,2.328596,-0.521596,9.982773,3.011136,-0.856785,5.568818,8.160376,-8.327023],[-7.477168,-4.615890,-4.046873,-7.175399,0.289649,-4.102357,1.676062,3.071976,1.241591,0.579650,-5.735278,1.953945,-8.848470,8.508232,5.912868],[8.823346,7.427264,0.694345,-6.975102,6.709557,-3.292612,1.570466,8.457894,-4.089858,-1.673881,4.721799,-1.405071,5.847246,5.105473,-4.365705],[-2.922192,-9.978980,-5.432432,1.000605,5.527679,-4.821128,1.321746,-3.163195,-5.637839,4.871567,-2.984805,-6.071744,6.442690,-8.900014,-6.638226],[6.829781,-0.559382,-5.364059,4.476505,-8.518636,2.881550,-1.012062,-1.310445,3.630790,7.947193,8.894732,4.057403,2.504294,4.094267,5.043839],[-1.382900,-0.899892,0.946711,0.999542,-7.500741,1.084102,-4.920357,-5.775216,-8.370638,-5.889529,-0.553700,-9.720552,8.052824,-3.908893,7.212372]],[[-4.681831,9.664036,-6.281543,8.958898,6.821416,9.537940,2.679039,1.055010,-4.173009,6.164877,4.744010,-4.395911,9.638223,4.775989,-4.298084],[-8.283754,2.691367,7.261442,-8.387335,3.246767,5.885647,-6.113853,2.260041,-3.349759,-0.217129,-7.837795,-1.476403,8.430361,-4.024210,4.914890],[8.282900,7.535104,1.692931,-1.472324,8.413883,-3.829822,6.969940,-0.961663,-4.590635,-6.634827,-9.140953,-5.518154,-0.437284,5.683856,6.517393],[6.865575,-4.087207,4.984381,-8.789705,3.077918,7.878014,-1.013540,-5.843739,8.060914,8.376921,7.818080,-0.805024,-7.546229,4.035682,5.703655],[8.015758,7.834932,0.299292,1.550504,7.068701,-7.318499,-0.850131,1.379251,4.354575,5.789612,-1.384974,-0.751695,6.711494,9.723726,-3.375609],[0.130973,-6.263509,8.194319,9.459503,3.021988,0.447228,0.658291,-1.040812,8.542588,-9.328454,-6.011627,6.592154,2.567854,-9.243623,-6.409303],[-9.050334,-5.874379,-0.366663,-6.583070,-3.717762,-7.628377,0.968299,-6.249415,-1.897973,3.912227,-9.354285,-6.576404,3.337964,-8.312128,-4.121583],[-0.482854,-0.864211,7.688078,8.563853,-8.582780,8.324465,7.981337,6.083585,-4.152432,8.544354,-1.399350,-0.972846,-7.758976,-9.034812,5.720948],[9.294568,4.958239,-5.203592,-2.893628,8.611742,8.563394,-6.205797,3.957020,-2.787395,5.043110,-2.721873,-5.123080,-0.203957,-1.286533,3.412482],[-7.735684,5.880572,7.559078,-0.864520,9.106341,-8.490757,1.615140,-2.399997,-6.713954,-8.865728,-5.718639,1.716802,2.947824,8.852561,8.578342],[1.365822,7.698599,7.550507,-1.093664,8.675611,0.981833,2.254605,-7.965942,-5.694993,-9.815680,-5.397619,4.670289,9.170073,-8.542678,-2.681607],[-7.791183,2.470102,-6.838917,-4.370685,-8.590652,4.055752,6.420835,-8.537980,-1.028283,8.821818,-0.248139,8.620400,9.504208,-2.219973,-6.810943]],[[0.134052,6.850206,-6.473973,-1.429428,-4.260272,-8.757840,-2.925306,-8.731826,3.221053,6.534003,-7.746145,0.207738,0.764930,-1.326994,-7.853252],[-5.682660,6.155198,-5.122304,-6.704669,-8.094086,8.735641,-5.193948,0.941774,8.044496,2.833792,9.446520,-3.918728,1.078207,7.454429,9.762156],[-3.019664,-0.523080,6.209159,-2.568002,6.346999,2.690943,0.350898,-4.469437,-2.044371,-0.698391,3.280636,5.738655,-7.105004,0.814955,2.493008],[4.882092,6.052800,1.591461,-9.819247,-8.006376,8.406239,-9.429412,2.224660,7.968408,-4.337504,9.374888,5.840978,7.505317,2.090406,8.188242],[-3.066077,5.963630,-3.163003,-4.316599,-2.235938,-8.453431,-2.363944,-1.675494,-5.782105,-9.961290,3.484029,-6.657470,-4.672578,-4.859076,-7.125981],[-1.702201,-3.832281,-4.758621,1.711852,5.296646,2.153259,4.082095,7.539741,8.401548,2.251521,-9.427910,1.564088,0.342941,3.570684,-9.070508],[9.368538,-6.870274,-1.235002,2.254553,7.665605,5.472434,-8.383840,7.885396,-2.543289,0.385889,-7.332106,9.688515,-3.971095,9.236179,-9.269495],[-3.173777,8.810560,-2.141401,2.942690,4.826966,-9.358804,-3.154185,4.682331,-6.222155,-3.977703,4.853628,-2.789446,3.755948,4.365355,-3.445121],[-9.426064,8.829195,6.204974,0.981516,7.540555,2.186756,8.627140,9.363226,8.536791,-4.696125,9.445920,-7.401967,-4.091599,2.207728,7.735513],[-9.367604,-1.906036,5.665137,5.551426,-8.304754,3.316563,-2.780803,5.822984,7.052528,-6.340817,5.347627,0.055928,2.176961,1.321157,6.975647],[-0.852824,-3.409070,4.621789,-7.896515,-5.888413,-1.567565,-1.416888,-0.473489,-7.688756,5.709727,8.355334,-5.689117,-5.872066,5.686070,-8.896554],[-6.533713,-3.830321,1.936572,-1.177196,-9.602925,8.901822,-8.823864,7.668580,7.889362,-2.760655,-2.020578,8.499293,-6.001737,-3.858428,5.199335]],[[-0.924111,9.263689,-3.649435,9.740771,-4.678201,4.112874,-8.695490,-4.979058,-7.577748,1.548566,-0.971189,7.543089,-1.548067,7.604011,1.992339],[-7.627999,9.894206,-2.553672,-3.822806,-6.739294,7.412912,-1.919322,-8.737888,8.355497,9.233276,7.612644,7.376298,1.611017,6.125028,-9.769827],[-2.609047,-8.600319,1.442801,8.444744,-7.940084,-5.957856,-2.334717,5.757310,2.904806,9.796973,0.523764,-9.761995,9.504146,3.137429,9.383791],[1.523928,-9.180333,5.496607,-3.387897,3.490107,-7.107726,-7.658307,6.154866,2.648156,5.321643,2.931419,-9.248520,1.674823,5.688152,-6.895743],[-0.058686,-8.523667,7.479761,-7.673813,9.529644,8.961037,-1.857801,-1.491022,3.118608,-7.997066,-4.392837,-8.056478,-2.006204,7.000161,-3.642732],[-6.031792,4.587382,7.018573,-7.129319,7.984665,3.552401,4.801606,-9.955862,3.028456,-1.554306,-5.799761,4.870731,2.090327,-4.026297,-2.037304],[-8.630041,-4.401605,9.732555,-0.768534,2.993789,5.401996,-7.133439,-3.859805,-1.870035,4.469988,-5.761699,-5.453581,-0.372776,7.790485,-3.528425],[3.953665,-4.905265,-6.985326,8.565032,2.690553,-2.912961,1.790893,6.085442,-9.045098,-3.321230,-8.052065,5.920415,-4.999348,-8.758265,6.034012],[3.649993,5.241727,-6.797684,-2.287338,5.862409,-2.697722,-8.688027,-4.260973,-8.682119,-3.788194,-9.586253,6.319036,7.718866,4.053458,1.487158],[-6.213107,3.568692,-8.130478,8.201482,2.552790,-4.365605,2.236737,-1.405869,-8.978921,-3.228988,4.355186,-8.843706,-8.199329,-9.955113,5.320000],[-8.103473,1.622253,-8.136912,5.010224,-3.627527,-5.240383,8.112575,6.785029,6.197740,-2.965899,-5.977624,9.602381,-2.805848,-9.878176,6.705268],[-2.375420,4.203707,-2.040473,4.302698,-6.746434,-3.125708,-7.175225,-0.419450,8.994973,4.880097,2.686933,0.304437,-5.012612,-0.188460,5.335540]],[[4.620934,-1.670358,4.411501,-7.992991,-0.960145,-6.567179,6.873191,-8.802716,-3.769433,6.011744,0.790074,-6.116311,0.008517,-3.789172,5.365269],[-2.421849,8.626846,-5.814740,0.401132,2.468360,1.045485,-8.162159,-0.090519,-0.973890,9.298199,3.861022,-1.568089,6.459869,-1.595157,0.437214],[2.244401,-3.665709,-0.932984,7.008138,7.261485,-4.910183,-2.064768,0.866519,9.094499,-6.383675,-6.801148,-6.684289,7.122468,-4.582869,6.499447],[8.410692,5.738753,-1.040422,-0.750926,4.154853,-3.258715,-5.842673,3.982092,-7.703053,2.113116,4.116309,-2.860989,-5.726506,4.991232,4.290503],[7.223176,-6.061380,1.287015,-6.438790,-5.398458,0.896924,2.714155,-8.454746,-3.462961,-7.624498,5.893375,1.172914,9.534262,2.202145,-8.157490],[9.441404,6.755701,4.686861,-6.500258,4.400906,0.247959,-3.838307,-5.196314,0.944094,4.362275,5.939412,6.426790,-8.507802,-6.028060,-2.744636],[-9.017843,-5.577020,8.121900,-8.987320,-4.859832,-5.554602,5.691383,-4.435717,2.670446,-7.717148,1.780152,2.509143,-3.964716,1.843612,9.442427],[8.505560,-0.013736,-1.829432,4.183627,4.164580,-7.410698,-5.160236,-6.108084,3.820461,-8.303516,-1.996987,5.379883,6.365600,8.976792,6.034605],[-2.222866,2.632425,-1.993954,-2.345520,-5.494826,1.437565,5.390544,-3.903247,8.756192,-7.611024,8.620261,2.509567,-0.472280,-7.631986,-3.615011],[3.240176,1.522632,1.918241,-9.665188,3.313737,2.114754,6.576237,-7.055785,9.321796,2.206341,-1.662062,-5.418026,-4.603138,-0.572702,3.565901],[-4.667301,7.020196,9.579011,8.256340,-3.285091,-7.196116,-3.727108,-2.872441,-0.404707,-5.487444,0.639569,-7.793104,-1.641926,1.778566,-7.796679],[4.671828,2.459383,-3.170906,5.121906,-3.855286,-3.904556,-9.679961,-3.945216,-2.503900,-6.444496,-5.109107,0.607042,5.550401,2.627325,-9.794584]],[[7.775031,-8.597389,-5.688232,2.353764,9.878502,6.221720,0.578917,-6.596762,-1.237019,-1.060204,3.769890,4.183985,8.818157,-7.064160,3.372899],[-7.992057,4.382771,0.072155,8.565242,3.379630,-6.713017,4.536231,-2.796929,3.435297,-8.661218,5.149153,-3.419503,-4.268567,-9.993904,7.199215],[0.466324,-0.366031,-2.130831,-6.030048,6.141618,-3.590467,-8.596965,9.723164,8.843878,8.550221,-6.510253,7.428338,5.953627,-6.586690,8.935545],[3.850297,-2.390503,6.305831,3.903222,-0.185602,8.390651,-3.137795,-9.974240,6.479351,-5.426533,2.805026,6.345408,-6.609426,-3.650995,-9.897285],[-8.787264,-7.863016,-3.356081,2.046585,9.624227,-8.130941,3.972649,-9.891705,-7.113661,6.898695,3.954683,4.110446,-7.066894,2.842636,-9.058637],[-1.410063,-2.170380,4.872943,-0.395483,-6.493814,5.401598,-5.349056,-3.445476,-7.910219,-1.226966,8.777522,6.658151,4.073071,-7.157788,-5.744294],[-6.751439,6.424191,-7.961638,8.707071,-9.742461,-1.407871,-6.283297,-0.569939,-9.634513,6.698935,-9.690549,-0.736069,9.544116,2.729807,-2.884213],[6.067438,-9.552306,2.264963,7.697311,9.431938,4.016007,1.404897,0.686161,-6.348261,8.998236,-4.653937,-4.656237,2.970411,-3.661023,-5.874674],[-4.866075,-9.444905,-7.156360,9.882770,-3.579187,1.948817,2.592801,-2.942228,-4.082661,-9.357010,-2.423632,-3.112853,3.866603,1.006742,-2.118499],[-9.976044,8.154018,-0.483576,7.437373,0.838408,-0.606294,1.055970,-2.350916,-9.181247,-7.214213,-0.685776,-5.465854,1.417593,-5.232375,6.852272],[-6.066951,5.213605,-8.758270,-3.454541,-2.335435,-1.193749,-1.395444,-7.764452,2.555976,-4.211454,6.595123,-0.709072,9.033410,1.139053,-9.154216],[-6.662703,-7.644427,-5.012219,2.372671,-2.154519,3.249270,1.059034,-5.896997,-8.036193,-9.793055,5.056243,3.770919,0.246375,-9.979370,-0.865289]],[[-1.599740,4.527241,-8.345199,2.868135,-6.289967,2.978654,-7.435577,-6.409184,-2.086640,-2.417878,7.913768,-4.911025,-3.112228,4.087969,-8.200971],[8.041379,-8.824976,-1.330012,7.157266,2.487822,1.117458,4.520088,3.732211,9.270674,-3.880660,-5.512157,4.529861,-3.075304,6.346349,-2.531985],[7.040655,-5.355943,9.974034,-1.967377,-6.088523,-7.944963,2.331775,-7.616296,1.558273,-7.763730,7.277647,5.404455,-7.600537,-2.639827,6.271104],[9.230720,8.581198,8.381933,-7.688669,3.030646,0.080391,6.376350,9.429140,5.142023,9.421283,-6.934869,-3.709434,0.918496,5.304686,-5.785878],[8.815583,8.747989,6.152431,0.241227,-8.360189,8.406788,-5.118370,-9.681214,-9.568114,3.255281,-3.020602,-4.441514,5.366548,7.994975,-0.372243],[-1.178096,5.312912,-4.799911,-0.418833,5.060933,-2.784186,-4.764052,8.836490,-3.270918,-9.632942,5.927780,6.744472,8.104101,7.129780,1.132730],[0.512924,6.861392,7.847809,6.474775,0.554663,-2.864466,9.267054,4.466721,-9.070868,-1.434884,4.859901,7.127911,-2.911127,9.178364,3.554505],[5.104228,-9.193184,5.772805,-6.642207,5.868163,6.646092,6.722992,-9.380608,1.450808,-4.381142,3.960779,7.800969,-8.517328,-5.609457,-0.750870],[-1.553405,-3.999873,-0.246342,-3.733142,-9.828664,9.610592,5.451924,2.356801,2.261489,-5.910682,-6.567719,3.045271,-9.211233,0.801417,2.462191],[-4.859348,2.714884,6.160625,1.667395,-6.213549,1.955498,5.600214,-6.777989,4.325698,-4.606510,8.072473,7.962598,-0.151204,-1.084208,-4.391257],[1.929083,1.454440,4.480781,9.850558,-4.663921,5.946656,3.236869,0.335886,5.584106,8.386547,-5.686785,-4.648886,9.620539,-4.739785,5.073019],[7.149227,2.527555,5.975963,8.062780,0.432266,5.868283,-3.587080,-8.360816,-2.196996,-2.725386,9.667414,0.554827,-1.729888,-0.247948,-2.042576]],[[-2.297843,4.127154,6.467350,-6.822425,4.423361,-2.687161,-8.391568,3.663329,-4.144681,-6.121874,5.169194,-8.167257,-4.414705,6.704694,2.405295],[-7.312290,9.937022,6.369882,-4.515548,-5.453998,-0.488267,-4.141685,8.326925,1.837818,-3.651903,-9.401471,7.302240,-2.468036,1.331064,-0.004058],[2.405129,-9.521958,-5.570252,4.112154,-8.403381,-9.543432,5.601000,3.381031,-3.212025,-9.920358,6.288463,-4.803044,3.824435,-4.145556,-8.246284],[5.518427,2.323027,5.334239,-9.222859,-7.063813,-4.704335,8.733907,-5.163064,-7.328349,8.712347,3.812814,6.065262,6.977737,-5.250232,2.522462],[-4.266132,-6.658716,4.745947,-1.645213,4.572892,-5.777281,4.443963,3.450572,-8.358344,2.768386,-7.070020,-9.630014,-2.711372,8.791240,3.385523],[-6.806238,9.736648,9.950864,-1.910276,-1.678491,1.888025,3.683255,-9.613003,-0.863771,-5.417419,-7.654956,-4.011799,-3.017828,-6.429073,1.527426],[-4.982496,-2.639023,-9.672063,-2.874963,1.315836,-3.741180,8.727863,9.711427,-9.661960,9.258215,1.529059,-2.802788,-6.230996,1.670668,-6.989828],[9.563344,-7.553793,-0.454165,1.305959,9.157069,-1.638430,4.354556,8.735508,9.286725,-4.815030,-0.154019,6.250136,6.854303,7.825750,-0.043726],[5.510892,-8.585248,4.408369,8.869623,-5.242152,8.537498,-1.327451,-7.785508,-0.201150,-1.908701,-4.376653,-7.312465,9.506343,-7.125450,-3.071523],[-7.209299,-3.583264,0.784372,7.373388,-6.084654,2.382989,-8.549821,2.700384,0.326491,9.002721,-3.457590,-2.871556,6.984257,8.838030,-4.948326],[-6.509245,5.681409,-6.788146,5.882963,9.312757,3.344361,6.766594,6.727829,-1.986657,-2.322669,-4.747197,-7.464405,-1.255088,-5.406475,2.519201],[0.222407,7.681412,-8.845249,-5.749628,9.893459,2.900755,-3.112397,5.216743,7.129372,5.742001,4.118411,0.674682,-5.635997,1.245846,7.614623]],[[-5.850011,-8.799216,8.221020,2.239530,-0.997060,-9.169484,1.089518,8.468363,-9.314173,-1.551784,-8.306824,2.936446,0.096235,4.453045,-4.432196],[0.931804,-3.282695,-4.011771,-8.645520,5.002034,-2.234333,1.657778,-8.838778,-0.344747,3.857397,-6.196271,-8.938527,5.662447,-5.844153,-6.620884],[8.134330,5.713747,-1.745142,-8.560606,0.715330,5.335271,3.645615,2.650284,5.864203,-7.879160,-5.048682,7.938342,-9.338502,2.909325,9.822886],[1.949057,1.437931,-6.691233,-1.103131,2.503371,-3.617099,3.153106,2.248078,-1.385232,0.635578,2.904699,3.113771,-7.003206,-4.725762,-8.944347],[-1.696352,-4.327688,-9.866685,8.063056,4.328289,-8.405920,1.556143,3.609065,-8.783238,-2.596554,-4.432175,-0.532331,-8.043992,0.071364,-9.942635],[-0.614826,2.382254,-3.475728,-1.936094,-8.350333,-0.378391,4.798819,7.948328,-3.050851,-9.993109,5.339905,1.368831,8.574203,-9.827890,-9.572779],[-5.763402,1.384001,5.673261,-2.424202,6.580654,-4.516831,4.356767,-6.097111,-6.787493,2.815146,4.757020,-3.043523,-5.846527,-0.401915,-4.815077],[9.085868,2.221404,4.712318,-8.966018,-1.370018,-7.138354,-9.784385,5.011343,-3.158613,6.724541,-6.973726,-6.935752,4.306039,-8.687879,-7.541731],[-9.752982,-3.312319,-9.952907,0.890333,2.995358,8.366386,-6.945292,5.640630,-8.569072,7.349332,9.626153,-8.697145,-0.852878,-7.854259,2.130609],[-4.061033,-0.882977,8.202028,-2.859018,-1.485919,3.898607,4.491934,9.488216,7.999272,1.158391,8.104268,-3.784952,-7.171592,-5.367704,-7.531766],[1.543549,4.083124,7.586271,8.599472,0.503685,8.860844,2.508128,-9.071054,9.230915,-7.050561,8.023236,-6.926298,7.734872,-5.598098,3.689417],[8.746720,6.033502,7.878565,3.799616,-1.178268,-8.518502,2.161103,1.967679,-3.091928,5.756997,2.835539,-7.593927,9.736052,-6.467905,2.675127]],[[-2.950185,6.783348,-5.153474,-4.748731,1.996042,-0.059195,-5.562340,9.071745,-5.369588,-6.324917,-7.721306,-4.241853,6.783474,-6.086530,3.232389],[-1.233337,-3.781285,-6.033202,-5.664093,-4.809022,3.741953,0.529686,9.637969,1.888984,-9.152638,6.050418,7.865102,3.215559,3.304244,1.354485],[-3.628113,-2.562814,3.919692,1.765816,2.410295,3.625529,-8.130874,-8.482944,1.877330,0.868827,-2.097536,-3.214060,-7.434724,-8.892979,0.862524],[7.349389,0.653102,-8.707477,-2.834003,-5.242320,7.425950,-3.469542,-3.607871,6.555017,8.156565,8.296510,-0.498826,1.498229,-0.650412,-7.600494],[1.896367,9.009040,-8.601670,2.145009,6.031902,-0.554692,5.490784,-5.231518,-9.464248,1.081272,0.777512,6.727170,-1.530479,-8.568629,-6.785293],[-6.599218,-1.933790,0.695715,0.393485,0.964244,-9.973409,-9.126651,1.226483,-8.252275,-7.608802,0.701780,-5.197647,7.432252,8.229210,4.613036],[5.529569,-3.439448,0.491717,-7.407687,-9.325679,7.344823,8.299975,9.651905,7.019385,-1.320372,5.917808,8.644073,-0.339069,9.943321,-0.407045],[-7.099733,-6.222913,-7.382173,-8.415385,7.217541,-9.298104,8.748256,-4.448383,-6.878301,-6.334659,2.305912,-2.672552,-3.548815,-9.409243,2.344488],[-2.076222,-7.775360,-4.217562,3.628906,2.652265,5.286131,5.381301,5.457208,1.514550,1.728871,7.805398,-9.765217,2.414421,-1.607517,-7.757773],[9.557762,7.270418,4.330231,-9.199172,-4.248489,3.058734,1.335412,0.705278,-3.963620,5.719520,-9.161894,2.570355,-7.556316,3.563078,-2.698401],[-3.206512,9.013945,5.702276,6.586984,0.221987,4.964871,-9.791695,9.213173,5.141451,-2.814347,-9.824200,7.117020,1.742549,-3.066436,9.305329],[-9.372655,-7.220469,7.349863,2.068489,0.360576,6.179566,5.768018,-2.158175,9.675348,3.012357,-3.203712,-8.600510,8.145303,2.510251,0.191432]],[[-7.362238,8.807258,4.091031,-9.707937,5.910740,5.038844,-2.796873,-6.752628,9.127951,-7.668668,-2.449951,-6.720002,8.099362,-1.753691,-2.687509],[7.999145,-6.701720,4.550919,3.572120,-2.232870,-7.000076,2.805432,-1.486625,7.199353,6.609466,-9.400090,-1.429314,9.144663,-3.786229,-9.490816],[8.981052,0.150726,-5.663114,1.585245,-4.698608,3.532565,7.979540,8.441077,-6.386680,1.276187,6.400962,1.062810,1.273965,5.273684,7.650596],[-4.524756,3.159913,-8.949026,-6.716768,4.404135,4.290639,4.296589,-0.647832,-5.187990,7.540477,-0.067015,-3.094436,-8.897026,-4.282796,1.986517],[-5.850654,-5.530766,-7.842492,6.460871,-4.545349,7.028687,6.067571,-4.383118,-2.587127,6.437446,4.794461,-4.217550,8.641504,7.655955,-0.406168],[2.641590,-8.488652,-7.885456,-5.200671,6.468081,-3.812938,-1.504269,-2.197005,0.850129,-3.632590,-6.076468,0.909378,8.104598,-1.214188,-4.893033],[8.300726,8.813981,-1.167120,-0.543679,7.147092,4.893528,3.716747,-0.575074,9.881019,-7.280506,-6.916370,2.002649,0.646710,-4.372702,3.729104],[-7.888565,4.154725,-8.349763,7.759760,-0.745954,-7.416385,-8.441629,-2.371285,0.581336,0.684879,2.739409,7.837008,9.676444,8.025513,-3.743707],[-1.005712,4.225109,-2.176844,0.979875,8.795808,-5.656591,-5.744480,4.042924,5.234446,-1.065752,-3.875871,-8.369161,-5.843225,-9.548711,-7.311546],[-8.262886,2.081051,-3.525800,4.880173,5.692230,9.826243,-9.730701,-5.011563,-6.386771,9.668514,-2.869962,-6.185149,5.284829,-8.914405,-7.848906],[-8.220408,-4.826872,1.145081,2.141147,-1.855799,8.238788,-6.430684,1.908231,2.128415,1.415755,-5.000547,-3.645466,-0.749024,8.259046,6.004421],[2.859153,-7.667741,2.407945,-4.055607,-6.389186,7.204563,7.161935,-9.286343,-7.317775,-7.163728,-8.150749,-9.406985,-5.854195,-0.382175,4.231215]]], dtype = "float32")#candidate|6226|(15, 12, 15)|const|float32
bop_6227 = relay.mod(call_6223.astype('float32'), const_6226.astype('float32')) # shape=(15, 12, 15)
bop_6230 = relay.mod(call_6224.astype('float32'), const_6226.astype('float32')) # shape=(15, 12, 15)
output = relay.Tuple([bop_6227,])
output2 = relay.Tuple([bop_6230,])
func_6231 = relay.Function([], output)
mod['func_6231'] = func_6231
mod = relay.transform.InferType()(mod)
mutated_mod['func_6231'] = func_6231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6231_call = mutated_mod.get_global_var('func_6231')
call_6232 = func_6231_call()
output = call_6232
func_6233 = relay.Function([], output)
mutated_mod['func_6233'] = func_6233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5736_call = mod.get_global_var('func_5736')
func_5737_call = mutated_mod.get_global_var('func_5737')
call_6237 = relay.TupleGetItem(func_5736_call(), 0)
call_6238 = relay.TupleGetItem(func_5737_call(), 0)
uop_6265 = relay.atan(call_6237.astype('float32')) # shape=(1, 12, 15)
uop_6267 = relay.atan(call_6238.astype('float32')) # shape=(1, 12, 15)
uop_6273 = relay.cos(call_6237.astype('float32')) # shape=(1, 12, 15)
uop_6275 = relay.cos(call_6238.astype('float32')) # shape=(1, 12, 15)
bop_6292 = relay.minimum(uop_6273.astype('float32'), relay.reshape(call_6237.astype('float32'), relay.shape_of(uop_6273))) # shape=(1, 12, 15)
bop_6295 = relay.minimum(uop_6275.astype('float32'), relay.reshape(call_6238.astype('float32'), relay.shape_of(uop_6275))) # shape=(1, 12, 15)
output = relay.Tuple([uop_6265,bop_6292,])
output2 = relay.Tuple([uop_6267,bop_6295,])
func_6300 = relay.Function([], output)
mod['func_6300'] = func_6300
mod = relay.transform.InferType()(mod)
mutated_mod['func_6300'] = func_6300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6300_call = mutated_mod.get_global_var('func_6300')
call_6301 = func_6300_call()
output = call_6301
func_6302 = relay.Function([], output)
mutated_mod['func_6302'] = func_6302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6300_call = mod.get_global_var('func_6300')
func_6302_call = mutated_mod.get_global_var('func_6302')
call_6344 = relay.TupleGetItem(func_6300_call(), 1)
call_6345 = relay.TupleGetItem(func_6302_call(), 1)
output = call_6344
output2 = call_6345
func_6347 = relay.Function([], output)
mod['func_6347'] = func_6347
mod = relay.transform.InferType()(mod)
mutated_mod['func_6347'] = func_6347
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6347_call = mutated_mod.get_global_var('func_6347')
call_6348 = func_6347_call()
output = call_6348
func_6349 = relay.Function([], output)
mutated_mod['func_6349'] = func_6349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5929_call = mod.get_global_var('func_5929')
func_5931_call = mutated_mod.get_global_var('func_5931')
call_6447 = relay.TupleGetItem(func_5929_call(), 0)
call_6448 = relay.TupleGetItem(func_5931_call(), 0)
func_5278_call = mod.get_global_var('func_5278')
func_5282_call = mutated_mod.get_global_var('func_5282')
const_6455 = relay.const([[-1,3,-2,1,-3,4,-9,4,-4,6,-7,-8,9,2,5,10,-2,1,3,10,8,1,4,3,-4,-3,-3,7,-10,10,3,-1,-2,-9,-4,-3]], dtype = "int64")#candidate|6455|(1, 36)|const|int64
var_6456 = relay.var("var_6456", dtype = "uint16", shape = (495,))#candidate|6456|(495,)|var|uint16
call_6454 = relay.TupleGetItem(func_5278_call(relay.reshape(const_6455.astype('int64'), [36,]), relay.reshape(var_6456.astype('uint16'), [495,]), ), 6)
call_6457 = relay.TupleGetItem(func_5282_call(relay.reshape(const_6455.astype('int64'), [36,]), relay.reshape(var_6456.astype('uint16'), [495,]), ), 6)
output = relay.Tuple([call_6447,call_6454,const_6455,var_6456,])
output2 = relay.Tuple([call_6448,call_6457,const_6455,var_6456,])
func_6468 = relay.Function([var_6456,], output)
mod['func_6468'] = func_6468
mod = relay.transform.InferType()(mod)
mutated_mod['func_6468'] = func_6468
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6469 = relay.var("var_6469", dtype = "uint16", shape = (495,))#candidate|6469|(495,)|var|uint16
func_6468_call = mutated_mod.get_global_var('func_6468')
call_6470 = func_6468_call(var_6469)
output = call_6470
func_6471 = relay.Function([var_6469], output)
mutated_mod['func_6471'] = func_6471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5929_call = mod.get_global_var('func_5929')
func_5931_call = mutated_mod.get_global_var('func_5931')
call_6473 = relay.TupleGetItem(func_5929_call(), 0)
call_6474 = relay.TupleGetItem(func_5931_call(), 0)
var_6490 = relay.var("var_6490", dtype = "float32", shape = (15, 12, 15))#candidate|6490|(15, 12, 15)|var|float32
bop_6491 = relay.power(call_6473.astype('float64'), var_6490.astype('float64')) # shape=(15, 12, 15)
bop_6494 = relay.power(call_6474.astype('float64'), var_6490.astype('float64')) # shape=(15, 12, 15)
output = relay.Tuple([bop_6491,])
output2 = relay.Tuple([bop_6494,])
func_6500 = relay.Function([var_6490,], output)
mod['func_6500'] = func_6500
mod = relay.transform.InferType()(mod)
var_6501 = relay.var("var_6501", dtype = "float32", shape = (15, 12, 15))#candidate|6501|(15, 12, 15)|var|float32
output = func_6500(var_6501)
func_6502 = relay.Function([var_6501], output)
mutated_mod['func_6502'] = func_6502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6300_call = mod.get_global_var('func_6300')
func_6302_call = mutated_mod.get_global_var('func_6302')
call_6506 = relay.TupleGetItem(func_6300_call(), 1)
call_6507 = relay.TupleGetItem(func_6302_call(), 1)
func_5278_call = mod.get_global_var('func_5278')
func_5282_call = mutated_mod.get_global_var('func_5282')
const_6511 = relay.const([-1,7,4,4,10,-4,1,7,-4,-3,-10,-3,9,4,-9,-5,6,8,-4,7,-10,-2,-9,-2,-1,5,5,2,5,5,4,6,-4,10,-5,-1], dtype = "int64")#candidate|6511|(36,)|const|int64
var_6512 = relay.var("var_6512", dtype = "uint16", shape = (5, 99))#candidate|6512|(5, 99)|var|uint16
call_6510 = relay.TupleGetItem(func_5278_call(relay.reshape(const_6511.astype('int64'), [36,]), relay.reshape(var_6512.astype('uint16'), [495,]), ), 2)
call_6513 = relay.TupleGetItem(func_5282_call(relay.reshape(const_6511.astype('int64'), [36,]), relay.reshape(var_6512.astype('uint16'), [495,]), ), 2)
func_2536_call = mod.get_global_var('func_2536')
func_2539_call = mutated_mod.get_global_var('func_2539')
const_6516 = relay.const([-9.520285,7.185643,8.707901,-4.221350,6.195247,-5.656452,5.977462,6.640713,7.690195,-5.061548,-1.121489,-8.860976,-7.952382,-3.448064,8.527514,-4.386232,1.253520,-5.916473,1.684285,0.869751,6.943322,3.579479,-5.646623,8.799944,-8.472017,-7.518898,8.395546,1.554960,-9.353084,6.825125,6.538501,5.382645,1.594661,4.088987,1.104098,-9.578138,5.243319,3.729694,-9.599000,7.387689,-5.785240,9.117196,-3.943592,1.812514,-9.460309,-7.506900,-2.192191,-3.066025,-2.784763,-6.820079,-1.712377,-9.896621,-7.515726,1.885985,9.923495,-2.821350,-1.776060,1.117548,-3.726517,2.909766,-2.067026,5.256046,-2.402707,-8.357834,0.983964,-3.210920,5.421755,0.537349,-1.928183,-7.504420,4.794374,4.767039,-8.630136,-4.677464,8.003805,8.779063,-3.743039,-8.550942,-9.679868,5.085585,0.056500,1.121136,-2.448555,-1.675629,9.068534,-6.923367,7.012574,-4.979414,5.643539,1.594729,6.236660,-5.497698,2.617211,-7.310641,7.709867,9.332610,8.467867,-1.176657,-5.180724,-0.981520,0.460748,-8.935655,-5.760499,1.332906,-1.747403,-6.136440,5.993076,9.211324,3.240383,4.176889,4.426412,7.313104], dtype = "float64")#candidate|6516|(112,)|const|float64
call_6515 = relay.TupleGetItem(func_2536_call(relay.reshape(const_6516.astype('float64'), [16, 1, 7])), 0)
call_6517 = relay.TupleGetItem(func_2539_call(relay.reshape(const_6516.astype('float64'), [16, 1, 7])), 0)
uop_6519 = relay.acosh(const_6511.astype('float64')) # shape=(36,)
output = relay.Tuple([call_6506,call_6510,var_6512,call_6515,const_6516,uop_6519,])
output2 = relay.Tuple([call_6507,call_6513,var_6512,call_6517,const_6516,uop_6519,])
func_6539 = relay.Function([var_6512,], output)
mod['func_6539'] = func_6539
mod = relay.transform.InferType()(mod)
mutated_mod['func_6539'] = func_6539
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6540 = relay.var("var_6540", dtype = "uint16", shape = (5, 99))#candidate|6540|(5, 99)|var|uint16
func_6539_call = mutated_mod.get_global_var('func_6539')
call_6541 = func_6539_call(var_6540)
output = call_6541
func_6542 = relay.Function([var_6540], output)
mutated_mod['func_6542'] = func_6542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5929_call = mod.get_global_var('func_5929')
func_5931_call = mutated_mod.get_global_var('func_5931')
call_6596 = relay.TupleGetItem(func_5929_call(), 0)
call_6597 = relay.TupleGetItem(func_5931_call(), 0)
output = relay.Tuple([call_6596,])
output2 = relay.Tuple([call_6597,])
func_6604 = relay.Function([], output)
mod['func_6604'] = func_6604
mod = relay.transform.InferType()(mod)
mutated_mod['func_6604'] = func_6604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6604_call = mutated_mod.get_global_var('func_6604')
call_6605 = func_6604_call()
output = call_6605
func_6606 = relay.Function([], output)
mutated_mod['func_6606'] = func_6606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6107_call = mod.get_global_var('func_6107')
func_6109_call = mutated_mod.get_global_var('func_6109')
call_6661 = relay.TupleGetItem(func_6107_call(), 0)
call_6662 = relay.TupleGetItem(func_6109_call(), 0)
const_6663 = relay.const([[[9.221444,-0.735264,-5.910383,-5.232103,-9.336363,-4.237580,4.669405,0.902298,-4.097357,-2.682430,-6.335654,-8.016943,-3.076741,2.911217,2.774939],[-3.789586,1.543567,7.233339,-5.469224,2.087912,1.396907,-5.752742,1.652901,4.565312,4.524045,3.004339,9.912756,-4.019977,-7.997140,7.492661],[9.790742,0.379740,-3.980250,-9.407518,-9.205347,8.742301,3.719465,-8.853346,-3.364769,8.098203,1.682189,6.199231,-4.306325,4.959717,8.992012],[-5.270754,-2.009295,2.305515,7.409218,0.637915,7.830303,3.793003,8.871747,4.557349,-7.339841,1.126284,-4.784450,-4.625568,-4.877600,6.372683],[-2.870990,-7.805452,9.856724,5.506499,1.867452,-3.582679,-8.001971,-1.159973,8.794072,5.318238,-2.435164,-6.381107,1.410167,4.149051,-4.780946],[8.959739,4.072365,2.132891,-3.949229,3.004397,3.983094,-9.886397,6.719316,0.678579,9.145013,-6.142367,4.370368,-4.605024,4.044269,8.762485],[-3.190013,-3.884720,-2.218369,4.930741,0.717464,7.973937,-5.493543,-8.949778,-4.480736,8.088729,-2.932639,3.134339,-5.320604,-0.826805,8.462696],[0.678427,-1.196978,3.808450,3.312597,1.666511,6.134377,2.640893,0.617244,-8.733559,-6.445725,6.273390,9.341603,-3.152862,-5.481800,-9.074154],[-9.962513,0.912359,1.037198,-0.843749,5.809302,7.447335,-0.849797,9.400210,-1.694643,8.605735,2.536353,1.297896,3.478318,-2.077564,-8.268421],[8.787660,-1.144386,-2.852975,-2.919625,-8.599023,-0.445699,-2.624053,-3.618709,-9.733284,7.588138,0.957698,-4.636872,-7.528707,3.004011,6.540652],[3.184919,-0.308748,-0.917892,0.754136,6.273141,-9.141088,-1.169393,-6.134869,-2.892114,3.866937,-8.208373,-6.508501,-5.922669,-6.804546,7.912452],[0.478633,3.278615,-0.611293,-9.521867,-7.024050,1.516693,-5.571396,2.346848,2.574772,1.643284,-3.893284,4.452340,7.267077,1.093899,6.901266]]], dtype = "float32")#candidate|6663|(1, 12, 15)|const|float32
bop_6664 = relay.right_shift(call_6661.astype('int64'), relay.reshape(const_6663.astype('int64'), relay.shape_of(call_6661))) # shape=(1, 12, 15)
bop_6667 = relay.right_shift(call_6662.astype('int64'), relay.reshape(const_6663.astype('int64'), relay.shape_of(call_6662))) # shape=(1, 12, 15)
bop_6679 = relay.bitwise_and(const_6663.astype('uint16'), relay.reshape(bop_6664.astype('uint16'), relay.shape_of(const_6663))) # shape=(1, 12, 15)
bop_6682 = relay.bitwise_and(const_6663.astype('uint16'), relay.reshape(bop_6667.astype('uint16'), relay.shape_of(const_6663))) # shape=(1, 12, 15)
func_4631_call = mod.get_global_var('func_4631')
func_4634_call = mutated_mod.get_global_var('func_4634')
const_6685 = relay.const([[7.703061,-6.592377,-0.761652,6.285258,-6.249614,-6.645607,-0.086588,-6.120203,-6.930173,8.630743,-3.799723],[-9.445941,4.113812,-4.519005,1.847401,-7.076969,7.453162,-8.206525,5.078677,0.489273,4.792430,-8.278643],[4.316122,-6.394668,-0.713502,-0.292823,-2.188434,1.803997,-4.202295,5.691783,9.620256,4.743657,4.980957],[-6.325849,5.499907,-4.942066,0.350128,-2.314621,6.217903,-5.057562,-0.631967,1.564160,1.699371,-2.707909],[-5.582360,4.733975,4.532499,-6.759977,-7.865933,9.724164,1.545585,8.401624,4.688285,3.826520,-1.904909],[-2.614701,-8.586557,2.284757,6.247223,6.827119,3.639596,5.188921,1.654403,4.701877,-5.004474,7.215695],[6.340644,-3.989952,9.036593,5.596518,6.952768,-3.090219,1.905908,1.114958,-2.669993,-6.683693,-8.206599],[-0.207650,-4.939690,4.072592,1.037244,-6.158534,1.062909,4.149459,-0.695233,-8.924102,-7.860473,2.287898],[-8.570946,-3.307888,0.402994,7.356783,-9.458423,-1.924965,1.473478,0.722237,-4.883820,9.510730,-1.032641],[-2.083991,-4.633161,-9.843123,-3.792482,-7.980471,6.320995,4.049859,-1.980944,-0.853227,-8.654814,8.208452],[-7.285992,-5.780055,-7.518976,3.609184,-7.221159,3.709676,-3.437957,-9.631167,9.861719,-3.926665,1.231392],[1.388454,-4.356807,6.670426,-8.985807,-5.514494,2.158736,-5.011861,7.925388,2.915167,0.643659,-3.449080],[-4.154819,-5.400973,2.779784,-6.449581,-2.267873,-5.517042,9.787159,-3.921659,-5.206122,1.435563,3.969797]], dtype = "float64")#candidate|6685|(13, 11)|const|float64
const_6686 = relay.const([2.518313,6.240343,-9.852321,-0.691531,2.839630,1.786049,-9.246246,-4.133799,-1.727145,-9.046095,1.556820,-1.485936,0.767283,-8.324068,-6.008222,7.089031,7.821383,9.804866,-1.991199,-2.028579,4.662181,-3.476453,-6.463886,8.260209,-4.190141,0.477844,-0.201424,-7.602396,1.776526,4.974601,-2.694859,2.557249,2.196396,-9.024463,-3.701289,-9.215474,-0.846719,-1.808115,3.565614,-8.374418,3.358492,6.854073,7.639014,9.042454,5.180038,-3.057672,3.900456,3.682246,-7.735399,0.703092,-5.795346,-2.669935,-8.490913,4.786515,-7.339807,5.079401,9.190915,-7.122099,5.254637,-7.212882,-3.776965,-5.646710,-0.885458,-2.220867,9.252319,-0.294973,3.062773,8.108423,9.662746,7.337807,-0.634011,9.284081,-5.607289,-6.350122,-2.966243,-7.860399,3.821881,-2.335726,-3.997062,-3.934046,-1.109383,2.708545,6.785791,2.277697,-8.643806,9.089091,-1.186787,-0.488917,-6.467711,-4.343448,0.386455,6.024591,8.205287,7.587528,-3.996408,-6.897161,-6.864907,2.873355,-5.177870,-6.825409,8.590301,9.358107,-6.316594,-4.864011,-2.179080,8.859082,4.795418,-0.994225,6.909688,-9.230150,3.828915,-4.786351,1.041142,0.113000,5.310959,-1.570181,5.271957,-6.980509,7.432787,-5.597942,1.525597,-4.718573,-4.482229,8.447957,-2.615560,-0.140446,-9.910297,9.177622,-2.723900,0.113233,-7.201829,-7.442687,4.643617,9.452633,-3.596778,-2.986272,-2.305661,-7.538112,6.009985,-4.748658,-7.068268,8.766839,9.014070,-6.287868,-1.745797,4.674510,6.291510,-2.691114,-0.385499,2.347495,-9.845348,-2.869379,-5.211193,0.368804,2.779087,3.145596,-2.516856,-6.802143,5.289787,1.103317,1.748899,-9.681644,9.850822,2.183412,8.501564,-1.045914,5.463789,-2.345102,5.890804,8.834691,5.323266,-7.250473,-3.037758,3.186831,2.401555,5.327008,-4.901585,9.749886,-9.291291,7.250595,-1.094864,1.861398,8.375250,1.453235,-2.637145,2.099185,-4.520483,7.055125,-1.737172,-8.358836,-6.100268,-1.072987,-7.485855,-4.641563,8.425368,-3.067679,7.400930,8.326785,9.338768,5.156159,8.768906,1.184230,5.981630,-4.718185,6.957486,1.687822,-7.589493,-6.171469,-1.966748,-1.910809,8.628201,3.865119,-5.575362,1.979501,4.161448,0.388227,1.508604,-3.714653,-4.011339,-4.657772,-9.073581,2.792350,-3.014247,3.091695,-3.389614,-9.182890,-0.836235,-9.751659,-4.603874,-2.685562,-7.278160,-2.570659,-4.858613,-9.679989,-7.542266,-2.364565,7.773466,0.582411,-6.407660,-2.459836,-7.017621,-5.717246,-7.609205,-7.679850,-1.848279,-3.750731,-8.768817,-6.078104,-5.764432,3.859157,5.904678,8.839279,1.170626,-4.834725,2.243443,-2.370165,6.792676,-2.518028,2.061800,-5.515150,7.341338,1.257517,-8.243066,-9.042169,-9.573907,0.664652,8.328614,-0.023433,8.957633,-9.954493,0.136284,5.974996,1.813196,-1.538055,-0.125312,-9.433665,-2.768056,5.493815,6.843202,7.380346,-7.377128,-0.630911,2.767786,-3.050480,4.344479,4.434422,-2.412286,-4.771961,-9.942438,-3.866188,2.909872,-5.670226,-7.565030,-0.213729,9.078701,-7.324024,-1.749041,7.033544,1.322324,6.991387,9.532928,-5.313885,2.408110,1.641922,3.281512,-8.299181,4.216774,-5.008077,-5.328655,0.990306,-9.028925,4.513889,-5.444247,-6.486152,0.118440,7.784457,-9.183108,-8.461990,-1.578772,0.114432,3.561757,-4.963871,-2.276257,9.021005,-6.404050,-7.954692,-1.577835,7.793790,8.049916,-6.139698,8.394643,4.009319,4.236384,5.119113,2.705435,-0.199114,-2.414064,4.802652,3.412656,-5.343490,-0.547998,7.698132,-2.022691,6.855580,-1.724803,-0.189735,6.233122,-2.328776,3.631883,-4.753095,-6.718543,-2.405169,-8.698301,-6.311399,-4.956213,4.326605,2.877536,5.357845,6.326480,6.702788,-6.950533,-2.394413,6.494243,8.103277,-4.624172,-6.802004,-0.330135,-2.581085,-4.180428,-6.203588,5.123819,1.145188,-3.586114,-9.985792,-3.172323,-6.204263,-6.443891,-3.710227,0.838853,-8.038138,-5.261307,-0.828107,1.671507,6.733284,8.915067,-2.903498,0.530339,-0.449436,-7.172588,0.239011,-7.282554,-7.702813,-5.953626,7.033874,-0.804216,-3.615999,-1.990460,1.961863,3.797463,5.794480,-6.661472,1.713381,-2.262624,-4.164544,-4.818688,8.564637,6.487737,8.594734,-8.937345,6.320523,0.374003,1.871543,-9.265497,1.642148,5.981158,6.335950,8.622222,0.677183,-8.200671,-2.668832,-6.546245,9.763689,1.741885,9.418223,3.566370,-4.046602,-1.303126,-4.981038,-9.810834,-6.005264,9.178606,-7.027141,-2.948808,-2.720716,6.333509,-6.630579,-9.666169,9.410368,-7.034622,5.809966,5.711369,-3.032153,-9.069609,-1.397304,2.905811,-4.368552,-5.808279,2.991548,0.335319,9.212440,-8.430091,-0.490785,-3.517355,3.057446,-5.372842,-7.345944,-7.494412,-5.804756,-5.656009,-2.941593,3.735425,-9.927815,1.892383,6.212073,8.131732,4.162950,-2.876262,-9.756453,1.069908,4.371670,-3.457882,8.272123,0.702597,8.983794,-1.157403,4.230981,6.176488,-0.486676,7.539173,8.302459,-3.242957,-6.686502,-8.529294,9.308167,-2.747635,3.492277,8.797758,-6.868718,-8.054559,-6.288407,3.591587,2.153251,6.717289,6.338094,2.180773,5.727111,1.257506,-0.466283,-6.005697,3.069132,-6.473225,8.517927,1.034996,-8.380737,-7.046105,-7.530858,-4.542337,-0.380129,8.476349,-2.541397,-8.958662,8.394515,-3.381870,9.963755,3.944749,2.170809,7.613351,4.129239,-8.964658,0.792676,-4.359630,-6.565909,7.347154,-2.393111,-9.465601,2.719691,-6.020949,-5.623867,-8.882529,5.066686,-8.875650,0.064352,-5.187467,-3.356747,5.756897,6.543923,-2.535377,-6.112730,-4.989673,-2.373108,-3.135177,2.336246,-3.168213,9.244845,0.320327,5.054691,5.483059,1.540737,8.460746,6.326193,6.120959,4.057845,-6.117480,5.903969,-1.120808,-2.451573,6.460208,-9.306156,7.954266,-9.137199,-9.751257,4.110908,0.636792,6.983761,-9.974927,0.494670,0.908120,8.450240,-4.611182,-1.970649,0.014094,2.925301,-2.851750,-1.267597,7.550406,-9.805581,-2.350043,-6.326543,2.786722,5.723021,-0.766750,9.609156,6.325712,7.140154,-5.501994,-1.457961,-0.207593,-8.120366,4.693444,9.162869,-9.964814,5.295293,0.897386,-6.585990,9.964591,-0.007617,-6.970850,-1.294885,3.620215,5.565759,1.131219,0.085206,-5.217727,8.412500,-8.565904,-1.296623,-4.543621,-0.872891,9.097928,-9.076847,-3.288038,-8.218739,0.901554,-2.223348,4.364649,-9.854847,3.996407,-6.795961,4.234751,-9.327410,-5.964577,-9.073533,-3.594108,-5.467922,2.928639,-3.480460,-1.485258,-3.812014,4.059279,-1.492515,6.810871,-6.205749,-9.876947,-5.181284,-1.230305,7.801518,2.507946,2.611203,-4.746206,-4.807202,2.706263,2.979420,2.054756,6.032337,-8.489085,6.007569,-0.120702,0.343360,4.659928,-0.049537,-8.127629,-3.702378,-6.190955,3.269341,-4.809914,-5.008935,-5.997389,8.848821,-8.440973,5.145933,-0.296932,-5.686191,-5.478809,2.722972,1.077324,4.351900,0.528164,3.721320,7.836538,2.414082,-0.403303,0.301600,8.069606,9.707724,0.360373,0.137867,5.394106,-0.665916,8.450561,0.967529,-9.460858,-9.889411,4.553486,3.686984,-3.415796,-5.372522,-1.023567,6.102015,-5.490698,5.822896,2.521541,5.870046,-7.286966,-9.246778,6.387800,-9.959145,-5.473812,3.305863,7.337330,6.927395,9.484221,-1.907029,6.481727,-9.460106,-2.402005,-5.698523,-5.823924,3.096972,6.621944,-1.356384,4.293757,-6.253129,0.212556,7.754960,-5.226300,-1.913934,-2.379144,-3.873081,-1.588176,7.258827,-0.392464,5.071566,7.399835,-0.947270,-2.722051,5.607055,3.536920,-4.436352,-8.402560,9.727321,-0.352137,-7.998666,8.240803,-9.693241,6.248053,-6.253565,9.156426,-9.947048,-7.342284,-1.187025,8.407012,1.504544,0.453769,7.464724,1.179383,0.223458,-7.011933,4.535607,-2.548013,-8.433336,8.196371,7.287842,-3.476290,-0.251233,-3.698596,0.452725,-5.590058,7.909190,-8.884908,7.731128,9.636251,4.631720,6.893924,0.986672,2.771179,0.253871,6.701507,1.730777,3.872852,-6.116213,-9.293095,6.105415,-8.895098,9.060218,-1.451262,9.216999,4.137624,8.343198,7.008841,-5.212690,-6.430401,4.580722,-2.016477,4.755006,-6.838186,-8.271411,-9.135445,-4.662874,-9.234323,3.015329,-9.650309,-5.230785,-1.572606,-1.733356,2.201045,-6.729792,8.604406,8.294931,-8.284099,1.489161,-2.987296,-4.638569,6.510144,-0.464266,-5.381072,-0.352875,-9.619149,-8.304598,9.343451,-4.034186,2.736710,-4.254373,-4.874549,-6.779739,7.473134,-4.159598,5.837780,-8.338265,1.291304,-5.446347,-9.781786,-9.096193,-5.692458,5.535712,-9.996277,-8.183108,-1.396019,-1.362873,-7.355971,-6.825396,-6.447588,6.291142,3.264550,-0.594344,-2.417013,-9.562818,-7.800773,8.314532,4.505761,-3.220491,-8.921081,6.524514,1.434719,-3.550136,-3.689126,2.919380,4.803794,8.649364,-6.202886,3.388237,-5.767912,-7.506793,-5.387228,6.211046,-9.712898,7.368941,-9.707690,-7.035455,-7.075418,9.528519,3.583295,3.830762,-2.873480,7.129329,2.723288,3.062907,-4.327871,-3.873950,-3.878151,-3.935058,0.557124,7.054820,-8.608963,7.165776,-7.775061,8.200840,-7.327561,-8.200558,8.710417,1.408193,-6.664483,2.293756,-8.326972,-0.847836,0.954756,-7.384124,-1.544105,9.398853,7.932804,-9.938512,8.208821,2.259643,-6.294838,-3.081757,5.763380,-3.093113,5.665249,-7.749652,6.333662,-9.617110,9.687790,0.782600,-1.683195,-2.862766,-8.357737,-9.858925,-9.567455,9.358920,4.101546,1.442679,6.719537,3.416871,0.797166,4.357690,-8.281963,0.667350,-1.215483,7.087601,1.848912,-6.086301,-1.045226,-0.858275,-8.672307,-5.511782,7.844410,-2.015648,4.127567,7.201823,3.033317,-6.568223,-8.488493,1.259430,-5.554340,-7.253306,-5.071865,6.820297,6.646756,4.597031,1.395140,9.974113,2.525804,-7.922276,6.330318,2.049372,-3.345367,-6.124213,-1.052200,2.080880,4.700958,-6.643041,-2.992442,-4.376410,7.985709,8.011309,0.414076,-8.577836,-0.879258,-5.120237,-3.768886,-7.101441,0.891307,-4.400318,-9.525080,-9.542422,0.484394,2.078863,8.974764,7.977986,0.578311,3.424920,7.288138,-0.857865,-1.683152,-2.074260,-1.249936,1.582095,3.972533,8.806283,2.725261,7.868968,6.365290,-9.377786,7.521341,9.451352,-9.665464,0.277105,-9.986859,6.838562,-9.814376,-3.729264,-2.583208,-9.331517,9.758559,1.548517,-8.701710,0.613762,6.892195,-2.471621,2.779999,-6.625239,-4.772079,3.155289,5.672429,-7.672850,-5.234694,-1.883332,-3.492638,2.277434,7.488090,7.903580,9.722216,7.285221,-2.892961,4.004769,4.714279,-1.260529,-9.516820,7.309492,-9.042005,5.360604,-0.869563,-5.811074,2.391004,-7.530635,-2.743006,-3.075801,-9.458269,4.560479,8.508825,-0.958933,-8.099765,-1.395268,-5.181801,-9.608432,2.422713,-7.096930,2.568574,2.552421,-1.872130,1.374913,6.996878,-8.987935,6.604876,-8.563153,7.007374,-3.199706,3.153125,-5.595473,-4.187791,1.479948,-7.758476,7.840448,-9.500845,-4.004902,-2.168942,7.750529,1.514614,8.158413,4.647793,9.662059,-7.358761,-0.446001,2.240304,7.868738,7.487284,2.478297,-5.548701,-0.896352,8.467743,3.731637,-4.152157,9.582784,9.679286,5.752472,3.184020,7.802039,-4.675457,4.364282,-6.228893,3.050213,6.561016,1.663303,4.863958,-0.747399,9.760879,-7.004658,4.654778,5.515125,-2.745316,0.342478,-6.337708,8.747094,0.677991,-9.518051,5.547769,9.417070,-8.274016,1.149803,-3.462918,6.528148,3.545951,-9.574189,8.196848,9.541739,-2.291967,9.929550,5.891775,8.652724,-4.191288,-8.069177,7.477929,-6.885566,6.072031,2.667708,-5.820771,0.871608,-4.538164,-1.425983,9.346797,3.315139,-8.873928,-0.365924,1.231167,-4.804552,8.048592,2.304893,6.392061,2.569646,8.847571,-6.276478,5.458726,-9.605415,9.639278,4.960387,-6.326015,-7.663323,-0.135111,7.203038,-5.658120,1.470428,-3.544775,-1.963305,-5.610151,-2.220954,-4.034178,5.364671,-4.380200,2.561831,-7.012075,5.904041,2.975030,-3.208722,-8.750976,1.135282,7.176316,4.575635,-5.099367,2.135437,5.514353,-2.783306,6.085185,7.545579,0.535227,0.833680,2.559524,4.720166,7.586084,-2.775645,8.466727,-2.893985,-6.454651,-1.411526,-4.994057,-4.889752,-7.518599,0.162764,-3.435857,9.273947,-4.428432,-7.026788,5.989273,-9.797254,3.234364,1.290613,6.557890,0.029036,3.046283,-8.376607,-4.867873,9.700180,1.495539,-1.571410,7.347057,-4.991736,-3.962331,9.221910,-8.954039,-5.193622,3.525694,-9.157215,-5.699049,-0.649661,7.877648,8.119708,3.802792,-8.092350,4.659764,7.955225,4.133904,-1.882514,-9.399797,7.519922,-9.686454,-1.371632,5.673798,-0.258882,-3.422165,4.386330,2.868053,5.057044,0.947246,7.490892,-4.664963,6.237900,-8.189161,-0.475646,-4.673783,5.975646,3.963176,-9.986779,-0.601906,-7.788943,3.201266,0.110967,-7.507474,-9.104763,-2.453447,2.409516,-5.701126,-2.223261,-2.193872,7.365082,3.554883,1.789755,-2.225721,6.770555,-6.022965,4.489541,-6.365105,-0.041180,-5.724120,-7.942232,9.251398,0.986964,4.453948,-3.093095,-7.625912,-1.166859,9.970747,8.694190,4.389637,-1.050079,-1.532802,9.859739,-6.600058,-7.072123,-5.297789,-4.489436,-2.181971,0.485020,5.072301,2.452872,7.554303,9.113376,-5.783211,-0.505330,-9.178938,5.573070,4.683111,5.863478,4.900886,-2.837656,-4.754583,5.673567,-9.382348,-4.271184,-4.249034,-2.205132,4.692090,-3.063029,-3.365779,7.975306,-3.546073,8.173686,-6.681348,9.786682,-0.429983,9.350462,-5.700658,6.162439,-4.946048,5.637100,-0.740375,-1.395508,0.902429,7.539175,-3.767018,-6.834316,5.887449,-6.831113,-8.823677,1.116118,3.973574,-5.820372,4.857513,-3.955509,4.650599,6.562082,7.486548,-3.811592,-8.723873,-9.341705,-7.589742,9.941838,1.078034,0.714198,-8.506826,-1.155271,-1.292379,1.302641,2.054831,1.027187,6.608572,-9.980499,-4.266328,-1.795909,-4.221430,2.772536,7.053880,-4.470427,-1.195722,5.712960,5.936119,-3.784434,-3.960707,8.395181,-6.022035,-8.663202,3.324711,-0.809920,1.707935,5.832446,-1.822616,6.111137,7.094079,-6.581441,5.151356,-0.596624,2.431438,-9.477513,2.241643,1.534436,-9.027492,4.835297,-5.117654,-6.143516,-2.742665,2.307483,-0.801291,8.864143,2.318674,-5.045106,9.608454,8.395533,7.180176,-4.971718,2.684185,-3.215782,2.686236,-9.168470,-1.587226,-1.989023,-1.217924,4.593577,-6.931330,-7.993138,-9.970812,-6.276810,-0.631426,-1.469440,-6.106348,-8.067685,5.572588,0.352619,-1.918517,-7.674264,-9.043454,-1.759908,0.908706,-7.743339,-6.642641,8.513453,1.247206,-8.573068,8.843806,8.109491,7.097082,8.540872,0.743710,9.348531,-9.564004,-5.893668,-8.477777,7.467825,-7.029359,3.725676,5.895528,9.413146,8.198967,-6.980206,-3.294282,-2.299359,0.094991,-4.906777,-4.014449,-3.698847,-6.243183,-3.024786,3.783426,-2.996593,8.781899,-5.922407,-8.494240,1.177630,1.689014,-4.736991,4.256027,9.281375,-4.151845,5.851489,-1.702223,-9.390747,-7.508813,4.425439,-3.095293,5.023237,-8.609551,-8.996234,2.389068,-0.498477,0.557308,4.497328,6.744668,1.677195,-9.976842,-7.064503,3.085481,6.806055,2.405235,8.681376,-5.113935,2.912417,1.749730,8.994925,0.130232,8.953987,-0.442534,-2.649819,-2.388905,-9.133355,-0.678124,0.037619,7.075395,-6.758336,6.537341,-5.822402,-9.541548,-4.001050,-9.611281,4.565459,8.873694,-8.410865,3.168636,9.454558,5.235190,-2.485692,8.621761,1.795396,9.776115,3.070110,5.246362,-9.956387,-9.988986,7.383852,5.628243,-7.983479,-2.962840,-1.569442,3.016582,1.526918,2.333988,0.497864,9.612873,2.054020,-9.551321,4.882817,4.836553,7.715945,1.496527,-9.246263,0.738681,8.668161,5.536371,1.015246,-4.721083,7.211892,4.825450,-9.199416,1.071399,3.903108,-2.088666,-7.811532,-9.715357,0.390021,-4.205328,-5.116628,4.246806,9.859728,-4.704470,7.521780,5.248126,-3.407408,1.933563,8.849031,5.173301,-7.728016,-4.659555,9.060897,4.861803,-3.276800,-1.576180,2.183894,-8.690050,-4.579840,-5.105117,3.173724,4.215896,-4.319527,-4.372838,8.364382,-7.875727,-6.776285,-3.690590,0.258156,-8.576180,-0.374510,6.461191,-8.904444,-9.552581,-1.096002,3.005463,0.691223,6.583634,6.847438,8.425918,0.305131,4.653050,-6.422462,2.671948,2.998281,7.103723,-1.277537,1.661417,0.975179,-8.276895,-2.880712,0.652531,-9.338382,2.265113,8.333915,-1.149293,-0.852780,-2.376616,-1.778398,0.689066,3.769742,3.002399,1.871600,5.773716,-9.707624,-5.515828,7.882658,-7.175443,-8.498717,0.976976,3.091678,6.170723,8.584982,-7.214734,5.015712,3.273623,1.842859,9.567009,-4.454699,5.375205,-7.903386,0.799222,2.174141,8.135110,-8.672962,3.220543,-1.801041,7.318877,-3.887881,8.831158,1.415261,0.534669,2.803438,0.681457,1.279479,6.755093,-1.173047,8.492915,-0.291096,-2.561234,8.070957,-3.371903,-4.300535,-3.435412,-7.252280,-8.217210,-9.851794,-9.428080,-5.484139,8.324400,-8.878265,4.840250,-3.313937,-5.161481,4.359904,0.142877,0.573439,7.750968,9.677259,-5.380357,4.219210,-2.403943,-5.198569,-2.745008,-0.224805,-6.993117,-3.665728,-9.380089,-1.580460,0.903909,5.013934,2.345076,3.078213,-0.264015,-6.045212,-3.402437,4.240755,5.548217,1.588753,0.438684,-9.364683,-6.550742,1.891232,8.232002,1.846251,-2.796493,1.938642,2.450659,-1.890516,2.628775,3.658685,-1.090063,-0.690844,-1.501503,3.011368,-9.353621,-8.881550,-7.702079,5.617876,9.487930,2.867002,8.781156,7.177500,0.859586,-7.534636,-6.829800,-5.592344,-9.169514,0.440168,-8.144755,-2.666570,-4.272980,9.763384,2.829401,-3.018265,5.710447,-2.946161,-0.235641,-0.933172,0.149180,-3.764221,-0.664559,-1.187181,-7.431923,2.173264,2.540101,6.802778,-8.771342,-2.078799,1.271807,1.866586,-1.486683,9.656522,1.241798,-3.787098,-9.619423,8.243269,9.270600,7.615768,2.240480,-9.628954,1.260011,-7.161346,-1.059730,6.521267,2.951399,2.283407,-2.410350,-1.942661,-0.198412,-5.643983,5.758821,9.898947,2.663738,-5.840611,8.646227,6.529448,-2.878889,8.920698,7.710180,-4.385916,4.192078,-4.596186,-3.054826,6.601591,-3.125957,3.331492,3.223192,-4.378257,-5.120764,2.744384,-2.517490,-7.763902,-1.110954,5.130854,-2.711104,-9.519172,5.041769,2.906330,1.876788,-1.963199,-3.183503,-9.606343,-3.735941,-6.574714,9.465151,9.857192,2.283619,0.733277,4.564287,9.098728,-0.123389,8.574398,-9.650648,-7.370472,8.825252,3.823534,-2.738202,-4.597409,3.895225,9.062519,-4.636551,-0.315450,-7.525489,-3.103289,-7.084847,7.176114,8.898425,5.337569,2.243759,-1.766668,-4.823694,-5.352222,8.648701,-8.957857,-4.381497,2.346044,-1.860169,-0.008917,3.363370,-6.780149,-0.680899,0.683106,-7.143707,5.455082,-0.884655,-4.506974,-7.519147,7.914862,8.147788,-9.292535,-2.531463,3.952616,0.065740,1.281390,-3.149258,-8.394818,-6.406521,-0.779541,-3.494671,-5.856087,1.023804,-6.595929,-4.353457,0.622163,9.951079,4.874231,-7.722902,-8.362747,-4.781053,-3.030196,3.246759,8.591044,-8.571100,-5.329036,0.755926,7.969618,4.446409,-6.668760,-1.369204,-2.054151,4.460259,6.842991,-8.509685,8.779684,7.617680,5.524586,5.919236,-8.537759,-0.903506,-3.553479,-3.094738,6.460072,5.838021,0.402595,6.192599,2.480775,4.415967,-8.164893,-8.043008,-1.327745,-0.715670,-3.913993,-7.812309,7.050029,5.401346,-7.231329,-4.458113,-6.162502,-6.668479,8.618128,3.933811,-7.216221,1.851409,-0.474933,2.299254,1.071860,-0.647838,7.848640,2.278191,2.655100,-2.635040,-1.860507,6.747785,2.642233,-5.855859,-9.497790,5.008252,-3.528963,8.927014,0.070585,6.954961,-8.303228,-9.789962,-2.388860,2.954610,1.572278,5.054894,-2.405329,-6.043201,-7.956630,-3.169123,-1.392304,-8.182157,-9.307355,5.904318,-8.181972,-5.430584,-3.830041,-1.155306,-9.213140,-9.463803,7.607672,2.588395,7.011839,8.993875,-6.657728,-4.201070,-6.392453,4.351881,-5.856707,-2.291463,1.738094,-1.747902,2.748743,-0.442387,-9.354499,8.142303,3.761567,9.880827,-7.758949,-4.866705,-9.399210,9.930251,8.789031,3.465305,4.987812,-3.674974,-9.539941,-5.366832,4.275258,-0.094337,-9.233989,-8.012012,-6.373324,-3.870938,-3.379001,-3.843146,0.682735,6.533679,-4.981526,-4.352337,-8.078171,7.543757,2.941908,1.137915,-2.929387,-3.765943,3.458039,-7.303106,-5.718439,5.416986,-0.152518,2.039214,2.516239,-4.796312,1.817697,-4.219530,-2.314563,1.682644,4.633492,-8.936018,-2.367818,-3.189819,8.514835,5.546943,2.218072,2.212558,-1.458996,6.205382,7.347732,-2.393307,2.752942,3.492025,-3.615829,3.262059,5.411874,8.647363,6.322298,0.443429,4.885902,-1.760799,2.357292,-4.914511,9.496429,-8.839290,2.681122,7.742305,3.889742,-9.285199,4.337226,5.786418,-9.839428,-8.376699,7.417593,-2.800165,3.114197,9.726061,-9.286165,-6.856236,-7.581998,2.773027,0.437207,-4.336402,6.200779,-2.892397,-2.170951,4.186932,6.575250,-6.585098,7.670642,7.558377,-3.444392,-4.889591,-5.426554,-2.217478,7.399748,-8.154942,-1.355938,8.916159,-4.116297,8.211623,1.032584,5.171506,-3.860400,0.616494,-7.476229,-0.964113,-0.204198,-9.291447,-6.139578,9.498286,-4.857781,-1.048562,-5.702690,-9.258705,-4.902687,3.580569,-6.716819,-2.782067,6.443885,-5.208783,-9.381250,-3.665945,9.088530,0.026757,3.988817,4.362321,-8.075040,-9.351284,2.919291,3.783190,-1.553432,-1.882076,2.515877,-4.251190,-2.957752,6.978587,0.516430,4.708045,-1.906944,-7.026683,9.083195,4.365061,-3.466431,-0.470381,-4.786104,6.868294,4.619152,2.764820,-2.085721,3.733512,-4.195214,8.122813,-0.790077,5.219767,2.038691,-7.626408,5.463632,-4.089086,1.121380,-2.431175,3.642259,6.878441,3.162648,3.560787,-7.911437,-9.016780,6.327604,-1.121195,7.422423,-6.565189,-0.280126,4.677201,-1.129845,6.445546,5.058732,6.979672,5.206726,8.493925,6.896294,-7.518618,9.939177,6.430602,-1.956711,-4.418833,7.968040,-3.723415,3.194939,2.799043,2.683924,5.412016,-2.913236,6.303164,8.681873,-5.791369,-1.559124,-2.574036,-1.431859,-1.887364,-5.280983,-2.715026,-1.844539,0.781529,-2.540518,4.736756,0.957874,-0.385196,-6.566607,9.581647], dtype = "float64")#candidate|6686|(2145,)|const|float64
call_6684 = relay.TupleGetItem(func_4631_call(relay.reshape(const_6685.astype('float64'), [13, 11, 1]), relay.reshape(const_6686.astype('float64'), [13, 11, 15]), ), 0)
call_6687 = relay.TupleGetItem(func_4634_call(relay.reshape(const_6685.astype('float64'), [13, 11, 1]), relay.reshape(const_6686.astype('float64'), [13, 11, 15]), ), 0)
func_3179_call = mod.get_global_var('func_3179')
func_3182_call = mutated_mod.get_global_var('func_3182')
const_6694 = relay.const([-1.522884,5.439520,-9.581301,4.446322,-1.820313,1.942462,-4.547769,1.934269,-9.448346,-1.471386,0.092127,7.209401,-5.899877,-2.337041,-9.937846,-6.094629,-0.992239,-1.611078,-4.385672,2.729248,-1.006715,-4.360768], dtype = "float64")#candidate|6694|(22,)|const|float64
var_6695 = relay.var("var_6695", dtype = "float32", shape = (308,))#candidate|6695|(308,)|var|float32
call_6693 = relay.TupleGetItem(func_3179_call(relay.reshape(const_6694.astype('float64'), [22,]), relay.reshape(var_6695.astype('float32'), [11, 14, 2]), ), 4)
call_6696 = relay.TupleGetItem(func_3182_call(relay.reshape(const_6694.astype('float64'), [22,]), relay.reshape(var_6695.astype('float32'), [11, 14, 2]), ), 4)
func_3418_call = mod.get_global_var('func_3418')
func_3421_call = mutated_mod.get_global_var('func_3421')
var_6723 = relay.var("var_6723", dtype = "float64", shape = (363, 2))#candidate|6723|(363, 2)|var|float64
call_6722 = relay.TupleGetItem(func_3418_call(relay.reshape(var_6723.astype('float64'), [11, 6, 11])), 0)
call_6724 = relay.TupleGetItem(func_3421_call(relay.reshape(var_6723.astype('float64'), [11, 6, 11])), 0)
output = relay.Tuple([bop_6679,call_6684,const_6685,const_6686,call_6693,const_6694,var_6695,call_6722,var_6723,])
output2 = relay.Tuple([bop_6682,call_6687,const_6685,const_6686,call_6696,const_6694,var_6695,call_6724,var_6723,])
func_6726 = relay.Function([var_6695,var_6723,], output)
mod['func_6726'] = func_6726
mod = relay.transform.InferType()(mod)
mutated_mod['func_6726'] = func_6726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6726_call = mutated_mod.get_global_var('func_6726')
var_6728 = relay.var("var_6728", dtype = "float32", shape = (308,))#candidate|6728|(308,)|var|float32
var_6729 = relay.var("var_6729", dtype = "float64", shape = (363, 2))#candidate|6729|(363, 2)|var|float64
call_6727 = func_6726_call(var_6728,var_6729,)
output = call_6727
func_6730 = relay.Function([var_6728,var_6729,], output)
mutated_mod['func_6730'] = func_6730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6231_call = mod.get_global_var('func_6231')
func_6233_call = mutated_mod.get_global_var('func_6233')
call_6735 = relay.TupleGetItem(func_6231_call(), 0)
call_6736 = relay.TupleGetItem(func_6233_call(), 0)
output = call_6735
output2 = call_6736
func_6739 = relay.Function([], output)
mod['func_6739'] = func_6739
mod = relay.transform.InferType()(mod)
mutated_mod['func_6739'] = func_6739
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6739_call = mutated_mod.get_global_var('func_6739')
call_6740 = func_6739_call()
output = call_6740
func_6741 = relay.Function([], output)
mutated_mod['func_6741'] = func_6741
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5164_call = mod.get_global_var('func_5164')
func_5166_call = mutated_mod.get_global_var('func_5166')
call_6759 = relay.TupleGetItem(func_5164_call(), 0)
call_6760 = relay.TupleGetItem(func_5166_call(), 0)
output = relay.Tuple([call_6759,])
output2 = relay.Tuple([call_6760,])
func_6764 = relay.Function([], output)
mod['func_6764'] = func_6764
mod = relay.transform.InferType()(mod)
output = func_6764()
func_6765 = relay.Function([], output)
mutated_mod['func_6765'] = func_6765
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6604_call = mod.get_global_var('func_6604')
func_6606_call = mutated_mod.get_global_var('func_6606')
call_6776 = relay.TupleGetItem(func_6604_call(), 0)
call_6777 = relay.TupleGetItem(func_6606_call(), 0)
output = relay.Tuple([call_6776,])
output2 = relay.Tuple([call_6777,])
func_6802 = relay.Function([], output)
mod['func_6802'] = func_6802
mod = relay.transform.InferType()(mod)
mutated_mod['func_6802'] = func_6802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6802_call = mutated_mod.get_global_var('func_6802')
call_6803 = func_6802_call()
output = call_6803
func_6804 = relay.Function([], output)
mutated_mod['func_6804'] = func_6804
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6845 = relay.var("var_6845", dtype = "bool", shape = (14, 7, 16))#candidate|6845|(14, 7, 16)|var|bool
var_6846 = relay.var("var_6846", dtype = "bool", shape = (14, 7, 16))#candidate|6846|(14, 7, 16)|var|bool
bop_6847 = relay.logical_and(var_6845.astype('bool'), relay.reshape(var_6846.astype('bool'), relay.shape_of(var_6845))) # shape=(14, 7, 16)
func_5418_call = mod.get_global_var('func_5418')
func_5420_call = mutated_mod.get_global_var('func_5420')
call_6850 = relay.TupleGetItem(func_5418_call(), 0)
call_6851 = relay.TupleGetItem(func_5420_call(), 0)
uop_6865 = relay.asinh(bop_6847.astype('float32')) # shape=(14, 7, 16)
func_3418_call = mod.get_global_var('func_3418')
func_3421_call = mutated_mod.get_global_var('func_3421')
var_6879 = relay.var("var_6879", dtype = "float64", shape = (726,))#candidate|6879|(726,)|var|float64
call_6878 = relay.TupleGetItem(func_3418_call(relay.reshape(var_6879.astype('float64'), [11, 6, 11])), 0)
call_6880 = relay.TupleGetItem(func_3421_call(relay.reshape(var_6879.astype('float64'), [11, 6, 11])), 0)
output = relay.Tuple([call_6850,uop_6865,call_6878,var_6879,])
output2 = relay.Tuple([call_6851,uop_6865,call_6880,var_6879,])
func_6881 = relay.Function([var_6845,var_6846,var_6879,], output)
mod['func_6881'] = func_6881
mod = relay.transform.InferType()(mod)
mutated_mod['func_6881'] = func_6881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6881_call = mutated_mod.get_global_var('func_6881')
var_6883 = relay.var("var_6883", dtype = "bool", shape = (14, 7, 16))#candidate|6883|(14, 7, 16)|var|bool
var_6884 = relay.var("var_6884", dtype = "bool", shape = (14, 7, 16))#candidate|6884|(14, 7, 16)|var|bool
var_6885 = relay.var("var_6885", dtype = "float64", shape = (726,))#candidate|6885|(726,)|var|float64
call_6882 = func_6881_call(var_6883,var_6884,var_6885,)
output = call_6882
func_6886 = relay.Function([var_6883,var_6884,var_6885,], output)
mutated_mod['func_6886'] = func_6886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5971_call = mod.get_global_var('func_5971')
func_5972_call = mutated_mod.get_global_var('func_5972')
call_6991 = relay.TupleGetItem(func_5971_call(), 0)
call_6992 = relay.TupleGetItem(func_5972_call(), 0)
func_4593_call = mod.get_global_var('func_4593')
func_4598_call = mutated_mod.get_global_var('func_4598')
const_6994 = relay.const([[-2.260382,0.789915,-3.071628,-8.811801,5.286136,-9.182932,5.198621,-7.556483,1.026210,-8.832826,4.268261,1.043885,3.834656,-2.064281,-0.049663,-6.128074,8.051584,5.130754,2.213034,2.769587,-7.941958,9.547204,2.188249,3.886313,1.517173,-1.871180,1.761250,8.254439,-4.158111,-4.575407],[-1.555563,1.864149,-9.909029,-3.157152,2.004463,-9.863935,0.200103,9.426996,5.582684,-0.851942,6.395473,-3.703416,-0.930421,2.030670,1.506938,-2.362161,1.970606,8.746169,-7.428214,6.094013,0.674624,0.455346,2.054016,1.131582,1.309210,9.923470,-0.479061,-8.019889,-0.036558,-6.410960],[9.959575,7.740590,-4.623648,8.026223,-0.923090,-0.367986,-7.785166,9.690403,1.017832,7.666172,-3.739598,0.318113,-9.645704,7.654958,8.982757,-5.393460,-5.312187,4.268596,-8.485797,2.344132,7.087479,7.160724,9.747634,5.374151,4.690729,-4.514781,-9.329282,8.485749,8.214279,8.457481],[-2.421552,0.631694,6.676684,0.444024,2.602517,3.111362,6.191765,9.053441,6.330187,1.309694,7.393988,-6.152923,6.134684,-2.605870,-6.064831,3.115746,0.233279,-9.833826,-3.759649,-5.876976,-0.337769,-5.425552,-8.225566,7.612505,0.894334,9.269544,-0.265009,-1.908956,4.844027,-1.436489],[-7.641199,-6.069047,-7.769058,-7.348242,-8.696837,7.563279,-3.683585,-5.356056,4.126833,-6.692978,-9.717813,3.439484,2.192036,-6.327269,-1.615870,5.641979,0.994703,-9.197932,-2.311797,-7.694402,3.899302,1.441022,6.130799,0.032421,4.676559,1.587915,7.643064,-6.461282,-9.452387,0.936860],[6.613338,4.723201,-9.464352,6.261930,5.655588,1.254331,5.228630,-9.046993,3.403275,1.192683,-0.431468,-4.834001,9.627752,-5.632105,-3.696253,-6.520139,-4.175529,-8.838230,2.847595,0.332662,5.556710,0.889748,-2.226929,6.068469,0.616003,-2.730806,-3.083240,9.368988,-9.463260,8.193150],[9.841950,-1.222903,-6.818860,-7.739501,-8.742971,-6.540075,4.766375,-3.986731,8.926485,2.562427,-0.710297,-2.645629,-2.620499,-2.203696,-2.875262,0.272848,3.640954,5.639220,-7.953819,4.112307,-8.778365,-2.005870,-2.431048,1.948476,5.293776,-7.620436,-7.993763,-4.918624,6.899223,6.400297],[-4.385170,9.021480,7.018463,5.731753,6.669169,-1.719725,-3.465030,8.256271,-6.860913,0.024418,1.127404,6.592995,-0.482983,-5.240997,5.072880,3.806430,1.420794,7.664821,-7.463415,-6.455917,-3.108418,3.793051,-4.122685,6.110470,2.296340,-8.042078,-4.855692,-2.326703,6.687935,-0.888930],[7.628823,-8.585392,8.948230,2.427322,7.991106,8.181867,-2.481519,-2.790210,8.960905,6.033499,-9.008170,1.122680,-1.122193,-7.031700,-0.473738,-0.211152,-6.910477,-7.287728,-2.935717,8.040327,-1.239625,4.022190,0.469988,0.621198,6.051112,7.425931,-8.562271,4.980373,4.013417,-9.833798],[-9.830443,6.883599,2.445715,-9.271440,6.769413,6.559711,-7.337431,-3.080807,4.436977,-2.547033,3.647351,-1.523601,-6.757033,-8.115999,6.562091,-9.324460,3.263355,6.110367,5.214338,-2.231452,5.812426,-8.549341,8.467205,-8.793371,-6.529240,1.135245,-9.370293,1.644301,0.352928,-5.274718],[-2.742978,3.778091,-6.797200,0.929924,-8.013550,-5.072401,7.740288,-8.515807,-3.458487,0.333039,1.744186,-1.431146,1.571880,7.111475,5.377278,8.183514,-0.997771,6.746077,2.855689,-4.291042,-8.668502,-8.842723,-1.093589,-2.356701,8.997095,4.703297,1.180787,-8.227274,-9.752453,5.415228],[-0.270038,9.762293,8.441840,3.396463,9.673728,8.680955,0.379804,-9.698203,-1.908230,-7.459447,-6.049080,-5.423656,3.297508,-8.820417,-7.450189,0.293646,0.856185,7.001064,8.369651,9.431569,2.841157,-8.699001,-1.407162,-8.240439,-7.218079,-9.320859,-3.241938,-8.465813,-0.465488,0.441768]], dtype = "float32")#candidate|6994|(12, 30)|const|float32
var_6995 = relay.var("var_6995", dtype = "uint16", shape = (495,))#candidate|6995|(495,)|var|uint16
var_6996 = relay.var("var_6996", dtype = "float32", shape = (308,))#candidate|6996|(308,)|var|float32
call_6993 = relay.TupleGetItem(func_4593_call(relay.reshape(const_6994.astype('float32'), [9, 8, 5]), relay.reshape(var_6995.astype('uint16'), [495,]), relay.reshape(var_6996.astype('float32'), [308,]), ), 1)
call_6997 = relay.TupleGetItem(func_4598_call(relay.reshape(const_6994.astype('float32'), [9, 8, 5]), relay.reshape(var_6995.astype('uint16'), [495,]), relay.reshape(var_6996.astype('float32'), [308,]), ), 1)
func_6468_call = mod.get_global_var('func_6468')
func_6471_call = mutated_mod.get_global_var('func_6471')
call_7012 = relay.TupleGetItem(func_6468_call(relay.reshape(call_6993.astype('uint16'), [495,])), 2)
call_7013 = relay.TupleGetItem(func_6471_call(relay.reshape(call_6993.astype('uint16'), [495,])), 2)
uop_7014 = relay.rsqrt(call_6993.astype('float64')) # shape=(495,)
uop_7016 = relay.rsqrt(call_6997.astype('float64')) # shape=(495,)
func_6347_call = mod.get_global_var('func_6347')
func_6349_call = mutated_mod.get_global_var('func_6349')
call_7018 = func_6347_call()
call_7019 = func_6347_call()
output = relay.Tuple([call_6991,const_6994,var_6995,var_6996,call_7012,uop_7014,call_7018,])
output2 = relay.Tuple([call_6992,const_6994,var_6995,var_6996,call_7013,uop_7016,call_7019,])
func_7023 = relay.Function([var_6995,var_6996,], output)
mod['func_7023'] = func_7023
mod = relay.transform.InferType()(mod)
mutated_mod['func_7023'] = func_7023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7023_call = mutated_mod.get_global_var('func_7023')
var_7025 = relay.var("var_7025", dtype = "uint16", shape = (495,))#candidate|7025|(495,)|var|uint16
var_7026 = relay.var("var_7026", dtype = "float32", shape = (308,))#candidate|7026|(308,)|var|float32
call_7024 = func_7023_call(var_7025,var_7026,)
output = call_7024
func_7027 = relay.Function([var_7025,var_7026,], output)
mutated_mod['func_7027'] = func_7027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6604_call = mod.get_global_var('func_6604')
func_6606_call = mutated_mod.get_global_var('func_6606')
call_7050 = relay.TupleGetItem(func_6604_call(), 0)
call_7051 = relay.TupleGetItem(func_6606_call(), 0)
func_6204_call = mod.get_global_var('func_6204')
func_6207_call = mutated_mod.get_global_var('func_6207')
var_7053 = relay.var("var_7053", dtype = "uint32", shape = (55,))#candidate|7053|(55,)|var|uint32
const_7054 = relay.const([[-9,-10,-6,-5,5,-5,-10,3,8,-1,-4,-2,-3,1,3,10,6,2,-6,-10,-10,5,2,5,-10,4,5,4,-5,3,-4,3,1,-2,2],[-10,-5,-4,5,-10,6,-8,9,8,10,-5,-2,-4,4,2,8,-10,-6,-3,-4,7,-6,-10,6,-3,1,1,-6,8,3,-8,1,5,2,2],[10,9,-2,-2,-9,7,5,-5,2,-1,-3,-5,6,-6,9,-8,5,6,-6,-10,-5,7,4,1,5,-1,10,7,-8,-6,-10,8,2,5,-6],[5,9,-1,3,-8,-3,-9,7,-1,-8,3,-1,-3,9,-3,2,-6,9,5,7,-2,-2,-5,8,5,-3,4,-3,9,7,-5,-1,2,-8,3],[10,-8,-8,-5,-9,2,1,7,5,4,-9,10,1,1,-9,-7,-10,5,-7,6,-1,7,-6,-3,-10,4,-9,-1,-8,-10,-7,-8,-1,6,-3],[6,-3,-5,-7,2,7,-1,10,-7,-2,-7,-5,7,10,-5,-6,-9,4,-9,-2,10,-7,-4,-3,-7,-9,4,-3,-1,4,8,-7,-10,10,-1],[8,-10,4,-4,-6,-10,7,-10,-4,-5,-6,-10,-9,3,-8,2,8,3,-9,-7,-1,-1,-2,1,1,-6,-9,10,-5,-7,-7,-10,-4,-5,3],[-7,10,3,8,-9,7,6,4,-4,-8,3,-4,10,-10,-9,6,5,4,7,-1,-1,-4,6,6,6,-3,-1,3,-4,-6,-6,-9,-8,1,4],[-6,4,-5,-7,-2,-5,3,3,7,1,-10,-8,9,1,3,-4,10,8,-8,-6,-9,7,-9,2,-6,9,-1,3,3,2,9,7,-3,7,-2],[-4,-6,-7,-1,-10,3,3,6,-3,-1,-9,10,2,-2,7,-3,-7,3,-3,4,-9,3,-8,-9,-10,-6,1,-4,9,1,10,-8,3,2,6],[-9,10,9,1,-10,6,-1,-2,-9,10,9,-6,-10,8,6,9,-1,7,8,-5,2,-4,10,7,7,9,-1,2,-3,5,-6,-7,5,6,6]], dtype = "uint32")#candidate|7054|(11, 35)|const|uint32
call_7052 = relay.TupleGetItem(func_6204_call(relay.reshape(var_7053.astype('uint32'), [1, 55]), relay.reshape(const_7054.astype('uint32'), [385,]), ), 6)
call_7055 = relay.TupleGetItem(func_6207_call(relay.reshape(var_7053.astype('uint32'), [1, 55]), relay.reshape(const_7054.astype('uint32'), [385,]), ), 6)
func_5504_call = mod.get_global_var('func_5504')
func_5506_call = mutated_mod.get_global_var('func_5506')
var_7060 = relay.var("var_7060", dtype = "float32", shape = (1440,))#candidate|7060|(1440,)|var|float32
call_7059 = relay.TupleGetItem(func_5504_call(relay.reshape(var_7060.astype('float32'), [8, 12, 15])), 0)
call_7061 = relay.TupleGetItem(func_5506_call(relay.reshape(var_7060.astype('float32'), [8, 12, 15])), 0)
output = relay.Tuple([call_7050,call_7052,var_7053,const_7054,call_7059,var_7060,])
output2 = relay.Tuple([call_7051,call_7055,var_7053,const_7054,call_7061,var_7060,])
func_7066 = relay.Function([var_7053,var_7060,], output)
mod['func_7066'] = func_7066
mod = relay.transform.InferType()(mod)
var_7067 = relay.var("var_7067", dtype = "uint32", shape = (55,))#candidate|7067|(55,)|var|uint32
var_7068 = relay.var("var_7068", dtype = "float32", shape = (1440,))#candidate|7068|(1440,)|var|float32
output = func_7066(var_7067,var_7068,)
func_7069 = relay.Function([var_7067,var_7068,], output)
mutated_mod['func_7069'] = func_7069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5418_call = mod.get_global_var('func_5418')
func_5420_call = mutated_mod.get_global_var('func_5420')
call_7082 = relay.TupleGetItem(func_5418_call(), 0)
call_7083 = relay.TupleGetItem(func_5420_call(), 0)
output = call_7082
output2 = call_7083
func_7104 = relay.Function([], output)
mod['func_7104'] = func_7104
mod = relay.transform.InferType()(mod)
mutated_mod['func_7104'] = func_7104
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7104_call = mutated_mod.get_global_var('func_7104')
call_7105 = func_7104_call()
output = call_7105
func_7106 = relay.Function([], output)
mutated_mod['func_7106'] = func_7106
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5164_call = mod.get_global_var('func_5164')
func_5166_call = mutated_mod.get_global_var('func_5166')
call_7115 = relay.TupleGetItem(func_5164_call(), 0)
call_7116 = relay.TupleGetItem(func_5166_call(), 0)
func_3179_call = mod.get_global_var('func_3179')
func_3182_call = mutated_mod.get_global_var('func_3182')
const_7121 = relay.const([-9.143374,4.957802,-7.039518,-5.597378,-4.680182,-7.154790,-1.574889,-0.663190,9.779439,-0.868675,-5.754082,2.991555,-5.098366,2.765372,7.097784,0.754763,9.426238,-2.966698,0.740931,-0.702472,-9.473575,-8.795835], dtype = "float64")#candidate|7121|(22,)|const|float64
var_7122 = relay.var("var_7122", dtype = "float32", shape = (77, 4))#candidate|7122|(77, 4)|var|float32
call_7120 = relay.TupleGetItem(func_3179_call(relay.reshape(const_7121.astype('float64'), [22,]), relay.reshape(var_7122.astype('float32'), [11, 14, 2]), ), 0)
call_7123 = relay.TupleGetItem(func_3182_call(relay.reshape(const_7121.astype('float64'), [22,]), relay.reshape(var_7122.astype('float32'), [11, 14, 2]), ), 0)
uop_7142 = relay.atanh(const_7121.astype('float64')) # shape=(22,)
bop_7158 = relay.floor_mod(const_7121.astype('float64'), call_7120.astype('float64')) # shape=(11, 14, 22)
bop_7161 = relay.floor_mod(const_7121.astype('float64'), call_7123.astype('float64')) # shape=(11, 14, 22)
var_7169 = relay.var("var_7169", dtype = "float64", shape = (22,))#candidate|7169|(22,)|var|float64
bop_7170 = relay.maximum(uop_7142.astype('int32'), relay.reshape(var_7169.astype('int32'), relay.shape_of(uop_7142))) # shape=(22,)
bop_7173 = relay.logical_or(bop_7170.astype('bool'), bop_7158.astype('bool')) # shape=(11, 14, 22)
bop_7176 = relay.logical_or(bop_7170.astype('bool'), bop_7161.astype('bool')) # shape=(11, 14, 22)
output = relay.Tuple([call_7115,var_7122,bop_7173,])
output2 = relay.Tuple([call_7116,var_7122,bop_7176,])
func_7178 = relay.Function([var_7122,var_7169,], output)
mod['func_7178'] = func_7178
mod = relay.transform.InferType()(mod)
mutated_mod['func_7178'] = func_7178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7178_call = mutated_mod.get_global_var('func_7178')
var_7180 = relay.var("var_7180", dtype = "float32", shape = (77, 4))#candidate|7180|(77, 4)|var|float32
var_7181 = relay.var("var_7181", dtype = "float64", shape = (22,))#candidate|7181|(22,)|var|float64
call_7179 = func_7178_call(var_7180,var_7181,)
output = call_7179
func_7182 = relay.Function([var_7180,var_7181,], output)
mutated_mod['func_7182'] = func_7182
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7192 = relay.var("var_7192", dtype = "int64", shape = (5, 4, 4))#candidate|7192|(5, 4, 4)|var|int64
var_7193 = relay.var("var_7193", dtype = "int64", shape = (5, 4, 4))#candidate|7193|(5, 4, 4)|var|int64
bop_7194 = relay.subtract(var_7192.astype('int64'), relay.reshape(var_7193.astype('int64'), relay.shape_of(var_7192))) # shape=(5, 4, 4)
bop_7226 = relay.less(var_7193.astype('bool'), relay.reshape(bop_7194.astype('bool'), relay.shape_of(var_7193))) # shape=(5, 4, 4)
output = relay.Tuple([bop_7226,])
output2 = relay.Tuple([bop_7226,])
func_7232 = relay.Function([var_7192,var_7193,], output)
mod['func_7232'] = func_7232
mod = relay.transform.InferType()(mod)
mutated_mod['func_7232'] = func_7232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7232_call = mutated_mod.get_global_var('func_7232')
var_7234 = relay.var("var_7234", dtype = "int64", shape = (5, 4, 4))#candidate|7234|(5, 4, 4)|var|int64
var_7235 = relay.var("var_7235", dtype = "int64", shape = (5, 4, 4))#candidate|7235|(5, 4, 4)|var|int64
call_7233 = func_7232_call(var_7234,var_7235,)
output = call_7233
func_7236 = relay.Function([var_7234,var_7235,], output)
mutated_mod['func_7236'] = func_7236
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5929_call = mod.get_global_var('func_5929')
func_5931_call = mutated_mod.get_global_var('func_5931')
call_7339 = relay.TupleGetItem(func_5929_call(), 0)
call_7340 = relay.TupleGetItem(func_5931_call(), 0)
var_7341 = relay.var("var_7341", dtype = "float32", shape = (16, 12, 15))#candidate|7341|(16, 12, 15)|var|float32
bop_7342 = relay.multiply(call_7339.astype('uint64'), var_7341.astype('uint64')) # shape=(16, 12, 15)
bop_7345 = relay.multiply(call_7340.astype('uint64'), var_7341.astype('uint64')) # shape=(16, 12, 15)
output = bop_7342
output2 = bop_7345
func_7362 = relay.Function([var_7341,], output)
mod['func_7362'] = func_7362
mod = relay.transform.InferType()(mod)
mutated_mod['func_7362'] = func_7362
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7363 = relay.var("var_7363", dtype = "float32", shape = (16, 12, 15))#candidate|7363|(16, 12, 15)|var|float32
func_7362_call = mutated_mod.get_global_var('func_7362')
call_7364 = func_7362_call(var_7363)
output = call_7364
func_7365 = relay.Function([var_7363], output)
mutated_mod['func_7365'] = func_7365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5929_call = mod.get_global_var('func_5929')
func_5931_call = mutated_mod.get_global_var('func_5931')
call_7400 = relay.TupleGetItem(func_5929_call(), 0)
call_7401 = relay.TupleGetItem(func_5931_call(), 0)
uop_7405 = relay.exp(call_7400.astype('float64')) # shape=(1, 12, 15)
uop_7407 = relay.exp(call_7401.astype('float64')) # shape=(1, 12, 15)
func_29_call = mod.get_global_var('func_29')
func_32_call = mutated_mod.get_global_var('func_32')
var_7410 = relay.var("var_7410", dtype = "bool", shape = (312,))#candidate|7410|(312,)|var|bool
call_7409 = func_29_call(relay.reshape(var_7410.astype('bool'), [2, 12, 13]))
call_7411 = func_29_call(relay.reshape(var_7410.astype('bool'), [2, 12, 13]))
output = relay.Tuple([uop_7405,call_7409,var_7410,])
output2 = relay.Tuple([uop_7407,call_7411,var_7410,])
func_7423 = relay.Function([var_7410,], output)
mod['func_7423'] = func_7423
mod = relay.transform.InferType()(mod)
mutated_mod['func_7423'] = func_7423
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7424 = relay.var("var_7424", dtype = "bool", shape = (312,))#candidate|7424|(312,)|var|bool
func_7423_call = mutated_mod.get_global_var('func_7423')
call_7425 = func_7423_call(var_7424)
output = call_7425
func_7426 = relay.Function([var_7424], output)
mutated_mod['func_7426'] = func_7426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6604_call = mod.get_global_var('func_6604')
func_6606_call = mutated_mod.get_global_var('func_6606')
call_7450 = relay.TupleGetItem(func_6604_call(), 0)
call_7451 = relay.TupleGetItem(func_6606_call(), 0)
func_7104_call = mod.get_global_var('func_7104')
func_7106_call = mutated_mod.get_global_var('func_7106')
call_7464 = func_7104_call()
call_7465 = func_7104_call()
func_5164_call = mod.get_global_var('func_5164')
func_5166_call = mutated_mod.get_global_var('func_5166')
call_7466 = relay.TupleGetItem(func_5164_call(), 0)
call_7467 = relay.TupleGetItem(func_5166_call(), 0)
output = relay.Tuple([call_7450,call_7464,call_7466,])
output2 = relay.Tuple([call_7451,call_7465,call_7467,])
func_7471 = relay.Function([], output)
mod['func_7471'] = func_7471
mod = relay.transform.InferType()(mod)
mutated_mod['func_7471'] = func_7471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7471_call = mutated_mod.get_global_var('func_7471')
call_7472 = func_7471_call()
output = call_7472
func_7473 = relay.Function([], output)
mutated_mod['func_7473'] = func_7473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6231_call = mod.get_global_var('func_6231')
func_6233_call = mutated_mod.get_global_var('func_6233')
call_7490 = relay.TupleGetItem(func_6231_call(), 0)
call_7491 = relay.TupleGetItem(func_6233_call(), 0)
func_6347_call = mod.get_global_var('func_6347')
func_6349_call = mutated_mod.get_global_var('func_6349')
call_7495 = func_6347_call()
call_7496 = func_6347_call()
output = relay.Tuple([call_7490,call_7495,])
output2 = relay.Tuple([call_7491,call_7496,])
func_7501 = relay.Function([], output)
mod['func_7501'] = func_7501
mod = relay.transform.InferType()(mod)
output = func_7501()
func_7502 = relay.Function([], output)
mutated_mod['func_7502'] = func_7502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5929_call = mod.get_global_var('func_5929')
func_5931_call = mutated_mod.get_global_var('func_5931')
call_7511 = relay.TupleGetItem(func_5929_call(), 0)
call_7512 = relay.TupleGetItem(func_5931_call(), 0)
output = call_7511
output2 = call_7512
func_7526 = relay.Function([], output)
mod['func_7526'] = func_7526
mod = relay.transform.InferType()(mod)
mutated_mod['func_7526'] = func_7526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7526_call = mutated_mod.get_global_var('func_7526')
call_7527 = func_7526_call()
output = call_7527
func_7528 = relay.Function([], output)
mutated_mod['func_7528'] = func_7528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5156_call = mod.get_global_var('func_5156')
func_5157_call = mutated_mod.get_global_var('func_5157')
call_7535 = func_5156_call()
call_7536 = func_5156_call()
uop_7546 = relay.sigmoid(call_7535.astype('float64')) # shape=(1, 12, 15)
uop_7548 = relay.sigmoid(call_7536.astype('float64')) # shape=(1, 12, 15)
func_5469_call = mod.get_global_var('func_5469')
func_5471_call = mutated_mod.get_global_var('func_5471')
var_7569 = relay.var("var_7569", dtype = "float64", shape = (112,))#candidate|7569|(112,)|var|float64
call_7568 = relay.TupleGetItem(func_5469_call(relay.reshape(var_7569.astype('float64'), [112, 1])), 0)
call_7570 = relay.TupleGetItem(func_5471_call(relay.reshape(var_7569.astype('float64'), [112, 1])), 0)
output = relay.Tuple([uop_7546,call_7568,var_7569,])
output2 = relay.Tuple([uop_7548,call_7570,var_7569,])
func_7571 = relay.Function([var_7569,], output)
mod['func_7571'] = func_7571
mod = relay.transform.InferType()(mod)
var_7572 = relay.var("var_7572", dtype = "float64", shape = (112,))#candidate|7572|(112,)|var|float64
output = func_7571(var_7572)
func_7573 = relay.Function([var_7572], output)
mutated_mod['func_7573'] = func_7573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5736_call = mod.get_global_var('func_5736')
func_5737_call = mutated_mod.get_global_var('func_5737')
call_7587 = relay.TupleGetItem(func_5736_call(), 0)
call_7588 = relay.TupleGetItem(func_5737_call(), 0)
func_4593_call = mod.get_global_var('func_4593')
func_4598_call = mutated_mod.get_global_var('func_4598')
const_7594 = relay.const([-2.373842,7.167232,3.062277,-8.825884,-5.329511,-1.882627,4.722211,9.836692,7.616347,-1.477468,-9.177921,-9.138372,7.608030,-5.581130,-8.273550,-5.584453,8.672540,8.924541,4.095293,-4.452099,6.569805,-4.283839,6.839672,4.993115,7.311134,9.369403,-6.776126,0.930862,-8.779591,-7.119573,6.763063,2.866479,-4.296718,-5.676664,5.134550,9.583379,7.284998,3.089411,0.116519,6.718970,-8.940966,-5.364534,9.063454,-3.232654,-8.689278,-5.977217,-9.711656,-2.060788,-4.247997,-4.395586,8.539447,-7.136366,2.249873,1.663334,-1.180761,1.524059,1.943904,-5.551534,8.748561,-6.226394,9.862630,5.357522,3.157195,6.196441,-8.527590,6.625082,9.602049,-0.639811,8.920710,-7.875050,3.956567,8.166000,6.151352,0.395200,-2.040885,-0.268188,-2.880206,1.039074,8.468714,1.781961,-4.901495,-5.486850,-4.430256,-0.162994,-6.962413,9.002925,-9.673275,4.156157,-9.107650,-3.908659,-5.030971,6.991833,1.052568,-4.431147,5.021189,-0.478887,-6.853808,7.079452,-7.151810,0.010325,-6.054552,-7.921797,2.507047,8.522572,-2.738107,-7.822748,-5.119487,9.791141,2.754919,8.153237,3.655434,-8.513273,-7.153533,-7.187923,-3.812856,8.319969,-3.498783,4.018599,4.877482,-9.518608,0.979635,7.571083,-7.457462,6.185234,-4.316354,-7.373879,-5.287457,-0.744864,-3.529297,6.677123,-8.988932,-6.988442,-6.553336,-9.805538,-3.202891,4.383572,1.819563,9.482520,1.277640,3.342010,2.433733,7.313869,6.540360,-3.276860,-9.927821,-8.908485,4.944660,-1.414340,-7.122245,3.890637,6.846065,-5.265007,7.805261,-1.804053,-8.330245,2.437436,4.513506,-2.315667,-1.288288,-5.381663,-8.294135,9.954382,9.957467,-6.189295,-6.081807,-3.468322,-9.680473,-5.560447,7.286273,3.587626,8.212080,1.752337,5.447966,4.348549,9.945625,8.874782,-3.325444,6.318061,-2.216016,6.716481,0.262790,-7.501944,7.381086,-3.515028,9.374340,-0.436022,-5.081528,2.227278,5.092066,9.463636,-3.600326,9.251916,1.690919,3.846213,-6.119960,-7.120921,-3.493384,9.746216,8.976925,-6.688483,6.765262,6.565444,8.030596,-5.106473,2.374482,8.814655,-9.407349,-5.701243,4.195452,4.626959,5.398338,2.219329,-3.728560,0.415023,-6.728281,-2.005948,-2.800944,3.381915,-3.709879,0.861547,6.444609,8.939658,7.543183,2.065172,1.440937,-8.842046,-7.905938,0.132925,-1.384006,4.183136,-4.008170,3.162152,1.258942,-7.119949,-7.350013,-3.660604,-4.471522,2.242260,7.733363,-6.472334,0.620826,0.250617,1.250557,-7.836224,0.306946,-5.092589,4.261075,7.199437,5.960014,-4.242939,8.958583,1.473726,-3.657767,8.952619,-3.217583,3.408636,-6.497028,7.519592,7.936705,1.861459,5.552157,-4.259367,8.716040,-4.241587,-5.269168,-1.033457,2.282573,5.861773,-9.924852,5.456018,2.670113,-8.509164,-3.288475,8.132811,1.503865,-0.855254,-5.421702,0.864602,-9.082177,-4.248230,-4.452805,-8.693040,6.164753,-7.715484,-3.827998,-9.999523,-7.956532,1.265949,-9.493496,-6.270100,-2.494440,7.999104,8.854574,-7.105649,-3.332203,-4.782025,-7.473970,-9.659123,5.025608,3.285546,-5.526220,2.754010,5.686546,7.696292,0.242750,3.056804,3.518473,-3.612730,-7.794741,-9.103431,-1.779436,1.555042,-9.037385,-3.003845,-8.590639,1.699343,5.744499,0.591353,-5.501471,-7.604870,-4.521943,1.274531,-6.273691,8.311420,-3.851911,7.149122,-4.667370,5.743889,-1.962839,-2.985536,-6.740710,-4.234233,-8.825024,-3.310674,-9.163913,-7.493376,-0.348850,-1.617380,-6.927691,5.791027,-6.252061,1.167834,-2.894060,3.701502,-1.734693,6.160913,5.438656,-8.029853,-6.598751,-2.480706,3.951270,7.030681,-7.460768,5.308412,4.094170,-7.049784,1.348083,0.755120,-7.665539,2.097355], dtype = "float32")#candidate|7594|(360,)|const|float32
var_7595 = relay.var("var_7595", dtype = "uint16", shape = (495,))#candidate|7595|(495,)|var|uint16
var_7596 = relay.var("var_7596", dtype = "float32", shape = (77, 4))#candidate|7596|(77, 4)|var|float32
call_7593 = relay.TupleGetItem(func_4593_call(relay.reshape(const_7594.astype('float32'), [9, 8, 5]), relay.reshape(var_7595.astype('uint16'), [495,]), relay.reshape(var_7596.astype('float32'), [308,]), ), 2)
call_7597 = relay.TupleGetItem(func_4598_call(relay.reshape(const_7594.astype('float32'), [9, 8, 5]), relay.reshape(var_7595.astype('uint16'), [495,]), relay.reshape(var_7596.astype('float32'), [308,]), ), 2)
output = relay.Tuple([call_7587,call_7593,const_7594,var_7595,var_7596,])
output2 = relay.Tuple([call_7588,call_7597,const_7594,var_7595,var_7596,])
func_7610 = relay.Function([var_7595,var_7596,], output)
mod['func_7610'] = func_7610
mod = relay.transform.InferType()(mod)
var_7611 = relay.var("var_7611", dtype = "uint16", shape = (495,))#candidate|7611|(495,)|var|uint16
var_7612 = relay.var("var_7612", dtype = "float32", shape = (77, 4))#candidate|7612|(77, 4)|var|float32
output = func_7610(var_7611,var_7612,)
func_7613 = relay.Function([var_7611,var_7612,], output)
mutated_mod['func_7613'] = func_7613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6802_call = mod.get_global_var('func_6802')
func_6804_call = mutated_mod.get_global_var('func_6804')
call_7635 = relay.TupleGetItem(func_6802_call(), 0)
call_7636 = relay.TupleGetItem(func_6804_call(), 0)
output = relay.Tuple([call_7635,])
output2 = relay.Tuple([call_7636,])
func_7639 = relay.Function([], output)
mod['func_7639'] = func_7639
mod = relay.transform.InferType()(mod)
mutated_mod['func_7639'] = func_7639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7639_call = mutated_mod.get_global_var('func_7639')
call_7640 = func_7639_call()
output = call_7640
func_7641 = relay.Function([], output)
mutated_mod['func_7641'] = func_7641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6802_call = mod.get_global_var('func_6802')
func_6804_call = mutated_mod.get_global_var('func_6804')
call_7731 = relay.TupleGetItem(func_6802_call(), 0)
call_7732 = relay.TupleGetItem(func_6804_call(), 0)
func_7232_call = mod.get_global_var('func_7232')
func_7236_call = mutated_mod.get_global_var('func_7236')
const_7741 = relay.const([-7,-10,-6,9,8,10,-10,1,-7,-5,7,-10,-8,-6,-9,8,-1,-2,-9,7,-10,9,5,10,-10,8,8,10,1,10,2,-7,8,2,-2,-7,5,10,5,-1,-6,4,6,-3,-9,-6,1,-6,3,-8,-6,-7,2,-10,-9,2,9,-1,-2,-10,9,4,9,1,-7,-1,6,1,-5,-5,-1,2,-4,2,9,-7,-10,-8,-10,-5], dtype = "int64")#candidate|7741|(80,)|const|int64
call_7740 = relay.TupleGetItem(func_7232_call(relay.reshape(const_7741.astype('int64'), [5, 4, 4]), relay.reshape(const_7741.astype('int64'), [5, 4, 4]), ), 0)
call_7742 = relay.TupleGetItem(func_7236_call(relay.reshape(const_7741.astype('int64'), [5, 4, 4]), relay.reshape(const_7741.astype('int64'), [5, 4, 4]), ), 0)
output = relay.Tuple([call_7731,call_7740,const_7741,])
output2 = relay.Tuple([call_7732,call_7742,const_7741,])
func_7801 = relay.Function([], output)
mod['func_7801'] = func_7801
mod = relay.transform.InferType()(mod)
mutated_mod['func_7801'] = func_7801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7801_call = mutated_mod.get_global_var('func_7801')
call_7802 = func_7801_call()
output = call_7802
func_7803 = relay.Function([], output)
mutated_mod['func_7803'] = func_7803
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6802_call = mod.get_global_var('func_6802')
func_6804_call = mutated_mod.get_global_var('func_6804')
call_7835 = relay.TupleGetItem(func_6802_call(), 0)
call_7836 = relay.TupleGetItem(func_6804_call(), 0)
output = call_7835
output2 = call_7836
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
func_5418_call = mod.get_global_var('func_5418')
func_5420_call = mutated_mod.get_global_var('func_5420')
call_7862 = relay.TupleGetItem(func_5418_call(), 0)
call_7863 = relay.TupleGetItem(func_5420_call(), 0)
var_7867 = relay.var("var_7867", dtype = "float32", shape = (12, 12, 15))#candidate|7867|(12, 12, 15)|var|float32
bop_7868 = relay.logical_or(call_7862.astype('bool'), var_7867.astype('bool')) # shape=(12, 12, 15)
bop_7871 = relay.logical_or(call_7863.astype('bool'), var_7867.astype('bool')) # shape=(12, 12, 15)
output = bop_7868
output2 = bop_7871
func_7879 = relay.Function([var_7867,], output)
mod['func_7879'] = func_7879
mod = relay.transform.InferType()(mod)
var_7880 = relay.var("var_7880", dtype = "float32", shape = (12, 12, 15))#candidate|7880|(12, 12, 15)|var|float32
output = func_7879(var_7880)
func_7881 = relay.Function([var_7880], output)
mutated_mod['func_7881'] = func_7881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6739_call = mod.get_global_var('func_6739')
func_6741_call = mutated_mod.get_global_var('func_6741')
call_7883 = func_6739_call()
call_7884 = func_6739_call()
func_7471_call = mod.get_global_var('func_7471')
func_7473_call = mutated_mod.get_global_var('func_7473')
call_7894 = relay.TupleGetItem(func_7471_call(), 1)
call_7895 = relay.TupleGetItem(func_7473_call(), 1)
func_6881_call = mod.get_global_var('func_6881')
func_6886_call = mutated_mod.get_global_var('func_6886')
const_7899 = relay.const([[False,False,True,True],[False,False,False,False],[False,True,True,True],[False,True,False,True],[False,True,True,True],[False,True,False,True],[True,True,False,True],[True,False,False,True],[False,True,True,False],[False,True,True,False],[False,False,True,False],[True,False,False,False],[True,True,True,True],[True,True,False,False],[True,True,False,False],[True,False,False,True],[False,True,False,False],[False,True,False,False],[True,False,True,False],[False,True,False,True],[False,True,True,True],[True,True,False,False],[False,False,False,True],[False,False,True,False],[True,True,False,True],[False,True,False,True],[True,True,True,True],[False,False,False,False],[True,True,False,False],[True,False,False,True],[False,True,True,False],[True,False,True,True],[True,True,False,True],[False,False,False,True],[True,True,False,True],[True,True,False,True],[False,False,True,True],[False,False,True,False],[True,False,False,False],[False,True,True,True],[True,False,False,True],[False,False,True,False],[True,True,True,True],[False,True,False,True],[True,True,False,True],[True,True,True,False],[True,False,True,True],[True,False,False,False],[False,False,False,True],[False,True,True,False],[False,False,True,True],[False,True,False,True],[False,False,True,False],[False,False,False,True],[False,True,True,False],[False,True,False,False],[False,False,True,False],[True,False,False,False],[True,True,True,True],[False,True,False,True],[True,True,True,True],[False,True,True,False],[True,False,False,True],[True,True,True,True],[True,True,False,True],[True,False,True,False],[False,False,True,False],[True,False,True,False],[True,False,False,True],[False,True,False,True],[True,False,False,False],[True,True,False,True],[False,False,False,False],[False,True,False,False],[True,False,True,False],[False,False,False,True],[True,False,True,True],[True,True,False,False],[True,False,True,True],[True,True,False,False],[True,False,False,True],[True,False,False,False],[False,True,False,False],[True,False,False,False],[True,True,True,False],[False,True,True,True],[True,False,False,True],[True,False,True,False],[False,True,True,True],[True,True,True,False],[False,True,False,False],[False,False,False,True],[True,False,True,True],[True,False,True,True],[False,True,False,True],[False,True,True,False],[False,True,False,True],[False,True,True,True],[True,False,True,True],[False,True,False,False],[True,True,True,True],[False,False,False,False],[False,False,False,False],[True,True,False,True],[False,False,False,True],[False,False,False,True],[False,True,False,False],[False,False,False,False],[True,False,True,True],[False,True,False,False],[True,False,False,False],[True,True,True,False],[True,True,True,True],[True,True,False,True],[False,False,False,False],[False,False,False,False],[False,True,True,True],[False,True,True,True],[True,False,True,True],[True,False,True,False],[False,False,False,True],[True,False,True,True],[True,True,True,True],[True,False,True,False],[True,True,True,False],[False,False,True,False],[False,True,True,True],[True,False,False,True],[False,False,True,True],[False,False,False,True],[True,True,True,False],[True,False,False,True],[True,True,True,False],[False,False,False,False],[True,True,False,True],[True,False,False,True],[False,True,False,False],[True,False,False,False],[True,True,True,True],[True,True,False,True],[True,True,True,True],[True,True,True,True],[False,True,False,True],[True,False,False,True],[False,False,False,True],[False,False,False,True],[True,True,False,False],[False,False,True,True],[True,False,False,True],[True,False,False,True],[True,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,True],[True,False,False,True],[True,True,True,False],[False,True,True,True],[True,True,True,True],[True,True,False,False],[False,False,False,False],[True,False,True,True],[False,True,True,True],[True,True,True,False],[False,False,True,False],[True,False,False,True],[False,True,False,True],[False,False,True,False],[False,False,True,True],[False,False,True,True],[True,False,False,False],[True,True,True,True],[True,False,False,True],[False,False,False,False],[True,False,False,True],[False,True,False,False],[True,True,False,False],[True,True,True,False],[True,True,False,False],[True,True,True,False],[True,True,True,False],[True,True,False,False],[True,False,False,True],[False,False,False,True],[True,False,True,False],[True,False,False,False],[False,False,False,True],[False,True,True,True],[True,True,True,False],[False,False,True,False],[False,True,True,False],[True,True,False,False],[True,True,False,False],[False,False,False,False],[False,False,True,False],[False,False,False,True],[True,True,True,False],[True,False,False,False],[True,True,False,False],[True,False,False,False],[False,False,True,False],[False,True,False,True],[False,True,True,False],[True,True,True,True],[True,False,True,False],[True,True,False,False],[False,True,True,True],[True,True,False,True],[False,True,True,False],[False,True,True,False],[False,True,False,False],[False,True,True,True],[False,False,False,True],[True,False,True,True],[True,False,True,True],[False,True,False,False],[False,False,False,False],[True,False,True,False],[True,True,False,True],[True,True,True,True],[True,True,False,False],[True,True,True,True],[False,False,False,False],[True,False,False,True],[False,False,False,False],[False,True,False,True],[False,False,True,True],[True,False,False,False],[True,False,False,False],[False,True,True,False],[False,True,False,True],[False,False,True,False],[False,True,False,True],[False,False,False,False],[False,True,False,True],[True,False,True,False],[True,True,True,True],[True,False,True,True],[False,True,False,False],[True,True,False,True],[False,True,False,False],[True,True,True,False],[False,True,True,False],[True,True,False,False],[False,True,True,True],[False,False,False,False],[True,True,False,False],[False,False,False,True],[True,False,True,True],[True,False,True,False],[True,False,False,True],[True,False,True,False],[False,True,True,False],[True,False,False,True],[True,False,True,True],[False,True,False,False],[False,False,True,True],[False,False,True,False],[False,True,True,False],[False,False,False,False],[True,True,False,True],[True,False,False,False],[False,True,False,False],[True,False,False,True],[False,True,False,True],[True,False,True,False],[True,False,False,True],[False,False,True,False],[True,True,True,True],[True,True,True,True],[False,True,False,True],[False,False,False,False],[False,True,True,True],[True,False,True,False],[False,True,False,True],[True,True,True,True],[True,False,False,False],[True,True,False,True],[True,False,True,True],[False,True,True,False],[False,True,False,True],[True,True,False,False],[True,False,True,False],[True,False,True,False],[False,True,True,True],[True,True,False,False],[True,True,True,True],[True,False,False,True],[True,False,True,True],[True,True,True,False],[True,False,True,False],[False,False,True,False],[False,False,True,True],[True,True,True,False],[True,False,True,False],[False,True,True,False],[True,False,True,True],[True,False,True,False],[False,False,True,False],[True,False,False,True],[False,True,False,True],[False,True,True,True],[True,False,True,True],[False,True,True,True],[True,False,False,True],[False,False,True,False],[False,False,False,True],[False,False,False,False],[True,False,True,False],[True,False,True,False],[True,True,False,True],[False,True,False,True],[False,True,False,False],[True,False,True,True],[False,True,True,True],[False,True,True,True],[False,True,True,True],[True,True,False,False],[False,False,True,False],[True,False,True,True],[True,False,False,False],[False,True,True,False],[False,False,True,False],[False,True,False,False],[False,True,True,True],[False,True,False,False],[True,True,False,True],[True,False,False,False],[False,False,False,False],[True,False,False,False],[False,False,False,False],[True,False,False,True],[False,False,False,False],[True,False,True,True],[False,True,False,True],[True,False,False,True],[True,False,True,False],[False,False,False,True],[False,True,True,True],[True,False,False,True],[False,False,False,True],[True,True,False,True],[False,False,False,False],[True,False,True,False],[True,True,False,True],[True,True,False,True],[False,False,False,True],[False,False,True,False],[False,True,True,True],[False,False,False,False],[False,True,False,True],[True,False,True,False],[True,False,False,False],[True,False,True,True],[False,True,False,False],[True,True,False,True],[False,False,True,False],[False,True,True,False],[False,True,False,False],[True,True,False,False],[True,False,False,False],[True,True,True,True],[False,False,False,True],[True,False,True,False],[False,False,False,False],[True,True,True,False],[True,True,False,False],[False,False,True,False],[True,True,False,False],[True,False,True,True],[False,True,True,True],[False,False,True,False],[False,False,True,True],[True,False,True,False],[True,True,True,True],[False,False,True,True],[True,False,True,False],[False,False,False,False],[False,True,True,False],[True,True,False,True],[True,True,False,False],[True,False,True,False],[True,False,False,True],[False,True,False,True],[True,True,False,True],[False,False,True,False],[True,True,False,False],[False,False,True,True],[False,True,True,True],[True,False,False,True],[False,False,False,False],[True,True,False,True],[False,False,False,False]], dtype = "bool")#candidate|7899|(392, 4)|const|bool
const_7900 = relay.const([-0.435223,-0.680968,3.474494,-0.026208,-5.420386,-3.928729,6.707041,3.338411,-0.948118,-4.217603,-8.236154,9.555737,-3.867986,9.559124,3.273699,7.956811,6.568361,6.177770,7.402013,-8.135829,2.241955,-7.153106,-8.662848,-7.536935,6.390914,-0.792316,-6.445808,9.395682,-7.605828,-1.078138,-9.772070,9.891376,8.412933,-0.406846,-9.198508,-6.150311,5.471896,-1.355927,-5.075713,-4.532266,6.928441,-9.272240,3.199337,-9.376923,-9.880728,2.508830,-0.150328,-5.845714,-7.371148,4.411162,0.496309,-9.719505,-6.585318,-3.733496,2.924566,-3.174837,5.934953,-4.906965,6.551250,-3.003822,-2.731770,-6.817857,-7.113431,-2.358567,0.916951,0.308854,-0.953119,-1.427053,-0.779707,4.724504,6.887233,8.063473,-3.214025,1.418628,-2.546248,9.174329,-1.409006,-6.537751,1.267540,4.291383,-9.759256,0.760126,-9.741266,4.391428,3.138599,-1.525357,7.155564,1.069913,0.647247,6.255922,5.974270,-1.087270,-5.579878,-5.421475,-5.013120,-4.606877,8.271369,8.524581,9.992802,-3.117568,9.713200,-6.422947,-7.572988,3.641773,-0.911089,-9.451061,1.858210,2.975108,8.171075,5.446250,6.236697,-5.310431,-0.428495,-5.529451,-7.845214,-2.946919,4.819936,-9.398099,-5.444934,-2.821764,-0.369776,-0.683266,5.773028,3.768673,-4.372619,-3.120438,7.625917,-0.729322,-9.264766,7.668916,1.588083,2.331127,-7.576569,4.298077,2.231897,-4.652388,-5.176898,4.955532,-2.616658,-5.106299,-8.355873,1.651170,6.758760,1.738808,-4.285634,-3.010108,-6.785943,9.681977,-5.339620,6.237802,-1.344284,6.254887,2.433987,-1.195437,-7.992503,-2.952297,-5.374298,-6.050434,5.144719,2.614917,-3.472874,8.994419,8.614731,-9.154042,9.347525,0.387293,5.801687,-3.145676,-1.837832,-1.200447,2.259115,8.493780,-7.625328,9.931359,5.265237,-5.540667,1.577076,-1.802820,-0.809802,-9.913387,-8.863299,8.896488,-0.405944,-8.901822,-6.942100,4.528004,1.884918,8.361964,-6.522045,7.831440,-7.521212,-4.224117,-8.256870,-1.300208,7.869772,-1.771184,2.884564,6.948975,-5.907962,-6.402545,-3.430081,-7.052090,-6.920355,-6.414082,1.217599,-5.736302,4.066647,8.946732,3.580021,-5.222771,-2.825533,-5.104877,-5.075167,8.296086,-1.146654,9.610887,-8.740026,-7.619098,-3.580712,5.663367,7.675253,0.555148,-2.002771,-4.969768,-3.173902,-3.210281,3.805947,-0.117177,-4.000653,-6.041098,7.901244,-5.086642,-7.325872,-0.295489,0.056347,-5.065141,9.638392,4.234590,-1.162636,6.977595,-0.866696,2.241067,7.757216,0.282127,5.504311,-8.304530,2.977676,-5.581533,2.789671,-1.167340,3.132128,4.453655,-4.972537,-8.371115,-8.910927,-1.212688,-9.412662,9.147734,9.274760,4.137501,-3.333718,-3.058186,-1.638418,2.520647,3.146148,-2.039728,-8.670006,-5.316998,-9.682166,7.552371,-3.590236,7.381539,5.013553,-9.455424,6.160414,-8.974438,7.722926,-2.427745,2.342964,-5.485153,8.163068,7.365909,-4.211124,6.603312,2.752117,-6.867677,-1.324913,-3.315794,-8.709372,-5.076289,-4.474007,1.186269,4.342247,-9.743198,-7.875996,-7.041119,4.121791,6.949428,1.424294,6.552625,-8.159358,-0.827012,8.816434,-9.492655,-5.577199,-1.145489,4.650032,-9.281743,2.073410,-2.892117,4.993377,4.839547,-0.082690,1.695934,1.693284,-6.352512,-0.775844,-1.936101,3.304070,4.096456,-9.249740,6.946002,2.488289,-1.218484,-0.551438,-6.680025,8.772407,-7.248068,6.771119,7.998117,-8.266619,-1.955346,0.744606,5.563209,5.212761,-1.479505,-0.613864,-3.785582,8.476784,-4.337892,8.284739,-7.509857,-8.027279,-9.398989,-0.225685,4.129153,-8.178401,7.197064,-1.009798,-6.467903,9.498448,1.335566,-3.401644,5.146797,5.933400,3.241209,1.831373,2.704074,6.464500,3.255444,-7.451979,-2.559346,-4.233018,-1.827997,-4.096641,-7.621366,3.998826,4.833396,9.888042,9.356606,-0.669952,2.365797,-5.278211,-5.113975,3.789174,3.446566,-6.937935,-4.599990,1.822616,5.968871,2.538323,6.927145,-2.093471,0.692366,-8.231702,-4.228161,0.574362,-5.278098,-5.947592,4.173025,-0.191682,3.618907,8.470494,3.212118,-7.025822,-5.617453,-8.816320,-5.980978,9.532540,2.903424,4.895378,-4.907001,5.382173,-2.049429,6.271915,4.865237,8.533746,-8.930679,-2.967542,3.836020,1.217378,9.142497,-7.353493,-8.434599,0.193061,3.352989,7.848244,2.003027,-3.879924,-5.959429,-0.003691,5.784009,1.508191,-1.617161,2.655543,-9.548569,5.285991,-5.475116,-6.707124,2.342297,-0.681107,-1.906755,7.560830,7.705464,4.810246,6.929129,3.973172,1.263202,4.162495,4.019917,-3.489689,5.119524,7.325070,4.414508,-3.023751,9.100410,1.048823,-7.828838,5.661582,-8.271094,0.951986,-1.203432,-1.638853,2.779818,0.413034,-1.912113,0.253425,-1.570312,4.355758,-1.753021,-0.722906,2.751966,5.383609,-5.205645,7.903011,3.455660,4.713771,0.293261,-5.231212,0.210498,1.767118,9.901951,2.837093,2.126621,2.645434,-1.394022,1.416471,0.486056,2.510051,-0.844305,-7.242342,0.462578,3.960888,0.047429,-6.603181,-7.800433,-8.816944,-0.722781,6.788299,-7.041836,9.773951,-2.654374,-7.412994,4.255746,-4.348178,-6.703746,7.111454,-5.965298,1.963173,-3.145598,-8.691884,7.723461,-6.717652,-4.196453,-8.252336,-6.593994,8.978354,-3.177003,-0.434805,5.408109,0.026064,1.807840,4.524502,-3.518379,3.075626,-7.294210,4.835799,-2.818192,3.267880,5.336844,-7.014668,1.302377,-9.703413,7.591939,5.642451,5.515950,7.479282,-2.323136,-7.566728,0.634828,6.474732,3.119812,9.959948,2.023349,-4.091125,-1.669183,-2.095886,-1.675419,-9.923331,-6.686075,-9.416008,-4.143082,-1.046410,9.600819,9.396174,5.271021,-3.487343,2.716404,-9.854150,9.345826,0.810715,1.627621,9.453210,3.447260,-2.991537,-4.628413,2.110476,-9.931173,0.914911,9.357146,-9.311713,5.048101,4.343870,-0.439406,2.695458,5.773341,-1.503133,8.711012,-5.623065,4.113166,-0.907917,-6.183915,-8.610343,9.093847,-5.599166,9.861717,9.031665,7.792489,0.800325,1.053580,4.242357,-1.856957,8.870067,-5.039371,-0.570204,-9.342301,2.809223,-6.643630,6.465938,1.328216,-8.924238,-1.115956,4.603346,7.178242,-7.432324,-9.433710,0.378986,9.291505,-0.259825,-8.515421,2.509482,6.237109,4.318006,-3.373987,5.673778,-8.501595,-1.044212,-2.069894,8.750663,3.083920,-0.123226,5.376706,-1.149137,-4.034348,-1.265899,1.221333,-0.117961,-6.258638,-8.296818,-0.941631,-2.114119,-7.483019,-9.854520,8.921737,-6.716181,7.138563,-7.621753,-3.130319,7.532264,0.702562,1.932893,8.874554,0.586147,-5.161951,-7.562726,8.364528,7.334674,-2.604121,-9.391567,0.170136,-6.130297,1.269972,-0.330662,7.853275,9.316495,7.223086,8.399625,-4.954438,5.227936,-3.646292,5.791152,-3.381407,0.059822,-4.911204,-5.740566,-2.089247,-1.199211,4.391708,2.631062,-3.908214,3.155010,-3.883350,-8.463223,4.789389,5.326345,-6.953153,-4.222815,5.074929,5.929215,1.175510,-8.186039,-5.386470,-5.186710,8.336180,-1.892245,-7.022704,1.801627,-4.993423,5.723866,6.503123,9.789630,2.287385,1.386776,-7.676666,4.266531,-0.866398,4.802963,-5.464354,8.225457,-2.335238,-7.834876,3.249330,6.208496,8.312361,-7.642536,3.917336,-7.551896,6.026288,8.270025,-8.158816,4.287287,-1.306961,2.769489,-7.584135,-5.727469,-2.276257,1.805219,4.863164,7.611708,6.357246,2.305293,-1.800343,-9.976869,3.725742,9.575233,-5.465616,1.308432,5.908981,1.817931,5.353176,-4.664353,-1.708053,2.927634,-1.827164,8.926817,-6.850678], dtype = "float64")#candidate|7900|(726,)|const|float64
call_7898 = relay.TupleGetItem(func_6881_call(relay.reshape(const_7899.astype('bool'), [14, 7, 16]), relay.reshape(const_7899.astype('bool'), [14, 7, 16]), relay.reshape(const_7900.astype('float64'), [726,]), ), 2)
call_7901 = relay.TupleGetItem(func_6886_call(relay.reshape(const_7899.astype('bool'), [14, 7, 16]), relay.reshape(const_7899.astype('bool'), [14, 7, 16]), relay.reshape(const_7900.astype('float64'), [726,]), ), 2)
output = relay.Tuple([call_7883,call_7894,call_7898,const_7899,const_7900,])
output2 = relay.Tuple([call_7884,call_7895,call_7901,const_7899,const_7900,])
func_7912 = relay.Function([], output)
mod['func_7912'] = func_7912
mod = relay.transform.InferType()(mod)
output = func_7912()
func_7913 = relay.Function([], output)
mutated_mod['func_7913'] = func_7913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5736_call = mod.get_global_var('func_5736')
func_5737_call = mutated_mod.get_global_var('func_5737')
call_7996 = relay.TupleGetItem(func_5736_call(), 0)
call_7997 = relay.TupleGetItem(func_5737_call(), 0)
func_7571_call = mod.get_global_var('func_7571')
func_7573_call = mutated_mod.get_global_var('func_7573')
var_8001 = relay.var("var_8001", dtype = "float64", shape = (112,))#candidate|8001|(112,)|var|float64
call_8000 = relay.TupleGetItem(func_7571_call(relay.reshape(var_8001.astype('float64'), [112,])), 0)
call_8002 = relay.TupleGetItem(func_7573_call(relay.reshape(var_8001.astype('float64'), [112,])), 0)
uop_8015 = relay.sqrt(call_8000.astype('float64')) # shape=(1, 12, 15)
uop_8017 = relay.sqrt(call_8002.astype('float64')) # shape=(1, 12, 15)
output = relay.Tuple([call_7996,var_8001,uop_8015,])
output2 = relay.Tuple([call_7997,var_8001,uop_8017,])
func_8022 = relay.Function([var_8001,], output)
mod['func_8022'] = func_8022
mod = relay.transform.InferType()(mod)
mutated_mod['func_8022'] = func_8022
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8023 = relay.var("var_8023", dtype = "float64", shape = (112,))#candidate|8023|(112,)|var|float64
func_8022_call = mutated_mod.get_global_var('func_8022')
call_8024 = func_8022_call(var_8023)
output = call_8024
func_8025 = relay.Function([var_8023], output)
mutated_mod['func_8025'] = func_8025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7912_call = mod.get_global_var('func_7912')
func_7913_call = mutated_mod.get_global_var('func_7913')
call_8045 = relay.TupleGetItem(func_7912_call(), 1)
call_8046 = relay.TupleGetItem(func_7913_call(), 1)
output = relay.Tuple([call_8045,])
output2 = relay.Tuple([call_8046,])
func_8051 = relay.Function([], output)
mod['func_8051'] = func_8051
mod = relay.transform.InferType()(mod)
output = func_8051()
func_8052 = relay.Function([], output)
mutated_mod['func_8052'] = func_8052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5929_call = mod.get_global_var('func_5929')
func_5931_call = mutated_mod.get_global_var('func_5931')
call_8086 = relay.TupleGetItem(func_5929_call(), 0)
call_8087 = relay.TupleGetItem(func_5931_call(), 0)
func_5699_call = mod.get_global_var('func_5699')
func_5702_call = mutated_mod.get_global_var('func_5702')
const_8099 = relay.const([3,1,-8,-3,-9,10,7,-5,3,-6,-1,-9,2,-7,8,4,-10,7,-2,-5,-3,2,-2,-5,-6,7,8,6,-1,10,3,-1,1,-4,-2,5], dtype = "int64")#candidate|8099|(36,)|const|int64
call_8098 = relay.TupleGetItem(func_5699_call(relay.reshape(const_8099.astype('int64'), [9, 4])), 4)
call_8100 = relay.TupleGetItem(func_5702_call(relay.reshape(const_8099.astype('int64'), [9, 4])), 4)
func_4003_call = mod.get_global_var('func_4003')
func_4006_call = mutated_mod.get_global_var('func_4006')
const_8115 = relay.const(-4, dtype = "int64")#candidate|8115|()|const|int64
var_8116 = relay.var("var_8116", dtype = "int64", shape = (1200, 1))#candidate|8116|(1200, 1)|var|int64
call_8114 = relay.TupleGetItem(func_4003_call(relay.reshape(const_8115.astype('int64'), []), relay.reshape(var_8116.astype('int64'), [16, 5, 15]), ), 0)
call_8117 = relay.TupleGetItem(func_4006_call(relay.reshape(const_8115.astype('int64'), []), relay.reshape(var_8116.astype('int64'), [16, 5, 15]), ), 0)
output = relay.Tuple([call_8086,call_8098,const_8099,call_8114,const_8115,var_8116,])
output2 = relay.Tuple([call_8087,call_8100,const_8099,call_8117,const_8115,var_8116,])
func_8135 = relay.Function([var_8116,], output)
mod['func_8135'] = func_8135
mod = relay.transform.InferType()(mod)
var_8136 = relay.var("var_8136", dtype = "int64", shape = (1200, 1))#candidate|8136|(1200, 1)|var|int64
output = func_8135(var_8136)
func_8137 = relay.Function([var_8136], output)
mutated_mod['func_8137'] = func_8137
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8139 = relay.const([[[6.403406,-3.452360,-2.053660,5.951344,4.853530,0.413211,-8.179719,-4.088771,4.138010],[-1.510993,3.685220,-4.198043,5.369686,0.146484,0.548946,0.628765,8.843312,5.977530],[-0.548397,-5.178668,-8.981383,0.936327,8.674155,-3.412054,7.413277,-3.131941,1.106029],[-1.348750,-9.824998,-3.278981,9.432699,-4.782490,9.158931,-7.470367,-5.108371,1.975564],[-7.056552,7.911555,-1.634433,-0.523723,9.157134,-3.904739,6.164082,6.440608,7.355848],[2.282700,-2.465146,1.196388,0.069628,4.130456,-9.282236,8.915890,8.499659,-4.528590],[-9.330114,1.548399,-7.851571,-6.546864,9.504361,3.626338,6.386278,2.175948,-8.397725],[-5.993644,-9.374325,-1.576117,-0.408751,-0.185627,-3.377763,-6.737083,7.824212,-5.211015]],[[1.363364,-6.251551,5.562062,7.237485,-3.838527,-4.426866,-6.156638,5.051986,-0.022754],[5.876374,8.023483,6.769425,8.854330,-1.835251,5.177886,-4.803505,9.810796,8.277841],[-7.758821,-3.556324,2.408472,1.898232,1.856019,1.003898,-3.284299,-7.559477,-8.793014],[-7.108391,7.850260,-5.007811,3.183294,-9.631265,7.319011,1.715695,-6.260235,8.383137],[-7.178291,4.843022,7.239634,-0.637104,-1.789863,1.915531,-9.847923,-7.954242,-1.789125],[-7.693590,3.373361,-8.093687,1.887909,-7.064497,2.446548,3.349841,-5.257901,6.345656],[3.736866,-6.997074,8.594045,-9.670215,1.128104,9.507096,-4.460029,9.142534,-6.682136],[-2.740887,-0.054020,-3.958812,-9.450360,4.950153,-7.474247,-4.480111,-7.487244,1.858801]],[[-0.210846,0.729348,-7.606056,3.977839,6.952565,-6.468177,6.507589,2.153853,7.526332],[7.473058,0.166296,2.817535,-3.162592,-0.305705,-7.277698,-9.696432,5.969029,-1.316630],[-1.676280,-4.576574,-5.690397,-7.889673,-7.642945,8.860084,1.735089,6.295375,-1.152110],[-8.505822,6.229583,9.123973,5.533769,-7.337543,-6.785403,-8.250764,8.727447,-4.818390],[-2.609191,3.031551,-7.727531,-7.985629,6.098038,-8.944953,-8.150702,-3.259691,9.649061],[7.225139,1.351294,-9.161202,-3.500839,1.135445,1.205491,-2.694958,-3.921947,-6.540718],[-6.445456,-9.187147,9.087124,0.746521,2.031507,0.798977,-8.953611,2.259851,-3.230550],[9.910440,5.885888,-8.660567,-2.201289,-6.949450,-1.458467,5.945202,6.038687,2.764717]],[[-5.340069,2.505399,-3.375786,2.893339,0.809682,5.384943,-5.316748,7.154845,9.813361],[-6.246754,-5.136558,-0.464203,-2.467105,9.396663,1.972233,-4.411281,-0.922555,4.841777],[-8.650115,8.196771,-9.680410,5.935559,1.985449,-5.722998,9.700433,-5.900700,8.610035],[-9.678768,-0.619241,8.417362,-0.318091,0.697427,6.607386,-6.324684,0.659287,-9.009805],[-2.110462,-4.647092,-7.162727,-2.109512,-6.013168,5.247020,0.863369,4.858351,8.997925],[9.875973,-6.335445,-8.441029,2.201307,4.351865,-3.605937,-9.867002,4.299573,-6.719429],[3.735607,4.276405,4.893131,8.955646,6.335532,-4.820081,-6.293880,-7.926315,4.243170],[-6.527404,7.735473,5.686949,6.359417,-9.380224,6.073985,-1.754611,6.775569,-9.621977]],[[-1.695249,8.376733,-0.057455,5.978509,0.255438,5.098700,-6.166453,-4.456705,4.842358],[-4.392973,9.456581,0.259638,9.644160,-3.977507,-4.823629,-9.141440,-9.729003,-3.176014],[6.317581,8.318451,4.264045,5.546475,0.254414,-9.320796,-5.500709,2.169831,4.851175],[-6.143909,5.661240,-1.477854,0.434381,-3.636589,-5.515886,-4.506683,-2.044640,6.611545],[-7.484463,-7.479668,-2.170939,-4.552280,1.565171,-5.069389,-6.397346,6.668743,3.746483],[9.587173,-3.370114,6.959621,-8.567154,1.354313,2.699138,4.488988,9.781690,4.251336],[-5.578928,-9.052222,-8.817894,-0.521909,4.168172,-1.688557,1.115412,6.160653,2.713375],[2.731517,-9.294981,8.683266,7.244714,0.739106,-3.216825,-7.408863,-9.560286,-4.828434]],[[4.165502,-6.829896,-7.098474,-3.397228,-5.573185,-3.878253,-7.340336,-2.647829,-3.150351],[-9.059723,-6.995933,-3.071247,7.301760,9.917299,-6.973605,-6.855137,-8.586686,-5.641069],[0.705204,6.530082,0.059853,8.763802,5.543960,-4.241464,2.528372,9.336100,8.539953],[-6.320828,-4.377919,-7.195813,3.943091,-5.002990,3.518719,8.717423,6.696115,1.868591],[-0.824009,-6.465571,-9.133494,6.450256,-0.455881,3.937376,-8.305497,-2.451379,7.175509],[0.150565,3.353103,-2.641722,6.853248,1.302609,-0.561427,7.855288,2.963417,-5.424379],[-8.409320,-4.089826,-0.621534,-7.982127,2.405389,5.929904,-5.092871,-9.573467,4.182383],[-6.516750,-8.464442,0.408635,-8.853015,2.132288,9.909020,2.750709,8.762197,-2.593416]],[[3.159606,-2.441123,9.517679,9.155190,5.223272,0.892785,9.308141,8.434514,2.129279],[-0.200785,2.079080,5.458435,-6.330039,-5.131056,-2.280142,4.257455,-7.901004,9.923092],[-7.537491,3.238622,-6.309912,-9.066458,-0.451559,9.502272,-4.341542,-3.382623,8.112428],[-9.729286,-3.563357,8.509738,9.218511,4.811708,-4.161097,8.588877,5.086141,-6.857323],[6.385065,2.415642,-3.385178,2.079099,1.877695,-5.399062,-5.956251,-0.751506,-0.712237],[5.846781,-1.263614,6.107310,5.501234,7.971018,6.524746,-6.162328,-1.996289,-4.156503],[-4.405392,-4.476995,3.289788,-6.636437,2.927287,1.069876,-6.924086,-9.827307,3.964504],[-8.678082,-4.201349,1.500401,8.693591,6.833802,-6.842568,4.937025,5.527962,-0.297311]],[[-3.477983,-3.092765,5.437966,9.977368,1.116073,-9.782754,0.586764,9.621645,8.847822],[6.769245,0.961977,-4.083192,8.867420,-4.500070,3.966529,0.309963,-5.848801,-5.803166],[7.955970,3.447536,4.488725,9.131246,-1.447559,-2.736720,-1.915452,3.963055,-3.932510],[5.183167,9.975369,9.254891,-0.207552,-0.246266,-5.832079,-6.122300,3.257352,-9.532454],[7.256015,6.276613,6.584907,0.781537,-4.330037,4.153320,2.175152,-6.544582,-6.479144],[1.730050,-3.479869,8.473249,-4.939979,6.718226,-8.095794,-5.996474,2.036756,4.448052],[-4.902084,-5.706653,6.597480,5.929384,-0.987930,5.826200,6.865485,9.711699,5.439269],[0.908019,-2.687969,0.236203,-9.689478,2.476148,5.124488,-9.792476,3.543920,-5.464663]],[[-1.782639,0.116354,2.033575,-8.624286,-3.576824,1.586261,-3.486605,4.980411,1.288835],[8.504761,0.332751,5.655946,-6.525529,-9.872546,6.881255,-4.434584,-9.941808,-5.758538],[6.248303,8.477275,5.943016,0.043151,8.917696,-8.915618,7.063227,-7.984481,-7.413727],[9.610771,-9.475890,7.756003,2.882409,5.930484,9.611747,0.267189,-2.511637,-4.955320],[6.618291,-3.311503,2.312047,1.335639,-4.714688,5.850122,-8.528972,0.403882,-6.557430],[-6.279994,8.832513,2.871465,3.614943,6.026568,2.872261,9.427533,3.854058,1.354835],[3.715048,1.735167,7.764744,-9.487421,9.575429,-6.735514,-3.946123,0.956024,-6.803203],[2.419969,-8.739932,-1.687449,-7.827891,-2.223484,2.460539,-5.791677,4.040172,-6.214761]],[[-1.922592,-7.065412,8.645304,1.584329,1.841707,8.140490,-8.540033,4.374114,6.793970],[-0.406550,-2.085126,4.900370,3.038513,-6.257257,6.449025,5.572892,4.054424,9.715022],[-2.375058,6.321429,-7.001812,8.730416,7.585549,3.426223,-4.505562,-3.269563,-7.695496],[-9.668482,-9.533504,-7.273507,-8.620465,9.171143,7.587220,-7.193283,-6.978467,5.942120],[-9.481229,7.775081,-9.623124,-8.863132,-3.381327,2.326764,-0.868498,-2.113314,-9.219777],[-8.636588,-5.630322,-2.320078,-8.080047,6.677969,-4.015675,4.669229,-1.840971,-0.721925],[4.211612,5.069227,-7.486940,8.532045,3.267209,6.616821,-6.630053,-8.777907,2.775974],[1.344672,7.973652,-3.448359,4.148505,-8.733905,-4.806474,-6.741170,7.388525,-3.179646]],[[-3.024679,-6.234345,8.351234,2.946496,8.146824,0.700370,9.276994,-3.094319,9.519115],[-1.066241,0.976845,-6.680563,-1.427903,1.843967,6.395194,9.038735,6.564421,7.594936],[8.158110,2.947874,-8.541617,2.154909,4.617584,-0.597687,2.916109,6.323718,7.023536],[-4.093402,2.011563,2.555648,6.539280,-3.919735,-2.472075,-0.633008,4.410179,-5.648467],[-0.473256,0.435756,1.323643,-7.039306,-8.778825,0.280468,-9.355628,0.566811,-6.533406],[-3.553288,4.992153,-7.111090,-0.884825,7.513255,-3.585948,3.295479,-2.135000,-1.674602],[-9.554085,-9.105171,1.361327,-0.979769,5.791107,8.691825,-6.322576,-9.455349,-1.856641],[8.463687,3.309393,-2.361703,-1.806391,-9.539169,-4.417832,-5.299574,1.878474,-0.646039]],[[6.112035,-5.143781,-1.171998,-7.185591,2.313759,8.333371,5.968568,-6.422567,0.682608],[6.594275,-6.662386,-9.363031,-3.349052,4.301480,5.459670,-8.318933,-4.360660,-4.750361],[-1.159944,4.286360,8.676083,-3.730996,9.785614,8.133243,2.229326,-0.342702,-2.927032],[3.584796,-2.862273,-1.349020,-5.631751,-6.671989,-4.067280,3.149047,0.024799,-0.116635],[3.947763,8.921910,-5.867428,-5.878496,3.523433,9.747351,8.830572,7.425338,-2.861093],[-2.482868,-6.667623,9.540421,6.758915,-0.785883,-3.409295,0.804658,3.084968,-3.768475],[1.819214,9.218871,-5.694532,-1.397260,4.482661,4.506097,5.658868,-2.820720,-5.054597],[-5.212801,6.248366,-9.305818,-4.429866,0.289194,-4.811942,9.184095,-3.409778,4.710289]],[[8.578112,2.885703,9.670090,-9.068931,-7.173832,-5.391651,3.529561,-9.294164,2.043176],[-8.192556,-6.631894,1.597461,0.576308,-9.350563,-7.327600,-8.793128,5.260416,-6.387012],[-7.235639,3.707082,-1.059641,8.417184,9.376238,-9.248545,-2.046683,-8.753614,-8.852147],[-3.575776,-3.044529,-8.748397,-7.688486,-6.703735,-8.592365,-0.675927,-7.066534,6.969446],[7.588910,-0.290844,-9.332327,-6.460548,9.776633,2.569982,-0.529644,9.006496,-0.757064],[1.428743,8.020838,-1.239764,4.807898,-7.598573,-6.241069,-9.079920,1.154165,-6.823621],[9.139019,-7.034478,4.448675,-4.873076,4.503829,-4.278363,4.400782,-9.337069,-5.635612],[-1.896893,5.821766,0.906772,-7.788449,-6.934884,-6.810364,7.558383,6.278092,-8.159629]],[[9.694788,-7.510385,-8.115582,-8.946991,8.182192,-4.670208,1.531646,3.395460,-1.971229],[6.215206,-0.411347,-0.119959,-7.017117,-3.081887,6.840761,7.457425,4.616826,-6.101339],[-9.490183,-0.562801,2.906859,2.485891,3.319861,-6.197922,7.318774,8.581376,9.090009],[-7.289388,8.436385,1.996686,8.441191,-1.412963,-8.001193,1.557844,1.946284,-7.015669],[-6.547100,-5.089507,-9.786046,6.489723,-1.267008,8.989005,-7.414967,4.488196,-7.133847],[5.378564,0.767311,5.197338,-3.626500,9.851053,-5.390570,-7.521406,4.525607,-4.889555],[5.200439,-4.784606,-9.622098,1.576988,6.299029,0.441726,7.072850,-4.092638,-0.533079],[8.674323,-1.051297,-1.976348,-4.779010,0.165705,6.488649,-6.707071,-7.642047,-2.688367]],[[-4.969137,3.574795,1.715152,-2.725657,0.282432,8.030360,-3.025242,-6.449195,7.744021],[9.945951,-0.285282,-7.439894,-6.809279,-7.592848,0.129930,-8.174231,0.889053,8.197994],[-0.676588,7.852876,-9.751175,9.799520,2.478064,3.089310,-8.559512,6.816170,-6.805741],[4.988289,-3.726236,4.469407,-0.042512,5.637822,0.431770,-5.037753,-9.511969,-1.018353],[8.896784,2.407929,0.758189,8.701430,1.226240,-7.091616,-4.450242,7.578017,-5.803734],[-9.489188,-7.012945,-2.650220,8.742687,1.785629,-8.180555,-4.372182,4.360144,9.527210],[1.457022,-1.750691,8.465396,-2.909653,-6.467728,-6.561221,-0.956000,-5.797075,-6.238057],[-5.592465,2.060555,-0.815408,7.760415,6.501858,-2.548009,-8.234773,-5.434736,8.218844]],[[3.905358,6.818709,8.168718,-6.202395,1.946539,-6.277333,2.063544,9.711934,-9.002609],[3.352622,-7.815003,-8.521195,4.244318,-9.776666,4.518690,9.109260,8.328923,3.922114],[-4.553649,-3.106780,-1.901964,7.206548,-3.444889,-0.625900,-8.708613,-8.866792,5.791316],[-1.645645,1.635078,-0.007832,-8.486478,-0.365349,-4.549979,-0.442280,1.480361,-5.533239],[9.097444,-3.844669,-6.345415,-8.088892,-3.089519,-0.578178,1.688226,-2.841149,9.866162],[9.125659,-9.512298,-6.668250,3.160003,8.406661,7.843199,-4.338533,7.572091,-7.248740],[-9.908623,7.555527,-4.525225,-2.936610,-6.116966,-4.720458,3.473079,0.930445,1.661303],[-7.248288,-6.209754,-8.709590,-9.127602,-0.903797,6.312185,6.523691,6.262114,-7.438612]]], dtype = "float32")#candidate|8139|(16, 8, 9)|const|float32
uop_8140 = relay.cosh(const_8139.astype('float32')) # shape=(16, 8, 9)
output = relay.Tuple([uop_8140,])
output2 = relay.Tuple([uop_8140,])
func_8143 = relay.Function([], output)
mod['func_8143'] = func_8143
mod = relay.transform.InferType()(mod)
output = func_8143()
func_8144 = relay.Function([], output)
mutated_mod['func_8144'] = func_8144
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8147 = relay.var("var_8147", dtype = "uint8", shape = (13, 3, 7))#candidate|8147|(13, 3, 7)|var|uint8
const_8148 = relay.const([[[3,-7,-8,-1,6,-3,3],[-4,8,5,10,2,-3,5],[8,6,-3,-2,7,-7,7]],[[-3,-5,-1,4,-6,9,2],[2,-6,5,2,4,-10,-9],[-3,-8,-7,5,5,-3,6]],[[10,-4,7,3,-1,-3,-10],[5,1,-6,-8,1,10,-3],[-10,-2,8,3,5,9,-4]],[[2,-5,-5,-7,-5,-3,-6],[-6,-3,1,7,3,-5,7],[-6,-8,4,5,10,-10,7]],[[-3,6,6,-6,-7,6,-2],[-10,-7,-9,-5,8,2,-4],[-5,6,5,-9,-1,8,7]],[[-8,5,9,4,-6,-1,-1],[-2,-5,-7,5,1,7,-9],[10,10,-5,5,6,-2,-8]],[[-5,-5,-5,4,-1,8,-2],[-6,9,-7,3,4,5,-7],[2,-9,-6,4,7,7,-6]],[[2,9,7,5,9,-5,7],[-2,-7,2,1,-2,-3,-2],[9,-7,-6,-8,-6,-8,-10]],[[-7,2,-3,-6,-7,-3,4],[10,-6,6,9,-10,6,9],[-3,4,7,-1,-7,5,4]],[[6,4,3,-4,-3,-2,1],[9,9,-10,1,-1,10,-1],[-3,-3,-4,5,-6,8,-4]],[[-2,-6,7,-2,10,-6,8],[-8,-9,4,8,-8,7,3],[-3,4,4,-6,-7,9,4]],[[6,-9,2,5,-1,-6,-7],[-5,6,9,-5,2,-5,-2],[4,-10,-9,-7,9,9,-5]],[[3,5,4,5,-3,-8,4],[4,10,3,2,-10,-2,-9],[1,5,-5,1,2,-3,-8]]], dtype = "uint8")#candidate|8148|(13, 3, 7)|const|uint8
bop_8149 = relay.less(var_8147.astype('bool'), relay.reshape(const_8148.astype('bool'), relay.shape_of(var_8147))) # shape=(13, 3, 7)
output = relay.Tuple([bop_8149,])
output2 = relay.Tuple([bop_8149,])
func_8154 = relay.Function([var_8147,], output)
mod['func_8154'] = func_8154
mod = relay.transform.InferType()(mod)
var_8155 = relay.var("var_8155", dtype = "uint8", shape = (13, 3, 7))#candidate|8155|(13, 3, 7)|var|uint8
output = func_8154(var_8155)
func_8156 = relay.Function([var_8155], output)
mutated_mod['func_8156'] = func_8156
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8200 = relay.var("var_8200", dtype = "float32", shape = ())#candidate|8200|()|var|float32
var_8201 = relay.var("var_8201", dtype = "float32", shape = (16, 8, 16))#candidate|8201|(16, 8, 16)|var|float32
bop_8202 = relay.floor_divide(var_8200.astype('float32'), var_8201.astype('float32')) # shape=(16, 8, 16)
output = relay.Tuple([bop_8202,])
output2 = relay.Tuple([bop_8202,])
func_8213 = relay.Function([var_8200,var_8201,], output)
mod['func_8213'] = func_8213
mod = relay.transform.InferType()(mod)
mutated_mod['func_8213'] = func_8213
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8213_call = mutated_mod.get_global_var('func_8213')
var_8215 = relay.var("var_8215", dtype = "float32", shape = ())#candidate|8215|()|var|float32
var_8216 = relay.var("var_8216", dtype = "float32", shape = (16, 8, 16))#candidate|8216|(16, 8, 16)|var|float32
call_8214 = func_8213_call(var_8215,var_8216,)
output = call_8214
func_8217 = relay.Function([var_8215,var_8216,], output)
mutated_mod['func_8217'] = func_8217
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7854_call = mod.get_global_var('func_7854')
func_7856_call = mutated_mod.get_global_var('func_7856')
call_8290 = func_7854_call()
call_8291 = func_7854_call()
output = relay.Tuple([call_8290,])
output2 = relay.Tuple([call_8291,])
func_8301 = relay.Function([], output)
mod['func_8301'] = func_8301
mod = relay.transform.InferType()(mod)
output = func_8301()
func_8302 = relay.Function([], output)
mutated_mod['func_8302'] = func_8302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6107_call = mod.get_global_var('func_6107')
func_6109_call = mutated_mod.get_global_var('func_6109')
call_8315 = relay.TupleGetItem(func_6107_call(), 1)
call_8316 = relay.TupleGetItem(func_6109_call(), 1)
func_5699_call = mod.get_global_var('func_5699')
func_5702_call = mutated_mod.get_global_var('func_5702')
const_8320 = relay.const([5,3,2,-8,-10,-2,-8,8,-4,-9,-3,-3,-6,-4,-6,-6,5,-4,-5,-9,-9,-1,-7,3,3,4,-8,4,3,-10,-5,1,8,-6,-8,-7], dtype = "int64")#candidate|8320|(36,)|const|int64
call_8319 = relay.TupleGetItem(func_5699_call(relay.reshape(const_8320.astype('int64'), [9, 4])), 5)
call_8321 = relay.TupleGetItem(func_5702_call(relay.reshape(const_8320.astype('int64'), [9, 4])), 5)
output = relay.Tuple([call_8315,call_8319,const_8320,])
output2 = relay.Tuple([call_8316,call_8321,const_8320,])
func_8324 = relay.Function([], output)
mod['func_8324'] = func_8324
mod = relay.transform.InferType()(mod)
output = func_8324()
func_8325 = relay.Function([], output)
mutated_mod['func_8325'] = func_8325
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6300_call = mod.get_global_var('func_6300')
func_6302_call = mutated_mod.get_global_var('func_6302')
call_8356 = relay.TupleGetItem(func_6300_call(), 1)
call_8357 = relay.TupleGetItem(func_6302_call(), 1)
func_5971_call = mod.get_global_var('func_5971')
func_5972_call = mutated_mod.get_global_var('func_5972')
call_8370 = relay.TupleGetItem(func_5971_call(), 0)
call_8371 = relay.TupleGetItem(func_5972_call(), 0)
func_4987_call = mod.get_global_var('func_4987')
func_4991_call = mutated_mod.get_global_var('func_4991')
call_8372 = func_4987_call(relay.reshape(call_8356.astype('float32'), [5, 12, 3]), relay.reshape(call_8370.astype('float32'), [5, 12, 3]), )
call_8373 = func_4987_call(relay.reshape(call_8356.astype('float32'), [5, 12, 3]), relay.reshape(call_8370.astype('float32'), [5, 12, 3]), )
output = relay.Tuple([call_8356,call_8370,call_8372,])
output2 = relay.Tuple([call_8357,call_8371,call_8373,])
func_8377 = relay.Function([], output)
mod['func_8377'] = func_8377
mod = relay.transform.InferType()(mod)
output = func_8377()
func_8378 = relay.Function([], output)
mutated_mod['func_8378'] = func_8378
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8433 = relay.const(7, dtype = "uint32")#candidate|8433|()|const|uint32
var_8434 = relay.var("var_8434", dtype = "uint32", shape = (5, 4, 16))#candidate|8434|(5, 4, 16)|var|uint32
bop_8435 = relay.bitwise_and(const_8433.astype('uint32'), var_8434.astype('uint32')) # shape=(5, 4, 16)
func_7501_call = mod.get_global_var('func_7501')
func_7502_call = mutated_mod.get_global_var('func_7502')
call_8438 = relay.TupleGetItem(func_7501_call(), 0)
call_8439 = relay.TupleGetItem(func_7502_call(), 0)
func_7362_call = mod.get_global_var('func_7362')
func_7365_call = mutated_mod.get_global_var('func_7365')
const_8442 = relay.const([[6.648594,-3.950690],[-4.691815,9.127316],[7.679765,8.243138],[7.746741,-2.473771],[-5.971564,5.253636],[0.662310,-3.318185],[0.666416,-5.891303],[7.621815,-6.855048],[-1.306734,9.788206],[-8.837880,1.845752],[4.502633,-6.924931],[-0.626419,9.370154],[5.275238,-6.767801],[2.514069,-5.678227],[-1.059035,-6.210452],[-4.897290,-7.099447],[-1.623380,5.746352],[-2.031875,-5.073207],[-1.448962,8.826778],[0.325915,1.137046],[2.670808,7.228064],[-2.200654,2.633740],[6.500721,-2.381520],[5.129919,-2.927013],[3.590371,-3.330250],[-9.947060,5.583591],[4.134668,3.402062],[9.942344,2.187011],[-3.953360,-3.245376],[-2.918547,6.550465],[7.815813,-3.871185],[0.092889,-4.334337],[-7.406097,-0.245426],[-4.267895,0.674195],[-9.511244,-5.958056],[5.593891,7.412305],[0.687284,-5.161961],[8.740294,8.469002],[-4.632286,2.256503],[-5.467253,-6.784060],[6.284114,2.569565],[-1.503782,8.216534],[9.925400,0.400589],[-2.481652,0.265244],[-0.767131,7.150026],[8.401968,-6.239501],[-8.767247,0.879302],[-3.221008,-3.979197],[2.563192,5.996743],[-0.631320,-2.357894],[-4.189988,2.578294],[-3.341408,-8.250305],[-8.874534,1.633193],[-3.170773,7.598309],[4.925185,9.029634],[-2.179321,0.809720],[0.690954,-0.786059],[-5.411660,-6.285128],[-7.776151,2.725327],[-3.295124,1.377525],[3.326486,-1.022800],[-7.901700,4.193074],[2.678546,8.330686],[-1.840947,2.865599],[5.179736,1.182449],[-1.298328,0.201291],[5.475190,-2.634160],[-9.884839,2.204248],[-1.398418,-9.430053],[3.985617,-0.440158],[-2.133160,4.350119],[9.002324,0.695482],[-9.679887,-5.615066],[-5.225236,5.864315],[-3.889067,3.066917],[3.298422,-9.597633],[-5.968232,-9.884876],[-3.515194,-3.437287],[1.481462,2.353970],[-4.704096,3.337792],[-2.169701,-7.113906],[0.121149,-4.706157],[2.447114,3.732830],[-3.140735,-7.053131],[-5.131520,1.824416],[1.118529,0.218579],[3.466820,3.648892],[9.647684,-1.907386],[-2.213911,-4.395476],[-1.048144,9.751099],[-6.475789,-9.290764],[4.596357,-6.080136],[4.554650,-9.950876],[3.539736,6.959510],[0.381056,9.277037],[-1.546904,-9.129009],[-2.466607,-3.818049],[0.305813,-5.526622],[-6.198293,6.908658],[4.302145,3.032652],[2.233316,3.890508],[-7.341188,2.408757],[-3.631788,-1.044563],[-2.837314,1.364573],[-5.021843,9.225521],[-2.022579,1.348043],[-4.507473,-3.318083],[-7.977067,-5.559440],[7.449381,8.428992],[9.246780,5.165144],[1.771662,-0.422368],[-9.540298,-3.975477],[7.311841,9.125202],[4.927638,2.321002],[2.803501,0.922227],[2.548172,6.543458],[9.242044,-2.899969],[9.441851,-7.176090],[-6.077897,-8.620349],[6.195790,0.419132],[-6.986958,-5.652386],[4.052571,7.514796],[4.925409,1.562891],[-0.824333,2.516771],[2.214785,-1.805508],[-7.284522,1.234785],[4.587200,7.774812],[-2.613142,-7.305094],[7.301235,-8.291776],[-7.010090,6.753837],[-9.331231,-4.507705],[1.322505,-2.397772],[-5.937920,9.527712],[-0.738116,0.437204],[-3.230461,-4.641690],[0.999776,6.747884],[5.765169,4.829823],[2.438727,6.481722],[1.513247,6.081204],[5.438526,2.934101],[-5.672425,-6.876514],[9.017767,9.714682],[9.351685,-8.372556],[-7.281758,3.830205],[8.539346,1.909332],[-6.926389,-3.081339],[-3.762116,-9.121686],[-3.568484,1.000025],[7.158498,3.881552],[7.610580,-7.120516],[-7.837324,0.805547],[8.906378,-2.916291],[-6.438566,8.082090],[-0.867619,-7.679370],[8.755241,-9.603641],[7.990604,8.065485],[-6.812499,5.491831],[2.136099,-8.870315],[5.349281,-3.726936],[-7.950830,1.008341],[-1.671560,2.024845],[0.247171,7.381450],[0.941316,-2.001366],[-1.048576,1.724814],[-4.138307,-2.449006],[-8.891023,4.000200],[5.054412,-0.729978],[-0.403290,-6.003907],[7.546639,2.644785],[3.920051,0.028648],[-6.165806,7.362956],[3.598712,0.967508],[-8.538091,1.602888],[-6.297462,-5.448259],[-1.553222,-8.669913],[-3.987931,8.099586],[-4.292116,-5.318437],[-8.598046,-6.907584],[1.725411,0.614841],[-6.911771,-9.572994],[-6.582755,-7.427840],[-7.908895,-2.392912],[0.463241,5.476594],[0.774208,6.063241],[5.318799,-2.480447],[-4.377693,5.903205],[-7.132618,-1.995590],[5.413021,4.833411],[9.700106,6.331675],[-1.844240,-5.723735],[-7.191887,-3.815374],[7.860842,1.494968],[2.720882,-5.882699],[3.632509,-7.116953],[-8.051193,-4.417903],[8.421841,9.052478],[5.229237,0.546673],[8.806660,-0.091658],[9.415036,6.498861],[-8.869227,-1.725811],[-1.563594,9.336249],[-5.173868,-4.338861],[7.127588,-0.508605],[-5.055868,9.302181],[-5.141866,-0.925978],[-4.544892,8.491254],[6.641512,-5.647897],[-1.140712,4.911050],[4.484829,-7.305147],[-4.834058,-7.312994],[4.702173,0.604633],[7.696358,-0.576154],[0.145748,1.181389],[3.087803,6.723454],[7.472102,-7.463103],[-2.980401,9.557671],[3.089330,5.158552],[-1.298636,6.868305],[7.127685,0.870710],[8.245619,-7.691520],[-1.071029,-8.391778],[7.684193,-8.728455],[-4.602009,-0.877698],[5.618531,-7.152525],[8.815010,-9.066782],[-4.787249,1.282228],[-4.576165,-3.456577],[-9.060322,-2.667438],[-3.760167,-4.859049],[9.309266,-2.184197],[-7.936024,-8.794623],[-0.173155,-2.595548],[1.025316,8.854470],[-6.017917,8.744019],[-3.549071,-4.851692],[-3.180722,5.596265],[7.441198,-9.262930],[2.177343,-6.762483],[8.733180,6.475912],[-5.287016,7.175866],[-0.089583,1.927980],[-8.978276,-4.869944],[-8.009085,7.832421],[3.267970,3.642212],[9.822387,1.655517],[-5.576686,-0.965854],[7.345231,-1.211723],[9.111909,1.250353],[-3.932017,-8.037353],[6.252820,4.891718],[2.632857,-0.192349],[-9.003154,9.184782],[-3.583027,-5.934172],[7.783465,-8.152531],[-3.130716,-0.284002],[9.713507,3.975264],[-6.572711,-7.049394],[-3.789558,6.991577],[-4.732866,1.085176],[1.666542,-9.530353],[5.869235,-2.824079],[6.599449,6.770191],[7.975933,7.165463],[6.308420,6.791706],[-5.543738,7.202438],[4.093889,-9.606397],[3.936178,-1.121708],[1.052669,-0.189927],[7.461535,8.266275],[7.897452,-8.291546],[-2.409685,8.866428],[8.577492,1.897828],[-5.584122,-0.597821],[9.340848,-3.876041],[-3.885498,4.374603],[4.002027,5.235460],[-6.962281,-3.390271],[5.782866,0.789425],[-2.399807,-0.763033],[9.232256,-1.326964],[-1.249254,1.568893],[5.569833,-1.414105],[9.611694,1.533465],[2.643920,5.413712],[6.627092,-9.856737],[4.705280,-5.018578],[-7.082904,2.393677],[-5.651510,-6.965709],[-9.099703,-2.170812],[3.951976,-8.533865],[-3.100588,8.997704],[-1.021854,-4.678599],[-5.764534,-5.369213],[-5.266782,-4.098456],[9.781996,-8.931993],[7.834217,9.289693],[-8.792810,3.618213],[-0.674466,-5.803502],[-9.766718,3.222361],[6.843367,-4.246976],[-8.658511,7.510021],[-6.651749,5.006049],[6.345134,0.536759],[-3.932656,-4.242003],[6.841308,-6.316483],[5.499973,-0.479515],[9.811289,-7.097572],[7.683279,-1.288383],[-1.587031,-5.480997],[6.041247,-4.620676],[6.059762,1.261864],[-8.245212,2.662850],[-8.917445,-4.048307],[-3.142809,2.402035],[-3.315676,-2.785497],[-3.730166,6.821517],[-1.335595,6.909924],[7.817626,-6.400448],[-0.632275,0.906850],[-9.690608,-7.527381],[-8.619938,-0.484900],[8.647535,-5.277546],[-1.947120,-4.527122],[-3.201444,1.774783],[0.734500,-2.243305],[-9.243276,-6.538551],[8.599617,-5.758326],[-7.035336,-5.775794],[5.801699,6.581116],[-4.596843,-7.208636],[1.588047,5.603376],[-8.765050,-4.037020],[-9.320699,-2.967156],[-0.617552,3.516841],[-2.596387,4.307250],[-7.436329,-4.151307],[-0.862014,-8.637601],[0.238878,4.852808],[3.407525,-8.765591],[7.386456,-4.183906],[-0.201110,3.875022],[1.923713,-1.844002],[-4.109640,-1.862696],[0.053263,-4.211538],[-5.042325,-5.537877],[9.487992,-0.392213],[-4.185040,-3.451884],[-3.727730,0.051354],[1.872482,3.489871],[5.446532,9.870434],[9.654466,-2.423907],[-3.569883,-7.201649],[-7.064777,-3.510360],[0.785663,-9.744294],[-2.028256,0.999093],[3.616833,5.138271],[8.125097,7.030742],[-8.558026,-1.056931],[-0.850845,-7.471829],[9.684165,-4.502970],[3.056604,6.779463],[7.422474,-4.473300],[-8.868846,-6.082547],[9.826088,2.965152],[-9.384163,9.862392],[7.378397,-3.392253],[2.029976,-8.580243],[-2.291065,-7.277259],[3.203786,-0.064919],[8.506461,-0.126365],[-3.493476,-1.597295],[-1.449464,5.865488],[-5.784766,3.548975],[-0.223232,-9.866376],[-5.526801,7.391219],[2.033259,-7.307569],[1.282127,5.711675],[-8.916938,3.278083],[8.395417,-5.369192],[8.481012,-7.639251],[-6.838753,8.304005],[-9.452614,-2.405570],[-7.320908,9.532242],[3.090501,-8.367283],[-3.240861,-8.092658],[-2.153652,5.951101],[6.585861,8.493162],[8.342711,-6.535137],[-5.570315,4.119713],[7.735674,8.589993],[7.635506,8.164951],[5.509404,7.519121],[-5.134089,-7.976166],[4.076247,-1.342363],[7.444841,9.168126],[6.477048,-3.583747],[1.738398,-7.599043],[-9.788396,-7.808570],[-7.474323,-6.139929],[-2.948889,1.736388],[0.293124,2.235246],[-9.848038,1.158293],[7.459837,-8.777795],[9.971327,-2.769332],[-9.066540,6.050815],[4.913532,-4.035465],[-2.206324,3.657559],[3.176291,0.566786],[-7.867562,5.556683],[-3.185386,-7.256007],[-8.274400,-4.454709],[7.722806,-8.931671],[-1.248238,-1.417758],[-3.518485,7.576606],[-7.648059,8.442183],[-5.540360,-6.212472],[0.869871,2.936377],[8.095319,3.005276],[-6.161604,4.380652],[2.905107,-1.153420],[6.609573,1.852531],[7.818947,-9.109971],[0.680794,3.455509],[-1.746492,-6.492567],[-3.260009,0.590556],[7.075087,0.020340],[3.014503,8.521013],[-8.957843,-5.419661],[6.382808,6.497202],[-5.613731,-6.006541],[0.529874,4.232418],[8.526152,4.738791],[4.782505,8.309917],[-7.794500,7.060786],[0.973051,-4.254328],[-1.070197,-5.678995],[-6.371357,-5.954940],[2.373330,-0.012016],[8.474063,7.593578],[7.944275,-6.910509],[2.844939,7.027030],[-1.902786,6.619288],[8.094335,5.014369],[-4.934569,6.549575],[-7.264999,-1.548246],[-6.156992,-6.457617],[-2.103913,3.290506],[9.823173,5.508103],[6.984637,-4.877703],[3.854567,-7.485501],[0.630425,-9.095972],[3.789200,-0.770491],[0.294184,4.490837],[5.044187,1.940583],[6.293220,8.768015],[-3.507950,-1.786066],[6.274792,9.420923],[-3.628394,6.721336],[-6.882699,-2.729600],[-3.897375,3.612308],[4.506376,7.879998],[-1.067378,-1.682555],[1.830907,-0.277651],[-0.194318,-0.019451],[0.857636,-8.333293],[3.453084,2.125704],[4.875588,3.951916],[-4.512485,-1.470374],[5.260621,-4.263792],[-6.610863,-0.748809],[-3.213844,-4.790466],[4.957830,-7.279094],[-5.174574,-0.937425],[4.272074,6.548295],[6.726293,-8.846716],[4.439392,0.807254],[-2.709321,5.902512],[3.776234,6.553463],[-8.778916,-5.418124],[-6.714762,1.054636],[-5.666006,-6.931120],[3.504763,-8.616041],[-0.419633,2.039930],[2.433843,-4.421978],[-0.287047,9.006881],[3.591276,-7.462980],[-0.301891,7.519481],[4.140745,4.362467],[5.121841,4.607339],[-9.072107,0.383415],[-1.614096,-4.341368],[-0.559052,-2.954082],[-7.442305,-9.373654],[-8.819772,-4.673962],[4.364882,7.616573],[-1.353000,-6.321269],[-4.034732,-2.210471],[-6.193235,8.423641],[-9.893633,-7.777166],[-2.891910,-4.066815],[-1.253079,3.705719],[0.361012,5.238722],[1.433439,1.607643],[-6.189625,9.998769],[-2.803410,5.494385],[-2.049491,2.307848],[-7.556958,2.891310],[-5.206950,-7.846234],[-7.549251,0.847232],[3.149167,-6.832739],[2.787846,-2.310052],[-7.622121,-2.983397],[8.165451,1.939261],[-5.903780,2.861671],[-6.287359,-6.188964],[-8.124802,-7.828262],[-1.000042,-1.144991],[-3.744664,-3.249872],[-0.980962,6.841545],[1.252785,6.254702],[9.266127,-6.379105],[-9.993463,1.840009],[-7.210441,8.947775],[-6.959424,1.500650],[-4.842159,-6.249753],[-5.457372,-2.747363],[1.046698,6.934675],[-5.861333,3.712375],[3.278602,4.797076],[9.498139,0.739661],[-2.584981,-2.741109],[-7.015367,0.792545],[5.962762,8.592492],[0.789687,5.682747],[-6.879022,3.742329],[7.103083,-6.832296],[-5.109532,-1.126774],[-1.826929,4.923252],[8.933615,3.921341],[0.018868,-0.243331],[-5.065961,-5.187920],[3.308740,-0.908740],[2.075961,-9.017209],[8.703477,0.407495],[5.945179,9.037245],[3.762302,-8.648634],[0.841782,-7.430926],[3.338647,9.421155],[7.124178,8.853598],[5.115926,-0.938219],[1.952258,-2.745497],[2.385824,-0.313469],[0.446878,8.685695],[-6.904473,2.019500],[3.185287,-5.282969],[-9.801694,9.914221],[9.592343,3.788621],[-6.040730,9.034448],[-3.149446,-8.498287],[-7.770944,-8.611460],[5.258747,-3.293904],[-9.538882,4.727989],[-3.605105,-3.191101],[2.629151,-5.556198],[-8.731377,-7.798291],[8.502859,-4.840426],[1.635581,0.885938],[3.833034,0.617273],[7.051257,-5.364866],[-9.900926,-1.116904],[2.880310,7.321303],[-2.108481,2.038526],[4.687143,1.920677],[-2.454730,3.193729],[3.662860,2.643773],[-9.510048,6.974465],[-7.882313,0.889537],[9.653831,7.614432],[-6.469381,5.655977],[-8.181128,8.975315],[-2.720446,-1.862429],[-3.370729,-4.603209],[5.106663,-5.014919],[6.975745,4.419129],[8.976704,-2.451461],[-8.277853,5.797715],[-2.583644,4.373254],[-4.462245,4.623771],[-2.807376,3.592083],[9.914137,-3.551192],[3.279976,-9.832804],[-3.008986,-7.380758],[7.532995,-7.024480],[6.252523,-8.112485],[-5.599895,-5.124930],[8.329396,-7.808682],[-5.388019,-8.617530],[3.167285,-3.724523],[-0.661216,1.766604],[-0.899525,-3.022143],[-2.088329,-6.913475],[1.809235,-3.223848],[-4.102202,-2.864580],[-4.446622,8.650902],[-0.056412,-6.331469],[-3.013985,-3.440175],[5.924970,1.483508],[2.488219,5.538062],[-6.531761,5.517141],[3.937400,-1.978459],[8.559894,1.169237],[0.419646,-0.772399],[-1.533064,7.400599],[9.486749,2.778243],[-0.774548,-6.554898],[9.529474,3.894439],[6.378332,3.137451],[-0.608241,9.958605],[-0.320271,2.617599],[6.548426,5.250636],[-0.444538,1.460005],[-8.141245,0.656793],[9.257675,-5.330090],[2.973479,9.022826],[5.687189,7.139494],[-2.592326,7.390116],[4.421731,-5.311153],[-7.148019,6.230237],[-4.558165,-0.860888],[5.220107,3.010165],[4.088208,2.392160],[-0.407016,-0.671818],[5.918992,5.256570],[-5.204174,-3.373681],[-2.038884,-4.930766],[-1.162788,5.010757],[-0.758577,0.686187],[8.856469,1.320372],[1.462847,-4.944861],[4.399966,3.743440],[-2.841353,-4.981473],[7.921934,4.916613],[0.257151,-0.729232],[5.091828,-9.578387],[1.275090,7.669256],[0.095566,1.074414],[-4.657165,-5.782236],[-9.274886,-2.349958],[-3.347168,6.857785],[-2.721176,3.283351],[1.356450,8.354491],[-1.885165,-2.614843],[-0.959197,-6.962311],[-8.157176,-7.247217],[1.424356,-5.221961],[-9.247370,6.785457],[8.116354,-0.490384],[3.952507,5.199046],[4.753139,2.255288],[4.972840,9.268729],[0.429991,1.157547],[3.463055,-7.910204],[-2.960732,0.839274],[-4.720886,3.850686],[9.162400,1.279990],[-2.754735,3.030445],[1.494344,7.650799],[1.214992,-4.023115],[-7.164060,-4.373601],[8.463129,4.823125],[-0.284044,-6.812339],[4.535910,-4.681744],[9.186632,0.689756],[4.453697,0.197923],[3.130687,7.487228],[5.724465,7.107338],[7.549726,-4.527661],[8.341284,-7.913231],[-6.286058,-9.195337],[-3.696975,-5.766703],[-6.380670,4.627479],[8.851105,-2.192661],[1.321428,1.713344],[-7.101140,0.658686],[-8.564822,-8.762925],[6.885887,7.849110],[-4.787115,0.860121],[7.371070,-3.841399],[7.827966,7.884017],[6.550295,8.334217],[0.997999,9.930716],[0.347407,1.458202],[-3.886969,9.953188],[-0.697429,3.569072],[-5.690589,1.978891],[9.725026,2.308690],[-0.873689,6.418267],[4.771684,-4.036565],[5.171339,-7.066636],[-2.940724,-4.742993],[0.469303,-9.430326],[7.628791,-0.524407],[-2.635993,9.249678],[-4.802536,-0.348888],[5.792618,-3.000725],[-6.136899,3.662076],[-4.206457,5.012167],[1.245913,-3.785605],[4.784228,-8.269873],[-0.918886,0.222045],[-2.774352,-1.507109],[7.728529,4.768150],[-7.413485,3.215037],[2.772387,-4.940666],[-7.542835,-7.032972],[-3.557440,2.476965],[-3.665439,-6.640958],[-4.360130,8.680083],[-2.313249,5.268003],[3.908433,-9.790700],[-4.610328,-4.094827],[-1.291506,-7.353581],[-8.067873,-9.014908],[2.584287,7.168721],[6.196066,-4.631875],[4.609086,-6.926263],[-8.949772,0.937359],[8.383901,1.830574],[-4.780443,1.933664],[3.050647,2.066251],[-2.173395,-1.943000],[8.193430,3.772027],[4.984190,9.233193],[-1.639709,-4.137021],[3.604256,-9.069982],[7.828741,9.544846],[8.819547,-2.090071],[-2.384870,0.015054],[2.455492,-2.159416],[4.421576,5.845165],[5.516178,3.103801],[-7.723078,-0.595713],[2.838327,-3.876639],[8.128763,-1.101563],[-4.974793,1.924465],[7.975856,-7.368066],[-1.797814,1.287389],[-9.567851,-9.182900],[3.584296,1.868663],[1.923524,-3.445881],[-2.967513,4.554859],[-8.907001,7.141132],[-2.378824,0.058104],[0.715054,-1.814270],[-1.901945,4.057382],[-5.341432,-4.872871],[4.744407,3.526300],[-6.008300,6.273689],[5.904884,-5.333986],[2.182777,-1.834967],[-9.081067,4.045390],[4.219644,3.282672],[8.218749,0.565836],[-3.840904,-2.474491],[0.496017,-4.702346],[6.795471,7.904705],[-7.486339,-9.386526],[5.357164,0.666681],[-0.087144,4.943345],[-3.990031,5.629606],[7.185554,3.665020],[-6.799529,3.770367],[3.374856,3.746893],[9.250884,3.660058],[-8.497493,3.000740],[1.294489,5.469357],[7.418242,8.635869],[8.011312,-9.277640],[9.263697,-9.487375],[8.076125,-4.618996],[1.057356,8.822840],[-9.842246,-2.286138],[-8.626349,-8.446352],[-9.279301,9.470070],[-3.091099,1.026742],[1.930008,-6.407695],[0.401040,-6.539746],[-6.949703,-0.723506],[5.936893,-8.214014],[-7.915028,-2.602740],[1.271337,-2.844854],[9.017665,2.000860],[8.418307,0.125333],[-2.152719,7.945849],[1.389552,-4.791881],[-4.574469,7.018183],[-8.110615,1.484422],[4.229091,2.855417],[-8.353599,-4.284685],[0.874198,3.475770],[2.746651,8.463910],[-8.848856,4.093169],[4.695596,7.633115],[-7.481321,3.769824],[6.666113,-8.890766],[-2.244297,2.134840],[8.008938,-0.512774],[4.358433,2.453642],[6.569513,8.995884],[-6.406662,7.482013],[-0.277175,5.111491],[8.291485,-4.280400],[-6.647440,3.884860],[-3.196621,9.910290],[5.038322,5.511572],[-2.161271,5.414292],[8.624852,0.746613],[0.932272,9.264059],[-1.427378,8.335299],[7.584538,-2.085436],[-5.985036,3.771948],[-8.851685,-1.134030],[-4.437474,-6.124307],[4.375790,-5.578772],[-3.410964,-6.817640],[-0.640475,-6.462609],[-0.845102,9.693978],[6.405615,1.036787],[7.569135,-5.038730],[-7.853452,3.945859],[-7.156235,6.453251],[0.481078,4.929772],[0.924150,-6.484237],[7.908892,-4.763020],[-6.423327,-2.398123],[8.067397,7.583399],[-9.588010,-4.725582],[-2.831266,6.459956],[-9.893078,-2.027480],[3.751375,7.686944],[7.027314,-6.301137],[-0.887361,2.890322],[-4.734847,-8.130104],[8.541067,9.949395],[-5.509751,-5.535781],[9.820063,6.044294],[-3.204569,-5.523371],[1.623443,4.163140],[4.709949,-7.064951],[-2.727594,-7.905823],[8.906446,4.114418],[-9.464092,-1.322832],[-5.003690,8.763037],[-3.469126,2.007507],[3.608923,-3.540884],[-3.876557,1.712821],[-9.209874,7.328387],[8.388970,7.414261],[2.745281,-3.591756],[0.655862,-9.477567],[1.557472,-8.689136],[-5.626965,3.403673],[6.257669,2.801208],[6.682389,7.581717],[-4.576440,-4.050246],[-5.986361,-4.616823],[-0.571872,7.138650],[2.776103,-0.331199],[7.419867,-7.645739],[-0.176283,1.071997],[-4.673468,7.879913],[-4.407894,9.581028],[-0.573763,-2.836560],[3.523550,-8.284690],[6.981487,-2.127207],[6.871079,-7.706318],[1.018185,-2.700233],[-8.752768,1.127509],[-1.432287,-9.944056],[7.581467,1.793402],[4.775150,-1.411718],[-7.929444,5.991781],[-8.334068,-3.757129],[-4.811403,-2.222043],[-9.118517,6.665248],[5.674124,9.849021],[-1.193622,-0.036821],[7.519887,4.736293],[9.500318,2.199182],[-9.276141,-8.590082],[-3.350017,-4.643229],[6.833478,-0.205485],[5.321122,-3.090918],[-5.748828,3.221055],[7.113604,-6.120458],[5.383800,9.695903],[9.374363,2.055330],[3.078382,-6.797718],[-6.500374,-2.151832],[-4.088806,3.815906],[7.254560,-4.603990],[6.095505,-7.226606],[2.280580,3.608761],[-3.671359,9.296868],[-3.650103,4.491854],[-4.614392,8.706201],[-4.387569,-9.194355],[5.835554,-9.931993],[4.289052,-6.687464],[-4.362662,3.048324],[-2.561517,1.586325],[-4.730356,-4.501223],[6.189926,-0.333771],[-5.425139,-6.595064],[-6.158413,9.253261],[0.518476,-0.146091],[-0.653647,7.174450],[4.262951,-5.639646],[-1.891830,-8.091600],[-2.230649,4.881985],[-9.192554,-1.534044],[1.594367,7.765894],[5.408967,6.015799],[-9.943751,-9.112166],[7.236420,-9.481899],[-6.108049,-9.897537],[-0.222667,2.092615],[0.242542,-7.452717],[7.996786,-4.560764],[7.994028,-2.421261],[-8.935861,0.738591],[0.159848,5.503017],[-8.105988,6.930234],[-6.978400,3.645273],[-5.675538,-2.589273],[6.108568,0.565497],[3.110035,8.227757],[0.724885,1.649741],[-9.147158,-1.516930],[-9.051734,-5.589903],[7.343613,-1.935767],[9.150682,-6.516032],[-6.438685,1.173555],[2.998656,-0.422208],[1.337050,-1.134304],[5.052882,-0.460360],[-5.099684,5.077343],[7.896080,8.697314],[0.891314,-4.937708],[8.959277,-8.331529],[0.185724,1.393816],[-4.528990,7.777046],[-1.139602,-8.750495],[-4.656507,3.855943],[-3.554549,2.223834],[-7.695257,-9.986956],[-1.516873,-1.937645],[-6.228394,-2.824674],[-2.993682,-8.015217],[5.665965,-5.919067],[8.145964,-5.001932],[-3.882443,1.228855],[-4.726249,-5.481113],[1.090734,8.357832],[0.061077,-4.601668],[-4.194800,-0.979164],[-1.310137,-9.595583],[-3.014256,3.084265],[6.450004,8.735125],[3.381613,-7.266660],[-4.362388,-3.678354],[-1.155529,5.677551],[1.043783,5.981514],[-4.834524,2.154142],[-6.004718,2.415187],[-3.905069,4.225931],[-7.891520,0.340431],[6.619647,4.526163],[-1.811051,5.447468],[8.216563,0.538578],[-4.921971,1.551279],[-6.600390,-5.874370],[-1.565811,0.381390],[-9.944143,-9.587864],[-0.641175,1.583222],[-5.713590,6.194124],[-8.073955,6.737034],[8.829028,9.352990],[6.818386,0.993000],[0.872297,-5.322309],[1.461596,-0.200780],[-1.984643,-9.850076],[3.213624,-1.389144],[-5.210861,-3.669891],[3.347944,2.022675],[-2.458584,-8.524213],[3.098013,1.244020],[8.716882,-9.651948],[-2.515428,2.406521],[7.329026,3.525548],[4.606155,-7.613851],[7.854292,-2.895156],[-6.132465,3.602076],[-9.583325,-4.401016],[4.886049,-1.775894],[-7.355113,9.901451],[-9.813195,5.073803],[-4.777515,-6.246376],[2.956675,-0.014313],[9.344281,1.730567],[-3.130662,8.490850],[-6.980568,-3.044512],[9.859477,2.990996],[1.325098,-3.519700],[6.515561,0.040744],[-5.248640,0.710855],[9.816176,-8.681537],[-0.973002,-3.299749],[3.175148,-8.114608],[-3.174426,7.750375],[3.721230,2.137340],[-0.385968,-2.852338],[2.373807,3.284005],[3.717021,7.185266],[-0.210246,-4.363368],[0.891990,0.265173],[-7.082323,6.580052],[-9.750292,-1.593712],[6.106973,-7.719300],[-0.952072,9.625471],[6.329523,3.197071],[4.264790,8.035724],[9.696089,-8.560914],[-2.863040,9.584171],[3.129464,4.686312],[5.156021,-9.523583],[1.203278,-5.703431],[0.517155,-3.481271],[7.816406,-8.836777],[-6.317859,-6.499565],[2.701183,3.923350],[3.649152,-4.664946],[7.847888,-6.165650],[1.099317,8.028077],[-1.739717,-9.225942],[5.472001,-3.791825],[3.645177,5.333074],[-2.365279,1.205657],[-0.656808,6.001147],[0.606307,6.611124],[-5.246705,9.522564],[-5.596210,-3.392965],[6.035805,-1.250641],[8.900689,2.691178],[9.555607,5.332646],[-2.744906,3.302017],[8.667418,-6.603634],[-3.533158,4.962624],[-2.192554,3.012121],[9.018039,8.735290],[-9.631777,6.395094],[-8.591222,-0.802433],[6.002422,2.031120],[-4.149937,-5.286268],[6.781287,-4.814952],[-8.015849,-9.069203],[4.937177,7.682307],[-2.148158,0.368415],[2.015613,-6.930417],[7.280667,5.530734],[-6.024219,-0.304915],[-7.248628,-2.652302],[-4.103859,9.500204],[-4.331455,7.874901],[0.308901,-2.309564],[3.074418,9.733958],[-8.669338,-7.371736],[-8.875059,-7.041592],[-8.306615,-9.095475],[-9.110847,-5.626225],[1.460726,6.020360],[-8.952276,8.731718],[-8.186672,0.317258],[7.528208,-9.641893],[-2.533854,9.227544],[-9.876662,-8.213790],[1.605273,5.736447],[0.388776,-0.584271],[-6.481163,8.037049],[-4.568473,-1.752505],[-7.060365,-6.598276],[-5.349865,-2.717619],[9.271464,-2.015221],[1.655505,-5.442301],[8.948758,-9.079434],[8.720695,0.922223],[2.782351,-9.768189],[-1.919420,-8.675527],[-3.371004,-1.043072],[3.843435,-7.085789],[0.268624,-3.367170],[8.476658,6.651505],[7.197522,2.970694],[-2.751082,-3.194562],[7.577852,4.797098],[6.835211,7.194825],[-9.131475,4.739707],[-8.878085,-7.168413],[-3.041089,-9.388559],[8.176611,-5.756579],[-1.937910,7.663831],[-3.392632,-3.544731],[1.119633,6.142460],[6.697228,-7.165804],[7.404831,8.096688],[6.918869,2.875619],[-7.279123,1.255104],[7.357023,-5.476356],[-7.782936,-1.149066],[2.888368,-0.448339],[-7.286221,-2.473621],[-0.616892,7.086658],[-2.707265,0.426230],[-5.420445,7.779100],[7.196911,-0.799267],[-0.529978,-6.916050],[-1.718013,6.409822],[3.378680,-4.375269],[-3.073545,1.687840],[-5.945200,-1.642109],[7.846964,-4.321699],[-3.263113,-0.488649],[8.109038,-9.946225],[-7.505255,-4.425153],[3.652450,-6.984784],[8.925737,-6.248451],[7.361033,5.062451],[-6.024356,-3.796246],[9.093021,6.404713],[-6.487022,0.662957],[-7.858394,0.566181],[-4.272224,2.624360],[-1.115185,-2.487552],[6.946766,4.686135],[-0.747488,-2.716010],[-0.373507,-0.512521],[0.841536,0.755917],[-6.848377,0.609560],[-5.140438,6.498822],[-9.744447,-8.162408],[-9.350049,8.728530],[1.130686,6.062609],[0.960750,-2.986168],[-2.734655,9.203328],[-5.493035,-2.763749],[-5.265192,0.275769],[-3.046021,8.033483],[8.678292,1.529152],[5.074929,6.592253],[1.652287,-8.831846],[-5.935139,-5.354732],[-3.430859,3.039897],[-6.373185,8.095242],[6.433104,5.250217],[1.070855,2.647586],[-8.939280,-8.030925],[8.223802,-8.886180],[-5.299723,2.269312],[7.071194,-5.842855],[1.647463,-4.913463],[4.189051,-8.295074],[-0.618448,-4.442727],[3.538480,5.639172],[3.892012,1.011441],[6.118640,4.868765],[-0.334038,5.570780],[3.702034,7.986545],[1.425302,-6.467414],[2.874394,0.015064],[9.453374,9.261200],[7.447861,-7.094730],[1.903000,4.189505],[-0.227822,-9.670513],[5.575333,-4.634868],[8.653196,-8.921416],[-4.094487,8.365872],[7.760654,3.042378],[0.971220,2.347637],[1.118337,1.529303],[3.612850,-9.469726],[7.891605,0.175651],[-6.185416,1.122136],[6.131047,-7.163335],[8.093975,-5.979206],[-8.965243,1.546956],[-9.135452,6.078019],[-4.119073,-3.145203],[5.450886,1.892166],[-8.327814,-1.671798],[6.915868,-9.322863],[1.904795,-8.063781],[7.725048,4.128817],[-4.125383,7.352160],[-5.208577,1.925752],[2.884366,-2.141593],[-5.124839,8.068078],[-5.679904,6.781076],[-6.193743,1.687799],[-7.850499,-5.591100],[-4.134028,5.765907],[-9.160387,8.454444],[1.408163,2.568517],[1.752389,-0.626879],[-0.120184,-9.969806],[1.698610,-9.005972],[7.744683,8.732904],[4.298916,6.547367],[4.121903,-5.668927],[8.312336,-6.654563],[-5.111920,6.170522],[-9.888465,0.277984],[-2.896547,1.168063],[6.040865,8.604967],[5.657017,-9.980079],[-2.412946,-3.906929],[8.214215,3.585829],[5.830385,7.458331],[1.597774,9.558006],[-0.354203,-6.580598],[-4.910648,-4.178262],[2.102551,-6.028523],[-5.253869,0.003598],[6.345694,3.719404],[2.007981,7.191402],[-0.407411,-3.403105],[-9.629523,8.711909],[8.332287,7.884016],[-3.259860,6.393744],[0.286155,-5.504385],[7.080730,-6.489427],[-7.003563,7.542573],[-2.661317,-7.313167],[2.910553,-5.979313],[-7.951041,8.671688],[-2.374955,9.160180],[-7.513152,-4.212332],[-0.356159,-2.608341],[1.561308,-2.353971],[-7.296062,2.442145],[4.810360,8.577574],[-0.005212,-2.010568],[-0.039609,-2.360547],[-7.823846,7.489261],[6.784107,-3.547040],[-4.103350,9.937963],[4.761792,3.741471],[3.882407,-4.651947],[-3.454424,6.725934],[1.746988,2.954454],[2.121243,-0.934967],[1.621359,8.280628],[-8.056971,1.757780],[-6.429170,-7.144697],[-0.814532,8.335744],[-7.713963,-1.423444],[8.886693,3.888144],[3.098735,-8.380052],[4.941707,-7.608383],[-4.931091,8.719325],[1.502656,-4.296314],[6.378284,1.664532],[-2.408032,4.944365],[-2.981658,-8.226629],[6.631366,5.655484],[-9.786353,-4.292038],[-9.666660,4.588448],[-4.522877,8.374931],[0.375987,2.139744],[-9.098996,-6.119972],[4.405332,0.792440],[-0.035715,3.345018],[-5.542483,-2.588318],[3.217826,-2.066764],[-6.407750,-4.681287],[-3.787929,-5.378998],[4.952961,-3.107246],[5.389730,9.697304],[-5.077246,-5.256120],[-1.712883,-9.662562],[-5.538112,7.079094],[0.828961,-5.853129],[1.694215,-8.555918],[-1.656618,4.416676],[-2.877613,-0.253664],[0.778574,-6.774530],[-0.451455,-0.887374],[8.619744,6.250219],[9.471960,8.519986],[-2.826600,-4.912633],[-5.863865,0.620213],[-9.623632,8.795356],[-8.757196,-4.483979],[2.334030,7.112492],[6.644161,-0.631681],[9.335791,4.863224],[-7.846181,4.186300],[-2.658606,9.137065],[4.142524,7.617416],[2.289274,-3.325983],[-8.964613,5.008806],[-8.844425,-2.758709],[-3.446720,-6.211195],[-8.487827,2.405954],[-6.206490,-3.016713],[-2.198234,4.877631],[-7.164510,3.279653],[7.452234,-9.210767],[-4.314868,5.917716],[-5.433045,9.540994],[-1.111089,-7.650373],[0.117005,-3.722198],[2.421623,-8.022586],[-6.314604,3.589352],[-6.851565,-1.629621],[-0.539513,-8.958401],[4.783890,0.399790],[2.151560,-4.043325],[-6.041656,-7.724574],[-8.792101,2.662131],[0.256969,-1.531795],[-8.602835,1.786813],[-9.771522,-2.697428],[-9.148758,-1.788963],[9.393376,7.254388],[-0.444750,-1.221204],[9.753872,-7.145621],[9.164917,8.044912],[5.176494,-3.906950],[0.277559,-2.695359],[-0.688919,-0.292137],[8.861987,-6.402754],[1.443424,5.291153],[1.023409,-3.707509],[9.278952,8.350612],[1.589440,3.186989],[-8.879638,-9.377450],[7.156061,8.294952],[3.627142,-1.883737],[-1.811874,4.591844],[9.062603,0.685761],[8.942843,4.410983],[-6.188108,0.759453],[2.751645,-3.298287],[3.216265,8.304517],[-1.442985,-6.640815],[-0.826716,-8.001683],[2.525809,-6.016699],[7.562694,5.137919],[-0.684800,1.274019],[6.929454,-0.927072],[4.788874,-3.247503],[6.647647,-5.206820],[2.154916,3.791968],[6.322399,-1.389910],[-3.628537,0.250111],[5.560137,-6.193107],[3.035413,-2.058770],[-6.160720,5.341726],[-0.135490,-2.498170],[1.851065,8.945718],[1.481587,0.212704],[-8.315407,6.192868],[-4.975144,-3.319315],[-3.425362,8.608102],[-4.723678,-4.337556],[-0.545924,6.955706],[-8.116205,-7.538252],[-1.335036,-6.012682],[1.361278,-7.477621],[0.639214,-9.872220],[4.146786,7.847618],[6.857840,6.762449],[2.052882,-0.941632],[-9.161290,-4.024232],[-7.222139,-9.832531],[-6.807796,-9.210459],[-2.967452,3.912375],[7.235376,-4.331052],[8.899530,-8.553240],[-6.807814,-8.444073],[6.915535,-9.323147],[-5.996000,-1.657919],[4.291278,2.948785],[7.510051,5.848469],[1.885137,-2.729221],[-8.714748,7.125114],[-6.894586,-4.730209],[4.098907,-1.661906],[-0.682168,-2.224315],[9.613723,4.368035],[-7.389944,-6.642038],[-8.190205,0.584397],[5.325628,-4.283152],[-2.589164,5.186512],[5.859781,-0.964194],[-1.192757,-5.056699],[1.521440,-6.279331],[8.688748,8.651552],[-8.044739,-9.654709],[-5.104041,-1.297650],[2.616915,9.234965],[-2.642816,-8.408342],[2.283809,6.354802],[-5.758889,-5.943485],[-8.888291,-8.779533],[-6.580809,0.845310],[-2.851914,2.561477],[-0.681901,-9.866040],[5.842602,4.720288],[-3.568925,0.374928],[-0.819543,2.415688],[-5.578603,-9.544314],[-8.453477,2.799882],[0.819578,-8.334600],[-8.410737,-9.458110],[6.908781,-9.876115],[-9.889533,6.137351],[4.040108,-6.716055],[4.290963,-4.133380],[8.985297,-0.416137],[-1.016109,-1.698880],[0.738091,9.958894],[6.062105,-9.422780],[-4.373982,5.164898],[-0.038400,0.249872],[9.634489,-0.513372],[8.482401,0.191686],[6.139808,7.429636],[3.491693,7.567423],[-0.193884,-4.465299]], dtype = "float32")#candidate|8442|(1440, 2)|const|float32
call_8441 = func_7362_call(relay.reshape(const_8442.astype('float32'), [16, 12, 15]))
call_8443 = func_7362_call(relay.reshape(const_8442.astype('float32'), [16, 12, 15]))
var_8446 = relay.var("var_8446", dtype = "uint32", shape = (5, 4, 16))#candidate|8446|(5, 4, 16)|var|uint32
bop_8447 = relay.equal(bop_8435.astype('bool'), relay.reshape(var_8446.astype('bool'), relay.shape_of(bop_8435))) # shape=(5, 4, 16)
bop_8453 = relay.maximum(var_8446.astype('int16'), relay.reshape(bop_8435.astype('int16'), relay.shape_of(var_8446))) # shape=(5, 4, 16)
output = relay.Tuple([call_8438,call_8441,const_8442,bop_8447,bop_8453,])
output2 = relay.Tuple([call_8439,call_8443,const_8442,bop_8447,bop_8453,])
func_8458 = relay.Function([var_8434,var_8446,], output)
mod['func_8458'] = func_8458
mod = relay.transform.InferType()(mod)
mutated_mod['func_8458'] = func_8458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8458_call = mutated_mod.get_global_var('func_8458')
var_8460 = relay.var("var_8460", dtype = "uint32", shape = (5, 4, 16))#candidate|8460|(5, 4, 16)|var|uint32
var_8461 = relay.var("var_8461", dtype = "uint32", shape = (5, 4, 16))#candidate|8461|(5, 4, 16)|var|uint32
call_8459 = func_8458_call(var_8460,var_8461,)
output = call_8459
func_8462 = relay.Function([var_8460,var_8461,], output)
mutated_mod['func_8462'] = func_8462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6739_call = mod.get_global_var('func_6739')
func_6741_call = mutated_mod.get_global_var('func_6741')
call_8474 = func_6739_call()
call_8475 = func_6739_call()
const_8479 = relay.const([[[-2.757806,1.884560,-8.996316,-7.940185,-8.120392,9.939461,4.296832,5.609133,-6.955495,-2.477297,7.988336,-6.264753,6.799733,5.542246,0.561299],[-5.972196,-1.819658,7.129913,7.936650,7.697546,9.898351,0.252191,-2.164339,-1.129236,5.027280,-7.951283,0.287853,-4.277635,4.397933,-1.148681],[-3.451720,-4.880481,-5.815120,-4.526678,-4.375658,4.669751,-9.875134,-4.244467,-9.226357,6.310093,1.770046,-2.492196,1.516297,4.991076,-4.397952],[5.292291,-6.757060,2.222341,3.153326,-4.258245,-3.983062,7.290186,6.538032,0.150157,-8.479802,1.048063,1.949146,1.728928,-9.313921,1.409097],[-1.230685,1.073847,9.947250,2.988246,-3.689362,-2.097072,5.031251,-8.566289,3.350449,-9.708069,-4.900073,4.807074,8.924307,-3.813737,-9.394791],[-4.444884,-3.322642,4.274200,2.314167,-4.280427,2.895406,-1.609493,-0.483589,7.943599,-0.917656,-1.933322,0.960222,-2.061795,-9.774119,-7.117113],[2.719540,5.849995,-1.478521,7.852604,2.639685,-2.782092,-4.215051,0.153657,6.372289,-3.582679,0.219938,-6.800461,-1.472012,4.505678,-8.768144],[0.847745,0.693560,2.164950,-6.499819,5.920359,8.264328,-3.023781,-1.065430,-1.503031,-3.215516,9.277030,8.354042,-3.800460,6.762802,-1.260935],[7.585004,5.719291,-2.275101,-7.607712,4.181052,-0.810431,4.724105,-5.102448,2.804233,4.887383,6.663830,4.549826,5.722939,-4.828211,2.925062],[-7.889665,8.084504,0.904357,-1.872611,-7.938173,0.982281,-0.740319,2.566665,-5.619739,-5.190041,-2.400772,3.663208,-8.065272,8.948647,9.896965],[-2.009894,7.688892,6.209192,1.476635,-7.846370,3.928799,5.899571,9.382258,-0.385690,7.551913,5.418680,-2.804283,2.410548,4.962346,8.309854],[4.548317,-7.339098,8.253483,-0.419102,-7.750207,-6.237536,-1.694168,2.401001,-6.630259,-4.496015,-0.677600,7.117526,-0.820228,-3.788862,1.124642]],[[-9.897818,9.812175,5.597940,-4.812639,6.175202,2.483412,-6.133934,8.430739,8.807357,8.157898,8.275157,6.284865,-2.689768,6.239733,-9.378433],[-1.969730,-2.146854,8.086670,1.632726,5.843478,-7.532224,-2.529585,-3.708256,6.981748,-0.632563,7.603822,-0.832907,-8.929002,-4.200668,3.740126],[2.701901,7.124115,5.766296,0.165909,-9.419367,-8.430188,2.033385,2.552083,-2.292648,5.945178,6.990212,8.627548,-3.383068,-8.994275,0.779133],[9.020891,-6.331036,-7.728151,3.287317,-3.976214,-0.497409,7.774516,4.564385,-6.893952,8.556580,-8.125801,-8.644283,-1.000703,-7.298027,-7.243729],[7.249681,-0.291003,-5.862000,8.327554,-7.766884,-9.954429,-2.913493,5.167909,-9.485021,-8.699268,8.532546,1.380996,-5.203152,-1.392671,-3.224252],[-6.408529,-3.529498,6.160865,-3.396966,0.815237,-4.319094,4.754481,5.038732,5.750325,-1.153205,9.275357,-3.519325,-9.811835,-7.158182,0.033866],[0.560184,-6.201404,-9.184391,-8.507750,8.498888,-4.909454,7.788325,-4.664256,-2.593528,6.391198,7.183356,-5.986781,9.693979,-2.791652,-2.877128],[-8.380787,-9.348052,9.423691,0.886783,0.092549,1.453692,-3.089443,8.807662,7.629988,-3.534073,9.627477,1.884974,-9.641323,-3.610894,1.748847],[-6.453761,-6.589260,-9.242905,-2.676084,4.491390,-5.188318,6.312257,-0.208264,-1.339119,-8.203440,-6.349256,-8.020107,7.583586,-3.592234,-6.420287],[-1.624642,5.309045,3.315316,0.849582,9.678249,8.142424,2.736711,3.941089,9.514866,-1.511586,-6.221367,6.933708,-1.897716,5.041433,-4.091866],[-8.350141,1.135952,3.708979,-3.577281,-7.538394,-7.787655,6.311405,-7.452538,6.692308,-5.617278,5.206051,-4.066493,-5.734943,5.493319,6.637744],[3.695778,3.058697,2.123219,3.704910,1.250479,-2.247574,1.039927,3.522895,-0.471459,8.317213,-3.533173,9.962304,-1.968026,-1.076143,-8.605157]],[[2.730622,5.626270,-4.114050,-3.794250,-5.036274,6.119490,1.300452,0.646271,-0.424370,4.726845,-4.644217,-1.347844,-3.355465,2.573207,-6.085020],[-2.758262,9.408722,-1.034631,-1.478855,1.169827,-4.000602,2.959634,5.480488,9.323189,-8.321753,-6.130887,-3.229963,5.874829,5.917730,1.193387],[-3.121560,2.213630,-4.416769,2.243785,-8.502792,9.609390,7.174076,-6.379898,6.596505,-9.979599,-0.819501,0.743244,5.469538,8.594064,5.288390],[-8.850581,-4.088457,-8.172435,-1.466052,-2.566014,-9.628420,0.546325,-5.017849,5.515393,7.228610,-7.123170,-4.830603,3.369617,-0.152188,-8.232298],[6.631694,0.125646,-9.256266,-3.118285,7.792861,-5.089492,3.602300,4.874301,9.770068,6.919849,-9.447038,8.397830,4.833380,-4.562626,9.682146],[-8.665257,4.632487,5.356363,6.644535,-2.069937,-7.644026,-6.446400,5.518452,5.504896,-3.901950,2.211870,-1.182709,6.259287,1.345535,9.129581],[-9.004283,-4.712477,2.592422,-0.032151,9.981879,3.610505,0.027652,9.789352,3.847779,2.387256,-3.137870,-0.846089,8.207599,-9.406290,6.868452],[-4.127775,6.322387,-6.763396,-3.343179,5.554839,7.150121,0.708432,1.729376,7.311218,4.351620,-8.308027,-1.714880,0.309660,8.079226,-4.918245],[4.033226,-4.034551,9.944851,-9.657152,7.241933,-6.367138,-9.964695,4.088202,-5.125657,6.474278,-4.037377,8.366710,-8.340886,-0.485704,1.099966],[6.074037,5.914925,8.416603,-2.589149,-9.788689,-8.648337,-9.024273,-7.705026,-5.837161,4.773880,1.460804,8.708271,-6.561102,8.126235,8.879883],[9.805249,1.306189,1.993843,-4.333523,-7.515379,7.378534,3.340094,-1.973457,-2.607881,-0.196747,-7.570187,2.853742,2.651489,6.451953,-8.338401],[7.730580,1.650193,3.015620,5.970426,-6.314918,-7.122898,-8.027764,-1.142385,-5.737586,5.020861,-1.067127,-6.295166,-8.965836,2.008054,-2.213682]],[[-2.374965,0.334475,-4.880291,-7.742575,-6.475158,-2.867738,4.862708,-0.415243,4.707935,-5.668132,-9.534398,-3.653763,-8.668673,-2.184400,-0.507376],[7.155443,-3.766045,4.430080,8.621167,-7.065286,-5.815348,7.855967,-9.034091,9.478880,-5.449746,-6.686698,-8.740684,0.777381,9.613862,-4.136842],[-5.567322,0.815555,4.907877,0.810797,-9.149628,-4.296312,-5.085022,-1.577467,-0.200920,-9.187813,9.153233,4.490219,0.162349,-1.826752,-5.550724],[0.439000,1.351948,1.857421,5.698516,1.614770,-1.955274,-2.793272,8.449942,2.624314,2.854920,-2.077471,0.883773,-1.287160,-6.633595,3.532155],[-3.536735,2.740111,6.332979,-2.350477,-4.135684,5.497966,3.791572,4.311975,-4.470000,-4.864754,1.956168,1.730223,-3.669271,9.132267,-5.197546],[5.878248,2.631949,-6.732429,1.175229,1.211738,3.643305,2.404797,7.311237,9.451406,1.913144,4.327675,8.341275,1.718229,-2.483244,-0.052209],[-3.624707,0.902225,9.753218,-0.942537,-3.751502,-9.453610,-4.800756,9.032995,-5.052933,-0.964454,-1.191244,-6.386803,-2.356678,-3.725525,9.614254],[7.315402,-2.809350,9.292193,7.140522,4.062496,-8.445520,7.754040,6.895435,-4.473489,4.298457,6.073893,-0.852029,6.475572,-9.904476,3.359979],[0.199110,6.708875,-2.468213,6.508919,-9.753981,9.358723,-1.083161,-0.493438,0.875047,1.175135,5.595032,4.129707,4.190920,-7.031746,-5.567629],[3.223278,-1.434870,4.850777,9.658004,-7.916076,3.011287,-4.041167,-0.787592,9.746914,7.580792,5.739377,-8.519295,-1.735141,7.068578,5.522537],[4.677540,0.414688,7.961289,-0.427312,2.792430,-9.544847,-4.364962,-8.041998,0.664703,1.625067,5.898147,0.806387,7.373010,3.735086,-6.069195],[-3.628898,9.789287,-1.538561,-4.198003,0.445380,0.685446,8.920465,7.687994,6.977650,8.002176,8.316783,5.269038,-8.008907,4.912042,0.850334]],[[-2.034650,6.683561,-6.078559,-4.759713,-7.540703,-1.025750,-7.263117,5.209196,-9.598070,-1.448027,5.717402,-4.730449,5.203267,1.085907,-2.593951],[-6.522589,-3.397068,-0.754825,7.281350,-1.577721,-3.439269,-1.531894,-9.256609,-3.749859,-5.911128,-5.343654,7.325564,-7.163256,-6.236459,1.187625],[-7.686684,8.856939,9.138211,8.944675,1.653628,-6.428338,2.412767,-4.847248,-9.703233,-4.492050,6.187759,8.884568,3.069802,2.291340,2.545573],[-6.222847,7.434286,4.654745,0.897791,1.415849,-6.372716,-7.633629,-1.661119,9.570910,-8.281612,2.157878,-2.712780,-7.417169,-5.489746,8.241872],[-9.494690,-7.460198,-3.934365,-7.436071,-4.929887,-8.675149,6.378338,-3.055936,4.940623,-1.564196,0.388206,5.598399,-5.819112,4.914792,-9.011370],[8.774345,-6.063175,-0.689573,2.591618,-8.236109,-9.241042,-5.949119,-2.579984,-4.627411,-2.711660,6.750983,-5.159648,2.471210,-0.375081,-0.044661],[-0.105219,8.381904,9.820439,2.071809,-7.229977,-5.061234,-7.974050,-7.383775,-9.099323,-1.119126,5.817942,-1.614182,-1.889488,2.529011,8.921930],[9.874896,5.877317,-7.666256,-2.011620,8.405769,-7.982822,-7.664257,-4.122420,9.470341,0.403505,7.320109,9.925002,-8.186656,9.752620,-9.976535],[9.762567,-1.795437,-5.867919,5.406536,-6.611189,5.416967,8.724925,2.800575,-9.189523,-7.792247,-0.297222,-7.859270,8.239454,-3.845442,-9.474419],[2.321111,-7.474639,-1.390864,0.488646,-3.461877,-2.501354,-5.354898,8.039688,6.108772,-1.635805,1.680447,4.379782,-0.925493,-8.833095,-0.844144],[2.683283,9.568693,2.466280,-8.255881,4.691273,6.605243,-8.984170,9.386139,1.823741,2.565553,-7.312754,3.322521,-7.247059,8.462551,-4.145052],[-3.968766,6.475590,6.121174,2.438475,1.401696,-2.356323,0.218898,-5.620655,-2.582614,9.219872,8.159176,-4.977317,-6.092692,-4.206967,-3.419923]],[[7.744892,-1.527859,-9.007668,8.927384,1.634363,-6.086888,4.336385,-7.038278,5.725856,-9.596450,-3.761978,-3.225722,-7.659531,-1.232164,-1.398141],[5.678878,5.903542,2.301757,7.202979,4.681605,2.475465,8.259794,9.351669,2.183821,-7.683661,-2.499115,5.876075,-1.423759,6.285152,9.428983],[0.095024,0.630754,-2.840196,-6.840631,1.801680,3.800567,1.520379,-1.853213,-4.389289,4.924567,5.736673,-3.473360,2.870448,-8.251869,4.881281],[-7.076693,-7.300846,4.975586,-6.928545,-5.376155,2.977964,5.291400,-7.604622,-6.833395,3.420159,-9.310632,8.013474,1.728857,6.276157,1.211007],[7.388363,6.614764,2.654914,0.985896,-3.602329,5.391986,6.721830,-6.281300,-5.785031,-3.824537,8.560895,-0.614718,6.387885,7.112231,4.169572],[5.500708,-2.960057,-2.654957,1.642065,-4.541032,-6.336017,-2.063750,-2.667913,4.306962,7.863417,-4.661225,-1.076026,9.631344,-0.905062,-2.104038],[8.260400,0.540186,-0.299393,8.780888,4.064655,9.605999,8.281156,6.327769,0.011303,1.530107,-5.419769,6.254166,-7.718219,3.729130,9.734305],[3.236256,5.365853,-5.681669,-7.709865,-8.551590,9.488096,0.601202,0.824990,-1.338172,-2.027894,7.247979,2.656153,6.716165,4.072570,2.041276],[0.448202,9.352872,9.708874,-8.944767,6.080320,1.810809,3.740649,5.297813,1.133371,1.660904,2.878378,-2.921796,2.930873,8.375405,-8.692482],[4.496781,2.448177,4.683070,-3.136575,-3.181631,-6.958111,2.305080,5.102691,-7.227688,-7.693018,-5.070831,-5.336083,7.154662,-3.181905,-5.084391],[8.365831,-9.292145,-8.752131,8.566001,-1.793148,-9.424169,6.827962,-9.688752,-0.884042,4.359185,-2.256742,7.327413,-8.733854,-6.342530,1.389827],[-5.032632,-6.239857,3.188643,-0.675796,6.769427,-7.692783,6.598361,5.044577,-0.546465,-9.266151,8.807997,2.282130,7.589556,9.684831,0.545884]],[[-7.841912,8.300136,-8.810102,3.315496,6.638445,3.486329,-7.729814,0.115891,-8.769730,1.713929,6.469377,1.087050,5.297837,-2.975101,-5.362263],[5.581374,2.568791,7.477912,6.034942,-8.619751,-9.880737,0.817306,-9.326664,-5.538708,-4.120616,4.897892,-3.079617,7.606395,1.137292,-1.953152],[3.090324,-9.269489,-3.781176,-1.149127,-0.628016,-8.085630,7.219535,1.096550,-7.065135,-3.062793,-0.513387,-0.580273,0.479336,-7.223557,-2.082113],[-8.551228,4.937940,-5.871083,6.304433,7.550463,-4.722840,-9.463647,5.995500,7.271802,2.352000,1.306171,-2.028062,7.785813,9.093999,-8.238309],[-9.336405,2.378557,-3.426805,-0.910663,-8.039594,0.517417,7.300513,-1.053383,-1.482562,8.580727,-9.079432,0.795648,-1.757884,-4.424127,-2.020810],[6.731820,1.487381,-0.567106,8.513638,2.801798,8.435480,-2.760206,-2.449047,8.928059,-2.576128,8.030373,7.016028,9.955980,9.397119,3.376873],[5.220397,-3.493520,7.589234,-3.744494,6.614268,6.480884,-6.128909,-7.421855,-2.116470,6.626181,-2.819862,0.148455,8.029717,4.372695,-3.689305],[2.326430,-5.730611,8.322879,-1.830305,-9.291598,7.297726,-7.881422,6.666554,4.688331,3.552211,-3.617024,5.776600,3.156138,1.456444,5.773926],[-0.139671,5.208237,-1.956820,-1.883727,-8.331582,5.101786,-1.176337,4.554834,-6.110020,-6.546688,-2.583879,3.194795,-6.121140,-2.221903,5.142690],[-5.785501,-2.280214,-5.053115,-3.361235,-7.511366,2.142108,-5.416747,0.238720,6.887304,-4.935869,7.779977,3.307565,-5.791676,-9.706040,8.441534],[-8.278325,1.251226,9.717183,-3.985181,-2.938801,-6.827068,-3.174022,-4.364954,-9.243206,7.576501,1.943604,3.904447,2.462757,-4.476446,8.731315],[0.343793,5.297020,-9.906122,1.174986,-0.917229,8.793429,3.663229,-8.468531,-2.486339,-5.000748,9.050382,-8.061301,-8.197035,3.896680,6.282874]],[[-8.319840,-9.430595,5.646102,-4.603465,3.869527,7.134889,0.720855,-8.868599,-4.928096,-4.605289,-0.357583,-8.167592,2.322062,-0.635052,2.746637],[8.047616,3.718079,-4.743995,-5.088549,1.888206,9.974133,4.340919,8.134252,-5.569674,-1.434556,-0.833815,1.905482,3.376110,5.707198,3.007916],[-8.807267,-9.482527,-0.524542,-5.325435,8.902925,3.648403,-4.654488,3.828877,-5.497922,3.435395,7.135812,-8.277616,-2.097080,7.811994,5.836863],[4.204672,1.969362,0.954483,-2.271748,-6.445740,3.081472,-4.390352,-3.543771,-8.355455,-9.619751,0.595600,9.407945,-8.611837,-3.495989,-3.019248],[-3.895531,9.630256,4.213869,2.787976,-0.027671,-5.185428,1.357720,-2.082069,-6.222474,5.522978,-3.058886,-7.392096,-6.853442,-2.542369,-9.185043],[-7.418149,-7.467867,-3.354339,1.085460,1.876399,-5.350617,3.884334,-1.400182,4.674899,-5.992137,3.541664,-2.055470,6.072761,-4.797602,6.839425],[-3.982210,7.684766,1.384575,-8.007264,-6.690656,-0.593238,5.570891,-3.441631,1.034021,1.596851,-5.769781,7.265589,-7.107554,7.986330,-2.329192],[-0.289514,6.589105,8.169559,3.625441,1.382162,1.733005,-4.381713,2.950425,-7.728813,1.140663,2.398825,8.802298,-7.650200,4.030541,-9.102706],[-5.251421,-8.457960,9.229111,-2.586270,5.793308,-7.113458,3.853972,-5.086236,8.188518,-0.047371,-1.236822,9.587722,-0.831214,1.987679,1.968275],[0.708735,-5.400812,1.545001,7.589996,5.296596,6.632904,7.083716,-9.543088,-0.411628,-6.427479,-6.126329,-1.073868,-7.752810,1.220057,-8.001960],[-0.683760,-1.226226,5.418884,-3.672146,0.525884,8.736725,8.997313,-4.629790,-7.241307,9.403535,5.883851,5.327663,2.273388,-7.938634,-1.745163],[-1.220508,-8.577864,9.585608,-9.347783,-7.292868,0.227231,6.423307,-7.748673,7.033084,-8.898193,7.002983,-5.809814,5.112413,5.033616,4.359038]],[[-0.992672,-3.196984,-5.719087,-1.776500,0.132290,6.915350,-6.199272,1.564128,-8.853457,-0.376040,2.716191,-0.757271,-3.468296,-9.265239,2.586502],[0.425437,2.131923,-1.776023,-3.856812,-4.019871,6.299839,-2.005786,-6.900917,-5.501950,-2.710485,7.068740,-4.689065,-3.459987,7.461884,-6.796649],[-5.204965,-0.583734,3.436464,6.451871,2.664801,7.039520,7.483072,1.677666,6.614283,-5.297174,-7.874439,-1.152801,4.687668,7.630218,8.591733],[5.655604,-3.389236,4.772474,-7.054501,5.026854,-5.089696,-0.119745,-8.087610,-7.943659,8.766224,-9.971149,-9.137475,9.779123,9.498091,0.726814],[-3.151734,-0.834102,-1.583114,2.435328,-1.257466,1.217345,6.873008,6.759712,6.654806,-7.502491,-3.678414,-7.933930,5.365861,6.341516,-7.959615],[7.466800,7.777694,8.413298,0.713714,0.585574,5.657350,-3.690470,-4.780316,2.324986,1.667157,3.028147,-3.527178,9.554680,7.219350,-6.556600],[1.022500,-1.979489,3.851932,-0.836659,-8.493124,-4.331147,-6.374983,5.087205,-9.504730,-8.028486,-0.205463,-1.907732,2.722001,-5.166327,-6.666641],[1.422460,-0.311923,-0.264053,3.583772,-3.269799,-7.786554,-3.516018,6.223773,-8.919260,-0.517978,-8.913459,-3.555687,1.447649,-2.127674,-5.031283],[-6.834814,-0.101003,6.584196,-0.409707,0.600409,6.335419,9.728123,3.030203,8.155051,0.409240,-3.266454,-4.476294,-8.448070,7.816145,7.917777],[0.647244,1.197818,-4.451232,-6.920996,7.124409,0.405367,-7.912460,-2.913387,0.966052,0.903640,2.718072,-1.491849,-7.562880,1.984708,1.444167],[8.345163,-1.857895,-2.355644,5.576342,6.052917,3.123972,2.976397,-0.795491,9.579502,9.231535,-6.702109,-3.682168,-9.390353,2.105948,-9.935741],[-0.059936,2.220300,-9.234160,2.115703,-2.139708,2.954962,0.126582,7.460758,-0.286701,-2.415886,9.941236,9.771431,9.490757,-8.832356,3.715124]],[[-1.547041,-7.501061,7.186511,1.131212,6.222198,3.098841,2.443953,0.542026,-0.833826,7.990393,-8.677517,8.644538,2.895394,3.909001,9.379414],[-6.734595,7.562085,5.227750,-0.948016,0.253077,2.925312,-0.703721,-4.620823,6.659682,1.675230,1.658733,-7.242599,3.242534,8.475809,2.880063],[-0.683750,-1.226000,4.883935,-4.078968,3.228326,8.561194,-3.634763,5.865147,8.703927,-3.247574,-2.118805,-3.441172,-1.198672,-1.037996,8.990304],[5.956974,0.883515,7.376080,2.353166,-1.729143,0.268741,2.923947,9.686720,-9.869470,-3.734269,-1.315930,-8.283161,6.888492,-4.101891,2.632833],[6.707531,2.792522,-3.592271,6.725848,-3.464482,-1.433834,0.352151,-9.505647,5.296174,-1.257852,7.636008,-8.398300,7.496074,-4.652989,0.821867],[0.298908,-8.353808,6.012516,6.717648,5.856839,5.884242,-3.981116,9.935684,8.251017,9.979491,-7.934053,-3.247636,1.784399,-3.448478,-0.914955],[7.859999,6.309159,-7.903355,-3.644558,0.192542,-5.999714,-5.753058,-1.291205,5.862721,-4.271214,3.823024,8.545446,8.253863,2.553316,-4.924800],[2.402593,-2.490569,-4.607549,3.170488,-5.675513,-1.578152,9.263172,1.526553,-6.966826,-0.494481,-6.837334,-2.261417,3.722609,-9.752642,7.297190],[-1.448313,-2.774898,3.319884,-4.587064,2.688944,-7.093875,0.962079,-2.134373,0.405815,5.254948,0.045997,2.033215,5.956462,3.628492,7.055606],[-8.765497,9.920885,-1.137935,7.524889,-5.700508,-9.513727,-5.333697,-2.270484,-3.015971,-6.277908,6.145722,4.211429,0.092569,-5.596381,-9.092285],[9.192312,4.241719,2.359397,-1.587880,-6.630013,-1.951051,1.423814,-6.757810,2.886255,0.224011,-0.412516,-4.956150,5.469167,-0.868332,-0.445665],[8.192841,-6.816922,8.303772,8.000080,-3.167552,-6.960517,-0.956726,-2.096868,2.402176,7.832369,5.561386,-0.932836,-8.241459,3.568343,9.222600]],[[3.858714,2.091857,2.753843,-6.438395,-1.359979,5.160371,1.037946,-0.495115,-3.195328,7.109016,-2.111289,-2.815331,-3.062672,-2.847321,8.074363],[-7.633558,4.502254,-8.382053,-4.941729,9.370160,-2.454635,1.460711,-0.037869,7.994724,5.654272,-6.661536,6.303032,-3.670142,0.067440,3.467128],[-1.453621,-2.566623,4.872482,6.881133,9.188450,3.443370,5.854843,4.449653,-9.687959,-7.427102,9.298594,-3.411834,1.896825,4.245755,8.673255],[-7.269008,-5.451844,1.751982,3.416766,8.518814,6.646051,-0.799088,5.981677,-2.529453,-0.443117,3.727521,-1.357772,-3.296867,3.049495,-4.109505],[-4.695301,-8.357932,3.566666,9.614827,-2.048216,7.478370,2.031405,-4.039188,9.138196,-7.975563,-4.507636,-1.971670,7.859450,-0.451373,-9.446998],[-9.438117,8.692292,7.802020,-6.317310,-9.814170,1.694640,4.692921,5.745957,5.232996,-4.649213,4.710022,3.516988,8.440937,-6.038999,8.255559],[5.015124,-9.656889,5.372398,0.339664,-1.175490,-8.013118,-2.316678,-6.460668,-1.101028,-4.513904,5.639951,3.479819,4.069213,-3.943207,-7.884700],[-9.909519,1.875788,3.513038,-7.626605,-4.264335,-6.752130,-6.334999,-4.189961,-6.700325,-9.935384,-7.007954,-1.403891,7.488235,-8.304313,-2.104056],[4.699686,-0.295495,3.401732,4.221832,0.669088,-8.402610,4.836190,-2.013873,9.504768,-6.780123,4.405636,9.251487,-1.565171,-2.745326,-3.438453],[5.176163,8.428246,-3.751266,1.243148,5.016598,-5.816642,-2.843126,-0.610272,2.467338,-4.362572,-2.296096,-8.180564,2.229423,-5.095846,-5.473437],[-4.482940,-2.733717,7.437033,-2.222178,9.348497,6.502968,4.092249,9.825665,-0.402494,3.008196,-1.908102,5.673755,-9.593181,5.436348,-7.777192],[6.077551,9.368857,-7.639053,2.698410,-2.632518,-9.199630,-4.012183,9.311757,-3.607986,-7.796126,-7.841420,8.892328,-3.411162,8.262204,-6.257039]],[[8.553534,-8.213098,4.172836,2.200349,-9.537724,9.977040,-0.549872,-4.912840,2.881620,6.989069,0.354752,-7.428298,8.024901,-1.133888,-4.980191],[-9.418762,-8.546326,9.704481,-0.881146,-0.448160,-4.152510,2.854715,8.771020,-3.616424,-0.319382,0.305791,-0.999165,-7.391551,-4.596810,-6.606940],[7.837388,-2.942734,2.181550,-1.841577,-3.039378,-2.444670,-4.381047,3.030953,-7.596733,0.894784,-0.809544,-6.927505,-7.085750,-3.588077,7.643937],[-6.601892,-3.977822,-0.537547,-3.233399,5.198478,-7.223282,2.208741,3.719890,-2.585292,-2.730334,5.942943,-5.944793,7.803875,-4.226267,8.591384],[-0.762844,7.564704,-8.647147,9.920696,-9.810721,-6.935374,-1.185224,7.752929,-2.893951,4.734925,2.124604,0.272517,-3.902610,4.367316,8.685709],[-2.021760,-4.802090,-5.007788,-8.162609,7.499931,-9.503718,9.287558,8.089190,-6.015058,-8.963078,-8.047244,-6.436456,-2.914189,8.614892,-9.796662],[-4.382046,-7.417271,-2.565710,-6.935380,-3.000255,8.851995,9.270730,-2.110242,3.828340,-3.259166,-2.115813,-2.872907,5.353736,-4.583965,-6.355692],[7.571207,4.646561,6.520809,-1.884433,-8.360001,7.910409,3.702819,-7.211369,3.570914,-8.021598,-7.518621,-7.961832,-3.661764,6.710190,-7.694739],[1.159375,-9.870178,-1.164757,-8.680249,1.447814,7.273659,-6.286736,5.618764,-4.638884,-2.120770,3.051662,-4.532278,4.075172,5.070147,5.643552],[-2.546409,1.600700,3.315522,-2.422589,-6.253092,6.547884,-4.566791,-4.885929,-9.569665,-8.556638,5.835816,3.840021,-9.517417,-5.225240,9.970603],[3.838144,-1.067805,0.713579,-3.926004,5.012080,1.782275,1.652241,-8.569578,-0.285343,-7.025195,-9.039306,-2.127578,3.195863,-6.598674,-3.619246],[5.611421,-9.376082,-6.249498,-3.175159,6.509524,7.095149,-6.818206,7.527636,-2.773690,0.472885,-8.572358,-6.161797,-7.333702,5.246937,-9.876187]],[[-7.359669,-2.330253,0.921433,-5.841695,8.149014,-9.865018,3.191622,8.042953,7.305288,-0.675196,8.876266,-5.517737,3.740159,6.228575,-1.485483],[-9.063685,-6.993487,0.886026,0.346032,9.242629,6.161560,4.148044,-1.474046,6.405457,-7.343810,-2.400339,6.513576,9.478404,6.794081,6.041015],[-0.270377,0.905058,-4.174717,1.464553,-4.352069,7.330636,-2.996894,-6.853151,5.466453,-7.855346,2.479667,5.977029,-6.646861,4.422005,-7.886574],[2.029223,-5.225577,9.749917,3.579648,-3.109090,6.819125,7.278800,-2.603206,-0.424768,-1.653639,7.747983,7.353765,-3.071713,-0.310636,-6.076487],[-6.235087,5.467749,-6.947525,-9.274558,4.818803,3.969326,-9.066931,-6.830048,3.444723,-9.032756,-2.786546,8.868064,0.212862,7.129056,-3.655277],[-3.291075,7.913105,8.499815,-5.089929,1.973672,0.177634,-2.845314,1.473959,-3.630244,4.496377,-1.049659,3.695813,0.977347,6.898072,-7.549362],[-0.337548,9.904922,-9.963657,4.696710,-6.285920,5.326945,-2.163061,5.836849,-3.762972,-8.947497,-9.682188,9.530755,-6.000061,-8.672300,2.320173],[8.288679,1.559026,4.472903,-1.567049,-4.652007,3.482838,-0.257596,5.209025,-7.871547,0.053060,5.681058,0.351144,8.851431,-6.002401,-9.270698],[-2.575987,1.621141,-9.111466,-0.849583,-6.648610,5.676956,-7.875537,6.294920,7.885015,5.730933,-5.690973,-5.813014,-3.148937,4.684748,-6.749612],[-2.591047,-5.770556,-0.699334,2.668005,1.930298,-6.768037,3.801561,-0.633885,-8.875687,-0.855176,-2.325352,6.512604,9.391848,0.826760,-2.356377],[-1.014889,-9.206858,-2.603276,7.616603,5.164064,9.226161,7.852793,-5.867228,0.942725,9.234653,6.294641,-1.175125,-6.034903,-3.769314,8.328395],[6.148490,2.450237,-1.584032,9.908607,2.292255,-6.235892,-7.025478,-6.818045,4.407878,4.704035,9.627082,-5.673743,6.397696,4.455956,-7.657685]],[[-4.642216,-7.470770,-9.572730,-6.018826,-1.239917,-6.920115,-5.051001,-1.044074,-5.845071,6.497069,-1.798001,-2.278750,-0.971594,-7.571566,4.792061],[-1.705080,-4.433049,1.373848,7.729461,-1.548485,-2.583114,-9.152130,9.974388,6.492483,-8.637683,-4.370238,8.986522,-2.299167,-4.030629,-9.498797],[1.845892,-9.146984,3.638888,-7.461071,5.298440,9.174836,-4.086372,-1.645385,-3.046732,7.093640,-7.130128,-6.785386,-1.732026,-5.814643,4.335677],[-7.432176,7.678708,-5.684867,-7.511454,-0.636459,-6.285972,9.258944,1.983182,-8.759326,4.925631,1.653352,6.591206,-3.302069,-9.888612,9.133178],[1.427173,-7.724113,-7.146653,4.537819,-3.244609,-6.790664,5.329929,6.382733,4.828281,1.049345,7.611291,3.570550,-7.846875,-3.242183,-0.273885],[-9.971774,9.788707,-4.001482,3.459793,-5.738141,7.908724,-9.633824,0.420149,-9.967389,-1.485228,7.155737,-4.520316,-0.457500,-2.277033,8.365253],[-2.731293,-2.307471,-2.316494,7.317189,2.271238,3.110873,-4.322266,8.375627,3.350862,0.114905,8.530827,7.382028,1.285814,-5.769798,-5.574897],[-5.171887,1.656708,-6.442490,1.074699,-5.678108,-6.537712,-5.153382,8.009365,-2.780040,0.779818,-4.263595,-4.231094,-5.671451,-6.009904,-1.978166],[-8.902959,5.781330,3.022875,1.024945,-2.284167,5.803231,-7.001236,9.087674,-4.706425,-4.855377,9.361683,-0.091163,7.931102,6.917571,-7.788535],[-8.594627,-9.785660,-5.594628,-8.700767,4.062740,5.771498,7.289074,-5.159464,-8.723790,-8.124773,-8.989294,2.224914,5.779240,1.886280,-1.704303],[-7.306809,-3.029565,0.724134,5.194873,-4.104483,-5.635962,6.134303,1.812721,-2.387628,-7.510684,3.585959,8.321439,-6.295614,6.299657,0.626861],[0.754016,-8.090521,7.755645,-2.542885,4.383007,3.659961,9.191420,7.080427,-9.040261,-7.641140,-7.946324,6.308584,-4.857316,9.583201,8.550075]],[[-5.230358,-1.583895,-5.130043,-3.631913,-2.349587,4.479329,6.254464,7.995822,-8.490218,-7.714426,-7.385318,-7.005602,-1.454839,7.413775,-3.313124],[3.914443,3.624506,8.790611,6.106889,0.326829,-8.195413,6.494021,0.268319,-4.830654,-4.900414,-5.467147,-5.492784,-7.450621,8.493270,-8.315938],[-9.690020,-6.578713,6.524370,3.183148,7.362012,0.014939,1.783455,1.275985,4.090900,-6.782609,7.000172,-4.553490,4.514783,-3.219728,0.410183],[-5.108871,-4.417413,0.551485,0.999706,-8.383585,0.100568,-5.662252,-6.928757,2.280091,1.906830,2.476429,-4.121040,-6.720908,-3.895722,0.297688],[1.765548,4.027056,-7.655405,-3.454217,4.025414,9.867914,-3.763767,-7.696590,4.123308,-4.146145,3.744960,6.927637,6.527303,-5.630515,7.413113],[5.115095,1.820880,-1.075394,-2.011517,2.861351,-8.938288,-5.270980,-4.626191,6.223504,7.605241,6.557997,-8.811399,-3.833077,-2.924439,2.909833],[-1.606633,6.986520,-3.913355,-1.418466,-9.848944,-8.739797,-1.305573,3.488349,6.261816,-3.798067,-4.319749,-0.161474,3.216686,-9.917958,4.859925],[3.642627,7.572608,4.944442,-8.147412,-0.557291,-2.501946,9.655217,4.171940,0.865713,-1.557946,5.225386,5.789277,0.276465,6.030075,5.556453],[3.418056,-3.422417,0.450480,-6.616973,4.785010,-4.149594,-8.995252,-0.892225,-4.103823,-0.028121,-2.997774,9.911616,7.978502,-7.370838,-3.846834],[7.155004,-5.913333,-7.266944,-9.463913,6.336421,2.485386,3.420354,-8.235523,-9.420888,0.822151,5.243398,-5.565310,-8.877185,2.957582,-0.229555],[-7.510146,6.347516,-6.426404,-4.339979,9.550288,-4.885998,6.967197,-1.971674,-4.362916,-2.680935,1.832985,4.484417,-6.530957,-2.007301,-6.199221],[9.514384,-2.948569,8.931926,9.832083,9.713838,8.336247,0.801019,3.104951,-2.060536,-6.740154,-3.238192,-8.062490,-7.690525,6.140801,-7.942541]]], dtype = "float32")#candidate|8479|(15, 12, 15)|const|float32
bop_8480 = relay.subtract(call_8474.astype('int32'), relay.reshape(const_8479.astype('int32'), relay.shape_of(call_8474))) # shape=(15, 12, 15)
bop_8483 = relay.subtract(call_8475.astype('int32'), relay.reshape(const_8479.astype('int32'), relay.shape_of(call_8475))) # shape=(15, 12, 15)
func_5164_call = mod.get_global_var('func_5164')
func_5166_call = mutated_mod.get_global_var('func_5166')
call_8492 = relay.TupleGetItem(func_5164_call(), 0)
call_8493 = relay.TupleGetItem(func_5166_call(), 0)
output = relay.Tuple([bop_8480,call_8492,])
output2 = relay.Tuple([bop_8483,call_8493,])
func_8505 = relay.Function([], output)
mod['func_8505'] = func_8505
mod = relay.transform.InferType()(mod)
mutated_mod['func_8505'] = func_8505
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8505_call = mutated_mod.get_global_var('func_8505')
call_8506 = func_8505_call()
output = call_8506
func_8507 = relay.Function([], output)
mutated_mod['func_8507'] = func_8507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5736_call = mod.get_global_var('func_5736')
func_5737_call = mutated_mod.get_global_var('func_5737')
call_8580 = relay.TupleGetItem(func_5736_call(), 0)
call_8581 = relay.TupleGetItem(func_5737_call(), 0)
func_5699_call = mod.get_global_var('func_5699')
func_5702_call = mutated_mod.get_global_var('func_5702')
const_8583 = relay.const([-10,6,9,-5,-5,7,-1,3,1,4,10,6,1,7,9,2,8,-3,5,-9,4,-10,-7,8,5,-7,-3,-4,10,8,-7,9,2,2,1,-10], dtype = "int64")#candidate|8583|(36,)|const|int64
call_8582 = relay.TupleGetItem(func_5699_call(relay.reshape(const_8583.astype('int64'), [9, 4])), 6)
call_8584 = relay.TupleGetItem(func_5702_call(relay.reshape(const_8583.astype('int64'), [9, 4])), 6)
var_8606 = relay.var("var_8606", dtype = "float64", shape = (4, 2145))#candidate|8606|(4, 2145)|var|float64
bop_8607 = relay.not_equal(call_8582.astype('bool'), var_8606.astype('bool')) # shape=(4, 2145)
bop_8610 = relay.not_equal(call_8584.astype('bool'), var_8606.astype('bool')) # shape=(4, 2145)
uop_8625 = relay.erf(var_8606.astype('float64')) # shape=(4, 2145)
uop_8627 = relay.acosh(uop_8625.astype('float32')) # shape=(4, 2145)
output = relay.Tuple([call_8580,const_8583,bop_8607,uop_8627,])
output2 = relay.Tuple([call_8581,const_8583,bop_8610,uop_8627,])
func_8630 = relay.Function([var_8606,], output)
mod['func_8630'] = func_8630
mod = relay.transform.InferType()(mod)
var_8631 = relay.var("var_8631", dtype = "float64", shape = (4, 2145))#candidate|8631|(4, 2145)|var|float64
output = func_8630(var_8631)
func_8632 = relay.Function([var_8631], output)
mutated_mod['func_8632'] = func_8632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8051_call = mod.get_global_var('func_8051')
func_8052_call = mutated_mod.get_global_var('func_8052')
call_8634 = relay.TupleGetItem(func_8051_call(), 0)
call_8635 = relay.TupleGetItem(func_8052_call(), 0)
const_8636 = relay.const([[[-9.474305,-8.391410,3.605870,-5.205602,4.326085,7.973729,-5.930155,4.526012,-3.064853,-2.224835,-9.822601,-2.750639,-3.650932,6.543092,-1.168037],[6.535619,9.316125,-9.812870,-9.668919,-9.106824,5.222060,-1.591248,7.922791,5.925414,-3.056490,-9.414365,-3.903157,2.331309,-0.190371,4.409325],[0.786765,-8.447203,-5.923744,7.632329,7.335544,-1.799074,2.404026,-8.953017,-8.895700,-1.791807,8.761254,8.188257,0.216018,4.039286,-5.209713],[-8.749001,4.681514,-2.178657,3.416637,-6.238432,7.299907,-7.654087,-3.218742,5.390586,-7.845059,6.809550,8.249163,3.242525,-7.521353,-9.682879],[-0.161956,-8.910033,6.659174,6.068547,2.479752,-1.356016,9.433062,0.056246,1.225654,-5.362951,9.822096,-1.444503,5.762729,1.310141,-5.123885],[-7.025494,4.205733,-4.405543,7.976768,4.167341,-9.877625,1.896403,-7.569437,5.964813,0.543203,-7.279183,9.795251,6.135558,-3.826666,-4.780851],[2.892627,7.089705,-0.806851,4.721955,-4.661801,-2.358269,-1.643159,-3.132790,-4.223973,5.168903,2.118630,-9.828682,-5.249756,0.868908,8.700444],[0.517986,-3.652253,8.445313,-9.944584,-8.897586,2.378163,5.700440,-8.891391,1.978954,7.490882,6.652991,-6.847146,-2.982587,0.776810,1.093500],[9.725097,3.249660,-8.620758,-7.158396,-1.958971,5.489711,1.120498,7.095664,-2.644630,7.386325,8.498085,-4.772411,-3.379618,-6.098825,7.266775],[-9.806272,-3.497964,-9.803461,-0.854983,-4.274164,-3.575472,0.593944,-0.020023,7.413722,9.187341,9.278428,9.673294,-7.059446,-7.126637,-8.227572],[-8.567390,-9.571853,-0.219959,9.471480,-4.005487,0.336320,3.361722,-8.863084,-2.935737,-7.474820,-9.749823,-3.642053,-9.411352,-0.555961,-0.214057],[-6.697411,9.168573,0.025952,1.956547,9.588827,-2.843082,-7.197742,2.429037,-0.118578,9.007947,2.315877,-5.477506,6.849647,-4.299275,6.408224]],[[-5.301372,5.934781,-6.181959,-3.423594,-9.076938,0.064692,-5.360291,-0.629981,1.761646,2.179387,-8.147589,-6.354284,7.962687,7.183221,3.673762],[-8.156223,-5.091259,-7.428468,-2.725417,-8.971041,-2.993604,-6.115033,-6.483037,-5.315885,2.406164,-3.050048,-5.472828,-1.115023,-4.254958,7.963217],[-0.048098,-2.397433,5.081082,7.781294,1.205027,-7.871926,-3.799667,-2.392552,-3.236561,-3.232700,4.533992,1.985463,2.436462,6.581790,1.473258],[-8.891327,-7.808231,-2.359754,8.220147,4.495785,2.454069,-4.286366,-9.208247,-9.973278,3.814067,-2.575944,5.573615,-1.986113,7.178080,5.469410],[-6.333830,-4.231388,-5.861725,-2.018018,8.248298,-2.961034,-6.352205,-7.582705,9.118469,0.177733,8.597242,9.129812,0.536474,7.308897,3.190799],[9.858909,-9.169287,-1.080301,-2.486838,-6.753599,5.142375,-9.370672,1.117314,-7.043979,-1.174312,0.425094,-8.893422,-2.940312,-1.948006,-9.818242],[-5.786393,0.096713,-6.147009,8.462971,9.315743,-4.998908,-0.306626,-0.326853,1.535212,6.964985,-7.860906,4.145429,2.064797,-6.454561,4.451001],[-1.060602,-3.859016,4.248119,1.335822,1.402368,-2.384356,8.995732,-0.702996,5.735846,1.294503,5.089111,3.107692,-5.890273,5.372629,9.186950],[5.075403,-5.839801,3.789163,-2.164397,0.014774,9.698479,1.232983,-4.927344,-0.040186,6.568921,-1.151650,7.140224,0.291819,8.375844,-3.494717],[-1.578765,-0.789495,3.682618,-5.002376,-8.098129,1.604429,9.166917,3.092886,4.739152,6.940240,2.920361,2.221688,-7.264530,-7.189846,7.114110],[-9.692250,-0.933433,9.033417,-0.819423,-3.681286,3.725203,6.498404,-4.128232,-5.347762,-6.122895,1.243861,-3.403327,7.781733,3.752055,-2.314172],[-4.103715,-1.428635,3.661977,8.698293,1.891850,-7.538686,8.818810,-0.466731,-6.916187,9.493956,-4.308695,-0.409196,-1.869443,3.965072,9.992471]],[[-9.505547,-8.836902,5.433282,-2.717700,-6.336333,-0.069298,-0.457171,-2.313540,1.841046,-0.432500,2.482494,5.720562,0.001013,3.572122,-5.058706],[-1.497286,7.683004,3.033070,-3.060207,7.200050,-2.478051,2.150248,4.165152,6.853061,0.814601,-3.670111,-4.283069,-8.083813,2.745943,3.716939],[2.961604,-0.903663,-7.223971,8.082239,-9.321643,7.691541,-3.573917,3.057427,-4.500436,-6.626364,-3.819787,1.126030,0.528644,-4.750073,6.313429],[-7.451413,7.677737,6.852971,-1.088585,-9.152077,1.737936,9.593112,1.050918,-1.506643,4.560202,8.364202,1.206207,0.802436,-5.122739,4.189327],[9.306340,-0.401789,-2.804825,-4.562212,-0.089587,2.431977,4.024832,9.560779,-0.909885,-4.684171,5.263782,6.635155,-9.812447,7.109081,5.902667],[2.026405,-1.972103,7.876508,5.193967,8.538169,8.446377,-8.622657,-0.334122,9.625834,7.666432,-9.630687,4.387664,6.266482,-5.745807,-8.154817],[2.481966,-0.096165,-8.816335,-6.777833,-1.137167,7.670632,6.162493,-2.102315,-3.851886,-1.559725,0.585875,-8.470642,-8.705397,8.850171,-1.826776],[-3.214602,2.438011,9.732453,2.843598,6.942013,0.318277,4.583241,-1.365332,-4.076913,5.510845,-1.701788,-1.647494,3.870778,-7.213278,3.066090],[-1.412352,-9.327947,8.228013,8.116356,-8.808382,-1.101225,-7.056812,-1.301551,2.855654,3.622225,0.973802,2.185797,-1.094347,-5.329335,3.033308],[5.119730,-8.767359,6.123846,5.602749,-2.869221,-5.452650,0.077517,-1.149648,2.133603,4.579812,-2.580586,8.032669,-5.316004,-4.288610,-9.421711],[-6.819046,6.876376,-4.778019,-9.550658,-1.379060,2.660314,5.017073,4.530786,-8.874844,0.198749,9.329128,-1.934511,-7.041415,-4.632314,8.227277],[-7.501642,-9.740723,-9.920653,1.601668,-3.020356,8.193866,-0.633024,-3.286687,-0.168240,-2.764798,-5.969098,4.200095,-4.557463,7.992561,-2.766008]],[[-3.869702,1.868994,5.057989,0.667894,-3.924993,-6.053794,7.818950,1.787207,-4.311704,-6.448673,3.950548,-0.736370,3.944493,-4.958066,0.606620],[9.548122,-3.494456,-8.638966,6.107264,-0.367722,4.537555,2.849914,0.020971,-4.985003,5.734416,-2.695868,-4.107604,1.198137,-9.468730,-0.769951],[1.464975,9.360241,-8.060657,4.580207,2.855010,-5.342486,-1.145626,0.359432,-1.695974,7.463839,-0.207521,-8.970814,-8.850454,-2.047694,-5.243203],[-8.928018,-1.101254,0.480792,0.175465,-1.444511,-1.605178,4.210101,1.928938,-3.214646,-0.727645,0.010150,2.027561,3.189006,7.479766,-4.623564],[2.523583,5.762893,-4.106971,-3.447609,6.582732,-7.004331,4.516881,-7.658272,-7.825021,-6.703966,-2.658279,0.499994,-6.392004,9.982669,-7.573605],[8.333944,-6.507025,-3.531934,9.593620,-4.238471,4.665890,-9.713670,-0.741060,8.497670,9.709501,-7.104896,9.978418,0.786389,-9.589434,-7.785248],[9.407769,-6.904236,-9.449052,-6.020123,-0.885366,8.001534,-1.848899,-4.639890,-8.464827,4.861845,-1.659974,-1.687588,-0.390618,7.857054,-2.730443],[4.491940,8.759668,-6.393667,-2.875973,3.654374,3.605044,8.395724,-6.816297,3.299256,8.956912,-0.081701,-1.562643,-7.758970,-8.774450,8.166098],[1.759719,-2.399873,3.109144,-5.878862,-0.652392,-9.403322,-1.086639,0.836142,0.738242,-0.415762,0.458623,-8.837961,2.815656,-2.312142,-7.666506],[-6.644017,2.584863,-2.359652,8.932270,-8.055523,-9.510038,-1.007254,-3.846545,1.871121,-6.592828,0.579769,-2.287129,5.232101,-5.474955,-1.384156],[1.289250,-3.105684,1.810363,0.009843,0.595256,-3.612885,-7.761941,5.422861,-7.914666,1.707708,-7.667620,5.903017,-7.216942,-2.813074,-6.225073],[-2.759043,0.228950,-6.864572,0.119911,-6.593245,-4.866493,5.656233,1.936535,2.728924,5.485052,-3.653487,5.719146,2.943505,-3.835003,-2.700710]],[[-8.834279,-0.946878,6.729118,-4.392503,4.649756,-5.393933,-4.481176,-0.674146,-4.792619,3.123584,-4.190151,1.305007,6.713226,-1.246859,-4.411487],[1.854376,5.345268,-4.668215,-9.916843,6.991739,4.094710,6.357181,8.126020,2.466712,-5.603190,-5.953543,-0.818906,-2.969374,-1.605001,1.704565],[-3.789590,6.011917,6.389919,-7.553550,-3.022098,4.400319,1.576187,4.767434,-6.057917,-7.149566,-7.805924,-1.075139,-7.026281,-5.956779,3.071184],[2.420415,-1.786776,8.715530,1.250908,-4.642575,4.875059,5.303417,-4.291604,-2.672816,-9.333172,2.655515,0.671745,1.099645,1.005039,-1.642898],[-1.468624,-3.304710,-5.496224,-7.644835,5.887964,7.811421,-8.380605,-6.367067,-2.063913,1.580753,8.533763,3.220555,-5.592841,9.969510,-3.580102],[-2.489031,4.881471,-5.097542,-8.982091,2.225251,6.481706,0.090513,-6.475901,-5.400488,-5.076303,8.896327,1.660264,-6.120682,8.703238,1.843307],[1.530024,-1.145510,-5.821303,-4.622803,6.429695,-6.717261,-6.365562,-8.167897,9.902687,8.813251,3.831717,-4.272308,7.810573,-9.113741,-7.546148],[0.497699,-1.674786,-1.474885,-9.169260,1.224767,4.011515,-2.485119,2.572137,-3.550565,3.216209,-8.871788,-7.576811,2.498307,6.902654,-5.155773],[9.092494,8.410027,-0.103644,-3.703000,-9.882714,-9.245297,-5.487346,-2.257279,-5.399010,-9.571109,-2.947346,-3.121667,9.840125,9.106965,4.830440],[-5.442621,9.282953,-2.994840,-7.808583,-8.537252,7.459994,-7.251130,4.306169,1.688655,7.894847,7.758138,8.663394,-5.098106,-7.876068,7.020979],[4.184160,-4.599765,-9.450540,-2.550800,-1.860650,8.620208,-1.732573,5.663903,-0.892623,9.927759,-6.663723,-1.117762,-1.007858,2.389681,-0.961757],[-4.083848,-0.029529,-0.476069,-3.558891,1.225832,8.587535,-3.504844,-4.108926,3.799311,-6.179906,-4.082506,7.365399,-5.242350,5.846836,-4.947663]],[[7.449137,-8.582237,-8.603695,-5.080035,1.560763,5.649917,-4.909705,-2.842316,0.846590,-7.602304,-0.740156,-5.214199,9.935031,7.891397,-0.547618],[-5.549613,3.929556,-2.387871,9.719360,-9.207963,-9.133496,2.374447,0.478731,-3.558507,9.525745,-7.274498,9.550589,3.151494,-5.832478,-0.830303],[7.849974,-5.713676,9.524252,-1.520604,2.269449,6.208520,-9.728746,-2.323079,2.342414,-3.077718,7.806623,-0.363131,9.414884,0.304369,7.989894],[8.784392,-7.458015,7.926598,-6.227697,-3.724504,-1.975261,1.179922,-1.948295,-7.719672,-1.317507,-6.101436,6.738384,5.855805,2.885703,-4.998660],[-3.104875,1.051691,6.501206,-0.693222,-5.473461,5.328412,-1.438958,6.439499,0.880218,-5.988922,-3.610870,2.981939,-4.130366,-7.866631,-7.875553],[-8.530982,-3.883292,0.172767,-5.218379,1.714044,5.629946,3.742656,-4.544943,-8.832471,-7.619804,3.260437,-2.433395,-4.389430,0.250618,-3.176105],[-9.236169,-2.636408,-4.755985,-6.380860,4.339098,9.413684,8.175487,3.298401,0.013605,1.804507,-5.532835,-8.259944,9.210983,0.320532,6.024651],[-8.187027,-8.930300,6.537821,7.901982,6.289265,7.484462,6.895263,7.781606,-9.177264,-0.571951,-5.983105,1.729196,4.308495,-4.683816,2.678924],[-9.399990,9.957699,7.609472,2.661028,-2.928334,9.660693,8.468969,-3.502208,6.934978,1.120718,-6.716082,7.753797,-0.756792,0.783483,8.025581],[2.677186,-0.658970,6.307044,4.869733,-6.257804,1.417233,7.992840,-3.190661,-9.048901,6.981646,-5.811756,4.906556,6.767143,-5.754706,-0.218571],[8.937975,-3.168265,-9.602764,1.329084,-6.944253,-3.294484,-1.793859,8.430082,8.103877,-5.923008,0.549715,6.672069,-5.631851,1.232236,4.383321],[7.341439,5.403386,-0.498967,5.787816,4.184088,-3.989168,7.607280,9.805962,4.387571,-1.086280,9.058900,-5.424901,7.241541,4.219617,-5.573475]],[[-7.835908,-8.066988,0.137630,-4.837826,-9.060828,-3.033470,9.535129,1.634199,-1.663278,1.595363,5.746747,6.658628,3.443435,-3.405144,5.939605],[7.296641,-1.027812,6.778846,6.400123,-8.942495,0.697274,-9.316519,4.603271,2.076515,-1.685711,-0.890880,-3.958502,-8.580725,-1.304341,-8.507451],[2.151618,-3.357367,7.432645,3.244155,9.556662,2.420496,-9.337466,7.995151,6.287898,-5.385890,0.890959,8.793482,-3.547248,-6.827029,2.068910],[-9.964860,-6.293924,-2.297219,-7.938827,-7.268241,-6.309776,-9.223252,8.787062,-2.760638,-1.962150,1.751791,6.373978,6.641733,-9.225855,3.667693],[8.484058,-5.675134,-3.184079,2.133769,-7.573362,-2.281135,7.143082,6.388558,-0.584189,-5.141381,-8.866594,-1.811196,-7.724341,5.906638,1.841386],[-5.055974,-5.342499,8.404573,-7.413560,2.520826,-6.114826,7.432298,-7.689673,1.539685,-9.459091,-5.787814,0.428041,-4.979884,-1.998965,-9.295223],[-6.128773,-9.021814,6.351463,0.031754,1.049940,-7.267933,-6.205300,2.759147,-5.404423,0.464905,-7.846521,-7.849247,0.472481,-5.798367,-9.714441],[2.129303,4.882057,-2.676546,0.836389,-7.250212,-9.183546,6.703648,-5.629826,-5.397852,5.402639,1.115881,2.467406,0.558886,9.568158,-1.111560],[-5.860144,-5.504541,-2.272070,-8.625799,0.458104,-1.215094,0.726610,-4.752309,-6.394952,-5.233596,3.790617,-7.668558,9.444069,6.401520,3.380957],[0.281195,1.172705,5.020730,-7.346399,-0.292946,7.329040,3.784068,-1.575517,-2.675233,-8.773736,-2.314563,6.199161,-0.476190,-0.113786,0.586620],[-0.767675,5.615039,-0.626920,8.384610,-6.942604,-8.142591,-4.395827,-6.598388,-4.035880,2.883689,7.818074,-6.777390,-3.216687,-3.351703,-0.446354],[-2.339964,-3.485845,-4.194847,5.047372,9.195131,9.687395,0.068350,6.465193,-5.502457,-0.441010,5.033961,6.072086,-1.159395,-9.095712,-7.990415]],[[-3.258733,1.061019,-3.489851,-3.582799,5.600964,8.553747,6.062674,-7.423377,-4.895051,-9.582023,6.618395,0.705105,6.405412,-2.966783,-1.113670],[-3.408933,-1.544955,3.666256,-3.019595,-8.705283,8.149331,-9.728946,-7.184864,3.870965,-1.325546,8.797399,1.130880,-1.249375,1.967723,7.509519],[-4.976315,-3.488090,6.323586,9.237432,7.755642,-9.186487,-4.290756,-5.827200,8.623706,4.421434,7.141241,3.939040,2.641312,-3.520606,7.955512],[-3.884034,2.975573,-4.397274,-1.741285,-9.999599,2.771790,-2.503295,-9.028065,-9.023130,9.867979,6.032781,-0.191891,4.023078,-0.706426,-7.153921],[0.386146,9.178918,-8.212047,-6.442714,-5.677382,-9.269063,6.121988,2.809547,0.708859,1.158578,3.708328,-6.806813,-4.905337,-9.731807,0.040856],[-7.857499,7.061960,7.671970,1.331160,8.892787,8.353888,9.701998,-6.089926,-2.670983,-4.973985,-4.032334,-0.175537,5.835143,5.648800,5.831207],[4.625420,0.973810,-9.524812,-0.371447,-3.279168,4.339954,8.083429,-1.786555,7.833175,-0.739625,5.119341,9.339631,5.156264,-1.247269,-1.844700],[9.468086,5.083715,0.952890,9.985670,5.529767,6.008727,7.269586,5.195871,-3.329219,-5.286602,-7.818802,-5.949171,3.312949,-5.382420,-2.487521],[-1.955631,-2.272567,-5.099204,2.562409,0.927990,-3.959728,5.292399,-3.572612,1.795897,1.222229,7.376890,0.618958,8.974956,5.050887,-5.419523],[5.019507,0.027521,-3.565971,5.591771,6.522539,-8.308003,6.645383,-5.353347,-7.457235,-5.345434,6.500050,7.035645,2.310020,-8.475128,9.650024],[-8.539287,2.622754,-0.972830,-2.778113,1.630484,0.891961,6.899546,7.390288,-5.535121,4.185769,3.319517,-1.955874,-2.423834,0.538103,-5.482603],[7.933649,3.975178,-3.115957,5.279833,2.902354,-6.540132,-3.344224,6.684528,0.353558,-4.517095,1.986468,-3.057935,-1.468306,5.963353,2.593106]],[[-9.537657,6.055249,4.296118,-0.802016,-1.836760,7.357584,-9.858665,-5.956797,7.276978,5.554260,-0.876954,2.579049,-1.402452,7.703318,9.645401],[7.788583,-7.532090,-3.486540,-4.441441,-8.057718,-9.649103,3.530622,1.671704,1.352054,-0.559129,-5.216848,6.004590,5.941556,-7.228069,9.790160],[1.017853,7.508194,0.305790,9.041278,-9.763952,-7.123625,3.733412,5.715070,1.968373,2.186554,1.825403,9.120848,1.915886,-6.924574,7.895757],[9.754470,-1.764352,-6.576268,-2.091036,6.339748,2.609277,-9.443575,-0.031329,-6.400998,-0.524558,8.963273,8.992197,-1.380039,5.260075,-0.359456],[-1.083394,5.042339,7.239582,0.472104,9.285572,-4.491326,-9.681094,3.365071,6.902139,5.838712,0.098847,3.042505,8.920788,9.321902,0.486269],[0.270192,2.966903,-3.975670,1.437748,1.553104,2.614861,3.872197,-9.040035,-5.127700,-9.620081,6.429674,-0.671409,4.095687,-2.506865,-7.161825],[-0.502961,2.408854,-3.347740,-7.346444,4.599189,-2.350335,-1.839504,0.258514,-8.335236,-7.297048,1.991058,-3.097988,-0.089706,7.396400,-3.370585],[-3.855720,4.549846,-7.157777,-5.368361,5.107626,-5.562211,-5.713700,-5.798411,0.629318,5.558769,9.900089,1.374034,-5.760440,1.886090,-3.087722],[2.657118,0.665509,4.262039,-5.558729,-4.213073,3.564248,3.299758,1.843804,8.676620,-5.911419,-3.033854,1.250277,0.760404,-9.065205,9.714096],[-1.370812,7.072660,-3.308521,9.431029,-0.947848,-5.156417,5.612062,2.355726,7.254604,8.681310,7.970579,-9.994687,-5.054373,-6.221551,-8.773690],[8.053310,-8.216311,-9.847728,5.300357,4.473480,-0.968003,-9.784842,4.580686,-9.710399,-4.004144,-0.534960,-7.970538,4.480023,-7.313207,1.196286],[1.090570,5.889361,0.034268,-9.395691,-6.798054,3.578775,-0.286541,-8.780231,1.526484,-7.721070,-1.802157,-9.876027,1.781882,5.367180,1.971743]],[[0.069399,-0.947024,5.454995,-4.136001,-3.390388,7.993435,0.044574,8.367556,-9.047117,4.900647,9.966220,8.390974,-9.988903,6.049650,5.912870],[-6.832307,9.478469,8.510446,-7.168494,9.924050,-4.956576,-3.969855,-2.291483,8.740191,3.655079,4.452366,3.771091,-0.734903,-0.135310,0.600375],[-5.414576,-5.524597,-2.791030,-1.801277,3.210808,-8.136462,5.840923,-3.991840,-6.885149,-3.544841,-1.069378,-9.016218,-8.787463,5.951435,-4.269984],[-6.057753,-7.954909,3.206130,6.065471,7.223123,0.908256,-4.529137,1.197240,-3.313884,6.256056,3.424436,-8.863283,1.934061,-5.803186,5.119492],[9.209127,6.477986,-4.081209,4.047179,8.672002,6.139477,-2.829721,5.633620,-7.821259,2.413385,-1.186038,3.463760,0.852005,6.157247,1.659939],[-2.011299,8.434644,-1.849500,-9.395655,1.633539,-3.284528,-8.089697,-9.237813,-8.246817,4.584192,-4.857781,-1.576818,2.062340,-7.932193,8.798366],[7.180017,1.808240,-4.943371,5.753288,6.967318,-3.904271,1.484067,-4.085884,-5.488257,-4.450555,-7.487820,5.499640,-6.090117,-0.481161,1.280817],[-3.594909,-0.424794,6.703767,7.437494,5.873310,7.896351,-0.346055,7.463210,5.544503,-6.985779,9.410699,-6.435482,1.465316,0.758619,-5.739030],[-9.294519,-5.072861,-9.030117,6.754903,-6.950492,-4.962905,-2.410255,-9.761481,2.715899,5.938573,8.282138,-0.424012,0.541267,-6.301162,-5.116678],[3.451071,9.030169,8.073184,-9.967821,8.524802,9.832564,-5.280128,-6.673337,0.482815,-1.746845,3.300350,-7.038784,-1.981180,-1.619027,-5.129647],[0.692866,4.750613,1.313601,-6.659073,1.587802,-7.891765,3.246677,-1.859314,0.761973,4.152626,-7.011689,4.842987,-8.873518,-6.962517,-1.070307],[7.599704,-1.238493,-3.939552,0.701612,0.032139,-8.082453,-2.305328,4.774540,-1.830538,-1.807693,-8.382780,-3.276589,6.087682,6.854846,5.491753]],[[5.113056,9.872362,3.049198,7.225137,-8.140067,0.775337,2.107675,-1.701483,-6.264913,5.231133,-9.304975,2.164022,-4.415933,-5.475778,-9.052615],[8.230684,-2.165273,-1.192810,3.855921,0.338022,-9.402872,-7.451530,-0.588840,-2.430561,9.343556,3.572688,-1.497964,5.949079,-9.506408,-3.653406],[4.842747,-7.135949,7.849337,-2.496736,-3.500502,-2.707888,-9.022045,-1.660935,-8.756377,-3.476086,1.517266,0.048559,-5.334430,-9.682004,-7.732192],[-6.310001,-1.062179,-6.466496,4.540753,-5.514532,-3.112177,-4.282123,-4.596408,5.364285,-6.262424,-9.231226,9.622491,1.752139,-0.930329,-3.697977],[-4.746362,3.882507,9.503828,-6.245344,-4.068228,6.605146,-5.544268,4.732908,-8.663772,2.700224,-6.540334,-0.292926,7.994629,-1.101593,7.154237],[8.277871,0.259709,4.846816,-7.376137,2.193967,-6.104302,2.345137,-5.338529,1.804623,5.832021,8.077781,4.939863,1.273832,8.601389,-9.011402],[0.227581,7.893600,-9.080092,8.929128,-7.292228,5.442154,9.326625,6.502138,-4.601623,9.453178,9.368306,4.830911,-2.856858,-8.977054,-0.734153],[0.839109,-8.635819,-1.957767,0.733787,2.729191,-3.226234,-4.120978,3.949528,-4.801833,7.096118,0.770703,-0.860174,1.027800,6.000813,9.186521],[-7.859021,0.026426,4.812196,-3.422477,-9.451221,-2.564854,-6.231237,-9.931890,3.847641,6.248523,-1.473779,9.589718,-4.136689,-3.654677,-1.346324],[5.642020,-3.807479,1.214322,6.178743,-8.770119,0.619948,-0.712758,8.098301,7.110392,9.789253,9.924578,9.083249,2.478150,5.386513,-9.958992],[7.630617,3.311361,-4.645865,0.414410,-0.339105,8.478761,-0.047260,2.019037,3.470844,-3.287899,-8.608421,-8.670482,3.563879,4.742231,9.020404],[-7.481832,5.124286,-5.805257,1.323926,9.810499,1.598399,4.985604,7.559473,-1.666590,-8.787762,8.808460,-1.041699,-0.414848,5.210394,0.584452]],[[6.015623,3.296193,8.279997,2.104842,6.015756,-9.270489,7.677478,5.959326,-5.877698,7.409845,-6.029983,2.819552,8.412944,-5.839010,1.318848],[2.682183,-2.810875,-1.911115,3.782312,-7.355608,-1.202361,0.500503,-9.324745,-0.933565,-0.270313,0.210144,4.693361,-2.575014,4.403074,6.507285],[-5.292748,3.701470,-6.701756,-2.401986,3.249304,-0.780223,9.881708,-0.124898,-3.605719,-4.066013,-5.793393,-0.915559,9.803220,-4.793334,2.240249],[0.768272,3.855548,-1.644657,-7.674287,0.599276,4.522263,-1.612113,5.429502,6.786393,5.995538,3.188315,7.955728,5.418314,-6.976345,2.877506],[-7.852861,7.666737,-9.881475,1.605694,-8.729397,-4.830950,-1.853114,-2.525233,1.045967,-1.852684,2.202480,8.960283,6.930813,2.106832,-1.807843],[0.319900,-7.367281,-7.351914,1.572241,5.989869,-9.749556,2.942589,-6.606829,8.328648,3.266657,1.777393,5.099620,-7.200799,6.382828,-0.823661],[-5.965858,-3.230549,-1.704654,2.903023,-6.646283,8.390663,6.133944,-3.135229,-7.126391,5.627515,7.121790,-7.063422,3.667039,2.377928,7.215176],[4.605930,3.383600,-0.518990,-9.034987,2.751931,-3.181365,-7.995543,-6.453831,-1.772036,-2.747816,-8.907594,-0.404857,-8.839446,3.404722,-9.403199],[4.868855,2.469048,-8.851432,-9.981584,7.004310,0.872287,-1.525631,2.728740,-2.762476,4.815995,-4.236387,-1.662965,-2.897791,-2.672977,-2.753861],[-8.404408,-2.134974,5.270595,5.375419,-4.720257,9.203169,4.823135,0.230030,-0.103097,-5.081445,-2.655580,-8.528076,3.920312,6.422341,-7.393926],[-2.902169,3.989710,-7.961281,4.808545,-0.463232,8.735469,-5.912495,5.947799,1.201149,9.089885,8.348836,-9.331635,5.881559,-8.693295,-8.265402],[-9.889122,-7.493750,1.322223,-1.090818,-0.068709,-8.337422,2.616281,-5.033980,-0.242436,-7.777061,2.836577,9.973169,4.548417,1.036298,0.890472]],[[1.589113,7.980297,5.359082,-0.428163,8.140934,-7.854379,-2.746853,-4.775612,-7.926943,1.535058,7.311102,-4.145292,-0.535739,9.295554,-8.272494],[1.018627,-9.846259,9.264347,-6.750463,-7.921804,-8.352034,8.278708,-3.308427,-2.999229,2.109449,3.148083,-7.732880,2.892049,-6.166263,3.834666],[-4.663775,-1.524355,1.135050,-0.190181,2.967547,8.021399,-4.758024,9.538610,4.458628,2.607424,0.611333,6.996355,3.645418,-1.629011,2.412183],[-8.639853,2.204427,-1.001286,-3.613552,-1.519962,1.491617,5.625387,-7.809418,-1.206747,-2.806552,-2.814739,1.005014,-1.390645,2.266334,-9.541437],[-8.078623,-4.456204,9.606382,-4.740249,1.774098,9.599051,-7.037970,-0.751093,0.407670,-6.949672,1.607808,8.051109,-6.597503,4.081941,6.413808],[-4.815703,-0.091241,3.073045,-5.734839,7.948052,-0.675189,-5.238021,9.876667,3.199821,-9.104607,5.143255,6.529292,-9.927539,-1.851509,2.799196],[4.719559,6.382861,-2.740279,6.251247,-5.430412,-9.718906,4.902219,2.233728,-2.939221,-1.466699,1.788525,-0.620913,-6.133814,-7.181733,-1.618900],[-3.285793,-8.418495,7.416242,-4.884060,7.092875,5.286970,8.331126,-2.642343,3.544693,-9.937757,5.913629,9.957047,-5.196288,-8.795570,-7.393594],[-2.735239,-9.672106,-5.511922,5.637546,-7.886065,3.022430,-4.166542,0.852744,-2.929754,1.582416,-8.173910,-2.127721,-9.681778,8.211810,8.650698],[3.322495,7.580569,-0.444482,4.218366,-1.455631,-0.727380,0.130255,0.555266,-9.828795,-2.903560,-7.147745,-9.149395,-4.795944,4.759624,-8.062874],[-7.979073,-5.657281,5.092411,2.842797,-3.442488,1.420492,-1.438506,3.908015,7.069984,5.676143,-2.921441,-7.091289,-8.309045,8.970329,-8.665958],[-5.407713,-4.119376,-2.194275,-0.322943,-2.645266,-7.970299,8.817125,0.548487,-5.925140,-0.526040,-2.097053,4.502858,-1.523649,0.432622,6.499950]],[[9.948827,-2.544283,-2.636418,5.245818,6.049482,2.623775,0.025490,-7.685699,1.289172,6.034750,-5.776863,-4.550013,-0.854667,9.027640,5.422089],[-8.711424,-5.537618,-3.699157,5.297703,4.642075,2.418430,-0.182274,-6.375135,2.485268,9.159614,6.231354,-3.719970,1.796097,-8.765770,5.805310],[5.359885,-3.298955,-7.568874,-4.279251,7.640872,-1.258715,-9.031737,1.819342,6.371968,1.571780,-3.213709,-3.104374,-9.681189,6.429476,-1.232570],[-1.270058,-2.721130,-6.536009,4.131649,8.640600,-0.128339,-5.423325,-7.692863,1.529287,-7.750634,3.763497,-4.370461,-1.373411,2.682400,1.575978],[-1.025832,-0.338824,7.639646,3.514655,8.138470,7.861809,4.258410,2.011479,7.201782,2.547486,3.979348,-1.480818,7.600216,-0.657964,4.179071],[-4.166621,-7.785430,-3.166716,9.058101,-7.152190,-8.109158,9.200740,8.935505,-0.874987,4.169985,3.802020,-5.367651,-9.091740,-2.947898,-3.487237],[1.647616,9.218358,7.707428,8.351466,7.846968,-0.125579,6.450755,3.383177,-3.502802,4.367382,-1.484715,-1.435591,5.430156,-8.658518,5.822608],[4.727141,8.983659,-3.523353,-4.025700,-1.850107,-1.753812,-7.304808,-9.304358,-4.454359,7.400094,-8.665199,-8.494935,-6.043256,-8.368202,7.262267],[2.047932,-8.458143,2.754794,-7.926368,-2.691120,-7.030560,8.131340,-7.032139,-9.809080,-4.469911,-3.893298,9.868106,5.653631,-3.441778,-5.225682],[8.575017,-2.007677,4.993718,0.847188,-4.829379,-8.857815,-1.247896,9.855432,4.488689,4.795676,5.866820,-9.454057,7.283136,-3.621039,9.178173],[5.918333,-9.564427,-7.046530,-4.881683,8.906552,9.746511,0.217743,8.681361,-0.884080,-5.328220,-2.258403,-2.641635,2.014884,-7.879493,2.915395],[-7.265027,1.402242,8.358594,-2.209389,1.793573,-4.237390,0.090725,-5.974667,-7.863681,9.572640,-5.076264,-5.888524,8.662233,-4.382727,9.980417]],[[1.317989,0.075381,-1.772320,3.519823,-2.088923,0.262912,2.599950,-7.616633,3.056803,3.062011,1.653257,9.989017,-0.313201,4.309321,-1.415317],[-3.162160,3.637152,-0.847810,-9.094213,-6.652931,-8.756623,8.586071,6.845080,5.497861,-4.747513,8.588435,2.252659,5.550010,3.799794,-1.678815],[9.642611,-7.114572,-5.089394,1.247223,-6.179832,1.186966,7.707006,-2.352985,-0.652584,2.793942,-9.801151,6.581822,7.844346,1.968961,2.321305],[1.273532,0.585479,0.337197,-6.747832,-1.321716,4.254939,-0.118019,0.974971,2.816500,-5.313264,-9.741834,3.921051,-6.620803,2.971538,-5.046187],[-5.331789,4.340190,7.040787,7.897641,2.324531,-5.201866,-6.006974,3.235097,9.705851,0.300901,-3.818132,6.223079,1.509192,-9.761603,5.242614],[-3.267457,-0.195233,4.612017,-9.226586,-5.957061,7.050153,-5.326924,0.203380,4.957200,-5.411320,-5.880751,-9.756187,7.252004,-8.157872,-6.277891],[-3.241575,0.686550,4.087734,-7.717243,1.689789,6.076129,2.649670,-0.633753,-3.397633,6.242783,8.369620,5.816906,4.460932,4.271154,-3.612300],[-7.848487,-7.220418,-2.733420,-0.917454,-2.618441,9.027420,-4.551168,2.535973,6.072080,-8.588364,5.079180,-9.735754,-0.839127,5.515481,4.233204],[5.993609,-3.974464,7.136843,3.806438,7.266675,-2.461520,-7.598128,2.168729,4.287956,6.451261,4.759950,4.607169,1.616772,-6.179209,-6.061366],[-7.639582,7.736236,7.866980,0.432211,-9.648521,-3.702566,9.684949,-6.539078,8.739237,2.927355,1.517167,2.963638,2.771516,-7.838207,6.129501],[7.253817,4.267138,-7.300930,-0.938349,7.150176,-9.198392,0.793423,-1.303437,-0.835776,5.045677,-8.629661,-9.677864,-4.225620,-0.395938,6.301069],[6.178505,-6.352303,2.211742,9.661507,-1.052677,6.752575,7.156402,9.102810,-8.318520,0.799179,5.189156,-3.120182,4.191976,9.077149,-8.104307]],[[9.790268,-0.051298,-8.896816,-2.264486,0.089492,-4.856646,4.937033,1.438802,-4.484999,-2.685107,4.495130,9.342377,6.041157,-6.499712,8.436588],[-9.599150,-6.108382,-1.149155,-9.799136,6.793698,3.215804,-9.540464,0.168397,8.636043,5.524917,7.772263,-4.328371,6.465472,7.119024,-6.303295],[-1.538184,1.924844,0.068295,9.536585,-4.896119,7.284513,-6.933299,-1.992561,3.720997,9.822475,1.930565,-2.739637,-6.093033,2.441899,0.840358],[-1.855237,-8.111867,1.476001,7.418626,-1.059940,8.991937,2.815173,0.703614,4.074112,-2.706987,-0.489873,3.393222,9.759308,-7.584980,2.747226],[-3.249951,6.367306,1.376828,5.461848,0.324071,-6.501146,3.203925,-5.838191,9.234827,-2.864262,1.854272,3.739430,2.005755,-3.327022,0.269382],[0.668328,0.590320,5.245938,5.563723,8.487798,-6.084795,7.791166,8.108707,-9.276683,5.097208,-6.572340,7.646325,1.894893,-1.962123,-0.795111],[4.082130,-0.660053,-1.648263,9.319204,-9.150571,-3.914924,-0.838317,-0.560955,-4.472146,-6.139065,9.480237,-6.562773,-5.151505,0.447859,9.606922],[5.058566,-6.800165,1.216319,4.102066,-9.198593,5.440877,-3.335596,1.328162,9.360722,8.677295,3.080880,0.091766,-5.940930,-7.410208,-7.000247],[2.083939,-2.003481,2.651690,4.168748,7.097829,-5.024602,-6.228323,-3.801506,-1.276325,5.959341,-3.539020,-2.676967,-5.735509,0.580583,2.539575],[-6.801926,4.542700,-1.071196,-7.122708,9.783028,0.327424,-0.103047,-7.200317,9.064454,5.208376,7.572219,-7.146043,7.266199,-1.041322,3.676362],[-3.557042,-8.338097,-5.814608,7.825364,-5.322307,-4.731343,-1.074468,-4.707695,-0.854745,8.086008,-8.384806,1.834781,9.889370,-3.065586,1.796586],[0.020971,7.583814,-2.317458,-2.549580,9.549844,-6.061668,-6.432191,-5.694207,-2.927801,2.320224,-1.014314,-9.333662,-9.754931,-4.177422,5.417722]]], dtype = "float32")#candidate|8636|(16, 12, 15)|const|float32
bop_8637 = relay.less(call_8634.astype('bool'), const_8636.astype('bool')) # shape=(16, 12, 15)
bop_8640 = relay.less(call_8635.astype('bool'), const_8636.astype('bool')) # shape=(16, 12, 15)
func_4003_call = mod.get_global_var('func_4003')
func_4006_call = mutated_mod.get_global_var('func_4006')
const_8650 = relay.const(8, dtype = "int64")#candidate|8650|()|const|int64
var_8651 = relay.var("var_8651", dtype = "int64", shape = (1, 1200))#candidate|8651|(1, 1200)|var|int64
call_8649 = relay.TupleGetItem(func_4003_call(relay.reshape(const_8650.astype('int64'), []), relay.reshape(var_8651.astype('int64'), [16, 5, 15]), ), 0)
call_8652 = relay.TupleGetItem(func_4006_call(relay.reshape(const_8650.astype('int64'), []), relay.reshape(var_8651.astype('int64'), [16, 5, 15]), ), 0)
output = relay.Tuple([bop_8637,call_8649,const_8650,var_8651,])
output2 = relay.Tuple([bop_8640,call_8652,const_8650,var_8651,])
func_8659 = relay.Function([var_8651,], output)
mod['func_8659'] = func_8659
mod = relay.transform.InferType()(mod)
mutated_mod['func_8659'] = func_8659
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8660 = relay.var("var_8660", dtype = "int64", shape = (1, 1200))#candidate|8660|(1, 1200)|var|int64
func_8659_call = mutated_mod.get_global_var('func_8659')
call_8661 = func_8659_call(var_8660)
output = call_8661
func_8662 = relay.Function([var_8660], output)
mutated_mod['func_8662'] = func_8662
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8667 = relay.var("var_8667", dtype = "float64", shape = (8, 5, 2))#candidate|8667|(8, 5, 2)|var|float64
uop_8668 = relay.atanh(var_8667.astype('float64')) # shape=(8, 5, 2)
output = uop_8668
output2 = uop_8668
func_8671 = relay.Function([var_8667,], output)
mod['func_8671'] = func_8671
mod = relay.transform.InferType()(mod)
mutated_mod['func_8671'] = func_8671
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8672 = relay.var("var_8672", dtype = "float64", shape = (8, 5, 2))#candidate|8672|(8, 5, 2)|var|float64
func_8671_call = mutated_mod.get_global_var('func_8671')
call_8673 = func_8671_call(var_8672)
output = call_8673
func_8674 = relay.Function([var_8672], output)
mutated_mod['func_8674'] = func_8674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8051_call = mod.get_global_var('func_8051')
func_8052_call = mutated_mod.get_global_var('func_8052')
call_8757 = relay.TupleGetItem(func_8051_call(), 0)
call_8758 = relay.TupleGetItem(func_8052_call(), 0)
const_8762 = relay.const([[[-4.152761,-1.014736,-1.745774,-1.439822,-5.836365,-8.891538,-8.347985,-0.130457,-6.949939,-2.293490,-9.432474,-6.263034,-0.900180,-9.644494,2.468893],[3.404768,-7.288740,-0.727215,-3.334745,0.908269,-2.198567,0.469206,-7.869970,5.852528,0.907996,-0.552819,5.300948,1.540867,-9.342127,0.972365],[5.660289,2.680633,3.316490,4.207990,9.506274,-2.357276,-0.193067,-7.210506,-9.424887,8.822778,0.460668,5.723527,8.439858,-9.371756,0.085962],[2.495690,-9.992484,-4.557191,-3.991288,-5.097468,-7.237297,-6.311935,-1.595322,5.592622,-5.693583,-4.772000,3.431819,-3.989288,-9.128428,-6.708267],[-8.669063,-0.174353,-8.333920,-9.521469,-0.203701,-4.348044,-4.535606,-2.780707,7.073252,3.957094,-9.519620,9.979701,5.888904,-5.556324,9.133397],[2.387248,-0.213949,-8.901944,-3.560119,-9.932430,7.450299,-2.307736,8.393981,-4.970835,-0.544414,-1.308391,5.658418,-0.308930,4.005792,-4.352736],[1.113077,-0.445156,-9.344857,9.277453,-2.579370,4.015188,-9.058516,1.779574,-6.595463,5.105410,6.804541,-4.264987,2.449860,3.741941,3.518906],[7.198365,-4.039527,6.096504,6.190190,2.594097,-0.999920,3.285989,-0.596102,-1.626310,7.740118,-6.664382,8.932557,8.070881,1.650282,2.116037],[4.775610,-4.748311,-6.443521,-8.534286,-0.121159,8.133692,-4.773681,1.981863,2.737664,-1.273105,6.104089,3.015409,0.947482,-7.851049,-1.548116],[2.954182,-7.418825,7.767474,2.743477,-6.951628,1.902705,-5.938024,8.291298,0.961302,4.127589,4.569576,-4.621218,3.045608,0.237154,-5.068458],[1.888320,5.147096,6.010745,5.663797,-9.362988,-5.934743,8.479853,-9.090140,2.339826,-8.735344,1.379636,7.775250,-0.260740,8.851676,-7.562165],[4.123529,0.142361,-9.506953,2.418888,-5.897361,7.801241,-7.813855,4.923218,9.134698,-0.134535,-3.933326,5.502523,2.393320,-1.302607,-7.229617]]], dtype = "float32")#candidate|8762|(1, 12, 15)|const|float32
bop_8763 = relay.not_equal(call_8757.astype('bool'), relay.reshape(const_8762.astype('bool'), relay.shape_of(call_8757))) # shape=(1, 12, 15)
bop_8766 = relay.not_equal(call_8758.astype('bool'), relay.reshape(const_8762.astype('bool'), relay.shape_of(call_8758))) # shape=(1, 12, 15)
func_7912_call = mod.get_global_var('func_7912')
func_7913_call = mutated_mod.get_global_var('func_7913')
call_8767 = relay.TupleGetItem(func_7912_call(), 3)
call_8768 = relay.TupleGetItem(func_7913_call(), 3)
func_5699_call = mod.get_global_var('func_5699')
func_5702_call = mutated_mod.get_global_var('func_5702')
const_8770 = relay.const([-8,3,10,-10,1,-3,-2,-5,-1,1,-5,8,-5,-1,-10,4,-5,-5,4,8,-9,-2,-1,6,-3,-7,-5,2,4,7,-6,-9,-2,8,2,-3], dtype = "int64")#candidate|8770|(36,)|const|int64
call_8769 = relay.TupleGetItem(func_5699_call(relay.reshape(const_8770.astype('int64'), [9, 4])), 2)
call_8771 = relay.TupleGetItem(func_5702_call(relay.reshape(const_8770.astype('int64'), [9, 4])), 2)
output = relay.Tuple([bop_8763,call_8767,call_8769,const_8770,])
output2 = relay.Tuple([bop_8766,call_8768,call_8771,const_8770,])
func_8782 = relay.Function([], output)
mod['func_8782'] = func_8782
mod = relay.transform.InferType()(mod)
mutated_mod['func_8782'] = func_8782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8782_call = mutated_mod.get_global_var('func_8782')
call_8783 = func_8782_call()
output = call_8783
func_8784 = relay.Function([], output)
mutated_mod['func_8784'] = func_8784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6604_call = mod.get_global_var('func_6604')
func_6606_call = mutated_mod.get_global_var('func_6606')
call_8791 = relay.TupleGetItem(func_6604_call(), 0)
call_8792 = relay.TupleGetItem(func_6606_call(), 0)
output = call_8791
output2 = call_8792
func_8793 = relay.Function([], output)
mod['func_8793'] = func_8793
mod = relay.transform.InferType()(mod)
output = func_8793()
func_8794 = relay.Function([], output)
mutated_mod['func_8794'] = func_8794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8301_call = mod.get_global_var('func_8301')
func_8302_call = mutated_mod.get_global_var('func_8302')
call_8798 = relay.TupleGetItem(func_8301_call(), 0)
call_8799 = relay.TupleGetItem(func_8302_call(), 0)
output = call_8798
output2 = call_8799
func_8807 = relay.Function([], output)
mod['func_8807'] = func_8807
mod = relay.transform.InferType()(mod)
output = func_8807()
func_8808 = relay.Function([], output)
mutated_mod['func_8808'] = func_8808
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7471_call = mod.get_global_var('func_7471')
func_7473_call = mutated_mod.get_global_var('func_7473')
call_8821 = relay.TupleGetItem(func_7471_call(), 1)
call_8822 = relay.TupleGetItem(func_7473_call(), 1)
output = relay.Tuple([call_8821,])
output2 = relay.Tuple([call_8822,])
func_8830 = relay.Function([], output)
mod['func_8830'] = func_8830
mod = relay.transform.InferType()(mod)
output = func_8830()
func_8831 = relay.Function([], output)
mutated_mod['func_8831'] = func_8831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5164_call = mod.get_global_var('func_5164')
func_5166_call = mutated_mod.get_global_var('func_5166')
call_8865 = relay.TupleGetItem(func_5164_call(), 0)
call_8866 = relay.TupleGetItem(func_5166_call(), 0)
func_6077_call = mod.get_global_var('func_6077')
func_6080_call = mutated_mod.get_global_var('func_6080')
const_8884 = relay.const([10,10,-3,7,-5,-3,3,7,2,6,8,8,-4,-3,6,4,3,8,-5,8,-5,-9,4,-4,6,6,-3,-8,-5,-6,6,-7,-2,-6,9,6,-4,-2,-3,-5,-8,2,9,8,10,5,4,6,-6,-4,8,-10,-7,3,3,-8,2,2,-10,5,4,6,3,-5,-8,-5,9,9,10,-5,-1,-3,2,4,8,2,1,-10,-1,3,-4,-6,-6,10,-6,-8,-7,-9,8,1,-3,8,10,-6,4,10,10,2,10,1,-6,-2,1,4,-5,3,-7,-1,8,-7,9,-2,-5,4,-6,-3,5,7,-9,3,-3,3,9,6,3,2,5,10,8,-7,-8,-9,8,-9,7,4,-10,2,2,7,-5,7,2,-10,-3,7,9,-6,-3,7,-9,-4,9,8,-5,-9,5,10,5,-8,-9,10,2,-7,1,7,-5,8,-8,-7,3,-3,2,-6,3,3,-10,2,-1,8,-4,-9,-5,-5,3,-6,-6,5,-2,4,4,9,-2,-5,-1,4,-8,-4,-10,-8,9,-3,4,-4,8,4,-5,7,4,-10,-5,-10,-7,-9,-1,4,-2,-6,5,-3,-8,-7,9,-2,-8,-10,7,7,2,3,-3,-7,3,1,5,-1,10,6,3,-2,10,-5,2,1,8,-1,-2,-7,-4,-3,2,-4,3,2,9,7,6,6,-4,3,-4,6,-3,-1,1,7,-7,6,10,7,1,-9,-8,6,6,5,-4,-6,-3,-5,10,-8,3,-8,-1,4,-9,-1,-10,8,-6,5,-3,8,-7,-2,5,5,-5,2,-8,-10,-9,-5,-9,6,5,7,4,7,10,-10,9,-2,-8,2,1,2,-4,1,-9,1,8,-5,-3,6,10,-8,-1,5,7,5,1,7,6,1,5,-1,-9,-7,-7,-6,1,7,-6,-3,-4,-10,8,2,-5,9,-4,3,5,6,5,10,-5,1,-3,-4,-5,-4,2,-6,9,-9,6,-8,3,4,5,-5,-2,4,1,4,2,8,4,-5,9,-7,5,7,-9,-10,-6,-7,-3,6,10,-9,-8,8,-3,6,-8,-9,10,3,-7,-8,-7,-3,-7,-4,1,-9,2,-2,2,-9,2,-3,3,6,8,5,8,-6,7,9,-5,8,6,4,-7,-8,10,3,-9,5,2,3,-8,-2,10,2,10,5,-9,7,10,4,9,5,-8,-5,10,8,-8,-2,4,6,-5,3,7,-9,5,9,3,-4,-4,-1,9,-10,-2,7,-8,3,3,-7,-5,-9,2,-6,4,7,-1,10,-8,8,5,-7,10,6,5,4,-10,2,-3,-8,-10], dtype = "uint16")#candidate|8884|(495,)|const|uint16
var_8885 = relay.var("var_8885", dtype = "float32", shape = (1, 308))#candidate|8885|(1, 308)|var|float32
call_8883 = relay.TupleGetItem(func_6077_call(relay.reshape(const_8884.astype('uint16'), [495,]), relay.reshape(var_8885.astype('float32'), [308,]), ), 6)
call_8886 = relay.TupleGetItem(func_6080_call(relay.reshape(const_8884.astype('uint16'), [495,]), relay.reshape(var_8885.astype('float32'), [308,]), ), 6)
const_8889 = relay.const([[[9.271400,-0.853714,-3.867662,4.327825,-7.766566,5.030857,-2.941461,4.758209,1.138610,5.086195,-7.130831,-3.669635,-7.686510,5.136727,-2.329952],[4.375706,5.629514,2.086622,4.746433,4.872294,-6.287617,-3.074420,6.333906,-9.375750,-7.706475,-6.790513,5.912753,7.285930,3.635806,-7.599679],[9.703442,6.441931,5.081538,2.125913,6.371429,-0.924437,5.125903,-8.172700,-1.295070,3.653261,-7.829110,-3.109205,3.354918,8.479553,-7.368450],[-6.320355,-2.039163,3.804785,-9.239674,-1.287026,6.171717,6.538900,4.262260,4.982534,-3.733191,-3.591248,-7.591758,-8.219774,5.796256,-5.923288],[-0.193625,0.968264,-6.655375,-9.799791,2.997454,-5.340181,-2.968299,-1.510173,2.628242,2.076658,-4.397354,6.352371,-9.007838,-6.517715,5.877035],[-6.996290,9.595370,-1.244380,-6.950525,-8.435800,6.275046,-7.405423,-9.557280,-2.424151,7.696083,-5.494868,4.195282,-9.701111,7.221910,4.332243],[-7.976488,-2.134150,-0.336110,0.077840,-8.950349,-2.525697,8.086309,3.422923,0.606255,0.934975,3.147885,2.178982,1.564785,6.264579,-5.260829],[-0.939178,-6.218045,1.146512,1.374781,0.657124,-5.118498,-9.096762,-3.783208,-8.736881,2.665892,-9.776437,8.360328,4.563053,-1.443364,4.821414],[-6.053447,3.313680,8.150172,8.428697,1.796541,-7.516393,-4.312372,9.290872,-5.100335,7.038279,-6.320811,-6.923986,3.692750,-1.721248,-4.341464],[-2.854798,3.210014,1.476679,-0.179110,-8.929715,3.711186,-1.415427,3.173568,5.626169,2.176132,7.381332,-8.995104,4.299205,4.295894,0.886845],[2.757924,-2.083117,3.937354,6.995160,-2.629983,-8.965595,-5.694376,-1.924240,-5.733052,7.812754,-2.329933,3.993023,7.909508,-2.773731,8.736776],[-4.324271,2.388411,6.725061,5.170402,2.760661,-0.607090,8.159467,-0.239153,-3.448120,9.374623,-4.528615,-0.843731,6.792211,-0.516581,2.716187]],[[2.131337,-4.481429,-9.063662,-6.304547,2.948353,-5.894251,2.428371,-7.646943,5.714071,-9.136550,0.275513,-4.959031,0.189733,8.433033,1.366869],[4.799874,-3.582631,3.530467,5.748260,-0.245276,9.840586,0.344546,3.712607,-7.658196,-3.638434,9.137910,2.553883,-0.597983,5.627780,-6.582344],[-1.656198,-4.909301,-5.965703,5.906949,5.375696,-3.268203,-7.151952,6.936200,0.495477,-9.895966,-7.797076,7.816767,5.664912,-9.120219,3.129452],[6.524523,-6.517178,4.383897,-3.191182,5.195724,-3.184075,-3.294489,5.878034,-1.596525,-5.900511,-2.188809,3.389345,-1.151286,3.665720,1.352744],[-5.025952,-2.827264,-2.589761,6.731912,3.535740,-7.484371,-2.929045,-1.210489,-6.018547,-4.774711,-5.670266,-7.223719,4.147645,-7.734665,5.275420],[1.475679,8.438805,6.992733,8.651713,-2.219721,6.226121,2.907310,0.854974,6.016664,-6.138068,-7.420416,-1.209726,-8.865776,-7.648325,1.035879],[1.819225,6.347042,-6.841223,-8.858093,6.659895,-5.065874,-2.867248,-6.900963,-3.142612,8.583932,4.152816,0.285387,-5.925135,5.072096,-6.992339],[7.745691,-5.371892,-0.472638,6.394750,-6.880529,6.375868,1.145993,-2.729160,-5.823084,6.196721,-1.164178,7.932717,-9.342574,0.341058,-9.092201],[-6.070504,6.682067,-6.798913,-0.263905,6.644077,-8.013371,1.888742,-4.409103,7.592727,-7.288358,-0.480660,-7.274415,-6.943347,-9.936213,-9.337054],[-8.596116,-6.864981,4.381673,2.573247,-5.899224,6.458380,-0.346867,-3.005119,-8.762320,2.567010,-5.004995,6.683684,9.606035,4.106896,-2.666411],[5.266914,9.134434,-4.097536,-7.181659,-1.329581,-2.676227,-6.534459,-4.605219,0.492886,-9.259559,-7.634986,0.642559,5.119426,7.248937,-6.081414],[9.316425,-4.237764,3.640537,5.447281,8.387984,-6.626606,3.590599,-5.739958,9.407097,6.791453,-1.158131,-5.645946,6.079073,-5.092451,-5.186807]],[[-1.603715,-3.195450,-8.389846,-3.079401,-4.364682,4.332740,9.797611,9.475600,5.924361,-3.647075,-4.468311,-9.640646,-0.855376,3.492098,-5.589431],[6.316520,8.818496,-4.658182,7.455550,8.147805,-4.989762,-2.898829,-5.798834,0.466376,-2.689554,-7.348563,-2.415711,9.043268,-9.060845,2.066177],[-0.650279,-2.879779,1.635711,-0.856095,4.746411,-4.326623,-9.615009,3.123725,-1.350384,-9.256728,-0.171029,3.990384,0.240305,8.863328,2.322976],[0.456252,1.801554,5.711042,-8.645756,9.209454,-7.941983,0.382840,-7.685044,7.338027,3.600428,3.606612,-6.630783,-7.263646,0.095106,2.771960],[-3.687058,6.919507,-7.740069,-0.292349,-9.054945,-1.423929,3.106505,5.831119,3.893598,-6.301833,1.075305,-5.067259,3.248208,1.500713,8.708709],[8.072267,6.578768,1.814281,-6.593782,-9.024056,-5.787690,8.726998,-2.544019,7.089706,2.712857,-4.180651,-2.741243,-8.747620,1.984720,-4.583003],[-5.858576,6.427298,-9.235711,-2.060187,-3.989843,9.276757,0.503355,7.358037,-3.538038,1.959617,-3.806660,-3.752797,6.259487,-2.977152,-1.640053],[8.780565,3.985541,0.199472,3.356443,-2.592432,-8.396341,-3.192622,-8.056847,-2.754024,1.165666,-5.047975,6.301174,-7.951018,1.910997,-6.464515],[1.883928,-2.079348,-2.731225,3.875253,4.773680,3.991408,5.781094,-3.992476,1.261024,-5.182266,-1.711366,6.216348,5.226200,-4.535777,-7.919345],[2.421219,-3.278918,-1.938302,6.119811,7.725694,0.150594,-0.801370,-7.958788,-3.004411,2.680446,-8.891807,3.940079,-8.232954,5.292734,4.609886],[3.774139,-9.634810,6.042269,-6.380604,-4.530418,9.628486,-1.563680,-8.773426,-3.095857,9.420943,-2.114896,-0.797204,9.695214,-3.581962,9.258773],[-7.881845,-8.487421,6.356373,-3.587374,-0.112356,1.102811,-8.462847,-4.758797,-4.258890,-8.036526,-4.058640,-3.606803,-2.288600,0.767898,-6.537787]],[[8.020172,6.748733,6.703109,8.392314,-5.339489,-7.319129,4.154875,-7.340656,-7.907368,5.672269,-4.789989,7.671228,-9.692270,-5.175405,-0.599222],[-8.958527,3.050267,-7.782077,-5.162071,-9.114144,3.993695,-7.731274,-6.864016,-5.155459,-1.889221,3.305168,-4.417378,3.603758,-5.231514,-7.078785],[-5.912917,-3.332913,8.684151,7.904964,-2.290874,-6.493811,-9.853064,5.210246,8.006334,2.586971,0.792769,-4.253242,4.844820,-0.163084,8.751512],[6.191949,3.760960,-1.948361,-0.269314,7.565576,5.674049,-1.446472,-4.556197,-0.664771,-1.673921,9.580436,-4.121473,3.417526,1.021742,-1.116243],[-7.415839,6.969653,2.055303,-5.231134,7.202690,9.851155,-9.293856,-7.361250,2.529315,-1.139616,4.999558,1.013980,-0.526813,4.878558,-7.591528],[-2.425190,8.772926,-3.283193,6.389661,-3.410398,-8.582308,-7.929263,-7.538279,-1.088999,0.421699,7.347836,-0.497581,5.578022,9.439415,4.667230],[-8.777229,-7.640082,4.117456,-9.293729,-7.003353,3.647066,-2.025527,5.057579,-3.921377,-8.061378,-7.416670,-3.354014,-1.346903,0.724602,7.172561],[0.546619,1.277494,7.281581,7.550808,0.518761,6.050012,-8.359272,-7.527991,-1.081390,7.501624,5.541099,-4.236821,5.537854,2.268679,-9.700937],[3.655930,-8.647299,5.359417,2.785597,2.972788,-4.215453,1.555651,2.825636,-8.787765,-8.086194,-2.425781,-7.472026,-8.647103,-1.869055,-0.534377],[-6.889149,-4.212344,-1.637689,-4.788730,-7.032179,5.869535,-9.656391,-7.614048,-6.520103,3.920324,-8.638235,-5.577241,-6.755074,-9.747194,-5.556243],[9.674366,-7.814266,7.170462,-1.972001,-8.132846,-9.745276,6.603512,-3.960638,-1.722985,2.173862,-7.784255,4.961404,-9.726576,9.302364,-3.690239],[1.181025,-2.689390,-6.555805,0.963559,1.746169,4.596389,0.085137,6.006647,-3.621427,-1.420712,6.262375,-2.314067,-9.258313,2.586435,3.075163]],[[8.510150,7.246412,6.371619,-6.068701,-9.951901,-7.153663,6.492002,7.283457,-5.930632,-9.810727,7.274918,1.613392,-0.336722,-5.781397,8.331181],[-6.875193,-5.328419,-9.810801,9.869082,-1.921367,-4.302528,7.833110,-3.506438,-5.219455,2.580193,-9.864509,1.851915,-5.778370,4.364330,1.316191],[-8.854540,3.337692,0.795707,-0.441442,-8.275763,8.147149,-3.666514,-1.839453,1.629984,2.654069,3.037795,0.404335,4.507479,8.845947,-2.411801],[2.374066,-3.182518,5.426501,-5.133902,-3.116022,9.062658,2.306231,-2.705018,-2.391277,1.193011,-9.998967,1.333344,8.177430,1.272447,2.453479],[1.816052,2.447708,-7.964036,8.815247,-4.674656,4.049120,9.196329,6.410108,1.030201,5.804104,1.743031,5.055035,2.407954,4.520008,4.461219],[-1.249028,0.172879,-8.659143,2.108605,-2.000431,7.552129,3.117835,1.883549,0.731835,-8.367105,2.841795,-9.271057,2.881999,1.624061,3.427013],[2.234500,6.014023,2.161508,-1.449662,7.732692,-7.806953,5.653636,-5.307119,9.495601,3.730809,-2.088303,5.924176,5.385176,3.696849,-3.167378],[-4.290451,-0.836817,-6.184264,5.332064,-0.194359,-0.820402,-7.479420,-2.378125,-2.413907,-4.759977,-9.090521,-0.693642,7.999247,-4.567196,-5.855937],[8.896657,-2.107022,-3.963195,4.447965,-2.835129,-5.776108,8.015844,-3.082337,5.120995,8.616676,-9.839452,3.402359,0.038700,-0.612597,3.339821],[-7.430119,1.281992,-0.801895,-2.666591,-9.815787,-0.840744,0.372741,6.181235,2.674473,-4.714381,-5.944813,-1.894917,2.006734,-3.760515,0.799554],[-3.114221,2.678600,7.634669,6.413099,8.410729,-4.513517,-9.250423,2.381990,3.822019,1.292706,9.947709,-5.108040,6.212041,-7.034900,0.795965],[3.959995,1.899871,-6.078038,-9.605454,-1.112052,1.904329,9.107613,-8.930252,4.418832,-5.006112,9.613056,-8.313811,3.123582,4.357633,8.744281]],[[-0.215708,-5.122653,1.327675,-1.186811,-7.870130,-1.390246,5.418545,-5.271461,-6.818004,0.393474,-3.004355,7.406554,-2.578686,-6.743964,-8.779932],[-1.669847,-6.266513,-5.217569,1.309625,2.843552,-6.156266,0.465343,-0.210118,8.319185,5.581369,9.754794,-7.393116,-6.647854,8.704808,-5.151971],[4.663243,-0.618355,-2.835000,9.914045,0.364571,8.706591,-1.265842,1.352786,-1.229493,-6.882888,8.313008,7.127018,-1.922905,-2.770135,-3.588813],[9.566759,-9.214181,1.988761,-2.593584,-8.831172,-3.245080,9.371157,1.612513,1.907203,-1.977588,3.567897,9.241317,2.456975,2.021129,9.945249],[-5.090136,1.425956,5.935536,4.698400,6.332971,7.295208,-7.364652,6.645492,-9.604050,4.206796,-6.457904,-3.520976,-0.325618,5.517254,-9.804336],[7.958252,8.585962,2.770367,-2.566365,-2.623642,-2.900992,4.256232,9.104511,-7.052527,9.376683,-0.219991,0.492606,0.419530,-4.134477,9.155279],[7.652043,6.823776,1.715518,6.698603,-1.900168,3.265787,-9.715857,0.994322,8.067926,4.623958,9.661435,-7.558634,-2.754027,-9.203061,-3.655118],[7.054530,7.460196,-3.222805,1.357979,-4.780696,-9.404398,8.476104,-0.111946,-3.073865,-7.600768,-7.938759,2.950890,-2.434798,-9.478157,-2.473686],[-5.255523,-6.449789,-7.624436,-9.250822,4.767891,1.836750,0.879298,-8.548511,3.284398,5.367549,-3.716988,-4.433188,3.002867,1.417656,6.204507],[-0.497452,-9.934930,2.673868,-3.338731,-7.726553,-3.904683,3.208238,-9.730021,2.588933,-1.128461,-9.249698,-1.981984,-2.788565,7.153964,4.758081],[2.783017,8.978558,1.121246,-4.228346,-9.235204,3.932216,4.408200,-5.311530,-9.359954,3.221738,8.000718,6.107086,-6.886919,8.226846,5.508635],[7.355821,-3.370381,-2.137089,1.466646,7.082368,-6.015858,5.684460,6.264317,4.068474,7.463207,-0.538573,-7.437808,6.576969,1.713805,2.176011]],[[2.021098,6.602844,1.721080,6.428833,3.797549,-6.086935,6.333876,9.654660,-7.188363,-4.085875,0.953990,-8.259598,-0.657479,6.565650,-6.968513],[5.477081,0.956191,2.802224,-5.681173,9.163278,-8.117265,7.925265,0.657071,-8.156541,-2.177133,-0.037566,-0.404084,6.658995,-0.475168,-7.542704],[5.692363,-3.420659,2.132010,2.026839,7.931065,4.872898,7.533022,9.337626,4.200652,-2.374004,5.894364,2.843834,6.358891,-3.796245,5.550871],[-9.498907,-0.024520,4.991254,-3.880077,-7.287091,-5.832307,9.057084,-7.466175,-4.576267,0.379308,5.604799,6.193625,-5.522335,-7.419404,-2.746964],[3.559111,-8.028951,-5.572546,6.674307,1.723995,-6.920322,4.704261,3.868378,-3.919611,5.165672,-4.516297,-7.434544,-2.471454,-6.202703,-8.327481],[-7.000994,5.624221,6.575569,6.099387,-4.678556,-8.184182,-5.911986,9.776021,-9.746396,4.214616,8.005693,-0.727185,-8.170001,-8.150631,3.933385],[2.751086,-3.278172,8.630656,-1.195940,4.986926,2.785741,5.728980,6.393720,5.983597,9.609180,-2.317486,-2.519224,-5.219112,7.349029,9.582739],[9.486997,-8.475926,7.479543,-0.886443,-9.758854,-6.819644,2.581344,6.248139,-4.870241,-7.652969,-6.736362,-8.801257,-4.090823,5.021249,5.187617],[-6.975544,7.183102,0.492853,-2.805846,2.950210,2.973753,-9.146633,9.190592,3.951154,-8.001645,1.501983,-8.823503,9.381210,8.593903,-0.480381],[4.398396,1.024885,-3.051717,3.691811,-9.186208,4.408892,9.941932,7.183815,-5.390303,-8.889039,-1.622163,7.844829,-5.923753,9.757302,1.031477],[-3.214620,8.248627,6.993071,-0.098887,-1.671622,7.892424,-0.886044,-7.536075,-3.176563,7.569837,5.958399,-8.768634,-8.103404,-9.095654,-8.027843],[-9.819906,-6.099290,9.724036,4.362430,0.335624,-2.060021,6.332210,3.692319,-8.645785,-1.906330,-6.363573,-4.905250,-5.091613,1.880739,-8.183021]],[[-5.505953,3.009086,-5.468906,5.818760,-0.863545,-1.510811,7.552271,-6.939312,3.696050,-3.354599,-8.072836,4.416303,-2.762064,9.797001,-3.682307],[8.510371,-6.005120,-6.905155,2.663182,-8.874057,-5.410608,7.827553,8.344848,-1.759235,-7.967693,-1.859452,3.949552,6.478321,-3.930829,-0.712409],[0.565941,5.235379,-8.730016,-4.154134,4.908104,9.575055,6.743777,-7.814581,-9.799287,7.973608,8.499140,1.466987,-4.116598,-1.639607,-9.400058],[4.577296,8.777833,3.215223,-8.110226,5.914972,2.346119,4.693349,6.345806,7.144405,-6.018035,3.849512,-5.588371,4.352035,5.839180,8.964229],[-3.307531,5.093344,-1.083978,5.707310,6.647473,-9.025885,8.148370,5.110153,4.976178,8.471074,-8.861570,-3.263966,6.752664,6.158356,6.758283],[-5.395707,0.434900,5.246024,8.680549,0.782106,-8.375925,0.269428,0.996983,-0.746926,4.812713,6.735730,-6.380293,-4.925837,0.154269,6.454647],[0.105253,-0.263145,7.499700,-6.281925,-5.930051,4.837708,3.756317,-0.240213,-1.330719,-6.294852,-3.607663,0.535548,4.532507,9.865663,1.915165],[9.205242,-4.948043,3.883191,-5.113293,-4.784030,7.715523,3.877940,-6.417123,-0.902907,-6.151142,-8.870150,-5.754143,-1.548631,-3.944907,-7.487527],[-9.458967,-5.301269,5.565358,-6.245388,2.065559,-5.840902,1.776164,8.515267,7.455913,-3.682820,-4.866057,7.061594,-7.858292,-7.271865,0.726236],[-8.585081,1.281262,-4.861979,-4.471176,-5.533212,-2.137197,7.501749,-1.988091,8.253501,-1.299141,4.942729,5.354033,5.681059,-5.818330,-4.501284],[-0.655487,8.442574,4.977069,-5.399525,0.413203,7.133455,6.800514,3.853543,4.931044,1.738558,-0.063689,2.146525,6.495010,9.460680,-2.381108],[1.740348,-9.609017,-8.298885,6.675307,6.733714,3.335792,-3.683687,1.516646,-5.728015,-9.242603,-0.646504,7.235296,-0.526951,-4.054836,-5.879869]],[[4.889302,9.394578,3.686114,6.205574,-8.303507,6.131485,3.024616,-1.005748,2.858925,-9.624013,0.080421,-0.399555,-6.380844,1.126976,-6.244496],[6.170306,-8.988100,1.122599,5.141356,-3.740627,4.509668,9.781187,3.254393,-5.246518,9.073319,-7.511988,3.394679,5.569979,-7.334260,3.533274],[-3.164586,-5.909780,2.115992,-7.144400,5.796002,6.622312,-0.880448,1.230717,-7.692219,-7.639489,-7.416386,-1.094244,5.678059,6.554768,2.000417],[-7.175560,-4.535543,-8.671256,-9.593266,-2.804705,1.061448,3.279641,-5.549827,1.191782,-6.259754,-3.689318,-6.450907,-0.133666,-2.392569,6.572406],[-8.363721,-5.313064,5.978608,1.063443,9.182838,4.868385,7.504012,9.183361,5.332206,-0.626498,-2.178155,3.656967,-9.347912,1.775511,8.691934],[-2.507380,-5.975908,-9.021087,9.912051,-8.541192,6.258947,5.354498,-4.950645,0.051753,8.159599,2.226874,-2.550723,-1.467346,-0.078088,-8.087796],[0.036016,-8.467978,4.642044,7.975200,-1.794828,7.253180,6.864965,-5.927621,2.480521,1.142763,8.597564,5.042882,5.277276,-8.300884,1.293461],[-2.597327,5.382889,-4.012685,7.957508,0.150632,4.036529,-1.271066,0.534939,-7.144492,-0.280954,4.848421,-2.021925,7.447278,7.125596,-5.782375],[-6.651489,2.382845,8.310873,-7.058268,9.354696,-8.390498,8.793370,2.275546,0.133393,3.245293,8.280137,9.779841,3.810987,-2.249472,5.018024],[2.600805,5.709592,3.447170,9.569109,7.560506,-4.995496,4.202692,-0.490342,-8.843820,0.123798,6.154410,6.361108,-8.207237,-2.289696,3.532318],[5.475330,3.321529,4.958427,6.481534,8.707001,0.023804,-2.240478,1.398466,8.965336,-5.383826,6.796046,5.337474,9.534664,-5.623807,-7.402000],[2.996149,-9.639109,-5.304747,6.502292,-6.721639,1.965015,-7.909120,7.239362,-4.317400,-3.748505,0.198895,5.128411,-6.440234,-9.898309,-2.017528]],[[-5.128866,7.898757,-1.341871,-8.834704,6.949911,-8.898234,-0.143345,4.518003,-7.170903,-0.866136,-3.768558,4.957324,-2.749082,-0.280234,-3.378622],[-2.967690,-2.216910,7.205115,2.323557,6.653663,4.629670,6.344609,-9.793460,1.978252,5.668963,5.333083,2.725319,0.398981,-8.196156,-8.117903],[-3.133419,1.368652,-5.417255,3.938177,-0.223337,2.367149,2.505810,4.340496,5.966559,-5.017248,-9.236217,-5.323832,-6.860571,-0.993192,-1.659687],[9.842672,4.388523,2.077136,-6.678624,5.688384,8.726077,-1.182937,-2.530179,7.900294,-5.753649,-4.034371,6.917135,-3.911707,-8.427402,3.832052],[4.132805,4.437073,1.286682,1.713932,4.817615,8.333369,7.658821,8.556714,6.773205,7.576863,3.552733,0.512251,-9.116647,-7.060480,-5.062797],[2.770457,5.832059,-3.962806,-5.322299,-1.434967,-4.822089,-1.040484,6.516694,9.529250,-6.084656,-2.011969,-8.620740,5.048794,9.864729,3.788441],[3.159657,4.226109,5.867547,7.359917,9.389718,-4.475554,7.912896,6.474977,-5.007464,-7.648077,4.000499,-3.662566,-1.909351,6.593493,-5.181947],[1.770416,8.862862,-4.782328,-0.939398,-9.601963,5.885258,1.217968,-6.554081,6.978619,-1.358859,9.673323,-3.198738,8.348831,0.129038,-3.286715],[-6.832924,3.379347,-9.486585,-9.502909,-7.433898,6.499895,0.795642,-7.221094,5.928961,3.971466,3.093167,-2.469469,-8.865529,-9.968505,-2.717830],[5.253284,-4.995665,-1.486991,-9.216216,6.324232,-2.240752,-1.057021,-5.752128,0.357622,-4.732718,9.854115,0.995483,0.900524,9.717128,-8.114727],[-5.503754,-3.610465,-8.785146,-9.144885,-7.551761,7.772301,-8.142969,-2.094251,3.164443,-3.857484,-4.954517,9.116630,1.301843,-6.532050,1.161676],[-8.042931,-2.816821,-8.783351,-2.872242,-3.873763,3.374729,5.210515,2.779239,-2.959467,0.383128,5.009224,-1.875072,1.971418,4.010731,-4.089777]],[[-1.879547,0.397680,-5.007767,-6.562865,-6.750847,5.060684,-9.508117,7.375294,-8.872035,-0.608624,-9.906107,-8.364234,6.029994,2.024466,8.428814],[7.062147,-8.784273,-6.052239,-9.647424,8.871692,5.788783,-5.179702,0.090026,-9.830145,7.586189,1.345298,-8.415726,-7.948931,-1.768683,-2.057194],[-7.718822,0.398294,-9.211059,2.501228,-3.747561,2.932288,7.388794,-2.989115,2.152135,-1.547065,9.832094,1.941753,0.697388,0.056969,7.742604],[7.480183,4.289186,-3.412326,0.611214,2.234528,8.629948,9.874151,-5.317540,0.710943,-9.306303,5.615076,-1.855696,7.242405,-2.520475,9.071944],[6.662543,6.242832,8.557577,-0.937091,9.686356,5.726916,4.253191,1.044860,-7.804993,9.479968,7.465921,-1.210146,2.937741,6.279232,5.182012],[4.366135,-3.592805,4.181100,3.464518,-4.600957,9.107387,1.516113,-7.397670,1.093280,0.541980,-0.564462,3.718946,-1.920650,-4.425809,-5.650190],[-6.789978,-8.720212,1.827044,8.950794,-9.757028,6.563831,4.719336,-4.749485,-8.714707,-3.658198,-8.255989,-6.733238,2.837302,1.704169,-1.060700],[1.604077,2.808171,9.519990,-4.700997,0.773579,-7.192288,-9.809723,6.361409,-0.063085,-8.155312,-8.024842,1.618802,-1.275152,1.506694,-1.817660],[-6.587844,1.292228,-3.322621,-6.327801,8.165835,6.349553,-2.533397,7.804069,-2.400506,9.003193,-1.633291,6.905922,-1.959752,-4.835795,3.635790],[-9.389736,1.847469,-4.219722,-2.353992,-2.539625,-7.598516,-7.867347,1.640021,1.219195,5.421304,9.982963,-0.202795,5.183390,-0.152578,-0.955806],[-8.762786,4.162900,-2.511719,7.090856,-0.247563,-2.797163,8.780621,-5.620356,-7.475929,-9.097975,-4.137464,1.130040,5.490753,-8.130990,7.757691],[6.051106,6.855332,4.179358,-4.589663,-2.029090,-0.299455,-3.303044,8.073039,-2.063356,-9.333931,2.347441,-8.913774,8.005266,7.266883,-4.454368]],[[-2.693265,4.349096,-8.478486,-1.249858,2.600424,-3.737341,9.996673,-1.398437,2.495555,3.108356,3.227220,-7.774899,8.348525,4.976449,8.369469],[8.115195,-4.187260,9.270759,7.616415,8.886782,6.010029,-4.709127,-8.432796,5.076684,-3.917296,1.837223,-0.972112,5.865967,7.162218,-6.097652],[-4.091613,0.726056,-0.789561,-5.748876,-2.468935,4.772520,7.963549,-7.542494,-7.782394,8.377559,-2.773069,-1.257281,-8.403580,4.363791,3.967046],[0.827783,7.317450,-8.010353,4.952526,-6.594729,-5.745909,6.909488,0.764999,-0.124915,-1.489780,-4.614476,-1.044400,7.913551,9.010541,5.900469],[-3.422653,-0.670699,4.954296,-7.339033,2.860545,-1.498151,-2.790015,2.041240,7.475033,3.109308,3.512121,5.475404,-6.408754,9.327607,8.757083],[-5.725174,9.559244,4.545219,4.726229,2.185893,-7.342086,1.215511,-1.777213,4.195416,-9.278052,7.927492,-3.884357,6.691823,5.065818,-1.690250],[0.498565,-1.018135,-4.131835,1.964254,1.234230,-1.115661,-8.315472,-2.883220,5.776970,6.845329,-8.599842,4.133261,9.412966,-4.989916,5.693281],[0.393357,2.719273,5.729026,7.092304,-7.559943,-8.241530,2.978269,-4.135394,9.921225,7.146111,4.257285,6.682582,-7.119198,1.572368,0.911087],[-5.674024,-6.570165,-0.264209,4.380826,-4.430980,6.058810,-2.481477,-8.155864,-0.671998,-3.189086,-6.781556,-1.439086,1.418166,-3.417070,3.188738],[7.115996,-3.503866,7.759756,-4.046583,-0.319429,-2.053707,3.134565,-4.197664,0.784773,7.431258,-3.607352,4.372082,0.568448,-2.041209,-1.238995],[3.602695,1.950043,2.002977,-3.682780,9.885111,-4.299743,-5.368921,-0.953843,2.422428,-0.896053,-4.759413,-7.406787,3.739241,-1.406577,8.340558],[9.259552,-0.830865,-2.374476,1.791051,7.878394,-4.333933,8.540993,1.279446,0.612342,9.708951,2.897962,8.494903,-3.352163,0.230439,-5.969292]]], dtype = "float32")#candidate|8889|(12, 12, 15)|const|float32
bop_8890 = relay.mod(call_8883.astype('float32'), const_8889.astype('float32')) # shape=(12, 12, 15)
bop_8893 = relay.mod(call_8886.astype('float32'), const_8889.astype('float32')) # shape=(12, 12, 15)
output = relay.Tuple([call_8865,const_8884,var_8885,bop_8890,])
output2 = relay.Tuple([call_8866,const_8884,var_8885,bop_8893,])
func_8896 = relay.Function([var_8885,], output)
mod['func_8896'] = func_8896
mod = relay.transform.InferType()(mod)
mutated_mod['func_8896'] = func_8896
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8897 = relay.var("var_8897", dtype = "float32", shape = (1, 308))#candidate|8897|(1, 308)|var|float32
func_8896_call = mutated_mod.get_global_var('func_8896')
call_8898 = func_8896_call(var_8897)
output = call_8898
func_8899 = relay.Function([var_8897], output)
mutated_mod['func_8899'] = func_8899
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8926 = relay.var("var_8926", dtype = "uint64", shape = ())#candidate|8926|()|var|uint64
const_8927 = relay.const([[[-4,7,-4,8,-5,-6,6],[-9,8,3,6,7,5,6],[-1,3,5,-5,9,2,2],[4,2,10,3,-2,-3,-6],[7,10,-4,-3,-4,-7,-6],[9,-6,8,4,-10,3,-5],[-10,-9,-2,3,3,-4,-6],[2,-9,2,3,5,-7,-6],[4,-9,4,-1,6,-2,-2],[7,-7,-2,9,-4,-1,2],[2,10,-1,2,6,4,7]],[[-2,4,7,-10,10,10,-2],[10,10,-3,-10,9,10,3],[-1,1,9,5,-9,-2,4],[10,6,-9,-2,9,7,-3],[-5,-2,-9,2,-10,-4,3],[5,-10,5,-5,-4,-7,8],[-1,2,1,4,10,-10,4],[7,-1,-7,7,9,-6,-8],[6,-8,1,2,-7,4,2],[-8,-1,8,-9,-5,6,-10],[-8,7,6,-8,-9,-1,-7]],[[-4,10,-9,-8,2,-1,4],[2,-2,-2,-2,-6,5,3],[2,10,10,7,-2,-6,2],[5,9,-2,8,1,4,2],[-3,-7,2,-10,-9,4,3],[10,-9,1,-2,8,7,-10],[7,10,5,-4,5,3,-2],[-9,-5,10,6,4,2,-8],[1,10,9,9,-7,5,8],[10,-3,5,-10,3,-6,-3],[-9,7,-10,10,-9,7,4]],[[10,2,-2,-8,4,-3,5],[-6,-8,-1,8,4,-5,9],[-10,6,2,1,2,4,9],[-4,7,-3,6,-1,-7,2],[-9,4,3,1,-5,-1,4],[-4,3,9,10,4,-8,-2],[-10,-9,-5,-10,2,-4,-6],[5,-2,-4,6,6,7,-2],[5,-2,-8,5,3,-4,9],[-1,6,-6,4,5,3,-6],[9,5,-3,8,7,7,-1]],[[4,-10,6,10,2,9,-4],[7,3,9,2,5,3,5],[4,10,5,-5,-4,10,1],[-5,4,-4,-10,4,-2,1],[-3,-5,2,6,-5,-8,-6],[-7,10,9,-4,10,5,-7],[5,4,4,-6,5,4,1],[-9,10,3,7,-3,-6,-8],[-9,1,3,-3,-5,3,-10],[-9,1,-9,5,-3,5,-7],[1,3,-10,-5,10,-10,-8]],[[4,-2,-1,5,3,4,-6],[2,-2,-9,-4,-9,-2,8],[3,-4,3,4,-8,4,10],[-9,-8,2,-5,-3,9,-9],[-3,2,-10,7,-4,-7,-1],[-6,-10,-9,-8,-6,-1,-4],[-3,1,8,5,10,9,-2],[-6,7,6,-9,-6,6,-1],[-1,7,-6,1,2,9,-8],[5,7,5,-7,3,-5,-4],[9,8,-8,5,5,-7,-1]],[[-8,7,1,7,1,-6,-10],[3,4,9,3,6,1,-3],[-8,-7,3,2,-1,1,-4],[4,10,10,-9,-5,-6,10],[2,-10,-8,-9,-2,-7,9],[-2,-5,-7,-4,-8,-5,7],[3,1,-9,-8,-7,-9,5],[1,-4,-6,-9,-5,-1,-10],[-7,8,-2,-5,-1,9,-9],[6,-4,7,9,-10,-8,3],[-9,6,10,6,-6,-5,6]],[[-4,2,-9,8,-6,-1,7],[-1,-9,-5,-6,10,7,5],[-2,5,3,7,-4,8,-1],[-4,8,-9,8,3,-9,8],[-8,7,1,7,7,-6,8],[1,-2,-8,-2,9,-10,-4],[7,4,-4,-7,-3,8,8],[-3,9,6,8,-4,-10,10],[7,-1,-5,-4,-10,-3,5],[4,-7,-10,2,-10,9,-1],[-8,2,-5,2,2,9,8]],[[4,3,-9,-7,-9,-4,-9],[2,5,-3,5,-2,9,4],[-3,-2,-6,-6,-7,5,-2],[-4,3,5,4,-6,7,6],[9,8,2,10,-6,4,-9],[-1,9,4,-1,-1,6,-6],[3,-10,1,6,-7,3,5],[9,6,7,-5,-7,-1,-3],[-6,-1,-10,1,1,5,8],[-3,7,8,-2,-9,7,5],[-6,6,-7,1,10,-1,3]],[[-8,5,-1,3,-6,-6,2],[-2,-3,5,-2,-8,2,-9],[8,-10,-1,8,-7,-5,6],[9,5,4,2,9,4,9],[5,8,9,8,4,6,-8],[6,2,-3,9,-5,7,-6],[-1,-6,4,8,3,-5,-5],[-10,-2,9,2,-1,1,3],[-1,-8,6,9,-1,3,-6],[-1,-1,-3,7,-9,6,-1],[7,5,-3,-2,-1,8,9]]], dtype = "uint64")#candidate|8927|(10, 11, 7)|const|uint64
bop_8928 = relay.maximum(var_8926.astype('uint64'), const_8927.astype('uint64')) # shape=(10, 11, 7)
output = relay.Tuple([bop_8928,])
output2 = relay.Tuple([bop_8928,])
func_8936 = relay.Function([var_8926,], output)
mod['func_8936'] = func_8936
mod = relay.transform.InferType()(mod)
var_8937 = relay.var("var_8937", dtype = "uint64", shape = ())#candidate|8937|()|var|uint64
output = func_8936(var_8937)
func_8938 = relay.Function([var_8937], output)
mutated_mod['func_8938'] = func_8938
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8955 = relay.const(4, dtype = "int32")#candidate|8955|()|const|int32
var_8956 = relay.var("var_8956", dtype = "int32", shape = (8, 16, 5))#candidate|8956|(8, 16, 5)|var|int32
bop_8957 = relay.maximum(const_8955.astype('int32'), var_8956.astype('int32')) # shape=(8, 16, 5)
uop_8960 = relay.acos(bop_8957.astype('float64')) # shape=(8, 16, 5)
func_1376_call = mod.get_global_var('func_1376')
func_1380_call = mutated_mod.get_global_var('func_1380')
const_8993 = relay.const([-0.225563,0.893605,-0.074434,-3.031700,-1.199406,-9.366791,4.831591,-8.386430,-0.936375,5.489236,-3.537366,0.943038,-4.970998,7.643846,6.204525,-3.542651,-9.738670,0.063970,-9.328489,0.546015,7.716220,4.946530,-4.530856,-6.007503,-9.387802,5.057777,9.472665,3.967904,3.947448,-0.373099,-8.124136,-8.548973,-0.071372,-4.886795,1.358502,8.664352,9.924490,8.631438,7.809080,-5.635336,-9.495383,-2.474051,-1.508145,9.592871,0.049300,-0.386332,-4.836177,-5.012287,1.205684,0.537775,-4.724279,0.743283,-4.402290,-3.377483,-0.513432,8.511054,-3.403984,-5.422823,-0.576576,-5.889200,0.592831,0.227232,5.649561,8.778622,-9.967725,9.975741,3.012679,-6.848404,-2.567726,3.756533,-6.736199,5.570781,9.024129,5.407671,6.549209,1.785441,5.923756,3.971547,-4.299523,3.830128,2.510182,7.358354,2.140669,-8.117439,-3.814538,-9.707892,2.562738,-9.589350,6.144492,-8.252904,9.457551,-2.296509,-3.890818,-6.264308,-0.581478,-8.069024,-9.842897,-2.194036,1.771189,0.546118,2.435664,-9.846934,3.154170,9.480059,0.268779,-7.543367,8.201497,9.718043,-2.327696,-9.462362,0.506716,-4.294240,-3.511547,0.165276,-1.287959,-8.506977,-5.343571,-6.702377,9.450455,-6.121301,0.578621,4.731965,6.355956,-7.150771,-1.447340,-1.197998,0.967817,-5.461540,-9.615196,-8.579131,-8.067952,-7.618325,1.566449,0.082206,-7.887764,2.059779,-6.584769,-9.962014,5.848817,1.239456,9.238565,0.022311,-5.646032,-0.516074,5.406918,2.827907,8.522496,-1.207213,-2.614678,5.533774,-3.398046,-5.601376,-9.436310,-8.902053,-6.068762,3.446965,-5.264078,-9.455220,-6.348150,7.798413,3.050487,-6.240260,-0.945889,-0.946117,-2.822169,3.075246,-5.507149,7.216147,-6.087040,6.429161,7.808035,-1.172079,0.692140,-5.419763,5.948007,-4.950667,7.684445,-5.254654,1.925822,-8.536150,-0.456091,-2.192696,-7.838966,8.954564,-2.714054,3.081259,-7.736408,4.192952,-3.894973,6.206352,6.426771,8.654602,-0.655431,-0.166323,-9.440193,7.240327,-9.809587,9.660989,0.002561,6.711669,7.672236,1.323122,-8.185930,-5.485748,8.125483,-9.744971,4.906482,3.569864,7.428544,8.756322,-8.532518,2.130844,6.740071,6.108974,3.790470,-7.619487,7.334301,-3.997257,-9.319529,1.830837,3.531858,-3.548043,8.591325,-1.747364,2.332706,-1.532746,2.980269,-4.648031,-8.589635,1.563296,-3.959188,9.483512,-0.952134,0.825579,-2.212538,-9.545309,-2.231945,-7.664438,-6.999333,5.286225,-4.077732,8.930045,5.946237,-0.371157,-6.321727,4.377481,0.454714,-7.442231,6.238670,-8.727708,-6.581187,5.856711,0.680314,-3.222058,-4.259903,9.982696,8.555764,-2.849909,-3.904245,4.309745,4.175221,9.355348,0.195173,-9.920270,1.721333,-4.691336,6.792709,9.440076,9.371957,-8.301994,9.732583,-0.952023,-2.830426,5.203390,-4.714343,5.948271,4.588766,-9.117363,6.820577,2.401790,-7.129941,-9.589221,0.850316,-3.933278,-0.860223,0.722229,2.420244,-2.583603,-2.116571,-0.362814,-0.911318,-1.107497,1.192327,-8.552422,1.950026,0.686803,2.818254,7.935288,6.581780,9.523644,-7.041490,1.237668,6.505523,-0.123087,4.784911,-1.391285,-3.934413,-0.476172,5.345009,-6.050263,-7.774096,-2.098243,-0.174417,0.164921,-0.818803,8.363948,2.745769,-0.832478,-3.432298,-6.396030,9.063372,-6.486384,-1.146760,1.146154,0.174526,-4.533304,-8.517273,-0.027702,6.770317,-5.282788,-1.333677,-2.582297,0.881758,-9.077377,2.957351,7.683276,3.791848,5.614896,-0.594934,-0.536321,-6.412120,-0.247564,6.017747,8.887280,-5.874758,-5.366059,7.099352,-6.270203,5.834481,3.065242,9.320339,-6.675047,-0.654181,-3.624188,-6.837846,-6.535778,-6.982365,6.305959,7.480641,-1.780278,6.781729,0.205279,1.981643,2.993724,-6.401557,-5.165815,6.901237,2.223622,-6.057906,2.050882,-2.479981,9.837395,-6.679865,-9.162000,-5.754679,1.044312,-9.082441,-0.199276,-7.002881,-1.753424,-4.960874,-2.052184,9.876086,4.454119,-2.074933,4.353311,9.831965,2.033735,1.454949,2.931632,-9.131048,5.775910,2.800959,-9.656745,9.969886,7.608887,1.130571,-5.970608,9.506806,-4.147244,-5.128512,-9.468249,7.340548,7.665526,7.508834,-8.032026,4.987774,-3.305040,5.212883,-6.545060,-0.671264,0.538160,1.450025,-8.051718,5.421927,-9.324480,-7.494654,1.366799,-7.060563,7.083819,-8.239743,9.357173,4.277299,-1.013840,9.291686,-5.138882,-4.248691,4.987357,9.889509,-5.303875,8.482942,-9.863272,4.071169,1.380010,-7.714392,-0.502758,-9.224786,-5.747072,0.268501,-4.241763,1.024321,-1.115622,-8.403500,2.898537,-8.848009,9.233916,0.603016,4.466475,4.965919,-0.141520,1.315371,-2.598904,1.612254,-2.405400,-7.295440,8.119522,8.346525,6.090557,6.055727,3.971629,7.207982,5.364702,-2.236387,1.291719,3.644961,4.222470,-5.948616,-1.400478,-2.139766,8.878174,-9.207809,-1.269624,-0.546885,5.986724,-5.490194,3.786252,1.350981,-0.962649,-5.497811,-4.279348,-7.969284,-4.085063,6.436877,-9.088114,0.070979,-4.316858,-9.857810,3.213697,9.584402,-7.571960,4.025835,9.142098,4.105211,-7.717097,3.732695,3.204631,-8.985556,9.126890,9.490094,1.769373,8.941820,-1.979302,-5.834377,-1.357068,-4.890847,-1.462459,9.127810,9.652158,6.627414,-7.596257,-7.850953,-0.801668,0.669985,-7.115868,5.977120,-3.167798,-9.896371,-8.786206,-5.406008,-6.416722,-5.163686,8.045266,-9.238317,-4.899466,-0.900375,-2.295552,-0.027654,-7.140355], dtype = "float32")#candidate|8993|(528,)|const|float32
var_8994 = relay.var("var_8994", dtype = "bool", shape = (3, 104))#candidate|8994|(3, 104)|var|bool
call_8992 = relay.TupleGetItem(func_1376_call(relay.reshape(const_8993.astype('float32'), [11, 12, 4]), relay.reshape(const_8993.astype('float32'), [11, 12, 4]), relay.reshape(var_8994.astype('bool'), [312,]), ), 1)
call_8995 = relay.TupleGetItem(func_1380_call(relay.reshape(const_8993.astype('float32'), [11, 12, 4]), relay.reshape(const_8993.astype('float32'), [11, 12, 4]), relay.reshape(var_8994.astype('bool'), [312,]), ), 1)
output = relay.Tuple([uop_8960,call_8992,const_8993,var_8994,])
output2 = relay.Tuple([uop_8960,call_8995,const_8993,var_8994,])
func_8998 = relay.Function([var_8956,var_8994,], output)
mod['func_8998'] = func_8998
mod = relay.transform.InferType()(mod)
mutated_mod['func_8998'] = func_8998
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8998_call = mutated_mod.get_global_var('func_8998')
var_9000 = relay.var("var_9000", dtype = "int32", shape = (8, 16, 5))#candidate|9000|(8, 16, 5)|var|int32
var_9001 = relay.var("var_9001", dtype = "bool", shape = (3, 104))#candidate|9001|(3, 104)|var|bool
call_8999 = func_8998_call(var_9000,var_9001,)
output = call_8999
func_9002 = relay.Function([var_9000,var_9001,], output)
mutated_mod['func_9002'] = func_9002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8782_call = mod.get_global_var('func_8782')
func_8784_call = mutated_mod.get_global_var('func_8784')
call_9030 = relay.TupleGetItem(func_8782_call(), 3)
call_9031 = relay.TupleGetItem(func_8784_call(), 3)
output = relay.Tuple([call_9030,])
output2 = relay.Tuple([call_9031,])
func_9038 = relay.Function([], output)
mod['func_9038'] = func_9038
mod = relay.transform.InferType()(mod)
mutated_mod['func_9038'] = func_9038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9038_call = mutated_mod.get_global_var('func_9038')
call_9039 = func_9038_call()
output = call_9039
func_9040 = relay.Function([], output)
mutated_mod['func_9040'] = func_9040
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5164_call = mod.get_global_var('func_5164')
func_5166_call = mutated_mod.get_global_var('func_5166')
call_9159 = relay.TupleGetItem(func_5164_call(), 0)
call_9160 = relay.TupleGetItem(func_5166_call(), 0)
func_6739_call = mod.get_global_var('func_6739')
func_6741_call = mutated_mod.get_global_var('func_6741')
call_9163 = func_6739_call()
call_9164 = func_6739_call()
func_4987_call = mod.get_global_var('func_4987')
func_4991_call = mutated_mod.get_global_var('func_4991')
call_9165 = func_4987_call(relay.reshape(call_9159.astype('float32'), [5, 12, 3]), relay.reshape(call_9159.astype('float32'), [5, 12, 3]), )
call_9166 = func_4987_call(relay.reshape(call_9159.astype('float32'), [5, 12, 3]), relay.reshape(call_9159.astype('float32'), [5, 12, 3]), )
output = relay.Tuple([call_9159,call_9163,call_9165,])
output2 = relay.Tuple([call_9160,call_9164,call_9166,])
func_9175 = relay.Function([], output)
mod['func_9175'] = func_9175
mod = relay.transform.InferType()(mod)
mutated_mod['func_9175'] = func_9175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9175_call = mutated_mod.get_global_var('func_9175')
call_9176 = func_9175_call()
output = call_9176
func_9177 = relay.Function([], output)
mutated_mod['func_9177'] = func_9177
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6764_call = mod.get_global_var('func_6764')
func_6765_call = mutated_mod.get_global_var('func_6765')
call_9178 = relay.TupleGetItem(func_6764_call(), 0)
call_9179 = relay.TupleGetItem(func_6765_call(), 0)
output = relay.Tuple([call_9178,])
output2 = relay.Tuple([call_9179,])
func_9190 = relay.Function([], output)
mod['func_9190'] = func_9190
mod = relay.transform.InferType()(mod)
output = func_9190()
func_9191 = relay.Function([], output)
mutated_mod['func_9191'] = func_9191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6107_call = mod.get_global_var('func_6107')
func_6109_call = mutated_mod.get_global_var('func_6109')
call_9196 = relay.TupleGetItem(func_6107_call(), 1)
call_9197 = relay.TupleGetItem(func_6109_call(), 1)
output = call_9196
output2 = call_9197
func_9198 = relay.Function([], output)
mod['func_9198'] = func_9198
mod = relay.transform.InferType()(mod)
output = func_9198()
func_9199 = relay.Function([], output)
mutated_mod['func_9199'] = func_9199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8301_call = mod.get_global_var('func_8301')
func_8302_call = mutated_mod.get_global_var('func_8302')
call_9253 = relay.TupleGetItem(func_8301_call(), 0)
call_9254 = relay.TupleGetItem(func_8302_call(), 0)
var_9256 = relay.var("var_9256", dtype = "float32", shape = (13, 12, 15))#candidate|9256|(13, 12, 15)|var|float32
bop_9257 = relay.floor_divide(call_9253.astype('float64'), var_9256.astype('float64')) # shape=(13, 12, 15)
bop_9260 = relay.floor_divide(call_9254.astype('float64'), var_9256.astype('float64')) # shape=(13, 12, 15)
bop_9266 = relay.right_shift(bop_9257.astype('int16'), relay.reshape(var_9256.astype('int16'), relay.shape_of(bop_9257))) # shape=(13, 12, 15)
bop_9269 = relay.right_shift(bop_9260.astype('int16'), relay.reshape(var_9256.astype('int16'), relay.shape_of(bop_9260))) # shape=(13, 12, 15)
uop_9272 = relay.acos(bop_9266.astype('float64')) # shape=(13, 12, 15)
uop_9274 = relay.acos(bop_9269.astype('float64')) # shape=(13, 12, 15)
uop_9278 = relay.acosh(call_9253.astype('float64')) # shape=(1, 12, 15)
uop_9280 = relay.acosh(call_9254.astype('float64')) # shape=(1, 12, 15)
output = relay.Tuple([uop_9272,uop_9278,])
output2 = relay.Tuple([uop_9274,uop_9280,])
func_9288 = relay.Function([var_9256,], output)
mod['func_9288'] = func_9288
mod = relay.transform.InferType()(mod)
var_9289 = relay.var("var_9289", dtype = "float32", shape = (13, 12, 15))#candidate|9289|(13, 12, 15)|var|float32
output = func_9288(var_9289)
func_9290 = relay.Function([var_9289], output)
mutated_mod['func_9290'] = func_9290
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9295 = relay.const([[[-6.387114,2.749614,-1.923304,-3.209738,-8.916664,6.704128,7.033917],[4.719362,-2.187767,-6.346978,3.648761,-1.649801,0.486724,1.443759],[-2.962956,-4.062456,7.694379,-9.464532,-3.055017,6.834025,-9.728303]],[[1.718565,4.071217,1.291115,-9.242738,7.337425,9.567036,3.127211],[9.516974,2.207544,3.509931,-9.988503,2.523865,9.520814,2.999250],[-6.058198,8.626236,9.402624,-0.503499,-0.735232,8.679934,-3.184823]]], dtype = "float64")#candidate|9295|(2, 3, 7)|const|float64
uop_9296 = relay.rsqrt(const_9295.astype('float64')) # shape=(2, 3, 7)
output = uop_9296
output2 = uop_9296
func_9301 = relay.Function([], output)
mod['func_9301'] = func_9301
mod = relay.transform.InferType()(mod)
mutated_mod['func_9301'] = func_9301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9301_call = mutated_mod.get_global_var('func_9301')
call_9302 = func_9301_call()
output = call_9302
func_9303 = relay.Function([], output)
mutated_mod['func_9303'] = func_9303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7639_call = mod.get_global_var('func_7639')
func_7641_call = mutated_mod.get_global_var('func_7641')
call_9336 = relay.TupleGetItem(func_7639_call(), 0)
call_9337 = relay.TupleGetItem(func_7641_call(), 0)
func_7610_call = mod.get_global_var('func_7610')
func_7613_call = mutated_mod.get_global_var('func_7613')
const_9361 = relay.const([-9,2,9,-10,-6,10,-4,-9,4,-2,7,-8,-4,10,6,-10,-2,7,-4,2,-1,4,-3,-6,-8,-9,-4,-9,10,4,-3,-2,-9,-6,-7,-3,-3,6,9,-3,2,-9,9,-7,-9,4,7,7,-5,1,1,2,10,-8,-2,5,4,-4,-3,-1,-2,-4,-1,7,4,-9,3,-9,-1,-3,9,-9,-3,8,-4,2,-4,-6,-9,-10,-2,-8,-2,9,3,6,-1,6,10,2,3,-1,-2,1,-2,4,3,1,10,-9,-2,-6,-2,7,-8,-7,4,-7,6,8,2,4,-6,1,4,1,-4,1,9,1,8,8,7,10,7,5,-2,7,3,7,7,-5,5,1,3,-1,10,-7,-9,2,7,-7,6,10,-1,1,3,1,4,-1,-3,-10,-4,-2,3,8,3,10,9,-1,7,10,-7,-9,4,8,4,10,4,-2,-8,-9,-8,-8,-1,9,10,9,2,-8,7,6,3,-1,8,6,-4,6,-3,8,5,3,7,-5,-1,-5,-1,2,-7,-3,-6,2,3,3,4,2,-9,5,9,4,4,-8,10,-9,5,-5,-8,-3,5,-6,7,8,-3,9,4,-1,3,-1,1,4,-1,-7,8,-1,3,-1,5,6,4,-1,-9,5,4,-8,6,-9,3,-8,-5,3,6,10,-5,3,-2,-8,-7,-4,10,5,6,-5,-1,7,3,6,7,-3,10,4,8,-2,6,7,-8,6,-8,2,-5,5,-10,-7,5,-9,-4,7,-6,1,5,-10,10,-8,8,-8,-8,10,4,-4,7,-3,8,-3,9,8,1,8,5,-4,5,-5,4,10,5,6,1,1,9,4,9,3,-2,-5,-8,-2,-10,-5,-4,-2,-1,9,8,-1,-7,5,1,-7,-1,-1,-1,4,-10,6,4,-3,8,8,3,3,8,-5,7,1,-4,9,-5,-7,-1,-9,4,-3,5,8,-3,-9,10,8,-5,7,1,-7,8,1,8,6,3,4,-1,7,7,2,9,-5,9,6,-8,6,6,7,9,-5,3,2,6,-5,-7,-10,-9,3,-9,-7,1,-4,3,10,-5,6,-4,9,8,-3,-4,-1,10,-10,2,-5,-3,9,-10,-7,4,10,-2,8,-6,-6,5,-1,3,1,9,8,3,-7,6,8,9,-8,1,-2,-8,-7,-6,-8,-10,-4,-5,2,-2,2,2,8,10,-2,-3,-5,-3,-5,-3,-9,4,-3,-8,8,3,-7,-2,6,-2,-10,-3,5,-9,6,-5,-4,-8,7,-1,7,-7,-9,-1,10,3,8,6,1,-6,-7,2,2,-8,8,-6], dtype = "uint16")#candidate|9361|(495,)|const|uint16
const_9362 = relay.const([9.892507,8.788263,9.131724,-1.245437,8.095731,-8.443908,-6.000106,5.342858,-6.324297,4.468499,-5.351985,4.121429,7.655729,-5.190797,8.419245,-5.270991,-1.305076,-2.311584,-9.951345,0.325161,-4.009043,2.054013,4.021930,2.437382,-5.855277,-0.182766,0.405798,8.588124,-6.896669,-0.817453,-6.303706,-9.257609,-0.487324,-3.259944,5.779111,-3.243384,8.676112,-9.906708,5.021080,-2.707429,6.518824,-1.336377,1.624301,7.423761,6.813773,2.364393,3.077824,-6.289575,-7.290087,-5.527303,-4.672756,0.764068,-1.566513,8.550407,-2.272629,8.840452,-5.221421,-3.570291,-7.364077,6.190451,6.635480,8.159986,8.228027,7.658597,9.763130,6.735608,-0.770035,5.204406,0.903559,-4.645810,2.633860,5.767381,1.849088,7.996946,0.466808,-8.281052,3.418502,9.538314,0.093385,8.931225,-9.344250,9.622598,5.554843,4.738427,7.130334,-3.255423,-9.547266,-4.058351,-8.984411,2.918006,3.153097,-1.742793,9.194889,4.475382,-5.502875,9.245757,8.431749,-2.323954,-2.983182,9.242970,3.955925,-7.441869,9.354684,-0.259874,-3.764073,-9.734788,0.259398,-8.469748,-9.905006,2.113884,-4.390921,-1.446075,9.035622,3.476044,-8.214615,6.770908,-4.242724,0.545261,1.643522,4.528858,1.758009,5.087078,9.545353,-5.355576,1.581925,-2.369258,-0.816790,7.261936,9.109961,0.414840,-4.792447,-3.551117,-2.048699,-0.197095,1.937648,4.137848,8.004707,1.008042,9.795967,5.444784,6.693941,-6.859859,-4.403209,-3.252797,-0.426593,0.663579,-1.406425,-0.879858,-2.510213,-3.901702,-0.063983,-2.176803,-8.553738,-0.135272,6.173102,-7.428089,-0.880837,0.667954,2.155922,-7.441914,1.126091,-4.268669,0.702509,3.996158,3.825048,3.079761,4.603282,-3.217274,4.944594,7.055771,-6.773326,-7.770405,1.145827,4.936368,1.910406,-4.289881,9.194783,-3.354438,9.750430,-5.356242,-7.481815,4.368501,-8.102868,0.591719,-1.017736,-8.472957,5.549792,3.395747,-4.416176,2.143503,1.444066,1.895316,-5.984914,0.150877,0.801773,-5.794730,-8.074616,2.646745,0.969158,-3.667592,-2.406361,-1.295231,4.234013,-6.202134,-5.274810,6.658483,1.618798,4.047246,0.606668,-2.865114,-0.311129,-0.795682,-3.311669,2.254573,-9.810012,1.985732,1.440334,-0.027205,-7.510499,-1.396922,-0.112021,-5.695640,-4.572565,9.563742,-8.787748,-1.946646,3.526100,7.884431,8.319440,7.000905,7.495320,-4.170754,1.999385,2.003312,5.428493,-7.241787,-0.476138,3.956975,-5.732116,-3.716065,-8.758280,-2.928332,1.018720,9.431192,-8.184494,-5.125003,-3.119456,-0.885164,-7.175377,9.843480,-1.908240,2.295528,-5.482008,0.520359,-3.053271,0.812080,6.015042,-3.863241,-4.503629,0.658611,-2.461802,-1.712418,-3.194572,-8.129130,-0.159344,-2.146010,-7.225269,9.395230,-4.543659,0.405833,-4.740244,-4.825587,-2.695377,-2.052948,-3.453347,-2.211195,-1.956615,4.335915,2.736822,3.429406,7.165470,-0.495677,2.136939,-1.886068,4.429774,-8.403348,0.376500,8.008511,8.867089,-6.013627,8.768314,7.248769,6.849033,-5.037165,-3.826449,-8.315322,5.989076,6.643529,5.908614,-4.743236,-8.419507,-3.153214,5.124280,9.730224,-5.200508,4.981807,-6.162330,3.897450], dtype = "float32")#candidate|9362|(308,)|const|float32
call_9360 = relay.TupleGetItem(func_7610_call(relay.reshape(const_9361.astype('uint16'), [495,]), relay.reshape(const_9362.astype('float32'), [77, 4]), ), 3)
call_9363 = relay.TupleGetItem(func_7613_call(relay.reshape(const_9361.astype('uint16'), [495,]), relay.reshape(const_9362.astype('float32'), [77, 4]), ), 3)
output = relay.Tuple([call_9336,call_9360,const_9361,const_9362,])
output2 = relay.Tuple([call_9337,call_9363,const_9361,const_9362,])
func_9366 = relay.Function([], output)
mod['func_9366'] = func_9366
mod = relay.transform.InferType()(mod)
output = func_9366()
func_9367 = relay.Function([], output)
mutated_mod['func_9367'] = func_9367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6604_call = mod.get_global_var('func_6604')
func_6606_call = mutated_mod.get_global_var('func_6606')
call_9368 = relay.TupleGetItem(func_6604_call(), 0)
call_9369 = relay.TupleGetItem(func_6606_call(), 0)
func_3501_call = mod.get_global_var('func_3501')
func_3504_call = mutated_mod.get_global_var('func_3504')
const_9380 = relay.const([[8.441183,-7.437506,-9.006037,-9.383319,-9.428092,3.701268,3.606172,-3.779017,-1.333557,0.823000,-7.292696,-6.880428,0.059284,0.293596,6.012096,-4.765210,8.973890,0.565895,-4.425070,-4.925382,4.336422,-7.984609,3.690583,-0.079658,3.770247,-1.783006,-3.265689,3.208656,2.408411,-8.261993,-2.484144,6.644765,2.003067,2.397165,-5.754524,-3.212619,5.900169,-7.854608,2.594966,-5.147886,6.828189,-9.244009,4.166635,7.370963],[5.686650,1.289918,-0.790555,5.914220,6.674872,5.229605,6.002202,4.473888,-6.620744,4.863415,-1.512300,-2.010804,-5.982724,-3.931185,-2.502681,-3.252007,7.711626,4.511750,-8.955721,0.996809,4.622648,-3.885745,-3.349118,2.545682,0.608912,-5.379199,-4.173168,7.801601,4.136169,-7.862471,5.015948,0.176867,-1.274812,-3.780217,-9.495275,-5.876716,6.152241,-7.782439,-8.832703,-2.538031,-0.272062,-6.553645,-8.900245,3.894618],[5.833014,4.408659,9.357448,9.459624,-0.866600,-7.598401,4.986362,-0.323830,2.017582,-7.903287,7.488733,-5.791660,7.610638,-6.441150,-3.030792,0.758367,-7.473054,3.394662,-5.944131,5.719017,-0.150326,4.760699,2.643388,-1.643358,-2.142992,-4.382978,-5.798372,1.756945,9.698970,6.623718,3.255750,4.860428,5.318137,9.086703,3.701955,-6.462589,6.903740,0.318634,-5.711282,5.645358,-1.767155,-1.478243,-5.248828,-9.739163],[4.715064,-1.213296,0.648915,-7.206129,-2.581907,-9.884446,4.808491,0.741208,-1.437538,3.758616,8.449390,0.202261,-0.188990,-1.298451,6.349248,7.831755,-9.428999,9.667002,5.862183,-0.678217,-3.649479,-9.781948,-2.477128,-5.766426,-5.870042,0.539719,-8.306748,-8.806805,-4.350724,-7.497188,1.614110,-9.003289,3.546622,9.667938,-8.171441,-5.186099,-2.876774,-0.708831,-9.175248,9.334667,-1.029829,-5.644217,5.616696,3.369660],[7.386027,6.506590,8.986943,-8.150122,-7.074208,-0.586729,-8.146212,7.416460,1.677131,3.714823,-6.687310,-7.978818,7.222844,7.078124,6.365619,-6.258332,-9.161323,-6.343324,4.512337,-6.204825,-0.218211,-9.577904,8.551959,-1.544119,3.716355,8.690956,-4.226936,-9.225409,-4.130175,7.379734,0.521398,9.571862,2.507861,0.203485,-2.387966,-7.164777,-9.912195,9.939134,-9.014910,-5.081092,8.293614,8.967481,-4.064239,7.011517],[-9.843447,-6.372100,-5.607672,5.034486,9.465082,8.308128,6.434381,4.228471,-5.408976,1.500745,-7.804792,0.290266,7.177191,1.644767,-4.797279,0.432159,8.111718,-3.821170,4.561753,-8.266371,4.512235,-9.874564,9.361235,-1.192861,3.630780,4.979165,-2.685546,6.170978,6.034409,1.772626,-7.937910,-1.550736,-6.723049,9.011382,6.409443,5.604977,6.002376,3.857442,9.930031,5.337812,5.757567,-7.800403,5.387768,-0.654225],[-8.154197,-9.103888,-7.678287,3.029175,-2.452528,-8.339636,-8.762482,-3.361006,8.392009,-1.596506,1.083116,7.968794,-5.139140,-3.373748,-4.089923,3.509613,-7.529789,7.571284,-2.992095,-4.866903,2.501809,-9.814588,-7.769194,-7.558058,-4.852833,-2.960591,-4.348434,3.819164,6.826590,-2.440783,-4.730817,-5.509029,8.979669,6.457488,-1.239404,-7.959934,-2.770508,6.414756,2.790667,-4.794309,9.510770,-6.354997,1.764444,-2.095867]], dtype = "float32")#candidate|9380|(7, 44)|const|float32
call_9379 = relay.TupleGetItem(func_3501_call(relay.reshape(const_9380.astype('float32'), [308, 1])), 4)
call_9381 = relay.TupleGetItem(func_3504_call(relay.reshape(const_9380.astype('float32'), [308, 1])), 4)
output = relay.Tuple([call_9368,call_9379,const_9380,])
output2 = relay.Tuple([call_9369,call_9381,const_9380,])
func_9388 = relay.Function([], output)
mod['func_9388'] = func_9388
mod = relay.transform.InferType()(mod)
mutated_mod['func_9388'] = func_9388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9388_call = mutated_mod.get_global_var('func_9388')
call_9389 = func_9388_call()
output = call_9389
func_9390 = relay.Function([], output)
mutated_mod['func_9390'] = func_9390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8324_call = mod.get_global_var('func_8324')
func_8325_call = mutated_mod.get_global_var('func_8325')
call_9486 = relay.TupleGetItem(func_8324_call(), 1)
call_9487 = relay.TupleGetItem(func_8325_call(), 1)
func_6077_call = mod.get_global_var('func_6077')
func_6080_call = mutated_mod.get_global_var('func_6080')
var_9504 = relay.var("var_9504", dtype = "uint16", shape = (495, 1))#candidate|9504|(495, 1)|var|uint16
const_9505 = relay.const([1.265818,1.297863,-1.516201,-6.511201,-7.192922,-6.951506,-3.135598,6.882949,-7.232485,-3.943017,0.934841,0.668103,1.274263,-2.815576,7.631782,-1.626993,9.080162,-2.361453,-5.668492,-7.823703,-8.049272,-9.096261,3.956576,-1.977231,-6.365386,-6.358891,6.475525,2.832987,-0.945130,8.212782,-1.559077,-7.832187,9.225243,0.431002,4.384468,0.757516,-2.580117,4.882435,4.573707,7.022467,-5.966760,6.174202,-7.891549,-6.074134,-0.138781,-1.211520,-9.620029,2.002253,1.824239,0.421220,-1.239584,-1.596674,3.711071,-4.252557,7.983079,-5.895059,6.187475,9.014371,8.954109,-8.179168,5.455139,-2.264105,1.559786,-1.639742,-6.378188,-8.601588,-4.596252,3.775602,-7.308525,-9.846417,-7.603677,1.593467,-9.925169,5.749669,-3.058661,3.442391,-8.421872,2.576883,8.502461,-9.677392,-3.545606,-4.556735,7.592921,-5.568397,-3.710361,-6.217937,2.622043,-6.879587,-7.606099,2.684797,-9.198812,4.812259,-2.323434,-5.058584,-1.207440,5.842992,3.698318,6.379751,-6.528217,-2.161985,-8.208965,0.702977,-8.762705,9.781697,1.780757,-7.784380,1.177662,-6.486840,-8.626327,-8.497881,9.646373,8.464612,6.188430,2.436516,-7.122820,-7.958104,-7.958466,2.734614,-5.634898,-3.104094,5.693970,8.391843,-6.012871,0.824107,-3.249615,8.583308,2.429855,1.990463,9.124906,-1.581931,-0.519258,-5.658440,-0.064032,-6.748473,-2.602023,-3.369496,5.438224,-2.847280,8.928372,-1.856419,0.284881,0.552272,1.951400,-9.124985,-1.714990,-3.402556,6.146772,6.852420,-8.992578,-1.955987,-0.848272,6.922772,-5.873490,7.404840,1.666716,-7.116072,8.577474,5.865909,-9.236684,9.129330,2.794274,8.353884,-1.501243,-5.521383,-2.002025,5.903274,-5.179591,-9.254745,7.654159,-4.630384,-0.858253,2.844794,1.925881,-2.980723,-1.254783,-7.289512,5.604669,5.603041,-5.690177,1.530916,-8.615378,-5.400235,8.716653,-7.701277,-2.669788,4.692507,1.477253,0.901855,1.857111,-1.925534,0.746447,7.176660,-6.052680,7.107992,1.423654,-4.294694,1.285955,-4.802509,1.385623,5.395440,9.998000,-9.620268,-9.810340,0.221407,1.174219,6.788823,-3.937861,-8.617699,8.697649,-6.570740,-2.454711,0.812730,6.931459,-2.759687,-5.773028,-8.137361,-4.541210,-4.635064,-1.360559,-1.925865,3.227841,6.167956,5.570544,-0.511388,8.776097,9.412244,7.963881,2.088649,-7.298976,-9.861755,-2.805372,-3.776429,6.096148,7.130066,0.909831,-7.885159,8.560862,-3.204978,1.007103,-2.275044,1.070703,-1.276523,-8.857241,3.596992,4.963838,4.327832,7.952478,-5.096771,-1.981503,-3.069280,1.978945,-3.240193,-8.571025,1.680823,3.801652,-5.560988,8.010374,-6.337439,2.507595,-0.291834,2.725623,-4.280249,-2.005193,7.933115,-4.612883,-9.559044,-4.941856,-6.694295,7.702666,-6.547672,3.087839,-6.775175,3.017916,-9.046007,-5.211610,9.557244,-8.904101,-2.746555,-6.340433,6.842130,-2.119465,3.544104,-8.872283,1.889539,6.571617,6.785449,5.816982,-3.541714,-2.978833,3.290541,8.054933,-9.337723,-9.198032,-3.678898,-9.652361,2.443440,2.223734,-1.645758,-9.843800,-1.344940,1.026988,3.834133,7.836945,-7.550266,-3.197592,-5.046064,-2.360369,-3.817865], dtype = "float32")#candidate|9505|(308,)|const|float32
call_9503 = relay.TupleGetItem(func_6077_call(relay.reshape(var_9504.astype('uint16'), [495,]), relay.reshape(const_9505.astype('float32'), [308,]), ), 5)
call_9506 = relay.TupleGetItem(func_6080_call(relay.reshape(var_9504.astype('uint16'), [495,]), relay.reshape(const_9505.astype('float32'), [308,]), ), 5)
output = relay.Tuple([call_9486,call_9503,var_9504,const_9505,])
output2 = relay.Tuple([call_9487,call_9506,var_9504,const_9505,])
func_9511 = relay.Function([var_9504,], output)
mod['func_9511'] = func_9511
mod = relay.transform.InferType()(mod)
mutated_mod['func_9511'] = func_9511
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9512 = relay.var("var_9512", dtype = "uint16", shape = (495, 1))#candidate|9512|(495, 1)|var|uint16
func_9511_call = mutated_mod.get_global_var('func_9511')
call_9513 = func_9511_call(var_9512)
output = call_9513
func_9514 = relay.Function([var_9512], output)
mutated_mod['func_9514'] = func_9514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7471_call = mod.get_global_var('func_7471')
func_7473_call = mutated_mod.get_global_var('func_7473')
call_9518 = relay.TupleGetItem(func_7471_call(), 2)
call_9519 = relay.TupleGetItem(func_7473_call(), 2)
uop_9533 = relay.sinh(call_9518.astype('float32')) # shape=(1, 12, 15)
uop_9535 = relay.sinh(call_9519.astype('float32')) # shape=(1, 12, 15)
output = uop_9533
output2 = uop_9535
func_9542 = relay.Function([], output)
mod['func_9542'] = func_9542
mod = relay.transform.InferType()(mod)
mutated_mod['func_9542'] = func_9542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9542_call = mutated_mod.get_global_var('func_9542')
call_9543 = func_9542_call()
output = call_9543
func_9544 = relay.Function([], output)
mutated_mod['func_9544'] = func_9544
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9591 = relay.var("var_9591", dtype = "float64", shape = (4, 4, 3))#candidate|9591|(4, 4, 3)|var|float64
const_9592 = relay.const([[[0.588458,-9.779224,4.363096],[2.234509,8.309750,2.329233],[3.090851,-8.969852,-1.510292],[2.223119,-6.870557,-8.782383]],[[-0.954560,9.802165,-0.882170],[5.688286,5.619241,2.953166],[8.818444,2.654993,4.409329],[-8.657666,-8.504907,-5.622218]],[[-8.398025,-6.728542,-5.819165],[-7.586887,-6.172620,0.248499],[-1.678636,5.083328,-6.303728],[-5.733027,7.429610,-3.506688]],[[-6.502435,-5.106587,-0.500123],[-2.023627,-6.941056,1.958940],[1.011205,9.133412,4.148287],[9.004573,-1.821071,1.550330]]], dtype = "float64")#candidate|9592|(4, 4, 3)|const|float64
bop_9593 = relay.less_equal(var_9591.astype('bool'), relay.reshape(const_9592.astype('bool'), relay.shape_of(var_9591))) # shape=(4, 4, 3)
func_5971_call = mod.get_global_var('func_5971')
func_5972_call = mutated_mod.get_global_var('func_5972')
call_9601 = relay.TupleGetItem(func_5971_call(), 1)
call_9602 = relay.TupleGetItem(func_5972_call(), 1)
func_6802_call = mod.get_global_var('func_6802')
func_6804_call = mutated_mod.get_global_var('func_6804')
call_9603 = relay.TupleGetItem(func_6802_call(), 0)
call_9604 = relay.TupleGetItem(func_6804_call(), 0)
uop_9609 = relay.rsqrt(var_9591.astype('float64')) # shape=(4, 4, 3)
func_7501_call = mod.get_global_var('func_7501')
func_7502_call = mutated_mod.get_global_var('func_7502')
call_9614 = relay.TupleGetItem(func_7501_call(), 1)
call_9615 = relay.TupleGetItem(func_7502_call(), 1)
uop_9618 = relay.tan(uop_9609.astype('float64')) # shape=(4, 4, 3)
func_8143_call = mod.get_global_var('func_8143')
func_8144_call = mutated_mod.get_global_var('func_8144')
call_9620 = relay.TupleGetItem(func_8143_call(), 0)
call_9621 = relay.TupleGetItem(func_8144_call(), 0)
uop_9624 = relay.erf(uop_9609.astype('float32')) # shape=(4, 4, 3)
func_3115_call = mod.get_global_var('func_3115')
func_3118_call = mutated_mod.get_global_var('func_3118')
const_9629 = relay.const([[7.268750,6.389602,-6.976265,0.870265,3.722347,6.014432,1.955350,7.392185,6.281053,-3.010123,-4.769674,5.033165,3.708591,-6.252783,7.184483,1.251564,8.934629,2.696820,0.331910,-5.753576,-6.636630,-8.919282]], dtype = "float64")#candidate|9629|(1, 22)|const|float64
call_9628 = relay.TupleGetItem(func_3115_call(relay.reshape(const_9629.astype('float64'), [1, 2, 11])), 0)
call_9630 = relay.TupleGetItem(func_3118_call(relay.reshape(const_9629.astype('float64'), [1, 2, 11])), 0)
output = relay.Tuple([bop_9593,call_9601,call_9603,call_9614,uop_9618,call_9620,uop_9624,call_9628,const_9629,])
output2 = relay.Tuple([bop_9593,call_9602,call_9604,call_9615,uop_9618,call_9621,uop_9624,call_9630,const_9629,])
func_9637 = relay.Function([var_9591,], output)
mod['func_9637'] = func_9637
mod = relay.transform.InferType()(mod)
var_9638 = relay.var("var_9638", dtype = "float64", shape = (4, 4, 3))#candidate|9638|(4, 4, 3)|var|float64
output = func_9637(var_9638)
func_9639 = relay.Function([var_9638], output)
mutated_mod['func_9639'] = func_9639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8830_call = mod.get_global_var('func_8830')
func_8831_call = mutated_mod.get_global_var('func_8831')
call_9641 = relay.TupleGetItem(func_8830_call(), 0)
call_9642 = relay.TupleGetItem(func_8831_call(), 0)
output = call_9641
output2 = call_9642
func_9646 = relay.Function([], output)
mod['func_9646'] = func_9646
mod = relay.transform.InferType()(mod)
mutated_mod['func_9646'] = func_9646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9646_call = mutated_mod.get_global_var('func_9646')
call_9647 = func_9646_call()
output = call_9647
func_9648 = relay.Function([], output)
mutated_mod['func_9648'] = func_9648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5736_call = mod.get_global_var('func_5736')
func_5737_call = mutated_mod.get_global_var('func_5737')
call_9657 = relay.TupleGetItem(func_5736_call(), 0)
call_9658 = relay.TupleGetItem(func_5737_call(), 0)
output = relay.Tuple([call_9657,])
output2 = relay.Tuple([call_9658,])
func_9662 = relay.Function([], output)
mod['func_9662'] = func_9662
mod = relay.transform.InferType()(mod)
mutated_mod['func_9662'] = func_9662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9662_call = mutated_mod.get_global_var('func_9662')
call_9663 = func_9662_call()
output = call_9663
func_9664 = relay.Function([], output)
mutated_mod['func_9664'] = func_9664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5156_call = mod.get_global_var('func_5156')
func_5157_call = mutated_mod.get_global_var('func_5157')
call_9724 = func_5156_call()
call_9725 = func_5156_call()
func_7526_call = mod.get_global_var('func_7526')
func_7528_call = mutated_mod.get_global_var('func_7528')
call_9740 = func_7526_call()
call_9741 = func_7526_call()
func_7526_call = mod.get_global_var('func_7526')
func_7528_call = mutated_mod.get_global_var('func_7528')
call_9743 = func_7526_call()
call_9744 = func_7526_call()
const_9749 = relay.const([[[-9.939965,2.670202,-2.447549,-9.867726,-7.164321,-7.024058,-8.254453,-5.389458,8.075331,7.970045,4.783777,5.268785,3.752858,-7.648124,-6.803310],[-7.227467,-2.238041,7.169678,-5.116165,0.575141,-2.649777,-2.946795,-9.774826,-2.651530,-1.746034,0.005175,-0.075784,6.498541,8.855624,-8.253842],[9.820724,-1.148691,-1.311331,7.113024,7.303298,7.051779,-4.615568,-3.746651,7.339570,-4.404965,-4.812603,6.060138,-4.254700,8.353973,-5.763218],[4.588268,-0.877985,1.992485,8.684288,-8.656083,-7.702135,-2.550456,0.223134,3.778298,-7.220268,-1.919344,0.565409,5.843316,1.594619,-2.331640],[-0.571593,2.184058,1.975571,-2.428155,8.528422,-5.706500,-9.931691,-9.451680,1.826110,-3.086803,6.002062,6.568452,-5.250598,7.357476,4.847949],[8.928771,6.132369,-2.148800,-2.236087,-6.930381,7.011860,7.413639,4.788189,-6.487453,6.870919,-9.318940,9.250571,-4.999369,-1.628530,5.604428],[2.012801,-5.598364,-5.159261,0.989464,7.853428,-3.656922,-9.605102,-9.300790,-3.361144,1.835710,-1.633651,-2.806132,7.412337,3.145303,-0.580805],[5.360622,-3.380312,7.272588,-3.305048,5.634844,-5.226861,0.939061,3.744244,-9.586640,-3.635545,7.964623,-6.294797,-6.826933,-1.391853,5.118887],[4.368488,-3.361157,-7.518092,-5.691947,7.209096,-5.840244,9.044905,-2.124724,-5.625735,-5.126693,-3.899392,0.243909,-0.319892,-6.753007,6.059071],[9.251807,-6.628496,-4.733824,4.321828,-6.750115,-3.062282,-7.003976,-4.567838,-2.715092,-9.983584,7.851744,6.288854,6.548281,-2.366957,-8.336776],[4.724299,-2.768985,-0.532090,7.059725,9.869300,-7.181247,-7.053654,-2.151964,1.730780,8.537905,9.010585,1.065073,5.950672,-6.744113,-6.674363],[-2.890396,7.788165,-5.600168,9.451661,5.576047,3.397586,2.885449,3.735009,-7.682597,-0.716675,-4.988204,-4.673011,-0.086099,-6.656337,0.449573]],[[-0.016126,-1.370847,6.651841,0.506263,-9.614401,3.209639,-3.983077,-6.388989,-5.662504,-8.073865,-9.472325,0.352021,-8.647721,1.913919,-5.120322],[-3.785225,-3.482747,-3.099374,2.660735,-4.251059,3.018647,1.348812,-6.767167,3.115365,-5.458721,-5.996710,-3.079188,9.737043,7.698351,4.962967],[6.833036,-3.726467,-6.169943,3.933338,-5.289391,-2.880778,-9.986050,0.579695,2.242155,4.000739,4.345687,-1.446360,1.021191,-9.567424,-5.811383],[0.175772,7.963504,1.959324,-9.952505,8.639006,9.217794,-1.288852,0.077905,-8.008039,-1.413868,-8.976346,5.390201,3.150337,-3.917247,-8.701276],[4.483905,8.949905,7.783819,3.028555,1.913062,8.509604,-7.976319,-3.764538,7.772951,-4.986853,1.517769,9.741601,6.209880,4.321964,4.568056],[0.048154,0.132179,2.851498,7.154176,0.543149,-0.976987,9.388846,-5.912504,-5.071439,2.068181,-1.159253,-6.698232,5.869818,-3.700865,6.594308],[-6.431909,1.413027,3.003466,2.836073,3.689381,-8.341792,5.700541,-7.705058,7.989225,4.791035,3.654585,2.892281,-6.537228,1.688217,-2.541645],[-9.404118,0.230625,-5.020033,-9.616985,-3.747240,-3.268654,5.688317,-7.779445,-1.305095,3.317794,-5.390603,0.707230,-6.303468,9.388245,-4.756558],[-1.674593,-8.616864,-8.484991,4.448069,-0.196517,-3.700249,-0.153637,-7.615837,8.075403,-2.124024,7.327910,9.085776,0.045701,-9.215814,-9.667923],[-5.287077,6.893631,-1.546679,0.503097,-0.545212,6.899228,9.878055,6.007071,4.786869,-4.866628,2.211768,-3.905641,-8.623749,-4.281860,-1.509005],[5.893645,6.032789,-7.851969,0.309637,1.758007,5.891148,-5.143753,-5.708234,0.593058,5.977840,-4.315118,8.168261,5.300322,-4.171448,-4.543107],[-9.157411,2.619950,-7.290808,-8.788110,5.264949,1.089803,-4.279333,4.171850,6.384743,-1.903696,-3.204955,0.073449,-7.291133,7.827618,-9.675826]],[[2.710551,-2.020104,9.958355,-2.709643,-3.124520,3.568355,0.141608,9.496290,8.902316,1.576815,7.894213,-4.374447,7.400132,-9.393649,7.248277],[-9.137925,1.176163,9.018958,5.318523,-0.109469,1.308628,3.864323,-6.876792,-2.577913,-6.988382,5.863889,4.973607,-3.719831,-0.061576,-5.684002],[-7.231883,4.762745,7.953462,-2.028809,-5.223352,-5.866932,-8.812933,-1.878953,-8.730392,-7.707906,-7.492276,8.615993,6.638001,-1.352980,-9.182153],[4.269463,5.998691,-9.339325,7.125872,1.343805,-8.197005,-6.907667,-2.704468,4.054733,7.002856,9.582672,0.602254,0.677356,-3.595547,8.720005],[-8.991068,9.919963,1.443253,-9.527581,-6.674634,-0.421075,5.375281,-3.340912,-2.258755,6.103970,8.508627,2.572642,7.201829,-3.456978,2.731579],[-0.243231,-4.926551,7.159068,1.081448,5.299390,-0.594473,-1.593914,-6.938510,0.056841,-6.397670,-9.610579,4.255662,0.096936,-8.428890,-4.602524],[4.173947,-4.282002,5.044396,1.680589,1.134709,-0.472985,-5.768416,-1.933477,4.806811,8.147574,-9.518224,-9.722225,-3.880377,-5.597482,7.744723],[-2.257307,1.698542,-5.884630,-9.891030,4.398328,-8.232281,4.883142,8.957382,8.872274,2.657612,-8.785449,-6.157520,2.556194,-8.122523,-3.922750],[0.031172,-3.789521,7.794178,2.979975,-3.719696,1.760675,-8.445803,-0.872167,-9.079938,2.840792,-5.230873,5.953366,-1.317578,2.058262,-6.660489],[-5.816966,-7.787319,-9.670907,8.732989,-4.396213,5.007840,1.991090,-2.105031,8.537263,8.817232,8.415811,-1.167352,5.409411,8.322827,-9.385771],[-2.767106,9.152531,4.015782,-5.389216,2.288507,8.138458,-1.716767,1.843682,-6.617654,-2.414958,9.902499,8.186934,-8.872023,-6.048709,-0.420340],[-5.863885,4.589906,1.941697,1.514207,9.001101,-8.048302,9.602936,0.232392,-6.300987,9.897327,-8.282081,-5.053352,1.216507,-5.990727,-7.919086]],[[-1.562111,5.145254,4.622343,-6.286869,-8.353173,2.626971,-9.706572,5.383118,3.148883,7.939592,-8.543297,0.297390,-9.502631,-0.826910,-5.670621],[7.687437,1.739465,-4.396748,5.341859,8.329843,3.809735,1.080485,-6.229469,9.113049,-7.287737,-3.519343,-3.706029,9.406093,-6.102389,8.355097],[-7.089775,6.381595,8.540050,-4.732618,3.710020,-7.599061,1.028887,-7.804039,2.891984,5.306083,8.655937,-5.378501,-7.706305,-0.027304,0.020074],[8.120427,-2.301982,2.732818,5.798201,-8.291771,-9.353314,3.591336,-4.347624,0.655380,1.378981,5.047262,-4.709853,4.791416,6.878162,-9.237367],[6.254038,2.949651,-0.696729,-5.365921,-6.376482,-0.213686,7.413571,-9.863391,-2.738718,2.716555,2.821131,-9.383384,4.802687,-4.817680,6.807608],[9.932126,-7.742526,-5.652756,-7.230640,-6.371325,2.728501,1.980148,-4.837391,4.775126,3.881502,7.283808,9.051789,-0.094835,7.885862,-2.955715],[7.564937,2.066194,-4.549151,1.782240,-6.612653,3.086429,-8.696167,1.978841,2.535820,9.133879,7.788104,5.192756,-3.380326,7.603499,-9.953445],[-0.238378,-3.801733,8.451062,1.587741,2.027534,5.277503,-5.524239,2.405331,-4.405033,-5.352283,4.901744,-3.068733,-8.495991,-8.368441,-6.319930],[0.150167,0.496822,3.670441,-3.144335,9.205538,-8.615597,2.193838,-0.628171,-9.099998,6.931867,8.861999,7.800967,5.947884,-8.038172,7.804091],[-3.990654,-7.699705,-2.866428,-8.179427,-8.846405,-0.769951,-1.748823,6.445929,-9.497619,-9.647333,-8.013321,-7.785422,4.897176,-6.318005,-0.092357],[7.015746,-3.173503,-9.471809,5.435568,-4.706126,-9.483957,-2.046548,-0.825657,0.236906,-5.961128,-6.027140,7.579049,-3.620851,-6.928654,9.669497],[-3.421302,5.103972,-1.106371,-6.163699,-6.641591,8.264013,8.284901,-4.896823,-4.105189,5.312581,3.365567,0.964833,-5.700916,1.850204,-2.406006]],[[0.843737,0.955511,-9.877102,-9.795703,3.617520,0.595386,4.398459,0.213445,-1.955178,-7.857496,-8.991017,0.925527,-7.454487,5.149014,-4.458182],[-7.778875,-9.552719,-4.554256,8.688128,5.300351,1.747960,-6.880231,-1.163092,-2.982581,5.062980,-9.370985,-9.517881,9.109051,4.142633,4.675901],[8.606078,-3.789103,7.801737,-3.296313,9.234040,-8.568241,-6.207215,-5.037263,-0.863321,1.936352,8.564467,4.220979,1.332428,-2.702064,0.952693],[-8.050676,-9.745251,-8.493478,2.966825,-9.806369,8.582464,0.448676,4.787075,-3.631025,8.562979,5.410210,1.698922,-4.739934,-1.971492,5.795057],[-5.729123,-4.039165,-2.176108,9.234065,7.596742,4.950990,-7.314539,-5.782933,-9.270877,2.136036,-1.552938,-2.739042,8.343090,-0.806928,3.709866],[5.114599,5.241910,-9.424923,-7.788890,5.138453,-2.881284,-0.735724,3.355600,-6.591168,3.135061,6.012733,6.365145,3.671675,8.498433,-2.301604],[-5.384122,-3.762812,7.655808,4.005597,-5.374294,5.205234,3.040939,8.656052,-6.107654,-6.729288,3.987798,0.657131,2.574533,0.830916,-8.765030],[-9.065301,5.278252,-2.988025,6.957183,5.425106,-6.744492,-6.818779,-1.392304,-3.240890,-8.827219,0.647495,4.758558,-3.029361,2.291555,4.986936],[6.930969,-0.698956,-7.615319,3.686229,0.943484,-4.763397,8.236248,0.195951,-2.365152,-1.365360,2.289480,2.541803,-3.491698,0.543522,9.668130],[3.591552,-6.320806,-2.698837,-8.561470,5.588747,-6.645590,6.785910,-0.637135,9.127874,-5.231019,7.335525,3.976969,-8.146818,-1.089762,-2.414430],[-3.912769,-9.376055,4.405718,-4.618389,-9.125580,6.244672,7.721868,-2.988823,-9.531567,-7.846880,9.873854,-6.279559,-3.615920,-5.240318,-4.208449],[2.710316,-0.387422,-8.650116,-6.920860,2.023811,-1.718740,2.755383,0.213791,4.873867,8.618837,0.543997,-4.685445,-2.708161,-2.737073,7.760192]],[[3.265989,-2.066135,2.347039,6.437670,9.832403,-7.418920,-9.574201,2.150027,-5.390948,1.043047,-2.358002,-0.543206,-2.087883,-7.616703,-5.191903],[9.033165,-7.819354,2.036248,-0.780213,7.941323,-5.740265,2.558386,8.083720,-5.715826,-8.285586,3.076554,-5.562812,7.210431,-1.176799,-6.963534],[7.635817,-9.443036,3.686496,1.735241,4.458258,3.964850,4.271517,-3.452935,2.673148,-7.581914,-2.306774,-5.260353,6.508317,8.310801,1.825587],[-2.055327,1.622013,-9.036384,5.626964,2.143089,-0.636741,-3.872056,9.303625,-1.566409,1.313994,-8.935892,9.499285,4.805551,-7.388749,-8.725757],[-4.938242,1.655636,-6.448648,-1.227959,5.908868,-6.557676,-1.507271,0.494834,5.117450,-8.300656,-8.664912,-9.025770,9.842919,5.003712,-0.513811],[-8.026174,-6.779375,-2.640892,3.387580,-6.938401,-9.602838,1.947010,0.877857,8.871097,-5.809635,-4.387752,-6.506526,-5.530825,-6.652254,-4.507759],[-0.759960,1.478614,-1.314185,3.632770,-7.015635,-8.822986,-4.064210,9.640701,3.006593,-6.221792,-6.090051,-2.914456,0.811809,-5.457124,-2.762241],[-1.550648,8.777590,-3.703103,7.170688,-5.382523,8.381531,3.242904,-7.106605,-3.615401,1.394535,2.955894,9.491638,-7.015348,3.019543,-8.507456],[3.106141,-3.477512,-2.713692,-0.423467,-5.980320,4.927436,-4.751001,7.873173,7.176809,-0.303576,-5.520541,-0.125588,9.559334,-7.885062,1.994584],[6.551332,2.037720,-7.809361,-4.069593,7.507653,3.913665,-8.883104,6.076653,-4.128754,5.679338,0.657902,-6.086458,8.986668,9.508528,-3.706060],[-7.595926,3.505058,8.981201,3.897887,8.394302,-2.229264,9.614630,-8.500699,-4.344719,9.429524,8.727550,7.854437,-9.399992,1.139391,-6.157094],[1.758094,3.299150,-7.997588,-0.912445,-9.324394,9.334978,-0.051216,-1.325143,4.831679,6.841212,-4.535704,-6.866331,-1.637763,7.817006,-2.640637]],[[-9.896262,-9.442890,-5.884828,-2.280550,2.643874,-6.026104,-4.307619,9.505525,2.033678,8.027388,-0.381850,2.496788,-0.509949,9.237385,-6.718684],[8.938766,9.875369,-9.302954,9.389853,-0.218389,-4.820414,4.144469,9.592583,7.444649,2.440886,0.650836,-2.390603,-7.863786,8.401260,-7.289248],[2.743805,-4.943055,-4.893043,6.623814,3.138306,-0.393235,-4.593460,-1.472955,-6.434900,6.899856,9.685333,1.064282,4.829010,-9.891581,-6.662503],[-8.368164,-4.695405,-6.341318,-2.410684,-5.028212,-0.566261,9.239561,-7.305213,-0.876425,8.691739,8.000808,6.422422,-5.154334,-5.430772,7.225074],[-7.065420,7.706702,-1.928397,7.242469,8.509095,-7.721452,-6.944486,-6.414207,-9.134055,2.178782,-3.165369,-1.230904,-5.441370,5.005857,3.229330],[3.091150,-1.451235,-9.002307,-9.186968,6.612351,-0.809113,8.506110,9.474469,5.742099,7.248150,1.505629,4.711629,3.267560,8.766697,0.703165],[0.563049,-5.554826,3.104379,-0.600576,-6.861080,7.844347,3.550946,6.799816,-5.162222,-4.121455,0.393958,-6.272730,7.381948,-5.418369,-4.144800],[4.461748,-3.992669,3.607538,5.560682,-2.484665,-5.470897,-6.815177,-4.750658,-5.513171,-4.285792,-9.286199,3.390980,6.040996,-9.255722,4.394587],[3.083695,-5.211046,-9.737316,3.516322,3.909389,6.825905,8.356666,-0.853092,7.259009,-3.260564,0.650794,0.703651,6.840852,-5.071300,0.716617],[-8.276030,-0.513018,-7.698763,7.663211,-7.370273,0.815499,-5.335709,6.261875,3.394192,0.251404,2.215327,-3.795311,4.441072,0.450806,-1.370236],[1.730384,5.857766,6.528907,-5.631511,3.940923,-0.833348,-7.996369,6.232833,8.347420,-5.208626,-5.684073,4.137183,6.599095,4.817934,-9.136000],[9.413455,-7.362197,-6.047647,-0.159675,-9.788589,2.520223,7.469088,4.168457,-2.352219,0.121877,-7.154317,-5.767749,-2.894010,-4.821727,-8.229746]],[[5.816552,6.933691,-9.415730,-1.048790,-6.598026,-7.113917,2.581937,-0.180082,-6.240259,7.823167,3.390178,5.834548,6.577292,0.340318,2.440387],[1.000683,8.518273,8.282014,-6.722672,3.180814,-2.482336,-4.494550,5.778624,7.582897,7.742242,8.394467,-9.639339,-6.646008,-8.420132,9.143245],[3.344540,7.887110,9.235375,-8.312171,-7.013612,5.984783,1.017543,-5.584899,-6.973389,-9.876257,-3.992808,-4.313639,9.779319,-4.385524,5.910313],[7.748443,-4.673936,1.837015,4.527698,7.541487,0.230593,3.010772,1.814074,3.616787,1.524216,6.597810,4.082885,-2.061047,7.154552,9.853886],[-0.030826,1.699581,2.558395,6.311771,4.997910,-0.854721,8.362814,1.397715,0.986268,-2.760120,0.601487,-2.338075,8.107652,3.441992,3.476175],[5.795870,7.323297,9.063044,-4.401524,-0.824053,4.413720,-1.451992,-9.020188,8.714344,9.344326,-7.050515,-0.230209,0.993936,5.308906,-3.764107],[7.584890,-6.103578,-8.808729,9.641192,-7.397279,-0.827225,-8.634482,-7.402557,8.991333,-7.318746,9.330945,6.595111,4.150349,-6.875135,8.328059],[-3.837602,-3.515198,3.485623,-4.135599,9.876370,-6.244157,-1.739740,2.161908,5.580935,8.578805,2.723915,-6.819307,-8.925848,8.766126,-3.506692],[3.280134,-7.563525,-9.536835,-3.207913,-4.320623,0.620412,-0.684084,-5.191977,5.099534,-1.215933,1.924780,2.253239,-3.867751,-8.757706,-5.872140],[-6.233354,3.380694,-7.333641,-8.045490,-9.154382,-4.776203,-4.081353,7.100737,-0.298209,-9.713528,9.278299,-0.956936,-1.248603,-1.214029,0.650729],[6.381547,-9.282364,-3.614642,-3.159099,-5.356613,8.327265,7.066215,4.834316,-6.414050,0.043938,-4.966715,1.548501,7.132638,4.927333,-4.675696],[5.848433,-5.169666,-8.676736,-1.082003,0.723817,7.877179,4.080599,-4.714891,0.003420,6.085146,-7.975304,-2.117287,-1.440955,4.803116,6.483952]],[[-7.035530,5.468704,3.615867,5.890156,8.601957,-3.394363,-1.500291,5.759001,-0.698237,3.149212,2.296966,8.775037,4.177135,7.681573,2.587733],[-2.567687,0.303453,-7.835847,4.440051,-7.306437,-4.799836,8.551167,5.661535,-0.259204,-2.642288,9.523037,4.462990,2.077758,-4.676700,9.150351],[4.937040,-3.818113,4.491068,1.327768,-4.535864,0.691802,-4.946096,6.983582,2.822321,3.402184,-1.156777,9.826448,6.861469,-5.725744,-0.656532],[9.224526,-1.231751,-5.546090,-7.955222,-8.398597,-7.954046,-9.485024,3.050711,-8.024982,9.825770,-1.964078,-3.836516,9.982724,-6.254602,5.693328],[4.244020,-7.765836,-8.162630,1.227789,0.721966,-3.561154,-7.104042,-3.516129,-1.953948,-5.293818,6.508017,8.037509,4.229041,9.233102,7.792733],[-3.758419,-6.049450,-3.213332,0.552645,2.523406,5.613741,-8.918955,-3.064036,6.626440,5.253975,-9.660534,-1.815396,-1.899163,-6.577641,3.099446],[8.885048,-6.312478,8.942964,-0.301626,2.713681,5.652625,9.862651,-6.931976,-9.952696,2.830790,9.930371,-5.259927,1.142384,4.004543,4.569601],[0.879236,-1.766009,-8.676382,-8.310840,4.922110,-7.867797,6.489220,-9.164005,-9.348951,7.433439,8.310280,1.250858,4.909889,-2.686999,0.098503],[0.882389,-6.003074,-3.726041,5.296408,-4.340167,-1.993607,7.266590,-6.817272,0.076396,7.187138,-0.222290,-3.970513,-8.028224,9.091638,-1.285578],[-8.591397,1.312632,-9.412292,2.638107,7.145450,-7.601835,3.439539,1.606831,9.227461,-3.407978,9.544708,3.703016,-3.530986,3.710603,3.541868],[-4.383236,-4.884522,-2.942932,-1.480428,-7.464160,9.077891,2.120462,8.593409,1.548483,-8.704590,8.217622,-8.412506,0.677205,-5.910238,-6.634977],[-8.369272,-0.829990,0.500496,0.680422,-2.013511,6.414128,-9.234760,-3.211910,0.086618,5.357979,4.624726,6.383141,4.916096,4.767243,-4.139000]],[[7.328530,-9.028656,4.530702,5.749392,3.074475,-2.523885,5.917497,-7.549939,-7.623937,3.524844,3.161593,-3.171851,3.130389,1.945433,-3.518104],[-7.335967,-5.326736,6.037366,-0.804893,5.602486,-9.913329,-3.453892,-4.699880,-9.739605,-4.984717,-4.726778,-3.356877,1.373834,9.693108,-1.840382],[-4.393404,0.319688,-0.063660,-3.263066,3.361466,-0.544381,5.579133,-0.589209,7.990724,0.711073,-9.988210,3.625083,-5.712166,-9.649781,1.480161],[2.165410,-7.450824,5.685256,6.122191,3.546926,9.029876,9.564231,6.004324,-6.447877,-4.342782,-0.606362,-9.227456,6.492680,-4.987174,-2.933649],[2.058381,5.173500,-4.131914,-1.670034,-7.114448,0.441072,4.371138,1.893421,-9.529088,-8.006973,9.145743,8.966488,-5.237039,-8.774729,4.535210],[7.536971,7.492438,-1.618485,0.559366,1.829511,-9.161264,5.872393,6.772082,-0.702828,-3.676801,-3.949821,-3.425760,5.254977,3.214124,3.703518],[-1.656196,5.335714,-8.903665,-9.369685,-6.206065,8.203593,-0.914391,-2.655937,9.898233,2.870365,2.805530,6.346503,1.866581,6.395270,4.198803],[7.172438,8.067302,6.004177,-9.802675,2.403633,0.434923,-4.191283,9.023023,-3.932470,0.659928,-7.656515,0.597565,-9.796158,0.569676,3.926384],[5.428660,-9.027114,1.585798,-3.753811,6.821233,-1.619616,-7.186361,-7.476520,-4.611907,8.676535,-7.046020,-9.532690,3.190470,1.492571,-2.613038],[2.471977,7.675153,-0.953856,5.360365,5.541841,-4.647600,-7.611902,-2.062956,-8.572210,2.554399,-0.923959,-5.917494,1.405844,-8.775229,-7.978905],[-7.688532,-1.370539,3.659425,-7.850777,0.969947,-1.716531,-9.081008,-4.600804,1.121023,6.792120,-2.597368,1.902702,-4.551945,5.713622,9.076808],[-5.202482,5.157562,2.457387,8.927158,-9.910272,3.508231,1.828328,8.981785,-0.635257,-0.641857,6.289382,-0.395828,8.784115,0.272456,7.712807]],[[-3.539709,-5.750230,-3.646706,7.360545,-1.557414,-2.291047,-3.984949,5.884858,3.900030,-9.491777,7.984453,6.270044,-5.479445,-5.612128,1.290986],[-0.228020,1.558589,2.880568,3.212950,-2.939757,-9.256664,4.442270,-6.290032,-0.084369,8.246812,7.152699,-9.729426,-4.488579,-7.053691,8.071649],[-8.426680,6.837009,-6.205308,1.542206,6.809948,2.092150,-1.337796,-9.235023,7.699974,-1.882001,-6.978816,1.060068,-0.940700,8.847452,0.728469],[-4.507714,4.375947,4.062621,8.501303,1.406546,-0.620918,-5.182761,2.243933,1.658962,-3.587627,9.603060,-0.640162,3.405483,-4.277867,6.497544],[6.772073,4.382804,6.874485,1.841874,6.495880,-5.566363,2.628243,-0.276946,5.119182,-4.592967,-2.406795,-9.710051,-3.210221,9.564276,0.257212],[-9.965081,1.493500,2.684201,5.400390,9.270747,5.344852,-4.482050,-6.829469,2.468152,1.703865,4.218691,-0.249822,-8.579298,-0.534286,5.947263],[-8.299338,-6.015255,-8.713132,-1.445721,-2.613272,-5.250711,8.899703,3.221383,-2.484051,-7.825614,-9.963365,3.116998,5.592352,2.013655,2.301707],[4.784377,5.342031,8.837209,3.296616,8.409821,0.652077,3.353689,-6.493045,9.015033,-5.934784,-2.562697,4.572972,9.636101,8.836655,-9.951017],[9.664550,-3.980617,-9.922074,-7.134238,-8.117356,9.630019,-4.656093,-5.297514,7.012253,9.548767,0.082836,-6.187742,3.446508,-5.157812,5.577189],[0.135349,-2.437002,1.000241,-8.197185,9.098963,5.710935,-3.969356,3.794147,-3.854972,-6.107440,-5.492722,-7.360859,6.438017,-6.829212,-3.787371],[-3.691803,6.972781,-3.301218,2.496244,-4.976408,9.851138,-2.663050,9.868828,-5.927602,-3.536264,6.373353,3.166081,-9.022890,8.688678,-1.666036],[-2.161107,-7.288248,4.008975,-3.552185,3.589564,7.760785,-7.000195,-8.332126,-9.791837,0.309973,-4.066690,5.260325,-1.810531,-7.443796,6.514427]],[[-8.540720,1.215085,0.403671,2.917742,-4.073072,-9.968384,1.727081,1.110792,0.625227,-0.131271,-7.400268,6.316575,-2.265097,1.685807,-3.171007],[3.311037,-5.506464,7.135451,-3.444117,1.796581,6.400319,-0.014576,-2.869744,-8.718460,9.078989,5.584911,1.451334,-9.483506,-0.996283,-1.269933],[-8.661959,7.462203,8.416280,-8.190584,6.848003,-6.529030,9.688355,2.014354,-6.802963,7.425566,4.681801,1.920109,-4.122260,-8.965823,-0.983545],[8.093333,4.518431,7.137958,3.341154,-5.893851,-4.989523,8.532339,7.751004,7.854512,-5.806340,-7.388841,0.056379,8.789339,4.592910,6.195193],[-7.770550,-5.045931,8.865089,-8.069210,1.165997,-6.336636,1.820191,6.520813,-6.517937,-5.451301,-3.376507,-2.932076,5.053761,0.350181,-0.204511],[-2.380234,4.491702,-3.791628,-3.245802,8.035434,8.002186,1.369171,5.674814,1.753342,-1.208457,-8.433389,-4.331823,-5.998136,-2.713627,-0.989276],[-4.332673,-2.953454,7.675674,4.832109,4.638130,2.890321,-8.190749,-4.157800,-2.916741,8.780470,0.256362,6.858397,2.038804,0.431606,7.349952],[-0.413399,-0.021309,5.633217,0.960758,-7.255620,0.357526,0.274882,-4.965261,8.780561,6.371488,9.308035,-3.880868,7.433231,7.581012,-4.544301],[-4.143720,-0.460831,9.343072,7.090761,-7.129557,0.248438,1.767487,8.666192,-4.198658,-2.420793,-3.562827,9.376912,-6.799485,-7.383211,2.587263],[-7.709125,9.723840,4.194613,-0.165708,9.792377,-5.880375,-5.954709,7.569041,0.943276,-7.808029,4.417438,-0.767638,-7.063260,5.172080,-9.896954],[4.249214,0.691350,6.068476,1.935971,2.782447,0.914953,7.335310,1.505922,3.973455,8.332235,7.631546,-0.358532,0.187352,-8.933522,0.494100],[1.876733,-0.671135,9.649738,8.277000,7.897882,5.844999,-0.573658,8.122670,5.138745,9.053331,-2.623510,-6.862191,-7.241679,4.157808,-6.016964]],[[6.859702,6.640848,-7.537251,7.963597,8.066013,-1.964202,5.525740,-2.344191,1.991542,-1.647192,-0.882359,3.866765,9.265447,-4.120304,-6.698505],[-2.419642,-4.652664,4.658959,-1.608636,9.133924,-1.782701,6.097706,-9.332828,-8.401376,1.460642,-8.785426,3.066505,-0.435042,7.531784,-9.696615],[-2.177450,2.618399,-1.092229,3.920642,-0.433656,9.044098,4.313290,-9.189156,-2.078507,5.041372,5.071029,8.542910,1.518875,-4.555406,-8.905589],[-7.482673,2.879310,8.402505,9.195718,-5.759620,4.348694,-4.952349,-2.957643,6.053911,1.569863,4.686030,-9.267171,6.484053,-2.744824,7.002918],[-5.018825,7.979379,9.761276,-9.209369,-1.567840,-9.183939,-2.903140,-2.080732,-4.714037,2.978361,-0.338381,-3.605010,5.338068,-5.167848,1.159127],[-4.571020,9.723769,8.258985,-3.248146,7.097206,7.231124,0.973299,-8.902725,-3.757481,2.737388,-1.129051,-6.142788,-7.927641,9.819252,-5.948892],[-5.910365,-1.836446,-7.366151,7.655952,1.801200,2.872994,-9.209395,-9.679697,-4.773472,8.866675,-4.507046,1.154688,1.769048,-7.449777,-4.563497],[6.117653,7.295276,0.015353,-3.876497,3.308169,1.977151,-1.304616,0.628531,3.286210,1.908122,2.313704,-8.707156,8.681915,-9.177432,-7.542383],[-0.530211,-2.467213,-2.729507,3.871726,-9.526849,-7.705466,-6.528378,6.848065,-8.542728,3.534846,-9.907153,0.776748,-6.561310,-4.539962,3.983369],[7.453851,-1.842899,9.855814,8.985791,8.994689,2.322171,-8.832868,-1.090721,7.168182,-2.384678,5.699007,5.120586,1.745696,7.217518,4.039038],[1.902989,-0.925741,-2.635789,-5.270834,-7.570449,7.767758,2.616952,6.724732,4.732240,-6.029157,-9.556253,-3.935460,8.902877,3.066707,7.640524],[5.857828,9.495907,9.788271,9.463639,-6.131583,5.964604,-6.780648,2.572137,9.172020,-9.612765,-2.614484,3.136892,3.562047,-1.196877,7.579759]]], dtype = "float32")#candidate|9749|(13, 12, 15)|const|float32
bop_9750 = relay.bitwise_xor(call_9740.astype('int64'), const_9749.astype('int64')) # shape=(13, 12, 15)
bop_9753 = relay.bitwise_xor(call_9741.astype('int64'), const_9749.astype('int64')) # shape=(13, 12, 15)
output = relay.Tuple([call_9724,call_9743,bop_9750,])
output2 = relay.Tuple([call_9725,call_9744,bop_9753,])
func_9759 = relay.Function([], output)
mod['func_9759'] = func_9759
mod = relay.transform.InferType()(mod)
output = func_9759()
func_9760 = relay.Function([], output)
mutated_mod['func_9760'] = func_9760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9759_call = mod.get_global_var('func_9759')
func_9760_call = mutated_mod.get_global_var('func_9760')
call_9791 = relay.TupleGetItem(func_9759_call(), 2)
call_9792 = relay.TupleGetItem(func_9760_call(), 2)
func_1109_call = mod.get_global_var('func_1109')
func_1112_call = mutated_mod.get_global_var('func_1112')
const_9802 = relay.const([[-3.473136,-0.462370,4.334972,-0.942121,0.677897,-3.343344,6.046789,-2.800238,1.979680,-4.468260,6.652276,4.451511,9.360085,-2.859097,4.935971,-8.790356,-2.753171,-9.337704,-6.572116,4.539489,-0.876366,-2.175718,-7.003696,1.894115,2.897236,6.606986,-4.340357,-2.944419,8.180220,9.161211,-0.104441,1.600144,3.839623,-4.333657,-7.508983,4.732695,6.127632,3.443757,-7.624586,4.149376,-3.551631,-6.333368,-1.119701,-1.596391,7.030791,-8.201208,8.407000,-0.299868,-1.370978,-3.442215,-2.151101,0.044071,8.722859,-0.802091,-7.168395,0.674899,-5.576983,3.234921,2.039512,3.028090,-3.979998,-7.765385,8.757252,-3.095463,1.670939,-2.868320,-5.182050,4.053658,-7.129208,2.484056,-5.860464,8.181875,-0.332720,0.404771,-8.946406,-0.710955,-7.248511,-3.263154,-1.110142,2.951049],[-1.155096,6.709391,-7.720427,-0.497695,-2.739883,3.373950,9.503445,-0.812492,6.701819,1.344177,-2.052766,-4.302551,-7.056958,-2.447100,7.125729,-4.343596,7.381511,-4.271711,-3.604284,0.446206,-4.767128,2.048002,5.498561,3.359766,9.287297,7.975491,6.840836,3.266157,-3.332300,-1.587537,0.029183,8.882730,-2.095542,-7.452205,3.622762,-5.091031,-3.862932,5.561324,2.431306,8.250406,1.722215,-9.496999,-8.881626,-0.013754,0.208198,0.094210,1.756429,4.749129,-7.768416,-0.270522,1.334928,-8.388894,9.997136,-5.576234,-7.565711,0.115186,-9.898854,-4.317412,9.820507,1.816645,0.404496,-8.503431,-1.631614,6.731901,2.151319,-8.125892,-2.748932,9.490801,-6.334206,-2.545030,1.598437,-8.511587,6.074426,-0.411196,1.752073,5.861158,-1.082747,0.991792,6.942073,-5.190883]], dtype = "float32")#candidate|9802|(2, 80)|const|float32
call_9801 = relay.TupleGetItem(func_1109_call(relay.reshape(const_9802.astype('float32'), [10, 1, 16])), 0)
call_9803 = relay.TupleGetItem(func_1112_call(relay.reshape(const_9802.astype('float32'), [10, 1, 16])), 0)
bop_9810 = relay.floor_mod(call_9801.astype('float32'), relay.reshape(const_9802.astype('float32'), relay.shape_of(call_9801))) # shape=(10, 1, 16)
bop_9813 = relay.floor_mod(call_9803.astype('float32'), relay.reshape(const_9802.astype('float32'), relay.shape_of(call_9803))) # shape=(10, 1, 16)
var_9815 = relay.var("var_9815", dtype = "float32", shape = (10, 13, 16))#candidate|9815|(10, 13, 16)|var|float32
bop_9816 = relay.right_shift(bop_9810.astype('int32'), var_9815.astype('int32')) # shape=(10, 13, 16)
bop_9819 = relay.right_shift(bop_9813.astype('int32'), var_9815.astype('int32')) # shape=(10, 13, 16)
uop_9820 = relay.cos(bop_9810.astype('float64')) # shape=(10, 1, 16)
uop_9822 = relay.cos(bop_9813.astype('float64')) # shape=(10, 1, 16)
bop_9825 = relay.bitwise_xor(var_9815.astype('int8'), uop_9820.astype('int8')) # shape=(10, 13, 16)
bop_9828 = relay.bitwise_xor(var_9815.astype('int8'), uop_9822.astype('int8')) # shape=(10, 13, 16)
func_5469_call = mod.get_global_var('func_5469')
func_5471_call = mutated_mod.get_global_var('func_5471')
const_9830 = relay.const([3.455352,2.413547,8.079489,-2.529733,0.893058,-6.059586,-6.255690,-5.309009,4.667898,4.235039,-8.985233,-4.848992,-7.732190,-2.101314,-3.291174,6.888755,-0.752371,-5.263580,8.453472,-7.074112,7.897785,4.160812,-4.606618,-1.878166,-6.915812,-5.176329,-2.320584,-6.276693,-4.960454,0.874715,-9.743682,-3.460140,5.817337,-7.678134,2.888207,-9.874043,-9.190659,6.942748,7.759117,-8.908523,7.951867,-9.140116,-1.501848,-6.222609,-5.314036,0.628252,-1.655007,5.000056,2.943435,-1.855033,-9.412557,4.662788,6.579195,9.068358,-9.807260,-2.682138,0.554852,-8.799633,-6.967472,-1.129995,-6.392927,6.683934,3.812916,-5.499485,1.530736,-1.120529,2.594917,-7.610343,-7.770148,-0.135730,0.205009,-7.233706,2.873144,-3.140794,2.057835,-2.747411,5.028648,9.176918,9.168037,2.900883,-6.900375,-1.052538,5.727458,-4.087466,2.977832,-8.110504,-5.452584,5.400527,9.796777,5.410986,-3.430608,-9.548780,9.695208,-5.000659,-7.147090,3.689201,0.881746,-1.468642,-0.141199,-3.184372,2.013640,7.213626,2.432377,-4.055117,-4.702464,-5.768330,4.801690,-8.998347,-3.591685,6.977285,-0.087958,5.727476], dtype = "float64")#candidate|9830|(112,)|const|float64
call_9829 = relay.TupleGetItem(func_5469_call(relay.reshape(const_9830.astype('float64'), [112, 1])), 1)
call_9831 = relay.TupleGetItem(func_5471_call(relay.reshape(const_9830.astype('float64'), [112, 1])), 1)
uop_9834 = relay.atanh(bop_9825.astype('float32')) # shape=(10, 13, 16)
uop_9836 = relay.atanh(bop_9828.astype('float32')) # shape=(10, 13, 16)
uop_9842 = relay.sigmoid(uop_9834.astype('float32')) # shape=(10, 13, 16)
uop_9844 = relay.sigmoid(uop_9836.astype('float32')) # shape=(10, 13, 16)
func_9759_call = mod.get_global_var('func_9759')
func_9760_call = mutated_mod.get_global_var('func_9760')
call_9845 = relay.TupleGetItem(func_9759_call(), 1)
call_9846 = relay.TupleGetItem(func_9760_call(), 1)
var_9858 = relay.var("var_9858", dtype = "float32", shape = (10, 13, 16))#candidate|9858|(10, 13, 16)|var|float32
bop_9859 = relay.greater(uop_9842.astype('bool'), relay.reshape(var_9858.astype('bool'), relay.shape_of(uop_9842))) # shape=(10, 13, 16)
bop_9862 = relay.greater(uop_9844.astype('bool'), relay.reshape(var_9858.astype('bool'), relay.shape_of(uop_9844))) # shape=(10, 13, 16)
output = relay.Tuple([call_9791,bop_9816,call_9829,const_9830,call_9845,bop_9859,])
output2 = relay.Tuple([call_9792,bop_9819,call_9831,const_9830,call_9846,bop_9862,])
func_9864 = relay.Function([var_9815,var_9858,], output)
mod['func_9864'] = func_9864
mod = relay.transform.InferType()(mod)
mutated_mod['func_9864'] = func_9864
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9864_call = mutated_mod.get_global_var('func_9864')
var_9866 = relay.var("var_9866", dtype = "float32", shape = (10, 13, 16))#candidate|9866|(10, 13, 16)|var|float32
var_9867 = relay.var("var_9867", dtype = "float32", shape = (10, 13, 16))#candidate|9867|(10, 13, 16)|var|float32
call_9865 = func_9864_call(var_9866,var_9867,)
output = call_9865
func_9868 = relay.Function([var_9866,var_9867,], output)
mutated_mod['func_9868'] = func_9868
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8807_call = mod.get_global_var('func_8807')
func_8808_call = mutated_mod.get_global_var('func_8808')
call_9886 = func_8807_call()
call_9887 = func_8807_call()
output = call_9886
output2 = call_9887
func_9891 = relay.Function([], output)
mod['func_9891'] = func_9891
mod = relay.transform.InferType()(mod)
mutated_mod['func_9891'] = func_9891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9891_call = mutated_mod.get_global_var('func_9891')
call_9892 = func_9891_call()
output = call_9892
func_9893 = relay.Function([], output)
mutated_mod['func_9893'] = func_9893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6604_call = mod.get_global_var('func_6604')
func_6606_call = mutated_mod.get_global_var('func_6606')
call_9906 = relay.TupleGetItem(func_6604_call(), 0)
call_9907 = relay.TupleGetItem(func_6606_call(), 0)
output = relay.Tuple([call_9906,])
output2 = relay.Tuple([call_9907,])
func_9908 = relay.Function([], output)
mod['func_9908'] = func_9908
mod = relay.transform.InferType()(mod)
mutated_mod['func_9908'] = func_9908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9908_call = mutated_mod.get_global_var('func_9908')
call_9909 = func_9908_call()
output = call_9909
func_9910 = relay.Function([], output)
mutated_mod['func_9910'] = func_9910
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9388_call = mod.get_global_var('func_9388')
func_9390_call = mutated_mod.get_global_var('func_9390')
call_9933 = relay.TupleGetItem(func_9388_call(), 1)
call_9934 = relay.TupleGetItem(func_9390_call(), 1)
output = call_9933
output2 = call_9934
func_9942 = relay.Function([], output)
mod['func_9942'] = func_9942
mod = relay.transform.InferType()(mod)
output = func_9942()
func_9943 = relay.Function([], output)
mutated_mod['func_9943'] = func_9943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9759_call = mod.get_global_var('func_9759')
func_9760_call = mutated_mod.get_global_var('func_9760')
call_9944 = relay.TupleGetItem(func_9759_call(), 2)
call_9945 = relay.TupleGetItem(func_9760_call(), 2)
func_9891_call = mod.get_global_var('func_9891')
func_9893_call = mutated_mod.get_global_var('func_9893')
call_9948 = func_9891_call()
call_9949 = func_9891_call()
func_7232_call = mod.get_global_var('func_7232')
func_7236_call = mutated_mod.get_global_var('func_7236')
const_9953 = relay.const([2,-3,-10,-2,-3,2,-1,-9,8,-3,5,-5,3,6,-6,9,1,-9,-9,7,7,7,-2,3,6,-4,-5,10,6,-7,-4,-2,-8,-7,-3,1,6,8,-4,7,-6,1,-3,1,-6,2,3,-7,7,10,-8,10,8,-1,8,2,-8,7,-3,-1,-5,9,8,-2,9,7,-2,-1,-6,3,-10,-9,-8,-2,-5,10,-7,-1,-8,-2], dtype = "int64")#candidate|9953|(80,)|const|int64
call_9952 = relay.TupleGetItem(func_7232_call(relay.reshape(const_9953.astype('int64'), [5, 4, 4]), relay.reshape(const_9953.astype('int64'), [5, 4, 4]), ), 0)
call_9954 = relay.TupleGetItem(func_7236_call(relay.reshape(const_9953.astype('int64'), [5, 4, 4]), relay.reshape(const_9953.astype('int64'), [5, 4, 4]), ), 0)
uop_9955 = relay.erf(call_9944.astype('float32')) # shape=(13, 12, 15)
uop_9957 = relay.erf(call_9945.astype('float32')) # shape=(13, 12, 15)
output = relay.Tuple([call_9948,call_9952,const_9953,uop_9955,])
output2 = relay.Tuple([call_9949,call_9954,const_9953,uop_9957,])
func_9963 = relay.Function([], output)
mod['func_9963'] = func_9963
mod = relay.transform.InferType()(mod)
output = func_9963()
func_9964 = relay.Function([], output)
mutated_mod['func_9964'] = func_9964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6107_call = mod.get_global_var('func_6107')
func_6109_call = mutated_mod.get_global_var('func_6109')
call_9968 = relay.TupleGetItem(func_6107_call(), 1)
call_9969 = relay.TupleGetItem(func_6109_call(), 1)
output = relay.Tuple([call_9968,])
output2 = relay.Tuple([call_9969,])
func_9970 = relay.Function([], output)
mod['func_9970'] = func_9970
mod = relay.transform.InferType()(mod)
mutated_mod['func_9970'] = func_9970
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9970_call = mutated_mod.get_global_var('func_9970')
call_9971 = func_9970_call()
output = call_9971
func_9972 = relay.Function([], output)
mutated_mod['func_9972'] = func_9972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5736_call = mod.get_global_var('func_5736')
func_5737_call = mutated_mod.get_global_var('func_5737')
call_10000 = relay.TupleGetItem(func_5736_call(), 0)
call_10001 = relay.TupleGetItem(func_5737_call(), 0)
const_10009 = relay.const([[[-3.024592,8.239370,4.484452,1.132373,-2.077941,0.301185,9.919632,-0.413513,9.894737,-5.691430,-8.370755,7.196666,-9.217637,0.936847,-2.180785],[-0.611619,-6.330695,-9.295708,8.161469,1.613239,-7.602602,-0.737459,-1.466414,-3.655061,8.423377,1.027919,-1.734457,-7.612869,4.894121,-8.552988],[-7.557101,-9.368199,5.890577,-7.660359,8.299014,-1.680457,3.640015,5.907333,6.442004,0.176232,5.859821,-9.049104,1.309812,-4.384881,-7.259585],[-5.127804,3.426777,5.990540,5.423650,7.524798,8.567303,-7.346773,-6.882442,-5.036526,1.846869,-2.426927,-7.139849,-1.848317,8.502807,4.890936],[-7.563829,-5.166082,-5.614311,-5.390925,-7.959257,-6.160992,8.686217,-6.001685,2.532962,2.338011,-7.187150,1.590736,7.617123,-8.567538,-9.070744],[-1.581783,-7.723182,-8.878327,0.937317,-1.639190,-1.859516,4.448248,-8.878194,6.503575,7.076724,-0.106101,-7.870376,-7.282394,-8.926181,8.842525],[-0.887670,7.194108,-3.473311,-7.889917,-8.914145,6.285588,5.608081,-3.332732,-0.558998,7.579309,-5.920971,1.640081,1.749955,-4.283760,5.997877],[-9.320747,-1.016692,-3.986932,5.430153,-1.481835,9.741481,-7.040089,-9.195100,-2.750230,-6.097498,-9.793636,-6.727540,-6.411920,-0.749301,7.519940],[-5.593537,6.321188,3.938806,5.879727,-7.210187,-6.928372,-1.253395,3.771081,0.222442,9.087346,4.791670,-2.105934,-4.599541,-7.452435,-5.488765],[-5.845440,6.493212,3.488728,7.432540,-1.638793,-8.186278,9.896947,7.683041,8.853202,5.672203,8.252627,8.294391,-2.927934,-1.072254,-7.647534],[-7.442980,1.318581,-8.816431,-6.362837,3.764989,-4.159598,9.529678,-1.218208,-9.163076,4.688534,3.464905,-9.718414,-7.985011,-4.068330,2.726860],[4.382618,6.684333,-0.070869,0.566138,6.914575,3.103824,-6.319828,5.027035,5.248769,7.789979,1.779641,0.093720,9.845639,-1.077602,-9.823462]],[[-0.401295,6.481169,-7.391119,7.123432,-8.070539,2.388935,-2.178745,-6.270210,-1.038366,5.926666,-4.359427,-8.527198,1.288797,-3.593770,4.240672],[0.561277,-4.356051,2.852279,-0.699791,4.139316,2.822488,-4.184467,-9.093019,-6.218086,1.151265,-0.976307,-8.388825,9.374660,-3.231925,-2.548478],[2.372571,9.961639,-3.036577,-0.050996,-6.991425,-0.380832,-9.923331,5.025765,1.041502,-5.490551,-0.686800,2.583297,0.045928,-6.459599,-9.016940],[-6.800811,-4.085660,4.965101,-5.854153,-9.914034,6.828877,7.492076,5.124726,8.112901,-6.528986,2.915204,-3.820404,6.451786,-1.160724,-1.836058],[-6.267450,-4.678039,-6.572924,-5.660802,0.859442,9.815602,8.655355,3.022373,-4.456077,0.641601,-6.238454,5.551602,3.537721,-1.746208,-8.214244],[-3.597540,0.818605,7.817521,4.055322,5.541983,-8.700303,6.534684,5.577762,7.971404,7.874449,-5.003753,5.552417,1.224094,-7.163757,-0.213100],[-7.266994,-0.926265,9.273080,7.190852,0.035590,-7.156796,-9.836387,7.554743,-9.312516,0.027581,8.436418,4.114816,5.203932,-4.346254,-3.830026],[-3.863928,4.642111,5.116055,-4.081154,8.338852,2.722045,-9.250663,-6.217580,0.469801,-1.706270,-4.128520,-6.175920,-7.741593,-5.757105,3.179280],[-0.887766,0.423274,-1.249982,-6.861498,-8.371307,-3.135294,0.311635,6.505292,-8.503572,-5.864129,3.665996,2.873383,-1.698206,2.284489,-8.119674],[-4.649676,-8.195384,-4.865332,-2.946212,0.161010,4.598647,-1.873271,-6.754398,-4.047664,-2.320967,4.089483,1.290272,8.609807,7.602653,7.205742],[0.148854,-8.877266,7.376604,2.520911,3.509694,-5.313396,-4.008773,-0.808313,-2.679060,-1.910255,7.978873,-5.945525,-7.133788,9.132206,-5.965519],[5.324630,-0.259740,0.677632,-7.998433,8.663586,-3.938278,-6.262768,-9.784771,0.533605,0.833252,7.541765,-1.113056,-2.028875,7.991129,-0.345893]],[[-2.142716,7.190339,3.224401,-4.649864,4.401127,6.308440,-4.493781,7.407373,-2.644281,1.237282,-5.717671,6.679231,2.646731,3.849178,5.824503],[-4.888568,3.338816,-8.383116,7.610721,-6.288918,-3.158839,-4.739804,-6.361796,3.118443,-9.254895,-6.148857,8.541778,0.199004,3.658858,5.022806],[-0.254187,-8.139775,3.271942,-9.007062,-6.171854,-7.635376,3.644731,2.572434,-3.635592,-2.753962,8.128652,6.923348,-8.276647,6.076479,5.411508],[-0.302600,6.718884,8.996296,8.727358,0.718652,-7.858372,-5.476103,-4.727837,3.118863,-9.784060,6.038488,9.770524,-7.537112,-9.280838,8.691650],[-0.072769,6.449071,2.470501,5.880754,2.256540,-1.884904,-1.843341,0.503490,-6.554774,0.188074,-8.680045,-3.169732,3.309820,-4.609123,1.289668],[5.862430,9.863893,9.657659,6.136415,-2.401538,0.816231,-6.998731,9.857681,-9.147594,4.030870,4.780842,-2.233719,2.110439,-0.590651,6.448987],[8.297683,-9.566306,-3.073610,7.724963,-6.785389,-0.221380,-7.476424,8.230842,-2.546482,6.333188,9.218582,3.664225,4.133813,5.878618,-2.125688],[4.967017,6.108576,5.816740,8.962212,8.623040,-0.330574,5.553038,-7.412607,-7.734427,-6.834592,-6.208890,-2.145747,4.747407,-1.282364,-1.448229],[-6.907642,7.304354,5.466207,7.505211,2.897621,-9.800525,-0.623039,7.016784,-9.131704,4.425162,9.108364,-9.328084,8.865873,6.959434,-1.614963],[6.407709,6.119698,-0.073564,8.021344,0.293477,-9.289285,-4.363218,4.763908,1.428455,3.324278,-2.758700,7.800515,3.389093,3.808957,-7.262521],[-6.974932,-3.659184,-6.117761,-2.349196,-2.495272,4.951888,4.077121,1.372799,2.864136,-8.899950,7.324528,0.676945,4.127344,1.512637,-5.832943],[-5.925872,3.255153,-6.327936,0.374191,6.994677,0.130407,-0.670363,-8.800318,9.401876,-6.920733,4.258921,6.952072,-7.333989,8.224636,1.340864]],[[-0.907228,-3.833185,-8.395862,9.714714,8.225213,0.356217,4.574365,6.526585,9.984883,9.136458,-4.267904,6.707568,-6.761288,-3.209441,5.085083],[4.417155,7.183928,-3.291641,-6.881517,0.353179,-2.202570,-8.549021,-1.687193,-9.272406,8.859332,4.666882,-6.493419,7.795145,7.142149,-4.068854],[8.757167,-1.483615,5.917833,-4.264584,-0.154650,5.231159,-8.577827,4.887687,0.387434,-1.643809,0.320762,-3.993923,-9.968523,-3.415757,6.026832],[-2.267890,-2.193829,4.467629,5.489262,-4.658392,9.747544,8.045133,1.551664,-7.149529,-4.377229,9.068048,-1.636891,3.192707,4.000612,-5.564093],[-5.609964,5.512807,5.607678,-8.710092,-3.204064,8.167787,-2.871542,0.500997,0.578320,-9.327883,-3.529961,1.830428,0.301209,8.443160,0.704373],[5.071585,6.402592,-2.213605,2.219640,6.637644,2.923801,5.662564,8.940515,-6.560427,-0.267724,-8.156301,-0.531269,5.965560,-6.187854,1.435102],[5.350045,4.940494,6.959217,9.334547,-6.585171,5.164144,6.789828,6.922255,0.926848,1.333087,-9.541924,0.547741,-0.937550,-4.825590,0.288352],[-4.574683,-4.624881,3.467185,7.747377,-3.289351,-8.888569,-7.262657,-8.780255,-3.848797,6.926894,8.196666,-2.798218,-0.458949,-5.485308,8.568040],[-0.258022,-0.647665,-0.670158,5.172637,-2.036143,3.118929,3.961016,3.100441,-5.549537,1.014155,3.551821,6.027474,2.054039,-9.207814,5.597058],[-2.236079,1.502252,-7.069297,-6.461358,-3.833878,-0.671697,1.443601,6.003693,2.384096,0.145008,3.624491,-1.057513,-2.970635,-3.178041,6.322363],[-4.354253,-9.746237,-6.578102,2.302510,-4.338041,0.529986,-0.654054,-7.410364,7.356707,9.723805,-8.446175,-4.390879,6.042826,6.547503,0.060300],[2.651551,-2.552563,-7.783440,4.042428,4.725166,3.015715,-9.628544,-9.042857,0.838961,-7.326834,-7.085537,1.875457,7.945100,1.340189,-6.019879]],[[9.709125,-7.270699,4.837571,-1.156844,2.599109,-2.564028,2.240095,-2.542138,7.002941,1.557284,-6.444878,4.437823,-3.662309,-1.702467,4.101288],[1.111117,7.845307,-4.500346,-4.264334,1.018405,-3.829646,-9.555736,-7.962636,2.732485,-1.733115,7.022733,-0.646067,-4.807653,-2.365492,-7.308652],[7.808483,-6.806601,-3.043743,-6.929958,-3.016450,-8.089575,4.669615,-7.987141,9.383216,-2.480787,-2.400921,-3.603205,-0.089879,-7.191953,1.844058],[-4.080297,-5.007430,6.583283,6.378064,0.442068,0.134287,-9.693891,-2.025979,-3.671452,0.187682,6.276136,9.724073,-1.973862,-6.557358,-9.342185],[-2.933532,-7.415915,9.518155,8.803022,2.668957,-7.152282,-6.855435,-2.801509,4.721440,-8.964038,4.813370,5.507136,2.722983,-6.846134,-7.089130],[4.316770,2.785829,4.333774,-3.590284,0.379749,2.997603,-6.491553,-3.435207,-8.993109,-5.468492,-2.808704,-3.123421,-1.451644,-1.678148,8.739672],[2.131297,7.082966,-7.054962,8.275818,6.677085,2.560103,6.984005,-9.637064,-0.433555,8.966358,1.251143,-3.442939,2.332898,9.650180,3.919222],[-2.943414,7.356907,9.427687,-0.084098,-7.297157,9.528749,-9.225386,-9.547466,-9.141188,8.144470,3.257345,-5.105538,-6.223207,-9.108196,2.621781],[-4.198919,-7.360522,1.699697,-5.632672,-9.436176,8.530574,-7.570186,-4.219094,-9.118617,4.421365,9.281089,-5.647604,-2.938122,0.692437,-7.817998],[-8.550897,2.441211,-6.067328,-2.102033,-8.125855,-5.715254,-5.107372,-4.657808,7.234957,6.456505,-9.114994,1.789452,-1.566537,-2.513033,-8.074809],[-9.497822,6.107748,7.439184,-4.907008,-1.301557,-6.358080,-0.579787,1.515450,-8.795689,4.496712,0.129642,-0.243180,-7.581290,-2.868939,-2.379874],[6.567784,3.966663,-4.551533,9.278979,-9.768266,-1.418608,-9.496017,0.296149,3.052978,-3.418509,-9.867429,-1.505725,-5.027099,2.768524,1.842810]],[[4.572095,8.412489,-4.307061,3.629557,-9.473629,0.968480,-8.209540,-3.286660,-3.169704,6.226643,-0.591053,-4.089879,-5.999701,-7.790356,-7.409260],[-1.895008,-0.664958,-3.771680,7.530652,-5.132304,-9.970092,-8.478158,7.282089,-1.942666,-3.577023,-1.738493,8.945687,-9.792517,0.233539,-7.583796],[-0.774387,1.615173,-2.545076,1.014228,4.292920,8.775307,-3.498956,5.378127,-9.775799,3.394645,3.866161,-3.097992,-8.276388,3.805711,3.070639],[5.698716,-9.148832,-7.256016,0.942243,-9.562826,-1.910142,-5.970452,-1.748547,-0.673988,8.338322,1.264835,-7.203963,-4.932118,-4.703091,-0.939958],[5.668385,-9.368042,5.664574,-8.751202,-9.127135,3.663657,-6.700172,9.062433,4.970085,-4.573054,9.899745,-9.817420,3.410159,8.135342,-4.333445],[3.098479,8.512598,2.248480,-1.563755,3.959896,-7.919126,6.698843,-9.857245,8.864259,0.115906,4.703931,-1.681997,-0.980469,-1.461475,8.937202],[4.021020,-3.388502,-7.311071,0.106495,6.696705,-4.252449,-4.463854,-1.155533,-4.400869,-9.747548,9.744263,7.772564,3.924677,9.661266,9.347708],[-4.329548,6.127488,3.161909,-9.682804,6.954967,-9.753042,-2.059260,0.417449,6.713953,-4.024087,9.730384,1.229615,6.509030,-9.213809,-8.220308],[-1.164234,6.893247,8.926949,3.758338,1.851689,0.228230,-2.174431,-0.165693,6.692315,-0.713711,-0.796843,2.124356,-7.836017,-4.566730,-9.170692],[-2.411318,-4.366131,-9.381177,-1.960327,0.101054,-9.524061,8.909907,-3.169917,0.192364,-5.725213,-5.944850,8.043733,-3.807657,-4.568789,3.699106],[-8.590940,8.019904,3.938980,-0.358357,-9.822780,8.837695,8.955441,4.672080,9.100406,7.650414,-2.212950,-3.260528,4.275020,7.777422,5.792255],[-2.606525,-5.886514,-0.304946,-8.490898,-5.492185,6.578448,3.212683,-7.110415,-1.664184,0.995306,3.952606,1.391592,-6.961587,1.254337,1.375381]],[[-6.094998,-4.387131,7.291478,-7.406248,2.032014,-3.807360,-9.695669,6.044089,0.525846,-4.653654,8.992456,-9.085863,9.519914,-0.007666,5.614366],[-6.627282,9.802448,-9.625140,0.834856,-9.084058,3.972620,3.600121,7.279224,1.192092,2.333981,3.444315,4.196623,4.015478,-6.311702,9.145833],[0.295018,4.164610,-4.198546,-9.596053,-3.455987,0.089634,6.972542,-2.449442,1.381226,1.466218,9.855083,-3.772777,6.268084,-7.617086,6.414122],[6.141778,3.331133,6.108013,-1.160465,8.273736,0.585903,9.817095,-8.971067,2.083669,7.638288,-7.902644,8.145926,4.880703,-3.910241,2.247243],[-0.940417,9.328347,9.202344,3.941595,-8.232003,7.370918,3.370768,-6.007910,-6.428220,-4.048776,6.799489,-7.551760,6.601400,6.567925,0.142928],[8.400691,0.099408,5.196164,0.858165,-0.445035,-4.642442,5.396999,-7.689747,0.713133,2.949247,-7.792860,-8.101630,-9.399765,8.943090,0.734828],[-0.894170,-4.965944,7.446230,-6.974009,-5.671580,-6.537157,-2.517700,2.636135,-7.802570,0.678455,-3.300623,-0.456225,0.677826,-8.017411,-7.034842],[0.756761,-9.164434,-2.840991,-4.381890,-9.427652,0.817535,5.618136,8.977385,8.126025,4.556980,2.811643,-7.550810,-7.648838,-6.388181,-5.921814],[-9.535103,9.589951,9.534424,5.555624,5.434046,2.016925,-9.054702,-6.834070,0.729340,8.068105,0.584947,-9.201115,-1.664856,9.959777,4.969754],[0.298726,2.845044,-9.685718,-3.860135,-0.681867,9.646437,6.686692,-4.609136,0.016946,0.508947,-0.250764,-0.907395,-6.063865,9.369211,4.018919],[-4.870111,6.960866,-2.335090,-9.700087,2.643541,-0.171818,-2.330347,-8.852040,6.161777,-7.190256,9.776639,9.291241,8.646489,-6.697442,3.931983],[3.258808,4.704117,-9.937280,-1.703300,-4.805453,1.704870,1.416517,-0.266748,5.151560,3.607272,-3.532250,-8.546350,-4.727126,-0.752855,3.444607]],[[0.158060,0.409356,5.082181,-6.376958,-8.369819,5.662622,1.038233,-2.083846,-7.042368,5.435084,2.356446,-1.242408,-0.911523,-1.585761,-7.293265],[-0.115235,-2.271598,-9.332986,1.029214,-8.530454,6.631922,-9.520864,-1.865957,7.797107,-9.848077,-0.209307,-2.754897,6.480712,-6.679922,6.984955],[0.606398,-0.611556,0.887878,8.157703,3.421614,8.764243,0.741043,0.734705,-6.545174,2.621515,5.891168,-2.552679,-0.880125,-0.719913,4.416533],[4.893815,-8.927709,1.797431,-7.940463,-5.060099,-9.075941,3.596769,7.242629,9.370899,2.692206,-5.509254,-5.349407,-0.973811,5.310439,2.601567],[9.001801,6.194430,-1.148998,1.545287,-6.166029,-2.957290,6.581302,-5.999383,-7.242609,-3.231780,-1.122854,2.601702,-0.906814,-2.390624,-4.928406],[-6.874581,-8.541648,9.280756,-6.761339,-5.594702,8.943397,3.530708,-9.257082,5.185252,5.466843,-9.515699,1.348561,2.519651,4.308732,1.840176],[8.705959,7.126389,5.226587,9.597781,-0.805876,-8.862946,-6.892353,-2.836640,-7.708873,-2.974119,-8.528175,9.535663,-5.390025,7.207495,-4.487196],[0.360931,-9.231639,-8.675551,-0.460101,-1.547705,3.790098,-9.694500,-8.440704,-0.068703,-5.474504,3.459923,8.927561,-8.749616,6.525553,4.881712],[-2.260065,5.417188,-2.944341,5.523875,4.319259,0.953291,-5.535674,0.941532,-5.918552,8.088872,-3.846308,7.439957,-7.020928,4.940379,5.917961],[4.055776,2.593864,9.571968,-0.519632,-4.890362,-7.245388,-1.784882,1.129863,6.453073,4.975331,9.544766,3.988085,7.179295,-8.572541,5.261915],[-0.938818,-3.482040,-2.256118,1.360724,-1.089271,-8.511167,5.650824,3.625597,-1.122776,-2.718547,-3.144191,0.892669,3.348156,7.829910,5.781567],[0.516836,9.701364,-6.871602,5.567700,6.728918,5.068887,-9.536531,-2.283118,-5.971761,8.137381,8.451134,-8.463634,0.792905,2.156729,1.643031]],[[-1.567529,-6.029174,-2.061849,3.144093,-2.285770,1.782276,-5.263156,-5.591369,-9.891307,-0.296350,-2.547072,2.333277,-0.204454,-6.146103,5.410153],[3.496571,-4.320223,8.680308,-3.923999,4.699368,5.550736,-1.821982,-1.841707,2.644786,7.143823,-3.606552,3.616263,-6.230111,2.282595,0.444102],[8.396458,-0.493836,2.245388,-4.496234,-9.592750,-3.678902,4.263009,1.499824,-7.319617,-1.056049,-5.518863,8.945766,-8.286023,-7.569101,-9.285482],[-8.793742,-9.351874,4.999255,-0.231169,1.067178,1.627716,6.580313,-3.647933,8.314613,0.981577,3.135959,-1.219018,5.819838,-3.306342,-0.890753],[3.742126,-0.058051,6.373970,2.753427,-4.588717,-9.776456,8.546714,-4.111122,0.907531,-1.507224,0.209484,-7.911371,-6.939043,-7.889727,4.343363],[4.040328,4.039480,-7.792432,9.707204,-3.457475,-9.405474,-2.600135,-8.104843,-7.214259,-4.518663,-3.756377,-1.306358,5.816493,-6.236671,1.287626],[9.167980,9.273798,3.233903,1.888545,6.832546,-7.596262,9.106774,0.596645,1.385378,6.675195,-6.158988,6.420299,-3.365350,1.613230,-6.423127],[1.445145,6.444041,-3.544991,-8.966642,-3.222458,4.523162,-6.829508,7.565497,2.590932,1.157168,-1.699945,-9.094882,-2.004951,-5.232178,-1.257578],[-4.239345,-1.332522,-7.163724,-9.577375,1.450690,-1.636398,0.446254,5.671550,8.200543,0.710101,2.523974,-7.712238,7.761088,-8.653873,2.926131],[-1.199362,-2.292558,5.398845,4.110848,-8.696477,-6.242901,-9.177411,3.411447,-8.240052,-0.632647,2.114363,7.458337,9.223398,-4.705234,7.434701],[-4.596307,6.488344,-1.974407,8.914492,8.400435,-4.654896,3.736171,0.692412,-9.079782,6.320889,-7.871162,-8.241680,-9.732912,-5.974828,-7.424481],[-1.895940,-6.162511,1.545586,7.496671,-3.552514,-0.334366,-3.346255,5.480343,-1.938013,-5.989983,-9.393489,-4.928480,-7.262495,6.914799,2.888873]],[[-0.156818,-6.909205,-1.080090,-7.736285,7.223641,-4.560151,3.459029,6.318792,-8.098709,7.140424,8.472658,0.381545,-5.937642,-5.011387,3.713567],[0.410975,-0.255130,-8.374129,-8.892968,-2.358581,2.244074,3.150732,9.593444,-3.701661,8.342387,-4.094230,5.503127,-7.376750,-5.985651,0.306786],[0.458540,0.914277,1.466906,-6.793229,-9.543711,3.103851,9.939941,5.537816,0.963847,-9.147832,9.496610,1.001553,0.773199,-3.693229,-6.693335],[7.811548,3.492590,5.364398,-3.922455,-4.149755,-3.976735,-8.295992,-1.954867,9.404454,6.715282,-9.923157,-7.936036,-8.124859,-1.975736,0.071602],[-5.527558,-5.185731,-2.507945,-2.128887,3.680088,3.390422,-7.365231,9.878151,6.614793,-5.175078,-3.365964,2.714388,-7.458413,-4.004045,7.609162],[-8.837462,-7.161062,2.048438,-5.132500,2.610488,-5.406837,-0.573593,2.060280,5.775278,-9.854481,5.575662,8.325538,7.372275,-7.827743,-7.025813],[-1.920470,-2.042895,4.926759,2.985473,1.948847,8.701261,7.517335,4.771345,3.532176,-9.858838,-4.274939,-8.872424,-6.605097,-2.747157,-5.961346],[-9.550812,0.067464,2.816105,-0.122167,-8.898411,-8.902091,5.215905,8.499529,-4.546337,-3.013530,-1.930310,-6.313430,-3.163830,2.688604,-2.312944],[0.296738,-0.856699,7.416435,0.590793,-1.797989,9.459796,4.376839,-8.157155,9.800670,6.084042,6.343362,8.568706,-8.675625,7.292351,-0.124859],[5.926144,-5.389261,-2.307916,-5.821777,-4.334428,0.149721,1.670974,-0.414878,-1.490078,-6.399478,2.159687,7.817359,6.075579,-9.448178,4.493151],[-4.756185,-4.059858,-6.061150,-3.890974,-2.911389,9.641625,8.406496,-6.027737,4.901447,0.185059,-8.493672,6.520118,6.190563,-8.623584,8.160603],[-2.416785,-6.193102,6.764445,0.534065,2.045963,-5.355730,-7.378735,6.375221,9.093955,8.879460,-9.228155,-7.423698,3.302754,9.271216,8.704771]],[[-3.850874,-0.335341,3.807739,6.604619,-6.602662,-0.512914,-9.343978,-8.062063,-1.127945,-4.385062,-8.831510,3.575512,-1.612771,8.621435,-0.677995],[9.679429,-5.006978,-6.675627,1.640667,9.023704,-0.149519,-8.808481,-0.905972,3.184291,-7.327972,-7.810580,-8.022015,4.541851,-0.962111,-1.378515],[-4.454998,8.049932,-7.428719,-0.384631,-1.479655,4.688562,4.349379,3.180875,-2.518901,-3.207309,-7.902261,7.168103,5.106832,9.927776,1.862913],[-6.843655,4.386788,7.924274,7.220457,8.266219,6.702972,2.266785,-0.290117,-7.784122,7.955705,-7.940204,0.698086,-6.913472,-5.089655,-6.994161],[-7.934713,4.124287,3.629441,0.673063,-2.792810,-4.100208,3.234806,5.541704,-8.488092,-3.474665,-2.701827,0.043343,-1.335493,-4.988768,5.536968],[1.428952,-8.083453,-2.742845,8.205977,-3.633990,-7.485523,4.036613,-7.602879,-7.414583,-8.421013,-0.633694,3.708789,-0.576000,-8.881707,-3.618664],[3.446642,7.753479,7.740761,8.985780,4.048978,-7.453366,-8.450538,5.681811,-5.773691,4.648750,-9.334051,-0.475443,7.890829,4.492550,7.740363],[-3.717659,0.477537,-5.714992,9.154969,8.203490,-7.534536,-5.650961,4.136145,3.202997,5.190196,-9.161373,7.099042,6.672647,1.971183,-0.399517],[6.362996,-4.747541,-8.761083,4.176119,-1.350258,-2.213026,-7.972529,-7.095843,-8.513539,-0.447596,-5.916871,4.282544,9.318781,5.855307,5.252619],[9.231360,-5.990038,-4.654347,4.024429,-0.652324,-4.728703,-9.601774,7.576056,1.374938,-0.243104,-9.960297,-9.783355,-7.907047,-8.823702,2.448388],[7.646210,-9.312002,-2.944631,-7.439976,-7.451562,4.251180,6.859277,-9.401454,-7.119547,-6.602222,2.462072,-6.903720,-7.777721,5.074258,-9.995954],[6.889719,4.045837,6.416396,-0.840842,3.977470,-5.782502,0.020553,-1.731365,-7.141033,5.317511,-7.519792,4.124307,7.350630,1.974850,9.272039]],[[6.542121,-9.940241,-3.455111,-8.818424,3.290940,-5.642548,-3.403295,-0.134484,7.920176,-6.582937,5.513197,9.031200,4.784740,0.754317,8.315784],[-5.638751,3.107257,1.239693,-9.664168,-1.833570,-3.874116,6.554708,-2.408900,4.997852,-0.941566,4.350656,-2.954147,9.957530,0.928901,1.134100],[8.978642,1.344868,-2.405795,-9.989424,-3.405215,-0.559278,8.424810,7.035415,1.563783,9.315574,-2.972731,-7.800351,4.447729,-2.928017,-9.158273],[4.334228,6.485935,-7.798436,-1.693344,-7.343809,7.921318,6.369247,-9.610971,-1.319837,6.177554,-8.519797,-7.211856,5.495769,-1.113124,-1.452879],[5.637837,-7.081057,-9.721044,-4.648648,5.678393,4.869828,6.101050,-6.389989,-2.233867,-4.166944,-4.229710,9.005364,5.086658,7.521817,2.084768],[-0.079964,4.151025,3.331689,6.901295,-6.514356,2.384830,8.444024,-9.936733,-8.513978,-5.640235,4.468477,3.472617,-3.691094,8.994761,-7.375378],[9.644997,0.408285,9.621377,2.359450,-0.385220,-2.487608,2.752960,-6.712762,5.206517,-7.238833,7.727698,-1.904763,7.866413,9.966565,-6.785242],[8.166626,-9.340136,6.587664,4.828728,-3.561318,-0.640368,2.357410,-2.168952,-8.661530,4.145036,-1.701261,-5.727570,7.912330,9.404223,-9.511390],[0.094408,2.215180,-8.170647,0.336578,6.522801,1.999233,-2.319120,-3.058958,-8.584831,-2.013676,1.875434,6.333789,-1.161504,3.269716,3.522081],[8.003888,7.525400,4.276425,4.905290,-0.555845,-5.016543,7.362088,-6.669034,-3.454967,-4.195819,-3.401216,5.816512,5.097032,2.137580,5.588468],[-4.644582,3.758232,8.260621,8.964076,8.035934,-9.324772,4.855245,9.868369,0.777903,-1.711672,-3.056983,0.399131,-0.035206,1.074373,-5.235346],[6.859980,-4.329228,-1.669557,1.337969,-9.367022,9.021916,-4.840832,-1.816805,5.184418,0.091549,0.671542,-7.852514,7.187480,1.315436,-2.057741]],[[4.944268,-6.912620,-5.856204,-1.506021,-8.590942,0.305649,8.410990,-7.508431,6.214879,4.982656,-6.075550,-5.067637,1.779560,4.475889,6.404550],[-2.690376,6.271085,-9.617783,-5.737783,5.080253,5.717281,-9.155203,7.671438,8.954842,-1.516057,5.035671,4.977576,-5.331285,-9.913366,-0.292440],[1.252391,-0.579313,7.964111,6.325031,5.715264,1.697380,8.972297,6.541381,-5.994339,9.172039,9.439725,7.345560,-3.943079,-6.085600,-5.830152],[-4.298285,1.298697,-7.033842,5.112854,-2.734764,7.868860,-3.465056,-4.730134,5.682678,-8.694974,3.320149,2.738203,-6.229546,-8.099857,-9.877439],[0.782190,8.387585,-6.452462,-1.249976,8.366088,-7.903728,-1.855305,4.046184,8.395338,0.984329,2.181126,7.385784,-3.494443,-5.594355,-8.135897],[6.365300,-0.908292,7.778013,-2.856058,-0.136742,-7.603488,-4.989103,1.288973,1.630440,-3.074365,-5.618951,-0.780741,7.969042,-6.384118,1.518675],[-9.488969,-6.677098,4.060219,6.043816,0.245076,9.528331,2.375767,-7.992418,3.430888,8.381631,3.779110,0.721633,9.242716,-7.675996,8.284941],[0.035645,-4.572729,-4.563234,6.099460,4.762475,0.526184,-4.631876,8.598639,-6.354232,4.186902,-8.489900,3.658422,-8.746727,-4.853279,-0.604022],[-3.251272,-3.595315,-1.231869,1.190017,-2.327602,-3.172084,0.360300,-4.883558,-6.490754,-6.397627,-7.061446,-7.325633,-6.135410,3.530896,0.325852],[-9.139793,6.227819,-3.392856,2.793787,6.650058,-3.083118,-3.431595,-5.479709,-3.234685,1.612733,-7.169036,-9.816422,5.127326,5.304182,8.029267],[7.842403,8.783068,-6.840033,-0.981853,7.402073,-5.660507,0.685469,4.391381,3.335770,-7.049049,-1.075875,1.091630,9.149957,-5.950236,7.145979],[5.325310,3.870338,1.440218,-3.467819,-3.289874,0.824147,-6.203111,7.606235,-8.535919,6.967564,7.667258,-0.471428,-3.349614,1.580962,-9.644245]]], dtype = "float32")#candidate|10009|(13, 12, 15)|const|float32
bop_10010 = relay.logical_and(call_10000.astype('bool'), const_10009.astype('bool')) # shape=(13, 12, 15)
bop_10013 = relay.logical_and(call_10001.astype('bool'), const_10009.astype('bool')) # shape=(13, 12, 15)
output = bop_10010
output2 = bop_10013
func_10024 = relay.Function([], output)
mod['func_10024'] = func_10024
mod = relay.transform.InferType()(mod)
mutated_mod['func_10024'] = func_10024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10024_call = mutated_mod.get_global_var('func_10024')
call_10025 = func_10024_call()
output = call_10025
func_10026 = relay.Function([], output)
mutated_mod['func_10026'] = func_10026
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6300_call = mod.get_global_var('func_6300')
func_6302_call = mutated_mod.get_global_var('func_6302')
call_10030 = relay.TupleGetItem(func_6300_call(), 0)
call_10031 = relay.TupleGetItem(func_6302_call(), 0)
func_9942_call = mod.get_global_var('func_9942')
func_9943_call = mutated_mod.get_global_var('func_9943')
call_10042 = func_9942_call()
call_10043 = func_9942_call()
func_5418_call = mod.get_global_var('func_5418')
func_5420_call = mutated_mod.get_global_var('func_5420')
call_10051 = relay.TupleGetItem(func_5418_call(), 0)
call_10052 = relay.TupleGetItem(func_5420_call(), 0)
uop_10057 = relay.cos(call_10042.astype('float32')) # shape=(11, 14, 2)
uop_10059 = relay.cos(call_10043.astype('float32')) # shape=(11, 14, 2)
output = relay.Tuple([call_10030,call_10051,uop_10057,])
output2 = relay.Tuple([call_10031,call_10052,uop_10059,])
func_10061 = relay.Function([], output)
mod['func_10061'] = func_10061
mod = relay.transform.InferType()(mod)
mutated_mod['func_10061'] = func_10061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10061_call = mutated_mod.get_global_var('func_10061')
call_10062 = func_10061_call()
output = call_10062
func_10063 = relay.Function([], output)
mutated_mod['func_10063'] = func_10063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7801_call = mod.get_global_var('func_7801')
func_7803_call = mutated_mod.get_global_var('func_7803')
call_10106 = relay.TupleGetItem(func_7801_call(), 0)
call_10107 = relay.TupleGetItem(func_7803_call(), 0)
func_9190_call = mod.get_global_var('func_9190')
func_9191_call = mutated_mod.get_global_var('func_9191')
call_10116 = relay.TupleGetItem(func_9190_call(), 0)
call_10117 = relay.TupleGetItem(func_9191_call(), 0)
bop_10123 = relay.logical_and(call_10116.astype('bool'), relay.reshape(call_10106.astype('bool'), relay.shape_of(call_10116))) # shape=(1, 12, 15)
bop_10126 = relay.logical_and(call_10117.astype('bool'), relay.reshape(call_10107.astype('bool'), relay.shape_of(call_10117))) # shape=(1, 12, 15)
func_6077_call = mod.get_global_var('func_6077')
func_6080_call = mutated_mod.get_global_var('func_6080')
const_10132 = relay.const([-8,-6,-6,-2,-1,-1,-4,-4,-4,-9,-2,10,-8,1,1,-7,4,9,-10,-6,10,6,4,-4,-8,3,-7,4,-5,3,10,-7,3,4,-9,-8,10,10,1,2,-8,9,-10,-5,9,3,7,-6,7,6,10,4,8,-4,9,10,1,-3,4,7,5,5,-1,-2,10,-6,-4,2,6,2,-2,-3,4,3,5,1,2,-9,8,-5,1,-9,-4,8,-7,-5,5,-9,5,6,5,-9,-3,4,-2,-10,-2,8,9,6,-8,-2,-9,1,4,4,-5,8,1,-1,-9,-4,9,-7,-9,4,-3,10,9,6,9,5,-10,3,-3,4,5,-4,-1,-3,-3,-10,5,-8,3,8,-1,7,-5,3,-7,9,7,6,-4,10,8,-4,10,-7,-6,-7,7,-10,-6,-10,2,-5,-5,-6,-2,8,6,4,6,1,8,10,-9,10,3,-8,-1,3,4,5,-8,9,-5,-2,-6,-4,8,-4,2,4,-5,-10,3,-2,-3,-4,-10,-4,8,7,-8,10,2,-3,-7,-2,9,-9,-5,1,10,8,-8,6,-8,-10,3,-2,-4,-1,-2,-3,5,3,-5,-8,10,4,8,-4,2,-3,-5,-1,-10,10,-5,4,5,2,2,4,7,1,-7,-2,-2,3,7,-4,6,8,-7,5,-10,3,-8,7,4,-3,-7,-9,9,4,-5,3,-2,-5,3,-2,-7,-6,-1,-2,-3,7,9,6,-9,-4,-9,-6,-7,-2,8,-5,7,10,6,-5,7,8,-8,-2,5,1,-2,-8,7,3,-2,-10,2,8,-4,-9,-5,-4,3,9,-3,-3,7,-8,-1,-8,9,-5,10,1,8,-4,8,7,-8,-9,-7,8,6,-8,6,2,-6,6,-2,-1,-10,-3,-6,10,-9,5,-3,-1,8,6,7,-9,6,-10,-4,-7,9,3,-4,-7,1,-10,4,5,-3,8,-10,-5,-2,-5,10,-3,3,2,8,-10,-1,7,-6,-9,-3,10,-2,2,-2,2,-8,-8,-2,8,-10,-1,1,-8,10,5,-4,1,-2,2,7,-5,-1,-5,5,-3,2,-8,3,9,3,9,10,3,-2,-7,1,3,7,2,-1,-9,-10,5,4,7,9,7,5,-3,-7,5,2,-9,-5,-3,8,9,-2,1,2,5,1,3,4,-2,-8,-2,-4,9,3,-6,-5,-1,3,3,8,-7,2,7,-9,8,6,6,-10,-9,-9,8,-4,-3,10,10,-3,-9,10,10,6,5,-9,-2,-9,2,8,6,-8,6,-4,-8,-7,4,4,7,6,-10,6,-2,2,5,-5,-9,9,-2,6], dtype = "uint16")#candidate|10132|(495,)|const|uint16
const_10133 = relay.const([-1.298861,-9.644813,-9.107674,2.234214,4.972733,-8.587639,-3.712827,-9.396930,-4.183275,2.204849,4.759063,4.007250,7.325442,-0.306040,7.218555,-7.056963,-7.528822,1.993990,0.606988,-3.670996,-7.629440,3.332155,4.239960,-7.038357,4.207492,2.985774,0.525847,-5.625329,4.569508,3.893718,-5.357525,8.086425,2.592054,1.461829,6.403892,0.267007,4.847439,-2.348280,-9.465045,-5.759617,-1.250938,-6.095729,6.326472,-6.452704,-1.402284,9.806121,-3.909880,8.963722,6.787050,-6.956933,6.385484,-0.392208,-0.145947,9.848456,6.052189,0.591975,3.517191,4.161087,-3.294490,-6.243810,5.151294,4.452156,-5.072986,0.357217,-6.428008,-0.638600,5.215112,-4.445213,-6.024747,-8.276736,1.121123,0.731826,-8.337815,8.481267,1.771099,1.761451,4.525433,-8.152177,2.073989,1.656938,5.817224,2.485797,-3.115285,-4.465415,-4.759130,-3.596025,-4.663499,-3.544509,-2.667242,-5.999340,9.825895,0.364127,-2.615349,-3.719914,8.767331,9.056235,-9.197761,-1.757776,-5.726139,6.090269,0.443208,5.171438,7.162553,-2.645505,5.912444,2.908432,-4.230327,-6.074066,-1.937969,8.780845,-8.942505,-2.087490,6.386653,-7.371062,-1.812554,-8.816974,8.356919,6.905647,-6.388522,2.604847,-5.044557,-8.404132,4.420596,-7.341520,-7.891304,9.434030,-9.973249,3.728709,-2.824244,-1.738996,3.682823,3.755961,-7.944484,0.299808,-5.129945,-0.136985,-3.412595,-6.455122,6.561225,9.190839,-6.632726,3.243142,9.863652,-7.993127,-1.512728,-1.353759,-7.226999,-0.333153,-1.563136,5.950257,-4.760206,-4.397949,-4.693242,-2.489269,9.148055,0.780886,5.719262,-8.378536,6.977603,-7.398354,7.783067,8.211086,-2.765668,-3.814520,-8.832523,-5.611636,-8.130515,1.325928,9.005678,-0.259975,4.302044,-6.230612,-7.223344,5.652679,7.760059,5.312392,-6.663504,-6.522758,0.508229,-1.072934,-8.544994,-3.573360,6.732466,-6.969184,-0.682275,1.449443,-2.806496,-3.118646,-0.136567,6.973720,9.285394,3.158739,0.861527,2.816348,-0.739086,-2.815319,-8.780326,3.437830,-4.201067,-1.191217,7.792462,2.281922,0.956146,-6.953142,9.264629,4.989665,3.013134,0.004368,4.033409,5.032432,-4.013262,-5.179332,-6.353334,-1.454529,2.956004,3.100226,-2.557140,6.027727,-9.144564,1.791704,8.923013,6.511616,2.569878,4.874149,0.911319,4.382629,0.896253,-7.934754,8.245059,-8.363851,2.939595,9.846105,-3.953605,2.892240,4.861410,4.496868,6.277647,0.552452,8.849098,4.032795,0.274508,-7.853922,5.287134,-0.364932,0.365744,8.071184,8.102908,-8.124525,3.480088,-0.347124,-1.936346,4.728998,-8.942876,3.861294,-3.737529,-5.106785,9.945288,-7.125853,3.693481,5.079573,3.447849,1.634227,-1.645960,6.091547,3.598773,-3.591307,4.643096,-5.345105,-3.072481,1.823046,-8.477190,-7.326036,-6.624925,-8.757433,5.926361,-1.272048,3.256589,3.571698,6.198476,7.931435,1.643002,-0.729355,-8.591920,-6.689004,-1.969113,4.958159,-0.235682,-3.693793,-9.530152,-9.651133,2.771027,-4.713689,5.961642,-5.200497,-1.614601,5.767928,2.457183,-8.724911,-6.315646,-8.907484,-5.265457,-8.920088,7.488630,4.275256,0.891977,0.700719,-9.685660,7.692094], dtype = "float32")#candidate|10133|(308,)|const|float32
call_10131 = relay.TupleGetItem(func_6077_call(relay.reshape(const_10132.astype('uint16'), [495,]), relay.reshape(const_10133.astype('float32'), [308,]), ), 1)
call_10134 = relay.TupleGetItem(func_6080_call(relay.reshape(const_10132.astype('uint16'), [495,]), relay.reshape(const_10133.astype('float32'), [308,]), ), 1)
var_10136 = relay.var("var_10136", dtype = "float32", shape = (308,))#candidate|10136|(308,)|var|float32
bop_10137 = relay.greater(const_10133.astype('bool'), relay.reshape(var_10136.astype('bool'), relay.shape_of(const_10133))) # shape=(308,)
output = relay.Tuple([bop_10123,call_10131,const_10132,bop_10137,])
output2 = relay.Tuple([bop_10126,call_10134,const_10132,bop_10137,])
func_10142 = relay.Function([var_10136,], output)
mod['func_10142'] = func_10142
mod = relay.transform.InferType()(mod)
var_10143 = relay.var("var_10143", dtype = "float32", shape = (308,))#candidate|10143|(308,)|var|float32
output = func_10142(var_10143)
func_10144 = relay.Function([var_10143], output)
mutated_mod['func_10144'] = func_10144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8051_call = mod.get_global_var('func_8051')
func_8052_call = mutated_mod.get_global_var('func_8052')
call_10156 = relay.TupleGetItem(func_8051_call(), 0)
call_10157 = relay.TupleGetItem(func_8052_call(), 0)
func_8896_call = mod.get_global_var('func_8896')
func_8899_call = mutated_mod.get_global_var('func_8899')
var_10163 = relay.var("var_10163", dtype = "float32", shape = (308,))#candidate|10163|(308,)|var|float32
call_10162 = relay.TupleGetItem(func_8896_call(relay.reshape(var_10163.astype('float32'), [1, 308])), 2)
call_10164 = relay.TupleGetItem(func_8899_call(relay.reshape(var_10163.astype('float32'), [1, 308])), 2)
func_7471_call = mod.get_global_var('func_7471')
func_7473_call = mutated_mod.get_global_var('func_7473')
call_10168 = relay.TupleGetItem(func_7471_call(), 0)
call_10169 = relay.TupleGetItem(func_7473_call(), 0)
func_6881_call = mod.get_global_var('func_6881')
func_6886_call = mutated_mod.get_global_var('func_6886')
const_10173 = relay.const([True,True,True,True,False,True,False,True,True,True,True,False,True,False,False,True,False,True,True,False,True,False,True,True,True,True,False,True,True,False,False,False,True,True,True,False,False,True,True,False,False,False,False,True,False,True,False,True,False,True,True,True,True,False,False,False,False,False,False,True,True,False,True,False,False,False,False,False,True,False,False,False,False,True,True,True,False,False,False,False,True,True,True,True,False,False,True,False,False,True,True,True,False,False,False,False,False,False,False,True,False,True,True,True,False,True,False,False,True,False,False,False,True,True,True,True,True,True,True,False,False,False,True,False,False,True,False,False,False,True,False,False,False,True,True,False,False,True,False,True,True,False,False,True,True,True,False,True,False,False,True,True,False,False,True,True,False,False,True,False,True,True,False,True,True,False,True,True,True,True,True,True,True,True,False,False,False,False,True,True,False,False,False,True,True,True,False,True,True,True,True,False,True,True,True,False,True,False,True,True,True,False,False,False,True,False,True,False,False,False,True,True,True,True,False,False,False,False,True,False,True,False,False,False,True,False,False,True,False,False,False,False,False,False,False,False,False,True,False,False,False,True,True,True,False,True,True,False,True,False,False,True,False,True,True,True,True,False,False,True,False,False,True,False,False,False,False,False,True,False,True,True,True,False,False,True,False,True,False,True,True,False,False,True,True,False,True,False,False,True,False,False,False,True,False,False,True,True,True,True,True,False,False,True,False,True,False,False,False,False,False,False,True,False,True,False,False,False,True,False,False,True,False,False,False,True,False,False,False,True,True,True,True,True,False,False,False,True,False,True,True,False,True,False,True,False,True,True,True,False,False,True,True,False,True,True,True,True,True,True,True,False,True,False,False,True,False,False,False,True,True,False,True,False,False,False,True,True,False,False,True,False,True,False,False,False,False,False,True,True,True,False,False,False,True,False,False,True,False,False,False,False,False,False,False,True,False,True,False,False,True,False,False,False,False,True,False,False,True,False,False,False,False,False,True,True,False,True,True,False,True,True,False,False,True,True,True,False,False,True,False,False,True,True,False,False,False,True,False,True,True,False,True,True,False,False,True,False,True,False,True,True,True,True,True,True,False,False,True,True,True,True,True,True,False,True,True,False,False,True,True,True,False,True,True,False,True,False,True,True,False,False,False,True,True,True,False,False,True,True,True,False,True,False,True,True,True,False,False,False,False,True,True,False,False,False,False,False,False,True,True,False,True,True,False,True,False,False,True,True,False,False,True,True,False,True,False,True,True,False,True,True,False,True,True,False,True,False,False,False,True,True,False,True,False,False,False,False,True,True,True,True,True,True,False,True,False,False,False,True,True,False,True,True,True,False,True,False,False,False,False,False,True,True,True,False,True,True,False,False,False,False,True,True,True,True,False,True,False,False,False,True,False,True,False,True,False,True,False,False,True,False,False,True,True,True,True,True,False,True,True,False,True,True,True,False,False,True,True,False,False,False,True,False,True,True,False,True,True,False,False,False,False,False,True,False,False,False,True,False,False,False,True,True,True,False,False,False,False,True,False,False,True,False,False,True,True,False,False,False,False,False,True,True,True,False,True,True,True,False,True,True,False,False,False,False,True,False,False,True,False,False,True,True,False,True,False,False,False,True,False,False,True,True,True,False,False,False,True,True,False,True,False,True,True,False,True,False,True,True,True,True,True,False,False,False,False,True,False,False,False,False,False,True,False,False,False,False,False,True,True,True,False,True,False,False,True,True,False,False,False,False,True,True,False,False,True,False,True,True,False,True,False,True,False,False,True,False,False,True,False,True,False,False,False,False,False,True,True,True,False,True,True,True,True,True,True,False,False,False,False,False,True,False,True,False,False,False,False,False,False,False,True,False,True,True,True,True,False,False,False,False,False,True,False,True,True,True,True,True,False,True,True,True,True,True,True,True,True,False,True,True,False,False,False,True,True,True,True,False,True,True,False,True,True,False,False,False,False,False,True,False,True,False,True,True,True,True,False,True,True,False,False,True,False,False,True,False,True,False,False,True,True,False,False,False,True,True,False,True,True,True,True,False,False,False,True,True,True,False,False,False,False,True,False,False,True,True,False,True,True,False,False,False,True,False,True,False,True,True,True,False,True,False,True,True,False,False,False,False,False,True,False,False,False,False,True,True,True,True,False,False,False,False,True,True,True,False,True,False,True,False,True,False,False,False,True,False,False,False,False,True,True,True,True,True,True,False,False,True,False,True,True,False,True,False,True,False,False,False,True,False,False,False,False,False,False,False,False,False,False,True,True,True,False,True,False,True,True,False,False,True,True,False,True,True,False,False,True,True,False,False,True,False,False,True,False,False,True,True,True,True,False,False,False,False,True,False,True,True,True,False,False,False,False,False,True,False,False,True,True,True,True,False,True,False,False,False,False,True,True,True,True,True,False,True,True,True,False,False,False,True,False,True,True,False,True,True,True,True,False,False,False,True,True,False,True,True,False,False,False,True,True,True,False,True,True,True,True,True,True,True,False,False,False,True,False,True,False,True,True,False,False,True,False,True,True,True,False,True,True,False,False,True,False,False,False,True,True,True,False,True,True,False,True,True,True,True,True,False,True,False,False,True,True,False,False,True,False,False,False,True,False,True,False,False,True,True,True,True,False,True,False,True,True,True,True,True,False,False,True,True,False,True,False,True,False,False,False,False,False,True,True,True,False,False,True,True,True,True,False,True,False,False,True,False,True,False,True,False,False,False,True,False,True,False,True,True,False,False,True,True,True,True,False,True,True,True,False,False,False,True,True,True,True,False,True,True,False,False,True,False,False,False,False,True,False,False,True,True,False,False,False,True,True,False,False,False,True,False,False,False,True,False,True,True,False,False,False,True,False,True,True,False,True,False,True,False,False,False,True,False,True,True,True,False,True,True,True,False,True,True,False,True,True,True,False,False,True,False,True,True,True,False,True,False,False,True,False,False,True,True,False,False,False,True,True,True,False,False,False,False,True,False,True,True,False,True,True,True,True,False,True,False,False,False,False,True,True,True,True,True,False,False,True,True,True,False,False,False,False,False,False,False,True,True,True,True,False,False,False,True,False,True,True,False,False,True,True,True,False,True,False,True,True,False,False,False,False,False,False,True,True,False,True,False,True,False,True,True,False,True,False,False,True,True,False,True,True,False,False,True,True,True,False,False,True,False,False,True,True,True,False,False,True,True,False,True,True,True,False,True,False,True,True,True,False,False,False,True,False,True,True,True,False,True,True,True,False,True,False,True,False,True,True,False,False,True,True,False,False,True,True,False,False,True,False,True,True,False,False,True,True,True,False,True,True,True,False,True,False,True,False,True,False,True,True,False,False,False,False,False,True,False,False,False,True,False,True,False,True,True,True,False,True,True,False,False,False,False,True,False,True,True,True,True,False,False,False,False,False,False,False,False,False,False,False,True,True,True,True,False,False,False,False,True,True,False,True,True,True,False,False,False,True,True,False,True,False,False,True,False,False,True,False,True,False,False,False,True,True,False,True,False,False,True,True,False,False,True,True,True,True,True,True,True,True,True,False,True,True,False,True,False,True,False,True,True,False,True,False,False,True,True,False,False,True,True,False,True,False,True,False,False,True,True,True,False], dtype = "bool")#candidate|10173|(1568,)|const|bool
var_10174 = relay.var("var_10174", dtype = "float64", shape = (11, 66))#candidate|10174|(11, 66)|var|float64
call_10172 = relay.TupleGetItem(func_6881_call(relay.reshape(const_10173.astype('bool'), [14, 7, 16]), relay.reshape(const_10173.astype('bool'), [14, 7, 16]), relay.reshape(var_10174.astype('float64'), [726,]), ), 1)
call_10175 = relay.TupleGetItem(func_6886_call(relay.reshape(const_10173.astype('bool'), [14, 7, 16]), relay.reshape(const_10173.astype('bool'), [14, 7, 16]), relay.reshape(var_10174.astype('float64'), [726,]), ), 1)
func_8998_call = mod.get_global_var('func_8998')
func_9002_call = mutated_mod.get_global_var('func_9002')
var_10177 = relay.var("var_10177", dtype = "int32", shape = (640,))#candidate|10177|(640,)|var|int32
var_10178 = relay.var("var_10178", dtype = "bool", shape = (312,))#candidate|10178|(312,)|var|bool
call_10176 = relay.TupleGetItem(func_8998_call(relay.reshape(var_10177.astype('int32'), [8, 16, 5]), relay.reshape(var_10178.astype('bool'), [3, 104]), ), 2)
call_10179 = relay.TupleGetItem(func_9002_call(relay.reshape(var_10177.astype('int32'), [8, 16, 5]), relay.reshape(var_10178.astype('bool'), [3, 104]), ), 2)
output = relay.Tuple([call_10156,call_10162,var_10163,call_10168,call_10172,const_10173,var_10174,call_10176,var_10177,var_10178,])
output2 = relay.Tuple([call_10157,call_10164,var_10163,call_10169,call_10175,const_10173,var_10174,call_10179,var_10177,var_10178,])
func_10181 = relay.Function([var_10163,var_10174,var_10177,var_10178,], output)
mod['func_10181'] = func_10181
mod = relay.transform.InferType()(mod)
var_10182 = relay.var("var_10182", dtype = "float32", shape = (308,))#candidate|10182|(308,)|var|float32
var_10183 = relay.var("var_10183", dtype = "float64", shape = (11, 66))#candidate|10183|(11, 66)|var|float64
var_10184 = relay.var("var_10184", dtype = "int32", shape = (640,))#candidate|10184|(640,)|var|int32
var_10185 = relay.var("var_10185", dtype = "bool", shape = (312,))#candidate|10185|(312,)|var|bool
output = func_10181(var_10182,var_10183,var_10184,var_10185,)
func_10186 = relay.Function([var_10182,var_10183,var_10184,var_10185,], output)
mutated_mod['func_10186'] = func_10186
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9366_call = mod.get_global_var('func_9366')
func_9367_call = mutated_mod.get_global_var('func_9367')
call_10209 = relay.TupleGetItem(func_9366_call(), 0)
call_10210 = relay.TupleGetItem(func_9367_call(), 0)
var_10220 = relay.var("var_10220", dtype = "float32", shape = (2, 12, 15))#candidate|10220|(2, 12, 15)|var|float32
bop_10221 = relay.logical_or(call_10209.astype('bool'), var_10220.astype('bool')) # shape=(2, 12, 15)
bop_10224 = relay.logical_or(call_10210.astype('bool'), var_10220.astype('bool')) # shape=(2, 12, 15)
func_2536_call = mod.get_global_var('func_2536')
func_2539_call = mutated_mod.get_global_var('func_2539')
const_10226 = relay.const([-4.967968,5.103912,-2.293611,2.604205,-3.435921,9.220514,-8.970714,-5.386795,-6.022804,2.889293,9.834657,5.167883,8.873290,-2.837412,-1.117754,-0.907299,-8.831417,9.298363,-3.978077,-0.750667,1.388536,-7.792405,-8.283142,-9.743678,0.624539,-4.447180,2.561602,-3.694304,6.842259,8.419358,0.647144,4.341610,-8.824184,-8.262710,7.451627,7.234181,-1.589360,8.276259,6.374421,-6.919958,7.678968,5.689213,-3.562869,1.560270,-0.427229,-3.719521,-2.513538,7.179178,-4.468584,3.241793,-5.202396,3.449119,-0.068856,-0.543118,-0.094824,8.562763,6.902766,1.811749,-5.612821,8.292574,8.997203,-6.565285,2.150593,-5.761687,-7.419535,-1.068224,8.175866,0.759467,-0.491816,0.024873,-0.325230,-5.653039,2.439072,-6.421325,-4.354407,-2.050067,8.390395,4.041538,7.032654,-4.484227,-2.661782,-4.242339,-9.655979,2.597663,8.963111,-1.699987,6.646560,5.350473,-3.396421,-7.364461,-7.648579,-7.241975,-2.072268,-9.190846,-2.658117,0.515386,7.497942,-2.334581,3.149530,-3.172329,-6.190614,4.684743,3.858509,-5.768685,-1.214203,-2.495126,1.138695,-4.453214,3.796812,2.121210,0.939326,-8.018482], dtype = "float64")#candidate|10226|(112,)|const|float64
call_10225 = relay.TupleGetItem(func_2536_call(relay.reshape(const_10226.astype('float64'), [16, 1, 7])), 0)
call_10227 = relay.TupleGetItem(func_2539_call(relay.reshape(const_10226.astype('float64'), [16, 1, 7])), 0)
func_7104_call = mod.get_global_var('func_7104')
func_7106_call = mutated_mod.get_global_var('func_7106')
call_10240 = func_7104_call()
call_10241 = func_7104_call()
var_10244 = relay.var("var_10244", dtype = "float32", shape = (10, 12, 15))#candidate|10244|(10, 12, 15)|var|float32
bop_10245 = relay.floor_divide(call_10209.astype('float64'), var_10244.astype('float64')) # shape=(10, 12, 15)
bop_10248 = relay.floor_divide(call_10210.astype('float64'), var_10244.astype('float64')) # shape=(10, 12, 15)
output = relay.Tuple([bop_10221,call_10225,const_10226,call_10240,bop_10245,])
output2 = relay.Tuple([bop_10224,call_10227,const_10226,call_10241,bop_10248,])
func_10256 = relay.Function([var_10220,var_10244,], output)
mod['func_10256'] = func_10256
mod = relay.transform.InferType()(mod)
var_10257 = relay.var("var_10257", dtype = "float32", shape = (2, 12, 15))#candidate|10257|(2, 12, 15)|var|float32
var_10258 = relay.var("var_10258", dtype = "float32", shape = (10, 12, 15))#candidate|10258|(10, 12, 15)|var|float32
output = func_10256(var_10257,var_10258,)
func_10259 = relay.Function([var_10257,var_10258,], output)
mutated_mod['func_10259'] = func_10259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7501_call = mod.get_global_var('func_7501')
func_7502_call = mutated_mod.get_global_var('func_7502')
call_10276 = relay.TupleGetItem(func_7501_call(), 0)
call_10277 = relay.TupleGetItem(func_7502_call(), 0)
output = call_10276
output2 = call_10277
func_10294 = relay.Function([], output)
mod['func_10294'] = func_10294
mod = relay.transform.InferType()(mod)
output = func_10294()
func_10295 = relay.Function([], output)
mutated_mod['func_10295'] = func_10295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8051_call = mod.get_global_var('func_8051')
func_8052_call = mutated_mod.get_global_var('func_8052')
call_10342 = relay.TupleGetItem(func_8051_call(), 0)
call_10343 = relay.TupleGetItem(func_8052_call(), 0)
func_7571_call = mod.get_global_var('func_7571')
func_7573_call = mutated_mod.get_global_var('func_7573')
var_10367 = relay.var("var_10367", dtype = "float64", shape = (112,))#candidate|10367|(112,)|var|float64
call_10366 = relay.TupleGetItem(func_7571_call(relay.reshape(var_10367.astype('float64'), [112,])), 1)
call_10368 = relay.TupleGetItem(func_7573_call(relay.reshape(var_10367.astype('float64'), [112,])), 1)
uop_10387 = relay.asin(call_10366.astype('float64')) # shape=(1, 12, 15)
uop_10389 = relay.asin(call_10368.astype('float64')) # shape=(1, 12, 15)
bop_10400 = relay.left_shift(call_10342.astype('uint64'), relay.reshape(uop_10387.astype('uint64'), relay.shape_of(call_10342))) # shape=(1, 12, 15)
bop_10403 = relay.left_shift(call_10343.astype('uint64'), relay.reshape(uop_10389.astype('uint64'), relay.shape_of(call_10343))) # shape=(1, 12, 15)
output = relay.Tuple([var_10367,bop_10400,])
output2 = relay.Tuple([var_10367,bop_10403,])
F = relay.Function([var_10367,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_10367,], output2)
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
