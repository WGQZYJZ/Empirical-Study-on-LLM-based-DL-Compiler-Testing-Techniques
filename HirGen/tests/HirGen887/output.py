import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_20 = relay.var("var_20", dtype = "float64", shape = (2, 4, 6))#candidate|20|(2, 4, 6)|var|float64
uop_21 = relay.sqrt(var_20.astype('float64')) # shape=(2, 4, 6)
output = relay.Tuple([uop_21,])
output2 = relay.Tuple([uop_21,])
func_32 = relay.Function([var_20,], output)
mod['func_32'] = func_32
mod = relay.transform.InferType()(mod)
mutated_mod['func_32'] = func_32
mutated_mod = relay.transform.InferType()(mutated_mod)
var_33 = relay.var("var_33", dtype = "float64", shape = (2, 4, 6))#candidate|33|(2, 4, 6)|var|float64
func_32_call = mutated_mod.get_global_var('func_32')
call_34 = func_32_call(var_33)
output = call_34
func_35 = relay.Function([var_33], output)
mutated_mod['func_35'] = func_35
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1829 = relay.var("var_1829", dtype = "int16", shape = (15, 1, 11))#candidate|1829|(15, 1, 11)|var|int16
var_1830 = relay.var("var_1830", dtype = "int16", shape = (15, 5, 11))#candidate|1830|(15, 5, 11)|var|int16
bop_1831 = relay.left_shift(var_1829.astype('int16'), var_1830.astype('int16')) # shape=(15, 5, 11)
output = relay.Tuple([bop_1831,])
output2 = relay.Tuple([bop_1831,])
func_1835 = relay.Function([var_1829,var_1830,], output)
mod['func_1835'] = func_1835
mod = relay.transform.InferType()(mod)
var_1836 = relay.var("var_1836", dtype = "int16", shape = (15, 1, 11))#candidate|1836|(15, 1, 11)|var|int16
var_1837 = relay.var("var_1837", dtype = "int16", shape = (15, 5, 11))#candidate|1837|(15, 5, 11)|var|int16
output = func_1835(var_1836,var_1837,)
func_1838 = relay.Function([var_1836,var_1837,], output)
mutated_mod['func_1838'] = func_1838
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2634 = relay.var("var_2634", dtype = "float32", shape = (1, 8, 10))#candidate|2634|(1, 8, 10)|var|float32
uop_2635 = relay.atan(var_2634.astype('float32')) # shape=(1, 8, 10)
func_1835_call = mod.get_global_var('func_1835')
func_1838_call = mutated_mod.get_global_var('func_1838')
const_2644 = relay.const([[-7],[2],[-9],[1],[-7],[2],[-10],[9],[-7],[3],[-1],[-7],[-9],[3],[-5],[10],[1],[-7],[2],[-10],[8],[2],[5],[8],[-2],[-9],[-1],[-5],[-7],[10],[9],[-2],[-1],[-1],[-1],[-5],[-1],[9],[-6],[7],[9],[5],[2],[10],[2],[1],[-7],[10],[-4],[-2],[-1],[5],[4],[7],[2],[-10],[-2],[3],[-8],[-5],[-1],[10],[9],[-8],[2],[-7],[-7],[-7],[6],[-10],[10],[1],[8],[-5],[-5],[5],[-7],[5],[-6],[9],[3],[10],[-10],[-2],[3],[-7],[4],[4],[-2],[-8],[-1],[4],[-7],[-4],[-2],[-10],[-10],[-6],[9],[7],[9],[-4],[1],[-5],[-7],[3],[-6],[-6],[8],[8],[4],[4],[10],[2],[-7],[3],[4],[9],[3],[2],[6],[10],[2],[7],[-7],[-1],[-4],[-4],[-6],[-6],[-7],[7],[6],[9],[-9],[-1],[-4],[-1],[8],[-10],[4],[7],[8],[-2],[10],[-7],[7],[-10],[-1],[2],[10],[7],[6],[-4],[-7],[-1],[-6],[8],[-2],[10],[8],[-2],[-1],[-10],[1]], dtype = "int16")#candidate|2644|(165, 1)|const|int16
var_2645 = relay.var("var_2645", dtype = "int16", shape = (5, 165))#candidate|2645|(5, 165)|var|int16
call_2643 = relay.TupleGetItem(func_1835_call(relay.reshape(const_2644.astype('int16'), [15, 1, 11]), relay.reshape(var_2645.astype('int16'), [15, 5, 11]), ), 0)
call_2646 = relay.TupleGetItem(func_1838_call(relay.reshape(const_2644.astype('int16'), [15, 1, 11]), relay.reshape(var_2645.astype('int16'), [15, 5, 11]), ), 0)
func_32_call = mod.get_global_var('func_32')
func_35_call = mutated_mod.get_global_var('func_35')
var_2648 = relay.var("var_2648", dtype = "float64", shape = (48,))#candidate|2648|(48,)|var|float64
call_2647 = relay.TupleGetItem(func_32_call(relay.reshape(var_2648.astype('float64'), [2, 4, 6])), 0)
call_2649 = relay.TupleGetItem(func_35_call(relay.reshape(var_2648.astype('float64'), [2, 4, 6])), 0)
func_1835_call = mod.get_global_var('func_1835')
func_1838_call = mutated_mod.get_global_var('func_1838')
call_2651 = relay.TupleGetItem(func_1835_call(relay.reshape(const_2644.astype('int16'), [15, 1, 11]), relay.reshape(var_2645.astype('int16'), [15, 5, 11]), ), 0)
call_2652 = relay.TupleGetItem(func_1838_call(relay.reshape(const_2644.astype('int16'), [15, 1, 11]), relay.reshape(var_2645.astype('int16'), [15, 5, 11]), ), 0)
func_1835_call = mod.get_global_var('func_1835')
func_1838_call = mutated_mod.get_global_var('func_1838')
call_2653 = relay.TupleGetItem(func_1835_call(relay.reshape(const_2644.astype('int16'), [15, 1, 11]), relay.reshape(call_2643.astype('int16'), [15, 5, 11]), ), 0)
call_2654 = relay.TupleGetItem(func_1838_call(relay.reshape(const_2644.astype('int16'), [15, 1, 11]), relay.reshape(call_2643.astype('int16'), [15, 5, 11]), ), 0)
func_1835_call = mod.get_global_var('func_1835')
func_1838_call = mutated_mod.get_global_var('func_1838')
call_2662 = relay.TupleGetItem(func_1835_call(relay.reshape(const_2644.astype('int16'), [15, 1, 11]), relay.reshape(var_2645.astype('int16'), [15, 5, 11]), ), 0)
call_2663 = relay.TupleGetItem(func_1838_call(relay.reshape(const_2644.astype('int16'), [15, 1, 11]), relay.reshape(var_2645.astype('int16'), [15, 5, 11]), ), 0)
func_1835_call = mod.get_global_var('func_1835')
func_1838_call = mutated_mod.get_global_var('func_1838')
call_2665 = relay.TupleGetItem(func_1835_call(relay.reshape(const_2644.astype('int16'), [15, 1, 11]), relay.reshape(call_2653.astype('int16'), [15, 5, 11]), ), 0)
call_2666 = relay.TupleGetItem(func_1838_call(relay.reshape(const_2644.astype('int16'), [15, 1, 11]), relay.reshape(call_2653.astype('int16'), [15, 5, 11]), ), 0)
output = relay.Tuple([uop_2635,call_2643,const_2644,var_2645,call_2647,var_2648,call_2651,call_2653,call_2662,call_2665,])
output2 = relay.Tuple([uop_2635,call_2646,const_2644,var_2645,call_2649,var_2648,call_2652,call_2654,call_2663,call_2666,])
func_2680 = relay.Function([var_2634,var_2645,var_2648,], output)
mod['func_2680'] = func_2680
mod = relay.transform.InferType()(mod)
mutated_mod['func_2680'] = func_2680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2680_call = mutated_mod.get_global_var('func_2680')
var_2682 = relay.var("var_2682", dtype = "float32", shape = (1, 8, 10))#candidate|2682|(1, 8, 10)|var|float32
var_2683 = relay.var("var_2683", dtype = "int16", shape = (5, 165))#candidate|2683|(5, 165)|var|int16
var_2684 = relay.var("var_2684", dtype = "float64", shape = (48,))#candidate|2684|(48,)|var|float64
call_2681 = func_2680_call(var_2682,var_2683,var_2684,)
output = call_2681
func_2685 = relay.Function([var_2682,var_2683,var_2684,], output)
mutated_mod['func_2685'] = func_2685
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3114 = relay.var("var_3114", dtype = "float64", shape = (10, 4, 2))#candidate|3114|(10, 4, 2)|var|float64
uop_3115 = relay.acosh(var_3114.astype('float64')) # shape=(10, 4, 2)
func_2680_call = mod.get_global_var('func_2680')
func_2685_call = mutated_mod.get_global_var('func_2685')
var_3123 = relay.var("var_3123", dtype = "int16", shape = (825,))#candidate|3123|(825,)|var|int16
const_3124 = relay.const([-3.109643,-1.480843,6.204467,5.364579,-7.702628,2.488852,6.061535,-1.803314,7.731093,1.934525,4.629150,5.401755,-1.201839,7.095712,-6.831804,5.216052,7.690922,5.656586,7.636740,-3.182215,6.109357,-1.158616,-1.286266,-1.769512,4.868967,1.210086,6.614649,-7.041516,6.457919,0.969533,1.449500,2.495703,3.045565,6.628981,6.506883,-3.748790,9.359113,-0.118664,2.977581,4.643043,-3.765361,4.974867,-9.314810,4.506946,-6.773792,9.320977,4.005541,-9.228191], dtype = "float64")#candidate|3124|(48,)|const|float64
call_3122 = relay.TupleGetItem(func_2680_call(relay.reshape(uop_3115.astype('float32'), [1, 8, 10]), relay.reshape(var_3123.astype('int16'), [5, 165]), relay.reshape(const_3124.astype('float64'), [48,]), ), 9)
call_3125 = relay.TupleGetItem(func_2685_call(relay.reshape(uop_3115.astype('float32'), [1, 8, 10]), relay.reshape(var_3123.astype('int16'), [5, 165]), relay.reshape(const_3124.astype('float64'), [48,]), ), 9)
bop_3140 = relay.mod(uop_3115.astype('float64'), relay.reshape(var_3114.astype('float64'), relay.shape_of(uop_3115))) # shape=(10, 4, 2)
func_1835_call = mod.get_global_var('func_1835')
func_1838_call = mutated_mod.get_global_var('func_1838')
var_3146 = relay.var("var_3146", dtype = "int16", shape = (165,))#candidate|3146|(165,)|var|int16
call_3145 = relay.TupleGetItem(func_1835_call(relay.reshape(var_3146.astype('int16'), [15, 1, 11]), relay.reshape(call_3122.astype('int16'), [15, 5, 11]), ), 0)
call_3147 = relay.TupleGetItem(func_1838_call(relay.reshape(var_3146.astype('int16'), [15, 1, 11]), relay.reshape(call_3122.astype('int16'), [15, 5, 11]), ), 0)
output = relay.Tuple([call_3122,var_3123,const_3124,bop_3140,call_3145,var_3146,])
output2 = relay.Tuple([call_3125,var_3123,const_3124,bop_3140,call_3147,var_3146,])
func_3152 = relay.Function([var_3114,var_3123,var_3146,], output)
mod['func_3152'] = func_3152
mod = relay.transform.InferType()(mod)
mutated_mod['func_3152'] = func_3152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3152_call = mutated_mod.get_global_var('func_3152')
var_3154 = relay.var("var_3154", dtype = "float64", shape = (10, 4, 2))#candidate|3154|(10, 4, 2)|var|float64
var_3155 = relay.var("var_3155", dtype = "int16", shape = (825,))#candidate|3155|(825,)|var|int16
var_3156 = relay.var("var_3156", dtype = "int16", shape = (165,))#candidate|3156|(165,)|var|int16
call_3153 = func_3152_call(var_3154,var_3155,var_3156,)
output = call_3153
func_3157 = relay.Function([var_3154,var_3155,var_3156,], output)
mutated_mod['func_3157'] = func_3157
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3600 = relay.var("var_3600", dtype = "float32", shape = (5, 4, 16))#candidate|3600|(5, 4, 16)|var|float32
uop_3601 = relay.log(var_3600.astype('float32')) # shape=(5, 4, 16)
func_1835_call = mod.get_global_var('func_1835')
func_1838_call = mutated_mod.get_global_var('func_1838')
var_3616 = relay.var("var_3616", dtype = "int16", shape = (11, 15))#candidate|3616|(11, 15)|var|int16
const_3617 = relay.const([[5,-10,7,10,3,3,6,-8,-1,6,3,-5,-4,7,-8,4,5,10,3,8,-7,-3,6,1,2,-9,3,-2,-3,-4,6,-6,5,4,5,4,-4,-9,10,2,-5,9,-2,-8,-3,-6,2,1,8,-5,-7,7,8,4,5,-2,-4,10,-5,1,-3,-9,8,2,5,-9,8,4,3,8,3,-10,-4,-2,-1,8,-1,6,-9,5,8,6,1,6,5,2,5,-4,-4,-7,-1,-6,-4,-2,-3,-6,-3,8,10,8,7,5,3,10,-8,-10,-10,1,-9,6,2,-4,2,-8,6,-10,-7,-7,-4,10,4,1,8,-7,-7,-10,4,-3,-6,1,-9,8,-7,8,2,5,10,9,10,-5,-10,7,7,-2,-2,-6,5,-9,-9,-8,-7,-6,-1,-2,-4,9,2,-7,7,-3,-4,10,-2,-4,7],[1,-4,-8,-3,-7,9,-10,5,3,9,-1,-4,-2,1,7,-7,10,7,-8,10,7,3,-4,7,10,-1,6,-3,6,-4,2,3,-3,-1,1,6,3,-9,10,4,9,3,3,-4,2,1,-9,7,5,5,-9,7,-2,1,-10,6,-10,-7,-6,3,-10,1,9,3,4,-3,1,-9,4,-7,-2,-6,-1,-7,-5,-5,5,4,4,9,7,4,-1,3,10,-2,4,-7,2,-3,2,-9,4,10,-5,7,-2,2,-4,1,-4,8,-2,4,-9,-10,-5,-8,4,-8,-1,-3,-7,-8,-7,-7,-3,-2,10,-10,2,-1,-1,-5,-9,6,-9,-4,-1,7,3,-10,9,-3,7,-9,5,6,-9,3,-6,-9,-5,9,-7,-3,-2,-7,6,-1,5,-3,-10,-8,-2,8,-7,10,9,-7,8,7,4,1,5],[-4,2,1,-6,2,10,-3,6,-9,3,-3,8,10,-5,-4,5,-1,5,10,2,7,-1,-9,4,-3,-3,-9,-8,3,-10,-4,-4,3,-10,9,6,-4,-8,3,10,-10,-4,-6,-8,6,7,-4,-8,8,-9,-7,-7,-1,3,-7,-1,8,6,8,4,-1,-5,-9,1,10,-8,-4,-8,-8,-8,-8,3,-2,1,-10,-3,3,7,2,3,5,-9,-4,1,-1,-8,8,4,-10,-10,-7,5,-5,-4,-8,9,6,-2,6,-6,-2,6,8,2,3,10,6,-2,6,10,-2,-7,6,3,-3,-10,3,-7,-6,-9,-2,10,4,1,-7,6,-7,-10,-4,-8,9,-4,-4,3,1,-8,1,-10,-8,-7,-9,4,5,2,6,6,8,8,-4,-9,-3,7,4,8,-10,7,-7,-7,7,-2,9,-8,2,8,-7],[1,5,3,-7,9,6,-7,9,7,-3,-8,-1,-1,4,-6,-6,10,-5,9,6,7,6,-8,8,-2,6,-5,-6,-7,6,1,8,-3,6,5,4,7,6,6,9,-8,7,10,-2,4,-10,-9,-8,-3,8,8,10,1,-9,3,-6,4,4,9,-3,-3,-7,3,-7,-2,6,7,5,3,7,-3,7,-8,-1,9,7,-7,4,-2,8,-6,-3,-10,2,-2,9,4,1,9,9,4,-9,2,2,-4,9,-3,-4,-9,-4,5,-6,-3,1,9,-9,-5,5,-4,3,-5,10,5,1,-10,6,-10,6,-9,7,-6,10,-7,-1,2,-10,6,-7,6,4,-4,-3,3,10,-6,-10,3,4,-7,-10,-8,-7,10,7,3,2,-2,-2,4,-4,8,5,-4,-1,5,-1,10,9,-4,-6,8,2,2,-4,7],[9,2,5,4,-8,-7,-1,-4,7,-9,-5,-10,6,3,10,-7,-3,4,6,6,-6,2,-10,-10,-6,-9,-7,-8,-4,-2,-10,5,10,3,-7,2,2,3,-10,-8,-3,7,-9,-2,5,7,-4,9,2,-2,3,-4,-7,6,1,6,-2,-1,-10,-3,-8,-2,-3,-6,5,7,3,-2,10,2,1,-3,-4,3,9,1,-6,-10,6,-5,-6,-10,4,1,-9,5,-2,-2,-5,10,-2,-1,-6,7,-7,-2,5,-3,-3,4,9,1,-10,-8,9,-10,1,-7,-4,-8,1,5,-3,6,3,9,1,-3,-2,-5,3,1,-9,-10,5,4,-9,3,-7,9,10,4,-5,-2,10,-9,3,6,10,-4,3,2,-9,5,3,8,9,5,-8,4,-4,-10,2,-8,-9,7,2,-7,2,1,-3,9,10,7,-8]], dtype = "int16")#candidate|3617|(5, 165)|const|int16
call_3615 = relay.TupleGetItem(func_1835_call(relay.reshape(var_3616.astype('int16'), [15, 1, 11]), relay.reshape(const_3617.astype('int16'), [15, 5, 11]), ), 0)
call_3618 = relay.TupleGetItem(func_1838_call(relay.reshape(var_3616.astype('int16'), [15, 1, 11]), relay.reshape(const_3617.astype('int16'), [15, 5, 11]), ), 0)
var_3622 = relay.var("var_3622", dtype = "float32", shape = (5, 4, 16))#candidate|3622|(5, 4, 16)|var|float32
bop_3623 = relay.logical_or(uop_3601.astype('bool'), relay.reshape(var_3622.astype('bool'), relay.shape_of(uop_3601))) # shape=(5, 4, 16)
func_2680_call = mod.get_global_var('func_2680')
func_2685_call = mutated_mod.get_global_var('func_2685')
const_3644 = relay.const([9.040044,8.105048,5.238838,9.482752,-5.042952,-6.203360,8.831379,1.497038,-5.339979,-8.639997,1.196139,-2.802063,-6.449927,-7.449282,1.327657,-6.161912,-3.505521,-8.911147,-2.003729,5.582116,-6.127546,7.193863,2.552909,-7.518259,-6.326768,-4.418402,8.377106,-4.046214,-6.298978,-8.868767,1.758233,9.224629,-1.630501,5.704469,5.092998,9.534032,-1.941405,1.491237,-6.180509,5.023999,-7.272050,-5.587727,3.271847,-9.443890,5.582698,5.486081,7.622623,-1.779440,-0.063753,-3.026104,-1.629144,2.230004,-2.390084,6.230547,-9.437228,1.459172,-5.347289,8.785844,2.632769,-4.049708,-1.224706,7.663074,-1.953810,5.876275,3.295783,-3.225356,-7.601973,-6.751814,-9.554505,0.317466,-7.340495,8.287929,-3.660524,-5.851310,-6.412415,-0.735101,-6.938919,-7.698408,4.436888,4.473811], dtype = "float32")#candidate|3644|(80,)|const|float32
const_3645 = relay.const([-2.351481,9.900056,2.261028,0.969385,-1.919481,3.921045,7.311013,1.793590,-4.282573,6.762089,-4.881597,-5.564506,0.016607,4.623105,5.011184,-9.864862,-2.389369,9.779042,5.276375,3.421441,-5.297201,1.336724,-5.848014,7.696207,-1.189897,-9.156174,-4.014615,5.600966,-4.700014,-8.340879,4.885577,-6.217742,-9.257674,2.666627,-0.122522,7.429331,8.741777,-7.127301,-5.645574,-9.089627,-2.190394,0.602922,-9.202250,-9.612575,-8.515031,-6.822725,2.739907,9.445598], dtype = "float64")#candidate|3645|(48,)|const|float64
call_3643 = relay.TupleGetItem(func_2680_call(relay.reshape(const_3644.astype('float32'), [1, 8, 10]), relay.reshape(const_3617.astype('int16'), [5, 165]), relay.reshape(const_3645.astype('float64'), [48,]), ), 2)
call_3646 = relay.TupleGetItem(func_2685_call(relay.reshape(const_3644.astype('float32'), [1, 8, 10]), relay.reshape(const_3617.astype('int16'), [5, 165]), relay.reshape(const_3645.astype('float64'), [48,]), ), 2)
func_3152_call = mod.get_global_var('func_3152')
func_3157_call = mutated_mod.get_global_var('func_3157')
call_3653 = relay.TupleGetItem(func_3152_call(relay.reshape(const_3644.astype('float64'), [10, 4, 2]), relay.reshape(call_3615.astype('int16'), [825,]), relay.reshape(var_3616.astype('int16'), [165,]), ), 1)
call_3654 = relay.TupleGetItem(func_3157_call(relay.reshape(const_3644.astype('float64'), [10, 4, 2]), relay.reshape(call_3615.astype('int16'), [825,]), relay.reshape(var_3616.astype('int16'), [165,]), ), 1)
func_32_call = mod.get_global_var('func_32')
func_35_call = mutated_mod.get_global_var('func_35')
call_3674 = relay.TupleGetItem(func_32_call(relay.reshape(const_3645.astype('float64'), [2, 4, 6])), 0)
call_3675 = relay.TupleGetItem(func_35_call(relay.reshape(const_3645.astype('float64'), [2, 4, 6])), 0)
bop_3681 = relay.right_shift(var_3600.astype('uint8'), relay.reshape(bop_3623.astype('uint8'), relay.shape_of(var_3600))) # shape=(5, 4, 16)
output = relay.Tuple([call_3615,var_3616,const_3617,call_3643,const_3644,const_3645,call_3653,call_3674,bop_3681,])
output2 = relay.Tuple([call_3618,var_3616,const_3617,call_3646,const_3644,const_3645,call_3654,call_3675,bop_3681,])
func_3695 = relay.Function([var_3600,var_3616,var_3622,], output)
mod['func_3695'] = func_3695
mod = relay.transform.InferType()(mod)
mutated_mod['func_3695'] = func_3695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3695_call = mutated_mod.get_global_var('func_3695')
var_3697 = relay.var("var_3697", dtype = "float32", shape = (5, 4, 16))#candidate|3697|(5, 4, 16)|var|float32
var_3698 = relay.var("var_3698", dtype = "int16", shape = (11, 15))#candidate|3698|(11, 15)|var|int16
var_3699 = relay.var("var_3699", dtype = "float32", shape = (5, 4, 16))#candidate|3699|(5, 4, 16)|var|float32
call_3696 = func_3695_call(var_3697,var_3698,var_3699,)
output = call_3696
func_3700 = relay.Function([var_3697,var_3698,var_3699,], output)
mutated_mod['func_3700'] = func_3700
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4220 = relay.const([[[8.175890,-6.369707,-6.109010,-9.767946,-4.353995,-2.166963,-0.460080,-2.708695,-4.807482,8.704039],[6.949513,4.047300,9.788294,-9.761044,-3.480612,-6.322094,2.511875,-7.480141,4.046439,-2.927564],[2.821082,-4.156417,-5.279050,5.569518,9.991941,-3.943927,6.311626,1.946853,-2.363038,-8.403260],[-4.306277,-5.191962,5.797935,6.917592,0.353618,-5.235325,-8.311974,1.383624,-3.916686,5.731286],[0.412955,-0.012593,-9.341889,-8.884584,4.689468,3.804120,8.263429,-8.408118,-4.333898,0.537719],[0.883414,3.641610,1.029804,4.859426,5.019666,2.045156,-6.869787,4.412770,-1.518814,9.321804],[8.244864,1.357304,6.447365,4.192834,3.995539,1.208143,1.529921,-8.476062,8.183777,-9.029211],[3.275300,-4.034054,6.469445,-7.558123,7.480688,-8.980806,-6.959684,3.308302,5.633156,3.321409],[-5.071456,5.555970,2.386110,-4.810258,3.071343,-0.511117,-6.444132,5.571333,-1.192229,8.298126],[8.609493,-3.283700,4.466867,7.564108,5.107746,8.927011,-2.440528,4.205466,3.223375,-1.839118]]], dtype = "float64")#candidate|4220|(1, 10, 10)|const|float64
uop_4221 = relay.sigmoid(const_4220.astype('float64')) # shape=(1, 10, 10)
output = relay.Tuple([uop_4221,])
output2 = relay.Tuple([uop_4221,])
func_4227 = relay.Function([], output)
mod['func_4227'] = func_4227
mod = relay.transform.InferType()(mod)
output = func_4227()
func_4228 = relay.Function([], output)
mutated_mod['func_4228'] = func_4228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4227_call = mod.get_global_var('func_4227')
func_4228_call = mutated_mod.get_global_var('func_4228')
call_4271 = relay.TupleGetItem(func_4227_call(), 0)
call_4272 = relay.TupleGetItem(func_4228_call(), 0)
func_3695_call = mod.get_global_var('func_3695')
func_3700_call = mutated_mod.get_global_var('func_3700')
var_4274 = relay.var("var_4274", dtype = "float32", shape = (320,))#candidate|4274|(320,)|var|float32
const_4275 = relay.const([[-3,-4,9,-10,-2],[-3,3,5,6,7],[1,-10,1,8,9],[4,4,-7,-7,-8],[-2,-9,6,8,-7],[-5,-10,5,-3,1],[-2,-6,-4,-3,-1],[-1,-1,-7,-4,10],[-1,4,-2,-5,2],[8,3,-2,8,10],[-4,2,3,4,-4],[1,-9,-1,3,-5],[3,9,-9,3,-4],[-7,-5,-6,8,-6],[-4,10,-3,4,6],[-1,3,5,8,-9],[2,-5,-5,-5,-2],[-5,-9,10,5,-8],[-3,2,-8,8,-6],[2,-1,4,7,10],[2,6,2,3,-9],[-10,1,-8,10,7],[-1,3,6,-9,-7],[-2,6,-10,3,-6],[6,7,-10,10,-9],[6,-8,3,4,-6],[-2,-10,6,7,-5],[4,-10,1,-5,2],[8,3,4,-9,-1],[3,-3,4,-5,1],[-5,-1,5,5,-1],[-4,-4,6,-7,10],[7,-3,-6,-10,-7]], dtype = "int16")#candidate|4275|(33, 5)|const|int16
call_4273 = relay.TupleGetItem(func_3695_call(relay.reshape(var_4274.astype('float32'), [5, 4, 16]), relay.reshape(const_4275.astype('int16'), [11, 15]), relay.reshape(var_4274.astype('float32'), [5, 4, 16]), ), 2)
call_4276 = relay.TupleGetItem(func_3700_call(relay.reshape(var_4274.astype('float32'), [5, 4, 16]), relay.reshape(const_4275.astype('int16'), [11, 15]), relay.reshape(var_4274.astype('float32'), [5, 4, 16]), ), 2)
var_4288 = relay.var("var_4288", dtype = "int16", shape = (5, 165))#candidate|4288|(5, 165)|var|int16
bop_4289 = relay.not_equal(call_4273.astype('bool'), relay.reshape(var_4288.astype('bool'), relay.shape_of(call_4273))) # shape=(5, 165)
bop_4292 = relay.not_equal(call_4276.astype('bool'), relay.reshape(var_4288.astype('bool'), relay.shape_of(call_4276))) # shape=(5, 165)
bop_4301 = relay.logical_or(var_4288.astype('bool'), relay.reshape(call_4273.astype('bool'), relay.shape_of(var_4288))) # shape=(5, 165)
bop_4304 = relay.logical_or(var_4288.astype('bool'), relay.reshape(call_4276.astype('bool'), relay.shape_of(var_4288))) # shape=(5, 165)
const_4306 = relay.const([[False,True,False,True,True,False,True,False,True,False,True,True,False,True,False,False,False,False,True,False,False,True,False,True,True,True,True,False,False,True,False,False,True,False,True,False,True,True,True,False,True,False,True,True,True,False,True,False,False,True,False,True,False,True,False,True,False,True,False,False,True,False,False,False,True,False,False,False,True,True,False,False,True,True,True,True,True,False,True,False,True,True,True,True,False,True,True,True,False,True,True,True,True,False,True,False,False,False,False,True,True,False,True,True,False,False,False,True,False,True,True,False,False,False,True,True,True,False,False,False,True,True,True,True,True,True,True,True,True,False,False,False,False,True,True,False,True,True,False,False,False,True,False,True,False,True,False,True,False,False,True,True,True,True,False,True,False,False,False,True,False,True,True,False,False],[True,True,False,False,True,False,True,False,False,False,False,True,False,False,True,False,True,True,True,False,True,False,False,True,True,True,True,False,True,False,False,False,True,False,False,False,False,True,False,False,True,True,False,True,True,True,True,False,False,True,True,False,True,True,True,False,True,True,False,False,True,True,False,False,True,False,False,False,False,False,False,True,True,False,True,False,False,False,True,False,True,False,False,True,True,False,True,False,True,False,False,False,True,False,False,False,True,False,False,True,False,True,False,False,True,True,False,True,False,True,False,True,True,False,False,True,False,False,True,True,False,False,True,True,False,True,True,True,True,False,False,False,True,True,False,False,False,False,False,False,False,False,False,True,False,False,False,True,False,False,False,False,False,False,True,False,True,True,False,True,True,False,True,False,True],[True,False,False,True,False,False,True,False,False,True,True,True,True,False,True,True,False,False,True,False,True,False,False,False,False,True,True,False,False,True,False,True,False,False,False,False,False,False,True,True,True,False,False,False,False,True,False,False,True,True,True,True,True,True,True,True,False,True,False,False,False,False,True,False,False,True,True,False,True,False,True,False,False,True,True,False,True,True,False,False,False,True,True,False,False,True,True,False,False,True,False,False,True,True,True,True,True,False,False,False,False,True,True,False,True,False,False,False,True,False,False,True,False,False,True,False,True,True,True,True,False,True,True,False,True,False,True,False,False,True,False,False,True,True,False,False,True,False,False,False,True,False,False,True,False,True,True,True,False,False,False,True,False,False,True,True,False,False,True,True,False,True,True,True,True],[False,True,False,False,True,True,True,True,True,False,False,False,False,True,True,False,False,False,False,False,True,True,False,True,False,True,True,False,True,False,True,True,True,True,True,False,False,True,False,True,True,False,False,True,True,True,False,True,True,False,True,False,False,False,True,False,True,True,False,False,True,True,True,True,True,True,True,True,False,True,True,True,True,True,True,True,False,True,False,True,True,False,True,True,False,False,False,True,True,False,False,True,False,True,False,True,False,True,False,False,True,True,False,False,False,True,True,False,False,False,True,True,False,False,True,False,True,True,True,False,True,True,True,True,True,True,False,True,True,True,False,False,False,False,False,True,True,False,True,True,False,True,False,False,True,True,False,False,False,True,True,False,True,False,True,False,False,False,True,True,True,True,True,True,True],[True,False,False,True,False,True,True,True,False,True,False,True,True,True,False,True,False,False,False,False,True,False,False,True,True,True,False,True,False,False,False,False,False,True,True,False,False,True,True,False,False,False,False,False,True,False,True,True,False,True,True,True,True,False,True,False,True,True,True,False,True,False,False,False,True,True,False,True,False,False,False,True,False,False,True,True,False,False,False,False,True,True,True,False,True,False,False,True,False,False,True,True,False,True,True,True,False,False,False,True,False,False,False,False,False,True,True,False,True,True,False,False,False,False,False,False,False,False,True,False,False,False,False,False,True,True,True,True,True,False,False,True,False,False,True,True,True,False,True,False,True,False,False,False,False,False,False,False,True,True,True,True,True,True,False,False,False,True,True,False,True,False,True,False,False]], dtype = "bool")#candidate|4306|(5, 165)|const|bool
bop_4307 = relay.greater_equal(bop_4301.astype('bool'), relay.reshape(const_4306.astype('bool'), relay.shape_of(bop_4301))) # shape=(5, 165)
bop_4310 = relay.greater_equal(bop_4304.astype('bool'), relay.reshape(const_4306.astype('bool'), relay.shape_of(bop_4304))) # shape=(5, 165)
func_32_call = mod.get_global_var('func_32')
func_35_call = mutated_mod.get_global_var('func_35')
var_4315 = relay.var("var_4315", dtype = "float64", shape = (1, 48))#candidate|4315|(1, 48)|var|float64
call_4314 = relay.TupleGetItem(func_32_call(relay.reshape(var_4315.astype('float64'), [2, 4, 6])), 0)
call_4316 = relay.TupleGetItem(func_35_call(relay.reshape(var_4315.astype('float64'), [2, 4, 6])), 0)
output = relay.Tuple([call_4271,var_4274,const_4275,bop_4289,bop_4307,call_4314,var_4315,])
output2 = relay.Tuple([call_4272,var_4274,const_4275,bop_4292,bop_4310,call_4316,var_4315,])
func_4319 = relay.Function([var_4274,var_4288,var_4315,], output)
mod['func_4319'] = func_4319
mod = relay.transform.InferType()(mod)
mutated_mod['func_4319'] = func_4319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4319_call = mutated_mod.get_global_var('func_4319')
var_4321 = relay.var("var_4321", dtype = "float32", shape = (320,))#candidate|4321|(320,)|var|float32
var_4322 = relay.var("var_4322", dtype = "int16", shape = (5, 165))#candidate|4322|(5, 165)|var|int16
var_4323 = relay.var("var_4323", dtype = "float64", shape = (1, 48))#candidate|4323|(1, 48)|var|float64
call_4320 = func_4319_call(var_4321,var_4322,var_4323,)
output = call_4320
func_4324 = relay.Function([var_4321,var_4322,var_4323,], output)
mutated_mod['func_4324'] = func_4324
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4343 = relay.var("var_4343", dtype = "float32", shape = (14, 16, 2))#candidate|4343|(14, 16, 2)|var|float32
uop_4344 = relay.sinh(var_4343.astype('float32')) # shape=(14, 16, 2)
func_3152_call = mod.get_global_var('func_3152')
func_3157_call = mutated_mod.get_global_var('func_3157')
var_4362 = relay.var("var_4362", dtype = "float64", shape = (80,))#candidate|4362|(80,)|var|float64
var_4363 = relay.var("var_4363", dtype = "int16", shape = (825,))#candidate|4363|(825,)|var|int16
var_4364 = relay.var("var_4364", dtype = "int16", shape = (165,))#candidate|4364|(165,)|var|int16
call_4361 = relay.TupleGetItem(func_3152_call(relay.reshape(var_4362.astype('float64'), [10, 4, 2]), relay.reshape(var_4363.astype('int16'), [825,]), relay.reshape(var_4364.astype('int16'), [165,]), ), 2)
call_4365 = relay.TupleGetItem(func_3157_call(relay.reshape(var_4362.astype('float64'), [10, 4, 2]), relay.reshape(var_4363.astype('int16'), [825,]), relay.reshape(var_4364.astype('int16'), [165,]), ), 2)
func_1835_call = mod.get_global_var('func_1835')
func_1838_call = mutated_mod.get_global_var('func_1838')
call_4366 = relay.TupleGetItem(func_1835_call(relay.reshape(var_4364.astype('int16'), [15, 1, 11]), relay.reshape(var_4363.astype('int16'), [15, 5, 11]), ), 0)
call_4367 = relay.TupleGetItem(func_1838_call(relay.reshape(var_4364.astype('int16'), [15, 1, 11]), relay.reshape(var_4363.astype('int16'), [15, 5, 11]), ), 0)
uop_4409 = relay.sin(uop_4344.astype('float32')) # shape=(14, 16, 2)
var_4413 = relay.var("var_4413", dtype = "float32", shape = (14, 16, 2))#candidate|4413|(14, 16, 2)|var|float32
bop_4414 = relay.greater_equal(uop_4409.astype('bool'), relay.reshape(var_4413.astype('bool'), relay.shape_of(uop_4409))) # shape=(14, 16, 2)
uop_4435 = relay.atan(uop_4409.astype('float32')) # shape=(14, 16, 2)
func_2680_call = mod.get_global_var('func_2680')
func_2685_call = mutated_mod.get_global_var('func_2685')
call_4438 = relay.TupleGetItem(func_2680_call(relay.reshape(var_4362.astype('float32'), [1, 8, 10]), relay.reshape(var_4363.astype('int16'), [5, 165]), relay.reshape(call_4361.astype('float64'), [48,]), ), 2)
call_4439 = relay.TupleGetItem(func_2685_call(relay.reshape(var_4362.astype('float32'), [1, 8, 10]), relay.reshape(var_4363.astype('int16'), [5, 165]), relay.reshape(call_4361.astype('float64'), [48,]), ), 2)
uop_4448 = relay.atanh(uop_4435.astype('float64')) # shape=(14, 16, 2)
func_4227_call = mod.get_global_var('func_4227')
func_4228_call = mutated_mod.get_global_var('func_4228')
call_4469 = relay.TupleGetItem(func_4227_call(), 0)
call_4470 = relay.TupleGetItem(func_4228_call(), 0)
output = relay.Tuple([call_4361,var_4362,var_4363,var_4364,call_4366,bop_4414,call_4438,uop_4448,call_4469,])
output2 = relay.Tuple([call_4365,var_4362,var_4363,var_4364,call_4367,bop_4414,call_4439,uop_4448,call_4470,])
func_4479 = relay.Function([var_4343,var_4362,var_4363,var_4364,var_4413,], output)
mod['func_4479'] = func_4479
mod = relay.transform.InferType()(mod)
var_4480 = relay.var("var_4480", dtype = "float32", shape = (14, 16, 2))#candidate|4480|(14, 16, 2)|var|float32
var_4481 = relay.var("var_4481", dtype = "float64", shape = (80,))#candidate|4481|(80,)|var|float64
var_4482 = relay.var("var_4482", dtype = "int16", shape = (825,))#candidate|4482|(825,)|var|int16
var_4483 = relay.var("var_4483", dtype = "int16", shape = (165,))#candidate|4483|(165,)|var|int16
var_4484 = relay.var("var_4484", dtype = "float32", shape = (14, 16, 2))#candidate|4484|(14, 16, 2)|var|float32
output = func_4479(var_4480,var_4481,var_4482,var_4483,var_4484,)
func_4485 = relay.Function([var_4480,var_4481,var_4482,var_4483,var_4484,], output)
mutated_mod['func_4485'] = func_4485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4227_call = mod.get_global_var('func_4227')
func_4228_call = mutated_mod.get_global_var('func_4228')
call_4518 = relay.TupleGetItem(func_4227_call(), 0)
call_4519 = relay.TupleGetItem(func_4228_call(), 0)
output = call_4518
output2 = call_4519
func_4522 = relay.Function([], output)
mod['func_4522'] = func_4522
mod = relay.transform.InferType()(mod)
mutated_mod['func_4522'] = func_4522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4522_call = mutated_mod.get_global_var('func_4522')
call_4523 = func_4522_call()
output = call_4523
func_4524 = relay.Function([], output)
mutated_mod['func_4524'] = func_4524
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4522_call = mod.get_global_var('func_4522')
func_4524_call = mutated_mod.get_global_var('func_4524')
call_4614 = func_4522_call()
call_4615 = func_4522_call()
output = call_4614
output2 = call_4615
func_4628 = relay.Function([], output)
mod['func_4628'] = func_4628
mod = relay.transform.InferType()(mod)
output = func_4628()
func_4629 = relay.Function([], output)
mutated_mod['func_4629'] = func_4629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4628_call = mod.get_global_var('func_4628')
func_4629_call = mutated_mod.get_global_var('func_4629')
call_4649 = func_4628_call()
call_4650 = func_4628_call()
output = call_4649
output2 = call_4650
func_4654 = relay.Function([], output)
mod['func_4654'] = func_4654
mod = relay.transform.InferType()(mod)
mutated_mod['func_4654'] = func_4654
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4654_call = mutated_mod.get_global_var('func_4654')
call_4655 = func_4654_call()
output = call_4655
func_4656 = relay.Function([], output)
mutated_mod['func_4656'] = func_4656
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4628_call = mod.get_global_var('func_4628')
func_4629_call = mutated_mod.get_global_var('func_4629')
call_4700 = func_4628_call()
call_4701 = func_4628_call()
func_4522_call = mod.get_global_var('func_4522')
func_4524_call = mutated_mod.get_global_var('func_4524')
call_4734 = func_4522_call()
call_4735 = func_4522_call()
func_4319_call = mod.get_global_var('func_4319')
func_4324_call = mutated_mod.get_global_var('func_4324')
const_4740 = relay.const([2.613764,-9.165925,-2.303866,0.458680,-2.360483,-3.856485,4.454783,6.149242,6.147877,-5.159025,-7.460809,-6.667287,-7.127054,3.225792,6.360661,-0.511091,-0.317473,2.159488,8.047393,-2.780406,8.758895,6.479086,-0.001055,7.278924,2.800172,6.749574,-6.092582,-7.911413,1.187633,3.022986,-6.280217,9.594451,-0.803609,-2.551444,-4.804805,-1.700290,9.038282,-1.274232,-8.262074,7.448486,9.383636,8.641108,-4.607671,-4.609415,-0.880118,0.880221,5.923409,3.786324,8.285229,9.171350,-9.613710,4.314156,3.579253,6.700687,3.686280,-3.097662,5.214383,5.660344,8.222682,-6.062194,2.501510,-7.006736,-3.639796,-3.858759,8.366464,0.698072,1.530410,-7.960510,-8.114316,-8.242553,-9.904341,3.964899,6.872057,-5.565829,-6.813526,-6.003938,-7.698475,6.836921,-4.463656,-7.060863,9.704227,0.311622,6.941394,-3.223790,9.192103,1.668137,1.472425,-3.258865,5.030027,6.950735,7.674890,8.536160,-0.922102,-2.497476,5.233335,9.632200,3.329499,8.482067,-6.376413,-0.888894,5.663311,7.092439,-7.319590,0.205628,-7.452449,-9.571668,-0.319144,7.692225,-2.827051,6.256267,8.938535,-6.538264,4.098105,4.026708,4.558060,5.434613,3.303231,9.149327,-5.459124,-3.008772,2.112339,-8.625520,-7.771815,0.375886,-8.199801,-8.720972,7.503074,-6.548717,6.762814,-3.575925,0.801122,1.027907,-4.016041,1.696768,7.820708,-8.495777,-3.619842,-2.221480,-9.155177,9.818434,-9.250496,-5.991448,-3.010045,-0.749688,-8.934864,5.701917,-5.487450,5.634524,4.571408,-5.893826,-3.996386,-8.075424,1.324564,5.948188,-5.378683,-0.778152,2.003635,-1.805224,2.602657,5.938979,4.435884,-9.872734,4.369935,-5.535051,-6.812631,6.689841,2.618615,3.088065,-1.368548,6.239654,3.948970,4.971274,-0.691652,-0.223159,-7.260063,-8.948408,-1.424357,5.860626,-7.133939,4.770439,-7.751279,2.910709,-0.603303,2.015962,1.600375,0.208589,-2.238245,7.151204,-1.410386,3.897972,3.043817,-1.403393,-9.135554,9.914000,4.474374,1.498623,3.180885,-7.167341,5.837986,-5.017335,-5.529132,5.055164,-0.410787,1.402406,-7.394064,9.191370,-1.863111,-7.836452,-7.226678,7.437371,-9.094255,8.789759,9.615384,9.144644,7.116942,-8.635326,6.182949,1.579365,-5.041938,-9.945645,3.538301,6.484015,7.068981,-7.365426,0.758589,7.882589,-6.546318,-5.938488,-6.901108,-8.076178,5.548182,1.411951,-1.695496,5.126094,-0.791419,4.459242,8.938781,7.270177,-4.269033,-6.421781,-2.958818,4.519137,7.824584,-0.768489,3.162588,2.183846,0.003203,9.141532,2.139529,3.678569,-1.138760,6.325655,7.906141,-0.290391,-5.805073,8.587895,3.883925,4.909595,-1.432884,-0.547449,-2.694045,8.825550,2.959120,8.829365,2.214992,-3.496685,-6.333757,8.508337,-0.537278,4.578268,5.119830,5.374589,-0.052476,5.548464,8.154394,-6.370078,3.955109,7.532424,5.533570,-3.145687,2.067043,-7.697051,-4.599910,4.926984,-2.317965,-8.000827,-8.655223,-7.457162,-5.149389,7.434374,8.171410,-0.868985,8.607834,5.210759,-7.652456,5.678902,-8.064588,4.014970,-6.973015,-1.449585,-0.316017,-4.404017,-8.549519,0.352442,-3.227550,-7.849409,-5.689761,-7.959897,4.470218,-3.482856,6.489119,1.230214,-7.144835,9.032557,-4.292707,0.807808,-5.471921,4.026406,-9.676221,2.755433], dtype = "float32")#candidate|4740|(320,)|const|float32
const_4741 = relay.const([[8],[-6],[-8],[7],[-5],[1],[-1],[3],[-10],[9],[9],[8],[-10],[4],[-10],[2],[8],[1],[9],[10],[-1],[6],[-1],[7],[-3],[-5],[-10],[-10],[-3],[-2],[7],[-5],[4],[-2],[3],[8],[4],[8],[-2],[9],[1],[10],[6],[-4],[4],[-3],[1],[-7],[3],[-9],[1],[2],[1],[3],[7],[1],[-5],[-1],[-2],[-9],[2],[9],[-10],[-10],[6],[-1],[7],[4],[-3],[3],[10],[-10],[-6],[-3],[8],[7],[4],[7],[4],[8],[7],[1],[-1],[3],[-4],[8],[2],[-9],[8],[9],[4],[8],[-5],[3],[-2],[-1],[8],[-4],[9],[-7],[-6],[8],[-2],[8],[-9],[-8],[4],[10],[-10],[-9],[3],[1],[4],[-4],[-7],[-7],[-5],[-2],[-2],[-9],[-7],[3],[-2],[1],[7],[4],[1],[-3],[5],[1],[8],[6],[3],[-2],[-8],[5],[9],[-9],[2],[-5],[-9],[8],[6],[-9],[7],[-4],[8],[-8],[-6],[7],[3],[-1],[1],[-3],[9],[1],[-9],[-10],[-8],[-8],[6],[10],[10],[6],[-10],[1],[-4],[-4],[-2],[9],[7],[1],[-9],[-10],[9],[2],[10],[1],[1],[7],[10],[-5],[-2],[-1],[-9],[8],[-10],[-1],[2],[-6],[1],[-8],[1],[10],[-9],[-7],[7],[-5],[-4],[5],[-9],[-9],[-2],[10],[4],[-6],[-5],[6],[8],[-9],[-5],[7],[-10],[-10],[3],[6],[-8],[2],[7],[-5],[9],[8],[6],[9],[-1],[10],[-7],[-7],[1],[1],[-1],[-7],[6],[-9],[3],[-6],[5],[-6],[7],[4],[8],[-2],[-3],[3],[-6],[-10],[-3],[-6],[-6],[2],[10],[10],[9],[6],[-3],[-3],[-8],[-5],[-4],[7],[-3],[9],[-1],[5],[-1],[-7],[-2],[-8],[-4],[10],[-7],[-8],[8],[6],[-10],[-3],[7],[8],[-6],[-7],[9],[-10],[10],[-3],[-2],[-2],[6],[4],[1],[-7],[2],[-5],[2],[8],[8],[7],[-9],[8],[4],[-4],[4],[7],[-3],[-5],[10],[7],[-2],[2],[-10],[1],[8],[-3],[4],[-6],[3],[-7],[5],[-9],[7],[-5],[6],[1],[-8],[9],[5],[-4],[-8],[10],[8],[-2],[-6],[-10],[-5],[9],[4],[10],[-10],[7],[4],[-4],[8],[2],[6],[-1],[5],[-7],[-4],[-2],[-7],[4],[-9],[-3],[-5],[-4],[6],[8],[7],[3],[-9],[8],[-8],[7],[-2],[-5],[-3],[2],[1],[-8],[-6],[5],[-2],[10],[-4],[-3],[-5],[-1],[5],[-7],[6],[-8],[8],[1],[-7],[-6],[-3],[9],[-8],[7],[9],[-7],[2],[-9],[5],[-6],[5],[1],[5],[-3],[-1],[7],[3],[-1],[4],[5],[9],[-10],[-9],[10],[5],[6],[-1],[3],[9],[10],[6],[5],[-3],[10],[-6],[3],[-6],[-6],[3],[10],[3],[8],[-3],[2],[9],[-3],[9],[-6],[-6],[-2],[-3],[8],[9],[6],[-2],[-8],[10],[-9],[-8],[-6],[-2],[2],[9],[-6],[6],[7],[-2],[-9],[-9],[-2],[9],[5],[7],[4],[-6],[-2],[1],[10],[4],[5],[3],[-9],[7],[7],[-1],[6],[-1],[1],[7],[-5],[8],[-3],[-3],[-9],[10],[-9],[5],[1],[4],[-5],[-9],[4],[4],[-9],[-1],[-5],[-2],[-7],[3],[4],[-7],[-8],[10],[4],[9],[10],[-10],[7],[-2],[-6],[9],[-3],[10],[-7],[-4],[-8],[-5],[5],[6],[-1],[9],[-3],[8],[5],[-4],[-4],[-4],[5],[-6],[9],[-5],[-3],[3],[-6],[-9],[6],[-10],[9],[8],[-1],[-6],[-9],[-1],[4],[-7],[9],[10],[-2],[2],[-6],[7],[-9],[2],[7],[3],[-6],[3],[9],[10],[-1],[-8],[8],[-2],[5],[-6],[-5],[2],[10],[-3],[7],[4],[-6],[7],[-1],[3],[-3],[-4],[-1],[1],[10],[-6],[2],[2],[-3],[8],[-2],[-3],[9],[6],[-8],[-2],[9],[2],[-2],[-5],[-2],[-9],[10],[-6],[-6],[-3],[7],[7],[-6],[6],[1],[5],[-3],[2],[-3],[10],[-10],[8],[2],[-3],[8],[-9],[3],[-3],[-10],[-3],[6],[-4],[8],[-6],[5],[-4],[5],[-4],[-10],[7],[6],[5],[3],[-8],[-6],[5],[2],[10],[-7],[1],[-2],[-6],[-1],[-6],[-9],[8],[-1],[5],[-10],[9],[6],[9],[5],[-8],[-8],[2],[-5],[9],[-9],[6],[-9],[3],[7],[6],[-1],[-5],[-8],[6],[4],[6],[4],[1],[6],[-5],[4],[5],[6],[-3],[-6],[-2],[1],[5],[-2],[5],[-5],[-7],[6],[-8],[6],[9],[5],[-1],[-10],[3],[5],[-4],[-3],[-8],[-9],[10],[-1],[-3],[-2],[1],[-4],[-8],[-4],[9],[-7],[-1],[-8],[-9],[-3],[-5],[-9],[6],[-3],[-10],[10],[5],[-2],[3],[3],[-2],[-2],[3],[10],[-2],[-10],[-7],[3],[10],[4],[1],[1],[-8],[-10],[-1],[-10],[-3],[7],[-4],[-9],[-10],[-3],[-7],[-10],[-2],[-7],[8],[8],[3],[8],[-1],[8],[-3],[-2],[-10],[3],[-10],[-6],[-3],[-6],[-3],[-10],[2],[-9],[-8],[-10],[7],[4],[3],[-7],[9],[-4],[6],[-7],[-8],[-6],[9],[2],[-3],[-8],[-9],[-9],[8],[-6],[-1],[7],[-5],[-10],[3],[-4],[4],[2],[5],[5],[-8],[-9],[5],[5],[3],[-8],[6],[-6],[-6],[-4],[4],[2],[7],[1],[9],[-9],[3],[5],[-10],[-3],[4],[7],[7],[-3],[-8],[4],[6],[-3],[-9],[4],[-2],[-6],[-5]], dtype = "int16")#candidate|4741|(825, 1)|const|int16
const_4742 = relay.const([[8.290806,3.836964],[-4.233484,4.980023],[-8.042459,4.819920],[5.718657,-8.058958],[0.979848,4.045471],[2.474966,-5.818932],[-2.429701,5.401300],[4.848771,-3.517756],[2.417790,-4.365814],[-2.298281,-6.056723],[1.186298,-1.014786],[-3.317591,-2.991845],[6.991498,0.095494],[-5.849321,-0.352383],[9.598818,4.198131],[3.543125,-1.190017],[-1.566049,-8.823953],[-0.650092,9.645761],[-5.331424,0.881818],[-0.618704,-2.676257],[6.600898,-5.343634],[5.959105,-9.957792],[-4.573758,0.309854],[5.948833,-9.296408]], dtype = "float64")#candidate|4742|(24, 2)|const|float64
call_4739 = relay.TupleGetItem(func_4319_call(relay.reshape(const_4740.astype('float32'), [320,]), relay.reshape(const_4741.astype('int16'), [5, 165]), relay.reshape(const_4742.astype('float64'), [1, 48]), ), 4)
call_4743 = relay.TupleGetItem(func_4324_call(relay.reshape(const_4740.astype('float32'), [320,]), relay.reshape(const_4741.astype('int16'), [5, 165]), relay.reshape(const_4742.astype('float64'), [1, 48]), ), 4)
uop_4758 = relay.atan(const_4741.astype('float64')) # shape=(825, 1)
var_4760 = relay.var("var_4760", dtype = "float64", shape = (6, 10, 10))#candidate|4760|(6, 10, 10)|var|float64
bop_4761 = relay.less(call_4700.astype('bool'), var_4760.astype('bool')) # shape=(6, 10, 10)
bop_4764 = relay.less(call_4701.astype('bool'), var_4760.astype('bool')) # shape=(6, 10, 10)
bop_4765 = relay.mod(uop_4758.astype('float64'), const_4740.astype('float64')) # shape=(825, 320)
output = relay.Tuple([call_4734,call_4739,const_4742,bop_4761,bop_4765,])
output2 = relay.Tuple([call_4735,call_4743,const_4742,bop_4764,bop_4765,])
func_4770 = relay.Function([var_4760,], output)
mod['func_4770'] = func_4770
mod = relay.transform.InferType()(mod)
mutated_mod['func_4770'] = func_4770
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4771 = relay.var("var_4771", dtype = "float64", shape = (6, 10, 10))#candidate|4771|(6, 10, 10)|var|float64
func_4770_call = mutated_mod.get_global_var('func_4770')
call_4772 = func_4770_call(var_4771)
output = call_4772
func_4773 = relay.Function([var_4771], output)
mutated_mod['func_4773'] = func_4773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4654_call = mod.get_global_var('func_4654')
func_4656_call = mutated_mod.get_global_var('func_4656')
call_4800 = func_4654_call()
call_4801 = func_4654_call()
func_32_call = mod.get_global_var('func_32')
func_35_call = mutated_mod.get_global_var('func_35')
var_4825 = relay.var("var_4825", dtype = "float64", shape = (48,))#candidate|4825|(48,)|var|float64
call_4824 = relay.TupleGetItem(func_32_call(relay.reshape(var_4825.astype('float64'), [2, 4, 6])), 0)
call_4826 = relay.TupleGetItem(func_35_call(relay.reshape(var_4825.astype('float64'), [2, 4, 6])), 0)
func_1835_call = mod.get_global_var('func_1835')
func_1838_call = mutated_mod.get_global_var('func_1838')
const_4828 = relay.const([[4,-6,-5,-6,4,-8,2,-9,-6,-6,-5,-2,9,-1,7,-6,-3,2,1,-10,-1,-1,6,3,-5,9,-3,4,-9,7,-2,-9,-9,2,-10,4,1,-6,7,9,8,9,-10,-5,8,7,9,7,-8,8,1,1,9,-1,7,-8,7,-8,2,6,-9,2,-8,6,7,-5,-7,-2,-4,-5,-2,-7,2,-8,1,6,6,8,6,1,9,2,4,4,-7,-10,4,10,3,10,-3,-1,-6,-4,-4,-4,2,-9,-9,4,-4,5,-2,-5,2,-8,-4,5,-10,10,7,-5,1,-5,10,6,-4,3,-5,-10,4,5,6,7,10,-8,-5,-6,-10,7,-10,4,-6,-9,-5,-2,-6,-6,9,-8,5,6,2,6,-10,-10,8,4,10,8,2,-2,-7,1,-6,-4,9,-8,-1,1,-9,-4,4,2,-1]], dtype = "int16")#candidate|4828|(1, 165)|const|int16
const_4829 = relay.const([10,-4,-10,4,-5,6,8,5,10,5,-4,6,-6,1,-9,-3,-8,8,3,5,-10,-4,-8,-2,-2,8,5,-5,4,-10,-2,2,9,9,3,2,4,-6,2,1,-4,-1,4,-9,1,1,-2,5,-4,5,-8,-3,-10,7,6,7,8,8,-5,-10,6,-4,-6,-2,-3,8,-6,6,-9,-10,-2,4,7,1,8,-10,3,-5,-3,9,-5,-9,-7,7,-9,-10,5,10,5,4,5,10,-8,-8,1,10,4,7,6,9,4,-8,-5,-1,-2,-8,10,6,2,-2,-1,10,-2,9,2,7,9,-3,6,7,-2,6,2,2,3,-6,8,2,-3,-10,-8,9,4,4,-9,-9,-5,-2,6,10,10,4,1,8,6,9,6,-3,-3,2,9,10,6,-2,6,2,7,-3,-3,-4,-8,-4,2,-7,-8,4,8,-1,6,9,-5,-9,8,-3,-5,-1,-2,9,4,-9,-3,-10,-9,-7,4,10,-6,4,-2,-6,-5,-2,-2,1,7,8,2,-2,1,-7,-7,6,7,1,6,6,2,8,-1,2,8,-7,-10,-5,-2,5,9,-7,1,6,3,9,-2,-3,-8,10,-7,-8,9,7,6,-1,3,-3,-5,-2,-5,-6,-9,-9,-4,-3,-7,7,6,7,5,-7,7,-3,-1,1,-7,2,-5,-5,1,7,2,-3,-7,-8,-10,3,9,8,-2,-7,-5,8,-1,7,4,-1,10,-5,-6,-3,10,-4,3,-8,-2,-5,3,6,-8,-5,1,-9,1,9,-6,4,8,6,1,-8,10,-1,-9,-8,-2,-1,10,3,5,9,-6,-1,2,-8,3,7,9,6,-4,5,9,8,-10,-1,5,-8,4,7,-5,2,-9,1,6,6,-4,-6,8,10,-7,3,-2,4,10,-5,-4,-3,5,-1,-3,-3,-7,-8,4,-5,3,-4,-10,-3,8,5,5,5,4,-3,2,-2,4,7,9,1,-1,9,1,-10,-1,1,5,-8,-1,-3,-6,3,6,7,2,-9,3,4,9,-5,1,6,3,2,-4,8,-2,9,-10,5,-4,-5,-2,1,3,2,3,9,-4,1,-7,-8,-9,-7,3,1,6,-4,-4,-2,2,-2,-5,-10,-1,-7,-9,7,1,-9,6,2,5,-2,3,-8,1,-10,1,5,3,10,6,2,-1,-2,8,-9,-9,5,-9,7,-3,6,10,-7,3,5,-5,7,-7,-1,2,-9,2,-5,7,1,-2,5,8,5,1,1,8,-10,-6,9,4,2,-3,7,10,3,4,-2,-2,-2,-8,7,-10,10,-1,-7,-8,-10,-6,3,6,-8,4,1,-8,6,-7,-1,-3,4,-9,-8,-9,-9,7,1,-8,2,-10,7,-7,3,10,-2,4,-7,-6,-1,3,-2,-10,2,3,-1,10,-10,-2,2,8,3,9,-6,-4,9,-6,8,3,5,5,-8,3,1,-10,5,6,-3,-7,9,7,7,-1,9,-4,-2,10,5,8,9,10,8,-2,-10,-10,-8,-8,-10,1,-5,-6,5,6,9,5,-2,2,10,10,2,-8,-9,-7,-7,8,5,-6,-10,-2,6,9,-2,-7,4,2,-9,6,9,7,-6,-8,9,-3,8,-9,3,-2,2,7,9,2,2,-8,-5,-8,9,2,-2,6,8,-2,-7,6,-6,-5,-2,2,7,4,-6,3,-10,3,7,10,7,8,8,3,-7,-8,-7,1,-2,-6,-1,4,-3,1,-4,-9,5,-7,1,9,-10,5,9,9,-4,10,5,5,10,-2,-7,7,8,8,-6,7,4,-1,-9,6,9,-9,9,6,1,6,-7,-3,9,-6,8,10,5,-7,-6,-10,-9,1,6,-9,-3,7,8,-7,-1,1,-6,3,2,8,3,3,8,3,-1,-10,-9,-6,-9,3,8,9,-5,-5,-4,-7,2,2,5,-5,8,-1,-4,-6,-2,3,5,3,-4,-10,-3,7,8,7,-5,-10,-8,1,-9,-7,6,-10,1,2,4,-6,-9,-2,2,-10,10,1,-2,3,9,-4,-7,-7,-10,6,3,8,-6,-6,-10,7,-8,-9,1,4,2,-7,4,9,-7,5,8,-9,-6,5,3,5,10,-2,7,-3,5,8,-7,1,-2,1,2,4,-7,3,1,-1,-3,2,-10,9,-8,-5,3,-9,4,7,-2,-3,8,-8,7,9,-4,-2], dtype = "int16")#candidate|4829|(825,)|const|int16
call_4827 = relay.TupleGetItem(func_1835_call(relay.reshape(const_4828.astype('int16'), [15, 1, 11]), relay.reshape(const_4829.astype('int16'), [15, 5, 11]), ), 0)
call_4830 = relay.TupleGetItem(func_1838_call(relay.reshape(const_4828.astype('int16'), [15, 1, 11]), relay.reshape(const_4829.astype('int16'), [15, 5, 11]), ), 0)
output = relay.Tuple([call_4800,call_4824,var_4825,call_4827,const_4828,const_4829,])
output2 = relay.Tuple([call_4801,call_4826,var_4825,call_4830,const_4828,const_4829,])
func_4844 = relay.Function([var_4825,], output)
mod['func_4844'] = func_4844
mod = relay.transform.InferType()(mod)
var_4845 = relay.var("var_4845", dtype = "float64", shape = (48,))#candidate|4845|(48,)|var|float64
output = func_4844(var_4845)
func_4846 = relay.Function([var_4845], output)
mutated_mod['func_4846'] = func_4846
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4654_call = mod.get_global_var('func_4654')
func_4656_call = mutated_mod.get_global_var('func_4656')
call_4970 = func_4654_call()
call_4971 = func_4654_call()
func_32_call = mod.get_global_var('func_32')
func_35_call = mutated_mod.get_global_var('func_35')
const_4973 = relay.const([[2.593004,-2.356762,2.824325,-1.682074],[8.791286,7.146721,-4.478721,-5.577192],[-6.106565,-3.699413,-0.899083,8.212905],[-1.488386,6.811629,-9.086139,-8.241022],[3.080798,-0.358094,1.171996,6.476248],[-6.337916,8.283771,1.070633,-2.107179],[-4.074627,7.612210,8.835511,5.771289],[9.760569,-6.434676,-7.695400,4.144935],[-3.077273,1.783893,0.286735,-0.299461],[8.639652,-1.184639,6.971751,9.909276],[8.400529,-1.241250,9.882808,-8.808189],[-9.957605,-3.116356,-3.134064,-2.259073]], dtype = "float64")#candidate|4973|(12, 4)|const|float64
call_4972 = relay.TupleGetItem(func_32_call(relay.reshape(const_4973.astype('float64'), [2, 4, 6])), 0)
call_4974 = relay.TupleGetItem(func_35_call(relay.reshape(const_4973.astype('float64'), [2, 4, 6])), 0)
func_4654_call = mod.get_global_var('func_4654')
func_4656_call = mutated_mod.get_global_var('func_4656')
call_4981 = func_4654_call()
call_4982 = func_4654_call()
var_4991 = relay.var("var_4991", dtype = "float64", shape = (1, 10, 10))#candidate|4991|(1, 10, 10)|var|float64
bop_4992 = relay.greater_equal(call_4981.astype('bool'), relay.reshape(var_4991.astype('bool'), relay.shape_of(call_4981))) # shape=(1, 10, 10)
bop_4995 = relay.greater_equal(call_4982.astype('bool'), relay.reshape(var_4991.astype('bool'), relay.shape_of(call_4982))) # shape=(1, 10, 10)
output = relay.Tuple([call_4970,call_4972,const_4973,bop_4992,])
output2 = relay.Tuple([call_4971,call_4974,const_4973,bop_4995,])
func_5004 = relay.Function([var_4991,], output)
mod['func_5004'] = func_5004
mod = relay.transform.InferType()(mod)
mutated_mod['func_5004'] = func_5004
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5005 = relay.var("var_5005", dtype = "float64", shape = (1, 10, 10))#candidate|5005|(1, 10, 10)|var|float64
func_5004_call = mutated_mod.get_global_var('func_5004')
call_5006 = func_5004_call(var_5005)
output = call_5006
func_5007 = relay.Function([var_5005], output)
mutated_mod['func_5007'] = func_5007
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5016 = relay.const([[[4.790898,7.667631,-3.692330,-4.277185,-4.752195,-2.899293,5.146677],[7.104838,-4.908758,-4.758268,-8.348304,-1.216192,-9.193024,-1.612803],[8.251656,-4.510491,2.458495,-8.645292,-6.839471,-3.719548,3.002979],[-7.906013,1.931762,-0.673702,-9.244416,-1.723012,-6.402848,8.441008],[-1.390958,-0.799428,-8.281351,-1.292455,-8.479578,8.009208,0.788010],[4.571459,-3.897881,1.563468,-2.495559,-0.520062,-4.881182,6.521425],[9.772993,0.008631,2.679446,-2.540303,6.546507,4.893278,2.798369],[-9.594302,-3.571361,5.056643,3.775246,-2.749091,8.103977,-9.727635]],[[-7.083087,-3.195918,8.669350,5.467722,6.618438,-0.041582,-8.195216],[2.998025,-6.857974,-4.252590,6.696368,-3.663163,-7.924408,-8.354918],[2.246576,8.744348,0.078317,8.367532,-6.628486,4.741593,-4.262969],[-8.122983,5.536498,-0.895311,9.311275,-0.985885,0.314222,3.022097],[-8.766546,8.789759,-7.589561,0.152568,-1.068369,-3.689412,7.894010],[-0.945288,5.037519,-4.368651,-7.554700,8.659007,0.865614,0.120767],[-3.095756,-8.496590,-4.739683,-5.226640,-4.459655,-2.905906,-6.711040],[8.120677,-4.310463,-5.924648,-5.173685,-4.149497,2.934784,-8.899080]],[[-0.351190,9.889452,-3.440156,1.220162,4.290370,-4.042825,4.716744],[-8.387389,2.352423,3.717008,-9.748432,-3.539677,-4.046437,4.319993],[-8.330539,-0.024899,1.043189,0.021408,6.734214,6.029647,-7.655499],[-8.865536,-5.057457,7.799008,0.958779,-3.487403,-8.495922,-4.935940],[0.394644,1.701305,-7.438978,-8.618280,6.912511,2.937365,-0.187775],[-9.267781,-8.573927,-3.877551,5.842821,8.075252,-4.026809,-6.007841],[-9.201128,1.746196,0.848596,9.374988,-7.860269,4.544324,6.305877],[-6.590485,0.098650,-2.759986,-6.370587,4.830215,-5.935904,-8.449106]],[[-2.752360,-6.155474,9.288984,-4.095749,-4.300795,-0.270943,-4.940011],[-3.394865,7.003466,8.431644,2.479931,-0.284868,0.217855,-2.427103],[-6.261300,-5.902509,1.980563,0.909071,2.579262,0.122356,3.500451],[-5.194709,-0.777858,8.190199,-3.090034,-9.497048,-7.571582,9.288267],[-3.499602,-4.962162,-9.562080,3.004755,4.172269,-0.852358,4.294200],[-6.994626,-9.362701,-5.924913,2.068779,-9.719480,-3.816011,-0.921059],[3.967769,-1.983426,1.454432,5.622624,-6.959214,0.717009,4.221831],[-4.452790,-7.550185,-2.249557,0.906745,7.179973,-0.058685,-3.476991]],[[-9.029522,-2.199143,-5.795100,-3.723721,4.281836,0.362836,-1.549540],[7.498090,5.947577,-5.816939,-1.462124,-6.114951,7.064114,-0.926640],[1.952114,0.293004,3.889122,2.269749,-2.746073,2.785271,2.306154],[3.717751,-1.264618,-4.133298,-1.345420,9.615297,7.510602,2.935393],[4.392220,-1.974203,-5.371781,-7.207376,9.459450,-7.321662,3.144836],[5.474255,-5.270437,8.890531,8.869242,-7.977487,-4.775490,-6.562112],[2.520490,9.679970,-0.345698,7.564858,2.311207,-8.888626,-4.656684],[-8.085326,9.687052,-1.362689,1.562579,-9.263083,6.905483,-8.207190]],[[-9.276723,1.457981,-7.366383,-5.805892,9.034643,-5.777347,1.650382],[6.724164,8.542126,-2.547348,-4.311136,-7.639036,-5.832545,-5.786078],[-1.371855,6.340733,-6.382860,-3.677232,9.178333,0.482154,8.599919],[8.332045,-3.970899,-3.400349,2.894220,-8.072622,8.284845,7.255074],[7.149526,-3.806093,-0.863624,-5.783281,-6.121016,-2.726628,2.436405],[-5.932670,0.466664,-7.430048,9.256626,7.214209,9.133427,-6.285426],[-6.732077,-4.764136,1.870098,2.956588,-5.417100,-1.898581,7.655429],[9.136225,-4.959497,4.095734,1.213073,-7.251576,-4.531660,4.124257]],[[5.768991,-6.799385,5.528831,-1.815671,8.093205,4.051990,2.710695],[2.806381,-7.615881,-7.285401,-5.860949,-7.643092,8.486669,-6.403471],[-7.109159,5.879576,2.766766,7.113223,-2.627584,-4.078492,-0.307675],[3.605892,5.610140,-5.057099,3.869914,9.498344,-2.138368,-8.508181],[-5.946672,1.260189,-3.908202,-2.946318,-3.947689,1.758041,0.285871],[4.148305,5.010671,-7.011186,6.992084,-2.336254,3.564881,-6.763261],[8.118572,0.855211,-6.344026,-5.945931,8.997785,-0.804211,-3.725709],[-6.462528,0.764323,5.723237,-8.910645,-6.509242,-5.148572,3.374570]],[[-8.930809,9.760580,-2.862813,8.827014,5.075363,0.766498,-5.095680],[6.942619,6.986597,4.125810,6.046686,8.448484,-1.373292,9.024694],[-2.398106,-5.214100,-2.026994,-2.186510,-3.265563,4.344776,2.710302],[-7.198583,2.507017,4.060029,4.709462,9.554833,4.835959,-4.376034],[-3.118314,7.064860,-4.876798,9.715683,8.999932,1.811373,2.955341],[-1.037251,-1.921766,4.503207,-1.567469,-2.713370,7.418170,-0.378565],[2.369369,-3.259526,-2.909023,-9.714266,7.342577,5.002130,-5.430223],[-9.825563,-1.274706,-7.830322,3.335125,-9.492517,-7.914677,0.092907]],[[-2.130375,4.477042,-5.076841,-3.995879,0.443994,-6.070621,-2.750569],[8.511882,-0.936392,1.758499,-2.369672,9.046026,2.838346,4.222337],[4.717108,9.351208,-8.832688,1.316972,-6.013405,7.178579,-4.866440],[-0.305927,-6.123730,4.309926,8.854586,1.238433,5.095258,5.650538],[-1.527913,-7.815013,5.425580,8.674041,-9.036369,-3.387393,-7.478574],[-6.640480,1.872908,-7.984704,1.706746,4.724079,-4.751185,-8.367946],[4.896606,-2.311938,7.461377,9.082061,-7.545169,-0.422770,8.947028],[9.451327,0.411350,1.675696,-7.252137,-5.072382,8.364858,-2.261382]],[[-2.217644,3.960926,-2.534149,5.713939,7.423708,-0.214105,8.465948],[-2.369775,1.515273,2.269556,-2.142700,-4.210762,-0.668277,-8.022695],[-4.576495,8.444904,8.516398,-1.569631,-9.132450,0.481820,8.827017],[9.350437,5.994931,3.771889,3.091006,6.903750,8.656602,-8.727806],[-1.542504,-4.904588,8.756425,8.924879,-4.212227,-7.059888,0.520269],[-0.997737,2.697356,9.969428,-2.496233,8.992308,4.683528,7.047733],[-9.820629,-4.264882,-0.610219,9.547821,-4.883906,-3.753692,5.726603],[7.789884,0.016474,0.970733,2.342096,8.754213,4.151933,7.286899]],[[4.531820,-2.415489,-7.716959,-9.008770,5.959737,-9.263804,-9.917175],[-4.758149,4.955459,-8.877478,-9.647199,2.228524,-7.395963,7.520822],[-8.130256,3.330571,2.048528,6.723182,-3.039826,-3.597451,-3.221529],[-6.227250,1.930123,-9.057976,-6.111552,9.613665,-9.840996,2.545164],[3.139408,-0.299983,1.861492,3.338068,4.813941,2.560379,-5.619901],[9.494313,-8.475843,4.525498,0.614167,1.950732,-7.469114,-7.385083],[0.177765,-2.702397,-1.935906,-4.409160,-3.276321,-6.581436,1.782079],[1.355792,2.939410,-3.686722,-5.432963,0.230468,8.677227,-2.311998]],[[-3.602652,-0.369361,-8.200372,-7.459956,8.182951,-5.093143,3.315948],[-4.577061,-2.108383,-4.603327,-8.501742,-3.259318,6.607402,-9.852530],[-0.770025,-9.068317,2.692315,-5.979895,5.619884,-4.720090,-6.277157],[-7.458534,0.800406,-9.313203,9.782556,8.619340,4.001645,-0.268387],[-8.668007,5.945038,0.806573,9.296311,-9.862559,-3.915870,-0.580402],[-6.813766,-0.890107,-1.130464,8.251677,9.045829,-7.577978,3.755869],[-8.981184,-6.655248,-1.068338,0.722295,1.887829,1.657268,4.382496],[-0.844436,-0.093073,-2.700481,0.090612,4.947525,4.169527,6.218818]]], dtype = "float32")#candidate|5016|(12, 8, 7)|const|float32
uop_5017 = relay.log10(const_5016.astype('float32')) # shape=(12, 8, 7)
output = uop_5017
output2 = uop_5017
func_5023 = relay.Function([], output)
mod['func_5023'] = func_5023
mod = relay.transform.InferType()(mod)
output = func_5023()
func_5024 = relay.Function([], output)
mutated_mod['func_5024'] = func_5024
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5107 = relay.var("var_5107", dtype = "uint64", shape = (4, 14, 5))#candidate|5107|(4, 14, 5)|var|uint64
var_5108 = relay.var("var_5108", dtype = "uint64", shape = (4, 14, 5))#candidate|5108|(4, 14, 5)|var|uint64
bop_5109 = relay.bitwise_and(var_5107.astype('uint64'), relay.reshape(var_5108.astype('uint64'), relay.shape_of(var_5107))) # shape=(4, 14, 5)
func_4479_call = mod.get_global_var('func_4479')
func_4485_call = mutated_mod.get_global_var('func_4485')
var_5113 = relay.var("var_5113", dtype = "float32", shape = (448,))#candidate|5113|(448,)|var|float32
var_5114 = relay.var("var_5114", dtype = "float64", shape = (80,))#candidate|5114|(80,)|var|float64
var_5115 = relay.var("var_5115", dtype = "int16", shape = (825,))#candidate|5115|(825,)|var|int16
var_5116 = relay.var("var_5116", dtype = "int16", shape = (165,))#candidate|5116|(165,)|var|int16
call_5112 = relay.TupleGetItem(func_4479_call(relay.reshape(var_5113.astype('float32'), [14, 16, 2]), relay.reshape(var_5114.astype('float64'), [80,]), relay.reshape(var_5115.astype('int16'), [825,]), relay.reshape(var_5116.astype('int16'), [165,]), relay.reshape(var_5113.astype('float32'), [14, 16, 2]), ), 4)
call_5117 = relay.TupleGetItem(func_4485_call(relay.reshape(var_5113.astype('float32'), [14, 16, 2]), relay.reshape(var_5114.astype('float64'), [80,]), relay.reshape(var_5115.astype('int16'), [825,]), relay.reshape(var_5116.astype('int16'), [165,]), relay.reshape(var_5113.astype('float32'), [14, 16, 2]), ), 4)
func_3695_call = mod.get_global_var('func_3695')
func_3700_call = mutated_mod.get_global_var('func_3700')
var_5150 = relay.var("var_5150", dtype = "float32", shape = (320,))#candidate|5150|(320,)|var|float32
call_5149 = relay.TupleGetItem(func_3695_call(relay.reshape(var_5150.astype('float32'), [5, 4, 16]), relay.reshape(var_5116.astype('int16'), [11, 15]), relay.reshape(var_5150.astype('float32'), [5, 4, 16]), ), 1)
call_5151 = relay.TupleGetItem(func_3700_call(relay.reshape(var_5150.astype('float32'), [5, 4, 16]), relay.reshape(var_5116.astype('int16'), [11, 15]), relay.reshape(var_5150.astype('float32'), [5, 4, 16]), ), 1)
output = relay.Tuple([bop_5109,call_5112,var_5113,var_5114,var_5115,var_5116,call_5149,var_5150,])
output2 = relay.Tuple([bop_5109,call_5117,var_5113,var_5114,var_5115,var_5116,call_5151,var_5150,])
func_5152 = relay.Function([var_5107,var_5108,var_5113,var_5114,var_5115,var_5116,var_5150,], output)
mod['func_5152'] = func_5152
mod = relay.transform.InferType()(mod)
mutated_mod['func_5152'] = func_5152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5152_call = mutated_mod.get_global_var('func_5152')
var_5154 = relay.var("var_5154", dtype = "uint64", shape = (4, 14, 5))#candidate|5154|(4, 14, 5)|var|uint64
var_5155 = relay.var("var_5155", dtype = "uint64", shape = (4, 14, 5))#candidate|5155|(4, 14, 5)|var|uint64
var_5156 = relay.var("var_5156", dtype = "float32", shape = (448,))#candidate|5156|(448,)|var|float32
var_5157 = relay.var("var_5157", dtype = "float64", shape = (80,))#candidate|5157|(80,)|var|float64
var_5158 = relay.var("var_5158", dtype = "int16", shape = (825,))#candidate|5158|(825,)|var|int16
var_5159 = relay.var("var_5159", dtype = "int16", shape = (165,))#candidate|5159|(165,)|var|int16
var_5160 = relay.var("var_5160", dtype = "float32", shape = (320,))#candidate|5160|(320,)|var|float32
call_5153 = func_5152_call(var_5154,var_5155,var_5156,var_5157,var_5158,var_5159,var_5160,)
output = call_5153
func_5161 = relay.Function([var_5154,var_5155,var_5156,var_5157,var_5158,var_5159,var_5160,], output)
mutated_mod['func_5161'] = func_5161
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4227_call = mod.get_global_var('func_4227')
func_4228_call = mutated_mod.get_global_var('func_4228')
call_5168 = relay.TupleGetItem(func_4227_call(), 0)
call_5169 = relay.TupleGetItem(func_4228_call(), 0)
output = relay.Tuple([call_5168,])
output2 = relay.Tuple([call_5169,])
func_5180 = relay.Function([], output)
mod['func_5180'] = func_5180
mod = relay.transform.InferType()(mod)
output = func_5180()
func_5181 = relay.Function([], output)
mutated_mod['func_5181'] = func_5181
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5023_call = mod.get_global_var('func_5023')
func_5024_call = mutated_mod.get_global_var('func_5024')
call_5237 = func_5023_call()
call_5238 = func_5023_call()
func_4227_call = mod.get_global_var('func_4227')
func_4228_call = mutated_mod.get_global_var('func_4228')
call_5241 = relay.TupleGetItem(func_4227_call(), 0)
call_5242 = relay.TupleGetItem(func_4228_call(), 0)
func_4654_call = mod.get_global_var('func_4654')
func_4656_call = mutated_mod.get_global_var('func_4656')
call_5257 = func_4654_call()
call_5258 = func_4654_call()
output = relay.Tuple([call_5237,call_5241,call_5257,])
output2 = relay.Tuple([call_5238,call_5242,call_5258,])
func_5267 = relay.Function([], output)
mod['func_5267'] = func_5267
mod = relay.transform.InferType()(mod)
output = func_5267()
func_5268 = relay.Function([], output)
mutated_mod['func_5268'] = func_5268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4522_call = mod.get_global_var('func_4522')
func_4524_call = mutated_mod.get_global_var('func_4524')
call_5348 = func_4522_call()
call_5349 = func_4522_call()
output = relay.Tuple([call_5348,])
output2 = relay.Tuple([call_5349,])
func_5378 = relay.Function([], output)
mod['func_5378'] = func_5378
mod = relay.transform.InferType()(mod)
output = func_5378()
func_5379 = relay.Function([], output)
mutated_mod['func_5379'] = func_5379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4227_call = mod.get_global_var('func_4227')
func_4228_call = mutated_mod.get_global_var('func_4228')
call_5415 = relay.TupleGetItem(func_4227_call(), 0)
call_5416 = relay.TupleGetItem(func_4228_call(), 0)
func_4654_call = mod.get_global_var('func_4654')
func_4656_call = mutated_mod.get_global_var('func_4656')
call_5427 = func_4654_call()
call_5428 = func_4654_call()
func_3152_call = mod.get_global_var('func_3152')
func_3157_call = mutated_mod.get_global_var('func_3157')
var_5431 = relay.var("var_5431", dtype = "float64", shape = (80,))#candidate|5431|(80,)|var|float64
var_5432 = relay.var("var_5432", dtype = "int16", shape = (825,))#candidate|5432|(825,)|var|int16
const_5433 = relay.const([-7,3,1,-6,6,-10,8,-5,6,3,-1,3,-4,7,1,10,-6,-8,1,-5,-9,5,-1,-10,-2,1,5,1,8,-9,-7,-9,-4,-9,10,-1,1,6,8,-8,-8,4,-4,-5,2,-1,5,-3,6,3,7,5,-1,1,7,-10,10,-10,-10,7,1,2,-8,4,-8,-2,-2,-7,7,2,9,1,-9,-4,-8,-10,8,6,8,10,6,5,8,-10,-7,-1,6,6,2,4,-10,10,8,-4,5,-6,-7,-8,-10,1,1,-4,3,4,-1,-7,5,-10,5,-3,1,1,8,-4,8,-8,7,-7,3,10,-10,-6,6,7,-4,-4,-10,1,-4,6,10,10,5,10,9,-3,-6,-5,9,-6,4,5,4,-2,3,-2,-2,-2,2,-7,1,1,3,4,9,2,-1,-5,-5,5,5,-10,-10,5,4], dtype = "int16")#candidate|5433|(165,)|const|int16
call_5430 = relay.TupleGetItem(func_3152_call(relay.reshape(var_5431.astype('float64'), [10, 4, 2]), relay.reshape(var_5432.astype('int16'), [825,]), relay.reshape(const_5433.astype('int16'), [165,]), ), 0)
call_5434 = relay.TupleGetItem(func_3157_call(relay.reshape(var_5431.astype('float64'), [10, 4, 2]), relay.reshape(var_5432.astype('int16'), [825,]), relay.reshape(const_5433.astype('int16'), [165,]), ), 0)
func_4628_call = mod.get_global_var('func_4628')
func_4629_call = mutated_mod.get_global_var('func_4629')
call_5435 = func_4628_call()
call_5436 = func_4628_call()
func_4654_call = mod.get_global_var('func_4654')
func_4656_call = mutated_mod.get_global_var('func_4656')
call_5439 = func_4654_call()
call_5440 = func_4654_call()
bop_5462 = relay.power(call_5430.astype('float64'), relay.reshape(var_5432.astype('float64'), relay.shape_of(call_5430))) # shape=(15, 5, 11)
bop_5465 = relay.power(call_5434.astype('float64'), relay.reshape(var_5432.astype('float64'), relay.shape_of(call_5434))) # shape=(15, 5, 11)
output = relay.Tuple([call_5415,call_5427,var_5431,const_5433,call_5435,call_5439,bop_5462,])
output2 = relay.Tuple([call_5416,call_5428,var_5431,const_5433,call_5436,call_5440,bop_5465,])
func_5468 = relay.Function([var_5431,var_5432,], output)
mod['func_5468'] = func_5468
mod = relay.transform.InferType()(mod)
var_5469 = relay.var("var_5469", dtype = "float64", shape = (80,))#candidate|5469|(80,)|var|float64
var_5470 = relay.var("var_5470", dtype = "int16", shape = (825,))#candidate|5470|(825,)|var|int16
output = func_5468(var_5469,var_5470,)
func_5471 = relay.Function([var_5469,var_5470,], output)
mutated_mod['func_5471'] = func_5471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4628_call = mod.get_global_var('func_4628')
func_4629_call = mutated_mod.get_global_var('func_4629')
call_5535 = func_4628_call()
call_5536 = func_4628_call()
output = call_5535
output2 = call_5536
func_5544 = relay.Function([], output)
mod['func_5544'] = func_5544
mod = relay.transform.InferType()(mod)
mutated_mod['func_5544'] = func_5544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5544_call = mutated_mod.get_global_var('func_5544')
call_5545 = func_5544_call()
output = call_5545
func_5546 = relay.Function([], output)
mutated_mod['func_5546'] = func_5546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4628_call = mod.get_global_var('func_4628')
func_4629_call = mutated_mod.get_global_var('func_4629')
call_5555 = func_4628_call()
call_5556 = func_4628_call()
output = relay.Tuple([call_5555,])
output2 = relay.Tuple([call_5556,])
func_5559 = relay.Function([], output)
mod['func_5559'] = func_5559
mod = relay.transform.InferType()(mod)
mutated_mod['func_5559'] = func_5559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5559_call = mutated_mod.get_global_var('func_5559')
call_5560 = func_5559_call()
output = call_5560
func_5561 = relay.Function([], output)
mutated_mod['func_5561'] = func_5561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4522_call = mod.get_global_var('func_4522')
func_4524_call = mutated_mod.get_global_var('func_4524')
call_5569 = func_4522_call()
call_5570 = func_4522_call()
output = call_5569
output2 = call_5570
func_5577 = relay.Function([], output)
mod['func_5577'] = func_5577
mod = relay.transform.InferType()(mod)
mutated_mod['func_5577'] = func_5577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5577_call = mutated_mod.get_global_var('func_5577')
call_5578 = func_5577_call()
output = call_5578
func_5579 = relay.Function([], output)
mutated_mod['func_5579'] = func_5579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4522_call = mod.get_global_var('func_4522')
func_4524_call = mutated_mod.get_global_var('func_4524')
call_5787 = func_4522_call()
call_5788 = func_4522_call()
output = relay.Tuple([call_5787,])
output2 = relay.Tuple([call_5788,])
func_5796 = relay.Function([], output)
mod['func_5796'] = func_5796
mod = relay.transform.InferType()(mod)
mutated_mod['func_5796'] = func_5796
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5796_call = mutated_mod.get_global_var('func_5796')
call_5797 = func_5796_call()
output = call_5797
func_5798 = relay.Function([], output)
mutated_mod['func_5798'] = func_5798
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5843 = relay.const([[[3.391051,-3.903603,9.110693,6.964097,5.953056,-1.312600,-9.163774,5.358246,0.236387,-7.113763,-7.956643,0.421004,3.451275,-7.215303]],[[3.339334,-6.481718,1.935698,-1.024783,-9.806005,-3.157461,-7.160709,-8.269817,-6.538921,5.250344,-1.801051,7.551127,-7.796681,0.078480]]], dtype = "float64")#candidate|5843|(2, 1, 14)|const|float64
var_5844 = relay.var("var_5844", dtype = "float64", shape = (2, 1, 14))#candidate|5844|(2, 1, 14)|var|float64
bop_5845 = relay.floor_mod(const_5843.astype('float64'), relay.reshape(var_5844.astype('float64'), relay.shape_of(const_5843))) # shape=(2, 1, 14)
output = bop_5845
output2 = bop_5845
func_5858 = relay.Function([var_5844,], output)
mod['func_5858'] = func_5858
mod = relay.transform.InferType()(mod)
var_5859 = relay.var("var_5859", dtype = "float64", shape = (2, 1, 14))#candidate|5859|(2, 1, 14)|var|float64
output = func_5858(var_5859)
func_5860 = relay.Function([var_5859], output)
mutated_mod['func_5860'] = func_5860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5023_call = mod.get_global_var('func_5023')
func_5024_call = mutated_mod.get_global_var('func_5024')
call_5868 = func_5023_call()
call_5869 = func_5023_call()
func_5004_call = mod.get_global_var('func_5004')
func_5007_call = mutated_mod.get_global_var('func_5007')
var_5882 = relay.var("var_5882", dtype = "float64", shape = (100,))#candidate|5882|(100,)|var|float64
call_5881 = relay.TupleGetItem(func_5004_call(relay.reshape(var_5882.astype('float64'), [1, 10, 10])), 1)
call_5883 = relay.TupleGetItem(func_5007_call(relay.reshape(var_5882.astype('float64'), [1, 10, 10])), 1)
func_5577_call = mod.get_global_var('func_5577')
func_5579_call = mutated_mod.get_global_var('func_5579')
call_5885 = func_5577_call()
call_5886 = func_5577_call()
func_5004_call = mod.get_global_var('func_5004')
func_5007_call = mutated_mod.get_global_var('func_5007')
call_5909 = relay.TupleGetItem(func_5004_call(relay.reshape(call_5885.astype('float64'), [1, 10, 10])), 2)
call_5910 = relay.TupleGetItem(func_5007_call(relay.reshape(call_5885.astype('float64'), [1, 10, 10])), 2)
func_4227_call = mod.get_global_var('func_4227')
func_4228_call = mutated_mod.get_global_var('func_4228')
call_5912 = relay.TupleGetItem(func_4227_call(), 0)
call_5913 = relay.TupleGetItem(func_4228_call(), 0)
func_5004_call = mod.get_global_var('func_5004')
func_5007_call = mutated_mod.get_global_var('func_5007')
call_5917 = relay.TupleGetItem(func_5004_call(relay.reshape(var_5882.astype('float64'), [1, 10, 10])), 2)
call_5918 = relay.TupleGetItem(func_5007_call(relay.reshape(var_5882.astype('float64'), [1, 10, 10])), 2)
func_4522_call = mod.get_global_var('func_4522')
func_4524_call = mutated_mod.get_global_var('func_4524')
call_5922 = func_4522_call()
call_5923 = func_4522_call()
func_4770_call = mod.get_global_var('func_4770')
func_4773_call = mutated_mod.get_global_var('func_4773')
var_5933 = relay.var("var_5933", dtype = "float64", shape = (600,))#candidate|5933|(600,)|var|float64
call_5932 = relay.TupleGetItem(func_4770_call(relay.reshape(var_5933.astype('float64'), [6, 10, 10])), 3)
call_5934 = relay.TupleGetItem(func_4773_call(relay.reshape(var_5933.astype('float64'), [6, 10, 10])), 3)
func_1835_call = mod.get_global_var('func_1835')
func_1838_call = mutated_mod.get_global_var('func_1838')
var_5963 = relay.var("var_5963", dtype = "int16", shape = (165,))#candidate|5963|(165,)|var|int16
var_5964 = relay.var("var_5964", dtype = "int16", shape = (825,))#candidate|5964|(825,)|var|int16
call_5962 = relay.TupleGetItem(func_1835_call(relay.reshape(var_5963.astype('int16'), [15, 1, 11]), relay.reshape(var_5964.astype('int16'), [15, 5, 11]), ), 0)
call_5965 = relay.TupleGetItem(func_1838_call(relay.reshape(var_5963.astype('int16'), [15, 1, 11]), relay.reshape(var_5964.astype('int16'), [15, 5, 11]), ), 0)
func_4628_call = mod.get_global_var('func_4628')
func_4629_call = mutated_mod.get_global_var('func_4629')
call_5967 = func_4628_call()
call_5968 = func_4628_call()
func_4654_call = mod.get_global_var('func_4654')
func_4656_call = mutated_mod.get_global_var('func_4656')
call_5973 = func_4654_call()
call_5974 = func_4654_call()
bop_6021 = relay.equal(var_5964.astype('bool'), relay.reshape(call_5962.astype('bool'), relay.shape_of(var_5964))) # shape=(825,)
bop_6024 = relay.equal(var_5964.astype('bool'), relay.reshape(call_5965.astype('bool'), relay.shape_of(var_5964))) # shape=(825,)
bop_6026 = relay.equal(call_5962.astype('bool'), relay.reshape(var_5964.astype('bool'), relay.shape_of(call_5962))) # shape=(15, 5, 11)
bop_6029 = relay.equal(call_5965.astype('bool'), relay.reshape(var_5964.astype('bool'), relay.shape_of(call_5965))) # shape=(15, 5, 11)
func_1835_call = mod.get_global_var('func_1835')
func_1838_call = mutated_mod.get_global_var('func_1838')
call_6039 = relay.TupleGetItem(func_1835_call(relay.reshape(var_5963.astype('int16'), [15, 1, 11]), relay.reshape(bop_6026.astype('int16'), [15, 5, 11]), ), 0)
call_6040 = relay.TupleGetItem(func_1838_call(relay.reshape(var_5963.astype('int16'), [15, 1, 11]), relay.reshape(bop_6026.astype('int16'), [15, 5, 11]), ), 0)
output = relay.Tuple([call_5868,call_5881,var_5882,call_5885,call_5909,call_5912,call_5917,call_5922,call_5932,var_5933,var_5963,call_5967,call_5973,bop_6021,bop_6026,call_6039,])
output2 = relay.Tuple([call_5869,call_5883,var_5882,call_5886,call_5910,call_5913,call_5918,call_5923,call_5934,var_5933,var_5963,call_5968,call_5974,bop_6024,bop_6029,call_6040,])
func_6042 = relay.Function([var_5882,var_5933,var_5963,var_5964,], output)
mod['func_6042'] = func_6042
mod = relay.transform.InferType()(mod)
var_6043 = relay.var("var_6043", dtype = "float64", shape = (100,))#candidate|6043|(100,)|var|float64
var_6044 = relay.var("var_6044", dtype = "float64", shape = (600,))#candidate|6044|(600,)|var|float64
var_6045 = relay.var("var_6045", dtype = "int16", shape = (165,))#candidate|6045|(165,)|var|int16
var_6046 = relay.var("var_6046", dtype = "int16", shape = (825,))#candidate|6046|(825,)|var|int16
output = func_6042(var_6043,var_6044,var_6045,var_6046,)
func_6047 = relay.Function([var_6043,var_6044,var_6045,var_6046,], output)
mutated_mod['func_6047'] = func_6047
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4522_call = mod.get_global_var('func_4522')
func_4524_call = mutated_mod.get_global_var('func_4524')
call_6154 = func_4522_call()
call_6155 = func_4522_call()
output = relay.Tuple([call_6154,])
output2 = relay.Tuple([call_6155,])
func_6162 = relay.Function([], output)
mod['func_6162'] = func_6162
mod = relay.transform.InferType()(mod)
output = func_6162()
func_6163 = relay.Function([], output)
mutated_mod['func_6163'] = func_6163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5023_call = mod.get_global_var('func_5023')
func_5024_call = mutated_mod.get_global_var('func_5024')
call_6254 = func_5023_call()
call_6255 = func_5023_call()
func_4654_call = mod.get_global_var('func_4654')
func_4656_call = mutated_mod.get_global_var('func_4656')
call_6256 = func_4654_call()
call_6257 = func_4654_call()
output = relay.Tuple([call_6254,call_6256,])
output2 = relay.Tuple([call_6255,call_6257,])
func_6273 = relay.Function([], output)
mod['func_6273'] = func_6273
mod = relay.transform.InferType()(mod)
mutated_mod['func_6273'] = func_6273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6273_call = mutated_mod.get_global_var('func_6273')
call_6274 = func_6273_call()
output = call_6274
func_6275 = relay.Function([], output)
mutated_mod['func_6275'] = func_6275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5267_call = mod.get_global_var('func_5267')
func_5268_call = mutated_mod.get_global_var('func_5268')
call_6342 = relay.TupleGetItem(func_5267_call(), 2)
call_6343 = relay.TupleGetItem(func_5268_call(), 2)
uop_6348 = relay.sqrt(call_6342.astype('float32')) # shape=(1, 10, 10)
uop_6350 = relay.sqrt(call_6343.astype('float32')) # shape=(1, 10, 10)
func_4227_call = mod.get_global_var('func_4227')
func_4228_call = mutated_mod.get_global_var('func_4228')
call_6365 = relay.TupleGetItem(func_4227_call(), 0)
call_6366 = relay.TupleGetItem(func_4228_call(), 0)
output = relay.Tuple([uop_6348,call_6365,])
output2 = relay.Tuple([uop_6350,call_6366,])
func_6400 = relay.Function([], output)
mod['func_6400'] = func_6400
mod = relay.transform.InferType()(mod)
mutated_mod['func_6400'] = func_6400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6400_call = mutated_mod.get_global_var('func_6400')
call_6401 = func_6400_call()
output = call_6401
func_6402 = relay.Function([], output)
mutated_mod['func_6402'] = func_6402
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5267_call = mod.get_global_var('func_5267')
func_5268_call = mutated_mod.get_global_var('func_5268')
call_6453 = relay.TupleGetItem(func_5267_call(), 2)
call_6454 = relay.TupleGetItem(func_5268_call(), 2)
var_6474 = relay.var("var_6474", dtype = "float64", shape = (4, 10, 10))#candidate|6474|(4, 10, 10)|var|float64
bop_6475 = relay.subtract(call_6453.astype('int16'), var_6474.astype('int16')) # shape=(4, 10, 10)
bop_6478 = relay.subtract(call_6454.astype('int16'), var_6474.astype('int16')) # shape=(4, 10, 10)
output = relay.Tuple([bop_6475,])
output2 = relay.Tuple([bop_6478,])
func_6479 = relay.Function([var_6474,], output)
mod['func_6479'] = func_6479
mod = relay.transform.InferType()(mod)
mutated_mod['func_6479'] = func_6479
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6480 = relay.var("var_6480", dtype = "float64", shape = (4, 10, 10))#candidate|6480|(4, 10, 10)|var|float64
func_6479_call = mutated_mod.get_global_var('func_6479')
call_6481 = func_6479_call(var_6480)
output = call_6481
func_6482 = relay.Function([var_6480], output)
mutated_mod['func_6482'] = func_6482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5559_call = mod.get_global_var('func_5559')
func_5561_call = mutated_mod.get_global_var('func_5561')
call_6569 = relay.TupleGetItem(func_5559_call(), 0)
call_6570 = relay.TupleGetItem(func_5561_call(), 0)
output = call_6569
output2 = call_6570
func_6571 = relay.Function([], output)
mod['func_6571'] = func_6571
mod = relay.transform.InferType()(mod)
mutated_mod['func_6571'] = func_6571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6571_call = mutated_mod.get_global_var('func_6571')
call_6572 = func_6571_call()
output = call_6572
func_6573 = relay.Function([], output)
mutated_mod['func_6573'] = func_6573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4522_call = mod.get_global_var('func_4522')
func_4524_call = mutated_mod.get_global_var('func_4524')
call_6581 = func_4522_call()
call_6582 = func_4522_call()
func_4522_call = mod.get_global_var('func_4522')
func_4524_call = mutated_mod.get_global_var('func_4524')
call_6588 = func_4522_call()
call_6589 = func_4522_call()
output = relay.Tuple([call_6581,call_6588,])
output2 = relay.Tuple([call_6582,call_6589,])
func_6596 = relay.Function([], output)
mod['func_6596'] = func_6596
mod = relay.transform.InferType()(mod)
output = func_6596()
func_6597 = relay.Function([], output)
mutated_mod['func_6597'] = func_6597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5023_call = mod.get_global_var('func_5023')
func_5024_call = mutated_mod.get_global_var('func_5024')
call_6617 = func_5023_call()
call_6618 = func_5023_call()
func_4628_call = mod.get_global_var('func_4628')
func_4629_call = mutated_mod.get_global_var('func_4629')
call_6621 = func_4628_call()
call_6622 = func_4628_call()
func_6400_call = mod.get_global_var('func_6400')
func_6402_call = mutated_mod.get_global_var('func_6402')
call_6630 = relay.TupleGetItem(func_6400_call(), 0)
call_6631 = relay.TupleGetItem(func_6402_call(), 0)
func_4770_call = mod.get_global_var('func_4770')
func_4773_call = mutated_mod.get_global_var('func_4773')
var_6634 = relay.var("var_6634", dtype = "float64", shape = (300, 2))#candidate|6634|(300, 2)|var|float64
call_6633 = relay.TupleGetItem(func_4770_call(relay.reshape(var_6634.astype('float64'), [6, 10, 10])), 3)
call_6635 = relay.TupleGetItem(func_4773_call(relay.reshape(var_6634.astype('float64'), [6, 10, 10])), 3)
uop_6638 = relay.cosh(var_6634.astype('float64')) # shape=(300, 2)
func_5004_call = mod.get_global_var('func_5004')
func_5007_call = mutated_mod.get_global_var('func_5007')
call_6652 = relay.TupleGetItem(func_5004_call(relay.reshape(call_6621.astype('float64'), [1, 10, 10])), 3)
call_6653 = relay.TupleGetItem(func_5007_call(relay.reshape(call_6621.astype('float64'), [1, 10, 10])), 3)
bop_6656 = relay.left_shift(uop_6638.astype('int8'), relay.reshape(var_6634.astype('int8'), relay.shape_of(uop_6638))) # shape=(300, 2)
var_6659 = relay.var("var_6659", dtype = "int8", shape = (300, 2))#candidate|6659|(300, 2)|var|int8
bop_6660 = relay.less(bop_6656.astype('bool'), relay.reshape(var_6659.astype('bool'), relay.shape_of(bop_6656))) # shape=(300, 2)
output = relay.Tuple([call_6617,call_6621,call_6630,call_6633,call_6652,bop_6660,])
output2 = relay.Tuple([call_6618,call_6622,call_6631,call_6635,call_6653,bop_6660,])
func_6665 = relay.Function([var_6634,var_6659,], output)
mod['func_6665'] = func_6665
mod = relay.transform.InferType()(mod)
var_6666 = relay.var("var_6666", dtype = "float64", shape = (300, 2))#candidate|6666|(300, 2)|var|float64
var_6667 = relay.var("var_6667", dtype = "int8", shape = (300, 2))#candidate|6667|(300, 2)|var|int8
output = func_6665(var_6666,var_6667,)
func_6668 = relay.Function([var_6666,var_6667,], output)
mutated_mod['func_6668'] = func_6668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5796_call = mod.get_global_var('func_5796')
func_5798_call = mutated_mod.get_global_var('func_5798')
call_6732 = relay.TupleGetItem(func_5796_call(), 0)
call_6733 = relay.TupleGetItem(func_5798_call(), 0)
output = call_6732
output2 = call_6733
func_6738 = relay.Function([], output)
mod['func_6738'] = func_6738
mod = relay.transform.InferType()(mod)
output = func_6738()
func_6739 = relay.Function([], output)
mutated_mod['func_6739'] = func_6739
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5577_call = mod.get_global_var('func_5577')
func_5579_call = mutated_mod.get_global_var('func_5579')
call_6757 = func_5577_call()
call_6758 = func_5577_call()
output = relay.Tuple([call_6757,])
output2 = relay.Tuple([call_6758,])
func_6762 = relay.Function([], output)
mod['func_6762'] = func_6762
mod = relay.transform.InferType()(mod)
mutated_mod['func_6762'] = func_6762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6762_call = mutated_mod.get_global_var('func_6762')
call_6763 = func_6762_call()
output = call_6763
func_6764 = relay.Function([], output)
mutated_mod['func_6764'] = func_6764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5559_call = mod.get_global_var('func_5559')
func_5561_call = mutated_mod.get_global_var('func_5561')
call_6765 = relay.TupleGetItem(func_5559_call(), 0)
call_6766 = relay.TupleGetItem(func_5561_call(), 0)
func_5378_call = mod.get_global_var('func_5378')
func_5379_call = mutated_mod.get_global_var('func_5379')
call_6777 = relay.TupleGetItem(func_5378_call(), 0)
call_6778 = relay.TupleGetItem(func_5379_call(), 0)
output = relay.Tuple([call_6765,call_6777,])
output2 = relay.Tuple([call_6766,call_6778,])
func_6785 = relay.Function([], output)
mod['func_6785'] = func_6785
mod = relay.transform.InferType()(mod)
output = func_6785()
func_6786 = relay.Function([], output)
mutated_mod['func_6786'] = func_6786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4628_call = mod.get_global_var('func_4628')
func_4629_call = mutated_mod.get_global_var('func_4629')
call_6822 = func_4628_call()
call_6823 = func_4628_call()
output = call_6822
output2 = call_6823
func_6837 = relay.Function([], output)
mod['func_6837'] = func_6837
mod = relay.transform.InferType()(mod)
mutated_mod['func_6837'] = func_6837
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6837_call = mutated_mod.get_global_var('func_6837')
call_6838 = func_6837_call()
output = call_6838
func_6839 = relay.Function([], output)
mutated_mod['func_6839'] = func_6839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5559_call = mod.get_global_var('func_5559')
func_5561_call = mutated_mod.get_global_var('func_5561')
call_6887 = relay.TupleGetItem(func_5559_call(), 0)
call_6888 = relay.TupleGetItem(func_5561_call(), 0)
output = call_6887
output2 = call_6888
func_6921 = relay.Function([], output)
mod['func_6921'] = func_6921
mod = relay.transform.InferType()(mod)
output = func_6921()
func_6922 = relay.Function([], output)
mutated_mod['func_6922'] = func_6922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4628_call = mod.get_global_var('func_4628')
func_4629_call = mutated_mod.get_global_var('func_4629')
call_6995 = func_4628_call()
call_6996 = func_4628_call()
func_4654_call = mod.get_global_var('func_4654')
func_4656_call = mutated_mod.get_global_var('func_4656')
call_6997 = func_4654_call()
call_6998 = func_4654_call()
output = relay.Tuple([call_6995,call_6997,])
output2 = relay.Tuple([call_6996,call_6998,])
func_7003 = relay.Function([], output)
mod['func_7003'] = func_7003
mod = relay.transform.InferType()(mod)
output = func_7003()
func_7004 = relay.Function([], output)
mutated_mod['func_7004'] = func_7004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6738_call = mod.get_global_var('func_6738')
func_6739_call = mutated_mod.get_global_var('func_6739')
call_7031 = func_6738_call()
call_7032 = func_6738_call()
output = relay.Tuple([call_7031,])
output2 = relay.Tuple([call_7032,])
func_7047 = relay.Function([], output)
mod['func_7047'] = func_7047
mod = relay.transform.InferType()(mod)
output = func_7047()
func_7048 = relay.Function([], output)
mutated_mod['func_7048'] = func_7048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5559_call = mod.get_global_var('func_5559')
func_5561_call = mutated_mod.get_global_var('func_5561')
call_7088 = relay.TupleGetItem(func_5559_call(), 0)
call_7089 = relay.TupleGetItem(func_5561_call(), 0)
output = relay.Tuple([call_7088,])
output2 = relay.Tuple([call_7089,])
func_7097 = relay.Function([], output)
mod['func_7097'] = func_7097
mod = relay.transform.InferType()(mod)
mutated_mod['func_7097'] = func_7097
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7097_call = mutated_mod.get_global_var('func_7097')
call_7098 = func_7097_call()
output = call_7098
func_7099 = relay.Function([], output)
mutated_mod['func_7099'] = func_7099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5378_call = mod.get_global_var('func_5378')
func_5379_call = mutated_mod.get_global_var('func_5379')
call_7100 = relay.TupleGetItem(func_5378_call(), 0)
call_7101 = relay.TupleGetItem(func_5379_call(), 0)
uop_7105 = relay.acos(call_7100.astype('float32')) # shape=(1, 10, 10)
uop_7107 = relay.acos(call_7101.astype('float32')) # shape=(1, 10, 10)
func_6273_call = mod.get_global_var('func_6273')
func_6275_call = mutated_mod.get_global_var('func_6275')
call_7114 = relay.TupleGetItem(func_6273_call(), 0)
call_7115 = relay.TupleGetItem(func_6275_call(), 0)
func_3152_call = mod.get_global_var('func_3152')
func_3157_call = mutated_mod.get_global_var('func_3157')
var_7117 = relay.var("var_7117", dtype = "float64", shape = (80,))#candidate|7117|(80,)|var|float64
var_7118 = relay.var("var_7118", dtype = "int16", shape = (825,))#candidate|7118|(825,)|var|int16
var_7119 = relay.var("var_7119", dtype = "int16", shape = (165,))#candidate|7119|(165,)|var|int16
call_7116 = relay.TupleGetItem(func_3152_call(relay.reshape(var_7117.astype('float64'), [10, 4, 2]), relay.reshape(var_7118.astype('int16'), [825,]), relay.reshape(var_7119.astype('int16'), [165,]), ), 4)
call_7120 = relay.TupleGetItem(func_3157_call(relay.reshape(var_7117.astype('float64'), [10, 4, 2]), relay.reshape(var_7118.astype('int16'), [825,]), relay.reshape(var_7119.astype('int16'), [165,]), ), 4)
bop_7126 = relay.bitwise_and(call_7100.astype('uint32'), relay.reshape(uop_7105.astype('uint32'), relay.shape_of(call_7100))) # shape=(1, 10, 10)
bop_7129 = relay.bitwise_and(call_7101.astype('uint32'), relay.reshape(uop_7107.astype('uint32'), relay.shape_of(call_7101))) # shape=(1, 10, 10)
output = relay.Tuple([call_7114,call_7116,var_7117,var_7118,var_7119,bop_7126,])
output2 = relay.Tuple([call_7115,call_7120,var_7117,var_7118,var_7119,bop_7129,])
func_7132 = relay.Function([var_7117,var_7118,var_7119,], output)
mod['func_7132'] = func_7132
mod = relay.transform.InferType()(mod)
mutated_mod['func_7132'] = func_7132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7132_call = mutated_mod.get_global_var('func_7132')
var_7134 = relay.var("var_7134", dtype = "float64", shape = (80,))#candidate|7134|(80,)|var|float64
var_7135 = relay.var("var_7135", dtype = "int16", shape = (825,))#candidate|7135|(825,)|var|int16
var_7136 = relay.var("var_7136", dtype = "int16", shape = (165,))#candidate|7136|(165,)|var|int16
call_7133 = func_7132_call(var_7134,var_7135,var_7136,)
output = call_7133
func_7137 = relay.Function([var_7134,var_7135,var_7136,], output)
mutated_mod['func_7137'] = func_7137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6837_call = mod.get_global_var('func_6837')
func_6839_call = mutated_mod.get_global_var('func_6839')
call_7159 = func_6837_call()
call_7160 = func_6837_call()
func_6665_call = mod.get_global_var('func_6665')
func_6668_call = mutated_mod.get_global_var('func_6668')
const_7162 = relay.const([3.293191,2.232562,0.640871,-7.598331,5.908165,4.337228,-6.966585,2.198470,2.866042,-4.722938,-6.084512,-4.147729,9.802777,-6.029314,-4.739533,0.248821,3.538331,-1.930108,7.836884,2.592594,-2.334385,1.964593,-7.975973,-6.193533,5.115883,9.032925,2.268566,0.648748,-8.043875,-2.513537,2.885029,6.291768,-5.535656,0.013284,-2.714654,-9.287800,-3.661311,3.304826,-5.537549,-4.588102,-3.594300,-6.699364,2.936766,2.605849,6.848936,-2.133445,2.424855,-1.158672,3.001941,3.965930,-8.288217,-9.797653,8.464180,6.138470,-9.632622,3.076278,1.251243,-1.319778,-4.677712,-1.244581,3.348361,-3.201199,-4.211006,-2.454039,1.032821,5.238565,-6.434036,-3.814475,7.992115,1.876096,2.028752,0.982261,-0.187395,-8.431301,1.580364,0.349841,6.388271,9.879149,-9.594086,-0.381939,7.946873,1.520295,7.809166,1.873131,7.158074,-2.727308,-5.578938,4.422659,-8.359497,0.074644,-4.493220,-2.180566,-2.254620,-4.892303,-9.609217,-8.598424,-6.218893,8.858022,4.345262,5.187022,0.436080,-5.102094,2.321076,9.623654,5.062526,8.818439,3.094517,7.962775,7.761219,-2.194907,-2.979150,9.550306,-1.436901,7.024740,8.246095,-9.068181,-7.647530,-5.197694,-5.367484,0.442947,-4.861455,0.260475,4.620916,-8.661948,-4.885207,-9.261802,0.870668,-4.854904,-8.808459,-8.336482,-4.173595,-8.594658,8.153890,-5.262932,-1.458612,5.354983,-0.667267,-2.242445,8.257695,-9.352710,3.835059,6.026423,-6.058282,-5.342415,3.706088,-4.092901,6.405005,-6.488506,-3.237387,-8.766121,3.469857,5.217082,6.142470,5.264474,-3.307871,-5.959350,-1.940201,1.845973,1.757957,8.860959,-0.118040,-4.550799,-3.197567,-5.328487,1.187915,-8.244103,-9.756080,-2.951045,4.048750,-1.326289,2.969881,-4.405500,-2.562884,-6.508724,2.452418,-6.271039,-2.555645,-1.905309,-2.790342,7.232743,6.239251,-0.301258,8.770188,9.052519,-7.482590,3.430684,5.127314,6.716056,7.824698,6.193373,7.750857,-3.015951,4.604639,-4.867336,6.088731,9.940494,1.606988,-3.021507,3.743234,-3.358969,6.573521,0.339376,5.505206,3.604387,0.679104,7.289206,-5.205468,-3.296559,-9.265305,2.967141,-3.643833,2.185555,-2.507971,-7.808471,6.086077,5.293649,-4.312944,2.058706,7.247159,-7.434856,-4.360839,0.136828,2.578748,-2.122116,6.889458,7.913213,-7.034190,7.932663,-8.220020,-1.700055,-4.669613,3.966172,9.036773,-1.595131,1.291205,3.945604,4.978383,-8.234419,-8.902528,-7.883774,1.398063,2.382790,-7.730487,-3.292624,-5.634530,5.498049,0.089845,-2.066713,2.790304,9.933734,2.721857,-0.281911,-7.226195,-3.918724,1.589297,-5.243488,-6.091472,1.121080,-5.824236,-1.646903,-5.274959,-3.839448,-9.216010,-9.076174,4.547606,-8.668998,-8.267191,3.429115,5.094775,3.928226,5.624384,9.106508,7.641070,-5.059587,7.818371,8.573918,-4.563094,9.222981,-0.801467,6.948884,2.609502,-3.081163,-9.617717,-1.810189,0.217177,9.747116,9.721181,9.968156,2.949303,9.146755,-0.013987,-8.280879,-6.076040,3.810384,-2.770612,-6.409892,-0.511679,2.068890,1.603322,-4.704265,-0.449872,3.919939,5.705009,-7.505636,-4.632112,8.109577,-4.886672,-7.270992,9.614485,1.228909,-5.015075,5.269702,4.788261,7.113580,9.755763,1.458580,4.555455,8.264016,3.138484,6.352002,3.549082,-7.050001,1.795309,-6.617968,-0.121772,-0.318957,-2.460499,6.208912,-2.673377,-4.888953,8.754924,7.940377,-3.163521,5.718127,5.735968,3.772290,1.172076,-5.994472,-0.864185,6.880473,6.635616,4.967818,3.291906,2.139715,-6.793331,5.029733,7.050711,-7.627650,-7.448785,-5.706906,0.144123,-4.607950,2.347257,3.668752,-5.412273,0.889327,-2.855073,2.652243,1.272629,1.792986,-6.474030,3.234692,-6.468189,5.527719,2.568452,-2.299860,7.957811,3.803741,7.759906,3.969019,1.650890,6.779079,1.803040,-7.638320,9.569132,-2.936020,-7.564334,-5.206633,-7.960683,0.671984,5.827063,-0.617188,6.279419,6.890242,-3.626858,-8.085612,1.610457,7.333030,-0.279686,-4.054843,2.957405,3.046510,-4.530289,-1.104074,7.816223,9.318240,4.118519,5.688604,3.375141,-1.244455,2.734069,-9.106415,-9.276310,-8.737177,2.419885,6.875685,7.871261,-8.096825,-3.850892,-5.909185,5.075068,-7.964666,0.013258,0.803664,-6.917263,-2.031644,-3.197828,5.594041,-1.658961,7.823231,-2.242560,5.463818,3.730116,6.170481,-2.647042,1.511599,7.413192,1.303155,5.902062,-1.052533,-5.933306,-7.384236,9.025066,9.702706,0.383383,7.951161,8.634064,3.887929,-6.433926,-8.033612,7.161513,-8.519776,8.001405,2.036288,-6.000958,2.393818,4.504656,5.992443,3.045955,-1.994059,3.105251,-5.694713,-4.741867,8.582565,-6.728196,-7.107249,2.006153,0.705246,-1.334171,-8.655620,-3.970993,5.050757,6.980625,-7.519500,8.476095,1.541139,-2.218802,-1.168119,9.202665,5.817442,5.994764,1.790203,8.806202,-5.568799,-3.688556,-9.362858,-0.609675,-4.649529,9.054728,-7.282383,6.713214,8.604146,3.842128,9.719804,-2.974815,-1.062958,-8.777901,-4.625276,-2.582503,3.195118,1.657401,1.113209,4.970847,6.570137,-1.159098,7.139324,1.595145,7.370407,-8.297293,-4.666805,-9.696696,1.350484,-8.716939,-1.131098,-7.845623,7.885315,7.941015,3.472385,-8.313334,5.538716,-7.403192,6.105251,-0.101542,-4.800462,3.060655,7.402097,9.008556,-4.115491,-9.500514,4.822063,-5.462237,8.790882,7.854861,-4.223548,7.136679,5.537984,-5.804071,-2.587868,8.994855,-9.136591,5.037657,-8.809191,-5.933741,-9.741453,9.294427,1.180049,8.727959,-1.324630,9.202546,-1.186319,-8.108944,-3.311459,-9.572927,5.338799,5.927710,-8.183173,1.182864,2.517395,8.838874,1.437920,9.594576,-5.849263,3.263174,-9.347232,1.709679,6.353251,-1.752197,1.810232,-3.903199,-8.415292,-2.186914,-2.246400,-4.968096,6.308888,-4.636893,-8.053073,0.416897,-9.328825,0.782178,4.706044,3.570891,7.266847,-9.533685,0.986469,3.136634,-5.722732,-1.842438,-2.626574,-9.898764,8.018063,-0.928504,3.701231,-0.498279,-6.961854,-4.323661,3.491559,-7.137098,1.444440,1.156654,-7.838487,-9.470497,-9.762177,8.540035,9.154463,-7.761025,-9.163727,5.768396,-7.825361,4.734415,7.204859], dtype = "float64")#candidate|7162|(600,)|const|float64
call_7161 = relay.TupleGetItem(func_6665_call(relay.reshape(const_7162.astype('float64'), [300, 2]), relay.reshape(const_7162.astype('int8'), [300, 2]), ), 3)
call_7163 = relay.TupleGetItem(func_6668_call(relay.reshape(const_7162.astype('float64'), [300, 2]), relay.reshape(const_7162.astype('int8'), [300, 2]), ), 3)
func_32_call = mod.get_global_var('func_32')
func_35_call = mutated_mod.get_global_var('func_35')
var_7165 = relay.var("var_7165", dtype = "float64", shape = (12, 4))#candidate|7165|(12, 4)|var|float64
call_7164 = relay.TupleGetItem(func_32_call(relay.reshape(var_7165.astype('float64'), [2, 4, 6])), 0)
call_7166 = relay.TupleGetItem(func_35_call(relay.reshape(var_7165.astype('float64'), [2, 4, 6])), 0)
func_6921_call = mod.get_global_var('func_6921')
func_6922_call = mutated_mod.get_global_var('func_6922')
call_7175 = func_6921_call()
call_7176 = func_6921_call()
output = relay.Tuple([call_7159,call_7161,const_7162,call_7164,var_7165,call_7175,])
output2 = relay.Tuple([call_7160,call_7163,const_7162,call_7166,var_7165,call_7176,])
func_7187 = relay.Function([var_7165,], output)
mod['func_7187'] = func_7187
mod = relay.transform.InferType()(mod)
var_7188 = relay.var("var_7188", dtype = "float64", shape = (12, 4))#candidate|7188|(12, 4)|var|float64
output = func_7187(var_7188)
func_7189 = relay.Function([var_7188], output)
mutated_mod['func_7189'] = func_7189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6738_call = mod.get_global_var('func_6738')
func_6739_call = mutated_mod.get_global_var('func_6739')
call_7213 = func_6738_call()
call_7214 = func_6738_call()
output = relay.Tuple([call_7213,])
output2 = relay.Tuple([call_7214,])
func_7257 = relay.Function([], output)
mod['func_7257'] = func_7257
mod = relay.transform.InferType()(mod)
mutated_mod['func_7257'] = func_7257
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7257_call = mutated_mod.get_global_var('func_7257')
call_7258 = func_7257_call()
output = call_7258
func_7259 = relay.Function([], output)
mutated_mod['func_7259'] = func_7259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6762_call = mod.get_global_var('func_6762')
func_6764_call = mutated_mod.get_global_var('func_6764')
call_7299 = relay.TupleGetItem(func_6762_call(), 0)
call_7300 = relay.TupleGetItem(func_6764_call(), 0)
func_5468_call = mod.get_global_var('func_5468')
func_5471_call = mutated_mod.get_global_var('func_5471')
var_7303 = relay.var("var_7303", dtype = "float64", shape = (80,))#candidate|7303|(80,)|var|float64
var_7304 = relay.var("var_7304", dtype = "int16", shape = (825,))#candidate|7304|(825,)|var|int16
call_7302 = relay.TupleGetItem(func_5468_call(relay.reshape(var_7303.astype('float64'), [80,]), relay.reshape(var_7304.astype('int16'), [825,]), ), 5)
call_7305 = relay.TupleGetItem(func_5471_call(relay.reshape(var_7303.astype('float64'), [80,]), relay.reshape(var_7304.astype('int16'), [825,]), ), 5)
func_4654_call = mod.get_global_var('func_4654')
func_4656_call = mutated_mod.get_global_var('func_4656')
call_7312 = func_4654_call()
call_7313 = func_4654_call()
output = relay.Tuple([call_7299,call_7302,var_7303,var_7304,call_7312,])
output2 = relay.Tuple([call_7300,call_7305,var_7303,var_7304,call_7313,])
func_7314 = relay.Function([var_7303,var_7304,], output)
mod['func_7314'] = func_7314
mod = relay.transform.InferType()(mod)
mutated_mod['func_7314'] = func_7314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7314_call = mutated_mod.get_global_var('func_7314')
var_7316 = relay.var("var_7316", dtype = "float64", shape = (80,))#candidate|7316|(80,)|var|float64
var_7317 = relay.var("var_7317", dtype = "int16", shape = (825,))#candidate|7317|(825,)|var|int16
call_7315 = func_7314_call(var_7316,var_7317,)
output = call_7315
func_7318 = relay.Function([var_7316,var_7317,], output)
mutated_mod['func_7318'] = func_7318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7003_call = mod.get_global_var('func_7003')
func_7004_call = mutated_mod.get_global_var('func_7004')
call_7322 = relay.TupleGetItem(func_7003_call(), 0)
call_7323 = relay.TupleGetItem(func_7004_call(), 0)
output = call_7322
output2 = call_7323
func_7346 = relay.Function([], output)
mod['func_7346'] = func_7346
mod = relay.transform.InferType()(mod)
mutated_mod['func_7346'] = func_7346
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7346_call = mutated_mod.get_global_var('func_7346')
call_7347 = func_7346_call()
output = call_7347
func_7348 = relay.Function([], output)
mutated_mod['func_7348'] = func_7348
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5180_call = mod.get_global_var('func_5180')
func_5181_call = mutated_mod.get_global_var('func_5181')
call_7369 = relay.TupleGetItem(func_5180_call(), 0)
call_7370 = relay.TupleGetItem(func_5181_call(), 0)
func_5023_call = mod.get_global_var('func_5023')
func_5024_call = mutated_mod.get_global_var('func_5024')
call_7374 = func_5023_call()
call_7375 = func_5023_call()
output = relay.Tuple([call_7369,call_7374,])
output2 = relay.Tuple([call_7370,call_7375,])
func_7392 = relay.Function([], output)
mod['func_7392'] = func_7392
mod = relay.transform.InferType()(mod)
output = func_7392()
func_7393 = relay.Function([], output)
mutated_mod['func_7393'] = func_7393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5023_call = mod.get_global_var('func_5023')
func_5024_call = mutated_mod.get_global_var('func_5024')
call_7438 = func_5023_call()
call_7439 = func_5023_call()
func_7314_call = mod.get_global_var('func_7314')
func_7318_call = mutated_mod.get_global_var('func_7318')
const_7458 = relay.const([[-4.581791,1.210761],[9.912083,-4.458122],[5.295083,8.608536],[8.578222,3.817022],[-0.625666,-6.039168],[-3.661550,6.447095],[-4.090275,4.727522],[-3.036468,3.669050],[-4.842528,-4.252362],[-8.262805,3.464023],[6.970361,-0.981855],[-3.210487,-9.780723],[-7.239600,9.411227],[0.192766,9.795358],[1.779047,-6.616998],[-0.323645,-7.889778],[4.680610,-1.672164],[7.833359,0.032038],[-8.067311,9.059537],[2.757256,-4.885042],[-5.626311,-8.870298],[-0.689216,-2.590544],[-2.160690,0.192389],[-0.658240,6.309943],[-4.687826,1.351490],[1.038575,6.846397],[-8.068617,3.252306],[-4.162268,-6.582761],[2.422494,-7.977918],[-2.346699,4.619544],[9.889207,9.309587],[-2.322309,1.553433],[4.409481,-6.898406],[6.074840,-4.266282],[1.190124,9.843906],[0.105222,-3.935892],[-2.849118,3.412903],[7.846708,-3.073957],[5.962018,-0.679785],[-0.580535,2.328238]], dtype = "float64")#candidate|7458|(40, 2)|const|float64
const_7459 = relay.const([-5,-5,1,3,1,-3,2,-1,7,7,-9,1,-9,1,2,-9,4,1,1,1,9,-2,-2,-2,-3,4,1,-5,2,2,-9,4,-6,-9,10,-6,5,-10,10,-3,2,-2,5,-5,-5,-4,9,-8,-2,9,-8,-2,2,-8,-7,-5,2,-4,-7,7,-8,-6,8,2,-2,5,8,3,-1,-2,5,9,-5,6,4,5,4,-8,7,4,3,-1,7,10,-4,8,2,-7,-2,10,-8,-9,8,5,-9,5,8,-4,-10,5,-9,-3,2,-1,-5,-2,7,7,1,1,1,-4,3,-4,-2,-7,1,3,4,-8,4,3,-3,7,2,-6,5,4,9,1,8,-4,9,-4,1,3,-4,-9,7,-3,-3,4,10,-5,9,-10,-3,-7,4,-5,-5,-4,-5,10,-8,-2,1,-10,3,9,1,-10,8,5,9,8,-10,-7,-5,6,-7,8,-4,10,-4,-1,2,9,9,1,6,3,10,-1,-4,-10,-5,2,5,-9,3,-5,-1,5,8,9,-5,-10,-2,-10,7,-9,8,-4,-5,3,-4,3,3,-7,-3,-7,-1,-3,-5,1,-5,-8,4,-6,-6,-7,9,8,-9,7,3,2,8,-7,10,-8,-8,8,6,-1,6,5,-7,1,7,-7,9,-6,-5,-1,1,-2,4,3,7,-4,-3,10,1,-5,7,-1,-3,5,-2,-5,-6,3,8,-3,1,9,8,5,9,10,-4,-6,9,-7,8,3,-2,7,4,6,-9,1,-2,-9,-8,1,-9,1,6,9,3,-1,10,-4,2,-10,-4,-10,-9,9,5,9,5,-2,-9,9,4,-6,10,9,-9,2,-1,-10,-1,-8,-9,2,7,4,-6,-8,5,-5,6,-6,4,-8,4,5,-9,2,10,-9,-8,4,8,-4,-8,9,-6,8,-6,-5,6,-4,3,-2,-9,-1,-8,3,-7,-10,-8,6,3,-4,-10,-7,-8,-1,8,5,6,6,-1,9,-6,10,5,9,-9,9,1,8,-9,-4,2,-6,-7,2,1,-3,-8,10,10,5,2,1,-2,-5,-7,9,8,10,8,-3,-1,4,9,5,5,9,4,1,6,-6,-6,-4,8,2,-4,-3,-1,-4,-2,10,-9,-5,8,6,3,-8,-4,-3,-4,8,-10,-3,-1,1,-6,-1,9,-5,-1,10,-2,2,9,-8,-2,3,1,-3,10,6,-5,10,-2,-1,-5,-6,9,3,-7,3,1,-1,1,-5,-10,-9,-7,-8,-4,-1,-10,-6,-6,9,3,-3,7,7,2,8,-2,-6,6,7,5,-8,4,5,4,3,5,2,-2,9,10,5,-6,10,-6,-1,4,7,-5,9,-6,9,-10,3,-1,-7,2,4,2,-10,-2,3,-2,5,3,-9,8,-10,8,-4,6,9,-1,5,-6,4,-6,3,7,5,1,3,-1,-10,6,7,5,-1,-8,2,3,-3,2,9,3,-3,10,-6,9,-10,-1,-9,5,-3,-8,1,10,10,-10,-5,-5,-9,-4,-3,-2,8,-4,-2,-8,-3,1,-10,6,4,1,8,8,8,-2,-5,-8,10,1,-10,-6,-7,-9,-7,-7,2,10,3,-9,10,-3,-8,7,4,9,-8,9,1,4,-2,10,-8,-3,-10,3,-4,4,-9,9,10,-7,2,-4,1,-4,9,-4,6,-10,-10,8,-1,-3,5,6,-9,-2,7,5,-5,1,-2,-3,-4,7,-7,-7,7,-1,-3,6,7,2,-5,4,-7,4,-3,2,-9,1,-1,-6,-8,9,-3,-1,4,-8,4,10,8,5,-2,-9,3,9,-8,-2,-4,-6,-7,-9,4,-3,9,2,-9,1,3,4,-1,9,10,4,4,2,8,-2,9,1,-9,7,9,1,9,-7,10,2,9,3,7,-5,-7,9,4,-3,-2,-3,8,4,-9,2,9,9,-9,1,8,-2,5,-10,-1,2,-3,6,-6,3,-5,5,8,-4,-6,2,3,10,5,-6,5,10,2,-1,10,6,-8,1,-2,-2,4,-4,-10,-6,6,-1,-10,9,9,-2,4,6,6,-8,4,9,-6,4,7,10,2,4,-2,-5,1,-2,3,6,7,10,-4,9,1,-5,-3,-4,6,-6,9,3,-9,4,5,3,-6,3,-3,-1,6,-7,-2,-2,6,-9,1,4,7,2,-2,3,-2,-9,1,-1,7,-3,-8,-7,7,9], dtype = "int16")#candidate|7459|(825,)|const|int16
call_7457 = relay.TupleGetItem(func_7314_call(relay.reshape(const_7458.astype('float64'), [80,]), relay.reshape(const_7459.astype('int16'), [825,]), ), 1)
call_7460 = relay.TupleGetItem(func_7318_call(relay.reshape(const_7458.astype('float64'), [80,]), relay.reshape(const_7459.astype('int16'), [825,]), ), 1)
func_4227_call = mod.get_global_var('func_4227')
func_4228_call = mutated_mod.get_global_var('func_4228')
call_7492 = relay.TupleGetItem(func_4227_call(), 0)
call_7493 = relay.TupleGetItem(func_4228_call(), 0)
func_6479_call = mod.get_global_var('func_6479')
func_6482_call = mutated_mod.get_global_var('func_6482')
var_7523 = relay.var("var_7523", dtype = "float64", shape = (400,))#candidate|7523|(400,)|var|float64
call_7522 = relay.TupleGetItem(func_6479_call(relay.reshape(var_7523.astype('float64'), [4, 10, 10])), 0)
call_7524 = relay.TupleGetItem(func_6482_call(relay.reshape(var_7523.astype('float64'), [4, 10, 10])), 0)
func_5023_call = mod.get_global_var('func_5023')
func_5024_call = mutated_mod.get_global_var('func_5024')
call_7531 = func_5023_call()
call_7532 = func_5023_call()
uop_7562 = relay.acosh(const_7458.astype('float32')) # shape=(40, 2)
func_5152_call = mod.get_global_var('func_5152')
func_5161_call = mutated_mod.get_global_var('func_5161')
var_7572 = relay.var("var_7572", dtype = "uint64", shape = (280,))#candidate|7572|(280,)|var|uint64
var_7573 = relay.var("var_7573", dtype = "float32", shape = (448, 1))#candidate|7573|(448, 1)|var|float32
const_7574 = relay.const([-5,9,-3,-3,-4,8,-5,-4,-8,-9,-6,6,1,-6,-2,-9,3,-2,-2,-5,3,6,-8,-1,7,-1,-6,-2,-2,6,-3,-10,4,1,8,-2,-1,8,-3,8,-10,3,-7,-1,-1,-10,1,-9,1,-10,-7,-9,-3,6,6,5,2,-2,-1,7,-1,6,-8,-8,6,9,2,-10,4,2,1,-6,5,3,2,-10,8,6,3,-4,-3,2,10,4,-1,4,6,-6,-9,-7,-10,5,-4,-3,-6,-6,1,-4,-10,-5,-7,-3,-10,-3,10,9,8,-8,-6,7,-10,-10,-1,-2,-5,3,5,-2,-7,-3,5,-6,7,-5,-7,-4,7,5,-8,-8,3,2,7,4,-9,10,-8,-8,4,-7,-6,-7,-3,-1,-1,-4,10,4,-4,-3,5,8,2,10,9,-7,8,-8,-6,4,7,2,7,-7,4], dtype = "int16")#candidate|7574|(165,)|const|int16
const_7575 = relay.const([9.037212,-7.505943,4.599876,-5.446101,3.541603,-5.759857,5.068378,0.771230,-2.902700,0.204471,7.714974,-5.863567,2.449696,-9.021046,4.781198,8.162168,7.910777,-2.385558,3.982544,8.164717,-8.342992,-4.717535,8.131223,5.616696,-2.348835,3.050634,-5.256949,-5.691598,-9.286265,4.747378,-8.488914,-7.141858,-6.216522,-1.958777,-2.888341,-8.998938,4.989004,-0.305083,4.785717,9.996683,-0.122329,5.597305,-6.064673,-5.703393,-3.589700,-5.567202,-6.266617,-4.561672,-2.326496,-1.305258,-7.329973,1.048004,4.918290,7.166337,4.844326,2.215573,8.616059,0.030720,-4.501416,-1.632603,3.274422,4.681725,-2.287702,-9.463631,-4.746967,4.090639,-1.968167,-2.236750,-5.444661,-3.733159,-3.027885,5.105124,-0.271810,6.027566,-2.408952,9.227909,6.911232,-5.077762,-4.708914,-0.883546,1.541492,3.880324,-1.639981,-8.039810,3.150430,1.195956,-0.444955,-1.819881,1.165929,7.966064,8.726587,8.977451,3.697139,-1.947229,-5.090855,-8.352241,-0.234520,3.153949,2.211233,0.907480,-2.303139,1.891242,3.877751,1.015739,9.389298,7.911026,5.960861,3.342706,-1.718442,-6.977836,-4.412942,-5.972142,0.730407,-5.907217,8.517929,7.326684,-2.503676,-2.939347,-8.344326,-8.705992,-6.825181,2.601973,-5.638905,-9.697093,-8.420336,8.522396,1.795971,-9.121183,-3.487128,-2.037270,-9.901968,9.680067,-0.378441,1.725403,-8.133202,-7.881653,0.019214,-0.541951,9.040142,-7.111997,-3.298843,-3.112293,3.974205,-8.478178,4.035560,-7.426166,-3.697850,-5.899408,4.133570,-0.744408,7.427869,0.893641,-3.909809,-8.108858,-0.876661,9.658298,8.047189,7.471686,-4.172409,-5.768016,-1.858714,-8.033001,-8.141183,4.384657,-9.110600,6.902529,-5.480284,-0.968502,1.749924,-9.129670,5.274982,-8.811054,-8.796309,8.143371,4.405582,-6.454638,-5.609817,-0.756750,-2.414312,6.987420,8.936672,-2.515725,9.699105,-1.435970,-6.424005,-2.978869,6.247131,-6.273418,-8.687576,-0.913483,4.877206,4.232439,6.881286,-1.792471,7.494815,-8.262133,3.387796,5.124031,3.686089,3.299672,-6.055155,5.845536,-0.112780,6.435119,-0.038003,-4.586979,5.261508,0.285782,3.557879,-0.440623,2.591301,-6.270070,6.944217,1.980462,4.176906,-3.796015,8.779560,2.087515,2.123771,-1.685547,5.181958,1.165172,1.571612,8.610245,4.587958,7.366396,6.780849,5.947577,3.605524,5.523012,4.808673,2.295555,-6.681476,-1.322328,5.192190,3.113893,0.999244,8.040294,2.077710,4.360310,-9.033844,-6.804939,-2.339092,0.875996,-1.823774,2.797243,-7.637524,-7.541090,2.828974,0.594935,-7.294540,8.042298,5.532598,-7.807769,-7.039610,0.503193,-8.749166,-1.772725,8.005110,6.528786,-6.345485,6.657054,3.260406,0.263745,-0.266955,3.705528,4.216135,-9.176121,-4.318314,-4.300492,8.826139,1.469692,9.438420,-4.634327,3.282557,-5.463380,-9.539375,7.343504,-8.992368,5.417149,8.514062,1.572209,4.994691,2.677002,-7.231219,-9.899602,-4.133846,4.941208,0.860513,-8.967189,6.879661,7.699947,2.853823,2.703434,1.617601,-0.724628,-4.990842,-4.870364,-7.478105,4.312863,6.347194,-1.485756,9.035100,2.296479,6.917632,-1.022545,-4.015572,3.925595,-1.463917,7.652222,4.680171,-3.559300,1.830273,5.869405,-9.643347,-8.645236,9.400177,4.162759,0.560313,4.541052], dtype = "float32")#candidate|7575|(320,)|const|float32
call_7571 = relay.TupleGetItem(func_5152_call(relay.reshape(var_7572.astype('uint64'), [4, 14, 5]), relay.reshape(var_7572.astype('uint64'), [4, 14, 5]), relay.reshape(var_7573.astype('float32'), [448,]), relay.reshape(uop_7562.astype('float64'), [80,]), relay.reshape(const_7459.astype('int16'), [825,]), relay.reshape(const_7574.astype('int16'), [165,]), relay.reshape(const_7575.astype('float32'), [320,]), ), 5)
call_7576 = relay.TupleGetItem(func_5161_call(relay.reshape(var_7572.astype('uint64'), [4, 14, 5]), relay.reshape(var_7572.astype('uint64'), [4, 14, 5]), relay.reshape(var_7573.astype('float32'), [448,]), relay.reshape(uop_7562.astype('float64'), [80,]), relay.reshape(const_7459.astype('int16'), [825,]), relay.reshape(const_7574.astype('int16'), [165,]), relay.reshape(const_7575.astype('float32'), [320,]), ), 5)
func_6762_call = mod.get_global_var('func_6762')
func_6764_call = mutated_mod.get_global_var('func_6764')
call_7580 = relay.TupleGetItem(func_6762_call(), 0)
call_7581 = relay.TupleGetItem(func_6764_call(), 0)
func_6837_call = mod.get_global_var('func_6837')
func_6839_call = mutated_mod.get_global_var('func_6839')
call_7583 = func_6837_call()
call_7584 = func_6837_call()
func_4770_call = mod.get_global_var('func_4770')
func_4773_call = mutated_mod.get_global_var('func_4773')
var_7586 = relay.var("var_7586", dtype = "float64", shape = (600,))#candidate|7586|(600,)|var|float64
call_7585 = relay.TupleGetItem(func_4770_call(relay.reshape(var_7586.astype('float64'), [6, 10, 10])), 3)
call_7587 = relay.TupleGetItem(func_4773_call(relay.reshape(var_7586.astype('float64'), [6, 10, 10])), 3)
func_5577_call = mod.get_global_var('func_5577')
func_5579_call = mutated_mod.get_global_var('func_5579')
call_7593 = func_5577_call()
call_7594 = func_5577_call()
output = relay.Tuple([call_7438,call_7457,const_7459,call_7492,call_7522,var_7523,call_7531,uop_7562,call_7571,var_7572,var_7573,const_7574,const_7575,call_7580,call_7583,call_7585,var_7586,call_7593,])
output2 = relay.Tuple([call_7439,call_7460,const_7459,call_7493,call_7524,var_7523,call_7532,uop_7562,call_7576,var_7572,var_7573,const_7574,const_7575,call_7581,call_7584,call_7587,var_7586,call_7594,])
func_7605 = relay.Function([var_7523,var_7572,var_7573,var_7586,], output)
mod['func_7605'] = func_7605
mod = relay.transform.InferType()(mod)
mutated_mod['func_7605'] = func_7605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7605_call = mutated_mod.get_global_var('func_7605')
var_7607 = relay.var("var_7607", dtype = "float64", shape = (400,))#candidate|7607|(400,)|var|float64
var_7608 = relay.var("var_7608", dtype = "uint64", shape = (280,))#candidate|7608|(280,)|var|uint64
var_7609 = relay.var("var_7609", dtype = "float32", shape = (448, 1))#candidate|7609|(448, 1)|var|float32
var_7610 = relay.var("var_7610", dtype = "float64", shape = (600,))#candidate|7610|(600,)|var|float64
call_7606 = func_7605_call(var_7607,var_7608,var_7609,var_7610,)
output = call_7606
func_7611 = relay.Function([var_7607,var_7608,var_7609,var_7610,], output)
mutated_mod['func_7611'] = func_7611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5577_call = mod.get_global_var('func_5577')
func_5579_call = mutated_mod.get_global_var('func_5579')
call_7618 = func_5577_call()
call_7619 = func_5577_call()
uop_7630 = relay.log(call_7618.astype('float32')) # shape=(1, 10, 10)
uop_7632 = relay.log(call_7619.astype('float32')) # shape=(1, 10, 10)
func_5577_call = mod.get_global_var('func_5577')
func_5579_call = mutated_mod.get_global_var('func_5579')
call_7641 = func_5577_call()
call_7642 = func_5577_call()
output = relay.Tuple([uop_7630,call_7641,])
output2 = relay.Tuple([uop_7632,call_7642,])
func_7659 = relay.Function([], output)
mod['func_7659'] = func_7659
mod = relay.transform.InferType()(mod)
mutated_mod['func_7659'] = func_7659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7659_call = mutated_mod.get_global_var('func_7659')
call_7660 = func_7659_call()
output = call_7660
func_7661 = relay.Function([], output)
mutated_mod['func_7661'] = func_7661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5544_call = mod.get_global_var('func_5544')
func_5546_call = mutated_mod.get_global_var('func_5546')
call_7722 = func_5544_call()
call_7723 = func_5544_call()
output = call_7722
output2 = call_7723
func_7727 = relay.Function([], output)
mod['func_7727'] = func_7727
mod = relay.transform.InferType()(mod)
output = func_7727()
func_7728 = relay.Function([], output)
mutated_mod['func_7728'] = func_7728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5577_call = mod.get_global_var('func_5577')
func_5579_call = mutated_mod.get_global_var('func_5579')
call_7790 = func_5577_call()
call_7791 = func_5577_call()
func_1835_call = mod.get_global_var('func_1835')
func_1838_call = mutated_mod.get_global_var('func_1838')
var_7818 = relay.var("var_7818", dtype = "int16", shape = (11, 15))#candidate|7818|(11, 15)|var|int16
var_7819 = relay.var("var_7819", dtype = "int16", shape = (825,))#candidate|7819|(825,)|var|int16
call_7817 = relay.TupleGetItem(func_1835_call(relay.reshape(var_7818.astype('int16'), [15, 1, 11]), relay.reshape(var_7819.astype('int16'), [15, 5, 11]), ), 0)
call_7820 = relay.TupleGetItem(func_1838_call(relay.reshape(var_7818.astype('int16'), [15, 1, 11]), relay.reshape(var_7819.astype('int16'), [15, 5, 11]), ), 0)
func_7659_call = mod.get_global_var('func_7659')
func_7661_call = mutated_mod.get_global_var('func_7661')
call_7824 = relay.TupleGetItem(func_7659_call(), 0)
call_7825 = relay.TupleGetItem(func_7661_call(), 0)
func_2680_call = mod.get_global_var('func_2680')
func_2685_call = mutated_mod.get_global_var('func_2685')
const_7841 = relay.const([-0.904026,3.108333,-1.520907,9.776760,4.131874,-2.336558,4.545067,0.935038,4.191108,4.441876,-2.182443,2.924826,-0.023898,2.879574,8.264480,-2.813468,3.980845,-9.664227,6.780486,-9.158382,-9.227259,-0.508264,1.361037,-9.181029,-3.493210,-8.924911,-4.605665,-0.597578,-6.602595,-2.691034,-6.419768,7.422034,0.111166,3.047776,1.171365,3.418928,9.534153,2.912095,5.527696,1.405818,7.641089,-6.114450,0.662523,-8.824006,-0.275492,-5.928072,-8.646952,9.446263,7.185798,-8.820024,-6.241448,-5.878568,1.236566,-1.719123,-7.136642,-3.455072,8.701676,7.497919,3.086485,-1.318061,8.518532,-6.343762,3.473061,4.996996,1.936522,4.865648,6.937736,9.351058,-0.676204,7.003592,0.664289,-5.977499,-6.542432,-0.196518,-6.139038,-2.621359,2.287102,0.683613,-8.531725,7.155175], dtype = "float32")#candidate|7841|(80,)|const|float32
const_7842 = relay.const([[-3.639520,0.361296,-9.997126,-9.825124],[-5.042947,-6.257642,-9.292668,-0.681756],[-4.955767,-5.360276,-6.101627,-5.145567],[-7.366190,-8.216451,-2.923526,9.495613],[-0.471698,-6.362469,8.449708,7.261856],[7.790673,-8.358897,-2.489727,0.641836],[-3.700017,7.827896,1.032672,0.763628],[7.397793,2.977786,-9.599135,-4.444135],[8.371481,2.393209,-8.315778,-8.258927],[2.104081,0.110611,1.541745,-2.683807],[-0.273047,-8.607701,1.533279,5.917010],[1.419453,-2.036288,-4.023434,-4.816093]], dtype = "float64")#candidate|7842|(12, 4)|const|float64
call_7840 = relay.TupleGetItem(func_2680_call(relay.reshape(const_7841.astype('float32'), [1, 8, 10]), relay.reshape(call_7817.astype('int16'), [5, 165]), relay.reshape(const_7842.astype('float64'), [48,]), ), 7)
call_7843 = relay.TupleGetItem(func_2685_call(relay.reshape(const_7841.astype('float32'), [1, 8, 10]), relay.reshape(call_7817.astype('int16'), [5, 165]), relay.reshape(const_7842.astype('float64'), [48,]), ), 7)
output = relay.Tuple([call_7790,call_7817,var_7818,var_7819,call_7824,call_7840,const_7841,const_7842,])
output2 = relay.Tuple([call_7791,call_7820,var_7818,var_7819,call_7825,call_7843,const_7841,const_7842,])
func_7848 = relay.Function([var_7818,var_7819,], output)
mod['func_7848'] = func_7848
mod = relay.transform.InferType()(mod)
mutated_mod['func_7848'] = func_7848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7848_call = mutated_mod.get_global_var('func_7848')
var_7850 = relay.var("var_7850", dtype = "int16", shape = (11, 15))#candidate|7850|(11, 15)|var|int16
var_7851 = relay.var("var_7851", dtype = "int16", shape = (825,))#candidate|7851|(825,)|var|int16
call_7849 = func_7848_call(var_7850,var_7851,)
output = call_7849
func_7852 = relay.Function([var_7850,var_7851,], output)
mutated_mod['func_7852'] = func_7852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6400_call = mod.get_global_var('func_6400')
func_6402_call = mutated_mod.get_global_var('func_6402')
call_7914 = relay.TupleGetItem(func_6400_call(), 0)
call_7915 = relay.TupleGetItem(func_6402_call(), 0)
output = call_7914
output2 = call_7915
func_7928 = relay.Function([], output)
mod['func_7928'] = func_7928
mod = relay.transform.InferType()(mod)
output = func_7928()
func_7929 = relay.Function([], output)
mutated_mod['func_7929'] = func_7929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7047_call = mod.get_global_var('func_7047')
func_7048_call = mutated_mod.get_global_var('func_7048')
call_7990 = relay.TupleGetItem(func_7047_call(), 0)
call_7991 = relay.TupleGetItem(func_7048_call(), 0)
func_6665_call = mod.get_global_var('func_6665')
func_6668_call = mutated_mod.get_global_var('func_6668')
const_8001 = relay.const([-0.463133,-0.599509,8.841473,-0.225845,-6.584151,-7.893582,-1.668808,6.724881,-4.991151,-2.684910,0.327624,-3.554055,4.204458,3.717644,4.852767,4.245366,-2.939256,-7.648449,0.629407,2.809331,-5.846928,1.368091,-0.225064,-3.525560,-6.565918,-9.800051,-0.019296,-4.151115,-3.141758,-7.862015,-8.047939,4.726354,7.142465,-2.434705,-5.037580,-6.026908,2.184511,0.081656,-3.195892,-7.747464,-9.966831,4.536455,-0.026381,-2.538233,0.998603,-9.860377,8.297727,-7.818935,8.289817,8.574214,-2.152679,-1.128890,-5.169892,3.253464,-3.099474,7.661413,9.315121,0.502025,-1.426198,-4.008711,3.629532,-7.248953,-6.696272,6.987017,4.991342,1.114111,3.385164,-9.668771,5.215705,-0.639110,3.034705,-9.527662,-7.906141,-1.428341,-4.176710,-5.837337,-2.743992,-5.143726,5.119011,-4.117050,-1.609682,9.061814,-5.596747,2.875340,6.203806,1.894940,6.486421,8.999068,1.160941,5.533388,-5.343788,7.885593,-0.476646,4.004479,-5.660079,-2.393444,5.720129,-8.470863,1.481897,4.307016,8.986553,-5.292953,0.924869,5.660608,5.482979,-8.893421,-1.697399,-5.643148,5.346405,8.763106,-8.176766,-9.498898,7.098842,8.402189,7.900515,2.909001,5.212523,6.587274,-7.704133,2.349457,8.254048,5.830124,-5.625468,-0.045464,-3.299955,1.241419,-8.722296,-4.333262,-0.093635,-9.574433,0.914247,-6.517579,0.515309,2.067148,-2.992983,-9.466834,-6.502418,-0.364737,5.605403,-3.903382,-2.673539,-4.462392,1.134866,-6.715037,-6.190802,8.684650,-7.066108,-9.480258,-8.219266,6.944346,6.993795,-9.571274,-8.604741,-4.754434,-2.478123,5.635776,-2.620327,8.059607,-9.418380,9.636672,-2.914602,-0.778117,-3.414222,2.192447,-5.804041,-2.716479,-3.115963,5.844648,9.282073,-5.535373,-0.451351,-6.733771,-4.713609,4.645559,1.662844,5.357857,0.557824,-2.819149,6.876194,-0.679174,5.018019,7.662805,-4.019371,-4.010658,-8.151650,2.720448,-8.898858,4.336043,0.869704,8.171018,0.453610,-1.263239,9.763805,-0.522968,-2.359354,-6.364014,9.540790,5.730137,2.438004,1.189974,0.192995,-4.112783,-2.364933,-4.597064,-6.500353,-1.180793,-5.865456,1.254822,-4.674053,-3.436972,-9.491660,-1.664138,-5.282081,0.347629,6.948463,7.908038,3.180782,-6.220887,1.064852,1.919897,-6.696072,3.636096,3.803125,-8.151704,4.122980,-7.243844,-6.750145,0.924078,7.570349,-6.201481,-6.712843,8.754946,9.697489,5.508973,-6.065026,5.464802,5.908948,4.410243,9.157108,-7.631869,4.762634,-7.454152,3.444878,-1.381003,3.233602,7.330874,4.143608,8.103491,-9.806215,5.394296,-7.592845,8.173872,-6.262691,-4.289531,0.644348,-4.885193,3.906921,-5.769764,-5.961612,8.525156,4.853380,4.602597,6.332987,9.349672,-8.993169,-0.176789,1.417399,-9.751647,7.048046,9.244364,4.703033,5.761943,4.846181,0.755794,-0.743415,7.517523,9.649705,-5.761233,5.480569,-9.005308,5.396043,-5.625497,-5.387815,-6.470485,4.014016,-8.345833,3.127956,-9.355672,1.802871,-6.385291,-9.691679,9.196928,8.048273,6.913811,-2.094465,-9.041571,-8.562871,-1.651981,4.614060,-3.274276,5.400621,9.202105,-0.555621,4.653832,5.292546,-2.849105,7.784807,7.640051,6.176202,9.988209,-0.264548,4.820704,5.216779,4.741938,-5.418173,3.127784,6.168351,-0.237996,-7.119065,6.511871,-4.325477,-5.656715,-1.199015,-4.269261,-8.096837,7.318657,6.217911,6.794454,-7.403560,4.959799,0.698317,-7.240086,7.583380,-4.842295,-7.535608,5.041617,0.486368,-5.324562,2.743681,-9.996195,6.609819,-6.546227,-5.048652,1.165840,-8.707437,-2.718229,9.299885,-3.422357,1.546185,2.583701,7.292431,-7.504284,-4.559513,-0.374860,2.621545,8.765787,-0.658539,7.074645,0.448544,5.852237,1.803964,1.347028,3.641044,1.157693,2.861581,-6.790626,9.141670,8.619161,-9.444043,7.310648,-7.036945,-0.321594,-0.790841,-0.414515,-5.096521,-1.180918,1.206660,-8.806289,1.061923,7.316990,-7.476562,5.916416,6.647693,2.691468,-1.157292,4.573163,6.630316,9.842561,-9.141606,-7.181966,-5.754776,-4.092929,-2.679372,-3.146672,7.992274,-8.439328,5.152324,4.382523,7.275651,-7.785531,-8.111078,-4.696856,1.201932,2.293244,7.419212,-0.923407,-1.316378,6.670644,-5.722451,3.396982,-6.229397,2.358032,0.884252,-9.652569,-6.133376,2.890534,-7.680904,-9.626900,0.132629,0.282299,4.367136,-1.759176,7.900898,5.815872,1.339963,6.401203,-3.421356,-5.198040,5.925496,-2.105729,1.961334,-3.381731,-8.052856,-9.142340,5.305191,-4.106886,9.479659,-6.406664,9.001897,-0.084544,-8.821182,-5.009406,2.908768,2.208684,0.559481,-5.599371,0.027722,-5.505878,7.715066,9.856699,3.043698,-5.825614,3.023094,3.336982,-0.040234,0.025835,0.193852,4.135919,-1.536695,0.703029,6.077098,2.526356,1.739165,-0.918592,-3.014675,5.587273,6.576094,-2.278120,-7.880676,0.249708,-3.362961,-3.609760,-7.378726,-8.925073,-7.371208,-7.621024,8.725844,-8.719605,-8.769834,6.896982,-9.963038,-2.437159,-4.408978,-6.414131,-3.379687,4.295036,0.361046,-9.502511,-4.404063,-4.031527,-0.167535,-9.073685,-7.245262,-5.721051,2.638471,2.736977,-3.889007,2.232899,6.316884,-5.822303,-2.055156,-1.967677,1.970470,8.373182,3.844694,-8.851720,0.204635,7.621537,2.334663,-2.673000,8.889151,-0.562301,9.401480,3.374698,-5.235840,-9.352257,9.341160,-4.514822,2.191407,-5.995017,5.288303,-5.849609,8.360617,4.393156,-3.890138,4.042376,9.910476,3.558427,-2.337107,0.333942,-8.717339,3.170919,-4.224644,-1.697962,0.395307,-7.278868,9.950132,3.830301,-9.266790,1.940619,-6.520612,9.142263,7.028805,-0.546357,1.859788,-9.566847,7.275488,8.101482,2.479928,4.066785,4.547202,7.116217,0.849313,8.238557,3.656136,-0.603273,-7.377343,-5.977805,-8.561167,1.714470,-8.951139,-1.667784,6.507469,-6.522462,2.538809,7.921557,6.065291,-0.923598,-1.599091,6.239051,-1.913495,0.127620,1.021728,-0.341273,5.343950,1.120202,6.376872,9.541828,6.485620,9.965716,-7.238337,4.668590,-5.982381,-4.342476,-8.166431,-9.540521,7.213586,9.588167,8.193602,-5.271230,5.153023,7.176810,8.497222,4.459884,-3.538366,-2.226220,7.406325,-6.963522,5.807013,-7.328547], dtype = "float64")#candidate|8001|(600,)|const|float64
call_8000 = relay.TupleGetItem(func_6665_call(relay.reshape(const_8001.astype('float64'), [300, 2]), relay.reshape(const_8001.astype('int8'), [300, 2]), ), 5)
call_8002 = relay.TupleGetItem(func_6668_call(relay.reshape(const_8001.astype('float64'), [300, 2]), relay.reshape(const_8001.astype('int8'), [300, 2]), ), 5)
output = relay.Tuple([call_7990,call_8000,const_8001,])
output2 = relay.Tuple([call_7991,call_8002,const_8001,])
func_8003 = relay.Function([], output)
mod['func_8003'] = func_8003
mod = relay.transform.InferType()(mod)
mutated_mod['func_8003'] = func_8003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8003_call = mutated_mod.get_global_var('func_8003')
call_8004 = func_8003_call()
output = call_8004
func_8005 = relay.Function([], output)
mutated_mod['func_8005'] = func_8005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6400_call = mod.get_global_var('func_6400')
func_6402_call = mutated_mod.get_global_var('func_6402')
call_8040 = relay.TupleGetItem(func_6400_call(), 0)
call_8041 = relay.TupleGetItem(func_6402_call(), 0)
output = relay.Tuple([call_8040,])
output2 = relay.Tuple([call_8041,])
func_8050 = relay.Function([], output)
mod['func_8050'] = func_8050
mod = relay.transform.InferType()(mod)
mutated_mod['func_8050'] = func_8050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8050_call = mutated_mod.get_global_var('func_8050')
call_8051 = func_8050_call()
output = call_8051
func_8052 = relay.Function([], output)
mutated_mod['func_8052'] = func_8052
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8074 = relay.var("var_8074", dtype = "float32", shape = (5, 9, 4))#candidate|8074|(5, 9, 4)|var|float32
uop_8075 = relay.log10(var_8074.astype('float32')) # shape=(5, 9, 4)
output = relay.Tuple([uop_8075,])
output2 = relay.Tuple([uop_8075,])
func_8079 = relay.Function([var_8074,], output)
mod['func_8079'] = func_8079
mod = relay.transform.InferType()(mod)
var_8080 = relay.var("var_8080", dtype = "float32", shape = (5, 9, 4))#candidate|8080|(5, 9, 4)|var|float32
output = func_8079(var_8080)
func_8081 = relay.Function([var_8080], output)
mutated_mod['func_8081'] = func_8081
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4628_call = mod.get_global_var('func_4628')
func_4629_call = mutated_mod.get_global_var('func_4629')
call_8125 = func_4628_call()
call_8126 = func_4628_call()
func_3695_call = mod.get_global_var('func_3695')
func_3700_call = mutated_mod.get_global_var('func_3700')
var_8141 = relay.var("var_8141", dtype = "float32", shape = (320,))#candidate|8141|(320,)|var|float32
var_8142 = relay.var("var_8142", dtype = "int16", shape = (165,))#candidate|8142|(165,)|var|int16
call_8140 = relay.TupleGetItem(func_3695_call(relay.reshape(var_8141.astype('float32'), [5, 4, 16]), relay.reshape(var_8142.astype('int16'), [11, 15]), relay.reshape(var_8141.astype('float32'), [5, 4, 16]), ), 0)
call_8143 = relay.TupleGetItem(func_3700_call(relay.reshape(var_8141.astype('float32'), [5, 4, 16]), relay.reshape(var_8142.astype('int16'), [11, 15]), relay.reshape(var_8141.astype('float32'), [5, 4, 16]), ), 0)
var_8160 = relay.var("var_8160", dtype = "int16", shape = (15, 5, 11))#candidate|8160|(15, 5, 11)|var|int16
bop_8161 = relay.logical_or(call_8140.astype('bool'), relay.reshape(var_8160.astype('bool'), relay.shape_of(call_8140))) # shape=(15, 5, 11)
bop_8164 = relay.logical_or(call_8143.astype('bool'), relay.reshape(var_8160.astype('bool'), relay.shape_of(call_8143))) # shape=(15, 5, 11)
func_7257_call = mod.get_global_var('func_7257')
func_7259_call = mutated_mod.get_global_var('func_7259')
call_8165 = relay.TupleGetItem(func_7257_call(), 0)
call_8166 = relay.TupleGetItem(func_7259_call(), 0)
func_6738_call = mod.get_global_var('func_6738')
func_6739_call = mutated_mod.get_global_var('func_6739')
call_8167 = func_6738_call()
call_8168 = func_6738_call()
output = relay.Tuple([call_8125,var_8141,var_8142,bop_8161,call_8165,call_8167,])
output2 = relay.Tuple([call_8126,var_8141,var_8142,bop_8164,call_8166,call_8168,])
func_8175 = relay.Function([var_8141,var_8142,var_8160,], output)
mod['func_8175'] = func_8175
mod = relay.transform.InferType()(mod)
var_8176 = relay.var("var_8176", dtype = "float32", shape = (320,))#candidate|8176|(320,)|var|float32
var_8177 = relay.var("var_8177", dtype = "int16", shape = (165,))#candidate|8177|(165,)|var|int16
var_8178 = relay.var("var_8178", dtype = "int16", shape = (15, 5, 11))#candidate|8178|(15, 5, 11)|var|int16
output = func_8175(var_8176,var_8177,var_8178,)
func_8179 = relay.Function([var_8176,var_8177,var_8178,], output)
mutated_mod['func_8179'] = func_8179
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6596_call = mod.get_global_var('func_6596')
func_6597_call = mutated_mod.get_global_var('func_6597')
call_8290 = relay.TupleGetItem(func_6596_call(), 1)
call_8291 = relay.TupleGetItem(func_6597_call(), 1)
output = call_8290
output2 = call_8291
func_8310 = relay.Function([], output)
mod['func_8310'] = func_8310
mod = relay.transform.InferType()(mod)
output = func_8310()
func_8311 = relay.Function([], output)
mutated_mod['func_8311'] = func_8311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7727_call = mod.get_global_var('func_7727')
func_7728_call = mutated_mod.get_global_var('func_7728')
call_8325 = func_7727_call()
call_8326 = func_7727_call()
output = call_8325
output2 = call_8326
func_8343 = relay.Function([], output)
mod['func_8343'] = func_8343
mod = relay.transform.InferType()(mod)
mutated_mod['func_8343'] = func_8343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8343_call = mutated_mod.get_global_var('func_8343')
call_8344 = func_8343_call()
output = call_8344
func_8345 = relay.Function([], output)
mutated_mod['func_8345'] = func_8345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6400_call = mod.get_global_var('func_6400')
func_6402_call = mutated_mod.get_global_var('func_6402')
call_8348 = relay.TupleGetItem(func_6400_call(), 0)
call_8349 = relay.TupleGetItem(func_6402_call(), 0)
output = relay.Tuple([call_8348,])
output2 = relay.Tuple([call_8349,])
func_8353 = relay.Function([], output)
mod['func_8353'] = func_8353
mod = relay.transform.InferType()(mod)
mutated_mod['func_8353'] = func_8353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8353_call = mutated_mod.get_global_var('func_8353')
call_8354 = func_8353_call()
output = call_8354
func_8355 = relay.Function([], output)
mutated_mod['func_8355'] = func_8355
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5023_call = mod.get_global_var('func_5023')
func_5024_call = mutated_mod.get_global_var('func_5024')
call_8372 = func_5023_call()
call_8373 = func_5023_call()
func_7727_call = mod.get_global_var('func_7727')
func_7728_call = mutated_mod.get_global_var('func_7728')
call_8399 = func_7727_call()
call_8400 = func_7727_call()
var_8403 = relay.var("var_8403", dtype = "float64", shape = (15, 10, 10))#candidate|8403|(15, 10, 10)|var|float64
bop_8404 = relay.bitwise_or(call_8399.astype('int8'), var_8403.astype('int8')) # shape=(15, 10, 10)
bop_8407 = relay.bitwise_or(call_8400.astype('int8'), var_8403.astype('int8')) # shape=(15, 10, 10)
output = relay.Tuple([call_8372,bop_8404,])
output2 = relay.Tuple([call_8373,bop_8407,])
func_8411 = relay.Function([var_8403,], output)
mod['func_8411'] = func_8411
mod = relay.transform.InferType()(mod)
var_8412 = relay.var("var_8412", dtype = "float64", shape = (15, 10, 10))#candidate|8412|(15, 10, 10)|var|float64
output = func_8411(var_8412)
func_8413 = relay.Function([var_8412], output)
mutated_mod['func_8413'] = func_8413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7659_call = mod.get_global_var('func_7659')
func_7661_call = mutated_mod.get_global_var('func_7661')
call_8415 = relay.TupleGetItem(func_7659_call(), 1)
call_8416 = relay.TupleGetItem(func_7661_call(), 1)
output = relay.Tuple([call_8415,])
output2 = relay.Tuple([call_8416,])
func_8419 = relay.Function([], output)
mod['func_8419'] = func_8419
mod = relay.transform.InferType()(mod)
output = func_8419()
func_8420 = relay.Function([], output)
mutated_mod['func_8420'] = func_8420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6738_call = mod.get_global_var('func_6738')
func_6739_call = mutated_mod.get_global_var('func_6739')
call_8617 = func_6738_call()
call_8618 = func_6738_call()
output = call_8617
output2 = call_8618
func_8650 = relay.Function([], output)
mod['func_8650'] = func_8650
mod = relay.transform.InferType()(mod)
output = func_8650()
func_8651 = relay.Function([], output)
mutated_mod['func_8651'] = func_8651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8343_call = mod.get_global_var('func_8343')
func_8345_call = mutated_mod.get_global_var('func_8345')
call_8661 = func_8343_call()
call_8662 = func_8343_call()
var_8692 = relay.var("var_8692", dtype = "float64", shape = (9, 10, 10))#candidate|8692|(9, 10, 10)|var|float64
bop_8693 = relay.bitwise_or(call_8661.astype('uint8'), var_8692.astype('uint8')) # shape=(9, 10, 10)
bop_8696 = relay.bitwise_or(call_8662.astype('uint8'), var_8692.astype('uint8')) # shape=(9, 10, 10)
func_5796_call = mod.get_global_var('func_5796')
func_5798_call = mutated_mod.get_global_var('func_5798')
call_8705 = relay.TupleGetItem(func_5796_call(), 0)
call_8706 = relay.TupleGetItem(func_5798_call(), 0)
func_7392_call = mod.get_global_var('func_7392')
func_7393_call = mutated_mod.get_global_var('func_7393')
call_8710 = relay.TupleGetItem(func_7392_call(), 0)
call_8711 = relay.TupleGetItem(func_7393_call(), 0)
output = relay.Tuple([bop_8693,call_8705,call_8710,])
output2 = relay.Tuple([bop_8696,call_8706,call_8711,])
func_8717 = relay.Function([var_8692,], output)
mod['func_8717'] = func_8717
mod = relay.transform.InferType()(mod)
mutated_mod['func_8717'] = func_8717
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8718 = relay.var("var_8718", dtype = "float64", shape = (9, 10, 10))#candidate|8718|(9, 10, 10)|var|float64
func_8717_call = mutated_mod.get_global_var('func_8717')
call_8719 = func_8717_call(var_8718)
output = call_8719
func_8720 = relay.Function([var_8718], output)
mutated_mod['func_8720'] = func_8720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5544_call = mod.get_global_var('func_5544')
func_5546_call = mutated_mod.get_global_var('func_5546')
call_8726 = func_5544_call()
call_8727 = func_5544_call()
func_6738_call = mod.get_global_var('func_6738')
func_6739_call = mutated_mod.get_global_var('func_6739')
call_8730 = func_6738_call()
call_8731 = func_6738_call()
func_6762_call = mod.get_global_var('func_6762')
func_6764_call = mutated_mod.get_global_var('func_6764')
call_8745 = relay.TupleGetItem(func_6762_call(), 0)
call_8746 = relay.TupleGetItem(func_6764_call(), 0)
func_5858_call = mod.get_global_var('func_5858')
func_5860_call = mutated_mod.get_global_var('func_5860')
const_8751 = relay.const([-4.067327,-9.293703,-6.888059,-7.656579,7.537630,-2.756003,-3.689228,-5.554329,-1.585428,9.320094,-7.185351,3.489784,5.451893,-6.284597,-4.876766,9.539631,-6.855291,2.725613,-9.534973,-2.567531,-6.558046,3.217263,4.776840,7.787574,0.972933,8.927153,3.609650,1.426037], dtype = "float64")#candidate|8751|(28,)|const|float64
call_8750 = func_5858_call(relay.reshape(const_8751.astype('float64'), [2, 1, 14]))
call_8752 = func_5858_call(relay.reshape(const_8751.astype('float64'), [2, 1, 14]))
bop_8758 = relay.minimum(call_8745.astype('uint16'), relay.reshape(call_8726.astype('uint16'), relay.shape_of(call_8745))) # shape=(1, 10, 10)
bop_8761 = relay.minimum(call_8746.astype('uint16'), relay.reshape(call_8727.astype('uint16'), relay.shape_of(call_8746))) # shape=(1, 10, 10)
output = relay.Tuple([call_8730,call_8750,const_8751,bop_8758,])
output2 = relay.Tuple([call_8731,call_8752,const_8751,bop_8761,])
func_8763 = relay.Function([], output)
mod['func_8763'] = func_8763
mod = relay.transform.InferType()(mod)
mutated_mod['func_8763'] = func_8763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8763_call = mutated_mod.get_global_var('func_8763')
call_8764 = func_8763_call()
output = call_8764
func_8765 = relay.Function([], output)
mutated_mod['func_8765'] = func_8765
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8763_call = mod.get_global_var('func_8763')
func_8765_call = mutated_mod.get_global_var('func_8765')
call_8779 = relay.TupleGetItem(func_8763_call(), 2)
call_8780 = relay.TupleGetItem(func_8765_call(), 2)
output = relay.Tuple([call_8779,])
output2 = relay.Tuple([call_8780,])
func_8794 = relay.Function([], output)
mod['func_8794'] = func_8794
mod = relay.transform.InferType()(mod)
mutated_mod['func_8794'] = func_8794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8794_call = mutated_mod.get_global_var('func_8794')
call_8795 = func_8794_call()
output = call_8795
func_8796 = relay.Function([], output)
mutated_mod['func_8796'] = func_8796
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8050_call = mod.get_global_var('func_8050')
func_8052_call = mutated_mod.get_global_var('func_8052')
call_8839 = relay.TupleGetItem(func_8050_call(), 0)
call_8840 = relay.TupleGetItem(func_8052_call(), 0)
output = relay.Tuple([call_8839,])
output2 = relay.Tuple([call_8840,])
func_8883 = relay.Function([], output)
mod['func_8883'] = func_8883
mod = relay.transform.InferType()(mod)
mutated_mod['func_8883'] = func_8883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8883_call = mutated_mod.get_global_var('func_8883')
call_8884 = func_8883_call()
output = call_8884
func_8885 = relay.Function([], output)
mutated_mod['func_8885'] = func_8885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8050_call = mod.get_global_var('func_8050')
func_8052_call = mutated_mod.get_global_var('func_8052')
call_8893 = relay.TupleGetItem(func_8050_call(), 0)
call_8894 = relay.TupleGetItem(func_8052_call(), 0)
func_7257_call = mod.get_global_var('func_7257')
func_7259_call = mutated_mod.get_global_var('func_7259')
call_8902 = relay.TupleGetItem(func_7257_call(), 0)
call_8903 = relay.TupleGetItem(func_7259_call(), 0)
output = relay.Tuple([call_8893,call_8902,])
output2 = relay.Tuple([call_8894,call_8903,])
func_8908 = relay.Function([], output)
mod['func_8908'] = func_8908
mod = relay.transform.InferType()(mod)
mutated_mod['func_8908'] = func_8908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8908_call = mutated_mod.get_global_var('func_8908')
call_8909 = func_8908_call()
output = call_8909
func_8910 = relay.Function([], output)
mutated_mod['func_8910'] = func_8910
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6596_call = mod.get_global_var('func_6596')
func_6597_call = mutated_mod.get_global_var('func_6597')
call_8950 = relay.TupleGetItem(func_6596_call(), 1)
call_8951 = relay.TupleGetItem(func_6597_call(), 1)
output = relay.Tuple([call_8950,])
output2 = relay.Tuple([call_8951,])
func_8955 = relay.Function([], output)
mod['func_8955'] = func_8955
mod = relay.transform.InferType()(mod)
mutated_mod['func_8955'] = func_8955
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8955_call = mutated_mod.get_global_var('func_8955')
call_8956 = func_8955_call()
output = call_8956
func_8957 = relay.Function([], output)
mutated_mod['func_8957'] = func_8957
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9014 = relay.var("var_9014", dtype = "float64", shape = (7, 5, 7))#candidate|9014|(7, 5, 7)|var|float64
uop_9015 = relay.tan(var_9014.astype('float64')) # shape=(7, 5, 7)
output = uop_9015
output2 = uop_9015
func_9048 = relay.Function([var_9014,], output)
mod['func_9048'] = func_9048
mod = relay.transform.InferType()(mod)
var_9049 = relay.var("var_9049", dtype = "float64", shape = (7, 5, 7))#candidate|9049|(7, 5, 7)|var|float64
output = func_9048(var_9049)
func_9050 = relay.Function([var_9049], output)
mutated_mod['func_9050'] = func_9050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5180_call = mod.get_global_var('func_5180')
func_5181_call = mutated_mod.get_global_var('func_5181')
call_9107 = relay.TupleGetItem(func_5180_call(), 0)
call_9108 = relay.TupleGetItem(func_5181_call(), 0)
output = relay.Tuple([call_9107,])
output2 = relay.Tuple([call_9108,])
func_9109 = relay.Function([], output)
mod['func_9109'] = func_9109
mod = relay.transform.InferType()(mod)
mutated_mod['func_9109'] = func_9109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9109_call = mutated_mod.get_global_var('func_9109')
call_9110 = func_9109_call()
output = call_9110
func_9111 = relay.Function([], output)
mutated_mod['func_9111'] = func_9111
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8419_call = mod.get_global_var('func_8419')
func_8420_call = mutated_mod.get_global_var('func_8420')
call_9259 = relay.TupleGetItem(func_8419_call(), 0)
call_9260 = relay.TupleGetItem(func_8420_call(), 0)
output = relay.Tuple([call_9259,])
output2 = relay.Tuple([call_9260,])
func_9275 = relay.Function([], output)
mod['func_9275'] = func_9275
mod = relay.transform.InferType()(mod)
output = func_9275()
func_9276 = relay.Function([], output)
mutated_mod['func_9276'] = func_9276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5796_call = mod.get_global_var('func_5796')
func_5798_call = mutated_mod.get_global_var('func_5798')
call_9289 = relay.TupleGetItem(func_5796_call(), 0)
call_9290 = relay.TupleGetItem(func_5798_call(), 0)
func_8079_call = mod.get_global_var('func_8079')
func_8081_call = mutated_mod.get_global_var('func_8081')
const_9318 = relay.const([5.658397,-9.784642,-2.060483,-6.362117,-2.944885,-4.884554,-0.849417,-3.336079,-6.255323,-2.615185,-0.605389,8.484192,1.581335,9.140996,-4.558887,-9.740068,9.331346,6.445748,5.569885,5.849276,-1.181958,-7.989658,-4.526654,3.596521,6.887749,9.580053,-0.856899,9.811072,-3.467517,-8.171424,-9.916495,-7.004173,-2.150591,9.997027,-6.614125,7.806038,-1.323914,6.102480,-3.124581,6.669971,-8.742682,-5.953419,-4.862218,-7.955830,-7.452320,0.216255,1.194014,5.227244,2.393169,-6.784834,4.258829,-9.037022,4.463932,-2.196770,-0.798656,0.034987,-7.402906,8.764736,3.014718,-4.920698,5.371195,-0.974927,1.900090,-7.901335,-4.532975,-2.498962,-5.354267,7.797966,-8.367815,8.380569,-8.769679,8.030629,-2.705689,7.956285,4.734947,-9.519480,8.176269,1.240636,-5.840559,6.915840,-5.651368,-6.237680,-7.029825,-6.724810,8.319098,8.045415,-3.486770,-0.665663,-7.585499,7.713709,0.129952,-3.367995,-0.079872,-2.467576,9.836730,-2.793904,5.017696,-1.824641,-2.526656,4.038231,-6.887828,9.537598,8.576331,-7.654960,1.113016,7.130768,7.759704,7.209400,-6.976894,-3.798482,5.276826,0.414172,4.125356,-3.122006,8.982321,6.919033,9.236186,-0.149940,-1.395991,-2.024315,-8.000207,7.234231,6.788927,-6.865487,-8.817562,5.431702,3.413295,-8.907723,-0.087672,-6.912586,-6.409934,9.741435,7.499668,2.579451,-6.500654,6.973817,0.975029,-8.267352,-6.717545,-3.792693,0.992118,-2.219211,2.099044,6.253571,-5.527435,0.339800,5.943964,-3.881731,-5.897900,9.614242,5.032039,-6.444658,9.163950,4.929189,4.760648,-7.550609,8.073950,3.631668,0.991665,-1.236832,-9.206233,6.426936,-0.499507,-5.643711,0.031651,-2.596921,7.573681,9.274232,2.015989,-9.384459,5.489138,-8.473231,5.480698,8.850936,-8.875594,-1.929027,9.005228,4.116357,8.701065,-3.113864], dtype = "float32")#candidate|9318|(180,)|const|float32
call_9317 = relay.TupleGetItem(func_8079_call(relay.reshape(const_9318.astype('float32'), [5, 9, 4])), 0)
call_9319 = relay.TupleGetItem(func_8081_call(relay.reshape(const_9318.astype('float32'), [5, 9, 4])), 0)
output = relay.Tuple([call_9289,call_9317,const_9318,])
output2 = relay.Tuple([call_9290,call_9319,const_9318,])
func_9321 = relay.Function([], output)
mod['func_9321'] = func_9321
mod = relay.transform.InferType()(mod)
mutated_mod['func_9321'] = func_9321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9321_call = mutated_mod.get_global_var('func_9321')
call_9322 = func_9321_call()
output = call_9322
func_9323 = relay.Function([], output)
mutated_mod['func_9323'] = func_9323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5796_call = mod.get_global_var('func_5796')
func_5798_call = mutated_mod.get_global_var('func_5798')
call_9324 = relay.TupleGetItem(func_5796_call(), 0)
call_9325 = relay.TupleGetItem(func_5798_call(), 0)
uop_9338 = relay.cos(call_9324.astype('float64')) # shape=(1, 10, 10)
uop_9340 = relay.cos(call_9325.astype('float64')) # shape=(1, 10, 10)
output = relay.Tuple([uop_9338,])
output2 = relay.Tuple([uop_9340,])
func_9346 = relay.Function([], output)
mod['func_9346'] = func_9346
mod = relay.transform.InferType()(mod)
output = func_9346()
func_9347 = relay.Function([], output)
mutated_mod['func_9347'] = func_9347
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8050_call = mod.get_global_var('func_8050')
func_8052_call = mutated_mod.get_global_var('func_8052')
call_9359 = relay.TupleGetItem(func_8050_call(), 0)
call_9360 = relay.TupleGetItem(func_8052_call(), 0)
func_5378_call = mod.get_global_var('func_5378')
func_5379_call = mutated_mod.get_global_var('func_5379')
call_9386 = relay.TupleGetItem(func_5378_call(), 0)
call_9387 = relay.TupleGetItem(func_5379_call(), 0)
output = relay.Tuple([call_9359,call_9386,])
output2 = relay.Tuple([call_9360,call_9387,])
func_9390 = relay.Function([], output)
mod['func_9390'] = func_9390
mod = relay.transform.InferType()(mod)
mutated_mod['func_9390'] = func_9390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9390_call = mutated_mod.get_global_var('func_9390')
call_9391 = func_9390_call()
output = call_9391
func_9392 = relay.Function([], output)
mutated_mod['func_9392'] = func_9392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7928_call = mod.get_global_var('func_7928')
func_7929_call = mutated_mod.get_global_var('func_7929')
call_9469 = func_7928_call()
call_9470 = func_7928_call()
output = relay.Tuple([call_9469,])
output2 = relay.Tuple([call_9470,])
func_9475 = relay.Function([], output)
mod['func_9475'] = func_9475
mod = relay.transform.InferType()(mod)
output = func_9475()
func_9476 = relay.Function([], output)
mutated_mod['func_9476'] = func_9476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6921_call = mod.get_global_var('func_6921')
func_6922_call = mutated_mod.get_global_var('func_6922')
call_9507 = func_6921_call()
call_9508 = func_6921_call()
output = relay.Tuple([call_9507,])
output2 = relay.Tuple([call_9508,])
func_9511 = relay.Function([], output)
mod['func_9511'] = func_9511
mod = relay.transform.InferType()(mod)
output = func_9511()
func_9512 = relay.Function([], output)
mutated_mod['func_9512'] = func_9512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8050_call = mod.get_global_var('func_8050')
func_8052_call = mutated_mod.get_global_var('func_8052')
call_9630 = relay.TupleGetItem(func_8050_call(), 0)
call_9631 = relay.TupleGetItem(func_8052_call(), 0)
func_7392_call = mod.get_global_var('func_7392')
func_7393_call = mutated_mod.get_global_var('func_7393')
call_9660 = relay.TupleGetItem(func_7392_call(), 1)
call_9661 = relay.TupleGetItem(func_7393_call(), 1)
output = relay.Tuple([call_9630,call_9660,])
output2 = relay.Tuple([call_9631,call_9661,])
func_9664 = relay.Function([], output)
mod['func_9664'] = func_9664
mod = relay.transform.InferType()(mod)
mutated_mod['func_9664'] = func_9664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9664_call = mutated_mod.get_global_var('func_9664')
call_9665 = func_9664_call()
output = call_9665
func_9666 = relay.Function([], output)
mutated_mod['func_9666'] = func_9666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5267_call = mod.get_global_var('func_5267')
func_5268_call = mutated_mod.get_global_var('func_5268')
call_9682 = relay.TupleGetItem(func_5267_call(), 0)
call_9683 = relay.TupleGetItem(func_5268_call(), 0)
output = call_9682
output2 = call_9683
func_9689 = relay.Function([], output)
mod['func_9689'] = func_9689
mod = relay.transform.InferType()(mod)
mutated_mod['func_9689'] = func_9689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9689_call = mutated_mod.get_global_var('func_9689')
call_9690 = func_9689_call()
output = call_9690
func_9691 = relay.Function([], output)
mutated_mod['func_9691'] = func_9691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4654_call = mod.get_global_var('func_4654')
func_4656_call = mutated_mod.get_global_var('func_4656')
call_9716 = func_4654_call()
call_9717 = func_4654_call()
output = relay.Tuple([call_9716,])
output2 = relay.Tuple([call_9717,])
func_9720 = relay.Function([], output)
mod['func_9720'] = func_9720
mod = relay.transform.InferType()(mod)
mutated_mod['func_9720'] = func_9720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9720_call = mutated_mod.get_global_var('func_9720')
call_9721 = func_9720_call()
output = call_9721
func_9722 = relay.Function([], output)
mutated_mod['func_9722'] = func_9722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9664_call = mod.get_global_var('func_9664')
func_9666_call = mutated_mod.get_global_var('func_9666')
call_9728 = relay.TupleGetItem(func_9664_call(), 0)
call_9729 = relay.TupleGetItem(func_9666_call(), 0)
output = relay.Tuple([call_9728,])
output2 = relay.Tuple([call_9729,])
func_9731 = relay.Function([], output)
mod['func_9731'] = func_9731
mod = relay.transform.InferType()(mod)
mutated_mod['func_9731'] = func_9731
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9731_call = mutated_mod.get_global_var('func_9731')
call_9732 = func_9731_call()
output = call_9732
func_9733 = relay.Function([], output)
mutated_mod['func_9733'] = func_9733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9511_call = mod.get_global_var('func_9511')
func_9512_call = mutated_mod.get_global_var('func_9512')
call_9768 = relay.TupleGetItem(func_9511_call(), 0)
call_9769 = relay.TupleGetItem(func_9512_call(), 0)
output = relay.Tuple([call_9768,])
output2 = relay.Tuple([call_9769,])
func_9844 = relay.Function([], output)
mod['func_9844'] = func_9844
mod = relay.transform.InferType()(mod)
output = func_9844()
func_9845 = relay.Function([], output)
mutated_mod['func_9845'] = func_9845
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6785_call = mod.get_global_var('func_6785')
func_6786_call = mutated_mod.get_global_var('func_6786')
call_9872 = relay.TupleGetItem(func_6785_call(), 0)
call_9873 = relay.TupleGetItem(func_6786_call(), 0)
func_5559_call = mod.get_global_var('func_5559')
func_5561_call = mutated_mod.get_global_var('func_5561')
call_9880 = relay.TupleGetItem(func_5559_call(), 0)
call_9881 = relay.TupleGetItem(func_5561_call(), 0)
func_8353_call = mod.get_global_var('func_8353')
func_8355_call = mutated_mod.get_global_var('func_8355')
call_9892 = relay.TupleGetItem(func_8353_call(), 0)
call_9893 = relay.TupleGetItem(func_8355_call(), 0)
func_8343_call = mod.get_global_var('func_8343')
func_8345_call = mutated_mod.get_global_var('func_8345')
call_9901 = func_8343_call()
call_9902 = func_8343_call()
bop_9906 = relay.add(call_9880.astype('int32'), relay.reshape(call_9872.astype('int32'), relay.shape_of(call_9880))) # shape=(1, 10, 10)
bop_9909 = relay.add(call_9881.astype('int32'), relay.reshape(call_9873.astype('int32'), relay.shape_of(call_9881))) # shape=(1, 10, 10)
output = relay.Tuple([call_9892,call_9901,bop_9906,])
output2 = relay.Tuple([call_9893,call_9902,bop_9909,])
func_9910 = relay.Function([], output)
mod['func_9910'] = func_9910
mod = relay.transform.InferType()(mod)
output = func_9910()
func_9911 = relay.Function([], output)
mutated_mod['func_9911'] = func_9911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8310_call = mod.get_global_var('func_8310')
func_8311_call = mutated_mod.get_global_var('func_8311')
call_9932 = func_8310_call()
call_9933 = func_8310_call()
var_9934 = relay.var("var_9934", dtype = "float64", shape = (12, 10, 10))#candidate|9934|(12, 10, 10)|var|float64
bop_9935 = relay.right_shift(call_9932.astype('int16'), var_9934.astype('int16')) # shape=(12, 10, 10)
bop_9938 = relay.right_shift(call_9933.astype('int16'), var_9934.astype('int16')) # shape=(12, 10, 10)
var_9946 = relay.var("var_9946", dtype = "int16", shape = (12, 10, 10))#candidate|9946|(12, 10, 10)|var|int16
bop_9947 = relay.logical_xor(bop_9935.astype('uint8'), relay.reshape(var_9946.astype('uint8'), relay.shape_of(bop_9935))) # shape=(12, 10, 10)
bop_9950 = relay.logical_xor(bop_9938.astype('uint8'), relay.reshape(var_9946.astype('uint8'), relay.shape_of(bop_9938))) # shape=(12, 10, 10)
uop_9951 = relay.log10(bop_9935.astype('float32')) # shape=(12, 10, 10)
uop_9953 = relay.log10(bop_9938.astype('float32')) # shape=(12, 10, 10)
func_6273_call = mod.get_global_var('func_6273')
func_6275_call = mutated_mod.get_global_var('func_6275')
call_9956 = relay.TupleGetItem(func_6273_call(), 0)
call_9957 = relay.TupleGetItem(func_6275_call(), 0)
output = relay.Tuple([bop_9947,uop_9951,call_9956,])
output2 = relay.Tuple([bop_9950,uop_9953,call_9957,])
func_9974 = relay.Function([var_9934,var_9946,], output)
mod['func_9974'] = func_9974
mod = relay.transform.InferType()(mod)
mutated_mod['func_9974'] = func_9974
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9974_call = mutated_mod.get_global_var('func_9974')
var_9976 = relay.var("var_9976", dtype = "float64", shape = (12, 10, 10))#candidate|9976|(12, 10, 10)|var|float64
var_9977 = relay.var("var_9977", dtype = "int16", shape = (12, 10, 10))#candidate|9977|(12, 10, 10)|var|int16
call_9975 = func_9974_call(var_9976,var_9977,)
output = call_9975
func_9978 = relay.Function([var_9976,var_9977,], output)
mutated_mod['func_9978'] = func_9978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7257_call = mod.get_global_var('func_7257')
func_7259_call = mutated_mod.get_global_var('func_7259')
call_10037 = relay.TupleGetItem(func_7257_call(), 0)
call_10038 = relay.TupleGetItem(func_7259_call(), 0)
output = call_10037
output2 = call_10038
func_10043 = relay.Function([], output)
mod['func_10043'] = func_10043
mod = relay.transform.InferType()(mod)
output = func_10043()
func_10044 = relay.Function([], output)
mutated_mod['func_10044'] = func_10044
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10100 = relay.var("var_10100", dtype = "float64", shape = (13, 16, 14))#candidate|10100|(13, 16, 14)|var|float64
var_10101 = relay.var("var_10101", dtype = "float64", shape = (13, 16, 14))#candidate|10101|(13, 16, 14)|var|float64
bop_10102 = relay.divide(var_10100.astype('float64'), relay.reshape(var_10101.astype('float64'), relay.shape_of(var_10100))) # shape=(13, 16, 14)
output = relay.Tuple([bop_10102,])
output2 = relay.Tuple([bop_10102,])
func_10105 = relay.Function([var_10100,var_10101,], output)
mod['func_10105'] = func_10105
mod = relay.transform.InferType()(mod)
mutated_mod['func_10105'] = func_10105
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10105_call = mutated_mod.get_global_var('func_10105')
var_10107 = relay.var("var_10107", dtype = "float64", shape = (13, 16, 14))#candidate|10107|(13, 16, 14)|var|float64
var_10108 = relay.var("var_10108", dtype = "float64", shape = (13, 16, 14))#candidate|10108|(13, 16, 14)|var|float64
call_10106 = func_10105_call(var_10107,var_10108,)
output = call_10106
func_10109 = relay.Function([var_10107,var_10108,], output)
mutated_mod['func_10109'] = func_10109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8050_call = mod.get_global_var('func_8050')
func_8052_call = mutated_mod.get_global_var('func_8052')
call_10146 = relay.TupleGetItem(func_8050_call(), 0)
call_10147 = relay.TupleGetItem(func_8052_call(), 0)
output = call_10146
output2 = call_10147
func_10159 = relay.Function([], output)
mod['func_10159'] = func_10159
mod = relay.transform.InferType()(mod)
mutated_mod['func_10159'] = func_10159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10159_call = mutated_mod.get_global_var('func_10159')
call_10160 = func_10159_call()
output = call_10160
func_10161 = relay.Function([], output)
mutated_mod['func_10161'] = func_10161
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8050_call = mod.get_global_var('func_8050')
func_8052_call = mutated_mod.get_global_var('func_8052')
call_10229 = relay.TupleGetItem(func_8050_call(), 0)
call_10230 = relay.TupleGetItem(func_8052_call(), 0)
func_9910_call = mod.get_global_var('func_9910')
func_9911_call = mutated_mod.get_global_var('func_9911')
call_10242 = relay.TupleGetItem(func_9910_call(), 2)
call_10243 = relay.TupleGetItem(func_9911_call(), 2)
func_4319_call = mod.get_global_var('func_4319')
func_4324_call = mutated_mod.get_global_var('func_4324')
var_10268 = relay.var("var_10268", dtype = "float32", shape = (320,))#candidate|10268|(320,)|var|float32
var_10269 = relay.var("var_10269", dtype = "int16", shape = (825,))#candidate|10269|(825,)|var|int16
var_10270 = relay.var("var_10270", dtype = "float64", shape = (48,))#candidate|10270|(48,)|var|float64
call_10267 = relay.TupleGetItem(func_4319_call(relay.reshape(var_10268.astype('float32'), [320,]), relay.reshape(var_10269.astype('int16'), [5, 165]), relay.reshape(var_10270.astype('float64'), [1, 48]), ), 3)
call_10271 = relay.TupleGetItem(func_4324_call(relay.reshape(var_10268.astype('float32'), [320,]), relay.reshape(var_10269.astype('int16'), [5, 165]), relay.reshape(var_10270.astype('float64'), [1, 48]), ), 3)
func_7187_call = mod.get_global_var('func_7187')
func_7189_call = mutated_mod.get_global_var('func_7189')
call_10276 = relay.TupleGetItem(func_7187_call(relay.reshape(var_10270.astype('float64'), [12, 4])), 1)
call_10277 = relay.TupleGetItem(func_7189_call(relay.reshape(var_10270.astype('float64'), [12, 4])), 1)
func_4479_call = mod.get_global_var('func_4479')
func_4485_call = mutated_mod.get_global_var('func_4485')
var_10289 = relay.var("var_10289", dtype = "float32", shape = (448,))#candidate|10289|(448,)|var|float32
var_10290 = relay.var("var_10290", dtype = "float64", shape = (80,))#candidate|10290|(80,)|var|float64
const_10291 = relay.const([[-5,7,-5,2,9,-1,-5,2,-7,-2,4,-8,1,-2,4],[-7,-8,-4,-9,2,10,3,-2,9,-1,8,-3,8,10,6],[-5,-4,-9,-6,7,-8,-1,4,8,-3,-6,-8,7,10,5],[3,1,5,-6,-10,-10,1,1,-5,9,-10,10,2,4,-5],[2,-1,5,-4,-8,5,-5,9,10,-5,-1,3,-2,9,1],[-5,3,-7,-1,-1,-9,6,1,-10,-9,-1,9,-2,-1,7],[8,-6,-7,9,-7,-8,7,10,1,-8,-6,-1,-2,-6,-5],[-6,6,-3,-6,4,5,10,7,-9,-10,9,5,-1,-2,-10],[3,-1,8,3,-8,-7,-8,-6,-7,-5,3,4,-1,-7,-5],[1,2,8,-6,6,-7,-9,-2,-4,-2,-9,-1,7,2,-7],[10,7,-10,6,6,-9,6,10,5,-6,-2,-3,10,7,3]], dtype = "int16")#candidate|10291|(11, 15)|const|int16
call_10288 = relay.TupleGetItem(func_4479_call(relay.reshape(var_10289.astype('float32'), [14, 16, 2]), relay.reshape(var_10290.astype('float64'), [80,]), relay.reshape(call_10267.astype('int16'), [825,]), relay.reshape(const_10291.astype('int16'), [165,]), relay.reshape(var_10289.astype('float32'), [14, 16, 2]), ), 4)
call_10292 = relay.TupleGetItem(func_4485_call(relay.reshape(var_10289.astype('float32'), [14, 16, 2]), relay.reshape(var_10290.astype('float64'), [80,]), relay.reshape(call_10267.astype('int16'), [825,]), relay.reshape(const_10291.astype('int16'), [165,]), relay.reshape(var_10289.astype('float32'), [14, 16, 2]), ), 4)
uop_10302 = relay.log2(call_10267.astype('float32')) # shape=(5, 165)
uop_10304 = relay.log2(call_10271.astype('float32')) # shape=(5, 165)
output = relay.Tuple([call_10229,call_10242,var_10268,var_10269,var_10270,call_10276,call_10288,var_10289,var_10290,const_10291,uop_10302,])
output2 = relay.Tuple([call_10230,call_10243,var_10268,var_10269,var_10270,call_10277,call_10292,var_10289,var_10290,const_10291,uop_10304,])
func_10315 = relay.Function([var_10268,var_10269,var_10270,var_10289,var_10290,], output)
mod['func_10315'] = func_10315
mod = relay.transform.InferType()(mod)
var_10316 = relay.var("var_10316", dtype = "float32", shape = (320,))#candidate|10316|(320,)|var|float32
var_10317 = relay.var("var_10317", dtype = "int16", shape = (825,))#candidate|10317|(825,)|var|int16
var_10318 = relay.var("var_10318", dtype = "float64", shape = (48,))#candidate|10318|(48,)|var|float64
var_10319 = relay.var("var_10319", dtype = "float32", shape = (448,))#candidate|10319|(448,)|var|float32
var_10320 = relay.var("var_10320", dtype = "float64", shape = (80,))#candidate|10320|(80,)|var|float64
output = func_10315(var_10316,var_10317,var_10318,var_10319,var_10320,)
func_10321 = relay.Function([var_10316,var_10317,var_10318,var_10319,var_10320,], output)
mutated_mod['func_10321'] = func_10321
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10352 = relay.const([[[-3.672278,0.287743,4.564127,3.535766,2.524891,6.303781],[3.130083,0.576824,-2.832500,-5.751301,9.298601,4.634884],[-7.938646,-3.743461,3.577814,7.831473,5.808754,-0.023548],[-1.831819,0.872764,-8.616471,7.533726,-4.300075,-1.658641],[-8.919404,7.604879,2.476367,-2.936484,-0.203329,-0.604738],[-9.420151,0.453995,-4.933172,-1.738468,7.850547,-3.870213],[-1.488218,9.010548,-8.142358,0.500316,8.035532,-3.836990],[8.971585,-6.030513,3.807586,-6.691369,-7.861474,2.314585],[9.550037,-1.616979,-1.365614,4.185959,-1.601423,7.068058],[-5.474057,4.999274,2.037908,2.607125,-6.756662,-3.702570],[-2.079147,-0.970094,-2.703810,-0.776100,3.839795,1.012527],[1.907643,4.493293,1.113192,0.934314,4.339585,9.336805],[-9.521593,-4.709890,3.568326,5.133254,2.121498,-3.071898],[2.134077,6.831840,1.351030,-2.747853,7.624142,-4.405410],[-0.642952,5.470257,-5.454798,-9.440548,9.179827,-4.535091],[3.920092,-3.154278,5.035670,9.457732,7.055817,1.850740]]], dtype = "float32")#candidate|10352|(1, 16, 6)|const|float32
var_10353 = relay.var("var_10353", dtype = "float32", shape = (7, 16, 6))#candidate|10353|(7, 16, 6)|var|float32
bop_10354 = relay.add(const_10352.astype('float32'), var_10353.astype('float32')) # shape=(7, 16, 6)
func_10159_call = mod.get_global_var('func_10159')
func_10161_call = mutated_mod.get_global_var('func_10161')
call_10358 = func_10159_call()
call_10359 = func_10159_call()
func_8650_call = mod.get_global_var('func_8650')
func_8651_call = mutated_mod.get_global_var('func_8651')
call_10363 = func_8650_call()
call_10364 = func_8650_call()
uop_10365 = relay.erf(call_10358.astype('float64')) # shape=(1, 10, 10)
uop_10367 = relay.erf(call_10359.astype('float64')) # shape=(1, 10, 10)
output = relay.Tuple([bop_10354,call_10363,uop_10365,])
output2 = relay.Tuple([bop_10354,call_10364,uop_10367,])
func_10373 = relay.Function([var_10353,], output)
mod['func_10373'] = func_10373
mod = relay.transform.InferType()(mod)
mutated_mod['func_10373'] = func_10373
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10374 = relay.var("var_10374", dtype = "float32", shape = (7, 16, 6))#candidate|10374|(7, 16, 6)|var|float32
func_10373_call = mutated_mod.get_global_var('func_10373')
call_10375 = func_10373_call(var_10374)
output = call_10375
func_10376 = relay.Function([var_10374], output)
mutated_mod['func_10376'] = func_10376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9664_call = mod.get_global_var('func_9664')
func_9666_call = mutated_mod.get_global_var('func_9666')
call_10378 = relay.TupleGetItem(func_9664_call(), 0)
call_10379 = relay.TupleGetItem(func_9666_call(), 0)
func_8003_call = mod.get_global_var('func_8003')
func_8005_call = mutated_mod.get_global_var('func_8005')
call_10390 = relay.TupleGetItem(func_8003_call(), 1)
call_10391 = relay.TupleGetItem(func_8005_call(), 1)
uop_10393 = relay.cos(call_10390.astype('float32')) # shape=(300, 2)
uop_10395 = relay.cos(call_10391.astype('float32')) # shape=(300, 2)
func_1835_call = mod.get_global_var('func_1835')
func_1838_call = mutated_mod.get_global_var('func_1838')
var_10405 = relay.var("var_10405", dtype = "int16", shape = (165,))#candidate|10405|(165,)|var|int16
const_10406 = relay.const([[-4,-2,9],[-6,10,10],[6,-1,-8],[9,-4,5],[-9,-5,-2],[6,1,2],[3,2,7],[7,1,6],[-5,-9,-5],[-1,3,-7],[-10,-10,2],[2,8,-9],[7,8,-3],[7,-1,-7],[3,3,5],[-2,3,-7],[-3,-8,-2],[-6,2,6],[2,1,4],[-2,-5,2],[4,-8,-5],[4,3,-9],[-9,-5,10],[-6,7,-6],[5,-7,-2],[4,-2,-5],[-7,-2,-10],[-7,-5,2],[6,-8,5],[-5,3,-5],[-10,10,-1],[-8,3,9],[1,2,2],[1,-2,-4],[-4,-9,10],[1,3,3],[-8,10,-9],[5,-9,-5],[-3,-9,-7],[3,-2,10],[8,-4,-5],[-5,-8,-4],[-6,-8,-10],[-3,3,-9],[5,-4,6],[-10,7,3],[3,-5,-3],[-9,-10,5],[1,-2,-2],[-7,-2,-3],[-6,3,9],[5,6,-2],[-9,-9,9],[10,1,-6],[-2,9,7],[6,-7,9],[7,-7,-4],[-3,1,5],[-5,1,6],[9,2,5],[2,-3,8],[-4,-7,-7],[1,5,1],[1,4,2],[-1,9,-10],[3,4,10],[9,9,6],[-7,6,-8],[-4,5,-5],[10,-9,-9],[1,-3,-9],[9,9,-4],[-3,-2,4],[8,-1,6],[9,1,-4],[8,-2,2],[-6,-1,-6],[9,-5,8],[1,7,-8],[-9,8,-4],[-8,-10,5],[-4,-1,-5],[-10,-8,-3],[4,2,-7],[4,-7,4],[7,-6,-6],[6,-10,-5],[-6,9,-7],[10,-8,3],[-5,1,-9],[3,-9,-2],[-8,5,7],[-4,4,-9],[-6,4,-5],[9,-4,-2],[-5,1,-4],[1,1,-3],[-7,-5,10],[1,5,10],[-2,10,9],[-1,6,2],[-4,5,10],[-8,-7,-5],[-7,5,-4],[9,-5,-2],[-10,-3,-4],[8,8,5],[-3,5,6],[-7,8,2],[-8,-8,2],[9,4,10],[-5,-7,-4],[-2,-7,-9],[9,-3,-9],[-9,-8,9],[-6,3,8],[-7,4,7],[8,6,-8],[-8,10,-6],[-6,5,-1],[-7,-1,-8],[-4,4,-10],[-7,-4,-6],[10,1,-3],[1,3,7],[-10,-2,5],[-2,6,-8],[-8,-5,-1],[-7,4,3],[9,9,9],[8,10,-2],[2,5,-1],[2,-9,-4],[-9,9,2],[-3,7,-3],[-7,8,10],[4,4,-8],[2,4,1],[2,-10,-3],[5,3,7],[-8,6,-6],[6,8,1],[6,-10,-5],[-10,-10,7],[3,9,-4],[10,5,-10],[2,-10,7],[-10,5,3],[10,-6,-4],[-4,-7,-10],[1,4,8],[6,-1,4],[-10,-3,4],[-4,9,-3],[-6,-9,1],[-5,3,-10],[-5,-3,-5],[-6,-1,9],[-7,10,-4],[9,9,5],[9,-4,-9],[-5,1,1],[-5,10,-8],[-1,-9,-10],[-3,4,-9],[6,9,2],[4,-2,-5],[10,4,6],[-6,-6,10],[-1,7,7],[-4,-7,2],[-1,-9,1],[8,6,1],[3,-10,4],[6,-3,1],[-2,2,10],[-1,10,5],[-3,-1,4],[-2,-9,7],[2,-9,8],[-6,6,10],[-2,8,10],[-3,8,-2],[6,-3,-6],[-10,-6,5],[10,-6,1],[-4,-6,7],[10,9,-4],[4,6,-6],[-10,3,7],[1,1,-6],[3,7,6],[5,2,4],[4,-7,-5],[-5,1,-10],[9,-8,9],[5,5,3],[-6,7,-2],[-5,9,9],[4,9,-3],[4,10,-2],[-9,3,9],[-5,-4,-4],[-3,3,8],[8,-7,7],[-7,3,4],[-10,-4,-7],[9,-9,-6],[9,1,-3],[-5,3,9],[-5,-1,-8],[6,8,-1],[7,8,-2],[1,4,-3],[-3,6,-4],[3,3,-10],[9,-7,7],[3,-7,-10],[-5,-10,2],[-4,6,10],[6,9,-7],[10,-4,4],[-6,-5,-8],[-2,7,2],[7,-6,-5],[-3,2,-10],[-1,-7,-7],[10,10,6],[2,2,10],[-9,-9,2],[-3,-5,-6],[-4,-3,-4],[3,-4,9],[4,-6,1],[2,6,6],[5,10,-2],[5,5,-8],[8,5,8],[-2,7,9],[-5,-9,2],[9,-5,-7],[7,-7,-10],[1,8,-10],[2,-9,9],[7,8,-8],[-3,10,-8],[-9,9,-7],[-2,-6,4],[7,7,5],[3,-3,1],[-3,-6,4],[-10,-9,10],[-7,-4,-3],[9,6,-5],[2,-6,8],[4,-2,6],[6,-3,-6],[-3,-5,6],[-5,9,8],[4,-1,7],[-8,3,-5],[7,9,-8],[-3,8,6],[-10,-6,6],[-3,8,-1],[-3,5,-8],[-9,2,5],[10,1,-7],[-1,-1,6],[-5,-8,-10],[5,7,-1],[10,1,5],[6,-5,-5],[-5,1,-5],[5,-3,2]], dtype = "int16")#candidate|10406|(275, 3)|const|int16
call_10404 = relay.TupleGetItem(func_1835_call(relay.reshape(var_10405.astype('int16'), [15, 1, 11]), relay.reshape(const_10406.astype('int16'), [15, 5, 11]), ), 0)
call_10407 = relay.TupleGetItem(func_1838_call(relay.reshape(var_10405.astype('int16'), [15, 1, 11]), relay.reshape(const_10406.astype('int16'), [15, 5, 11]), ), 0)
bop_10415 = relay.logical_or(uop_10393.astype('bool'), relay.reshape(call_10390.astype('bool'), relay.shape_of(uop_10393))) # shape=(300, 2)
bop_10418 = relay.logical_or(uop_10395.astype('bool'), relay.reshape(call_10391.astype('bool'), relay.shape_of(uop_10395))) # shape=(300, 2)
uop_10426 = relay.asin(bop_10415.astype('float64')) # shape=(300, 2)
uop_10428 = relay.asin(bop_10418.astype('float64')) # shape=(300, 2)
output = relay.Tuple([call_10378,call_10404,var_10405,const_10406,uop_10426,])
output2 = relay.Tuple([call_10379,call_10407,var_10405,const_10406,uop_10428,])
func_10429 = relay.Function([var_10405,], output)
mod['func_10429'] = func_10429
mod = relay.transform.InferType()(mod)
mutated_mod['func_10429'] = func_10429
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10430 = relay.var("var_10430", dtype = "int16", shape = (165,))#candidate|10430|(165,)|var|int16
func_10429_call = mutated_mod.get_global_var('func_10429')
call_10431 = func_10429_call(var_10430)
output = call_10431
func_10432 = relay.Function([var_10430], output)
mutated_mod['func_10432'] = func_10432
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10043_call = mod.get_global_var('func_10043')
func_10044_call = mutated_mod.get_global_var('func_10044')
call_10453 = func_10043_call()
call_10454 = func_10043_call()
func_4522_call = mod.get_global_var('func_4522')
func_4524_call = mutated_mod.get_global_var('func_4524')
call_10464 = func_4522_call()
call_10465 = func_4522_call()
output = relay.Tuple([call_10453,call_10464,])
output2 = relay.Tuple([call_10454,call_10465,])
func_10473 = relay.Function([], output)
mod['func_10473'] = func_10473
mod = relay.transform.InferType()(mod)
mutated_mod['func_10473'] = func_10473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10473_call = mutated_mod.get_global_var('func_10473')
call_10474 = func_10473_call()
output = call_10474
func_10475 = relay.Function([], output)
mutated_mod['func_10475'] = func_10475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7257_call = mod.get_global_var('func_7257')
func_7259_call = mutated_mod.get_global_var('func_7259')
call_10483 = relay.TupleGetItem(func_7257_call(), 0)
call_10484 = relay.TupleGetItem(func_7259_call(), 0)
func_10373_call = mod.get_global_var('func_10373')
func_10376_call = mutated_mod.get_global_var('func_10376')
var_10492 = relay.var("var_10492", dtype = "float32", shape = (672,))#candidate|10492|(672,)|var|float32
call_10491 = relay.TupleGetItem(func_10373_call(relay.reshape(var_10492.astype('float32'), [7, 16, 6])), 0)
call_10493 = relay.TupleGetItem(func_10376_call(relay.reshape(var_10492.astype('float32'), [7, 16, 6])), 0)
func_5180_call = mod.get_global_var('func_5180')
func_5181_call = mutated_mod.get_global_var('func_5181')
call_10497 = relay.TupleGetItem(func_5180_call(), 0)
call_10498 = relay.TupleGetItem(func_5181_call(), 0)
output = relay.Tuple([call_10483,call_10491,var_10492,call_10497,])
output2 = relay.Tuple([call_10484,call_10493,var_10492,call_10498,])
func_10541 = relay.Function([var_10492,], output)
mod['func_10541'] = func_10541
mod = relay.transform.InferType()(mod)
mutated_mod['func_10541'] = func_10541
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10542 = relay.var("var_10542", dtype = "float32", shape = (672,))#candidate|10542|(672,)|var|float32
func_10541_call = mutated_mod.get_global_var('func_10541')
call_10543 = func_10541_call(var_10542)
output = call_10543
func_10544 = relay.Function([var_10542], output)
mutated_mod['func_10544'] = func_10544
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10546 = relay.var("var_10546", dtype = "uint16", shape = (15, 16, 5))#candidate|10546|(15, 16, 5)|var|uint16
var_10547 = relay.var("var_10547", dtype = "uint16", shape = (15, 16, 5))#candidate|10547|(15, 16, 5)|var|uint16
bop_10548 = relay.logical_xor(var_10546.astype('uint16'), relay.reshape(var_10547.astype('uint16'), relay.shape_of(var_10546))) # shape=(15, 16, 5)
output = relay.Tuple([bop_10548,])
output2 = relay.Tuple([bop_10548,])
func_10555 = relay.Function([var_10546,var_10547,], output)
mod['func_10555'] = func_10555
mod = relay.transform.InferType()(mod)
var_10556 = relay.var("var_10556", dtype = "uint16", shape = (15, 16, 5))#candidate|10556|(15, 16, 5)|var|uint16
var_10557 = relay.var("var_10557", dtype = "uint16", shape = (15, 16, 5))#candidate|10557|(15, 16, 5)|var|uint16
output = func_10555(var_10556,var_10557,)
func_10558 = relay.Function([var_10556,var_10557,], output)
mutated_mod['func_10558'] = func_10558
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10577 = relay.const([[[-9.958223,8.288614,-8.959013,-2.678460,6.459727,-9.184126,-3.197514,-8.902720,8.336449,7.160554,-8.590561,-2.191503,-8.196625,6.235936],[1.918782,9.763427,-4.209486,-8.140868,8.255528,6.166618,-7.756253,9.080756,7.222656,-0.434939,1.289904,-2.824076,0.373850,7.575579],[-7.776998,-2.461629,6.652416,9.730481,-8.062473,-4.107376,9.400281,9.621779,6.828314,-9.970694,-3.558963,-7.093470,-9.337085,1.601504],[6.924877,7.997189,4.181714,1.443356,1.427505,1.397572,2.806273,-5.172274,2.400704,-4.781112,-3.243129,8.636613,-8.101647,-2.737427],[-2.691173,-5.054358,-5.773325,-9.170486,-2.051324,-7.248854,-1.225525,2.381842,8.307833,-1.620117,5.721013,6.208506,-3.374493,-1.898136],[-6.615439,1.364573,3.918777,9.724556,-9.624037,4.649636,9.710624,-7.047490,9.372208,5.233091,1.203383,2.884431,4.414733,-5.020785],[8.314350,-2.078164,2.558231,5.428008,6.570438,-5.281193,-5.252700,-6.816268,8.737863,0.699328,1.983107,8.480113,0.667110,5.977632],[-9.516620,-8.771850,5.325838,9.751810,-2.229258,8.302912,5.334355,8.792127,1.856431,-3.012218,2.661958,-9.153754,-0.689716,3.980144],[-9.154914,-6.893306,7.711295,7.483960,8.731107,6.712987,8.850741,-2.641450,6.476780,-6.225830,8.512297,7.806551,-0.407624,0.139687]],[[-5.474221,-8.097343,-7.268891,9.361480,8.179802,-7.095701,3.438762,7.818674,-9.707662,-7.111231,8.475820,-3.354239,4.748545,0.995476],[6.856960,-1.214654,-4.415984,1.099261,-2.648369,-4.170861,1.924001,-2.639737,-0.252396,8.595420,3.218403,-4.440909,-2.023793,-5.807042],[3.895574,7.069171,-7.041737,-6.829842,5.893172,4.612348,-8.261719,5.945302,-1.208891,-3.021020,8.225532,3.364114,0.213355,-5.524328],[4.447403,6.459479,-6.370451,2.595511,5.673636,2.323950,8.945949,-6.563563,-2.184873,1.372461,8.577109,-2.253358,4.773764,-1.816452],[0.724259,-2.332352,9.890354,2.803756,6.385588,-6.540439,-5.027417,6.890893,5.505576,1.400968,3.384790,-1.315018,1.566238,-0.853527],[1.003723,8.066332,6.191023,6.466830,-5.981552,-1.785489,0.454634,-1.701060,0.271608,-2.409892,8.832654,-2.665620,-2.255194,1.237444],[6.556397,2.101037,-3.858497,-9.900132,-9.761685,-7.843252,-3.133263,-4.157122,-5.811871,-6.304796,-4.505508,-8.932672,-0.717168,3.653329],[0.324600,-5.018435,-1.775084,1.821324,7.506526,-7.034021,7.458804,-3.273554,6.920469,-3.112053,0.402503,3.019589,2.481182,5.758610],[1.972179,-4.635217,2.816630,5.183866,-3.203091,5.841957,-1.392106,-6.352911,-1.608775,-0.246123,2.153757,0.836071,6.886564,1.180865]],[[-9.288815,-8.011353,9.659903,6.020912,-6.772689,-8.007554,7.749030,-8.622653,7.899515,-0.112344,7.951610,3.885802,1.627283,1.482661],[-2.114232,6.154425,1.512359,-2.991839,-6.131552,4.041677,-0.597211,-6.997594,7.758919,-9.031966,1.064491,9.308460,9.665216,5.031565],[3.874505,3.206946,5.088118,2.339584,-5.614888,0.704575,3.894402,6.976334,-8.621430,1.972044,-4.767031,-8.856145,-5.785644,-3.627219],[3.448434,-0.769571,-7.212726,-7.326548,-6.603188,-6.478960,4.977382,-0.116462,1.837331,-6.676043,8.589232,1.810619,0.506152,4.785962],[5.235880,2.108018,3.454985,-3.514498,6.968965,-2.752479,-1.351273,3.110476,-4.538779,-2.380235,5.571074,-0.434797,-1.922404,2.373411],[0.743046,-8.151777,-4.863167,7.778366,3.342880,-4.616624,-8.392047,7.168054,4.505443,-9.578504,-5.087631,2.013492,-8.636461,-2.632892],[-4.407209,-5.972165,-8.026832,-7.603803,5.014080,-3.194388,8.838494,1.377445,2.969680,-5.054552,4.479359,6.921092,0.901362,-6.724328],[-5.466548,1.746442,-1.385997,-9.925663,-8.397855,6.183330,0.904963,-5.235715,-8.521203,-7.650135,-9.742482,1.951449,-2.329396,5.492901],[7.907957,3.969339,-3.154160,-5.309336,-4.172502,0.362716,-7.054949,-6.953429,0.364537,-3.753003,2.813278,6.007717,-8.589494,8.838901]],[[6.004100,-2.209561,-1.119334,-0.389553,-1.161776,7.450089,-9.903410,5.311539,-9.598053,-7.695000,4.292546,7.360668,7.388486,-2.463876],[1.818630,-4.262305,6.688089,-1.266417,-5.362859,-0.960603,8.604761,-0.875509,6.516033,-7.359611,3.316300,5.915044,-2.520625,1.932642],[4.167166,1.876400,-5.314532,-3.265339,-2.437441,5.314067,9.350603,-5.221597,-5.604807,-2.612056,-2.436828,7.793829,9.364214,-8.385430],[9.014304,-0.506108,-2.865448,-0.866062,2.910311,-2.662045,1.074310,5.879711,2.597272,2.431395,-6.770116,0.864771,0.535521,-1.624486],[1.953649,-6.366157,1.205223,-2.524305,-2.306700,-1.317736,9.450474,3.854800,-1.786686,6.761275,-8.272254,1.084234,5.945661,-2.071792],[2.605284,2.170431,5.911325,-1.640555,-6.575018,-4.641000,2.697652,2.402646,8.984914,0.070152,9.870620,-8.285350,4.352071,-3.068616],[-4.631182,8.588977,5.499149,5.569463,-1.716689,6.597605,-3.593708,4.204318,-2.478928,-3.717572,-6.115192,-9.801119,-0.506760,9.326569],[-7.007233,-2.616137,-7.405170,4.976987,8.245876,4.435670,-3.809647,-4.975757,-6.155557,-7.358981,-0.227071,9.967254,-5.247521,-0.180538],[-1.041905,-6.124475,4.708469,4.437170,8.809641,-9.820425,7.663472,-7.776715,-6.787886,-6.158050,6.271171,-9.762387,3.378184,-1.595583]],[[2.915992,3.626196,-2.982503,-7.479193,-0.084336,-7.517194,-8.548093,-9.797734,-6.728716,6.102660,-3.192476,6.108575,-5.383035,0.838375],[2.440445,7.373913,3.046181,-8.595794,4.989411,5.200239,2.131001,9.947997,-3.508795,8.193698,-6.915829,-1.559310,9.116886,-1.619772],[8.873179,4.045235,6.990213,8.297923,8.609872,0.510407,-5.465484,9.662399,-5.874927,-7.276526,-1.327067,7.610645,-7.619782,0.144355],[7.902093,-9.102670,-2.809115,-9.651880,-7.986860,-8.280503,7.188596,-9.653181,-6.686070,0.638403,-8.469171,-6.452118,-3.573713,-9.720872],[4.453360,-6.405936,0.575768,9.138399,-7.555661,-1.200696,3.248597,0.516671,-2.937021,-9.099462,5.770650,2.747633,9.842819,-4.574667],[4.659341,7.183293,3.551768,7.730538,-6.214340,-3.804027,-9.181312,3.440273,4.797167,5.878224,2.650562,-8.906153,3.031520,-8.656069],[3.158949,-2.421848,3.251069,9.508617,1.262945,-7.318975,7.944561,0.420370,0.292814,8.985245,6.796886,-6.527440,3.113046,4.624459],[-6.159485,0.784060,-5.672162,-4.356312,1.340428,-8.755037,-6.800922,-7.522645,4.413972,-2.995373,5.784439,3.999875,-4.542396,9.287544],[3.077236,-5.896009,-0.158360,7.979075,-5.571427,6.621873,-0.099576,-8.891119,-2.620500,-2.190425,-8.751082,-1.430881,2.730041,-7.343320]]], dtype = "float32")#candidate|10577|(5, 9, 14)|const|float32
uop_10578 = relay.rsqrt(const_10577.astype('float32')) # shape=(5, 9, 14)
func_6738_call = mod.get_global_var('func_6738')
func_6739_call = mutated_mod.get_global_var('func_6739')
call_10584 = func_6738_call()
call_10585 = func_6738_call()
output = relay.Tuple([uop_10578,call_10584,])
output2 = relay.Tuple([uop_10578,call_10585,])
func_10595 = relay.Function([], output)
mod['func_10595'] = func_10595
mod = relay.transform.InferType()(mod)
output = func_10595()
func_10596 = relay.Function([], output)
mutated_mod['func_10596'] = func_10596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9720_call = mod.get_global_var('func_9720')
func_9722_call = mutated_mod.get_global_var('func_9722')
call_10617 = relay.TupleGetItem(func_9720_call(), 0)
call_10618 = relay.TupleGetItem(func_9722_call(), 0)
func_6571_call = mod.get_global_var('func_6571')
func_6573_call = mutated_mod.get_global_var('func_6573')
call_10635 = func_6571_call()
call_10636 = func_6571_call()
func_8353_call = mod.get_global_var('func_8353')
func_8355_call = mutated_mod.get_global_var('func_8355')
call_10639 = relay.TupleGetItem(func_8353_call(), 0)
call_10640 = relay.TupleGetItem(func_8355_call(), 0)
output = relay.Tuple([call_10617,call_10635,call_10639,])
output2 = relay.Tuple([call_10618,call_10636,call_10640,])
func_10653 = relay.Function([], output)
mod['func_10653'] = func_10653
mod = relay.transform.InferType()(mod)
mutated_mod['func_10653'] = func_10653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10653_call = mutated_mod.get_global_var('func_10653')
call_10654 = func_10653_call()
output = call_10654
func_10655 = relay.Function([], output)
mutated_mod['func_10655'] = func_10655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9689_call = mod.get_global_var('func_9689')
func_9691_call = mutated_mod.get_global_var('func_9691')
call_10685 = func_9689_call()
call_10686 = func_9689_call()
func_9346_call = mod.get_global_var('func_9346')
func_9347_call = mutated_mod.get_global_var('func_9347')
call_10691 = relay.TupleGetItem(func_9346_call(), 0)
call_10692 = relay.TupleGetItem(func_9347_call(), 0)
output = relay.Tuple([call_10685,call_10691,])
output2 = relay.Tuple([call_10686,call_10692,])
func_10702 = relay.Function([], output)
mod['func_10702'] = func_10702
mod = relay.transform.InferType()(mod)
mutated_mod['func_10702'] = func_10702
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10702_call = mutated_mod.get_global_var('func_10702')
call_10703 = func_10702_call()
output = call_10703
func_10704 = relay.Function([], output)
mutated_mod['func_10704'] = func_10704
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10702_call = mod.get_global_var('func_10702')
func_10704_call = mutated_mod.get_global_var('func_10704')
call_10763 = relay.TupleGetItem(func_10702_call(), 0)
call_10764 = relay.TupleGetItem(func_10704_call(), 0)
func_32_call = mod.get_global_var('func_32')
func_35_call = mutated_mod.get_global_var('func_35')
var_10771 = relay.var("var_10771", dtype = "float64", shape = (48,))#candidate|10771|(48,)|var|float64
call_10770 = relay.TupleGetItem(func_32_call(relay.reshape(var_10771.astype('float64'), [2, 4, 6])), 0)
call_10772 = relay.TupleGetItem(func_35_call(relay.reshape(var_10771.astype('float64'), [2, 4, 6])), 0)
func_1835_call = mod.get_global_var('func_1835')
func_1838_call = mutated_mod.get_global_var('func_1838')
var_10783 = relay.var("var_10783", dtype = "int16", shape = (165,))#candidate|10783|(165,)|var|int16
var_10784 = relay.var("var_10784", dtype = "int16", shape = (825,))#candidate|10784|(825,)|var|int16
call_10782 = relay.TupleGetItem(func_1835_call(relay.reshape(var_10783.astype('int16'), [15, 1, 11]), relay.reshape(var_10784.astype('int16'), [15, 5, 11]), ), 0)
call_10785 = relay.TupleGetItem(func_1838_call(relay.reshape(var_10783.astype('int16'), [15, 1, 11]), relay.reshape(var_10784.astype('int16'), [15, 5, 11]), ), 0)
func_9844_call = mod.get_global_var('func_9844')
func_9845_call = mutated_mod.get_global_var('func_9845')
call_10803 = relay.TupleGetItem(func_9844_call(), 0)
call_10804 = relay.TupleGetItem(func_9845_call(), 0)
func_8175_call = mod.get_global_var('func_8175')
func_8179_call = mutated_mod.get_global_var('func_8179')
var_10814 = relay.var("var_10814", dtype = "float32", shape = (320,))#candidate|10814|(320,)|var|float32
call_10813 = relay.TupleGetItem(func_8175_call(relay.reshape(var_10814.astype('float32'), [320,]), relay.reshape(var_10783.astype('int16'), [165,]), relay.reshape(call_10782.astype('int16'), [15, 5, 11]), ), 3)
call_10815 = relay.TupleGetItem(func_8179_call(relay.reshape(var_10814.astype('float32'), [320,]), relay.reshape(var_10783.astype('int16'), [165,]), relay.reshape(call_10782.astype('int16'), [15, 5, 11]), ), 3)
func_7928_call = mod.get_global_var('func_7928')
func_7929_call = mutated_mod.get_global_var('func_7929')
call_10825 = func_7928_call()
call_10826 = func_7928_call()
var_10827 = relay.var("var_10827", dtype = "int16", shape = (825,))#candidate|10827|(825,)|var|int16
bop_10828 = relay.right_shift(var_10784.astype('int32'), relay.reshape(var_10827.astype('int32'), relay.shape_of(var_10784))) # shape=(825,)
func_4654_call = mod.get_global_var('func_4654')
func_4656_call = mutated_mod.get_global_var('func_4656')
call_10834 = func_4654_call()
call_10835 = func_4654_call()
func_7605_call = mod.get_global_var('func_7605')
func_7611_call = mutated_mod.get_global_var('func_7611')
var_10851 = relay.var("var_10851", dtype = "float64", shape = (8, 50))#candidate|10851|(8, 50)|var|float64
const_10852 = relay.const([-2,6,2,-8,4,7,-7,1,-7,7,2,1,-7,-7,8,-2,-4,2,8,-4,-2,-2,8,-10,6,-7,1,-6,-5,-3,8,3,-6,9,7,-6,-6,9,-4,9,8,8,-5,10,-7,5,2,9,-3,4,2,2,-8,2,-1,2,8,-3,-4,5,9,7,9,9,-4,3,-3,-4,7,-3,-6,10,-4,-8,-7,10,-4,7,-2,-5,-9,4,5,-3,3,-1,-10,4,-5,2,5,7,-8,-3,3,9,-8,6,-1,6,-6,3,-9,9,9,-5,3,4,-10,-2,-6,-5,-3,8,1,-6,-10,-4,-5,-10,-6,9,-10,-1,-1,-1,3,3,-8,-10,2,9,-6,-10,8,5,6,-3,6,-7,6,-8,-6,5,-2,7,4,6,7,-10,6,10,9,10,-7,6,5,-2,-3,-6,-5,-8,9,8,-2,2,6,-3,5,-2,-10,-8,2,-7,9,1,8,-3,-7,-4,1,-10,8,-2,7,-7,-6,-2,-5,5,-4,-7,10,-9,1,8,9,-9,-9,2,-8,-3,-6,-3,3,6,-6,10,-5,5,-4,7,8,2,8,-5,5,-1,10,5,-1,3,-5,7,1,7,-2,-9,-2,-10,-5,9,3,-4,-3,8,-1,5,-3,-8,-2,-2,-9,5,-3,4,-1,9,-2,-7,-3,8,6,-10,4,5,-10,2,-7,-3,-3,-8,9,-6,-4,3,-10,9,-4,4,6,-6,6,8,-5,6,9,2,-3,8], dtype = "uint64")#candidate|10852|(280,)|const|uint64
const_10853 = relay.const([3.826705,-1.880304,1.323871,8.849967,-2.059488,1.182697,8.818255,-4.530580,4.591404,-7.362463,-9.279026,-4.381693,3.806280,5.740434,6.444560,-2.501441,6.117649,6.247560,7.447603,-9.264921,6.538615,3.726414,9.029510,9.152699,9.893472,1.040574,-4.266363,-0.680499,4.845596,-0.480407,2.272960,8.521757,-3.971532,-1.997053,-6.169905,7.188964,-6.652063,-4.475242,-5.294078,-2.978787,4.976725,9.288984,-2.950165,-6.137692,-5.940273,-8.307881,9.352516,-5.229770,-4.323645,-8.924426,-9.122855,-3.782631,-9.800017,-2.098243,-2.379681,4.453717,-6.712155,0.900952,-0.754860,5.431567,7.659962,7.297462,9.472073,-0.918611,-1.589840,-7.057205,-3.384575,6.214738,8.072544,-0.935122,-8.716645,-0.790331,-5.214498,7.464840,7.458993,9.535847,-7.802175,4.894728,7.687493,0.861024,-1.669033,-9.975259,9.461426,-7.291851,8.136482,-0.800284,-5.314204,-2.909696,3.463324,7.538768,-7.735490,2.036463,1.004471,8.957906,-5.010788,-9.708474,-0.969604,7.722603,-2.246235,1.129874,-2.335467,-2.601412,-4.215004,-6.735084,-3.922406,-2.740805,-1.425276,-8.322108,-1.535682,-0.913974,-4.937425,-6.180422,5.619255,-4.761699,9.135688,0.152787,-2.494341,-8.018171,6.696175,-9.514233,-4.589714,-5.320458,-7.199540,8.267072,-9.579389,8.595253,-0.670212,-4.229063,2.870048,-2.671640,-2.233586,7.734669,1.366019,5.066165,-7.140122,-3.291182,-5.085649,9.753209,0.949240,4.527293,7.420108,8.231670,-0.475091,1.817442,-1.647006,-1.328019,-0.038634,8.043451,2.868706,-3.382595,-5.474009,6.522809,7.706113,5.176883,7.001783,0.722442,6.759203,-6.839811,-7.438332,-9.838281,8.464086,2.832868,-4.680205,9.790920,8.567186,7.747439,5.089794,-0.366507,7.140408,7.321641,-1.629732,4.261130,7.305286,-7.738835,-4.615754,9.219652,9.114259,6.721674,9.032493,-4.784078,-1.960797,3.789218,-5.871234,-6.742109,0.980180,-3.232354,-4.283392,-5.001001,2.902485,5.079933,1.983149,-2.941424,4.295884,-6.863160,-3.655865,4.516737,-7.809131,-1.918661,-3.666392,-6.228544,9.448919,-0.223781,4.824444,5.436472,0.027450,-6.829744,7.907034,7.096087,-0.925158,-5.548003,-4.348404,4.022276,-4.846746,4.780470,-5.813157,-0.064358,-3.524483,-6.104363,4.637709,3.667573,-7.575320,4.001599,-9.487077,7.863305,-8.922829,5.281093,3.673500,1.151802,4.157870,3.529372,8.274416,4.648088,-9.488980,8.314589,9.703718,-5.921807,-7.114882,-3.180546,-1.649197,0.864659,7.916370,-7.225524,8.954879,-8.017260,-0.035238,-8.816419,2.926893,-5.506312,3.768767,-0.649577,-7.093765,6.553854,-5.026989,6.459553,6.597016,-7.642438,0.456767,6.138691,-3.267761,6.842153,3.141122,-3.797808,6.851759,-2.278927,-8.666974,-5.029066,3.044494,9.776932,4.339973,4.939420,5.930342,9.956309,-0.497819,2.357666,-6.726134,1.687427,6.453621,-1.594305,-7.764323,3.034430,0.837135,6.415339,7.689832,8.467858,7.236867,6.393817,-4.374643,-6.642148,-6.243777,9.527400,-3.482856,-6.932708,3.923492,4.221331,-0.465247,-9.154872,-4.395622,-9.093362,9.128192,-1.663333,-6.289671,9.445597,-7.953346,1.055206,-4.199976,9.292821,-6.416312,-2.527447,-2.236357,6.646053,-4.174149,6.132880,-0.203856,7.846454,8.039479,-9.090985,8.952812,-3.671354,7.135825,-7.631097,-9.575819,3.169024,-7.747058,-3.777093,2.937623,5.844139,-7.881141,-4.195784,-4.841344,-6.286681,0.821827,-3.319864,-4.979028,-7.542973,-6.304678,5.728905,-0.008949,3.241747,-6.109701,1.968037,-8.126581,-2.304430,7.644024,9.862829,-4.815616,3.452353,-7.990335,-1.248854,-1.333048,6.690071,-6.602167,-1.942404,1.281877,7.762570,7.399278,7.083506,0.031562,-6.869444,-9.422658,-3.587868,7.460528,-8.765446,2.934387,1.647924,6.622032,3.693744,0.155900,-7.839797,2.751995,5.945708,-6.649711,-3.112059,-9.327678,4.906919,-0.056445,0.472059,8.550033,-3.633932,-0.357707,0.618496,-0.958431,1.738732,-1.628884,-0.797405,2.438201,-9.258194,-5.897410,9.736467,-9.807335,9.994857,0.054315,-1.377796,-7.392512,4.299721,-3.461586,-5.807347,0.756055,8.357621,6.930068,-8.834502,6.258229,-9.890149,6.439371,-2.037291,-7.131147,4.129744,-8.049091,1.496215,-4.462695,5.074940,7.832311,4.350701,-5.385843,-1.476013,-0.789208,-9.261553,0.909197,9.840029,5.767068,-3.856820,3.891589,2.639738,-1.661234,-6.040561,0.661557,7.887457,5.440999,-3.949914,8.247593,0.823559,4.830697,2.574386,-4.540543,8.406804,-7.025149,-5.186924,5.576371,3.197093,-3.623765,-5.012362,-5.832100,-2.295534,-4.945233,1.452702,8.973293,7.289223,-0.392209,4.718688], dtype = "float32")#candidate|10853|(448,)|const|float32
const_10854 = relay.const([[8.070149,-4.788790,-5.274743,-1.677232,2.957040,-5.830034,-6.371055,-7.505091,1.222008,-3.236082],[-1.445390,9.222019,-0.253300,-0.957564,0.582959,4.037252,7.747337,2.787970,-1.612566,-0.160944],[-2.079790,6.948897,-7.697480,-9.880952,1.010441,-0.949228,-4.723550,5.671014,1.591465,2.767723],[4.760690,9.684520,8.652017,-5.288244,4.494520,1.219835,-5.633839,-0.972552,-6.867690,-2.868331],[-5.381048,9.328653,-1.550024,8.179178,-0.538708,-3.901364,9.497288,-4.817510,4.107179,-7.049242],[-6.394763,-4.842103,-6.399430,5.898665,-7.155386,-8.921532,-2.821225,7.470918,-5.100217,-7.076512],[9.933596,1.336794,1.126824,5.996795,-0.432519,2.585786,4.762090,2.815605,-8.681763,-4.714522],[-9.603201,1.192234,-5.194561,-0.627254,1.462546,-9.495419,3.949696,9.577540,4.187286,4.198349],[-8.402060,-6.678921,1.362304,7.309134,-5.061044,-3.014013,-6.258221,-4.966404,-3.377994,-8.894323],[3.995305,-5.836872,-7.986772,3.214738,7.013820,3.920184,6.406117,4.756786,-6.107447,1.478925],[5.617534,2.074041,5.120094,-7.664692,-4.424116,-8.991054,9.070401,4.327590,-6.996760,-8.090983],[3.667329,-3.696563,0.878578,8.391567,-2.258706,5.090963,-5.331214,-3.213314,-9.565307,4.403688],[4.609779,-1.591774,6.525822,-3.538395,8.133522,4.100798,-5.709071,3.228255,0.857161,8.887945],[1.267725,1.240343,-6.746965,-8.224835,9.331135,6.620553,1.517506,9.737613,0.168169,-4.035107],[-1.674074,-5.960867,1.984978,9.576708,-8.537367,4.640540,6.927513,-3.343580,-9.591835,-1.066364],[-1.958556,-2.325309,2.093577,-2.448981,4.870470,2.043999,-3.722324,-6.291815,-6.130427,6.216449],[2.315720,-0.555566,3.974717,-3.163492,0.735054,4.054285,-8.926237,3.878774,-7.527877,4.839066],[4.182249,5.090654,-1.590405,7.612819,8.153027,1.471172,6.746751,7.844591,-1.748977,-2.013760],[-4.846972,-2.384150,3.347736,7.374869,2.902045,8.388698,6.093793,1.883719,4.515010,-3.731571],[8.157593,7.999753,-4.227941,7.075176,-4.995814,-6.811888,-0.171602,0.691566,5.056258,7.935343],[9.051700,7.970436,9.857619,-6.843751,6.707884,-4.156753,1.853403,-7.324767,-7.039483,-1.461476],[6.120124,-3.245240,8.901718,-6.242596,-6.652062,-6.069328,-0.630062,-3.194777,-1.853152,-9.630310],[-6.962167,-0.440714,-1.794720,9.390807,-5.503815,8.306879,-2.509064,6.173618,-7.155249,-8.169285],[1.702741,-9.546404,-6.051488,-4.322493,-0.112607,3.977052,9.341435,-5.818926,-5.226629,-5.441894],[2.094119,-4.550331,6.306919,-2.659573,9.524581,-3.556255,4.915928,5.542527,-2.747661,-0.875635],[-4.216074,7.835601,5.610040,-4.892685,4.963638,-9.122548,-7.178448,-7.243773,8.373274,6.176785],[-6.218810,2.983951,7.576407,9.505430,-9.792325,-3.445718,3.422607,-4.116984,2.379780,-8.947788],[-3.701586,9.318521,-6.738941,-4.783441,-3.064880,-9.080727,-9.135573,-6.085377,-4.779199,5.874216],[9.753338,-8.790816,9.117312,4.092546,3.575119,6.188625,2.881032,-0.309898,-2.706065,1.162371],[1.129163,8.742968,2.408775,7.061318,-2.244147,1.273416,-1.876282,-5.643035,-4.574700,-6.328976],[-0.475187,6.486474,-9.873578,0.092569,4.198593,-2.317788,-4.613589,-7.284434,0.429056,-6.968711],[-9.197169,-3.624579,5.710486,-5.950556,-2.572172,0.334616,-4.951523,-5.577240,-1.834996,5.922231],[-7.259346,-3.435230,-6.253208,2.752852,-9.577221,1.027002,6.975103,3.544668,-6.303105,-8.924069],[-9.185239,2.624978,4.451214,-2.698544,9.135367,1.847751,9.780872,2.101305,-0.844915,8.187883],[-8.610485,0.650158,-5.416891,-2.141669,-4.197646,-0.419557,-7.513439,3.595772,3.584175,4.139833],[2.360991,1.072076,7.675159,-3.357359,6.321902,-3.537277,-6.355492,5.508205,1.797925,-8.909436],[-0.955676,-9.289247,-7.612518,-9.546707,6.334126,4.411219,-1.674081,4.688673,8.017319,4.361451],[-4.927913,-1.240975,7.372028,4.477423,2.455512,-7.521787,-8.221851,-8.929891,-1.706037,8.975019],[-6.244918,7.025335,9.405619,-0.517401,-9.942663,7.398020,-0.503849,-3.029405,4.846209,-7.865044],[7.421665,-1.361594,6.606130,-2.220624,-3.361048,-2.727995,-2.149096,8.696746,-0.864728,-2.232075],[-9.767918,8.255018,9.807947,-5.793412,-5.689278,2.127621,-4.682751,9.657900,-1.734920,4.295927],[8.254619,-6.526732,9.920275,7.154397,7.506323,4.034423,2.460596,-9.633910,-5.888938,4.860713],[2.385711,-5.760949,0.489059,-5.263571,5.415345,-3.692462,7.810363,3.618728,-8.866569,-8.386394],[-0.620291,4.851814,6.870489,1.840988,9.933939,-4.124847,6.863818,-2.143573,-6.278993,9.035730],[-2.893252,5.305718,-4.479251,6.050303,5.059210,-4.994830,8.006187,-4.853612,-8.667865,-2.023462],[-2.890209,-2.635566,7.973866,-7.709943,4.070883,8.401455,4.268216,8.381012,1.855567,7.210675],[7.111799,0.909886,4.451344,0.530234,6.332738,8.565946,-9.144216,8.058542,-8.189891,1.627962],[4.939278,-1.036583,6.973680,-6.172913,-3.291105,-1.929840,-9.371346,-5.762168,5.733594,4.423848],[5.894247,-9.699041,-9.570550,9.351231,-0.775111,0.394348,3.201905,-5.494050,3.371544,-9.882469],[-2.512670,0.030478,-6.277565,0.021661,0.549252,-2.898676,0.008710,-4.754109,-1.922378,9.285417],[1.612050,6.997949,-4.591473,3.966075,-8.377677,5.976736,-7.925562,5.482719,-8.797713,-8.126810],[2.972100,-5.606424,-8.694203,8.565040,-9.264972,6.616907,5.755956,-8.143479,-5.094684,3.465519],[2.749907,-9.793513,-6.657058,-6.498368,-4.741102,-8.002900,8.760120,-6.682420,-4.155306,3.905214],[-0.046620,-8.546922,9.438310,1.009293,-0.126535,-6.372545,0.323289,-9.485670,3.826131,-0.909622],[7.214335,6.265741,8.060704,-6.198128,2.885551,-3.435203,-6.038781,9.699150,-3.923244,-5.094279],[-4.077052,-8.686542,1.159762,6.027945,-3.949317,-8.126836,-6.410246,-0.716714,4.959610,2.004009],[-6.109434,5.385489,-3.832246,-8.451677,3.029580,-8.483524,-6.651229,-9.056881,9.766289,-0.556985],[1.250720,3.524389,-7.864283,-3.948801,7.783794,6.327835,7.448792,-3.647561,7.251896,-7.843678],[0.995619,-0.695945,-1.466753,8.109107,-5.524879,5.724730,-4.050012,-7.093841,-8.786918,0.476285],[-6.508465,-7.896558,2.636847,-0.435463,9.279917,1.672312,3.138925,-6.391805,-2.684779,4.148145]], dtype = "float64")#candidate|10854|(60, 10)|const|float64
call_10850 = relay.TupleGetItem(func_7605_call(relay.reshape(var_10851.astype('float64'), [400,]), relay.reshape(const_10852.astype('uint64'), [280,]), relay.reshape(const_10853.astype('float32'), [448, 1]), relay.reshape(const_10854.astype('float64'), [600,]), ), 3)
call_10855 = relay.TupleGetItem(func_7611_call(relay.reshape(var_10851.astype('float64'), [400,]), relay.reshape(const_10852.astype('uint64'), [280,]), relay.reshape(const_10853.astype('float32'), [448, 1]), relay.reshape(const_10854.astype('float64'), [600,]), ), 3)
output = relay.Tuple([call_10763,call_10770,var_10771,call_10782,var_10783,call_10803,call_10813,var_10814,call_10825,bop_10828,call_10834,call_10850,var_10851,const_10852,const_10853,const_10854,])
output2 = relay.Tuple([call_10764,call_10772,var_10771,call_10785,var_10783,call_10804,call_10815,var_10814,call_10826,bop_10828,call_10835,call_10855,var_10851,const_10852,const_10853,const_10854,])
func_10858 = relay.Function([var_10771,var_10783,var_10784,var_10814,var_10827,var_10851,], output)
mod['func_10858'] = func_10858
mod = relay.transform.InferType()(mod)
mutated_mod['func_10858'] = func_10858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10858_call = mutated_mod.get_global_var('func_10858')
var_10860 = relay.var("var_10860", dtype = "float64", shape = (48,))#candidate|10860|(48,)|var|float64
var_10861 = relay.var("var_10861", dtype = "int16", shape = (165,))#candidate|10861|(165,)|var|int16
var_10862 = relay.var("var_10862", dtype = "int16", shape = (825,))#candidate|10862|(825,)|var|int16
var_10863 = relay.var("var_10863", dtype = "float32", shape = (320,))#candidate|10863|(320,)|var|float32
var_10864 = relay.var("var_10864", dtype = "int16", shape = (825,))#candidate|10864|(825,)|var|int16
var_10865 = relay.var("var_10865", dtype = "float64", shape = (8, 50))#candidate|10865|(8, 50)|var|float64
call_10859 = func_10858_call(var_10860,var_10861,var_10862,var_10863,var_10864,var_10865,)
output = call_10859
func_10866 = relay.Function([var_10860,var_10861,var_10862,var_10863,var_10864,var_10865,], output)
mutated_mod['func_10866'] = func_10866
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9275_call = mod.get_global_var('func_9275')
func_9276_call = mutated_mod.get_global_var('func_9276')
call_10908 = relay.TupleGetItem(func_9275_call(), 0)
call_10909 = relay.TupleGetItem(func_9276_call(), 0)
var_10918 = relay.var("var_10918", dtype = "float64", shape = (13, 10, 10))#candidate|10918|(13, 10, 10)|var|float64
bop_10919 = relay.subtract(call_10908.astype('uint64'), var_10918.astype('uint64')) # shape=(13, 10, 10)
bop_10922 = relay.subtract(call_10909.astype('uint64'), var_10918.astype('uint64')) # shape=(13, 10, 10)
func_7727_call = mod.get_global_var('func_7727')
func_7728_call = mutated_mod.get_global_var('func_7728')
call_10925 = func_7727_call()
call_10926 = func_7727_call()
var_10928 = relay.var("var_10928", dtype = "float64", shape = (15, 10, 10))#candidate|10928|(15, 10, 10)|var|float64
bop_10929 = relay.floor_mod(call_10908.astype('float32'), var_10928.astype('float32')) # shape=(15, 10, 10)
bop_10932 = relay.floor_mod(call_10909.astype('float32'), var_10928.astype('float32')) # shape=(15, 10, 10)
bop_10946 = relay.logical_or(var_10928.astype('bool'), call_10925.astype('bool')) # shape=(15, 10, 10)
bop_10949 = relay.logical_or(var_10928.astype('bool'), call_10926.astype('bool')) # shape=(15, 10, 10)
bop_10967 = relay.subtract(call_10925.astype('uint32'), var_10928.astype('uint32')) # shape=(15, 10, 10)
bop_10970 = relay.subtract(call_10926.astype('uint32'), var_10928.astype('uint32')) # shape=(15, 10, 10)
output = relay.Tuple([bop_10919,bop_10929,bop_10946,bop_10967,])
output2 = relay.Tuple([bop_10922,bop_10932,bop_10949,bop_10970,])
func_10978 = relay.Function([var_10918,var_10928,], output)
mod['func_10978'] = func_10978
mod = relay.transform.InferType()(mod)
var_10979 = relay.var("var_10979", dtype = "float64", shape = (13, 10, 10))#candidate|10979|(13, 10, 10)|var|float64
var_10980 = relay.var("var_10980", dtype = "float64", shape = (15, 10, 10))#candidate|10980|(15, 10, 10)|var|float64
output = func_10978(var_10979,var_10980,)
func_10981 = relay.Function([var_10979,var_10980,], output)
mutated_mod['func_10981'] = func_10981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9321_call = mod.get_global_var('func_9321')
func_9323_call = mutated_mod.get_global_var('func_9323')
call_10997 = relay.TupleGetItem(func_9321_call(), 1)
call_10998 = relay.TupleGetItem(func_9323_call(), 1)
func_5180_call = mod.get_global_var('func_5180')
func_5181_call = mutated_mod.get_global_var('func_5181')
call_11001 = relay.TupleGetItem(func_5180_call(), 0)
call_11002 = relay.TupleGetItem(func_5181_call(), 0)
func_2680_call = mod.get_global_var('func_2680')
func_2685_call = mutated_mod.get_global_var('func_2685')
const_11023 = relay.const([-5.772058,-6.522188,-0.713828,7.693208,5.749495,5.440858,8.894331,3.168599,-5.320800,8.601484,3.795463,-0.643907,5.761231,7.174539,7.762713,4.636022,3.945845,-1.929446,3.790715,-9.769132,1.599344,3.908051,4.857233,2.665340,9.000469,-5.176067,-5.674494,3.488674,4.034705,-6.707791,-0.124987,-8.309159,8.499279,8.440368,-2.839530,-4.684625,1.836026,-3.726042,-3.597142,1.822423,6.764645,-3.644988,-6.480931,6.460886,0.480392,-9.594442,7.788115,1.438235,-5.959654,3.596083,-6.084342,-9.055234,1.814512,-4.981455,-3.057463,1.341706,-6.203183,5.223896,-9.350578,-8.643026,0.049512,0.719937,2.042086,7.883036,6.136196,1.856703,-5.912812,-7.438376,-5.383007,-7.758719,-7.090999,-6.294067,0.664479,7.766187,-2.911003,1.443185,3.581175,-4.586674,-8.674913,-7.611383], dtype = "float32")#candidate|11023|(80,)|const|float32
var_11024 = relay.var("var_11024", dtype = "int16", shape = (825,))#candidate|11024|(825,)|var|int16
const_11025 = relay.const([8.906678,-4.316850,8.728189,-1.222935,-7.219705,-3.197908,8.113287,-4.665678,-7.546714,9.392233,6.054298,4.076409,9.057897,-1.240051,-7.892565,2.129074,6.621706,6.724675,-3.816309,-0.987766,6.693861,-7.732211,-2.157064,3.760782,0.462924,7.125792,-5.465822,1.482081,-0.304088,-0.377904,4.606784,-3.365382,5.127685,6.480474,7.123132,0.270168,2.429843,1.114930,-6.817967,-9.374647,4.410611,-2.753711,-7.363569,-6.390489,-7.482869,0.501449,-0.214120,-2.438097], dtype = "float64")#candidate|11025|(48,)|const|float64
call_11022 = relay.TupleGetItem(func_2680_call(relay.reshape(const_11023.astype('float32'), [1, 8, 10]), relay.reshape(var_11024.astype('int16'), [5, 165]), relay.reshape(const_11025.astype('float64'), [48,]), ), 4)
call_11026 = relay.TupleGetItem(func_2685_call(relay.reshape(const_11023.astype('float32'), [1, 8, 10]), relay.reshape(var_11024.astype('int16'), [5, 165]), relay.reshape(const_11025.astype('float64'), [48,]), ), 4)
func_7346_call = mod.get_global_var('func_7346')
func_7348_call = mutated_mod.get_global_var('func_7348')
call_11028 = func_7346_call()
call_11029 = func_7346_call()
output = relay.Tuple([call_10997,call_11001,call_11022,const_11023,var_11024,const_11025,call_11028,])
output2 = relay.Tuple([call_10998,call_11002,call_11026,const_11023,var_11024,const_11025,call_11029,])
func_11039 = relay.Function([var_11024,], output)
mod['func_11039'] = func_11039
mod = relay.transform.InferType()(mod)
var_11040 = relay.var("var_11040", dtype = "int16", shape = (825,))#candidate|11040|(825,)|var|int16
output = func_11039(var_11040)
func_11041 = relay.Function([var_11040], output)
mutated_mod['func_11041'] = func_11041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9511_call = mod.get_global_var('func_9511')
func_9512_call = mutated_mod.get_global_var('func_9512')
call_11119 = relay.TupleGetItem(func_9511_call(), 0)
call_11120 = relay.TupleGetItem(func_9512_call(), 0)
var_11124 = relay.var("var_11124", dtype = "float64", shape = (6, 10, 10))#candidate|11124|(6, 10, 10)|var|float64
bop_11125 = relay.multiply(call_11119.astype('int64'), var_11124.astype('int64')) # shape=(6, 10, 10)
bop_11128 = relay.multiply(call_11120.astype('int64'), var_11124.astype('int64')) # shape=(6, 10, 10)
func_6479_call = mod.get_global_var('func_6479')
func_6482_call = mutated_mod.get_global_var('func_6482')
const_11139 = relay.const([-4.856012,-6.692894,-4.220471,-8.316239,3.759676,4.766396,-8.186488,7.175210,-3.419712,8.864399,1.104639,-5.982083,5.579342,-2.230354,-6.138441,4.686378,-2.253014,1.253935,-3.618130,0.261557,-6.441405,-2.506352,3.471047,7.440399,-5.650669,-2.289742,6.197462,3.866758,-3.887127,-5.446121,9.962821,-2.178161,9.493483,-7.610915,1.855074,9.153527,-6.408180,-4.457502,8.261715,3.759998,1.605165,9.328799,5.660982,1.220951,-4.940696,-2.708466,-9.656341,4.231095,-3.776048,3.413466,2.821651,7.977951,1.825418,-2.111294,2.144375,-3.827638,9.690511,-9.144068,2.111529,3.582456,9.275652,3.587724,-2.357203,0.238848,-2.562230,-0.017688,3.148873,3.706878,-2.180219,-9.155974,4.507767,-3.891825,-5.950164,1.855444,-7.487377,-2.291094,-1.369900,8.664015,-4.516680,2.715433,-0.632380,2.763185,0.244172,-9.868189,-7.289291,-0.737056,3.253830,-2.659205,6.715658,0.982699,-8.025181,4.289687,5.290102,8.059878,8.351337,-4.741834,4.906954,4.315002,-4.556394,-4.101297,-3.616905,5.102072,7.918565,-6.188665,8.820410,-8.583209,9.826825,5.679224,5.640644,-6.299379,3.819437,-5.891765,-8.693635,-9.102781,0.554755,7.477044,5.805227,7.971706,7.765748,4.550633,-3.794762,-6.672178,7.964288,-2.494440,6.623615,4.582195,-3.459208,9.975740,8.367165,1.948281,-5.118452,2.089577,2.025876,-2.347633,-0.497660,-7.046362,8.681600,-9.070105,-0.490837,2.499972,7.216794,-4.669971,-3.901792,5.568946,3.717237,-7.162118,9.576240,5.705220,9.354573,5.956732,6.152234,-7.385044,5.578792,9.173676,4.475518,4.700202,3.928769,-0.092922,7.102828,-0.736465,0.883768,-4.477637,-9.868593,1.327350,0.453208,1.382543,-4.704246,2.132415,-8.622080,7.254278,-1.049219,-7.283219,7.103881,3.766890,-7.841283,2.427909,1.488301,6.555462,-0.212231,8.950205,4.507286,-8.728651,-2.659430,8.572057,7.782585,-8.022555,2.344280,0.084343,-1.491152,5.846692,-0.434760,-7.912022,-7.849992,2.253496,-5.630980,-8.888952,0.129747,-5.123633,2.773138,-4.925739,-7.728232,-7.923977,-8.036615,-1.245835,-8.119277,9.645730,7.378118,-4.261983,6.541270,-5.226299,-5.325006,-7.259995,1.721433,9.649129,-4.375179,4.368932,0.842274,3.393972,-5.714773,-1.036541,0.235559,5.785444,8.760688,1.719340,-1.658199,-6.002612,-9.688439,-4.747563,6.473524,-0.712115,-6.948927,2.060834,0.191112,8.456427,-3.863374,5.300631,3.735854,-5.134767,-0.673079,-1.237756,9.228841,-6.725992,5.764260,-9.481175,-0.334832,-4.354751,-7.882697,-7.621735,-5.177616,5.312158,1.892554,3.314432,-8.721435,5.883363,6.834251,9.340581,9.089738,-5.163329,-4.403781,1.007699,-6.096006,1.212505,0.063225,-1.132917,7.155814,0.951856,-9.825633,-2.946169,-7.032620,-1.726646,5.618378,7.231739,3.596968,3.366593,-1.458119,-6.324809,-2.513044,2.488224,-6.788096,-7.577126,-4.267440,-0.957656,-3.479305,5.844793,4.272311,-0.682460,3.486576,0.829267,7.786074,-4.020975,1.456051,-5.068124,6.429002,-4.350868,-5.733967,4.765948,-1.473416,2.203758,-9.408517,1.901531,-1.953757,-5.195084,3.477049,-6.854633,-0.588165,-1.088704,-3.451967,-9.591098,6.873003,2.753820,3.729522,-8.406051,-5.753892,-6.186045,-3.959989,-7.150875,8.600067,-3.806993,-4.845359,3.922940,7.459261,5.274605,7.688170,8.131657,-6.797421,-5.136161,-3.010510,5.213634,-0.910659,2.844186,3.661272,-1.629518,3.744660,-6.581034,8.831787,-3.281236,0.242626,-8.643607,0.940586,6.840477,-4.863413,0.140209,-6.159996,-8.925724,-5.857819,6.709107,3.640757,-5.780383,-8.246306,0.694439,6.878184,8.236120,8.327214,1.764258,5.052476,-1.836501,-6.767505,-9.762772,-2.725593,3.995789,2.063201,-7.923412,-7.774289,6.866686,5.633743,6.742530,-7.286285,-2.419994,-1.636157,6.212637,-0.636515,-2.229177,7.510707,-5.505836,9.385078,5.608015,-1.411109,3.233394,-5.878128,-1.536108,2.563426,-8.817943,-0.179045,7.295073,-2.581332,-1.686423,-5.865632,8.480012,-6.886226,8.019537,-9.936010,-3.059419,1.134826,3.418797,-1.375900,5.465386,4.210472,5.076981,-1.077087,6.151417], dtype = "float64")#candidate|11139|(400,)|const|float64
call_11138 = relay.TupleGetItem(func_6479_call(relay.reshape(const_11139.astype('float64'), [4, 10, 10])), 0)
call_11140 = relay.TupleGetItem(func_6482_call(relay.reshape(const_11139.astype('float64'), [4, 10, 10])), 0)
output = relay.Tuple([bop_11125,call_11138,const_11139,])
output2 = relay.Tuple([bop_11128,call_11140,const_11139,])
func_11146 = relay.Function([var_11124,], output)
mod['func_11146'] = func_11146
mod = relay.transform.InferType()(mod)
mutated_mod['func_11146'] = func_11146
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11147 = relay.var("var_11147", dtype = "float64", shape = (6, 10, 10))#candidate|11147|(6, 10, 10)|var|float64
func_11146_call = mutated_mod.get_global_var('func_11146')
call_11148 = func_11146_call(var_11147)
output = call_11148
func_11149 = relay.Function([var_11147], output)
mutated_mod['func_11149'] = func_11149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6738_call = mod.get_global_var('func_6738')
func_6739_call = mutated_mod.get_global_var('func_6739')
call_11242 = func_6738_call()
call_11243 = func_6738_call()
func_8883_call = mod.get_global_var('func_8883')
func_8885_call = mutated_mod.get_global_var('func_8885')
call_11251 = relay.TupleGetItem(func_8883_call(), 0)
call_11252 = relay.TupleGetItem(func_8885_call(), 0)
output = relay.Tuple([call_11242,call_11251,])
output2 = relay.Tuple([call_11243,call_11252,])
func_11253 = relay.Function([], output)
mod['func_11253'] = func_11253
mod = relay.transform.InferType()(mod)
output = func_11253()
func_11254 = relay.Function([], output)
mutated_mod['func_11254'] = func_11254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5577_call = mod.get_global_var('func_5577')
func_5579_call = mutated_mod.get_global_var('func_5579')
call_11297 = func_5577_call()
call_11298 = func_5577_call()
output = call_11297
output2 = call_11298
func_11309 = relay.Function([], output)
mod['func_11309'] = func_11309
mod = relay.transform.InferType()(mod)
mutated_mod['func_11309'] = func_11309
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11309_call = mutated_mod.get_global_var('func_11309')
call_11310 = func_11309_call()
output = call_11310
func_11311 = relay.Function([], output)
mutated_mod['func_11311'] = func_11311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5544_call = mod.get_global_var('func_5544')
func_5546_call = mutated_mod.get_global_var('func_5546')
call_11399 = func_5544_call()
call_11400 = func_5544_call()
output = call_11399
output2 = call_11400
func_11410 = relay.Function([], output)
mod['func_11410'] = func_11410
mod = relay.transform.InferType()(mod)
output = func_11410()
func_11411 = relay.Function([], output)
mutated_mod['func_11411'] = func_11411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6596_call = mod.get_global_var('func_6596')
func_6597_call = mutated_mod.get_global_var('func_6597')
call_11504 = relay.TupleGetItem(func_6596_call(), 1)
call_11505 = relay.TupleGetItem(func_6597_call(), 1)
output = relay.Tuple([call_11504,])
output2 = relay.Tuple([call_11505,])
func_11506 = relay.Function([], output)
mod['func_11506'] = func_11506
mod = relay.transform.InferType()(mod)
mutated_mod['func_11506'] = func_11506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11506_call = mutated_mod.get_global_var('func_11506')
call_11507 = func_11506_call()
output = call_11507
func_11508 = relay.Function([], output)
mutated_mod['func_11508'] = func_11508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7928_call = mod.get_global_var('func_7928')
func_7929_call = mutated_mod.get_global_var('func_7929')
call_11553 = func_7928_call()
call_11554 = func_7928_call()
func_7346_call = mod.get_global_var('func_7346')
func_7348_call = mutated_mod.get_global_var('func_7348')
call_11555 = func_7346_call()
call_11556 = func_7346_call()
output = relay.Tuple([call_11553,call_11555,])
output2 = relay.Tuple([call_11554,call_11556,])
func_11558 = relay.Function([], output)
mod['func_11558'] = func_11558
mod = relay.transform.InferType()(mod)
output = func_11558()
func_11559 = relay.Function([], output)
mutated_mod['func_11559'] = func_11559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8883_call = mod.get_global_var('func_8883')
func_8885_call = mutated_mod.get_global_var('func_8885')
call_11661 = relay.TupleGetItem(func_8883_call(), 0)
call_11662 = relay.TupleGetItem(func_8885_call(), 0)
output = relay.Tuple([call_11661,])
output2 = relay.Tuple([call_11662,])
func_11670 = relay.Function([], output)
mod['func_11670'] = func_11670
mod = relay.transform.InferType()(mod)
mutated_mod['func_11670'] = func_11670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11670_call = mutated_mod.get_global_var('func_11670')
call_11671 = func_11670_call()
output = call_11671
func_11672 = relay.Function([], output)
mutated_mod['func_11672'] = func_11672
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9321_call = mod.get_global_var('func_9321')
func_9323_call = mutated_mod.get_global_var('func_9323')
call_11763 = relay.TupleGetItem(func_9321_call(), 1)
call_11764 = relay.TupleGetItem(func_9323_call(), 1)
func_5559_call = mod.get_global_var('func_5559')
func_5561_call = mutated_mod.get_global_var('func_5561')
call_11765 = relay.TupleGetItem(func_5559_call(), 0)
call_11766 = relay.TupleGetItem(func_5561_call(), 0)
func_7659_call = mod.get_global_var('func_7659')
func_7661_call = mutated_mod.get_global_var('func_7661')
call_11800 = relay.TupleGetItem(func_7659_call(), 0)
call_11801 = relay.TupleGetItem(func_7661_call(), 0)
func_1835_call = mod.get_global_var('func_1835')
func_1838_call = mutated_mod.get_global_var('func_1838')
var_11805 = relay.var("var_11805", dtype = "int16", shape = (1, 165))#candidate|11805|(1, 165)|var|int16
var_11806 = relay.var("var_11806", dtype = "int16", shape = (825,))#candidate|11806|(825,)|var|int16
call_11804 = relay.TupleGetItem(func_1835_call(relay.reshape(var_11805.astype('int16'), [15, 1, 11]), relay.reshape(var_11806.astype('int16'), [15, 5, 11]), ), 0)
call_11807 = relay.TupleGetItem(func_1838_call(relay.reshape(var_11805.astype('int16'), [15, 1, 11]), relay.reshape(var_11806.astype('int16'), [15, 5, 11]), ), 0)
func_5468_call = mod.get_global_var('func_5468')
func_5471_call = mutated_mod.get_global_var('func_5471')
const_11811 = relay.const([-3.289796,7.898127,8.882579,-0.698987,-3.000804,6.087136,8.611500,8.921981,-6.987413,6.237753,5.254609,7.544654,-9.152489,8.114464,2.385676,1.498840,1.297994,-5.905540,-6.026316,0.628087,2.143212,4.154072,9.870632,-4.946313,-7.626156,4.763789,-0.346587,-6.272974,9.439724,7.667569,-7.929974,-0.206058,5.862079,7.656571,8.316779,-5.642447,5.914464,2.645283,-4.136299,5.422738,3.240179,-7.940451,9.890351,-7.494102,-7.593980,8.183571,-3.853315,9.555433,-0.559192,6.092944,1.114468,0.567033,-1.808736,5.345900,-1.753244,0.453307,8.381203,7.217759,3.628205,6.368013,3.605864,-8.532048,-0.785860,7.478861,-7.037336,-5.800303,-7.834167,7.482608,-0.221714,2.626719,7.897716,-0.575795,-6.749579,1.160785,6.614203,-3.109684,-0.232369,-7.036335,-0.687420,2.207481], dtype = "float64")#candidate|11811|(80,)|const|float64
call_11810 = relay.TupleGetItem(func_5468_call(relay.reshape(const_11811.astype('float64'), [80,]), relay.reshape(var_11806.astype('int16'), [825,]), ), 3)
call_11812 = relay.TupleGetItem(func_5471_call(relay.reshape(const_11811.astype('float64'), [80,]), relay.reshape(var_11806.astype('int16'), [825,]), ), 3)
output = relay.Tuple([call_11763,call_11765,call_11800,call_11804,var_11805,var_11806,call_11810,const_11811,])
output2 = relay.Tuple([call_11764,call_11766,call_11801,call_11807,var_11805,var_11806,call_11812,const_11811,])
func_11821 = relay.Function([var_11805,var_11806,], output)
mod['func_11821'] = func_11821
mod = relay.transform.InferType()(mod)
var_11822 = relay.var("var_11822", dtype = "int16", shape = (1, 165))#candidate|11822|(1, 165)|var|int16
var_11823 = relay.var("var_11823", dtype = "int16", shape = (825,))#candidate|11823|(825,)|var|int16
output = func_11821(var_11822,var_11823,)
func_11824 = relay.Function([var_11822,var_11823,], output)
mutated_mod['func_11824'] = func_11824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8050_call = mod.get_global_var('func_8050')
func_8052_call = mutated_mod.get_global_var('func_8052')
call_11826 = relay.TupleGetItem(func_8050_call(), 0)
call_11827 = relay.TupleGetItem(func_8052_call(), 0)
var_11839 = relay.var("var_11839", dtype = "float32", shape = (10, 10, 10))#candidate|11839|(10, 10, 10)|var|float32
bop_11840 = relay.greater(call_11826.astype('bool'), var_11839.astype('bool')) # shape=(10, 10, 10)
bop_11843 = relay.greater(call_11827.astype('bool'), var_11839.astype('bool')) # shape=(10, 10, 10)
func_5796_call = mod.get_global_var('func_5796')
func_5798_call = mutated_mod.get_global_var('func_5798')
call_11869 = relay.TupleGetItem(func_5796_call(), 0)
call_11870 = relay.TupleGetItem(func_5798_call(), 0)
func_9720_call = mod.get_global_var('func_9720')
func_9722_call = mutated_mod.get_global_var('func_9722')
call_11875 = relay.TupleGetItem(func_9720_call(), 0)
call_11876 = relay.TupleGetItem(func_9722_call(), 0)
output = relay.Tuple([bop_11840,call_11869,call_11875,])
output2 = relay.Tuple([bop_11843,call_11870,call_11876,])
func_11890 = relay.Function([var_11839,], output)
mod['func_11890'] = func_11890
mod = relay.transform.InferType()(mod)
var_11891 = relay.var("var_11891", dtype = "float32", shape = (10, 10, 10))#candidate|11891|(10, 10, 10)|var|float32
output = func_11890(var_11891)
func_11892 = relay.Function([var_11891], output)
mutated_mod['func_11892'] = func_11892
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7346_call = mod.get_global_var('func_7346')
func_7348_call = mutated_mod.get_global_var('func_7348')
call_12006 = func_7346_call()
call_12007 = func_7346_call()
output = relay.Tuple([call_12006,])
output2 = relay.Tuple([call_12007,])
func_12029 = relay.Function([], output)
mod['func_12029'] = func_12029
mod = relay.transform.InferType()(mod)
mutated_mod['func_12029'] = func_12029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12029_call = mutated_mod.get_global_var('func_12029')
call_12030 = func_12029_call()
output = call_12030
func_12031 = relay.Function([], output)
mutated_mod['func_12031'] = func_12031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10595_call = mod.get_global_var('func_10595')
func_10596_call = mutated_mod.get_global_var('func_10596')
call_12060 = relay.TupleGetItem(func_10595_call(), 1)
call_12061 = relay.TupleGetItem(func_10596_call(), 1)
output = relay.Tuple([call_12060,])
output2 = relay.Tuple([call_12061,])
func_12073 = relay.Function([], output)
mod['func_12073'] = func_12073
mod = relay.transform.InferType()(mod)
mutated_mod['func_12073'] = func_12073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12073_call = mutated_mod.get_global_var('func_12073')
call_12074 = func_12073_call()
output = call_12074
func_12075 = relay.Function([], output)
mutated_mod['func_12075'] = func_12075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5180_call = mod.get_global_var('func_5180')
func_5181_call = mutated_mod.get_global_var('func_5181')
call_12124 = relay.TupleGetItem(func_5180_call(), 0)
call_12125 = relay.TupleGetItem(func_5181_call(), 0)
output = relay.Tuple([call_12124,])
output2 = relay.Tuple([call_12125,])
func_12138 = relay.Function([], output)
mod['func_12138'] = func_12138
mod = relay.transform.InferType()(mod)
mutated_mod['func_12138'] = func_12138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12138_call = mutated_mod.get_global_var('func_12138')
call_12139 = func_12138_call()
output = call_12139
func_12140 = relay.Function([], output)
mutated_mod['func_12140'] = func_12140
mutated_mod = relay.transform.InferType()(mutated_mod)
const_12285 = relay.const([[[-6,-9,-4,2,9,-2,2],[-2,7,-9,-8,-1,-4,-1],[1,-8,7,-5,2,-4,-3],[-5,10,9,7,-10,-1,-7],[-1,5,-6,-1,10,8,3],[3,10,-9,7,10,6,-6],[10,1,2,5,8,-3,-4],[-2,-2,-1,5,5,-9,-6],[6,5,5,-7,-1,5,8],[10,10,7,7,4,-9,3],[-5,-7,1,5,8,-3,4],[-10,9,-4,-2,-10,-10,-8],[-5,-1,2,-9,9,-8,-8],[8,2,-4,-8,9,9,8],[4,-10,-8,7,-8,2,-2],[4,3,2,10,8,4,9]],[[-7,-3,-4,9,-4,4,5],[-7,8,7,-3,-9,-6,-4],[-4,-4,-1,-1,-9,-9,-7],[5,8,-8,-3,-8,-5,3],[3,2,2,10,4,-10,-4],[-8,-1,4,4,6,9,8],[-10,-5,-10,-2,-4,8,6],[1,-7,10,1,-5,-5,2],[4,8,-3,-9,-2,5,-5],[-2,-9,2,1,3,-5,-6],[-1,6,10,-1,7,-4,-3],[2,2,-3,-8,-8,-7,10],[-9,-4,-5,-6,-4,-8,9],[9,10,1,7,2,9,4],[-9,9,3,10,6,4,5],[1,3,7,1,-3,2,-4]],[[5,8,-4,-4,2,4,-2],[-8,-10,2,-10,7,6,10],[7,-10,1,6,7,-2,-6],[9,-7,-8,7,-2,-10,8],[1,6,1,-8,-6,-10,8],[3,8,-5,-8,-4,2,2],[5,8,10,-3,1,-7,-8],[1,-9,-2,-4,-4,10,7],[-5,6,1,-7,-9,3,-2],[7,5,9,-10,-1,-8,7],[4,-9,-3,1,10,-2,-8],[7,5,-1,-1,4,-1,-6],[-1,-6,6,-4,-2,-10,2],[-1,9,2,1,-4,-6,-4],[3,-8,4,9,-1,9,-9],[8,-3,4,7,7,1,-2]],[[10,-6,7,-7,-7,-3,3],[-6,10,-6,2,-8,7,-9],[-9,-5,-9,1,-4,9,9],[2,3,-4,1,-8,9,-6],[-3,5,7,8,3,-4,-2],[-10,4,-2,-9,9,-4,7],[-3,2,-7,8,10,-10,7],[-10,6,1,4,-6,-8,5],[4,-9,-2,-4,9,2,8],[-10,7,-6,-2,4,8,8],[-9,-2,-2,9,-2,-4,-5],[-8,-10,9,-2,2,-10,1],[8,-8,2,-9,10,10,-3],[3,-3,-2,-1,10,-6,7],[-1,-5,-8,6,-2,-6,-5],[4,-3,7,-8,-8,-9,-10]],[[3,10,6,10,8,-5,3],[3,-2,-5,4,2,2,-8],[-8,-8,8,4,-3,9,2],[-4,-5,-2,-5,-1,-10,8],[-3,-5,-5,-4,10,6,-2],[-7,-8,9,9,2,10,-1],[-8,-2,-5,4,9,4,5],[3,6,-2,-2,-10,4,-6],[-7,3,-6,-6,4,-5,-9],[-2,-9,-2,6,9,-6,-10],[-1,5,3,-1,4,4,-1],[-9,-7,5,-6,3,2,2],[1,10,-10,9,-2,-4,10],[-2,-8,1,4,3,4,3],[-10,-6,1,-2,-9,-4,-1],[-7,10,-4,-2,4,-1,-7]]], dtype = "int8")#candidate|12285|(5, 16, 7)|const|int8
var_12286 = relay.var("var_12286", dtype = "int8", shape = (5, 16, 7))#candidate|12286|(5, 16, 7)|var|int8
bop_12287 = relay.not_equal(const_12285.astype('bool'), relay.reshape(var_12286.astype('bool'), relay.shape_of(const_12285))) # shape=(5, 16, 7)
output = relay.Tuple([bop_12287,])
output2 = relay.Tuple([bop_12287,])
func_12298 = relay.Function([var_12286,], output)
mod['func_12298'] = func_12298
mod = relay.transform.InferType()(mod)
var_12299 = relay.var("var_12299", dtype = "int8", shape = (5, 16, 7))#candidate|12299|(5, 16, 7)|var|int8
output = func_12298(var_12299)
func_12300 = relay.Function([var_12299], output)
mutated_mod['func_12300'] = func_12300
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12320 = relay.var("var_12320", dtype = "float64", shape = (6, 13, 11))#candidate|12320|(6, 13, 11)|var|float64
uop_12321 = relay.sigmoid(var_12320.astype('float64')) # shape=(6, 13, 11)
bop_12325 = relay.less(uop_12321.astype('bool'), relay.reshape(var_12320.astype('bool'), relay.shape_of(uop_12321))) # shape=(6, 13, 11)
output = bop_12325
output2 = bop_12325
func_12329 = relay.Function([var_12320,], output)
mod['func_12329'] = func_12329
mod = relay.transform.InferType()(mod)
var_12330 = relay.var("var_12330", dtype = "float64", shape = (6, 13, 11))#candidate|12330|(6, 13, 11)|var|float64
output = func_12329(var_12330)
func_12331 = relay.Function([var_12330], output)
mutated_mod['func_12331'] = func_12331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9731_call = mod.get_global_var('func_9731')
func_9733_call = mutated_mod.get_global_var('func_9733')
call_12382 = relay.TupleGetItem(func_9731_call(), 0)
call_12383 = relay.TupleGetItem(func_9733_call(), 0)
func_11558_call = mod.get_global_var('func_11558')
func_11559_call = mutated_mod.get_global_var('func_11559')
call_12403 = relay.TupleGetItem(func_11558_call(), 0)
call_12404 = relay.TupleGetItem(func_11559_call(), 0)
func_7659_call = mod.get_global_var('func_7659')
func_7661_call = mutated_mod.get_global_var('func_7661')
call_12409 = relay.TupleGetItem(func_7659_call(), 1)
call_12410 = relay.TupleGetItem(func_7661_call(), 1)
bop_12421 = relay.mod(call_12403.astype('float64'), relay.reshape(call_12382.astype('float64'), relay.shape_of(call_12403))) # shape=(1, 10, 10)
bop_12424 = relay.mod(call_12404.astype('float64'), relay.reshape(call_12383.astype('float64'), relay.shape_of(call_12404))) # shape=(1, 10, 10)
func_4479_call = mod.get_global_var('func_4479')
func_4485_call = mutated_mod.get_global_var('func_4485')
var_12434 = relay.var("var_12434", dtype = "float32", shape = (448,))#candidate|12434|(448,)|var|float32
const_12435 = relay.const([3.338834,8.884813,-5.853646,4.937794,-5.358655,6.194585,0.544322,4.531644,-4.508687,-8.612177,9.618085,2.937539,1.594543,3.999840,6.916445,5.217594,0.277219,3.114677,9.127101,-5.836188,-7.668087,2.545442,4.649505,5.733683,-0.091579,-8.391159,9.007702,2.061785,-7.282881,-9.722353,4.936645,-1.499215,-7.022330,-9.218286,-5.711131,-2.740837,-8.463087,1.304407,-5.643771,-2.236474,-8.065951,-9.044790,-8.845798,5.051595,-9.773619,-8.371899,9.961535,-7.418724,-2.492147,8.056034,2.003763,-4.735755,-9.049976,-7.438393,-9.438190,1.378629,5.658367,-1.722058,-4.217237,-9.987652,6.058187,-0.699470,-2.019190,2.965027,1.998435,4.884086,-8.581192,-2.860242,8.217498,1.355545,2.928529,5.644801,-3.052034,-7.023767,4.635046,3.073248,4.240711,8.929227,-0.989838,0.992812], dtype = "float64")#candidate|12435|(80,)|const|float64
var_12436 = relay.var("var_12436", dtype = "int16", shape = (825,))#candidate|12436|(825,)|var|int16
var_12437 = relay.var("var_12437", dtype = "int16", shape = (165,))#candidate|12437|(165,)|var|int16
call_12433 = relay.TupleGetItem(func_4479_call(relay.reshape(var_12434.astype('float32'), [14, 16, 2]), relay.reshape(const_12435.astype('float64'), [80,]), relay.reshape(var_12436.astype('int16'), [825,]), relay.reshape(var_12437.astype('int16'), [165,]), relay.reshape(var_12434.astype('float32'), [14, 16, 2]), ), 6)
call_12438 = relay.TupleGetItem(func_4485_call(relay.reshape(var_12434.astype('float32'), [14, 16, 2]), relay.reshape(const_12435.astype('float64'), [80,]), relay.reshape(var_12436.astype('int16'), [825,]), relay.reshape(var_12437.astype('int16'), [165,]), relay.reshape(var_12434.astype('float32'), [14, 16, 2]), ), 6)
func_10555_call = mod.get_global_var('func_10555')
func_10558_call = mutated_mod.get_global_var('func_10558')
var_12446 = relay.var("var_12446", dtype = "uint16", shape = (1200,))#candidate|12446|(1200,)|var|uint16
call_12445 = relay.TupleGetItem(func_10555_call(relay.reshape(var_12446.astype('uint16'), [15, 16, 5]), relay.reshape(var_12446.astype('uint16'), [15, 16, 5]), ), 0)
call_12447 = relay.TupleGetItem(func_10558_call(relay.reshape(var_12446.astype('uint16'), [15, 16, 5]), relay.reshape(var_12446.astype('uint16'), [15, 16, 5]), ), 0)
func_10473_call = mod.get_global_var('func_10473')
func_10475_call = mutated_mod.get_global_var('func_10475')
call_12450 = relay.TupleGetItem(func_10473_call(), 1)
call_12451 = relay.TupleGetItem(func_10475_call(), 1)
func_8175_call = mod.get_global_var('func_8175')
func_8179_call = mutated_mod.get_global_var('func_8179')
const_12456 = relay.const([-6.440213,-0.293580,-3.479585,-2.577970,-5.944541,-9.352910,-3.109360,7.952707,-4.643336,0.359378,1.847678,-3.564719,1.051830,7.499431,4.420718,-8.089172,4.576265,4.357272,3.096723,6.212959,-7.225935,7.729572,-3.131343,6.594972,9.990817,6.465780,-8.690508,-7.768120,-5.961688,-0.536007,7.761649,9.815604,-2.266955,-2.686769,4.585374,4.100262,-9.213003,-0.651083,1.370386,4.417293,6.632612,0.129874,-7.806597,9.636678,5.437536,-5.914538,-2.322058,-5.422548,1.034585,-4.113294,-0.768793,-8.001093,9.534184,4.594152,-7.918960,5.231932,-4.129651,0.374446,-1.363362,7.798949,7.734591,4.463952,-2.788670,-7.097430,-8.317453,-6.919144,-4.619910,3.044418,1.133270,-7.348926,0.341406,1.463675,-7.735234,-1.866613,6.453577,4.650482,-4.403901,4.370276,-2.507496,-9.737870,-5.706597,7.412765,1.220232,-0.144717,-7.607118,7.981527,-5.441785,1.696216,8.572651,-1.606976,6.433212,1.074704,-0.956157,-2.034601,-9.379399,2.756713,8.380994,2.373238,-6.359122,-7.573590,-4.204072,-0.260429,-0.560237,-2.576069,-4.191797,0.122671,-9.545772,8.889215,8.763620,2.290193,-9.070778,-9.649521,0.451153,-3.508169,-1.603828,-3.781674,-7.297444,7.276650,-6.087200,6.620121,-5.846021,5.111051,6.478791,9.136017,-5.819772,7.455561,-9.199604,8.825159,5.160728,3.881082,-0.891605,6.988941,-2.128056,0.604773,-9.775210,6.887647,2.263517,3.083169,0.826254,2.470096,3.270276,-7.313006,9.392555,2.747413,-4.114851,-5.864112,7.314606,3.523234,-8.583787,-2.990025,0.355672,-7.606870,-6.878360,-1.774904,-3.656719,-8.931432,-4.291912,5.642512,-5.242374,-1.336165,7.235036,0.964567,-6.457997,6.603700,1.974962,1.609721,9.783908,-7.503995,0.117622,-9.237974,-8.249719,7.741049,5.992557,-1.204747,-4.037028,-7.038263,8.545758,-5.454744,8.636350,8.210103,0.481528,8.558804,-0.453388,0.813557,-0.948886,4.741416,-3.491940,3.796279,-7.073005,1.031772,8.653211,-0.845158,3.135055,-5.096522,-7.515919,6.289811,6.094127,3.695517,-9.825766,8.569379,-5.960737,-6.060508,-7.334883,-3.169352,8.117042,8.972022,-2.616955,-4.275528,-0.950178,-7.654737,-4.056449,-0.054078,-9.901458,8.763220,-1.815017,-3.152196,7.044444,3.632681,-3.920181,-1.053591,6.057613,-5.497261,-1.419537,4.473449,-9.519500,7.051584,-6.220579,-4.492435,8.317779,8.687526,-3.199119,-1.938295,-8.263178,3.513762,-9.947560,6.978347,2.804438,4.514743,-2.279425,-2.460662,-6.095914,4.675205,-3.485624,5.427474,5.293990,7.447093,-5.554374,5.072719,-6.585381,-6.217148,4.761682,-5.177332,6.629152,-6.854392,2.117095,-0.131777,-8.661254,-2.096188,2.099302,2.525960,-1.471299,4.491205,-0.163926,-7.619451,9.470884,7.784985,-1.381773,-3.190503,0.476475,4.900070,8.531927,-6.106435,2.732176,-5.207963,4.828542,7.169582,9.096064,-2.104406,0.388953,-5.747270,4.532981,5.436569,1.712498,-5.214219,-5.129424,8.392603,4.045567,-0.621821,-1.797504,-2.133521,-6.301168,-9.388568,-9.591720,2.823277,9.138337,-0.713942,-9.106572,-4.894526,7.403176,-1.739454,-2.955675,-2.335082,-5.590684,-7.190679,7.103323,-3.762473,-4.668078,5.952612,2.811763,-3.108870,-8.030814,-0.271234,7.038265,0.212731,0.855727,-8.267154,8.350289,8.038232,5.993381,0.586820], dtype = "float32")#candidate|12456|(320,)|const|float32
call_12455 = relay.TupleGetItem(func_8175_call(relay.reshape(const_12456.astype('float32'), [320,]), relay.reshape(call_12433.astype('int16'), [165,]), relay.reshape(var_12436.astype('int16'), [15, 5, 11]), ), 3)
call_12457 = relay.TupleGetItem(func_8179_call(relay.reshape(const_12456.astype('float32'), [320,]), relay.reshape(call_12433.astype('int16'), [165,]), relay.reshape(var_12436.astype('int16'), [15, 5, 11]), ), 3)
bop_12466 = relay.less_equal(call_12433.astype('bool'), var_12436.astype('bool')) # shape=(165, 825)
bop_12469 = relay.less_equal(call_12438.astype('bool'), var_12436.astype('bool')) # shape=(165, 825)
func_5378_call = mod.get_global_var('func_5378')
func_5379_call = mutated_mod.get_global_var('func_5379')
call_12478 = relay.TupleGetItem(func_5378_call(), 0)
call_12479 = relay.TupleGetItem(func_5379_call(), 0)
output = relay.Tuple([call_12409,bop_12421,var_12434,const_12435,var_12437,call_12445,var_12446,call_12450,call_12455,const_12456,bop_12466,call_12478,])
output2 = relay.Tuple([call_12410,bop_12424,var_12434,const_12435,var_12437,call_12447,var_12446,call_12451,call_12457,const_12456,bop_12469,call_12479,])
func_12481 = relay.Function([var_12434,var_12436,var_12437,var_12446,], output)
mod['func_12481'] = func_12481
mod = relay.transform.InferType()(mod)
mutated_mod['func_12481'] = func_12481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12481_call = mutated_mod.get_global_var('func_12481')
var_12483 = relay.var("var_12483", dtype = "float32", shape = (448,))#candidate|12483|(448,)|var|float32
var_12484 = relay.var("var_12484", dtype = "int16", shape = (825,))#candidate|12484|(825,)|var|int16
var_12485 = relay.var("var_12485", dtype = "int16", shape = (165,))#candidate|12485|(165,)|var|int16
var_12486 = relay.var("var_12486", dtype = "uint16", shape = (1200,))#candidate|12486|(1200,)|var|uint16
call_12482 = func_12481_call(var_12483,var_12484,var_12485,var_12486,)
output = call_12482
func_12487 = relay.Function([var_12483,var_12484,var_12485,var_12486,], output)
mutated_mod['func_12487'] = func_12487
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4628_call = mod.get_global_var('func_4628')
func_4629_call = mutated_mod.get_global_var('func_4629')
call_12491 = func_4628_call()
call_12492 = func_4628_call()
func_6596_call = mod.get_global_var('func_6596')
func_6597_call = mutated_mod.get_global_var('func_6597')
call_12497 = relay.TupleGetItem(func_6596_call(), 1)
call_12498 = relay.TupleGetItem(func_6597_call(), 1)
func_10595_call = mod.get_global_var('func_10595')
func_10596_call = mutated_mod.get_global_var('func_10596')
call_12513 = relay.TupleGetItem(func_10595_call(), 1)
call_12514 = relay.TupleGetItem(func_10596_call(), 1)
func_11821_call = mod.get_global_var('func_11821')
func_11824_call = mutated_mod.get_global_var('func_11824')
const_12518 = relay.const([10,-3,9,-6,-4,-4,-5,9,10,4,3,-7,-7,8,-8,8,-8,-1,-7,-10,5,4,-6,4,5,3,-7,-10,1,-6,10,5,4,-7,-2,-10,4,6,8,-7,-8,-8,1,1,-7,-8,-2,-7,6,7,-2,6,-2,-5,2,3,2,-7,1,-2,-9,-5,1,7,-7,-9,1,6,-8,4,-3,-2,-8,8,8,-10,-10,8,-9,3,7,-5,-7,-2,2,-5,-2,-1,-5,-2,1,-2,8,-4,-4,1,7,2,6,7,7,-4,8,-1,-6,-5,-4,-8,8,-7,7,6,5,7,9,3,7,-8,5,-7,-2,-8,1,9,5,10,8,-7,-3,8,10,9,-9,4,6,-6,6,-5,7,-4,1,-6,1,2,8,5,1,9,3,-5,7,-5,5,-7,3,-9,-7,-1,-8,2,5,6,-5,6,-8], dtype = "int16")#candidate|12518|(165,)|const|int16
const_12519 = relay.const([4,7,-4,-6,-8,-1,-7,5,7,1,-9,8,4,2,-8,-7,10,4,8,1,2,-3,6,6,7,7,-6,10,10,-2,-8,1,-2,-6,-4,8,-10,-4,-7,2,-10,10,4,6,9,-4,-6,8,9,-10,-2,-8,-9,9,-5,-10,9,-10,1,1,-5,-10,10,-1,-2,4,1,-6,-6,-6,5,-7,7,9,5,-7,-5,-1,5,-7,-5,2,-5,-4,-5,-4,-8,5,8,3,-6,-2,-9,7,5,2,-5,3,5,10,10,10,-5,-3,-3,-4,9,1,9,2,1,3,2,-7,7,-9,-1,5,6,-9,-6,-9,1,1,-7,5,8,-6,-7,-7,10,1,7,-7,8,3,1,7,1,5,4,7,-1,2,6,2,7,7,-1,-8,-4,-3,2,-8,-9,-2,4,-4,-4,3,-10,-8,-8,3,-1,10,-10,2,-4,-7,-5,5,10,-4,-8,4,2,4,-7,1,8,5,6,-1,8,-3,-9,-2,-10,1,3,-5,-9,5,8,6,-1,5,8,10,-4,-7,-1,-9,-5,-8,-10,-3,6,7,-6,-9,3,6,9,-5,9,5,-3,1,-7,-6,6,7,7,-5,6,2,9,9,2,-1,10,-10,-2,-10,-2,7,-8,-7,8,-10,5,2,-7,-1,8,9,10,10,-10,1,1,-9,4,-5,-9,7,-6,9,-3,-4,4,9,-1,-4,-3,5,4,-2,2,-1,4,-5,8,-4,6,-9,1,2,9,5,4,-8,5,-9,9,8,-7,-2,8,-3,5,-3,-2,-10,-3,-6,6,7,4,-8,5,4,8,-8,-3,-9,5,-5,-8,-1,-10,10,-9,-7,3,3,9,10,5,-4,-9,7,4,2,-8,3,-9,4,-9,8,6,8,1,5,-7,4,-1,-1,-6,-6,-5,-2,3,-2,-9,-2,4,-2,-1,-2,-5,4,9,2,-8,2,9,-10,2,-5,-2,9,1,10,-8,10,-9,1,2,5,-2,-5,-1,-3,5,-5,7,3,-7,9,5,1,8,4,-3,-9,-8,-6,-9,3,9,1,3,-5,6,6,-7,-7,-8,2,4,6,6,-10,-3,9,10,-9,1,-3,-9,-10,5,1,2,3,-5,-5,-3,7,7,-1,5,2,-5,5,-4,-10,4,-10,-5,10,6,-4,-4,6,-7,10,6,-10,-7,-4,-9,7,8,-2,4,6,9,8,10,-7,-2,9,-9,8,-1,6,-9,-7,-2,-1,-1,6,-6,5,10,-1,7,10,-8,-3,-1,10,1,6,-6,-2,3,-9,4,-4,-4,-9,-4,8,-5,2,-9,3,-2,5,-7,7,7,-8,-7,-9,7,3,-5,5,3,6,-2,2,-10,-3,6,-7,-3,-7,-7,-3,-2,-8,-9,-7,-10,4,1,-7,-5,-8,-8,3,9,-4,-6,-1,-1,-3,1,3,-2,5,-3,6,3,-8,-10,2,10,-8,-3,5,7,4,-8,1,-4,-7,1,4,9,4,-2,3,-4,-8,-1,1,-1,-7,-4,2,9,4,3,3,-9,-5,7,4,-8,-8,-7,6,6,10,-6,-7,-2,-4,-10,-8,5,-1,-1,4,9,-10,-3,-4,-2,8,-7,-2,7,-5,-2,-7,8,1,-4,1,-9,10,7,-2,8,-8,6,-5,3,-1,5,-4,-7,-2,-2,-4,4,-2,10,2,5,-5,10,-3,2,-10,3,7,8,10,-2,10,10,7,-5,8,-8,10,-4,1,-6,-2,4,8,-1,-2,7,-9,4,-7,-4,9,-1,-2,-4,3,-3,-9,-6,-8,7,10,-2,1,4,4,-4,-3,-4,9,9,7,9,-10,-5,2,8,6,-2,3,4,5,2,4,-3,3,-7,4,6,-2,2,-5,-7,-10,7,-4,-3,-2,5,1,8,-9,-2,-2,-7,-1,8,9,6,-6,-7,7,-9,6,-2,-3,-1,-5,5,3,-2,1,2,-7,1,5,-6,-9,9,9,4,-2,-4,8,-6,1,9,8,-4,-2,-2,5,9,-3,1,10,5,10,8,-1,1,2,6,1,-7,-4,-2,-7,3,9,-1,9,10,-7,7,5,-10,8,-9,5,-6,4,-6,-10,2,-4,10,-1,5,1,6,2,4,-3,10,8,-4,3,7,10,-3,-2,-10,-5,1,-6,3,6,-9,2,-4,7,-5,10,6,-1,6,3,-6,-10,-4,5,-6,9,-9,-5,1], dtype = "int16")#candidate|12519|(825,)|const|int16
call_12517 = relay.TupleGetItem(func_11821_call(relay.reshape(const_12518.astype('int16'), [1, 165]), relay.reshape(const_12519.astype('int16'), [825,]), ), 0)
call_12520 = relay.TupleGetItem(func_11824_call(relay.reshape(const_12518.astype('int16'), [1, 165]), relay.reshape(const_12519.astype('int16'), [825,]), ), 0)
func_8079_call = mod.get_global_var('func_8079')
func_8081_call = mutated_mod.get_global_var('func_8081')
call_12521 = relay.TupleGetItem(func_8079_call(relay.reshape(call_12517.astype('float32'), [5, 9, 4])), 0)
call_12522 = relay.TupleGetItem(func_8081_call(relay.reshape(call_12517.astype('float32'), [5, 9, 4])), 0)
func_8353_call = mod.get_global_var('func_8353')
func_8355_call = mutated_mod.get_global_var('func_8355')
call_12527 = relay.TupleGetItem(func_8353_call(), 0)
call_12528 = relay.TupleGetItem(func_8355_call(), 0)
func_6596_call = mod.get_global_var('func_6596')
func_6597_call = mutated_mod.get_global_var('func_6597')
call_12531 = relay.TupleGetItem(func_6596_call(), 0)
call_12532 = relay.TupleGetItem(func_6597_call(), 0)
uop_12545 = relay.rsqrt(call_12521.astype('float32')) # shape=(5, 9, 4)
uop_12547 = relay.rsqrt(call_12522.astype('float32')) # shape=(5, 9, 4)
func_10978_call = mod.get_global_var('func_10978')
func_10981_call = mutated_mod.get_global_var('func_10981')
const_12549 = relay.const([-4.252337,5.036113,-4.970058,9.424199,-8.970751,8.194100,-0.364196,5.960387,3.782336,8.324350,4.640723,-3.086703,9.212400,-8.337650,-9.588832,-0.347740,5.565785,4.495520,-3.094419,-8.801734,-5.964584,8.621999,3.238683,8.053742,0.369420,-3.701638,-8.597203,-0.448609,3.238056,-1.073938,-7.263770,-3.446999,4.145440,5.089372,-2.096615,-9.427180,3.591787,3.565434,-7.144406,1.752163,-4.041802,-9.974965,-9.799897,-1.548103,2.723843,0.876985,5.808037,-7.431945,3.914834,6.110552,7.041411,-9.301379,1.465313,5.055111,8.240490,3.910997,-6.039754,-9.327292,-2.093952,-4.471038,5.323448,3.055451,-3.254385,3.453738,5.516514,3.208844,-7.097836,9.104438,-6.955586,-3.437437,9.794625,3.809199,8.886727,-7.785999,-4.662226,-8.215881,-7.865722,-9.411141,8.099510,-0.426441,-2.387802,7.838710,-8.626525,9.131280,1.065119,-3.681122,5.503064,8.532462,1.348955,1.948839,-4.972162,7.740900,0.895524,5.786165,-0.806094,-3.456103,-6.402403,5.689860,-5.246823,1.872933,-6.077677,0.143530,0.876751,1.082960,-2.193950,-1.455307,-4.102556,-6.206926,7.225838,-3.481127,8.560678,5.790457,-4.694290,-2.239054,8.247774,-1.531691,3.843988,5.668129,-0.054987,6.111507,9.056477,-6.268812,-2.534522,-8.162499,-4.440904,1.988226,9.898180,5.020038,4.935531,-8.699750,9.974968,9.723640,-6.541451,3.292872,7.328176,-4.764030,-1.857828,-9.911547,6.736344,1.582644,8.589341,1.708865,5.259379,-7.310828,1.435769,0.520706,0.315112,0.960198,5.371820,6.781200,-2.616513,-3.536040,-5.596560,5.807495,4.311429,3.080447,9.898784,9.205854,-0.917888,3.128508,-6.810356,-5.846338,7.855373,-4.493430,6.325358,7.473857,7.563302,-4.793543,-9.537802,0.675432,-4.182173,-8.015020,9.624598,-2.846101,4.590544,3.599935,-7.407771,-4.148371,-0.576775,0.344896,-7.065955,4.758415,-3.306211,6.474635,5.663397,-7.167449,9.157446,0.169549,-6.743328,-7.156643,4.786088,3.021168,-4.862879,-2.885129,-9.123488,-3.768496,-1.578259,-6.335298,9.075632,-5.570839,-8.600815,9.950615,2.862829,3.122073,-3.405312,-6.591933,9.525844,-7.594918,2.495569,-5.317403,-8.192818,-9.080130,-2.677769,7.893193,-3.267647,-1.588871,-9.063571,-4.894884,-5.189463,1.209604,-8.041835,6.810674,8.896593,2.816411,-5.723537,0.824656,-5.262171,0.608701,-4.061522,-4.980331,-7.552087,-1.131685,-9.793995,4.956822,-6.176892,-4.911504,-7.287316,-0.419044,4.290269,-5.844975,-4.098464,-7.785691,3.853601,3.730817,-9.215266,-4.322236,1.230121,3.961768,8.364426,-5.171579,5.715641,-4.359033,-1.588171,4.095921,-8.897247,8.022739,6.663129,2.758830,-3.275123,5.805083,4.594968,0.014120,-9.542270,-3.086183,6.058135,6.246138,2.971074,-1.772064,-9.885715,0.358453,3.751658,3.483317,-4.395919,8.099148,-9.695841,8.203276,-1.556551,-2.838746,6.846973,0.269803,4.602788,8.535696,-3.433747,8.531829,-8.530386,-2.232348,5.235460,-3.851302,-6.300393,-7.345747,-2.619315,-7.550808,9.214594,2.577798,-1.387357,8.492871,4.314747,-9.023238,0.773813,5.324531,7.894932,6.736315,2.948661,-7.186239,-1.563982,-6.357694,6.799759,3.573974,7.005384,8.941488,4.659858,-7.477602,-6.584129,6.792563,-3.485532,9.922041,-5.416964,-0.085982,-0.814238,7.503388,-5.871666,-3.735021,5.441567,-9.485590,-9.202233,-2.057446,-5.335052,0.364576,2.787672,-2.166429,7.898471,3.733086,5.490161,0.490129,7.674723,-8.634333,5.973497,2.471625,-4.831717,1.283941,6.116432,4.962205,-8.927890,-8.498417,1.050890,7.128655,-7.566535,-3.560466,0.872143,-6.375620,-3.863257,-6.749594,9.734365,-6.734479,0.485706,-0.418992,2.925106,-7.175932,-9.231394,-1.662515,-9.147587,-7.240223,-4.546913,-8.275738,0.476785,-1.331108,0.575221,9.303040,-3.851224,-4.194583,3.261863,3.160343,-9.396351,9.594690,-0.649919,-0.332919,8.548611,-4.513216,8.738200,3.272731,3.174040,1.549033,-3.658868,0.442106,-6.325332,-4.004130,-3.545658,1.064247,-9.162060,-5.690364,-5.332246,3.101842,0.030306,8.285249,-5.741582,2.299208,1.565945,-1.813885,4.464744,-0.629352,9.533955,-8.300656,-6.166999,3.636374,-0.718488,-0.253892,-7.932488,-2.961268,2.295782,7.458295,6.179472,1.793231,2.368771,-0.177298,7.475457,-4.377565,-6.118692,-5.059607,-7.372816,3.988822,8.341139,8.843045,4.030164,-9.683223,-5.641371,-9.976473,-0.197692,-1.042537,0.133386,9.093146,3.193929,8.440850,-9.285043,1.854300,0.004008,3.458242,-0.274822,2.035294,-5.633853,-2.951538,4.072264,-6.451747,-5.275362,0.472041,-8.707859,-8.400450,-4.435409,9.001476,6.797867,-1.556175,1.410518,-3.379772,-9.804701,7.674618,8.698010,8.844663,-8.491118,-6.556840,-8.643065,-0.969785,-8.269334,9.147831,-8.028593,2.924502,4.595370,9.709152,7.774735,-1.446474,3.364239,9.307527,0.065631,6.726113,-9.665152,-9.503197,3.755636,9.111673,2.690281,-7.949231,7.241553,1.486536,4.086811,4.220278,-3.613477,3.723279,0.035367,-0.057636,0.438829,-8.232424,-7.791522,5.349454,6.388309,0.394640,9.307707,6.908716,-4.488586,0.173175,8.671792,-2.572587,-4.060467,3.838789,-5.217826,-5.028487,4.805285,-6.582678,0.360882,5.263980,-6.047857,4.232876,-6.944609,5.975338,1.836127,7.040969,1.350351,7.557168,6.947079,-6.703882,-0.966217,2.110774,5.572021,1.724451,4.810031,-1.654983,-0.993476,6.686394,-7.203671,9.601376,5.790482,-1.107047,-0.043930,-5.655763,-1.552750,-1.078428,0.555141,-6.844064,5.911358,0.006337,-8.042922,-3.437826,9.073887,7.164481,-0.340667,-1.681574,1.274515,5.525085,-3.086585,5.026630,-1.930231,5.749490,-7.667199,-8.786333,-3.683213,-0.365853,9.421834,0.290861,8.353607,-0.135988,4.173460,6.703840,9.905468,-1.037695,4.068935,-2.879706,1.293379,7.519796,7.960079,1.755483,-8.715091,-8.863881,0.716416,-6.643347,9.201271,-6.801080,7.395810,0.932588,-9.036181,-4.069746,-3.784316,9.727382,1.650434,7.062898,2.788072,-4.697536,-8.258800,3.977366,-3.280322,-7.981147,9.978400,-9.948325,0.515042,1.988325,9.761466,3.501809,0.308267,-4.771137,0.201867,4.071133,-6.911673,-1.241702,8.786204,-6.784157,-3.501227,4.019904,-9.806949,-2.800476,4.234530,7.143903,-2.000006,-8.733597,-4.387506,-0.842850,-0.078533,-0.440418,4.120468,-2.055119,-2.560862,-5.650480,8.431008,-3.996458,4.711849,4.026773,6.772682,0.759723,6.827602,7.877432,-5.186992,-5.233456,1.279148,-7.625634,8.456249,1.013429,2.873469,-4.057172,5.698237,-1.886609,-8.110114,-5.330344,4.475662,0.712254,5.763591,-0.700847,-8.435397,8.747241,3.923640,-2.000336,-1.218074,-3.406100,0.886070,-8.721433,-2.612762,7.459212,3.519323,-6.365505,8.744185,5.339510,-5.020380,8.209741,-2.045244,-6.265020,-8.275840,0.747152,9.173144,-3.831522,-5.981132,5.811199,-1.218921,4.486393,-4.958797,-0.384883,6.374387,6.124041,0.971689,-8.823460,2.778534,1.055212,6.700073,-9.326576,-2.022675,4.766753,8.938437,8.829030,9.139304,2.374321,-7.243497,-6.758470,-7.137584,7.707753,-8.238759,3.122170,2.990310,0.338129,0.761087,6.072991,-8.287279,3.139447,4.074167,4.937237,5.008010,6.867226,-5.242824,-2.620039,9.898504,-4.706388,9.656795,6.298430,-2.421640,-3.258771,-5.402571,-7.549500,-4.861233,-6.558290,-0.178788,4.944039,7.689389,-2.229578,-5.749649,-3.874711,-5.265582,2.161035,-0.014411,-5.921182,8.370109,1.867822,-9.379785,-8.710848,0.904761,3.903162,8.841411,5.372479,5.216179,-1.838856,-1.108464,1.116904,-8.674551,3.716910,9.875593,1.662670,-1.442848,-7.049707,-0.184072,7.742534,0.965550,-2.079844,6.533453,8.218394,3.134189,-5.952076,-0.503983,-4.034444,-1.222883,-5.821155,-8.817184,-0.333331,-2.972723,5.142841,-3.370742,-8.204926,5.325862,-4.749510,-9.875571,3.424965,9.953113,-4.385348,7.296399,-0.847050,-4.482126,6.340695,0.304307,0.053030,-2.302314,-7.113379,8.167667,6.326822,6.933222,-9.860033,7.537598,2.671897,6.695398,5.902458,6.696364,3.989891,-7.807826,-6.883673,-0.732310,7.874958,-2.268889,0.981176,-5.706090,3.664690,-6.188008,0.198246,8.252443,0.881964,-0.539589,-3.099416,-8.175863,5.612143,-0.425932,-6.802422,2.138746,-3.182494,-0.188032,-4.196302,-8.185361,-9.817653,3.688854,-9.601650,0.228361,8.941266,-2.974116,6.991238,1.755265,9.374762,-3.636991,4.553529,8.202930,0.609721,2.585893,-5.691263,5.572761,8.977489,5.695239,-4.456189,8.790830,-0.939146,8.544011,-3.942169,6.843221,-3.466540,-3.144796,3.927922,1.709949,3.688521,-2.894743,-9.437606,-7.994278,-9.282356,-3.331643,-4.306736,1.519600,1.337118,-2.683577,4.123988,-0.429352,0.618649,4.412662,-0.634933,-0.982439,-8.728570,-8.744366,-8.440168,-2.061556,-9.735269,8.153583,-6.436732,5.997931,3.561863,2.028121,5.811038,9.584784,-1.875362,-5.943657,6.317572,-7.480081,0.928895,5.218980,-9.687353,2.914721,-0.341479,7.447513,8.756680,-4.424560,6.793116,0.739100,3.489433,5.656444,-4.156207,5.720538,-2.123941,4.442133,-7.412360,-5.606115,-9.482831,9.557214,-8.926960,5.289028,1.771848,4.800604,8.196558,-7.859112,2.406027,3.273467,0.923845,7.058860,-6.017172,7.892347,0.587365,2.093908,4.621489,-1.061162,-8.337499,4.166561,-0.644962,-1.989474,-0.107381,-4.933526,-0.043485,2.020245,-2.393451,-1.817675,8.276501,7.208418,4.478421,-0.513884,7.283636,-5.974990,-5.052160,-5.849460,-5.672621,-8.800146,1.616657,-3.992847,-2.398747,8.377186,1.144523,-8.864994,3.526495,5.509249,-3.655910,-3.609744,2.259056,5.190606,-9.774928,-0.498614,-2.181841,8.040883,9.609251,-0.711898,8.384630,2.388491,2.021099,9.146715,3.144199,0.699853,-1.657264,-0.521474,-7.639812,9.950429,2.346969,-9.898110,7.318059,9.599258,7.680493,-6.342762,4.334458,7.917027,0.500138,0.323187,-4.780253,1.055369,-6.791570,-2.121705,7.247391,-0.566226,4.535604,3.648587,-3.708173,7.095769,-3.993053,7.448565,1.537025,-8.543076,7.957501,-8.213822,-1.120650,0.091358,5.337285,8.841596,5.013557,0.524833,-6.902768,8.592017,4.979388,1.313583,0.393919,8.862533,4.683988,1.033085,7.667399,-5.069938,5.754620,9.178964,0.570217,-0.467858,-6.626694,5.928441,-2.929811,3.517866,-9.628992,9.435675,5.859480,-9.919596,-0.764677,-6.748639,5.575774,0.377855,-9.623738,6.380251,0.464812,-8.131349,5.341453,8.117677,6.366968,2.277808,2.264029,7.769161,8.687807,1.455426,5.735463,-2.496095,5.795867,-8.381828,-7.538208,9.663725,3.479873,1.169282,-6.955481,-6.786210,5.036367,8.990571,-9.492438,-1.284000,-2.586800,6.448350,4.324114,3.209191,4.039724,-5.285224,0.561397,0.724236,9.118048,-5.361838,4.176927,3.655854,-8.187477,2.205623,5.746445,9.580167,-8.437802,-1.529868,-1.098146,-2.666301,5.177576,4.228911,-2.867343,4.163608,9.867824,4.996605,-7.188380,8.291772,8.387678,1.095899,-3.432726,0.489163,3.072596,-9.389105,8.244157,6.273529,6.656349,4.256200,8.314193,-8.602798,-1.399037,-2.772722,-2.554192,-7.289742,-9.588769,7.923409,-0.807355,7.431398,-8.442020,6.222040,-4.138961,-6.945666,5.478503,-4.409728,-6.705086,3.350086,-3.884551,2.058345,1.139781,2.965994,3.759543,2.136803,4.568445,8.874352,-1.805700,6.015561,3.491174,2.073155,5.037823,9.785601,-1.321903,9.302465,-6.726201,9.057909,-8.115684,-1.041728,6.720502,3.377342,-0.625859,-6.305522,7.499388,-9.763008,5.890987,8.535260,8.144188,-3.439310,8.982635,-0.746855,-6.767508,1.592153,-4.769095,-5.326300,6.296308,-3.519100,-6.754925,7.907263,-2.278682,-4.966250,3.589681,1.022332,9.768829,-2.233613,8.341412,-0.355583,-0.278137,-0.268209,5.855825,8.938353,-2.756645,4.100171,-4.350244,-8.227998,-1.120730,3.790563,-6.645761,-0.922840,-6.516790,-6.670748,5.706608,-5.740914,-0.411622,4.872320,6.631106,4.333168,-0.480296,1.980927,3.986384,-2.506932,-1.748376,8.135848,-0.425182,-7.042235,-7.146974,-2.203725,-5.685358,9.215133,7.385813,-3.935022,3.516058,-7.582763,-3.751961,8.154452,1.243669,7.826798,2.208021,-3.294470,-6.301567,-9.282698,3.691899,8.073805,7.357361,-9.301726,3.158120,-9.264763,-1.848291,-5.349618,-8.599823,-2.966532,4.531486,0.946935,-7.572985,-0.739301,9.319561,0.028268,3.991048,-3.109210,-7.663772,0.903635,9.667158,-0.280204,-0.329575,8.564147,-5.166937,-6.614190,5.743127,-7.074700,0.261637,9.970992,-6.846399,5.731763,2.872120,-5.465408,3.984280,7.732320,2.229450,-1.809416,-2.077478,-0.084454,-6.028236,3.045658,0.845495,9.164398,-0.525053,3.880490,-7.317324,0.175403,-6.348906,3.686862,2.030796,-3.727901,-7.115687,3.146403,-6.340991,-0.821627,-6.643449,2.953168,9.003328,6.853992,4.401038,-0.368687,9.695852,3.518491,-1.354465,0.359332,0.523323,-5.839990,0.859630,-4.069545,-5.792550,-5.960358,-1.513795,-9.854835,-1.457506,-3.819673,-3.501483,2.328226,-5.438083,3.994743,3.218101,-1.611915,-1.607695,0.839028,-8.834755,-6.260406,-6.901302,-6.855059,-7.464307,-5.858438,-5.432233,-6.159122,-4.622659,-2.179493,-5.034065,4.570948,6.268819,-2.986611,-6.206153,3.978462,6.289523,4.066239,-2.259957,6.938166,-7.052424,2.052222,-1.452666,0.181727,-6.036904,2.909386,9.152898,-1.116546,-7.834446,1.546825,-4.664349,-4.646465,-1.929011,5.312596,6.715531,3.157532,6.356900], dtype = "float64")#candidate|12549|(1300,)|const|float64
var_12550 = relay.var("var_12550", dtype = "float64", shape = (1500, 1))#candidate|12550|(1500, 1)|var|float64
call_12548 = relay.TupleGetItem(func_10978_call(relay.reshape(const_12549.astype('float64'), [13, 10, 10]), relay.reshape(var_12550.astype('float64'), [15, 10, 10]), ), 1)
call_12551 = relay.TupleGetItem(func_10981_call(relay.reshape(const_12549.astype('float64'), [13, 10, 10]), relay.reshape(var_12550.astype('float64'), [15, 10, 10]), ), 1)
func_8419_call = mod.get_global_var('func_8419')
func_8420_call = mutated_mod.get_global_var('func_8420')
call_12574 = relay.TupleGetItem(func_8419_call(), 0)
call_12575 = relay.TupleGetItem(func_8420_call(), 0)
func_5023_call = mod.get_global_var('func_5023')
func_5024_call = mutated_mod.get_global_var('func_5024')
call_12579 = func_5023_call()
call_12580 = func_5023_call()
func_10429_call = mod.get_global_var('func_10429')
func_10432_call = mutated_mod.get_global_var('func_10432')
call_12594 = relay.TupleGetItem(func_10429_call(relay.reshape(const_12518.astype('int16'), [165,])), 1)
call_12595 = relay.TupleGetItem(func_10432_call(relay.reshape(const_12518.astype('int16'), [165,])), 1)
bop_12614 = relay.greater(const_12549.astype('bool'), var_12550.astype('bool')) # shape=(1500, 1300)
var_12623 = relay.var("var_12623", dtype = "float32", shape = (5, 9, 4))#candidate|12623|(5, 9, 4)|var|float32
bop_12624 = relay.maximum(uop_12545.astype('int64'), relay.reshape(var_12623.astype('int64'), relay.shape_of(uop_12545))) # shape=(5, 9, 4)
bop_12627 = relay.maximum(uop_12547.astype('int64'), relay.reshape(var_12623.astype('int64'), relay.shape_of(uop_12547))) # shape=(5, 9, 4)
uop_12630 = relay.log10(bop_12614.astype('float32')) # shape=(1500, 1300)
func_8003_call = mod.get_global_var('func_8003')
func_8005_call = mutated_mod.get_global_var('func_8005')
call_12634 = relay.TupleGetItem(func_8003_call(), 1)
call_12635 = relay.TupleGetItem(func_8005_call(), 1)
var_12644 = relay.var("var_12644", dtype = "int64", shape = (5, 9, 4))#candidate|12644|(5, 9, 4)|var|int64
bop_12645 = relay.greater(bop_12624.astype('bool'), relay.reshape(var_12644.astype('bool'), relay.shape_of(bop_12624))) # shape=(5, 9, 4)
bop_12648 = relay.greater(bop_12627.astype('bool'), relay.reshape(var_12644.astype('bool'), relay.shape_of(bop_12627))) # shape=(5, 9, 4)
func_9844_call = mod.get_global_var('func_9844')
func_9845_call = mutated_mod.get_global_var('func_9845')
call_12664 = relay.TupleGetItem(func_9844_call(), 0)
call_12665 = relay.TupleGetItem(func_9845_call(), 0)
output = relay.Tuple([call_12491,call_12497,call_12513,call_12517,const_12518,const_12519,call_12527,call_12531,call_12548,call_12574,call_12579,call_12594,uop_12630,call_12634,bop_12645,call_12664,])
output2 = relay.Tuple([call_12492,call_12498,call_12514,call_12520,const_12518,const_12519,call_12528,call_12532,call_12551,call_12575,call_12580,call_12595,uop_12630,call_12635,bop_12648,call_12665,])
func_12673 = relay.Function([var_12550,var_12623,var_12644,], output)
mod['func_12673'] = func_12673
mod = relay.transform.InferType()(mod)
mutated_mod['func_12673'] = func_12673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12673_call = mutated_mod.get_global_var('func_12673')
var_12675 = relay.var("var_12675", dtype = "float64", shape = (1500, 1))#candidate|12675|(1500, 1)|var|float64
var_12676 = relay.var("var_12676", dtype = "float32", shape = (5, 9, 4))#candidate|12676|(5, 9, 4)|var|float32
var_12677 = relay.var("var_12677", dtype = "int64", shape = (5, 9, 4))#candidate|12677|(5, 9, 4)|var|int64
call_12674 = func_12673_call(var_12675,var_12676,var_12677,)
output = call_12674
func_12678 = relay.Function([var_12675,var_12676,var_12677,], output)
mutated_mod['func_12678'] = func_12678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8353_call = mod.get_global_var('func_8353')
func_8355_call = mutated_mod.get_global_var('func_8355')
call_12789 = relay.TupleGetItem(func_8353_call(), 0)
call_12790 = relay.TupleGetItem(func_8355_call(), 0)
func_10159_call = mod.get_global_var('func_10159')
func_10161_call = mutated_mod.get_global_var('func_10161')
call_12795 = func_10159_call()
call_12796 = func_10159_call()
func_7047_call = mod.get_global_var('func_7047')
func_7048_call = mutated_mod.get_global_var('func_7048')
call_12797 = relay.TupleGetItem(func_7047_call(), 0)
call_12798 = relay.TupleGetItem(func_7048_call(), 0)
var_12801 = relay.var("var_12801", dtype = "float32", shape = (3, 10, 10))#candidate|12801|(3, 10, 10)|var|float32
bop_12802 = relay.mod(call_12789.astype('float32'), var_12801.astype('float32')) # shape=(3, 10, 10)
bop_12805 = relay.mod(call_12790.astype('float32'), var_12801.astype('float32')) # shape=(3, 10, 10)
output = relay.Tuple([call_12795,call_12797,bop_12802,])
output2 = relay.Tuple([call_12796,call_12798,bop_12805,])
func_12807 = relay.Function([var_12801,], output)
mod['func_12807'] = func_12807
mod = relay.transform.InferType()(mod)
mutated_mod['func_12807'] = func_12807
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12808 = relay.var("var_12808", dtype = "float32", shape = (3, 10, 10))#candidate|12808|(3, 10, 10)|var|float32
func_12807_call = mutated_mod.get_global_var('func_12807')
call_12809 = func_12807_call(var_12808)
output = call_12809
func_12810 = relay.Function([var_12808], output)
mutated_mod['func_12810'] = func_12810
mutated_mod = relay.transform.InferType()(mutated_mod)
const_12812 = relay.const([[[-6,-6,-9,-4,5,-7,2,9,1],[7,5,-8,2,1,10,2,3,10],[10,-4,-4,3,-4,-1,8,-6,-2],[1,-6,3,-10,-4,2,7,-8,7],[2,7,-2,3,-6,7,5,-1,-2],[-7,-1,7,4,5,3,-1,-4,10],[-7,-8,-4,-1,2,-10,-8,7,7],[-3,8,-3,2,5,-2,-1,-10,10],[-3,2,2,-10,-10,-10,-2,10,-2],[2,-4,-7,-4,3,-7,-9,-5,6]],[[3,-10,4,10,2,8,2,6,-7],[-2,1,-4,-2,9,-3,5,-10,1],[-4,1,-2,9,-7,9,10,-4,7],[-1,2,-6,-2,1,5,-7,-2,4],[5,7,8,7,-5,1,10,3,-2],[7,2,-6,-9,-6,1,-6,-3,2],[8,1,2,-9,2,4,-3,-7,-8],[-1,-8,-1,-7,7,1,1,-9,-5],[4,3,8,-1,-8,-3,3,-7,-1],[2,-7,-7,-10,-8,-3,-10,-8,5]],[[2,-6,-4,1,5,2,6,5,5],[-2,2,-4,6,4,-10,-2,4,-5],[9,8,3,1,4,-5,-7,5,-6],[6,4,-5,-8,-7,5,3,-7,9],[10,3,5,4,2,3,8,-1,-9],[9,3,4,-7,5,5,-5,-5,1],[-4,-4,-4,-6,6,7,4,-5,-1],[9,5,1,8,-6,-4,-5,-2,9],[-3,8,-2,5,2,-5,8,-10,-5],[-4,7,-8,-5,-3,1,2,-7,-3]],[[9,5,9,-4,-3,1,-5,3,-3],[7,3,6,2,-7,-10,9,10,1],[-5,6,9,-8,-2,-8,-3,4,7],[-1,6,9,2,-5,4,-2,1,9],[-7,6,-9,4,-1,1,8,8,-3],[2,-7,-6,3,9,7,-7,6,-6],[2,-8,-10,-3,-2,2,8,-9,-1],[5,6,-1,4,9,-3,-5,-5,-8],[-4,3,3,-1,9,5,8,7,6],[7,8,-7,9,6,7,-8,8,-6]]], dtype = "int16")#candidate|12812|(4, 10, 9)|const|int16
var_12813 = relay.var("var_12813", dtype = "int16", shape = (4, 10, 9))#candidate|12813|(4, 10, 9)|var|int16
bop_12814 = relay.bitwise_or(const_12812.astype('int16'), relay.reshape(var_12813.astype('int16'), relay.shape_of(const_12812))) # shape=(4, 10, 9)
func_6596_call = mod.get_global_var('func_6596')
func_6597_call = mutated_mod.get_global_var('func_6597')
call_12824 = relay.TupleGetItem(func_6596_call(), 0)
call_12825 = relay.TupleGetItem(func_6597_call(), 0)
func_7257_call = mod.get_global_var('func_7257')
func_7259_call = mutated_mod.get_global_var('func_7259')
call_12842 = relay.TupleGetItem(func_7257_call(), 0)
call_12843 = relay.TupleGetItem(func_7259_call(), 0)
output = relay.Tuple([bop_12814,call_12824,call_12842,])
output2 = relay.Tuple([bop_12814,call_12825,call_12843,])
func_12845 = relay.Function([var_12813,], output)
mod['func_12845'] = func_12845
mod = relay.transform.InferType()(mod)
var_12846 = relay.var("var_12846", dtype = "int16", shape = (4, 10, 9))#candidate|12846|(4, 10, 9)|var|int16
output = func_12845(var_12846)
func_12847 = relay.Function([var_12846], output)
mutated_mod['func_12847'] = func_12847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5544_call = mod.get_global_var('func_5544')
func_5546_call = mutated_mod.get_global_var('func_5546')
call_12901 = func_5544_call()
call_12902 = func_5544_call()
output = relay.Tuple([call_12901,])
output2 = relay.Tuple([call_12902,])
func_12917 = relay.Function([], output)
mod['func_12917'] = func_12917
mod = relay.transform.InferType()(mod)
mutated_mod['func_12917'] = func_12917
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12917_call = mutated_mod.get_global_var('func_12917')
call_12918 = func_12917_call()
output = call_12918
func_12919 = relay.Function([], output)
mutated_mod['func_12919'] = func_12919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5544_call = mod.get_global_var('func_5544')
func_5546_call = mutated_mod.get_global_var('func_5546')
call_12945 = func_5544_call()
call_12946 = func_5544_call()
var_12955 = relay.var("var_12955", dtype = "float64", shape = (2, 10, 10))#candidate|12955|(2, 10, 10)|var|float64
bop_12956 = relay.logical_and(call_12945.astype('bool'), var_12955.astype('bool')) # shape=(2, 10, 10)
bop_12959 = relay.logical_and(call_12946.astype('bool'), var_12955.astype('bool')) # shape=(2, 10, 10)
func_7605_call = mod.get_global_var('func_7605')
func_7611_call = mutated_mod.get_global_var('func_7611')
const_12971 = relay.const([-5.604064,5.860354,-7.113369,-3.729017,-3.990467,0.910346,-5.974305,4.377263,-7.837790,7.739971,-4.918751,-5.040459,9.276156,3.083931,-7.110910,8.916196,9.277353,6.763276,-6.769884,8.557472,-4.333038,5.004516,2.112756,-3.653448,-2.464240,3.076247,-4.183836,-4.974730,-0.254233,5.916289,-4.716435,-8.599317,9.545221,2.018223,3.727901,-3.958818,1.972374,-8.047490,-2.592069,-3.679569,-6.618325,3.018680,-4.216570,4.056456,2.871878,2.074865,3.652162,0.177272,5.855478,-4.411193,7.941422,5.251046,-0.524567,6.031316,-4.161370,9.296773,-6.757897,9.803269,1.500877,5.790621,2.581817,-7.700389,-0.732974,0.670778,4.328821,-0.022504,9.723415,2.712123,8.824974,-3.839069,2.176096,0.450258,5.422221,-7.580255,2.044508,0.697524,-7.917061,1.766044,-3.676172,-1.628745,-4.565557,-4.822605,-3.040153,-5.087078,8.121928,7.672526,-5.737261,-0.701442,-0.551617,-2.644907,-5.541754,-7.348579,-5.255358,-6.054717,4.929372,-0.281009,8.135539,2.955241,-2.840233,-7.866404,-1.015229,-3.641750,-5.710781,-7.367534,2.851293,-7.314535,1.382833,-3.902086,-3.106873,-3.255628,-6.813282,6.846317,1.581124,4.524420,-8.111623,1.628607,-1.096339,-1.963504,-4.449046,0.765469,4.633318,-4.382334,-9.751888,-7.852392,8.532017,-6.654587,7.355719,0.077311,-7.053054,9.772690,-0.690173,-9.825876,-0.586972,1.555876,0.249799,0.604183,-4.013551,9.164990,-1.913753,7.924381,-5.487472,5.932248,-9.281635,0.029743,-9.308774,4.252665,2.379301,5.098720,-7.626236,7.289012,3.868518,4.397521,-8.087489,-0.626678,-3.118003,-0.109446,-4.229147,7.407392,-9.692023,8.002182,5.734482,-5.753192,-1.442020,-3.407700,-7.242780,9.251081,-9.183419,-0.365716,1.768301,-2.203148,-9.331327,3.600485,-3.672249,2.608076,1.019898,1.105923,-2.198385,6.028840,2.228531,3.898704,1.671021,7.213652,2.103015,-9.616834,7.466280,0.440633,9.668307,-1.843977,1.787345,5.448966,-0.836228,8.899564,-6.680679,-0.970420,-7.435314,4.129249,-3.515581,-4.353262,-7.902231,-5.085025,0.078928,-6.022647,-1.078013,-0.862691,-3.682131,-2.122230,4.820538,7.626294,1.995514,9.235280,-3.679492,4.123901,-3.846422,-3.132323,1.421300,-7.005728,-9.414718,6.370936,5.798490,-4.839942,3.842319,-3.525085,-6.279279,-8.819058,9.586460,-7.605577,1.886813,-4.421290,3.202064,-1.300713,-2.564147,2.618962,5.016976,2.737355,-4.065329,5.779955,0.537119,-5.761996,4.215081,3.390974,7.862984,-7.595560,8.731195,-7.722605,-0.117162,0.283915,4.953122,4.508742,-7.788400,3.301924,0.238800,-3.962296,-5.854317,-2.492667,-5.053938,4.956178,8.804748,-7.268735,-6.543685,4.461826,7.589485,3.064839,2.609649,-4.965179,-2.318037,5.283890,-7.985388,-4.295302,-1.081613,-9.378769,-1.657690,-3.645862,-7.766360,-6.792089,3.684506,2.570831,4.670763,1.966203,3.576014,-2.641809,4.976291,1.842826,1.709100,4.550659,2.890793,-0.800648,0.264926,3.827592,3.102277,-6.790572,-2.832697,-0.831932,6.174639,-5.886092,4.937328,-5.387772,-6.702786,-3.603979,5.115897,-1.283492,8.863552,-1.596604,0.764312,-6.352643,3.771053,-4.599565,-8.074593,8.408307,-5.246465,3.176560,-6.119469,6.666939,3.796233,0.603212,7.314718,0.610218,-2.839411,5.362053,-1.624814,8.181986,-2.040492,9.119349,-2.488801,-4.121095,-7.042870,-0.191407,5.131615,-8.500496,3.901526,0.459521,7.188241,5.944242,-3.034805,4.486894,7.610768,2.775645,-5.856086,-6.972873,7.647309,-0.067115,-7.283597,8.937718,-5.574728,6.503557,3.534470,-4.203276,3.462564,-6.904351,-8.492556,-5.791825,-6.222910,4.402059,-2.707273,0.343622,1.534181,-8.767682,-5.263679,5.782683,0.384815,-2.820135,-0.310702,0.407469,6.020403,5.588149,9.043612,7.451572,8.127950,1.783486,-9.721999,-5.772998,-7.927004,-9.891306,-5.652034,9.672000,-3.835154,-7.935527,-2.419913,-5.126897,6.912680,3.510324,-1.787727,0.711732,0.259482,2.069783,0.907092,9.526147,-3.720613,1.507061,-6.529639,-0.223469,-2.354166,8.530996,-2.106272,-9.357794,9.694908,4.536320,-9.813745,-4.037137,7.560004,-9.717769], dtype = "float64")#candidate|12971|(400,)|const|float64
const_12972 = relay.const([-7,-4,9,1,-1,9,-3,-6,10,8,9,5,-3,8,-5,8,7,6,5,4,-6,-8,3,-6,5,1,5,-7,4,8,-6,1,2,9,-7,-5,-4,-2,4,-10,-3,4,8,8,-7,-1,-5,-6,2,-6,6,3,-2,-7,-4,-7,7,-7,-5,4,3,4,-2,7,-4,4,-2,-2,-2,3,3,5,5,4,8,9,5,-1,4,2,3,-9,-3,-1,9,2,-8,-3,-10,-1,5,4,-5,-9,-5,8,9,2,10,8,9,-5,-1,-10,-5,1,-2,4,-10,-6,-5,4,4,5,-1,-5,-5,9,-1,6,9,10,4,9,-6,-10,1,-3,10,-1,3,3,-8,-5,-3,-5,-10,-4,-8,10,-9,-4,-4,5,9,7,4,1,6,3,6,-4,4,1,-2,-5,-3,1,-10,-3,4,10,-4,2,-4,9,-4,6,-2,9,2,-5,4,2,4,-2,7,-6,10,9,4,6,3,-5,1,-9,7,7,9,7,5,2,1,1,8,7,-1,2,-5,7,1,10,-9,3,-8,-1,-2,-5,1,-4,9,2,4,-2,-3,6,6,-3,-3,-4,7,-4,-8,-3,6,-9,1,-2,7,4,4,3,-4,-6,-5,9,-6,2,-1,-5,2,-1,7,-6,7,4,9,-3,8,-3,-2,4,5,-3,10,-3,-4,-3,-8,-5,10,8,1,-4,3,-9,-10,-4,-10,1,-7,-2,1,-9,-8,-5,4,-10,7,3], dtype = "uint64")#candidate|12972|(280,)|const|uint64
const_12973 = relay.const([-1.403862,-8.355428,-1.182485,5.120544,-4.741719,7.104060,-6.696952,-3.654692,6.900442,-7.806131,5.977926,1.700191,0.194319,1.621305,2.274201,-2.388161,-5.182034,-8.181426,1.207037,6.180039,2.991916,-2.803086,3.261599,-1.376311,3.886662,9.643134,8.181924,0.996706,6.309267,5.640428,7.619198,-8.649145,9.573140,-7.349368,-3.164527,-9.609958,-9.776062,2.264546,4.672129,-8.445698,3.138211,-6.060589,-2.446608,1.854221,-6.770418,-2.195863,-3.291783,-1.511620,-6.810775,-8.997859,-9.485585,-3.831558,3.763804,-0.477164,-5.533237,3.877656,-8.426100,-6.953695,2.413549,-2.131920,-3.592079,4.389616,5.932754,-4.766015,-2.912916,-6.669157,3.175818,2.495115,-9.334438,-8.026102,5.423418,-3.985201,4.012921,-1.892057,1.099920,-2.626771,-7.318945,-7.805614,5.549720,9.436434,-0.502160,-3.466567,-8.980670,-7.868954,5.668033,7.788649,1.200479,-6.936261,-7.606018,1.168848,5.636552,-6.825845,-7.765615,2.323604,3.623181,2.418358,-5.623987,-0.109568,-7.748219,-8.416705,2.872419,-7.018102,1.145810,9.403945,0.071073,4.604618,-5.319454,-3.492277,6.803982,3.413303,-9.472230,-2.952848,-9.452635,-2.980989,1.042978,2.008464,-4.692485,0.313413,-4.419788,-5.542928,-8.235388,0.169977,6.133406,9.751215,1.059198,9.208484,9.232617,4.955718,-0.136745,-5.831195,-6.047025,-1.258358,3.848295,-2.171443,-8.993170,-8.031264,8.407055,-3.590230,3.811973,3.029879,-1.874379,9.309333,-8.568225,8.157625,-1.366528,-4.637860,2.695042,2.064527,7.083792,2.055971,-2.268529,-1.131699,4.705311,-0.810579,-7.116648,1.323062,6.584761,-7.932351,8.113779,-0.198065,-3.039547,-0.799102,-3.106907,-6.203160,-1.173847,5.535519,1.487004,-7.779185,-6.828414,-0.500771,-7.386443,4.635391,-7.456531,4.105440,-6.057708,5.412423,-7.444315,-0.074722,8.614548,-5.283980,-2.032612,0.336779,8.309073,-9.086918,-6.215151,-1.489271,9.729795,-2.887111,-3.555162,5.417881,-4.120010,5.187341,5.421952,1.891141,-7.960193,-4.158326,7.767875,1.969805,7.719617,8.694254,-1.695889,-6.679723,4.284798,8.852937,-1.931012,-9.920911,2.004207,0.735560,-8.094825,5.634810,3.392277,9.026487,9.642460,1.185760,8.309716,8.483624,1.091486,3.834563,-5.725323,-7.137458,3.413581,1.938573,-1.487902,1.702798,7.458842,3.737447,-3.207617,-4.737923,1.829106,-5.350284,-1.697780,-2.688620,0.689811,-4.450156,-4.190492,-0.274625,-6.002483,-1.151779,7.720464,7.517164,7.282715,2.181421,2.072824,3.074418,8.853810,7.066002,4.667450,1.218511,5.828735,4.142941,-5.470476,-0.028219,8.487933,8.570000,-7.966737,-9.987945,-8.666956,-1.126252,0.438215,-8.953210,7.521383,-1.741414,-2.142646,-5.377862,0.934662,7.150266,1.828035,-7.088288,3.540168,1.339163,-2.211367,0.277385,7.996448,3.787748,8.339704,-7.734431,0.911717,-8.889321,-1.200161,-2.494806,-4.323658,-7.595562,1.358728,-5.737269,-7.236944,-7.240607,5.351372,2.659047,7.954084,3.535333,3.883938,-5.710775,-7.667734,-9.584057,2.505901,8.211750,-5.601425,6.636774,-6.961090,-5.464773,-7.369756,-5.967906,-7.042045,-6.047647,-4.640961,5.586698,2.763465,-3.164914,-1.970656,9.698076,0.723228,5.543128,-0.161059,8.182045,-0.126628,2.045161,7.100665,2.981445,-0.581551,6.601820,7.676578,-4.848868,-4.567681,0.756296,2.312652,-0.781686,3.666176,-2.522837,3.071864,-6.575038,-7.120812,-8.948033,0.571525,3.790807,6.500616,-6.522835,6.529926,-1.027944,-8.518402,-9.191578,-7.209504,-5.902969,-7.501494,8.161467,5.474067,-1.160051,2.457353,7.696106,-9.631535,-0.552957,0.280283,-8.753946,7.384099,6.066416,-7.745498,3.595718,-7.617157,-5.506808,8.587857,-9.330292,-5.884012,-8.580293,6.330110,-1.298767,-7.039871,-4.898462,-0.499893,0.674911,0.296630,8.092593,-5.608083,-4.712824,-6.093187,-8.781915,-3.380151,-1.375021,4.442601,-1.275756,-2.731725,-4.784649,-6.205180,1.229105,7.155501,-7.871893,1.954566,1.930379,2.553821,-5.687113,-9.526476,3.033129,-1.757017,3.965156,-6.675592,-2.661087,8.427920,7.060947,8.091482,-9.175427,5.602657,2.613287,-6.536392,8.769807,-3.640576,5.344064,-8.794151,2.294700,2.839286,-1.751923,5.016076,-4.120776,6.413529,-4.276194,-4.668677,1.362687,3.004077,-4.644590,5.615107,1.339100,-1.531522,4.583749,1.567997,9.270345,8.794553,-6.223443,-7.977584,2.062637,1.069724,2.820499,-3.840631,0.190071,8.045578,6.072496,7.131431,7.528497,-2.636977,-9.831391,4.427566,-6.020397,7.352024,2.762751,7.799912,3.262539,-0.721182,5.763644,-6.478727,1.329574,-0.596365,-5.552667], dtype = "float32")#candidate|12973|(448,)|const|float32
const_12974 = relay.const([-0.485576,-0.104700,2.397739,9.543157,5.635649,5.453735,1.067095,7.524221,7.683868,7.652784,-9.812344,8.060577,5.070435,-4.951495,3.952249,-1.636773,-3.844707,-1.532373,2.399769,-1.965148,-4.470902,-2.637709,5.105385,-4.675649,-9.577483,-4.091034,-0.666669,3.428714,6.994493,-3.652909,-5.146263,4.596602,6.782963,-0.105570,7.223362,-7.806346,-0.371701,7.533266,-4.997930,-3.370348,0.475532,5.248319,7.057608,-0.338523,3.053619,5.015796,0.867811,-8.367997,-6.476235,-4.692859,2.861267,-9.138397,7.379605,9.512536,4.678658,-4.643479,-2.281013,-5.488701,-3.878279,0.315314,6.365989,9.637455,3.939444,-6.446365,3.022484,8.241082,4.535272,-1.589716,0.171955,-2.285036,-8.150762,-8.215249,9.034062,-8.909151,7.116488,5.280420,-3.502257,9.116938,-6.162133,-3.278742,-5.237159,-0.008351,6.253532,-2.452179,2.488309,6.814669,4.450885,-8.425332,-7.634160,9.868542,-5.388949,-3.049021,9.800500,-4.377418,3.630612,1.582027,-5.207402,6.492035,8.915212,5.006765,0.075420,-6.925278,-1.687287,6.819117,7.946022,-8.104708,7.228186,-8.775955,-0.135652,-1.119550,9.382573,-0.853882,8.943256,3.708559,5.538587,3.360208,9.252743,-9.279718,5.401512,-2.067052,-4.889307,-4.506668,-7.353108,-7.527446,-8.154929,-0.154236,9.694501,0.103267,2.078870,8.728170,5.244765,4.426498,-2.966020,-3.266700,9.260263,-4.997681,9.372462,9.462379,1.431717,8.941421,-5.301183,-2.931296,-5.663618,-4.879997,-3.301158,-8.604118,5.156039,3.023323,5.538372,2.149383,-3.058043,-3.517004,-7.241066,5.625505,-1.026649,3.720399,1.082932,-6.626672,-2.407890,4.748410,-9.482828,-3.120315,4.433842,3.013999,-7.867965,8.460776,-3.820787,-7.541865,5.886596,-0.926190,-7.151555,-7.825836,3.038114,5.807779,2.573709,2.727974,2.895068,7.075114,1.781761,1.653131,9.590077,-5.524307,8.572544,0.030750,3.228403,-6.839212,3.355757,8.594211,7.340753,-8.565184,1.625302,-3.849035,-3.543400,6.993592,-3.280648,6.732954,9.120489,5.750094,-6.634275,0.843988,-7.798015,-6.435568,-1.785868,4.445024,-1.471945,-7.088545,2.105539,-1.251799,4.652328,5.948542,6.831419,4.935137,-1.862997,9.942540,9.817155,-0.120188,-0.476638,-8.868466,-0.914601,-9.962237,2.807782,-1.899992,7.444300,-9.999528,-8.699960,-9.459000,-1.520650,-0.494755,-9.238935,-1.077219,-2.716630,4.945396,1.038178,4.120890,3.945672,-8.220906,4.491167,9.440932,-4.787033,6.807960,7.753434,-8.154479,8.817465,0.993874,-7.376868,-2.853991,-7.771842,4.904539,2.864775,-7.880545,-7.903801,5.074022,6.681534,-0.222881,6.832113,5.727358,3.997108,-6.613117,-0.777697,-2.321971,0.754306,-5.354427,-3.066257,3.803341,-0.882353,1.548646,3.797669,-2.175723,1.008502,-1.312730,-4.800609,-3.457275,5.367193,5.380784,-5.901561,-0.547255,-8.488891,7.383573,-8.249646,-0.567201,-8.327252,7.177980,-6.227426,5.447800,-5.178478,-3.210000,0.949425,-7.235129,-1.269748,-1.495389,4.385143,-6.629172,9.138838,-9.780593,1.441853,0.947611,-0.101412,4.081465,-9.019158,2.362439,-9.546621,-6.315319,-0.839797,-9.391123,-2.658517,6.297573,4.186650,3.421940,8.235637,-0.920763,-8.461851,0.889052,-8.387707,0.145750,5.275759,2.250734,1.754695,3.773816,-3.900209,-7.489134,-6.378565,-9.747152,9.666991,9.094931,4.252503,2.203156,7.467202,2.679662,5.182391,-3.284360,9.191802,-0.815630,1.315985,-8.050669,1.642537,-8.792529,-0.263054,7.070071,-4.082457,-9.934491,-6.205156,9.480294,-8.048515,0.623284,-1.258916,-1.459018,4.964072,-4.344600,-1.915116,-4.226772,3.934117,-6.754117,2.914486,7.115295,-2.962187,-5.743251,-9.271574,-4.134705,-0.274505,-9.948647,0.109432,-6.062211,-1.101670,-7.179645,6.834236,-0.097034,3.448621,-8.592472,7.674633,4.031353,2.191832,-1.110761,5.091423,7.233510,8.460801,-5.922487,-1.456337,5.779778,7.455851,-6.227832,4.807001,5.783041,2.535153,3.175056,-0.596877,-3.806492,-6.411066,2.721602,6.290591,3.270001,-4.206652,4.601961,-7.791561,3.884516,-5.369159,-9.988597,1.105367,8.208655,0.571695,3.389154,7.682258,-8.854160,-4.305211,7.517256,-5.489972,-1.657341,6.084460,4.135869,8.455415,5.503590,-4.124768,3.223312,-2.752439,-5.302252,5.310094,9.038455,3.220574,9.602910,3.355320,2.294449,3.010278,-8.615432,-7.592873,9.552790,6.462679,8.111568,-0.135449,5.542228,1.280465,9.221327,9.189991,9.651048,-3.610318,-2.707996,-7.185253,3.192266,-1.590481,-4.388023,6.260572,-3.106398,-8.782670,6.644702,-8.735483,8.292318,-2.769805,-0.884439,2.034156,0.504023,-8.176675,4.947031,6.210252,0.135186,3.796308,-2.644568,7.019903,5.650310,6.367590,-8.064322,7.177242,9.599364,-5.465610,9.672382,-0.325992,6.049739,-0.043091,6.152644,5.584930,0.295728,-0.880610,-5.353021,-9.316394,5.703665,-9.789652,7.071674,-5.981624,9.374748,0.703648,-6.079410,9.376508,-3.614355,5.275951,-0.885409,-3.344232,3.355229,9.644449,-7.666668,5.415672,0.330395,-4.525178,9.414103,-2.767956,7.663970,5.708247,1.603902,-3.463889,-6.535107,3.618871,-6.317370,5.677417,-4.935274,9.034145,-6.114949,-2.245553,-4.789316,9.587071,2.860333,7.566944,9.372660,2.699001,0.660728,-7.974784,5.259948,-4.299006,-4.509013,1.326799,5.535361,7.766444,6.883961,5.069735,-1.311034,6.724085,-3.775575,6.188648,3.863905,-9.558811,-1.569931,-5.470626,-6.383679,4.304452,-9.375584,7.009829,-1.329994,-9.673555,0.692775,8.807369,-5.194483,8.100748,4.661403,-2.814260,7.275387,-7.905957,4.120726,5.915814,6.838644,-6.794913,3.352883,5.388041,4.413841,4.332357,-5.664356,-0.432575,9.038864,0.226658,-8.536639,9.027622,4.478237,0.320225,9.716330,-2.491207,-6.289857,-7.788968,0.945243,7.583632,6.341991,0.701309,7.289449,-4.846168,6.566417,-6.576976,3.721467,-4.289893,9.217200,-1.376297,-4.098329,4.694679,2.340407,2.769315,-0.342133,1.406383,2.950628,5.186854,5.344675,-6.536427,9.908196,-6.635403,-8.061694,9.843311,3.663960,-1.648201,0.978137,-7.982119,-3.266640,5.025169,-1.970063,-2.072057,4.098688,-8.057808,-9.888820,5.883080,3.411208], dtype = "float64")#candidate|12974|(600,)|const|float64
call_12970 = relay.TupleGetItem(func_7605_call(relay.reshape(const_12971.astype('float64'), [400,]), relay.reshape(const_12972.astype('uint64'), [280,]), relay.reshape(const_12973.astype('float32'), [448, 1]), relay.reshape(const_12974.astype('float64'), [600,]), ), 11)
call_12975 = relay.TupleGetItem(func_7611_call(relay.reshape(const_12971.astype('float64'), [400,]), relay.reshape(const_12972.astype('uint64'), [280,]), relay.reshape(const_12973.astype('float32'), [448, 1]), relay.reshape(const_12974.astype('float64'), [600,]), ), 11)
func_5577_call = mod.get_global_var('func_5577')
func_5579_call = mutated_mod.get_global_var('func_5579')
call_12981 = func_5577_call()
call_12982 = func_5577_call()
func_7097_call = mod.get_global_var('func_7097')
func_7099_call = mutated_mod.get_global_var('func_7099')
call_13007 = relay.TupleGetItem(func_7097_call(), 0)
call_13008 = relay.TupleGetItem(func_7099_call(), 0)
func_11821_call = mod.get_global_var('func_11821')
func_11824_call = mutated_mod.get_global_var('func_11824')
var_13014 = relay.var("var_13014", dtype = "int16", shape = (55, 15))#candidate|13014|(55, 15)|var|int16
call_13013 = relay.TupleGetItem(func_11821_call(relay.reshape(call_12970.astype('int16'), [1, 165]), relay.reshape(var_13014.astype('int16'), [825,]), ), 6)
call_13015 = relay.TupleGetItem(func_11824_call(relay.reshape(call_12970.astype('int16'), [1, 165]), relay.reshape(var_13014.astype('int16'), [825,]), ), 6)
func_9664_call = mod.get_global_var('func_9664')
func_9666_call = mutated_mod.get_global_var('func_9666')
call_13048 = relay.TupleGetItem(func_9664_call(), 1)
call_13049 = relay.TupleGetItem(func_9666_call(), 1)
func_6479_call = mod.get_global_var('func_6479')
func_6482_call = mutated_mod.get_global_var('func_6482')
call_13050 = relay.TupleGetItem(func_6479_call(relay.reshape(const_12971.astype('float64'), [4, 10, 10])), 0)
call_13051 = relay.TupleGetItem(func_6482_call(relay.reshape(const_12971.astype('float64'), [4, 10, 10])), 0)
output = relay.Tuple([bop_12956,call_12970,const_12971,const_12972,const_12973,const_12974,call_12981,call_13007,call_13013,var_13014,call_13048,call_13050,])
output2 = relay.Tuple([bop_12959,call_12975,const_12971,const_12972,const_12973,const_12974,call_12982,call_13008,call_13015,var_13014,call_13049,call_13051,])
func_13068 = relay.Function([var_12955,var_13014,], output)
mod['func_13068'] = func_13068
mod = relay.transform.InferType()(mod)
mutated_mod['func_13068'] = func_13068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13068_call = mutated_mod.get_global_var('func_13068')
var_13070 = relay.var("var_13070", dtype = "float64", shape = (2, 10, 10))#candidate|13070|(2, 10, 10)|var|float64
var_13071 = relay.var("var_13071", dtype = "int16", shape = (55, 15))#candidate|13071|(55, 15)|var|int16
call_13069 = func_13068_call(var_13070,var_13071,)
output = call_13069
func_13072 = relay.Function([var_13070,var_13071,], output)
mutated_mod['func_13072'] = func_13072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7928_call = mod.get_global_var('func_7928')
func_7929_call = mutated_mod.get_global_var('func_7929')
call_13076 = func_7928_call()
call_13077 = func_7928_call()
output = relay.Tuple([call_13076,])
output2 = relay.Tuple([call_13077,])
func_13083 = relay.Function([], output)
mod['func_13083'] = func_13083
mod = relay.transform.InferType()(mod)
mutated_mod['func_13083'] = func_13083
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13083_call = mutated_mod.get_global_var('func_13083')
call_13084 = func_13083_call()
output = call_13084
func_13085 = relay.Function([], output)
mutated_mod['func_13085'] = func_13085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4227_call = mod.get_global_var('func_4227')
func_4228_call = mutated_mod.get_global_var('func_4228')
call_13091 = relay.TupleGetItem(func_4227_call(), 0)
call_13092 = relay.TupleGetItem(func_4228_call(), 0)
func_10373_call = mod.get_global_var('func_10373')
func_10376_call = mutated_mod.get_global_var('func_10376')
const_13106 = relay.const([-5.314399,9.753807,8.167032,-2.538570,2.037018,-9.108183,-5.560919,4.996623,9.830848,0.941239,5.824237,-2.817984,7.019164,-9.867195,-5.463242,6.006029,-6.028825,9.474935,-0.726686,9.920878,-3.610881,-6.551787,-5.249515,8.074966,-7.438989,9.214970,4.570888,-9.416730,2.723772,6.857298,-5.761599,-2.841050,1.264230,-3.795303,5.863166,-1.850936,-7.368287,-2.577921,-0.145940,-4.087429,-4.531952,-4.399106,6.309545,4.912031,0.100644,-7.922881,8.174337,-5.819773,3.897105,-0.301325,-3.453806,-6.446911,6.812347,-6.108160,-3.325181,8.102781,-7.380145,7.297203,-8.645196,-2.570818,5.989260,4.381833,-4.656569,-4.226178,1.305124,-5.412188,7.607950,-9.103877,-5.614623,-4.034982,9.361950,5.170888,8.298721,-4.992698,4.106289,4.899731,1.189686,5.638595,-8.931057,8.797602,-6.932619,-9.972134,2.748673,7.759736,7.831045,-7.812826,4.362384,-8.156739,-2.010946,-6.514613,-3.955702,7.405517,-2.161154,4.615735,-5.101116,-2.948163,-7.244679,-1.143906,2.942953,9.294970,2.070038,-9.559776,-3.887960,0.791407,1.787084,-0.051176,6.423528,9.703327,4.793041,-9.495680,-4.218054,-0.208619,6.495542,-1.255209,-7.250661,9.942533,9.819903,-5.704223,5.635474,2.588729,7.939588,-8.882928,4.480894,0.880755,-4.134422,-3.741968,-9.372728,6.364887,3.606206,3.357663,-4.612012,3.990265,-5.430105,1.846441,3.893633,-0.646505,-6.760405,1.743159,-2.793160,-8.381841,-7.826102,8.712613,-7.596479,8.401120,-7.501006,2.632674,0.513599,3.317081,9.550538,1.699779,5.704578,6.491719,-7.595127,1.529595,8.962921,2.762295,-7.952554,4.593486,-7.038278,-1.802306,2.006964,2.531235,-9.872186,-6.082903,2.403284,-2.125399,6.898601,-6.567395,-4.855984,-4.398160,-1.443269,0.237975,1.016225,5.162906,2.303229,-8.104139,2.830980,-0.453709,-0.297040,2.912780,-8.861476,-7.535141,-4.965754,-9.530086,-3.103155,-7.370606,-0.413146,2.052434,-6.316670,4.400846,-1.592646,-6.836865,0.838163,9.733632,2.764278,5.037729,-4.229807,4.405423,4.935335,0.138777,9.158460,-1.974463,-2.259639,1.507956,-4.024210,-9.654854,-6.442217,-4.968943,3.563588,-1.456765,2.326696,8.023448,8.037373,-1.104494,-7.547439,1.740668,7.458635,9.165529,9.331553,4.152824,-4.229428,4.889042,-7.505161,-5.968975,3.154176,9.929822,4.772213,3.712771,8.288995,7.170993,5.370020,3.136833,-6.972167,-6.985100,6.435205,8.913723,-0.219904,3.360703,-2.850717,-1.373762,-4.568289,-6.934902,-5.450060,-6.147390,1.192604,9.639178,-9.922966,-0.844186,-4.551530,3.408412,-5.507153,9.351374,3.023150,9.167429,-5.595486,7.473084,3.118906,-9.159192,3.874946,-9.984893,-1.238327,-4.009026,-8.840454,1.383622,9.132050,4.747208,2.164120,-8.699105,0.902613,9.323390,-7.353350,-8.910444,-6.421435,9.716497,7.173294,3.923019,-7.653989,8.683900,-7.779708,9.184473,9.636081,7.178716,5.781030,5.764546,4.753823,-7.048644,9.430491,-6.145236,-3.702739,-0.512468,0.155740,1.662545,3.653274,-8.713166,-9.773341,3.043944,-9.045840,-8.423584,7.865583,-8.353761,-9.123812,-5.084426,0.923167,-0.880964,-0.478724,-6.316478,-5.829514,0.689768,-0.021903,3.348950,1.129392,-9.490806,5.813465,1.948134,-4.736184,3.999660,9.554286,-7.040483,-9.072998,-0.895861,7.385990,-3.422015,-8.034062,7.651351,-3.692132,3.928239,-4.092713,5.912568,6.885535,-7.811588,2.051114,-6.255644,7.498690,1.431896,7.148077,-5.742623,-6.636677,-5.488055,9.094428,8.288700,-1.235158,2.913958,-9.263710,-0.774964,-4.412294,0.886710,1.300389,-1.551372,0.149074,-0.282116,0.347457,5.653505,-9.552459,-1.175749,-2.087669,0.472229,4.706797,6.169836,1.836945,7.239268,-9.866624,4.048267,-1.094574,-5.203371,-7.482154,0.386931,6.302862,1.079928,-0.716111,3.757707,-0.993494,-3.582817,-1.729848,6.401757,0.370152,0.354951,-8.539764,7.570313,-8.936088,-5.563576,0.478279,-0.342077,-4.965355,-6.579931,2.708046,0.784001,-5.431786,3.169740,5.974188,-2.238145,3.651333,-5.265513,6.078481,7.787784,1.184182,-3.626496,4.878449,-3.637191,-1.018101,-5.897615,-7.998103,9.176456,4.339002,9.926276,-5.085614,-1.178830,4.738409,3.792667,-4.156836,-3.505643,-3.946404,-8.026721,0.075179,1.618990,1.329237,-5.735635,-6.994093,-1.348171,-2.577614,-6.579281,-8.204403,3.953492,-2.724343,-2.370732,3.578140,-1.062891,5.710589,1.990490,4.287444,-4.455579,-4.433097,9.923942,2.729655,5.039838,9.467918,-3.177305,-1.968445,-9.933484,-6.182939,6.693627,2.377393,9.822825,3.472111,-0.774699,1.186961,7.278894,4.126854,-3.054351,6.763365,-3.039552,-4.291654,-3.825841,-0.699328,4.421863,7.296713,-2.367481,-6.304429,5.957659,-2.613035,4.288082,-3.029418,-6.513648,7.934045,-7.884888,-8.915196,3.689606,2.243153,0.816776,-9.722226,-5.724478,7.750249,9.921308,-1.698344,3.144083,-7.507214,6.787104,-2.109903,-4.761793,-8.501636,-2.105352,8.626512,2.409422,4.578683,5.237385,4.193532,7.334803,-9.477949,2.148112,3.935506,-6.560343,7.703654,-6.652948,7.634064,5.136805,-3.740117,-8.407509,5.785512,-9.703407,-3.990422,2.164340,-8.168917,-0.266131,1.610675,7.285521,0.760596,-5.234085,3.627602,-5.686279,9.887103,5.303333,1.146080,9.889560,5.217264,9.059684,3.461870,-4.899562,7.765452,4.409659,-7.136432,2.290622,-1.140297,-4.654615,-3.412890,-7.549117,-2.062008,2.310935,8.657521,-8.150692,1.878460,-8.444647,-4.711875,-5.630597,3.566211,-5.502931,-5.815414,9.810232,9.736645,1.915696,-0.240673,9.267119,8.585257,-1.078363,-8.023154,8.729594,-6.915427,-8.636239,-0.637553,-1.409631,-6.450668,0.615704,-8.671185,5.183192,-7.063379,-4.275896,-4.888428,6.232862,-6.482594,-3.891477,8.395099,-7.734068,3.051372,-6.276074,5.751375,-3.719534,-7.174877,4.291138,-5.852288,-7.343494,2.204612,-7.075005,4.537652,4.477385,8.050856,-4.469933,0.034367,5.328538,4.638762,7.446703,-7.212763,0.983987,0.835715,-4.323284,2.112899,8.326898,8.268361,0.384777,4.789440,-7.443008,-3.273411,5.205215,-5.500446,1.511008,7.633543,-2.370016,-8.273642,-3.581374,-3.732128,6.846318,8.294020,-7.559256,-0.163629,5.554775,-8.980123,8.355659,-4.445843,9.929404,8.803305,7.423884,0.969112,-8.661643,8.578764,7.586068,1.999279,6.052147,1.043597,0.434541,8.160207,-3.862717,0.322688,8.383082,-7.127809,-8.609333,0.839145,-9.780961,4.569200,-4.447920,2.049530,8.418427,-9.338316,-7.797797,-5.195007,-0.050681,-2.211645,-1.960413,-4.664111,-9.064874,-3.265158,-6.915879,-3.482162,-7.295801,8.695414,-6.036568,-3.503927,-1.912894,-6.836543,1.189123,-5.024336,1.474972,-0.001789,-3.379069,5.660106,2.016872,0.007647,5.807948,4.705790,-0.029868,-7.554766,0.514199,-3.559412,9.034424,-0.772631,6.842263,-1.504972,-4.099187,-9.093543,1.535636,3.238640,5.509416,-8.750898,-2.466768,-5.791200,0.493043], dtype = "float32")#candidate|13106|(672,)|const|float32
call_13105 = relay.TupleGetItem(func_10373_call(relay.reshape(const_13106.astype('float32'), [7, 16, 6])), 0)
call_13107 = relay.TupleGetItem(func_10376_call(relay.reshape(const_13106.astype('float32'), [7, 16, 6])), 0)
func_11253_call = mod.get_global_var('func_11253')
func_11254_call = mutated_mod.get_global_var('func_11254')
call_13117 = relay.TupleGetItem(func_11253_call(), 1)
call_13118 = relay.TupleGetItem(func_11254_call(), 1)
uop_13121 = relay.erf(call_13105.astype('float64')) # shape=(7, 16, 6)
uop_13123 = relay.erf(call_13107.astype('float64')) # shape=(7, 16, 6)
uop_13129 = relay.log(uop_13121.astype('float32')) # shape=(7, 16, 6)
uop_13131 = relay.log(uop_13123.astype('float32')) # shape=(7, 16, 6)
output = relay.Tuple([call_13091,const_13106,call_13117,uop_13129,])
output2 = relay.Tuple([call_13092,const_13106,call_13118,uop_13131,])
func_13132 = relay.Function([], output)
mod['func_13132'] = func_13132
mod = relay.transform.InferType()(mod)
output = func_13132()
func_13133 = relay.Function([], output)
mutated_mod['func_13133'] = func_13133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5577_call = mod.get_global_var('func_5577')
func_5579_call = mutated_mod.get_global_var('func_5579')
call_13153 = func_5577_call()
call_13154 = func_5577_call()
func_3695_call = mod.get_global_var('func_3695')
func_3700_call = mutated_mod.get_global_var('func_3700')
var_13160 = relay.var("var_13160", dtype = "float32", shape = (320,))#candidate|13160|(320,)|var|float32
const_13161 = relay.const([-6,8,-6,3,-4,-9,-8,4,10,4,7,6,-5,-10,-9,-8,-1,10,-1,-5,-9,-9,-9,-5,-6,2,2,-5,-10,-6,6,-3,10,-4,10,7,6,-6,-9,-5,-9,-10,-6,10,10,9,9,2,-7,10,8,7,-3,8,-4,-7,-1,-8,10,4,-5,7,-7,3,7,-3,1,8,3,-6,-10,-1,-7,-7,6,-8,-8,-5,6,-9,1,10,2,-8,6,1,6,-7,1,-2,9,8,-7,-2,-10,7,-3,-7,-7,-9,8,10,-9,9,-3,7,-2,-1,9,-3,-6,-4,9,5,4,-8,-3,-8,-5,4,-7,4,-7,10,10,-7,-4,-9,-10,-7,-8,9,-5,-6,4,-10,3,2,-1,-8,-4,9,-5,10,-3,-2,-4,-4,9,-9,2,-6,3,4,8,9,6,1,6,-7,-8,4,1,9,8], dtype = "int16")#candidate|13161|(165,)|const|int16
call_13159 = relay.TupleGetItem(func_3695_call(relay.reshape(var_13160.astype('float32'), [5, 4, 16]), relay.reshape(const_13161.astype('int16'), [11, 15]), relay.reshape(var_13160.astype('float32'), [5, 4, 16]), ), 5)
call_13162 = relay.TupleGetItem(func_3700_call(relay.reshape(var_13160.astype('float32'), [5, 4, 16]), relay.reshape(const_13161.astype('int16'), [11, 15]), relay.reshape(var_13160.astype('float32'), [5, 4, 16]), ), 5)
output = relay.Tuple([call_13153,call_13159,var_13160,const_13161,])
output2 = relay.Tuple([call_13154,call_13162,var_13160,const_13161,])
func_13182 = relay.Function([var_13160,], output)
mod['func_13182'] = func_13182
mod = relay.transform.InferType()(mod)
var_13183 = relay.var("var_13183", dtype = "float32", shape = (320,))#candidate|13183|(320,)|var|float32
output = func_13182(var_13183)
func_13184 = relay.Function([var_13183], output)
mutated_mod['func_13184'] = func_13184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7659_call = mod.get_global_var('func_7659')
func_7661_call = mutated_mod.get_global_var('func_7661')
call_13296 = relay.TupleGetItem(func_7659_call(), 0)
call_13297 = relay.TupleGetItem(func_7661_call(), 0)
output = call_13296
output2 = call_13297
func_13314 = relay.Function([], output)
mod['func_13314'] = func_13314
mod = relay.transform.InferType()(mod)
output = func_13314()
func_13315 = relay.Function([], output)
mutated_mod['func_13315'] = func_13315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9275_call = mod.get_global_var('func_9275')
func_9276_call = mutated_mod.get_global_var('func_9276')
call_13346 = relay.TupleGetItem(func_9275_call(), 0)
call_13347 = relay.TupleGetItem(func_9276_call(), 0)
func_5023_call = mod.get_global_var('func_5023')
func_5024_call = mutated_mod.get_global_var('func_5024')
call_13353 = func_5023_call()
call_13354 = func_5023_call()
output = relay.Tuple([call_13346,call_13353,])
output2 = relay.Tuple([call_13347,call_13354,])
func_13385 = relay.Function([], output)
mod['func_13385'] = func_13385
mod = relay.transform.InferType()(mod)
mutated_mod['func_13385'] = func_13385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13385_call = mutated_mod.get_global_var('func_13385')
call_13386 = func_13385_call()
output = call_13386
func_13387 = relay.Function([], output)
mutated_mod['func_13387'] = func_13387
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10473_call = mod.get_global_var('func_10473')
func_10475_call = mutated_mod.get_global_var('func_10475')
call_13433 = relay.TupleGetItem(func_10473_call(), 0)
call_13434 = relay.TupleGetItem(func_10475_call(), 0)
output = relay.Tuple([call_13433,])
output2 = relay.Tuple([call_13434,])
func_13439 = relay.Function([], output)
mod['func_13439'] = func_13439
mod = relay.transform.InferType()(mod)
output = func_13439()
func_13440 = relay.Function([], output)
mutated_mod['func_13440'] = func_13440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9390_call = mod.get_global_var('func_9390')
func_9392_call = mutated_mod.get_global_var('func_9392')
call_13453 = relay.TupleGetItem(func_9390_call(), 0)
call_13454 = relay.TupleGetItem(func_9392_call(), 0)
var_13461 = relay.var("var_13461", dtype = "float32", shape = (10, 10, 10))#candidate|13461|(10, 10, 10)|var|float32
bop_13462 = relay.left_shift(call_13453.astype('uint32'), var_13461.astype('uint32')) # shape=(10, 10, 10)
bop_13465 = relay.left_shift(call_13454.astype('uint32'), var_13461.astype('uint32')) # shape=(10, 10, 10)
output = bop_13462
output2 = bop_13465
func_13466 = relay.Function([var_13461,], output)
mod['func_13466'] = func_13466
mod = relay.transform.InferType()(mod)
var_13467 = relay.var("var_13467", dtype = "float32", shape = (10, 10, 10))#candidate|13467|(10, 10, 10)|var|float32
output = func_13466(var_13467)
func_13468 = relay.Function([var_13467], output)
mutated_mod['func_13468'] = func_13468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8763_call = mod.get_global_var('func_8763')
func_8765_call = mutated_mod.get_global_var('func_8765')
call_13511 = relay.TupleGetItem(func_8763_call(), 0)
call_13512 = relay.TupleGetItem(func_8765_call(), 0)
output = relay.Tuple([call_13511,])
output2 = relay.Tuple([call_13512,])
func_13522 = relay.Function([], output)
mod['func_13522'] = func_13522
mod = relay.transform.InferType()(mod)
output = func_13522()
func_13523 = relay.Function([], output)
mutated_mod['func_13523'] = func_13523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13385_call = mod.get_global_var('func_13385')
func_13387_call = mutated_mod.get_global_var('func_13387')
call_13549 = relay.TupleGetItem(func_13385_call(), 1)
call_13550 = relay.TupleGetItem(func_13387_call(), 1)
func_4654_call = mod.get_global_var('func_4654')
func_4656_call = mutated_mod.get_global_var('func_4656')
call_13564 = func_4654_call()
call_13565 = func_4654_call()
output = relay.Tuple([call_13549,call_13564,])
output2 = relay.Tuple([call_13550,call_13565,])
func_13566 = relay.Function([], output)
mod['func_13566'] = func_13566
mod = relay.transform.InferType()(mod)
mutated_mod['func_13566'] = func_13566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13566_call = mutated_mod.get_global_var('func_13566')
call_13567 = func_13566_call()
output = call_13567
func_13568 = relay.Function([], output)
mutated_mod['func_13568'] = func_13568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8310_call = mod.get_global_var('func_8310')
func_8311_call = mutated_mod.get_global_var('func_8311')
call_13679 = func_8310_call()
call_13680 = func_8310_call()
output = relay.Tuple([call_13679,])
output2 = relay.Tuple([call_13680,])
func_13692 = relay.Function([], output)
mod['func_13692'] = func_13692
mod = relay.transform.InferType()(mod)
mutated_mod['func_13692'] = func_13692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13692_call = mutated_mod.get_global_var('func_13692')
call_13693 = func_13692_call()
output = call_13693
func_13694 = relay.Function([], output)
mutated_mod['func_13694'] = func_13694
mutated_mod = relay.transform.InferType()(mutated_mod)
const_13723 = relay.const([[[-0.732884,-4.501090,-7.317897,6.933990,-0.752429,4.614037,-8.141668,-3.092858,1.514560,-4.375983,-5.997525]],[[7.836652,-4.590708,-2.035057,6.939810,2.686025,0.772970,-8.144618,-0.929042,-1.028440,3.043240,2.456044]],[[7.493671,-2.028750,4.499202,-2.334527,-4.775269,-5.844109,9.340098,-1.700187,-8.271071,-4.999723,9.592113]],[[-4.978926,-2.665638,-3.876366,-2.290123,-4.733422,1.577002,-9.547815,5.645522,6.921802,-4.443621,-5.456258]],[[-4.901631,-6.689778,-9.531250,-6.998295,8.874423,-9.957434,-1.726739,6.829213,-5.999311,-2.114281,-5.425581]],[[-2.811464,-8.540876,5.388856,0.781014,-3.682015,9.624089,-2.925207,6.541261,5.486060,7.251328,9.377803]],[[5.498430,-1.016209,-1.670293,0.610073,8.863451,-9.397622,0.434895,-1.446030,-1.736892,-3.637588,3.188430]],[[7.602469,-1.625196,5.561763,-4.379704,4.976631,0.602729,7.403913,-9.932475,8.673129,-2.200050,5.395221]],[[1.595187,-7.997158,-8.740777,2.736236,-4.080121,6.715966,-7.173502,-6.807748,4.274793,-2.026565,-4.479276]],[[-4.441577,-7.287318,-2.021428,3.221689,7.891603,-3.042312,-8.057663,-1.868111,-1.846486,4.325865,8.475838]],[[2.532596,-9.871498,9.451090,4.221031,7.370344,3.023172,4.920355,-2.381384,9.355940,-0.316091,-5.157367]],[[8.775133,-2.789207,9.006063,9.091463,1.531943,-1.206135,6.282625,-9.268740,7.812166,-8.724812,-2.693628]],[[7.502392,-5.008472,-8.048353,-5.570586,-6.153485,1.241517,6.049016,-2.974392,-7.997695,8.783192,8.346524]],[[-2.062990,-9.429790,0.944316,-3.312310,-1.962394,0.671271,1.808216,0.684418,-3.945488,4.766500,7.255121]]], dtype = "float32")#candidate|13723|(14, 1, 11)|const|float32
uop_13724 = relay.atan(const_13723.astype('float32')) # shape=(14, 1, 11)
output = uop_13724
output2 = uop_13724
func_13735 = relay.Function([], output)
mod['func_13735'] = func_13735
mod = relay.transform.InferType()(mod)
mutated_mod['func_13735'] = func_13735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13735_call = mutated_mod.get_global_var('func_13735')
call_13736 = func_13735_call()
output = call_13736
func_13737 = relay.Function([], output)
mutated_mod['func_13737'] = func_13737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8343_call = mod.get_global_var('func_8343')
func_8345_call = mutated_mod.get_global_var('func_8345')
call_13807 = func_8343_call()
call_13808 = func_8343_call()
func_10858_call = mod.get_global_var('func_10858')
func_10866_call = mutated_mod.get_global_var('func_10866')
var_13820 = relay.var("var_13820", dtype = "float64", shape = (48,))#candidate|13820|(48,)|var|float64
var_13821 = relay.var("var_13821", dtype = "int16", shape = (165,))#candidate|13821|(165,)|var|int16
const_13822 = relay.const([-7,4,-4,3,-6,1,-7,4,-6,7,4,7,-9,-1,8,-6,6,4,4,-1,2,-10,9,-10,8,3,7,-8,-1,-7,-7,-1,-5,-1,2,-9,-6,-7,3,-9,5,3,-2,-8,9,1,10,-7,8,-4,-3,-7,2,-5,-3,5,6,2,10,10,-7,5,4,-4,3,-3,1,-7,-5,-9,7,-6,4,1,-10,-3,-2,4,-2,8,-6,-4,-10,1,3,4,6,3,10,3,-4,6,-7,-2,9,-6,1,-4,-3,8,7,-6,-4,2,-2,3,-3,2,9,9,-5,5,-9,9,-5,7,-1,-4,1,-10,-3,9,-9,-4,-8,-6,-1,9,9,-1,-4,-6,-1,-1,-8,-7,3,-7,-8,1,-7,9,8,-8,-5,-3,7,-6,-4,3,8,-5,8,3,2,-4,-3,-6,2,-1,-5,7,-6,2,-4,3,7,-4,9,-10,3,1,6,6,3,6,4,10,8,1,9,3,2,-10,5,4,-6,4,2,10,9,-1,-9,2,-5,9,-7,-1,-2,-9,-4,4,6,10,10,-1,-7,-2,5,4,-7,5,9,-2,-8,-7,2,10,9,-5,-3,-10,3,7,-7,8,-5,-9,-9,-5,-2,9,4,-3,3,-4,8,-5,7,9,-2,-10,-1,3,-10,9,1,-9,1,-9,-1,9,8,-2,-7,-9,-1,-9,-7,-4,-1,10,-3,6,-10,6,-8,5,-2,-1,10,-1,-8,-1,3,6,8,-5,-7,-5,-3,-10,-10,5,2,3,5,-10,4,-1,-9,-10,-5,8,-3,-8,-5,-7,5,-7,7,8,-3,8,4,-4,-6,-9,-7,-2,-1,-9,3,3,8,-5,-1,-1,-5,-4,10,-1,-2,9,7,-2,-4,-9,6,4,-4,-3,6,-3,-2,-10,-5,-9,1,-8,9,-1,2,-9,1,-4,-4,4,-10,-1,-4,-5,3,-7,3,-5,7,7,-3,10,2,1,-1,-6,-9,-3,9,3,-3,-6,-8,-9,4,-6,4,3,10,-2,8,-1,-4,-2,-4,4,-5,-6,-1,10,2,-4,-10,2,2,10,-1,-9,-5,7,5,-9,-4,-5,-1,-2,-1,-7,5,10,3,-9,2,9,-8,9,10,6,-4,-8,-8,-5,-7,9,-4,-1,-10,9,-10,-9,5,-4,7,-10,2,3,-8,-6,-3,-9,5,-1,-2,-7,9,1,-6,-2,4,2,-7,6,3,10,-9,10,1,-9,4,-5,5,-8,8,4,9,8,10,3,5,1,4,-8,-5,-10,-6,-1,-1,-2,10,-1,-1,-6,4,-8,5,-3,-1,8,7,-4,-2,-3,-5,-10,-10,-3,-3,-6,8,-5,3,6,6,-1,-9,-7,-9,2,5,8,-6,-8,10,3,6,-5,-6,5,2,-7,1,1,-4,6,8,5,-5,-10,-5,-4,-3,-1,9,-10,-2,-3,-1,-2,9,4,-2,-9,2,-3,-6,-7,8,-5,6,10,-2,-10,7,-10,2,4,-5,-10,-6,-1,1,-9,-9,-6,2,4,8,1,-8,4,6,-5,-2,-7,9,9,9,-7,-6,5,8,4,-3,-1,-5,-2,-2,-4,-1,3,3,8,-1,2,9,-5,-5,2,1,9,-10,-1,-6,-7,7,7,-9,4,1,7,-1,6,1,-4,-3,10,-3,-6,-7,-6,-10,-6,1,10,6,-1,-2,-3,-6,5,9,3,-8,1,-9,-10,3,9,-6,5,10,8,-2,3,7,7,5,10,-8,-7,-1,7,2,5,9,-9,5,-9,10,4,1,-5,-1,10,-7,8,3,-1,3,5,7,9,3,8,-1,1,6,-8,3,8,-4,-8,-2,-4,-7,7,4,6,3,1,8,5,9,1,-1,4,5,-2,2,-2,-6,-3,-6,-8,-2,-4,-4,-4,-4,7,-6,-1,-2,10,1,-3,2,7,-2,6,5,-4,-10,-4,-3,-10,-9,-10,5,4,-1,-1,10,10,3,6,5,-1,-6,9,-3,8,9,-2,5,10,-3,-8,9,7,-3,3,2,-3,8,-8,1,2,4,-4,-2,-7,-5,1,3,9,-10,-6,-8,-9,-10,-5,2,1,-3,-7,9,-3,-8,-10,10,-9,-6,1,5,-8,8,6,-3,8,-3,-5,8,9,-10,-9,10,3,4,-10,5,-3,-3,4,7,-4,-8,3,6,-4,-2,-9,2,10,5,4,-8,-4,6,-9,-4,3,3,-8,9,7,6], dtype = "int16")#candidate|13822|(825,)|const|int16
var_13823 = relay.var("var_13823", dtype = "float32", shape = (320,))#candidate|13823|(320,)|var|float32
const_13824 = relay.const([5.299147,-9.944679,-3.563493,9.630688,8.518364,5.649454,-3.192680,-8.061914,-0.890730,3.328191,-3.693570,-9.978964,-0.294224,6.648637,-4.321819,-2.731436,2.064637,6.972488,3.261419,9.078085,0.995356,6.071130,5.894190,2.921262,-6.212371,-4.237960,-0.917503,-2.906863,-8.547287,9.325372,-3.993223,3.206845,-1.723209,2.849902,0.078681,-2.960575,-7.524096,7.611982,9.996012,6.939940,5.165083,3.876171,-1.830354,-1.840279,6.787532,-2.204497,5.646869,-9.083776,-7.801097,-3.926280,-7.011720,-1.202471,-2.299881,-1.691004,5.182246,-3.035259,5.535178,-0.429856,8.090202,3.006975,-5.036467,0.450431,0.318087,3.275240,4.169731,4.276673,-1.402212,-0.673593,8.686228,3.097988,8.622989,8.428109,1.372709,-1.514280,-5.201063,5.043078,0.293959,6.163630,-7.966440,-1.640327,-1.925303,6.565434,-0.385419,0.991037,3.063815,-6.392566,-7.586816,0.133681,5.301749,4.886774,9.119830,9.797066,5.194571,1.737502,6.377153,4.503426,-5.254614,4.327381,9.962816,-2.743357,7.306294,6.603607,4.124510,3.372112,-5.806625,-8.258504,4.578881,1.542308,-1.780783,8.523778,-2.822743,4.581432,7.981389,4.992297,-5.574099,6.312405,-3.233327,7.928449,-8.989147,8.473146,2.080804,-8.606624,2.617929,3.366085,6.973461,9.924887,-0.240227,-2.400548,6.867776,-1.019376,7.572640,7.396245,-6.189535,3.204733,8.627095,7.236341,9.869075,-8.974942,0.156586,-6.236531,-4.364956,5.763229,7.855310,-5.422772,9.261670,-9.136941,6.929118,2.531381,-4.045686,-7.889747,2.179273,2.360752,9.606088,9.476229,2.354512,7.687576,4.180043,-1.072119,-1.747096,-4.224734,5.066594,8.003891,-1.926253,-2.860100,4.843979,6.114612,9.329711,2.419573,-7.914165,5.695697,9.319954,1.927574,3.415210,5.846623,-5.273542,-4.294051,-1.127732,-1.637980,-0.104829,5.558092,4.669574,-3.137015,2.366247,-2.996808,-0.670699,-7.626983,-3.678984,-9.715574,3.924905,-7.082471,8.021933,-1.125745,-6.681700,1.544227,6.014108,-1.342310,8.771382,9.231422,1.397354,-2.158764,-0.829314,7.673507,-2.248168,-7.359531,7.204207,1.350475,3.645170,-6.049134,3.729618,-6.477399,-0.322639,0.045281,8.468121,0.311921,-7.195118,-0.285083,-0.250996,-8.380525,-1.844863,-2.152025,0.301334,-4.182216,5.411272,-5.007392,-0.120270,-3.658818,4.468888,-9.323628,-0.340644,0.994216,5.402131,3.385163,5.341814,-1.981830,1.960588,1.467761,2.707895,4.437620,-8.708000,1.002827,7.162592,-9.403305,6.684347,5.107019,-0.381671,9.650779,2.882328,7.230714,-0.521371,-3.803049,-7.578600,-8.703041,5.533593,9.363819,5.569967,6.276383,-1.761481,4.949832,-5.422983,2.719248,-4.006198,6.725846,-3.325729,-5.704299,-0.156872,-0.212130,5.851470,-6.333550,-0.149850,-0.951521,-8.123828,-5.975480,3.375130,5.539338,9.895074,-0.635750,4.160945,7.429947,-4.318891,-6.816316,-0.248924,-5.609630,5.225766,-0.900098,-2.039185,1.251109,-6.384197,3.399810,6.658391,-0.200563,1.631281,-0.805754,-3.763948,-5.208213,-3.772383,4.890241,2.933044,-8.980400,8.961947,5.195811,7.056940,-4.694129,-8.560460,-6.710022,-6.188881,-1.988957,1.378388,-2.485344,-2.736396,6.148604,0.329373,9.611154,-5.287098,2.481581,0.713216,8.749017,5.880261,-5.975950,4.858861,-1.144830,0.871953,7.830474,2.824309,-0.342472,6.107957,-8.514078,4.773433,8.843517,0.054830,3.416155,4.914268,-1.465708,-6.521482,1.581108,3.469688,-8.827049,-4.426832,3.137879,4.239663,-9.730422,4.266704,-2.573395,-2.273911,-1.186349,-7.846028,-4.613908,-5.972770,5.790376,-3.412530,-7.072405,-5.315311,-5.687510,6.983429,-9.155248,-6.565644,6.453404,-1.740120,-1.189221,6.990776,-3.367744,-7.800146,-9.238915,1.100949,3.892553,-0.761466,7.784372,-0.914836,4.836596,-6.694511,1.257733,-2.119514,-1.357367,-9.645661,-9.701267,-5.914647,9.481043,0.045540,5.203673,9.912711,-3.813495,2.198751,-8.305297,-0.918625,4.152190,-9.100549,5.694623,2.343156,5.891733,-9.887665,7.856139,-3.035578,7.184532,-2.183265,0.714430,4.031424,6.665941,3.492172,6.028286,-6.176358,-4.569060], dtype = "float64")#candidate|13824|(400,)|const|float64
call_13819 = relay.TupleGetItem(func_10858_call(relay.reshape(var_13820.astype('float64'), [48,]), relay.reshape(var_13821.astype('int16'), [165,]), relay.reshape(const_13822.astype('int16'), [825,]), relay.reshape(var_13823.astype('float32'), [320,]), relay.reshape(const_13822.astype('int16'), [825,]), relay.reshape(const_13824.astype('float64'), [8, 50]), ), 14)
call_13825 = relay.TupleGetItem(func_10866_call(relay.reshape(var_13820.astype('float64'), [48,]), relay.reshape(var_13821.astype('int16'), [165,]), relay.reshape(const_13822.astype('int16'), [825,]), relay.reshape(var_13823.astype('float32'), [320,]), relay.reshape(const_13822.astype('int16'), [825,]), relay.reshape(const_13824.astype('float64'), [8, 50]), ), 14)
func_7257_call = mod.get_global_var('func_7257')
func_7259_call = mutated_mod.get_global_var('func_7259')
call_13835 = relay.TupleGetItem(func_7257_call(), 0)
call_13836 = relay.TupleGetItem(func_7259_call(), 0)
output = relay.Tuple([call_13807,call_13819,var_13820,var_13821,const_13822,var_13823,const_13824,call_13835,])
output2 = relay.Tuple([call_13808,call_13825,var_13820,var_13821,const_13822,var_13823,const_13824,call_13836,])
func_13846 = relay.Function([var_13820,var_13821,var_13823,], output)
mod['func_13846'] = func_13846
mod = relay.transform.InferType()(mod)
mutated_mod['func_13846'] = func_13846
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13846_call = mutated_mod.get_global_var('func_13846')
var_13848 = relay.var("var_13848", dtype = "float64", shape = (48,))#candidate|13848|(48,)|var|float64
var_13849 = relay.var("var_13849", dtype = "int16", shape = (165,))#candidate|13849|(165,)|var|int16
var_13850 = relay.var("var_13850", dtype = "float32", shape = (320,))#candidate|13850|(320,)|var|float32
call_13847 = func_13846_call(var_13848,var_13849,var_13850,)
output = call_13847
func_13851 = relay.Function([var_13848,var_13849,var_13850,], output)
mutated_mod['func_13851'] = func_13851
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8883_call = mod.get_global_var('func_8883')
func_8885_call = mutated_mod.get_global_var('func_8885')
call_13853 = relay.TupleGetItem(func_8883_call(), 0)
call_13854 = relay.TupleGetItem(func_8885_call(), 0)
output = call_13853
output2 = call_13854
func_13860 = relay.Function([], output)
mod['func_13860'] = func_13860
mod = relay.transform.InferType()(mod)
output = func_13860()
func_13861 = relay.Function([], output)
mutated_mod['func_13861'] = func_13861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6785_call = mod.get_global_var('func_6785')
func_6786_call = mutated_mod.get_global_var('func_6786')
call_13974 = relay.TupleGetItem(func_6785_call(), 0)
call_13975 = relay.TupleGetItem(func_6786_call(), 0)
output = call_13974
output2 = call_13975
func_13979 = relay.Function([], output)
mod['func_13979'] = func_13979
mod = relay.transform.InferType()(mod)
mutated_mod['func_13979'] = func_13979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13979_call = mutated_mod.get_global_var('func_13979')
call_13980 = func_13979_call()
output = call_13980
func_13981 = relay.Function([], output)
mutated_mod['func_13981'] = func_13981
mutated_mod = relay.transform.InferType()(mutated_mod)
const_13982 = relay.const([[[-3.153982,7.909862,-1.392272,9.730030,-8.410120,9.036685,1.861805,2.350013,0.803751,1.151055,-5.897060,-9.580956,-6.262565,0.294433,1.067219]],[[2.233771,-0.963916,4.277438,9.750233,-7.821392,-8.195164,8.596822,-2.090072,-8.648065,-8.556879,-9.349769,2.334599,3.046906,-9.092780,9.567377]],[[4.545850,-1.406769,5.792360,-4.362509,-6.485657,2.867299,0.470733,4.432795,1.358383,6.414809,8.457665,-9.110292,-3.481600,9.375325,4.399782]],[[-2.124734,2.386845,-3.940777,2.120752,1.647238,6.979489,-2.439744,6.408656,-8.925636,-4.372095,-8.121770,4.898038,-9.034227,-5.032636,1.730225]],[[0.779522,-5.945848,-7.966524,2.586824,-8.307455,8.200570,9.312110,-5.256884,8.321257,-2.414429,-2.047445,-9.101192,1.334215,6.848950,-4.419146]],[[9.104072,-9.397953,-5.960431,-6.434930,-9.976182,-3.017038,-5.309932,-6.240260,-9.369298,-0.960884,2.676961,2.879063,-4.433580,-2.493232,-5.064563]]], dtype = "float32")#candidate|13982|(6, 1, 15)|const|float32
uop_13983 = relay.log(const_13982.astype('float32')) # shape=(6, 1, 15)
bop_13985 = relay.less(uop_13983.astype('bool'), relay.reshape(const_13982.astype('bool'), relay.shape_of(uop_13983))) # shape=(6, 1, 15)
output = bop_13985
output2 = bop_13985
func_14009 = relay.Function([], output)
mod['func_14009'] = func_14009
mod = relay.transform.InferType()(mod)
output = func_14009()
func_14010 = relay.Function([], output)
mutated_mod['func_14010'] = func_14010
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5023_call = mod.get_global_var('func_5023')
func_5024_call = mutated_mod.get_global_var('func_5024')
call_14036 = func_5023_call()
call_14037 = func_5023_call()
output = call_14036
output2 = call_14037
func_14050 = relay.Function([], output)
mod['func_14050'] = func_14050
mod = relay.transform.InferType()(mod)
output = func_14050()
func_14051 = relay.Function([], output)
mutated_mod['func_14051'] = func_14051
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12917_call = mod.get_global_var('func_12917')
func_12919_call = mutated_mod.get_global_var('func_12919')
call_14074 = relay.TupleGetItem(func_12917_call(), 0)
call_14075 = relay.TupleGetItem(func_12919_call(), 0)
output = relay.Tuple([call_14074,])
output2 = relay.Tuple([call_14075,])
func_14087 = relay.Function([], output)
mod['func_14087'] = func_14087
mod = relay.transform.InferType()(mod)
mutated_mod['func_14087'] = func_14087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14087_call = mutated_mod.get_global_var('func_14087')
call_14088 = func_14087_call()
output = call_14088
func_14089 = relay.Function([], output)
mutated_mod['func_14089'] = func_14089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5559_call = mod.get_global_var('func_5559')
func_5561_call = mutated_mod.get_global_var('func_5561')
call_14094 = relay.TupleGetItem(func_5559_call(), 0)
call_14095 = relay.TupleGetItem(func_5561_call(), 0)
output = relay.Tuple([call_14094,])
output2 = relay.Tuple([call_14095,])
func_14137 = relay.Function([], output)
mod['func_14137'] = func_14137
mod = relay.transform.InferType()(mod)
output = func_14137()
func_14138 = relay.Function([], output)
mutated_mod['func_14138'] = func_14138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13132_call = mod.get_global_var('func_13132')
func_13133_call = mutated_mod.get_global_var('func_13133')
call_14188 = relay.TupleGetItem(func_13132_call(), 0)
call_14189 = relay.TupleGetItem(func_13133_call(), 0)
func_5577_call = mod.get_global_var('func_5577')
func_5579_call = mutated_mod.get_global_var('func_5579')
call_14205 = func_5577_call()
call_14206 = func_5577_call()
func_6571_call = mod.get_global_var('func_6571')
func_6573_call = mutated_mod.get_global_var('func_6573')
call_14223 = func_6571_call()
call_14224 = func_6571_call()
output = relay.Tuple([call_14188,call_14205,call_14223,])
output2 = relay.Tuple([call_14189,call_14206,call_14224,])
func_14231 = relay.Function([], output)
mod['func_14231'] = func_14231
mod = relay.transform.InferType()(mod)
output = func_14231()
func_14232 = relay.Function([], output)
mutated_mod['func_14232'] = func_14232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6162_call = mod.get_global_var('func_6162')
func_6163_call = mutated_mod.get_global_var('func_6163')
call_14249 = relay.TupleGetItem(func_6162_call(), 0)
call_14250 = relay.TupleGetItem(func_6163_call(), 0)
output = call_14249
output2 = call_14250
func_14256 = relay.Function([], output)
mod['func_14256'] = func_14256
mod = relay.transform.InferType()(mod)
mutated_mod['func_14256'] = func_14256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14256_call = mutated_mod.get_global_var('func_14256')
call_14257 = func_14256_call()
output = call_14257
func_14258 = relay.Function([], output)
mutated_mod['func_14258'] = func_14258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5378_call = mod.get_global_var('func_5378')
func_5379_call = mutated_mod.get_global_var('func_5379')
call_14331 = relay.TupleGetItem(func_5378_call(), 0)
call_14332 = relay.TupleGetItem(func_5379_call(), 0)
output = call_14331
output2 = call_14332
func_14345 = relay.Function([], output)
mod['func_14345'] = func_14345
mod = relay.transform.InferType()(mod)
mutated_mod['func_14345'] = func_14345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14345_call = mutated_mod.get_global_var('func_14345')
call_14346 = func_14345_call()
output = call_14346
func_14347 = relay.Function([], output)
mutated_mod['func_14347'] = func_14347
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9731_call = mod.get_global_var('func_9731')
func_9733_call = mutated_mod.get_global_var('func_9733')
call_14364 = relay.TupleGetItem(func_9731_call(), 0)
call_14365 = relay.TupleGetItem(func_9733_call(), 0)
func_7605_call = mod.get_global_var('func_7605')
func_7611_call = mutated_mod.get_global_var('func_7611')
var_14394 = relay.var("var_14394", dtype = "float64", shape = (400,))#candidate|14394|(400,)|var|float64
var_14395 = relay.var("var_14395", dtype = "uint64", shape = (280,))#candidate|14395|(280,)|var|uint64
const_14396 = relay.const([0.574692,3.720227,-9.429978,-4.189982,0.194228,-5.484086,5.396145,2.015803,6.856306,-3.100847,8.521151,5.296032,-9.013520,7.282051,-8.284571,1.547471,-7.067330,3.412452,-4.650730,0.622450,-9.682670,-9.439904,7.035698,4.180402,1.326948,5.396103,-4.168972,-7.612606,-3.404538,-0.326663,-8.236006,-5.847301,6.145055,-4.704323,-1.217894,7.936710,1.243436,-2.671024,-7.531838,6.540301,6.920637,-5.434502,-8.510471,-1.537050,-3.831397,1.421679,5.059759,3.391640,2.110460,-4.560665,0.566440,3.071208,1.534712,-2.604053,3.268095,4.723994,-1.148206,6.394062,6.070538,1.429119,-1.865232,-5.354719,8.763692,-4.521742,8.885542,-6.237416,6.168468,1.127988,8.587273,-0.315824,-3.984822,-5.277462,1.278179,3.722352,1.522136,-0.223793,2.075180,1.486788,-4.457528,-8.756747,7.710229,1.379735,-5.434735,5.512378,-6.712985,-2.711050,-3.912137,5.837442,-6.229341,-9.252303,5.999291,-3.283959,9.170677,6.299174,5.470791,-6.919692,-7.920931,8.050015,-9.570468,6.966415,-6.294367,2.009117,-7.874916,-0.610862,8.774045,-7.097413,4.270601,-1.254978,8.156690,2.345935,1.281272,1.709899,9.585856,-4.529811,5.377038,-6.660967,1.752479,-1.926849,-5.621645,2.037628,9.503490,-7.355321,-4.259667,-5.980517,2.410722,-4.963937,1.721416,-1.537375,1.054595,-1.878290,-6.104205,-5.510898,2.604010,9.767879,-8.203564,0.645177,4.924379,-6.650060,-3.533172,3.580750,-3.444559,-7.398121,4.127406,-8.478556,0.514176,8.685959,6.737517,-4.355552,7.981529,-0.286320,-1.824672,6.323028,-5.350918,2.084291,-6.985457,-5.248717,-0.464442,-8.953384,4.212616,-4.816366,-9.714502,6.592397,-0.649811,-8.476300,6.085826,2.984209,-9.924753,4.845019,-4.418352,-5.907632,3.212279,-9.607875,9.419137,7.835532,6.834118,-7.172968,-4.917299,-2.219847,6.121126,-8.001992,2.552775,-6.785657,-6.296338,-2.212848,-5.384508,-1.423665,7.414191,8.100203,0.188520,-0.059706,4.858269,-4.961954,-2.504465,-9.193816,1.023577,-9.967997,-0.770797,9.094813,0.687048,7.911599,-1.887685,9.175232,-4.517465,-9.481904,-7.869529,8.815729,1.477388,5.436637,-2.565038,4.486888,-5.574032,-3.983053,-2.518324,3.995116,-1.568809,6.114584,-3.210472,-3.545558,-3.382721,4.927930,3.161917,-4.614977,-8.586659,-7.310670,5.682046,2.794440,-0.111191,-9.081258,5.928109,-0.127684,-3.082873,-7.090744,-8.385357,-9.316174,9.714489,1.231203,-0.282926,-4.905664,3.292369,5.223808,-6.165681,-0.105480,-8.843342,-1.421467,8.030818,3.982212,-0.174265,-9.303788,1.630413,0.678876,-0.599230,1.465747,-6.482989,-0.912711,8.805213,-3.245218,-9.818075,-9.639724,0.869962,-0.113959,6.113770,6.022386,3.661243,-1.833941,-3.917426,3.943294,4.196997,2.364834,-0.437105,8.549830,9.229737,-8.467675,5.205844,-2.591326,6.775986,5.169248,1.177683,-0.414402,-2.827884,3.057235,8.007456,-6.631490,8.454137,-4.249155,7.948847,2.738408,-0.836795,-9.722025,-2.462266,-5.623267,7.662453,-1.700515,-6.496187,1.885430,-4.956362,6.115994,9.585533,-4.591745,2.812143,3.537548,-7.187643,8.430462,-7.688355,-3.227032,0.482954,-4.661850,-0.104767,1.118555,9.053205,-8.513872,5.104607,1.945714,2.819288,0.015358,9.826438,6.863847,-0.375594,-2.873270,-1.824270,0.773625,1.373025,-9.966070,5.388386,6.482421,-9.362426,-1.377108,6.013789,-9.061008,3.454557,-5.886134,-2.849607,-8.362769,-9.501414,4.699756,-6.021345,-1.533821,-0.241601,5.361964,-9.313093,9.764356,-8.206513,-6.976665,1.069857,-0.283851,3.347700,5.460182,-8.417373,-3.276158,-5.498844,7.621134,-1.760058,2.643391,-3.999917,-6.601076,2.263649,8.041427,0.646784,9.971116,2.253685,0.622116,-2.045163,-9.845285,4.964774,-9.331758,4.576855,-1.610929,1.278637,-7.320861,-1.498920,4.847368,-7.999744,-8.708479,-6.083538,0.563313,1.421751,-0.694518,6.501971,7.841198,6.066664,6.472865,0.216911,7.044771,1.442046,4.783012,-4.374291,8.272572,5.122198,2.645347,0.991073,1.006520,0.642640,1.169660,3.808444,0.111612,-1.900357,8.286756,-2.705283,-0.895170,-7.752076,-4.934051,-1.011507,-8.369849,5.316731,-4.761555,-5.186130,6.270352,5.699511,-6.012120,0.110212,-0.822229,-0.104662,-1.061234,-4.845090,-8.603609,-0.886157,2.213637,-5.189103,-1.630086,5.873714,3.190882,3.149437,-6.714314,2.451202,5.940082,-0.723532,-7.604397,2.389890,-2.219712,3.862167,-0.745073,9.351736,5.989680,2.315589,5.570863,-0.756307,-1.997369,7.511807,-6.351366,-5.323301,-2.457755,4.817635,4.450967,6.984315,-3.283223,5.334280,-0.248232,4.864520,-7.507058], dtype = "float32")#candidate|14396|(448,)|const|float32
const_14397 = relay.const([-1.400609,0.260611,-3.497839,-5.430387,1.646328,-7.771193,5.570460,7.357484,2.380788,-1.332294,8.483086,0.544336,-2.468550,6.330589,3.619141,4.677595,3.575780,1.195696,-0.246384,-1.118926,-5.217489,9.593133,-6.398003,-9.297149,-4.132037,-0.072974,8.068999,-7.629067,-5.307067,-0.927182,7.753776,9.831932,-2.301877,-9.049953,7.089074,3.303708,5.874488,7.947729,1.299104,4.944698,-3.627715,4.990851,8.062981,1.571064,-3.466719,8.014569,0.089347,-1.837563,-5.040027,2.184453,2.304879,7.063679,2.065595,-1.308101,8.432870,-1.148933,-8.967031,2.689207,-6.113103,6.715180,-0.487072,-7.750805,3.769846,-8.739422,0.508410,4.531785,-8.449352,-4.054098,-2.032836,-0.304869,-6.397264,3.377700,5.582550,1.686512,-1.929464,-3.159809,7.162195,-3.483886,5.665640,-6.079998,-2.536486,7.956458,5.911527,-9.379386,-5.320746,8.430771,-8.796932,4.639732,8.066207,1.269295,7.989770,6.870265,-5.756668,-4.863572,-1.454463,-5.903625,-5.132336,5.348864,8.953260,0.202582,-5.716788,3.488460,-3.778297,-3.402837,2.576496,4.791282,9.751266,6.604733,-5.404206,1.290334,2.185954,-6.684731,5.287002,9.047388,3.375603,2.703924,1.263097,-2.294138,3.669273,3.213997,-6.416620,-8.879451,5.826381,6.833111,5.461268,-1.011055,3.857311,-5.448541,-3.947615,9.257916,1.656344,-3.181939,7.204024,-4.469842,0.415567,6.623771,-0.149730,-7.103120,-9.179275,0.486619,-3.026022,-8.068959,-1.320752,1.731249,-3.078981,1.916339,1.990674,-2.639032,-0.641366,9.668611,-1.866669,-1.524015,-5.514877,5.604938,-6.432215,-2.502929,-1.966911,-8.714955,-8.427054,-2.353962,8.583795,-4.679950,7.482200,8.121203,3.913604,0.712980,-6.740142,-3.076691,-3.799933,5.955253,-6.804754,-5.512595,-2.301901,-8.277842,-6.770490,3.829885,-2.122096,-2.046486,-9.180673,1.017924,-3.259888,7.760277,-6.619074,-9.489980,9.543486,-5.310240,9.892735,3.439613,1.608349,-0.682082,-7.039744,5.712589,4.122451,-5.631868,-6.485567,7.069115,-2.106668,0.016008,-2.442176,-6.362955,8.844610,-9.725598,9.934315,-9.434667,1.488763,-4.124983,-2.591134,-1.656679,0.260511,0.911465,-0.224504,-7.543392,2.343043,-9.816609,1.899727,-6.606557,1.624955,-6.566406,-6.787803,4.424912,1.654176,6.195045,-0.723843,-4.365136,-8.990947,1.640934,-7.250552,6.807496,9.257009,-0.070984,-5.544693,9.913431,7.553225,-6.644139,-2.559405,5.708053,2.182964,5.548917,-7.494711,5.444314,1.691256,0.345147,0.907858,2.142080,-4.753677,8.754200,-2.143576,-8.877568,-5.667528,0.415176,4.398183,0.469777,5.731501,-1.164573,-0.258240,-1.223313,-0.915789,6.445830,0.470551,-6.431682,-0.642670,-2.376790,-0.722658,-7.512857,-6.017712,5.147168,-2.768022,-3.554146,0.210266,0.010264,3.147057,9.327545,-0.344580,1.981471,1.066382,5.740954,9.517026,2.557795,2.532772,4.939098,7.316743,2.058228,1.923771,-8.554457,-9.322440,-0.109083,6.556088,1.654150,-3.053296,8.864691,-9.174891,-1.198778,3.600092,8.292152,8.723835,-0.659989,7.291968,1.408915,4.358558,2.910845,7.121947,4.346750,0.696378,-8.055585,9.698242,4.445752,1.510418,-7.904584,3.226267,6.882142,-8.082162,-9.456872,7.807687,-8.429057,1.856788,-6.858918,4.038825,4.103929,-0.210361,-6.116613,-3.724967,2.728647,4.825911,-9.472999,9.598305,-2.157718,2.271523,0.673556,-4.064947,7.791296,2.654722,-6.253573,-8.189006,5.322634,-2.495588,-5.229452,7.577393,-0.913661,8.622844,-4.580839,-7.747539,-3.824098,0.709750,-2.687177,2.188273,5.372392,0.896493,1.178732,8.778785,-5.121500,5.480261,-0.566073,-5.537823,1.481223,9.138747,-4.453315,-2.911496,1.281645,-4.447806,2.884013,-3.606619,-3.671453,6.053694,9.755373,-3.157453,-8.728988,-3.597234,-1.496975,0.418429,4.372004,4.590389,-3.093818,-9.827529,7.637188,9.121874,5.255713,6.575319,2.476332,6.514702,-7.738763,-1.710422,3.492177,5.558790,3.409612,-4.516837,-7.361379,-3.448803,9.806738,-2.258636,5.438700,-3.121154,6.861533,-3.649217,-5.807265,1.786057,5.786322,7.744332,7.353161,-0.697964,7.080288,9.077806,2.202665,-8.895422,-3.565817,0.783019,-1.656574,-7.321966,-1.993084,-5.699147,4.514686,3.843486,1.972640,9.285703,1.573276,6.189035,-3.858729,-7.298580,-1.551185,9.347712,-9.502789,-0.553054,-4.837055,-3.567102,6.583025,8.244073,6.495636,9.734984,4.004606,0.585751,-1.607099,5.472754,8.729762,-6.978701,-0.923455,-1.691534,5.121604,7.878609,-0.225577,-0.790674,-3.977807,-7.089475,-5.497914,-9.207507,-8.342249,-9.639907,-0.363664,-9.976510,-8.878717,3.966401,-8.371148,5.676921,-5.216905,9.462726,-3.317832,-1.207561,6.012288,-8.873834,-1.934890,7.612765,-8.270709,9.260767,7.083863,-9.531959,7.943721,-4.850692,-3.757531,3.149463,-6.153849,1.762745,-6.562685,6.793462,-7.100098,0.603214,-7.679147,4.349668,-7.655690,9.333226,-0.633523,4.098612,0.761393,2.759284,8.614093,-9.042577,7.707382,0.018463,1.782389,2.084393,-5.004347,-0.266149,8.447526,-4.458688,-1.834608,9.752954,0.581403,-4.523919,-3.968450,-8.045012,-3.262040,4.082418,-1.956452,5.845161,3.463624,0.054874,5.959613,-1.875690,-8.572044,5.557335,-8.795966,6.031994,4.513297,-6.758884,-9.006521,-6.517233,2.195017,-2.513570,-0.604494,9.134396,0.099476,4.221145,-1.200269,7.963018,-0.684086,-2.446666,-9.476311,8.201001,9.550351,4.420796,-3.686743,4.815595,-4.647957,-0.868603,3.072227,-7.393107,-7.375654,-0.460237,-8.065886,7.173922,-4.210981,0.994199,-9.093745,-2.276414,0.202624,1.790426,7.733646,2.867062,-4.668728,-1.661357,-0.400204,-5.915948,0.417884,5.681867,7.890907,-0.741119,-3.309215,-7.690500,-1.180902,0.385589,-8.513830,-2.118039,0.666101,7.146418,8.314581,8.991576,6.195066,-5.881846,-9.207065,-3.571703,5.872537,8.890899,-8.399067,-1.346471,3.202886,-8.246189,-6.639200,9.723400,8.079660,0.510537,0.541003,-2.932994,1.621887,7.014555,-9.153043,9.819027,-5.547759,-3.238638,-2.994200,-7.789307,-2.937352,8.954603,6.550440,-7.487573,-4.243363,8.371608,-7.332945,-8.206491,-4.590944,-3.599393,1.968117,-4.362688,-7.019465], dtype = "float64")#candidate|14397|(600,)|const|float64
call_14393 = relay.TupleGetItem(func_7605_call(relay.reshape(var_14394.astype('float64'), [400,]), relay.reshape(var_14395.astype('uint64'), [280,]), relay.reshape(const_14396.astype('float32'), [448, 1]), relay.reshape(const_14397.astype('float64'), [600,]), ), 3)
call_14398 = relay.TupleGetItem(func_7611_call(relay.reshape(var_14394.astype('float64'), [400,]), relay.reshape(var_14395.astype('uint64'), [280,]), relay.reshape(const_14396.astype('float32'), [448, 1]), relay.reshape(const_14397.astype('float64'), [600,]), ), 3)
func_3695_call = mod.get_global_var('func_3695')
func_3700_call = mutated_mod.get_global_var('func_3700')
const_14403 = relay.const([[4.885962,4.860093,0.423504,7.935051,4.348069,-8.714599,7.300373,-6.387403,-3.094660,-7.019424,0.322897,-7.355059,6.623719,1.754708,3.656880,-8.920153,2.179246,-8.998220,-7.440723,9.654116,-7.338174,-5.749824,9.264355,2.931276,-2.958986,-3.702992,-9.603952,4.798408,6.409006,0.408120,9.976753,0.726269,-5.763492,7.538579,-6.802320,-0.207132,2.426659,-2.670299,4.369296,-3.238078,6.831208,6.826416,5.619771,3.815620,7.577335,0.418249,6.882327,9.270145,-5.618886,-3.754046,2.999555,4.425500,-9.908640,3.449535,-1.247740,6.686088,1.641069,5.712224,-4.536900,2.644155,4.336603,-2.541779,1.250790,-3.405971,-9.153382,-6.007533,4.686732,-1.480927,4.787291,2.742725,-1.162726,-9.871107,-6.767320,-4.072435,-9.285377,-3.899089,2.324109,-8.642956,0.189450,-6.018867,-3.618122,9.282198,7.390900,9.930333,-4.963835,-9.153974,7.978859,-4.023820,-0.009139,-0.277052,-0.395310,-2.959086,4.957278,-1.024664,-6.985917,8.839266,-8.135762,-0.968773,-5.127429,-2.285146,6.990895,1.892532,7.523237,-1.550388,3.999109,4.099979,5.364773,8.185380,-0.275910,4.106124,-0.908911,9.686708,-5.689367,-9.319342,2.629122,7.032296,6.536524,-9.185051,-0.425170,-6.534631,3.616769,4.647656,-6.296830,-5.256171,-2.834007,7.968098,-1.040452,5.403408,-1.244151,8.099193,8.797473,-1.805894,-9.698450,5.342122,9.433485,-6.633177,6.709308,-4.870864,-3.807452,5.215705,-5.337265,4.221646,1.661039,0.954635,5.342258,-9.078355,7.637913,6.996388,9.272149,-6.487388,5.227531,7.944288,-8.801413,-2.351560,-0.921447,-8.134141,-3.502895,9.951432,-6.866583,8.025729],[-2.935322,-5.882192,4.589067,0.913482,4.131350,3.054207,-1.418386,0.871770,-6.938002,1.400535,4.081857,-7.471559,1.187650,-4.166025,-5.010083,8.530452,6.706206,3.169475,-0.697932,4.942647,-9.724533,-4.622735,7.415107,-4.489461,0.329162,0.539835,5.935314,-1.087607,9.335204,-4.069629,-3.788618,-7.168283,-1.484782,-4.173819,-5.308277,-1.589467,1.857865,1.161424,-1.140722,-6.153842,6.750479,2.836745,5.429138,-6.983277,-1.152810,5.740384,-9.777445,-9.506359,4.705124,2.115668,-3.949900,-6.139423,-8.551992,-6.732511,9.732636,-5.387056,-9.634584,5.126793,0.070507,3.080277,0.990469,2.063938,-7.702788,-5.940998,-5.560058,-4.782524,4.452334,-1.873402,-2.651894,-1.813095,-1.161684,1.329249,-1.166652,-8.425133,-2.432932,4.800366,-5.299813,4.169403,-3.602495,-8.483023,-4.979729,5.253143,-7.380360,1.465936,1.094727,-1.415187,0.512697,-3.948302,6.601684,3.676301,-3.456360,3.691756,9.256379,-9.094400,-1.884155,8.029228,0.539664,-4.955341,-3.658008,-4.295212,9.805480,4.401425,-7.648364,9.134642,8.286892,2.336176,1.819760,-3.898459,-8.973798,2.544952,-7.451711,4.501738,0.554965,9.173739,4.716922,8.528547,-6.695261,1.815834,3.868880,-8.016990,-0.583622,-7.754351,-2.078994,-5.042267,0.961118,1.851448,-0.478806,2.065578,-0.954809,-3.063575,1.072470,1.881591,-6.424805,-1.176946,5.919573,-7.387412,9.536514,3.007577,-8.932447,-6.018728,5.999766,8.263583,-9.252916,-3.506327,2.940549,-1.410048,-3.459107,-9.613511,1.127412,-0.742980,-2.101323,-6.919384,-6.779691,8.210375,1.406126,-0.615708,-0.407645,4.282725,5.236875,2.627792]], dtype = "float32")#candidate|14403|(2, 160)|const|float32
var_14404 = relay.var("var_14404", dtype = "int16", shape = (165,))#candidate|14404|(165,)|var|int16
call_14402 = relay.TupleGetItem(func_3695_call(relay.reshape(const_14403.astype('float32'), [5, 4, 16]), relay.reshape(var_14404.astype('int16'), [11, 15]), relay.reshape(const_14403.astype('float32'), [5, 4, 16]), ), 6)
call_14405 = relay.TupleGetItem(func_3700_call(relay.reshape(const_14403.astype('float32'), [5, 4, 16]), relay.reshape(var_14404.astype('int16'), [11, 15]), relay.reshape(const_14403.astype('float32'), [5, 4, 16]), ), 6)
func_11146_call = mod.get_global_var('func_11146')
func_11149_call = mutated_mod.get_global_var('func_11149')
call_14413 = relay.TupleGetItem(func_11146_call(relay.reshape(const_14397.astype('float64'), [6, 10, 10])), 1)
call_14414 = relay.TupleGetItem(func_11149_call(relay.reshape(const_14397.astype('float64'), [6, 10, 10])), 1)
var_14417 = relay.var("var_14417", dtype = "float32", shape = (2, 160))#candidate|14417|(2, 160)|var|float32
bop_14418 = relay.mod(const_14403.astype('float32'), relay.reshape(var_14417.astype('float32'), relay.shape_of(const_14403))) # shape=(2, 160)
func_5577_call = mod.get_global_var('func_5577')
func_5579_call = mutated_mod.get_global_var('func_5579')
call_14425 = func_5577_call()
call_14426 = func_5577_call()
output = relay.Tuple([call_14364,call_14393,var_14394,var_14395,const_14396,const_14397,call_14402,var_14404,call_14413,bop_14418,call_14425,])
output2 = relay.Tuple([call_14365,call_14398,var_14394,var_14395,const_14396,const_14397,call_14405,var_14404,call_14414,bop_14418,call_14426,])
func_14466 = relay.Function([var_14394,var_14395,var_14404,var_14417,], output)
mod['func_14466'] = func_14466
mod = relay.transform.InferType()(mod)
mutated_mod['func_14466'] = func_14466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14466_call = mutated_mod.get_global_var('func_14466')
var_14468 = relay.var("var_14468", dtype = "float64", shape = (400,))#candidate|14468|(400,)|var|float64
var_14469 = relay.var("var_14469", dtype = "uint64", shape = (280,))#candidate|14469|(280,)|var|uint64
var_14470 = relay.var("var_14470", dtype = "int16", shape = (165,))#candidate|14470|(165,)|var|int16
var_14471 = relay.var("var_14471", dtype = "float32", shape = (2, 160))#candidate|14471|(2, 160)|var|float32
call_14467 = func_14466_call(var_14468,var_14469,var_14470,var_14471,)
output = call_14467
func_14472 = relay.Function([var_14468,var_14469,var_14470,var_14471,], output)
mutated_mod['func_14472'] = func_14472
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6571_call = mod.get_global_var('func_6571')
func_6573_call = mutated_mod.get_global_var('func_6573')
call_14549 = func_6571_call()
call_14550 = func_6571_call()
output = relay.Tuple([call_14549,])
output2 = relay.Tuple([call_14550,])
func_14553 = relay.Function([], output)
mod['func_14553'] = func_14553
mod = relay.transform.InferType()(mod)
mutated_mod['func_14553'] = func_14553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14553_call = mutated_mod.get_global_var('func_14553')
call_14554 = func_14553_call()
output = call_14554
func_14555 = relay.Function([], output)
mutated_mod['func_14555'] = func_14555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7003_call = mod.get_global_var('func_7003')
func_7004_call = mutated_mod.get_global_var('func_7004')
call_14596 = relay.TupleGetItem(func_7003_call(), 1)
call_14597 = relay.TupleGetItem(func_7004_call(), 1)
func_12138_call = mod.get_global_var('func_12138')
func_12140_call = mutated_mod.get_global_var('func_12140')
call_14602 = relay.TupleGetItem(func_12138_call(), 0)
call_14603 = relay.TupleGetItem(func_12140_call(), 0)
output = relay.Tuple([call_14596,call_14602,])
output2 = relay.Tuple([call_14597,call_14603,])
func_14617 = relay.Function([], output)
mod['func_14617'] = func_14617
mod = relay.transform.InferType()(mod)
mutated_mod['func_14617'] = func_14617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14617_call = mutated_mod.get_global_var('func_14617')
call_14618 = func_14617_call()
output = call_14618
func_14619 = relay.Function([], output)
mutated_mod['func_14619'] = func_14619
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6762_call = mod.get_global_var('func_6762')
func_6764_call = mutated_mod.get_global_var('func_6764')
call_14639 = relay.TupleGetItem(func_6762_call(), 0)
call_14640 = relay.TupleGetItem(func_6764_call(), 0)
output = call_14639
output2 = call_14640
func_14648 = relay.Function([], output)
mod['func_14648'] = func_14648
mod = relay.transform.InferType()(mod)
mutated_mod['func_14648'] = func_14648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14648_call = mutated_mod.get_global_var('func_14648')
call_14649 = func_14648_call()
output = call_14649
func_14650 = relay.Function([], output)
mutated_mod['func_14650'] = func_14650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9275_call = mod.get_global_var('func_9275')
func_9276_call = mutated_mod.get_global_var('func_9276')
call_14670 = relay.TupleGetItem(func_9275_call(), 0)
call_14671 = relay.TupleGetItem(func_9276_call(), 0)
var_14684 = relay.var("var_14684", dtype = "float64", shape = (5, 10, 10))#candidate|14684|(5, 10, 10)|var|float64
bop_14685 = relay.power(call_14670.astype('float32'), var_14684.astype('float32')) # shape=(5, 10, 10)
bop_14688 = relay.power(call_14671.astype('float32'), var_14684.astype('float32')) # shape=(5, 10, 10)
output = bop_14685
output2 = bop_14688
func_14701 = relay.Function([var_14684,], output)
mod['func_14701'] = func_14701
mod = relay.transform.InferType()(mod)
mutated_mod['func_14701'] = func_14701
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14702 = relay.var("var_14702", dtype = "float64", shape = (5, 10, 10))#candidate|14702|(5, 10, 10)|var|float64
func_14701_call = mutated_mod.get_global_var('func_14701')
call_14703 = func_14701_call(var_14702)
output = call_14703
func_14704 = relay.Function([var_14702], output)
mutated_mod['func_14704'] = func_14704
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14345_call = mod.get_global_var('func_14345')
func_14347_call = mutated_mod.get_global_var('func_14347')
call_14773 = func_14345_call()
call_14774 = func_14345_call()
func_7727_call = mod.get_global_var('func_7727')
func_7728_call = mutated_mod.get_global_var('func_7728')
call_14789 = func_7727_call()
call_14790 = func_7727_call()
func_7392_call = mod.get_global_var('func_7392')
func_7393_call = mutated_mod.get_global_var('func_7393')
call_14812 = relay.TupleGetItem(func_7392_call(), 1)
call_14813 = relay.TupleGetItem(func_7393_call(), 1)
func_14553_call = mod.get_global_var('func_14553')
func_14555_call = mutated_mod.get_global_var('func_14555')
call_14815 = relay.TupleGetItem(func_14553_call(), 0)
call_14816 = relay.TupleGetItem(func_14555_call(), 0)
bop_14821 = relay.not_equal(call_14773.astype('bool'), relay.reshape(call_14815.astype('bool'), relay.shape_of(call_14773))) # shape=(1, 10, 10)
bop_14824 = relay.not_equal(call_14774.astype('bool'), relay.reshape(call_14816.astype('bool'), relay.shape_of(call_14774))) # shape=(1, 10, 10)
output = relay.Tuple([call_14789,call_14812,bop_14821,])
output2 = relay.Tuple([call_14790,call_14813,bop_14824,])
func_14857 = relay.Function([], output)
mod['func_14857'] = func_14857
mod = relay.transform.InferType()(mod)
mutated_mod['func_14857'] = func_14857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14857_call = mutated_mod.get_global_var('func_14857')
call_14858 = func_14857_call()
output = call_14858
func_14859 = relay.Function([], output)
mutated_mod['func_14859'] = func_14859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12138_call = mod.get_global_var('func_12138')
func_12140_call = mutated_mod.get_global_var('func_12140')
call_14875 = relay.TupleGetItem(func_12138_call(), 0)
call_14876 = relay.TupleGetItem(func_12140_call(), 0)
output = relay.Tuple([call_14875,])
output2 = relay.Tuple([call_14876,])
func_14884 = relay.Function([], output)
mod['func_14884'] = func_14884
mod = relay.transform.InferType()(mod)
mutated_mod['func_14884'] = func_14884
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14884_call = mutated_mod.get_global_var('func_14884')
call_14885 = func_14884_call()
output = call_14885
func_14886 = relay.Function([], output)
mutated_mod['func_14886'] = func_14886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7047_call = mod.get_global_var('func_7047')
func_7048_call = mutated_mod.get_global_var('func_7048')
call_14935 = relay.TupleGetItem(func_7047_call(), 0)
call_14936 = relay.TupleGetItem(func_7048_call(), 0)
output = call_14935
output2 = call_14936
func_14953 = relay.Function([], output)
mod['func_14953'] = func_14953
mod = relay.transform.InferType()(mod)
output = func_14953()
func_14954 = relay.Function([], output)
mutated_mod['func_14954'] = func_14954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6738_call = mod.get_global_var('func_6738')
func_6739_call = mutated_mod.get_global_var('func_6739')
call_14996 = func_6738_call()
call_14997 = func_6738_call()
output = relay.Tuple([call_14996,])
output2 = relay.Tuple([call_14997,])
func_14998 = relay.Function([], output)
mod['func_14998'] = func_14998
mod = relay.transform.InferType()(mod)
output = func_14998()
func_14999 = relay.Function([], output)
mutated_mod['func_14999'] = func_14999
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12029_call = mod.get_global_var('func_12029')
func_12031_call = mutated_mod.get_global_var('func_12031')
call_15006 = relay.TupleGetItem(func_12029_call(), 0)
call_15007 = relay.TupleGetItem(func_12031_call(), 0)
output = relay.Tuple([call_15006,])
output2 = relay.Tuple([call_15007,])
func_15008 = relay.Function([], output)
mod['func_15008'] = func_15008
mod = relay.transform.InferType()(mod)
output = func_15008()
func_15009 = relay.Function([], output)
mutated_mod['func_15009'] = func_15009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5180_call = mod.get_global_var('func_5180')
func_5181_call = mutated_mod.get_global_var('func_5181')
call_15078 = relay.TupleGetItem(func_5180_call(), 0)
call_15079 = relay.TupleGetItem(func_5181_call(), 0)
output = call_15078
output2 = call_15079
func_15090 = relay.Function([], output)
mod['func_15090'] = func_15090
mod = relay.transform.InferType()(mod)
output = func_15090()
func_15091 = relay.Function([], output)
mutated_mod['func_15091'] = func_15091
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15128 = relay.var("var_15128", dtype = "float32", shape = (10, 7, 15))#candidate|15128|(10, 7, 15)|var|float32
uop_15129 = relay.sigmoid(var_15128.astype('float32')) # shape=(10, 7, 15)
func_14648_call = mod.get_global_var('func_14648')
func_14650_call = mutated_mod.get_global_var('func_14650')
call_15139 = func_14648_call()
call_15140 = func_14648_call()
func_14256_call = mod.get_global_var('func_14256')
func_14258_call = mutated_mod.get_global_var('func_14258')
call_15149 = func_14256_call()
call_15150 = func_14256_call()
func_6571_call = mod.get_global_var('func_6571')
func_6573_call = mutated_mod.get_global_var('func_6573')
call_15157 = func_6571_call()
call_15158 = func_6571_call()
output = relay.Tuple([uop_15129,call_15139,call_15149,call_15157,])
output2 = relay.Tuple([uop_15129,call_15140,call_15150,call_15158,])
func_15160 = relay.Function([var_15128,], output)
mod['func_15160'] = func_15160
mod = relay.transform.InferType()(mod)
mutated_mod['func_15160'] = func_15160
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15161 = relay.var("var_15161", dtype = "float32", shape = (10, 7, 15))#candidate|15161|(10, 7, 15)|var|float32
func_15160_call = mutated_mod.get_global_var('func_15160')
call_15162 = func_15160_call(var_15161)
output = call_15162
func_15163 = relay.Function([var_15161], output)
mutated_mod['func_15163'] = func_15163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13132_call = mod.get_global_var('func_13132')
func_13133_call = mutated_mod.get_global_var('func_13133')
call_15167 = relay.TupleGetItem(func_13132_call(), 3)
call_15168 = relay.TupleGetItem(func_13133_call(), 3)
output = relay.Tuple([call_15167,])
output2 = relay.Tuple([call_15168,])
func_15189 = relay.Function([], output)
mod['func_15189'] = func_15189
mod = relay.transform.InferType()(mod)
mutated_mod['func_15189'] = func_15189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15189_call = mutated_mod.get_global_var('func_15189')
call_15190 = func_15189_call()
output = call_15190
func_15191 = relay.Function([], output)
mutated_mod['func_15191'] = func_15191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10043_call = mod.get_global_var('func_10043')
func_10044_call = mutated_mod.get_global_var('func_10044')
call_15222 = func_10043_call()
call_15223 = func_10043_call()
func_10653_call = mod.get_global_var('func_10653')
func_10655_call = mutated_mod.get_global_var('func_10655')
call_15229 = relay.TupleGetItem(func_10653_call(), 1)
call_15230 = relay.TupleGetItem(func_10655_call(), 1)
func_12138_call = mod.get_global_var('func_12138')
func_12140_call = mutated_mod.get_global_var('func_12140')
call_15239 = relay.TupleGetItem(func_12138_call(), 0)
call_15240 = relay.TupleGetItem(func_12140_call(), 0)
func_10555_call = mod.get_global_var('func_10555')
func_10558_call = mutated_mod.get_global_var('func_10558')
var_15242 = relay.var("var_15242", dtype = "uint16", shape = (1200,))#candidate|15242|(1200,)|var|uint16
call_15241 = relay.TupleGetItem(func_10555_call(relay.reshape(var_15242.astype('uint16'), [15, 16, 5]), relay.reshape(var_15242.astype('uint16'), [15, 16, 5]), ), 0)
call_15243 = relay.TupleGetItem(func_10558_call(relay.reshape(var_15242.astype('uint16'), [15, 16, 5]), relay.reshape(var_15242.astype('uint16'), [15, 16, 5]), ), 0)
func_6785_call = mod.get_global_var('func_6785')
func_6786_call = mutated_mod.get_global_var('func_6786')
call_15259 = relay.TupleGetItem(func_6785_call(), 1)
call_15260 = relay.TupleGetItem(func_6786_call(), 1)
func_8353_call = mod.get_global_var('func_8353')
func_8355_call = mutated_mod.get_global_var('func_8355')
call_15262 = relay.TupleGetItem(func_8353_call(), 0)
call_15263 = relay.TupleGetItem(func_8355_call(), 0)
func_12917_call = mod.get_global_var('func_12917')
func_12919_call = mutated_mod.get_global_var('func_12919')
call_15269 = relay.TupleGetItem(func_12917_call(), 0)
call_15270 = relay.TupleGetItem(func_12919_call(), 0)
output = relay.Tuple([call_15222,call_15229,call_15239,call_15241,var_15242,call_15259,call_15262,call_15269,])
output2 = relay.Tuple([call_15223,call_15230,call_15240,call_15243,var_15242,call_15260,call_15263,call_15270,])
func_15271 = relay.Function([var_15242,], output)
mod['func_15271'] = func_15271
mod = relay.transform.InferType()(mod)
var_15272 = relay.var("var_15272", dtype = "uint16", shape = (1200,))#candidate|15272|(1200,)|var|uint16
output = func_15271(var_15272)
func_15273 = relay.Function([var_15272], output)
mutated_mod['func_15273'] = func_15273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10043_call = mod.get_global_var('func_10043')
func_10044_call = mutated_mod.get_global_var('func_10044')
call_15354 = func_10043_call()
call_15355 = func_10043_call()
output = call_15354
output2 = call_15355
func_15357 = relay.Function([], output)
mod['func_15357'] = func_15357
mod = relay.transform.InferType()(mod)
output = func_15357()
func_15358 = relay.Function([], output)
mutated_mod['func_15358'] = func_15358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5378_call = mod.get_global_var('func_5378')
func_5379_call = mutated_mod.get_global_var('func_5379')
call_15377 = relay.TupleGetItem(func_5378_call(), 0)
call_15378 = relay.TupleGetItem(func_5379_call(), 0)
output = call_15377
output2 = call_15378
func_15392 = relay.Function([], output)
mod['func_15392'] = func_15392
mod = relay.transform.InferType()(mod)
output = func_15392()
func_15393 = relay.Function([], output)
mutated_mod['func_15393'] = func_15393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11253_call = mod.get_global_var('func_11253')
func_11254_call = mutated_mod.get_global_var('func_11254')
call_15446 = relay.TupleGetItem(func_11253_call(), 0)
call_15447 = relay.TupleGetItem(func_11254_call(), 0)
output = call_15446
output2 = call_15447
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
func_15392_call = mod.get_global_var('func_15392')
func_15393_call = mutated_mod.get_global_var('func_15393')
call_15480 = func_15392_call()
call_15481 = func_15392_call()
output = call_15480
output2 = call_15481
func_15482 = relay.Function([], output)
mod['func_15482'] = func_15482
mod = relay.transform.InferType()(mod)
mutated_mod['func_15482'] = func_15482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15482_call = mutated_mod.get_global_var('func_15482')
call_15483 = func_15482_call()
output = call_15483
func_15484 = relay.Function([], output)
mutated_mod['func_15484'] = func_15484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8763_call = mod.get_global_var('func_8763')
func_8765_call = mutated_mod.get_global_var('func_8765')
call_15594 = relay.TupleGetItem(func_8763_call(), 3)
call_15595 = relay.TupleGetItem(func_8765_call(), 3)
func_11253_call = mod.get_global_var('func_11253')
func_11254_call = mutated_mod.get_global_var('func_11254')
call_15642 = relay.TupleGetItem(func_11253_call(), 0)
call_15643 = relay.TupleGetItem(func_11254_call(), 0)
func_4319_call = mod.get_global_var('func_4319')
func_4324_call = mutated_mod.get_global_var('func_4324')
var_15656 = relay.var("var_15656", dtype = "float32", shape = (320,))#candidate|15656|(320,)|var|float32
const_15657 = relay.const([-3,9,7,-4,-6,3,2,-2,-8,-2,-2,4,3,-5,5,-2,7,6,-5,-2,9,-6,-5,-2,9,-4,8,-9,2,-4,1,5,9,1,2,-5,-9,4,1,-8,3,-3,10,2,5,-8,3,-4,5,-6,-9,9,-4,-3,-2,-7,-5,-4,4,6,3,6,5,6,-3,10,3,-1,4,-6,-9,1,-5,8,2,-7,-5,-1,-2,4,-9,-9,-6,3,-6,-8,2,-6,4,-4,-9,-3,5,9,-1,3,9,-4,2,-5,-4,1,2,-3,-5,-7,10,-1,2,-2,-2,2,-9,-4,-4,9,-4,6,-10,-4,-5,-1,9,-2,9,5,-3,3,-5,-2,8,9,-2,7,3,8,10,-7,-1,-1,4,-4,-3,6,-5,-7,10,4,2,-5,-1,-6,-4,10,-1,8,5,2,-8,-7,9,-6,1,-10,-9,1,1,1,-10,1,-1,9,-10,5,-3,10,6,10,4,-2,6,5,3,-3,8,-6,-4,5,10,-1,-2,-3,-5,-8,5,-5,5,10,-7,-3,-8,6,-8,3,2,-8,-5,3,-6,-10,-4,3,7,9,8,-1,-3,-8,9,-6,7,3,7,-3,-10,-5,10,-4,-5,2,-5,10,1,6,1,-9,5,2,2,6,-6,6,3,2,-1,3,-9,-3,-3,10,-10,-2,-3,-9,-10,8,-10,-4,2,-2,2,10,-8,-4,1,-5,-5,8,-3,-4,3,-9,-4,-9,8,-1,9,-4,6,8,-1,10,1,-3,-4,7,9,-4,8,-1,-5,1,-6,10,2,-9,2,9,7,10,-1,1,-5,-4,8,-3,8,8,-8,5,-8,-3,6,-6,5,6,-2,-7,4,2,-5,-9,-9,-6,-5,7,9,-4,3,10,5,-6,-7,-8,4,-4,-6,-3,-10,-4,-4,-8,10,-10,3,2,7,9,-3,-6,-6,8,-5,-9,-10,8,1,-6,10,-5,-5,-1,7,8,-6,6,7,3,5,-7,-4,-10,2,7,2,-5,1,1,5,-7,-6,-2,-9,4,-9,-10,5,8,-3,-9,9,4,-9,5,4,6,6,-2,-7,10,7,-8,7,-8,-5,9,-1,1,6,4,9,-10,10,-2,8,2,2,-8,8,-3,-2,-4,-3,-3,-2,-1,-8,9,-2,-4,5,-6,8,7,-9,-8,5,8,-8,9,9,-4,-10,7,-4,-4,9,-5,3,2,4,-7,-3,-7,5,2,5,-2,-8,8,-4,-10,-2,1,-9,-1,2,-10,-10,-7,-2,-10,-6,3,-1,-6,3,9,3,5,2,2,4,10,-10,1,-5,-8,-1,-5,-4,-9,-6,-4,-8,-8,-3,-4,-4,-10,-1,-4,-2,-7,5,-7,-2,-6,7,-7,9,7,8,8,6,-4,-1,-5,-5,5,-4,-1,-3,7,6,-6,1,-6,5,-1,-4,-9,-5,7,7,-2,-6,-9,1,-8,-10,-4,8,-10,-6,5,5,-6,-10,-2,4,-10,-8,-9,7,-6,2,9,-1,-4,-9,-8,4,-5,-6,-3,-3,-1,6,-10,7,-1,7,8,9,5,-2,-2,-7,-3,6,-3,1,-9,-6,-1,6,-2,1,3,4,8,2,-2,-7,-2,-3,9,1,-2,-9,-1,-2,-2,-5,-5,-4,6,-10,-5,-3,7,3,9,-8,-2,3,-5,-6,-10,-9,-1,5,-9,6,-2,-2,-7,9,-1,-9,5,6,-7,-5,7,-9,7,6,10,9,-4,-3,7,9,8,-1,-1,10,-3,-4,-1,9,-8,-3,8,10,-4,-5,4,1,3,4,-10,2,3,6,-9,-1,9,-7,9,-10,-2,-6,-10,-10,-8,7,-1,3,-4,-8,-3,2,-5,10,-6,-7,-5,5,-9,-10,-9,6,7,6,10,6,4,-5,9,-3,6,-5,4,-8,-7,3,-7,-10,10,-6,1,-4,-4,-4,-6,9,-8,5,-6,-8,-3,-9,-9,5,-4,-10,6,1,-2,-2,3,-10,-6,6,10,-5,4,5,4,3,-4,-4,-4,10,-10,-4,-4,6,1,-3,6,8,-3,-3,5,-6,8,1,7,-2,4,1,-2,9,1,-6,10,-8,7,2,9,4,10,-3,-5,-3,1,-6,-3,6,-4,10,6,-9,-1,-6,-8,8,-6,-2,-4,-9,-1,7,9,-7,-4,9,6,3,-8,6,1,-4,6,7,3,4,2,-7,5,-4,-2,8,-2,5,-4,-7,-8,-4,-7,4], dtype = "int16")#candidate|15657|(825,)|const|int16
const_15658 = relay.const([5.740156,-0.298332,-3.267082,1.263587,-9.425224,-0.329817,6.285947,5.799174,3.975578,-1.762231,-7.836578,-9.438393,-3.148957,7.995878,-8.460478,0.530809,8.912459,6.895515,-3.807436,6.449976,-6.179158,-6.061291,6.854326,7.733863,0.159572,3.122514,9.062979,-8.203846,0.813156,5.233199,6.395358,1.116362,-3.882003,-3.718484,1.163140,8.197522,0.485326,7.434227,5.086031,4.903033,-2.805420,-8.652336,4.306724,4.594415,-1.268995,-9.080395,5.223377,-1.211376], dtype = "float64")#candidate|15658|(48,)|const|float64
call_15655 = relay.TupleGetItem(func_4319_call(relay.reshape(var_15656.astype('float32'), [320,]), relay.reshape(const_15657.astype('int16'), [5, 165]), relay.reshape(const_15658.astype('float64'), [1, 48]), ), 3)
call_15659 = relay.TupleGetItem(func_4324_call(relay.reshape(var_15656.astype('float32'), [320,]), relay.reshape(const_15657.astype('int16'), [5, 165]), relay.reshape(const_15658.astype('float64'), [1, 48]), ), 3)
output = relay.Tuple([call_15594,call_15642,call_15655,var_15656,const_15657,const_15658,])
output2 = relay.Tuple([call_15595,call_15643,call_15659,var_15656,const_15657,const_15658,])
func_15666 = relay.Function([var_15656,], output)
mod['func_15666'] = func_15666
mod = relay.transform.InferType()(mod)
var_15667 = relay.var("var_15667", dtype = "float32", shape = (320,))#candidate|15667|(320,)|var|float32
output = func_15666(var_15667)
func_15668 = relay.Function([var_15667], output)
mutated_mod['func_15668'] = func_15668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8050_call = mod.get_global_var('func_8050')
func_8052_call = mutated_mod.get_global_var('func_8052')
call_15720 = relay.TupleGetItem(func_8050_call(), 0)
call_15721 = relay.TupleGetItem(func_8052_call(), 0)
func_7314_call = mod.get_global_var('func_7314')
func_7318_call = mutated_mod.get_global_var('func_7318')
const_15758 = relay.const([[-8.723564,-4.920619,6.892805,2.023607,-5.864972,-0.370766,-8.566964,6.131818,9.987585,-1.562692,9.015630,9.240424,6.458204,-0.445035,6.552673,-6.678896,9.000872,-0.657809,-9.044708,-1.861906,9.951957,-8.392424,6.828174,-9.723462,5.062877,1.185821,-9.958644,6.329084,4.875080,-4.336872,2.426990,6.694494,9.621997,-4.887610,6.522242,-1.049760,6.580741,5.690283,-3.550829,1.759341,-4.698360,-7.924703,-6.655214,-7.688579,-5.948991,-8.704806,4.834272,-0.947529,6.098924,-2.261424,-2.234811,-1.141790,-0.572486,-3.700042,6.427031,-4.304518,4.248371,-8.591512,9.815218,5.860293,6.316241,8.339445,4.927793,8.858522,-0.449652,-1.172934,4.189144,-8.706995,-4.157683,-2.809080,4.623023,0.069967,-7.627872,-4.899981,1.747639,9.171696,7.269723,0.174497,-0.122830,6.915134]], dtype = "float64")#candidate|15758|(1, 80)|const|float64
const_15759 = relay.const([-10,-1,5,8,-9,-10,7,1,-3,6,8,-4,-3,9,8,-7,10,-9,-7,-3,-4,-9,8,-4,8,6,8,-1,6,-8,9,-5,5,-3,1,-9,8,-7,-9,-7,4,4,-5,5,-6,-8,-2,3,-6,-10,-10,-3,8,-3,4,-5,-5,-2,-4,4,2,5,4,9,-4,-9,9,-3,4,3,7,-6,-7,-3,-5,-8,-8,1,3,-5,9,1,8,5,1,-9,8,-3,4,-3,-2,6,-6,-5,8,-5,-4,7,2,3,1,-4,-7,-1,2,2,5,-7,8,1,1,-3,2,-8,-1,8,3,9,8,5,-4,-5,8,1,3,9,7,1,-9,4,10,-2,-3,-4,-10,10,-7,-4,-4,-8,6,10,-9,-3,-10,10,6,-4,2,-9,-9,8,-1,-1,-5,1,-6,5,4,6,4,5,-6,10,-8,-2,-5,3,1,2,-4,-9,3,-6,3,-2,-7,-8,7,3,-6,-4,-3,8,2,-2,-2,7,-7,6,-6,-9,-5,-6,-5,-8,3,-4,9,-2,4,5,5,5,6,1,8,-5,-5,5,-1,2,3,10,-2,10,6,-5,-9,10,2,5,1,4,2,-7,2,-7,-9,-4,-1,6,2,-8,-2,4,10,-5,-1,7,10,-4,-7,-5,8,-7,6,6,-5,-8,-3,-2,-6,-5,9,10,-8,-10,-7,-1,-8,4,2,-3,4,-7,-6,1,-7,10,-8,5,-7,1,2,9,-10,4,-4,-8,-8,7,-3,7,5,-8,-10,-1,8,8,-3,9,-3,5,10,8,-10,4,-5,7,-10,5,8,6,-7,7,3,-3,-1,-6,4,10,10,9,-9,-7,1,-9,-9,6,-1,-6,-3,3,-9,-6,2,9,2,-9,-6,9,10,6,-5,5,-9,2,-10,-5,-3,-4,-7,-9,2,-7,4,-6,4,-4,-6,6,-10,5,-5,-8,1,5,8,-6,-10,9,-9,-10,6,-3,-3,-8,-9,-2,5,-3,4,6,-2,2,-7,7,5,10,-9,6,4,-4,8,7,6,2,10,1,2,5,4,5,7,-1,-10,10,-10,9,10,3,-10,5,-5,-1,2,4,7,-5,5,-1,-4,1,7,4,-7,-1,-4,-6,-5,-7,4,2,3,6,-5,4,-9,-5,-6,2,-8,2,-1,4,-7,2,-2,-3,-2,-6,-7,6,7,2,10,1,-1,1,-3,-8,4,4,-4,5,-7,1,-1,-9,8,-4,-9,6,9,-2,10,3,-1,2,-3,1,5,-1,1,-7,-5,-7,7,4,9,-8,-7,-3,-7,4,-3,9,9,6,-2,-6,3,3,5,8,5,-4,-7,1,-3,4,-9,4,3,-5,1,5,-7,6,6,-7,-9,1,8,-10,6,7,-6,-5,-8,-5,-4,-7,-7,-4,-8,-3,-3,-1,-8,-4,-4,2,-9,-9,9,-8,-4,-5,-9,-7,-3,-1,7,-9,-4,1,-1,10,-2,-9,-2,-6,-3,1,-2,-6,-9,1,-1,-10,3,-5,-8,6,-1,-3,-3,3,-9,-5,-1,8,-8,-5,-1,-3,10,-1,-10,-10,-4,-8,-1,-1,5,5,-9,-7,2,-7,9,-7,8,7,5,-3,-10,3,1,-4,-4,-4,2,9,3,6,5,-3,9,3,9,2,6,-3,-1,-5,7,-7,1,2,-1,-8,-2,-1,4,7,-9,-5,4,4,-6,-2,6,-4,5,-1,-4,5,1,-7,10,-10,-2,-6,2,4,6,-5,-5,-1,4,-1,2,-4,-1,-10,4,-2,3,-3,-9,-7,2,9,-8,10,-2,-10,-6,-9,-7,10,7,10,-1,8,-1,-4,6,2,6,8,2,2,4,7,-10,-3,-2,-8,-5,4,1,8,-3,-3,-2,-9,-9,-4,-4,-2,-9,-1,7,5,-6,-7,7,4,4,1,6,-2,-10,-6,7,-7,3,9,-5,-2,-1,8,2,10,-9,6,8,10,2,2,-8,-8,-7,2,1,-5,-1,-2,6,3,-2,3,-6,-10,3,-10,3,1,-6,5,7,2,4,-4,-6,8,-5,8,5,10,1,8,-9,-5,-4,-4,2,-8,10,9,-9,1,-9,5,-10,4,6,-9,-3,-4,5,-5,-4,5,4,-7,10,-9,1,-5,-9,-4,2,-2,8,-1,3,-1,-2,-10,-10,-1,9,1,2,-10,-6,-7,-10,5,-6,2,-6,-8,-9,5,9,10,-6,5,9], dtype = "int16")#candidate|15759|(825,)|const|int16
call_15757 = relay.TupleGetItem(func_7314_call(relay.reshape(const_15758.astype('float64'), [80,]), relay.reshape(const_15759.astype('int16'), [825,]), ), 1)
call_15760 = relay.TupleGetItem(func_7318_call(relay.reshape(const_15758.astype('float64'), [80,]), relay.reshape(const_15759.astype('int16'), [825,]), ), 1)
func_13692_call = mod.get_global_var('func_13692')
func_13694_call = mutated_mod.get_global_var('func_13694')
call_15762 = relay.TupleGetItem(func_13692_call(), 0)
call_15763 = relay.TupleGetItem(func_13694_call(), 0)
output = relay.Tuple([call_15720,call_15757,const_15758,const_15759,call_15762,])
output2 = relay.Tuple([call_15721,call_15760,const_15758,const_15759,call_15763,])
func_15769 = relay.Function([], output)
mod['func_15769'] = func_15769
mod = relay.transform.InferType()(mod)
mutated_mod['func_15769'] = func_15769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15769_call = mutated_mod.get_global_var('func_15769')
call_15770 = func_15769_call()
output = call_15770
func_15771 = relay.Function([], output)
mutated_mod['func_15771'] = func_15771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15189_call = mod.get_global_var('func_15189')
func_15191_call = mutated_mod.get_global_var('func_15191')
call_15836 = relay.TupleGetItem(func_15189_call(), 0)
call_15837 = relay.TupleGetItem(func_15191_call(), 0)
func_32_call = mod.get_global_var('func_32')
func_35_call = mutated_mod.get_global_var('func_35')
var_15847 = relay.var("var_15847", dtype = "float64", shape = (48,))#candidate|15847|(48,)|var|float64
call_15846 = relay.TupleGetItem(func_32_call(relay.reshape(var_15847.astype('float64'), [2, 4, 6])), 0)
call_15848 = relay.TupleGetItem(func_35_call(relay.reshape(var_15847.astype('float64'), [2, 4, 6])), 0)
bop_15849 = relay.less(call_15846.astype('bool'), relay.reshape(var_15847.astype('bool'), relay.shape_of(call_15846))) # shape=(2, 4, 6)
bop_15852 = relay.less(call_15848.astype('bool'), relay.reshape(var_15847.astype('bool'), relay.shape_of(call_15848))) # shape=(2, 4, 6)
func_8003_call = mod.get_global_var('func_8003')
func_8005_call = mutated_mod.get_global_var('func_8005')
call_15867 = relay.TupleGetItem(func_8003_call(), 2)
call_15868 = relay.TupleGetItem(func_8005_call(), 2)
func_5004_call = mod.get_global_var('func_5004')
func_5007_call = mutated_mod.get_global_var('func_5007')
const_15879 = relay.const([-9.311271,7.795131,1.454984,3.519379,0.990254,5.547200,-1.758303,6.529424,4.385015,-6.142335,4.327006,3.856701,7.202147,-0.508111,-1.858690,-0.263976,0.411211,-3.229729,-4.772086,9.785408,-7.229539,-1.670124,-4.223328,-8.657323,5.067166,6.280528,-6.966018,0.875037,3.978460,-5.874976,7.814372,-0.412047,-8.912031,6.128674,-2.876322,-6.405964,0.010288,-6.853602,8.843121,4.108632,3.143600,1.760749,3.537503,3.643421,-6.199753,0.383096,8.804387,4.427461,-6.592332,-4.342853,7.912604,2.167105,-7.587723,-7.613109,-9.229726,-5.744897,-5.305468,-6.142864,4.114362,-8.487432,8.398160,6.159824,-9.000156,9.723660,3.275573,4.718201,-9.445600,7.153365,-2.037817,-9.497058,-4.181511,-8.246114,0.813510,-3.303600,9.199835,-2.060716,-8.172652,4.731619,-9.214241,3.559448,-0.967281,-6.917141,2.647637,2.801480,-0.383452,3.911719,5.553245,9.306570,-1.004250,0.233952,5.393306,-3.771904,5.289097,-5.319252,-2.223290,7.219874,-1.458323,-7.894136,1.092809,-0.936456], dtype = "float64")#candidate|15879|(100,)|const|float64
call_15878 = relay.TupleGetItem(func_5004_call(relay.reshape(const_15879.astype('float64'), [1, 10, 10])), 2)
call_15880 = relay.TupleGetItem(func_5007_call(relay.reshape(const_15879.astype('float64'), [1, 10, 10])), 2)
func_9689_call = mod.get_global_var('func_9689')
func_9691_call = mutated_mod.get_global_var('func_9691')
call_15903 = func_9689_call()
call_15904 = func_9689_call()
func_7346_call = mod.get_global_var('func_7346')
func_7348_call = mutated_mod.get_global_var('func_7348')
call_15925 = func_7346_call()
call_15926 = func_7346_call()
func_13522_call = mod.get_global_var('func_13522')
func_13523_call = mutated_mod.get_global_var('func_13523')
call_15952 = relay.TupleGetItem(func_13522_call(), 0)
call_15953 = relay.TupleGetItem(func_13523_call(), 0)
func_11039_call = mod.get_global_var('func_11039')
func_11041_call = mutated_mod.get_global_var('func_11041')
var_15974 = relay.var("var_15974", dtype = "int16", shape = (825,))#candidate|15974|(825,)|var|int16
call_15973 = relay.TupleGetItem(func_11039_call(relay.reshape(var_15974.astype('int16'), [825,])), 5)
call_15975 = relay.TupleGetItem(func_11041_call(relay.reshape(var_15974.astype('int16'), [825,])), 5)
func_7132_call = mod.get_global_var('func_7132')
func_7137_call = mutated_mod.get_global_var('func_7137')
var_15977 = relay.var("var_15977", dtype = "float64", shape = (80,))#candidate|15977|(80,)|var|float64
var_15978 = relay.var("var_15978", dtype = "int16", shape = (165, 1))#candidate|15978|(165, 1)|var|int16
call_15976 = relay.TupleGetItem(func_7132_call(relay.reshape(var_15977.astype('float64'), [80,]), relay.reshape(var_15974.astype('int16'), [825,]), relay.reshape(var_15978.astype('int16'), [165,]), ), 1)
call_15979 = relay.TupleGetItem(func_7137_call(relay.reshape(var_15977.astype('float64'), [80,]), relay.reshape(var_15974.astype('int16'), [825,]), relay.reshape(var_15978.astype('int16'), [165,]), ), 1)
func_13846_call = mod.get_global_var('func_13846')
func_13851_call = mutated_mod.get_global_var('func_13851')
const_15995 = relay.const([-0.935907,-4.827733,-1.152647,-7.776720,-3.864789,0.746235,-7.217678,2.009522,9.895404,-3.711183,0.451409,4.294058,-3.080136,0.302746,9.290554,5.681523,3.809110,-0.675096,8.238958,-6.704778,-9.788101,2.999923,-8.969932,8.384577,-6.636429,-7.668299,9.677928,-3.947761,1.707696,-2.378274,6.268502,-4.625021,1.268094,-0.580551,-8.832059,-5.956004,6.945308,4.990147,0.492101,9.278682,-6.637017,0.226929,2.406766,2.313506,9.299214,6.005716,-7.410805,6.762242,6.007046,-3.625126,0.452023,-2.921195,-9.290125,-0.869102,-4.510712,8.869884,6.447756,6.399256,-5.716840,4.027424,-2.344937,-5.878359,0.879722,-1.557202,-6.749847,-5.078725,5.589076,-9.724430,-4.457571,3.458551,-6.558882,4.685131,-0.146779,7.987363,-4.842960,-7.293518,2.133604,4.717450,9.974269,7.483698,-5.907183,2.073699,8.763163,8.814206,-9.302630,-4.698463,-2.914267,7.641253,-6.827451,3.683284,2.457275,3.991488,0.736750,1.929579,-2.427689,-2.170958,-2.916582,2.904339,0.689139,0.638123,5.897913,-2.977184,-9.160262,-9.069336,-0.730627,9.561014,-7.862337,2.339254,5.621070,-0.239351,9.359889,-4.681804,-7.936952,5.587364,-3.858030,9.142318,2.328210,0.594194,7.112471,-5.064222,-9.484260,-2.989581,6.784131,-1.387054,-4.206135,-6.139918,3.048224,-2.646673,-6.109259,0.235426,-9.516430,0.507706,-3.118006,5.578243,-6.842618,-5.211022,4.851446,1.994743,-7.926666,2.830088,-0.613335,-7.557896,-7.371366,8.271268,9.879284,-1.079111,-8.461253,9.590415,-8.474581,-6.532952,-9.845955,3.062084,5.468149,-0.993369,-5.248824,6.947764,-6.498521,-4.752246,-1.761175,6.409390,-7.265031,1.610217,1.850558,-4.145234,-4.734170,2.715282,7.623554,-4.537573,1.577092,-9.761517,7.281009,8.745001,3.833485,-4.159770,9.066515,2.415682,8.587466,-7.809663,5.145513,6.754711,-4.201554,4.466749,8.375886,-2.904211,-1.262884,3.774566,-3.149068,4.334865,-6.352962,0.883777,-6.042514,-5.572444,-9.564995,-8.190011,3.149970,4.462463,-8.897628,0.572583,-2.377145,1.392198,-5.751306,-6.502022,7.583219,-9.303379,-9.937241,8.120344,0.555641,-8.730057,3.425207,4.162672,-6.319633,-6.877884,4.220411,4.161694,7.061672,2.355463,5.673310,5.921293,6.102029,-6.352458,9.370662,-0.572747,6.818648,-1.177916,-9.738571,8.086222,-9.842997,7.520489,7.979498,-4.249400,6.146532,-8.933439,7.323016,6.585379,-8.935183,-2.248433,-9.857544,-2.747003,-0.541769,-9.000086,-0.677515,5.833534,2.745348,2.878524,5.452461,7.049309,4.965804,6.752554,3.335867,2.301778,9.889810,-1.965699,1.701069,2.525727,9.193864,-1.343235,-8.002984,0.887726,-2.763610,-3.651753,-5.539402,3.507836,-5.162623,-4.533571,8.944778,9.017743,-9.937580,-1.759381,-7.213471,2.161563,4.980126,5.614788,4.881694,2.050257,8.030134,-2.493105,-3.787454,0.104856,-5.907224,-2.061057,-2.694964,-8.296163,9.426096,-4.017978,2.108435,-1.827749,6.116707,-6.108244,-3.038517,-9.697466,7.400632,0.667561,-5.237235,-3.945698,-4.118213,7.933670,-5.364363,4.873039,-4.949633,1.515780,1.241229,0.787812,-2.519923,-1.827035,9.148188,-5.042277,9.213680,-2.825044,0.170895,-6.945614,-6.060387,-7.787002,-1.022596,-7.528877,8.216998,-1.961847,9.017474,2.882261,6.621288,-1.294930], dtype = "float32")#candidate|15995|(320,)|const|float32
call_15994 = relay.TupleGetItem(func_13846_call(relay.reshape(call_15878.astype('float64'), [48,]), relay.reshape(var_15978.astype('int16'), [165,]), relay.reshape(const_15995.astype('float32'), [320,]), ), 2)
call_15996 = relay.TupleGetItem(func_13851_call(relay.reshape(call_15878.astype('float64'), [48,]), relay.reshape(var_15978.astype('int16'), [165,]), relay.reshape(const_15995.astype('float32'), [320,]), ), 2)
output = relay.Tuple([call_15836,bop_15849,call_15867,call_15878,const_15879,call_15903,call_15925,call_15952,call_15973,var_15974,call_15976,var_15977,var_15978,call_15994,const_15995,])
output2 = relay.Tuple([call_15837,bop_15852,call_15868,call_15880,const_15879,call_15904,call_15926,call_15953,call_15975,var_15974,call_15979,var_15977,var_15978,call_15996,const_15995,])
func_16005 = relay.Function([var_15847,var_15974,var_15977,var_15978,], output)
mod['func_16005'] = func_16005
mod = relay.transform.InferType()(mod)
mutated_mod['func_16005'] = func_16005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16005_call = mutated_mod.get_global_var('func_16005')
var_16007 = relay.var("var_16007", dtype = "float64", shape = (48,))#candidate|16007|(48,)|var|float64
var_16008 = relay.var("var_16008", dtype = "int16", shape = (825,))#candidate|16008|(825,)|var|int16
var_16009 = relay.var("var_16009", dtype = "float64", shape = (80,))#candidate|16009|(80,)|var|float64
var_16010 = relay.var("var_16010", dtype = "int16", shape = (165, 1))#candidate|16010|(165, 1)|var|int16
call_16006 = func_16005_call(var_16007,var_16008,var_16009,var_16010,)
output = call_16006
func_16011 = relay.Function([var_16007,var_16008,var_16009,var_16010,], output)
mutated_mod['func_16011'] = func_16011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12073_call = mod.get_global_var('func_12073')
func_12075_call = mutated_mod.get_global_var('func_12075')
call_16039 = relay.TupleGetItem(func_12073_call(), 0)
call_16040 = relay.TupleGetItem(func_12075_call(), 0)
func_13182_call = mod.get_global_var('func_13182')
func_13184_call = mutated_mod.get_global_var('func_13184')
const_16044 = relay.const([-8.044137,-4.781447,9.762185,2.743956,-2.808452,-8.852312,6.313068,-1.134802,-9.432120,-3.090856,-8.776027,-1.851314,3.396574,8.388709,-1.730108,6.945648,-9.297925,1.184972,0.192818,-7.340668,3.966643,-9.057162,-6.921839,4.478617,6.049693,1.953651,5.751150,1.809080,-5.561369,2.602128,-6.478924,7.797613,-5.470458,5.652772,8.550713,5.457879,-9.062838,-5.764910,4.285314,3.463572,4.769755,-6.894338,-9.500898,1.836794,4.880651,4.045389,6.694858,-1.039550,0.978685,0.941117,9.947377,8.138321,-1.961200,0.292945,4.040495,-9.657987,2.892083,1.850138,-2.282406,-8.537559,5.591864,-8.486089,-3.774228,3.819097,-5.869645,-2.931493,4.112538,3.663239,1.692221,9.999423,7.597128,5.259449,3.002341,-3.696875,-7.772647,8.768092,7.311309,-0.027739,-3.531748,7.408043,3.952393,-1.511717,-9.236356,-4.401432,-9.344995,-1.557112,-2.906195,-0.638964,6.842530,5.066979,5.453722,0.369479,-7.422008,-6.872658,8.592398,9.619207,-2.790965,-8.786937,4.100657,-9.110342,-6.197578,6.372719,5.784624,-4.834934,6.699251,-5.518582,-3.482000,3.826299,4.888185,7.900653,4.412236,6.233044,9.405383,-4.391362,8.155550,-2.580978,-1.641943,-2.716439,-1.656698,-9.948747,-9.469613,-4.203936,-5.130437,-9.408789,-5.712749,8.552695,-7.014015,9.438092,-7.881971,2.021257,-7.194887,0.482203,9.244503,-9.136901,1.281549,7.314796,0.930085,-7.021866,2.155463,-3.607880,8.921600,-2.452587,-8.125849,0.698747,5.788149,-8.234782,-9.989212,-0.107119,3.823897,5.086447,3.515116,0.952478,5.441468,6.874607,-9.925869,-3.448685,0.080374,0.514487,-5.311385,-6.022094,8.198696,9.710567,-0.115418,-8.716054,4.177602,-7.981335,-5.491562,3.918181,-4.170833,4.883457,-9.525030,-4.274896,-5.388466,-5.836839,-2.698169,-7.878436,5.472784,8.383168,-9.081983,-7.530860,-6.144110,-9.926864,-7.537084,-5.100358,-3.395158,3.972479,3.290829,-6.316970,7.382845,-6.151189,8.236291,-7.111402,-2.854271,9.252338,7.306419,-8.229406,-0.648205,-7.274182,8.985075,0.899102,-0.618749,-2.245486,-6.951507,3.947075,6.782859,4.608398,8.002922,-9.524015,-4.979843,-1.284858,8.485275,4.353862,8.035852,-2.134728,-8.167603,2.931986,-3.714467,-2.548519,-6.214247,-2.941609,0.225436,0.076146,6.651313,-0.636861,2.834901,6.542521,-1.109330,-7.958967,7.518850,-2.767708,0.957158,-5.256543,5.168515,-9.218997,6.323641,-3.299389,2.022026,3.662083,0.662207,-4.860320,-6.858481,7.688709,-0.593895,-3.781852,-7.196822,1.343272,-5.311490,1.899935,-4.536402,-7.391644,-5.090338,-9.306521,-8.426037,9.170793,4.321713,-0.601984,5.727486,-5.270697,3.089068,5.708809,7.746558,4.191080,2.462001,-4.716738,4.198016,6.975251,5.363624,5.287177,0.426001,9.075226,-2.208153,-3.851997,6.610350,1.398351,5.228814,-4.428658,6.478091,1.501643,-6.889628,-3.217021,-1.434181,6.533551,4.753246,4.244155,1.143584,0.133585,-3.718267,-5.339256,1.956203,-2.018456,-2.958352,2.347912,9.369472,-1.115464,-7.384259,0.959768,-8.031336,-2.130519,3.148570,-9.298245,-9.686268,-5.575232,0.427364,-3.225260,-8.457247,-7.252208,7.869788,-4.953467,-7.248159,-8.232722,5.912040,0.619012,3.688074,8.814983,5.773678,5.894410,5.147429,-8.855016,-0.443463,8.579409], dtype = "float32")#candidate|16044|(320,)|const|float32
call_16043 = relay.TupleGetItem(func_13182_call(relay.reshape(const_16044.astype('float32'), [320,])), 1)
call_16045 = relay.TupleGetItem(func_13184_call(relay.reshape(const_16044.astype('float32'), [320,])), 1)
func_12807_call = mod.get_global_var('func_12807')
func_12810_call = mutated_mod.get_global_var('func_12810')
const_16053 = relay.const([[-2.900645,-9.197648,-2.605922,2.891453,3.657836,5.177746,-8.426573,-0.569567,-9.006502,4.443074,2.478235,5.210763,-0.668991,8.848235,-0.619034,7.391483,2.195434,-9.366406,-1.867818,8.561023,5.172453,3.750646,6.953516,-5.417695,9.462612,0.418187,-3.748548,0.184486,8.020681,3.938132,-8.428490,-7.521194,-2.060566,8.303258,9.212725,-8.620317,6.079787,-5.369280,-9.802822,6.081800,-8.638641,-5.343950,2.183019,-6.374833,-2.045185,-3.026747,-6.797354,6.295933,4.645550,0.534512,2.905117,-4.754396,4.527044,0.485185,9.798043,9.036144,8.219893,-5.928717,7.811064,5.069244],[-1.729003,-5.037336,-2.363335,4.219396,-6.209641,-9.138538,0.560995,8.711429,3.709830,-7.164281,0.425536,1.876918,9.933254,4.522247,-0.556883,4.432680,-2.145311,8.823991,1.416565,-0.458837,5.587345,0.258675,3.156185,4.446683,5.324899,9.613915,-5.300216,2.935338,-5.597172,-0.933521,0.073684,0.142418,-8.754792,-1.355177,-8.093439,8.485063,-4.723795,-5.104349,3.837743,-3.367810,1.329285,2.019702,-4.444343,7.930770,6.625066,1.674694,6.646523,-3.389304,5.415785,3.881063,-7.410319,6.617449,1.590065,-9.170099,-2.614166,6.529298,6.403219,3.793333,0.346351,-4.843001],[-9.305033,4.772041,7.757810,6.773535,9.511663,-9.534175,-3.394804,-6.329180,8.066182,-6.443098,7.939102,7.400242,6.842632,7.264073,9.009050,1.120225,6.008947,-3.882858,4.622808,-5.876612,-7.236703,-8.381705,-3.645637,4.999754,6.099917,9.869042,0.602482,2.355203,9.930643,-0.529787,2.376429,0.391988,-8.418133,9.662837,7.763894,-3.535494,-6.316190,-1.949260,5.148953,-9.302380,-2.541801,-1.619743,-4.885152,-2.964317,-9.592809,-0.475885,-4.630925,-7.323724,8.022170,-5.790724,7.663927,1.460074,7.170254,9.212104,1.645430,-6.031444,1.840937,2.224155,-9.513026,-0.314695],[-2.327708,-7.548319,-2.725628,-5.343939,-3.717609,-9.077112,5.052688,1.543184,-2.053434,-0.718177,-9.232651,1.148612,3.887577,7.642301,-7.174792,-4.198130,3.497581,7.965954,3.785316,1.343024,4.770234,-2.085652,4.686274,9.227987,-9.964862,5.155808,-3.556444,-4.206523,-1.362855,-3.340011,8.803096,5.464162,3.469800,-9.754175,-1.045553,4.899189,-2.657955,2.495063,6.481692,7.267945,-0.809586,1.266160,2.920258,-4.793653,0.413662,-5.430736,4.545519,5.846504,-4.458455,3.829638,-8.070450,-0.883276,-1.128356,-5.272487,7.790751,4.155148,6.389193,-8.843638,5.194199,-1.547491],[3.476815,4.407100,-0.311656,-9.242194,7.956887,-7.782602,-6.444393,-6.017034,-2.559779,-4.502140,-7.839687,6.968072,-4.671555,-1.669067,-6.063013,2.313120,1.905124,-2.633951,6.427559,-6.598257,-7.808908,-8.121318,-7.088718,-3.905672,-8.164648,-8.230070,-0.844737,-8.722051,2.969459,-5.190687,1.864076,-7.341109,9.756292,-4.033541,9.489310,1.834686,1.543060,-6.756526,-0.370736,-5.426348,1.871742,7.528611,-8.040208,0.596924,-0.871445,3.010846,4.887690,-4.911071,-0.625128,6.597460,7.448951,-2.705097,6.174828,-6.772989,0.445438,-4.835488,3.355552,-1.337511,2.367839,-6.163248]], dtype = "float32")#candidate|16053|(5, 60)|const|float32
call_16052 = relay.TupleGetItem(func_12807_call(relay.reshape(const_16053.astype('float32'), [3, 10, 10])), 0)
call_16054 = relay.TupleGetItem(func_12810_call(relay.reshape(const_16053.astype('float32'), [3, 10, 10])), 0)
func_10105_call = mod.get_global_var('func_10105')
func_10109_call = mutated_mod.get_global_var('func_10109')
const_16061 = relay.const([8.999978,-4.451444,3.303794,-9.955779,-7.742570,-8.445446,5.446739,-2.210198,-7.790760,-8.825774,1.978120,-5.702189,2.555785,8.773502,5.603750,8.681419,8.480617,1.355308,4.691654,-2.644907,-8.540708,-8.873415,1.395718,-4.295872,-6.557400,-1.164950,-1.675220,1.077532,-2.084828,-1.335059,3.193488,-7.261318,0.739599,4.248700,-7.386581,-3.437839,8.361634,-9.759439,9.900585,-5.066889,-1.995883,2.512638,-6.137065,-7.647199,-3.589980,-2.441046,7.246181,-1.248247,-6.046778,7.027567,2.231901,-7.600872,4.719588,0.080873,3.075804,-8.072956,7.796012,-6.777233,-7.523114,-7.233003,0.524814,-9.706334,-4.873586,0.624315,0.104840,6.816446,-7.217182,7.232793,-4.014180,-4.760154,-7.903805,8.625901,-1.069732,1.896081,2.612758,7.691246,1.208134,9.869847,-8.917962,-6.861511,2.671669,-3.765247,5.565514,7.585030,7.996358,0.918486,3.008681,4.769325,-5.532661,-4.666026,-4.614065,-2.082444,-0.659759,5.551142,-0.978201,-8.186301,8.236902,0.624232,-0.917064,3.972615,-4.617155,3.193698,9.891275,-1.745048,-2.378703,4.339510,-4.598701,-3.058203,5.566350,-8.615597,5.744454,-4.084080,9.934122,-2.834114,-6.166897,3.171456,-5.290796,-1.471815,7.127055,-4.362748,-8.369054,8.788046,8.250940,7.793787,7.403634,0.038367,-2.031678,-7.462021,0.146471,1.320155,-0.172981,6.983239,9.115172,-4.425506,-4.735191,-3.422374,0.137716,2.784434,2.341355,8.739782,-4.184493,-1.354013,-3.358180,5.320686,9.652836,-5.870761,7.626176,-8.152104,3.368139,-2.587833,0.021342,-7.048019,-4.832212,-2.923116,-0.176457,-2.156647,-6.903698,9.959090,3.096458,-3.960079,9.383178,-7.690572,-9.815678,-4.714590,-5.711150,1.338364,7.331528,-9.185760,-1.570092,-7.631793,-5.560472,9.072320,7.689553,-6.653987,3.490389,1.547682,4.466937,-2.893329,-9.235926,3.400868,5.351894,7.063226,7.733516,-9.429831,-0.288902,-8.988341,3.222703,6.574260,8.926603,-7.385702,-2.979515,0.051053,8.132754,-4.564258,-4.666690,-5.369582,-0.713795,2.887581,7.892303,3.012403,-8.492333,1.113026,-5.657086,-5.462283,-6.148130,-3.865823,-1.427342,-2.287360,3.827775,6.651078,-6.886359,9.078464,1.213880,-5.517976,-2.167136,-6.951763,-5.238866,5.045110,-3.246721,-7.535693,-1.156910,-1.344240,-8.848315,-7.597205,5.678210,-5.732770,-2.681933,-4.143924,-4.151213,-3.329591,2.164857,5.849938,-4.275430,-6.346520,-4.802911,1.461491,3.360043,5.675469,-0.529147,-4.597667,4.610274,-2.000480,-0.143461,-8.103418,6.169935,-1.405429,1.290006,-8.449261,-3.334987,4.659241,1.068810,9.474341,-4.088837,1.659112,-6.753909,-0.428170,-9.548157,5.368240,6.205724,3.365115,9.812317,7.632678,2.953242,-4.328017,-2.168037,-9.892948,8.858114,0.446365,-9.940989,-5.943398,-6.710197,-6.770832,0.555371,9.855876,3.228575,-1.864520,-6.694462,-8.227027,3.984033,4.906990,-7.924982,-8.986964,1.426994,3.983842,-3.352331,3.260638,-3.632233,9.828038,7.112081,-7.418939,4.890362,9.958262,1.987550,8.316982,1.532174,-9.264337,-5.354330,6.333359,-2.774734,9.375614,-3.159668,8.368911,-1.153020,9.106954,-8.802555,0.733580,-5.635701,5.559700,-9.923446,-9.811661,-6.882759,3.864285,4.153616,-7.144406,8.802687,-7.163574,-5.837948,-2.367212,-8.523137,4.221242,8.048436,-4.765881,2.193193,4.799736,-8.141425,3.867120,4.597618,7.819083,6.198793,-2.553972,8.485236,5.342523,0.045600,5.062180,5.442336,-6.788946,0.722148,-5.941820,-5.717802,-2.001889,5.271467,9.040233,-5.019754,-7.128328,7.672466,-6.469769,5.514947,-4.488141,2.991669,3.012078,-9.595121,5.179506,-8.904498,9.701238,-1.091070,-2.850851,8.574362,-5.091458,-8.779671,-2.064644,3.642871,3.505199,-2.137192,2.314155,8.479459,-2.276389,-3.033112,9.967984,9.963524,-0.941871,-9.041330,0.037417,-5.000899,2.078724,-9.617419,-3.067887,-5.932467,4.236463,-3.957039,-3.030407,5.513569,8.471211,-8.781914,-3.025709,0.850645,8.690299,2.414087,-4.905401,-1.683285,6.498704,2.719272,3.358602,8.993367,-9.348666,4.501173,8.498002,8.321063,4.180581,4.337188,7.170854,-9.798712,-5.400035,6.814244,9.199000,-1.297131,9.312108,0.556201,8.723854,6.212576,-3.123929,-0.947702,8.024330,-9.005296,9.591892,-0.494394,5.421877,-8.084397,2.846195,-3.208318,3.823922,5.929539,-3.062800,6.471942,7.797533,2.672592,-0.528046,3.609743,6.988519,-8.183216,4.726989,0.252242,9.000146,-7.503077,1.005711,8.462049,9.277072,0.073769,1.040873,4.108989,6.986352,-7.176441,-1.569805,3.269259,-9.684995,-6.669799,4.069009,-4.985677,7.148845,2.093502,3.739371,-0.065496,1.929488,-7.901563,-1.585403,1.646413,-0.677171,3.319652,4.867457,-9.320327,-9.150104,5.324321,-3.492816,-2.020912,-0.560622,-6.454753,8.214656,-8.631908,7.928811,5.515482,-6.129772,7.418858,8.110202,0.776821,-2.933744,-4.160124,-6.108603,-7.349828,5.820268,6.186724,-6.370687,6.313268,-8.672678,-2.697821,-0.097653,1.749736,-9.933751,7.893715,-2.221762,-3.513985,-3.454768,0.666718,-1.248750,3.808679,1.039387,8.469551,-0.940747,3.314249,-6.845977,-1.754255,7.810944,2.766331,2.284657,2.735875,1.879766,-9.288230,-5.203984,-3.320972,5.667380,-2.976737,-6.435335,-9.201063,-3.546059,9.114463,0.528862,5.011460,-8.525817,-4.064680,3.285781,6.027252,0.209844,-0.547270,4.657845,-4.872822,-2.023695,5.154881,-9.193689,-3.191131,6.596998,4.312287,0.457695,-5.062818,3.957988,3.626135,-3.453578,9.038830,-6.845780,-2.208928,-8.171935,-8.354694,4.427206,-6.930633,4.766021,8.271729,-4.067006,3.381370,4.177337,8.409556,-8.520217,-4.297157,7.049776,-1.884800,6.324152,-7.672028,9.972893,3.989031,-1.339718,-1.244707,-0.395456,8.831750,-6.080757,-7.216880,-9.284937,-7.813475,7.515222,4.494764,-2.846783,-9.142580,-1.861373,-2.645017,-8.513350,8.656088,0.619622,-2.997815,4.890877,-2.268396,5.368848,4.658053,5.710683,-9.980479,-1.677497,3.846262,-9.575429,2.021736,-2.926724,-9.049745,5.659887,-8.793171,-7.945174,-5.894453,-7.089039,3.324608,3.459491,8.192307,8.461865,1.542004,4.750860,-7.355300,7.609325,3.568907,2.868265,-2.891192,4.249515,7.183109,8.312732,7.366514,0.039904,4.705598,8.437893,5.616768,0.191679,1.897344,1.921505,-0.146211,4.897042,5.712865,7.988224,1.248107,-4.280088,-1.101621,-7.465327,3.777236,2.072592,-6.774249,9.425384,2.464773,0.026146,3.236006,-7.999311,5.985149,6.734182,0.159582,-2.341351,6.909703,8.660517,-5.741083,8.315978,2.508909,5.244372,-9.482461,7.532592,0.491626,-0.566309,-9.112646,-0.429833,-1.306544,-1.025439,-2.657484,-4.434075,6.378097,-1.319331,2.402040,1.857439,-6.987390,-9.360417,3.387406,-0.927859,-0.315059,0.359543,2.597344,-8.407447,-2.294039,0.987159,2.929093,-3.162297,-5.613476,5.277221,9.501390,-7.842429,3.842719,-1.153070,7.088518,8.500422,3.741277,-6.214920,-5.056871,-1.656572,7.600190,1.024706,0.179786,3.043227,-0.802933,1.669393,8.849952,3.578587,-5.076035,2.265679,-6.139967,-8.399732,0.343942,0.396544,1.723099,-4.627095,0.149907,-7.628176,-7.886265,-5.700732,-2.637514,-3.083355,-5.239193,-0.099107,1.195081,-3.964680,-5.519952,0.883406,8.866455,7.714357,-1.788559,3.938071,2.258921,-7.365638,7.853109,0.527473,-4.754273,2.928142,2.674103,9.902170,9.142250,0.673012,-2.469248,7.376795,6.645583,7.316292,1.120028,2.742244,-9.134235,-3.139456,4.674221,1.332025,5.286258,-1.326666,-4.554607,8.606267,9.644194,5.886914,4.082853,0.947345,6.314189,-0.036865,5.997599,9.748420,3.237961,4.203595,5.051658,-5.240778,4.989347,-3.959099,-5.715987,4.417805,-8.154705,-6.491149,5.715302,-1.578360,-5.134400,6.420157,-7.316096,6.664204,-6.500799,-3.092359,1.641887,-3.963977,7.154736,-6.243810,-6.806295,1.366995,-5.441421,-9.170341,7.398398,-9.877733,4.883442,4.582133,-7.433741,8.702379,1.731956,5.743674,-7.731433,4.610382,-8.126918,-7.284186,2.898936,8.447808,0.356345,-4.903153,-3.327488,-5.021925,-6.359357,3.401087,-9.665900,-7.873754,5.482306,-7.515421,5.382041,1.070087,2.722075,0.774602,-3.178611,-9.461094,-8.460220,-4.925736,8.101542,2.717134,3.649861,-7.244468,1.204354,4.754265,-0.983670,6.823023,-9.554105,1.945610,-3.337598,-4.561512,8.840559,-1.751659,8.511209,-8.470238,3.639541,7.231016,9.357235,-4.354088,-7.479223,8.566708,0.686230,-2.339484,0.434187,2.567105,-0.307098,-3.929169,-5.061245,-7.825455,-4.101600,-7.479171,-2.177105,-8.891113,0.411003,-8.452383,-1.281490,5.830411,-2.602229,1.527002,9.552568,0.291676,0.627655,-0.487271,-6.812455,7.309967,0.578785,-6.397835,8.405029,4.556255,7.925178,-0.409932,4.635165,1.517145,-5.681650,-6.802681,0.455131,4.052207,4.404098,-3.226479,-1.932563,-5.357278,2.374689,2.370304,9.851387,-8.068186,2.431488,9.682947,-5.207740,-4.533989,4.535308,-1.499203,6.320878,1.011294,0.911213,-2.869763,-4.964647,-1.201510,-7.610623,-3.260904,-0.803212,-4.811931,-6.761583,4.038794,9.553293,8.370722,-7.821481,4.490068,4.540579,-3.273929,0.976507,3.192927,-7.214285,0.002969,7.615600,-7.857974,-8.892925,5.716873,-1.326528,0.062879,2.043743,8.243114,4.483213,7.892237,3.160698,6.756649,-0.098060,-2.979191,-8.592676,6.373893,-9.930747,-2.005730,3.341745,6.150562,-7.458012,6.829492,7.108139,5.046833,6.777135,8.606039,-4.283991,1.418375,3.930292,7.268201,-5.843546,-0.119364,5.570952,0.484522,-0.072718,-5.266663,-5.035660,-7.597914,-3.386549,-8.540642,-2.010898,0.475409,-1.437278,-6.003845,-9.825832,-2.939113,-0.803274,9.374195,0.653691,-1.614493,4.342743,-2.447371,-0.412801,7.546276,-2.660669,4.559505,-8.711753,7.679834,7.501894,-6.890621,-4.114568,-4.367150,5.409773,-8.992737,8.823898,5.663037,2.700170,-2.923373,-9.944510,9.859543,0.588616,-4.997433,3.421380,-2.294038,8.143848,-7.258580,1.440155,-6.349961,6.185211,8.341079,-4.837651,0.821723,-0.693703,9.165835,-8.174599,1.940595,9.459459,0.546958,-1.299786,-9.862422,-8.006592,2.292109,5.426235,6.114223,-0.689757,4.747130,7.478457,-6.496143,-2.364398,-7.754880,-2.212400,-8.902769,5.791441,-5.993879,-0.870909,4.990298,-3.493600,-1.565066,6.523728,-0.943306,4.841912,-3.831097,-8.295507,-4.249340,-9.775114,8.863707,8.947245,1.099283,8.213466,-4.839898,-7.856670,0.068436,-9.841462,-3.894652,9.980270,5.179106,2.407963,2.382960,-2.644919,-5.068206,-9.045301,-3.059823,-2.005781,1.418965,2.196715,5.059270,4.744593,-8.642602,-2.753151,4.644307,7.770770,-0.830725,-0.480404,2.145980,-9.826647,-2.901646,2.170507,-3.214064,-3.193053,-2.493225,2.801274,0.789557,-9.596069,-5.039185,-8.759390,-2.579274,-4.182065,-8.763458,-1.619548,4.292556,-8.653550,9.731842,-7.635153,2.801308,6.210158,6.500675,9.293650,-8.572832,-3.056181,-0.154938,-3.217928,8.035039,-1.910847,-1.179316,7.851749,7.957439,3.894940,9.348137,-4.019166,-9.203336,-9.094607,-7.612093,-8.633467,5.314426,5.206529,0.137507,-3.899558,-9.467139,9.429196,5.853948,-4.925697,-7.179706,-6.091118,-8.843394,-0.070612,-7.104181,-3.643725,-4.685442,1.728411,8.914275,2.411078,4.001573,5.749298,-9.671857,-8.818205,6.818604,-6.982450,-8.186012,-4.629281,3.304901,4.775545,6.624324,-6.342475,-1.809674,-3.211460,-1.648038,-5.428621,0.887195,0.785469,-5.063977,-7.351266,4.630390,5.384854,8.423925,-6.194660,-1.706604,-8.657153,5.290937,9.720966,6.618365,9.691072,-0.662941,4.892273,-6.093461,9.745452,-6.732400,-6.653627,4.428756,8.321675,7.479669,1.672611,7.540609,-9.259437,6.346140,-6.099518,0.924485,-4.160979,2.190165,9.941438,7.030037,8.855058,-5.650179,0.374905,6.001600,-2.502115,-0.527272,6.875389,-1.017720,-6.011905,8.170903,-2.414204,-1.550737,-7.853734,-8.453348,3.374301,7.494682,5.316254,4.434218,5.932358,0.189868,2.143203,9.079580,1.578565,-2.528131,3.874456,-6.504816,-8.093489,1.709655,-8.477391,8.654750,0.400014,-7.994687,-5.744114,1.664649,5.593859,-7.893937,-5.170123,2.666824,4.230471,6.730849,9.720491,-5.888545,-3.859061,4.141164,8.891956,6.820424,9.143666,6.310613,5.569248,7.743376,2.342135,9.110222,2.847971,1.257231,3.270725,-9.395788,-3.074749,-8.914327,-4.924054,3.652786,-3.227284,-4.972612,3.275657,-7.854046,-2.899124,5.007651,2.101826,6.746897,4.650226,0.836364,0.970740,8.867159,-0.881569,-6.338330,6.429057,-7.092192,-0.493438,0.720661,-5.119069,-3.244866,5.219848,-3.506177,9.171633,-4.483137,-9.169434,0.731937,7.548256,5.804715,-1.934075,-9.952725,5.418864,-8.437739,8.854915,8.507976,3.817661,-7.723799,0.879872,3.827089,-8.952315,1.616869,4.527917,-8.103095,-4.814618,-2.839120,0.466289,-8.148981,1.442250,8.074890,8.350399,-7.998678,-8.006198,9.354182,7.005540,-3.881312,-0.270126,-2.268224,-3.259206,-9.979760,-0.061103,-0.098092,6.200158,-1.555625,4.558260,1.829116,9.757451,5.309066,-2.953244,1.768058,2.254655,6.449790,-8.903223,8.714192,-6.226603,9.257001,-3.636443,1.555413,-7.141966,-8.275549,8.611384,-5.309188,3.606564,-0.937164,1.286402,8.156743,-1.041533,-4.413647,-1.286366,2.530326,-5.153491,3.467490,-9.550123,-2.263394,-9.119647,-3.544374,6.367263,-6.210937,-5.309086,-1.922195,8.280103,-5.548462,0.939272,-2.113931,-2.255306,-4.508806,-2.242970,5.379795,-8.142361,0.279129,-5.025275,-9.713685,2.599339,-7.173208,-4.925138,6.902898,-9.082470,2.214623,-2.264175,9.059758,4.050794,2.892146,0.920608,7.493032,1.277787,9.594055,-4.399062,5.317993,-1.990958,-7.783793,-1.286859,-4.312176,3.974530,-2.757461,2.317611,4.334994,-4.709546,-5.043491,0.048035,4.046069,4.200494,2.504942,4.808270,4.150337,-1.090447,-5.255411,1.231952,-1.173394,-7.949919,-9.455625,-7.825685,-7.371580,0.832109,3.466672,-3.299093,0.467904,5.204911,-5.970042,5.532033,-8.367256,5.769329,-5.378479,-6.714684,6.804756,-2.876494,-3.643655,1.885696,6.831372,-8.192047,-6.546292,5.775770,-2.746371,-9.629051,9.065139,-5.729777,9.588144,-2.056145,-8.080402,-7.301648,8.809543,5.409608,-7.926770,3.782038,2.805660,-8.773082,-9.537954,2.823961,-9.573755,0.130725,3.822980,2.521712,7.479124,9.490588,-4.706736,-9.881708,-1.251625,-6.641210,-6.009844,-7.610284,1.748573,0.629208,-8.639986,-9.690934,-6.295327,9.480579,7.979861,0.145864,-9.232366,-1.798718,-7.396444,9.149953,-4.412323,1.443516,0.679091,3.253910,-4.000810,-2.174758,9.842742,2.899676,1.688593,-1.927636,-2.644030,7.984833,-7.245909,6.601396,-6.199318,1.042090,-7.358935,-3.290327,-7.019561,-7.442462,-4.610306,8.649753,5.898214,-4.440725,2.275616,4.801850,-3.773944,1.304390,-3.599906,3.877822,3.395582,-5.798085,-7.764156,5.784810,-0.521755,8.569010,-1.620041,-3.544372,-6.240643,-4.485809,7.973481,9.788404,7.201958,-6.119171,5.228175,-1.558218,-6.904884,9.695076,0.857880,8.189697,-4.677745,6.180790,-5.725467,3.331296,-5.181050,-3.364043,8.111008,9.595546,-7.823214,4.518111,9.091673,-6.464181,-4.805298,-0.571411,-3.898249,2.591513,6.940403,-4.931178,-4.942885,-2.054372,4.335362,3.914259,-7.156781,9.126849,-7.042540,-4.119331,1.108524,-3.828398,-7.674607,5.142440,-2.328936,-4.776812,7.447613,7.010152,-2.565325,-5.215204,4.687138,-6.287576,-0.414030,-7.561025,-0.742688,6.656646,-7.555716,2.228672,-6.389453,6.133335,4.226257,-6.431685,-5.869548,2.224852,6.513055,8.253864,6.938817,-7.095123,5.716257,-1.975825,-1.966913,9.698001,6.873580,4.434067,-3.535795,5.775065,-2.273277,-9.773688,6.999546,3.044599,-9.172148,0.663622,2.981846,0.777078,8.419103,-4.978612,5.420254,-3.650703,9.267206,5.177434,-2.573586,4.073632,-3.472774,-1.571433,4.599286,0.226466,-2.640084,0.146923,-0.217300,-7.803199,3.695225,0.927870,0.281793,9.770018,-6.548606,-7.582131,5.307899,4.669488,8.678233,-9.254476,-0.839426,-5.967747,-1.009914,-0.107252,6.025881,-9.996050,7.750244,2.610564,3.371907,6.950108,1.985093,7.086185,-3.837149,8.587736,-1.392230,-1.331631,1.256573,4.435760,2.738929,-3.296157,-4.099997,0.320849,5.263888,-1.511171,2.492075,-2.230036,1.503645,-4.244668,-2.208788,-2.641678,2.346675,1.464174,8.059155,-5.472843,-4.449146,2.863241,-0.311262,3.924852,-0.161023,-9.264279,2.123106,-5.918597,-9.984710,-7.544501,-0.228368,6.967377,-2.419085,-1.681208,6.257807,-5.370560,-5.287396,6.749564,-1.849909,-5.256384,-0.478969,-1.323820,2.847948,8.314450,9.556046,-3.266189,-5.049909,4.400864,3.851391,-6.891532,0.828922,-6.151420,4.399017,-9.725774,-9.357389,-3.917254,1.133458,4.464923,5.977089,7.586891,-8.653157,1.939232,6.401081,1.486251,-0.627953,-3.906887,-2.281685,4.496479,-6.622365,4.134855,-8.237333,2.704127,7.786153,-9.891206,9.036745,2.364978,-4.843493,-5.251809,-9.632598,-9.127393,-3.657139,-7.121811,1.416086,-8.943652,6.921864,0.986621,6.454619,3.943937,2.545002,9.752529,0.796725,-1.517112,3.154285,-0.537255,8.624850,4.993822,0.268958,-3.052411,0.058485,-0.867350,9.677988,6.216373,-5.200753,8.083834,-9.570894,2.346153,2.380407,3.994340,-2.736699,-9.429379,-3.161363,0.444893,4.169600,0.111109,-9.062911,9.198403,2.597167,-5.080221,-4.507082,6.818163,8.702937,-0.110387,-0.528414,7.183870,2.209609,-1.994134,2.231646,1.599933,-6.461520,-3.451089,-4.719822,-6.334077,-4.177462,-5.000125,-0.875875,2.979606,-0.354888,-7.040192,-0.699201,2.459016,-6.995888,6.403064,-7.336411,-7.690604,8.292871,5.265014,8.894321,6.168874,8.566301,-8.387018,3.759566,6.561722,2.310816,9.412360,7.902070,-1.241871,-4.176482,-9.709688,-6.192197,3.733733,3.742359,-2.959738,-6.749578,-5.100023,7.598600,4.416999,-9.253649,-6.609014,0.866590,5.391106,-5.477121,-0.346635,-9.704933,7.322232,7.096919,-3.204187,-8.651035,8.141620,2.800357,-7.417473,-7.027683,5.479925,-5.721805,3.476671,8.669049,-4.233068,-0.488370,3.756258,1.717250,6.905467,6.088448,8.041520,-0.362792,2.734513,-3.144199,-9.559227,9.391794,-8.643925,4.282402,3.072003,-3.982366,3.808743,-2.300866,8.720958,6.417609,1.575258,6.456436,-2.031735,5.664475,4.991788,4.248333,9.892511,1.177351,-7.411738,2.130694,-8.675657,-3.435752,-4.353883,-7.538793,-1.619329,-4.022531,-2.471040,0.769766,-1.924285,-4.497720,-8.195961,2.128174,0.892554,1.440050,-3.798250,7.199499,3.755139,-5.846076,1.421963,9.247765,-9.253034,1.513269,2.026799,-9.698623,9.089195,8.512164,-4.673099,5.815220,-1.808074,-9.109717,2.387374,6.708386,0.374717,-4.065781,-8.313012,-0.462632,-2.865491,1.132748,-3.167186,9.608584,6.414661,-1.360856,0.775987,5.326681,-4.971830,-0.237224,2.388207,-4.765384,3.333553,8.851647,8.739208,2.523887,6.006225,8.096292,-0.874050,-5.602134,-3.570283,4.615827,-4.243443,0.664274,-8.105554,9.912775,4.494431,-8.910420,-7.950665,-1.713728,-9.445211,1.797105,-8.593751,5.180826,5.650745,-9.325186,-5.130189,-1.827499,-5.046260,-1.839043,1.144543,8.521371,2.335695,-5.948967,5.709168,1.235640,-2.712223,-5.831537,-9.252266,9.518147,6.858391,5.531738,5.056991,-7.252095,0.783740,5.810093,-8.201733,8.230044,-3.425936,-6.667368,-8.475484,7.625203,-0.970149,6.873091,-0.770230,9.785893,1.526100,4.979420,-8.253216,-6.517309,-3.652681,-3.668292,-6.930707,2.559234,7.545539,3.441575,5.404399,-7.073411,-2.505372,-9.088746,-8.676478,-8.309606,-9.427342,3.208563,4.470815,-0.303711,8.649738,6.204338,-6.526021,-6.111605,-8.545566,1.086519,7.362601,3.070108,-1.135227,-2.144149,2.975325,-6.358853,-7.025983,-4.279142,0.306493,-9.367103,-2.820050,2.957298,-5.384912,-0.801276,1.652937,-1.548870,-2.021224,-9.418550,-3.921533,4.049150,0.920910,9.380243,8.447997,0.140315,9.791514,9.124881,7.430071,-8.669726,5.436261,-3.048606,2.915773,8.306352,4.540128,-0.133655,-4.162296,6.173066,8.273142,0.200023,6.128264,9.844742,-1.833320,-7.963205,2.548157,7.929129,1.032778,8.039524,1.587188,-3.510481,-3.154896,-0.995390,0.672387,-7.750810,-7.691423,2.982495,0.169651,-3.480343,-4.751627,2.056908,-6.021234,-5.075073,0.953710,-6.025064,-9.092294,4.813636,6.808033,3.493696,3.896477,5.381501,4.904025,7.535741,2.321438,9.186604,-7.198637,-4.237444,7.327505,0.047961,-9.092202,4.252886,-7.432914,-8.964923,-5.693397,-6.217877,0.666933,-7.624485,1.973848,8.331627,1.650930,-0.632616,-6.564231,-9.362830,3.817753,-2.661288,6.956295,-1.204609,-9.523133,0.040710,-8.681035,-6.995723,5.827316,-8.028353,9.455884,-5.247403,-7.082831,-2.205390,0.254253,9.544350,-4.898872,-8.027248,9.835583,-3.075305,0.910270,5.879250,9.977285,-5.601970,-0.554116,7.091647,-9.577342,-5.693542,-4.281588,9.217775,-6.153199,-0.555669,-2.634244,-3.321412,6.329346,5.401807,7.347432,-8.806617,9.260726,6.504090,-7.793714,8.434860,-8.041735,8.939040,-4.132852,-5.174821,3.652561,-8.792684,-3.309000,-7.600831,8.622671,-3.399141,-9.640606,0.585724,2.283808,5.508672,-3.969652,1.645611,-3.176001,2.251143,9.210212,0.692970,3.779613,3.470171,5.055387,3.396043,3.573508,5.353087,7.701349,3.899782,5.715595,-4.051711,5.674292,9.056274,-2.704347,5.355252,-0.226318,2.193279,-4.218969,4.923226,-1.173703,-3.433845,5.268288,7.155741,-6.415660,7.031755,0.961632,5.469424,8.822646,-7.241644,-9.857195,-1.963050,9.685491,-1.487673,-7.092254,5.342365,-2.038792,-2.524119,1.295459,-9.668558,2.805848,0.995559,2.783183,4.659398,7.106461,3.262007,3.868376,6.969316,0.253281,-6.067595,4.931448,-7.800971,6.691071,5.094232,-2.293143,2.084966,-5.892794,-0.898850,1.987979,-6.246181,4.054534,-7.723436,8.936194,4.527007,7.945368,-7.837396,7.227728,3.039757,-0.649762,0.458956,-0.370431,-8.006523,-1.967680,5.886166,-8.554310,-0.244029,8.512864,6.789891,-0.152188,8.516631,-1.673805,6.296681,-2.682770,5.255154,1.153232,1.524623,8.349996,-9.659791,-5.988116,0.273535,-8.310171,-3.847790,0.158541,-7.277503,8.162036,9.962816,-6.920181,7.356253,5.258675,0.070722,-9.062342,1.369221,-8.253418,2.007629,1.645519,6.840853,-7.979293,7.739262,9.764099,-2.189887,3.349536,2.639899,-2.088575,-7.542521,8.115284,-6.230072,-6.037733,8.589129,-2.882644,9.746496,0.744579,4.413222,-5.490668,5.418134,-5.632658,-2.259115,-6.757712,8.307640,2.950507,-7.271748,1.537011,-0.305877,-3.423184,-1.983673,-3.095351,-8.437350,2.435050,6.891618,-5.429692,5.431821,-5.498990,-6.435081,2.440098,6.882899,4.132598,6.922234,5.166632,-8.633824,7.433675,-4.552204,-5.810342,-9.668141,-5.936809,-3.931061,-9.525835,6.704600,9.001037,4.840429,-9.444869,8.321023,7.419615,-2.645091,-4.018157,-8.798740,-7.252007,9.675014,-3.841560,-1.707242,-5.536034,6.753766,-8.930443,9.240050,7.485527,5.572113,-5.039680,7.956802,9.851288,-3.537136,6.043963,-4.789600,7.806524,-2.094130,2.183444,-0.320762,1.801634,-5.480255,-3.148361,-3.721370,2.347349,6.648235,-7.412606,5.953860,2.285756,-7.799833,-8.671940,-4.411091,-6.927973,1.313889,2.360052,2.046483,-4.401560,-5.506815,-3.504880,-0.671805,-3.297313,2.874341,-8.012845,9.046160,-7.060455,-9.754595,-8.286615,-5.423394,-1.822445,-2.100040,8.387022,-2.554132,4.027799,-5.306116,3.501737,0.823070,2.350661,5.143304,2.277255,5.832464,-5.113833,5.472472,-2.933722,3.075614,5.330707,-7.703905,-2.456986,-2.134356,9.441553,1.312426,6.267499,3.934811,6.765842,1.184552,4.780049,-9.713975,-6.128381,-7.217127,3.660108,7.476691,0.718452,1.522015,4.076757,2.633580,-9.653255,7.121235,-8.679997,-3.647761,1.428613,-3.098743,-6.526651,-1.722670,-4.817390,1.864251,4.999092,1.581654,-8.553727,-2.931096,-4.403858,5.119487,-9.723375,7.651476,7.827477,-6.117010,2.667138,4.298046,9.672853,-3.992582,-9.993485,0.127467,2.962937,-7.462523,4.684382,6.219772,-2.796143,-5.267576,7.703694,3.467677,-4.235008,-9.758853,2.511449,8.447382,7.236134,-6.852440,-7.262194,3.807594,-7.224327,0.667019,-7.178366,-2.341192,0.385782,2.379378,-7.494743,0.724084,-2.259230,-7.792408,4.841143,-7.549837,1.580027,-3.159447,-2.767988,8.352177,1.063871,-8.068922,1.539095,4.963306,-6.157259,-9.041100,9.693592,7.784362,2.755006,3.986323,7.541113,3.853955,4.046062,-1.559939,-5.068802,-6.979123,1.950446,6.156111,7.877388,1.969481,-7.164227,-2.398149,-4.422691,7.219249,7.081064,-3.227251,6.032292,-4.334029,-1.656265,-9.142573,-2.631665,-4.882112,-5.779338,4.836716,-6.494932,4.056665,-3.294513,8.703449,9.722315,-5.080944,2.472451,7.335750,-4.485609,8.273901,3.709728,5.845462,9.834166,7.396490,-0.502436,6.776770,5.626638,9.512361,5.637078,-0.956927,4.397881,7.445579,-7.144788,1.031675,-9.641593,9.782398,2.446122,-9.915749,-3.703702,-4.335120,-0.247123,-3.085618,-9.408959,1.809152,-3.975845,-9.530597,-8.235805,-6.846825,-8.652070,6.196958,0.498968,-8.759710,-6.217170,7.267418,-0.087707,6.551858,7.994402,0.425286,8.893644,0.454217,-3.874054,0.856099,-3.070882,8.292810,-1.428296,3.873758,0.344702,-5.973836,-3.776657,1.565620,8.661318,3.882629,-5.968213,-2.736842,1.280938,9.289683,1.901042,-3.113611,-1.475181,-1.711708,6.261488,-8.632093,-0.820424,-0.317535,-7.871514,1.608160,-0.879029,3.363450,2.857625,-9.400501,8.194388,0.108840,-3.748674,-5.429177,6.549619,5.043425,3.293827,-3.258304,-3.748982,-6.287004,-6.874623,-7.006398,4.429806,8.151804,5.419509,5.426454,2.512477,4.464143,3.730798,-7.026445,6.533998,6.152059,-3.338329,-9.756509,-0.520966,0.692585,-5.801760,3.522056,7.621361,5.541135,-5.845717,-3.991092,8.256969,1.249580,0.315166,2.940239,-4.291895,2.476870,-1.766954,5.435887,3.494733,0.234613,2.288547,8.966850,6.551676,4.732505,1.280171,8.875499,-4.359549,0.597098,5.199641,-9.548510,4.604098,-9.274287,1.151492,-0.285163,-1.227822,-1.609313,-4.631444,2.671110,-2.980303,2.738927,-7.052460,-8.943081,-8.174552,-3.002795,5.994275,2.711296,1.769044,-2.939831,3.386970,2.322941,0.391815,2.530264,5.625683,5.361704,-9.372929,2.887854,-2.965542,6.321309,-1.640512,-5.759774,-0.444593,-4.183938,5.194070,-3.559714,-9.438654,-0.412277,5.384016,3.446646,-9.660051,4.545184,-8.920653,3.338281,-8.235114,5.026939,8.468530,-2.382997,5.750594,7.463099,-4.787056,0.587938,3.376608,-0.713699,-7.523689,2.303708,-3.692266,0.970856,2.569615,2.584001,7.911187,-2.426793,-2.568461,-7.810305,-1.048638,-4.151086,0.190827,6.789217,-1.324781,3.412473,9.311122,3.632289,1.327900,-3.585329,-1.336966,1.206344,-8.013153,-6.803231,-9.891780,-3.268576,-3.456755,8.666684,2.302764,-1.036249,-2.898979,-7.358758,-0.619322,-1.223759,-2.222317,-3.018142,-5.551251,-9.314678,-5.990246,-2.057968,5.113857,5.015713,3.377970,6.923956,5.926902,-2.864479,7.963148,2.751585,9.374013,-7.621150,5.883176,-6.008523,-0.590244,-2.970230,3.688539,2.819109,-0.298663,-2.399901,-0.019177,-5.108177,8.201096,6.970994,3.191693,-9.492161,-9.875551,-0.548227,9.937340,-8.786591,2.003969,-2.058855,4.033473,0.686583,-6.693068,5.721054,7.574151,-5.991040,0.352274,6.199820,2.302556,9.212695,-4.267104,6.860669,-8.050813,1.704993,-1.974677,-7.928825,-1.922827,3.061739,0.773050,6.700353,-6.013732,9.325929,6.761216,-9.791216,-7.429257,3.619136,6.072805,-3.797787,-4.319536,2.958561,-9.339342,-9.877219,2.530234,0.056636,-3.994260,5.350812,8.077529,-0.996177,-0.335045,5.813351,-8.567934,1.809580,8.314524,5.268633,-7.137729,-5.453844,-1.739828,3.211632,5.800124,-0.461530,6.636711,-8.740549,-4.892626,1.805839,-6.871750,3.023127,2.988780,-4.395209,2.811433,-8.562786,6.671362,-6.522918,6.784643,7.917650,-8.679953,7.049155,-7.396811,-7.528429,-3.180862,3.866286,-8.968928,-3.595290,9.198162,-6.720411,-3.920299,-3.129379,-0.370281,-0.185743,-7.650815,-9.596918,2.215795,-9.862898,1.864737,2.594339,9.473943,-9.636570,1.420813,6.914966,-8.600400,9.449216,0.494426,-3.268460,-9.179319,0.681821,-9.284742,-7.525603,5.473547,5.162347,9.515744,0.922843,3.102346,6.429758,-1.178127,-6.856301,-4.103646,2.659383,5.889817,7.321804,-2.235698,2.173248,-5.291544,1.733304,-8.686321,1.538428,7.722688,-0.169006,-3.315015,3.927477,6.169401,2.871584,-7.881563,4.419598,-9.381510,7.108703,5.762054,-9.735204,-4.637309,-7.842006,-1.743308,5.116667,-2.843884,5.705987,4.510402,4.201957,-2.608697,-5.691823,3.130569,-3.517739,8.074272,5.734049,-1.865400,-7.158083,2.157840,-3.285929,-3.007116,4.656557,2.810623,-4.452198,4.020137,6.215767,-6.688974,-4.032983,0.700551,-7.303826,3.023747,-3.396094,2.108971,-9.175256,2.383004,-6.886482,-3.306644,-2.832077,-8.502041,-2.385828,-6.817423,1.061012,-4.865257,-5.735873,5.003149,-6.486531,-0.744664,-8.184715,1.209259,-2.752525,1.339785,6.638162,-8.972895,-8.717302,-5.059562,9.640233,-2.457042,6.453221,-9.731041,6.768653,-9.886963,-0.815357,-5.812653,-5.071807,-2.630621,-8.472588,-8.671936,9.865103,9.518168,2.605389,1.729614,-4.339354,-9.946912,-1.575682,9.762595,-3.205034,8.483222,5.181417,5.255381,9.740851,-3.820624,-2.494950,9.406296,-7.918941,9.803600,-8.425337,-6.515231,-2.951515,9.339663,7.737956,-2.459758,-8.785329,1.905343,4.035994,-7.616789,-6.932445,-8.658843,9.742889,-3.503426,-4.199886,9.163147,-0.601646,2.196701,-9.640182,0.738320,-5.289882,4.039178,7.163737,-6.871479,-0.908743,-6.331070,0.873375,3.476240,-9.875785,-8.277843,5.897266,-3.202289,4.169166,-1.055960,-9.960766,-6.186202,-2.398248,3.757522,-6.793306,-3.617306,-5.476620,1.940608,-1.323863,-6.866405,-4.048247], dtype = "float64")#candidate|16061|(2912,)|const|float64
call_16060 = relay.TupleGetItem(func_10105_call(relay.reshape(const_16061.astype('float64'), [13, 16, 14]), relay.reshape(const_16061.astype('float64'), [13, 16, 14]), ), 0)
call_16062 = relay.TupleGetItem(func_10109_call(relay.reshape(const_16061.astype('float64'), [13, 16, 14]), relay.reshape(const_16061.astype('float64'), [13, 16, 14]), ), 0)
func_5468_call = mod.get_global_var('func_5468')
func_5471_call = mutated_mod.get_global_var('func_5471')
var_16064 = relay.var("var_16064", dtype = "float64", shape = (80,))#candidate|16064|(80,)|var|float64
const_16065 = relay.const([-7,-8,-2,-9,-4,6,5,-4,-8,-5,1,6,1,-10,-8,-2,7,9,-4,4,7,-10,2,3,10,-7,-3,3,-10,1,-4,-5,7,-2,10,9,-10,4,-2,-1,4,5,4,1,3,-4,-7,7,10,-2,-7,-2,9,6,2,4,-7,3,-9,5,-8,-8,-5,8,-6,10,1,-8,-7,-2,4,-4,6,-10,4,8,4,7,-5,-9,-5,-2,-8,-9,-7,-3,-6,9,6,9,-7,-4,-5,4,-5,-10,-1,-9,5,5,8,4,-5,-7,4,-3,-5,6,7,1,-3,4,-5,5,10,5,-6,-3,-2,5,8,-9,-4,-6,-4,-5,-2,-1,4,9,3,-4,-3,-3,-9,10,-8,-2,-3,5,7,-4,-1,-8,-2,8,2,-6,1,1,10,7,2,10,10,-3,-7,8,4,2,-2,1,4,-9,9,-3,1,4,-9,-9,2,-8,10,5,-9,-8,-7,6,-6,-6,-5,3,9,1,4,9,-3,2,-2,-7,-6,-3,-4,6,-4,-7,3,8,9,-2,-3,-6,-9,-10,-7,-3,2,8,6,7,8,10,-6,-3,-2,-6,7,1,-4,6,-10,6,6,-1,10,2,-4,7,-5,-4,5,-1,-4,8,-7,-9,5,2,-9,-4,3,-7,2,-6,4,3,-10,4,1,3,-8,7,-8,-7,-4,-8,-8,-3,-8,-7,-10,4,7,7,-9,5,1,-3,5,-7,-10,5,9,8,8,10,6,-10,-1,10,-5,9,9,8,9,-2,-10,7,-6,7,-8,1,-2,-6,10,-6,1,3,-7,-7,-6,-7,7,-8,-9,-6,-3,-1,-10,1,-5,4,-2,9,8,10,-4,-2,1,1,-4,-6,-3,-3,6,-2,-1,-6,-1,-4,10,5,-1,2,-5,-1,-1,8,-8,7,-5,4,5,-10,-6,7,10,-9,-9,2,-7,4,4,1,5,5,-7,7,-2,10,3,5,9,6,-6,-1,3,-10,-1,8,-9,7,3,-9,3,4,-7,1,2,4,-8,-10,2,10,1,9,-1,7,10,-9,-5,1,2,8,1,-4,6,-10,6,-2,-7,6,-5,2,-10,8,-5,-1,-5,3,-10,-5,-10,5,-4,-2,7,-9,-4,-10,3,4,-9,7,4,9,4,10,-8,2,3,-1,4,5,-10,-4,2,-2,-3,-4,6,10,-7,6,5,-5,3,-1,5,-7,-8,9,1,1,-10,-10,8,10,10,3,5,-6,-4,-5,10,8,-5,7,10,-7,-3,-9,-6,-8,-7,4,9,-8,6,5,-7,3,10,5,6,-10,-10,-1,10,-5,-10,-6,-8,3,-10,-9,9,-7,1,-9,-6,7,-8,4,-8,4,9,-7,6,2,-8,5,4,6,-5,-4,4,7,-8,1,-10,-3,6,-6,10,10,-9,-7,6,8,-8,10,-2,7,8,7,2,-6,2,1,-10,-1,-4,9,2,1,10,4,-10,1,9,-5,9,-7,3,-2,7,-1,-10,2,10,1,-7,-9,8,-5,1,5,-1,-9,-10,-7,-6,9,1,-7,-5,10,-7,-8,-10,-1,-3,10,-9,-10,2,6,-10,-6,-6,-1,-5,-4,-1,-7,-7,3,-5,8,4,2,9,-5,-7,-9,4,-6,2,-1,-6,5,7,7,-3,-5,-5,2,-9,1,8,8,10,2,8,5,2,-7,-10,-10,-9,7,-5,8,-9,-1,6,10,-5,-10,-6,5,6,8,8,6,-4,-3,-3,-5,9,1,5,-3,-4,1,7,9,-2,7,6,9,-8,8,-3,-6,-9,8,-8,4,2,-3,5,-2,10,5,5,-5,8,4,10,-4,7,-5,-2,7,6,5,-6,6,-8,-4,-7,-4,4,-8,8,-3,5,9,7,-3,6,4,-7,-9,-3,8,10,7,-9,-8,7,3,-1,9,-8,3,-2,-7,-9,-4,7,-4,-3,3,-8,-3,6,6,10,-5,10,6,5,1,-8,-6,-10,-4,-1,-8,-1,3,9,-5,7,-9,6,-8,-9,-4,-7,-3,-9,9,7,-1,8,-6,-5,8,-10,8,-4,-8,-9,-1,-1,3,-5,-3,10,1,-8,-7,-9,-5,-3,7,-1,-2,7,7,10,-9,-2,5,4,2,-6,-5,5,6,-2,9,7,-4,-5,-2,8,-9,-4,4,2,-2,-6,-5,-6,1,3,-3,-9,5,-7,10,10,8,4,2,8,8,2,5,4], dtype = "int16")#candidate|16065|(825,)|const|int16
call_16063 = relay.TupleGetItem(func_5468_call(relay.reshape(var_16064.astype('float64'), [80,]), relay.reshape(const_16065.astype('int16'), [825,]), ), 1)
call_16066 = relay.TupleGetItem(func_5471_call(relay.reshape(var_16064.astype('float64'), [80,]), relay.reshape(const_16065.astype('int16'), [825,]), ), 1)
output = relay.Tuple([call_16039,call_16043,const_16044,call_16052,const_16053,call_16060,const_16061,call_16063,var_16064,const_16065,])
output2 = relay.Tuple([call_16040,call_16045,const_16044,call_16054,const_16053,call_16062,const_16061,call_16066,var_16064,const_16065,])
func_16074 = relay.Function([var_16064,], output)
mod['func_16074'] = func_16074
mod = relay.transform.InferType()(mod)
var_16075 = relay.var("var_16075", dtype = "float64", shape = (80,))#candidate|16075|(80,)|var|float64
output = func_16074(var_16075)
func_16076 = relay.Function([var_16075], output)
mutated_mod['func_16076'] = func_16076
mutated_mod = relay.transform.InferType()(mutated_mod)
const_16135 = relay.const(False, dtype = "bool")#candidate|16135|()|const|bool
const_16136 = relay.const([[[False],[False],[True],[True],[True],[False],[True],[True],[True],[True],[False],[False]]], dtype = "bool")#candidate|16136|(1, 12, 1)|const|bool
bop_16137 = relay.logical_and(const_16135.astype('bool'), const_16136.astype('bool')) # shape=(1, 12, 1)
output = relay.Tuple([bop_16137,])
output2 = relay.Tuple([bop_16137,])
func_16140 = relay.Function([], output)
mod['func_16140'] = func_16140
mod = relay.transform.InferType()(mod)
output = func_16140()
func_16141 = relay.Function([], output)
mutated_mod['func_16141'] = func_16141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15392_call = mod.get_global_var('func_15392')
func_15393_call = mutated_mod.get_global_var('func_15393')
call_16204 = func_15392_call()
call_16205 = func_15392_call()
func_14701_call = mod.get_global_var('func_14701')
func_14704_call = mutated_mod.get_global_var('func_14704')
var_16211 = relay.var("var_16211", dtype = "float64", shape = (250, 2))#candidate|16211|(250, 2)|var|float64
call_16210 = func_14701_call(relay.reshape(var_16211.astype('float64'), [5, 10, 10]))
call_16212 = func_14701_call(relay.reshape(var_16211.astype('float64'), [5, 10, 10]))
func_6837_call = mod.get_global_var('func_6837')
func_6839_call = mutated_mod.get_global_var('func_6839')
call_16224 = func_6837_call()
call_16225 = func_6837_call()
output = relay.Tuple([call_16204,call_16210,var_16211,call_16224,])
output2 = relay.Tuple([call_16205,call_16212,var_16211,call_16225,])
func_16240 = relay.Function([var_16211,], output)
mod['func_16240'] = func_16240
mod = relay.transform.InferType()(mod)
mutated_mod['func_16240'] = func_16240
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16241 = relay.var("var_16241", dtype = "float64", shape = (250, 2))#candidate|16241|(250, 2)|var|float64
func_16240_call = mutated_mod.get_global_var('func_16240')
call_16242 = func_16240_call(var_16241)
output = call_16242
func_16243 = relay.Function([var_16241], output)
mutated_mod['func_16243'] = func_16243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13439_call = mod.get_global_var('func_13439')
func_13440_call = mutated_mod.get_global_var('func_13440')
call_16253 = relay.TupleGetItem(func_13439_call(), 0)
call_16254 = relay.TupleGetItem(func_13440_call(), 0)
func_10473_call = mod.get_global_var('func_10473')
func_10475_call = mutated_mod.get_global_var('func_10475')
call_16274 = relay.TupleGetItem(func_10473_call(), 1)
call_16275 = relay.TupleGetItem(func_10475_call(), 1)
output = relay.Tuple([call_16253,call_16274,])
output2 = relay.Tuple([call_16254,call_16275,])
func_16280 = relay.Function([], output)
mod['func_16280'] = func_16280
mod = relay.transform.InferType()(mod)
output = func_16280()
func_16281 = relay.Function([], output)
mutated_mod['func_16281'] = func_16281
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6837_call = mod.get_global_var('func_6837')
func_6839_call = mutated_mod.get_global_var('func_6839')
call_16284 = func_6837_call()
call_16285 = func_6837_call()
func_12807_call = mod.get_global_var('func_12807')
func_12810_call = mutated_mod.get_global_var('func_12810')
var_16298 = relay.var("var_16298", dtype = "float32", shape = (300,))#candidate|16298|(300,)|var|float32
call_16297 = relay.TupleGetItem(func_12807_call(relay.reshape(var_16298.astype('float32'), [3, 10, 10])), 2)
call_16299 = relay.TupleGetItem(func_12810_call(relay.reshape(var_16298.astype('float32'), [3, 10, 10])), 2)
output = relay.Tuple([call_16284,call_16297,var_16298,])
output2 = relay.Tuple([call_16285,call_16299,var_16298,])
func_16303 = relay.Function([var_16298,], output)
mod['func_16303'] = func_16303
mod = relay.transform.InferType()(mod)
var_16304 = relay.var("var_16304", dtype = "float32", shape = (300,))#candidate|16304|(300,)|var|float32
output = func_16303(var_16304)
func_16305 = relay.Function([var_16304], output)
mutated_mod['func_16305'] = func_16305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4628_call = mod.get_global_var('func_4628')
func_4629_call = mutated_mod.get_global_var('func_4629')
call_16375 = func_4628_call()
call_16376 = func_4628_call()
func_6162_call = mod.get_global_var('func_6162')
func_6163_call = mutated_mod.get_global_var('func_6163')
call_16377 = relay.TupleGetItem(func_6162_call(), 0)
call_16378 = relay.TupleGetItem(func_6163_call(), 0)
func_6162_call = mod.get_global_var('func_6162')
func_6163_call = mutated_mod.get_global_var('func_6163')
call_16388 = relay.TupleGetItem(func_6162_call(), 0)
call_16389 = relay.TupleGetItem(func_6163_call(), 0)
output = relay.Tuple([call_16375,call_16377,call_16388,])
output2 = relay.Tuple([call_16376,call_16378,call_16389,])
func_16399 = relay.Function([], output)
mod['func_16399'] = func_16399
mod = relay.transform.InferType()(mod)
mutated_mod['func_16399'] = func_16399
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16399_call = mutated_mod.get_global_var('func_16399')
call_16400 = func_16399_call()
output = call_16400
func_16401 = relay.Function([], output)
mutated_mod['func_16401'] = func_16401
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6400_call = mod.get_global_var('func_6400')
func_6402_call = mutated_mod.get_global_var('func_6402')
call_16404 = relay.TupleGetItem(func_6400_call(), 0)
call_16405 = relay.TupleGetItem(func_6402_call(), 0)
output = call_16404
output2 = call_16405
func_16411 = relay.Function([], output)
mod['func_16411'] = func_16411
mod = relay.transform.InferType()(mod)
output = func_16411()
func_16412 = relay.Function([], output)
mutated_mod['func_16412'] = func_16412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11670_call = mod.get_global_var('func_11670')
func_11672_call = mutated_mod.get_global_var('func_11672')
call_16482 = relay.TupleGetItem(func_11670_call(), 0)
call_16483 = relay.TupleGetItem(func_11672_call(), 0)
var_16497 = relay.var("var_16497", dtype = "float32", shape = (9, 10, 10))#candidate|16497|(9, 10, 10)|var|float32
bop_16498 = relay.left_shift(call_16482.astype('uint16'), var_16497.astype('uint16')) # shape=(9, 10, 10)
bop_16501 = relay.left_shift(call_16483.astype('uint16'), var_16497.astype('uint16')) # shape=(9, 10, 10)
output = bop_16498
output2 = bop_16501
func_16506 = relay.Function([var_16497,], output)
mod['func_16506'] = func_16506
mod = relay.transform.InferType()(mod)
var_16507 = relay.var("var_16507", dtype = "float32", shape = (9, 10, 10))#candidate|16507|(9, 10, 10)|var|float32
output = func_16506(var_16507)
func_16508 = relay.Function([var_16507], output)
mutated_mod['func_16508'] = func_16508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8050_call = mod.get_global_var('func_8050')
func_8052_call = mutated_mod.get_global_var('func_8052')
call_16571 = relay.TupleGetItem(func_8050_call(), 0)
call_16572 = relay.TupleGetItem(func_8052_call(), 0)
func_11558_call = mod.get_global_var('func_11558')
func_11559_call = mutated_mod.get_global_var('func_11559')
call_16583 = relay.TupleGetItem(func_11558_call(), 1)
call_16584 = relay.TupleGetItem(func_11559_call(), 1)
func_5267_call = mod.get_global_var('func_5267')
func_5268_call = mutated_mod.get_global_var('func_5268')
call_16601 = relay.TupleGetItem(func_5267_call(), 2)
call_16602 = relay.TupleGetItem(func_5268_call(), 2)
func_11821_call = mod.get_global_var('func_11821')
func_11824_call = mutated_mod.get_global_var('func_11824')
const_16604 = relay.const([[-7,-2,-7,-1,3,-9,-7,-10,-9,-10,-6,-2,-9,3,-4,-1,3,4,-10,-2,-6,-1,-9,8,5,5,-6,2,-3,-3,5,-8,9,10,-8,-4,5,-9,-8,2,-4,-9,-5,6,-5,9,-4,2,-10,3,-7,4,4,-8,-10,-10,-9,-3,-9,6,-9,-7,1,-6,-2,-1,-8,10,-8,-6,1,3,2,-6,-6,-6,7,-9,1,-1,6,1,-7,-6,9,3,6,2,1,-1,-2,1,-10,-10,-6,5,1,6,7,2,3,-8,1,-7,9,9,-4,-1,-3,-7,-9,10,10,-9,7,-5,-9,9,4,-2,5,4,-6,-6,-5,-9,-7,8,7,6,-9,4,5,-9,1,-4,5,-6,5,1,6,8,-8,-3,-4,-9,-10,-2,-8,8,2,-4,1,1,1,-10,1,2,-4,6,-4,2,10,2,5]], dtype = "int16")#candidate|16604|(1, 165)|const|int16
const_16605 = relay.const([-1,-8,-8,-10,1,8,8,1,7,-10,2,8,8,-8,-8,-1,-2,3,6,-1,-5,-8,10,-7,-7,-9,-10,3,-5,-10,5,-3,-8,9,2,-10,-8,2,-8,-7,5,-5,1,3,-10,8,-4,-2,-9,-8,-10,2,7,-8,-2,-1,8,-3,6,4,1,-1,5,7,4,-9,-6,-2,4,9,4,-2,-7,-3,1,1,1,6,5,2,-1,-4,3,-1,8,10,9,8,6,-3,1,8,-5,-8,2,-2,2,-1,3,-1,-9,5,-2,7,6,-5,-3,-7,-1,-1,-6,5,10,-4,-5,4,-5,-5,-3,4,-2,4,-4,-8,-7,-8,-3,-2,9,3,-10,-10,-7,-1,9,10,6,1,-5,7,-7,5,-5,2,-1,-8,6,-6,-6,3,-2,-1,5,8,-10,-1,7,-6,1,8,6,4,7,5,5,-1,1,5,1,-7,8,7,-4,-2,4,8,8,-2,-10,-8,-6,-3,-10,-2,-2,3,5,-7,-4,5,-7,-10,2,9,10,8,10,-1,-10,3,-2,-1,-6,-5,7,10,2,10,1,-8,9,-7,1,-9,-2,2,9,-10,-4,-7,4,7,-7,-2,6,-1,9,-4,-7,1,5,1,1,-9,6,-7,5,-10,9,-3,3,-10,4,-5,4,10,9,3,5,-6,8,-5,5,7,7,-9,-4,5,2,8,-3,-7,-10,-4,-2,7,-4,-5,6,-3,10,3,2,1,-7,-1,-7,-5,-9,-1,-1,-1,9,-4,-7,-7,-10,4,-10,7,4,-8,-8,-8,-3,-6,-9,9,-6,-4,9,-4,4,4,-3,-1,-1,-7,-3,-4,6,-1,10,3,-1,10,10,1,-10,-10,-8,-1,2,-5,-5,-1,2,7,4,-7,7,-6,-9,-3,-2,3,5,-8,-2,-2,-6,9,9,-10,-6,-7,-4,1,10,4,6,3,-1,-8,5,-1,5,9,-4,6,-3,4,-5,-3,-9,-8,-4,6,-1,-10,6,-9,1,-4,4,6,2,7,5,2,-6,-10,-1,-10,3,-1,3,-10,6,9,6,9,5,5,7,5,8,-6,4,-1,5,-5,-2,3,1,-7,-9,-4,6,6,9,-7,-7,-3,-8,-7,6,3,7,5,-8,-4,3,-1,1,10,-1,6,1,-8,-6,4,-6,-10,-5,-10,1,9,-4,-1,-2,-3,-10,-8,10,2,10,8,4,-9,-4,1,-3,-9,5,-1,5,-7,-5,-7,-2,9,-4,-9,6,7,-9,7,-9,8,-8,-8,-3,7,-9,-2,-3,4,-7,-6,-3,7,9,1,-2,-1,-7,3,-5,9,7,6,2,9,-3,4,-8,-5,5,-7,6,-7,-9,5,3,8,5,3,-4,-7,-7,-10,-4,-2,-2,5,-6,-10,-3,9,-1,9,10,3,4,10,3,-4,6,7,4,-5,4,-5,2,-6,-10,-7,9,-4,-2,-2,-4,-3,2,-8,3,7,9,-6,-4,2,-7,6,-2,7,-5,-10,-7,9,4,8,-9,5,-6,8,1,-6,10,-4,-2,-6,-4,-4,-9,2,8,-1,4,-6,-4,10,4,-8,8,9,-5,-7,-9,-9,3,4,-3,10,-10,8,9,-1,-8,9,1,7,1,6,-2,10,8,7,-8,9,-3,2,-8,5,4,-1,-10,-2,10,-2,-4,-10,-8,-4,-3,-4,9,-8,-1,-3,7,-1,-2,-1,-2,7,-9,6,5,4,2,-6,-4,-10,-7,9,6,-4,-2,3,10,-7,8,-6,5,2,-8,8,1,6,-2,-6,2,7,7,-7,1,-5,9,-3,-1,-2,1,10,10,2,10,10,-9,7,8,-2,10,-9,1,3,-5,3,-7,-10,1,-8,-9,5,5,4,8,4,7,6,5,10,-4,-6,7,7,7,9,4,-5,-7,-4,-7,10,-2,-2,8,7,-6,-5,8,-3,7,-2,-9,2,8,-9,-4,10,7,-1,5,-9,10,8,-5,-2,4,-5,-2,6,-3,-6,-8,-1,8,2,-9,-4,4,-6,2,1,-5,-8,-3,7,-3,-1,7,6,7,9,-10,4,7,-10,1,7,-6,-2,-1,-5,2,-3,-9,4,-8,1,-8,-9,8,-3,1,-6,5,5,9,-8,5,9,2,-1,8,10,8,2,9,6,5,8,-2,-6,5,1,7,8,-5,2,1,-3,1,7,-9,3,-5,-6,4,-5,7,-10,5,-6,7], dtype = "int16")#candidate|16605|(825,)|const|int16
call_16603 = relay.TupleGetItem(func_11821_call(relay.reshape(const_16604.astype('int16'), [1, 165]), relay.reshape(const_16605.astype('int16'), [825,]), ), 1)
call_16606 = relay.TupleGetItem(func_11824_call(relay.reshape(const_16604.astype('int16'), [1, 165]), relay.reshape(const_16605.astype('int16'), [825,]), ), 1)
output = relay.Tuple([call_16571,call_16583,call_16601,call_16603,const_16604,const_16605,])
output2 = relay.Tuple([call_16572,call_16584,call_16602,call_16606,const_16604,const_16605,])
func_16615 = relay.Function([], output)
mod['func_16615'] = func_16615
mod = relay.transform.InferType()(mod)
mutated_mod['func_16615'] = func_16615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16615_call = mutated_mod.get_global_var('func_16615')
call_16616 = func_16615_call()
output = call_16616
func_16617 = relay.Function([], output)
mutated_mod['func_16617'] = func_16617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5796_call = mod.get_global_var('func_5796')
func_5798_call = mutated_mod.get_global_var('func_5798')
call_16651 = relay.TupleGetItem(func_5796_call(), 0)
call_16652 = relay.TupleGetItem(func_5798_call(), 0)
func_10373_call = mod.get_global_var('func_10373')
func_10376_call = mutated_mod.get_global_var('func_10376')
var_16654 = relay.var("var_16654", dtype = "float32", shape = (672,))#candidate|16654|(672,)|var|float32
call_16653 = relay.TupleGetItem(func_10373_call(relay.reshape(var_16654.astype('float32'), [7, 16, 6])), 0)
call_16655 = relay.TupleGetItem(func_10376_call(relay.reshape(var_16654.astype('float32'), [7, 16, 6])), 0)
func_7003_call = mod.get_global_var('func_7003')
func_7004_call = mutated_mod.get_global_var('func_7004')
call_16656 = relay.TupleGetItem(func_7003_call(), 1)
call_16657 = relay.TupleGetItem(func_7004_call(), 1)
output = relay.Tuple([call_16651,call_16653,var_16654,call_16656,])
output2 = relay.Tuple([call_16652,call_16655,var_16654,call_16657,])
func_16659 = relay.Function([var_16654,], output)
mod['func_16659'] = func_16659
mod = relay.transform.InferType()(mod)
var_16660 = relay.var("var_16660", dtype = "float32", shape = (672,))#candidate|16660|(672,)|var|float32
output = func_16659(var_16660)
func_16661 = relay.Function([var_16660], output)
mutated_mod['func_16661'] = func_16661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14345_call = mod.get_global_var('func_14345')
func_14347_call = mutated_mod.get_global_var('func_14347')
call_16694 = func_14345_call()
call_16695 = func_14345_call()
func_8310_call = mod.get_global_var('func_8310')
func_8311_call = mutated_mod.get_global_var('func_8311')
call_16719 = func_8310_call()
call_16720 = func_8310_call()
output = relay.Tuple([call_16694,call_16719,])
output2 = relay.Tuple([call_16695,call_16720,])
func_16768 = relay.Function([], output)
mod['func_16768'] = func_16768
mod = relay.transform.InferType()(mod)
mutated_mod['func_16768'] = func_16768
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16768_call = mutated_mod.get_global_var('func_16768')
call_16769 = func_16768_call()
output = call_16769
func_16770 = relay.Function([], output)
mutated_mod['func_16770'] = func_16770
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16777 = relay.var("var_16777", dtype = "uint32", shape = (2, 7, 16))#candidate|16777|(2, 7, 16)|var|uint32
var_16778 = relay.var("var_16778", dtype = "uint32", shape = (2, 7, 16))#candidate|16778|(2, 7, 16)|var|uint32
bop_16779 = relay.bitwise_or(var_16777.astype('uint32'), relay.reshape(var_16778.astype('uint32'), relay.shape_of(var_16777))) # shape=(2, 7, 16)
func_10653_call = mod.get_global_var('func_10653')
func_10655_call = mutated_mod.get_global_var('func_10655')
call_16790 = relay.TupleGetItem(func_10653_call(), 1)
call_16791 = relay.TupleGetItem(func_10655_call(), 1)
output = relay.Tuple([bop_16779,call_16790,])
output2 = relay.Tuple([bop_16779,call_16791,])
func_16794 = relay.Function([var_16777,var_16778,], output)
mod['func_16794'] = func_16794
mod = relay.transform.InferType()(mod)
var_16795 = relay.var("var_16795", dtype = "uint32", shape = (2, 7, 16))#candidate|16795|(2, 7, 16)|var|uint32
var_16796 = relay.var("var_16796", dtype = "uint32", shape = (2, 7, 16))#candidate|16796|(2, 7, 16)|var|uint32
output = func_16794(var_16795,var_16796,)
func_16797 = relay.Function([var_16795,var_16796,], output)
mutated_mod['func_16797'] = func_16797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14345_call = mod.get_global_var('func_14345')
func_14347_call = mutated_mod.get_global_var('func_14347')
call_16806 = func_14345_call()
call_16807 = func_14345_call()
func_15160_call = mod.get_global_var('func_15160')
func_15163_call = mutated_mod.get_global_var('func_15163')
const_16825 = relay.const([6.101089,-9.545616,-9.054821,2.041876,-1.792772,5.552670,-6.395940,3.953964,9.147189,6.036140,1.535079,-6.943830,-6.003512,8.078664,8.035508,5.977652,-8.248687,-4.391203,-6.706680,-7.827036,0.714117,-5.406238,-9.227517,7.729279,8.551777,-0.345644,4.122347,5.790400,1.507903,7.675323,5.616282,3.470205,-2.144122,-6.537764,0.103644,6.349740,-6.532308,-4.654492,2.176784,3.177528,-5.500012,8.967557,-1.785627,0.318416,3.194225,-1.670997,-9.994732,-9.086766,5.732810,8.380659,7.976378,-3.254422,-7.668608,-9.002249,-5.946267,-9.873205,8.127748,-9.423441,2.947567,4.165550,-2.298842,9.642287,-6.457499,0.418621,1.598760,-7.771364,8.662686,-4.845398,-2.110736,-6.978828,-5.033820,1.616633,-0.843567,5.298749,-0.391311,5.876678,8.401352,4.681205,-4.667323,5.898421,1.565832,3.838074,-5.403483,-5.756643,-8.359818,-5.867055,6.852809,4.342339,7.957698,2.288021,6.054424,9.238433,-2.873412,-2.071712,9.544014,-2.617670,-0.671830,-2.473241,7.885124,1.211162,2.483198,1.292319,1.965305,-8.709369,3.758314,-6.110248,-9.385873,5.963159,-3.110742,-1.837256,-3.770320,-1.613629,-2.117565,3.424525,4.160873,4.145700,-9.070743,-2.455617,8.969625,6.501399,-5.970315,-9.311576,4.937172,1.779079,5.275043,7.870651,-8.323420,-1.726439,-2.327516,1.509144,-8.785059,-5.742018,3.776008,0.762878,-9.975035,3.526955,-8.823538,0.040565,-7.741999,-0.332668,-0.605959,8.971717,8.309704,6.191813,4.102027,-3.064075,-7.543033,0.694222,3.449977,-4.352175,0.544361,-6.801525,2.727483,5.793366,4.093161,-5.695141,6.837386,-6.628717,4.107695,0.168614,-3.918530,6.470128,-9.025439,-2.801102,8.798592,7.841420,4.332488,-3.550872,-9.985817,-4.968092,1.234945,3.767204,-1.609768,-7.025487,-3.683952,-5.186374,7.125077,4.117335,-2.079491,9.376315,-5.973701,-2.557826,-0.754055,6.200940,-3.200732,-6.172554,-1.326563,1.728688,-4.950788,-6.975145,4.579406,3.226261,-8.271889,-2.444200,9.293032,-2.564046,6.443382,6.415812,-7.128874,-7.739734,-8.703859,-8.986518,-0.169640,9.619496,7.838032,1.869094,-3.168422,6.811808,1.822572,-9.875511,4.305574,6.439453,7.897138,4.034837,8.874983,4.888456,-9.991362,-8.656728,5.922731,0.477253,5.696562,7.777951,-9.202295,9.067428,-6.435251,-0.247234,-1.355680,-2.491091,-9.298761,2.714837,9.242413,6.998334,6.142798,5.196499,5.587351,8.635248,9.996875,-8.041601,-7.326553,-9.245823,6.316548,-2.132283,-8.066420,-7.562716,-8.914506,-7.913200,-5.315811,-4.015130,7.526756,-3.956029,-8.891111,5.239500,-8.325795,2.752772,6.342420,6.093587,-5.073090,9.318678,4.594286,7.373759,7.755925,4.319211,8.235589,3.186629,8.771062,7.531870,-9.318745,-7.189227,0.747612,1.696952,8.641903,5.053749,-3.203146,-7.049234,-8.716416,-9.324941,9.195066,9.010856,8.958854,4.128276,-3.774752,-2.753844,6.962914,7.512758,6.987465,-8.687767,-5.956685,-2.860547,-3.182866,-6.347785,6.371601,-7.027743,-8.476939,1.924124,5.751453,0.653885,-3.149727,-0.848732,-8.131380,-6.025309,-2.138277,-5.709306,-6.984866,0.896847,2.312405,-6.613732,-2.676879,4.729242,-6.393609,-5.049802,8.781417,-2.526413,-1.937192,9.704545,-7.859408,-3.664185,-2.268078,7.654117,6.326881,4.201573,-5.891082,0.219212,7.336625,-0.996331,-1.322878,5.730717,-9.717067,2.191750,-2.360918,6.256786,-4.103562,2.383179,-8.169231,7.105106,6.543280,-2.078411,-9.545951,4.733864,-9.986207,-4.482087,-1.909514,-6.141477,6.270563,5.385923,-5.883042,-9.977772,-1.078495,-1.263167,0.107071,9.460660,-6.403058,-2.187386,1.294774,-4.669807,6.129135,-5.911572,-0.918050,-6.263695,-3.481982,6.379667,-1.194591,4.082540,5.139804,9.799998,-2.164515,-3.530644,-9.087195,8.867474,-9.335513,0.749567,-4.417558,3.519659,-1.137601,-6.765648,-7.738900,-3.079163,-2.340414,3.512146,4.091046,-0.529826,9.612022,-1.796378,9.078544,-3.541230,-8.510945,-3.199355,9.094523,4.862836,5.632390,2.824201,-6.874930,2.212384,2.764214,-9.290466,8.907362,-4.631163,2.048473,4.597638,9.462588,-0.023402,6.635295,-4.629655,7.269108,6.231325,-1.890948,-1.981195,-7.595709,0.046681,-7.170064,-4.063229,-0.691929,9.619577,2.406534,-5.177187,-7.582002,-6.962995,6.145732,-2.933993,2.749053,-9.393552,-5.289326,-6.680422,-6.268881,0.839927,4.867305,-7.865311,-0.569186,-0.307602,-2.017723,-8.761305,7.280659,0.392958,-1.882370,7.925838,4.957525,1.760971,-9.750799,-1.939407,3.538813,-2.939880,5.443290,-8.632910,-1.628846,4.320334,6.504523,7.873908,7.830150,-1.141986,-5.318049,0.727292,8.169880,-0.171869,-3.218235,-5.533038,-4.437019,-7.976103,6.132450,2.524852,4.850971,6.768323,9.078378,-1.758498,4.780211,-3.552183,-0.448964,1.118676,-6.906515,-6.644851,-3.647828,-1.363248,7.729304,-7.615405,0.152287,-4.918988,-2.377172,2.981795,-4.340767,-2.427419,-8.307549,9.221965,-9.649486,-1.450871,-4.572063,7.514985,0.782952,8.118093,8.526560,-4.172193,-2.161971,8.901645,-7.403716,-8.240271,-7.833467,-6.181802,1.149928,-0.928165,-4.493784,-4.302061,7.890139,8.036896,0.433029,3.498887,-9.069182,3.690577,-8.187392,8.756331,2.811307,3.388642,8.801210,9.749356,8.422185,-4.135993,-9.855146,2.059245,7.009531,2.396716,7.000238,8.575795,-0.124020,-3.612926,3.849053,8.129196,7.358694,5.367658,-3.873106,3.193332,-1.041333,8.829433,-9.065709,-8.081445,1.098727,-1.135838,-7.422863,-9.191091,-7.124698,5.720522,-7.004880,5.140813,2.944654,-6.420143,7.007989,2.927314,-4.900795,-1.195329,0.588073,-7.983561,-3.880904,-5.267265,-6.943345,6.204432,0.185234,-0.816930,5.874720,-5.509946,-1.161344,-3.880946,-2.496922,6.754477,-6.995720,-2.759998,-9.858339,-2.687261,2.808168,4.091702,2.586864,2.395634,1.748654,4.893326,0.021573,6.241305,-0.879788,8.878933,-3.274487,7.659779,-3.310718,-3.410171,-4.884896,-0.609377,7.326016,2.215524,-6.302560,-2.922370,1.654945,1.515216,0.616759,-5.009725,-6.363596,-3.325095,3.105211,-5.113695,7.005442,-0.503190,0.967132,-3.053783,7.002662,-5.472887,-9.959461,4.511292,-7.396030,-0.948348,-2.208345,8.948836,-0.193032,0.468930,-0.267308,4.994333,-8.783310,0.072973,-9.739559,5.925328,-7.593323,-3.099789,-2.880028,-1.759040,-3.180144,-2.347307,8.572137,7.727073,1.506918,5.856239,-9.056299,-6.492113,8.220090,9.686396,1.642414,3.119140,-2.098702,-2.965778,4.996666,4.021672,0.677926,-0.415776,5.265428,-5.138655,-8.906532,-7.760725,-3.871916,-8.854388,6.533201,-8.301180,-7.953164,-5.473534,6.896970,5.257872,7.043603,-7.026418,-1.325176,2.727297,-3.853124,-8.292536,-7.083879,-8.341725,6.772639,-5.977470,-0.489061,4.001290,-3.766261,0.033795,-7.617999,-4.020030,0.846325,-9.357779,-4.593135,5.553450,4.313224,3.323807,0.915791,4.050230,-6.369163,8.289395,-0.384764,4.930573,-1.440490,-1.719704,8.513829,-4.767423,9.562275,-9.547478,-6.973699,-0.911243,-6.073748,6.093211,1.143455,-2.312385,-3.483948,-7.450833,6.842896,9.494170,-2.942412,-7.101374,6.054470,-1.927398,-3.174503,-1.812041,7.272545,-3.492282,-3.975565,3.755825,-8.018762,-5.218616,7.466540,5.576817,-7.737086,-9.336773,-1.129494,8.265165,6.729694,-7.589068,-6.843500,-7.870792,-0.254345,6.140534,8.034752,-5.627690,2.997809,-5.831132,-9.363330,8.921453,6.087140,2.299227,-1.014522,1.570586,1.538855,0.392751,-0.599685,2.224342,4.749425,5.596489,4.240777,-2.625671,-7.852122,0.534307,6.612353,-1.685624,-3.071735,-0.582351,-9.477091,-1.868269,-9.932317,4.886760,9.472727,4.529156,-1.976100,0.178838,-4.725066,-1.106040,6.720970,3.605500,-6.172751,6.944745,-9.035552,2.965740,2.117460,-9.176525,-6.769722,-3.452902,-2.896705,-7.256676,-5.424109,-7.044237,7.979944,-8.350715,-8.285428,4.804964,6.426484,2.297590,0.859064,-8.162114,-8.636496,-2.281088,-4.897527,-9.361790,-6.772853,9.159948,0.430584,8.849183,-8.273889,9.015648,-2.386854,9.821715,9.881126,7.865288,-9.094226,6.588395,-1.661777,5.424942,-5.593118,5.706679,-8.183254,9.097041,-5.125161,-1.600810,-6.561461,8.477787,3.053014,-4.555536,4.626306,5.895615,9.573563,-1.202806,-7.589208,1.956959,6.164735,5.541483,0.805700,1.024804,8.693255,5.718299,2.740645,-7.393081,3.239381,5.532827,-6.142627,-8.126052,7.350911,8.136011,-0.291594,-8.936041,5.493985,0.712466,7.981541,-1.928793,6.696920,-8.111663,-0.987754,6.858628,-0.675672,-7.706297,3.921863,-6.444609,9.970993,-2.145982,-9.234905,-6.495206,-7.671356,7.236231,-8.179122,-3.933063,1.217040,9.849898,-7.630258,0.096464,8.301214,8.257717,0.248756,-1.367014,-4.839651,-7.583158,5.391906,-1.298412,1.661650,1.610658,-4.991726,5.753971,5.213890,1.822949,7.321844,-5.961801,5.835615,1.830352,9.138277,4.230717,-3.338994,1.781452,-5.381623,0.243570,1.388828,-2.764208,-5.369537,1.376119,-4.381840,7.225542,0.566728,-7.071984,-0.101404,5.865669,7.679654,4.417587,1.839682,-6.347892,-7.418409,4.352808,-4.951521,6.142496,5.644482,-6.247301,-5.811070,8.750055,5.406256,-7.696045,1.945348,-9.249962,-3.370417,-7.440313,-7.600817,-1.214110,-9.078357,-8.540100,5.372275,0.375759,-1.423969,-5.146096,-6.598513,-6.328878,3.451836,0.285637,8.450654,-0.806668,1.711336,3.118988,1.972771,-9.015686,4.338297,-0.035894,0.735767,0.944032,-9.104448,-5.764308,7.479491,-9.221788,7.275911,9.624193,8.931301,-0.608165,-1.292562,-9.806804,0.045426,8.320600,3.731204,9.089919,8.295909,-7.735867,-7.508315,-3.652291,-5.757819,1.803131,-8.667970,-7.766897,-9.136197,-1.995754,-2.303245,-2.141612,-5.386622,-1.850361,3.422042,-1.833276,-1.566078,-4.639438,9.551306,-8.389152,-0.015683,9.796179,-2.881761,-5.388730,-3.903931,3.513417,-0.384652,3.797003,2.777233,-4.873992,7.765722,2.437090,-9.093052,1.611986,2.858153,1.036713,7.743285,-0.555134,-2.325888,-5.927014,-2.306863,5.863128,7.844202,2.985236,-8.396944,5.117748,-8.825053,0.336961,3.672766,-0.877687,-4.288047,-9.914197,-8.579213,4.887200,3.182722,7.662284,7.924516,-9.870432,1.881423,9.826786,-0.398551,-7.409331,1.177624,6.090763,-0.316391,6.960417,6.896964,-0.030849,7.143991,-1.204311,7.551136,-9.415063,-0.615611,9.407184,-6.304177,5.913999,6.669907,5.324617,2.613217,3.366428,-0.143445,-5.614526,-7.375492,7.980134,-5.375580,9.436883,9.948962,-7.343885,-3.523490,-0.542664,-7.862810,6.081780,1.706249,-3.102336,4.188626,-0.059243,6.607691,6.053665,2.169090,0.493565,-0.698497,4.342447,-4.665404,6.351470,9.731219,0.180514,9.329653,2.577490,5.640823,3.013096,-2.685321,-7.954861,-4.251220,8.659333,-0.783918,5.021053,5.324127,-5.309008,-6.587912,2.478737], dtype = "float32")#candidate|16825|(1050,)|const|float32
call_16824 = relay.TupleGetItem(func_15160_call(relay.reshape(const_16825.astype('float32'), [10, 7, 15])), 1)
call_16826 = relay.TupleGetItem(func_15163_call(relay.reshape(const_16825.astype('float32'), [10, 7, 15])), 1)
func_7928_call = mod.get_global_var('func_7928')
func_7929_call = mutated_mod.get_global_var('func_7929')
call_16829 = func_7928_call()
call_16830 = func_7928_call()
func_4628_call = mod.get_global_var('func_4628')
func_4629_call = mutated_mod.get_global_var('func_4629')
call_16846 = func_4628_call()
call_16847 = func_4628_call()
bop_16848 = relay.equal(call_16829.astype('bool'), relay.reshape(call_16846.astype('bool'), relay.shape_of(call_16829))) # shape=(1, 10, 10)
bop_16851 = relay.equal(call_16830.astype('bool'), relay.reshape(call_16847.astype('bool'), relay.shape_of(call_16830))) # shape=(1, 10, 10)
func_10858_call = mod.get_global_var('func_10858')
func_10866_call = mutated_mod.get_global_var('func_10866')
const_16860 = relay.const([-7.871367,-8.089953,-4.490235,0.496730,-1.350475,2.240420,1.253786,-4.829778,2.360895,4.016660,-4.715457,8.688942,2.445842,4.564697,3.896454,-9.744643,-0.692843,3.577961,1.193772,7.941712,7.824141,-1.711460,-1.581452,-1.634603,-1.906919,-8.305906,5.820948,-4.800703,1.348836,-1.030043,-5.917972,-3.159400,9.390809,-6.626666,1.042360,-4.089766,-5.965084,1.398441,-6.473542,-9.668110,9.698724,4.746647,-8.842620,-8.790395,-5.559828,-0.441447,7.395621,6.283837], dtype = "float64")#candidate|16860|(48,)|const|float64
const_16861 = relay.const([9,2,-5,6,-5,-8,-9,1,-2,7,-1,5,-5,2,-4,4,1,7,-2,-5,9,4,-4,4,-4,-7,-1,8,-1,6,7,1,7,3,-10,-8,4,4,7,-6,-1,7,3,-10,8,-2,-7,5,10,5,8,8,5,10,2,-6,8,4,9,-10,1,3,6,4,-8,5,-2,6,4,3,3,-8,-1,6,8,8,-9,-7,-9,-8,-10,10,3,1,-5,3,4,-1,-4,6,3,1,-4,-5,-9,-9,8,-1,7,-10,8,10,-3,-8,8,-10,7,2,-10,-4,2,6,-5,10,-10,-6,-2,-10,-9,-3,-10,9,4,1,-8,5,-8,-7,7,-9,-8,5,3,-6,-4,9,-3,3,10,3,9,-8,-8,-2,-2,4,-5,-1,-4,1,5,-2,-8,6,-9,4,7,-4,6,-4,8,2,6,-2,-10], dtype = "int16")#candidate|16861|(165,)|const|int16
var_16862 = relay.var("var_16862", dtype = "int16", shape = (825,))#candidate|16862|(825,)|var|int16
var_16863 = relay.var("var_16863", dtype = "float32", shape = (320,))#candidate|16863|(320,)|var|float32
var_16864 = relay.var("var_16864", dtype = "float64", shape = (400,))#candidate|16864|(400,)|var|float64
call_16859 = relay.TupleGetItem(func_10858_call(relay.reshape(const_16860.astype('float64'), [48,]), relay.reshape(const_16861.astype('int16'), [165,]), relay.reshape(var_16862.astype('int16'), [825,]), relay.reshape(var_16863.astype('float32'), [320,]), relay.reshape(var_16862.astype('int16'), [825,]), relay.reshape(var_16864.astype('float64'), [8, 50]), ), 11)
call_16865 = relay.TupleGetItem(func_10866_call(relay.reshape(const_16860.astype('float64'), [48,]), relay.reshape(const_16861.astype('int16'), [165,]), relay.reshape(var_16862.astype('int16'), [825,]), relay.reshape(var_16863.astype('float32'), [320,]), relay.reshape(var_16862.astype('int16'), [825,]), relay.reshape(var_16864.astype('float64'), [8, 50]), ), 11)
output = relay.Tuple([call_16806,call_16824,const_16825,bop_16848,call_16859,const_16860,const_16861,var_16862,var_16863,var_16864,])
output2 = relay.Tuple([call_16807,call_16826,const_16825,bop_16851,call_16865,const_16860,const_16861,var_16862,var_16863,var_16864,])
func_16866 = relay.Function([var_16862,var_16863,var_16864,], output)
mod['func_16866'] = func_16866
mod = relay.transform.InferType()(mod)
var_16867 = relay.var("var_16867", dtype = "int16", shape = (825,))#candidate|16867|(825,)|var|int16
var_16868 = relay.var("var_16868", dtype = "float32", shape = (320,))#candidate|16868|(320,)|var|float32
var_16869 = relay.var("var_16869", dtype = "float64", shape = (400,))#candidate|16869|(400,)|var|float64
output = func_16866(var_16867,var_16868,var_16869,)
func_16870 = relay.Function([var_16867,var_16868,var_16869,], output)
mutated_mod['func_16870'] = func_16870
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14087_call = mod.get_global_var('func_14087')
func_14089_call = mutated_mod.get_global_var('func_14089')
call_16942 = relay.TupleGetItem(func_14087_call(), 0)
call_16943 = relay.TupleGetItem(func_14089_call(), 0)
output = call_16942
output2 = call_16943
func_16949 = relay.Function([], output)
mod['func_16949'] = func_16949
mod = relay.transform.InferType()(mod)
output = func_16949()
func_16950 = relay.Function([], output)
mutated_mod['func_16950'] = func_16950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15769_call = mod.get_global_var('func_15769')
func_15771_call = mutated_mod.get_global_var('func_15771')
call_16971 = relay.TupleGetItem(func_15769_call(), 3)
call_16972 = relay.TupleGetItem(func_15771_call(), 3)
func_7047_call = mod.get_global_var('func_7047')
func_7048_call = mutated_mod.get_global_var('func_7048')
call_16989 = relay.TupleGetItem(func_7047_call(), 0)
call_16990 = relay.TupleGetItem(func_7048_call(), 0)
var_16998 = relay.var("var_16998", dtype = "float64", shape = (11, 10, 10))#candidate|16998|(11, 10, 10)|var|float64
bop_16999 = relay.equal(call_16989.astype('bool'), var_16998.astype('bool')) # shape=(11, 10, 10)
bop_17002 = relay.equal(call_16990.astype('bool'), var_16998.astype('bool')) # shape=(11, 10, 10)
func_7848_call = mod.get_global_var('func_7848')
func_7852_call = mutated_mod.get_global_var('func_7852')
var_17006 = relay.var("var_17006", dtype = "int16", shape = (165,))#candidate|17006|(165,)|var|int16
call_17005 = relay.TupleGetItem(func_7848_call(relay.reshape(var_17006.astype('int16'), [11, 15]), relay.reshape(call_16971.astype('int16'), [825,]), ), 1)
call_17007 = relay.TupleGetItem(func_7852_call(relay.reshape(var_17006.astype('int16'), [11, 15]), relay.reshape(call_16971.astype('int16'), [825,]), ), 1)
output = relay.Tuple([call_16971,bop_16999,call_17005,var_17006,])
output2 = relay.Tuple([call_16972,bop_17002,call_17007,var_17006,])
func_17029 = relay.Function([var_16998,var_17006,], output)
mod['func_17029'] = func_17029
mod = relay.transform.InferType()(mod)
var_17030 = relay.var("var_17030", dtype = "float64", shape = (11, 10, 10))#candidate|17030|(11, 10, 10)|var|float64
var_17031 = relay.var("var_17031", dtype = "int16", shape = (165,))#candidate|17031|(165,)|var|int16
output = func_17029(var_17030,var_17031,)
func_17032 = relay.Function([var_17030,var_17031,], output)
mutated_mod['func_17032'] = func_17032
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5267_call = mod.get_global_var('func_5267')
func_5268_call = mutated_mod.get_global_var('func_5268')
call_17058 = relay.TupleGetItem(func_5267_call(), 0)
call_17059 = relay.TupleGetItem(func_5268_call(), 0)
func_13068_call = mod.get_global_var('func_13068')
func_13072_call = mutated_mod.get_global_var('func_13072')
var_17061 = relay.var("var_17061", dtype = "float64", shape = (200,))#candidate|17061|(200,)|var|float64
var_17062 = relay.var("var_17062", dtype = "int16", shape = (825,))#candidate|17062|(825,)|var|int16
call_17060 = relay.TupleGetItem(func_13068_call(relay.reshape(var_17061.astype('float64'), [2, 10, 10]), relay.reshape(var_17062.astype('int16'), [55, 15]), ), 9)
call_17063 = relay.TupleGetItem(func_13072_call(relay.reshape(var_17061.astype('float64'), [2, 10, 10]), relay.reshape(var_17062.astype('int16'), [55, 15]), ), 9)
func_8343_call = mod.get_global_var('func_8343')
func_8345_call = mutated_mod.get_global_var('func_8345')
call_17069 = func_8343_call()
call_17070 = func_8343_call()
uop_17071 = relay.sinh(var_17062.astype('float64')) # shape=(825,)
output = relay.Tuple([call_17058,call_17060,var_17061,call_17069,uop_17071,])
output2 = relay.Tuple([call_17059,call_17063,var_17061,call_17070,uop_17071,])
func_17078 = relay.Function([var_17061,var_17062,], output)
mod['func_17078'] = func_17078
mod = relay.transform.InferType()(mod)
mutated_mod['func_17078'] = func_17078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17078_call = mutated_mod.get_global_var('func_17078')
var_17080 = relay.var("var_17080", dtype = "float64", shape = (200,))#candidate|17080|(200,)|var|float64
var_17081 = relay.var("var_17081", dtype = "int16", shape = (825,))#candidate|17081|(825,)|var|int16
call_17079 = func_17078_call(var_17080,var_17081,)
output = call_17079
func_17082 = relay.Function([var_17080,var_17081,], output)
mutated_mod['func_17082'] = func_17082
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8650_call = mod.get_global_var('func_8650')
func_8651_call = mutated_mod.get_global_var('func_8651')
call_17266 = func_8650_call()
call_17267 = func_8650_call()
output = call_17266
output2 = call_17267
func_17286 = relay.Function([], output)
mod['func_17286'] = func_17286
mod = relay.transform.InferType()(mod)
mutated_mod['func_17286'] = func_17286
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17286_call = mutated_mod.get_global_var('func_17286')
call_17287 = func_17286_call()
output = call_17287
func_17288 = relay.Function([], output)
mutated_mod['func_17288'] = func_17288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13566_call = mod.get_global_var('func_13566')
func_13568_call = mutated_mod.get_global_var('func_13568')
call_17325 = relay.TupleGetItem(func_13566_call(), 1)
call_17326 = relay.TupleGetItem(func_13568_call(), 1)
output = call_17325
output2 = call_17326
func_17327 = relay.Function([], output)
mod['func_17327'] = func_17327
mod = relay.transform.InferType()(mod)
mutated_mod['func_17327'] = func_17327
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17327_call = mutated_mod.get_global_var('func_17327')
call_17328 = func_17327_call()
output = call_17328
func_17329 = relay.Function([], output)
mutated_mod['func_17329'] = func_17329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13735_call = mod.get_global_var('func_13735')
func_13737_call = mutated_mod.get_global_var('func_13737')
call_17338 = func_13735_call()
call_17339 = func_13735_call()
var_17340 = relay.var("var_17340", dtype = "float32", shape = (14, 11, 11))#candidate|17340|(14, 11, 11)|var|float32
bop_17341 = relay.bitwise_and(call_17338.astype('uint8'), var_17340.astype('uint8')) # shape=(14, 11, 11)
bop_17344 = relay.bitwise_and(call_17339.astype('uint8'), var_17340.astype('uint8')) # shape=(14, 11, 11)
func_10541_call = mod.get_global_var('func_10541')
func_10544_call = mutated_mod.get_global_var('func_10544')
const_17349 = relay.const([-4.440842,6.230819,0.707229,4.328822,5.686621,-4.473148,-5.079300,-8.947999,-7.193915,-1.150173,4.463961,-4.494436,5.581714,1.904817,7.059987,-3.218406,4.419281,-6.136927,-5.584386,6.576301,7.723422,-1.458518,-7.785579,-2.046811,2.623191,-5.561735,-3.774709,0.909699,-3.752476,-7.756053,4.465337,-5.839237,-0.442579,9.851673,-6.582698,-8.378883,-7.550258,0.072829,3.060815,2.155404,3.477751,-5.783172,-8.252599,4.457687,-1.103300,2.440161,-1.691429,-7.939057,-4.674076,0.353865,6.070563,-3.600163,-0.507592,-6.675769,3.332982,-4.564988,-9.814361,-8.294179,6.809174,7.091743,6.553013,4.172111,-1.552665,-9.118281,9.860759,9.037383,-1.896885,-1.185534,-8.142606,-3.538308,0.647676,-4.874261,2.993903,-6.220375,-8.356387,1.401652,-8.902649,-2.580089,-6.358089,3.045224,-0.156858,-3.141132,-4.638827,-0.024681,-4.713524,-4.828712,7.910950,5.289126,7.775600,4.689740,1.407851,3.707207,7.874605,6.610433,0.945147,7.029090,7.588488,-8.898262,0.453688,-8.633257,6.215012,3.880824,9.096527,-4.623867,-9.091261,5.750722,-6.417129,-7.320252,-8.219062,0.808512,-7.515976,0.414845,8.853073,-8.933725,-7.945526,-4.571128,4.236770,0.734291,-5.230676,-6.504507,0.046300,-1.780906,-8.731038,-1.415302,-4.668966,-3.308021,-0.219234,2.333307,0.452408,-4.379829,-8.015612,-0.309055,-1.724698,0.588893,3.984549,-7.219768,7.836906,-1.127881,7.421238,-2.961670,-2.215921,-0.512657,-3.019284,-1.096140,7.065907,-1.294153,1.763354,-6.648556,-4.903704,-9.688023,6.856416,-0.035814,-6.821495,-1.827726,6.831447,5.479322,-7.093921,6.470676,7.675745,-9.166234,-5.315027,1.808744,2.823593,-5.857212,5.112282,8.899964,2.087030,2.017868,-9.246155,1.404201,-2.032659,-6.310723,-1.322652,6.161799,3.824244,4.507702,-2.358859,-4.024560,-4.820701,2.646372,6.853934,-7.028900,2.380595,-0.678638,3.597440,9.046606,4.729241,-0.435025,3.777668,0.635113,-0.376888,3.423768,5.616950,-0.376894,-9.989666,4.104417,3.355286,-5.252002,7.023783,-1.671511,-9.104748,-1.757344,8.940198,3.597638,1.097168,-3.175475,4.980800,-2.365470,4.843220,-8.570090,4.103864,5.663446,0.308809,7.057462,8.715571,-0.148714,1.265630,3.958942,6.426660,-5.651254,6.079817,-4.998308,-9.867547,-4.513441,-0.509199,5.793793,-1.558989,-0.031213,-0.887268,2.258976,4.906978,1.196089,-4.258108,-3.531830,9.760278,-1.017910,3.586140,-5.208404,-7.979814,0.210488,1.013599,-8.965100,7.234224,-6.679589,-2.982189,6.551985,3.214627,-0.926720,1.417192,4.710826,3.788970,-4.925604,9.762272,-1.744855,5.708724,-1.587207,-9.383577,-7.534150,1.453322,1.387751,-7.189399,6.831700,2.208337,-2.362794,-1.478591,-2.325102,3.216205,-4.792911,0.545637,-8.904349,-9.251056,4.678503,2.132492,9.091478,-6.593228,-3.960195,5.716639,-1.250666,-2.370940,-0.718412,5.965217,-1.278079,4.901564,6.922990,-6.675885,8.152124,-8.814997,2.062493,-0.843496,-6.040979,-0.305984,-3.227942,-7.104310,-8.673394,7.766307,-8.241410,7.275042,0.325022,3.260909,1.959087,8.990779,6.302040,-9.953625,1.243887,9.185635,1.824870,9.412283,1.943838,5.613336,-4.878054,-0.242528,5.144673,1.766947,-4.912076,5.004361,-2.446752,-4.571311,-6.653300,9.369931,-3.989477,4.304254,-2.945236,0.053576,-3.365156,5.650990,9.742220,8.833057,-3.877809,5.436891,-2.778525,-4.524014,3.920744,-3.928910,8.673832,-5.266160,-5.102939,-5.617888,-1.251850,-5.663332,-2.814954,4.877961,-8.198359,-9.951550,4.010710,3.148855,-5.114715,8.054619,6.908204,5.884597,8.523434,-7.623326,6.306954,-3.115976,-4.909686,-9.130895,-3.130556,-8.755041,2.251447,8.521187,-1.770354,-1.635739,6.969034,8.423251,7.067545,0.613071,-8.873432,-9.250247,-6.458232,9.745951,7.763268,0.738749,4.931491,-2.410285,-0.052716,7.373078,8.168998,8.517673,1.076454,2.651130,4.045887,3.442499,-9.084118,4.182496,-0.647577,3.002662,9.820182,-3.349195,-8.579402,5.960852,-6.226076,1.898748,-9.839875,-6.745415,3.122525,-5.913456,4.530686,-9.626074,6.194050,-7.755219,-3.289802,8.576161,3.937012,-2.538068,6.383647,-6.212195,5.303677,4.084456,0.149864,0.206075,9.734746,3.862000,-2.589828,-4.747119,-4.735269,9.954150,-4.477663,-3.553959,-0.419480,3.209111,-0.438134,-3.992127,8.199460,1.744599,1.891838,-4.094592,-1.979272,2.732630,4.138874,-9.028832,8.844572,9.134020,-2.402680,5.811710,-9.860444,-5.628892,-4.215037,-0.407119,-2.129228,-8.545627,2.278595,-6.630208,0.198735,-3.855185,7.187881,-7.023246,-4.140040,-0.670493,7.394875,-1.127826,-2.495756,-6.467076,0.915518,5.155313,-2.572582,6.964821,-8.407505,6.204965,-0.923671,-6.567085,-3.259066,-2.923869,-1.411902,0.385337,-3.111508,-8.900084,9.978696,4.251124,2.000313,-5.254246,7.972678,6.256589,-7.827944,6.240767,-4.891662,-3.206090,-3.695330,-1.673619,-1.779350,-7.487766,5.018014,0.916620,8.200354,7.130776,6.461017,-3.974700,6.564576,-6.072610,-9.520184,-8.242164,-6.758115,9.869688,8.614273,8.951116,4.272107,-7.985540,-2.207096,0.788693,6.995047,1.571436,7.117133,4.094778,9.517212,-6.305789,5.391780,9.294099,5.397109,-7.662093,-9.375411,-4.398756,1.955293,-0.208087,8.101411,5.978737,-3.860591,9.005163,-2.031815,-7.332313,7.434825,6.401049,-5.392855,-5.213104,4.810183,-7.184036,-6.680291,0.840358,-8.625755,-2.189493,-8.143268,-1.273098,-3.651666,-0.516096,-3.765338,-1.715577,5.257705,-9.421014,-1.348333,3.966542,3.614490,4.650771,6.663842,3.278552,-1.611486,2.654967,2.589694,1.731901,4.700768,-9.939858,0.811430,3.603284,-3.669230,-2.968975,-4.457997,-4.782213,2.568612,-3.051764,-2.261617,-9.997509,2.471416,2.844941,0.330935,-1.835035,-0.802975,-0.141528,5.906431,-2.305038,4.282717,9.418310,8.363694,9.373660,2.796118,0.788822,3.434154,5.025598,2.577085,7.329861,1.074733,9.497556,-6.471358,9.175637,-9.518717,2.621553,-3.551290,9.537543,-9.228997,7.996697,-9.677263,-7.401123,-4.329062,-6.408347,-5.985125,6.082571,1.355035,-3.705996,-1.732514,-0.331450,9.514032,3.941185,-5.834724,1.184892,4.151773,-4.116150,5.122411,-8.488138,-2.225704,2.501081,-3.850226,7.684552,-0.626540,-8.200166,0.912219,1.277146,-3.703005,6.777405,1.593959,-5.081492,1.452267,3.965508,9.327107,-5.862655,-6.160813,-7.644592,-6.299371,7.561192,5.316259,-6.609893,-8.961977,-2.281246,-0.975754,1.829203,-2.747342,-1.430648,-5.134151,0.801610,1.915893,-8.307053,6.715994,9.344900,-4.693123,-8.611159,-2.816177,-1.488244,-1.818008,9.907514,-1.115610,6.277303,-2.149467,-6.267019,3.783850,-0.239621,-4.683628,-9.304713,-1.612684,7.751417,-2.781953,-2.367646,-9.635113,7.598540,1.254775,7.856173,5.055903,9.119620,5.186513,6.471152,3.607257,3.763177,-8.451573,9.451493,1.579679,7.297429,5.799461,-6.105858,-3.757857], dtype = "float32")#candidate|17349|(672,)|const|float32
call_17348 = relay.TupleGetItem(func_10541_call(relay.reshape(const_17349.astype('float32'), [672,])), 2)
call_17350 = relay.TupleGetItem(func_10544_call(relay.reshape(const_17349.astype('float32'), [672,])), 2)
uop_17360 = relay.cos(var_17340.astype('float64')) # shape=(14, 11, 11)
output = relay.Tuple([bop_17341,call_17348,const_17349,uop_17360,])
output2 = relay.Tuple([bop_17344,call_17350,const_17349,uop_17360,])
func_17364 = relay.Function([var_17340,], output)
mod['func_17364'] = func_17364
mod = relay.transform.InferType()(mod)
var_17365 = relay.var("var_17365", dtype = "float32", shape = (14, 11, 11))#candidate|17365|(14, 11, 11)|var|float32
output = func_17364(var_17365)
func_17366 = relay.Function([var_17365], output)
mutated_mod['func_17366'] = func_17366
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17374 = relay.var("var_17374", dtype = "uint32", shape = (13, 15, 11))#candidate|17374|(13, 15, 11)|var|uint32
var_17375 = relay.var("var_17375", dtype = "uint32", shape = (13, 15, 11))#candidate|17375|(13, 15, 11)|var|uint32
bop_17376 = relay.greater_equal(var_17374.astype('bool'), relay.reshape(var_17375.astype('bool'), relay.shape_of(var_17374))) # shape=(13, 15, 11)
func_4522_call = mod.get_global_var('func_4522')
func_4524_call = mutated_mod.get_global_var('func_4524')
call_17383 = func_4522_call()
call_17384 = func_4522_call()
output = relay.Tuple([bop_17376,call_17383,])
output2 = relay.Tuple([bop_17376,call_17384,])
func_17386 = relay.Function([var_17374,var_17375,], output)
mod['func_17386'] = func_17386
mod = relay.transform.InferType()(mod)
mutated_mod['func_17386'] = func_17386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17386_call = mutated_mod.get_global_var('func_17386')
var_17388 = relay.var("var_17388", dtype = "uint32", shape = (13, 15, 11))#candidate|17388|(13, 15, 11)|var|uint32
var_17389 = relay.var("var_17389", dtype = "uint32", shape = (13, 15, 11))#candidate|17389|(13, 15, 11)|var|uint32
call_17387 = func_17386_call(var_17388,var_17389,)
output = call_17387
func_17390 = relay.Function([var_17388,var_17389,], output)
mutated_mod['func_17390'] = func_17390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16949_call = mod.get_global_var('func_16949')
func_16950_call = mutated_mod.get_global_var('func_16950')
call_17491 = func_16949_call()
call_17492 = func_16949_call()
func_9321_call = mod.get_global_var('func_9321')
func_9323_call = mutated_mod.get_global_var('func_9323')
call_17495 = relay.TupleGetItem(func_9321_call(), 1)
call_17496 = relay.TupleGetItem(func_9323_call(), 1)
output = relay.Tuple([call_17491,call_17495,])
output2 = relay.Tuple([call_17492,call_17496,])
func_17497 = relay.Function([], output)
mod['func_17497'] = func_17497
mod = relay.transform.InferType()(mod)
mutated_mod['func_17497'] = func_17497
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17497_call = mutated_mod.get_global_var('func_17497')
call_17498 = func_17497_call()
output = call_17498
func_17499 = relay.Function([], output)
mutated_mod['func_17499'] = func_17499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13385_call = mod.get_global_var('func_13385')
func_13387_call = mutated_mod.get_global_var('func_13387')
call_17612 = relay.TupleGetItem(func_13385_call(), 0)
call_17613 = relay.TupleGetItem(func_13387_call(), 0)
output = relay.Tuple([call_17612,])
output2 = relay.Tuple([call_17613,])
func_17667 = relay.Function([], output)
mod['func_17667'] = func_17667
mod = relay.transform.InferType()(mod)
output = func_17667()
func_17668 = relay.Function([], output)
mutated_mod['func_17668'] = func_17668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7097_call = mod.get_global_var('func_7097')
func_7099_call = mutated_mod.get_global_var('func_7099')
call_17677 = relay.TupleGetItem(func_7097_call(), 0)
call_17678 = relay.TupleGetItem(func_7099_call(), 0)
const_17691 = relay.const([[[9.417140,9.235128,7.765033,0.164507,-5.964833,3.374328,-1.751107,4.151763,7.490732,-5.812056],[-4.494443,9.962071,9.477943,-3.419179,-0.567028,-6.872666,7.885463,1.508751,6.249770,8.573291],[0.004784,5.890477,3.190557,4.381530,3.507033,-1.387533,-5.785224,7.645775,-3.238849,7.267998],[6.349123,0.064086,5.965563,2.620995,0.333604,-6.031132,-6.619539,-8.270628,-2.587154,-3.700493],[-0.259223,-3.104246,-4.926585,-9.446396,4.672680,8.996155,5.154661,5.687159,4.807556,-0.684360],[5.629644,6.237740,-6.697185,-6.844064,-4.845106,-2.621897,9.792228,4.437794,-7.577481,2.357248],[6.695891,-9.632947,2.447027,8.062182,2.716720,3.804825,5.056662,-3.121991,1.011718,-9.351070],[7.433060,-4.953641,2.478779,-8.656053,4.297237,0.470681,-2.893640,5.027371,-0.997356,-8.901119],[-0.355241,-5.518517,9.351203,-4.325843,1.324406,-2.174837,4.679508,-8.691046,-0.412647,2.277304],[-9.365260,3.163901,-2.425934,-1.113367,1.011168,-3.862000,-8.074848,1.424130,3.630904,-6.832601]]], dtype = "float64")#candidate|17691|(1, 10, 10)|const|float64
bop_17692 = relay.bitwise_or(call_17677.astype('uint16'), relay.reshape(const_17691.astype('uint16'), relay.shape_of(call_17677))) # shape=(1, 10, 10)
bop_17695 = relay.bitwise_or(call_17678.astype('uint16'), relay.reshape(const_17691.astype('uint16'), relay.shape_of(call_17678))) # shape=(1, 10, 10)
output = bop_17692
output2 = bop_17695
func_17705 = relay.Function([], output)
mod['func_17705'] = func_17705
mod = relay.transform.InferType()(mod)
output = func_17705()
func_17706 = relay.Function([], output)
mutated_mod['func_17706'] = func_17706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9910_call = mod.get_global_var('func_9910')
func_9911_call = mutated_mod.get_global_var('func_9911')
call_17740 = relay.TupleGetItem(func_9910_call(), 1)
call_17741 = relay.TupleGetItem(func_9911_call(), 1)
func_9731_call = mod.get_global_var('func_9731')
func_9733_call = mutated_mod.get_global_var('func_9733')
call_17760 = relay.TupleGetItem(func_9731_call(), 0)
call_17761 = relay.TupleGetItem(func_9733_call(), 0)
func_11039_call = mod.get_global_var('func_11039')
func_11041_call = mutated_mod.get_global_var('func_11041')
var_17773 = relay.var("var_17773", dtype = "int16", shape = (5, 165))#candidate|17773|(5, 165)|var|int16
call_17772 = relay.TupleGetItem(func_11039_call(relay.reshape(var_17773.astype('int16'), [825,])), 0)
call_17774 = relay.TupleGetItem(func_11041_call(relay.reshape(var_17773.astype('int16'), [825,])), 0)
output = relay.Tuple([call_17740,call_17760,call_17772,var_17773,])
output2 = relay.Tuple([call_17741,call_17761,call_17774,var_17773,])
func_17775 = relay.Function([var_17773,], output)
mod['func_17775'] = func_17775
mod = relay.transform.InferType()(mod)
mutated_mod['func_17775'] = func_17775
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17776 = relay.var("var_17776", dtype = "int16", shape = (5, 165))#candidate|17776|(5, 165)|var|int16
func_17775_call = mutated_mod.get_global_var('func_17775')
call_17777 = func_17775_call(var_17776)
output = call_17777
func_17778 = relay.Function([var_17776], output)
mutated_mod['func_17778'] = func_17778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14953_call = mod.get_global_var('func_14953')
func_14954_call = mutated_mod.get_global_var('func_14954')
call_17800 = func_14953_call()
call_17801 = func_14953_call()
func_8343_call = mod.get_global_var('func_8343')
func_8345_call = mutated_mod.get_global_var('func_8345')
call_17806 = func_8343_call()
call_17807 = func_8343_call()
func_14137_call = mod.get_global_var('func_14137')
func_14138_call = mutated_mod.get_global_var('func_14138')
call_17816 = relay.TupleGetItem(func_14137_call(), 0)
call_17817 = relay.TupleGetItem(func_14138_call(), 0)
bop_17824 = relay.less_equal(call_17800.astype('bool'), relay.reshape(call_17816.astype('bool'), relay.shape_of(call_17800))) # shape=(1, 10, 10)
bop_17827 = relay.less_equal(call_17801.astype('bool'), relay.reshape(call_17817.astype('bool'), relay.shape_of(call_17801))) # shape=(1, 10, 10)
func_13132_call = mod.get_global_var('func_13132')
func_13133_call = mutated_mod.get_global_var('func_13133')
call_17834 = relay.TupleGetItem(func_13132_call(), 2)
call_17835 = relay.TupleGetItem(func_13133_call(), 2)
output = relay.Tuple([call_17806,bop_17824,call_17834,])
output2 = relay.Tuple([call_17807,bop_17827,call_17835,])
func_17838 = relay.Function([], output)
mod['func_17838'] = func_17838
mod = relay.transform.InferType()(mod)
mutated_mod['func_17838'] = func_17838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17838_call = mutated_mod.get_global_var('func_17838')
call_17839 = func_17838_call()
output = call_17839
func_17840 = relay.Function([], output)
mutated_mod['func_17840'] = func_17840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4628_call = mod.get_global_var('func_4628')
func_4629_call = mutated_mod.get_global_var('func_4629')
call_17848 = func_4628_call()
call_17849 = func_4628_call()
func_16303_call = mod.get_global_var('func_16303')
func_16305_call = mutated_mod.get_global_var('func_16305')
const_17867 = relay.const([0.689838,5.311213,9.380888,-7.991060,-0.816345,8.137847,-1.066409,0.931363,4.757062,0.158856,-0.728348,5.075611,-7.185209,-8.528313,0.346947,-6.902364,-5.362517,-8.592892,-2.503077,-3.568024,-1.756476,-5.955330,-1.098833,-5.601903,7.623788,8.185283,1.196464,-5.310571,7.037529,6.001171,-3.410888,8.537876,-9.600804,-4.859619,5.595455,2.735589,2.963272,-5.087199,3.294394,6.125418,-4.446986,-0.022387,-6.424127,1.341735,2.544947,-1.273821,-9.510884,2.311414,8.091081,9.244327,-8.041494,3.618265,-4.048252,0.184972,-9.615019,0.638813,0.800107,-1.491381,-9.381856,-8.196516,6.221996,1.210416,-6.030224,-6.069039,-7.228968,-9.565976,-9.109375,-9.017294,7.944600,-2.527079,3.439118,-5.866967,4.964547,-1.841887,-0.631875,-5.334957,9.311730,2.488579,-7.672424,8.690757,3.069820,3.530641,4.043270,9.275291,5.114678,-6.469068,8.514163,1.940369,-4.982396,-2.847091,-4.070174,-8.607852,-4.751527,-3.256396,4.133329,4.927576,5.016717,-7.430032,8.152175,-9.141051,1.131539,0.995905,4.961925,6.539620,-2.354352,8.102625,-5.344196,-7.603687,5.614780,9.804313,-0.258063,-6.826599,5.400252,4.427829,-3.176123,8.279790,-1.818445,-2.427808,-5.180609,0.139042,4.415797,2.021582,-2.969776,-1.645253,-7.445042,-4.479073,-1.219783,8.950021,6.196259,-7.007873,-8.771671,4.450668,-0.348207,-2.915416,-6.338343,7.888699,-6.979789,3.515977,-9.191895,0.010195,-3.162855,-3.784206,-9.720591,-3.943493,-4.534511,8.111039,3.688937,8.307663,-9.949436,-3.728599,-1.124197,-6.074848,-4.869685,6.916494,6.677028,-0.977383,6.027348,-7.779807,-6.396318,2.640517,-1.317488,0.307297,-2.423216,4.866279,-3.643073,6.057502,-8.139956,-7.385098,8.524542,8.935215,-7.946528,-0.082581,-5.411546,6.034062,-2.958944,1.988766,3.567275,-5.972079,-5.124454,-5.125236,4.539829,1.606963,1.058693,-6.497921,0.199865,6.010192,8.972735,1.066455,-5.238624,-8.995251,-1.193433,0.156072,-1.079900,3.147767,-8.474675,-3.302658,6.749998,0.356676,9.842461,6.015505,8.217410,-9.715463,9.288917,1.222841,-5.903815,-4.734725,2.782551,-3.399472,8.021602,-6.283064,2.202333,0.788591,-4.108546,6.732752,-1.915224,0.248303,8.008186,3.660714,2.760261,-4.638827,-2.027087,-9.886253,0.089892,-6.965012,-1.050617,-1.419213,5.305854,-6.275959,-7.752590,7.803579,4.302543,-2.251292,-0.173595,8.302154,-6.362011,5.469520,-5.711562,1.985460,-6.809388,-5.821953,-1.556716,-2.070531,-8.434239,-4.000363,-8.247107,1.307897,-6.812857,-8.258480,0.313627,-4.955498,3.189795,0.126822,-0.663968,9.065819,-4.553335,1.710327,-8.960472,-4.579501,9.973865,1.904916,-0.618696,7.261341,6.575728,5.958767,1.041103,-4.974059,7.621454,-4.088570,-5.989656,-9.922013,9.087903,-9.631539,5.022935,-7.020540,3.585478,-0.824457,-0.427574,-3.781722,8.035558,0.995168,6.401888,3.161416,1.399881,-9.229312,-0.295246,-9.481748,2.439624,4.724417,3.695380,2.975085,-5.593423,-6.704347,6.829880,-6.302524,-7.173426,4.488770,1.633219,-8.594386,-0.112847,5.020862], dtype = "float32")#candidate|17867|(300,)|const|float32
call_17866 = relay.TupleGetItem(func_16303_call(relay.reshape(const_17867.astype('float32'), [300,])), 1)
call_17868 = relay.TupleGetItem(func_16305_call(relay.reshape(const_17867.astype('float32'), [300,])), 1)
output = relay.Tuple([call_17848,call_17866,const_17867,])
output2 = relay.Tuple([call_17849,call_17868,const_17867,])
func_17878 = relay.Function([], output)
mod['func_17878'] = func_17878
mod = relay.transform.InferType()(mod)
output = func_17878()
func_17879 = relay.Function([], output)
mutated_mod['func_17879'] = func_17879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17286_call = mod.get_global_var('func_17286')
func_17288_call = mutated_mod.get_global_var('func_17288')
call_17880 = func_17286_call()
call_17881 = func_17286_call()
func_14884_call = mod.get_global_var('func_14884')
func_14886_call = mutated_mod.get_global_var('func_14886')
call_17894 = relay.TupleGetItem(func_14884_call(), 0)
call_17895 = relay.TupleGetItem(func_14886_call(), 0)
output = relay.Tuple([call_17880,call_17894,])
output2 = relay.Tuple([call_17881,call_17895,])
func_17913 = relay.Function([], output)
mod['func_17913'] = func_17913
mod = relay.transform.InferType()(mod)
output = func_17913()
func_17914 = relay.Function([], output)
mutated_mod['func_17914'] = func_17914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11253_call = mod.get_global_var('func_11253')
func_11254_call = mutated_mod.get_global_var('func_11254')
call_17947 = relay.TupleGetItem(func_11253_call(), 1)
call_17948 = relay.TupleGetItem(func_11254_call(), 1)
output = relay.Tuple([call_17947,])
output2 = relay.Tuple([call_17948,])
func_17949 = relay.Function([], output)
mod['func_17949'] = func_17949
mod = relay.transform.InferType()(mod)
output = func_17949()
func_17950 = relay.Function([], output)
mutated_mod['func_17950'] = func_17950
mutated_mod = relay.transform.InferType()(mutated_mod)
var_18003 = relay.var("var_18003", dtype = "uint16", shape = (12, 12, 12))#candidate|18003|(12, 12, 12)|var|uint16
var_18004 = relay.var("var_18004", dtype = "uint16", shape = (12, 12, 12))#candidate|18004|(12, 12, 12)|var|uint16
bop_18005 = relay.bitwise_and(var_18003.astype('uint16'), relay.reshape(var_18004.astype('uint16'), relay.shape_of(var_18003))) # shape=(12, 12, 12)
output = bop_18005
output2 = bop_18005
func_18011 = relay.Function([var_18003,var_18004,], output)
mod['func_18011'] = func_18011
mod = relay.transform.InferType()(mod)
mutated_mod['func_18011'] = func_18011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18011_call = mutated_mod.get_global_var('func_18011')
var_18013 = relay.var("var_18013", dtype = "uint16", shape = (12, 12, 12))#candidate|18013|(12, 12, 12)|var|uint16
var_18014 = relay.var("var_18014", dtype = "uint16", shape = (12, 12, 12))#candidate|18014|(12, 12, 12)|var|uint16
call_18012 = func_18011_call(var_18013,var_18014,)
output = call_18012
func_18015 = relay.Function([var_18013,var_18014,], output)
mutated_mod['func_18015'] = func_18015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11558_call = mod.get_global_var('func_11558')
func_11559_call = mutated_mod.get_global_var('func_11559')
call_18054 = relay.TupleGetItem(func_11558_call(), 0)
call_18055 = relay.TupleGetItem(func_11559_call(), 0)
func_2680_call = mod.get_global_var('func_2680')
func_2685_call = mutated_mod.get_global_var('func_2685')
const_18059 = relay.const([[5.400894,-6.381562,9.953661,0.316835,-4.337269,-1.388890,5.245799,-7.837623,9.514590,5.764008,4.250711,-6.163260,-8.878670,6.965303,8.134398,-3.492939,5.813104,-9.496793,2.288321,6.236951],[1.449888,-6.703722,8.400807,1.505335,1.088001,6.885689,5.007920,8.109401,6.324336,-1.772143,5.308347,-5.177173,-5.499920,5.253348,-4.437985,4.686772,-6.443028,1.911437,2.578222,-5.016800],[3.680952,5.632184,-7.865622,-9.916902,7.641814,-1.370151,1.779326,2.266822,8.878939,1.412877,-0.903627,3.613292,-4.500626,-5.821341,-6.377059,5.663311,8.928196,-2.095921,3.494182,2.816886],[-6.186477,-4.502596,-5.352726,9.384469,-0.274053,-6.068456,5.237689,-6.982065,-4.277322,8.858687,6.336772,-4.597139,-7.636312,-3.570942,3.104240,-2.534907,6.504802,8.425689,4.287417,-8.280825]], dtype = "float32")#candidate|18059|(4, 20)|const|float32
var_18060 = relay.var("var_18060", dtype = "int16", shape = (55, 15))#candidate|18060|(55, 15)|var|int16
const_18061 = relay.const([3.677239,3.924503,6.147666,3.411818,-6.623477,-7.770125,-8.388859,9.897083,3.324864,-5.388202,-4.106137,-0.099919,-3.863501,3.908582,0.650087,7.013565,-2.777345,-0.012596,-3.206782,2.437627,-2.168733,3.410409,-2.380281,5.419251,5.931493,9.719424,-4.225400,-8.247168,-6.967954,-3.680653,8.063136,5.173659,7.216643,3.821149,9.742636,-8.070378,-7.527547,-7.664190,-8.285042,6.082355,7.279588,1.986562,-1.213629,-3.543355,-2.805899,1.399812,-5.031858,3.208555], dtype = "float64")#candidate|18061|(48,)|const|float64
call_18058 = relay.TupleGetItem(func_2680_call(relay.reshape(const_18059.astype('float32'), [1, 8, 10]), relay.reshape(var_18060.astype('int16'), [5, 165]), relay.reshape(const_18061.astype('float64'), [48,]), ), 4)
call_18062 = relay.TupleGetItem(func_2685_call(relay.reshape(const_18059.astype('float32'), [1, 8, 10]), relay.reshape(var_18060.astype('int16'), [5, 165]), relay.reshape(const_18061.astype('float64'), [48,]), ), 4)
func_13860_call = mod.get_global_var('func_13860')
func_13861_call = mutated_mod.get_global_var('func_13861')
call_18066 = func_13860_call()
call_18067 = func_13860_call()
output = relay.Tuple([call_18054,call_18058,const_18059,var_18060,const_18061,call_18066,])
output2 = relay.Tuple([call_18055,call_18062,const_18059,var_18060,const_18061,call_18067,])
func_18070 = relay.Function([var_18060,], output)
mod['func_18070'] = func_18070
mod = relay.transform.InferType()(mod)
mutated_mod['func_18070'] = func_18070
mutated_mod = relay.transform.InferType()(mutated_mod)
var_18071 = relay.var("var_18071", dtype = "int16", shape = (55, 15))#candidate|18071|(55, 15)|var|int16
func_18070_call = mutated_mod.get_global_var('func_18070')
call_18072 = func_18070_call(var_18071)
output = call_18072
func_18073 = relay.Function([var_18071], output)
mutated_mod['func_18073'] = func_18073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13385_call = mod.get_global_var('func_13385')
func_13387_call = mutated_mod.get_global_var('func_13387')
call_18077 = relay.TupleGetItem(func_13385_call(), 0)
call_18078 = relay.TupleGetItem(func_13387_call(), 0)
output = relay.Tuple([call_18077,])
output2 = relay.Tuple([call_18078,])
func_18080 = relay.Function([], output)
mod['func_18080'] = func_18080
mod = relay.transform.InferType()(mod)
mutated_mod['func_18080'] = func_18080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18080_call = mutated_mod.get_global_var('func_18080')
call_18081 = func_18080_call()
output = call_18081
func_18082 = relay.Function([], output)
mutated_mod['func_18082'] = func_18082
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14009_call = mod.get_global_var('func_14009')
func_14010_call = mutated_mod.get_global_var('func_14010')
call_18085 = func_14009_call()
call_18086 = func_14009_call()
output = call_18085
output2 = call_18086
func_18094 = relay.Function([], output)
mod['func_18094'] = func_18094
mod = relay.transform.InferType()(mod)
output = func_18094()
func_18095 = relay.Function([], output)
mutated_mod['func_18095'] = func_18095
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14050_call = mod.get_global_var('func_14050')
func_14051_call = mutated_mod.get_global_var('func_14051')
call_18127 = func_14050_call()
call_18128 = func_14050_call()
output = call_18127
output2 = call_18128
func_18129 = relay.Function([], output)
mod['func_18129'] = func_18129
mod = relay.transform.InferType()(mod)
mutated_mod['func_18129'] = func_18129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18129_call = mutated_mod.get_global_var('func_18129')
call_18130 = func_18129_call()
output = call_18130
func_18131 = relay.Function([], output)
mutated_mod['func_18131'] = func_18131
mutated_mod = relay.transform.InferType()(mutated_mod)
var_18189 = relay.var("var_18189", dtype = "float32", shape = (13, 5, 3))#candidate|18189|(13, 5, 3)|var|float32
uop_18190 = relay.rsqrt(var_18189.astype('float32')) # shape=(13, 5, 3)
output = relay.Tuple([uop_18190,])
output2 = relay.Tuple([uop_18190,])
F = relay.Function([var_18189,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_18189,], output2)
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
