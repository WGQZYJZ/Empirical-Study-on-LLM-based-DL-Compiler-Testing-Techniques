import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_421 = relay.var("var_421", dtype = "float32", shape = (7, 2, 9))#candidate|421|(7, 2, 9)|var|float32
uop_422 = relay.asin(var_421.astype('float32')) # shape=(7, 2, 9)
var_427 = relay.var("var_427", dtype = "float32", shape = (7, 2, 9))#candidate|427|(7, 2, 9)|var|float32
bop_428 = relay.subtract(uop_422.astype('int16'), relay.reshape(var_427.astype('int16'), relay.shape_of(uop_422))) # shape=(7, 2, 9)
output = bop_428
output2 = bop_428
func_447 = relay.Function([var_421,var_427,], output)
mod['func_447'] = func_447
mod = relay.transform.InferType()(mod)
mutated_mod['func_447'] = func_447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_447_call = mutated_mod.get_global_var('func_447')
var_449 = relay.var("var_449", dtype = "float32", shape = (7, 2, 9))#candidate|449|(7, 2, 9)|var|float32
var_450 = relay.var("var_450", dtype = "float32", shape = (7, 2, 9))#candidate|450|(7, 2, 9)|var|float32
call_448 = func_447_call(var_449,var_450,)
output = call_448
func_451 = relay.Function([var_449,var_450,], output)
mutated_mod['func_451'] = func_451
mutated_mod = relay.transform.InferType()(mutated_mod)
const_575 = relay.const([[[-7.773714,2.302597,1.882553,5.592865],[-5.765450,-8.256474,3.085076,-9.695601],[-7.497285,5.870013,2.499031,-4.810974]],[[3.819781,-9.973525,4.026709,-9.646024],[-1.618459,0.709225,5.419754,-9.896778],[-8.340555,5.322850,3.115444,-2.910273]],[[-2.431654,3.735583,1.639277,-1.467837],[8.079794,-4.303488,-2.755882,8.062942],[-2.353312,-6.124691,9.332373,7.362652]],[[7.995881,3.599870,-1.008944,7.663347],[1.592585,-3.662602,-9.492217,6.860394],[2.099076,1.729222,-2.980275,2.692251]],[[9.509392,-1.909536,-4.149257,-9.394140],[-4.921331,-1.056222,8.518615,4.922399],[1.568863,3.503470,-0.314642,4.120065]]], dtype = "float64")#candidate|575|(5, 3, 4)|const|float64
var_576 = relay.var("var_576", dtype = "float64", shape = (5, 3, 4))#candidate|576|(5, 3, 4)|var|float64
bop_577 = relay.less(const_575.astype('bool'), relay.reshape(var_576.astype('bool'), relay.shape_of(const_575))) # shape=(5, 3, 4)
func_447_call = mod.get_global_var('func_447')
func_451_call = mutated_mod.get_global_var('func_451')
var_591 = relay.var("var_591", dtype = "float32", shape = (126,))#candidate|591|(126,)|var|float32
call_590 = func_447_call(relay.reshape(var_591.astype('float32'), [7, 2, 9]), relay.reshape(var_591.astype('float32'), [7, 2, 9]), )
call_592 = func_447_call(relay.reshape(var_591.astype('float32'), [7, 2, 9]), relay.reshape(var_591.astype('float32'), [7, 2, 9]), )
uop_595 = relay.tan(const_575.astype('float64')) # shape=(5, 3, 4)
func_447_call = mod.get_global_var('func_447')
func_451_call = mutated_mod.get_global_var('func_451')
call_608 = func_447_call(relay.reshape(var_591.astype('float32'), [7, 2, 9]), relay.reshape(var_591.astype('float32'), [7, 2, 9]), )
call_609 = func_447_call(relay.reshape(var_591.astype('float32'), [7, 2, 9]), relay.reshape(var_591.astype('float32'), [7, 2, 9]), )
output = relay.Tuple([bop_577,call_590,var_591,uop_595,call_608,])
output2 = relay.Tuple([bop_577,call_592,var_591,uop_595,call_609,])
func_618 = relay.Function([var_576,var_591,], output)
mod['func_618'] = func_618
mod = relay.transform.InferType()(mod)
mutated_mod['func_618'] = func_618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_618_call = mutated_mod.get_global_var('func_618')
var_620 = relay.var("var_620", dtype = "float64", shape = (5, 3, 4))#candidate|620|(5, 3, 4)|var|float64
var_621 = relay.var("var_621", dtype = "float32", shape = (126,))#candidate|621|(126,)|var|float32
call_619 = func_618_call(var_620,var_621,)
output = call_619
func_622 = relay.Function([var_620,var_621,], output)
mutated_mod['func_622'] = func_622
mutated_mod = relay.transform.InferType()(mutated_mod)
const_654 = relay.const(1.626400, dtype = "float32")#candidate|654|()|const|float32
var_655 = relay.var("var_655", dtype = "float32", shape = (15, 11, 16))#candidate|655|(15, 11, 16)|var|float32
bop_656 = relay.divide(const_654.astype('float32'), var_655.astype('float32')) # shape=(15, 11, 16)
func_447_call = mod.get_global_var('func_447')
func_451_call = mutated_mod.get_global_var('func_451')
const_661 = relay.const([7.871347,8.022533,1.070499,2.855967,0.286435,5.130179,5.344867,-0.068320,7.340018,-1.953652,7.562077,-2.794468,3.759940,-3.499910,-5.857253,-9.826638,9.235741,7.672645,-2.445327,-3.241184,-9.681821,-4.807719,0.272252,-4.275185,8.373673,1.456914,5.816615,0.904724,1.152643,3.378636,-5.662069,-6.633286,7.368432,-3.037692,-9.550419,1.542990,1.518324,2.772630,-3.573788,5.960314,-9.273891,9.061568,-3.284278,-8.440534,-9.369582,4.380329,0.236368,-9.137306,6.343550,0.337991,3.428859,5.731364,-9.492189,-7.492293,-0.327730,-6.823779,-4.442233,-6.517787,4.309256,2.307993,-6.273580,-1.945255,-0.305913,5.763178,5.010947,9.445995,5.286689,2.108103,4.701346,4.024972,4.233331,-1.849752,1.317145,-1.380741,-0.308536,-1.440711,4.960209,-2.789804,0.281862,2.782803,-8.899549,0.614567,6.901383,7.449126,-6.330876,1.373777,2.523659,-0.884897,-4.177231,3.458600,-5.417617,-9.625666,-6.819032,7.655112,-4.050883,-5.338803,4.268706,-1.044867,0.092168,-2.664899,-1.749892,6.588997,6.568971,-2.499614,4.796590,-7.295074,2.472498,0.597919,-4.266224,2.381510,1.955518,9.090545,-4.255769,-8.439579,-9.910644,4.991631,-4.188378,-2.875267,-6.529660,4.829274,-2.210619,8.140717,-4.710303,2.932976,4.125740,8.933955], dtype = "float32")#candidate|661|(126,)|const|float32
call_660 = func_447_call(relay.reshape(const_661.astype('float32'), [7, 2, 9]), relay.reshape(const_661.astype('float32'), [7, 2, 9]), )
call_662 = func_447_call(relay.reshape(const_661.astype('float32'), [7, 2, 9]), relay.reshape(const_661.astype('float32'), [7, 2, 9]), )
output = relay.Tuple([bop_656,call_660,const_661,])
output2 = relay.Tuple([bop_656,call_662,const_661,])
func_663 = relay.Function([var_655,], output)
mod['func_663'] = func_663
mod = relay.transform.InferType()(mod)
mutated_mod['func_663'] = func_663
mutated_mod = relay.transform.InferType()(mutated_mod)
var_664 = relay.var("var_664", dtype = "float32", shape = (15, 11, 16))#candidate|664|(15, 11, 16)|var|float32
func_663_call = mutated_mod.get_global_var('func_663')
call_665 = func_663_call(var_664)
output = call_665
func_666 = relay.Function([var_664], output)
mutated_mod['func_666'] = func_666
mutated_mod = relay.transform.InferType()(mutated_mod)
var_840 = relay.var("var_840", dtype = "uint64", shape = (16, 11, 13))#candidate|840|(16, 11, 13)|var|uint64
var_841 = relay.var("var_841", dtype = "uint64", shape = (16, 11, 13))#candidate|841|(16, 11, 13)|var|uint64
bop_842 = relay.maximum(var_840.astype('uint64'), relay.reshape(var_841.astype('uint64'), relay.shape_of(var_840))) # shape=(16, 11, 13)
output = bop_842
output2 = bop_842
func_848 = relay.Function([var_840,var_841,], output)
mod['func_848'] = func_848
mod = relay.transform.InferType()(mod)
mutated_mod['func_848'] = func_848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_848_call = mutated_mod.get_global_var('func_848')
var_850 = relay.var("var_850", dtype = "uint64", shape = (16, 11, 13))#candidate|850|(16, 11, 13)|var|uint64
var_851 = relay.var("var_851", dtype = "uint64", shape = (16, 11, 13))#candidate|851|(16, 11, 13)|var|uint64
call_849 = func_848_call(var_850,var_851,)
output = call_849
func_852 = relay.Function([var_850,var_851,], output)
mutated_mod['func_852'] = func_852
mutated_mod = relay.transform.InferType()(mutated_mod)
var_896 = relay.var("var_896", dtype = "float64", shape = (2, 10, 10))#candidate|896|(2, 10, 10)|var|float64
uop_897 = relay.log10(var_896.astype('float64')) # shape=(2, 10, 10)
var_906 = relay.var("var_906", dtype = "float64", shape = (2, 10, 10))#candidate|906|(2, 10, 10)|var|float64
bop_907 = relay.bitwise_xor(uop_897.astype('int16'), relay.reshape(var_906.astype('int16'), relay.shape_of(uop_897))) # shape=(2, 10, 10)
output = relay.Tuple([bop_907,])
output2 = relay.Tuple([bop_907,])
func_910 = relay.Function([var_896,var_906,], output)
mod['func_910'] = func_910
mod = relay.transform.InferType()(mod)
mutated_mod['func_910'] = func_910
mutated_mod = relay.transform.InferType()(mutated_mod)
func_910_call = mutated_mod.get_global_var('func_910')
var_912 = relay.var("var_912", dtype = "float64", shape = (2, 10, 10))#candidate|912|(2, 10, 10)|var|float64
var_913 = relay.var("var_913", dtype = "float64", shape = (2, 10, 10))#candidate|913|(2, 10, 10)|var|float64
call_911 = func_910_call(var_912,var_913,)
output = call_911
func_914 = relay.Function([var_912,var_913,], output)
mutated_mod['func_914'] = func_914
mutated_mod = relay.transform.InferType()(mutated_mod)
var_916 = relay.var("var_916", dtype = "int16", shape = ())#candidate|916|()|var|int16
const_917 = relay.const([[[-1,8,-7,3,-5],[-2,-8,4,-1,-9]],[[-9,5,-6,2,-7],[3,-3,8,-3,9]],[[1,-8,2,-7,10],[-8,-8,2,3,-7]],[[8,8,2,-3,-7],[6,4,9,5,8]],[[1,-4,-9,4,4],[-4,-3,6,-8,-4]],[[-1,-5,4,2,-9],[7,-6,-10,9,9]],[[-7,-6,5,8,10],[10,-2,-8,-10,-8]]], dtype = "int16")#candidate|917|(7, 2, 5)|const|int16
bop_918 = relay.equal(var_916.astype('bool'), const_917.astype('bool')) # shape=(7, 2, 5)
output = relay.Tuple([bop_918,])
output2 = relay.Tuple([bop_918,])
func_921 = relay.Function([var_916,], output)
mod['func_921'] = func_921
mod = relay.transform.InferType()(mod)
var_922 = relay.var("var_922", dtype = "int16", shape = ())#candidate|922|()|var|int16
output = func_921(var_922)
func_923 = relay.Function([var_922], output)
mutated_mod['func_923'] = func_923
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1193 = relay.var("var_1193", dtype = "float64", shape = (11, 7, 2))#candidate|1193|(11, 7, 2)|var|float64
uop_1194 = relay.log2(var_1193.astype('float64')) # shape=(11, 7, 2)
output = uop_1194
output2 = uop_1194
func_1209 = relay.Function([var_1193,], output)
mod['func_1209'] = func_1209
mod = relay.transform.InferType()(mod)
mutated_mod['func_1209'] = func_1209
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1210 = relay.var("var_1210", dtype = "float64", shape = (11, 7, 2))#candidate|1210|(11, 7, 2)|var|float64
func_1209_call = mutated_mod.get_global_var('func_1209')
call_1211 = func_1209_call(var_1210)
output = call_1211
func_1212 = relay.Function([var_1210], output)
mutated_mod['func_1212'] = func_1212
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1769 = relay.const([[[7],[-10],[9],[8],[-6],[2],[2]],[[-8],[4],[-1],[6],[7],[-5],[-8]],[[10],[8],[-1],[2],[6],[7],[-4]]], dtype = "uint32")#candidate|1769|(3, 7, 1)|const|uint32
const_1770 = relay.const([[[-10,-9,3,-9,5,-4,-10,-7,-6,-8,3,-1,10,10,5],[-4,-4,-3,10,6,10,6,-10,2,7,-5,10,7,3,5],[-5,-7,9,6,2,7,-9,1,7,7,3,-4,9,-2,9],[10,-6,4,7,-9,9,-10,-10,-10,-6,2,-1,2,-6,-2],[-4,10,1,9,2,-6,5,-1,-7,-3,10,-2,-10,10,-9],[-4,9,4,7,-10,3,-2,-10,-3,-4,9,2,4,6,-1],[-10,-9,-6,-1,-8,4,6,8,-8,4,7,-7,-7,-2,-9]],[[-7,7,-10,-8,-8,1,-6,7,-5,-6,7,2,-4,-7,9],[3,-4,1,5,-4,-6,4,-2,-5,-6,-5,6,-8,-6,1],[10,-3,-2,8,-4,10,-7,-1,7,-5,-8,-7,8,5,2],[-1,-7,9,-9,-9,-9,-2,-5,-7,-8,7,-3,-8,-10,6],[10,4,-10,-9,10,-1,-8,7,-5,-8,-9,6,-9,-4,7],[1,-7,-5,10,7,3,-10,2,-8,4,-7,1,4,8,-9],[7,-4,-6,3,-4,-7,8,-10,7,-7,-4,-3,-8,4,-4]],[[-10,-2,-9,-3,4,1,-6,1,1,-6,8,-3,-4,7,-4],[1,-5,-8,3,5,1,-1,6,5,-7,-6,-10,5,7,-1],[2,-6,-7,9,10,-9,1,9,1,7,-6,2,-3,9,-8],[2,4,-9,6,3,4,-6,10,-4,-3,9,-5,5,-2,7],[-7,-2,-9,-4,-10,1,-8,9,-6,9,4,-7,2,5,6],[-4,5,6,8,10,-8,2,-10,4,-1,-3,2,4,-4,10],[4,-5,-1,-2,-2,4,3,-3,-6,1,1,-4,6,9,-8]]], dtype = "uint32")#candidate|1770|(3, 7, 15)|const|uint32
bop_1771 = relay.add(const_1769.astype('uint32'), const_1770.astype('uint32')) # shape=(3, 7, 15)
func_618_call = mod.get_global_var('func_618')
func_622_call = mutated_mod.get_global_var('func_622')
const_1781 = relay.const([-9.459280,7.273203,6.401474,-7.758529,-7.390287,-7.046650,6.817568,4.621506,-2.687384,7.533897,-0.034919,-1.576932,0.412625,-5.633066,-0.379079,-4.830049,-6.353556,0.205333,-7.798428,-7.337551,-5.581755,4.503407,9.287045,-0.910759,-7.043111,7.665813,2.362244,4.457114,-4.362092,-7.656428,-1.705728,9.344153,-6.974165,-0.075548,-7.144560,-6.061857,4.678546,-4.592041,-3.986542,3.020664,8.288190,-8.748904,-3.060106,2.104027,1.073501,0.192606,9.850568,-5.192287,3.699394,-1.959692,8.135363,-5.954256,-3.722762,-6.783065,-8.431111,9.053494,-9.110844,-9.379083,8.880579,0.658252], dtype = "float64")#candidate|1781|(60,)|const|float64
const_1782 = relay.const([2.324528,9.281470,-5.523043,6.659750,-1.910723,-4.157583,-9.135901,7.262834,-1.329069,-2.552999,-9.899747,5.459789,5.602245,0.870127,-0.984270,4.894813,-5.848250,-5.719476,-2.889668,8.959211,-1.082457,9.951023,-4.247522,2.885798,4.605672,8.417443,-4.461996,6.944651,7.391364,7.811976,9.358491,9.611771,8.110730,-7.780020,2.684891,-4.114946,5.998718,1.200968,-9.424342,5.097134,-6.805501,-3.601363,3.324299,-8.841695,-1.245878,-3.839921,-4.543111,9.708583,-9.292572,5.957681,0.091460,2.941158,6.773890,-5.839706,2.999031,8.782068,-9.355804,-5.736927,-6.546532,-8.112758,-6.251209,-0.578962,3.515978,-0.258284,0.154435,0.172761,3.607714,7.605218,7.973001,2.171074,8.218261,8.163668,-6.271344,-2.454402,-9.395845,7.301312,4.317836,-6.338202,7.831522,-2.249723,-4.008591,-6.382251,-3.240499,9.675355,9.140535,-9.398874,9.195609,1.996695,-8.532528,-1.347863,-4.859015,5.677774,9.020725,-8.169485,4.344949,6.097336,1.950253,4.054826,-7.590875,5.878353,6.705355,-9.902414,4.927025,-4.725594,2.332663,2.636618,-2.380348,-6.884534,-3.464620,2.033042,8.706924,9.847273,-2.936891,2.203318,6.545207,-2.374872,-9.091707,-9.268059,-6.622149,0.297409,9.609189,-4.323416,-0.567792,-5.875652,3.635015,-4.079980], dtype = "float32")#candidate|1782|(126,)|const|float32
call_1780 = relay.TupleGetItem(func_618_call(relay.reshape(const_1781.astype('float64'), [5, 3, 4]), relay.reshape(const_1782.astype('float32'), [126,]), ), 1)
call_1783 = relay.TupleGetItem(func_622_call(relay.reshape(const_1781.astype('float64'), [5, 3, 4]), relay.reshape(const_1782.astype('float32'), [126,]), ), 1)
func_447_call = mod.get_global_var('func_447')
func_451_call = mutated_mod.get_global_var('func_451')
call_1785 = func_447_call(relay.reshape(const_1782.astype('float32'), [7, 2, 9]), relay.reshape(call_1780.astype('float32'), [7, 2, 9]), )
call_1786 = func_447_call(relay.reshape(const_1782.astype('float32'), [7, 2, 9]), relay.reshape(call_1780.astype('float32'), [7, 2, 9]), )
func_848_call = mod.get_global_var('func_848')
func_852_call = mutated_mod.get_global_var('func_852')
var_1789 = relay.var("var_1789", dtype = "uint64", shape = (2288,))#candidate|1789|(2288,)|var|uint64
call_1788 = func_848_call(relay.reshape(var_1789.astype('uint64'), [16, 11, 13]), relay.reshape(var_1789.astype('uint64'), [16, 11, 13]), )
call_1790 = func_848_call(relay.reshape(var_1789.astype('uint64'), [16, 11, 13]), relay.reshape(var_1789.astype('uint64'), [16, 11, 13]), )
output = relay.Tuple([bop_1771,call_1780,const_1781,const_1782,call_1785,call_1788,var_1789,])
output2 = relay.Tuple([bop_1771,call_1783,const_1781,const_1782,call_1786,call_1790,var_1789,])
func_1796 = relay.Function([var_1789,], output)
mod['func_1796'] = func_1796
mod = relay.transform.InferType()(mod)
mutated_mod['func_1796'] = func_1796
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1797 = relay.var("var_1797", dtype = "uint64", shape = (2288,))#candidate|1797|(2288,)|var|uint64
func_1796_call = mutated_mod.get_global_var('func_1796')
call_1798 = func_1796_call(var_1797)
output = call_1798
func_1799 = relay.Function([var_1797], output)
mutated_mod['func_1799'] = func_1799
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2290 = relay.var("var_2290", dtype = "float64", shape = (7, 14, 2))#candidate|2290|(7, 14, 2)|var|float64
uop_2291 = relay.acosh(var_2290.astype('float64')) # shape=(7, 14, 2)
output = uop_2291
output2 = uop_2291
func_2300 = relay.Function([var_2290,], output)
mod['func_2300'] = func_2300
mod = relay.transform.InferType()(mod)
var_2301 = relay.var("var_2301", dtype = "float64", shape = (7, 14, 2))#candidate|2301|(7, 14, 2)|var|float64
output = func_2300(var_2301)
func_2302 = relay.Function([var_2301], output)
mutated_mod['func_2302'] = func_2302
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2497 = relay.var("var_2497", dtype = "float64", shape = (12, 15, 8))#candidate|2497|(12, 15, 8)|var|float64
uop_2498 = relay.asinh(var_2497.astype('float64')) # shape=(12, 15, 8)
func_618_call = mod.get_global_var('func_618')
func_622_call = mutated_mod.get_global_var('func_622')
const_2510 = relay.const([3.222606,2.486706,-4.464387,9.894249,-5.435903,9.359937,-7.594862,-5.744284,-5.915160,-3.683315,7.217606,-7.980691,-3.560429,5.579327,-5.555865,9.989043,0.275490,-7.660752,-5.498143,-4.669507,-6.161129,4.584022,2.199419,8.554201,-9.226182,2.769798,-8.478930,-4.155828,1.469668,-5.540641,5.548525,4.149890,-1.839443,2.489993,7.332560,1.699934,5.532333,-2.553729,-7.619600,-8.109523,-1.343794,1.128273,6.266025,7.282617,2.580289,6.304921,-5.647741,0.837752,-1.622260,3.310688,-1.652948,2.013755,-7.528378,-7.778494,-0.122068,5.256856,-9.616187,9.978499,-0.294921,-3.599213], dtype = "float64")#candidate|2510|(60,)|const|float64
var_2511 = relay.var("var_2511", dtype = "float32", shape = (126,))#candidate|2511|(126,)|var|float32
call_2509 = relay.TupleGetItem(func_618_call(relay.reshape(const_2510.astype('float64'), [5, 3, 4]), relay.reshape(var_2511.astype('float32'), [126,]), ), 1)
call_2512 = relay.TupleGetItem(func_622_call(relay.reshape(const_2510.astype('float64'), [5, 3, 4]), relay.reshape(var_2511.astype('float32'), [126,]), ), 1)
output = relay.Tuple([uop_2498,call_2509,const_2510,var_2511,])
output2 = relay.Tuple([uop_2498,call_2512,const_2510,var_2511,])
func_2517 = relay.Function([var_2497,var_2511,], output)
mod['func_2517'] = func_2517
mod = relay.transform.InferType()(mod)
mutated_mod['func_2517'] = func_2517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2517_call = mutated_mod.get_global_var('func_2517')
var_2519 = relay.var("var_2519", dtype = "float64", shape = (12, 15, 8))#candidate|2519|(12, 15, 8)|var|float64
var_2520 = relay.var("var_2520", dtype = "float32", shape = (126,))#candidate|2520|(126,)|var|float32
call_2518 = func_2517_call(var_2519,var_2520,)
output = call_2518
func_2521 = relay.Function([var_2519,var_2520,], output)
mutated_mod['func_2521'] = func_2521
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3032 = relay.var("var_3032", dtype = "float64", shape = (4, 3, 6))#candidate|3032|(4, 3, 6)|var|float64
uop_3033 = relay.atan(var_3032.astype('float64')) # shape=(4, 3, 6)
func_848_call = mod.get_global_var('func_848')
func_852_call = mutated_mod.get_global_var('func_852')
var_3037 = relay.var("var_3037", dtype = "uint64", shape = (2288,))#candidate|3037|(2288,)|var|uint64
call_3036 = func_848_call(relay.reshape(var_3037.astype('uint64'), [16, 11, 13]), relay.reshape(var_3037.astype('uint64'), [16, 11, 13]), )
call_3038 = func_848_call(relay.reshape(var_3037.astype('uint64'), [16, 11, 13]), relay.reshape(var_3037.astype('uint64'), [16, 11, 13]), )
output = relay.Tuple([uop_3033,call_3036,var_3037,])
output2 = relay.Tuple([uop_3033,call_3038,var_3037,])
func_3045 = relay.Function([var_3032,var_3037,], output)
mod['func_3045'] = func_3045
mod = relay.transform.InferType()(mod)
var_3046 = relay.var("var_3046", dtype = "float64", shape = (4, 3, 6))#candidate|3046|(4, 3, 6)|var|float64
var_3047 = relay.var("var_3047", dtype = "uint64", shape = (2288,))#candidate|3047|(2288,)|var|uint64
output = func_3045(var_3046,var_3047,)
func_3048 = relay.Function([var_3046,var_3047,], output)
mutated_mod['func_3048'] = func_3048
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3056 = relay.const([[[4,5,1,8],[-8,10,9,2],[-4,4,3,-8],[-6,-9,-6,4],[10,7,9,-7],[-8,8,-10,7],[-9,3,-10,-3],[6,1,9,-1]],[[5,10,-3,1],[-3,9,1,-7],[-6,6,-1,-10],[3,8,-9,10],[-7,7,7,-3],[1,2,-7,-6],[-9,-1,-1,9],[4,-7,6,-6]],[[8,-3,5,3],[-10,-10,6,-2],[-6,7,-3,3],[-2,2,-8,1],[4,-10,1,-7],[-10,10,2,-1],[4,-8,-4,6],[-3,-4,-9,-6]],[[-10,-3,2,4],[6,-8,-5,-7],[-8,-7,7,-8],[4,-1,10,5],[6,3,-8,9],[-10,-4,-7,3],[7,-10,7,-5],[2,5,5,-2]],[[-10,8,1,-3],[6,5,8,1],[-1,-10,-8,1],[-2,2,8,10],[-10,-7,-6,3],[8,5,7,1],[-6,-4,9,4],[2,9,-3,-8]],[[-7,-5,5,-7],[5,9,8,8],[3,10,-9,-3],[2,3,-3,10],[3,-5,3,-1],[3,-2,10,-7],[-4,-4,3,6],[-3,3,-9,6]],[[-10,10,2,-4],[1,-8,-6,1],[3,-4,5,4],[-8,-4,1,9],[-2,5,-2,10],[4,2,6,9],[3,8,5,7],[-8,-10,-2,10]]], dtype = "int16")#candidate|3056|(7, 8, 4)|const|int16
var_3057 = relay.var("var_3057", dtype = "int16", shape = (7, 8, 4))#candidate|3057|(7, 8, 4)|var|int16
bop_3058 = relay.logical_xor(const_3056.astype('int16'), relay.reshape(var_3057.astype('int16'), relay.shape_of(const_3056))) # shape=(7, 8, 4)
func_3045_call = mod.get_global_var('func_3045')
func_3048_call = mutated_mod.get_global_var('func_3048')
const_3067 = relay.const([-3.408092,-8.527159,-4.184963,6.923564,-1.717298,2.347769,-1.505792,7.372821,0.948287,4.943907,-0.400371,4.254013,5.925479,-2.571117,-5.506925,9.242783,-2.149883,-8.302149,7.609242,4.577978,-8.700181,0.567795,-2.255788,0.134201,9.799699,-7.233480,-2.969005,-9.049892,0.397174,-1.270026,-5.653204,-1.533775,7.914684,6.672951,0.592727,-5.136792,0.435005,-9.747921,7.060501,-2.410343,-0.082377,-8.370432,-1.445226,9.965580,1.427325,6.803527,1.726713,-6.559901,-8.812290,-8.033611,4.316382,8.753074,-1.598850,-3.196880,2.217972,8.421373,1.573608,-1.935363,-2.323771,-0.161930,4.195011,4.155643,6.835094,-5.695323,9.780252,2.881954,7.824325,-8.664599,4.673737,8.395822,5.773904,-1.662862], dtype = "float64")#candidate|3067|(72,)|const|float64
var_3068 = relay.var("var_3068", dtype = "uint64", shape = (2288,))#candidate|3068|(2288,)|var|uint64
call_3066 = relay.TupleGetItem(func_3045_call(relay.reshape(const_3067.astype('float64'), [4, 3, 6]), relay.reshape(var_3068.astype('uint64'), [2288,]), ), 0)
call_3069 = relay.TupleGetItem(func_3048_call(relay.reshape(const_3067.astype('float64'), [4, 3, 6]), relay.reshape(var_3068.astype('uint64'), [2288,]), ), 0)
func_618_call = mod.get_global_var('func_618')
func_622_call = mutated_mod.get_global_var('func_622')
var_3079 = relay.var("var_3079", dtype = "float64", shape = (30, 2))#candidate|3079|(30, 2)|var|float64
const_3080 = relay.const([7.006648,7.386242,-5.805657,-1.860209,7.522528,2.472157,6.238447,-9.666776,-9.581730,0.855780,-8.975229,1.665142,4.772544,-6.839360,-1.124237,-6.720706,-5.785717,4.002104,3.816374,-8.922493,-8.818099,3.855218,-6.957797,-0.706015,-7.810612,-8.275486,-4.558705,4.156931,8.013472,-2.938381,0.662303,7.854764,-1.150480,-5.745679,-9.246554,-3.896885,-0.860303,-3.712761,-8.764085,-2.790034,2.360318,3.464236,-1.802147,5.298284,3.862911,9.429756,7.053584,-7.942442,4.879592,1.285514,9.660370,-6.320024,-9.653084,2.300660,-2.690188,4.376083,-3.317919,5.280361,6.649800,-4.650365,-7.588266,5.278589,-0.454688,0.072182,8.478913,5.102235,9.271605,-4.256686,2.103573,-2.965589,5.702935,1.221748,-8.535464,-2.326579,1.708155,-5.783854,5.305232,5.831916,3.315611,0.470659,-4.620766,-2.688162,5.197543,7.943382,-7.528065,-6.286712,1.606983,3.182207,-6.767209,5.706390,7.025744,9.868195,3.778070,-7.671699,5.858224,5.027593,6.254311,3.315170,7.797859,7.589296,-4.234153,7.719758,9.456819,-8.932067,2.198441,8.064956,7.527334,2.312330,-1.105796,-8.040192,4.679743,2.374192,7.031149,9.116933,9.161045,-7.036202,-0.593350,6.354534,-7.993448,4.360775,1.319073,-4.359921,7.075581,3.338353,-6.001419,-4.932563], dtype = "float32")#candidate|3080|(126,)|const|float32
call_3078 = relay.TupleGetItem(func_618_call(relay.reshape(var_3079.astype('float64'), [5, 3, 4]), relay.reshape(const_3080.astype('float32'), [126,]), ), 0)
call_3081 = relay.TupleGetItem(func_622_call(relay.reshape(var_3079.astype('float64'), [5, 3, 4]), relay.reshape(const_3080.astype('float32'), [126,]), ), 0)
output = relay.Tuple([bop_3058,call_3066,const_3067,var_3068,call_3078,var_3079,const_3080,])
output2 = relay.Tuple([bop_3058,call_3069,const_3067,var_3068,call_3081,var_3079,const_3080,])
func_3104 = relay.Function([var_3057,var_3068,var_3079,], output)
mod['func_3104'] = func_3104
mod = relay.transform.InferType()(mod)
var_3105 = relay.var("var_3105", dtype = "int16", shape = (7, 8, 4))#candidate|3105|(7, 8, 4)|var|int16
var_3106 = relay.var("var_3106", dtype = "uint64", shape = (2288,))#candidate|3106|(2288,)|var|uint64
var_3107 = relay.var("var_3107", dtype = "float64", shape = (30, 2))#candidate|3107|(30, 2)|var|float64
output = func_3104(var_3105,var_3106,var_3107,)
func_3108 = relay.Function([var_3105,var_3106,var_3107,], output)
mutated_mod['func_3108'] = func_3108
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3302 = relay.var("var_3302", dtype = "bool", shape = (7, 7, 12))#candidate|3302|(7, 7, 12)|var|bool
const_3303 = relay.const([[[True,True,False,False,True,True,True,True,False,True,True,True],[False,False,True,True,False,False,False,True,True,False,True,True],[False,False,True,False,False,False,False,True,True,True,True,False],[False,False,True,True,True,False,False,True,False,True,True,True],[False,True,False,True,True,True,True,True,False,False,False,False],[False,False,True,False,True,False,False,False,True,False,True,False],[False,True,False,True,True,True,False,True,False,False,False,True]],[[False,True,True,False,False,True,False,False,True,True,False,True],[True,True,True,False,True,False,True,True,True,True,False,False],[False,False,True,False,True,False,True,True,True,False,True,True],[True,True,False,True,False,False,False,True,True,True,False,False],[True,True,False,False,False,False,True,False,True,False,False,False],[False,True,True,False,False,False,True,True,True,True,False,True],[False,False,False,True,True,False,False,False,True,False,True,True]],[[False,False,True,True,False,True,True,True,True,False,True,True],[False,False,False,True,False,True,False,False,True,True,True,True],[True,True,True,True,True,False,False,False,False,False,True,True],[True,True,False,False,True,True,True,False,True,False,True,True],[True,False,True,False,True,True,True,False,False,True,True,False],[True,False,False,False,False,True,True,True,False,True,False,False],[False,True,False,True,True,True,True,False,True,False,True,False]],[[True,False,True,False,True,False,False,True,False,False,True,False],[True,False,False,False,True,False,False,True,True,False,False,True],[True,True,True,True,False,False,True,True,True,False,True,False],[True,True,True,True,True,False,False,True,False,False,True,True],[False,True,False,True,True,True,False,False,False,False,True,False],[False,True,False,True,True,True,False,False,True,True,False,False],[False,False,True,False,False,False,False,False,True,False,True,False]],[[True,False,True,False,False,False,False,False,True,False,False,True],[False,False,True,True,True,True,True,True,True,True,False,True],[True,False,True,True,False,True,True,False,True,False,False,True],[True,False,True,False,True,True,True,True,True,True,False,True],[False,True,False,False,False,False,True,False,False,True,True,True],[False,False,True,True,True,True,False,False,True,True,False,False],[True,False,True,False,True,True,True,True,True,False,True,True]],[[False,True,True,True,False,False,False,False,True,True,True,False],[False,True,False,True,False,False,False,True,False,True,False,True],[True,True,True,False,True,False,True,False,True,True,True,True],[True,True,True,False,False,False,False,False,True,False,True,False],[True,True,True,True,True,True,True,False,True,False,False,False],[False,True,False,False,False,True,True,False,False,True,False,False],[True,True,False,True,True,False,True,False,True,False,False,False]],[[False,True,False,True,True,False,True,True,False,False,True,False],[True,True,False,False,False,True,False,True,False,True,False,True],[True,True,False,False,False,False,True,False,True,True,True,False],[False,False,True,False,False,True,False,False,False,True,False,False],[False,False,True,False,True,False,True,False,True,True,True,True],[True,False,True,False,True,False,False,True,True,False,True,True],[True,False,True,True,True,True,True,True,False,False,True,True]]], dtype = "bool")#candidate|3303|(7, 7, 12)|const|bool
bop_3304 = relay.logical_or(var_3302.astype('bool'), relay.reshape(const_3303.astype('bool'), relay.shape_of(var_3302))) # shape=(7, 7, 12)
func_2517_call = mod.get_global_var('func_2517')
func_2521_call = mutated_mod.get_global_var('func_2521')
const_3309 = relay.const([-0.458527,8.374254,2.807027,7.783439,1.904114,-9.844870,9.196517,-9.415601,-9.526610,-4.352936,7.740374,0.797569,-0.353253,-4.989777,-3.549637,-4.272284,3.506767,6.779166,0.255249,1.119645,-6.665945,8.874309,6.274811,-9.702622,-2.118396,4.375215,4.709762,7.831683,-9.271076,2.097085,-3.728471,4.678557,-2.257817,-0.249368,-1.792199,-8.201485,5.289878,-6.135277,-1.021823,3.111396,1.269288,-8.183986,4.429210,-8.664313,-5.021038,7.647837,8.556121,-2.763178,8.950137,-2.616608,-6.409170,-8.593018,-0.541240,4.766043,1.939689,-2.333726,1.181284,-1.193583,-8.028980,-0.839671,-6.113167,6.642558,-7.811544,6.036092,-8.250210,7.767705,2.374093,9.573540,-8.152914,-0.022659,9.745646,8.946062,2.397634,9.971171,-9.554096,-2.347051,7.323911,7.914097,7.778895,-6.957575,-4.863308,6.285371,6.913073,3.086515,8.147883,-5.859217,-6.746429,0.899657,0.261776,-1.312862,-8.864114,-4.698513,-3.512459,4.711041,0.229283,-2.053535,-0.862084,6.818546,-8.157487,6.334907,-5.887840,-5.300568,4.933892,-8.950817,-2.144988,2.397349,-6.059839,2.462475,5.195209,-7.546047,-1.329373,-7.515970,-9.093440,-8.875671,-1.414253,-9.678009,8.177292,-0.426574,-6.328869,0.186839,8.079927,1.545931,2.211900,-1.802667,-4.771376,5.621848,9.391836,4.089156,4.886072,-9.370662,1.692087,-0.501557,1.669948,-0.822347,4.072147,5.954519,-5.997090,-1.238400,5.340396,-9.762524,-9.536729,-0.268901,4.709543,6.776909,0.061375,-7.484872,7.021152,-6.169549,5.678800,-3.679291,-3.923335,2.061418,7.927494,-5.938076,1.089308,-7.342255,-3.135637,3.428672,-5.503715,-1.583211,7.230629,-1.470896,9.811189,8.113789,5.083454,-0.907742,7.233705,-2.807520,3.143437,7.548866,9.026790,-4.628895,-4.058226,9.022187,8.759402,8.794358,6.907134,3.133227,-8.071038,5.930834,-9.263823,9.298397,-3.236922,-5.224714,2.962914,-0.468650,1.103887,-5.259688,-6.796775,-2.271524,-4.241324,-2.437640,-8.204093,-8.099112,6.227662,-2.838471,4.941371,1.907478,-1.004772,-5.838751,-3.721404,-2.015143,4.932617,0.110343,8.592021,1.411122,3.359660,7.647529,8.550996,-6.156503,9.599945,6.359464,0.673690,-1.552610,-3.348740,9.179930,2.766198,6.100110,-0.944398,4.254108,-0.784953,1.432865,-5.806423,3.547428,1.018539,-6.593413,9.640429,1.625563,5.435670,-2.897872,-0.050538,-0.388800,4.310934,9.633504,-2.952640,4.971189,8.158563,6.371221,9.277185,-2.635034,-1.499836,-6.619462,-7.189179,-6.633508,1.988473,5.683476,-7.845339,-3.922672,8.405007,-2.632918,-4.743381,5.870463,-1.878381,1.606263,1.094402,-5.930904,5.958183,6.395080,7.036208,3.137160,-4.534052,-5.479947,-2.343800,7.654309,-9.216813,2.096581,6.214223,0.487430,0.847730,-3.285178,-7.072255,6.277925,8.672977,7.342456,-9.939448,7.476901,2.949785,-0.352971,-5.618647,-0.665337,4.103861,2.692966,-8.954255,-5.288089,-1.745005,-3.673610,-1.289986,-0.321261,2.529660,-0.386477,-3.235798,-2.652176,9.254421,5.321117,-7.298248,8.592195,6.638713,5.148649,4.357761,-9.773654,-9.406326,-4.972479,-2.130861,-7.400618,-4.842100,3.191731,-8.702234,-8.836539,-4.364744,-5.510823,9.022436,-2.022309,-0.639643,-0.712529,-5.088978,3.269713,-7.221692,5.673605,-0.169392,-2.168507,-5.568817,4.987061,6.222151,-3.490640,1.829854,6.849936,-2.244512,-7.579777,0.397912,-3.701539,3.606988,-5.428386,0.284205,-7.185206,5.886453,-3.692071,-0.759257,-5.254648,-8.042557,-0.295175,2.091154,-5.344770,6.598304,0.859265,-8.572058,-2.097595,8.612064,2.213485,-6.629473,5.469611,-0.523216,9.025787,7.264728,-6.579194,9.448524,-7.248150,-3.921841,-5.036302,5.590965,-7.008765,-3.792925,7.632309,2.546691,-2.868930,-2.453409,2.080330,-7.624370,6.645079,8.812738,0.486932,-0.918542,7.861712,-8.916943,9.577389,6.503902,9.224819,-7.088356,-3.243206,5.306817,-5.107905,-9.331078,-7.494254,-4.386616,-4.501036,-7.535555,-4.534672,4.989451,6.470606,-3.245850,0.764084,0.866336,7.590392,6.512375,4.284264,-2.372799,-6.076783,-5.856634,7.956642,9.501958,-4.614572,9.833054,-6.839304,-4.843487,5.304254,-3.909982,4.579408,9.433360,-6.303804,-0.688762,-1.279586,6.289173,5.456948,7.715209,-0.916723,-7.047443,-2.856718,-1.861590,8.824451,1.784024,1.635715,7.359438,9.248577,1.076715,-3.373283,3.768259,-1.698860,9.740689,-7.138118,0.127888,8.423600,9.768728,3.225507,3.486633,0.263719,1.003698,-3.927173,7.845653,-6.474913,2.510925,-3.439443,1.150026,9.842487,-3.607924,7.254139,1.010230,8.676260,4.171383,-2.705196,4.202844,2.093169,-6.438820,-5.898468,9.735790,-4.326685,9.084619,3.155620,1.716157,5.712998,7.361849,2.664558,-1.617002,8.178927,-9.656393,-4.305282,1.595346,-4.960745,2.130914,7.894645,8.237619,-7.539863,-9.220387,9.636795,-2.729650,8.778044,-9.295691,-9.576977,-0.298602,-6.732701,5.489500,-8.997129,-2.766637,-7.367530,3.350165,-6.000583,2.877456,3.651968,-5.735302,-5.121995,-5.640471,-8.086481,-3.719478,8.930109,4.841913,4.770880,-1.921611,3.158279,1.644621,-7.749066,-7.105543,9.467673,7.778116,8.103584,-5.278315,8.318878,-3.422716,8.884174,-7.117907,0.610668,-4.286372,5.410374,-6.636966,5.669207,-2.150582,7.553523,-9.668615,6.693598,7.378035,7.927051,-0.250862,-5.221869,9.385548,2.162453,-8.745875,5.825849,-9.363344,6.333853,5.291972,-3.900373,7.744374,-1.527492,-2.939561,1.552408,9.694113,9.716462,1.071802,-8.122075,0.093826,3.580040,-7.896141,-2.865780,4.339959,5.370203,-8.507459,-8.240910,6.950232,9.852618,-3.213373,-2.412289,-4.931221,0.803222,4.485863,-6.519603,-6.755157,3.005410,-0.923301,0.682908,8.359046,-2.765076,-2.314905,0.355536,-7.420973,8.753948,-9.589288,-4.604768,-4.997020,-3.668023,5.616177,-7.260205,-0.627875,-8.291298,-9.982298,-7.163112,-1.302412,7.967418,-7.517480,9.386138,-1.805088,4.390486,-3.612417,2.189854,-8.708908,-3.753287,-7.412015,6.637463,-4.215921,6.059048,6.488806,7.374076,-5.269554,-5.575602,3.308102,2.448194,-7.779086,-2.804080,-7.232527,0.177276,-2.639689,-7.069265,7.431021,3.698631,0.462916,-1.161562,8.874370,9.206250,-2.910422,-3.833751,8.616674,9.164414,-6.003027,-3.649680,2.910098,1.108504,3.229341,-0.732319,2.401208,3.587244,-4.429111,4.405977,4.022514,-3.328306,-5.979292,4.879002,-1.244072,-3.908258,8.221549,-0.363606,-0.135391,-0.928210,0.266397,-3.925606,-1.192537,-1.566307,3.827821,-3.545699,-7.629816,1.227513,7.977451,-8.652847,2.315343,1.017890,2.370702,-0.221493,1.354219,7.809238,3.916496,-6.247177,1.334579,4.984519,-3.279892,0.150370,-5.082406,-0.308286,-1.829807,0.794582,1.238685,-5.042242,-9.606436,-5.068766,2.056592,6.720437,-8.725633,-8.709401,-8.746726,-1.682681,-3.506437,9.367600,-7.315406,-2.641713,-7.165158,3.624327,-6.269922,-6.361874,-3.418861,3.134726,-5.928147,-1.501856,-4.166256,7.176762,-7.001630,8.870214,4.419381,1.472552,-6.882007,-3.455602,-3.790356,-7.701919,2.794208,8.335320,-8.283247,8.868838,4.981428,9.732213,5.348650,-9.717477,-7.729688,-5.809258,-8.583466,-7.729082,3.468978,4.424406,-1.469107,8.972343,-5.567248,2.745239,3.991134,-0.702310,-1.775495,-7.058874,-0.598883,-2.582729,-4.339469,-9.112162,-0.224026,-6.221708,-6.854020,8.746955,6.844965,-7.503067,-4.702091,-6.182611,9.136575,-6.752512,-6.912850,1.125332,-5.974534,-6.035076,-1.283959,3.034371,6.209840,-8.781565,-1.571180,-6.403788,-1.984545,0.146096,-7.340638,-7.326910,-0.394861,6.691274,6.481112,9.779827,-7.657045,5.522455,6.248649,-6.471905,-2.857970,-7.571873,-1.874068,-5.131262,6.853934,9.437223,-6.998131,2.763415,3.850447,6.992003,5.027601,-7.422218,-3.312711,-2.638444,-9.045728,-4.477108,-4.233721,6.398289,8.944078,5.299830,-3.947789,-8.557072,4.360952,0.418400,3.435337,6.328188,-3.020385,-9.953967,0.311683,-9.186330,4.745457,-3.729080,8.011427,2.156952,-3.141111,2.551468,2.761731,0.527995,-0.533725,3.978549,8.956850,-1.342358,-2.144368,1.190363,-2.469591,-6.461412,-1.844937,7.533369,-5.410687,1.243249,7.644430,2.898026,-4.874839,6.086149,-3.875134,-6.317982,-9.041121,3.945437,-6.285720,-5.316395,-1.174445,-5.119258,-0.743687,-0.872926,-9.018833,1.121151,-9.811771,5.625615,7.457120,9.059478,4.814281,4.316633,6.997067,1.113614,2.864254,-7.111533,-7.344371,2.230737,-5.570701,8.091143,6.144568,-1.708801,-4.510408,-0.923419,4.137320,5.195812,-6.369069,-9.623424,7.972771,9.521832,6.037320,-6.552217,-1.427560,-2.076079,8.910274,-8.324170,-5.196495,-5.965463,-6.173151,-9.928466,6.551289,-5.575120,4.367998,4.033160,-3.307936,4.315209,-2.363775,3.829531,8.308705,4.436719,-8.026336,6.142897,-2.873007,2.795010,0.314829,-3.775019,7.735650,-9.263956,6.705785,3.050135,-4.669589,-9.215125,-5.454788,1.828628,3.341788,-3.642387,-1.971107,1.858287,1.407465,5.836244,-9.052563,9.604568,4.031170,-9.455631,7.529055,-4.390980,1.336928,-9.462736,4.261556,0.924313,-9.152709,-9.454210,-9.353768,-9.628549,-5.579355,-5.735344,1.644121,-6.915331,0.994690,-8.613306,-1.639410,-8.694261,1.872115,5.828294,-0.498934,8.570262,-8.879972,-5.372612,3.702589,-9.282375,-4.838679,3.521189,4.661349,-6.595675,-2.121570,2.318227,-5.554744,-3.359865,4.185135,-7.696316,8.203665,-2.607894,4.788913,-7.875610,3.486022,-8.649024,0.126185,-6.782210,5.579534,3.580911,4.257297,-1.367009,-3.988324,2.951703,-1.627008,6.734841,9.976035,8.825517,-4.356198,-3.686532,-9.746348,-4.651339,-6.076633,-6.199584,2.263425,7.050942,3.519882,-1.107270,8.422222,1.084387,8.346608,4.223109,-4.838473,1.177635,-9.217179,7.350869,-7.681345,-7.946603,-6.050513,-2.563865,-5.024477,-2.986980,2.544405,2.745004,-8.017084,-8.050574,7.404702,-8.417589,-9.510638,7.743475,6.193754,-1.798195,-4.072872,-2.164724,2.717880,-5.868468,0.602145,6.803563,-5.927689,6.005285,5.282445,-1.938116,0.454165,5.283560,8.878545,-6.206628,3.158698,-5.657537,7.523105,-8.496730,-3.424800,-6.177794,4.772587,-5.786685,-1.084798,-5.082918,-2.342627,-8.516672,4.139955,2.087719,-6.298835,-4.784525,-4.417999,3.310127,0.633470,9.320404,7.131018,9.660807,7.303471,-8.160507,8.286295,-5.778375,7.880879,2.234721,-1.862036,7.611758,-2.585944,-6.888399,8.790482,-4.593692,6.255400,-2.950251,1.978709,7.175491,3.577381,-1.195129,-8.837827,-0.917667,-3.494374,-6.488788,3.344171,2.920866,1.238734,-6.182276,-4.125497,-9.642182,-7.500157,-4.871174,-4.145628,4.055041,9.374634,5.698305,-0.810382,3.952011,5.860242,8.706608,-5.614917,2.297074,-8.877517,-5.452324,-4.859309,-5.345147,9.906521,3.930384,-3.078190,0.597961,-8.820413,9.353782,2.837452,3.941395,-1.869359,5.529472,-3.058637,5.090092,-0.251564,7.711129,-4.758465,-1.919862,-0.554984,6.048481,-6.128449,-4.394182,5.553268,6.806140,-5.406945,-5.789977,2.505510,4.384549,-4.993290,-0.603731,-3.932871,5.650895,7.054576,-0.758585,9.598966,-4.441571,3.486611,1.009075,-1.394930,6.314087,5.307540,4.086385,4.420865,-9.653353,9.046493,-9.545184,-9.615332,-0.456364,8.329751,4.730408,2.343642,-3.732142,-2.950482,6.980841,-6.725191,-6.111740,-4.085113,-2.694594,-9.742712,2.645365,8.305804,-4.413837,-4.213020,5.483541,0.344431,-0.102208,-2.493628,1.652689,-4.595025,4.927744,0.396616,4.250119,-1.122826,8.401135,-0.314059,-5.730834,5.507073,-1.159916,-1.795978,3.585740,-6.660859,-8.432860,8.649882,-6.383186,-7.909461,-6.503961,1.423562,-4.677485,-8.492827,-4.440945,-5.452536,-1.692427,3.406976,2.026965,2.687843,-9.215847,9.840251,-9.808135,-8.414190,-2.544667,9.247430,4.174604,-1.691417,-3.595155,3.698272,-4.936909,5.955619,9.527956,5.641528,-0.436220,-2.862470,-8.303429,9.339310,-3.226797,4.767164,8.597571,5.745105,5.550989,-7.817749,-3.828162,9.807732,8.618450,-4.360458,6.242008,-7.310583,-8.954033,-4.881081,-3.287242,3.249536,-5.158690,2.043760,3.804611,-9.797338,5.356250,-7.221602,-1.661338,-7.807201,9.214953,6.758387,-5.484906,-3.102811,-3.999489,5.925816,5.844417,8.796237,-5.305019,7.859211,0.151017,-2.142667,-3.693515,1.673297,-2.507564,-7.322833,-7.106595,5.053318,0.036860,1.264956,-4.840516,-4.569177,8.292743,6.846570,2.928004,-1.033075,-3.866741,3.995489,8.282837,-0.237784,-0.966600,4.816461,-2.320839,8.055552,2.508696,0.235989,5.971268,5.482884,6.198217,-1.234458,8.281378,2.601386,-6.544525,-3.579477,5.701778,1.180212,6.639282,-8.523391,9.642260,-0.288893,-9.307249,1.006516,7.797898,2.475515,9.699950,3.288241,-3.856374,4.742812,1.623695,-2.325534,-0.801709,-8.109094,0.729894,2.279989,-8.474860,4.807101,7.654474,4.865671,7.599660,3.408708,-5.887378,1.026199,6.387336,5.021136,-5.545816,-8.330048,-6.189217,-9.852249,0.382070,-8.787004,5.002320,3.773027,-7.610169,-8.839740,2.514723,9.801264,-2.393290,-7.280957,7.324645,7.332288,0.672411,-3.832370,-7.708548,0.850590,-9.579201,-0.450772,1.348783,-3.137745,-4.946299,9.864419,-4.395180,2.935887,7.686473,-9.910633,-4.117454,-5.730915,3.361001,8.203163,-3.699795,-1.770787,-8.701591,-4.072664,-2.791513,-8.844477,4.130562,-1.844571,-6.027852,3.499821,6.725480,-5.918800,6.683611,5.533307,5.774789,-2.067144,-2.876249,-2.827230,3.262091,-7.867644,8.964791,-7.769383,0.942653,-9.492400,0.631138,1.788659,9.975300,-8.471842,8.394911,-2.578071,-0.484015,-0.964098,8.684446,4.307827,5.368263,-1.823845,-6.231341,-0.153579,9.509286,4.606456,-2.783013,4.972360,-1.362512,-5.701975,3.221506,-2.539587,4.689077,-6.027195,0.441991,-4.256395,-8.097929,4.534188,4.442442,-7.505983,-5.586676,1.161479,-6.255075,5.719014,-4.843608,-4.567772,-6.362697,3.205022,9.753757,-2.816777,-1.898069,-4.018753,0.641048,1.902894,8.301717,6.726632,-5.019028,-5.830523,3.527058,7.107724,9.451055,8.176663,9.362316,4.286369,5.327019,4.882705,-5.562216,-1.060170,-1.050641,2.992271,6.469987,2.616206,9.939917,-6.640858,4.000698,3.737034,-8.208086,-4.237714,2.152976,-8.920652,0.762983,-1.578595,1.923508,7.394429,9.029234,7.043192,7.437736,-8.436273,-7.875836,7.827592,-8.274745,-6.073028,-0.783615,-6.142557,3.485730,-3.049911,4.942785,-8.225524,2.850124,-5.984662,-8.798347,5.491344,-0.289618,7.798980,-4.611250,6.591251,2.633881,8.110050,-3.158756,7.923204,8.864439,5.312126,0.022786,5.147737,2.497731,0.004781,-5.342827,-1.594798,-8.766043,9.186003,-7.723954,7.282097,7.390609,3.404576,3.120201,8.485272,-0.127667,9.216504,-7.350016,-7.517261,-5.455032,-4.234852,-6.730513,4.105296,-5.798187,-2.330792,9.492614], dtype = "float64")#candidate|3309|(1440,)|const|float64
var_3310 = relay.var("var_3310", dtype = "float32", shape = (126, 1))#candidate|3310|(126, 1)|var|float32
call_3308 = relay.TupleGetItem(func_2517_call(relay.reshape(const_3309.astype('float64'), [12, 15, 8]), relay.reshape(var_3310.astype('float32'), [126,]), ), 1)
call_3311 = relay.TupleGetItem(func_2521_call(relay.reshape(const_3309.astype('float64'), [12, 15, 8]), relay.reshape(var_3310.astype('float32'), [126,]), ), 1)
func_848_call = mod.get_global_var('func_848')
func_852_call = mutated_mod.get_global_var('func_852')
const_3313 = relay.const([[-7],[-6],[-1],[-10],[-10],[-4],[-8],[8],[3],[9],[-4],[6],[-3],[4],[-8],[-7],[-9],[-4],[1],[3],[-6],[10],[3],[4],[-1],[-5],[-1],[10],[-9],[-9],[3],[2],[10],[10],[-9],[-5],[-9],[1],[-3],[7],[-7],[1],[-1],[-3],[-7],[9],[-8],[-2],[6],[-10],[-5],[10],[-9],[8],[-7],[8],[-5],[-3],[1],[-9],[8],[-10],[9],[-5],[-4],[-2],[7],[4],[6],[-8],[7],[8],[-4],[-2],[-6],[-3],[9],[1],[5],[-6],[10],[-9],[1],[-2],[7],[9],[-7],[-10],[7],[8],[-3],[10],[-6],[3],[-8],[2],[7],[4],[7],[5],[8],[-2],[1],[10],[3],[3],[-2],[-1],[5],[-2],[5],[8],[5],[9],[10],[10],[8],[-4],[3],[6],[3],[6],[-2],[4],[1],[10],[-9],[-7],[2],[8],[4],[9],[9],[10],[9],[-2],[7],[10],[4],[-7],[-9],[2],[-5],[4],[-7],[-7],[-2],[2],[2],[-5],[-1],[-5],[-4],[-6],[-10],[-3],[9],[-9],[-4],[-2],[-7],[1],[-7],[-3],[6],[10],[-5],[-6],[2],[7],[-6],[-1],[8],[1],[-2],[5],[4],[-9],[1],[-10],[9],[6],[6],[5],[5],[-10],[-6],[8],[-10],[6],[-4],[1],[8],[-8],[3],[-8],[7],[8],[-8],[-3],[-7],[-4],[3],[-7],[-2],[7],[5],[-3],[10],[-2],[1],[-5],[3],[-4],[-6],[-4],[10],[-6],[-1],[-8],[-7],[1],[6],[4],[9],[-1],[5],[-9],[-9],[3],[-9],[-10],[6],[-4],[8],[-2],[-10],[6],[-8],[4],[-6],[8],[-8],[4],[-1],[5],[-4],[3],[-1],[-7],[-2],[6],[3],[-7],[-2],[-10],[3],[4],[6],[-1],[6],[9],[10],[-10],[-8],[10],[7],[1],[7],[10],[-9],[2],[10],[-5],[7],[-3],[1],[5],[-3],[-2],[3],[10],[-7],[-9],[-7],[6],[1],[9],[-5],[8],[-2],[4],[-3],[7],[-3],[7],[-1],[5],[8],[-4],[5],[2],[-9],[7],[-5],[5],[8],[-1],[8],[8],[-6],[-9],[-2],[7],[-10],[-6],[1],[1],[8],[4],[-7],[-1],[10],[-5],[-1],[-2],[-10],[4],[-7],[3],[-1],[4],[-4],[2],[5],[7],[8],[-6],[-1],[9],[-5],[-7],[-5],[-8],[-3],[2],[7],[-6],[1],[5],[5],[-9],[-10],[-3],[7],[1],[4],[7],[-2],[-2],[6],[-8],[9],[6],[-1],[9],[4],[1],[2],[-5],[6],[1],[7],[-9],[-4],[3],[-4],[5],[-3],[5],[-3],[-2],[-2],[-3],[8],[5],[7],[6],[-5],[2],[-6],[1],[5],[5],[-8],[-4],[5],[-2],[-8],[1],[-4],[-10],[4],[4],[10],[1],[10],[-8],[-10],[3],[-1],[3],[-10],[5],[9],[-5],[-4],[-3],[-2],[-8],[-2],[10],[2],[4],[-9],[2],[-3],[-10],[-1],[2],[2],[-4],[-4],[-3],[-3],[-1],[-9],[-4],[9],[5],[-7],[1],[-3],[3],[-5],[3],[-4],[-2],[-3],[7],[7],[10],[10],[-8],[-3],[8],[1],[10],[-10],[7],[9],[1],[-8],[-4],[-7],[8],[10],[1],[-5],[-1],[-2],[-8],[8],[-7],[2],[2],[-6],[5],[-5],[7],[-9],[-5],[7],[10],[-4],[10],[-10],[9],[10],[-4],[7],[-4],[-10],[-9],[7],[6],[-2],[-6],[8],[-3],[-7],[-8],[-3],[4],[-10],[6],[6],[-4],[-8],[-1],[8],[-10],[8],[-1],[3],[9],[-9],[8],[-6],[7],[-3],[-5],[2],[7],[-2],[-4],[4],[3],[1],[-10],[-10],[-6],[-8],[10],[7],[9],[-10],[-8],[4],[2],[-4],[6],[-2],[1],[5],[-8],[10],[1],[-10],[-9],[-10],[-8],[-3],[-3],[-4],[4],[-3],[7],[9],[9],[-9],[6],[-4],[-9],[-10],[3],[9],[10],[-8],[10],[2],[-9],[4],[2],[-5],[-7],[7],[6],[-2],[6],[-5],[4],[10],[7],[-1],[-1],[3],[-9],[7],[-10],[10],[7],[-1],[-1],[-9],[-5],[-5],[10],[4],[-5],[-8],[-7],[-8],[6],[6],[10],[-1],[5],[1],[5],[2],[6],[-10],[7],[8],[1],[10],[-5],[-4],[6],[6],[8],[-4],[-1],[9],[-4],[-7],[-2],[-1],[-3],[1],[-4],[-1],[9],[-1],[5],[-2],[7],[8],[-10],[-6],[-9],[9],[2],[-10],[-8],[10],[-2],[-1],[8],[8],[1],[8],[6],[8],[2],[4],[-10],[5],[-2],[8],[6],[2],[-1],[-6],[6],[4],[-6],[5],[-6],[-9],[10],[-2],[-6],[-2],[-9],[-6],[10],[-10],[-4],[-2],[4],[8],[-6],[-1],[-10],[3],[-6],[8],[-1],[10],[-1],[-7],[-6],[-4],[5],[1],[-1],[9],[-3],[-4],[-3],[-1],[-3],[10],[-9],[5],[7],[-3],[-9],[3],[4],[-3],[-4],[4],[3],[8],[-6],[-4],[8],[-4],[4],[-9],[9],[6],[-8],[2],[-5],[-6],[-9],[4],[-8],[-7],[-3],[-5],[7],[-2],[-7],[4],[10],[6],[10],[-9],[-2],[4],[5],[3],[-4],[10],[-3],[2],[4],[-3],[-2],[9],[-10],[1],[2],[7],[-5],[7],[-2],[-3],[-3],[4],[10],[8],[-10],[7],[9],[-4],[-2],[8],[-5],[9],[-7],[9],[-9],[6],[5],[-7],[-7],[-1],[5],[9],[-3],[-2],[-9],[8],[-7],[-3],[-3],[4],[7],[1],[-1],[9],[3],[-5],[5],[4],[-6],[-2],[9],[9],[6],[8],[6],[-9],[-3],[5],[1],[4],[-3],[4],[-4],[7],[-7],[6],[-8],[9],[9],[-3],[-3],[-8],[-5],[10],[8],[-9],[4],[8],[-6],[-7],[3],[-8],[-8],[-6],[8],[4],[2],[-8],[6],[2],[-4],[6],[6],[6],[-10],[-2],[8],[-5],[-9],[-5],[-10],[8],[2],[10],[4],[3],[-3],[-7],[-2],[9],[-10],[4],[-3],[8],[10],[8],[-4],[-2],[2],[4],[4],[-5],[-4],[-3],[9],[-8],[-7],[9],[-1],[-3],[-10],[-9],[-9],[1],[-4],[9],[-10],[-4],[9],[3],[-3],[9],[3],[-1],[4],[-3],[7],[1],[4],[-7],[-4],[-8],[-1],[9],[4],[-1],[2],[7],[7],[10],[-2],[-10],[-7],[-4],[10],[3],[8],[-8],[-6],[2],[-10],[-6],[-3],[10],[1],[-3],[-6],[-1],[-1],[-6],[-8],[5],[-10],[6],[10],[5],[1],[4],[4],[-3],[-5],[5],[9],[-4],[3],[-3],[9],[-7],[-1],[-7],[1],[10],[-3],[3],[8],[10],[4],[5],[-5],[6],[-9],[7],[7],[10],[-6],[-8],[1],[8],[-4],[-1],[9],[-6],[-1],[6],[7],[4],[-1],[5],[6],[5],[-2],[-9],[-2],[-7],[10],[-9],[-1],[1],[3],[8],[1],[8],[-2],[9],[10],[-7],[6],[-7],[5],[-5],[2],[-5],[8],[-5],[-5],[-2],[2],[8],[7],[-1],[1],[1],[-6],[-8],[-10],[7],[8],[7],[9],[-8],[4],[3],[-4],[-1],[10],[9],[-9],[-1],[-7],[-7],[5],[-3],[9],[-10],[1],[-5],[1],[-2],[-10],[-7],[-6],[-4],[-7],[2],[-7],[4],[-7],[4],[4],[-4],[-5],[9],[-8],[-1],[5],[-1],[-6],[-6],[1],[8],[-8],[-9],[-7],[1],[-8],[-6],[4],[8],[-8],[2],[-9],[-4],[7],[10],[9],[7],[8],[2],[-2],[9],[-8],[4],[-2],[-5],[3],[6],[8],[9],[-2],[-7],[-6],[-8],[-2],[-10],[-5],[-6],[-3],[6],[1],[8],[7],[-8],[-3],[-4],[5],[-6],[8],[5],[-6],[6],[-3],[-4],[-1],[4],[2],[-7],[-5],[7],[1],[5],[-3],[-5],[4],[-10],[-5],[2],[7],[8],[6],[1],[5],[10],[3],[2],[-9],[10],[-5],[-10],[4],[-9],[-6],[-1],[-7],[-10],[-5],[5],[-9],[2],[2],[-5],[-10],[-10],[9],[5],[-2],[6],[-7],[1],[-8],[-9],[4],[-2],[6],[-6],[-9],[-9],[8],[-3],[-3],[-2],[-5],[3],[7],[-4],[-4],[9],[6],[10],[9],[-2],[9],[-7],[-3],[1],[9],[1],[4],[-5],[-5],[-8],[-3],[-7],[-10],[3],[-5],[8],[-6],[-8],[-5],[5],[4],[9],[-9],[1],[-3],[-4],[-7],[5],[10],[-7],[-3],[-8],[9],[-10],[-6],[-8],[2],[-10],[-2],[-6],[3],[-3],[-3],[-10],[-8],[-7],[-3],[2],[10],[6],[-6],[8],[-4],[10],[1],[-2],[7],[7],[-4],[2],[-3],[3],[-3],[-9],[6],[1],[-2],[1],[-7],[-1],[-8],[-5],[8],[3],[-6],[-6],[-4],[-8],[-3],[-2],[-2],[2],[-1],[-1],[5],[-9],[7],[-5],[3],[-7],[-3],[-1],[-1],[5],[-5],[6],[1],[-3],[-2],[-3],[8],[-9],[3],[10],[-4],[-8],[-9],[3],[7],[7],[-7],[9],[-10],[10],[-9],[-6],[-2],[-10],[10],[4],[6],[-10],[-10],[-6],[-3],[9],[5],[-5],[2],[-4],[8],[-6],[6],[9],[7],[-10],[7],[9],[-3],[6],[-7],[5],[5],[-6],[7],[10],[1],[-10],[-3],[2],[4],[4],[-2],[-1],[-7],[10],[-2],[-7],[-6],[5],[-2],[-1],[-2],[-1],[-9],[6],[7],[-7],[10],[-3],[-2],[2],[-7],[-2],[3],[-8],[-4],[-9],[1],[-3],[5],[6],[-9],[10],[-8],[8],[-7],[6],[1],[-8],[-7],[9],[-7],[-10],[-8],[-1],[-2],[6],[9],[-1],[-10],[-8],[9],[-10],[-2],[-5],[5],[2],[10],[-2],[-7],[-3],[9],[10],[-7],[4],[-2],[-2],[-6],[1],[1],[1],[-10],[9],[7],[10],[4],[4],[-5],[9],[7],[-9],[8],[10],[-4],[-6],[-7],[-2],[-9],[8],[-4],[-1],[4],[-2],[-10],[-2],[8],[4],[3],[-2],[4],[-3],[-2],[-9],[7],[1],[6],[10],[5],[-8],[4],[-2],[1],[8],[9],[-10],[-7],[-6],[-7],[-2],[-4],[6],[4],[9],[-9],[-6],[7],[7],[3],[10],[7],[-5],[-3],[3],[-7],[4],[9],[1],[-7],[3],[-5],[3],[5],[10],[7],[-10],[-1],[9],[5],[6],[9],[5],[-10],[-9],[5],[3],[1],[4],[7],[-3],[-7],[9],[7],[4],[1],[6],[-9],[-10],[-7],[6],[-3],[4],[6],[-9],[3],[7],[7],[7],[-5],[-6],[2],[10],[4],[10],[9],[3],[-4],[5],[4],[-3],[9],[6],[6],[-10],[6],[-1],[9],[-8],[1],[4],[4],[1],[6],[-10],[-3],[-5],[4],[8],[5],[-3],[3],[9],[-5],[-7],[-7],[-6],[2],[-10],[7],[-7],[4],[-5],[-3],[10],[-1],[1],[9],[10],[-9],[2],[-9],[8],[10],[-8],[-10],[9],[6],[4],[-7],[1],[9],[3],[-4],[-2],[9],[-10],[2],[8],[7],[-9],[2],[3],[-2],[-9],[-3],[-4],[-4],[10],[10],[-10],[6],[5],[-5],[-10],[-10],[1],[8],[10],[-3],[6],[1],[10],[-9],[-3],[2],[7],[-1],[-6],[9],[1],[8],[3],[-6],[-4],[4],[-8],[-4],[-2],[9],[-3],[7],[1],[-4],[6],[-4],[5],[9],[-7],[-3],[-5],[-3],[-3],[3],[9],[1],[5],[1],[7],[2],[9],[10],[-9],[3],[5],[7],[4],[7],[6],[-5],[2],[-4],[-3],[10],[10],[-3],[9],[6],[4],[3],[7],[3],[9],[-9],[8],[9],[-9],[4],[10],[1],[-9],[3],[-8],[7],[8],[3],[-10],[-7],[6],[4],[-9],[3],[-8],[9],[4],[-7],[4],[10],[-9],[-6],[-9],[-2],[-7],[9],[-4],[-9],[-8],[8],[-1],[1],[7],[-6],[-8],[-5],[-7],[3],[3],[-4],[4],[-6],[-8],[9],[9],[-9],[6],[-6],[10],[8],[-10],[4],[-5],[3],[2],[-10],[3],[-5],[3],[7],[3],[2],[10],[4],[2],[9],[-6],[-1],[-1],[9],[-6],[-10],[-7],[1],[10],[3],[8],[5],[-5],[-9],[3],[-9],[10],[-10],[-6],[6],[9],[10],[2],[-7],[-1],[-6],[-8],[-6],[-1],[2],[-2],[3],[-2],[-5],[-1],[10],[-7],[-6],[-2],[-1],[-3],[-10],[9],[-6],[1],[-4],[-10],[7],[7],[10],[-4],[-8],[9],[-2],[-8],[3],[-4],[-4],[1],[3],[9],[-6],[-6],[1],[-8],[-3],[-9],[3],[-6],[-10],[10],[8],[6],[-8],[6],[-10],[-1],[-4],[-1],[10],[5],[-10],[-4],[-6],[-10],[7],[-10],[5],[-6],[3],[-4],[-7],[-9],[-2],[9],[8],[3],[10],[-2],[10],[-3],[-5],[9],[-10],[-5],[-9],[8],[-6],[10],[-7],[-7],[-2],[-4],[-10],[1],[2],[4],[-8],[7],[9],[3],[-3],[-7],[-7],[-6],[-5],[1],[3],[-2],[-6],[2],[8],[3],[-10],[5],[4],[-1],[-10],[7],[-5],[-4],[-4],[-10],[4],[4],[6],[6],[-2],[3],[3],[3],[-8],[6],[3],[7],[-4],[10],[8],[9],[-3],[-2],[8],[4],[-8],[4],[-7],[-9],[-3],[2],[8],[-6],[10],[2],[-6],[-2],[3],[8],[1],[-1],[-1],[10],[-4],[-10],[6],[5],[-3],[6],[-8],[3],[-9],[-3],[-8],[-4],[-4],[-2],[2],[10],[3],[-4],[-4],[-2],[-1],[10],[7],[5],[10],[-10],[10],[-9],[-1],[-1],[5],[2],[3],[-6],[7],[6],[8],[-9],[-1],[3],[-2],[-2],[-9],[9],[4],[-6],[1],[-6],[3],[3],[-1],[10],[-7],[4],[-3],[3],[-4],[-10],[-8],[4],[8],[10],[7],[6],[-7],[10],[10],[-9],[10],[8],[2],[1],[-6],[8],[9],[-3],[-3],[6],[8],[-10],[3],[-5],[3],[-1],[-7],[6],[-10],[-5],[9],[8],[9],[-5],[-4],[-2],[5],[9],[5],[10],[-6],[-1],[-9],[4],[8],[-4],[7],[5],[5],[8],[-2],[-4],[-4],[6],[7],[-9],[8],[9],[1],[-7],[-3],[3],[4],[5],[7],[1],[-4],[8],[-9],[9],[-2],[-2],[10],[-8],[-5],[9],[-5],[-9],[8],[8],[-5],[-7],[-5],[-9],[1],[4],[-8],[-4],[8],[-1],[-8],[-10],[-3],[-1],[2],[8],[-10],[8],[-10],[-4],[7],[-4],[4],[5],[-1],[-4],[9],[1],[-4],[-4],[-4],[6],[5],[-3],[-1],[6],[5],[-2],[8],[-3],[-8],[-10],[-5],[-10],[5],[-5],[-6],[5],[5],[8],[5],[3],[-4],[10],[-4],[2],[2],[-10],[5],[5],[-4],[9],[3],[1],[3],[5],[3],[-7],[3],[-10],[-2],[1],[-6],[-2],[1],[-1],[10],[-2],[5],[3],[5],[6],[-6],[-7],[-2],[-9],[9],[10],[-1],[6],[-2],[6],[8],[-6],[-5],[1],[-9],[-10],[-9],[5],[3],[-8],[4],[-10],[2],[8],[5],[-7],[3],[-8],[-4],[-8],[5],[7],[4],[5],[-4],[2],[1],[-2],[1],[9],[3],[1],[-1],[6],[-7],[8],[4],[-3],[-9],[-8],[3],[10],[5],[9],[3],[2],[-3],[-6],[9],[2],[8],[-7],[7],[-3],[-10],[9],[2],[-7],[3],[-2],[3],[-6],[4],[-3],[-4],[10],[-4],[4],[-9],[-8],[-7],[-2],[6],[5],[5],[-10],[9],[9],[8],[10],[-6],[3],[9],[3],[-2],[7],[-8],[8],[8],[7],[-1],[4],[-3],[-7],[4],[10],[-2],[-3],[-10],[-9],[7],[-2],[4],[-3],[5],[8],[7],[10],[-6],[8],[6],[1],[2],[-9],[10],[5],[-5],[-4],[-10],[3],[-7],[5],[-2],[3],[-2],[7],[10],[8],[-2],[6],[-4],[-9],[9],[7],[-10],[-7],[9],[2],[-7],[-9],[-5]], dtype = "uint64")#candidate|3313|(2288, 1)|const|uint64
call_3312 = func_848_call(relay.reshape(const_3313.astype('uint64'), [16, 11, 13]), relay.reshape(const_3313.astype('uint64'), [16, 11, 13]), )
call_3314 = func_848_call(relay.reshape(const_3313.astype('uint64'), [16, 11, 13]), relay.reshape(const_3313.astype('uint64'), [16, 11, 13]), )
func_663_call = mod.get_global_var('func_663')
func_666_call = mutated_mod.get_global_var('func_666')
var_3323 = relay.var("var_3323", dtype = "float32", shape = (4, 660))#candidate|3323|(4, 660)|var|float32
call_3322 = relay.TupleGetItem(func_663_call(relay.reshape(var_3323.astype('float32'), [15, 11, 16])), 1)
call_3324 = relay.TupleGetItem(func_666_call(relay.reshape(var_3323.astype('float32'), [15, 11, 16])), 1)
output = relay.Tuple([bop_3304,call_3308,const_3309,var_3310,call_3312,const_3313,call_3322,var_3323,])
output2 = relay.Tuple([bop_3304,call_3311,const_3309,var_3310,call_3314,const_3313,call_3324,var_3323,])
func_3334 = relay.Function([var_3302,var_3310,var_3323,], output)
mod['func_3334'] = func_3334
mod = relay.transform.InferType()(mod)
var_3335 = relay.var("var_3335", dtype = "bool", shape = (7, 7, 12))#candidate|3335|(7, 7, 12)|var|bool
var_3336 = relay.var("var_3336", dtype = "float32", shape = (126, 1))#candidate|3336|(126, 1)|var|float32
var_3337 = relay.var("var_3337", dtype = "float32", shape = (4, 660))#candidate|3337|(4, 660)|var|float32
output = func_3334(var_3335,var_3336,var_3337,)
func_3338 = relay.Function([var_3335,var_3336,var_3337,], output)
mutated_mod['func_3338'] = func_3338
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3664 = relay.const([[[-4,6,4,5,-6,6,-6,-7,-7,7,10,-1,4,9]],[[9,-4,6,1,2,9,-10,2,-9,4,-2,5,-8,-5]],[[8,-10,7,7,8,5,-7,-9,-9,-10,10,2,8,-3]],[[4,9,-4,-8,-5,-6,5,2,-6,-9,-2,1,5,-5]],[[3,-7,8,10,5,4,-4,-4,2,1,8,2,8,-3]],[[9,6,-10,8,1,1,-5,-9,-5,-8,-8,2,-10,6]],[[-8,-3,-9,-10,5,8,-5,5,3,-10,4,5,10,6]],[[2,10,-2,-8,5,1,-5,8,-9,-3,-7,-1,3,-3]],[[-3,-5,-2,6,9,7,3,3,-9,1,4,-8,-9,1]],[[7,6,-4,5,-5,2,-7,7,-6,-10,-9,-1,-5,1]],[[-2,-7,-8,-8,-4,-10,6,-3,2,-4,10,3,7,2]],[[7,-7,8,7,-6,8,-8,1,2,-10,5,3,10,-5]],[[-2,-10,-2,9,2,8,10,10,-6,-5,-6,-3,9,-6]],[[-1,-5,-10,1,3,-4,5,2,9,7,-4,4,-7,3]]], dtype = "uint16")#candidate|3664|(14, 1, 14)|const|uint16
var_3665 = relay.var("var_3665", dtype = "uint16", shape = (14, 10, 14))#candidate|3665|(14, 10, 14)|var|uint16
bop_3666 = relay.bitwise_or(const_3664.astype('uint16'), var_3665.astype('uint16')) # shape=(14, 10, 14)
bop_3682 = relay.floor_divide(bop_3666.astype('float32'), relay.reshape(var_3665.astype('float32'), relay.shape_of(bop_3666))) # shape=(14, 10, 14)
func_2300_call = mod.get_global_var('func_2300')
func_2302_call = mutated_mod.get_global_var('func_2302')
call_3692 = func_2300_call(relay.reshape(const_3664.astype('float64'), [7, 14, 2]))
call_3693 = func_2300_call(relay.reshape(const_3664.astype('float64'), [7, 14, 2]))
output = relay.Tuple([bop_3682,call_3692,])
output2 = relay.Tuple([bop_3682,call_3693,])
func_3717 = relay.Function([var_3665,], output)
mod['func_3717'] = func_3717
mod = relay.transform.InferType()(mod)
mutated_mod['func_3717'] = func_3717
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3718 = relay.var("var_3718", dtype = "uint16", shape = (14, 10, 14))#candidate|3718|(14, 10, 14)|var|uint16
func_3717_call = mutated_mod.get_global_var('func_3717')
call_3719 = func_3717_call(var_3718)
output = call_3719
func_3720 = relay.Function([var_3718], output)
mutated_mod['func_3720'] = func_3720
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3872 = relay.const([[[-2.600762,-2.938586,6.759110,-7.250015,3.683236,-7.806262,-9.584457,4.038812,7.525132,0.618775,0.803000,6.397674,-0.024884],[-5.471900,5.314948,4.942365,4.332656,5.799609,-9.982279,6.402727,3.380589,-5.040436,-8.121846,0.110771,-6.306877,5.279311],[3.811423,3.232000,-1.327741,9.127904,0.983433,9.730640,1.149542,-7.200226,-4.167204,4.724148,5.219485,6.600647,5.821939],[-0.160092,-5.263417,4.414897,-0.374902,9.344732,2.410730,-3.822635,-5.018207,8.510253,-3.566161,6.422216,5.707781,8.591317],[-9.860811,-0.735233,7.693452,4.861594,-4.607522,5.569799,4.473320,3.026437,-3.142036,4.515658,4.234231,-0.774944,-4.208715],[-9.534171,-0.490251,5.158913,0.131000,-0.334918,-2.286983,-8.958984,5.191344,8.365950,-6.360432,6.325468,-4.030949,5.818036],[8.388042,-9.130752,6.640135,8.741032,-1.378451,-2.179350,2.315565,-2.757437,-6.426344,-1.895173,2.719735,-2.462759,3.381834],[-8.679194,6.659261,1.010965,0.785356,-3.748495,6.722247,-9.619311,-8.708023,4.141760,9.400837,3.219816,-7.213787,9.979238],[1.810969,1.377256,6.728655,6.210146,-0.071789,7.297592,-6.592410,-5.702714,-4.823155,2.887936,-8.573399,-5.189990,-3.465353],[7.390020,5.278685,-1.930012,0.147077,2.413789,7.475416,2.083698,-8.985563,4.668078,-7.008781,-2.263061,-9.102159,-9.042753],[-1.948523,4.073870,-7.761664,0.244996,7.760081,0.552347,6.447889,-6.958724,4.657907,-7.313793,-3.295304,-8.409613,-8.059086],[5.442306,-1.728231,7.483971,-9.685082,2.785988,7.760316,5.644932,1.387485,8.365727,6.081776,8.252658,8.377905,-5.848018],[-4.336006,1.634692,8.900734,5.964307,-6.250384,-4.232527,7.707982,6.278226,-9.239897,-9.030965,3.599120,7.750768,9.789220],[5.462724,-3.077706,-5.520071,-3.994988,9.911792,4.686896,2.583477,3.514629,-8.683831,-7.338102,-2.202890,-4.029298,-0.255522]],[[-1.576683,9.104912,-3.142251,3.910916,-3.363036,3.632231,2.720087,5.545197,-7.056117,-3.275019,-5.590503,-0.235529,-7.883996],[-3.925788,3.480074,0.555099,-8.707693,1.043130,8.256047,5.512692,1.767729,3.289602,-1.000460,2.354356,3.388648,-0.031435],[-0.220282,-1.900092,2.337375,-2.171529,9.360070,2.218549,-0.447248,2.033089,3.532602,1.967918,8.076575,4.536749,1.202311],[-0.045304,-4.956732,3.816284,-0.521426,1.915527,-1.632065,-4.415003,7.285486,9.132414,7.559551,-9.846845,0.296582,1.703622],[-2.429098,-4.697497,8.800017,-5.241528,-2.968402,-5.448711,-3.820116,-9.379644,6.380740,-9.817949,-0.799842,-7.805663,-7.007290],[-9.945581,7.654703,4.192813,-9.841272,0.017110,-5.007213,3.888487,4.370694,1.589171,-2.545279,-2.870693,3.241697,-3.207892],[-4.092146,1.768380,0.796389,1.692113,3.871987,-0.728759,-6.106193,0.132829,-1.959643,6.266620,-7.991671,9.783217,6.201386],[4.411136,-4.854824,-1.182232,-4.011676,-5.558009,-0.286300,-5.428407,-8.956060,5.453680,3.578274,9.335457,-0.059840,0.900033],[-2.405979,8.697787,4.571616,-2.047193,-4.499545,-4.008751,-0.650693,3.131728,-1.026888,-3.292581,-5.135891,-9.565062,-9.920115],[3.093839,-9.409646,3.941299,0.049270,-5.872617,5.294838,2.540394,-9.652940,9.137242,-2.180881,8.607620,-8.027480,6.582901],[2.484215,-8.885330,9.444260,-1.337657,6.158596,-0.476577,-0.851858,9.047798,8.916712,-6.887585,-4.357203,-9.549992,-9.996251],[-0.541698,4.951270,7.905221,5.857483,-6.951333,-0.033564,-5.453981,0.389263,-6.723890,-8.894540,8.479199,-9.761772,9.324030],[1.201120,2.180900,6.871006,8.345399,2.157711,5.142220,-9.778638,-3.386814,1.932940,-4.246449,9.176819,-1.260393,-3.197460],[-7.360404,7.827119,-0.848082,4.097554,-1.406593,6.751615,-4.451952,7.203601,6.906133,4.104352,-0.271290,-5.467329,0.332695]],[[3.326578,7.375683,-1.646323,9.201792,6.619442,-6.887726,7.049343,2.002333,-3.334981,-1.702832,-6.122036,-2.409515,4.442687],[-0.758799,8.498836,2.983134,2.517932,3.854298,-0.137294,-9.774112,-6.212334,8.748595,8.751607,-4.267242,-3.609424,8.357307],[-2.425548,-6.768037,-4.924837,2.006612,8.006097,0.744711,-2.398241,-0.262124,8.643914,-3.357717,1.181975,4.650808,2.468873],[4.523540,-7.348049,-9.768431,-3.937052,-0.062014,0.108114,-3.840455,4.055769,3.697593,-3.518760,-6.386349,-1.910947,4.145367],[-3.762552,7.383331,-1.361329,4.404835,2.879541,8.905521,5.836695,0.820078,-2.833743,9.377853,5.154122,7.905216,-5.348284],[2.609911,-2.775622,-9.017992,7.703567,-6.298336,-0.850024,7.799293,5.743249,2.378699,-6.279398,3.940163,0.191015,-9.490513],[-1.151839,-0.507079,-3.308763,5.190896,5.983574,6.963011,6.394084,-5.629333,-6.848695,-7.320466,0.027022,-8.654357,-6.039459],[-0.390390,-0.686307,-9.514796,-9.264171,4.165558,-6.141247,1.906187,-6.870279,-9.538137,8.938100,-3.350412,-2.034768,4.157071],[-6.857862,-5.804289,-0.559900,-1.472767,8.860349,7.646268,-9.006104,-7.539300,9.193378,-2.557434,2.296560,-8.026683,0.177037],[-7.410772,6.351163,1.515464,0.012692,-7.919364,-2.508238,-3.979698,0.884968,8.060119,-1.857627,-2.931499,-0.274633,4.694347],[5.953831,-0.221915,-0.769281,7.096178,-5.350261,-6.065881,-7.628341,9.783967,5.889824,-3.890270,4.931165,-1.300783,-7.771079],[-6.161221,8.281653,-5.531150,2.973030,-4.456456,8.148743,5.216599,-0.416992,8.135260,-9.423229,-2.808616,-9.184626,-4.610532],[-7.142474,2.139459,8.791807,4.119722,8.489434,8.096782,-2.151894,2.459131,4.113816,-5.171348,-7.970172,-8.708839,-7.159134],[-5.457510,-9.368047,4.516170,-8.032441,9.194826,-0.216121,-5.871332,-5.021719,-1.922698,6.066139,-3.012756,-6.644377,2.389414]],[[-9.056568,6.697042,-1.009346,8.723173,-9.149622,8.923487,3.777710,-2.675606,-3.615948,3.426688,-6.619855,6.984167,1.153757],[1.654293,-5.784420,-2.189630,-4.192743,-4.085180,-1.317209,7.864103,-8.462216,3.446391,8.692278,9.924726,-2.353939,-6.009254],[-5.761411,0.967169,2.749769,7.737995,0.708027,-3.176317,5.428260,-3.417136,-3.074360,-8.528951,-3.842085,-7.752394,7.420290],[8.324568,5.505556,-8.131162,-5.229824,1.834034,-0.779466,8.402334,5.158017,-2.938307,-5.646765,-8.034438,-7.774065,4.479152],[-6.692427,4.700968,5.661530,1.895783,-9.198652,-6.950816,5.140213,0.108024,-5.171505,2.997887,-9.911584,-8.730892,-7.257382],[-3.680801,0.595545,-9.253556,2.564807,2.107129,-8.773745,2.364737,2.369988,1.910329,-8.066846,-2.221922,-3.511359,-5.359816],[0.640295,7.267528,2.399981,1.087689,-0.368761,-8.317545,2.596725,-8.553468,-4.424384,-9.009134,-3.704048,6.739002,-1.115639],[2.605745,4.279192,-1.658643,4.546606,7.760120,8.567978,0.412038,-6.725683,3.801952,-6.198472,2.470070,-3.521928,-8.971652],[-2.754632,4.476876,7.476721,6.546613,-1.110115,-9.760971,5.530643,-4.132988,-4.263629,-3.263463,3.952255,-5.775793,-9.741118],[-7.005911,8.628806,2.358268,-9.297771,8.466356,7.289547,3.735652,-5.431276,6.727049,2.276974,-2.285346,-5.781749,-2.087940],[-6.481323,5.896394,-4.833061,8.658347,-1.031799,7.268398,0.592328,-0.055625,1.926188,-3.920951,5.099428,-9.542641,4.729200],[-5.364179,2.571352,7.029384,0.295571,-8.578112,2.774529,-1.093764,-2.105292,-7.233600,-5.546157,1.692558,-0.666628,6.937584],[7.440149,-2.939072,-3.945214,-7.094951,1.953063,9.366636,-2.727659,6.609503,-2.982264,6.007767,5.096934,-7.036544,4.947431],[-3.933337,-6.455658,6.320054,1.897354,-1.964015,8.544363,9.405534,6.271565,2.367372,8.049302,3.585088,-7.812202,-1.840111]],[[-6.572115,3.262483,-6.549579,-3.477084,2.420538,3.806941,1.753422,-5.390233,-9.656183,-6.339925,5.024466,-1.856320,-7.479648],[-0.532529,-8.940286,-6.413022,1.295993,-5.254017,1.557668,-4.216963,1.949101,5.992052,-4.290118,4.825600,-9.180904,-2.641554],[9.819176,-1.541084,-7.534312,5.342888,9.291436,1.487699,0.953778,4.109126,-4.699584,-3.471142,8.007401,3.296678,1.788979],[-1.873907,-7.582199,6.399751,9.034573,3.833949,-0.848431,4.983704,-8.780187,0.804020,-3.078528,8.199783,-0.186001,-3.125932],[8.452077,1.480400,-2.208881,-1.631981,-9.886989,4.418963,6.284926,6.479564,4.152971,-9.091066,-7.139057,5.807156,-0.741666],[7.224574,-5.827422,-6.895794,5.369827,6.698442,6.363556,-3.443964,1.365529,-5.419984,-0.601550,4.812964,-6.500153,-2.548573],[3.566326,7.559001,-4.119681,-1.305524,3.760250,-1.751226,9.014780,-2.096329,-9.707976,-8.788443,-3.210617,-2.423935,9.290424],[-4.285078,0.164962,-1.446579,9.494985,-0.473239,-9.083389,-8.914873,9.936541,1.230196,-8.885502,-7.608878,-2.100820,5.995265],[1.733065,-9.884093,5.594967,-7.749037,3.478257,1.081296,-0.079602,-4.681689,-4.994833,-8.583398,4.340795,-9.165889,-3.268074],[-3.518818,-0.707395,1.291062,-3.518580,-5.138903,5.664345,-0.850311,4.995475,0.961380,-1.017084,-6.984988,-8.407558,-2.559147],[-3.196321,-7.044071,7.544408,-4.506404,-6.341517,4.779250,6.622939,-7.095602,-4.339911,8.523439,-9.030196,-0.666113,-7.066952],[4.627906,0.515639,-0.385390,1.946663,-0.724439,-2.699056,-3.427822,1.085333,0.570027,8.876311,2.860146,-8.201802,2.485179],[4.942825,1.248442,-7.104215,-2.313233,9.413837,-6.980224,2.210237,2.505435,5.015448,-0.638803,-2.275636,5.646420,1.914033],[0.944471,3.414738,-4.594071,-9.248457,-0.526364,3.778118,9.169843,7.244547,5.128281,-1.628829,-5.678499,-4.554796,-6.490113]],[[-2.537228,-1.260967,-9.395743,-1.963904,-1.441508,-8.922357,-4.656062,7.847338,-2.960671,-0.401679,-2.289513,-7.003940,4.897266],[-0.932652,-4.340892,-7.761607,-5.918397,-5.151738,-4.444706,-2.514418,-5.792067,-5.597394,0.435236,-9.666920,-0.435397,-0.753715],[-9.934442,4.637275,7.742219,3.909402,7.112859,4.230580,-3.422355,-1.536842,-6.991888,8.591256,-3.968787,1.252034,0.605429],[2.470763,0.281468,4.800952,-2.375206,5.948724,-8.313247,5.172098,-8.446022,-2.020291,2.829411,6.091973,2.428746,-7.210826],[-8.405991,-9.320693,3.370574,7.484566,2.455328,-8.970783,-4.153130,8.108815,-1.536960,-9.683558,7.965636,4.631991,3.655545],[-7.224544,9.443189,-2.912587,4.079911,8.881360,-8.699485,6.381767,8.354325,-2.091458,5.688344,6.528753,-2.159025,-0.744322],[-2.104980,-1.544711,-7.865611,-9.210075,9.696266,-4.097853,3.775336,4.102199,-7.427766,9.400934,-7.110390,0.872027,-7.024001],[6.457900,-4.411942,-3.914461,0.607146,2.815053,-9.643408,8.750039,-6.344515,-7.165695,-2.389279,-7.155228,-9.687032,-4.887126],[2.345511,-3.415871,-9.541512,-3.054465,3.261768,0.319115,-8.065408,-7.227373,4.196891,-3.855820,9.549301,1.265152,7.648456],[4.806340,-8.186662,-2.410538,7.970201,3.892817,4.111016,3.140440,-1.472678,3.238731,6.940487,1.625892,-8.125121,-2.272528],[-5.242263,0.119639,4.892310,0.612302,-1.122546,3.674590,-2.040823,-2.525966,4.548519,-6.119800,-7.608789,-7.378557,-6.620552],[-4.976434,3.455783,-0.417024,0.172932,7.618047,-8.563387,-3.095684,5.898135,4.482650,-7.060288,9.668408,2.262073,2.991824],[7.121443,7.679053,-9.970223,-1.207546,-7.000263,4.696369,-4.862346,3.867592,-1.504212,-6.073032,2.165784,0.544499,5.830632],[7.291116,5.887453,-4.778685,-4.091568,-5.596044,-5.342217,6.402096,3.901167,-4.706539,9.046325,7.647431,3.098010,2.532793]],[[8.390002,-6.459410,9.864799,9.706620,-9.045659,-2.982055,1.601800,8.231552,3.191617,-1.915089,-3.862866,7.520965,-7.389064],[0.564232,-9.065115,9.968729,2.309425,-6.859532,9.138907,0.351716,4.780623,7.444016,-3.178291,-8.355335,5.448302,3.306187],[8.025164,3.159462,3.122925,5.924796,-8.285508,9.135822,-9.875016,-1.918207,9.918987,-0.580413,6.865982,5.146543,-8.538759],[-7.923622,-3.200647,9.922220,-5.720670,-0.922534,4.115309,9.169421,-6.517502,-1.047620,-2.450477,-6.368106,-0.384222,-3.518339],[-5.485324,-3.334061,-8.663780,-0.940583,-2.179067,-5.674839,2.969521,-5.083108,7.094356,-6.270739,-3.501470,-4.699883,9.807663],[-4.328767,0.310829,-9.825861,-3.287010,0.686232,9.157181,8.260091,1.555730,-8.484366,-8.341212,-0.223927,-4.979698,2.993572],[7.679340,3.248017,1.605988,-2.579601,-8.476983,-5.413583,8.986838,6.605641,-0.863837,-8.061436,6.200951,-3.474997,4.181476],[7.326906,3.752893,-0.315011,-5.971025,6.833939,8.014218,2.151419,-1.749626,-8.199078,5.924048,-1.693882,8.550244,7.348614],[5.711141,-7.645025,-4.354962,-2.662807,6.618561,-3.659755,-7.411804,0.610605,-0.982394,-7.677116,-3.562697,-9.863119,-7.697131],[2.242959,-7.699932,-8.085342,-6.758141,-6.573544,-9.967517,-6.671532,-2.227358,-6.204236,0.309208,-5.915834,-0.179109,-5.272705],[-3.048218,-9.167046,-3.337736,-8.370764,-2.058052,-2.572803,2.965304,-2.216245,-8.048434,7.066619,6.846304,9.347060,8.348780],[-7.010370,-0.721262,4.193845,-9.484140,-7.997422,6.590427,8.273953,5.787042,4.436681,-4.194865,8.411299,-3.837464,2.327699],[-7.455622,-6.755115,7.109474,2.429223,-3.818061,-1.913169,-0.759866,5.464716,7.732362,1.590954,-2.633703,7.432657,-3.981323],[3.136212,-6.242168,5.935899,-5.010140,-4.128854,-8.982474,7.682783,-0.840999,1.398627,-2.634767,6.967636,3.692376,9.591898]],[[2.876491,5.840985,1.715921,-2.549466,1.148988,-9.072468,-6.210582,6.321035,-7.937145,5.662886,-2.591139,3.541437,1.097857],[-8.471242,1.948809,-8.027083,1.734619,2.385059,0.216324,-6.408298,2.716697,-6.520366,1.024361,-9.880313,-6.822816,2.131759],[5.936382,-6.474242,1.860997,2.561648,-0.099602,9.978057,8.810842,-8.252750,-2.310174,-4.200606,0.968479,8.400309,-2.421526],[-8.240188,8.801371,-5.213168,-9.071922,7.737699,9.180817,-0.307082,4.669619,7.722951,-3.074939,4.434137,-3.457718,-3.767896],[-1.744868,5.773945,-8.619193,6.404215,3.121532,-1.792539,-7.716521,6.337933,-8.610903,5.018248,2.610342,2.786523,-6.731141],[-1.428277,-1.196648,-0.464382,6.618864,1.557281,4.894184,8.405966,-6.888903,-3.746593,-3.804719,4.274821,-7.258233,-3.627455],[9.744169,4.269641,-6.954102,6.602049,9.843309,7.720177,8.760892,-0.911913,4.627581,1.246730,6.971575,5.805731,8.407921],[-4.974585,1.078990,4.593524,-6.136981,6.578861,-8.092191,3.859794,-4.318213,-6.901783,-7.039465,4.394319,4.774490,4.453182],[-1.265031,-2.872833,9.490842,5.732664,4.767194,-5.453054,-8.413305,-2.141219,-0.518241,-3.404310,-1.438814,-2.739735,9.801653],[-3.338290,-9.344534,5.195022,-2.718873,-0.019173,-9.117599,5.428318,-1.043014,-9.292977,5.962470,4.490243,-2.798082,-1.191865],[0.048645,4.128011,-4.695799,4.112011,-5.803319,-7.423896,-9.674108,-7.970103,-6.151032,-1.814955,1.639131,0.583756,1.193375],[-0.924961,-8.465964,-8.110915,9.630132,-4.212159,9.875691,-3.687386,-6.038254,7.935662,2.338685,-8.039989,6.593376,-1.028552],[4.936965,8.224692,2.942338,-0.767877,-1.408560,5.109081,7.664323,-0.806802,2.598355,-1.025807,8.632014,-2.281220,4.791882],[-2.773378,2.648795,-0.023037,3.958843,4.087804,7.335475,-0.670037,-7.918504,-0.104629,-8.537716,-8.476808,6.716113,6.730334]],[[-3.501649,-6.668479,-3.001915,-9.187754,1.981183,-0.464947,-0.035746,7.466315,-2.899835,-9.949565,4.291660,-6.486911,4.074212],[8.407156,4.734298,0.310278,-7.221980,5.685167,-8.726687,-8.378571,-5.206403,-0.858710,-1.061925,7.258645,-4.459014,3.461033],[-8.515223,5.803874,8.147131,-4.271581,7.612107,-4.773831,9.807628,6.587536,-7.703444,-5.294955,-8.591576,4.470281,-7.678407],[6.864662,-1.874103,5.059616,-1.340792,-9.977336,1.706319,-2.972337,-1.781960,8.230307,3.138165,-5.580950,-0.741359,-2.337808],[5.904031,-2.808930,-6.105953,-0.597443,-4.609195,3.165559,-1.044842,-7.251167,9.367140,7.636575,-7.980207,3.046534,2.719386],[0.079671,-3.649696,-4.863465,0.992901,-7.556722,9.108636,9.039368,-3.527525,-1.159570,-1.970432,-9.225668,-1.674872,-1.309544],[-1.930952,-3.051364,0.478262,-1.379732,7.188796,5.179294,0.322587,2.036212,4.649419,-7.582781,0.432331,-6.519002,-0.852831],[4.549313,-9.254660,8.724193,-6.238303,-8.148265,5.792492,0.429690,-9.378038,9.030907,-6.422941,-3.268864,0.272705,2.941071],[0.563382,9.325173,4.627668,-4.692637,-3.934561,-9.864709,1.301139,-3.371368,4.975626,-7.002342,-0.482851,3.749456,-2.802198],[-9.552355,9.178335,-6.496324,-3.823361,-1.250633,7.417260,9.477300,-3.279822,-9.768874,4.907846,-7.974330,-9.250790,-8.623376],[-8.441979,-0.238195,0.047397,7.146421,-8.097882,7.945614,1.148805,-1.054025,4.035373,-4.507653,-1.664339,8.166412,5.781665],[-0.205981,-6.912989,-1.268819,9.127501,1.545962,-8.523358,0.100997,3.067163,3.155385,-7.865326,1.582343,0.724515,0.999981],[-4.668806,1.028185,-5.731986,9.027617,-5.161723,2.201881,-0.790267,-7.871740,5.024839,-9.963128,7.829203,2.846068,5.545749],[9.157821,-6.373015,-3.581911,5.630738,-8.844836,-5.374497,6.430612,-5.303654,-6.556592,6.297697,0.220612,-7.989786,1.986102]],[[5.840597,3.946057,4.195486,0.932326,8.373658,-5.956327,-2.019475,-3.065575,1.784191,5.140321,-3.943590,-0.357234,3.058149],[0.739222,2.639809,0.714712,4.822667,-0.501435,4.166968,6.762435,3.890050,7.499426,-4.606280,-0.957031,5.442538,3.472911],[8.285489,-7.881410,2.067875,-3.725146,-5.802956,9.625132,-8.525244,2.745380,-1.970005,-3.258523,-4.025897,6.176837,7.895080],[-5.424750,3.899717,5.552517,-9.071911,0.008928,3.087165,-8.748051,0.740202,1.586691,1.614127,4.064780,2.896492,-6.554410],[-7.132054,3.991360,7.442800,-5.020547,2.906152,-4.297310,3.108457,-1.328752,1.187047,4.907501,-8.199688,7.619471,2.205057],[6.312809,-7.808460,-6.086776,3.179834,7.937487,-3.268759,-2.531665,4.133400,5.130082,-3.987900,4.058647,-8.596715,4.777295],[6.551727,9.506407,3.433711,-8.549428,-7.195609,-7.382686,-4.850547,-7.538079,-6.930552,-0.171062,5.622349,-9.671966,8.876280],[-5.796456,-1.163177,4.657477,-0.083906,-7.175047,0.108524,6.436483,-1.834321,-7.502141,9.118464,8.066302,0.303831,8.597423],[5.864144,-3.102075,1.840459,-1.356769,-1.081867,-4.677042,-7.689022,2.790316,3.400446,7.880980,-8.009087,-6.050579,0.439861],[7.724918,5.932257,5.698264,5.812508,-8.695714,-1.880332,-5.367150,-8.843589,5.605289,-1.003027,-8.974572,-7.788483,7.394340],[6.274677,-7.589369,5.035969,9.948977,3.291531,3.428589,4.799746,4.427797,-5.528143,-0.274450,-6.635065,-2.123296,-1.049219],[-0.336600,-2.186827,-6.931727,7.663061,-0.581483,-1.996532,-4.297842,4.264336,-7.626725,8.925532,-4.936506,-8.325714,-7.637408],[1.933742,2.707543,1.113362,-0.722781,1.828806,-3.057567,1.876433,8.367198,-7.370661,9.030250,0.853739,-1.473951,-3.143327],[-1.905061,-0.947420,6.632269,2.596633,9.436192,9.759109,9.031329,-1.210393,8.188920,-6.926866,-3.885764,-9.028912,-3.766143]],[[9.673894,-7.625970,-8.111177,-5.225631,6.877020,-8.199585,-1.637831,-0.145162,5.788417,-8.049456,5.031468,6.598353,-4.866421],[-9.262917,-8.172619,-4.437620,-9.895082,3.508396,-0.958845,0.863532,0.456178,-1.680577,7.518406,7.579025,-2.040752,7.999799],[-5.467461,-1.789284,-3.858081,4.244696,3.190019,-4.588783,3.233137,-2.413391,-8.142740,9.218641,0.472270,6.077238,-5.225367],[0.886937,9.487420,-2.354748,-8.013546,-0.007119,-8.206436,7.285809,-5.479809,7.767830,3.940052,1.399314,6.535019,1.437740],[-5.776405,8.730486,-0.380075,-0.500427,8.818788,3.808770,0.346887,-8.986579,2.045898,2.332337,-7.388940,9.176590,7.871547],[0.451847,-4.687817,7.287507,6.623608,6.425315,-2.564476,3.783818,7.122031,4.448056,3.532299,-4.392055,7.293063,-0.815282],[-2.451044,2.371118,-7.506478,-0.588323,2.437529,5.263715,-2.188852,-8.907604,-1.551993,8.406640,-1.540135,-0.609441,-8.573963],[3.256258,8.901843,0.697516,9.894692,2.881636,4.871552,-3.238466,4.565189,-8.354128,6.597907,-5.437617,-5.092924,3.293933],[-3.372288,-9.456230,-9.601533,-9.237671,7.732875,3.254767,-9.392595,-4.834514,-4.420075,0.173685,5.895039,9.211633,-6.112313],[-9.930961,6.303000,-7.934111,-8.984448,6.482345,-2.080206,-4.163829,2.628537,-8.970350,-5.388640,-0.352974,-3.193411,-6.039095],[3.700066,-3.843761,-8.804385,-3.366760,-9.431481,3.879490,-7.467808,2.680022,3.454932,-7.523333,6.192866,-5.301794,-2.775240],[-4.707915,-6.609671,-0.855066,-1.421402,-9.601544,6.931828,2.305772,2.126393,-5.347016,3.368252,-6.641995,8.872584,5.951110],[9.694951,-5.340922,-1.993339,-8.812757,-2.550386,-2.841737,0.568093,2.897239,-5.127431,-3.613800,1.015000,4.217868,-3.936843],[4.827326,-5.897916,-6.993654,9.513698,5.671699,9.536104,-8.840914,-2.502431,7.934378,1.719148,8.632485,6.234154,0.051229]],[[-6.957508,5.057001,-8.722065,3.968851,8.155882,6.764013,-5.115906,5.204871,-8.266769,2.620529,-0.758033,0.447154,9.260838],[8.750813,-4.920681,-7.621213,8.726780,-8.273990,-2.750962,6.236039,0.912455,-6.169793,2.608465,-9.649034,-1.359890,5.917215],[-3.751232,-1.476912,0.238098,-9.085426,5.759748,-7.676659,-8.457319,-0.193597,-4.885104,-0.883126,-1.717219,-1.639202,-4.568232],[-8.814167,-3.196336,-5.712530,-4.306226,5.457363,-5.661190,0.563286,-0.443983,2.427584,-8.451678,1.558930,8.676354,5.412752],[1.505060,7.653350,-5.283844,-0.661933,9.210984,1.929421,7.731914,6.517810,-3.268421,0.435187,9.165371,9.447618,8.869928],[-5.685073,-7.345972,-5.083009,8.077926,-1.581671,0.217143,2.874219,4.762884,-1.964577,0.901170,-8.294366,0.216583,-1.142898],[-7.430621,-9.519969,-2.336816,-7.318298,-2.724812,-9.966792,1.785919,0.366466,8.414638,1.586982,1.936730,-8.199114,-1.023767],[-7.524649,-5.591007,-6.490905,-9.228391,-7.005803,2.492299,-3.859445,-8.823608,-0.949786,7.651261,-1.484754,-7.011717,6.506095],[-6.953324,-6.699110,-0.475647,-2.951896,3.470073,-1.805986,0.854248,-4.761884,3.477541,7.006597,-1.370007,0.848997,5.350797],[-5.345964,-4.476182,-2.532297,9.251127,2.194023,9.843764,0.854287,-2.757076,4.460981,-1.708038,-9.467086,-7.215957,6.076677],[3.516511,-9.865401,7.430940,-2.635738,-3.016840,-6.783296,3.198257,5.018308,0.930035,6.242151,-9.596646,4.750256,5.626832],[9.341133,2.755831,-4.944877,1.835609,-5.715332,9.613271,-6.932142,0.894194,-5.256509,-4.732226,1.754536,-5.361335,7.674050],[0.332858,0.704605,8.343198,-1.866715,-6.867415,6.714374,7.130143,-1.936122,7.472888,-5.200233,4.380891,1.680501,4.914268],[4.375166,-1.182410,-7.466100,4.539346,-4.494314,-7.371882,-2.750806,2.450572,5.484869,9.384269,7.295093,-6.325291,9.069186]]], dtype = "float32")#candidate|3872|(12, 14, 13)|const|float32
uop_3873 = relay.exp(const_3872.astype('float32')) # shape=(12, 14, 13)
func_3045_call = mod.get_global_var('func_3045')
func_3048_call = mutated_mod.get_global_var('func_3048')
var_3881 = relay.var("var_3881", dtype = "float64", shape = (72,))#candidate|3881|(72,)|var|float64
const_3882 = relay.const([-9,1,7,-4,-4,3,-1,-1,8,7,-6,10,-1,3,2,7,9,9,-1,10,-3,9,6,3,10,1,-6,-7,6,10,6,-1,-7,-10,3,-6,-2,10,-5,-1,2,2,3,-5,-9,-8,4,9,-10,-2,8,-9,4,-10,4,-5,3,4,-9,6,-6,1,6,5,-9,-10,6,-9,1,-1,-1,1,8,-2,6,2,-4,4,-5,7,6,2,9,4,1,6,6,5,-3,-10,9,-3,-9,5,5,-7,-7,7,-2,-7,8,4,1,9,-10,-4,-3,2,-3,-5,8,3,2,-3,-1,-9,4,-5,5,-8,5,6,9,9,6,2,7,-9,-3,3,-1,-3,6,-9,-3,7,-8,-5,2,9,-7,10,-8,3,9,5,8,6,-9,-8,1,8,8,-8,-7,-8,10,8,-7,9,-7,-8,6,3,-1,6,6,-5,9,-7,-10,1,-1,8,-10,-3,-3,3,9,3,-5,-5,-4,7,2,10,-7,4,9,-7,10,5,-5,3,4,-5,6,10,-10,5,-1,6,5,-7,3,-3,-5,6,-7,-3,4,10,8,2,-6,-10,10,-4,-7,9,-6,2,-1,9,-7,6,10,1,-5,6,10,10,-3,4,7,3,-6,-3,3,-2,4,-2,-6,-10,8,2,-3,7,-9,7,6,9,5,8,4,10,10,4,-7,-6,-2,2,-3,9,-1,7,-6,-9,8,1,-9,-2,5,8,-2,-8,5,8,-10,-1,5,8,2,-4,-7,4,8,-9,-4,6,1,8,3,-5,5,1,4,5,9,8,-6,5,10,6,1,8,5,10,-4,-8,3,-10,1,4,-5,-9,7,-7,-8,-9,-5,2,4,8,1,6,-7,2,2,-9,10,-9,10,4,-9,8,1,-5,-4,-3,-9,8,5,-2,-5,5,-9,-2,10,-8,10,-6,7,-6,-2,-3,-7,-7,-10,1,-1,1,-3,-10,1,-4,5,-2,1,3,-6,-6,-9,7,-1,-5,5,4,-10,-10,4,2,6,-4,-9,-2,-7,-9,-1,-8,-3,7,-2,5,-7,3,-1,-3,-8,-3,7,-3,6,-3,-8,-1,5,-8,-9,8,-10,-7,7,-9,8,5,9,-8,-2,2,-1,1,-1,2,4,7,-3,6,-4,-7,6,6,2,10,6,-1,5,2,3,-7,3,10,6,-6,-10,3,-6,3,4,1,-5,4,6,-5,9,5,-4,8,2,2,-8,10,-3,-2,-6,4,5,1,-3,10,8,6,10,-4,7,-6,9,10,1,-9,-5,10,1,1,8,8,7,-8,7,1,7,10,7,10,-2,-5,-1,6,6,8,1,10,9,6,1,9,-7,6,8,2,-4,-6,-3,9,-10,-3,-2,-8,2,-6,-3,1,-5,-6,10,7,-8,-10,-5,-2,7,-7,-10,-1,-1,5,3,6,10,5,1,-5,4,9,6,6,7,-2,10,-1,-2,7,-2,-5,4,-2,3,3,5,-7,-3,4,-10,-9,2,1,8,-1,-10,1,-8,8,-4,-9,3,2,10,-6,-4,1,6,-2,-2,5,9,4,10,-9,3,5,-3,-9,-3,-5,3,7,-10,4,-3,-3,-6,2,-9,2,10,-7,2,-7,-3,6,-2,5,-1,3,-9,-8,3,3,-10,5,2,-2,10,-1,-6,8,9,10,-6,6,1,-2,-2,8,10,2,5,-6,5,-7,4,9,-3,-5,-1,-4,-5,-7,-1,-10,8,3,-8,-10,6,-6,-5,6,-1,6,-4,-4,-9,7,-6,3,1,-9,4,-5,-7,3,-5,1,-9,-10,9,3,5,-8,-7,4,8,8,-3,2,-4,-3,3,-5,-2,7,-10,-7,-10,-5,9,-4,3,7,-5,-5,4,-7,3,-1,-8,-6,1,-3,-10,8,10,-4,-6,-10,-2,9,6,-4,10,3,4,-8,3,-5,-2,4,-7,-6,1,-5,4,2,-1,-6,-2,1,-8,-2,-10,6,10,-5,-8,1,8,6,-9,1,-5,-3,8,4,2,-9,-2,4,6,-10,-10,-6,6,-2,10,-5,4,1,-1,-10,-10,-5,5,-8,-1,-7,-9,3,7,-10,-1,-2,-2,-7,-10,4,-9,6,-2,-6,3,6,-6,-7,4,-10,4,-2,-8,7,-9,10,4,1,-10,-7,-10,-5,1,9,-3,2,4,-2,-4,-10,4,8,-8,1,8,1,2,4,1,-1,-6,-10,9,-3,-4,6,3,-5,-7,-10,-8,-10,-8,6,-10,2,3,4,-5,-7,-10,-9,10,-5,-2,-9,6,3,-6,1,-9,9,6,-6,-2,2,-9,-6,-6,-6,-6,1,8,5,-6,-9,-3,8,4,2,8,-10,6,-6,7,-3,10,-6,-1,-10,1,-1,-8,4,5,-9,-10,10,7,8,-1,-8,6,-7,8,3,7,-4,7,10,-1,-6,10,-7,-3,10,10,5,5,-5,9,2,6,-2,3,-4,1,-7,6,-7,-1,-5,6,-6,-9,-3,1,-6,-3,-9,-10,-3,2,3,4,-9,6,5,-3,2,6,-10,-3,3,5,-4,-4,8,-7,-6,-1,-5,8,-1,-4,10,-10,-6,-9,1,-10,2,4,-4,1,9,2,10,-5,-10,4,9,-4,-9,4,8,-6,2,10,-10,-3,-4,-4,-6,7,-10,-7,7,3,-4,-7,-5,-1,-5,-2,-2,4,1,-2,9,-4,-2,-7,2,-4,-9,9,6,-10,2,5,-8,-2,9,9,-5,4,-5,8,-2,-6,-5,-6,6,1,-9,-2,7,7,9,-1,-10,6,7,3,-8,2,-5,-4,4,6,4,-2,3,-7,5,1,-5,1,10,-3,4,-2,4,7,-5,-3,5,2,-5,2,-6,-5,1,3,9,-2,1,-9,1,-5,3,5,-3,5,5,8,-2,2,-9,7,-3,1,2,-1,8,-7,-5,-8,-9,-8,10,-8,9,8,-5,5,3,-1,8,7,-9,-6,9,5,-4,-4,7,9,-2,-5,3,4,-8,10,-9,9,-1,2,-8,8,8,-8,-4,2,-5,2,8,3,-2,-9,8,-1,-4,9,-10,6,8,6,3,7,-6,6,-6,-10,-2,1,7,-10,-5,-5,-5,4,4,-5,-9,-5,-1,8,1,-6,-7,4,-7,6,-5,-6,1,4,-9,2,-1,-2,7,-10,8,-1,2,-8,2,-10,7,5,-5,3,8,-1,-10,1,-3,-6,-6,-5,-2,7,6,-9,5,-1,5,-6,7,1,-2,-5,-3,7,7,10,-4,-5,6,3,10,-2,8,-7,5,2,-2,4,9,-7,-3,8,-5,8,-9,-3,-7,-5,2,1,3,9,-2,1,4,10,6,-5,-2,-4,-3,3,3,6,3,-5,3,-10,-8,-8,10,10,-7,8,-5,2,9,-10,5,-10,-7,3,-10,7,-3,-10,5,10,2,-3,10,9,-3,6,6,6,-10,5,3,7,9,10,7,7,-10,8,-6,-1,-5,6,-2,7,3,-1,-4,-2,-8,-8,-4,4,-3,-4,-7,-7,4,6,-8,-8,-4,5,9,-2,2,2,3,10,6,5,10,8,5,-10,8,4,-8,10,8,6,2,-8,4,10,-1,-7,-7,5,-10,7,-4,10,1,3,3,-1,-9,-9,6,-5,6,-10,-7,-7,1,-5,-4,-10,4,-4,5,2,-4,-9,2,-9,-5,1,5,1,3,-4,-2,10,10,-4,9,10,-9,-6,-2,1,-6,-3,2,9,-3,-10,9,-10,-6,-3,2,-10,10,-2,-3,-4,-7,1,3,5,-7,1,-7,-5,5,9,9,8,5,6,5,10,6,-1,3,5,3,6,-6,2,-8,1,-10,1,-3,7,8,1,-9,5,10,-4,5,-2,10,4,-7,-7,6,-6,6,8,-9,8,-5,1,-2,-8,-4,7,6,-4,-6,2,3,-2,9,1,-1,7,-1,-1,3,9,2,1,-7,3,-10,-7,10,9,3,9,-2,-2,-5,5,4,5,-2,-6,-3,-4,3,-5,-5,2,6,-2,8,-1,-6,-10,4,8,2,-5,-2,-10,-4,-8,9,7,-1,-4,-2,3,5,10,-9,-3,2,-7,-1,-1,-10,-4,-1,4,7,-5,7,6,-1,9,-5,-2,4,-5,-4,8,7,5,-2,-4,-1,7,-6,7,-1,9,1,-7,9,-10,8,9,1,-7,-4,-1,9,10,2,3,6,-3,1,3,-2,5,10,-7,-9,-3,5,-6,1,10,-5,-9,6,7,-2,9,5,3,-9,8,7,9,-3,-8,2,10,-2,-6,2,8,-6,-7,-1,8,-3,8,-6,-1,3,-5,-9,10,-3,10,4,1,-4,-10,-1,7,-5,-5,3,1,-7,-2,-1,-8,1,-2,-5,-4,1,4,-4,-7,5,9,-10,-5,-7,3,-1,2,8,-6,7,10,8,2,-4,-1,3,-8,-2,-1,-1,-7,-5,4,-7,4,2,3,-7,-2,-6,-1,-4,-3,1,-7,8,3,-7,5,-9,7,3,3,-5,-3,9,9,3,2,-5,6,-5,5,8,-5,8,-10,9,3,8,4,-1,1,-6,10,3,5,7,-9,1,-3,3,-2,-9,-8,-2,-4,-5,1,-1,-3,6,-10,9,7,-3,-8,4,-1,-6,9,1,-3,2,8,-6,6,2,-5,7,-2,2,7,2,10,6,6,-5,-4,6,10,6,1,6,-10,10,5,1,-2,1,1,-1,5,-7,-5,-4,4,-5,-7,-3,-5,-8,-6,2,2,-10,-1,1,9,8,2,2,-1,10,-7,-8,7,3,-4,1,-10,-10,-2,-8,2,6,9,9,7,1,-6,8,-4,-7,6,6,-9,-7,-9,3,-5,7,-8,-6,-8,9,-6,7,8,6,-2,-9,1,1,5,3,-2,3,-7,-5,6,10,10,1,1,-3,-2,-3,10,-2,7,-6,4,-9,8,9,-7,-7,-6,7,6,2,2,-10,1,-9,5,-7,3,-3,9,7,1,-3,2,6,-9,5,-8,-4,-5,7,-6,-1,8,2,-6,-3,4,-3,7,-4,10,6,4,-8,2,-1,8,7,-7,-5,-9,9,-6,2,2,10,5,3,-7,-10,-4,5,-6,10,-3,-8,5,8,10,5,-5,-5,2,-2,8,-5,-3,-4,5,4,-1,2,8,7,1,-9,6,7,-3,-4,8,-3,2,-2,3,6,-8,2,-10,3,1,-8,-9,3,-1,-3,8,4,3,-8,-3,2,3,-9,-5,4,6,10,-4,-7,4,8,6,-4,1,7,6,-5,-5,2,9,-3,6,2,10,7,-1,-8,8,-8,-3,10,4,8,4,-9,-6,7,10,1,3,6,2,3,-7,8,-3,1,6,9,1,-2,-2,8,2,-2,7,9,1,1,2,-7,-8,4,-8,-5,-3,-6,7,5,-3,-4,-6,-4,-4,4,-4,1,-1,-7,10,-10,10,7,9,-7,-10,5,-6,2,3,6,-1,9,-5,-3,-8,-7,-8,-6,-6,-1,5,-2,-6,1,-2,-9,5,5,2,-7,10,7,-8,-4,7,3,-3,3,9,1,10,-4,-5,6,-8,10,-7,-3,1,1,3,9,9,7,3,-1,7,-9,6,-4,10,-10,2,-4,-3,2,-1,3,-1,9,-10,9,8,4,5,8,-1,-4,4,-9,-5,4,-9,7,9,4,-8,9,-10,10,10,-3,-10,5,7,10,2,-1,1,1,-5,9,5,-1,-10,4,-1,-10,-6,-5,-10,6,-1,5,6,-3,-8,-6,2,-1,8,-2,-2,10,-9,10,1,3,2,5,-1,-9,-3,-3,-2,-7,10,9,-4,-8,5,-4,4,10,3,-4,-6,-5,-9,5,-5,-10,-4,4,8,-10,-10,9,2,-1,-5,-1,-9,-9,5,8,6,4,6,7,10,7,6,7,5,2,5,10,-10,-2,5,-6,9,3,7,-1,1,-10,-6,-4,-5,3,-2,1,4,-8,5,-1,3,10,-8,-7,-1,-6,4,-9,6,6,-5,-1,-2,9,2,-2,6,5,4,-2,10,5,-10,10,8,-6,-3,-3,4,2,4,1,7,5,-9,-10,7,-1,-2,2,7,3,5,-6,-10,6,-6,5,4,-7,-6,-2,-2,9,5,2,-1,5,2,6], dtype = "uint64")#candidate|3882|(2288,)|const|uint64
call_3880 = relay.TupleGetItem(func_3045_call(relay.reshape(var_3881.astype('float64'), [4, 3, 6]), relay.reshape(const_3882.astype('uint64'), [2288,]), ), 1)
call_3883 = relay.TupleGetItem(func_3048_call(relay.reshape(var_3881.astype('float64'), [4, 3, 6]), relay.reshape(const_3882.astype('uint64'), [2288,]), ), 1)
output = relay.Tuple([uop_3873,call_3880,var_3881,const_3882,])
output2 = relay.Tuple([uop_3873,call_3883,var_3881,const_3882,])
func_3884 = relay.Function([var_3881,], output)
mod['func_3884'] = func_3884
mod = relay.transform.InferType()(mod)
var_3885 = relay.var("var_3885", dtype = "float64", shape = (72,))#candidate|3885|(72,)|var|float64
output = func_3884(var_3885)
func_3886 = relay.Function([var_3885], output)
mutated_mod['func_3886'] = func_3886
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4024 = relay.var("var_4024", dtype = "float64", shape = (7, 11, 1))#candidate|4024|(7, 11, 1)|var|float64
uop_4025 = relay.asin(var_4024.astype('float64')) # shape=(7, 11, 1)
func_921_call = mod.get_global_var('func_921')
func_923_call = mutated_mod.get_global_var('func_923')
var_4038 = relay.var("var_4038", dtype = "int16", shape = ())#candidate|4038|()|var|int16
call_4037 = relay.TupleGetItem(func_921_call(relay.reshape(var_4038.astype('int16'), [])), 0)
call_4039 = relay.TupleGetItem(func_923_call(relay.reshape(var_4038.astype('int16'), [])), 0)
output = relay.Tuple([uop_4025,call_4037,var_4038,])
output2 = relay.Tuple([uop_4025,call_4039,var_4038,])
func_4052 = relay.Function([var_4024,var_4038,], output)
mod['func_4052'] = func_4052
mod = relay.transform.InferType()(mod)
var_4053 = relay.var("var_4053", dtype = "float64", shape = (7, 11, 1))#candidate|4053|(7, 11, 1)|var|float64
var_4054 = relay.var("var_4054", dtype = "int16", shape = ())#candidate|4054|()|var|int16
output = func_4052(var_4053,var_4054,)
func_4055 = relay.Function([var_4053,var_4054,], output)
mutated_mod['func_4055'] = func_4055
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4301 = relay.const([[[-8.230111,2.058596,1.878902,0.420928,-4.127245,-9.904957,-2.949570,-6.656351,-9.071121,-0.347508,-6.349819,-5.382258,-6.183121,-4.490348,1.655201],[-7.223425,6.559678,-9.559718,0.007665,8.046942,-5.985837,-5.395380,-9.617335,0.379558,5.534122,-3.648420,-0.579815,7.028067,-0.826074,-5.891250],[7.389772,1.602167,-8.175712,8.748719,8.523645,9.774816,-8.554089,8.106330,-1.846699,-1.717545,-6.075874,-2.151293,9.961567,4.458582,9.459014],[-4.175494,-7.695001,5.246690,2.889647,2.294330,-5.471174,-5.968809,-2.379732,1.795028,-4.691427,-2.056562,-8.777126,6.919546,-5.992856,3.680449],[-2.332423,-8.519415,-3.096186,0.476503,1.947536,-5.690961,-6.987652,-3.274931,-9.219525,3.147684,3.929740,4.188551,-1.500291,-2.801380,4.859073],[-8.210345,3.489018,6.742643,7.975872,5.363736,2.922087,-7.866592,-3.126998,-6.519935,-1.233569,-2.858800,2.500929,4.752383,-2.405569,8.475906],[-5.985484,-8.338872,-8.399811,8.546448,-3.603834,-2.732288,-4.543961,7.554280,-6.184479,-8.305475,-4.916634,-1.853064,-2.957397,4.723433,6.745385],[5.779611,3.587009,4.805737,0.642370,7.974590,4.973068,5.539182,-8.255106,1.563830,-1.249438,3.795551,-6.157209,-9.561781,7.149296,1.897907],[-9.826843,-5.443953,-5.687110,-5.783788,-7.500102,-6.408284,5.138830,-3.907021,-7.984173,-5.756187,3.480501,0.180839,-4.937067,-8.756504,-6.078147],[-0.525773,-4.983972,-3.329310,5.662349,-2.442788,-1.220745,1.748604,-0.567166,8.535074,6.461754,0.550449,0.794624,-0.542292,9.633487,2.137840],[3.723147,-4.677121,6.214713,-5.387864,9.674234,-4.247723,9.596201,-6.189400,2.592780,3.762137,7.771956,3.998895,0.492483,-8.540773,2.801707],[-9.395803,-8.297922,-3.417565,8.898189,-2.034525,-5.696167,-1.784149,-9.053227,4.649917,-5.704643,5.162087,-6.034598,-2.889235,-6.992282,-0.812009],[3.628999,-7.479284,6.392767,5.630929,-5.488790,-0.292703,-7.787001,-6.229178,0.954054,1.717755,-2.691405,7.372105,3.191828,7.784691,6.216898],[6.521904,-2.616281,-0.060556,5.156011,6.974919,5.628204,-8.850526,-1.137190,-6.690503,-4.079033,-3.566986,-4.937963,0.138802,5.059473,-3.350903],[-2.675987,0.093355,9.157511,0.282944,4.543777,-3.551561,-9.709188,2.186011,-5.386356,-1.217722,5.117103,8.216785,-3.914003,7.632573,0.257701],[-1.454880,-2.130938,9.681528,6.334198,-6.982128,2.798526,4.373315,4.917221,-6.420354,3.380217,-6.618109,8.520854,-7.093102,7.633245,-4.550483]],[[4.098555,-1.116624,-3.724661,-8.736385,-9.049500,6.283465,3.324679,2.229330,2.117044,-9.870982,-9.466072,9.189345,5.997802,-3.461544,2.809927],[1.863638,1.280858,-1.329194,0.603553,-8.858811,7.951685,3.527026,-4.123732,5.776190,1.252947,-2.719499,4.672659,8.800656,-8.681621,7.308762],[-9.719273,-5.590988,-4.229472,-6.187040,9.396208,-2.616961,-0.667172,-5.769928,-8.423516,-0.914897,6.458376,-7.681062,-7.836840,0.691936,1.728576],[-9.952899,-0.639681,8.782648,-3.918778,-2.129937,-6.071906,-1.391522,8.563578,-5.387653,0.714223,8.926295,8.973108,4.495300,4.492274,-7.717581],[1.977244,7.310286,-1.354714,-8.365848,-8.641195,-2.133409,2.994276,8.937404,7.062962,5.890213,-2.091192,-5.241965,-4.207184,3.377042,-3.595924],[-0.910705,-1.688902,8.968112,-0.728003,5.707436,8.990606,-3.911164,2.845709,5.809653,7.853027,6.620646,5.436685,5.472089,0.718283,0.771367],[6.645624,6.249627,3.962461,-0.774706,-8.143509,-9.948971,1.867729,9.569923,-0.366605,-6.701421,5.245891,5.765945,5.226908,-9.774866,3.646690],[-6.413952,6.720460,7.406226,2.658079,-4.280795,2.750554,5.466234,9.191863,4.339630,2.775675,6.311833,9.968183,7.317920,-9.652311,3.821641],[2.185903,-3.994253,3.023183,-3.100912,4.379827,4.783668,0.826595,7.382984,4.689514,9.101496,-5.968391,2.445762,0.348364,-7.223593,-4.241025],[-5.343331,-2.937995,-7.727583,-8.823826,-0.028697,2.292574,-1.824991,-7.133988,-0.388200,4.543981,-9.847639,-3.674686,3.810718,-3.053110,2.523893],[-7.999945,-6.151356,-6.569675,-5.600290,6.962028,-7.615169,-8.811409,-8.819223,9.295039,-0.142556,-2.680972,-6.772907,-0.394271,-5.594981,-8.268576],[4.093296,7.007850,4.427278,-0.043106,-0.030159,-1.675057,9.401154,-7.821684,1.736075,-0.782055,-4.014139,-4.110621,4.170510,-4.932674,4.073838],[-7.878163,7.078663,-4.797716,1.280437,3.242201,7.995846,1.804265,-2.144880,-2.935015,5.858749,-9.101207,7.622709,-9.177440,6.010487,-8.245730],[2.517679,-3.514724,9.801295,7.623579,0.627312,-9.284907,-6.850684,3.079634,5.220367,-3.946548,-0.370664,-2.264310,4.339804,9.681446,-8.837514],[5.822346,-9.262674,-0.075125,1.689032,-4.100472,-1.626129,6.127719,-7.019719,-6.749989,-4.691147,-5.032339,4.405495,-1.745959,-1.305922,7.968137],[6.203957,-4.458515,-5.504587,9.425089,5.420863,6.254623,1.708124,-3.561295,9.239019,1.610095,-3.828306,1.617409,0.393642,-0.269183,3.279641]],[[-1.459723,3.254574,-8.068754,5.879623,7.656840,2.001558,2.919628,0.380978,3.479864,-0.412655,-0.753393,-4.213060,-3.744878,5.689872,5.330184],[-4.686731,7.225589,6.966151,-2.562636,-9.520670,9.545000,-6.981604,-4.976324,-0.400309,-4.917851,-3.819464,8.881296,-1.643348,-0.108009,5.946904],[-6.427743,7.839393,6.247174,1.854923,-2.776060,5.491781,-6.262123,-9.289168,3.811919,-8.623901,3.128464,-5.817001,6.987738,-1.049518,-5.381289],[-1.240046,1.290050,-9.197230,-8.215277,-1.943962,8.341999,-3.388799,4.234413,-1.851320,0.646980,9.224123,-8.442600,-9.459887,-0.034083,8.403048],[-8.445639,-0.687241,-8.528349,-0.111046,-3.102326,5.738532,-4.284570,8.329102,-1.985246,-4.519115,-3.111179,-2.241496,6.557692,9.728673,1.224665],[-4.485558,-6.659907,3.203471,7.931340,0.322848,2.759721,-2.823420,-8.757936,3.318808,1.276732,-2.001681,7.175347,-2.769210,5.770715,0.773421],[2.996780,-2.872966,-9.646610,-7.495859,1.980243,9.958287,-1.215061,-8.350841,-0.391778,0.330568,8.358942,4.288149,-0.032267,1.268309,6.307693],[-6.464483,-1.019941,-9.332902,-7.150854,9.421537,-2.792605,-7.218846,-9.909704,3.504345,5.715086,-4.074235,5.062206,8.387821,-6.865681,0.694632],[7.416283,-9.263566,5.905275,-9.649755,4.796006,2.510365,9.200242,-6.411611,3.072454,-3.602303,-8.443322,3.885433,-7.356464,5.353927,-1.849551],[6.136104,-4.953419,4.368425,-2.022637,0.393158,3.105598,-2.390763,7.547838,-9.702947,-4.933944,4.028324,-2.656320,-6.145784,8.051659,6.442428],[8.331262,-3.306098,-6.192784,6.222144,8.691587,-2.086720,0.480626,1.404957,8.788552,4.673425,-8.614612,-8.563240,-4.600216,-8.326378,-1.042070],[4.489966,-7.749619,6.250213,9.136878,8.838493,4.252524,-2.008469,-3.972342,0.885990,0.323262,-0.316413,9.850386,-3.953818,7.018470,-0.853711],[-4.234249,1.446245,3.602109,1.409800,9.187894,8.430212,-9.766543,-3.872347,-7.174579,-9.282930,-5.709559,4.559987,7.273127,6.541769,-0.266158],[-7.839893,8.628738,7.742992,-4.006982,-7.840662,-6.409974,6.210666,6.038313,3.784160,0.402876,1.334549,-7.362463,-9.066226,6.899066,3.928229],[4.184498,-6.234027,5.589277,1.299367,2.875508,-1.672054,5.158741,-7.539428,9.406627,-7.094616,-9.522300,-5.374242,6.985643,-8.544370,4.475135],[-9.574109,-3.874250,5.663167,4.824597,2.188203,-7.475789,-8.281149,5.498853,-7.227050,-2.432078,-7.164374,8.040445,-0.628506,7.602309,1.405990]],[[-8.084526,8.121715,-7.915513,-5.868258,1.095977,-2.682842,3.771488,5.649477,-4.620388,9.063729,6.642348,9.626795,4.170050,1.517201,-3.372114],[9.997034,-7.512731,6.154265,8.434059,-9.897460,-8.296617,8.328449,3.950446,-4.956859,-2.658574,4.894913,0.658591,-5.618563,-5.266820,1.300205],[-0.533289,0.894166,2.079925,-0.671209,-1.231017,1.323296,5.533607,3.547246,-4.310659,-4.974570,8.079010,-7.701372,-9.755565,7.139688,-3.468198],[-6.127148,5.081645,1.571395,-5.719399,-6.189010,6.565676,8.310291,-2.925518,8.118544,0.308642,0.157469,0.128263,7.756075,2.125308,-7.377892],[-3.977989,-3.287978,-4.535245,-6.115465,2.440464,-6.725747,3.614153,-5.588479,-6.076393,-7.417469,3.090988,-7.439665,1.450360,4.928420,9.772566],[-5.496449,-2.076344,4.002438,-4.879075,8.009892,-3.029907,-0.804841,-0.776453,9.122016,9.801272,-6.449150,-8.959921,4.353193,-4.542996,-2.296086],[0.065884,3.674873,9.459468,-7.606608,1.559732,-7.795408,4.002279,7.616974,7.065905,-6.749128,-1.906011,1.232776,-9.669367,-8.184673,5.840763],[-9.604577,1.156877,-8.173599,-7.348957,-1.657799,2.019402,-8.978615,-5.204764,-2.514872,-0.125569,-8.673856,1.903464,2.362652,-8.466415,-2.246958],[-1.620679,-6.559074,0.602753,2.460096,-5.752952,8.740320,-2.763765,-7.421756,6.354475,-6.103568,-7.878384,-9.224269,-1.841695,7.519779,1.541131],[6.630137,-6.428107,9.768763,-8.022859,2.539635,-2.261955,-3.905697,-2.983174,3.632434,3.294806,-2.526346,-7.934291,5.743590,-5.370609,-7.632330],[4.760160,-9.420699,4.141819,5.890057,-2.409127,-6.338334,0.127792,1.580778,-2.134803,3.160815,-7.576913,1.461279,-5.660202,3.843611,2.819676],[-5.707293,5.861148,-0.450247,-9.434339,4.475579,-9.980941,5.557589,-8.756536,-5.365531,-1.707183,7.934243,5.338027,4.174081,4.876043,-2.212551],[-4.844983,9.481955,0.705895,8.351605,2.271477,-8.903565,-0.305222,4.098077,-6.072104,0.556263,6.744884,0.458286,8.513320,-9.712273,-7.520606],[9.282890,2.459516,-1.261434,-3.493613,-8.812028,-2.474814,-7.282342,8.679258,-1.179337,6.256218,-5.978825,-0.348604,7.382680,-9.475615,-7.384799],[-0.304566,-5.524890,4.335119,9.280926,-0.019929,7.495188,-8.735041,3.454904,-9.952412,-4.208650,-2.751609,-8.608944,-3.716848,-1.454717,-8.004912],[2.710424,2.718869,-3.930688,5.606608,-7.011176,-6.171645,-3.510871,2.755608,-4.537397,0.058616,6.972976,0.462903,-6.760200,5.203992,-2.757997]],[[-4.030367,6.076442,8.649817,-6.489705,4.136220,-2.397613,-5.797517,-8.764698,5.371803,6.390376,1.326995,-7.026742,3.628217,9.004866,7.918352],[-4.530700,6.732279,9.209444,1.478605,6.034011,2.963075,-5.734909,3.171492,3.169533,4.294974,0.181214,-1.194727,2.886047,9.561282,-1.964686],[0.787411,-3.372159,-8.146272,8.227254,5.273949,-4.384308,3.534586,-8.137218,-1.643514,5.399908,2.770582,-3.322653,-2.058984,0.225835,-1.517695],[-5.261332,-0.423029,4.877740,8.963293,-3.722571,3.520381,2.323772,-1.349081,6.722544,6.363592,-8.361419,-9.128984,-1.796467,1.048434,-4.999799],[-8.026164,3.187690,7.837808,6.243280,5.590297,7.110001,8.100423,0.601616,-8.144715,-4.124413,3.535579,-7.590022,4.129647,-4.422627,-6.079246],[0.436251,-1.848094,6.791677,8.346755,-9.446737,9.748191,2.587601,-6.032119,-4.575653,-4.237252,-5.983613,0.569834,3.912087,-9.328255,6.446949],[-2.333642,3.305326,6.450678,-4.284428,7.932160,-7.739551,-8.852509,5.622682,-9.296831,9.734400,-6.455427,5.924451,0.356675,6.443556,-5.805088],[-5.588287,4.053761,1.570147,4.694507,1.598976,-7.442069,8.271645,5.121110,2.166688,-1.334744,-4.170393,8.900191,-1.155290,-6.262479,-5.250129],[5.862119,2.754984,-0.714588,1.234602,-2.468283,-2.511604,-3.041267,7.838313,4.195484,-9.190216,-9.325125,-8.127947,-6.019919,-4.452314,-9.718245],[8.304966,1.627444,-9.014321,-3.930700,5.498708,-4.510169,0.921185,3.836827,3.400416,-7.170380,-8.913188,-6.751815,-6.930172,-4.666443,-8.074698],[3.420750,-0.206569,-9.140845,-2.776244,-3.701085,-9.969387,2.019973,-0.681036,-8.523418,6.636544,7.320291,6.744531,6.030172,-6.616166,-9.674993],[-8.730574,-7.401911,6.517808,-9.757270,1.983594,9.731164,9.636134,-3.665533,-1.674708,7.092123,2.375165,0.061042,6.135042,-6.979484,-2.161658],[-7.354856,-8.099667,2.229572,7.556076,4.783181,4.262447,-5.475055,4.651828,-0.270760,-7.768638,-9.334303,-9.533184,-9.320174,-2.334328,2.714814],[-0.888602,0.924527,-5.836334,-5.265402,-0.977585,5.532498,-7.039744,6.420844,-9.411317,5.796528,7.624423,-1.170054,-3.039440,4.835795,0.095991],[4.112084,-3.773437,-7.098670,-3.769919,6.267421,-4.283357,-4.841255,-1.673158,-1.010500,4.582449,5.489742,0.034397,-5.273977,5.205024,-9.435496],[-0.686915,-3.774788,1.453512,0.266008,3.222678,-9.250258,6.202756,-9.827018,-4.092782,-1.439883,2.117793,0.769001,4.708952,-1.575844,1.476265]],[[4.319730,-0.094199,7.430857,-1.386671,8.436330,6.639775,1.096801,-4.610487,-1.220478,4.672375,-0.554323,0.805876,6.068989,4.619452,2.941750],[6.564945,-5.352283,-0.242858,2.819325,6.833809,-4.491113,-1.244243,3.839206,3.117486,-1.567771,6.394211,2.490882,-3.832016,4.528539,-9.794764],[-5.353919,-8.252541,-4.137090,-5.132324,7.911329,-3.214677,-0.452976,-9.999232,-6.785254,-7.020139,-5.231177,1.603753,-6.850985,-2.364962,-0.701233],[-7.872851,-7.650308,3.514322,7.473244,-8.212033,9.912990,-4.810930,-9.059131,-4.160247,-1.342601,6.717897,-3.643197,3.577931,-6.313470,-5.623886],[-1.645615,1.717572,0.007885,5.930730,1.596523,-2.451505,4.483826,-2.343415,3.000628,-0.431375,8.838957,-8.067672,-2.097990,-6.089569,2.778482],[1.349284,6.947068,3.291560,-4.258940,8.717920,-7.371665,-1.189546,-7.763105,2.064096,9.394535,-0.289567,8.374965,-8.190122,-3.337739,-5.186104],[-3.615566,7.769549,0.420876,-2.187246,-3.320233,8.644692,8.391414,-1.452292,-0.862698,1.796290,1.262845,6.058573,-1.890555,-7.626811,-1.661118],[4.408705,8.465902,5.599276,3.863009,-0.623985,4.883866,-5.744656,0.845079,9.031083,6.273220,-7.189711,-8.488314,7.390242,7.970358,5.349858],[5.000004,-9.664673,8.693633,9.525510,-3.134940,-1.226038,4.350388,-5.607032,7.090192,-9.326328,7.882036,6.919935,-2.426782,-7.488675,0.084626],[-2.966365,-2.839887,5.295991,-0.889100,-6.394091,-0.580597,-3.210339,-7.326367,-5.988837,-4.632933,-1.290302,5.305512,7.926740,-1.658248,-2.891763],[2.662014,-7.274558,8.126042,-9.762020,-3.589613,-3.810502,7.568225,-5.095614,-0.480393,-9.358918,-3.489806,-3.877575,-1.063550,1.720272,5.812192],[-5.620225,-7.074789,7.144107,-7.928701,3.134542,-7.633757,6.686714,4.530209,5.949327,9.849962,-8.475859,-2.094815,7.607768,0.892538,-4.550992],[-7.492968,1.550040,0.855197,4.076492,-1.620924,6.536115,-0.161433,6.211243,-5.692275,1.707401,-7.409022,0.010963,-9.804650,5.312555,-4.607485],[0.969232,0.565769,5.897485,0.864113,-2.195699,-6.639245,-0.834899,8.129671,-0.030224,1.359424,4.230256,9.503624,-2.417965,0.503836,2.775089],[4.377856,2.919817,-0.848156,-3.154610,2.391310,0.415375,-4.358192,-8.627179,2.969034,4.931377,8.548845,-7.119292,-0.511831,-9.011975,1.257331],[2.098880,-0.727966,0.599193,0.709772,-7.204670,-2.120832,-1.317569,-8.272931,-3.932386,7.705749,-3.206974,-5.636476,-5.246724,7.603895,4.651298]],[[-4.599787,-5.248118,2.228747,0.839403,0.650362,7.597894,-9.128509,-3.031377,-0.300609,-9.479105,-9.164966,-1.286803,-7.453137,1.820702,-8.751198],[-2.325677,6.109637,0.964766,-9.732135,-7.277075,7.519188,3.300561,0.518638,-6.851266,3.836269,-6.252895,4.824862,-5.737548,5.189017,8.971610],[-5.153467,-4.157299,-4.305340,-3.974796,8.499898,-2.053376,-1.252965,-2.520355,9.986251,-6.460904,6.613153,6.615905,8.440931,-2.193746,9.203534],[-0.549077,0.241034,-8.544897,8.786928,-8.958723,5.684829,0.145301,1.848887,3.554012,-4.847298,1.768424,-3.837357,-7.773276,-6.004478,-8.222127],[-1.935952,-8.923412,-8.908783,-1.307257,4.777781,-3.845297,2.554154,5.455837,9.177533,-3.584953,-4.155336,5.125172,-1.989870,-6.940398,9.148156],[-2.442074,-5.297131,5.110531,8.269612,-8.641843,3.166428,8.909852,-0.908224,0.748039,-4.502997,5.232537,3.017323,1.157649,-9.973454,-4.320850],[7.157068,2.564552,9.858325,-3.034839,-0.635275,-2.504171,5.782701,8.263466,-4.267491,9.549791,-5.486043,8.004959,5.616460,0.900341,-5.501194],[4.650256,-8.542051,7.081491,-6.252970,1.286408,-5.008848,-8.096170,6.865067,8.766842,-8.261048,-3.102300,0.255556,-1.490982,3.296471,-4.966637],[2.160150,9.993677,0.406139,-5.972280,-6.983413,-7.725750,1.828687,-0.845523,-0.960769,-4.937381,-9.197652,9.318784,-6.126597,-1.845593,9.805017],[1.407302,5.457882,9.821892,-7.959792,-3.961089,9.998506,5.850711,8.356771,6.570645,-0.707111,-9.907433,8.434212,-3.909591,1.230360,4.862662],[-9.736688,0.262321,6.075540,-4.244292,-1.781730,-4.896777,0.819994,-0.029614,8.639706,5.374250,6.753224,-4.933399,2.101107,-0.926302,5.101356],[-4.962140,9.596451,3.067998,-3.661500,-3.133122,-0.639573,-7.656653,-9.944979,-3.345703,-7.129690,8.443100,2.102732,-0.218097,0.600862,4.896767],[-7.674134,-5.958583,-2.585940,-5.083786,3.083597,3.371512,0.328544,1.264908,3.398799,6.800673,5.787921,2.684844,-2.617558,-3.375808,5.535628],[2.105452,0.999301,3.665176,1.029431,-3.669422,-5.273675,1.739040,9.677486,3.897033,-5.771123,-3.863886,-5.722349,5.392134,-4.274742,-0.986104],[7.998303,6.172730,5.447363,-9.052613,7.751154,0.255026,8.661310,7.135206,6.056626,4.166204,-5.335490,-9.001289,0.158665,3.214070,6.084270],[5.272096,5.218317,6.482864,5.524547,-2.039689,-9.597482,-5.293141,-4.187243,-8.270609,5.700265,8.029688,1.030665,-7.764543,0.925100,-3.064703]],[[0.795702,-7.629128,4.861199,2.847873,5.326953,1.364436,0.296830,6.072592,7.264955,5.569566,8.718333,-5.524942,-4.463499,-8.768919,1.443482],[-2.523619,-6.224972,0.976695,-0.560369,0.420083,-9.618579,8.159583,-7.828995,0.994318,-7.562384,-8.109603,-6.777004,9.799334,3.962919,-3.199239],[-3.570303,0.834733,8.179741,-0.795064,7.428375,-0.645933,-6.076461,2.780492,-7.714680,9.154684,-6.342656,7.199224,-4.547716,4.029172,-3.618682],[-9.897804,4.009617,3.943742,2.606442,-5.465607,3.023624,-8.868823,0.383377,4.692629,0.815919,-2.561918,-2.081960,-8.286184,-1.584796,9.257043],[7.816824,-0.547574,6.337626,-7.917611,9.424771,-7.277117,4.905731,3.365146,-1.568205,-6.299100,4.513035,8.905406,-5.468744,-1.239953,-0.280896],[2.411975,-1.616039,-2.384480,-7.377939,-4.562948,9.503372,-7.790054,0.023211,2.309150,-6.484349,4.055792,7.182269,-7.614793,-4.182697,-4.150434],[-3.568838,4.550714,2.996026,-9.572413,-2.044462,-7.488685,5.807653,-3.849839,-0.472736,0.490610,8.227931,-8.659360,5.933401,9.161798,3.176091],[-0.734025,2.342279,-5.959940,8.458287,-8.385850,6.380206,-7.984579,-9.417596,-4.768638,-2.141315,5.005841,-1.669688,-3.718206,-1.456880,-1.315511],[-6.740523,5.437359,-8.110512,-6.118535,1.404900,0.137707,1.270230,0.619683,-0.183236,-4.736496,7.982036,-8.622424,8.366468,-5.108135,-9.881038],[-9.639846,1.675996,3.069846,1.473238,-4.164381,-0.040402,-5.379867,1.591574,9.022430,8.182700,-9.331181,-0.677679,-1.247010,-3.129606,2.156819],[2.951564,1.020677,-2.639616,-8.818148,-4.619069,-0.243320,-1.208088,8.148186,-4.112740,4.361116,-0.800992,0.467472,8.751712,6.626278,-9.860745],[-3.349012,-0.636908,-0.467202,-1.521942,-3.549934,3.491696,-2.672771,6.337944,4.833896,-2.751461,5.125477,1.429588,9.119810,2.073622,-8.277467],[-5.997605,4.895625,-7.736155,8.313607,2.967424,6.913963,-6.250978,-7.202398,3.631074,3.912217,9.533852,3.173988,4.591573,4.069054,5.641870],[-7.718168,-6.593768,-0.333946,-3.967086,-9.174465,2.240125,-8.196067,0.419184,-9.272056,9.865092,-9.330658,-1.100133,5.752960,3.545112,-9.255515],[-8.871385,-9.877088,8.780686,6.722419,-1.173141,3.604544,7.296356,3.417825,-1.950446,-5.627562,6.747034,-2.600118,-2.714955,-2.030178,-9.534611],[-6.857098,6.630186,-0.820309,0.634356,-6.031536,1.439433,9.086036,-3.964776,3.919623,-6.303802,-0.765971,-2.788082,-1.254581,-7.419049,-6.232935]],[[2.962555,3.245053,4.231211,1.404319,7.942613,-7.303743,9.589777,9.435930,-4.831670,0.956321,-5.368839,5.758177,-6.201181,6.857488,-1.356913],[-2.557447,-5.553677,-6.777369,7.234666,-1.097296,-6.331940,0.278708,6.995514,9.462734,1.887634,-9.069490,-6.121972,-7.229675,7.151902,0.270734],[-9.097585,-4.993076,4.369079,-4.196075,-6.787201,3.910620,-3.863744,6.224537,8.519113,1.512437,6.223463,7.560239,8.517000,-0.899335,7.179896],[-6.259061,0.091892,8.240007,-1.924712,0.437462,-9.743576,3.338629,9.298649,-3.302257,4.708862,2.974209,-4.352099,-0.742056,7.118263,-3.896875],[-7.237220,-6.130881,9.508351,-6.891295,2.769341,7.847554,-2.711049,-0.871982,7.647060,-2.410177,4.558720,4.399834,-1.492404,8.336261,-8.771753],[2.101439,3.320152,2.293406,4.695398,-0.443544,3.786415,-0.817968,-5.103201,-9.620923,-2.102993,-7.797246,-5.555135,8.098708,0.423047,-9.515833],[-9.201408,-8.222441,5.627028,4.519821,0.728869,-6.460002,7.639229,-3.346960,9.785064,1.551024,4.827653,7.895940,5.983404,6.818409,-8.938175],[-9.039965,5.966722,-2.064926,-3.326045,7.913143,9.470908,9.559296,-5.660400,-1.145881,-5.227064,9.913838,8.239823,3.918305,8.816175,1.283316],[6.405003,2.837459,-4.655543,6.624518,4.887002,-4.587512,-8.700123,1.331875,4.456211,8.756427,5.166196,0.389550,6.667385,0.515205,0.704323],[-8.533746,-0.065057,5.251186,5.434355,-2.921304,6.852882,1.686672,-4.043009,1.915699,-6.676060,1.158925,5.292562,-6.541629,8.322146,-8.042318],[-1.697327,6.572860,-1.149322,6.172018,-8.596609,-8.605929,-6.648886,1.159920,-9.802236,-0.277555,0.867544,-8.824058,7.307603,-4.711942,-3.242705],[3.653579,0.832510,9.285151,-0.282890,-7.825843,-4.632272,-7.430843,-2.373683,5.568679,-2.545015,-3.042124,8.820145,3.345387,6.339107,-0.224670],[-1.654595,0.470044,-7.831830,9.989039,7.508594,1.890547,-4.767530,9.226122,-7.448754,3.059505,-2.626957,-3.501542,-8.049300,-9.982024,9.452602],[2.861889,7.967623,-7.441215,9.224242,-4.917293,9.984197,4.690351,6.851321,-1.124405,8.546050,9.620003,7.616823,-3.055308,5.353723,-5.268131],[9.167812,-1.314498,-9.065756,-2.936627,-0.038512,-6.220975,7.457228,8.776792,-3.888169,-5.397068,3.573433,-7.240133,6.026635,-3.548432,4.969602],[-0.920450,-0.885988,7.066452,1.953076,-2.846103,-3.257825,0.472565,-0.641859,9.860869,-6.551429,1.848199,8.233522,6.607780,-1.108774,6.584959]],[[-7.107324,-8.484691,-5.742371,9.799419,4.037494,8.354838,-6.581934,7.711196,6.607882,-8.368942,-8.731585,9.934892,3.189102,1.361197,-9.398066],[2.263126,-8.359555,7.554624,-2.359677,-2.507306,-4.619094,8.942740,-7.378649,-4.244680,0.521623,1.676824,-2.963836,3.037313,0.866192,7.330670],[8.764084,-7.783361,-3.013676,-4.655019,-8.558591,-5.650316,-0.471746,-5.131564,4.047850,-0.525450,2.833257,-4.180296,-0.418783,8.637574,-3.614865],[3.566779,6.403163,3.771601,9.384706,-3.881545,-7.466832,6.007722,9.704895,1.115550,-7.691315,8.803278,-1.323081,0.886794,-1.823907,-1.944389],[5.036120,-5.520439,-2.101972,-8.218964,-4.157293,5.901732,7.322501,5.932203,-3.414652,8.732173,3.934386,-9.314406,4.647372,-0.274717,-6.649758],[-7.605507,2.046187,3.843503,6.590475,2.577227,-0.352750,-2.487673,4.365947,-2.682846,5.193494,-5.273823,1.209173,-3.806800,-4.957660,-7.747936],[0.783621,-6.074738,3.924803,-5.311189,0.957204,-5.571776,6.964645,-5.575064,9.153876,-9.613769,-9.096394,4.916271,-1.953160,-8.990036,-3.939550],[1.315258,-8.643009,-7.867616,9.005804,-2.563039,1.477698,6.903971,3.233163,7.497740,-8.927061,0.066096,0.904701,-4.926362,-6.108531,-7.505814],[2.408462,7.321005,-7.450180,-0.070869,-3.475875,-5.033682,9.983938,-4.794448,3.868279,0.445937,-6.206357,7.235102,3.964661,4.925990,-4.633412],[7.979461,6.864183,4.620551,-9.139382,-8.640743,-3.655535,-1.364528,-1.853207,4.599195,3.920031,2.486291,5.306969,4.846705,3.033922,4.552951],[-4.032719,7.444139,2.641745,3.904709,-4.363189,-7.791376,4.730685,2.984017,-9.629307,8.693632,8.232679,1.645881,3.897875,-9.593692,8.415287],[9.049083,-3.436201,8.362478,4.746444,7.966692,-5.152353,1.194294,3.160831,9.527845,9.421569,9.645397,-5.222218,4.647331,2.649189,-6.072674],[7.105169,-7.820379,-9.642492,5.214231,2.020795,-2.980173,7.740631,3.461138,-7.481237,-6.782053,7.715590,-1.703807,-7.414206,-7.199774,8.012674],[-5.285962,-8.086866,-8.415514,-8.096763,-0.669338,2.002270,-2.325725,-3.238727,3.559233,-2.850397,-4.917028,2.897293,3.599409,2.372259,1.188251],[-7.783964,8.798186,-2.689689,-3.619195,-9.809087,-9.985607,9.258410,-5.039553,-1.075156,-7.245425,3.994089,5.835084,5.868716,-1.676960,-9.932118],[-4.117551,8.087746,3.692527,7.009623,-2.355580,-3.458820,9.960046,0.100641,-0.958871,1.089341,3.352210,2.950718,2.853838,2.805024,7.750204]],[[2.538238,5.712445,-3.914638,1.911277,-4.498342,1.844992,-1.526722,-3.058134,-6.946292,-7.567827,3.600237,-2.776756,-8.821643,6.672907,2.538438],[5.122175,-7.266335,2.389006,7.687730,2.972001,-0.681462,-7.289416,5.922192,3.066068,3.202601,-5.471535,1.496389,-6.795124,-9.005733,6.932464],[-2.944484,7.753235,7.058185,0.065138,0.494307,-0.094841,0.539903,-8.456728,1.891671,-5.790457,5.868449,7.309267,4.068183,-4.390870,-3.164776],[8.436768,-1.990174,4.764721,1.436891,-4.585765,8.271617,6.127203,-3.115265,-0.908770,6.528465,-9.963048,6.348093,3.622512,7.843142,-3.632881],[0.354319,2.295847,-5.013187,-3.871843,8.369749,-0.543414,5.843341,-5.326338,-3.288472,-7.790512,9.999015,-2.932017,-5.943257,-4.431177,-5.403339],[5.822488,-8.106204,2.096120,-8.702802,1.531206,2.197827,-3.309053,4.414582,-5.610819,0.687020,0.225413,5.983741,7.531508,1.076616,-3.854033],[6.990427,5.746566,-7.915887,-0.438672,-5.884156,-3.448971,-2.570956,7.447434,5.693820,8.743410,-2.790679,-3.192232,-8.098803,0.918599,8.031156],[0.383773,-4.478416,-3.657246,-1.885429,3.314472,-8.884886,-8.988829,-0.493448,-4.245219,8.946873,3.946987,-0.526088,0.079197,8.886285,-4.076973],[-0.056579,4.455297,0.106686,8.740720,2.656412,-4.842176,6.822741,-9.905036,-5.625107,6.891128,-4.937877,0.109121,-3.697489,4.260312,-0.351398],[-8.374116,-6.159534,0.152122,-0.792738,3.571600,0.309911,9.339006,-7.123961,-0.398799,4.156366,-1.373246,-7.118435,-0.739853,-7.770316,3.643848],[-1.712953,-1.760789,2.067438,-4.880073,-9.409356,8.113542,8.238472,-2.670225,-7.665540,1.001965,4.134102,2.746932,8.982900,-3.006368,-4.153476],[-0.375572,-5.337328,5.348731,-9.807138,6.762341,2.161328,-4.389290,5.890591,-3.132708,-1.900986,3.969728,4.599944,4.389536,2.687063,-9.810648],[9.852207,-0.025789,3.998300,-4.779538,3.762067,8.933827,-2.218926,8.682474,-5.657767,-1.296082,6.208868,-4.297390,-8.827076,-8.440235,-3.608899],[3.519726,9.255147,8.875533,6.270214,5.230886,6.768998,8.631965,-6.687197,0.329670,-3.956808,1.443816,-9.936361,-8.741261,-7.625317,-3.238438],[-8.468393,-0.377833,8.552142,-9.118410,9.868426,6.761323,-9.161292,4.188902,9.933654,-5.920247,-6.907917,-4.307717,7.474876,9.752218,8.017160],[-5.368698,-0.485857,3.686702,-6.529767,-4.657447,7.135369,-0.616668,5.432071,0.828299,2.253509,-9.431086,0.031766,-9.733235,-1.336662,-8.738746]],[[6.821815,8.631022,-3.699747,5.058008,-0.768740,-7.225198,4.262117,-6.674007,-4.090572,2.975744,2.111600,9.354877,-8.868011,0.902455,-9.866312],[-7.833572,5.250527,9.076587,4.893670,-9.104353,-5.411428,6.098142,-7.876323,-1.225048,5.332141,-8.624336,-2.225277,-1.856299,3.007969,5.243410],[2.163953,9.622887,9.188214,-1.299331,2.853554,-7.566781,-0.852056,7.514982,5.735584,0.053109,0.583513,1.374270,-0.662525,8.946757,-9.917370],[5.984968,-6.412931,-9.689866,4.535772,-6.376699,4.361585,-6.699723,0.458484,-9.233564,-9.221126,7.631115,7.914557,5.077171,-1.578199,3.952661],[2.860154,0.326257,8.580555,7.574199,-4.706279,6.708089,-3.877565,4.870882,1.235100,6.222006,-8.329365,-7.159635,4.562571,8.693530,-8.770911],[-9.420521,9.673700,7.968207,9.763696,2.569286,7.953200,-9.245757,-8.734321,8.607367,8.825801,5.328344,2.648884,-7.095438,9.174268,5.220572],[-3.810644,0.427730,6.605480,7.806844,6.948680,-6.123761,2.528224,9.141129,4.351351,-5.614176,1.845620,-3.074438,6.763159,6.837257,-6.809038],[-3.898936,8.928622,-8.290261,-8.554763,6.830654,-7.858669,-0.196323,-4.643385,7.766985,-9.928644,8.949110,-1.907889,9.459650,-4.584944,-8.976820],[0.506852,9.552559,3.770976,8.656527,2.902427,3.442063,-9.165364,-9.619185,3.270909,-9.461735,3.046291,0.648923,8.156549,8.682475,-7.783815],[-3.768939,-9.853922,-0.661051,2.573076,9.976714,-2.943014,-7.833862,7.040165,-8.996065,2.294461,-3.945937,-4.531549,-5.859520,-8.361095,0.781959],[8.896399,-9.951297,2.110601,7.145607,-5.816918,-3.178461,-2.883779,-6.018537,4.338438,-4.227597,5.593804,2.783090,5.940894,-9.264671,9.058644],[-4.402658,5.322207,-1.646372,1.038428,-6.067920,-4.173486,-9.126672,7.949731,-5.450990,9.930769,4.651991,-8.390654,-6.873941,-9.830131,6.346865],[-1.413892,1.498133,9.871478,9.722286,2.124868,-7.137992,-8.879311,-2.780496,1.294644,-4.952122,-7.076762,-7.581288,-5.485254,-8.987698,3.196841],[-1.029385,2.210050,3.601342,9.486093,7.009559,-7.105277,-8.753548,-7.232257,1.006545,-9.114234,6.068111,9.722777,9.177530,-5.700363,6.263437],[6.623054,-4.728314,1.495281,7.012444,-6.250132,8.063725,2.616944,6.327201,3.895257,4.960298,-1.988076,-9.617307,-9.280405,0.709963,3.682551],[-9.100158,-1.107591,8.257902,4.603007,-0.973300,7.461262,-6.744167,4.761647,-6.804770,-7.318376,-4.887660,-0.512472,3.485681,-6.084422,-5.369469]],[[8.235095,0.324959,2.336668,3.083977,1.473276,-9.715229,8.391107,0.685098,-3.627367,5.731733,-7.844034,0.061468,-8.846872,3.756301,7.824557],[-0.416201,6.222152,-4.187826,-0.900776,2.189591,7.872192,-4.151714,-7.162491,3.467437,-6.960151,-3.712123,1.172998,9.341481,-7.481165,-4.372841],[-9.540054,-8.848999,-7.843546,-3.527412,-5.919077,8.668324,8.194261,-3.167151,0.372556,-4.056905,4.500596,-8.339537,-7.969757,-9.241945,7.269643],[-9.413421,-4.397472,6.429109,5.499076,7.202833,8.113167,8.360826,6.996546,-5.684823,-4.923266,-4.831999,6.564360,-3.193361,-2.528772,-5.841134],[7.691934,-9.381569,9.244747,5.192081,5.717481,-1.144731,0.960888,-3.633035,-6.465698,1.165084,7.340249,-6.737113,0.189571,2.903069,5.009213],[2.033880,-5.403218,-6.439411,5.890076,3.189607,1.226344,4.916285,3.727283,4.576686,-6.137115,-9.205884,-7.248420,6.242165,9.926614,7.742574],[-5.975409,-2.952122,-4.056985,4.085772,-4.126410,7.333491,-2.155683,-3.668678,-2.709639,1.184876,-6.028239,-3.215022,-6.497699,-5.098734,-1.364491],[9.669120,-6.664665,-8.454883,-8.285881,-5.576269,-5.562667,-8.551660,-2.187019,-6.488188,-0.652861,-6.328878,-7.218202,8.278788,-6.942638,-4.608403],[-2.802883,6.313069,7.503496,2.774061,2.514200,-6.639821,1.831163,0.050639,4.812124,-7.065820,2.620058,9.351484,-0.708553,8.248814,-3.137941],[7.709188,6.364105,-7.935126,-9.178667,-1.113375,2.910731,1.102202,-2.602178,1.864386,9.092042,6.142492,-4.895867,-4.858454,-6.278140,9.833909],[6.457358,3.277198,1.359933,-8.203305,8.455735,-8.832966,1.291953,-4.019251,-5.885460,-6.446768,4.290782,-8.804637,-7.954972,-1.832267,-4.241126],[5.103404,8.572571,-1.956194,-6.587329,-7.349012,-0.433128,1.178730,9.467780,8.282093,3.748597,7.702746,0.951953,-1.777176,-3.484383,-9.468404],[-7.211403,-2.728457,-1.202038,-5.117674,6.372612,5.069303,2.106105,-7.898451,-6.817131,-5.082430,7.785759,-0.364324,-8.687046,-4.009266,-3.572317],[3.645972,-9.459114,-2.899799,8.833906,-9.747650,6.768400,-0.365382,-0.165869,3.644987,-3.642035,-0.054311,4.077188,-0.294646,8.164319,-4.111062],[-6.630226,-7.531879,-3.931361,0.331915,2.273359,-4.698118,4.315809,-6.785149,3.030167,-4.896742,5.690410,1.957961,-2.879379,-6.539609,-1.205772],[1.409131,6.236441,-3.367707,-7.105481,9.784392,2.592925,-5.551550,-9.487593,-1.745673,5.651660,0.960599,5.399129,7.003213,-9.876288,5.231263]],[[6.971470,7.806176,-8.053950,-9.423428,-7.879418,-4.857165,5.849619,-6.311186,2.134212,-1.576437,-1.686918,-3.889954,-9.943246,7.680045,8.799667],[-3.127208,8.111740,8.326131,1.122569,-3.454263,2.104798,0.359253,2.801772,-5.676706,-6.698573,8.582557,-2.427227,-7.478652,-4.083538,-0.434223],[-2.467458,-3.250609,-6.853025,0.872677,0.338146,1.497124,-1.637603,1.108746,1.520437,6.284742,-0.472902,-1.225388,-4.157427,-2.042574,-5.251836],[-8.786532,0.833747,-7.221801,2.626719,8.802979,4.158393,8.251184,0.513786,3.015874,3.267742,-3.893763,-6.212557,-8.354309,3.135106,7.147541],[1.715643,-7.701230,-0.203142,4.761195,-8.108725,-2.176454,7.471479,7.786865,-1.126316,9.426540,5.478436,-5.792611,-9.244403,-7.039649,2.675461],[8.081492,-5.870862,7.461746,-8.913252,-7.278754,5.575906,-4.143596,-0.498219,3.541878,9.326521,-3.157414,-7.646110,-0.973623,-8.108780,-7.338457],[-5.410298,-0.715058,9.405458,6.768521,-4.798127,-1.895187,-6.908385,3.474031,-4.196338,8.053211,5.704424,9.856972,-2.640167,0.986761,-7.873630],[-9.926967,7.114716,0.595728,-0.366456,5.067708,-5.212495,-7.514984,-0.634212,-2.389325,-3.970943,-4.104068,9.098294,7.106881,9.136930,-4.091981],[-0.265045,-7.282383,-2.932783,-0.313901,-8.728380,1.025081,6.482411,8.099045,6.575516,4.495263,-3.107614,-4.861690,8.262957,2.932206,-3.486014],[-3.032583,7.939024,-8.640548,0.191827,-0.021732,-9.396772,-3.382153,-6.016325,-8.337872,6.778584,9.109700,5.545269,-0.611277,-6.452585,-6.813424],[9.984262,6.545878,3.345385,-8.985635,9.244496,1.846805,3.451725,0.423988,2.050830,6.774859,6.833108,-6.785952,-8.405468,3.988940,5.549788],[7.681193,6.905695,5.444553,5.606018,9.842764,-0.682073,-4.742699,-9.056042,9.871623,3.888051,7.402552,-4.478870,-0.025791,-8.465419,1.360316],[1.238092,-4.472962,2.936981,4.056154,-8.754974,2.458687,6.747748,-6.616947,-1.541901,-3.285036,-0.734440,-8.839745,7.017789,-1.542083,0.373450],[3.403996,-2.113331,6.972143,5.300142,-5.884132,5.372225,2.907052,-2.886027,-0.420275,0.116001,-1.824858,-8.702513,-8.713322,7.083721,9.398889],[-1.569670,9.726179,7.975191,9.080701,-6.964753,-9.322123,5.322816,-4.427501,5.495218,-8.252488,3.721831,-9.230733,-4.314802,-3.199023,1.366716],[-5.581181,-0.481162,4.728353,-0.979391,8.377071,-9.162548,-1.425253,5.103471,4.261453,1.235621,5.852701,0.064508,4.453433,3.925519,7.952361]],[[0.909684,-8.290669,-0.193851,8.040663,-4.607722,9.464134,-0.211744,2.246435,-7.383264,-0.270836,-5.780769,3.941376,-4.927728,4.148726,-9.280478],[-8.299285,-2.384653,2.287277,-9.912909,1.557620,9.328898,-3.359195,-4.642664,0.574137,-7.836648,5.856170,-0.302103,-4.690097,1.070495,-0.950951],[2.507078,3.990224,1.839036,-5.147210,-8.153568,2.868549,-6.987481,7.335532,7.609644,1.088615,1.691741,-7.623115,4.260404,-4.715188,0.551011],[-5.554631,8.542328,-8.792705,4.170308,5.946861,2.751189,6.554412,-2.271027,-0.260773,-6.952153,0.891512,-7.539262,1.287698,2.725174,-3.414698],[-6.934396,1.001816,2.547860,-8.333561,-0.492729,-6.839566,-5.947245,3.067062,-1.981578,-3.999284,6.128268,-5.743871,-5.762269,-3.097231,4.701245],[-0.578829,0.192740,-5.703572,3.956873,8.919599,-9.282407,8.417013,-7.472384,1.838260,3.441030,7.259015,3.344294,-0.774910,9.763744,5.424159],[-6.779335,-6.698522,4.887791,-7.181329,4.072652,-2.889632,1.055782,0.135252,-6.234533,-4.052239,-5.251999,4.698978,-0.176875,4.961083,-6.571980],[-6.764273,-9.203150,-6.817190,1.009365,0.220157,2.575305,-7.572886,4.173068,-5.012880,-5.344447,3.187204,-1.899690,6.456615,6.748944,-9.056043],[7.858765,-1.036163,0.806573,-8.511480,4.372832,3.648546,9.015625,8.244682,9.787867,8.307935,-8.563206,1.513628,5.903484,8.492734,1.202949],[-4.302807,9.425937,1.059289,5.599796,2.893141,6.422409,8.245987,0.317263,9.897139,-6.521032,-2.065756,-6.600527,9.363656,-7.267542,-1.578766],[-3.373291,6.012910,0.530446,-1.300771,-9.538149,6.198096,2.436665,-5.044252,8.191274,5.662656,-1.501548,-7.714765,6.315419,-4.820861,3.308997],[-8.843252,7.144786,0.390742,-8.339642,-6.035450,4.205327,-3.410659,-4.670541,5.634506,-8.449984,-8.413083,3.376305,5.988300,-1.111441,-9.442904],[-7.481229,-1.657091,-4.214431,-6.352675,1.495040,2.320527,-3.649963,6.723775,2.686219,-5.370754,-1.677872,-9.144282,-5.473968,-7.184739,-1.375064],[-5.735087,0.357694,-7.113952,-3.109110,-3.726381,9.516381,-9.047255,9.818485,6.409399,3.036019,1.059729,-0.068273,4.996376,2.094685,9.578457],[-3.057133,0.391810,-6.420761,-3.022035,-8.127286,2.190814,-5.887010,-9.230334,7.610028,-1.133653,6.152707,-2.836242,-7.354606,-4.420850,-6.755408],[8.396499,2.003621,-6.527728,-6.852806,-5.631459,-0.278655,5.657521,-0.795862,-8.617957,6.857426,-6.437000,-5.947760,-5.539667,-6.224619,7.289062]],[[-2.341013,3.084839,4.941052,-3.029319,-8.649139,-3.656050,-1.392678,-9.276121,0.125173,-5.791601,8.206893,-4.912761,-8.121782,-2.108416,7.525128],[4.392758,-1.384577,-5.042707,-5.744511,-5.868393,7.434630,1.978810,-7.091510,-4.192074,1.596220,-9.909545,1.566248,-7.517859,3.334621,-4.754486],[-7.349358,-5.109240,1.300415,-0.904473,6.812385,-8.076403,-4.899109,-2.924167,3.523040,-5.618463,-2.683971,-1.937189,6.449057,5.098395,9.957254],[-2.833975,9.441584,2.930854,5.504105,-5.576868,-9.433118,0.484569,0.612040,5.384421,2.983846,1.498013,-7.329990,1.604513,-5.741761,-4.952839],[4.394234,-6.854855,5.829778,0.391497,8.111710,-7.686425,-4.946486,-3.309985,6.266936,7.604319,-9.341300,-1.303054,-7.708900,-6.058232,-8.387803],[-6.446338,4.044565,-1.007219,-1.940258,4.052343,-7.722283,6.084176,-3.476795,-6.116628,0.960454,-8.693607,-4.047569,-2.154708,-5.419059,5.902560],[4.899268,-1.654955,-8.485494,-0.071315,-3.561705,2.345514,1.889433,-0.210765,-9.135892,6.395213,-3.308526,7.825569,6.363866,0.491501,7.673969],[-9.508617,-3.269709,3.824209,-6.408739,-9.963966,-8.437151,7.851549,-7.516259,1.909268,-8.424239,8.048213,-2.912492,1.598961,-9.332322,3.399419],[4.096889,4.389584,5.400976,7.383383,-7.429423,-6.117415,8.910246,-7.958262,8.480810,-6.375061,-8.093064,-0.899346,9.858982,-1.694094,-5.223285],[2.920056,-4.419672,-2.469921,6.365677,7.088897,4.578957,-6.580899,9.628470,-8.539413,-8.594462,-9.880634,-5.156006,9.898644,-2.882446,-0.741177],[-4.303733,-9.269411,-1.425982,-2.018061,-5.779164,3.541206,2.942075,-9.305686,-4.393688,-7.561862,-8.481585,4.678770,0.938228,-3.935421,4.845945],[0.198561,-7.224527,-6.966167,-8.196590,-2.578324,-9.516940,-0.697455,-1.973743,-1.680988,1.795610,6.409218,2.139859,4.689498,-9.442826,-7.270812],[-1.498327,4.071077,0.282901,2.403503,-7.318288,1.531691,4.647852,-4.839849,-3.726692,-1.702834,7.486788,2.868009,-6.298493,-4.241799,-6.432815],[-9.899337,-7.449698,7.059745,1.169541,5.343458,0.149466,-9.859795,-6.240074,-9.035058,4.684317,-2.440000,-6.573404,1.544414,-8.734987,3.622351],[-7.671524,7.067992,9.351398,7.767480,1.470726,-6.288228,6.831844,9.280678,-3.348056,-7.551826,-0.326411,-1.639531,6.274172,-9.636405,7.926270],[-1.391827,9.700714,-4.165828,7.927573,-1.535893,-8.213575,1.002551,7.270223,7.392464,-0.847546,-1.751071,6.994312,1.560519,-1.061008,-1.320698]]], dtype = "float64")#candidate|4301|(16, 16, 15)|const|float64
uop_4302 = relay.atan(const_4301.astype('float64')) # shape=(16, 16, 15)
func_618_call = mod.get_global_var('func_618')
func_622_call = mutated_mod.get_global_var('func_622')
const_4317 = relay.const([-9.532505,5.742980,-5.663020,9.603558,-2.469893,9.573586,-6.896594,-8.324026,-1.337532,-2.597367,-1.643576,-1.086756,0.735153,-4.876769,8.687127,9.775369,-1.580343,-2.935172,-5.145134,-9.691699,7.119876,-3.283720,3.039340,3.839362,-1.603488,5.459534,-3.940541,6.731193,-8.164173,8.172997,5.767059,0.556522,2.855867,1.452221,8.249605,9.799554,6.102075,-9.858132,-2.914852,-2.731422,-4.125544,6.943655,3.209111,-7.691989,-9.533174,8.763906,-9.136722,0.894919,7.105131,0.123149,-0.262433,4.358979,-3.352030,-1.458419,4.223285,-3.723017,-7.047811,3.311199,-0.435284,-1.332844], dtype = "float64")#candidate|4317|(60,)|const|float64
const_4318 = relay.const([-2.887993,2.863672,2.110419,5.188202,8.242653,4.124303,-6.787952,-1.486854,-9.615774,7.801980,-2.571079,-1.085156,-3.085129,1.826723,7.979185,5.507389,9.651087,1.492645,5.688336,-7.643772,7.528902,7.001167,3.061750,-8.329552,-2.951042,7.372797,-6.001779,0.759580,-9.474061,-8.830941,6.096064,9.686521,-0.890435,9.108157,3.758953,9.318948,2.956138,3.042480,-5.566506,-4.084088,8.195217,-2.230497,-3.084667,3.395963,-9.312705,-4.515476,5.188458,3.022135,-3.178772,-2.160495,-1.430080,-6.099072,-1.323506,4.196543,9.475296,7.729478,7.443575,-1.188155,3.304922,-6.506967,1.877125,-9.405478,-1.104755,5.544158,-5.800130,3.696814,5.021763,2.501580,7.068912,-6.154427,-4.375718,9.060022,6.188843,9.712295,0.908686,5.810564,-6.033694,-1.660204,3.609854,4.021098,1.161183,-4.546310,1.297408,-3.550859,-0.232341,7.374680,-8.964692,-7.705813,4.404206,-6.267257,0.709159,5.430511,6.878059,0.122969,5.084998,9.267918,1.634893,0.814461,1.867168,0.614335,8.467648,-1.474686,4.291857,4.733633,1.741422,-5.565568,4.440903,-4.285752,3.308881,3.247486,3.452365,8.552855,2.653413,7.712545,-6.107072,-8.197284,6.447178,5.323630,-7.623241,2.991012,-0.197417,-6.320982,-1.683839,8.057175,-1.063430,-9.154757], dtype = "float32")#candidate|4318|(126,)|const|float32
call_4316 = relay.TupleGetItem(func_618_call(relay.reshape(const_4317.astype('float64'), [5, 3, 4]), relay.reshape(const_4318.astype('float32'), [126,]), ), 4)
call_4319 = relay.TupleGetItem(func_622_call(relay.reshape(const_4317.astype('float64'), [5, 3, 4]), relay.reshape(const_4318.astype('float32'), [126,]), ), 4)
output = relay.Tuple([uop_4302,call_4316,const_4317,const_4318,])
output2 = relay.Tuple([uop_4302,call_4319,const_4317,const_4318,])
func_4325 = relay.Function([], output)
mod['func_4325'] = func_4325
mod = relay.transform.InferType()(mod)
output = func_4325()
func_4326 = relay.Function([], output)
mutated_mod['func_4326'] = func_4326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4325_call = mod.get_global_var('func_4325')
func_4326_call = mutated_mod.get_global_var('func_4326')
call_4368 = relay.TupleGetItem(func_4325_call(), 3)
call_4369 = relay.TupleGetItem(func_4326_call(), 3)
func_921_call = mod.get_global_var('func_921')
func_923_call = mutated_mod.get_global_var('func_923')
const_4372 = relay.const(-10, dtype = "int16")#candidate|4372|()|const|int16
call_4371 = relay.TupleGetItem(func_921_call(relay.reshape(const_4372.astype('int16'), [])), 0)
call_4373 = relay.TupleGetItem(func_923_call(relay.reshape(const_4372.astype('int16'), [])), 0)
output = relay.Tuple([call_4368,call_4371,const_4372,])
output2 = relay.Tuple([call_4369,call_4373,const_4372,])
func_4386 = relay.Function([], output)
mod['func_4386'] = func_4386
mod = relay.transform.InferType()(mod)
mutated_mod['func_4386'] = func_4386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4386_call = mutated_mod.get_global_var('func_4386')
call_4387 = func_4386_call()
output = call_4387
func_4388 = relay.Function([], output)
mutated_mod['func_4388'] = func_4388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4386_call = mod.get_global_var('func_4386')
func_4388_call = mutated_mod.get_global_var('func_4388')
call_4440 = relay.TupleGetItem(func_4386_call(), 2)
call_4441 = relay.TupleGetItem(func_4388_call(), 2)
output = relay.Tuple([call_4440,])
output2 = relay.Tuple([call_4441,])
func_4446 = relay.Function([], output)
mod['func_4446'] = func_4446
mod = relay.transform.InferType()(mod)
output = func_4446()
func_4447 = relay.Function([], output)
mutated_mod['func_4447'] = func_4447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4446_call = mod.get_global_var('func_4446')
func_4447_call = mutated_mod.get_global_var('func_4447')
call_4466 = relay.TupleGetItem(func_4446_call(), 0)
call_4467 = relay.TupleGetItem(func_4447_call(), 0)
func_3334_call = mod.get_global_var('func_3334')
func_3338_call = mutated_mod.get_global_var('func_3338')
var_4472 = relay.var("var_4472", dtype = "bool", shape = (588, 1))#candidate|4472|(588, 1)|var|bool
var_4473 = relay.var("var_4473", dtype = "float32", shape = (126,))#candidate|4473|(126,)|var|float32
const_4474 = relay.const([-5.002068,-2.596273,5.618932,0.509586,-4.420148,6.550201,-3.525736,1.494045,1.543761,7.704937,-1.850240,9.133678,0.388479,-0.155041,-9.363870,-4.119161,8.502571,6.201039,-0.499232,-5.362027,-5.817957,-3.277406,-3.542108,6.899813,6.158779,6.099280,-3.984183,-9.754603,2.898499,-1.933347,7.809264,-6.091476,5.824089,1.532741,-2.499420,-1.211831,0.530678,3.410030,-7.781620,-5.816521,9.961955,6.719106,-7.653761,-4.867061,-4.594383,4.674614,6.340401,7.958896,2.133354,-0.640581,-8.655748,-6.986920,4.564000,1.456082,-2.490174,-2.421047,7.656356,3.095929,4.172937,4.134932,-1.624808,1.457837,-4.637487,0.122421,1.807855,3.242781,-5.348222,-6.591268,-0.366788,-5.603927,2.435992,-6.774231,-7.008270,-2.748195,7.822523,-7.014032,-0.411485,-6.782222,-9.505125,4.483652,3.213270,3.633635,-8.806398,-8.823375,0.007741,-2.871284,7.163999,6.762682,-3.426745,9.999120,8.883169,-6.992344,-2.287288,-7.671846,-1.773038,-4.209981,-0.139299,0.584155,5.462160,4.747163,-5.313586,7.229923,3.270318,-9.129649,-2.728066,1.459285,5.023587,-9.292064,-2.529212,-7.028248,-4.239620,5.883147,-0.603022,3.229976,-0.529343,-8.630736,-4.768728,-7.715041,-2.470187,-0.161113,-1.348180,-1.807523,3.485070,6.523802,1.315605,-7.611605,3.720051,-1.881508,-8.245220,3.677992,3.168089,-4.631780,-0.782722,1.244559,0.551809,8.832841,6.632954,2.292281,-9.072761,4.348459,-7.415221,7.265611,6.851880,5.193800,-5.284061,-0.373228,-4.943231,6.770265,6.814157,0.179792,-9.967768,-1.231210,-6.084895,-4.028682,5.630223,-1.103205,8.692725,2.252074,5.361481,3.531639,2.162921,0.541120,-5.141500,-5.141528,9.902336,-0.910925,4.253788,-5.661895,-5.057474,-6.264496,-4.983372,6.560756,3.710450,-6.690964,1.987958,-7.585492,6.871430,-2.147919,-4.077008,2.932731,-5.780004,-8.847446,-1.353729,3.712200,2.175899,-4.608078,-4.132968,-3.073718,-8.391516,-9.733906,-4.057853,9.037916,8.364294,3.411997,-0.399669,1.675988,-0.784252,-5.385120,-9.127037,1.482114,-2.055948,0.116627,3.175174,-4.038771,-9.148959,2.629187,6.792584,-3.332725,-5.867631,-5.934774,-6.369783,8.699036,3.873682,-0.232231,2.074739,-1.112318,2.209769,-7.863020,4.928437,7.653129,4.136227,-6.786817,9.033250,8.493221,-7.356903,-5.107288,-1.773940,6.908666,-6.601312,0.094324,2.219885,1.412077,-2.792104,8.494865,-9.205593,0.706910,1.692891,-3.488572,8.179177,-3.953833,1.422949,-2.405029,-7.361732,-5.795052,9.303523,-0.827029,4.995680,-1.881898,9.753018,1.541805,-3.669814,2.731353,-8.548981,-0.756699,-3.795668,9.018541,7.119892,0.762180,4.039763,-6.903075,8.381541,5.308603,-2.142951,-6.352640,4.254550,8.522239,8.439722,1.855067,-8.413474,1.549730,-1.573071,2.093165,-7.314383,5.247228,-0.097568,5.222315,-7.530507,-7.565602,-3.086188,-2.045514,-5.437918,9.917561,-3.596928,9.664801,-4.174538,4.505434,1.522853,-0.328063,2.686804,2.051083,-4.031134,-9.566717,1.947306,6.095368,1.911120,7.589713,-4.080930,0.974883,1.187355,1.716101,8.760638,-1.743402,0.317260,1.511542,-3.977602,-9.275380,0.802898,9.922044,9.528631,-1.397513,-4.205887,-6.499110,-4.625366,2.515246,-6.690506,0.221114,-8.340838,-7.190149,-4.521413,-5.488437,-4.831963,5.074524,8.939202,-9.807602,-1.792981,-8.866164,-5.903287,5.824470,-8.380086,-0.613043,6.864113,7.265754,7.210559,-0.713969,5.007157,-2.058550,1.145583,2.593720,-5.822692,-4.375072,-7.748171,1.477925,9.563961,2.207554,-8.283224,1.257637,7.894053,4.942007,-7.557816,-2.990936,-0.131545,-8.347512,9.513005,5.818583,6.133324,-6.202842,-2.816431,9.851792,-9.410512,0.271783,-9.289932,-0.037479,8.128413,7.644171,2.956553,8.701408,-5.646440,-0.760426,0.096734,-5.543670,5.261004,-2.689995,-0.787244,8.421722,-6.044934,7.817537,0.264930,-7.453974,6.282291,7.868393,-9.377244,3.627126,-7.211628,-4.536561,4.449664,-3.023383,0.222142,-9.014253,-6.979539,-3.270677,-7.224099,-0.255646,9.923226,9.434746,-7.455131,-4.496008,5.658672,6.054829,2.782481,-4.498424,-0.814578,2.872958,3.661156,-6.166416,7.616928,4.257329,-5.476139,-8.126286,-5.623489,0.700896,-5.103979,6.919920,7.401041,9.285725,-3.673742,0.443443,-0.250010,-1.635110,-7.566790,-7.919713,2.970458,3.572428,1.354925,-6.719429,0.935356,-1.322817,3.353617,-8.185710,-8.811525,7.392502,2.257838,-0.513915,0.841766,2.565329,4.271095,6.319201,8.323425,-0.788867,-2.277793,8.663775,-5.111358,5.643475,5.893597,-3.693653,1.991592,3.923598,-4.346817,0.652074,-9.806487,0.528300,-9.657372,1.092455,-8.003282,-4.855081,-6.602431,-4.506815,5.833735,-9.758939,5.374867,-5.853763,-4.556470,4.141170,8.025440,-6.048097,-3.927983,1.883823,-0.731550,-6.370331,1.373751,-2.496996,-8.725488,-1.627734,-2.688044,2.324527,-5.387020,7.242604,8.456125,3.012786,5.806959,-9.839346,-9.766356,-4.564122,-4.220973,9.750626,5.584401,6.232354,-8.449527,1.945109,-8.622981,0.731042,-6.929374,2.816733,5.593794,4.386037,-6.965823,-3.447343,9.001077,-4.562882,-7.597565,5.016294,1.321037,8.694374,5.459707,-7.281683,6.661288,-9.952526,-5.288367,7.828747,-6.973360,-1.937491,5.384157,9.449065,3.545337,-0.519422,1.179073,6.073376,9.982723,4.420399,3.728653,-6.825939,1.870231,7.609189,1.677910,5.078559,7.203554,-3.991187,6.338929,4.711495,5.462665,-9.081647,-7.263264,2.671920,-8.650475,-5.785160,3.458173,6.389196,3.304968,-2.464770,6.663134,-7.031506,-1.664048,2.560932,3.716334,-5.742647,4.455477,6.320298,2.438875,9.700171,7.166962,1.137409,-4.234940,2.556285,2.310950,-3.851766,-3.182837,3.038492,-2.427632,-4.032970,-0.713640,-3.881825,0.398575,9.006263,6.580860,-1.728186,-1.110920,3.168213,-2.764779,-5.717332,-5.555384,8.457232,7.474315,3.434223,9.662584,8.827222,5.320808,7.078740,-6.791720,3.158011,3.300340,-1.726075,5.264274,8.444013,6.556670,-8.396050,-8.242221,-1.367907,-8.743656,0.674800,3.975453,3.534607,1.109981,3.428642,4.548829,4.596862,-5.751221,-4.928900,7.192342,-5.515660,5.061360,-6.476920,-6.979586,-0.327523,5.335592,-3.228270,-1.666044,0.963760,0.123438,2.828197,4.392429,0.267720,4.773712,7.636603,4.913979,5.890913,-0.796036,2.542370,-3.015679,-5.408444,3.678770,-5.796742,-9.330433,7.696459,-7.068659,2.788175,2.143590,6.849301,-8.050845,5.809825,-4.945306,7.463427,7.808283,8.654467,-7.501495,7.524420,3.269486,4.892691,5.166839,3.906326,-0.234061,2.261320,8.546125,-8.284393,2.475843,-1.126754,-8.307186,9.714825,-9.592812,5.356329,-3.286107,-8.190033,-0.865695,0.089440,0.012952,2.312060,0.394047,5.348167,7.160802,5.859983,-2.353065,5.652701,4.766577,-3.468983,1.404143,-0.431863,-4.174314,4.421376,-9.776706,-7.968772,3.034043,9.172436,-5.842354,-1.631205,-0.590516,-8.428656,9.062581,2.687245,-5.898714,-5.459924,7.911285,6.819272,7.936860,-0.121403,-8.841087,1.413773,-3.343096,-6.687042,-7.950379,5.975191,-7.856547,7.465198,2.098198,-4.071274,-3.525092,9.978369,1.762349,7.797803,-7.941732,7.657194,-1.514364,-0.491396,2.507414,4.615678,8.502555,2.990881,-1.988595,7.375137,4.043348,-3.146354,-6.005952,-2.521642,-5.412370,5.446620,5.454630,8.165605,0.981050,5.030077,1.198466,-5.467636,8.760860,-0.686506,-5.890495,4.595413,-0.851338,8.635881,6.134050,-9.100113,0.959029,-7.514483,-2.809892,-9.098992,-8.570161,5.005022,-7.370521,-6.621015,7.459933,-9.663733,4.068717,0.181673,3.464531,-0.403943,-3.470732,-8.087560,-4.404600,0.002312,2.949050,0.284627,6.353501,7.522332,-8.008719,7.669370,-9.420453,-9.323840,7.638609,3.718761,-8.502561,2.945214,6.854426,5.356716,7.299585,-2.906924,-2.726459,-7.162240,-7.175981,-2.574406,0.195034,-1.413215,5.480086,5.596771,4.970380,5.293861,1.974458,-6.310462,-6.162902,-3.001927,-7.250842,-8.328332,-8.832177,-1.291080,-2.781245,-9.180799,-6.387914,-3.315750,5.051699,-0.594538,-1.693119,-4.085987,3.266910,-2.236261,-7.364757,5.859399,-3.307047,-0.803702,-1.449352,0.872378,9.481925,-1.969359,2.173487,1.276624,1.278124,4.289998,7.819408,8.724806,-0.418481,-9.310009,-7.547122,-7.167661,-6.371424,-3.470744,2.452199,5.001519,8.829272,1.332278,-0.015226,2.285055,-5.526588,-1.001773,-9.812203,-1.420959,1.836358,-8.563057,-8.666840,-9.675956,7.562112,7.310701,3.539369,4.753480,8.035837,2.218410,0.235116,4.830193,8.478602,6.340211,8.763241,-1.307683,-8.160345,-2.915214,3.883421,6.540640,3.680334,-6.789544,-4.310614,3.598836,-1.249306,0.459159,6.493044,6.159589,-3.279358,4.858052,2.357030,6.012778,-9.969156,-5.099564,-0.638300,-7.885084,8.295720,-8.589400,-7.537594,4.802781,-9.921564,-6.987119,0.364374,-0.557509,-0.157926,8.618064,-6.841842,9.495521,-3.613677,-6.802568,-6.063110,5.065764,1.449248,1.195601,5.446772,-6.338347,2.036897,-3.084864,5.280058,0.428044,-2.622374,9.470461,6.374543,0.518638,-0.981833,-2.220959,-0.762338,-5.756667,-9.223326,1.180788,-7.911772,0.872525,-8.169042,-6.244877,6.083821,5.372952,-8.665972,-0.490848,7.370752,-6.037754,5.866705,-3.062710,-8.714704,-4.500407,-7.862816,-0.426986,1.610963,6.007786,2.071956,8.558944,8.591713,-1.428249,1.605084,8.002456,-1.524217,8.120573,-2.212721,9.874796,-3.890480,0.880898,4.737697,-6.715468,-3.160785,-4.796099,7.599453,-1.514880,-8.068974,1.390933,6.411227,4.274450,-9.175536,6.919805,-8.502356,5.123907,-6.607535,-9.182307,-5.761089,5.505631,-9.208726,1.106284,7.817629,-1.284292,-9.586718,-0.187022,-0.182955,-4.213887,-0.687424,6.019090,-8.215272,5.360891,-5.695536,4.641622,-4.224427,1.477585,-5.993917,1.271072,-5.432218,-5.775400,1.460758,-3.527107,-5.886564,-3.471223,-2.793978,1.550844,-2.970497,-7.153535,-9.023392,5.402549,-0.835928,7.490378,2.773603,-8.750122,-0.926028,3.333531,8.282837,5.542381,-3.629115,-2.813629,-0.181288,5.352986,4.338451,5.833099,0.708486,-5.603225,9.292593,9.218715,-5.463339,-1.840848,-3.331683,-3.815531,4.722310,0.489204,8.644593,-8.330061,5.722449,-4.041951,4.212226,0.825791,0.513270,-6.187157,2.787315,2.372268,-8.071028,9.619880,2.922357,-6.754187,7.681784,-1.718524,-3.794649,-1.379057,2.609022,-6.109182,-3.629070,7.442845,3.888108,-3.575957,7.605095,5.055506,4.132308,-8.024982,-3.658961,6.398404,-7.993764,9.378493,3.882514,9.576976,-2.976697,9.125021,0.586449,-7.958875,0.023789,8.508336,4.952793,-3.965307,0.484579,1.951825,2.704149,-5.334835,4.252818,-0.082635,3.761976,2.674446,4.517902,7.662772,3.338960,-9.081770,-5.876477,-8.771494,-2.336987,7.912239,5.113420,7.173021,3.787394,4.100446,2.087042,5.829934,9.497448,9.026200,-4.591495,4.757700,-2.688117,-4.129736,1.480845,-6.326216,1.101986,-7.344902,1.451242,9.613797,1.315888,3.571818,1.919614,1.134588,5.817046,4.975482,9.598310,8.010544,-5.411632,3.860017,-7.334632,8.809642,3.372925,9.827501,-7.677346,7.816040,7.373530,-7.220813,-6.514013,1.740024,-7.659469,8.572567,8.707930,-3.767972,-2.804309,0.830378,9.243882,-7.194730,-5.655938,9.360379,-3.244534,-7.501370,7.032875,-3.845877,7.148855,2.659911,3.390205,0.086700,-9.071734,-1.820535,8.243160,2.852453,1.208378,5.526148,3.761039,-5.211467,-1.041466,9.027046,3.439634,0.005719,9.998529,8.772646,2.204098,3.567265,-7.521026,-1.212612,-8.516382,-8.357625,6.803290,1.665282,3.792275,-0.060270,9.428099,1.237087,-5.161397,0.289331,-6.077296,-4.820867,1.022670,7.029340,1.631373,-7.541363,1.746882,8.874202,-9.122303,-5.870407,-3.077843,5.180720,-9.592710,4.278772,4.269990,4.804614,3.337764,9.393527,9.947532,-2.017256,-6.387437,-5.857203,9.640509,-0.961630,3.848588,0.697340,-1.410032,1.778015,-4.537401,4.256348,8.307908,1.571717,-2.034742,0.996318,5.467782,-0.008971,-7.361292,1.398437,9.598817,-1.772456,-8.509914,-6.888623,-0.904969,-4.395365,-2.758013,8.579896,-7.462574,-7.151573,5.414317,-0.644144,3.339992,2.659224,-3.295091,-6.316129,-2.142747,-1.349896,-1.951700,7.093431,-1.731895,3.005121,3.043899,-6.566130,1.315595,-0.251194,-7.411636,1.484796,-7.857402,-0.362285,-3.836274,-8.841419,8.372713,6.236248,7.158289,-5.181794,-7.752186,7.314930,-2.482879,4.464020,-0.559418,7.814119,9.983496,0.323045,0.338960,-1.715886,-6.805230,-3.270449,1.403251,9.568466,0.083124,-3.686943,-0.227822,8.380718,1.897907,-7.841765,7.839469,-9.568531,4.417604,-4.885668,2.838728,-5.345745,3.634450,4.561660,-7.067065,6.845802,1.244059,-8.149214,6.073237,-3.367775,-7.445397,0.364040,-0.411940,-5.688483,3.800947,-5.662010,5.719173,-0.326093,-9.283677,4.274686,-8.478352,-2.008933,-8.047278,4.270922,-8.189409,-3.535643,1.746490,-6.058029,-5.290025,6.344492,0.930949,-3.710953,-7.468239,8.319362,5.905456,4.561846,-7.893478,4.358747,-1.583572,-7.625466,-1.940392,-6.950109,-1.098652,-4.156037,5.926212,-1.258408,8.136601,-3.251429,8.782629,-4.789020,-8.120799,7.402352,6.331851,-6.835688,1.060025,3.355582,1.262122,2.589395,-9.333547,-3.582881,1.652417,0.306802,-4.691468,-6.813734,8.515221,-4.680022,0.572614,-0.399844,-7.910788,-6.941946,-3.024663,1.460461,5.585378,7.211230,-3.561169,-2.030340,7.567995,9.528506,4.630371,9.007068,-4.720446,-6.128171,2.898675,9.633118,6.560846,-0.437038,4.861512,-8.658230,-3.754160,-8.362955,4.275826,4.437632,-4.122312,-4.786271,-6.937866,7.301541,1.547270,-9.829069,-4.399674,-2.839654,-8.026571,9.709386,7.687708,-8.018265,-0.808116,-8.985901,5.758286,-8.269133,-4.878035,4.339592,-2.365539,-0.573787,3.009977,3.599124,-7.858442,5.698816,-8.403783,-3.283248,-7.318712,6.443049,5.037796,9.595959,4.991279,8.115507,-8.872600,5.341264,8.406637,8.611065,-3.950436,-9.806582,-6.522436,8.112014,3.493054,-6.276380,4.138111,-0.966031,-7.489766,7.906907,9.212442,7.450239,-2.893343,-0.987543,-6.342834,-2.648137,-1.500090,4.727225,-4.318167,1.817866,-1.439333,-6.787707,-5.385035,3.145973,-1.701497,-0.143831,1.926301,1.436042,-5.423564,8.894887,7.725135,-6.017464,-5.090774,9.478517,-2.157648,-8.573376,-9.980987,-0.056220,9.993438,8.874302,0.974413,3.424696,-9.000342,-8.639414,5.484305,0.153031,2.870011,-5.735337,-7.405204,-0.055153,2.730752,0.831820,1.070731,-1.033351,6.704674,-6.327103,6.069841,1.320228,6.748961,4.162632,2.077127,3.851307,-6.875904,6.028699,0.175881,2.457034,-6.526057,3.546010,9.075534,0.553959,8.240845,4.949178,7.439386,-0.575486,-2.883023,1.362048,0.229007,-4.218527,0.443907,-6.192387,5.533880,7.722461,-6.340024,-2.516739,-8.933068,0.359595,8.431600,-9.787763,6.600221,8.418484,-6.699570,-6.885099,-1.834619,5.439661,-7.325094,-9.714514,-1.426670,5.089674,-9.631670,-4.191016,1.265588,7.009825,-2.723172,-0.708151,-8.590676,2.516010,-8.625863,-3.712740,-6.698316,-7.694276,0.405070,-0.540743,-4.836941,3.493131,0.381397,7.056009,5.654005,-0.090597,2.201414,7.212799,-3.348901,-6.086131,-9.204428,5.910227,1.670728,9.326780,9.789948,-2.942611,-0.891007,-8.763006,1.220834,-5.261004,-2.995472,-6.885524,4.231825,-4.766034,-1.253954,4.486408,0.713592,8.706941,-9.430044,-9.101389,-7.190734,-2.862337,-0.119798,0.937163,-8.758272,-0.176935,-6.876226,-1.010954,-0.814021,1.195705,-6.434488,-8.435699,-8.756230,-8.249475,-0.245693,-1.215770,1.441875,7.121787,0.935933,3.361626,5.524951,2.655570,-3.927363,6.639223,-7.833875,0.091001,2.838435,-7.705394,9.813022,1.375861,2.191382,-1.860599,-1.490807,-6.933586,-1.994178,9.754175,8.997818,6.171075,5.215047,8.774122,-5.509881,-0.205843,-1.039487,9.052549,4.342868,3.050751,-3.953277,3.244558,-0.411560,-7.941976,2.775842,-7.560279,-7.048062,-6.857203,-6.202121,5.714793,-9.172528,9.122985,8.630506,-3.053701,7.457708,6.751711,8.971435,-2.902045,3.568118,4.849002,-3.765776,8.760395,0.038746,-8.655154,5.053644,-7.621168,2.390207,-5.612428,-0.759988,5.662704,9.114229,4.608714,3.449166,-1.031678,9.558138,4.340313,4.914891,-3.374836,-9.998010,-6.479696,7.390862,2.266884,-5.844333,6.208287,-8.217406,-7.433682,5.999446,4.154321,6.342534,0.406975,6.014226,0.524666,-4.542537,3.483219,-2.339594,-8.360075,0.919373,1.087422,-3.556646,-6.370205,4.518853,-5.673179,9.450210,-1.083980,7.834212,9.918644,-7.915966,5.627714,-7.660327,-5.974877,-3.979418,-8.681284,-6.256386,-2.430895,-1.526008,-4.970102,8.479725,9.132122,-4.209680,-3.937552,3.286580,-4.742685,-9.426760,-5.960474,-7.910718,6.569154,-6.331747,-0.798123,7.296647,9.945279,-1.447751,-8.478500,-5.137007,-7.453198,1.126448,-8.368479,-9.262958,-4.896005,-3.366345,5.069159,8.788779,7.978596,8.409773,8.574442,-5.539203,-6.764111,-0.435963,5.063222,-8.797091,1.346138,-0.125756,7.064565,-3.543515,6.077127,-7.830560,2.169272,2.720730,5.742299,8.984559,-5.361290,7.028827,-2.445043,0.573491,-1.153561,3.120887,4.005110,8.834331,-7.859081,-2.273027,-0.556193,-6.334889,9.566707,5.184733,-0.425451,4.456396,-5.338714,-3.662229,-8.039222,-1.505910,0.937320,-5.613084,1.717019,3.209001,8.739660,1.751087,0.992749,9.147283,-5.388861,0.021809,5.727624,6.411675,-3.584876,-1.990594,4.735401,8.788712,-6.403829,2.407218,-2.629450,3.195197,-4.513808,3.306675,3.945499,-7.761012,8.689942,-2.515049,-2.476630,9.229724,6.020060,6.676130,-0.875438,-5.527614,-4.100766,6.149853,-3.773229,-6.308931,6.805423,-5.341596,4.524660,-4.518821,3.648021,6.068485,-3.444972,-8.933687,8.886940,-1.927659,-7.847387,-4.413156,-4.453301,4.194578,3.571452,-2.071850,-6.815435,9.185578,4.397724,-7.416646,-9.759306,9.959626,-8.471147,6.394277,7.797485,-6.185642,-4.685294,2.443079,-1.461614,4.124126,-2.188504,-9.586149,6.375121,-2.428820,-7.644119,0.455254,7.401337,2.636352,-5.807023,2.482874,1.730558,9.344470,-2.024479,-7.482382,-9.422437,-0.168518,5.540451,4.136961,-5.126142,-1.379394,-2.659994,-1.886002,-7.068351,-1.062728,-6.135905,-9.592122,3.658516,2.032607,-5.974254,-3.220311,9.365481,-6.209502,9.653897,3.677939,9.233485,-6.277243,4.598915,8.853741,7.896430,-3.662388,8.337225,3.488705,9.331401,2.913762,-8.852135,-6.906509,-1.597173,5.893940,-3.420376,-5.745307,-6.533535,1.352021,8.244638,1.359570,-2.579276,-2.262835,-3.605833,-2.478041,-3.955335,-8.493825,3.518604,-1.070828,3.883544,-2.159030,3.408293,1.095314,1.535944,0.099798,-3.135208,0.943362,0.533704,-7.947163,0.715126,2.925793,-4.712527,3.703440,-1.180982,-4.491721,4.308435,5.326884,5.882517,-5.108566,9.894294,6.255692,-6.401589,1.345804,-2.833998,9.163421,-0.706190,5.703981,-8.330817,8.899159,-2.599636,-5.189919,-5.656554,-5.608548,5.608211,-9.524805,7.195061,-7.483247,1.808416,3.238858,9.987006,0.941671,9.777490,7.329849,0.168844,-5.171959,-8.685514,5.826664,-1.631468,-3.874261,-0.756502,-4.362219,-2.286041,8.923106,-4.648130,8.107714,-5.058781,-0.147609,7.601131,4.792326,-1.989806,-3.722645,9.566122,9.775369,-6.970806,7.113142,-1.343278,-2.345026,-7.143460,-9.081514,-9.759141,-4.885232,0.668327,-3.827288,-8.709102,1.787790,5.479000,5.265177,-9.502427,-3.987668,-5.859591,4.712574,1.892736,3.422623,-5.828723,6.047995,7.308118,8.770686,-7.323783,1.224534,6.999297,0.152806,7.760040,8.311616,9.550587,-9.019017,5.686348,-5.579330,1.020555,-3.867270,-9.078332,-7.431368,-7.033499,-8.971074,8.547583,7.084215,-5.116465,7.922795,-3.275276,8.332352,-9.501585,7.589045,-4.376270,-4.906877,-4.667268,1.872427,-2.525845,-4.637392,3.044153,6.655841,1.348888,7.667641,1.678877,3.011872,-6.061328,9.744832,-2.677866,-1.271835,8.720831,-1.626179,-5.219027,-1.005830,9.475869,8.334124,0.525357,5.715963,7.256966,-7.101564,6.313791,-4.431209,6.427160,-0.802149,7.529035,-4.697869,1.146643,-5.631045,-5.245486,6.159645,7.138428,-8.479360,2.095763,3.636194,-3.171563,-1.860036,4.156340,6.293609,-7.355885,-4.353950,4.346167,-9.824340,7.215796,-9.245123,1.744831,1.049149,-3.468816,3.662332,0.151590,-2.350815,5.766086,1.396218,-0.262396,1.866837,-4.835410,-7.155768,-4.973029,3.569002,1.773837,3.623857,2.640774,7.381051,-3.987347,5.497009,-9.837424,9.705265,-3.467546,-1.847542,-0.206786,-3.297027,-7.258895,-0.135256,1.323248,-3.822171,7.545661,-8.559496,1.066017,-9.531650,-0.898474,2.186069,7.318185,-0.059085,-7.339834,-0.913253,-2.405348,4.144498,6.700085,3.918805,9.106968,2.415576,9.277306,9.050346,-4.531668,-3.646556,-7.678976,6.030540,8.290355,0.566652,-8.754025,-8.183997,-0.379834,1.428595,5.255495,2.956187,8.184549,5.580105,-6.996580,1.781784,-0.078155,8.751214,3.747393,-6.328041,9.209621,-5.386574,-1.624920,-4.056106,2.878185,-0.613411,3.233686,3.375515,8.604055,7.667654,-7.098897,-9.181047,9.350179,3.138124,-0.766753,0.243115,6.346753,8.941707,-9.005525,0.872039,-6.760317,-8.096574,5.340127,-9.759272,-3.703806,-6.615279,-4.608629,3.859576,-2.205904,-1.268907,-6.160110,-9.470327,-6.537871,6.665391,-8.841164,-6.327225,4.525988,-7.346977,-5.705134,9.123698,-3.382028,9.230459,-3.275425,-3.990461,2.143441,0.451693,-7.847910,-5.932100,7.911501,0.104722,-7.110994,-0.241617,-7.593651,-5.391120,2.157918,5.651672,5.230084,-6.669079,8.496482,-9.222696,-4.218418,7.695948,-7.970497,3.250819,9.276568,0.922729,-6.855777,5.910501,-9.935550,9.802363,4.528613,2.671337,-0.326031,-9.979663,6.051544,-2.065457,-8.877696,-0.646631,2.087490,3.998909,2.705061,-1.605384,-7.741711,-3.597497,1.562734,3.554533,1.215435,6.101184,-8.235109,1.320463,9.185799,7.673876,5.140181,-6.605405,9.910831,-2.015651,-1.307918,-3.627598,-1.276409,8.962795,7.623929,3.615095,7.941195,-9.635512,-7.005794,5.171578,3.835559,-8.855557,6.848180,-6.740047,-5.832652,0.050083,9.497901,2.918441,-4.764935,-3.234718,2.631934,-2.954576,-1.004007,4.468692,2.721770,-3.349563,4.008639,7.023044,1.862677,-5.546559,-3.824308,-4.525033,0.238371,-3.787392,-2.491106,0.445823,-1.846192,7.821774,-3.608379,1.199751,8.686641,1.285464,-1.044305,1.640343,-8.046783,6.205912,9.188709,-5.395991,-6.651229,0.120190,1.060251,-7.794212,-4.014689,5.460145,-7.742399,-2.938975,-5.164164,0.257813,9.627664,0.463421,-9.001100,-3.914877,-9.705336,-4.622638,2.646617,-1.703109,5.907725,-5.273795,-4.830668,-3.117729,5.343825,-4.162225,-0.758568,-4.701550,1.369940,6.433811,2.964345,8.698175,5.913549,-3.911673,4.255591,5.054809,5.085909,9.570469,4.387326,8.189725,-7.260344,8.675558,6.488224,-2.772856,4.663135,-1.225384,-3.365808,-2.796692,2.304803,-3.555267,8.113360,1.625194,-6.062771,-8.439571,0.720015,-2.558806,-7.495402,-6.015745,7.861336,-2.026276,6.141789,9.625632,-5.536252,3.044001,-9.862391,3.930908,2.035466,1.915594,0.778996,-9.660978,5.170445,-6.745091,-9.746872,6.182594,-8.989311,-1.405230,-3.877859,1.523401,8.567274,-1.443758,-7.768548,-8.813973,0.504121,3.228779,1.039820,5.968973,-6.345361,-6.156701,-4.144634,5.865736,7.238443,-6.763601,0.621832,0.348913,-3.961582,6.852241,7.799425,8.853432,2.837747,5.957239,-0.524446,4.883868,-0.329337,3.892939,2.919182,4.430886,-9.414914,-1.367792,3.212789,-0.540211,4.847075,5.600780,8.764093,3.704227,1.058074,-4.030501,3.692350,2.597604,9.630700,5.864741,4.575084,-2.134682,-7.673654,2.176943,-8.748070,-8.859217,0.646276,-8.732558,-8.886943,5.952224,-6.264762,0.709077,1.720720,2.337030,5.561489,5.971464,-2.587608,-1.635899,-3.439492,-9.493473,8.398485,7.913899,-2.372932,-7.613695,7.634021,3.213245,3.606643,-6.145869,2.039076,4.843233,-2.375792,1.034566,-3.415657,9.740895,8.699788,8.188541,-3.215110,-2.370573,-7.802540,2.603126,-7.429568,4.678148,0.880570,9.312967,-7.764684,9.603224,8.696531,1.476759,-4.669340,2.918215,-8.823466,8.709544,1.611936,-6.312979,-6.165654,1.644913,-4.291643,-6.306305,-2.763571,-5.801446,-2.714892,3.574300,-9.854664,-0.562380,-0.621289,-0.605812,-3.225557,6.983223,3.758548,-7.432138,-5.059798,4.795679,-1.211321,-7.943211,0.590645,5.853817,8.889259,7.249575,3.458806,-6.086093,8.283951,9.484776,-6.819749,6.255815,-6.539031,3.770961,-4.629057,5.444624,-9.065314,6.740172,-8.889771,-9.318584,-1.109313,0.132107,3.839378,3.057572,-2.395334,-2.204979,5.467687,4.864703,9.872625,-0.430862,8.330131,2.138259,-0.424740,6.664794,4.716108,-3.177684,7.790826,-2.652356,5.903898,-0.565395,-3.681437,4.681880,-0.861743,8.518403,6.942207,4.654408,9.918006,8.483059,-4.769551,-0.366830,-3.553629,5.189495,-4.830824,-9.082018,9.493192,3.439072,2.603081,2.892636,7.472484,-5.307018,3.563824,4.121111,-2.041576,-2.860656,4.866290,-3.500682,9.499366,-4.245908,7.642651,2.943714,9.341933,-4.107872,0.188184,-8.216496,-9.171769,-0.932628,6.519528,-8.529358,-7.523751,-4.563366,0.750004,5.769365,-3.749947,-1.056124,-9.454771,-1.357300,1.732473,-2.090687,-5.045258,2.987262,5.006947,-4.531573,-3.730945,-6.911266,5.107224,-5.656782,-9.939977,8.328187,4.204736,-3.108409,-2.733580,0.879219,-4.922066,-7.508150,7.235673,4.235718,1.104088,1.543726,0.684214,-3.362090,-4.173642,6.362265,-6.522956,2.104211,9.703486,7.479930,-4.937349,6.640282,7.444841,3.694435,4.529692,6.909985,6.298108,-4.705599,7.872076,8.873548,-6.337816,-9.626454,-9.008741,-4.148986,0.302191,4.433041,4.158259,-5.293355,-7.666372,8.100875,8.735485,9.345118,2.827558,7.580541,-2.341529,-1.774796,1.151658,-5.028816,-7.358504,6.028984,-1.603355,6.042984,9.678608,-4.478441,6.792482,-0.133996,4.907566,8.700429,7.232072,6.215522,-1.522527,-9.839194,-2.533535,8.337066,-1.484930,-6.839370,9.066711,-5.711731,-5.735048,-8.622093,-2.703009,-4.260760,-6.645964,-8.741779,-4.898349,-9.498017,9.030588,-7.301924,5.486243,-7.913646,9.066581,-1.591783,-1.329058,6.415838,-6.694820,-2.620673,-4.695925,-8.783899,3.230387,4.322845,-1.595124,-6.224153,-3.826068,8.895078,-4.032816,3.435115,-3.293186,-6.931501,-6.528789,2.655991,8.860977,0.686002,-1.238636,5.033649,-0.669365,8.977261,-0.787382,-3.881648,7.234019,-8.380747,2.812311,0.061104,0.966839,-2.794645,1.490555,-7.361462,-7.660938,1.630658,7.387112,-2.049981,0.466689,-7.667088,6.569018,-5.054206,-1.535552,-6.588416,9.871387,-5.819468,7.361296,-0.320398,-6.996480,1.619633,8.051861,-7.114845,6.093709,-7.001792,-1.442712,-4.042953,-4.427186,-6.649355,0.077991,-9.911394,-1.604100,-3.715123,-6.755632,7.115052,8.593779,6.665710,1.309903,-7.152654,-5.172109,3.240248,4.031921,-7.985460,-2.561079,8.250315,4.654122,-5.793899,-7.941318,7.958731,-2.520914,6.798526,2.862211,-0.293176,-2.042961,-4.879196,2.834044], dtype = "float32")#candidate|4474|(2640,)|const|float32
call_4471 = relay.TupleGetItem(func_3334_call(relay.reshape(var_4472.astype('bool'), [7, 7, 12]), relay.reshape(var_4473.astype('float32'), [126, 1]), relay.reshape(const_4474.astype('float32'), [4, 660]), ), 5)
call_4475 = relay.TupleGetItem(func_3338_call(relay.reshape(var_4472.astype('bool'), [7, 7, 12]), relay.reshape(var_4473.astype('float32'), [126, 1]), relay.reshape(const_4474.astype('float32'), [4, 660]), ), 5)
output = relay.Tuple([call_4466,call_4471,var_4472,var_4473,const_4474,])
output2 = relay.Tuple([call_4467,call_4475,var_4472,var_4473,const_4474,])
func_4476 = relay.Function([var_4472,var_4473,], output)
mod['func_4476'] = func_4476
mod = relay.transform.InferType()(mod)
mutated_mod['func_4476'] = func_4476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4476_call = mutated_mod.get_global_var('func_4476')
var_4478 = relay.var("var_4478", dtype = "bool", shape = (588, 1))#candidate|4478|(588, 1)|var|bool
var_4479 = relay.var("var_4479", dtype = "float32", shape = (126,))#candidate|4479|(126,)|var|float32
call_4477 = func_4476_call(var_4478,var_4479,)
output = call_4477
func_4480 = relay.Function([var_4478,var_4479,], output)
mutated_mod['func_4480'] = func_4480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4325_call = mod.get_global_var('func_4325')
func_4326_call = mutated_mod.get_global_var('func_4326')
call_4564 = relay.TupleGetItem(func_4325_call(), 1)
call_4565 = relay.TupleGetItem(func_4326_call(), 1)
var_4572 = relay.var("var_4572", dtype = "int16", shape = (7, 2, 9))#candidate|4572|(7, 2, 9)|var|int16
bop_4573 = relay.bitwise_xor(call_4564.astype('uint32'), relay.reshape(var_4572.astype('uint32'), relay.shape_of(call_4564))) # shape=(7, 2, 9)
bop_4576 = relay.bitwise_xor(call_4565.astype('uint32'), relay.reshape(var_4572.astype('uint32'), relay.shape_of(call_4565))) # shape=(7, 2, 9)
output = relay.Tuple([bop_4573,])
output2 = relay.Tuple([bop_4576,])
func_4584 = relay.Function([var_4572,], output)
mod['func_4584'] = func_4584
mod = relay.transform.InferType()(mod)
var_4585 = relay.var("var_4585", dtype = "int16", shape = (7, 2, 9))#candidate|4585|(7, 2, 9)|var|int16
output = func_4584(var_4585)
func_4586 = relay.Function([var_4585], output)
mutated_mod['func_4586'] = func_4586
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4596 = relay.var("var_4596", dtype = "int8", shape = (14, 3, 9))#candidate|4596|(14, 3, 9)|var|int8
var_4597 = relay.var("var_4597", dtype = "int8", shape = (14, 3, 9))#candidate|4597|(14, 3, 9)|var|int8
bop_4598 = relay.not_equal(var_4596.astype('bool'), relay.reshape(var_4597.astype('bool'), relay.shape_of(var_4596))) # shape=(14, 3, 9)
output = bop_4598
output2 = bop_4598
func_4602 = relay.Function([var_4596,var_4597,], output)
mod['func_4602'] = func_4602
mod = relay.transform.InferType()(mod)
mutated_mod['func_4602'] = func_4602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4602_call = mutated_mod.get_global_var('func_4602')
var_4604 = relay.var("var_4604", dtype = "int8", shape = (14, 3, 9))#candidate|4604|(14, 3, 9)|var|int8
var_4605 = relay.var("var_4605", dtype = "int8", shape = (14, 3, 9))#candidate|4605|(14, 3, 9)|var|int8
call_4603 = func_4602_call(var_4604,var_4605,)
output = call_4603
func_4606 = relay.Function([var_4604,var_4605,], output)
mutated_mod['func_4606'] = func_4606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4446_call = mod.get_global_var('func_4446')
func_4447_call = mutated_mod.get_global_var('func_4447')
call_4614 = relay.TupleGetItem(func_4446_call(), 0)
call_4615 = relay.TupleGetItem(func_4447_call(), 0)
func_3104_call = mod.get_global_var('func_3104')
func_3108_call = mutated_mod.get_global_var('func_3108')
var_4622 = relay.var("var_4622", dtype = "int16", shape = (16, 14))#candidate|4622|(16, 14)|var|int16
var_4623 = relay.var("var_4623", dtype = "uint64", shape = (2288,))#candidate|4623|(2288,)|var|uint64
var_4624 = relay.var("var_4624", dtype = "float64", shape = (60,))#candidate|4624|(60,)|var|float64
call_4621 = relay.TupleGetItem(func_3104_call(relay.reshape(var_4622.astype('int16'), [7, 8, 4]), relay.reshape(var_4623.astype('uint64'), [2288,]), relay.reshape(var_4624.astype('float64'), [30, 2]), ), 1)
call_4625 = relay.TupleGetItem(func_3108_call(relay.reshape(var_4622.astype('int16'), [7, 8, 4]), relay.reshape(var_4623.astype('uint64'), [2288,]), relay.reshape(var_4624.astype('float64'), [30, 2]), ), 1)
output = relay.Tuple([call_4614,call_4621,var_4622,var_4623,var_4624,])
output2 = relay.Tuple([call_4615,call_4625,var_4622,var_4623,var_4624,])
func_4638 = relay.Function([var_4622,var_4623,var_4624,], output)
mod['func_4638'] = func_4638
mod = relay.transform.InferType()(mod)
mutated_mod['func_4638'] = func_4638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4638_call = mutated_mod.get_global_var('func_4638')
var_4640 = relay.var("var_4640", dtype = "int16", shape = (16, 14))#candidate|4640|(16, 14)|var|int16
var_4641 = relay.var("var_4641", dtype = "uint64", shape = (2288,))#candidate|4641|(2288,)|var|uint64
var_4642 = relay.var("var_4642", dtype = "float64", shape = (60,))#candidate|4642|(60,)|var|float64
call_4639 = func_4638_call(var_4640,var_4641,var_4642,)
output = call_4639
func_4643 = relay.Function([var_4640,var_4641,var_4642,], output)
mutated_mod['func_4643'] = func_4643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4325_call = mod.get_global_var('func_4325')
func_4326_call = mutated_mod.get_global_var('func_4326')
call_4656 = relay.TupleGetItem(func_4325_call(), 2)
call_4657 = relay.TupleGetItem(func_4326_call(), 2)
output = call_4656
output2 = call_4657
func_4672 = relay.Function([], output)
mod['func_4672'] = func_4672
mod = relay.transform.InferType()(mod)
output = func_4672()
func_4673 = relay.Function([], output)
mutated_mod['func_4673'] = func_4673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4672_call = mod.get_global_var('func_4672')
func_4673_call = mutated_mod.get_global_var('func_4673')
call_4706 = func_4672_call()
call_4707 = func_4672_call()
output = relay.Tuple([call_4706,])
output2 = relay.Tuple([call_4707,])
func_4724 = relay.Function([], output)
mod['func_4724'] = func_4724
mod = relay.transform.InferType()(mod)
mutated_mod['func_4724'] = func_4724
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4724_call = mutated_mod.get_global_var('func_4724')
call_4725 = func_4724_call()
output = call_4725
func_4726 = relay.Function([], output)
mutated_mod['func_4726'] = func_4726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4446_call = mod.get_global_var('func_4446')
func_4447_call = mutated_mod.get_global_var('func_4447')
call_4751 = relay.TupleGetItem(func_4446_call(), 0)
call_4752 = relay.TupleGetItem(func_4447_call(), 0)
output = call_4751
output2 = call_4752
func_4758 = relay.Function([], output)
mod['func_4758'] = func_4758
mod = relay.transform.InferType()(mod)
output = func_4758()
func_4759 = relay.Function([], output)
mutated_mod['func_4759'] = func_4759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4446_call = mod.get_global_var('func_4446')
func_4447_call = mutated_mod.get_global_var('func_4447')
call_4819 = relay.TupleGetItem(func_4446_call(), 0)
call_4820 = relay.TupleGetItem(func_4447_call(), 0)
func_2517_call = mod.get_global_var('func_2517')
func_2521_call = mutated_mod.get_global_var('func_2521')
const_4831 = relay.const([1.118181,-0.367261,0.729270,-7.361891,-0.766238,2.396146,-2.128512,3.416083,-7.970856,9.013567,7.304778,-8.246500,-0.846055,7.679872,4.262968,-3.836072,4.220648,1.146406,-3.624549,8.704952,-2.094270,0.148593,-2.839191,4.056772,3.284560,-7.688577,-2.589369,-9.584268,9.572063,7.437491,3.070224,-1.483264,-5.147955,1.312901,0.839964,3.485895,0.296480,-0.046240,8.228894,-3.540274,-6.511482,-2.740425,2.700921,0.552448,-6.708965,-6.172948,6.825376,-1.515714,-5.449637,-4.382816,-5.757903,1.790877,4.526281,-0.411483,4.056897,9.695748,6.270585,9.962692,-0.218293,-6.281499,6.531127,-3.785016,6.516316,-1.783605,2.161225,3.767421,0.242120,6.785203,-7.805548,5.376123,8.950955,6.709536,-4.847586,1.907596,1.521031,7.240317,-8.786033,5.343892,2.519931,-2.766693,0.742809,-5.026891,-6.493231,7.283197,1.719710,6.874573,7.178084,-7.608778,6.714069,-4.284941,3.888617,6.722885,2.326637,5.208517,-5.570478,5.577606,8.493833,-2.502681,-2.766828,-8.025854,4.026802,-5.150339,-8.258320,-3.737616,-7.294580,-6.630382,5.544687,-0.633739,5.084563,1.606927,5.578788,4.052827,-4.084202,-3.046827,9.965877,2.450421,-9.077548,1.294507,-2.916226,-2.997850,-7.517101,-8.365192,-5.144303,-9.381357,-3.053484,-8.952063,7.825151,-6.151511,2.194473,-5.968657,2.807685,8.184556,1.704610,-8.480193,9.707495,-0.026799,8.260049,2.899364,9.130789,6.142845,0.623262,2.391795,6.082571,-6.938371,2.025183,4.291954,-9.710568,-9.923463,8.374431,0.167420,-3.188829,-1.641767,-1.481059,3.106330,-4.980686,8.444285,-0.937958,-3.794574,-6.052217,3.009139,4.145296,-4.483816,9.673246,0.052701,6.062326,7.650675,-4.037075,-8.710433,5.841786,7.862193,-7.131698,5.312671,4.400607,3.128682,9.859960,7.245976,6.565558,-3.523753,4.583088,-0.340970,2.641712,-4.025825,0.185243,-9.470187,-0.593106,-6.830669,5.424654,-8.515836,6.557566,-8.142149,-8.682697,3.335305,-4.983255,-1.705987,2.910876,-9.558897,6.156376,4.892268,7.168527,7.712954,7.191578,5.617049,-5.033959,5.364197,8.775223,-0.506875,-0.304495,0.108329,6.100903,-6.910059,-6.032485,9.058064,4.005794,9.929074,5.492360,-3.176762,-5.446674,7.986576,4.203474,2.916616,-0.890664,-1.699905,7.189493,0.029762,-5.999752,-5.056254,3.867053,-9.273415,-9.942556,9.319704,-9.766881,-0.787411,5.118453,3.283718,-0.619934,1.299759,-2.731051,1.881557,-0.312905,7.157342,-3.974469,2.880838,2.473782,-3.359334,1.975070,1.561404,-4.614602,7.718424,2.158467,-1.876815,0.970830,9.081147,-2.193702,3.702711,3.855936,2.321554,-5.170260,3.912106,-3.467051,5.408017,-5.209391,4.728483,-1.342815,-5.384475,-3.660275,-4.997477,8.827427,7.186329,-0.195092,-9.972838,1.300161,-2.673113,-5.245422,-6.249430,1.569145,3.030713,-0.579685,-5.836826,3.638583,7.925728,-1.335195,6.200368,3.571372,1.251752,2.022980,6.952872,0.665200,2.953287,-8.426564,-6.687429,3.808027,1.346256,-3.547357,1.787350,-0.699505,0.930422,-1.776882,-9.589033,-7.912969,9.247010,9.467506,-1.652298,-0.915253,1.523174,9.346562,3.802610,0.889947,6.056799,-1.042592,7.589451,9.607500,0.931762,9.516343,7.299361,3.654521,7.569426,1.563809,3.265879,0.555642,-4.038171,-4.832869,-1.870939,-9.261505,-2.297079,-4.837026,-4.009174,-1.543026,3.631927,1.176927,8.457162,1.630452,-4.157198,9.123076,7.240263,-4.908409,9.448327,6.157022,-2.586702,7.482302,-9.306118,-1.398869,3.667225,7.417856,-1.137121,0.872783,2.893723,-0.828876,-8.032730,-1.459984,4.522281,9.609975,4.234861,-5.917689,1.608503,-5.898984,2.087838,-1.371963,-7.416578,2.281493,-5.021750,-7.138107,1.162423,9.093158,-0.191035,7.836412,-0.533129,5.494563,6.203384,8.916767,6.250173,8.032001,-2.087241,-5.199389,8.396742,2.480576,-6.341144,5.439256,0.481884,1.572627,-1.683524,4.608244,-1.884689,8.021950,-6.192536,-0.330682,-0.918029,-9.798041,5.570850,3.956502,-8.674169,-0.605524,6.852569,-7.224801,4.127391,-7.693204,7.611670,-0.826750,-9.814889,6.069798,1.192552,6.787949,0.346128,-3.679934,-1.782157,4.168934,3.286439,3.235269,-3.430769,1.183297,-5.602580,6.512686,8.929606,7.151793,2.286121,-2.303391,-9.529449,2.737070,0.398757,-0.029382,9.555002,-6.220145,4.504953,1.609412,5.685810,5.007577,5.867325,3.592356,0.109407,-3.881946,-3.880622,5.047431,-3.625511,-9.833637,-7.164758,7.335518,9.168139,-3.180814,-5.268734,-6.120020,-9.336708,0.621789,-2.555770,-3.012411,4.192516,6.786926,8.878223,-2.786604,3.350703,6.796157,3.225017,6.901879,-4.795813,4.139313,-1.861715,1.684881,-5.429857,-3.148266,6.986176,-1.315099,9.350858,-5.620250,-1.112526,2.065443,-8.542332,0.167728,1.078158,-6.007558,6.748819,-2.770250,8.033823,-1.294036,-5.210590,-1.056394,-0.865390,-5.553681,-2.767575,-9.704668,4.671586,-8.778594,6.958090,0.660934,6.716726,-5.288749,-2.742330,-3.944470,-4.390019,7.561709,4.031458,2.233802,-7.164988,5.655598,-6.293578,4.186775,5.228221,7.444310,3.867793,-6.103803,-1.740860,9.667476,7.609389,-0.725058,0.868466,1.749144,-0.049947,-6.731986,-6.473959,2.041869,8.599816,6.756995,7.889599,1.241127,8.996886,3.792459,9.624851,-2.792066,-7.642608,-7.612370,-4.282391,-6.437025,-9.826324,6.969339,-3.240155,-9.207777,2.322826,8.591436,-2.741462,-9.492456,-9.121112,-8.159960,-6.581985,-9.751217,9.190215,-0.658535,-8.057550,-2.902262,9.101144,-3.447150,2.972853,-5.686719,-4.119592,4.385640,-5.683277,-3.720514,6.537574,-4.641949,-6.311546,-1.619562,-0.605934,0.034477,3.967620,6.196968,-6.500945,-2.743887,-3.665888,-1.004534,-1.805025,-9.055754,1.955122,5.768413,7.600428,2.318956,7.463165,2.715327,-6.084861,-8.627475,9.879801,2.928600,6.976065,2.261752,-6.076715,-5.090257,0.068534,1.041015,-9.975948,3.488260,5.005041,9.186146,-7.605759,-0.920247,9.745882,-2.098023,-5.450882,-1.222321,1.913054,-4.029501,-9.942717,8.103916,0.473397,-2.508304,9.321260,6.552507,-5.939569,8.848991,6.038579,-0.339624,3.624959,8.364493,-8.067158,9.973019,8.708600,7.135970,4.968694,1.359572,0.389003,-2.813328,7.495594,0.435343,-5.712588,-9.072144,-7.183192,-0.570307,1.144980,-0.253084,-9.776077,-1.391189,3.638908,3.461277,-0.411082,0.927842,-4.816099,-3.855329,6.653958,-1.924540,5.106265,1.110236,3.623185,2.295066,-6.586863,-6.040666,2.676687,-9.043350,-4.390257,1.089466,7.736539,-5.793115,-4.061982,2.147618,6.881130,5.090774,9.212447,-6.878773,0.987889,3.835717,4.661912,-2.161348,-5.717772,5.999568,-1.116916,3.519489,1.250320,9.449864,3.499897,9.280389,-3.942618,5.620647,-6.888700,-5.261873,7.901384,1.263182,2.254086,5.328137,-1.678997,-5.241608,-8.771079,-5.356711,-4.568789,3.847207,3.107963,-7.740402,-1.168624,8.274306,2.091488,-8.349354,7.320920,-8.070567,1.354366,2.225734,-6.749379,-4.427803,5.733481,9.855348,-0.628374,3.028918,3.054770,-9.281344,1.467856,-9.353969,5.610342,1.398360,-3.399958,-9.370775,-5.045200,-4.000243,0.950397,1.152990,6.393482,-8.268132,4.299780,0.009583,4.754855,-0.748668,9.299315,-6.553744,9.827046,-4.398204,7.312857,0.942422,-9.193669,-6.226189,-5.925825,-1.170196,-0.836675,-4.047718,0.205274,8.272709,0.462469,6.053248,-8.643876,4.964620,-6.208102,-3.133168,-5.792897,7.182935,2.283459,8.649751,5.660074,9.527526,-2.887907,1.350839,-8.282059,4.987181,3.525451,-8.540065,-0.431192,6.450329,3.542964,-7.610770,-6.455314,-7.173140,3.211841,0.670829,-0.811133,8.415795,-5.096931,-8.884122,7.375712,-4.109606,-0.042659,-9.864773,3.903166,2.729125,0.482535,-9.117050,2.041983,1.366265,-3.764116,2.731781,-6.178235,-1.377078,-1.050078,1.955117,-2.100384,-9.360304,-7.239632,9.361107,-3.916355,4.165858,-2.085784,7.956616,-5.702638,-3.460040,-4.208273,8.962891,-7.120179,6.331221,-5.403111,-2.966939,9.454821,-2.571094,-9.944646,1.508622,-1.225463,-3.715845,-5.692394,6.297901,8.775657,-0.707550,5.926816,-0.688962,1.810284,-4.152279,-2.710612,-2.601367,8.290035,1.381588,-1.212965,6.104197,4.847047,4.699670,1.333341,7.565722,-3.140843,-1.645424,5.673453,-1.101565,5.014223,6.656484,1.570831,0.812199,-9.276907,-7.004639,5.297628,9.567468,-6.478237,-9.450289,8.787939,-1.613982,7.581911,-2.233231,5.966623,3.753512,6.087266,-0.292207,-0.933399,-6.823479,-9.338118,3.061130,-2.297520,4.501104,3.878036,-7.160277,9.413657,4.110043,-8.208256,1.252967,-2.664325,-6.167162,3.955410,-7.298449,-8.988898,-8.495414,-3.892379,-9.635702,9.360983,4.074786,9.755197,9.543463,-7.811938,-2.920038,-7.659106,-2.764805,-2.418163,8.039743,2.330873,-7.212380,-4.333858,-6.892303,-5.268223,4.881395,-5.042051,4.228527,-9.724212,-0.386190,4.242803,3.190008,3.274590,-4.145384,-7.367391,4.308615,4.986269,3.636062,5.340429,-9.293283,-6.246071,9.106803,-1.872638,1.270066,1.445213,4.141585,-2.905027,3.774731,-1.478596,6.913166,1.109066,-5.205964,-7.796751,-2.738080,-5.934744,-2.367466,-2.761469,4.150882,-1.293410,7.437621,5.825716,-9.671778,-4.680128,1.088235,5.267280,7.971092,4.440924,2.158905,-1.265657,8.523582,7.648687,5.833614,4.131719,-4.181368,8.848321,-4.977647,9.163720,-4.423474,-9.339947,-6.100397,2.112873,-4.794530,-4.781911,-6.001176,2.050211,2.211111,4.124776,-5.131705,6.556222,-4.287741,-6.411542,4.030595,6.554876,7.210489,0.477085,7.009214,-4.595508,-9.935127,-1.487513,2.238037,-1.816898,-6.545998,6.808379,5.557703,5.340440,-4.653383,-3.066382,5.204573,1.751133,4.914142,6.281895,5.225496,-2.853804,-6.378362,5.457466,-0.175368,-5.157787,5.002479,2.723469,-4.727729,8.932287,-8.892316,5.533846,7.872537,4.087771,7.383272,-0.410081,-3.183492,-8.786844,7.436536,-1.158770,-7.740422,-6.088140,-1.207073,-7.472796,-4.755746,9.544658,4.976869,5.025372,-3.814660,1.586043,3.881910,-9.829603,-8.526550,-7.966192,-6.417282,0.640515,9.033250,4.478436,3.820201,-6.832599,5.397554,-2.695840,-5.626562,9.830614,-9.601160,4.017319,-3.386264,7.599300,-6.492655,-5.554161,-1.196054,0.639672,9.315679,-8.772518,-9.305220,0.465913,-4.354241,-1.351449,8.713930,8.337247,-7.069942,5.368538,5.924935,2.772379,-6.055475,-1.822487,1.901449,-0.227239,-6.322900,0.423620,0.847764,-2.500760,3.594102,9.141968,0.557094,-1.035880,3.492763,-2.277396,3.718560,-9.038980,-1.328255,-2.661090,5.683984,-2.705191,0.037582,-1.660464,-5.670343,9.701089,-2.650217,-5.661513,0.462953,8.283286,-2.101069,9.621151,-3.194114,4.038520,6.404622,-6.192437,-5.613062,-5.646671,0.773637,5.444872,-3.850471,2.922338,8.038697,-7.844452,-3.781005,3.249024,8.420274,-6.400846,-7.415927,-7.406889,-1.081581,-1.787129,-2.857733,-6.593437,-2.542233,4.784218,-2.016793,7.942649,7.350822,0.424047,3.356835,-4.795088,5.682296,-3.648814,7.251917,6.735778,-0.964592,-8.780908,5.874481,-9.495656,-2.048836,-3.745671,-4.246552,-5.495879,8.580963,0.218319,-0.440390,4.994307,4.280278,-5.813107,8.264855,-3.439542,2.282433,-9.501934,9.833303,-7.788651,-1.510674,8.004205,-8.346044,-2.959255,0.634135,9.179196,-8.212343,7.792322,-9.197748,-1.560508,-7.400411,6.967447,9.452476,-7.529634,-2.701367,1.795475,0.338436,1.644680,-2.433152,4.696517,-4.522574,-6.134177,4.924473,-6.365052,1.362341,9.817999,0.343814,1.292666,-2.236353,2.820570,8.355679,-7.541785,6.356894,-1.259984,5.150883,5.075183,-3.511904,-2.024585,-2.800403,-8.533048,7.640972,2.710848,-2.896439,-7.351189,-4.095908,-4.370746,-5.433950,-1.575636,-5.085450,1.733896,-5.875302,4.085165,-6.124216,-0.509223,-8.623454,-8.797842,4.390442,-1.745366,9.123219,-5.079455,2.794460,3.628058,4.418549,8.997043,-1.140477,-8.042481,-9.414469,-2.383872,5.197016,5.523327,2.797128,-3.445828,0.426191,-0.640998,7.318535,-3.173096,9.236540,-2.715799,4.517144,3.228629,-8.587866,-6.979981,9.300597,-0.267996,0.031969,1.266875,3.071463,2.440989,-1.915216,0.846418,7.072069,-6.852407,6.306373,7.671927,9.682426,7.176857,-9.549349,-1.189071,-2.092782,6.377718,-7.916622,-7.812819,-6.840555,-1.331253,5.247227,-8.208934,0.503103,-7.583105,6.728500,0.179981,-9.656679,-5.587422,-0.467535,-9.712241,6.001189,-3.434980,-1.077149,-2.604086,4.707034,-4.838596,-5.225476,7.811773,4.296337,0.125500,9.273759,1.440243,7.464242,6.640714,-7.229183,-1.675336,4.021380,9.861933,9.558449,-8.494689,-0.303606,2.889791,0.270579,-6.696364,-1.377686,9.266140,-5.097959,2.657697,-7.521492,9.671425,4.495408,4.292570,8.207804,-7.051381,-5.702545,9.761661,8.013364,8.983621,9.170184,-8.727536,4.916705,4.092019,-1.307919,3.146776,1.180562,-8.381620,-8.148425,3.304594,-1.529084,-2.809632,-6.374058,-5.029251,0.494047,-4.524148,1.677559,-1.613371,-3.758746,1.571022,4.334752,-5.801908,5.920610,5.852063,-2.666714,9.280230,-9.133204,2.805941,3.893471,7.005380,6.477440,7.624859,-5.950653,-5.638356,-3.249841,0.747688,-5.129859,-6.633957,-7.416069,-4.362573,7.264634,-0.757102,1.447009,-8.965108,4.239009,8.422524,-2.698391,3.918390,3.743489,8.959042,5.588854,6.915242,-1.481559,-4.442343,0.262733,2.898600,-2.279336,-0.698822,1.327507,0.717303,-8.626748,-1.177558,0.358346,0.057485,5.944566,-6.097079,-9.906945,-2.317416,-1.836414,7.645112,1.299545,-8.173528,-6.714546,-8.188963,0.892462,-6.281671,-2.201511,-3.483955,5.084981,-7.961973,9.036366,4.459084,-9.831739,-5.099347,-5.235679,-4.616181,8.163556,-9.449753,-0.519354,3.576572,-2.666787,5.865891,-2.161207,-8.208889,-4.814056,-4.270926,-5.413261,0.039139,-4.068897,9.526153,2.325885,-6.255917,-1.753542,2.079995,2.807552,-7.579375,-2.896030,0.992372,-7.229960,-7.040012,-0.966070,-5.558625,2.840862,-9.384389,9.304349,-3.150229,5.618448,8.416969,5.939758,-9.495563,-3.154432,-6.273592,6.609906,0.326422,-3.723272,-3.398875,4.990963,7.643455,-2.061223,-5.491781,9.243378,-7.011181,2.766242,-9.475150,-9.182402,-0.760668,0.179563,-4.231609,-6.483746,-5.619785,8.204774,1.629189,4.040934,3.914494,-7.760441,-1.683296,6.126858,7.050020,-9.905642,2.064229,-9.351036,0.959078,7.556254,-9.860576,-7.076983,-3.668689,0.189656,-0.706717,-7.773061,-3.761727,5.688866,-5.888159,-2.700460,5.436553,8.700935,2.565079,-5.394653,3.325081,-3.882266,3.211586,1.605391,0.617505,-2.749870,2.154972,2.523407,1.910733,-1.461454,0.655863,9.040500,-4.450538,-0.447339,6.930537,-5.932873,-7.449463,-2.986978,0.618076,4.600390,1.312584,-9.990567,-5.585354,-4.746230,-3.205502,3.265069,8.334807,0.481291,6.629126], dtype = "float64")#candidate|4831|(1440,)|const|float64
var_4832 = relay.var("var_4832", dtype = "float32", shape = (126,))#candidate|4832|(126,)|var|float32
call_4830 = relay.TupleGetItem(func_2517_call(relay.reshape(const_4831.astype('float64'), [12, 15, 8]), relay.reshape(var_4832.astype('float32'), [126,]), ), 1)
call_4833 = relay.TupleGetItem(func_2521_call(relay.reshape(const_4831.astype('float64'), [12, 15, 8]), relay.reshape(var_4832.astype('float32'), [126,]), ), 1)
output = relay.Tuple([call_4819,call_4830,const_4831,var_4832,])
output2 = relay.Tuple([call_4820,call_4833,const_4831,var_4832,])
func_4838 = relay.Function([var_4832,], output)
mod['func_4838'] = func_4838
mod = relay.transform.InferType()(mod)
var_4839 = relay.var("var_4839", dtype = "float32", shape = (126,))#candidate|4839|(126,)|var|float32
output = func_4838(var_4839)
func_4840 = relay.Function([var_4839], output)
mutated_mod['func_4840'] = func_4840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4758_call = mod.get_global_var('func_4758')
func_4759_call = mutated_mod.get_global_var('func_4759')
call_4866 = func_4758_call()
call_4867 = func_4758_call()
output = call_4866
output2 = call_4867
func_4886 = relay.Function([], output)
mod['func_4886'] = func_4886
mod = relay.transform.InferType()(mod)
mutated_mod['func_4886'] = func_4886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4886_call = mutated_mod.get_global_var('func_4886')
call_4887 = func_4886_call()
output = call_4887
func_4888 = relay.Function([], output)
mutated_mod['func_4888'] = func_4888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4758_call = mod.get_global_var('func_4758')
func_4759_call = mutated_mod.get_global_var('func_4759')
call_4899 = func_4758_call()
call_4900 = func_4758_call()
func_4476_call = mod.get_global_var('func_4476')
func_4480_call = mutated_mod.get_global_var('func_4480')
const_4917 = relay.const([[False],[False],[False],[False],[False],[False],[True],[True],[False],[False],[True],[False],[False],[False],[False],[True],[True],[False],[False],[True],[True],[True],[False],[False],[True],[False],[False],[False],[False],[True],[True],[False],[True],[False],[True],[True],[False],[False],[False],[True],[True],[True],[True],[True],[True],[False],[False],[False],[False],[True],[False],[True],[False],[False],[False],[True],[False],[False],[True],[False],[True],[True],[True],[False],[True],[False],[True],[True],[False],[True],[False],[True],[True],[False],[False],[False],[False],[True],[True],[False],[False],[True],[True],[False],[True],[True],[True],[True],[True],[False],[True],[False],[True],[False],[False],[False],[False],[True],[False],[True],[True],[False],[False],[False],[False],[True],[False],[False],[False],[True],[False],[False],[False],[False],[False],[True],[True],[True],[False],[True],[True],[False],[True],[True],[False],[False],[True],[True],[True],[True],[False],[False],[False],[False],[False],[False],[True],[True],[True],[True],[False],[True],[True],[True],[True],[True],[False],[True],[False],[True],[False],[False],[True],[True],[True],[True],[True],[False],[False],[True],[False],[False],[True],[False],[True],[False],[False],[False],[True],[True],[False],[True],[True],[True],[False],[False],[True],[True],[True],[True],[False],[True],[True],[True],[True],[False],[False],[False],[True],[True],[True],[True],[True],[True],[True],[False],[True],[True],[True],[False],[True],[True],[True],[False],[False],[False],[False],[True],[True],[False],[True],[True],[True],[False],[False],[False],[True],[False],[True],[False],[True],[False],[True],[True],[True],[False],[True],[False],[True],[False],[False],[False],[True],[False],[False],[False],[False],[True],[True],[True],[True],[False],[False],[False],[True],[False],[True],[False],[False],[False],[False],[False],[False],[True],[True],[False],[True],[False],[False],[False],[True],[True],[True],[False],[True],[True],[False],[True],[False],[False],[False],[True],[False],[False],[False],[True],[False],[True],[True],[False],[True],[True],[False],[True],[False],[True],[True],[True],[False],[False],[False],[True],[True],[True],[True],[False],[False],[False],[True],[True],[False],[True],[False],[False],[True],[False],[False],[True],[True],[True],[True],[False],[True],[False],[False],[True],[True],[True],[True],[True],[True],[True],[False],[False],[False],[False],[False],[False],[False],[True],[True],[False],[False],[False],[False],[True],[False],[False],[False],[False],[False],[False],[False],[True],[False],[False],[False],[True],[False],[True],[True],[True],[False],[True],[False],[False],[True],[False],[True],[True],[False],[False],[True],[False],[False],[False],[False],[True],[False],[False],[True],[False],[False],[True],[True],[False],[False],[False],[False],[False],[True],[True],[True],[False],[False],[True],[False],[False],[False],[True],[True],[False],[False],[True],[False],[False],[True],[False],[True],[True],[True],[False],[False],[True],[False],[True],[False],[False],[True],[False],[False],[True],[True],[True],[True],[True],[True],[True],[True],[True],[True],[True],[True],[True],[False],[True],[True],[True],[False],[True],[False],[True],[True],[False],[False],[True],[False],[False],[True],[True],[False],[True],[False],[True],[True],[True],[True],[False],[True],[False],[True],[False],[True],[False],[True],[True],[True],[False],[False],[True],[True],[True],[False],[True],[True],[True],[False],[True],[True],[False],[True],[False],[True],[True],[True],[False],[True],[False],[False],[False],[True],[True],[False],[False],[True],[True],[False],[True],[True],[False],[False],[True],[True],[True],[False],[True],[False],[False],[False],[True],[False],[True],[True],[False],[True],[True],[False],[False],[True],[True],[False],[False],[False],[False],[True],[False],[True],[True],[True],[False],[True],[True],[True],[True],[False],[True],[False],[False],[False],[False],[False],[False],[False],[True],[False],[True],[False],[True],[True],[False],[False],[True],[False],[False],[True],[True],[False],[False],[False],[True],[False],[False],[True],[False],[True],[True],[True],[True],[False],[True],[True],[False],[False],[True],[True],[False],[False],[False],[True],[True],[False],[True],[False],[False],[False],[True],[False],[False],[True],[False],[False],[False],[False],[True],[False],[True],[False],[True]], dtype = "bool")#candidate|4917|(588, 1)|const|bool
const_4918 = relay.const([-2.957469,6.785874,4.122315,-5.847094,-5.092153,8.453642,-4.437198,3.790719,9.075778,-4.668071,-9.851549,7.793257,5.900191,0.483209,4.518133,7.640440,-6.930220,3.233369,-9.234345,-7.503502,-2.359341,-6.575580,-1.638863,-2.424263,6.945913,-3.229596,-1.969968,8.630780,7.641865,-5.671365,-0.586878,-2.921966,-0.855217,-8.481190,1.672401,-8.421349,-0.357976,6.798996,-1.766336,-9.562477,-8.277919,4.064618,-4.503530,-1.810890,2.250212,2.874933,5.162301,3.452687,1.849889,-7.992716,-1.420554,-3.753510,2.567680,5.548394,-8.150717,2.088772,-4.814416,4.039674,3.043059,-0.878246,-5.454443,-6.157171,-1.143305,-8.197933,-1.544337,-5.847135,6.558804,3.828200,-1.651252,-4.149955,0.180333,8.948884,-9.299147,-8.624562,7.648195,3.832514,-2.749639,2.294897,2.477408,5.765620,-2.651275,-4.346315,-7.159653,-9.436713,-4.518334,5.810878,-3.501726,8.204741,0.295811,-1.558558,-5.172131,9.437047,-7.358686,3.252634,-1.792109,6.196117,9.687748,-3.714034,4.533468,-3.529934,5.766715,1.497393,1.764615,-8.003801,7.423792,1.653357,-1.987397,-9.241808,9.884028,-8.967247,-7.406128,-7.716200,7.454893,-7.140746,1.902168,-3.213650,-2.853868,-0.952802,-7.071925,8.376063,4.004759,-5.488076,5.175800,-9.259706,-1.532360,-0.984773], dtype = "float32")#candidate|4918|(126,)|const|float32
call_4916 = relay.TupleGetItem(func_4476_call(relay.reshape(const_4917.astype('bool'), [588, 1]), relay.reshape(const_4918.astype('float32'), [126,]), ), 3)
call_4919 = relay.TupleGetItem(func_4480_call(relay.reshape(const_4917.astype('bool'), [588, 1]), relay.reshape(const_4918.astype('float32'), [126,]), ), 3)
bop_4921 = relay.not_equal(call_4916.astype('bool'), const_4917.astype('bool')) # shape=(588, 126)
bop_4924 = relay.not_equal(call_4919.astype('bool'), const_4917.astype('bool')) # shape=(588, 126)
bop_4929 = relay.bitwise_and(const_4917.astype('int64'), bop_4921.astype('int64')) # shape=(588, 126)
bop_4932 = relay.bitwise_and(const_4917.astype('int64'), bop_4924.astype('int64')) # shape=(588, 126)
func_3045_call = mod.get_global_var('func_3045')
func_3048_call = mutated_mod.get_global_var('func_3048')
const_4936 = relay.const([[6.774648],[-6.320054],[-7.818422],[-9.558883],[-3.088607],[-9.485527],[6.974118],[5.310909],[-0.175561],[-7.067722],[-5.248312],[0.556303],[8.228398],[-4.811458],[-1.365402],[7.303957],[9.188478],[5.032830],[-2.536418],[4.971236],[-5.414273],[-0.081970],[-7.044738],[0.831506],[7.477627],[-0.712464],[1.681608],[-9.060334],[-2.741721],[-4.220491],[-8.143987],[-0.609993],[-5.913962],[9.740804],[2.674405],[9.257164],[5.629546],[7.812037],[-1.852806],[-5.257561],[9.860915],[5.618025],[6.406413],[0.168390],[-7.457218],[-0.874669],[2.591178],[-3.213835],[0.471568],[9.411005],[-1.081525],[-4.287570],[-1.154658],[8.024973],[-0.160039],[-6.249551],[-3.036246],[3.879311],[-8.524028],[1.049778],[-9.734680],[4.915270],[-0.522231],[3.377062],[6.678662],[-6.147199],[-7.149847],[7.733826],[-9.632204],[9.522905],[1.301433],[-9.548578]], dtype = "float64")#candidate|4936|(72, 1)|const|float64
const_4937 = relay.const([-10,10,-5,-9,-9,2,3,-9,-5,-6,5,-7,-7,8,-4,7,5,9,4,6,4,7,1,8,-6,-2,-6,-1,-9,-1,7,7,9,3,-4,1,8,-7,3,-6,10,10,-6,10,-10,-8,-1,1,3,-5,3,-8,3,2,3,-5,-8,10,5,-9,1,4,-6,-3,-8,-7,6,2,3,7,3,-10,6,5,9,10,5,3,-10,-10,9,-9,-5,6,4,5,-7,8,-6,-9,-9,5,3,-5,6,-3,-3,2,3,3,3,-7,-4,4,-10,-2,-1,6,9,-9,5,2,6,3,3,-9,5,-7,-2,6,5,4,-9,2,-10,-4,4,-2,-9,-10,-4,-9,4,7,-6,-2,4,-6,6,2,-8,-2,2,3,-10,6,-1,-2,-10,4,5,6,2,2,-10,4,3,-2,-2,8,9,8,8,8,-1,1,-6,5,1,-6,4,-10,-7,-1,1,-3,-3,4,-10,-7,-3,-9,7,9,-3,-10,-6,-3,-7,2,-6,-8,-5,-10,5,6,-8,-10,-8,5,-3,-10,7,2,10,2,8,-4,-4,-7,-4,8,-9,8,-7,-9,-2,-1,-2,3,-8,9,6,-10,10,9,2,5,-4,-9,10,1,-8,-10,-7,4,9,3,7,-4,-1,-10,-10,2,-1,-5,10,-4,-8,9,-9,-1,8,-4,7,3,-2,-1,-9,-6,-4,1,7,-2,-10,-2,-6,9,-9,9,2,-6,-5,9,-9,-6,6,-9,-3,-9,4,5,-8,-3,9,5,-4,-8,-7,4,-1,-3,8,-9,-4,7,2,7,-8,9,4,9,-6,-8,-1,10,-5,-9,4,-7,6,6,5,10,-6,9,2,10,4,-2,2,-6,-7,-1,3,-9,1,-1,-1,-10,-9,-6,8,10,4,6,5,5,9,3,4,-2,-7,1,-3,4,-1,-4,6,2,7,-8,-2,-6,-10,4,9,9,1,4,1,8,8,-5,-8,-4,5,-9,6,-7,-2,-10,-8,-9,-9,3,-2,-5,10,3,-5,3,9,-6,-7,1,5,-2,-10,-10,-5,8,1,-8,-3,1,7,7,-7,-3,7,4,5,3,-9,2,-5,1,-6,-8,-9,-7,2,4,-9,4,3,6,-5,3,3,10,-10,7,-10,-4,-4,5,7,7,-10,-9,-2,3,7,3,-1,-9,4,6,-1,-2,3,4,9,-3,-4,-2,-1,-6,-10,8,2,4,-3,9,-3,10,-8,-6,-8,8,3,-10,4,1,-5,-7,6,4,-10,-5,3,8,2,10,3,1,7,-2,-5,7,2,8,3,-9,-4,7,2,3,-9,1,3,10,1,-3,5,-8,-1,-8,8,-9,-4,4,-4,-9,1,7,-1,-4,-10,-1,-6,-3,7,3,-1,-10,3,-10,-10,-9,8,-5,-2,-3,5,-7,-5,7,-4,-7,-5,9,-10,4,-7,-1,9,-3,-4,-3,-2,-9,5,-7,6,-5,1,-10,2,-3,7,3,1,-6,2,-3,4,-1,7,7,4,-8,-5,-9,2,-3,5,6,-1,2,-6,2,-6,6,-3,-7,-6,-3,3,5,4,-8,-5,7,-9,-3,-4,2,6,-3,4,7,7,8,-3,-9,2,-8,-2,-4,3,-5,-2,7,8,8,-4,-1,-6,10,3,-6,7,-3,-8,9,6,-10,-2,8,-9,-1,1,3,-10,-9,-4,-9,9,-1,10,-10,-5,-7,-7,6,-1,-8,-8,2,-6,10,-5,1,10,-5,-2,-9,7,-4,8,2,-1,-4,3,-7,-6,-9,8,9,1,-8,-8,10,2,-10,7,10,4,7,9,-6,-2,9,2,8,9,6,5,-3,-3,-7,-6,-6,-10,-8,6,-7,-7,-8,2,4,-4,-1,8,3,-8,10,7,6,3,-8,6,-9,2,3,3,-5,10,3,-1,-9,-7,7,-9,1,5,-10,7,-7,7,2,7,-7,5,-5,8,-7,5,9,7,3,-1,4,-10,-6,-10,7,8,-6,-5,1,-7,8,-4,-3,9,2,8,-8,8,-5,4,8,7,-7,7,6,6,-5,3,1,5,-1,-3,1,-5,-10,2,1,1,2,5,1,5,4,-5,9,-2,3,1,7,-4,-7,2,-6,7,3,7,3,-2,-2,-6,9,3,-3,7,2,-4,8,8,-3,1,5,9,-1,-9,-8,-4,-2,10,-3,5,10,6,-9,1,9,5,-3,-4,-5,-7,-7,-1,-8,-4,10,6,-3,10,-7,2,-7,2,3,-4,8,-1,-10,5,5,-9,-1,7,-9,5,-1,2,6,-8,9,-7,-1,3,3,9,9,3,3,5,-8,-8,9,-7,-5,6,-6,10,-3,9,2,6,-6,-3,-10,2,9,8,-1,5,-9,9,-3,-1,3,2,7,-9,6,3,10,-5,5,-7,8,2,2,-3,2,1,5,1,1,7,1,5,-7,-10,-4,1,-8,9,6,-5,7,4,-9,-6,-6,-10,-6,8,-7,-6,-5,3,1,5,6,-8,6,-7,-8,7,-7,-10,-4,-6,5,10,-10,5,-4,3,-10,3,10,1,2,-1,-5,-3,9,7,-1,6,-1,5,1,5,6,7,7,-5,6,-9,-8,1,2,-1,-7,4,-8,-3,-6,10,6,1,5,-4,3,5,8,9,6,-2,-9,-10,7,5,4,7,-1,5,4,9,7,-1,10,4,1,8,4,6,5,-5,7,1,2,-5,9,6,-10,10,8,-7,-2,9,-4,7,6,-10,-8,2,9,6,5,-4,10,6,-10,7,7,7,-2,-5,-10,3,6,-6,7,2,8,9,-2,8,-10,-3,4,2,-8,-4,10,4,7,2,6,9,2,3,-5,-5,7,-3,1,5,-10,8,10,-7,-6,4,5,-5,1,10,-9,10,6,-5,9,-8,2,-1,10,1,9,7,7,10,7,4,8,2,-7,2,-8,5,8,10,5,3,5,9,-1,-9,-2,6,7,3,4,10,-8,10,2,-6,-3,3,1,1,-3,-4,-5,5,8,-8,7,-6,4,3,-8,-2,-7,1,9,10,2,8,-6,-1,-3,9,-6,5,3,-7,6,-3,6,-1,-6,10,-6,-7,-3,7,7,8,-2,-7,-2,7,-4,10,-6,7,-1,2,-5,-10,-9,-6,2,2,-8,1,1,-7,10,-5,8,10,6,7,-3,2,3,-8,2,10,-9,10,-9,-5,4,-7,9,-2,-1,8,7,6,6,8,2,-9,-9,10,-6,10,2,-4,7,8,6,-2,4,2,1,-9,8,-5,7,-8,10,-6,-5,5,-6,-8,9,-3,9,6,-7,-3,2,-5,-3,5,9,8,-10,4,6,-8,3,9,-9,1,9,-3,4,-4,-1,10,10,3,-1,-8,10,-5,7,6,8,-4,-3,-9,-4,-4,2,4,4,-4,4,-3,5,-9,1,-8,3,7,8,-3,-1,-9,10,6,3,-8,-9,-1,-10,-7,-6,-1,7,-6,-6,-9,-7,9,-4,-3,3,3,-4,-6,-7,-7,-8,-5,-8,9,-2,-10,-7,-8,4,-7,3,-10,-4,-3,-9,-5,1,-3,-1,-5,-3,3,6,2,-1,6,8,-10,2,5,-4,-10,10,-5,8,-5,-5,-2,10,-10,2,4,3,4,9,-7,-2,7,-4,5,2,-2,10,9,-7,-10,6,9,-10,-5,4,2,-10,-2,-3,6,-8,-4,4,8,-4,-10,-2,10,-4,3,-8,8,5,-4,-6,6,1,-2,-5,4,-9,-2,5,-5,8,1,-4,-5,8,9,-10,-7,5,3,2,-1,-6,-1,6,2,-5,-1,-9,-10,-4,10,-6,-4,-8,2,6,10,6,-3,-7,-8,5,3,-4,2,6,3,-10,-2,3,10,-9,1,10,-10,8,-1,-7,-10,9,-2,-5,6,3,-6,4,-8,-4,10,5,-3,10,-10,10,2,4,-6,-3,6,10,2,6,9,-1,6,-1,-10,6,-1,-2,8,1,6,-6,-7,2,2,-9,10,2,-7,4,7,7,-6,3,4,-10,7,3,-4,-3,-5,-9,-4,10,7,9,3,4,-5,-7,-2,-1,3,-2,1,5,-10,10,7,-5,5,10,10,-1,-2,5,-3,2,-10,-3,2,4,2,7,-5,6,6,10,-2,2,7,-8,2,8,-6,3,-1,-9,-3,4,9,-2,8,5,-2,3,-4,2,5,-8,-3,9,9,6,-6,-2,4,2,-5,-3,-3,10,1,3,-4,-5,3,-10,3,4,8,-6,9,6,6,5,-8,-7,5,-3,1,5,-3,6,-2,-9,6,5,-5,1,2,1,9,7,7,4,-9,4,7,-9,-8,-1,4,-10,-1,-8,-7,1,6,3,-9,3,-7,1,7,-2,8,1,-3,1,-4,-7,10,10,-7,1,-7,5,3,9,-5,5,6,7,9,-3,9,-5,-9,4,7,3,4,-9,3,-5,8,-6,-7,6,-1,10,-1,6,1,4,-9,-3,7,10,-9,10,6,-4,9,1,-10,-7,-8,-9,-6,9,1,8,4,-8,2,10,4,-5,5,2,-8,4,-3,-7,7,-6,-7,-4,2,-2,2,6,-10,-10,6,-10,-2,-2,-9,-5,4,5,-6,2,1,-4,-8,10,1,2,-1,-2,1,7,3,-6,-3,-10,-10,-7,-6,3,-1,-1,2,-8,10,-3,3,10,-1,-7,-5,-3,7,5,9,9,-2,10,6,6,-9,-4,10,2,-10,6,-4,-2,7,6,9,7,6,5,7,-7,-2,-1,-6,-4,10,4,8,-6,-5,-2,8,6,-9,7,6,-10,-8,9,-4,2,2,7,-2,-7,-5,-3,-10,-8,-2,3,-10,4,-6,2,7,-3,10,1,2,10,6,-2,-2,7,7,2,5,-5,-1,2,-3,-9,2,6,5,-1,9,1,-6,-5,-8,-2,5,5,-8,-5,1,-3,-1,7,5,9,5,-5,-8,-8,7,1,-9,7,-3,-10,6,7,2,-5,6,-9,6,4,4,10,1,-3,-8,-10,5,-5,-1,10,10,10,-9,-7,-5,-1,-10,-10,4,1,-8,-5,1,5,4,-7,1,10,-6,-7,7,-10,10,-8,-5,-6,-2,-7,-1,-4,8,-1,9,-8,-8,6,2,-2,5,-7,-1,-3,-4,-3,-1,-1,-10,-7,-4,2,2,7,3,6,-1,6,6,2,-10,-6,-6,1,9,-3,-2,9,6,-8,7,-4,-1,-8,-2,8,9,-4,-10,9,10,4,-10,8,1,4,3,4,-10,10,5,5,-1,9,1,-1,-1,-7,-10,-8,2,-8,-1,9,-7,5,-9,5,9,-9,3,3,7,-6,4,7,-7,-3,7,10,-2,-5,-5,-1,6,3,10,-3,8,3,7,-10,-2,3,-6,3,-7,-7,1,-5,7,-6,7,-5,1,9,-9,4,-3,-3,9,-4,-4,-1,10,2,5,8,9,9,3,-10,6,-6,-1,7,-6,-8,-6,7,-4,-5,7,5,9,8,1,-6,1,5,2,-4,4,1,1,-8,-7,8,-8,-1,-6,-9,-6,3,1,-1,-1,-3,7,5,-2,-6,5,2,-6,10,-4,8,-6,-9,-10,-9,-3,6,-6,9,5,6,9,3,1,-9,4,4,10,-8,4,-1,-2,9,9,8,3,-4,-10,-8,-4,-7,-6,-10,-4,9,8,5,9,9,-1,-4,9,-7,-8,-1,1,1,-10,-6,-1,-2,-4,-10,2,3,-6,-8,-4,5,1,4,-5,1,-10,-10,1,2,1,-8,-3,6,7,-4,10,-5,-5,-5,8,6,3,10,9,9,6,-3,-8,8,-5,-8,-2,-8,-6,9,-10,-1,-2,7,3,-1,3,7,3,9,-8,6,2,6,8,-1,2,-3,4,-4,-8,-7,-9,2,-10,3,-10,7,-3,-1,10,-1,-5,-7,-6,6,-7,3,-7,-9,10,6,-1,1,8,8,3,2,-6,6,9,-4,-7,2,5,-3,-5,4,-6,1,6,-3,1,-8,-2,6,6,-8,10,9,1,-10,-4,4,9,3,-7,6,-2,4,9,-7,-4,10,-5,7,2,4,-2,-4,-6,-6,-3,-2,7,9,7,-2,1,3,10,3,9,-8,6,2,10,6,2,-8,-3,6,-5,1], dtype = "uint64")#candidate|4937|(2288,)|const|uint64
call_4935 = relay.TupleGetItem(func_3045_call(relay.reshape(const_4936.astype('float64'), [4, 3, 6]), relay.reshape(const_4937.astype('uint64'), [2288,]), ), 2)
call_4938 = relay.TupleGetItem(func_3048_call(relay.reshape(const_4936.astype('float64'), [4, 3, 6]), relay.reshape(const_4937.astype('uint64'), [2288,]), ), 2)
uop_4944 = relay.asinh(bop_4921.astype('float32')) # shape=(588, 126)
uop_4946 = relay.asinh(bop_4924.astype('float32')) # shape=(588, 126)
func_4724_call = mod.get_global_var('func_4724')
func_4726_call = mutated_mod.get_global_var('func_4726')
call_4954 = relay.TupleGetItem(func_4724_call(), 0)
call_4955 = relay.TupleGetItem(func_4726_call(), 0)
bop_4957 = relay.bitwise_xor(uop_4944.astype('uint8'), relay.reshape(bop_4921.astype('uint8'), relay.shape_of(uop_4944))) # shape=(588, 126)
bop_4960 = relay.bitwise_xor(uop_4946.astype('uint8'), relay.reshape(bop_4924.astype('uint8'), relay.shape_of(uop_4946))) # shape=(588, 126)
output = relay.Tuple([call_4899,const_4918,bop_4929,call_4935,const_4936,const_4937,call_4954,bop_4957,])
output2 = relay.Tuple([call_4900,const_4918,bop_4932,call_4938,const_4936,const_4937,call_4955,bop_4960,])
func_4963 = relay.Function([], output)
mod['func_4963'] = func_4963
mod = relay.transform.InferType()(mod)
mutated_mod['func_4963'] = func_4963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4963_call = mutated_mod.get_global_var('func_4963')
call_4964 = func_4963_call()
output = call_4964
func_4965 = relay.Function([], output)
mutated_mod['func_4965'] = func_4965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4325_call = mod.get_global_var('func_4325')
func_4326_call = mutated_mod.get_global_var('func_4326')
call_5081 = relay.TupleGetItem(func_4325_call(), 2)
call_5082 = relay.TupleGetItem(func_4326_call(), 2)
output = call_5081
output2 = call_5082
func_5113 = relay.Function([], output)
mod['func_5113'] = func_5113
mod = relay.transform.InferType()(mod)
output = func_5113()
func_5114 = relay.Function([], output)
mutated_mod['func_5114'] = func_5114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4386_call = mod.get_global_var('func_4386')
func_4388_call = mutated_mod.get_global_var('func_4388')
call_5123 = relay.TupleGetItem(func_4386_call(), 1)
call_5124 = relay.TupleGetItem(func_4388_call(), 1)
uop_5131 = relay.atan(call_5123.astype('float64')) # shape=(7, 2, 5)
uop_5133 = relay.atan(call_5124.astype('float64')) # shape=(7, 2, 5)
func_4446_call = mod.get_global_var('func_4446')
func_4447_call = mutated_mod.get_global_var('func_4447')
call_5135 = relay.TupleGetItem(func_4446_call(), 0)
call_5136 = relay.TupleGetItem(func_4447_call(), 0)
output = relay.Tuple([uop_5131,call_5135,])
output2 = relay.Tuple([uop_5133,call_5136,])
func_5137 = relay.Function([], output)
mod['func_5137'] = func_5137
mod = relay.transform.InferType()(mod)
output = func_5137()
func_5138 = relay.Function([], output)
mutated_mod['func_5138'] = func_5138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4724_call = mod.get_global_var('func_4724')
func_4726_call = mutated_mod.get_global_var('func_4726')
call_5139 = relay.TupleGetItem(func_4724_call(), 0)
call_5140 = relay.TupleGetItem(func_4726_call(), 0)
func_663_call = mod.get_global_var('func_663')
func_666_call = mutated_mod.get_global_var('func_666')
const_5142 = relay.const([[8.710279,-6.020286,-8.649231,6.465432,-2.023093,-0.744836,5.981112,5.418679,-8.605230,-9.449939,5.291075,-8.028100,-9.466604,5.002203,-4.787811,-5.059697,8.321010,-1.278574,-2.983003,-8.445403,6.015622,9.072669,4.833656,-8.721547,-2.830863,-6.688934,-8.513979,-9.626536,2.397764,9.335628,4.475166,9.617225,-0.117806,-8.332897,-6.248305,9.582746,-2.102961,-9.711944,6.683792,4.140762,7.516513,-3.194458,-9.022867,1.570854,-8.379595,-5.831045,-8.484013,-6.011645,0.938976,-1.970115,4.758336,-0.324370,-6.204840,-0.876272,4.924745,-1.690507,4.712122,-3.879681,8.375540,8.014051,3.800985,9.753721,-6.989092,-9.573127,0.626987,6.951874,8.837910,-5.255652,-2.308505,5.597680,-1.619981,4.781673,-0.644610,-3.499597,9.619313,3.184549,0.073256,-3.420840,-0.414449,5.221212,3.480584,8.660838,-9.915663,3.803999,-1.149811,-2.484097,-8.958776,-0.097366,-2.908567,-4.394351,4.754481,-5.224878,-2.388645,-5.586857,8.705340,-5.875593,-7.937449,6.643450,3.553628,6.406516,-2.790707,7.153254,7.022540,5.956286,-7.215662,1.258792,-1.851040,-7.819656,7.887169,7.136093,-7.699204,7.781100,9.257083,-7.521140,6.833129,-0.640412,6.220772,-9.972496,-3.821545,-9.112494,1.276925,-7.152873,9.662654,0.619158,8.854028,-6.344405,-2.607209,-6.505661,-1.876420,8.555223,-0.301517,2.245343,5.484009,5.777058,-0.435929,-8.532342,7.076046,7.994583,6.957825,8.996886,5.044008,-1.444880,-5.585528,-8.418235,3.093474,-5.590175,4.547920,-6.913048,-4.571204,-2.294769,1.517339,-0.545015,2.986957,-8.805975,-6.455135,8.913234,4.063457,-4.650434,-4.936992,-1.665889,-6.536604,-3.261317,8.444794,-6.176105,-1.382104,-6.349797,7.628905,-5.012464,-1.879034,9.437257,5.632298,-5.182830,-5.495114,-9.007733,7.781382,6.120254,8.836782,-0.937540,-8.117941,-4.831727,4.350876,-1.861056,-3.135896,-2.355081,8.088801,9.365327,-2.759929,0.729570,-1.944491,-7.822400,5.187048,8.253584,1.292035,5.784407,-4.448564,-0.231273,-1.805518,-8.970749,3.776219,0.502080,-9.422736,6.644435,-9.374281,-0.365368,-9.249888,5.472304,-2.187654,8.714176,-5.567579,4.577058,-6.219765,-4.193191,-7.511120,4.420829,6.427868,7.045704,-9.637228,0.917993,0.183560,3.606015,-9.684005,1.130233,-2.991745,-0.121700,3.241980,1.809707,0.591982,-3.968627,3.959908,4.558894,-6.806997,-8.870818,-3.095514,-7.801098,9.687155,7.168102,-7.100696,-2.378422,6.351565,0.995718,-9.604064,9.290630,-2.801843,-2.185227,4.069882,9.337026,-2.000178,-3.129933,6.258047,-9.848323,6.404411,-2.656747,5.347255,-9.877113,7.918333,3.932003,-2.748264,8.339590,6.062790,-0.211248,9.521114,-8.027889,-2.369881,-0.474560,2.170141,-0.301060,1.612976,-0.197441,-8.334775,4.287652,-1.383747,2.272453,9.960672,-9.858502,-8.201678,-2.646614,-8.774958,7.623050,5.942532,-9.508662,7.332041,4.904599,3.110215,8.313917,-8.429946,9.208917,0.645255,-2.797109,9.738915,9.727327,9.446731,5.231403,6.619123,-8.820325,0.743422,5.478720,-6.153132,9.689970,2.514145,6.170442,8.087676,-7.299241,6.295317,-4.615199,1.492854,1.591340,1.888631,-0.113676,7.480796,6.572136,7.783688,3.247562,-7.925555,3.891056,6.763229,0.705996,8.593331,-4.789406,-1.276413,8.919442,-9.531755,5.215629,-0.708431,-2.799362,-3.538684,-9.251851,3.494049,0.767265,-8.961346,5.403543,3.514610,-9.748076,-0.389641,-5.890889,7.842451,3.982430,-0.790146,8.925225,-0.887060,-0.955396,-6.960978,2.803977,5.345353,1.656160,3.303718,8.375977,6.574296,-7.695477,-7.746660,4.802094,-3.451506,-4.892729,9.698633,5.399456,9.660176,-9.557308,-2.337284,2.768455,1.487538,1.532297,7.209355,6.044431,8.319950,1.427316,-5.513639,4.512418,6.585132,4.353603,-8.696676,-9.443564,6.399929,5.323167,-4.880570,4.086310,5.441467,2.673912,4.647484,5.831489,-8.805745,6.561492,1.256760,7.000852,-9.711204,5.738494,-9.884006,-5.164172,8.821859,0.355455,0.617149,8.919228,-5.653664,0.425111,8.857924,-6.476062,3.943358,4.611717,-2.974583,6.973793,1.773629,4.796292,4.799505,7.647383,9.912191,-8.973231,1.481485,4.378893,-0.595170,-1.281617,-3.938686,9.255735,-1.628197,-6.608206,-1.585316,4.589797,2.849555,3.692826,-9.234176,6.293089,6.003851,-8.905091,0.649296,-0.917586,1.692742,2.223997,9.856989,1.387264,2.607317,6.405457,-7.644089,-7.604515,3.140946,-3.117942,-3.191133,-3.204420,6.157113,3.669039,-3.774878,4.686506,-7.146987,3.438828,6.965795,6.494725,9.606556,-9.905000,0.110680,7.330796,-4.384046,-3.149507,3.597851,8.758877,-2.457645,2.118878,-0.475596,-5.204568,5.837145,0.224352,-4.142661,-6.657286,3.543710,6.526134,7.685280,0.468393,-9.296879,-6.408016,-0.898112,0.093461,-8.919362,-3.980719,9.095383,4.486637,-8.657599,5.729057,7.080762,-1.432598,4.642098,5.540409,-9.028343,-2.172079,9.594499,-1.926937,-9.696737,-2.984498,-3.689289,-7.912729,4.202281,8.899608,-2.117794,-8.405328,-6.092102,-5.468562,1.772644,-8.644801,-4.131241,-2.027238,6.139867,-0.672994,-8.024292,4.288176,9.579471,-6.336352,2.372295,-5.486254,6.410224,-7.125576,-5.774581,6.878632,-7.544704,3.320427,-1.912963,-1.283565,5.178217,-1.878040,3.942744,-1.261008,1.988689,8.076019,-5.007341,-7.750045,6.620298,8.746136,3.493839,8.283482,-5.885265,-6.764132,-5.977436,5.557908,0.650956,-6.691861,8.872805,4.341734,5.475902,0.039736,3.710490,2.024694,-8.867514,-4.015778,5.850789,-6.745683,-8.853202,8.583333,5.781424,-3.091178,-6.306634,-8.014365,-5.207922,-1.839600,-9.537892,5.699162,0.042779,-3.788692,-5.560682,6.543085,-9.028110,5.375202,-5.354432,-9.913795,6.943502,1.288572,8.052179,7.848096,5.000381,1.405685,-3.049646,8.440165,-6.324017,9.622826,-2.162004,-0.614585,-9.614148,-0.942376,-8.481455,5.302712,8.811287,3.229324,-2.149293,-3.050634,-7.869948,3.368819,4.915424,-7.426173,6.019023,-3.998200,-4.837394,-6.408817,-9.537039,-7.918998,0.710113,5.176559,-0.315834,5.831949,8.268073,-5.916954,-7.864316,-1.543434,0.320360,5.724941,2.497135,-4.471171,-3.991935,-0.465386,3.420434,-0.752951,-7.733581,-9.834898,-7.400100,3.087946,4.361258,-1.345012,-7.066527,6.971719,8.337893,-6.273347,-2.019663,5.648621,1.739840,-0.280463,-2.720514,-8.631633,-1.882842,3.954996,-5.047092,-8.041934,-5.800733,1.953553,-1.628079,-3.790714,9.220049,-0.933256,-3.853931,5.437911,7.681050,-8.794392,-6.343861,7.124930,1.209348,1.526818,9.064149,-3.069935,-1.345898,-4.029222,-2.507177,6.142549,0.346078,-6.452294,1.033158,-6.042656,6.379917,-4.550626,8.309677,-9.225541,-3.916087,-8.406933,0.013463,5.499584,4.178993,-9.904760,0.632744,8.556775,6.944095,-8.677441,8.098715,-0.702262,9.135311,-8.371910,-7.547496,-1.118933,4.733242,-4.123474,4.490664,-0.990818,-9.239868,-5.221280,-5.881285,-0.613430,4.475508,-9.194016,0.245125,8.270589,4.975521,2.416430,-5.797493,-9.823367,2.361690,6.906927,1.080590,3.025989,-2.389064,0.898720,9.321697,5.577101,-6.636051,-7.412971,-4.387400,-6.333738,4.870445,3.920608,4.049370,6.225905,-2.984696,2.940831,8.326423,6.050214,7.948348,-5.944324,9.559464,6.018847,-5.734296,7.505953,-8.361817,-2.310650,-8.955771,3.207137,-0.630709,-9.504251,7.268933,-6.613741,-7.213006,8.524556,-0.469214,-6.822361,6.399910,4.215030,5.090283,-8.495371,-1.341715,-2.973955,-7.552824,5.461060,-4.693853,6.018391,8.039793,-8.607967,-1.377913,2.455402,-2.037828,-3.970067,-1.979164,5.449648,-2.620703,7.369392,-7.330793,2.832447,8.026326,0.993587,-7.123050,-8.438049,-7.530455,5.603338,-7.847381,5.629491,6.710473,-1.846029,0.535896,4.588981,1.603769,6.330841,-2.237636,-8.529186,7.651313,-3.712629,-9.910953,2.210713,0.454038,6.910112,-7.909022,-5.987128,-2.472965,5.555006,-2.118961,-8.065069,7.426117,-9.760989,-9.036359,1.492510,-9.825446,-0.852842,-5.923514,-9.342547,-4.782067,5.662613,-8.048477,-0.464026,-1.168253,2.884964,5.926607,-3.378240,4.227360,-8.352746,2.298007,5.939220,2.651799,4.554636,5.083248,-1.968088,0.221191,-6.685431,9.824474,7.770131,-1.003150,0.869818,-8.156055,-7.810241,-7.268918,2.528800,4.390175,5.885236,-3.283315,-7.910449,-4.866766,-4.880776,8.014307,-4.184843,5.998714,-2.204032,-7.032749,9.777713,-0.232675,-1.860245,7.836949,-5.499110,-3.933177,7.551437,-0.606143,-2.044381,-4.707603,3.391184,-1.274638,8.205553,9.185101,2.206236,0.004906,-4.528203,4.061356,-4.789945,-2.645982,2.521024,-8.138102,-2.974953,-0.267851,-3.954755,3.238441,-6.464413,4.718288,9.134890,-9.808121,-1.091126,-1.267597,3.875791,7.681918,-2.644275,-5.255848,-1.597363,-4.617506,-1.704111,5.670425,-1.675974,-5.762450,-4.941198,-1.328971,-7.717591,7.991272,-5.026948,0.932419,4.143208,2.328609,-0.272300,3.885258,-1.480267,5.450792,-8.195135,0.377622,5.596171,-3.356328,4.156012,-5.197876,4.085599,-7.084995,3.053514,8.061544,-1.980111,-7.997501,-5.400258,6.184442,4.071445,3.853340,-4.222080,-5.095160,-6.109154,8.495276,5.026226,7.469017,6.780910,-4.759672,3.461796,6.244155,-6.885311,5.918141,5.553107,-1.406439,2.181723,2.631234,-3.209276,-9.365190,-1.356807,1.427463,0.091050,-7.625766,-8.002209,2.580684,-8.139525,-5.969488,-3.201624,1.611440,-0.057964,-2.647588,-8.518752,8.554669,-9.872264,0.757201,-4.438008,-5.402193,-3.490788,-1.640302,-9.979576,-1.868214,7.854855,5.584264,-0.647551,2.835938,-4.687038,2.171584,5.995265,-7.406097,-0.912675,-1.146999,-6.098168,-1.769376,3.390494,8.789611,-3.046798,-5.417900,-6.058791,9.365614,8.286842,-3.123673,-1.937249,-4.251366,-7.977130,3.940799,-3.658986,9.954245,2.144255,6.644560,2.757690,-9.738304,4.111599,1.057068,-9.892751,-5.119359,2.836397,-8.831141,-7.145273,-1.293207,1.376538,4.394445,9.916921,-4.495976,-8.953025,-4.663636,-9.112642,6.691758,3.445811,-6.016442,0.746662,2.452914,3.866623,6.660693,-1.942586,-9.514193,7.057938,-3.526837,7.757618,4.698909,-2.827229,8.475648,-6.281076,-3.153949,6.599152,-3.458948,-1.124740,4.449611,4.439645,0.908901,-4.081953,3.932793,-1.621052,9.607520,-5.228771,8.226112,-1.724271,7.704332,-5.476470,-1.873778,-8.283945,-9.124949,7.314184,-0.623787,-0.964299,-1.082558,-3.922218,4.594769,9.889606,-5.798846,1.004339,7.662688,-7.703932,8.367885,-8.669765,-2.225196,-4.642479,3.385902,-0.762409,-7.647065,-0.449913,-3.686797,-2.323345,3.606837,-3.073188,5.759431,5.646634,9.305578,1.978460,-7.713327,-5.201089,1.933788,-5.536045,-5.893396,-8.286917,8.938113,-5.450908,8.064112,6.689636,-2.354095,-1.921572,-6.754090,-6.410314,7.048113,-6.218875,-0.760245,-3.946078,6.855395,-6.811198,-6.959580,-7.463475,2.624605,8.639743,0.678745,9.928977,-1.260538,3.506732,-4.034249,-8.891832,3.909100,3.975719,0.763496,7.426588,-9.784501,6.948048,9.805893,4.585854,-4.372113,6.715278,5.079011,8.881021,3.274994,-1.542078,1.160729,2.652518,5.882924,-9.283841,9.019928,7.012819,2.081981,-2.791322,-7.940266,-3.089277,-0.254777,-1.117862,-1.380944,2.385302,-9.797483,8.005181,-5.015441,4.490107,-1.987893,-3.453293,6.950458,0.833140,-9.913168,8.803109,7.741491,3.085071,-2.204400,-0.139354,-7.465941,-0.985599,5.862210,-7.161561,-4.911964,-7.965177,3.212062,-3.747068,-4.804856,9.827487,4.112084,-7.185495,-9.866848,-5.120126,6.214919,-0.269539,-6.999753,2.878987,-3.240991,7.890308,0.535178,3.518838,8.257458,6.403564,-4.842209,-2.029744,-8.038383,-3.606775,7.391363,3.302345,1.389139,-8.095123,-6.952170,-8.014655,4.975170,7.661134,0.168077,7.333179,1.464203,-6.017426,2.143456,5.799288,0.339496,5.569347,0.049654,-5.421033,-8.925995,-8.913899,-2.801155,4.022278,9.031199,-6.054666,-6.281689,2.280436,-8.502002,3.587146,-8.690611,7.265331,-5.951755,-4.336339,0.277857,1.429222,4.081671,-8.240093,-7.095603,1.947116,0.854738,-2.645861,3.277268,7.211573,8.186216,-0.359686,6.117829,-9.195833,-3.732172,6.467061,2.868178,4.492431,3.768406,-3.921956,1.436885,0.455692,0.508373,-3.809588,7.139300,-3.864643,-2.792872,-2.534555,4.341312,-9.626482,-2.119641,6.750488,-7.951329,-4.583723,4.071022,2.488964,1.972176,7.612391,-1.018165,3.525023,0.326854,-0.112968,-8.368758,7.228852,3.143246,3.647396,-3.547021,5.809679,7.130292,-5.968641,-1.193504,-6.569798,-5.983475,-2.435529,1.682833,-9.547768,-8.634449,8.490368,8.098911,-4.925438,-9.310846,-3.674142,-2.862974,7.072903,-0.279107,-0.070738,8.593741,-9.238175,-3.736536,-8.932799,-8.062653,-4.388899,5.938498,-4.157409,8.322833,-7.625459,-4.122583,-1.169805,-3.514429,2.670561,6.378826,-2.254982,-2.467860,-7.568013,6.078119,-4.529864,7.565110,-0.368499,-9.494251,6.400818,9.637928,5.645279,5.855275,2.993498,7.492174,-9.195614,-9.050720,4.340019,2.777045,-3.724680,-9.817329,-7.953538,9.184487,4.551658,8.998404,5.360258,-8.654127,5.334891,-3.073576,7.953992,6.170227,-8.583545,-6.955645,-0.912530,7.794080,1.084608,8.751124,4.402370,-0.655326,9.251248,-6.041080,0.714922,3.267561,-8.181899,1.541459,-6.516721,5.869821,-6.089491,-7.323904,4.114949,5.966386,-4.924038,-5.189541,-2.326538,-3.637999,1.669105,-6.848629,7.578486,4.723966,-2.048880,7.079581,0.462755,5.545506,1.666040,-8.489620,-2.843360,8.153557,-4.252905,-0.958298,-1.216115,-1.602803,3.214459,-9.027000,4.254330,-8.850276,-4.212524],[-0.112603,-6.865076,-5.445430,8.236993,-3.462959,-5.341112,-9.868412,-0.897638,3.455736,7.316681,-9.784082,6.924650,8.417770,-8.033447,-4.149062,-0.836166,-0.033796,-8.907888,-5.281669,9.277733,8.407644,-3.508457,-4.869414,9.607281,7.363785,-4.480252,2.963441,9.130108,-9.760828,7.328662,-7.658937,9.165150,-4.479466,4.573524,0.990821,-4.567699,5.444784,7.012910,5.001753,9.208800,5.066480,-0.951475,8.563902,-8.528542,5.680962,-6.908113,4.141970,-1.131129,-1.366452,-9.932548,-7.025070,-3.735265,6.728500,3.515377,-9.837643,9.982544,-9.028557,0.727115,9.968757,9.428689,1.913688,0.093696,8.667150,-5.920901,4.637180,-0.371175,0.780073,2.612401,-3.894585,8.899671,-4.180932,-9.956045,-9.871193,-4.069570,2.090188,-4.375910,-4.032292,9.080388,6.108663,1.364278,-1.026179,-8.387346,-2.688781,-9.011259,8.319035,-2.291488,5.213475,-4.125201,-9.243839,4.534305,2.408991,-3.260386,3.380523,0.305810,3.501923,-6.195286,-7.120313,-7.170094,-9.870880,1.590652,-7.241756,4.185217,7.855781,-0.187056,6.766978,6.011229,8.001823,-6.387175,-2.122992,-4.690753,-3.732778,9.894364,2.004554,4.033854,4.013039,6.704810,-1.204264,4.632245,5.197456,1.901719,8.462874,3.730019,-0.119921,-3.772682,7.282806,3.283959,5.100438,2.402809,-6.437426,-1.479579,1.043429,0.190962,6.421964,1.703333,-8.555249,3.618477,-9.569934,5.114997,-6.086923,5.377256,-1.227835,4.730874,5.099384,-7.086411,2.496757,8.514501,8.602030,0.185088,6.267712,6.118991,4.230550,-1.237541,1.396156,2.377371,1.080833,4.900304,7.720809,2.237242,4.823931,-0.358758,-3.361149,-6.728299,-6.757886,-1.824011,-3.550689,-2.548097,-7.358867,7.052731,-4.131276,2.079151,1.859694,7.569877,7.584814,-2.300706,-5.075079,-4.998189,-0.533226,-3.730364,-1.008066,2.745960,-7.432742,-8.331762,-3.292453,-4.604908,-3.643380,-7.367545,2.691343,-3.412236,-7.897581,1.764712,6.211768,7.822316,-1.098438,8.545376,0.550786,-4.834930,-5.668863,-2.364127,-7.303694,7.647194,4.986125,6.151325,1.380090,4.392106,-4.762963,-6.825568,-2.189273,7.173220,-6.671647,3.720916,8.492584,0.753012,1.684035,-5.885662,9.767973,-1.920628,7.515388,5.546140,-9.162926,-9.101869,3.817489,-4.574151,7.194283,2.260772,-1.983734,5.100246,-2.075606,6.837850,-0.504351,9.548020,1.043592,-2.950970,0.345154,5.644287,5.198123,-4.775483,1.666226,-2.494676,4.237545,-4.163073,1.484141,2.976236,-7.483432,5.288726,8.010640,-7.163301,-1.941856,0.269124,-7.732030,1.388676,7.038065,0.929955,4.260481,7.262764,0.687534,-2.537527,3.724137,-2.698124,5.904905,-5.719000,-2.304157,4.779987,-0.433667,6.936963,-3.113712,-0.983873,-8.785547,-9.775476,1.328500,-4.925612,4.789983,5.802464,5.392631,-2.203220,7.857557,6.255559,-7.472609,9.852038,2.719455,5.706111,8.408728,9.458838,7.446902,3.917444,9.866268,6.091706,9.487600,2.375397,-1.357653,1.392527,2.164069,-3.713687,2.186256,-3.974423,-6.848445,-7.065859,7.780697,6.997072,4.252010,9.153322,4.647646,3.334852,-4.676291,1.450298,5.068250,-4.967248,5.417158,-3.665278,-9.098564,5.475042,-2.163981,4.553685,-5.863708,3.501878,5.540168,-8.970400,3.103481,8.708436,6.548548,1.396585,7.109657,3.965179,-3.453997,-7.241861,-6.087236,3.387496,2.424529,-4.184333,4.193307,-9.407953,-8.976070,9.011123,-2.751580,1.758379,6.269427,-7.920516,7.399275,6.375287,7.202525,-8.963532,-7.119292,3.163753,-7.835823,3.694830,0.729383,5.357425,-7.085686,9.074457,0.916585,-2.211626,8.677160,-0.409201,-4.991437,-6.668915,1.526964,1.548756,-4.883190,1.418614,-0.204493,6.584102,-8.135937,-8.370729,3.964070,-0.329957,-2.166517,-0.628022,0.653078,-0.682966,-2.475354,-7.233009,-7.859783,4.559693,-2.143848,5.617221,9.086170,-7.950422,1.625720,5.924634,-8.578510,-7.983685,-1.246063,4.529710,7.344594,-8.904418,-2.868125,1.727620,-5.314525,-4.019472,4.440563,-4.304578,-4.075581,0.039574,6.621443,-8.474862,-4.878786,-6.985361,9.867486,-2.170187,-4.325852,6.352211,8.253085,7.424146,2.038828,-1.357683,3.190650,-4.753419,6.785441,-4.114324,-7.154580,1.668046,2.784298,4.839183,6.571395,2.633671,-6.101667,-4.458602,9.636944,-8.152090,1.474314,2.823980,1.837181,-0.743663,0.257592,4.859628,-4.044069,-1.806678,-1.278246,-8.437955,-8.867257,4.494670,-4.044061,-3.108139,8.577312,4.450506,-9.777267,-8.218670,-4.720746,-8.102948,6.370330,1.374796,-8.426167,0.406237,1.741737,-6.907760,3.674561,9.451746,-8.731753,5.252169,-4.342999,-4.929679,5.676654,-1.031996,-0.771842,-3.342494,-6.308745,7.538816,9.256455,1.455910,-2.394412,-0.825346,-2.838694,-0.457014,-5.907613,-8.000480,-0.153032,3.304875,5.355059,9.631745,-2.894056,0.063696,4.548419,-3.937391,7.139018,3.986927,7.878844,1.168475,0.344827,-8.261434,7.968885,-2.941777,-5.320284,-9.343109,8.262281,2.512326,8.108367,-2.343184,6.075415,1.863916,1.629959,-9.842833,6.476405,-2.617108,2.184016,-6.724258,8.941985,-4.837193,-3.180466,-5.523142,-5.097537,8.495887,-5.023255,-8.355362,-2.445526,4.995295,6.042392,4.714009,4.723353,5.368003,-9.192745,-3.173436,6.215629,4.724004,3.762513,4.211813,8.046917,8.320328,6.107894,2.825460,5.565220,1.217606,5.734865,8.693413,-4.594373,3.146729,-4.509540,-9.916633,4.957814,8.797442,2.184772,-7.503167,-6.968127,7.891682,-8.407823,5.882969,3.029078,-6.106747,6.528100,1.298398,-5.853837,4.604946,-1.517142,-2.097525,8.559641,-5.439684,9.979561,-1.723517,-3.869302,4.019030,-2.607205,6.722716,0.946735,-8.639958,4.632740,-9.953814,7.619472,5.905380,1.128767,7.853489,9.076691,-3.294275,-0.015357,-1.921550,-2.280569,7.830829,4.440379,-7.737294,-2.538654,5.753390,-1.398256,-5.661612,0.193333,-6.752001,4.282210,-7.385861,6.608717,0.289619,1.087646,3.445646,4.118299,-6.494398,7.285395,1.897540,-2.042043,2.902118,-7.221282,-0.753060,7.829813,9.131743,-8.286925,-5.607092,-2.940961,5.248587,3.965580,5.669755,-3.482726,3.141769,-1.935532,4.006082,-2.285935,1.928506,-8.618867,-1.107847,-8.953920,2.043995,5.877870,6.013883,6.131677,3.566981,8.948964,-9.091717,9.035340,4.105100,-8.130151,-7.049191,9.573052,-9.531921,2.128850,-5.957260,-5.466871,-3.535146,1.068373,8.229866,-0.720542,2.936578,8.102268,7.982203,-4.565657,-9.709871,-2.718806,5.121742,-3.974560,2.165185,-8.019963,-0.954517,7.957502,4.678580,-4.075775,-4.428135,3.635577,-8.390860,1.862670,1.521370,-5.974735,-5.961329,-7.254105,-0.682457,0.003471,-8.857429,3.355697,-9.767859,7.077363,6.002784,-5.335519,8.259502,-1.142570,-7.525042,7.025413,3.522193,3.260806,-2.424649,4.590450,0.203780,5.261342,-5.349968,-1.877862,8.038632,-9.124270,2.283732,-0.473052,8.044534,-3.431270,-7.986379,4.967984,2.827230,-2.444713,4.858503,-1.040294,-1.572543,-8.771544,7.486927,-6.019239,1.333954,6.493725,9.070988,7.103176,-7.977032,6.664537,6.990592,-5.261897,1.746116,3.422905,-6.934393,5.243700,5.564966,-6.438804,-7.947201,2.016839,7.953760,-5.276145,1.213727,6.580728,0.931314,-4.591648,-8.401583,8.510239,3.303838,-5.623268,6.029864,5.149187,2.179912,6.973428,-0.087981,7.699262,8.017671,-4.797180,4.026943,0.391179,-4.576358,-6.031480,-1.044161,7.508054,-0.255832,-7.742560,8.386926,-0.922741,6.009871,5.695741,-0.836847,1.507818,-2.009230,-8.375050,-7.914650,7.758354,-0.809844,0.651527,9.086603,-2.450751,-4.935390,1.430909,-7.351695,-7.134766,6.160583,0.202390,8.714329,-6.067115,2.828332,8.642989,-4.493843,-1.321573,-5.841823,8.549021,-9.326460,9.668265,-9.224486,3.709900,-3.405836,-9.933142,9.264121,-6.240822,7.996395,-3.273338,3.724966,-2.472358,-7.928355,-8.895793,-5.347808,5.143266,-6.206718,8.233762,3.265821,7.397239,-2.250480,-8.351733,-3.761222,-0.220164,6.297362,-7.136560,3.481421,-7.763785,5.307805,-5.679140,-7.526574,2.642336,8.102072,-4.510331,8.248048,-7.815427,3.642661,7.089233,5.313346,9.407028,-2.486296,-3.016921,-6.928768,-8.459637,8.572905,1.421329,-3.634759,-4.596484,1.914179,-2.802045,3.881176,4.834330,2.996926,-5.813288,-6.335375,5.692430,1.712572,-0.034830,-4.203622,0.115091,-9.298239,-2.293943,3.559566,-4.632496,7.146937,5.471716,8.005192,7.807229,7.224952,-9.037315,-5.450055,3.564686,3.986684,8.901069,-0.974018,7.296019,-5.340911,9.261291,0.217029,-4.362421,-7.682288,8.683862,-4.329949,5.745603,-3.445406,-4.441292,4.527298,-9.100140,7.495824,2.941142,-2.744806,-1.581869,-6.972215,2.612283,5.800441,-1.203745,2.019466,-4.172591,-4.711598,-1.738944,9.042561,1.454660,-2.787178,7.827358,-3.924515,8.630067,1.980052,2.793204,1.926537,3.426956,-7.482260,-7.482167,7.356595,-1.692250,-4.502802,-9.555459,2.769866,5.607948,4.620680,2.864135,5.555982,5.329206,0.277257,-4.893595,8.513071,9.886770,4.120935,2.536152,-9.764135,-7.116637,-3.982705,-0.697178,0.682511,6.141314,-6.925214,-2.000020,6.705735,0.451699,-2.370272,8.992629,5.078417,1.287509,6.222233,-2.049264,-8.118672,-1.868822,9.019165,-6.910759,-2.983738,-1.484737,2.851481,-2.350035,-8.888391,8.327235,9.529441,-4.899194,2.518613,4.676396,-4.495296,9.216032,4.630032,-8.109666,-2.817134,4.897790,-3.586069,-4.707579,-2.911373,2.047010,-9.569950,3.935668,6.384781,-6.004848,6.471517,5.884996,9.262874,6.067856,6.946479,-2.303408,-7.133514,-1.725273,5.464406,-1.286837,-4.821958,-0.119896,-6.411751,-4.910700,2.425489,8.269426,5.570729,-8.020959,7.668949,6.929273,5.692185,-9.204305,6.078603,9.810809,3.562131,-7.370238,0.664365,-5.153395,-6.067632,6.971697,-3.835463,-7.604526,-8.878090,-8.838966,-0.865375,-4.996182,1.102379,-9.305100,2.947418,2.242811,2.675811,-2.112313,-2.937276,1.631159,-0.400247,-0.605705,3.927622,-2.257134,-9.464451,9.509628,-8.672245,-1.607764,-8.625351,-1.752138,-9.003775,4.032040,9.494837,-5.048394,-4.946924,-9.599470,5.888741,3.524190,9.008003,-3.579509,4.986654,2.956550,8.217591,0.027870,-6.275273,5.934792,-6.277663,-0.968985,5.708806,3.572211,-7.530784,-7.018242,8.271842,-5.286243,5.291115,-2.562615,-0.031188,-9.285667,5.795500,-4.048907,2.787127,2.766940,-8.017793,9.816758,-6.961425,1.974775,-7.775468,-3.996193,-0.903270,-6.621278,6.384382,-6.081282,-1.028097,9.727174,-7.573064,2.616848,-4.316485,0.270082,0.224700,-5.729041,-7.584285,-0.991611,2.550755,-0.139691,-5.649773,0.337978,2.663479,2.239404,-3.331360,5.123966,-1.414591,-2.883257,0.202571,8.300562,-6.018905,7.070189,-5.169988,7.830509,-5.601546,9.180921,-5.045744,9.305543,-0.936529,-5.430700,3.631606,2.049991,-9.763261,-9.473677,-0.465710,-4.299315,1.482874,1.584583,-6.496853,6.482812,-6.303749,1.143116,7.787735,-6.389014,7.050061,-2.133072,-0.897150,6.202545,9.198395,3.626756,8.494455,-7.336747,1.418419,-7.053261,-8.987312,-6.832730,-3.535828,-4.481304,-9.988619,3.519671,0.147706,3.315824,-4.538891,-4.012788,-7.656156,4.822195,-5.272550,4.232885,2.177232,1.264058,5.581409,-1.616008,6.061225,-1.906480,4.202400,7.328855,7.026203,-6.567388,7.314859,-7.597928,-2.723234,-0.600156,2.969568,-2.983845,5.460666,6.778762,-8.404635,0.019682,-6.428988,5.851411,5.941892,-9.896981,0.030336,-3.931140,0.340683,5.079895,-5.952066,-4.079138,0.703717,-0.245742,-9.239402,0.575731,7.690315,-8.594409,-9.780466,0.904323,3.549782,7.182314,8.559783,5.459106,-2.889569,-1.943990,-7.724053,-1.163465,-5.066904,0.003952,-9.615024,3.051630,9.478580,0.571751,2.581988,6.189000,-4.830173,-2.297754,0.633045,2.879970,-2.861248,-6.469656,-2.012848,-9.894596,-3.473226,-7.139632,-4.808534,-7.006923,3.305813,-1.088941,4.055854,7.578340,-1.104400,7.691857,-8.579925,9.238411,-7.535169,8.899162,-0.457045,3.809256,5.976431,-6.248540,2.076615,3.811353,-6.150659,-3.227913,-6.731363,-5.004184,6.400292,-0.907011,-7.632592,-8.241464,8.714928,5.848201,9.723123,-0.609830,-5.540254,-5.773593,-9.567188,5.646224,2.376571,-3.583841,5.398630,-9.363901,-2.112247,-7.135850,-6.111955,1.651668,3.855929,-4.354669,-8.428116,3.668890,8.299543,-4.785980,-5.658693,-6.447354,0.892650,4.379199,8.107732,2.139826,-4.463012,-2.400358,-8.138814,-0.464490,9.508350,-8.518000,-9.899304,-3.675954,-6.724891,7.081715,-9.725917,-1.456121,-4.666648,1.281598,-6.337693,8.555235,-3.848218,1.896446,3.883249,-3.539684,-3.182757,-7.338460,2.964999,-5.041935,-3.828413,-0.741995,-2.772502,-6.181211,-0.206463,-6.911293,2.147204,6.146390,-4.251243,-6.849342,-5.446281,-1.310975,-5.334558,0.218250,4.303851,1.593876,1.735670,2.169891,-5.506581,-0.948939,2.363583,4.071883,-4.481090,-3.208998,-9.774782,5.557849,-0.696436,2.319572,-8.710027,-6.584248,9.843491,6.724030,5.860292,-1.015209,0.123938,-1.599442,6.567251,6.680944,-5.806842,-4.921828,-8.964404,4.592150,0.921321,4.462638,-8.459895,-9.001014,4.367996,-1.726061,-7.071236,3.235694,-7.290320,-3.402029,8.520328,9.097915,5.794674,-6.474528,1.737728,-6.084392,8.757472,8.314568,9.069385,8.065493,6.678143,3.805506,-0.266591,0.273562,-9.602422,-2.582670,5.662796,9.171638,-6.433214,0.101443,-8.478136,-2.943410,0.071494,7.553468,3.193624,-4.521501,-9.695089,-6.688482,-9.697920,8.608737,4.123839,-0.392166,-4.500025,-1.430629,-9.843431,-3.479431,3.648432]], dtype = "float32")#candidate|5142|(2, 1320)|const|float32
call_5141 = relay.TupleGetItem(func_663_call(relay.reshape(const_5142.astype('float32'), [15, 11, 16])), 0)
call_5143 = relay.TupleGetItem(func_666_call(relay.reshape(const_5142.astype('float32'), [15, 11, 16])), 0)
func_3884_call = mod.get_global_var('func_3884')
func_3886_call = mutated_mod.get_global_var('func_3886')
const_5150 = relay.const([-7.519271,-2.095226,4.703076,-8.481744,2.699527,-4.135256,9.949259,-5.669999,9.177863,7.527885,4.654095,9.658643,-8.571820,-6.278110,-6.241881,1.775133,-6.005436,7.452725,-0.878435,-4.190310,6.187566,0.591625,3.886056,4.132050,-4.638932,8.193322,0.134704,3.140850,9.615689,-8.689701,-4.183164,2.898881,5.740588,-5.328155,-2.522587,5.750800,2.631256,-8.980764,-2.180708,4.620328,2.103439,0.238311,5.270284,-8.633919,-6.653336,4.111951,-9.966439,3.077434,6.599310,4.498212,4.557669,2.775439,2.489253,1.535552,6.234697,-3.082031,9.386786,-7.102397,6.759704,1.590456,1.716837,-3.319046,8.157966,0.297702,-9.527099,-2.715935,-9.901039,-2.059914,-5.880553,7.008589,8.369391,-7.455732], dtype = "float64")#candidate|5150|(72,)|const|float64
call_5149 = relay.TupleGetItem(func_3884_call(relay.reshape(const_5150.astype('float64'), [72,])), 0)
call_5151 = relay.TupleGetItem(func_3886_call(relay.reshape(const_5150.astype('float64'), [72,])), 0)
uop_5165 = relay.log10(call_5149.astype('float64')) # shape=(12, 14, 13)
uop_5167 = relay.log10(call_5151.astype('float64')) # shape=(12, 14, 13)
bop_5174 = relay.less_equal(uop_5165.astype('bool'), relay.reshape(call_5149.astype('bool'), relay.shape_of(uop_5165))) # shape=(12, 14, 13)
bop_5177 = relay.less_equal(uop_5167.astype('bool'), relay.reshape(call_5151.astype('bool'), relay.shape_of(uop_5167))) # shape=(12, 14, 13)
output = relay.Tuple([call_5139,call_5141,const_5142,const_5150,bop_5174,])
output2 = relay.Tuple([call_5140,call_5143,const_5142,const_5150,bop_5177,])
func_5180 = relay.Function([], output)
mod['func_5180'] = func_5180
mod = relay.transform.InferType()(mod)
mutated_mod['func_5180'] = func_5180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5180_call = mutated_mod.get_global_var('func_5180')
call_5181 = func_5180_call()
output = call_5181
func_5182 = relay.Function([], output)
mutated_mod['func_5182'] = func_5182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5180_call = mod.get_global_var('func_5180')
func_5182_call = mutated_mod.get_global_var('func_5182')
call_5186 = relay.TupleGetItem(func_5180_call(), 4)
call_5187 = relay.TupleGetItem(func_5182_call(), 4)
output = relay.Tuple([call_5186,])
output2 = relay.Tuple([call_5187,])
func_5191 = relay.Function([], output)
mod['func_5191'] = func_5191
mod = relay.transform.InferType()(mod)
output = func_5191()
func_5192 = relay.Function([], output)
mutated_mod['func_5192'] = func_5192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4672_call = mod.get_global_var('func_4672')
func_4673_call = mutated_mod.get_global_var('func_4673')
call_5209 = func_4672_call()
call_5210 = func_4672_call()
output = relay.Tuple([call_5209,])
output2 = relay.Tuple([call_5210,])
func_5211 = relay.Function([], output)
mod['func_5211'] = func_5211
mod = relay.transform.InferType()(mod)
mutated_mod['func_5211'] = func_5211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5211_call = mutated_mod.get_global_var('func_5211')
call_5212 = func_5211_call()
output = call_5212
func_5213 = relay.Function([], output)
mutated_mod['func_5213'] = func_5213
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5137_call = mod.get_global_var('func_5137')
func_5138_call = mutated_mod.get_global_var('func_5138')
call_5219 = relay.TupleGetItem(func_5137_call(), 0)
call_5220 = relay.TupleGetItem(func_5138_call(), 0)
output = relay.Tuple([call_5219,])
output2 = relay.Tuple([call_5220,])
func_5223 = relay.Function([], output)
mod['func_5223'] = func_5223
mod = relay.transform.InferType()(mod)
mutated_mod['func_5223'] = func_5223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5223_call = mutated_mod.get_global_var('func_5223')
call_5224 = func_5223_call()
output = call_5224
func_5225 = relay.Function([], output)
mutated_mod['func_5225'] = func_5225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5223_call = mod.get_global_var('func_5223')
func_5225_call = mutated_mod.get_global_var('func_5225')
call_5232 = relay.TupleGetItem(func_5223_call(), 0)
call_5233 = relay.TupleGetItem(func_5225_call(), 0)
output = relay.Tuple([call_5232,])
output2 = relay.Tuple([call_5233,])
func_5234 = relay.Function([], output)
mod['func_5234'] = func_5234
mod = relay.transform.InferType()(mod)
output = func_5234()
func_5235 = relay.Function([], output)
mutated_mod['func_5235'] = func_5235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5211_call = mod.get_global_var('func_5211')
func_5213_call = mutated_mod.get_global_var('func_5213')
call_5262 = relay.TupleGetItem(func_5211_call(), 0)
call_5263 = relay.TupleGetItem(func_5213_call(), 0)
output = relay.Tuple([call_5262,])
output2 = relay.Tuple([call_5263,])
func_5272 = relay.Function([], output)
mod['func_5272'] = func_5272
mod = relay.transform.InferType()(mod)
output = func_5272()
func_5273 = relay.Function([], output)
mutated_mod['func_5273'] = func_5273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5234_call = mod.get_global_var('func_5234')
func_5235_call = mutated_mod.get_global_var('func_5235')
call_5337 = relay.TupleGetItem(func_5234_call(), 0)
call_5338 = relay.TupleGetItem(func_5235_call(), 0)
output = relay.Tuple([call_5337,])
output2 = relay.Tuple([call_5338,])
func_5345 = relay.Function([], output)
mod['func_5345'] = func_5345
mod = relay.transform.InferType()(mod)
output = func_5345()
func_5346 = relay.Function([], output)
mutated_mod['func_5346'] = func_5346
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5113_call = mod.get_global_var('func_5113')
func_5114_call = mutated_mod.get_global_var('func_5114')
call_5368 = func_5113_call()
call_5369 = func_5113_call()
output = call_5368
output2 = call_5369
func_5372 = relay.Function([], output)
mod['func_5372'] = func_5372
mod = relay.transform.InferType()(mod)
mutated_mod['func_5372'] = func_5372
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5372_call = mutated_mod.get_global_var('func_5372')
call_5373 = func_5372_call()
output = call_5373
func_5374 = relay.Function([], output)
mutated_mod['func_5374'] = func_5374
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5113_call = mod.get_global_var('func_5113')
func_5114_call = mutated_mod.get_global_var('func_5114')
call_5421 = func_5113_call()
call_5422 = func_5113_call()
func_5345_call = mod.get_global_var('func_5345')
func_5346_call = mutated_mod.get_global_var('func_5346')
call_5425 = relay.TupleGetItem(func_5345_call(), 0)
call_5426 = relay.TupleGetItem(func_5346_call(), 0)
output = relay.Tuple([call_5421,call_5425,])
output2 = relay.Tuple([call_5422,call_5426,])
func_5427 = relay.Function([], output)
mod['func_5427'] = func_5427
mod = relay.transform.InferType()(mod)
output = func_5427()
func_5428 = relay.Function([], output)
mutated_mod['func_5428'] = func_5428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4386_call = mod.get_global_var('func_4386')
func_4388_call = mutated_mod.get_global_var('func_4388')
call_5453 = relay.TupleGetItem(func_4386_call(), 2)
call_5454 = relay.TupleGetItem(func_4388_call(), 2)
func_4638_call = mod.get_global_var('func_4638')
func_4643_call = mutated_mod.get_global_var('func_4643')
var_5456 = relay.var("var_5456", dtype = "int16", shape = (224,))#candidate|5456|(224,)|var|int16
const_5457 = relay.const([10,6,-7,-9,2,-2,10,-1,-7,7,-8,-5,7,-4,1,-10,-5,2,9,-2,1,-1,-9,5,-5,4,-5,4,-8,-2,-10,-2,1,6,5,2,1,8,8,-10,6,-4,-4,10,7,-2,8,-3,-6,-8,-8,-7,-4,10,8,2,-3,-2,7,10,-6,2,-4,3,-3,-3,3,-7,-6,-8,-9,10,-9,9,-6,1,-1,8,-5,7,3,-6,-1,3,1,4,4,-2,-6,-8,-1,-8,1,10,-8,3,-9,10,-3,7,-4,6,3,-10,10,-5,6,-5,-1,2,-4,-3,-5,10,5,2,6,-5,5,-2,-3,7,-2,8,-7,-5,7,-3,10,-10,1,-2,7,10,5,8,10,-9,8,-10,-10,-8,-10,1,4,-4,-3,-4,4,-4,-5,-8,6,1,-7,-10,3,-5,-7,-4,-8,-6,5,-1,3,9,-8,4,4,-9,-4,7,-5,2,-1,-4,5,1,-9,8,-10,9,3,5,9,-6,10,-2,-8,-8,-3,1,4,7,-6,5,-3,7,10,-1,3,3,3,-2,-10,-1,5,-2,-3,2,7,7,-4,5,-4,2,-6,-5,-10,9,9,6,1,3,-8,-5,-4,4,7,-1,-6,2,-2,8,-4,-4,8,-7,8,2,4,-1,-10,-8,4,7,4,1,-6,8,7,-3,1,-3,1,-5,5,-5,8,-3,3,-2,9,5,-2,7,6,-6,3,6,-7,1,6,8,-1,8,-10,5,6,9,4,7,8,-8,3,5,6,5,-3,-8,3,-8,-8,6,-2,2,-1,-7,4,-7,1,10,-7,-1,-7,5,-7,-5,-6,9,-6,-4,-1,7,6,4,-8,-5,9,-5,5,6,-3,-8,-4,6,7,-8,-1,-8,8,6,-8,1,9,2,8,-7,-1,-9,-2,-4,7,1,-8,6,-1,-2,-3,6,2,7,8,-10,-7,-3,-6,-9,-10,10,7,3,-6,9,-1,3,-3,-3,2,-1,4,1,-8,4,9,5,10,6,-3,7,-9,7,-1,-6,-4,6,-8,2,5,5,10,4,8,-7,-6,-6,9,1,-4,4,2,9,-7,8,-7,-8,3,-10,-3,-3,-3,5,4,1,1,-7,-5,4,7,4,5,2,5,2,-9,6,-5,6,-5,7,-2,8,9,7,-4,-2,2,-10,6,-4,8,-10,1,2,5,-1,-4,-4,2,10,4,-8,6,5,9,-10,9,10,8,-7,1,-9,8,-7,7,-10,-9,-9,-6,10,4,-4,10,5,8,-10,-10,6,-2,-10,-2,10,-9,-8,-3,-4,-8,10,-4,7,-4,1,-6,4,9,7,-4,-5,-5,-2,3,3,-4,-1,-7,8,-7,-9,-7,-9,5,-8,-10,-6,7,-3,-1,2,-1,-4,3,-4,-3,1,4,-6,5,-1,-10,2,-2,6,3,-1,-10,5,-6,-6,-9,-9,-9,3,-3,-1,-9,8,9,-7,1,7,2,9,-10,-7,1,2,-4,-4,-7,-2,7,10,-6,-10,-6,2,-8,5,5,-9,-1,8,5,-6,6,-3,-10,1,-1,-6,-8,4,-1,-6,-5,5,-5,5,5,-6,-9,-4,-1,8,-3,-8,3,9,-5,2,-9,7,-10,-7,4,-5,-2,4,3,-5,6,-9,7,5,-2,-1,-6,6,1,-2,-7,-7,-4,-2,5,-5,-1,4,-10,-10,-7,-3,7,10,5,2,7,-2,-2,-9,-4,-2,7,-4,6,-9,-3,6,4,-10,8,-2,1,7,10,2,10,-8,-7,-4,-6,-6,7,-1,-9,-3,-2,3,9,-7,-6,5,-1,3,-7,3,-1,-4,-2,-3,-7,2,-1,3,5,-1,8,-6,-8,9,7,-9,-2,1,10,-8,10,6,-3,3,8,-8,1,7,5,7,9,-2,-8,8,-9,-5,-4,-2,10,6,3,-6,8,-6,-3,-4,-8,5,3,4,-10,3,-9,-5,-4,7,-5,-2,10,5,-8,6,-9,-1,-6,4,-3,-2,-4,1,7,5,-5,-4,-4,8,10,-9,-9,-1,5,-3,-4,1,3,6,-10,-2,10,9,5,-8,-1,5,-7,-5,4,1,4,-6,5,-6,4,9,-6,-10,8,-9,2,1,10,2,-5,-2,6,-5,-1,-8,-3,-3,-7,-1,8,4,-3,1,-10,-9,-5,-5,10,-4,4,-10,-8,5,3,-10,5,-4,10,2,-8,6,-2,6,10,-3,-3,1,-5,7,-2,2,3,-4,9,5,-4,3,-10,8,-3,6,3,5,4,7,-1,1,-4,6,-10,-3,2,10,6,-3,8,-3,7,-10,-2,-6,7,6,2,-5,5,-7,-5,-8,-5,-10,-2,-6,2,1,5,6,3,-5,6,-7,9,7,-3,5,-9,10,7,-2,4,-3,-1,2,3,-10,7,-1,3,8,-4,-3,7,4,-1,-3,10,-3,4,-4,3,5,1,-6,-3,-2,9,-8,1,10,-8,5,8,-8,3,7,-6,-6,8,5,8,6,3,4,8,5,9,-6,8,-9,-8,9,-1,-2,8,-8,-3,4,2,1,3,8,6,9,1,-8,-6,-10,-1,6,10,-4,10,-10,-7,4,6,4,-9,-9,2,-7,2,5,-2,3,-5,-4,6,-9,6,4,5,-6,-10,-5,2,-1,9,-10,-7,2,9,-8,3,-9,-1,1,-1,-2,-3,5,9,10,2,-1,-10,-2,1,7,7,3,10,-4,2,-6,-3,8,7,-7,5,-9,-3,7,10,9,1,5,-5,-6,5,2,5,7,8,-2,-6,-10,-3,-2,-3,2,5,9,8,-7,-9,2,-8,5,-5,-9,-7,9,-9,5,-3,8,-6,-8,-4,9,5,-7,-10,-9,7,-7,8,-6,-6,9,-10,7,-7,10,1,5,9,-7,4,6,-3,-8,7,-7,5,-4,6,8,-6,5,10,-1,3,9,-5,9,-6,-8,10,-7,1,7,3,-3,6,8,9,4,-9,-9,8,2,-4,-6,-4,-9,-4,-4,-2,8,4,-5,-7,-7,3,-1,-4,4,1,-4,5,-2,10,8,5,-1,3,-4,-6,-9,6,10,2,2,8,-10,9,-3,-2,-2,-10,7,-10,6,-1,7,-4,7,-2,9,5,2,3,-5,-6,-1,-4,2,9,-2,-2,8,-7,-1,-4,-9,-2,-4,-4,-10,-10,9,-9,-9,-8,9,-1,5,1,-7,6,5,6,-3,-10,3,5,-5,-4,1,7,-1,6,-6,-1,2,-8,-5,6,-5,2,8,1,-10,-8,-8,-2,3,6,-4,2,-4,1,-5,7,5,7,7,-7,-6,1,-9,-4,10,2,6,-10,-4,-8,-7,-8,-6,-6,-6,1,9,5,-4,2,10,-8,8,7,-8,-3,-1,7,-10,10,5,8,-3,4,6,1,-10,2,-6,1,3,-9,9,-2,9,4,3,-10,7,-4,-9,-8,-4,6,9,-6,-3,7,-10,-2,-2,7,-8,-2,10,-9,2,6,8,-8,9,-9,8,8,-6,-9,5,-4,2,10,-3,-10,6,3,-8,-1,2,3,8,7,10,-2,1,-1,-3,4,-2,3,10,2,-4,9,2,7,3,-6,10,-1,-6,-4,5,-7,2,-3,-5,-4,-7,-6,-5,1,-8,5,4,1,-10,1,4,-10,-7,1,-9,10,8,-5,10,4,-4,6,-5,-10,-1,-10,-8,-1,3,-4,9,-8,-3,-9,-2,10,2,-4,2,-3,4,10,-4,-6,5,9,5,10,-4,-10,3,-2,8,3,-1,-5,-10,6,7,10,3,5,-1,-7,-5,-1,9,-3,-9,-4,-5,-5,3,-8,5,-2,9,6,4,5,2,-8,-9,-5,9,7,10,8,5,-6,6,-9,-7,7,10,-1,-9,-3,-1,-7,10,4,-5,-7,-10,1,1,3,4,-9,3,7,10,2,-8,6,10,2,-4,-8,-10,-2,-6,8,6,-6,-7,3,-3,-3,-4,1,-8,-1,-1,-7,-5,-3,4,3,-9,1,2,-3,10,5,4,-8,-10,3,8,-6,10,6,-1,4,-7,-3,-10,1,-6,-4,4,-1,10,10,7,-1,-5,9,-3,5,-1,-7,7,-10,6,-3,5,9,-9,1,4,1,8,-5,-6,-1,9,5,-7,10,9,6,-7,-9,-3,-10,-2,-6,4,1,4,-4,-1,-10,8,-2,1,-10,4,-5,-10,3,10,4,5,-2,7,-1,-9,-7,-10,3,-8,10,-4,8,-1,-8,4,-5,-7,-5,4,-1,6,-9,6,8,9,-7,-4,-9,-7,8,-10,8,1,-10,-1,10,-10,6,3,1,3,-4,-2,-3,-9,10,-5,7,-6,-1,-1,-6,9,6,-5,5,4,4,2,6,-10,3,5,-1,8,-9,4,9,-7,-7,-3,-8,-2,4,10,5,6,-5,-9,-3,-2,-7,8,-2,-2,-5,3,-5,-6,9,9,-5,-4,-8,-1,-2,-3,-9,-5,-4,-2,-4,-4,10,-10,-5,-4,5,-5,3,-4,-10,3,8,2,7,-4,-9,-1,-8,9,-9,-8,-3,7,-10,10,-8,9,1,1,-5,8,-3,4,-10,-5,-6,-3,-5,-4,1,-4,4,-6,-5,2,2,-4,9,-6,-9,-9,-5,5,-3,6,-10,3,-4,-1,-8,8,3,6,-10,-2,-5,-5,3,2,-6,10,-9,-1,3,-3,-5,4,-5,-9,-5,3,1,-2,-7,-8,1,2,-2,2,-5,8,-7,7,3,6,-8,-9,10,-1,4,-3,-7,4,8,-5,-4,-4,-5,5,-8,7,-4,4,10,3,5,8,9,-3,1,-1,-3,7,5,-8,-5,-10,3,-2,-9,6,9,8,-9,6,-1,4,9,1,-3,10,4,-6,-3,-10,3,6,2,-1,-5,1,-3,7,8,9,-7,-1,8,7,-6,-6,5,-3,6,-7,3,6,-5,-2,-2,-6,2,9,-5,-1,-7,1,9,-8,10,-7,-5,2,7,-1,-5,-10,-4,-6,9,-1,-6,-8,-6,1,4,-10,-10,-9,6,-8,8,-9,8,1,-5,-6,5,-8,-2,9,-5,-7,3,4,5,-2,9,-3,-9,8,9,8,8,6,-5,6,-8,-6,8,-10,-1,3,-6,-1,-5,2,3,-5,-6,-10,8,2,10,6,-8,-10,1,-1,2,-5,-10,-10,-4,3,7,-10,1,10,-10,9,3,8,-3,-4,-2,-3,-3,-7,-7,9,-6,-9,-3,-8,5,2,9,5,-9,-8,-7,5,-3,9,3,-3,10,-7,3,5,-5,10,-7,7,-4,-8,5,1,6,-9,1,-9,4,-2,-3,6,4,-3,1,-8,4,-5,9,-6,-9,3,7,-9,-10,-9,-9,-3,1,5,-6,8,-7,9,-1,1,10,-10,-8,9,1,10,-4,-5,1,-8,3,4,-1,7,8,1,-2,6,-9,7,-4,2,-2,-5,-8,-9,-9,2,8,1,5,-7,-1,8,-9,-10,4,2,-10,10,-10,-9,-3,-10,-10,8,-2,-4,-7,3,-9,-10,-6,10,9,-3,2,7,-5,-8,-7,10,-3,-2,-7,8,-9,-9,-3,10,1,-1,5,10,-5,3,-7,1,7,2,-10,2,-3,4,-9,7,6,-5,-6,-1,5,4,8,2,1,-3,-8,-10,-5,-6,7,-6,-1,-5,8,-7,3,5,-7,1,4,-8,-7,3,5,6,-5,6,-5,-1,1,10,-7,7,3,-3,10,-1,-2,-10,-6,-10,1,4,-8,-3,-3,5,7,6,-8,8,2,6,8,10,2,-4,5,1,7,4,-4,-1,-1,-2,8,8,1,-2,1,2,4,-8,-8,-4,-2,4,-9,6,4,8,8,-9,-1,-8,5,-8,10,7,7,-2,2,-5,-2,9,-1,-5,-5,9,-7,10,1,-10,6,-8,3,-1,7,-3,9,3,1,10,-4,3,8,-3,3,-9,-5,3,-6,-10,-10,-1,7,8,6,5,7,-1,-5,-5,10,-9,-2,2,7,-2,-6,-6,9,-2,-2,-4,9,7,2,4,7,-8,8,-10,3,-3,-4,-2,3,-7,5,5,7,-9,5,10,9,-2,7,3,3,-8,3,2,-8,-2,-2,-6,-10,-9,-10,-6,8,-5,9,4,-2,-8,6,2,1,-6,4,2,-9,-8,10,8,-5,3,-1,-5,-3,9], dtype = "uint64")#candidate|5457|(2288,)|const|uint64
const_5458 = relay.const([0.799640,5.978945,-2.217057,8.172042,-0.812995,5.773066,1.586723,8.557817,5.780501,9.953040,3.374243,-9.594203,8.980612,-5.052488,-9.282867,-5.057098,-6.176083,-7.403376,9.887639,-2.543294,-6.117883,1.740484,-8.442169,-9.003077,-2.197449,-2.503877,7.744863,-4.947850,-7.728149,7.193044,6.312278,1.786350,6.677645,-7.464206,4.630783,7.270743,-8.988905,0.438456,1.854541,-8.245347,-0.125181,0.207062,1.489930,-9.183887,-4.724639,-7.368388,9.883232,-6.820901,0.188279,4.184199,2.840270,-4.048873,-4.740894,-1.458266,2.168431,7.869894,-9.196283,-5.690084,7.201318,9.048781], dtype = "float64")#candidate|5458|(60,)|const|float64
call_5455 = relay.TupleGetItem(func_4638_call(relay.reshape(var_5456.astype('int16'), [16, 14]), relay.reshape(const_5457.astype('uint64'), [2288,]), relay.reshape(const_5458.astype('float64'), [60,]), ), 0)
call_5459 = relay.TupleGetItem(func_4643_call(relay.reshape(var_5456.astype('int16'), [16, 14]), relay.reshape(const_5457.astype('uint64'), [2288,]), relay.reshape(const_5458.astype('float64'), [60,]), ), 0)
output = relay.Tuple([call_5453,call_5455,var_5456,const_5457,const_5458,])
output2 = relay.Tuple([call_5454,call_5459,var_5456,const_5457,const_5458,])
func_5465 = relay.Function([var_5456,], output)
mod['func_5465'] = func_5465
mod = relay.transform.InferType()(mod)
mutated_mod['func_5465'] = func_5465
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5466 = relay.var("var_5466", dtype = "int16", shape = (224,))#candidate|5466|(224,)|var|int16
func_5465_call = mutated_mod.get_global_var('func_5465')
call_5467 = func_5465_call(var_5466)
output = call_5467
func_5468 = relay.Function([var_5466], output)
mutated_mod['func_5468'] = func_5468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5211_call = mod.get_global_var('func_5211')
func_5213_call = mutated_mod.get_global_var('func_5213')
call_5596 = relay.TupleGetItem(func_5211_call(), 0)
call_5597 = relay.TupleGetItem(func_5213_call(), 0)
func_4886_call = mod.get_global_var('func_4886')
func_4888_call = mutated_mod.get_global_var('func_4888')
call_5633 = func_4886_call()
call_5634 = func_4886_call()
output = relay.Tuple([call_5596,call_5633,])
output2 = relay.Tuple([call_5597,call_5634,])
func_5664 = relay.Function([], output)
mod['func_5664'] = func_5664
mod = relay.transform.InferType()(mod)
output = func_5664()
func_5665 = relay.Function([], output)
mutated_mod['func_5665'] = func_5665
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5180_call = mod.get_global_var('func_5180')
func_5182_call = mutated_mod.get_global_var('func_5182')
call_5666 = relay.TupleGetItem(func_5180_call(), 3)
call_5667 = relay.TupleGetItem(func_5182_call(), 3)
output = call_5666
output2 = call_5667
func_5695 = relay.Function([], output)
mod['func_5695'] = func_5695
mod = relay.transform.InferType()(mod)
mutated_mod['func_5695'] = func_5695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5695_call = mutated_mod.get_global_var('func_5695')
call_5696 = func_5695_call()
output = call_5696
func_5697 = relay.Function([], output)
mutated_mod['func_5697'] = func_5697
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5708 = relay.var("var_5708", dtype = "float64", shape = (3, 12, 14))#candidate|5708|(3, 12, 14)|var|float64
uop_5709 = relay.log(var_5708.astype('float64')) # shape=(3, 12, 14)
bop_5714 = relay.logical_and(var_5708.astype('bool'), relay.reshape(uop_5709.astype('bool'), relay.shape_of(var_5708))) # shape=(3, 12, 14)
output = relay.Tuple([bop_5714,])
output2 = relay.Tuple([bop_5714,])
func_5727 = relay.Function([var_5708,], output)
mod['func_5727'] = func_5727
mod = relay.transform.InferType()(mod)
var_5728 = relay.var("var_5728", dtype = "float64", shape = (3, 12, 14))#candidate|5728|(3, 12, 14)|var|float64
output = func_5727(var_5728)
func_5729 = relay.Function([var_5728], output)
mutated_mod['func_5729'] = func_5729
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4886_call = mod.get_global_var('func_4886')
func_4888_call = mutated_mod.get_global_var('func_4888')
call_5802 = func_4886_call()
call_5803 = func_4886_call()
output = call_5802
output2 = call_5803
func_5807 = relay.Function([], output)
mod['func_5807'] = func_5807
mod = relay.transform.InferType()(mod)
mutated_mod['func_5807'] = func_5807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5807_call = mutated_mod.get_global_var('func_5807')
call_5808 = func_5807_call()
output = call_5808
func_5809 = relay.Function([], output)
mutated_mod['func_5809'] = func_5809
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5191_call = mod.get_global_var('func_5191')
func_5192_call = mutated_mod.get_global_var('func_5192')
call_5819 = relay.TupleGetItem(func_5191_call(), 0)
call_5820 = relay.TupleGetItem(func_5192_call(), 0)
output = relay.Tuple([call_5819,])
output2 = relay.Tuple([call_5820,])
func_5829 = relay.Function([], output)
mod['func_5829'] = func_5829
mod = relay.transform.InferType()(mod)
output = func_5829()
func_5830 = relay.Function([], output)
mutated_mod['func_5830'] = func_5830
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5829_call = mod.get_global_var('func_5829')
func_5830_call = mutated_mod.get_global_var('func_5830')
call_5855 = relay.TupleGetItem(func_5829_call(), 0)
call_5856 = relay.TupleGetItem(func_5830_call(), 0)
output = call_5855
output2 = call_5856
func_5865 = relay.Function([], output)
mod['func_5865'] = func_5865
mod = relay.transform.InferType()(mod)
mutated_mod['func_5865'] = func_5865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5865_call = mutated_mod.get_global_var('func_5865')
call_5866 = func_5865_call()
output = call_5866
func_5867 = relay.Function([], output)
mutated_mod['func_5867'] = func_5867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4758_call = mod.get_global_var('func_4758')
func_4759_call = mutated_mod.get_global_var('func_4759')
call_5904 = func_4758_call()
call_5905 = func_4758_call()
output = relay.Tuple([call_5904,])
output2 = relay.Tuple([call_5905,])
func_5906 = relay.Function([], output)
mod['func_5906'] = func_5906
mod = relay.transform.InferType()(mod)
mutated_mod['func_5906'] = func_5906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5906_call = mutated_mod.get_global_var('func_5906')
call_5907 = func_5906_call()
output = call_5907
func_5908 = relay.Function([], output)
mutated_mod['func_5908'] = func_5908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4963_call = mod.get_global_var('func_4963')
func_4965_call = mutated_mod.get_global_var('func_4965')
call_5928 = relay.TupleGetItem(func_4963_call(), 7)
call_5929 = relay.TupleGetItem(func_4965_call(), 7)
uop_5931 = relay.asin(call_5928.astype('float32')) # shape=(588, 126)
uop_5933 = relay.asin(call_5929.astype('float32')) # shape=(588, 126)
output = uop_5931
output2 = uop_5933
func_5939 = relay.Function([], output)
mod['func_5939'] = func_5939
mod = relay.transform.InferType()(mod)
mutated_mod['func_5939'] = func_5939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5939_call = mutated_mod.get_global_var('func_5939')
call_5940 = func_5939_call()
output = call_5940
func_5941 = relay.Function([], output)
mutated_mod['func_5941'] = func_5941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5180_call = mod.get_global_var('func_5180')
func_5182_call = mutated_mod.get_global_var('func_5182')
call_5983 = relay.TupleGetItem(func_5180_call(), 3)
call_5984 = relay.TupleGetItem(func_5182_call(), 3)
func_1796_call = mod.get_global_var('func_1796')
func_1799_call = mutated_mod.get_global_var('func_1799')
var_5987 = relay.var("var_5987", dtype = "uint64", shape = (2288,))#candidate|5987|(2288,)|var|uint64
call_5986 = relay.TupleGetItem(func_1796_call(relay.reshape(var_5987.astype('uint64'), [2288,])), 2)
call_5988 = relay.TupleGetItem(func_1799_call(relay.reshape(var_5987.astype('uint64'), [2288,])), 2)
output = relay.Tuple([call_5983,call_5986,var_5987,])
output2 = relay.Tuple([call_5984,call_5988,var_5987,])
func_6011 = relay.Function([var_5987,], output)
mod['func_6011'] = func_6011
mod = relay.transform.InferType()(mod)
mutated_mod['func_6011'] = func_6011
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6012 = relay.var("var_6012", dtype = "uint64", shape = (2288,))#candidate|6012|(2288,)|var|uint64
func_6011_call = mutated_mod.get_global_var('func_6011')
call_6013 = func_6011_call(var_6012)
output = call_6013
func_6014 = relay.Function([var_6012], output)
mutated_mod['func_6014'] = func_6014
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6025 = relay.const([[[-8.726495,5.327894,3.068466,1.460111,-0.120218,-4.234077],[-8.772196,4.940991,3.487339,-9.149591,1.014037,-8.932771],[-3.475546,-4.615630,-3.315148,1.569007,-6.892632,-9.036336],[9.789132,-8.815447,6.195142,4.260065,5.678187,-5.678902],[-8.311324,6.908951,0.142256,3.261409,5.955624,-4.550029]],[[3.923206,-3.820654,-9.488104,4.970104,-9.667290,4.057833],[-7.350694,-6.938413,5.942483,-9.854432,6.310801,-7.256385],[-9.173619,-3.920605,9.533529,1.016996,-4.743352,-7.699624],[-2.005728,-9.865778,-0.192266,7.955478,8.600353,-5.159816],[-2.280707,-1.568017,-3.579050,-4.683661,-9.952425,9.231720]],[[9.397137,-2.197913,-6.261882,-4.035033,6.714699,-7.736177],[-8.860366,-4.294628,9.099176,1.526307,-8.347736,3.445458],[-4.332317,5.826779,-1.917263,-3.805131,4.015343,4.467462],[1.220835,-0.785528,7.117620,-8.084065,-4.772525,3.993203],[-9.104371,3.250240,-9.085566,9.359819,-6.076057,-5.773418]],[[3.574987,-0.535940,4.600341,7.429099,1.734906,5.213091],[-4.074074,4.506552,5.099013,-3.968132,7.616757,-0.532831],[-5.973579,-8.659839,-5.117717,9.727911,0.806873,-8.453292],[6.317188,5.283210,9.134657,8.089677,6.369844,3.287107],[4.799333,-5.919907,6.292849,3.665260,-2.861247,9.910169]],[[-3.369746,7.822067,-2.568356,-1.877057,2.006272,3.039849],[7.209992,-6.038069,8.355844,7.685696,9.572448,1.904069],[-0.617753,-5.426456,-5.636427,8.121270,-8.797775,-8.914080],[-0.119834,-1.675816,-9.397823,-9.608787,5.506942,-8.168302],[-7.090208,7.909296,6.696714,4.135740,6.272829,5.967149]],[[6.101911,-2.653523,3.878830,-5.276126,-0.157300,1.065056],[-9.312369,-2.460432,-3.078399,-5.640968,-1.512892,-1.217469],[-4.334983,6.348457,9.583585,3.839933,9.470151,-9.814169],[-3.765513,-4.809258,5.675806,-7.343858,2.769811,2.652707],[2.403565,4.583875,-1.497954,-6.923708,0.824724,-5.756343]],[[-8.187655,5.493736,-8.178401,-6.166526,-3.207745,2.640247],[-5.364289,-3.404107,-0.217358,3.482039,7.794849,5.947775],[-1.119477,7.980223,7.263304,-4.261141,2.136395,1.189496],[1.612664,9.632657,-8.202292,0.889909,-6.008494,-4.651857],[-7.460310,-9.402972,-7.693266,2.945178,7.091455,-3.605145]],[[-4.518056,-2.082940,-2.377216,4.087281,5.362475,-6.112846],[5.403643,-7.785839,7.157605,-8.599736,-6.070984,0.124159],[-3.694231,4.786718,3.115144,-0.510357,-9.944296,-5.356890],[-0.435632,-3.003716,-1.430976,4.237393,9.748883,7.620974],[5.535857,-2.914512,-9.402536,-0.395431,-1.956116,2.752447]],[[-7.529502,7.706309,-7.500761,7.164262,-4.240601,4.205700],[-4.179239,-4.539081,-6.678505,-3.982000,-0.267639,-8.291235],[6.377493,9.079292,-4.059883,6.939587,3.472704,-8.393902],[-4.627489,-6.100258,0.771731,4.283765,2.948201,3.355254],[5.029007,9.018352,-7.227472,7.473800,-2.077022,8.488085]]], dtype = "float32")#candidate|6025|(9, 5, 6)|const|float32
var_6026 = relay.var("var_6026", dtype = "float32", shape = (9, 5, 6))#candidate|6026|(9, 5, 6)|var|float32
bop_6027 = relay.mod(const_6025.astype('float32'), relay.reshape(var_6026.astype('float32'), relay.shape_of(const_6025))) # shape=(9, 5, 6)
func_4886_call = mod.get_global_var('func_4886')
func_4888_call = mutated_mod.get_global_var('func_4888')
call_6031 = func_4886_call()
call_6032 = func_4886_call()
func_5345_call = mod.get_global_var('func_5345')
func_5346_call = mutated_mod.get_global_var('func_5346')
call_6044 = relay.TupleGetItem(func_5345_call(), 0)
call_6045 = relay.TupleGetItem(func_5346_call(), 0)
func_921_call = mod.get_global_var('func_921')
func_923_call = mutated_mod.get_global_var('func_923')
call_6048 = relay.TupleGetItem(func_921_call(relay.reshape(call_6031.astype('int16'), [])), 0)
call_6049 = relay.TupleGetItem(func_923_call(relay.reshape(call_6031.astype('int16'), [])), 0)
output = relay.Tuple([bop_6027,call_6031,call_6044,call_6048,])
output2 = relay.Tuple([bop_6027,call_6032,call_6045,call_6049,])
func_6050 = relay.Function([var_6026,], output)
mod['func_6050'] = func_6050
mod = relay.transform.InferType()(mod)
mutated_mod['func_6050'] = func_6050
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6051 = relay.var("var_6051", dtype = "float32", shape = (9, 5, 6))#candidate|6051|(9, 5, 6)|var|float32
func_6050_call = mutated_mod.get_global_var('func_6050')
call_6052 = func_6050_call(var_6051)
output = call_6052
func_6053 = relay.Function([var_6051], output)
mutated_mod['func_6053'] = func_6053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5272_call = mod.get_global_var('func_5272')
func_5273_call = mutated_mod.get_global_var('func_5273')
call_6071 = relay.TupleGetItem(func_5272_call(), 0)
call_6072 = relay.TupleGetItem(func_5273_call(), 0)
func_2517_call = mod.get_global_var('func_2517')
func_2521_call = mutated_mod.get_global_var('func_2521')
var_6083 = relay.var("var_6083", dtype = "float64", shape = (1440,))#candidate|6083|(1440,)|var|float64
const_6084 = relay.const([[4.960725],[-1.798217],[-1.026653],[-4.737626],[-0.241878],[8.008602],[-9.668976],[4.736323],[0.022187],[9.716658],[8.432118],[5.582523],[-9.486591],[6.076301],[-9.866336],[-6.592040],[1.903569],[5.129767],[3.767536],[-1.338845],[4.071498],[8.473765],[0.680642],[-1.611526],[-4.791475],[-0.244531],[1.151511],[-1.847756],[-5.978656],[4.680304],[0.291539],[-8.142799],[-3.604366],[-5.302594],[8.589304],[-9.540871],[-6.601297],[-0.511295],[-9.920797],[4.926975],[-4.392178],[6.232517],[6.858094],[1.450119],[8.912696],[-7.355164],[-1.724942],[5.640236],[-0.193223],[2.653044],[-6.633104],[-2.905685],[3.121791],[0.512091],[5.634702],[-1.326395],[-3.036421],[-0.991163],[3.240095],[0.951944],[-6.056982],[8.269918],[-3.304267],[9.208417],[2.450625],[-8.536586],[-8.443827],[-2.324148],[3.091579],[-7.876010],[-6.845700],[-6.254221],[-3.688282],[-0.512336],[5.003924],[-5.997057],[7.413344],[-7.765927],[-3.696927],[-6.019409],[-1.330085],[-6.369882],[-6.403776],[-2.163016],[-8.044944],[-7.560692],[5.766856],[6.210703],[7.835312],[4.693195],[7.309685],[-9.881804],[-4.650040],[-7.621785],[1.589219],[-9.045840],[6.932861],[-9.641103],[5.774650],[8.309211],[4.153288],[0.307430],[-0.470588],[-3.615419],[-8.138029],[-4.414251],[8.998877],[1.847586],[-1.735912],[3.477475],[-0.082400],[5.980344],[-7.980738],[5.299791],[0.466120],[8.320908],[2.972318],[1.283436],[3.627575],[4.077689],[-6.121063],[3.940579],[8.125206],[1.956545],[-3.487444],[1.927257]], dtype = "float32")#candidate|6084|(126, 1)|const|float32
call_6082 = relay.TupleGetItem(func_2517_call(relay.reshape(var_6083.astype('float64'), [12, 15, 8]), relay.reshape(const_6084.astype('float32'), [126,]), ), 0)
call_6085 = relay.TupleGetItem(func_2521_call(relay.reshape(var_6083.astype('float64'), [12, 15, 8]), relay.reshape(const_6084.astype('float32'), [126,]), ), 0)
func_618_call = mod.get_global_var('func_618')
func_622_call = mutated_mod.get_global_var('func_622')
call_6095 = relay.TupleGetItem(func_618_call(relay.reshape(call_6071.astype('float64'), [5, 3, 4]), relay.reshape(const_6084.astype('float32'), [126,]), ), 1)
call_6096 = relay.TupleGetItem(func_622_call(relay.reshape(call_6071.astype('float64'), [5, 3, 4]), relay.reshape(const_6084.astype('float32'), [126,]), ), 1)
output = relay.Tuple([call_6071,call_6082,var_6083,const_6084,call_6095,])
output2 = relay.Tuple([call_6072,call_6085,var_6083,const_6084,call_6096,])
func_6098 = relay.Function([var_6083,], output)
mod['func_6098'] = func_6098
mod = relay.transform.InferType()(mod)
var_6099 = relay.var("var_6099", dtype = "float64", shape = (1440,))#candidate|6099|(1440,)|var|float64
output = func_6098(var_6099)
func_6100 = relay.Function([var_6099], output)
mutated_mod['func_6100'] = func_6100
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5191_call = mod.get_global_var('func_5191')
func_5192_call = mutated_mod.get_global_var('func_5192')
call_6109 = relay.TupleGetItem(func_5191_call(), 0)
call_6110 = relay.TupleGetItem(func_5192_call(), 0)
func_1796_call = mod.get_global_var('func_1796')
func_1799_call = mutated_mod.get_global_var('func_1799')
const_6117 = relay.const([10,9,7,-8,1,-9,-9,10,7,4,1,1,10,-3,-1,-9,-2,-10,6,-3,4,-5,8,-4,3,10,-6,3,-9,6,5,-10,6,7,9,-10,-2,5,-8,-5,-7,-5,6,-6,-6,-6,10,7,7,7,-4,9,1,5,3,10,-7,-10,3,-9,-10,10,-4,-5,3,-6,-8,2,-9,9,-9,1,-6,-10,-8,-7,-5,-10,6,-1,-7,5,-4,-7,5,4,-8,1,-5,-2,1,1,8,6,-7,10,-4,3,3,-10,7,2,8,-7,6,5,-9,-5,10,-1,-10,2,8,-1,-5,-9,2,8,-7,-2,6,-10,6,4,-9,-2,7,-3,1,-6,-3,-1,-6,-7,-5,6,8,8,3,9,-6,1,9,8,7,6,-1,-7,7,-10,6,-4,3,-8,4,8,-2,-5,4,1,-9,3,6,-7,-7,3,-4,-8,1,-1,7,6,10,-10,-7,10,-8,6,-5,6,1,-5,-8,-9,-1,3,10,7,3,8,6,5,-1,9,3,1,-7,-6,1,6,-6,10,-10,-9,4,-2,5,6,6,5,-1,5,3,6,9,-8,3,-4,-6,-6,10,3,-5,5,-4,-3,7,4,-1,5,-2,-4,2,-8,1,-1,1,-8,10,-8,-4,-9,10,10,-6,1,10,3,-5,2,-4,-9,-4,-3,-2,1,3,6,7,-7,3,-1,5,-2,-4,6,-7,6,2,10,-2,8,2,1,2,-2,-5,-5,-6,1,-3,-1,10,4,9,-5,-4,6,-9,-5,6,5,2,-4,-10,10,1,-6,1,4,3,-8,-4,-2,3,3,7,-1,-9,9,1,3,-3,5,-8,-3,-10,-5,-7,-7,-8,-10,-10,6,-7,9,4,-9,10,10,-3,-8,-4,-5,-1,3,-5,-4,3,4,-5,-7,-4,8,10,-5,-1,-6,-5,-7,-3,8,3,-3,-4,-8,8,9,-4,10,-5,7,-8,-2,-3,-1,-1,-6,-5,-3,-4,9,8,7,-7,8,-2,9,-9,2,3,-2,-4,-1,7,-9,4,-4,10,-8,8,10,-4,-1,1,7,-9,-10,-5,-4,-4,-3,3,-3,-1,-9,-9,-1,7,6,-5,3,1,-7,-4,-9,5,7,1,10,-2,-3,9,4,5,-5,-2,-6,-2,9,5,-4,-2,-8,-2,-7,1,-7,-5,6,8,2,-10,1,1,-9,8,7,-4,-6,-7,-3,4,-9,-9,-9,-8,9,1,-1,-1,-9,4,10,-4,4,-9,10,-7,10,-3,4,-2,-1,-4,5,5,-4,-3,6,-1,9,-9,3,7,3,4,3,-2,-1,9,10,2,-4,8,-2,-4,9,7,1,-7,6,-4,9,3,2,6,9,-6,2,-5,-5,3,-2,7,-6,10,6,-1,9,3,-8,-3,-8,10,-3,2,1,3,10,9,-2,8,-10,-3,2,10,6,9,-2,-3,3,4,-5,-9,7,-10,4,9,8,-5,-1,-2,-10,-2,-9,1,10,-6,-4,-9,3,-2,-9,3,6,-10,6,-3,-5,3,9,6,9,6,8,-6,7,10,-10,3,-4,2,-5,8,-1,-3,-5,4,4,-9,7,5,-5,8,-9,-1,4,-3,-10,8,-2,-4,2,2,7,-8,9,6,8,9,-7,-2,-6,1,-8,9,-9,-6,10,7,-1,2,6,-4,-4,-6,3,-3,3,-7,4,-10,9,-6,-5,-6,5,6,6,10,3,10,-3,7,8,8,1,6,3,-1,-2,7,-5,-3,-3,10,8,-1,6,9,-1,-5,-3,4,-1,-8,-2,-4,-6,-7,-7,-4,-8,8,-3,7,1,8,-4,-4,5,-10,5,-3,9,1,-8,3,-9,1,7,8,1,6,8,10,1,2,4,-8,-7,2,-5,-3,-7,8,6,6,2,5,-1,5,7,-8,3,7,-9,5,-4,-10,-7,-7,-6,10,-4,-8,-2,-6,10,-1,4,-3,4,6,-8,-3,5,-8,4,9,-5,-2,1,5,6,4,-1,-10,5,-7,2,-10,1,-10,-7,2,9,10,-5,-3,10,-8,4,-10,-6,2,6,-7,-9,1,-7,10,6,-5,-5,-2,6,8,10,9,-4,3,4,-6,-6,-10,9,-6,2,-7,-10,3,-9,-3,8,2,-4,3,-5,-2,-5,2,4,10,9,-2,4,-2,8,-1,-9,10,10,-1,2,5,-6,3,5,6,9,-3,-7,8,-2,2,4,5,5,8,-9,-5,8,-7,-9,6,-2,3,-6,5,-9,-9,8,6,10,-9,5,-6,-1,-7,-5,-2,-4,6,-5,-9,-7,9,4,9,9,5,-3,8,-3,6,-10,4,-3,-5,3,-5,4,-8,-7,-2,-6,-10,-7,10,-3,-7,5,8,-6,-6,-9,-3,-5,3,9,-10,-4,1,1,3,-10,-9,-4,2,-2,-10,9,5,-4,8,6,6,8,-3,-9,-3,9,-3,-8,4,5,-10,9,10,8,7,-6,5,-10,-3,7,9,7,-10,9,5,-1,-10,-2,4,-10,3,-3,2,-7,4,10,-1,-5,1,6,-10,1,-7,-4,-5,1,-2,8,-8,8,10,-5,-6,1,-8,5,6,-10,1,6,-8,-5,1,-4,-8,-3,2,-9,-2,-8,-9,-8,9,10,2,7,4,2,-5,6,-1,-10,-9,-3,-9,-1,4,-5,-9,-4,-4,-3,-4,6,3,3,-3,9,3,-4,3,-3,7,1,-7,-7,9,-9,-8,2,-7,7,7,-1,-8,-3,10,-9,3,3,6,-1,1,-7,3,10,4,7,5,-2,-4,-5,10,-3,5,-5,5,7,-5,7,-4,7,6,9,-3,6,5,-2,-5,-10,-1,3,-10,-6,-5,-3,1,6,6,-1,-8,8,8,10,5,6,-6,3,-7,3,1,-10,-7,-4,-4,2,1,9,10,-5,-1,2,-7,-7,4,-8,-7,-9,-7,-7,-5,-4,1,-8,-3,7,-1,5,-3,-4,-4,10,-1,6,-2,-10,4,-5,-7,7,7,6,-2,-8,5,10,4,-1,-10,2,1,-9,6,-1,9,5,-1,-4,3,-6,3,8,-7,-2,-5,7,8,3,9,9,4,-4,6,-6,9,5,-9,7,1,10,-8,4,-2,2,-2,1,-6,1,-10,-8,10,-1,8,2,1,-5,-9,-5,-7,4,7,-7,10,-4,6,1,7,2,2,-3,8,-10,-9,9,1,9,-1,-2,6,-1,-7,-6,-4,10,-4,7,-2,-8,1,1,5,1,-6,-6,8,-3,-10,1,-9,10,-5,5,3,10,-3,7,9,-3,-10,7,6,4,1,2,8,3,-8,-1,-4,-8,-10,-6,-2,5,-7,9,-4,-9,-2,-7,2,4,-2,4,7,-4,6,7,-8,7,7,-9,3,-8,-1,-5,-6,-7,-7,-4,-3,-1,-8,-7,3,4,-2,-10,4,-9,-4,-10,-5,-9,-9,5,3,3,6,-10,5,-6,-6,3,-6,-5,-7,1,5,4,-6,8,-7,-3,-10,-2,4,2,-6,-1,7,5,2,-6,7,-1,-9,4,-9,-8,7,-3,-10,4,10,-10,-1,9,-10,-2,-6,-10,3,2,-1,10,2,9,-8,8,8,5,3,-5,-10,10,4,-3,-5,9,-7,2,-4,-1,-5,10,-9,5,8,4,8,6,-5,-9,1,-4,10,-8,-10,7,-10,-1,2,2,5,-10,2,-7,4,-7,3,-3,-9,7,10,7,3,-10,5,6,9,-4,-3,-8,-6,-2,-6,4,-6,5,5,7,-1,4,10,-5,-8,-10,10,10,10,-5,-6,2,-9,9,10,-1,-6,4,-7,-5,-7,-7,-2,3,10,-10,6,-10,10,7,7,10,5,9,4,8,-8,10,-4,2,10,10,-6,9,10,-4,7,10,10,3,-1,7,6,9,-2,-3,5,-8,-2,6,6,8,-6,5,-6,-9,-9,-8,6,6,10,-10,-3,-7,7,8,3,-7,4,2,10,9,-10,8,-6,-3,6,-5,-4,-5,-4,-6,-8,-6,5,-4,-1,-8,-4,6,3,-8,5,-9,6,9,8,6,8,-10,-10,-2,9,-2,8,-3,-1,1,4,2,7,-9,9,-1,-7,-2,7,-10,7,9,3,-8,5,-8,-3,-9,4,-5,5,-9,-9,3,-6,2,4,9,-5,10,10,9,10,4,-7,-4,5,9,4,-9,5,-4,-7,6,3,2,-8,7,-8,-10,9,9,7,7,-10,-2,10,-3,10,-8,9,-6,-10,5,-5,-5,8,10,4,5,-6,10,-4,4,6,6,-2,2,-9,-10,-1,1,-10,5,8,7,-10,9,-10,5,-5,-1,5,-10,2,1,6,-7,2,-10,3,-4,4,6,-8,-2,-3,-1,8,-5,3,8,-7,-6,6,-7,1,3,-7,-1,-9,8,-8,2,-10,10,2,-5,-2,8,-4,6,-8,-3,7,10,1,-10,6,-6,-3,-2,-2,-6,7,-2,-8,-6,-9,-3,-7,4,10,-6,10,-5,-6,-7,-3,5,-6,-10,-5,-3,7,3,-9,-1,-1,-5,9,-3,4,-7,5,-8,-9,7,5,10,-8,-8,-10,-5,-10,-3,8,-5,-7,3,4,-5,10,-7,-6,10,10,10,-1,-10,-5,9,10,-10,-6,-1,6,3,1,-2,-9,-8,10,-8,5,1,2,5,-6,10,-10,4,10,2,9,6,-6,-6,4,-9,-3,-1,10,8,-3,-8,1,10,9,-1,-6,6,-3,8,8,8,-8,8,-5,4,7,4,3,-9,4,3,-9,1,1,1,9,-3,-8,-2,7,4,7,-4,-10,5,3,5,6,5,-7,1,8,2,-4,3,-2,7,-5,-2,-4,-10,-6,10,-2,3,3,-5,7,9,4,3,8,-5,-1,-7,-5,-1,-1,5,7,-3,2,-3,5,-8,-3,5,1,4,9,6,-8,5,9,3,7,-8,5,-6,5,-9,7,2,4,-9,-9,6,-3,7,10,7,7,6,9,2,10,-4,5,-4,-4,-3,7,10,-10,-1,8,-2,5,7,-2,10,2,8,2,8,4,-10,-1,-2,-7,5,-2,2,-5,-1,-10,10,5,-9,7,-4,9,1,-2,2,5,-7,-4,-6,10,5,-10,-1,-2,-3,-8,-1,9,-8,6,-2,-7,10,10,10,5,1,2,-10,2,5,-8,-6,2,-10,4,-1,-5,-2,-7,6,-8,7,8,-4,9,-10,-10,6,2,8,9,7,-10,-6,1,-1,8,-9,-5,7,-4,1,-5,4,2,-3,1,3,-9,10,-3,-9,1,7,10,-10,-1,8,7,-3,-4,-9,6,-8,-3,5,3,8,3,-10,1,9,2,-8,-9,-9,7,2,10,-8,-10,10,10,-7,-5,-8,-8,10,4,8,-1,10,5,-9,2,9,-2,-5,-8,5,-3,2,10,9,10,-9,4,-8,9,-5,7,-3,4,-1,-4,8,7,-9,1,-3,7,1,3,-10,9,5,9,4,8,6,2,-1,5,8,-8,-7,4,6,-7,10,-10,-9,3,-2,9,-4,3,1,-3,-4,-9,6,8,9,-8,1,-1,7,-6,-4,-1,7,4,-4,5,8,8,7,7,1,-4,1,3,-9,1,5,4,5,-7,4,6,6,-7,-8,-9,-8,-9,8,1,2,-3,-1,6,4,5,-7,-2,-3,-8,-3,-9,-9,4,-2,-7,4,-1,8,2,-3,9,-10,-3,-10,-5,9,6,4,-7,4,3,5,-4,1,4,7,-2,-6,1,7,3,-1,3,-10,2,-6,1,-8,6,-4,-1,-8,7,7,2,-5,-9,-5,-10,5,-8,-8,4,-5,-3,-3,-10,-9,-6,7,10,4,-8,4,-5,-3,-7,1,7,2,-7,-6,7,-5,4,3,-6,5,-6,-4,-5,-4,-8,-6,3,6,-4,-8,-10,5,9,-7,-5,-10,9,-3,-1,-9,-4,-3,-2,8,3,-10,-10,-4,1,5,6,-8,-1,1,6,10,-4,6,2,-5,-1,-8,8,-4,-5,-6,6,6,-2,9,7,-9,-2,9,10,-9,-7,-4,10,5,-8,-6,4,2,-1,4,-2,-8,-10,10,-1,1,-7,2,-4,3,-7,-8,1,6,3,-9,-5,-9,6,-2,-8,4,1,-3,2,-9,-4,-1,-9,8], dtype = "uint64")#candidate|6117|(2288,)|const|uint64
call_6116 = relay.TupleGetItem(func_1796_call(relay.reshape(const_6117.astype('uint64'), [2288,])), 2)
call_6118 = relay.TupleGetItem(func_1799_call(relay.reshape(const_6117.astype('uint64'), [2288,])), 2)
output = relay.Tuple([call_6109,call_6116,const_6117,])
output2 = relay.Tuple([call_6110,call_6118,const_6117,])
func_6125 = relay.Function([], output)
mod['func_6125'] = func_6125
mod = relay.transform.InferType()(mod)
output = func_6125()
func_6126 = relay.Function([], output)
mutated_mod['func_6126'] = func_6126
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4724_call = mod.get_global_var('func_4724')
func_4726_call = mutated_mod.get_global_var('func_4726')
call_6177 = relay.TupleGetItem(func_4724_call(), 0)
call_6178 = relay.TupleGetItem(func_4726_call(), 0)
output = relay.Tuple([call_6177,])
output2 = relay.Tuple([call_6178,])
func_6210 = relay.Function([], output)
mod['func_6210'] = func_6210
mod = relay.transform.InferType()(mod)
mutated_mod['func_6210'] = func_6210
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6210_call = mutated_mod.get_global_var('func_6210')
call_6211 = func_6210_call()
output = call_6211
func_6212 = relay.Function([], output)
mutated_mod['func_6212'] = func_6212
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6267 = relay.var("var_6267", dtype = "float64", shape = (15, 8, 14))#candidate|6267|(15, 8, 14)|var|float64
uop_6268 = relay.exp(var_6267.astype('float64')) # shape=(15, 8, 14)
output = relay.Tuple([uop_6268,])
output2 = relay.Tuple([uop_6268,])
func_6274 = relay.Function([var_6267,], output)
mod['func_6274'] = func_6274
mod = relay.transform.InferType()(mod)
var_6275 = relay.var("var_6275", dtype = "float64", shape = (15, 8, 14))#candidate|6275|(15, 8, 14)|var|float64
output = func_6274(var_6275)
func_6276 = relay.Function([var_6275], output)
mutated_mod['func_6276'] = func_6276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5372_call = mod.get_global_var('func_5372')
func_5374_call = mutated_mod.get_global_var('func_5374')
call_6309 = func_5372_call()
call_6310 = func_5372_call()
func_4386_call = mod.get_global_var('func_4386')
func_4388_call = mutated_mod.get_global_var('func_4388')
call_6320 = relay.TupleGetItem(func_4386_call(), 0)
call_6321 = relay.TupleGetItem(func_4388_call(), 0)
func_5345_call = mod.get_global_var('func_5345')
func_5346_call = mutated_mod.get_global_var('func_5346')
call_6323 = relay.TupleGetItem(func_5345_call(), 0)
call_6324 = relay.TupleGetItem(func_5346_call(), 0)
func_1209_call = mod.get_global_var('func_1209')
func_1212_call = mutated_mod.get_global_var('func_1212')
const_6327 = relay.const([-1.028481,6.452524,-0.241539,6.620205,-0.135403,-3.213051,-6.992174,5.711183,-2.525434,4.211966,-8.889153,-2.359670,8.920959,-2.096022,1.027201,9.756016,0.178261,-5.960162,5.779655,-7.513044,8.081549,-5.057467,1.772839,7.412532,-1.971985,-1.011103,-9.421578,-7.442951,5.029775,2.094113,1.961830,2.393608,2.929643,-9.574658,2.151505,-3.584753,8.614698,-9.255571,6.260421,4.694796,-9.596675,-6.546282,-1.304720,-4.762588,-7.164640,-9.599710,-7.715964,-3.470820,0.633584,-2.053481,-7.442267,9.680066,9.745121,-4.777744,6.151528,6.743966,6.315419,4.839443,-2.399197,-7.464688,1.766754,-1.856606,-0.898200,1.047980,6.106883,-7.897739,2.260044,-1.407013,4.607192,1.463206,-8.988051,0.829000,-8.638611,3.484456,-3.882579,1.957110,-2.029054,-9.022469,2.875764,-4.637580,9.751507,-2.850260,1.597428,-9.681924,6.566424,9.263086,-7.350986,-6.065066,9.881339,0.138249,4.463049,1.845896,-3.984930,-4.667746,-5.947240,-3.390664,9.043689,-8.830215,2.204084,8.243069,-5.803519,-1.582289,4.229743,6.944098,-5.306112,4.118281,-1.131220,2.747842,-4.572315,-3.204937,3.885188,-1.219844,2.817257,0.410941,5.762461,9.786195,3.530545,-3.393491,-4.581983,-3.552023,-0.358328,-1.683158,-2.946710,6.353702,5.095408,1.447262,8.424114,4.876185,-1.315834,1.383962,-0.395374,6.129691,7.654673,-1.336731,-8.088955,-3.844051,-3.899114,6.755900,5.385820,1.662326,-2.203365,2.858948,5.755741,-2.569400,2.761149,4.421864,-1.176381,6.600541,2.102056,-8.891916,-2.165029,-4.578251,7.707058,-2.433487], dtype = "float64")#candidate|6327|(154,)|const|float64
call_6326 = func_1209_call(relay.reshape(const_6327.astype('float64'), [11, 7, 2]))
call_6328 = func_1209_call(relay.reshape(const_6327.astype('float64'), [11, 7, 2]))
output = relay.Tuple([call_6309,call_6320,call_6323,call_6326,const_6327,])
output2 = relay.Tuple([call_6310,call_6321,call_6324,call_6328,const_6327,])
func_6330 = relay.Function([], output)
mod['func_6330'] = func_6330
mod = relay.transform.InferType()(mod)
mutated_mod['func_6330'] = func_6330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6330_call = mutated_mod.get_global_var('func_6330')
call_6331 = func_6330_call()
output = call_6331
func_6332 = relay.Function([], output)
mutated_mod['func_6332'] = func_6332
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4386_call = mod.get_global_var('func_4386')
func_4388_call = mutated_mod.get_global_var('func_4388')
call_6388 = relay.TupleGetItem(func_4386_call(), 1)
call_6389 = relay.TupleGetItem(func_4388_call(), 1)
func_5234_call = mod.get_global_var('func_5234')
func_5235_call = mutated_mod.get_global_var('func_5235')
call_6400 = relay.TupleGetItem(func_5234_call(), 0)
call_6401 = relay.TupleGetItem(func_5235_call(), 0)
output = relay.Tuple([call_6388,call_6400,])
output2 = relay.Tuple([call_6389,call_6401,])
func_6405 = relay.Function([], output)
mod['func_6405'] = func_6405
mod = relay.transform.InferType()(mod)
mutated_mod['func_6405'] = func_6405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6405_call = mutated_mod.get_global_var('func_6405')
call_6406 = func_6405_call()
output = call_6406
func_6407 = relay.Function([], output)
mutated_mod['func_6407'] = func_6407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5223_call = mod.get_global_var('func_5223')
func_5225_call = mutated_mod.get_global_var('func_5225')
call_6454 = relay.TupleGetItem(func_5223_call(), 0)
call_6455 = relay.TupleGetItem(func_5225_call(), 0)
func_6011_call = mod.get_global_var('func_6011')
func_6014_call = mutated_mod.get_global_var('func_6014')
var_6463 = relay.var("var_6463", dtype = "uint64", shape = (2288,))#candidate|6463|(2288,)|var|uint64
call_6462 = relay.TupleGetItem(func_6011_call(relay.reshape(var_6463.astype('uint64'), [2288,])), 1)
call_6464 = relay.TupleGetItem(func_6014_call(relay.reshape(var_6463.astype('uint64'), [2288,])), 1)
output = relay.Tuple([call_6454,call_6462,var_6463,])
output2 = relay.Tuple([call_6455,call_6464,var_6463,])
func_6480 = relay.Function([var_6463,], output)
mod['func_6480'] = func_6480
mod = relay.transform.InferType()(mod)
var_6481 = relay.var("var_6481", dtype = "uint64", shape = (2288,))#candidate|6481|(2288,)|var|uint64
output = func_6480(var_6481)
func_6482 = relay.Function([var_6481], output)
mutated_mod['func_6482'] = func_6482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6125_call = mod.get_global_var('func_6125')
func_6126_call = mutated_mod.get_global_var('func_6126')
call_6501 = relay.TupleGetItem(func_6125_call(), 0)
call_6502 = relay.TupleGetItem(func_6126_call(), 0)
output = call_6501
output2 = call_6502
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
func_5180_call = mod.get_global_var('func_5180')
func_5182_call = mutated_mod.get_global_var('func_5182')
call_6540 = relay.TupleGetItem(func_5180_call(), 1)
call_6541 = relay.TupleGetItem(func_5182_call(), 1)
func_4325_call = mod.get_global_var('func_4325')
func_4326_call = mutated_mod.get_global_var('func_4326')
call_6544 = relay.TupleGetItem(func_4325_call(), 2)
call_6545 = relay.TupleGetItem(func_4326_call(), 2)
output = relay.Tuple([call_6540,call_6544,])
output2 = relay.Tuple([call_6541,call_6545,])
func_6551 = relay.Function([], output)
mod['func_6551'] = func_6551
mod = relay.transform.InferType()(mod)
output = func_6551()
func_6552 = relay.Function([], output)
mutated_mod['func_6552'] = func_6552
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6553 = relay.const([[[-3,-8,-10,9,-4,4,-3,8,9,-2,5,-4,-7,6,10,1]],[[-4,4,-9,-7,-7,-8,3,2,1,-3,-9,9,-5,3,6,1]],[[-2,-3,1,5,-2,-8,1,5,3,10,6,7,4,-9,3,-8]],[[6,-5,1,4,-5,8,-2,7,2,-7,-9,-10,-4,3,10,4]],[[5,4,1,1,2,-1,-2,-2,-8,-3,-3,9,-3,-7,-6,-10]],[[10,6,3,7,-7,-2,7,-5,2,1,10,-3,4,7,-2,-10]],[[-2,4,-4,-5,-9,9,-2,10,-2,-9,1,-9,-5,5,-5,10]]], dtype = "uint64")#candidate|6553|(7, 1, 16)|const|uint64
var_6554 = relay.var("var_6554", dtype = "uint64", shape = (7, 13, 16))#candidate|6554|(7, 13, 16)|var|uint64
bop_6555 = relay.less(const_6553.astype('bool'), var_6554.astype('bool')) # shape=(7, 13, 16)
output = relay.Tuple([bop_6555,])
output2 = relay.Tuple([bop_6555,])
func_6560 = relay.Function([var_6554,], output)
mod['func_6560'] = func_6560
mod = relay.transform.InferType()(mod)
var_6561 = relay.var("var_6561", dtype = "uint64", shape = (7, 13, 16))#candidate|6561|(7, 13, 16)|var|uint64
output = func_6560(var_6561)
func_6562 = relay.Function([var_6561], output)
mutated_mod['func_6562'] = func_6562
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4758_call = mod.get_global_var('func_4758')
func_4759_call = mutated_mod.get_global_var('func_4759')
call_6672 = func_4758_call()
call_6673 = func_4758_call()
output = relay.Tuple([call_6672,])
output2 = relay.Tuple([call_6673,])
func_6674 = relay.Function([], output)
mod['func_6674'] = func_6674
mod = relay.transform.InferType()(mod)
output = func_6674()
func_6675 = relay.Function([], output)
mutated_mod['func_6675'] = func_6675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4758_call = mod.get_global_var('func_4758')
func_4759_call = mutated_mod.get_global_var('func_4759')
call_6695 = func_4758_call()
call_6696 = func_4758_call()
output = relay.Tuple([call_6695,])
output2 = relay.Tuple([call_6696,])
func_6700 = relay.Function([], output)
mod['func_6700'] = func_6700
mod = relay.transform.InferType()(mod)
mutated_mod['func_6700'] = func_6700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6700_call = mutated_mod.get_global_var('func_6700')
call_6701 = func_6700_call()
output = call_6701
func_6702 = relay.Function([], output)
mutated_mod['func_6702'] = func_6702
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5664_call = mod.get_global_var('func_5664')
func_5665_call = mutated_mod.get_global_var('func_5665')
call_6736 = relay.TupleGetItem(func_5664_call(), 1)
call_6737 = relay.TupleGetItem(func_5665_call(), 1)
output = relay.Tuple([call_6736,])
output2 = relay.Tuple([call_6737,])
func_6800 = relay.Function([], output)
mod['func_6800'] = func_6800
mod = relay.transform.InferType()(mod)
output = func_6800()
func_6801 = relay.Function([], output)
mutated_mod['func_6801'] = func_6801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5865_call = mod.get_global_var('func_5865')
func_5867_call = mutated_mod.get_global_var('func_5867')
call_6888 = func_5865_call()
call_6889 = func_5865_call()
func_5113_call = mod.get_global_var('func_5113')
func_5114_call = mutated_mod.get_global_var('func_5114')
call_6904 = func_5113_call()
call_6905 = func_5113_call()
func_2300_call = mod.get_global_var('func_2300')
func_2302_call = mutated_mod.get_global_var('func_2302')
const_6919 = relay.const([-9.874870,0.798631,6.618349,6.014975,1.541068,-3.404924,5.139500,-1.898610,-5.129909,-5.537298,-1.886977,2.167418,-1.425333,1.050403,-3.503976,6.637118,-0.700608,1.045822,3.930100,-9.142635,5.358268,6.882214,7.572454,2.063114,-9.333268,3.451012,-0.784582,-2.717155,5.352367,4.670322,-2.144125,4.384840,0.619219,-7.670046,9.652232,1.371612,8.034697,3.113205,8.118825,-4.475494,-3.037550,-5.249671,-5.255051,-2.454801,-2.256469,-4.574803,-6.626115,7.004526,-4.909934,-4.854563,-7.359910,-5.787150,-4.658209,-5.886395,-1.078069,1.851905,-1.245511,2.153440,2.908943,0.526245,2.533871,-6.796635,2.775794,5.885880,3.414080,2.888027,-4.365457,-3.844105,-4.942803,-3.650605,3.707519,4.410738,1.311530,9.949801,-0.450858,6.594580,-5.601121,4.008933,3.781263,5.080832,-3.587123,0.408707,-5.910987,-2.193027,-6.658637,1.470901,-0.493358,-5.758183,1.253694,-5.090197,-3.929311,-8.867704,2.883862,-0.312642,-2.170199,-0.788556,-1.479331,8.814178,2.908368,5.601721,-2.429382,4.966677,-0.550337,5.873878,2.708910,8.716158,4.712105,-5.171749,-3.199533,6.586668,-6.089593,5.867071,1.225414,7.105044,-7.880329,7.810837,8.489786,-8.425887,-7.966341,-9.185001,3.466806,9.017297,5.673824,-1.764720,-8.050592,-7.298285,2.893585,1.426610,8.419322,5.391601,-1.243981,-2.787335,2.305842,7.976340,-0.031685,-0.711372,7.771444,-9.750037,8.581419,-1.195603,1.534050,9.220048,2.437134,8.891651,1.762415,-8.614248,0.341597,-3.918576,1.128347,-9.806303,7.489043,-0.686233,-2.992976,3.917588,6.767634,0.346792,-1.862326,3.029803,-1.458806,-8.690005,2.952303,3.530185,-4.434440,8.051817,9.287617,2.693814,-6.223657,0.709449,1.176559,8.692065,4.596060,2.097877,1.443761,8.828386,8.755270,9.452579,-3.591482,-9.723935,-7.114674,6.576397,5.765469,-7.331713,-3.153072,2.023799,-9.616394,-9.395706,2.436607,-7.800242,-4.516158,-8.708604,4.398483,-3.909643,-5.707871,-3.155075,-2.504141,-8.019636], dtype = "float64")#candidate|6919|(196,)|const|float64
call_6918 = func_2300_call(relay.reshape(const_6919.astype('float64'), [7, 14, 2]))
call_6920 = func_2300_call(relay.reshape(const_6919.astype('float64'), [7, 14, 2]))
output = relay.Tuple([call_6888,call_6904,call_6918,const_6919,])
output2 = relay.Tuple([call_6889,call_6905,call_6920,const_6919,])
func_6926 = relay.Function([], output)
mod['func_6926'] = func_6926
mod = relay.transform.InferType()(mod)
output = func_6926()
func_6927 = relay.Function([], output)
mutated_mod['func_6927'] = func_6927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6926_call = mod.get_global_var('func_6926')
func_6927_call = mutated_mod.get_global_var('func_6927')
call_6959 = relay.TupleGetItem(func_6926_call(), 3)
call_6960 = relay.TupleGetItem(func_6927_call(), 3)
func_2300_call = mod.get_global_var('func_2300')
func_2302_call = mutated_mod.get_global_var('func_2302')
call_6970 = func_2300_call(relay.reshape(call_6959.astype('float64'), [7, 14, 2]))
call_6971 = func_2300_call(relay.reshape(call_6959.astype('float64'), [7, 14, 2]))
output = relay.Tuple([call_6959,call_6970,])
output2 = relay.Tuple([call_6960,call_6971,])
func_6979 = relay.Function([], output)
mod['func_6979'] = func_6979
mod = relay.transform.InferType()(mod)
output = func_6979()
func_6980 = relay.Function([], output)
mutated_mod['func_6980'] = func_6980
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5223_call = mod.get_global_var('func_5223')
func_5225_call = mutated_mod.get_global_var('func_5225')
call_7031 = relay.TupleGetItem(func_5223_call(), 0)
call_7032 = relay.TupleGetItem(func_5225_call(), 0)
func_6979_call = mod.get_global_var('func_6979')
func_6980_call = mutated_mod.get_global_var('func_6980')
call_7033 = relay.TupleGetItem(func_6979_call(), 1)
call_7034 = relay.TupleGetItem(func_6980_call(), 1)
output = relay.Tuple([call_7031,call_7033,])
output2 = relay.Tuple([call_7032,call_7034,])
func_7035 = relay.Function([], output)
mod['func_7035'] = func_7035
mod = relay.transform.InferType()(mod)
output = func_7035()
func_7036 = relay.Function([], output)
mutated_mod['func_7036'] = func_7036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5664_call = mod.get_global_var('func_5664')
func_5665_call = mutated_mod.get_global_var('func_5665')
call_7054 = relay.TupleGetItem(func_5664_call(), 1)
call_7055 = relay.TupleGetItem(func_5665_call(), 1)
func_6210_call = mod.get_global_var('func_6210')
func_6212_call = mutated_mod.get_global_var('func_6212')
call_7060 = relay.TupleGetItem(func_6210_call(), 0)
call_7061 = relay.TupleGetItem(func_6212_call(), 0)
output = relay.Tuple([call_7054,call_7060,])
output2 = relay.Tuple([call_7055,call_7061,])
func_7067 = relay.Function([], output)
mod['func_7067'] = func_7067
mod = relay.transform.InferType()(mod)
mutated_mod['func_7067'] = func_7067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7067_call = mutated_mod.get_global_var('func_7067')
call_7068 = func_7067_call()
output = call_7068
func_7069 = relay.Function([], output)
mutated_mod['func_7069'] = func_7069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5137_call = mod.get_global_var('func_5137')
func_5138_call = mutated_mod.get_global_var('func_5138')
call_7075 = relay.TupleGetItem(func_5137_call(), 1)
call_7076 = relay.TupleGetItem(func_5138_call(), 1)
func_6011_call = mod.get_global_var('func_6011')
func_6014_call = mutated_mod.get_global_var('func_6014')
const_7078 = relay.const([3,5,8,-7,3,-4,10,7,-9,-6,-9,10,7,-6,-2,-3,2,8,-4,-8,-9,-5,6,-8,-1,3,-3,-1,-6,7,6,2,-10,10,7,10,-8,3,-6,-10,-7,-10,-3,3,6,7,10,1,-2,-3,-1,-5,7,-5,-10,4,8,-2,-3,-2,2,2,-1,-3,6,-5,8,-5,9,2,5,-1,-9,5,5,-10,9,1,5,-6,-10,7,1,5,-2,-1,2,-1,4,-3,-3,8,-5,3,-2,2,-8,-2,-2,10,1,-2,-3,3,1,6,9,8,-2,-7,-10,8,9,-8,6,-5,-7,-1,-4,-8,10,-10,6,4,-9,-4,-9,8,2,-7,1,-7,-2,1,-3,-10,-2,2,8,-8,7,7,-4,-2,-10,7,4,2,-2,-2,3,-8,2,-5,-5,9,-4,-8,9,5,2,1,-5,1,-9,10,5,-8,-7,-7,-5,6,3,8,-5,-1,4,-2,8,-6,-8,-8,-6,10,-1,-8,5,6,10,-10,-6,4,5,-10,-1,10,5,-10,4,4,1,2,8,2,1,-2,2,-8,4,-10,4,-2,-7,8,6,-9,-6,1,-10,-9,-4,9,-1,-5,-2,-7,4,-5,-6,6,-5,-7,7,-4,-2,9,5,3,2,-10,2,3,9,-1,-9,6,-2,-6,2,6,-2,-9,-3,-5,-10,-1,2,-10,-10,-7,6,6,6,-8,1,-2,9,1,6,6,1,-8,-1,-6,-9,-3,-4,-6,-10,-1,-8,-5,-4,8,-4,-6,4,-8,4,8,-6,-10,-10,3,1,-3,6,-6,6,-2,10,3,-4,9,-4,-3,9,-3,2,-1,9,-1,-1,9,1,-8,-9,-3,2,3,2,-8,-1,-2,-6,-7,-8,-4,-3,8,2,5,7,-8,-1,-6,-9,5,-5,5,9,-8,8,6,5,-7,10,-10,-9,5,-1,4,3,-10,-4,2,4,-2,2,-8,-4,5,7,10,-6,-10,3,-7,-1,5,-1,-3,-6,9,-5,-8,4,-2,1,-10,6,-3,2,-5,6,-2,-8,-4,-10,-6,-2,5,-8,-8,8,5,6,10,8,4,-7,5,-1,-2,3,-7,2,2,8,8,-8,9,1,-3,-7,4,-3,-1,-7,-5,-3,-7,6,-7,-7,-10,8,-8,-3,7,-8,-5,-2,-3,-3,1,-5,-3,6,-3,2,10,5,8,-1,-7,8,7,-2,10,3,1,10,6,1,10,5,3,10,-9,6,9,9,3,10,-7,5,-10,-10,-10,8,-6,2,4,-3,-4,-8,-3,10,-10,-3,3,3,-2,10,5,6,10,1,3,-6,2,-9,-4,-5,1,-9,6,8,6,4,7,-3,9,10,9,-6,-3,-8,-5,-9,-2,1,-4,-8,8,-4,-1,1,-2,-1,-10,-1,-3,9,-5,4,-1,-5,-7,-5,-6,-1,5,-8,-4,7,-5,8,9,-6,8,-2,-9,1,-4,1,7,-9,-4,1,-6,-6,9,7,-1,-6,4,-5,-7,-9,7,10,-3,-8,4,7,-10,-10,-6,10,-1,6,4,-10,-2,-1,10,2,-8,10,-2,3,1,2,2,5,-10,-1,-4,5,-4,4,-8,7,9,-2,-8,2,10,-9,9,6,-6,-4,-9,-6,-9,-7,9,5,-3,8,3,3,7,6,7,-5,-8,-3,10,-10,-2,-6,-10,8,9,9,5,5,-3,7,-2,2,1,-7,-5,-2,3,-7,-10,-8,-8,-2,8,-4,-8,-2,-3,-10,-8,-7,-3,1,6,1,-10,6,-6,2,8,9,-8,6,-3,-6,-3,-5,10,4,-3,-6,4,2,2,5,1,6,5,1,-8,1,9,-2,4,-7,-1,-10,6,-4,-10,-6,5,10,-4,7,9,-7,-4,9,3,4,10,-8,10,3,-2,-10,-3,-6,3,-2,1,-5,6,-4,-2,4,4,8,-5,3,4,-6,-4,-7,-6,-3,6,-2,2,3,6,-7,1,-6,10,6,3,-2,-2,5,-6,5,-8,6,4,-5,-9,1,-10,8,6,-4,4,5,-3,-4,-3,-10,-9,-1,8,-3,8,6,-3,-8,6,10,-5,8,7,8,-2,-1,7,-3,-9,1,-4,-7,-1,8,4,1,-2,9,10,1,6,-4,5,-7,8,2,-4,1,-4,7,6,1,-5,-1,-8,1,-4,8,-4,4,4,4,-6,5,5,-10,-10,-10,1,-1,4,6,7,-7,-10,3,-6,-2,-3,4,9,-8,5,3,1,-9,-4,-1,9,-1,9,-3,-10,-9,9,10,7,6,-10,-10,-1,-4,-3,7,4,-3,10,10,-10,-5,-10,7,-7,-9,-4,-5,-9,-1,7,8,-3,-6,6,7,5,-5,10,-4,8,1,-6,6,-9,-10,2,10,1,-10,-2,-5,10,-3,3,-5,-5,-3,-7,6,4,2,6,-3,8,3,2,-6,-9,3,10,-5,6,-6,4,7,-10,8,-1,-2,-6,-8,5,3,6,-6,-3,1,-8,10,-9,-2,8,-4,2,-9,-2,-1,2,1,-9,4,7,-9,2,-6,6,1,-9,4,-2,-2,-7,-1,6,-7,-8,-4,6,-7,3,-1,-3,-5,-1,6,10,-10,-2,6,-5,-2,3,8,-1,10,-10,5,5,-6,6,2,1,-3,-6,-10,3,6,1,-7,-10,-6,-10,-4,10,-3,-3,2,-8,-6,5,5,-9,8,-4,-2,-4,5,-1,8,10,-8,6,-6,5,9,7,2,5,-5,4,3,8,-9,6,10,1,-8,10,-1,5,6,4,-9,-7,7,-4,7,-6,-2,-8,-6,-2,3,-8,6,-6,7,-10,8,3,-7,4,2,4,2,-6,-10,3,-10,-10,6,9,-6,2,-6,-7,-5,-1,-1,-10,-9,-1,7,-4,7,-3,10,8,3,-7,-4,-6,-5,3,3,9,10,-3,-6,-3,-1,-7,2,-6,-3,8,9,-6,2,-2,-5,-9,3,-3,8,-3,6,-1,-5,-3,-4,-8,4,9,5,3,6,-8,-5,-9,9,-4,-4,-3,-4,7,-9,10,9,9,3,-6,3,10,-7,1,-3,-2,9,-5,-4,-10,-7,6,2,-4,7,-7,-5,10,-6,-9,5,-5,9,-1,2,7,4,9,-1,4,-2,10,-6,9,-9,-2,-10,-3,6,-1,5,-10,-1,6,2,10,1,-1,-10,10,9,-8,-8,5,4,2,5,-2,-3,-10,10,-10,2,9,-4,-3,-10,1,9,10,3,7,-6,-4,-7,5,-6,10,8,10,-8,-4,-2,-6,2,-8,-2,3,-4,-6,-1,10,-7,5,-10,9,6,8,-10,-10,-4,7,3,-3,-5,10,1,-5,-10,6,-3,-2,10,-10,-6,-3,1,8,10,-1,-2,2,10,-4,8,-2,6,-2,6,7,2,-4,-9,-7,4,3,8,9,-3,-10,-4,-3,-8,7,7,-6,3,4,-4,1,10,2,-1,7,6,6,2,10,-4,-6,2,-2,3,7,8,5,-3,-7,10,10,-5,-5,6,9,-4,-1,-6,-1,10,8,7,-7,10,5,-9,-7,-3,-1,10,9,4,2,6,1,-1,-3,10,-9,3,2,10,6,2,4,-5,9,4,1,3,5,1,-4,-7,3,8,-2,5,-4,5,-2,-1,-2,-2,-5,5,1,-8,-6,10,5,-7,8,6,10,2,-2,4,-9,4,-1,4,4,-9,-8,-2,-6,-1,10,10,9,-5,-6,4,3,-9,-9,-8,-6,-5,-5,7,-5,-8,8,-6,-2,9,-8,-3,-4,-7,7,8,-2,8,-2,-9,-3,-2,6,9,9,-6,-2,-1,-9,-9,-6,10,10,5,2,8,2,-8,10,-8,5,7,1,4,-6,8,10,2,-5,1,-3,-3,-1,-5,8,7,7,1,-1,10,7,-3,-8,-8,-2,-10,-10,-9,-4,9,10,-5,1,7,-2,3,-6,8,-1,-9,-7,-5,-4,7,1,-9,-3,9,2,-8,-2,-6,7,-2,-2,1,-10,6,3,1,9,-8,-6,-6,1,-3,-5,1,2,-2,4,4,10,-7,3,-8,8,3,-2,-2,-3,8,-5,1,2,-2,7,-10,7,-1,-5,-3,6,7,-6,-1,-6,-8,7,8,3,6,7,-8,-3,-3,9,-1,3,-2,-9,-8,1,-7,5,8,7,-9,-1,-9,7,5,9,2,-6,-8,7,-1,2,-7,-5,-7,10,-7,5,9,9,10,10,9,-6,2,-3,-2,-2,1,5,-10,-4,-9,-4,-2,2,2,-6,9,-7,5,-5,6,5,7,-5,-6,5,-9,4,5,-7,-8,-7,5,10,-4,7,4,-9,-4,7,5,-5,-4,-8,-5,-3,8,-3,-4,4,-10,9,-5,-7,3,10,8,2,6,-9,7,-5,-4,9,-1,-7,4,-9,4,-7,-9,-3,-2,-7,7,9,-1,-10,-3,4,-1,-9,9,-3,1,8,-7,-7,9,7,-3,9,-1,1,-7,-1,6,-3,-5,7,-6,-8,-7,-4,-10,-2,7,8,-2,5,-4,10,-4,6,-9,9,-8,-10,3,-1,5,9,7,-4,-4,10,5,9,-3,1,8,9,1,10,5,9,7,4,5,2,-8,9,-10,-3,3,-5,5,6,-3,-10,-8,-8,8,8,1,5,10,-3,2,5,1,6,-4,-2,9,-5,4,3,-7,-7,10,-10,-6,5,8,-3,8,6,4,-8,1,-1,9,9,6,8,10,8,-10,3,-1,-8,-10,2,2,6,-5,10,-10,4,9,-1,10,4,-2,-10,5,-3,-2,-8,7,10,10,10,3,7,-5,-8,10,7,-10,7,4,-10,-7,1,-2,-7,-2,-2,2,6,10,4,-7,1,7,3,-10,-8,-3,10,-3,-8,6,10,9,-5,2,-10,8,6,-1,-7,-4,-7,-5,2,6,2,10,-9,-10,10,4,10,-1,-7,5,-3,-10,-6,7,-4,-8,4,10,8,8,1,10,-5,-10,-5,-8,-6,9,3,1,-1,-4,8,-10,4,-6,1,-8,9,9,-5,-4,-5,-2,-1,6,2,10,-3,-6,-10,2,10,-10,-8,-5,-7,-1,-4,-9,-5,-8,4,-7,-10,-2,7,6,5,-8,-6,-5,4,3,10,4,8,2,-1,9,-2,-4,8,-6,-5,-4,-9,-3,-5,-2,10,-10,-7,-2,-3,-2,3,-4,5,2,8,2,-6,-2,-1,6,10,10,10,8,3,8,5,7,-4,1,-6,1,7,-3,-8,10,6,-7,-1,10,2,-10,-10,6,-7,-7,-9,-6,-2,5,-9,9,-4,-2,1,9,-9,-2,-5,4,7,-4,10,5,1,3,6,5,-10,6,-10,5,-1,8,-7,-7,-6,3,3,1,9,-1,-5,6,5,7,7,7,-10,6,-9,-2,-6,-4,-2,-2,-8,7,-1,-1,6,-4,-1,-5,-7,-10,7,-3,8,3,-2,-2,-8,-6,-3,9,-6,-4,-5,-7,3,-9,1,3,-9,1,9,-4,2,10,-6,5,-2,-8,-10,-7,4,1,-8,-7,1,10,1,1,-5,-9,9,-4,2,8,-9,-5,3,-2,-2,-9,7,7,5,-3,8,-3,5,8,9,1,10,-1,-4,3,-2,-3,4,-8,7,-1,-3,-1,-10,-6,-4,-7,3,-7,-2,4,-3,-4,-6,-5,-6,-9,-1,-9,-1,1,2,-10,-7,5,-7,3,8,6,2,9,10,-8,10,1,2,7,-2,-10,-3,-8,4,10,-3,-7,10,4,6,10,-9,9,4,7,2,5,-2,8,8,-9,-6,3,-4,7,-9,6,-9,9,-1,-9,4,10,9,-4,-6,6,-1,10,-8,-3,-8,-6,4,-10,2,9,5,1,-7,-1,-2,-7,-9,-8,5,-5,2,10,7,-2,1,-4,-9,2,-2,1,1,-6,-4,-7,-6,4,4,-4,3,-9,-7,3,-7,-4,-8,-2,-10,1,-3,-4,3,-6,1,-7,6,-1,8,-1,-10,4,9,-9,6,-6,8,-5,8,-7,1,-5,1,-2,-3,4,9,3,7,8,4,10,3,-5,9,2,-8,-1,-5,10,7,1,-3,3,-8,3,4,-4,-1,10,10,1,10,-1,-4,-3,6,-6,-10,-8,1,-10,7,4,2,-7,7,-2,-8,2,-3,-3,-10,-7,8,-1,-9], dtype = "uint64")#candidate|7078|(2288,)|const|uint64
call_7077 = relay.TupleGetItem(func_6011_call(relay.reshape(const_7078.astype('uint64'), [2288,])), 0)
call_7079 = relay.TupleGetItem(func_6014_call(relay.reshape(const_7078.astype('uint64'), [2288,])), 0)
output = relay.Tuple([call_7075,call_7077,const_7078,])
output2 = relay.Tuple([call_7076,call_7079,const_7078,])
func_7082 = relay.Function([], output)
mod['func_7082'] = func_7082
mod = relay.transform.InferType()(mod)
mutated_mod['func_7082'] = func_7082
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7082_call = mutated_mod.get_global_var('func_7082')
call_7083 = func_7082_call()
output = call_7083
func_7084 = relay.Function([], output)
mutated_mod['func_7084'] = func_7084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5345_call = mod.get_global_var('func_5345')
func_5346_call = mutated_mod.get_global_var('func_5346')
call_7107 = relay.TupleGetItem(func_5345_call(), 0)
call_7108 = relay.TupleGetItem(func_5346_call(), 0)
var_7143 = relay.var("var_7143", dtype = "float64", shape = (7, 2, 5))#candidate|7143|(7, 2, 5)|var|float64
bop_7144 = relay.floor_divide(call_7107.astype('float64'), relay.reshape(var_7143.astype('float64'), relay.shape_of(call_7107))) # shape=(7, 2, 5)
bop_7147 = relay.floor_divide(call_7108.astype('float64'), relay.reshape(var_7143.astype('float64'), relay.shape_of(call_7108))) # shape=(7, 2, 5)
output = bop_7144
output2 = bop_7147
func_7162 = relay.Function([var_7143,], output)
mod['func_7162'] = func_7162
mod = relay.transform.InferType()(mod)
mutated_mod['func_7162'] = func_7162
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7163 = relay.var("var_7163", dtype = "float64", shape = (7, 2, 5))#candidate|7163|(7, 2, 5)|var|float64
func_7162_call = mutated_mod.get_global_var('func_7162')
call_7164 = func_7162_call(var_7163)
output = call_7164
func_7165 = relay.Function([var_7163], output)
mutated_mod['func_7165'] = func_7165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5372_call = mod.get_global_var('func_5372')
func_5374_call = mutated_mod.get_global_var('func_5374')
call_7214 = func_5372_call()
call_7215 = func_5372_call()
func_6551_call = mod.get_global_var('func_6551')
func_6552_call = mutated_mod.get_global_var('func_6552')
call_7218 = relay.TupleGetItem(func_6551_call(), 1)
call_7219 = relay.TupleGetItem(func_6552_call(), 1)
func_6405_call = mod.get_global_var('func_6405')
func_6407_call = mutated_mod.get_global_var('func_6407')
call_7224 = relay.TupleGetItem(func_6405_call(), 0)
call_7225 = relay.TupleGetItem(func_6407_call(), 0)
output = relay.Tuple([call_7214,call_7218,call_7224,])
output2 = relay.Tuple([call_7215,call_7219,call_7225,])
func_7227 = relay.Function([], output)
mod['func_7227'] = func_7227
mod = relay.transform.InferType()(mod)
output = func_7227()
func_7228 = relay.Function([], output)
mutated_mod['func_7228'] = func_7228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7035_call = mod.get_global_var('func_7035')
func_7036_call = mutated_mod.get_global_var('func_7036')
call_7229 = relay.TupleGetItem(func_7035_call(), 0)
call_7230 = relay.TupleGetItem(func_7036_call(), 0)
output = relay.Tuple([call_7229,])
output2 = relay.Tuple([call_7230,])
func_7277 = relay.Function([], output)
mod['func_7277'] = func_7277
mod = relay.transform.InferType()(mod)
mutated_mod['func_7277'] = func_7277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7277_call = mutated_mod.get_global_var('func_7277')
call_7278 = func_7277_call()
output = call_7278
func_7279 = relay.Function([], output)
mutated_mod['func_7279'] = func_7279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5372_call = mod.get_global_var('func_5372')
func_5374_call = mutated_mod.get_global_var('func_5374')
call_7287 = func_5372_call()
call_7288 = func_5372_call()
func_5223_call = mod.get_global_var('func_5223')
func_5225_call = mutated_mod.get_global_var('func_5225')
call_7291 = relay.TupleGetItem(func_5223_call(), 0)
call_7292 = relay.TupleGetItem(func_5225_call(), 0)
func_5180_call = mod.get_global_var('func_5180')
func_5182_call = mutated_mod.get_global_var('func_5182')
call_7297 = relay.TupleGetItem(func_5180_call(), 2)
call_7298 = relay.TupleGetItem(func_5182_call(), 2)
output = relay.Tuple([call_7287,call_7291,call_7297,])
output2 = relay.Tuple([call_7288,call_7292,call_7298,])
func_7299 = relay.Function([], output)
mod['func_7299'] = func_7299
mod = relay.transform.InferType()(mod)
mutated_mod['func_7299'] = func_7299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7299_call = mutated_mod.get_global_var('func_7299')
call_7300 = func_7299_call()
output = call_7300
func_7301 = relay.Function([], output)
mutated_mod['func_7301'] = func_7301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5113_call = mod.get_global_var('func_5113')
func_5114_call = mutated_mod.get_global_var('func_5114')
call_7305 = func_5113_call()
call_7306 = func_5113_call()
func_3334_call = mod.get_global_var('func_3334')
func_3338_call = mutated_mod.get_global_var('func_3338')
const_7308 = relay.const([True,True,False,False,False,True,False,False,False,False,True,False,False,True,False,True,True,True,False,True,True,True,True,False,True,True,False,False,False,True,True,False,False,False,False,False,True,False,False,True,True,True,True,True,False,True,False,True,True,False,False,False,False,False,False,True,True,True,False,False,False,True,False,False,True,False,False,False,True,False,True,False,True,True,True,True,False,False,False,True,False,True,False,False,True,False,False,False,True,False,False,True,True,False,True,True,True,True,True,False,True,True,False,False,False,True,True,False,True,False,False,False,True,False,False,False,False,False,False,False,False,True,True,False,True,True,True,False,False,False,False,False,True,False,False,True,False,False,False,True,False,False,True,True,False,False,True,False,False,True,False,True,False,False,True,False,True,False,False,True,False,True,True,False,True,False,True,True,False,True,True,False,True,False,True,True,False,False,False,True,True,False,False,False,False,True,False,True,True,False,True,True,True,False,True,True,False,True,False,False,False,True,False,False,False,True,True,False,True,True,True,True,False,True,True,False,False,True,False,True,True,True,True,True,True,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,True,False,True,True,True,False,True,False,True,True,True,False,False,False,True,False,True,True,False,False,False,False,False,False,True,False,False,False,False,False,False,True,False,True,False,False,True,True,False,False,True,True,False,True,False,False,True,True,True,True,True,True,False,False,True,True,False,True,True,False,False,True,True,False,False,True,False,True,True,False,True,False,False,False,True,False,False,True,True,True,False,False,True,False,False,False,False,True,False,True,True,False,True,True,False,True,False,True,True,True,True,False,True,True,False,True,True,False,False,False,False,False,True,True,True,True,True,True,False,True,False,False,True,True,True,False,True,True,True,False,True,False,False,False,False,True,True,True,True,True,False,True,False,True,False,True,False,False,False,True,True,False,True,True,False,False,True,True,True,False,True,False,False,True,True,False,False,False,False,False,False,False,True,False,True,False,True,True,False,True,False,True,True,True,False,True,True,True,False,True,True,True,True,False,True,False,False,True,True,False,True,True,False,True,True,True,True,False,True,True,True,True,False,False,True,True,False,False,False,False,True,False,False,True,False,True,True,False,False,False,True,False,True,True,True,False,True,False,False,False,True,True,True,True,False,False,False,False,True,True,False,False,True,False,True,True,True,True,True,False,True,False,False,True,False,True,True,True,True,False,True,False,True,False,True,True,True,False,True,False,True,False,False,False,False,False,True,False,True,False,False,False,True,False,True,True,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,False,False,False,True,False,False,False,True,True,False,True,False,True,True,False,False,False,False,True,False,False,True,False,True,False,True,True,True], dtype = "bool")#candidate|7308|(588,)|const|bool
const_7309 = relay.const([[7.583758],[-1.488189],[7.304135],[-5.356610],[-2.344763],[5.178247],[-4.887886],[9.111686],[-3.184010],[-6.894072],[-1.136804],[-8.894959],[9.329512],[9.552529],[-5.958397],[-8.764280],[-4.778281],[1.293119],[9.163390],[-5.505714],[8.600171],[-0.384802],[-1.124769],[-0.568860],[8.024150],[8.656500],[-8.908066],[-4.689252],[-4.201758],[6.502832],[-9.934918],[-5.326108],[4.357718],[-0.857297],[-6.454322],[-0.081245],[-3.584580],[2.895279],[3.255369],[6.641627],[0.398611],[-2.209348],[-5.849419],[9.386256],[6.951991],[3.587468],[-5.803684],[-5.511842],[1.605507],[-3.895306],[3.776653],[3.397691],[-2.821680],[-2.664174],[0.791469],[-5.990810],[4.090320],[-2.973405],[8.875168],[-0.637045],[-6.497003],[-4.104458],[7.711571],[-8.639253],[9.732754],[-6.490125],[-2.211491],[-1.986573],[4.739889],[-1.839754],[-8.769080],[4.701854],[6.462952],[9.116030],[3.026694],[0.360803],[-5.164042],[2.451632],[-4.889432],[-8.466557],[-1.865309],[-5.418061],[2.234350],[8.457390],[-9.786954],[9.313617],[-9.560869],[-5.734453],[-4.288671],[2.257047],[5.617216],[7.321743],[-2.679075],[3.995446],[5.076063],[3.367032],[3.486573],[-6.168579],[-7.970439],[2.114992],[3.916330],[-2.221488],[9.616697],[3.007646],[-2.430894],[7.245823],[-1.473921],[3.567237],[5.519620],[7.349824],[0.006618],[2.024790],[7.174731],[7.820172],[4.941419],[-4.082844],[4.595072],[0.329484],[7.188118],[-4.544968],[5.870915],[3.903526],[-0.743862],[-7.557490],[6.773338],[-3.514411]], dtype = "float32")#candidate|7309|(126, 1)|const|float32
var_7310 = relay.var("var_7310", dtype = "float32", shape = (2640,))#candidate|7310|(2640,)|var|float32
call_7307 = relay.TupleGetItem(func_3334_call(relay.reshape(const_7308.astype('bool'), [7, 7, 12]), relay.reshape(const_7309.astype('float32'), [126, 1]), relay.reshape(var_7310.astype('float32'), [4, 660]), ), 7)
call_7311 = relay.TupleGetItem(func_3338_call(relay.reshape(const_7308.astype('bool'), [7, 7, 12]), relay.reshape(const_7309.astype('float32'), [126, 1]), relay.reshape(var_7310.astype('float32'), [4, 660]), ), 7)
func_4838_call = mod.get_global_var('func_4838')
func_4840_call = mutated_mod.get_global_var('func_4840')
call_7312 = relay.TupleGetItem(func_4838_call(relay.reshape(const_7309.astype('float32'), [126,])), 2)
call_7313 = relay.TupleGetItem(func_4840_call(relay.reshape(const_7309.astype('float32'), [126,])), 2)
output = relay.Tuple([call_7305,call_7307,const_7308,const_7309,var_7310,call_7312,])
output2 = relay.Tuple([call_7306,call_7311,const_7308,const_7309,var_7310,call_7313,])
func_7316 = relay.Function([var_7310,], output)
mod['func_7316'] = func_7316
mod = relay.transform.InferType()(mod)
mutated_mod['func_7316'] = func_7316
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7317 = relay.var("var_7317", dtype = "float32", shape = (2640,))#candidate|7317|(2640,)|var|float32
func_7316_call = mutated_mod.get_global_var('func_7316')
call_7318 = func_7316_call(var_7317)
output = call_7318
func_7319 = relay.Function([var_7317], output)
mutated_mod['func_7319'] = func_7319
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7336 = relay.var("var_7336", dtype = "float64", shape = (10, 10, 11))#candidate|7336|(10, 10, 11)|var|float64
var_7337 = relay.var("var_7337", dtype = "float64", shape = (10, 10, 11))#candidate|7337|(10, 10, 11)|var|float64
bop_7338 = relay.divide(var_7336.astype('float64'), relay.reshape(var_7337.astype('float64'), relay.shape_of(var_7336))) # shape=(10, 10, 11)
func_5180_call = mod.get_global_var('func_5180')
func_5182_call = mutated_mod.get_global_var('func_5182')
call_7347 = relay.TupleGetItem(func_5180_call(), 3)
call_7348 = relay.TupleGetItem(func_5182_call(), 3)
func_4584_call = mod.get_global_var('func_4584')
func_4586_call = mutated_mod.get_global_var('func_4586')
var_7351 = relay.var("var_7351", dtype = "int16", shape = (126,))#candidate|7351|(126,)|var|int16
call_7350 = relay.TupleGetItem(func_4584_call(relay.reshape(var_7351.astype('int16'), [7, 2, 9])), 0)
call_7352 = relay.TupleGetItem(func_4586_call(relay.reshape(var_7351.astype('int16'), [7, 2, 9])), 0)
func_6700_call = mod.get_global_var('func_6700')
func_6702_call = mutated_mod.get_global_var('func_6702')
call_7354 = relay.TupleGetItem(func_6700_call(), 0)
call_7355 = relay.TupleGetItem(func_6702_call(), 0)
func_7067_call = mod.get_global_var('func_7067')
func_7069_call = mutated_mod.get_global_var('func_7069')
call_7370 = relay.TupleGetItem(func_7067_call(), 1)
call_7371 = relay.TupleGetItem(func_7069_call(), 1)
func_7299_call = mod.get_global_var('func_7299')
func_7301_call = mutated_mod.get_global_var('func_7301')
call_7385 = relay.TupleGetItem(func_7299_call(), 2)
call_7386 = relay.TupleGetItem(func_7301_call(), 2)
output = relay.Tuple([bop_7338,call_7347,call_7350,var_7351,call_7354,call_7370,call_7385,])
output2 = relay.Tuple([bop_7338,call_7348,call_7352,var_7351,call_7355,call_7371,call_7386,])
func_7391 = relay.Function([var_7336,var_7337,var_7351,], output)
mod['func_7391'] = func_7391
mod = relay.transform.InferType()(mod)
mutated_mod['func_7391'] = func_7391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7391_call = mutated_mod.get_global_var('func_7391')
var_7393 = relay.var("var_7393", dtype = "float64", shape = (10, 10, 11))#candidate|7393|(10, 10, 11)|var|float64
var_7394 = relay.var("var_7394", dtype = "float64", shape = (10, 10, 11))#candidate|7394|(10, 10, 11)|var|float64
var_7395 = relay.var("var_7395", dtype = "int16", shape = (126,))#candidate|7395|(126,)|var|int16
call_7392 = func_7391_call(var_7393,var_7394,var_7395,)
output = call_7392
func_7396 = relay.Function([var_7393,var_7394,var_7395,], output)
mutated_mod['func_7396'] = func_7396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7277_call = mod.get_global_var('func_7277')
func_7279_call = mutated_mod.get_global_var('func_7279')
call_7417 = relay.TupleGetItem(func_7277_call(), 0)
call_7418 = relay.TupleGetItem(func_7279_call(), 0)
output = call_7417
output2 = call_7418
func_7440 = relay.Function([], output)
mod['func_7440'] = func_7440
mod = relay.transform.InferType()(mod)
mutated_mod['func_7440'] = func_7440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7440_call = mutated_mod.get_global_var('func_7440')
call_7441 = func_7440_call()
output = call_7441
func_7442 = relay.Function([], output)
mutated_mod['func_7442'] = func_7442
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7451 = relay.var("var_7451", dtype = "uint8", shape = ())#candidate|7451|()|var|uint8
var_7452 = relay.var("var_7452", dtype = "uint8", shape = (6, 1, 15))#candidate|7452|(6, 1, 15)|var|uint8
bop_7453 = relay.left_shift(var_7451.astype('uint8'), var_7452.astype('uint8')) # shape=(6, 1, 15)
bop_7468 = relay.mod(var_7451.astype('float64'), var_7452.astype('float64')) # shape=(6, 1, 15)
bop_7472 = relay.floor_mod(bop_7468.astype('float64'), var_7451.astype('float64')) # shape=(6, 1, 15)
output = relay.Tuple([bop_7453,bop_7472,])
output2 = relay.Tuple([bop_7453,bop_7472,])
func_7476 = relay.Function([var_7451,var_7452,], output)
mod['func_7476'] = func_7476
mod = relay.transform.InferType()(mod)
mutated_mod['func_7476'] = func_7476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7476_call = mutated_mod.get_global_var('func_7476')
var_7478 = relay.var("var_7478", dtype = "uint8", shape = ())#candidate|7478|()|var|uint8
var_7479 = relay.var("var_7479", dtype = "uint8", shape = (6, 1, 15))#candidate|7479|(6, 1, 15)|var|uint8
call_7477 = func_7476_call(var_7478,var_7479,)
output = call_7477
func_7480 = relay.Function([var_7478,var_7479,], output)
mutated_mod['func_7480'] = func_7480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5829_call = mod.get_global_var('func_5829')
func_5830_call = mutated_mod.get_global_var('func_5830')
call_7493 = relay.TupleGetItem(func_5829_call(), 0)
call_7494 = relay.TupleGetItem(func_5830_call(), 0)
func_2517_call = mod.get_global_var('func_2517')
func_2521_call = mutated_mod.get_global_var('func_2521')
const_7500 = relay.const([-7.260627,-0.415279,-4.405762,9.949817,-6.347974,-7.536155,9.390596,-2.236002,3.887118,6.746604,0.012758,-1.016728,8.616925,6.257232,7.906146,0.995230,-3.414142,-5.049240,-5.687488,8.173403,4.641874,-7.554422,5.996858,4.999431,-2.195688,-3.748852,4.455732,0.100202,1.844207,3.314192,-2.585038,-6.419385,-3.278930,2.832803,-1.709049,6.612591,-3.132577,-5.859865,9.667677,1.325122,-6.232609,0.606023,-7.215034,-1.997196,0.883265,-8.129170,3.946898,-0.051107,2.061933,-4.689185,-7.436378,-9.629283,3.577730,-6.754345,-1.812643,-8.489606,0.344664,-8.897268,-9.199669,4.537316,-3.689033,5.073589,-5.991785,0.040105,-1.900873,-2.900798,-3.806277,8.072107,4.057917,-2.150938,7.682997,1.132693,-2.192613,-3.200323,-6.827068,-7.820814,7.461378,-8.743181,4.696176,-0.981535,-3.370498,-0.321708,0.629303,-9.859961,0.265624,-8.370800,-0.098633,-0.147748,-2.293999,5.278665,-6.224682,3.916853,-4.694438,-8.446542,-6.963540,3.083794,1.983147,2.591578,9.491900,5.962124,-2.728873,-2.841545,2.912698,1.149365,8.932274,1.226306,-1.084481,-2.352345,-5.265878,-4.170168,2.927113,6.103627,9.284154,5.384616,7.821625,1.037633,-8.967714,-7.825581,-8.592958,2.596615,-3.739780,-7.795090,-8.954378,9.595039,4.696116,4.976895,0.807355,2.520237,5.501990,-8.459661,6.313913,-5.857771,9.563568,-4.242407,-4.119656,2.118233,-0.560629,2.454127,-1.270078,2.859236,-5.040504,-5.529407,-7.764290,-9.632008,-3.710341,-2.597768,-4.437794,-3.313250,3.150312,-5.822201,-9.842304,-8.299656,7.526738,4.789122,4.494612,3.978491,2.162295,3.557378,2.895759,9.912926,-9.482914,0.689008,-7.437730,-3.634941,-6.262250,6.946029,5.204419,5.497214,0.280283,-5.776552,-3.652034,-9.831367,-8.756211,5.700979,0.443831,7.350819,-4.860092,4.630643,-7.478230,-7.971599,-7.265327,-7.748674,0.722230,-5.989758,-3.089826,9.602691,-7.241424,5.000646,-6.060490,-2.446252,1.509353,6.739091,-9.235594,8.279206,3.531310,-6.226452,0.720307,3.412030,-8.652624,-2.748407,-7.443862,7.526051,6.718953,3.475032,7.013841,-4.225428,-1.577763,-8.051538,-4.031479,3.353867,2.013777,2.169703,-7.839103,-0.225717,-6.146950,-4.281298,-9.437811,2.105261,-1.943904,8.061488,-5.425742,-4.776154,-2.055407,6.434516,-6.233688,-8.136443,-6.231473,2.576008,-9.391670,-1.747619,-5.400899,8.809539,-7.391787,-3.577671,-4.941433,4.088250,7.560689,2.857011,-0.438996,-9.781847,0.923684,9.217929,-7.396149,4.030080,-4.083398,6.943426,-7.305554,2.233856,2.203900,2.079091,-1.448465,-6.355536,-4.363622,0.653786,8.942387,-6.305821,-5.800797,-4.710857,-9.543933,6.790874,0.681052,4.306572,9.800638,7.029776,-4.095536,-5.403517,8.067061,8.438732,-1.082800,-2.864054,-3.685098,7.152206,-2.401164,-9.536198,7.549457,3.780051,-5.389889,-7.352455,-4.733320,2.037277,-6.335751,4.575621,-7.820339,1.944807,2.462775,-6.835949,-9.453022,-1.727349,-0.041930,8.640652,-3.251820,-8.883554,9.744680,-3.492659,-4.015154,2.404532,-7.645013,-5.626753,3.278851,9.115898,-0.332003,-8.367782,0.986716,5.223467,4.642417,2.554509,-1.643808,0.850201,-2.932078,5.063138,0.800239,4.195889,9.493249,-9.261826,-1.067104,6.468530,-8.743504,0.441545,-7.033925,9.225065,-7.311607,0.149428,-0.021848,-9.549371,-3.552478,-8.669648,-9.027663,6.104754,1.272530,-9.147713,-0.123722,-3.479056,-3.033456,-4.180494,1.903423,-1.730912,5.322597,-5.767960,-5.880587,-7.596671,-2.127987,-1.686630,7.447370,-6.805746,-7.525331,-3.541035,-0.521062,4.161017,-4.486908,0.197984,4.683568,3.979156,8.492968,-6.612291,7.907644,-1.645034,2.131136,-1.090880,7.459058,-9.592274,-6.439718,-7.723694,9.720448,5.680415,9.866667,8.760755,-7.995415,1.083517,-8.957450,-2.486503,5.512815,5.611685,1.543081,6.285549,-3.935095,-8.276828,-4.204421,8.205684,-6.191126,8.816279,4.715387,-1.446076,-4.977272,5.449156,-2.276162,-1.906362,9.865063,-9.571941,1.739005,6.367391,4.741243,-9.734153,-9.589113,-2.793757,-3.345946,-0.940600,-6.593677,-8.732170,8.030646,-6.647718,3.631475,7.259719,-0.235441,4.075777,0.192068,-6.354306,9.570863,-5.395477,-4.275407,-6.684912,-4.610990,4.126738,-0.183470,8.149834,4.579316,7.969978,-6.838161,1.720879,-3.797349,9.952576,1.624628,2.316237,-9.867314,-1.230397,-9.185688,-7.258778,-9.132063,5.579593,4.693158,-8.536853,-5.872792,3.518595,-0.681604,-5.284575,5.582370,-3.758209,1.387624,6.085254,8.273477,-8.321595,7.191715,-9.710866,-9.769175,-7.627563,8.668678,3.631142,-2.352658,-5.631709,4.775269,0.816408,-3.984200,-6.663402,0.834102,-9.777925,4.565356,-9.997972,8.628978,-3.957043,2.498672,9.964771,4.711141,-6.614397,9.737051,-7.428987,9.511157,1.729982,4.932316,0.744212,-2.238274,0.342889,0.224005,-7.694375,3.048359,-2.178303,1.984752,9.220039,-2.961712,-5.004069,-5.935753,3.253066,-3.432182,-2.111936,-9.323363,3.363172,9.269504,-3.638196,-0.118837,1.582438,-5.463932,-3.314743,1.573614,-0.545877,-2.317957,0.067587,-9.827948,-9.074781,3.347314,-9.306899,3.943046,-0.164923,0.853503,6.891717,6.561642,3.667019,-3.924579,7.550034,4.348488,-2.472103,-1.993214,-8.249650,-8.167241,-8.535582,5.937735,4.785039,-8.736969,0.294348,-7.461798,5.809117,2.578513,1.727871,1.963208,6.365022,2.359271,-0.656119,2.061682,-9.564049,1.984303,-1.093482,8.919218,1.308700,0.614881,4.742306,6.447885,-0.985189,4.251408,7.313098,-2.677163,1.228214,-7.793102,-0.340169,0.641580,8.653653,3.797872,9.102161,7.562620,-7.675388,-8.504368,-5.642089,-1.987053,-2.674419,8.015422,-8.906929,8.363399,2.993081,5.024193,4.918385,-6.419029,-2.674635,-8.277229,-4.043420,-8.115492,2.714988,6.264651,0.879192,-0.901910,9.834385,1.755245,2.876135,-5.519513,-7.984881,-8.498772,-0.872253,-5.805672,-6.678534,-8.975828,-0.423420,7.374245,4.145700,0.458927,2.500598,0.056601,8.769216,-1.683538,1.511235,1.512591,0.822731,5.320589,-1.122268,-8.258609,5.581983,-3.304821,7.972935,3.796122,-0.359397,7.564078,-4.258270,-0.341207,9.448420,-1.208037,0.232239,-0.640831,-9.820200,-4.307681,0.655113,8.532925,-3.322234,-0.870493,-3.428854,-0.946564,9.605545,-5.228287,-4.283356,9.493355,7.937022,-6.359136,-9.426842,8.593938,5.356841,3.251659,-3.343819,4.630500,-9.463485,0.082450,6.909252,2.321694,0.285122,-6.488468,8.391518,-6.212638,6.015276,0.702220,6.366051,-3.356809,1.268041,-5.442625,2.595750,-7.556343,8.995456,-4.545197,2.174464,4.364417,4.917352,8.820857,-4.949567,1.922910,-4.673791,8.590518,-8.030903,-5.094154,9.786266,5.764593,-1.612886,5.966401,9.590847,-1.481982,6.909968,-0.691181,7.618701,3.008359,8.624152,-7.234370,-1.607759,8.950898,0.429449,-8.576760,-9.302683,9.181515,9.342162,3.963010,-4.042168,2.904428,1.535062,-9.855442,7.987612,-5.908086,1.817056,4.826592,-7.356959,-2.785196,-8.551745,2.356034,-7.467299,-0.556859,1.427456,3.172299,4.299991,3.987878,-9.345952,-4.746625,-0.725839,-4.406956,3.815917,9.136987,-0.226346,8.817896,-2.091351,-8.161797,-7.502768,-1.697264,-6.036203,2.534202,-1.149136,-3.674214,9.965019,1.280099,-8.514411,6.117916,6.483836,0.985461,-9.292595,-0.919078,6.505990,2.997192,9.162546,7.350415,0.543721,-4.131757,-4.228169,-2.314158,0.940446,3.398724,7.787504,3.215929,3.100809,4.566435,2.099088,-3.042566,-0.125961,-6.356437,3.231606,9.023393,9.356620,-2.174160,-9.856938,3.010329,-8.380481,1.333509,8.509576,-2.733414,-9.990867,-6.332623,-8.595289,-9.247656,-0.279432,-7.605071,6.166457,0.639839,7.751366,-9.675206,-4.397800,6.986469,-7.893261,7.434415,4.001792,-8.567616,9.335276,-0.472784,4.399683,-8.005751,2.090144,7.487521,-5.698300,2.477678,-9.433560,1.058719,8.296687,-2.025106,-3.123722,9.530302,9.849075,5.768634,-8.741534,-9.163363,-8.725323,-2.497979,-6.679899,-2.465843,-4.448526,-5.152925,1.888768,1.203493,3.435506,-9.428506,9.350463,4.854114,4.860273,5.223771,-4.706273,2.841756,-0.861307,9.591496,3.803144,6.438523,9.457391,1.989600,-1.493418,-2.274850,-0.253152,0.880867,-2.810830,-4.390100,2.127893,-7.089135,-1.401626,-4.770675,0.761565,9.014982,-2.778086,-2.269025,-0.691506,-4.947388,-5.382254,-9.176733,-5.720393,9.056976,5.615723,-8.850254,6.372936,-8.749947,4.687559,6.806003,-8.949584,5.365666,4.768124,5.853426,6.521020,-7.478510,-3.271068,-5.132808,-5.140036,3.970362,-5.000120,-8.304930,-9.669619,5.147270,-8.827703,-4.065708,0.763686,4.733033,4.168859,-6.572498,-6.981359,2.709830,-3.370949,8.236057,7.455608,-1.677804,0.840795,7.742156,4.999552,1.706336,3.119705,6.964768,7.469338,-1.133307,2.735193,-2.973328,0.869373,-4.565947,1.752764,1.781760,-7.020408,-8.994983,-2.919295,-9.318976,-6.913005,2.329136,6.177104,-7.692681,0.628195,-0.148776,-0.744320,3.043201,-2.581431,7.596364,2.348199,-4.018718,-8.989937,3.193457,-1.739419,-5.023635,9.785728,9.061128,-1.719950,-4.237740,-4.247689,-4.759159,0.370530,-4.175730,8.922500,4.513311,-6.558136,1.853415,2.753751,-8.335945,-1.580219,-2.998358,-2.547269,-1.971683,-2.787325,9.740433,6.980033,6.903146,9.016996,-6.792064,4.757631,4.416068,3.734895,-9.171129,-5.573411,6.171818,9.652175,-1.403149,1.854728,0.837138,4.348835,-6.456425,-7.165034,6.661971,4.502950,2.505846,-7.696220,7.236206,2.516667,-5.645217,-7.764001,-8.730476,1.515058,3.303344,3.408132,-1.295308,7.641333,-3.249175,-7.091405,3.614645,9.598863,-5.609736,-5.727004,-0.046262,8.149732,5.206226,-6.430797,-9.277884,-6.738157,-0.916567,-8.697317,5.733735,1.648392,4.846574,9.859446,1.648153,7.399532,-1.526355,0.368422,9.683976,6.588762,-2.501239,-9.811649,-8.238867,8.967863,4.839748,4.153340,7.139387,-3.285996,2.766182,-2.523906,-7.900280,-0.823828,1.170744,2.518774,6.962303,1.239867,-0.489980,-0.954993,-5.656840,9.603472,8.243913,-4.824496,4.347958,7.999053,5.921554,-8.204640,-3.445365,-7.308714,-9.486135,-2.044186,7.804846,-9.334785,-6.572456,-9.535294,-5.230782,-3.439125,-9.110307,-8.986888,7.777121,-6.172395,8.344436,-7.424786,-9.132909,3.783328,7.762967,-9.135393,0.321154,-1.972444,4.006487,5.480857,4.574790,8.318524,-9.613339,2.787629,9.983639,-6.335699,-9.524026,-6.163349,-3.247626,-1.999246,-4.044666,-7.737231,9.764992,9.365662,9.345766,-2.386008,-2.125051,-0.399378,3.291674,-2.988667,-7.375293,-0.503991,2.859162,1.108251,-8.411010,9.015065,-4.778066,3.221402,2.376833,-6.248881,4.089168,2.298470,-5.501705,-2.620435,2.690133,-3.567751,-5.216012,5.061769,-1.793387,9.873864,-2.903744,9.350666,-5.817402,-5.274574,5.740273,-3.204346,6.431001,-5.624384,4.797366,5.356679,5.267527,-8.213292,-1.475149,6.143256,-5.830498,-8.041652,-3.518844,3.647600,-7.476193,-7.863422,-5.555738,-0.349476,-6.102455,3.924535,0.079746,-3.957793,8.301347,-8.170784,-5.801986,-4.077398,-1.079774,0.582363,-2.138575,3.164221,-0.260934,-8.604567,-6.535166,-1.565856,7.909849,9.083260,6.683334,3.812255,-6.232633,-4.620919,1.579048,-9.493912,4.021560,-0.410578,-2.000984,-9.179069,3.311458,-8.415977,8.889609,-9.318304,-7.253033,-6.691970,-4.012019,-5.239525,2.859898,7.572522,2.524283,3.775448,-0.393853,-8.406841,3.252247,1.553950,9.514832,5.579852,6.118100,5.852467,3.447304,8.133187,4.567109,-9.583528,-3.667576,-5.269076,7.768531,7.894497,5.718203,9.258080,-4.267621,-9.082434,-6.177401,2.009453,3.944988,3.014624,-7.499478,-9.032406,6.419960,-2.371758,3.080755,2.333208,-5.496133,-4.641036,3.852886,9.136652,-1.308715,6.015951,8.929305,-9.962737,-6.590934,4.061507,-7.154851,-1.920031,-1.813080,-8.105610,1.422178,6.240389,-6.830120,-9.260862,0.088344,9.646381,5.670984,-8.227940,1.683143,7.603408,-7.497363,-4.959144,6.408182,-2.489732,-8.041728,4.384507,6.827896,8.548986,-7.548902,6.331194,1.677433,3.314262,2.978297,1.599449,9.176924,-2.978464,7.249442,-1.870909,-3.289677,2.138119,8.907900,-9.640381,1.519890,-0.981361,6.146380,7.848201,5.577762,1.182248,-1.749535,5.342487,-6.660424,7.821687,0.207046,-4.895159,0.235912,-6.721216,-6.882053,1.507964,-0.004873,7.861018,7.657139,5.913157,7.567175,3.902233,8.129493,2.574926,3.991634,-6.615626,7.883676,-6.808713,-1.423639,3.395386,1.388175,-7.665379,9.637452,-3.939517,-4.305349,7.999019,-8.558596,8.223369,3.398035,3.279092,7.513524,8.400663,-4.984782,3.287702,-3.058835,1.108746,5.449261,-3.036933,0.755993,5.986055,-1.726533,-9.991750,-3.669595,-2.361272,-8.613356,-0.487235,1.012677,-2.934580,1.241584,-7.923188,4.800798,6.843475,7.119547,5.854336,-7.861683,-4.519582,0.592388,-3.805645,-0.356278,7.356999,-0.243492,4.182788,-7.375502,-3.227573,2.747369,5.301789,-6.487966,-6.782090,-7.785742,2.639456,-0.209431,1.945060,-4.386594,2.222492,9.117908,7.311467,-9.901813,0.202321,0.312209,-2.731004,9.011222,0.065269,0.742374,9.825246,7.334275,-2.474600,8.623757,3.769516,0.382225,-4.065494,7.421074,6.651738,-8.953652,-1.662089,-1.570198,3.437985,5.147607,7.209621,-9.670089,-5.567076,9.221285,9.185759,4.646527,-4.283946,-3.803596,2.725956,6.969659,8.239390,0.282380,4.131511,8.192013,6.320366,3.121751,4.179937,-3.220938,0.113996,-2.077598,-6.447261,3.581697,4.275841,3.648550,6.269930,0.665077,0.902202,1.550836,-9.969359,2.598375,6.907194,-4.648440,-6.218907,-0.477493,0.860057,-8.686466,-6.381204,-7.031839,1.581844,-6.145304,-8.982247,-1.241326,2.952775,-5.184740,-7.903001,4.344508,-3.472416,-7.183193,-9.713451,-0.144997,4.087379,5.877573,-7.232189,8.296716,-3.562349,1.988567,4.760287,-7.380237,8.416391,-3.989207,-3.419487,1.269879,-6.420349,6.711381,-4.300129,-0.570964,-5.789112,-4.920176,2.059117,5.655357,3.613023,7.445801,-3.232058,2.320469,-3.740321,0.532958,-3.289480,-1.088228,-3.825235,1.470685,1.134422,-4.008431,-2.884100,0.570165,2.704605,6.690795,7.517983,2.917813,-2.830077,3.930637,8.914885,7.210738,6.051475,-3.831577,2.267001,-1.036671,0.710628,-9.369445,4.181890,0.731119,-3.268196,-4.344110,3.266433,2.475189,-1.243880,1.175294,5.701267,4.591214,-2.525777,-9.407144,-0.912003,-2.187240,-7.724121,4.022243,-0.246353,-4.294649,1.490825,-9.414436,-3.661210,-7.037065,-7.559749,-1.327539,-5.282519,-6.631811,2.489017,-1.685181,-4.710420,5.823052,7.739483,-7.531481,-1.441463,8.223775,7.989963,-5.710662,7.617458,0.203745,-4.571859,-0.525144,9.588434,5.281491,4.038370,-6.870986,9.576593,-3.504420,-3.264764,-1.631362,7.555259,-8.793273,-5.473620], dtype = "float64")#candidate|7500|(1440,)|const|float64
const_7501 = relay.const([7.077592,-8.305712,-0.684435,3.548079,8.011947,9.250950,-9.890934,4.799668,-3.992450,7.832780,-6.324869,-6.727615,-0.526989,-2.126215,-0.213219,-9.673712,7.929963,7.987147,-9.700403,-0.717824,-0.168387,-0.744169,-9.999422,5.720495,3.670983,0.281167,-7.912215,7.592347,-6.352560,-9.077677,8.414664,4.027952,0.475206,6.346075,2.015803,7.269269,3.773466,-9.491268,-4.345773,-9.151090,-0.608224,4.967149,5.669559,0.216961,-3.544485,4.552295,-7.906754,8.989666,6.336965,-1.834558,-6.975081,-5.883001,6.036112,2.143117,8.221336,3.870098,9.759797,-4.529878,0.401374,1.255053,0.226706,-4.945641,0.780294,3.612010,-5.765995,2.376358,-5.375867,-6.159024,-2.550843,6.780417,-3.160301,0.886304,5.388150,-1.378950,-9.744210,5.929887,-0.191023,0.398286,1.735906,7.812648,-3.439497,-6.017551,-0.131681,-7.795420,-4.208161,-5.046875,7.854173,-0.555051,6.976830,3.010229,-0.938969,5.716021,-8.895426,-6.167990,-9.431327,9.681194,-5.764229,7.107535,1.505356,8.808719,7.417595,-8.219556,-3.683074,7.519648,0.923003,9.881610,9.379035,9.117263,2.365667,7.531983,3.779516,9.748146,-6.422093,-7.736014,-9.434460,3.976706,-9.208076,-5.851151,8.975278,-3.082172,2.358733,-5.098202,7.574517,-1.149114,-0.572310,-5.940846], dtype = "float32")#candidate|7501|(126,)|const|float32
call_7499 = relay.TupleGetItem(func_2517_call(relay.reshape(const_7500.astype('float64'), [12, 15, 8]), relay.reshape(const_7501.astype('float32'), [126,]), ), 3)
call_7502 = relay.TupleGetItem(func_2521_call(relay.reshape(const_7500.astype('float64'), [12, 15, 8]), relay.reshape(const_7501.astype('float32'), [126,]), ), 3)
func_3045_call = mod.get_global_var('func_3045')
func_3048_call = mutated_mod.get_global_var('func_3048')
const_7508 = relay.const([9.466502,2.557707,1.706420,-5.450112,9.176066,-2.944016,-0.138931,7.882578,-4.096798,-2.202879,-1.995093,1.193455,-1.458832,-1.625918,-9.843171,-6.736117,8.064205,2.401763,6.648438,0.766181,2.593719,-2.616301,8.448195,2.804002,-7.892612,-7.263193,6.847034,4.817592,-8.806069,0.789378,-0.124127,-5.344303,-6.582354,-1.446358,-7.276224,-8.374850,-4.854203,7.358137,-7.072780,7.512715,-4.651026,8.896235,-6.875654,0.240225,3.191420,1.964677,-0.836612,1.780493,-9.320658,-4.299137,-3.970665,-1.985318,-4.671928,-7.373634,-6.754816,1.059523,5.764392,-7.199016,1.037038,9.834600,0.625727,3.664831,-7.401824,-6.174383,-9.885729,2.957419,0.585778,9.435694,-1.110039,1.434605,-3.246447,3.255234], dtype = "float64")#candidate|7508|(72,)|const|float64
const_7509 = relay.const([10,3,-6,5,-5,-10,4,-8,-1,-4,-9,5,-4,5,-8,5,-4,2,-3,-9,7,-5,-7,9,1,6,-10,2,-5,2,-5,3,-7,-1,-3,1,10,-10,7,4,5,-10,3,8,10,1,-9,7,7,-8,-8,10,-3,4,2,-9,-10,-1,-2,-8,1,8,-4,-5,2,-3,10,-10,-6,4,4,6,-6,-8,-9,3,-8,9,-5,-2,10,1,1,-5,-8,6,2,-10,10,-7,4,9,10,-3,4,5,-3,4,-8,10,7,9,-9,-10,-7,-9,6,3,8,4,-3,6,5,-1,-10,-10,6,-8,8,-5,-4,6,-2,7,-8,2,10,-9,-1,-8,1,7,9,4,1,4,2,5,-10,-4,3,-2,-5,8,1,-6,-3,-4,10,2,7,-9,6,5,-8,6,6,-6,9,8,9,-6,8,-7,-8,-10,-4,4,-4,-10,7,-4,4,-5,-4,-6,-6,5,2,2,10,-7,-2,-6,1,9,-2,2,-4,2,7,-9,10,-8,-8,4,-6,-4,-3,7,6,1,-10,5,-7,2,-5,-10,-6,9,1,-4,6,7,10,-3,-1,-6,7,-7,-10,-2,-1,-10,-1,3,-4,-2,6,-2,-5,-5,-9,-7,4,-3,-2,-7,-7,10,-8,3,1,-2,5,3,9,6,9,-6,-7,7,-6,-2,3,-3,6,-3,-9,4,-1,4,7,9,3,-10,6,2,4,-5,8,8,-3,-1,-7,8,3,7,-2,-5,2,7,-3,-10,-5,-5,-2,-8,-5,-9,5,-8,9,-10,2,6,-1,3,-2,-2,-5,-9,-10,-6,-8,-7,2,3,3,-4,9,10,-3,-7,-4,-1,5,-10,8,2,-10,-1,6,-6,7,5,-10,-7,8,7,2,4,7,-6,9,3,9,-2,5,-4,-7,-10,4,9,3,7,-5,5,-5,9,9,3,-3,4,4,2,-7,-10,2,-4,-7,-10,-1,6,-8,-10,-4,-6,8,7,-8,-5,5,-7,-7,4,3,8,-1,-10,7,5,-2,2,-2,2,-10,-4,-2,-2,1,5,-9,8,7,-10,-7,-8,7,9,-9,-9,9,3,-4,2,-2,1,-10,-3,6,-3,-10,2,-3,7,3,2,-7,5,2,7,4,7,-7,-3,6,8,9,3,2,-3,-6,-8,9,-6,-1,-7,3,1,6,4,1,8,-1,-3,5,-9,10,5,1,10,-6,-8,-1,-10,-4,7,-4,7,-9,10,6,-4,7,4,3,-3,-1,10,10,6,-2,-1,-9,-4,9,-2,-3,9,-6,-1,9,9,-3,-1,-1,-6,2,-1,-6,-1,7,9,-2,2,-3,8,-5,1,8,-10,1,-1,-3,-5,-7,3,-2,6,1,1,-10,-6,-7,-4,1,3,-2,-6,-9,4,-9,-2,9,4,-7,-4,3,-6,8,-5,-6,2,5,2,9,1,-5,9,-4,-4,8,-10,9,-1,-7,-8,7,10,-10,-7,8,-6,-3,-7,-8,8,10,-6,5,9,-4,-3,-9,-2,-5,7,-6,-8,-10,6,7,-5,-3,7,-8,7,5,2,5,2,-2,-5,4,7,-8,1,8,-2,6,-6,8,-6,-5,7,-2,-2,-6,3,10,-3,5,-2,1,-4,5,-3,3,-6,-10,2,9,-8,-1,-6,-3,7,-4,-10,7,4,-4,-5,-8,9,3,2,3,1,-9,5,6,9,-3,7,-5,-3,7,7,-10,-3,-8,-7,5,7,4,7,3,2,-6,-7,-9,9,-8,-1,-3,-1,1,1,5,9,9,-9,-1,10,9,8,8,4,-6,-4,1,-1,5,-6,2,-10,-9,-3,10,-8,1,-7,-5,-4,-7,-3,6,-1,-6,1,-4,8,2,4,5,10,-9,-4,9,-7,-8,5,4,7,6,-9,1,-4,9,4,1,1,-3,4,4,-6,-4,8,-10,-8,-5,5,-6,-10,6,-8,-7,6,-3,2,4,2,1,-5,-7,7,2,9,-10,3,-2,-4,-2,-1,-1,-4,10,-4,-6,-4,-4,2,-7,-5,9,-5,-1,-9,9,9,2,-6,9,-5,-9,-5,-4,-10,-9,7,3,8,1,8,-7,10,2,2,-4,-4,8,7,-10,10,-1,7,9,1,-5,9,-8,3,-5,-9,4,3,5,-5,-8,-6,3,5,1,1,-5,-7,-1,2,7,-4,-7,4,-8,8,-3,-5,8,-10,5,4,-4,-4,-3,-9,-10,-1,2,2,4,4,-4,6,10,-2,7,-9,-7,6,-1,-2,9,-9,-1,-1,-9,-6,5,-9,-8,-1,7,10,3,5,2,-5,1,4,-3,8,-1,8,-6,2,-8,-3,-3,8,-8,1,2,-2,10,-6,-10,-6,9,-6,1,-1,1,3,-4,1,5,1,-6,2,-9,-10,3,2,1,6,-8,-10,-10,2,-5,-7,4,8,3,7,-8,-2,2,10,-4,7,3,10,2,9,-4,8,4,-8,-7,10,-2,4,-8,1,-3,3,-6,9,-6,5,-5,-8,2,10,2,5,-4,-2,-5,6,1,-6,-4,-7,5,10,9,-3,-5,8,-10,-5,-4,-9,-10,-9,-4,-10,-1,-9,-10,-6,-9,8,1,5,-1,-8,-7,-5,1,2,10,4,-10,8,3,9,-3,8,-6,-5,-1,-3,-9,-9,-4,-6,2,6,4,-2,-7,1,-9,-6,-9,-2,-6,-1,3,7,-1,-4,4,3,-5,7,5,6,6,-6,4,7,3,9,8,-7,-9,-1,2,-3,10,-1,-9,-8,-8,9,-2,-4,-4,3,6,-2,3,-2,-9,4,-6,-4,-1,-9,7,-10,4,-4,-4,-10,-8,-9,-8,-6,5,-6,-4,-7,3,1,-4,6,7,-6,-10,-3,-9,-9,-5,-3,4,5,-2,-10,-8,2,4,-2,2,1,-4,-10,1,9,-4,-8,4,4,-6,10,7,-10,1,-1,-9,5,-1,6,6,-7,10,9,-1,-1,-7,-4,2,-7,-5,-6,-3,8,7,5,1,-4,-9,4,-5,-10,-5,-9,8,10,6,-8,8,-2,-1,-10,1,1,6,4,2,6,-6,-2,2,-8,9,-9,3,6,8,-4,2,1,-3,-1,-8,-2,-3,1,-6,6,-6,-4,6,-2,-6,5,2,-5,-10,-1,5,-3,8,6,2,1,6,-6,7,-9,4,2,2,2,4,-10,-7,-7,-8,10,6,-7,-9,7,3,-1,-9,-3,-10,5,-2,-5,10,3,7,-8,-5,3,2,-9,5,-9,3,-7,1,-9,7,-2,-5,4,8,-3,9,-8,8,-5,9,1,-8,-5,10,-9,-7,3,6,4,-1,1,-6,2,-8,9,1,-9,8,-5,7,7,-7,-8,10,-10,-10,3,-10,10,-2,-5,-8,-1,8,7,1,1,-4,10,-10,5,1,-6,4,9,8,10,-8,-4,-8,2,-5,-7,10,3,10,-2,7,-2,-5,-9,-6,-10,-2,1,-5,9,-5,-9,4,7,-1,6,6,-8,-10,-5,-8,1,9,-7,-4,-6,-3,-6,-6,-2,1,-4,-6,1,1,-2,-2,8,4,8,4,-7,-9,-5,-5,4,4,4,-2,6,10,4,-1,-3,-10,1,5,2,-2,-10,1,-6,2,7,-4,9,10,-5,-6,4,-1,9,-6,9,7,6,5,-4,-3,-3,3,2,-3,-2,7,-4,-2,2,5,5,-3,1,6,-5,6,5,-9,-3,-2,-3,3,-5,2,3,1,1,-1,-3,10,6,-7,-7,6,9,5,6,9,2,-3,1,3,9,6,2,2,-4,-7,-3,1,2,6,-5,-1,8,-4,-9,3,-2,2,7,-4,-10,3,5,-7,-3,2,8,7,-9,-7,7,-8,10,-4,3,1,-8,-9,10,7,1,-1,7,4,-8,-6,-10,-3,8,9,-5,7,5,-6,3,8,7,2,-7,1,9,10,6,2,-3,5,3,3,5,-3,-7,2,-8,9,1,3,-9,-9,-8,-7,4,-1,4,-3,7,7,6,-7,4,-2,-8,-4,9,10,-6,10,-10,7,7,3,7,-10,-1,-7,-5,-9,3,-7,-9,-10,7,5,3,1,1,7,-4,-8,4,-2,-4,9,4,-2,7,8,-3,9,-4,-7,-4,2,9,-5,-7,1,7,1,-10,-6,4,-8,8,5,10,6,6,4,-10,-10,5,8,-5,-5,1,-9,5,2,-7,-5,8,-2,3,-4,4,-10,7,-3,9,7,-9,-5,-8,-10,-3,-3,-8,7,-9,-4,5,2,-4,-6,2,2,-2,6,3,4,-10,-9,9,10,7,1,-8,5,9,-4,5,-10,3,6,1,2,-6,-8,8,-3,3,-10,10,-2,9,7,4,-2,3,-10,7,-6,6,-7,3,1,7,-7,-7,5,-7,-1,-10,-5,-10,-9,-1,-9,10,-9,-10,-9,2,-4,-6,-6,-1,-3,9,-6,-5,5,4,10,3,-7,2,10,5,-4,2,4,-4,-4,5,1,7,-3,-3,4,-4,9,-10,-9,-2,4,2,5,4,-10,-9,6,-10,-8,-4,9,5,6,-8,10,10,3,-1,8,8,-4,-1,-7,-1,-4,-9,-5,-2,10,7,-1,4,-9,-2,2,-8,-1,9,10,4,7,8,10,4,-3,1,-10,-7,2,9,-1,10,-6,1,9,1,-1,-7,-10,-10,-3,-6,-6,5,2,3,9,-7,-4,-2,-4,-8,-1,-7,-7,-5,-9,-5,-3,4,4,-9,1,-9,-4,8,5,4,-3,8,-9,-2,5,-3,10,6,-5,9,10,-2,1,4,-8,-2,1,-10,-5,9,2,10,1,7,10,-3,4,-7,-7,-10,1,-7,2,-3,2,8,-5,-7,4,-2,10,7,1,10,4,5,10,10,-9,-8,6,-8,-4,-7,1,-5,5,6,5,-5,3,-8,2,-4,10,6,8,7,9,10,-3,10,8,-5,-9,4,10,5,-10,7,-3,-6,-4,-2,-6,2,9,9,-7,2,3,-10,-10,7,5,7,-4,8,-5,5,-5,3,1,3,4,-6,1,-2,-2,-8,2,7,-10,7,7,7,9,10,-1,7,-6,6,8,10,-8,9,6,9,-2,1,8,-3,-9,-8,6,8,8,-1,2,6,-10,2,-8,-1,-7,10,-2,4,-8,4,8,5,-9,-10,-10,3,-9,7,5,-10,2,-10,6,10,8,7,-9,10,3,-9,8,2,-4,-7,-6,-3,-10,7,-7,-10,-10,-9,-1,4,-2,-4,4,8,-4,-9,5,-3,3,10,4,4,-7,2,5,4,1,-6,6,5,10,-2,-3,9,-4,9,9,3,-8,5,-3,1,-7,-10,-4,2,-6,8,-1,9,-5,5,-2,1,-3,5,5,1,6,4,-6,-3,-5,4,-9,-3,-1,-10,7,5,8,-8,-6,5,-10,-2,-7,1,-8,-8,-7,-3,9,1,7,-6,6,7,2,-5,-1,3,4,10,8,-10,8,3,-9,3,-2,2,-4,-1,-1,1,5,-1,-7,-10,-10,-9,-4,-8,-1,-10,2,3,10,-2,-10,6,8,-4,-10,-9,-5,-1,-3,3,-9,-6,-6,9,-3,-9,-6,10,-2,-1,1,5,10,-4,-4,-6,-1,-6,-3,2,-5,-1,-6,5,5,2,-5,1,-10,10,-5,7,-1,2,-7,2,-5,-1,3,-9,-1,6,8,3,6,10,-10,-7,1,6,4,-7,10,10,-5,6,1,-4,-1,5,-4,9,3,6,-5,-1,2,-8,6,-10,8,-7,-7,-6,-1,10,-7,9,6,5,10,10,3,-6,5,-10,-9,-2,1,9,-8,-9,-7,-6,-6,4,-6,-9,2,8,1,-2,6,-1,1,-10,8,-5,-10,9,3,-3,10,8,9,-1,5,-1,7,-9,-1,-9,-10,7,7,-7,1,-9,-4,-3,6,-1,7,-3,3,5,5,-4,-10,5,7,8,-2,9,6,6,5,-3,1,-9,10,-10,-9,9,7,9,-8,2,-5,-7,-2,-3,2,1,5,-10,5,-9,-6,6,-6,9,-1,3,3,-7,3,-4,-9,10,5,9,10,6,10,-1,-6,-8,1,-5,3,9,-5,3,-8,-7,3,-4,-8,10,2,-2,-2,-9,6,-7,-9,5,1,-9,-2,-3,4,9,10,8,3,-4,4,7], dtype = "uint64")#candidate|7509|(2288,)|const|uint64
call_7507 = relay.TupleGetItem(func_3045_call(relay.reshape(const_7508.astype('float64'), [4, 3, 6]), relay.reshape(const_7509.astype('uint64'), [2288,]), ), 1)
call_7510 = relay.TupleGetItem(func_3048_call(relay.reshape(const_7508.astype('float64'), [4, 3, 6]), relay.reshape(const_7509.astype('uint64'), [2288,]), ), 1)
output = relay.Tuple([call_7493,call_7499,const_7500,const_7501,call_7507,const_7508,const_7509,])
output2 = relay.Tuple([call_7494,call_7502,const_7500,const_7501,call_7510,const_7508,const_7509,])
func_7516 = relay.Function([], output)
mod['func_7516'] = func_7516
mod = relay.transform.InferType()(mod)
output = func_7516()
func_7517 = relay.Function([], output)
mutated_mod['func_7517'] = func_7517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5137_call = mod.get_global_var('func_5137')
func_5138_call = mutated_mod.get_global_var('func_5138')
call_7533 = relay.TupleGetItem(func_5137_call(), 0)
call_7534 = relay.TupleGetItem(func_5138_call(), 0)
func_4638_call = mod.get_global_var('func_4638')
func_4643_call = mutated_mod.get_global_var('func_4643')
const_7536 = relay.const([-2,2,-5,5,-1,-2,-2,-3,4,9,9,1,3,7,-5,4,1,3,2,-3,8,5,-2,2,-4,9,3,7,-4,-7,-1,8,-8,2,-10,1,2,9,-6,-9,-2,-6,-10,10,-9,5,-10,4,6,8,-10,-4,-4,-6,4,1,-4,10,1,-10,-10,2,9,-10,1,1,-6,6,9,-10,-5,-8,7,-7,-1,1,-3,3,-9,7,10,3,-4,-4,9,8,5,5,6,-2,-8,-6,4,-2,-2,-4,8,6,4,-7,-4,-7,10,2,-3,-1,-5,-1,-8,-3,4,1,-3,-6,-9,-10,-9,-3,-8,-5,7,-1,4,-5,-2,3,6,-10,2,-7,-10,-5,5,-7,3,3,9,6,5,8,-10,5,-6,6,-10,9,2,-8,2,-2,-7,-6,-1,2,4,3,-10,9,-1,1,7,-1,6,8,5,4,6,-10,4,3,1,-1,2,4,4,7,7,-2,7,2,1,6,8,4,-10,-2,-3,-2,3,-10,-1,-8,-7,1,2,8,9,-3,-1,-3,-4,-4,7,3,1,-9,-2,-3,9,5,-9,-7,8,-7,8,2,4,10,9,3,9,-4,-9,2], dtype = "int16")#candidate|7536|(224,)|const|int16
const_7537 = relay.const([[1],[-7],[8],[7],[7],[8],[-3],[1],[2],[9],[-3],[-6],[-10],[-7],[-4],[-9],[4],[4],[-8],[-8],[10],[-4],[-7],[-10],[10],[-2],[-10],[10],[-1],[-10],[-2],[1],[-9],[-8],[9],[1],[-1],[4],[-2],[9],[-2],[7],[-1],[5],[-3],[-8],[4],[-3],[-6],[7],[8],[-5],[-2],[9],[3],[-6],[-10],[8],[-9],[3],[6],[9],[3],[-4],[-4],[4],[-8],[10],[-10],[-6],[8],[-8],[4],[-10],[-9],[-8],[-8],[-8],[10],[2],[2],[5],[7],[-1],[-4],[-9],[-8],[3],[-5],[8],[-7],[2],[5],[8],[1],[-9],[-8],[-2],[-10],[3],[8],[10],[-3],[10],[5],[-3],[-4],[10],[4],[-5],[8],[5],[-10],[10],[-9],[-8],[6],[-5],[-9],[6],[-4],[-8],[3],[-8],[-6],[9],[8],[-9],[-2],[8],[3],[-8],[-2],[-10],[9],[6],[-5],[10],[2],[5],[10],[1],[2],[6],[-2],[-3],[2],[6],[4],[6],[-1],[7],[-7],[-6],[-6],[7],[8],[5],[10],[2],[-8],[7],[-6],[-4],[8],[-6],[-4],[-9],[-1],[-10],[-7],[-4],[-6],[5],[-10],[10],[-1],[8],[9],[-10],[5],[7],[10],[-10],[2],[-9],[-8],[-4],[-1],[2],[5],[1],[-8],[-5],[-4],[5],[-2],[7],[-10],[-4],[-1],[-9],[-5],[-5],[3],[10],[-9],[8],[-2],[4],[8],[5],[2],[4],[1],[4],[9],[10],[8],[10],[3],[3],[-1],[-9],[4],[8],[3],[-3],[-5],[8],[-3],[7],[6],[5],[3],[9],[-5],[7],[-3],[-8],[-10],[-8],[2],[-7],[-6],[-5],[7],[-2],[1],[9],[1],[1],[-2],[2],[7],[-2],[-8],[9],[2],[7],[2],[1],[-3],[-2],[-8],[-10],[1],[-7],[-10],[-8],[-8],[-3],[1],[-6],[-9],[-4],[-2],[10],[-6],[10],[5],[5],[1],[-9],[-8],[9],[9],[4],[-3],[4],[-1],[3],[-3],[-1],[-5],[-5],[10],[6],[-9],[-2],[4],[-6],[-1],[-5],[-1],[10],[-9],[-7],[6],[-3],[8],[-1],[7],[10],[4],[6],[-1],[-3],[3],[1],[-6],[7],[-4],[10],[-4],[-10],[1],[3],[-3],[-6],[4],[9],[4],[-10],[-9],[-2],[9],[-2],[6],[2],[-5],[4],[-8],[-3],[-1],[7],[3],[-9],[-7],[6],[9],[5],[-9],[-3],[-9],[5],[-9],[-1],[8],[-7],[-5],[2],[-10],[4],[1],[7],[10],[-10],[-9],[4],[-5],[-3],[9],[-1],[-7],[4],[5],[-9],[1],[4],[5],[-4],[1],[6],[4],[-7],[8],[-5],[-3],[-4],[7],[10],[5],[6],[-3],[10],[2],[-5],[-5],[-5],[8],[9],[-4],[-4],[3],[5],[5],[-3],[-7],[8],[1],[-9],[9],[8],[-2],[4],[4],[9],[10],[-5],[1],[-4],[-9],[9],[-7],[-5],[-5],[1],[-8],[-10],[9],[4],[7],[-1],[7],[9],[-8],[-4],[-1],[-3],[10],[-5],[4],[-10],[5],[7],[-4],[-9],[-4],[-6],[-6],[9],[-8],[-1],[8],[7],[1],[2],[10],[-10],[-4],[8],[5],[6],[8],[2],[-9],[-10],[-6],[5],[-6],[-1],[-6],[4],[8],[8],[-8],[7],[6],[7],[-9],[9],[-2],[4],[1],[-3],[4],[6],[10],[6],[2],[10],[-2],[5],[2],[3],[-1],[-9],[1],[-2],[-5],[-1],[-2],[10],[5],[-9],[-10],[8],[6],[2],[-5],[9],[-7],[-2],[2],[-3],[10],[7],[-9],[3],[-5],[-2],[1],[-8],[5],[-7],[5],[8],[-6],[10],[-4],[-6],[-9],[8],[2],[-3],[-4],[-1],[-6],[4],[-9],[2],[8],[-7],[2],[-2],[-2],[-5],[-3],[-8],[-4],[3],[7],[5],[-5],[5],[-1],[-1],[8],[-3],[5],[1],[8],[-10],[-6],[-8],[-1],[-8],[-9],[4],[-3],[9],[5],[-3],[7],[-7],[5],[-2],[1],[4],[2],[10],[6],[-4],[3],[10],[-4],[-10],[-8],[3],[-2],[8],[8],[10],[3],[1],[-9],[9],[-10],[-2],[-8],[9],[-1],[2],[-3],[-5],[-9],[2],[-4],[-9],[8],[2],[-10],[5],[-5],[-3],[7],[-8],[2],[-8],[-7],[1],[7],[-3],[6],[7],[1],[-3],[2],[3],[3],[2],[-9],[-10],[10],[-7],[2],[-5],[9],[-7],[-10],[-3],[6],[4],[-4],[-5],[4],[-8],[-10],[3],[8],[-9],[7],[-1],[-1],[-5],[5],[-4],[4],[6],[6],[4],[1],[-2],[-2],[-10],[-6],[-3],[2],[1],[-4],[-4],[4],[7],[5],[-3],[-9],[2],[9],[-2],[8],[3],[1],[-9],[10],[6],[-8],[-3],[8],[8],[7],[8],[-8],[-7],[-4],[-10],[-1],[8],[-9],[-6],[-9],[-4],[-5],[-7],[9],[10],[-9],[-4],[-7],[-6],[10],[-3],[8],[-4],[10],[-5],[4],[-4],[-8],[-4],[8],[-5],[-10],[-6],[1],[-10],[-9],[-1],[-6],[-6],[-5],[-5],[-2],[-6],[2],[7],[3],[1],[-4],[2],[10],[-4],[5],[-9],[-10],[-7],[-6],[2],[3],[-8],[9],[9],[1],[5],[6],[9],[-9],[8],[-10],[-5],[10],[3],[-6],[3],[6],[-8],[-9],[7],[6],[3],[1],[-9],[-7],[-4],[-4],[5],[-3],[-9],[7],[2],[-5],[8],[-7],[4],[-9],[7],[-1],[10],[-5],[-2],[3],[2],[-10],[-7],[-7],[2],[-1],[-8],[5],[4],[-10],[-6],[9],[-10],[-8],[5],[2],[9],[10],[-2],[-7],[1],[-5],[6],[2],[6],[3],[5],[-5],[8],[9],[-7],[1],[-4],[-4],[-2],[-1],[8],[-1],[-5],[-6],[-6],[-4],[1],[-8],[-5],[4],[-8],[9],[-10],[10],[-5],[2],[-6],[10],[7],[-4],[-5],[4],[8],[-8],[-8],[6],[-7],[-8],[8],[-8],[9],[-6],[2],[-8],[-2],[-2],[3],[-6],[9],[-5],[-6],[3],[-5],[-2],[-8],[-4],[10],[-4],[6],[1],[-8],[-6],[10],[-3],[7],[6],[-8],[7],[-9],[-6],[9],[8],[10],[2],[-5],[5],[-8],[6],[4],[-7],[-9],[4],[-1],[1],[-2],[-10],[7],[-8],[9],[-4],[-5],[-10],[1],[-10],[-7],[-7],[9],[4],[-4],[3],[3],[5],[-1],[-8],[5],[9],[-4],[-2],[6],[1],[-9],[8],[2],[2],[-6],[-2],[-10],[1],[-1],[6],[-5],[-7],[-3],[-4],[-3],[2],[7],[-1],[-3],[-5],[-10],[10],[-5],[1],[-9],[4],[-1],[3],[-4],[-5],[-3],[-10],[-9],[1],[6],[3],[-4],[-5],[-3],[5],[-3],[-6],[-3],[-10],[-7],[5],[-2],[-2],[8],[4],[-9],[7],[7],[2],[-10],[2],[9],[-8],[10],[-1],[-3],[-8],[-1],[-9],[-4],[-10],[-10],[-10],[-1],[-7],[-1],[-4],[10],[3],[2],[-8],[10],[3],[6],[10],[-4],[7],[-1],[1],[9],[-5],[-10],[1],[3],[-1],[-9],[9],[4],[-1],[-3],[-2],[-3],[-9],[4],[-6],[-7],[-3],[10],[-6],[-9],[-7],[5],[-8],[-9],[9],[1],[-6],[-8],[9],[-4],[-5],[8],[9],[-2],[-10],[-3],[9],[-2],[-9],[5],[-2],[7],[3],[3],[-9],[8],[10],[-4],[3],[-6],[-8],[9],[-9],[4],[3],[-5],[-8],[-1],[10],[-4],[2],[7],[-8],[-3],[-10],[6],[-7],[7],[10],[-3],[-5],[-6],[-1],[-5],[-4],[3],[10],[8],[-2],[1],[-9],[2],[-5],[-2],[-4],[-8],[5],[1],[2],[10],[4],[-1],[-3],[2],[-9],[9],[-1],[-4],[2],[1],[-4],[3],[2],[7],[2],[1],[-1],[8],[-1],[-1],[-5],[-8],[1],[-5],[9],[7],[5],[-3],[7],[-3],[7],[3],[-4],[2],[-3],[-6],[3],[-5],[8],[-7],[5],[8],[-5],[-9],[1],[1],[5],[6],[7],[7],[-10],[10],[-10],[8],[-6],[3],[-1],[3],[4],[-8],[5],[-4],[5],[4],[-9],[4],[5],[-3],[-3],[-3],[7],[2],[8],[4],[9],[-10],[-1],[-9],[-6],[10],[3],[3],[10],[-4],[-10],[-1],[2],[-3],[-1],[6],[-10],[6],[-1],[-8],[7],[2],[-2],[7],[2],[4],[-8],[-9],[8],[-3],[-10],[1],[-5],[1],[-4],[-5],[-9],[-9],[2],[2],[9],[8],[-2],[-10],[-2],[9],[1],[-1],[-9],[-2],[-5],[3],[4],[4],[2],[-3],[-3],[8],[1],[-6],[-10],[4],[7],[6],[10],[-10],[-7],[-9],[-7],[-8],[-1],[7],[4],[-9],[-5],[8],[10],[-5],[-7],[-2],[2],[-4],[-4],[-1],[-7],[7],[-2],[10],[-4],[-2],[4],[4],[-10],[-10],[1],[8],[3],[-4],[6],[-10],[-4],[1],[-3],[-3],[1],[-6],[3],[-8],[1],[2],[9],[7],[3],[-1],[-5],[-5],[7],[-7],[8],[9],[-5],[-4],[-7],[1],[-8],[9],[-6],[-9],[8],[-1],[-10],[3],[10],[-10],[-10],[-8],[8],[-3],[-4],[-4],[-1],[10],[-1],[-8],[1],[-1],[-4],[2],[4],[2],[3],[-1],[4],[7],[-10],[10],[3],[-1],[-1],[3],[-6],[6],[-9],[-4],[10],[-9],[8],[5],[3],[9],[2],[7],[9],[2],[-4],[-5],[9],[10],[10],[1],[4],[3],[7],[3],[2],[5],[3],[-1],[-9],[4],[6],[-6],[1],[-3],[4],[10],[-1],[9],[3],[-7],[-5],[-8],[4],[1],[-10],[9],[-6],[-3],[2],[7],[9],[1],[2],[-7],[1],[-1],[8],[-3],[9],[-6],[-8],[-7],[9],[-1],[-7],[5],[8],[5],[6],[-9],[7],[3],[9],[10],[9],[7],[2],[-2],[-7],[1],[3],[-9],[2],[5],[7],[6],[3],[-1],[-3],[-10],[-8],[2],[4],[-10],[8],[2],[-7],[-6],[-6],[-8],[-4],[9],[2],[-10],[1],[-9],[-9],[-9],[-6],[-2],[10],[8],[7],[-8],[-3],[-6],[-1],[-4],[4],[-1],[-4],[-6],[-3],[5],[-3],[4],[3],[3],[-5],[10],[7],[7],[-10],[-2],[5],[-9],[-6],[-1],[9],[-8],[3],[8],[-5],[-5],[-9],[-10],[-3],[-4],[-8],[-7],[-4],[3],[9],[-10],[-9],[3],[-2],[9],[9],[8],[1],[6],[-5],[-8],[1],[-9],[2],[-4],[5],[1],[2],[-10],[-4],[-10],[5],[3],[-5],[3],[-9],[6],[-6],[4],[4],[-1],[2],[5],[-8],[8],[3],[7],[7],[-7],[8],[6],[-1],[-9],[5],[7],[1],[-10],[-1],[-7],[-1],[-1],[3],[4],[7],[-4],[-1],[4],[3],[9],[7],[9],[3],[1],[6],[3],[2],[-2],[3],[7],[-9],[-6],[-3],[2],[-6],[-4],[-6],[-10],[-4],[-3],[8],[-10],[3],[5],[9],[-7],[-5],[9],[-7],[-2],[2],[5],[10],[-7],[6],[-7],[-9],[5],[10],[-7],[2],[-9],[8],[4],[1],[-6],[1],[8],[-9],[-8],[-8],[-9],[3],[-6],[-4],[5],[-6],[-2],[4],[-10],[2],[-5],[9],[4],[2],[-3],[8],[-5],[6],[5],[-6],[-5],[-5],[-9],[-2],[4],[-6],[7],[-4],[-5],[3],[-7],[2],[2],[-5],[9],[7],[6],[-10],[1],[-5],[-6],[-3],[8],[3],[4],[-3],[-9],[-2],[4],[-9],[-1],[-6],[8],[-3],[2],[3],[-8],[-10],[-4],[10],[-3],[8],[8],[4],[-9],[5],[-1],[8],[-1],[-10],[6],[-10],[10],[1],[-4],[-1],[-3],[-6],[10],[1],[7],[1],[10],[-9],[10],[-1],[-5],[-3],[10],[-8],[-6],[-1],[7],[-8],[-9],[8],[8],[6],[-9],[-7],[6],[-5],[3],[-9],[-3],[-7],[-5],[8],[8],[-1],[-8],[3],[-8],[-1],[5],[8],[-10],[-6],[3],[5],[-2],[7],[-3],[-3],[10],[7],[3],[-3],[10],[2],[4],[9],[-2],[-6],[-10],[-3],[5],[10],[-4],[8],[7],[1],[7],[4],[9],[-3],[5],[8],[6],[-4],[-7],[9],[-6],[2],[1],[1],[7],[-1],[9],[-2],[-3],[-3],[8],[6],[5],[10],[-7],[-6],[7],[-1],[9],[-10],[8],[-9],[-9],[5],[-5],[-8],[10],[-6],[-6],[-9],[-5],[-3],[2],[-3],[-8],[7],[4],[-10],[6],[-5],[-4],[5],[9],[-8],[-10],[-5],[1],[-7],[2],[6],[-3],[-5],[-9],[-10],[-2],[10],[-7],[7],[6],[10],[-2],[1],[5],[-10],[10],[-8],[-1],[1],[-9],[6],[7],[-5],[-1],[-2],[-10],[5],[1],[9],[5],[-4],[7],[1],[-6],[7],[3],[-7],[9],[7],[-6],[9],[3],[-2],[-1],[10],[-10],[3],[8],[-3],[-6],[10],[-6],[-2],[-8],[-5],[9],[-10],[9],[9],[-3],[-7],[3],[8],[4],[6],[4],[1],[-2],[4],[-3],[-2],[-4],[-7],[6],[-2],[4],[2],[9],[-1],[-5],[-7],[2],[8],[-1],[1],[1],[8],[-8],[10],[-8],[-5],[-4],[-10],[-8],[10],[-7],[-2],[-2],[-2],[-1],[1],[-8],[9],[2],[4],[-4],[10],[7],[-2],[10],[-8],[-6],[-5],[-1],[5],[2],[5],[-5],[-10],[6],[6],[-2],[-9],[-8],[-5],[5],[-5],[-6],[-3],[-9],[-10],[-4],[-3],[-1],[-5],[6],[8],[-8],[8],[-10],[-4],[6],[5],[-10],[-8],[7],[-2],[-3],[2],[-9],[-1],[-10],[4],[8],[6],[4],[-2],[-9],[-10],[-7],[10],[6],[-7],[-8],[-1],[9],[1],[-2],[9],[-8],[7],[-5],[2],[-8],[-3],[-1],[-9],[4],[6],[-8],[-6],[-10],[6],[5],[-2],[-10],[-2],[-10],[7],[9],[4],[-2],[8],[10],[5],[-10],[5],[-1],[2],[6],[-6],[4],[1],[4],[-1],[7],[-4],[-8],[-4],[-4],[-8],[-3],[6],[4],[9],[-3],[8],[7],[-1],[-9],[-6],[8],[5],[10],[-6],[-10],[3],[-7],[-7],[-9],[5],[-1],[1],[-2],[9],[-7],[-8],[-2],[-10],[-4],[-9],[3],[10],[-2],[-3],[3],[-7],[10],[-2],[-2],[-6],[7],[3],[6],[-4],[-2],[-9],[-6],[6],[-5],[-9],[8],[-1],[-3],[3],[-6],[-4],[2],[2],[1],[-10],[-10],[9],[-7],[-2],[-6],[9],[6],[-2],[-4],[2],[-3],[-5],[-4],[-5],[-3],[-7],[4],[-7],[-10],[3],[9],[-10],[5],[3],[9],[1],[2],[9],[3],[2],[-8],[8],[-6],[7],[3],[4],[4],[-8],[7],[8],[7],[-2],[-5],[6],[6],[3],[6],[8],[-6],[9],[-6],[5],[6],[7],[-5],[1],[-6],[2],[3],[-9],[-5],[-3],[-4],[6],[-7],[-1],[-6],[3],[8],[-7],[-6],[-4],[9],[-6],[-3],[1],[7],[-10],[6],[-1],[10],[8],[-6],[10],[-2],[6],[3],[-2],[5],[5],[1],[5],[-2],[9],[10],[-3],[-1],[8],[3],[-3],[3],[2],[-9],[-10],[-10],[-2],[1],[-1],[4],[-10],[-1],[5],[-5],[9],[-1],[2],[-2],[-1],[9],[-7],[4],[-2],[-9],[-9],[4],[-7],[4],[6],[7],[9],[8],[3],[6],[-4],[3],[7],[-3],[6],[3],[-6],[3],[-1],[7],[6],[3],[-3],[7],[-2],[10],[-9],[9],[2],[-5],[7],[2],[-5],[7],[3],[1],[2],[-5],[6],[1],[-6],[-4],[-3],[10],[-7],[4],[5],[7],[2],[-3],[-10],[4],[-10],[-6],[-2],[4],[7],[-2],[-5],[6],[9],[5],[-5],[-1],[-6],[3],[3],[-7],[8],[-1],[10],[8],[-7],[8],[5],[1],[-3],[8],[-9],[-6],[-7],[1],[10],[-3],[1],[1],[-1],[-1],[-1],[8],[2],[-2],[10],[-4]], dtype = "uint64")#candidate|7537|(2288, 1)|const|uint64
var_7538 = relay.var("var_7538", dtype = "float64", shape = (60,))#candidate|7538|(60,)|var|float64
call_7535 = relay.TupleGetItem(func_4638_call(relay.reshape(const_7536.astype('int16'), [16, 14]), relay.reshape(const_7537.astype('uint64'), [2288,]), relay.reshape(var_7538.astype('float64'), [60,]), ), 4)
call_7539 = relay.TupleGetItem(func_4643_call(relay.reshape(const_7536.astype('int16'), [16, 14]), relay.reshape(const_7537.astype('uint64'), [2288,]), relay.reshape(var_7538.astype('float64'), [60,]), ), 4)
uop_7548 = relay.rsqrt(const_7537.astype('float32')) # shape=(2288, 1)
func_4886_call = mod.get_global_var('func_4886')
func_4888_call = mutated_mod.get_global_var('func_4888')
call_7550 = func_4886_call()
call_7551 = func_4886_call()
output = relay.Tuple([call_7533,call_7535,const_7536,var_7538,uop_7548,call_7550,])
output2 = relay.Tuple([call_7534,call_7539,const_7536,var_7538,uop_7548,call_7551,])
func_7553 = relay.Function([var_7538,], output)
mod['func_7553'] = func_7553
mod = relay.transform.InferType()(mod)
var_7554 = relay.var("var_7554", dtype = "float64", shape = (60,))#candidate|7554|(60,)|var|float64
output = func_7553(var_7554)
func_7555 = relay.Function([var_7554], output)
mutated_mod['func_7555'] = func_7555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6551_call = mod.get_global_var('func_6551')
func_6552_call = mutated_mod.get_global_var('func_6552')
call_7568 = relay.TupleGetItem(func_6551_call(), 1)
call_7569 = relay.TupleGetItem(func_6552_call(), 1)
output = relay.Tuple([call_7568,])
output2 = relay.Tuple([call_7569,])
func_7577 = relay.Function([], output)
mod['func_7577'] = func_7577
mod = relay.transform.InferType()(mod)
mutated_mod['func_7577'] = func_7577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7577_call = mutated_mod.get_global_var('func_7577')
call_7578 = func_7577_call()
output = call_7578
func_7579 = relay.Function([], output)
mutated_mod['func_7579'] = func_7579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6979_call = mod.get_global_var('func_6979')
func_6980_call = mutated_mod.get_global_var('func_6980')
call_7597 = relay.TupleGetItem(func_6979_call(), 0)
call_7598 = relay.TupleGetItem(func_6980_call(), 0)
output = call_7597
output2 = call_7598
func_7608 = relay.Function([], output)
mod['func_7608'] = func_7608
mod = relay.transform.InferType()(mod)
mutated_mod['func_7608'] = func_7608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7608_call = mutated_mod.get_global_var('func_7608')
call_7609 = func_7608_call()
output = call_7609
func_7610 = relay.Function([], output)
mutated_mod['func_7610'] = func_7610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6674_call = mod.get_global_var('func_6674')
func_6675_call = mutated_mod.get_global_var('func_6675')
call_7625 = relay.TupleGetItem(func_6674_call(), 0)
call_7626 = relay.TupleGetItem(func_6675_call(), 0)
func_6674_call = mod.get_global_var('func_6674')
func_6675_call = mutated_mod.get_global_var('func_6675')
call_7639 = relay.TupleGetItem(func_6674_call(), 0)
call_7640 = relay.TupleGetItem(func_6675_call(), 0)
func_6210_call = mod.get_global_var('func_6210')
func_6212_call = mutated_mod.get_global_var('func_6212')
call_7645 = relay.TupleGetItem(func_6210_call(), 0)
call_7646 = relay.TupleGetItem(func_6212_call(), 0)
output = relay.Tuple([call_7625,call_7639,call_7645,])
output2 = relay.Tuple([call_7626,call_7640,call_7646,])
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
func_4724_call = mod.get_global_var('func_4724')
func_4726_call = mutated_mod.get_global_var('func_4726')
call_7675 = relay.TupleGetItem(func_4724_call(), 0)
call_7676 = relay.TupleGetItem(func_4726_call(), 0)
func_5113_call = mod.get_global_var('func_5113')
func_5114_call = mutated_mod.get_global_var('func_5114')
call_7685 = func_5113_call()
call_7686 = func_5113_call()
func_7035_call = mod.get_global_var('func_7035')
func_7036_call = mutated_mod.get_global_var('func_7036')
call_7694 = relay.TupleGetItem(func_7035_call(), 0)
call_7695 = relay.TupleGetItem(func_7036_call(), 0)
output = relay.Tuple([call_7675,call_7685,call_7694,])
output2 = relay.Tuple([call_7676,call_7686,call_7695,])
func_7702 = relay.Function([], output)
mod['func_7702'] = func_7702
mod = relay.transform.InferType()(mod)
output = func_7702()
func_7703 = relay.Function([], output)
mutated_mod['func_7703'] = func_7703
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7516_call = mod.get_global_var('func_7516')
func_7517_call = mutated_mod.get_global_var('func_7517')
call_7732 = relay.TupleGetItem(func_7516_call(), 5)
call_7733 = relay.TupleGetItem(func_7517_call(), 5)
output = relay.Tuple([call_7732,])
output2 = relay.Tuple([call_7733,])
func_7735 = relay.Function([], output)
mod['func_7735'] = func_7735
mod = relay.transform.InferType()(mod)
output = func_7735()
func_7736 = relay.Function([], output)
mutated_mod['func_7736'] = func_7736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5695_call = mod.get_global_var('func_5695')
func_5697_call = mutated_mod.get_global_var('func_5697')
call_7768 = func_5695_call()
call_7769 = func_5695_call()
output = relay.Tuple([call_7768,])
output2 = relay.Tuple([call_7769,])
func_7783 = relay.Function([], output)
mod['func_7783'] = func_7783
mod = relay.transform.InferType()(mod)
output = func_7783()
func_7784 = relay.Function([], output)
mutated_mod['func_7784'] = func_7784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7608_call = mod.get_global_var('func_7608')
func_7610_call = mutated_mod.get_global_var('func_7610')
call_7793 = func_7608_call()
call_7794 = func_7608_call()
func_4838_call = mod.get_global_var('func_4838')
func_4840_call = mutated_mod.get_global_var('func_4840')
var_7823 = relay.var("var_7823", dtype = "float32", shape = (126,))#candidate|7823|(126,)|var|float32
call_7822 = relay.TupleGetItem(func_4838_call(relay.reshape(var_7823.astype('float32'), [126,])), 1)
call_7824 = relay.TupleGetItem(func_4840_call(relay.reshape(var_7823.astype('float32'), [126,])), 1)
func_5695_call = mod.get_global_var('func_5695')
func_5697_call = mutated_mod.get_global_var('func_5697')
call_7826 = func_5695_call()
call_7827 = func_5695_call()
output = relay.Tuple([call_7793,call_7822,var_7823,call_7826,])
output2 = relay.Tuple([call_7794,call_7824,var_7823,call_7827,])
func_7843 = relay.Function([var_7823,], output)
mod['func_7843'] = func_7843
mod = relay.transform.InferType()(mod)
var_7844 = relay.var("var_7844", dtype = "float32", shape = (126,))#candidate|7844|(126,)|var|float32
output = func_7843(var_7844)
func_7845 = relay.Function([var_7844], output)
mutated_mod['func_7845'] = func_7845
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7516_call = mod.get_global_var('func_7516')
func_7517_call = mutated_mod.get_global_var('func_7517')
call_7910 = relay.TupleGetItem(func_7516_call(), 0)
call_7911 = relay.TupleGetItem(func_7517_call(), 0)
func_6274_call = mod.get_global_var('func_6274')
func_6276_call = mutated_mod.get_global_var('func_6276')
const_7916 = relay.const([-8.773133,0.254224,-7.575665,-2.673722,-7.832407,5.401761,5.695675,-9.527145,-0.880403,-5.112617,-5.184568,6.271290,-6.940097,-9.245000,9.264793,0.343407,-5.903536,5.145099,-5.753441,8.787254,-9.335332,6.848912,7.265509,0.653157,-4.784759,-4.762959,4.746209,-3.985685,0.092231,6.838295,-4.898077,-0.399450,3.131043,-6.509251,-0.624795,2.380206,-5.442435,-3.444659,-6.045833,0.886534,7.639998,2.164267,-6.416075,-6.055650,-6.507937,-7.474326,-7.855464,7.455965,-7.246474,-4.837176,3.911180,7.862842,-8.295215,4.940038,4.863530,2.791329,9.737348,1.470591,-9.244476,2.385153,7.735013,-8.899830,1.815683,-4.032413,7.266244,-1.948246,-4.028341,-7.125280,3.566075,2.740545,-5.123925,6.605510,3.624038,9.351769,-3.224663,-7.932046,-0.867109,-8.401072,1.882311,-3.877492,8.843095,3.183403,-6.271554,-6.308523,-7.377859,7.905595,-8.900829,-1.644805,6.058558,9.912983,-4.138767,-8.087800,-9.238540,-1.549654,1.167061,-1.251575,6.715256,-2.203464,1.502474,1.738226,-3.654531,0.959816,6.808593,-3.804533,3.549405,2.114123,5.912481,2.182373,-0.006902,9.369240,-5.777098,-1.226400,-1.998174,6.300222,1.712749,0.230528,0.489809,-0.621334,-8.183172,-6.987398,-4.408129,0.708848,0.808932,-1.670074,4.528829,2.974779,2.729082,2.913036,-3.184294,-5.428237,-0.957199,4.271036,-2.873352,-9.529819,-2.030431,-2.736195,-1.900421,-3.987127,-4.724208,3.504012,4.189324,5.118613,-6.392570,-1.348679,-4.963521,-0.381637,-8.281258,-4.646580,1.846889,4.753562,4.287150,7.737083,9.406952,1.179036,-2.615524,8.776347,7.140749,-5.427193,-7.336563,-5.335909,3.174129,4.957077,-6.555063,-8.024558,-3.262788,4.866626,-0.021568,-7.564373,4.142607,2.575662,-1.966352,6.040304,-2.939782,-6.777514,-4.451343,4.407477,2.415799,1.372184,-4.100487,-1.921163,8.949030,0.313802,-4.399455,6.691727,6.082416,7.322602,-4.243969,-2.222485,-4.322583,5.959442,2.530980,7.333536,5.729044,3.580789,-0.810580,-1.724764,7.652306,3.268349,4.861426,8.722059,-1.960852,6.075095,7.185455,5.169680,-3.635955,-2.339628,4.657633,-7.531033,-0.291929,-1.206347,2.937131,-0.051025,-4.453064,-8.458847,2.292661,6.987001,-1.516518,-6.378178,-2.781273,-8.852491,-6.000797,-5.748592,-0.870304,-8.431182,-4.960076,7.752344,6.686063,7.734176,-2.090115,-5.555308,4.597643,4.374513,-8.002508,-1.520030,7.807724,3.560211,4.891921,9.649503,-6.328870,1.715502,-3.797572,7.596545,-2.829682,-4.664598,-4.204769,-7.643343,-0.847807,-2.922168,8.810958,7.532439,7.164136,-7.656064,-6.739645,-1.709946,8.296381,-0.814852,-0.565459,-7.089529,-5.737032,8.420138,2.402989,-7.115008,9.889858,-0.505615,8.566413,8.215849,-4.836435,-5.397787,6.851507,3.869202,-2.111038,7.194902,2.035474,3.083915,-8.143673,9.630487,7.242969,3.430189,-8.052495,3.655546,0.107357,-4.745604,7.132460,-0.048433,1.952220,6.562931,7.486997,-9.901968,-8.735721,-7.889631,8.269844,-3.155624,-8.267288,7.637976,5.457943,-1.039779,-9.989302,-9.721305,4.376634,-2.954266,9.494725,-6.342014,-6.927064,3.405952,2.356269,4.188291,5.550704,2.598636,9.773563,-3.546020,1.204345,5.135073,3.782214,0.388888,7.831204,1.958981,-3.666545,7.675079,3.019399,8.774132,8.502002,3.715951,1.306311,-1.464497,9.425864,9.195224,4.749947,-8.451638,0.443172,-5.323878,-0.487544,1.298521,8.595604,5.939830,7.849152,6.620416,-7.953314,-5.131572,3.452230,-8.665539,7.904149,-2.971501,4.383740,-8.705693,-1.094618,7.542410,-9.646278,7.013584,3.995687,-0.807984,-6.735861,7.144618,-3.648462,-3.247366,-1.063641,4.791547,-5.357011,9.626907,-6.342598,-6.690572,-4.152703,2.042716,-0.094648,-9.200839,-7.234061,0.542326,9.205646,2.560111,-6.954269,9.043532,-1.642002,-7.284431,-7.833815,-6.793768,5.607132,-9.101871,-7.263065,1.714807,-1.420487,4.249642,-5.767094,0.320756,8.184773,-1.339482,-0.095284,1.288217,-9.858653,-8.760843,1.489776,8.513380,2.427065,-6.412206,-4.245119,2.298145,9.650274,7.022875,1.489779,1.013588,6.988999,-9.366531,-0.595549,-6.378488,6.619110,6.134579,-6.184458,-4.137845,-9.967180,7.376699,-8.142216,-0.255303,8.723941,4.728173,-7.302119,-1.501539,-3.121850,-1.492487,-1.716576,1.494826,3.555550,-0.308961,-3.915040,1.130524,7.527290,3.472205,1.952815,5.685403,6.683789,3.879650,-7.849323,7.100171,-1.430069,7.269703,-8.707978,4.248153,7.209417,4.476747,-9.727364,5.751731,-8.080989,4.441144,-5.744296,-6.025637,1.201110,1.165628,1.295886,1.217018,-1.654704,-8.297780,2.085674,-5.512290,6.324436,-2.942864,5.415223,8.967128,-7.872954,5.032533,-0.759353,-1.451472,-0.922986,3.342221,-5.902573,2.611150,3.594224,-5.894704,8.150737,0.805366,-6.164697,-8.178274,6.543882,3.058761,-2.577252,-2.641938,8.711346,7.615685,0.108014,4.685078,5.768682,-0.177678,2.829608,5.347345,-7.556192,7.414076,5.328880,-9.010264,-0.674500,-2.272156,-3.723981,5.222562,-4.058895,8.516088,2.793409,7.332403,-1.332407,6.826542,-6.018879,-5.247765,5.498458,-7.647034,-5.577821,-5.156889,-5.137066,3.969471,8.463074,-1.661858,8.487965,7.653814,6.131538,7.341460,5.635667,6.324377,-4.857919,-4.127107,7.084715,-6.804689,2.665088,-9.300692,7.421857,-3.484655,-9.601901,-1.765385,1.471946,-5.747945,0.656023,-6.723880,-6.835798,-3.869177,3.694705,1.136124,4.247338,-3.038735,-4.721675,7.965571,4.136861,-3.162779,-3.933633,9.982790,4.866609,-9.656142,-3.689120,5.055716,-9.277991,8.268084,-6.732442,1.744870,-9.744345,-8.713968,-8.618349,-9.907970,1.288081,-0.938101,-2.870485,0.051672,1.920061,-1.461891,-4.671010,8.444358,3.957256,0.512975,6.615010,-4.794481,-9.271825,-9.845173,-2.055941,-9.381455,4.332237,6.636227,5.670355,2.627447,8.452638,-9.096984,3.997085,-2.718581,-1.830933,-1.327061,-1.013279,7.481467,0.741478,-5.440556,-1.397722,-4.082508,0.880555,1.783054,-1.919726,5.416568,-4.935792,-0.891473,6.637051,1.372152,-7.733679,6.971242,-3.453204,0.307593,-6.919132,0.687769,6.104645,2.431060,0.631347,5.952921,1.723045,0.422216,-2.120884,-5.131863,3.489702,4.841569,5.563967,-0.058509,1.287830,-4.906267,3.891467,-8.931134,8.989398,5.589954,3.106164,-8.852818,-6.585076,-7.349707,3.862530,-1.671097,-1.854740,-3.939959,8.550858,7.056969,1.777903,-9.994318,6.558305,6.266497,-0.532358,-9.888510,4.721276,0.612962,-2.825143,-8.018200,-3.094811,-6.534060,-1.181844,-1.279092,-5.960755,-3.909579,6.848867,-7.031799,5.667871,5.524779,3.078970,9.569806,2.092352,-1.743504,2.921206,4.329797,0.904077,-3.381543,1.671812,7.720425,6.262242,1.636759,9.361594,1.691660,0.700175,-7.098228,-3.657429,9.751110,-9.475682,-4.182475,-3.732435,3.992782,2.106233,6.375558,9.936315,-8.946923,-6.712179,4.041807,-8.302242,-8.027732,-4.754245,-5.960900,0.252511,-4.263182,7.040384,0.427806,-6.720217,7.726012,-8.024682,-5.399260,-2.538712,-3.642037,-0.379165,-6.803705,7.330317,-6.958837,7.358447,-3.328898,-9.962703,9.760654,5.207001,3.233203,1.157104,-5.839535,4.207117,6.726702,3.585434,-0.827138,-3.430372,-9.951913,-2.118726,5.575311,6.968378,-3.887213,-1.122097,0.862031,-3.917828,2.377470,-4.060031,0.756330,7.572411,6.360731,0.180438,-4.989414,-4.131779,4.280224,-2.988913,-4.276407,-1.396765,1.647042,-1.508315,3.294788,-2.294011,4.934163,-7.029462,-8.003316,4.979478,-9.648739,-0.837885,-3.262955,-1.889025,4.281723,-4.968856,-0.902084,-0.935756,9.677016,1.421521,7.369793,-8.180393,-0.947797,4.288097,-8.683930,-2.948553,4.197686,1.192295,6.969179,0.646075,-6.678325,-5.061520,4.189480,5.614346,-3.479371,8.992155,-1.541726,-8.518447,-1.091766,5.566372,-7.510047,6.413159,-2.614480,-4.343662,-6.790376,-4.313236,6.823660,-9.069169,3.081314,-1.760765,-0.335120,3.813637,3.606159,7.518446,-8.656706,-4.301976,-7.663846,-6.907201,-3.260918,-5.865831,0.431585,-0.801868,8.181777,6.009025,-2.704167,-0.894257,6.913161,1.388867,7.292216,-9.963372,1.590234,3.622075,-1.389246,3.628640,-4.673554,-9.379871,-4.018693,-7.469417,3.168396,6.604312,1.635929,-5.488956,6.787880,1.838971,-9.421713,-2.599380,-3.680873,3.404185,-3.564663,-5.562308,-1.855739,-8.921251,0.814049,-8.295189,-5.314397,-4.042114,-0.846974,-1.693524,-0.210479,-1.491562,7.630713,-3.241885,-5.592768,-1.011314,-4.974822,1.905434,0.099079,-7.718167,0.016664,2.919908,-2.677629,3.993205,-5.065999,-0.084376,-0.553237,9.942647,-3.923643,8.912178,0.294197,2.651189,-8.705047,-0.703577,-6.580419,-5.991990,-0.855143,5.616678,1.503464,3.259081,-4.339485,-7.966748,-3.789018,-3.262753,-4.449574,-1.730918,8.542999,4.251041,-6.995148,-8.496329,-7.974155,-6.394758,-5.344917,6.917619,6.946744,-8.155293,3.849952,-0.207618,-3.389346,-0.834257,-2.667432,8.622419,-2.437840,-9.040594,-6.077829,6.784610,9.064118,1.863503,4.726083,-7.917361,3.503154,-1.425910,4.083909,5.813901,6.190655,-4.085418,-1.740109,0.138325,0.373340,5.241565,-6.975401,-3.302929,2.938669,-1.446791,3.577750,3.381055,9.606540,3.425420,-2.800587,-3.049539,-6.736477,3.146415,-9.813998,9.485088,-7.331192,-0.298147,3.595134,2.208159,-6.177296,0.490331,-4.207115,6.353432,-0.380190,-6.619347,2.444812,-3.432227,-9.557684,-2.988560,-8.509340,-0.574359,-0.858228,-6.822331,0.473736,-6.512938,1.835351,2.745665,-7.987678,7.768329,1.480704,1.726221,-9.193328,-0.231278,-5.176757,-8.634299,-7.480137,4.472805,6.524156,-5.436348,2.717903,-6.717013,-6.477573,-9.545825,-3.989526,1.778959,-1.817645,-6.645305,-8.134414,9.588397,7.974310,-1.747460,-0.570304,5.072249,5.074427,-9.445263,-8.985918,2.533171,8.985730,-5.080916,9.002229,1.176108,-5.832675,-1.638059,3.586287,7.210983,9.700109,-1.666537,-8.400759,9.804212,-4.532773,-9.532928,8.750378,6.059255,-5.154390,-4.156196,-1.281185,3.860205,-9.292088,7.287599,4.468075,-8.228846,-0.151542,-4.570364,-2.682647,-1.425480,1.208984,-0.805591,-2.625999,3.960996,7.653760,-7.153220,-6.333567,-4.336382,-7.539589,-9.053353,2.188000,-6.750686,8.610475,-8.684411,9.003286,-2.537905,4.318852,3.743332,2.179128,-2.689006,-9.674686,-9.093216,-0.716373,4.184226,-3.545803,-2.180779,4.251435,-3.445341,5.191973,-8.445662,6.064033,-3.481633,5.551308,0.166638,-6.978150,5.765992,-4.686429,7.005726,8.412537,7.774332,-5.378463,2.208639,2.596797,7.070416,-0.592494,9.307096,-9.860547,-6.679195,9.328657,-0.551770,-2.598481,-9.803569,8.758037,0.285429,3.503392,8.366205,9.888392,9.188674,-8.972993,3.288495,-4.685406,-6.109275,-5.107416,6.001460,-6.115448,-3.264195,9.898193,-2.330856,-4.954425,0.268839,-3.888049,-6.058972,4.723037,-6.299384,-4.194178,-7.826871,-2.388765,3.153750,-8.876221,-3.784833,1.163176,7.928523,-8.295587,1.749245,4.667209,-5.454040,8.534891,5.797612,-0.564915,-9.918550,-8.137382,7.093055,-2.868478,8.994216,3.579188,3.619259,-7.424863,-8.976003,-7.601390,-3.884690,-2.828023,-0.920757,6.256357,6.024967,9.246980,-2.896354,-3.426248,2.405599,-6.169976,2.418585,-2.021810,-3.810771,9.407276,9.082831,3.139310,-8.156392,-3.673978,3.735057,-3.019766,3.989037,7.982350,9.074225,-4.858836,-0.583515,-4.256909,-4.706779,-4.302752,0.191327,8.351528,-5.560411,-3.587772,7.325639,7.050614,-1.302544,7.977875,2.195840,8.895071,-9.643701,3.827544,4.001094,1.183723,0.998150,-6.596934,7.544979,1.305880,-1.920284,-8.236622,7.806972,1.504298,-6.848489,0.755335,0.308549,-7.326732,-0.120575,-3.407508,1.796903,-4.029515,9.197461,-8.604223,-3.368299,-3.217286,1.888191,-0.672882,-2.877479,5.005653,-3.413185,2.211106,6.799114,-5.586906,4.514229,4.929629,-5.425811,9.326606,2.201049,-2.475295,-6.979818,-2.980575,-5.803862,-2.005661,-0.085102,4.837369,-6.484813,-8.488101,-8.858966,-2.809258,7.338233,8.639884,6.828910,-2.358035,-9.069701,-2.306234,4.254329,-3.499528,-8.093359,5.748011,-3.475006,1.460573,4.848891,0.798047,-5.748738,4.573469,4.432154,9.449899,-4.253428,6.534640,7.972608,9.744287,3.505230,-1.679331,-9.233640,-7.206988,-1.162202,1.319394,-6.112986,2.533417,-3.809812,-2.248535,9.744343,-3.390290,6.533871,-1.437779,-1.899185,-2.912666,-2.568889,3.410249,-2.012586,0.191643,2.948240,-7.209263,5.940184,1.880167,-6.247926,-0.917747,9.327778,7.679568,-8.761442,0.859839,2.184383,-5.306197,-2.774002,-3.084152,-7.193313,7.320362,4.949309,1.105306,-9.885431,-0.415743,-8.023380,-4.071700,-4.908558,4.976253,-4.979467,9.981286,-7.828019,4.909948,1.360732,5.468378,4.835460,8.061852,-7.831222,-8.036025,8.628986,4.199823,8.084741,-6.350346,-8.118261,-2.527132,-7.885512,-1.683612,-1.646645,-4.002398,-1.305067,9.671795,-1.924600,-8.475625,0.481450,1.147019,6.226200,-4.757361,7.721110,-9.260783,-3.286139,-1.464318,-0.863285,9.358329,-7.864992,-9.116086,9.243871,-5.665316,4.148982,-2.485007,2.022845,9.992471,3.855675,5.038408,-2.212805,-2.972820,2.248113,-3.874431,9.770044,-2.136746,9.109714,-5.512410,-4.927037,-0.720319,1.997433,-5.053176,0.624907,-2.103660,2.303960,2.703804,1.076608,8.249656,-8.252683,7.771583,3.616005,7.918024,-1.709888,-8.359095,-6.282447,-3.479094,0.873708,7.830253,9.240202,4.505442,8.161891,-3.267505,-9.170768,7.747999,1.956311,3.771800,-3.048419,1.579874,-6.086838,9.448481,9.443203,6.752907,-7.563877,6.283924,-9.681632,3.908153,8.213021,-4.416832,1.922205,-2.465316,-8.796305,7.737188,-9.495494,-4.493747,-7.625710,3.978531,1.357897,4.733291,0.960396,9.314818,0.976366,-6.222745,6.313661,7.004256,-8.868642,9.745456,0.191466,-5.243603,-9.675327,-3.591000,-7.589332,-5.142748,-9.465021,-8.034164,-3.099981,7.590195,-3.934444,-3.099944,1.973511,-1.527525,2.909937,-4.095662,-1.751815,-1.833395,4.805782,-8.723623,-5.141357,-3.675594,-3.184363,4.002544,-4.191087,-0.281527,-8.591748,-6.890834,-2.549282,6.858239,0.656534,-6.307133,-1.614203,-1.191013,-9.598210,-2.099593,3.065656,0.393371,4.402367,-6.114999,-4.927950,-2.195253,9.541831,-5.848435,5.515281,3.646746,3.857547,-9.168490,-8.162429,-3.131751,2.931024,4.923205,3.669696,-0.965639,0.061160,-6.812613,-1.491665,-8.398819,-5.958140,0.665537,8.888937,-3.816849,9.035687,-1.407233,5.892944,-1.170428,6.854135,4.733751,-3.772006,0.877330,-2.050321,5.153996,-1.101320,-9.643581,-5.358637,-2.892717,-6.616133,1.709238,-9.074913,0.912031,-5.886958,-9.145170,2.351102,-3.550913,-5.257134,-9.353412,0.687237,3.511862,4.405325,-6.617104,8.284805,1.425104,3.892935,5.968803,4.924731,0.893531,-1.582900,7.133447,3.662740,-0.365005,-4.065752,-3.646755,-7.129738,9.067986,4.043222,-9.649419,9.530256,-0.598362,-5.295977,-4.967666,-6.861013,4.292601,5.712432,1.572557,-4.282645,-5.319664,-7.237710,-2.572115,-7.980588,-2.859899,-3.819017,1.076778,7.135250,-7.045267,7.390761,6.809184,6.466839,9.919488,4.655902,2.908823,-8.643755,-8.641057,6.315600,8.071344,9.938198,5.446704,-9.542609,3.974017,2.971015,5.485163,-2.118629,-8.351656,8.357180,-9.531664,-0.648054,-4.442204,-0.346251,9.092999,-1.821682,6.122813,1.801950,5.397296,6.093119,3.647183,-4.937075,-4.394808,3.995644,-7.108817,-5.333750,0.983082,9.277128,3.008805,3.122994,1.661778,2.011081,8.772559,9.421901,2.763132,8.628635,8.139640,8.295087,-5.866708,9.229404,-6.741350,2.916242,-7.534882,2.534587,-4.552288,1.450906,-6.310477,4.471920,0.365597,-3.266406,9.547365,5.165466,-1.920380,-1.764987,2.991587,0.768599,3.469985,7.213788,7.292793,2.408050,3.147409,0.275752,-8.386513,9.388908,-2.236429,-5.126323,6.650676,-4.531488,-6.444886,-0.667602,-8.683506,2.578471,3.370357,-0.976728,-6.218137,-0.236235,-4.588464,8.904413,-6.373919,-6.085656,9.196680,3.520041,-8.869724,-2.070827,-4.300731,-2.861021,-7.774359,6.034897,-6.722034,9.302523,0.389759,1.638982,1.336731,-6.964593,9.282611,-3.333471,0.549495,-3.076280,-4.664693,6.358395,2.099983,0.711025,4.782306,9.852328,-0.504956,-5.340180,2.800641,6.696642,0.547841,-5.364120,-1.488682,6.088512,-6.462483,9.568226,-6.953460,-8.912881,-7.474887,1.778520,-9.170290,-6.743732,4.548834,-0.142982,-5.519384,-0.485262,-6.422247,-1.523747,0.984207,-7.196418,5.681014,-1.599481,-1.583430,-1.581039,8.159785,6.015985,-2.979312,-5.933574,-6.424102,-7.386042,9.730736,-2.201794,-0.598659,-6.160218,-0.046864,8.951288,2.268064,8.927929,-6.048643,-5.371546,-2.937582,8.500877,7.721147,-1.290687,8.414294,-7.100983,4.485109,-1.616678,-1.366784,-5.957827,3.746522,-2.541963,7.465640,2.508859,6.006580,6.013386,3.683482,1.405653,6.712094,-5.107239,-8.496766,7.425478,-0.020959,7.207957,-3.534821,7.665752,-3.211234,-4.059423,-8.891478,1.722553,-2.559557,6.055779,-5.253554,-7.613476,-1.427961,-0.378634,-3.654201,8.589634,7.899339,5.726659,-2.766155,0.941607,-8.324277,-7.695497,9.700993,4.060835,9.605320,1.132749,3.989902,0.256569,1.748814,-2.131104,8.736435,-5.050346,3.013633,-8.949949,-0.176274], dtype = "float64")#candidate|7916|(1680,)|const|float64
call_7915 = relay.TupleGetItem(func_6274_call(relay.reshape(const_7916.astype('float64'), [15, 8, 14])), 0)
call_7917 = relay.TupleGetItem(func_6276_call(relay.reshape(const_7916.astype('float64'), [15, 8, 14])), 0)
func_7702_call = mod.get_global_var('func_7702')
func_7703_call = mutated_mod.get_global_var('func_7703')
call_7962 = relay.TupleGetItem(func_7702_call(), 2)
call_7963 = relay.TupleGetItem(func_7703_call(), 2)
func_6700_call = mod.get_global_var('func_6700')
func_6702_call = mutated_mod.get_global_var('func_6702')
call_8009 = relay.TupleGetItem(func_6700_call(), 0)
call_8010 = relay.TupleGetItem(func_6702_call(), 0)
output = relay.Tuple([call_7910,call_7915,const_7916,call_7962,call_8009,])
output2 = relay.Tuple([call_7911,call_7917,const_7916,call_7963,call_8010,])
func_8019 = relay.Function([], output)
mod['func_8019'] = func_8019
mod = relay.transform.InferType()(mod)
mutated_mod['func_8019'] = func_8019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8019_call = mutated_mod.get_global_var('func_8019')
call_8020 = func_8019_call()
output = call_8020
func_8021 = relay.Function([], output)
mutated_mod['func_8021'] = func_8021
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5906_call = mod.get_global_var('func_5906')
func_5908_call = mutated_mod.get_global_var('func_5908')
call_8071 = relay.TupleGetItem(func_5906_call(), 0)
call_8072 = relay.TupleGetItem(func_5908_call(), 0)
var_8090 = relay.var("var_8090", dtype = "int16", shape = (16, 16, 16))#candidate|8090|(16, 16, 16)|var|int16
bop_8091 = relay.maximum(call_8071.astype('int16'), var_8090.astype('int16')) # shape=(16, 16, 16)
bop_8094 = relay.maximum(call_8072.astype('int16'), var_8090.astype('int16')) # shape=(16, 16, 16)
func_4963_call = mod.get_global_var('func_4963')
func_4965_call = mutated_mod.get_global_var('func_4965')
call_8095 = relay.TupleGetItem(func_4963_call(), 5)
call_8096 = relay.TupleGetItem(func_4965_call(), 5)
output = relay.Tuple([bop_8091,call_8095,])
output2 = relay.Tuple([bop_8094,call_8096,])
func_8111 = relay.Function([var_8090,], output)
mod['func_8111'] = func_8111
mod = relay.transform.InferType()(mod)
var_8112 = relay.var("var_8112", dtype = "int16", shape = (16, 16, 16))#candidate|8112|(16, 16, 16)|var|int16
output = func_8111(var_8112)
func_8113 = relay.Function([var_8112], output)
mutated_mod['func_8113'] = func_8113
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6125_call = mod.get_global_var('func_6125')
func_6126_call = mutated_mod.get_global_var('func_6126')
call_8152 = relay.TupleGetItem(func_6125_call(), 1)
call_8153 = relay.TupleGetItem(func_6126_call(), 1)
output = relay.Tuple([call_8152,])
output2 = relay.Tuple([call_8153,])
func_8232 = relay.Function([], output)
mod['func_8232'] = func_8232
mod = relay.transform.InferType()(mod)
output = func_8232()
func_8233 = relay.Function([], output)
mutated_mod['func_8233'] = func_8233
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8237 = relay.var("var_8237", dtype = "float64", shape = (8, 2, 5))#candidate|8237|(8, 2, 5)|var|float64
uop_8238 = relay.acosh(var_8237.astype('float64')) # shape=(8, 2, 5)
const_8240 = relay.const([[[-5.894766,-7.999621,5.168195,1.599607,-7.611919],[6.775932,-0.286036,-1.522874,3.518842,-9.412385]],[[4.006712,2.473025,-6.471866,2.564605,6.145561],[5.951396,-4.664893,-3.390448,7.635330,9.060581]],[[2.107518,8.623201,3.012552,6.127081,-1.769470],[-5.098012,-0.629812,7.544604,3.369262,-1.819219]],[[-0.312592,-4.917414,-7.328151,-5.441821,-5.648941],[5.499624,-9.794769,-2.217158,-0.155639,-3.415161]],[[8.029823,-3.210714,8.779588,2.010552,-8.466233],[3.401256,3.480494,-3.521221,-7.201857,8.587002]],[[-9.846654,3.969423,5.551876,2.770532,1.781669],[2.181592,-1.806880,-7.842903,8.292858,-8.421260]],[[9.912224,-7.207439,-4.315846,-4.097263,7.650396],[0.516240,-2.326418,2.617908,-3.365770,3.176180]],[[-9.235689,2.969211,-0.223641,-1.065751,5.727466],[-7.194061,0.612180,0.223077,5.718565,-1.089325]]], dtype = "float64")#candidate|8240|(8, 2, 5)|const|float64
bop_8241 = relay.floor_mod(uop_8238.astype('float32'), relay.reshape(const_8240.astype('float32'), relay.shape_of(uop_8238))) # shape=(8, 2, 5)
func_6050_call = mod.get_global_var('func_6050')
func_6053_call = mutated_mod.get_global_var('func_6053')
const_8257 = relay.const([-9.100703,-6.144452,-7.675674,6.055837,4.788389,2.315129,-7.834131,-1.490999,0.628229,1.525034,9.848643,-3.246208,-6.177026,-6.789910,7.730156,-9.844782,-6.612713,-8.018225,5.561566,-3.591268,9.321555,-3.287879,-1.997724,5.905695,8.082756,-8.566325,-5.394404,4.834831,-9.383480,-8.382534,7.553207,9.181132,7.333964,1.147429,6.341167,5.783490,3.148951,8.638333,-6.217792,1.544929,5.899752,-7.398488,-2.013805,-3.895704,-9.477564,-5.135067,1.037539,9.026183,9.267784,-7.174451,-1.079389,-4.177079,5.987850,1.738620,-0.216688,-6.822395,-8.581458,3.595681,-5.746257,6.023333,-9.835700,3.902336,5.371264,-2.629359,6.539393,-3.879100,1.445085,0.774210,-6.525915,-2.860820,1.789484,-1.287637,-4.073280,-3.273088,-4.151688,5.781587,-9.867340,-4.462816,2.580750,-9.289031,7.667375,-3.599738,0.092834,-0.150415,4.243395,-4.256976,1.041603,-9.318608,-9.104376,-5.503915,0.804919,9.842949,-6.971084,7.772763,8.541926,-5.619468,-9.346887,7.045014,-3.392893,8.977317,-1.002522,-0.386659,5.079600,1.241813,-1.481084,-7.015174,0.659844,9.151617,0.791641,2.356942,-3.437013,-9.391832,3.651901,3.394223,3.801762,9.404998,-1.981443,0.267972,-8.164978,-2.047150,-7.616873,-1.119937,-2.275470,-2.647215,1.379847,-3.266753,0.628754,-3.275795,-2.382054,4.862341,8.920703,-8.945445,-4.905412,4.278336,-5.264349,7.439528,-7.752323,0.685691,2.372931,-6.040845,0.078598,6.476905,3.565200,2.562505,9.750317,8.734116,9.794946,-6.047924,1.463415,8.460997,8.415790,2.872965,-4.319295,0.454936,-7.199252,-6.296954,-8.564056,-0.259388,-1.503203,-7.678650,-8.446797,-1.516300,0.077989,-8.726185,-8.402827,-5.441464,-4.807813,3.169048,-8.746000,9.784116,-1.205752,6.960546,0.994926,0.202268,1.907026,5.265938,4.911978,-6.177391,-9.573050,-9.823742,-1.629930,1.569813,-8.264034,4.165736,5.198455,1.283468,0.313385,-2.679997,-2.580938,-1.121361,7.445882,-2.733321,9.300373,6.788384,7.168793,-1.820247,0.257866,-4.972636,-4.006704,-2.758384,-2.790330,0.534851,-2.788198,-2.554367,5.114319,8.488758,-1.687015,-3.079806,-2.105348,-8.580879,2.274598,9.879727,-0.609239,-7.418572,3.346674,-8.905404,-8.662924,8.902725,8.141330,6.604662,-6.016003,-1.420911,-9.039949,-3.176973,-6.143338,-0.462154,0.887109,-0.131770,-6.796022,-4.196838,-1.241759,2.136996,3.782198,5.498383,9.672376,5.144595,5.005449,-8.962536,-4.428218,-0.451545,0.137212,-8.738612,-8.949141,-1.363877,5.181283,7.766926,8.333734,-6.136718,4.072260,-7.640709,5.044454,3.154321,9.134480,-4.909625,-4.243149,-1.613094,-1.923827,3.157413,-6.740619,8.033154,-2.142807,7.762443,1.434548,-1.357573,5.559449,2.791644,9.995601,-4.947880,4.513203,-6.165835], dtype = "float32")#candidate|8257|(270,)|const|float32
call_8256 = relay.TupleGetItem(func_6050_call(relay.reshape(const_8257.astype('float32'), [9, 5, 6])), 2)
call_8258 = relay.TupleGetItem(func_6053_call(relay.reshape(const_8257.astype('float32'), [9, 5, 6])), 2)
uop_8260 = relay.asin(uop_8238.astype('float32')) # shape=(8, 2, 5)
output = relay.Tuple([bop_8241,call_8256,const_8257,uop_8260,])
output2 = relay.Tuple([bop_8241,call_8258,const_8257,uop_8260,])
func_8265 = relay.Function([var_8237,], output)
mod['func_8265'] = func_8265
mod = relay.transform.InferType()(mod)
mutated_mod['func_8265'] = func_8265
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8266 = relay.var("var_8266", dtype = "float64", shape = (8, 2, 5))#candidate|8266|(8, 2, 5)|var|float64
func_8265_call = mutated_mod.get_global_var('func_8265')
call_8267 = func_8265_call(var_8266)
output = call_8267
func_8268 = relay.Function([var_8266], output)
mutated_mod['func_8268'] = func_8268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6700_call = mod.get_global_var('func_6700')
func_6702_call = mutated_mod.get_global_var('func_6702')
call_8276 = relay.TupleGetItem(func_6700_call(), 0)
call_8277 = relay.TupleGetItem(func_6702_call(), 0)
output = call_8276
output2 = call_8277
func_8293 = relay.Function([], output)
mod['func_8293'] = func_8293
mod = relay.transform.InferType()(mod)
output = func_8293()
func_8294 = relay.Function([], output)
mutated_mod['func_8294'] = func_8294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7299_call = mod.get_global_var('func_7299')
func_7301_call = mutated_mod.get_global_var('func_7301')
call_8312 = relay.TupleGetItem(func_7299_call(), 2)
call_8313 = relay.TupleGetItem(func_7301_call(), 2)
output = call_8312
output2 = call_8313
func_8321 = relay.Function([], output)
mod['func_8321'] = func_8321
mod = relay.transform.InferType()(mod)
output = func_8321()
func_8322 = relay.Function([], output)
mutated_mod['func_8322'] = func_8322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5191_call = mod.get_global_var('func_5191')
func_5192_call = mutated_mod.get_global_var('func_5192')
call_8358 = relay.TupleGetItem(func_5191_call(), 0)
call_8359 = relay.TupleGetItem(func_5192_call(), 0)
output = relay.Tuple([call_8358,])
output2 = relay.Tuple([call_8359,])
func_8369 = relay.Function([], output)
mod['func_8369'] = func_8369
mod = relay.transform.InferType()(mod)
output = func_8369()
func_8370 = relay.Function([], output)
mutated_mod['func_8370'] = func_8370
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6551_call = mod.get_global_var('func_6551')
func_6552_call = mutated_mod.get_global_var('func_6552')
call_8417 = relay.TupleGetItem(func_6551_call(), 0)
call_8418 = relay.TupleGetItem(func_6552_call(), 0)
func_3717_call = mod.get_global_var('func_3717')
func_3720_call = mutated_mod.get_global_var('func_3720')
const_8425 = relay.const([[-5,-2,3,-7,-3,-2,-4,-4,-6,9,-1,1,-3,1],[2,-8,6,-5,-1,-10,5,3,-4,-10,-2,-6,-2,-1],[9,-8,7,1,-5,-2,1,3,1,7,-3,-6,10,9],[8,6,2,-10,9,2,-8,-10,-4,6,9,3,-4,10],[-10,3,-9,-7,4,-1,9,-7,-8,7,-2,-9,10,-4],[10,6,2,-10,-10,-1,-4,-7,6,1,5,-7,-3,-7],[-8,-5,4,10,3,-5,5,-9,-10,4,-4,-1,-3,3],[5,-6,10,3,7,10,-3,6,2,-9,-4,2,7,7],[4,-3,2,3,-5,6,2,-3,-2,5,4,8,-8,-8],[-6,3,6,8,-7,10,1,-3,3,-10,-5,-8,-10,7],[-9,-10,-1,-4,1,5,-6,10,-10,-10,1,5,-6,4],[-1,1,9,4,6,-7,3,5,-6,7,-9,8,-9,-7],[7,-1,4,6,-3,3,10,6,-1,-5,5,-2,10,-6],[2,6,-7,-8,8,6,6,-3,-1,-2,-10,-9,8,9],[9,9,-3,3,-1,-2,-4,-2,-10,-9,-6,3,-7,-8],[4,-4,-7,6,-9,9,-9,1,-1,-6,-10,6,-5,1],[-1,-10,8,-8,9,4,-5,10,-6,-1,-5,-2,1,2],[-6,1,-10,4,7,3,-8,-5,-10,8,5,-2,6,7],[9,7,-10,3,-9,10,-1,-5,-9,-3,-5,-4,-2,-3],[10,8,-7,5,5,-9,-6,-2,1,-5,8,-1,9,-7],[10,1,-10,-9,6,-8,3,5,6,6,7,-10,-9,9],[-6,9,6,6,-9,-7,-1,5,-10,-3,10,-6,1,1],[8,-6,-4,-10,4,-8,-3,7,-8,7,-5,-6,10,-1],[9,8,9,2,10,-8,10,-9,-1,-6,-3,8,-3,-10],[-8,1,2,-9,-5,6,2,4,-10,-4,3,1,-5,1],[-5,1,3,-5,3,-8,2,8,10,8,6,10,-6,-3],[-1,-8,-9,-2,-5,7,-8,8,1,-7,-7,8,9,-3],[2,-5,-2,9,-6,-4,-7,-8,-8,-6,2,7,-8,-5],[6,3,3,8,5,-5,-8,1,-1,-10,-5,5,2,9],[8,9,1,9,4,-9,7,-9,2,2,-8,2,1,-1],[9,2,-5,9,-7,-9,-10,-9,2,-3,9,-8,8,-10],[-7,-1,-2,-4,-6,-4,5,-3,2,1,-9,8,10,4],[-8,-6,-5,3,-1,-6,-2,-9,4,10,-3,9,5,-1],[7,-2,10,-4,-8,4,-4,6,3,-2,7,-4,-5,4],[2,5,-1,-8,9,-7,7,-4,-4,-6,8,-5,-2,-7],[1,8,-7,5,-4,-10,-5,9,10,4,6,2,-9,-8],[3,-1,7,10,-4,3,-9,10,1,7,-5,-7,2,4],[8,4,9,6,7,-1,2,-9,-10,5,10,-5,3,-3],[-3,6,-1,3,-8,-6,-6,5,3,-8,-5,-4,-5,10],[-1,2,-10,-7,3,-10,10,7,5,5,6,-10,-8,-7],[-3,10,-8,10,-3,10,9,-6,-6,-7,4,8,9,2],[2,8,-4,1,-3,3,-10,-1,-3,-7,9,-1,-10,-5],[-6,-6,-8,-6,-5,8,10,3,4,-8,-10,-9,1,-5],[8,-9,9,-5,-2,-1,9,-4,-1,-8,8,4,-1,8],[-3,-2,-3,5,8,10,2,6,3,8,-6,10,2,-3],[-7,4,6,-10,9,-2,5,9,-7,7,-7,-5,3,9],[9,6,-5,-5,6,-1,-1,6,-8,3,9,5,-7,9],[6,-3,9,3,2,6,-3,5,-9,10,-5,3,3,2],[-8,9,-10,-1,4,5,-1,-3,6,-8,10,-2,-3,9],[-3,-7,3,-7,10,1,1,9,-5,-6,-4,-5,4,-9],[4,-6,-10,-2,-1,-3,-6,-5,8,-8,-8,-3,-9,-7],[8,2,6,3,-3,7,3,-4,-6,-5,-5,-7,-5,7],[1,-9,-10,4,-8,-9,9,6,-8,10,-1,8,8,-3],[8,-9,4,1,-8,9,10,-1,-6,1,-7,-9,8,8],[-5,-2,-1,-5,10,8,-8,6,-4,9,1,-5,-2,1],[-4,-7,2,-3,10,-5,-1,-8,9,-1,10,3,1,-4],[-4,5,3,-6,-1,7,6,-4,6,-8,-8,8,-8,-1],[-10,-3,9,-10,-2,-9,-5,8,8,-8,6,9,-4,1],[-9,2,7,-4,3,-9,10,10,4,-9,-10,7,5,-7],[5,3,-10,3,-10,4,-1,-10,2,-8,-6,9,6,-1],[3,1,5,2,-9,-5,-4,-4,-3,-7,2,3,4,5],[9,-2,3,-2,9,6,-1,-9,-1,9,5,10,1,7],[-5,-9,8,9,-7,10,5,6,-6,-10,-7,-10,4,2],[-5,-5,3,7,5,5,-6,-8,2,6,8,-6,6,-9],[-7,-10,-4,-5,8,10,-7,-5,-1,-4,6,2,8,9],[5,-4,1,-7,8,-3,1,8,-10,10,6,4,-6,6],[-4,5,4,-4,-3,1,-2,-6,8,2,6,7,8,4],[10,5,6,5,-1,-5,9,-6,10,3,-7,-4,-7,-7],[-4,8,-2,10,-4,5,4,-8,10,6,-5,6,6,-6],[-2,-9,-5,-10,9,-2,5,-6,1,-3,-9,9,-2,7],[6,10,-8,6,-5,8,-6,-6,-8,-1,-10,10,-5,-3],[-5,-4,6,10,-2,-5,3,-10,-4,10,-3,-2,7,-2],[8,-9,8,5,7,5,-2,-6,-4,3,-7,1,-6,-2],[-3,-5,-2,6,-8,-1,6,6,-8,4,1,1,2,7],[-3,3,5,-8,4,6,-5,-9,-7,-1,-7,9,2,-5],[10,-6,-3,10,9,-7,-10,-7,4,-7,10,5,3,-7],[-4,3,4,-8,8,-9,3,-8,-2,1,-10,6,6,-1],[-5,-8,-1,-4,10,-6,-1,-3,-2,9,-7,-10,9,-1],[7,-8,10,-5,6,-8,3,-3,8,9,1,1,-8,-9],[7,6,1,10,7,-4,3,9,3,-10,-2,-8,7,-10],[-2,-4,8,5,-3,3,-8,-4,7,9,-7,-3,-6,-1],[2,-9,-2,-3,4,-2,-3,-8,-9,4,-8,-8,-1,-4],[-3,1,-8,-10,-5,3,-3,8,-9,6,9,-6,2,1],[-6,-2,4,4,4,-4,-1,2,-3,1,-9,10,7,-6],[-1,-4,-6,7,10,1,9,6,-4,3,9,9,-1,7],[-6,-10,-1,-7,-1,-6,8,-6,5,-7,8,-6,6,-6],[-6,-8,7,-9,-2,-3,1,-5,-7,5,3,-10,-4,2],[6,8,3,2,3,6,10,-10,1,9,8,-1,-6,4],[9,-1,-3,7,-4,-6,2,2,-3,2,-8,3,7,-9],[-5,4,-8,-1,3,-9,-6,-1,8,2,-6,9,-7,3],[6,-6,4,7,4,-5,5,-3,-10,1,8,3,-10,-1],[5,-9,-6,2,-7,-10,-8,-10,-10,5,-7,-1,-2,2],[-7,8,-7,-2,4,-10,4,5,-8,4,8,-9,-8,2],[3,1,-9,3,-6,8,1,-2,-10,9,-10,6,-4,4],[3,1,2,-9,9,-6,7,4,1,-4,-10,9,-8,1],[7,-4,-3,-10,7,5,-9,2,2,3,1,-4,-10,5],[7,-10,1,-7,-10,-9,-6,6,3,1,-5,1,-4,1],[10,-2,1,-1,7,-7,5,-8,8,8,4,-1,6,5],[8,1,-1,3,6,-4,-2,-4,7,-1,5,-8,-9,-8],[-10,-4,-8,-4,-10,8,-3,-1,-5,5,6,-7,-3,2],[4,6,2,2,-7,-6,5,2,-10,4,-7,-7,5,6],[1,-2,9,-8,-10,-10,9,3,-3,2,10,-7,7,2],[10,-1,-9,5,-3,-8,5,9,5,8,6,9,7,5],[-2,7,-8,-2,-1,4,1,-6,-9,10,6,-1,-9,-8],[-8,10,1,-3,-6,-5,-1,-3,-10,-1,-4,4,1,2],[-8,4,-5,-8,-4,7,-6,-10,-1,3,10,4,-5,3],[6,5,6,-3,-6,9,-4,3,-1,10,6,5,7,1],[8,7,-9,-1,2,8,-5,-1,3,8,6,6,-1,-7],[10,10,2,-5,10,6,8,-3,8,3,-7,-7,-8,5],[6,8,2,8,-5,-2,9,-10,-1,1,6,-3,4,8],[-5,-3,-8,8,9,3,9,1,-5,-4,-6,6,-10,7],[-10,-7,-9,-7,3,7,1,8,-7,-7,-1,-9,-7,-9],[5,-10,10,-2,-8,-7,4,5,-6,-7,-1,5,7,-9],[10,-1,3,-2,9,-5,4,-9,8,6,-6,-8,7,-1],[7,9,9,2,1,6,-7,8,2,10,3,5,10,8],[-7,2,-2,-3,10,2,1,-1,10,-10,9,4,5,-1],[3,2,10,-7,-6,-3,8,-8,-7,7,-10,-2,4,-1],[5,6,3,1,-6,8,-1,-8,8,7,-7,-5,-9,8],[-2,6,2,9,-2,9,-9,9,9,8,-3,5,9,-9],[-6,4,9,-5,-2,6,-5,3,3,-5,-9,-10,-9,-6],[-6,7,-3,7,-8,3,-9,5,6,-9,2,-1,-8,-7],[7,-5,8,2,2,-3,4,-2,5,-6,-9,-9,-8,4],[-3,-2,4,-3,9,4,-9,-4,5,7,-7,-2,-7,-7],[-1,-2,4,5,1,-8,5,4,1,6,-5,-7,-5,7],[9,-10,7,-7,8,-8,-1,-3,-10,-10,-4,8,-1,-10],[-3,-2,-2,-5,6,9,3,7,6,10,-7,-7,-1,10],[10,-10,-6,-9,7,-9,-7,1,6,6,5,7,8,-3],[-9,-1,-3,-5,-5,9,-10,9,5,-1,-5,4,-5,-2],[-5,2,-7,6,-5,-9,7,4,-4,-9,10,-1,-7,7],[-6,-2,5,6,8,2,-4,6,8,-1,3,-3,-9,2],[-3,-5,9,1,-5,7,-10,-9,-1,8,-6,-4,-10,-4],[5,-5,4,-7,-1,-8,-7,10,-4,-4,5,-6,2,10],[1,2,-9,-4,1,7,-2,-8,9,-8,10,-10,5,-4],[10,-2,-7,6,-3,10,-4,8,1,6,-6,5,-10,9],[-2,6,-8,-10,-5,2,7,-4,8,-8,5,-10,-2,-7],[9,10,10,3,6,-4,2,-9,-7,-1,-2,-7,-4,-2],[-2,-1,-6,4,8,-5,-1,-3,4,-1,4,5,2,5],[-8,4,-5,-3,-7,8,-2,-10,-1,-7,5,-5,1,-5],[3,-1,-6,-1,4,-3,-10,-6,3,7,-9,10,-4,2],[-6,-2,-8,9,10,6,-5,4,-9,8,-8,-9,-1,2]], dtype = "uint16")#candidate|8425|(140, 14)|const|uint16
call_8424 = relay.TupleGetItem(func_3717_call(relay.reshape(const_8425.astype('uint16'), [14, 10, 14])), 0)
call_8426 = relay.TupleGetItem(func_3720_call(relay.reshape(const_8425.astype('uint16'), [14, 10, 14])), 0)
bop_8428 = relay.bitwise_xor(call_8424.astype('int16'), relay.reshape(const_8425.astype('int16'), relay.shape_of(call_8424))) # shape=(14, 10, 14)
bop_8431 = relay.bitwise_xor(call_8426.astype('int16'), relay.reshape(const_8425.astype('int16'), relay.shape_of(call_8426))) # shape=(14, 10, 14)
output = relay.Tuple([call_8417,bop_8428,])
output2 = relay.Tuple([call_8418,bop_8431,])
func_8438 = relay.Function([], output)
mod['func_8438'] = func_8438
mod = relay.transform.InferType()(mod)
output = func_8438()
func_8439 = relay.Function([], output)
mutated_mod['func_8439'] = func_8439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4758_call = mod.get_global_var('func_4758')
func_4759_call = mutated_mod.get_global_var('func_4759')
call_8557 = func_4758_call()
call_8558 = func_4758_call()
func_3045_call = mod.get_global_var('func_3045')
func_3048_call = mutated_mod.get_global_var('func_3048')
var_8565 = relay.var("var_8565", dtype = "float64", shape = (72, 1))#candidate|8565|(72, 1)|var|float64
var_8566 = relay.var("var_8566", dtype = "uint64", shape = (2288,))#candidate|8566|(2288,)|var|uint64
call_8564 = relay.TupleGetItem(func_3045_call(relay.reshape(var_8565.astype('float64'), [4, 3, 6]), relay.reshape(var_8566.astype('uint64'), [2288,]), ), 2)
call_8567 = relay.TupleGetItem(func_3048_call(relay.reshape(var_8565.astype('float64'), [4, 3, 6]), relay.reshape(var_8566.astype('uint64'), [2288,]), ), 2)
output = relay.Tuple([call_8557,call_8564,var_8565,var_8566,])
output2 = relay.Tuple([call_8558,call_8567,var_8565,var_8566,])
func_8612 = relay.Function([var_8565,var_8566,], output)
mod['func_8612'] = func_8612
mod = relay.transform.InferType()(mod)
mutated_mod['func_8612'] = func_8612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8612_call = mutated_mod.get_global_var('func_8612')
var_8614 = relay.var("var_8614", dtype = "float64", shape = (72, 1))#candidate|8614|(72, 1)|var|float64
var_8615 = relay.var("var_8615", dtype = "uint64", shape = (2288,))#candidate|8615|(2288,)|var|uint64
call_8613 = func_8612_call(var_8614,var_8615,)
output = call_8613
func_8616 = relay.Function([var_8614,var_8615,], output)
mutated_mod['func_8616'] = func_8616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7659_call = mod.get_global_var('func_7659')
func_7661_call = mutated_mod.get_global_var('func_7661')
call_8648 = relay.TupleGetItem(func_7659_call(), 1)
call_8649 = relay.TupleGetItem(func_7661_call(), 1)
output = call_8648
output2 = call_8649
func_8657 = relay.Function([], output)
mod['func_8657'] = func_8657
mod = relay.transform.InferType()(mod)
output = func_8657()
func_8658 = relay.Function([], output)
mutated_mod['func_8658'] = func_8658
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7608_call = mod.get_global_var('func_7608')
func_7610_call = mutated_mod.get_global_var('func_7610')
call_8674 = func_7608_call()
call_8675 = func_7608_call()
func_7702_call = mod.get_global_var('func_7702')
func_7703_call = mutated_mod.get_global_var('func_7703')
call_8706 = relay.TupleGetItem(func_7702_call(), 1)
call_8707 = relay.TupleGetItem(func_7703_call(), 1)
func_6330_call = mod.get_global_var('func_6330')
func_6332_call = mutated_mod.get_global_var('func_6332')
call_8708 = relay.TupleGetItem(func_6330_call(), 4)
call_8709 = relay.TupleGetItem(func_6332_call(), 4)
output = relay.Tuple([call_8674,call_8706,call_8708,])
output2 = relay.Tuple([call_8675,call_8707,call_8709,])
func_8712 = relay.Function([], output)
mod['func_8712'] = func_8712
mod = relay.transform.InferType()(mod)
output = func_8712()
func_8713 = relay.Function([], output)
mutated_mod['func_8713'] = func_8713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8712_call = mod.get_global_var('func_8712')
func_8713_call = mutated_mod.get_global_var('func_8713')
call_8745 = relay.TupleGetItem(func_8712_call(), 1)
call_8746 = relay.TupleGetItem(func_8713_call(), 1)
output = relay.Tuple([call_8745,])
output2 = relay.Tuple([call_8746,])
func_8754 = relay.Function([], output)
mod['func_8754'] = func_8754
mod = relay.transform.InferType()(mod)
mutated_mod['func_8754'] = func_8754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8754_call = mutated_mod.get_global_var('func_8754')
call_8755 = func_8754_call()
output = call_8755
func_8756 = relay.Function([], output)
mutated_mod['func_8756'] = func_8756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4886_call = mod.get_global_var('func_4886')
func_4888_call = mutated_mod.get_global_var('func_4888')
call_8760 = func_4886_call()
call_8761 = func_4886_call()
func_7440_call = mod.get_global_var('func_7440')
func_7442_call = mutated_mod.get_global_var('func_7442')
call_8770 = func_7440_call()
call_8771 = func_7440_call()
uop_8772 = relay.log2(call_8770.astype('float32')) # shape=(7, 2, 5)
uop_8774 = relay.log2(call_8771.astype('float32')) # shape=(7, 2, 5)
output = relay.Tuple([call_8760,uop_8772,])
output2 = relay.Tuple([call_8761,uop_8774,])
func_8776 = relay.Function([], output)
mod['func_8776'] = func_8776
mod = relay.transform.InferType()(mod)
mutated_mod['func_8776'] = func_8776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8776_call = mutated_mod.get_global_var('func_8776')
call_8777 = func_8776_call()
output = call_8777
func_8778 = relay.Function([], output)
mutated_mod['func_8778'] = func_8778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7067_call = mod.get_global_var('func_7067')
func_7069_call = mutated_mod.get_global_var('func_7069')
call_8881 = relay.TupleGetItem(func_7067_call(), 1)
call_8882 = relay.TupleGetItem(func_7069_call(), 1)
output = call_8881
output2 = call_8882
func_8894 = relay.Function([], output)
mod['func_8894'] = func_8894
mod = relay.transform.InferType()(mod)
output = func_8894()
func_8895 = relay.Function([], output)
mutated_mod['func_8895'] = func_8895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7735_call = mod.get_global_var('func_7735')
func_7736_call = mutated_mod.get_global_var('func_7736')
call_8938 = relay.TupleGetItem(func_7735_call(), 0)
call_8939 = relay.TupleGetItem(func_7736_call(), 0)
func_4602_call = mod.get_global_var('func_4602')
func_4606_call = mutated_mod.get_global_var('func_4606')
var_8953 = relay.var("var_8953", dtype = "int8", shape = (378,))#candidate|8953|(378,)|var|int8
call_8952 = func_4602_call(relay.reshape(var_8953.astype('int8'), [14, 3, 9]), relay.reshape(var_8953.astype('int8'), [14, 3, 9]), )
call_8954 = func_4602_call(relay.reshape(var_8953.astype('int8'), [14, 3, 9]), relay.reshape(var_8953.astype('int8'), [14, 3, 9]), )
func_6674_call = mod.get_global_var('func_6674')
func_6675_call = mutated_mod.get_global_var('func_6675')
call_8994 = relay.TupleGetItem(func_6674_call(), 0)
call_8995 = relay.TupleGetItem(func_6675_call(), 0)
func_7067_call = mod.get_global_var('func_7067')
func_7069_call = mutated_mod.get_global_var('func_7069')
call_8999 = relay.TupleGetItem(func_7067_call(), 0)
call_9000 = relay.TupleGetItem(func_7069_call(), 0)
const_9001 = relay.const([10,-4,9,4,-1,1,-5,3,5,4,-6,9,8,-5,4,-6,4,-3,2,-6,10,4,-6,3,2,1,8,3,-9,9,-10,10,-5,-7,-2,-1,2,-10,-2,-2,-2,-4,2,-8,-8,6,2,-2,-9,-7,5,5,-3,8,10,2,2,6,-5,-4,-1,-1,-6,-3,3,10,-10,-5,-2,10,4,5,10,-9,6,-8,-6,4,-1,1,-9,-3,-5,-1,3,10,5,-3,-7,-2,10,9,-8,-1,10,-4,-2,7,5,-4,-9,-6,-10,-1,-3,-9,10,8,3,-8,1,3,9,9,-7,-4,7,-3,7,3,5,-3,-2,-5,-10,9,7,3,3,1,6,6,-3,2,3,2,-1,-4,-5,9,4,-7,1,4,-5,-4,2,6,-1,9,-8,-1,-5,-2,-4,8,-9,6,6,-4,8,-3,9,6,-10,3,6,-4,7,-3,-7,10,7,-5,-9,-5,-8,5,-8,7,-8,5,-4,-4,5,3,-10,9,10,-2,5,-4,-6,2,2,1,10,3,-4,-5,6,-2,-3,-4,7,10,3,-4,-6,10,-8,9,6,-1,9,-9,8,-1,-4,-3,-3,2,-8,-3,-5,-4,6,10,-5,2,9,-1,5,-7,1,10,3,-7,10,-7,5,-5,-5,4,-6,-4,-10,-1,10,-5,-7,2,7,-5,9,10,-3,6,-10,8,7,-10,-8,9,10,-7,-9,9,8,4,5,-3,1,-6,8,-6,7,-9,8,3,3,4,-10,-9,6,8,-9,10,8,10,10,-10,-3,-2,-8,8,-8,5,-7,8,10,-7,-7,-9,-2,3,-5,1,-4,9,-9,-5,-3,-4,-7,-6,-10,-7,9,-4,-5,5,3,-9,8,-1,7,5,-8,-10,3,3,-8,-2,6,-8,-4,2,8,6,-1,6,-3,-10,1,-6,-6,10,1,3,-8,10,-5,-1,6,-2,4,-9,-8,-8,8,3,-4,10,-5,-3,-3,8,5,-2,9,-10,-9,-10,7,-7,-3,-9], dtype = "int8")#candidate|9001|(378,)|const|int8
bop_9002 = relay.logical_and(var_8953.astype('bool'), relay.reshape(const_9001.astype('bool'), relay.shape_of(var_8953))) # shape=(378,)
output = relay.Tuple([call_8938,call_8952,call_8994,call_8999,bop_9002,])
output2 = relay.Tuple([call_8939,call_8954,call_8995,call_9000,bop_9002,])
func_9012 = relay.Function([var_8953,], output)
mod['func_9012'] = func_9012
mod = relay.transform.InferType()(mod)
mutated_mod['func_9012'] = func_9012
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9013 = relay.var("var_9013", dtype = "int8", shape = (378,))#candidate|9013|(378,)|var|int8
func_9012_call = mutated_mod.get_global_var('func_9012')
call_9014 = func_9012_call(var_9013)
output = call_9014
func_9015 = relay.Function([var_9013], output)
mutated_mod['func_9015'] = func_9015
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9062 = relay.const([[[-0.381416,-6.141716,7.866456,6.199753,1.750714,4.014171,-0.192316,-3.385177,-0.153394,-7.867329,-4.917342,0.777496],[6.306777,-3.486996,4.359499,1.145359,-3.038603,6.170455,2.309868,5.679148,5.969618,8.483601,0.624344,-6.614947],[-7.816010,-3.595443,-9.011685,-8.752947,9.390089,8.007796,-9.677173,8.416530,-9.473232,-6.870286,9.085718,9.258951],[3.206050,-7.104949,-5.603973,-9.885327,-4.437289,5.374755,-5.320347,-8.255210,-2.679183,-5.154392,-2.764731,-2.392376],[-4.317657,-3.784962,-3.884974,-7.828648,-3.870251,0.479010,-4.726375,-4.387103,-0.317187,2.069341,5.940649,-4.010093],[1.467608,-0.731622,-1.217653,9.401335,-9.512596,-2.029544,6.774751,-3.356510,-8.340696,-4.232612,5.474051,7.250406]],[[-6.245649,-3.366940,-1.046630,1.309977,4.026542,0.749438,-3.842176,9.916369,7.804807,-2.483286,-9.370011,-9.794717],[-1.996319,4.201414,3.482929,9.663312,1.448522,7.672601,-1.912320,-8.807112,9.435995,-3.877102,-5.822960,-1.930740],[4.457875,-3.628689,9.426739,-1.870053,9.315842,1.601315,-6.781868,-0.538656,-0.600945,7.149098,-5.991278,-2.019638],[-5.286293,-0.429259,-7.112818,-5.200996,4.222279,-5.038016,5.148172,-6.572959,-7.727034,-0.069978,-3.462512,5.568056],[-8.629149,0.013195,-0.692118,-3.003650,-8.183716,4.412708,9.783732,3.791799,-6.155089,7.209361,-9.250698,-4.142608],[4.689457,-1.632242,8.292328,-5.254175,-5.852629,-0.395390,-4.677306,0.304671,4.581903,5.645012,-3.514959,8.621702]],[[-5.322741,1.385519,-5.314301,-6.941434,-9.514637,5.050819,-1.507190,5.573540,-7.383856,5.354276,4.575757,2.129531],[8.858945,7.429111,1.919377,-1.866105,-2.846238,3.288379,0.723718,-3.867708,-1.891443,8.709265,-5.015755,9.943364],[-8.368877,6.495986,-0.866306,2.362964,7.429635,2.894096,6.903876,5.524851,3.806760,2.868319,-5.624756,-4.306999],[4.703482,7.758839,9.620225,-9.066039,8.680904,9.410437,6.456780,8.106246,6.108327,8.977183,-9.906778,-5.772362],[6.277919,-0.740570,-3.410996,-0.741814,-9.372797,9.208568,5.480878,3.012653,0.957734,-9.359681,4.332666,0.108179],[-3.722870,-1.521677,4.140905,9.552598,-8.566600,-2.971013,-0.524380,-4.508960,-4.776761,-5.114111,-2.501036,-5.768323]],[[-1.477061,-2.338341,-9.241623,2.356616,-7.264912,4.007919,-2.051845,7.826219,-4.755056,3.662223,-4.214138,3.285061],[6.611895,-9.651294,-2.447279,3.985967,0.204972,-0.740667,-6.444045,5.025957,8.002325,-0.884451,3.545833,-3.981583],[-3.486061,-3.809755,-7.945401,9.281609,-5.377668,4.833041,2.250754,0.661853,-8.476547,-9.602320,4.954215,5.956883],[3.706597,6.023717,4.318044,-0.334406,7.149439,6.519991,1.300602,-3.944879,-9.103028,-2.785803,-1.476645,3.223411],[1.247908,5.263955,0.459158,-6.434935,3.966327,7.587598,5.968300,-8.386595,-2.937552,-8.072270,-0.712192,3.963012],[-7.044148,-9.109354,-7.346774,1.002120,-4.856974,-7.301346,-4.490958,-6.061430,-4.196015,-4.716825,3.721858,6.544103]],[[-8.024790,0.782799,-3.320958,-2.791012,-6.274443,9.257094,-7.713576,1.249322,-1.780221,-8.999651,-2.525242,-8.908888],[-0.522475,-5.417379,3.826818,9.360023,-4.510865,-0.017097,-2.158201,4.627203,-0.748886,0.293388,-3.522906,5.070011],[-3.502560,8.773350,-2.183692,-2.170054,-6.453951,-7.425386,-9.071900,-5.990088,2.510777,3.133254,2.708927,-0.670836],[7.466205,-3.249795,-9.513304,-2.098141,3.271816,9.721500,0.180786,-7.506584,8.495128,7.886377,-9.958453,-5.173869],[8.612305,4.514708,-1.159677,-2.744334,5.500451,2.636101,-3.008962,8.291458,4.755965,7.665201,-4.111399,6.392201],[-8.660575,3.481772,-1.975020,-8.547077,2.131609,-5.587796,-3.895428,6.670843,6.644606,6.619051,5.984589,2.898490]],[[-3.613917,6.252078,-1.658420,-7.678862,-8.026882,9.712536,9.579538,-9.564722,-6.305260,-9.129993,9.995087,-3.446085],[1.644550,-6.828455,-6.518375,7.987376,-1.859644,6.513685,3.257081,9.283829,2.268258,-0.827017,6.270442,7.435480],[3.907158,-2.425817,-5.126747,1.246314,-4.935770,-7.276722,0.638965,1.426519,-2.815880,-3.605499,-1.882187,6.176846],[4.776301,-5.075984,-3.212454,-9.872711,-9.692194,-9.451546,1.404176,-8.388932,3.294707,2.395379,-2.883534,-1.653673],[2.875232,8.245260,9.419258,-0.383701,-0.427762,6.824665,-6.797890,6.053774,-4.976942,4.290080,9.375667,3.713381],[-6.719318,-8.356334,-1.688010,-4.628064,3.836436,8.515791,-4.072510,2.603094,2.676215,-3.034712,-2.643471,-2.287292]],[[3.581977,9.179808,3.442975,-3.406218,6.642818,-4.018855,0.636540,9.327199,-1.828041,7.574315,-1.470486,-2.870017],[8.918152,-2.015924,-7.687869,-5.506762,-4.647601,-8.524026,0.142021,-1.747408,2.832122,-3.296744,2.358507,-5.567981],[-0.731532,-8.972547,-6.394581,-6.766071,2.429771,-2.403615,1.922227,-4.281844,-3.829709,9.028178,2.879678,-2.670512],[3.842373,9.403665,-0.118286,-1.038723,-5.010305,-7.813765,7.460260,-7.691900,5.096087,-8.026556,-2.867779,-1.168992],[-2.358384,-9.772269,5.923890,-0.115055,5.511184,0.226337,6.570639,-3.518756,8.582203,3.229393,-8.947731,0.036684],[-2.862589,-9.374165,-4.124599,6.108516,7.336752,-9.873541,-4.767331,3.314579,4.552028,3.646410,-8.007895,-9.598694]],[[-0.582138,9.234074,3.333952,-0.195495,-5.815589,-9.063512,-4.522424,7.772354,5.803687,-6.001199,4.406884,1.767190],[3.440115,9.029421,4.075044,7.647412,4.391509,-9.013447,9.040979,-5.690114,0.473495,0.598450,-3.396859,8.951088],[-5.791030,7.702660,5.946919,-2.435104,-1.836799,1.579245,5.694571,0.219131,8.211908,-0.342514,7.860207,-2.699526],[6.064233,-1.932773,7.102896,-9.897993,5.968471,1.712717,-4.331828,0.698998,5.481390,-1.901015,1.566977,-2.526863],[0.018374,-8.045858,3.820860,-2.961818,-7.812599,1.807638,-4.703345,4.221889,3.975233,7.039569,4.014268,-0.632533],[3.638297,0.049061,7.524575,3.968335,-3.051717,6.648364,-4.860346,8.952370,-5.316024,-8.731699,-9.235111,-2.453504]]], dtype = "float64")#candidate|9062|(8, 6, 12)|const|float64
uop_9063 = relay.cosh(const_9062.astype('float64')) # shape=(8, 6, 12)
func_7476_call = mod.get_global_var('func_7476')
func_7480_call = mutated_mod.get_global_var('func_7480')
const_9066 = relay.const(-9, dtype = "uint8")#candidate|9066|()|const|uint8
const_9067 = relay.const([[2,-4,10,-8,-2,-2,-10,6,4,9,-3,1,8,7,8,9,-9,-8,10,-3,2,7,2,2,-5,3,7,5,-4,7,4,-1,9,-2,-7,3,-4,3,-4,-3,5,-7,8,8,-6,1,1,3,-1,-10,3,8,-6,3,-6,-10,-2,3,-9,-9,6,-5,4,-6,6,-3,-1,-6,2,6,-8,8,3,8,-2,7,1,-4,1,-9,-8,-5,3,-6,1,-4,-10,8,4,5]], dtype = "uint8")#candidate|9067|(1, 90)|const|uint8
call_9065 = relay.TupleGetItem(func_7476_call(relay.reshape(const_9066.astype('uint8'), []), relay.reshape(const_9067.astype('uint8'), [6, 1, 15]), ), 0)
call_9068 = relay.TupleGetItem(func_7480_call(relay.reshape(const_9066.astype('uint8'), []), relay.reshape(const_9067.astype('uint8'), [6, 1, 15]), ), 0)
output = relay.Tuple([uop_9063,call_9065,const_9066,const_9067,])
output2 = relay.Tuple([uop_9063,call_9068,const_9066,const_9067,])
func_9070 = relay.Function([], output)
mod['func_9070'] = func_9070
mod = relay.transform.InferType()(mod)
mutated_mod['func_9070'] = func_9070
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9070_call = mutated_mod.get_global_var('func_9070')
call_9071 = func_9070_call()
output = call_9071
func_9072 = relay.Function([], output)
mutated_mod['func_9072'] = func_9072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4724_call = mod.get_global_var('func_4724')
func_4726_call = mutated_mod.get_global_var('func_4726')
call_9117 = relay.TupleGetItem(func_4724_call(), 0)
call_9118 = relay.TupleGetItem(func_4726_call(), 0)
func_7659_call = mod.get_global_var('func_7659')
func_7661_call = mutated_mod.get_global_var('func_7661')
call_9119 = relay.TupleGetItem(func_7659_call(), 2)
call_9120 = relay.TupleGetItem(func_7661_call(), 2)
output = relay.Tuple([call_9117,call_9119,])
output2 = relay.Tuple([call_9118,call_9120,])
func_9122 = relay.Function([], output)
mod['func_9122'] = func_9122
mod = relay.transform.InferType()(mod)
output = func_9122()
func_9123 = relay.Function([], output)
mutated_mod['func_9123'] = func_9123
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9124 = relay.var("var_9124", dtype = "float64", shape = (6, 7, 6))#candidate|9124|(6, 7, 6)|var|float64
uop_9125 = relay.acos(var_9124.astype('float64')) # shape=(6, 7, 6)
func_7277_call = mod.get_global_var('func_7277')
func_7279_call = mutated_mod.get_global_var('func_7279')
call_9127 = relay.TupleGetItem(func_7277_call(), 0)
call_9128 = relay.TupleGetItem(func_7279_call(), 0)
func_8754_call = mod.get_global_var('func_8754')
func_8756_call = mutated_mod.get_global_var('func_8756')
call_9134 = relay.TupleGetItem(func_8754_call(), 0)
call_9135 = relay.TupleGetItem(func_8756_call(), 0)
uop_9144 = relay.log10(uop_9125.astype('float32')) # shape=(6, 7, 6)
output = relay.Tuple([call_9127,call_9134,uop_9144,])
output2 = relay.Tuple([call_9128,call_9135,uop_9144,])
func_9152 = relay.Function([var_9124,], output)
mod['func_9152'] = func_9152
mod = relay.transform.InferType()(mod)
var_9153 = relay.var("var_9153", dtype = "float64", shape = (6, 7, 6))#candidate|9153|(6, 7, 6)|var|float64
output = func_9152(var_9153)
func_9154 = relay.Function([var_9153], output)
mutated_mod['func_9154'] = func_9154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4963_call = mod.get_global_var('func_4963')
func_4965_call = mutated_mod.get_global_var('func_4965')
call_9185 = relay.TupleGetItem(func_4963_call(), 2)
call_9186 = relay.TupleGetItem(func_4965_call(), 2)
func_8369_call = mod.get_global_var('func_8369')
func_8370_call = mutated_mod.get_global_var('func_8370')
call_9188 = relay.TupleGetItem(func_8369_call(), 0)
call_9189 = relay.TupleGetItem(func_8370_call(), 0)
var_9198 = relay.var("var_9198", dtype = "int64", shape = (588, 126))#candidate|9198|(588, 126)|var|int64
bop_9199 = relay.less(call_9185.astype('bool'), relay.reshape(var_9198.astype('bool'), relay.shape_of(call_9185))) # shape=(588, 126)
bop_9202 = relay.less(call_9186.astype('bool'), relay.reshape(var_9198.astype('bool'), relay.shape_of(call_9186))) # shape=(588, 126)
var_9203 = relay.var("var_9203", dtype = "bool", shape = (588, 126))#candidate|9203|(588, 126)|var|bool
bop_9204 = relay.subtract(bop_9199.astype('int32'), relay.reshape(var_9203.astype('int32'), relay.shape_of(bop_9199))) # shape=(588, 126)
bop_9207 = relay.subtract(bop_9202.astype('int32'), relay.reshape(var_9203.astype('int32'), relay.shape_of(bop_9202))) # shape=(588, 126)
output = relay.Tuple([call_9188,bop_9204,])
output2 = relay.Tuple([call_9189,bop_9207,])
func_9208 = relay.Function([var_9198,var_9203,], output)
mod['func_9208'] = func_9208
mod = relay.transform.InferType()(mod)
var_9209 = relay.var("var_9209", dtype = "int64", shape = (588, 126))#candidate|9209|(588, 126)|var|int64
var_9210 = relay.var("var_9210", dtype = "bool", shape = (588, 126))#candidate|9210|(588, 126)|var|bool
output = func_9208(var_9209,var_9210,)
func_9211 = relay.Function([var_9209,var_9210,], output)
mutated_mod['func_9211'] = func_9211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5372_call = mod.get_global_var('func_5372')
func_5374_call = mutated_mod.get_global_var('func_5374')
call_9213 = func_5372_call()
call_9214 = func_5372_call()
output = call_9213
output2 = call_9214
func_9216 = relay.Function([], output)
mod['func_9216'] = func_9216
mod = relay.transform.InferType()(mod)
output = func_9216()
func_9217 = relay.Function([], output)
mutated_mod['func_9217'] = func_9217
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4758_call = mod.get_global_var('func_4758')
func_4759_call = mutated_mod.get_global_var('func_4759')
call_9234 = func_4758_call()
call_9235 = func_4758_call()
output = call_9234
output2 = call_9235
func_9252 = relay.Function([], output)
mod['func_9252'] = func_9252
mod = relay.transform.InferType()(mod)
output = func_9252()
func_9253 = relay.Function([], output)
mutated_mod['func_9253'] = func_9253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8369_call = mod.get_global_var('func_8369')
func_8370_call = mutated_mod.get_global_var('func_8370')
call_9266 = relay.TupleGetItem(func_8369_call(), 0)
call_9267 = relay.TupleGetItem(func_8370_call(), 0)
output = relay.Tuple([call_9266,])
output2 = relay.Tuple([call_9267,])
func_9273 = relay.Function([], output)
mod['func_9273'] = func_9273
mod = relay.transform.InferType()(mod)
output = func_9273()
func_9274 = relay.Function([], output)
mutated_mod['func_9274'] = func_9274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5137_call = mod.get_global_var('func_5137')
func_5138_call = mutated_mod.get_global_var('func_5138')
call_9307 = relay.TupleGetItem(func_5137_call(), 1)
call_9308 = relay.TupleGetItem(func_5138_call(), 1)
output = call_9307
output2 = call_9308
func_9336 = relay.Function([], output)
mod['func_9336'] = func_9336
mod = relay.transform.InferType()(mod)
mutated_mod['func_9336'] = func_9336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9336_call = mutated_mod.get_global_var('func_9336')
call_9337 = func_9336_call()
output = call_9337
func_9338 = relay.Function([], output)
mutated_mod['func_9338'] = func_9338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7299_call = mod.get_global_var('func_7299')
func_7301_call = mutated_mod.get_global_var('func_7301')
call_9339 = relay.TupleGetItem(func_7299_call(), 1)
call_9340 = relay.TupleGetItem(func_7301_call(), 1)
output = relay.Tuple([call_9339,])
output2 = relay.Tuple([call_9340,])
func_9357 = relay.Function([], output)
mod['func_9357'] = func_9357
mod = relay.transform.InferType()(mod)
output = func_9357()
func_9358 = relay.Function([], output)
mutated_mod['func_9358'] = func_9358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7440_call = mod.get_global_var('func_7440')
func_7442_call = mutated_mod.get_global_var('func_7442')
call_9361 = func_7440_call()
call_9362 = func_7440_call()
func_6700_call = mod.get_global_var('func_6700')
func_6702_call = mutated_mod.get_global_var('func_6702')
call_9370 = relay.TupleGetItem(func_6700_call(), 0)
call_9371 = relay.TupleGetItem(func_6702_call(), 0)
bop_9386 = relay.right_shift(call_9361.astype('uint32'), call_9370.astype('uint32')) # shape=(7, 2, 5)
bop_9389 = relay.right_shift(call_9362.astype('uint32'), call_9371.astype('uint32')) # shape=(7, 2, 5)
output = relay.Tuple([bop_9386,])
output2 = relay.Tuple([bop_9389,])
func_9413 = relay.Function([], output)
mod['func_9413'] = func_9413
mod = relay.transform.InferType()(mod)
output = func_9413()
func_9414 = relay.Function([], output)
mutated_mod['func_9414'] = func_9414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9357_call = mod.get_global_var('func_9357')
func_9358_call = mutated_mod.get_global_var('func_9358')
call_9460 = relay.TupleGetItem(func_9357_call(), 0)
call_9461 = relay.TupleGetItem(func_9358_call(), 0)
uop_9481 = relay.cosh(call_9460.astype('float32')) # shape=(7, 2, 5)
uop_9483 = relay.cosh(call_9461.astype('float32')) # shape=(7, 2, 5)
output = uop_9481
output2 = uop_9483
func_9492 = relay.Function([], output)
mod['func_9492'] = func_9492
mod = relay.transform.InferType()(mod)
mutated_mod['func_9492'] = func_9492
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9492_call = mutated_mod.get_global_var('func_9492')
call_9493 = func_9492_call()
output = call_9493
func_9494 = relay.Function([], output)
mutated_mod['func_9494'] = func_9494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7659_call = mod.get_global_var('func_7659')
func_7661_call = mutated_mod.get_global_var('func_7661')
call_9512 = relay.TupleGetItem(func_7659_call(), 1)
call_9513 = relay.TupleGetItem(func_7661_call(), 1)
func_5664_call = mod.get_global_var('func_5664')
func_5665_call = mutated_mod.get_global_var('func_5665')
call_9534 = relay.TupleGetItem(func_5664_call(), 0)
call_9535 = relay.TupleGetItem(func_5665_call(), 0)
output = relay.Tuple([call_9512,call_9534,])
output2 = relay.Tuple([call_9513,call_9535,])
func_9551 = relay.Function([], output)
mod['func_9551'] = func_9551
mod = relay.transform.InferType()(mod)
mutated_mod['func_9551'] = func_9551
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9551_call = mutated_mod.get_global_var('func_9551')
call_9552 = func_9551_call()
output = call_9552
func_9553 = relay.Function([], output)
mutated_mod['func_9553'] = func_9553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5113_call = mod.get_global_var('func_5113')
func_5114_call = mutated_mod.get_global_var('func_5114')
call_9565 = func_5113_call()
call_9566 = func_5113_call()
func_8111_call = mod.get_global_var('func_8111')
func_8113_call = mutated_mod.get_global_var('func_8113')
var_9588 = relay.var("var_9588", dtype = "int16", shape = (4096,))#candidate|9588|(4096,)|var|int16
call_9587 = relay.TupleGetItem(func_8111_call(relay.reshape(var_9588.astype('int16'), [16, 16, 16])), 0)
call_9589 = relay.TupleGetItem(func_8113_call(relay.reshape(var_9588.astype('int16'), [16, 16, 16])), 0)
func_5829_call = mod.get_global_var('func_5829')
func_5830_call = mutated_mod.get_global_var('func_5830')
call_9600 = relay.TupleGetItem(func_5829_call(), 0)
call_9601 = relay.TupleGetItem(func_5830_call(), 0)
func_4838_call = mod.get_global_var('func_4838')
func_4840_call = mutated_mod.get_global_var('func_4840')
const_9604 = relay.const([-9.945977,-5.595922,-3.491000,5.704587,-8.081674,-2.989028,0.487874,4.742225,9.796466,7.744923,-0.813845,-3.475901,5.998901,-8.212732,1.674886,4.047048,-9.485169,-3.665118,5.965279,-6.876472,3.000507,5.480682,9.215456,0.429732,0.224733,2.219079,-6.718247,2.633014,1.136377,8.111393,-0.241011,6.661962,-0.335779,1.672372,2.641352,0.667649,-3.772814,1.307464,0.751858,-7.941579,8.431295,4.157765,-0.675009,1.742871,-4.615471,-7.746906,2.520166,0.957115,-8.713454,9.064700,0.977432,-0.623803,4.178302,3.057224,-9.771037,-3.495223,-2.656417,4.054079,-6.944504,-5.913046,2.886473,1.745313,-8.893534,-6.244562,-1.481912,-0.576332,-0.596790,1.762642,-8.933973,9.396628,3.922511,-0.067130,8.644039,-3.658045,-7.524305,-0.083455,1.711924,-7.317685,-9.089663,-1.894714,0.367563,-5.880281,0.252558,3.357706,6.822826,-7.262576,-6.542472,-8.360344,2.190659,-9.608696,3.421308,4.910225,-2.723703,7.669257,9.847328,2.745492,-7.962416,-0.615761,-9.446239,-5.170772,-6.203232,-0.074969,0.507055,-6.843865,7.666913,9.534547,2.169368,8.194098,-9.070301,6.332650,8.679438,-6.262463,-9.320982,3.876320,3.228197,-7.090775,7.444477,-0.291627,0.214709,8.959485,7.944242,-7.177520,5.783819,6.767523,-5.567501,4.445863], dtype = "float32")#candidate|9604|(126,)|const|float32
call_9603 = relay.TupleGetItem(func_4838_call(relay.reshape(const_9604.astype('float32'), [126,])), 2)
call_9605 = relay.TupleGetItem(func_4840_call(relay.reshape(const_9604.astype('float32'), [126,])), 2)
func_9122_call = mod.get_global_var('func_9122')
func_9123_call = mutated_mod.get_global_var('func_9123')
call_9618 = relay.TupleGetItem(func_9122_call(), 1)
call_9619 = relay.TupleGetItem(func_9123_call(), 1)
func_3045_call = mod.get_global_var('func_3045')
func_3048_call = mutated_mod.get_global_var('func_3048')
var_9621 = relay.var("var_9621", dtype = "float64", shape = (72,))#candidate|9621|(72,)|var|float64
var_9622 = relay.var("var_9622", dtype = "uint64", shape = (88, 26))#candidate|9622|(88, 26)|var|uint64
call_9620 = relay.TupleGetItem(func_3045_call(relay.reshape(var_9621.astype('float64'), [4, 3, 6]), relay.reshape(var_9622.astype('uint64'), [2288,]), ), 2)
call_9623 = relay.TupleGetItem(func_3048_call(relay.reshape(var_9621.astype('float64'), [4, 3, 6]), relay.reshape(var_9622.astype('uint64'), [2288,]), ), 2)
output = relay.Tuple([call_9565,call_9587,var_9588,call_9600,call_9603,const_9604,call_9618,call_9620,var_9621,var_9622,])
output2 = relay.Tuple([call_9566,call_9589,var_9588,call_9601,call_9605,const_9604,call_9619,call_9623,var_9621,var_9622,])
func_9629 = relay.Function([var_9588,var_9621,var_9622,], output)
mod['func_9629'] = func_9629
mod = relay.transform.InferType()(mod)
var_9630 = relay.var("var_9630", dtype = "int16", shape = (4096,))#candidate|9630|(4096,)|var|int16
var_9631 = relay.var("var_9631", dtype = "float64", shape = (72,))#candidate|9631|(72,)|var|float64
var_9632 = relay.var("var_9632", dtype = "uint64", shape = (88, 26))#candidate|9632|(88, 26)|var|uint64
output = func_9629(var_9630,var_9631,var_9632,)
func_9633 = relay.Function([var_9630,var_9631,var_9632,], output)
mutated_mod['func_9633'] = func_9633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9070_call = mod.get_global_var('func_9070')
func_9072_call = mutated_mod.get_global_var('func_9072')
call_9658 = relay.TupleGetItem(func_9070_call(), 0)
call_9659 = relay.TupleGetItem(func_9072_call(), 0)
output = relay.Tuple([call_9658,])
output2 = relay.Tuple([call_9659,])
func_9661 = relay.Function([], output)
mod['func_9661'] = func_9661
mod = relay.transform.InferType()(mod)
mutated_mod['func_9661'] = func_9661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9661_call = mutated_mod.get_global_var('func_9661')
call_9662 = func_9661_call()
output = call_9662
func_9663 = relay.Function([], output)
mutated_mod['func_9663'] = func_9663
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6700_call = mod.get_global_var('func_6700')
func_6702_call = mutated_mod.get_global_var('func_6702')
call_9672 = relay.TupleGetItem(func_6700_call(), 0)
call_9673 = relay.TupleGetItem(func_6702_call(), 0)
func_7082_call = mod.get_global_var('func_7082')
func_7084_call = mutated_mod.get_global_var('func_7084')
call_9679 = relay.TupleGetItem(func_7082_call(), 1)
call_9680 = relay.TupleGetItem(func_7084_call(), 1)
output = relay.Tuple([call_9672,call_9679,])
output2 = relay.Tuple([call_9673,call_9680,])
func_9683 = relay.Function([], output)
mod['func_9683'] = func_9683
mod = relay.transform.InferType()(mod)
mutated_mod['func_9683'] = func_9683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9683_call = mutated_mod.get_global_var('func_9683')
call_9684 = func_9683_call()
output = call_9684
func_9685 = relay.Function([], output)
mutated_mod['func_9685'] = func_9685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5234_call = mod.get_global_var('func_5234')
func_5235_call = mutated_mod.get_global_var('func_5235')
call_9686 = relay.TupleGetItem(func_5234_call(), 0)
call_9687 = relay.TupleGetItem(func_5235_call(), 0)
output = call_9686
output2 = call_9687
func_9715 = relay.Function([], output)
mod['func_9715'] = func_9715
mod = relay.transform.InferType()(mod)
output = func_9715()
func_9716 = relay.Function([], output)
mutated_mod['func_9716'] = func_9716
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9749 = relay.var("var_9749", dtype = "float32", shape = (8, 12, 9))#candidate|9749|(8, 12, 9)|var|float32
var_9750 = relay.var("var_9750", dtype = "float32", shape = (8, 12, 9))#candidate|9750|(8, 12, 9)|var|float32
bop_9751 = relay.maximum(var_9749.astype('float32'), relay.reshape(var_9750.astype('float32'), relay.shape_of(var_9749))) # shape=(8, 12, 9)
output = bop_9751
output2 = bop_9751
func_9756 = relay.Function([var_9749,var_9750,], output)
mod['func_9756'] = func_9756
mod = relay.transform.InferType()(mod)
mutated_mod['func_9756'] = func_9756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9756_call = mutated_mod.get_global_var('func_9756')
var_9758 = relay.var("var_9758", dtype = "float32", shape = (8, 12, 9))#candidate|9758|(8, 12, 9)|var|float32
var_9759 = relay.var("var_9759", dtype = "float32", shape = (8, 12, 9))#candidate|9759|(8, 12, 9)|var|float32
call_9757 = func_9756_call(var_9758,var_9759,)
output = call_9757
func_9760 = relay.Function([var_9758,var_9759,], output)
mutated_mod['func_9760'] = func_9760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5865_call = mod.get_global_var('func_5865')
func_5867_call = mutated_mod.get_global_var('func_5867')
call_9768 = func_5865_call()
call_9769 = func_5865_call()
output = call_9768
output2 = call_9769
func_9786 = relay.Function([], output)
mod['func_9786'] = func_9786
mod = relay.transform.InferType()(mod)
mutated_mod['func_9786'] = func_9786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9786_call = mutated_mod.get_global_var('func_9786')
call_9787 = func_9786_call()
output = call_9787
func_9788 = relay.Function([], output)
mutated_mod['func_9788'] = func_9788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6926_call = mod.get_global_var('func_6926')
func_6927_call = mutated_mod.get_global_var('func_6927')
call_9808 = relay.TupleGetItem(func_6926_call(), 2)
call_9809 = relay.TupleGetItem(func_6927_call(), 2)
func_7316_call = mod.get_global_var('func_7316')
func_7319_call = mutated_mod.get_global_var('func_7319')
var_9836 = relay.var("var_9836", dtype = "float32", shape = (12, 220))#candidate|9836|(12, 220)|var|float32
call_9835 = relay.TupleGetItem(func_7316_call(relay.reshape(var_9836.astype('float32'), [2640,])), 5)
call_9837 = relay.TupleGetItem(func_7319_call(relay.reshape(var_9836.astype('float32'), [2640,])), 5)
var_9838 = relay.var("var_9838", dtype = "float32", shape = (12, 220))#candidate|9838|(12, 220)|var|float32
bop_9839 = relay.not_equal(var_9836.astype('bool'), relay.reshape(var_9838.astype('bool'), relay.shape_of(var_9836))) # shape=(12, 220)
bop_9842 = relay.less_equal(var_9836.astype('bool'), relay.reshape(bop_9839.astype('bool'), relay.shape_of(var_9836))) # shape=(12, 220)
uop_9848 = relay.log2(bop_9839.astype('float64')) # shape=(12, 220)
bop_9859 = relay.minimum(uop_9848.astype('uint8'), relay.reshape(bop_9842.astype('uint8'), relay.shape_of(uop_9848))) # shape=(12, 220)
output = relay.Tuple([call_9808,call_9835,bop_9859,])
output2 = relay.Tuple([call_9809,call_9837,bop_9859,])
func_9867 = relay.Function([var_9836,var_9838,], output)
mod['func_9867'] = func_9867
mod = relay.transform.InferType()(mod)
mutated_mod['func_9867'] = func_9867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9867_call = mutated_mod.get_global_var('func_9867')
var_9869 = relay.var("var_9869", dtype = "float32", shape = (12, 220))#candidate|9869|(12, 220)|var|float32
var_9870 = relay.var("var_9870", dtype = "float32", shape = (12, 220))#candidate|9870|(12, 220)|var|float32
call_9868 = func_9867_call(var_9869,var_9870,)
output = call_9868
func_9871 = relay.Function([var_9869,var_9870,], output)
mutated_mod['func_9871'] = func_9871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4886_call = mod.get_global_var('func_4886')
func_4888_call = mutated_mod.get_global_var('func_4888')
call_9905 = func_4886_call()
call_9906 = func_4886_call()
func_6405_call = mod.get_global_var('func_6405')
func_6407_call = mutated_mod.get_global_var('func_6407')
call_9907 = relay.TupleGetItem(func_6405_call(), 1)
call_9908 = relay.TupleGetItem(func_6407_call(), 1)
output = relay.Tuple([call_9905,call_9907,])
output2 = relay.Tuple([call_9906,call_9908,])
func_9928 = relay.Function([], output)
mod['func_9928'] = func_9928
mod = relay.transform.InferType()(mod)
output = func_9928()
func_9929 = relay.Function([], output)
mutated_mod['func_9929'] = func_9929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9357_call = mod.get_global_var('func_9357')
func_9358_call = mutated_mod.get_global_var('func_9358')
call_9932 = relay.TupleGetItem(func_9357_call(), 0)
call_9933 = relay.TupleGetItem(func_9358_call(), 0)
output = call_9932
output2 = call_9933
func_9936 = relay.Function([], output)
mod['func_9936'] = func_9936
mod = relay.transform.InferType()(mod)
output = func_9936()
func_9937 = relay.Function([], output)
mutated_mod['func_9937'] = func_9937
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6674_call = mod.get_global_var('func_6674')
func_6675_call = mutated_mod.get_global_var('func_6675')
call_9966 = relay.TupleGetItem(func_6674_call(), 0)
call_9967 = relay.TupleGetItem(func_6675_call(), 0)
func_8657_call = mod.get_global_var('func_8657')
func_8658_call = mutated_mod.get_global_var('func_8658')
call_9977 = func_8657_call()
call_9978 = func_8657_call()
func_5465_call = mod.get_global_var('func_5465')
func_5468_call = mutated_mod.get_global_var('func_5468')
var_9981 = relay.var("var_9981", dtype = "int16", shape = (224,))#candidate|9981|(224,)|var|int16
call_9980 = relay.TupleGetItem(func_5465_call(relay.reshape(var_9981.astype('int16'), [224,])), 2)
call_9982 = relay.TupleGetItem(func_5468_call(relay.reshape(var_9981.astype('int16'), [224,])), 2)
func_9336_call = mod.get_global_var('func_9336')
func_9338_call = mutated_mod.get_global_var('func_9338')
call_9988 = func_9336_call()
call_9989 = func_9336_call()
output = relay.Tuple([call_9966,call_9977,call_9980,var_9981,call_9988,])
output2 = relay.Tuple([call_9967,call_9978,call_9982,var_9981,call_9989,])
func_9997 = relay.Function([var_9981,], output)
mod['func_9997'] = func_9997
mod = relay.transform.InferType()(mod)
var_9998 = relay.var("var_9998", dtype = "int16", shape = (224,))#candidate|9998|(224,)|var|int16
output = func_9997(var_9998)
func_9999 = relay.Function([var_9998], output)
mutated_mod['func_9999'] = func_9999
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8293_call = mod.get_global_var('func_8293')
func_8294_call = mutated_mod.get_global_var('func_8294')
call_10004 = func_8293_call()
call_10005 = func_8293_call()
output = relay.Tuple([call_10004,])
output2 = relay.Tuple([call_10005,])
func_10021 = relay.Function([], output)
mod['func_10021'] = func_10021
mod = relay.transform.InferType()(mod)
output = func_10021()
func_10022 = relay.Function([], output)
mutated_mod['func_10022'] = func_10022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4386_call = mod.get_global_var('func_4386')
func_4388_call = mutated_mod.get_global_var('func_4388')
call_10032 = relay.TupleGetItem(func_4386_call(), 2)
call_10033 = relay.TupleGetItem(func_4388_call(), 2)
func_1209_call = mod.get_global_var('func_1209')
func_1212_call = mutated_mod.get_global_var('func_1212')
const_10047 = relay.const([-3.658210,-5.505718,-0.093621,-3.888735,2.094077,9.778899,-5.620992,6.287732,-0.453049,-4.270783,2.088960,-2.925513,2.433817,5.122395,0.420091,-1.052315,-8.294859,-0.849591,-5.548524,-8.391316,-7.202367,9.047734,8.786753,7.189463,3.681986,-3.521544,4.583046,0.791253,3.920256,-8.279191,4.455408,-4.744863,7.015801,-1.689638,7.297130,7.793160,-8.772571,-3.032212,0.987826,5.211935,-8.719280,-1.217401,-8.874400,-6.029836,-7.369835,3.981462,0.476225,6.813577,-9.823422,1.759362,-8.184486,-8.112992,5.339959,-8.816204,-5.021105,4.006549,8.120400,5.785243,9.671277,3.858158,-9.932563,8.488007,-4.454737,-5.041369,3.084830,-9.097402,-6.661491,-3.185174,-0.265198,-1.718933,2.094048,0.690080,9.629313,-4.539626,-8.302307,-8.207643,-8.998275,-4.617840,-8.590293,-1.046736,-8.396403,3.274470,8.104775,-1.366230,-1.438023,-6.889664,-1.308280,1.319202,-4.308220,-3.962669,4.273514,8.412071,5.116332,2.984079,-9.500883,7.488950,-8.444443,4.056754,-0.728776,3.876591,2.501816,-9.754139,0.005671,3.358872,-2.095692,-1.734839,1.909924,6.283843,-9.148190,-0.062635,-8.931746,1.345786,0.935968,-7.932864,4.633409,-1.684058,-9.195108,-5.171142,-0.705259,7.204797,-7.843801,5.856978,-3.966304,-5.065036,3.633966,9.072487,-7.056458,-6.382093,-3.031640,1.465199,0.361359,-5.788676,8.020927,8.707563,-3.393776,-1.575934,1.877307,-7.880824,-6.052734,-3.035231,-8.525517,-2.497111,-5.078599,-2.445229,3.993797,-5.568026,1.946555,-2.428578,-9.094525,0.106229,3.408162,1.800010,7.336821,-0.591787], dtype = "float64")#candidate|10047|(154,)|const|float64
call_10046 = func_1209_call(relay.reshape(const_10047.astype('float64'), [11, 7, 2]))
call_10048 = func_1209_call(relay.reshape(const_10047.astype('float64'), [11, 7, 2]))
output = relay.Tuple([call_10032,call_10046,const_10047,])
output2 = relay.Tuple([call_10033,call_10048,const_10047,])
func_10051 = relay.Function([], output)
mod['func_10051'] = func_10051
mod = relay.transform.InferType()(mod)
output = func_10051()
func_10052 = relay.Function([], output)
mutated_mod['func_10052'] = func_10052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5829_call = mod.get_global_var('func_5829')
func_5830_call = mutated_mod.get_global_var('func_5830')
call_10060 = relay.TupleGetItem(func_5829_call(), 0)
call_10061 = relay.TupleGetItem(func_5830_call(), 0)
const_10078 = relay.const([[[False,False,True,True,False,False,False,True,False,True,True,True,True],[False,False,True,False,False,False,True,False,False,True,True,False,False],[True,False,False,False,False,False,False,True,True,False,True,False,True],[True,True,True,True,False,True,True,False,True,False,False,True,False],[False,False,False,False,False,True,False,True,True,False,True,True,True],[True,False,True,True,True,False,False,False,True,True,False,True,True],[True,True,True,False,True,False,True,True,False,True,False,True,False],[True,True,False,True,True,True,True,False,False,False,False,False,True],[False,True,True,True,False,False,False,False,True,True,False,False,True],[False,True,True,True,False,True,True,False,False,False,True,True,False],[True,True,False,True,False,False,True,True,True,True,False,True,True],[True,True,True,True,False,False,False,True,True,False,False,False,False],[False,False,True,True,False,False,True,True,False,True,True,True,True],[True,False,True,False,False,False,True,True,True,True,True,True,True]],[[True,False,True,True,False,False,False,False,True,False,False,False,True],[False,False,True,True,True,False,False,False,False,False,False,False,True],[True,True,True,False,False,False,False,False,True,True,False,True,True],[True,False,True,False,True,False,False,False,True,True,False,True,True],[True,True,True,True,True,False,False,False,False,True,False,True,True],[True,False,True,True,True,False,True,False,False,False,False,False,True],[False,True,True,True,False,False,True,True,True,False,True,False,False],[False,True,False,True,False,True,True,True,False,False,True,True,False],[False,False,True,False,True,True,False,False,False,False,True,True,False],[False,True,True,False,True,True,True,True,False,True,True,True,False],[True,True,False,True,False,False,True,True,False,False,False,False,False],[False,True,True,False,True,False,True,False,False,True,False,False,False],[False,True,True,False,False,True,True,False,False,True,False,True,False],[False,True,False,True,True,True,False,True,True,True,True,False,True]],[[True,True,True,True,False,False,True,True,False,True,False,True,True],[False,True,True,True,True,True,False,False,False,False,True,False,True],[False,True,False,False,True,True,False,False,True,False,False,False,True],[False,True,False,False,False,False,True,True,False,False,False,False,False],[True,False,True,True,True,True,True,True,False,False,True,False,False],[False,False,True,False,True,True,True,True,True,True,False,False,False],[False,True,False,False,True,True,True,True,True,False,False,False,False],[False,False,True,False,False,True,False,True,True,False,True,False,True],[False,True,True,True,True,True,False,True,False,True,True,True,False],[False,True,True,False,True,True,False,False,False,False,True,False,False],[False,False,True,False,False,True,True,True,False,False,True,False,False],[True,False,True,False,False,True,True,True,True,True,True,True,True],[True,True,True,True,True,True,False,False,False,False,False,True,True],[False,False,False,True,False,True,True,True,True,True,False,True,True]],[[True,False,False,False,True,True,True,False,False,True,False,False,True],[False,False,True,True,False,False,True,False,True,True,False,False,False],[True,True,False,False,False,True,False,False,True,False,True,True,False],[False,False,False,False,True,False,True,True,False,True,True,True,True],[False,True,True,False,True,True,True,False,True,False,True,False,False],[True,False,False,False,False,False,False,True,False,True,True,True,False],[True,False,True,True,False,True,False,True,True,True,False,True,True],[False,True,True,False,True,False,False,True,False,False,True,False,True],[False,True,True,True,False,False,False,True,True,False,True,True,True],[False,True,False,True,False,False,False,True,False,False,True,False,True],[True,False,True,True,False,True,True,True,False,True,True,False,False],[True,False,True,False,False,False,True,False,True,False,False,False,True],[False,False,True,False,True,False,False,False,False,False,True,True,True],[False,False,True,False,False,False,True,False,False,True,False,False,True]],[[True,False,True,True,True,True,True,False,True,True,True,True,True],[True,False,True,False,True,True,False,False,True,False,False,False,False],[True,True,False,True,False,False,True,True,True,False,False,True,True],[True,False,False,True,True,True,True,False,True,False,True,True,True],[True,True,True,True,False,False,True,False,True,True,False,False,True],[False,True,True,True,False,True,True,False,False,False,True,True,True],[False,True,False,True,False,True,False,False,True,False,False,False,True],[False,True,True,False,False,True,True,False,False,True,True,True,True],[True,False,False,False,True,False,True,True,True,False,True,False,False],[False,False,False,False,True,False,True,True,True,False,False,False,False],[True,False,True,False,True,False,False,False,False,True,False,True,True],[False,True,False,False,True,False,False,False,False,False,False,True,True],[True,True,True,False,True,False,False,False,True,True,False,True,True],[False,True,False,False,False,False,True,False,False,True,False,False,True]],[[False,False,True,True,True,True,True,True,True,False,True,True,True],[False,False,True,False,False,False,True,False,False,True,False,True,True],[False,False,True,False,True,True,True,True,False,False,False,True,True],[True,False,True,False,True,True,False,False,True,False,False,False,False],[False,True,False,False,False,False,False,True,True,False,False,False,True],[True,False,True,False,False,False,False,True,False,True,False,False,False],[False,True,False,False,True,True,False,False,True,False,False,True,False],[True,True,False,True,False,True,False,True,False,False,True,False,True],[True,False,True,False,False,True,True,False,False,False,True,False,False],[False,False,True,False,False,False,True,True,False,False,False,False,True],[False,False,True,True,True,False,True,False,False,True,False,True,True],[False,False,True,False,False,True,False,True,True,True,False,True,False],[False,True,False,False,False,True,False,True,False,True,False,True,True],[False,False,True,False,True,True,False,False,True,False,False,False,False]],[[True,True,False,False,True,False,True,True,False,False,False,False,True],[False,True,True,True,False,False,True,False,False,True,True,False,True],[True,False,True,True,False,True,False,False,True,True,False,True,False],[False,True,True,False,False,True,True,False,True,False,False,False,False],[False,True,True,False,True,False,False,False,True,True,True,True,True],[True,False,False,False,True,False,True,False,True,True,True,False,True],[False,False,True,True,False,True,False,False,True,True,False,False,False],[False,True,True,True,False,False,False,False,False,True,True,True,True],[False,True,False,False,False,True,True,False,False,True,True,False,True],[True,False,False,True,False,False,False,True,True,False,False,True,True],[False,False,False,False,True,False,True,False,False,True,True,True,True],[True,True,True,True,False,False,True,False,True,True,False,True,True],[False,True,True,True,False,True,False,False,True,True,False,False,True],[True,False,False,False,True,True,True,False,True,False,False,False,False]],[[True,False,True,False,True,True,False,False,False,False,True,False,True],[True,False,True,True,True,False,True,False,True,True,True,False,True],[False,False,False,True,True,True,True,False,False,False,True,False,False],[True,False,True,False,True,False,False,True,False,True,True,True,True],[False,False,True,True,False,True,True,False,False,False,True,True,False],[True,True,True,True,True,True,False,True,True,True,True,True,False],[True,False,False,True,False,False,True,True,True,True,False,True,True],[True,True,True,False,False,False,False,True,False,True,False,False,False],[True,True,False,False,False,True,True,False,False,True,False,False,False],[False,True,False,True,True,True,False,False,False,False,False,False,False],[False,True,False,False,False,False,False,False,False,False,True,True,False],[False,False,False,False,False,False,True,True,True,False,False,False,False],[False,False,True,False,False,True,False,True,False,False,True,False,False],[True,False,True,True,False,True,True,False,True,False,True,True,True]],[[False,True,True,False,False,False,True,True,False,True,False,False,False],[False,False,True,False,False,True,False,False,False,False,True,True,True],[True,True,False,False,False,False,True,False,True,True,False,False,False],[False,True,True,True,False,True,True,True,False,False,False,False,False],[False,True,True,False,False,False,True,False,False,False,False,False,False],[True,True,False,True,False,False,True,True,True,True,False,True,False],[False,True,True,True,True,True,False,False,True,False,True,True,False],[True,True,False,True,True,False,True,True,True,True,True,False,False],[True,True,False,False,False,True,True,True,False,False,False,False,False],[False,False,True,True,False,True,False,False,False,True,False,True,False],[False,False,True,False,False,False,False,True,False,False,False,True,True],[False,True,True,False,False,True,False,True,False,False,False,False,False],[True,True,True,False,True,True,True,True,True,True,True,True,False],[False,True,False,True,False,False,True,False,False,True,True,False,False]],[[False,False,True,False,True,False,False,False,False,True,True,True,False],[False,True,False,False,True,False,True,False,True,False,False,False,False],[True,True,True,True,False,True,False,True,False,True,True,False,True],[True,True,False,True,False,False,False,False,False,True,False,False,True],[True,False,False,False,False,True,True,True,False,True,True,False,False],[True,True,True,True,False,True,False,False,False,False,True,False,False],[True,True,False,True,True,False,True,True,False,True,False,True,True],[False,True,False,True,True,True,False,True,False,True,False,False,True],[False,True,False,False,True,False,True,False,True,False,False,True,True],[False,False,True,True,True,False,False,True,True,False,False,True,True],[False,False,True,True,False,True,False,False,True,True,False,False,True],[False,True,True,True,False,True,True,False,True,True,False,True,False],[True,True,True,False,False,True,True,True,False,True,False,False,True],[True,False,False,False,True,False,True,True,True,True,False,False,True]],[[True,True,True,True,False,False,False,True,True,True,False,False,False],[True,True,True,True,False,False,True,False,False,True,False,True,False],[True,True,False,False,False,False,True,False,True,True,False,True,False],[True,False,True,True,True,False,False,False,True,True,False,True,True],[True,False,False,False,False,True,True,False,True,False,False,True,False],[True,False,False,True,True,False,True,False,True,False,False,False,False],[True,True,True,False,False,False,False,False,False,False,False,False,True],[True,False,True,False,False,True,True,False,False,False,False,True,False],[False,False,False,False,False,True,True,True,False,True,True,False,False],[False,True,False,False,False,True,False,True,False,False,False,True,False],[False,True,True,False,True,True,False,True,True,False,False,False,False],[False,True,True,True,True,True,False,True,True,False,True,True,True],[True,True,False,False,False,False,True,True,False,False,False,False,True],[True,True,True,True,True,False,False,False,True,False,False,True,True]],[[True,True,False,True,False,True,False,False,True,False,True,False,True],[True,False,True,False,True,False,True,True,True,False,True,False,False],[False,False,False,True,True,False,False,False,True,False,True,True,True],[True,False,False,True,True,True,False,True,True,True,True,False,False],[True,False,True,True,True,True,True,True,False,False,True,False,False],[False,True,False,False,False,True,False,False,False,True,True,False,False],[True,False,False,True,False,True,False,False,False,True,True,True,False],[False,True,False,False,False,False,True,False,False,True,True,False,True],[True,False,True,False,False,False,False,False,True,False,True,True,False],[True,False,False,False,True,False,False,True,False,False,True,False,False],[False,True,True,False,True,False,False,False,False,True,False,False,True],[True,True,True,True,True,False,True,True,True,False,True,True,True],[False,True,True,False,True,True,True,False,True,False,False,False,False],[True,True,False,True,False,False,False,True,True,False,False,False,True]]], dtype = "bool")#candidate|10078|(12, 14, 13)|const|bool
bop_10079 = relay.maximum(call_10060.astype('uint8'), relay.reshape(const_10078.astype('uint8'), relay.shape_of(call_10060))) # shape=(12, 14, 13)
bop_10082 = relay.maximum(call_10061.astype('uint8'), relay.reshape(const_10078.astype('uint8'), relay.shape_of(call_10061))) # shape=(12, 14, 13)
func_5906_call = mod.get_global_var('func_5906')
func_5908_call = mutated_mod.get_global_var('func_5908')
call_10084 = relay.TupleGetItem(func_5906_call(), 0)
call_10085 = relay.TupleGetItem(func_5908_call(), 0)
output = relay.Tuple([bop_10079,call_10084,])
output2 = relay.Tuple([bop_10082,call_10085,])
func_10086 = relay.Function([], output)
mod['func_10086'] = func_10086
mod = relay.transform.InferType()(mod)
mutated_mod['func_10086'] = func_10086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10086_call = mutated_mod.get_global_var('func_10086')
call_10087 = func_10086_call()
output = call_10087
func_10088 = relay.Function([], output)
mutated_mod['func_10088'] = func_10088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6330_call = mod.get_global_var('func_6330')
func_6332_call = mutated_mod.get_global_var('func_6332')
call_10102 = relay.TupleGetItem(func_6330_call(), 3)
call_10103 = relay.TupleGetItem(func_6332_call(), 3)
func_7702_call = mod.get_global_var('func_7702')
func_7703_call = mutated_mod.get_global_var('func_7703')
call_10111 = relay.TupleGetItem(func_7702_call(), 2)
call_10112 = relay.TupleGetItem(func_7703_call(), 2)
func_4838_call = mod.get_global_var('func_4838')
func_4840_call = mutated_mod.get_global_var('func_4840')
var_10119 = relay.var("var_10119", dtype = "float32", shape = (126,))#candidate|10119|(126,)|var|float32
call_10118 = relay.TupleGetItem(func_4838_call(relay.reshape(var_10119.astype('float32'), [126,])), 0)
call_10120 = relay.TupleGetItem(func_4840_call(relay.reshape(var_10119.astype('float32'), [126,])), 0)
func_7316_call = mod.get_global_var('func_7316')
func_7319_call = mutated_mod.get_global_var('func_7319')
const_10126 = relay.const([-9.834442,2.736802,0.944712,-1.970795,6.091761,-7.284793,5.568789,2.475662,-1.007204,5.787315,-3.745545,-8.235062,-2.887076,-5.498019,4.755552,-0.519518,1.577196,-0.612942,3.375575,2.793926,-8.269084,7.658695,-9.536418,5.675789,-6.030812,-7.183487,-0.717162,-8.036083,4.657048,-0.843449,-8.058187,-2.556053,-6.044280,-4.790973,2.422570,4.741782,0.438533,0.910259,9.787038,4.650631,-7.518382,-7.621083,-3.989735,6.588084,5.854074,1.667779,9.244189,5.700595,-3.172221,1.158666,-8.790517,4.609702,-5.634686,2.380363,2.031001,4.369203,-9.583771,-2.843858,-7.878321,-2.646571,6.932474,2.977957,-3.376759,4.214378,8.747348,-9.968723,4.922049,5.491305,6.865677,3.932807,4.336131,-9.712655,-2.060619,0.393435,-2.817586,4.030773,7.125227,-6.714440,3.722568,-1.801779,9.231629,-7.731902,-5.548817,-0.396976,-4.527351,5.384049,-3.499079,-3.143726,-7.362066,-7.347163,9.458672,2.691299,-2.496717,-5.114161,8.642785,-3.109268,-8.692987,4.191437,0.694122,-0.530155,5.506666,2.679602,6.754284,-7.964625,9.278423,-1.768874,-4.550682,7.741898,-4.289398,0.415734,-8.918138,-6.435516,-4.113732,-4.300918,1.723236,-0.055828,-0.188821,-9.985842,4.206311,1.164638,6.844980,6.278985,2.344994,9.663551,2.326851,4.282046,-0.515036,-4.003558,6.502123,-7.962999,4.003616,9.623234,0.418896,2.407331,6.831098,3.198758,-2.427325,-0.166123,-0.572470,5.956050,-7.958732,2.540569,-1.352969,-8.594894,-0.858059,-8.236999,5.409441,9.333255,-9.075489,6.947149,-0.070322,-1.357380,3.358657,-7.874437,-1.434513,1.543480,3.403451,-2.015512,-1.251617,9.463266,5.261148,-7.267902,-4.067486,6.508181,-3.723092,-7.013766,-0.438116,-3.640824,4.309208,6.565843,-7.002664,5.825940,6.130807,-4.475519,-2.776139,6.718683,1.211037,-4.103942,0.859895,-1.732600,-4.837349,-9.070316,-8.473871,-3.893053,-0.343583,9.657609,1.152122,-3.097711,-8.938376,-7.889624,-2.895007,1.340476,-7.168143,8.930442,6.847316,9.175774,-1.932726,-2.680584,-4.552153,6.513667,-9.176672,-3.322269,1.528785,8.679135,3.375625,-8.887940,9.373831,5.868757,5.142410,6.022645,7.097596,-7.722404,5.605577,-0.514855,4.086174,-2.244304,-3.150710,2.850767,1.450392,-1.417145,5.305551,-5.648925,-3.552296,-8.608719,9.747126,-7.236936,-1.492105,-3.968017,-3.355531,-9.184369,-2.490085,1.949300,1.280361,-3.257022,4.931098,0.940006,1.315984,4.634767,0.201835,7.570817,-6.221867,4.418521,-7.924471,-7.902834,-9.926093,0.126500,9.741291,-6.671905,2.775721,8.346035,6.142197,0.632994,-2.938464,-2.756185,-8.944678,-9.022452,3.387485,-4.463715,-3.552245,-5.820362,5.195671,2.774622,5.762498,8.706220,5.905561,3.180646,0.869737,6.516654,-1.308042,4.994645,-6.652187,8.441198,-3.193619,4.476271,-1.483945,0.363793,4.088816,-0.648411,-5.828096,-4.721296,-0.828267,-8.293663,-2.540635,9.193080,6.647458,-5.660067,9.299193,-0.502639,8.154211,-0.185625,1.446593,3.764188,-4.144389,8.963676,9.501047,-2.165916,-8.034496,6.112937,2.420740,0.724589,7.266437,-5.267136,1.312286,-9.749898,-6.609276,-0.228605,4.300476,7.542030,3.059108,-6.435286,-8.142746,-0.013542,-9.854223,5.532308,-1.809725,-8.411706,-5.905015,-6.462811,5.941799,-3.090333,6.749210,-8.335460,-5.443173,7.704683,-2.489713,-2.887526,-7.239594,1.974116,-6.925385,-8.519600,8.413067,7.676440,1.959883,4.630435,-4.683352,2.689630,-1.255383,-5.484166,8.299523,-6.307041,-3.797529,-5.378761,0.242503,7.329093,-0.913644,9.113103,-6.873959,-8.016103,-9.216620,3.275549,0.100328,5.826078,-5.276726,3.610836,8.315381,3.194205,-7.119041,-8.663779,-2.307732,-1.326900,-6.173248,-9.665793,-9.213684,-8.968927,9.335948,7.835853,-7.104827,-5.762680,8.118859,-6.808147,-9.088737,-1.931969,4.333130,-9.791472,-3.051826,4.331474,-3.115941,4.717971,-7.470974,-9.886999,2.103974,-1.099303,-0.729079,-2.886458,-8.490442,-7.326773,7.006746,-7.868005,1.793721,-2.811988,1.506586,-1.327320,5.502232,-7.641404,-2.803441,0.624420,-7.738722,3.231478,0.097989,-5.527795,2.189982,-0.991949,1.161102,4.095805,4.973642,-8.232123,1.366557,7.021757,3.404574,-1.678100,-8.927693,3.722546,-6.489361,1.707315,4.804953,8.237569,-8.079613,1.936439,-3.634609,-2.405054,-8.581940,-2.105338,-9.298115,-9.620001,1.583226,1.729896,1.113957,9.600568,5.090916,5.454936,-1.723538,3.417579,-7.534358,7.502420,-3.339524,-5.871811,-9.940098,-4.160122,-2.937386,-0.209299,-9.102109,1.744315,5.300017,9.198577,0.717329,8.845974,5.313233,-2.312922,8.797538,7.495952,-3.640684,-4.310365,-5.552385,1.347320,8.827813,1.115490,8.149097,0.632490,8.311692,5.484369,2.292990,-6.558144,-6.538444,-0.635508,-5.126980,7.474086,-0.386661,-3.494128,-6.162734,2.454401,7.167685,7.118278,-9.886280,0.937679,7.226629,-2.075041,0.945811,-4.622563,-8.872949,0.669394,-7.500843,1.791762,-0.510535,0.750600,4.595223,4.854527,6.705052,0.014069,2.040954,5.171987,2.329359,-6.137622,1.519655,-4.433116,1.961213,-3.985928,-1.094253,-5.188050,5.170107,-2.019841,4.675177,-5.166565,-6.858453,-9.687793,-1.337964,9.999994,0.726749,7.760668,-2.875814,-4.920737,4.946747,1.570333,-3.880504,1.018691,5.551708,-7.835613,6.201855,-0.259291,-7.352584,6.205257,-6.328951,6.133130,-4.568388,-7.835726,-7.430394,8.590373,-4.439510,-7.591125,-6.434899,-6.887250,3.013867,-8.217229,9.873093,-5.219826,9.551181,3.471234,-1.876619,-1.336661,5.675160,2.550072,4.401388,1.013077,5.325561,7.306938,8.549219,-7.032097,-1.949229,4.363443,4.161350,-5.388268,-4.920266,-4.251703,-9.174659,4.421194,-9.939884,5.371989,9.217801,6.777338,-4.907954,1.229060,-5.075868,-8.848241,-8.697158,1.513666,-9.657507,4.184867,8.406338,7.302285,-5.842805,6.551349,-1.170979,-0.261011,5.372003,-1.391173,-3.101516,-6.837113,6.587796,-7.131177,-8.552746,2.631534,1.959390,4.206442,5.406336,-4.164811,-4.821172,-9.204849,-4.048723,-8.191107,-8.544462,-0.498087,-9.616035,0.369915,2.542955,-7.287146,9.701242,-0.840453,-5.856307,6.056545,5.628285,6.003634,0.859322,-9.770458,-9.011020,-6.280511,1.680241,-6.044231,2.962524,-8.400473,9.327462,-1.800676,-0.766271,9.299470,3.548187,-6.110582,-7.072646,-0.919880,0.369893,8.536682,3.526577,-8.498437,-3.145882,5.105826,8.600925,6.497895,-0.975977,3.676168,-3.211985,0.727235,-5.159472,-6.630164,5.237420,-0.139824,3.932343,-5.235553,1.163052,-4.781707,3.197993,1.805813,1.130610,3.738624,7.070095,-5.003123,2.857039,7.487345,-1.484139,-5.143963,-2.112680,-5.915185,4.513795,-5.315238,-1.916279,-5.080703,-6.847883,-7.939618,-8.288308,6.612883,-4.072401,-6.800106,2.895613,0.483332,7.298801,2.721051,5.787915,-3.506046,6.962179,5.365555,1.611744,8.054064,-1.217729,7.305746,-9.543310,-9.091408,-6.862171,-3.969223,-8.078200,8.873045,-8.924404,1.868219,6.843878,-2.817314,-6.876950,-6.409881,7.016007,-8.682054,4.180413,6.678772,-3.269884,-6.996624,-2.673798,9.585835,4.509562,-5.305004,1.541580,5.002450,8.421994,6.574507,6.008737,6.734735,-1.764050,-3.331156,4.185301,3.186076,4.904861,7.054154,-7.818412,-0.677765,1.694967,9.343103,-4.094942,3.037688,-9.344106,-2.805084,-7.471590,1.781971,4.166691,-7.322073,8.654048,-2.509921,-0.826978,-1.807686,-6.993386,-8.030004,1.043912,1.304048,-2.200298,-7.528056,0.470035,-8.447404,-2.072812,-6.158039,-9.887257,0.352489,-0.680821,-8.473312,6.420085,-9.120583,-8.558132,7.801172,-6.812175,6.017277,-6.066446,-6.647550,-4.930464,4.796437,-2.136282,-3.440483,2.311549,-1.219333,-5.421914,-9.694181,9.131199,5.267581,6.614526,7.568835,1.887267,-9.738644,-5.151903,-0.250822,7.825273,-2.631300,9.256606,-5.984545,-4.252035,7.704236,-9.771120,-5.344724,-1.162270,4.353417,-5.278613,8.724152,0.529249,5.471383,-3.698313,8.495410,-4.725394,2.430869,-9.200027,-9.665552,-3.342537,9.099550,5.214590,-1.001132,-3.746984,4.851001,1.469565,-8.787593,-6.625293,-5.675291,6.406847,-2.540469,8.682179,-9.620348,-3.700087,-8.752640,-3.075407,7.724821,4.162623,0.712668,2.049201,0.186900,6.260622,5.903035,5.914771,7.097360,6.345665,-7.688310,4.964078,4.543832,9.514449,9.486783,3.669265,3.703630,-9.938066,-7.421779,8.712594,-0.593087,-6.350231,-9.127380,-5.048203,-9.173236,-3.924970,-0.036627,8.227907,3.109854,-8.860448,-5.370679,0.708950,-4.849313,-5.627806,7.073817,-6.229733,7.446543,9.525391,3.902157,2.596650,-0.641065,-0.609178,2.901179,-0.567640,2.472284,4.866211,-1.886822,0.117301,7.918923,-4.425121,-9.599207,-2.195286,8.758483,2.030027,9.245943,-0.171699,-5.396707,4.851169,0.619676,-8.812938,-5.936235,-7.042925,-7.212315,4.016430,-3.746989,-5.073480,5.363812,-3.661307,3.634737,8.535386,-5.713508,-7.532504,-4.106705,-6.019314,7.791858,-9.167467,4.399653,-6.276190,1.776470,9.493577,2.676520,-4.638696,-9.006960,4.045199,-8.363808,0.365125,9.183688,-5.941678,8.960678,3.626868,7.894284,-7.319754,-3.684208,6.077413,-7.717205,8.451558,-3.667255,-8.791973,-5.738352,-1.909021,-5.107028,6.150258,5.777067,-2.567267,7.380321,8.920381,8.674058,1.687133,0.319066,7.305115,8.387620,7.685859,-4.065540,-3.833226,-7.017589,-5.118264,-6.787296,-4.692421,6.004851,-0.412992,-7.106196,2.166017,1.566325,9.546113,1.436007,6.882738,-4.118862,2.153243,-5.841181,4.237733,-6.919741,-7.084749,-5.286109,1.964577,3.435335,-3.530966,8.623031,9.834660,-3.482474,5.404774,-9.637197,-3.404308,-7.431605,7.038643,3.667595,7.320967,-2.176290,6.427568,-6.247985,-6.219791,-4.448979,9.862758,9.574457,7.968408,8.340664,9.071690,6.730439,-9.199434,6.533061,-0.871962,8.108150,6.560465,1.904658,-1.399752,9.345522,8.747877,6.808610,2.564451,-6.524137,-1.608849,-1.607742,4.569798,0.296629,7.936535,4.255734,5.583253,7.452969,2.907405,2.279399,-9.254025,-8.820452,5.754235,-8.627032,-4.646762,9.933491,-6.814446,1.996687,3.350143,-7.251492,1.536679,-5.787253,-5.307217,5.641075,8.661459,2.094436,7.179253,8.169193,2.486971,-7.922499,-3.183490,-1.982264,1.008909,-6.092055,-6.310717,3.154395,6.065259,-0.145155,7.829478,6.491162,8.535080,-0.545527,-9.667776,7.286095,4.442659,-5.318296,4.482130,-3.351936,-1.883872,8.999492,9.499346,-6.455134,-5.788804,-4.014891,3.126114,-0.624953,-9.577935,4.548624,5.008820,-9.861413,-1.699329,-6.390997,3.684596,-4.282264,-8.852460,-8.628417,-7.439661,-1.572102,-3.598111,-9.511011,-1.723149,-3.070997,1.738167,2.159426,-9.502086,3.949515,-1.853907,-6.175677,2.322495,2.919302,-1.046769,3.088741,7.467595,5.637127,8.096274,1.268003,7.708896,-7.273156,9.628092,2.958978,-3.086699,0.304532,-6.150321,-3.878006,-2.631087,4.781506,-9.662488,-5.804041,-5.033559,7.528974,0.283804,9.985625,-7.611722,-7.169730,-3.696298,5.425114,-9.104022,9.267666,-4.724806,-4.922617,-7.476317,8.304589,8.206835,-1.770284,8.733075,6.017741,-4.202160,0.991393,-0.322073,-8.736025,4.383443,0.857477,-8.311019,6.245592,7.658079,-8.050345,3.930239,-1.251957,4.724650,4.537238,-9.754251,9.580200,8.952808,4.786851,-3.141697,-9.842420,8.790878,-8.732920,6.701595,-1.611400,0.675742,-9.546579,-5.082813,2.196902,8.943240,-9.823835,2.524905,-6.163954,4.824705,4.637420,0.541359,0.050329,0.881654,0.562915,6.788512,6.122280,-5.925930,-4.411834,-6.132157,-4.714540,-0.819258,2.718236,-1.941372,-5.248144,0.598388,-5.501665,-4.358886,5.763781,0.114403,-5.259911,-4.304220,1.579667,4.792003,5.111359,-6.242666,4.472199,3.166444,-1.316842,-9.790980,3.414190,-9.779119,-7.716473,0.516435,6.539840,-0.610786,-3.514537,0.396500,1.197945,2.121962,9.130052,-9.439930,-3.169301,1.326836,-3.594851,0.605302,-1.649257,7.936961,-3.111533,-0.707861,0.322412,8.066015,-9.316545,7.702878,4.525525,-0.235845,-9.405841,5.970701,-5.574349,-2.768427,-6.736492,-1.730590,6.621568,-1.967466,6.165699,7.026229,7.551766,-3.096201,-5.599446,-7.721450,-2.068258,-9.924165,4.240520,2.757561,-8.225763,-0.056619,7.387883,3.024373,-7.779721,6.891721,1.148278,-4.539741,6.821362,-2.638596,7.877797,-2.091445,2.934549,-7.409736,-9.569972,1.587147,9.322337,-8.015651,-5.118897,-5.748059,7.057923,-4.457484,-5.548677,9.321922,6.788184,3.909629,-1.461500,-7.070603,-4.973568,2.047129,-2.900353,-2.881817,-4.428320,0.167960,-2.871854,-3.341737,2.783171,-8.846435,7.578024,4.650226,0.277592,8.515523,-2.884296,-7.846148,9.129669,-7.818635,-2.415755,0.282171,3.766764,7.606630,-2.362814,9.054560,1.411003,-0.424120,5.171879,2.394122,-4.228977,1.600277,0.543875,-1.282765,1.989985,-0.325434,9.631872,-3.940856,-7.147642,-3.296948,5.816714,-1.831215,-3.112464,-1.697950,2.974766,-8.580586,-7.569615,-2.641261,5.824874,-0.781220,2.786593,-4.506392,7.268020,4.622556,1.902872,-6.925292,6.041085,8.330282,9.244098,-8.701288,2.460869,6.496297,-4.169063,2.868256,-2.931574,-1.494927,7.108736,-8.614466,6.120644,-6.024014,8.049640,-9.328658,-5.582421,-4.864330,2.086318,-9.999941,-3.860054,-6.988271,9.695767,-5.919125,-3.386938,-7.916275,-5.543690,-3.052992,-8.678193,-9.188766,1.309405,0.113285,-7.215468,-3.938589,-0.072129,-7.798763,-1.299699,6.955060,1.576279,8.888982,-5.831951,0.933194,-6.191363,-2.864159,-4.607317,-3.489489,3.924629,9.743958,-4.965369,5.379558,-8.528577,0.259760,3.226263,3.234744,-9.915834,-7.935907,-9.002636,8.820692,5.077222,1.832390,-4.615014,1.856890,8.759321,3.255275,-8.126723,-1.398811,0.113453,5.751714,-0.575669,6.706326,2.592627,9.499891,8.846057,-3.608560,0.097663,-1.420319,-1.833418,6.470448,0.704627,3.660847,-8.983343,-1.514164,0.308250,-4.129716,-6.248786,-6.926400,8.631491,8.175734,1.170625,9.253824,-5.212688,-1.589529,8.192943,-8.960395,8.324743,4.614784,-5.902744,8.413546,6.563802,8.850994,1.573826,-3.882205,-3.308932,0.671165,6.629989,-2.046406,-2.327513,-5.597196,-2.111908,-1.818749,-1.454073,4.133360,-8.420479,-8.248272,-1.272339,2.289073,-8.219767,-9.267527,-1.995555,-7.400567,-0.802350,0.726282,2.444644,3.843182,-4.621356,4.707915,5.110423,4.098462,4.931301,8.502857,-1.815989,7.315520,-7.438119,6.997683,4.809416,8.456539,-8.492293,4.194630,-4.624330,2.476863,-5.071790,-5.310831,-7.412729,9.427185,2.307869,9.771106,-7.104069,-4.900926,5.825198,2.996238,9.901221,-6.795393,1.059299,-1.147718,-7.339972,-0.498757,-5.737789,-2.440726,0.964866,2.981579,1.876084,-9.282780,2.107058,-1.036964,-3.479403,-4.563970,-7.383371,3.343035,-1.462645,-8.833301,4.472584,7.311148,6.579369,-7.428661,-1.433742,6.727538,8.014665,1.352356,0.254173,6.680651,4.880926,1.958826,-8.783934,7.916829,-7.168649,-1.909771,-1.326363,-4.405596,2.775136,-6.072259,-5.803598,0.897843,8.986463,-4.617116,9.003803,-6.452727,5.037720,-8.915996,-7.840783,-1.746174,6.520458,3.466567,3.801733,1.018437,-8.206663,-4.753471,-7.158093,-5.079960,-2.234229,-2.917351,-6.555159,-2.382106,-6.224902,-7.976674,-1.625015,-3.677966,9.285709,1.724300,7.054813,2.092020,6.002328,-7.823587,-0.274336,0.522320,9.056632,-7.885303,1.782071,-1.108733,3.521652,-6.308618,4.564535,-5.313800,-7.614641,0.950235,-9.874252,-6.795070,-2.535691,3.618959,6.847693,1.549229,-9.794671,2.796080,-0.373225,-5.953075,-6.055324,2.592376,7.251028,-7.479345,-5.987570,8.308395,-7.753012,-1.445675,-7.711227,1.983679,-4.554958,-5.691182,-7.600299,-4.956989,3.225411,4.665774,-9.521115,-0.830858,-7.297213,4.835864,-8.541103,8.577463,-2.552103,-1.499842,-2.810643,0.097983,-6.530208,0.517402,1.141801,-1.783833,-7.632243,-1.667221,-4.455650,-2.793452,8.219394,7.816781,-3.498547,-3.294413,-3.755648,9.856901,5.728700,-7.691021,8.071366,-8.235544,5.370670,7.157736,-6.812026,-2.772635,-9.033157,2.359537,6.564177,-5.673357,-8.349661,-6.575456,9.612032,1.453818,-4.848394,-4.037976,5.505583,-8.735651,7.456356,3.646687,3.459911,5.555716,-2.311904,6.429957,7.209783,-6.541796,5.782140,4.843082,-5.174055,7.812461,-6.375955,-9.530343,-6.113096,-6.657982,8.389079,-4.552356,-4.735451,-1.458708,-1.184219,-2.127760,0.634205,7.261958,3.976888,6.262039,0.902356,2.519508,7.126287,-8.705941,-9.832992,0.869088,-4.528681,5.812901,7.588619,4.871869,4.682807,-4.665351,-6.913446,5.855631,-2.617050,-9.829213,8.409187,3.399541,9.706031,4.528717,-3.632713,5.824000,-3.464992,0.227975,8.463277,0.235549,-5.158129,4.661826,-1.728259,0.268782,-2.192921,-8.263595,2.888786,-5.674370,6.806398,-9.204186,-9.097555,-4.087225,-7.869890,4.380736,8.285318,0.855397,-8.346251,-2.801744,2.428648,3.166906,6.269425,-0.368804,5.520262,-1.444109,-2.316584,-4.958957,-0.753971,6.266718,8.904836,-6.925225,5.479095,-0.887994,2.091659,-6.333768,-1.312766,-5.756919,-5.304372,-8.041575,9.515748,-0.208577,-6.673257,-9.977594,-1.033000,2.389131,-1.570803,-5.467921,3.040118,3.259818,0.673959,-8.830762,5.403067,-4.629195,1.975390,2.513431,2.855439,-2.930183,1.254667,-7.008047,-1.046736,2.836492,-8.069810,-0.409147,-0.692227,-9.350973,-1.812450,-8.352100,7.983533,3.896334,2.364731,0.288599,-1.436706,-1.943251,-4.039655,0.585511,2.127566,-4.815209,-6.844475,7.594203,-5.472442,8.291177,-3.817195,1.380145,-6.798797,-7.064292,0.682146,-1.395220,2.836960,2.655178,4.847632,-3.773750,4.987951,-5.179505,-4.611567,3.651532,8.540572,6.199509,-9.656744,6.822795,9.111353,-5.518108,5.012085,-4.898178,-1.251898,7.716282,9.538178,-5.160000,-6.224026,-9.725684,-3.804333,4.205524,-4.907234,-0.296471,1.994650,4.823006,3.935373,-0.577722,-8.879066,-4.792861,-2.605099,0.887182,0.965300,3.194348,-3.283084,-4.072929,1.234205,7.102573,-4.313802,-9.096614,9.777656,-1.432325,7.411910,-2.938000,-3.562283,-7.514314,-7.352795,-4.691242,8.139338,2.674215,1.457142,5.784019,4.197050,8.966676,-4.029522,-7.483809,3.890061,-0.979344,6.620385,4.634065,0.458121,-9.156509,1.594201,-7.184801,-5.712883,-7.120855,7.178902,-3.121047,-4.252267,9.801514,1.846893,6.132658,-1.810056,-0.204802,-8.926094,6.302016,8.317733,4.996812,-2.027163,-6.995499,3.235965,0.713932,-3.044487,6.449622,2.429047,4.576720,-6.377760,5.286427,-3.880307,-4.726677,1.345657,4.027792,-6.836438,3.455351,-9.141251,5.632632,5.750743,-3.478641,6.697591,-7.414055,-6.645934,6.965304,-3.246060,-7.496776,-3.359509,2.002858,-4.364946,0.049552,0.710172,-7.616476,-1.252562,0.947239,-6.948828,4.062079,-6.717480,-8.342609,2.729258,9.724975,-9.465372,-7.307241,9.722313,6.607270,-6.704931,-8.271887,2.981178,3.889055,-6.815781,8.627262,0.672899,-6.180609,5.822455,-2.002005,2.034708,-5.500977,3.709444,-6.463398,3.827352,5.881895,-4.339920,0.151461,-3.121518,4.893900,-6.104853,8.204716,9.526309,9.664113,-2.747512,7.105396,1.346753,0.855169,2.923535,3.340632,2.395178,-2.502603,-8.710205,-8.145046,7.952892,-7.140314,-0.957376,0.014742,1.310000,-3.817087,-9.817636,7.403787,-4.332407,7.502993,4.287724,-1.246609,3.934762,-6.688228,-2.473150,-2.817951,9.165976,2.271502,-8.026379,6.792624,6.973112,0.871373,-1.115667,-0.625699,5.498603,-1.930798,-0.670523,-5.652399,0.309741,-4.570192,7.453784,8.497805,9.268853,-2.481110,4.577917,3.412777,-8.228547,9.370642,-1.270580,5.934271,5.213937,-0.859499,-9.861613,6.346814,6.386547,4.835595,-3.191305,2.137808,-6.983371,7.269654,-1.266909,-5.641550,3.885865,4.848194,8.432262,8.702381,-0.697151,7.982554,-6.825107,-9.861294,-7.359728,-0.833495,1.685233,-7.016707,-7.490498,3.613821,-4.192655,0.130323,4.888682,0.764082,8.942496,9.687273,-9.996326,-8.279644,0.597745,8.781054,-3.369496,-4.019169,8.907953,1.616694,-9.595560,-1.057574,5.910787,-7.494211,-0.128820,3.779089,3.070122,5.311837,6.882101,-6.670359,3.170785,-9.057139,-7.436287,3.956990,3.398206,5.231555,6.032826,0.134455,0.454039,-3.512144,9.618855,1.397303,-4.978490,6.565789,-9.533086,4.629306,1.822251,2.842264,-0.014926,3.662725,-9.387464,-6.564670,3.976544,-7.825315,1.936090,-2.792133,-6.193716,1.119425,4.674607,6.485333,1.133761,0.120453,-3.891185,-7.507372,2.746326,5.437998,-6.822264,7.622902,0.231368,-7.810263,-8.791795,7.797393,-1.104543,-0.729999,9.189209,9.341363,-9.744632,0.066306,6.134271,8.243177,-5.992925,-6.384836,-2.173851,-8.491612,4.081741,0.488802,6.031873,1.449254,0.810199,7.389187,0.492500,5.442129,0.934519,-3.206026,-6.099663,7.347494,-6.972056,0.993113,-6.179973,-3.227020,-5.560468,1.948325,1.366649,9.144135,-3.568401,3.893666,6.789523,4.802451,-6.973960,-8.076803,-0.633713,4.311971,0.571769,6.994665,-5.421021,-2.465756,0.573041,-8.155318,-9.179780,-0.593750,7.433992,-8.929157,-3.103874,7.407526,4.001442,-8.101602,-1.647122,9.316246,-0.823518,7.083588,-5.841504,-7.615367,4.489186,-4.712898,-2.410179,8.461184,6.664313,2.173644,9.751369,-0.253802,-5.420350,-4.244765,-3.380299,-1.544602,4.250482,1.672560,6.290823,8.666794,-2.495111,-2.656450,-9.887590,-0.446280,8.983842,-2.080601,2.872438,-7.722415,3.864941,-3.653035,-8.863524,-4.843266,-4.482688,9.634110,7.819953,-5.096593,0.298445,2.867926,-9.120328,2.825017,7.013733,8.005386,-5.067345,-7.580508,-6.167625,3.976205,7.262821,-5.374984,3.976018,-2.207974,4.707960,-0.806925,2.327620,-6.189883,-5.875733,-5.356954,7.419595,-5.875192,1.575558,8.395238,0.728067,-1.817714,4.845661,-2.796086,-8.657657,3.001066,9.926950,-0.941550,4.245124,3.377215,-5.876250,9.228168,9.323099,1.139234,-7.305423,-4.752601,8.154023,7.817505,-1.002517,8.455357,-7.159151,-1.025630,5.237034,-0.618248,6.566447,-0.129230,2.469117,-4.772479,4.258484,8.516418,-0.211386,0.458251,-7.570978,-9.752975,-0.908321,-2.698808,2.321948,-8.358011,2.462459,5.870994,-3.628822,9.584711,-9.022112,-0.229341,6.676520,5.769977,-5.317835,-4.916810,0.082048,2.373887,-7.667174,-7.156548,-0.363169,-5.110366,-7.205600,-1.080658,6.874156,-5.181264,1.775560,0.155829,6.331680,9.925790,4.237842,-8.763194,-8.891700,-1.780500,2.173929,-2.209416,-3.393151,-9.804891,2.697446,6.364414,-7.057555,-3.355390,4.989255,-8.878085,-8.461039,-9.965419,1.646718,1.091000,-3.001472,9.247391,-4.218986,0.372696,-8.239369,2.054766,-1.313151,4.728277,2.065431,6.107714,7.505625,0.074986,9.865622,-8.248618,-7.494833,-9.090856,7.693979,2.385380,-2.943095,-4.982895,-1.813600,-6.902697,5.689965,3.445272,1.261236,9.997043,-2.743702,-1.359087,-6.374003,9.524623,-9.345735,5.672400,1.147583,-0.041756,9.559556,-3.620418,-5.023538,-9.711524,-4.168266,-4.998224,-4.847650,2.465710,-2.326913,-7.982875,-6.871506,-0.080968,-3.068550,-1.021487,-9.376611,7.249121,-8.035887,2.368007,-1.287771,-0.911622,7.790109,-5.618863,-6.670919,-4.210206,7.250630,4.365893,-5.345079,1.651231,5.721260,-9.677336,-4.708947,2.734504,-1.725218,4.510480,-1.495978,8.527701,9.028989,-9.892535,8.363277,-5.884501,8.228901,-1.094226,5.260731,-8.219542,-4.623791,-0.458385,-1.360146,5.530366,-5.183186,7.150657,-8.557084,-5.470087,-8.941839,3.550490,-6.278500,6.024723,5.491913,2.039934,5.880434,9.126633,0.337886,-9.865160,1.363239,-2.216034,-8.063477,-7.015768,-7.728666,-7.735586,0.044916,5.513008,-8.887805,-5.387301,-8.162656,-9.124315,6.022732,6.630126,-7.549990,0.626458,4.257853,0.535256,9.442942,-7.184222,1.942829,4.016676,-6.943483,-8.353603,0.072270,-7.139009,-3.949916,1.364983,-2.019805,-2.760855,-9.886431,-3.295738,0.749101,5.655617,-5.279089,1.167909,0.221880,-1.002542,9.914578,-3.244243,0.033060,-5.266210,0.324176,-2.517045,3.941878,-7.317311,-8.999916,0.747914,9.793370,-9.620965,6.335036,0.481745,-7.853469,-4.718663,-0.983211,-9.077121,-5.599143,2.784265,-9.461564,2.612868,3.508024,8.758083,8.739728,5.139073,-7.608878,-7.804254,0.825157,-8.508834,0.205131,2.283424,2.239302,-9.062737,6.778144,6.450068,3.385242,8.486604,3.750967,-2.738869,3.073463,5.490785,7.447903,4.978446,9.017866,5.347876,4.785167,-1.653243,-7.532771,-8.944508,-6.154469,-8.137348,-1.801451,-1.420290,-1.500530,-3.593411,8.429196,7.324150,1.214595,4.914351,-6.501959,-8.475082,-7.882662,-0.277901,6.890861,-4.889743,9.714557,5.890776,-4.175749,2.823677,-2.593639,-0.636118,3.109434,-9.813724,5.988444,4.809301,-2.899520,2.172760,-9.214593,-9.833794,-0.566029,8.976839,2.976030,6.366459,4.380650,-3.428655,9.570328,3.433229,2.557497,7.297867,3.323206,-1.970180,-1.149677,-1.125728,-3.679075,-0.737288,0.949676,-6.643763,-0.620724,-4.383153,-1.755103,0.726513,-2.706835,-9.370464,2.234728,-5.861595,-5.789048,-2.898454,-1.774469,9.267314,3.366398,7.776495,0.379408,7.223387,6.091204,1.419919,5.574876,1.668176,4.992614,1.443960,-1.907440,-8.405072,-3.154923,9.207560,0.138304,5.164525,0.124156,-8.089633,-3.578753,-4.773592,0.878804,7.890914,5.283515,-5.444617,-9.838981,7.102771,8.368843,8.040886,-4.753456,-7.413715,9.188148,8.431965,-1.894513,-5.095355,2.731568,5.645204,-7.627152,1.393564,4.501865,8.080472,1.224279,-1.355784,-3.221633,1.841073,1.686482,-0.897129,8.755740,6.366819,9.573455,3.698714,-7.152393,-9.534781,0.915939,-4.592218,3.141038,4.004157,-9.934730,-4.076805,2.353234,-0.458921,5.804394,-8.321547,-9.177117,9.800514,6.035511,-3.657016,9.156728,-5.710580,8.088859,6.559927,-3.929461,8.101878,4.763916,4.795224,2.176380,6.715928,1.885656,-0.115811,9.668596,7.965754,-3.398283,-2.119640,-5.227944,-8.074821,-0.647067,2.974780,-9.061660,0.640329,-3.763593,8.615496,-0.073821,-3.508828,-6.731283,7.988770,-2.660561,-5.979428,0.824018,-4.168158,5.924741,2.525270,8.658490,5.110582,5.274353,6.868952,3.474250,-7.844166,0.152950,4.631015,0.704704,1.966182,-1.384924,-3.443480,-4.402237,8.289020,1.680321,4.549682,4.514114,2.529889,-6.130082,-4.784180,9.000862,9.939864,-0.706035,-5.714982,-1.379813,3.406206,1.600100,-9.064274,7.511646,1.159551,-6.898043,7.822921,8.722643,-0.609043,9.056302,-6.487713,1.210920,3.689933,-4.539285,5.519064,6.997586,3.933449,-1.495217,-9.408116,-2.598681,3.176754,2.446539,-9.027657,7.527720,-2.033130,-8.506953,4.661108,-2.779222,9.235179,-0.197106,3.099655,9.527449,-4.156275,-4.155195,9.722174,-3.834261,9.680673,9.571592,1.626579,6.102952,6.857478,-6.153651,4.631435,3.448298,9.893164,-0.261564,2.366489,-9.905548,8.802147,9.677648,9.579060,4.868881,4.993146,-1.014969,8.410130,-5.896655,1.297371,3.839201,0.486167,2.021010,-9.603695,-4.264683,-3.930297,1.070264,2.365330,-4.620814,6.946203,-7.460868,8.857228,4.017090,-7.854521,3.492141,-0.204725,-9.001658], dtype = "float32")#candidate|10126|(2640,)|const|float32
call_10125 = relay.TupleGetItem(func_7316_call(relay.reshape(const_10126.astype('float32'), [2640,])), 4)
call_10127 = relay.TupleGetItem(func_7319_call(relay.reshape(const_10126.astype('float32'), [2640,])), 4)
func_4963_call = mod.get_global_var('func_4963')
func_4965_call = mutated_mod.get_global_var('func_4965')
call_10130 = relay.TupleGetItem(func_4963_call(), 4)
call_10131 = relay.TupleGetItem(func_4965_call(), 4)
func_7783_call = mod.get_global_var('func_7783')
func_7784_call = mutated_mod.get_global_var('func_7784')
call_10132 = relay.TupleGetItem(func_7783_call(), 0)
call_10133 = relay.TupleGetItem(func_7784_call(), 0)
uop_10142 = relay.atan(call_10130.astype('float32')) # shape=(72, 1)
uop_10144 = relay.atan(call_10131.astype('float32')) # shape=(72, 1)
bop_10160 = relay.bitwise_or(call_10125.astype('int16'), call_10130.astype('int16')) # shape=(72, 2640)
bop_10163 = relay.bitwise_or(call_10127.astype('int16'), call_10131.astype('int16')) # shape=(72, 2640)
bop_10182 = relay.not_equal(uop_10142.astype('bool'), relay.reshape(call_10132.astype('bool'), relay.shape_of(uop_10142))) # shape=(72, 1)
bop_10185 = relay.not_equal(uop_10144.astype('bool'), relay.reshape(call_10133.astype('bool'), relay.shape_of(uop_10144))) # shape=(72, 1)
output = relay.Tuple([call_10102,call_10111,call_10118,var_10119,const_10126,bop_10160,bop_10182,])
output2 = relay.Tuple([call_10103,call_10112,call_10120,var_10119,const_10126,bop_10163,bop_10185,])
func_10190 = relay.Function([var_10119,], output)
mod['func_10190'] = func_10190
mod = relay.transform.InferType()(mod)
var_10191 = relay.var("var_10191", dtype = "float32", shape = (126,))#candidate|10191|(126,)|var|float32
output = func_10190(var_10191)
func_10192 = relay.Function([var_10191], output)
mutated_mod['func_10192'] = func_10192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5234_call = mod.get_global_var('func_5234')
func_5235_call = mutated_mod.get_global_var('func_5235')
call_10244 = relay.TupleGetItem(func_5234_call(), 0)
call_10245 = relay.TupleGetItem(func_5235_call(), 0)
output = call_10244
output2 = call_10245
func_10246 = relay.Function([], output)
mod['func_10246'] = func_10246
mod = relay.transform.InferType()(mod)
mutated_mod['func_10246'] = func_10246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10246_call = mutated_mod.get_global_var('func_10246')
call_10247 = func_10246_call()
output = call_10247
func_10248 = relay.Function([], output)
mutated_mod['func_10248'] = func_10248
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5372_call = mod.get_global_var('func_5372')
func_5374_call = mutated_mod.get_global_var('func_5374')
call_10257 = func_5372_call()
call_10258 = func_5372_call()
func_10246_call = mod.get_global_var('func_10246')
func_10248_call = mutated_mod.get_global_var('func_10248')
call_10259 = func_10246_call()
call_10260 = func_10246_call()
func_8019_call = mod.get_global_var('func_8019')
func_8021_call = mutated_mod.get_global_var('func_8021')
call_10262 = relay.TupleGetItem(func_8019_call(), 1)
call_10263 = relay.TupleGetItem(func_8021_call(), 1)
output = relay.Tuple([call_10257,call_10259,call_10262,])
output2 = relay.Tuple([call_10258,call_10260,call_10263,])
func_10308 = relay.Function([], output)
mod['func_10308'] = func_10308
mod = relay.transform.InferType()(mod)
mutated_mod['func_10308'] = func_10308
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10308_call = mutated_mod.get_global_var('func_10308')
call_10309 = func_10308_call()
output = call_10309
func_10310 = relay.Function([], output)
mutated_mod['func_10310'] = func_10310
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10320 = relay.const([[[4,3,-4,-2,-5,10,6,2,9,5,-7],[10,5,-6,-4,8,-4,1,6,-7,-4,-7],[-1,2,-8,-2,10,-7,-7,-7,-6,7,8],[8,-1,6,-3,8,10,2,10,1,7,-6],[-8,3,10,4,10,-1,-8,-10,8,5,-9],[7,2,-9,5,5,-10,9,-2,7,4,7],[-5,-3,5,4,-6,3,-7,8,2,7,-4],[4,-9,10,-9,5,1,10,7,-2,-2,-2],[-9,-3,4,5,-8,5,-7,3,9,-1,-8],[-8,4,-10,7,5,2,9,8,5,-10,-5],[5,-5,6,7,-9,-8,7,7,-10,1,10],[8,-1,-6,-5,-10,-9,-5,10,-8,10,-2],[-6,2,3,7,-3,-3,-10,-7,-2,-5,1],[5,-5,2,8,2,-5,1,-10,-1,-5,-7],[-5,-10,-1,-7,7,4,4,-7,10,-8,6],[10,10,-8,8,-10,2,-10,-8,-5,-9,-7]],[[7,-5,3,-1,-5,-4,-4,9,-10,3,-2],[-4,9,5,2,-1,6,-3,3,10,7,-2],[8,1,10,-9,8,-3,7,-7,10,8,-5],[-6,7,8,-2,2,-2,8,-8,4,-4,-3],[7,-2,7,2,10,-2,-4,8,-1,-5,-3],[4,-4,7,7,1,-9,10,2,8,10,9],[-10,-1,7,-3,1,-4,-6,-4,-3,5,-9],[-6,7,-3,5,4,-8,8,10,-10,7,-7],[6,-5,8,9,-5,8,-10,-10,4,-2,-8],[2,2,-3,3,-1,3,8,-6,-9,-1,-4],[10,3,9,-8,6,8,-9,8,-1,3,-4],[5,5,2,1,-4,-3,4,-4,10,-10,9],[-1,3,5,8,-6,-3,7,6,3,-6,1],[-8,-2,-9,9,4,-7,4,3,-3,-6,-10],[2,-8,10,-1,6,7,10,-2,6,-10,3],[4,7,4,4,6,-4,2,2,6,-5,-8]],[[1,-3,-4,-9,-9,2,2,1,4,3,4],[3,-1,4,3,10,-1,-10,-7,3,-4,4],[-5,-2,-4,6,-10,-4,7,6,9,4,8],[7,5,-1,-5,4,2,8,9,-4,2,-2],[7,10,4,7,10,-9,-4,-3,-9,-10,1],[9,-1,-2,2,-5,-4,6,-9,-1,-7,-3],[3,9,-2,-5,6,-6,-6,1,4,8,10],[-5,-6,-7,1,3,7,5,2,6,-3,-6],[-1,-6,2,-3,7,3,-6,-8,2,10,5],[9,-7,-7,7,9,10,-3,3,-5,5,6],[8,-8,-7,-8,-8,-2,-3,-7,-10,-8,-6],[-3,8,9,-5,5,-1,4,5,-10,2,-10],[-1,-5,7,-3,6,-2,-3,-6,-10,-4,3],[-8,-3,-1,-2,-7,-10,-6,-8,10,5,6],[4,8,2,4,-1,4,-3,-6,8,10,8],[6,2,-7,9,5,-5,7,7,3,-6,-10]],[[3,-5,-3,-10,-8,-6,2,9,9,5,9],[3,7,-3,-4,1,-3,10,-1,7,-7,-2],[-8,-10,-7,3,1,1,2,1,9,5,10],[7,6,-1,-5,-1,1,10,-8,-3,8,7],[2,-6,-1,2,-6,3,1,4,4,-10,9],[-5,4,-8,-4,2,4,-6,9,-6,-8,-9],[-2,8,-8,-3,10,-8,5,-9,-2,4,9],[4,-9,6,-1,8,-6,9,5,-5,-7,-1],[8,3,1,9,-9,-1,-5,-10,2,10,-4],[-3,9,6,-2,10,7,3,3,9,5,4],[6,6,10,5,-5,3,-8,-1,5,2,7],[9,7,3,7,4,9,-1,-6,-5,9,-6],[-8,-7,2,-5,5,10,4,-4,1,8,7],[-1,8,-5,-5,-3,-10,5,2,-3,-8,6],[8,-4,-7,-1,2,9,-9,6,-7,-6,-1],[-1,5,-9,8,-4,7,-5,10,9,7,1]],[[-4,9,-10,-10,-10,-4,-4,-7,-2,9,6],[-4,-10,-8,2,-3,10,8,1,-1,-9,-5],[1,7,2,1,-10,6,-9,-6,-8,7,-3],[8,-3,4,-5,6,2,7,9,-3,4,-8],[-6,6,-3,1,-8,-9,-9,4,1,-10,-3],[-8,7,-3,1,-6,8,-10,-4,7,4,-6],[9,7,-10,-5,-5,7,-2,-7,-4,1,-6],[4,-6,6,9,2,-2,9,7,-6,7,-8],[-4,4,-7,-9,-8,5,-6,-1,-2,2,-4],[-5,7,5,3,-2,8,6,-3,-10,-9,-2],[-5,9,-7,-9,-6,-2,-6,-4,10,-7,-4],[-4,7,7,-9,3,3,9,-5,-3,-5,-3],[-9,1,4,8,10,-4,-5,4,-1,8,-9],[6,-5,4,-3,10,-5,-3,-8,7,-4,4],[-4,-3,-5,3,-8,-7,-9,5,-9,3,-8],[3,7,2,2,1,6,3,9,-5,-6,-1]],[[7,-4,-3,-2,-5,-6,4,-6,-6,4,-2],[-5,-4,7,-7,2,6,-2,-5,1,9,2],[7,-2,4,-5,5,-9,-2,-9,-7,-1,-9],[4,-7,-3,4,2,5,4,-1,8,-1,-7],[3,10,-8,-3,-5,-2,5,1,-3,1,-8],[-9,-6,-9,4,-7,-3,-5,7,-10,6,-5],[7,10,-10,8,-8,8,-4,10,-4,-4,-4],[-10,6,5,9,-3,-7,-6,6,4,-1,-9],[-1,2,5,-4,5,-2,-3,-5,9,1,-2],[3,-1,3,1,-8,8,2,7,4,2,-5],[5,1,9,-1,9,9,3,3,-4,8,2],[-7,8,3,9,6,7,1,-7,4,-8,-7],[7,-7,-2,2,7,-3,3,4,3,8,-5],[-5,-1,10,4,-2,-7,1,-4,-3,6,-5],[-3,1,-8,5,7,-8,9,-8,7,-5,9],[-6,-2,-5,9,5,10,8,-6,3,-5,2]],[[1,8,-9,4,10,2,-9,8,8,9,-3],[6,-4,-3,-10,-4,6,-10,-4,3,-4,-5],[2,2,1,8,2,3,4,4,2,6,-9],[-3,1,-6,10,2,7,4,7,1,-7,-5],[10,-5,-7,-10,-7,9,6,-7,-9,2,2],[3,9,9,10,-7,3,-3,-2,7,4,1],[1,10,-4,-5,10,6,-4,7,8,4,-7],[2,-2,1,4,9,8,5,-4,10,10,7],[-2,-8,10,2,3,-7,4,10,-9,-5,-10],[1,-3,-10,-9,-7,-3,1,-10,-1,10,7],[-5,4,-8,3,9,2,4,-5,2,4,-8],[9,2,3,9,6,7,-9,8,10,5,9],[7,4,5,-3,5,-3,3,8,5,5,3],[4,-6,-9,10,2,-10,-5,4,-8,-3,7],[6,-7,9,-3,-5,-4,-3,2,8,1,10],[-3,-5,7,-3,-5,10,-1,3,1,-3,1]],[[-7,9,8,-5,7,5,10,-1,6,3,-7],[5,10,-10,-3,9,5,-7,-10,-3,4,-9],[10,9,-6,-10,-1,-3,-2,-4,-1,5,2],[10,6,-7,9,-5,7,-5,-8,-6,-1,-10],[9,6,-6,7,-4,-8,-8,1,4,-8,-1],[4,9,8,8,-1,-1,-8,-1,-5,-1,5],[1,-9,-1,-5,-10,-2,10,7,10,-6,8],[-8,-10,3,-7,1,2,10,-6,8,6,5],[3,-8,1,-4,10,9,4,-1,8,-6,1],[8,2,5,7,8,1,3,-9,-2,-6,9],[3,-10,2,-5,-3,-2,10,-7,-5,-7,10],[-10,-4,6,-5,1,-4,3,8,-9,-3,-7],[8,2,-8,2,8,7,-6,5,9,-3,8],[9,6,-6,-10,-3,-7,-4,1,-5,9,2],[-4,-9,2,3,8,3,-1,2,-4,-10,8],[-7,1,10,3,-5,9,-7,-6,9,6,5]],[[-5,-9,-1,-9,4,-8,10,-4,9,10,-3],[-9,9,10,-1,3,3,-4,-10,3,-3,-8],[8,5,-9,-7,2,-1,3,-8,-10,2,-2],[8,-1,5,-2,6,5,9,-6,8,2,1],[-3,-2,10,6,10,6,-5,-5,6,-6,1],[-4,-4,5,2,-1,-4,7,7,-8,9,8],[8,10,-3,6,-4,10,-3,-3,-10,-1,7],[10,3,-1,-5,6,-10,-9,5,-8,-4,-8],[-3,3,5,-10,1,-6,-10,-7,-6,8,9],[9,-1,-2,5,-5,1,6,9,8,-7,-4],[-3,-2,6,-5,9,1,-2,6,-3,8,8],[-1,9,7,-6,-5,-4,8,-8,6,-6,7],[10,-5,-4,-8,-8,-9,8,5,1,-3,-6],[4,3,-9,-7,-8,2,9,-8,-8,5,5],[7,7,9,-2,2,-7,8,-5,4,1,7],[-2,6,-3,-9,-4,8,4,-3,10,-2,10]],[[5,-4,-9,5,-6,4,6,5,-8,4,10],[3,2,-9,-4,-4,-4,-10,-5,2,-1,-5],[4,4,1,-7,-6,4,-8,4,-2,3,-9],[1,-9,7,-7,-8,-4,-2,2,6,4,8],[3,-5,10,-10,-2,-7,2,-2,-8,-2,7],[-9,-7,-9,-5,4,8,-2,9,9,1,-6],[-10,3,-1,2,1,6,-6,-9,-9,10,4],[6,-4,-7,-1,-9,1,10,-9,7,4,7],[8,5,-9,-5,-7,-6,-5,7,6,-6,-9],[9,9,-9,-1,6,-2,-7,8,-6,2,-7],[7,-5,-1,1,9,10,-8,-4,-5,8,-3],[-10,6,5,8,-9,5,7,6,8,10,5],[6,6,-10,-9,-1,4,-7,-7,1,9,9],[4,5,-1,9,-4,-5,-6,-7,8,6,-7],[-8,-7,2,7,-5,7,4,-7,-5,-7,3],[5,-10,8,-2,-10,-1,3,4,-7,2,9]],[[3,10,6,8,3,-9,-4,-1,-6,-1,10],[2,-4,3,2,-4,7,-3,-1,4,2,-9],[2,5,4,7,-9,-6,-6,1,-10,-5,8],[3,8,-5,3,-9,7,5,1,5,-8,3],[1,-4,-10,9,-6,9,-10,-4,-2,9,8],[-3,5,7,9,7,-5,-3,9,-4,4,7],[-2,8,6,5,1,-1,6,-10,-9,6,-10],[-10,1,-4,-9,-1,-3,-5,8,3,10,8],[3,2,6,7,-7,7,-10,4,-3,2,-4],[7,9,-1,-5,2,8,-9,1,2,-2,7],[3,3,6,4,-4,-4,-4,-9,-6,6,-6],[8,-2,9,-3,-7,-10,2,6,8,10,3],[8,2,7,-10,6,2,10,1,-10,2,9],[-5,-2,6,-6,-8,3,10,10,2,-10,4],[-8,5,-3,5,1,-8,-5,-8,5,5,6],[9,7,-1,-10,7,10,-5,7,7,-1,4]],[[1,-5,6,6,7,-7,9,-9,5,-6,-8],[-9,2,-4,3,9,9,-10,-5,-6,-4,-7],[3,1,-2,6,-9,-6,3,5,7,9,9],[-1,-10,9,2,-6,-3,-4,7,6,6,-8],[-1,4,9,4,-5,-4,-1,-8,8,9,-4],[-8,-4,-6,6,7,8,-7,-5,7,-7,-4],[4,3,-5,-5,5,9,-10,8,-2,5,-8],[-9,5,-4,4,3,9,10,-6,4,-8,1],[-9,-6,-5,1,5,-6,-3,-5,8,5,-1],[3,9,1,10,7,-10,-8,-4,-8,-6,-1],[5,-8,-1,-2,7,2,-5,-5,-4,4,-5],[-10,-3,8,-3,10,5,4,-10,-8,4,-5],[4,1,2,1,10,-8,10,-2,-5,2,10],[-5,2,9,5,2,4,7,-3,-5,10,5],[9,2,2,5,-9,4,4,-7,7,-10,7],[9,4,2,-9,-3,-4,2,10,-10,8,10]]], dtype = "int64")#candidate|10320|(12, 16, 11)|const|int64
const_10321 = relay.const([[[-9,4,2,-7,5,-3,8,8,1,-9,1],[5,-6,6,-6,-5,-1,-4,-5,1,8,10],[-1,9,6,-10,-6,4,10,1,-10,10,5],[2,6,2,7,-7,10,-2,-6,1,9,-5],[-7,4,3,7,-7,-10,4,4,-1,2,1],[-8,-8,10,-6,8,-9,1,6,2,8,-6],[-3,6,5,7,-3,2,4,3,-7,3,1],[10,1,3,-5,4,3,-3,-9,4,-3,-5],[10,-7,9,5,-2,-9,6,-6,3,8,-9],[6,-9,-10,-9,-1,5,6,-6,5,-5,-4],[-8,-3,-10,9,-1,-9,-7,7,6,-7,-6],[6,-3,1,-7,10,-5,8,-3,7,4,-8],[-5,-9,3,-5,-10,-10,-3,-2,7,-6,6],[-8,-9,-4,-10,-5,5,5,3,-6,10,7],[-6,4,2,6,1,6,-10,4,1,3,7],[-6,10,1,-8,5,-9,9,-8,9,10,1]],[[4,-10,-7,4,2,4,2,4,-6,-5,-8],[6,1,7,-9,-3,-6,-1,-7,8,-7,-3],[-8,10,-8,6,-1,-3,-8,-4,-9,-1,2],[-7,-6,-10,5,-3,-10,6,-8,-5,-7,-1],[-1,1,4,4,-3,-6,-5,-4,-8,5,10],[10,-6,-6,5,7,2,7,-9,5,3,-2],[6,1,3,-5,-9,-2,10,-7,5,3,9],[5,-1,9,2,4,-9,3,3,6,3,-7],[4,-9,8,-8,2,-7,6,8,-7,-5,9],[8,-7,4,-2,2,6,7,-5,-3,10,1],[3,-1,4,-9,-5,-5,-3,2,-1,-3,8],[-1,5,-10,-1,1,2,8,-10,-9,6,-9],[4,-4,8,1,9,8,5,9,3,-4,3],[-1,9,-10,-5,-5,10,1,7,3,4,-10],[-1,7,-10,-9,4,-6,1,9,-4,-4,-4],[-10,6,6,7,1,6,4,-10,1,-4,-9]],[[2,10,2,10,-8,6,-6,-6,-10,-10,6],[6,-6,1,3,-6,6,1,-9,-4,1,-5],[-2,-9,7,-3,-3,10,-4,-1,1,-2,-3],[-4,3,-3,8,3,-6,-4,-10,-9,-6,4],[10,-6,3,9,-10,2,3,-8,-1,2,-3],[-2,3,-8,10,8,-9,2,-2,-10,4,-6],[7,-7,-6,6,5,-2,1,7,2,-3,10],[3,-6,4,6,6,-3,2,2,-7,-7,-5],[-9,-2,-8,1,2,-1,8,-10,-3,-10,3],[-6,-9,2,-1,4,9,-10,3,-6,5,5],[3,10,6,-4,9,2,4,3,8,7,3],[6,-9,1,10,-7,-3,-10,-6,-6,8,-2],[1,-10,-3,8,-6,-2,-7,-7,8,9,-3],[-10,7,2,3,10,9,7,-8,-8,9,7],[2,2,-2,-3,4,-1,-9,-6,9,10,-5],[10,2,-8,-7,-7,-3,-8,2,7,7,8]],[[-1,10,-10,7,-5,-1,-4,-8,-5,9,5],[-10,-1,4,-5,3,9,-5,6,-6,-1,-10],[7,-6,-2,-2,-2,-6,9,10,4,-1,9],[-2,10,-5,-9,5,-2,10,-6,3,-5,1],[-10,-10,-4,-5,-7,-9,-9,9,9,3,9],[-7,4,-2,-8,-4,4,3,5,3,7,10],[-6,1,6,-9,7,-9,6,1,2,2,-7],[4,-5,3,-8,-7,5,2,-3,-6,6,3],[-7,-6,8,-5,-5,9,5,-3,9,9,-9],[7,3,6,1,1,-4,4,-9,8,-7,3],[1,7,5,3,-9,9,4,-3,-5,-2,3],[10,7,5,7,6,-5,5,10,-5,-8,5],[10,-8,2,3,-6,-7,-10,-6,2,4,-6],[-7,-9,-9,7,-3,-10,1,9,-7,-6,9],[-9,-5,-7,-8,8,-3,-8,-5,6,1,9],[10,-5,-4,-5,8,-7,5,-10,1,10,4]],[[-8,-2,-9,2,4,-5,-1,1,1,10,-10],[4,-9,9,-10,-7,4,-3,-2,-8,-7,5],[-1,5,-6,1,-9,-8,-1,8,-2,10,-4],[-8,7,3,10,-3,-6,4,-3,-10,2,-3],[-6,6,7,1,-8,8,-6,1,-8,-6,3],[6,7,-10,-5,3,5,-7,-7,6,9,3],[4,1,8,-8,-1,9,-2,6,4,-9,1],[5,-6,5,4,1,2,4,3,-3,6,-10],[-4,8,-8,-1,2,-8,5,-2,-3,-1,-6],[5,6,-2,3,-3,-10,7,5,-8,-1,5],[-2,-9,9,10,-4,5,-4,-4,-10,-3,7],[10,-7,-1,7,-6,-1,5,-4,7,9,-8],[8,-1,-9,7,-6,8,-5,2,2,-2,3],[-5,2,5,-4,6,4,-8,-2,9,-4,-9],[-7,-3,-9,4,-2,-8,-2,6,5,8,7],[-4,-3,-7,1,5,9,7,-3,-1,-1,-9]],[[-10,-9,-5,6,-4,-3,3,-1,-7,10,-4],[-5,7,2,-5,-3,6,-1,10,4,-6,-1],[8,3,10,-5,-10,3,-8,-9,6,7,-5],[-4,6,1,5,-2,5,2,9,-2,-8,8],[2,9,9,-1,-6,1,2,-5,5,-4,3],[6,1,-2,-6,7,10,-7,1,5,-4,-9],[-10,5,-2,-4,3,8,1,-5,4,5,7],[5,10,5,-8,-10,9,-4,4,-7,-9,1],[6,-4,-7,4,-1,-1,-9,-6,-1,5,-4],[10,-6,-3,1,-4,-1,5,7,9,8,-10],[-6,-4,-5,-6,8,6,-2,-7,-4,-10,-1],[-2,-6,-8,-3,-1,-7,6,6,2,8,5],[9,-3,-5,10,9,6,-7,10,-5,10,8],[7,-10,5,8,-7,4,-2,2,6,-7,7],[-7,5,9,-5,1,-10,-10,8,7,-5,-5],[3,-10,-9,1,9,2,-9,9,-8,5,-1]],[[5,5,5,6,-6,7,5,-10,-3,-4,3],[8,7,-2,5,1,5,3,-3,-9,-7,-4],[-6,1,-3,4,10,8,7,-2,-7,4,9],[1,-8,1,-1,-2,-9,-6,-9,8,4,9],[-10,-6,5,9,9,6,-2,-5,-1,-10,1],[3,-6,-9,1,-2,8,7,7,-7,-6,4],[-9,-1,-7,3,6,-7,-8,-3,-4,-1,-2],[-10,-4,7,-8,-10,-1,9,3,-3,-7,9],[7,-6,6,7,-6,1,4,4,9,10,6],[-6,-9,-7,-1,2,8,-1,7,-6,-7,-5],[-3,4,4,1,-3,-8,-8,-9,-1,7,10],[8,7,10,-9,6,5,-5,4,-6,5,-9],[9,9,10,-9,-3,-10,1,8,-7,5,6],[9,-7,7,9,2,6,7,-7,-8,5,5],[-8,-7,9,6,-1,-7,10,-10,-2,8,-6],[-3,3,-7,9,-6,7,3,5,-1,-4,7]],[[-2,2,1,-1,-5,10,-6,-6,-9,6,-6],[-1,-8,-1,3,-6,-5,1,8,-3,-6,1],[-9,9,-1,-3,-5,10,-7,8,9,6,-2],[-1,9,-1,8,9,9,5,-4,-7,-1,2],[9,9,-4,3,-2,-6,2,-5,9,8,-1],[-8,-9,2,3,9,6,2,-3,-7,3,3],[9,4,10,-8,4,6,2,-3,-3,-8,10],[-10,7,7,9,3,-8,9,-10,-10,4,8],[-3,-2,-5,5,2,-10,3,9,9,-3,3],[-8,-9,-7,-2,9,-8,-2,-3,2,-6,-4],[-2,-2,-7,10,7,2,6,-6,-8,6,6],[-1,-8,-4,-7,-3,3,10,10,-1,9,4],[-5,-6,5,-1,9,-10,6,1,-4,2,10],[9,-5,-9,-4,-2,3,-3,9,1,-7,6],[9,-9,-10,2,7,1,10,8,3,2,-7],[6,1,3,2,-3,5,-4,5,4,-5,-7]],[[5,8,5,-5,7,6,1,-3,-9,2,10],[-8,1,-8,8,-1,1,10,1,8,-9,3],[-6,-10,5,-6,7,-10,7,-5,5,8,5],[-2,5,2,6,1,4,-6,5,-1,-7,3],[3,9,-3,-4,6,5,-7,7,-4,7,2],[-6,9,-1,10,-2,-9,-1,-9,1,10,-1],[4,-2,8,8,-7,9,2,2,-4,-7,7],[-7,2,6,-5,10,-6,-2,4,-6,-4,6],[-7,-10,-5,3,-6,2,10,9,-6,-5,-1],[-7,-6,-5,10,-6,2,-5,6,10,-10,-9],[8,-6,-7,7,9,-5,8,5,1,-4,-9],[9,1,-7,-2,1,-6,-6,-9,3,8,-3],[9,-4,-9,-5,-9,6,-6,1,1,7,9],[2,-8,-6,-4,3,-6,6,-7,-6,7,-6],[-8,10,9,9,-3,-7,-8,5,3,7,-7],[5,-4,-10,-4,4,1,3,1,9,-3,-3]],[[9,-4,8,-2,-6,8,-9,-1,-7,6,8],[10,-9,1,5,-4,-4,9,-2,6,7,8],[-6,-8,3,-1,-3,-8,9,-4,-5,-9,7],[-10,8,-6,2,10,10,-1,3,-4,4,-9],[-5,-7,3,9,3,-8,-7,-5,-8,-9,2],[1,-3,-2,-1,7,-5,-6,10,8,-7,4],[1,-3,2,-7,-3,2,7,10,-6,-2,3],[7,5,9,-2,-6,-2,-3,-2,-3,-1,8],[10,4,8,4,7,-7,7,-4,8,-3,10],[7,6,-6,4,5,-3,9,-6,-3,4,-5],[7,-1,9,7,2,3,5,-5,5,-2,-8],[2,-4,8,4,-1,3,7,-10,3,-10,9],[6,-4,-5,-1,-9,-8,-7,-3,10,-3,-9],[-6,3,-8,8,8,-3,-6,1,1,10,5],[6,8,3,10,2,-1,-5,-7,8,8,-10],[-8,-2,4,-8,9,8,-1,-9,-5,5,5]],[[6,-5,-1,-6,7,-3,4,-3,6,-8,9],[5,8,-10,-5,5,1,6,4,3,9,-2],[-3,5,7,4,-3,-8,9,4,-5,7,-10],[7,6,-5,6,-8,-4,-10,6,-1,-5,10],[6,-9,-2,8,9,5,-5,-10,10,2,1],[-5,8,-8,4,6,-9,-5,-9,-4,-8,6],[9,-6,4,-1,10,3,-3,-10,6,-8,-8],[7,-4,8,10,-7,9,-8,-9,-7,-6,-8],[1,5,-3,4,4,1,-2,1,-4,-9,-10],[-6,-7,-2,5,-1,8,-6,8,4,-9,1],[-5,-3,3,-4,10,-5,-4,7,7,-10,5],[7,5,-5,-8,6,-3,6,3,-10,-9,8],[-2,-7,-5,5,2,-1,-5,1,-7,1,-8],[-5,-7,1,-1,-1,6,-3,4,8,2,-1],[8,-4,-1,-4,-2,-9,5,4,9,-1,1],[5,-4,1,4,6,-4,-6,5,-5,10,-5]],[[3,1,5,6,-7,-1,-4,8,-4,2,7],[6,-10,1,2,5,7,9,9,8,-8,7],[-3,2,1,9,1,-8,-4,-9,6,4,-9],[3,-8,-3,2,-8,5,4,1,-2,9,-3],[10,1,-5,7,-8,3,-3,-4,-6,-10,2],[7,-7,8,-10,9,3,5,-7,-6,-3,2],[-3,1,-9,-10,-4,6,5,-7,5,2,6],[-7,-10,-7,-2,-10,-5,6,-5,7,-3,-3],[7,1,4,1,3,-2,-1,-7,-9,-7,10],[-10,-10,-4,-10,-9,-5,-2,-6,-10,10,-1],[2,-5,-4,5,6,9,-2,8,10,-2,10],[5,-6,-4,-8,9,-10,8,7,-8,-1,-10],[9,-7,-7,-3,3,-2,4,5,-2,1,1],[8,5,2,2,-6,-1,-10,-2,-5,5,-3],[-5,1,5,1,-1,3,-2,9,8,-7,-10],[9,-1,8,4,-5,2,-8,7,-10,-6,-4]]], dtype = "int64")#candidate|10321|(12, 16, 11)|const|int64
bop_10322 = relay.add(const_10320.astype('int64'), relay.reshape(const_10321.astype('int64'), relay.shape_of(const_10320))) # shape=(12, 16, 11)
output = bop_10322
output2 = bop_10322
func_10344 = relay.Function([], output)
mod['func_10344'] = func_10344
mod = relay.transform.InferType()(mod)
mutated_mod['func_10344'] = func_10344
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10344_call = mutated_mod.get_global_var('func_10344')
call_10345 = func_10344_call()
output = call_10345
func_10346 = relay.Function([], output)
mutated_mod['func_10346'] = func_10346
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5939_call = mod.get_global_var('func_5939')
func_5941_call = mutated_mod.get_global_var('func_5941')
call_10368 = func_5939_call()
call_10369 = func_5939_call()
func_4963_call = mod.get_global_var('func_4963')
func_4965_call = mutated_mod.get_global_var('func_4965')
call_10375 = relay.TupleGetItem(func_4963_call(), 2)
call_10376 = relay.TupleGetItem(func_4965_call(), 2)
func_6480_call = mod.get_global_var('func_6480')
func_6482_call = mutated_mod.get_global_var('func_6482')
var_10386 = relay.var("var_10386", dtype = "uint64", shape = (2288,))#candidate|10386|(2288,)|var|uint64
call_10385 = relay.TupleGetItem(func_6480_call(relay.reshape(var_10386.astype('uint64'), [2288,])), 0)
call_10387 = relay.TupleGetItem(func_6482_call(relay.reshape(var_10386.astype('uint64'), [2288,])), 0)
output = relay.Tuple([call_10368,call_10375,call_10385,var_10386,])
output2 = relay.Tuple([call_10369,call_10376,call_10387,var_10386,])
func_10413 = relay.Function([var_10386,], output)
mod['func_10413'] = func_10413
mod = relay.transform.InferType()(mod)
mutated_mod['func_10413'] = func_10413
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10414 = relay.var("var_10414", dtype = "uint64", shape = (2288,))#candidate|10414|(2288,)|var|uint64
func_10413_call = mutated_mod.get_global_var('func_10413')
call_10415 = func_10413_call(var_10414)
output = call_10415
func_10416 = relay.Function([var_10414], output)
mutated_mod['func_10416'] = func_10416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7577_call = mod.get_global_var('func_7577')
func_7579_call = mutated_mod.get_global_var('func_7579')
call_10418 = relay.TupleGetItem(func_7577_call(), 0)
call_10419 = relay.TupleGetItem(func_7579_call(), 0)
func_3104_call = mod.get_global_var('func_3104')
func_3108_call = mutated_mod.get_global_var('func_3108')
var_10463 = relay.var("var_10463", dtype = "int16", shape = (8, 28))#candidate|10463|(8, 28)|var|int16
const_10464 = relay.const([-10,5,-3,9,-10,5,10,-7,-10,2,6,-7,1,-1,10,-5,10,8,4,5,4,10,-7,-6,1,-8,-1,1,9,-4,-8,1,7,-1,5,-7,-9,6,5,2,-1,1,7,5,-6,7,5,1,-5,7,2,2,2,-7,9,2,-2,-1,7,-7,4,6,-1,-5,1,8,-5,-3,8,3,9,-7,-2,-10,-6,-3,-2,-2,-6,-1,9,10,-10,1,5,7,-1,7,-7,-2,7,-3,-4,1,-4,-9,-2,4,-6,-1,-1,8,-5,7,3,2,5,-8,4,1,2,8,-2,5,9,10,-4,-2,-3,-8,-8,-6,-8,2,-4,8,4,7,10,2,7,9,-10,10,-2,2,9,-3,-2,8,9,-9,6,6,9,-7,-2,10,9,-9,-8,-1,9,-5,10,-5,1,-9,-2,-5,5,-7,-8,2,7,-10,-2,-2,-6,10,-10,4,-10,10,-10,-1,7,-5,-7,4,-8,-8,7,9,-9,-9,3,2,-8,5,9,2,-6,-3,-4,8,3,-2,8,-6,-10,7,10,-9,4,-6,-2,9,5,-2,8,3,-5,-2,4,-1,-4,-10,-8,1,-4,6,-5,-3,-8,-3,4,10,9,-4,1,-1,-2,7,1,5,-7,1,-8,6,9,2,3,3,-3,7,2,9,1,7,6,-7,-3,-6,-3,4,-10,-7,8,7,9,-7,3,7,10,6,-6,-10,1,9,-10,10,-1,5,7,3,9,8,-4,8,1,-3,-8,5,10,-7,-6,10,-2,-9,10,-6,1,-3,-9,2,-6,6,-7,5,-6,8,7,-1,7,-7,-3,-6,-7,1,9,-7,-6,8,7,-1,-4,-6,8,-10,-9,-10,10,-7,6,-4,-1,9,-5,3,2,4,4,9,-7,-5,-7,-9,2,5,-5,-10,-1,8,-9,7,-6,9,9,1,8,2,-10,2,10,7,-8,6,9,-5,-6,2,-1,3,1,-8,8,6,-3,-10,-6,8,4,-3,-7,-3,-9,6,-6,-2,1,-9,9,8,4,5,-3,-5,-9,1,-7,1,-9,-7,-6,-3,-8,7,-6,9,3,1,9,6,-4,-5,3,-8,3,-7,-6,-7,5,-2,-10,-2,-7,10,6,-5,3,3,6,-8,7,-9,8,-7,-1,-3,-10,-4,7,-4,-10,-5,-6,8,-8,-10,-2,7,-6,-2,-3,-8,9,1,-7,-10,3,9,2,3,6,6,-4,-7,-9,-7,-5,9,-8,1,-5,-2,6,10,-1,-9,-8,-4,-2,-3,9,5,-5,-7,5,8,-8,-10,2,-2,5,-9,-8,7,5,3,10,-7,10,-9,5,-5,-8,7,7,4,-5,-8,7,5,5,-5,3,3,-9,8,-8,6,10,-5,-5,2,3,2,-3,-1,2,7,-9,1,-1,-1,-6,6,-10,-4,1,4,-5,-3,5,9,9,5,6,-5,6,7,-2,-7,-5,9,8,9,4,-4,-5,6,-8,-3,8,-3,-5,8,5,-2,-8,-4,6,10,5,-9,-6,8,10,10,1,-4,-6,-6,8,9,10,-2,9,8,-5,-8,-4,7,-6,-1,2,3,-8,7,6,-1,3,3,-7,-8,8,5,2,5,9,-5,1,-9,9,-4,3,-1,9,10,7,-10,6,6,-5,6,-6,7,10,-6,-3,6,-4,-4,-3,2,-2,2,6,-6,10,9,2,3,1,3,-10,1,5,8,8,5,-2,10,8,1,5,-6,-5,8,-10,1,9,-3,-5,-2,1,-5,-8,-1,10,-4,1,1,-9,-3,2,-9,3,-9,3,5,1,-6,-4,5,10,-8,-1,6,-10,1,10,4,9,6,-5,5,1,-6,10,-9,-3,9,6,6,-2,-7,-4,-8,6,-5,2,-10,-9,8,-10,-10,-5,-8,4,-8,-10,9,-8,7,10,7,-1,-7,-5,-2,3,9,10,-1,-3,1,4,9,8,7,9,-1,3,1,-4,-3,4,7,1,-6,-4,10,-6,1,-7,1,-6,-6,-2,-7,1,-5,3,-7,-9,3,-10,5,-3,10,-7,-8,5,2,-3,6,-8,-7,5,9,6,9,-4,4,1,9,-4,10,1,7,-10,5,3,1,7,2,-2,1,-5,3,-8,-3,9,2,-7,1,-9,5,10,10,8,1,2,3,-7,-1,-1,7,-2,-8,-5,6,7,8,9,-5,7,-4,7,6,6,-9,6,6,3,4,-3,4,2,-9,7,8,9,-6,-1,-10,-10,5,5,3,-3,7,-7,-8,-2,-10,1,6,-1,-4,-3,-1,-3,10,-6,-7,-9,-9,-5,7,-5,8,-6,6,7,10,-6,4,5,-9,-8,-2,-1,3,-7,5,7,8,8,-1,-3,6,9,-9,5,-7,-4,-9,-9,5,5,8,5,-7,7,9,-6,9,4,-2,-6,3,-6,-9,7,3,-3,-5,-6,-1,-8,-4,5,4,1,-10,2,1,8,-5,3,6,-8,6,1,8,8,-8,5,-4,-5,-7,10,9,9,2,3,-10,8,4,3,-1,-3,-6,10,-7,4,3,2,-3,-7,5,-2,-10,2,10,-5,-8,9,-7,2,3,5,-4,-10,-10,-2,7,-9,-4,9,6,-4,-2,-8,1,2,10,2,6,10,10,-10,-8,2,-2,8,6,-4,-5,9,2,10,9,-5,5,-1,-7,-10,8,9,-4,7,8,-2,4,7,-1,8,-10,-6,-8,7,-6,2,-10,5,7,6,5,-8,-9,5,-3,-1,7,5,-2,3,-9,1,8,-3,-8,-2,-9,2,-7,-8,-9,1,-6,-1,1,6,9,-9,-3,-3,5,4,6,-10,2,-3,-6,-8,3,1,-1,5,-4,8,9,8,7,-8,9,-5,-7,-3,3,5,1,9,3,-4,10,-4,-3,5,-6,2,2,-8,4,-3,-5,4,-6,-7,-8,-6,5,5,10,-10,4,4,9,-8,7,1,-2,5,-7,7,-5,2,-10,-10,9,-1,-9,-1,-8,1,-10,5,-7,-10,-5,8,9,-2,8,-1,9,2,-6,-6,3,2,-10,-5,-9,1,-3,6,2,-1,7,9,-4,3,7,-8,7,-4,-7,5,-6,-10,9,1,1,2,-3,-3,4,-1,-5,1,-7,2,6,7,-6,-2,-2,-6,4,2,-9,-6,-1,3,-6,-10,9,-8,-9,-8,-4,2,3,1,-6,-5,-8,-9,2,6,6,2,8,-2,-4,4,9,4,-3,-9,9,-3,9,-7,6,8,1,-9,7,-10,10,-9,-9,2,9,1,9,5,8,8,7,-5,-3,9,-6,3,2,-6,4,-3,1,-8,-7,-8,-5,6,2,2,6,7,2,-7,-9,-5,2,5,1,-6,8,-3,10,-5,-3,-8,-10,-2,-3,7,3,-7,10,-10,5,1,-2,6,-6,-4,10,9,-9,2,-1,5,9,-8,-4,-3,-6,2,-9,-10,1,-3,8,-1,-4,-8,-10,-8,5,-1,6,-5,6,-10,8,-9,4,10,-7,-8,3,-7,-8,-5,5,-9,-10,3,4,3,3,-10,8,-8,2,8,-1,2,2,-2,5,-7,-8,3,6,-5,-1,-6,9,-4,2,-10,-6,2,-2,-4,6,2,-4,7,2,-8,8,-2,2,10,5,-4,-2,9,-1,-1,-4,2,-9,-7,4,3,-1,-1,-10,-6,-10,-6,-9,6,-7,8,7,9,-2,6,2,-7,6,-8,10,-1,-6,-3,-3,-4,4,-4,-5,-7,-9,-2,4,-6,9,7,9,10,-3,8,-9,-6,6,4,-3,10,-7,5,-4,-2,-8,-4,6,-2,-4,7,-5,-6,5,4,-2,9,7,-1,-6,3,3,-1,-1,10,-3,1,-9,9,-9,-1,-7,2,-6,-2,9,8,-5,3,-2,-3,7,3,1,10,-6,4,-1,5,1,-2,7,4,-9,-9,-7,5,4,-2,9,8,-10,7,9,9,-3,10,-10,-1,-1,-9,-3,-6,10,4,7,5,4,-1,5,-3,-2,8,9,-3,2,-3,-6,-1,-5,8,-9,-3,4,-6,-5,-5,3,-3,3,-5,9,9,4,-4,7,5,4,10,2,-4,6,8,-3,4,-8,-10,-6,4,8,-1,9,-4,-1,-8,-2,-4,2,-10,2,2,4,6,-2,9,8,7,-3,-10,-5,9,-1,-8,4,1,-5,-7,4,6,-4,5,5,1,3,4,10,-7,-8,-5,6,-10,6,9,-1,-7,10,-8,4,-2,-1,-6,2,1,2,-2,-1,-9,-10,-8,-3,-7,-6,9,6,-8,-8,7,10,9,3,10,4,2,8,-2,-4,-6,-5,2,-4,8,5,-3,-1,-8,-4,8,-10,9,-10,-10,1,7,-9,-5,9,9,9,2,-4,6,-1,-5,7,-10,6,-3,6,-3,1,9,3,8,2,4,2,-6,-6,-3,-9,-10,-3,-4,-7,3,6,9,-2,3,-9,-1,-9,-4,-10,-8,2,-3,-2,-3,5,6,1,-5,4,-8,7,4,8,10,6,8,5,4,-10,6,-4,9,10,8,-1,7,-8,3,10,6,9,-6,7,4,7,-3,4,6,-5,8,-5,-4,-5,-10,10,2,2,-6,8,-6,-1,5,2,-9,-10,-3,-1,9,-3,2,-7,-5,-2,9,2,-4,6,-10,3,-7,8,9,8,7,8,-7,2,3,-4,4,10,8,-7,6,8,6,-5,5,-4,-7,2,5,-7,-9,-3,-4,9,10,-2,8,4,-8,-9,-4,-5,-3,-4,-10,1,1,-2,-8,9,-9,-8,1,-10,-1,-1,-4,-6,5,7,1,7,-1,-7,10,-9,-6,-7,-7,5,-8,2,5,10,8,-5,5,-2,-9,-5,4,-9,1,7,-4,7,-9,5,7,-1,-3,7,-8,-4,8,7,3,4,3,1,2,-3,-7,2,-4,-2,-9,4,-7,-6,8,-9,-1,-5,2,6,-4,-4,5,-6,1,7,6,-9,10,8,-9,10,-9,6,1,-5,9,5,-7,7,8,10,-5,-6,4,-4,-2,5,-7,3,3,2,-7,-9,7,-2,8,-10,-1,-10,2,-8,-6,6,-3,3,6,9,-10,8,4,4,-4,-5,-9,-7,-8,-7,-7,-10,-1,8,6,-1,-6,6,10,2,-2,-8,3,-4,-10,5,-4,-10,6,10,-5,-10,1,1,-6,5,9,1,-9,-2,7,-10,2,6,8,-2,1,2,-10,3,-5,5,2,-5,-2,1,2,-2,1,-4,8,-2,10,10,6,-7,2,4,-8,6,-3,1,10,2,3,-10,2,9,5,-1,3,-3,-9,-8,5,-9,2,-8,5,-6,5,-9,-8,-8,-10,-8,-8,7,-10,-4,-10,7,-5,6,4,8,10,6,-6,2,5,8,-1,-1,-9,-7,-10,-10,-7,4,-10,1,-10,7,3,-3,-1,4,-3,4,1,-10,6,-7,8,-6,-4,8,6,-9,7,1,-2,-10,9,-8,5,-1,-9,4,10,10,9,-5,5,7,-7,-10,3,-7,-3,-1,2,-9,-10,10,7,1,8,-2,-3,5,-5,-2,-4,-1,1,-5,-5,6,1,5,-8,3,-6,10,-2,-1,9,-7,10,2,-3,-6,5,-6,-10,4,1,5,-10,9,10,-1,3,4,8,-9,-4,9,-7,-6,8,-6,-9,6,-3,-3,5,4,4,5,5,-4,7,10,10,2,8,-9,-8,-6,10,-4,5,-6,7,4,-5,10,-4,7,-8,6,-8,5,-9,-7,-2,7,10,-8,-5,8,1,-2,-10,-10,2,6,-8,8,-4,8,7,-5,9,3,-6,-3,-10,-1,-8,1,-7,-1,-2,4,-5,3,-10,-10,-2,2,-5,6,-4,8,-9,3,9,-3,-3,6,1,-10,8,9,-3,9,-8,5,-1,5,3,-6,-1,5,5,-10,1,-9,-9,8,-9,-10,-1,10,-10,-9,-2,7,-3,-5,-6,-7,6,7,-2,7,-3,10,-4,3,7,8,7,3,10,8,-5,-4,-1,-8,5,6,-6,9,9,3,3,5,9,-2,6,-6,7,5,8,-2,-1,-10,-7,7,10,-1,-3,7,-2,2,10,-10,7,-4,-1,7,-7,8,-5,-9,7,2,-6,-6,7,-8,-6,-4,6,-10,-6,-8,4,-8,-3,8,9,-1], dtype = "uint64")#candidate|10464|(2288,)|const|uint64
call_10462 = relay.TupleGetItem(func_3104_call(relay.reshape(var_10463.astype('int16'), [7, 8, 4]), relay.reshape(const_10464.astype('uint64'), [2288,]), relay.reshape(call_10418.astype('float64'), [30, 2]), ), 4)
call_10465 = relay.TupleGetItem(func_3108_call(relay.reshape(var_10463.astype('int16'), [7, 8, 4]), relay.reshape(const_10464.astype('uint64'), [2288,]), relay.reshape(call_10418.astype('float64'), [30, 2]), ), 4)
func_4638_call = mod.get_global_var('func_4638')
func_4643_call = mutated_mod.get_global_var('func_4643')
call_10483 = relay.TupleGetItem(func_4638_call(relay.reshape(var_10463.astype('int16'), [16, 14]), relay.reshape(const_10464.astype('uint64'), [2288,]), relay.reshape(call_10418.astype('float64'), [60,]), ), 3)
call_10484 = relay.TupleGetItem(func_4643_call(relay.reshape(var_10463.astype('int16'), [16, 14]), relay.reshape(const_10464.astype('uint64'), [2288,]), relay.reshape(call_10418.astype('float64'), [60,]), ), 3)
func_848_call = mod.get_global_var('func_848')
func_852_call = mutated_mod.get_global_var('func_852')
call_10492 = func_848_call(relay.reshape(const_10464.astype('uint64'), [16, 11, 13]), relay.reshape(const_10464.astype('uint64'), [16, 11, 13]), )
call_10493 = func_848_call(relay.reshape(const_10464.astype('uint64'), [16, 11, 13]), relay.reshape(const_10464.astype('uint64'), [16, 11, 13]), )
func_9715_call = mod.get_global_var('func_9715')
func_9716_call = mutated_mod.get_global_var('func_9716')
call_10499 = func_9715_call()
call_10500 = func_9715_call()
output = relay.Tuple([call_10418,call_10462,var_10463,const_10464,call_10483,call_10492,call_10499,])
output2 = relay.Tuple([call_10419,call_10465,var_10463,const_10464,call_10484,call_10493,call_10500,])
func_10516 = relay.Function([var_10463,], output)
mod['func_10516'] = func_10516
mod = relay.transform.InferType()(mod)
mutated_mod['func_10516'] = func_10516
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10517 = relay.var("var_10517", dtype = "int16", shape = (8, 28))#candidate|10517|(8, 28)|var|int16
func_10516_call = mutated_mod.get_global_var('func_10516')
call_10518 = func_10516_call(var_10517)
output = call_10518
func_10519 = relay.Function([var_10517], output)
mutated_mod['func_10519'] = func_10519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7608_call = mod.get_global_var('func_7608')
func_7610_call = mutated_mod.get_global_var('func_7610')
call_10521 = func_7608_call()
call_10522 = func_7608_call()
output = relay.Tuple([call_10521,])
output2 = relay.Tuple([call_10522,])
func_10536 = relay.Function([], output)
mod['func_10536'] = func_10536
mod = relay.transform.InferType()(mod)
mutated_mod['func_10536'] = func_10536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10536_call = mutated_mod.get_global_var('func_10536')
call_10537 = func_10536_call()
output = call_10537
func_10538 = relay.Function([], output)
mutated_mod['func_10538'] = func_10538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4446_call = mod.get_global_var('func_4446')
func_4447_call = mutated_mod.get_global_var('func_4447')
call_10550 = relay.TupleGetItem(func_4446_call(), 0)
call_10551 = relay.TupleGetItem(func_4447_call(), 0)
output = relay.Tuple([call_10550,])
output2 = relay.Tuple([call_10551,])
func_10552 = relay.Function([], output)
mod['func_10552'] = func_10552
mod = relay.transform.InferType()(mod)
output = func_10552()
func_10553 = relay.Function([], output)
mutated_mod['func_10553'] = func_10553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5427_call = mod.get_global_var('func_5427')
func_5428_call = mutated_mod.get_global_var('func_5428')
call_10554 = relay.TupleGetItem(func_5427_call(), 1)
call_10555 = relay.TupleGetItem(func_5428_call(), 1)
const_10558 = relay.const([[[8.666414,-7.921030,9.399137,3.924256,6.799363],[-3.039775,-1.631817,-2.792321,-7.468851,1.449496]],[[3.271682,6.323220,-7.810081,-8.395241,-3.541603],[-8.338585,-3.943482,-8.751392,-7.709357,-4.298095]],[[2.069452,-7.721336,6.456043,-8.740487,2.772308],[8.940427,-5.526312,-9.994223,-3.392349,2.631352]],[[-5.107601,-6.422278,-3.586913,-7.639140,8.607216],[9.813228,-7.184339,-7.467377,-5.000962,9.031203]],[[-9.661877,3.173760,-6.820948,-4.688725,-4.294402],[3.823583,6.784311,9.583852,-9.034016,-0.348528]],[[-3.843307,-9.453531,-3.543112,6.259169,7.907421],[-3.538633,2.917748,-6.098730,6.966108,-9.625214]],[[-0.971511,-7.309178,2.557386,-5.573526,3.537833],[6.950503,-1.823404,-8.599565,8.798570,2.323734]]], dtype = "float64")#candidate|10558|(7, 2, 5)|const|float64
bop_10559 = relay.left_shift(call_10554.astype('int16'), relay.reshape(const_10558.astype('int16'), relay.shape_of(call_10554))) # shape=(7, 2, 5)
bop_10562 = relay.left_shift(call_10555.astype('int16'), relay.reshape(const_10558.astype('int16'), relay.shape_of(call_10555))) # shape=(7, 2, 5)
output = relay.Tuple([bop_10559,])
output2 = relay.Tuple([bop_10562,])
func_10586 = relay.Function([], output)
mod['func_10586'] = func_10586
mod = relay.transform.InferType()(mod)
mutated_mod['func_10586'] = func_10586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10586_call = mutated_mod.get_global_var('func_10586')
call_10587 = func_10586_call()
output = call_10587
func_10588 = relay.Function([], output)
mutated_mod['func_10588'] = func_10588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4724_call = mod.get_global_var('func_4724')
func_4726_call = mutated_mod.get_global_var('func_4726')
call_10613 = relay.TupleGetItem(func_4724_call(), 0)
call_10614 = relay.TupleGetItem(func_4726_call(), 0)
output = call_10613
output2 = call_10614
func_10617 = relay.Function([], output)
mod['func_10617'] = func_10617
mod = relay.transform.InferType()(mod)
output = func_10617()
func_10618 = relay.Function([], output)
mutated_mod['func_10618'] = func_10618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9413_call = mod.get_global_var('func_9413')
func_9414_call = mutated_mod.get_global_var('func_9414')
call_10622 = relay.TupleGetItem(func_9413_call(), 0)
call_10623 = relay.TupleGetItem(func_9414_call(), 0)
output = call_10622
output2 = call_10623
func_10636 = relay.Function([], output)
mod['func_10636'] = func_10636
mod = relay.transform.InferType()(mod)
mutated_mod['func_10636'] = func_10636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10636_call = mutated_mod.get_global_var('func_10636')
call_10637 = func_10636_call()
output = call_10637
func_10638 = relay.Function([], output)
mutated_mod['func_10638'] = func_10638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10617_call = mod.get_global_var('func_10617')
func_10618_call = mutated_mod.get_global_var('func_10618')
call_10643 = func_10617_call()
call_10644 = func_10617_call()
func_4602_call = mod.get_global_var('func_4602')
func_4606_call = mutated_mod.get_global_var('func_4606')
var_10664 = relay.var("var_10664", dtype = "int8", shape = (378,))#candidate|10664|(378,)|var|int8
call_10663 = func_4602_call(relay.reshape(var_10664.astype('int8'), [14, 3, 9]), relay.reshape(var_10664.astype('int8'), [14, 3, 9]), )
call_10665 = func_4602_call(relay.reshape(var_10664.astype('int8'), [14, 3, 9]), relay.reshape(var_10664.astype('int8'), [14, 3, 9]), )
func_3884_call = mod.get_global_var('func_3884')
func_3886_call = mutated_mod.get_global_var('func_3886')
var_10667 = relay.var("var_10667", dtype = "float64", shape = (72,))#candidate|10667|(72,)|var|float64
call_10666 = relay.TupleGetItem(func_3884_call(relay.reshape(var_10667.astype('float64'), [72,])), 3)
call_10668 = relay.TupleGetItem(func_3886_call(relay.reshape(var_10667.astype('float64'), [72,])), 3)
func_5137_call = mod.get_global_var('func_5137')
func_5138_call = mutated_mod.get_global_var('func_5138')
call_10709 = relay.TupleGetItem(func_5137_call(), 1)
call_10710 = relay.TupleGetItem(func_5138_call(), 1)
func_6210_call = mod.get_global_var('func_6210')
func_6212_call = mutated_mod.get_global_var('func_6212')
call_10733 = relay.TupleGetItem(func_6210_call(), 0)
call_10734 = relay.TupleGetItem(func_6212_call(), 0)
output = relay.Tuple([call_10643,call_10663,var_10664,call_10666,var_10667,call_10709,call_10733,])
output2 = relay.Tuple([call_10644,call_10665,var_10664,call_10668,var_10667,call_10710,call_10734,])
func_10743 = relay.Function([var_10664,var_10667,], output)
mod['func_10743'] = func_10743
mod = relay.transform.InferType()(mod)
mutated_mod['func_10743'] = func_10743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10743_call = mutated_mod.get_global_var('func_10743')
var_10745 = relay.var("var_10745", dtype = "int8", shape = (378,))#candidate|10745|(378,)|var|int8
var_10746 = relay.var("var_10746", dtype = "float64", shape = (72,))#candidate|10746|(72,)|var|float64
call_10744 = func_10743_call(var_10745,var_10746,)
output = call_10744
func_10747 = relay.Function([var_10745,var_10746,], output)
mutated_mod['func_10747'] = func_10747
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5272_call = mod.get_global_var('func_5272')
func_5273_call = mutated_mod.get_global_var('func_5273')
call_10879 = relay.TupleGetItem(func_5272_call(), 0)
call_10880 = relay.TupleGetItem(func_5273_call(), 0)
func_9122_call = mod.get_global_var('func_9122')
func_9123_call = mutated_mod.get_global_var('func_9123')
call_10903 = relay.TupleGetItem(func_9122_call(), 0)
call_10904 = relay.TupleGetItem(func_9123_call(), 0)
func_7659_call = mod.get_global_var('func_7659')
func_7661_call = mutated_mod.get_global_var('func_7661')
call_10905 = relay.TupleGetItem(func_7659_call(), 0)
call_10906 = relay.TupleGetItem(func_7661_call(), 0)
func_5223_call = mod.get_global_var('func_5223')
func_5225_call = mutated_mod.get_global_var('func_5225')
call_10914 = relay.TupleGetItem(func_5223_call(), 0)
call_10915 = relay.TupleGetItem(func_5225_call(), 0)
output = relay.Tuple([call_10879,call_10903,call_10905,call_10914,])
output2 = relay.Tuple([call_10880,call_10904,call_10906,call_10915,])
func_10950 = relay.Function([], output)
mod['func_10950'] = func_10950
mod = relay.transform.InferType()(mod)
mutated_mod['func_10950'] = func_10950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10950_call = mutated_mod.get_global_var('func_10950')
call_10951 = func_10950_call()
output = call_10951
func_10952 = relay.Function([], output)
mutated_mod['func_10952'] = func_10952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6926_call = mod.get_global_var('func_6926')
func_6927_call = mutated_mod.get_global_var('func_6927')
call_10958 = relay.TupleGetItem(func_6926_call(), 1)
call_10959 = relay.TupleGetItem(func_6927_call(), 1)
func_5807_call = mod.get_global_var('func_5807')
func_5809_call = mutated_mod.get_global_var('func_5809')
call_10960 = func_5807_call()
call_10961 = func_5807_call()
func_6125_call = mod.get_global_var('func_6125')
func_6126_call = mutated_mod.get_global_var('func_6126')
call_10980 = relay.TupleGetItem(func_6125_call(), 1)
call_10981 = relay.TupleGetItem(func_6126_call(), 1)
func_4386_call = mod.get_global_var('func_4386')
func_4388_call = mutated_mod.get_global_var('func_4388')
call_10992 = relay.TupleGetItem(func_4386_call(), 1)
call_10993 = relay.TupleGetItem(func_4388_call(), 1)
func_6480_call = mod.get_global_var('func_6480')
func_6482_call = mutated_mod.get_global_var('func_6482')
const_10995 = relay.const([3,-4,4,2,-6,6,-3,4,1,1,1,5,-1,-7,8,-6,-1,-9,-10,-4,3,10,6,-4,-2,-7,1,2,-8,10,6,-6,-6,-1,-5,3,-5,-3,-1,-2,-4,-9,-2,8,8,5,-3,3,5,6,-1,7,5,8,9,-8,-8,9,-8,9,2,-1,6,-4,8,-10,-10,4,1,9,4,4,-6,4,-7,-9,-9,-3,4,4,9,2,3,3,10,3,-3,7,-9,1,-6,-6,-1,-7,-8,7,-7,5,5,-5,3,-10,-6,-6,-10,10,7,10,-4,-1,8,-8,-8,-6,-2,-9,-10,1,-8,10,4,-5,-5,-9,9,-3,-9,-3,-5,-10,-1,-4,-8,6,2,5,5,6,-2,-3,4,-10,-7,2,6,-1,-10,8,9,-3,10,-6,-7,-9,9,4,7,8,8,6,-3,1,-1,1,-2,1,-4,9,1,-2,7,6,9,8,4,-1,2,-10,10,-2,-8,6,-2,-3,10,-5,-1,-1,-5,-8,-4,7,3,-8,9,-9,3,-8,8,-1,-7,5,9,10,6,6,9,7,-1,8,3,6,1,-4,-5,7,-5,-2,10,-10,-10,-10,10,-2,2,-10,7,2,9,-9,5,6,10,-6,-10,1,-5,-8,8,-5,-1,-5,10,-10,-7,5,7,-2,1,-9,6,-10,3,-5,9,-1,-4,1,-8,-7,10,-7,-5,-5,-6,-7,6,-3,-5,-10,-8,-5,9,-8,-6,2,-7,4,5,-6,6,5,-1,9,-5,-2,-1,-5,4,-9,-8,-8,-7,5,-4,7,6,-1,10,-7,-10,8,-6,6,-8,-2,-6,-1,7,-9,7,-2,-7,2,-3,-2,7,-6,7,-5,-7,-1,-9,5,6,-6,9,-8,1,4,10,-8,-8,-2,-8,-9,-3,-7,-1,-8,-6,2,4,-2,3,-10,-1,-1,-5,-5,-9,-8,-5,9,-7,4,3,7,-9,2,-4,-4,3,8,-10,10,9,4,-5,1,9,-5,3,-10,2,4,-6,-1,-6,6,-1,-5,-8,-6,3,-5,3,7,-2,8,-10,-10,-1,-5,1,10,2,2,-6,5,6,-2,-9,-6,-5,-7,-7,1,-7,4,2,9,9,5,2,5,-9,-8,7,1,8,-6,4,-4,6,10,2,-3,3,-8,-8,-4,3,7,-7,3,8,-2,-9,-3,2,4,-3,7,-4,2,10,-9,1,5,6,-3,7,7,2,10,3,2,-10,-1,-5,-4,-2,-8,-3,-1,10,5,3,-1,2,-1,-7,9,1,10,7,-1,-1,4,-3,-4,10,10,3,-8,-7,10,-3,1,-10,-2,-7,8,3,5,-6,10,-10,1,4,-8,2,2,8,-1,-4,-7,-5,2,-6,5,8,2,-6,1,4,-8,9,2,-3,6,-4,-2,-8,7,1,-10,7,-7,4,-10,1,-3,-8,-8,7,-2,-8,2,-9,2,10,9,3,-10,-7,-3,8,9,-2,9,-4,2,5,8,2,-4,-3,4,10,-2,4,-5,3,8,-2,9,-10,-8,5,-9,-7,3,-5,-7,-9,-9,-6,5,8,-7,4,6,6,-9,9,10,-10,-9,10,-7,7,-1,-2,-2,-2,5,-4,-10,-5,1,-8,4,-4,10,-1,2,-6,-8,-1,-1,9,1,-6,-6,-1,-9,-10,6,7,7,-4,3,3,-8,-2,-9,4,-6,2,-5,9,-3,-6,4,-6,1,-1,2,6,8,1,-10,-9,7,-8,-6,6,-7,-8,-8,-1,6,1,-6,10,-6,-3,-7,-3,-4,7,-8,-9,7,-8,-4,2,-1,-10,4,10,10,-6,-6,3,8,9,-5,2,4,7,-9,9,-3,-6,10,7,-1,-9,10,6,2,-5,-2,8,-9,5,5,-9,-5,-5,2,7,5,-10,-7,-2,-2,7,3,9,2,1,1,6,-4,-3,3,2,5,2,10,3,10,-5,5,7,1,-5,-8,8,-9,2,10,-9,-8,9,4,2,-3,-9,3,6,-3,-4,-1,5,-1,4,-1,-6,-6,8,8,6,-7,10,10,-3,8,-6,-10,-10,5,4,-7,-4,-7,4,2,-9,-4,8,6,9,-9,-4,5,9,6,-8,6,-9,-6,-10,-3,-7,7,-3,7,8,10,-4,-6,4,8,6,-6,9,-7,10,8,-9,5,10,7,-7,-2,1,-5,9,-9,-9,1,6,-7,-10,-4,-1,-2,-2,-3,-5,1,10,-10,-9,-7,3,4,-7,-6,7,-7,-10,3,9,10,-8,7,6,10,-8,4,6,1,-1,4,8,10,2,9,-9,5,-1,-9,2,2,8,-9,6,-10,6,6,-7,1,2,-1,10,-2,8,10,3,-10,-10,7,-9,-4,3,1,8,9,2,3,-8,5,-8,-6,6,6,-4,-3,-2,-10,-7,-4,10,7,7,-6,-8,-9,-5,-9,-10,9,8,7,-9,4,7,-4,-3,-1,-2,-5,9,7,10,4,-3,-4,-7,10,7,3,-1,-2,-8,7,1,10,-6,3,7,6,2,-10,10,-4,-3,2,4,10,-9,3,1,-2,-4,-2,4,-10,5,-5,9,1,-6,8,9,3,-7,1,-2,4,2,7,-2,-2,7,2,-7,-10,10,-5,7,10,-8,3,-6,8,-3,-3,1,1,-5,6,10,6,-3,8,1,-6,-8,1,-6,-3,-3,5,2,-4,1,-10,3,10,7,7,-7,-6,-4,1,5,10,-10,4,10,-10,5,3,-4,-5,2,-8,7,-8,-3,10,2,-8,2,8,-7,3,8,1,9,-4,9,2,10,-6,8,10,3,-6,-9,7,1,-9,5,3,-5,-7,-1,-10,-10,3,-2,9,3,10,-10,-10,-8,1,9,9,3,10,-6,6,-9,-3,-3,6,-10,2,5,10,-10,-9,7,5,-4,7,-7,4,-5,7,-1,-6,9,-2,9,-10,-5,10,-6,5,3,-10,8,-6,-2,10,4,-8,-5,9,-4,-5,-1,2,-3,9,-2,6,-4,-2,-5,-4,8,6,-4,-9,6,-7,10,-4,10,-9,-4,-2,-9,-7,-7,-5,-4,-10,6,7,3,10,-5,8,-10,8,4,-4,-4,-9,-3,6,5,-6,-5,-6,-6,4,3,-7,-9,-8,-6,-7,-5,-1,-1,8,5,1,-8,10,3,5,6,-8,-10,-9,1,7,4,-6,9,5,9,-5,10,1,9,-9,10,1,8,-6,-8,6,-3,1,8,5,1,-4,-5,-6,1,-1,-5,-10,-2,1,-9,4,-1,3,10,-7,-10,-3,4,-1,-7,7,-3,-4,-5,-5,-1,-8,5,-2,-1,-5,9,-8,-9,7,1,7,-3,1,5,-4,-6,-1,-6,-5,1,10,9,-3,6,4,6,-3,2,6,-9,-6,-5,-5,9,7,-9,-1,4,-7,-4,6,-4,-8,3,6,8,-7,10,-3,-2,-10,-9,9,3,-2,9,-6,8,-1,-1,3,8,2,3,-6,6,-4,-7,8,1,8,9,2,9,10,-10,-9,4,8,-7,-2,4,-9,1,10,9,-1,-1,6,8,-2,-1,-1,-4,-4,-7,7,-6,-10,-6,-10,-10,3,-4,3,-7,2,-10,4,-2,-9,7,-8,-4,10,1,-7,9,-2,1,6,-4,7,-9,-10,-7,10,4,-7,-10,-8,-6,-2,5,1,1,3,6,-9,-10,8,7,3,7,8,6,-8,1,1,-6,-3,8,4,7,-8,2,4,5,-1,-9,2,6,-10,-10,4,-1,-4,-4,-4,-2,6,10,5,9,-10,6,-6,1,-9,6,8,-2,-8,-1,-5,-9,-8,5,6,1,4,9,-8,-3,1,2,-9,-2,-1,1,5,-1,1,-8,1,5,7,-5,-4,3,8,-7,-2,-5,-1,2,-6,-10,-10,6,-8,-7,6,-9,10,8,-9,-6,3,5,8,1,-2,-5,-9,-6,-1,-3,4,-9,-4,-4,-1,6,-2,9,10,-7,1,9,-10,-1,7,-10,-6,5,6,-4,2,1,1,-5,2,-7,2,4,-8,-7,-9,-6,-7,-4,2,10,-8,-7,2,1,-2,6,-4,-7,7,9,-2,2,6,10,4,2,-2,-10,-1,-6,-9,10,-7,8,-1,-2,2,2,-10,7,-2,-3,-10,-9,-3,-7,-1,8,3,2,2,7,-7,-3,-1,10,-3,-10,-5,-5,7,-1,-6,6,6,3,1,-4,-1,7,1,-7,-10,7,-7,-4,-4,-3,-7,-10,-7,10,7,8,3,9,-3,-8,5,-10,8,7,10,-2,8,-9,9,3,-5,3,6,-2,8,4,3,-8,-8,3,-6,5,9,9,3,-3,2,-6,7,9,-8,-1,-7,-4,-3,-4,-1,2,-5,9,2,-8,-9,-3,4,6,-7,5,-5,10,5,8,5,8,-1,-7,1,7,10,8,6,-6,-10,-10,9,6,5,1,-4,-7,-8,-1,-10,10,-10,3,-2,-10,1,9,9,-3,-9,-4,3,-1,-6,1,1,-5,10,9,-9,6,9,10,-1,4,-9,-3,10,5,-4,-9,8,6,-3,1,5,2,3,4,4,1,6,6,-6,1,7,-5,-5,-2,7,10,9,6,5,5,9,5,-10,3,-1,-7,4,3,4,-10,7,3,-4,-9,8,-10,-1,-4,3,-8,2,5,1,7,-1,8,-9,-5,9,-3,1,-6,6,3,7,-6,-9,7,8,5,1,9,-4,4,-10,10,8,-4,-8,-6,10,-6,-2,9,4,-9,-9,6,3,-7,-5,-6,5,-9,-7,-7,-6,6,-3,10,-10,4,-9,3,10,-7,-8,-10,-3,3,-6,4,3,-2,4,-8,10,6,-4,-3,10,9,-5,9,10,5,-2,7,-1,-6,10,-9,-5,2,-3,-4,-7,1,4,9,9,1,6,-1,-7,-10,-8,-9,-6,-4,8,-4,-1,-8,-2,-10,-4,6,-10,-7,-1,-6,-9,-4,8,6,6,-4,4,3,-2,10,-7,-5,3,-4,10,5,-6,4,7,-3,-9,-1,8,2,-10,-5,-1,1,-4,-10,6,-4,4,-6,8,-5,6,-4,1,-6,10,-5,-4,3,-1,4,8,-10,8,7,-7,6,10,10,6,2,9,-5,4,-3,-2,-4,7,-7,2,-10,6,-2,6,10,10,-9,9,-2,-5,10,1,10,-8,2,2,-8,-10,7,-6,9,8,5,-4,-10,1,8,4,2,6,-3,-6,9,3,1,2,7,9,-5,8,-6,5,-5,-2,10,-8,8,-4,-1,4,10,5,-6,-7,9,-6,6,-9,-10,-7,2,-5,-1,-9,10,6,7,-5,-8,-4,10,2,-3,9,3,-8,-1,-5,-4,9,-8,-3,-8,10,3,-3,-5,-10,-9,6,5,6,6,2,-8,5,-8,2,9,2,-5,-6,1,1,-7,1,-10,9,10,10,-4,5,5,10,9,-7,-8,-7,1,8,-4,1,9,1,-5,9,-6,-3,-4,-7,4,9,1,10,3,-1,8,10,1,-7,4,6,-2,3,10,9,7,6,4,-9,4,2,9,-1,7,9,-8,1,3,-6,-5,-9,-4,10,10,3,-9,-10,-10,3,1,-9,6,-10,6,-4,-2,-5,7,-4,-5,1,-3,4,-3,1,8,4,-1,-3,-10,-8,-9,1,-8,-4,-2,-9,-7,-10,-10,4,-2,2,-3,-10,3,7,1,-1,-3,-4,-10,-1,5,-5,2,-5,-8,-8,3,3,-4,-1,8,-5,-4,5,-9,-9,6,1,3,-4,2,-1,-8,2,-7,-8,-4,-6,-2,-10,-7,-9,-5,3,-6,-9,9,-7,8,-10,4,-2,2,5,-8,7,6,-10,-6,-8,-10,-5,1,-5,-3,4,4,4,-3,-10,-5,-8,-4,-3,3,-7,10,-3,3,-10,4,2,9,4,6,-4,-2,2,-5,8,-8,-3,4,9,-4,4,10,-6,3,-2,-3,-9,-1,2,-8,3,5,4,2,9,-10,-3,-2,-3,10,-3,2,-9,5,-10,-4,-10,-9,-8,-8,6,-1,-2,10,7,9,-5,6,-5,-7,-5,-9,10,9,-10,7,7,-7,-3,2,-8,-2,3,7,8,-2,5,-9,-9,4,-5,7,3,1,-2,-5,-4,-3,6,5,-6,-10,10,9,-8,-1,6,-7,2,4,-8,4,8], dtype = "uint64")#candidate|10995|(2288,)|const|uint64
call_10994 = relay.TupleGetItem(func_6480_call(relay.reshape(const_10995.astype('uint64'), [2288,])), 2)
call_10996 = relay.TupleGetItem(func_6482_call(relay.reshape(const_10995.astype('uint64'), [2288,])), 2)
func_9936_call = mod.get_global_var('func_9936')
func_9937_call = mutated_mod.get_global_var('func_9937')
call_11022 = func_9936_call()
call_11023 = func_9936_call()
output = relay.Tuple([call_10958,call_10960,call_10980,call_10992,call_10994,const_10995,call_11022,])
output2 = relay.Tuple([call_10959,call_10961,call_10981,call_10993,call_10996,const_10995,call_11023,])
func_11028 = relay.Function([], output)
mod['func_11028'] = func_11028
mod = relay.transform.InferType()(mod)
output = func_11028()
func_11029 = relay.Function([], output)
mutated_mod['func_11029'] = func_11029
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11051 = relay.var("var_11051", dtype = "float64", shape = (9, 10, 16))#candidate|11051|(9, 10, 16)|var|float64
uop_11052 = relay.asinh(var_11051.astype('float64')) # shape=(9, 10, 16)
output = uop_11052
output2 = uop_11052
func_11063 = relay.Function([var_11051,], output)
mod['func_11063'] = func_11063
mod = relay.transform.InferType()(mod)
var_11064 = relay.var("var_11064", dtype = "float64", shape = (9, 10, 16))#candidate|11064|(9, 10, 16)|var|float64
output = func_11063(var_11064)
func_11065 = relay.Function([var_11064], output)
mutated_mod['func_11065'] = func_11065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10308_call = mod.get_global_var('func_10308')
func_10310_call = mutated_mod.get_global_var('func_10310')
call_11080 = relay.TupleGetItem(func_10308_call(), 1)
call_11081 = relay.TupleGetItem(func_10310_call(), 1)
func_7735_call = mod.get_global_var('func_7735')
func_7736_call = mutated_mod.get_global_var('func_7736')
call_11089 = relay.TupleGetItem(func_7735_call(), 0)
call_11090 = relay.TupleGetItem(func_7736_call(), 0)
func_5906_call = mod.get_global_var('func_5906')
func_5908_call = mutated_mod.get_global_var('func_5908')
call_11092 = relay.TupleGetItem(func_5906_call(), 0)
call_11093 = relay.TupleGetItem(func_5908_call(), 0)
output = relay.Tuple([call_11080,call_11089,call_11092,])
output2 = relay.Tuple([call_11081,call_11090,call_11093,])
func_11099 = relay.Function([], output)
mod['func_11099'] = func_11099
mod = relay.transform.InferType()(mod)
mutated_mod['func_11099'] = func_11099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11099_call = mutated_mod.get_global_var('func_11099')
call_11100 = func_11099_call()
output = call_11100
func_11101 = relay.Function([], output)
mutated_mod['func_11101'] = func_11101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5191_call = mod.get_global_var('func_5191')
func_5192_call = mutated_mod.get_global_var('func_5192')
call_11152 = relay.TupleGetItem(func_5191_call(), 0)
call_11153 = relay.TupleGetItem(func_5192_call(), 0)
output = call_11152
output2 = call_11153
func_11159 = relay.Function([], output)
mod['func_11159'] = func_11159
mod = relay.transform.InferType()(mod)
mutated_mod['func_11159'] = func_11159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11159_call = mutated_mod.get_global_var('func_11159')
call_11160 = func_11159_call()
output = call_11160
func_11161 = relay.Function([], output)
mutated_mod['func_11161'] = func_11161
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5180_call = mod.get_global_var('func_5180')
func_5182_call = mutated_mod.get_global_var('func_5182')
call_11170 = relay.TupleGetItem(func_5180_call(), 2)
call_11171 = relay.TupleGetItem(func_5182_call(), 2)
func_10086_call = mod.get_global_var('func_10086')
func_10088_call = mutated_mod.get_global_var('func_10088')
call_11172 = relay.TupleGetItem(func_10086_call(), 1)
call_11173 = relay.TupleGetItem(func_10088_call(), 1)
bop_11180 = relay.bitwise_xor(call_11172.astype('uint8'), call_11170.astype('uint8')) # shape=(2, 1320)
bop_11183 = relay.bitwise_xor(call_11173.astype('uint8'), call_11171.astype('uint8')) # shape=(2, 1320)
output = bop_11180
output2 = bop_11183
func_11191 = relay.Function([], output)
mod['func_11191'] = func_11191
mod = relay.transform.InferType()(mod)
output = func_11191()
func_11192 = relay.Function([], output)
mutated_mod['func_11192'] = func_11192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5939_call = mod.get_global_var('func_5939')
func_5941_call = mutated_mod.get_global_var('func_5941')
call_11316 = func_5939_call()
call_11317 = func_5939_call()
uop_11320 = relay.log(call_11316.astype('float64')) # shape=(588, 126)
uop_11322 = relay.log(call_11317.astype('float64')) # shape=(588, 126)
output = relay.Tuple([uop_11320,])
output2 = relay.Tuple([uop_11322,])
func_11336 = relay.Function([], output)
mod['func_11336'] = func_11336
mod = relay.transform.InferType()(mod)
mutated_mod['func_11336'] = func_11336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11336_call = mutated_mod.get_global_var('func_11336')
call_11337 = func_11336_call()
output = call_11337
func_11338 = relay.Function([], output)
mutated_mod['func_11338'] = func_11338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8712_call = mod.get_global_var('func_8712')
func_8713_call = mutated_mod.get_global_var('func_8713')
call_11484 = relay.TupleGetItem(func_8712_call(), 0)
call_11485 = relay.TupleGetItem(func_8713_call(), 0)
func_7299_call = mod.get_global_var('func_7299')
func_7301_call = mutated_mod.get_global_var('func_7301')
call_11523 = relay.TupleGetItem(func_7299_call(), 2)
call_11524 = relay.TupleGetItem(func_7301_call(), 2)
uop_11552 = relay.sin(call_11523.astype('float32')) # shape=(2, 1320)
uop_11554 = relay.sin(call_11524.astype('float32')) # shape=(2, 1320)
bop_11558 = relay.less(call_11523.astype('bool'), relay.reshape(uop_11552.astype('bool'), relay.shape_of(call_11523))) # shape=(2, 1320)
bop_11561 = relay.less(call_11524.astype('bool'), relay.reshape(uop_11554.astype('bool'), relay.shape_of(call_11524))) # shape=(2, 1320)
output = relay.Tuple([call_11484,bop_11558,])
output2 = relay.Tuple([call_11485,bop_11561,])
func_11565 = relay.Function([], output)
mod['func_11565'] = func_11565
mod = relay.transform.InferType()(mod)
mutated_mod['func_11565'] = func_11565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11565_call = mutated_mod.get_global_var('func_11565')
call_11566 = func_11565_call()
output = call_11566
func_11567 = relay.Function([], output)
mutated_mod['func_11567'] = func_11567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5223_call = mod.get_global_var('func_5223')
func_5225_call = mutated_mod.get_global_var('func_5225')
call_11632 = relay.TupleGetItem(func_5223_call(), 0)
call_11633 = relay.TupleGetItem(func_5225_call(), 0)
output = relay.Tuple([call_11632,])
output2 = relay.Tuple([call_11633,])
func_11638 = relay.Function([], output)
mod['func_11638'] = func_11638
mod = relay.transform.InferType()(mod)
output = func_11638()
func_11639 = relay.Function([], output)
mutated_mod['func_11639'] = func_11639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5223_call = mod.get_global_var('func_5223')
func_5225_call = mutated_mod.get_global_var('func_5225')
call_11682 = relay.TupleGetItem(func_5223_call(), 0)
call_11683 = relay.TupleGetItem(func_5225_call(), 0)
output = relay.Tuple([call_11682,])
output2 = relay.Tuple([call_11683,])
func_11698 = relay.Function([], output)
mod['func_11698'] = func_11698
mod = relay.transform.InferType()(mod)
output = func_11698()
func_11699 = relay.Function([], output)
mutated_mod['func_11699'] = func_11699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9715_call = mod.get_global_var('func_9715')
func_9716_call = mutated_mod.get_global_var('func_9716')
call_11788 = func_9715_call()
call_11789 = func_9715_call()
output = call_11788
output2 = call_11789
func_11799 = relay.Function([], output)
mod['func_11799'] = func_11799
mod = relay.transform.InferType()(mod)
mutated_mod['func_11799'] = func_11799
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11799_call = mutated_mod.get_global_var('func_11799')
call_11800 = func_11799_call()
output = call_11800
func_11801 = relay.Function([], output)
mutated_mod['func_11801'] = func_11801
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11810 = relay.var("var_11810", dtype = "float32", shape = (15, 3, 4))#candidate|11810|(15, 3, 4)|var|float32
uop_11811 = relay.sqrt(var_11810.astype('float32')) # shape=(15, 3, 4)
output = relay.Tuple([uop_11811,])
output2 = relay.Tuple([uop_11811,])
func_11828 = relay.Function([var_11810,], output)
mod['func_11828'] = func_11828
mod = relay.transform.InferType()(mod)
mutated_mod['func_11828'] = func_11828
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11829 = relay.var("var_11829", dtype = "float32", shape = (15, 3, 4))#candidate|11829|(15, 3, 4)|var|float32
func_11828_call = mutated_mod.get_global_var('func_11828')
call_11830 = func_11828_call(var_11829)
output = call_11830
func_11831 = relay.Function([var_11829], output)
mutated_mod['func_11831'] = func_11831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7299_call = mod.get_global_var('func_7299')
func_7301_call = mutated_mod.get_global_var('func_7301')
call_11875 = relay.TupleGetItem(func_7299_call(), 2)
call_11876 = relay.TupleGetItem(func_7301_call(), 2)
output = call_11875
output2 = call_11876
func_11901 = relay.Function([], output)
mod['func_11901'] = func_11901
mod = relay.transform.InferType()(mod)
output = func_11901()
func_11902 = relay.Function([], output)
mutated_mod['func_11902'] = func_11902
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8321_call = mod.get_global_var('func_8321')
func_8322_call = mutated_mod.get_global_var('func_8322')
call_11908 = func_8321_call()
call_11909 = func_8321_call()
var_11911 = relay.var("var_11911", dtype = "float32", shape = (2, 1320))#candidate|11911|(2, 1320)|var|float32
bop_11912 = relay.left_shift(call_11908.astype('uint16'), relay.reshape(var_11911.astype('uint16'), relay.shape_of(call_11908))) # shape=(2, 1320)
bop_11915 = relay.left_shift(call_11909.astype('uint16'), relay.reshape(var_11911.astype('uint16'), relay.shape_of(call_11909))) # shape=(2, 1320)
bop_11926 = relay.subtract(call_11908.astype('int64'), relay.reshape(var_11911.astype('int64'), relay.shape_of(call_11908))) # shape=(2, 1320)
bop_11929 = relay.subtract(call_11909.astype('int64'), relay.reshape(var_11911.astype('int64'), relay.shape_of(call_11909))) # shape=(2, 1320)
func_848_call = mod.get_global_var('func_848')
func_852_call = mutated_mod.get_global_var('func_852')
var_11934 = relay.var("var_11934", dtype = "uint64", shape = (8, 286))#candidate|11934|(8, 286)|var|uint64
call_11933 = func_848_call(relay.reshape(var_11934.astype('uint64'), [16, 11, 13]), relay.reshape(var_11934.astype('uint64'), [16, 11, 13]), )
call_11935 = func_848_call(relay.reshape(var_11934.astype('uint64'), [16, 11, 13]), relay.reshape(var_11934.astype('uint64'), [16, 11, 13]), )
output = relay.Tuple([bop_11912,bop_11926,call_11933,var_11934,])
output2 = relay.Tuple([bop_11915,bop_11929,call_11935,var_11934,])
func_11936 = relay.Function([var_11911,var_11934,], output)
mod['func_11936'] = func_11936
mod = relay.transform.InferType()(mod)
mutated_mod['func_11936'] = func_11936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11936_call = mutated_mod.get_global_var('func_11936')
var_11938 = relay.var("var_11938", dtype = "float32", shape = (2, 1320))#candidate|11938|(2, 1320)|var|float32
var_11939 = relay.var("var_11939", dtype = "uint64", shape = (8, 286))#candidate|11939|(8, 286)|var|uint64
call_11937 = func_11936_call(var_11938,var_11939,)
output = call_11937
func_11940 = relay.Function([var_11938,var_11939,], output)
mutated_mod['func_11940'] = func_11940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7608_call = mod.get_global_var('func_7608')
func_7610_call = mutated_mod.get_global_var('func_7610')
call_11954 = func_7608_call()
call_11955 = func_7608_call()
output = relay.Tuple([call_11954,])
output2 = relay.Tuple([call_11955,])
func_11977 = relay.Function([], output)
mod['func_11977'] = func_11977
mod = relay.transform.InferType()(mod)
output = func_11977()
func_11978 = relay.Function([], output)
mutated_mod['func_11978'] = func_11978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9661_call = mod.get_global_var('func_9661')
func_9663_call = mutated_mod.get_global_var('func_9663')
call_12079 = relay.TupleGetItem(func_9661_call(), 0)
call_12080 = relay.TupleGetItem(func_9663_call(), 0)
uop_12083 = relay.log(call_12079.astype('float64')) # shape=(8, 6, 12)
uop_12085 = relay.log(call_12080.astype('float64')) # shape=(8, 6, 12)
func_7735_call = mod.get_global_var('func_7735')
func_7736_call = mutated_mod.get_global_var('func_7736')
call_12086 = relay.TupleGetItem(func_7735_call(), 0)
call_12087 = relay.TupleGetItem(func_7736_call(), 0)
output = relay.Tuple([uop_12083,call_12086,])
output2 = relay.Tuple([uop_12085,call_12087,])
func_12091 = relay.Function([], output)
mod['func_12091'] = func_12091
mod = relay.transform.InferType()(mod)
output = func_12091()
func_12092 = relay.Function([], output)
mutated_mod['func_12092'] = func_12092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9786_call = mod.get_global_var('func_9786')
func_9788_call = mutated_mod.get_global_var('func_9788')
call_12115 = func_9786_call()
call_12116 = func_9786_call()
uop_12137 = relay.atanh(call_12115.astype('float64')) # shape=(12, 14, 13)
uop_12139 = relay.atanh(call_12116.astype('float64')) # shape=(12, 14, 13)
output = uop_12137
output2 = uop_12139
func_12149 = relay.Function([], output)
mod['func_12149'] = func_12149
mod = relay.transform.InferType()(mod)
output = func_12149()
func_12150 = relay.Function([], output)
mutated_mod['func_12150'] = func_12150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6125_call = mod.get_global_var('func_6125')
func_6126_call = mutated_mod.get_global_var('func_6126')
call_12157 = relay.TupleGetItem(func_6125_call(), 2)
call_12158 = relay.TupleGetItem(func_6126_call(), 2)
var_12159 = relay.var("var_12159", dtype = "uint64", shape = (2288,))#candidate|12159|(2288,)|var|uint64
bop_12160 = relay.logical_or(call_12157.astype('bool'), relay.reshape(var_12159.astype('bool'), relay.shape_of(call_12157))) # shape=(2288,)
bop_12163 = relay.logical_or(call_12158.astype('bool'), relay.reshape(var_12159.astype('bool'), relay.shape_of(call_12158))) # shape=(2288,)
output = relay.Tuple([bop_12160,])
output2 = relay.Tuple([bop_12163,])
func_12165 = relay.Function([var_12159,], output)
mod['func_12165'] = func_12165
mod = relay.transform.InferType()(mod)
var_12166 = relay.var("var_12166", dtype = "uint64", shape = (2288,))#candidate|12166|(2288,)|var|uint64
output = func_12165(var_12166)
func_12167 = relay.Function([var_12166], output)
mutated_mod['func_12167'] = func_12167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7227_call = mod.get_global_var('func_7227')
func_7228_call = mutated_mod.get_global_var('func_7228')
call_12190 = relay.TupleGetItem(func_7227_call(), 2)
call_12191 = relay.TupleGetItem(func_7228_call(), 2)
output = call_12190
output2 = call_12191
func_12200 = relay.Function([], output)
mod['func_12200'] = func_12200
mod = relay.transform.InferType()(mod)
output = func_12200()
func_12201 = relay.Function([], output)
mutated_mod['func_12201'] = func_12201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9122_call = mod.get_global_var('func_9122')
func_9123_call = mutated_mod.get_global_var('func_9123')
call_12220 = relay.TupleGetItem(func_9122_call(), 1)
call_12221 = relay.TupleGetItem(func_9123_call(), 1)
output = call_12220
output2 = call_12221
func_12233 = relay.Function([], output)
mod['func_12233'] = func_12233
mod = relay.transform.InferType()(mod)
mutated_mod['func_12233'] = func_12233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12233_call = mutated_mod.get_global_var('func_12233')
call_12234 = func_12233_call()
output = call_12234
func_12235 = relay.Function([], output)
mutated_mod['func_12235'] = func_12235
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12312 = relay.var("var_12312", dtype = "float64", shape = (11, 7, 2))#candidate|12312|(11, 7, 2)|var|float64
uop_12313 = relay.sin(var_12312.astype('float64')) # shape=(11, 7, 2)
output = relay.Tuple([uop_12313,])
output2 = relay.Tuple([uop_12313,])
func_12318 = relay.Function([var_12312,], output)
mod['func_12318'] = func_12318
mod = relay.transform.InferType()(mod)
var_12319 = relay.var("var_12319", dtype = "float64", shape = (11, 7, 2))#candidate|12319|(11, 7, 2)|var|float64
output = func_12318(var_12319)
func_12320 = relay.Function([var_12319], output)
mutated_mod['func_12320'] = func_12320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9683_call = mod.get_global_var('func_9683')
func_9685_call = mutated_mod.get_global_var('func_9685')
call_12327 = relay.TupleGetItem(func_9683_call(), 0)
call_12328 = relay.TupleGetItem(func_9685_call(), 0)
func_5865_call = mod.get_global_var('func_5865')
func_5867_call = mutated_mod.get_global_var('func_5867')
call_12334 = func_5865_call()
call_12335 = func_5865_call()
uop_12342 = relay.cosh(call_12334.astype('float64')) # shape=(12, 14, 13)
uop_12344 = relay.cosh(call_12335.astype('float64')) # shape=(12, 14, 13)
output = relay.Tuple([call_12327,uop_12342,])
output2 = relay.Tuple([call_12328,uop_12344,])
func_12348 = relay.Function([], output)
mod['func_12348'] = func_12348
mod = relay.transform.InferType()(mod)
mutated_mod['func_12348'] = func_12348
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12348_call = mutated_mod.get_global_var('func_12348')
call_12349 = func_12348_call()
output = call_12349
func_12350 = relay.Function([], output)
mutated_mod['func_12350'] = func_12350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9661_call = mod.get_global_var('func_9661')
func_9663_call = mutated_mod.get_global_var('func_9663')
call_12476 = relay.TupleGetItem(func_9661_call(), 0)
call_12477 = relay.TupleGetItem(func_9663_call(), 0)
var_12500 = relay.var("var_12500", dtype = "float64", shape = (8, 6, 12))#candidate|12500|(8, 6, 12)|var|float64
bop_12501 = relay.floor_mod(call_12476.astype('float32'), relay.reshape(var_12500.astype('float32'), relay.shape_of(call_12476))) # shape=(8, 6, 12)
bop_12504 = relay.floor_mod(call_12477.astype('float32'), relay.reshape(var_12500.astype('float32'), relay.shape_of(call_12477))) # shape=(8, 6, 12)
func_9152_call = mod.get_global_var('func_9152')
func_9154_call = mutated_mod.get_global_var('func_9154')
const_12508 = relay.const([-8.629886,-8.489274,4.987512,-3.001193,-4.005692,-7.210629,-7.255967,-5.828522,-3.043745,5.626114,-9.986208,-1.513196,-0.515015,-8.629993,-7.028138,7.938672,-9.829656,7.695318,6.865875,-7.776460,-3.106437,-4.116699,8.360409,-8.874744,-1.140231,-0.107921,-9.439444,6.099194,2.718172,-2.985634,-2.967984,-9.182368,8.368184,-7.951734,1.013378,-9.971501,5.778186,2.089088,-9.182011,-8.278435,9.231006,9.258106,4.346506,-4.203547,-3.588352,3.678012,-7.516735,-6.614240,2.910327,-8.039706,3.995235,-8.375056,-7.980737,5.885337,-2.618795,4.399982,-2.319715,9.690248,3.467344,-0.420191,-6.203972,-6.683724,7.481086,1.807215,3.419191,5.567249,-7.583619,-4.416732,1.062424,1.824616,1.679048,-9.685734,-5.670553,-7.713771,2.835813,6.604813,-0.486115,3.267579,-9.924639,-9.042678,-3.431798,-0.385840,4.486157,0.163030,-4.173070,-3.423784,6.982424,0.845193,-0.708887,-5.976700,-5.922095,-1.520571,6.115356,-7.165623,-8.269146,-6.403432,4.453832,4.088426,6.265750,5.361030,-1.072630,2.715948,-4.851418,1.513628,-2.563453,7.386894,9.815980,7.496370,8.802223,7.052219,-5.940229,-6.613219,-5.027687,2.474373,0.739538,-9.065823,-8.482822,3.002123,-4.446066,-3.835391,-5.265250,-1.260105,3.806406,9.367622,3.624947,-3.022884,-8.533513,2.283848,-6.559297,-3.948521,-0.085961,1.997297,-0.394252,1.196832,8.386497,-4.361358,5.708219,-4.114082,-5.614661,9.570605,-9.139160,-9.175577,9.313642,7.475402,-9.374361,5.276540,-8.301265,6.268414,2.101455,-3.753336,-8.219497,6.148908,5.969856,-9.916052,5.097548,4.090498,5.352323,-0.523670,-5.510602,9.711879,0.394174,7.447035,7.806220,-4.347487,8.541831,-4.350427,5.630942,-3.080297,0.098764,0.049647,-2.427122,-1.825918,-4.820884,-4.582534,-4.597151,7.487375,-9.328949,-0.804264,7.545196,5.846380,5.135901,0.511546,3.436558,9.119734,-3.968971,9.052418,3.735747,2.984333,-0.202281,-7.609162,4.019782,-3.421355,-0.820558,7.242567,5.672581,7.905270,-3.614659,-1.332291,-5.760938,-5.158485,-5.827464,2.676662,7.363008,8.541759,1.263381,6.973002,3.017894,-8.778371,-9.378076,2.529232,-3.240779,-0.748098,0.340254,-7.543271,-1.899407,8.690710,-2.577764,-7.981701,8.214533,7.712016,-6.183569,8.097082,-7.718001,7.967524,1.577160,8.842081,8.669576,2.192435,-6.973528,-3.891238,-6.827890,2.430470,2.757403,2.090832,1.189158,7.919798,4.095701,8.230561,-8.444618,-3.659835,7.509430,-8.499507,3.002348,-9.744069,1.294690,-7.860583,-7.630630,1.860655,0.688941,-5.968057,0.462758,-7.381400], dtype = "float64")#candidate|12508|(252,)|const|float64
call_12507 = relay.TupleGetItem(func_9152_call(relay.reshape(const_12508.astype('float64'), [6, 7, 6])), 1)
call_12509 = relay.TupleGetItem(func_9154_call(relay.reshape(const_12508.astype('float64'), [6, 7, 6])), 1)
output = relay.Tuple([bop_12501,call_12507,const_12508,])
output2 = relay.Tuple([bop_12504,call_12509,const_12508,])
func_12518 = relay.Function([var_12500,], output)
mod['func_12518'] = func_12518
mod = relay.transform.InferType()(mod)
mutated_mod['func_12518'] = func_12518
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12519 = relay.var("var_12519", dtype = "float64", shape = (8, 6, 12))#candidate|12519|(8, 6, 12)|var|float64
func_12518_call = mutated_mod.get_global_var('func_12518')
call_12520 = func_12518_call(var_12519)
output = call_12520
func_12521 = relay.Function([var_12519], output)
mutated_mod['func_12521'] = func_12521
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5345_call = mod.get_global_var('func_5345')
func_5346_call = mutated_mod.get_global_var('func_5346')
call_12545 = relay.TupleGetItem(func_5345_call(), 0)
call_12546 = relay.TupleGetItem(func_5346_call(), 0)
output = call_12545
output2 = call_12546
func_12560 = relay.Function([], output)
mod['func_12560'] = func_12560
mod = relay.transform.InferType()(mod)
output = func_12560()
func_12561 = relay.Function([], output)
mutated_mod['func_12561'] = func_12561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9661_call = mod.get_global_var('func_9661')
func_9663_call = mutated_mod.get_global_var('func_9663')
call_12716 = relay.TupleGetItem(func_9661_call(), 0)
call_12717 = relay.TupleGetItem(func_9663_call(), 0)
output = relay.Tuple([call_12716,])
output2 = relay.Tuple([call_12717,])
func_12734 = relay.Function([], output)
mod['func_12734'] = func_12734
mod = relay.transform.InferType()(mod)
mutated_mod['func_12734'] = func_12734
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12734_call = mutated_mod.get_global_var('func_12734')
call_12735 = func_12734_call()
output = call_12735
func_12736 = relay.Function([], output)
mutated_mod['func_12736'] = func_12736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7440_call = mod.get_global_var('func_7440')
func_7442_call = mutated_mod.get_global_var('func_7442')
call_12750 = func_7440_call()
call_12751 = func_7440_call()
output = call_12750
output2 = call_12751
func_12752 = relay.Function([], output)
mod['func_12752'] = func_12752
mod = relay.transform.InferType()(mod)
mutated_mod['func_12752'] = func_12752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12752_call = mutated_mod.get_global_var('func_12752')
call_12753 = func_12752_call()
output = call_12753
func_12754 = relay.Function([], output)
mutated_mod['func_12754'] = func_12754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12348_call = mod.get_global_var('func_12348')
func_12350_call = mutated_mod.get_global_var('func_12350')
call_12832 = relay.TupleGetItem(func_12348_call(), 0)
call_12833 = relay.TupleGetItem(func_12350_call(), 0)
func_11901_call = mod.get_global_var('func_11901')
func_11902_call = mutated_mod.get_global_var('func_11902')
call_12848 = func_11901_call()
call_12849 = func_11901_call()
output = relay.Tuple([call_12832,call_12848,])
output2 = relay.Tuple([call_12833,call_12849,])
func_12851 = relay.Function([], output)
mod['func_12851'] = func_12851
mod = relay.transform.InferType()(mod)
mutated_mod['func_12851'] = func_12851
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12851_call = mutated_mod.get_global_var('func_12851')
call_12852 = func_12851_call()
output = call_12852
func_12853 = relay.Function([], output)
mutated_mod['func_12853'] = func_12853
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11638_call = mod.get_global_var('func_11638')
func_11639_call = mutated_mod.get_global_var('func_11639')
call_12883 = relay.TupleGetItem(func_11638_call(), 0)
call_12884 = relay.TupleGetItem(func_11639_call(), 0)
output = call_12883
output2 = call_12884
func_12885 = relay.Function([], output)
mod['func_12885'] = func_12885
mod = relay.transform.InferType()(mod)
output = func_12885()
func_12886 = relay.Function([], output)
mutated_mod['func_12886'] = func_12886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12348_call = mod.get_global_var('func_12348')
func_12350_call = mutated_mod.get_global_var('func_12350')
call_12891 = relay.TupleGetItem(func_12348_call(), 1)
call_12892 = relay.TupleGetItem(func_12350_call(), 1)
output = call_12891
output2 = call_12892
func_12911 = relay.Function([], output)
mod['func_12911'] = func_12911
mod = relay.transform.InferType()(mod)
output = func_12911()
func_12912 = relay.Function([], output)
mutated_mod['func_12912'] = func_12912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4724_call = mod.get_global_var('func_4724')
func_4726_call = mutated_mod.get_global_var('func_4726')
call_12963 = relay.TupleGetItem(func_4724_call(), 0)
call_12964 = relay.TupleGetItem(func_4726_call(), 0)
output = relay.Tuple([call_12963,])
output2 = relay.Tuple([call_12964,])
func_12979 = relay.Function([], output)
mod['func_12979'] = func_12979
mod = relay.transform.InferType()(mod)
output = func_12979()
func_12980 = relay.Function([], output)
mutated_mod['func_12980'] = func_12980
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11565_call = mod.get_global_var('func_11565')
func_11567_call = mutated_mod.get_global_var('func_11567')
call_13027 = relay.TupleGetItem(func_11565_call(), 1)
call_13028 = relay.TupleGetItem(func_11567_call(), 1)
uop_13030 = relay.asin(call_13027.astype('float64')) # shape=(2, 1320)
uop_13032 = relay.asin(call_13028.astype('float64')) # shape=(2, 1320)
func_7227_call = mod.get_global_var('func_7227')
func_7228_call = mutated_mod.get_global_var('func_7228')
call_13038 = relay.TupleGetItem(func_7227_call(), 0)
call_13039 = relay.TupleGetItem(func_7228_call(), 0)
uop_13046 = relay.asinh(uop_13030.astype('float64')) # shape=(2, 1320)
uop_13048 = relay.asinh(uop_13032.astype('float64')) # shape=(2, 1320)
bop_13062 = relay.bitwise_and(uop_13046.astype('int64'), relay.reshape(uop_13030.astype('int64'), relay.shape_of(uop_13046))) # shape=(2, 1320)
bop_13065 = relay.bitwise_and(uop_13048.astype('int64'), relay.reshape(uop_13032.astype('int64'), relay.shape_of(uop_13048))) # shape=(2, 1320)
func_11565_call = mod.get_global_var('func_11565')
func_11567_call = mutated_mod.get_global_var('func_11567')
call_13066 = relay.TupleGetItem(func_11565_call(), 0)
call_13067 = relay.TupleGetItem(func_11567_call(), 0)
func_3334_call = mod.get_global_var('func_3334')
func_3338_call = mutated_mod.get_global_var('func_3338')
const_13109 = relay.const([[True,False,False,False,False,False,False,True,False,True,True,True,False,True,True,True,True,False,True,True,False,False,True,False,False,True,False,False,True,True,True,False,False,True,False,False,False,False,True,False,False,False,True,False,False,True,True,True,True,True,False,True,True,True,False,False,False,False,False,True,False,True,True,False,True,False,False,True,False,True,True,False,False,False,False,False,True,False,True,True,True,False,False,False],[True,False,False,False,True,False,True,True,False,True,True,True,True,True,False,True,False,True,False,False,True,False,False,True,False,False,False,True,False,False,False,True,True,False,True,False,True,True,True,True,False,False,False,True,True,False,False,True,True,False,False,False,True,False,True,True,False,True,True,False,False,True,False,True,True,True,True,False,False,False,True,False,False,True,True,True,True,False,False,False,False,False,True,True],[True,False,True,True,False,False,False,False,True,False,True,False,True,False,True,False,False,False,False,False,False,False,True,True,False,True,False,False,False,True,False,True,True,True,False,True,True,False,True,False,False,False,False,False,False,True,False,False,False,False,False,False,False,True,True,False,True,True,True,True,False,True,False,False,False,False,True,True,True,True,True,True,True,True,True,False,True,True,False,True,False,True,True,False],[False,False,True,True,False,False,False,False,True,False,False,True,True,False,False,False,True,True,True,False,False,True,False,True,False,True,False,False,False,True,True,False,False,False,False,False,False,False,False,True,True,True,False,False,True,False,False,False,True,True,False,True,False,True,True,True,False,True,True,False,True,False,False,True,False,False,True,False,True,True,True,False,False,True,False,True,True,False,True,False,True,False,False,False],[True,True,True,True,False,False,True,True,True,True,False,True,False,True,False,True,True,True,True,True,True,True,True,False,True,False,True,False,False,True,False,True,False,True,False,False,False,True,False,True,True,False,False,True,False,False,False,True,False,True,False,True,False,True,True,True,False,False,True,False,True,False,False,True,True,False,False,True,False,False,False,True,False,True,False,False,True,False,True,True,True,False,False,True],[True,False,False,True,False,True,False,False,True,False,True,True,False,True,False,False,True,True,True,False,False,True,False,True,True,False,True,False,False,True,True,True,True,True,True,False,True,True,False,False,True,True,True,True,True,False,False,False,True,True,False,True,True,True,False,False,True,True,True,True,True,False,False,False,False,True,False,True,False,False,True,True,False,True,True,True,True,True,True,False,False,False,True,True],[True,True,False,False,True,True,True,False,True,True,False,True,True,True,False,True,True,False,True,True,True,False,False,False,True,False,False,True,False,True,True,True,False,True,True,True,False,False,True,True,True,False,True,False,True,True,False,False,True,True,False,False,True,False,False,False,False,False,True,False,True,False,True,False,True,False,True,True,False,True,True,False,True,False,False,False,True,False,False,True,True,False,True,False]], dtype = "bool")#candidate|13109|(7, 84)|const|bool
var_13110 = relay.var("var_13110", dtype = "float32", shape = (126,))#candidate|13110|(126,)|var|float32
call_13108 = relay.TupleGetItem(func_3334_call(relay.reshape(const_13109.astype('bool'), [7, 7, 12]), relay.reshape(var_13110.astype('float32'), [126, 1]), relay.reshape(call_13027.astype('float32'), [4, 660]), ), 5)
call_13111 = relay.TupleGetItem(func_3338_call(relay.reshape(const_13109.astype('bool'), [7, 7, 12]), relay.reshape(var_13110.astype('float32'), [126, 1]), relay.reshape(call_13027.astype('float32'), [4, 660]), ), 5)
uop_13113 = relay.sqrt(uop_13046.astype('float32')) # shape=(2, 1320)
uop_13115 = relay.sqrt(uop_13048.astype('float32')) # shape=(2, 1320)
uop_13118 = relay.atanh(bop_13062.astype('float32')) # shape=(2, 1320)
uop_13120 = relay.atanh(bop_13065.astype('float32')) # shape=(2, 1320)
var_13134 = relay.var("var_13134", dtype = "float64", shape = (2, 1320))#candidate|13134|(2, 1320)|var|float64
bop_13135 = relay.floor_divide(uop_13030.astype('float64'), relay.reshape(var_13134.astype('float64'), relay.shape_of(uop_13030))) # shape=(2, 1320)
bop_13138 = relay.floor_divide(uop_13032.astype('float64'), relay.reshape(var_13134.astype('float64'), relay.shape_of(uop_13032))) # shape=(2, 1320)
func_12911_call = mod.get_global_var('func_12911')
func_12912_call = mutated_mod.get_global_var('func_12912')
call_13142 = func_12911_call()
call_13143 = func_12911_call()
output = relay.Tuple([call_13038,call_13066,call_13108,const_13109,var_13110,uop_13113,uop_13118,bop_13135,call_13142,])
output2 = relay.Tuple([call_13039,call_13067,call_13111,const_13109,var_13110,uop_13115,uop_13120,bop_13138,call_13143,])
func_13146 = relay.Function([var_13110,var_13134,], output)
mod['func_13146'] = func_13146
mod = relay.transform.InferType()(mod)
var_13147 = relay.var("var_13147", dtype = "float32", shape = (126,))#candidate|13147|(126,)|var|float32
var_13148 = relay.var("var_13148", dtype = "float64", shape = (2, 1320))#candidate|13148|(2, 1320)|var|float64
output = func_13146(var_13147,var_13148,)
func_13149 = relay.Function([var_13147,var_13148,], output)
mutated_mod['func_13149'] = func_13149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5807_call = mod.get_global_var('func_5807')
func_5809_call = mutated_mod.get_global_var('func_5809')
call_13156 = func_5807_call()
call_13157 = func_5807_call()
output = call_13156
output2 = call_13157
func_13163 = relay.Function([], output)
mod['func_13163'] = func_13163
mod = relay.transform.InferType()(mod)
output = func_13163()
func_13164 = relay.Function([], output)
mutated_mod['func_13164'] = func_13164
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7783_call = mod.get_global_var('func_7783')
func_7784_call = mutated_mod.get_global_var('func_7784')
call_13186 = relay.TupleGetItem(func_7783_call(), 0)
call_13187 = relay.TupleGetItem(func_7784_call(), 0)
output = relay.Tuple([call_13186,])
output2 = relay.Tuple([call_13187,])
func_13193 = relay.Function([], output)
mod['func_13193'] = func_13193
mod = relay.transform.InferType()(mod)
output = func_13193()
func_13194 = relay.Function([], output)
mutated_mod['func_13194'] = func_13194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5939_call = mod.get_global_var('func_5939')
func_5941_call = mutated_mod.get_global_var('func_5941')
call_13195 = func_5939_call()
call_13196 = func_5939_call()
var_13222 = relay.var("var_13222", dtype = "float32", shape = (588, 126))#candidate|13222|(588, 126)|var|float32
bop_13223 = relay.logical_or(call_13195.astype('bool'), relay.reshape(var_13222.astype('bool'), relay.shape_of(call_13195))) # shape=(588, 126)
bop_13226 = relay.logical_or(call_13196.astype('bool'), relay.reshape(var_13222.astype('bool'), relay.shape_of(call_13196))) # shape=(588, 126)
func_12734_call = mod.get_global_var('func_12734')
func_12736_call = mutated_mod.get_global_var('func_12736')
call_13232 = relay.TupleGetItem(func_12734_call(), 0)
call_13233 = relay.TupleGetItem(func_12736_call(), 0)
output = relay.Tuple([bop_13223,call_13232,])
output2 = relay.Tuple([bop_13226,call_13233,])
func_13245 = relay.Function([var_13222,], output)
mod['func_13245'] = func_13245
mod = relay.transform.InferType()(mod)
var_13246 = relay.var("var_13246", dtype = "float32", shape = (588, 126))#candidate|13246|(588, 126)|var|float32
output = func_13245(var_13246)
func_13247 = relay.Function([var_13246], output)
mutated_mod['func_13247'] = func_13247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7082_call = mod.get_global_var('func_7082')
func_7084_call = mutated_mod.get_global_var('func_7084')
call_13252 = relay.TupleGetItem(func_7082_call(), 0)
call_13253 = relay.TupleGetItem(func_7084_call(), 0)
func_8612_call = mod.get_global_var('func_8612')
func_8616_call = mutated_mod.get_global_var('func_8616')
var_13255 = relay.var("var_13255", dtype = "float64", shape = (72,))#candidate|13255|(72,)|var|float64
var_13256 = relay.var("var_13256", dtype = "uint64", shape = (2288,))#candidate|13256|(2288,)|var|uint64
call_13254 = relay.TupleGetItem(func_8612_call(relay.reshape(var_13255.astype('float64'), [72, 1]), relay.reshape(var_13256.astype('uint64'), [2288,]), ), 0)
call_13257 = relay.TupleGetItem(func_8616_call(relay.reshape(var_13255.astype('float64'), [72, 1]), relay.reshape(var_13256.astype('uint64'), [2288,]), ), 0)
func_8438_call = mod.get_global_var('func_8438')
func_8439_call = mutated_mod.get_global_var('func_8439')
call_13267 = relay.TupleGetItem(func_8438_call(), 1)
call_13268 = relay.TupleGetItem(func_8439_call(), 1)
output = relay.Tuple([call_13252,call_13254,var_13255,var_13256,call_13267,])
output2 = relay.Tuple([call_13253,call_13257,var_13255,var_13256,call_13268,])
func_13280 = relay.Function([var_13255,var_13256,], output)
mod['func_13280'] = func_13280
mod = relay.transform.InferType()(mod)
mutated_mod['func_13280'] = func_13280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13280_call = mutated_mod.get_global_var('func_13280')
var_13282 = relay.var("var_13282", dtype = "float64", shape = (72,))#candidate|13282|(72,)|var|float64
var_13283 = relay.var("var_13283", dtype = "uint64", shape = (2288,))#candidate|13283|(2288,)|var|uint64
call_13281 = func_13280_call(var_13282,var_13283,)
output = call_13281
func_13284 = relay.Function([var_13282,var_13283,], output)
mutated_mod['func_13284'] = func_13284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7659_call = mod.get_global_var('func_7659')
func_7661_call = mutated_mod.get_global_var('func_7661')
call_13293 = relay.TupleGetItem(func_7659_call(), 0)
call_13294 = relay.TupleGetItem(func_7661_call(), 0)
output = call_13293
output2 = call_13294
func_13311 = relay.Function([], output)
mod['func_13311'] = func_13311
mod = relay.transform.InferType()(mod)
mutated_mod['func_13311'] = func_13311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13311_call = mutated_mod.get_global_var('func_13311')
call_13312 = func_13311_call()
output = call_13312
func_13313 = relay.Function([], output)
mutated_mod['func_13313'] = func_13313
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11028_call = mod.get_global_var('func_11028')
func_11029_call = mutated_mod.get_global_var('func_11029')
call_13318 = relay.TupleGetItem(func_11028_call(), 6)
call_13319 = relay.TupleGetItem(func_11029_call(), 6)
output = relay.Tuple([call_13318,])
output2 = relay.Tuple([call_13319,])
func_13330 = relay.Function([], output)
mod['func_13330'] = func_13330
mod = relay.transform.InferType()(mod)
mutated_mod['func_13330'] = func_13330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13330_call = mutated_mod.get_global_var('func_13330')
call_13331 = func_13330_call()
output = call_13331
func_13332 = relay.Function([], output)
mutated_mod['func_13332'] = func_13332
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10552_call = mod.get_global_var('func_10552')
func_10553_call = mutated_mod.get_global_var('func_10553')
call_13336 = relay.TupleGetItem(func_10552_call(), 0)
call_13337 = relay.TupleGetItem(func_10553_call(), 0)
func_6509_call = mod.get_global_var('func_6509')
func_6511_call = mutated_mod.get_global_var('func_6511')
call_13338 = func_6509_call()
call_13339 = func_6509_call()
func_1209_call = mod.get_global_var('func_1209')
func_1212_call = mutated_mod.get_global_var('func_1212')
const_13352 = relay.const([-7.615739,-4.355291,0.532452,-8.327334,2.326309,5.732461,-9.650927,7.286243,2.139465,-0.134509,8.591537,9.188520,6.035949,-9.534227,9.134344,4.552203,0.685817,-4.056749,4.570811,-9.175513,7.696021,-4.351295,-9.318150,8.223835,-4.138752,9.639441,1.703644,-2.496654,9.662434,1.632094,-9.635767,-6.152777,-0.155484,-8.781095,6.371413,-5.965687,-5.082753,-0.723570,3.784131,-8.087978,0.565977,4.449955,5.028610,0.655082,-1.391253,2.595289,7.359990,8.383651,-8.467022,-2.845625,-1.305747,-9.670000,0.510694,7.408423,8.295298,-6.636485,8.045140,7.704701,2.212131,0.323057,-7.617981,-1.139452,-1.941669,9.631692,3.196184,3.079781,8.147485,9.015546,-0.678563,6.799458,-1.452518,4.802126,2.165992,-7.224262,2.968149,0.172074,-5.988958,-7.584747,4.882269,-2.865150,8.552578,-0.662689,4.769844,3.538404,-4.980740,9.024988,4.607063,-3.015848,-6.763862,0.145669,3.751523,7.942099,6.989918,-7.814491,5.192670,5.536590,-3.612142,1.217719,9.630909,-1.753033,3.693651,8.850766,-2.613400,-2.120124,-0.482898,-2.471752,-0.942901,-1.429781,4.598861,-2.869009,0.276270,0.314150,3.772060,4.423638,-1.461872,-4.860462,-6.199557,-1.997901,9.544226,9.987225,-6.885116,5.083538,7.776557,-2.016965,0.442908,2.177568,2.043296,-4.389710,-4.020405,0.919891,5.229840,-4.587380,4.205654,-3.167805,8.963765,5.194233,-8.867219,-8.733765,-9.637681,-5.207764,0.280684,-9.587399,5.084451,3.667737,-5.715501,-9.418261,-9.164497,4.284628,7.675024,5.439957,4.386430,-7.136730,6.125605,4.930510], dtype = "float64")#candidate|13352|(154,)|const|float64
call_13351 = func_1209_call(relay.reshape(const_13352.astype('float64'), [11, 7, 2]))
call_13353 = func_1209_call(relay.reshape(const_13352.astype('float64'), [11, 7, 2]))
output = relay.Tuple([call_13336,call_13338,call_13351,const_13352,])
output2 = relay.Tuple([call_13337,call_13339,call_13353,const_13352,])
func_13361 = relay.Function([], output)
mod['func_13361'] = func_13361
mod = relay.transform.InferType()(mod)
output = func_13361()
func_13362 = relay.Function([], output)
mutated_mod['func_13362'] = func_13362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9492_call = mod.get_global_var('func_9492')
func_9494_call = mutated_mod.get_global_var('func_9494')
call_13378 = func_9492_call()
call_13379 = func_9492_call()
func_6011_call = mod.get_global_var('func_6011')
func_6014_call = mutated_mod.get_global_var('func_6014')
var_13381 = relay.var("var_13381", dtype = "uint64", shape = (2288,))#candidate|13381|(2288,)|var|uint64
call_13380 = relay.TupleGetItem(func_6011_call(relay.reshape(var_13381.astype('uint64'), [2288,])), 2)
call_13382 = relay.TupleGetItem(func_6014_call(relay.reshape(var_13381.astype('uint64'), [2288,])), 2)
output = relay.Tuple([call_13378,call_13380,var_13381,])
output2 = relay.Tuple([call_13379,call_13382,var_13381,])
func_13383 = relay.Function([var_13381,], output)
mod['func_13383'] = func_13383
mod = relay.transform.InferType()(mod)
mutated_mod['func_13383'] = func_13383
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13384 = relay.var("var_13384", dtype = "uint64", shape = (2288,))#candidate|13384|(2288,)|var|uint64
func_13383_call = mutated_mod.get_global_var('func_13383')
call_13385 = func_13383_call(var_13384)
output = call_13385
func_13386 = relay.Function([var_13384], output)
mutated_mod['func_13386'] = func_13386
mutated_mod = relay.transform.InferType()(mutated_mod)
const_13396 = relay.const([[[5,1,-7,4,2,6,4,-6,9],[-6,-1,1,9,8,4,-7,1,1],[-10,-5,8,2,-1,4,-2,10,-7],[9,-8,1,-6,-1,8,-7,6,1],[-3,-7,5,2,-4,-1,3,9,6],[-5,2,-1,9,-9,10,-2,6,5],[1,-7,2,-7,7,-10,8,7,-3],[-10,-6,1,2,-9,1,8,-3,-6],[-4,-4,9,-3,-9,-8,-9,-7,9],[1,9,10,3,-1,-2,5,-10,-6],[-1,7,-1,4,-5,-5,9,6,3],[2,-3,-4,10,10,8,-8,-6,1],[-1,-7,8,-1,-7,8,4,-8,1],[-3,-3,10,10,10,-4,-5,-8,1],[6,4,2,3,-2,-2,-5,5,-7],[-9,4,7,4,4,4,-9,-9,4]],[[-5,-7,8,-9,6,10,8,4,-1],[-9,-1,-9,8,7,-1,1,8,2],[-1,8,4,3,-1,3,6,-9,6],[-5,-3,4,-1,-9,-4,4,1,-3],[2,-8,-2,7,4,-6,1,7,-4],[-8,-5,-4,6,-4,-2,2,2,-8],[-1,-4,-10,-7,4,5,-2,-2,7],[-8,6,2,9,-5,-5,7,10,5],[4,9,4,3,-4,-7,-3,-8,4],[-8,-5,6,-5,-10,-4,3,4,5],[5,-8,-3,3,-7,-4,10,-8,4],[-9,-6,-4,-1,-8,10,-5,-1,5],[7,1,-9,-8,6,6,-9,9,-3],[8,1,-10,-1,-5,9,8,7,1],[6,-7,-7,-2,-9,4,5,5,-9],[-8,-10,-5,-2,7,4,-7,9,-3]],[[-6,-3,-8,-6,-8,-9,-6,7,10],[8,-5,-3,-3,9,6,-8,-5,-7],[9,-5,6,6,-3,-9,5,6,2],[-10,4,7,-1,2,8,-10,5,-4],[1,3,2,-8,-9,8,-6,6,-10],[-9,10,9,-1,2,4,4,-5,1],[1,6,-4,3,5,-1,2,7,9],[9,5,-5,9,-6,8,-2,7,-9],[2,-2,-1,3,-2,7,-6,-3,-10],[-2,10,3,-3,7,3,-2,9,-6],[-8,-8,-1,2,-1,-10,3,-10,-10],[-1,8,-5,-7,7,-3,-10,4,-9],[-3,4,-6,-7,-6,4,-9,-1,6],[-7,-2,-10,-9,-4,-8,-8,6,9],[8,-2,4,-10,-10,8,-6,-8,-3],[-3,-1,-5,-2,2,-9,-1,-8,1]]], dtype = "int8")#candidate|13396|(3, 16, 9)|const|int8
var_13397 = relay.var("var_13397", dtype = "int8", shape = (3, 16, 9))#candidate|13397|(3, 16, 9)|var|int8
bop_13398 = relay.bitwise_or(const_13396.astype('int8'), relay.reshape(var_13397.astype('int8'), relay.shape_of(const_13396))) # shape=(3, 16, 9)
func_7391_call = mod.get_global_var('func_7391')
func_7396_call = mutated_mod.get_global_var('func_7396')
const_13402 = relay.const([-9.286405,8.919082,-2.037117,3.041971,9.705677,8.816380,1.337251,-7.848158,4.705340,3.957235,1.655054,2.646857,-0.625605,-9.916197,-8.759853,-3.473873,-5.196927,0.223025,-9.163974,-3.679240,-2.360029,8.874197,-6.290089,-1.440925,4.324522,-0.644775,3.368266,9.193568,-2.807033,-9.795311,7.826338,9.791695,-1.326562,-6.423487,5.132034,-0.666123,2.837456,5.252784,-1.628932,7.567892,5.336484,-5.985501,4.296841,-9.278962,0.057243,-5.128840,6.491982,5.272343,-1.296191,-4.551673,-8.694004,3.368336,1.397030,8.687139,-6.291002,7.212079,6.805584,6.559539,4.220992,-7.464467,-7.645881,4.535595,-8.187249,0.895189,3.845845,-8.110949,-0.617061,2.769392,-9.897127,8.588632,5.005781,1.586101,-2.730653,-5.455973,-1.541218,3.395926,1.238241,3.936424,4.214292,7.907184,-5.814254,-5.694031,2.381507,-1.949548,-0.663888,0.180914,3.675443,-2.423206,6.669577,8.077473,5.991133,-4.605758,-4.272422,-2.277106,-5.559963,-8.353567,6.275125,5.761938,-6.361048,0.056767,-0.039739,-2.927651,7.782021,1.230866,5.925966,-2.980333,4.971437,-3.985379,-8.445543,0.228317,-5.725326,-2.824328,-6.499384,-5.001013,5.199363,-0.125873,-5.291435,9.874905,5.280705,-2.273631,-6.092654,-6.302461,4.310189,2.811922,1.127858,-8.921553,-7.452115,-0.744690,2.019235,2.435639,-5.510616,-8.334259,-6.717659,-1.415862,-8.477760,8.397526,4.135403,4.592298,-2.584288,4.192672,9.573564,1.301192,-2.648563,5.654200,-0.783852,-0.280523,-7.192422,-0.282938,1.721247,-8.923180,6.974513,-9.322984,0.443150,-8.674310,-1.921844,-6.382580,4.503424,1.949852,3.246443,5.351558,0.581963,-0.393566,-0.270558,-0.264794,4.483610,-0.746774,-9.872131,0.982041,-5.325103,9.311199,2.090245,-8.020680,0.995801,-6.300695,-9.698044,1.323939,-3.618708,9.042402,-4.307549,-6.435673,9.753462,-0.923597,1.047306,9.880073,1.889727,-6.475181,-4.995578,-8.385539,-6.795708,-8.494121,-4.795090,-1.442934,6.049247,-2.434065,0.650452,3.734320,7.446910,4.635515,-9.463229,-6.553459,9.672714,-5.915913,6.244091,-1.032807,-0.001670,8.609232,-7.524462,8.602161,3.476003,0.565809,-9.979709,3.433078,-9.671389,-8.335501,-8.446699,7.140517,4.480474,1.726550,-4.466748,-9.697268,1.137572,1.795298,0.960051,6.927738,-8.895927,7.327614,-3.863813,-6.823075,3.285431,7.136625,7.228198,-6.397772,-5.709231,-9.380233,7.038350,9.468672,-3.380077,-1.472793,4.660600,-5.506115,-0.670366,-5.750210,6.419901,8.964860,6.181441,-0.267314,2.297214,0.006721,-0.835195,-2.267745,-0.515107,-5.661257,4.612379,-1.046091,7.088404,-5.084292,3.844989,-8.103602,-9.740394,4.771707,-6.300434,-6.665442,-1.939108,0.002044,9.520580,-9.511787,-0.513814,-3.288431,9.719720,-8.723576,-6.031797,-6.988002,-2.684819,-7.909806,2.243798,-9.958666,1.881355,5.501886,1.972192,-1.656898,9.955715,-3.498413,-6.769023,1.176280,-3.596068,-7.932692,-4.881392,-5.060594,6.736959,6.793804,-3.398770,-5.193927,6.245337,-4.037233,-5.993288,4.217225,1.787488,0.516569,7.256735,-3.438843,3.075764,-2.128359,5.863003,-5.995199,8.272603,2.889996,6.250087,5.122351,-1.033853,5.298773,-2.065601,-3.765916,4.880540,5.865500,-3.168999,-3.122355,-9.912407,9.635048,0.564839,-5.174528,-7.890269,-6.101279,6.834343,-9.414653,3.240131,1.834208,-5.892229,-1.397382,3.138264,-3.323016,9.466072,7.995056,4.756615,6.826305,-1.528796,0.576266,-3.107546,0.440796,9.272354,4.204052,7.583818,7.400879,-6.024347,4.231106,1.956029,7.064883,-7.583700,8.642595,1.372860,-3.162397,-2.756079,-1.444096,-5.910940,7.546590,5.425738,-9.080379,5.393589,0.599065,4.453423,2.398076,-8.314190,0.950706,-2.098791,3.880663,-8.886845,5.837756,6.243677,5.314009,1.700988,-4.517805,7.010517,-9.001042,-3.146516,-1.336102,-3.342542,-1.477091,-2.079780,-8.144271,-3.505779,-6.123958,2.522921,-8.610528,-1.546377,-7.738868,-2.429988,-4.417866,-4.385445,-3.378345,-7.384797,-3.041976,-9.577882,-1.492998,0.540869,8.712376,-4.498778,-5.999780,-6.209661,-0.455813,-2.173440,-7.198474,8.750006,-2.450849,2.288306,-5.629545,1.273122,8.778762,-9.293443,-4.108815,-0.528486,6.048598,0.535634,-0.286674,-1.168263,-0.091672,-1.094342,4.789600,-8.069625,9.756138,-1.375921,7.536586,-9.709036,-7.848034,-5.144066,-6.413377,-7.458423,4.663961,5.477615,3.604037,7.957406,-0.709413,0.328673,7.422767,0.432265,9.617082,7.835817,9.992904,3.944980,-1.648950,-8.173734,-8.281226,-5.894249,3.871975,-4.777610,-2.429677,-4.287498,7.770304,-0.595360,3.308325,9.119011,-7.820257,-8.836814,-0.924285,2.173925,4.355753,-3.818069,-0.858630,-2.564928,-4.756135,9.116774,-5.264956,-3.005973,4.065285,-3.694205,-5.260608,9.640303,-7.182476,7.633428,-5.134309,5.549710,-2.534823,9.873457,4.025613,-3.414833,-0.457768,-3.646430,-3.930130,-2.356549,4.720979,-6.504647,-7.932167,-9.216732,7.228454,-7.868712,-4.114497,-3.184704,2.500164,-6.212562,8.059438,-4.337259,-6.562754,-8.626893,8.380108,-1.303887,1.033172,3.876925,-7.094025,6.847827,2.798077,0.253519,6.653007,-9.178871,-5.568601,7.360956,-0.675137,2.402229,-6.209057,3.179651,5.919879,6.271304,-1.964589,-2.079845,-5.237907,3.442404,5.418999,-0.853705,-6.397840,0.331539,6.648240,-0.927942,5.971677,-8.956477,2.142938,0.026763,5.944058,1.836100,7.206275,-0.754326,6.408171,8.792330,1.020036,-2.015132,2.499739,-0.711883,-3.399822,-8.591398,-1.931711,-4.816510,-8.869559,-7.789345,-1.505734,4.181591,-3.637746,7.789814,9.260049,-2.813823,-2.947259,-6.707451,6.130001,-3.217130,2.511720,7.870062,5.898777,2.836626,6.199602,4.022941,-7.954166,-6.996652,6.475482,-6.921418,-8.695861,2.081321,6.960817,-4.257677,-1.364748,9.717061,0.552056,8.632190,-2.561537,-3.840937,8.356036,5.530992,3.628477,-0.323825,6.184881,1.306923,1.953432,5.484445,3.652075,5.440208,-4.372241,9.512350,3.109474,2.683367,-5.145978,-9.410530,8.865753,9.080746,7.862038,3.659684,-7.028364,-5.190034,9.614795,5.871755,-8.336079,-7.407322,1.512064,-0.351427,2.545890,-8.629510,-8.903298,1.265982,-0.165885,-4.836763,-2.504543,-8.339087,-5.775384,-4.830863,-1.233431,-9.633165,4.940531,-2.742451,3.343062,5.554802,-4.306402,-0.840280,-8.629847,-4.095275,-6.473896,-3.390419,9.463174,9.800811,-1.007799,6.077377,5.068982,0.486216,0.609543,8.597882,-4.530337,2.005055,-3.251334,1.423035,6.478400,8.975641,-9.299862,-9.256161,8.314410,-2.788187,3.877157,-7.862425,7.714231,7.021548,1.832241,5.123982,-3.397610,-7.201113,-6.671976,4.271834,-2.277398,1.666109,7.039496,-3.061835,-7.929977,-0.025206,-0.573391,-5.409736,-0.731808,-8.772626,5.107908,9.764765,-3.584923,-4.349861,-9.593042,-1.622442,5.234250,4.816959,7.285488,9.186046,-4.396861,-8.203968,-9.809088,1.675358,-3.180184,7.758479,8.614600,3.856974,-2.902966,7.164281,-6.563456,0.797007,0.113168,-1.535509,-8.909731,-6.903292,1.993194,-3.917995,-7.856733,-3.828678,4.805765,-6.013362,-0.012961,5.809579,3.311057,5.435664,-6.885618,8.422915,-4.685881,4.295039,5.315068,2.473063,-5.726012,6.437458,3.152784,8.311692,0.324145,-0.239607,-7.632831,-1.412873,-1.773262,5.104764,9.737769,-0.696676,-6.084656,-1.755120,-7.736732,-9.276402,6.276946,3.743889,0.859073,-2.998670,-6.716498,-1.826973,-1.851859,-2.140222,0.128477,9.605063,8.694582,-6.711492,8.418406,5.875390,-9.459397,-6.336662,9.010925,7.810674,9.775282,3.005195,-7.299851,-1.896654,8.732664,9.304562,-5.798827,9.579100,-2.527260,9.438392,-4.359908,6.367662,-4.691122,3.703984,6.080553,-9.279843,-8.249564,-5.551321,8.109046,2.022161,-1.386794,1.018277,1.892811,-2.743775,-8.926657,-3.793904,-7.169726,-4.142929,3.395463,8.199261,-8.705591,6.699741,3.610745,0.414378,-4.167468,7.054180,7.966387,1.553693,1.965769,-4.093230,7.894701,5.090894,1.944067,-9.527575,7.786475,2.784277,8.502502,-3.180164,1.105788,-3.853476,-0.264187,-2.342434,-8.318497,-5.939690,9.375241,-6.786068,3.213568,-3.831788,1.429134,-3.374549,-2.594265,-2.597668,-3.359314,0.231551,-7.330803,-3.826628,9.078486,-5.094384,-0.305557,-3.487282,9.839845,8.470274,-0.022034,3.975833,-4.786880,-7.014892,-7.717265,5.266999,3.548065,-1.805491,-3.119691,-0.159505,4.368176,5.907156,6.272965,5.938513,-0.611747,-4.534839,-2.032939,-2.611014,6.009712,-6.881983,9.304025,-5.434566,-7.177592,-6.081658,7.436108,-3.085640,7.034636,0.518842,8.406448,-5.675043,7.702141,-2.823107,-4.299644,-3.361926,1.449683,3.458462,-7.686010,2.920950,-7.243794,8.937106,-9.203437,-0.257529,-7.078516,0.631986,-3.782771,8.354766,-2.615928,-7.534733,0.632453,-1.374537,2.504395,5.765622,7.947593,-8.853389,9.999455,-0.015083,3.049524,0.168744,-3.240619,-4.229124,-0.987732,-5.536382,4.860980,-9.089923,6.488512,-3.812142,-8.940363,5.310192,-7.022766,-2.391877,4.614432,-1.692381,2.074677,-4.597181,-0.301749,3.799001,3.265130,5.562680,-9.735083,1.146430,-8.686557,-7.687766,8.005910,-6.783829,3.923921,7.557604,4.029078,0.485848,-9.187096,-4.124440,-0.928098,0.338019,8.197340,6.460636,-7.145275,-5.570973,-3.937913,-5.031042,-0.730983,5.100333,4.923650,-5.434733,-6.178230,3.378774,-2.278158,9.449092,6.237810,-0.210727,5.799208,-3.398808,-2.448265,-7.904974,1.264091,-2.774593,-8.451690,0.092351,8.243349,-9.730713,-7.182585,-6.932106,-2.892122,1.671942,-3.499940,-0.218318,8.706855,-5.494108,0.187218,-8.109739,2.087408,-3.178515,4.533032,7.497629,-8.627383,-7.587480,6.354228,9.528746,7.252604,-2.125609,-4.519216,3.886665,4.688189,2.828587,4.405402,-5.928204,-4.162618,-7.574328,-1.505494,-3.733492,4.851349,9.046051,6.375667,-7.244877,-0.394452,3.451342,-4.441214,-8.802248,-7.488951,-1.698030,-5.116755,-5.820963,-6.510710,-5.076130,-0.545517,9.037057,7.715312,-6.919982,3.056819,3.751666,3.503110,-7.001190,-5.158314,-0.809367,-2.391425,-1.949687,6.784645,1.618727,0.241873,-1.134035,1.551430,6.185785,2.090118,0.221443,5.288112,-5.897390,2.545252,-4.766865,1.735204,-1.405770,4.776574,-1.358235,3.812825,-1.286476,7.329766,-6.289115,-4.160150,-4.656243,-1.015096,-4.013312,-3.999329,-6.513602,3.319077,0.968593,2.876819,-6.309520,-4.384443,3.558475,1.244540,-7.009783,1.085698,8.548199,3.083506,7.199370,2.231748,0.638619,-1.999538,-7.441421,-8.052302,-2.562995,7.772402,-6.773049,-2.512918,-7.692902,-8.220023,-8.304489,3.922677,2.825433,6.491350,-1.679930,8.880070,5.073918,-0.991323,0.498243,1.351495,-8.132329,7.409976,4.638760,9.724335,5.316712,-1.816933,4.073569,9.268711,-0.365327,7.245045,2.496886,-7.216180,-0.675194,-2.449291,3.455325,1.285662,8.116684,7.598504,-3.604040,-8.662184,-7.439463,-6.064697,-6.698589,-9.681955,-1.484545,-4.489267,-6.991302,-5.120068,0.410876,7.919177,6.867564,-1.457957,2.403296,5.732533,-4.608220,6.565287,-0.031524,-6.443165,4.349764,-6.007782,-4.409257,0.175316,5.520585,1.165607,9.615542,-1.114947,-4.799610,9.442384,-2.503458,7.519472,-8.833015,3.565237,-4.163244,3.430343,-2.837922,-4.902310,-8.227818,-0.994512,4.575697,-3.502883,-7.132909,7.976114], dtype = "float64")#candidate|13402|(1100,)|const|float64
var_13403 = relay.var("var_13403", dtype = "int16", shape = (126,))#candidate|13403|(126,)|var|int16
call_13401 = relay.TupleGetItem(func_7391_call(relay.reshape(const_13402.astype('float64'), [10, 10, 11]), relay.reshape(const_13402.astype('float64'), [10, 10, 11]), relay.reshape(var_13403.astype('int16'), [126,]), ), 2)
call_13404 = relay.TupleGetItem(func_7396_call(relay.reshape(const_13402.astype('float64'), [10, 10, 11]), relay.reshape(const_13402.astype('float64'), [10, 10, 11]), relay.reshape(var_13403.astype('int16'), [126,]), ), 2)
func_10552_call = mod.get_global_var('func_10552')
func_10553_call = mutated_mod.get_global_var('func_10553')
call_13406 = relay.TupleGetItem(func_10552_call(), 0)
call_13407 = relay.TupleGetItem(func_10553_call(), 0)
output = relay.Tuple([bop_13398,call_13401,const_13402,var_13403,call_13406,])
output2 = relay.Tuple([bop_13398,call_13404,const_13402,var_13403,call_13407,])
func_13420 = relay.Function([var_13397,var_13403,], output)
mod['func_13420'] = func_13420
mod = relay.transform.InferType()(mod)
var_13421 = relay.var("var_13421", dtype = "int8", shape = (3, 16, 9))#candidate|13421|(3, 16, 9)|var|int8
var_13422 = relay.var("var_13422", dtype = "int16", shape = (126,))#candidate|13422|(126,)|var|int16
output = func_13420(var_13421,var_13422,)
func_13423 = relay.Function([var_13421,var_13422,], output)
mutated_mod['func_13423'] = func_13423
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8776_call = mod.get_global_var('func_8776')
func_8778_call = mutated_mod.get_global_var('func_8778')
call_13482 = relay.TupleGetItem(func_8776_call(), 1)
call_13483 = relay.TupleGetItem(func_8778_call(), 1)
output = call_13482
output2 = call_13483
func_13495 = relay.Function([], output)
mod['func_13495'] = func_13495
mod = relay.transform.InferType()(mod)
mutated_mod['func_13495'] = func_13495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13495_call = mutated_mod.get_global_var('func_13495')
call_13496 = func_13495_call()
output = call_13496
func_13497 = relay.Function([], output)
mutated_mod['func_13497'] = func_13497
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5939_call = mod.get_global_var('func_5939')
func_5941_call = mutated_mod.get_global_var('func_5941')
call_13564 = func_5939_call()
call_13565 = func_5939_call()
func_10308_call = mod.get_global_var('func_10308')
func_10310_call = mutated_mod.get_global_var('func_10310')
call_13568 = relay.TupleGetItem(func_10308_call(), 0)
call_13569 = relay.TupleGetItem(func_10310_call(), 0)
output = relay.Tuple([call_13564,call_13568,])
output2 = relay.Tuple([call_13565,call_13569,])
func_13579 = relay.Function([], output)
mod['func_13579'] = func_13579
mod = relay.transform.InferType()(mod)
output = func_13579()
func_13580 = relay.Function([], output)
mutated_mod['func_13580'] = func_13580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12348_call = mod.get_global_var('func_12348')
func_12350_call = mutated_mod.get_global_var('func_12350')
call_13614 = relay.TupleGetItem(func_12348_call(), 1)
call_13615 = relay.TupleGetItem(func_12350_call(), 1)
output = relay.Tuple([call_13614,])
output2 = relay.Tuple([call_13615,])
func_13621 = relay.Function([], output)
mod['func_13621'] = func_13621
mod = relay.transform.InferType()(mod)
mutated_mod['func_13621'] = func_13621
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13621_call = mutated_mod.get_global_var('func_13621')
call_13622 = func_13621_call()
output = call_13622
func_13623 = relay.Function([], output)
mutated_mod['func_13623'] = func_13623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13193_call = mod.get_global_var('func_13193')
func_13194_call = mutated_mod.get_global_var('func_13194')
call_13628 = relay.TupleGetItem(func_13193_call(), 0)
call_13629 = relay.TupleGetItem(func_13194_call(), 0)
func_11828_call = mod.get_global_var('func_11828')
func_11831_call = mutated_mod.get_global_var('func_11831')
var_13633 = relay.var("var_13633", dtype = "float32", shape = (180,))#candidate|13633|(180,)|var|float32
call_13632 = relay.TupleGetItem(func_11828_call(relay.reshape(var_13633.astype('float32'), [15, 3, 4])), 0)
call_13634 = relay.TupleGetItem(func_11831_call(relay.reshape(var_13633.astype('float32'), [15, 3, 4])), 0)
func_6560_call = mod.get_global_var('func_6560')
func_6562_call = mutated_mod.get_global_var('func_6562')
var_13652 = relay.var("var_13652", dtype = "uint64", shape = (1456,))#candidate|13652|(1456,)|var|uint64
call_13651 = relay.TupleGetItem(func_6560_call(relay.reshape(var_13652.astype('uint64'), [7, 13, 16])), 0)
call_13653 = relay.TupleGetItem(func_6562_call(relay.reshape(var_13652.astype('uint64'), [7, 13, 16])), 0)
func_13280_call = mod.get_global_var('func_13280')
func_13284_call = mutated_mod.get_global_var('func_13284')
var_13668 = relay.var("var_13668", dtype = "uint64", shape = (2288,))#candidate|13668|(2288,)|var|uint64
call_13667 = relay.TupleGetItem(func_13280_call(relay.reshape(call_13628.astype('float64'), [72,]), relay.reshape(var_13668.astype('uint64'), [2288,]), ), 1)
call_13669 = relay.TupleGetItem(func_13284_call(relay.reshape(call_13628.astype('float64'), [72,]), relay.reshape(var_13668.astype('uint64'), [2288,]), ), 1)
output = relay.Tuple([call_13628,call_13632,var_13633,call_13651,var_13652,call_13667,var_13668,])
output2 = relay.Tuple([call_13629,call_13634,var_13633,call_13653,var_13652,call_13669,var_13668,])
func_13684 = relay.Function([var_13633,var_13652,var_13668,], output)
mod['func_13684'] = func_13684
mod = relay.transform.InferType()(mod)
var_13685 = relay.var("var_13685", dtype = "float32", shape = (180,))#candidate|13685|(180,)|var|float32
var_13686 = relay.var("var_13686", dtype = "uint64", shape = (1456,))#candidate|13686|(1456,)|var|uint64
var_13687 = relay.var("var_13687", dtype = "uint64", shape = (2288,))#candidate|13687|(2288,)|var|uint64
output = func_13684(var_13685,var_13686,var_13687,)
func_13688 = relay.Function([var_13685,var_13686,var_13687,], output)
mutated_mod['func_13688'] = func_13688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11977_call = mod.get_global_var('func_11977')
func_11978_call = mutated_mod.get_global_var('func_11978')
call_13920 = relay.TupleGetItem(func_11977_call(), 0)
call_13921 = relay.TupleGetItem(func_11978_call(), 0)
output = call_13920
output2 = call_13921
func_13922 = relay.Function([], output)
mod['func_13922'] = func_13922
mod = relay.transform.InferType()(mod)
output = func_13922()
func_13923 = relay.Function([], output)
mutated_mod['func_13923'] = func_13923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5939_call = mod.get_global_var('func_5939')
func_5941_call = mutated_mod.get_global_var('func_5941')
call_13969 = func_5939_call()
call_13970 = func_5939_call()
output = relay.Tuple([call_13969,])
output2 = relay.Tuple([call_13970,])
func_13973 = relay.Function([], output)
mod['func_13973'] = func_13973
mod = relay.transform.InferType()(mod)
mutated_mod['func_13973'] = func_13973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13973_call = mutated_mod.get_global_var('func_13973')
call_13974 = func_13973_call()
output = call_13974
func_13975 = relay.Function([], output)
mutated_mod['func_13975'] = func_13975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5223_call = mod.get_global_var('func_5223')
func_5225_call = mutated_mod.get_global_var('func_5225')
call_13982 = relay.TupleGetItem(func_5223_call(), 0)
call_13983 = relay.TupleGetItem(func_5225_call(), 0)
uop_13990 = relay.sin(call_13982.astype('float32')) # shape=(7, 2, 5)
uop_13992 = relay.sin(call_13983.astype('float32')) # shape=(7, 2, 5)
func_12200_call = mod.get_global_var('func_12200')
func_12201_call = mutated_mod.get_global_var('func_12201')
call_13993 = func_12200_call()
call_13994 = func_12200_call()
output = relay.Tuple([uop_13990,call_13993,])
output2 = relay.Tuple([uop_13992,call_13994,])
func_14001 = relay.Function([], output)
mod['func_14001'] = func_14001
mod = relay.transform.InferType()(mod)
mutated_mod['func_14001'] = func_14001
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14001_call = mutated_mod.get_global_var('func_14001')
call_14002 = func_14001_call()
output = call_14002
func_14003 = relay.Function([], output)
mutated_mod['func_14003'] = func_14003
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14004 = relay.var("var_14004", dtype = "uint8", shape = (13, 3, 9))#candidate|14004|(13, 3, 9)|var|uint8
var_14005 = relay.var("var_14005", dtype = "uint8", shape = (13, 3, 9))#candidate|14005|(13, 3, 9)|var|uint8
bop_14006 = relay.subtract(var_14004.astype('uint8'), relay.reshape(var_14005.astype('uint8'), relay.shape_of(var_14004))) # shape=(13, 3, 9)
func_4386_call = mod.get_global_var('func_4386')
func_4388_call = mutated_mod.get_global_var('func_4388')
call_14009 = relay.TupleGetItem(func_4386_call(), 1)
call_14010 = relay.TupleGetItem(func_4388_call(), 1)
output = relay.Tuple([bop_14006,call_14009,])
output2 = relay.Tuple([bop_14006,call_14010,])
func_14026 = relay.Function([var_14004,var_14005,], output)
mod['func_14026'] = func_14026
mod = relay.transform.InferType()(mod)
mutated_mod['func_14026'] = func_14026
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14026_call = mutated_mod.get_global_var('func_14026')
var_14028 = relay.var("var_14028", dtype = "uint8", shape = (13, 3, 9))#candidate|14028|(13, 3, 9)|var|uint8
var_14029 = relay.var("var_14029", dtype = "uint8", shape = (13, 3, 9))#candidate|14029|(13, 3, 9)|var|uint8
call_14027 = func_14026_call(var_14028,var_14029,)
output = call_14027
func_14030 = relay.Function([var_14028,var_14029,], output)
mutated_mod['func_14030'] = func_14030
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14057 = relay.var("var_14057", dtype = "uint8", shape = ())#candidate|14057|()|var|uint8
var_14058 = relay.var("var_14058", dtype = "uint8", shape = (10, 8, 15))#candidate|14058|(10, 8, 15)|var|uint8
bop_14059 = relay.left_shift(var_14057.astype('uint8'), var_14058.astype('uint8')) # shape=(10, 8, 15)
func_1209_call = mod.get_global_var('func_1209')
func_1212_call = mutated_mod.get_global_var('func_1212')
var_14079 = relay.var("var_14079", dtype = "float64", shape = (154,))#candidate|14079|(154,)|var|float64
call_14078 = func_1209_call(relay.reshape(var_14079.astype('float64'), [11, 7, 2]))
call_14080 = func_1209_call(relay.reshape(var_14079.astype('float64'), [11, 7, 2]))
output = relay.Tuple([bop_14059,call_14078,var_14079,])
output2 = relay.Tuple([bop_14059,call_14080,var_14079,])
func_14082 = relay.Function([var_14057,var_14058,var_14079,], output)
mod['func_14082'] = func_14082
mod = relay.transform.InferType()(mod)
var_14083 = relay.var("var_14083", dtype = "uint8", shape = ())#candidate|14083|()|var|uint8
var_14084 = relay.var("var_14084", dtype = "uint8", shape = (10, 8, 15))#candidate|14084|(10, 8, 15)|var|uint8
var_14085 = relay.var("var_14085", dtype = "float64", shape = (154,))#candidate|14085|(154,)|var|float64
output = func_14082(var_14083,var_14084,var_14085,)
func_14086 = relay.Function([var_14083,var_14084,var_14085,], output)
mutated_mod['func_14086'] = func_14086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9336_call = mod.get_global_var('func_9336')
func_9338_call = mutated_mod.get_global_var('func_9338')
call_14126 = func_9336_call()
call_14127 = func_9336_call()
output = relay.Tuple([call_14126,])
output2 = relay.Tuple([call_14127,])
func_14134 = relay.Function([], output)
mod['func_14134'] = func_14134
mod = relay.transform.InferType()(mod)
output = func_14134()
func_14135 = relay.Function([], output)
mutated_mod['func_14135'] = func_14135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5906_call = mod.get_global_var('func_5906')
func_5908_call = mutated_mod.get_global_var('func_5908')
call_14145 = relay.TupleGetItem(func_5906_call(), 0)
call_14146 = relay.TupleGetItem(func_5908_call(), 0)
func_2300_call = mod.get_global_var('func_2300')
func_2302_call = mutated_mod.get_global_var('func_2302')
const_14156 = relay.const([-6.817097,1.481248,0.184831,-5.824954,3.853895,-2.605843,-5.837554,-4.091044,-0.287760,7.755803,8.595020,7.794223,0.688057,9.453638,0.761382,6.345185,-5.094579,5.733123,-4.436815,-1.387510,9.219648,-3.810252,-3.646105,0.992369,1.526450,4.655982,-5.550944,0.877577,-7.581676,-0.022522,-7.122886,9.950331,-5.886308,-8.132196,-2.873425,-1.363013,-3.833323,8.230243,-9.669814,5.974459,-7.038719,-9.285695,0.735625,-9.613715,-4.232939,-2.054667,3.772426,2.991245,-7.435454,-4.687272,5.512859,3.572293,3.552984,-8.063668,8.660048,0.361572,-4.168946,-4.660242,6.355239,4.194875,8.468551,-3.974050,7.209896,-2.808107,-6.538681,6.579181,-4.786612,6.076276,0.627288,0.245148,4.425955,-7.689406,-5.838978,4.529802,-8.174110,3.465921,-4.936724,-2.139027,6.994194,-8.549405,3.588708,8.161942,-8.130512,4.184096,-1.920802,-5.387719,-8.122534,-8.064297,1.234185,-1.539358,-2.118532,9.892345,-0.562594,9.791425,-3.649591,0.384878,7.000913,0.312699,3.981021,5.033792,1.066569,4.057303,1.825435,-7.732852,3.218838,-1.007410,-6.079593,7.942776,0.904752,0.266547,-7.180565,0.327887,3.393845,0.080052,7.951977,8.137802,-3.796418,-2.682575,-1.032686,-0.214336,-9.928783,5.027546,-8.242489,3.275936,1.836141,9.513115,1.434334,9.899408,-6.671175,2.873046,-8.786970,-8.734053,2.130901,-3.779464,-4.982011,8.691708,7.057525,3.136358,0.285760,5.490011,2.112376,-6.281511,9.963771,-3.446105,-1.377168,0.180542,-0.850215,5.048924,4.230896,0.266852,-3.277907,-0.149314,3.986288,2.249892,-7.200963,-6.988930,-0.503526,-1.586979,-1.199428,1.630682,-9.881932,7.456240,-2.437305,-2.758760,-3.800973,6.667368,-1.109818,-7.007777,-9.268544,5.647273,-6.121112,-2.006251,-2.957269,-8.624192,4.356288,-3.846667,6.390381,-8.251090,-1.910192,8.034373,-5.818208,-1.800131,-0.269271,8.617282,-4.044308,4.957799,-1.978393,3.097050,-2.904103,0.776019,3.698296,4.616583,-7.832068,4.143976,-1.318884,4.238275], dtype = "float64")#candidate|14156|(196,)|const|float64
call_14155 = func_2300_call(relay.reshape(const_14156.astype('float64'), [7, 14, 2]))
call_14157 = func_2300_call(relay.reshape(const_14156.astype('float64'), [7, 14, 2]))
output = relay.Tuple([call_14145,call_14155,const_14156,])
output2 = relay.Tuple([call_14146,call_14157,const_14156,])
func_14159 = relay.Function([], output)
mod['func_14159'] = func_14159
mod = relay.transform.InferType()(mod)
output = func_14159()
func_14160 = relay.Function([], output)
mutated_mod['func_14160'] = func_14160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8232_call = mod.get_global_var('func_8232')
func_8233_call = mutated_mod.get_global_var('func_8233')
call_14226 = relay.TupleGetItem(func_8232_call(), 0)
call_14227 = relay.TupleGetItem(func_8233_call(), 0)
func_7277_call = mod.get_global_var('func_7277')
func_7279_call = mutated_mod.get_global_var('func_7279')
call_14238 = relay.TupleGetItem(func_7277_call(), 0)
call_14239 = relay.TupleGetItem(func_7279_call(), 0)
output = relay.Tuple([call_14226,call_14238,])
output2 = relay.Tuple([call_14227,call_14239,])
func_14252 = relay.Function([], output)
mod['func_14252'] = func_14252
mod = relay.transform.InferType()(mod)
mutated_mod['func_14252'] = func_14252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14252_call = mutated_mod.get_global_var('func_14252')
call_14253 = func_14252_call()
output = call_14253
func_14254 = relay.Function([], output)
mutated_mod['func_14254'] = func_14254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5223_call = mod.get_global_var('func_5223')
func_5225_call = mutated_mod.get_global_var('func_5225')
call_14283 = relay.TupleGetItem(func_5223_call(), 0)
call_14284 = relay.TupleGetItem(func_5225_call(), 0)
func_7553_call = mod.get_global_var('func_7553')
func_7555_call = mutated_mod.get_global_var('func_7555')
var_14305 = relay.var("var_14305", dtype = "float64", shape = (3, 20))#candidate|14305|(3, 20)|var|float64
call_14304 = relay.TupleGetItem(func_7553_call(relay.reshape(var_14305.astype('float64'), [60,])), 1)
call_14306 = relay.TupleGetItem(func_7555_call(relay.reshape(var_14305.astype('float64'), [60,])), 1)
output = relay.Tuple([call_14283,call_14304,var_14305,])
output2 = relay.Tuple([call_14284,call_14306,var_14305,])
func_14312 = relay.Function([var_14305,], output)
mod['func_14312'] = func_14312
mod = relay.transform.InferType()(mod)
var_14313 = relay.var("var_14313", dtype = "float64", shape = (3, 20))#candidate|14313|(3, 20)|var|float64
output = func_14312(var_14313)
func_14314 = relay.Function([var_14313], output)
mutated_mod['func_14314'] = func_14314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10308_call = mod.get_global_var('func_10308')
func_10310_call = mutated_mod.get_global_var('func_10310')
call_14324 = relay.TupleGetItem(func_10308_call(), 2)
call_14325 = relay.TupleGetItem(func_10310_call(), 2)
func_10743_call = mod.get_global_var('func_10743')
func_10747_call = mutated_mod.get_global_var('func_10747')
const_14351 = relay.const([-3,-8,9,2,9,-1,4,5,9,-5,8,2,-5,4,-4,-4,6,-10,7,4,-6,4,-4,7,3,-4,6,-6,9,-9,-7,-9,-6,-7,-3,-8,-8,10,5,7,1,-8,7,10,-8,-10,3,-5,10,-1,-4,1,5,-6,-1,6,-6,9,-2,1,7,4,-3,-6,-2,-6,-7,-10,10,-3,-9,-1,5,10,6,-9,5,2,4,-2,6,-5,-7,-5,9,6,-9,4,-4,3,-8,-4,6,2,3,-8,-4,-1,-8,-5,-4,-6,5,-7,6,10,2,6,7,10,2,6,1,-4,-4,3,-10,-3,10,-4,1,8,-8,-3,-4,3,-9,1,-8,8,-6,4,-1,-10,10,-7,8,6,2,10,-2,-2,-4,2,10,6,10,-3,-8,2,-7,-8,-4,10,4,4,3,-9,-8,10,9,-7,7,-10,1,2,-2,-2,7,-4,1,8,-1,10,-8,-1,-8,7,-6,-2,-10,-6,7,9,-9,-4,1,4,-1,-5,-9,-5,5,-4,-1,-10,1,3,4,-1,-5,5,8,-9,-8,-7,1,3,6,-6,4,-7,-2,2,-2,-10,9,-4,9,-8,-8,-3,7,-2,3,-9,4,1,-6,-3,-5,5,2,-5,-3,-7,7,9,-6,-8,-10,6,-3,-3,10,-7,-1,-1,4,-2,-10,-9,9,-5,-10,3,-2,-8,-4,3,-7,8,-5,-8,6,5,9,5,3,-2,-2,4,4,6,3,1,-2,-5,-2,3,5,4,-1,3,-8,6,9,-2,2,-10,-9,-4,-2,7,1,1,-7,1,5,-3,-8,1,-3,-2,-2,9,-5,-4,1,2,1,-10,-10,10,5,-8,-4,-2,-5,1,7,1,-4,-1,-4,9,-6,-6,9,4,9,9,-5,2,3,5,7,2,-1,-8,-5,2,7,-2,4,-2,-9,10,-2,-4,-10,-7,-7,8,-3,2,-5,-3,-4,3,-10,3,-8,5,-7,-4,-8,-2,1,2,10,4,-10,-10,-2,2,-9,-5], dtype = "int8")#candidate|14351|(378,)|const|int8
var_14352 = relay.var("var_14352", dtype = "float64", shape = (3, 24))#candidate|14352|(3, 24)|var|float64
call_14350 = relay.TupleGetItem(func_10743_call(relay.reshape(const_14351.astype('int8'), [378,]), relay.reshape(var_14352.astype('float64'), [72,]), ), 3)
call_14353 = relay.TupleGetItem(func_10747_call(relay.reshape(const_14351.astype('int8'), [378,]), relay.reshape(var_14352.astype('float64'), [72,]), ), 3)
output = relay.Tuple([call_14324,call_14350,const_14351,var_14352,])
output2 = relay.Tuple([call_14325,call_14353,const_14351,var_14352,])
func_14373 = relay.Function([var_14352,], output)
mod['func_14373'] = func_14373
mod = relay.transform.InferType()(mod)
var_14374 = relay.var("var_14374", dtype = "float64", shape = (3, 24))#candidate|14374|(3, 24)|var|float64
output = func_14373(var_14374)
func_14375 = relay.Function([var_14374], output)
mutated_mod['func_14375'] = func_14375
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14416 = relay.var("var_14416", dtype = "bool", shape = (10, 8, 10))#candidate|14416|(10, 8, 10)|var|bool
var_14417 = relay.var("var_14417", dtype = "bool", shape = (10, 8, 10))#candidate|14417|(10, 8, 10)|var|bool
bop_14418 = relay.logical_and(var_14416.astype('bool'), relay.reshape(var_14417.astype('bool'), relay.shape_of(var_14416))) # shape=(10, 8, 10)
func_7299_call = mod.get_global_var('func_7299')
func_7301_call = mutated_mod.get_global_var('func_7301')
call_14425 = relay.TupleGetItem(func_7299_call(), 1)
call_14426 = relay.TupleGetItem(func_7301_call(), 1)
func_13621_call = mod.get_global_var('func_13621')
func_13623_call = mutated_mod.get_global_var('func_13623')
call_14454 = relay.TupleGetItem(func_13621_call(), 0)
call_14455 = relay.TupleGetItem(func_13623_call(), 0)
output = relay.Tuple([bop_14418,call_14425,call_14454,])
output2 = relay.Tuple([bop_14418,call_14426,call_14455,])
func_14456 = relay.Function([var_14416,var_14417,], output)
mod['func_14456'] = func_14456
mod = relay.transform.InferType()(mod)
var_14457 = relay.var("var_14457", dtype = "bool", shape = (10, 8, 10))#candidate|14457|(10, 8, 10)|var|bool
var_14458 = relay.var("var_14458", dtype = "bool", shape = (10, 8, 10))#candidate|14458|(10, 8, 10)|var|bool
output = func_14456(var_14457,var_14458,)
func_14459 = relay.Function([var_14457,var_14458,], output)
mutated_mod['func_14459'] = func_14459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10536_call = mod.get_global_var('func_10536')
func_10538_call = mutated_mod.get_global_var('func_10538')
call_14461 = relay.TupleGetItem(func_10536_call(), 0)
call_14462 = relay.TupleGetItem(func_10538_call(), 0)
func_9122_call = mod.get_global_var('func_9122')
func_9123_call = mutated_mod.get_global_var('func_9123')
call_14473 = relay.TupleGetItem(func_9122_call(), 1)
call_14474 = relay.TupleGetItem(func_9123_call(), 1)
output = relay.Tuple([call_14461,call_14473,])
output2 = relay.Tuple([call_14462,call_14474,])
func_14483 = relay.Function([], output)
mod['func_14483'] = func_14483
mod = relay.transform.InferType()(mod)
output = func_14483()
func_14484 = relay.Function([], output)
mutated_mod['func_14484'] = func_14484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11565_call = mod.get_global_var('func_11565')
func_11567_call = mutated_mod.get_global_var('func_11567')
call_14557 = relay.TupleGetItem(func_11565_call(), 1)
call_14558 = relay.TupleGetItem(func_11567_call(), 1)
output = call_14557
output2 = call_14558
func_14559 = relay.Function([], output)
mod['func_14559'] = func_14559
mod = relay.transform.InferType()(mod)
mutated_mod['func_14559'] = func_14559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14559_call = mutated_mod.get_global_var('func_14559')
call_14560 = func_14559_call()
output = call_14560
func_14561 = relay.Function([], output)
mutated_mod['func_14561'] = func_14561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6551_call = mod.get_global_var('func_6551')
func_6552_call = mutated_mod.get_global_var('func_6552')
call_14575 = relay.TupleGetItem(func_6551_call(), 1)
call_14576 = relay.TupleGetItem(func_6552_call(), 1)
output = call_14575
output2 = call_14576
func_14587 = relay.Function([], output)
mod['func_14587'] = func_14587
mod = relay.transform.InferType()(mod)
mutated_mod['func_14587'] = func_14587
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14587_call = mutated_mod.get_global_var('func_14587')
call_14588 = func_14587_call()
output = call_14588
func_14589 = relay.Function([], output)
mutated_mod['func_14589'] = func_14589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13579_call = mod.get_global_var('func_13579')
func_13580_call = mutated_mod.get_global_var('func_13580')
call_14606 = relay.TupleGetItem(func_13579_call(), 0)
call_14607 = relay.TupleGetItem(func_13580_call(), 0)
var_14610 = relay.var("var_14610", dtype = "float32", shape = (588, 126))#candidate|14610|(588, 126)|var|float32
bop_14611 = relay.equal(call_14606.astype('bool'), relay.reshape(var_14610.astype('bool'), relay.shape_of(call_14606))) # shape=(588, 126)
bop_14614 = relay.equal(call_14607.astype('bool'), relay.reshape(var_14610.astype('bool'), relay.shape_of(call_14607))) # shape=(588, 126)
bop_14637 = relay.mod(var_14610.astype('float32'), relay.reshape(call_14606.astype('float32'), relay.shape_of(var_14610))) # shape=(588, 126)
bop_14640 = relay.mod(var_14610.astype('float32'), relay.reshape(call_14607.astype('float32'), relay.shape_of(var_14610))) # shape=(588, 126)
output = relay.Tuple([bop_14611,bop_14637,])
output2 = relay.Tuple([bop_14614,bop_14640,])
func_14646 = relay.Function([var_14610,], output)
mod['func_14646'] = func_14646
mod = relay.transform.InferType()(mod)
mutated_mod['func_14646'] = func_14646
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14647 = relay.var("var_14647", dtype = "float32", shape = (588, 126))#candidate|14647|(588, 126)|var|float32
func_14646_call = mutated_mod.get_global_var('func_14646')
call_14648 = func_14646_call(var_14647)
output = call_14648
func_14649 = relay.Function([var_14647], output)
mutated_mod['func_14649'] = func_14649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7783_call = mod.get_global_var('func_7783')
func_7784_call = mutated_mod.get_global_var('func_7784')
call_14673 = relay.TupleGetItem(func_7783_call(), 0)
call_14674 = relay.TupleGetItem(func_7784_call(), 0)
func_910_call = mod.get_global_var('func_910')
func_914_call = mutated_mod.get_global_var('func_914')
const_14685 = relay.const([4.595311,1.896563,5.852920,8.117788,3.856629,2.671297,-3.322617,-8.147811,-7.215797,-2.897102,4.482794,-2.008164,9.617010,-9.217873,4.247622,0.388827,-0.714947,8.994746,7.725870,-9.514756,-4.917434,3.243512,2.617594,-7.838647,-2.109334,-8.801617,-5.555634,-5.184824,7.335884,-7.750963,-1.847111,-4.917083,-2.849179,3.072142,-1.420275,-5.915337,2.149493,9.676721,6.850041,-2.966169,8.728761,-9.815028,-6.672902,7.181508,4.118642,-7.782186,2.638661,-6.682900,-1.260454,5.548325,3.073299,5.720460,3.311997,3.144933,-4.357308,-6.588976,1.779733,1.858665,-1.961063,0.111441,-3.641097,1.456903,-7.851418,-5.263333,3.926002,-6.980867,0.908789,-6.264203,-3.104554,-2.752664,3.530082,-0.062457,3.388992,-4.040298,-7.980203,9.835188,-6.649889,2.293490,4.368395,5.966598,5.781446,5.028970,-1.107614,-1.423078,-2.230922,2.342044,5.118464,-3.565421,-4.337758,-6.663430,-5.156741,4.549364,9.238653,-5.837977,-1.366554,3.108825,5.734941,0.194805,-0.770660,-7.742026,-1.832863,4.107967,-2.871845,-4.182623,-6.165970,8.491820,-5.658043,1.779317,3.349700,-9.459587,-2.703814,-0.952607,6.900131,4.969865,7.014047,-9.578227,0.867038,7.871753,7.326922,-5.849478,8.847105,-5.612356,1.434786,6.801117,0.447960,-7.537934,7.454429,2.390528,-9.424894,6.917250,1.745503,6.014801,7.997163,-8.563254,-7.909029,-5.316173,-7.559683,-7.298274,9.444153,3.023160,0.657890,-9.704350,-1.855728,5.118533,-4.078109,-9.436024,-8.740692,-0.822672,-7.204032,-3.219338,-3.144435,-9.358965,-2.058657,-6.875447,-5.813570,-9.957608,0.237564,9.906019,4.561327,6.687334,2.901725,9.679342,6.697767,2.525322,-7.687212,9.086138,-4.438355,0.066302,-2.901066,-9.352632,0.951574,-9.449992,7.072965,-4.520006,1.789863,-6.323983,4.707064,-7.618491,-9.162836,9.298275,-7.720339,9.424668,-3.418361,9.152875,-6.018604,-9.797908,-9.408577,-3.696848,-9.412476,-9.971150,-4.847247,-2.246495,-8.581478,7.108166,-4.857791,6.946797,0.657989,2.222449,-5.372786,-7.056565], dtype = "float64")#candidate|14685|(200,)|const|float64
call_14684 = relay.TupleGetItem(func_910_call(relay.reshape(const_14685.astype('float64'), [2, 10, 10]), relay.reshape(const_14685.astype('float64'), [2, 10, 10]), ), 0)
call_14686 = relay.TupleGetItem(func_914_call(relay.reshape(const_14685.astype('float64'), [2, 10, 10]), relay.reshape(const_14685.astype('float64'), [2, 10, 10]), ), 0)
func_8776_call = mod.get_global_var('func_8776')
func_8778_call = mutated_mod.get_global_var('func_8778')
call_14695 = relay.TupleGetItem(func_8776_call(), 1)
call_14696 = relay.TupleGetItem(func_8778_call(), 1)
output = relay.Tuple([call_14673,call_14684,const_14685,call_14695,])
output2 = relay.Tuple([call_14674,call_14686,const_14685,call_14696,])
func_14703 = relay.Function([], output)
mod['func_14703'] = func_14703
mod = relay.transform.InferType()(mod)
mutated_mod['func_14703'] = func_14703
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14703_call = mutated_mod.get_global_var('func_14703')
call_14704 = func_14703_call()
output = call_14704
func_14705 = relay.Function([], output)
mutated_mod['func_14705'] = func_14705
mutated_mod = relay.transform.InferType()(mutated_mod)
const_14711 = relay.const([[[-3.288881,-9.083662,5.455956,6.454984,8.922431,-9.539059,-9.342848],[-8.757859,5.940270,3.507905,1.330365,-4.961130,-6.453181,1.273128],[4.747888,0.769405,-7.131136,1.090508,-4.350560,5.197023,-6.818619],[1.568573,3.204952,6.234018,4.415138,-8.867061,2.440847,-9.260341],[-4.201281,5.504351,-8.006726,5.322357,-0.220444,-2.207735,7.055682],[5.207649,5.133476,-4.050611,-5.105402,7.591604,4.834491,8.073014],[7.066293,-9.354825,9.519010,6.477367,-9.161906,3.719156,2.481736],[8.228290,1.630785,-1.787415,0.652471,-0.523791,-1.329879,3.112120],[5.684020,-2.686421,5.136322,-8.687677,7.471142,-6.419514,-7.533744],[-3.401206,-0.649922,4.204907,-3.148453,-6.878373,-9.064394,-3.467646],[0.062622,-0.917599,-7.347705,9.252231,-3.143866,-7.551773,5.214974],[4.770775,-9.261978,7.547585,-4.973143,0.105131,-2.408716,-7.675834]],[[-7.472646,4.911699,0.929629,-4.257049,5.213735,4.719120,-4.837733],[6.386504,-7.627043,8.263701,-8.884437,2.584606,1.378826,-4.549182],[7.573467,0.905151,8.338319,9.609630,-9.261117,-7.430726,9.068613],[2.252618,2.983098,3.787335,-7.223735,2.651956,8.442599,2.339691],[1.903180,-8.258524,-5.244553,-7.764153,-4.665221,-2.845264,2.690403],[-0.438934,-9.797940,-6.138814,-9.943958,-7.597529,2.451665,-8.859205],[-2.369713,7.089857,1.642302,-6.613988,5.593170,4.465292,-6.465517],[5.034017,-1.800712,-6.726405,9.495217,-1.640554,-4.667179,-2.546081],[-0.943669,-2.952036,-9.368472,-9.633989,0.612922,-7.890585,2.963308],[0.123621,9.280376,-1.529974,-8.163369,7.836168,4.723476,-9.593351],[-7.113077,1.454946,1.538907,1.135813,-1.609272,2.509951,2.368769],[-3.205293,2.466958,-9.776584,-7.783725,-3.907319,-7.408031,9.616120]],[[4.924877,1.285882,-5.560141,3.561595,2.274139,-9.352519,-6.311156],[0.543849,5.923984,5.039200,2.393548,3.896084,-1.959832,0.242947],[5.515921,-2.730793,-9.667236,-8.488594,0.824271,-0.457875,0.665837],[-8.926952,-3.703781,3.720871,8.778915,-8.698511,-1.212292,3.816497],[8.044982,3.351378,5.875007,6.631608,-4.645717,-6.746762,1.233228],[-0.620510,0.984326,1.844796,-0.766360,0.089342,8.176941,9.412082],[-9.232530,-8.131514,5.089686,-8.628900,1.700030,-2.690623,-0.385721],[1.495441,7.037333,-6.347746,-4.067224,-1.585270,-9.071144,6.211609],[3.851796,6.232118,2.750464,4.466952,-2.663199,7.270333,1.554790],[7.124320,-8.557191,-9.720033,-8.792035,4.053061,-8.954463,0.301102],[1.858942,-7.155897,2.462628,-8.055092,6.131441,3.784990,-1.812278],[7.548876,-0.380582,4.089198,-3.039992,-3.628877,-0.323354,1.335743]],[[5.183368,6.896454,6.396902,8.223405,1.918958,4.198651,5.375619],[-5.374919,5.421221,-7.933786,-4.533096,2.769425,9.010990,7.467655],[1.391892,-9.951231,-0.204574,1.658360,9.705700,-6.498557,8.325762],[1.341012,8.136313,-5.815233,6.518939,-8.824598,-1.006139,-1.075940],[-0.123270,0.232886,1.868189,-2.879460,0.202398,0.889834,0.139973],[9.747606,-0.949259,5.430888,0.797797,-2.963450,-2.239751,-9.392839],[-2.890941,-2.259953,3.584379,-6.197065,8.230401,-5.490704,1.108971],[7.720208,0.751983,3.419247,3.109013,7.682776,-8.238058,-2.049510],[0.487937,9.922352,0.191332,-7.829707,7.972339,0.400426,4.689231],[0.512643,-5.100813,6.032012,9.603871,9.589296,-4.606002,6.386832],[-5.695704,5.443524,1.161107,-5.272376,2.244529,9.809708,3.896356],[4.016133,-4.026739,8.669271,-8.022544,-1.827947,9.450575,-8.237484]],[[1.410190,-9.746614,2.005667,7.036694,-1.743486,-3.715678,-5.982905],[-8.283773,-2.068011,-2.958142,-8.246125,4.855677,4.342318,9.829969],[0.879763,-7.445760,2.679093,8.159697,-5.380987,8.640725,-4.237970],[-1.544972,1.346701,-6.163058,2.711886,-7.292459,8.391704,-3.488849],[-9.648157,2.336627,1.299943,-4.319833,1.648569,-0.210801,-1.291355],[-1.000274,7.563329,0.483616,-1.273826,-1.373758,-1.068226,5.717230],[6.729222,-5.746122,4.261215,7.494212,7.096867,-7.832908,4.335740],[2.032155,-0.029154,-3.325131,-3.781999,7.299683,-0.677865,-4.612829],[-8.251333,-1.061137,9.506218,4.468834,-6.101989,-7.593076,-9.416198],[-1.495206,6.716085,0.273042,-8.415264,4.362602,2.777002,6.288756],[-5.892888,4.580524,0.055231,-5.711055,-4.180939,-4.178615,5.604446],[8.121412,4.780100,6.525869,0.020309,-3.482840,8.719912,-5.514851]],[[-6.826525,-7.256341,-9.268686,-4.663861,8.013273,-5.063645,-4.927198],[-7.863965,7.547300,-6.901440,-2.102221,5.201309,-0.762359,5.174722],[3.439950,1.653727,5.958768,6.052004,6.240124,6.065156,-0.704835],[-6.951238,-0.272177,-6.534636,-3.113565,-6.780538,4.601968,-8.647650],[-6.770193,7.474631,-9.788771,7.321082,-6.538912,3.876944,-1.067006],[-6.257613,-8.601059,-1.845067,0.845358,8.490249,6.893130,-6.080406],[5.129722,-0.325710,-5.878762,-1.576894,-1.256533,-2.828769,-0.227748],[-8.659638,0.895662,0.039002,-6.486484,-3.113309,2.712396,5.060150],[-4.552986,6.128133,8.038473,9.610792,2.479763,-2.056287,4.865330],[-1.020407,-8.093217,8.657992,5.701225,7.096492,-9.704038,0.865479],[4.121183,-8.769278,9.288208,-8.828414,3.127846,-3.617352,6.546001],[3.021922,-5.059010,-3.260720,-8.586125,-5.337527,-0.806086,2.647755]],[[8.627525,-2.542897,-2.154441,-2.743006,-6.254242,-7.327838,-5.674561],[-6.690147,4.684444,1.416441,7.985587,-4.838463,0.295519,0.075952],[-3.785645,-3.630349,-5.367749,5.642280,0.979325,-3.621961,-6.927001],[2.819807,1.811242,-2.807225,0.029113,-0.729547,5.103637,2.314338],[4.410890,-0.465905,0.631839,-7.501064,-7.586985,-4.398576,8.060072],[1.318779,9.449684,2.762697,8.287021,7.328045,8.093972,1.722510],[-3.529718,4.149110,-8.602189,-2.349085,-5.567136,4.298323,-8.812695],[-2.316559,-5.977669,9.697390,-1.944770,-1.998852,-0.594567,2.212164],[-4.309239,-3.883721,9.927786,-9.570696,1.012573,5.154544,4.689137],[-6.785339,4.372203,-1.873910,2.083465,0.285865,-8.257703,5.608545],[-5.002850,-0.593944,5.974410,6.164361,-1.780977,-3.685731,-6.415703],[7.667053,-6.893508,1.573139,-0.590749,7.488659,3.982108,5.435879]],[[3.640663,-8.720354,8.116264,-3.016905,3.746542,0.670889,6.451845],[-1.081096,-9.553218,-8.982039,4.088065,-9.935394,5.727380,0.425252],[-2.666662,-3.686305,3.124546,1.667871,0.316762,-2.222168,-9.470786],[-5.318388,8.704700,1.883242,-6.034134,3.502374,-1.854625,5.115287],[6.856583,-9.980988,3.931863,7.076429,-7.431595,-5.418026,-4.705132],[-2.119148,-8.581936,4.197540,8.235611,6.854609,-9.288630,-8.648489],[-0.806412,-2.459570,-2.425483,-6.715901,1.695117,5.581587,-5.794092],[5.206825,-9.385410,2.907635,-8.485034,-8.264815,-6.263011,1.695796],[-8.163436,5.282067,5.997712,0.055425,-4.978183,2.999646,3.898968],[9.918878,-1.041267,1.204979,5.919220,-6.473298,3.033125,3.026468],[-8.162086,-3.699457,-5.328936,-4.369560,2.348077,-3.646407,5.998930],[2.498533,-4.016556,-2.605870,0.106028,6.048734,6.306944,-4.773524]],[[-8.567078,-5.594378,-3.054832,-6.916245,-7.330274,-5.230949,-6.951045],[4.423164,-2.969510,-7.883631,-1.453167,-8.617682,-6.175948,-8.598210],[7.190840,-4.369377,-8.282937,-7.771524,7.164494,-0.310261,4.701731],[7.349814,1.409015,5.930968,0.587991,-6.385397,5.049304,1.173884],[-9.785224,7.690933,-1.998897,5.609954,-1.476461,6.430095,-3.487497],[4.929439,-7.518707,6.567533,9.185816,-3.176271,9.844386,-3.714496],[8.862415,-4.467179,0.379024,4.935936,-1.088385,9.102989,-2.284269],[-6.597474,-2.580346,3.360289,6.672552,-1.378952,9.866761,9.835703],[9.106506,8.261660,-3.716017,-0.552301,8.425424,0.029092,-6.658423],[-1.787266,-5.556573,-9.381370,-3.524353,2.060719,-4.058875,2.140883],[-6.858033,-1.583362,-1.618997,-9.936832,-4.310982,0.436818,-8.363755],[7.777048,5.338444,-0.270537,-4.213118,-6.607722,-2.823347,-3.572811]],[[8.739607,-2.246093,2.554670,1.025939,0.237106,-5.998193,-2.714214],[8.492297,-2.624769,4.830752,2.557733,0.690333,-7.989861,-0.218689],[-5.013144,-5.805686,-7.989485,0.341995,7.913278,-6.393625,4.982438],[-3.742138,-3.136983,-1.388055,-3.046689,-8.158234,6.544725,-5.602991],[8.323649,-5.418133,5.017140,1.403480,-4.031598,1.102477,7.121511],[-5.714849,-1.909676,-7.855560,-1.451165,-0.232198,-5.011148,-4.011657],[-4.711848,-3.277739,-2.044311,3.497871,2.752507,9.979219,-1.463051],[9.702626,-4.941266,-3.432985,5.582360,4.732882,3.372301,-2.231397],[-4.915413,-5.436079,5.624647,-6.453572,6.831972,-0.155410,-9.464852],[-4.251240,-2.902659,-4.977704,9.797323,-3.975708,1.325122,5.629335],[1.106239,0.230631,-4.402932,-3.915702,-6.137128,6.058243,6.299063],[-5.198103,-8.249827,-3.784158,-0.792938,0.657386,0.708509,-2.174407]],[[-9.662743,3.030369,-4.237392,3.421639,-2.064717,-0.061802,6.043527],[5.628618,5.554161,-0.007803,-5.040032,6.221260,-2.928144,9.912259],[-9.086551,-8.164575,8.601366,-4.242658,-6.109700,-7.985781,5.824879],[4.280635,5.555750,0.700310,-1.747349,-2.622075,-7.826433,-6.763882],[-0.097925,-2.953435,3.619661,3.927309,3.602740,-5.684933,-2.516074],[-1.831536,-0.826541,-4.900203,-4.059776,-8.784025,5.291886,-4.895533],[-2.394942,-1.227546,-2.760945,2.659613,-7.020602,-5.138269,-7.477320],[4.057319,9.446381,9.754523,-4.533451,3.615600,1.211190,0.706978],[-3.028066,5.982785,-9.260513,-6.669365,-4.005140,2.415149,-3.709142],[-6.388169,-7.471448,2.656771,-5.797095,0.303316,-9.495389,4.000707],[5.901519,0.324164,-7.947610,-4.783319,-2.727525,1.429802,5.986726],[1.054385,-8.063799,-6.832725,-9.742409,6.862308,-9.760163,9.882883]],[[4.891811,8.161004,1.604795,4.654086,1.432810,1.977057,-0.472157],[-4.974531,2.120250,3.987806,-0.426668,-4.749006,-4.761592,7.589839],[5.681019,1.175903,8.268069,9.790674,0.915127,0.308913,-5.079172],[4.365475,7.303561,-2.190604,8.878570,7.861443,-5.269205,-6.830666],[6.584750,2.986180,-5.076804,0.913835,0.520664,2.494393,4.779820],[5.988937,7.606466,-7.651888,5.713721,1.471414,7.857118,-2.352626],[-6.209626,-5.780453,-6.285284,-8.426095,-0.392347,-9.526131,-9.708750],[5.693231,-0.034375,-4.859094,6.359701,8.012999,6.319386,1.696881],[5.521899,-0.126386,8.515726,9.397224,3.038886,-3.396263,0.411898],[7.396334,-7.209627,-5.731258,-9.146018,-9.131642,6.660014,-8.192974],[-5.641713,0.729727,7.392457,-1.229303,-1.087598,-1.254561,8.196629],[-5.692904,4.358010,5.579212,-6.654269,3.483276,-7.607484,-3.310918]],[[1.882289,-5.087595,-2.627980,7.755107,-2.724464,-8.456401,1.064570],[-6.569514,-4.963826,0.283444,-0.419840,7.428752,-3.642946,7.539434],[9.553243,9.101474,-5.648997,-4.367512,1.913936,-1.896986,0.692625],[7.765217,5.217505,-2.914427,-2.176367,-1.947272,-6.179514,5.982075],[-4.526149,0.924659,-2.055666,-5.881541,-9.105763,9.940162,-2.262180],[2.720682,1.515058,-7.356823,-9.994457,-3.730059,-5.270551,-7.385548],[-6.071634,-1.915509,-1.483031,-0.150330,-5.768381,-0.037133,-3.105948],[-0.858032,3.411284,-0.722452,-0.939230,-1.792473,3.743590,1.900483],[8.056845,-4.612865,6.323211,-3.646703,-6.604295,-0.635081,2.179114],[-7.456694,0.494317,-6.601099,-1.014647,6.212643,0.602061,-9.529185],[-4.175658,-1.549744,8.688474,0.955533,8.282132,-6.652140,8.370543],[-3.847898,8.606237,-9.841252,-4.295917,-5.212199,4.265138,3.199906]],[[7.510536,-1.609811,-3.613959,4.208333,9.001408,-6.677159,-0.180016],[3.800829,-1.263773,-2.089730,-0.154736,-5.042642,5.970655,9.187829],[-1.877225,3.864486,-5.051181,8.481872,-1.072823,-7.395590,8.960106],[1.841348,-3.171023,4.142373,-3.267025,-0.441600,-1.426485,8.821798],[6.396574,7.888547,-4.193981,6.836981,-9.145132,3.041044,0.537657],[-8.357982,-3.568380,-7.459185,-0.023266,5.110713,8.244021,0.739648],[-4.062507,2.940476,-6.055423,6.271055,3.996838,1.574102,0.301371],[1.113370,1.757705,-1.063852,3.082463,-7.220778,-1.529644,-5.303009],[7.335926,-5.757502,7.415459,-4.290591,-4.260662,-8.879479,-5.891781],[2.801038,-6.379989,7.204488,-9.819458,3.038682,-5.481517,-2.263851],[-9.764398,0.356665,-8.946520,2.371952,8.886928,6.454850,-8.814981],[-6.722501,-3.582485,-9.181545,-1.097430,-4.706285,1.419123,-7.955278]]], dtype = "float32")#candidate|14711|(14, 12, 7)|const|float32
const_14712 = relay.const([[[3.533106,1.542772,9.778852,-7.575510,7.284535,-7.259536,2.457778],[-2.420008,-4.871447,1.113037,5.546748,-8.675922,-3.783489,-8.248328],[7.327875,5.902553,5.907142,2.363812,4.689778,8.861080,-7.268977],[3.260019,-2.619708,8.882452,-0.725234,-0.061275,-7.295978,7.784675],[-5.809688,2.217968,4.560259,-4.087373,0.101676,-7.754334,3.333779],[-5.442941,7.393380,5.699379,5.686420,-1.163805,1.034257,-5.756833],[7.638142,9.246267,7.162441,-9.927999,0.140177,2.129034,-8.400473],[3.656846,4.662778,5.540355,-2.750643,4.326055,7.711749,9.097972],[-9.471073,-6.642450,-6.115673,6.439814,-3.061642,-7.487998,4.514914],[1.573100,0.849712,7.137828,-8.234581,-8.044584,-3.688307,-4.040191],[8.635662,-6.976744,7.915219,-2.559116,-6.318641,2.733433,2.261469],[4.409766,0.973673,-5.175779,5.020429,-7.252316,6.702771,-3.779373]],[[-2.110013,5.294259,5.781499,1.366618,5.032521,-1.036506,4.561837],[-5.626440,5.276547,5.807519,-9.062562,-1.286015,-4.149447,4.333002],[3.752293,9.616711,8.155724,2.769524,-6.668337,3.173017,-2.094696],[-4.076032,-5.222349,-1.833314,-2.561839,-5.806182,-6.409534,-1.612179],[2.429269,-0.472705,-9.155961,-0.503561,-6.925598,-6.952600,-5.574078],[-9.553810,1.603675,2.043827,-1.410023,3.022528,8.120426,3.646808],[-8.613196,-3.555582,-1.994999,-0.340506,-3.188280,-7.881097,8.138461],[-5.007197,-0.848495,-8.660896,6.578293,3.597790,-0.151079,-3.934496],[0.536883,1.584166,1.234897,1.128316,-0.235895,-6.702723,5.813041],[6.038439,3.791074,-7.034588,8.915950,5.378382,-6.080356,-8.007228],[-0.576591,7.564231,-0.583322,8.672210,-9.727307,6.282970,9.815007],[-6.615531,-3.357431,0.479798,1.741684,-7.060137,-7.314566,6.424010]],[[-5.883272,6.448606,-7.585954,-9.073325,3.101946,-6.285825,2.828335],[-6.057602,-9.864033,8.977208,1.078231,-5.216306,-2.150410,7.493737],[9.741839,-8.915846,-5.011255,-4.121228,-1.660217,0.976458,-6.689321],[2.539427,-6.634454,-6.327241,-8.868903,2.924455,-7.121293,-2.736271],[-5.906667,-3.894585,-1.576540,-3.518321,-9.763031,3.845090,1.035680],[7.856395,5.030955,7.407171,-8.903205,-8.273062,7.314912,-9.620855],[0.921407,9.831812,-7.733472,8.282312,-5.049740,1.803237,-9.371171],[0.415871,-9.783971,-9.556730,4.538899,8.922982,9.710060,4.289230],[0.888951,0.364791,-9.490618,3.624472,-8.012345,-7.370113,-5.345731],[5.038649,-7.474008,-4.307778,5.200738,-4.506213,6.094836,7.172364],[6.210416,7.362353,-3.195234,-1.827014,6.377283,-9.788791,-7.149342],[-5.693275,-6.674940,-0.796796,-8.783600,6.376574,0.816574,0.111263]],[[4.357294,9.473644,5.692963,-4.820617,1.153503,-0.690563,-6.075121],[-9.958504,5.028242,7.782564,2.940893,0.190836,-9.866524,2.433594],[-4.797956,-9.974814,1.323527,5.255738,7.563651,1.176507,-8.543375],[9.166202,-7.467690,1.760882,1.287620,7.358633,-9.947319,-5.412901],[-2.713803,-1.609510,-6.718619,-3.246768,1.787415,-3.908105,5.141531],[3.378042,-3.483069,-8.131065,2.990951,-9.674089,-8.140096,3.295599],[-6.344778,-2.336333,0.024230,-4.309112,5.490361,-3.125720,-3.113061],[3.500705,-7.137365,0.410607,-5.852027,9.264749,7.182342,-9.222100],[6.966122,2.581423,4.701353,-2.675144,-7.111046,6.539163,-1.616942],[-0.156870,-8.116767,-8.571942,5.665441,3.367376,-3.111165,2.727923],[6.223406,7.103016,8.746705,-8.310654,-8.094365,3.336001,8.577639],[9.941806,-4.713367,-3.722533,1.329082,4.311527,-6.602338,-3.609722]],[[0.643358,4.789510,8.482966,-0.107879,8.969748,-7.446490,2.767518],[-7.320141,-2.085060,-8.559190,-4.396667,8.733484,-7.709703,-9.302786],[-3.025327,4.511091,-5.352328,-2.813533,9.954215,-3.146667,7.618741],[6.481868,-1.294785,-7.533303,8.709735,-1.989779,8.786069,2.224788],[-8.402734,1.683726,2.825873,4.727178,9.017586,0.509833,-7.816710],[1.908930,-2.197665,-4.854625,-6.278109,2.854548,-4.520279,2.072925],[-6.906698,8.573967,-1.957138,8.274803,4.748005,9.833058,-1.980409],[2.883226,-7.514284,-4.194868,9.563435,-5.555570,8.983323,3.013384],[9.017821,-7.784861,-7.643014,-4.374116,-7.217437,-9.478057,-9.451095],[-8.806095,-6.933954,5.639036,-0.754647,-7.955100,6.609637,0.273319],[-3.277244,-8.332799,-3.590611,4.310062,-7.609140,2.265606,6.505754],[-9.765256,-4.038254,-8.525932,-3.485656,4.302945,-0.224066,1.539030]],[[-5.519828,-2.980557,8.581951,-7.336593,0.007657,-8.320692,-9.206841],[-8.846433,9.118368,3.618138,9.370252,2.164823,-4.127001,-9.048743],[-2.177996,-4.011532,1.531753,0.505688,5.463489,-2.313207,-3.486418],[-3.711009,-3.346526,-3.525044,6.483736,4.466062,-0.893153,-3.226528],[-4.884461,1.871220,-3.629564,5.649645,-8.343582,9.652203,9.118783],[7.247605,-5.676915,-5.604404,-2.260853,9.570905,-2.506341,0.410544],[4.113928,1.039152,-3.135055,-6.854133,-2.416490,-7.594456,-2.902301],[-9.786870,5.598656,0.111949,8.012991,3.596918,0.949532,4.747405],[1.461440,-1.880521,3.613350,-9.573484,-7.013745,-4.155834,5.423835],[0.186589,-0.939449,2.291683,6.045187,-0.209797,-6.308643,1.939378],[-0.446516,1.142917,4.599299,-4.646404,-9.360882,-6.748148,6.073560],[9.359945,-1.770359,-3.752344,0.290303,-5.543454,0.662716,7.433283]],[[-9.373537,0.491400,-1.945195,3.005597,-6.526339,-2.728361,-2.213951],[6.616459,7.442545,-9.678699,2.951581,4.987213,-6.786401,-4.566846],[-9.059813,9.979354,-6.117098,1.383604,-1.340111,-4.434952,-2.527104],[7.960215,1.902684,-8.615470,9.463893,-4.129012,6.156980,3.849818],[-9.515815,5.953402,-4.894867,6.193550,0.803121,6.943882,8.564543],[-7.641659,-8.238568,0.026157,-1.069951,-2.337597,-8.074543,8.544954],[-6.162441,-2.191011,-8.684224,6.904558,-9.783650,8.710854,1.175567],[7.939871,-3.733821,-1.022888,8.679852,-8.896357,0.769866,-4.961537],[-0.787148,-8.378734,-1.589461,7.220356,-0.020740,3.686845,7.345578],[2.368249,0.172138,-3.738497,-7.394422,-9.133785,-5.672373,-5.342691],[-9.325108,8.887802,-5.429122,2.537316,-6.961722,3.427414,-4.567513],[-6.974830,8.903497,-8.802275,-7.727613,-0.984912,-6.007571,2.965041]],[[1.467113,-7.266414,-1.826977,-1.750135,6.195798,8.588071,-2.992223],[0.236204,-1.855425,8.943323,1.172616,-2.754943,-3.600455,-8.873309],[-8.953934,8.138047,8.390896,1.630498,3.690838,-2.587142,6.583100],[7.741919,-7.484376,-8.359437,-5.378856,-8.412997,-4.388344,3.623777],[7.373077,9.765218,4.630072,-1.605888,-0.701740,-5.443251,2.662533],[2.333792,2.555048,8.118408,1.441647,-0.821437,8.602713,6.466581],[1.137753,-1.197243,-8.776926,-0.267847,-5.848273,7.498727,-4.365433],[-3.980135,-6.952557,8.778935,-4.002898,-4.484348,-9.453828,0.419863],[3.764728,7.532832,-2.040450,-6.965191,4.745050,-9.562040,2.867885],[2.953548,-6.254880,3.844095,4.833022,-9.033890,2.952119,4.057500],[0.750151,4.285062,5.036591,1.939271,-6.072169,-6.808527,8.787549],[6.996659,-6.518548,-4.527066,5.803515,-5.304684,-0.330911,-0.374727]],[[7.191392,-3.885353,9.690614,9.414819,-6.727030,-9.007193,-5.394580],[2.235936,3.118202,-3.261556,9.761011,-1.872425,4.486882,0.224508],[9.703789,4.014372,1.835107,5.942659,-5.056074,5.116176,-2.369051],[0.414462,-8.488515,-8.891912,-1.309367,-4.513846,3.356987,-1.195548],[7.682309,4.218127,0.224689,9.408582,-7.786188,8.606818,2.372476],[0.922117,-8.049151,9.926059,3.506256,7.335493,-6.123234,9.548111],[-2.651104,-6.180565,3.826803,0.493802,7.536402,7.261944,4.184194],[-0.629250,3.254944,-5.039213,-7.055764,4.769954,3.096334,0.039388],[-3.307746,-4.196965,-0.033001,-4.461412,-4.733356,5.078364,-6.424562],[4.789364,2.737092,-3.781498,1.645757,9.061498,-8.201409,-8.332473],[3.097189,-6.874080,-0.231362,-0.482013,7.198567,0.578240,-8.746007],[8.494604,1.925453,8.909471,-8.827348,-4.530409,-9.351560,-7.494435]],[[-0.885693,2.306264,-1.179188,2.675022,-7.594437,-6.898792,-5.885442],[4.488590,-8.739493,1.551392,5.620585,-4.641165,-8.439262,9.460140],[-2.071230,-5.010961,-2.766925,-7.009154,0.172855,-8.996915,-0.170013],[9.391751,-4.562176,7.470576,-3.466833,-3.097778,4.306271,6.705849],[3.141025,6.968770,-6.711387,-9.699348,3.413730,-1.594890,-8.766445],[-4.558427,6.203758,5.952364,-7.827047,-7.550504,2.879983,-3.837295],[7.966379,7.388190,-6.029639,6.717437,-0.210599,-3.791614,-5.387947],[-7.498917,8.055673,7.448152,-8.968295,-3.822330,-6.746677,2.519699],[7.311839,-7.825673,-8.846525,-0.729787,-3.601606,0.488232,6.252594],[-4.406713,-1.846238,4.586697,7.136458,-0.044534,9.079163,-7.109741],[5.191199,-7.701354,3.490127,-6.657438,-9.744905,0.124209,-9.364821],[1.310990,-3.161203,3.986327,-6.534564,-3.267259,-5.286553,9.346907]],[[9.413385,6.858483,-5.060536,9.778111,-0.725681,7.461036,-9.028002],[-6.027127,1.719930,4.422888,1.674744,4.645732,9.247950,-9.143391],[-8.376907,3.165878,3.167720,9.864843,-1.320590,-2.393687,-7.864605],[8.613423,-7.964691,9.993181,2.673390,9.126952,5.999036,-3.613974],[-2.579607,-6.649204,0.296826,-3.903713,-1.382424,-5.661504,-2.240498],[-4.502129,-2.865942,-1.429855,8.003207,-3.532908,-1.391335,1.230201],[-7.093010,-9.288960,-6.158560,-2.338673,-4.420157,4.626455,-1.763031],[-5.608627,-3.408380,8.703688,-7.300570,6.191217,2.983732,5.103850],[8.065094,4.201959,-1.505370,-7.009946,8.270426,-1.296881,8.210110],[-1.553581,6.208132,-3.895160,1.321909,-2.023003,5.874743,4.871227],[-9.971249,-2.741443,-9.639875,5.651205,7.749995,5.894100,-8.512033],[1.146345,3.703296,8.832900,-1.169272,-3.697819,1.778935,5.112491]],[[-0.502709,4.627856,7.597445,-7.749234,-2.389224,8.355599,8.486857],[-2.715782,-6.873969,1.238437,1.275616,8.093828,8.973314,-0.046812],[-2.398683,9.124019,-3.994862,5.442639,0.777877,1.377597,-3.367308],[3.427480,-5.385302,4.791618,0.488547,-5.544543,-7.770758,-5.138277],[-9.425109,-9.259810,2.642122,1.072781,6.246984,9.748159,0.756784],[-4.542531,1.648769,4.216965,5.143065,3.838251,-7.746593,8.984672],[7.255667,-7.351490,-3.305229,-4.764936,-6.555396,-8.412478,2.956739],[-4.718304,-0.586558,-2.507856,3.842549,7.822017,-9.426035,6.493028],[8.548354,1.878188,7.000561,-9.783706,6.326249,1.385038,-9.708988],[8.535028,0.943136,-5.250194,-4.223697,-0.992883,7.907770,-1.313229],[-4.769270,-9.351604,-8.621107,-7.072430,8.913862,-5.059243,1.301871],[-7.685951,2.004674,5.054728,-2.402429,-4.843179,-7.998835,-1.008415]],[[2.925164,-4.718325,-9.289637,3.238540,-0.644760,-2.066690,-5.689768],[-9.558042,-7.116950,8.912052,-5.557497,3.786281,1.140344,0.264931],[-6.802257,9.189872,-9.330714,2.587912,-8.048689,-9.091284,-1.953209],[-8.784118,4.806894,-6.434732,7.456273,0.987288,3.705987,-4.509773],[-1.120004,-6.010877,5.591108,-3.046557,9.566237,0.684253,-8.513154],[9.718659,-5.472716,3.464781,-9.852469,-7.272839,-5.663035,-6.212144],[-2.411724,-0.745377,-6.163126,3.989970,-0.015273,-8.026193,6.779291],[4.281114,7.058882,-2.770281,-9.711801,3.004363,4.989491,-8.199606],[6.066000,0.125876,-5.886817,-9.443402,4.676569,-5.001978,-1.136941],[9.981897,-1.311323,9.289852,5.260653,-4.496965,-9.787774,9.185665],[8.145233,7.811283,-1.658768,-7.019981,-5.946142,6.292521,-1.537274],[9.132311,-8.104483,-2.534902,5.052095,-0.976144,9.015767,-7.579972]],[[-2.099441,4.477259,5.971449,-6.365739,-3.475379,-6.599364,-7.025106],[-9.102788,-2.584917,4.439954,-3.016855,1.019694,0.648183,1.837287],[-3.362827,-2.481788,9.368046,-4.402647,-4.344116,-2.926487,3.447281],[4.080167,-0.984108,-5.082228,1.858263,-4.690155,1.873102,0.927085],[5.310390,7.867920,-1.649863,6.684049,-9.085191,0.053636,-2.496661],[9.882638,-5.309784,4.583996,-3.979548,6.159178,2.377570,8.242451],[-8.253236,-3.634396,0.667956,3.153125,6.565029,4.397513,0.807366],[4.348060,-8.685101,6.206846,0.041587,-9.025574,5.174235,-8.102152],[5.581101,3.669964,-6.298163,1.485763,-9.838613,-2.434311,6.901084],[8.917091,-7.157501,8.382010,9.950978,5.621442,3.478600,-9.044013],[-8.328785,-3.342188,-9.188904,9.110613,1.384690,5.462235,2.642008],[6.544703,5.900224,5.485945,0.566670,4.894436,-4.084304,-6.697498]]], dtype = "float32")#candidate|14712|(14, 12, 7)|const|float32
bop_14713 = relay.mod(const_14711.astype('float32'), relay.reshape(const_14712.astype('float32'), relay.shape_of(const_14711))) # shape=(14, 12, 7)
output = relay.Tuple([bop_14713,])
output2 = relay.Tuple([bop_14713,])
func_14722 = relay.Function([], output)
mod['func_14722'] = func_14722
mod = relay.transform.InferType()(mod)
mutated_mod['func_14722'] = func_14722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14722_call = mutated_mod.get_global_var('func_14722')
call_14723 = func_14722_call()
output = call_14723
func_14724 = relay.Function([], output)
mutated_mod['func_14724'] = func_14724
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9715_call = mod.get_global_var('func_9715')
func_9716_call = mutated_mod.get_global_var('func_9716')
call_14734 = func_9715_call()
call_14735 = func_9715_call()
output = relay.Tuple([call_14734,])
output2 = relay.Tuple([call_14735,])
func_14751 = relay.Function([], output)
mod['func_14751'] = func_14751
mod = relay.transform.InferType()(mod)
output = func_14751()
func_14752 = relay.Function([], output)
mutated_mod['func_14752'] = func_14752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5695_call = mod.get_global_var('func_5695')
func_5697_call = mutated_mod.get_global_var('func_5697')
call_14799 = func_5695_call()
call_14800 = func_5695_call()
output = relay.Tuple([call_14799,])
output2 = relay.Tuple([call_14800,])
func_14802 = relay.Function([], output)
mod['func_14802'] = func_14802
mod = relay.transform.InferType()(mod)
mutated_mod['func_14802'] = func_14802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14802_call = mutated_mod.get_global_var('func_14802')
call_14803 = func_14802_call()
output = call_14803
func_14804 = relay.Function([], output)
mutated_mod['func_14804'] = func_14804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12752_call = mod.get_global_var('func_12752')
func_12754_call = mutated_mod.get_global_var('func_12754')
call_14810 = func_12752_call()
call_14811 = func_12752_call()
func_12091_call = mod.get_global_var('func_12091')
func_12092_call = mutated_mod.get_global_var('func_12092')
call_14829 = relay.TupleGetItem(func_12091_call(), 1)
call_14830 = relay.TupleGetItem(func_12092_call(), 1)
output = relay.Tuple([call_14810,call_14829,])
output2 = relay.Tuple([call_14811,call_14830,])
func_14831 = relay.Function([], output)
mod['func_14831'] = func_14831
mod = relay.transform.InferType()(mod)
output = func_14831()
func_14832 = relay.Function([], output)
mutated_mod['func_14832'] = func_14832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9492_call = mod.get_global_var('func_9492')
func_9494_call = mutated_mod.get_global_var('func_9494')
call_14864 = func_9492_call()
call_14865 = func_9492_call()
var_14871 = relay.var("var_14871", dtype = "float32", shape = (7, 2, 5))#candidate|14871|(7, 2, 5)|var|float32
bop_14872 = relay.add(call_14864.astype('uint64'), relay.reshape(var_14871.astype('uint64'), relay.shape_of(call_14864))) # shape=(7, 2, 5)
bop_14875 = relay.add(call_14865.astype('uint64'), relay.reshape(var_14871.astype('uint64'), relay.shape_of(call_14865))) # shape=(7, 2, 5)
uop_14895 = relay.log10(bop_14872.astype('float64')) # shape=(7, 2, 5)
uop_14897 = relay.log10(bop_14875.astype('float64')) # shape=(7, 2, 5)
output = uop_14895
output2 = uop_14897
func_14903 = relay.Function([var_14871,], output)
mod['func_14903'] = func_14903
mod = relay.transform.InferType()(mod)
mutated_mod['func_14903'] = func_14903
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14904 = relay.var("var_14904", dtype = "float32", shape = (7, 2, 5))#candidate|14904|(7, 2, 5)|var|float32
func_14903_call = mutated_mod.get_global_var('func_14903')
call_14905 = func_14903_call(var_14904)
output = call_14905
func_14906 = relay.Function([var_14904], output)
mutated_mod['func_14906'] = func_14906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5223_call = mod.get_global_var('func_5223')
func_5225_call = mutated_mod.get_global_var('func_5225')
call_14926 = relay.TupleGetItem(func_5223_call(), 0)
call_14927 = relay.TupleGetItem(func_5225_call(), 0)
func_5807_call = mod.get_global_var('func_5807')
func_5809_call = mutated_mod.get_global_var('func_5809')
call_14958 = func_5807_call()
call_14959 = func_5807_call()
output = relay.Tuple([call_14926,call_14958,])
output2 = relay.Tuple([call_14927,call_14959,])
func_14965 = relay.Function([], output)
mod['func_14965'] = func_14965
mod = relay.transform.InferType()(mod)
mutated_mod['func_14965'] = func_14965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14965_call = mutated_mod.get_global_var('func_14965')
call_14966 = func_14965_call()
output = call_14966
func_14967 = relay.Function([], output)
mutated_mod['func_14967'] = func_14967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5939_call = mod.get_global_var('func_5939')
func_5941_call = mutated_mod.get_global_var('func_5941')
call_15064 = func_5939_call()
call_15065 = func_5939_call()
func_7516_call = mod.get_global_var('func_7516')
func_7517_call = mutated_mod.get_global_var('func_7517')
call_15072 = relay.TupleGetItem(func_7516_call(), 0)
call_15073 = relay.TupleGetItem(func_7517_call(), 0)
output = relay.Tuple([call_15064,call_15072,])
output2 = relay.Tuple([call_15065,call_15073,])
func_15092 = relay.Function([], output)
mod['func_15092'] = func_15092
mod = relay.transform.InferType()(mod)
output = func_15092()
func_15093 = relay.Function([], output)
mutated_mod['func_15093'] = func_15093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14483_call = mod.get_global_var('func_14483')
func_14484_call = mutated_mod.get_global_var('func_14484')
call_15143 = relay.TupleGetItem(func_14483_call(), 0)
call_15144 = relay.TupleGetItem(func_14484_call(), 0)
output = relay.Tuple([call_15143,])
output2 = relay.Tuple([call_15144,])
func_15163 = relay.Function([], output)
mod['func_15163'] = func_15163
mod = relay.transform.InferType()(mod)
mutated_mod['func_15163'] = func_15163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15163_call = mutated_mod.get_global_var('func_15163')
call_15164 = func_15163_call()
output = call_15164
func_15165 = relay.Function([], output)
mutated_mod['func_15165'] = func_15165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9336_call = mod.get_global_var('func_9336')
func_9338_call = mutated_mod.get_global_var('func_9338')
call_15220 = func_9336_call()
call_15221 = func_9336_call()
func_910_call = mod.get_global_var('func_910')
func_914_call = mutated_mod.get_global_var('func_914')
var_15252 = relay.var("var_15252", dtype = "float64", shape = (200, 1))#candidate|15252|(200, 1)|var|float64
call_15251 = relay.TupleGetItem(func_910_call(relay.reshape(var_15252.astype('float64'), [2, 10, 10]), relay.reshape(var_15252.astype('float64'), [2, 10, 10]), ), 0)
call_15253 = relay.TupleGetItem(func_914_call(relay.reshape(var_15252.astype('float64'), [2, 10, 10]), relay.reshape(var_15252.astype('float64'), [2, 10, 10]), ), 0)
func_7277_call = mod.get_global_var('func_7277')
func_7279_call = mutated_mod.get_global_var('func_7279')
call_15256 = relay.TupleGetItem(func_7277_call(), 0)
call_15257 = relay.TupleGetItem(func_7279_call(), 0)
func_6979_call = mod.get_global_var('func_6979')
func_6980_call = mutated_mod.get_global_var('func_6980')
call_15271 = relay.TupleGetItem(func_6979_call(), 1)
call_15272 = relay.TupleGetItem(func_6980_call(), 1)
output = relay.Tuple([call_15220,call_15251,var_15252,call_15256,call_15271,])
output2 = relay.Tuple([call_15221,call_15253,var_15252,call_15257,call_15272,])
func_15310 = relay.Function([var_15252,], output)
mod['func_15310'] = func_15310
mod = relay.transform.InferType()(mod)
mutated_mod['func_15310'] = func_15310
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15311 = relay.var("var_15311", dtype = "float64", shape = (200, 1))#candidate|15311|(200, 1)|var|float64
func_15310_call = mutated_mod.get_global_var('func_15310')
call_15312 = func_15310_call(var_15311)
output = call_15312
func_15313 = relay.Function([var_15311], output)
mutated_mod['func_15313'] = func_15313
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5345_call = mod.get_global_var('func_5345')
func_5346_call = mutated_mod.get_global_var('func_5346')
call_15328 = relay.TupleGetItem(func_5345_call(), 0)
call_15329 = relay.TupleGetItem(func_5346_call(), 0)
output = relay.Tuple([call_15328,])
output2 = relay.Tuple([call_15329,])
func_15341 = relay.Function([], output)
mod['func_15341'] = func_15341
mod = relay.transform.InferType()(mod)
mutated_mod['func_15341'] = func_15341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15341_call = mutated_mod.get_global_var('func_15341')
call_15342 = func_15341_call()
output = call_15342
func_15343 = relay.Function([], output)
mutated_mod['func_15343'] = func_15343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9273_call = mod.get_global_var('func_9273')
func_9274_call = mutated_mod.get_global_var('func_9274')
call_15388 = relay.TupleGetItem(func_9273_call(), 0)
call_15389 = relay.TupleGetItem(func_9274_call(), 0)
func_4838_call = mod.get_global_var('func_4838')
func_4840_call = mutated_mod.get_global_var('func_4840')
var_15401 = relay.var("var_15401", dtype = "float32", shape = (3, 42))#candidate|15401|(3, 42)|var|float32
call_15400 = relay.TupleGetItem(func_4838_call(relay.reshape(var_15401.astype('float32'), [126,])), 0)
call_15402 = relay.TupleGetItem(func_4840_call(relay.reshape(var_15401.astype('float32'), [126,])), 0)
func_8612_call = mod.get_global_var('func_8612')
func_8616_call = mutated_mod.get_global_var('func_8616')
const_15412 = relay.const([-5.162264,-8.685295,1.318652,-9.450149,-1.154757,-1.493271,-4.951795,-3.457334,-4.456862,6.697459,-9.873029,3.905276,7.035221,-9.730135,7.472917,4.983976,-5.505971,-6.228772,-5.657327,2.022654,-7.011103,2.243538,-1.544373,-5.963192,-5.710111,1.660048,-8.341969,-5.729579,-8.146722,-7.328649,-7.993157,7.516024,7.646938,-0.850315,-0.528973,2.617215,-5.886681,9.631799,-5.147789,3.897518,5.760146,2.590041,-0.623871,6.922258,1.306672,-0.512699,-6.771759,-6.785116,5.862176,7.323357,4.803637,-8.999043,2.119216,-8.870380,-3.869933,1.878777,2.566580,9.552466,-9.363712,-9.997291,8.380612,-0.042735,0.593885,1.893986,7.554321,-0.772445,6.206615,-2.700390,9.018145,8.725532,7.463923,1.439533], dtype = "float64")#candidate|15412|(72,)|const|float64
const_15413 = relay.const([2,3,-7,1,1,-4,-9,5,10,-6,-1,-1,10,-4,-8,7,3,9,6,1,-5,-6,-4,8,4,6,-2,10,9,-10,-2,-8,-7,-2,-8,-2,-8,7,-9,5,-10,-9,-9,4,-10,6,3,5,-4,3,-2,3,3,-1,7,-6,-6,-9,3,-3,-10,-4,-7,-3,8,1,2,9,7,8,3,-1,8,-3,5,-3,-7,10,-8,4,-2,7,10,9,-5,1,10,8,-4,-8,-9,6,10,9,-2,3,10,7,-5,9,-5,7,-2,3,5,7,-4,9,10,9,1,-7,3,2,10,7,10,1,10,10,-7,9,-9,-5,-8,-2,-8,1,2,-1,-3,-10,-4,-6,4,2,-4,-3,1,3,-2,-10,5,4,-5,4,5,2,4,4,8,1,6,5,4,9,-7,8,10,-3,-9,4,10,3,-8,2,-2,-7,1,-8,-4,-10,-3,4,4,-10,-4,-9,4,6,9,-7,-5,1,-8,8,3,-2,-8,-2,4,7,8,-2,-8,-4,8,-9,-8,6,9,-8,4,1,-6,6,6,-10,9,-9,-2,-3,-6,3,5,10,7,-6,-7,5,-9,3,-6,2,-7,-2,3,9,-2,-5,-6,-8,-4,4,-3,-3,1,8,1,5,-10,-6,4,6,8,2,-8,-6,7,2,-8,2,4,-9,1,-4,-2,-6,4,2,-3,7,-7,2,1,-3,10,2,-9,-1,-4,-3,-3,-3,-1,10,-1,3,-8,-1,-10,1,4,-6,-4,-5,-1,-5,7,1,4,10,-10,3,-10,8,1,-4,3,-7,-8,-7,1,3,-1,4,8,3,6,6,2,-10,3,7,-5,-5,7,1,-4,-3,-9,-2,-2,-2,3,-6,2,-8,-9,5,1,6,9,-7,-4,-10,9,9,-7,10,9,-4,2,-9,9,7,-1,-10,-2,7,-7,-8,-7,8,8,-3,-3,-9,1,10,-2,-1,-1,7,-8,-9,9,3,-4,1,10,10,-3,2,7,-5,8,3,-9,-3,5,5,-9,2,-1,5,9,7,-4,-7,1,-1,-9,8,-7,8,3,5,-4,-5,-10,-8,-6,8,-6,-3,8,-7,10,-9,-6,-8,2,9,10,3,-6,6,10,4,-2,4,-2,-9,8,-1,6,-1,5,-6,-6,5,-4,4,7,-9,-4,9,5,10,7,-8,-3,3,9,-4,-10,6,10,-7,7,-7,10,9,-5,1,-10,-7,7,10,-1,2,-3,-5,-8,3,-8,-10,-8,8,-8,7,9,3,-6,-2,7,-8,2,-5,-6,10,1,-4,9,-2,2,-6,-3,-7,-2,-4,4,-3,-5,-9,-9,5,-8,-6,-3,-3,8,-6,-8,10,3,-3,7,-5,4,-3,4,-2,-9,9,-7,-6,4,7,-6,-4,-2,8,-2,-2,-9,-9,3,3,-10,-3,-5,-3,1,-10,9,-6,2,-10,6,-1,9,8,-3,-5,5,1,6,-8,-6,-4,6,-5,5,-3,1,8,7,-3,8,3,-7,3,10,2,4,10,7,8,-5,5,-8,6,-10,6,-9,3,-5,1,10,9,1,-3,7,2,-4,-5,-1,-8,4,-9,2,8,8,1,3,3,-1,2,-10,9,-1,-6,7,-3,7,3,4,7,3,2,-1,-9,3,-10,6,-7,-6,-1,-9,4,-8,5,8,-4,1,-6,2,5,-7,-6,-6,1,-10,-5,-9,-6,5,7,-3,-6,-8,7,8,-3,8,-7,6,8,-2,-6,-1,-6,-4,-2,5,-3,10,2,3,2,-9,-8,9,-3,-9,2,1,-8,10,-2,-8,9,-7,8,8,-3,-3,4,-9,2,7,-7,3,-3,-7,-9,4,-5,-9,-10,4,-6,4,-8,-6,-10,6,1,-5,4,3,-5,1,5,4,9,-9,-5,-4,6,5,2,3,3,-10,-8,-8,8,-4,9,8,-7,2,10,7,5,1,-3,3,-10,3,-3,-2,10,6,5,-9,3,-4,-7,-8,-1,2,-3,2,-7,3,7,1,-1,-9,2,-7,-9,-7,-2,-3,-4,-8,9,2,6,5,1,1,4,-8,-7,-1,-8,5,3,-2,2,-6,4,8,-1,5,1,-6,5,-3,-9,-9,3,6,1,-3,-1,-7,-4,5,9,9,-8,-7,9,5,6,-6,9,3,1,4,-2,7,5,-3,-3,-4,-9,4,-3,-5,-5,8,-4,-4,6,9,9,5,-9,6,-3,5,-3,10,-9,7,-6,8,3,-5,1,8,-9,4,3,1,2,8,4,3,2,7,-2,-8,-6,7,-8,-7,-8,-4,-1,-9,-1,-10,4,8,3,6,2,-4,8,8,-6,2,6,-7,2,-9,2,10,3,3,-5,3,2,8,9,-5,-10,1,6,-10,1,-3,-1,8,-3,1,-10,7,-4,-2,-10,-9,6,4,-7,10,8,-10,8,-4,-1,-1,1,-4,5,-9,-5,-7,8,4,-8,3,10,4,5,9,2,8,-9,10,10,-1,10,7,9,-3,-6,4,4,-3,5,7,-1,-3,-9,4,-2,6,3,10,-7,-9,-3,-10,-1,6,-7,3,9,-10,-9,-10,1,5,-3,4,-7,-4,5,7,-9,2,-7,-3,3,5,-10,-4,-4,3,-1,-7,1,1,5,2,3,1,-8,-6,-10,2,-7,10,-5,-9,1,7,9,-8,7,10,5,-10,6,6,9,5,-6,9,10,-10,-6,-3,-6,-1,4,-5,-3,-1,-2,-4,-7,-9,5,-4,8,6,-10,8,3,-3,1,5,4,4,5,9,10,-4,-5,-10,2,-6,-6,-10,-6,-5,2,2,5,2,-5,-1,8,-9,-4,6,6,10,-6,10,-5,10,4,1,-1,1,-7,-2,10,8,2,-1,5,8,-4,-5,3,6,1,-7,4,8,-2,6,4,9,-7,-2,-4,4,-9,8,-6,7,6,10,4,1,8,10,-1,-8,9,-1,-8,-4,-5,9,9,-9,-2,2,6,-3,-1,8,2,-10,-4,8,5,-1,2,-10,-5,-5,7,-4,3,7,8,5,9,-5,-6,7,2,-10,7,7,-10,-1,-10,-9,-10,-8,-4,-10,-10,-8,-5,10,2,-4,-1,-10,-1,-9,4,5,-6,2,-8,3,-9,-8,7,-4,7,5,-6,10,-6,10,7,-3,10,3,2,-10,10,-9,-6,-3,10,-1,-4,6,10,-1,-5,1,4,5,-3,-8,3,-9,10,-1,1,9,-3,-7,-4,3,5,-3,10,-4,3,8,-9,4,-9,2,-7,7,-7,-4,-3,8,-10,8,9,5,-5,-1,-9,6,9,10,-8,-7,-1,3,7,3,-2,-1,2,6,-10,4,1,-7,-9,-8,4,-3,6,9,9,5,1,-4,-2,2,9,-1,-7,3,-7,-4,-8,-6,-3,2,-4,-3,10,2,2,-4,-10,-3,3,-5,-9,-1,-6,-3,-9,10,1,2,3,-3,-6,5,-2,-4,-4,-5,-8,2,-1,-2,10,-8,7,2,4,6,6,7,-2,3,10,1,-6,1,-9,-10,6,2,7,-3,3,2,-3,-7,2,2,-2,9,7,-5,-2,7,-4,1,-7,4,-8,-9,-7,-5,-8,10,-10,-8,-8,5,-10,10,-3,9,9,-10,-2,-7,7,8,9,-7,-7,-7,-8,7,-7,3,-9,-10,8,3,-2,8,2,-7,4,-1,-9,-5,3,8,-10,9,-5,-8,-10,-2,-1,4,-8,6,6,-2,8,-3,-1,8,-2,-3,-6,10,1,-10,2,-10,6,-2,-5,-7,-6,-3,-1,-10,-8,2,1,-3,1,9,-7,4,4,6,-2,2,3,-7,-6,9,-10,-1,-2,7,6,-7,-2,-8,10,-8,7,2,-5,6,6,7,-8,-8,1,-4,-9,3,5,-2,5,7,9,-2,8,6,-3,9,1,10,3,2,6,-5,-7,3,-6,6,10,8,5,-2,-8,10,10,-3,5,-5,9,1,9,-9,-6,10,2,4,3,6,8,-1,5,1,9,2,-10,-5,-8,-3,1,10,3,-9,-1,10,-10,-8,-6,4,9,-3,-8,9,5,10,-7,-7,4,1,-2,5,-3,-6,5,4,9,-2,-6,-3,-3,4,5,2,-1,5,3,5,4,-5,-5,-3,-8,1,6,-4,-1,2,-4,-5,7,-8,1,-8,-9,4,-4,10,3,-6,9,1,10,4,-8,-9,-1,5,2,-9,-6,7,-1,2,8,5,7,7,-9,-3,2,-2,-1,-6,-2,-6,-9,10,9,8,-9,-7,8,6,-7,-6,3,3,-7,-8,8,-7,6,1,-7,-7,1,-3,-9,8,-7,6,-2,-3,10,6,-5,6,-10,1,3,6,-1,3,-9,8,7,6,-3,-6,2,2,7,-1,5,6,9,2,-2,-3,-7,-7,-5,2,5,2,4,-7,1,9,1,4,9,1,10,-4,-5,1,-7,-7,-5,-2,-10,-1,10,-7,-7,-2,-4,10,6,-2,9,10,-8,-8,3,-3,10,6,-2,-10,3,-5,-4,-2,3,3,9,5,10,2,7,10,7,-7,8,-10,-9,9,-4,-6,-5,6,-2,-3,8,10,1,3,6,1,-9,-5,7,-4,5,7,-8,-5,-6,7,-4,-9,6,6,-4,-4,-7,-3,-4,-7,-6,-8,9,-9,2,9,2,4,2,10,5,8,4,10,8,-5,-4,-3,6,6,-9,-7,-4,10,9,9,3,-9,1,-5,7,-5,4,-1,-9,2,3,10,-8,-3,-10,2,2,-10,-1,1,-6,-8,-6,1,-8,-5,2,-10,6,9,6,7,5,2,-4,-5,-1,9,5,-5,4,-6,5,-9,9,-7,1,4,3,1,1,8,-2,1,8,10,6,-2,-4,-2,-9,10,4,6,-2,-7,-7,-6,1,-4,-3,-4,-2,10,5,9,-2,6,4,5,10,-8,-4,-4,4,-5,4,-6,4,-2,-9,-5,-1,6,2,1,1,7,-6,2,10,-4,5,-1,-5,7,4,-4,-4,10,2,-8,-1,-10,-9,-4,10,-3,10,-3,7,-1,-6,7,3,-8,9,10,2,-8,4,9,-1,-8,-4,-8,-3,-1,-1,-8,6,-1,-1,-8,3,-5,-7,1,-7,-1,-10,-4,-7,1,-5,-4,7,7,-10,-3,8,-10,-4,-5,7,-4,4,-1,4,8,-3,10,2,9,2,-3,-10,7,1,7,-7,-7,8,1,10,-1,4,2,-9,-5,3,-3,-10,-8,-4,1,7,-2,5,-7,3,-7,-9,10,-2,-1,5,-9,-6,-8,-4,-2,8,-6,-7,8,-2,4,4,9,3,10,-4,2,5,-10,2,10,6,-3,-8,3,-5,-1,-3,4,2,3,-2,8,9,-8,2,1,3,-2,-4,-3,2,-8,6,-10,-8,6,9,9,2,9,5,-3,-3,-9,10,5,-8,6,7,-2,-2,-4,2,9,1,9,5,4,7,-6,-7,-8,6,-9,-1,-7,-9,3,4,-7,-9,1,-10,-3,-8,5,-10,8,-6,-10,-8,-1,-7,10,8,8,-6,3,-2,3,5,-3,1,-2,10,8,-8,7,-5,9,-4,3,4,6,-10,5,-6,-2,-2,6,4,-10,-4,10,-3,5,5,-7,-1,4,1,9,-10,6,5,3,-5,4,9,-9,10,-8,-1,6,8,-5,1,-6,-5,2,4,9,-8,1,6,8,5,3,-4,7,-8,1,-4,-10,-1,1,8,9,3,-3,-9,5,10,-7,6,4,-6,-3,6,-1,8,4,-2,-1,-2,-3,5,4,-7,-8,7,-5,1,-3,-3,-3,6,4,10,-4,10,-3,7,-10,8,-5,4,-8,-10,-1,7,4,1,3,5,-2,-5,2,2,-6,4,7,-5,-2,-8,-10,6,8,5,-7,-9,7,-3,7,3,-6,-9,4,8,1,-8,10,-6,-1,2,-3,-6,6,-9,5,-8,-8,5,-1,7,-8,-4,9,1,-2,6,5,-6,-3,5,9,-2,10,-9,10,-4,1,1,9,9,-4,-5,-9,1,7,2,9,3,1,4,-9,10,-8,1,-2,7,5,6,-4,-8,4,7,5,-5,-5,8,7,6,-10,3,7,-7,-1,-10,1,-5,9,-8,-1,3,-4,-2,10,8,-4,9,8,-6,10,-5], dtype = "uint64")#candidate|15413|(2288,)|const|uint64
call_15411 = relay.TupleGetItem(func_8612_call(relay.reshape(const_15412.astype('float64'), [72, 1]), relay.reshape(const_15413.astype('uint64'), [2288,]), ), 1)
call_15414 = relay.TupleGetItem(func_8616_call(relay.reshape(const_15412.astype('float64'), [72, 1]), relay.reshape(const_15413.astype('uint64'), [2288,]), ), 1)
func_14026_call = mod.get_global_var('func_14026')
func_14030_call = mutated_mod.get_global_var('func_14030')
var_15416 = relay.var("var_15416", dtype = "uint8", shape = (351,))#candidate|15416|(351,)|var|uint8
call_15415 = relay.TupleGetItem(func_14026_call(relay.reshape(var_15416.astype('uint8'), [13, 3, 9]), relay.reshape(var_15416.astype('uint8'), [13, 3, 9]), ), 0)
call_15417 = relay.TupleGetItem(func_14030_call(relay.reshape(var_15416.astype('uint8'), [13, 3, 9]), relay.reshape(var_15416.astype('uint8'), [13, 3, 9]), ), 0)
bop_15420 = relay.greater_equal(var_15401.astype('bool'), call_15400.astype('bool')) # shape=(3, 42)
bop_15423 = relay.greater_equal(var_15401.astype('bool'), call_15402.astype('bool')) # shape=(3, 42)
output = relay.Tuple([call_15388,call_15411,const_15412,const_15413,call_15415,var_15416,bop_15420,])
output2 = relay.Tuple([call_15389,call_15414,const_15412,const_15413,call_15417,var_15416,bop_15423,])
func_15430 = relay.Function([var_15401,var_15416,], output)
mod['func_15430'] = func_15430
mod = relay.transform.InferType()(mod)
var_15431 = relay.var("var_15431", dtype = "float32", shape = (3, 42))#candidate|15431|(3, 42)|var|float32
var_15432 = relay.var("var_15432", dtype = "uint8", shape = (351,))#candidate|15432|(351,)|var|uint8
output = func_15430(var_15431,var_15432,)
func_15433 = relay.Function([var_15431,var_15432,], output)
mutated_mod['func_15433'] = func_15433
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5223_call = mod.get_global_var('func_5223')
func_5225_call = mutated_mod.get_global_var('func_5225')
call_15438 = relay.TupleGetItem(func_5223_call(), 0)
call_15439 = relay.TupleGetItem(func_5225_call(), 0)
func_6125_call = mod.get_global_var('func_6125')
func_6126_call = mutated_mod.get_global_var('func_6126')
call_15445 = relay.TupleGetItem(func_6125_call(), 2)
call_15446 = relay.TupleGetItem(func_6126_call(), 2)
output = relay.Tuple([call_15438,call_15445,])
output2 = relay.Tuple([call_15439,call_15446,])
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
func_4758_call = mod.get_global_var('func_4758')
func_4759_call = mutated_mod.get_global_var('func_4759')
call_15488 = func_4758_call()
call_15489 = func_4758_call()
func_11099_call = mod.get_global_var('func_11099')
func_11101_call = mutated_mod.get_global_var('func_11101')
call_15512 = relay.TupleGetItem(func_11099_call(), 2)
call_15513 = relay.TupleGetItem(func_11101_call(), 2)
func_7277_call = mod.get_global_var('func_7277')
func_7279_call = mutated_mod.get_global_var('func_7279')
call_15519 = relay.TupleGetItem(func_7277_call(), 0)
call_15520 = relay.TupleGetItem(func_7279_call(), 0)
func_14252_call = mod.get_global_var('func_14252')
func_14254_call = mutated_mod.get_global_var('func_14254')
call_15524 = relay.TupleGetItem(func_14252_call(), 1)
call_15525 = relay.TupleGetItem(func_14254_call(), 1)
output = relay.Tuple([call_15488,call_15512,call_15519,call_15524,])
output2 = relay.Tuple([call_15489,call_15513,call_15520,call_15525,])
func_15529 = relay.Function([], output)
mod['func_15529'] = func_15529
mod = relay.transform.InferType()(mod)
output = func_15529()
func_15530 = relay.Function([], output)
mutated_mod['func_15530'] = func_15530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14802_call = mod.get_global_var('func_14802')
func_14804_call = mutated_mod.get_global_var('func_14804')
call_15535 = relay.TupleGetItem(func_14802_call(), 0)
call_15536 = relay.TupleGetItem(func_14804_call(), 0)
func_7553_call = mod.get_global_var('func_7553')
func_7555_call = mutated_mod.get_global_var('func_7555')
var_15580 = relay.var("var_15580", dtype = "float64", shape = (60,))#candidate|15580|(60,)|var|float64
call_15579 = relay.TupleGetItem(func_7553_call(relay.reshape(var_15580.astype('float64'), [60,])), 4)
call_15581 = relay.TupleGetItem(func_7555_call(relay.reshape(var_15580.astype('float64'), [60,])), 4)
func_9786_call = mod.get_global_var('func_9786')
func_9788_call = mutated_mod.get_global_var('func_9788')
call_15593 = func_9786_call()
call_15594 = func_9786_call()
output = relay.Tuple([call_15535,call_15579,var_15580,call_15593,])
output2 = relay.Tuple([call_15536,call_15581,var_15580,call_15594,])
func_15602 = relay.Function([var_15580,], output)
mod['func_15602'] = func_15602
mod = relay.transform.InferType()(mod)
mutated_mod['func_15602'] = func_15602
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15603 = relay.var("var_15603", dtype = "float64", shape = (60,))#candidate|15603|(60,)|var|float64
func_15602_call = mutated_mod.get_global_var('func_15602')
call_15604 = func_15602_call(var_15603)
output = call_15604
func_15605 = relay.Function([var_15603], output)
mutated_mod['func_15605'] = func_15605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7659_call = mod.get_global_var('func_7659')
func_7661_call = mutated_mod.get_global_var('func_7661')
call_15616 = relay.TupleGetItem(func_7659_call(), 1)
call_15617 = relay.TupleGetItem(func_7661_call(), 1)
output = call_15616
output2 = call_15617
func_15634 = relay.Function([], output)
mod['func_15634'] = func_15634
mod = relay.transform.InferType()(mod)
mutated_mod['func_15634'] = func_15634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15634_call = mutated_mod.get_global_var('func_15634')
call_15635 = func_15634_call()
output = call_15635
func_15636 = relay.Function([], output)
mutated_mod['func_15636'] = func_15636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12233_call = mod.get_global_var('func_12233')
func_12235_call = mutated_mod.get_global_var('func_12235')
call_15637 = func_12233_call()
call_15638 = func_12233_call()
func_3104_call = mod.get_global_var('func_3104')
func_3108_call = mutated_mod.get_global_var('func_3108')
var_15657 = relay.var("var_15657", dtype = "int16", shape = (224,))#candidate|15657|(224,)|var|int16
const_15658 = relay.const([6,7,5,-8,-2,4,5,8,4,8,9,-7,-5,-5,9,-8,5,-8,-7,-5,-9,2,8,3,6,-4,-3,9,3,1,-1,-5,-4,-5,9,9,-10,4,-3,-10,10,3,6,3,6,-1,5,-1,1,2,-7,-10,6,-7,-10,-9,2,6,-5,-7,-5,8,-4,-10,9,7,-5,-5,10,1,10,2,1,1,-7,9,-9,-3,-9,10,-7,4,-3,-4,-10,2,-4,-3,2,-2,-4,-4,-9,-8,2,-6,6,-2,8,1,-2,7,9,10,4,2,-5,1,-3,-4,-6,5,-10,-10,-6,4,5,-1,-1,-8,5,3,6,5,10,6,10,7,-2,-8,-7,4,6,-8,8,-4,-4,2,8,1,9,-3,9,-10,-6,-9,3,-6,-9,-7,-10,10,5,-6,-3,10,-2,-2,-4,4,-3,2,-6,-6,-5,-2,6,-1,-5,-4,3,10,-9,-10,7,3,-7,-7,-5,8,7,-9,1,4,8,-4,-5,8,-9,7,4,-5,6,2,6,-3,9,8,1,-7,3,10,10,-2,-8,-4,-10,3,-2,7,-6,-4,4,6,7,4,7,-8,6,5,-10,8,9,-3,-6,-10,1,-7,10,-10,-9,7,-2,4,-6,4,7,5,1,8,8,-10,-3,-6,2,-8,-2,-8,1,-2,10,-2,-6,-4,4,-6,1,-3,-7,-7,-5,-2,1,3,2,8,1,-3,-4,-8,1,3,2,-6,5,7,-8,10,9,-3,9,4,-9,1,-4,-4,-2,6,-2,-2,6,8,-8,-5,-2,-1,8,-2,-2,2,9,10,-10,-5,9,-9,7,-8,6,4,-2,8,10,-6,-3,10,-2,-5,-7,7,8,-2,5,-9,-3,-10,10,4,-10,-4,-9,-4,5,7,10,9,-2,-4,-10,2,8,8,-2,9,5,4,6,-6,7,-2,-7,-8,3,-10,5,-6,-3,-2,-9,8,4,7,-10,-10,6,8,6,-6,6,-2,5,-3,-6,-7,5,10,-7,-9,2,6,5,5,7,-10,5,-5,2,3,4,5,-5,-1,2,1,-3,-3,-8,10,8,-2,2,5,7,3,8,-3,1,-7,-3,-8,-3,5,-9,-9,-4,10,-8,3,-3,-5,2,-5,-1,7,-9,10,-6,-5,9,2,5,-3,-8,-8,-3,-1,-10,-10,-9,7,-4,9,-2,-6,10,-8,1,8,8,-2,9,-5,-2,-2,-4,8,-5,-9,-3,2,5,8,1,-7,2,-9,-3,-1,-3,-5,-1,-4,-9,-7,-8,-6,9,10,10,9,5,2,-6,4,-6,-6,-1,5,-3,-6,9,5,6,8,-3,7,-8,-7,-9,-4,1,2,-10,5,7,-8,3,-6,9,4,-2,-1,7,-3,-10,-9,-6,-4,-8,-10,10,3,3,10,-5,5,5,-6,-3,-7,5,-3,-9,-7,-6,3,-7,9,8,-2,-6,-8,1,3,2,-7,8,-8,-9,-5,4,-2,4,8,3,-7,-7,1,-9,-3,4,10,2,-10,-4,7,-3,-8,-2,-3,10,-7,-4,-6,1,-6,1,-7,-3,-5,4,-7,-1,-5,5,2,-5,2,-5,2,8,-3,1,2,-8,5,9,8,10,4,9,-1,-5,4,9,-10,-4,-6,2,3,2,-2,1,-2,-3,-4,-4,-9,-8,-1,-10,4,3,-1,5,-8,3,10,10,-2,-10,-7,1,-5,8,-6,8,-4,-9,9,10,-2,7,-6,-8,10,-5,4,3,-5,-7,1,10,-8,4,-4,3,9,2,7,-2,-7,3,2,-1,7,9,-1,5,9,-7,4,-1,-9,8,2,-4,6,-10,-3,9,-9,8,-9,-1,2,3,7,-1,-8,4,-9,-1,-6,-5,-2,-9,-5,2,1,4,9,-1,3,7,-1,3,1,-6,5,-6,-6,-9,-3,4,-4,9,-8,-2,-6,-2,1,-6,-9,7,-4,2,-9,2,2,8,-6,9,-1,5,-1,-4,-4,3,3,-7,5,10,8,8,9,6,-4,9,6,-1,-1,-7,5,8,2,-8,5,-2,9,-5,-5,2,-7,-5,5,10,-10,2,-9,-7,8,-1,-1,-9,3,9,-6,9,3,6,9,3,5,9,8,8,-9,-2,-1,1,7,-2,-2,-6,-5,1,8,-5,3,-8,10,-8,2,9,3,7,-1,-2,-2,-8,-1,-2,4,6,3,-8,-10,2,-8,-7,-5,10,-5,-1,-1,5,7,-4,7,10,-4,5,-9,-5,-9,10,7,2,-2,-1,9,6,-3,10,-10,2,-1,5,-5,8,5,10,8,7,2,-3,-4,-10,9,9,-8,-1,-9,10,-1,9,-6,9,2,4,-4,8,7,-2,-6,6,-1,5,-5,5,-5,1,7,7,-6,3,9,-7,-9,-3,-2,-9,7,-5,10,8,6,9,1,-1,9,8,-7,-4,-6,9,9,-10,-3,9,-5,-1,8,4,-5,8,-3,2,3,-6,7,4,-5,-2,-1,4,-8,9,-6,-5,8,-7,-2,-10,-6,-2,4,-1,-2,1,-2,9,1,-7,-1,-10,-8,9,-5,-4,7,-8,-4,4,-9,-9,-2,-2,6,-2,4,5,8,-1,-7,5,-1,-9,-1,-10,9,-3,10,6,5,-3,9,-10,-6,-9,5,8,-1,2,-9,-4,2,9,-3,9,10,-8,2,5,10,-10,2,-5,-5,4,-9,-10,4,-4,4,-6,5,-3,-3,-6,4,9,6,-8,-1,4,-9,-3,-6,1,-10,4,4,-4,-8,1,6,10,6,-2,-10,-6,-1,-3,6,4,-4,9,8,4,-4,7,-7,-4,7,-9,-2,-8,-4,9,7,-5,-4,9,-10,5,10,-3,-1,9,3,-6,4,8,-5,9,-10,4,-9,-3,8,2,-2,-4,-4,-2,10,1,-2,-2,-4,10,5,8,-9,-4,9,-6,3,-5,-2,5,4,3,-5,-2,6,-4,8,-7,-3,7,-7,4,-2,8,-5,-5,8,-5,-3,-3,1,-1,9,7,9,7,-6,5,-9,1,5,-3,3,6,-4,-8,4,3,7,7,-3,-1,5,-8,-8,-10,-6,6,8,-7,10,-7,-5,10,-10,10,-3,-6,-9,-5,-7,10,8,5,7,-10,7,1,-8,8,10,-5,10,-3,8,-6,3,-8,-1,8,-5,6,6,8,10,5,-5,-7,2,4,8,-4,-5,3,-7,5,-1,-6,10,-2,9,2,-6,8,9,-9,-9,1,7,-1,6,8,7,-4,-7,7,2,9,10,-9,9,-5,2,4,9,4,9,3,-6,-3,1,-9,1,4,-5,-8,10,-3,-1,-2,10,8,-9,-5,7,-8,-10,-3,4,10,-2,-2,-6,-5,-1,7,-4,-1,5,-8,6,3,4,4,-5,9,-7,-10,-7,-7,-1,-10,-3,-7,-8,3,4,9,1,-8,-10,-4,8,-7,8,-3,-2,3,3,4,-7,-5,-2,-9,-8,1,-3,-4,-8,6,-8,-2,-2,-6,7,6,10,4,-8,6,9,-3,-10,-3,-9,-4,-8,9,-1,4,-6,1,6,7,10,7,1,-4,-8,-9,6,5,-10,-5,-9,1,1,-1,-9,8,-4,-1,-6,5,-1,-4,10,2,-4,-2,-6,-8,7,4,2,9,1,-8,-6,3,-7,-6,-8,8,-5,-5,-5,10,6,10,-7,1,-1,-7,2,-4,-8,-6,9,8,-4,7,-8,1,-10,-10,-2,-7,10,9,7,-10,4,-1,2,8,-2,7,-9,-4,1,-8,-4,5,-2,-5,8,1,-1,-4,4,9,7,6,6,7,-3,-2,3,-1,4,1,1,-3,-8,5,10,-8,2,7,5,5,10,-6,-7,-7,5,2,-1,8,3,-1,-9,-4,-6,-9,2,8,-3,6,-3,10,10,-2,6,-2,5,-4,6,-5,6,3,10,-1,-6,-3,-9,-7,-5,-3,10,10,1,-10,-3,-9,-9,-8,-4,3,7,10,-9,6,-7,4,4,-5,-1,4,-1,2,7,-10,10,-2,-9,2,1,-3,7,-8,-3,-10,9,8,-8,10,10,-6,-5,-7,1,4,7,10,7,9,-2,-6,-2,3,-7,-5,4,9,-10,-6,6,-4,-9,9,6,-8,6,1,2,-9,-8,-8,-6,4,5,-10,9,-6,-10,-6,2,5,10,7,2,9,-10,2,5,-3,-5,-1,-7,-3,-1,-3,3,-2,-6,4,-5,-7,1,-1,5,-7,9,5,5,4,8,-9,-5,-5,2,-8,2,9,5,10,-6,-2,-6,-10,8,-5,1,-9,-6,9,4,2,3,9,-5,-9,7,5,-8,-4,-9,3,4,-8,8,6,-5,8,-4,-5,8,-8,-3,10,-8,-10,-3,8,-6,-6,4,-6,4,4,-1,-5,-2,5,7,-1,-10,-3,3,-8,8,1,8,10,1,10,-4,2,9,3,3,-5,4,-3,1,-4,-7,-2,4,9,-5,-9,3,7,1,9,6,6,-2,-7,-4,4,9,8,-6,-1,5,2,-5,9,-10,9,-2,6,-6,7,-5,1,6,7,6,5,-10,-9,-7,-1,7,-1,-7,-3,9,2,10,7,-5,-8,-2,4,1,7,2,-2,-7,7,1,4,-7,-5,-2,-3,-5,-9,5,9,7,-1,-3,7,10,-2,2,-3,4,8,-8,-4,1,2,-9,9,6,-4,-6,8,2,5,6,3,-5,8,1,8,7,5,2,9,-7,-8,-3,7,6,9,1,2,2,-9,1,-4,-1,2,4,-3,4,4,-10,3,2,-8,4,8,7,9,-7,4,-4,1,-10,1,-8,1,3,-3,-6,9,-8,-5,2,-3,-7,-9,5,-10,-6,9,3,3,-6,2,-7,1,6,2,-10,-1,6,-9,-9,6,-8,-9,-6,9,-9,3,4,1,10,1,2,8,-9,-1,-5,-2,-3,-6,-3,1,7,-8,-10,2,4,-9,-3,-6,-1,1,-3,9,-5,-5,9,10,3,-7,-7,-2,-10,1,5,6,-4,4,-1,5,9,4,-9,-3,4,-3,1,-4,-6,6,4,-9,-10,-8,-7,9,-5,3,-9,4,10,-4,5,-2,5,-2,2,7,-8,5,8,-1,-6,4,-5,-1,-8,-6,3,5,5,-8,1,-9,10,4,7,-2,-4,-10,-7,-3,-4,-9,6,8,3,8,-1,3,-10,-1,6,10,10,-8,1,-3,8,-3,-7,-6,6,6,-1,-9,8,10,3,-4,1,9,3,6,-5,-6,1,5,-7,7,2,1,-5,-5,-2,-1,-1,5,-6,5,-2,-6,-4,4,-3,-1,6,4,4,2,-8,-9,7,3,4,5,-1,-3,-5,8,8,1,-1,7,-4,-1,2,-1,3,2,-2,-7,1,9,9,-2,-7,2,9,5,-8,8,-8,1,-1,-1,2,-7,10,-7,-3,5,-3,2,-8,-7,-5,8,-4,-5,2,1,3,-4,-3,-1,9,8,5,-6,-9,9,10,5,6,2,-7,-1,8,-5,-6,7,4,-9,-5,4,-10,8,-2,-5,-5,8,7,-2,3,-5,-6,4,8,-1,-8,7,-9,9,7,10,10,-4,7,3,-7,-9,-1,-3,6,-3,8,-4,4,6,7,5,-6,-4,9,3,6,-9,6,-7,5,-9,-10,9,4,7,-3,-9,-5,2,-2,10,-8,6,-10,-6,-3,-7,8,6,1,-5,8,-5,-9,-7,-3,-9,-7,-5,-8,-1,8,3,-3,-9,-2,9,8,-3,3,8,-8,-9,3,-9,8,1,7,3,-5,-4,-7,-7,9,4,9,-1,10,-1,7,4,-1,1,-1,7,7,2,-6,-10,10,-8,7,-5,1,-8,5,2,-6,-3,-7,2,-4,7,5,5,-3,-6,2,5,-9,-2,6,-2,8,1,8,9,-2,-9,6,-2,-9,-7,-2,-4,9,5,9,10,-3,-5,6,10,-10,5,-7,5,7,-6,-6,10,-8,3,-2,-7,3,3,-5,7,6,-1,1,8,10,9,-6,-3,1,2,-10,8,10,-5,8,10,6,-6,9,-8,-8,7,3,-8,8,8,8,1,9,1,-10,1,4,4,1,-2,-7,5,-9,-6,1,-4,2,-7,1,-6,10,-6,5,6,4,-9,7,2,-4,-2,2,6,-9,-5,-2,1,10,-6,1,-5,2], dtype = "uint64")#candidate|15658|(2288,)|const|uint64
call_15656 = relay.TupleGetItem(func_3104_call(relay.reshape(var_15657.astype('int16'), [7, 8, 4]), relay.reshape(const_15658.astype('uint64'), [2288,]), relay.reshape(call_15637.astype('float64'), [30, 2]), ), 4)
call_15659 = relay.TupleGetItem(func_3108_call(relay.reshape(var_15657.astype('int16'), [7, 8, 4]), relay.reshape(const_15658.astype('uint64'), [2288,]), relay.reshape(call_15637.astype('float64'), [30, 2]), ), 4)
output = relay.Tuple([call_15637,call_15656,var_15657,const_15658,])
output2 = relay.Tuple([call_15638,call_15659,var_15657,const_15658,])
func_15673 = relay.Function([var_15657,], output)
mod['func_15673'] = func_15673
mod = relay.transform.InferType()(mod)
mutated_mod['func_15673'] = func_15673
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15674 = relay.var("var_15674", dtype = "int16", shape = (224,))#candidate|15674|(224,)|var|int16
func_15673_call = mutated_mod.get_global_var('func_15673')
call_15675 = func_15673_call(var_15674)
output = call_15675
func_15676 = relay.Function([var_15674], output)
mutated_mod['func_15676'] = func_15676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15482_call = mod.get_global_var('func_15482')
func_15484_call = mutated_mod.get_global_var('func_15484')
call_15701 = relay.TupleGetItem(func_15482_call(), 0)
call_15702 = relay.TupleGetItem(func_15484_call(), 0)
func_6125_call = mod.get_global_var('func_6125')
func_6126_call = mutated_mod.get_global_var('func_6126')
call_15714 = relay.TupleGetItem(func_6125_call(), 0)
call_15715 = relay.TupleGetItem(func_6126_call(), 0)
output = relay.Tuple([call_15701,call_15714,])
output2 = relay.Tuple([call_15702,call_15715,])
func_15719 = relay.Function([], output)
mod['func_15719'] = func_15719
mod = relay.transform.InferType()(mod)
mutated_mod['func_15719'] = func_15719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15719_call = mutated_mod.get_global_var('func_15719')
call_15720 = func_15719_call()
output = call_15720
func_15721 = relay.Function([], output)
mutated_mod['func_15721'] = func_15721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12200_call = mod.get_global_var('func_12200')
func_12201_call = mutated_mod.get_global_var('func_12201')
call_15728 = func_12200_call()
call_15729 = func_12200_call()
func_14587_call = mod.get_global_var('func_14587')
func_14589_call = mutated_mod.get_global_var('func_14589')
call_15752 = func_14587_call()
call_15753 = func_14587_call()
func_14026_call = mod.get_global_var('func_14026')
func_14030_call = mutated_mod.get_global_var('func_14030')
var_15758 = relay.var("var_15758", dtype = "uint8", shape = (351,))#candidate|15758|(351,)|var|uint8
call_15757 = relay.TupleGetItem(func_14026_call(relay.reshape(var_15758.astype('uint8'), [13, 3, 9]), relay.reshape(var_15758.astype('uint8'), [13, 3, 9]), ), 1)
call_15759 = relay.TupleGetItem(func_14030_call(relay.reshape(var_15758.astype('uint8'), [13, 3, 9]), relay.reshape(var_15758.astype('uint8'), [13, 3, 9]), ), 1)
const_15777 = relay.const([-2,-1,-2,-4,-10,6,4,10,-6,-8,7,7,10,1,1,-5,8,-1,2,-1,-10,2,6,2,6,-1,9,6,9,5,-3,4,6,-2,-9,-3,-10,4,9,-10,-4,-10,8,4,3,-9,10,8,7,8,-10,4,8,-8,4,3,-8,2,-9,5,-6,8,6,-3,7,10,2,9,-1,-6,2,4,-4,-8,-5,-5,-5,-6,-3,7,-2,-7,-10,4,-3,8,-2,5,-9,9,6,-4,8,-6,-10,-1,8,7,-4,9,5,-3,10,-5,3,-4,9,-1,-7,-10,-8,9,8,-5,-1,8,-10,5,10,-10,5,1,-9,2,9,-4,10,-4,3,9,-4,10,-9,-3,-8,-2,-6,-6,5,-2,8,3,9,-6,-9,-6,5,6,-4,3,-3,-4,7,-3,-8,9,8,5,1,10,10,2,4,9,8,-10,6,9,4,8,-4,-9,10,2,7,3,9,-3,5,3,-4,4,6,3,-3,3,7,2,8,-3,7,2,-3,-1,7,-4,8,8,1,-6,-2,4,3,-9,9,5,9,-1,4,-3,-5,-1,4,7,-3,-10,1,6,-7,4,8,1,7,-2,-4,-2,-1,-10,-4,-8,9,2,1,6,3,-5,9,8,8,9,-4,-8,3,10,6,-6,8,-7,-8,-9,4,3,10,3,1,7,-2,2,5,-5,-4,8,-9,-2,-9,-7,5,-10,1,-10,-5,10,1,1,6,9,-6,-3,-1,1,6,-6,-8,-3,-10,-3,-1,10,-7,-10,-10,-2,-5,1,-9,-7,-2,3,1,-1,10,-8,9,3,-3,-8,1,9,-6,-1,5,-10,-2,9,1,-8,7,2,-8,-1,-9,3,-2,3,5,3,-1,-8,-5,10,-10,9,-8,3,-7,6,5,5,4,-5,1,10,8,8,-7,-9,9,-4,10,-3,-4], dtype = "uint8")#candidate|15777|(351,)|const|uint8
bop_15778 = relay.bitwise_xor(var_15758.astype('int8'), relay.reshape(const_15777.astype('int8'), relay.shape_of(var_15758))) # shape=(351,)
output = relay.Tuple([call_15728,call_15752,call_15757,bop_15778,])
output2 = relay.Tuple([call_15729,call_15753,call_15759,bop_15778,])
F = relay.Function([var_15758,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_15758,], output2)
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
