import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_24 = relay.var("var_24", dtype = "uint8", shape = (5, 4, 2))#candidate|24|(5, 4, 2)|var|uint8
var_25 = relay.var("var_25", dtype = "uint8", shape = (5, 4, 2))#candidate|25|(5, 4, 2)|var|uint8
bop_26 = relay.greater_equal(var_24.astype('bool'), relay.reshape(var_25.astype('bool'), relay.shape_of(var_24))) # shape=(5, 4, 2)
output = relay.Tuple([bop_26,])
output2 = relay.Tuple([bop_26,])
func_31 = relay.Function([var_24,var_25,], output)
mod['func_31'] = func_31
mod = relay.transform.InferType()(mod)
var_32 = relay.var("var_32", dtype = "uint8", shape = (5, 4, 2))#candidate|32|(5, 4, 2)|var|uint8
var_33 = relay.var("var_33", dtype = "uint8", shape = (5, 4, 2))#candidate|33|(5, 4, 2)|var|uint8
output = func_31(var_32,var_33,)
func_34 = relay.Function([var_32,var_33,], output)
mutated_mod['func_34'] = func_34
mutated_mod = relay.transform.InferType()(mutated_mod)
var_79 = relay.var("var_79", dtype = "float64", shape = (2, 2, 13))#candidate|79|(2, 2, 13)|var|float64
var_80 = relay.var("var_80", dtype = "float64", shape = (2, 2, 13))#candidate|80|(2, 2, 13)|var|float64
bop_81 = relay.less_equal(var_79.astype('bool'), relay.reshape(var_80.astype('bool'), relay.shape_of(var_79))) # shape=(2, 2, 13)
bop_86 = relay.floor_divide(var_80.astype('float32'), relay.reshape(var_79.astype('float32'), relay.shape_of(var_80))) # shape=(2, 2, 13)
output = relay.Tuple([bop_81,bop_86,])
output2 = relay.Tuple([bop_81,bop_86,])
func_97 = relay.Function([var_79,var_80,], output)
mod['func_97'] = func_97
mod = relay.transform.InferType()(mod)
var_98 = relay.var("var_98", dtype = "float64", shape = (2, 2, 13))#candidate|98|(2, 2, 13)|var|float64
var_99 = relay.var("var_99", dtype = "float64", shape = (2, 2, 13))#candidate|99|(2, 2, 13)|var|float64
output = func_97(var_98,var_99,)
func_100 = relay.Function([var_98,var_99,], output)
mutated_mod['func_100'] = func_100
mutated_mod = relay.transform.InferType()(mutated_mod)
var_480 = relay.var("var_480", dtype = "int64", shape = ())#candidate|480|()|var|int64
var_481 = relay.var("var_481", dtype = "int64", shape = (15, 9, 2))#candidate|481|(15, 9, 2)|var|int64
bop_482 = relay.less(var_480.astype('bool'), var_481.astype('bool')) # shape=(15, 9, 2)
bop_490 = relay.right_shift(var_481.astype('uint64'), var_480.astype('uint64')) # shape=(15, 9, 2)
func_97_call = mod.get_global_var('func_97')
func_100_call = mutated_mod.get_global_var('func_100')
var_496 = relay.var("var_496", dtype = "float64", shape = (52,))#candidate|496|(52,)|var|float64
call_495 = relay.TupleGetItem(func_97_call(relay.reshape(var_496.astype('float64'), [2, 2, 13]), relay.reshape(var_496.astype('float64'), [2, 2, 13]), ), 0)
call_497 = relay.TupleGetItem(func_100_call(relay.reshape(var_496.astype('float64'), [2, 2, 13]), relay.reshape(var_496.astype('float64'), [2, 2, 13]), ), 0)
func_31_call = mod.get_global_var('func_31')
func_34_call = mutated_mod.get_global_var('func_34')
var_499 = relay.var("var_499", dtype = "uint8", shape = (40,))#candidate|499|(40,)|var|uint8
call_498 = relay.TupleGetItem(func_31_call(relay.reshape(var_499.astype('uint8'), [5, 4, 2]), relay.reshape(var_499.astype('uint8'), [5, 4, 2]), ), 0)
call_500 = relay.TupleGetItem(func_34_call(relay.reshape(var_499.astype('uint8'), [5, 4, 2]), relay.reshape(var_499.astype('uint8'), [5, 4, 2]), ), 0)
output = relay.Tuple([bop_482,bop_490,call_495,var_496,call_498,var_499,])
output2 = relay.Tuple([bop_482,bop_490,call_497,var_496,call_500,var_499,])
func_504 = relay.Function([var_480,var_481,var_496,var_499,], output)
mod['func_504'] = func_504
mod = relay.transform.InferType()(mod)
var_505 = relay.var("var_505", dtype = "int64", shape = ())#candidate|505|()|var|int64
var_506 = relay.var("var_506", dtype = "int64", shape = (15, 9, 2))#candidate|506|(15, 9, 2)|var|int64
var_507 = relay.var("var_507", dtype = "float64", shape = (52,))#candidate|507|(52,)|var|float64
var_508 = relay.var("var_508", dtype = "uint8", shape = (40,))#candidate|508|(40,)|var|uint8
output = func_504(var_505,var_506,var_507,var_508,)
func_509 = relay.Function([var_505,var_506,var_507,var_508,], output)
mutated_mod['func_509'] = func_509
mutated_mod = relay.transform.InferType()(mutated_mod)
const_624 = relay.const([[[2,2,5,-9],[-3,-4,-8,-5],[-2,-1,-7,-2],[2,-5,-4,-6],[-6,-10,10,-3],[-2,9,-10,4],[7,2,-4,8],[-6,-5,-7,7],[-9,4,6,6],[4,7,8,-7],[9,-1,-8,1],[4,-6,-8,4],[-10,9,-6,4],[-10,6,-4,-7]],[[4,6,-8,8],[4,3,-7,-9],[5,-4,5,-9],[-3,-7,7,2],[1,-5,-6,1],[7,1,-10,10],[2,-4,-6,-4],[-9,-5,-4,-10],[-4,5,8,-9],[-1,8,3,-7],[-5,-2,8,-9],[-8,5,-1,6],[-2,7,-7,6],[1,1,3,8]],[[1,-7,9,-7],[-10,8,9,-1],[5,2,8,-1],[-1,2,-2,-10],[-2,3,-4,-6],[-3,8,-8,-3],[-8,-8,1,3],[2,4,6,7],[4,9,10,-2],[2,3,2,-5],[-10,-7,2,3],[-5,-10,-2,9],[6,-3,5,-9],[9,7,9,10]]], dtype = "uint16")#candidate|624|(3, 14, 4)|const|uint16
var_625 = relay.var("var_625", dtype = "uint16", shape = (3, 14, 4))#candidate|625|(3, 14, 4)|var|uint16
bop_626 = relay.greater(const_624.astype('bool'), relay.reshape(var_625.astype('bool'), relay.shape_of(const_624))) # shape=(3, 14, 4)
output = relay.Tuple([bop_626,])
output2 = relay.Tuple([bop_626,])
func_635 = relay.Function([var_625,], output)
mod['func_635'] = func_635
mod = relay.transform.InferType()(mod)
mutated_mod['func_635'] = func_635
mutated_mod = relay.transform.InferType()(mutated_mod)
var_636 = relay.var("var_636", dtype = "uint16", shape = (3, 14, 4))#candidate|636|(3, 14, 4)|var|uint16
func_635_call = mutated_mod.get_global_var('func_635')
call_637 = func_635_call(var_636)
output = call_637
func_638 = relay.Function([var_636], output)
mutated_mod['func_638'] = func_638
mutated_mod = relay.transform.InferType()(mutated_mod)
var_782 = relay.var("var_782", dtype = "float32", shape = (3, 7, 5))#candidate|782|(3, 7, 5)|var|float32
uop_783 = relay.cos(var_782.astype('float32')) # shape=(3, 7, 5)
output = relay.Tuple([uop_783,])
output2 = relay.Tuple([uop_783,])
func_789 = relay.Function([var_782,], output)
mod['func_789'] = func_789
mod = relay.transform.InferType()(mod)
var_790 = relay.var("var_790", dtype = "float32", shape = (3, 7, 5))#candidate|790|(3, 7, 5)|var|float32
output = func_789(var_790)
func_791 = relay.Function([var_790], output)
mutated_mod['func_791'] = func_791
mutated_mod = relay.transform.InferType()(mutated_mod)
var_826 = relay.var("var_826", dtype = "int32", shape = (15, 6, 11))#candidate|826|(15, 6, 11)|var|int32
const_827 = relay.const([[[-9,2,-2,7,2,-8,-6,-5,-9,-5,-3],[-10,7,-3,-9,-3,-3,4,-10,7,8,-4],[-10,-5,10,-3,-2,3,9,2,-7,4,-8],[7,-1,1,-2,4,-4,3,10,-8,-1,6],[1,7,3,-1,-2,-10,-3,-4,5,-6,-8],[-4,7,5,-7,9,8,-7,7,-3,-4,-6]],[[3,-1,10,9,10,-8,-9,6,-3,3,1],[2,10,1,-6,3,6,10,-3,6,4,10],[-9,7,-3,3,2,6,-1,-6,-3,-8,2],[5,-7,-1,-6,-4,9,-9,4,6,7,8],[8,-5,-4,10,-3,3,7,-10,-5,10,-6],[4,-10,5,-6,-5,6,7,-5,8,-3,7]],[[-5,7,-3,-1,3,-10,10,2,8,-10,9],[6,6,1,3,1,5,7,4,-9,-5,-2],[4,-1,-1,-7,-10,-2,7,6,-1,9,5],[-6,-3,-8,3,5,1,-10,-1,-1,-1,5],[-6,7,8,-5,-1,-3,-5,-5,8,8,8],[-2,-8,-7,-7,7,5,-3,2,-7,-9,7]],[[1,4,2,9,-3,-10,-5,10,-1,-7,10],[9,-8,-5,7,2,-4,7,10,7,-8,-4],[5,-7,10,-3,4,4,-10,-10,3,-5,8],[-4,-10,6,9,3,4,8,-5,-6,-5,-2],[1,2,-4,10,10,4,6,-2,-10,7,-6],[-7,8,-2,6,-7,-10,9,-7,7,3,-9]],[[-9,-4,-5,-2,7,-4,7,-9,-3,-9,7],[-6,9,4,-5,10,4,-5,-4,4,8,-8],[5,7,-4,-9,-4,-5,-8,-4,-2,9,10],[-8,10,-10,9,3,-5,-2,-5,-10,-7,2],[4,10,-4,-3,-2,-1,-3,1,6,6,2],[-10,10,-8,5,-4,-7,4,-5,6,-7,10]],[[-7,-2,2,-4,-5,-3,-4,-1,2,7,-2],[-1,-9,-4,3,6,2,-2,-5,1,3,-2],[5,-8,-1,-6,-8,-7,3,5,5,5,9],[-4,-4,-2,-8,-5,-10,-2,8,3,7,4],[3,-8,-1,6,10,4,-4,2,3,-7,-8],[3,8,-3,7,-5,-9,9,-5,9,6,1]],[[10,-3,9,-7,10,-7,7,3,9,4,-2],[9,-1,-5,2,6,7,6,-1,7,2,-10],[-5,-2,-5,-4,3,-4,-2,1,5,9,-7],[2,-9,-9,-2,-1,-4,-3,1,-5,1,-9],[10,-10,-7,7,-5,2,-7,-6,-10,7,-9],[-2,-8,-7,6,-3,-7,-9,1,8,6,-1]],[[-3,-1,-1,10,9,-4,-6,-5,8,9,2],[-10,8,10,-2,-7,5,1,-8,-9,10,3],[6,-10,-5,-2,9,-1,-1,-10,-1,7,7],[-3,-6,2,-8,4,3,10,5,7,3,-10],[9,5,-9,6,-10,-2,3,-4,9,5,-2],[-3,7,2,10,-4,3,8,4,9,5,2]],[[-5,9,4,7,-10,-4,2,7,-7,-2,-2],[4,6,-2,5,9,10,-6,-3,-10,-5,10],[-8,9,9,10,2,9,-9,9,5,-6,5],[7,6,10,2,9,6,9,-1,-9,3,3],[9,8,9,10,7,-3,-7,-2,-5,-10,1],[8,-8,-5,5,5,-9,9,-10,-5,8,-9]],[[2,-3,4,-8,3,-7,3,4,-7,1,5],[-5,10,-1,7,-3,-3,6,10,-2,-7,5],[-8,-7,9,2,-9,8,-6,-10,-9,4,9],[-7,1,5,-8,-10,-1,-3,5,6,-4,-7],[-3,5,-8,-4,-6,-8,-2,-9,-3,-7,5],[7,-5,6,-5,-2,-10,10,6,6,7,-3]],[[7,9,8,-4,-4,-3,-2,-8,3,-7,7],[-2,-3,8,-2,-1,10,7,-4,1,4,6],[-6,-4,6,-4,3,9,2,-8,-6,-3,6],[6,-5,-7,2,2,2,9,-9,5,8,-8],[1,7,4,4,2,-2,-9,-5,-6,1,4],[8,-4,7,-6,2,-2,5,-1,-8,10,-1]],[[8,-10,-2,2,2,1,-4,-7,3,8,-10],[-1,-3,-7,6,-10,3,-1,-2,1,5,-9],[8,9,-5,7,1,8,7,-5,-3,-9,6],[1,5,1,2,8,5,-3,8,8,8,-1],[3,-7,-2,3,8,-5,6,2,-5,-9,-2],[3,-4,7,-8,8,8,-8,-4,10,6,5]],[[-3,-9,-9,-1,3,-9,4,3,-8,-3,-8],[9,-3,6,-6,1,-7,-10,-9,7,6,2],[-4,3,-6,10,-9,-10,8,2,-6,-3,-3],[1,-3,-5,4,10,10,4,8,-4,3,-9],[-9,-4,6,-1,-10,1,1,-4,-3,5,-6],[3,-2,-2,10,-7,4,5,-1,-9,9,4]],[[-7,-6,-3,-4,-1,4,4,10,7,5,1],[1,8,-2,-1,-8,-7,9,-7,-10,1,-4],[7,-1,5,6,-7,7,1,2,-8,-2,-7],[6,5,-4,9,3,6,-2,1,-5,9,2],[5,-1,8,-9,-4,3,-2,-8,-7,-9,-7],[1,3,4,2,-1,4,10,-5,9,6,9]],[[-8,-9,7,7,-10,-2,8,4,-6,7,-7],[3,5,-1,3,7,6,8,3,-9,-6,8],[1,-4,-7,6,-7,5,-1,1,6,-7,5],[8,-3,-2,2,-6,2,-9,-2,-4,-5,9],[5,2,-9,6,8,-1,-4,1,5,-8,-9],[7,-3,-8,-9,-4,10,-6,9,-2,-7,-8]]], dtype = "int32")#candidate|827|(15, 6, 11)|const|int32
bop_828 = relay.greater_equal(var_826.astype('bool'), relay.reshape(const_827.astype('bool'), relay.shape_of(var_826))) # shape=(15, 6, 11)
output = relay.Tuple([bop_828,])
output2 = relay.Tuple([bop_828,])
func_832 = relay.Function([var_826,], output)
mod['func_832'] = func_832
mod = relay.transform.InferType()(mod)
mutated_mod['func_832'] = func_832
mutated_mod = relay.transform.InferType()(mutated_mod)
var_833 = relay.var("var_833", dtype = "int32", shape = (15, 6, 11))#candidate|833|(15, 6, 11)|var|int32
func_832_call = mutated_mod.get_global_var('func_832')
call_834 = func_832_call(var_833)
output = call_834
func_835 = relay.Function([var_833], output)
mutated_mod['func_835'] = func_835
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1021 = relay.var("var_1021", dtype = "int8", shape = (15, 11, 14))#candidate|1021|(15, 11, 14)|var|int8
var_1022 = relay.var("var_1022", dtype = "int8", shape = (15, 11, 14))#candidate|1022|(15, 11, 14)|var|int8
bop_1023 = relay.bitwise_xor(var_1021.astype('int8'), relay.reshape(var_1022.astype('int8'), relay.shape_of(var_1021))) # shape=(15, 11, 14)
output = relay.Tuple([bop_1023,])
output2 = relay.Tuple([bop_1023,])
func_1026 = relay.Function([var_1021,var_1022,], output)
mod['func_1026'] = func_1026
mod = relay.transform.InferType()(mod)
mutated_mod['func_1026'] = func_1026
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1026_call = mutated_mod.get_global_var('func_1026')
var_1028 = relay.var("var_1028", dtype = "int8", shape = (15, 11, 14))#candidate|1028|(15, 11, 14)|var|int8
var_1029 = relay.var("var_1029", dtype = "int8", shape = (15, 11, 14))#candidate|1029|(15, 11, 14)|var|int8
call_1027 = func_1026_call(var_1028,var_1029,)
output = call_1027
func_1030 = relay.Function([var_1028,var_1029,], output)
mutated_mod['func_1030'] = func_1030
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1087 = relay.var("var_1087", dtype = "int8", shape = (14, 5, 1))#candidate|1087|(14, 5, 1)|var|int8
var_1088 = relay.var("var_1088", dtype = "int8", shape = (14, 5, 6))#candidate|1088|(14, 5, 6)|var|int8
bop_1089 = relay.right_shift(var_1087.astype('int8'), var_1088.astype('int8')) # shape=(14, 5, 6)
func_31_call = mod.get_global_var('func_31')
func_34_call = mutated_mod.get_global_var('func_34')
var_1096 = relay.var("var_1096", dtype = "uint8", shape = (40,))#candidate|1096|(40,)|var|uint8
call_1095 = relay.TupleGetItem(func_31_call(relay.reshape(var_1096.astype('uint8'), [5, 4, 2]), relay.reshape(var_1096.astype('uint8'), [5, 4, 2]), ), 0)
call_1097 = relay.TupleGetItem(func_34_call(relay.reshape(var_1096.astype('uint8'), [5, 4, 2]), relay.reshape(var_1096.astype('uint8'), [5, 4, 2]), ), 0)
uop_1109 = relay.atanh(var_1088.astype('float32')) # shape=(14, 5, 6)
output = relay.Tuple([bop_1089,call_1095,var_1096,uop_1109,])
output2 = relay.Tuple([bop_1089,call_1097,var_1096,uop_1109,])
func_1111 = relay.Function([var_1087,var_1088,var_1096,], output)
mod['func_1111'] = func_1111
mod = relay.transform.InferType()(mod)
mutated_mod['func_1111'] = func_1111
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1111_call = mutated_mod.get_global_var('func_1111')
var_1113 = relay.var("var_1113", dtype = "int8", shape = (14, 5, 1))#candidate|1113|(14, 5, 1)|var|int8
var_1114 = relay.var("var_1114", dtype = "int8", shape = (14, 5, 6))#candidate|1114|(14, 5, 6)|var|int8
var_1115 = relay.var("var_1115", dtype = "uint8", shape = (40,))#candidate|1115|(40,)|var|uint8
call_1112 = func_1111_call(var_1113,var_1114,var_1115,)
output = call_1112
func_1116 = relay.Function([var_1113,var_1114,var_1115,], output)
mutated_mod['func_1116'] = func_1116
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1230 = relay.var("var_1230", dtype = "float64", shape = (7, 5, 9))#candidate|1230|(7, 5, 9)|var|float64
uop_1231 = relay.cos(var_1230.astype('float64')) # shape=(7, 5, 9)
output = relay.Tuple([uop_1231,])
output2 = relay.Tuple([uop_1231,])
func_1237 = relay.Function([var_1230,], output)
mod['func_1237'] = func_1237
mod = relay.transform.InferType()(mod)
var_1238 = relay.var("var_1238", dtype = "float64", shape = (7, 5, 9))#candidate|1238|(7, 5, 9)|var|float64
output = func_1237(var_1238)
func_1239 = relay.Function([var_1238], output)
mutated_mod['func_1239'] = func_1239
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1438 = relay.const([[[1.848774,-6.558767],[4.277135,5.499895],[-7.628797,3.492999],[-0.132768,-1.988751],[-7.877167,-4.192081],[3.201521,-7.840967],[-7.201225,0.025729],[-8.799664,-1.138436],[-9.967973,0.267030],[-4.225759,-9.142157],[3.602580,-1.578084],[-6.710511,6.831419],[-8.034986,-7.751861],[7.160843,3.208632]],[[1.607660,-3.320606],[-8.079648,-2.291483],[1.129235,-5.317601],[-0.166692,-4.077240],[2.152418,-0.738441],[9.034418,-2.999056],[4.813275,9.719804],[3.398591,-9.867604],[2.560410,-9.615142],[1.261862,-3.276936],[-4.866538,-6.004046],[-9.079446,4.008008],[-6.480400,3.993888],[4.163915,7.384961]],[[-4.336380,4.136986],[-4.879183,5.289077],[-2.434798,1.711528],[-6.939862,-6.378065],[-8.712936,6.285530],[6.607012,-3.554333],[-0.271764,5.677100],[0.754383,9.154882],[6.765991,7.062420],[-8.171527,-3.942649],[-4.348306,8.505189],[2.681471,-2.796599],[-8.993370,-5.132659],[-2.773827,3.676276]],[[-6.215796,-9.006867],[-4.953422,-4.176798],[3.624166,5.301462],[-8.039545,-5.205792],[1.375787,1.069807],[-5.517040,-7.135440],[4.611456,-0.013865],[-7.994030,0.371372],[4.154368,-2.912684],[8.386450,3.811331],[8.424617,-3.153468],[-8.710271,-8.544609],[-3.176767,7.019135],[7.528202,-6.071326]],[[-6.766703,-5.171277],[-3.820004,-3.946145],[-5.023157,4.024991],[8.596663,-2.279216],[4.150623,-0.371426],[1.258586,8.631248],[-9.274116,-6.845595],[7.029137,-7.200897],[-4.529188,-7.256014],[-9.099154,-1.143033],[1.915341,-3.481802],[-1.739303,4.353287],[-5.457185,-7.138743],[7.407046,3.925571]],[[-5.861412,7.100292],[-1.002152,4.691403],[1.486161,-9.006110],[-4.605004,-2.230728],[-7.610292,-0.764935],[6.984254,2.908785],[5.035180,4.131250],[3.273179,-0.117460],[9.329935,4.811223],[-5.629600,-8.527958],[-1.461233,8.729788],[2.405790,6.616408],[0.913246,-1.251977],[1.374422,-3.814748]],[[3.818727,9.108568],[-8.592363,-5.217974],[-5.698434,-2.634581],[8.207320,-8.613187],[7.910106,-0.013261],[4.133996,-3.888350],[-9.222393,3.235842],[-7.928758,-1.184977],[5.632071,8.904211],[-8.162577,3.286683],[5.048376,5.243617],[-7.029602,6.874760],[1.986126,-2.190477],[9.507374,2.966276]],[[-3.320012,0.699875],[-6.328099,-0.250254],[-6.907264,-7.107962],[-4.544755,0.374645],[3.539238,-9.977472],[-6.704287,1.539341],[0.734704,-4.584262],[-8.422179,-3.281118],[-5.110568,-6.381909],[-7.759973,-3.794611],[-0.865895,3.401995],[5.248692,-6.133263],[5.471586,-6.727808],[-7.115060,6.609217]]], dtype = "float64")#candidate|1438|(8, 14, 2)|const|float64
uop_1439 = relay.asinh(const_1438.astype('float64')) # shape=(8, 14, 2)
bop_1454 = relay.multiply(const_1438.astype('int8'), relay.reshape(uop_1439.astype('int8'), relay.shape_of(const_1438))) # shape=(8, 14, 2)
output = bop_1454
output2 = bop_1454
func_1462 = relay.Function([], output)
mod['func_1462'] = func_1462
mod = relay.transform.InferType()(mod)
output = func_1462()
func_1463 = relay.Function([], output)
mutated_mod['func_1463'] = func_1463
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1462_call = mod.get_global_var('func_1462')
func_1463_call = mutated_mod.get_global_var('func_1463')
call_1501 = func_1462_call()
call_1502 = func_1462_call()
const_1508 = relay.const([[[-10,5],[4,8],[8,6],[-7,10],[-7,-8],[-5,-4],[-2,8],[7,7],[10,-9],[-9,8],[-10,-7],[9,8],[-6,-4],[7,-9]],[[4,8],[-3,-1],[1,9],[9,-5],[-4,-6],[2,10],[4,-10],[3,2],[7,9],[5,6],[3,5],[-5,-1],[-7,-3],[-4,-8]],[[6,-1],[-7,6],[-3,5],[6,5],[7,3],[2,-2],[-2,-7],[-7,-7],[1,3],[3,2],[-4,-7],[8,-2],[-1,10],[9,-2]],[[6,-9],[4,-7],[-6,-3],[-8,6],[-3,4],[4,-10],[-3,10],[-10,-2],[4,1],[-7,-3],[7,-3],[-2,-8],[-1,-8],[-10,-2]],[[7,-4],[-6,5],[-10,-6],[-3,2],[-6,8],[4,-4],[-8,-10],[1,1],[5,8],[4,1],[-10,-10],[7,-6],[5,-2],[-7,3]],[[-9,6],[-6,1],[-6,3],[2,1],[3,4],[3,5],[-1,-8],[3,8],[6,-3],[2,-4],[-1,-8],[10,-5],[-1,5],[9,4]],[[4,2],[5,9],[-3,6],[6,-6],[8,10],[-3,3],[5,10],[7,-6],[7,-8],[8,-8],[10,8],[3,-5],[-10,-10],[-1,9]],[[-10,-10],[4,-8],[5,-5],[-5,-4],[6,-3],[10,1],[4,-10],[-4,-8],[7,-3],[-3,-2],[-9,1],[-10,3],[1,-5],[3,-8]]], dtype = "int8")#candidate|1508|(8, 14, 2)|const|int8
bop_1509 = relay.bitwise_and(call_1501.astype('int16'), relay.reshape(const_1508.astype('int16'), relay.shape_of(call_1501))) # shape=(8, 14, 2)
bop_1512 = relay.bitwise_and(call_1502.astype('int16'), relay.reshape(const_1508.astype('int16'), relay.shape_of(call_1502))) # shape=(8, 14, 2)
func_504_call = mod.get_global_var('func_504')
func_509_call = mutated_mod.get_global_var('func_509')
const_1521 = relay.const(9, dtype = "int64")#candidate|1521|()|const|int64
var_1522 = relay.var("var_1522", dtype = "int64", shape = (270,))#candidate|1522|(270,)|var|int64
const_1523 = relay.const([-8.147379,0.431428,-1.652108,2.161084,1.360574,-0.886777,-3.180505,-2.327294,0.659991,-3.226033,-6.276451,2.231139,-1.544975,-8.479150,-5.661022,5.613799,-9.435915,9.531777,-4.305912,-1.197400,4.730669,4.591873,-2.695963,1.727352,7.975222,-9.105948,4.009533,-5.333503,4.546931,-2.404598,8.673818,-6.411498,-9.336532,-6.606033,-1.391439,-0.932197,6.231805,-2.441025,6.793253,-1.810923,7.658806,-6.719671,-2.277791,2.799056,-3.664221,5.895074,0.687606,3.193375,1.071997,-2.031922,-1.830217,-5.643242], dtype = "float64")#candidate|1523|(52,)|const|float64
var_1524 = relay.var("var_1524", dtype = "uint8", shape = (40,))#candidate|1524|(40,)|var|uint8
call_1520 = relay.TupleGetItem(func_504_call(relay.reshape(const_1521.astype('int64'), []), relay.reshape(var_1522.astype('int64'), [15, 9, 2]), relay.reshape(const_1523.astype('float64'), [52,]), relay.reshape(var_1524.astype('uint8'), [40,]), ), 2)
call_1525 = relay.TupleGetItem(func_509_call(relay.reshape(const_1521.astype('int64'), []), relay.reshape(var_1522.astype('int64'), [15, 9, 2]), relay.reshape(const_1523.astype('float64'), [52,]), relay.reshape(var_1524.astype('uint8'), [40,]), ), 2)
var_1527 = relay.var("var_1527", dtype = "bool", shape = (2, 2, 13))#candidate|1527|(2, 2, 13)|var|bool
bop_1528 = relay.logical_and(call_1520.astype('bool'), relay.reshape(var_1527.astype('bool'), relay.shape_of(call_1520))) # shape=(2, 2, 13)
bop_1531 = relay.logical_and(call_1525.astype('bool'), relay.reshape(var_1527.astype('bool'), relay.shape_of(call_1525))) # shape=(2, 2, 13)
output = relay.Tuple([bop_1509,const_1521,var_1522,const_1523,var_1524,bop_1528,])
output2 = relay.Tuple([bop_1512,const_1521,var_1522,const_1523,var_1524,bop_1531,])
func_1535 = relay.Function([var_1522,var_1524,var_1527,], output)
mod['func_1535'] = func_1535
mod = relay.transform.InferType()(mod)
var_1536 = relay.var("var_1536", dtype = "int64", shape = (270,))#candidate|1536|(270,)|var|int64
var_1537 = relay.var("var_1537", dtype = "uint8", shape = (40,))#candidate|1537|(40,)|var|uint8
var_1538 = relay.var("var_1538", dtype = "bool", shape = (2, 2, 13))#candidate|1538|(2, 2, 13)|var|bool
output = func_1535(var_1536,var_1537,var_1538,)
func_1539 = relay.Function([var_1536,var_1537,var_1538,], output)
mutated_mod['func_1539'] = func_1539
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1462_call = mod.get_global_var('func_1462')
func_1463_call = mutated_mod.get_global_var('func_1463')
call_1557 = func_1462_call()
call_1558 = func_1462_call()
output = relay.Tuple([call_1557,])
output2 = relay.Tuple([call_1558,])
func_1559 = relay.Function([], output)
mod['func_1559'] = func_1559
mod = relay.transform.InferType()(mod)
mutated_mod['func_1559'] = func_1559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1559_call = mutated_mod.get_global_var('func_1559')
call_1560 = func_1559_call()
output = call_1560
func_1561 = relay.Function([], output)
mutated_mod['func_1561'] = func_1561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1462_call = mod.get_global_var('func_1462')
func_1463_call = mutated_mod.get_global_var('func_1463')
call_1593 = func_1462_call()
call_1594 = func_1462_call()
func_1535_call = mod.get_global_var('func_1535')
func_1539_call = mutated_mod.get_global_var('func_1539')
const_1608 = relay.const([-9,4,-10,9,-8,-5,-2,-7,-2,4,-6,-5,10,-9,1,-9,-4,-8,-5,-4,-9,-5,-5,-3,-1,-7,9,-1,5,-7,2,5,-8,10,1,6,2,10,-4,-6,-1,1,-7,8,-4,8,-1,-4,7,2,-8,7,-2,1,9,8,-4,-1,-3,5,-6,-3,-8,-7,1,-3,10,10,7,7,-1,-6,-5,-6,-6,4,-5,-10,-4,-6,-8,5,-8,-9,8,-1,-2,6,3,-4,4,-2,8,10,7,-8,-6,3,8,3,10,7,-2,-7,-6,6,2,-8,10,-2,-5,-3,3,-9,10,9,5,-3,-10,3,-3,7,-7,-6,3,5,10,3,4,6,-3,5,4,6,-8,1,8,-9,-1,3,6,-3,5,-10,7,4,-5,-9,-9,-3,6,10,-2,-10,-5,8,-2,-8,9,6,7,8,-1,9,4,6,-7,-3,-5,-3,-7,-4,6,-5,-1,2,3,8,-9,-1,-10,-4,-3,-8,-1,1,-4,8,-6,-4,8,-4,6,-4,-10,9,-1,-9,-9,3,9,-9,-10,2,1,-2,4,9,-10,6,-7,-2,-7,3,9,7,1,-1,-4,-6,3,-6,-5,-8,8,-7,-8,-3,1,4,-3,7,8,4,3,8,9,-2,9,-1,3,-3,-8,-9,-4,6,3,-1,1,2,7,-9,-4,-1,2,-1,2,7,10,-7,-8,-4,-6,3,-2,1,-7,-4,-5,5], dtype = "int64")#candidate|1608|(270,)|const|int64
var_1609 = relay.var("var_1609", dtype = "uint8", shape = (40,))#candidate|1609|(40,)|var|uint8
var_1610 = relay.var("var_1610", dtype = "bool", shape = (52,))#candidate|1610|(52,)|var|bool
call_1607 = relay.TupleGetItem(func_1535_call(relay.reshape(const_1608.astype('int64'), [270,]), relay.reshape(var_1609.astype('uint8'), [40,]), relay.reshape(var_1610.astype('bool'), [2, 2, 13]), ), 0)
call_1611 = relay.TupleGetItem(func_1539_call(relay.reshape(const_1608.astype('int64'), [270,]), relay.reshape(var_1609.astype('uint8'), [40,]), relay.reshape(var_1610.astype('bool'), [2, 2, 13]), ), 0)
func_1535_call = mod.get_global_var('func_1535')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_1614 = relay.TupleGetItem(func_1535_call(relay.reshape(const_1608.astype('int64'), [270,]), relay.reshape(var_1609.astype('uint8'), [40,]), relay.reshape(var_1610.astype('bool'), [2, 2, 13]), ), 4)
call_1615 = relay.TupleGetItem(func_1539_call(relay.reshape(const_1608.astype('int64'), [270,]), relay.reshape(var_1609.astype('uint8'), [40,]), relay.reshape(var_1610.astype('bool'), [2, 2, 13]), ), 4)
const_1630 = relay.const([False,True,True,True,True,True,True,True,True,False,True,True,False,False,True,False,False,False,False,False,True,False,False,True,False,True,False,False,False,False,True,True,False,False,False,True,True,True,False,False,True,True,True,False,True,False,False,True,True,True,False,False], dtype = "bool")#candidate|1630|(52,)|const|bool
bop_1631 = relay.divide(var_1610.astype('float64'), relay.reshape(const_1630.astype('float64'), relay.shape_of(var_1610))) # shape=(52,)
output = relay.Tuple([call_1593,call_1607,const_1608,var_1609,call_1614,bop_1631,])
output2 = relay.Tuple([call_1594,call_1611,const_1608,var_1609,call_1615,bop_1631,])
func_1653 = relay.Function([var_1609,var_1610,], output)
mod['func_1653'] = func_1653
mod = relay.transform.InferType()(mod)
mutated_mod['func_1653'] = func_1653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1653_call = mutated_mod.get_global_var('func_1653')
var_1655 = relay.var("var_1655", dtype = "uint8", shape = (40,))#candidate|1655|(40,)|var|uint8
var_1656 = relay.var("var_1656", dtype = "bool", shape = (52,))#candidate|1656|(52,)|var|bool
call_1654 = func_1653_call(var_1655,var_1656,)
output = call_1654
func_1657 = relay.Function([var_1655,var_1656,], output)
mutated_mod['func_1657'] = func_1657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1462_call = mod.get_global_var('func_1462')
func_1463_call = mutated_mod.get_global_var('func_1463')
call_1704 = func_1462_call()
call_1705 = func_1462_call()
var_1711 = relay.var("var_1711", dtype = "int8", shape = (8, 14, 2))#candidate|1711|(8, 14, 2)|var|int8
bop_1712 = relay.not_equal(call_1704.astype('bool'), relay.reshape(var_1711.astype('bool'), relay.shape_of(call_1704))) # shape=(8, 14, 2)
bop_1715 = relay.not_equal(call_1705.astype('bool'), relay.reshape(var_1711.astype('bool'), relay.shape_of(call_1705))) # shape=(8, 14, 2)
output = relay.Tuple([bop_1712,])
output2 = relay.Tuple([bop_1715,])
func_1720 = relay.Function([var_1711,], output)
mod['func_1720'] = func_1720
mod = relay.transform.InferType()(mod)
var_1721 = relay.var("var_1721", dtype = "int8", shape = (8, 14, 2))#candidate|1721|(8, 14, 2)|var|int8
output = func_1720(var_1721)
func_1722 = relay.Function([var_1721], output)
mutated_mod['func_1722'] = func_1722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1559_call = mod.get_global_var('func_1559')
func_1561_call = mutated_mod.get_global_var('func_1561')
call_1815 = relay.TupleGetItem(func_1559_call(), 0)
call_1816 = relay.TupleGetItem(func_1561_call(), 0)
func_31_call = mod.get_global_var('func_31')
func_34_call = mutated_mod.get_global_var('func_34')
var_1818 = relay.var("var_1818", dtype = "uint8", shape = (40,))#candidate|1818|(40,)|var|uint8
call_1817 = relay.TupleGetItem(func_31_call(relay.reshape(var_1818.astype('uint8'), [5, 4, 2]), relay.reshape(var_1818.astype('uint8'), [5, 4, 2]), ), 0)
call_1819 = relay.TupleGetItem(func_34_call(relay.reshape(var_1818.astype('uint8'), [5, 4, 2]), relay.reshape(var_1818.astype('uint8'), [5, 4, 2]), ), 0)
var_1826 = relay.var("var_1826", dtype = "int8", shape = (8, 14, 2))#candidate|1826|(8, 14, 2)|var|int8
bop_1827 = relay.left_shift(call_1815.astype('int64'), relay.reshape(var_1826.astype('int64'), relay.shape_of(call_1815))) # shape=(8, 14, 2)
bop_1830 = relay.left_shift(call_1816.astype('int64'), relay.reshape(var_1826.astype('int64'), relay.shape_of(call_1816))) # shape=(8, 14, 2)
const_1867 = relay.const([[[10,-9],[1,-3],[2,-8],[-10,3],[-4,8],[4,7],[1,-9],[-7,-3],[10,-3],[1,-7],[2,1],[-6,4],[3,-10],[-1,4]],[[-9,1],[8,3],[5,1],[4,2],[-5,-9],[-9,3],[-8,-8],[9,3],[7,-6],[-7,2],[-6,1],[-3,7],[-5,-1],[3,6]],[[-8,-10],[-6,-7],[-8,-7],[1,-8],[-4,-1],[1,-5],[6,3],[-1,-1],[-5,5],[6,4],[4,-9],[-3,-4],[-6,-4],[-2,-3]],[[4,-8],[-9,3],[9,-5],[2,9],[3,3],[-4,2],[1,-7],[4,3],[-10,-2],[-1,-2],[5,-7],[9,4],[-5,7],[-3,1]],[[5,-9],[10,9],[-3,8],[6,-6],[7,9],[-1,-5],[8,-8],[-3,5],[7,-8],[-3,6],[6,4],[1,-4],[-5,-4],[5,-3]],[[-3,2],[-7,3],[10,-10],[8,1],[-9,-7],[-4,1],[-5,-6],[-6,1],[-9,7],[-1,-2],[4,6],[-10,-6],[-3,-1],[6,-8]],[[7,-1],[-4,-6],[9,-1],[-6,3],[-6,1],[-5,5],[10,7],[-8,-6],[9,-9],[2,-6],[-1,-1],[-1,-6],[-3,-3],[4,8]],[[-3,-1],[-8,-5],[-6,9],[-2,-9],[3,1],[-6,1],[3,-10],[1,2],[-3,-5],[2,1],[8,8],[-5,4],[-8,-2],[-1,-6]]], dtype = "int64")#candidate|1867|(8, 14, 2)|const|int64
bop_1868 = relay.greater(bop_1827.astype('bool'), relay.reshape(const_1867.astype('bool'), relay.shape_of(bop_1827))) # shape=(8, 14, 2)
bop_1871 = relay.greater(bop_1830.astype('bool'), relay.reshape(const_1867.astype('bool'), relay.shape_of(bop_1830))) # shape=(8, 14, 2)
func_1026_call = mod.get_global_var('func_1026')
func_1030_call = mutated_mod.get_global_var('func_1030')
const_1873 = relay.const([2,-10,10,-9,-4,1,9,-10,3,-8,-2,9,-3,-3,-3,4,4,-4,-8,5,2,-3,-3,-1,-10,-3,-8,-10,7,-9,-2,4,7,-2,3,-6,-5,-3,1,-5,3,-3,10,1,-7,-6,3,6,-1,6,8,-6,-2,-1,3,6,-6,8,-2,-3,-9,-9,2,2,-6,7,4,-8,4,-1,-7,-4,6,1,1,9,5,-2,-3,-2,5,-2,-3,-5,-10,-4,5,-2,-10,-9,8,-10,-5,-2,7,9,5,10,4,5,-6,-2,8,2,-6,-10,-8,-7,-3,3,-5,3,-6,8,-2,3,-3,-9,-9,-3,-1,-9,-5,3,-7,9,9,-4,5,-4,-4,-3,1,1,2,-5,7,3,2,10,-4,-3,-9,9,-8,10,-9,-10,6,8,-5,4,-7,-4,5,-10,2,-2,-10,-6,-6,-2,-1,5,4,-7,6,-9,-8,-4,8,2,9,3,-6,10,9,-5,4,8,-3,7,8,-4,10,9,-6,-7,4,-6,3,10,-8,2,7,2,-9,-1,4,1,-5,-1,1,8,2,-6,2,8,-3,3,-4,-9,-1,-8,-6,-10,-1,-4,3,-8,5,-1,-9,6,1,1,-2,6,1,-10,-7,9,-1,10,4,8,-1,-8,-8,-4,4,4,-8,-3,6,-9,4,-1,-1,-1,-1,8,-10,6,-3,-8,-8,4,3,-8,-1,-4,-4,-1,7,2,1,-2,8,-8,6,7,8,-1,-9,2,3,4,-8,-2,7,3,-8,8,10,-7,3,2,7,2,4,7,-9,-5,-6,-4,-5,-10,9,-8,-5,7,9,9,7,-4,-7,-8,-10,5,-2,-10,3,9,-7,5,2,-9,-3,8,4,-1,-3,-9,-2,10,1,-2,-9,8,-9,-7,5,3,8,10,-5,3,9,-2,4,6,1,10,10,5,3,2,2,7,-1,10,-7,-6,4,-7,10,-4,5,3,5,7,-2,5,-6,-1,-7,-5,-3,3,10,6,5,-3,5,8,-3,-8,-3,6,3,-10,-10,9,7,3,-1,-7,10,-9,-5,-6,1,3,5,7,9,-2,-2,4,-10,9,7,-10,-8,-5,5,1,-5,1,-4,-2,6,3,3,-9,6,4,6,2,4,-6,1,4,10,8,4,8,-1,7,-8,-7,-4,8,7,-3,9,10,5,-6,1,-10,3,4,8,-10,-10,9,-1,6,-6,9,-6,-5,-4,7,-4,-2,-6,-3,-2,9,1,7,-4,2,-2,7,-1,-1,3,2,-5,-6,-5,-5,1,8,-3,-6,8,9,10,-5,10,7,4,-3,-8,-1,-6,-7,-2,3,-9,-4,-8,4,9,-10,-7,-2,-8,3,-4,6,-3,-8,-9,-2,-1,-5,7,6,3,7,-3,-3,6,5,-2,-9,-6,-2,8,-3,-8,8,10,-3,10,-4,-3,-3,5,-8,-1,-2,5,-1,-7,2,5,-3,5,-7,-8,-9,-8,-9,-4,-9,-5,3,-6,3,-1,7,4,-10,-5,-4,-9,-5,7,9,-2,-6,1,7,4,-1,4,2,9,8,8,-9,7,4,-2,7,5,-3,3,-6,-1,-3,-6,-4,6,8,-8,-10,3,-10,1,8,-1,4,2,-2,-6,7,-9,-6,-7,-10,1,9,-6,-10,-8,-4,-3,6,8,-8,4,-6,-8,-9,-5,9,1,-4,9,-5,-6,10,5,3,-4,8,6,-3,6,-1,-3,9,-10,-10,-8,-8,3,-2,-5,-2,7,9,3,10,-5,2,-1,1,-5,10,7,-8,7,-7,-6,-1,10,-6,3,-4,-7,8,9,-9,2,8,9,-8,-7,-9,7,-7,10,-3,9,3,6,-4,-3,-7,-2,4,2,-8,-10,-3,-8,5,-4,-3,6,9,-7,4,5,7,-6,-1,-5,-7,-9,-2,-1,-5,5,-7,3,-10,-8,4,-6,5,2,-2,8,-3,-2,-3,4,-7,5,-8,2,3,-10,5,8,10,9,-8,-1,-3,-6,5,4,8,8,10,-2,9,-1,-10,8,8,1,-4,7,-5,-4,4,2,7,-6,9,-3,-3,-5,-3,4,10,-7,8,-4,8,1,5,-4,5,-3,-1,7,9,9,-6,-3,-8,3,-6,-9,4,-8,5,-3,-3,9,1,10,-7,-3,-1,1,9,-5,10,1,4,-3,3,-3,10,-4,7,10,10,9,10,-1,4,5,-10,8,-8,-4,4,-1,9,-5,7,2,-9,-9,1,-9,5,-8,2,8,-4,-3,10,-3,9,-7,3,4,-10,-2,-2,-7,7,-2,1,9,2,6,-5,-3,8,9,-1,3,5,-2,8,-5,-7,2,-5,-5,-2,-3,3,1,7,-1,4,-10,1,9,-3,2,9,8,-6,3,6,-7,1,8,-10,8,5,5,10,-5,6,3,-5,1,5,-9,1,10,4,2,1,7,6,1,-6,10,-6,-7,-7,-2,4,3,-9,-7,-5,8,7,-1,9,-2,2,7,9,9,-4,-8,6,2,-6,-10,-8,-8,-4,-9,-3,-8,-4,-3,10,-7,-4,-3,-8,-6,5,-7,4,7,4,-3,-10,-2,-5,-7,8,9,1,-4,6,3,-8,4,6,2,-1,7,-5,4,-3,-6,5,2,-7,2,8,5,-6,8,10,9,4,-1,-4,-10,7,9,1,-7,10,2,-7,-4,3,4,-3,-7,1,-7,-4,-4,-4,5,4,2,5,4,10,-6,9,8,-3,10,-4,10,5,-1,9,-2,9,-9,-9,-6,-10,-2,2,-10,5,-10,-8,-7,6,-1,3,10,-9,-6,-1,-5,-5,-9,-7,4,10,10,-6,-10,-4,-9,-4,9,-9,2,-9,10,-6,-3,-1,-4,2,-10,1,-3,3,-4,-5,10,9,-4,1,-4,-7,9,-5,1,-6,-6,-3,4,4,-2,-2,-3,-4,-9,2,-1,2,7,2,-5,-10,-9,-1,-8,-2,4,-3,-5,3,-2,-9,4,-5,-1,10,9,-6,-3,-3,3,-9,7,3,9,-8,-1,-7,10,-9,-1,6,8,-8,8,4,-5,8,5,6,7,8,-2,-4,-7,5,1,7,3,2,7,3,-9,5,-4,9,-8,-9,1,5,6,5,-1,-9,-10,-6,-7,8,-1,3,6,9,10,-6,-3,9,3,7,8,8,8,-2,4,4,-5,-3,8,6,-9,-7,3,2,-1,10,6,7,2,1,-1,3,10,6,-7,-6,-5,9,-10,-4,1,-10,3,-10,-7,1,6,4,10,-3,-4,-3,1,-7,-10,-2,6,-7,9,4,-10,6,10,1,-3,7,5,-6,-10,7,-7,-3,1,4,9,8,6,5,-7,8,-1,7,4,2,10,8,-10,-10,10,5,-3,-9,8,-5,-10,-4,7,-9,-7,-7,-2,-2,-5,-7,8,8,-4,10,-1,-6,-9,2,-2,-7,3,3,10,-2,-10,3,1,-1,6,-7,-8,10,3,-3,4,-5,-7,-4,6,1,-5,5,-6,8,-10,1,-10,-7,-2,10,-2,2,-3,-6,4,-6,2,4,-10,1,9,-1,-10,2,9,-9,8,2,-10,2,-6,3,-10,7,9,-3,8,5,-10,-2,-10,-2,2,10,2,6,-8,5,3,-1,8,9,6,5,-3,-9,-10,1,-4,-6,1,-4,2,-1,9,-7,6,2,4,-1,8,9,-10,-2,1,3,-1,-3,4,7,-7,-2,-2,6,4,2,7,10,2,-4,-9,5,1,10,-3,1,-1,5,-7,-7,10,3,-1,-5,-4,-5,5,10,1,5,8,4,-9,1,1,9,7,9,4,10,4,-10,9,-8,1,-4,7,8,-8,2,-7,1,2,2,3,-5,-1,-7,-6,-1,-6,7,5,-1,-2,-4,-3,-5,-4,-2,-10,5,3,-2,-7,-7,-7,8,8,9,-4,1,10,4,-2,1,5,-5,-10,-7,-9,-9,9,-10,-9,-6,-2,10,-2,5,3,8,-4,6,10,-8,-10,-5,8,-5,-4,10,6,7,-4,-2,10,5,-2,5,-6,3,4,6,-3,9,-10,3,-6,-5,-3,-7,6,-7,5,-4,-9,-1,-3,4,-8,3,-9,5,7,8,-7,-4,-1,5,5,8,-6,-8,6,5,5,1,4,-1,-5,2,-8,-9,9,4,5,9,-1,-10,-7,8,-5,-7,-6,-2,9,-5,10,5,-1,-3,-3,10,9,10,7,9,-8,4,5,4,-2,3,6,3,-9,4,1,5,-3,6,-4,5,1,3,-7,-2,-8,1,2,-9,-10,-4,-8,1,-5,-5,-1,-8,-2,-10,10,6,-6,-9,-10,-9,5,3,2,7,10,6,-2,8,7,-3,-10,4,7,-4,6,-1,-9,-4,-8,-8,-5,-4,1,1,9,-5,-4,-5,-4,1,-2,-1,-7,-2,10,-7,-8,-9,4,7,5,-4,-10,-3,-8,6,-7,3,-4,10,8,-6,-10,-3,9,8,1,7,1,-10,4,-10,-3,-6,-7,10,6,2,-2,-2,7,7,2,-3,-1,3,-7,8,-4,-6,3,-8,3,-6,-5,8,-8,1,-8,-4,-5,6,-8,1,-9,4,-6,-10,2,-6,2,-8,2,10,-4,-10,-9,-1,3,10,-1,-5,-7,-8,10,-8,9,-5,-5,-10,9,-10,-8,-9,4,-2,-6,-4,1,3,-5,6,-7,4,7,-3,-3,9,3,-2,-7,-2,1,-5,-7,8,9,5,-6,-8,-2,-1,3,6,-8,-2,1,10,-9,8,5,-7,9,-10,10,8,-10,-5,-1,-8,-9,7,-6,4,4,-3,-8,-5,2,-4,3,2,-2,-6,-10,-5,-7,-9,-9,-8,6,4,-2,3,-4,4,-8,3,-5,-7,5,4,-4,3,-7,-6,2,1,9,-6,10,10,-8,1,2,-8,8,9,6,-5,4,-10,-3,10,4,7,-8,5,2,9,4,2,-3,5,-2,-2,4,-3,-2,1,9,-1,4,2,2,9,3,9,2,-5,4,3,1,7,10,-9,-5,-7,6,7,3,7,7,3,-10,6,-6,-6,-4,10,10,-5,10,7,1,8,-10,-3,-9,-8,3,-6,2,5,2,2,-3,-10,8,10,1,-5,-1,10,3,2,2,4,-8,4,4,-4,4,3,1,-1,-1,3,-3,5,-1,-3,-3,-10,7,10,9,-10,2,-5,9,7,-10,-4,-3,10,-4,-8,-9,-9,-2,8,5,-4,-3,1,-5,-2,9,8,4,6,9,6,-4,-4,6,-10,4,-9,5,1,-6,-2,10,7,-8,-4,10,-4,-7,-1,-4,3,4,-7,9,8,-10,2,-10,3,-5,4,-7,10,-1,-6,-1,-3,10,-6,7,-6,-4,-6,-9,-2,-8,-10,5,10,10,-10,-4,9,-2,-2,-9,-5,-1,7,2,4,4,-6,3,-6,9,-5,-1,-6,9,10,-8,-1,8,9,-5,-1,-9,1,-10,-7,5,3,-4,8,8,-1,5,-5,10,-2,-9,6,-7,-3,6,-9,2,8,10,9,-4,-6,4,1,-5,7,-5,5,-1,-10,-6,9,-10,4,-3,-9,7,7,7,3,10,-8,-4,6,1,2,6,5,-8,-7,6,-7,1,2,1,-10,5,7,-2,5,-10,3,8,-1,9,-7,-4,-5,10,5,-3,4,4,7,6,-1,1,-2,2,-7,-1,-5,1,-4,-9,4,-3,-2,-2,4,3,4,-9,-4,10,-1,6,-10,8,-9,10,-1,-4,1,-3,3,2,1,4,2,9,-6,1,-3,9,-6,-7,-1,1,6,9,-2,-9,-2,-10,-8,10,-3,2,-10,10,-8,-4,-6,5,10,3,4,-5,-6,3,-2,-8,3,-3,-8,8,9,-9,8,-9,7,-8,-6,7,8,6,2,6,-3,-8,-3,-1,10,-7,3,7,-2,10,10,1,-7,7,-2,-5,-4,-8,-1,9,-8,-2,-6,10,5,-7,-9,-2,-5,6,-2,4,5,-2,10,10,10,10,10,-2,-2,-10,7,-7,-1,-2,5,-10,10,9,-3,-10,10,9,-2,4,9,-4,6,-1,-6,1,-10,6,-2,2,5,-10,-3,-6,7,-10,-6,5,10,8,-10,9,-9,-4,9,8,-9,8,5,-9,-4,3,5,-1,-5,-1,9,6,3,10,-7,4,7,8,-8,8,-5,-1,8,-7,2,-7,8,-10,5,-2,10,-8,10,3,-2,9,10,2,-3,-1,7,-7,-5], dtype = "int8")#candidate|1873|(2310,)|const|int8
call_1872 = relay.TupleGetItem(func_1026_call(relay.reshape(const_1873.astype('int8'), [15, 11, 14]), relay.reshape(const_1873.astype('int8'), [15, 11, 14]), ), 0)
call_1874 = relay.TupleGetItem(func_1030_call(relay.reshape(const_1873.astype('int8'), [15, 11, 14]), relay.reshape(const_1873.astype('int8'), [15, 11, 14]), ), 0)
var_1877 = relay.var("var_1877", dtype = "int64", shape = (8, 14, 2))#candidate|1877|(8, 14, 2)|var|int64
bop_1878 = relay.greater_equal(bop_1827.astype('bool'), relay.reshape(var_1877.astype('bool'), relay.shape_of(bop_1827))) # shape=(8, 14, 2)
bop_1881 = relay.greater_equal(bop_1830.astype('bool'), relay.reshape(var_1877.astype('bool'), relay.shape_of(bop_1830))) # shape=(8, 14, 2)
func_1653_call = mod.get_global_var('func_1653')
func_1657_call = mutated_mod.get_global_var('func_1657')
const_1884 = relay.const([True,True,False,False,False,True,False,True,False,False,False,False,True,False,False,True,False,True,True,False,True,True,False,False,True,True,True,True,False,True,False,False,True,False,False,True,True,False,False,False,True,True,False,False,True,False,True,False,True,False,False,False], dtype = "bool")#candidate|1884|(52,)|const|bool
call_1883 = relay.TupleGetItem(func_1653_call(relay.reshape(call_1817.astype('uint8'), [40,]), relay.reshape(const_1884.astype('bool'), [52,]), ), 4)
call_1885 = relay.TupleGetItem(func_1657_call(relay.reshape(call_1817.astype('uint8'), [40,]), relay.reshape(const_1884.astype('bool'), [52,]), ), 4)
func_1720_call = mod.get_global_var('func_1720')
func_1722_call = mutated_mod.get_global_var('func_1722')
call_1887 = relay.TupleGetItem(func_1720_call(relay.reshape(bop_1878.astype('int8'), [8, 14, 2])), 0)
call_1888 = relay.TupleGetItem(func_1722_call(relay.reshape(bop_1878.astype('int8'), [8, 14, 2])), 0)
output = relay.Tuple([call_1817,var_1818,bop_1868,call_1872,const_1873,bop_1878,call_1883,const_1884,call_1887,])
output2 = relay.Tuple([call_1819,var_1818,bop_1871,call_1874,const_1873,bop_1881,call_1885,const_1884,call_1888,])
func_1889 = relay.Function([var_1818,var_1826,var_1877,], output)
mod['func_1889'] = func_1889
mod = relay.transform.InferType()(mod)
var_1890 = relay.var("var_1890", dtype = "uint8", shape = (40,))#candidate|1890|(40,)|var|uint8
var_1891 = relay.var("var_1891", dtype = "int8", shape = (8, 14, 2))#candidate|1891|(8, 14, 2)|var|int8
var_1892 = relay.var("var_1892", dtype = "int64", shape = (8, 14, 2))#candidate|1892|(8, 14, 2)|var|int64
output = func_1889(var_1890,var_1891,var_1892,)
func_1893 = relay.Function([var_1890,var_1891,var_1892,], output)
mutated_mod['func_1893'] = func_1893
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1906 = relay.var("var_1906", dtype = "uint64", shape = ())#candidate|1906|()|var|uint64
var_1907 = relay.var("var_1907", dtype = "uint64", shape = (13, 5, 2))#candidate|1907|(13, 5, 2)|var|uint64
bop_1908 = relay.greater(var_1906.astype('bool'), var_1907.astype('bool')) # shape=(13, 5, 2)
func_97_call = mod.get_global_var('func_97')
func_100_call = mutated_mod.get_global_var('func_100')
const_1937 = relay.const([0.116758,2.141601,0.628739,2.015599,-3.847626,9.365563,-9.607731,4.798165,5.238805,7.873108,3.595040,-8.804943,5.882338,-5.318390,1.353319,-6.575208,9.674876,8.220245,1.742305,-5.658228,-6.016612,-4.696108,7.797350,6.195911,-9.757046,6.714163,1.512505,-0.110211,-7.881054,0.462561,-9.445527,9.116974,1.740254,-0.997562,2.458873,-5.671643,8.061865,-4.522538,-8.292791,3.094579,-6.039143,-3.964467,-3.189167,-7.414134,-7.366003,-1.294443,0.014238,-8.244067,-5.305147,0.074595,7.105317,4.005617], dtype = "float64")#candidate|1937|(52,)|const|float64
call_1936 = relay.TupleGetItem(func_97_call(relay.reshape(const_1937.astype('float64'), [2, 2, 13]), relay.reshape(const_1937.astype('float64'), [2, 2, 13]), ), 1)
call_1938 = relay.TupleGetItem(func_100_call(relay.reshape(const_1937.astype('float64'), [2, 2, 13]), relay.reshape(const_1937.astype('float64'), [2, 2, 13]), ), 1)
uop_1945 = relay.asin(call_1936.astype('float32')) # shape=(2, 2, 13)
uop_1947 = relay.asin(call_1938.astype('float32')) # shape=(2, 2, 13)
func_97_call = mod.get_global_var('func_97')
func_100_call = mutated_mod.get_global_var('func_100')
call_1951 = relay.TupleGetItem(func_97_call(relay.reshape(const_1937.astype('float64'), [2, 2, 13]), relay.reshape(const_1937.astype('float64'), [2, 2, 13]), ), 1)
call_1952 = relay.TupleGetItem(func_100_call(relay.reshape(const_1937.astype('float64'), [2, 2, 13]), relay.reshape(const_1937.astype('float64'), [2, 2, 13]), ), 1)
var_1953 = relay.var("var_1953", dtype = "float32", shape = (2, 2, 13))#candidate|1953|(2, 2, 13)|var|float32
bop_1954 = relay.add(uop_1945.astype('uint16'), relay.reshape(var_1953.astype('uint16'), relay.shape_of(uop_1945))) # shape=(2, 2, 13)
bop_1957 = relay.add(uop_1947.astype('uint16'), relay.reshape(var_1953.astype('uint16'), relay.shape_of(uop_1947))) # shape=(2, 2, 13)
uop_1972 = relay.log2(bop_1954.astype('float64')) # shape=(2, 2, 13)
uop_1974 = relay.log2(bop_1957.astype('float64')) # shape=(2, 2, 13)
func_1653_call = mod.get_global_var('func_1653')
func_1657_call = mutated_mod.get_global_var('func_1657')
var_1979 = relay.var("var_1979", dtype = "uint8", shape = (40,))#candidate|1979|(40,)|var|uint8
call_1978 = relay.TupleGetItem(func_1653_call(relay.reshape(var_1979.astype('uint8'), [40,]), relay.reshape(call_1951.astype('bool'), [52,]), ), 5)
call_1980 = relay.TupleGetItem(func_1657_call(relay.reshape(var_1979.astype('uint8'), [40,]), relay.reshape(call_1951.astype('bool'), [52,]), ), 5)
func_1462_call = mod.get_global_var('func_1462')
func_1463_call = mutated_mod.get_global_var('func_1463')
call_1998 = func_1462_call()
call_1999 = func_1462_call()
uop_2000 = relay.acos(uop_1972.astype('float32')) # shape=(2, 2, 13)
uop_2002 = relay.acos(uop_1974.astype('float32')) # shape=(2, 2, 13)
func_1653_call = mod.get_global_var('func_1653')
func_1657_call = mutated_mod.get_global_var('func_1657')
call_2012 = relay.TupleGetItem(func_1653_call(relay.reshape(var_1979.astype('uint8'), [40,]), relay.reshape(call_1978.astype('bool'), [52,]), ), 2)
call_2013 = relay.TupleGetItem(func_1657_call(relay.reshape(var_1979.astype('uint8'), [40,]), relay.reshape(call_1978.astype('bool'), [52,]), ), 2)
output = relay.Tuple([bop_1908,const_1937,call_1951,call_1978,var_1979,call_1998,uop_2000,call_2012,])
output2 = relay.Tuple([bop_1908,const_1937,call_1952,call_1980,var_1979,call_1999,uop_2002,call_2013,])
func_2022 = relay.Function([var_1906,var_1907,var_1953,var_1979,], output)
mod['func_2022'] = func_2022
mod = relay.transform.InferType()(mod)
mutated_mod['func_2022'] = func_2022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2022_call = mutated_mod.get_global_var('func_2022')
var_2024 = relay.var("var_2024", dtype = "uint64", shape = ())#candidate|2024|()|var|uint64
var_2025 = relay.var("var_2025", dtype = "uint64", shape = (13, 5, 2))#candidate|2025|(13, 5, 2)|var|uint64
var_2026 = relay.var("var_2026", dtype = "float32", shape = (2, 2, 13))#candidate|2026|(2, 2, 13)|var|float32
var_2027 = relay.var("var_2027", dtype = "uint8", shape = (40,))#candidate|2027|(40,)|var|uint8
call_2023 = func_2022_call(var_2024,var_2025,var_2026,var_2027,)
output = call_2023
func_2028 = relay.Function([var_2024,var_2025,var_2026,var_2027,], output)
mutated_mod['func_2028'] = func_2028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1559_call = mod.get_global_var('func_1559')
func_1561_call = mutated_mod.get_global_var('func_1561')
call_2099 = relay.TupleGetItem(func_1559_call(), 0)
call_2100 = relay.TupleGetItem(func_1561_call(), 0)
uop_2104 = relay.cos(call_2099.astype('float32')) # shape=(8, 14, 2)
uop_2106 = relay.cos(call_2100.astype('float32')) # shape=(8, 14, 2)
func_1237_call = mod.get_global_var('func_1237')
func_1239_call = mutated_mod.get_global_var('func_1239')
var_2108 = relay.var("var_2108", dtype = "float64", shape = (315,))#candidate|2108|(315,)|var|float64
call_2107 = relay.TupleGetItem(func_1237_call(relay.reshape(var_2108.astype('float64'), [7, 5, 9])), 0)
call_2109 = relay.TupleGetItem(func_1239_call(relay.reshape(var_2108.astype('float64'), [7, 5, 9])), 0)
func_1237_call = mod.get_global_var('func_1237')
func_1239_call = mutated_mod.get_global_var('func_1239')
call_2115 = relay.TupleGetItem(func_1237_call(relay.reshape(call_2107.astype('float64'), [7, 5, 9])), 0)
call_2116 = relay.TupleGetItem(func_1239_call(relay.reshape(call_2107.astype('float64'), [7, 5, 9])), 0)
func_1720_call = mod.get_global_var('func_1720')
func_1722_call = mutated_mod.get_global_var('func_1722')
call_2135 = relay.TupleGetItem(func_1720_call(relay.reshape(uop_2104.astype('int8'), [8, 14, 2])), 0)
call_2136 = relay.TupleGetItem(func_1722_call(relay.reshape(uop_2104.astype('int8'), [8, 14, 2])), 0)
output = relay.Tuple([uop_2104,call_2107,var_2108,call_2115,call_2135,])
output2 = relay.Tuple([uop_2106,call_2109,var_2108,call_2116,call_2136,])
func_2139 = relay.Function([var_2108,], output)
mod['func_2139'] = func_2139
mod = relay.transform.InferType()(mod)
var_2140 = relay.var("var_2140", dtype = "float64", shape = (315,))#candidate|2140|(315,)|var|float64
output = func_2139(var_2140)
func_2141 = relay.Function([var_2140], output)
mutated_mod['func_2141'] = func_2141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1559_call = mod.get_global_var('func_1559')
func_1561_call = mutated_mod.get_global_var('func_1561')
call_2162 = relay.TupleGetItem(func_1559_call(), 0)
call_2163 = relay.TupleGetItem(func_1561_call(), 0)
output = call_2162
output2 = call_2163
func_2164 = relay.Function([], output)
mod['func_2164'] = func_2164
mod = relay.transform.InferType()(mod)
mutated_mod['func_2164'] = func_2164
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2164_call = mutated_mod.get_global_var('func_2164')
call_2165 = func_2164_call()
output = call_2165
func_2166 = relay.Function([], output)
mutated_mod['func_2166'] = func_2166
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2164_call = mod.get_global_var('func_2164')
func_2166_call = mutated_mod.get_global_var('func_2166')
call_2170 = func_2164_call()
call_2171 = func_2164_call()
output = call_2170
output2 = call_2171
func_2173 = relay.Function([], output)
mod['func_2173'] = func_2173
mod = relay.transform.InferType()(mod)
mutated_mod['func_2173'] = func_2173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2173_call = mutated_mod.get_global_var('func_2173')
call_2174 = func_2173_call()
output = call_2174
func_2175 = relay.Function([], output)
mutated_mod['func_2175'] = func_2175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2173_call = mod.get_global_var('func_2173')
func_2175_call = mutated_mod.get_global_var('func_2175')
call_2237 = func_2173_call()
call_2238 = func_2173_call()
output = relay.Tuple([call_2237,])
output2 = relay.Tuple([call_2238,])
func_2257 = relay.Function([], output)
mod['func_2257'] = func_2257
mod = relay.transform.InferType()(mod)
output = func_2257()
func_2258 = relay.Function([], output)
mutated_mod['func_2258'] = func_2258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1462_call = mod.get_global_var('func_1462')
func_1463_call = mutated_mod.get_global_var('func_1463')
call_2329 = func_1462_call()
call_2330 = func_1462_call()
output = relay.Tuple([call_2329,])
output2 = relay.Tuple([call_2330,])
func_2336 = relay.Function([], output)
mod['func_2336'] = func_2336
mod = relay.transform.InferType()(mod)
mutated_mod['func_2336'] = func_2336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2336_call = mutated_mod.get_global_var('func_2336')
call_2337 = func_2336_call()
output = call_2337
func_2338 = relay.Function([], output)
mutated_mod['func_2338'] = func_2338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2336_call = mod.get_global_var('func_2336')
func_2338_call = mutated_mod.get_global_var('func_2338')
call_2365 = relay.TupleGetItem(func_2336_call(), 0)
call_2366 = relay.TupleGetItem(func_2338_call(), 0)
func_1720_call = mod.get_global_var('func_1720')
func_1722_call = mutated_mod.get_global_var('func_1722')
call_2376 = relay.TupleGetItem(func_1720_call(relay.reshape(call_2365.astype('int8'), [8, 14, 2])), 0)
call_2377 = relay.TupleGetItem(func_1722_call(relay.reshape(call_2365.astype('int8'), [8, 14, 2])), 0)
uop_2380 = relay.cosh(call_2376.astype('float32')) # shape=(8, 14, 2)
uop_2382 = relay.cosh(call_2377.astype('float32')) # shape=(8, 14, 2)
bop_2404 = relay.less_equal(call_2376.astype('bool'), relay.reshape(call_2365.astype('bool'), relay.shape_of(call_2376))) # shape=(8, 14, 2)
bop_2407 = relay.less_equal(call_2377.astype('bool'), relay.reshape(call_2366.astype('bool'), relay.shape_of(call_2377))) # shape=(8, 14, 2)
output = relay.Tuple([uop_2380,bop_2404,])
output2 = relay.Tuple([uop_2382,bop_2407,])
func_2421 = relay.Function([], output)
mod['func_2421'] = func_2421
mod = relay.transform.InferType()(mod)
output = func_2421()
func_2422 = relay.Function([], output)
mutated_mod['func_2422'] = func_2422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2336_call = mod.get_global_var('func_2336')
func_2338_call = mutated_mod.get_global_var('func_2338')
call_2441 = relay.TupleGetItem(func_2336_call(), 0)
call_2442 = relay.TupleGetItem(func_2338_call(), 0)
output = call_2441
output2 = call_2442
func_2450 = relay.Function([], output)
mod['func_2450'] = func_2450
mod = relay.transform.InferType()(mod)
output = func_2450()
func_2451 = relay.Function([], output)
mutated_mod['func_2451'] = func_2451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2336_call = mod.get_global_var('func_2336')
func_2338_call = mutated_mod.get_global_var('func_2338')
call_2462 = relay.TupleGetItem(func_2336_call(), 0)
call_2463 = relay.TupleGetItem(func_2338_call(), 0)
output = call_2462
output2 = call_2463
func_2464 = relay.Function([], output)
mod['func_2464'] = func_2464
mod = relay.transform.InferType()(mod)
output = func_2464()
func_2465 = relay.Function([], output)
mutated_mod['func_2465'] = func_2465
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2464_call = mod.get_global_var('func_2464')
func_2465_call = mutated_mod.get_global_var('func_2465')
call_2475 = func_2464_call()
call_2476 = func_2464_call()
uop_2498 = relay.sqrt(call_2475.astype('float64')) # shape=(8, 14, 2)
uop_2500 = relay.sqrt(call_2476.astype('float64')) # shape=(8, 14, 2)
func_1237_call = mod.get_global_var('func_1237')
func_1239_call = mutated_mod.get_global_var('func_1239')
const_2504 = relay.const([-9.117774,-5.629123,7.400951,5.887105,-9.367133,0.504996,-0.594834,1.151261,0.674440,-5.115355,-3.314521,-2.376072,-7.116879,9.261072,7.930619,4.876988,-7.486871,1.350117,-6.287786,-6.816957,6.947066,-1.047903,9.640331,3.212408,-4.713656,-3.092166,-4.163176,-2.242351,0.740086,5.834552,7.634770,-1.729626,-5.581654,1.614876,5.880473,3.892415,-1.266923,-6.332411,4.704646,-5.527433,2.246463,-1.790451,6.002644,-4.608731,-8.876834,6.721399,-8.018974,3.860717,9.567684,6.296047,-7.990383,5.047780,-7.809962,1.011727,-6.162343,1.061575,-7.047111,6.140156,7.401146,7.851391,0.282791,1.697311,-2.920437,-1.159161,6.750685,-4.925871,-4.898577,-3.578245,0.374364,5.807851,6.094600,0.440393,-0.929056,-7.801105,-1.101614,-1.801375,-2.703358,-5.298181,-4.688139,6.987585,-2.003243,-6.101880,2.423598,-1.767616,-0.435883,-5.937507,-0.907669,6.004713,2.536811,-5.597731,3.633661,6.763623,-1.967481,6.497652,1.740961,0.097004,-1.356222,-2.552679,-8.690722,1.065654,-7.887900,2.135511,2.875065,-4.279175,-1.745547,9.389921,6.734258,5.666802,-8.523341,-7.073379,3.775831,7.976458,0.305684,-1.730586,-4.675106,-1.700976,3.033754,-8.200729,6.317719,7.216109,2.780234,8.754172,-2.514724,2.572388,7.491018,-8.045294,6.858855,4.279683,5.648369,-3.457933,4.527613,4.516580,-6.345969,6.239476,-3.388228,1.033658,6.808332,-7.619605,-5.952312,-2.563940,9.974475,-3.086506,2.664762,-6.436186,1.915549,-1.229057,3.261040,-0.987828,4.432676,8.955751,-6.244987,-1.731496,-7.866345,4.692905,-2.317486,-9.875303,-1.813241,-0.997619,-1.108614,4.315771,0.550278,-8.102434,0.674700,7.734442,5.493488,-7.178406,3.156880,5.987610,7.794203,-4.464867,5.097942,8.374596,-0.241597,3.345107,-1.983190,-8.366678,-3.653349,4.963594,7.600074,2.505678,7.929428,4.664568,-8.473262,-8.047926,8.925027,9.814428,-5.744233,5.264934,-1.181482,9.567046,2.734736,-3.472936,3.731941,2.185947,-6.467619,6.387966,-7.850309,4.741599,9.991582,-8.658830,-3.924245,6.791926,-0.624226,1.069441,0.124358,-7.260355,5.362065,8.751653,-7.659662,0.406558,6.266319,-3.768240,5.008379,-6.760649,-6.569607,-3.334218,-1.592699,4.385268,-1.354508,6.883088,9.037608,-4.903094,-8.576227,1.553056,-4.091451,-5.978597,1.218419,6.526935,-1.558420,-5.602183,-5.662720,1.905023,-0.219853,7.806629,-6.469409,4.321548,-7.836481,-8.630358,0.746540,3.844014,-6.679660,3.925176,8.636706,5.795400,-8.095485,-2.253477,-9.731238,9.428893,-4.671965,0.923299,2.828974,-4.573308,-5.035374,-5.004975,6.073186,3.899309,9.188730,2.152487,4.055005,-7.978279,-7.428145,-9.746174,4.011440,-6.113709,-7.915048,-0.028222,-1.301886,-6.251707,9.061077,-1.208739,-4.735671,-7.492641,-5.867581,-2.799125,-0.932899,0.175918,6.087728,1.745721,8.687270,-5.446075,7.426738,0.446658,-1.441844,-0.255443,-3.211839,-5.042890,-5.827435,1.316652,-5.758346,-2.781191,-6.455934,-3.913697,6.206975,-4.725379,7.265399,3.750314,7.898596,-9.799277,-8.010189,9.781105,8.357804,7.721567,2.161967,-7.012248,8.902541,-4.890371,-4.668274,6.746462,5.686538,-0.654031,2.150087,5.921875,-0.628182,-0.615695,7.029345], dtype = "float64")#candidate|2504|(315,)|const|float64
call_2503 = relay.TupleGetItem(func_1237_call(relay.reshape(const_2504.astype('float64'), [7, 5, 9])), 0)
call_2505 = relay.TupleGetItem(func_1239_call(relay.reshape(const_2504.astype('float64'), [7, 5, 9])), 0)
const_2511 = relay.const([[[3.541799,8.725633],[-1.677312,4.711260],[9.857408,5.348090],[8.293493,-0.440048],[3.768890,3.443145],[5.805919,5.739509],[9.888905,8.995546],[-8.629307,-5.791929],[7.381026,8.561062],[-1.080532,3.720488],[1.094937,-3.752186],[2.273605,-5.454553],[-9.847847,1.245444],[5.088381,9.929869]],[[8.868589,0.279502],[4.309600,9.943112],[3.281176,-5.304092],[-4.800280,-7.438647],[-4.477031,-5.415245],[5.712990,-0.295943],[-5.348496,2.707779],[7.240360,-8.054108],[0.310453,-4.052141],[6.372169,-0.428716],[3.927391,-6.088785],[-4.511505,2.692772],[8.361108,-7.461948],[-2.131017,3.676069]],[[-8.726989,-2.985888],[2.800194,-5.307503],[2.091398,1.559019],[1.166974,0.809407],[-9.483767,-1.645085],[-6.300016,2.959298],[2.338716,-9.359755],[6.965227,-7.132548],[7.938958,6.282354],[3.965169,3.613874],[-1.214198,-8.042020],[-5.018242,-9.788549],[8.505411,2.737651],[-4.332837,-4.369448]],[[4.934046,-2.618702],[-5.775521,-5.624835],[9.347199,-3.101737],[-3.702286,3.507953],[-9.494776,-3.358688],[-0.820074,1.392508],[8.718300,0.232488],[4.669577,3.043600],[8.507195,9.953981],[-0.541694,7.654543],[6.245017,-4.766222],[1.624093,6.070161],[1.959706,8.708372],[-5.403619,-1.525297]],[[5.835910,-3.716518],[0.603728,9.428132],[8.622550,-2.628133],[4.118026,1.156962],[2.644663,-6.069197],[-4.260016,-4.494920],[0.630427,9.928314],[-9.102524,4.459147],[6.398981,-6.833184],[6.024166,5.318446],[8.093667,-6.400347],[5.263340,6.521023],[4.797144,-6.255927],[2.537741,-3.333247]],[[-4.661303,2.000068],[9.227143,-1.302788],[-0.840735,6.328872],[6.369665,-5.019079],[-8.287565,8.208830],[-7.150141,-4.046675],[-5.210358,2.589337],[1.551100,-0.937953],[7.034177,-0.253600],[-0.704326,-8.205348],[0.258489,-8.842626],[-8.058971,6.197330],[6.729407,4.121432],[-5.736674,9.135486]],[[-4.474544,-7.930748],[-8.447607,4.209859],[-5.769776,-8.432225],[-5.615503,0.650134],[-9.345255,-4.314034],[-8.929807,1.006453],[-4.613684,-5.056206],[-3.113870,2.685315],[-4.541103,-2.514626],[-8.995750,1.180214],[7.948212,5.759163],[-0.932749,-6.040567],[-3.882421,5.066311],[-1.470544,-9.126962]],[[4.809962,3.966166],[2.629472,-9.706716],[3.962396,-0.500898],[-2.354967,-1.914824],[-8.771044,-0.553355],[2.407628,1.204648],[5.858526,-8.916276],[-9.002015,0.353292],[1.873523,2.764029],[3.035984,1.076103],[2.421100,3.203286],[3.670318,5.407047],[0.108373,-4.262925],[-9.038640,9.715540]]], dtype = "float64")#candidate|2511|(8, 14, 2)|const|float64
bop_2512 = relay.divide(uop_2498.astype('float64'), relay.reshape(const_2511.astype('float64'), relay.shape_of(uop_2498))) # shape=(8, 14, 2)
bop_2515 = relay.divide(uop_2500.astype('float64'), relay.reshape(const_2511.astype('float64'), relay.shape_of(uop_2500))) # shape=(8, 14, 2)
output = relay.Tuple([call_2503,const_2504,bop_2512,])
output2 = relay.Tuple([call_2505,const_2504,bop_2515,])
func_2525 = relay.Function([], output)
mod['func_2525'] = func_2525
mod = relay.transform.InferType()(mod)
output = func_2525()
func_2526 = relay.Function([], output)
mutated_mod['func_2526'] = func_2526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2173_call = mod.get_global_var('func_2173')
func_2175_call = mutated_mod.get_global_var('func_2175')
call_2531 = func_2173_call()
call_2532 = func_2173_call()
func_2257_call = mod.get_global_var('func_2257')
func_2258_call = mutated_mod.get_global_var('func_2258')
call_2535 = relay.TupleGetItem(func_2257_call(), 0)
call_2536 = relay.TupleGetItem(func_2258_call(), 0)
output = relay.Tuple([call_2531,call_2535,])
output2 = relay.Tuple([call_2532,call_2536,])
func_2537 = relay.Function([], output)
mod['func_2537'] = func_2537
mod = relay.transform.InferType()(mod)
output = func_2537()
func_2538 = relay.Function([], output)
mutated_mod['func_2538'] = func_2538
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2539 = relay.var("var_2539", dtype = "float64", shape = (5, 10, 12))#candidate|2539|(5, 10, 12)|var|float64
uop_2540 = relay.log(var_2539.astype('float64')) # shape=(5, 10, 12)
func_832_call = mod.get_global_var('func_832')
func_835_call = mutated_mod.get_global_var('func_835')
var_2543 = relay.var("var_2543", dtype = "int32", shape = (990,))#candidate|2543|(990,)|var|int32
call_2542 = relay.TupleGetItem(func_832_call(relay.reshape(var_2543.astype('int32'), [15, 6, 11])), 0)
call_2544 = relay.TupleGetItem(func_835_call(relay.reshape(var_2543.astype('int32'), [15, 6, 11])), 0)
output = relay.Tuple([uop_2540,call_2542,var_2543,])
output2 = relay.Tuple([uop_2540,call_2544,var_2543,])
func_2566 = relay.Function([var_2539,var_2543,], output)
mod['func_2566'] = func_2566
mod = relay.transform.InferType()(mod)
var_2567 = relay.var("var_2567", dtype = "float64", shape = (5, 10, 12))#candidate|2567|(5, 10, 12)|var|float64
var_2568 = relay.var("var_2568", dtype = "int32", shape = (990,))#candidate|2568|(990,)|var|int32
output = func_2566(var_2567,var_2568,)
func_2569 = relay.Function([var_2567,var_2568,], output)
mutated_mod['func_2569'] = func_2569
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2537_call = mod.get_global_var('func_2537')
func_2538_call = mutated_mod.get_global_var('func_2538')
call_2574 = relay.TupleGetItem(func_2537_call(), 1)
call_2575 = relay.TupleGetItem(func_2538_call(), 1)
func_1462_call = mod.get_global_var('func_1462')
func_1463_call = mutated_mod.get_global_var('func_1463')
call_2576 = func_1462_call()
call_2577 = func_1462_call()
func_2173_call = mod.get_global_var('func_2173')
func_2175_call = mutated_mod.get_global_var('func_2175')
call_2580 = func_2173_call()
call_2581 = func_2173_call()
output = relay.Tuple([call_2574,call_2576,call_2580,])
output2 = relay.Tuple([call_2575,call_2577,call_2581,])
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
func_2421_call = mod.get_global_var('func_2421')
func_2422_call = mutated_mod.get_global_var('func_2422')
call_2680 = relay.TupleGetItem(func_2421_call(), 0)
call_2681 = relay.TupleGetItem(func_2422_call(), 0)
output = call_2680
output2 = call_2681
func_2682 = relay.Function([], output)
mod['func_2682'] = func_2682
mod = relay.transform.InferType()(mod)
mutated_mod['func_2682'] = func_2682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2682_call = mutated_mod.get_global_var('func_2682')
call_2683 = func_2682_call()
output = call_2683
func_2684 = relay.Function([], output)
mutated_mod['func_2684'] = func_2684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2525_call = mod.get_global_var('func_2525')
func_2526_call = mutated_mod.get_global_var('func_2526')
call_2705 = relay.TupleGetItem(func_2525_call(), 2)
call_2706 = relay.TupleGetItem(func_2526_call(), 2)
uop_2730 = relay.tan(call_2705.astype('float64')) # shape=(8, 14, 2)
uop_2732 = relay.tan(call_2706.astype('float64')) # shape=(8, 14, 2)
func_1653_call = mod.get_global_var('func_1653')
func_1657_call = mutated_mod.get_global_var('func_1657')
var_2736 = relay.var("var_2736", dtype = "uint8", shape = (40,))#candidate|2736|(40,)|var|uint8
var_2737 = relay.var("var_2737", dtype = "bool", shape = (52,))#candidate|2737|(52,)|var|bool
call_2735 = relay.TupleGetItem(func_1653_call(relay.reshape(var_2736.astype('uint8'), [40,]), relay.reshape(var_2737.astype('bool'), [52,]), ), 5)
call_2738 = relay.TupleGetItem(func_1657_call(relay.reshape(var_2736.astype('uint8'), [40,]), relay.reshape(var_2737.astype('bool'), [52,]), ), 5)
bop_2744 = relay.mod(call_2705.astype('float64'), relay.reshape(uop_2730.astype('float64'), relay.shape_of(call_2705))) # shape=(8, 14, 2)
bop_2747 = relay.mod(call_2706.astype('float64'), relay.reshape(uop_2732.astype('float64'), relay.shape_of(call_2706))) # shape=(8, 14, 2)
func_2022_call = mod.get_global_var('func_2022')
func_2028_call = mutated_mod.get_global_var('func_2028')
var_2752 = relay.var("var_2752", dtype = "uint64", shape = ())#candidate|2752|()|var|uint64
var_2753 = relay.var("var_2753", dtype = "uint64", shape = (130,))#candidate|2753|(130,)|var|uint64
call_2751 = relay.TupleGetItem(func_2022_call(relay.reshape(var_2752.astype('uint64'), []), relay.reshape(var_2753.astype('uint64'), [13, 5, 2]), relay.reshape(var_2737.astype('float32'), [2, 2, 13]), relay.reshape(var_2736.astype('uint8'), [40,]), ), 3)
call_2754 = relay.TupleGetItem(func_2028_call(relay.reshape(var_2752.astype('uint64'), []), relay.reshape(var_2753.astype('uint64'), [13, 5, 2]), relay.reshape(var_2737.astype('float32'), [2, 2, 13]), relay.reshape(var_2736.astype('uint8'), [40,]), ), 3)
output = relay.Tuple([call_2735,var_2736,var_2737,bop_2744,call_2751,var_2752,var_2753,])
output2 = relay.Tuple([call_2738,var_2736,var_2737,bop_2747,call_2754,var_2752,var_2753,])
func_2779 = relay.Function([var_2736,var_2737,var_2752,var_2753,], output)
mod['func_2779'] = func_2779
mod = relay.transform.InferType()(mod)
var_2780 = relay.var("var_2780", dtype = "uint8", shape = (40,))#candidate|2780|(40,)|var|uint8
var_2781 = relay.var("var_2781", dtype = "bool", shape = (52,))#candidate|2781|(52,)|var|bool
var_2782 = relay.var("var_2782", dtype = "uint64", shape = ())#candidate|2782|()|var|uint64
var_2783 = relay.var("var_2783", dtype = "uint64", shape = (130,))#candidate|2783|(130,)|var|uint64
output = func_2779(var_2780,var_2781,var_2782,var_2783,)
func_2784 = relay.Function([var_2780,var_2781,var_2782,var_2783,], output)
mutated_mod['func_2784'] = func_2784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2450_call = mod.get_global_var('func_2450')
func_2451_call = mutated_mod.get_global_var('func_2451')
call_2788 = func_2450_call()
call_2789 = func_2450_call()
output = relay.Tuple([call_2788,])
output2 = relay.Tuple([call_2789,])
func_2799 = relay.Function([], output)
mod['func_2799'] = func_2799
mod = relay.transform.InferType()(mod)
mutated_mod['func_2799'] = func_2799
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2799_call = mutated_mod.get_global_var('func_2799')
call_2800 = func_2799_call()
output = call_2800
func_2801 = relay.Function([], output)
mutated_mod['func_2801'] = func_2801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2164_call = mod.get_global_var('func_2164')
func_2166_call = mutated_mod.get_global_var('func_2166')
call_2876 = func_2164_call()
call_2877 = func_2164_call()
output = call_2876
output2 = call_2877
func_2887 = relay.Function([], output)
mod['func_2887'] = func_2887
mod = relay.transform.InferType()(mod)
output = func_2887()
func_2888 = relay.Function([], output)
mutated_mod['func_2888'] = func_2888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2537_call = mod.get_global_var('func_2537')
func_2538_call = mutated_mod.get_global_var('func_2538')
call_2908 = relay.TupleGetItem(func_2537_call(), 0)
call_2909 = relay.TupleGetItem(func_2538_call(), 0)
output = call_2908
output2 = call_2909
func_2943 = relay.Function([], output)
mod['func_2943'] = func_2943
mod = relay.transform.InferType()(mod)
output = func_2943()
func_2944 = relay.Function([], output)
mutated_mod['func_2944'] = func_2944
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2943_call = mod.get_global_var('func_2943')
func_2944_call = mutated_mod.get_global_var('func_2944')
call_2964 = func_2943_call()
call_2965 = func_2943_call()
output = call_2964
output2 = call_2965
func_2984 = relay.Function([], output)
mod['func_2984'] = func_2984
mod = relay.transform.InferType()(mod)
mutated_mod['func_2984'] = func_2984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2984_call = mutated_mod.get_global_var('func_2984')
call_2985 = func_2984_call()
output = call_2985
func_2986 = relay.Function([], output)
mutated_mod['func_2986'] = func_2986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2582_call = mod.get_global_var('func_2582')
func_2584_call = mutated_mod.get_global_var('func_2584')
call_2989 = relay.TupleGetItem(func_2582_call(), 0)
call_2990 = relay.TupleGetItem(func_2584_call(), 0)
func_789_call = mod.get_global_var('func_789')
func_791_call = mutated_mod.get_global_var('func_791')
const_3010 = relay.const([-4.626528,4.959160,3.307318,-5.836642,-9.256212,-9.495524,-9.847182,7.668395,-5.794408,-5.275446,5.444268,-6.360461,4.972916,3.782252,-8.061391,2.420709,-4.801433,-7.267287,-1.748535,-2.202134,-7.774639,0.820091,-0.211403,-1.392458,3.976331,9.555475,-3.988518,1.200824,1.796739,4.221512,-8.376507,-6.962208,8.936895,3.848654,6.715162,6.094332,-4.311532,-5.785318,2.632924,1.905949,-8.055726,5.260498,-1.742511,-6.224860,7.434279,4.495645,-6.739861,-5.294178,0.530736,4.165184,0.003902,-1.527789,-3.637214,-2.766648,3.500311,-7.553274,0.157561,0.010659,-2.788496,9.236026,1.901314,8.225269,-4.354549,9.890796,6.220587,9.834630,7.493290,3.553334,-6.279268,6.582053,2.751404,7.445269,0.241006,0.304839,1.232190,-0.242740,6.811047,-6.984583,1.881522,6.733529,5.716500,-7.348350,-0.380824,-4.024063,7.642337,9.289871,5.395991,0.108970,9.976559,-9.401114,7.636544,4.010341,-7.107913,7.859398,4.621656,6.311724,3.919455,-0.223943,1.875382,-0.555873,-1.975197,2.953344,4.758166,8.288416,0.150854], dtype = "float32")#candidate|3010|(105,)|const|float32
call_3009 = relay.TupleGetItem(func_789_call(relay.reshape(const_3010.astype('float32'), [3, 7, 5])), 0)
call_3011 = relay.TupleGetItem(func_791_call(relay.reshape(const_3010.astype('float32'), [3, 7, 5])), 0)
func_504_call = mod.get_global_var('func_504')
func_509_call = mutated_mod.get_global_var('func_509')
var_3015 = relay.var("var_3015", dtype = "int64", shape = ())#candidate|3015|()|var|int64
const_3016 = relay.const([-2,-5,4,-10,3,-6,-7,8,-3,-4,4,5,-10,6,-5,-4,-10,5,10,-10,1,10,10,-5,-5,-3,-9,-2,5,-4,7,-7,-7,-2,8,-2,7,-9,9,10,-5,10,-3,-4,2,-9,5,5,-8,1,-8,-5,2,-2,9,5,-4,9,-9,6,-2,10,10,-1,2,-4,-2,5,-4,9,8,-9,-10,2,5,1,-2,5,6,-10,-8,9,7,8,-3,-7,10,7,-6,9,6,9,3,-10,1,-7,6,1,-4,-5,3,-7,-7,4,3,3,5,9,-7,7,9,-7,4,8,-4,-2,-2,3,-5,-1,10,2,-7,3,2,-1,6,5,5,-5,-6,-9,9,-6,-7,-7,-2,-2,1,-4,-7,-3,-3,2,-4,7,7,-8,6,-5,2,9,10,-4,1,4,-1,3,-7,-1,4,-3,-6,1,5,-6,-5,-3,-8,-8,5,7,10,1,4,2,-2,1,6,-1,-8,-7,1,10,7,10,-1,-9,6,-2,-3,-10,-9,-4,-5,-5,-9,-5,-4,-4,4,-4,-1,-10,4,1,8,4,-4,-4,1,-3,-4,3,-5,1,-10,-8,2,2,-10,5,6,-5,8,-1,-9,-1,3,2,-2,-9,2,7,-5,-9,-2,3,6,8,7,2,6,-10,-1,8,5,-8,-5,10,4,5,6,3,7,-5,-3,-2,-4,7,-5,9,-4,-7,-9,-1,8,8,5,7], dtype = "int64")#candidate|3016|(270,)|const|int64
const_3017 = relay.const([-8.459145,8.025664,7.472404,-3.365983,-2.218477,-0.980750,1.855227,-4.530447,-3.782184,8.146911,9.021974,-7.277594,3.863868,8.870636,1.536775,6.562892,-7.673107,-7.999337,5.266585,-8.883366,6.554591,-5.790903,-8.238598,0.878935,4.284906,-0.113424,4.177580,4.355373,0.671226,7.035722,-5.338921,-8.691067,9.867261,-1.248454,9.457787,-5.187638,5.019029,8.305078,7.670772,1.136319,4.773659,6.445789,-0.607540,-0.671198,1.193334,0.569939,-7.219575,5.028862,-6.706095,-3.524226,-6.019766,-6.087579], dtype = "float64")#candidate|3017|(52,)|const|float64
var_3018 = relay.var("var_3018", dtype = "uint8", shape = (40,))#candidate|3018|(40,)|var|uint8
call_3014 = relay.TupleGetItem(func_504_call(relay.reshape(var_3015.astype('int64'), []), relay.reshape(const_3016.astype('int64'), [15, 9, 2]), relay.reshape(const_3017.astype('float64'), [52,]), relay.reshape(var_3018.astype('uint8'), [40,]), ), 5)
call_3019 = relay.TupleGetItem(func_509_call(relay.reshape(var_3015.astype('int64'), []), relay.reshape(const_3016.astype('int64'), [15, 9, 2]), relay.reshape(const_3017.astype('float64'), [52,]), relay.reshape(var_3018.astype('uint8'), [40,]), ), 5)
func_2421_call = mod.get_global_var('func_2421')
func_2422_call = mutated_mod.get_global_var('func_2422')
call_3022 = relay.TupleGetItem(func_2421_call(), 0)
call_3023 = relay.TupleGetItem(func_2422_call(), 0)
func_2464_call = mod.get_global_var('func_2464')
func_2465_call = mutated_mod.get_global_var('func_2465')
call_3029 = func_2464_call()
call_3030 = func_2464_call()
output = relay.Tuple([call_2989,call_3009,const_3010,call_3014,var_3015,const_3016,const_3017,var_3018,call_3022,call_3029,])
output2 = relay.Tuple([call_2990,call_3011,const_3010,call_3019,var_3015,const_3016,const_3017,var_3018,call_3023,call_3030,])
func_3040 = relay.Function([var_3015,var_3018,], output)
mod['func_3040'] = func_3040
mod = relay.transform.InferType()(mod)
var_3041 = relay.var("var_3041", dtype = "int64", shape = ())#candidate|3041|()|var|int64
var_3042 = relay.var("var_3042", dtype = "uint8", shape = (40,))#candidate|3042|(40,)|var|uint8
output = func_3040(var_3041,var_3042,)
func_3043 = relay.Function([var_3041,var_3042,], output)
mutated_mod['func_3043'] = func_3043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2164_call = mod.get_global_var('func_2164')
func_2166_call = mutated_mod.get_global_var('func_2166')
call_3069 = func_2164_call()
call_3070 = func_2164_call()
output = call_3069
output2 = call_3070
func_3097 = relay.Function([], output)
mod['func_3097'] = func_3097
mod = relay.transform.InferType()(mod)
mutated_mod['func_3097'] = func_3097
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3097_call = mutated_mod.get_global_var('func_3097')
call_3098 = func_3097_call()
output = call_3098
func_3099 = relay.Function([], output)
mutated_mod['func_3099'] = func_3099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2682_call = mod.get_global_var('func_2682')
func_2684_call = mutated_mod.get_global_var('func_2684')
call_3117 = func_2682_call()
call_3118 = func_2682_call()
func_2464_call = mod.get_global_var('func_2464')
func_2465_call = mutated_mod.get_global_var('func_2465')
call_3119 = func_2464_call()
call_3120 = func_2464_call()
output = relay.Tuple([call_3117,call_3119,])
output2 = relay.Tuple([call_3118,call_3120,])
func_3122 = relay.Function([], output)
mod['func_3122'] = func_3122
mod = relay.transform.InferType()(mod)
output = func_3122()
func_3123 = relay.Function([], output)
mutated_mod['func_3123'] = func_3123
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3150 = relay.const([[[-3.627783,6.265154,4.359876,-5.560000,8.914312,6.452416,2.975187,8.178137,-8.989943,-3.320161,8.847072,-3.021982,-0.738689,-1.040594],[-8.462351,-7.469618,5.121257,-0.002110,1.786027,5.186924,-2.577961,7.377652,0.174498,-2.285872,-0.844119,-7.776709,6.583467,-7.718826],[-0.380144,-3.057238,-8.843055,9.781684,6.397261,-8.009632,7.872258,7.982394,-4.777327,2.425558,-8.553492,7.710567,1.169245,-0.165013]],[[-1.667732,-0.003799,2.585128,-4.864676,8.455726,8.735628,7.743098,-8.685500,8.289887,-0.984026,-9.339173,3.473928,3.393037,5.029630],[3.829409,-0.390440,-2.964576,-3.001106,0.812339,7.638876,2.013636,5.248601,-3.433750,8.870690,-8.715701,1.191852,4.073521,9.665194],[-6.171443,6.878249,-3.473089,5.449721,-8.715842,8.691046,-2.995058,4.184609,6.441633,-2.671607,-9.846990,-6.517542,8.974247,9.882715]],[[-7.329388,-4.468997,4.103573,-8.135432,2.569572,-4.027206,-7.169847,9.964176,-4.322532,-6.370053,-0.500485,1.021968,-7.933531,8.813607],[6.017357,-2.464147,0.585859,-0.015779,9.490460,-0.531680,0.548538,-0.142002,-3.500700,-2.036350,-4.478991,3.577617,-6.856073,7.176009],[-4.098538,-7.804885,7.578213,5.223197,1.708408,3.391200,7.520049,0.817824,-6.372100,-5.738538,-5.249292,2.734276,6.878477,2.518304]],[[5.353623,-1.107794,6.147020,-1.765274,9.626589,7.023131,9.495414,6.295886,-7.079630,1.418311,7.005739,-0.068848,1.328898,-3.048822],[-7.660558,-1.132873,2.225555,3.556181,9.761226,2.234606,5.948059,-2.736112,-1.797836,0.497465,-9.046715,6.132891,-1.533676,4.690027],[-5.124889,-2.220372,2.214363,-3.226087,3.122711,8.883544,5.283849,-3.802743,1.466197,-2.980251,-0.811554,6.093559,-3.202316,-5.205012]],[[-0.474095,-8.920684,-9.010218,0.882661,0.795314,-4.546990,7.751694,-5.386402,-5.277940,8.529190,9.826885,9.849356,-5.235675,-4.352475],[-0.144338,1.377035,3.333363,5.770509,8.159221,1.869431,-7.656229,9.914764,-8.125257,5.975789,-6.057232,-4.864015,-9.305241,-9.805612],[-8.403446,4.495659,2.253291,4.853331,5.967886,-5.737908,8.048014,2.514063,9.268264,6.098107,-1.229658,5.491901,-1.749712,-6.164331]],[[0.069951,1.961151,-5.799546,-6.148269,5.330944,-9.264957,-2.615873,4.948310,-5.378617,-7.937098,-4.219305,7.844850,-7.213097,3.586121],[6.044644,1.412540,-7.564887,-9.165872,8.096872,5.145434,9.287281,4.511310,-6.860749,7.381800,-3.910363,5.886274,-4.199389,9.414802],[6.755899,4.415200,8.354790,1.734531,3.457964,-9.238813,0.027063,2.343377,5.672914,-5.345177,-0.562403,-3.782219,6.270528,5.610144]],[[3.305475,-6.579075,9.410099,6.311841,-7.338879,5.809931,-1.299077,7.661255,6.552842,-8.058447,7.742039,-6.140205,7.147130,-5.375259],[-0.661585,-2.693557,6.274478,-6.356121,-1.476539,1.748349,6.470327,-6.069615,-7.720858,9.509997,-0.013170,-2.436312,-0.961176,1.675283],[0.662117,9.245536,2.777770,7.465654,-2.215032,-0.228186,0.410964,-6.717984,-8.841178,2.524309,-6.661116,-6.681635,-0.164971,-7.598252]],[[9.218297,-9.044374,-3.853260,0.718321,0.491251,-7.966353,-1.169359,-7.567122,-4.564726,-0.183579,9.234047,9.356620,-4.917677,6.741631],[-8.192081,-6.372760,9.203437,-3.489142,-1.131706,-7.297253,9.632449,6.067101,7.398123,9.658776,-6.057065,-0.564723,6.454612,1.487770],[9.306822,5.238147,9.151750,6.901163,-0.723207,-4.186744,8.193217,2.035407,4.916916,8.989000,-6.638950,-8.209727,-2.831808,8.641647]],[[-0.158163,-4.161897,7.545093,5.332805,3.480242,0.508228,-2.714895,-6.574893,-8.754183,-9.345918,-1.842878,-4.892643,3.104680,-5.146200],[0.163919,1.895591,-1.396907,5.888410,9.996000,-0.146793,-7.894554,7.704842,3.006187,-4.217834,9.781278,7.248951,-8.991611,-5.447221],[-7.378927,-3.612614,-7.700584,0.186178,6.494877,-8.352775,6.192165,3.193314,7.750783,1.021862,-8.338139,-7.265334,-6.355753,0.796529]],[[-2.059120,-9.325615,-8.540640,-7.780747,2.627208,-1.753935,7.571571,4.022209,6.235630,-3.440944,6.618485,-8.581679,7.846854,5.157377],[-5.512129,0.919171,1.890153,-8.583402,-5.583808,-8.304038,-1.077023,-8.642493,-6.223091,6.041318,-6.428439,-3.769277,1.497128,0.665295],[2.831798,-4.891502,7.565803,-2.392889,-9.154635,7.666159,-3.614040,-2.812204,-2.056198,-3.850200,-4.785427,-2.212655,5.246349,7.622250]],[[4.092400,5.454044,4.528535,5.623818,6.585500,2.492291,-9.314614,-9.143810,4.602957,0.132344,2.287386,-7.909401,7.832981,-1.511027],[1.643214,3.912937,-4.638780,8.881563,7.942336,2.147214,4.080622,-5.953212,6.180911,-3.827329,8.091110,-1.173002,0.061372,-9.948721],[1.698834,3.234247,-2.248628,-7.167974,1.251983,1.044902,-9.640543,-4.849382,1.780536,4.550586,7.547510,9.766869,1.784510,-1.676988]]], dtype = "float32")#candidate|3150|(11, 3, 14)|const|float32
var_3151 = relay.var("var_3151", dtype = "float32", shape = (11, 3, 14))#candidate|3151|(11, 3, 14)|var|float32
bop_3152 = relay.floor_mod(const_3150.astype('float32'), relay.reshape(var_3151.astype('float32'), relay.shape_of(const_3150))) # shape=(11, 3, 14)
output = bop_3152
output2 = bop_3152
func_3184 = relay.Function([var_3151,], output)
mod['func_3184'] = func_3184
mod = relay.transform.InferType()(mod)
mutated_mod['func_3184'] = func_3184
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3185 = relay.var("var_3185", dtype = "float32", shape = (11, 3, 14))#candidate|3185|(11, 3, 14)|var|float32
func_3184_call = mutated_mod.get_global_var('func_3184')
call_3186 = func_3184_call(var_3185)
output = call_3186
func_3187 = relay.Function([var_3185], output)
mutated_mod['func_3187'] = func_3187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2582_call = mod.get_global_var('func_2582')
func_2584_call = mutated_mod.get_global_var('func_2584')
call_3189 = relay.TupleGetItem(func_2582_call(), 0)
call_3190 = relay.TupleGetItem(func_2584_call(), 0)
uop_3200 = relay.asin(call_3189.astype('float64')) # shape=(8, 14, 2)
uop_3202 = relay.asin(call_3190.astype('float64')) # shape=(8, 14, 2)
uop_3236 = relay.sigmoid(uop_3200.astype('float32')) # shape=(8, 14, 2)
uop_3238 = relay.sigmoid(uop_3202.astype('float32')) # shape=(8, 14, 2)
func_2336_call = mod.get_global_var('func_2336')
func_2338_call = mutated_mod.get_global_var('func_2338')
call_3247 = relay.TupleGetItem(func_2336_call(), 0)
call_3248 = relay.TupleGetItem(func_2338_call(), 0)
func_635_call = mod.get_global_var('func_635')
func_638_call = mutated_mod.get_global_var('func_638')
var_3260 = relay.var("var_3260", dtype = "uint16", shape = (168,))#candidate|3260|(168,)|var|uint16
call_3259 = relay.TupleGetItem(func_635_call(relay.reshape(var_3260.astype('uint16'), [3, 14, 4])), 0)
call_3261 = relay.TupleGetItem(func_638_call(relay.reshape(var_3260.astype('uint16'), [3, 14, 4])), 0)
func_789_call = mod.get_global_var('func_789')
func_791_call = mutated_mod.get_global_var('func_791')
var_3265 = relay.var("var_3265", dtype = "float32", shape = (105,))#candidate|3265|(105,)|var|float32
call_3264 = relay.TupleGetItem(func_789_call(relay.reshape(var_3265.astype('float32'), [3, 7, 5])), 0)
call_3266 = relay.TupleGetItem(func_791_call(relay.reshape(var_3265.astype('float32'), [3, 7, 5])), 0)
uop_3271 = relay.acos(uop_3236.astype('float32')) # shape=(8, 14, 2)
uop_3273 = relay.acos(uop_3238.astype('float32')) # shape=(8, 14, 2)
output = relay.Tuple([call_3247,call_3259,var_3260,call_3264,var_3265,uop_3271,])
output2 = relay.Tuple([call_3248,call_3261,var_3260,call_3266,var_3265,uop_3273,])
func_3274 = relay.Function([var_3260,var_3265,], output)
mod['func_3274'] = func_3274
mod = relay.transform.InferType()(mod)
mutated_mod['func_3274'] = func_3274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3274_call = mutated_mod.get_global_var('func_3274')
var_3276 = relay.var("var_3276", dtype = "uint16", shape = (168,))#candidate|3276|(168,)|var|uint16
var_3277 = relay.var("var_3277", dtype = "float32", shape = (105,))#candidate|3277|(105,)|var|float32
call_3275 = func_3274_call(var_3276,var_3277,)
output = call_3275
func_3278 = relay.Function([var_3276,var_3277,], output)
mutated_mod['func_3278'] = func_3278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2799_call = mod.get_global_var('func_2799')
func_2801_call = mutated_mod.get_global_var('func_2801')
call_3302 = relay.TupleGetItem(func_2799_call(), 0)
call_3303 = relay.TupleGetItem(func_2801_call(), 0)
func_635_call = mod.get_global_var('func_635')
func_638_call = mutated_mod.get_global_var('func_638')
const_3318 = relay.const([[-3,-1],[-3,5],[7,-9],[1,-8],[6,-10],[10,-9],[-2,-9],[-10,-8],[-7,-9],[-7,10],[-8,-9],[-4,-2],[4,-1],[7,-1],[8,-1],[8,-3],[-8,5],[9,-9],[4,-6],[4,-1],[9,3],[1,4],[5,-10],[-5,-7],[-5,8],[8,1],[-3,4],[-4,-8],[-6,10],[6,-7],[-9,5],[9,-7],[-4,8],[-10,6],[7,-5],[-5,-5],[-1,-6],[-1,9],[1,-6],[-5,7],[-7,1],[-6,-5],[7,4],[-10,-10],[-6,-9],[3,-6],[1,5],[4,5],[-6,9],[5,5],[-3,-5],[9,-3],[4,-1],[9,1],[9,5],[-9,3],[1,9],[7,10],[-4,2],[-2,8],[4,-5],[7,2],[-4,-7],[9,2],[5,6],[5,1],[-2,-3],[-7,-10],[-2,-3],[-3,-7],[2,-1],[6,-1],[-5,5],[4,1],[9,10],[-7,-9],[7,10],[-7,-6],[10,1],[1,9],[8,5],[-9,10],[10,-6],[-2,8]], dtype = "uint16")#candidate|3318|(84, 2)|const|uint16
call_3317 = relay.TupleGetItem(func_635_call(relay.reshape(const_3318.astype('uint16'), [3, 14, 4])), 0)
call_3319 = relay.TupleGetItem(func_638_call(relay.reshape(const_3318.astype('uint16'), [3, 14, 4])), 0)
output = relay.Tuple([call_3302,call_3317,const_3318,])
output2 = relay.Tuple([call_3303,call_3319,const_3318,])
func_3333 = relay.Function([], output)
mod['func_3333'] = func_3333
mod = relay.transform.InferType()(mod)
mutated_mod['func_3333'] = func_3333
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3333_call = mutated_mod.get_global_var('func_3333')
call_3334 = func_3333_call()
output = call_3334
func_3335 = relay.Function([], output)
mutated_mod['func_3335'] = func_3335
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2887_call = mod.get_global_var('func_2887')
func_2888_call = mutated_mod.get_global_var('func_2888')
call_3388 = func_2887_call()
call_3389 = func_2887_call()
output = call_3388
output2 = call_3389
func_3396 = relay.Function([], output)
mod['func_3396'] = func_3396
mod = relay.transform.InferType()(mod)
mutated_mod['func_3396'] = func_3396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3396_call = mutated_mod.get_global_var('func_3396')
call_3397 = func_3396_call()
output = call_3397
func_3398 = relay.Function([], output)
mutated_mod['func_3398'] = func_3398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2450_call = mod.get_global_var('func_2450')
func_2451_call = mutated_mod.get_global_var('func_2451')
call_3448 = func_2450_call()
call_3449 = func_2450_call()
output = relay.Tuple([call_3448,])
output2 = relay.Tuple([call_3449,])
func_3463 = relay.Function([], output)
mod['func_3463'] = func_3463
mod = relay.transform.InferType()(mod)
mutated_mod['func_3463'] = func_3463
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3463_call = mutated_mod.get_global_var('func_3463')
call_3464 = func_3463_call()
output = call_3464
func_3465 = relay.Function([], output)
mutated_mod['func_3465'] = func_3465
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3477 = relay.var("var_3477", dtype = "uint32", shape = (13, 14, 1))#candidate|3477|(13, 14, 1)|var|uint32
var_3478 = relay.var("var_3478", dtype = "uint32", shape = (13, 14, 1))#candidate|3478|(13, 14, 1)|var|uint32
bop_3479 = relay.bitwise_and(var_3477.astype('uint32'), relay.reshape(var_3478.astype('uint32'), relay.shape_of(var_3477))) # shape=(13, 14, 1)
var_3482 = relay.var("var_3482", dtype = "uint32", shape = (13, 14, 9))#candidate|3482|(13, 14, 9)|var|uint32
bop_3483 = relay.left_shift(var_3477.astype('uint8'), var_3482.astype('uint8')) # shape=(13, 14, 9)
func_2779_call = mod.get_global_var('func_2779')
func_2784_call = mutated_mod.get_global_var('func_2784')
const_3489 = relay.const([2,-8,7,-6,4,-4,10,9,-10,8,10,9,-9,4,-2,3,-5,10,8,-10,5,-3,4,8,3,-10,-6,-3,-5,-6,-7,4,-8,4,2,8,2,10,-5,1], dtype = "uint8")#candidate|3489|(40,)|const|uint8
var_3490 = relay.var("var_3490", dtype = "bool", shape = (52,))#candidate|3490|(52,)|var|bool
const_3491 = relay.const(-3, dtype = "uint64")#candidate|3491|()|const|uint64
const_3492 = relay.const([-8,-4,-2,9,-1,8,-8,-7,5,5,-5,-2,2,-6,-8,-2,-7,-3,9,4,9,-9,7,1,5,-4,1,-5,-1,9,5,4,-8,-2,-10,-8,-8,-5,3,9,-2,-8,-8,-7,3,8,7,-9,10,-3,-8,1,-8,-5,4,10,-6,10,-1,-4,-5,2,6,-9,5,-9,5,-10,-8,-5,-8,8,-1,-7,9,7,-6,8,-10,-8,-2,-7,9,-7,4,-9,7,6,8,-2,-7,-3,-8,4,-9,-3,3,8,-1,9,9,8,5,-5,9,2,-6,10,-5,2,-9,6,6,4,-1,3,-10,5,4,10,7,1,6,-7,-6,-6,-5,8,8,-1], dtype = "uint64")#candidate|3492|(130,)|const|uint64
call_3488 = relay.TupleGetItem(func_2779_call(relay.reshape(const_3489.astype('uint8'), [40,]), relay.reshape(var_3490.astype('bool'), [52,]), relay.reshape(const_3491.astype('uint64'), []), relay.reshape(const_3492.astype('uint64'), [130,]), ), 4)
call_3493 = relay.TupleGetItem(func_2784_call(relay.reshape(const_3489.astype('uint8'), [40,]), relay.reshape(var_3490.astype('bool'), [52,]), relay.reshape(const_3491.astype('uint64'), []), relay.reshape(const_3492.astype('uint64'), [130,]), ), 4)
func_1026_call = mod.get_global_var('func_1026')
func_1030_call = mutated_mod.get_global_var('func_1030')
const_3496 = relay.const([-10,1,-6,9,-7,-8,9,6,-10,6,-2,4,5,5,-4,6,-5,-9,5,-2,3,7,-3,-1,1,-9,-4,-8,-1,-7,-5,10,-7,-10,9,5,9,-5,-6,-7,6,9,-9,8,-1,-6,5,-6,-6,-7,6,6,3,-10,-8,5,5,3,-2,-3,-4,-1,6,3,4,7,-1,7,-6,4,-6,-9,2,4,-3,-7,5,-7,-5,-2,-10,1,4,7,7,-6,-10,-5,-7,8,-5,6,-5,2,5,1,5,-9,1,10,9,2,-9,6,7,5,-1,3,-5,-9,1,8,-3,-6,4,4,-4,-3,-5,-10,-2,-6,5,2,4,-2,5,-2,8,-5,-6,4,-7,-2,7,-7,-6,-4,2,-2,-1,-1,4,-5,1,-5,-6,6,7,8,-9,-4,5,5,6,-4,-2,3,8,8,-5,8,-1,7,-2,3,9,6,5,-3,-9,-10,-2,4,-1,1,5,-9,4,6,10,-9,7,3,7,7,-3,-4,1,6,2,8,-9,-6,3,-8,3,2,-3,4,-8,-3,-9,5,8,-4,1,10,10,-2,9,-6,7,2,2,9,8,-3,10,-1,-1,9,-8,1,-4,-1,-3,5,6,10,-5,9,3,-2,-2,-3,7,-7,10,3,1,9,2,3,-1,-7,4,-10,10,9,-7,6,-4,-9,1,10,-5,-5,3,6,-3,-10,2,1,6,-3,2,-4,-4,-1,-4,-6,-10,-7,-3,6,-7,2,-8,1,-4,-4,-6,5,3,5,-6,6,6,-8,-6,4,3,-5,10,5,-2,2,-9,-10,-2,-10,7,-6,-9,1,-9,3,10,4,-3,6,8,-5,-5,-1,-9,-5,7,9,-6,-3,5,8,3,-7,-9,-4,-1,5,-4,-10,7,9,-7,-2,-9,7,-3,9,-6,-4,1,3,-9,-7,7,5,-5,10,3,4,-6,-7,-7,-5,-5,8,-9,8,-3,10,-2,-6,9,6,7,-5,-2,-2,-1,10,5,1,-2,3,-2,5,-8,-1,-8,-9,9,-6,8,-8,4,-4,9,-7,4,6,1,-2,-4,-5,9,7,-8,9,-2,5,-8,-7,4,-5,3,6,5,-2,10,1,-1,-9,3,7,6,1,10,-10,1,-3,-7,8,-5,-10,10,-6,4,-4,-5,2,4,7,3,-8,-3,1,-10,-1,-1,-1,6,6,5,7,-2,3,-2,1,6,-2,-10,8,-1,-6,3,7,-7,9,4,1,-3,-3,-3,-2,2,7,-8,4,5,4,-9,7,-6,9,-2,-8,-5,2,3,-8,-10,9,-3,7,-4,7,-6,3,-3,-3,-3,10,2,-7,-9,-10,-3,7,3,-3,9,-4,4,-8,-10,-2,4,10,-5,8,3,3,8,-9,5,10,3,10,1,-4,1,-3,-9,10,1,6,-8,9,10,-9,-1,-1,-4,2,1,8,4,-6,4,5,-5,-1,-3,-9,8,9,8,4,3,9,3,-7,-9,-10,-10,-2,7,8,-4,4,-6,3,-3,7,-4,1,6,-4,4,1,8,-10,5,-6,4,10,3,5,-10,-3,1,-10,3,-1,8,2,5,3,-10,8,-1,6,-2,9,3,6,5,8,-2,8,3,7,3,-8,3,9,-6,9,5,-2,9,10,-8,5,-1,1,4,-2,10,-10,-5,8,-3,1,-6,-6,-3,-2,-7,10,-1,-10,10,1,-1,4,1,9,-10,2,5,2,4,-8,2,-7,-10,-5,-10,-10,-7,-6,8,-2,6,-8,-2,9,-6,-7,7,-9,-4,7,1,4,4,8,-7,-4,-4,4,-3,-4,-1,5,-8,7,9,5,-3,-9,2,1,-8,10,7,10,6,9,6,5,10,-5,8,-8,2,10,-5,-1,7,-4,7,6,-9,-1,1,-10,-10,10,8,8,9,2,-10,6,-6,2,8,7,5,4,-5,-8,9,2,-10,-7,-8,-3,-4,4,1,5,7,7,-1,-9,5,-1,7,-4,-2,8,-10,8,9,-7,-1,-10,-4,10,7,-2,-9,9,-4,5,-1,-8,3,8,10,-4,6,9,2,5,-9,4,-10,5,3,2,4,-9,-7,-9,-2,10,-7,-10,-8,-8,2,6,4,-7,-3,3,8,4,-6,-4,4,-6,3,-9,3,-2,1,8,-1,-4,-2,4,8,-7,9,-3,-5,5,7,1,-5,-4,2,4,6,10,5,-10,-1,7,8,4,-1,3,5,7,-8,-6,4,6,6,-10,1,3,-8,-4,10,-2,-9,8,-1,-3,9,-3,-9,-5,-6,-7,-4,1,-1,-10,2,-4,9,4,9,2,5,1,4,-9,10,9,6,-7,4,-10,1,7,5,3,9,4,-9,-9,2,3,-6,7,2,-1,-1,-3,6,-4,1,7,-3,3,-7,-6,10,10,-4,10,-10,2,-3,-6,7,9,9,8,-8,-5,3,3,-3,-1,-9,2,-3,3,-1,4,10,6,9,1,-4,4,8,-5,4,7,-9,3,7,-6,4,6,3,-3,-5,4,1,-1,7,9,1,5,8,2,5,-4,9,-4,2,-5,-2,-10,-6,3,6,7,1,-9,-1,2,10,4,6,10,-5,-6,-5,-1,7,8,-7,1,6,-7,-3,-10,7,-10,2,-10,8,-4,-4,6,9,5,9,-6,-7,10,1,3,-6,10,5,-4,10,6,3,5,7,7,-9,-1,-5,-8,-2,6,-4,-7,8,3,-9,2,-2,3,-9,5,5,-6,-8,-9,-7,-2,3,1,-1,9,-3,2,-10,-5,5,-8,-8,3,1,8,-8,1,10,-5,6,10,7,-7,7,5,-1,-4,-9,7,-10,-8,-7,-10,-10,-9,10,-8,-3,1,6,-6,1,8,-9,-10,1,-5,-8,9,-1,6,10,-8,8,5,-7,3,-2,-8,7,10,-9,-8,2,-6,-6,6,-8,-8,-6,-2,-5,1,-5,8,10,-10,3,-5,-5,-9,3,6,-2,8,7,-8,-3,10,9,-10,6,-7,5,-5,3,1,3,-5,-2,-10,-1,3,-9,-3,-3,-9,-10,9,8,-8,-1,-5,8,7,3,1,6,-1,7,5,-7,-8,-1,-6,2,-10,-5,-5,-8,-5,10,6,-9,10,3,5,-10,-8,-1,-9,-8,-6,-7,8,-5,-6,-8,-10,-1,5,6,5,7,6,-8,3,-6,-1,-1,-8,-3,-3,9,1,4,6,-8,-7,-6,2,-9,-2,-3,-10,3,1,2,-10,-7,-3,-7,-4,-3,7,-3,-3,-2,-9,-9,9,5,-9,-6,-10,-10,-6,5,1,1,5,-6,8,5,-5,4,-6,4,8,6,4,2,-2,-10,-4,10,-6,-10,-6,-2,7,5,-7,-9,-10,2,1,-2,2,6,2,5,-4,-2,10,-1,10,-10,-4,9,-6,-8,8,9,-1,-5,-5,-10,-7,-9,-4,4,6,-10,-5,-6,1,-7,3,6,3,6,-4,-6,9,-6,8,7,-3,6,-8,-8,-4,6,1,1,5,-1,-4,-8,2,5,5,4,1,-8,2,-7,-1,4,-7,7,4,3,-4,-10,6,-6,9,8,10,8,2,-8,8,-8,-9,-9,4,1,-4,6,-6,10,2,5,6,4,7,-4,6,-2,-8,7,2,1,1,-5,-10,10,4,4,9,9,-1,-4,4,1,-6,3,-8,-3,2,6,6,-3,-3,2,4,1,4,-2,9,2,4,3,-10,3,-6,-3,6,3,-1,-3,-6,-2,-10,-1,-8,6,8,5,6,9,6,-6,-6,-4,-6,5,3,-4,-2,4,8,3,9,-4,-6,9,-5,-6,6,1,7,3,5,-3,-2,8,-6,6,1,-10,-4,-10,-6,3,6,-3,2,-3,5,6,4,9,-7,5,6,-4,6,9,-10,-1,6,9,2,-7,-9,-4,6,-3,8,-10,5,5,10,1,-8,-6,8,4,-9,-7,-1,1,6,-10,-4,-1,4,8,1,6,4,4,9,-4,-7,7,5,5,4,8,-6,6,-6,-6,6,6,3,-3,-8,-1,1,-4,5,-8,7,-8,-6,2,1,-8,-9,-10,-4,3,2,-6,-1,9,-2,-7,-2,9,-9,1,9,8,4,10,-3,-10,8,-9,-6,5,3,4,-4,5,-6,-5,6,4,-1,9,-9,10,5,-4,-6,-1,-2,-8,10,2,-2,2,10,9,10,7,9,7,-7,-6,-2,3,2,10,5,-7,-7,-6,-4,-10,4,-4,-7,8,-1,-4,-3,-7,-8,-8,-9,1,-5,4,-3,4,4,-2,-6,-2,9,10,-4,-1,-5,7,-6,-9,7,-2,10,10,1,-2,4,-6,1,-7,4,-7,-8,3,5,7,-5,-2,5,8,4,5,-5,3,8,9,1,-2,-2,-5,7,1,-2,-9,-7,-3,9,2,-10,8,-6,-1,-6,-6,-10,-7,4,10,-5,1,8,-4,3,-10,3,-10,-6,-6,5,-1,4,1,10,-1,2,8,7,8,-7,2,8,-9,-4,9,8,4,1,-9,9,-5,-2,-3,-4,9,-1,3,3,-8,-10,8,-8,-1,8,-2,-8,9,10,10,-5,7,-10,-7,-4,-1,3,-2,2,2,1,-8,-10,10,-9,6,-9,-1,-5,3,-5,-4,4,1,-1,-5,-6,-5,9,8,8,-3,-9,6,-3,3,-5,-6,7,2,-2,-2,1,-7,-3,-10,3,5,-6,-5,-4,-6,-7,6,2,2,7,2,-9,8,-8,-10,2,10,-10,8,3,-1,-8,6,6,-4,2,-1,-9,-3,-9,-7,-10,-10,1,-2,-2,7,-1,2,1,-2,-3,3,4,-8,-9,-6,1,-7,4,1,6,7,-2,-7,-6,5,-2,3,4,-10,8,10,-2,4,-10,-3,2,4,-9,-7,7,-6,2,-6,-3,-9,-4,10,8,3,8,4,6,-4,-8,1,4,-8,-7,3,3,-8,-1,-7,2,-8,-8,10,2,-10,-4,-10,8,-5,2,-4,-9,6,-1,-8,-2,3,9,-3,-7,3,-4,2,-3,-7,-4,-2,3,3,-8,9,7,2,-5,-9,8,4,9,5,2,4,3,10,-3,-2,-4,-3,-2,9,9,-10,3,10,1,-1,9,10,3,-8,3,-9,10,9,8,9,-7,-6,-6,-2,4,-9,-9,5,-7,2,2,6,-5,5,-3,1,-5,2,-3,-6,6,-10,-4,-10,-7,-10,4,-2,-3,2,-1,-7,10,-8,4,2,1,8,6,-6,-8,3,-4,-1,-3,-2,6,3,-1,-10,6,6,3,-5,-1,3,9,3,2,10,-7,-10,-6,-10,3,-3,-4,-8,-2,-8,-4,-2,9,-8,-9,6,3,-2,6,-7,4,8,6,6,7,-10,-7,5,10,-8,-2,-9,-8,-5,3,-5,-1,-6,9,6,10,-10,-10,4,8,1,6,-8,-10,-1,6,-1,-1,3,-3,-7,-5,-9,-1,7,4,-1,9,-5,2,-4,-1,5,-4,-1,9,7,4,1,10,3,9,4,-3,8,4,8,-9,-9,-3,-1,8,-6,-5,-8,-8,-8,-6,4,-9,7,-8,-1,7,-1,10,-5,-1,3,-10,10,-3,-3,-1,8,-3,3,1,-10,6,9,3,-6,-4,2,-1,2,-1,3,-5,-1,-8,-10,10,7,1,-4,1,1,-3,1,-5,10,-9,-7,-3,-1,-5,-2,-10,5,-5,8,-8,-3,-1,-7,-7,-2,7,1,10,-5,-4,3,5,7,-4,-8,-3,-5,5,-1,-6,-1,6,7,5,-2,8,-4,1,3,-6,10,-3,-6,-7,-3,3,10,-7,5,8,2,1,10,-7,7,-5,-7,-2,-9,3,3,-7,5,-9,-7,-6,-6,-4,10,1,-9,4,7,10,-4,5,8,2,7,4,10,-2,8,3,1,3,10,-5,-3,10,-7,7,-8,-9,-10,-10,2,7,10,-7,-3,9,10,-2,-1,2,-9,5,8,6,-8,10,-6,1,-6,7,1,-7,-3,5,1,-4,-8,2,7,-6,2,-5,3,-6,-4,-10,-10,7,-6,-7,-2,1,-2,-8,9,-3,9,1,4,1,-2,-5,8,6,-6,2,6,10,6,-8,-1,8,-7,-2,-8,-8,-1,-5,-7,-6,-5,-5,-4,10,4,-5,-9,4,3,6,8,4,-9,10,-1,10,-7,-9,-1,-8,-9,9,7,-3,-9,2,2,-9,-4,-10,-7,10,-7,-2], dtype = "int8")#candidate|3496|(2310,)|const|int8
call_3495 = relay.TupleGetItem(func_1026_call(relay.reshape(const_3496.astype('int8'), [15, 11, 14]), relay.reshape(const_3496.astype('int8'), [15, 11, 14]), ), 0)
call_3497 = relay.TupleGetItem(func_1030_call(relay.reshape(const_3496.astype('int8'), [15, 11, 14]), relay.reshape(const_3496.astype('int8'), [15, 11, 14]), ), 0)
func_2464_call = mod.get_global_var('func_2464')
func_2465_call = mutated_mod.get_global_var('func_2465')
call_3503 = func_2464_call()
call_3504 = func_2464_call()
func_3040_call = mod.get_global_var('func_3040')
func_3043_call = mutated_mod.get_global_var('func_3043')
call_3505 = relay.TupleGetItem(func_3040_call(relay.reshape(const_3491.astype('int64'), []), relay.reshape(const_3489.astype('uint8'), [40,]), ), 0)
call_3506 = relay.TupleGetItem(func_3043_call(relay.reshape(const_3491.astype('int64'), []), relay.reshape(const_3489.astype('uint8'), [40,]), ), 0)
output = relay.Tuple([bop_3479,bop_3483,call_3488,const_3489,var_3490,const_3491,const_3492,call_3495,const_3496,call_3503,call_3505,])
output2 = relay.Tuple([bop_3479,bop_3483,call_3493,const_3489,var_3490,const_3491,const_3492,call_3497,const_3496,call_3504,call_3506,])
func_3508 = relay.Function([var_3477,var_3478,var_3482,var_3490,], output)
mod['func_3508'] = func_3508
mod = relay.transform.InferType()(mod)
var_3509 = relay.var("var_3509", dtype = "uint32", shape = (13, 14, 1))#candidate|3509|(13, 14, 1)|var|uint32
var_3510 = relay.var("var_3510", dtype = "uint32", shape = (13, 14, 1))#candidate|3510|(13, 14, 1)|var|uint32
var_3511 = relay.var("var_3511", dtype = "uint32", shape = (13, 14, 9))#candidate|3511|(13, 14, 9)|var|uint32
var_3512 = relay.var("var_3512", dtype = "bool", shape = (52,))#candidate|3512|(52,)|var|bool
output = func_3508(var_3509,var_3510,var_3511,var_3512,)
func_3513 = relay.Function([var_3509,var_3510,var_3511,var_3512,], output)
mutated_mod['func_3513'] = func_3513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2464_call = mod.get_global_var('func_2464')
func_2465_call = mutated_mod.get_global_var('func_2465')
call_3551 = func_2464_call()
call_3552 = func_2464_call()
func_3097_call = mod.get_global_var('func_3097')
func_3099_call = mutated_mod.get_global_var('func_3099')
call_3558 = func_3097_call()
call_3559 = func_3097_call()
func_2984_call = mod.get_global_var('func_2984')
func_2986_call = mutated_mod.get_global_var('func_2986')
call_3566 = func_2984_call()
call_3567 = func_2984_call()
output = relay.Tuple([call_3551,call_3558,call_3566,])
output2 = relay.Tuple([call_3552,call_3559,call_3567,])
func_3568 = relay.Function([], output)
mod['func_3568'] = func_3568
mod = relay.transform.InferType()(mod)
output = func_3568()
func_3569 = relay.Function([], output)
mutated_mod['func_3569'] = func_3569
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3097_call = mod.get_global_var('func_3097')
func_3099_call = mutated_mod.get_global_var('func_3099')
call_3600 = func_3097_call()
call_3601 = func_3097_call()
func_2566_call = mod.get_global_var('func_2566')
func_2569_call = mutated_mod.get_global_var('func_2569')
const_3606 = relay.const([-3.399700,3.231498,2.905019,1.664221,4.846155,2.252152,-0.595074,0.962741,-4.860343,-6.795893,-6.650325,5.885968,5.908828,-2.286583,3.607181,6.765454,-4.427358,-4.301032,0.398498,-6.061420,-4.678240,-6.651492,6.142389,-0.370339,2.634571,7.256226,-1.408159,2.499296,4.724849,-4.156756,-5.827869,2.045353,-3.200706,0.506987,2.820536,-0.814858,5.218346,-5.888629,-9.883230,-8.442623,4.078286,-4.158720,-4.809311,-1.767887,9.687222,-6.159939,-2.113256,-2.394801,-5.943139,-1.607327,0.753428,8.596856,6.332481,-1.296808,-1.525913,7.726648,-7.502659,7.139050,-7.027990,-4.803961,-3.251704,7.642955,-5.636264,-0.503475,8.311955,-8.305301,6.058258,1.098444,0.323904,9.242665,-5.870282,-2.791473,-4.259920,-7.794516,4.023103,-1.090025,2.456110,-8.400512,-7.543684,-4.212732,2.122956,-0.309570,1.089787,-7.011325,4.089275,-2.765065,-3.868194,-0.056473,8.946473,5.671971,-6.838630,-8.381086,-8.046763,0.057700,8.539773,-4.896351,0.054867,-8.792789,5.984921,7.043628,-8.963460,-6.184802,-6.000153,7.738878,3.692486,-9.846610,-3.696605,-5.098852,7.095526,1.183489,2.142371,-5.556771,5.157987,1.777749,8.694798,5.556973,0.165522,-6.322611,0.988721,8.377024,9.437161,-8.704188,-0.416737,-5.339133,-5.320981,2.784117,0.095615,-4.672169,-2.480232,2.569015,3.008722,5.976608,1.359427,-5.687465,9.007590,2.522964,-2.830965,-3.921490,-4.986965,-6.878045,9.992276,4.163298,7.809996,6.408241,0.193461,3.383336,6.987222,9.084038,1.285673,0.156090,1.765115,4.991400,-4.871707,2.650102,-7.502540,-4.880380,3.891215,-3.877756,6.704196,-3.219881,6.109386,7.236969,-0.086439,7.168423,0.774968,-3.413891,7.459703,-2.869863,4.922647,9.469442,9.205245,2.249029,7.785350,-9.971647,9.992510,4.715501,-0.804797,-4.977454,-8.690906,-6.780404,-1.140171,-8.089549,-5.537953,-2.515599,-3.962435,8.418023,4.972293,-5.379917,1.782887,8.598008,6.510983,4.314080,-7.123256,-5.811118,3.975737,-9.986254,0.471728,4.642699,1.007335,-0.324865,8.502461,2.526611,-2.244524,1.675608,-3.191939,3.930979,-3.705754,-0.731595,-9.478580,4.031871,1.983553,7.753425,-4.175358,8.483657,-1.853241,-4.592344,0.829874,-3.280391,6.048240,7.722625,1.483991,-1.463277,9.292669,-1.034146,8.530605,6.847345,2.516617,-6.411864,-8.130863,4.677280,6.837016,-6.583436,6.100717,-3.189997,9.971168,8.990370,-5.639036,-3.621979,-7.086020,0.889819,-4.263554,-9.786168,-0.948229,6.385713,-9.862019,1.900293,-0.170995,7.558382,9.675908,1.339686,0.799073,5.804311,-4.526274,-4.358459,-0.196521,-2.675775,-1.779764,-6.329208,6.509468,9.024108,-4.154423,2.632110,0.538088,-9.564318,2.971070,1.826299,-4.613647,-5.315344,-7.759258,2.446471,7.984460,5.235069,2.357908,-4.344870,8.564959,-8.363573,-7.291517,5.309445,-7.713661,-3.373966,9.223496,6.832382,-6.074110,-9.396917,-9.530358,6.155822,1.078640,4.030584,-3.101882,-9.108976,-1.823484,1.331150,-3.471914,-7.061422,0.555199,-5.421565,-2.604917,-5.062144,-1.738454,9.858999,5.548190,-5.711097,5.826549,9.600071,6.196351,8.686648,-9.919205,-0.451008,4.619665,-7.466309,-8.984295,5.999131,-8.754365,2.224524,-0.047918,3.557113,-6.080533,2.098153,7.699953,5.656905,-7.543071,-4.306814,-8.894070,7.585152,9.356659,-0.049273,4.974775,-6.055398,5.075358,-6.495863,-0.247554,4.495066,4.662663,-9.676054,8.861779,8.553587,5.252529,4.659625,-4.479229,5.097332,-0.309035,1.513217,-0.977087,0.734457,-3.854128,4.107840,2.691711,3.822760,4.439724,6.159533,8.235850,-3.309166,0.740507,-2.517939,4.098601,6.622969,9.667884,2.628398,9.369875,-5.057299,-4.987191,-7.967626,-7.247766,-4.941760,-5.551142,7.255738,-7.835305,-4.348022,5.970579,9.594265,-0.735766,-9.092743,-3.474353,0.447229,-5.080932,8.355894,-1.874743,-4.115002,4.956449,-3.658256,-5.139915,6.694917,-9.970621,-8.637318,8.921565,-6.451262,4.594578,0.827480,-8.945497,4.989351,-1.653007,9.633414,-9.671822,-5.987015,-1.623461,9.754705,-5.353305,7.134459,-2.124458,-2.463749,1.634540,-0.570711,2.632623,-5.331865,-7.791444,-7.528899,-8.661548,4.147163,7.136998,-4.063918,4.451263,-4.114720,8.737431,-0.485309,-6.691163,0.171970,6.459547,-9.746392,7.159542,-6.150981,-9.917522,6.912329,-9.220416,5.260763,-4.946675,8.958975,-0.545120,6.672478,8.830910,0.492100,-8.578898,2.874990,-2.062120,-9.366046,0.507958,-0.908150,0.793381,-2.289155,-0.267568,3.271569,-5.626589,-4.593044,-3.556255,-6.371247,0.912459,3.181377,-0.619471,4.144004,-2.834965,-1.902017,-3.005066,3.217198,-0.001201,3.937722,-5.088214,9.246611,2.717554,5.581017,8.531519,7.012567,3.129222,-3.178156,-8.736627,8.702376,8.719000,-3.091233,-8.388980,2.669063,5.174499,9.753569,3.658866,-2.123531,8.741819,3.733873,8.086461,4.606283,3.312126,-4.684769,-8.389355,1.391542,-7.723831,7.586249,3.999144,9.390336,-4.831760,-3.785522,-0.050417,-7.725263,-5.152240,-1.194603,0.266967,2.271080,-2.947694,-0.151130,0.266297,-0.616893,1.909937,-3.606027,3.647215,9.074246,-9.636791,7.200202,5.344291,-4.552137,4.125955,7.676931,4.007308,-2.574568,2.615138,-9.008010,-7.435950,-5.478667,-6.494436,-3.525554,-0.248846,9.413182,-1.536498,8.065146,6.390700,9.127423,3.270116,4.350345,7.356573,-3.038730,-5.908421,7.515148,0.138173,-3.886851,-0.351512,7.103574,-0.188888,-5.965027,-0.331992,-4.425312,7.947288,-0.687793,6.239305,7.728076,2.999994,9.509334,-6.392048,-1.873954,-8.861135,-3.804721,-9.491552,3.099844,-5.824681,6.432387,-1.571827,-9.474936,6.850022,-1.928003,-2.250874,-7.952027,0.995526,4.973774,-0.338695,7.059236,-0.014305,-8.381441,-5.078238,-7.582216,4.044735,1.105332,6.357484,1.215717,-3.874491,1.387409,-6.563821,1.229966,7.455651,7.852040,-2.400991,-1.427658,-5.003217,9.219717,1.857378,-3.952084,2.699851,-5.712751,4.951903,-7.462307,1.275988,8.908320,3.439722,8.306649,9.279824,-5.319880,4.322041,2.639376,4.891139,-8.405478,-8.478065,0.442549,-0.295953,-1.886680,-9.290494,-5.985408,1.835524,9.736688], dtype = "float64")#candidate|3606|(600,)|const|float64
var_3607 = relay.var("var_3607", dtype = "int32", shape = (990,))#candidate|3607|(990,)|var|int32
call_3605 = relay.TupleGetItem(func_2566_call(relay.reshape(const_3606.astype('float64'), [5, 10, 12]), relay.reshape(var_3607.astype('int32'), [990,]), ), 2)
call_3608 = relay.TupleGetItem(func_2569_call(relay.reshape(const_3606.astype('float64'), [5, 10, 12]), relay.reshape(var_3607.astype('int32'), [990,]), ), 2)
output = relay.Tuple([call_3600,call_3605,const_3606,var_3607,])
output2 = relay.Tuple([call_3601,call_3608,const_3606,var_3607,])
func_3613 = relay.Function([var_3607,], output)
mod['func_3613'] = func_3613
mod = relay.transform.InferType()(mod)
mutated_mod['func_3613'] = func_3613
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3614 = relay.var("var_3614", dtype = "int32", shape = (990,))#candidate|3614|(990,)|var|int32
func_3613_call = mutated_mod.get_global_var('func_3613')
call_3615 = func_3613_call(var_3614)
output = call_3615
func_3616 = relay.Function([var_3614], output)
mutated_mod['func_3616'] = func_3616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3463_call = mod.get_global_var('func_3463')
func_3465_call = mutated_mod.get_global_var('func_3465')
call_3639 = relay.TupleGetItem(func_3463_call(), 0)
call_3640 = relay.TupleGetItem(func_3465_call(), 0)
func_3396_call = mod.get_global_var('func_3396')
func_3398_call = mutated_mod.get_global_var('func_3398')
call_3647 = func_3396_call()
call_3648 = func_3396_call()
func_1559_call = mod.get_global_var('func_1559')
func_1561_call = mutated_mod.get_global_var('func_1561')
call_3651 = relay.TupleGetItem(func_1559_call(), 0)
call_3652 = relay.TupleGetItem(func_1561_call(), 0)
output = relay.Tuple([call_3639,call_3647,call_3651,])
output2 = relay.Tuple([call_3640,call_3648,call_3652,])
func_3661 = relay.Function([], output)
mod['func_3661'] = func_3661
mod = relay.transform.InferType()(mod)
output = func_3661()
func_3662 = relay.Function([], output)
mutated_mod['func_3662'] = func_3662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2336_call = mod.get_global_var('func_2336')
func_2338_call = mutated_mod.get_global_var('func_2338')
call_3680 = relay.TupleGetItem(func_2336_call(), 0)
call_3681 = relay.TupleGetItem(func_2338_call(), 0)
func_3122_call = mod.get_global_var('func_3122')
func_3123_call = mutated_mod.get_global_var('func_3123')
call_3693 = relay.TupleGetItem(func_3122_call(), 1)
call_3694 = relay.TupleGetItem(func_3123_call(), 1)
func_1462_call = mod.get_global_var('func_1462')
func_1463_call = mutated_mod.get_global_var('func_1463')
call_3700 = func_1462_call()
call_3701 = func_1462_call()
func_3508_call = mod.get_global_var('func_3508')
func_3513_call = mutated_mod.get_global_var('func_3513')
const_3703 = relay.const([[4,3,9,8,7,-8,-10,7,3,5,-1,-2,3,6,3,-4,-3,6,6,-3,-10,5,5,5,1,7,-9,7,-8,-10,1,9,-2,6,-3,-3,8,-4,-8,-1,9,1,9,-1,-4,-10,-6,9,-6,-8,-1,-1,-6,4,-3,5,2,-1,-7,-8,3,6,-8,9,-7,4,-5,1,-1,-7,9,-8,9,4,2,-7,-3,-6,5,7,-10,3,8,-9,6,-5,10,-10,5,-7,7,3,6,-10,-5,-6,-10,2,-1,-8,9,-4,1,1,7,2,-3,-3,-6,-3,-10,6,8,-7,-1,7,-10,-2,-6,-4,3,8,-3,-9,4,8,1,-1,5,1,4,-7,-1,-5,2,-10,7,10,-9,-9,-1,6,-2,-4,-6,3,2,-4,9,-10,1,3,-9,8,-4,-10,5,-8,4,5,4,10,8,-9,-3,7,8,-2,6,5,-8,-4,5,-9,3,-9,-2,5,4,8,-2,1]], dtype = "uint32")#candidate|3703|(1, 182)|const|uint32
var_3704 = relay.var("var_3704", dtype = "uint32", shape = (546, 3))#candidate|3704|(546, 3)|var|uint32
var_3705 = relay.var("var_3705", dtype = "bool", shape = (52,))#candidate|3705|(52,)|var|bool
call_3702 = relay.TupleGetItem(func_3508_call(relay.reshape(const_3703.astype('uint32'), [13, 14, 1]), relay.reshape(const_3703.astype('uint32'), [13, 14, 1]), relay.reshape(var_3704.astype('uint32'), [13, 14, 9]), relay.reshape(var_3705.astype('bool'), [52,]), ), 10)
call_3706 = relay.TupleGetItem(func_3513_call(relay.reshape(const_3703.astype('uint32'), [13, 14, 1]), relay.reshape(const_3703.astype('uint32'), [13, 14, 1]), relay.reshape(var_3704.astype('uint32'), [13, 14, 9]), relay.reshape(var_3705.astype('bool'), [52,]), ), 10)
uop_3718 = relay.sinh(call_3680.astype('float32')) # shape=(8, 14, 2)
uop_3720 = relay.sinh(call_3681.astype('float32')) # shape=(8, 14, 2)
func_789_call = mod.get_global_var('func_789')
func_791_call = mutated_mod.get_global_var('func_791')
const_3725 = relay.const([4.649737,0.834332,-6.662492,-4.523870,4.126359,2.791317,-4.331856,9.122863,-3.261703,-7.788063,-5.625442,-3.106549,5.066403,3.370349,-8.197891,-8.533385,-6.266433,7.628978,3.273879,-8.387022,2.881868,-9.225457,-9.284502,-8.259375,-1.643963,4.753966,-0.706191,-9.673335,6.023352,-1.188164,8.699079,-2.060987,-5.843418,-7.165887,5.530250,-8.996124,1.496778,-8.732666,0.255005,-1.350460,8.614089,-3.051954,-9.912443,3.622624,2.186845,3.419104,-0.408845,-9.798041,7.856105,-1.533549,8.632598,9.016395,9.695976,9.130163,7.553921,5.832951,9.113446,-6.124159,-2.107060,-6.476825,4.077646,-9.270393,0.312405,-8.025337,-1.168496,8.716886,3.014432,-2.570236,9.092814,8.286910,7.025131,5.758016,1.525073,-4.296604,-6.166511,8.381873,-5.429400,4.907103,-4.920205,2.212822,4.809334,-0.683209,0.408818,6.055877,-0.654447,0.808337,9.816994,8.038536,-7.019314,5.879287,-0.955761,-0.444557,-3.847133,-5.640702,4.389256,0.463345,-9.429452,-5.622426,-2.145904,-0.846377,-7.125883,0.963516,8.986839,-4.664199,-6.715597], dtype = "float32")#candidate|3725|(105,)|const|float32
call_3724 = relay.TupleGetItem(func_789_call(relay.reshape(const_3725.astype('float32'), [3, 7, 5])), 0)
call_3726 = relay.TupleGetItem(func_791_call(relay.reshape(const_3725.astype('float32'), [3, 7, 5])), 0)
func_31_call = mod.get_global_var('func_31')
func_34_call = mutated_mod.get_global_var('func_34')
const_3746 = relay.const([3,3,-10,7,-5,-3,10,-9,-2,3,-1,-10,-6,-3,9,7,9,10,-6,-5,5,1,-5,-10,-7,7,-9,-9,5,-2,-3,-10,10,-2,-9,9,-5,9,-1,7], dtype = "uint8")#candidate|3746|(40,)|const|uint8
call_3745 = relay.TupleGetItem(func_31_call(relay.reshape(const_3746.astype('uint8'), [5, 4, 2]), relay.reshape(const_3746.astype('uint8'), [5, 4, 2]), ), 0)
call_3747 = relay.TupleGetItem(func_34_call(relay.reshape(const_3746.astype('uint8'), [5, 4, 2]), relay.reshape(const_3746.astype('uint8'), [5, 4, 2]), ), 0)
output = relay.Tuple([call_3693,call_3700,call_3702,const_3703,var_3704,var_3705,uop_3718,call_3724,const_3725,call_3745,const_3746,])
output2 = relay.Tuple([call_3694,call_3701,call_3706,const_3703,var_3704,var_3705,uop_3720,call_3726,const_3725,call_3747,const_3746,])
func_3751 = relay.Function([var_3704,var_3705,], output)
mod['func_3751'] = func_3751
mod = relay.transform.InferType()(mod)
mutated_mod['func_3751'] = func_3751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3751_call = mutated_mod.get_global_var('func_3751')
var_3753 = relay.var("var_3753", dtype = "uint32", shape = (546, 3))#candidate|3753|(546, 3)|var|uint32
var_3754 = relay.var("var_3754", dtype = "bool", shape = (52,))#candidate|3754|(52,)|var|bool
call_3752 = func_3751_call(var_3753,var_3754,)
output = call_3752
func_3755 = relay.Function([var_3753,var_3754,], output)
mutated_mod['func_3755'] = func_3755
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2336_call = mod.get_global_var('func_2336')
func_2338_call = mutated_mod.get_global_var('func_2338')
call_3771 = relay.TupleGetItem(func_2336_call(), 0)
call_3772 = relay.TupleGetItem(func_2338_call(), 0)
func_3661_call = mod.get_global_var('func_3661')
func_3662_call = mutated_mod.get_global_var('func_3662')
call_3789 = relay.TupleGetItem(func_3661_call(), 0)
call_3790 = relay.TupleGetItem(func_3662_call(), 0)
func_1111_call = mod.get_global_var('func_1111')
func_1116_call = mutated_mod.get_global_var('func_1116')
const_3809 = relay.const([-1,1,3,-8,6,9,-9,8,10,-6,7,1,-1,-3,10,-1,10,3,-9,-8,-4,-10,-7,-9,-10,-9,7,10,-1,-10,-10,-1,2,-4,6,-6,10,-5,6,-4,-9,5,5,3,-10,-6,-3,-1,-3,-7,-6,9,-1,-2,8,-5,-1,4,-6,1,-9,6,-3,8,9,-3,10,-2,-6,-10], dtype = "int8")#candidate|3809|(70,)|const|int8
var_3810 = relay.var("var_3810", dtype = "int8", shape = (1, 420))#candidate|3810|(1, 420)|var|int8
var_3811 = relay.var("var_3811", dtype = "uint8", shape = (40,))#candidate|3811|(40,)|var|uint8
call_3808 = relay.TupleGetItem(func_1111_call(relay.reshape(const_3809.astype('int8'), [14, 5, 1]), relay.reshape(var_3810.astype('int8'), [14, 5, 6]), relay.reshape(var_3811.astype('uint8'), [40,]), ), 1)
call_3812 = relay.TupleGetItem(func_1116_call(relay.reshape(const_3809.astype('int8'), [14, 5, 1]), relay.reshape(var_3810.astype('int8'), [14, 5, 6]), relay.reshape(var_3811.astype('uint8'), [40,]), ), 1)
var_3817 = relay.var("var_3817", dtype = "int8", shape = (10, 420))#candidate|3817|(10, 420)|var|int8
bop_3818 = relay.equal(var_3810.astype('bool'), var_3817.astype('bool')) # shape=(10, 420)
output = relay.Tuple([call_3771,call_3789,call_3808,const_3809,var_3811,bop_3818,])
output2 = relay.Tuple([call_3772,call_3790,call_3812,const_3809,var_3811,bop_3818,])
func_3827 = relay.Function([var_3810,var_3811,var_3817,], output)
mod['func_3827'] = func_3827
mod = relay.transform.InferType()(mod)
mutated_mod['func_3827'] = func_3827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3827_call = mutated_mod.get_global_var('func_3827')
var_3829 = relay.var("var_3829", dtype = "int8", shape = (1, 420))#candidate|3829|(1, 420)|var|int8
var_3830 = relay.var("var_3830", dtype = "uint8", shape = (40,))#candidate|3830|(40,)|var|uint8
var_3831 = relay.var("var_3831", dtype = "int8", shape = (10, 420))#candidate|3831|(10, 420)|var|int8
call_3828 = func_3827_call(var_3829,var_3830,var_3831,)
output = call_3828
func_3832 = relay.Function([var_3829,var_3830,var_3831,], output)
mutated_mod['func_3832'] = func_3832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3122_call = mod.get_global_var('func_3122')
func_3123_call = mutated_mod.get_global_var('func_3123')
call_3836 = relay.TupleGetItem(func_3122_call(), 0)
call_3837 = relay.TupleGetItem(func_3123_call(), 0)
output = relay.Tuple([call_3836,])
output2 = relay.Tuple([call_3837,])
func_3840 = relay.Function([], output)
mod['func_3840'] = func_3840
mod = relay.transform.InferType()(mod)
output = func_3840()
func_3841 = relay.Function([], output)
mutated_mod['func_3841'] = func_3841
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2164_call = mod.get_global_var('func_2164')
func_2166_call = mutated_mod.get_global_var('func_2166')
call_3961 = func_2164_call()
call_3962 = func_2164_call()
var_3969 = relay.var("var_3969", dtype = "int8", shape = (8, 14, 2))#candidate|3969|(8, 14, 2)|var|int8
bop_3970 = relay.power(call_3961.astype('float64'), relay.reshape(var_3969.astype('float64'), relay.shape_of(call_3961))) # shape=(8, 14, 2)
bop_3973 = relay.power(call_3962.astype('float64'), relay.reshape(var_3969.astype('float64'), relay.shape_of(call_3962))) # shape=(8, 14, 2)
output = relay.Tuple([bop_3970,])
output2 = relay.Tuple([bop_3973,])
func_3979 = relay.Function([var_3969,], output)
mod['func_3979'] = func_3979
mod = relay.transform.InferType()(mod)
mutated_mod['func_3979'] = func_3979
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3980 = relay.var("var_3980", dtype = "int8", shape = (8, 14, 2))#candidate|3980|(8, 14, 2)|var|int8
func_3979_call = mutated_mod.get_global_var('func_3979')
call_3981 = func_3979_call(var_3980)
output = call_3981
func_3982 = relay.Function([var_3980], output)
mutated_mod['func_3982'] = func_3982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2582_call = mod.get_global_var('func_2582')
func_2584_call = mutated_mod.get_global_var('func_2584')
call_3994 = relay.TupleGetItem(func_2582_call(), 1)
call_3995 = relay.TupleGetItem(func_2584_call(), 1)
output = call_3994
output2 = call_3995
func_4011 = relay.Function([], output)
mod['func_4011'] = func_4011
mod = relay.transform.InferType()(mod)
output = func_4011()
func_4012 = relay.Function([], output)
mutated_mod['func_4012'] = func_4012
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2164_call = mod.get_global_var('func_2164')
func_2166_call = mutated_mod.get_global_var('func_2166')
call_4046 = func_2164_call()
call_4047 = func_2164_call()
func_3274_call = mod.get_global_var('func_3274')
func_3278_call = mutated_mod.get_global_var('func_3278')
const_4052 = relay.const([-2,-4,10,-1,-6,-10,-10,-6,-5,-9,2,-4,-3,7,10,3,-9,-6,-4,-5,10,3,4,-5,8,9,-1,-8,-2,8,-3,3,1,10,6,8,-1,-8,-8,-5,8,10,-9,-6,3,10,-9,7,4,-7,-3,8,6,10,-10,-2,-10,-10,3,7,-1,10,-4,2,-6,-10,-4,2,4,-5,10,-3,-2,-7,-10,-8,5,-3,-9,-5,-3,-2,3,8,10,4,-1,-8,1,-7,-4,-3,7,6,-10,8,7,-2,-8,10,2,-7,2,-7,5,-7,2,-7,-8,4,-7,-1,6,5,-4,3,-10,10,-10,-8,-4,5,4,5,-7,10,-3,8,-6,3,-1,-5,-7,-4,5,-1,8,-5,7,6,10,2,7,-3,5,3,2,-9,-7,5,7,-1,1,-9,7,-6,9,2,-8,-1,3,-10,-5,4,-2,-4,-7,5], dtype = "uint16")#candidate|4052|(168,)|const|uint16
var_4053 = relay.var("var_4053", dtype = "float32", shape = (105, 1))#candidate|4053|(105, 1)|var|float32
call_4051 = relay.TupleGetItem(func_3274_call(relay.reshape(const_4052.astype('uint16'), [168,]), relay.reshape(var_4053.astype('float32'), [105,]), ), 1)
call_4054 = relay.TupleGetItem(func_3278_call(relay.reshape(const_4052.astype('uint16'), [168,]), relay.reshape(var_4053.astype('float32'), [105,]), ), 1)
bop_4055 = relay.logical_xor(var_4053.astype('uint8'), const_4052.astype('uint8')) # shape=(105, 168)
var_4068 = relay.var("var_4068", dtype = "float32", shape = (105, 1))#candidate|4068|(105, 1)|var|float32
bop_4069 = relay.bitwise_and(var_4053.astype('int16'), relay.reshape(var_4068.astype('int16'), relay.shape_of(var_4053))) # shape=(105, 1)
output = relay.Tuple([call_4046,call_4051,bop_4055,bop_4069,])
output2 = relay.Tuple([call_4047,call_4054,bop_4055,bop_4069,])
func_4074 = relay.Function([var_4053,var_4068,], output)
mod['func_4074'] = func_4074
mod = relay.transform.InferType()(mod)
var_4075 = relay.var("var_4075", dtype = "float32", shape = (105, 1))#candidate|4075|(105, 1)|var|float32
var_4076 = relay.var("var_4076", dtype = "float32", shape = (105, 1))#candidate|4076|(105, 1)|var|float32
output = func_4074(var_4075,var_4076,)
func_4077 = relay.Function([var_4075,var_4076,], output)
mutated_mod['func_4077'] = func_4077
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4179 = relay.const([[[-3,7,2,-2,1,3,1,-1,-4,-4,2,-4,-8,-5],[7,6,10,-6,7,7,-9,-8,-8,5,-1,4,-4,2],[1,4,-9,-7,-6,-1,-3,2,9,-4,-7,8,-10,1],[1,6,3,9,2,10,1,10,-2,-5,4,-7,-10,1]],[[9,4,7,1,9,3,8,-9,7,-2,-6,9,8,-1],[2,8,5,-1,-3,-4,4,4,-3,10,4,10,-9,-10],[-4,7,2,-9,-9,-1,7,-5,-5,3,-3,9,-5,7],[-7,-2,7,-10,7,8,-2,-8,-8,-9,1,-2,-3,2]],[[-1,3,-8,-10,-4,-6,2,7,-6,-2,-8,-7,1,5],[-2,3,8,1,8,-2,4,3,3,9,-5,-4,-1,3],[-10,-5,7,-4,-3,2,-8,8,-2,7,3,5,-8,2],[-7,1,-3,-8,6,7,8,-3,-2,8,3,9,3,3]],[[-2,1,10,-9,-8,-5,-10,6,-10,2,-1,7,-8,-8],[-2,-4,-6,6,-9,-10,3,-3,-8,10,-7,1,5,-10],[6,-5,8,3,-4,-1,3,2,-9,-8,2,-6,-10,-7],[-8,-9,-6,1,2,10,-2,-1,-2,-10,7,-1,-3,8]],[[-5,2,5,-6,-4,4,2,5,5,-8,8,10,-5,4],[8,-3,10,-8,7,-3,2,8,-1,7,-9,-3,-2,-2],[-3,-5,10,-6,5,5,-10,2,6,-8,-3,3,10,8],[-8,-9,9,-4,5,-1,-5,-4,-7,-9,-8,-9,1,-2]],[[-7,-5,3,8,9,2,3,6,-2,-5,7,-1,10,-6],[4,-4,-8,-8,2,-2,-9,6,-10,1,3,10,-1,-6],[2,2,10,7,-4,9,-10,-6,7,-10,-4,-8,9,6],[-10,-1,-4,6,-10,4,-7,-7,-5,-3,-4,-1,4,-5]],[[9,2,-6,2,5,-4,3,6,-2,-7,7,1,-5,-2],[-2,-1,-10,10,6,-6,2,-6,9,-6,-7,7,-5,7],[-1,-10,-8,3,5,-4,5,-2,1,3,9,2,-2,-10],[-9,8,6,2,10,1,-9,6,6,-3,3,-10,5,10]],[[3,6,-7,-4,4,-8,-1,8,6,4,-2,-3,-10,9],[7,5,-9,3,-7,2,3,6,1,-2,7,-2,-2,4],[-10,-9,2,8,-7,1,8,-5,-3,4,4,10,-3,-10],[9,-9,9,-5,-2,-6,6,2,9,6,10,-6,10,-8]],[[10,10,-6,-8,6,7,10,8,-1,9,-10,3,-9,-6],[7,-3,-6,8,-1,6,-4,5,8,-10,-4,10,6,-7],[4,-3,9,-10,9,6,8,5,-7,-6,6,4,4,7],[9,6,-7,-6,7,1,6,5,-9,6,5,-1,-7,-10]],[[-10,5,-10,5,-2,-4,-7,-6,-2,4,3,5,3,6],[2,-3,4,-2,-10,10,7,2,8,-4,-1,10,-2,2],[3,-5,6,7,-5,4,7,-9,9,6,-1,8,3,-6],[4,-8,5,-4,-1,-3,-2,-4,-3,3,4,9,-2,-7]],[[-4,-1,8,9,-3,4,-6,2,4,-6,1,-8,1,-10],[4,-9,2,-9,9,4,1,-8,7,-6,10,-7,-1,3],[4,-6,-3,-9,5,5,-7,8,1,6,7,-8,-4,-5],[-3,9,-4,-8,-8,-3,-6,-8,1,3,-1,-7,-1,-5]]], dtype = "uint16")#candidate|4179|(11, 4, 14)|const|uint16
var_4180 = relay.var("var_4180", dtype = "uint16", shape = (11, 4, 14))#candidate|4180|(11, 4, 14)|var|uint16
bop_4181 = relay.equal(const_4179.astype('bool'), relay.reshape(var_4180.astype('bool'), relay.shape_of(const_4179))) # shape=(11, 4, 14)
output = bop_4181
output2 = bop_4181
func_4188 = relay.Function([var_4180,], output)
mod['func_4188'] = func_4188
mod = relay.transform.InferType()(mod)
mutated_mod['func_4188'] = func_4188
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4189 = relay.var("var_4189", dtype = "uint16", shape = (11, 4, 14))#candidate|4189|(11, 4, 14)|var|uint16
func_4188_call = mutated_mod.get_global_var('func_4188')
call_4190 = func_4188_call(var_4189)
output = call_4190
func_4191 = relay.Function([var_4189], output)
mutated_mod['func_4191'] = func_4191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2943_call = mod.get_global_var('func_2943')
func_2944_call = mutated_mod.get_global_var('func_2944')
call_4271 = func_2943_call()
call_4272 = func_2943_call()
func_2336_call = mod.get_global_var('func_2336')
func_2338_call = mutated_mod.get_global_var('func_2338')
call_4273 = relay.TupleGetItem(func_2336_call(), 0)
call_4274 = relay.TupleGetItem(func_2338_call(), 0)
func_2022_call = mod.get_global_var('func_2022')
func_2028_call = mutated_mod.get_global_var('func_2028')
const_4292 = relay.const(1, dtype = "uint64")#candidate|4292|()|const|uint64
const_4293 = relay.const([[-1,9,7,-4,-7],[1,8,-8,-10,-5],[10,4,-4,-9,2],[-10,6,-4,-9,-7],[3,6,3,-6,-9],[-1,-10,4,-10,5],[-10,7,-6,8,-9],[-4,4,4,5,10],[2,2,8,6,-1],[-2,-7,7,-1,-1],[-4,3,-6,-7,10],[7,-1,-3,-7,9],[-7,-6,-9,10,-10],[10,-9,-3,-3,-7],[8,-2,5,7,4],[7,-6,-8,10,5],[-2,-3,10,-7,6],[6,10,-2,5,4],[-5,1,-7,-6,-10],[6,-6,2,-5,-8],[2,5,-4,-4,8],[8,-2,5,-1,-4],[-10,10,9,3,-10],[-7,7,-4,-2,-1],[8,-4,-2,8,9],[-2,-4,6,-6,-9]], dtype = "uint64")#candidate|4293|(26, 5)|const|uint64
var_4294 = relay.var("var_4294", dtype = "float32", shape = (52,))#candidate|4294|(52,)|var|float32
const_4295 = relay.const([-1,1,1,2,5,10,4,-1,-3,4,9,1,9,-2,-8,-9,3,-10,3,-6,9,-6,-7,6,3,-7,1,6,8,10,-8,-4,-10,7,-8,2,10,-10,6,-7], dtype = "uint8")#candidate|4295|(40,)|const|uint8
call_4291 = relay.TupleGetItem(func_2022_call(relay.reshape(const_4292.astype('uint64'), []), relay.reshape(const_4293.astype('uint64'), [13, 5, 2]), relay.reshape(var_4294.astype('float32'), [2, 2, 13]), relay.reshape(const_4295.astype('uint8'), [40,]), ), 6)
call_4296 = relay.TupleGetItem(func_2028_call(relay.reshape(const_4292.astype('uint64'), []), relay.reshape(const_4293.astype('uint64'), [13, 5, 2]), relay.reshape(var_4294.astype('float32'), [2, 2, 13]), relay.reshape(const_4295.astype('uint8'), [40,]), ), 6)
output = relay.Tuple([call_4271,call_4273,call_4291,const_4292,const_4293,var_4294,const_4295,])
output2 = relay.Tuple([call_4272,call_4274,call_4296,const_4292,const_4293,var_4294,const_4295,])
func_4303 = relay.Function([var_4294,], output)
mod['func_4303'] = func_4303
mod = relay.transform.InferType()(mod)
mutated_mod['func_4303'] = func_4303
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4304 = relay.var("var_4304", dtype = "float32", shape = (52,))#candidate|4304|(52,)|var|float32
func_4303_call = mutated_mod.get_global_var('func_4303')
call_4305 = func_4303_call(var_4304)
output = call_4305
func_4306 = relay.Function([var_4304], output)
mutated_mod['func_4306'] = func_4306
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2164_call = mod.get_global_var('func_2164')
func_2166_call = mutated_mod.get_global_var('func_2166')
call_4308 = func_2164_call()
call_4309 = func_2164_call()
output = relay.Tuple([call_4308,])
output2 = relay.Tuple([call_4309,])
func_4311 = relay.Function([], output)
mod['func_4311'] = func_4311
mod = relay.transform.InferType()(mod)
output = func_4311()
func_4312 = relay.Function([], output)
mutated_mod['func_4312'] = func_4312
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2450_call = mod.get_global_var('func_2450')
func_2451_call = mutated_mod.get_global_var('func_2451')
call_4335 = func_2450_call()
call_4336 = func_2450_call()
output = call_4335
output2 = call_4336
func_4353 = relay.Function([], output)
mod['func_4353'] = func_4353
mod = relay.transform.InferType()(mod)
output = func_4353()
func_4354 = relay.Function([], output)
mutated_mod['func_4354'] = func_4354
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2464_call = mod.get_global_var('func_2464')
func_2465_call = mutated_mod.get_global_var('func_2465')
call_4355 = func_2464_call()
call_4356 = func_2464_call()
var_4357 = relay.var("var_4357", dtype = "int8", shape = (8, 14, 2))#candidate|4357|(8, 14, 2)|var|int8
bop_4358 = relay.floor_divide(call_4355.astype('float32'), relay.reshape(var_4357.astype('float32'), relay.shape_of(call_4355))) # shape=(8, 14, 2)
bop_4361 = relay.floor_divide(call_4356.astype('float32'), relay.reshape(var_4357.astype('float32'), relay.shape_of(call_4356))) # shape=(8, 14, 2)
output = bop_4358
output2 = bop_4361
func_4372 = relay.Function([var_4357,], output)
mod['func_4372'] = func_4372
mod = relay.transform.InferType()(mod)
var_4373 = relay.var("var_4373", dtype = "int8", shape = (8, 14, 2))#candidate|4373|(8, 14, 2)|var|int8
output = func_4372(var_4373)
func_4374 = relay.Function([var_4373], output)
mutated_mod['func_4374'] = func_4374
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3568_call = mod.get_global_var('func_3568')
func_3569_call = mutated_mod.get_global_var('func_3569')
call_4383 = relay.TupleGetItem(func_3568_call(), 0)
call_4384 = relay.TupleGetItem(func_3569_call(), 0)
output = call_4383
output2 = call_4384
func_4395 = relay.Function([], output)
mod['func_4395'] = func_4395
mod = relay.transform.InferType()(mod)
output = func_4395()
func_4396 = relay.Function([], output)
mutated_mod['func_4396'] = func_4396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3333_call = mod.get_global_var('func_3333')
func_3335_call = mutated_mod.get_global_var('func_3335')
call_4399 = relay.TupleGetItem(func_3333_call(), 1)
call_4400 = relay.TupleGetItem(func_3335_call(), 1)
output = relay.Tuple([call_4399,])
output2 = relay.Tuple([call_4400,])
func_4413 = relay.Function([], output)
mod['func_4413'] = func_4413
mod = relay.transform.InferType()(mod)
mutated_mod['func_4413'] = func_4413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4413_call = mutated_mod.get_global_var('func_4413')
call_4414 = func_4413_call()
output = call_4414
func_4415 = relay.Function([], output)
mutated_mod['func_4415'] = func_4415
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2336_call = mod.get_global_var('func_2336')
func_2338_call = mutated_mod.get_global_var('func_2338')
call_4451 = relay.TupleGetItem(func_2336_call(), 0)
call_4452 = relay.TupleGetItem(func_2338_call(), 0)
output = relay.Tuple([call_4451,])
output2 = relay.Tuple([call_4452,])
func_4453 = relay.Function([], output)
mod['func_4453'] = func_4453
mod = relay.transform.InferType()(mod)
output = func_4453()
func_4454 = relay.Function([], output)
mutated_mod['func_4454'] = func_4454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2887_call = mod.get_global_var('func_2887')
func_2888_call = mutated_mod.get_global_var('func_2888')
call_4463 = func_2887_call()
call_4464 = func_2887_call()
func_3661_call = mod.get_global_var('func_3661')
func_3662_call = mutated_mod.get_global_var('func_3662')
call_4467 = relay.TupleGetItem(func_3661_call(), 2)
call_4468 = relay.TupleGetItem(func_3662_call(), 2)
output = relay.Tuple([call_4463,call_4467,])
output2 = relay.Tuple([call_4464,call_4468,])
func_4471 = relay.Function([], output)
mod['func_4471'] = func_4471
mod = relay.transform.InferType()(mod)
mutated_mod['func_4471'] = func_4471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4471_call = mutated_mod.get_global_var('func_4471')
call_4472 = func_4471_call()
output = call_4472
func_4473 = relay.Function([], output)
mutated_mod['func_4473'] = func_4473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2173_call = mod.get_global_var('func_2173')
func_2175_call = mutated_mod.get_global_var('func_2175')
call_4521 = func_2173_call()
call_4522 = func_2173_call()
output = relay.Tuple([call_4521,])
output2 = relay.Tuple([call_4522,])
func_4537 = relay.Function([], output)
mod['func_4537'] = func_4537
mod = relay.transform.InferType()(mod)
mutated_mod['func_4537'] = func_4537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4537_call = mutated_mod.get_global_var('func_4537')
call_4538 = func_4537_call()
output = call_4538
func_4539 = relay.Function([], output)
mutated_mod['func_4539'] = func_4539
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3122_call = mod.get_global_var('func_3122')
func_3123_call = mutated_mod.get_global_var('func_3123')
call_4540 = relay.TupleGetItem(func_3122_call(), 1)
call_4541 = relay.TupleGetItem(func_3123_call(), 1)
output = relay.Tuple([call_4540,])
output2 = relay.Tuple([call_4541,])
func_4557 = relay.Function([], output)
mod['func_4557'] = func_4557
mod = relay.transform.InferType()(mod)
mutated_mod['func_4557'] = func_4557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4557_call = mutated_mod.get_global_var('func_4557')
call_4558 = func_4557_call()
output = call_4558
func_4559 = relay.Function([], output)
mutated_mod['func_4559'] = func_4559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4395_call = mod.get_global_var('func_4395')
func_4396_call = mutated_mod.get_global_var('func_4396')
call_4567 = func_4395_call()
call_4568 = func_4395_call()
func_789_call = mod.get_global_var('func_789')
func_791_call = mutated_mod.get_global_var('func_791')
const_4584 = relay.const([-7.734914,2.126228,-4.169365,-2.809149,5.318446,3.700897,2.141267,-4.710249,3.725618,2.502770,-8.565743,-0.134545,-4.647495,4.781172,-2.863948,-2.016267,-9.447863,5.235582,-5.128289,-8.815254,-4.900422,-4.355222,4.705322,6.182631,8.296301,4.065947,9.594162,-0.688502,-9.749571,2.078688,-1.885841,8.385024,-0.556479,5.105881,-1.437640,-9.584989,4.052104,9.494862,8.394198,-6.011603,3.631843,-3.871724,3.708781,-6.523484,-4.570176,0.387597,6.730870,-0.937870,4.239207,5.935192,8.874261,-0.844258,-8.645047,7.759350,4.509904,-3.883401,9.363485,2.941626,0.613294,9.282033,9.537771,-2.481977,8.309713,-7.260875,7.670825,8.178602,0.438180,8.164257,3.154786,6.731346,-1.611632,0.892603,-5.994264,9.690427,-1.972601,-7.693904,0.708300,7.553064,2.429341,3.107131,3.178583,2.658054,-3.485015,-1.249493,6.493213,-0.787456,3.780871,8.649779,-8.006732,3.733023,3.655538,2.734391,-8.992920,-5.073263,-4.219647,-9.075654,-6.843578,2.297462,9.735366,-6.708622,8.091418,-7.970818,-1.397608,7.047100,-4.953750], dtype = "float32")#candidate|4584|(105,)|const|float32
call_4583 = relay.TupleGetItem(func_789_call(relay.reshape(const_4584.astype('float32'), [3, 7, 5])), 0)
call_4585 = relay.TupleGetItem(func_791_call(relay.reshape(const_4584.astype('float32'), [3, 7, 5])), 0)
output = relay.Tuple([call_4567,call_4583,const_4584,])
output2 = relay.Tuple([call_4568,call_4585,const_4584,])
func_4590 = relay.Function([], output)
mod['func_4590'] = func_4590
mod = relay.transform.InferType()(mod)
mutated_mod['func_4590'] = func_4590
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4590_call = mutated_mod.get_global_var('func_4590')
call_4591 = func_4590_call()
output = call_4591
func_4592 = relay.Function([], output)
mutated_mod['func_4592'] = func_4592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4453_call = mod.get_global_var('func_4453')
func_4454_call = mutated_mod.get_global_var('func_4454')
call_4680 = relay.TupleGetItem(func_4453_call(), 0)
call_4681 = relay.TupleGetItem(func_4454_call(), 0)
output = relay.Tuple([call_4680,])
output2 = relay.Tuple([call_4681,])
func_4687 = relay.Function([], output)
mod['func_4687'] = func_4687
mod = relay.transform.InferType()(mod)
mutated_mod['func_4687'] = func_4687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4687_call = mutated_mod.get_global_var('func_4687')
call_4688 = func_4687_call()
output = call_4688
func_4689 = relay.Function([], output)
mutated_mod['func_4689'] = func_4689
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4699 = relay.var("var_4699", dtype = "float32", shape = (7, 2, 13))#candidate|4699|(7, 2, 13)|var|float32
uop_4700 = relay.tan(var_4699.astype('float32')) # shape=(7, 2, 13)
uop_4704 = relay.log10(uop_4700.astype('float32')) # shape=(7, 2, 13)
func_4687_call = mod.get_global_var('func_4687')
func_4689_call = mutated_mod.get_global_var('func_4689')
call_4715 = relay.TupleGetItem(func_4687_call(), 0)
call_4716 = relay.TupleGetItem(func_4689_call(), 0)
bop_4725 = relay.maximum(uop_4704.astype('float64'), relay.reshape(uop_4700.astype('float64'), relay.shape_of(uop_4704))) # shape=(7, 2, 13)
output = relay.Tuple([call_4715,bop_4725,])
output2 = relay.Tuple([call_4716,bop_4725,])
func_4736 = relay.Function([var_4699,], output)
mod['func_4736'] = func_4736
mod = relay.transform.InferType()(mod)
var_4737 = relay.var("var_4737", dtype = "float32", shape = (7, 2, 13))#candidate|4737|(7, 2, 13)|var|float32
output = func_4736(var_4737)
func_4738 = relay.Function([var_4737], output)
mutated_mod['func_4738'] = func_4738
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4537_call = mod.get_global_var('func_4537')
func_4539_call = mutated_mod.get_global_var('func_4539')
call_4763 = relay.TupleGetItem(func_4537_call(), 0)
call_4764 = relay.TupleGetItem(func_4539_call(), 0)
func_1535_call = mod.get_global_var('func_1535')
func_1539_call = mutated_mod.get_global_var('func_1539')
const_4780 = relay.const([-5,10,-8,8,-3,7,-9,-9,-1,6,4,2,-2,-5,6,-10,6,8,10,10,-7,3,-9,7,-3,5,-6,5,9,10,-10,8,-2,-2,6,-6,-8,-9,1,-6,-8,-6,-9,-2,-9,-6,3,-6,2,-7,-7,-1,4,-3,-5,1,-1,-6,8,-9,-10,-7,-10,-10,-9,1,2,3,4,-2,9,10,10,10,-6,4,-5,1,-2,-8,-9,-8,-2,8,-9,3,-4,7,1,-10,6,4,-5,-7,-3,-9,-3,-3,8,-9,2,6,-6,-7,-10,-5,5,10,-2,8,-9,10,-1,-6,-6,7,-8,-1,-6,5,-9,2,10,3,-8,-9,-5,-8,-6,9,-1,10,-9,-6,-1,-1,-1,-4,7,-3,6,4,5,-2,-8,2,7,-9,-5,1,5,-8,-7,9,10,10,6,-9,-8,3,-2,-7,7,5,-10,9,8,-6,-10,10,-7,-7,-6,5,7,-10,-2,-8,-3,-2,9,2,9,-4,-1,10,-7,-2,-3,-7,-4,1,-5,7,-2,-3,-10,-8,-3,9,-9,3,-6,-6,-1,-9,-9,-2,-1,-2,-8,6,2,-1,8,-10,-1,-10,-7,5,-1,-4,7,5,-7,-3,-4,6,-10,-8,7,5,2,-4,-2,-8,3,3,9,8,-7,-2,-7,-6,5,7,-3,-9,-8,3,-2,-4,4,-5,-7,1,-3,4,1,-8,3,8,8,10,-10,7,-1,-7,8,8], dtype = "int64")#candidate|4780|(270,)|const|int64
var_4781 = relay.var("var_4781", dtype = "uint8", shape = (1, 40))#candidate|4781|(1, 40)|var|uint8
var_4782 = relay.var("var_4782", dtype = "bool", shape = (52,))#candidate|4782|(52,)|var|bool
call_4779 = relay.TupleGetItem(func_1535_call(relay.reshape(const_4780.astype('int64'), [270,]), relay.reshape(var_4781.astype('uint8'), [40,]), relay.reshape(var_4782.astype('bool'), [2, 2, 13]), ), 2)
call_4783 = relay.TupleGetItem(func_1539_call(relay.reshape(const_4780.astype('int64'), [270,]), relay.reshape(var_4781.astype('uint8'), [40,]), relay.reshape(var_4782.astype('bool'), [2, 2, 13]), ), 2)
uop_4788 = relay.tan(var_4781.astype('float64')) # shape=(1, 40)
output = relay.Tuple([call_4763,call_4779,const_4780,var_4782,uop_4788,])
output2 = relay.Tuple([call_4764,call_4783,const_4780,var_4782,uop_4788,])
func_4811 = relay.Function([var_4781,var_4782,], output)
mod['func_4811'] = func_4811
mod = relay.transform.InferType()(mod)
var_4812 = relay.var("var_4812", dtype = "uint8", shape = (1, 40))#candidate|4812|(1, 40)|var|uint8
var_4813 = relay.var("var_4813", dtype = "bool", shape = (52,))#candidate|4813|(52,)|var|bool
output = func_4811(var_4812,var_4813,)
func_4814 = relay.Function([var_4812,var_4813,], output)
mutated_mod['func_4814'] = func_4814
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4821 = relay.const([[[3,-2,9,-7,-4],[-3,-5,-8,-5,-6],[-5,-9,6,-9,8],[-1,-10,-9,-3,-9],[3,1,-3,1,-6]],[[-10,-6,9,9,-4],[-3,-5,-8,-9,3],[1,2,-6,-3,-4],[3,-1,3,10,-7],[8,-9,-1,7,9]],[[10,6,4,-8,8],[-5,5,10,5,1],[-6,9,10,-4,4],[7,-5,-7,-4,7],[6,-2,9,1,4]],[[3,-9,-5,4,5],[5,1,6,1,4],[3,2,-1,7,-5],[1,1,10,-8,7],[4,7,4,-3,3]],[[-4,7,2,-9,1],[-2,-1,2,-10,8],[6,-9,-7,-8,7],[10,-10,9,7,2],[1,-2,-8,-6,7]],[[-4,-7,-7,6,-9],[-7,-6,9,10,5],[-6,6,1,-2,-2],[4,-1,-1,-9,4],[-1,8,9,-5,5]],[[-10,8,-7,-2,9],[-8,-2,-6,-7,-9],[3,-3,9,8,2],[-4,4,-8,3,10],[4,5,-8,8,-5]],[[8,8,1,-5,1],[-4,-10,7,9,-10],[1,8,-9,-8,10],[5,-3,1,-10,5],[-4,4,-5,-3,-10]],[[3,6,-9,6,1],[3,5,-9,-2,-3],[-10,-3,-2,-7,3],[10,1,5,-1,9],[8,8,-8,10,-7]],[[4,-9,-4,-5,5],[-10,-4,-1,3,2],[3,-4,3,-9,-3],[-5,4,5,-4,8],[-10,4,-1,5,-8]],[[4,6,4,1,6],[10,10,-3,3,-7],[7,-1,-1,10,4],[2,-9,7,2,7],[-1,-7,-2,-8,-10]],[[-5,-2,1,-7,-1],[7,1,2,9,6],[-1,-4,10,1,-8],[4,-7,10,-2,-9],[7,6,1,-6,3]],[[-8,-10,1,8,-9],[2,-10,10,8,-8],[-6,-2,3,-2,6],[10,8,-6,-10,-10],[1,-2,2,2,7]],[[7,-6,-6,4,9],[-3,-6,1,-9,-6],[-1,4,9,-5,-8],[-2,-6,5,7,-1],[-1,-7,7,-9,-8]],[[7,2,-3,7,-2],[10,1,-2,1,-8],[-8,-9,6,-5,-2],[9,-2,-3,2,5],[-5,9,3,2,5]]], dtype = "int16")#candidate|4821|(15, 5, 5)|const|int16
var_4822 = relay.var("var_4822", dtype = "int16", shape = (15, 5, 5))#candidate|4822|(15, 5, 5)|var|int16
bop_4823 = relay.minimum(const_4821.astype('int16'), relay.reshape(var_4822.astype('int16'), relay.shape_of(const_4821))) # shape=(15, 5, 5)
func_3979_call = mod.get_global_var('func_3979')
func_3982_call = mutated_mod.get_global_var('func_3982')
var_4837 = relay.var("var_4837", dtype = "int8", shape = (224,))#candidate|4837|(224,)|var|int8
call_4836 = relay.TupleGetItem(func_3979_call(relay.reshape(var_4837.astype('int8'), [8, 14, 2])), 0)
call_4838 = relay.TupleGetItem(func_3982_call(relay.reshape(var_4837.astype('int8'), [8, 14, 2])), 0)
output = relay.Tuple([bop_4823,call_4836,var_4837,])
output2 = relay.Tuple([bop_4823,call_4838,var_4837,])
func_4839 = relay.Function([var_4822,var_4837,], output)
mod['func_4839'] = func_4839
mod = relay.transform.InferType()(mod)
var_4840 = relay.var("var_4840", dtype = "int16", shape = (15, 5, 5))#candidate|4840|(15, 5, 5)|var|int16
var_4841 = relay.var("var_4841", dtype = "int8", shape = (224,))#candidate|4841|(224,)|var|int8
output = func_4839(var_4840,var_4841,)
func_4842 = relay.Function([var_4840,var_4841,], output)
mutated_mod['func_4842'] = func_4842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4471_call = mod.get_global_var('func_4471')
func_4473_call = mutated_mod.get_global_var('func_4473')
call_4888 = relay.TupleGetItem(func_4471_call(), 1)
call_4889 = relay.TupleGetItem(func_4473_call(), 1)
func_4413_call = mod.get_global_var('func_4413')
func_4415_call = mutated_mod.get_global_var('func_4415')
call_4912 = relay.TupleGetItem(func_4413_call(), 0)
call_4913 = relay.TupleGetItem(func_4415_call(), 0)
const_4918 = relay.const([[[True,False,True,False],[False,False,True,True],[False,False,False,True],[True,True,True,True],[True,True,True,True],[True,False,True,True],[False,True,False,True],[False,False,True,True],[False,False,False,True],[True,True,False,True],[True,False,False,False],[False,True,False,True],[False,True,False,False],[True,True,True,True]],[[False,True,True,False],[True,False,False,False],[True,False,True,False],[True,True,True,True],[False,True,True,False],[False,True,True,False],[False,True,False,True],[False,False,True,False],[True,False,False,True],[False,False,True,True],[False,False,True,False],[True,False,True,True],[True,False,True,True],[False,False,False,False]],[[True,False,False,True],[False,True,True,False],[True,False,True,True],[False,False,True,True],[False,False,True,True],[True,False,True,False],[False,False,False,False],[True,False,True,False],[False,True,False,True],[False,True,True,True],[True,False,False,False],[False,True,True,False],[False,False,True,True],[False,False,True,False]]], dtype = "bool")#candidate|4918|(3, 14, 4)|const|bool
bop_4919 = relay.add(call_4912.astype('int8'), relay.reshape(const_4918.astype('int8'), relay.shape_of(call_4912))) # shape=(3, 14, 4)
bop_4922 = relay.add(call_4913.astype('int8'), relay.reshape(const_4918.astype('int8'), relay.shape_of(call_4913))) # shape=(3, 14, 4)
uop_4925 = relay.asinh(const_4918.astype('float32')) # shape=(3, 14, 4)
func_2799_call = mod.get_global_var('func_2799')
func_2801_call = mutated_mod.get_global_var('func_2801')
call_4927 = relay.TupleGetItem(func_2799_call(), 0)
call_4928 = relay.TupleGetItem(func_2801_call(), 0)
output = relay.Tuple([call_4888,bop_4919,uop_4925,call_4927,])
output2 = relay.Tuple([call_4889,bop_4922,uop_4925,call_4928,])
func_4929 = relay.Function([], output)
mod['func_4929'] = func_4929
mod = relay.transform.InferType()(mod)
mutated_mod['func_4929'] = func_4929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4929_call = mutated_mod.get_global_var('func_4929')
call_4930 = func_4929_call()
output = call_4930
func_4931 = relay.Function([], output)
mutated_mod['func_4931'] = func_4931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3333_call = mod.get_global_var('func_3333')
func_3335_call = mutated_mod.get_global_var('func_3335')
call_4959 = relay.TupleGetItem(func_3333_call(), 1)
call_4960 = relay.TupleGetItem(func_3335_call(), 1)
output = call_4959
output2 = call_4960
func_4970 = relay.Function([], output)
mod['func_4970'] = func_4970
mod = relay.transform.InferType()(mod)
output = func_4970()
func_4971 = relay.Function([], output)
mutated_mod['func_4971'] = func_4971
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2257_call = mod.get_global_var('func_2257')
func_2258_call = mutated_mod.get_global_var('func_2258')
call_5098 = relay.TupleGetItem(func_2257_call(), 0)
call_5099 = relay.TupleGetItem(func_2258_call(), 0)
output = call_5098
output2 = call_5099
func_5110 = relay.Function([], output)
mod['func_5110'] = func_5110
mod = relay.transform.InferType()(mod)
output = func_5110()
func_5111 = relay.Function([], output)
mutated_mod['func_5111'] = func_5111
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5140 = relay.var("var_5140", dtype = "float32", shape = (8, 15, 7))#candidate|5140|(8, 15, 7)|var|float32
uop_5141 = relay.erf(var_5140.astype('float32')) # shape=(8, 15, 7)
output = relay.Tuple([uop_5141,])
output2 = relay.Tuple([uop_5141,])
func_5144 = relay.Function([var_5140,], output)
mod['func_5144'] = func_5144
mod = relay.transform.InferType()(mod)
mutated_mod['func_5144'] = func_5144
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5145 = relay.var("var_5145", dtype = "float32", shape = (8, 15, 7))#candidate|5145|(8, 15, 7)|var|float32
func_5144_call = mutated_mod.get_global_var('func_5144')
call_5146 = func_5144_call(var_5145)
output = call_5146
func_5147 = relay.Function([var_5145], output)
mutated_mod['func_5147'] = func_5147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4353_call = mod.get_global_var('func_4353')
func_4354_call = mutated_mod.get_global_var('func_4354')
call_5170 = func_4353_call()
call_5171 = func_4353_call()
func_31_call = mod.get_global_var('func_31')
func_34_call = mutated_mod.get_global_var('func_34')
var_5206 = relay.var("var_5206", dtype = "uint8", shape = (40,))#candidate|5206|(40,)|var|uint8
call_5205 = relay.TupleGetItem(func_31_call(relay.reshape(var_5206.astype('uint8'), [5, 4, 2]), relay.reshape(var_5206.astype('uint8'), [5, 4, 2]), ), 0)
call_5207 = relay.TupleGetItem(func_34_call(relay.reshape(var_5206.astype('uint8'), [5, 4, 2]), relay.reshape(var_5206.astype('uint8'), [5, 4, 2]), ), 0)
func_4372_call = mod.get_global_var('func_4372')
func_4374_call = mutated_mod.get_global_var('func_4374')
call_5212 = func_4372_call(relay.reshape(call_5170.astype('int8'), [8, 14, 2]))
call_5213 = func_4372_call(relay.reshape(call_5170.astype('int8'), [8, 14, 2]))
func_4557_call = mod.get_global_var('func_4557')
func_4559_call = mutated_mod.get_global_var('func_4559')
call_5214 = relay.TupleGetItem(func_4557_call(), 0)
call_5215 = relay.TupleGetItem(func_4559_call(), 0)
func_2022_call = mod.get_global_var('func_2022')
func_2028_call = mutated_mod.get_global_var('func_2028')
var_5218 = relay.var("var_5218", dtype = "uint64", shape = ())#candidate|5218|()|var|uint64
var_5219 = relay.var("var_5219", dtype = "uint64", shape = (130,))#candidate|5219|(130,)|var|uint64
const_5220 = relay.const([1.020663,-8.629831,0.633624,-1.776846,-4.005310,-0.369078,-9.119002,-0.135912,8.110147,5.427634,7.813978,1.706223,0.584019,5.865445,0.386053,-9.819418,-6.752188,0.225445,1.591711,-2.902556,0.568633,9.836601,9.799070,-5.593692,-3.849157,-5.443547,9.635222,1.585939,-9.450683,9.975351,1.013018,-4.301165,-3.648462,-1.511200,8.199195,8.576289,4.900862,2.468225,-6.039596,6.929624,8.508632,-7.998259,-5.012001,4.677526,3.815692,-1.989928,-4.769571,-9.402173,1.160134,-0.073525,2.507468,2.409043], dtype = "float32")#candidate|5220|(52,)|const|float32
call_5217 = relay.TupleGetItem(func_2022_call(relay.reshape(var_5218.astype('uint64'), []), relay.reshape(var_5219.astype('uint64'), [13, 5, 2]), relay.reshape(const_5220.astype('float32'), [2, 2, 13]), relay.reshape(var_5206.astype('uint8'), [40,]), ), 1)
call_5221 = relay.TupleGetItem(func_2028_call(relay.reshape(var_5218.astype('uint64'), []), relay.reshape(var_5219.astype('uint64'), [13, 5, 2]), relay.reshape(const_5220.astype('float32'), [2, 2, 13]), relay.reshape(var_5206.astype('uint8'), [40,]), ), 1)
func_3333_call = mod.get_global_var('func_3333')
func_3335_call = mutated_mod.get_global_var('func_3335')
call_5224 = relay.TupleGetItem(func_3333_call(), 2)
call_5225 = relay.TupleGetItem(func_3335_call(), 2)
func_2582_call = mod.get_global_var('func_2582')
func_2584_call = mutated_mod.get_global_var('func_2584')
call_5235 = relay.TupleGetItem(func_2582_call(), 2)
call_5236 = relay.TupleGetItem(func_2584_call(), 2)
output = relay.Tuple([call_5170,call_5205,var_5206,call_5212,call_5214,call_5217,var_5218,var_5219,const_5220,call_5224,call_5235,])
output2 = relay.Tuple([call_5171,call_5207,var_5206,call_5213,call_5215,call_5221,var_5218,var_5219,const_5220,call_5225,call_5236,])
func_5241 = relay.Function([var_5206,var_5218,var_5219,], output)
mod['func_5241'] = func_5241
mod = relay.transform.InferType()(mod)
mutated_mod['func_5241'] = func_5241
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5241_call = mutated_mod.get_global_var('func_5241')
var_5243 = relay.var("var_5243", dtype = "uint8", shape = (40,))#candidate|5243|(40,)|var|uint8
var_5244 = relay.var("var_5244", dtype = "uint64", shape = ())#candidate|5244|()|var|uint64
var_5245 = relay.var("var_5245", dtype = "uint64", shape = (130,))#candidate|5245|(130,)|var|uint64
call_5242 = func_5241_call(var_5243,var_5244,var_5245,)
output = call_5242
func_5246 = relay.Function([var_5243,var_5244,var_5245,], output)
mutated_mod['func_5246'] = func_5246
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5327 = relay.var("var_5327", dtype = "float32", shape = (5, 16, 13))#candidate|5327|(5, 16, 13)|var|float32
uop_5328 = relay.asinh(var_5327.astype('float32')) # shape=(5, 16, 13)
func_3184_call = mod.get_global_var('func_3184')
func_3187_call = mutated_mod.get_global_var('func_3187')
var_5332 = relay.var("var_5332", dtype = "float32", shape = (462,))#candidate|5332|(462,)|var|float32
call_5331 = func_3184_call(relay.reshape(var_5332.astype('float32'), [11, 3, 14]))
call_5333 = func_3184_call(relay.reshape(var_5332.astype('float32'), [11, 3, 14]))
bop_5349 = relay.right_shift(call_5331.astype('int64'), relay.reshape(var_5332.astype('int64'), relay.shape_of(call_5331))) # shape=(11, 3, 14)
bop_5352 = relay.right_shift(call_5333.astype('int64'), relay.reshape(var_5332.astype('int64'), relay.shape_of(call_5333))) # shape=(11, 3, 14)
func_504_call = mod.get_global_var('func_504')
func_509_call = mutated_mod.get_global_var('func_509')
const_5354 = relay.const(-6, dtype = "int64")#candidate|5354|()|const|int64
var_5355 = relay.var("var_5355", dtype = "int64", shape = (270,))#candidate|5355|(270,)|var|int64
var_5356 = relay.var("var_5356", dtype = "float64", shape = (52, 1))#candidate|5356|(52, 1)|var|float64
const_5357 = relay.const([8,-10,-4,2,5,10,-7,-10,3,-6,-5,-4,-7,-7,-9,-10,4,6,5,5,7,4,6,-2,1,6,10,6,-6,4,-3,-2,6,-5,9,1,-7,9,8,-4], dtype = "uint8")#candidate|5357|(40,)|const|uint8
call_5353 = relay.TupleGetItem(func_504_call(relay.reshape(const_5354.astype('int64'), []), relay.reshape(var_5355.astype('int64'), [15, 9, 2]), relay.reshape(var_5356.astype('float64'), [52,]), relay.reshape(const_5357.astype('uint8'), [40,]), ), 2)
call_5358 = relay.TupleGetItem(func_509_call(relay.reshape(const_5354.astype('int64'), []), relay.reshape(var_5355.astype('int64'), [15, 9, 2]), relay.reshape(var_5356.astype('float64'), [52,]), relay.reshape(const_5357.astype('uint8'), [40,]), ), 2)
output = relay.Tuple([uop_5328,bop_5349,call_5353,const_5354,var_5355,var_5356,const_5357,])
output2 = relay.Tuple([uop_5328,bop_5352,call_5358,const_5354,var_5355,var_5356,const_5357,])
func_5363 = relay.Function([var_5327,var_5332,var_5355,var_5356,], output)
mod['func_5363'] = func_5363
mod = relay.transform.InferType()(mod)
mutated_mod['func_5363'] = func_5363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5363_call = mutated_mod.get_global_var('func_5363')
var_5365 = relay.var("var_5365", dtype = "float32", shape = (5, 16, 13))#candidate|5365|(5, 16, 13)|var|float32
var_5366 = relay.var("var_5366", dtype = "float32", shape = (462,))#candidate|5366|(462,)|var|float32
var_5367 = relay.var("var_5367", dtype = "int64", shape = (270,))#candidate|5367|(270,)|var|int64
var_5368 = relay.var("var_5368", dtype = "float64", shape = (52, 1))#candidate|5368|(52, 1)|var|float64
call_5364 = func_5363_call(var_5365,var_5366,var_5367,var_5368,)
output = call_5364
func_5369 = relay.Function([var_5365,var_5366,var_5367,var_5368,], output)
mutated_mod['func_5369'] = func_5369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3097_call = mod.get_global_var('func_3097')
func_3099_call = mutated_mod.get_global_var('func_3099')
call_5376 = func_3097_call()
call_5377 = func_3097_call()
output = call_5376
output2 = call_5377
func_5381 = relay.Function([], output)
mod['func_5381'] = func_5381
mod = relay.transform.InferType()(mod)
output = func_5381()
func_5382 = relay.Function([], output)
mutated_mod['func_5382'] = func_5382
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2164_call = mod.get_global_var('func_2164')
func_2166_call = mutated_mod.get_global_var('func_2166')
call_5383 = func_2164_call()
call_5384 = func_2164_call()
func_2682_call = mod.get_global_var('func_2682')
func_2684_call = mutated_mod.get_global_var('func_2684')
call_5403 = func_2682_call()
call_5404 = func_2682_call()
output = relay.Tuple([call_5383,call_5403,])
output2 = relay.Tuple([call_5384,call_5404,])
func_5405 = relay.Function([], output)
mod['func_5405'] = func_5405
mod = relay.transform.InferType()(mod)
mutated_mod['func_5405'] = func_5405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5405_call = mutated_mod.get_global_var('func_5405')
call_5406 = func_5405_call()
output = call_5406
func_5407 = relay.Function([], output)
mutated_mod['func_5407'] = func_5407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2887_call = mod.get_global_var('func_2887')
func_2888_call = mutated_mod.get_global_var('func_2888')
call_5458 = func_2887_call()
call_5459 = func_2887_call()
output = relay.Tuple([call_5458,])
output2 = relay.Tuple([call_5459,])
func_5474 = relay.Function([], output)
mod['func_5474'] = func_5474
mod = relay.transform.InferType()(mod)
output = func_5474()
func_5475 = relay.Function([], output)
mutated_mod['func_5475'] = func_5475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3568_call = mod.get_global_var('func_3568')
func_3569_call = mutated_mod.get_global_var('func_3569')
call_5492 = relay.TupleGetItem(func_3568_call(), 2)
call_5493 = relay.TupleGetItem(func_3569_call(), 2)
output = relay.Tuple([call_5492,])
output2 = relay.Tuple([call_5493,])
func_5495 = relay.Function([], output)
mod['func_5495'] = func_5495
mod = relay.transform.InferType()(mod)
mutated_mod['func_5495'] = func_5495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5495_call = mutated_mod.get_global_var('func_5495')
call_5496 = func_5495_call()
output = call_5496
func_5497 = relay.Function([], output)
mutated_mod['func_5497'] = func_5497
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5405_call = mod.get_global_var('func_5405')
func_5407_call = mutated_mod.get_global_var('func_5407')
call_5517 = relay.TupleGetItem(func_5405_call(), 1)
call_5518 = relay.TupleGetItem(func_5407_call(), 1)
func_2943_call = mod.get_global_var('func_2943')
func_2944_call = mutated_mod.get_global_var('func_2944')
call_5525 = func_2943_call()
call_5526 = func_2943_call()
uop_5541 = relay.sin(call_5525.astype('float64')) # shape=(8, 14, 2)
uop_5543 = relay.sin(call_5526.astype('float64')) # shape=(8, 14, 2)
func_1559_call = mod.get_global_var('func_1559')
func_1561_call = mutated_mod.get_global_var('func_1561')
call_5545 = relay.TupleGetItem(func_1559_call(), 0)
call_5546 = relay.TupleGetItem(func_1561_call(), 0)
output = relay.Tuple([call_5517,uop_5541,call_5545,])
output2 = relay.Tuple([call_5518,uop_5543,call_5546,])
func_5547 = relay.Function([], output)
mod['func_5547'] = func_5547
mod = relay.transform.InferType()(mod)
mutated_mod['func_5547'] = func_5547
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5547_call = mutated_mod.get_global_var('func_5547')
call_5548 = func_5547_call()
output = call_5548
func_5549 = relay.Function([], output)
mutated_mod['func_5549'] = func_5549
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5405_call = mod.get_global_var('func_5405')
func_5407_call = mutated_mod.get_global_var('func_5407')
call_5563 = relay.TupleGetItem(func_5405_call(), 1)
call_5564 = relay.TupleGetItem(func_5407_call(), 1)
func_5547_call = mod.get_global_var('func_5547')
func_5549_call = mutated_mod.get_global_var('func_5549')
call_5567 = relay.TupleGetItem(func_5547_call(), 0)
call_5568 = relay.TupleGetItem(func_5549_call(), 0)
output = relay.Tuple([call_5563,call_5567,])
output2 = relay.Tuple([call_5564,call_5568,])
func_5570 = relay.Function([], output)
mod['func_5570'] = func_5570
mod = relay.transform.InferType()(mod)
output = func_5570()
func_5571 = relay.Function([], output)
mutated_mod['func_5571'] = func_5571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4929_call = mod.get_global_var('func_4929')
func_4931_call = mutated_mod.get_global_var('func_4931')
call_5656 = relay.TupleGetItem(func_4929_call(), 1)
call_5657 = relay.TupleGetItem(func_4931_call(), 1)
func_4970_call = mod.get_global_var('func_4970')
func_4971_call = mutated_mod.get_global_var('func_4971')
call_5667 = func_4970_call()
call_5668 = func_4970_call()
func_2682_call = mod.get_global_var('func_2682')
func_2684_call = mutated_mod.get_global_var('func_2684')
call_5673 = func_2682_call()
call_5674 = func_2682_call()
func_4839_call = mod.get_global_var('func_4839')
func_4842_call = mutated_mod.get_global_var('func_4842')
var_5680 = relay.var("var_5680", dtype = "int16", shape = (5, 75))#candidate|5680|(5, 75)|var|int16
call_5679 = relay.TupleGetItem(func_4839_call(relay.reshape(var_5680.astype('int16'), [15, 5, 5]), relay.reshape(call_5673.astype('int8'), [224,]), ), 1)
call_5681 = relay.TupleGetItem(func_4842_call(relay.reshape(var_5680.astype('int16'), [15, 5, 5]), relay.reshape(call_5673.astype('int8'), [224,]), ), 1)
func_2682_call = mod.get_global_var('func_2682')
func_2684_call = mutated_mod.get_global_var('func_2684')
call_5686 = func_2682_call()
call_5687 = func_2682_call()
output = relay.Tuple([call_5656,call_5667,call_5673,call_5679,var_5680,call_5686,])
output2 = relay.Tuple([call_5657,call_5668,call_5674,call_5681,var_5680,call_5687,])
func_5688 = relay.Function([var_5680,], output)
mod['func_5688'] = func_5688
mod = relay.transform.InferType()(mod)
mutated_mod['func_5688'] = func_5688
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5689 = relay.var("var_5689", dtype = "int16", shape = (5, 75))#candidate|5689|(5, 75)|var|int16
func_5688_call = mutated_mod.get_global_var('func_5688')
call_5690 = func_5688_call(var_5689)
output = call_5690
func_5691 = relay.Function([var_5689], output)
mutated_mod['func_5691'] = func_5691
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5703 = relay.var("var_5703", dtype = "int32", shape = (6, 5, 13))#candidate|5703|(6, 5, 13)|var|int32
const_5704 = relay.const([[[-9,9,-6,3,6,-10,1,2,2,3,-10,-8,5],[5,-10,-6,-9,-10,9,-9,-7,-4,8,-8,-10,10],[2,-8,-4,5,-8,-4,-5,4,-2,-2,3,-9,2],[1,-10,1,1,-1,2,8,6,-9,-8,8,5,1],[4,6,7,9,8,-1,9,3,-5,-3,3,-3,-2]],[[-3,9,-2,-1,-10,-8,8,-8,5,9,1,9,5],[4,4,-7,3,-10,10,5,-2,6,9,6,-1,1],[9,4,1,1,5,4,-3,-5,6,10,3,9,-10],[-5,10,-1,-8,-4,-4,-6,-1,9,5,-9,-3,10],[-7,-7,3,-5,10,3,-4,6,-2,-9,3,8,-1]],[[8,8,-10,-6,-9,1,-4,-2,6,6,6,-4,-10],[2,-4,7,-6,9,-9,5,4,3,-6,6,3,-3],[7,-3,-6,-5,7,-2,6,-1,6,4,-1,-9,4],[-8,-7,-5,2,-1,10,-9,-9,-9,2,-1,-5,2],[2,4,7,2,-5,-8,6,5,5,-4,-5,-1,-3]],[[7,9,-4,1,6,10,-3,8,3,-1,9,-10,-2],[6,-4,-8,-6,2,-8,8,2,4,6,-7,6,-5],[3,8,2,7,-10,7,-1,-6,4,3,-5,-1,8],[7,-3,-1,-10,10,-10,8,-3,7,-5,-1,8,-5],[10,1,-2,-6,-3,-1,-3,-4,7,4,-10,6,-6]],[[4,-2,5,5,-1,-6,-1,-1,1,1,-8,9,2],[7,-5,-2,4,-8,-7,-9,-9,5,-4,-10,2,-10],[4,6,-1,2,3,4,10,-10,-6,-5,-2,5,-9],[-10,-10,3,2,-8,2,8,5,-5,-8,2,-4,1],[9,1,-2,-9,3,-6,3,7,-5,-3,9,-7,-4]],[[2,-8,-3,6,-5,7,1,-5,-5,1,6,-9,8],[6,4,6,8,-9,-3,5,5,9,1,3,6,10],[-1,10,6,7,-8,7,1,6,-1,1,2,4,-5],[1,-2,-5,9,-6,-3,-4,8,-4,-9,2,-1,8],[2,-9,8,10,1,6,-1,5,-5,-5,-2,3,-1]]], dtype = "int32")#candidate|5704|(6, 5, 13)|const|int32
bop_5705 = relay.minimum(var_5703.astype('int32'), relay.reshape(const_5704.astype('int32'), relay.shape_of(var_5703))) # shape=(6, 5, 13)
func_5495_call = mod.get_global_var('func_5495')
func_5497_call = mutated_mod.get_global_var('func_5497')
call_5721 = relay.TupleGetItem(func_5495_call(), 0)
call_5722 = relay.TupleGetItem(func_5497_call(), 0)
func_2799_call = mod.get_global_var('func_2799')
func_2801_call = mutated_mod.get_global_var('func_2801')
call_5732 = relay.TupleGetItem(func_2799_call(), 0)
call_5733 = relay.TupleGetItem(func_2801_call(), 0)
output = relay.Tuple([bop_5705,call_5721,call_5732,])
output2 = relay.Tuple([bop_5705,call_5722,call_5733,])
func_5737 = relay.Function([var_5703,], output)
mod['func_5737'] = func_5737
mod = relay.transform.InferType()(mod)
mutated_mod['func_5737'] = func_5737
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5738 = relay.var("var_5738", dtype = "int32", shape = (6, 5, 13))#candidate|5738|(6, 5, 13)|var|int32
func_5737_call = mutated_mod.get_global_var('func_5737')
call_5739 = func_5737_call(var_5738)
output = call_5739
func_5740 = relay.Function([var_5738], output)
mutated_mod['func_5740'] = func_5740
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4471_call = mod.get_global_var('func_4471')
func_4473_call = mutated_mod.get_global_var('func_4473')
call_5749 = relay.TupleGetItem(func_4471_call(), 1)
call_5750 = relay.TupleGetItem(func_4473_call(), 1)
output = relay.Tuple([call_5749,])
output2 = relay.Tuple([call_5750,])
func_5760 = relay.Function([], output)
mod['func_5760'] = func_5760
mod = relay.transform.InferType()(mod)
mutated_mod['func_5760'] = func_5760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5760_call = mutated_mod.get_global_var('func_5760')
call_5761 = func_5760_call()
output = call_5761
func_5762 = relay.Function([], output)
mutated_mod['func_5762'] = func_5762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5474_call = mod.get_global_var('func_5474')
func_5475_call = mutated_mod.get_global_var('func_5475')
call_5763 = relay.TupleGetItem(func_5474_call(), 0)
call_5764 = relay.TupleGetItem(func_5475_call(), 0)
func_4839_call = mod.get_global_var('func_4839')
func_4842_call = mutated_mod.get_global_var('func_4842')
var_5770 = relay.var("var_5770", dtype = "int16", shape = (375,))#candidate|5770|(375,)|var|int16
call_5769 = relay.TupleGetItem(func_4839_call(relay.reshape(var_5770.astype('int16'), [15, 5, 5]), relay.reshape(call_5763.astype('int8'), [224,]), ), 0)
call_5771 = relay.TupleGetItem(func_4842_call(relay.reshape(var_5770.astype('int16'), [15, 5, 5]), relay.reshape(call_5763.astype('int8'), [224,]), ), 0)
func_1535_call = mod.get_global_var('func_1535')
func_1539_call = mutated_mod.get_global_var('func_1539')
const_5776 = relay.const([-2,-4,-7,-9,-7,2,-9,6,7,-2,-3,6,-9,-4,-8,5,-7,6,8,-5,-2,-10,9,8,7,7,-2,-9,-5,-1,1,-10,-5,-2,-6,9,-3,-8,4,-10,-7,-10,-4,-9,-4,-10,8,-3,10,7,4,1,-4,2,6,-8,3,-1,-9,-3,-3,-9,-7,-2,-10,3,5,-1,-5,-7,-7,4,-5,6,-5,6,-4,-7,-9,-9,9,1,8,-5,7,3,-8,-5,-2,-8,1,-3,1,7,-2,-7,8,7,1,8,3,-1,8,6,6,5,8,-2,1,-8,-8,5,4,4,3,3,-3,9,-2,-1,8,6,7,6,-9,-10,7,5,-9,-9,10,10,-8,-5,5,9,-4,-1,4,9,-2,-2,-8,2,-5,8,3,-9,9,1,9,-7,-4,-6,-6,4,5,8,-5,9,-9,5,6,-3,7,-9,4,3,-4,6,3,-9,6,-4,-8,-2,3,-1,3,-6,-7,-9,10,-9,-1,6,7,-4,5,-5,-10,-9,4,2,3,-8,-10,5,8,-4,-1,5,-8,-10,-5,-5,1,8,4,-3,-7,-1,-7,-6,-10,-8,-3,-8,9,5,4,9,-3,-3,6,-8,-6,-9,-5,1,-7,6,-9,-10,-4,-4,-4,6,-1,-6,4,9,3,6,-5,3,6,-2,6,7,9,-10,4,2,-6,2,4,-1,-1,5,6,10,7,-10,7,5,-7,-1,-3,-6], dtype = "int64")#candidate|5776|(270,)|const|int64
const_5777 = relay.const([[-7,-1],[4,8],[6,-2],[-5,7],[10,3],[-1,7],[-10,-10],[3,10],[-2,-10],[-10,8],[6,-6],[4,8],[-9,-3],[2,6],[1,2],[6,1],[-3,-6],[1,-1],[-5,-6],[10,5]], dtype = "uint8")#candidate|5777|(20, 2)|const|uint8
const_5778 = relay.const([True,True,True,False,True,True,False,True,True,True,True,True,False,True,False,True,True,True,False,True,False,False,False,True,False,False,False,False,False,False,False,True,True,True,True,False,False,True,True,True,True,True,False,True,False,True,False,True,False,False,False,False], dtype = "bool")#candidate|5778|(52,)|const|bool
call_5775 = relay.TupleGetItem(func_1535_call(relay.reshape(const_5776.astype('int64'), [270,]), relay.reshape(const_5777.astype('uint8'), [40,]), relay.reshape(const_5778.astype('bool'), [2, 2, 13]), ), 2)
call_5779 = relay.TupleGetItem(func_1539_call(relay.reshape(const_5776.astype('int64'), [270,]), relay.reshape(const_5777.astype('uint8'), [40,]), relay.reshape(const_5778.astype('bool'), [2, 2, 13]), ), 2)
output = relay.Tuple([call_5763,call_5769,var_5770,call_5775,const_5776,const_5777,const_5778,])
output2 = relay.Tuple([call_5764,call_5771,var_5770,call_5779,const_5776,const_5777,const_5778,])
func_5790 = relay.Function([var_5770,], output)
mod['func_5790'] = func_5790
mod = relay.transform.InferType()(mod)
var_5791 = relay.var("var_5791", dtype = "int16", shape = (375,))#candidate|5791|(375,)|var|int16
output = func_5790(var_5791)
func_5792 = relay.Function([var_5791], output)
mutated_mod['func_5792'] = func_5792
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5812 = relay.const([[[-9.456245,6.621896,-4.583248,-2.678017,-4.437928,-8.496336,9.233800,0.368502,0.328778],[6.056430,5.832483,-8.052215,6.327967,-5.018315,-7.980541,-2.397978,-1.090778,7.304729],[8.281449,2.641425,-6.205082,2.878477,-8.177177,9.067810,-1.774314,3.371033,-2.630099],[-3.465624,0.621085,-3.415866,-7.858286,-8.484378,5.063640,-7.963263,0.499277,-2.496209],[6.351021,6.542181,3.229710,3.528509,0.306737,5.524461,-4.672762,-2.728805,-8.556508],[0.249702,6.476529,9.564107,3.738234,6.482608,-9.159418,-7.344025,9.373481,2.361993],[-3.222793,-2.583860,1.450381,1.533552,-2.478997,5.897446,6.591239,6.132316,6.208828],[1.115788,-7.490714,7.781734,-6.592032,-9.858196,-6.482591,-0.881489,-5.881805,-7.238731],[-0.444442,-4.526490,3.408694,-5.102159,-5.385065,7.772653,-4.507802,9.002361,4.519223]],[[1.048088,-9.599367,-0.091482,1.662533,-8.904722,1.358572,1.147222,-8.303499,-5.677008],[-0.515809,-3.597853,4.366834,-8.617477,-0.752987,-0.157719,-8.701561,-8.362610,-5.177830],[0.186222,2.892546,6.058644,7.775676,4.587735,-9.530736,2.411664,-8.857266,-5.200757],[-2.738346,3.226418,-5.774981,-8.773822,-8.947179,6.076799,2.986182,-1.969807,-7.271149],[-0.929373,7.240111,-8.142203,9.660575,-6.683886,7.639452,1.733084,7.253450,4.912442],[1.127510,-1.234901,-6.471198,-0.621359,2.624251,-3.321921,-1.919737,1.313284,-2.227950],[-7.043364,1.215544,9.302173,8.488542,-0.986566,-3.793138,-0.958940,-9.338572,2.500673],[-9.973424,-2.537099,-4.646976,-3.225393,5.955208,-0.888123,3.100519,-2.926989,3.728795],[3.040580,-5.085472,8.756871,6.174306,-0.315484,7.869164,-4.091013,6.103040,7.238906]],[[-3.866003,0.474768,0.453072,4.986646,-8.452583,1.394866,-6.177887,-9.208679,3.616202],[6.350113,9.666861,-5.922244,5.295947,-1.106128,4.292851,-4.251481,4.928918,-5.979077],[-1.199271,4.068538,7.971835,-8.539788,-1.506695,-2.587851,5.872455,-1.655839,-7.840818],[6.927848,-2.503936,-6.723340,1.284409,6.775755,-4.394919,3.245763,2.906864,2.418444],[3.101525,-6.072065,-0.408735,3.260317,-9.561706,-7.462783,-2.357905,-6.964008,-0.811998],[9.761292,-8.367987,-2.811200,-3.470507,9.977794,0.015461,-2.625170,-1.009962,-9.145681],[8.097527,-6.158649,5.272732,-5.853356,-5.421047,-6.199211,-4.210838,-3.079522,-5.333701],[6.435170,-5.854643,6.628315,-1.309247,2.112258,-7.836315,2.021963,2.471059,-5.048204],[3.366040,5.157289,2.356356,-1.034401,4.578574,-5.269045,0.271954,-3.243279,-2.828966]],[[8.261870,1.673381,-1.000724,-5.469646,9.844789,5.643218,5.026639,0.819504,2.859285],[-3.903022,-6.783887,-5.878363,-0.135706,-3.237377,-5.603759,-5.684616,1.798136,-5.992882],[7.805328,-4.592441,-3.017355,-7.937411,-7.191955,-6.403115,2.327773,1.209209,-5.213684],[-3.510210,9.223013,6.266810,-0.491333,-3.598753,2.317478,7.894747,9.979606,-3.347006],[3.619783,3.010003,-5.883186,4.058708,8.819422,6.220570,9.770807,-3.918301,-5.343756],[-0.619671,2.329120,5.203034,3.156502,4.981349,-0.313287,-8.522789,3.827336,9.968647],[-1.935472,8.403001,8.802898,2.833839,-1.303772,4.135814,-4.494908,0.325835,-1.969145],[-0.766293,3.840845,4.138602,1.047726,-3.143983,6.246231,-1.540977,-2.855118,6.873750],[-1.553470,-0.948099,-2.986810,-4.612140,7.202253,-7.146450,-3.055298,8.300727,0.311922]],[[2.748569,0.119744,5.617574,8.887274,-4.129482,5.243705,9.283140,-1.464648,-6.077547],[4.800756,2.095999,9.237493,8.577375,0.303259,6.661556,6.483849,7.920833,-3.364058],[9.975990,9.086833,-5.857857,-1.755278,-5.523137,6.260357,3.914270,0.695094,-0.777179],[8.177035,-6.420096,-1.021346,5.020720,-5.171094,-7.346995,8.460761,-3.374428,1.858829],[0.109259,-0.873058,1.437643,-9.017374,2.263845,9.047197,-1.240849,8.923973,9.193056],[5.694289,8.928684,-3.918434,-4.321840,8.136639,-0.826731,9.801620,-0.121242,5.458868],[-2.864267,2.046606,-3.403284,8.655224,0.400411,8.990819,-3.692147,8.233632,3.132620],[-0.796563,9.166103,-3.679517,-2.688975,3.932830,-5.073512,-2.540572,-2.506102,-5.679484],[9.470718,-7.687359,-8.455001,3.816161,-6.691108,-3.724767,-5.712178,6.575269,-0.357348]],[[4.378686,-6.434090,-4.884923,-4.326856,1.097877,-0.397502,5.616225,4.035732,-3.059539],[9.835412,-1.797331,-6.436524,5.125639,7.754933,-0.930693,4.807923,3.883522,-9.010924],[-7.115053,-3.453821,7.009476,8.338686,-1.982674,-0.909665,-7.023790,3.768239,7.328686],[8.319229,-9.549470,-3.414925,-9.274535,8.633773,3.924235,3.469949,-3.863244,6.852926],[-1.514694,-7.836767,1.561883,5.944200,-8.736568,-8.128504,-2.551200,1.243129,6.312292],[9.726925,9.059987,2.579612,-7.545322,-5.076978,-4.508125,1.422718,-9.222862,-9.085455],[-8.610403,5.581294,-4.596815,8.428715,7.168448,0.112455,-7.949667,-2.990917,3.284766],[-6.263982,3.264254,-1.904953,-6.204302,-0.632370,1.847481,-5.431783,2.701469,7.443622],[4.748306,-9.820234,7.758016,7.562200,8.293400,6.042014,3.636606,-3.036537,-8.379794]],[[9.090111,-1.424779,9.942443,-2.583758,-1.470844,6.925711,9.698272,-3.803934,3.511764],[0.347363,5.712009,-5.847500,-7.058383,-4.104559,-1.812410,8.613168,6.349829,-0.484776],[-3.071370,-6.064718,-0.992088,-6.854929,-8.135354,1.537824,-6.223935,6.983634,4.931278],[-9.435942,3.574963,6.949418,1.735170,8.245520,-9.906931,6.773341,-3.412183,7.370967],[4.335088,-3.945507,-9.260697,9.922692,9.184114,-0.731161,-6.479274,-8.947874,1.642686],[-6.073600,-1.604694,0.328424,9.956369,4.945821,-5.024998,-0.065975,-9.111234,-5.606661],[-6.098226,1.558711,-7.855020,3.697152,-9.453476,-1.624363,7.190781,-4.313274,1.297045],[-1.325536,-3.400170,-0.535464,6.551132,-9.725401,-3.453624,-8.960999,-2.616140,-3.489850],[-9.331407,-3.309680,7.714944,-1.221827,4.194701,-4.613045,4.057963,8.098080,1.963863]],[[-5.067084,-0.148628,-1.952084,8.941237,9.475535,2.396845,-6.647665,4.347592,-9.447121],[-5.393608,3.570415,-7.047439,-6.952905,6.988897,4.769611,4.492018,7.955498,9.420530],[-5.431705,-0.322302,-7.362526,1.809138,6.204824,3.179689,9.156311,5.430375,5.603879],[3.387396,0.642060,2.578926,3.320505,-8.353212,-8.704706,-4.726869,5.326340,3.743723],[-8.803975,-5.743248,1.517857,-9.676686,5.881545,-8.192436,0.671425,-1.838290,-1.701427],[7.777816,9.538179,-7.566386,5.883968,-6.553133,7.925094,1.527540,2.943760,-2.497852],[2.280268,3.054942,-6.507725,-5.399752,8.164666,-7.367664,-4.887524,3.120384,6.548719],[-9.086489,7.946744,7.862440,-0.370252,-7.596111,2.900178,-4.467132,2.010834,3.719604],[8.932773,7.603664,4.992359,-1.727142,-8.428519,9.482166,4.048846,-2.759240,-0.378094]],[[-9.041251,-2.249843,-3.224008,7.316744,6.619619,5.533839,-8.492716,-6.754183,5.004272],[9.519611,4.427479,-9.972821,8.003703,-5.398146,-5.865502,-3.411573,5.468220,4.888335],[-1.586173,6.748972,-6.387609,-2.836447,6.900603,-9.734267,-1.866957,4.728839,6.265028],[-3.673395,5.599922,6.855445,-4.358654,-6.930880,-7.949509,7.311021,-3.555108,-1.999358],[9.769174,3.957218,5.971921,-6.653847,1.674783,-1.987765,5.369661,-2.923429,7.713450],[-2.439937,0.810337,-5.975072,-0.732707,-4.759411,-1.686082,3.252669,8.087291,-9.596208],[1.064881,5.390869,-6.876538,7.236088,-9.174696,7.116011,1.222708,6.864218,-4.865649],[8.866312,-3.554267,-4.983213,-1.839081,-0.764581,-3.896691,0.614122,5.800575,8.182846],[-2.268191,4.958300,-5.724452,-3.497524,-2.409222,-6.506242,1.673655,-2.305819,9.387989]],[[-3.126127,-3.293595,2.634562,-5.915504,-0.315132,4.742296,9.454538,7.575916,6.491392],[0.854799,0.028119,8.898787,5.018139,0.378917,-3.465331,-4.268993,3.860275,-1.842289],[7.740241,8.381243,-2.042552,9.567297,-1.150313,6.936184,-7.630036,9.567900,-7.433142],[5.215633,-5.515457,9.396031,2.285277,4.829949,3.166475,-0.633875,-2.730191,-2.033502],[-1.397986,4.639080,-4.274905,-5.900787,7.610101,6.024466,8.752451,0.597911,2.488130],[-2.148896,-7.150556,5.656016,5.050596,3.491224,0.938104,4.895151,0.541674,-6.523549],[2.636741,7.389931,5.409544,-1.671277,8.617473,-2.691986,6.773147,-1.630730,-0.166037],[7.733448,3.471314,-3.508266,-8.924366,-7.854785,-1.081917,-9.164249,-5.789585,-7.992620],[-9.096413,-3.909636,2.983762,-1.673095,3.236489,-5.190997,3.005822,-9.182078,-3.547857]],[[6.468350,-4.731739,1.067510,7.299023,-1.766264,2.397798,0.335999,8.906997,4.033660],[-3.618596,8.893590,-6.741352,1.698768,7.925360,-8.566276,-0.439883,7.734742,-2.459424],[8.306399,-7.498206,5.927899,9.815957,7.425858,-0.199570,5.427548,-1.937093,-3.845332],[-4.925646,-4.899278,3.360865,-8.235585,5.491122,-7.936631,-8.801007,8.212583,8.916647],[-1.251804,9.557548,-1.819098,-1.485119,-9.799294,-0.540700,-4.538165,-1.179367,5.887896],[0.168094,-2.986693,2.114004,-1.683305,-0.464621,-6.773615,-6.596902,-6.179162,-1.331501],[8.629689,-5.521493,3.904471,9.846272,-7.691962,6.976806,2.520525,2.425483,0.433601],[7.208659,-7.892785,5.302680,9.042354,9.443525,5.598183,-5.372730,-4.745017,-9.905414],[-6.826666,8.270916,2.727377,-1.337313,-3.874311,-3.597272,-4.462496,5.140639,-9.933084]]], dtype = "float32")#candidate|5812|(11, 9, 9)|const|float32
uop_5813 = relay.asinh(const_5812.astype('float32')) # shape=(11, 9, 9)
output = uop_5813
output2 = uop_5813
func_5818 = relay.Function([], output)
mod['func_5818'] = func_5818
mod = relay.transform.InferType()(mod)
mutated_mod['func_5818'] = func_5818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5818_call = mutated_mod.get_global_var('func_5818')
call_5819 = func_5818_call()
output = call_5819
func_5820 = relay.Function([], output)
mutated_mod['func_5820'] = func_5820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5110_call = mod.get_global_var('func_5110')
func_5111_call = mutated_mod.get_global_var('func_5111')
call_5833 = func_5110_call()
call_5834 = func_5110_call()
func_789_call = mod.get_global_var('func_789')
func_791_call = mutated_mod.get_global_var('func_791')
const_5836 = relay.const([[-5.653464,-3.876478,-3.238208,9.449209,-0.155099,1.800129,3.216196,-2.436402,4.484981,-8.707813,6.254788,-5.899663,2.906258,8.782219,-5.773907],[9.636614,8.860677,3.082677,5.561313,0.213011,4.088934,9.894650,5.285486,5.109263,-7.943966,-4.311508,9.819167,1.445276,-6.161484,-2.746042],[5.054998,-0.923223,2.493723,-4.261113,-8.566365,-7.121740,-9.245767,-0.395762,5.656889,-4.095840,3.929165,7.310416,-6.006444,0.389955,5.369551],[2.988094,0.425000,-5.517507,3.358868,9.046874,-5.604965,4.267651,6.941847,-4.399004,7.359259,-2.232660,-1.789967,8.359893,-6.082007,3.807440],[-8.062778,-5.011713,-4.919443,-9.703894,9.957440,5.151682,3.241993,-1.968003,-7.260746,6.859982,-8.355117,-7.870410,-2.736633,8.812955,-8.522903],[-0.217739,9.571233,-8.131935,3.033351,-2.508991,-3.000063,7.510899,-7.306560,-7.938439,-1.538119,0.661862,0.816844,1.299968,3.060421,4.551070],[-1.928993,1.399284,-2.435220,5.301076,-0.836608,5.211826,-9.284554,9.453212,-9.092126,5.420925,6.029293,6.192883,0.523819,-9.030556,1.265029]], dtype = "float32")#candidate|5836|(7, 15)|const|float32
call_5835 = relay.TupleGetItem(func_789_call(relay.reshape(const_5836.astype('float32'), [3, 7, 5])), 0)
call_5837 = relay.TupleGetItem(func_791_call(relay.reshape(const_5836.astype('float32'), [3, 7, 5])), 0)
func_2943_call = mod.get_global_var('func_2943')
func_2944_call = mutated_mod.get_global_var('func_2944')
call_5854 = func_2943_call()
call_5855 = func_2943_call()
output = relay.Tuple([call_5833,call_5835,const_5836,call_5854,])
output2 = relay.Tuple([call_5834,call_5837,const_5836,call_5855,])
func_5870 = relay.Function([], output)
mod['func_5870'] = func_5870
mod = relay.transform.InferType()(mod)
output = func_5870()
func_5871 = relay.Function([], output)
mutated_mod['func_5871'] = func_5871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3463_call = mod.get_global_var('func_3463')
func_3465_call = mutated_mod.get_global_var('func_3465')
call_5903 = relay.TupleGetItem(func_3463_call(), 0)
call_5904 = relay.TupleGetItem(func_3465_call(), 0)
func_4413_call = mod.get_global_var('func_4413')
func_4415_call = mutated_mod.get_global_var('func_4415')
call_5919 = relay.TupleGetItem(func_4413_call(), 0)
call_5920 = relay.TupleGetItem(func_4415_call(), 0)
func_5737_call = mod.get_global_var('func_5737')
func_5740_call = mutated_mod.get_global_var('func_5740')
var_5922 = relay.var("var_5922", dtype = "int32", shape = (390,))#candidate|5922|(390,)|var|int32
call_5921 = relay.TupleGetItem(func_5737_call(relay.reshape(var_5922.astype('int32'), [6, 5, 13])), 1)
call_5923 = relay.TupleGetItem(func_5740_call(relay.reshape(var_5922.astype('int32'), [6, 5, 13])), 1)
func_5790_call = mod.get_global_var('func_5790')
func_5792_call = mutated_mod.get_global_var('func_5792')
const_5937 = relay.const([8,-8,7,2,7,5,2,7,-10,8,-1,-2,4,3,2,9,7,-8,7,6,-8,8,-4,1,3,-6,4,-7,-10,2,4,1,9,8,9,-2,4,6,4,3,-7,-6,-5,-9,5,8,-3,3,-8,7,-2,4,-10,-5,10,-2,7,9,-10,10,10,-5,4,-4,-8,2,2,7,8,6,1,6,5,3,-2,3,8,-4,5,-9,-8,2,-8,-4,4,-6,-8,-5,8,10,-1,-1,-10,-1,2,7,-10,-2,1,-7,-3,-10,-7,-6,2,-4,-7,-2,-9,-4,-5,-1,-2,-5,6,-8,7,4,2,7,-5,7,-6,-1,-1,8,-5,-1,3,-2,8,-9,-7,-6,-2,2,-6,9,7,-8,4,2,-6,-8,9,-9,-9,1,-1,4,-10,1,7,-9,-4,1,-5,-7,8,-2,-7,-3,9,-2,-8,6,-7,5,10,6,-1,2,-2,8,6,6,-1,2,10,2,2,-10,-8,-3,-9,4,8,7,-7,-1,-5,8,5,-7,4,4,1,5,1,8,8,9,8,-7,10,-7,4,-2,5,-5,1,7,5,1,-1,-3,3,-7,9,5,2,6,-9,-7,8,-5,1,-10,5,10,2,-5,9,-5,5,-2,4,-5,6,9,-3,-4,-8,1,-6,9,8,3,3,-8,8,7,7,4,1,-7,10,9,6,1,-2,-1,4,8,2,8,-7,9,-5,7,-8,2,-6,8,-4,-5,1,7,-2,3,-4,-1,5,2,4,-10,4,2,7,-3,1,7,5,-9,2,10,-4,6,-10,-3,-8,7,-7,3,1,4,5,5,-7,9,-6,-5,10,2,-10,6,-8,-1,4,-6,1,8,-3,-9,7,10,-9,-4,8,2,-10,7,1,-10,3,1,-8,-1,-2,-1,-2,-4,10,1,5,6,-2,-3,9,2,-3,-6,-2,4,-1,4,-10,4,6,5,-1,-7,2,-7,-7,-4,2,5,-1,9,-6,5,9,3,7], dtype = "int16")#candidate|5937|(375,)|const|int16
call_5936 = relay.TupleGetItem(func_5790_call(relay.reshape(const_5937.astype('int16'), [375,])), 1)
call_5938 = relay.TupleGetItem(func_5792_call(relay.reshape(const_5937.astype('int16'), [375,])), 1)
const_5958 = relay.const([[[False,False,True,True],[False,False,False,True],[False,True,True,True],[False,True,False,False],[False,True,False,False],[True,False,False,True],[False,False,True,True],[True,False,True,True],[False,False,True,True],[False,True,False,True],[False,True,False,False],[False,False,True,True],[False,True,True,True],[True,True,False,False]],[[True,False,True,False],[False,False,False,True],[False,True,False,False],[False,False,True,False],[True,True,True,True],[False,False,False,False],[True,True,True,False],[False,False,False,True],[False,True,False,False],[True,False,True,True],[True,True,False,True],[True,True,True,False],[True,False,False,True],[False,False,True,True]],[[False,False,False,False],[False,False,False,False],[False,False,True,True],[False,False,True,True],[False,True,False,True],[False,True,False,True],[False,False,False,False],[False,True,False,False],[False,False,True,False],[False,True,True,False],[True,False,False,True],[False,True,False,False],[False,False,False,False],[True,False,False,True]]], dtype = "bool")#candidate|5958|(3, 14, 4)|const|bool
bop_5959 = relay.multiply(call_5919.astype('int8'), relay.reshape(const_5958.astype('int8'), relay.shape_of(call_5919))) # shape=(3, 14, 4)
bop_5962 = relay.multiply(call_5920.astype('int8'), relay.reshape(const_5958.astype('int8'), relay.shape_of(call_5920))) # shape=(3, 14, 4)
func_2943_call = mod.get_global_var('func_2943')
func_2944_call = mutated_mod.get_global_var('func_2944')
call_5963 = func_2943_call()
call_5964 = func_2943_call()
output = relay.Tuple([call_5903,call_5921,var_5922,call_5936,const_5937,bop_5959,call_5963,])
output2 = relay.Tuple([call_5904,call_5923,var_5922,call_5938,const_5937,bop_5962,call_5964,])
func_5966 = relay.Function([var_5922,], output)
mod['func_5966'] = func_5966
mod = relay.transform.InferType()(mod)
mutated_mod['func_5966'] = func_5966
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5967 = relay.var("var_5967", dtype = "int32", shape = (390,))#candidate|5967|(390,)|var|int32
func_5966_call = mutated_mod.get_global_var('func_5966')
call_5968 = func_5966_call(var_5967)
output = call_5968
func_5969 = relay.Function([var_5967], output)
mutated_mod['func_5969'] = func_5969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5381_call = mod.get_global_var('func_5381')
func_5382_call = mutated_mod.get_global_var('func_5382')
call_5985 = func_5381_call()
call_5986 = func_5381_call()
output = relay.Tuple([call_5985,])
output2 = relay.Tuple([call_5986,])
func_6021 = relay.Function([], output)
mod['func_6021'] = func_6021
mod = relay.transform.InferType()(mod)
output = func_6021()
func_6022 = relay.Function([], output)
mutated_mod['func_6022'] = func_6022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2464_call = mod.get_global_var('func_2464')
func_2465_call = mutated_mod.get_global_var('func_2465')
call_6095 = func_2464_call()
call_6096 = func_2464_call()
func_5688_call = mod.get_global_var('func_5688')
func_5691_call = mutated_mod.get_global_var('func_5691')
var_6103 = relay.var("var_6103", dtype = "int16", shape = (375,))#candidate|6103|(375,)|var|int16
call_6102 = relay.TupleGetItem(func_5688_call(relay.reshape(var_6103.astype('int16'), [5, 75])), 5)
call_6104 = relay.TupleGetItem(func_5691_call(relay.reshape(var_6103.astype('int16'), [5, 75])), 5)
output = relay.Tuple([call_6095,call_6102,var_6103,])
output2 = relay.Tuple([call_6096,call_6104,var_6103,])
func_6106 = relay.Function([var_6103,], output)
mod['func_6106'] = func_6106
mod = relay.transform.InferType()(mod)
mutated_mod['func_6106'] = func_6106
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6107 = relay.var("var_6107", dtype = "int16", shape = (375,))#candidate|6107|(375,)|var|int16
func_6106_call = mutated_mod.get_global_var('func_6106')
call_6108 = func_6106_call(var_6107)
output = call_6108
func_6109 = relay.Function([var_6107], output)
mutated_mod['func_6109'] = func_6109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5570_call = mod.get_global_var('func_5570')
func_5571_call = mutated_mod.get_global_var('func_5571')
call_6127 = relay.TupleGetItem(func_5570_call(), 1)
call_6128 = relay.TupleGetItem(func_5571_call(), 1)
output = call_6127
output2 = call_6128
func_6129 = relay.Function([], output)
mod['func_6129'] = func_6129
mod = relay.transform.InferType()(mod)
mutated_mod['func_6129'] = func_6129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6129_call = mutated_mod.get_global_var('func_6129')
call_6130 = func_6129_call()
output = call_6130
func_6131 = relay.Function([], output)
mutated_mod['func_6131'] = func_6131
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6135 = relay.const([[[9,5,-9,-3,4,-3],[-5,-7,6,-6,10,-7],[4,3,-2,-2,-4,-10],[5,-4,-7,7,1,-2],[-5,3,2,2,-6,6],[1,-10,4,-6,5,5],[8,-4,5,5,-4,5],[-8,4,3,3,-7,-9],[-7,1,6,6,9,4]],[[-7,5,-9,1,-9,-3],[-6,-8,-1,5,3,-2],[1,6,1,5,-9,1],[-1,5,-7,4,-7,6],[1,-8,9,-5,9,2],[1,7,-10,-10,-1,2],[-5,1,3,2,3,10],[1,2,-9,9,4,2],[6,-4,6,7,4,-3]],[[-9,1,-4,-2,8,-4],[-10,7,-3,-5,-10,8],[-7,-7,-4,10,-5,3],[-3,4,-1,-8,-5,3],[3,-7,-9,1,9,-10],[8,6,2,5,-6,-7],[-9,-6,-10,-2,-8,-8],[-3,4,-6,-7,-6,-10],[-4,-6,-3,-7,-9,-9]],[[-3,6,10,-8,-2,7],[9,-4,10,-5,-8,7],[5,-4,-9,5,-3,-3],[6,8,-4,-8,10,9],[-6,4,-7,-5,-5,9],[5,-5,-7,-1,-10,1],[-3,-8,-2,3,-3,-4],[-8,-5,2,-8,-1,5],[-3,-3,5,-8,4,1]],[[5,8,3,-10,-2,3],[-2,3,5,-3,4,3],[9,-8,-9,1,-5,4],[10,8,-1,-8,-3,6],[6,-10,3,-8,7,5],[6,-4,4,8,1,6],[6,-5,-4,9,-10,8],[2,-6,-5,9,-1,-2],[-8,-9,-4,-3,10,1]],[[8,-1,9,-4,9,-2],[-4,-6,1,-10,-6,-9],[5,-3,9,8,-4,-8],[2,5,-3,-6,7,2],[9,8,10,-6,-1,-9],[-4,10,5,10,1,9],[-2,2,6,-9,5,-10],[5,9,8,-6,4,8],[-5,9,4,1,2,5]],[[-9,-4,-2,-9,-4,-4],[-8,-3,-8,4,-1,-1],[-8,3,8,-1,-2,9],[-1,2,-9,-6,-1,-9],[-1,-2,5,-7,6,4],[-8,10,10,-6,10,-4],[8,-7,-10,6,1,-4],[-3,-9,1,-2,-8,10],[2,9,-8,2,-7,-3]],[[-7,-8,8,5,3,10],[-9,4,7,-9,2,2],[3,3,2,6,-6,-8],[-6,-8,8,4,2,-9],[4,9,-6,-5,4,-10],[8,8,2,-10,8,7],[6,5,1,-9,2,2],[-9,-6,9,-9,-1,10],[-2,2,-6,10,-2,2]],[[-9,-10,-8,-8,9,10],[-7,2,-8,1,-3,-2],[4,3,-6,-9,5,-5],[-10,-10,6,-7,-10,3],[5,10,7,-9,3,-6],[8,-6,-5,-7,-4,5],[8,-5,5,8,1,8],[-9,8,-10,1,-2,-2],[-7,-3,8,3,4,-6]],[[-5,8,2,4,6,3],[10,5,-10,8,-6,10],[-3,-3,10,-5,-6,1],[-3,-9,-8,-5,6,-10],[-7,-4,1,8,-7,-8],[-10,2,-10,-4,-7,-1],[7,3,6,-2,2,-5],[-1,5,-3,7,-10,9],[-3,4,-8,-6,1,-10]],[[3,-7,9,-7,4,-10],[-9,-2,7,10,6,9],[8,-3,-5,3,7,4],[-1,-8,-7,2,9,-6],[5,6,9,-9,1,6],[-5,3,-9,7,9,5],[-8,-1,-2,1,4,-1],[5,2,10,-1,8,-6],[-2,-7,10,9,10,5]],[[9,-9,5,8,10,5],[9,-6,1,-4,-4,-8],[-6,4,-6,-7,-7,10],[8,2,-9,9,-5,6],[6,-1,-4,7,-5,-3],[-2,-8,9,-8,7,5],[9,7,-9,-9,5,-7],[8,-7,9,-6,4,-7],[-3,10,-7,7,8,-7]],[[8,-4,-8,2,-7,1],[-2,-6,-2,-9,-7,4],[-1,9,8,8,2,9],[-5,5,3,-9,-2,1],[-5,8,9,-6,-6,2],[1,-8,-4,-4,-9,4],[-7,-6,5,3,-10,-3],[-5,-9,-4,-5,-3,-1],[-9,9,-5,1,-3,1]],[[6,9,8,-3,3,-4],[-5,5,1,6,-10,-1],[7,7,8,-9,5,-2],[-1,6,9,2,-10,-3],[-2,4,-3,7,6,9],[5,10,-7,2,9,4],[1,-1,3,-3,-2,-7],[1,-6,-1,1,-4,-5],[-5,-9,-9,2,8,-1]]], dtype = "int16")#candidate|6135|(14, 9, 6)|const|int16
var_6136 = relay.var("var_6136", dtype = "int16", shape = (14, 9, 6))#candidate|6136|(14, 9, 6)|var|int16
bop_6137 = relay.bitwise_xor(const_6135.astype('int16'), relay.reshape(var_6136.astype('int16'), relay.shape_of(const_6135))) # shape=(14, 9, 6)
uop_6142 = relay.sinh(var_6136.astype('float32')) # shape=(14, 9, 6)
func_5474_call = mod.get_global_var('func_5474')
func_5475_call = mutated_mod.get_global_var('func_5475')
call_6155 = relay.TupleGetItem(func_5474_call(), 0)
call_6156 = relay.TupleGetItem(func_5475_call(), 0)
output = relay.Tuple([bop_6137,uop_6142,call_6155,])
output2 = relay.Tuple([bop_6137,uop_6142,call_6156,])
func_6165 = relay.Function([var_6136,], output)
mod['func_6165'] = func_6165
mod = relay.transform.InferType()(mod)
mutated_mod['func_6165'] = func_6165
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6166 = relay.var("var_6166", dtype = "int16", shape = (14, 9, 6))#candidate|6166|(14, 9, 6)|var|int16
func_6165_call = mutated_mod.get_global_var('func_6165')
call_6167 = func_6165_call(var_6166)
output = call_6167
func_6168 = relay.Function([var_6166], output)
mutated_mod['func_6168'] = func_6168
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6170 = relay.var("var_6170", dtype = "float32", shape = (12, 1, 14))#candidate|6170|(12, 1, 14)|var|float32
uop_6171 = relay.atanh(var_6170.astype('float32')) # shape=(12, 1, 14)
func_1462_call = mod.get_global_var('func_1462')
func_1463_call = mutated_mod.get_global_var('func_1463')
call_6175 = func_1462_call()
call_6176 = func_1462_call()
func_5405_call = mod.get_global_var('func_5405')
func_5407_call = mutated_mod.get_global_var('func_5407')
call_6184 = relay.TupleGetItem(func_5405_call(), 0)
call_6185 = relay.TupleGetItem(func_5407_call(), 0)
output = relay.Tuple([uop_6171,call_6175,call_6184,])
output2 = relay.Tuple([uop_6171,call_6176,call_6185,])
func_6191 = relay.Function([var_6170,], output)
mod['func_6191'] = func_6191
mod = relay.transform.InferType()(mod)
mutated_mod['func_6191'] = func_6191
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6192 = relay.var("var_6192", dtype = "float32", shape = (12, 1, 14))#candidate|6192|(12, 1, 14)|var|float32
func_6191_call = mutated_mod.get_global_var('func_6191')
call_6193 = func_6191_call(var_6192)
output = call_6193
func_6194 = relay.Function([var_6192], output)
mutated_mod['func_6194'] = func_6194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2799_call = mod.get_global_var('func_2799')
func_2801_call = mutated_mod.get_global_var('func_2801')
call_6230 = relay.TupleGetItem(func_2799_call(), 0)
call_6231 = relay.TupleGetItem(func_2801_call(), 0)
func_5144_call = mod.get_global_var('func_5144')
func_5147_call = mutated_mod.get_global_var('func_5147')
const_6241 = relay.const([[-9.689960,-3.869200,6.213701,-9.262890,-5.868211,7.641093,4.745772,0.760938,5.249169,1.093677,-0.480405,-6.123128,4.276947,-5.454651,0.997543,-2.384163,7.593083,5.479208,1.499200,9.090797,-0.393272,1.934510,4.486575,-9.514815,-9.216092,5.295570,8.251568,6.805826,7.054162,-6.635374,-6.871211,-8.923129,5.306039,-8.204044,4.572701,-9.194721,-0.412658,-4.582889,-8.237853,-6.305339,-7.029832,-8.696888,5.977804,-3.312933,1.328170,-8.347220,1.507463,4.597725,-6.320747,-0.500138,-2.635016,4.396671,-4.929759,-4.121855,-7.766476,6.633553,-3.926940,4.563979,0.677911,-0.562942,-4.671210,-8.247801,3.464146,2.668862,8.558157,9.302969,-3.935127,-6.980864,-6.398971,-9.914980],[8.845685,5.163529,2.883571,-7.344666,9.196179,3.782785,7.302893,2.408335,6.942479,-9.890812,-7.447272,-9.598925,-1.264448,4.168658,6.508565,5.033683,-4.411934,-7.485598,3.694491,-5.014590,4.620492,5.732133,-3.424367,5.385739,7.009411,-6.782727,-6.642154,-1.398149,-8.655338,2.589298,0.962351,-6.136164,-1.541126,2.244644,0.474240,-0.233950,5.439399,6.674765,-6.160584,-9.807197,-2.332544,-6.065332,8.798139,3.656247,-4.069567,-8.659692,-8.590672,3.205849,6.132917,-9.451900,9.740522,-3.176435,-8.571243,-9.727425,-7.918424,-6.753328,8.579091,3.649020,-1.947733,-2.937571,-3.136554,-7.063229,-8.620101,0.594500,2.624404,-6.175972,-6.281741,4.905382,7.257958,5.009600],[-9.414423,-7.157968,-6.388331,9.222245,1.138089,-3.684394,-3.130889,-8.353811,-1.349578,-4.121456,2.075227,-2.419741,1.247747,1.155572,0.471984,6.798112,-8.270739,-6.745202,4.700494,8.297286,3.417850,-4.499540,4.403932,-7.718442,-9.288805,7.618077,-5.250098,6.951149,4.981688,-9.527775,-1.596958,1.773722,6.811366,0.650635,9.905035,8.693043,-9.616986,-0.767692,-1.986409,-0.206309,5.442970,2.165060,3.202209,-6.103463,5.256199,-2.737431,-2.677409,-9.496702,4.470783,-5.689739,4.056438,1.355015,-9.528270,7.668507,8.823918,3.960218,6.124751,-1.212951,-9.667454,4.410776,3.547530,7.497245,4.193602,6.672986,6.331492,8.149743,-3.865257,9.738880,-1.502177,0.573671],[-7.087231,0.330090,9.787136,-7.704530,-1.147968,7.562354,0.606258,6.537278,9.449017,2.010252,-2.546754,7.459307,-7.016264,5.104172,3.195828,-8.098212,-9.297114,8.789802,5.424540,5.844762,6.517832,2.988687,7.296690,-1.802110,0.583836,6.558169,-2.847760,-3.393602,3.931858,-9.119964,7.751742,-1.895924,-0.268010,7.798002,-5.084617,0.188004,-8.707311,-5.346048,2.221879,-3.349817,7.146793,-1.297249,-1.221343,-2.218061,6.858208,-3.888135,3.725539,-8.818967,-5.085383,8.253152,-9.341500,-7.373030,7.680419,-0.026080,6.873903,2.724251,-2.072678,4.358401,8.737615,0.850023,-4.175566,2.064906,-7.882942,3.110533,1.597996,2.670818,6.016067,-8.696791,5.052562,5.199565],[7.445528,9.954185,-3.271720,-4.888799,-2.816539,-2.509359,4.792109,-4.058642,8.190908,-6.661586,-8.086419,-4.004753,-6.346680,-3.679711,7.730123,-3.166987,-5.817716,0.649701,-8.619037,-1.590654,8.020282,0.537793,-8.198388,-7.380086,0.405374,0.852425,9.237103,6.492243,-0.376601,1.523643,0.252688,8.965582,8.339023,9.811018,-4.080290,-8.355094,-1.688767,0.054977,5.707380,5.212477,-5.805532,-8.659689,-0.419837,5.680753,2.099021,1.423556,1.156790,-6.071657,7.388311,-9.864273,-4.886211,1.135868,4.538252,0.824081,-0.628701,6.487145,8.403113,-0.392626,-6.417805,4.429817,-1.003098,-1.723461,8.379916,-3.134224,-5.443408,-0.675620,9.541265,-3.018244,-9.153301,2.137999],[-4.184857,-4.136838,-6.092990,8.037081,-8.323584,-1.205334,1.074673,-0.035784,-2.068114,3.544873,-2.066221,2.207938,5.961169,-3.247996,6.786541,4.612618,-2.879407,-5.306092,-3.706925,3.849631,-8.316665,-4.116046,3.310293,-2.553011,5.617355,-5.949386,7.938311,-6.532089,8.592290,1.147147,-8.941632,-5.610792,-9.569814,-8.214696,6.552758,0.250121,5.909469,3.075043,4.212428,-9.497182,-4.507446,-8.973237,-8.315094,-0.788366,7.589548,8.542628,-3.694205,-2.380055,-8.095434,-3.137643,0.544598,4.387828,9.863977,5.297310,-7.094906,2.001595,-5.367135,-3.546315,-6.483601,3.803920,-0.734902,-8.592782,-0.473208,7.945042,8.862795,-8.677015,-6.437638,2.811676,1.873095,-1.583941],[7.751745,-3.819925,6.571561,-7.563048,4.850492,3.502441,-6.841221,4.801889,-1.238735,8.137888,-0.373990,-3.353852,2.821178,-3.135389,-8.054306,-6.464767,-8.959390,-2.101924,-2.897863,-9.282195,-0.819293,3.639435,6.556810,2.796138,-1.507850,8.843136,8.019219,5.121863,4.049401,3.206265,-9.157136,4.177557,-0.775778,-0.269827,8.675234,-3.010528,-4.282425,-9.441660,-7.328888,1.247365,3.445115,9.997087,6.794154,6.120218,-5.416990,-0.329429,1.727401,-2.220146,2.415924,-8.351926,6.227949,-5.723201,-8.946621,4.448756,9.165529,8.953454,7.189878,4.630657,2.677442,7.689675,6.422164,-2.418545,-7.599393,-1.586902,7.678559,-3.121535,9.149715,-7.545765,8.317508,0.731583],[2.674050,0.712877,3.166796,8.104545,-8.046464,2.406455,-5.848348,-6.330200,-6.227172,2.612321,4.049517,-3.981980,-4.372781,-7.235652,-0.507593,-7.640424,7.928042,-2.304488,-6.600751,0.982656,-7.778632,-5.562507,9.247203,7.138245,7.618975,8.993816,-1.795107,-1.525836,3.441779,6.576825,-7.974603,1.144679,1.052806,-2.770457,7.761578,-9.436550,-5.561629,-1.211434,7.560031,4.539464,-8.233176,7.738683,-2.139372,-9.854202,5.581668,1.787654,9.126061,1.293816,-9.708045,0.435800,2.845898,-6.616315,-8.032526,2.400140,-4.438725,0.265548,-0.835947,-1.644798,-0.331294,-8.982921,-0.517040,1.408163,-8.590379,-7.033346,-4.216114,-0.592979,-8.946107,-8.005235,5.845927,-4.495597],[-6.721635,2.804325,5.039073,-2.705983,-2.799977,3.284690,-4.419300,-1.491012,1.749933,-3.655350,-3.114458,6.263839,2.562575,-8.195695,-5.250096,-4.605858,-0.402014,7.457267,9.995584,3.774705,-3.541703,-4.294729,2.702069,5.157148,-9.306059,-9.368535,-8.375422,8.066899,3.786625,-3.573552,-5.310176,5.556374,-6.146836,-8.411217,-8.188484,1.237604,-2.983417,8.210013,3.564288,-1.147000,-1.189856,-6.358225,4.635809,-0.848771,4.659901,-1.943246,-0.506322,-6.420535,-7.993534,-9.988716,-7.620935,6.433356,-9.246098,-0.595639,8.942138,3.102502,-9.155770,-7.051130,8.445916,-4.207364,3.377347,-2.398536,-6.190248,5.066239,-0.936254,1.639418,8.383658,5.622705,-2.542228,9.256840],[9.737123,2.584155,4.994422,2.542554,1.809970,2.727831,-9.109131,-3.073559,1.102691,3.328877,5.167351,-2.688974,2.256001,-9.717215,-9.320739,6.481845,-2.533438,5.728432,-2.789774,-3.701993,-9.116276,-4.939951,-9.404406,-7.399137,-5.168707,6.135967,-6.577417,2.346896,2.203763,9.821832,7.653653,5.715754,-4.237549,6.738285,4.099003,-7.450215,-9.220154,-9.344753,5.751092,-0.537189,-8.101750,9.690516,6.124891,-6.545920,5.289130,-4.911978,-8.959494,-5.120094,-3.258478,5.262636,-5.775080,-8.573959,0.522179,5.097296,5.055452,-0.589701,7.857916,-0.097868,-4.436303,8.860026,6.718992,7.608630,-7.573092,-9.470926,9.519194,-6.099442,7.268702,-0.005638,-3.045263,9.021119],[7.379114,9.147235,8.003208,-4.743058,0.581954,8.001030,3.025463,-7.764963,1.294973,4.593179,3.124850,-3.021559,-3.892562,4.476504,-0.590279,-2.844096,-7.373685,-9.693821,3.638255,-1.809106,-2.456442,8.113604,-2.125354,8.161007,-3.257977,-4.254900,8.153304,-3.363018,-5.771005,-4.060109,-4.514569,-0.314739,-2.944613,8.162196,2.901198,-1.764531,5.544109,-9.012648,-7.608127,1.304623,-2.257132,-0.958063,-4.243973,8.610928,-8.902149,9.073226,-0.891540,4.425792,-3.785052,-7.523067,-6.881386,-8.720672,6.104938,1.646732,-4.242180,-0.413935,2.154120,-0.640173,-3.990196,-0.688767,0.843712,7.557133,5.411694,1.816123,3.509614,-0.197237,-5.737036,-2.747606,1.214525,5.281134],[-7.130414,-9.272981,-3.104962,-4.701762,-6.322033,5.512035,-4.240699,9.472737,-3.617276,-2.416250,-9.075885,6.539812,2.487757,-4.507181,-3.179486,-7.473130,-3.668999,-2.021286,-6.112034,4.840596,0.080907,-2.351196,4.669511,6.765762,-7.780289,-2.193644,-4.876260,-1.455545,8.301178,-9.613009,-8.162927,-1.818213,3.040249,-4.515392,2.977059,-8.239430,-6.203210,7.253198,-2.096912,0.919100,-4.191708,-9.105045,-0.600387,-5.450932,9.010509,7.652498,1.888052,-5.606739,-3.142508,-8.592699,-5.432291,-6.804563,-4.280989,2.057696,-5.309172,0.734661,-5.224857,-8.121481,-1.283404,-1.702891,0.089583,-9.196359,6.051936,-9.991167,4.039531,-0.362523,5.479302,-5.708391,-5.587177,8.118913]], dtype = "float32")#candidate|6241|(12, 70)|const|float32
call_6240 = relay.TupleGetItem(func_5144_call(relay.reshape(const_6241.astype('float32'), [8, 15, 7])), 0)
call_6242 = relay.TupleGetItem(func_5147_call(relay.reshape(const_6241.astype('float32'), [8, 15, 7])), 0)
output = relay.Tuple([call_6230,call_6240,const_6241,])
output2 = relay.Tuple([call_6231,call_6242,const_6241,])
func_6245 = relay.Function([], output)
mod['func_6245'] = func_6245
mod = relay.transform.InferType()(mod)
mutated_mod['func_6245'] = func_6245
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6245_call = mutated_mod.get_global_var('func_6245')
call_6246 = func_6245_call()
output = call_6246
func_6247 = relay.Function([], output)
mutated_mod['func_6247'] = func_6247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4471_call = mod.get_global_var('func_4471')
func_4473_call = mutated_mod.get_global_var('func_4473')
call_6282 = relay.TupleGetItem(func_4471_call(), 1)
call_6283 = relay.TupleGetItem(func_4473_call(), 1)
output = call_6282
output2 = call_6283
func_6286 = relay.Function([], output)
mod['func_6286'] = func_6286
mod = relay.transform.InferType()(mod)
mutated_mod['func_6286'] = func_6286
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6286_call = mutated_mod.get_global_var('func_6286')
call_6287 = func_6286_call()
output = call_6287
func_6288 = relay.Function([], output)
mutated_mod['func_6288'] = func_6288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2336_call = mod.get_global_var('func_2336')
func_2338_call = mutated_mod.get_global_var('func_2338')
call_6306 = relay.TupleGetItem(func_2336_call(), 0)
call_6307 = relay.TupleGetItem(func_2338_call(), 0)
func_4929_call = mod.get_global_var('func_4929')
func_4931_call = mutated_mod.get_global_var('func_4931')
call_6315 = relay.TupleGetItem(func_4929_call(), 3)
call_6316 = relay.TupleGetItem(func_4931_call(), 3)
output = relay.Tuple([call_6306,call_6315,])
output2 = relay.Tuple([call_6307,call_6316,])
func_6344 = relay.Function([], output)
mod['func_6344'] = func_6344
mod = relay.transform.InferType()(mod)
mutated_mod['func_6344'] = func_6344
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6344_call = mutated_mod.get_global_var('func_6344')
call_6345 = func_6344_call()
output = call_6345
func_6346 = relay.Function([], output)
mutated_mod['func_6346'] = func_6346
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6434 = relay.var("var_6434", dtype = "uint64", shape = (8, 7, 9))#candidate|6434|(8, 7, 9)|var|uint64
var_6435 = relay.var("var_6435", dtype = "uint64", shape = (8, 7, 9))#candidate|6435|(8, 7, 9)|var|uint64
bop_6436 = relay.less_equal(var_6434.astype('bool'), relay.reshape(var_6435.astype('bool'), relay.shape_of(var_6434))) # shape=(8, 7, 9)
output = bop_6436
output2 = bop_6436
func_6441 = relay.Function([var_6434,var_6435,], output)
mod['func_6441'] = func_6441
mod = relay.transform.InferType()(mod)
mutated_mod['func_6441'] = func_6441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6441_call = mutated_mod.get_global_var('func_6441')
var_6443 = relay.var("var_6443", dtype = "uint64", shape = (8, 7, 9))#candidate|6443|(8, 7, 9)|var|uint64
var_6444 = relay.var("var_6444", dtype = "uint64", shape = (8, 7, 9))#candidate|6444|(8, 7, 9)|var|uint64
call_6442 = func_6441_call(var_6443,var_6444,)
output = call_6442
func_6445 = relay.Function([var_6443,var_6444,], output)
mutated_mod['func_6445'] = func_6445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4453_call = mod.get_global_var('func_4453')
func_4454_call = mutated_mod.get_global_var('func_4454')
call_6450 = relay.TupleGetItem(func_4453_call(), 0)
call_6451 = relay.TupleGetItem(func_4454_call(), 0)
func_3274_call = mod.get_global_var('func_3274')
func_3278_call = mutated_mod.get_global_var('func_3278')
const_6456 = relay.const([8,-5,8,-6,-7,2,-9,-4,8,10,5,-5,-2,-4,8,1,9,-4,-2,-10,7,6,4,10,6,-9,-7,-3,-9,-3,6,4,-2,2,9,6,-3,5,-4,9,-3,2,-3,9,2,10,8,3,4,-7,-7,-10,-5,8,-10,-9,3,2,-6,9,-5,-8,-3,-6,-4,10,7,-2,7,-2,-6,9,-6,-5,-4,-2,3,5,-9,-1,-5,6,2,-4,9,5,9,-5,7,-7,4,1,9,3,8,-3,-6,-2,-7,9,-2,-1,10,-8,-6,7,6,9,-5,-1,6,-3,3,5,10,7,-8,-5,-4,5,-7,10,-2,9,1,10,4,-4,-9,-8,-2,-2,-5,9,9,-7,-8,-2,-6,-8,10,6,1,4,6,-8,-9,9,7,-3,-3,5,-9,-2,7,-4,7,-3,-8,6,-9,4,-5,3,-2,10,-7,7], dtype = "uint16")#candidate|6456|(168,)|const|uint16
const_6457 = relay.const([[0.821159,-2.187351,-6.990904,3.347512,-2.521054,-5.583210,5.494315,6.730668,1.456642,-8.965704,8.421741,-2.992119,-3.612865,-2.209881,1.177558,-0.241484,-9.538908,0.467503,1.237416,-6.991641,-4.237289,-4.331851,-9.066862,-4.568676,-3.538263,5.771395,-7.350360,-0.433334,-3.364164,1.844937,-2.683984,-3.677224,-7.463428,5.466000,-0.135190,-4.024160,1.085634,-7.020294,-8.588680,9.396325,-2.245776,-9.683785,-2.092934,1.646138,5.897392,4.193968,0.394297,-8.504649,3.660060,4.323324,-8.502405,-9.782175,-8.783289,8.112034,-9.088760,8.418659,7.079834,0.237758,-1.396862,-8.876879,-9.440752,-7.719215,-7.926874,0.264910,-8.646828,4.069160,-1.538147,-2.627381,8.827578,-5.575322,3.034220,-2.574032,7.594948,-5.656373,-8.184422,-8.748344,-7.993301,-2.717180,4.635757,-1.306593,-7.821636,-5.923422,-3.391711,1.486957,-9.248963,4.610022,6.178107,6.444593,0.668421,5.887519,-3.141276,-5.033793,-2.840310,8.045488,2.343301,5.048370,-7.898524,-0.379289,2.208447,-2.198081,1.022858,3.970132,4.873114,-3.467306,-2.842053]], dtype = "float32")#candidate|6457|(1, 105)|const|float32
call_6455 = relay.TupleGetItem(func_3274_call(relay.reshape(const_6456.astype('uint16'), [168,]), relay.reshape(const_6457.astype('float32'), [105,]), ), 2)
call_6458 = relay.TupleGetItem(func_3278_call(relay.reshape(const_6456.astype('uint16'), [168,]), relay.reshape(const_6457.astype('float32'), [105,]), ), 2)
uop_6481 = relay.acosh(call_6455.astype('float32')) # shape=(168,)
uop_6483 = relay.acosh(call_6458.astype('float32')) # shape=(168,)
func_6021_call = mod.get_global_var('func_6021')
func_6022_call = mutated_mod.get_global_var('func_6022')
call_6492 = relay.TupleGetItem(func_6021_call(), 0)
call_6493 = relay.TupleGetItem(func_6022_call(), 0)
func_6129_call = mod.get_global_var('func_6129')
func_6131_call = mutated_mod.get_global_var('func_6131')
call_6502 = func_6129_call()
call_6503 = func_6129_call()
output = relay.Tuple([call_6450,const_6456,const_6457,uop_6481,call_6492,call_6502,])
output2 = relay.Tuple([call_6451,const_6456,const_6457,uop_6483,call_6493,call_6503,])
func_6511 = relay.Function([], output)
mod['func_6511'] = func_6511
mod = relay.transform.InferType()(mod)
mutated_mod['func_6511'] = func_6511
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6511_call = mutated_mod.get_global_var('func_6511')
call_6512 = func_6511_call()
output = call_6512
func_6513 = relay.Function([], output)
mutated_mod['func_6513'] = func_6513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4395_call = mod.get_global_var('func_4395')
func_4396_call = mutated_mod.get_global_var('func_4396')
call_6520 = func_4395_call()
call_6521 = func_4395_call()
func_3184_call = mod.get_global_var('func_3184')
func_3187_call = mutated_mod.get_global_var('func_3187')
const_6541 = relay.const([8.959827,-6.302029,-5.646758,-7.209177,-6.062668,9.782698,-0.354623,-2.689759,-7.545774,0.813542,-7.884643,-9.565753,0.694449,7.984524,0.634632,-6.980415,-3.340557,4.533908,-7.569963,5.533148,2.024536,-0.125950,-0.081870,-0.456641,9.019184,-3.585555,5.263483,-2.374033,-7.335464,-0.950158,-1.361997,-2.294852,1.448587,-0.721577,5.713660,-2.385717,-6.181950,-0.939269,-1.075532,-2.388566,9.982414,9.820793,7.050992,8.501448,-7.159775,-8.415178,1.756483,6.841907,-4.727099,-6.967598,2.863883,-2.362137,-3.628135,-3.534180,6.182838,-9.811824,7.694761,-1.690541,8.008322,4.370028,5.587437,3.970196,-4.279002,2.415617,-1.608740,4.916457,-4.487696,3.146742,-6.410500,9.999219,-4.449507,-9.660692,-7.644777,4.071384,6.330592,2.648304,-7.880433,1.445032,2.760216,6.037182,-1.273180,1.435784,-5.094192,7.565664,-2.220155,1.171459,7.872694,-9.665557,-0.382245,3.254200,-2.945821,-4.071704,5.436743,-4.656721,-0.809937,-6.725772,-2.160600,6.114137,0.703052,2.792015,-9.859524,-8.553784,0.280681,5.541602,-6.548660,5.639947,3.316135,7.730864,2.897594,0.706117,5.115751,-6.963799,4.920783,1.580087,4.917018,-5.802798,9.538105,9.889353,6.736431,-9.290662,1.206107,2.515799,8.210862,-9.547571,-5.932361,-9.396014,1.605199,4.295833,-9.815861,5.870903,0.188521,6.762731,5.659111,1.701552,9.108582,-1.347594,4.783996,5.003710,6.645302,1.374684,8.195209,7.015134,5.162029,9.861593,0.788592,1.041278,-8.216324,1.578768,4.873733,8.293571,-1.149800,8.588824,1.238934,-3.617282,-9.545211,-6.060672,1.831070,1.554702,-0.313094,3.586349,5.561736,-3.939590,1.454663,8.855875,1.007540,-2.123410,7.066104,0.767698,-1.354032,5.944112,-4.293757,5.625612,2.866626,-8.532928,0.190402,-1.235844,-3.601989,4.225730,-9.069005,-5.911151,6.686779,-5.043683,-2.661025,2.755797,0.670615,-8.486621,-3.180129,-0.451311,-2.523173,2.585507,-2.682458,-3.194130,-2.253646,-1.032848,8.677706,-2.225758,2.196504,7.737055,8.300286,5.371959,8.035223,-7.181403,3.041949,9.474453,0.471702,3.119302,-5.116088,-1.758244,3.957454,-7.297777,8.115271,4.487235,5.278654,-5.382447,7.220310,1.348821,2.522453,-1.914776,-1.175589,-6.404329,-1.477758,4.742295,-8.391954,-1.757931,8.142929,-0.238562,7.428205,5.052442,-5.604300,1.816258,8.722500,-3.930787,-7.936245,2.030341,-4.058036,-9.766413,-8.493880,-3.712142,4.384752,-4.368645,2.153726,8.449660,5.642715,3.869130,7.753377,9.872597,6.752127,7.539039,4.376111,0.852558,9.823885,-5.394023,3.917338,-0.904773,5.134879,5.593907,8.471394,-5.288750,-2.228454,-5.179048,-0.085370,-4.472257,1.922839,-2.739235,7.630739,-8.666262,2.638880,-8.896386,0.546144,-4.419958,7.909903,2.801269,-3.037522,9.525885,0.673162,-9.703020,-1.326043,-0.312795,5.215042,-3.803652,-3.376597,5.416781,6.634102,-9.222048,-7.463845,-6.845455,8.565869,-9.000024,1.322041,-4.363018,0.100982,-3.457900,7.485734,4.960215,4.214051,3.175045,-1.206728,-9.739575,-9.727231,7.194146,2.801859,1.315608,9.260095,-8.745170,7.061495,-9.391266,-8.688711,-4.904176,4.668472,-2.228430,5.204264,-0.375359,-6.620564,-9.624089,5.347836,6.129263,7.028492,2.383268,-8.915909,1.573370,-3.113557,-4.779620,-3.611826,6.603264,-9.910813,9.520138,0.570354,9.234252,-0.986599,3.962837,8.544845,-9.071064,0.421371,-5.677841,6.566559,2.574227,2.371276,-8.187753,9.264143,1.288355,0.263728,7.975777,-0.221558,-7.968691,-9.195442,-1.478436,-9.915232,-4.171261,4.320629,8.651820,-6.169332,-0.471498,-0.873655,-6.873467,-6.964445,2.904106,-6.616613,6.166642,-2.651311,2.073971,6.354430,-0.330531,-0.475771,9.219103,7.025159,-2.547226,7.214795,1.196198,-9.517717,3.913265,5.850293,-4.389916,-0.633276,-1.223349,-8.573996,4.665833,-8.633575,9.979128,6.343870,-3.630800,-1.162790,-4.611349,7.795638,9.895056,2.078237,7.549673,-0.952325,-3.278638,8.035071,4.128065,-5.910007,4.259734,-9.552864,5.002613,9.745678,3.608422,8.363918,9.744148,4.431379,-7.730669,-9.381190,-0.063058,5.555846,6.709586,5.336277,-5.416994,6.108779,-8.979612,3.630408,4.362616,2.085963,-1.444670,7.240211,-3.236480,-5.428763,1.364793,-4.411915,0.162575,3.142261,-7.963290,5.814559,-9.801981,-3.696393,1.486434,3.652800,-9.421916,6.349803,8.121246,-7.473946,4.652191,-7.477070,3.220897,-2.585341,-1.793871,2.034962,0.399977,-4.019573,-3.178180,-9.414125,-1.552732,-7.048488,8.738873,5.293141,-9.793109,-8.253020,-9.643736,8.164628,7.849683,0.083502,5.565529,-9.509915,1.060333,-7.582539,6.030443,5.573278,-0.281828,-5.502399,0.652353,-2.039003,3.090477,-4.698798,4.671474], dtype = "float32")#candidate|6541|(462,)|const|float32
call_6540 = func_3184_call(relay.reshape(const_6541.astype('float32'), [11, 3, 14]))
call_6542 = func_3184_call(relay.reshape(const_6541.astype('float32'), [11, 3, 14]))
var_6544 = relay.var("var_6544", dtype = "float32", shape = (11, 3, 14))#candidate|6544|(11, 3, 14)|var|float32
bop_6545 = relay.bitwise_or(call_6540.astype('uint64'), relay.reshape(var_6544.astype('uint64'), relay.shape_of(call_6540))) # shape=(11, 3, 14)
bop_6548 = relay.bitwise_or(call_6542.astype('uint64'), relay.reshape(var_6544.astype('uint64'), relay.shape_of(call_6542))) # shape=(11, 3, 14)
uop_6576 = relay.acosh(var_6544.astype('float32')) # shape=(11, 3, 14)
uop_6578 = relay.log(uop_6576.astype('float32')) # shape=(11, 3, 14)
output = relay.Tuple([call_6520,const_6541,bop_6545,uop_6578,])
output2 = relay.Tuple([call_6521,const_6541,bop_6548,uop_6578,])
func_6584 = relay.Function([var_6544,], output)
mod['func_6584'] = func_6584
mod = relay.transform.InferType()(mod)
var_6585 = relay.var("var_6585", dtype = "float32", shape = (11, 3, 14))#candidate|6585|(11, 3, 14)|var|float32
output = func_6584(var_6585)
func_6586 = relay.Function([var_6585], output)
mutated_mod['func_6586'] = func_6586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4590_call = mod.get_global_var('func_4590')
func_4592_call = mutated_mod.get_global_var('func_4592')
call_6619 = relay.TupleGetItem(func_4590_call(), 0)
call_6620 = relay.TupleGetItem(func_4592_call(), 0)
output = call_6619
output2 = call_6620
func_6629 = relay.Function([], output)
mod['func_6629'] = func_6629
mod = relay.transform.InferType()(mod)
mutated_mod['func_6629'] = func_6629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6629_call = mutated_mod.get_global_var('func_6629')
call_6630 = func_6629_call()
output = call_6630
func_6631 = relay.Function([], output)
mutated_mod['func_6631'] = func_6631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2173_call = mod.get_global_var('func_2173')
func_2175_call = mutated_mod.get_global_var('func_2175')
call_6653 = func_2173_call()
call_6654 = func_2173_call()
func_2257_call = mod.get_global_var('func_2257')
func_2258_call = mutated_mod.get_global_var('func_2258')
call_6655 = relay.TupleGetItem(func_2257_call(), 0)
call_6656 = relay.TupleGetItem(func_2258_call(), 0)
func_4413_call = mod.get_global_var('func_4413')
func_4415_call = mutated_mod.get_global_var('func_4415')
call_6660 = relay.TupleGetItem(func_4413_call(), 0)
call_6661 = relay.TupleGetItem(func_4415_call(), 0)
func_2943_call = mod.get_global_var('func_2943')
func_2944_call = mutated_mod.get_global_var('func_2944')
call_6672 = func_2943_call()
call_6673 = func_2943_call()
func_1026_call = mod.get_global_var('func_1026')
func_1030_call = mutated_mod.get_global_var('func_1030')
var_6683 = relay.var("var_6683", dtype = "int8", shape = (2310, 1))#candidate|6683|(2310, 1)|var|int8
call_6682 = relay.TupleGetItem(func_1026_call(relay.reshape(var_6683.astype('int8'), [15, 11, 14]), relay.reshape(var_6683.astype('int8'), [15, 11, 14]), ), 0)
call_6684 = relay.TupleGetItem(func_1030_call(relay.reshape(var_6683.astype('int8'), [15, 11, 14]), relay.reshape(var_6683.astype('int8'), [15, 11, 14]), ), 0)
output = relay.Tuple([call_6653,call_6655,call_6660,call_6672,call_6682,var_6683,])
output2 = relay.Tuple([call_6654,call_6656,call_6661,call_6673,call_6684,var_6683,])
func_6699 = relay.Function([var_6683,], output)
mod['func_6699'] = func_6699
mod = relay.transform.InferType()(mod)
mutated_mod['func_6699'] = func_6699
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6700 = relay.var("var_6700", dtype = "int8", shape = (2310, 1))#candidate|6700|(2310, 1)|var|int8
func_6699_call = mutated_mod.get_global_var('func_6699')
call_6701 = func_6699_call(var_6700)
output = call_6701
func_6702 = relay.Function([var_6700], output)
mutated_mod['func_6702'] = func_6702
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3097_call = mod.get_global_var('func_3097')
func_3099_call = mutated_mod.get_global_var('func_3099')
call_6718 = func_3097_call()
call_6719 = func_3097_call()
func_2257_call = mod.get_global_var('func_2257')
func_2258_call = mutated_mod.get_global_var('func_2258')
call_6726 = relay.TupleGetItem(func_2257_call(), 0)
call_6727 = relay.TupleGetItem(func_2258_call(), 0)
func_1462_call = mod.get_global_var('func_1462')
func_1463_call = mutated_mod.get_global_var('func_1463')
call_6738 = func_1462_call()
call_6739 = func_1462_call()
func_6629_call = mod.get_global_var('func_6629')
func_6631_call = mutated_mod.get_global_var('func_6631')
call_6757 = func_6629_call()
call_6758 = func_6629_call()
func_1111_call = mod.get_global_var('func_1111')
func_1116_call = mutated_mod.get_global_var('func_1116')
const_6768 = relay.const([[5,-2,-2,-8,9,-3,-8,-3,2,7],[-1,-9,10,-4,3,8,4,3,-6,8],[10,8,-2,6,-3,2,-1,-9,-10,-2],[8,3,3,-8,4,6,-9,-5,-9,5],[-5,6,-7,-9,-9,-1,4,-9,-9,-5],[4,10,-8,-6,-7,7,-5,8,-9,8],[9,-2,-5,-9,9,1,5,-9,-6,10]], dtype = "int8")#candidate|6768|(7, 10)|const|int8
var_6769 = relay.var("var_6769", dtype = "int8", shape = (420,))#candidate|6769|(420,)|var|int8
const_6770 = relay.const([-1,3,-3,5,-2,4,-10,-4,-7,2,-6,-7,-6,8,-5,10,-10,-5,4,5,-10,5,-4,-9,-4,6,-4,4,9,1,-9,-9,4,1,7,3,-7,-7,7,-3], dtype = "uint8")#candidate|6770|(40,)|const|uint8
call_6767 = relay.TupleGetItem(func_1111_call(relay.reshape(const_6768.astype('int8'), [14, 5, 1]), relay.reshape(var_6769.astype('int8'), [14, 5, 6]), relay.reshape(const_6770.astype('uint8'), [40,]), ), 2)
call_6771 = relay.TupleGetItem(func_1116_call(relay.reshape(const_6768.astype('int8'), [14, 5, 1]), relay.reshape(var_6769.astype('int8'), [14, 5, 6]), relay.reshape(const_6770.astype('uint8'), [40,]), ), 2)
func_3184_call = mod.get_global_var('func_3184')
func_3187_call = mutated_mod.get_global_var('func_3187')
const_6775 = relay.const([0.781198,8.497810,-0.055084,-6.738969,-2.990992,-7.160568,-3.905069,-3.292707,1.592175,3.571433,-8.729216,2.095784,-6.559887,6.312068,-5.182709,-4.203051,7.200526,-0.045183,-2.765949,5.466498,6.781323,-2.668193,-0.815372,-7.660499,6.764964,8.202884,-0.514453,3.318119,-9.462461,-7.884496,0.689078,5.111844,-1.119017,-4.829541,-8.383577,5.106039,-5.924552,-2.117893,2.387372,-2.094201,-5.534751,-5.796805,-7.447276,2.644514,-9.727911,1.822201,-2.042942,7.330841,-9.457595,5.303935,3.939163,-5.958887,-6.826855,0.977690,-8.542635,2.983301,6.638564,2.720392,0.401166,3.969112,-6.199427,-1.963671,8.774883,0.329226,7.774853,-9.538804,-8.321155,-5.589807,3.014621,-0.423028,6.938577,-4.106008,9.871700,-1.460969,-3.695568,0.037520,-3.368059,-9.810782,9.614825,9.617788,-4.669372,4.897710,4.681214,-9.100486,4.965852,-3.507275,-2.343760,-9.782228,-2.999686,-6.646006,-1.806768,1.194311,9.905406,-4.590354,6.360327,-5.457044,4.995898,-6.924275,4.134907,-1.565542,0.310291,-6.157393,1.299296,-0.992117,7.835405,7.121402,-8.045323,4.992452,-0.351480,-5.454229,7.457449,9.786150,-3.732372,8.745229,-3.604985,8.625448,-2.918506,9.532142,-3.127272,0.084847,1.286285,0.025581,6.918036,7.378525,-5.325724,-2.204016,-6.770908,-1.939865,2.487338,9.650756,6.247492,-8.855179,-3.427252,-1.957263,8.619591,-1.318798,-1.056515,-6.974368,-6.376212,8.407671,9.696301,7.999975,5.063990,-0.457426,5.472797,8.397668,-6.020693,2.369485,5.622515,6.811688,9.013812,5.949091,7.294410,-7.268508,-4.720950,-8.416163,4.941128,7.003439,-4.241808,2.961279,4.974747,-5.826878,-2.214736,-2.935677,4.834928,-8.747803,-3.464659,-3.708558,7.219745,6.892134,-8.459377,0.776972,5.877424,9.834990,5.901835,-3.852388,7.224628,-3.225295,-5.241653,1.945258,9.399013,-2.822222,-8.488199,4.008970,7.229135,0.245024,6.249701,3.169276,4.178355,-1.193879,-6.604466,-9.180323,3.112682,1.337978,8.842621,-8.371432,4.199593,-2.905206,0.073757,2.154395,8.378256,7.014937,-0.282747,4.345756,9.794304,-0.907002,-3.443882,6.884839,7.449870,9.429785,3.585622,6.487102,7.216410,-3.067067,-2.829167,4.682333,-8.676800,-4.337627,-7.380331,5.643758,8.795511,8.233008,-4.737449,8.871658,4.677507,-3.395810,-8.481862,4.716908,-3.051380,6.100630,-4.691582,-3.584931,3.377251,0.943855,-0.919409,0.333391,-4.701412,-8.283533,2.373592,-2.428358,-7.832264,2.929324,2.048401,-3.109717,1.979984,-6.741092,8.769812,-1.215126,5.893767,-2.869664,-7.555686,2.007794,-6.914128,1.698982,8.601288,-5.803313,7.647433,8.295868,1.543722,-0.926208,7.492696,-4.342678,9.589504,8.315781,-0.143306,-5.375759,0.385538,8.687642,9.900579,8.456320,-3.024081,3.531914,1.495164,-5.935014,-0.452943,6.601589,0.269900,-7.066889,9.216494,1.702843,2.455748,-1.270470,5.644475,-3.803944,7.332837,-1.133844,-9.229722,3.675335,-5.954746,-7.011089,-8.257629,-1.569112,3.646587,-3.141380,-9.993953,-9.542917,8.975805,-7.352163,-9.443084,-7.337024,-3.637987,4.365853,-3.288264,-1.017681,7.064920,1.122680,7.096449,2.280530,2.984705,3.368962,-3.457593,1.895796,-3.763263,-1.699284,2.800436,-1.848206,9.657605,-6.546491,-2.790999,-9.342849,3.429684,0.578288,1.593249,5.643804,-6.476365,-8.288949,-7.376953,2.494761,8.132441,9.072313,-8.108324,-2.301357,7.154556,5.724276,-7.870421,4.231964,9.702065,-1.525823,-1.184640,6.409091,-4.726689,2.475715,-0.537223,3.654486,-0.887139,-6.693379,7.155824,9.841269,6.943668,-9.314604,-2.754415,9.671921,8.568998,7.184026,9.311859,-1.065160,-3.733866,-0.086691,-0.083422,6.256632,-3.921559,0.338974,-1.015439,-7.819340,2.624866,6.108870,4.891167,-5.878810,-4.271569,-9.160942,-2.094805,2.350690,-2.607513,9.706675,-7.038167,1.423137,-5.856364,-4.892043,8.788527,-2.919443,2.343702,8.506895,-2.410219,3.557892,2.372049,-1.108218,2.572066,-1.931532,0.736237,-6.151579,-9.420918,-1.325963,0.090408,-3.133666,-9.103776,6.641761,-4.380343,-3.438291,-4.702439,-1.826408,1.204413,-8.275734,-4.807778,-4.207670,-0.334424,7.918490,-9.610092,-5.301722,-3.701160,1.397357,3.417195,1.147863,1.540786,8.453320,4.321388,5.392301,-5.130469,7.534037,-0.449846,2.081725,2.112394,-1.843156,-8.302554,3.960495,0.333857,9.802894,7.862408,-6.919859,-7.692459,5.035103,0.471582,-3.235602,-1.593229,1.513465,8.735436,0.793598,1.992140,9.836045,-6.542020,6.119695,9.254830,5.552957,6.677461,2.554049,1.869045,6.794926,7.443240,-8.370305,-6.687424,-9.928329,-2.784540,-4.901248,7.388454,-2.667830,-8.650308,5.106983,-7.281479,-5.848590,1.957814,-6.492453,-0.386360,5.760652], dtype = "float32")#candidate|6775|(462,)|const|float32
call_6774 = func_3184_call(relay.reshape(const_6775.astype('float32'), [11, 3, 14]))
call_6776 = func_3184_call(relay.reshape(const_6775.astype('float32'), [11, 3, 14]))
output = relay.Tuple([call_6718,call_6726,call_6738,call_6757,call_6767,const_6768,var_6769,const_6770,call_6774,const_6775,])
output2 = relay.Tuple([call_6719,call_6727,call_6739,call_6758,call_6771,const_6768,var_6769,const_6770,call_6776,const_6775,])
func_6786 = relay.Function([var_6769,], output)
mod['func_6786'] = func_6786
mod = relay.transform.InferType()(mod)
var_6787 = relay.var("var_6787", dtype = "int8", shape = (420,))#candidate|6787|(420,)|var|int8
output = func_6786(var_6787)
func_6788 = relay.Function([var_6787], output)
mutated_mod['func_6788'] = func_6788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5381_call = mod.get_global_var('func_5381')
func_5382_call = mutated_mod.get_global_var('func_5382')
call_6803 = func_5381_call()
call_6804 = func_5381_call()
func_4736_call = mod.get_global_var('func_4736')
func_4738_call = mutated_mod.get_global_var('func_4738')
var_6815 = relay.var("var_6815", dtype = "float32", shape = (182,))#candidate|6815|(182,)|var|float32
call_6814 = relay.TupleGetItem(func_4736_call(relay.reshape(var_6815.astype('float32'), [7, 2, 13])), 1)
call_6816 = relay.TupleGetItem(func_4738_call(relay.reshape(var_6815.astype('float32'), [7, 2, 13])), 1)
output = relay.Tuple([call_6803,call_6814,var_6815,])
output2 = relay.Tuple([call_6804,call_6816,var_6815,])
func_6827 = relay.Function([var_6815,], output)
mod['func_6827'] = func_6827
mod = relay.transform.InferType()(mod)
var_6828 = relay.var("var_6828", dtype = "float32", shape = (182,))#candidate|6828|(182,)|var|float32
output = func_6827(var_6828)
func_6829 = relay.Function([var_6828], output)
mutated_mod['func_6829'] = func_6829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4453_call = mod.get_global_var('func_4453')
func_4454_call = mutated_mod.get_global_var('func_4454')
call_6848 = relay.TupleGetItem(func_4453_call(), 0)
call_6849 = relay.TupleGetItem(func_4454_call(), 0)
output = relay.Tuple([call_6848,])
output2 = relay.Tuple([call_6849,])
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
func_1462_call = mod.get_global_var('func_1462')
func_1463_call = mutated_mod.get_global_var('func_1463')
call_6884 = func_1462_call()
call_6885 = func_1462_call()
output = call_6884
output2 = call_6885
func_6909 = relay.Function([], output)
mod['func_6909'] = func_6909
mod = relay.transform.InferType()(mod)
output = func_6909()
func_6910 = relay.Function([], output)
mutated_mod['func_6910'] = func_6910
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3396_call = mod.get_global_var('func_3396')
func_3398_call = mutated_mod.get_global_var('func_3398')
call_6920 = func_3396_call()
call_6921 = func_3396_call()
output = call_6920
output2 = call_6921
func_6931 = relay.Function([], output)
mod['func_6931'] = func_6931
mod = relay.transform.InferType()(mod)
mutated_mod['func_6931'] = func_6931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6931_call = mutated_mod.get_global_var('func_6931')
call_6932 = func_6931_call()
output = call_6932
func_6933 = relay.Function([], output)
mutated_mod['func_6933'] = func_6933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3396_call = mod.get_global_var('func_3396')
func_3398_call = mutated_mod.get_global_var('func_3398')
call_6934 = func_3396_call()
call_6935 = func_3396_call()
func_3040_call = mod.get_global_var('func_3040')
func_3043_call = mutated_mod.get_global_var('func_3043')
var_6939 = relay.var("var_6939", dtype = "int64", shape = ())#candidate|6939|()|var|int64
var_6940 = relay.var("var_6940", dtype = "uint8", shape = (40,))#candidate|6940|(40,)|var|uint8
call_6938 = relay.TupleGetItem(func_3040_call(relay.reshape(var_6939.astype('int64'), []), relay.reshape(var_6940.astype('uint8'), [40,]), ), 0)
call_6941 = relay.TupleGetItem(func_3043_call(relay.reshape(var_6939.astype('int64'), []), relay.reshape(var_6940.astype('uint8'), [40,]), ), 0)
output = relay.Tuple([call_6934,call_6938,var_6939,var_6940,])
output2 = relay.Tuple([call_6935,call_6941,var_6939,var_6940,])
func_6943 = relay.Function([var_6939,var_6940,], output)
mod['func_6943'] = func_6943
mod = relay.transform.InferType()(mod)
mutated_mod['func_6943'] = func_6943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6943_call = mutated_mod.get_global_var('func_6943')
var_6945 = relay.var("var_6945", dtype = "int64", shape = ())#candidate|6945|()|var|int64
var_6946 = relay.var("var_6946", dtype = "uint8", shape = (40,))#candidate|6946|(40,)|var|uint8
call_6944 = func_6943_call(var_6945,var_6946,)
output = call_6944
func_6947 = relay.Function([var_6945,var_6946,], output)
mutated_mod['func_6947'] = func_6947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4687_call = mod.get_global_var('func_4687')
func_4689_call = mutated_mod.get_global_var('func_4689')
call_6949 = relay.TupleGetItem(func_4687_call(), 0)
call_6950 = relay.TupleGetItem(func_4689_call(), 0)
output = relay.Tuple([call_6949,])
output2 = relay.Tuple([call_6950,])
func_6968 = relay.Function([], output)
mod['func_6968'] = func_6968
mod = relay.transform.InferType()(mod)
mutated_mod['func_6968'] = func_6968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6968_call = mutated_mod.get_global_var('func_6968')
call_6969 = func_6968_call()
output = call_6969
func_6970 = relay.Function([], output)
mutated_mod['func_6970'] = func_6970
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7034 = relay.var("var_7034", dtype = "float32", shape = (9, 15, 16))#candidate|7034|(9, 15, 16)|var|float32
uop_7035 = relay.log2(var_7034.astype('float32')) # shape=(9, 15, 16)
func_6165_call = mod.get_global_var('func_6165')
func_6168_call = mutated_mod.get_global_var('func_6168')
const_7044 = relay.const([[-2,4,3,7,-8,-4,3,10,-3,-2,-3,7,4,-9,-4,10,-10,-7,10,6,3,4,1,-3,-3,3,4,3,10,6,-1,-1,1,-3,-1,10,9,1,7,6,1,-7,-1,-4,4,-6,-6,-7,4,1,-1,1,-4,1,8,-3,-9,5,-3,-3,-7,-4,-6,4,-3,5,-6,3,1,-3,-3,8,-7,2,-10,-6,1,-3,-5,9,2,3,2,-7,-1,-2,7,4,2,3,-10,2,1,10,-2,3,5,-9,-1,10,7,4,-1,-9,6,-7,-10,-8,2,-6,-9,8,4,-10,4,-7,-3,6,-1,9,6,6,2,-9,-3,3,-4,7,8,5,1,-4,2,8,-8,5,-2,-2,-4,-3,5,-1,4,-9,7,-6,-5,-3,-4,-2,-8,4,5,-4,-6,8,-10,-2,-6,9,-4,-2,-5,6,5,-10,5,1,-2,3,-4,9,7,-10,-2,-8,2,-5,-4,6,9,2,-2,7,2,1,-8,-9,4,10,8,2,10,9,-8,-5,3,-4,2,10,-1,7,-3,-8,6,5,-6,6,-6,-1,-1,3,4,8,1,8,-9,3,3,-1,9,-5,-4,-2,7,7,10,2,9,9,-8,-2,-4,-10,-6,8,-8,-10,-5,3,6,1,-1,-9,3,-8,5,-9,-5,-7,-2,6,-9,2,-9,-7,-6,2,-1,6,6,-6,-4,-9,-4,1,1,-3,4,-6,2,-9,-2,-6,9,-9,-7,-8,-8,3,-5,-7,10,7,-7,8,-6,10,7,3,9,2,4,1,7,5,8,8,-2,-3,-8,8,7,2,-5,9,6,4,-1,4,-10,-10,1,-8,5,-3,4,6,1,-5,-2,2,6,-8,2,-5,-10,-3,-4,-5,-4,-1,10,-2,-5,9,3,-5,-9,6,-4,-4,-7,-7,-7,10,-1,-2,8,3,-4,3,6,-8,1,-4,6,-1,-2,6,1,3,-8,-2,-10,2,-9,-3,2,-8,5,10,-10,6,9,1,9,1,-10,6,10,-6,-10,2,10,5,-9,-9,-5,-1,9,6,10,7,-2,2,8,1,-8,-10,-10,-6,-9,10,-3,2,-6,2,-8,6,10,4,-5,-8,5,-1,-2,-7,-5,-4,-9,10,7,-1,-9,-4,4,-8,10,-4,-3,-1,-4,-3,7,-5,6,-4,-7,7,-4,6,-1,-9,-10,8,-5,-8,9,-10,-1,-3,-2,1,1,-5,8,-3,8,10,2,-1,8,10,3,4,-6,-2,-3,8,-10,1,4,9,-7,-10,-8,9,-4,-5,-8,-10,5,3,-6,4,-3,6,-8,-9,-5,-5,4,10,1,-3,-4,5,7,-7,-6,1,-5,-7,3,7,7,-2,6,-8,-9,7,-4,-5,8,-5,5,4,-2,-3,8,-2,4,7,10,-4,-6,4,-3,2,3,6,3,7,4,8,-10,1,8,1,-3,9,-7,-1,2,-2,1,2,-1,-9,9,-8,-10,2,-7,8,-1,9,-9,-10,4,-7,-3,10,10,-10,-7,-9,-7,6,5,2,-10,5,1,-10,9,-1,10,8,-9,8,-7,2,7,6,2,7,-10,9,10,-8,1,-3,9,1,-10,-3,-8,-10,2,9,7,6,-10,1,-6,-1,6,-10,-5,-4,-1,-3,1,6,-3,-7,-2,-8,-8,6,-7,3,-1,10,-5,3,1,-7,-3,-6,-9,-7,-6,7,3,9,10,-3,6,-7,8,-7,7,-9,-6,-7,10,9,-8,-1,10,10,4,1,9,-1,9,3,-1,-8,-1,-3,8,6,-8,8,-7,-10,-4,-10,-8,-7,6,-4,-6,3,9,6,-10,7,1,8,4,8,-8,2,-9,4,10,-2,4,2,5,-3,4,3,-5,-3,10,10,2,-5,-10,-8,-8,-7,-8,-6,-10,-8,-10,10,-3,-8,-6,2,-8,-9,-7,-1,7,-9,-6,10,7,10,8,-5,-3,-5,-1,7,5,10,-4,8,8,8,2,9,5,-9,7,5,6,9,8,-9,-3,-4,-1,-8,-8,2]], dtype = "int16")#candidate|7044|(1, 756)|const|int16
call_7043 = relay.TupleGetItem(func_6165_call(relay.reshape(const_7044.astype('int16'), [14, 9, 6])), 0)
call_7045 = relay.TupleGetItem(func_6168_call(relay.reshape(const_7044.astype('int16'), [14, 9, 6])), 0)
func_6909_call = mod.get_global_var('func_6909')
func_6910_call = mutated_mod.get_global_var('func_6910')
call_7046 = func_6909_call()
call_7047 = func_6909_call()
output = relay.Tuple([uop_7035,call_7043,const_7044,call_7046,])
output2 = relay.Tuple([uop_7035,call_7045,const_7044,call_7047,])
func_7050 = relay.Function([var_7034,], output)
mod['func_7050'] = func_7050
mod = relay.transform.InferType()(mod)
var_7051 = relay.var("var_7051", dtype = "float32", shape = (9, 15, 16))#candidate|7051|(9, 15, 16)|var|float32
output = func_7050(var_7051)
func_7052 = relay.Function([var_7051], output)
mutated_mod['func_7052'] = func_7052
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7140 = relay.const([[[10,-8,1,-8,-3,-8,-9,-5,5,7,-6,-3,2,5,1]],[[-9,-3,-7,6,3,-10,4,3,8,-5,1,3,-6,-1,2]]], dtype = "uint8")#candidate|7140|(2, 1, 15)|const|uint8
var_7141 = relay.var("var_7141", dtype = "uint8", shape = (2, 4, 15))#candidate|7141|(2, 4, 15)|var|uint8
bop_7142 = relay.bitwise_or(const_7140.astype('uint8'), var_7141.astype('uint8')) # shape=(2, 4, 15)
bop_7145 = relay.mod(var_7141.astype('float32'), const_7140.astype('float32')) # shape=(2, 4, 15)
uop_7151 = relay.sqrt(const_7140.astype('float32')) # shape=(2, 1, 15)
bop_7153 = relay.not_equal(uop_7151.astype('bool'), bop_7145.astype('bool')) # shape=(2, 4, 15)
output = relay.Tuple([bop_7142,bop_7153,])
output2 = relay.Tuple([bop_7142,bop_7153,])
func_7156 = relay.Function([var_7141,], output)
mod['func_7156'] = func_7156
mod = relay.transform.InferType()(mod)
mutated_mod['func_7156'] = func_7156
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7157 = relay.var("var_7157", dtype = "uint8", shape = (2, 4, 15))#candidate|7157|(2, 4, 15)|var|uint8
func_7156_call = mutated_mod.get_global_var('func_7156')
call_7158 = func_7156_call(var_7157)
output = call_7158
func_7159 = relay.Function([var_7157], output)
mutated_mod['func_7159'] = func_7159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4557_call = mod.get_global_var('func_4557')
func_4559_call = mutated_mod.get_global_var('func_4559')
call_7202 = relay.TupleGetItem(func_4557_call(), 0)
call_7203 = relay.TupleGetItem(func_4559_call(), 0)
output = call_7202
output2 = call_7203
func_7225 = relay.Function([], output)
mod['func_7225'] = func_7225
mod = relay.transform.InferType()(mod)
output = func_7225()
func_7226 = relay.Function([], output)
mutated_mod['func_7226'] = func_7226
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2257_call = mod.get_global_var('func_2257')
func_2258_call = mutated_mod.get_global_var('func_2258')
call_7233 = relay.TupleGetItem(func_2257_call(), 0)
call_7234 = relay.TupleGetItem(func_2258_call(), 0)
output = relay.Tuple([call_7233,])
output2 = relay.Tuple([call_7234,])
func_7243 = relay.Function([], output)
mod['func_7243'] = func_7243
mod = relay.transform.InferType()(mod)
mutated_mod['func_7243'] = func_7243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7243_call = mutated_mod.get_global_var('func_7243')
call_7244 = func_7243_call()
output = call_7244
func_7245 = relay.Function([], output)
mutated_mod['func_7245'] = func_7245
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7296 = relay.var("var_7296", dtype = "uint8", shape = (1, 10, 12))#candidate|7296|(1, 10, 12)|var|uint8
var_7297 = relay.var("var_7297", dtype = "uint8", shape = (14, 10, 12))#candidate|7297|(14, 10, 12)|var|uint8
bop_7298 = relay.less(var_7296.astype('bool'), var_7297.astype('bool')) # shape=(14, 10, 12)
var_7306 = relay.var("var_7306", dtype = "uint8", shape = (13, 10, 12))#candidate|7306|(13, 10, 12)|var|uint8
bop_7307 = relay.floor_mod(var_7296.astype('float64'), var_7306.astype('float64')) # shape=(13, 10, 12)
output = relay.Tuple([bop_7298,bop_7307,])
output2 = relay.Tuple([bop_7298,bop_7307,])
func_7311 = relay.Function([var_7296,var_7297,var_7306,], output)
mod['func_7311'] = func_7311
mod = relay.transform.InferType()(mod)
var_7312 = relay.var("var_7312", dtype = "uint8", shape = (1, 10, 12))#candidate|7312|(1, 10, 12)|var|uint8
var_7313 = relay.var("var_7313", dtype = "uint8", shape = (14, 10, 12))#candidate|7313|(14, 10, 12)|var|uint8
var_7314 = relay.var("var_7314", dtype = "uint8", shape = (13, 10, 12))#candidate|7314|(13, 10, 12)|var|uint8
output = func_7311(var_7312,var_7313,var_7314,)
func_7315 = relay.Function([var_7312,var_7313,var_7314,], output)
mutated_mod['func_7315'] = func_7315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3333_call = mod.get_global_var('func_3333')
func_3335_call = mutated_mod.get_global_var('func_3335')
call_7319 = relay.TupleGetItem(func_3333_call(), 1)
call_7320 = relay.TupleGetItem(func_3335_call(), 1)
uop_7326 = relay.log2(call_7319.astype('float64')) # shape=(3, 14, 4)
uop_7328 = relay.log2(call_7320.astype('float64')) # shape=(3, 14, 4)
uop_7340 = relay.tan(uop_7326.astype('float32')) # shape=(3, 14, 4)
uop_7342 = relay.tan(uop_7328.astype('float32')) # shape=(3, 14, 4)
output = relay.Tuple([uop_7340,])
output2 = relay.Tuple([uop_7342,])
func_7343 = relay.Function([], output)
mod['func_7343'] = func_7343
mod = relay.transform.InferType()(mod)
mutated_mod['func_7343'] = func_7343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7343_call = mutated_mod.get_global_var('func_7343')
call_7344 = func_7343_call()
output = call_7344
func_7345 = relay.Function([], output)
mutated_mod['func_7345'] = func_7345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5405_call = mod.get_global_var('func_5405')
func_5407_call = mutated_mod.get_global_var('func_5407')
call_7349 = relay.TupleGetItem(func_5405_call(), 0)
call_7350 = relay.TupleGetItem(func_5407_call(), 0)
func_6106_call = mod.get_global_var('func_6106')
func_6109_call = mutated_mod.get_global_var('func_6109')
var_7355 = relay.var("var_7355", dtype = "int16", shape = (375,))#candidate|7355|(375,)|var|int16
call_7354 = relay.TupleGetItem(func_6106_call(relay.reshape(var_7355.astype('int16'), [375,])), 1)
call_7356 = relay.TupleGetItem(func_6109_call(relay.reshape(var_7355.astype('int16'), [375,])), 1)
func_4413_call = mod.get_global_var('func_4413')
func_4415_call = mutated_mod.get_global_var('func_4415')
call_7402 = relay.TupleGetItem(func_4413_call(), 0)
call_7403 = relay.TupleGetItem(func_4415_call(), 0)
func_7050_call = mod.get_global_var('func_7050')
func_7052_call = mutated_mod.get_global_var('func_7052')
var_7413 = relay.var("var_7413", dtype = "float32", shape = (2160,))#candidate|7413|(2160,)|var|float32
call_7412 = relay.TupleGetItem(func_7050_call(relay.reshape(var_7413.astype('float32'), [9, 15, 16])), 1)
call_7414 = relay.TupleGetItem(func_7052_call(relay.reshape(var_7413.astype('float32'), [9, 15, 16])), 1)
func_2164_call = mod.get_global_var('func_2164')
func_2166_call = mutated_mod.get_global_var('func_2166')
call_7420 = func_2164_call()
call_7421 = func_2164_call()
output = relay.Tuple([call_7349,call_7354,var_7355,call_7402,call_7412,var_7413,call_7420,])
output2 = relay.Tuple([call_7350,call_7356,var_7355,call_7403,call_7414,var_7413,call_7421,])
func_7423 = relay.Function([var_7355,var_7413,], output)
mod['func_7423'] = func_7423
mod = relay.transform.InferType()(mod)
var_7424 = relay.var("var_7424", dtype = "int16", shape = (375,))#candidate|7424|(375,)|var|int16
var_7425 = relay.var("var_7425", dtype = "float32", shape = (2160,))#candidate|7425|(2160,)|var|float32
output = func_7423(var_7424,var_7425,)
func_7426 = relay.Function([var_7424,var_7425,], output)
mutated_mod['func_7426'] = func_7426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4413_call = mod.get_global_var('func_4413')
func_4415_call = mutated_mod.get_global_var('func_4415')
call_7467 = relay.TupleGetItem(func_4413_call(), 0)
call_7468 = relay.TupleGetItem(func_4415_call(), 0)
func_7343_call = mod.get_global_var('func_7343')
func_7345_call = mutated_mod.get_global_var('func_7345')
call_7486 = relay.TupleGetItem(func_7343_call(), 0)
call_7487 = relay.TupleGetItem(func_7345_call(), 0)
output = relay.Tuple([call_7467,call_7486,])
output2 = relay.Tuple([call_7468,call_7487,])
func_7488 = relay.Function([], output)
mod['func_7488'] = func_7488
mod = relay.transform.InferType()(mod)
mutated_mod['func_7488'] = func_7488
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7488_call = mutated_mod.get_global_var('func_7488')
call_7489 = func_7488_call()
output = call_7489
func_7490 = relay.Function([], output)
mutated_mod['func_7490'] = func_7490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7225_call = mod.get_global_var('func_7225')
func_7226_call = mutated_mod.get_global_var('func_7226')
call_7523 = func_7225_call()
call_7524 = func_7225_call()
output = relay.Tuple([call_7523,])
output2 = relay.Tuple([call_7524,])
func_7530 = relay.Function([], output)
mod['func_7530'] = func_7530
mod = relay.transform.InferType()(mod)
mutated_mod['func_7530'] = func_7530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7530_call = mutated_mod.get_global_var('func_7530')
call_7531 = func_7530_call()
output = call_7531
func_7532 = relay.Function([], output)
mutated_mod['func_7532'] = func_7532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2943_call = mod.get_global_var('func_2943')
func_2944_call = mutated_mod.get_global_var('func_2944')
call_7560 = func_2943_call()
call_7561 = func_2943_call()
func_3333_call = mod.get_global_var('func_3333')
func_3335_call = mutated_mod.get_global_var('func_3335')
call_7570 = relay.TupleGetItem(func_3333_call(), 2)
call_7571 = relay.TupleGetItem(func_3335_call(), 2)
func_6968_call = mod.get_global_var('func_6968')
func_6970_call = mutated_mod.get_global_var('func_6970')
call_7573 = relay.TupleGetItem(func_6968_call(), 0)
call_7574 = relay.TupleGetItem(func_6970_call(), 0)
func_2173_call = mod.get_global_var('func_2173')
func_2175_call = mutated_mod.get_global_var('func_2175')
call_7578 = func_2173_call()
call_7579 = func_2173_call()
func_5870_call = mod.get_global_var('func_5870')
func_5871_call = mutated_mod.get_global_var('func_5871')
call_7580 = relay.TupleGetItem(func_5870_call(), 2)
call_7581 = relay.TupleGetItem(func_5871_call(), 2)
func_2525_call = mod.get_global_var('func_2525')
func_2526_call = mutated_mod.get_global_var('func_2526')
call_7583 = relay.TupleGetItem(func_2525_call(), 0)
call_7584 = relay.TupleGetItem(func_2526_call(), 0)
func_3396_call = mod.get_global_var('func_3396')
func_3398_call = mutated_mod.get_global_var('func_3398')
call_7585 = func_3396_call()
call_7586 = func_3396_call()
output = relay.Tuple([call_7560,call_7570,call_7573,call_7578,call_7580,call_7583,call_7585,])
output2 = relay.Tuple([call_7561,call_7571,call_7574,call_7579,call_7581,call_7584,call_7586,])
func_7588 = relay.Function([], output)
mod['func_7588'] = func_7588
mod = relay.transform.InferType()(mod)
output = func_7588()
func_7589 = relay.Function([], output)
mutated_mod['func_7589'] = func_7589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2682_call = mod.get_global_var('func_2682')
func_2684_call = mutated_mod.get_global_var('func_2684')
call_7609 = func_2682_call()
call_7610 = func_2682_call()
output = relay.Tuple([call_7609,])
output2 = relay.Tuple([call_7610,])
func_7617 = relay.Function([], output)
mod['func_7617'] = func_7617
mod = relay.transform.InferType()(mod)
output = func_7617()
func_7618 = relay.Function([], output)
mutated_mod['func_7618'] = func_7618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3396_call = mod.get_global_var('func_3396')
func_3398_call = mutated_mod.get_global_var('func_3398')
call_7619 = func_3396_call()
call_7620 = func_3396_call()
output = relay.Tuple([call_7619,])
output2 = relay.Tuple([call_7620,])
func_7641 = relay.Function([], output)
mod['func_7641'] = func_7641
mod = relay.transform.InferType()(mod)
output = func_7641()
func_7642 = relay.Function([], output)
mutated_mod['func_7642'] = func_7642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5570_call = mod.get_global_var('func_5570')
func_5571_call = mutated_mod.get_global_var('func_5571')
call_7689 = relay.TupleGetItem(func_5570_call(), 0)
call_7690 = relay.TupleGetItem(func_5571_call(), 0)
output = relay.Tuple([call_7689,])
output2 = relay.Tuple([call_7690,])
func_7691 = relay.Function([], output)
mod['func_7691'] = func_7691
mod = relay.transform.InferType()(mod)
mutated_mod['func_7691'] = func_7691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7691_call = mutated_mod.get_global_var('func_7691')
call_7692 = func_7691_call()
output = call_7692
func_7693 = relay.Function([], output)
mutated_mod['func_7693'] = func_7693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4557_call = mod.get_global_var('func_4557')
func_4559_call = mutated_mod.get_global_var('func_4559')
call_7794 = relay.TupleGetItem(func_4557_call(), 0)
call_7795 = relay.TupleGetItem(func_4559_call(), 0)
output = relay.Tuple([call_7794,])
output2 = relay.Tuple([call_7795,])
func_7803 = relay.Function([], output)
mod['func_7803'] = func_7803
mod = relay.transform.InferType()(mod)
mutated_mod['func_7803'] = func_7803
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7803_call = mutated_mod.get_global_var('func_7803')
call_7804 = func_7803_call()
output = call_7804
func_7805 = relay.Function([], output)
mutated_mod['func_7805'] = func_7805
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5818_call = mod.get_global_var('func_5818')
func_5820_call = mutated_mod.get_global_var('func_5820')
call_7826 = func_5818_call()
call_7827 = func_5818_call()
output = relay.Tuple([call_7826,])
output2 = relay.Tuple([call_7827,])
func_7837 = relay.Function([], output)
mod['func_7837'] = func_7837
mod = relay.transform.InferType()(mod)
mutated_mod['func_7837'] = func_7837
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7837_call = mutated_mod.get_global_var('func_7837')
call_7838 = func_7837_call()
output = call_7838
func_7839 = relay.Function([], output)
mutated_mod['func_7839'] = func_7839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7588_call = mod.get_global_var('func_7588')
func_7589_call = mutated_mod.get_global_var('func_7589')
call_7911 = relay.TupleGetItem(func_7588_call(), 4)
call_7912 = relay.TupleGetItem(func_7589_call(), 4)
output = relay.Tuple([call_7911,])
output2 = relay.Tuple([call_7912,])
func_7919 = relay.Function([], output)
mod['func_7919'] = func_7919
mod = relay.transform.InferType()(mod)
output = func_7919()
func_7920 = relay.Function([], output)
mutated_mod['func_7920'] = func_7920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7641_call = mod.get_global_var('func_7641')
func_7642_call = mutated_mod.get_global_var('func_7642')
call_7940 = relay.TupleGetItem(func_7641_call(), 0)
call_7941 = relay.TupleGetItem(func_7642_call(), 0)
output = relay.Tuple([call_7940,])
output2 = relay.Tuple([call_7941,])
func_7956 = relay.Function([], output)
mod['func_7956'] = func_7956
mod = relay.transform.InferType()(mod)
output = func_7956()
func_7957 = relay.Function([], output)
mutated_mod['func_7957'] = func_7957
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7963 = relay.var("var_7963", dtype = "uint64", shape = (15, 2, 12))#candidate|7963|(15, 2, 12)|var|uint64
var_7964 = relay.var("var_7964", dtype = "uint64", shape = (15, 2, 12))#candidate|7964|(15, 2, 12)|var|uint64
bop_7965 = relay.subtract(var_7963.astype('uint64'), relay.reshape(var_7964.astype('uint64'), relay.shape_of(var_7963))) # shape=(15, 2, 12)
func_5144_call = mod.get_global_var('func_5144')
func_5147_call = mutated_mod.get_global_var('func_5147')
var_7969 = relay.var("var_7969", dtype = "float32", shape = (1, 840))#candidate|7969|(1, 840)|var|float32
call_7968 = relay.TupleGetItem(func_5144_call(relay.reshape(var_7969.astype('float32'), [8, 15, 7])), 0)
call_7970 = relay.TupleGetItem(func_5147_call(relay.reshape(var_7969.astype('float32'), [8, 15, 7])), 0)
func_2682_call = mod.get_global_var('func_2682')
func_2684_call = mutated_mod.get_global_var('func_2684')
call_7972 = func_2682_call()
call_7973 = func_2682_call()
func_2887_call = mod.get_global_var('func_2887')
func_2888_call = mutated_mod.get_global_var('func_2888')
call_7989 = func_2887_call()
call_7990 = func_2887_call()
bop_7995 = relay.logical_xor(var_7969.astype('int32'), relay.reshape(call_7968.astype('int32'), relay.shape_of(var_7969))) # shape=(1, 840)
bop_7998 = relay.logical_xor(var_7969.astype('int32'), relay.reshape(call_7970.astype('int32'), relay.shape_of(var_7969))) # shape=(1, 840)
func_3751_call = mod.get_global_var('func_3751')
func_3755_call = mutated_mod.get_global_var('func_3755')
const_8000 = relay.const([1,2,-7,-1,4,-4,8,-3,-4,-4,7,-8,-9,1,5,6,7,1,10,2,1,-8,-3,-8,8,-1,-3,7,10,-4,5,10,-9,7,-2,7,2,4,6,10,3,-2,-10,10,6,-4,5,-4,-4,-6,-9,4,8,-5,-10,-2,-8,-9,5,10,-5,-4,-10,-5,-1,-3,-3,10,-4,8,3,7,4,4,9,-1,-10,-5,5,-5,10,-7,-4,4,5,4,-2,1,-10,5,9,-4,-1,7,10,2,-1,-4,-7,5,-2,10,-1,-10,-4,-2,1,1,-6,7,2,5,10,8,-8,9,-3,4,8,7,-10,-6,-5,-2,5,7,1,-9,-1,-10,2,-9,-8,1,8,9,-6,-9,-2,-2,-10,-4,-10,2,2,10,-1,10,-3,-7,-10,-1,3,-7,-8,-2,9,9,-1,-1,-5,8,10,-7,-1,-6,-3,7,-4,1,-5,-2,10,-6,-6,-3,-7,-1,1,2,4,-2,4,3,4,-3,6,5,-1,-7,7,-2,-3,3,-10,-7,-4,1,8,9,-7,-3,10,-9,9,9,-7,2,1,7,4,-6,-5,-8,1,5,10,3,5,2,-9,2,2,-8,-1,6,1,4,3,8,-1,-3,10,2,7,1,-7,-4,9,3,8,-7,-5,2,-5,1,-3,7,-10,1,5,3,-7,2,-10,-5,-6,7,3,9,-2,-6,-5,-2,-3,2,7,1,-4,-9,8,7,8,5,-5,-1,-7,6,9,-6,-3,2,6,5,6,6,-9,8,-7,1,9,3,-9,7,6,-4,-2,10,-2,7,8,2,6,-7,4,7,9,9,-8,10,10,5,-10,7,8,10,9,7,3,-8,-3,-2,4,2,8,8,-6,9,7,-8,1,-3,1,4,6,-2,-9,-1,6,9,-7,-1,9,1,-5,1,8,-6,5,-4,4,-10,-10,7,6,9,2,-6,-9,7,5,-2,1,3,-10,7,-3,-6,-9,7,1,-7,-6,-6,-10,-1,-10,-8,-2,8,-8,-5,-5,-3,6,-8,-6,1,-9,-6,-1,-4,9,3,4,1,-10,2,9,-8,5,-3,-2,-2,-3,-10,5,-7,-7,-6,-4,3,-5,-9,-2,1,-4,10,-1,9,-1,10,2,-2,6,7,9,3,-7,-10,1,8,-6,-3,1,10,-8,1,8,8,3,5,9,8,2,5,-1,-1,1,3,6,7,-6,6,2,-7,3,-1,-1,6,-8,7,8,-6,1,-3,5,-1,-10,6,-4,9,6,-8,8,10,-9,-5,4,5,3,2,-10,2,1,2,-2,3,-10,4,-4,-5,-1,9,-4,-1,-2,8,6,-10,7,-4,-2,6,7,1,6,4,8,3,6,10,6,10,7,1,-3,-2,2,-8,-2,10,-8,-5,8,8,-1,3,-6,9,4,-7,7,-3,-9,-9,1,9,6,6,4,-1,4,-2,9,-6,-5,2,-4,2,8,-6,-3,-8,1,-4,-10,9,8,-6,5,2,7,-4,8,8,-9,5,-9,10,9,-4,8,-4,-7,5,-6,-3,-10,-6,3,6,-8,2,6,-9,8,7,-9,4,3,9,4,-2,7,5,-4,9,-2,1,-7,-4,-6,-2,-1,-2,-4,2,10,-6,-4,6,2,9,-10,-1,-1,-1,5,3,-10,10,5,-3,8,4,10,9,9,7,8,-4,4,-7,1,-5,-8,-4,-1,-10,8,-2,-5,-2,8,-4,7,7,-5,10,-6,-6,4,-7,-1,-3,-2,1,7,-4,3,3,-5,-1,7,-6,-10,9,-6,-8,-5,8,-7,7,-2,-9,6,-5,2,-3,1,4,-4,5,9,-7,-6,4,-3,5,1,-10,-6,9,-5,9,-2,7,-5,-3,8,9,-6,5,-1,7,-6,10,-4,-4,-9,-4,5,6,4,4,-1,5,-5,9,3,-9,-2,3,-8,-4,-7,8,10,3,5,-7,10,4,-2,-1,-8,4,-9,-4,3,4,6,3,7,-3,3,9,-2,9,7,-1,-2,2,1,8,6,3,7,-10,-1,-7,3,-8,-10,-8,-6,-1,-3,10,9,-9,2,-6,9,-5,9,7,-9,-6,9,-9,3,3,-3,10,-1,-6,3,3,-10,-4,-10,2,3,2,1,9,9,10,5,5,-10,-8,-5,-5,-7,7,-10,-9,-6,-9,2,1,-1,5,-10,9,-1,3,8,-2,-8,4,-9,-3,6,4,-9,1,-7,-6,-7,8,-4,6,10,-10,-9,8,-9,-3,-2,-5,3,3,-2,-6,5,-7,-5,-4,-2,-5,9,9,4,-7,10,-1,7,10,6,10,-9,2,-1,1,1,6,-9,1,6,4,-9,-8,3,-8,5,-10,-7,10,-3,3,9,5,2,-5,-4,-6,-6,-9,-4,7,5,4,4,-9,-7,10,-2,3,-2,4,-7,-9,7,-3,-5,10,2,1,2,-2,4,4,-10,10,5,-8,-6,-9,-4,-6,3,-8,-4,10,3,-4,5,-3,-4,6,8,-6,-10,-1,-7,5,5,-6,4,-4,7,4,-5,-8,-1,-2,8,-5,-3,5,3,2,3,8,4,-4,1,7,-6,-9,-9,6,-1,8,-7,-5,-4,10,-5,-5,-4,3,9,-3,3,10,5,1,-6,9,3,4,3,3,4,-8,-8,-4,-1,2,1,7,-9,-1,7,-8,5,6,-8,5,-8,2,6,-5,-5,2,-10,-3,9,-5,5,7,-7,-8,-3,-1,-8,8,-9,2,9,-1,4,9,-7,10,-8,-1,-1,2,-2,4,5,7,-5,9,4,5,3,3,-8,3,-1,5,-3,-3,-9,6,-9,10,-1,-9,9,5,10,2,-3,8,-9,-6,-9,7,6,-3,-8,2,-2,-6,-7,-10,1,6,9,7,-4,-10,2,2,3,-6,10,2,-8,-10,-1,1,4,-5,-9,1,-5,-10,-10,-6,10,4,9,10,6,4,2,-9,-1,1,9,7,5,-3,-10,8,3,7,-9,3,9,-3,1,9,-8,-5,-2,-3,10,10,6,-1,9,5,7,5,3,8,2,7,-6,9,5,-3,-7,-6,-2,-4,-4,-10,4,10,-5,-1,-6,7,1,9,7,2,8,6,6,10,-8,-5,-6,-2,-1,-8,-3,8,2,-3,-3,2,4,1,10,4,-2,2,1,-10,9,9,4,10,-9,4,8,3,-6,4,6,3,6,-7,-1,9,-5,-4,10,-7,-6,2,7,-6,2,6,-9,-5,6,1,-10,-9,-1,-6,-8,-9,-3,8,6,10,7,5,7,-10,3,4,10,-10,8,-1,8,3,-8,-1,7,2,7,10,9,-1,-9,-6,8,-1,4,7,1,3,-10,-6,6,-9,-7,-1,8,9,-4,-8,2,3,1,-8,-7,-4,7,-4,-9,-8,-3,-3,10,8,-6,8,-6,-4,8,-1,-6,4,8,8,2,-6,-4,5,10,8,2,5,-7,-8,2,-2,6,-2,3,-4,6,1,8,6,1,-3,1,2,-5,-5,-10,7,-4,-2,1,-5,5,-8,1,-8,-7,-9,7,8,-2,2,3,-1,8,-5,9,-5,5,-7,7,-3,6,-5,-3,-8,-8,-10,10,8,-5,7,5,10,5,-8,-5,-1,3,6,10,3,-4,9,-4,-10,-1,5,-10,4,4,-10,-3,8,6,3,7,4,-9,-5,-9,4,-3,6,5,1,-3,6,3,-3,-1,-4,2,-10,-2,-6,10,-1,-10,-6,-6,-6,-7,7,8,8,-4,-8,2,-7,-4,7,4,7,-4,1,-10,-1,9,7,-5,9,-9,8,-6,6,-10,4,-1,-10,-3,-7,7,-2,-7,8,-3,-3,-5,-4,8,10,4,-3,-4,2,-3,-10,10,-1,-2,8,5,8,2,10,5,-9,-4,6,3,-5,10,1,9,4,10,-7,-3,6,10,-9,-5,-3,-9,7,8,2,-9,-5,-4,10,-3,8,3,-5,-9,-7,3,5,1,-5,6,-7,10,-5,-5,8,-1,5,-10,8,-5,6,-7,1,7,-8,-5,7,-9,2,7,-3,6,-6,-8,-10,9,4,-8,-5,1,7,-8,-3,-9,2,-5,-8,-1,-9,-9,6,6,-6,-3,9,-4,-1,-3,1,7,9,6,-3,10,-10,3,-8,7,3,-5,-5,-9,3,-1,3,8,2,-7,-5,-8,-7,2,-10,-9,9,5,3,2,-5,10,1,-8,-2,-9,-2,-1,-10,4,1,2,7,6,1,-8,9,2,6,4,-5,-4,-1,-7,9,10,-7,10,10,-6,3,7,1,-3,-1,4,1,-6,4,-1,7,3,-4,7,-8,-4,6,3,3,6,-5,2,10,-8,1,9,3,-1,-4,10,3,5,7,9,-3,6,7,6,5,-4,-5,6,7], dtype = "uint32")#candidate|8000|(1638,)|const|uint32
var_8001 = relay.var("var_8001", dtype = "bool", shape = (52, 1))#candidate|8001|(52, 1)|var|bool
call_7999 = relay.TupleGetItem(func_3751_call(relay.reshape(const_8000.astype('uint32'), [546, 3]), relay.reshape(var_8001.astype('bool'), [52,]), ), 2)
call_8002 = relay.TupleGetItem(func_3755_call(relay.reshape(const_8000.astype('uint32'), [546, 3]), relay.reshape(var_8001.astype('bool'), [52,]), ), 2)
output = relay.Tuple([bop_7965,call_7972,call_7989,bop_7995,call_7999,const_8000,var_8001,])
output2 = relay.Tuple([bop_7965,call_7973,call_7990,bop_7998,call_8002,const_8000,var_8001,])
func_8010 = relay.Function([var_7963,var_7964,var_7969,var_8001,], output)
mod['func_8010'] = func_8010
mod = relay.transform.InferType()(mod)
var_8011 = relay.var("var_8011", dtype = "uint64", shape = (15, 2, 12))#candidate|8011|(15, 2, 12)|var|uint64
var_8012 = relay.var("var_8012", dtype = "uint64", shape = (15, 2, 12))#candidate|8012|(15, 2, 12)|var|uint64
var_8013 = relay.var("var_8013", dtype = "float32", shape = (1, 840))#candidate|8013|(1, 840)|var|float32
var_8014 = relay.var("var_8014", dtype = "bool", shape = (52, 1))#candidate|8014|(52, 1)|var|bool
output = func_8010(var_8011,var_8012,var_8013,var_8014,)
func_8015 = relay.Function([var_8011,var_8012,var_8013,var_8014,], output)
mutated_mod['func_8015'] = func_8015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2525_call = mod.get_global_var('func_2525')
func_2526_call = mutated_mod.get_global_var('func_2526')
call_8037 = relay.TupleGetItem(func_2525_call(), 2)
call_8038 = relay.TupleGetItem(func_2526_call(), 2)
func_4372_call = mod.get_global_var('func_4372')
func_4374_call = mutated_mod.get_global_var('func_4374')
call_8045 = func_4372_call(relay.reshape(call_8037.astype('int8'), [8, 14, 2]))
call_8046 = func_4372_call(relay.reshape(call_8037.astype('int8'), [8, 14, 2]))
func_5790_call = mod.get_global_var('func_5790')
func_5792_call = mutated_mod.get_global_var('func_5792')
var_8065 = relay.var("var_8065", dtype = "int16", shape = (375,))#candidate|8065|(375,)|var|int16
call_8064 = relay.TupleGetItem(func_5790_call(relay.reshape(var_8065.astype('int16'), [375,])), 1)
call_8066 = relay.TupleGetItem(func_5792_call(relay.reshape(var_8065.astype('int16'), [375,])), 1)
uop_8069 = relay.acosh(var_8065.astype('float32')) # shape=(375,)
output = relay.Tuple([call_8037,call_8045,call_8064,uop_8069,])
output2 = relay.Tuple([call_8038,call_8046,call_8066,uop_8069,])
func_8072 = relay.Function([var_8065,], output)
mod['func_8072'] = func_8072
mod = relay.transform.InferType()(mod)
var_8073 = relay.var("var_8073", dtype = "int16", shape = (375,))#candidate|8073|(375,)|var|int16
output = func_8072(var_8073)
func_8074 = relay.Function([var_8073], output)
mutated_mod['func_8074'] = func_8074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7691_call = mod.get_global_var('func_7691')
func_7693_call = mutated_mod.get_global_var('func_7693')
call_8084 = relay.TupleGetItem(func_7691_call(), 0)
call_8085 = relay.TupleGetItem(func_7693_call(), 0)
func_3661_call = mod.get_global_var('func_3661')
func_3662_call = mutated_mod.get_global_var('func_3662')
call_8088 = relay.TupleGetItem(func_3661_call(), 1)
call_8089 = relay.TupleGetItem(func_3662_call(), 1)
output = relay.Tuple([call_8084,call_8088,])
output2 = relay.Tuple([call_8085,call_8089,])
func_8105 = relay.Function([], output)
mod['func_8105'] = func_8105
mod = relay.transform.InferType()(mod)
output = func_8105()
func_8106 = relay.Function([], output)
mutated_mod['func_8106'] = func_8106
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7530_call = mod.get_global_var('func_7530')
func_7532_call = mutated_mod.get_global_var('func_7532')
call_8160 = relay.TupleGetItem(func_7530_call(), 0)
call_8161 = relay.TupleGetItem(func_7532_call(), 0)
output = relay.Tuple([call_8160,])
output2 = relay.Tuple([call_8161,])
func_8172 = relay.Function([], output)
mod['func_8172'] = func_8172
mod = relay.transform.InferType()(mod)
output = func_8172()
func_8173 = relay.Function([], output)
mutated_mod['func_8173'] = func_8173
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8210 = relay.const([[[-0.941893,0.333829,9.066093,0.430424,1.168519,-6.146816,3.192121,-8.652733,5.797967,6.994229,4.421120,7.243792,5.686955],[-9.674453,5.039028,-2.282445,3.887986,-3.838267,5.617405,-7.519451,-0.917283,2.712726,-1.576798,8.492179,9.815045,-3.524645],[-2.323475,4.249253,0.902506,-0.885511,8.036930,-3.047160,-6.059036,-3.946938,-1.695429,-5.480168,2.368880,9.146522,3.372671],[9.786108,4.046967,-7.671977,-7.196350,-0.292710,2.065238,-2.211647,9.533668,-5.030028,3.521262,7.247564,7.016148,5.320284],[-6.645910,-4.679173,0.669728,-1.956416,5.477813,-5.801915,2.718003,-9.943865,-0.916401,4.711368,1.265199,0.215693,-4.399070],[1.241251,3.465851,4.702030,6.557281,8.898705,9.916586,8.770384,-5.511246,-0.194275,-3.150402,3.008444,-4.962486,-4.844533],[-7.271026,-2.227782,3.854204,-9.823185,-1.833886,-3.526968,8.492327,-7.375593,2.331762,6.593652,-3.043505,0.128463,-8.439899],[8.463638,-6.872648,3.166124,2.017809,2.984235,6.671794,6.842549,3.188827,7.842561,-5.200090,-3.870260,7.576433,3.827018],[2.169090,7.201778,2.592089,-0.311404,-0.799463,-0.496750,-1.018522,-1.948679,1.774852,7.859510,2.296536,7.665963,0.431035],[-7.787845,-3.564220,-2.904833,-8.567335,4.377061,-7.175744,6.072708,3.487820,-4.421534,-4.491276,3.540309,4.384267,-7.699213],[6.188522,-2.335697,2.335344,-6.781374,-3.639330,-0.012153,-3.383876,3.639441,6.486417,2.987111,-7.262750,-6.244531,3.548631],[2.803212,3.886656,5.776155,6.832294,6.587319,-5.194985,-3.440895,-4.264764,-5.872410,7.149059,8.167683,-9.544727,8.519520]],[[-6.321613,2.210500,-0.920529,-4.887852,0.008006,-8.093997,8.103774,0.786809,5.909580,9.461562,-0.214335,-0.638435,3.905972],[4.751636,4.699476,-8.887281,-8.366808,4.009412,-8.405748,-4.021957,5.872841,8.177900,-2.479875,4.537736,-1.308405,5.493076],[-2.835475,-2.955187,9.180709,8.689871,1.068826,4.954944,-0.893889,-3.205606,-4.410992,-0.482264,9.983332,2.697886,-6.152113],[-8.357654,3.986280,-6.678181,3.768915,5.967970,-6.258582,9.998411,-7.048893,8.289814,2.596550,-6.706055,4.324495,-6.739294],[-2.881786,-4.243315,-1.062230,6.143559,7.100784,7.255438,4.810800,7.744922,9.607990,1.248615,5.555554,-0.018331,-6.247939],[5.555415,6.399149,-0.204545,2.315491,2.785416,8.077469,7.638856,-1.303322,-3.456149,0.153625,7.339359,-3.280631,-1.465385],[2.727956,7.780849,6.177109,8.062195,-8.004270,-1.102726,0.358221,3.780366,9.044447,6.708080,9.946983,3.620945,9.573543],[8.174423,8.681884,-9.306431,3.114088,-5.442224,-3.704691,8.220931,8.336115,-9.570593,3.643000,-9.622565,-5.632750,-6.804509],[1.660237,-7.377726,-9.082019,-1.092579,4.238244,9.412937,-9.260673,-7.437346,1.998624,8.371823,1.954549,4.286489,4.448942],[0.397136,9.833739,7.289518,0.736467,-8.183129,-7.748141,1.524701,9.356674,-4.242046,-8.340371,-0.507403,-0.799325,4.201931],[0.682250,0.402245,-7.374918,-1.786180,-5.132551,-0.770638,0.265867,-8.680940,7.089722,6.197018,-1.002672,6.793242,-9.884721],[-9.588660,1.140308,2.169759,1.161905,-7.393327,8.459984,1.729316,-1.066300,-6.437091,-4.746431,5.696106,-4.458855,-8.729196]],[[-8.018306,-4.541828,1.432992,-5.242766,-6.587267,5.695576,-7.906621,0.371817,-7.072769,0.111636,-5.187095,-0.233461,-0.327999],[-8.400866,0.606806,9.193492,-9.812729,-4.276996,9.830670,3.645661,-5.538913,8.529248,-4.079987,4.427044,6.739188,1.039953],[-9.460685,6.041746,-0.936608,0.602966,-1.659246,9.282435,-6.915932,9.208707,-0.695828,9.499349,3.109542,6.920717,7.931823],[1.411397,-2.843032,-0.894791,-0.209025,2.385958,-4.991782,-9.178013,-9.283340,7.145398,-4.308180,-8.090822,9.130331,4.079613],[-1.198435,-1.283299,1.872077,-7.421625,3.762687,-8.785921,-8.430904,-1.579748,9.400685,-2.399335,-6.639890,-5.447722,-5.082880],[-2.891751,1.992602,-2.873058,-9.605947,1.301254,-5.659160,0.797932,4.810856,-6.965254,-0.890023,-4.287404,5.806492,4.497419],[-0.486483,-0.114295,-0.782808,1.441506,4.349138,7.848248,-2.976187,7.241332,-5.704667,-9.568688,6.188474,-0.390279,6.161204],[5.504436,4.952824,3.696874,-4.142566,-5.453803,-2.378386,-9.248498,0.401896,6.064419,6.037992,1.362446,-0.687642,3.898583],[-7.773385,5.618543,-5.965998,-2.783030,0.414210,2.001206,-2.764168,-4.405547,9.745473,-0.536829,-3.423007,9.748739,-9.737509],[4.713701,-7.442947,-0.643869,-1.109442,7.495090,-7.360608,-9.224112,2.234380,-4.449244,1.974458,-8.349690,2.932250,-0.378784],[-6.386749,5.730481,-1.873785,5.202567,5.054786,0.300113,0.851172,-0.025541,-9.520641,5.858970,6.916262,3.449143,-6.485827],[5.888136,-9.750151,9.767926,9.328409,-4.752101,-7.356021,4.667247,2.801564,7.456054,6.223889,9.696728,2.734169,4.695973]],[[-5.084317,2.466900,-5.219779,-0.908733,-3.328557,2.511621,9.202243,2.411260,-6.603085,1.224882,3.895190,-7.804559,2.520010],[2.710775,8.500487,8.829791,8.811625,-0.972623,2.113571,5.266417,1.430045,-3.518230,-1.083031,-2.741633,-5.347649,-5.121802],[-3.888585,-9.840423,-8.811864,-2.193252,-9.762946,0.394034,0.351659,2.504521,2.170879,-0.898668,2.039126,7.750991,4.914948],[-9.554034,4.550642,2.321833,-8.614411,1.201186,1.053324,-3.552274,1.723842,-6.143579,7.601859,-5.212859,-8.028489,0.036331],[6.361805,9.125826,-3.621762,-3.970129,-3.621623,-1.692125,0.032020,-0.750292,8.497790,-8.537905,-4.714933,3.793356,-2.492301],[-4.953903,2.805138,-8.721224,-4.316844,8.770745,-5.333944,3.739503,2.951079,0.029602,0.453944,-7.147306,-0.966240,-1.204727],[9.970435,-0.961204,1.858589,-5.803162,6.396441,6.525376,-9.474152,-6.973590,-0.314012,3.584883,8.163000,-5.530794,-5.932992],[-1.558429,2.764894,-0.954012,-4.953561,-7.012847,7.927335,-6.824933,6.368452,6.137125,-0.431945,-8.396946,3.128120,8.816098],[-5.107907,0.719547,-3.302600,4.689185,-1.181615,-5.416968,8.148259,-7.112667,1.964730,8.623944,-5.103510,-7.330181,-7.589872],[3.760166,-9.609045,4.444086,-2.455479,-7.326385,-9.392163,-2.051274,2.326541,3.337308,9.641884,7.521052,1.656281,-7.773531],[7.299586,-7.666578,9.540783,9.395704,-6.846406,2.283945,-5.467762,0.530488,7.825994,2.178640,-6.420334,6.845251,3.428474],[-4.192844,7.663831,-7.013764,8.949341,7.565890,6.246527,4.963597,5.151881,-0.851958,-7.164353,-8.315939,-5.333473,-2.093191]],[[-8.447695,-2.850169,-0.226833,-4.004943,5.065829,1.321138,-9.760381,-8.629158,2.588358,7.018816,-3.074358,-2.118942,-7.345760],[-1.665751,1.486313,9.105275,2.523657,1.226674,3.431508,0.513667,-8.703362,8.051397,5.206998,-5.366570,5.925543,4.733938],[-4.559689,-1.833050,-4.450219,8.232264,5.884477,-5.254589,-6.690150,0.794191,6.339460,7.327265,3.398901,-2.288506,-5.368052],[4.168693,6.307419,4.152873,5.372056,-6.240303,-6.747027,0.417828,-4.057247,-9.845261,5.702718,-7.067893,2.307772,-5.385804],[3.153250,0.740485,-4.216586,0.644059,-6.434377,9.249176,6.720472,1.919237,6.497912,5.303437,-2.148125,-8.166919,1.030044],[9.504091,-0.219212,8.785691,-8.729231,0.026615,-8.248958,-1.119307,8.426201,-9.025666,2.830499,1.967115,-1.501852,0.891706],[-1.689361,-6.583327,-6.050893,-2.611144,7.758166,-5.947771,8.039416,-0.659813,4.032290,-5.531664,-8.431373,7.542791,-4.819929],[-1.282581,3.634559,-4.665268,-1.378496,-5.279100,-2.936435,1.747110,-4.193430,5.349380,-6.348261,6.450010,7.761882,-2.667424],[-1.050633,3.546512,-5.791613,6.071046,6.182204,-2.765213,-9.546153,1.722843,7.969965,1.969670,-9.622506,7.423409,-5.615566],[-4.642668,-5.393364,-9.908870,-3.252155,-0.677606,9.049760,3.736179,2.756740,-8.548055,-4.299809,-4.566299,0.003650,8.912600],[-7.115047,-6.885783,-6.399492,-1.964363,2.397642,8.938148,0.532224,8.568645,-6.447652,8.519822,-9.420166,1.469691,8.032725],[-6.515880,3.758993,6.924908,6.213961,4.729988,-5.323243,-9.665664,-8.640695,-8.498877,9.107154,-9.973118,-7.489426,4.151842]],[[-4.014275,9.988857,-0.017588,-0.276214,1.417285,-9.671763,0.725000,-1.695043,8.582939,6.795004,2.908171,2.324287,5.472374],[-6.198572,-1.086200,-9.693442,-5.300673,-8.285088,-2.876028,0.385644,-5.175955,-3.456790,1.504348,-0.205287,7.641867,-5.988551],[6.197611,-6.376010,4.670605,-5.993005,-3.003821,-8.675175,-4.417344,-2.107756,6.906653,-6.009059,5.593338,1.346237,-5.506713],[7.356622,-0.110417,-1.428464,-5.380628,-5.119520,6.510407,1.829208,-4.542761,-1.476099,-3.306180,6.599830,-3.973065,-3.785808],[-5.190386,-8.276349,9.183985,-2.088091,4.096482,2.808254,7.396682,-7.437509,-6.285855,8.667518,4.458054,7.857956,-4.912446],[-0.407559,-2.828237,-1.543561,-4.479128,6.581828,-0.738715,6.717104,-2.382170,1.298063,3.795841,-0.447129,9.552537,-0.804560],[-2.193762,1.898655,-4.787140,6.270477,-9.916291,4.919432,6.757029,-2.028396,-2.593271,0.764492,-2.162962,0.664761,-4.395436],[1.941703,8.090361,0.516895,6.839836,-8.150775,-2.903606,-6.017734,5.560962,8.115062,5.343256,-6.992620,-8.454895,-0.745974],[3.366429,-4.961524,-5.855513,0.455555,3.893167,7.507099,2.631631,-5.443827,8.261399,-9.306339,-1.690021,4.228783,3.633634],[5.756384,-5.726867,-1.408018,5.733637,2.358622,-5.542451,5.459135,1.864138,-6.624962,-9.173240,-0.153884,-7.842564,-9.220006],[9.323507,-3.716168,-7.625501,-5.543029,1.096927,-8.326718,6.316860,-6.953434,-0.015226,5.374699,-4.966586,8.920079,-5.398716],[3.393164,-4.594750,2.468164,1.417094,9.670466,9.510859,-7.873452,-9.490125,-3.751672,7.758065,-2.691703,-1.687986,7.731290]],[[6.058888,-7.743283,1.742070,-4.971174,9.180812,4.382211,5.491473,-6.202397,-6.512473,-5.223177,2.635095,-6.905394,1.866233],[2.637208,-5.803616,2.903140,4.256701,9.063656,5.468604,-1.935363,4.018917,2.873425,-9.774387,0.833819,9.624649,-7.123499],[-2.349419,8.761586,6.709447,-2.529406,8.581012,1.236527,6.702967,9.613295,2.010297,0.248202,7.760055,8.849470,0.180674],[-3.271593,-2.063254,2.785324,7.734043,0.185049,0.392116,-0.411496,2.769894,4.737928,-3.658359,7.153215,9.655415,-3.055583],[3.564733,-1.448713,3.238374,4.678648,8.855357,-2.463347,3.445930,2.097344,7.267783,-6.863395,-6.588766,3.907125,-8.413888],[-4.033229,-2.357272,7.523224,-2.554601,-5.698125,-8.118642,-3.892808,-2.106946,9.040294,-3.969592,6.374466,-0.244909,-4.558719],[1.899226,-0.662445,-1.552254,0.156641,6.968858,-3.877006,8.186286,7.586095,0.233252,0.123165,7.569214,1.021101,-7.685322],[2.548619,-3.020843,9.964600,-5.205627,-6.313007,-7.956040,9.201620,-5.593154,6.668969,-9.202532,5.013591,-4.254361,0.996433],[3.965726,0.013817,2.892284,5.310784,-2.485311,-1.776683,-3.534772,2.123109,-0.202678,-9.244722,5.552772,-1.882959,3.082813],[8.617744,2.488452,2.854674,6.575284,-9.244498,1.743229,6.283557,-7.360488,-9.210657,-9.410274,5.421634,-8.267817,5.466431],[7.954536,2.646292,2.830193,0.186966,-3.439537,-5.426242,3.176960,-9.895101,-7.721590,1.938522,2.432560,6.795152,6.639446],[8.500408,-9.317501,8.437123,-4.188625,-6.180483,2.822528,-9.307072,-7.454168,-5.778761,4.692269,5.409806,-0.605637,-4.797436]],[[-8.603291,0.520608,-8.803930,-1.489066,5.390514,9.024665,-1.113768,7.945929,4.288919,5.673821,-3.672719,8.249798,1.416962],[4.166085,5.551795,5.234535,4.773208,-1.838938,9.166881,7.642259,-3.808760,1.510948,-3.734022,0.471966,-6.620604,-2.313762],[-5.506559,6.975234,-8.318487,1.275915,-8.936756,4.809107,5.883669,-6.873471,-2.231001,8.518055,-1.520113,-1.727477,9.684089],[-2.039492,-7.301156,8.935575,-6.139880,-5.781901,4.088187,6.722182,0.855402,-9.450740,-0.129682,9.077024,-3.485468,0.548142],[5.151295,8.156871,0.633856,2.849246,-8.589304,-6.989021,2.054539,8.738337,-5.500953,-9.204301,-9.591572,-7.155890,9.153829],[1.845102,-9.183062,-4.781638,-6.562531,3.145361,8.068424,-8.233622,2.097424,6.547052,0.656138,1.598252,7.647304,4.209046],[-5.075638,-3.349525,-0.585709,4.725521,-0.817593,-0.177553,-8.553287,9.396037,-2.767575,2.284035,-3.179708,-7.832636,-2.501867],[-4.551452,-3.657107,9.884522,6.936760,-4.925998,0.802909,2.242698,-6.089559,8.252107,5.834933,-4.454951,-8.079648,1.340274],[-4.419818,-7.272218,9.558430,-6.574316,9.300532,6.004657,4.039219,-3.685801,8.889193,4.778132,3.260498,-2.767411,4.291375],[1.443395,9.488085,-4.660218,-8.636194,-6.065068,8.915267,1.333385,-5.383217,-9.563988,3.282544,-9.076602,-2.607538,-8.094347],[-9.914275,-3.505431,3.967733,9.520694,-0.601278,9.519003,6.523832,-1.952959,-3.178297,9.429767,-6.350555,5.507994,-9.919389],[6.893895,1.577704,-4.852062,-6.492156,8.735911,-3.595788,-8.424064,-0.308101,-1.003166,0.335530,0.032601,-8.226450,-1.247210]],[[-8.688116,-7.525815,-9.475886,6.497091,3.043672,0.908485,-6.775648,-1.903944,-9.574375,0.422732,-3.920872,-8.454456,-2.016456],[1.893290,-3.543258,-2.567997,7.378333,3.184324,-9.156156,9.716188,-2.556799,1.220048,5.948274,-5.858501,7.913529,9.162258],[9.800682,0.066884,0.467598,-5.427816,2.570158,-1.369866,-7.034718,-8.569861,-6.135686,-5.684719,-4.723301,3.721934,9.216480],[0.572389,0.709834,-0.725722,-6.444497,-3.207371,1.503611,8.682883,5.922791,8.664571,1.778413,-7.736102,-9.443717,2.781007],[2.964067,-9.519350,-4.955203,5.502958,-0.154260,-9.010123,4.315771,-6.330493,9.797284,6.749984,0.861758,-1.494436,-4.853915],[-0.069781,-9.812088,-3.215756,-4.890658,-0.913305,-4.914258,-6.530749,-5.941272,-3.997668,-8.341379,-4.615312,-9.154759,-6.903850],[-2.788985,0.781225,-1.620289,1.312410,7.633016,-5.480047,9.879606,-5.943374,-6.398282,-7.233091,7.111294,-7.814664,-2.838474],[1.683794,1.693796,-2.919688,6.814597,-1.925331,-5.629121,-9.529074,5.359391,8.603336,9.907798,8.877878,1.504102,-0.879286],[-4.794671,-9.405364,0.945251,6.608064,3.835123,8.909626,9.863479,-9.602645,5.772390,7.534822,3.225272,0.908154,-5.258164],[-6.229586,5.489679,-1.198203,-4.954445,-8.514809,1.056306,-8.045293,8.779443,4.126370,8.364628,-7.377866,-4.700326,-9.555168],[5.882098,-2.537624,-5.881643,3.619172,-9.909695,2.887889,-8.218296,-5.186804,1.068605,-1.474304,-1.557472,-6.389071,-6.799318],[6.388388,-1.885540,-3.250101,9.244859,-4.983803,-5.285501,0.365851,5.077967,3.995792,-1.372661,1.094452,-7.666510,4.075921]]], dtype = "float64")#candidate|8210|(9, 12, 13)|const|float64
uop_8211 = relay.cos(const_8210.astype('float64')) # shape=(9, 12, 13)
func_2537_call = mod.get_global_var('func_2537')
func_2538_call = mutated_mod.get_global_var('func_2538')
call_8221 = relay.TupleGetItem(func_2537_call(), 1)
call_8222 = relay.TupleGetItem(func_2538_call(), 1)
uop_8224 = relay.asin(uop_8211.astype('float32')) # shape=(9, 12, 13)
func_4736_call = mod.get_global_var('func_4736')
func_4738_call = mutated_mod.get_global_var('func_4738')
var_8229 = relay.var("var_8229", dtype = "float32", shape = (26, 7))#candidate|8229|(26, 7)|var|float32
call_8228 = relay.TupleGetItem(func_4736_call(relay.reshape(var_8229.astype('float32'), [7, 2, 13])), 0)
call_8230 = relay.TupleGetItem(func_4738_call(relay.reshape(var_8229.astype('float32'), [7, 2, 13])), 0)
output = relay.Tuple([call_8221,uop_8224,call_8228,var_8229,])
output2 = relay.Tuple([call_8222,uop_8224,call_8230,var_8229,])
func_8233 = relay.Function([var_8229,], output)
mod['func_8233'] = func_8233
mod = relay.transform.InferType()(mod)
mutated_mod['func_8233'] = func_8233
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8234 = relay.var("var_8234", dtype = "float32", shape = (26, 7))#candidate|8234|(26, 7)|var|float32
func_8233_call = mutated_mod.get_global_var('func_8233')
call_8235 = func_8233_call(var_8234)
output = call_8235
func_8236 = relay.Function([var_8234], output)
mutated_mod['func_8236'] = func_8236
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3463_call = mod.get_global_var('func_3463')
func_3465_call = mutated_mod.get_global_var('func_3465')
call_8243 = relay.TupleGetItem(func_3463_call(), 0)
call_8244 = relay.TupleGetItem(func_3465_call(), 0)
func_7803_call = mod.get_global_var('func_7803')
func_7805_call = mutated_mod.get_global_var('func_7805')
call_8256 = relay.TupleGetItem(func_7803_call(), 0)
call_8257 = relay.TupleGetItem(func_7805_call(), 0)
func_2525_call = mod.get_global_var('func_2525')
func_2526_call = mutated_mod.get_global_var('func_2526')
call_8274 = relay.TupleGetItem(func_2525_call(), 1)
call_8275 = relay.TupleGetItem(func_2526_call(), 1)
func_5363_call = mod.get_global_var('func_5363')
func_5369_call = mutated_mod.get_global_var('func_5369')
var_8279 = relay.var("var_8279", dtype = "float32", shape = (1040,))#candidate|8279|(1040,)|var|float32
const_8280 = relay.const([-6.745897,-4.778231,-9.246410,-1.423520,-8.523689,0.458162,-8.389692,3.920951,-7.189492,-4.262485,-4.335868,4.445157,6.234636,0.201818,-5.473097,1.550057,3.735584,-7.400477,4.977629,-5.337259,-4.610448,-6.263893,-4.180204,-8.837684,-6.841961,5.044170,-0.443457,-5.808708,-9.083160,-7.899209,-1.953049,7.467085,-6.227033,6.342251,-5.595640,9.753079,-1.002625,3.179689,3.856404,5.278057,9.119489,-3.317072,5.032892,7.531965,-7.507781,-6.840326,7.514619,3.591662,-4.548931,-1.649261,-4.773107,6.620665,2.524372,0.859690,7.803981,2.021154,-6.908621,-7.203656,-2.791021,2.869094,1.848011,3.951609,5.097159,-6.209196,-5.367372,0.272039,5.420884,7.183370,7.020140,2.656115,2.395604,0.001198,1.918571,-8.627470,-9.055114,-4.501857,4.890867,-1.869649,-3.030578,-2.465080,1.633104,-3.278780,0.755199,-0.753168,-9.000148,1.980636,-6.689446,8.029480,-0.052481,9.822949,0.056901,-7.117514,7.302766,-4.837015,-1.677584,-4.666403,-1.174900,-1.550324,-5.155591,-6.889533,-0.314442,2.510007,1.800789,-0.661883,-4.163686,-0.782792,-7.197949,-5.358582,5.071611,0.053401,-3.775283,-3.929446,-0.630803,-5.769365,0.003965,-5.707864,-0.163282,-4.689842,-8.531339,5.304759,-4.861913,3.946526,-8.096733,-2.251448,-7.074914,4.138200,-4.520968,8.098577,-0.262132,5.981938,-1.847910,-1.677564,3.444337,-9.095093,7.492907,-9.575257,0.141156,-2.791643,-5.243806,-2.912712,8.425889,8.937140,2.142725,-5.963633,-0.391893,4.978033,1.292947,1.423554,-4.612962,7.091957,1.041373,3.872623,8.660176,-3.308260,-7.997330,-9.829050,5.126343,5.788110,-0.200708,-1.881414,-8.198069,9.732360,1.431137,-7.941424,3.165124,-2.854827,-7.998469,7.508322,9.596085,3.461165,-5.445355,2.880807,0.922739,-5.892273,1.077158,-6.888293,-4.968834,7.670013,-0.716033,9.920587,1.309592,-5.264551,5.979659,3.313719,1.356682,7.201042,-1.203894,5.951981,1.956728,0.890390,0.007448,-3.709051,-3.011997,3.943817,-0.652504,-8.816697,-3.766730,1.904823,-7.692739,1.432860,1.877851,-9.049396,0.233372,3.780364,9.822846,6.877514,-7.529837,8.518173,-4.325016,0.220689,6.988145,-8.348860,-2.031854,-6.612300,3.939580,-8.113733,-6.751374,-7.575301,9.837535,-8.037345,0.045748,7.345023,-7.135238,-5.308922,7.709944,9.441580,9.104842,7.931183,9.568273,-8.418770,4.831457,9.216653,8.174852,1.960477,7.682396,-1.391857,-9.283909,-5.426846,-4.792872,9.683746,-5.064436,-3.970936,-5.152339,4.828024,4.230129,-2.576064,-8.898738,-9.515335,-9.405468,-1.496384,-5.759475,-6.908290,-5.699171,4.773925,6.710336,6.251034,3.308089,3.352362,1.421884,5.108969,-8.115840,6.268877,3.253835,9.088021,2.912328,3.144124,-6.997819,-8.758520,-7.137094,3.717856,-2.248522,8.190025,-5.375590,-7.490450,9.436481,6.284139,7.497241,-9.106889,-1.406218,-4.078287,-2.967835,1.782957,7.580683,3.938494,4.969715,6.104608,5.066878,3.800027,4.234162,0.712002,5.377900,0.599077,2.163731,8.293928,0.875588,-8.203323,7.398398,-2.541891,6.889840,-9.019616,-5.951485,7.238311,-5.843946,4.159377,-7.853150,-7.063292,8.208785,-8.548986,-8.565785,5.764776,-0.417639,8.040347,6.319396,-0.239475,8.229114,-7.085520,7.835706,-1.221729,-7.327056,3.608339,-0.950728,2.181691,0.216838,8.792585,6.427044,8.399182,-0.523581,-2.021603,-2.667621,-1.209544,9.847659,1.320032,-1.366443,7.901488,-3.105778,5.682903,-7.599224,-9.278140,2.851202,6.818577,-0.586651,-9.121344,1.982089,4.968086,1.468063,-7.634745,-1.533554,8.520833,6.174516,3.410073,-6.232406,-6.942334,8.697565,-0.764900,-4.986108,-7.714875,0.935611,8.624829,8.254635,-4.839485,2.944349,5.333199,2.660410,-8.328513,6.499400,-7.449855,7.122226,7.954930,5.492170,4.345793,3.256306,3.518898,-1.944632,-7.377820,6.681273,-2.918239,7.747845,-5.525109,7.002771,6.715851,-4.673238,-9.362696,-5.175667,4.889489,7.150517,-8.170374,-0.565701,3.833525,-8.329176,-7.589010,7.719770,-8.660153,-0.118787,4.895097,-6.167146,0.256451,-5.952500,-6.061717,8.447579,-0.485353,-0.330669,9.927019,-1.324730,5.928120,-0.272754,-0.409109,-5.975592,-1.824786,7.976574,-9.799135,-0.714376,6.749983,0.598845,-7.346585,9.147015,-5.183802,8.173909,-9.547106,-5.970479,-5.261030,6.503884,-7.710643,-5.416021,-8.567753,-9.095876,4.881032,-5.037672,0.460931,-0.848107,-0.291194,0.611517,1.426970,8.869700,-7.349449,2.259923,-4.794494,-9.312525,-4.726320,-8.051190,-6.794732,-5.165285,7.534414,-6.674729,-5.191607,-8.838633,-8.903943,7.203084,-6.533325,5.576885,2.653986,-3.970600,2.179512,-5.157975,5.012374,8.716882,-2.528587,5.322454,-8.752379,-1.166523,-4.805322,-8.387456,-2.272727], dtype = "float32")#candidate|8280|(462,)|const|float32
var_8281 = relay.var("var_8281", dtype = "int64", shape = (3, 90))#candidate|8281|(3, 90)|var|int64
var_8282 = relay.var("var_8282", dtype = "float64", shape = (52,))#candidate|8282|(52,)|var|float64
call_8278 = relay.TupleGetItem(func_5363_call(relay.reshape(var_8279.astype('float32'), [5, 16, 13]), relay.reshape(const_8280.astype('float32'), [462,]), relay.reshape(var_8281.astype('int64'), [270,]), relay.reshape(var_8282.astype('float64'), [52, 1]), ), 3)
call_8283 = relay.TupleGetItem(func_5369_call(relay.reshape(var_8279.astype('float32'), [5, 16, 13]), relay.reshape(const_8280.astype('float32'), [462,]), relay.reshape(var_8281.astype('int64'), [270,]), relay.reshape(var_8282.astype('float64'), [52, 1]), ), 3)
func_6931_call = mod.get_global_var('func_6931')
func_6933_call = mutated_mod.get_global_var('func_6933')
call_8286 = func_6931_call()
call_8287 = func_6931_call()
func_2139_call = mod.get_global_var('func_2139')
func_2141_call = mutated_mod.get_global_var('func_2141')
call_8289 = relay.TupleGetItem(func_2139_call(relay.reshape(call_8274.astype('float64'), [315,])), 3)
call_8290 = relay.TupleGetItem(func_2141_call(relay.reshape(call_8274.astype('float64'), [315,])), 3)
func_7156_call = mod.get_global_var('func_7156')
func_7159_call = mutated_mod.get_global_var('func_7159')
var_8292 = relay.var("var_8292", dtype = "uint8", shape = (120,))#candidate|8292|(120,)|var|uint8
call_8291 = relay.TupleGetItem(func_7156_call(relay.reshape(var_8292.astype('uint8'), [2, 4, 15])), 0)
call_8293 = relay.TupleGetItem(func_7159_call(relay.reshape(var_8292.astype('uint8'), [2, 4, 15])), 0)
func_5737_call = mod.get_global_var('func_5737')
func_5740_call = mutated_mod.get_global_var('func_5740')
const_8310 = relay.const([[1,6,-8,-5,-1,5,-4,-3,2,-1,-6,3,-9,4,-8,9,-6,3,9,8,4,-1,2,1,9,-8,4,3,-6,7,9,3,10,1,4,1,-1,-8,6,9,-3,2,-6,1,6,-8,-5,-4,9,-6,5,4,-8,2,-2,-1,8,2,-10,8,2,-1,-8,-4,10,-3,7,-4,-8,1,7,-6,-7,9,-3,1,4,4],[9,-1,8,-6,9,-10,-6,8,-4,8,-3,7,3,-3,4,-9,7,-1,-3,-2,7,-1,4,8,-4,-9,3,-2,8,3,5,2,-1,-9,-10,-9,4,1,1,-5,-4,-1,2,3,-9,1,-8,9,8,6,-10,4,-6,1,-4,2,1,-5,7,7,6,-1,3,-6,8,8,6,2,-8,-1,7,10,-7,5,5,-9,9,5],[-9,-10,2,7,-1,2,-9,-10,6,-8,-5,6,-6,2,6,7,10,-4,-7,-10,9,-6,3,-9,-5,2,2,1,5,-1,-1,-8,-6,-1,3,-9,-3,3,2,7,-8,9,-8,-6,-2,-6,7,-3,-6,6,-8,-4,-4,1,8,5,-8,8,5,-3,-2,1,10,-4,10,6,9,-3,6,8,3,-3,-8,-8,-4,-1,9,8],[7,8,4,-7,3,-5,-3,6,-6,8,-10,10,-9,-2,4,10,2,9,3,8,-8,-6,5,9,-10,9,5,-4,10,-3,-6,6,-2,-5,-2,10,5,1,9,-3,-8,1,-2,6,-2,8,5,-7,8,-1,-4,-10,-8,-1,2,-9,8,2,6,-4,10,-8,6,1,9,6,-4,4,-9,2,-9,-2,1,-7,-3,-9,2,5],[3,6,9,-5,10,6,4,-9,-8,-8,-4,-8,-5,-9,4,-9,-1,1,8,-4,7,6,-7,-2,5,-6,6,-7,2,-10,-9,7,5,-1,-6,-9,-4,-4,-1,9,-8,-6,-10,-7,-8,-1,9,8,-8,5,3,-8,-1,9,-1,-8,3,5,-7,-8,-1,-4,8,4,-1,1,5,3,2,-9,-10,3,-3,7,-1,6,3,-4]], dtype = "int32")#candidate|8310|(5, 78)|const|int32
call_8309 = relay.TupleGetItem(func_5737_call(relay.reshape(const_8310.astype('int32'), [6, 5, 13])), 0)
call_8311 = relay.TupleGetItem(func_5740_call(relay.reshape(const_8310.astype('int32'), [6, 5, 13])), 0)
output = relay.Tuple([call_8243,call_8256,call_8274,call_8278,var_8279,const_8280,var_8281,var_8282,call_8286,call_8289,call_8291,var_8292,call_8309,const_8310,])
output2 = relay.Tuple([call_8244,call_8257,call_8275,call_8283,var_8279,const_8280,var_8281,var_8282,call_8287,call_8290,call_8293,var_8292,call_8311,const_8310,])
func_8317 = relay.Function([var_8279,var_8281,var_8282,var_8292,], output)
mod['func_8317'] = func_8317
mod = relay.transform.InferType()(mod)
mutated_mod['func_8317'] = func_8317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8317_call = mutated_mod.get_global_var('func_8317')
var_8319 = relay.var("var_8319", dtype = "float32", shape = (1040,))#candidate|8319|(1040,)|var|float32
var_8320 = relay.var("var_8320", dtype = "int64", shape = (3, 90))#candidate|8320|(3, 90)|var|int64
var_8321 = relay.var("var_8321", dtype = "float64", shape = (52,))#candidate|8321|(52,)|var|float64
var_8322 = relay.var("var_8322", dtype = "uint8", shape = (120,))#candidate|8322|(120,)|var|uint8
call_8318 = func_8317_call(var_8319,var_8320,var_8321,var_8322,)
output = call_8318
func_8323 = relay.Function([var_8319,var_8320,var_8321,var_8322,], output)
mutated_mod['func_8323'] = func_8323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8172_call = mod.get_global_var('func_8172')
func_8173_call = mutated_mod.get_global_var('func_8173')
call_8329 = relay.TupleGetItem(func_8172_call(), 0)
call_8330 = relay.TupleGetItem(func_8173_call(), 0)
output = relay.Tuple([call_8329,])
output2 = relay.Tuple([call_8330,])
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
var_8379 = relay.var("var_8379", dtype = "float64", shape = (13, 13, 14))#candidate|8379|(13, 13, 14)|var|float64
uop_8380 = relay.log(var_8379.astype('float64')) # shape=(13, 13, 14)
output = relay.Tuple([uop_8380,])
output2 = relay.Tuple([uop_8380,])
func_8382 = relay.Function([var_8379,], output)
mod['func_8382'] = func_8382
mod = relay.transform.InferType()(mod)
var_8383 = relay.var("var_8383", dtype = "float64", shape = (13, 13, 14))#candidate|8383|(13, 13, 14)|var|float64
output = func_8382(var_8383)
func_8384 = relay.Function([var_8383], output)
mutated_mod['func_8384'] = func_8384
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2257_call = mod.get_global_var('func_2257')
func_2258_call = mutated_mod.get_global_var('func_2258')
call_8389 = relay.TupleGetItem(func_2257_call(), 0)
call_8390 = relay.TupleGetItem(func_2258_call(), 0)
func_2022_call = mod.get_global_var('func_2022')
func_2028_call = mutated_mod.get_global_var('func_2028')
var_8406 = relay.var("var_8406", dtype = "uint64", shape = ())#candidate|8406|()|var|uint64
var_8407 = relay.var("var_8407", dtype = "uint64", shape = (130,))#candidate|8407|(130,)|var|uint64
var_8408 = relay.var("var_8408", dtype = "float32", shape = (26, 2))#candidate|8408|(26, 2)|var|float32
const_8409 = relay.const([[-4,2,7,10,10,-4,6,3,7,2,10,9,-7,1,-10,-5,-7,-10,2,6,3,-3,9,-8,9,-10,-9,9,8,9,8,6,1,-2,6,-5,7,10,3,-2]], dtype = "uint8")#candidate|8409|(1, 40)|const|uint8
call_8405 = relay.TupleGetItem(func_2022_call(relay.reshape(var_8406.astype('uint64'), []), relay.reshape(var_8407.astype('uint64'), [13, 5, 2]), relay.reshape(var_8408.astype('float32'), [2, 2, 13]), relay.reshape(const_8409.astype('uint8'), [40,]), ), 7)
call_8410 = relay.TupleGetItem(func_2028_call(relay.reshape(var_8406.astype('uint64'), []), relay.reshape(var_8407.astype('uint64'), [13, 5, 2]), relay.reshape(var_8408.astype('float32'), [2, 2, 13]), relay.reshape(const_8409.astype('uint8'), [40,]), ), 7)
func_2022_call = mod.get_global_var('func_2022')
func_2028_call = mutated_mod.get_global_var('func_2028')
call_8411 = relay.TupleGetItem(func_2022_call(relay.reshape(var_8406.astype('uint64'), []), relay.reshape(var_8407.astype('uint64'), [13, 5, 2]), relay.reshape(var_8408.astype('float32'), [2, 2, 13]), relay.reshape(const_8409.astype('uint8'), [40,]), ), 2)
call_8412 = relay.TupleGetItem(func_2028_call(relay.reshape(var_8406.astype('uint64'), []), relay.reshape(var_8407.astype('uint64'), [13, 5, 2]), relay.reshape(var_8408.astype('float32'), [2, 2, 13]), relay.reshape(const_8409.astype('uint8'), [40,]), ), 2)
output = relay.Tuple([call_8389,call_8405,var_8406,var_8407,var_8408,const_8409,call_8411,])
output2 = relay.Tuple([call_8390,call_8410,var_8406,var_8407,var_8408,const_8409,call_8412,])
func_8414 = relay.Function([var_8406,var_8407,var_8408,], output)
mod['func_8414'] = func_8414
mod = relay.transform.InferType()(mod)
var_8415 = relay.var("var_8415", dtype = "uint64", shape = ())#candidate|8415|()|var|uint64
var_8416 = relay.var("var_8416", dtype = "uint64", shape = (130,))#candidate|8416|(130,)|var|uint64
var_8417 = relay.var("var_8417", dtype = "float32", shape = (26, 2))#candidate|8417|(26, 2)|var|float32
output = func_8414(var_8415,var_8416,var_8417,)
func_8418 = relay.Function([var_8415,var_8416,var_8417,], output)
mutated_mod['func_8418'] = func_8418
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4537_call = mod.get_global_var('func_4537')
func_4539_call = mutated_mod.get_global_var('func_4539')
call_8469 = relay.TupleGetItem(func_4537_call(), 0)
call_8470 = relay.TupleGetItem(func_4539_call(), 0)
func_8317_call = mod.get_global_var('func_8317')
func_8323_call = mutated_mod.get_global_var('func_8323')
var_8489 = relay.var("var_8489", dtype = "float32", shape = (1040, 1))#candidate|8489|(1040, 1)|var|float32
var_8490 = relay.var("var_8490", dtype = "int64", shape = (3, 90))#candidate|8490|(3, 90)|var|int64
const_8491 = relay.const([5.533268,-8.797068,-8.811360,-9.523576,-3.291192,-0.045958,8.916430,-4.549879,1.008207,4.287297,-6.881678,-4.095491,4.698174,-2.487770,-7.018249,-6.415385,7.175294,1.255692,1.333744,-6.649255,3.366012,7.690765,1.744113,-4.684040,8.994841,-8.074012,1.133490,-4.358870,5.391537,4.774661,3.250937,8.609286,1.843728,-3.631371,1.612734,-7.627060,-1.005752,0.956747,2.564990,-8.697867,-2.613876,-0.921017,2.671520,-3.387728,3.907835,3.071811,4.138366,5.326584,1.691241,0.007377,-2.285952,4.584412], dtype = "float64")#candidate|8491|(52,)|const|float64
var_8492 = relay.var("var_8492", dtype = "uint8", shape = (120,))#candidate|8492|(120,)|var|uint8
call_8488 = relay.TupleGetItem(func_8317_call(relay.reshape(var_8489.astype('float32'), [1040,]), relay.reshape(var_8490.astype('int64'), [3, 90]), relay.reshape(const_8491.astype('float64'), [52,]), relay.reshape(var_8492.astype('uint8'), [120,]), ), 9)
call_8493 = relay.TupleGetItem(func_8323_call(relay.reshape(var_8489.astype('float32'), [1040,]), relay.reshape(var_8490.astype('int64'), [3, 90]), relay.reshape(const_8491.astype('float64'), [52,]), relay.reshape(var_8492.astype('uint8'), [120,]), ), 9)
func_4311_call = mod.get_global_var('func_4311')
func_4312_call = mutated_mod.get_global_var('func_4312')
call_8503 = relay.TupleGetItem(func_4311_call(), 0)
call_8504 = relay.TupleGetItem(func_4312_call(), 0)
output = relay.Tuple([call_8469,call_8488,var_8489,var_8490,const_8491,var_8492,call_8503,])
output2 = relay.Tuple([call_8470,call_8493,var_8489,var_8490,const_8491,var_8492,call_8504,])
func_8512 = relay.Function([var_8489,var_8490,var_8492,], output)
mod['func_8512'] = func_8512
mod = relay.transform.InferType()(mod)
var_8513 = relay.var("var_8513", dtype = "float32", shape = (1040, 1))#candidate|8513|(1040, 1)|var|float32
var_8514 = relay.var("var_8514", dtype = "int64", shape = (3, 90))#candidate|8514|(3, 90)|var|int64
var_8515 = relay.var("var_8515", dtype = "uint8", shape = (120,))#candidate|8515|(120,)|var|uint8
output = func_8512(var_8513,var_8514,var_8515,)
func_8516 = relay.Function([var_8513,var_8514,var_8515,], output)
mutated_mod['func_8516'] = func_8516
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8536 = relay.var("var_8536", dtype = "uint16", shape = (15, 11, 2))#candidate|8536|(15, 11, 2)|var|uint16
var_8537 = relay.var("var_8537", dtype = "uint16", shape = (15, 11, 2))#candidate|8537|(15, 11, 2)|var|uint16
bop_8538 = relay.right_shift(var_8536.astype('uint16'), relay.reshape(var_8537.astype('uint16'), relay.shape_of(var_8536))) # shape=(15, 11, 2)
func_4074_call = mod.get_global_var('func_4074')
func_4077_call = mutated_mod.get_global_var('func_4077')
const_8547 = relay.const([-8.451820,3.440702,7.808725,3.933774,5.137529,6.194102,-9.181147,-9.650152,1.946936,0.610416,-5.776290,0.952566,4.003707,8.039838,-1.087835,-6.776361,9.686556,-8.350768,7.421708,-8.270292,-7.513278,-0.342059,-7.992601,3.418551,-0.711585,-6.586374,-7.090522,4.694895,-2.317335,-9.991513,-0.791762,6.548708,-0.087409,-9.914345,-3.052339,-2.636875,-0.959533,2.894147,5.009611,-1.584107,1.109160,-3.893802,2.360739,-2.757552,-8.890330,-3.668098,1.781421,8.057822,-6.181022,5.083310,-5.973788,6.937721,9.750976,6.942748,0.852910,-6.819199,9.206244,-3.798320,7.908424,-6.582275,3.560447,-2.229704,9.237781,-8.192953,5.057728,-7.245095,1.280123,8.692263,-4.095166,1.389596,-6.816006,9.108850,-0.059476,-9.745614,-9.193377,-2.159935,-5.510903,-8.783124,-4.271334,8.083682,-9.739038,4.103664,1.314989,-6.584525,-9.104326,8.160791,-9.569863,-4.834464,-9.479352,-5.242941,9.655811,-9.015346,5.626198,9.864827,0.296368,0.811079,-0.359846,7.920831,7.324636,-0.846952,8.077663,9.729736,-2.825006,-1.618425,-1.387727], dtype = "float32")#candidate|8547|(105,)|const|float32
call_8546 = relay.TupleGetItem(func_4074_call(relay.reshape(const_8547.astype('float32'), [105, 1]), relay.reshape(const_8547.astype('float32'), [105, 1]), ), 2)
call_8548 = relay.TupleGetItem(func_4077_call(relay.reshape(const_8547.astype('float32'), [105, 1]), relay.reshape(const_8547.astype('float32'), [105, 1]), ), 2)
output = relay.Tuple([bop_8538,call_8546,const_8547,])
output2 = relay.Tuple([bop_8538,call_8548,const_8547,])
func_8549 = relay.Function([var_8536,var_8537,], output)
mod['func_8549'] = func_8549
mod = relay.transform.InferType()(mod)
mutated_mod['func_8549'] = func_8549
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8549_call = mutated_mod.get_global_var('func_8549')
var_8551 = relay.var("var_8551", dtype = "uint16", shape = (15, 11, 2))#candidate|8551|(15, 11, 2)|var|uint16
var_8552 = relay.var("var_8552", dtype = "uint16", shape = (15, 11, 2))#candidate|8552|(15, 11, 2)|var|uint16
call_8550 = func_8549_call(var_8551,var_8552,)
output = call_8550
func_8553 = relay.Function([var_8551,var_8552,], output)
mutated_mod['func_8553'] = func_8553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3097_call = mod.get_global_var('func_3097')
func_3099_call = mutated_mod.get_global_var('func_3099')
call_8633 = func_3097_call()
call_8634 = func_3097_call()
output = call_8633
output2 = call_8634
func_8639 = relay.Function([], output)
mod['func_8639'] = func_8639
mod = relay.transform.InferType()(mod)
output = func_8639()
func_8640 = relay.Function([], output)
mutated_mod['func_8640'] = func_8640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5381_call = mod.get_global_var('func_5381')
func_5382_call = mutated_mod.get_global_var('func_5382')
call_8641 = func_5381_call()
call_8642 = func_5381_call()
func_2525_call = mod.get_global_var('func_2525')
func_2526_call = mutated_mod.get_global_var('func_2526')
call_8668 = relay.TupleGetItem(func_2525_call(), 1)
call_8669 = relay.TupleGetItem(func_2526_call(), 1)
output = relay.Tuple([call_8641,call_8668,])
output2 = relay.Tuple([call_8642,call_8669,])
func_8677 = relay.Function([], output)
mod['func_8677'] = func_8677
mod = relay.transform.InferType()(mod)
mutated_mod['func_8677'] = func_8677
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8677_call = mutated_mod.get_global_var('func_8677')
call_8678 = func_8677_call()
output = call_8678
func_8679 = relay.Function([], output)
mutated_mod['func_8679'] = func_8679
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4471_call = mod.get_global_var('func_4471')
func_4473_call = mutated_mod.get_global_var('func_4473')
call_8680 = relay.TupleGetItem(func_4471_call(), 1)
call_8681 = relay.TupleGetItem(func_4473_call(), 1)
output = relay.Tuple([call_8680,])
output2 = relay.Tuple([call_8681,])
func_8690 = relay.Function([], output)
mod['func_8690'] = func_8690
mod = relay.transform.InferType()(mod)
mutated_mod['func_8690'] = func_8690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8690_call = mutated_mod.get_global_var('func_8690')
call_8691 = func_8690_call()
output = call_8691
func_8692 = relay.Function([], output)
mutated_mod['func_8692'] = func_8692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7919_call = mod.get_global_var('func_7919')
func_7920_call = mutated_mod.get_global_var('func_7920')
call_8707 = relay.TupleGetItem(func_7919_call(), 0)
call_8708 = relay.TupleGetItem(func_7920_call(), 0)
func_5760_call = mod.get_global_var('func_5760')
func_5762_call = mutated_mod.get_global_var('func_5762')
call_8723 = relay.TupleGetItem(func_5760_call(), 0)
call_8724 = relay.TupleGetItem(func_5762_call(), 0)
output = relay.Tuple([call_8707,call_8723,])
output2 = relay.Tuple([call_8708,call_8724,])
func_8737 = relay.Function([], output)
mod['func_8737'] = func_8737
mod = relay.transform.InferType()(mod)
output = func_8737()
func_8738 = relay.Function([], output)
mutated_mod['func_8738'] = func_8738
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4413_call = mod.get_global_var('func_4413')
func_4415_call = mutated_mod.get_global_var('func_4415')
call_8813 = relay.TupleGetItem(func_4413_call(), 0)
call_8814 = relay.TupleGetItem(func_4415_call(), 0)
func_5966_call = mod.get_global_var('func_5966')
func_5969_call = mutated_mod.get_global_var('func_5969')
var_8823 = relay.var("var_8823", dtype = "int32", shape = (390, 1))#candidate|8823|(390, 1)|var|int32
call_8822 = relay.TupleGetItem(func_5966_call(relay.reshape(var_8823.astype('int32'), [390,])), 1)
call_8824 = relay.TupleGetItem(func_5969_call(relay.reshape(var_8823.astype('int32'), [390,])), 1)
func_6245_call = mod.get_global_var('func_6245')
func_6247_call = mutated_mod.get_global_var('func_6247')
call_8839 = relay.TupleGetItem(func_6245_call(), 1)
call_8840 = relay.TupleGetItem(func_6247_call(), 1)
var_8850 = relay.var("var_8850", dtype = "bool", shape = (3, 14, 4))#candidate|8850|(3, 14, 4)|var|bool
bop_8851 = relay.minimum(call_8813.astype('uint64'), relay.reshape(var_8850.astype('uint64'), relay.shape_of(call_8813))) # shape=(3, 14, 4)
bop_8854 = relay.minimum(call_8814.astype('uint64'), relay.reshape(var_8850.astype('uint64'), relay.shape_of(call_8814))) # shape=(3, 14, 4)
output = relay.Tuple([call_8822,var_8823,call_8839,bop_8851,])
output2 = relay.Tuple([call_8824,var_8823,call_8840,bop_8854,])
func_8859 = relay.Function([var_8823,var_8850,], output)
mod['func_8859'] = func_8859
mod = relay.transform.InferType()(mod)
mutated_mod['func_8859'] = func_8859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8859_call = mutated_mod.get_global_var('func_8859')
var_8861 = relay.var("var_8861", dtype = "int32", shape = (390, 1))#candidate|8861|(390, 1)|var|int32
var_8862 = relay.var("var_8862", dtype = "bool", shape = (3, 14, 4))#candidate|8862|(3, 14, 4)|var|bool
call_8860 = func_8859_call(var_8861,var_8862,)
output = call_8860
func_8863 = relay.Function([var_8861,var_8862,], output)
mutated_mod['func_8863'] = func_8863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2257_call = mod.get_global_var('func_2257')
func_2258_call = mutated_mod.get_global_var('func_2258')
call_8885 = relay.TupleGetItem(func_2257_call(), 0)
call_8886 = relay.TupleGetItem(func_2258_call(), 0)
output = relay.Tuple([call_8885,])
output2 = relay.Tuple([call_8886,])
func_8907 = relay.Function([], output)
mod['func_8907'] = func_8907
mod = relay.transform.InferType()(mod)
mutated_mod['func_8907'] = func_8907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8907_call = mutated_mod.get_global_var('func_8907')
call_8908 = func_8907_call()
output = call_8908
func_8909 = relay.Function([], output)
mutated_mod['func_8909'] = func_8909
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8639_call = mod.get_global_var('func_8639')
func_8640_call = mutated_mod.get_global_var('func_8640')
call_8925 = func_8639_call()
call_8926 = func_8639_call()
output = relay.Tuple([call_8925,])
output2 = relay.Tuple([call_8926,])
func_8930 = relay.Function([], output)
mod['func_8930'] = func_8930
mod = relay.transform.InferType()(mod)
mutated_mod['func_8930'] = func_8930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8930_call = mutated_mod.get_global_var('func_8930')
call_8931 = func_8930_call()
output = call_8931
func_8932 = relay.Function([], output)
mutated_mod['func_8932'] = func_8932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6909_call = mod.get_global_var('func_6909')
func_6910_call = mutated_mod.get_global_var('func_6910')
call_8980 = func_6909_call()
call_8981 = func_6909_call()
output = call_8980
output2 = call_8981
func_8985 = relay.Function([], output)
mod['func_8985'] = func_8985
mod = relay.transform.InferType()(mod)
output = func_8985()
func_8986 = relay.Function([], output)
mutated_mod['func_8986'] = func_8986
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9021 = relay.const([[[8.961056,-0.007978,2.782675,-6.404963,-8.562117,7.621921,1.775891,5.819126,0.377170,9.211982,4.157094,4.094374,-7.284899,-9.665705,-2.663916],[7.204214,3.479923,1.540019,4.825062,-6.630598,-3.730610,0.752778,9.065622,4.334563,-1.917775,-8.756257,-4.555508,6.653015,5.367054,-3.584877],[6.630591,6.198978,-1.268948,-4.003786,-9.076888,2.620356,-4.335318,-5.183847,0.112971,-6.063875,-5.703400,1.820641,-9.909706,-3.187899,2.417647],[0.636622,-8.991456,6.118078,-9.796771,-7.762174,-2.798898,6.070825,2.615294,5.601757,6.346554,-3.596030,-9.158868,6.770241,-0.739710,-2.323535],[-7.641707,0.484736,-1.121209,4.189247,-5.043653,3.862807,8.364754,8.358921,-0.740414,-3.447900,-0.808381,3.665857,-3.926207,4.925108,-7.638613],[-8.307867,-1.620850,4.111705,5.127809,9.206739,7.408040,-6.006881,3.078457,9.277558,-1.902947,3.743956,-2.141982,9.475041,3.152407,-3.384946],[-6.145954,3.128892,-7.083514,5.598084,8.483690,7.709096,1.265580,-0.103956,1.204095,-1.492724,5.225443,-1.582311,3.906271,-2.789931,-3.474097],[-6.599546,-1.783968,7.980532,6.206821,-1.563562,4.240732,6.128947,5.194437,4.230277,7.572238,2.170764,-9.326531,-8.989027,3.914299,-8.987172]],[[1.227301,6.018786,-3.859816,-0.276347,8.254210,8.638458,-1.381135,-9.178590,-3.717701,-3.180337,4.000510,-4.087942,9.766853,4.382849,6.373884],[2.605700,1.779703,-2.489746,7.151603,8.266379,5.319595,-3.086657,1.877973,-4.014990,-1.106820,4.198819,-3.728527,6.982507,-2.031702,-2.419787],[8.671213,1.248158,-3.086595,-5.013592,-8.029513,2.934168,-1.291484,-3.418092,-2.283080,3.997899,4.047130,-8.995307,-5.873490,-4.368035,7.403977],[0.463910,-4.020167,6.890744,-5.592535,-6.027449,5.959272,4.833236,8.037393,3.760357,-3.977869,1.084199,5.991346,5.052250,8.006591,-2.352442],[-8.999332,1.943607,-8.918385,-1.830574,4.929904,-8.522791,-3.629942,-1.516031,0.079566,2.829935,3.186386,9.959696,-1.661689,-8.554040,-3.236120],[-8.050689,-1.473305,1.661674,-3.493766,-4.921649,7.060248,-9.180485,-4.686481,0.556081,-7.812100,5.270954,4.399368,-7.891044,5.564466,-3.682729],[-0.776753,-5.099625,-4.028936,3.961393,6.376824,-4.917348,-8.341254,-0.639150,-5.128304,-8.090502,-9.869138,-8.698725,5.295736,-0.062935,3.308836],[-7.779450,9.452670,1.887899,2.906742,9.206587,-7.854674,4.061914,-4.074972,0.748431,9.809059,-2.832705,2.134990,-6.379811,7.462586,8.074110]],[[1.298502,-8.869988,-1.891978,-2.271144,9.678866,4.953667,-8.959841,-3.326637,-6.406672,8.491915,-2.037549,-9.435505,-7.394934,-7.667096,7.073785],[-5.821724,1.977205,7.664906,-9.312491,3.977685,1.333507,3.752027,6.477162,2.920408,3.442495,-1.073271,-0.675262,8.014649,8.280675,-8.634930],[2.792757,2.400341,-9.434557,3.458634,-6.128056,-8.028274,4.329072,8.571381,1.161301,-5.730521,3.542824,-4.893736,3.368545,-1.283717,7.436568],[4.881329,-5.758990,-9.764044,-6.295514,0.991139,-9.957703,-5.069127,-7.563171,2.999744,-6.921748,-0.878549,-8.509290,2.676623,3.611273,-4.572938],[7.715453,1.734222,-1.442657,-4.570656,6.692615,6.578476,3.432644,1.684358,-5.220136,6.039464,7.750911,-6.189310,6.368280,8.811031,-9.705135],[3.288894,-0.301256,4.911024,-8.026739,0.795951,3.365544,-2.044605,-2.832136,-8.597148,-6.996088,-8.799974,-7.246620,8.036446,-6.670743,-4.506065],[-1.205352,-9.827162,-9.195569,8.514915,7.577702,7.339874,6.557948,6.636203,3.503133,-3.787817,-6.794688,3.916207,-6.965755,-4.883940,-4.058862],[0.352509,-8.613940,5.023231,7.971318,-7.723984,1.859298,5.417077,9.226792,-6.155809,9.046011,-9.298807,6.141251,-7.231185,-5.414900,1.768536]],[[5.542513,3.576782,-0.227881,-5.017186,9.053311,8.468777,-0.919265,1.796300,6.015213,7.493762,4.488131,-9.358261,3.335673,-4.924961,1.193495],[-5.782200,-6.306649,8.567913,-9.603291,-9.926656,-5.071577,-5.631235,-8.838018,-8.797107,-1.395163,-2.996710,7.765616,-6.380748,5.296673,-7.124727],[-1.856073,4.638685,-2.108564,-2.421848,7.067656,-4.309032,-1.263832,-8.731009,-9.970845,-6.318745,-9.763343,-0.444251,-3.585803,0.234609,6.311578],[-6.383269,-3.229315,-4.812797,-1.725532,-3.706862,2.387842,9.993689,2.418222,0.795114,-8.221465,-0.027562,-7.239233,-9.163267,-2.576005,0.727661],[0.678323,6.032891,8.860359,-6.540884,-7.330459,6.414148,6.384764,8.732452,2.111221,3.658898,1.463109,-8.721026,-0.972765,-9.604565,-7.496010],[2.423364,8.546975,-5.069887,-3.913490,0.620343,6.265573,7.174931,9.126281,5.283792,6.885304,4.475851,0.660271,-2.360429,-1.314163,-2.526713],[-7.457887,7.159183,-3.965957,5.140925,-0.821739,-2.004768,2.029127,7.321042,-4.259769,6.148974,6.561802,-7.165676,8.593148,-7.536963,3.040170],[-8.954793,-3.635641,-1.128333,7.474403,-8.971235,-0.505126,6.023575,-2.022257,-3.870022,-4.074510,-4.461636,-2.247412,-0.929165,9.570433,-1.573161]],[[3.493331,9.850971,-5.933539,-8.883028,6.924496,5.147277,5.903282,9.739215,8.012073,8.759125,-1.827024,6.958290,-8.219231,-8.740987,0.374931],[4.267415,1.430061,-3.731415,-7.568951,-1.460381,0.146577,9.648958,-5.788189,-0.635206,-3.747550,4.694452,2.294957,-2.472268,-5.769881,-2.234238],[5.724129,-2.926976,-2.817553,-6.224910,-6.296099,-0.982167,-9.619464,-2.698630,-3.822844,3.792163,-2.087910,8.938960,7.373563,-0.399723,-9.814812],[8.506341,-7.422391,0.127203,4.909697,5.966151,-9.689256,9.294237,6.790917,7.428007,3.972002,-4.718886,-9.425733,8.458273,0.311287,3.914215],[-4.698722,6.325267,3.893124,2.120189,-1.272133,-3.820265,-2.161640,-3.445259,0.505743,-2.966708,-2.833947,9.204643,-2.753165,-7.053819,-0.576438],[-0.703085,3.569066,4.364953,-4.294917,6.584971,9.363126,0.481206,8.960482,5.009554,5.926554,9.420485,-7.247778,-5.673581,-4.992093,0.245487],[6.947519,6.197439,1.127947,8.296699,-1.925728,6.858155,-8.688763,0.931358,-6.360564,-4.957391,-1.539050,5.063513,-7.633758,-0.914587,-3.668397],[1.586294,7.655397,-5.149776,7.198230,-3.481346,-6.454595,4.207259,-5.386075,7.758537,6.184937,-8.442118,4.020374,6.060173,-1.298944,-3.595598]],[[6.842006,-0.805567,7.261202,4.682095,-4.950303,-8.983711,9.375779,9.521122,-6.401960,-3.805067,-8.902479,-5.657257,-8.740849,-7.164877,6.029015],[-8.461461,-9.556053,2.260173,7.698655,5.648718,-1.989145,3.155804,0.791434,0.385571,8.411350,-2.821841,-8.277704,3.243486,-5.798268,1.671589],[8.110255,-9.746949,-1.974656,3.937583,-5.836110,8.693328,-5.735175,0.012222,7.761303,8.062683,-5.311688,8.683684,-9.712019,-3.646147,-1.030597],[-9.285038,6.197386,6.594157,-5.748034,8.437539,6.463534,3.318217,6.041413,-4.380052,9.774910,1.510447,7.706608,5.380898,-0.832420,-7.010532],[1.247482,-7.649773,8.071834,0.539927,-0.124681,-4.684395,7.274615,0.401899,-5.398346,-9.212147,4.834437,-5.496242,-4.077361,8.305074,4.463873],[5.958407,-3.582243,7.219972,0.134571,-1.426948,5.051837,-2.673595,-8.135976,-6.910598,8.721630,0.984947,-5.752050,2.025405,5.279410,3.209930],[-7.023775,9.093438,-6.770068,-9.286546,9.461686,8.910018,8.626697,-0.093737,4.496062,9.198623,3.590895,-0.532154,-4.874814,-4.304647,-0.898449],[-3.267717,-2.330023,1.173226,-0.162807,-8.113219,-0.877950,-7.290584,4.152731,-6.111245,7.906738,4.688081,-9.929463,2.898134,6.704760,-0.357476]],[[2.516544,-0.050755,-2.537570,7.361205,5.506401,0.323872,7.297256,-1.328401,-5.049481,-6.122580,-3.751580,-9.162106,1.118129,8.292042,0.452252],[-7.845494,-9.035063,-4.502523,-4.452130,0.437666,8.851724,-3.287992,-3.489079,-2.317481,5.937848,0.688266,-1.763568,-1.355623,4.998900,8.305612],[8.309252,7.251607,-9.959666,-2.728407,6.669251,5.456439,-7.830194,-7.603236,-7.644806,1.146911,5.376828,7.278868,-0.412353,6.901808,5.963499],[-1.892511,-4.441422,-8.199556,2.119490,6.793399,-1.073071,-2.115251,-1.886538,9.824236,5.033627,-8.382524,5.484290,-3.131187,8.163692,0.446102],[-3.058107,6.853727,-9.374921,-4.937885,2.076566,-8.445858,-9.519144,-5.884846,6.541865,7.236972,2.744895,9.531835,0.759137,-8.824609,0.777711],[2.081269,-3.583804,-2.025909,-6.998362,-2.266883,6.254498,1.935537,5.213475,-9.594455,5.756876,1.697008,-9.215964,-1.587703,3.969057,-7.921460],[-9.745819,-9.596856,1.871453,2.122532,3.490358,1.940442,4.133801,-0.937222,-0.406686,6.223509,-5.681546,-5.483283,-0.861702,-5.521112,-2.919137],[-0.369940,-0.668290,1.474695,-3.591453,6.645225,-0.209393,-7.469688,3.253305,3.107429,2.923870,-1.812023,6.161736,-0.186758,5.627382,6.907755]],[[-6.032761,-9.195765,6.899162,-6.273891,1.175187,3.329090,-9.681990,7.364878,8.791192,4.687190,2.644421,-6.344392,8.659129,-1.637072,-9.588531],[-6.669648,-4.820247,9.886825,-6.902761,8.728343,-1.605792,1.362477,-2.482171,-4.113215,1.101622,-1.229859,6.673490,-6.346284,-4.863764,5.823848],[-7.888640,0.456317,1.286310,-9.565099,-0.635266,3.777066,4.701230,0.291618,4.905726,5.733315,5.802376,8.114540,-0.298905,6.129070,0.693129],[4.841409,-7.783745,-2.319852,-7.235445,5.908226,-5.710923,6.325100,-9.846361,2.505376,-7.293232,-9.483589,-8.441908,3.115516,7.684039,7.708406],[5.103410,3.882036,9.997170,0.531646,-8.225868,-7.164898,9.761207,-4.590028,-1.283585,9.145640,-2.974099,5.833093,-6.051766,-7.536094,8.007608],[-1.127299,-5.519792,4.548010,7.204398,0.588363,7.821017,-5.532926,6.180409,-3.489972,-4.186143,3.307832,-4.234707,8.066849,3.332974,-7.721404],[-2.705859,5.547586,-7.772944,-9.300558,-1.652712,-3.792895,-0.506296,-7.358093,2.468942,4.462699,4.273931,6.431070,5.954254,-9.903918,-6.956747],[-7.223135,5.252110,6.548201,-1.993966,2.844856,-5.653158,-7.798970,-2.972597,-4.502908,-5.980157,5.390425,-1.960889,3.710566,5.572152,-1.015625]],[[-9.744120,-2.261163,3.825249,-2.814545,-6.814908,-5.956414,0.346678,5.550785,7.148275,1.021472,6.597377,1.125066,8.843955,-7.495886,-3.591822],[-7.863927,5.549640,-8.878640,6.513832,-2.287528,-3.698637,-3.227547,1.076515,9.444807,5.135747,-6.470314,2.318654,0.355599,-7.283205,-5.011105],[-9.414380,-5.372145,8.847901,-6.657115,4.026133,-2.839087,4.763204,0.119055,-9.175741,-6.924416,0.867448,9.251095,-6.764638,-9.934938,-2.137969],[-0.656482,6.612444,-2.399391,4.101401,0.448018,3.074759,9.980138,-0.350857,2.684962,5.398025,9.305128,8.783655,-0.750394,8.298633,-2.197053],[0.450618,-3.247946,4.827522,7.914172,-1.500965,9.540167,7.133583,-4.173049,4.796953,-8.291455,2.697567,-9.958491,-0.357467,4.823742,2.627175],[4.453551,-1.981204,7.906370,-6.129084,-5.838623,-1.946636,-8.561828,-9.955510,0.760033,5.261233,6.592894,3.803829,2.962198,-1.299868,6.278324],[-6.723854,-7.379674,0.863117,4.796911,-7.138170,-4.193034,7.799877,-3.701709,1.972587,-9.339192,-1.284586,-7.605974,0.759599,1.634893,-8.198868],[7.281775,-2.332287,6.856419,8.539159,6.444485,-2.695654,-1.736990,1.924589,-4.580157,3.228026,7.188985,-5.217780,3.500942,8.025445,7.511492]],[[-6.515201,-4.633370,-2.772291,-0.171815,-8.435766,6.973649,3.705241,3.817259,4.583928,9.647394,-3.874852,-8.588268,-6.520730,-5.141792,-6.154533],[9.876010,-8.536643,9.085313,6.678849,-8.174935,-6.518975,5.047216,-1.470644,-7.606258,-8.951838,-9.341835,-5.791080,2.585316,-6.806325,-0.942264],[7.991756,0.489300,9.637752,-1.313957,-1.748334,6.696467,-0.238340,-4.305574,6.912153,-3.639583,9.336408,-8.129528,1.831490,-3.774604,1.469608],[5.618814,5.817839,-0.509135,3.876596,7.368872,4.531848,-9.064406,3.304272,-1.764917,9.513332,-1.843602,7.624704,-5.900905,-6.857370,4.953838],[1.592236,-2.428622,0.820912,-0.758201,0.890886,5.140758,-7.177913,4.342608,-1.927561,-2.211623,-2.392256,-6.497641,9.497102,9.067643,-5.526286],[3.773280,0.557751,-3.023774,-1.936784,0.903566,-9.116650,-4.256185,1.607533,9.741273,-5.893192,0.680726,-1.567600,-6.025914,2.051811,-0.453877],[-1.450240,4.463104,4.922390,1.691438,-2.008034,-3.290483,2.856589,9.525066,-5.960828,-6.256677,-8.632879,8.692927,-7.161122,-1.960280,4.766887],[3.884687,-5.844531,0.666592,-7.989627,1.052829,-8.996645,4.468467,4.123055,-0.327551,3.246362,-1.782936,-4.313810,4.515130,4.660054,-0.935843]],[[-3.255297,6.412082,6.194506,-2.048792,3.692439,-9.422986,0.437127,8.976280,5.485265,-4.274425,-5.525583,-7.236854,6.121408,1.045011,-3.600459],[8.921845,8.106027,1.847453,-2.971709,-7.789376,-9.544538,9.248537,9.750721,-4.540447,-9.931638,6.487626,5.835627,3.497082,0.930512,4.380739],[9.345322,-1.872282,7.388672,1.670651,-2.659352,4.801609,-1.677831,-6.502899,7.974891,-3.601041,-8.489727,7.404232,-5.857958,-2.503864,5.107222],[8.251790,-8.733922,-8.312576,0.433450,9.116594,8.109968,-5.633944,9.158333,8.602320,4.739326,-5.892078,-4.420051,5.803258,9.420231,-6.873196],[-9.460147,9.698691,-7.755958,-2.710033,4.333409,1.478324,5.718878,-8.284248,-9.810128,9.511043,-9.709790,6.206642,8.207269,5.648624,-6.812569],[-0.901499,8.616795,-4.853592,4.495550,9.821620,-9.785573,3.081036,4.137968,0.390224,-7.449785,9.446371,-8.821887,3.486358,-8.283570,-3.481619],[-0.044363,0.310056,-8.614248,0.242939,-8.698030,-4.560693,8.324745,-9.527660,-9.518073,4.621724,9.906294,7.127573,6.309985,8.336124,6.520048],[7.792203,-4.580391,7.896929,-2.440983,-0.030973,6.821151,0.827464,2.348104,5.769777,5.775089,-2.041892,-2.803254,3.500969,-3.653406,2.426322]],[[-2.041517,3.288949,9.974578,-3.918458,-4.071157,-2.616373,1.954949,-6.174872,-0.450913,-0.989349,-0.637292,-5.561936,-5.431843,6.600988,-3.089608],[-5.042017,0.639459,-1.652839,-9.079375,-8.113604,9.398421,0.363951,-4.209251,1.112156,4.326528,6.054971,-1.786078,-8.425624,2.338411,1.891233],[-4.244565,-6.546267,-1.584598,-7.791980,3.233591,2.166554,-8.133123,-1.795423,-0.818962,4.918680,5.436352,-4.907951,-2.939560,2.296267,-4.892985],[2.177735,-8.943365,-0.922196,-8.830394,-2.692270,2.029623,0.849898,-0.632623,-8.063323,6.596671,-6.879839,-2.757632,8.283905,-0.719303,-5.099135],[6.636886,6.560222,-7.987208,-2.399752,5.363888,-7.775463,-6.503054,-3.421836,5.229348,-8.811210,-8.736608,-2.156356,4.983124,3.138182,-9.718557],[-3.974854,1.594222,1.817163,7.744273,5.233535,-7.639763,0.198978,0.020821,7.486860,-4.643719,1.100032,4.367938,-1.785666,0.928511,-5.266487],[1.428032,-0.985495,-7.137811,-4.947104,7.273976,-6.054307,-4.554166,6.992193,8.379912,-9.669138,-5.793798,-3.915992,6.847719,-0.770276,-7.521632],[-6.568359,7.496058,5.447443,5.887744,8.134565,8.345095,-4.907853,2.996843,5.924347,1.767058,-1.958759,3.579645,6.068860,6.069165,-0.058398]],[[-3.237131,-8.170415,0.063944,3.613358,4.666826,4.619579,1.472945,-5.317484,6.616801,4.482858,-2.554852,-6.206424,1.519793,-9.651914,7.433219],[-1.027243,-8.991712,5.127965,-1.264964,-9.016283,6.238506,-6.686504,1.643802,9.717294,-2.544244,5.796996,0.384508,2.685213,0.209456,2.369562],[-8.507197,-9.522677,-8.351239,-4.029550,7.668459,8.547140,-5.160961,8.591745,-4.757923,7.260335,2.213648,1.392506,-5.339415,9.283933,0.531135],[1.091217,3.811059,-7.565714,6.080911,-8.391546,8.778071,-0.406084,-6.774190,6.367089,-9.887541,8.746695,-8.708748,-4.097957,3.540913,-8.093425],[5.765268,-7.628735,-1.701922,-6.806491,9.225585,-3.146505,-5.271171,2.004671,-1.327505,-9.610200,0.871107,-8.351405,-3.777445,-1.550119,1.847993],[-2.934241,-4.155747,7.224001,3.113348,6.650509,-4.223327,9.645684,-0.389926,3.715858,-4.121282,7.475191,-2.188083,5.824981,5.556698,-8.336953],[-4.518198,0.544316,-1.849266,8.955449,-6.937624,-0.943783,-1.308307,-7.493417,-8.089731,0.183648,3.652295,-9.673986,3.171542,-7.221044,-9.211762],[9.452185,-3.244568,8.018575,3.311292,-9.424524,6.520602,-2.651967,9.811586,-2.653294,2.769413,-7.827643,2.630100,-0.382827,-0.026165,2.126158]]], dtype = "float64")#candidate|9021|(13, 8, 15)|const|float64
uop_9022 = relay.atan(const_9021.astype('float64')) # shape=(13, 8, 15)
func_1237_call = mod.get_global_var('func_1237')
func_1239_call = mutated_mod.get_global_var('func_1239')
var_9037 = relay.var("var_9037", dtype = "float64", shape = (315,))#candidate|9037|(315,)|var|float64
call_9036 = relay.TupleGetItem(func_1237_call(relay.reshape(var_9037.astype('float64'), [7, 5, 9])), 0)
call_9038 = relay.TupleGetItem(func_1239_call(relay.reshape(var_9037.astype('float64'), [7, 5, 9])), 0)
output = relay.Tuple([uop_9022,call_9036,var_9037,])
output2 = relay.Tuple([uop_9022,call_9038,var_9037,])
func_9047 = relay.Function([var_9037,], output)
mod['func_9047'] = func_9047
mod = relay.transform.InferType()(mod)
var_9048 = relay.var("var_9048", dtype = "float64", shape = (315,))#candidate|9048|(315,)|var|float64
output = func_9047(var_9048)
func_9049 = relay.Function([var_9048], output)
mutated_mod['func_9049'] = func_9049
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9159 = relay.const(-5, dtype = "uint16")#candidate|9159|()|const|uint16
var_9160 = relay.var("var_9160", dtype = "uint16", shape = (6, 4, 12))#candidate|9160|(6, 4, 12)|var|uint16
bop_9161 = relay.less(const_9159.astype('bool'), var_9160.astype('bool')) # shape=(6, 4, 12)
output = relay.Tuple([bop_9161,])
output2 = relay.Tuple([bop_9161,])
func_9169 = relay.Function([var_9160,], output)
mod['func_9169'] = func_9169
mod = relay.transform.InferType()(mod)
var_9170 = relay.var("var_9170", dtype = "uint16", shape = (6, 4, 12))#candidate|9170|(6, 4, 12)|var|uint16
output = func_9169(var_9170)
func_9171 = relay.Function([var_9170], output)
mutated_mod['func_9171'] = func_9171
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9187 = relay.var("var_9187", dtype = "float32", shape = (2, 10, 3))#candidate|9187|(2, 10, 3)|var|float32
uop_9188 = relay.log10(var_9187.astype('float32')) # shape=(2, 10, 3)
output = uop_9188
output2 = uop_9188
func_9194 = relay.Function([var_9187,], output)
mod['func_9194'] = func_9194
mod = relay.transform.InferType()(mod)
mutated_mod['func_9194'] = func_9194
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9195 = relay.var("var_9195", dtype = "float32", shape = (2, 10, 3))#candidate|9195|(2, 10, 3)|var|float32
func_9194_call = mutated_mod.get_global_var('func_9194')
call_9196 = func_9194_call(var_9195)
output = call_9196
func_9197 = relay.Function([var_9195], output)
mutated_mod['func_9197'] = func_9197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4590_call = mod.get_global_var('func_4590')
func_4592_call = mutated_mod.get_global_var('func_4592')
call_9239 = relay.TupleGetItem(func_4590_call(), 2)
call_9240 = relay.TupleGetItem(func_4592_call(), 2)
func_5737_call = mod.get_global_var('func_5737')
func_5740_call = mutated_mod.get_global_var('func_5740')
const_9242 = relay.const([-2,2,3,-10,9,-7,6,3,4,5,-10,10,8,2,-5,5,3,5,9,3,1,-3,3,3,3,7,-10,3,-8,10,-1,3,10,-1,3,7,3,-1,7,-8,-3,6,-4,1,-5,5,6,9,6,-9,4,-3,5,7,-9,4,10,5,-10,-5,-9,-10,-8,3,1,-3,7,3,-1,7,3,-9,-1,6,3,8,-2,7,7,4,-3,2,4,-5,6,-2,-3,-4,7,8,3,-2,-4,7,-2,-1,9,-6,-9,-5,-2,5,-7,-2,1,6,7,9,6,3,8,-4,7,7,2,-2,8,-2,8,-1,5,5,5,3,1,-1,2,-3,5,7,-1,-2,10,-5,-9,9,4,-7,-7,10,8,6,-7,9,10,-9,-6,-1,-8,-5,3,-10,8,-7,10,3,-1,8,-10,1,-2,3,5,6,-2,-8,-7,-3,-10,1,8,-5,-5,-8,-9,-4,-1,-1,-3,-8,10,-2,-6,3,5,-5,-8,-3,-3,-7,-10,-3,2,-7,-5,-9,-1,-3,6,-5,1,-6,-10,3,2,4,-3,-4,5,9,6,-6,-9,-4,-6,-5,-8,-4,-4,10,9,1,-4,-6,-8,-8,2,-1,-2,5,-5,3,-5,-2,7,6,-9,-7,-2,2,7,4,6,2,10,8,-10,-9,-1,4,2,-2,-7,-3,-2,-8,-7,-10,-8,2,10,1,2,-6,10,9,-10,-4,9,-3,-4,-2,5,-3,6,9,7,7,2,10,-3,-8,1,-7,1,3,-3,6,7,-9,7,1,9,-1,1,-5,-2,5,-6,4,-2,-3,-4,-3,10,-3,1,1,2,-3,5,5,-2,9,-1,-5,1,-10,-9,-5,-4,-6,-4,4,-8,9,6,1,4,-8,-6,-10,3,2,-10,8,9,8,10,-9,9,-4,-2,5,-6,3,-7,8,2,3,9,5,-7,1,-4,-6,10,8,-6,8,-7,1,-3,-8,-9,6,-2,7,-5,-5,-1,-10,4,5,-2,-9,5,4,8,-2,3,-6,10,-2,-2,-3,-1,-5,2,4], dtype = "int32")#candidate|9242|(390,)|const|int32
call_9241 = relay.TupleGetItem(func_5737_call(relay.reshape(const_9242.astype('int32'), [6, 5, 13])), 2)
call_9243 = relay.TupleGetItem(func_5740_call(relay.reshape(const_9242.astype('int32'), [6, 5, 13])), 2)
var_9286 = relay.var("var_9286", dtype = "int32", shape = (390,))#candidate|9286|(390,)|var|int32
bop_9287 = relay.divide(const_9242.astype('float64'), relay.reshape(var_9286.astype('float64'), relay.shape_of(const_9242))) # shape=(390,)
bop_9305 = relay.bitwise_or(var_9286.astype('uint8'), relay.reshape(const_9242.astype('uint8'), relay.shape_of(var_9286))) # shape=(390,)
output = relay.Tuple([call_9239,call_9241,bop_9287,bop_9305,])
output2 = relay.Tuple([call_9240,call_9243,bop_9287,bop_9305,])
func_9318 = relay.Function([var_9286,], output)
mod['func_9318'] = func_9318
mod = relay.transform.InferType()(mod)
var_9319 = relay.var("var_9319", dtype = "int32", shape = (390,))#candidate|9319|(390,)|var|int32
output = func_9318(var_9319)
func_9320 = relay.Function([var_9319], output)
mutated_mod['func_9320'] = func_9320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5474_call = mod.get_global_var('func_5474')
func_5475_call = mutated_mod.get_global_var('func_5475')
call_9328 = relay.TupleGetItem(func_5474_call(), 0)
call_9329 = relay.TupleGetItem(func_5475_call(), 0)
func_3274_call = mod.get_global_var('func_3274')
func_3278_call = mutated_mod.get_global_var('func_3278')
const_9340 = relay.const([[1,9,2,5,3,-3,-7,6,6,1,-5,3,8,9,9,2,-5,-9,-10,-7,4,5,7,-3,7,-6,10,10,1,5,-9,2,-5,-1,9,10,-7,5,8,1,-3,8,4,-1,-7,9,-1,-10,-1,-5,-6,-4,-10,9,10,-3],[-4,-8,1,7,4,-4,6,5,-2,10,5,-2,-4,5,2,-8,-1,7,4,9,-10,4,4,5,-10,-7,8,2,-2,-7,6,-9,2,8,1,-5,-10,-7,10,4,7,-7,-1,-9,5,-5,3,-8,1,-10,-5,3,4,4,2,-6],[-9,3,1,1,10,-6,4,-8,2,-7,-3,-4,2,2,6,-2,10,-5,7,-8,-5,-8,8,4,-3,9,-3,2,-3,-9,4,-5,5,7,7,-9,-10,9,-2,-10,-6,-1,-1,6,1,2,7,10,-7,-5,2,9,2,10,3,-9]], dtype = "uint16")#candidate|9340|(3, 56)|const|uint16
var_9341 = relay.var("var_9341", dtype = "float32", shape = (105,))#candidate|9341|(105,)|var|float32
call_9339 = relay.TupleGetItem(func_3274_call(relay.reshape(const_9340.astype('uint16'), [168,]), relay.reshape(var_9341.astype('float32'), [105,]), ), 5)
call_9342 = relay.TupleGetItem(func_3278_call(relay.reshape(const_9340.astype('uint16'), [168,]), relay.reshape(var_9341.astype('float32'), [105,]), ), 5)
func_8512_call = mod.get_global_var('func_8512')
func_8516_call = mutated_mod.get_global_var('func_8516')
const_9350 = relay.const([-3.953946,-2.061231,9.632491,8.976953,-0.957166,9.161150,6.161965,-4.465419,-0.081794,2.984885,-9.443032,-2.268026,-5.461171,-5.797186,-0.088707,4.580815,-7.527235,8.376322,0.873200,2.745264,-4.461690,7.561345,-9.193935,1.174069,4.064450,0.269630,4.387245,-3.098177,-3.680443,7.132482,5.740133,5.158542,-7.881206,1.023069,9.820823,7.867903,6.993114,-7.108071,-7.627463,-1.367986,-6.360589,5.952564,6.196977,-4.202718,-5.554713,-0.698875,-0.631374,-7.180205,-3.449802,-1.433027,-4.066997,5.390870,-3.857036,3.086285,-5.581631,-5.572538,5.799095,-6.157852,-1.834711,-4.324839,-2.849465,-4.635221,-5.137331,-7.044051,-6.386218,5.593507,-7.954241,-7.041160,-4.972815,-1.173726,5.328458,3.902022,-2.213706,-6.934017,-8.589595,-6.677418,6.027753,4.728974,4.721595,2.477955,-9.474830,-4.420264,0.908206,-7.444126,1.739548,-6.351121,7.501889,2.681712,2.577089,-9.445010,2.772858,1.212324,4.775986,-9.226016,-1.131103,-4.881661,-2.802706,5.669233,0.877581,1.637024,-0.576554,-5.073181,-1.159479,-6.971458,1.286289,9.262366,0.237093,3.988579,-0.284423,3.834259,9.338532,2.763642,-8.881391,-5.015008,-6.573354,-7.501329,7.448690,8.698434,8.675374,-7.877719,-6.395513,5.720322,-8.970233,4.662514,-4.720048,8.068552,-0.487913,-8.696603,8.249522,6.429992,-7.740201,1.546817,-0.965550,8.218577,-2.475510,-1.625132,-4.648725,-3.691910,-0.973320,4.616887,-7.819905,3.122582,9.445528,3.278045,-7.462939,0.928399,6.073729,-2.784696,1.026237,4.280642,7.467133,-2.974612,3.978051,-7.689516,-7.827119,-8.783670,-1.383804,-2.886853,9.783901,8.434646,-2.901988,6.110906,4.913335,4.521447,0.716874,-0.241030,-4.160802,-1.817110,6.473211,7.692655,-2.596727,-5.021135,5.186340,1.657905,-1.171564,-8.129819,9.183089,-8.829881,-1.069237,7.337562,-5.860828,-3.388272,-0.880086,-6.611813,-6.939595,-2.371109,-1.162597,3.775741,7.529023,-2.933923,4.527188,-7.132346,-1.384363,2.588949,-0.469011,9.154773,-4.665080,0.221983,-7.129428,-1.054417,8.153254,-5.027316,7.254032,-4.718415,-0.459069,8.174999,3.018676,-8.082206,-3.204479,-5.555150,-0.887715,-1.968209,-2.884350,1.532108,3.419011,1.683737,-0.549338,-2.000816,8.907555,-9.984831,-6.586062,-3.347918,7.353551,9.282878,-5.616560,-5.668171,2.673932,-0.622496,-5.824290,1.055604,0.530692,1.677267,-7.931744,-7.616955,-0.198306,6.062218,-3.345100,-6.357490,-5.766883,8.023448,-3.763618,2.265153,-1.232813,7.679792,8.016074,5.343618,8.488342,2.652263,-6.118598,8.829031,-9.408908,1.476138,-0.961224,9.878559,-8.008566,-0.125903,-7.041254,-1.324767,5.880142,-9.640023,-5.159500,4.397854,-1.986561,0.056421,-3.511128,4.308751,1.784379,0.027598,-3.357627,-0.068513,-0.222081,8.900383,-2.615290,4.401394,7.780836,5.536534,7.966480,4.333952,6.583863,4.432998,-1.964062,-1.036822,7.329867,6.586774,-0.106429,-2.364347,-9.668403,-5.946966,-9.947494,-8.615715,0.266195,1.401557,1.572852,-9.387103,-1.882115,-2.861672,-3.781205,-4.135650,2.642880,1.912124,-8.511137,-7.534114,-5.347121,1.159616,-5.718302,-7.735600,5.575648,9.407504,3.956144,5.614929,5.235479,-8.260983,7.234930,1.362325,-6.764243,-2.568704,0.470399,-1.723956,0.134006,-8.580184,8.651462,4.875379,-3.594983,7.705592,-7.193607,1.503460,4.556042,4.767102,7.880873,8.144676,-1.613888,-7.458523,-4.372784,1.373626,-3.628786,2.954443,-7.887916,3.455664,8.239453,-4.485897,9.704604,0.108212,7.373700,5.836758,-4.879511,9.810554,2.694253,-8.780282,-6.522531,7.144835,2.243897,-0.547122,-7.406707,-0.568283,8.684739,3.103124,6.727834,4.541511,-8.595148,4.334353,5.975235,9.289703,-1.572482,-5.583483,8.840417,1.899700,-2.119062,-6.923511,9.990994,2.167424,-8.581657,-8.632986,1.891676,-4.229770,-9.820766,-9.690884,-9.554758,-0.959237,3.521956,4.139674,8.127098,5.063383,5.438735,-8.254633,2.319887,4.609463,-2.630311,7.716233,9.448865,3.859662,7.097447,4.816146,5.322875,-5.980088,-8.954316,9.003715,-7.282327,1.380993,1.390996,0.360458,1.221684,-0.666571,-7.998370,-9.801194,6.692295,4.853656,5.142076,6.297854,4.314201,-8.497940,1.687499,5.349117,-7.629677,4.193593,-6.634149,-7.879459,6.870843,4.620426,-0.553218,1.599938,-6.002446,-4.238949,0.995220,-8.431199,0.521432,-7.093225,4.655478,4.672877,3.566408,7.677249,2.671207,5.486273,-7.466993,-0.166459,-7.886197,-3.214610,-1.455221,3.243880,-7.442167,-8.380901,-1.747004,1.315237,-7.296409,9.149144,6.438370,4.824245,9.373204,-1.199928,-7.265168,-4.106010,-8.159061,0.581732,-6.343040,7.516920,-7.812367,-6.336955,-7.781813,-7.331908,-6.703818,-5.973463,-4.050179,-3.929748,9.528742,6.043491,4.136181,-8.918034,2.479678,1.689099,-9.242792,-1.834966,-6.754504,0.953380,-7.717607,-2.550352,-6.988857,9.980893,-8.190037,-2.626331,-1.169598,4.314729,2.251711,7.681789,5.533395,-5.835852,6.361942,7.023061,-3.324621,1.215245,-6.200957,6.947129,-8.193680,-8.205137,8.287632,-5.554963,-0.219689,3.814437,-3.539108,-6.035658,7.254354,1.323499,-2.216216,7.603024,-5.000956,9.464328,-8.135809,9.185627,5.190736,9.228577,-5.691823,-3.319262,-7.426930,-1.247718,9.658460,-5.151215,-6.204701,9.086068,-1.144925,3.788997,1.948438,-4.023212,8.895042,8.658744,9.167862,0.720691,-6.138904,-2.161867,-7.333518,4.483381,-1.893681,-3.414321,-4.838421,1.710655,-6.278291,5.019169,6.544335,2.062661,2.917016,-4.343930,-0.415090,-3.144752,9.679308,3.570473,6.011757,6.203437,-9.487400,-4.983082,-3.453395,-7.088284,-3.832840,-7.871164,8.525595,9.895827,-4.807606,1.363382,2.168106,-4.537158,-8.668387,-9.506343,-7.563443,5.129780,-6.412510,8.607267,6.861751,1.379811,2.565896,-7.473868,-7.062095,2.762499,7.275323,6.119322,-0.687928,0.728364,8.468706,9.748194,-9.709948,-2.091933,-8.765473,5.845594,5.750875,-9.544112,-7.247183,1.305342,-4.935932,-7.259489,5.366893,-4.684317,2.107900,6.222693,-7.965725,-9.724290,6.599979,1.516848,4.973245,-5.156438,1.994594,9.274160,6.725813,-2.057719,-1.036072,2.846782,-8.315765,1.073429,6.247409,-0.558301,9.602892,-4.126177,-5.522776,3.506102,-9.192341,-1.128778,-9.479545,-4.495787,0.378376,3.544976,3.111165,0.057934,-1.365690,4.161003,4.086494,7.666066,-9.043145,-6.920613,7.545274,-8.337565,8.435775,-3.837670,6.854152,9.947279,9.243344,-6.939434,2.417088,9.413722,-3.897476,5.019830,-6.849932,9.667274,7.615542,9.072785,0.984640,-1.833559,1.590164,-5.938132,4.862162,5.077910,-3.958802,3.739779,6.126011,6.878630,5.655645,-3.762481,-2.041687,6.937546,2.086977,-3.358883,-3.765206,2.790877,4.529315,-9.644312,4.048430,-5.961172,3.163933,7.848919,-9.246058,9.862062,4.530554,5.859395,0.328475,6.798760,-0.373057,9.636539,4.835232,-3.725317,-8.178399,0.259444,-3.180522,6.472471,-7.334489,-9.136750,3.172517,-5.632718,5.890759,-4.284843,-9.980176,4.035077,-5.910282,-5.773620,6.706113,-3.914167,5.758833,1.538845,4.688028,-2.387809,2.371173,-3.938794,-6.610502,-8.618281,0.249960,-1.818329,-3.978090,-8.539218,-1.951094,-3.746569,8.335783,7.002663,1.173946,-4.048801,0.359368,-0.357605,3.067716,4.590957,9.775550,-0.426077,7.991568,7.761664,-3.669156,-2.805851,-1.788928,1.402439,2.541292,-9.279389,1.702366,-3.466781,7.787213,-6.387044,8.081168,-3.826761,2.218409,2.454721,9.306086,-7.059368,-6.510132,-1.038188,-1.167542,-6.614612,-4.162137,-5.354376,4.758458,-9.344017,8.187349,-8.837798,1.866601,8.703956,6.672336,2.594407,5.900798,-9.392309,-4.487038,-4.381873,-9.399387,-3.062108,-0.892689,6.755648,8.195310,-0.263965,-5.712176,-5.223546,-5.487527,-8.650770,-0.002073,-8.733555,6.496457,-4.702726,-6.766470,-2.445872,3.485415,6.259247,5.015150,-6.719865,3.788486,6.586709,2.889969,6.151272,-4.220617,5.890931,8.324955,-6.091118,-4.764573,-3.087541,-4.912687,-8.709129,9.873012,7.574854,-4.966305,-6.464854,-9.358829,7.006237,6.030187,1.531488,-0.460941,-6.912353,4.878655,-5.225402,2.957169,-8.838841,-4.987145,-6.863986,-1.598040,-1.583211,3.221647,-0.254699,2.174497,4.405569,-0.973062,-1.101688,4.221100,-7.786730,8.602551,-1.391603,0.059878,-7.439680,1.838208,-5.784758,-1.105175,-6.631555,0.865998,-4.276918,-2.780219,9.588811,-9.787027,0.652778,-6.721166,-5.230040,4.785187,2.992230,4.208171,-5.965686,-5.006155,4.850288,4.777386,-3.822000,-1.036011,8.326539,-3.006001,-8.911002,-4.312483,-3.081657,1.320720,3.895296,4.463579,-6.925170,-2.240238,-0.158430,3.390986,-8.095600,9.242058,0.456342,2.197848,9.572232,8.615014,-4.813260,3.334064,-8.009954,-7.447440,1.503380,-7.955352,-0.556626,-6.781287,8.429223,-5.783678,3.591776,-1.685118,-7.378206,8.807036,6.422244,3.647139,8.898088,-8.399920,4.053036,6.141500,2.642639,-7.368933,-3.177025,-5.269115,-9.654448,8.176162,-2.708009,-2.248010,6.215421,-2.987962,-8.039366,0.068586,1.224412,-0.547596,-0.584144,5.191299,4.285524,8.166908,5.018263,-2.135504,0.132677,8.084048,8.564490,-7.510353,7.920581,-9.309691,-5.541406,6.516065,0.821353,-9.265573,0.662346,5.375550,-0.185501,3.845829,-6.214199,4.783824,4.814745,-7.940828,4.509854,-5.049315,5.471420,-3.754483,-1.191255,3.392757,6.080455,3.798523,-1.079327,-3.278530,7.989890,-1.148775,1.956363,9.436886,-2.916826,2.841192,-8.682701,-3.018517,-4.901815,5.343785,9.355304,8.501212,2.473938,5.201232,7.901183,-2.013569,3.650097,9.224271,-0.474508,-1.659322,-7.039831,-9.769926,2.374013,-2.817537,-1.297434,-2.202462,4.708747,-1.045067,-6.311442,-1.247808,5.661818,-6.929460,6.102684,6.804400,2.896862,-3.503954,-7.835002,-3.876823,2.849944,8.642512,8.628329,9.730987,9.859436,7.155004,-6.365655,-4.698320,-5.170085,-5.354517,-4.675021,1.812232,7.378038,4.658678,6.360579,5.661637,-0.094386,-6.716351,-3.577280,-6.758462,3.854147,4.239620,5.773137,-2.262100,9.398604,8.064428,-7.498894,7.912171,-9.906233,2.596117,-5.250250,4.370020,-5.620433,-5.349089,2.518718,-1.292459,-2.948149,-0.244478,8.416863,6.674716,-6.210031,-8.032657,-4.999514,-9.097267,-6.115378,-6.588078,9.057646,-3.306572,7.866806,-1.998653,0.872040,0.843292,7.263069,-6.216229,-0.455261,1.085211,-0.987298,-2.037763,7.263360,-0.574803,-4.183385,-7.455789,-9.101882,5.872961,-5.300822,-0.441032,5.462428,9.944301,-5.875463,6.273360,-5.757851,8.356325,4.321498,9.441779,-2.294922,-3.828875,-1.141690,-3.057896,5.242147,-2.948281,-8.284420,-2.775498,-6.239238,-5.639849,0.052661], dtype = "float32")#candidate|9350|(1040,)|const|float32
var_9351 = relay.var("var_9351", dtype = "int64", shape = (270, 1))#candidate|9351|(270, 1)|var|int64
const_9352 = relay.const([[4,10],[-6,3],[3,4],[-9,6],[-1,-1],[-7,-5],[-2,-7],[-2,-4],[-6,-8],[-5,6],[4,9],[-2,-7],[5,1],[5,-6],[-7,-3],[5,7],[-2,-8],[5,6],[-3,-3],[9,-7],[7,10],[-5,1],[7,-1],[1,-8],[3,3],[-1,9],[3,-6],[-9,-1],[-4,-8],[-5,-1],[5,9],[-1,1],[2,-4],[-3,6],[3,2],[-8,10],[-4,-10],[-7,5],[2,8],[-8,7],[-4,-4],[4,-5],[-3,-10],[-10,10],[-9,4],[1,8],[1,7],[6,3],[5,-7],[9,-7],[-8,3],[5,1],[6,-10],[7,10],[-5,-9],[-3,2],[-4,-8],[-10,-5],[-9,-6],[4,10]], dtype = "uint8")#candidate|9352|(60, 2)|const|uint8
call_9349 = relay.TupleGetItem(func_8512_call(relay.reshape(const_9350.astype('float32'), [1040, 1]), relay.reshape(var_9351.astype('int64'), [3, 90]), relay.reshape(const_9352.astype('uint8'), [120,]), ), 2)
call_9353 = relay.TupleGetItem(func_8516_call(relay.reshape(const_9350.astype('float32'), [1040, 1]), relay.reshape(var_9351.astype('int64'), [3, 90]), relay.reshape(const_9352.astype('uint8'), [120,]), ), 2)
func_9318_call = mod.get_global_var('func_9318')
func_9320_call = mutated_mod.get_global_var('func_9320')
const_9364 = relay.const([[4],[8],[8],[-5],[-3],[5],[-3],[-4],[-10],[-2],[1],[9],[3],[-5],[-7],[-4],[9],[-10],[4],[-1],[8],[-8],[7],[-9],[-5],[1],[-7],[7],[2],[-4],[2],[-7],[10],[8],[-7],[-10],[5],[7],[-1],[8],[7],[3],[2],[3],[3],[10],[-7],[-6],[8],[-10],[5],[9],[-9],[-1],[-3],[6],[8],[4],[-1],[-1],[-6],[10],[2],[10],[-10],[-5],[10],[6],[-2],[-10],[5],[3],[-7],[-3],[-5],[1],[-9],[-3],[-6],[1],[3],[2],[9],[3],[-4],[6],[-8],[3],[7],[-2],[-2],[4],[-5],[-2],[-9],[-7],[-8],[6],[-7],[-1],[-1],[-2],[-8],[-4],[3],[-7],[-2],[-8],[-9],[-8],[-3],[3],[-5],[3],[9],[5],[-10],[8],[-2],[-5],[10],[-9],[5],[9],[-8],[-2],[-1],[-6],[-5],[8],[-2],[-1],[10],[2],[-4],[6],[-9],[8],[4],[5],[4],[5],[-4],[2],[10],[1],[-3],[-4],[-4],[6],[3],[3],[8],[-3],[-1],[-4],[-8],[10],[2],[9],[-4],[-3],[5],[-1],[-6],[-6],[-8],[1],[2],[-8],[-4],[6],[5],[-4],[-2],[10],[3],[2],[-5],[-6],[1],[-9],[3],[-8],[-6],[6],[1],[2],[9],[-5],[-8],[6],[10],[-1],[4],[-5],[-9],[5],[6],[5],[-2],[-4],[4],[-10],[-3],[-4],[2],[6],[10],[7],[5],[9],[8],[-6],[-9],[-10],[3],[-3],[1],[1],[-10],[7],[-7],[-4],[-10],[-10],[-4],[-7],[-7],[1],[-5],[9],[5],[6],[-5],[2],[-2],[-7],[-1],[5],[-3],[4],[-8],[-4],[-7],[10],[-5],[1],[-1],[10],[6],[3],[-10],[-6],[-3],[-4],[-9],[-4],[3],[-1],[2],[-2],[2],[-1],[-2],[1],[10],[5],[-6],[4],[-5],[-6],[1],[3],[-7],[-6],[-8],[7],[4],[3],[6],[6],[-9],[9],[6],[-5],[-6],[-7],[-10],[-2],[-5],[-7],[7],[-2],[-4],[8],[8],[10],[-7],[-3],[4],[5],[-10],[6],[-3],[8],[-5],[2],[10],[2],[7],[-6],[6],[-4],[-4],[-7],[6],[8],[-4],[-5],[-1],[6],[9],[9],[-10],[-5],[-10],[5],[8],[-10],[-8],[-3],[-7],[-2],[7],[10],[10],[5],[2],[1],[4],[-10],[-9],[-2],[-4],[-1],[9],[9],[-7],[1],[-8],[-4],[-4],[10],[-3],[-1],[-4],[-5],[8],[10],[-2],[-4],[-7],[1],[2],[9],[-10],[10],[2],[-4],[-8],[-3],[-8],[5],[-8],[7],[8],[-2],[-4],[8],[-2],[8],[10],[10],[8],[8],[-10],[8],[1],[-3]], dtype = "int32")#candidate|9364|(390, 1)|const|int32
call_9363 = relay.TupleGetItem(func_9318_call(relay.reshape(const_9364.astype('int32'), [390,])), 3)
call_9365 = relay.TupleGetItem(func_9320_call(relay.reshape(const_9364.astype('int32'), [390,])), 3)
uop_9366 = relay.sinh(const_9352.astype('float32')) # shape=(60, 2)
func_4590_call = mod.get_global_var('func_4590')
func_4592_call = mutated_mod.get_global_var('func_4592')
call_9376 = relay.TupleGetItem(func_4590_call(), 0)
call_9377 = relay.TupleGetItem(func_4592_call(), 0)
uop_9378 = relay.atanh(call_9349.astype('float32')) # shape=(1040, 1)
uop_9380 = relay.atanh(call_9353.astype('float32')) # shape=(1040, 1)
output = relay.Tuple([call_9328,call_9339,const_9340,var_9341,const_9350,var_9351,call_9363,const_9364,uop_9366,call_9376,uop_9378,])
output2 = relay.Tuple([call_9329,call_9342,const_9340,var_9341,const_9350,var_9351,call_9365,const_9364,uop_9366,call_9377,uop_9380,])
func_9382 = relay.Function([var_9341,var_9351,], output)
mod['func_9382'] = func_9382
mod = relay.transform.InferType()(mod)
var_9383 = relay.var("var_9383", dtype = "float32", shape = (105,))#candidate|9383|(105,)|var|float32
var_9384 = relay.var("var_9384", dtype = "int64", shape = (270, 1))#candidate|9384|(270, 1)|var|int64
output = func_9382(var_9383,var_9384,)
func_9385 = relay.Function([var_9383,var_9384,], output)
mutated_mod['func_9385'] = func_9385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5381_call = mod.get_global_var('func_5381')
func_5382_call = mutated_mod.get_global_var('func_5382')
call_9387 = func_5381_call()
call_9388 = func_5381_call()
func_4395_call = mod.get_global_var('func_4395')
func_4396_call = mutated_mod.get_global_var('func_4396')
call_9396 = func_4395_call()
call_9397 = func_4395_call()
func_5363_call = mod.get_global_var('func_5363')
func_5369_call = mutated_mod.get_global_var('func_5369')
const_9402 = relay.const([[1.980896],[-7.543502],[3.677443],[-5.925613],[8.759804],[5.655863],[0.889420],[-3.919346],[4.008252],[9.951678],[8.158416],[4.250179],[-5.540586],[-7.496711],[9.279835],[-8.605554],[-5.014805],[-4.025844],[-4.693537],[7.498288],[7.936179],[-5.633333],[-2.499815],[1.400903],[0.756206],[8.710103],[5.076419],[-3.409480],[6.834567],[-7.352407],[-4.999258],[0.375273],[0.203409],[-8.393595],[7.869562],[5.907689],[-1.906340],[4.926432],[3.002503],[-7.174867],[4.709607],[5.389975],[-8.254114],[-1.534314],[-6.155873],[-8.033921],[-5.981648],[4.514429],[5.856822],[1.674227],[7.693237],[-3.335589],[-1.648736],[7.131076],[-5.484706],[4.824669],[5.507395],[-4.480976],[-0.140226],[-4.005294],[5.231476],[4.527034],[-5.511289],[2.305319],[-7.926037],[-4.988029],[-3.191928],[7.572037],[9.240604],[-7.854517],[5.905618],[6.527963],[-8.378057],[-8.957168],[6.472564],[-8.200548],[-0.382096],[-1.217298],[-4.101384],[-0.001493],[-6.981216],[9.095113],[5.940026],[5.446983],[3.702055],[5.400436],[1.465581],[5.735640],[-7.906987],[-4.070964],[-7.915591],[1.331367],[-3.447485],[-8.256802],[8.468819],[9.432224],[7.098428],[-8.986258],[-5.464253],[0.739829],[0.730772],[-0.638982],[-9.592687],[0.209390],[7.390904],[-6.749177],[-4.196322],[-0.512788],[3.672700],[9.264975],[-3.472256],[-9.321518],[8.700163],[-3.378282],[-4.647623],[7.321717],[-3.213493],[1.310955],[-0.838536],[-9.932847],[-6.087864],[0.101059],[-0.956874],[-8.024923],[-6.429714],[-4.607552],[-9.926441],[6.214937],[-6.703458],[1.332189],[2.813323],[-5.665817],[-1.813169],[-4.450941],[-2.637534],[9.324134],[0.650864],[2.049597],[-3.303595],[0.389761],[-9.327707],[0.775127],[-5.535184],[-7.834951],[2.171843],[-4.556119],[4.245236],[-7.338339],[-3.025790],[-7.671934],[0.151732],[1.459339],[-1.690589],[-0.894424],[-4.441354],[-5.996856],[-7.361068],[-6.798418],[-3.217182],[8.209411],[-6.435880],[-0.835842],[-5.230049],[-2.713205],[-7.206899],[-8.401456],[-7.701320],[-7.024251],[-7.132283],[0.576405],[7.020120],[9.863341],[-0.232075],[-1.592996],[3.392011],[-1.244525],[4.407601],[3.995748],[9.326679],[-0.478237],[-4.871496],[-8.679068],[0.251577],[6.415494],[4.683000],[-5.355866],[-9.626336],[-3.323474],[5.206727],[9.502165],[-1.068251],[5.960281],[4.819561],[-6.467149],[-3.411147],[-6.713209],[2.725075],[7.582413],[0.935480],[-0.360189],[7.802807],[3.107770],[2.989621],[-5.777612],[5.987377],[5.802629],[1.314970],[6.186362],[3.692770],[-1.805981],[2.475258],[-3.125711],[8.610359],[3.748470],[-3.270211],[0.831284],[-4.281844],[-1.683483],[1.622761],[5.536048],[-3.861691],[-7.471813],[6.723286],[-7.266078],[4.077985],[-6.437423],[6.888057],[2.844641],[-7.226860],[-4.915356],[1.609807],[-3.897860],[-7.993605],[8.065720],[-6.989735],[-3.537176],[7.117055],[-2.349176],[1.347093],[4.304280],[0.155929],[8.643281],[-9.927942],[6.957532],[1.188589],[4.506080],[-5.840188],[-6.334280],[-9.999436],[-6.348667],[-6.704899],[-8.852212],[2.252375],[-2.144108],[5.335609],[-4.640876],[9.186301],[-7.976959],[-1.800916],[-3.616116],[3.472448],[-7.660831],[-7.896430],[-7.265462],[-8.765601],[0.003102],[-5.128019],[-0.038894],[-3.481866],[-6.918323],[-1.631232],[9.727905],[-3.460742],[4.648360],[0.119411],[-7.042096],[-8.582313],[-9.287066],[2.388878],[6.762149],[0.208284],[2.148522],[-7.846077],[-7.463576],[-0.041893],[1.337559],[3.592625],[0.297169],[-9.961902],[-4.715301],[-2.573584],[-7.059148],[-9.606845],[3.040068],[1.490557],[5.818806],[9.393132],[-3.933550],[0.778851],[0.007634],[5.684686],[-3.740600],[0.649176],[-8.795234],[8.839970],[8.352782],[6.199039],[-1.714032],[0.456398],[-1.795659],[-7.466722],[2.470682],[-5.803976],[-9.165150],[-6.307455],[4.686430],[-1.071126],[-0.069924],[9.359373],[4.858544],[-4.651196],[7.107333],[-2.940063],[6.305427],[6.772952],[-9.245848],[9.769747],[-1.527177],[-0.553683],[8.341225],[-5.376898],[-3.960887],[6.149823],[-7.349265],[-9.279141],[2.422859],[-0.175462],[-0.478493],[-0.297677],[-1.722496],[4.009007],[5.365180],[9.848001],[-1.125362],[-9.400823],[-1.399854],[4.331267],[9.503918],[-8.911276],[0.958269],[1.003502],[2.431654],[0.658393],[-7.182816],[4.509209],[-8.947401],[-2.405917],[3.045110],[6.393846],[1.839709],[-0.213683],[-2.380314],[-3.167108],[-4.650054],[6.638379],[9.559056],[-4.416251],[-3.691246],[9.033607],[7.738904],[-3.321376],[3.926363],[9.813593],[-9.696723],[0.585769],[1.113869],[1.797422],[4.020033],[1.248187],[-7.535932],[5.188022],[-2.048774],[-1.560456],[-8.438488],[3.219004],[-8.569000],[3.353674],[-6.549730],[0.037860],[3.914234],[-6.193861],[-9.703393],[-4.388307],[-6.818253],[7.997768],[-9.278490],[-5.046260],[-4.250576],[9.613335],[-7.607341],[-2.084962],[-4.141834],[8.126569],[-0.456083],[4.011766],[8.415103],[-2.561117],[-2.047035],[0.585601],[1.640081],[6.246754],[0.889908],[-1.945721],[9.127020],[-4.855794],[-9.212361],[-1.345979],[-7.339536],[-9.982230],[-9.182432],[-8.538236],[7.968867],[3.528798],[8.091344],[-5.005895],[1.919482],[-4.691847],[-1.770416],[-8.192620],[3.574305],[4.400397],[8.219521],[-0.730835],[4.211981],[8.646164],[7.460005],[2.489071],[-9.503599],[-4.551531],[8.886738],[-6.650290],[-1.471999],[-0.748794],[7.290178],[-2.647698],[7.947557],[0.514195],[-7.400316],[7.535889],[-6.228832],[4.615992],[-7.101056],[-5.811384],[-5.487469],[9.938904],[-4.636132],[-0.347673],[-7.773235],[9.908250],[-1.220861],[-9.802499],[8.337017],[-0.370181],[-6.426335],[-1.457636],[-5.492220],[-0.241043],[-9.894581],[-3.638760],[6.537846],[4.891075],[4.073011],[-5.293367],[-4.678941],[-5.070317],[-2.454057],[-0.725051],[-7.997430],[3.531428],[-2.145383],[8.230049],[3.698360],[-4.404973],[-0.889923],[-2.043168],[-5.522159],[9.115865],[-5.188084],[5.638538],[8.641695],[8.197512],[1.229838],[-8.619626],[-1.131958],[-2.064054],[4.923832],[-7.977616],[6.486982],[-4.290769],[9.498073],[7.084107],[-5.283088],[7.273731],[-6.165609],[0.869480],[-7.640711],[7.085985],[1.224245],[3.878704],[0.733714],[-7.686026],[0.556816],[-6.694073],[5.652992],[8.004332],[7.157177],[-1.010195],[7.357392],[-1.538646],[6.186736],[-3.815821],[-5.445171],[5.214681],[5.117320],[-0.688713],[-6.637779],[5.668418],[8.786156],[-6.075071],[-2.020583],[7.316799],[-0.486508],[-9.533090],[4.887439],[7.566291],[-8.037541],[3.822791],[-6.584621],[-9.091639],[7.021016],[-3.335198],[-6.610743],[-8.931198],[8.404663],[-7.192371],[-9.748951],[-8.103838],[-6.361423],[-5.098208],[8.013828],[-5.907714],[4.152470],[5.567723],[-0.948747],[6.054034],[-1.048313],[5.140880],[6.692076],[-2.884827],[-3.884960],[0.695591],[-2.281379],[3.540927],[-0.887901],[-6.976955],[3.965729],[9.884179],[-6.671606],[-2.479541],[1.478195],[3.629004],[-6.182878],[-4.423819],[-9.935374],[-8.340709],[1.477921],[3.042688],[8.659077],[-6.551826],[-2.050924],[-1.346422],[0.557926],[2.522851],[-5.678586],[-7.488884],[0.278570],[9.375100],[-3.169682],[-1.390849],[-5.724874],[6.421419],[-6.771287],[3.335760],[0.880938],[1.470459],[-5.494864],[-7.549158],[6.324827],[-5.127518],[8.099652],[8.093227],[-9.941133],[-8.224244],[-0.733439],[5.696404],[-8.468495],[9.023891],[6.672742],[-0.742825],[-0.236456],[-0.131018],[2.974671],[8.687303],[-8.125856],[-0.552970],[-8.322009],[0.706364],[-8.046475],[-2.364301],[-0.384660],[3.544051],[-4.609338],[9.689212],[8.487701],[3.264742],[7.505539],[3.952243],[-9.366935],[8.429336],[-2.638187],[-8.185744],[-2.925453],[0.957676],[-7.103550],[5.726939],[3.017855],[0.331490],[4.812994],[8.138071],[-4.332396],[9.400191],[-4.528323],[2.131202],[7.440283],[-6.176929],[-5.907615],[-2.744738],[-7.440654],[-4.016425],[4.749455],[9.916764],[-8.546779],[5.552671],[2.159915],[4.186779],[5.767795],[9.059330],[8.430395],[-1.960848],[4.174785],[-8.936091],[1.617959],[-1.861493],[-4.175310],[-4.448136],[2.951676],[-1.248874],[-4.786294],[4.507761],[-5.863038],[-4.453467],[2.787408],[4.057079],[-2.877258],[8.185278],[-3.433007],[2.038603],[6.826166],[8.677976],[-4.967868],[3.089184],[8.631553],[-3.552057],[1.023243],[6.613656],[-4.679826],[8.416463],[6.201404],[-9.028633],[-5.358362],[-3.557291],[3.221663],[9.236224],[0.461903],[-2.582115],[-2.150357],[4.725598],[1.419433],[-3.428195],[-9.984474],[-9.168331],[8.309683],[-6.988625],[-1.411217],[-4.217700],[7.314783],[-9.747841],[-7.678052],[9.555667],[-3.829839],[-1.302907],[1.415115],[5.051012],[8.796125],[-1.265783],[2.087035],[-0.217421],[-7.509405],[-7.227655],[1.237088],[-7.226257],[2.290985],[9.658606],[-8.226338],[5.984407],[-1.527945],[5.948427],[-6.045451],[-7.318777],[-8.270222],[8.559257],[3.022686],[-6.405611],[-1.884153],[-6.543221],[0.480879],[-5.022158],[4.364977],[0.022964],[-1.583624],[2.810576],[-1.834388],[4.187371],[4.705044],[-5.605854],[-3.549292],[9.980190],[4.004880],[9.967724],[-5.974654],[6.474607],[-9.717590],[-0.818121],[2.997300],[8.843160],[1.521007],[-7.932015],[-4.179971],[-0.080831],[5.810506],[5.431610],[-7.994234],[7.862206],[8.499946],[7.854921],[-2.521103],[7.554920],[6.843691],[3.044329],[4.745706],[-0.974263],[9.187148],[-4.261676],[-3.287048],[2.456573],[8.651612],[8.053049],[3.679797],[4.509578],[-5.579531],[7.942373],[8.430875],[4.371065],[-6.544844],[5.269263],[-3.174679],[-2.382959],[-4.122545],[7.199302],[0.497617],[-1.885807],[3.021640],[-1.508723],[-6.319556],[8.752629],[5.815950],[-6.987626],[-2.195457],[3.064807],[-9.125187],[-6.419262],[-8.239681],[-4.729859],[-1.023351],[-9.045152],[-0.289010],[-6.697790],[-1.419432],[-4.880748],[2.452119],[6.246308],[-4.594843],[8.136147],[-0.286452],[-4.044032],[-2.836683],[2.921895],[9.125820],[3.361021],[7.698801],[-4.530695],[7.054048],[4.553110],[1.244754],[-5.752285],[-3.817927],[6.259413],[9.668606],[2.038794],[7.811423],[-6.950720],[-7.486513],[7.994442],[1.404349],[4.396182],[-8.663592],[-5.542866],[1.395762],[2.123988],[-5.060195],[2.827304],[-0.926703],[7.983891],[4.409300],[5.498003],[-1.249663],[-0.810053],[4.749664],[8.785871],[0.346574],[5.252760],[-7.036670],[0.171934],[5.713825],[-2.612091],[-1.012629],[-9.677579],[9.992492],[6.783498],[-6.935143],[5.438023],[-4.024555],[-5.467131],[2.450405],[8.895562],[-7.816268],[-0.866159],[-7.738275],[-3.140987],[9.344557],[3.653731],[-3.989807],[-0.412913],[-5.433553],[0.585730],[-6.619782],[3.507920],[-4.979061],[-2.560981],[1.221042],[-4.764213],[-5.453399],[-8.907715],[-8.947721],[-0.036712],[-2.215739],[-9.168378],[-9.310717],[-6.595747],[-4.962080],[1.114067],[-1.526514],[8.596975],[-0.415704],[3.736974],[6.831971],[-5.614915],[-0.604982],[4.611624],[7.887027],[-0.278664],[8.669268],[7.341778],[5.789651],[-2.704940],[3.473512],[-0.591030],[2.824043],[-1.712021],[8.387618],[7.466060],[-8.236512],[-1.163517],[2.774958],[2.616101],[-2.376552],[-0.931673],[-5.983746],[9.100280],[0.960041],[4.723050],[4.000267],[-6.842301],[-0.030014],[9.647057],[-5.010892],[-4.359415],[-4.672353],[-0.823774],[-9.992794],[-7.448045],[5.154763],[5.763242],[-3.853207],[-9.228449],[-6.215133],[-6.248212],[4.399313],[-5.494649],[-6.705950],[-8.339603],[4.058731],[3.184693],[3.057842],[4.281701],[1.745589],[-0.962079],[-1.014513],[7.782666],[-7.414041],[-4.114252],[7.001345],[3.207318],[7.213854],[-7.778463],[6.842282],[2.703249],[-8.463964],[-9.313857],[-9.074874],[4.750110],[6.739852],[-3.567122],[1.249085],[8.715593],[4.919448],[8.500771],[-0.917421],[-4.594823],[-5.304631],[3.596012],[5.574389],[-3.158999],[1.578843],[0.504733],[-9.557096],[-6.222400],[1.612539],[5.235837],[-9.627495],[-2.238359],[-6.056738],[-8.470425],[-8.633162],[3.331825],[-0.729186],[-2.466141],[2.645104],[9.699682],[1.753861],[-2.227557],[4.233726],[-9.826455],[3.436617],[-3.486477],[-2.266369],[-7.264862],[-8.430528],[0.514766],[7.436566],[1.196255],[-9.925715],[8.478600],[6.633394],[-8.680887],[5.720881],[-7.208584],[8.733352],[3.154378],[5.665399],[-0.185266],[1.513976],[-2.031968],[-7.395845],[-8.041117],[-5.394730],[8.284525],[-2.690461],[-6.794626],[5.500434],[-2.044543],[4.486833],[3.980444],[1.487528],[-5.470602],[-3.858041],[-9.507457],[8.532336],[8.981577],[9.944144],[8.494855],[-3.589389],[-3.791558],[7.881473],[-9.773796],[7.751181],[4.986871],[6.124725],[-6.292152],[-9.979772]], dtype = "float32")#candidate|9402|(1040, 1)|const|float32
const_9403 = relay.const([-0.893679,3.949138,-5.402252,1.245853,-8.321897,-0.334652,-8.585587,-0.433588,-1.166618,-4.820123,-0.204457,3.395348,-7.169940,1.858962,-9.600718,-2.508232,3.390400,6.705805,-4.515699,1.976766,-6.118288,6.812450,2.682460,2.825869,3.939705,-5.484418,2.541875,-8.464203,3.274855,-8.429269,9.906834,-1.641771,-5.417496,-5.465273,-7.857371,4.950214,-3.973635,-1.038806,-4.380286,0.868533,8.366925,-5.342520,5.268817,-3.032572,-4.423292,8.380188,6.747030,3.791883,3.137528,-7.833097,7.594277,-7.213543,-3.684678,-3.044024,-9.488411,3.195821,0.338885,-9.996408,-3.749174,4.735054,9.912906,-3.307430,-1.109761,-8.630585,-3.379815,9.051403,7.627103,4.230549,-8.797144,-9.111172,8.064599,-3.855320,6.867504,-9.495287,-7.128022,2.533134,-0.850658,-9.036128,1.453160,-7.999886,-4.106723,3.554394,6.695946,3.013058,-9.121929,-4.017945,6.488509,-8.346107,9.204055,0.423116,-5.114457,-7.230942,-0.484487,2.180505,0.806551,4.510458,-9.264435,4.266986,1.295425,8.469758,5.722014,-8.494863,5.297412,5.986993,0.950942,-7.702897,0.038052,-9.832410,0.361135,8.212296,4.066357,-7.887347,-8.160467,4.135728,6.987884,7.375203,-8.155337,3.568458,0.202764,-4.496255,7.623329,-7.171238,7.141384,5.818022,7.584089,-2.841075,8.495483,-3.002850,-5.703152,-1.907481,-0.755733,-5.779368,3.770064,-8.426465,3.045348,7.603214,4.324741,9.706577,-0.769496,-0.190005,-6.231645,-7.953934,5.473376,1.239446,-6.673805,9.500971,0.868446,7.625350,-5.434560,7.933829,-4.186268,-9.389722,2.444605,4.462520,-5.320113,8.918837,-9.042638,2.315698,-5.246404,2.144685,-4.795645,3.260286,4.620825,-6.452461,6.349682,0.170098,-1.643161,5.599959,1.947336,8.877190,-5.074229,-4.404101,-7.128129,9.792755,-0.377327,3.694580,8.513933,9.822606,9.953966,-8.876845,3.095411,-1.133434,-4.817862,1.242809,-7.894713,1.222706,9.512455,5.386132,5.229980,-9.124835,-4.843003,-8.829662,2.052675,-0.995618,5.661308,4.926412,-8.842872,-7.679626,1.918555,-8.763262,-1.787821,5.411136,-8.811227,0.089539,7.116269,8.680417,6.348413,3.043861,0.396014,8.185033,4.771208,-2.683680,2.391093,-6.476505,-9.832205,-1.862358,-2.905037,7.709396,6.290628,9.722219,-6.445674,-1.790586,-8.052214,-3.051118,6.906895,6.503847,-8.494579,-1.124243,-9.797870,7.033887,3.309267,-9.781202,6.868245,-5.775749,-1.299691,5.521189,6.589430,3.226952,1.812764,6.260118,0.219632,0.969923,-7.565573,8.981998,-6.113412,-6.980987,5.214009,-0.225679,-6.480190,6.560577,-0.430942,8.379904,-1.150866,6.496146,8.452301,-9.648161,7.803322,-7.389821,8.221484,2.433403,-0.568861,2.291073,-6.227258,-0.737015,9.691678,8.877629,-1.368731,4.573174,4.092978,4.570469,7.428751,-7.219416,8.209440,5.624673,-0.313585,6.724505,-6.727017,-5.150740,-8.625635,6.011381,-3.211199,6.160158,1.288843,5.503685,5.502335,1.555929,-8.014917,-8.329067,4.286740,-0.014774,-0.559755,-4.370598,4.680009,9.539136,-2.398434,1.342761,4.304316,1.887400,0.785328,-0.280293,3.560959,8.593868,5.073799,-5.745979,1.860346,-4.388750,-8.485091,-7.235349,-7.614670,0.891297,-8.992350,9.374487,9.218003,6.640554,-5.571205,1.195820,3.462723,4.703797,-5.050665,9.817205,8.328164,6.102032,9.905943,9.583730,7.067376,-7.188998,8.869814,-2.718946,-6.635427,1.855622,3.531754,0.146172,6.206860,7.522954,-4.638384,-4.945678,-3.574915,8.062179,0.001182,4.292879,0.211900,8.728953,-5.481832,1.344206,8.819088,9.378589,4.046939,2.176716,9.390794,2.704353,-6.679183,8.266004,2.304895,-7.746500,1.183303,-6.963442,4.205708,1.855084,4.001571,-3.616543,6.420861,2.119310,-5.904160,-2.294560,9.672517,5.279074,5.144722,-1.443537,2.190664,7.375749,3.939677,4.146636,6.102423,-4.452663,4.796965,5.915537,-3.772850,-4.974333,-2.321019,-8.271439,-1.310853,0.331629,6.664724,-2.806632,-0.967262,7.368259,9.488163,-4.315440,-6.065415,3.461424,1.414946,-5.071166,8.021356,4.989721,3.031679,8.351717,6.683007,9.830336,7.195830,-3.093798,-8.423760,1.733485,-0.166118,-1.426063,-5.311414,4.209275,2.299805,0.561822,-9.891250,-6.205931,-0.583819,7.995909,-7.721368,-8.419785,-4.826031,0.549295,7.193047,6.808762,-8.458025,-2.974707,7.144318,-4.760865,2.001598,-6.206542,-4.136476,-4.710618,-5.568440,3.224829,-5.185329,-4.019918,-7.559714,8.042962,-7.543205,5.494285,5.618405,1.558060,7.385954,3.124893,7.113395,-4.120621,-3.013892,1.842215,-0.925648,6.469842,-1.331788,-7.020791,8.330654,-7.332933,-9.366198,-2.791196,4.115383,-1.570410,0.290148,-6.131917,5.580494,1.410607,3.464141,2.414012,3.335192,-6.469215,-9.294476,-0.936762], dtype = "float32")#candidate|9403|(462,)|const|float32
const_9404 = relay.const([10,6,7,-6,-7,-2,-5,-8,-3,1,-5,9,4,7,8,-6,-3,6,2,-10,10,-9,-6,-3,-4,-8,9,-7,9,8,-9,6,9,-1,-5,1,2,10,9,-6,8,-1,3,-9,-1,10,3,1,9,2,-2,7,5,1,-1,-6,-5,7,5,10,4,6,-7,7,9,-10,-4,-3,6,-4,5,5,7,7,7,9,-1,-9,2,-6,7,9,5,-2,-10,-10,-8,-4,-9,8,2,9,2,4,4,-4,6,-2,-9,-5,-5,-3,-10,-8,10,6,3,7,-1,-1,1,-6,3,1,6,-9,9,-2,1,-7,-7,-4,6,8,-4,-4,8,-3,10,1,10,-5,-1,7,6,-4,-8,-3,-2,4,2,3,10,1,10,3,1,8,-4,6,10,3,8,2,9,-8,-6,2,-6,3,4,-5,-4,7,-7,-10,-4,-5,-10,-4,5,-3,2,-4,-8,-4,4,7,2,8,8,-8,-2,7,-10,-3,3,-5,-3,5,9,-4,-9,-3,-7,-2,-8,9,3,-3,7,1,4,-8,6,-8,1,8,-5,2,-1,-8,5,10,-5,5,1,-5,2,9,5,3,-9,7,-3,5,5,4,3,10,-8,-4,-10,3,-2,-10,-2,-4,-5,5,2,-1,-5,7,-2,10,3,-9,2,-7,-6,3,1,9,10,5,5,-9,2,10,6,-3,3,3,6,10,-6,-10,-10,-4], dtype = "int64")#candidate|9404|(270,)|const|int64
var_9405 = relay.var("var_9405", dtype = "float64", shape = (13, 4))#candidate|9405|(13, 4)|var|float64
call_9401 = relay.TupleGetItem(func_5363_call(relay.reshape(const_9402.astype('float32'), [5, 16, 13]), relay.reshape(const_9403.astype('float32'), [462,]), relay.reshape(const_9404.astype('int64'), [270,]), relay.reshape(var_9405.astype('float64'), [52, 1]), ), 6)
call_9406 = relay.TupleGetItem(func_5369_call(relay.reshape(const_9402.astype('float32'), [5, 16, 13]), relay.reshape(const_9403.astype('float32'), [462,]), relay.reshape(const_9404.astype('int64'), [270,]), relay.reshape(var_9405.astype('float64'), [52, 1]), ), 6)
func_3568_call = mod.get_global_var('func_3568')
func_3569_call = mutated_mod.get_global_var('func_3569')
call_9407 = relay.TupleGetItem(func_3568_call(), 0)
call_9408 = relay.TupleGetItem(func_3569_call(), 0)
func_4372_call = mod.get_global_var('func_4372')
func_4374_call = mutated_mod.get_global_var('func_4374')
call_9410 = func_4372_call(relay.reshape(call_9396.astype('int8'), [8, 14, 2]))
call_9411 = func_4372_call(relay.reshape(call_9396.astype('int8'), [8, 14, 2]))
func_8690_call = mod.get_global_var('func_8690')
func_8692_call = mutated_mod.get_global_var('func_8692')
call_9412 = relay.TupleGetItem(func_8690_call(), 0)
call_9413 = relay.TupleGetItem(func_8692_call(), 0)
output = relay.Tuple([call_9387,call_9396,call_9401,const_9402,const_9403,const_9404,var_9405,call_9407,call_9410,call_9412,])
output2 = relay.Tuple([call_9388,call_9397,call_9406,const_9402,const_9403,const_9404,var_9405,call_9408,call_9411,call_9413,])
func_9414 = relay.Function([var_9405,], output)
mod['func_9414'] = func_9414
mod = relay.transform.InferType()(mod)
var_9415 = relay.var("var_9415", dtype = "float64", shape = (13, 4))#candidate|9415|(13, 4)|var|float64
output = func_9414(var_9415)
func_9416 = relay.Function([var_9415], output)
mutated_mod['func_9416'] = func_9416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6021_call = mod.get_global_var('func_6021')
func_6022_call = mutated_mod.get_global_var('func_6022')
call_9447 = relay.TupleGetItem(func_6021_call(), 0)
call_9448 = relay.TupleGetItem(func_6022_call(), 0)
output = call_9447
output2 = call_9448
func_9449 = relay.Function([], output)
mod['func_9449'] = func_9449
mod = relay.transform.InferType()(mod)
output = func_9449()
func_9450 = relay.Function([], output)
mutated_mod['func_9450'] = func_9450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3840_call = mod.get_global_var('func_3840')
func_3841_call = mutated_mod.get_global_var('func_3841')
call_9459 = relay.TupleGetItem(func_3840_call(), 0)
call_9460 = relay.TupleGetItem(func_3841_call(), 0)
func_4188_call = mod.get_global_var('func_4188')
func_4191_call = mutated_mod.get_global_var('func_4191')
var_9481 = relay.var("var_9481", dtype = "uint16", shape = (616,))#candidate|9481|(616,)|var|uint16
call_9480 = func_4188_call(relay.reshape(var_9481.astype('uint16'), [11, 4, 14]))
call_9482 = func_4188_call(relay.reshape(var_9481.astype('uint16'), [11, 4, 14]))
func_5760_call = mod.get_global_var('func_5760')
func_5762_call = mutated_mod.get_global_var('func_5762')
call_9487 = relay.TupleGetItem(func_5760_call(), 0)
call_9488 = relay.TupleGetItem(func_5762_call(), 0)
func_3333_call = mod.get_global_var('func_3333')
func_3335_call = mutated_mod.get_global_var('func_3335')
call_9489 = relay.TupleGetItem(func_3333_call(), 2)
call_9490 = relay.TupleGetItem(func_3335_call(), 2)
output = relay.Tuple([call_9459,call_9480,var_9481,call_9487,call_9489,])
output2 = relay.Tuple([call_9460,call_9482,var_9481,call_9488,call_9490,])
func_9518 = relay.Function([var_9481,], output)
mod['func_9518'] = func_9518
mod = relay.transform.InferType()(mod)
mutated_mod['func_9518'] = func_9518
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9519 = relay.var("var_9519", dtype = "uint16", shape = (616,))#candidate|9519|(616,)|var|uint16
func_9518_call = mutated_mod.get_global_var('func_9518')
call_9520 = func_9518_call(var_9519)
output = call_9520
func_9521 = relay.Function([var_9519], output)
mutated_mod['func_9521'] = func_9521
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3661_call = mod.get_global_var('func_3661')
func_3662_call = mutated_mod.get_global_var('func_3662')
call_9566 = relay.TupleGetItem(func_3661_call(), 1)
call_9567 = relay.TupleGetItem(func_3662_call(), 1)
output = relay.Tuple([call_9566,])
output2 = relay.Tuple([call_9567,])
func_9603 = relay.Function([], output)
mod['func_9603'] = func_9603
mod = relay.transform.InferType()(mod)
mutated_mod['func_9603'] = func_9603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9603_call = mutated_mod.get_global_var('func_9603')
call_9604 = func_9603_call()
output = call_9604
func_9605 = relay.Function([], output)
mutated_mod['func_9605'] = func_9605
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9610 = relay.var("var_9610", dtype = "float64", shape = (2, 14, 14))#candidate|9610|(2, 14, 14)|var|float64
uop_9611 = relay.log(var_9610.astype('float64')) # shape=(2, 14, 14)
output = relay.Tuple([uop_9611,])
output2 = relay.Tuple([uop_9611,])
func_9621 = relay.Function([var_9610,], output)
mod['func_9621'] = func_9621
mod = relay.transform.InferType()(mod)
var_9622 = relay.var("var_9622", dtype = "float64", shape = (2, 14, 14))#candidate|9622|(2, 14, 14)|var|float64
output = func_9621(var_9622)
func_9623 = relay.Function([var_9622], output)
mutated_mod['func_9623'] = func_9623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7837_call = mod.get_global_var('func_7837')
func_7839_call = mutated_mod.get_global_var('func_7839')
call_9664 = relay.TupleGetItem(func_7837_call(), 0)
call_9665 = relay.TupleGetItem(func_7839_call(), 0)
func_789_call = mod.get_global_var('func_789')
func_791_call = mutated_mod.get_global_var('func_791')
var_9679 = relay.var("var_9679", dtype = "float32", shape = (105,))#candidate|9679|(105,)|var|float32
call_9678 = relay.TupleGetItem(func_789_call(relay.reshape(var_9679.astype('float32'), [3, 7, 5])), 0)
call_9680 = relay.TupleGetItem(func_791_call(relay.reshape(var_9679.astype('float32'), [3, 7, 5])), 0)
func_4557_call = mod.get_global_var('func_4557')
func_4559_call = mutated_mod.get_global_var('func_4559')
call_9681 = relay.TupleGetItem(func_4557_call(), 0)
call_9682 = relay.TupleGetItem(func_4559_call(), 0)
func_9449_call = mod.get_global_var('func_9449')
func_9450_call = mutated_mod.get_global_var('func_9450')
call_9686 = func_9449_call()
call_9687 = func_9449_call()
func_8172_call = mod.get_global_var('func_8172')
func_8173_call = mutated_mod.get_global_var('func_8173')
call_9689 = relay.TupleGetItem(func_8172_call(), 0)
call_9690 = relay.TupleGetItem(func_8173_call(), 0)
output = relay.Tuple([call_9664,call_9678,var_9679,call_9681,call_9686,call_9689,])
output2 = relay.Tuple([call_9665,call_9680,var_9679,call_9682,call_9687,call_9690,])
func_9693 = relay.Function([var_9679,], output)
mod['func_9693'] = func_9693
mod = relay.transform.InferType()(mod)
var_9694 = relay.var("var_9694", dtype = "float32", shape = (105,))#candidate|9694|(105,)|var|float32
output = func_9693(var_9694)
func_9695 = relay.Function([var_9694], output)
mutated_mod['func_9695'] = func_9695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2464_call = mod.get_global_var('func_2464')
func_2465_call = mutated_mod.get_global_var('func_2465')
call_9715 = func_2464_call()
call_9716 = func_2464_call()
func_7691_call = mod.get_global_var('func_7691')
func_7693_call = mutated_mod.get_global_var('func_7693')
call_9735 = relay.TupleGetItem(func_7691_call(), 0)
call_9736 = relay.TupleGetItem(func_7693_call(), 0)
output = relay.Tuple([call_9715,call_9735,])
output2 = relay.Tuple([call_9716,call_9736,])
func_9737 = relay.Function([], output)
mod['func_9737'] = func_9737
mod = relay.transform.InferType()(mod)
output = func_9737()
func_9738 = relay.Function([], output)
mutated_mod['func_9738'] = func_9738
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1462_call = mod.get_global_var('func_1462')
func_1463_call = mutated_mod.get_global_var('func_1463')
call_9787 = func_1462_call()
call_9788 = func_1462_call()
func_4074_call = mod.get_global_var('func_4074')
func_4077_call = mutated_mod.get_global_var('func_4077')
var_9790 = relay.var("var_9790", dtype = "float32", shape = (105,))#candidate|9790|(105,)|var|float32
call_9789 = relay.TupleGetItem(func_4074_call(relay.reshape(var_9790.astype('float32'), [105, 1]), relay.reshape(var_9790.astype('float32'), [105, 1]), ), 1)
call_9791 = relay.TupleGetItem(func_4077_call(relay.reshape(var_9790.astype('float32'), [105, 1]), relay.reshape(var_9790.astype('float32'), [105, 1]), ), 1)
output = relay.Tuple([call_9787,call_9789,var_9790,])
output2 = relay.Tuple([call_9788,call_9791,var_9790,])
func_9794 = relay.Function([var_9790,], output)
mod['func_9794'] = func_9794
mod = relay.transform.InferType()(mod)
var_9795 = relay.var("var_9795", dtype = "float32", shape = (105,))#candidate|9795|(105,)|var|float32
output = func_9794(var_9795)
func_9796 = relay.Function([var_9795], output)
mutated_mod['func_9796'] = func_9796
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5870_call = mod.get_global_var('func_5870')
func_5871_call = mutated_mod.get_global_var('func_5871')
call_9820 = relay.TupleGetItem(func_5870_call(), 3)
call_9821 = relay.TupleGetItem(func_5871_call(), 3)
output = call_9820
output2 = call_9821
func_9823 = relay.Function([], output)
mod['func_9823'] = func_9823
mod = relay.transform.InferType()(mod)
output = func_9823()
func_9824 = relay.Function([], output)
mutated_mod['func_9824'] = func_9824
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9854 = relay.var("var_9854", dtype = "float32", shape = (15, 7, 16))#candidate|9854|(15, 7, 16)|var|float32
uop_9855 = relay.atanh(var_9854.astype('float32')) # shape=(15, 7, 16)
uop_9864 = relay.tan(uop_9855.astype('float32')) # shape=(15, 7, 16)
uop_9867 = relay.log10(uop_9864.astype('float64')) # shape=(15, 7, 16)
func_5547_call = mod.get_global_var('func_5547')
func_5549_call = mutated_mod.get_global_var('func_5549')
call_9869 = relay.TupleGetItem(func_5547_call(), 0)
call_9870 = relay.TupleGetItem(func_5549_call(), 0)
func_3508_call = mod.get_global_var('func_3508')
func_3513_call = mutated_mod.get_global_var('func_3513')
var_9876 = relay.var("var_9876", dtype = "uint32", shape = (182,))#candidate|9876|(182,)|var|uint32
var_9877 = relay.var("var_9877", dtype = "uint32", shape = (1638,))#candidate|9877|(1638,)|var|uint32
const_9878 = relay.const([True,True,True,True,True,False,True,True,False,True,False,True,True,False,False,True,True,True,True,True,True,True,True,True,False,True,True,False,True,True,True,False,False,False,True,False,False,False,True,False,False,True,True,True,False,True,False,True,True,True,True,False], dtype = "bool")#candidate|9878|(52,)|const|bool
call_9875 = relay.TupleGetItem(func_3508_call(relay.reshape(var_9876.astype('uint32'), [13, 14, 1]), relay.reshape(var_9876.astype('uint32'), [13, 14, 1]), relay.reshape(var_9877.astype('uint32'), [13, 14, 9]), relay.reshape(const_9878.astype('bool'), [52,]), ), 4)
call_9879 = relay.TupleGetItem(func_3513_call(relay.reshape(var_9876.astype('uint32'), [13, 14, 1]), relay.reshape(var_9876.astype('uint32'), [13, 14, 1]), relay.reshape(var_9877.astype('uint32'), [13, 14, 9]), relay.reshape(const_9878.astype('bool'), [52,]), ), 4)
output = relay.Tuple([uop_9867,call_9869,call_9875,var_9876,var_9877,const_9878,])
output2 = relay.Tuple([uop_9867,call_9870,call_9879,var_9876,var_9877,const_9878,])
func_9909 = relay.Function([var_9854,var_9876,var_9877,], output)
mod['func_9909'] = func_9909
mod = relay.transform.InferType()(mod)
mutated_mod['func_9909'] = func_9909
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9909_call = mutated_mod.get_global_var('func_9909')
var_9911 = relay.var("var_9911", dtype = "float32", shape = (15, 7, 16))#candidate|9911|(15, 7, 16)|var|float32
var_9912 = relay.var("var_9912", dtype = "uint32", shape = (182,))#candidate|9912|(182,)|var|uint32
var_9913 = relay.var("var_9913", dtype = "uint32", shape = (1638,))#candidate|9913|(1638,)|var|uint32
call_9910 = func_9909_call(var_9911,var_9912,var_9913,)
output = call_9910
func_9914 = relay.Function([var_9911,var_9912,var_9913,], output)
mutated_mod['func_9914'] = func_9914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3661_call = mod.get_global_var('func_3661')
func_3662_call = mutated_mod.get_global_var('func_3662')
call_9923 = relay.TupleGetItem(func_3661_call(), 2)
call_9924 = relay.TupleGetItem(func_3662_call(), 2)
func_8105_call = mod.get_global_var('func_8105')
func_8106_call = mutated_mod.get_global_var('func_8106')
call_9928 = relay.TupleGetItem(func_8105_call(), 1)
call_9929 = relay.TupleGetItem(func_8106_call(), 1)
output = relay.Tuple([call_9923,call_9928,])
output2 = relay.Tuple([call_9924,call_9929,])
func_9936 = relay.Function([], output)
mod['func_9936'] = func_9936
mod = relay.transform.InferType()(mod)
output = func_9936()
func_9937 = relay.Function([], output)
mutated_mod['func_9937'] = func_9937
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5547_call = mod.get_global_var('func_5547')
func_5549_call = mutated_mod.get_global_var('func_5549')
call_9948 = relay.TupleGetItem(func_5547_call(), 2)
call_9949 = relay.TupleGetItem(func_5549_call(), 2)
output = relay.Tuple([call_9948,])
output2 = relay.Tuple([call_9949,])
func_9973 = relay.Function([], output)
mod['func_9973'] = func_9973
mod = relay.transform.InferType()(mod)
mutated_mod['func_9973'] = func_9973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9973_call = mutated_mod.get_global_var('func_9973')
call_9974 = func_9973_call()
output = call_9974
func_9975 = relay.Function([], output)
mutated_mod['func_9975'] = func_9975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2984_call = mod.get_global_var('func_2984')
func_2986_call = mutated_mod.get_global_var('func_2986')
call_10016 = func_2984_call()
call_10017 = func_2984_call()
func_6286_call = mod.get_global_var('func_6286')
func_6288_call = mutated_mod.get_global_var('func_6288')
call_10030 = func_6286_call()
call_10031 = func_6286_call()
output = relay.Tuple([call_10016,call_10030,])
output2 = relay.Tuple([call_10017,call_10031,])
func_10036 = relay.Function([], output)
mod['func_10036'] = func_10036
mod = relay.transform.InferType()(mod)
output = func_10036()
func_10037 = relay.Function([], output)
mutated_mod['func_10037'] = func_10037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8639_call = mod.get_global_var('func_8639')
func_8640_call = mutated_mod.get_global_var('func_8640')
call_10066 = func_8639_call()
call_10067 = func_8639_call()
func_2582_call = mod.get_global_var('func_2582')
func_2584_call = mutated_mod.get_global_var('func_2584')
call_10068 = relay.TupleGetItem(func_2582_call(), 0)
call_10069 = relay.TupleGetItem(func_2584_call(), 0)
output = relay.Tuple([call_10066,call_10068,])
output2 = relay.Tuple([call_10067,call_10069,])
func_10072 = relay.Function([], output)
mod['func_10072'] = func_10072
mod = relay.transform.InferType()(mod)
mutated_mod['func_10072'] = func_10072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10072_call = mutated_mod.get_global_var('func_10072')
call_10073 = func_10072_call()
output = call_10073
func_10074 = relay.Function([], output)
mutated_mod['func_10074'] = func_10074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7837_call = mod.get_global_var('func_7837')
func_7839_call = mutated_mod.get_global_var('func_7839')
call_10078 = relay.TupleGetItem(func_7837_call(), 0)
call_10079 = relay.TupleGetItem(func_7839_call(), 0)
func_7343_call = mod.get_global_var('func_7343')
func_7345_call = mutated_mod.get_global_var('func_7345')
call_10082 = relay.TupleGetItem(func_7343_call(), 0)
call_10083 = relay.TupleGetItem(func_7345_call(), 0)
output = relay.Tuple([call_10078,call_10082,])
output2 = relay.Tuple([call_10079,call_10083,])
func_10092 = relay.Function([], output)
mod['func_10092'] = func_10092
mod = relay.transform.InferType()(mod)
mutated_mod['func_10092'] = func_10092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10092_call = mutated_mod.get_global_var('func_10092')
call_10093 = func_10092_call()
output = call_10093
func_10094 = relay.Function([], output)
mutated_mod['func_10094'] = func_10094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9737_call = mod.get_global_var('func_9737')
func_9738_call = mutated_mod.get_global_var('func_9738')
call_10124 = relay.TupleGetItem(func_9737_call(), 1)
call_10125 = relay.TupleGetItem(func_9738_call(), 1)
func_6286_call = mod.get_global_var('func_6286')
func_6288_call = mutated_mod.get_global_var('func_6288')
call_10130 = func_6286_call()
call_10131 = func_6286_call()
func_7691_call = mod.get_global_var('func_7691')
func_7693_call = mutated_mod.get_global_var('func_7693')
call_10150 = relay.TupleGetItem(func_7691_call(), 0)
call_10151 = relay.TupleGetItem(func_7693_call(), 0)
output = relay.Tuple([call_10124,call_10130,call_10150,])
output2 = relay.Tuple([call_10125,call_10131,call_10151,])
func_10165 = relay.Function([], output)
mod['func_10165'] = func_10165
mod = relay.transform.InferType()(mod)
mutated_mod['func_10165'] = func_10165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10165_call = mutated_mod.get_global_var('func_10165')
call_10166 = func_10165_call()
output = call_10166
func_10167 = relay.Function([], output)
mutated_mod['func_10167'] = func_10167
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10210 = relay.const([[[-8.683680,4.275729,-5.154059,1.094655,0.336594,4.045892,-7.087687],[-1.875850,7.341068,0.597611,-0.384676,-1.467163,-5.834923,3.702099],[-4.945398,-5.391321,3.345509,4.049752,2.674729,-5.279191,8.147396],[-5.423678,7.979133,-2.558731,-3.698778,4.968013,0.291243,-7.665267],[-4.218615,1.681588,-7.740763,8.101377,8.825293,-2.161564,-1.019320],[-6.815885,-0.341875,4.959693,8.756407,-3.712207,1.295007,-7.864464],[4.553379,-6.081439,-7.441411,-3.317457,-1.780866,-6.554253,-4.036951],[-5.982744,6.523732,5.792622,9.619554,-8.362173,-8.994993,-3.371845],[-0.723391,-0.057277,4.721511,4.873234,-1.709097,8.180962,-8.311801]],[[1.275869,-2.785351,5.034439,-6.249970,2.629792,7.612429,-5.775386],[2.289146,5.309390,-9.084985,2.806851,8.162658,7.774887,0.818042],[-9.032872,8.248334,-3.013017,3.349722,0.341241,-0.301350,8.977067],[-7.191919,0.492678,-7.727897,-5.277091,-7.694436,-5.248903,-1.987718],[-6.029528,-0.765646,4.762369,-2.530610,7.856531,5.412159,3.884763],[-0.711409,8.572156,-8.707224,-5.243455,-1.821323,1.917703,-6.559763],[-4.633184,-4.781511,-5.413671,9.509871,-5.566215,-2.565537,4.797013],[-9.782564,0.671826,9.881392,-9.747765,-0.745402,-2.107850,9.002258],[8.238488,8.386799,-5.556507,-1.688063,6.688374,5.695327,2.650004]],[[3.615199,4.296456,6.888880,-5.848685,-8.990123,6.596971,3.756488],[1.242823,1.805254,2.242873,-9.606170,-2.162246,-8.479483,-0.650983],[9.331312,3.649401,-5.812007,5.435404,-4.193699,-1.754617,-7.897063],[5.317426,0.215557,-0.626155,1.624193,7.526744,9.901226,4.816835],[0.858251,4.449621,3.759495,-5.791481,-8.669457,-3.787849,5.376763],[1.110494,-8.942710,-4.371736,5.304090,-8.463186,-8.908970,-2.905097],[-0.836286,0.445504,3.214347,-5.527044,-8.396082,-5.641076,-7.517484],[5.213294,9.543699,3.303717,5.164834,3.362277,-2.216930,4.304282],[0.694837,7.237159,2.495407,-6.841452,4.655057,-3.069181,0.356188]],[[-7.732893,5.259884,6.176360,-0.487656,-3.293729,-9.081128,-9.889783],[9.664380,5.043136,3.352371,-3.179439,-9.153983,3.647746,-8.321705],[0.812109,-1.871888,3.083367,1.380673,-8.085178,-7.731836,4.535216],[-7.038775,0.831535,2.417157,3.140158,4.946132,-0.667265,-9.948344],[-0.471529,5.177171,-4.352013,8.936561,9.719390,-0.343244,8.003511],[-6.384062,-0.170136,-1.934860,-9.117070,-0.656330,0.702413,-6.661408],[3.347959,8.255345,6.235616,1.817674,6.127410,4.798370,6.989444],[-8.815906,-3.070538,1.425151,-9.206904,7.837927,-0.083841,-1.156026],[8.852635,0.147548,7.286918,-8.517760,4.411752,-9.064922,9.317898]],[[9.827872,0.880904,2.649997,-3.428021,-5.552261,-9.570664,0.210914],[-6.726465,-1.162949,-4.196966,-3.337335,1.129654,-7.395740,1.858535],[4.701450,2.221562,2.383826,-0.960654,-5.786135,-4.311839,4.386361],[-5.210491,0.170887,-3.267642,8.777727,9.649528,-3.187436,-0.038780],[5.152024,0.552599,-7.966542,2.703706,-8.017387,-3.826134,-5.769463],[1.807236,-1.774904,-9.161756,-9.486101,3.054877,-1.971187,-1.847577],[3.525015,3.536277,-7.119780,2.036751,8.830580,-5.932360,7.308605],[6.652204,2.477620,8.711859,-3.765733,6.718060,1.227589,-5.898575],[6.755416,-3.452543,-0.848987,1.431132,9.920016,1.106862,3.587481]]], dtype = "float64")#candidate|10210|(5, 9, 7)|const|float64
uop_10211 = relay.log10(const_10210.astype('float64')) # shape=(5, 9, 7)
output = relay.Tuple([uop_10211,])
output2 = relay.Tuple([uop_10211,])
func_10213 = relay.Function([], output)
mod['func_10213'] = func_10213
mod = relay.transform.InferType()(mod)
output = func_10213()
func_10214 = relay.Function([], output)
mutated_mod['func_10214'] = func_10214
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10215 = relay.var("var_10215", dtype = "float32", shape = (8, 1, 5))#candidate|10215|(8, 1, 5)|var|float32
uop_10216 = relay.log2(var_10215.astype('float32')) # shape=(8, 1, 5)
var_10223 = relay.var("var_10223", dtype = "float32", shape = (8, 1, 5))#candidate|10223|(8, 1, 5)|var|float32
bop_10224 = relay.greater_equal(var_10215.astype('bool'), relay.reshape(var_10223.astype('bool'), relay.shape_of(var_10215))) # shape=(8, 1, 5)
output = relay.Tuple([uop_10216,bop_10224,])
output2 = relay.Tuple([uop_10216,bop_10224,])
F = relay.Function([var_10215,var_10223,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_10215,var_10223,], output2)
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
