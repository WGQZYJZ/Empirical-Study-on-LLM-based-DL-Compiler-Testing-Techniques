import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_230 = relay.const(-2, dtype = "int8")#candidate|230|()|const|int8
var_231 = relay.var("var_231", dtype = "int8", shape = (4, 6, 11))#candidate|231|(4, 6, 11)|var|int8
bop_232 = relay.bitwise_or(const_230.astype('int8'), var_231.astype('int8')) # shape=(4, 6, 11)
output = relay.Tuple([bop_232,])
output2 = relay.Tuple([bop_232,])
func_244 = relay.Function([var_231,], output)
mod['func_244'] = func_244
mod = relay.transform.InferType()(mod)
var_245 = relay.var("var_245", dtype = "int8", shape = (4, 6, 11))#candidate|245|(4, 6, 11)|var|int8
output = func_244(var_245)
func_246 = relay.Function([var_245], output)
mutated_mod['func_246'] = func_246
mutated_mod = relay.transform.InferType()(mutated_mod)
var_380 = relay.var("var_380", dtype = "int32", shape = ())#candidate|380|()|var|int32
var_381 = relay.var("var_381", dtype = "int32", shape = (7, 9, 10))#candidate|381|(7, 9, 10)|var|int32
bop_382 = relay.less(var_380.astype('bool'), var_381.astype('bool')) # shape=(7, 9, 10)
bop_388 = relay.maximum(var_381.astype('uint8'), var_380.astype('uint8')) # shape=(7, 9, 10)
func_244_call = mod.get_global_var('func_244')
func_246_call = mutated_mod.get_global_var('func_246')
var_399 = relay.var("var_399", dtype = "int8", shape = (264,))#candidate|399|(264,)|var|int8
call_398 = relay.TupleGetItem(func_244_call(relay.reshape(var_399.astype('int8'), [4, 6, 11])), 0)
call_400 = relay.TupleGetItem(func_246_call(relay.reshape(var_399.astype('int8'), [4, 6, 11])), 0)
uop_403 = relay.acosh(call_398.astype('float32')) # shape=(4, 6, 11)
uop_405 = relay.acosh(call_400.astype('float32')) # shape=(4, 6, 11)
func_244_call = mod.get_global_var('func_244')
func_246_call = mutated_mod.get_global_var('func_246')
call_407 = relay.TupleGetItem(func_244_call(relay.reshape(uop_403.astype('int8'), [4, 6, 11])), 0)
call_408 = relay.TupleGetItem(func_246_call(relay.reshape(uop_403.astype('int8'), [4, 6, 11])), 0)
uop_416 = relay.asin(var_381.astype('float32')) # shape=(7, 9, 10)
output = relay.Tuple([bop_382,bop_388,var_399,uop_403,call_407,uop_416,])
output2 = relay.Tuple([bop_382,bop_388,var_399,uop_405,call_408,uop_416,])
func_423 = relay.Function([var_380,var_381,var_399,], output)
mod['func_423'] = func_423
mod = relay.transform.InferType()(mod)
mutated_mod['func_423'] = func_423
mutated_mod = relay.transform.InferType()(mutated_mod)
func_423_call = mutated_mod.get_global_var('func_423')
var_425 = relay.var("var_425", dtype = "int32", shape = ())#candidate|425|()|var|int32
var_426 = relay.var("var_426", dtype = "int32", shape = (7, 9, 10))#candidate|426|(7, 9, 10)|var|int32
var_427 = relay.var("var_427", dtype = "int8", shape = (264,))#candidate|427|(264,)|var|int8
call_424 = func_423_call(var_425,var_426,var_427,)
output = call_424
func_428 = relay.Function([var_425,var_426,var_427,], output)
mutated_mod['func_428'] = func_428
mutated_mod = relay.transform.InferType()(mutated_mod)
var_485 = relay.var("var_485", dtype = "int8", shape = (11, 13, 1))#candidate|485|(11, 13, 1)|var|int8
var_486 = relay.var("var_486", dtype = "int8", shape = (11, 13, 11))#candidate|486|(11, 13, 11)|var|int8
bop_487 = relay.less(var_485.astype('bool'), var_486.astype('bool')) # shape=(11, 13, 11)
bop_491 = relay.left_shift(var_486.astype('uint32'), var_485.astype('uint32')) # shape=(11, 13, 11)
bop_496 = relay.bitwise_or(bop_491.astype('int32'), var_485.astype('int32')) # shape=(11, 13, 11)
output = relay.Tuple([bop_487,bop_496,])
output2 = relay.Tuple([bop_487,bop_496,])
func_533 = relay.Function([var_485,var_486,], output)
mod['func_533'] = func_533
mod = relay.transform.InferType()(mod)
mutated_mod['func_533'] = func_533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_533_call = mutated_mod.get_global_var('func_533')
var_535 = relay.var("var_535", dtype = "int8", shape = (11, 13, 1))#candidate|535|(11, 13, 1)|var|int8
var_536 = relay.var("var_536", dtype = "int8", shape = (11, 13, 11))#candidate|536|(11, 13, 11)|var|int8
call_534 = func_533_call(var_535,var_536,)
output = call_534
func_537 = relay.Function([var_535,var_536,], output)
mutated_mod['func_537'] = func_537
mutated_mod = relay.transform.InferType()(mutated_mod)
const_818 = relay.const([[[-9.592596,8.678543,2.220397,-5.276103],[-2.593430,2.431607,6.186067,8.083282],[2.954632,-6.444789,-8.594736,-8.987744],[-5.561878,7.760231,3.772165,-5.581187],[3.418469,9.947027,-7.740173,-0.920127],[-8.851984,-2.214958,6.303142,-0.812762],[-4.980639,2.138350,-4.418785,-8.074222]]], dtype = "float64")#candidate|818|(1, 7, 4)|const|float64
uop_819 = relay.exp(const_818.astype('float64')) # shape=(1, 7, 4)
func_423_call = mod.get_global_var('func_423')
func_428_call = mutated_mod.get_global_var('func_428')
const_834 = relay.const(6, dtype = "int32")#candidate|834|()|const|int32
const_835 = relay.const([2,-1,-7,3,-9,4,-9,-3,2,-10,-8,10,-10,-6,-8,-10,-5,5,-10,-7,-3,4,10,2,9,2,6,-1,-1,-3,-6,-1,-5,-2,-5,8,1,-10,1,-2,-6,6,-8,-10,-4,10,-7,-2,7,9,-4,-10,1,8,3,-10,4,-3,-3,-3,-8,-6,4,-9,-3,-5,-7,1,-6,-10,9,-10,-4,-7,-7,-3,-3,-2,-8,-8,-1,-7,9,-6,7,3,-6,10,7,-8,-10,-3,-1,-8,6,-9,2,-7,3,5,1,-7,3,8,9,-6,8,-9,-4,7,6,9,1,-6,-1,-4,1,1,3,3,7,8,-1,-4,6,7,7,-8,3,-3,-7,9,10,-1,1,-2,3,4,9,-9,9,-6,1,7,2,-10,-6,-6,-1,9,10,10,3,7,2,-10,-1,9,2,8,5,2,9,8,-4,-5,10,8,-1,-9,3,6,-6,8,3,2,5,1,-6,7,-8,6,10,-3,-1,4,2,9,-6,-5,-4,9,3,-7,-3,-10,-9,-10,10,-7,-8,4,2,-7,2,-9,9,8,-2,-2,9,5,-6,-6,2,7,6,-9,7,-1,6,-5,-2,8,8,-8,-1,7,-9,4,-6,-1,-4,-5,6,10,-7,-8,6,2,5,-2,-2,4,2,5,10,-2,-6,-5,-4,4,-8,10,-8,9,-2,-10,10,6,-3,-9,6,-7,-10,-5,-7,-8,1,10,-2,-3,-2,7,-8,-3,5,-5,-3,5,5,10,9,7,-7,7,8,2,-4,1,5,4,5,-4,2,-4,9,6,-3,8,-2,9,-7,-9,3,3,-3,9,8,6,5,6,-3,2,7,-6,-4,-8,-8,-2,-6,-1,5,7,-5,3,1,4,4,-10,7,-10,2,2,5,-3,10,-2,-5,-8,1,2,1,-8,3,5,-5,-1,-5,5,8,2,3,2,-4,8,-2,-1,-6,9,8,-9,3,8,-4,7,-2,-1,7,-10,-6,6,1,-4,-6,-8,8,-7,-1,8,-7,-9,-6,-3,8,3,6,-3,-9,-5,9,-1,-5,8,1,-1,-1,-9,-5,-1,8,6,-3,10,-5,7,8,-2,6,9,8,-8,-4,-7,9,-9,-9,-2,3,6,-7,-3,1,-10,-7,-4,10,-3,9,3,-7,-9,-7,-3,-1,8,2,-2,7,1,2,-9,9,7,4,-8,-2,9,7,8,1,-5,9,7,1,2,-5,-6,-4,2,2,-1,8,2,4,-3,-9,-1,8,-4,7,-2,8,-7,-10,-2,-3,-7,-7,-6,2,-7,2,9,5,8,-1,4,-10,-4,2,-5,1,7,2,8,-7,-4,2,-6,7,8,-8,-7,-5,-1,7,3,-7,-3,-6,-4,5,-9,-1,3,-2,-10,-5,-9,10,-9,-5,4,-5,-2,9,1,3,-2,-6,6,7,-6,-3,-5,6,-9,-8,-2,1,3,1,-5,-3,-1,-3,7,-5,4,-10,2,-7,-7,-3,8,-5,5,5,10,-6,-9,2,-10,-10,6,7,8,-6,-9,-3,4,-9,6,8,6,-1,-4,2,9,-8,2,2,9,4,-8,6,9,-10,1,-10,-3,-1,-3,8,-5,-6,4,-10,5,-1,-2,-4,4,5,1,2,6,10,-8,-3,7,-3,-7,-5,6,-5,5,-9,-3,-2,-10,8,-10,7,-9,5,10,-8,-1], dtype = "int32")#candidate|835|(630,)|const|int32
const_836 = relay.const([-1,5,-8,-2,-1,-5,1,-10,4,-10,-8,10,3,6,10,-10,6,6,-2,-2,3,5,-5,-6,4,1,-3,9,8,9,-5,-1,-6,2,3,2,-3,1,-4,6,-5,10,-7,-5,6,-5,2,-1,-10,8,-9,1,-7,-10,1,9,-5,5,7,9,3,6,9,-6,10,-4,4,1,-10,-2,-8,-9,9,-7,6,-2,9,8,3,10,-10,2,-2,5,3,4,-10,4,-1,-8,6,-7,7,-4,-1,-4,1,-5,9,6,9,3,7,9,-8,-4,-8,-1,8,5,-2,-2,-7,3,-7,5,-10,-3,6,4,2,10,1,-3,9,-10,-9,1,9,1,4,10,-6,3,-7,-8,5,9,9,6,-1,6,-1,7,2,4,4,2,-8,-2,1,6,-7,-1,8,-6,-6,-1,1,6,6,1,-3,9,-9,-6,10,6,6,6,7,-5,6,1,-5,-3,7,2,9,3,2,-10,-3,2,6,-5,9,9,7,-5,6,-5,1,7,7,-2,9,-1,-8,4,-10,8,-9,7,6,-10,9,9,1,2,4,-8,5,7,-4,-9,8,-6,-4,-2,-6,-5,8,-6,8,8,3,-6,7,4,-4,6,8,-8,-6,3,5,-6,1,-3,-10,-4,-8,1,-6,9,-6,2,6,8,-4,-1,-10,3,8,2,-8,-9,9,-4,-5,-2,7,-4], dtype = "int8")#candidate|836|(264,)|const|int8
call_833 = relay.TupleGetItem(func_423_call(relay.reshape(const_834.astype('int32'), []), relay.reshape(const_835.astype('int32'), [7, 9, 10]), relay.reshape(const_836.astype('int8'), [264,]), ), 4)
call_837 = relay.TupleGetItem(func_428_call(relay.reshape(const_834.astype('int32'), []), relay.reshape(const_835.astype('int32'), [7, 9, 10]), relay.reshape(const_836.astype('int8'), [264,]), ), 4)
output = relay.Tuple([uop_819,call_833,const_834,const_835,const_836,])
output2 = relay.Tuple([uop_819,call_837,const_834,const_835,const_836,])
func_839 = relay.Function([], output)
mod['func_839'] = func_839
mod = relay.transform.InferType()(mod)
mutated_mod['func_839'] = func_839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_839_call = mutated_mod.get_global_var('func_839')
call_840 = func_839_call()
output = call_840
func_841 = relay.Function([], output)
mutated_mod['func_841'] = func_841
mutated_mod = relay.transform.InferType()(mutated_mod)
var_857 = relay.var("var_857", dtype = "float32", shape = (3, 11, 9))#candidate|857|(3, 11, 9)|var|float32
uop_858 = relay.log(var_857.astype('float32')) # shape=(3, 11, 9)
const_865 = relay.const([[[2.942861,8.075214,-1.738667,7.251472,-8.418526,-7.895296,9.476862,2.113312,2.188155],[1.905495,-7.056697,-7.446570,7.499992,9.204302,0.903242,5.752432,6.984125,1.644002],[-3.986863,2.287449,-1.819071,6.686971,5.246211,7.252596,-8.761378,-9.733948,-9.262947],[-5.841206,-0.945087,-3.846224,-0.015151,-6.605203,8.759874,-2.055448,3.892617,-6.432406],[4.793775,8.853511,6.234527,7.395741,2.862952,-5.452121,-4.370507,0.765467,-2.862793],[-5.444254,-9.236942,1.972168,0.808276,1.073821,2.861556,-5.304149,8.169633,-4.556463],[7.674314,-3.628514,3.041166,-3.709855,8.471373,-6.815408,6.199450,-8.978425,-9.275215],[5.232798,2.395931,-7.362937,6.446129,5.030255,-3.350299,6.034542,6.971523,-0.862709],[-7.581712,1.124745,9.919500,-9.722141,-0.331387,-7.364334,-9.849094,-0.108124,-6.996907],[-0.412146,-9.634495,-0.224458,0.750340,-4.618782,7.613453,-7.577500,4.017403,1.559140],[9.105925,8.230147,-5.149699,-7.773754,-7.530063,2.646772,3.053736,-0.736897,9.513792]],[[-0.938431,-1.884048,-5.676570,-8.017852,5.491125,-0.648290,-7.701727,-0.571773,4.974993],[2.758024,9.995543,3.269502,-1.589809,3.149205,-7.461144,0.655528,0.414664,9.853282],[1.613661,-0.046988,9.176726,0.188868,8.538007,6.353355,-7.673329,-2.621681,-6.850957],[-1.077483,4.917363,6.684878,3.254474,-8.811114,-7.392201,-8.478281,1.827862,1.003535],[1.298496,-8.087278,-9.773038,3.298733,-2.517373,1.580968,3.839683,8.861343,2.639122],[-3.689875,1.789421,6.014190,-1.631407,8.500943,3.761832,-9.002778,2.460793,2.787148],[7.700550,3.380823,-5.952847,-4.541375,-4.857174,-4.466617,0.908426,-4.113215,-1.814525],[-2.426375,6.144174,-6.829958,-6.714109,2.073536,-5.674903,-8.271924,-2.467161,4.818590],[-2.402938,-1.674320,-9.672037,-0.865127,-5.106457,-4.161007,-1.049969,3.141761,9.841343],[-3.922094,5.930029,1.147138,-3.061233,8.918085,9.225435,-2.114920,-4.284345,6.909945],[2.529140,-0.532436,-8.928206,-8.926363,-5.713998,8.785004,-5.771787,5.685010,2.651042]],[[4.459217,-5.783774,-4.251394,8.577240,9.308843,-1.259306,-1.893757,-2.361964,8.849528],[-0.184984,-5.783246,9.189782,-3.012612,5.005596,6.500539,-4.681020,1.064095,1.269497],[4.445063,-0.578014,0.879756,7.782501,-7.703200,-9.031570,-7.455557,-9.615315,5.578447],[-9.218534,2.226996,-2.458918,2.798665,8.590038,2.410851,-2.475651,4.138937,-7.677392],[4.336501,7.304447,6.966906,9.860559,-1.169856,-1.618159,-4.751013,7.708344,1.203752],[-5.962597,-8.077371,1.659153,4.966155,-4.937809,-9.913197,5.962257,-4.768115,4.257531],[-9.248959,-5.503814,-5.323770,3.270232,4.140495,-7.566249,-5.335620,5.614784,-7.760430],[-8.895260,7.008163,4.505139,8.649148,6.234024,7.908169,-9.084842,-6.494742,-7.775514],[2.610098,4.021567,-3.920824,9.326790,-5.677883,1.147926,5.865027,-8.596111,6.639612],[-1.879863,-8.583661,-0.166194,6.989755,-5.431392,3.222380,-6.011964,-3.671680,-4.430993],[-4.905948,2.939293,-5.906794,2.076609,-0.806128,-3.533830,5.026748,7.368717,9.534323]]], dtype = "float32")#candidate|865|(3, 11, 9)|const|float32
bop_866 = relay.add(uop_858.astype('int16'), relay.reshape(const_865.astype('int16'), relay.shape_of(uop_858))) # shape=(3, 11, 9)
func_244_call = mod.get_global_var('func_244')
func_246_call = mutated_mod.get_global_var('func_246')
var_879 = relay.var("var_879", dtype = "int8", shape = (264,))#candidate|879|(264,)|var|int8
call_878 = relay.TupleGetItem(func_244_call(relay.reshape(var_879.astype('int8'), [4, 6, 11])), 0)
call_880 = relay.TupleGetItem(func_246_call(relay.reshape(var_879.astype('int8'), [4, 6, 11])), 0)
uop_891 = relay.log10(var_857.astype('float32')) # shape=(3, 11, 9)
output = relay.Tuple([bop_866,call_878,var_879,uop_891,])
output2 = relay.Tuple([bop_866,call_880,var_879,uop_891,])
func_893 = relay.Function([var_857,var_879,], output)
mod['func_893'] = func_893
mod = relay.transform.InferType()(mod)
mutated_mod['func_893'] = func_893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_893_call = mutated_mod.get_global_var('func_893')
var_895 = relay.var("var_895", dtype = "float32", shape = (3, 11, 9))#candidate|895|(3, 11, 9)|var|float32
var_896 = relay.var("var_896", dtype = "int8", shape = (264,))#candidate|896|(264,)|var|int8
call_894 = func_893_call(var_895,var_896,)
output = call_894
func_897 = relay.Function([var_895,var_896,], output)
mutated_mod['func_897'] = func_897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_839_call = mod.get_global_var('func_839')
func_841_call = mutated_mod.get_global_var('func_841')
call_939 = relay.TupleGetItem(func_839_call(), 1)
call_940 = relay.TupleGetItem(func_841_call(), 1)
func_839_call = mod.get_global_var('func_839')
func_841_call = mutated_mod.get_global_var('func_841')
call_950 = relay.TupleGetItem(func_839_call(), 0)
call_951 = relay.TupleGetItem(func_841_call(), 0)
uop_958 = relay.sinh(call_950.astype('float64')) # shape=(1, 7, 4)
uop_960 = relay.sinh(call_951.astype('float64')) # shape=(1, 7, 4)
func_533_call = mod.get_global_var('func_533')
func_537_call = mutated_mod.get_global_var('func_537')
var_965 = relay.var("var_965", dtype = "int8", shape = (143,))#candidate|965|(143,)|var|int8
var_966 = relay.var("var_966", dtype = "int8", shape = (1573,))#candidate|966|(1573,)|var|int8
call_964 = relay.TupleGetItem(func_533_call(relay.reshape(var_965.astype('int8'), [11, 13, 1]), relay.reshape(var_966.astype('int8'), [11, 13, 11]), ), 0)
call_967 = relay.TupleGetItem(func_537_call(relay.reshape(var_965.astype('int8'), [11, 13, 1]), relay.reshape(var_966.astype('int8'), [11, 13, 11]), ), 0)
var_970 = relay.var("var_970", dtype = "int8", shape = (143,))#candidate|970|(143,)|var|int8
bop_971 = relay.multiply(var_965.astype('int16'), relay.reshape(var_970.astype('int16'), relay.shape_of(var_965))) # shape=(143,)
uop_981 = relay.erf(call_950.astype('float32')) # shape=(1, 7, 4)
uop_983 = relay.erf(call_951.astype('float32')) # shape=(1, 7, 4)
bop_986 = relay.logical_and(uop_958.astype('bool'), relay.reshape(call_950.astype('bool'), relay.shape_of(uop_958))) # shape=(1, 7, 4)
bop_989 = relay.logical_and(uop_960.astype('bool'), relay.reshape(call_951.astype('bool'), relay.shape_of(uop_960))) # shape=(1, 7, 4)
bop_1003 = relay.subtract(call_964.astype('uint8'), relay.reshape(var_966.astype('uint8'), relay.shape_of(call_964))) # shape=(11, 13, 11)
bop_1006 = relay.subtract(call_967.astype('uint8'), relay.reshape(var_966.astype('uint8'), relay.shape_of(call_967))) # shape=(11, 13, 11)
output = relay.Tuple([call_939,bop_971,uop_981,bop_986,bop_1003,])
output2 = relay.Tuple([call_940,bop_971,uop_983,bop_989,bop_1006,])
func_1012 = relay.Function([var_965,var_966,var_970,], output)
mod['func_1012'] = func_1012
mod = relay.transform.InferType()(mod)
var_1013 = relay.var("var_1013", dtype = "int8", shape = (143,))#candidate|1013|(143,)|var|int8
var_1014 = relay.var("var_1014", dtype = "int8", shape = (1573,))#candidate|1014|(1573,)|var|int8
var_1015 = relay.var("var_1015", dtype = "int8", shape = (143,))#candidate|1015|(143,)|var|int8
output = func_1012(var_1013,var_1014,var_1015,)
func_1016 = relay.Function([var_1013,var_1014,var_1015,], output)
mutated_mod['func_1016'] = func_1016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_839_call = mod.get_global_var('func_839')
func_841_call = mutated_mod.get_global_var('func_841')
call_1020 = relay.TupleGetItem(func_839_call(), 3)
call_1021 = relay.TupleGetItem(func_841_call(), 3)
uop_1024 = relay.erf(call_1020.astype('float64')) # shape=(630,)
uop_1026 = relay.erf(call_1021.astype('float64')) # shape=(630,)
func_423_call = mod.get_global_var('func_423')
func_428_call = mutated_mod.get_global_var('func_428')
const_1045 = relay.const(6, dtype = "int32")#candidate|1045|()|const|int32
const_1046 = relay.const([-2,-7,6,7,2,-1,3,-1,8,-7,-9,-5,7,-5,-2,-2,-5,-7,2,4,-1,4,10,5,3,9,3,2,1,8,-8,-10,-9,3,2,-7,4,-9,5,6,-9,3,-8,4,4,5,-2,6,1,-7,1,-5,5,1,9,-9,2,-10,9,-2,-8,7,-1,3,4,-4,-4,-10,-3,9,10,-10,-4,-7,-6,3,5,4,-5,-9,-9,-4,1,3,8,-8,4,3,8,-8,-8,-8,3,8,-3,6,9,6,-7,6,1,-6,-1,2,10,6,10,-10,8,-2,-6,-2,10,6,6,-5,-5,-3,-1,-8,4,-8,7,-9,7,-3,-2,7,-4,-1,7,9,-8,-10,9,9,-3,-10,-6,-3,-2,5,3,6,-5,8,-5,-5,1,-2,-3,-4,10,7,4,-7,8,2,4,-9,-5,2,-3,-2,2,5,-7,-4,-4,10,-10,-6,-1,-10,-6,-5,-5,10,-5,2,-8,-3,-5,-9,7,-9,-10,-5,-1,5,3,8,-8,8,3,-1,7,6,-10,-3,8,-1,-4,9,-3,-5,-8,-6,3,2,-4,-9,-6,2,-1,10,-6,-10,-9,-8,-5,1,-5,-2,3,-6,-4,7,-1,-5,-6,2,9,-2,10,3,4,1,-2,-8,4,9,1,1,7,-4,2,-4,-9,9,8,-7,5,2,10,2,5,5,9,8,1,-8,-10,-1], dtype = "int8")#candidate|1046|(264,)|const|int8
call_1044 = relay.TupleGetItem(func_423_call(relay.reshape(const_1045.astype('int32'), []), relay.reshape(uop_1024.astype('int32'), [7, 9, 10]), relay.reshape(const_1046.astype('int8'), [264,]), ), 3)
call_1047 = relay.TupleGetItem(func_428_call(relay.reshape(const_1045.astype('int32'), []), relay.reshape(uop_1024.astype('int32'), [7, 9, 10]), relay.reshape(const_1046.astype('int8'), [264,]), ), 3)
func_423_call = mod.get_global_var('func_423')
func_428_call = mutated_mod.get_global_var('func_428')
call_1049 = relay.TupleGetItem(func_423_call(relay.reshape(const_1045.astype('int32'), []), relay.reshape(uop_1024.astype('int32'), [7, 9, 10]), relay.reshape(call_1044.astype('int8'), [264,]), ), 0)
call_1050 = relay.TupleGetItem(func_428_call(relay.reshape(const_1045.astype('int32'), []), relay.reshape(uop_1024.astype('int32'), [7, 9, 10]), relay.reshape(call_1044.astype('int8'), [264,]), ), 0)
func_1012_call = mod.get_global_var('func_1012')
func_1016_call = mutated_mod.get_global_var('func_1016')
const_1055 = relay.const([-4,9,-3,8,8,-1,9,1,6,-1,10,-3,1,-4,-8,8,-5,7,-2,2,-7,2,-6,-9,5,-5,9,9,-3,-10,-9,4,5,-2,4,-8,-8,-8,-5,7,7,4,10,-6,10,4,4,1,-7,8,-8,-4,-9,1,9,6,9,-4,5,2,3,3,3,-7,-1,-6,5,5,4,10,3,-1,-5,-1,-4,6,-8,5,6,-6,10,4,-1,9,-7,3,4,4,1,-10,8,-2,-6,10,10,-7,-7,4,-1,7,4,10,4,-7,-7,9,2,4,6,-8,-1,7,-5,9,-3,-6,4,5,7,-2,7,-2,3,-7,-3,5,1,5,2,3,-8,-2,-4,2,-9,8,6,-6,-9,7,-1,7,6], dtype = "int8")#candidate|1055|(143,)|const|int8
const_1056 = relay.const([-5,6,1,6,7,9,-2,3,-8,-8,4,-10,-2,7,8,-8,8,6,2,-7,10,6,-2,2,9,-8,7,-10,-4,7,-2,-4,-9,-2,-2,1,-6,6,5,9,-7,-7,-6,1,3,-3,-3,7,-7,2,-9,-1,-9,2,-4,7,1,-6,-10,-8,-5,2,-8,-9,-10,-4,3,4,2,-7,1,8,10,9,-10,-7,-6,2,-7,-8,-1,6,8,7,7,8,8,10,-9,9,3,-2,-4,4,-5,-6,7,-10,3,-6,-1,-8,10,8,6,7,-3,8,-5,-7,-7,7,-7,8,6,10,-10,-6,-8,-10,-4,-4,7,-4,-6,-3,8,-6,8,-4,-10,2,7,-10,2,7,-6,3,-5,-6,-2,4,10,4,6,2,4,-7,2,6,-9,2,-6,-1,-3,-1,-5,-6,5,-2,-10,10,-8,7,-4,4,5,-1,2,-1,-8,-2,7,7,-10,4,3,5,1,-9,-4,10,-10,2,2,9,-8,-2,-10,9,-8,-1,-9,2,8,-6,-6,-6,7,10,-3,-9,1,8,-10,3,-9,1,-1,-7,4,-5,-2,-1,-9,8,2,-5,-9,-8,9,9,8,-6,-2,-9,-10,9,5,9,-2,8,-6,-9,-7,8,-8,3,-6,4,4,4,-10,-6,-4,-1,-3,10,-3,8,4,3,2,8,7,-6,9,-6,5,-8,-6,3,9,1,-2,1,5,-10,1,5,-3,-8,-10,-3,-6,-4,-9,2,-2,-7,1,2,1,-5,1,-10,-10,7,5,-5,-1,1,-7,6,-5,-4,3,6,-8,-8,-8,3,9,8,-2,-2,3,2,8,1,-1,2,3,-9,9,-1,-6,-5,-6,8,9,10,-7,3,-10,-9,-1,6,10,-4,3,-6,-2,3,-5,6,4,9,10,-7,8,1,8,3,3,5,-5,-4,-3,4,1,-3,8,6,-3,6,8,1,7,4,-3,7,-1,4,-1,1,8,6,-7,2,5,3,9,1,-10,-7,5,5,-6,-9,7,8,-5,3,-7,4,-5,7,-3,-10,-3,-9,1,-2,3,4,3,-7,-6,-2,7,7,3,6,4,10,-2,-4,1,10,9,-5,-5,3,-5,6,-1,6,9,-1,-9,-10,9,6,2,-3,-1,3,3,7,9,1,-8,-7,8,-10,8,-8,4,9,9,4,2,-5,-3,2,6,3,8,-3,-9,-3,-2,6,-6,-1,6,-4,5,3,4,2,-9,-5,7,5,-10,-5,-1,8,5,-2,-7,7,-8,1,-6,-3,2,-3,-4,4,-7,8,-9,5,8,-3,6,10,-2,7,6,4,5,-6,6,-7,-1,2,1,-4,-9,-5,-8,-10,-8,2,-6,-3,-4,4,-10,-4,5,-1,-7,5,-1,-2,9,-3,10,10,-4,9,-1,9,-3,2,-2,2,9,5,2,-1,1,8,1,-5,1,4,-6,-3,7,7,-10,9,10,9,3,-3,-8,-6,-8,-4,7,-1,1,4,-3,7,9,3,4,-1,4,3,-4,-10,10,-1,4,-9,-10,-2,3,-6,-9,-2,-1,-10,-9,-6,2,5,-2,10,-10,2,2,-1,-5,-7,-6,-7,-2,-3,-2,3,-6,7,-5,-5,-5,-3,3,2,-2,4,8,4,-2,2,-5,9,3,1,-4,3,5,8,1,-8,9,-1,-5,8,10,-1,-6,8,10,-7,8,-6,7,3,-4,-3,6,1,-6,9,10,3,-4,-5,-10,9,-4,3,10,1,8,8,-7,5,9,-1,8,5,5,-4,-2,-3,9,10,-3,-5,7,6,4,7,-7,-2,-4,-5,-7,-4,-6,-5,-2,-6,6,-7,-5,-6,4,2,-4,4,-3,7,-2,9,7,-2,-1,-5,8,-9,-4,-1,10,2,8,-4,-7,-1,1,4,5,8,-6,4,-4,8,8,10,3,-6,8,-1,10,-3,-3,-8,4,-6,-8,6,-3,-3,2,-3,-3,-5,8,5,10,-8,6,-3,3,-3,-2,-4,-1,-10,-10,9,1,-4,2,6,1,4,1,10,-1,-6,3,-1,-6,-1,-3,10,4,10,5,-7,1,6,1,7,-10,-6,-10,-1,-8,-3,-3,-5,-6,3,1,10,3,4,-1,-7,-2,5,-2,10,-9,10,-5,8,-10,-3,-3,2,6,-2,-7,-9,4,4,-2,-7,-9,-4,-2,6,-5,2,1,-6,2,-5,10,1,-1,1,9,-6,-3,-3,-3,6,7,8,1,-4,-5,-5,4,-9,1,8,-8,-10,-7,7,-1,9,-10,-5,-2,-8,-9,-2,-7,8,2,7,10,-2,-10,6,1,-1,-2,-4,5,-3,-2,-5,-5,6,9,-7,1,-8,8,6,1,10,2,-10,-5,1,-6,-8,-1,10,8,-3,-7,-3,6,4,-5,-1,-10,7,-1,-5,-9,2,5,-2,-9,3,-5,-1,-4,-8,-1,9,7,-9,4,-9,-4,3,-3,4,1,8,-4,8,-5,-10,-5,-2,-4,-3,4,1,3,9,2,-5,-1,-10,-3,-6,5,9,-4,4,-9,-6,1,10,5,9,5,8,-9,2,9,2,-3,-5,9,4,-8,-2,-10,-2,-4,-10,-7,4,9,7,3,1,2,2,7,1,6,6,-6,9,-9,6,1,1,-5,9,10,3,-8,-5,-10,-2,-10,10,-7,5,-2,-4,-2,-5,5,-6,-4,9,5,-8,-10,1,7,7,4,9,-4,9,8,-4,7,-10,-10,-4,-2,-2,-1,2,6,-3,3,6,-5,-5,10,5,-3,8,-3,10,5,10,7,-5,3,-5,9,6,-8,-6,2,8,8,1,-10,-9,-5,2,-2,6,6,4,7,-9,10,-5,-7,-10,-9,-6,-1,6,5,9,5,-7,-1,4,10,2,9,6,10,-2,-6,10,5,-7,-3,2,-6,-9,-7,-2,8,-8,-3,4,-2,-4,5,10,-1,-2,3,-2,-2,-5,-4,7,3,9,-2,9,7,4,1,-2,1,7,-10,3,8,3,7,3,7,-7,-3,5,-2,-4,3,3,1,-7,9,-5,10,-10,-9,-8,-5,7,1,-1,-5,6,-10,3,1,4,-2,6,8,2,10,-4,-4,6,5,8,10,-9,5,2,1,-5,-5,-8,8,8,9,5,-3,1,-8,-9,5,7,-9,5,4,-3,-10,2,3,5,2,-7,1,-6,-9,7,2,-3,2,-10,-5,-5,-6,-2,-7,-10,9,5,-5,10,5,-7,3,7,-7,4,-10,6,8,-4,7,5,3,-7,-10,-2,4,1,9,-3,-4,6,-7,-1,-2,-9,1,4,-3,-2,-8,9,4,-1,7,9,2,7,-10,6,5,3,-9,-2,10,9,-10,1,-6,9,8,-7,3,-2,4,7,3,-7,-6,9,5,-3,-4,-1,9,-6,-7,-9,-10,-5,1,6,-9,10,-4,-1,-5,-5,1,1,-5,-8,1,3,10,-6,10,-7,-4,6,6,-6,2,-9,-9,-4,9,-7,9,2,9,-2,-9,-8,8,1,-1,-4,-2,7,-5,-6,-1,7,-4,-1,6,-4,6,7,5,-9,-9,-1,-10,-10,9,1,8,2,-4,9,-8,-6,2,-10,5,5,-4,5,-5,9,1,-4,6,5,10,-2,4,7,-3,-4,6,-10,-6,-4,-2,-4,3,-3,5,10,3,-6,-10,-4,-9,1,10,8,8,6,7,2,8,-8,5,-8,2,5,6,6,8,3,-9,-3,-4,-7,-10,10,6,1,-8,10,-7,-1,-2,10,-4,-9,3,2,-10,-10,-9,8,-10,5,-2,-7,9,1,7,-5,-4,6,6,-7,-8,-9,-7,2,-10,5,-3,-10,-2,-6,-4,-10,5,8,-5,-8,-1,-9,3,-8,-10,4,5,6,7,-8,2,9,-3,7,-1,-2,1,3,-5,-9,-1,-8,9,8,7,8,4,-7,4,7,-10,-8,-10,-8,-9,2,2,-10,6,-6,4,2,-1,4,-4,1,-10,8,-9,7,-3,-1,8,5,-9,-7,-5,8,-6,1,3,-6,10,-3,10,8,8,8,1,2,-6,-5,-7,-9,5,-5,-4,1,4,-7,-5,-10,4,-3,-3,9,3,2,-6,5,3,-2,-10,2,-9,2,4,9,10,-7,6,-4,-7,-10,-9,4,4,8,-9,2,1,-1,4,5,1,-8,-5,5,1,2,-10,-2,2,-2,2,8,6,8,-9,-7,-2,-7,-9,8,-10], dtype = "int8")#candidate|1056|(1573,)|const|int8
call_1054 = relay.TupleGetItem(func_1012_call(relay.reshape(const_1055.astype('int8'), [143,]), relay.reshape(const_1056.astype('int8'), [1573,]), relay.reshape(const_1055.astype('int8'), [143,]), ), 3)
call_1057 = relay.TupleGetItem(func_1016_call(relay.reshape(const_1055.astype('int8'), [143,]), relay.reshape(const_1056.astype('int8'), [1573,]), relay.reshape(const_1055.astype('int8'), [143,]), ), 3)
output = relay.Tuple([uop_1024,call_1044,const_1045,const_1046,call_1049,call_1054,const_1055,const_1056,])
output2 = relay.Tuple([uop_1026,call_1047,const_1045,const_1046,call_1050,call_1057,const_1055,const_1056,])
func_1083 = relay.Function([], output)
mod['func_1083'] = func_1083
mod = relay.transform.InferType()(mod)
mutated_mod['func_1083'] = func_1083
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1083_call = mutated_mod.get_global_var('func_1083')
call_1084 = func_1083_call()
output = call_1084
func_1085 = relay.Function([], output)
mutated_mod['func_1085'] = func_1085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1083_call = mod.get_global_var('func_1083')
func_1085_call = mutated_mod.get_global_var('func_1085')
call_1097 = relay.TupleGetItem(func_1083_call(), 4)
call_1098 = relay.TupleGetItem(func_1085_call(), 4)
uop_1105 = relay.acos(call_1097.astype('float64')) # shape=(7, 9, 10)
uop_1107 = relay.acos(call_1098.astype('float64')) # shape=(7, 9, 10)
func_244_call = mod.get_global_var('func_244')
func_246_call = mutated_mod.get_global_var('func_246')
const_1109 = relay.const([7,10,2,2,-7,2,-4,5,-1,5,-7,-5,3,4,-2,-7,-5,-2,2,-6,5,-4,-6,-8,-4,-2,5,10,9,-4,-3,9,7,8,5,8,-5,-10,1,-8,3,8,7,-8,9,7,-2,-1,-8,-8,-4,-5,-9,8,3,5,-7,-5,-10,-9,2,5,2,3,-5,-3,9,8,2,-8,-3,2,7,-4,-10,-9,9,-8,-10,-1,4,-5,-3,-1,-8,-2,1,3,-5,6,-10,-8,9,-3,9,-5,9,5,1,-9,-6,-4,-6,6,3,-7,-7,3,-2,-4,-2,5,-8,-3,8,-10,2,-1,10,-2,-9,8,-5,-1,-9,10,-3,3,3,2,8,6,-5,-2,2,10,2,-7,-10,4,3,-1,6,8,9,-3,-2,-9,-5,6,3,-9,5,-4,4,6,-3,-4,10,10,-3,-6,-3,-6,6,-8,-9,5,-4,-10,-8,-6,3,10,5,5,-7,5,-8,10,2,-6,-6,-4,2,9,-10,9,-6,-9,10,-8,-6,7,-1,-1,-7,-3,-8,3,9,-9,8,2,-8,-2,-6,-5,1,-8,3,7,-6,4,7,3,-1,7,-10,-1,2,9,6,-10,-8,-1,-10,2,1,2,-5,-6,-7,6,-1,-6,-2,9,-8,5,9,-8,6,-9,-8,-5,-5,-9,-3,10,2,5,2,2,-2,8,4,-4,-10,9,3,-8,6,-1], dtype = "int8")#candidate|1109|(264,)|const|int8
call_1108 = relay.TupleGetItem(func_244_call(relay.reshape(const_1109.astype('int8'), [4, 6, 11])), 0)
call_1110 = relay.TupleGetItem(func_246_call(relay.reshape(const_1109.astype('int8'), [4, 6, 11])), 0)
output = relay.Tuple([uop_1105,call_1108,const_1109,])
output2 = relay.Tuple([uop_1107,call_1110,const_1109,])
func_1112 = relay.Function([], output)
mod['func_1112'] = func_1112
mod = relay.transform.InferType()(mod)
mutated_mod['func_1112'] = func_1112
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1112_call = mutated_mod.get_global_var('func_1112')
call_1113 = func_1112_call()
output = call_1113
func_1114 = relay.Function([], output)
mutated_mod['func_1114'] = func_1114
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1123 = relay.var("var_1123", dtype = "uint16", shape = (4, 9, 14))#candidate|1123|(4, 9, 14)|var|uint16
var_1124 = relay.var("var_1124", dtype = "uint16", shape = (4, 9, 14))#candidate|1124|(4, 9, 14)|var|uint16
bop_1125 = relay.bitwise_or(var_1123.astype('uint16'), relay.reshape(var_1124.astype('uint16'), relay.shape_of(var_1123))) # shape=(4, 9, 14)
uop_1132 = relay.cosh(var_1123.astype('float32')) # shape=(4, 9, 14)
uop_1134 = relay.log10(uop_1132.astype('float64')) # shape=(4, 9, 14)
uop_1145 = relay.atan(var_1123.astype('float32')) # shape=(4, 9, 14)
func_1083_call = mod.get_global_var('func_1083')
func_1085_call = mutated_mod.get_global_var('func_1085')
call_1151 = relay.TupleGetItem(func_1083_call(), 0)
call_1152 = relay.TupleGetItem(func_1085_call(), 0)
output = relay.Tuple([bop_1125,uop_1134,uop_1145,call_1151,])
output2 = relay.Tuple([bop_1125,uop_1134,uop_1145,call_1152,])
func_1174 = relay.Function([var_1123,var_1124,], output)
mod['func_1174'] = func_1174
mod = relay.transform.InferType()(mod)
mutated_mod['func_1174'] = func_1174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1174_call = mutated_mod.get_global_var('func_1174')
var_1176 = relay.var("var_1176", dtype = "uint16", shape = (4, 9, 14))#candidate|1176|(4, 9, 14)|var|uint16
var_1177 = relay.var("var_1177", dtype = "uint16", shape = (4, 9, 14))#candidate|1177|(4, 9, 14)|var|uint16
call_1175 = func_1174_call(var_1176,var_1177,)
output = call_1175
func_1178 = relay.Function([var_1176,var_1177,], output)
mutated_mod['func_1178'] = func_1178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1083_call = mod.get_global_var('func_1083')
func_1085_call = mutated_mod.get_global_var('func_1085')
call_1202 = relay.TupleGetItem(func_1083_call(), 5)
call_1203 = relay.TupleGetItem(func_1085_call(), 5)
const_1204 = relay.const([[[False,False,False,True],[False,False,True,True],[True,False,True,False],[False,True,True,True],[True,True,True,True],[True,False,True,False],[True,False,False,False]]], dtype = "bool")#candidate|1204|(1, 7, 4)|const|bool
bop_1205 = relay.mod(call_1202.astype('float32'), relay.reshape(const_1204.astype('float32'), relay.shape_of(call_1202))) # shape=(1, 7, 4)
bop_1208 = relay.mod(call_1203.astype('float32'), relay.reshape(const_1204.astype('float32'), relay.shape_of(call_1203))) # shape=(1, 7, 4)
bop_1215 = relay.maximum(call_1202.astype('float64'), relay.reshape(const_1204.astype('float64'), relay.shape_of(call_1202))) # shape=(1, 7, 4)
bop_1218 = relay.maximum(call_1203.astype('float64'), relay.reshape(const_1204.astype('float64'), relay.shape_of(call_1203))) # shape=(1, 7, 4)
uop_1227 = relay.sqrt(bop_1215.astype('float32')) # shape=(1, 7, 4)
uop_1229 = relay.sqrt(bop_1218.astype('float32')) # shape=(1, 7, 4)
bop_1232 = relay.multiply(uop_1227.astype('int16'), relay.reshape(const_1204.astype('int16'), relay.shape_of(uop_1227))) # shape=(1, 7, 4)
bop_1235 = relay.multiply(uop_1229.astype('int16'), relay.reshape(const_1204.astype('int16'), relay.shape_of(uop_1229))) # shape=(1, 7, 4)
uop_1236 = relay.rsqrt(uop_1227.astype('float32')) # shape=(1, 7, 4)
uop_1238 = relay.rsqrt(uop_1229.astype('float32')) # shape=(1, 7, 4)
func_244_call = mod.get_global_var('func_244')
func_246_call = mutated_mod.get_global_var('func_246')
var_1246 = relay.var("var_1246", dtype = "int8", shape = (264,))#candidate|1246|(264,)|var|int8
call_1245 = relay.TupleGetItem(func_244_call(relay.reshape(var_1246.astype('int8'), [4, 6, 11])), 0)
call_1247 = relay.TupleGetItem(func_246_call(relay.reshape(var_1246.astype('int8'), [4, 6, 11])), 0)
output = relay.Tuple([bop_1205,bop_1232,uop_1236,call_1245,var_1246,])
output2 = relay.Tuple([bop_1208,bop_1235,uop_1238,call_1247,var_1246,])
func_1253 = relay.Function([var_1246,], output)
mod['func_1253'] = func_1253
mod = relay.transform.InferType()(mod)
var_1254 = relay.var("var_1254", dtype = "int8", shape = (264,))#candidate|1254|(264,)|var|int8
output = func_1253(var_1254)
func_1255 = relay.Function([var_1254], output)
mutated_mod['func_1255'] = func_1255
mutated_mod = relay.transform.InferType()(mutated_mod)
func_839_call = mod.get_global_var('func_839')
func_841_call = mutated_mod.get_global_var('func_841')
call_1257 = relay.TupleGetItem(func_839_call(), 3)
call_1258 = relay.TupleGetItem(func_841_call(), 3)
output = relay.Tuple([call_1257,])
output2 = relay.Tuple([call_1258,])
func_1259 = relay.Function([], output)
mod['func_1259'] = func_1259
mod = relay.transform.InferType()(mod)
output = func_1259()
func_1260 = relay.Function([], output)
mutated_mod['func_1260'] = func_1260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_839_call = mod.get_global_var('func_839')
func_841_call = mutated_mod.get_global_var('func_841')
call_1273 = relay.TupleGetItem(func_839_call(), 0)
call_1274 = relay.TupleGetItem(func_841_call(), 0)
var_1281 = relay.var("var_1281", dtype = "float64", shape = (12, 7, 4))#candidate|1281|(12, 7, 4)|var|float64
bop_1282 = relay.left_shift(call_1273.astype('int32'), var_1281.astype('int32')) # shape=(12, 7, 4)
bop_1285 = relay.left_shift(call_1274.astype('int32'), var_1281.astype('int32')) # shape=(12, 7, 4)
output = bop_1282
output2 = bop_1285
func_1286 = relay.Function([var_1281,], output)
mod['func_1286'] = func_1286
mod = relay.transform.InferType()(mod)
mutated_mod['func_1286'] = func_1286
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1287 = relay.var("var_1287", dtype = "float64", shape = (12, 7, 4))#candidate|1287|(12, 7, 4)|var|float64
func_1286_call = mutated_mod.get_global_var('func_1286')
call_1288 = func_1286_call(var_1287)
output = call_1288
func_1289 = relay.Function([var_1287], output)
mutated_mod['func_1289'] = func_1289
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1303 = relay.const([[[3.555598,-3.497070,-8.734643,7.951493,-2.641038,3.474615,8.476851,2.437011,-7.641441,8.859118,2.029678,-2.680348,1.978662,-0.560951]],[[3.501068,-2.207894,2.746232,-0.920845,2.825074,6.884107,-8.307276,-9.741709,-4.571467,-5.434823,3.159680,-5.529919,1.624656,-2.481341]],[[-2.147483,8.655915,5.885913,7.265876,-3.557209,-4.415190,5.034746,1.688223,-0.799755,5.841427,1.964874,-0.186336,7.176895,-2.017237]],[[8.481831,-5.306874,5.916195,7.167066,3.536956,6.934603,-8.205651,8.444932,5.756766,6.865360,-7.622773,-0.023608,-4.393380,-9.438934]],[[9.667394,7.362742,-5.094342,5.914838,9.504412,-1.368209,0.353367,-4.017068,5.025726,9.583231,6.027570,-9.265638,6.505456,2.954056]],[[2.546610,6.506905,-4.370338,7.876792,-8.524749,-9.657046,-0.155222,-8.962056,-6.726253,1.173450,7.270283,7.801337,-9.958723,-9.352887]]], dtype = "float64")#candidate|1303|(6, 1, 14)|const|float64
uop_1304 = relay.acos(const_1303.astype('float64')) # shape=(6, 1, 14)
output = uop_1304
output2 = uop_1304
func_1319 = relay.Function([], output)
mod['func_1319'] = func_1319
mod = relay.transform.InferType()(mod)
output = func_1319()
func_1320 = relay.Function([], output)
mutated_mod['func_1320'] = func_1320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1259_call = mod.get_global_var('func_1259')
func_1260_call = mutated_mod.get_global_var('func_1260')
call_1340 = relay.TupleGetItem(func_1259_call(), 0)
call_1341 = relay.TupleGetItem(func_1260_call(), 0)
output = relay.Tuple([call_1340,])
output2 = relay.Tuple([call_1341,])
func_1355 = relay.Function([], output)
mod['func_1355'] = func_1355
mod = relay.transform.InferType()(mod)
output = func_1355()
func_1356 = relay.Function([], output)
mutated_mod['func_1356'] = func_1356
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1319_call = mod.get_global_var('func_1319')
func_1320_call = mutated_mod.get_global_var('func_1320')
call_1359 = func_1319_call()
call_1360 = func_1319_call()
output = relay.Tuple([call_1359,])
output2 = relay.Tuple([call_1360,])
func_1361 = relay.Function([], output)
mod['func_1361'] = func_1361
mod = relay.transform.InferType()(mod)
mutated_mod['func_1361'] = func_1361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1361_call = mutated_mod.get_global_var('func_1361')
call_1362 = func_1361_call()
output = call_1362
func_1363 = relay.Function([], output)
mutated_mod['func_1363'] = func_1363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1112_call = mod.get_global_var('func_1112')
func_1114_call = mutated_mod.get_global_var('func_1114')
call_1368 = relay.TupleGetItem(func_1112_call(), 0)
call_1369 = relay.TupleGetItem(func_1114_call(), 0)
output = relay.Tuple([call_1368,])
output2 = relay.Tuple([call_1369,])
func_1370 = relay.Function([], output)
mod['func_1370'] = func_1370
mod = relay.transform.InferType()(mod)
output = func_1370()
func_1371 = relay.Function([], output)
mutated_mod['func_1371'] = func_1371
mutated_mod = relay.transform.InferType()(mutated_mod)
func_839_call = mod.get_global_var('func_839')
func_841_call = mutated_mod.get_global_var('func_841')
call_1383 = relay.TupleGetItem(func_839_call(), 3)
call_1384 = relay.TupleGetItem(func_841_call(), 3)
func_893_call = mod.get_global_var('func_893')
func_897_call = mutated_mod.get_global_var('func_897')
const_1443 = relay.const([-7.197564,7.599124,6.931464,1.975521,3.458230,-8.139607,9.014434,-8.072510,-4.406626,8.864568,1.121440,6.574190,9.131818,9.708751,7.251597,9.835930,-2.518578,-4.082093,-6.048332,4.117166,2.875731,7.989018,-3.793006,1.319816,-5.936344,9.690290,9.727407,9.986875,-6.676349,8.348990,7.977482,-8.770383,6.807789,2.215405,-4.242940,-6.719000,-4.509970,5.469728,4.968960,9.419635,4.297471,2.436428,9.393990,9.107737,0.946431,4.365572,-3.150061,-3.121545,1.952196,9.620110,0.514005,9.835740,2.802812,-2.909753,5.306097,3.607322,4.486520,5.978812,5.017706,-7.343408,-1.087810,7.172420,8.766235,-1.959356,1.056097,8.482766,0.126459,-7.080634,9.120972,-9.404782,-0.459332,8.789297,-4.667801,-7.982278,5.337973,3.983756,-9.786972,-3.981070,-4.796257,-2.874831,-5.144892,-0.393279,8.890728,9.438016,-2.687358,8.925631,1.739117,-1.548123,-3.793859,1.833517,2.536481,8.827567,7.157294,-3.679052,-6.719470,7.256352,-1.605904,2.881994,-2.714817,-4.622151,-9.053219,1.941016,-8.678595,1.015193,-9.111742,-0.450706,7.832876,7.457373,-2.278735,6.002678,5.105187,6.020523,-7.158999,6.676589,2.535338,1.721299,1.520819,1.012812,-4.940436,-8.423352,7.748317,0.474527,-7.418256,5.597667,-7.930472,-0.525807,3.350245,4.927526,-2.191120,-4.568190,-3.439185,1.730711,-9.063168,1.505306,4.264888,9.095019,-6.767717,-1.321018,-7.906035,6.349372,-7.419851,-5.003575,-5.302231,2.555871,-2.969257,-9.218482,-5.646840,-5.917656,9.633404,4.963588,-9.602826,1.951271,6.641770,6.047279,-6.769930,-0.974889,-5.194715,-3.155791,-0.463911,0.472493,-1.057198,5.063628,2.155491,1.284119,7.843455,-5.397443,-9.811349,3.600141,8.241011,7.760299,7.402189,-9.502413,-2.720097,-3.777939,-8.402972,6.129576,-9.592577,7.263387,-3.218790,-3.300551,-8.804790,8.165072,-2.739808,-8.350585,-4.150490,7.843360,-1.099664,0.652795,8.887984,6.717882,-5.681066,-8.777129,-7.248002,-4.455606,-8.523233,-4.156097,5.086301,1.796185,-9.591228,6.743034,4.448480,2.830497,-6.497991,-8.071881,-4.392144,-3.275767,-4.972091,4.982530,-9.277168,-3.151812,-5.523546,1.968910,-3.578651,-9.143082,5.562603,1.151956,-0.253965,-0.218577,-9.955858,-2.323431,-4.962017,3.874271,0.820697,7.906886,-5.484629,0.478992,4.794661,8.898275,7.959259,-9.834431,2.382287,-0.026322,-0.824430,9.913358,9.427126,-8.304424,-4.791872,6.719403,-5.636046,8.241461,-9.837642,-3.684957,-6.570024,5.629505,0.766559,-8.153215,-4.502230,-2.490535,7.307206,6.751613,-5.946446,-5.152738,3.295175,-2.243525,9.760114,-6.177187,-5.416119,6.324068,-1.439130,0.911794,-9.103817,2.177010,-1.060839,-7.667422,2.756482,-0.762550,5.131298,-9.486665,-7.227274,-1.993708,-6.342624,3.149692,4.122780,4.834275,-1.074306,4.506077,-3.631870,8.219778,7.127569,-5.509517,0.707315,-4.497137,-8.788791,6.953002,3.273526,-8.556648,-2.975107,8.078536,-4.152484,-2.438381,8.918893,3.131011,-6.100621,-8.339695,-3.436858,-3.273495,1.461047], dtype = "float32")#candidate|1443|(297,)|const|float32
var_1444 = relay.var("var_1444", dtype = "int8", shape = (264,))#candidate|1444|(264,)|var|int8
call_1442 = relay.TupleGetItem(func_893_call(relay.reshape(const_1443.astype('float32'), [3, 11, 9]), relay.reshape(var_1444.astype('int8'), [264,]), ), 1)
call_1445 = relay.TupleGetItem(func_897_call(relay.reshape(const_1443.astype('float32'), [3, 11, 9]), relay.reshape(var_1444.astype('int8'), [264,]), ), 1)
func_1370_call = mod.get_global_var('func_1370')
func_1371_call = mutated_mod.get_global_var('func_1371')
call_1448 = relay.TupleGetItem(func_1370_call(), 0)
call_1449 = relay.TupleGetItem(func_1371_call(), 0)
uop_1468 = relay.atan(const_1443.astype('float32')) # shape=(297,)
func_1012_call = mod.get_global_var('func_1012')
func_1016_call = mutated_mod.get_global_var('func_1016')
var_1479 = relay.var("var_1479", dtype = "int8", shape = (1, 143))#candidate|1479|(1, 143)|var|int8
const_1480 = relay.const([-10,3,4,-2,8,-10,-6,6,3,1,7,4,6,7,2,1,-6,7,4,-2,-1,-9,-9,-3,3,4,6,3,3,-10,-1,8,7,9,7,8,-4,-7,4,-7,-7,-8,-9,5,-5,9,-7,-3,-4,-10,4,1,6,10,9,6,8,-9,7,9,8,-7,-4,-3,-5,-1,2,-6,1,8,-3,8,-10,-6,-10,8,2,-6,8,-7,4,-1,-2,-5,-2,5,-9,5,-9,-8,-6,10,4,6,-5,4,-3,-6,-1,-7,3,-8,-6,-4,4,5,-8,7,1,3,-8,-7,-1,5,-5,-7,-6,-3,-8,9,-8,-1,1,10,5,2,-2,4,2,-7,4,5,9,-4,6,-10,-10,-3,-2,5,-6,-1,-5,-2,-4,6,-5,8,1,-2,5,-1,4,8,-5,-3,9,1,-9,-1,-4,-9,-7,4,10,5,9,-2,10,-10,10,-7,-9,3,1,-9,10,-3,-8,9,2,-3,1,-3,5,5,-9,4,-1,6,-10,7,6,9,7,-1,-1,10,-2,-1,8,-10,-10,-5,-1,5,5,-3,3,4,-9,1,-9,-2,-3,6,10,-8,-4,3,5,9,9,-10,4,-2,-9,3,-3,-1,-9,-8,6,-9,-3,6,-10,8,6,10,4,-3,7,2,-2,-6,1,9,-4,-6,3,-2,6,10,8,4,-4,-6,4,10,-1,6,-10,9,-5,10,-6,9,-2,6,1,-3,-8,7,-7,9,-3,1,-1,-9,5,4,-2,5,-2,-6,-2,9,8,-3,2,4,-10,1,7,-8,9,-6,-5,-3,-4,1,7,-6,-5,-1,-5,-6,-2,-6,7,3,-8,-7,10,9,10,-9,-9,2,-8,-2,-10,7,7,2,9,-2,-4,1,10,9,-1,6,5,-5,3,-5,-8,-6,8,-9,-3,8,-9,-3,-9,6,1,8,-2,-9,2,7,-10,3,10,7,-2,-1,3,9,-4,-10,8,1,2,-4,-7,4,-3,5,10,7,8,4,-1,1,-1,2,-10,-1,6,7,-6,9,10,5,8,4,9,7,-3,9,1,5,-6,-4,-2,6,-3,-9,10,3,-5,6,-4,-8,-3,-1,8,-8,2,7,-6,-2,-9,-2,-7,7,-1,-8,9,-2,-2,-9,-10,-5,10,6,6,-4,1,3,10,-9,-4,8,2,-6,-4,5,3,-8,-5,-8,6,-5,8,4,10,1,-10,-9,-8,7,1,7,3,8,4,6,-8,7,-10,3,4,-6,-2,9,2,-3,-7,9,-8,5,-5,-1,5,-8,-9,-7,-7,-7,9,-1,1,4,-4,9,9,3,-6,-6,2,-6,-9,2,-7,8,-7,7,-1,-10,-5,7,3,-10,4,-10,2,-5,-2,-8,10,-6,-5,8,5,10,-7,4,7,-8,9,-9,-5,-3,-3,-7,9,1,6,9,-7,3,-6,-3,10,5,-1,-4,9,5,-10,-7,6,10,-9,-5,-8,2,5,6,-9,9,-7,10,8,-8,-8,7,4,7,-8,10,3,9,-9,5,8,-2,5,-1,-7,-5,-5,-10,2,10,2,-6,-4,-2,10,3,-1,4,-6,3,3,8,-10,7,-6,10,1,-2,10,9,1,-9,6,-10,-8,4,1,-1,2,1,-7,5,-8,2,-1,8,-3,-6,-8,-1,-1,10,-9,-3,7,9,6,1,-1,1,-1,3,6,3,8,-4,9,1,3,8,-7,-5,9,8,-6,-1,2,3,5,-5,9,10,-1,5,4,-5,10,-5,-5,-10,-5,-10,-7,6,8,-3,-9,5,5,-6,-5,9,1,6,-8,-7,-7,10,1,-6,-7,5,3,8,2,-6,-4,-4,-10,3,9,10,8,-10,8,-7,8,-1,-4,10,2,4,-2,5,1,7,-7,-5,-1,-5,4,1,3,-2,2,2,-7,-2,-7,10,-4,-9,6,-7,3,-5,3,9,-10,1,-3,8,1,1,-8,7,10,4,-2,-2,-2,-1,2,8,-1,6,4,-7,5,-3,1,-6,6,8,10,2,-6,6,3,4,3,-1,5,1,8,-4,4,1,-1,-5,-10,2,9,7,-1,5,10,-2,4,6,7,-2,-3,10,-5,-4,1,-10,-3,-2,8,10,-5,-5,-8,-2,3,8,10,-8,1,7,-8,-2,-6,7,4,-3,2,8,9,4,6,7,-10,-1,7,-4,-9,-7,-3,-10,-10,5,-9,1,-5,-9,9,-8,-1,9,-9,4,-9,4,3,-8,4,-6,-8,-2,-4,-7,9,9,6,-9,-10,4,1,-1,9,9,5,-8,-4,8,-5,8,-10,-5,6,-3,6,4,-7,-4,-4,-2,10,-2,2,2,-6,-1,-9,5,8,-2,7,-4,10,-1,-2,-3,-2,-7,-6,-2,-9,-9,7,4,3,-2,1,-7,3,-7,-2,7,7,10,5,4,-5,4,8,-9,-5,3,6,-9,7,-4,-8,5,-7,7,-7,7,5,-5,-3,-3,-7,6,-6,2,3,-2,-7,4,-2,-7,3,10,-7,-2,3,-1,-2,2,2,-1,10,-3,10,10,-8,10,2,1,9,2,-7,-10,9,-8,8,5,-5,-4,8,7,-2,9,-9,5,-2,-7,1,-1,-1,-3,-8,-6,9,-8,-1,-4,3,7,4,1,-1,6,-8,-4,5,10,6,-6,4,-1,-2,10,-8,1,-10,-7,-3,-5,-7,-1,-4,6,7,-4,-10,9,-2,9,-7,2,-3,2,-2,-6,-6,3,-8,-10,5,-7,1,-6,7,4,6,-3,5,-2,2,7,-4,8,1,8,-3,10,-3,8,-4,5,-8,-6,4,1,-5,-2,1,3,-7,10,10,-6,8,4,-6,-3,-5,-9,-8,-5,-1,4,-4,-5,-9,-10,7,-1,-10,9,4,-2,1,-10,-4,-4,9,-6,-4,-5,-6,-2,-3,-9,10,10,-2,-2,6,3,-6,-2,4,9,10,3,-9,10,7,-4,1,-10,-6,7,-6,-9,-9,7,-2,-1,10,-8,-8,10,10,-4,-8,6,-9,-8,-5,-9,-2,8,-5,-4,-3,-4,3,-8,-10,5,-7,3,-6,-4,10,7,-2,-3,6,-3,-2,-9,5,-7,10,-2,-5,-4,8,3,-1,-9,5,-1,-3,-9,-5,9,8,2,10,-4,1,-5,5,-8,-8,1,-2,4,9,10,4,4,7,-9,-2,-1,10,-3,-4,1,-9,-5,5,6,-3,-9,-6,-8,-1,-10,-9,-7,7,-5,-2,-4,1,3,9,3,6,10,5,4,6,-8,-7,7,8,8,10,-2,-1,8,-4,3,-3,1,4,5,-1,6,-9,-3,-5,-6,1,8,2,-2,-9,4,10,1,1,6,8,-10,-7,3,-4,-8,6,8,4,-4,-7,-6,-4,-2,4,6,2,-10,-3,-10,3,-3,-4,6,-3,2,9,-8,8,7,-10,3,-3,8,7,2,-5,-8,5,8,4,-7,-9,-5,7,-8,-9,10,5,5,-7,3,-1,1,-5,-6,-1,4,-10,-9,-3,5,-10,-3,2,-1,6,-10,-5,4,4,-10,3,-6,-5,9,4,1,8,2,-1,-10,7,3,-3,-1,-7,1,-7,10,-4,1,2,3,-7,9,-10,-4,-10,-8,-5,7,1,9,-7,-1,7,-8,-5,8,-9,-9,-7,5,-3,-10,1,-10,7,2,2,4,7,-10,-4,4,7,-2,10,4,10,2,3,-4,5,4,-9,-7,-2,-9,-5,-2,8,-9,-3,2,8,5,-9,-2,6,10,-6,-2,-3,-7,-3,3,4,2,6,1,9,5,-6,10,3,-7,-10,9,9,-4,-2,-4,8,4,-1,7,-10,7,9,7,-1,3,3,-5,-6,3,-5,-6,6,-8,-4,6,-7,-9,-10,6,-9,1,1,-4,-6,-4,-5,-3,-2,-7,-5,-10,4,7,-4,-5,4,-6,-5,-1,-7,-9,9,7,-4,6,5,-2,-5,-5,5,-5,10,-5,2,-4,-5,5,-9,-3,-7,2,7,3,4,5,1,-8,1,-6,1,6,-6,-8,-3,8,2,-2,-4,2,-6,-7,7,10,1,3,-7,-6,9,-8,6,4,5,-8,-2,7,9,7,-9,6,-2,-2,7,3,-3,-10,-8,9,-2,-2,-1,-4,-1,8,5,-2,4,-5,-1,9,-1,2,-5,1,-10,-4,2,-3,9,4,5,1,7,10,-6,1,10,-5,6,2,10,9,4,-4,-3,-8,-2,10,9], dtype = "int8")#candidate|1480|(1573,)|const|int8
call_1478 = relay.TupleGetItem(func_1012_call(relay.reshape(var_1479.astype('int8'), [143,]), relay.reshape(const_1480.astype('int8'), [1573,]), relay.reshape(var_1479.astype('int8'), [143,]), ), 2)
call_1481 = relay.TupleGetItem(func_1016_call(relay.reshape(var_1479.astype('int8'), [143,]), relay.reshape(const_1480.astype('int8'), [1573,]), relay.reshape(var_1479.astype('int8'), [143,]), ), 2)
func_1370_call = mod.get_global_var('func_1370')
func_1371_call = mutated_mod.get_global_var('func_1371')
call_1489 = relay.TupleGetItem(func_1370_call(), 0)
call_1490 = relay.TupleGetItem(func_1371_call(), 0)
uop_1493 = relay.asin(uop_1468.astype('float32')) # shape=(297,)
uop_1508 = relay.acosh(uop_1468.astype('float64')) # shape=(297,)
func_533_call = mod.get_global_var('func_533')
func_537_call = mutated_mod.get_global_var('func_537')
call_1513 = relay.TupleGetItem(func_533_call(relay.reshape(var_1479.astype('int8'), [11, 13, 1]), relay.reshape(const_1480.astype('int8'), [11, 13, 11]), ), 1)
call_1514 = relay.TupleGetItem(func_537_call(relay.reshape(var_1479.astype('int8'), [11, 13, 1]), relay.reshape(const_1480.astype('int8'), [11, 13, 11]), ), 1)
output = relay.Tuple([call_1383,call_1442,var_1444,call_1448,call_1478,var_1479,const_1480,call_1489,uop_1493,uop_1508,call_1513,])
output2 = relay.Tuple([call_1384,call_1445,var_1444,call_1449,call_1481,var_1479,const_1480,call_1490,uop_1493,uop_1508,call_1514,])
func_1529 = relay.Function([var_1444,var_1479,], output)
mod['func_1529'] = func_1529
mod = relay.transform.InferType()(mod)
mutated_mod['func_1529'] = func_1529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1529_call = mutated_mod.get_global_var('func_1529')
var_1531 = relay.var("var_1531", dtype = "int8", shape = (264,))#candidate|1531|(264,)|var|int8
var_1532 = relay.var("var_1532", dtype = "int8", shape = (1, 143))#candidate|1532|(1, 143)|var|int8
call_1530 = func_1529_call(var_1531,var_1532,)
output = call_1530
func_1533 = relay.Function([var_1531,var_1532,], output)
mutated_mod['func_1533'] = func_1533
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1535 = relay.var("var_1535", dtype = "float64", shape = (9, 4, 15))#candidate|1535|(9, 4, 15)|var|float64
var_1536 = relay.var("var_1536", dtype = "float64", shape = (9, 4, 15))#candidate|1536|(9, 4, 15)|var|float64
bop_1537 = relay.multiply(var_1535.astype('float64'), relay.reshape(var_1536.astype('float64'), relay.shape_of(var_1535))) # shape=(9, 4, 15)
output = relay.Tuple([bop_1537,])
output2 = relay.Tuple([bop_1537,])
func_1545 = relay.Function([var_1535,var_1536,], output)
mod['func_1545'] = func_1545
mod = relay.transform.InferType()(mod)
var_1546 = relay.var("var_1546", dtype = "float64", shape = (9, 4, 15))#candidate|1546|(9, 4, 15)|var|float64
var_1547 = relay.var("var_1547", dtype = "float64", shape = (9, 4, 15))#candidate|1547|(9, 4, 15)|var|float64
output = func_1545(var_1546,var_1547,)
func_1548 = relay.Function([var_1546,var_1547,], output)
mutated_mod['func_1548'] = func_1548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1355_call = mod.get_global_var('func_1355')
func_1356_call = mutated_mod.get_global_var('func_1356')
call_1597 = relay.TupleGetItem(func_1355_call(), 0)
call_1598 = relay.TupleGetItem(func_1356_call(), 0)
func_1361_call = mod.get_global_var('func_1361')
func_1363_call = mutated_mod.get_global_var('func_1363')
call_1603 = relay.TupleGetItem(func_1361_call(), 0)
call_1604 = relay.TupleGetItem(func_1363_call(), 0)
output = relay.Tuple([call_1597,call_1603,])
output2 = relay.Tuple([call_1598,call_1604,])
func_1620 = relay.Function([], output)
mod['func_1620'] = func_1620
mod = relay.transform.InferType()(mod)
mutated_mod['func_1620'] = func_1620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1620_call = mutated_mod.get_global_var('func_1620')
call_1621 = func_1620_call()
output = call_1621
func_1622 = relay.Function([], output)
mutated_mod['func_1622'] = func_1622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1319_call = mod.get_global_var('func_1319')
func_1320_call = mutated_mod.get_global_var('func_1320')
call_1626 = func_1319_call()
call_1627 = func_1319_call()
func_423_call = mod.get_global_var('func_423')
func_428_call = mutated_mod.get_global_var('func_428')
var_1639 = relay.var("var_1639", dtype = "int32", shape = ())#candidate|1639|()|var|int32
const_1640 = relay.const([-7,-5,10,-10,-1,-10,-6,-6,-7,-7,-4,8,-10,-5,4,-4,8,-1,-9,-5,-5,9,5,-10,-2,3,-2,5,-5,-4,-6,-9,10,-5,1,1,-9,7,-8,8,-4,7,-3,-7,-3,-7,-1,-5,6,-2,-4,-3,1,-6,-7,-10,5,-6,-10,-7,3,-3,-10,-7,-10,5,10,-6,-8,-2,7,5,-9,-2,-3,1,-5,-10,5,-3,-6,1,-6,7,-1,2,-10,2,9,8,5,8,8,-4,7,9,6,9,9,10,6,-10,9,6,7,10,7,-1,7,-7,-3,-8,-4,-4,3,-3,-6,-5,-6,-2,7,5,1,-9,1,3,-10,-4,-7,9,2,7,6,2,-5,5,8,7,5,-8,-4,2,-1,10,5,-8,-3,5,-8,-1,3,6,5,-3,-1,-7,-1,9,-5,1,-10,9,3,5,2,4,-4,-9,4,-9,2,-8,-7,6,-5,4,-4,-1,8,8,-5,-7,3,-8,-7,-9,-5,3,-3,-5,-6,6,-5,-8,-6,-3,1,8,6,-8,-4,-4,-6,-2,4,1,-8,1,-5,-6,-7,2,1,-1,-5,-1,-8,8,10,6,7,7,4,9,-8,2,6,-5,-3,3,5,-9,-1,-10,-6,8,-4,1,2,7,4,7,-3,-4,-7,6,-5,7,-1,6,3,-3,8,5,3,-1,-1,-5,-1,3,-10,-9,4,-10,5,2,-1,-3,8,-10,-9,-8,-9,9,3,-5,-8,9,-4,-7,-6,-5,6,5,-7,5,-6,-10,-7,3,10,-5,6,-10,-5,-7,8,8,-3,9,10,8,8,-10,-7,-5,5,-5,5,9,-4,1,-2,7,-3,-5,-10,-10,-3,1,7,6,7,-1,9,-2,-8,-9,3,-6,-2,-9,4,-1,4,-8,10,-1,5,1,3,1,6,4,5,6,-10,10,-8,2,2,1,4,-1,3,7,5,9,-7,3,-4,-9,-7,10,-9,5,4,5,7,7,8,-8,-1,8,-2,9,-1,-10,-9,-2,-5,-10,-3,5,1,-2,7,1,8,5,10,8,4,8,8,-2,8,-10,-4,-3,-8,-3,-6,4,-6,8,4,-7,-1,4,8,-4,7,-7,10,8,-4,4,7,-8,6,-1,9,3,-5,-3,4,-9,-1,3,-6,-1,2,-4,3,4,-5,4,-2,-6,-5,-2,-6,9,7,9,5,-6,5,-7,-10,-10,5,1,-10,-6,7,3,9,1,5,1,-1,-6,7,-7,-6,3,2,1,-2,8,-7,3,4,-3,-5,9,-1,2,-10,-4,7,-8,-3,2,7,5,10,9,-3,3,5,3,6,-4,6,3,-9,-6,-1,8,-10,-2,-2,-4,-1,2,-8,-4,2,-3,9,-6,8,-1,-10,-8,3,-1,-9,1,-4,8,9,8,-1,2,6,6,-7,4,-5,8,-2,-6,-5,-3,-3,-1,-2,-6,10,2,-5,2,7,-1,-10,-2,-1,-3,7,-3,6,3,-5,-2,-6,-2,5,6,4,4,-8,6,7,6,-5,6,-5,1,7,-6,10,-7,4,4,-1,-1,7,10,7,9,5,5,-4,9,-10,8,4,4,9,7,-8,-10,-6,-8,6,-4,3,-10,-6,10,-5,5,-4,-9,-6,-4,3,-9,4,-1,-7,9,6,8,-10,7,9,-7,10,-7,-10,-3,4,-3,1,7], dtype = "int32")#candidate|1640|(630,)|const|int32
const_1641 = relay.const([-7,7,1,6,-5,10,9,7,10,-8,10,5,10,-9,4,-5,1,10,1,7,-2,-9,-1,-8,4,4,-10,1,-6,9,2,-3,-7,-2,9,-8,10,-6,6,2,2,7,-6,1,9,-2,-5,-4,9,3,-9,1,-10,10,10,5,-9,-3,-9,9,-6,8,7,4,-10,-4,-7,8,-3,-1,-2,7,1,6,-6,-9,-5,4,1,-8,4,-1,8,-8,10,3,10,-1,10,10,-2,10,7,9,-1,-10,10,8,3,-8,9,-4,3,-7,-3,-9,-7,-4,5,4,-2,-3,-10,-4,-8,5,-6,-6,4,-2,-2,6,1,6,5,10,-6,4,5,-8,-10,10,-4,5,-10,9,-7,3,-4,2,1,-9,-6,-5,-8,-3,8,4,-10,1,3,3,-4,-8,5,8,-3,-5,9,-1,4,7,9,-3,-8,10,6,-5,-10,-9,-4,-1,5,7,7,-2,4,-1,1,-6,2,-4,1,-9,2,-6,-6,-3,-4,-6,8,9,9,9,-8,1,-10,6,-2,-10,2,3,4,8,6,-8,4,-8,-9,-3,9,7,-6,-1,-8,5,9,-10,3,1,-4,4,6,8,-1,2,-4,-1,2,1,5,1,-5,6,-1,-7,-6,10,7,7,1,-7,-6,7,2,-7,-5,2,-1,10,-7,-4,2,-7,4,-6,-1,9,-3,5,-6,2,-1,3], dtype = "int8")#candidate|1641|(264,)|const|int8
call_1638 = relay.TupleGetItem(func_423_call(relay.reshape(var_1639.astype('int32'), []), relay.reshape(const_1640.astype('int32'), [7, 9, 10]), relay.reshape(const_1641.astype('int8'), [264,]), ), 2)
call_1642 = relay.TupleGetItem(func_428_call(relay.reshape(var_1639.astype('int32'), []), relay.reshape(const_1640.astype('int32'), [7, 9, 10]), relay.reshape(const_1641.astype('int8'), [264,]), ), 2)
output = relay.Tuple([call_1626,call_1638,var_1639,const_1640,const_1641,])
output2 = relay.Tuple([call_1627,call_1642,var_1639,const_1640,const_1641,])
func_1647 = relay.Function([var_1639,], output)
mod['func_1647'] = func_1647
mod = relay.transform.InferType()(mod)
var_1648 = relay.var("var_1648", dtype = "int32", shape = ())#candidate|1648|()|var|int32
output = func_1647(var_1648)
func_1649 = relay.Function([var_1648], output)
mutated_mod['func_1649'] = func_1649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1370_call = mod.get_global_var('func_1370')
func_1371_call = mutated_mod.get_global_var('func_1371')
call_1661 = relay.TupleGetItem(func_1370_call(), 0)
call_1662 = relay.TupleGetItem(func_1371_call(), 0)
var_1663 = relay.var("var_1663", dtype = "float64", shape = (7, 9, 10))#candidate|1663|(7, 9, 10)|var|float64
bop_1664 = relay.floor_mod(call_1661.astype('float32'), relay.reshape(var_1663.astype('float32'), relay.shape_of(call_1661))) # shape=(7, 9, 10)
bop_1667 = relay.floor_mod(call_1662.astype('float32'), relay.reshape(var_1663.astype('float32'), relay.shape_of(call_1662))) # shape=(7, 9, 10)
func_244_call = mod.get_global_var('func_244')
func_246_call = mutated_mod.get_global_var('func_246')
var_1673 = relay.var("var_1673", dtype = "int8", shape = (264,))#candidate|1673|(264,)|var|int8
call_1672 = relay.TupleGetItem(func_244_call(relay.reshape(var_1673.astype('int8'), [4, 6, 11])), 0)
call_1674 = relay.TupleGetItem(func_246_call(relay.reshape(var_1673.astype('int8'), [4, 6, 11])), 0)
bop_1675 = relay.bitwise_xor(call_1661.astype('uint16'), relay.reshape(var_1663.astype('uint16'), relay.shape_of(call_1661))) # shape=(7, 9, 10)
bop_1678 = relay.bitwise_xor(call_1662.astype('uint16'), relay.reshape(var_1663.astype('uint16'), relay.shape_of(call_1662))) # shape=(7, 9, 10)
uop_1683 = relay.sigmoid(bop_1664.astype('float64')) # shape=(7, 9, 10)
uop_1685 = relay.sigmoid(bop_1667.astype('float64')) # shape=(7, 9, 10)
output = relay.Tuple([call_1672,var_1673,bop_1675,uop_1683,])
output2 = relay.Tuple([call_1674,var_1673,bop_1678,uop_1685,])
func_1688 = relay.Function([var_1663,var_1673,], output)
mod['func_1688'] = func_1688
mod = relay.transform.InferType()(mod)
var_1689 = relay.var("var_1689", dtype = "float64", shape = (7, 9, 10))#candidate|1689|(7, 9, 10)|var|float64
var_1690 = relay.var("var_1690", dtype = "int8", shape = (264,))#candidate|1690|(264,)|var|int8
output = func_1688(var_1689,var_1690,)
func_1691 = relay.Function([var_1689,var_1690,], output)
mutated_mod['func_1691'] = func_1691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1361_call = mod.get_global_var('func_1361')
func_1363_call = mutated_mod.get_global_var('func_1363')
call_1693 = relay.TupleGetItem(func_1361_call(), 0)
call_1694 = relay.TupleGetItem(func_1363_call(), 0)
var_1706 = relay.var("var_1706", dtype = "float64", shape = (6, 2, 14))#candidate|1706|(6, 2, 14)|var|float64
bop_1707 = relay.logical_or(call_1693.astype('bool'), var_1706.astype('bool')) # shape=(6, 2, 14)
bop_1710 = relay.logical_or(call_1694.astype('bool'), var_1706.astype('bool')) # shape=(6, 2, 14)
output = bop_1707
output2 = bop_1710
func_1714 = relay.Function([var_1706,], output)
mod['func_1714'] = func_1714
mod = relay.transform.InferType()(mod)
var_1715 = relay.var("var_1715", dtype = "float64", shape = (6, 2, 14))#candidate|1715|(6, 2, 14)|var|float64
output = func_1714(var_1715)
func_1716 = relay.Function([var_1715], output)
mutated_mod['func_1716'] = func_1716
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1752 = relay.var("var_1752", dtype = "float32", shape = (11, 8, 9))#candidate|1752|(11, 8, 9)|var|float32
uop_1753 = relay.asinh(var_1752.astype('float32')) # shape=(11, 8, 9)
func_1688_call = mod.get_global_var('func_1688')
func_1691_call = mutated_mod.get_global_var('func_1691')
var_1765 = relay.var("var_1765", dtype = "float64", shape = (630,))#candidate|1765|(630,)|var|float64
const_1766 = relay.const([6,4,-10,-7,-2,2,-3,-7,8,8,-10,10,-10,10,-7,-8,3,-8,8,3,-4,-6,-7,-4,10,-6,-6,10,-7,8,3,7,-7,-8,-2,6,5,-5,-5,-7,10,5,2,-3,-8,-1,6,-7,-2,-7,4,-2,-7,1,-5,-7,4,2,9,-4,-6,-8,-2,-5,-9,-1,-8,-6,-10,-7,7,-2,9,-8,-1,7,-5,2,-1,-4,-1,-7,-7,-4,-10,-2,6,-8,1,-5,-8,2,9,-3,-2,1,9,2,1,-3,-6,7,-2,-7,3,-5,-6,4,-4,-4,-1,2,4,-8,-8,5,-9,-8,-7,1,-8,-1,-5,10,2,-6,10,5,-9,-1,5,3,-10,2,-7,-7,1,-9,-3,-6,2,5,9,8,-4,-9,8,-10,4,-6,-7,5,-1,6,3,6,-5,9,-3,-4,-9,6,4,6,10,-8,-4,-6,-7,-8,6,10,-7,5,-8,-8,9,-4,10,10,3,8,1,4,-10,-10,6,-6,-9,-4,-10,-3,4,10,1,-5,-8,-2,9,-6,-8,-5,-8,-9,4,3,-4,10,8,-6,-2,3,-6,-8,1,-5,-2,-5,-3,-7,-8,10,-1,-3,-2,7,-10,5,-5,10,-9,-9,7,-3,-8,7,3,9,-10,2,-9,-8,-9,-4,8,-4,-1,9,-5,-8,5,9,3,-1,-8,6,9,-8,-1,-5,-10,-5,10,-1], dtype = "int8")#candidate|1766|(264,)|const|int8
call_1764 = relay.TupleGetItem(func_1688_call(relay.reshape(var_1765.astype('float64'), [7, 9, 10]), relay.reshape(const_1766.astype('int8'), [264,]), ), 3)
call_1767 = relay.TupleGetItem(func_1691_call(relay.reshape(var_1765.astype('float64'), [7, 9, 10]), relay.reshape(const_1766.astype('int8'), [264,]), ), 3)
func_1253_call = mod.get_global_var('func_1253')
func_1255_call = mutated_mod.get_global_var('func_1255')
call_1768 = relay.TupleGetItem(func_1253_call(relay.reshape(const_1766.astype('int8'), [264,])), 3)
call_1769 = relay.TupleGetItem(func_1255_call(relay.reshape(const_1766.astype('int8'), [264,])), 3)
output = relay.Tuple([uop_1753,call_1764,var_1765,const_1766,call_1768,])
output2 = relay.Tuple([uop_1753,call_1767,var_1765,const_1766,call_1769,])
func_1771 = relay.Function([var_1752,var_1765,], output)
mod['func_1771'] = func_1771
mod = relay.transform.InferType()(mod)
mutated_mod['func_1771'] = func_1771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1771_call = mutated_mod.get_global_var('func_1771')
var_1773 = relay.var("var_1773", dtype = "float32", shape = (11, 8, 9))#candidate|1773|(11, 8, 9)|var|float32
var_1774 = relay.var("var_1774", dtype = "float64", shape = (630,))#candidate|1774|(630,)|var|float64
call_1772 = func_1771_call(var_1773,var_1774,)
output = call_1772
func_1775 = relay.Function([var_1773,var_1774,], output)
mutated_mod['func_1775'] = func_1775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1083_call = mod.get_global_var('func_1083')
func_1085_call = mutated_mod.get_global_var('func_1085')
call_1803 = relay.TupleGetItem(func_1083_call(), 6)
call_1804 = relay.TupleGetItem(func_1085_call(), 6)
func_1714_call = mod.get_global_var('func_1714')
func_1716_call = mutated_mod.get_global_var('func_1716')
var_1806 = relay.var("var_1806", dtype = "float64", shape = (168,))#candidate|1806|(168,)|var|float64
call_1805 = func_1714_call(relay.reshape(var_1806.astype('float64'), [6, 2, 14]))
call_1807 = func_1714_call(relay.reshape(var_1806.astype('float64'), [6, 2, 14]))
func_839_call = mod.get_global_var('func_839')
func_841_call = mutated_mod.get_global_var('func_841')
call_1827 = relay.TupleGetItem(func_839_call(), 2)
call_1828 = relay.TupleGetItem(func_841_call(), 2)
output = relay.Tuple([call_1803,call_1805,var_1806,call_1827,])
output2 = relay.Tuple([call_1804,call_1807,var_1806,call_1828,])
func_1829 = relay.Function([var_1806,], output)
mod['func_1829'] = func_1829
mod = relay.transform.InferType()(mod)
mutated_mod['func_1829'] = func_1829
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1830 = relay.var("var_1830", dtype = "float64", shape = (168,))#candidate|1830|(168,)|var|float64
func_1829_call = mutated_mod.get_global_var('func_1829')
call_1831 = func_1829_call(var_1830)
output = call_1831
func_1832 = relay.Function([var_1830], output)
mutated_mod['func_1832'] = func_1832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1370_call = mod.get_global_var('func_1370')
func_1371_call = mutated_mod.get_global_var('func_1371')
call_1850 = relay.TupleGetItem(func_1370_call(), 0)
call_1851 = relay.TupleGetItem(func_1371_call(), 0)
output = call_1850
output2 = call_1851
func_1859 = relay.Function([], output)
mod['func_1859'] = func_1859
mod = relay.transform.InferType()(mod)
output = func_1859()
func_1860 = relay.Function([], output)
mutated_mod['func_1860'] = func_1860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1859_call = mod.get_global_var('func_1859')
func_1860_call = mutated_mod.get_global_var('func_1860')
call_1861 = func_1859_call()
call_1862 = func_1859_call()
func_893_call = mod.get_global_var('func_893')
func_897_call = mutated_mod.get_global_var('func_897')
const_1864 = relay.const([[0.994747,-4.564262,-7.757696,-5.488179,3.657231,5.866330,-6.827312,6.301476,-9.812341],[0.344558,8.461004,6.151213,2.937125,9.064448,-6.282804,4.811304,7.462011,6.977361],[-6.719853,9.904373,-5.960115,9.109984,-5.397083,-8.306292,-3.500731,-7.282929,-4.901046],[9.518128,-3.039291,-9.234451,0.277946,-8.045234,0.189706,-5.770270,-4.622525,5.041779],[-0.270324,6.377206,9.579070,-8.125597,1.086136,8.299565,-8.347044,-9.199076,-4.578274],[1.994054,-7.943330,-3.491200,9.433769,-5.329860,-5.151113,-3.658389,-2.461888,4.618214],[5.861352,2.836613,-8.966970,1.402871,-8.952236,-9.395371,-5.425950,-7.665940,8.726205],[-2.589208,2.616615,-1.097004,-5.226356,-8.784019,-8.381588,-6.649075,5.299436,5.188980],[9.372944,-7.902785,-3.061189,-3.649873,-4.091774,2.583546,8.991267,-8.119952,-1.423436],[-0.972577,-4.513132,0.907790,-8.370094,-7.764397,-5.903695,-5.455179,-4.589618,4.172797],[5.585353,1.254810,-4.656851,4.434912,-9.343156,-2.365353,3.237916,8.484185,6.545088],[-7.538938,6.460061,-9.192970,-1.408606,7.108573,5.890024,6.703005,-3.679363,6.508389],[-1.830327,-1.521283,-5.958282,8.791678,8.455148,5.386475,-6.892687,-8.277170,0.277642],[1.062194,3.536523,-5.897410,4.619617,8.597456,0.897798,-8.405566,-3.210621,-4.851600],[6.171735,-9.677573,0.146873,5.082292,7.939430,4.137869,-6.669350,2.156199,7.293379],[4.246577,9.302235,-9.933803,8.087735,-8.793305,4.328855,-0.679727,5.062191,2.438306],[0.105125,-5.769868,-6.517435,8.381588,-1.461476,7.746051,-7.231878,-1.249008,6.467032],[-3.270285,3.180809,-6.177454,-5.305937,4.710074,2.915307,-4.438457,5.263622,-6.856138],[-3.859264,0.454039,-4.052194,-4.511055,0.774061,-9.351368,4.725352,6.091289,-0.946192],[0.979267,-8.286559,-0.380798,3.911125,-8.469487,6.340977,-1.771462,-5.173675,-6.789819],[-2.571490,-8.793579,2.651896,2.361955,8.909475,4.103798,-2.801634,-7.259333,4.873231],[2.026183,2.572785,9.978891,-8.919656,-6.113581,7.452728,5.488983,9.882852,9.742949],[-8.628265,4.346148,5.540685,2.125272,0.759322,2.658078,-5.442344,6.318324,-2.344851],[-9.214296,9.341749,-0.588110,9.183298,-3.450524,0.660657,6.164646,-7.392483,1.475135],[8.596225,-4.202953,5.746470,1.184507,-6.070540,6.969233,-2.165560,3.460635,3.106905],[-8.435438,6.819076,3.522953,3.107948,-3.262206,-4.035535,6.630071,6.455421,-7.455217],[1.785741,-8.219420,3.884531,8.443039,-9.097718,5.602593,-8.990750,-1.737315,-4.520860],[-9.460108,8.384060,-5.184474,-9.618254,5.608447,0.928268,-8.298226,-3.479123,-3.859353],[6.320326,6.307690,-7.086459,1.106417,-5.640317,-2.474622,3.191000,-0.220478,3.671384],[-3.764969,9.983996,9.448769,-2.692525,9.906674,6.715415,-6.875292,9.229367,-2.242349],[-8.877102,-9.843878,1.514640,8.479706,5.362798,1.665031,-6.857978,8.220074,-9.261089],[-6.277757,-7.795210,2.729717,6.420587,-7.628743,2.921391,-5.232443,-8.275197,-2.423982],[6.401473,0.142142,-2.144564,-2.282190,-6.734549,-6.280366,-7.536794,3.513118,-6.748787]], dtype = "float32")#candidate|1864|(33, 9)|const|float32
var_1865 = relay.var("var_1865", dtype = "int8", shape = (264,))#candidate|1865|(264,)|var|int8
call_1863 = relay.TupleGetItem(func_893_call(relay.reshape(const_1864.astype('float32'), [3, 11, 9]), relay.reshape(var_1865.astype('int8'), [264,]), ), 3)
call_1866 = relay.TupleGetItem(func_897_call(relay.reshape(const_1864.astype('float32'), [3, 11, 9]), relay.reshape(var_1865.astype('int8'), [264,]), ), 3)
bop_1867 = relay.equal(const_1864.astype('bool'), relay.reshape(call_1863.astype('bool'), relay.shape_of(const_1864))) # shape=(33, 9)
bop_1870 = relay.equal(const_1864.astype('bool'), relay.reshape(call_1866.astype('bool'), relay.shape_of(const_1864))) # shape=(33, 9)
output = relay.Tuple([call_1861,var_1865,bop_1867,])
output2 = relay.Tuple([call_1862,var_1865,bop_1870,])
func_1871 = relay.Function([var_1865,], output)
mod['func_1871'] = func_1871
mod = relay.transform.InferType()(mod)
mutated_mod['func_1871'] = func_1871
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1872 = relay.var("var_1872", dtype = "int8", shape = (264,))#candidate|1872|(264,)|var|int8
func_1871_call = mutated_mod.get_global_var('func_1871')
call_1873 = func_1871_call(var_1872)
output = call_1873
func_1874 = relay.Function([var_1872], output)
mutated_mod['func_1874'] = func_1874
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1259_call = mod.get_global_var('func_1259')
func_1260_call = mutated_mod.get_global_var('func_1260')
call_1909 = relay.TupleGetItem(func_1259_call(), 0)
call_1910 = relay.TupleGetItem(func_1260_call(), 0)
func_1286_call = mod.get_global_var('func_1286')
func_1289_call = mutated_mod.get_global_var('func_1289')
var_1937 = relay.var("var_1937", dtype = "float64", shape = (336,))#candidate|1937|(336,)|var|float64
call_1936 = func_1286_call(relay.reshape(var_1937.astype('float64'), [12, 7, 4]))
call_1938 = func_1286_call(relay.reshape(var_1937.astype('float64'), [12, 7, 4]))
func_1529_call = mod.get_global_var('func_1529')
func_1533_call = mutated_mod.get_global_var('func_1533')
var_1948 = relay.var("var_1948", dtype = "int8", shape = (264,))#candidate|1948|(264,)|var|int8
var_1949 = relay.var("var_1949", dtype = "int8", shape = (143,))#candidate|1949|(143,)|var|int8
call_1947 = relay.TupleGetItem(func_1529_call(relay.reshape(var_1948.astype('int8'), [264,]), relay.reshape(var_1949.astype('int8'), [1, 143]), ), 1)
call_1950 = relay.TupleGetItem(func_1533_call(relay.reshape(var_1948.astype('int8'), [264,]), relay.reshape(var_1949.astype('int8'), [1, 143]), ), 1)
func_423_call = mod.get_global_var('func_423')
func_428_call = mutated_mod.get_global_var('func_428')
var_1963 = relay.var("var_1963", dtype = "int32", shape = ())#candidate|1963|()|var|int32
call_1962 = relay.TupleGetItem(func_423_call(relay.reshape(var_1963.astype('int32'), []), relay.reshape(call_1909.astype('int32'), [7, 9, 10]), relay.reshape(var_1948.astype('int8'), [264,]), ), 1)
call_1964 = relay.TupleGetItem(func_428_call(relay.reshape(var_1963.astype('int32'), []), relay.reshape(call_1909.astype('int32'), [7, 9, 10]), relay.reshape(var_1948.astype('int8'), [264,]), ), 1)
func_423_call = mod.get_global_var('func_423')
func_428_call = mutated_mod.get_global_var('func_428')
call_1968 = relay.TupleGetItem(func_423_call(relay.reshape(var_1963.astype('int32'), []), relay.reshape(call_1909.astype('int32'), [7, 9, 10]), relay.reshape(call_1947.astype('int8'), [264,]), ), 0)
call_1969 = relay.TupleGetItem(func_428_call(relay.reshape(var_1963.astype('int32'), []), relay.reshape(call_1909.astype('int32'), [7, 9, 10]), relay.reshape(call_1947.astype('int8'), [264,]), ), 0)
func_1771_call = mod.get_global_var('func_1771')
func_1775_call = mutated_mod.get_global_var('func_1775')
var_1972 = relay.var("var_1972", dtype = "float32", shape = (792,))#candidate|1972|(792,)|var|float32
call_1971 = relay.TupleGetItem(func_1771_call(relay.reshape(var_1972.astype('float32'), [11, 8, 9]), relay.reshape(call_1968.astype('float64'), [630,]), ), 0)
call_1973 = relay.TupleGetItem(func_1775_call(relay.reshape(var_1972.astype('float32'), [11, 8, 9]), relay.reshape(call_1968.astype('float64'), [630,]), ), 0)
output = relay.Tuple([call_1909,call_1936,var_1937,call_1947,var_1948,var_1949,call_1962,var_1963,call_1968,call_1971,var_1972,])
output2 = relay.Tuple([call_1910,call_1938,var_1937,call_1950,var_1948,var_1949,call_1964,var_1963,call_1969,call_1973,var_1972,])
func_1983 = relay.Function([var_1937,var_1948,var_1949,var_1963,var_1972,], output)
mod['func_1983'] = func_1983
mod = relay.transform.InferType()(mod)
var_1984 = relay.var("var_1984", dtype = "float64", shape = (336,))#candidate|1984|(336,)|var|float64
var_1985 = relay.var("var_1985", dtype = "int8", shape = (264,))#candidate|1985|(264,)|var|int8
var_1986 = relay.var("var_1986", dtype = "int8", shape = (143,))#candidate|1986|(143,)|var|int8
var_1987 = relay.var("var_1987", dtype = "int32", shape = ())#candidate|1987|()|var|int32
var_1988 = relay.var("var_1988", dtype = "float32", shape = (792,))#candidate|1988|(792,)|var|float32
output = func_1983(var_1984,var_1985,var_1986,var_1987,var_1988,)
func_1989 = relay.Function([var_1984,var_1985,var_1986,var_1987,var_1988,], output)
mutated_mod['func_1989'] = func_1989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1112_call = mod.get_global_var('func_1112')
func_1114_call = mutated_mod.get_global_var('func_1114')
call_2047 = relay.TupleGetItem(func_1112_call(), 2)
call_2048 = relay.TupleGetItem(func_1114_call(), 2)
const_2053 = relay.const([8,-1,-5,2,-10,1,-9,5,-10,-3,-1,10,5,7,-4,-7,-8,-3,1,-7,6,-4,-1,-7,6,-4,2,-2,-7,-6,-3,-5,-1,6,-2,3,-10,-2,-6,10,8,8,7,4,10,-8,3,5,-2,6,-3,3,-5,-2,4,4,7,10,3,-9,6,-9,-9,-4,5,-6,-10,4,3,-10,-10,-9,-6,1,4,2,5,2,-6,-6,10,-3,-10,8,3,-10,-2,-1,9,8,2,-5,3,-3,-6,2,-3,-6,4,-6,-4,1,5,-4,4,8,-4,-6,-10,6,10,-2,4,3,6,6,-6,-5,9,-5,-3,-2,8,4,7,-6,9,-7,7,-3,-1,-4,4,-2,-1,7,-2,3,-4,-7,-4,-7,2,5,6,-4,-7,-8,10,-5,6,6,-10,7,-3,-5,9,1,-6,1,-6,-10,5,-3,7,3,9,-3,-8,3,5,8,9,-5,6,8,-3,5,8,1,4,-1,5,2,-2,-5,-10,-3,4,4,4,-2,-10,-2,-4,4,-9,1,-8,-7,5,-9,7,-5,-10,1,-3,-8,9,-3,-3,1,3,7,-4,-4,-6,-7,5,-4,-3,8,9,10,7,10,-2,3,-4,7,-5,-10,-3,6,9,6,8,-9,-9,-4,6,-8,7,-4,-2,-3,-3,9,-10,-8,8,2,-6,-10,3,5,8,-8,5,-7,4,-5,3,-4], dtype = "int8")#candidate|2053|(264,)|const|int8
bop_2054 = relay.less(call_2047.astype('bool'), relay.reshape(const_2053.astype('bool'), relay.shape_of(call_2047))) # shape=(264,)
bop_2057 = relay.less(call_2048.astype('bool'), relay.reshape(const_2053.astype('bool'), relay.shape_of(call_2048))) # shape=(264,)
func_1620_call = mod.get_global_var('func_1620')
func_1622_call = mutated_mod.get_global_var('func_1622')
call_2061 = relay.TupleGetItem(func_1620_call(), 1)
call_2062 = relay.TupleGetItem(func_1622_call(), 1)
func_1688_call = mod.get_global_var('func_1688')
func_1691_call = mutated_mod.get_global_var('func_1691')
const_2066 = relay.const([-1.205594,3.611570,-0.693607,5.200355,3.015098,-9.225061,0.500668,6.621273,0.905751,-6.349882,3.115929,-9.230196,-5.049721,5.234782,-6.491602,5.544487,-0.047830,-5.621033,-5.155749,0.855492,-1.296242,7.216382,-1.024886,1.415007,1.352197,-2.300843,-8.655307,9.019767,0.325963,1.935160,-3.529390,-9.978538,9.525605,6.592277,-7.412178,7.342141,-6.534559,1.717928,0.814205,-4.021341,-1.706709,3.851332,-5.507412,-6.953818,7.859083,1.713285,-2.774469,-1.206583,-0.212003,7.780350,-3.525578,0.373563,8.518681,-8.974186,8.293121,2.185258,6.866340,1.394445,5.666973,4.959592,4.541063,-4.841445,-3.106427,4.692507,-4.216078,7.420960,-1.318122,0.261329,3.808870,-9.709484,0.273217,0.155842,6.180823,-4.932328,-3.577340,8.998862,-2.981377,0.334359,7.472746,9.023015,7.483481,-4.835892,-0.891229,9.593556,1.050289,-3.377587,5.901001,7.050818,-9.073698,2.730967,4.609693,-2.137728,-0.608013,-5.314979,9.322619,8.206563,5.933990,-6.736001,2.429677,5.695553,9.259218,8.759948,7.355348,0.052120,-1.806805,-3.890561,-7.922110,0.116856,-0.728090,-3.349950,-8.290157,-3.549611,3.342834,9.699376,-8.926926,-9.258991,-3.811836,-2.685971,-5.446524,-5.327828,-7.180819,5.464821,8.449797,0.049652,-7.981429,9.865541,9.691073,-7.074499,-9.897026,-7.047217,1.421794,8.685287,-0.787184,2.546306,9.362637,-6.730841,0.149224,-6.324225,-6.862420,-3.807007,6.704748,9.088653,-2.415731,-5.551210,5.124768,2.387742,6.076440,7.448417,0.462794,-9.035915,-9.132780,-4.955983,-4.930158,-5.675269,4.639569,-6.579038,8.364398,9.545083,5.903728,-1.310142,-6.861163,7.823338,-1.640798,-8.840803,-2.073534,3.848712,3.809865,-6.427607,-5.987171,-1.269466,0.319385,0.580956,0.626083,-6.325998,-1.225762,6.191924,8.192605,-0.646137,6.614902,3.574634,2.564359,-6.535029,-7.445960,2.081811,-2.881868,-1.852611,-7.642086,-6.541360,6.221229,-7.467391,4.797044,-2.435785,8.510246,9.088619,0.485479,-1.433299,6.804941,8.459402,3.966180,-1.210688,2.701847,7.588063,-4.714669,1.026290,3.198301,2.789229,5.078496,9.867704,-3.683086,-4.834535,9.044546,4.761049,1.562735,-6.725867,6.513244,-6.892356,-4.019758,-2.721276,5.933130,-1.798813,9.684237,-5.613073,6.249717,0.659347,-9.139681,-1.742562,-7.792023,-9.600395,-3.255658,-3.201025,8.472256,-4.688214,0.969544,8.118295,-5.360340,1.468206,0.825432,9.256610,7.110997,1.390924,-1.176942,1.175061,9.405556,-8.786742,-8.027888,6.897302,-3.698652,8.568385,-8.633785,-0.289301,-6.403237,-8.312573,0.958586,0.514335,7.599948,-6.614300,-6.201757,-3.548636,4.289574,0.976171,-1.792372,-1.472287,0.339400,-5.119274,-7.045189,-6.515182,-3.641016,-1.515636,-5.321318,-2.956379,-5.106889,3.622275,-2.062682,-3.781695,0.915061,3.087905,-4.660403,-7.890417,-0.152447,0.133494,1.654353,5.831538,4.733986,-8.551999,4.487633,1.016225,8.673738,-7.588060,-6.385461,-9.588880,2.237439,3.935718,6.948199,7.457655,-3.858416,-4.936137,-8.545873,6.149068,1.520627,-0.862144,-2.898252,7.443268,-9.190542,1.921241,-4.695753,-8.590499,-4.608185,-8.533696,3.356860,6.300943,-4.514823,-2.770919,1.007421,-0.895460,2.528500,-3.610637,-0.975162,2.244530,8.593670,-8.787197,-6.020517,6.710297,-0.269527,-8.368181,1.201890,-7.717939,4.568900,8.586284,-3.962776,-8.825925,-6.685371,-9.876779,-4.404708,7.495281,-4.473588,9.898069,6.800875,1.670489,-1.332268,9.445314,7.340843,-1.724553,-1.395586,-3.161391,8.282363,-2.881510,2.747307,1.365415,9.268842,3.401050,-7.642553,-7.946607,-0.928268,4.939136,-0.751061,-4.673202,-1.512032,-1.919575,-4.053674,-1.483058,0.507917,5.820912,8.411025,-1.987585,-2.703358,-3.936864,8.512543,-2.179699,4.446896,-0.300504,-1.022648,4.703497,3.500801,-4.427235,-6.992577,-8.894873,4.220110,-7.626260,-1.265448,6.658756,0.954507,6.485177,2.010061,-6.211584,6.914130,-2.985513,7.823478,6.479727,4.976484,9.116009,-3.532966,-5.901502,9.079680,-1.663937,2.457647,-4.290517,7.883247,0.881083,2.657625,4.355023,0.243323,2.205102,-8.539656,0.197908,-3.636691,0.778539,-3.631979,-8.919273,1.101438,0.352458,2.717091,3.277671,5.537050,0.962827,-3.161816,-9.481715,-3.138731,-4.027105,-3.890340,-6.424872,-1.995075,5.661279,1.845583,7.999064,-1.497038,-5.641910,-1.328810,-9.226368,-6.897468,2.129205,3.208475,-7.660160,6.312410,-3.492603,8.185393,-9.980759,-1.666925,-2.323091,8.555015,-9.420959,3.428003,3.493591,-7.836265,5.590905,3.179330,1.993478,-3.731497,-7.648027,7.362534,1.208062,-4.572097,-6.536035,1.430362,-0.258134,-4.189109,-6.677969,0.476819,-9.976764,-7.727885,9.720152,-3.682969,-6.792060,-7.878063,-7.118774,4.421308,-0.097083,9.515674,-0.862316,-3.866805,1.512818,-5.159609,-8.825339,-1.459625,7.357213,-0.122723,-7.551624,-3.782039,-7.734686,-0.434699,-2.957391,-0.855135,7.867194,0.282525,4.406024,-0.028371,0.403843,-2.313052,4.226141,-0.456871,8.817741,4.646469,0.311438,-6.887818,-5.418083,-6.241453,-1.866089,-2.149598,-6.615592,-9.070909,5.059248,-2.680165,3.878673,-7.742163,1.336097,4.705418,4.106303,2.483652,-7.198827,-0.031538,-2.811469,3.721310,-0.969796,-1.771095,-9.009921,-4.681822,4.002037,-3.481834,6.716865,5.414541,7.011341,-7.531385,8.470457,3.067118,0.016986,6.128600,-6.168649,1.725100,-2.230293,4.434056,-3.116424,-7.475359,-7.752958,-1.485079,9.077456,6.971025,-2.479881,2.583679,5.259632,-3.380524,5.241064,-5.930738,-8.316658,-0.409398,4.592591,1.289150,4.202264,9.360697,-0.259820,2.891684,-9.728043,-4.112484,-1.510134,-7.830968,-4.593164,1.730461,-6.095730,7.875274,5.402599,1.839645,2.806558,-8.892447,-7.115179,1.230603,5.134346,-5.127757,1.423047,-8.328877,8.461762,6.653663,0.014579,1.698980,-9.070179,1.071705,-1.091312,-1.706851,1.678207,-9.182443,-4.523096,8.211568,-0.507499,2.829020,-1.340310,-1.269405,6.823358,-0.345890,-8.600563,-1.828557,-7.999253,-9.876315,3.164506,3.704259,7.659037,-1.313212,7.906672,9.521279,-6.576452,1.345220,-5.561726,-2.815650,6.979977,9.819584,-1.757628,-4.067307,4.175048,7.456179,5.310108,7.215822,-1.970937,-3.513682,8.108860,6.350995,6.250263,2.514862,-6.508260,0.784657,-6.743738,3.313416,-9.478690,0.055041,-5.508072,-8.589675,5.718766,-5.034322,-8.699383,7.650834,-8.892465,3.692345,0.190063,-9.149463,-6.211423], dtype = "float64")#candidate|2066|(630,)|const|float64
call_2065 = relay.TupleGetItem(func_1688_call(relay.reshape(const_2066.astype('float64'), [7, 9, 10]), relay.reshape(bop_2054.astype('int8'), [264,]), ), 3)
call_2067 = relay.TupleGetItem(func_1691_call(relay.reshape(const_2066.astype('float64'), [7, 9, 10]), relay.reshape(bop_2054.astype('int8'), [264,]), ), 3)
func_1529_call = mod.get_global_var('func_1529')
func_1533_call = mutated_mod.get_global_var('func_1533')
var_2073 = relay.var("var_2073", dtype = "int8", shape = (143,))#candidate|2073|(143,)|var|int8
call_2072 = relay.TupleGetItem(func_1529_call(relay.reshape(call_2047.astype('int8'), [264,]), relay.reshape(var_2073.astype('int8'), [1, 143]), ), 7)
call_2074 = relay.TupleGetItem(func_1533_call(relay.reshape(call_2047.astype('int8'), [264,]), relay.reshape(var_2073.astype('int8'), [1, 143]), ), 7)
output = relay.Tuple([bop_2054,call_2061,call_2065,const_2066,call_2072,var_2073,])
output2 = relay.Tuple([bop_2057,call_2062,call_2067,const_2066,call_2074,var_2073,])
func_2099 = relay.Function([var_2073,], output)
mod['func_2099'] = func_2099
mod = relay.transform.InferType()(mod)
mutated_mod['func_2099'] = func_2099
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2100 = relay.var("var_2100", dtype = "int8", shape = (143,))#candidate|2100|(143,)|var|int8
func_2099_call = mutated_mod.get_global_var('func_2099')
call_2101 = func_2099_call(var_2100)
output = call_2101
func_2102 = relay.Function([var_2100], output)
mutated_mod['func_2102'] = func_2102
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2144 = relay.var("var_2144", dtype = "float64", shape = (14, 4, 4))#candidate|2144|(14, 4, 4)|var|float64
var_2145 = relay.var("var_2145", dtype = "float64", shape = (14, 4, 4))#candidate|2145|(14, 4, 4)|var|float64
bop_2146 = relay.divide(var_2144.astype('float64'), relay.reshape(var_2145.astype('float64'), relay.shape_of(var_2144))) # shape=(14, 4, 4)
bop_2170 = relay.bitwise_or(var_2144.astype('uint32'), relay.reshape(bop_2146.astype('uint32'), relay.shape_of(var_2144))) # shape=(14, 4, 4)
output = relay.Tuple([bop_2170,])
output2 = relay.Tuple([bop_2170,])
func_2174 = relay.Function([var_2144,var_2145,], output)
mod['func_2174'] = func_2174
mod = relay.transform.InferType()(mod)
var_2175 = relay.var("var_2175", dtype = "float64", shape = (14, 4, 4))#candidate|2175|(14, 4, 4)|var|float64
var_2176 = relay.var("var_2176", dtype = "float64", shape = (14, 4, 4))#candidate|2176|(14, 4, 4)|var|float64
output = func_2174(var_2175,var_2176,)
func_2177 = relay.Function([var_2175,var_2176,], output)
mutated_mod['func_2177'] = func_2177
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2195 = relay.const([[[-0.346657,-1.594659,-3.549364,-4.383554],[4.474154,5.440980,-2.932727,0.263473],[0.125704,8.752633,9.200401,-0.186137],[-2.532304,-7.153420,6.639424,9.160869],[6.134525,-2.165096,9.824178,1.529543],[9.378296,3.028916,-6.822594,8.677342]],[[4.195197,-7.649577,-1.077571,1.319175],[3.986459,1.848378,7.345758,-1.992915],[6.565959,-8.489228,3.519345,4.742646],[-4.644367,9.637450,-1.677188,3.970820],[6.747156,-5.249554,-5.832589,6.475700],[-6.457951,-2.928468,5.129988,-6.642603]],[[-0.235416,-5.855595,-3.288814,-7.862610],[-4.637429,-5.776653,-9.802382,-2.552037],[2.204963,0.257800,-7.026711,0.234088],[-4.003521,-5.671293,-7.644113,-0.628920],[-3.986518,8.256842,-0.054468,3.291904],[3.879414,5.757825,6.353046,6.885504]],[[0.922392,4.629227,9.564634,-7.779637],[-2.293171,-5.601503,0.822863,5.694496],[3.410598,7.778244,-0.482962,-5.007245],[-2.924816,1.448760,0.578255,-2.104932],[-6.634599,0.065967,-7.462690,0.820425],[-9.383832,6.917525,-5.713366,7.174723]],[[6.171414,8.414172,-2.366099,2.367870],[-7.425411,-8.236739,-2.177177,-9.146552],[-4.113814,-4.496300,6.144372,-4.822231],[3.234751,3.024339,-9.440587,1.221206],[6.859362,-2.050414,-8.917195,-6.175857],[-3.641875,9.221814,9.174138,8.765147]],[[7.930907,-4.123151,4.861293,-0.420208],[8.570398,-8.658991,9.568638,2.504041],[6.617169,-6.079273,-9.648890,-2.404738],[0.758082,2.849228,5.899163,9.852776],[-9.723179,3.091089,-9.270659,5.128892],[6.315713,8.087813,5.495792,-8.487083]],[[-3.968876,3.040224,4.991429,-3.842558],[7.070178,-7.306723,-2.626403,0.926371],[4.237170,5.040830,-8.447314,2.895304],[-9.884481,-3.452065,-9.372323,-3.713648],[3.924321,1.183363,1.293208,-6.702986],[2.493639,3.666830,-0.907409,-6.827955]],[[3.047421,2.615698,-7.158958,-6.182404],[7.109483,1.473609,5.559860,8.775517],[8.025929,1.624928,-2.829544,3.091027],[-0.306786,9.020046,9.820833,0.761648],[6.832217,-1.576046,6.403447,9.433706],[-9.370556,-2.803947,-5.350287,-3.646121]],[[-8.102249,0.923100,3.473361,-5.335239],[5.835262,-7.829790,-6.278676,-0.177770],[-8.836900,7.741414,5.028203,8.020735],[8.281825,9.149042,7.214940,8.925582],[0.477293,-3.103774,8.805031,3.784105],[-4.888283,8.315732,7.071569,6.677726]],[[0.379523,0.638376,9.204420,-3.023207],[6.552902,-0.285122,9.540294,-2.520270],[-8.919995,-3.208068,-2.138212,3.322114],[6.158126,8.842928,-4.535122,2.410614],[1.298698,-5.207501,6.035186,-5.718802],[-4.954870,4.167740,-6.988392,-2.017434]],[[-0.401439,4.882725,-7.595853,3.385622],[7.757224,-9.449129,4.180661,4.219439],[9.072399,4.153775,-4.398293,2.739303],[4.328390,3.663690,-3.120805,-4.602903],[-2.699097,3.008861,-4.099148,-3.634707],[0.770594,0.099631,-1.508076,-7.330144]],[[-0.322541,-2.358239,7.777954,5.913950],[-3.474073,-8.394490,5.693033,2.489321],[-8.739458,-2.125450,-2.973571,0.691061],[-8.440422,-2.767359,4.835276,-7.039984],[3.520408,3.026485,-5.606009,2.426045],[5.402888,6.227326,-9.421170,-0.350054]],[[-2.751781,-7.511429,2.487822,-2.400325],[-0.572814,3.936423,0.288386,-9.971944],[-9.278321,8.169142,-6.446947,-9.695624],[5.164765,-0.268325,-7.559169,-0.395437],[-1.519839,6.489383,-3.376914,3.116941],[2.689086,6.376627,-0.277990,5.026157]],[[2.422328,5.753750,8.410782,1.394058],[6.424394,-3.209720,-6.994193,-0.517146],[4.846265,-6.796784,-8.900005,2.979349],[-2.568513,-5.739033,-8.225784,-7.945473],[3.586008,1.690679,1.507963,1.392777],[5.067486,-5.304894,-4.581371,-2.298286]],[[1.876459,-3.794687,-3.221617,6.776391],[-6.526249,4.201021,7.785414,-6.177842],[1.578140,4.141629,-6.887064,8.636807],[-7.425638,1.341751,7.118557,3.050774],[-2.497674,-7.210556,9.859994,-4.139295],[5.280889,-2.789138,7.774216,3.843624]],[[-1.440014,6.517565,2.232948,-2.763470],[-8.444104,6.456779,1.219408,-4.369190],[-7.636049,-4.436496,-8.984282,7.795273],[-0.136769,-3.089046,-1.624846,-2.551117],[-6.712186,6.168182,3.041349,-6.269471],[1.148778,5.328523,-1.741449,-1.718980]]], dtype = "float32")#candidate|2195|(16, 6, 4)|const|float32
uop_2196 = relay.asinh(const_2195.astype('float32')) # shape=(16, 6, 4)
output = uop_2196
output2 = uop_2196
func_2204 = relay.Function([], output)
mod['func_2204'] = func_2204
mod = relay.transform.InferType()(mod)
mutated_mod['func_2204'] = func_2204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2204_call = mutated_mod.get_global_var('func_2204')
call_2205 = func_2204_call()
output = call_2205
func_2206 = relay.Function([], output)
mutated_mod['func_2206'] = func_2206
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2231 = relay.var("var_2231", dtype = "float64", shape = (16, 14, 12))#candidate|2231|(16, 14, 12)|var|float64
uop_2232 = relay.sinh(var_2231.astype('float64')) # shape=(16, 14, 12)
uop_2239 = relay.sigmoid(uop_2232.astype('float32')) # shape=(16, 14, 12)
output = relay.Tuple([uop_2239,])
output2 = relay.Tuple([uop_2239,])
func_2243 = relay.Function([var_2231,], output)
mod['func_2243'] = func_2243
mod = relay.transform.InferType()(mod)
mutated_mod['func_2243'] = func_2243
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2244 = relay.var("var_2244", dtype = "float64", shape = (16, 14, 12))#candidate|2244|(16, 14, 12)|var|float64
func_2243_call = mutated_mod.get_global_var('func_2243')
call_2245 = func_2243_call(var_2244)
output = call_2245
func_2246 = relay.Function([var_2244], output)
mutated_mod['func_2246'] = func_2246
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2248 = relay.var("var_2248", dtype = "uint32", shape = ())#candidate|2248|()|var|uint32
var_2249 = relay.var("var_2249", dtype = "uint32", shape = (8, 16))#candidate|2249|(8, 16)|var|uint32
bop_2250 = relay.maximum(var_2248.astype('uint32'), var_2249.astype('uint32')) # shape=(8, 16)
output = bop_2250
output2 = bop_2250
func_2261 = relay.Function([var_2248,var_2249,], output)
mod['func_2261'] = func_2261
mod = relay.transform.InferType()(mod)
var_2262 = relay.var("var_2262", dtype = "uint32", shape = ())#candidate|2262|()|var|uint32
var_2263 = relay.var("var_2263", dtype = "uint32", shape = (8, 16))#candidate|2263|(8, 16)|var|uint32
output = func_2261(var_2262,var_2263,)
func_2264 = relay.Function([var_2262,var_2263,], output)
mutated_mod['func_2264'] = func_2264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1319_call = mod.get_global_var('func_1319')
func_1320_call = mutated_mod.get_global_var('func_1320')
call_2286 = func_1319_call()
call_2287 = func_1319_call()
var_2288 = relay.var("var_2288", dtype = "float64", shape = (6, 9, 14))#candidate|2288|(6, 9, 14)|var|float64
bop_2289 = relay.equal(call_2286.astype('bool'), var_2288.astype('bool')) # shape=(6, 9, 14)
bop_2292 = relay.equal(call_2287.astype('bool'), var_2288.astype('bool')) # shape=(6, 9, 14)
uop_2295 = relay.cosh(call_2286.astype('float64')) # shape=(6, 1, 14)
uop_2297 = relay.cosh(call_2287.astype('float64')) # shape=(6, 1, 14)
uop_2304 = relay.cos(uop_2295.astype('float64')) # shape=(6, 1, 14)
uop_2306 = relay.cos(uop_2297.astype('float64')) # shape=(6, 1, 14)
func_533_call = mod.get_global_var('func_533')
func_537_call = mutated_mod.get_global_var('func_537')
var_2316 = relay.var("var_2316", dtype = "int8", shape = (143,))#candidate|2316|(143,)|var|int8
const_2317 = relay.const([6,8,-1,2,-2,-1,-8,2,1,4,-2,-3,10,2,-1,-7,-7,3,-1,-3,7,6,1,9,-9,1,3,-10,-1,9,7,9,2,3,-6,8,2,-9,5,-6,4,-10,1,-1,2,8,-7,3,-8,-3,-3,-8,-7,10,6,8,3,-6,-6,1,-7,9,-6,3,1,10,9,10,4,9,6,-9,-3,-5,4,-1,7,-4,6,-8,-3,10,-6,-9,-10,2,4,-7,10,10,-10,-2,-2,-9,-6,-5,7,3,6,6,10,4,-3,3,-2,7,3,-8,-8,3,-6,-4,-6,8,1,-9,-6,-5,3,2,2,-9,1,-1,-6,4,5,-7,-7,2,-9,-8,-4,-3,4,6,7,2,5,-6,8,-5,7,3,-6,-1,5,-1,-6,-8,10,-8,-9,6,4,9,1,6,-7,-2,-3,10,-6,-7,-5,-5,-8,3,-3,-5,10,-10,7,7,-2,-9,-3,5,9,-2,-8,9,-1,-5,-1,3,4,2,-7,7,9,-8,-4,2,4,6,-4,-8,-9,-1,-5,4,8,-3,7,6,-6,10,5,3,-7,-1,-6,-6,-2,-9,-1,-8,-1,4,3,-5,4,8,9,-1,10,9,-1,-3,2,-1,7,2,4,-7,7,5,9,-5,7,-7,7,5,3,-4,1,9,-7,-5,8,8,-6,-9,8,-3,9,2,-8,-8,8,-5,7,7,7,-9,-6,2,-9,6,6,-4,1,-3,-4,9,2,1,8,-7,3,-9,10,10,-4,-1,-8,-5,1,-8,-8,-7,1,-10,-9,3,3,-3,-5,4,-1,-2,-10,-10,5,-7,4,-3,-5,3,2,-8,-8,-7,5,-4,8,7,-3,10,6,-10,5,-7,-6,4,6,2,4,9,-3,-6,-7,1,-10,7,-10,6,10,-6,4,6,-4,6,-8,-5,-5,9,6,3,3,-1,7,-8,3,-3,6,8,8,7,-6,4,-5,-5,-5,6,10,-10,-7,4,-4,8,6,9,-10,9,-9,9,-10,-5,-5,-2,8,-2,2,-6,2,-8,2,4,6,-7,-8,10,-1,2,6,10,10,1,-9,10,-5,-2,8,8,-1,10,1,9,7,-9,7,-6,-3,-9,-8,-4,9,-9,-5,-4,1,-8,-6,-6,10,5,-5,6,-10,10,8,-8,-1,-8,3,5,-6,8,-1,4,-10,-3,-9,-4,-8,6,10,4,2,-10,-2,9,-9,1,-1,-1,3,7,5,-3,-10,8,5,-3,-2,2,-9,3,9,-8,-8,-3,-5,6,-6,2,10,-5,-1,-3,-3,-6,-5,-2,2,5,3,2,-10,7,-9,-1,-10,-3,-5,4,1,-2,-1,-3,8,-5,-7,8,-7,-5,-5,-5,-3,8,7,5,1,6,-6,5,8,5,-10,5,8,-4,-6,-10,9,4,9,4,1,-2,-9,-10,-8,2,-6,5,-7,-8,8,-2,7,3,-9,4,8,-4,-2,6,9,-7,-5,10,-1,-6,8,8,-6,-9,-9,-5,-8,6,5,-1,-9,9,3,7,10,5,-1,-3,-5,4,-5,2,7,-5,-3,-7,7,8,9,-3,9,7,10,-9,-2,10,-1,3,2,2,-8,-8,9,2,1,5,3,2,-1,8,-5,3,1,-7,5,10,2,-8,-6,-7,6,-9,-5,2,-3,1,9,7,9,-2,-5,8,10,6,-6,5,6,-5,-6,-9,9,8,-4,-7,10,7,-4,1,-3,-2,-2,3,10,1,6,4,1,-3,-8,8,-2,3,2,-3,-1,-3,3,-2,-5,8,4,7,5,-10,10,3,5,-9,-8,-1,7,-3,-4,-3,10,10,-5,-1,7,-5,1,9,4,2,-10,4,-1,-10,-3,-3,6,7,10,-2,-1,-4,-7,-8,-2,-4,5,2,4,-10,6,-8,-7,-4,4,4,2,-8,2,1,-8,6,10,9,1,9,-3,2,5,-6,1,-4,9,-4,-8,3,-8,9,-9,4,-8,-9,-1,10,6,-4,-6,-10,8,6,-8,2,-9,6,1,-10,-2,-9,-10,8,5,-1,-10,-7,-4,6,1,-8,1,8,3,-1,7,-9,-1,2,-8,-6,-5,-9,-6,-1,-3,9,4,-5,7,1,6,-10,-6,2,7,-4,-2,3,10,-7,4,6,-3,-4,-7,-4,-6,1,-9,8,4,10,9,-4,-7,1,-6,1,7,10,2,-8,-10,-2,1,-7,-4,-1,-10,1,7,-1,8,-2,9,1,-10,2,6,-1,6,4,-4,-4,-1,6,-8,10,-10,2,-8,1,-2,8,-8,6,6,3,-6,-8,3,-4,-10,-6,-1,-10,-3,-7,-3,-2,-5,-5,2,-2,-7,5,4,-3,-6,-7,-9,-5,7,5,10,-2,-10,5,7,8,8,5,5,-8,-9,7,1,8,6,9,5,-1,8,-6,-3,-8,10,-5,-3,3,10,-10,3,-1,3,7,1,4,-3,-4,-5,-7,8,-9,9,-5,-3,1,2,7,4,-5,9,4,-10,-8,3,-1,9,5,3,8,4,-3,3,-4,-3,4,10,6,8,-6,-1,-3,-8,-10,-8,-10,10,-9,-3,-2,1,10,5,3,2,-4,8,-3,8,9,2,6,-3,4,7,-4,-1,-2,-2,10,2,-7,5,-9,5,-7,-9,8,-10,-10,10,5,-2,-10,2,10,-5,-4,-9,3,3,1,-5,-6,5,1,-3,1,-5,-2,2,-9,-1,9,-10,-3,2,-4,5,1,-5,-7,9,4,8,9,9,7,4,7,-8,-6,-6,-7,-10,3,1,6,8,3,7,6,-3,4,-8,-1,3,7,10,10,-2,-9,-3,-4,4,-4,1,-7,-2,-2,-1,-7,4,6,7,6,-9,4,-10,10,6,-7,6,1,-2,-10,-8,1,-10,6,1,9,-6,1,-1,-2,-8,4,-10,4,8,8,3,-7,-6,-2,-6,-8,-6,-10,1,4,10,3,-2,3,3,5,-3,-10,-9,8,5,-10,5,10,4,5,-1,-4,-9,3,2,-7,2,4,10,-9,-7,8,10,10,-1,8,5,-6,-10,-6,7,-7,-3,-2,-4,9,-9,5,-4,-3,-2,-8,-2,-1,3,5,3,1,-3,-10,-2,-10,6,2,2,7,-6,-1,9,-1,9,2,-7,9,-4,9,-8,8,-6,-3,8,4,-5,4,-7,6,-2,2,-1,-1,10,2,-1,-1,3,-7,4,-4,-6,-2,-5,3,-5,7,3,-1,-8,-10,-5,5,-5,-10,-6,9,-5,7,7,7,4,-10,-4,10,5,-10,-1,10,-1,-8,-7,1,5,-3,-7,-8,8,7,-8,1,-9,6,10,-9,-8,-8,-1,8,6,-2,-6,3,8,-4,-9,2,10,1,5,8,4,-8,-4,4,-2,2,-7,-9,-7,5,-2,7,6,9,-5,-3,-5,-7,-9,-9,-7,8,8,-3,2,2,-7,-3,4,-2,-1,1,8,-6,-8,8,6,3,3,8,6,-9,-8,3,6,-4,-4,4,-2,9,-7,-9,-4,6,10,5,5,-6,8,-8,7,-1,6,3,8,-10,-2,8,3,5,10,-7,4,2,5,6,2,2,-7,-8,10,9,-8,8,-5,-3,3,-1,-3,10,-3,-9,6,-4,10,-9,9,2,9,9,5,8,-3,-8,2,-6,6,1,-1,-6,-7,1,5,3,7,5,-5,-3,-1,-7,-9,-9,10,-1,-7,2,-4,-9,-8,2,-6,9,-1,2,-1,7,3,9,10,-6,6,8,-3,-10,9,8,2,-9,-10,-5,1,5,1,-1,3,-5,-5,1,-10,-3,-5,-4,-10,10,-3,3,8,-2,-1,8,-8,4,-6,5,6,-4,-1,-7,-1,-1,1,-10,1,8,3,-7,-10,6,8,1,9,4,-4,-1,8,-9,7,10,9,1,5,-5,-10,3,4,1,-9,-5,8,8,-9,6,6,5,5,9,5,7,9,-3,-3,-8,1,-7,-1,-6,-2,6,10,3,-7,-7,8,-10,-3,-10,7,-1,5,-7,1,-7,-8,8,6,3,-4,8,4,9,-10,6,-8,6,-2,-8,-8,7,1,4,-9,-3,-7,6,-10,1,-3,9,-1,-3,-10,10,-9,4,6,-9,4,9,4,3,10,6,-10,-5,10,5,-10,-9,-4,8,2,-7,1,8,-1,1,-6,5,2,8,-9,-1,10,9,-3,-5,6,1,-8,-3,3,-10,-1,-6,8,-4,-7], dtype = "int8")#candidate|2317|(1573,)|const|int8
call_2315 = relay.TupleGetItem(func_533_call(relay.reshape(var_2316.astype('int8'), [11, 13, 1]), relay.reshape(const_2317.astype('int8'), [11, 13, 11]), ), 0)
call_2318 = relay.TupleGetItem(func_537_call(relay.reshape(var_2316.astype('int8'), [11, 13, 1]), relay.reshape(const_2317.astype('int8'), [11, 13, 11]), ), 0)
bop_2322 = relay.logical_and(uop_2295.astype('bool'), relay.reshape(call_2286.astype('bool'), relay.shape_of(uop_2295))) # shape=(6, 1, 14)
bop_2325 = relay.logical_and(uop_2297.astype('bool'), relay.reshape(call_2287.astype('bool'), relay.shape_of(uop_2297))) # shape=(6, 1, 14)
bop_2326 = relay.logical_and(uop_2304.astype('bool'), bop_2289.astype('bool')) # shape=(6, 9, 14)
bop_2329 = relay.logical_and(uop_2306.astype('bool'), bop_2292.astype('bool')) # shape=(6, 9, 14)
func_1714_call = mod.get_global_var('func_1714')
func_1716_call = mutated_mod.get_global_var('func_1716')
var_2343 = relay.var("var_2343", dtype = "float64", shape = (168,))#candidate|2343|(168,)|var|float64
call_2342 = func_1714_call(relay.reshape(var_2343.astype('float64'), [6, 2, 14]))
call_2344 = func_1714_call(relay.reshape(var_2343.astype('float64'), [6, 2, 14]))
uop_2353 = relay.asinh(bop_2326.astype('float64')) # shape=(6, 9, 14)
uop_2355 = relay.asinh(bop_2329.astype('float64')) # shape=(6, 9, 14)
func_533_call = mod.get_global_var('func_533')
func_537_call = mutated_mod.get_global_var('func_537')
call_2358 = relay.TupleGetItem(func_533_call(relay.reshape(var_2316.astype('int8'), [11, 13, 1]), relay.reshape(call_2315.astype('int8'), [11, 13, 11]), ), 1)
call_2359 = relay.TupleGetItem(func_537_call(relay.reshape(var_2316.astype('int8'), [11, 13, 1]), relay.reshape(call_2315.astype('int8'), [11, 13, 11]), ), 1)
func_1829_call = mod.get_global_var('func_1829')
func_1832_call = mutated_mod.get_global_var('func_1832')
call_2370 = relay.TupleGetItem(func_1829_call(relay.reshape(call_2342.astype('float64'), [168,])), 2)
call_2371 = relay.TupleGetItem(func_1832_call(relay.reshape(call_2342.astype('float64'), [168,])), 2)
bop_2376 = relay.logical_or(uop_2295.astype('bool'), uop_2353.astype('bool')) # shape=(6, 9, 14)
bop_2379 = relay.logical_or(uop_2297.astype('bool'), uop_2355.astype('bool')) # shape=(6, 9, 14)
func_423_call = mod.get_global_var('func_423')
func_428_call = mutated_mod.get_global_var('func_428')
var_2383 = relay.var("var_2383", dtype = "int32", shape = ())#candidate|2383|()|var|int32
const_2384 = relay.const([[-10,3,-4],[2,-10,9],[2,-3,-9],[-6,9,-9],[-3,-6,6],[5,9,-7],[-2,-10,-3],[-4,4,2],[2,6,-5],[6,10,3],[2,-4,-7],[-7,-2,-1],[7,2,3],[-7,-9,-6],[-8,2,-4],[5,-4,-8],[-2,10,-3],[-10,8,-2],[-3,-6,1],[-7,-6,-6],[6,8,-8],[3,-3,-5],[5,5,-5],[-4,5,1],[4,5,-6],[2,-10,-4],[-9,10,1],[6,-1,1],[9,4,-9],[-10,-10,-5],[-3,10,7],[4,2,-8],[9,1,7],[6,1,-10],[5,-3,4],[-1,5,2],[7,10,10],[-4,-3,1],[-1,6,6],[-2,7,-6],[-3,9,10],[2,7,-9],[-9,8,-2],[-2,7,-4],[-7,4,2],[-6,-8,-5],[-6,8,-10],[-2,1,-8],[10,-5,9],[10,8,9],[-5,-6,-2],[1,-9,-3],[7,-7,7],[3,-7,-4],[10,4,9],[7,-8,7],[8,-8,-9],[6,-8,8],[10,5,-4],[6,5,1],[3,8,-2],[3,-4,-7],[-4,3,-7],[9,4,7],[-3,1,10],[1,-1,7],[7,5,1],[-6,-6,8],[2,3,1],[4,-2,1],[-9,7,5],[-5,-4,-4],[4,-1,-1],[-8,-8,8],[2,3,-7],[7,-9,7],[-8,4,7],[-6,-10,-3],[-8,1,-1],[-5,-1,6],[3,7,8],[5,8,-6],[9,-6,-1],[-9,10,-2],[1,6,6],[-1,7,-2],[-1,1,-8],[4,10,-8],[9,-9,9],[9,-1,-9],[9,5,-7],[-1,3,8],[10,1,-10],[-3,8,7],[3,5,-1],[10,-6,5],[1,-2,7],[-8,-1,-9],[9,9,3],[-3,2,-2],[-4,-2,-7],[-6,3,5],[-9,9,3],[1,1,9],[6,2,-2],[10,7,10],[8,-6,-5],[5,5,4],[-3,2,-4],[7,5,-9],[-4,-4,-10],[-6,-2,3],[3,-1,-1],[8,9,7],[-3,5,-6],[4,3,2],[4,-4,-10],[4,-5,6],[2,-2,-6],[-4,5,-6],[4,-10,9],[10,10,8],[3,5,-6],[5,-7,-9],[-6,-1,-4],[4,6,-5],[-6,8,3],[7,-9,5],[5,3,7],[-4,-7,-5],[-1,-1,5],[-4,4,-8],[-10,-2,-7],[-4,7,4],[-9,6,-3],[-9,4,-3],[-7,-9,-9],[-6,9,-5],[5,1,-7],[3,-5,-6],[-3,-5,6],[-5,5,3],[-8,2,-9],[6,-8,-3],[3,-5,-8],[-9,5,-8],[-1,3,7],[-9,-7,4],[8,9,6],[1,9,-8],[-6,-9,-10],[-1,10,-7],[1,3,5],[-3,5,8],[-3,3,-6],[8,9,-4],[-4,1,10],[4,4,-9],[-3,5,-4],[3,4,1],[6,-4,9],[-5,-3,-1],[-4,4,10],[-10,-8,5],[8,1,-2],[3,-4,-5],[3,7,6],[-10,-3,-10],[-10,10,-3],[-1,-2,2],[9,-4,-2],[-7,8,-2],[-4,-5,-9],[-1,-5,-6],[-5,1,3],[1,-9,-4],[-5,6,5],[-10,-2,-5],[9,-7,-7],[5,4,-9],[-9,9,-7],[-9,-2,-6],[4,-5,10],[-7,-5,5],[9,-2,-8],[-2,-1,-7],[1,-1,-2],[1,2,2],[7,-2,4],[-2,1,-8],[7,8,-10],[-8,-10,6],[-7,-7,5],[2,-9,-2],[-4,-7,-10],[-4,6,9],[-6,7,-8],[-7,9,4],[3,6,10],[6,2,-1],[-10,-1,8],[2,-7,-9],[3,-9,-9],[-8,9,-4],[-2,7,4],[6,2,10],[-9,3,5],[-10,5,5],[-2,-6,-9],[-4,-1,-2]], dtype = "int32")#candidate|2384|(210, 3)|const|int32
var_2385 = relay.var("var_2385", dtype = "int8", shape = (264,))#candidate|2385|(264,)|var|int8
call_2382 = relay.TupleGetItem(func_423_call(relay.reshape(var_2383.astype('int32'), []), relay.reshape(const_2384.astype('int32'), [7, 9, 10]), relay.reshape(var_2385.astype('int8'), [264,]), ), 3)
call_2386 = relay.TupleGetItem(func_428_call(relay.reshape(var_2383.astype('int32'), []), relay.reshape(const_2384.astype('int32'), [7, 9, 10]), relay.reshape(var_2385.astype('int8'), [264,]), ), 3)
output = relay.Tuple([call_2315,var_2316,const_2317,bop_2322,call_2342,var_2343,call_2358,call_2370,bop_2376,call_2382,var_2383,const_2384,var_2385,])
output2 = relay.Tuple([call_2318,var_2316,const_2317,bop_2325,call_2344,var_2343,call_2359,call_2371,bop_2379,call_2386,var_2383,const_2384,var_2385,])
func_2389 = relay.Function([var_2288,var_2316,var_2343,var_2383,var_2385,], output)
mod['func_2389'] = func_2389
mod = relay.transform.InferType()(mod)
mutated_mod['func_2389'] = func_2389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2389_call = mutated_mod.get_global_var('func_2389')
var_2391 = relay.var("var_2391", dtype = "float64", shape = (6, 9, 14))#candidate|2391|(6, 9, 14)|var|float64
var_2392 = relay.var("var_2392", dtype = "int8", shape = (143,))#candidate|2392|(143,)|var|int8
var_2393 = relay.var("var_2393", dtype = "float64", shape = (168,))#candidate|2393|(168,)|var|float64
var_2394 = relay.var("var_2394", dtype = "int32", shape = ())#candidate|2394|()|var|int32
var_2395 = relay.var("var_2395", dtype = "int8", shape = (264,))#candidate|2395|(264,)|var|int8
call_2390 = func_2389_call(var_2391,var_2392,var_2393,var_2394,var_2395,)
output = call_2390
func_2396 = relay.Function([var_2391,var_2392,var_2393,var_2394,var_2395,], output)
mutated_mod['func_2396'] = func_2396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1620_call = mod.get_global_var('func_1620')
func_1622_call = mutated_mod.get_global_var('func_1622')
call_2515 = relay.TupleGetItem(func_1620_call(), 0)
call_2516 = relay.TupleGetItem(func_1622_call(), 0)
func_1871_call = mod.get_global_var('func_1871')
func_1874_call = mutated_mod.get_global_var('func_1874')
const_2518 = relay.const([-6,4,10,9,-3,-2,-10,-8,8,7,7,7,7,1,6,-1,-8,-6,1,4,-4,-10,1,-9,9,2,-3,3,9,-5,-9,7,3,6,1,-8,8,9,8,-10,-5,-5,3,10,4,-5,4,-10,5,1,-8,9,8,7,8,-3,10,-3,7,-3,9,-4,9,-9,10,8,-10,-5,-9,-4,-8,1,-6,10,-10,-4,10,3,2,4,2,1,1,10,-8,8,-5,3,5,-5,-6,-3,9,-10,8,4,-7,1,10,-9,-10,-6,6,-6,-3,-4,-2,-9,-5,-1,-4,2,-9,-1,-8,9,9,-1,-5,6,10,10,8,-2,-10,-3,-7,6,-10,6,9,-6,-3,3,-5,-7,-8,-6,6,-9,-8,-1,-9,-2,-7,-9,-6,-5,1,6,-9,-1,-9,5,-3,-4,-9,8,5,9,8,8,-2,-2,3,10,-2,8,8,-1,-8,-3,-3,4,-3,-7,2,7,-8,-10,-1,-2,-1,-6,-6,9,-1,10,7,1,-9,-3,6,9,-10,-7,-9,-4,1,-9,-7,10,5,2,-4,-2,-3,-7,6,3,7,7,-10,6,10,-10,-6,-5,-10,2,1,-10,8,3,5,10,-5,6,7,-9,-9,-4,-9,5,5,3,1,8,1,3,-7,-6,9,8,-7,-3,-5,-1,-3,2,-6,-3,10,-8,3,7,-4,4,8,-9,8,9,-8,-8], dtype = "int8")#candidate|2518|(264,)|const|int8
call_2517 = relay.TupleGetItem(func_1871_call(relay.reshape(const_2518.astype('int8'), [264,])), 1)
call_2519 = relay.TupleGetItem(func_1874_call(relay.reshape(const_2518.astype('int8'), [264,])), 1)
output = relay.Tuple([call_2515,call_2517,const_2518,])
output2 = relay.Tuple([call_2516,call_2519,const_2518,])
func_2523 = relay.Function([], output)
mod['func_2523'] = func_2523
mod = relay.transform.InferType()(mod)
mutated_mod['func_2523'] = func_2523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2523_call = mutated_mod.get_global_var('func_2523')
call_2524 = func_2523_call()
output = call_2524
func_2525 = relay.Function([], output)
mutated_mod['func_2525'] = func_2525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1361_call = mod.get_global_var('func_1361')
func_1363_call = mutated_mod.get_global_var('func_1363')
call_2528 = relay.TupleGetItem(func_1361_call(), 0)
call_2529 = relay.TupleGetItem(func_1363_call(), 0)
uop_2547 = relay.atan(call_2528.astype('float64')) # shape=(6, 1, 14)
uop_2549 = relay.atan(call_2529.astype('float64')) # shape=(6, 1, 14)
func_1688_call = mod.get_global_var('func_1688')
func_1691_call = mutated_mod.get_global_var('func_1691')
const_2552 = relay.const([[-8.538991],[-6.932476],[-7.086356],[7.000400],[2.977739],[3.209358],[8.317534],[2.574732],[-3.676771],[9.473738],[-0.780018],[-3.931040],[-2.663060],[8.544576],[-1.417603],[2.532225],[1.950295],[-1.872903],[7.480878],[3.347999],[5.827099],[-3.406864],[9.029522],[-1.604785],[2.121739],[5.543260],[0.755909],[7.451150],[-1.366860],[-5.836609],[3.636831],[1.517056],[6.097248],[-2.764689],[7.681901],[7.897877],[9.666081],[-3.691444],[1.654922],[-2.516768],[-3.409967],[-5.334320],[-4.908830],[8.740736],[0.662151],[2.351554],[2.511943],[5.492625],[8.151924],[8.409267],[6.514284],[3.391305],[5.713634],[-7.029150],[7.369860],[3.413043],[-7.249314],[1.260620],[2.304985],[4.858119],[-7.486606],[3.815093],[5.144829],[-7.995076],[2.725788],[-5.421224],[-3.096475],[2.128833],[8.945094],[-0.462386],[-6.797753],[-9.502112],[9.535039],[5.129059],[-7.015836],[8.114852],[-8.740881],[-0.540975],[4.090221],[-8.124859],[-0.219650],[-7.360092],[-2.760183],[-8.031972],[3.764718],[-6.309653],[-1.716842],[-8.285694],[-8.416490],[2.426743],[3.308701],[7.342595],[1.596783],[6.776044],[-0.342078],[0.461430],[-9.139732],[5.177713],[4.653721],[-3.895752],[-4.312931],[0.505922],[9.091897],[4.997816],[0.890497],[-7.942863],[9.015077],[-2.488517],[8.748233],[-7.475809],[2.635979],[6.519872],[7.755527],[9.107261],[-6.902376],[1.444271],[-5.914013],[-8.121383],[-8.262665],[-9.962846],[-7.152148],[-4.149188],[-0.541478],[-8.038787],[2.626349],[-2.445361],[2.159623],[-0.471167],[-9.761899],[0.358730],[-8.797957],[-6.818013],[9.595271],[-6.941608],[-7.159859],[-7.533451],[-4.486265],[-2.165901],[8.548474],[-8.000170],[3.301821],[-6.595119],[-8.747745],[1.738234],[-0.757454],[-8.121743],[6.202537],[9.674297],[2.664861],[0.764654],[-7.504010],[-4.040241],[-5.180334],[-5.813521],[2.485244],[-2.430557],[4.607370],[6.657206],[-6.110496],[-7.426077],[-0.751094],[4.728075],[1.820594],[-6.626294],[-5.302948],[-0.385419],[4.068527],[4.629867],[-8.547129],[-1.496754],[3.475821],[-6.150040],[8.336144],[-3.633184],[9.792436],[-6.458730],[8.279895],[8.305401],[-0.451661],[1.937733],[7.698772],[-4.572402],[-1.066435],[3.946011],[1.678648],[4.170422],[-5.214683],[0.151829],[4.144782],[5.739751],[-2.765007],[-1.990406],[1.624266],[7.830889],[-5.575707],[3.761135],[-5.398860],[-9.432188],[4.259867],[4.034997],[7.138783],[4.452460],[8.647944],[9.090712],[7.425482],[2.366492],[-0.885235],[3.649945],[0.215522],[-0.540341],[-4.974219],[-0.961667],[0.111232],[6.971820],[-2.876300],[9.830675],[5.183203],[1.330196],[1.914754],[-7.709172],[-5.434111],[-9.965627],[4.852808],[-7.650265],[-3.948055],[-7.909362],[-3.569072],[-0.818066],[-3.845850],[4.817560],[-3.753802],[-7.084983],[5.330938],[-6.009550],[7.936066],[9.863292],[-8.656121],[-0.628451],[-1.633500],[5.550748],[9.453136],[8.727106],[-4.626322],[2.731932],[6.657847],[4.053392],[8.213846],[-1.484966],[4.811742],[6.421620],[5.021837],[-0.298816],[0.922624],[4.030220],[-3.334009],[-4.577465],[9.075823],[5.549296],[7.920479],[-4.459216],[6.922487],[9.167973],[6.393367],[-2.677158],[-6.350726],[1.098335],[-2.129604],[-8.456179],[1.244822],[0.098674],[-6.865326],[6.388305],[7.106811],[2.305804],[-5.485652],[-0.668200],[3.399281],[-5.212148],[6.122015],[8.573391],[9.935711],[5.992899],[5.122910],[0.778176],[9.950014],[-1.534495],[-9.556087],[4.254437],[-2.847208],[6.247107],[-6.902779],[9.898696],[4.659107],[8.919201],[-6.422882],[-6.180095],[0.650341],[5.876480],[2.579415],[6.488714],[-5.465298],[-2.586919],[-3.181047],[-5.442882],[-4.672461],[6.117277],[9.611455],[-7.035687],[-7.423817],[3.999106],[9.723237],[-0.862792],[7.741930],[7.040751],[-1.778524],[-7.903818],[-8.322733],[-2.940143],[-2.221378],[2.510994],[-6.684615],[-0.294730],[6.301899],[-5.555178],[-1.313545],[-5.372821],[4.733762],[-4.907609],[7.358566],[-3.875274],[8.104459],[-3.398011],[2.136714],[-4.637743],[8.494593],[8.883831],[-0.381881],[-0.186995],[-4.005999],[1.882899],[-6.372083],[-4.615921],[2.774128],[1.949136],[-8.156356],[-3.875116],[-2.847205],[6.492205],[7.499181],[3.118843],[-5.534824],[-0.792101],[-8.586798],[-0.006878],[2.258382],[5.356964],[-2.745890],[-7.386233],[9.665185],[-6.271987],[6.461694],[8.241565],[5.028809],[6.098947],[-7.646900],[4.611854],[0.869379],[6.304924],[-5.339109],[4.940229],[4.059897],[-0.453075],[-4.466210],[4.010810],[-7.826342],[-1.010257],[9.531740],[9.474995],[-3.289583],[3.087225],[9.460370],[7.254809],[2.581245],[2.465709],[8.291665],[1.470358],[0.251003],[-8.987232],[-8.867870],[6.111382],[8.816961],[-0.609456],[6.973931],[0.647768],[5.835213],[-5.662722],[8.075077],[1.793173],[-9.599700],[7.777780],[7.252468],[2.602342],[-1.733224],[4.356300],[9.271233],[8.046425],[-0.242197],[0.165406],[5.502983],[1.143080],[-1.247803],[4.694982],[-6.349691],[-3.205113],[2.473840],[-0.701132],[-0.905964],[-2.952083],[9.441890],[-5.583826],[-9.055654],[7.857125],[7.982582],[2.806830],[5.037531],[1.313592],[-2.336816],[2.759608],[-5.770448],[-9.939711],[0.564123],[-4.954586],[-0.682283],[-3.713877],[-3.449930],[-1.820151],[-4.360606],[6.936621],[3.112075],[-9.157658],[-7.268429],[-9.139185],[5.827837],[3.154973],[6.534820],[8.990303],[-3.775153],[-3.687895],[-5.874324],[-8.209342],[0.446273],[-4.184137],[-8.031256],[-9.976235],[-1.470149],[-9.671565],[-0.713979],[6.360934],[-8.560498],[7.996199],[-9.472099],[6.970212],[7.797731],[5.729238],[-4.093222],[-8.244363],[6.715691],[-2.336246],[8.391551],[2.235682],[0.376217],[-1.318218],[-1.077110],[8.532164],[-8.000074],[-7.469169],[-6.384381],[3.053254],[8.784790],[2.930648],[-0.120362],[-1.098299],[-4.805946],[0.222332],[1.235373],[9.213422],[-9.769206],[-5.847694],[-6.249124],[3.012934],[0.408461],[3.780627],[0.016061],[3.816740],[-7.059900],[4.426988],[-4.853732],[-7.434594],[-9.549406],[-7.010500],[-8.960786],[-8.854333],[4.102578],[4.912055],[5.215232],[-6.643960],[-2.673058],[-0.965317],[-4.713234],[-0.225133],[-2.672891],[9.082169],[2.485906],[-0.855136],[6.936865],[5.258503],[-0.482810],[-7.784296],[8.003733],[8.582406],[9.451451],[2.068784],[-3.892208],[4.929372],[9.328803],[2.031050],[9.119054],[-1.074426],[-1.460491],[-6.531458],[-3.675674],[8.780396],[-3.878059],[-7.188671],[0.475730],[-0.514801],[-7.061084],[-9.956392],[6.535484],[2.508119],[9.597667],[-8.012340],[-4.263167],[-7.029603],[1.778753],[-6.124084],[-1.397060],[5.990311],[-1.517614],[-8.514495],[1.253256],[-9.982998],[-9.183866],[-6.587691],[-1.907891],[-1.790608],[-9.989587],[8.324363],[-6.386902],[4.847996],[-8.705756],[0.369776],[7.942796],[0.222215],[-7.363508],[9.143072],[-7.396446],[1.755171],[-7.297151],[-1.682859],[-2.414673],[1.416253],[-5.719770],[3.882905],[-2.715994],[-7.214688],[-5.006414],[6.179762],[-1.576668],[4.401647],[3.026877],[2.470025],[-5.957233],[-4.310971],[-4.962893],[-2.987974],[-2.137948],[-2.793892],[-9.045292],[7.456214],[-5.460065],[0.049517],[3.209430],[1.597931],[-1.280821],[-2.969303],[0.938219],[6.855813],[9.365106],[1.005900],[6.216060],[-4.318976],[8.478982],[-2.459305],[-4.474276],[-2.087364],[0.433622],[8.541999],[-0.371322],[8.172914],[-2.024268],[-1.979688],[8.302919],[0.658801],[-9.675335],[-8.680820],[-8.852054],[8.053498],[0.997818],[5.901265],[3.675031],[1.688124],[-8.754303],[0.175306],[4.453649],[6.920518],[-2.393903],[6.997629],[9.891965],[-4.556272]], dtype = "float64")#candidate|2552|(630, 1)|const|float64
const_2553 = relay.const([7,-2,8,-9,-7,7,-4,-8,8,-2,1,8,-5,-9,-1,-10,-10,-1,8,-9,4,-2,1,-7,-3,2,9,9,-10,4,-5,-2,-7,-3,3,-1,-10,-5,2,9,-5,9,-3,-5,9,6,6,-10,1,9,7,-2,4,7,-1,1,-9,9,-1,9,-6,3,-5,6,-6,1,-6,10,2,3,-6,-1,-7,1,5,-9,6,-4,4,-8,-4,6,4,9,7,-3,-8,-10,-5,4,-10,2,4,-7,-3,-3,-6,8,-6,7,-10,-8,5,5,8,1,-4,-6,-6,-7,7,-9,-10,4,5,-1,4,-5,-7,10,-2,5,-3,-4,-3,-9,2,5,6,-10,-3,-5,-10,7,-3,-5,9,10,-1,10,-5,6,8,9,-1,2,-10,10,-9,1,3,6,-8,-3,-3,4,-1,-7,-4,-10,7,-10,10,9,6,-1,8,10,-6,-6,3,6,10,4,2,-10,7,-6,-7,-8,8,3,-7,-9,-3,9,-5,-3,-10,1,-2,-9,-1,8,3,-3,5,5,9,4,-1,10,-10,10,-2,10,-4,-3,-5,2,-4,8,-1,1,9,1,-10,5,-8,10,8,3,10,-6,4,-4,5,8,-7,7,4,-5,1,-4,4,8,-3,-5,-5,-9,-9,9,-5,1,6,9,5,6,-3,-4,4,1,3,10,7,8,2,-1,4,10,-1,2,2,-4], dtype = "int8")#candidate|2553|(264,)|const|int8
call_2551 = relay.TupleGetItem(func_1688_call(relay.reshape(const_2552.astype('float64'), [7, 9, 10]), relay.reshape(const_2553.astype('int8'), [264,]), ), 2)
call_2554 = relay.TupleGetItem(func_1691_call(relay.reshape(const_2552.astype('float64'), [7, 9, 10]), relay.reshape(const_2553.astype('int8'), [264,]), ), 2)
bop_2565 = relay.less(uop_2547.astype('bool'), relay.reshape(call_2528.astype('bool'), relay.shape_of(uop_2547))) # shape=(6, 1, 14)
bop_2568 = relay.less(uop_2549.astype('bool'), relay.reshape(call_2529.astype('bool'), relay.shape_of(uop_2549))) # shape=(6, 1, 14)
uop_2575 = relay.atanh(const_2552.astype('float64')) # shape=(630, 1)
func_2261_call = mod.get_global_var('func_2261')
func_2264_call = mutated_mod.get_global_var('func_2264')
const_2578 = relay.const(-2, dtype = "uint32")#candidate|2578|()|const|uint32
const_2579 = relay.const([-1,8,6,-10,-6,-2,5,-2,1,-8,5,1,-6,-3,4,-4,6,2,-6,6,-9,-4,2,-7,9,-8,-1,-8,-4,7,8,2,5,-5,6,4,-2,10,-8,1,-4,-4,7,-4,-4,8,10,5,6,6,-3,-5,-3,-3,2,10,2,-3,-9,-10,5,2,-2,3,-7,9,-3,7,9,-9,-1,-1,5,1,-10,-5,-3,-2,-6,-2,-6,-4,-3,-7,8,-7,4,-1,-9,-3,5,4,8,2,1,-8,-3,7,3,10,9,2,3,-4,-8,-3,-6,-1,-3,8,-5,4,-9,5,7,3,3,1,1,-10,2,-3,10,-3,-7,8,7,3], dtype = "uint32")#candidate|2579|(128,)|const|uint32
call_2577 = func_2261_call(relay.reshape(const_2578.astype('uint32'), []), relay.reshape(const_2579.astype('uint32'), [8, 16]), )
call_2580 = func_2261_call(relay.reshape(const_2578.astype('uint32'), []), relay.reshape(const_2579.astype('uint32'), [8, 16]), )
output = relay.Tuple([call_2551,const_2553,bop_2565,uop_2575,call_2577,const_2578,const_2579,])
output2 = relay.Tuple([call_2554,const_2553,bop_2568,uop_2575,call_2580,const_2578,const_2579,])
func_2581 = relay.Function([], output)
mod['func_2581'] = func_2581
mod = relay.transform.InferType()(mod)
mutated_mod['func_2581'] = func_2581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2581_call = mutated_mod.get_global_var('func_2581')
call_2582 = func_2581_call()
output = call_2582
func_2583 = relay.Function([], output)
mutated_mod['func_2583'] = func_2583
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2593 = relay.var("var_2593", dtype = "bool", shape = (14, 14, 5))#candidate|2593|(14, 14, 5)|var|bool
const_2594 = relay.const([[[True,True,False,False,False],[True,False,True,False,True],[False,False,False,False,True],[True,False,True,False,True],[False,False,False,True,True],[False,True,True,False,False],[True,True,False,True,True],[False,False,True,True,False],[True,True,True,True,True],[False,False,True,True,False],[True,True,False,True,True],[False,True,False,True,True],[False,False,False,False,True],[False,False,False,True,True]],[[False,False,False,True,True],[False,True,True,True,False],[False,False,False,False,False],[True,False,True,True,True],[True,True,True,True,False],[True,True,False,True,True],[False,True,True,False,True],[True,False,False,False,False],[True,False,False,True,True],[False,False,True,False,True],[True,True,False,False,False],[False,True,False,True,False],[True,True,False,False,True],[True,True,False,True,False]],[[False,False,False,False,True],[True,True,True,True,True],[False,False,False,True,False],[False,True,False,False,False],[False,True,True,False,False],[True,True,True,True,True],[True,True,True,False,True],[True,True,False,False,False],[True,True,False,True,False],[True,False,True,True,False],[False,True,False,True,False],[False,False,True,True,True],[False,True,False,False,True],[False,True,False,False,True]],[[True,False,False,True,True],[False,False,True,False,True],[False,False,True,False,True],[True,False,False,False,True],[True,True,False,False,True],[True,False,False,False,False],[True,True,False,False,False],[False,False,True,True,False],[False,True,False,True,True],[False,False,True,False,True],[True,True,False,True,True],[True,True,True,True,True],[False,False,False,False,False],[False,False,True,True,False]],[[True,False,True,False,True],[True,False,False,False,False],[True,True,True,True,True],[True,False,False,False,True],[True,False,True,True,True],[False,True,True,True,True],[True,False,True,True,False],[False,False,False,False,False],[False,True,False,False,False],[True,True,False,True,True],[True,False,False,True,True],[True,True,False,False,False],[True,False,False,False,True],[True,True,True,True,True]],[[True,False,True,True,False],[True,False,True,False,True],[False,True,True,False,False],[False,True,True,True,False],[True,False,False,False,True],[True,True,False,False,False],[True,True,False,False,True],[False,False,True,True,False],[True,False,True,False,False],[False,True,False,True,False],[False,True,False,False,True],[True,True,False,True,True],[False,True,False,True,True],[True,True,True,True,True]],[[True,False,True,True,False],[True,True,True,True,False],[True,True,True,False,True],[False,True,False,False,True],[True,True,False,False,False],[True,True,True,True,False],[False,False,False,True,True],[True,True,False,False,False],[True,False,False,False,False],[True,True,True,False,True],[False,True,False,False,True],[False,False,True,False,True],[True,False,True,False,False],[True,True,True,True,True]],[[True,False,True,True,True],[True,True,False,True,True],[True,True,False,False,False],[False,False,False,True,False],[True,False,True,False,False],[True,True,True,False,True],[True,True,True,False,True],[False,False,False,False,True],[True,False,False,True,False],[False,True,False,False,False],[True,True,True,False,False],[True,True,True,True,True],[False,False,False,False,False],[True,False,False,True,True]],[[True,False,True,False,False],[True,False,True,True,True],[False,False,False,True,False],[False,False,True,False,True],[False,False,True,True,False],[False,False,True,False,False],[False,False,False,True,False],[False,False,False,False,True],[True,False,False,False,True],[False,False,True,False,False],[True,False,True,False,True],[True,False,False,False,True],[False,False,True,False,True],[True,True,True,True,True]],[[True,True,True,True,True],[False,True,True,True,True],[False,False,False,True,True],[True,False,True,True,True],[False,True,True,True,False],[True,False,True,False,False],[False,True,True,True,False],[False,True,False,True,False],[True,True,True,True,False],[False,True,True,True,False],[False,False,False,True,True],[False,False,False,True,True],[False,True,False,True,False],[True,True,True,True,False]],[[True,False,False,False,False],[False,False,True,True,False],[True,True,False,True,True],[True,True,True,True,False],[False,True,True,True,False],[True,False,True,False,True],[False,False,True,False,False],[True,False,True,False,False],[True,False,True,True,True],[False,False,True,False,False],[True,False,True,True,True],[False,False,True,True,True],[False,True,True,False,True],[True,True,False,False,False]],[[False,True,False,True,False],[True,False,True,False,False],[True,False,False,False,True],[False,False,True,True,False],[False,False,True,True,False],[True,True,True,True,True],[True,True,True,True,False],[True,True,False,False,True],[False,True,True,True,False],[False,True,False,False,False],[False,False,False,False,False],[False,True,True,False,False],[False,True,True,True,True],[True,True,False,False,True]],[[True,False,True,True,True],[True,True,False,True,True],[True,False,False,True,False],[False,False,True,True,False],[True,True,True,False,True],[False,True,False,False,True],[True,False,False,False,True],[True,True,False,False,True],[False,True,True,False,False],[True,False,False,False,True],[False,True,False,False,True],[True,False,False,True,True],[False,True,True,False,True],[False,True,True,False,True]],[[False,False,False,True,False],[True,False,False,True,False],[True,False,True,False,False],[False,True,False,False,True],[True,False,False,False,False],[True,False,False,False,True],[True,False,True,False,True],[False,True,True,False,False],[True,False,False,False,False],[False,False,True,True,True],[False,False,True,False,True],[False,False,True,False,False],[False,True,True,False,True],[False,False,False,False,False]]], dtype = "bool")#candidate|2594|(14, 14, 5)|const|bool
bop_2595 = relay.logical_or(var_2593.astype('bool'), relay.reshape(const_2594.astype('bool'), relay.shape_of(var_2593))) # shape=(14, 14, 5)
output = relay.Tuple([bop_2595,])
output2 = relay.Tuple([bop_2595,])
func_2600 = relay.Function([var_2593,], output)
mod['func_2600'] = func_2600
mod = relay.transform.InferType()(mod)
var_2601 = relay.var("var_2601", dtype = "bool", shape = (14, 14, 5))#candidate|2601|(14, 14, 5)|var|bool
output = func_2600(var_2601)
func_2602 = relay.Function([var_2601], output)
mutated_mod['func_2602'] = func_2602
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2622 = relay.var("var_2622", dtype = "int16", shape = (4, 14, 13))#candidate|2622|(4, 14, 13)|var|int16
var_2623 = relay.var("var_2623", dtype = "int16", shape = (4, 14, 13))#candidate|2623|(4, 14, 13)|var|int16
bop_2624 = relay.multiply(var_2622.astype('int16'), relay.reshape(var_2623.astype('int16'), relay.shape_of(var_2622))) # shape=(4, 14, 13)
output = relay.Tuple([bop_2624,])
output2 = relay.Tuple([bop_2624,])
func_2643 = relay.Function([var_2622,var_2623,], output)
mod['func_2643'] = func_2643
mod = relay.transform.InferType()(mod)
var_2644 = relay.var("var_2644", dtype = "int16", shape = (4, 14, 13))#candidate|2644|(4, 14, 13)|var|int16
var_2645 = relay.var("var_2645", dtype = "int16", shape = (4, 14, 13))#candidate|2645|(4, 14, 13)|var|int16
output = func_2643(var_2644,var_2645,)
func_2646 = relay.Function([var_2644,var_2645,], output)
mutated_mod['func_2646'] = func_2646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1370_call = mod.get_global_var('func_1370')
func_1371_call = mutated_mod.get_global_var('func_1371')
call_2720 = relay.TupleGetItem(func_1370_call(), 0)
call_2721 = relay.TupleGetItem(func_1371_call(), 0)
output = call_2720
output2 = call_2721
func_2724 = relay.Function([], output)
mod['func_2724'] = func_2724
mod = relay.transform.InferType()(mod)
output = func_2724()
func_2725 = relay.Function([], output)
mutated_mod['func_2725'] = func_2725
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2724_call = mod.get_global_var('func_2724')
func_2725_call = mutated_mod.get_global_var('func_2725')
call_2750 = func_2724_call()
call_2751 = func_2724_call()
var_2752 = relay.var("var_2752", dtype = "float64", shape = (7, 9, 10))#candidate|2752|(7, 9, 10)|var|float64
bop_2753 = relay.greater(call_2750.astype('bool'), relay.reshape(var_2752.astype('bool'), relay.shape_of(call_2750))) # shape=(7, 9, 10)
bop_2756 = relay.greater(call_2751.astype('bool'), relay.reshape(var_2752.astype('bool'), relay.shape_of(call_2751))) # shape=(7, 9, 10)
func_839_call = mod.get_global_var('func_839')
func_841_call = mutated_mod.get_global_var('func_841')
call_2764 = relay.TupleGetItem(func_839_call(), 2)
call_2765 = relay.TupleGetItem(func_841_call(), 2)
output = relay.Tuple([bop_2753,call_2764,])
output2 = relay.Tuple([bop_2756,call_2765,])
func_2766 = relay.Function([var_2752,], output)
mod['func_2766'] = func_2766
mod = relay.transform.InferType()(mod)
var_2767 = relay.var("var_2767", dtype = "float64", shape = (7, 9, 10))#candidate|2767|(7, 9, 10)|var|float64
output = func_2766(var_2767)
func_2768 = relay.Function([var_2767], output)
mutated_mod['func_2768'] = func_2768
mutated_mod = relay.transform.InferType()(mutated_mod)
func_839_call = mod.get_global_var('func_839')
func_841_call = mutated_mod.get_global_var('func_841')
call_2798 = relay.TupleGetItem(func_839_call(), 1)
call_2799 = relay.TupleGetItem(func_841_call(), 1)
output = call_2798
output2 = call_2799
func_2811 = relay.Function([], output)
mod['func_2811'] = func_2811
mod = relay.transform.InferType()(mod)
mutated_mod['func_2811'] = func_2811
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2811_call = mutated_mod.get_global_var('func_2811')
call_2812 = func_2811_call()
output = call_2812
func_2813 = relay.Function([], output)
mutated_mod['func_2813'] = func_2813
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2204_call = mod.get_global_var('func_2204')
func_2206_call = mutated_mod.get_global_var('func_2206')
call_2876 = func_2204_call()
call_2877 = func_2204_call()
uop_2881 = relay.acos(call_2876.astype('float32')) # shape=(16, 6, 4)
uop_2883 = relay.acos(call_2877.astype('float32')) # shape=(16, 6, 4)
func_244_call = mod.get_global_var('func_244')
func_246_call = mutated_mod.get_global_var('func_246')
var_2885 = relay.var("var_2885", dtype = "int8", shape = (264,))#candidate|2885|(264,)|var|int8
call_2884 = relay.TupleGetItem(func_244_call(relay.reshape(var_2885.astype('int8'), [4, 6, 11])), 0)
call_2886 = relay.TupleGetItem(func_246_call(relay.reshape(var_2885.astype('int8'), [4, 6, 11])), 0)
output = relay.Tuple([uop_2881,call_2884,var_2885,])
output2 = relay.Tuple([uop_2883,call_2886,var_2885,])
func_2889 = relay.Function([var_2885,], output)
mod['func_2889'] = func_2889
mod = relay.transform.InferType()(mod)
var_2890 = relay.var("var_2890", dtype = "int8", shape = (264,))#candidate|2890|(264,)|var|int8
output = func_2889(var_2890)
func_2891 = relay.Function([var_2890], output)
mutated_mod['func_2891'] = func_2891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1319_call = mod.get_global_var('func_1319')
func_1320_call = mutated_mod.get_global_var('func_1320')
call_2911 = func_1319_call()
call_2912 = func_1319_call()
func_1871_call = mod.get_global_var('func_1871')
func_1874_call = mutated_mod.get_global_var('func_1874')
var_2939 = relay.var("var_2939", dtype = "int8", shape = (6, 44))#candidate|2939|(6, 44)|var|int8
call_2938 = relay.TupleGetItem(func_1871_call(relay.reshape(var_2939.astype('int8'), [264,])), 1)
call_2940 = relay.TupleGetItem(func_1874_call(relay.reshape(var_2939.astype('int8'), [264,])), 1)
const_2947 = relay.const([-3,2,8,-6,-2,-7,10,3,-9,2,-3,-3,3,-9,5,8,-10,5,4,10,-2,5,7,10,4,3,1,4,7,-10,3,-10,8,2,9,-10,-8,-2,2,-2,-6,-6,1,2,3,2,-1,10,10,-3,-1,9,-9,4,-5,-10,3,9,-5,-2,6,-4,-8,6,4,6,-4,7,-6,-9,-9,-5,6,-6,6,9,4,8,-8,10,6,9,1,-7,9,9,4,10,-7,-1,4,4,3,-10,8,5,5,6,-2,-2,-7,-10,-2,-1,7,-1,-1,-1,-9,-7,4,-3,-8,5,-9,2,8,1,2,-1,5,2,-9,2,7,-8,-3,-9,7,-4,3,-6,-8,2,-8,-9,-7,9,-7,7,-4,4,-4,-10,-9,9,2,2,2,-10,-7,3,1,1,7,-1,-10,8,-7,7,5,-7,-1,7,-3,4,-5,5,3,3,3,-10,-8,-9,9,1,1,-2,-5,6,5,1,10,-5,3,4,-3,-8,-3,6,-2,7,-4,-6,8,-8,-3,-3,4,-6,10,-2,-4,-4,9,10,-6,3,-8,1,-10,-8,-10,5,-3,-1,-3,-5,-5,-6,10,6,-5,-6,-9,-8,7,-3,1,1,1,8,-6,2,4,6,6,-10,10,-3,-4,-7,8,-6,-9,2,8,5,5,-5,-5,-2,2,1,9,-10,-4,-4,8,1,8,7,-5,1], dtype = "int8")#candidate|2947|(264,)|const|int8
bop_2948 = relay.floor_divide(call_2938.astype('float32'), relay.reshape(const_2947.astype('float32'), relay.shape_of(call_2938))) # shape=(264,)
bop_2951 = relay.floor_divide(call_2940.astype('float32'), relay.reshape(const_2947.astype('float32'), relay.shape_of(call_2940))) # shape=(264,)
uop_2952 = relay.erf(var_2939.astype('float32')) # shape=(6, 44)
bop_2957 = relay.power(uop_2952.astype('float32'), relay.reshape(const_2947.astype('float32'), relay.shape_of(uop_2952))) # shape=(6, 44)
output = relay.Tuple([call_2911,bop_2948,bop_2957,])
output2 = relay.Tuple([call_2912,bop_2951,bop_2957,])
func_2973 = relay.Function([var_2939,], output)
mod['func_2973'] = func_2973
mod = relay.transform.InferType()(mod)
var_2974 = relay.var("var_2974", dtype = "int8", shape = (6, 44))#candidate|2974|(6, 44)|var|int8
output = func_2973(var_2974)
func_2975 = relay.Function([var_2974], output)
mutated_mod['func_2975'] = func_2975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1112_call = mod.get_global_var('func_1112')
func_1114_call = mutated_mod.get_global_var('func_1114')
call_3022 = relay.TupleGetItem(func_1112_call(), 2)
call_3023 = relay.TupleGetItem(func_1114_call(), 2)
func_1545_call = mod.get_global_var('func_1545')
func_1548_call = mutated_mod.get_global_var('func_1548')
const_3025 = relay.const([[-7.618682,9.218392,8.814943,5.023312,-1.898838,6.839282,9.366867,8.445240,-9.512964,2.887893,4.181434,9.468627,-8.785428,6.340105,5.868233,-7.838273,-5.652412,6.485120,-9.771906,6.503980,-4.777161,-6.281758,-9.198814,-7.145044,-0.001870,2.727655,1.657736,-0.199220,1.082853,-8.522895],[9.381555,-6.790607,0.967871,7.807077,-5.086093,-8.259580,1.812313,-5.335852,3.437082,6.442321,-7.473856,3.166737,4.954317,9.499206,-4.549291,5.516060,1.591204,7.435663,-6.427776,-1.387794,-4.170717,3.583138,-6.808548,5.462637,8.905020,3.058893,2.036884,4.464375,7.264339,1.024405],[8.671722,2.892378,-6.237031,5.667329,-5.514599,6.049678,-7.192912,-7.883656,-3.549345,-2.686771,-3.126710,9.173990,6.847609,-4.281733,-2.977589,-5.440367,9.439025,-1.332384,-4.883255,-6.015595,7.608601,6.875809,-6.770950,-2.731442,-6.192699,-8.813499,4.096306,-4.694171,9.979331,9.807964],[4.553455,5.959096,1.424514,-3.030828,3.957203,-8.701600,0.887105,-7.023865,-4.989954,-0.585469,-4.452222,0.386854,3.266981,-1.081120,0.947092,-2.218793,3.634832,0.687924,5.186301,-5.567898,-5.031950,5.477653,2.950988,1.555915,7.792765,-1.688801,9.023820,8.023504,5.694130,4.337617],[8.166291,9.973048,9.108077,9.023157,8.189256,7.702519,8.062189,5.738355,-5.948617,-9.893740,-2.460334,7.641890,-1.995074,-0.297069,-0.516706,-1.241817,0.987876,-3.317867,-6.506196,8.752958,-6.618025,0.658403,-0.451958,-2.118138,-7.853814,-2.515021,6.383217,-6.018640,-8.341256,3.165876],[-4.283253,-3.103685,-0.761271,-5.363433,-4.960180,-7.782348,-2.501085,-7.888924,-0.720524,9.623295,1.272144,1.071643,-6.170809,8.607252,1.445723,7.143066,-9.287078,1.246820,9.302020,-1.765752,-6.359681,-5.570187,-8.446536,9.090743,8.038635,5.418860,-4.967365,2.200364,-0.907583,7.495078],[8.828915,2.757124,-0.955392,-2.938956,-5.783010,4.499875,8.591145,7.529477,9.478271,-6.186714,-3.078327,8.972623,9.454897,4.727573,5.091478,3.821304,9.406709,5.526583,9.724535,0.939827,-2.013423,-8.531376,-5.081275,4.476527,-2.969906,-0.548621,-6.407896,7.110111,-5.480734,5.714654],[8.850909,9.490756,-5.181872,-7.281442,-4.059992,8.257495,2.309319,8.694609,-9.588822,9.162527,-3.266601,7.444498,8.104368,-5.233485,8.675299,-3.703837,-5.041992,6.187102,-2.374287,3.795782,-5.311584,2.113875,-3.510863,2.344115,1.786447,-7.468580,4.707785,-9.153010,-8.913158,-5.964815],[5.450420,2.211156,-7.573857,-1.618718,-7.312150,-4.218954,-0.518859,-8.110880,-7.129020,5.368115,-5.226658,1.726762,4.305433,1.238692,6.037669,4.792395,-2.060444,-4.711248,-6.766745,4.728337,-5.054272,5.275348,5.253967,-1.410127,7.252552,2.738141,3.718172,4.361092,8.366037,-1.430996],[6.039278,2.274916,-8.997032,-0.620111,-9.029583,-5.550474,9.676587,2.846849,2.649994,-9.942671,-1.050829,5.041188,0.134610,-9.457252,2.941314,1.627187,6.925380,-9.895463,-6.187990,-7.154537,-9.227470,-0.551848,-5.091165,-3.295832,4.485276,-5.043392,-4.729902,2.818511,3.985293,-2.836963],[-0.976180,7.234325,-3.502245,-8.028112,-0.747500,3.363995,8.484446,8.970551,-5.807464,8.566486,-0.560723,3.092036,5.998802,-0.960677,-9.333426,9.508035,-1.324671,-9.980263,-6.825410,-7.980535,4.768254,9.241259,4.986339,-7.873869,-2.164572,4.963823,-2.151250,-7.014900,8.426488,-0.547570],[6.221510,-7.000876,-4.267853,7.371363,4.757710,2.778381,5.866483,3.810832,3.430806,-3.165398,-3.283565,7.172491,-1.084581,-5.849419,-8.287135,-9.736160,1.363536,-5.498593,8.261624,-9.478633,9.840280,-1.485078,0.338504,4.501896,9.668241,-5.170567,4.275517,-7.784313,5.031768,6.448621],[7.871764,-7.496359,-8.503869,-3.617986,-9.271387,6.441902,4.720472,-1.587587,4.050396,1.822421,-5.754220,-3.718598,6.970597,1.376577,-1.336461,9.172169,-6.311141,-5.622555,-1.227088,1.273511,7.425157,-5.237317,-3.059080,9.526457,-8.247191,-7.719191,9.784446,-5.185389,-3.717423,7.693747],[-5.298241,-9.264080,-9.330878,3.919859,-7.100460,2.188187,1.397668,-3.528433,3.386581,-1.468380,-9.947421,-0.900910,8.040118,4.798591,-8.870091,-6.990136,9.634127,-9.013586,1.202167,-0.203885,-1.510393,-5.106986,3.771701,0.935442,-3.520291,-3.617487,-8.548428,-5.618683,9.585601,4.163057],[5.465198,-3.420366,2.176115,-5.526934,-5.228098,-1.983312,0.861031,8.285375,9.660296,0.185445,-2.115916,-6.121795,-0.627750,-8.925395,-5.866893,3.091954,-8.556031,-8.656953,-6.316441,-5.963550,5.731406,4.819742,2.848441,6.895824,3.711637,4.594587,-5.022511,9.051284,-1.769120,-3.342686],[3.138526,-6.899451,8.113009,2.508507,-0.512654,0.285454,-1.967612,-8.193951,4.896534,-2.316798,-0.279751,-9.250952,-0.098048,0.757732,9.719237,9.486871,6.075639,-9.968242,3.614062,3.483545,-7.476256,5.835711,9.076052,-1.804733,-1.416727,-7.072410,-9.914958,5.479546,-4.766221,-5.431237],[5.923008,-7.759670,8.090320,2.213257,8.570507,-6.249320,8.471499,-7.351910,7.028523,0.596236,-2.701466,-2.866330,-2.983031,6.178038,-8.140533,5.196060,3.365120,9.238649,-3.233283,5.257615,5.895697,4.128426,-9.207264,7.775546,0.493418,5.771805,-4.422817,-3.253902,6.533198,7.353486],[7.941839,9.556110,6.237969,-6.652170,-3.232887,5.240791,6.464543,-4.385004,-2.052375,-5.933351,7.554094,3.359908,7.881562,-6.958433,0.463993,7.724463,-1.137696,-0.513196,6.116185,-6.566890,-2.481010,9.412313,-9.945974,3.384459,9.038313,-5.841293,9.853702,5.805036,-8.053560,-7.789439]], dtype = "float64")#candidate|3025|(18, 30)|const|float64
call_3024 = relay.TupleGetItem(func_1545_call(relay.reshape(const_3025.astype('float64'), [9, 4, 15]), relay.reshape(const_3025.astype('float64'), [9, 4, 15]), ), 0)
call_3026 = relay.TupleGetItem(func_1548_call(relay.reshape(const_3025.astype('float64'), [9, 4, 15]), relay.reshape(const_3025.astype('float64'), [9, 4, 15]), ), 0)
output = relay.Tuple([call_3022,call_3024,const_3025,])
output2 = relay.Tuple([call_3023,call_3026,const_3025,])
func_3033 = relay.Function([], output)
mod['func_3033'] = func_3033
mod = relay.transform.InferType()(mod)
mutated_mod['func_3033'] = func_3033
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3033_call = mutated_mod.get_global_var('func_3033')
call_3034 = func_3033_call()
output = call_3034
func_3035 = relay.Function([], output)
mutated_mod['func_3035'] = func_3035
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2581_call = mod.get_global_var('func_2581')
func_2583_call = mutated_mod.get_global_var('func_2583')
call_3059 = relay.TupleGetItem(func_2581_call(), 1)
call_3060 = relay.TupleGetItem(func_2583_call(), 1)
output = call_3059
output2 = call_3060
func_3074 = relay.Function([], output)
mod['func_3074'] = func_3074
mod = relay.transform.InferType()(mod)
mutated_mod['func_3074'] = func_3074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3074_call = mutated_mod.get_global_var('func_3074')
call_3075 = func_3074_call()
output = call_3075
func_3076 = relay.Function([], output)
mutated_mod['func_3076'] = func_3076
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3086 = relay.var("var_3086", dtype = "float32", shape = (6, 14, 12))#candidate|3086|(6, 14, 12)|var|float32
uop_3087 = relay.atan(var_3086.astype('float32')) # shape=(6, 14, 12)
const_3091 = relay.const([[[1.514749,9.717013,-0.833985,-4.715915,-0.499471,7.752534,-2.107584,-2.995248,-6.324141,-1.502219,-7.741302,2.440951],[3.353804,7.761256,-4.246380,-8.247152,0.876637,5.319485,2.301784,8.783857,-6.831224,8.069558,0.876528,-0.595087],[-2.177213,-9.274517,3.421244,-4.419618,-8.391415,-8.052948,0.296132,-0.612879,2.404944,-9.944587,-9.310981,-1.275369],[-2.259478,7.308831,-1.543998,3.726088,-6.169131,6.129794,-6.382268,3.696194,3.054472,8.255370,-0.875704,5.738787],[-2.320831,-7.916251,-0.554780,6.534536,-5.201338,-8.481943,8.975387,-6.086881,-5.693331,5.735651,7.801506,8.231695],[-3.278373,7.512710,-3.818203,-6.478223,-0.900353,4.542728,-4.971373,2.861913,-8.149449,9.828118,-2.165188,3.669865],[6.200119,6.618567,9.022221,8.986275,0.165023,2.334436,-2.211044,-1.397189,-8.659550,4.950111,3.487397,-9.206681],[-8.459902,1.749617,8.490185,5.445458,0.188932,4.976049,9.708418,-2.086105,-0.485832,4.007799,-5.154895,4.472560],[5.021222,5.318694,-7.256486,-6.253316,6.543660,7.387290,5.115412,2.664993,0.253082,6.670815,0.126145,8.844494],[2.441269,-0.175756,1.698274,4.085992,-2.693299,1.928347,-9.857816,-5.518970,6.824805,-9.550066,-5.055880,1.769386],[-0.361861,9.224038,-2.073969,2.106002,7.255268,2.393350,-2.524571,1.862278,6.717610,2.296894,3.510578,7.072619],[0.641194,6.002296,3.654038,2.426968,3.698863,-5.052609,5.958336,-1.378142,3.976021,2.842317,-6.678834,9.952823],[3.299662,3.472254,-4.749185,3.418633,-3.152751,6.158985,1.982298,7.429030,4.485542,0.381276,-1.963432,9.825817],[3.043212,8.465761,-9.896503,-7.448515,5.740062,-5.843898,-2.414246,3.574824,-9.354739,4.447034,4.477057,-2.465544]],[[-3.076268,5.190672,3.357932,-7.936050,-1.696204,-7.452508,-5.279324,-5.905283,-7.795332,0.556012,6.686886,6.785168],[-9.291482,2.149636,-3.878436,-8.743779,5.350581,4.650458,3.183960,-9.131956,1.290450,-1.730678,2.849803,7.102478],[0.770636,-3.677148,4.853875,-7.686397,-0.223442,6.171574,9.456631,5.100420,4.004275,-8.731021,4.564134,-5.750713],[0.953436,-2.620898,-3.637290,5.593336,3.164811,-8.223700,0.880143,-5.917790,-6.630286,-7.574173,3.461830,6.394286],[-5.480783,7.855394,-5.997223,-7.511067,-6.245862,-8.421426,-0.330687,-1.367395,4.360353,-9.709244,8.974689,6.684186],[-2.052983,-6.095001,3.429509,2.383107,6.511841,4.953223,-0.564710,8.546866,3.442025,3.566872,3.954472,1.529519],[-2.919853,-3.884945,-5.193012,-8.061915,8.362043,-7.414704,-5.207568,5.290558,1.180075,7.422534,-8.476991,-8.090024],[-2.835446,-0.164306,-6.440677,-8.469935,9.189656,-8.447271,-6.345967,2.928343,5.293090,5.952332,5.241245,8.421728],[8.915575,-4.943205,-2.621226,5.628730,6.828602,-3.991945,2.419119,-4.200226,5.350273,-8.825805,8.563827,-0.796440],[-3.850480,-3.397233,-7.506263,-9.598664,-5.224504,4.834654,1.076940,8.236310,-0.124881,-5.290271,7.002117,7.702161],[-6.542028,-6.737780,5.994368,-8.881920,-6.580376,5.126767,9.676775,2.689983,-5.034676,-7.884337,7.766827,-4.709491],[8.569431,-8.933826,-6.090434,-7.407142,1.449072,-8.279294,9.363003,-3.878668,-6.632384,-4.841054,0.948087,0.986890],[-7.949731,-6.662946,-2.431627,-7.116338,7.364584,-8.163457,-6.713069,-7.658683,6.633375,-5.817706,-6.312875,5.765188],[-4.509580,-5.151170,3.849098,7.946852,6.322412,4.392205,5.772537,9.032483,-2.974531,-2.214617,-7.081948,7.384319]],[[6.460325,-4.887308,-5.748450,-5.637210,0.820164,0.890779,6.075592,6.815758,-1.551607,-4.898246,-4.928772,-0.965019],[5.545690,0.486987,-9.586206,7.024813,-2.422489,2.642038,7.757590,2.434036,-2.035199,3.068570,9.351949,-5.168189],[-6.112948,8.602711,-7.370869,7.020958,-9.105560,-5.708614,9.544555,5.163477,9.299388,7.611046,-2.068292,-6.228892],[5.573596,-1.749031,-2.172198,-6.429228,2.089022,3.672107,9.636712,2.177802,7.324787,-6.787797,-5.050178,-9.264265],[-2.541359,-6.551918,-5.454147,9.573603,8.842741,-5.375887,-2.965789,-3.728669,4.535008,-4.710993,-5.135180,-1.856087],[3.255962,8.723053,-3.254341,1.833153,9.709983,-2.280352,-6.839011,3.438691,9.430006,7.093213,-1.311040,-0.800161],[4.919149,-2.384193,-6.721295,2.227005,-0.434375,2.699177,-0.487442,3.043234,5.353874,8.383312,-2.918671,9.107314],[2.667550,9.843508,-9.652942,6.335386,-8.449420,2.626020,-9.740901,-0.808367,2.735617,-8.006834,3.942442,5.663546],[1.710217,-2.554519,7.017839,9.549791,5.371179,-1.940430,-3.529674,7.577524,-8.214352,-3.537847,-6.022092,7.651865],[-1.966857,9.372679,0.593071,-0.109619,-1.791671,-8.826502,-6.967353,-5.535030,0.740982,7.144006,-7.780187,-4.062527],[-6.645886,5.922625,-6.699341,-4.335715,-5.454977,-2.382636,8.113074,-0.235865,9.758691,8.185201,5.395031,9.683947],[2.889621,-5.746645,-6.430477,-9.772585,9.750509,2.365797,-5.688629,6.563728,2.096861,-8.163907,-7.267156,-2.981966],[-1.332189,-7.912849,1.332825,-2.453157,-4.127998,-7.671516,7.488321,5.794948,2.709969,-9.407731,8.815737,-3.155141],[1.322261,8.552170,-3.397543,-8.643606,3.547017,-1.898730,-7.005544,0.912631,0.939146,5.433375,-3.415797,-9.944868]],[[1.929886,7.724231,-1.422686,-1.562012,4.279896,4.158361,8.661347,-2.389900,-8.201828,-7.425805,4.294648,-0.830422],[7.515410,8.197420,-7.384430,8.813319,7.563742,-4.190925,9.327720,2.429614,-6.604161,-2.303466,-3.056504,1.556876],[3.287028,-5.884617,1.651706,0.574899,-7.247618,5.875159,-8.843681,7.842531,5.203358,3.234675,-8.015167,0.404134],[-9.213736,-7.211745,-7.690077,8.065889,2.825685,-8.214226,-2.435125,-5.586464,5.535458,-1.466833,-2.317176,0.076820],[8.944086,-7.584089,6.832653,3.589756,4.711151,1.508166,6.695127,4.211877,-6.893208,6.679638,-2.332653,6.282487],[2.707148,0.503252,0.480912,-4.391678,-3.784539,-2.112739,-8.571731,9.837736,-6.250325,-7.021173,3.011382,-7.714863],[5.469446,6.778176,4.855850,9.854579,-7.973651,9.946116,9.439399,-3.757611,-9.918650,-1.101846,-5.810616,3.286405],[-3.577079,-2.295586,6.935184,9.711445,6.818969,-6.791485,8.980167,6.872162,3.707109,-2.681289,-6.660373,-2.975283],[8.325857,-1.219551,-9.266471,-9.122018,2.606338,-3.442753,-0.661880,0.293959,-9.371038,-2.696618,-9.372616,2.045702],[-8.650292,-3.076235,8.330213,-9.860377,8.784504,-2.047351,-9.083191,-6.442122,-9.997652,-3.660793,-6.135145,-1.571427],[-9.447842,5.566587,-7.492597,-5.363970,-1.199730,-6.517422,7.224277,-9.524003,7.825773,-4.012400,-9.313774,2.539028],[9.607191,6.258875,9.872783,7.976183,-4.877456,-9.028966,6.770131,-9.804497,-9.680862,1.936109,6.260022,-8.177331],[3.648757,-8.598879,-3.115325,-5.143387,8.662400,7.932913,7.861182,-4.549562,0.394901,-0.434130,9.940866,-9.503145],[7.790191,6.664882,-5.334777,3.833486,-4.950641,1.337987,6.963092,2.243749,7.969126,-0.842679,5.626076,-2.172569]],[[2.634731,2.960067,9.158126,-6.640651,-5.157221,0.237656,-5.827386,-4.384970,-6.249521,2.237767,8.485037,5.232005],[7.263074,9.027726,-4.589473,-1.330784,-2.716926,9.169989,5.610393,8.834063,1.567305,-6.989834,9.413602,5.267225],[-1.794618,-4.873234,8.109317,-9.164318,5.852324,6.661706,-7.211827,1.572240,8.244893,-7.311658,7.694922,-8.554937],[2.161927,-0.396012,1.464479,-1.909749,-1.197552,4.338418,-7.661340,-0.907785,7.629908,-8.223492,5.613409,8.338159],[-0.789392,-3.085367,1.133228,-6.781619,6.901245,8.680697,-4.107642,1.342102,-1.567112,-1.167472,-4.538408,-6.082872],[-4.739159,3.686890,3.382792,1.644509,8.691771,4.004861,-2.369753,4.255327,-0.458695,7.183889,-7.443011,6.391731],[2.839627,-8.354465,-5.688999,-3.326664,8.726200,5.730783,-8.618161,-1.632155,-2.604120,-4.971255,8.667067,-5.525236],[-6.104394,7.347513,-1.636919,-5.785249,-4.197627,-3.967472,5.241597,-7.775946,-1.656517,3.334164,-4.486883,-8.230482],[1.916992,7.193576,-9.235856,-5.089257,0.408796,-8.371806,-3.655422,-6.558609,0.257335,-2.699316,5.603109,7.035797],[-1.350838,-1.869571,-6.310689,9.265432,9.107747,-2.407312,-9.317356,-5.609410,-2.910320,-6.843227,6.473721,-2.684188],[3.682557,-6.047344,7.293859,-2.344209,-1.002558,-3.148929,-9.349724,7.379448,-9.849663,1.925397,-1.213754,1.484326],[-1.476214,-4.734882,-4.311855,-5.790135,0.441316,-7.426052,-3.141161,-3.321027,0.635772,5.514143,-0.579324,6.286604],[2.234052,1.045959,-6.311012,-5.907141,-0.928929,3.318698,8.501387,-9.319001,-4.452802,4.755072,-9.930645,3.148554],[-1.822188,6.183754,6.118593,-8.983112,7.342229,6.806702,-8.883833,5.390121,-4.984686,1.111268,-4.686733,-5.213944]],[[-7.976454,-6.896375,9.772557,-4.714127,-9.986959,-5.148926,-3.519651,-2.591427,-1.727389,5.823070,-8.066652,-5.972150],[7.448376,-9.898114,0.956711,-2.822797,6.942682,-3.012726,1.511282,-3.838065,-9.579594,9.272460,2.393973,8.699374],[5.673734,-7.919269,4.548895,-1.558298,-8.016017,-9.033816,7.754079,1.677385,7.769360,9.141574,-8.567812,2.471386],[-3.595432,1.271310,-0.647981,-8.932268,-1.767738,6.305026,0.077423,-3.950996,5.131083,7.185863,-8.524195,6.040915],[7.361618,-2.145388,-6.966130,-2.060958,-1.862924,2.023447,-2.415457,8.915256,-4.965100,-9.670107,-1.697433,-4.454828],[-7.040917,0.898933,-5.325436,-5.219150,9.992086,-0.587183,-5.313532,9.791905,-7.575905,-4.815113,-3.936546,5.839770],[-2.487659,-7.935515,1.423918,-5.567400,-7.165704,-7.872733,-3.285271,-1.279160,0.466416,-4.710601,-4.508129,-6.959494],[-8.091095,5.449712,-6.959468,8.010283,2.599182,-6.874401,-0.255153,-5.664214,-0.674260,-6.807819,3.564304,-9.853769],[9.097347,5.207555,-1.366427,-7.623776,-9.466128,6.065923,8.797479,7.977960,-6.407389,8.332800,5.380449,-3.461125],[-0.307030,-5.324545,2.436370,-8.591839,8.042590,-3.953474,7.192078,-7.324406,3.032867,4.895556,6.168973,5.563104],[-0.206404,-2.570072,-2.407698,7.512957,2.345583,-1.495609,-7.965191,0.021456,-6.428087,-9.168888,4.512707,3.207235],[-9.562281,1.711765,-6.424511,-4.926817,5.604566,-0.108928,7.924308,-4.487116,0.428794,3.763411,3.907256,-1.336351],[3.424968,8.531030,0.973796,0.938880,0.209251,6.577628,4.128244,-3.942622,4.937031,-3.705441,-1.673721,5.971848],[9.458398,-2.784570,-0.642600,1.153494,6.823735,-4.196133,0.370415,-6.335730,-1.732020,-2.770266,0.232306,-9.341706]]], dtype = "float32")#candidate|3091|(6, 14, 12)|const|float32
bop_3092 = relay.bitwise_and(var_3086.astype('int32'), relay.reshape(const_3091.astype('int32'), relay.shape_of(var_3086))) # shape=(6, 14, 12)
func_2643_call = mod.get_global_var('func_2643')
func_2646_call = mutated_mod.get_global_var('func_2646')
const_3105 = relay.const([8,2,5,10,6,-2,-8,10,-10,10,4,-6,-5,6,10,-7,1,4,7,-5,5,-9,-2,7,-3,-3,-4,-6,7,2,3,8,3,10,-5,10,-2,3,1,5,6,9,-1,1,-6,7,-4,-5,-6,-4,10,1,6,-6,-3,-1,3,8,-6,1,-4,3,-3,5,-3,-10,-5,-5,-6,-8,-5,7,10,9,-6,9,-9,8,-1,1,1,9,4,-9,-8,-9,-7,-9,4,2,-10,-10,3,1,8,-10,-5,7,4,2,-2,-4,-9,-5,-3,-3,-9,-10,-10,6,4,8,-6,3,-10,1,7,-2,-10,-1,5,-4,8,7,-4,5,1,-9,8,-7,6,2,-5,2,-1,-8,7,-3,5,-3,4,-9,3,4,-10,2,2,1,-8,5,-8,-10,-3,1,4,9,4,-7,-5,-8,3,-1,6,2,-7,-7,-10,-9,9,-2,-4,3,8,4,-10,-10,-4,7,5,6,-8,6,-10,-2,-6,4,-5,9,8,9,-6,10,-10,-10,6,-8,10,2,-2,1,-9,10,-3,-9,10,10,9,-6,6,-7,-5,-7,-10,5,1,9,-2,-6,-8,7,-5,6,6,6,-1,4,-5,-8,-10,-6,-8,3,-6,6,-5,3,-9,-5,-2,-7,-3,6,-4,4,9,6,-7,-9,1,-8,-6,6,10,2,-4,5,-2,7,7,-1,-3,4,-10,-4,8,-7,3,-2,7,-8,-5,-10,6,-4,-9,9,-3,-4,8,4,-2,-10,4,-9,-6,-2,10,7,-9,8,5,2,2,1,-5,-6,5,1,8,8,7,-6,-2,-4,5,9,-1,7,8,-3,-2,10,-5,-5,-1,10,5,-6,8,-5,9,-2,-6,4,-7,-7,-8,-8,-7,9,-8,-5,-4,7,8,4,8,10,4,-8,-2,4,1,6,-5,-6,-3,-5,10,8,5,-9,-7,9,-2,-4,3,8,-10,-1,-1,-9,8,1,7,7,-3,-9,5,4,6,-4,8,4,-8,4,-4,4,-6,-1,6,6,-4,10,2,9,-1,-6,4,-6,7,-2,10,2,-10,-10,-10,-4,1,6,-7,1,7,-7,-1,5,-1,-8,2,-9,-4,-9,-7,-1,-6,-2,-3,10,-4,4,8,-3,6,-1,5,1,1,6,-2,6,7,2,5,-9,-9,-4,2,-7,1,9,8,-5,-1,-4,-9,2,10,-5,5,4,7,-2,-5,9,5,-10,-9,1,-8,-4,7,3,1,-2,2,-2,-6,-9,-1,5,-10,8,-3,-1,6,-8,-1,-2,-6,1,-2,8,5,-7,10,4,-10,-9,-1,-2,6,-10,10,1,6,-6,3,6,-3,-6,-8,3,3,9,-4,3,-2,9,6,-9,-2,-3,-1,6,-4,9,5,8,-5,3,1,-3,10,-4,-4,9,10,-2,10,4,-2,-6,4,4,4,-3,5,7,-10,2,-5,-1,-4,5,2,-10,2,-1,3,-10,-5,9,10,5,-6,-5,7,-8,-2,-7,-2,-1,4,-3,-9,3,7,-2,-9,-7,4,-7,-10,4,-6,8,-9,-4,-1,1,1,2,5,5,2,10,-5,-1,-2,9,-7,7,4,-10,-10,4,4,-9,3,6,7,-3,2,9,8,-1,-3,-2,10,3,-4,1,-5,10,4,5,-9,4,-2,-3,-1,5,3,-2,-9,4,1,3,6,6,-7,-1,-9,8,-10,-2,-7,4,4,4,-10,-9,4,1,-5,-9,-9,-9,-7,-10,7,-5,-8,-4,-4,8,-9,-5,8,2,-2,-6,-1,-9,-1,3,-10,-2,-7,1,-9,5,5,-10,7,-8,10,2,-10,-8,-2,9,-9,-2,-1,10,-1,5,-7,3,-4,-5,-7,-6,9,-8,-4,5,-9,-4,10,-8,10,-1,8,-3,6,-7,-8,-10,8,10,-6,-7,-3,-5,4,-8,-9,-1,4,9,3,-5,-10,8,4,10], dtype = "int16")#candidate|3105|(728,)|const|int16
call_3104 = relay.TupleGetItem(func_2643_call(relay.reshape(const_3105.astype('int16'), [4, 14, 13]), relay.reshape(const_3105.astype('int16'), [4, 14, 13]), ), 0)
call_3106 = relay.TupleGetItem(func_2646_call(relay.reshape(const_3105.astype('int16'), [4, 14, 13]), relay.reshape(const_3105.astype('int16'), [4, 14, 13]), ), 0)
var_3107 = relay.var("var_3107", dtype = "float32", shape = (6, 14, 12))#candidate|3107|(6, 14, 12)|var|float32
bop_3108 = relay.equal(uop_3087.astype('bool'), relay.reshape(var_3107.astype('bool'), relay.shape_of(uop_3087))) # shape=(6, 14, 12)
uop_3112 = relay.sigmoid(var_3086.astype('float32')) # shape=(6, 14, 12)
func_2261_call = mod.get_global_var('func_2261')
func_2264_call = mutated_mod.get_global_var('func_2264')
const_3116 = relay.const(-9, dtype = "uint32")#candidate|3116|()|const|uint32
var_3117 = relay.var("var_3117", dtype = "uint32", shape = (128,))#candidate|3117|(128,)|var|uint32
call_3115 = func_2261_call(relay.reshape(const_3116.astype('uint32'), []), relay.reshape(var_3117.astype('uint32'), [8, 16]), )
call_3118 = func_2261_call(relay.reshape(const_3116.astype('uint32'), []), relay.reshape(var_3117.astype('uint32'), [8, 16]), )
uop_3119 = relay.erf(bop_3092.astype('float32')) # shape=(6, 14, 12)
func_2174_call = mod.get_global_var('func_2174')
func_2177_call = mutated_mod.get_global_var('func_2177')
const_3125 = relay.const([[1.314719],[-4.491112],[-9.223675],[-7.234356],[-8.087173],[-3.764984],[-0.644169],[-9.804202],[5.829583],[-9.947911],[-1.216343],[-2.350451],[-0.001540],[-3.016232],[-0.469662],[-0.610370],[-2.432978],[-1.945884],[8.000306],[4.634146],[7.678234],[-4.986058],[2.871130],[-8.461729],[-9.875733],[6.545698],[-6.723501],[-9.500865],[-7.302766],[9.655881],[5.779172],[-9.141383],[5.514845],[-8.238153],[3.734871],[-7.527651],[-4.439410],[-0.692415],[-0.559202],[-8.385444],[7.585563],[5.896308],[-7.271634],[7.540806],[0.421130],[1.460834],[-1.097970],[-4.551295],[4.002795],[-5.351384],[-5.501581],[9.670301],[-3.379344],[2.640320],[-0.112148],[2.615284],[1.321891],[2.572674],[-5.479554],[-1.354104],[-8.210736],[-9.358882],[1.364490],[-0.994236],[-1.475486],[7.163763],[7.506101],[2.040701],[-2.575577],[-3.269085],[-6.977621],[1.306982],[9.971186],[8.824998],[2.748789],[0.847573],[-9.828942],[-1.497575],[-6.000907],[-4.719659],[-3.174609],[1.895367],[-7.979988],[8.108324],[7.745369],[1.229521],[7.626394],[-5.862857],[0.149151],[8.404713],[2.404312],[-1.866746],[-9.382174],[-9.995568],[5.601383],[3.448069],[-2.116887],[-3.597529],[2.504362],[-5.261643],[3.728738],[8.005919],[-0.056729],[3.898645],[7.093052],[-9.006359],[3.202110],[-6.415852],[1.655856],[-8.273818],[3.144790],[-3.012036],[4.877952],[-8.436232],[-0.749696],[0.763276],[-8.773767],[7.671063],[-2.617325],[7.981726],[5.262411],[7.964418],[-6.957956],[-4.260232],[-1.082138],[9.837410],[8.835856],[4.069276],[-4.785551],[6.529907],[-0.629482],[-0.736065],[5.722512],[3.526410],[7.563254],[-3.735728],[-9.118429],[1.602268],[3.597839],[4.830142],[8.531781],[-2.433290],[-0.977177],[6.547094],[4.759152],[-7.148479],[1.373231],[0.474523],[-0.555804],[2.578564],[1.732635],[-8.760968],[5.092432],[-4.167291],[8.193869],[-8.383919],[-1.360900],[1.444028],[-8.876986],[6.486164],[-3.850633],[-8.942525],[9.403655],[-1.834571],[-1.412805],[3.273177],[2.549532],[-2.846807],[8.935875],[-1.131492],[-5.320835],[1.965400],[1.142866],[6.350182],[9.423574],[1.110271],[-0.377496],[-9.847529],[7.198477],[3.083089],[-9.892925],[0.450051],[-7.786430],[-1.569216],[7.496038],[9.409870],[6.459425],[-3.070754],[6.080407],[-3.160520],[4.166690],[-7.100907],[7.437531],[8.212410],[-4.793463],[9.124151],[8.690244],[-0.606177],[-4.020353],[0.802444],[4.410548],[6.768223],[-4.570192],[2.973642],[9.712302],[-4.926181],[-4.358595],[3.195988],[0.666835],[-3.727947],[1.274523],[-2.588972],[9.436298],[0.299433],[2.350359],[5.018391],[8.375225],[8.057511],[-5.946105],[2.134920],[1.688525],[-4.619342],[1.038945],[6.921280]], dtype = "float64")#candidate|3125|(224, 1)|const|float64
call_3124 = relay.TupleGetItem(func_2174_call(relay.reshape(const_3125.astype('float64'), [14, 4, 4]), relay.reshape(const_3125.astype('float64'), [14, 4, 4]), ), 0)
call_3126 = relay.TupleGetItem(func_2177_call(relay.reshape(const_3125.astype('float64'), [14, 4, 4]), relay.reshape(const_3125.astype('float64'), [14, 4, 4]), ), 0)
uop_3131 = relay.sinh(uop_3119.astype('float32')) # shape=(6, 14, 12)
func_1083_call = mod.get_global_var('func_1083')
func_1085_call = mutated_mod.get_global_var('func_1085')
call_3134 = relay.TupleGetItem(func_1083_call(), 2)
call_3135 = relay.TupleGetItem(func_1085_call(), 2)
output = relay.Tuple([call_3104,const_3105,bop_3108,uop_3112,call_3115,const_3116,var_3117,call_3124,const_3125,uop_3131,call_3134,])
output2 = relay.Tuple([call_3106,const_3105,bop_3108,uop_3112,call_3118,const_3116,var_3117,call_3126,const_3125,uop_3131,call_3135,])
func_3137 = relay.Function([var_3086,var_3107,var_3117,], output)
mod['func_3137'] = func_3137
mod = relay.transform.InferType()(mod)
var_3138 = relay.var("var_3138", dtype = "float32", shape = (6, 14, 12))#candidate|3138|(6, 14, 12)|var|float32
var_3139 = relay.var("var_3139", dtype = "float32", shape = (6, 14, 12))#candidate|3139|(6, 14, 12)|var|float32
var_3140 = relay.var("var_3140", dtype = "uint32", shape = (128,))#candidate|3140|(128,)|var|uint32
output = func_3137(var_3138,var_3139,var_3140,)
func_3141 = relay.Function([var_3138,var_3139,var_3140,], output)
mutated_mod['func_3141'] = func_3141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1083_call = mod.get_global_var('func_1083')
func_1085_call = mutated_mod.get_global_var('func_1085')
call_3152 = relay.TupleGetItem(func_1083_call(), 3)
call_3153 = relay.TupleGetItem(func_1085_call(), 3)
func_1620_call = mod.get_global_var('func_1620')
func_1622_call = mutated_mod.get_global_var('func_1622')
call_3158 = relay.TupleGetItem(func_1620_call(), 0)
call_3159 = relay.TupleGetItem(func_1622_call(), 0)
uop_3161 = relay.sinh(call_3158.astype('float32')) # shape=(630,)
uop_3163 = relay.sinh(call_3159.astype('float32')) # shape=(630,)
func_2204_call = mod.get_global_var('func_2204')
func_2206_call = mutated_mod.get_global_var('func_2206')
call_3166 = func_2204_call()
call_3167 = func_2204_call()
func_2581_call = mod.get_global_var('func_2581')
func_2583_call = mutated_mod.get_global_var('func_2583')
call_3174 = relay.TupleGetItem(func_2581_call(), 0)
call_3175 = relay.TupleGetItem(func_2583_call(), 0)
func_1174_call = mod.get_global_var('func_1174')
func_1178_call = mutated_mod.get_global_var('func_1178')
const_3179 = relay.const([-6,-8,9,7,2,-5,-1,-4,-4,8,5,10,1,1,10,5,-3,10,8,-5,5,7,-4,8,1,10,1,-9,-3,-2,-8,-9,-10,2,-10,10,8,-1,10,10,3,-1,-3,-1,-9,-9,7,-8,1,-5,-9,-6,2,-7,7,8,-9,-6,-7,9,7,-5,-8,-3,4,-9,3,-8,-3,9,-4,1,6,-8,-4,9,6,6,-8,2,7,5,-9,6,9,3,2,9,-1,1,5,-7,-5,-5,-3,4,-2,-1,3,-4,-3,-10,-1,5,7,9,7,10,-8,4,4,1,-7,7,-10,-6,8,-9,4,-2,1,2,-7,7,-9,-9,9,9,4,9,6,6,1,4,-1,-8,-10,-8,5,2,-8,-7,1,-4,5,-9,-9,7,-2,7,9,-4,6,-6,9,4,-1,6,-10,-8,-4,-6,-2,2,5,-7,-5,-5,-5,1,-3,3,6,5,-10,9,-10,6,9,7,-7,8,5,10,-6,-4,-6,2,-6,5,2,9,-10,-7,3,3,-8,10,6,-3,-3,-3,4,8,-4,8,-1,-1,4,-2,-2,6,7,3,-8,-8,-1,-9,-6,-9,-1,8,5,-5,-5,-5,1,7,7,-3,-4,5,10,4,-10,6,-9,-5,4,-3,-8,-8,-10,-9,4,-2,-1,-6,1,-8,-3,4,1,-6,9,5,-10,6,-7,8,7,2,7,10,7,8,-2,-2,2,-9,-1,-10,-9,-2,-1,10,8,-5,-9,4,-3,-8,7,-10,-9,-1,5,-3,10,-1,-4,1,10,-9,-1,4,7,8,3,-4,9,5,9,-8,-3,-9,7,-1,6,-7,4,2,5,-5,10,-1,7,2,-3,-4,-9,-1,5,-5,-3,9,-4,-9,10,7,5,8,-3,-7,-1,3,8,-8,8,-3,6,8,-2,10,3,2,7,-2,-2,-9,2,5,-5,-2,-6,4,6,5,1,9,-5,3,-1,-4,-4,6,-2,5,-5,10,1,-5,-8,-4,-8,-2,-4,-4,-8,9,-9,7,7,-1,-10,-6,-5,-7,-3,-1,-1,-3,7,-1,-6,-8,-5,-8,-8,5,-10,-8,-1,-9,3,-5,-4,-1,-6,8,3,10,-1,-10,-9,-9,-5,-3,2,-3,3,-1,-8,6,5,7,9,5,8,-3,10,6,-10,2,-3,7,4,-1,-2,-6,2,-6,3,-5,5,-7,-1,-10,2,-3,8,-10,-1,7,-7,-2,-8,-2,-8,-3,-6,-9,3,-7,3,1,1,-6,-2,6,7,10,4,8,10,6,4,-4,7,6,-3,-3,-8,-7,-3,-2,8,-8,6,6,-9,-4,10,-2,9,-8,4,-7,2,5,-6,8,8,8], dtype = "uint16")#candidate|3179|(504,)|const|uint16
call_3178 = relay.TupleGetItem(func_1174_call(relay.reshape(const_3179.astype('uint16'), [4, 9, 14]), relay.reshape(const_3179.astype('uint16'), [4, 9, 14]), ), 2)
call_3180 = relay.TupleGetItem(func_1178_call(relay.reshape(const_3179.astype('uint16'), [4, 9, 14]), relay.reshape(const_3179.astype('uint16'), [4, 9, 14]), ), 2)
func_2643_call = mod.get_global_var('func_2643')
func_2646_call = mutated_mod.get_global_var('func_2646')
const_3182 = relay.const([-3,-3,-7,-10,-7,8,-9,7,-6,8,8,-7,2,1,8,9,2,-6,-6,-5,3,8,-2,5,-7,1,10,2,-7,3,4,9,-6,6,-3,7,-4,7,10,-5,4,-2,7,-6,6,4,-3,-9,-7,-3,6,6,6,10,-7,3,-3,6,9,-8,1,-9,4,5,3,-4,9,10,7,-1,5,6,1,1,3,-6,-1,9,3,9,-4,-4,4,10,4,-4,9,8,-1,9,8,8,-10,-5,3,-6,6,1,4,9,-5,8,4,-4,-4,-7,-6,-2,-2,-9,10,3,5,-5,-7,8,9,6,1,8,-2,-8,10,7,6,8,-1,-9,4,7,8,3,-1,-1,-10,-10,4,3,7,-7,-7,-6,-3,-5,8,-8,9,-6,-4,-5,-7,-9,2,-6,-3,1,-5,8,-3,-7,-7,9,-8,-6,-3,-7,5,-3,9,5,10,3,4,-3,8,-8,-7,-1,-4,-9,10,-7,-3,10,-10,5,-1,-3,-2,2,10,-5,8,2,-6,9,9,9,-8,4,-5,6,-7,-3,-9,9,4,4,1,-4,-1,1,8,-9,-10,-2,10,-5,9,6,-2,7,8,-9,-1,3,5,9,-5,-10,1,-2,-2,-10,4,8,8,3,7,4,-5,10,-1,5,-7,-1,-9,-9,-9,-3,-2,8,-6,-7,-2,-3,-8,-9,1,-4,-1,5,7,2,-3,-8,5,9,4,-8,-9,-5,5,-5,-10,-5,2,-10,5,5,-6,-5,9,-6,-9,1,-7,-4,-10,9,6,10,5,8,-3,-10,-8,-4,8,-1,-2,7,-7,-2,-10,9,-6,-5,-1,2,10,5,-8,6,-8,-7,7,2,4,5,6,1,2,-4,1,-9,10,10,4,8,-10,4,8,5,1,-6,-3,10,3,10,-2,6,4,1,-1,-10,3,-10,2,-3,-7,-2,7,8,6,5,-7,-9,6,-9,-1,8,4,5,5,-1,-8,-5,-4,5,8,-7,3,-6,-8,-6,3,-2,-3,-5,6,3,8,9,10,2,-7,3,-5,-9,-3,3,-8,-2,-4,3,2,4,-3,-2,10,-1,2,-5,4,-1,8,4,1,-8,3,-4,7,-5,-2,3,10,9,1,-1,9,-1,-8,-2,3,3,-1,-10,-7,-9,5,-5,8,-9,9,4,-1,-4,2,-7,7,-8,9,5,7,6,-5,-9,4,-10,5,2,10,7,3,-4,4,-9,4,-10,5,2,-7,-3,-8,-6,8,1,6,-8,1,-9,6,1,-9,10,7,6,-5,-6,3,-6,-2,8,6,-6,10,6,-3,-3,-6,-10,6,-8,6,-2,10,9,6,9,-5,-10,2,8,-3,-2,5,5,-10,10,8,5,1,-9,3,-10,-5,-3,10,-4,4,3,8,9,-2,-3,3,6,2,-3,-3,5,-5,5,-10,8,3,-3,1,10,-1,4,9,-7,5,-7,-3,6,-1,-5,10,-6,9,7,-1,5,-7,7,-9,8,6,-4,-8,-9,3,-9,-9,9,4,8,-10,1,-10,-5,5,-4,-1,-8,-3,9,2,1,4,-7,-6,6,-8,3,-5,8,2,-9,-4,-3,5,-3,1,-6,5,-5,-10,5,8,-7,-8,1,1,-2,-8,-2,-8,-9,10,-6,-3,-6,-2,1,10,-2,-5,8,-2,10,7,4,8,6,3,3,-3,-8,-1,-4,9,1,9,-1,-2,-3,-5,-8,-10,-1,6,-8,-4,-1,-5,9,-1,7,2,10,-1,6,-10,8,-9,-5,-4,2,-7,-6,10,-6,8,10,1,5,-3,-5,5,2,-4,-9,-8,-8,-7,-9,2,9,-9,1,9,10,-8,2,10,-9,1,-5,-10,7,-7,-4,2,-10,-2,-10,6,-2,7,-8,-10,-3,5,-3,9,2,-6,9,-10,10,-8,5,-10,-8,5,-4,-3,7,3,4,-1,1,3,-5], dtype = "int16")#candidate|3182|(728,)|const|int16
call_3181 = relay.TupleGetItem(func_2643_call(relay.reshape(const_3182.astype('int16'), [4, 14, 13]), relay.reshape(const_3182.astype('int16'), [4, 14, 13]), ), 0)
call_3183 = relay.TupleGetItem(func_2646_call(relay.reshape(const_3182.astype('int16'), [4, 14, 13]), relay.reshape(const_3182.astype('int16'), [4, 14, 13]), ), 0)
output = relay.Tuple([call_3152,uop_3161,call_3166,call_3174,call_3178,const_3179,call_3181,const_3182,])
output2 = relay.Tuple([call_3153,uop_3163,call_3167,call_3175,call_3180,const_3179,call_3183,const_3182,])
func_3230 = relay.Function([], output)
mod['func_3230'] = func_3230
mod = relay.transform.InferType()(mod)
output = func_3230()
func_3231 = relay.Function([], output)
mutated_mod['func_3231'] = func_3231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1620_call = mod.get_global_var('func_1620')
func_1622_call = mutated_mod.get_global_var('func_1622')
call_3311 = relay.TupleGetItem(func_1620_call(), 0)
call_3312 = relay.TupleGetItem(func_1622_call(), 0)
output = relay.Tuple([call_3311,])
output2 = relay.Tuple([call_3312,])
func_3315 = relay.Function([], output)
mod['func_3315'] = func_3315
mod = relay.transform.InferType()(mod)
output = func_3315()
func_3316 = relay.Function([], output)
mutated_mod['func_3316'] = func_3316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_839_call = mod.get_global_var('func_839')
func_841_call = mutated_mod.get_global_var('func_841')
call_3367 = relay.TupleGetItem(func_839_call(), 0)
call_3368 = relay.TupleGetItem(func_841_call(), 0)
uop_3373 = relay.sin(call_3367.astype('float64')) # shape=(1, 7, 4)
uop_3375 = relay.sin(call_3368.astype('float64')) # shape=(1, 7, 4)
func_244_call = mod.get_global_var('func_244')
func_246_call = mutated_mod.get_global_var('func_246')
var_3392 = relay.var("var_3392", dtype = "int8", shape = (264,))#candidate|3392|(264,)|var|int8
call_3391 = relay.TupleGetItem(func_244_call(relay.reshape(var_3392.astype('int8'), [4, 6, 11])), 0)
call_3393 = relay.TupleGetItem(func_246_call(relay.reshape(var_3392.astype('int8'), [4, 6, 11])), 0)
uop_3398 = relay.log(call_3367.astype('float64')) # shape=(1, 7, 4)
uop_3400 = relay.log(call_3368.astype('float64')) # shape=(1, 7, 4)
bop_3405 = relay.equal(call_3391.astype('bool'), relay.reshape(var_3392.astype('bool'), relay.shape_of(call_3391))) # shape=(4, 6, 11)
bop_3408 = relay.equal(call_3393.astype('bool'), relay.reshape(var_3392.astype('bool'), relay.shape_of(call_3393))) # shape=(4, 6, 11)
output = relay.Tuple([uop_3373,uop_3398,bop_3405,])
output2 = relay.Tuple([uop_3375,uop_3400,bop_3408,])
func_3416 = relay.Function([var_3392,], output)
mod['func_3416'] = func_3416
mod = relay.transform.InferType()(mod)
var_3417 = relay.var("var_3417", dtype = "int8", shape = (264,))#candidate|3417|(264,)|var|int8
output = func_3416(var_3417)
func_3418 = relay.Function([var_3417], output)
mutated_mod['func_3418'] = func_3418
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3432 = relay.var("var_3432", dtype = "float32", shape = (4, 11, 2))#candidate|3432|(4, 11, 2)|var|float32
uop_3433 = relay.cos(var_3432.astype('float32')) # shape=(4, 11, 2)
bop_3438 = relay.not_equal(uop_3433.astype('bool'), relay.reshape(var_3432.astype('bool'), relay.shape_of(uop_3433))) # shape=(4, 11, 2)
uop_3443 = relay.sinh(var_3432.astype('float64')) # shape=(4, 11, 2)
func_1253_call = mod.get_global_var('func_1253')
func_1255_call = mutated_mod.get_global_var('func_1255')
var_3453 = relay.var("var_3453", dtype = "int8", shape = (132, 2))#candidate|3453|(132, 2)|var|int8
call_3452 = relay.TupleGetItem(func_1253_call(relay.reshape(var_3453.astype('int8'), [264,])), 1)
call_3454 = relay.TupleGetItem(func_1255_call(relay.reshape(var_3453.astype('int8'), [264,])), 1)
output = relay.Tuple([bop_3438,uop_3443,call_3452,var_3453,])
output2 = relay.Tuple([bop_3438,uop_3443,call_3454,var_3453,])
func_3459 = relay.Function([var_3432,var_3453,], output)
mod['func_3459'] = func_3459
mod = relay.transform.InferType()(mod)
mutated_mod['func_3459'] = func_3459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3459_call = mutated_mod.get_global_var('func_3459')
var_3461 = relay.var("var_3461", dtype = "float32", shape = (4, 11, 2))#candidate|3461|(4, 11, 2)|var|float32
var_3462 = relay.var("var_3462", dtype = "int8", shape = (132, 2))#candidate|3462|(132, 2)|var|int8
call_3460 = func_3459_call(var_3461,var_3462,)
output = call_3460
func_3463 = relay.Function([var_3461,var_3462,], output)
mutated_mod['func_3463'] = func_3463
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1259_call = mod.get_global_var('func_1259')
func_1260_call = mutated_mod.get_global_var('func_1260')
call_3470 = relay.TupleGetItem(func_1259_call(), 0)
call_3471 = relay.TupleGetItem(func_1260_call(), 0)
output = call_3470
output2 = call_3471
func_3474 = relay.Function([], output)
mod['func_3474'] = func_3474
mod = relay.transform.InferType()(mod)
output = func_3474()
func_3475 = relay.Function([], output)
mutated_mod['func_3475'] = func_3475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2724_call = mod.get_global_var('func_2724')
func_2725_call = mutated_mod.get_global_var('func_2725')
call_3499 = func_2724_call()
call_3500 = func_2724_call()
func_1083_call = mod.get_global_var('func_1083')
func_1085_call = mutated_mod.get_global_var('func_1085')
call_3506 = relay.TupleGetItem(func_1083_call(), 7)
call_3507 = relay.TupleGetItem(func_1085_call(), 7)
func_244_call = mod.get_global_var('func_244')
func_246_call = mutated_mod.get_global_var('func_246')
const_3529 = relay.const([-10,-7,-10,2,-1,-4,-2,9,8,-10,1,-10,3,3,10,3,5,-9,-3,2,2,2,-2,3,3,8,9,2,-1,5,8,-1,9,9,-3,-5,-8,8,-10,-2,8,-8,8,-6,-6,2,10,9,7,1,-1,-6,5,-7,-9,-5,-8,4,4,7,-1,-4,-6,10,10,-3,10,-10,-5,8,-7,-1,-8,3,4,-2,10,-6,8,8,-1,-1,-2,8,9,1,10,2,-6,-2,4,-5,-1,-9,-9,10,-9,3,-3,1,6,7,4,8,4,-8,5,3,4,-6,10,-5,9,2,-10,4,-5,-3,-2,-8,-10,-7,10,2,3,-9,6,-3,5,-6,10,-8,-1,-3,2,9,8,9,-5,3,1,-10,9,3,-1,-6,9,4,-7,-2,10,2,-9,-7,-4,-4,-4,5,8,-5,6,-9,-7,4,-2,2,-2,-10,-7,-7,7,7,6,5,9,4,-5,-10,-8,6,-5,-1,-5,9,-8,-5,8,8,-4,-9,-5,8,-7,-2,-7,4,7,10,-4,7,5,-7,-4,8,-8,-2,-1,-4,-1,3,5,1,-3,-7,9,-1,6,9,2,9,-6,6,-1,6,-7,3,8,-5,4,10,-3,-10,-8,8,-6,-2,8,-10,8,-3,6,-6,-10,9,-10,1,-9,-4,-10,9,-9,-6,10,-6,-1,3,4,6,-2,-10,-4,-8,2,2], dtype = "int8")#candidate|3529|(264,)|const|int8
call_3528 = relay.TupleGetItem(func_244_call(relay.reshape(const_3529.astype('int8'), [4, 6, 11])), 0)
call_3530 = relay.TupleGetItem(func_246_call(relay.reshape(const_3529.astype('int8'), [4, 6, 11])), 0)
uop_3538 = relay.sinh(call_3528.astype('float64')) # shape=(4, 6, 11)
uop_3540 = relay.sinh(call_3530.astype('float64')) # shape=(4, 6, 11)
bop_3543 = relay.left_shift(uop_3538.astype('int8'), relay.reshape(const_3529.astype('int8'), relay.shape_of(uop_3538))) # shape=(4, 6, 11)
bop_3546 = relay.left_shift(uop_3540.astype('int8'), relay.reshape(const_3529.astype('int8'), relay.shape_of(uop_3540))) # shape=(4, 6, 11)
output = relay.Tuple([call_3499,call_3506,bop_3543,])
output2 = relay.Tuple([call_3500,call_3507,bop_3546,])
func_3548 = relay.Function([], output)
mod['func_3548'] = func_3548
mod = relay.transform.InferType()(mod)
mutated_mod['func_3548'] = func_3548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3548_call = mutated_mod.get_global_var('func_3548')
call_3549 = func_3548_call()
output = call_3549
func_3550 = relay.Function([], output)
mutated_mod['func_3550'] = func_3550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2523_call = mod.get_global_var('func_2523')
func_2525_call = mutated_mod.get_global_var('func_2525')
call_3562 = relay.TupleGetItem(func_2523_call(), 0)
call_3563 = relay.TupleGetItem(func_2525_call(), 0)
output = relay.Tuple([call_3562,])
output2 = relay.Tuple([call_3563,])
func_3565 = relay.Function([], output)
mod['func_3565'] = func_3565
mod = relay.transform.InferType()(mod)
mutated_mod['func_3565'] = func_3565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3565_call = mutated_mod.get_global_var('func_3565')
call_3566 = func_3565_call()
output = call_3566
func_3567 = relay.Function([], output)
mutated_mod['func_3567'] = func_3567
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3577 = relay.var("var_3577", dtype = "int64", shape = (13, 15, 16))#candidate|3577|(13, 15, 16)|var|int64
const_3578 = relay.const([[[6,5,1,5,-2,-7,8,1,-2,-8,-3,3,-1,1,-2,3],[-8,-7,4,7,6,4,-8,1,3,9,8,-1,9,-2,6,8],[-4,5,8,6,7,-8,-5,5,10,-6,-7,9,9,-6,9,-1],[8,2,9,8,8,-1,4,-4,1,5,5,6,7,10,-6,8],[-8,-10,8,3,3,-10,-7,3,4,-7,-4,-4,-5,-7,-9,4],[7,2,-1,3,8,-3,10,4,6,5,-2,-10,-7,-7,2,-2],[5,-4,1,-10,-3,-4,1,-6,-7,6,2,-8,3,-5,-7,5],[3,6,-7,10,1,2,2,-10,9,-10,-2,-9,-4,-1,3,2],[-7,7,7,3,-3,-2,3,4,6,4,-2,6,-9,-8,-4,6],[9,5,-5,5,-5,3,-7,-1,-2,-4,10,-2,-6,3,1,1],[-5,5,7,7,7,2,-10,-8,10,9,-1,-2,3,6,5,3],[6,-1,10,-6,10,2,3,-2,-3,6,2,-10,1,9,7,-5],[10,7,4,6,1,5,7,10,8,3,-2,-7,2,9,5,-2],[2,4,3,1,9,2,3,5,6,1,2,-2,-3,-6,7,-5],[7,6,-1,-6,2,6,7,-7,1,2,-8,-2,7,1,-5,-4]],[[6,-2,6,-9,7,-4,-1,9,2,9,-10,-3,6,3,-10,4],[7,-7,8,-1,-3,9,-7,8,-2,1,8,8,-8,5,-8,-6],[-7,-5,-8,9,-3,-7,-9,-2,-4,4,9,-5,-3,-4,1,5],[2,-4,8,2,-4,-2,6,3,-8,-9,8,-3,6,1,9,9],[6,10,9,-5,-2,5,4,-5,4,9,-10,3,2,-7,-8,2],[2,-9,-5,5,3,5,-5,-10,-6,10,-3,-4,-7,-8,9,-10],[-2,-3,5,-4,5,6,8,10,-6,10,5,6,6,6,4,6],[7,2,-5,-10,6,2,-5,9,-5,3,-4,-10,5,-6,2,-6],[9,-10,-6,7,-8,7,-3,5,7,8,8,-2,3,-1,-9,-5],[7,-5,6,7,2,1,10,3,-3,1,-8,4,10,-6,2,-9],[7,-4,-9,10,4,-7,7,-4,-9,-4,7,-8,-3,7,-8,-6],[2,1,-10,-3,2,9,-7,4,5,5,-5,-10,-9,-8,3,3],[4,7,5,-8,-7,8,7,4,-9,-7,-1,-5,-4,-7,-6,2],[-4,-4,8,-6,9,1,-8,-10,-1,1,4,2,6,-4,-2,2],[5,5,-10,-8,-8,4,3,3,3,-8,10,4,3,-8,-4,1]],[[8,5,-10,6,-4,-4,-4,-3,-10,5,-4,6,7,-4,-8,-2],[-4,6,-10,2,1,-10,-2,6,-7,10,10,-3,-1,7,2,6],[6,10,4,-9,7,-2,4,10,8,7,7,-4,6,10,3,-6],[7,3,7,8,1,2,9,1,4,-5,7,-1,-3,1,-8,2],[-2,-9,-7,2,7,7,5,-3,-5,2,-10,-5,6,6,4,9],[5,4,5,1,-9,7,-6,3,-1,-3,9,-1,-5,-7,6,-2],[6,-4,1,2,-6,4,-1,3,-3,2,-4,5,3,6,-9,-2],[-6,5,-4,7,-8,-3,-7,3,-3,-10,-2,-8,-8,-4,-5,-2],[-5,-8,6,2,-6,4,-3,1,-6,5,-7,-2,-7,4,7,3],[-4,2,8,-3,8,8,-6,7,10,-9,5,4,2,-4,-3,-10],[1,7,5,-4,7,4,10,5,-3,9,-8,10,10,-6,10,-1],[7,10,10,-4,-7,2,10,-7,4,1,-10,1,-4,6,4,-6],[-7,-2,2,6,4,7,5,-7,2,2,-10,2,1,-1,-7,-7],[-3,1,-3,-5,3,1,5,-1,-7,-9,-8,-4,-10,6,-9,-2],[-2,-10,-8,-3,8,-2,-3,2,-8,8,3,-6,6,10,5,-2]],[[5,-1,8,7,-8,-10,4,3,-4,-7,-5,-2,5,8,6,-6],[-9,-5,2,4,-10,3,10,-7,6,-1,-9,2,7,-5,-8,-3],[1,-8,7,-3,8,-5,3,-1,8,-10,9,10,-3,-6,-9,10],[6,-10,-9,1,2,-4,-8,4,10,-2,7,4,8,-1,-8,4],[8,-8,1,-4,5,-8,6,-10,5,5,1,-9,1,5,-10,5],[5,5,-3,8,9,-3,-7,1,-3,1,-8,-5,10,-10,9,8],[-7,9,-2,-7,5,5,-3,4,-5,-9,5,3,6,-8,9,10],[-1,-7,7,3,6,-4,6,-4,-2,5,-9,-7,-4,-1,-10,-2],[-9,3,4,10,6,8,3,-5,5,4,-10,10,-5,8,9,8],[10,-7,-7,-6,-2,-7,8,-10,1,8,5,7,8,-7,9,6],[5,6,10,-9,8,-7,-7,9,1,1,-7,7,-8,-2,-8,-6],[2,6,-4,4,10,-8,8,-5,7,6,8,9,8,1,-2,8],[9,-7,9,-4,-3,-4,-2,-4,8,-2,3,-10,-5,-6,10,-2],[-8,-1,-10,-3,-7,-8,9,7,1,-2,5,5,5,-6,7,-3],[6,-1,-10,3,-5,-6,10,2,5,6,-7,9,-4,6,-4,6]],[[4,-10,4,-2,4,-3,-3,6,10,7,4,-9,2,2,6,-10],[7,-3,-5,2,-2,4,2,3,-1,-7,-8,-3,-2,10,3,8],[-4,-3,-7,6,9,-7,9,1,2,-7,6,5,-5,6,9,-9],[7,9,4,3,7,-2,-2,10,-3,-6,-5,7,-8,-9,8,-9],[10,9,5,-7,4,3,-4,-9,8,-6,-8,6,-9,-4,-4,4],[-1,10,-6,2,-8,-7,-8,1,-4,2,3,8,4,9,-5,6],[7,-3,4,-5,10,7,8,7,-9,4,6,4,-3,2,7,5],[-1,-8,-4,9,3,-4,-6,-3,-10,8,8,-10,8,-1,7,10],[-2,4,1,2,1,-5,6,3,4,6,7,2,-7,10,-9,-3],[-1,7,-2,6,-4,2,10,10,9,7,-1,9,4,-1,4,-3],[2,-4,8,10,2,6,7,7,1,10,-3,-9,2,7,3,-8],[-10,3,-4,-4,5,10,3,8,1,5,10,-10,-1,6,-9,-2],[1,-8,8,-3,1,5,-1,7,2,6,5,4,-5,1,7,2],[9,-2,4,-10,-9,1,7,-9,-2,-2,-3,3,7,1,-7,9],[-4,3,-6,-5,7,2,3,-4,8,-2,-2,-8,-8,10,-1,3]],[[2,5,10,-1,-5,-2,6,-5,-2,7,1,3,-6,7,4,3],[8,1,10,-7,-7,-7,-5,-1,-1,-2,-6,4,-10,9,2,9],[4,10,-6,-10,5,7,-10,-8,-9,-3,-7,-8,9,2,-3,-1],[-5,-10,-9,-3,8,6,-10,-10,7,7,2,3,-5,1,8,-5],[-7,3,7,-10,-9,4,-1,10,10,1,3,1,1,-5,6,-1],[7,8,-1,9,-7,9,7,-5,9,9,4,-9,2,1,6,-2],[7,6,-10,-5,-10,-4,-6,-6,-9,-4,-4,5,10,5,-9,10],[-7,-1,3,-2,2,2,7,10,2,6,-10,-4,-6,-8,-6,-10],[-7,7,-8,-5,-5,8,-6,5,-6,-5,-1,-7,-10,5,-3,6],[-7,-2,-2,-9,5,-10,-8,10,-7,10,-8,6,-4,-1,-7,9],[-9,-2,7,9,-9,-4,3,10,-2,7,-1,-5,5,2,-2,7],[9,4,9,1,-4,4,8,7,-8,10,-9,-4,3,-6,4,-8],[-1,2,-10,9,-5,-9,-10,-7,-1,8,1,6,-6,1,-6,-7],[-5,-8,-10,-7,1,-2,-4,-9,-5,7,-9,-2,-5,-6,-5,-9],[-2,5,5,10,8,7,10,-9,3,3,-6,8,1,2,9,-6]],[[8,2,3,-9,4,5,2,-3,9,-8,2,-8,-1,10,-2,8],[8,-3,-4,2,-8,5,10,-6,3,-3,1,-9,2,2,-6,3],[-4,2,9,-7,-2,9,-2,2,3,2,9,-8,-1,-4,-3,-8],[3,5,8,3,6,-4,10,-4,3,7,-7,2,5,2,5,5],[2,4,-3,9,-8,10,1,1,9,-6,2,4,-4,-5,8,8],[1,-9,-8,6,1,4,-1,6,2,8,-7,-1,-1,-3,6,7],[3,2,4,7,-3,9,-5,-7,4,9,8,-6,6,-7,1,10],[10,5,-7,3,-3,-7,7,5,9,-7,-6,7,-2,-4,8,9],[3,4,-8,3,9,-2,-4,-10,-3,-2,-1,10,-1,10,-8,7],[-5,-3,-10,-4,8,7,-3,5,-5,-2,5,-2,6,-6,-1,6],[-6,8,-7,4,8,-7,10,4,10,4,10,4,7,10,2,5],[5,5,4,7,-3,-1,-8,-8,5,-6,7,-10,-9,-4,6,-1],[3,-3,5,8,-6,-1,-8,-3,-9,5,-8,-2,-5,7,8,-4],[-4,-7,-9,-9,6,9,8,-4,-10,5,-5,-4,5,-4,9,-1],[7,6,-3,-10,4,10,1,9,4,-1,10,1,-7,6,5,3]],[[-7,9,-5,-10,8,10,-5,-1,2,-10,-7,10,8,-2,-5,-6],[-3,4,-3,6,6,3,7,-10,5,-3,-1,-6,1,3,-2,-10],[-3,4,1,-9,6,-8,-5,-1,-8,-5,-9,7,1,-6,8,-2],[2,-9,4,2,2,-2,-8,-9,9,-5,-5,8,4,-10,10,5],[8,7,-4,3,-6,-2,9,-1,3,9,-10,-7,9,-9,9,-10],[-10,10,-5,9,-7,-8,-2,5,6,-7,-8,-3,2,-7,7,-10],[6,10,-1,5,-2,4,-3,-3,-2,-3,5,-1,-7,-9,-8,1],[9,5,2,7,4,-2,-2,-4,-5,9,5,6,8,6,2,-10],[-9,-2,7,-9,-3,-10,3,-9,2,-8,-8,1,-8,10,4,-3],[-4,-8,-4,-4,5,2,-7,-8,-9,-8,-1,-2,5,2,-1,6],[2,10,10,-5,-7,7,-9,7,-3,6,-3,4,-10,9,3,-1],[-1,3,5,8,-6,-10,-2,-3,-9,9,-7,9,-1,-9,8,-1],[10,-10,-3,-7,-7,-4,-3,2,-5,-3,7,-10,-4,3,8,9],[-10,-3,1,-10,8,-7,-10,-2,-1,-9,-6,-7,9,-2,-5,-7],[4,-6,1,-5,-1,-7,-1,-7,-3,-3,7,-1,9,5,6,9]],[[-1,5,2,-10,-2,3,7,8,-8,1,10,-4,-5,4,-1,3],[9,-4,8,3,1,5,-10,10,-1,-5,-2,9,8,-1,6,8],[2,6,6,-1,-7,-6,9,-5,6,-3,-9,-6,-8,5,-2,9],[5,-5,-7,1,-5,1,3,-6,7,7,-4,4,-3,5,-2,-9],[-4,-9,3,4,-6,-3,4,10,-9,-9,4,-6,-2,10,7,-2],[-4,-1,2,-4,-2,-1,-6,-8,-10,1,-2,-10,-8,-10,-10,6],[-7,10,2,-10,-2,-3,-2,7,-9,7,-3,-6,5,-6,2,8],[6,-9,-3,5,9,-6,-8,-2,-9,-8,4,-3,-2,6,10,-3],[4,-7,8,4,1,-8,-1,7,1,-4,9,-6,6,-5,7,-3],[8,10,5,5,2,-4,-8,-4,-6,4,6,8,-5,10,-1,-3],[-4,-6,6,4,9,-2,-1,-5,-5,-4,-10,-4,-3,7,7,2],[-4,2,-4,-8,6,-1,6,-4,3,-1,8,10,-10,-7,6,2],[-10,1,-1,-8,-9,-4,4,-6,-5,2,4,7,8,1,-3,-5],[7,10,7,7,-8,-2,8,-9,-7,-8,-2,3,9,3,8,9],[-6,-5,7,-8,10,7,-8,-3,-9,3,8,-1,-3,10,-4,9]],[[8,-10,4,1,-8,6,-7,10,-1,-7,-3,5,3,-7,6,7],[-10,10,7,-9,-2,-10,5,-6,4,-3,-2,-3,6,3,8,8],[9,1,1,-2,9,3,3,-8,3,-6,-4,1,10,3,-4,-7],[9,10,2,-5,3,2,-9,2,6,8,-6,-1,1,-8,5,9],[-3,-3,8,-5,8,-4,10,9,-6,5,4,-10,-7,3,4,-7],[-8,4,-8,8,6,3,9,-1,8,7,-9,-8,-7,-2,2,2],[8,7,-4,-4,-8,6,10,2,-3,-10,6,-3,-9,-6,2,3],[3,-8,5,-7,2,10,-1,9,-1,-8,-7,2,4,8,-5,6],[3,6,9,-10,-7,2,-5,3,8,-3,-10,4,4,-8,5,8],[9,5,-7,8,7,3,-8,8,-6,4,7,-10,2,-9,-3,4],[-10,9,-5,-3,-4,8,3,-2,6,-4,4,3,1,4,8,-5],[8,-8,-8,9,7,8,3,8,-5,-4,8,8,9,5,-1,-10],[2,-6,-10,6,2,9,5,-7,-10,3,10,9,-3,-9,-3,-5],[-8,9,8,7,-3,-7,4,1,5,-3,-5,-4,-7,5,3,-6],[3,-3,3,10,8,4,-1,7,-9,3,-5,2,-4,-3,-1,10]],[[-6,-4,2,-7,-3,-2,6,-2,-2,-8,-4,10,-9,4,1,3],[-6,-8,-3,1,-4,10,-2,4,9,-4,4,2,-6,3,-2,-7],[-5,9,8,6,2,-3,-10,10,-8,-2,-10,-8,-1,-6,-9,-1],[5,-4,9,4,-6,8,3,5,4,-6,4,-1,-6,7,-7,2],[2,5,-6,3,-6,-9,-8,-2,4,7,1,2,-4,-5,-1,4],[-2,5,8,1,-10,10,-7,-2,-10,6,8,1,8,4,-2,3],[5,-4,-5,-4,-7,2,-9,-2,3,2,-9,3,8,9,6,-4],[9,4,2,10,4,-3,8,4,5,-3,1,-2,-5,-9,-2,-2],[10,8,3,9,-9,4,8,-9,4,-9,-9,-3,3,-5,-4,7],[-2,4,-2,5,-7,-9,7,-10,-1,5,2,-6,10,2,-8,-8],[6,6,-6,9,9,10,5,6,-1,-6,1,-9,-3,4,2,2],[3,5,-10,-3,-2,7,-5,3,-6,-10,-9,7,-10,5,-1,9],[4,3,8,-5,9,8,-8,1,-8,-2,-9,-2,10,-2,-2,-6],[7,-4,-5,5,-2,-9,4,4,-2,2,5,-2,-9,5,9,10],[1,1,3,-4,-9,-5,5,-4,8,-8,-9,-8,-9,10,6,-2]],[[-5,7,-8,-5,3,9,-1,-5,-10,2,7,8,4,-2,9,7],[8,2,-4,3,8,5,7,-8,5,6,9,8,3,4,-5,-8],[5,-10,-8,6,7,5,3,10,-3,-2,2,6,9,9,-10,-8],[6,8,3,10,-7,-3,-6,2,1,4,3,9,9,-9,-5,-8],[7,5,-9,-7,9,1,-2,5,-7,7,8,-4,-5,7,-10,-9],[10,4,-8,-10,-2,2,-1,9,7,-8,3,-3,-6,6,-7,2],[10,9,-8,7,-7,6,-8,-8,1,10,-9,-10,-3,-1,-3,8],[-9,-1,5,9,-7,-1,-9,7,-4,-2,10,-10,-10,3,-3,5],[9,1,4,-7,-6,-5,7,5,-1,-8,2,-5,-6,4,-9,-3],[6,2,7,-10,-8,-10,-9,10,-5,-10,-4,-7,-5,-2,-1,3],[-9,7,6,9,-2,-1,-5,10,9,4,7,6,4,6,-2,-3],[6,7,7,6,-6,-2,-9,-8,2,-4,5,1,-5,-5,6,8],[-7,-1,-4,6,5,-10,8,-5,-1,-9,8,-8,-7,-1,-2,-2],[-5,-5,-4,-8,7,-5,5,-7,-10,5,-6,-10,7,-5,-2,7],[-2,8,-3,4,4,7,1,8,-2,-7,5,1,-3,-10,-3,-2]],[[-1,-10,-7,-4,-4,-10,7,-6,10,-7,-3,8,7,10,-7,7],[-3,2,-1,-10,-9,2,10,-5,1,7,10,-1,3,9,6,-10],[4,8,10,2,10,-5,2,-1,2,1,3,-1,5,-8,7,-9],[-10,6,-7,-9,-2,9,6,9,10,-2,-3,-9,4,-7,-5,-1],[3,5,4,1,8,-2,-2,2,2,-4,8,1,-3,2,5,5],[1,-2,-1,2,4,4,6,7,2,3,7,2,4,-9,9,9],[-1,-6,-3,-4,4,-3,5,-10,-5,7,-9,-3,-4,2,-8,5],[1,4,8,2,-7,4,-7,9,9,4,-6,1,-3,5,-3,1],[-2,1,-4,-3,8,-2,-4,-8,8,1,3,8,-2,-5,5,-2],[-2,6,5,-8,-9,-9,3,3,1,7,-5,-10,-8,-3,-3,-10],[7,-3,-5,5,-1,-6,4,-6,-3,-1,-8,5,-7,10,5,-7],[6,-7,10,5,-8,8,10,9,8,4,-2,-3,1,-9,1,-1],[3,-10,-9,6,7,9,7,3,-9,-1,-7,-8,-8,-5,2,-8],[3,9,4,-7,-1,-8,-6,4,-7,-4,9,-3,10,8,3,6],[3,-7,-3,5,5,-2,6,4,-1,10,-4,-9,-2,-6,-2,-2]]], dtype = "int64")#candidate|3578|(13, 15, 16)|const|int64
bop_3579 = relay.bitwise_xor(var_3577.astype('int64'), relay.reshape(const_3578.astype('int64'), relay.shape_of(var_3577))) # shape=(13, 15, 16)
bop_3585 = relay.power(const_3578.astype('float64'), relay.reshape(bop_3579.astype('float64'), relay.shape_of(const_3578))) # shape=(13, 15, 16)
func_2600_call = mod.get_global_var('func_2600')
func_2602_call = mutated_mod.get_global_var('func_2602')
const_3592 = relay.const([True,False,True,True,False,True,True,True,True,True,True,True,False,False,False,True,False,False,False,True,True,True,True,False,False,False,True,True,False,True,True,True,True,True,False,True,False,False,False,True,True,True,False,False,True,False,True,True,False,True,False,True,False,False,True,True,False,False,False,False,False,False,False,True,True,False,True,True,False,True,False,False,True,False,False,False,False,True,False,False,False,False,True,True,False,False,False,True,False,False,True,False,False,True,False,True,False,True,False,False,False,False,False,True,False,False,False,False,True,False,False,False,False,True,True,True,True,True,False,False,True,True,False,False,True,False,True,True,True,False,True,False,False,False,True,True,False,True,True,False,True,False,False,False,True,True,True,True,False,True,True,True,False,True,True,True,False,True,False,True,True,False,True,True,False,True,False,False,False,False,False,False,False,False,False,True,True,True,False,True,False,True,True,False,True,False,False,True,True,False,False,False,False,False,False,False,True,False,True,True,False,True,True,False,False,True,False,True,False,False,True,False,False,False,True,True,False,True,False,False,True,False,False,False,False,False,False,True,True,True,True,True,True,False,False,True,False,False,False,False,False,True,True,False,True,False,True,False,True,True,False,False,False,False,False,False,True,True,False,False,False,True,True,True,True,True,False,True,True,True,False,False,False,True,False,False,True,False,False,False,True,False,False,True,False,True,False,True,False,False,True,False,True,True,False,False,False,False,False,False,True,False,False,False,True,False,False,False,False,False,False,False,False,False,True,False,True,True,False,True,True,True,False,False,False,False,True,True,False,True,True,False,True,True,False,False,True,False,False,False,False,False,False,False,False,True,False,False,True,False,True,False,False,True,True,False,True,False,True,False,True,False,False,False,True,False,False,True,False,False,True,False,False,True,False,False,False,False,False,True,True,False,False,True,True,True,True,True,True,True,True,False,True,True,False,True,True,False,False,True,False,True,True,False,False,True,False,False,True,True,False,False,True,False,True,False,True,True,True,False,False,False,False,True,True,False,False,False,False,False,True,False,True,False,False,True,True,False,False,True,True,False,True,False,False,True,True,True,False,False,True,False,True,True,True,False,True,False,True,True,False,False,True,False,True,True,True,False,True,True,True,True,True,True,True,True,False,False,False,False,True,True,False,False,False,True,False,True,True,True,False,False,False,True,False,True,False,True,True,False,True,True,True,False,False,False,False,False,True,False,False,False,False,False,False,False,True,False,False,True,False,False,True,False,False,True,True,False,False,False,False,True,True,True,False,True,False,False,True,True,False,True,True,False,True,True,True,True,True,True,False,True,True,True,True,True,False,False,False,False,True,False,False,False,False,False,False,False,False,True,True,False,True,False,True,False,True,False,True,False,True,True,False,False,False,True,False,False,False,False,True,True,False,True,True,False,True,True,False,True,True,True,True,False,True,False,False,False,False,False,True,True,True,True,False,False,False,False,False,False,False,True,True,False,False,True,True,True,False,True,False,True,True,False,True,False,False,False,True,True,False,False,False,True,True,False,True,True,False,False,False,False,True,True,True,False,False,False,True,True,True,False,False,False,False,False,True,False,False,False,True,False,False,False,True,True,False,True,False,True,True,False,True,False,False,False,False,False,False,False,True,False,False,False,False,False,False,True,False,False,True,False,False,True,False,True,False,False,False,True,True,True,True,True,False,True,True,False,False,False,False,True,False,False,True,False,False,True,False,True,True,True,True,True,True,True,True,True,True,True,False,True,True,False,False,True,True,True,True,True,True,False,True,True,False,False,False,True,False,False,False,True,True,True,True,False,False,False,False,True,True,False,False,False,False,False,True,False,False,True,True,True,True,False,True,True,True,True,False,True,True,False,False,False,True,True,True,True,True,True,True,True,True,True,True,False,False,True,False,False,False,True,True,True,False,False,False,True,True,True,False,False,True,False,True,True,False,False,False,True,True,True,False,False,True,False,False,True,True,False,True,True,False,False,False,False,True,False,True,False,True,True,True,True,True,False,False,True,False,False,True,True,False,True,True,True,True,False,False,False,False,True,True,False,True,True,False,False,False,True,True,True,False,False,False,False,False,False,True,False,True,False,True,True,False,False,False,True,False,False,False,True,True,True,True,False,True,False,True,True,True,False,False,False,False,True,False,False,True,True,False,False,False,True,True,False,True,True,True,False,True,True,True,False,True,False,True,False,False,False,True,False,False,True,False,False,False,False,False,False,True,False,False,True,True,False,True,False,True,True,False,True,False,True,True,True,False,False,True,False,False,False,False,False,False,False,False,False,False,False], dtype = "bool")#candidate|3592|(980,)|const|bool
call_3591 = relay.TupleGetItem(func_2600_call(relay.reshape(const_3592.astype('bool'), [14, 14, 5])), 0)
call_3593 = relay.TupleGetItem(func_2602_call(relay.reshape(const_3592.astype('bool'), [14, 14, 5])), 0)
func_893_call = mod.get_global_var('func_893')
func_897_call = mutated_mod.get_global_var('func_897')
var_3595 = relay.var("var_3595", dtype = "float32", shape = (1, 297))#candidate|3595|(1, 297)|var|float32
var_3596 = relay.var("var_3596", dtype = "int8", shape = (1, 264))#candidate|3596|(1, 264)|var|int8
call_3594 = relay.TupleGetItem(func_893_call(relay.reshape(var_3595.astype('float32'), [3, 11, 9]), relay.reshape(var_3596.astype('int8'), [264,]), ), 0)
call_3597 = relay.TupleGetItem(func_897_call(relay.reshape(var_3595.astype('float32'), [3, 11, 9]), relay.reshape(var_3596.astype('int8'), [264,]), ), 0)
var_3603 = relay.var("var_3603", dtype = "bool", shape = (14, 14, 5))#candidate|3603|(14, 14, 5)|var|bool
bop_3604 = relay.bitwise_and(call_3591.astype('int64'), relay.reshape(var_3603.astype('int64'), relay.shape_of(call_3591))) # shape=(14, 14, 5)
bop_3607 = relay.bitwise_and(call_3593.astype('int64'), relay.reshape(var_3603.astype('int64'), relay.shape_of(call_3593))) # shape=(14, 14, 5)
uop_3611 = relay.atan(var_3577.astype('float64')) # shape=(13, 15, 16)
func_423_call = mod.get_global_var('func_423')
func_428_call = mutated_mod.get_global_var('func_428')
var_3614 = relay.var("var_3614", dtype = "int32", shape = ())#candidate|3614|()|var|int32
const_3615 = relay.const([4,5,-1,-4,-7,-8,-1,-2,-8,7,5,8,2,10,4,7,9,4,8,-7,-6,6,2,2,-10,5,9,-5,7,10,-5,1,-8,4,-2,-10,5,-8,6,1,9,3,-9,-8,6,-10,-4,6,8,7,-10,8,5,-6,-4,-8,3,2,2,2,7,-10,5,-4,-8,10,-9,5,4,6,-10,-4,6,7,-3,7,-1,2,6,10,10,2,-10,-5,10,-4,-8,3,4,3,1,9,10,9,-9,8,8,-9,8,-5,-7,-9,9,8,-4,-9,4,8,-1,-10,5,-10,-7,-3,4,3,9,8,-4,9,9,4,8,-7,-6,-7,-4,-5,-7,8,-8,-5,-3,-3,9,-6,2,2,-9,-6,6,9,4,3,-4,-3,3,9,10,4,6,8,9,7,-10,4,-10,-10,-9,-6,-5,7,-6,4,10,3,-8,-5,2,-7,-9,-2,6,-3,-4,-7,-7,-7,-3,-7,10,3,5,-5,2,-1,2,1,-3,2,3,-8,-6,-1,9,1,2,-7,2,3,-3,6,-8,-5,1,-10,-7,-3,7,-1,4,6,-8,10,-5,5,-7,-5,-9,-8,6,-5,10,7,3,-4,9,-10,10,-8,-5,5,5,-9,-8,7,6,-10,-1,4,4,1,-5,-2,-3,2,-3,-3,6,-7,8,-10,-7,3,-7,1,4,-5,-5,3,-7,-9,1,3,2,4,3,8,-6,7,7,-5,2,-9,-6,8,-9,-6,-6,10,6,-2,7,8,-1,5,4,1,9,-6,4,8,10,-6,2,6,7,8,10,-7,4,-10,-1,6,-3,-7,-6,-2,1,-3,-3,3,-9,-4,-1,-9,-5,3,2,-8,-4,1,9,6,-1,-5,10,-4,10,-5,1,4,-4,1,-8,10,1,-2,7,10,-1,-2,-2,-9,6,-5,-9,-2,8,7,-2,8,10,-6,9,5,-1,-10,-3,9,-2,-8,-3,-4,-6,7,-9,3,-4,-6,-5,3,-6,-2,10,10,-4,-5,-9,-10,-3,2,1,-3,4,-7,8,4,-3,-5,-8,4,-3,10,1,8,-6,-8,-8,3,-10,-9,-2,-4,-1,-7,6,-10,-2,5,-10,-9,-5,-5,-8,3,1,-6,-6,8,-1,-4,-6,-10,-5,-6,-7,-3,-2,3,7,5,9,2,4,-3,-7,-4,3,5,-10,-5,4,9,-4,-3,10,2,-1,-5,6,-10,6,8,-1,-9,2,7,-10,1,1,-9,-3,-10,-5,9,-4,-4,6,-4,-5,-7,-7,-2,-1,2,-6,-2,-2,-5,-9,6,-5,6,4,-6,2,-5,-8,-5,1,-10,10,8,-4,9,-5,-7,-7,2,2,2,3,-1,6,9,-7,4,3,-1,5,10,-7,2,9,-7,4,-3,7,-8,-3,-2,-8,-10,-10,-7,1,7,-4,3,-5,-4,-10,-5,-4,1,2,8,10,2,-8,-7,8,-8,2,-8,2,5,-3,-10,-5,-2,6,8,9,8,-9,-8,-8,9,-10,9,3,3,-6,10,-7,8,-4,1,-6,-3,-5,-2,-9,-3,10,-10,-7,6,7,-5,-10,-8,-1,8,-10,-10,1,-6,-5,-9,2,-7,-4,2,-10,-8,4,-5,-6,2,-3,1,-6,-6,9,-3,7,-9,4,-6,10,3,1,9,-2,-5,5,10,-4,-10,4,-3,-5,3,6,2,-3,-2], dtype = "int32")#candidate|3615|(630,)|const|int32
call_3613 = relay.TupleGetItem(func_423_call(relay.reshape(var_3614.astype('int32'), []), relay.reshape(const_3615.astype('int32'), [7, 9, 10]), relay.reshape(var_3596.astype('int8'), [264,]), ), 3)
call_3616 = relay.TupleGetItem(func_428_call(relay.reshape(var_3614.astype('int32'), []), relay.reshape(const_3615.astype('int32'), [7, 9, 10]), relay.reshape(var_3596.astype('int8'), [264,]), ), 3)
uop_3623 = relay.log10(bop_3604.astype('float32')) # shape=(14, 14, 5)
uop_3625 = relay.log10(bop_3607.astype('float32')) # shape=(14, 14, 5)
func_1361_call = mod.get_global_var('func_1361')
func_1363_call = mutated_mod.get_global_var('func_1363')
call_3629 = relay.TupleGetItem(func_1361_call(), 0)
call_3630 = relay.TupleGetItem(func_1363_call(), 0)
bop_3631 = relay.logical_and(bop_3579.astype('bool'), relay.reshape(uop_3611.astype('bool'), relay.shape_of(bop_3579))) # shape=(13, 15, 16)
func_1286_call = mod.get_global_var('func_1286')
func_1289_call = mutated_mod.get_global_var('func_1289')
const_3638 = relay.const([6.933389,-4.924638,7.090934,0.345038,4.909273,-2.366190,7.618807,5.329415,6.401806,-9.285038,-8.960740,0.024989,1.974464,1.585793,-8.023248,-4.484368,0.500137,5.110854,8.498349,-7.249260,-9.634840,2.968210,9.012343,-5.269157,1.040732,0.914475,-2.661254,6.289770,-3.745763,-1.321791,-3.250820,-3.380577,-1.779357,-0.087122,-1.210223,-7.707104,2.457336,-3.670237,-2.633021,6.710501,2.250032,0.428105,-2.885932,1.818861,-6.287319,8.635896,2.084779,-7.999377,6.893751,2.717530,1.687566,2.807642,6.439183,-4.439124,-1.950915,-2.872746,-7.206821,7.898236,-4.301631,3.645216,6.589969,8.188646,6.063651,-6.579550,-1.128599,-9.895806,9.609314,6.220648,-8.054053,8.397684,4.048444,-2.123456,6.706759,-4.117910,1.834619,-7.627345,-6.216119,6.492562,2.638568,3.027138,9.758775,-2.192598,3.384698,-8.168226,4.236956,-1.791917,4.356489,-9.641946,9.569248,-8.354681,-8.715893,4.934536,2.649165,-5.465924,-9.318978,-4.332819,-6.705162,-7.739815,-0.613928,4.081887,-5.510912,0.487176,-3.024967,3.599824,-6.411335,-2.457092,-2.989427,-7.406277,-1.220768,8.308818,-7.625897,3.144057,-2.342282,-4.014406,-2.974382,-0.877911,1.690690,-0.328379,2.904906,7.153894,4.656795,-8.187160,6.545013,6.452064,-7.806014,-0.559718,5.823657,4.695773,-3.478538,-5.858291,1.155363,9.063487,-9.276805,-2.226533,1.427900,-4.525482,-4.588515,1.444141,0.070411,9.162986,9.781047,-9.305521,5.627995,-4.267612,3.333544,-5.294304,8.671613,6.401800,7.649410,2.201527,-3.564885,-9.806627,-5.427552,-5.943769,-4.454177,6.581135,-5.742727,-0.679243,6.789489,3.608996,-9.062242,3.280907,1.911936,8.020122,8.120754,-4.738141,-5.157628,-6.440008,-2.198161,-4.433374,-1.252113,-5.677231,8.673831,3.115334,6.437255,7.129984,-3.580278,1.626035,-1.092060,8.770021,2.430684,9.833006,-7.730971,-8.734449,-3.131143,7.209255,0.763330,0.449456,8.339914,3.758600,2.080884,-1.156033,-0.815174,-3.510961,-0.920166,-5.816252,2.802453,-9.636401,6.896471,-8.920981,2.210104,-7.529181,0.600469,-9.703439,-1.958706,9.481534,-1.362141,-1.335033,5.679932,6.161598,-0.969872,4.662030,1.058439,4.372253,-6.164714,5.521533,7.199207,-0.604240,6.698359,2.369661,1.309920,-1.990514,-9.880352,-3.785957,1.463653,-7.966863,5.482052,3.794728,5.543584,6.345742,-8.194109,5.788961,-8.050896,-7.884070,-1.193858,-8.043044,-8.909323,-3.303747,0.561419,-7.072548,-8.668629,-3.805341,-0.589995,1.847739,-8.772781,4.356715,0.615559,-5.933553,1.611857,9.364132,9.279081,1.388245,-6.778828,-0.261679,-7.787591,-5.763207,8.830869,-5.141696,-2.427005,1.513440,-2.910084,3.334238,-5.721791,4.229863,-9.383130,6.230256,-7.080828,8.609132,-8.995636,-3.630892,-2.994317,-2.408383,7.410376,8.444839,-8.797204,-7.701936,-6.378132,-2.781590,-3.911839,-7.169769,-9.099725,-7.190465,-5.031863,-6.629153,1.461790,8.089071,0.173344,-2.057516,-2.683016,8.958671,-7.712706,2.561211,0.504958,8.944266,5.922733,0.193713,-2.156001,3.961096,8.568750,1.537588,-4.255400,2.238529,-4.010685,9.974081,5.450084,3.788182,-4.927983,-4.490714,-9.833557,0.573184,0.052791,-9.411812,-3.129443,-0.874629,5.380157,3.881571,-6.376105,9.593141,-7.149134,0.812712,2.612882,6.486794,8.239353,-2.826787,-2.894732,-1.987373,-4.589704,4.015887,-4.194972,-9.667074,9.511613,3.897653,-8.169247,5.133268,3.369183,4.454147], dtype = "float64")#candidate|3638|(336,)|const|float64
call_3637 = func_1286_call(relay.reshape(const_3638.astype('float64'), [12, 7, 4]))
call_3639 = func_1286_call(relay.reshape(const_3638.astype('float64'), [12, 7, 4]))
func_1012_call = mod.get_global_var('func_1012')
func_1016_call = mutated_mod.get_global_var('func_1016')
var_3645 = relay.var("var_3645", dtype = "int8", shape = (143,))#candidate|3645|(143,)|var|int8
var_3646 = relay.var("var_3646", dtype = "int8", shape = (1573,))#candidate|3646|(1573,)|var|int8
call_3644 = relay.TupleGetItem(func_1012_call(relay.reshape(var_3645.astype('int8'), [143,]), relay.reshape(var_3646.astype('int8'), [1573,]), relay.reshape(var_3645.astype('int8'), [143,]), ), 4)
call_3647 = relay.TupleGetItem(func_1016_call(relay.reshape(var_3645.astype('int8'), [143,]), relay.reshape(var_3646.astype('int8'), [1573,]), relay.reshape(var_3645.astype('int8'), [143,]), ), 4)
func_1174_call = mod.get_global_var('func_1174')
func_1178_call = mutated_mod.get_global_var('func_1178')
const_3654 = relay.const([-5,1,8,1,7,7,3,-5,6,3,-5,10,5,10,5,3,-10,1,4,-8,-1,6,-4,8,-10,3,-2,-9,-4,9,6,9,-8,2,2,5,-6,7,4,8,-8,1,6,7,9,-9,-9,1,-1,-9,4,6,7,-9,-1,-4,10,1,5,5,-5,1,5,3,-4,8,-8,-7,2,-3,5,-1,3,2,-9,4,-3,10,-8,1,7,9,8,8,3,2,-1,4,5,3,-5,2,3,-4,-6,2,-8,9,-8,5,-10,-3,10,-4,5,10,4,8,3,6,-10,-3,9,4,10,-3,6,3,3,-10,-5,-8,10,4,-9,5,9,8,1,-9,3,5,-8,-5,4,-1,4,7,7,-1,2,-8,3,2,9,-9,5,-2,-10,4,-10,4,4,2,-3,-10,7,9,-3,8,-4,2,10,-2,9,-6,-9,-7,-4,-6,9,3,3,10,4,-6,6,10,2,-6,-8,-3,7,-1,6,7,3,-3,-5,-10,2,9,-6,4,1,-2,-6,-7,5,-3,5,-8,1,5,-6,-7,3,-8,7,8,4,8,-4,-3,10,8,6,-4,-9,5,3,6,7,4,6,1,-1,9,3,4,8,9,-10,-2,-1,6,10,10,6,1,-8,-1,3,-8,-2,10,-4,5,-1,5,-6,5,-3,-3,-1,-10,-9,1,2,10,2,5,8,-2,-7,-2,5,8,4,-6,8,-7,-8,-2,-8,4,2,-5,-9,1,3,-8,-3,-6,-2,4,-8,-8,9,-7,-2,-8,10,5,2,5,9,4,4,9,-2,-5,-3,-9,4,-3,6,-1,9,-8,-1,-4,8,2,-8,7,3,-2,-8,-3,6,-9,9,1,-3,7,-1,4,-1,-3,-9,-10,-4,-3,5,3,1,-6,-1,6,-3,9,6,-5,-2,-7,-9,-5,3,-5,3,-2,1,3,-4,-7,-4,2,2,8,-6,-6,3,-9,-1,-7,-4,7,8,7,-10,10,3,-5,-9,-8,7,-1,-5,-9,5,-1,6,4,9,-3,-8,-5,4,5,-3,2,6,2,-4,-10,-6,7,10,-3,3,-9,10,-1,6,-2,8,8,-7,-9,-1,9,-9,-9,-8,-7,-2,-1,2,9,-9,-8,-4,4,7,4,2,7,-10,2,3,-10,-8,9,4,-10,10,-1,-4,-8,8,-3,5,-2,8,-4,5,-6,-4,5,-5,-2,-4,-9,-8,3,9,6,4,3,-4,-5,-1,-2,-7,7,-5,-5,2,9,-3,7,8,7,3,-6,-7,4,1,6,-4,-8,-10,9,-8,-5,1,-2,5,-1,-9,5,-7,5,6,5,-2,10,9,7,8,-10,-4,-7], dtype = "uint16")#candidate|3654|(504,)|const|uint16
call_3653 = relay.TupleGetItem(func_1174_call(relay.reshape(const_3654.astype('uint16'), [4, 9, 14]), relay.reshape(const_3654.astype('uint16'), [4, 9, 14]), ), 2)
call_3655 = relay.TupleGetItem(func_1178_call(relay.reshape(const_3654.astype('uint16'), [4, 9, 14]), relay.reshape(const_3654.astype('uint16'), [4, 9, 14]), ), 2)
output = relay.Tuple([bop_3585,const_3592,call_3594,var_3595,var_3596,call_3613,var_3614,const_3615,uop_3623,call_3629,bop_3631,call_3637,const_3638,call_3644,var_3645,var_3646,call_3653,const_3654,])
output2 = relay.Tuple([bop_3585,const_3592,call_3597,var_3595,var_3596,call_3616,var_3614,const_3615,uop_3625,call_3630,bop_3631,call_3639,const_3638,call_3647,var_3645,var_3646,call_3655,const_3654,])
func_3660 = relay.Function([var_3577,var_3595,var_3596,var_3603,var_3614,var_3645,var_3646,], output)
mod['func_3660'] = func_3660
mod = relay.transform.InferType()(mod)
mutated_mod['func_3660'] = func_3660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3660_call = mutated_mod.get_global_var('func_3660')
var_3662 = relay.var("var_3662", dtype = "int64", shape = (13, 15, 16))#candidate|3662|(13, 15, 16)|var|int64
var_3663 = relay.var("var_3663", dtype = "float32", shape = (1, 297))#candidate|3663|(1, 297)|var|float32
var_3664 = relay.var("var_3664", dtype = "int8", shape = (1, 264))#candidate|3664|(1, 264)|var|int8
var_3665 = relay.var("var_3665", dtype = "bool", shape = (14, 14, 5))#candidate|3665|(14, 14, 5)|var|bool
var_3666 = relay.var("var_3666", dtype = "int32", shape = ())#candidate|3666|()|var|int32
var_3667 = relay.var("var_3667", dtype = "int8", shape = (143,))#candidate|3667|(143,)|var|int8
var_3668 = relay.var("var_3668", dtype = "int8", shape = (1573,))#candidate|3668|(1573,)|var|int8
call_3661 = func_3660_call(var_3662,var_3663,var_3664,var_3665,var_3666,var_3667,var_3668,)
output = call_3661
func_3669 = relay.Function([var_3662,var_3663,var_3664,var_3665,var_3666,var_3667,var_3668,], output)
mutated_mod['func_3669'] = func_3669
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3230_call = mod.get_global_var('func_3230')
func_3231_call = mutated_mod.get_global_var('func_3231')
call_3681 = relay.TupleGetItem(func_3230_call(), 0)
call_3682 = relay.TupleGetItem(func_3231_call(), 0)
output = relay.Tuple([call_3681,])
output2 = relay.Tuple([call_3682,])
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
const_3717 = relay.const([[[True,False,False,False],[False,True,False,True],[True,False,True,False],[False,False,True,True]],[[True,False,False,False],[True,True,False,True],[True,True,True,False],[False,False,False,False]],[[False,True,False,True],[False,False,False,True],[True,True,True,True],[True,True,False,False]],[[True,False,False,False],[False,True,True,True],[False,False,True,False],[False,False,False,True]],[[True,False,False,True],[True,False,False,False],[True,False,True,False],[True,True,True,False]],[[False,True,False,False],[False,True,True,False],[False,False,True,False],[False,True,True,True]],[[False,True,False,True],[True,True,True,False],[True,False,True,False],[True,False,False,True]],[[True,False,True,False],[True,False,False,True],[True,True,False,True],[True,True,True,True]],[[True,True,False,False],[False,True,True,True],[True,False,True,False],[False,True,False,True]],[[True,True,True,True],[False,False,False,True],[True,False,False,False],[False,True,True,True]],[[True,True,True,True],[False,False,True,True],[False,False,False,False],[False,False,False,True]],[[True,True,False,True],[True,True,False,True],[True,True,True,True],[False,True,False,True]],[[False,False,True,True],[False,False,False,True],[False,False,True,False],[False,True,False,False]],[[True,False,True,False],[True,False,True,True],[True,True,False,True],[False,True,True,False]],[[True,False,True,True],[False,False,False,False],[False,False,True,True],[True,True,True,False]],[[True,False,True,True],[False,False,False,True],[True,False,True,True],[True,False,False,False]]], dtype = "bool")#candidate|3717|(16, 4, 4)|const|bool
var_3718 = relay.var("var_3718", dtype = "bool", shape = (16, 4, 4))#candidate|3718|(16, 4, 4)|var|bool
bop_3719 = relay.logical_and(const_3717.astype('bool'), relay.reshape(var_3718.astype('bool'), relay.shape_of(const_3717))) # shape=(16, 4, 4)
bop_3732 = relay.mod(var_3718.astype('float32'), relay.reshape(const_3717.astype('float32'), relay.shape_of(var_3718))) # shape=(16, 4, 4)
bop_3735 = relay.bitwise_xor(var_3718.astype('uint64'), relay.reshape(bop_3732.astype('uint64'), relay.shape_of(var_3718))) # shape=(16, 4, 4)
output = relay.Tuple([bop_3719,bop_3735,])
output2 = relay.Tuple([bop_3719,bop_3735,])
func_3748 = relay.Function([var_3718,], output)
mod['func_3748'] = func_3748
mod = relay.transform.InferType()(mod)
mutated_mod['func_3748'] = func_3748
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3749 = relay.var("var_3749", dtype = "bool", shape = (16, 4, 4))#candidate|3749|(16, 4, 4)|var|bool
func_3748_call = mutated_mod.get_global_var('func_3748')
call_3750 = func_3748_call(var_3749)
output = call_3750
func_3751 = relay.Function([var_3749], output)
mutated_mod['func_3751'] = func_3751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1620_call = mod.get_global_var('func_1620')
func_1622_call = mutated_mod.get_global_var('func_1622')
call_3756 = relay.TupleGetItem(func_1620_call(), 1)
call_3757 = relay.TupleGetItem(func_1622_call(), 1)
var_3760 = relay.var("var_3760", dtype = "float64", shape = (6, 6, 14))#candidate|3760|(6, 6, 14)|var|float64
bop_3761 = relay.logical_and(call_3756.astype('bool'), var_3760.astype('bool')) # shape=(6, 6, 14)
bop_3764 = relay.logical_and(call_3757.astype('bool'), var_3760.astype('bool')) # shape=(6, 6, 14)
func_2523_call = mod.get_global_var('func_2523')
func_2525_call = mutated_mod.get_global_var('func_2525')
call_3766 = relay.TupleGetItem(func_2523_call(), 1)
call_3767 = relay.TupleGetItem(func_2525_call(), 1)
output = relay.Tuple([bop_3761,call_3766,])
output2 = relay.Tuple([bop_3764,call_3767,])
func_3781 = relay.Function([var_3760,], output)
mod['func_3781'] = func_3781
mod = relay.transform.InferType()(mod)
mutated_mod['func_3781'] = func_3781
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3782 = relay.var("var_3782", dtype = "float64", shape = (6, 6, 14))#candidate|3782|(6, 6, 14)|var|float64
func_3781_call = mutated_mod.get_global_var('func_3781')
call_3783 = func_3781_call(var_3782)
output = call_3783
func_3784 = relay.Function([var_3782], output)
mutated_mod['func_3784'] = func_3784
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3788 = relay.var("var_3788", dtype = "int32", shape = (11, 8, 1))#candidate|3788|(11, 8, 1)|var|int32
var_3789 = relay.var("var_3789", dtype = "int32", shape = (11, 8, 3))#candidate|3789|(11, 8, 3)|var|int32
bop_3790 = relay.multiply(var_3788.astype('int32'), var_3789.astype('int32')) # shape=(11, 8, 3)
func_1714_call = mod.get_global_var('func_1714')
func_1716_call = mutated_mod.get_global_var('func_1716')
const_3800 = relay.const([-4.184448,-5.401990,1.553417,0.973105,7.799617,-9.665690,8.972321,-9.581044,-1.005780,-2.730879,7.300429,8.623708,9.995042,7.487811,-3.342835,5.321341,-2.459858,9.512702,-1.739189,9.236239,0.402362,-6.452363,7.082956,-7.759514,-2.906555,1.993639,4.809846,-3.756090,-1.560719,8.696899,-8.610732,4.612129,3.695022,-6.821731,-5.465632,7.635429,-9.513094,-6.565876,-3.063488,6.008004,1.837900,4.125288,9.805378,1.721885,9.891158,-1.062629,1.698682,-3.755653,0.016332,-2.259475,-1.575436,2.326218,5.871844,-2.346875,-5.125624,3.205327,9.138486,1.626020,-5.935253,-8.605742,1.971524,6.421269,2.429989,5.952831,7.030758,-3.992186,2.806560,-1.838597,7.579317,7.921066,-7.269935,5.377148,0.288020,-5.973255,3.620984,1.120212,1.816125,1.438804,-6.955037,1.668738,-4.065048,-8.833254,5.049921,-3.433562,1.566614,5.830139,-7.237557,4.319470,1.147264,0.983756,2.118008,6.328749,-8.153476,4.259103,-5.753910,-0.088515,-7.724346,-3.918859,3.667635,-3.670216,-1.527332,-1.582244,-7.281597,-9.579888,2.589447,-7.411446,-7.957251,3.141043,-9.223607,-8.305979,-8.635576,1.572147,1.430021,-4.035432,-1.362808,5.705696,-1.541367,-1.792121,-2.919214,-2.288912,-8.762597,-0.438334,2.950404,3.962189,-8.375598,-4.228711,-3.351881,6.060902,6.525036,-9.632715,-1.440266,9.085154,7.971330,9.767179,-7.593244,7.751982,-6.346251,-7.088281,-7.887984,4.036123,1.978262,9.899642,1.180900,8.289806,-9.773581,-0.593833,5.664486,-0.720451,8.188129,-2.716552,4.637137,1.521586,9.085693,1.572283,7.860631,-8.354324,-5.812343,5.490821,-4.963745,9.919914,-7.239972,4.091998,3.450937,2.774641,4.038093,-3.296845,8.858744,-0.280845], dtype = "float64")#candidate|3800|(168,)|const|float64
call_3799 = func_1714_call(relay.reshape(const_3800.astype('float64'), [6, 2, 14]))
call_3801 = func_1714_call(relay.reshape(const_3800.astype('float64'), [6, 2, 14]))
output = relay.Tuple([bop_3790,call_3799,const_3800,])
output2 = relay.Tuple([bop_3790,call_3801,const_3800,])
func_3807 = relay.Function([var_3788,var_3789,], output)
mod['func_3807'] = func_3807
mod = relay.transform.InferType()(mod)
mutated_mod['func_3807'] = func_3807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3807_call = mutated_mod.get_global_var('func_3807')
var_3809 = relay.var("var_3809", dtype = "int32", shape = (11, 8, 1))#candidate|3809|(11, 8, 1)|var|int32
var_3810 = relay.var("var_3810", dtype = "int32", shape = (11, 8, 3))#candidate|3810|(11, 8, 3)|var|int32
call_3808 = func_3807_call(var_3809,var_3810,)
output = call_3808
func_3811 = relay.Function([var_3809,var_3810,], output)
mutated_mod['func_3811'] = func_3811
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3074_call = mod.get_global_var('func_3074')
func_3076_call = mutated_mod.get_global_var('func_3076')
call_3819 = func_3074_call()
call_3820 = func_3074_call()
output = call_3819
output2 = call_3820
func_3823 = relay.Function([], output)
mod['func_3823'] = func_3823
mod = relay.transform.InferType()(mod)
output = func_3823()
func_3824 = relay.Function([], output)
mutated_mod['func_3824'] = func_3824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3033_call = mod.get_global_var('func_3033')
func_3035_call = mutated_mod.get_global_var('func_3035')
call_3828 = relay.TupleGetItem(func_3033_call(), 0)
call_3829 = relay.TupleGetItem(func_3035_call(), 0)
output = relay.Tuple([call_3828,])
output2 = relay.Tuple([call_3829,])
func_3842 = relay.Function([], output)
mod['func_3842'] = func_3842
mod = relay.transform.InferType()(mod)
output = func_3842()
func_3843 = relay.Function([], output)
mutated_mod['func_3843'] = func_3843
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3315_call = mod.get_global_var('func_3315')
func_3316_call = mutated_mod.get_global_var('func_3316')
call_3875 = relay.TupleGetItem(func_3315_call(), 0)
call_3876 = relay.TupleGetItem(func_3316_call(), 0)
output = call_3875
output2 = call_3876
func_3877 = relay.Function([], output)
mod['func_3877'] = func_3877
mod = relay.transform.InferType()(mod)
output = func_3877()
func_3878 = relay.Function([], output)
mutated_mod['func_3878'] = func_3878
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3921 = relay.var("var_3921", dtype = "int64", shape = (9, 14, 10))#candidate|3921|(9, 14, 10)|var|int64
var_3922 = relay.var("var_3922", dtype = "int64", shape = (9, 14, 10))#candidate|3922|(9, 14, 10)|var|int64
bop_3923 = relay.greater_equal(var_3921.astype('bool'), relay.reshape(var_3922.astype('bool'), relay.shape_of(var_3921))) # shape=(9, 14, 10)
func_3781_call = mod.get_global_var('func_3781')
func_3784_call = mutated_mod.get_global_var('func_3784')
const_3929 = relay.const([0.901250,0.011651,6.262772,-7.652165,-5.327258,-4.274762,-1.740215,-9.086667,3.741895,-9.314866,-1.032298,-8.735106,8.906334,5.210914,-0.435808,3.966068,-5.656283,4.080323,-0.871612,0.301763,2.037393,5.502944,-2.731346,9.879805,-0.024572,-9.217434,-8.588983,9.846324,2.832954,-5.995315,-1.411936,0.785671,3.937333,-4.335065,-5.151148,-2.659939,4.592370,-3.825815,-2.684476,-8.665211,6.405739,2.283862,0.777298,0.553071,1.313839,-3.224109,3.718336,4.273637,-5.238646,7.899406,6.921579,3.739002,1.055244,-5.260472,7.174608,8.435605,-6.647792,-9.410658,9.201224,-9.687363,-0.713860,-6.018561,-5.984217,-4.453313,-5.299229,-0.593146,8.142913,-1.120168,7.332166,-9.103128,0.952822,6.025503,-7.629828,-0.936165,-4.544573,4.910469,2.799696,-0.217185,5.567002,8.446340,-8.473206,9.714665,0.227437,7.887789,-9.034383,4.479785,6.466231,3.918623,-0.498302,8.995593,-3.185898,0.659489,6.680149,-8.459954,-6.096532,-9.421853,1.163910,3.724710,9.153016,9.798899,-4.154828,-6.623778,8.630665,-2.309843,3.370077,-1.226946,-2.685825,8.073945,-2.745588,-3.774670,2.179034,5.448238,-3.933423,6.980445,6.799590,7.858344,4.289612,8.508706,-5.411719,1.817959,-5.217159,0.442303,8.089344,-4.767434,-1.456688,6.788736,2.831108,-4.542904,4.580963,0.177558,-3.318142,-4.887011,-0.670513,7.167067,9.616458,-1.543564,-6.603890,-5.649483,3.152856,1.516857,8.367591,7.404620,-5.671043,-2.140462,-6.568408,-4.680188,1.314437,-4.410022,8.338364,-6.608442,-7.423347,-8.239326,-4.263387,8.650033,0.052588,-8.409627,5.562405,1.406069,2.156968,1.473796,5.834229,2.063168,-0.364092,4.812627,1.469515,3.820381,-1.019598,-0.763196,-0.228654,-4.557098,4.859367,8.850542,1.983969,-7.102749,-3.276263,-7.446567,7.551812,-6.011608,1.813744,5.441888,1.703719,3.368928,-0.242776,3.351102,5.151797,-1.723753,-4.580303,7.782974,-7.903161,-2.223793,5.181028,7.315378,-1.347180,-0.562714,0.006515,-8.222129,-6.733458,-6.526101,-9.145165,-5.639049,-4.348309,-7.318378,-0.363098,-8.788591,9.659297,1.873143,5.914586,4.163778,7.722742,5.622482,-1.196184,7.762690,1.149919,6.436755,6.017506,0.907348,1.087969,-9.165083,9.702938,-3.370991,-2.041603,1.713078,-7.015205,8.978677,7.764268,-5.480001,2.850029,-5.556681,-8.374421,-7.688946,5.261760,3.535715,8.859644,-1.598716,-9.022876,1.971956,9.373210,-2.119347,7.472759,7.435563,-1.370151,-4.142191,2.335116,0.505128,4.766168,-1.514011,1.373085,1.975924,0.977241,-1.460329,-2.626276,-4.659787,-2.332895,-0.386480,9.531686,-5.951765,0.909416,5.188698,-7.611042,-5.765221,-1.435896,-2.238601,-3.262129,-8.869669,-5.895600,3.047524,-2.473927,-4.618184,-5.260443,-8.661938,-6.174210,-3.146540,-5.050065,-1.391288,-4.876728,-4.087377,7.401215,-8.994801,-2.656165,-9.189763,5.665824,4.697905,2.167203,4.475217,-7.704667,3.659903,-3.953220,6.854668,3.670040,0.826751,-9.650175,-2.265069,4.602959,-8.991728,2.187295,-2.845102,-4.437664,-0.623220,3.671705,-2.140612,-9.676466,-6.771319,3.499188,9.521400,9.851911,-9.362252,-6.273573,-9.382222,3.449227,3.306036,7.712488,-4.142785,2.709787,3.460231,-8.197515,4.584338,-7.747212,6.048892,7.457866,-5.561066,-8.695974,-0.408554,-5.837795,-5.882222,6.704266,-0.484034,2.261634,5.235886,-7.163553,6.450319,-7.885911,5.805978,-2.207273,-0.761607,7.804917,-7.182193,9.113240,-7.055430,3.013743,4.537496,-4.706139,7.823945,-6.499466,-3.613611,-4.217801,6.102631,-8.981709,4.444147,-5.520434,-1.720831,-5.952494,5.812660,-3.304087,5.265081,-6.202496,-9.681386,6.711628,-3.121972,-6.569334,-1.563177,-6.589692,1.124946,-1.915580,0.292258,-9.284021,-0.653109,-8.100503,-4.820374,2.273441,1.643693,3.969260,-4.131233,3.176062,-5.009196,3.506787,-4.434328,9.983120,3.493273,-6.926496,-6.508852,-9.802005,-1.211448,-7.892357,1.226644,-2.788911,6.424630,9.498441,-0.310360,-4.480844,-2.486661,7.682861,0.999513,3.339784,-3.535482,3.269603,-8.764319,8.358777,-9.345112,-0.221175,3.001428,-7.279033,-2.362674,-2.725146,4.165944,7.792254,2.068448,-9.251669,6.255929,8.244282,-9.888001,-5.234812,-6.571779,3.984593,4.744645,2.870673,-6.399039,4.852542,6.390031,-0.496993,-2.298362,-6.429744,-7.857919,-9.997379,-2.894513,-1.633017,-9.102837,-8.582496,-9.116984,-2.761816,1.131591,4.857300,4.241777,-4.381216,-1.892906,9.298947,-1.117035,-3.961403,1.874143,8.274074,-4.352839,-5.278875,-5.021581,-7.391503,-1.803616,6.598688,-0.423137,6.880662,8.696293,-2.861626,-4.750458,3.371794,3.572311,-1.260617,-3.418275,7.288951,0.872824,-7.399775,-1.629331,-0.093406,6.380152,-2.524111,-6.083423,2.412772,6.343473,-5.454122,-1.975074,-8.272661,8.214627,-1.082423,-3.986614,4.892723,6.185329,-7.785767,-6.682598,-5.210920,-6.936310,8.006484,-9.419494,-6.834616,-7.844212,-8.236993,-5.439650,-7.632435,4.541672,-5.275443,-6.025854,1.314622,3.861879,6.576350,-3.880949,6.067818,-3.711128,-7.920553,2.019406,-5.256635,4.838271,-2.678048,-9.105416,5.019578,4.658568,0.365731,9.646328,9.793901,-5.126907], dtype = "float64")#candidate|3929|(504,)|const|float64
call_3928 = relay.TupleGetItem(func_3781_call(relay.reshape(const_3929.astype('float64'), [6, 6, 14])), 0)
call_3930 = relay.TupleGetItem(func_3784_call(relay.reshape(const_3929.astype('float64'), [6, 6, 14])), 0)
uop_3931 = relay.cosh(var_3922.astype('float32')) # shape=(9, 14, 10)
output = relay.Tuple([bop_3923,call_3928,const_3929,uop_3931,])
output2 = relay.Tuple([bop_3923,call_3930,const_3929,uop_3931,])
func_3934 = relay.Function([var_3921,var_3922,], output)
mod['func_3934'] = func_3934
mod = relay.transform.InferType()(mod)
mutated_mod['func_3934'] = func_3934
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3934_call = mutated_mod.get_global_var('func_3934')
var_3936 = relay.var("var_3936", dtype = "int64", shape = (9, 14, 10))#candidate|3936|(9, 14, 10)|var|int64
var_3937 = relay.var("var_3937", dtype = "int64", shape = (9, 14, 10))#candidate|3937|(9, 14, 10)|var|int64
call_3935 = func_3934_call(var_3936,var_3937,)
output = call_3935
func_3938 = relay.Function([var_3936,var_3937,], output)
mutated_mod['func_3938'] = func_3938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2811_call = mod.get_global_var('func_2811')
func_2813_call = mutated_mod.get_global_var('func_2813')
call_3946 = func_2811_call()
call_3947 = func_2811_call()
uop_3952 = relay.erf(call_3946.astype('float32')) # shape=(4, 6, 11)
uop_3954 = relay.erf(call_3947.astype('float32')) # shape=(4, 6, 11)
func_244_call = mod.get_global_var('func_244')
func_246_call = mutated_mod.get_global_var('func_246')
call_3955 = relay.TupleGetItem(func_244_call(relay.reshape(uop_3952.astype('int8'), [4, 6, 11])), 0)
call_3956 = relay.TupleGetItem(func_246_call(relay.reshape(uop_3952.astype('int8'), [4, 6, 11])), 0)
func_423_call = mod.get_global_var('func_423')
func_428_call = mutated_mod.get_global_var('func_428')
const_3958 = relay.const(-2, dtype = "int32")#candidate|3958|()|const|int32
var_3959 = relay.var("var_3959", dtype = "int32", shape = (630,))#candidate|3959|(630,)|var|int32
call_3957 = relay.TupleGetItem(func_423_call(relay.reshape(const_3958.astype('int32'), []), relay.reshape(var_3959.astype('int32'), [7, 9, 10]), relay.reshape(call_3946.astype('int8'), [264,]), ), 2)
call_3960 = relay.TupleGetItem(func_428_call(relay.reshape(const_3958.astype('int32'), []), relay.reshape(var_3959.astype('int32'), [7, 9, 10]), relay.reshape(call_3946.astype('int8'), [264,]), ), 2)
func_3823_call = mod.get_global_var('func_3823')
func_3824_call = mutated_mod.get_global_var('func_3824')
call_3970 = func_3823_call()
call_3971 = func_3823_call()
func_2811_call = mod.get_global_var('func_2811')
func_2813_call = mutated_mod.get_global_var('func_2813')
call_3973 = func_2811_call()
call_3974 = func_2811_call()
output = relay.Tuple([uop_3952,call_3955,call_3957,const_3958,var_3959,call_3970,call_3973,])
output2 = relay.Tuple([uop_3954,call_3956,call_3960,const_3958,var_3959,call_3971,call_3974,])
func_3976 = relay.Function([var_3959,], output)
mod['func_3976'] = func_3976
mod = relay.transform.InferType()(mod)
var_3977 = relay.var("var_3977", dtype = "int32", shape = (630,))#candidate|3977|(630,)|var|int32
output = func_3976(var_3977)
func_3978 = relay.Function([var_3977], output)
mutated_mod['func_3978'] = func_3978
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3988 = relay.var("var_3988", dtype = "uint32", shape = (6, 16, 12))#candidate|3988|(6, 16, 12)|var|uint32
var_3989 = relay.var("var_3989", dtype = "uint32", shape = (6, 16, 12))#candidate|3989|(6, 16, 12)|var|uint32
bop_3990 = relay.multiply(var_3988.astype('uint32'), relay.reshape(var_3989.astype('uint32'), relay.shape_of(var_3988))) # shape=(6, 16, 12)
func_3823_call = mod.get_global_var('func_3823')
func_3824_call = mutated_mod.get_global_var('func_3824')
call_3997 = func_3823_call()
call_3998 = func_3823_call()
output = relay.Tuple([bop_3990,call_3997,])
output2 = relay.Tuple([bop_3990,call_3998,])
func_4024 = relay.Function([var_3988,var_3989,], output)
mod['func_4024'] = func_4024
mod = relay.transform.InferType()(mod)
mutated_mod['func_4024'] = func_4024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4024_call = mutated_mod.get_global_var('func_4024')
var_4026 = relay.var("var_4026", dtype = "uint32", shape = (6, 16, 12))#candidate|4026|(6, 16, 12)|var|uint32
var_4027 = relay.var("var_4027", dtype = "uint32", shape = (6, 16, 12))#candidate|4027|(6, 16, 12)|var|uint32
call_4025 = func_4024_call(var_4026,var_4027,)
output = call_4025
func_4028 = relay.Function([var_4026,var_4027,], output)
mutated_mod['func_4028'] = func_4028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1083_call = mod.get_global_var('func_1083')
func_1085_call = mutated_mod.get_global_var('func_1085')
call_4057 = relay.TupleGetItem(func_1083_call(), 7)
call_4058 = relay.TupleGetItem(func_1085_call(), 7)
output = relay.Tuple([call_4057,])
output2 = relay.Tuple([call_4058,])
func_4074 = relay.Function([], output)
mod['func_4074'] = func_4074
mod = relay.transform.InferType()(mod)
output = func_4074()
func_4075 = relay.Function([], output)
mutated_mod['func_4075'] = func_4075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1620_call = mod.get_global_var('func_1620')
func_1622_call = mutated_mod.get_global_var('func_1622')
call_4139 = relay.TupleGetItem(func_1620_call(), 0)
call_4140 = relay.TupleGetItem(func_1622_call(), 0)
output = relay.Tuple([call_4139,])
output2 = relay.Tuple([call_4140,])
func_4141 = relay.Function([], output)
mod['func_4141'] = func_4141
mod = relay.transform.InferType()(mod)
mutated_mod['func_4141'] = func_4141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4141_call = mutated_mod.get_global_var('func_4141')
call_4142 = func_4141_call()
output = call_4142
func_4143 = relay.Function([], output)
mutated_mod['func_4143'] = func_4143
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2204_call = mod.get_global_var('func_2204')
func_2206_call = mutated_mod.get_global_var('func_2206')
call_4154 = func_2204_call()
call_4155 = func_2204_call()
func_3416_call = mod.get_global_var('func_3416')
func_3418_call = mutated_mod.get_global_var('func_3418')
var_4158 = relay.var("var_4158", dtype = "int8", shape = (264,))#candidate|4158|(264,)|var|int8
call_4157 = relay.TupleGetItem(func_3416_call(relay.reshape(var_4158.astype('int8'), [264,])), 0)
call_4159 = relay.TupleGetItem(func_3418_call(relay.reshape(var_4158.astype('int8'), [264,])), 0)
var_4162 = relay.var("var_4162", dtype = "float32", shape = (16, 6, 4))#candidate|4162|(16, 6, 4)|var|float32
bop_4163 = relay.mod(call_4154.astype('float64'), relay.reshape(var_4162.astype('float64'), relay.shape_of(call_4154))) # shape=(16, 6, 4)
bop_4166 = relay.mod(call_4155.astype('float64'), relay.reshape(var_4162.astype('float64'), relay.shape_of(call_4155))) # shape=(16, 6, 4)
func_3781_call = mod.get_global_var('func_3781')
func_3784_call = mutated_mod.get_global_var('func_3784')
const_4168 = relay.const([[9.141940],[8.001180],[0.389014],[-8.495458],[1.414287],[-6.184884],[-8.790901],[7.701245],[8.891902],[5.577524],[-6.375265],[9.777919],[-6.543656],[8.629520],[2.709937],[-9.479258],[4.656209],[-5.628976],[4.698767],[6.682859],[5.163536],[-0.992337],[-9.109530],[9.445225],[0.830186],[-5.621123],[1.728740],[2.406963],[-9.127494],[-2.774661],[-2.885781],[-0.292296],[-1.265227],[-3.368838],[-7.755688],[1.156188],[-0.841184],[3.488519],[8.619897],[-8.814009],[7.172117],[4.366951],[-8.407759],[-0.837423],[1.861376],[8.794138],[8.174310],[1.974810],[-4.915581],[0.314880],[0.992858],[-3.405320],[-3.439031],[-8.567483],[7.148485],[9.665338],[6.634455],[7.113080],[7.244045],[-6.479577],[-1.858445],[2.753793],[3.464025],[6.291517],[-8.309096],[-9.707630],[9.037797],[9.200682],[-7.833510],[-8.375661],[-6.176046],[-2.355233],[-4.078662],[-2.795442],[-8.793374],[-6.293081],[-2.193271],[-9.977279],[-5.792381],[8.054843],[5.537124],[-3.920072],[-8.460902],[-5.015641],[0.532563],[-0.770363],[-6.051504],[9.333518],[-2.897843],[1.678134],[-0.201331],[9.320167],[2.515501],[-5.948467],[-6.663294],[-5.583496],[-1.076719],[-9.667119],[9.676400],[0.121071],[3.726715],[-2.722243],[6.239422],[-1.017625],[6.776368],[-6.094417],[0.414380],[-6.555224],[8.390102],[-8.828932],[-1.435477],[5.707859],[5.833159],[-2.263082],[8.777438],[0.125448],[6.425335],[-8.700432],[7.925108],[9.576778],[-3.588164],[-6.840855],[7.223948],[-8.499509],[-6.695613],[-2.122592],[-2.010951],[8.308064],[-9.315594],[-2.732987],[7.937467],[-8.558532],[9.979414],[1.483068],[-3.865802],[-2.501927],[-5.034649],[-3.025586],[4.185451],[6.471265],[-3.853379],[1.463104],[2.388081],[-8.802815],[-2.089948],[1.846441],[4.220801],[-0.389481],[0.891789],[2.033728],[-7.570297],[-7.148535],[8.220926],[0.892405],[-4.342352],[-7.949647],[-7.183256],[8.716645],[-8.968693],[9.180538],[-4.047032],[-9.192494],[9.268717],[-2.022482],[6.691102],[-4.569605],[8.332279],[-5.169672],[6.350686],[-1.028711],[-6.997052],[-2.891802],[-0.208125],[8.817838],[-6.838063],[2.075646],[3.637068],[-5.782381],[-3.793566],[0.532977],[-3.559979],[-6.389865],[1.903976],[-1.512657],[-1.988097],[-6.842600],[6.557576],[7.886940],[-4.889122],[-4.836463],[-6.692867],[8.812749],[-1.344078],[-0.901394],[-3.536500],[-6.171268],[8.657575],[0.579070],[8.790450],[4.411215],[-2.629363],[6.468190],[0.985267],[5.936649],[5.121251],[-9.786685],[9.926189],[9.126158],[6.992571],[-7.977160],[-1.221300],[-9.958837],[7.031776],[-1.206904],[-7.077361],[-1.925426],[0.333112],[-0.560762],[1.719318],[-8.053489],[-2.292291],[-8.361700],[-4.181832],[0.967910],[3.299879],[0.993771],[-7.170219],[2.114629],[1.352717],[-7.831182],[0.297007],[-1.538021],[-2.030294],[6.577044],[-2.847440],[-9.812876],[-9.890213],[-9.969095],[5.309833],[-1.141514],[-5.029155],[-4.342889],[-7.549958],[-7.345122],[7.957394],[6.861554],[-3.180366],[0.660237],[-6.178875],[-5.741464],[-9.477483],[0.955416],[0.033178],[5.970728],[8.240482],[6.054991],[0.554919],[-7.370274],[1.381542],[-0.295394],[-0.190800],[0.875072],[9.810306],[8.838740],[-4.209576],[1.158117],[3.446549],[5.042145],[-5.563793],[2.822546],[7.032576],[9.862440],[-7.676309],[-7.245730],[5.263747],[-4.677127],[-9.342041],[-8.946737],[-9.603073],[9.242835],[3.041849],[9.165938],[-2.453278],[3.936601],[2.682542],[-1.372818],[3.341867],[5.046659],[-1.299993],[8.931206],[-0.740885],[8.411107],[6.635158],[5.019301],[1.693368],[-8.391103],[7.103159],[6.819737],[1.905673],[-3.635527],[2.735177],[2.666337],[0.929056],[-3.251253],[-9.134292],[0.295987],[4.090480],[5.372905],[-8.176609],[-7.820572],[6.973357],[-7.854056],[-6.008808],[-3.136416],[-2.308751],[-7.071363],[-3.810533],[-7.470693],[3.868641],[7.818714],[-6.572696],[-8.122116],[3.788808],[-3.257472],[-7.548010],[1.778899],[-0.420854],[-9.298581],[-0.539293],[-6.100397],[-0.673712],[-9.919304],[-3.653539],[-6.562446],[-0.579332],[9.383468],[-8.286310],[-9.875428],[8.883160],[0.081997],[-4.068641],[6.888532],[-6.842575],[9.034545],[4.729638],[5.981155],[4.526319],[-2.951339],[-3.813154],[0.109117],[-8.828576],[3.807981],[-2.613222],[-9.788521],[-9.287347],[-0.863979],[-6.216045],[9.081997],[0.401940],[1.225695],[-2.182665],[-1.980692],[8.650048],[2.366148],[2.288316],[-0.064641],[9.682144],[-9.574551],[3.247605],[0.446944],[-4.501099],[-1.462024],[-6.572275],[6.822670],[0.651448],[-7.352846],[9.106099],[6.821218],[1.114705],[-9.871193],[4.980487],[-1.552955],[-3.147581],[-1.494563],[6.240946],[-5.090693],[7.329687],[-1.076654],[-3.767747],[-2.091655],[5.881840],[-2.055318],[6.246857],[8.165759],[-6.030829],[-0.689683],[-7.200977],[0.135777],[3.775164],[-6.707266],[8.505899],[7.105535],[-8.303480],[-9.012225],[4.981662],[-4.081294],[2.932923],[-1.326908],[-7.892906],[2.988432],[0.418929],[-2.893209],[-0.999423],[9.825290],[2.877358],[-7.866820],[-2.576846],[-1.906367],[-0.359057],[0.278502],[3.029492],[-7.999400],[-2.942785],[9.030572],[-4.962338],[-8.029768],[-8.105996],[7.673216],[-8.184095],[5.006409],[-3.595332],[-1.134025],[4.955084],[3.725327],[-9.812727],[8.803714],[-3.548886],[-6.481418],[-7.763306],[4.012780],[8.518388],[3.136834],[-6.803956],[-6.069553],[2.941890],[7.607573],[-7.010725],[-7.539405],[-1.712452],[0.725135],[-3.883721],[-3.456017],[-1.810471],[-6.919643],[-4.193723],[7.831856],[1.553426],[-3.963847],[9.835354],[-4.351791],[-0.331072],[-7.386982],[3.025345],[-9.101519],[0.046400],[-0.400194],[-8.404275],[-7.692107],[-2.377667],[-4.252008],[1.524569],[-1.120437],[-2.068400],[-5.000318],[0.935993],[-7.577502],[-7.446753],[-5.847736],[4.599923],[4.283573],[-8.244707],[-8.441267],[-1.049617],[9.758151],[8.338671],[-5.914180],[6.744584],[6.189520],[2.420270],[6.050922],[-3.273784],[-6.565808],[6.552889],[5.581907],[7.339837],[7.577610],[-1.663221],[-0.468513],[-4.268243],[3.185100],[4.700705],[-1.837700],[-9.665924],[-1.461564]], dtype = "float64")#candidate|4168|(504, 1)|const|float64
call_4167 = relay.TupleGetItem(func_3781_call(relay.reshape(const_4168.astype('float64'), [6, 6, 14])), 0)
call_4169 = relay.TupleGetItem(func_3784_call(relay.reshape(const_4168.astype('float64'), [6, 6, 14])), 0)
func_3877_call = mod.get_global_var('func_3877')
func_3878_call = mutated_mod.get_global_var('func_3878')
call_4176 = func_3877_call()
call_4177 = func_3877_call()
uop_4179 = relay.sqrt(call_4167.astype('float64')) # shape=(6, 6, 14)
uop_4181 = relay.sqrt(call_4169.astype('float64')) # shape=(6, 6, 14)
output = relay.Tuple([call_4157,var_4158,bop_4163,const_4168,call_4176,uop_4179,])
output2 = relay.Tuple([call_4159,var_4158,bop_4166,const_4168,call_4177,uop_4181,])
func_4183 = relay.Function([var_4158,var_4162,], output)
mod['func_4183'] = func_4183
mod = relay.transform.InferType()(mod)
mutated_mod['func_4183'] = func_4183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4183_call = mutated_mod.get_global_var('func_4183')
var_4185 = relay.var("var_4185", dtype = "int8", shape = (264,))#candidate|4185|(264,)|var|int8
var_4186 = relay.var("var_4186", dtype = "float32", shape = (16, 6, 4))#candidate|4186|(16, 6, 4)|var|float32
call_4184 = func_4183_call(var_4185,var_4186,)
output = call_4184
func_4187 = relay.Function([var_4185,var_4186,], output)
mutated_mod['func_4187'] = func_4187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3230_call = mod.get_global_var('func_3230')
func_3231_call = mutated_mod.get_global_var('func_3231')
call_4253 = relay.TupleGetItem(func_3230_call(), 2)
call_4254 = relay.TupleGetItem(func_3231_call(), 2)
output = relay.Tuple([call_4253,])
output2 = relay.Tuple([call_4254,])
func_4259 = relay.Function([], output)
mod['func_4259'] = func_4259
mod = relay.transform.InferType()(mod)
output = func_4259()
func_4260 = relay.Function([], output)
mutated_mod['func_4260'] = func_4260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3690_call = mod.get_global_var('func_3690')
func_3692_call = mutated_mod.get_global_var('func_3692')
call_4274 = relay.TupleGetItem(func_3690_call(), 0)
call_4275 = relay.TupleGetItem(func_3692_call(), 0)
var_4297 = relay.var("var_4297", dtype = "int8", shape = (264,))#candidate|4297|(264,)|var|int8
bop_4298 = relay.subtract(call_4274.astype('int64'), relay.reshape(var_4297.astype('int64'), relay.shape_of(call_4274))) # shape=(264,)
bop_4301 = relay.subtract(call_4275.astype('int64'), relay.reshape(var_4297.astype('int64'), relay.shape_of(call_4275))) # shape=(264,)
func_893_call = mod.get_global_var('func_893')
func_897_call = mutated_mod.get_global_var('func_897')
var_4306 = relay.var("var_4306", dtype = "float32", shape = (297,))#candidate|4306|(297,)|var|float32
call_4305 = relay.TupleGetItem(func_893_call(relay.reshape(var_4306.astype('float32'), [3, 11, 9]), relay.reshape(call_4274.astype('int8'), [264,]), ), 2)
call_4307 = relay.TupleGetItem(func_897_call(relay.reshape(var_4306.astype('float32'), [3, 11, 9]), relay.reshape(call_4274.astype('int8'), [264,]), ), 2)
func_1319_call = mod.get_global_var('func_1319')
func_1320_call = mutated_mod.get_global_var('func_1320')
call_4320 = func_1319_call()
call_4321 = func_1319_call()
output = relay.Tuple([bop_4298,call_4305,var_4306,call_4320,])
output2 = relay.Tuple([bop_4301,call_4307,var_4306,call_4321,])
func_4322 = relay.Function([var_4297,var_4306,], output)
mod['func_4322'] = func_4322
mod = relay.transform.InferType()(mod)
mutated_mod['func_4322'] = func_4322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4322_call = mutated_mod.get_global_var('func_4322')
var_4324 = relay.var("var_4324", dtype = "int8", shape = (264,))#candidate|4324|(264,)|var|int8
var_4325 = relay.var("var_4325", dtype = "float32", shape = (297,))#candidate|4325|(297,)|var|float32
call_4323 = func_4322_call(var_4324,var_4325,)
output = call_4323
func_4326 = relay.Function([var_4324,var_4325,], output)
mutated_mod['func_4326'] = func_4326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1361_call = mod.get_global_var('func_1361')
func_1363_call = mutated_mod.get_global_var('func_1363')
call_4333 = relay.TupleGetItem(func_1361_call(), 0)
call_4334 = relay.TupleGetItem(func_1363_call(), 0)
func_1083_call = mod.get_global_var('func_1083')
func_1085_call = mutated_mod.get_global_var('func_1085')
call_4339 = relay.TupleGetItem(func_1083_call(), 1)
call_4340 = relay.TupleGetItem(func_1085_call(), 1)
func_839_call = mod.get_global_var('func_839')
func_841_call = mutated_mod.get_global_var('func_841')
call_4350 = relay.TupleGetItem(func_839_call(), 0)
call_4351 = relay.TupleGetItem(func_841_call(), 0)
output = relay.Tuple([call_4333,call_4339,call_4350,])
output2 = relay.Tuple([call_4334,call_4340,call_4351,])
func_4373 = relay.Function([], output)
mod['func_4373'] = func_4373
mod = relay.transform.InferType()(mod)
mutated_mod['func_4373'] = func_4373
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4373_call = mutated_mod.get_global_var('func_4373')
call_4374 = func_4373_call()
output = call_4374
func_4375 = relay.Function([], output)
mutated_mod['func_4375'] = func_4375
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1083_call = mod.get_global_var('func_1083')
func_1085_call = mutated_mod.get_global_var('func_1085')
call_4381 = relay.TupleGetItem(func_1083_call(), 1)
call_4382 = relay.TupleGetItem(func_1085_call(), 1)
func_2581_call = mod.get_global_var('func_2581')
func_2583_call = mutated_mod.get_global_var('func_2583')
call_4396 = relay.TupleGetItem(func_2581_call(), 4)
call_4397 = relay.TupleGetItem(func_2583_call(), 4)
uop_4418 = relay.tan(call_4381.astype('float64')) # shape=(4, 6, 11)
uop_4420 = relay.tan(call_4382.astype('float64')) # shape=(4, 6, 11)
output = relay.Tuple([call_4396,uop_4418,])
output2 = relay.Tuple([call_4397,uop_4420,])
func_4422 = relay.Function([], output)
mod['func_4422'] = func_4422
mod = relay.transform.InferType()(mod)
output = func_4422()
func_4423 = relay.Function([], output)
mutated_mod['func_4423'] = func_4423
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4427 = relay.var("var_4427", dtype = "int8", shape = (16, 8, 15))#candidate|4427|(16, 8, 15)|var|int8
const_4428 = relay.const([[[-8,3,4,9,-7,-10,4,9,-10,-1,3,9,-4,6,-10],[1,2,5,9,5,-9,-8,-7,-9,5,-1,4,6,5,-3],[3,-5,9,-10,-4,-6,-9,5,1,-3,4,7,-2,-7,4],[-3,3,1,-8,10,-5,-6,-1,10,-7,-10,-7,-10,-7,7],[6,-8,10,10,-2,1,-9,2,9,3,5,6,10,10,-4],[1,-10,8,-10,-9,1,10,6,3,5,1,1,1,-5,1],[1,1,10,-3,-10,-5,-10,-2,-8,-4,-2,3,2,7,7],[9,9,-1,-1,-1,5,-1,-10,3,-9,1,10,9,9,1]],[[3,6,-2,-10,1,2,-7,1,8,-5,3,-2,-1,-6,4],[-8,9,-8,-3,2,2,-8,-8,8,6,-7,-1,-3,10,5],[-7,3,-9,7,-1,-5,-4,4,5,2,-5,-10,7,-1,3],[1,2,-7,6,4,4,10,2,2,6,-9,-2,-7,4,-8],[-7,8,4,2,-1,7,6,5,-3,-7,10,10,-7,-3,-7],[10,9,-5,5,-10,6,4,-7,9,-6,7,-4,-8,-3,2],[1,8,-9,-10,2,5,-9,9,-9,-4,-7,-1,-9,2,1],[4,5,9,-6,-10,-10,8,3,-7,-8,-7,3,5,-8,-4]],[[10,-10,-1,-9,-9,7,4,-3,3,-1,-9,5,8,-4,7],[-7,5,4,-8,10,1,-1,3,6,-1,4,-5,4,8,-10],[-5,4,6,-3,-10,-6,-2,-8,10,-10,10,5,-4,-9,-8],[-9,-7,10,-10,10,7,3,-4,4,-6,6,-10,-1,1,-9],[10,9,-3,-3,-3,-5,10,10,10,9,-10,-3,-6,-7,6],[-6,-5,6,-4,-3,3,-7,-7,-8,-3,-6,-3,-5,3,6],[9,-8,6,4,-2,-9,4,-1,-5,1,-7,10,6,-9,-9],[-10,6,3,-1,-6,-4,1,2,-3,10,-4,-9,-5,2,-3]],[[8,9,3,-7,-1,-9,-9,4,-10,-8,-1,7,9,-4,-3],[-1,-2,6,2,-10,-6,7,9,7,-8,-2,-9,10,9,10],[3,-5,-4,2,4,-1,3,8,-1,5,-3,-8,-6,-2,-4],[-10,-8,4,6,9,2,-2,8,-8,8,8,-2,4,7,-4],[-2,8,1,-1,-9,-9,-10,5,5,-7,-9,-4,1,9,-6],[9,-1,-10,-6,-9,3,6,-1,1,2,-6,-3,2,-8,4],[-7,-6,7,-1,8,7,-8,-5,2,4,4,-9,-2,-2,3],[6,6,-10,-7,7,-3,-7,7,-1,-7,-7,6,-9,6,-9]],[[-9,2,-9,10,5,1,2,-10,-7,-10,-5,7,-2,8,-10],[-10,1,4,-6,6,-2,9,3,10,10,4,8,5,-10,1],[-9,8,-5,-2,9,-2,4,-4,3,-7,-6,6,-4,6,-3],[5,10,-4,8,-5,3,-9,-1,4,-6,4,-5,8,3,-5],[-2,8,4,6,9,10,-1,9,-1,-7,-5,1,-3,-1,-2],[1,-7,-8,3,4,9,4,-4,-3,7,1,1,3,-10,10],[-1,10,2,-10,3,-10,9,-2,8,-5,5,10,10,10,8],[-4,3,-10,9,3,-3,4,-7,-4,-2,-10,6,3,-3,-4]],[[4,-3,-1,1,2,-1,7,6,4,6,10,-2,-8,-10,9],[4,-3,10,10,3,-7,7,-2,7,5,-1,-1,-1,10,-2],[7,-4,-4,6,8,-6,-6,1,7,5,9,-7,2,9,-1],[-1,-8,-1,-9,-6,8,4,-6,3,10,5,7,2,-2,-1],[4,1,9,4,-1,-7,-2,-3,7,-2,-8,-8,1,-4,3],[-5,-9,8,-10,-8,-3,-8,-7,3,-10,2,-2,-3,-2,-7],[4,3,2,-1,-6,-1,-5,5,-3,7,5,-1,2,1,1],[-1,4,6,7,-8,8,3,-10,5,-9,7,4,1,2,-9]],[[4,5,4,-3,1,-4,-1,-2,7,6,-2,8,-3,-9,4],[7,8,5,-5,2,10,-7,-5,3,6,8,4,-3,8,1],[2,10,-2,-3,-5,-7,5,5,-4,-1,-8,10,6,1,5],[-4,2,8,-10,2,-8,-8,2,-4,-4,7,-6,5,10,6],[10,2,-5,-5,-1,-10,-6,3,-4,6,-2,1,10,1,-2],[5,6,-3,8,-8,6,2,-6,2,2,9,1,-5,4,2],[1,-9,5,-10,9,-5,-3,9,-2,1,-10,-1,8,3,9],[9,3,7,-9,2,-4,-5,2,6,8,9,8,1,3,8]],[[-1,2,-5,3,-7,-2,-2,7,4,9,3,-1,7,6,8],[-1,-1,7,3,1,-7,-10,1,-2,-3,6,8,-6,9,-4],[-6,-10,-10,-4,-8,-3,-8,-3,-10,-6,5,-8,9,-7,-6],[9,-10,10,7,4,-8,10,2,9,-8,5,-6,6,9,-8],[-8,6,8,-7,9,-2,-10,5,8,4,-8,1,3,3,-5],[-6,10,9,7,4,-9,3,3,-9,-3,-8,5,-6,9,10],[-2,4,-10,1,1,1,2,-7,-3,7,-3,-8,-4,-7,-6],[4,-5,10,-3,1,6,4,-10,-4,-9,-1,-6,1,3,-1]],[[-6,9,-5,-7,1,2,3,-7,7,6,-2,10,-7,-8,-8],[-1,5,-6,-8,1,-10,-7,9,6,7,5,10,-7,-6,-7],[-5,-9,-8,-3,5,-6,-8,-7,-8,4,6,5,5,-3,9],[5,8,-6,-8,-3,-2,-9,-5,-7,1,10,-3,3,9,6],[6,5,5,10,-10,-6,3,5,4,-1,-5,2,6,-5,3],[-6,-3,3,-2,-9,6,-7,1,-9,5,-9,10,10,9,2],[7,1,9,-5,-6,3,10,-3,1,-7,1,-9,-1,9,-4],[-4,-1,10,8,2,2,6,-5,-4,-2,-5,8,5,2,-9]],[[-7,7,7,-9,-5,-9,-6,8,5,-2,-6,1,10,3,-10],[-10,7,-6,-7,9,7,8,2,-7,-9,-5,5,-8,2,6],[-6,-10,6,-7,-10,-4,4,-2,-9,5,-7,4,6,6,-3],[-9,-1,-4,-4,1,-7,1,-8,-10,-2,-6,3,1,-1,-7],[-3,7,-5,2,-2,-1,9,-2,7,-5,-5,7,10,9,-9],[10,-3,6,6,5,-3,8,-2,-9,2,-7,-7,-9,4,-10],[4,-5,-7,-5,10,-2,8,-5,2,-9,-9,3,1,-5,-10],[10,-7,1,9,-8,5,4,-9,6,-4,-8,-1,1,5,-1]],[[-2,-10,-7,2,8,4,7,-9,-6,10,9,-5,8,-2,-1],[-7,3,2,8,-7,4,-10,-9,9,-3,7,8,-10,-7,9],[-7,-3,-4,2,10,10,1,5,10,-9,-5,-5,-8,9,-1],[-5,7,-9,-4,-4,-10,-6,-6,-3,7,1,8,-2,3,2],[-2,-10,-7,-9,-10,3,9,1,2,-2,-3,8,-9,8,6],[5,8,-4,-4,6,-5,-4,-10,-10,8,-1,6,-4,4,6],[1,5,-7,-4,1,7,-9,-2,7,-1,-5,5,2,8,-1],[-3,8,-2,8,-7,4,-8,-6,-1,-2,7,-3,-1,-4,-10]],[[-3,-7,-4,7,-3,-2,10,-9,10,-1,-10,-4,-3,-9,-3],[-1,-3,-9,-5,10,1,-4,-4,7,-3,-8,7,8,-6,6],[-6,-8,-5,-8,3,10,-10,7,9,7,4,-7,-7,2,3],[-3,-7,10,9,-6,-3,-8,-3,6,1,-6,-7,8,1,9],[2,-3,-4,2,-8,-6,5,6,1,1,-3,8,1,8,-8],[6,-9,-8,1,-6,10,-1,-10,-2,1,4,10,6,10,5],[-8,-5,-9,2,4,-10,4,9,10,-4,7,-5,-1,-10,4],[6,-6,3,-7,5,4,8,-7,-9,-10,-10,-2,4,7,-4]],[[-9,6,-5,-1,3,4,1,3,-8,-7,-7,3,-3,3,-1],[10,9,-5,5,7,-2,-5,-2,3,3,8,8,-9,10,-10],[1,3,7,6,-2,10,-3,-8,-3,5,-2,8,-8,-2,1],[1,3,-5,10,10,2,7,-7,10,-6,8,2,2,2,-8],[6,-8,3,-7,3,-6,-9,10,-8,6,7,-3,-9,-9,-9],[-6,6,3,-5,4,-2,-5,-3,-9,-7,-6,10,-5,6,-9],[-3,-1,-9,10,-7,-2,-5,1,3,-3,-6,9,10,-4,10],[-1,-8,-3,7,1,-10,-4,-1,4,-7,-8,-6,9,-1,-4]],[[6,-5,8,-3,1,-2,8,-7,2,-7,-8,4,-10,-4,3],[3,3,-6,-7,-9,-3,-9,-6,-2,-8,9,-1,-4,5,-3],[5,-10,7,-1,-4,-1,1,8,8,8,-8,-4,2,-2,-5],[7,-5,8,6,-4,-10,-7,-9,-8,6,3,-5,-3,-4,-3],[-1,8,-1,8,8,8,-9,8,-2,2,-4,-4,-1,-3,-3],[5,1,10,2,7,-9,7,-2,3,3,3,-2,6,3,10],[8,-10,9,-8,9,10,-2,6,-3,-7,-6,-4,7,-2,9],[-6,7,5,9,6,3,-8,4,1,4,-4,8,1,-9,-6]],[[4,5,-2,-7,6,-9,-1,3,10,3,-2,8,-6,-7,-1],[3,-9,-5,1,-1,7,-7,6,4,-6,4,7,-9,-9,7],[-3,5,1,2,4,-10,-3,9,-8,5,-3,1,-1,2,9],[9,-2,-4,6,6,1,-3,4,4,-7,4,-10,-8,5,10],[-1,-6,5,7,-7,-5,10,3,-10,-6,7,-4,4,7,-2],[-3,-8,-6,-10,6,8,6,-7,-2,5,1,7,-9,9,-10],[3,-4,4,-3,4,10,1,10,6,-5,9,4,-3,-6,-9],[3,-4,2,-10,-10,4,-8,7,-3,9,3,7,-5,10,-3]],[[2,2,7,-1,9,-3,1,-8,-1,-1,-10,-10,4,7,9],[-7,-10,-4,-3,3,-8,4,10,-10,-2,3,7,-1,9,9],[10,8,4,-6,-10,-8,-7,-6,4,-10,-6,2,-6,-8,-1],[-2,2,-10,5,3,6,2,4,2,5,-8,-5,-6,-1,6],[1,4,2,-10,-9,2,4,1,-3,10,5,1,-6,2,3],[-3,10,8,1,-8,-2,-8,-6,8,1,7,4,7,7,9],[-9,-4,10,-10,-3,3,-3,-4,9,-8,8,6,5,3,-5],[2,5,-7,-2,-5,-7,10,9,-9,-6,9,-4,7,8,-3]]], dtype = "int8")#candidate|4428|(16, 8, 15)|const|int8
bop_4429 = relay.bitwise_and(var_4427.astype('int8'), relay.reshape(const_4428.astype('int8'), relay.shape_of(var_4427))) # shape=(16, 8, 15)
var_4444 = relay.var("var_4444", dtype = "int8", shape = (16, 8, 15))#candidate|4444|(16, 8, 15)|var|int8
bop_4445 = relay.equal(var_4427.astype('bool'), relay.reshape(var_4444.astype('bool'), relay.shape_of(var_4427))) # shape=(16, 8, 15)
output = relay.Tuple([bop_4429,bop_4445,])
output2 = relay.Tuple([bop_4429,bop_4445,])
F = relay.Function([var_4427,var_4444,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_4427,var_4444,], output2)
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
	relay.transform.FuseOps(3),
	relay.transform.DefuseOps(),
	relay.transform.SimplifyExpr(),
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
