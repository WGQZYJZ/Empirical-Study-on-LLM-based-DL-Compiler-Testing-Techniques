import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_665 = relay.const([[[-5.574824,7.397728],[4.037033,1.680662],[3.490818,-3.266301],[8.839609,-4.469059],[-4.267231,-2.728622],[-3.756211,5.481261],[9.174322,-6.564423]],[[-0.249054,7.109148],[2.329976,4.481447],[7.625868,-6.702280],[7.209139,9.817092],[6.696984,-6.488343],[-3.797145,3.129331],[-4.778889,6.103749]],[[7.363270,3.081516],[2.688750,6.844673],[7.519212,3.171714],[1.972919,8.665862],[6.673432,-3.108345],[4.523085,-2.837897],[3.941687,-2.432412]],[[-3.989244,2.568436],[8.096063,8.697405],[-1.194236,-6.284292],[3.339597,-3.748568],[9.024095,6.778074],[-2.548230,7.579206],[0.686035,6.268735]],[[-6.647151,-6.349928],[1.918388,-1.375831],[-1.448996,-3.510913],[-7.787508,-5.083468],[-4.454281,7.768391],[-4.966640,-8.685164],[-1.060793,-9.340513]],[[8.619776,-1.179785],[-3.501167,-1.570521],[-0.908000,-4.272962],[-6.008224,7.403286],[3.206213,-5.684187],[-8.298661,-4.242521],[4.485070,3.857526]],[[-2.640044,2.577652],[6.308553,1.928974],[-6.721384,-6.259167],[2.520684,8.361309],[6.952149,-3.186764],[-2.617962,-3.984706],[-9.567997,2.498454]],[[-7.892102,9.244385],[8.033258,-3.723580],[-4.856109,-9.868509],[-2.376339,-9.070217],[7.104773,5.192986],[-6.454854,-9.216448],[4.213104,-4.042941]],[[1.091613,7.511096],[-8.921027,-7.212410],[1.196929,2.194157],[5.802720,-3.715479],[-9.257963,1.945696],[-9.091734,-3.762598],[-4.932028,3.838812]],[[4.761764,-9.768788],[6.086975,-7.880509],[-8.316030,3.713778],[-5.640980,-5.151039],[-3.767686,1.675993],[1.759836,2.948394],[2.211665,-5.614942]]], dtype = "float64")#candidate|665|(10, 7, 2)|const|float64
uop_666 = relay.atanh(const_665.astype('float64')) # shape=(10, 7, 2)
output = uop_666
output2 = uop_666
func_668 = relay.Function([], output)
mod['func_668'] = func_668
mod = relay.transform.InferType()(mod)
output = func_668()
func_669 = relay.Function([], output)
mutated_mod['func_669'] = func_669
mutated_mod = relay.transform.InferType()(mutated_mod)
func_668_call = mod.get_global_var('func_668')
func_669_call = mutated_mod.get_global_var('func_669')
call_684 = func_668_call()
call_685 = func_668_call()
func_668_call = mod.get_global_var('func_668')
func_669_call = mutated_mod.get_global_var('func_669')
call_706 = func_668_call()
call_707 = func_668_call()
output = relay.Tuple([call_684,call_706,])
output2 = relay.Tuple([call_685,call_707,])
func_751 = relay.Function([], output)
mod['func_751'] = func_751
mod = relay.transform.InferType()(mod)
output = func_751()
func_752 = relay.Function([], output)
mutated_mod['func_752'] = func_752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_668_call = mod.get_global_var('func_668')
func_669_call = mutated_mod.get_global_var('func_669')
call_798 = func_668_call()
call_799 = func_668_call()
uop_804 = relay.erf(call_798.astype('float32')) # shape=(10, 7, 2)
uop_806 = relay.erf(call_799.astype('float32')) # shape=(10, 7, 2)
func_668_call = mod.get_global_var('func_668')
func_669_call = mutated_mod.get_global_var('func_669')
call_815 = func_668_call()
call_816 = func_668_call()
output = relay.Tuple([uop_804,call_815,])
output2 = relay.Tuple([uop_806,call_816,])
func_827 = relay.Function([], output)
mod['func_827'] = func_827
mod = relay.transform.InferType()(mod)
mutated_mod['func_827'] = func_827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_827_call = mutated_mod.get_global_var('func_827')
call_828 = func_827_call()
output = call_828
func_829 = relay.Function([], output)
mutated_mod['func_829'] = func_829
mutated_mod = relay.transform.InferType()(mutated_mod)
var_839 = relay.var("var_839", dtype = "int32", shape = (7, 2, 4))#candidate|839|(7, 2, 4)|var|int32
var_840 = relay.var("var_840", dtype = "int32", shape = (7, 2, 4))#candidate|840|(7, 2, 4)|var|int32
bop_841 = relay.bitwise_xor(var_839.astype('int32'), relay.reshape(var_840.astype('int32'), relay.shape_of(var_839))) # shape=(7, 2, 4)
bop_848 = relay.bitwise_or(var_839.astype('uint32'), relay.reshape(var_840.astype('uint32'), relay.shape_of(var_839))) # shape=(7, 2, 4)
func_751_call = mod.get_global_var('func_751')
func_752_call = mutated_mod.get_global_var('func_752')
call_858 = relay.TupleGetItem(func_751_call(), 0)
call_859 = relay.TupleGetItem(func_752_call(), 0)
func_668_call = mod.get_global_var('func_668')
func_669_call = mutated_mod.get_global_var('func_669')
call_872 = func_668_call()
call_873 = func_668_call()
output = relay.Tuple([bop_841,bop_848,call_858,call_872,])
output2 = relay.Tuple([bop_841,bop_848,call_859,call_873,])
func_896 = relay.Function([var_839,var_840,], output)
mod['func_896'] = func_896
mod = relay.transform.InferType()(mod)
var_897 = relay.var("var_897", dtype = "int32", shape = (7, 2, 4))#candidate|897|(7, 2, 4)|var|int32
var_898 = relay.var("var_898", dtype = "int32", shape = (7, 2, 4))#candidate|898|(7, 2, 4)|var|int32
output = func_896(var_897,var_898,)
func_899 = relay.Function([var_897,var_898,], output)
mutated_mod['func_899'] = func_899
mutated_mod = relay.transform.InferType()(mutated_mod)
func_751_call = mod.get_global_var('func_751')
func_752_call = mutated_mod.get_global_var('func_752')
call_933 = relay.TupleGetItem(func_751_call(), 0)
call_934 = relay.TupleGetItem(func_752_call(), 0)
output = call_933
output2 = call_934
func_935 = relay.Function([], output)
mod['func_935'] = func_935
mod = relay.transform.InferType()(mod)
output = func_935()
func_936 = relay.Function([], output)
mutated_mod['func_936'] = func_936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_668_call = mod.get_global_var('func_668')
func_669_call = mutated_mod.get_global_var('func_669')
call_964 = func_668_call()
call_965 = func_668_call()
func_751_call = mod.get_global_var('func_751')
func_752_call = mutated_mod.get_global_var('func_752')
call_968 = relay.TupleGetItem(func_751_call(), 1)
call_969 = relay.TupleGetItem(func_752_call(), 1)
output = relay.Tuple([call_964,call_968,])
output2 = relay.Tuple([call_965,call_969,])
func_971 = relay.Function([], output)
mod['func_971'] = func_971
mod = relay.transform.InferType()(mod)
mutated_mod['func_971'] = func_971
mutated_mod = relay.transform.InferType()(mutated_mod)
func_971_call = mutated_mod.get_global_var('func_971')
call_972 = func_971_call()
output = call_972
func_973 = relay.Function([], output)
mutated_mod['func_973'] = func_973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_668_call = mod.get_global_var('func_668')
func_669_call = mutated_mod.get_global_var('func_669')
call_985 = func_668_call()
call_986 = func_668_call()
var_990 = relay.var("var_990", dtype = "float64", shape = (10, 7, 2))#candidate|990|(10, 7, 2)|var|float64
bop_991 = relay.maximum(call_985.astype('int64'), relay.reshape(var_990.astype('int64'), relay.shape_of(call_985))) # shape=(10, 7, 2)
bop_994 = relay.maximum(call_986.astype('int64'), relay.reshape(var_990.astype('int64'), relay.shape_of(call_986))) # shape=(10, 7, 2)
bop_1000 = relay.add(var_990.astype('uint8'), relay.reshape(call_985.astype('uint8'), relay.shape_of(var_990))) # shape=(10, 7, 2)
bop_1003 = relay.add(var_990.astype('uint8'), relay.reshape(call_986.astype('uint8'), relay.shape_of(var_990))) # shape=(10, 7, 2)
uop_1010 = relay.cos(var_990.astype('float64')) # shape=(10, 7, 2)
output = relay.Tuple([bop_991,bop_1000,uop_1010,])
output2 = relay.Tuple([bop_994,bop_1003,uop_1010,])
func_1027 = relay.Function([var_990,], output)
mod['func_1027'] = func_1027
mod = relay.transform.InferType()(mod)
mutated_mod['func_1027'] = func_1027
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1028 = relay.var("var_1028", dtype = "float64", shape = (10, 7, 2))#candidate|1028|(10, 7, 2)|var|float64
func_1027_call = mutated_mod.get_global_var('func_1027')
call_1029 = func_1027_call(var_1028)
output = call_1029
func_1030 = relay.Function([var_1028], output)
mutated_mod['func_1030'] = func_1030
mutated_mod = relay.transform.InferType()(mutated_mod)
func_668_call = mod.get_global_var('func_668')
func_669_call = mutated_mod.get_global_var('func_669')
call_1032 = func_668_call()
call_1033 = func_668_call()
var_1045 = relay.var("var_1045", dtype = "float64", shape = (10, 7, 2))#candidate|1045|(10, 7, 2)|var|float64
bop_1046 = relay.logical_and(call_1032.astype('bool'), relay.reshape(var_1045.astype('bool'), relay.shape_of(call_1032))) # shape=(10, 7, 2)
bop_1049 = relay.logical_and(call_1033.astype('bool'), relay.reshape(var_1045.astype('bool'), relay.shape_of(call_1033))) # shape=(10, 7, 2)
func_896_call = mod.get_global_var('func_896')
func_899_call = mutated_mod.get_global_var('func_899')
const_1051 = relay.const([-6,5,-6,-10,-9,-4,-2,10,3,-10,4,5,-5,-1,-4,2,-7,-2,7,-5,-6,1,-9,-3,-8,1,7,5,2,6,8,-7,-4,-7,-10,9,3,-5,-4,7,1,5,5,-7,-8,4,-10,9,10,7,10,8,-8,6,-3,-4], dtype = "int32")#candidate|1051|(56,)|const|int32
call_1050 = relay.TupleGetItem(func_896_call(relay.reshape(const_1051.astype('int32'), [7, 2, 4]), relay.reshape(const_1051.astype('int32'), [7, 2, 4]), ), 0)
call_1052 = relay.TupleGetItem(func_899_call(relay.reshape(const_1051.astype('int32'), [7, 2, 4]), relay.reshape(const_1051.astype('int32'), [7, 2, 4]), ), 0)
func_827_call = mod.get_global_var('func_827')
func_829_call = mutated_mod.get_global_var('func_829')
call_1054 = relay.TupleGetItem(func_827_call(), 1)
call_1055 = relay.TupleGetItem(func_829_call(), 1)
output = relay.Tuple([bop_1046,call_1050,const_1051,call_1054,])
output2 = relay.Tuple([bop_1049,call_1052,const_1051,call_1055,])
func_1070 = relay.Function([var_1045,], output)
mod['func_1070'] = func_1070
mod = relay.transform.InferType()(mod)
var_1071 = relay.var("var_1071", dtype = "float64", shape = (10, 7, 2))#candidate|1071|(10, 7, 2)|var|float64
output = func_1070(var_1071)
func_1072 = relay.Function([var_1071], output)
mutated_mod['func_1072'] = func_1072
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1084 = relay.var("var_1084", dtype = "int64", shape = ())#candidate|1084|()|var|int64
const_1085 = relay.const([[[-10,1,5,-4,-7,-8,7],[-1,-9,2,-6,-6,-2,-5],[-2,8,-1,4,1,5,-2],[4,-5,8,5,-3,-4,-7],[-7,-5,-3,2,9,3,4],[7,-9,7,-5,1,7,-10],[2,-9,2,-9,-4,10,-7],[-5,-9,10,3,-5,2,-8],[-9,-2,-8,1,5,-6,10]],[[-6,8,-9,6,-8,-7,-5],[8,-10,4,7,4,-1,-7],[2,2,4,9,-9,-5,2],[-8,10,4,3,5,7,10],[-10,6,4,-8,-10,-6,-2],[3,-2,4,-9,6,-4,3],[-2,-3,2,4,7,-8,1],[-5,-4,8,3,2,10,-5],[-8,-8,-3,-3,-2,1,-3]],[[8,3,-8,4,-5,-9,9],[4,6,4,4,-6,-2,-6],[-8,4,-2,9,-5,7,10],[-8,5,-2,-6,6,-4,9],[-1,-9,-3,-4,1,6,-6],[6,8,4,-6,6,-3,-3],[3,2,-6,-2,5,3,-1],[10,1,3,1,-5,-4,-10],[1,3,-3,9,-6,-8,9]],[[7,-2,7,-4,-5,8,2],[10,10,-5,-7,-7,-10,9],[6,-3,10,-9,-1,7,-7],[-5,-6,3,6,8,8,10],[-2,8,-1,-10,-6,-7,-3],[-4,-9,3,6,1,6,5],[-7,-2,8,-7,-2,-9,10],[-7,8,7,-2,3,6,10],[-3,6,4,9,9,-10,-6]],[[1,-2,-9,10,8,-6,-10],[4,6,8,9,1,3,-5],[1,1,7,10,6,4,2],[6,4,-5,-7,-4,5,6],[5,3,3,10,9,-8,10],[8,5,7,4,-2,4,-9],[9,-9,5,10,5,-1,-10],[9,2,3,3,-7,-1,-8],[-2,4,-2,-6,4,-8,8]],[[5,-8,-9,4,-8,-1,4],[3,-6,10,-8,4,1,4],[1,9,-9,2,7,-9,5],[-9,3,-4,9,-1,-8,3],[-5,1,8,-3,4,4,-3],[6,4,-8,9,5,6,7],[3,5,6,7,3,2,5],[-1,-10,8,-4,2,-10,3],[7,2,-9,-9,3,10,5]],[[-5,9,-1,-5,-4,7,2],[7,7,-3,-3,6,-9,9],[4,3,-4,-7,3,6,-9],[-7,2,6,5,8,6,-1],[2,-8,2,8,-6,-3,-7],[8,3,8,-9,-5,-8,2],[9,-10,-3,-1,-10,3,6],[-6,-6,-10,2,-4,-4,5],[4,-7,1,5,-6,1,5]],[[-3,-3,-3,-5,-5,1,-8],[-8,1,10,-4,7,-7,4],[-10,-5,2,-2,-4,-8,-6],[8,-7,6,-8,-6,-7,2],[6,5,6,9,-5,-3,-9],[-6,1,8,-10,-6,1,3],[-4,6,-2,6,-9,8,-5],[1,-3,1,-2,-1,-5,3],[8,-6,2,4,10,-3,-4]],[[-1,3,5,10,7,-6,6],[-5,7,-6,8,2,-1,-2],[1,5,-5,5,-2,5,-9],[-10,-10,6,10,10,-10,-8],[5,3,-5,10,-7,-7,2],[-8,3,-7,-3,-2,-5,-1],[-5,3,-10,-7,-7,3,4],[10,-2,-8,-8,-7,8,-6],[-2,-9,7,-6,-10,-9,10]],[[8,-2,9,-9,-10,-1,-8],[8,3,10,-6,4,3,5],[-1,-4,10,-7,1,-5,1],[-7,5,4,5,2,10,-3],[9,6,4,9,7,2,-2],[-8,5,3,-3,9,-10,1],[-6,4,4,-7,10,-4,-4],[5,-7,10,-2,-1,-1,-5],[3,2,10,-7,7,-7,-4]],[[4,-9,-5,-5,8,1,2],[-10,-4,3,-2,-3,9,5],[-9,-9,8,-3,4,-1,5],[2,3,-6,-6,-4,-4,-9],[8,-1,4,7,7,6,-10],[-6,10,-4,-1,-1,-1,-5],[-1,8,-10,-4,8,-10,-3],[-8,5,10,1,8,4,7],[2,10,10,-1,-8,7,-8]],[[3,-5,-6,5,4,10,8],[-1,1,8,-7,1,9,4],[-7,4,6,3,10,6,3],[-7,-1,-5,2,-4,-4,-8],[2,10,8,1,3,-4,9],[-6,7,3,-2,10,4,4],[9,-10,5,2,5,-7,-5],[-3,4,-9,5,-1,-10,10],[7,1,-5,6,-2,5,-10]],[[-10,-5,1,4,-10,-10,5],[-2,-6,-8,-4,8,5,6],[9,-2,3,4,7,-2,7],[8,5,-7,-10,8,8,-1],[7,-4,-5,7,-6,-2,9],[9,-9,9,8,5,-3,-1],[-8,-5,-4,-1,-5,-9,-9],[3,-6,-5,-1,10,-2,-1],[-7,-7,7,-10,-3,9,1]],[[-1,8,10,8,8,-2,3],[3,-1,6,-5,-4,-3,-6],[-6,-10,-7,9,-2,-5,-8],[-1,2,-3,-6,5,-4,-8],[5,-9,1,6,-8,9,5],[2,-2,-4,-9,-9,6,8],[-2,-6,10,-8,5,-3,2],[-4,-6,10,-1,2,1,-7],[-5,8,-3,4,10,-8,-9]]], dtype = "int64")#candidate|1085|(14, 9, 7)|const|int64
bop_1086 = relay.greater_equal(var_1084.astype('bool'), const_1085.astype('bool')) # shape=(14, 9, 7)
uop_1097 = relay.cos(bop_1086.astype('float64')) # shape=(14, 9, 7)
func_1027_call = mod.get_global_var('func_1027')
func_1030_call = mutated_mod.get_global_var('func_1030')
var_1100 = relay.var("var_1100", dtype = "float64", shape = (1, 140))#candidate|1100|(1, 140)|var|float64
call_1099 = relay.TupleGetItem(func_1027_call(relay.reshape(var_1100.astype('float64'), [10, 7, 2])), 0)
call_1101 = relay.TupleGetItem(func_1030_call(relay.reshape(var_1100.astype('float64'), [10, 7, 2])), 0)
func_751_call = mod.get_global_var('func_751')
func_752_call = mutated_mod.get_global_var('func_752')
call_1104 = relay.TupleGetItem(func_751_call(), 1)
call_1105 = relay.TupleGetItem(func_752_call(), 1)
func_935_call = mod.get_global_var('func_935')
func_936_call = mutated_mod.get_global_var('func_936')
call_1106 = func_935_call()
call_1107 = func_935_call()
output = relay.Tuple([uop_1097,call_1099,var_1100,call_1104,call_1106,])
output2 = relay.Tuple([uop_1097,call_1101,var_1100,call_1105,call_1107,])
func_1110 = relay.Function([var_1084,var_1100,], output)
mod['func_1110'] = func_1110
mod = relay.transform.InferType()(mod)
var_1111 = relay.var("var_1111", dtype = "int64", shape = ())#candidate|1111|()|var|int64
var_1112 = relay.var("var_1112", dtype = "float64", shape = (1, 140))#candidate|1112|(1, 140)|var|float64
output = func_1110(var_1111,var_1112,)
func_1113 = relay.Function([var_1111,var_1112,], output)
mutated_mod['func_1113'] = func_1113
mutated_mod = relay.transform.InferType()(mutated_mod)
func_668_call = mod.get_global_var('func_668')
func_669_call = mutated_mod.get_global_var('func_669')
call_1126 = func_668_call()
call_1127 = func_668_call()
output = call_1126
output2 = call_1127
func_1136 = relay.Function([], output)
mod['func_1136'] = func_1136
mod = relay.transform.InferType()(mod)
output = func_1136()
func_1137 = relay.Function([], output)
mutated_mod['func_1137'] = func_1137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_827_call = mod.get_global_var('func_827')
func_829_call = mutated_mod.get_global_var('func_829')
call_1167 = relay.TupleGetItem(func_827_call(), 0)
call_1168 = relay.TupleGetItem(func_829_call(), 0)
func_1070_call = mod.get_global_var('func_1070')
func_1072_call = mutated_mod.get_global_var('func_1072')
call_1169 = relay.TupleGetItem(func_1070_call(relay.reshape(call_1167.astype('float64'), [10, 7, 2])), 1)
call_1170 = relay.TupleGetItem(func_1072_call(relay.reshape(call_1167.astype('float64'), [10, 7, 2])), 1)
func_1070_call = mod.get_global_var('func_1070')
func_1072_call = mutated_mod.get_global_var('func_1072')
call_1190 = relay.TupleGetItem(func_1070_call(relay.reshape(call_1167.astype('float64'), [10, 7, 2])), 0)
call_1191 = relay.TupleGetItem(func_1072_call(relay.reshape(call_1167.astype('float64'), [10, 7, 2])), 0)
func_935_call = mod.get_global_var('func_935')
func_936_call = mutated_mod.get_global_var('func_936')
call_1197 = func_935_call()
call_1198 = func_935_call()
func_827_call = mod.get_global_var('func_827')
func_829_call = mutated_mod.get_global_var('func_829')
call_1205 = relay.TupleGetItem(func_827_call(), 1)
call_1206 = relay.TupleGetItem(func_829_call(), 1)
func_1136_call = mod.get_global_var('func_1136')
func_1137_call = mutated_mod.get_global_var('func_1137')
call_1210 = func_1136_call()
call_1211 = func_1136_call()
const_1227 = relay.const([[[3,-7,-1,7],[3,-5,2,4]],[[10,8,7,-1],[5,-4,-8,-4]],[[-6,7,-9,-5],[-8,3,-2,7]],[[-8,-5,9,9],[6,2,-6,-3]],[[7,-8,-4,-9],[5,-4,10,-1]],[[8,-7,-6,4],[-10,3,1,10]],[[6,4,-3,4],[-6,-7,2,9]]], dtype = "int32")#candidate|1227|(7, 2, 4)|const|int32
bop_1228 = relay.minimum(call_1169.astype('float64'), relay.reshape(const_1227.astype('float64'), relay.shape_of(call_1169))) # shape=(7, 2, 4)
bop_1231 = relay.minimum(call_1170.astype('float64'), relay.reshape(const_1227.astype('float64'), relay.shape_of(call_1170))) # shape=(7, 2, 4)
const_1238 = relay.const([[[True,False],[True,True],[True,False],[True,False],[False,True],[False,True],[True,True]],[[False,True],[False,False],[False,False],[True,True],[True,False],[False,True],[False,False]],[[True,True],[False,False],[False,False],[True,True],[False,False],[True,False],[False,True]],[[False,True],[True,False],[False,True],[False,False],[True,True],[True,True],[True,False]],[[False,False],[False,True],[True,True],[True,True],[True,True],[False,True],[True,True]],[[True,True],[True,True],[False,False],[True,False],[True,True],[True,True],[True,False]],[[False,False],[False,False],[False,True],[True,False],[False,False],[True,True],[True,False]],[[False,True],[True,True],[False,False],[True,True],[False,False],[True,False],[False,False]],[[True,True],[True,True],[True,True],[True,False],[False,False],[False,False],[False,True]],[[True,False],[True,True],[True,True],[True,True],[True,False],[False,False],[False,False]]], dtype = "bool")#candidate|1238|(10, 7, 2)|const|bool
bop_1239 = relay.bitwise_and(call_1190.astype('int16'), relay.reshape(const_1238.astype('int16'), relay.shape_of(call_1190))) # shape=(10, 7, 2)
bop_1242 = relay.bitwise_and(call_1191.astype('int16'), relay.reshape(const_1238.astype('int16'), relay.shape_of(call_1191))) # shape=(10, 7, 2)
output = relay.Tuple([call_1167,call_1197,call_1205,call_1210,bop_1228,bop_1239,])
output2 = relay.Tuple([call_1168,call_1198,call_1206,call_1211,bop_1231,bop_1242,])
func_1255 = relay.Function([], output)
mod['func_1255'] = func_1255
mod = relay.transform.InferType()(mod)
output = func_1255()
func_1256 = relay.Function([], output)
mutated_mod['func_1256'] = func_1256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1255_call = mod.get_global_var('func_1255')
func_1256_call = mutated_mod.get_global_var('func_1256')
call_1288 = relay.TupleGetItem(func_1255_call(), 1)
call_1289 = relay.TupleGetItem(func_1256_call(), 1)
output = call_1288
output2 = call_1289
func_1308 = relay.Function([], output)
mod['func_1308'] = func_1308
mod = relay.transform.InferType()(mod)
mutated_mod['func_1308'] = func_1308
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1308_call = mutated_mod.get_global_var('func_1308')
call_1309 = func_1308_call()
output = call_1309
func_1310 = relay.Function([], output)
mutated_mod['func_1310'] = func_1310
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1328 = relay.var("var_1328", dtype = "float32", shape = (1, 4, 3))#candidate|1328|(1, 4, 3)|var|float32
uop_1329 = relay.sinh(var_1328.astype('float32')) # shape=(1, 4, 3)
bop_1334 = relay.power(var_1328.astype('float64'), relay.reshape(uop_1329.astype('float64'), relay.shape_of(var_1328))) # shape=(1, 4, 3)
func_1110_call = mod.get_global_var('func_1110')
func_1113_call = mutated_mod.get_global_var('func_1113')
var_1340 = relay.var("var_1340", dtype = "int64", shape = ())#candidate|1340|()|var|int64
const_1341 = relay.const([0.781243,-2.574054,-1.727872,4.480666,3.384350,8.570335,9.730231,0.963637,-9.929821,3.636419,-9.642219,5.541032,-8.542144,-4.279125,9.396954,2.331222,3.011936,-2.883891,8.171361,-5.876838,1.385233,7.520997,-4.820891,0.605646,2.946109,9.024263,9.280152,-3.248047,-6.571661,4.725316,9.388424,0.098429,-7.217962,-0.696911,5.265461,8.229315,-7.374902,9.669801,8.687204,0.225180,2.597545,8.537380,4.676617,-9.635881,-6.194273,-8.857587,-0.212757,0.381172,6.207808,8.909989,-9.652638,0.562548,5.022158,1.311023,-6.879467,8.716366,5.278520,-1.451933,3.793485,-9.141654,4.724445,6.957958,-6.797428,-3.999803,-8.492398,-6.823964,-7.042537,-4.068179,4.926831,0.542277,-9.384814,1.541598,7.349769,4.776093,7.198935,-2.965238,-4.615189,-6.796311,-4.682191,-0.938133,-0.020867,7.677441,-4.177825,4.633771,0.849696,9.851168,2.950271,7.745066,9.707177,3.010236,6.611010,7.180941,1.033958,-2.907072,-0.057850,3.404582,-2.359917,-2.231118,-1.417425,-8.059814,-3.692164,2.960262,-2.558721,-1.445420,6.799455,-6.758897,4.460216,-7.442615,-5.050240,2.157046,4.044852,5.382944,8.246763,9.776286,1.800484,-9.262011,8.716744,-0.982439,-3.795372,4.561636,-1.639295,-7.974909,6.239491,0.706820,-3.383203,8.194450,4.498754,4.615455,-3.175912,-3.099678,-3.957421,6.634701,-5.036934,6.340744,-7.680279,1.783913,7.634911,-8.366039,-8.510496,-3.629656], dtype = "float64")#candidate|1341|(140,)|const|float64
call_1339 = relay.TupleGetItem(func_1110_call(relay.reshape(var_1340.astype('int64'), []), relay.reshape(const_1341.astype('float64'), [1, 140]), ), 1)
call_1342 = relay.TupleGetItem(func_1113_call(relay.reshape(var_1340.astype('int64'), []), relay.reshape(const_1341.astype('float64'), [1, 140]), ), 1)
func_1110_call = mod.get_global_var('func_1110')
func_1113_call = mutated_mod.get_global_var('func_1113')
call_1349 = relay.TupleGetItem(func_1110_call(relay.reshape(var_1340.astype('int64'), []), relay.reshape(const_1341.astype('float64'), [1, 140]), ), 1)
call_1350 = relay.TupleGetItem(func_1113_call(relay.reshape(var_1340.astype('int64'), []), relay.reshape(const_1341.astype('float64'), [1, 140]), ), 1)
func_896_call = mod.get_global_var('func_896')
func_899_call = mutated_mod.get_global_var('func_899')
var_1354 = relay.var("var_1354", dtype = "int32", shape = (56,))#candidate|1354|(56,)|var|int32
call_1353 = relay.TupleGetItem(func_896_call(relay.reshape(var_1354.astype('int32'), [7, 2, 4]), relay.reshape(var_1354.astype('int32'), [7, 2, 4]), ), 2)
call_1355 = relay.TupleGetItem(func_899_call(relay.reshape(var_1354.astype('int32'), [7, 2, 4]), relay.reshape(var_1354.astype('int32'), [7, 2, 4]), ), 2)
output = relay.Tuple([bop_1334,call_1339,var_1340,const_1341,call_1349,call_1353,var_1354,])
output2 = relay.Tuple([bop_1334,call_1342,var_1340,const_1341,call_1350,call_1355,var_1354,])
func_1360 = relay.Function([var_1328,var_1340,var_1354,], output)
mod['func_1360'] = func_1360
mod = relay.transform.InferType()(mod)
var_1361 = relay.var("var_1361", dtype = "float32", shape = (1, 4, 3))#candidate|1361|(1, 4, 3)|var|float32
var_1362 = relay.var("var_1362", dtype = "int64", shape = ())#candidate|1362|()|var|int64
var_1363 = relay.var("var_1363", dtype = "int32", shape = (56,))#candidate|1363|(56,)|var|int32
output = func_1360(var_1361,var_1362,var_1363,)
func_1364 = relay.Function([var_1361,var_1362,var_1363,], output)
mutated_mod['func_1364'] = func_1364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_751_call = mod.get_global_var('func_751')
func_752_call = mutated_mod.get_global_var('func_752')
call_1387 = relay.TupleGetItem(func_751_call(), 1)
call_1388 = relay.TupleGetItem(func_752_call(), 1)
output = call_1387
output2 = call_1388
func_1401 = relay.Function([], output)
mod['func_1401'] = func_1401
mod = relay.transform.InferType()(mod)
output = func_1401()
func_1402 = relay.Function([], output)
mutated_mod['func_1402'] = func_1402
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1308_call = mod.get_global_var('func_1308')
func_1310_call = mutated_mod.get_global_var('func_1310')
call_1436 = func_1308_call()
call_1437 = func_1308_call()
func_896_call = mod.get_global_var('func_896')
func_899_call = mutated_mod.get_global_var('func_899')
const_1447 = relay.const([10,2,-2,-10,-1,-10,-9,10,-9,1,10,-1,10,8,-4,1,-4,-8,7,5,-8,-2,-8,-8,-7,-8,-7,-9,2,6,-8,-10,10,-3,9,7,-3,-2,-1,9,-1,6,8,6,5,-6,9,-9,5,7,10,-9,3,3,4,-4], dtype = "int32")#candidate|1447|(56,)|const|int32
call_1446 = relay.TupleGetItem(func_896_call(relay.reshape(const_1447.astype('int32'), [7, 2, 4]), relay.reshape(const_1447.astype('int32'), [7, 2, 4]), ), 3)
call_1448 = relay.TupleGetItem(func_899_call(relay.reshape(const_1447.astype('int32'), [7, 2, 4]), relay.reshape(const_1447.astype('int32'), [7, 2, 4]), ), 3)
func_971_call = mod.get_global_var('func_971')
func_973_call = mutated_mod.get_global_var('func_973')
call_1464 = relay.TupleGetItem(func_971_call(), 0)
call_1465 = relay.TupleGetItem(func_973_call(), 0)
output = relay.Tuple([call_1436,call_1446,const_1447,call_1464,])
output2 = relay.Tuple([call_1437,call_1448,const_1447,call_1465,])
func_1468 = relay.Function([], output)
mod['func_1468'] = func_1468
mod = relay.transform.InferType()(mod)
mutated_mod['func_1468'] = func_1468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1468_call = mutated_mod.get_global_var('func_1468')
call_1469 = func_1468_call()
output = call_1469
func_1470 = relay.Function([], output)
mutated_mod['func_1470'] = func_1470
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1136_call = mod.get_global_var('func_1136')
func_1137_call = mutated_mod.get_global_var('func_1137')
call_1476 = func_1136_call()
call_1477 = func_1136_call()
output = call_1476
output2 = call_1477
func_1488 = relay.Function([], output)
mod['func_1488'] = func_1488
mod = relay.transform.InferType()(mod)
output = func_1488()
func_1489 = relay.Function([], output)
mutated_mod['func_1489'] = func_1489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_668_call = mod.get_global_var('func_668')
func_669_call = mutated_mod.get_global_var('func_669')
call_1560 = func_668_call()
call_1561 = func_668_call()
output = relay.Tuple([call_1560,])
output2 = relay.Tuple([call_1561,])
func_1569 = relay.Function([], output)
mod['func_1569'] = func_1569
mod = relay.transform.InferType()(mod)
mutated_mod['func_1569'] = func_1569
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1569_call = mutated_mod.get_global_var('func_1569')
call_1570 = func_1569_call()
output = call_1570
func_1571 = relay.Function([], output)
mutated_mod['func_1571'] = func_1571
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1611 = relay.var("var_1611", dtype = "uint32", shape = (5, 7, 9))#candidate|1611|(5, 7, 9)|var|uint32
const_1612 = relay.const([[[3,-6,2,-9,8,3,4,-1,-3],[1,-3,-1,-3,-5,-3,8,5,-1],[5,10,-8,9,6,-5,8,-8,-5],[8,-2,-8,-1,10,-2,3,-1,-3],[9,-8,-5,-2,9,5,-3,-3,5],[-7,-10,10,-8,-1,9,5,-7,3],[-8,-6,6,-2,-4,3,8,4,7]],[[-2,-9,3,1,8,-10,2,5,-6],[7,10,-5,-1,-3,3,-8,-4,-1],[5,-4,10,3,4,9,-8,8,-10],[-1,7,3,-3,-6,8,-5,-9,-7],[4,10,7,-8,8,5,10,-8,-1],[9,-5,-2,-2,7,5,-10,-5,5],[-2,9,10,9,-9,8,-1,5,-2]],[[9,1,5,2,-4,-8,3,3,-9],[5,4,-6,-5,1,-2,-4,-9,9],[-2,9,-1,5,6,-5,1,-4,3],[9,-10,-5,-5,5,5,-8,-6,3],[4,9,-5,7,-4,3,3,-5,-6],[5,-1,-3,-4,-5,10,6,-5,-5],[9,8,-5,1,5,-2,8,2,10]],[[6,-8,4,7,1,-7,4,-10,-1],[3,4,-10,9,-6,7,-6,-9,4],[-10,5,4,-10,10,-9,5,-5,-10],[-5,-10,9,6,10,8,9,4,-3],[-6,5,3,6,-5,-8,3,3,-6],[-3,-6,10,-7,-5,-2,9,1,3],[9,-5,10,1,-9,-1,5,-9,-6]],[[-8,-7,4,-1,-9,-7,10,6,2],[9,1,8,-4,5,5,-2,4,5],[-1,1,1,-4,5,6,-6,-3,-2],[-9,3,10,5,10,-3,9,3,6],[9,-7,-2,4,-10,6,-5,10,1],[7,-4,-7,-3,-3,-6,2,-10,10],[4,1,10,-5,2,-4,-5,-9,7]]], dtype = "uint32")#candidate|1612|(5, 7, 9)|const|uint32
bop_1613 = relay.logical_xor(var_1611.astype('uint32'), relay.reshape(const_1612.astype('uint32'), relay.shape_of(var_1611))) # shape=(5, 7, 9)
uop_1617 = relay.acosh(var_1611.astype('float32')) # shape=(5, 7, 9)
func_751_call = mod.get_global_var('func_751')
func_752_call = mutated_mod.get_global_var('func_752')
call_1625 = relay.TupleGetItem(func_751_call(), 0)
call_1626 = relay.TupleGetItem(func_752_call(), 0)
func_1360_call = mod.get_global_var('func_1360')
func_1364_call = mutated_mod.get_global_var('func_1364')
var_1637 = relay.var("var_1637", dtype = "float32", shape = (12,))#candidate|1637|(12,)|var|float32
const_1638 = relay.const(3, dtype = "int64")#candidate|1638|()|const|int64
var_1639 = relay.var("var_1639", dtype = "int32", shape = (56,))#candidate|1639|(56,)|var|int32
call_1636 = relay.TupleGetItem(func_1360_call(relay.reshape(var_1637.astype('float32'), [1, 4, 3]), relay.reshape(const_1638.astype('int64'), []), relay.reshape(var_1639.astype('int32'), [56,]), ), 1)
call_1640 = relay.TupleGetItem(func_1364_call(relay.reshape(var_1637.astype('float32'), [1, 4, 3]), relay.reshape(const_1638.astype('int64'), []), relay.reshape(var_1639.astype('int32'), [56,]), ), 1)
uop_1643 = relay.acos(const_1612.astype('float32')) # shape=(5, 7, 9)
output = relay.Tuple([bop_1613,uop_1617,call_1625,call_1636,var_1637,const_1638,var_1639,uop_1643,])
output2 = relay.Tuple([bop_1613,uop_1617,call_1626,call_1640,var_1637,const_1638,var_1639,uop_1643,])
func_1653 = relay.Function([var_1611,var_1637,var_1639,], output)
mod['func_1653'] = func_1653
mod = relay.transform.InferType()(mod)
var_1654 = relay.var("var_1654", dtype = "uint32", shape = (5, 7, 9))#candidate|1654|(5, 7, 9)|var|uint32
var_1655 = relay.var("var_1655", dtype = "float32", shape = (12,))#candidate|1655|(12,)|var|float32
var_1656 = relay.var("var_1656", dtype = "int32", shape = (56,))#candidate|1656|(56,)|var|int32
output = func_1653(var_1654,var_1655,var_1656,)
func_1657 = relay.Function([var_1654,var_1655,var_1656,], output)
mutated_mod['func_1657'] = func_1657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1468_call = mod.get_global_var('func_1468')
func_1470_call = mutated_mod.get_global_var('func_1470')
call_1710 = relay.TupleGetItem(func_1468_call(), 1)
call_1711 = relay.TupleGetItem(func_1470_call(), 1)
output = call_1710
output2 = call_1711
func_1717 = relay.Function([], output)
mod['func_1717'] = func_1717
mod = relay.transform.InferType()(mod)
output = func_1717()
func_1718 = relay.Function([], output)
mutated_mod['func_1718'] = func_1718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1717_call = mod.get_global_var('func_1717')
func_1718_call = mutated_mod.get_global_var('func_1718')
call_1721 = func_1717_call()
call_1722 = func_1717_call()
func_1468_call = mod.get_global_var('func_1468')
func_1470_call = mutated_mod.get_global_var('func_1470')
call_1729 = relay.TupleGetItem(func_1468_call(), 2)
call_1730 = relay.TupleGetItem(func_1470_call(), 2)
func_1569_call = mod.get_global_var('func_1569')
func_1571_call = mutated_mod.get_global_var('func_1571')
call_1737 = relay.TupleGetItem(func_1569_call(), 0)
call_1738 = relay.TupleGetItem(func_1571_call(), 0)
func_1569_call = mod.get_global_var('func_1569')
func_1571_call = mutated_mod.get_global_var('func_1571')
call_1740 = relay.TupleGetItem(func_1569_call(), 0)
call_1741 = relay.TupleGetItem(func_1571_call(), 0)
output = relay.Tuple([call_1721,call_1729,call_1737,call_1740,])
output2 = relay.Tuple([call_1722,call_1730,call_1738,call_1741,])
func_1754 = relay.Function([], output)
mod['func_1754'] = func_1754
mod = relay.transform.InferType()(mod)
mutated_mod['func_1754'] = func_1754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1754_call = mutated_mod.get_global_var('func_1754')
call_1755 = func_1754_call()
output = call_1755
func_1756 = relay.Function([], output)
mutated_mod['func_1756'] = func_1756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1569_call = mod.get_global_var('func_1569')
func_1571_call = mutated_mod.get_global_var('func_1571')
call_1774 = relay.TupleGetItem(func_1569_call(), 0)
call_1775 = relay.TupleGetItem(func_1571_call(), 0)
func_751_call = mod.get_global_var('func_751')
func_752_call = mutated_mod.get_global_var('func_752')
call_1785 = relay.TupleGetItem(func_751_call(), 1)
call_1786 = relay.TupleGetItem(func_752_call(), 1)
func_1110_call = mod.get_global_var('func_1110')
func_1113_call = mutated_mod.get_global_var('func_1113')
const_1835 = relay.const(-7, dtype = "int64")#candidate|1835|()|const|int64
call_1834 = relay.TupleGetItem(func_1110_call(relay.reshape(const_1835.astype('int64'), []), relay.reshape(call_1774.astype('float64'), [1, 140]), ), 3)
call_1836 = relay.TupleGetItem(func_1113_call(relay.reshape(const_1835.astype('int64'), []), relay.reshape(call_1774.astype('float64'), [1, 140]), ), 3)
func_1488_call = mod.get_global_var('func_1488')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_1839 = func_1488_call()
call_1840 = func_1488_call()
output = relay.Tuple([call_1774,call_1785,call_1834,const_1835,call_1839,])
output2 = relay.Tuple([call_1775,call_1786,call_1836,const_1835,call_1840,])
func_1862 = relay.Function([], output)
mod['func_1862'] = func_1862
mod = relay.transform.InferType()(mod)
mutated_mod['func_1862'] = func_1862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1862_call = mutated_mod.get_global_var('func_1862')
call_1863 = func_1862_call()
output = call_1863
func_1864 = relay.Function([], output)
mutated_mod['func_1864'] = func_1864
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1308_call = mod.get_global_var('func_1308')
func_1310_call = mutated_mod.get_global_var('func_1310')
call_1890 = func_1308_call()
call_1891 = func_1308_call()
func_668_call = mod.get_global_var('func_668')
func_669_call = mutated_mod.get_global_var('func_669')
call_1892 = func_668_call()
call_1893 = func_668_call()
output = relay.Tuple([call_1890,call_1892,])
output2 = relay.Tuple([call_1891,call_1893,])
func_1896 = relay.Function([], output)
mod['func_1896'] = func_1896
mod = relay.transform.InferType()(mod)
mutated_mod['func_1896'] = func_1896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1896_call = mutated_mod.get_global_var('func_1896')
call_1897 = func_1896_call()
output = call_1897
func_1898 = relay.Function([], output)
mutated_mod['func_1898'] = func_1898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_935_call = mod.get_global_var('func_935')
func_936_call = mutated_mod.get_global_var('func_936')
call_1934 = func_935_call()
call_1935 = func_935_call()
output = call_1934
output2 = call_1935
func_1938 = relay.Function([], output)
mod['func_1938'] = func_1938
mod = relay.transform.InferType()(mod)
mutated_mod['func_1938'] = func_1938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1938_call = mutated_mod.get_global_var('func_1938')
call_1939 = func_1938_call()
output = call_1939
func_1940 = relay.Function([], output)
mutated_mod['func_1940'] = func_1940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1308_call = mod.get_global_var('func_1308')
func_1310_call = mutated_mod.get_global_var('func_1310')
call_2032 = func_1308_call()
call_2033 = func_1308_call()
output = relay.Tuple([call_2032,])
output2 = relay.Tuple([call_2033,])
func_2059 = relay.Function([], output)
mod['func_2059'] = func_2059
mod = relay.transform.InferType()(mod)
mutated_mod['func_2059'] = func_2059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2059_call = mutated_mod.get_global_var('func_2059')
call_2060 = func_2059_call()
output = call_2060
func_2061 = relay.Function([], output)
mutated_mod['func_2061'] = func_2061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1717_call = mod.get_global_var('func_1717')
func_1718_call = mutated_mod.get_global_var('func_1718')
call_2145 = func_1717_call()
call_2146 = func_1717_call()
func_1027_call = mod.get_global_var('func_1027')
func_1030_call = mutated_mod.get_global_var('func_1030')
call_2159 = relay.TupleGetItem(func_1027_call(relay.reshape(call_2145.astype('float64'), [10, 7, 2])), 1)
call_2160 = relay.TupleGetItem(func_1030_call(relay.reshape(call_2145.astype('float64'), [10, 7, 2])), 1)
func_896_call = mod.get_global_var('func_896')
func_899_call = mutated_mod.get_global_var('func_899')
var_2162 = relay.var("var_2162", dtype = "int32", shape = (56,))#candidate|2162|(56,)|var|int32
call_2161 = relay.TupleGetItem(func_896_call(relay.reshape(var_2162.astype('int32'), [7, 2, 4]), relay.reshape(var_2162.astype('int32'), [7, 2, 4]), ), 0)
call_2163 = relay.TupleGetItem(func_899_call(relay.reshape(var_2162.astype('int32'), [7, 2, 4]), relay.reshape(var_2162.astype('int32'), [7, 2, 4]), ), 0)
func_827_call = mod.get_global_var('func_827')
func_829_call = mutated_mod.get_global_var('func_829')
call_2180 = relay.TupleGetItem(func_827_call(), 1)
call_2181 = relay.TupleGetItem(func_829_call(), 1)
func_1754_call = mod.get_global_var('func_1754')
func_1756_call = mutated_mod.get_global_var('func_1756')
call_2182 = relay.TupleGetItem(func_1754_call(), 3)
call_2183 = relay.TupleGetItem(func_1756_call(), 3)
uop_2185 = relay.sin(call_2161.astype('float32')) # shape=(7, 2, 4)
uop_2187 = relay.sin(call_2163.astype('float32')) # shape=(7, 2, 4)
output = relay.Tuple([call_2145,call_2159,var_2162,call_2180,call_2182,uop_2185,])
output2 = relay.Tuple([call_2146,call_2160,var_2162,call_2181,call_2183,uop_2187,])
func_2191 = relay.Function([var_2162,], output)
mod['func_2191'] = func_2191
mod = relay.transform.InferType()(mod)
var_2192 = relay.var("var_2192", dtype = "int32", shape = (56,))#candidate|2192|(56,)|var|int32
output = func_2191(var_2192)
func_2193 = relay.Function([var_2192], output)
mutated_mod['func_2193'] = func_2193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_827_call = mod.get_global_var('func_827')
func_829_call = mutated_mod.get_global_var('func_829')
call_2216 = relay.TupleGetItem(func_827_call(), 0)
call_2217 = relay.TupleGetItem(func_829_call(), 0)
uop_2219 = relay.asin(call_2216.astype('float32')) # shape=(10, 7, 2)
uop_2221 = relay.asin(call_2217.astype('float32')) # shape=(10, 7, 2)
func_827_call = mod.get_global_var('func_827')
func_829_call = mutated_mod.get_global_var('func_829')
call_2228 = relay.TupleGetItem(func_827_call(), 0)
call_2229 = relay.TupleGetItem(func_829_call(), 0)
output = relay.Tuple([uop_2219,call_2228,])
output2 = relay.Tuple([uop_2221,call_2229,])
func_2237 = relay.Function([], output)
mod['func_2237'] = func_2237
mod = relay.transform.InferType()(mod)
mutated_mod['func_2237'] = func_2237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2237_call = mutated_mod.get_global_var('func_2237')
call_2238 = func_2237_call()
output = call_2238
func_2239 = relay.Function([], output)
mutated_mod['func_2239'] = func_2239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1938_call = mod.get_global_var('func_1938')
func_1940_call = mutated_mod.get_global_var('func_1940')
call_2316 = func_1938_call()
call_2317 = func_1938_call()
func_1754_call = mod.get_global_var('func_1754')
func_1756_call = mutated_mod.get_global_var('func_1756')
call_2348 = relay.TupleGetItem(func_1754_call(), 0)
call_2349 = relay.TupleGetItem(func_1756_call(), 0)
func_1754_call = mod.get_global_var('func_1754')
func_1756_call = mutated_mod.get_global_var('func_1756')
call_2366 = relay.TupleGetItem(func_1754_call(), 0)
call_2367 = relay.TupleGetItem(func_1756_call(), 0)
output = relay.Tuple([call_2316,call_2348,call_2366,])
output2 = relay.Tuple([call_2317,call_2349,call_2367,])
func_2376 = relay.Function([], output)
mod['func_2376'] = func_2376
mod = relay.transform.InferType()(mod)
output = func_2376()
func_2377 = relay.Function([], output)
mutated_mod['func_2377'] = func_2377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2237_call = mod.get_global_var('func_2237')
func_2239_call = mutated_mod.get_global_var('func_2239')
call_2413 = relay.TupleGetItem(func_2237_call(), 0)
call_2414 = relay.TupleGetItem(func_2239_call(), 0)
output = call_2413
output2 = call_2414
func_2428 = relay.Function([], output)
mod['func_2428'] = func_2428
mod = relay.transform.InferType()(mod)
mutated_mod['func_2428'] = func_2428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2428_call = mutated_mod.get_global_var('func_2428')
call_2429 = func_2428_call()
output = call_2429
func_2430 = relay.Function([], output)
mutated_mod['func_2430'] = func_2430
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2489 = relay.var("var_2489", dtype = "float64", shape = (5, 14, 7))#candidate|2489|(5, 14, 7)|var|float64
uop_2490 = relay.atan(var_2489.astype('float64')) # shape=(5, 14, 7)
func_1468_call = mod.get_global_var('func_1468')
func_1470_call = mutated_mod.get_global_var('func_1470')
call_2499 = relay.TupleGetItem(func_1468_call(), 0)
call_2500 = relay.TupleGetItem(func_1470_call(), 0)
const_2502 = relay.const([[[2.510356,9.028319,4.692325,8.834995,9.424211,8.862436,8.127711],[1.192429,5.755036,-1.235827,-6.479739,6.218709,4.639944,-7.338003],[-2.475929,7.647400,-2.587326,-1.339678,9.417597,-0.677307,4.918574],[1.651651,-6.425722,7.175574,2.524997,-6.826796,-7.475128,4.203513],[5.427200,4.516363,1.617903,2.511131,3.150102,4.140916,8.030785],[5.034096,0.929981,4.494870,-1.934339,-3.594277,-1.989667,4.686863],[-2.501070,2.939002,-6.554468,-1.567294,1.186657,4.207648,1.679344],[-1.288009,4.367222,4.894611,-9.105106,-7.308736,0.116892,6.008621],[0.634213,-6.850354,2.252063,7.287115,4.658728,7.865450,7.809892],[9.746345,-4.466865,-8.552666,-6.275543,-1.627323,-1.907963,0.542611],[3.401612,-7.562680,7.721931,5.280380,-4.740908,-8.074608,-2.199393],[-2.333562,-3.573823,-0.076051,4.057841,-3.194974,-8.109902,4.115508],[-7.506778,-7.230222,4.319219,-3.089317,-7.366072,4.988992,3.354300],[-1.012324,0.746319,4.582846,-2.946202,-0.590404,-6.159098,8.248486]],[[-0.732851,-5.853548,3.469717,-0.012144,7.393047,4.448899,-4.787173],[-5.672296,-0.243558,7.757557,4.711803,-8.329876,-5.502731,-8.572114],[0.755373,6.108221,-1.932258,-9.090385,1.028554,-7.991385,-9.575674],[-8.165719,-0.825544,-3.539872,7.525424,-2.060465,-7.910452,-7.435914],[-3.566378,-8.798517,5.840422,2.701370,5.931938,2.677515,-0.550181],[3.060244,-1.987331,-7.875154,-4.144243,1.277817,-9.463828,-8.478281],[-2.653908,-1.073527,1.507706,7.300307,-9.708967,-0.921364,-0.291517],[-3.591412,5.585378,5.740844,6.707217,-3.045866,-4.590942,7.454435],[-9.090467,-2.900721,9.969693,1.113357,6.002722,3.437603,4.847684],[3.598648,2.000314,-5.365953,3.427111,-7.795533,8.843950,-7.053000],[5.936001,3.096524,8.531340,-5.961381,-3.364859,-2.324785,-7.748954],[7.712939,9.150775,-1.787616,8.526786,-1.376968,-7.635907,7.148880],[2.119030,-3.897645,-1.484755,-8.493249,5.783185,-3.739815,-5.244492],[1.791658,-9.945936,-6.959514,1.724763,-3.473175,-7.270147,2.258226]],[[-6.993186,-9.791415,-0.056313,-8.434482,-7.080077,-7.121657,8.174725],[3.812269,9.617971,6.643109,-3.222774,-0.608945,-8.372538,-7.416372],[7.052319,8.084242,-2.427443,4.127567,-9.727943,7.018735,7.006826],[-5.694967,-9.101517,-2.822798,-5.214960,4.452812,-3.248536,-3.906697],[6.489605,7.484593,-6.283137,-6.960160,-4.034410,5.446363,6.347782],[-1.181469,4.673458,0.981350,-7.074856,7.931475,1.194393,1.457307],[-5.560057,-5.445962,-3.219071,-1.573227,9.778087,-0.468495,9.499123],[-3.435250,-3.166360,8.908004,-9.103559,-2.353637,-0.328795,2.569883],[-8.503407,5.225133,4.347059,-3.096131,3.824569,-6.899006,9.612361],[4.005449,1.429618,5.138678,-5.077799,7.012556,-1.711732,4.973283],[2.201586,-5.467265,-3.247459,2.230150,-6.110916,3.578664,-0.825851],[-7.330366,-4.724474,-4.736467,7.814889,-7.685866,-6.512109,-3.672610],[8.060035,-0.354735,4.455676,-2.799597,-7.764326,2.273473,-1.666614],[6.853520,-8.191138,-4.993443,4.410962,-1.521618,3.998783,-5.990440]],[[-7.070950,-8.049586,-7.515172,4.989832,4.238639,6.890568,7.310743],[-5.290432,-3.451370,-5.613993,6.263999,9.151315,-3.970386,-6.105336],[-2.626988,0.418047,2.464469,-3.236076,-3.215478,1.419808,-4.239350],[-8.109404,3.485710,7.332105,-8.487238,0.551531,-2.145692,-1.913404],[-1.041365,-2.206821,9.983081,-6.733981,7.391358,-6.208995,-7.466490],[-3.028305,6.557511,-0.197098,8.689267,-2.338440,4.368107,-7.912912],[-6.324391,-5.349510,6.913483,-9.013860,0.012899,4.520219,6.958538],[-3.246886,-2.024015,-3.807301,6.961487,-7.959110,-1.304246,-4.961410],[-2.906433,-9.059128,3.897986,-7.680801,2.653974,3.992180,3.594082],[-7.745547,7.222934,-9.125650,6.152688,5.782068,1.155346,9.508658],[-2.785927,2.920975,-5.363741,8.794448,3.400038,-4.893868,-5.943553],[1.549120,4.557229,0.685787,-2.199508,-2.846308,-3.332201,9.424282],[4.086291,-0.544415,-6.779443,2.617260,6.354111,8.202135,-8.620086],[3.531615,6.627823,-7.628348,-0.220177,5.084544,5.043236,-1.038396]],[[2.464771,1.518728,0.686472,-8.421133,0.155374,-4.698358,4.811319],[8.683549,-3.345433,-3.344858,8.718949,-5.106410,-2.461755,7.490907],[1.134398,-3.900247,2.239352,7.055961,2.754825,-3.085450,0.708575],[4.892160,-2.800207,-7.968565,3.466462,7.465921,1.961377,0.270518],[9.494171,5.400049,-5.621219,-5.154372,9.577412,-1.058683,8.091396],[-3.922217,-3.810795,0.238584,-2.711355,5.696700,8.282772,1.851087],[-3.965545,-9.232629,1.252270,-2.627197,0.475893,9.285958,-9.579532],[2.600432,-9.468669,9.307052,2.187266,-3.415812,-6.728999,-1.795059],[-2.572931,1.668099,-7.022064,-2.941283,4.565092,9.586759,5.081091],[-1.382678,0.304234,-7.771589,6.728204,-2.452961,-2.781805,-1.935957],[-5.770044,-9.441432,-3.181569,8.602232,-1.199973,-8.042971,-8.844472],[-3.624231,-9.243952,1.916063,8.534981,-8.039398,5.798393,4.901436],[1.411116,4.277936,-8.899962,-1.066808,1.447332,6.948872,5.831447],[1.877786,-4.010370,-1.984224,-7.864963,-2.443348,9.739200,-0.777009]]], dtype = "float64")#candidate|2502|(5, 14, 7)|const|float64
bop_2503 = relay.bitwise_or(uop_2490.astype('int16'), relay.reshape(const_2502.astype('int16'), relay.shape_of(uop_2490))) # shape=(5, 14, 7)
output = relay.Tuple([call_2499,bop_2503,])
output2 = relay.Tuple([call_2500,bop_2503,])
func_2508 = relay.Function([var_2489,], output)
mod['func_2508'] = func_2508
mod = relay.transform.InferType()(mod)
var_2509 = relay.var("var_2509", dtype = "float64", shape = (5, 14, 7))#candidate|2509|(5, 14, 7)|var|float64
output = func_2508(var_2509)
func_2510 = relay.Function([var_2509], output)
mutated_mod['func_2510'] = func_2510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1255_call = mod.get_global_var('func_1255')
func_1256_call = mutated_mod.get_global_var('func_1256')
call_2518 = relay.TupleGetItem(func_1255_call(), 2)
call_2519 = relay.TupleGetItem(func_1256_call(), 2)
output = call_2518
output2 = call_2519
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
var_2548 = relay.var("var_2548", dtype = "int64", shape = (5, 14, 13))#candidate|2548|(5, 14, 13)|var|int64
var_2549 = relay.var("var_2549", dtype = "int64", shape = (5, 14, 13))#candidate|2549|(5, 14, 13)|var|int64
bop_2550 = relay.logical_xor(var_2548.astype('int64'), relay.reshape(var_2549.astype('int64'), relay.shape_of(var_2548))) # shape=(5, 14, 13)
output = bop_2550
output2 = bop_2550
func_2556 = relay.Function([var_2548,var_2549,], output)
mod['func_2556'] = func_2556
mod = relay.transform.InferType()(mod)
var_2557 = relay.var("var_2557", dtype = "int64", shape = (5, 14, 13))#candidate|2557|(5, 14, 13)|var|int64
var_2558 = relay.var("var_2558", dtype = "int64", shape = (5, 14, 13))#candidate|2558|(5, 14, 13)|var|int64
output = func_2556(var_2557,var_2558,)
func_2559 = relay.Function([var_2557,var_2558,], output)
mutated_mod['func_2559'] = func_2559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1468_call = mod.get_global_var('func_1468')
func_1470_call = mutated_mod.get_global_var('func_1470')
call_2598 = relay.TupleGetItem(func_1468_call(), 0)
call_2599 = relay.TupleGetItem(func_1470_call(), 0)
func_2523_call = mod.get_global_var('func_2523')
func_2525_call = mutated_mod.get_global_var('func_2525')
call_2612 = func_2523_call()
call_2613 = func_2523_call()
func_1569_call = mod.get_global_var('func_1569')
func_1571_call = mutated_mod.get_global_var('func_1571')
call_2621 = relay.TupleGetItem(func_1569_call(), 0)
call_2622 = relay.TupleGetItem(func_1571_call(), 0)
func_1468_call = mod.get_global_var('func_1468')
func_1470_call = mutated_mod.get_global_var('func_1470')
call_2629 = relay.TupleGetItem(func_1468_call(), 2)
call_2630 = relay.TupleGetItem(func_1470_call(), 2)
func_1360_call = mod.get_global_var('func_1360')
func_1364_call = mutated_mod.get_global_var('func_1364')
var_2636 = relay.var("var_2636", dtype = "float32", shape = (12,))#candidate|2636|(12,)|var|float32
var_2637 = relay.var("var_2637", dtype = "int64", shape = ())#candidate|2637|()|var|int64
call_2635 = relay.TupleGetItem(func_1360_call(relay.reshape(var_2636.astype('float32'), [1, 4, 3]), relay.reshape(var_2637.astype('int64'), []), relay.reshape(call_2629.astype('int32'), [56,]), ), 4)
call_2638 = relay.TupleGetItem(func_1364_call(relay.reshape(var_2636.astype('float32'), [1, 4, 3]), relay.reshape(var_2637.astype('int64'), []), relay.reshape(call_2629.astype('int32'), [56,]), ), 4)
func_1862_call = mod.get_global_var('func_1862')
func_1864_call = mutated_mod.get_global_var('func_1864')
call_2678 = relay.TupleGetItem(func_1862_call(), 3)
call_2679 = relay.TupleGetItem(func_1864_call(), 3)
output = relay.Tuple([call_2598,call_2612,call_2621,call_2629,call_2635,var_2636,var_2637,call_2678,])
output2 = relay.Tuple([call_2599,call_2613,call_2622,call_2630,call_2638,var_2636,var_2637,call_2679,])
func_2680 = relay.Function([var_2636,var_2637,], output)
mod['func_2680'] = func_2680
mod = relay.transform.InferType()(mod)
var_2681 = relay.var("var_2681", dtype = "float32", shape = (12,))#candidate|2681|(12,)|var|float32
var_2682 = relay.var("var_2682", dtype = "int64", shape = ())#candidate|2682|()|var|int64
output = func_2680(var_2681,var_2682,)
func_2683 = relay.Function([var_2681,var_2682,], output)
mutated_mod['func_2683'] = func_2683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1488_call = mod.get_global_var('func_1488')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_2730 = func_1488_call()
call_2731 = func_1488_call()
func_2508_call = mod.get_global_var('func_2508')
func_2510_call = mutated_mod.get_global_var('func_2510')
const_2752 = relay.const([[-5.426324,-7.855017,8.484514,7.544884,-0.408393,4.788812,6.173616,2.121522,5.327369,7.428356],[6.664511,0.358664,-5.497731,-9.222000,-3.180750,-0.886203,-6.238119,1.857412,-1.816536,-5.842675],[4.543686,7.582865,-3.982160,-8.453491,8.183610,-3.123233,-8.399706,6.856733,-6.298570,5.179881],[2.146391,-9.593004,-1.925488,1.472960,-6.005658,-6.543388,6.547301,-5.807740,-6.043487,-9.054959],[8.772480,-6.708308,-7.400578,-0.357237,9.405007,1.416083,0.932767,-6.109117,-2.648574,9.586755],[1.542363,-1.296326,7.536027,-7.041598,1.162278,-6.037853,0.859255,-8.122578,-6.017585,6.805704],[0.178556,-4.145364,-0.067357,-9.042087,-3.803885,7.925519,3.553474,-2.353252,8.580976,-4.546138],[0.363023,5.675030,-4.740516,-8.402412,-9.049745,-5.285030,4.722241,-9.668855,-9.546195,-5.035412],[-3.649478,-4.023138,3.197618,9.912024,-6.405216,5.113800,-1.099987,-1.969988,-6.408148,3.914675],[-4.591468,-3.027489,-7.232593,3.500908,-1.317317,3.883978,-2.155910,-0.808701,-8.721906,-0.899985],[-3.033828,8.699315,-4.299783,8.488111,-6.365157,4.887626,-4.273283,-3.466085,-8.313039,3.826128],[6.609988,-9.524876,4.000636,9.095404,-4.489156,-2.183117,0.649610,4.604346,2.354845,1.221470],[6.383376,5.599502,-4.922264,-0.828784,2.410201,9.308510,-4.879157,-7.388917,3.703997,3.716241],[2.982472,-9.192125,6.304890,-7.034387,-8.271655,4.217161,-9.999429,8.979759,-0.426159,-3.229733],[-9.877548,5.685200,9.138428,-4.002309,1.345127,-4.041616,8.499694,-7.370388,-8.113041,1.423540],[-2.270548,-2.629728,1.958849,7.687492,5.966343,-4.818638,-9.028805,-7.414944,8.497529,-6.823564],[-5.120961,-4.271439,6.276476,5.302263,2.915531,-0.936203,1.514394,7.186830,-1.862880,-3.056320],[-2.153589,8.004776,-4.505878,-6.216339,-1.006177,6.736800,0.884408,-3.617496,-0.857972,-0.375782],[0.691900,3.109527,4.152525,0.445937,2.673175,4.289399,-0.636730,-3.494331,-4.493233,6.451475],[4.715010,8.765728,-9.633738,8.259975,5.820696,-9.146070,-9.742572,2.873342,-9.973907,-0.303934],[1.227346,0.807536,-2.889147,-3.015113,-4.732422,-6.998848,-2.406048,-2.705667,2.645094,4.750155],[7.427321,8.304061,7.177953,8.659568,-6.693746,-4.384676,1.257167,7.779897,9.418988,-6.869109],[1.206609,-7.195003,8.930141,-0.947347,-0.931489,5.459833,-1.503967,-7.822018,-4.323412,9.834442],[2.535577,-0.021699,-6.878844,-8.957546,6.246422,6.870224,8.751896,6.158004,3.768764,-5.070981],[5.859287,7.320391,-7.177832,-2.478718,-1.524212,2.470085,2.900667,-4.687592,-0.454035,8.589364],[-2.460454,-7.733242,-2.871384,-5.405363,-1.477089,-7.140640,-6.378437,1.393127,4.098639,7.313028],[9.301363,8.108120,-6.463854,-8.866606,-3.504285,7.233600,7.212546,2.104103,7.684308,7.945030],[-1.811376,4.654877,5.484456,5.921754,-2.741964,-0.307711,-6.813686,-2.615515,-0.616728,1.495822],[7.764144,4.836719,-1.906848,-1.056295,-1.179362,6.066419,6.190041,0.784227,4.826936,8.659372],[-5.223062,-0.685739,7.831246,3.778487,0.410238,8.108852,0.833314,4.832437,3.259751,3.520703],[9.585218,-1.817130,-8.435861,-0.807980,-5.909044,4.222989,0.460479,7.760992,6.875269,-2.438209],[8.455004,4.840387,-3.429777,8.702979,-9.820029,5.429113,7.494399,6.598724,-9.631012,-4.405619],[4.320367,8.779204,4.607584,-8.999659,2.049046,8.373938,-1.694788,-7.000067,-8.005536,-0.498627],[-5.346854,-9.893409,7.852057,2.560897,9.428768,-0.098339,-9.531192,-8.857730,6.687681,-0.359334],[4.595194,1.837058,-6.035096,5.368840,8.947035,1.165047,1.026751,-1.937722,5.282845,-4.173209],[3.767849,-8.702364,-2.574818,0.179712,2.716161,3.995282,3.246554,-9.888696,-3.164651,-6.959020],[1.502445,3.360640,-0.388797,8.620084,-1.934974,-9.657438,-1.271771,0.117869,0.053226,-6.379186],[-1.827830,-3.564439,9.301738,1.214205,-6.799713,7.460990,6.976568,-1.890469,-2.983616,-5.096645],[-5.214993,-0.375821,1.179603,3.660495,-5.289892,7.970233,6.964080,1.828161,-2.760009,-9.136597],[-1.750083,-0.645144,2.832109,7.274659,-2.028760,-5.311629,5.851847,4.775972,-3.253067,4.879014],[1.884999,3.324021,-2.817790,3.180419,8.995192,0.131315,4.055238,5.711094,7.536883,4.784788],[-6.085268,-7.481107,-5.220085,-9.068913,-8.715989,-3.117329,-2.033001,1.430874,-1.442493,4.602215],[-2.181900,3.509101,-8.903852,-6.160303,-7.648072,4.902763,3.368323,-7.432683,-4.142375,-7.286540],[-2.327844,-5.705991,-7.701326,-3.588564,-8.483509,-1.788532,-0.918058,-2.075208,1.417007,-9.833484],[-4.237271,-7.887004,9.749313,-7.934072,-0.020746,3.483311,5.421675,5.490708,6.208139,-5.916515],[-6.899547,-8.419577,-6.791792,4.821087,-3.127557,1.859356,-8.482910,-0.904552,-2.329563,6.833284],[-2.570778,-3.421681,-0.523471,5.206123,0.238018,0.186034,2.658076,-3.194274,-2.270789,2.373490],[-3.014731,-0.868071,-6.386059,-9.507075,0.736275,6.992552,-8.558695,2.847481,-3.015748,-5.647248],[-1.060953,4.333032,-9.614874,2.844751,6.610244,1.068654,-9.077525,-5.728713,-7.532075,3.137155]], dtype = "float64")#candidate|2752|(49, 10)|const|float64
call_2751 = relay.TupleGetItem(func_2508_call(relay.reshape(const_2752.astype('float64'), [5, 14, 7])), 1)
call_2753 = relay.TupleGetItem(func_2510_call(relay.reshape(const_2752.astype('float64'), [5, 14, 7])), 1)
uop_2760 = relay.sinh(call_2751.astype('float64')) # shape=(5, 14, 7)
uop_2762 = relay.sinh(call_2753.astype('float64')) # shape=(5, 14, 7)
output = relay.Tuple([call_2730,const_2752,uop_2760,])
output2 = relay.Tuple([call_2731,const_2752,uop_2762,])
func_2763 = relay.Function([], output)
mod['func_2763'] = func_2763
mod = relay.transform.InferType()(mod)
output = func_2763()
func_2764 = relay.Function([], output)
mutated_mod['func_2764'] = func_2764
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2796 = relay.var("var_2796", dtype = "bool", shape = (9, 1, 15))#candidate|2796|(9, 1, 15)|var|bool
var_2797 = relay.var("var_2797", dtype = "bool", shape = (9, 13, 15))#candidate|2797|(9, 13, 15)|var|bool
bop_2798 = relay.logical_and(var_2796.astype('bool'), var_2797.astype('bool')) # shape=(9, 13, 15)
output = relay.Tuple([bop_2798,])
output2 = relay.Tuple([bop_2798,])
func_2807 = relay.Function([var_2796,var_2797,], output)
mod['func_2807'] = func_2807
mod = relay.transform.InferType()(mod)
var_2808 = relay.var("var_2808", dtype = "bool", shape = (9, 1, 15))#candidate|2808|(9, 1, 15)|var|bool
var_2809 = relay.var("var_2809", dtype = "bool", shape = (9, 13, 15))#candidate|2809|(9, 13, 15)|var|bool
output = func_2807(var_2808,var_2809,)
func_2810 = relay.Function([var_2808,var_2809,], output)
mutated_mod['func_2810'] = func_2810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1938_call = mod.get_global_var('func_1938')
func_1940_call = mutated_mod.get_global_var('func_1940')
call_2815 = func_1938_call()
call_2816 = func_1938_call()
output = relay.Tuple([call_2815,])
output2 = relay.Tuple([call_2816,])
func_2817 = relay.Function([], output)
mod['func_2817'] = func_2817
mod = relay.transform.InferType()(mod)
mutated_mod['func_2817'] = func_2817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2817_call = mutated_mod.get_global_var('func_2817')
call_2818 = func_2817_call()
output = call_2818
func_2819 = relay.Function([], output)
mutated_mod['func_2819'] = func_2819
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2763_call = mod.get_global_var('func_2763')
func_2764_call = mutated_mod.get_global_var('func_2764')
call_2847 = relay.TupleGetItem(func_2763_call(), 0)
call_2848 = relay.TupleGetItem(func_2764_call(), 0)
func_2191_call = mod.get_global_var('func_2191')
func_2193_call = mutated_mod.get_global_var('func_2193')
var_2857 = relay.var("var_2857", dtype = "int32", shape = (56,))#candidate|2857|(56,)|var|int32
call_2856 = relay.TupleGetItem(func_2191_call(relay.reshape(var_2857.astype('int32'), [56,])), 1)
call_2858 = relay.TupleGetItem(func_2193_call(relay.reshape(var_2857.astype('int32'), [56,])), 1)
func_2817_call = mod.get_global_var('func_2817')
func_2819_call = mutated_mod.get_global_var('func_2819')
call_2863 = relay.TupleGetItem(func_2817_call(), 0)
call_2864 = relay.TupleGetItem(func_2819_call(), 0)
output = relay.Tuple([call_2847,call_2856,var_2857,call_2863,])
output2 = relay.Tuple([call_2848,call_2858,var_2857,call_2864,])
func_2869 = relay.Function([var_2857,], output)
mod['func_2869'] = func_2869
mod = relay.transform.InferType()(mod)
var_2870 = relay.var("var_2870", dtype = "int32", shape = (56,))#candidate|2870|(56,)|var|int32
output = func_2869(var_2870)
func_2871 = relay.Function([var_2870], output)
mutated_mod['func_2871'] = func_2871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1896_call = mod.get_global_var('func_1896')
func_1898_call = mutated_mod.get_global_var('func_1898')
call_3009 = relay.TupleGetItem(func_1896_call(), 0)
call_3010 = relay.TupleGetItem(func_1898_call(), 0)
func_1110_call = mod.get_global_var('func_1110')
func_1113_call = mutated_mod.get_global_var('func_1113')
var_3020 = relay.var("var_3020", dtype = "int64", shape = ())#candidate|3020|()|var|int64
call_3019 = relay.TupleGetItem(func_1110_call(relay.reshape(var_3020.astype('int64'), []), relay.reshape(call_3009.astype('float64'), [1, 140]), ), 2)
call_3021 = relay.TupleGetItem(func_1113_call(relay.reshape(var_3020.astype('int64'), []), relay.reshape(call_3009.astype('float64'), [1, 140]), ), 2)
output = relay.Tuple([call_3009,call_3019,var_3020,])
output2 = relay.Tuple([call_3010,call_3021,var_3020,])
func_3023 = relay.Function([var_3020,], output)
mod['func_3023'] = func_3023
mod = relay.transform.InferType()(mod)
mutated_mod['func_3023'] = func_3023
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3024 = relay.var("var_3024", dtype = "int64", shape = ())#candidate|3024|()|var|int64
func_3023_call = mutated_mod.get_global_var('func_3023')
call_3025 = func_3023_call(var_3024)
output = call_3025
func_3026 = relay.Function([var_3024], output)
mutated_mod['func_3026'] = func_3026
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2376_call = mod.get_global_var('func_2376')
func_2377_call = mutated_mod.get_global_var('func_2377')
call_3033 = relay.TupleGetItem(func_2376_call(), 1)
call_3034 = relay.TupleGetItem(func_2377_call(), 1)
output = call_3033
output2 = call_3034
func_3065 = relay.Function([], output)
mod['func_3065'] = func_3065
mod = relay.transform.InferType()(mod)
output = func_3065()
func_3066 = relay.Function([], output)
mutated_mod['func_3066'] = func_3066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2376_call = mod.get_global_var('func_2376')
func_2377_call = mutated_mod.get_global_var('func_2377')
call_3084 = relay.TupleGetItem(func_2376_call(), 0)
call_3085 = relay.TupleGetItem(func_2377_call(), 0)
const_3088 = relay.const([[[-1.804092,5.688183],[-3.234140,5.564866],[-3.014323,1.960945],[2.091744,5.359168],[2.248663,-5.897373],[-7.386704,3.493792],[9.703553,0.935821]],[[4.987160,-1.558018],[-6.619444,-3.728305],[-1.345682,6.444336],[4.117955,-7.952864],[-3.781846,-3.567538],[8.470044,-6.090373],[-7.341406,0.785378]],[[0.137698,2.859343],[8.344558,5.454642],[9.711989,-1.520553],[4.470921,-9.658166],[-1.833542,4.363522],[-4.317776,-8.277540],[4.938156,9.408521]],[[9.729032,7.551176],[-7.556717,1.213956],[9.730103,4.951844],[-0.629642,-8.344809],[4.578253,-5.451538],[1.412324,-1.202024],[0.128487,6.178075]],[[-0.983145,-4.747104],[2.859388,-4.273950],[5.258569,-1.026427],[-5.607744,1.643100],[0.598503,-8.177786],[1.130967,1.352170],[9.091169,-9.311336]],[[-4.115594,0.368470],[8.073166,-4.486223],[5.494225,-0.113746],[-0.507788,7.327983],[-8.273159,4.170536],[-9.664732,-4.301130],[-0.479672,-2.726164]],[[-4.789986,3.169805],[7.100041,2.915590],[-6.034202,6.059783],[-5.396334,-8.730916],[-9.001084,-8.831536],[2.476027,2.540610],[4.059333,3.953962]],[[7.278025,0.578220],[-5.996926,-1.559983],[5.212480,-9.770126],[-8.622498,-2.849735],[8.162057,2.430018],[-8.443698,-4.431489],[-4.214082,-8.548151]],[[-3.363860,0.995930],[2.050310,9.705501],[2.954353,6.427638],[1.705415,4.935553],[-8.943265,-5.637261],[-3.210491,8.388805],[1.212501,-0.623856]],[[9.411007,-0.411885],[-0.376632,9.123612],[-5.996883,-0.284169],[9.452420,9.229795],[5.249099,-3.474114],[-6.967399,-3.570585],[-4.767195,6.065457]]], dtype = "float64")#candidate|3088|(10, 7, 2)|const|float64
bop_3089 = relay.logical_xor(call_3084.astype('uint32'), relay.reshape(const_3088.astype('uint32'), relay.shape_of(call_3084))) # shape=(10, 7, 2)
bop_3092 = relay.logical_xor(call_3085.astype('uint32'), relay.reshape(const_3088.astype('uint32'), relay.shape_of(call_3085))) # shape=(10, 7, 2)
output = bop_3089
output2 = bop_3092
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
var_3100 = relay.var("var_3100", dtype = "float64", shape = (16, 5, 2))#candidate|3100|(16, 5, 2)|var|float64
uop_3101 = relay.asinh(var_3100.astype('float64')) # shape=(16, 5, 2)
func_2817_call = mod.get_global_var('func_2817')
func_2819_call = mutated_mod.get_global_var('func_2819')
call_3108 = relay.TupleGetItem(func_2817_call(), 0)
call_3109 = relay.TupleGetItem(func_2819_call(), 0)
output = relay.Tuple([uop_3101,call_3108,])
output2 = relay.Tuple([uop_3101,call_3109,])
func_3118 = relay.Function([var_3100,], output)
mod['func_3118'] = func_3118
mod = relay.transform.InferType()(mod)
var_3119 = relay.var("var_3119", dtype = "float64", shape = (16, 5, 2))#candidate|3119|(16, 5, 2)|var|float64
output = func_3118(var_3119)
func_3120 = relay.Function([var_3119], output)
mutated_mod['func_3120'] = func_3120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1401_call = mod.get_global_var('func_1401')
func_1402_call = mutated_mod.get_global_var('func_1402')
call_3132 = func_1401_call()
call_3133 = func_1401_call()
uop_3141 = relay.asinh(call_3132.astype('float32')) # shape=(10, 7, 2)
uop_3143 = relay.asinh(call_3133.astype('float32')) # shape=(10, 7, 2)
func_2523_call = mod.get_global_var('func_2523')
func_2525_call = mutated_mod.get_global_var('func_2525')
call_3145 = func_2523_call()
call_3146 = func_2523_call()
func_1255_call = mod.get_global_var('func_1255')
func_1256_call = mutated_mod.get_global_var('func_1256')
call_3148 = relay.TupleGetItem(func_1255_call(), 0)
call_3149 = relay.TupleGetItem(func_1256_call(), 0)
output = relay.Tuple([uop_3141,call_3145,call_3148,])
output2 = relay.Tuple([uop_3143,call_3146,call_3149,])
func_3153 = relay.Function([], output)
mod['func_3153'] = func_3153
mod = relay.transform.InferType()(mod)
output = func_3153()
func_3154 = relay.Function([], output)
mutated_mod['func_3154'] = func_3154
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3164 = relay.var("var_3164", dtype = "uint64", shape = ())#candidate|3164|()|var|uint64
var_3165 = relay.var("var_3165", dtype = "uint64", shape = (4, 4, 5))#candidate|3165|(4, 4, 5)|var|uint64
bop_3166 = relay.multiply(var_3164.astype('uint64'), var_3165.astype('uint64')) # shape=(4, 4, 5)
output = bop_3166
output2 = bop_3166
func_3177 = relay.Function([var_3164,var_3165,], output)
mod['func_3177'] = func_3177
mod = relay.transform.InferType()(mod)
var_3178 = relay.var("var_3178", dtype = "uint64", shape = ())#candidate|3178|()|var|uint64
var_3179 = relay.var("var_3179", dtype = "uint64", shape = (4, 4, 5))#candidate|3179|(4, 4, 5)|var|uint64
output = func_3177(var_3178,var_3179,)
func_3180 = relay.Function([var_3178,var_3179,], output)
mutated_mod['func_3180'] = func_3180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2376_call = mod.get_global_var('func_2376')
func_2377_call = mutated_mod.get_global_var('func_2377')
call_3195 = relay.TupleGetItem(func_2376_call(), 0)
call_3196 = relay.TupleGetItem(func_2377_call(), 0)
func_1110_call = mod.get_global_var('func_1110')
func_1113_call = mutated_mod.get_global_var('func_1113')
var_3222 = relay.var("var_3222", dtype = "int64", shape = ())#candidate|3222|()|var|int64
call_3221 = relay.TupleGetItem(func_1110_call(relay.reshape(var_3222.astype('int64'), []), relay.reshape(call_3195.astype('float64'), [1, 140]), ), 4)
call_3223 = relay.TupleGetItem(func_1113_call(relay.reshape(var_3222.astype('int64'), []), relay.reshape(call_3195.astype('float64'), [1, 140]), ), 4)
func_1027_call = mod.get_global_var('func_1027')
func_1030_call = mutated_mod.get_global_var('func_1030')
call_3228 = relay.TupleGetItem(func_1027_call(relay.reshape(call_3195.astype('float64'), [10, 7, 2])), 1)
call_3229 = relay.TupleGetItem(func_1030_call(relay.reshape(call_3195.astype('float64'), [10, 7, 2])), 1)
func_2376_call = mod.get_global_var('func_2376')
func_2377_call = mutated_mod.get_global_var('func_2377')
call_3242 = relay.TupleGetItem(func_2376_call(), 0)
call_3243 = relay.TupleGetItem(func_2377_call(), 0)
func_2508_call = mod.get_global_var('func_2508')
func_2510_call = mutated_mod.get_global_var('func_2510')
const_3247 = relay.const([6.819737,-4.609454,-2.541584,3.341730,2.464159,7.300069,-0.151505,-8.721705,0.467329,-0.776627,5.492754,-5.177079,-7.512825,0.919772,-4.094453,-0.047799,7.794603,-4.256540,5.584903,-9.446804,-1.943632,1.153401,2.521276,-8.278217,2.775971,5.594638,1.721003,5.516204,-1.573271,9.854309,-8.677001,-1.355824,-3.684603,8.685908,-8.735964,4.067935,-8.184767,-2.422385,-2.831771,-7.897638,8.486912,3.788028,-1.449094,-6.580520,7.061167,3.188664,2.707878,1.617865,-0.598690,-3.203591,5.367868,-3.933292,-5.216246,2.218605,7.069839,-0.412578,8.510563,1.649099,-3.699213,4.567050,2.192892,6.243223,-0.500380,4.840045,4.026916,-6.204258,4.095273,-5.543639,4.202907,-9.661315,-7.095757,6.799675,-6.341317,2.560827,-9.143597,3.627095,1.437982,-8.420326,4.107964,6.167427,2.430156,7.926267,-4.106097,-4.789687,5.935925,-3.365513,6.859832,-1.911507,9.823236,-8.154853,-1.987872,2.415541,-7.824560,7.244443,8.070096,8.900246,-3.056373,1.396677,-1.716131,-1.552385,0.779924,3.199374,-0.625591,-3.788867,2.218394,5.374295,-8.995015,-8.458130,4.124609,7.086766,-0.358481,2.249715,6.846734,2.816551,2.441864,-7.546878,-4.159861,1.864794,8.584984,-5.785116,3.931249,-0.141546,8.628252,-6.598973,-3.173869,0.525611,-6.562529,-8.270952,-6.861799,-7.427906,3.407116,-9.697716,-7.091917,0.237107,2.465041,4.677579,3.803342,7.875399,-7.858957,1.567463,5.055096,1.482937,-5.276834,1.213452,8.779473,-3.950045,-7.694129,-5.712590,-4.849618,-8.817286,-1.026794,-1.998994,4.904274,-5.982381,-3.447877,2.602136,-3.764311,8.944682,-7.352004,6.320271,-1.622411,-4.168128,-3.742842,-3.713059,-1.786140,8.540146,-0.085488,0.910311,2.111496,3.623837,7.300627,6.812529,0.834750,-9.509927,5.958185,7.723628,4.803853,3.659346,-7.716864,4.858069,-7.050915,7.426590,-8.654575,8.010903,-9.625172,8.376395,4.971234,-8.762778,-0.131433,-1.239733,-5.124393,5.826357,1.404434,-8.076930,-8.088733,6.472323,-5.372439,3.397780,8.881324,-7.035184,8.717820,0.383813,-9.468659,4.004291,1.088592,-7.126794,3.204817,1.380148,-1.757835,4.891552,1.887816,-2.621429,8.984842,6.294960,-5.369954,9.447332,0.412249,-6.431448,-0.852716,-5.348576,3.380686,4.114834,0.772713,8.605520,-4.833739,-3.920203,1.617876,1.892811,6.885532,6.827295,-4.335375,8.387981,-0.825338,5.416122,-7.227412,-0.879426,1.291207,-3.273797,-9.261503,-9.547051,-8.860311,2.820603,7.888967,6.399182,8.308890,-0.190627,1.632964,8.956336,6.117797,-2.459631,0.371362,3.888006,-7.209147,1.873392,-7.584200,-9.456777,-7.580090,-1.216355,-3.304305,-7.868485,9.292439,-6.613598,0.572381,-5.264156,-4.824792,-2.678583,5.051094,-1.240724,9.571327,-6.543715,-2.129817,9.383327,-1.431099,-6.780320,5.758961,-0.275548,-3.217706,0.171746,3.140198,-6.859406,-1.939942,5.389542,7.488540,6.365560,1.151179,-4.409245,-3.091406,-9.048244,1.555455,-9.102291,-9.285628,2.303929,9.806553,-7.524858,-1.454056,-7.017585,5.389100,-7.289614,-6.979154,6.340219,-3.281492,5.350550,2.714704,1.401446,-5.742495,6.655976,7.934252,0.434391,8.707945,9.874621,0.596297,-1.308274,2.644814,4.947856,3.775742,9.208304,-9.166968,-7.018676,-9.758442,-5.317413,1.073610,7.825976,1.672249,0.637484,-6.636377,-7.123957,9.781202,-7.243109,-9.024066,-9.169104,6.089628,3.782625,-6.153290,2.702982,9.079676,4.381542,-7.687084,5.863642,-0.014034,-1.619818,1.612990,-0.182154,-3.744553,5.081163,-9.710037,-9.523414,3.304116,3.056949,6.511292,2.208793,-8.637376,-1.887762,6.133229,-3.891236,-1.891951,9.362335,-2.226163,-5.169455,-6.326286,0.897484,3.151373,-9.040337,3.161048,-5.665406,4.545880,6.959530,9.690379,-2.616288,-8.276453,-6.126517,1.770180,-5.452981,9.131467,-1.537416,5.609954,-7.593229,9.703214,9.764614,-4.201739,-3.194930,6.812375,5.898392,8.432879,-9.265927,9.117480,-9.289053,-1.946423,-0.580263,-3.119553,8.158739,-6.588702,-4.574188,2.626161,-0.670540,-9.144869,6.651465,-8.782867,-2.576300,-1.686095,5.931612,2.159543,-4.814007,6.490659,5.573220,-0.046547,1.012633,-3.321259,-8.634947,1.805762,7.136575,7.362361,-9.047433,4.164814,3.003708,6.028292,4.390889,0.199932,-3.337526,-9.783360,-7.031453,-7.246545,9.723532,1.199662,-1.087858,-8.451125,-1.580031,-8.359380,-0.193330,8.817517,7.319889,-8.825052,9.476789,9.098506,-6.512171,1.388943,-8.370436,-2.701393,-5.060206,8.784796,5.952798,-0.385310,-0.939769,-8.443466,6.752304,-0.840370,-7.626613,2.835516,-0.300898,4.199639,1.722967,1.321505,-9.387456,8.615700,-1.701751,-9.792293,3.161606,2.266735,1.156185,-2.846286,-3.948622,-0.262227,0.050287,-1.490842,-8.926300,0.117829,6.449865,6.681885,-9.539155,-6.114441,7.373121,-1.856297,-4.432738,-0.154914,0.457535,-2.295660,-6.093963,-5.895334,-0.171317,3.489817,-1.568780,-1.526700,-9.265393,-8.345993,0.894180,1.192435,3.659967,5.741025,2.709371,4.214022,-1.758333], dtype = "float64")#candidate|3247|(490,)|const|float64
call_3246 = relay.TupleGetItem(func_2508_call(relay.reshape(const_3247.astype('float64'), [5, 14, 7])), 1)
call_3248 = relay.TupleGetItem(func_2510_call(relay.reshape(const_3247.astype('float64'), [5, 14, 7])), 1)
output = relay.Tuple([call_3195,call_3221,var_3222,call_3228,call_3242,call_3246,const_3247,])
output2 = relay.Tuple([call_3196,call_3223,var_3222,call_3229,call_3243,call_3248,const_3247,])
func_3250 = relay.Function([var_3222,], output)
mod['func_3250'] = func_3250
mod = relay.transform.InferType()(mod)
mutated_mod['func_3250'] = func_3250
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3251 = relay.var("var_3251", dtype = "int64", shape = ())#candidate|3251|()|var|int64
func_3250_call = mutated_mod.get_global_var('func_3250')
call_3252 = func_3250_call(var_3251)
output = call_3252
func_3253 = relay.Function([var_3251], output)
mutated_mod['func_3253'] = func_3253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3065_call = mod.get_global_var('func_3065')
func_3066_call = mutated_mod.get_global_var('func_3066')
call_3287 = func_3065_call()
call_3288 = func_3065_call()
func_1110_call = mod.get_global_var('func_1110')
func_1113_call = mutated_mod.get_global_var('func_1113')
var_3315 = relay.var("var_3315", dtype = "int64", shape = ())#candidate|3315|()|var|int64
call_3314 = relay.TupleGetItem(func_1110_call(relay.reshape(var_3315.astype('int64'), []), relay.reshape(call_3287.astype('float64'), [1, 140]), ), 4)
call_3316 = relay.TupleGetItem(func_1113_call(relay.reshape(var_3315.astype('int64'), []), relay.reshape(call_3287.astype('float64'), [1, 140]), ), 4)
func_1308_call = mod.get_global_var('func_1308')
func_1310_call = mutated_mod.get_global_var('func_1310')
call_3334 = func_1308_call()
call_3335 = func_1308_call()
func_1136_call = mod.get_global_var('func_1136')
func_1137_call = mutated_mod.get_global_var('func_1137')
call_3345 = func_1136_call()
call_3346 = func_1136_call()
output = relay.Tuple([call_3287,call_3314,var_3315,call_3334,call_3345,])
output2 = relay.Tuple([call_3288,call_3316,var_3315,call_3335,call_3346,])
func_3353 = relay.Function([var_3315,], output)
mod['func_3353'] = func_3353
mod = relay.transform.InferType()(mod)
var_3354 = relay.var("var_3354", dtype = "int64", shape = ())#candidate|3354|()|var|int64
output = func_3353(var_3354)
func_3355 = relay.Function([var_3354], output)
mutated_mod['func_3355'] = func_3355
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2428_call = mod.get_global_var('func_2428')
func_2430_call = mutated_mod.get_global_var('func_2430')
call_3378 = func_2428_call()
call_3379 = func_2428_call()
output = relay.Tuple([call_3378,])
output2 = relay.Tuple([call_3379,])
func_3386 = relay.Function([], output)
mod['func_3386'] = func_3386
mod = relay.transform.InferType()(mod)
mutated_mod['func_3386'] = func_3386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3386_call = mutated_mod.get_global_var('func_3386')
call_3387 = func_3386_call()
output = call_3387
func_3388 = relay.Function([], output)
mutated_mod['func_3388'] = func_3388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1938_call = mod.get_global_var('func_1938')
func_1940_call = mutated_mod.get_global_var('func_1940')
call_3457 = func_1938_call()
call_3458 = func_1938_call()
func_751_call = mod.get_global_var('func_751')
func_752_call = mutated_mod.get_global_var('func_752')
call_3459 = relay.TupleGetItem(func_751_call(), 0)
call_3460 = relay.TupleGetItem(func_752_call(), 0)
func_1468_call = mod.get_global_var('func_1468')
func_1470_call = mutated_mod.get_global_var('func_1470')
call_3467 = relay.TupleGetItem(func_1468_call(), 1)
call_3468 = relay.TupleGetItem(func_1470_call(), 1)
output = relay.Tuple([call_3457,call_3459,call_3467,])
output2 = relay.Tuple([call_3458,call_3460,call_3468,])
func_3471 = relay.Function([], output)
mod['func_3471'] = func_3471
mod = relay.transform.InferType()(mod)
mutated_mod['func_3471'] = func_3471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3471_call = mutated_mod.get_global_var('func_3471')
call_3472 = func_3471_call()
output = call_3472
func_3473 = relay.Function([], output)
mutated_mod['func_3473'] = func_3473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_751_call = mod.get_global_var('func_751')
func_752_call = mutated_mod.get_global_var('func_752')
call_3516 = relay.TupleGetItem(func_751_call(), 1)
call_3517 = relay.TupleGetItem(func_752_call(), 1)
func_935_call = mod.get_global_var('func_935')
func_936_call = mutated_mod.get_global_var('func_936')
call_3550 = func_935_call()
call_3551 = func_935_call()
func_1569_call = mod.get_global_var('func_1569')
func_1571_call = mutated_mod.get_global_var('func_1571')
call_3553 = relay.TupleGetItem(func_1569_call(), 0)
call_3554 = relay.TupleGetItem(func_1571_call(), 0)
func_3386_call = mod.get_global_var('func_3386')
func_3388_call = mutated_mod.get_global_var('func_3388')
call_3555 = relay.TupleGetItem(func_3386_call(), 0)
call_3556 = relay.TupleGetItem(func_3388_call(), 0)
output = relay.Tuple([call_3516,call_3550,call_3553,call_3555,])
output2 = relay.Tuple([call_3517,call_3551,call_3554,call_3556,])
func_3562 = relay.Function([], output)
mod['func_3562'] = func_3562
mod = relay.transform.InferType()(mod)
mutated_mod['func_3562'] = func_3562
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3562_call = mutated_mod.get_global_var('func_3562')
call_3563 = func_3562_call()
output = call_3563
func_3564 = relay.Function([], output)
mutated_mod['func_3564'] = func_3564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3562_call = mod.get_global_var('func_3562')
func_3564_call = mutated_mod.get_global_var('func_3564')
call_3799 = relay.TupleGetItem(func_3562_call(), 2)
call_3800 = relay.TupleGetItem(func_3564_call(), 2)
func_1569_call = mod.get_global_var('func_1569')
func_1571_call = mutated_mod.get_global_var('func_1571')
call_3815 = relay.TupleGetItem(func_1569_call(), 0)
call_3816 = relay.TupleGetItem(func_1571_call(), 0)
output = relay.Tuple([call_3799,call_3815,])
output2 = relay.Tuple([call_3800,call_3816,])
func_3827 = relay.Function([], output)
mod['func_3827'] = func_3827
mod = relay.transform.InferType()(mod)
output = func_3827()
func_3828 = relay.Function([], output)
mutated_mod['func_3828'] = func_3828
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1401_call = mod.get_global_var('func_1401')
func_1402_call = mutated_mod.get_global_var('func_1402')
call_3931 = func_1401_call()
call_3932 = func_1401_call()
output = relay.Tuple([call_3931,])
output2 = relay.Tuple([call_3932,])
func_3933 = relay.Function([], output)
mod['func_3933'] = func_3933
mod = relay.transform.InferType()(mod)
mutated_mod['func_3933'] = func_3933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3933_call = mutated_mod.get_global_var('func_3933')
call_3934 = func_3933_call()
output = call_3934
func_3935 = relay.Function([], output)
mutated_mod['func_3935'] = func_3935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2059_call = mod.get_global_var('func_2059')
func_2061_call = mutated_mod.get_global_var('func_2061')
call_3950 = relay.TupleGetItem(func_2059_call(), 0)
call_3951 = relay.TupleGetItem(func_2061_call(), 0)
func_3933_call = mod.get_global_var('func_3933')
func_3935_call = mutated_mod.get_global_var('func_3935')
call_3958 = relay.TupleGetItem(func_3933_call(), 0)
call_3959 = relay.TupleGetItem(func_3935_call(), 0)
func_3097_call = mod.get_global_var('func_3097')
func_3099_call = mutated_mod.get_global_var('func_3099')
call_3969 = func_3097_call()
call_3970 = func_3097_call()
output = relay.Tuple([call_3950,call_3958,call_3969,])
output2 = relay.Tuple([call_3951,call_3959,call_3970,])
func_3976 = relay.Function([], output)
mod['func_3976'] = func_3976
mod = relay.transform.InferType()(mod)
mutated_mod['func_3976'] = func_3976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3976_call = mutated_mod.get_global_var('func_3976')
call_3977 = func_3976_call()
output = call_3977
func_3978 = relay.Function([], output)
mutated_mod['func_3978'] = func_3978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2428_call = mod.get_global_var('func_2428')
func_2430_call = mutated_mod.get_global_var('func_2430')
call_4049 = func_2428_call()
call_4050 = func_2428_call()
func_827_call = mod.get_global_var('func_827')
func_829_call = mutated_mod.get_global_var('func_829')
call_4069 = relay.TupleGetItem(func_827_call(), 0)
call_4070 = relay.TupleGetItem(func_829_call(), 0)
func_3065_call = mod.get_global_var('func_3065')
func_3066_call = mutated_mod.get_global_var('func_3066')
call_4089 = func_3065_call()
call_4090 = func_3065_call()
output = relay.Tuple([call_4049,call_4069,call_4089,])
output2 = relay.Tuple([call_4050,call_4070,call_4090,])
func_4093 = relay.Function([], output)
mod['func_4093'] = func_4093
mod = relay.transform.InferType()(mod)
mutated_mod['func_4093'] = func_4093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4093_call = mutated_mod.get_global_var('func_4093')
call_4094 = func_4093_call()
output = call_4094
func_4095 = relay.Function([], output)
mutated_mod['func_4095'] = func_4095
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4093_call = mod.get_global_var('func_4093')
func_4095_call = mutated_mod.get_global_var('func_4095')
call_4106 = relay.TupleGetItem(func_4093_call(), 2)
call_4107 = relay.TupleGetItem(func_4095_call(), 2)
uop_4110 = relay.exp(call_4106.astype('float64')) # shape=(10, 7, 2)
uop_4112 = relay.exp(call_4107.astype('float64')) # shape=(10, 7, 2)
func_1136_call = mod.get_global_var('func_1136')
func_1137_call = mutated_mod.get_global_var('func_1137')
call_4126 = func_1136_call()
call_4127 = func_1136_call()
func_3153_call = mod.get_global_var('func_3153')
func_3154_call = mutated_mod.get_global_var('func_3154')
call_4136 = relay.TupleGetItem(func_3153_call(), 2)
call_4137 = relay.TupleGetItem(func_3154_call(), 2)
output = relay.Tuple([uop_4110,call_4126,call_4136,])
output2 = relay.Tuple([uop_4112,call_4127,call_4137,])
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
var_4187 = relay.var("var_4187", dtype = "uint32", shape = ())#candidate|4187|()|var|uint32
var_4188 = relay.var("var_4188", dtype = "uint32", shape = (5, 2, 5))#candidate|4188|(5, 2, 5)|var|uint32
bop_4189 = relay.left_shift(var_4187.astype('uint32'), var_4188.astype('uint32')) # shape=(5, 2, 5)
output = bop_4189
output2 = bop_4189
func_4218 = relay.Function([var_4187,var_4188,], output)
mod['func_4218'] = func_4218
mod = relay.transform.InferType()(mod)
mutated_mod['func_4218'] = func_4218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4218_call = mutated_mod.get_global_var('func_4218')
var_4220 = relay.var("var_4220", dtype = "uint32", shape = ())#candidate|4220|()|var|uint32
var_4221 = relay.var("var_4221", dtype = "uint32", shape = (5, 2, 5))#candidate|4221|(5, 2, 5)|var|uint32
call_4219 = func_4218_call(var_4220,var_4221,)
output = call_4219
func_4222 = relay.Function([var_4220,var_4221,], output)
mutated_mod['func_4222'] = func_4222
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4141_call = mod.get_global_var('func_4141')
func_4143_call = mutated_mod.get_global_var('func_4143')
call_4238 = relay.TupleGetItem(func_4141_call(), 1)
call_4239 = relay.TupleGetItem(func_4143_call(), 1)
output = call_4238
output2 = call_4239
func_4266 = relay.Function([], output)
mod['func_4266'] = func_4266
mod = relay.transform.InferType()(mod)
output = func_4266()
func_4267 = relay.Function([], output)
mutated_mod['func_4267'] = func_4267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3933_call = mod.get_global_var('func_3933')
func_3935_call = mutated_mod.get_global_var('func_3935')
call_4284 = relay.TupleGetItem(func_3933_call(), 0)
call_4285 = relay.TupleGetItem(func_3935_call(), 0)
output = call_4284
output2 = call_4285
func_4286 = relay.Function([], output)
mod['func_4286'] = func_4286
mod = relay.transform.InferType()(mod)
output = func_4286()
func_4287 = relay.Function([], output)
mutated_mod['func_4287'] = func_4287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3562_call = mod.get_global_var('func_3562')
func_3564_call = mutated_mod.get_global_var('func_3564')
call_4291 = relay.TupleGetItem(func_3562_call(), 1)
call_4292 = relay.TupleGetItem(func_3564_call(), 1)
output = relay.Tuple([call_4291,])
output2 = relay.Tuple([call_4292,])
func_4294 = relay.Function([], output)
mod['func_4294'] = func_4294
mod = relay.transform.InferType()(mod)
mutated_mod['func_4294'] = func_4294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4294_call = mutated_mod.get_global_var('func_4294')
call_4295 = func_4294_call()
output = call_4295
func_4296 = relay.Function([], output)
mutated_mod['func_4296'] = func_4296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2237_call = mod.get_global_var('func_2237')
func_2239_call = mutated_mod.get_global_var('func_2239')
call_4311 = relay.TupleGetItem(func_2237_call(), 0)
call_4312 = relay.TupleGetItem(func_2239_call(), 0)
output = call_4311
output2 = call_4312
func_4314 = relay.Function([], output)
mod['func_4314'] = func_4314
mod = relay.transform.InferType()(mod)
output = func_4314()
func_4315 = relay.Function([], output)
mutated_mod['func_4315'] = func_4315
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4330 = relay.var("var_4330", dtype = "uint16", shape = (16, 14, 3))#candidate|4330|(16, 14, 3)|var|uint16
var_4331 = relay.var("var_4331", dtype = "uint16", shape = (16, 14, 3))#candidate|4331|(16, 14, 3)|var|uint16
bop_4332 = relay.subtract(var_4330.astype('uint16'), relay.reshape(var_4331.astype('uint16'), relay.shape_of(var_4330))) # shape=(16, 14, 3)
func_4286_call = mod.get_global_var('func_4286')
func_4287_call = mutated_mod.get_global_var('func_4287')
call_4335 = func_4286_call()
call_4336 = func_4286_call()
uop_4359 = relay.atan(bop_4332.astype('float64')) # shape=(16, 14, 3)
uop_4368 = relay.acos(uop_4359.astype('float32')) # shape=(16, 14, 3)
uop_4370 = relay.sqrt(uop_4368.astype('float64')) # shape=(16, 14, 3)
var_4375 = relay.var("var_4375", dtype = "float64", shape = (16, 14, 3))#candidate|4375|(16, 14, 3)|var|float64
bop_4376 = relay.multiply(uop_4370.astype('float64'), relay.reshape(var_4375.astype('float64'), relay.shape_of(uop_4370))) # shape=(16, 14, 3)
func_2763_call = mod.get_global_var('func_2763')
func_2764_call = mutated_mod.get_global_var('func_2764')
call_4384 = relay.TupleGetItem(func_2763_call(), 1)
call_4385 = relay.TupleGetItem(func_2764_call(), 1)
uop_4408 = relay.erf(call_4384.astype('float32')) # shape=(49, 10)
uop_4410 = relay.erf(call_4385.astype('float32')) # shape=(49, 10)
output = relay.Tuple([call_4335,bop_4376,uop_4408,])
output2 = relay.Tuple([call_4336,bop_4376,uop_4410,])
func_4417 = relay.Function([var_4330,var_4331,var_4375,], output)
mod['func_4417'] = func_4417
mod = relay.transform.InferType()(mod)
mutated_mod['func_4417'] = func_4417
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4417_call = mutated_mod.get_global_var('func_4417')
var_4419 = relay.var("var_4419", dtype = "uint16", shape = (16, 14, 3))#candidate|4419|(16, 14, 3)|var|uint16
var_4420 = relay.var("var_4420", dtype = "uint16", shape = (16, 14, 3))#candidate|4420|(16, 14, 3)|var|uint16
var_4421 = relay.var("var_4421", dtype = "float64", shape = (16, 14, 3))#candidate|4421|(16, 14, 3)|var|float64
call_4418 = func_4417_call(var_4419,var_4420,var_4421,)
output = call_4418
func_4422 = relay.Function([var_4419,var_4420,var_4421,], output)
mutated_mod['func_4422'] = func_4422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2763_call = mod.get_global_var('func_2763')
func_2764_call = mutated_mod.get_global_var('func_2764')
call_4424 = relay.TupleGetItem(func_2763_call(), 1)
call_4425 = relay.TupleGetItem(func_2764_call(), 1)
func_2817_call = mod.get_global_var('func_2817')
func_2819_call = mutated_mod.get_global_var('func_2819')
call_4426 = relay.TupleGetItem(func_2817_call(), 0)
call_4427 = relay.TupleGetItem(func_2819_call(), 0)
func_3250_call = mod.get_global_var('func_3250')
func_3253_call = mutated_mod.get_global_var('func_3253')
const_4444 = relay.const(-10, dtype = "int64")#candidate|4444|()|const|int64
call_4443 = relay.TupleGetItem(func_3250_call(relay.reshape(const_4444.astype('int64'), [])), 1)
call_4445 = relay.TupleGetItem(func_3253_call(relay.reshape(const_4444.astype('int64'), [])), 1)
func_2059_call = mod.get_global_var('func_2059')
func_2061_call = mutated_mod.get_global_var('func_2061')
call_4446 = relay.TupleGetItem(func_2059_call(), 0)
call_4447 = relay.TupleGetItem(func_2061_call(), 0)
func_4093_call = mod.get_global_var('func_4093')
func_4095_call = mutated_mod.get_global_var('func_4095')
call_4453 = relay.TupleGetItem(func_4093_call(), 1)
call_4454 = relay.TupleGetItem(func_4095_call(), 1)
func_2817_call = mod.get_global_var('func_2817')
func_2819_call = mutated_mod.get_global_var('func_2819')
call_4455 = relay.TupleGetItem(func_2817_call(), 0)
call_4456 = relay.TupleGetItem(func_2819_call(), 0)
func_4417_call = mod.get_global_var('func_4417')
func_4422_call = mutated_mod.get_global_var('func_4422')
const_4463 = relay.const([-3,-8,8,-9,-6,9,-6,-9,7,6,-1,-9,-8,3,-2,-1,-9,-6,-5,-2,-4,9,3,-4,8,-4,6,7,-10,3,-1,8,3,6,1,-1,1,2,7,-4,-7,-4,-2,6,-3,3,-5,-3,7,8,-9,10,6,6,1,8,6,10,5,1,6,2,-7,10,4,1,-7,-5,-4,-6,-1,-2,8,-7,9,-3,-4,-6,9,4,-6,-9,7,-5,7,7,-8,6,-2,-3,3,-5,10,-7,-9,-2,-7,7,-7,6,-6,3,-3,-1,6,-5,7,-5,1,-6,4,-5,-1,6,7,-5,4,-6,-8,3,1,2,-7,-7,-8,9,10,-2,8,-10,-9,-7,-2,-1,10,-4,-1,-8,-3,7,7,1,1,8,-1,-4,1,5,-4,4,10,6,-4,2,-1,-7,6,-6,3,-6,-2,7,6,7,-8,-6,6,-2,6,6,-2,6,2,4,-5,2,-5,-1,2,-10,6,1,-8,4,8,1,-4,-7,-8,2,5,3,4,10,-1,-8,-6,10,-3,-8,-4,-2,-8,5,-2,-3,4,7,-7,5,7,4,-2,9,-9,-8,-10,3,1,-5,-8,2,-2,9,-7,-7,8,10,-8,-7,8,1,-10,-5,2,-4,8,-2,6,-2,-6,7,-4,5,-8,8,2,5,2,10,1,6,-1,-2,2,10,-6,-1,6,10,-10,1,8,1,5,7,9,-7,-4,9,-4,-1,6,9,-9,7,9,-9,-5,8,4,-7,-1,-3,-3,10,-1,-6,-4,-10,-5,-2,6,-3,4,2,9,2,4,-4,10,-4,4,10,6,10,-9,-8,-6,8,4,-1,-1,-2,10,2,9,-1,-8,2,-2,-7,-7,-10,8,4,-9,-7,-9,5,-7,9,3,-1,-2,-4,5,7,-6,4,4,6,-4,4,-3,1,6,-6,-4,1,-7,-2,6,-4,-6,-6,6,-6,6,4,-10,7,-6,8,-1,-6,4,3,-7,2,-3,6,10,-2,5,-4,-10,3,-8,-8,2,7,3,-5,7,6,4,1,-5,10,8,4,-7,-8,10,3,-1,7,10,-4,7,-7,3,7,-3,-5,1,1,-6,2,-4,-7,3,8,-6,-2,-4,6,-9,3,-9,2,-10,7,-9,-4,-4,-7,7,-2,-8,5,-5,7,-3,-3,3,-2,8,8,10,10,5,1,-1,-2,-9,-10,8,-6,2,-5,5,-5,-9,-10,-7,3,8,-3,-6,7,-3,-8,6,4,-5,10,-6,-3,-10,-6,-3,-8,-2,1,5,3,-5,-9,-7,7,-3,2,-4,6,7,-10,10,3,-6,-2,-2,-8,-6,-8,-1,-4,3,-4,10,8,4,10,-5,-8,9,1,4,8,6,4,-2,2,4,-2,-9,-2,10,9,-6,4,6,7,-5,-10,3,-8,2,-10,-7,-1,-3,-9,6,6,-4,9,8,-2,3,3,7,10,-3,-4,-3,9,9,-8,-8,8,9,-4,5,9,9,3,5,-5,-4,-3,5,4,1,-8,-8,-1,-8,-3,4,-1,6,-8,9,-3,4,1,-7,-3,7,-5,2,2,-4,10,-9,-10,-9,9,-4,3,6,5,-9,10,-2,10,3,-1,-9,5,-6,-6,-5,-10,-5,5,7,5,-8,1,-1,3,5,3,7,-5,-2,7,-3,-4,-2,-2,-1,-4,-1,1,7,6,-8,-9,6,9,4,5,4,8,10,-4,6,-10,-4,8,4,5,-2,10,-8,-6,-6,-2,4,-6,-9,-7,-10,-1,-7,8,-3,-5,7,3,-6,-8,3,3,-9,2,-3,4], dtype = "uint16")#candidate|4463|(672,)|const|uint16
call_4462 = relay.TupleGetItem(func_4417_call(relay.reshape(const_4463.astype('uint16'), [16, 14, 3]), relay.reshape(const_4463.astype('uint16'), [16, 14, 3]), relay.reshape(const_4463.astype('float64'), [16, 14, 3]), ), 0)
call_4464 = relay.TupleGetItem(func_4422_call(relay.reshape(const_4463.astype('uint16'), [16, 14, 3]), relay.reshape(const_4463.astype('uint16'), [16, 14, 3]), relay.reshape(const_4463.astype('float64'), [16, 14, 3]), ), 0)
func_1468_call = mod.get_global_var('func_1468')
func_1470_call = mutated_mod.get_global_var('func_1470')
call_4466 = relay.TupleGetItem(func_1468_call(), 2)
call_4467 = relay.TupleGetItem(func_1470_call(), 2)
output = relay.Tuple([call_4424,call_4426,call_4443,const_4444,call_4446,call_4453,call_4455,call_4462,const_4463,call_4466,])
output2 = relay.Tuple([call_4425,call_4427,call_4445,const_4444,call_4447,call_4454,call_4456,call_4464,const_4463,call_4467,])
func_4472 = relay.Function([], output)
mod['func_4472'] = func_4472
mod = relay.transform.InferType()(mod)
output = func_4472()
func_4473 = relay.Function([], output)
mutated_mod['func_4473'] = func_4473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2428_call = mod.get_global_var('func_2428')
func_2430_call = mutated_mod.get_global_var('func_2430')
call_4476 = func_2428_call()
call_4477 = func_2428_call()
func_4417_call = mod.get_global_var('func_4417')
func_4422_call = mutated_mod.get_global_var('func_4422')
var_4481 = relay.var("var_4481", dtype = "uint16", shape = (672,))#candidate|4481|(672,)|var|uint16
call_4480 = relay.TupleGetItem(func_4417_call(relay.reshape(var_4481.astype('uint16'), [16, 14, 3]), relay.reshape(var_4481.astype('uint16'), [16, 14, 3]), relay.reshape(var_4481.astype('float64'), [16, 14, 3]), ), 2)
call_4482 = relay.TupleGetItem(func_4422_call(relay.reshape(var_4481.astype('uint16'), [16, 14, 3]), relay.reshape(var_4481.astype('uint16'), [16, 14, 3]), relay.reshape(var_4481.astype('float64'), [16, 14, 3]), ), 2)
uop_4493 = relay.asin(call_4480.astype('float32')) # shape=(49, 10)
uop_4495 = relay.asin(call_4482.astype('float32')) # shape=(49, 10)
const_4503 = relay.const([[-0.614290,1.760977,5.542828,3.298574,0.680017,7.894320,-9.938703,-4.199962,-6.472567,8.992675],[-7.353144,-3.453315,-9.372333,5.541324,-2.768204,5.183123,-6.530961,5.142770,-9.388678,9.306924],[7.686921,-9.691219,5.588100,-9.492642,-1.635511,-0.256050,-0.518830,3.539242,3.525691,-0.496695],[0.616947,-5.532828,-8.938503,5.573264,6.799910,6.065123,9.616910,-0.395555,-1.789061,-4.477964],[1.890158,5.077487,-5.852420,-9.135105,1.794769,3.799252,-4.127935,-2.127968,0.993396,7.677974],[8.995473,-7.248070,1.800133,7.095351,0.680048,-0.812369,-7.433466,0.016186,-5.822194,-0.565063],[-4.659243,-6.685933,-8.054665,-8.684355,-6.487316,-2.693593,-8.155520,-2.254042,8.712401,8.531621],[-2.162696,3.362438,-9.303614,9.758620,8.812102,-8.970382,9.233078,-4.299709,-4.602301,-1.736363],[0.503102,-8.689187,5.017453,0.428107,-3.338199,0.325287,-7.065622,3.797727,4.934440,-8.971328],[9.187401,6.573620,9.814271,-7.389146,-9.267752,4.267246,9.248597,7.704742,-5.570139,7.040067],[7.036418,6.684479,-7.664683,-9.403720,4.619187,-4.686378,-4.792760,-2.003479,9.942988,1.288761],[1.637272,1.453893,-6.336814,7.383100,2.694378,4.313717,8.201037,1.966936,4.374445,-5.370342],[-6.189461,2.919861,-1.554396,-6.515423,-6.534726,6.056656,-6.900424,-4.788567,9.825394,-4.465384],[7.124600,4.367465,-6.308873,-0.950868,3.605306,7.370479,8.105289,-1.766976,-7.548898,4.916094],[-4.801192,-4.283684,-5.325674,8.128371,-8.768039,-3.045791,0.480298,-0.271455,-2.987570,2.334079],[5.420785,3.418260,-7.895373,-4.818418,6.841024,8.561707,-3.525906,-9.738361,0.350126,-4.998726],[3.311896,8.284584,9.308114,9.427249,-1.378759,9.512480,3.072500,-2.736687,-6.576371,-4.645938],[-0.939118,5.909896,8.772703,0.265284,8.305393,-3.065166,4.642125,0.877820,2.773250,-3.089026],[6.226314,-7.767063,3.275215,-7.211515,8.080851,9.916489,1.742828,1.504790,-1.190043,4.705063],[-8.163941,8.962392,0.583153,-2.532387,1.587998,-0.173787,-8.707648,0.019305,0.595185,4.261882],[-4.016005,-8.573561,2.528665,-0.591143,8.983349,1.539686,3.747792,9.527821,3.201160,1.556646],[-4.097538,-2.116566,-4.521075,-3.834358,4.790570,7.253395,-0.197932,6.038985,5.676474,-8.453085],[0.547561,-2.445206,-0.015005,9.841335,-5.744663,-3.011982,-6.408234,4.774377,-2.443555,-1.959479],[-9.580384,8.259711,-3.198040,-8.456371,-4.807696,-4.121810,5.546253,-7.930838,-0.701969,7.305167],[-0.122493,8.314148,-4.812623,-7.585290,1.970529,6.874488,-8.312766,-2.839497,6.418829,-0.068485],[9.848798,-9.036154,5.255543,-9.117483,-5.220910,-0.568807,1.665855,-8.723970,8.160024,-8.183704],[1.075596,-6.488737,-8.710368,-0.818301,7.774419,1.711638,1.374674,8.163258,-8.828134,-7.268663],[-7.176796,-9.829762,9.149750,6.696716,0.394875,2.770170,1.952906,-1.162740,-4.864463,-4.292823],[4.632326,6.385218,6.798060,1.646002,-4.144519,-5.443351,8.943535,2.897959,2.783878,8.017487],[-9.654675,-6.980888,-1.363598,-5.764733,0.510781,-9.478973,-1.087508,-2.492550,8.158879,-9.308385],[5.398979,-9.683593,8.231505,4.977384,-8.763029,1.204974,5.748887,8.638360,-1.278835,2.559006],[-5.078127,-6.399868,2.455592,-4.461555,-5.613909,-3.435166,0.818217,-7.552465,-9.206655,-1.625206],[-5.228755,-7.770211,3.105734,0.736988,3.707440,1.213167,7.875947,-8.861167,-7.022753,8.751212],[6.597315,3.462100,-7.113812,5.112663,0.095338,9.191037,8.693281,-1.163434,8.058660,-7.390864],[-4.016734,-8.632249,7.472636,-3.167010,7.646501,6.096507,6.333064,-0.451296,-9.143016,9.686289],[6.777445,-6.123989,-6.798062,0.338878,-0.114282,-1.048637,5.960284,-3.719384,4.841475,0.535888],[-1.557699,-8.918877,5.047773,0.839807,-2.674922,8.728493,-6.705090,2.167409,-2.484549,-7.928644],[-3.877478,3.696312,-9.808778,7.045510,-2.447996,-6.941749,6.447160,5.685280,2.543591,-2.249103],[3.221689,1.756527,9.635440,-4.402204,1.243615,4.770720,6.712640,-9.980235,-8.703661,0.263305],[-6.822221,-7.878801,-1.495902,-3.351895,-2.071951,-2.195752,-0.665349,2.738993,-3.893009,-7.708156],[5.287167,2.231263,-4.761020,-1.860619,5.880509,-4.637141,8.360114,8.335663,-3.011957,-6.224467],[1.017983,-8.536851,-4.419575,5.736639,8.500784,0.538005,3.549368,1.707419,-6.705567,4.480633],[9.338871,4.465220,-4.984213,0.549243,-3.410020,8.446574,-2.853910,7.519184,-0.394803,9.336861],[-9.795545,-4.990770,0.238072,-2.886088,8.599961,-7.669733,5.732036,7.613410,-0.274724,-8.589448],[-6.190283,-0.053339,5.209306,-3.844707,3.881066,7.980880,-4.572032,6.619582,2.360466,4.715255],[8.090442,3.361790,3.300939,-7.588158,0.469018,-7.301843,5.952172,-4.485040,-6.836096,-6.091247],[-2.271459,-7.467213,5.505637,7.621949,7.455355,0.148231,-3.886670,0.146839,0.821153,5.994206],[-8.802750,6.912268,2.521797,-8.620968,-2.711010,3.231832,-5.804037,9.236226,5.916472,-8.473019],[1.547679,-2.975798,-4.394729,6.253248,2.175296,4.777130,-5.579539,8.042507,-1.598153,0.167951]], dtype = "float32")#candidate|4503|(49, 10)|const|float32
bop_4504 = relay.bitwise_and(uop_4493.astype('int64'), relay.reshape(const_4503.astype('int64'), relay.shape_of(uop_4493))) # shape=(49, 10)
bop_4507 = relay.bitwise_and(uop_4495.astype('int64'), relay.reshape(const_4503.astype('int64'), relay.shape_of(uop_4495))) # shape=(49, 10)
var_4513 = relay.var("var_4513", dtype = "float32", shape = (49, 10))#candidate|4513|(49, 10)|var|float32
bop_4514 = relay.floor_mod(call_4480.astype('float64'), relay.reshape(var_4513.astype('float64'), relay.shape_of(call_4480))) # shape=(49, 10)
bop_4517 = relay.floor_mod(call_4482.astype('float64'), relay.reshape(var_4513.astype('float64'), relay.shape_of(call_4482))) # shape=(49, 10)
output = relay.Tuple([call_4476,var_4481,bop_4504,bop_4514,])
output2 = relay.Tuple([call_4477,var_4481,bop_4507,bop_4517,])
func_4526 = relay.Function([var_4481,var_4513,], output)
mod['func_4526'] = func_4526
mod = relay.transform.InferType()(mod)
mutated_mod['func_4526'] = func_4526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4526_call = mutated_mod.get_global_var('func_4526')
var_4528 = relay.var("var_4528", dtype = "uint16", shape = (672,))#candidate|4528|(672,)|var|uint16
var_4529 = relay.var("var_4529", dtype = "float32", shape = (49, 10))#candidate|4529|(49, 10)|var|float32
call_4527 = func_4526_call(var_4528,var_4529,)
output = call_4527
func_4530 = relay.Function([var_4528,var_4529,], output)
mutated_mod['func_4530'] = func_4530
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4532 = relay.var("var_4532", dtype = "int64", shape = (3, 7, 11))#candidate|4532|(3, 7, 11)|var|int64
var_4533 = relay.var("var_4533", dtype = "int64", shape = (3, 7, 11))#candidate|4533|(3, 7, 11)|var|int64
bop_4534 = relay.right_shift(var_4532.astype('int64'), relay.reshape(var_4533.astype('int64'), relay.shape_of(var_4532))) # shape=(3, 7, 11)
var_4542 = relay.var("var_4542", dtype = "int64", shape = (3, 7, 11))#candidate|4542|(3, 7, 11)|var|int64
bop_4543 = relay.greater_equal(var_4532.astype('bool'), relay.reshape(var_4542.astype('bool'), relay.shape_of(var_4532))) # shape=(3, 7, 11)
bop_4557 = relay.logical_xor(bop_4534.astype('int8'), relay.reshape(var_4533.astype('int8'), relay.shape_of(bop_4534))) # shape=(3, 7, 11)
bop_4563 = relay.maximum(var_4542.astype('int8'), relay.reshape(bop_4534.astype('int8'), relay.shape_of(var_4542))) # shape=(3, 7, 11)
uop_4570 = relay.rsqrt(bop_4543.astype('float32')) # shape=(3, 7, 11)
uop_4578 = relay.atan(var_4542.astype('float32')) # shape=(3, 7, 11)
func_4093_call = mod.get_global_var('func_4093')
func_4095_call = mutated_mod.get_global_var('func_4095')
call_4581 = relay.TupleGetItem(func_4093_call(), 0)
call_4582 = relay.TupleGetItem(func_4095_call(), 0)
bop_4608 = relay.mod(uop_4570.astype('float64'), relay.reshape(var_4542.astype('float64'), relay.shape_of(uop_4570))) # shape=(3, 7, 11)
func_1717_call = mod.get_global_var('func_1717')
func_1718_call = mutated_mod.get_global_var('func_1718')
call_4615 = func_1717_call()
call_4616 = func_1717_call()
output = relay.Tuple([bop_4557,bop_4563,uop_4578,call_4581,bop_4608,call_4615,])
output2 = relay.Tuple([bop_4557,bop_4563,uop_4578,call_4582,bop_4608,call_4616,])
func_4617 = relay.Function([var_4532,var_4533,var_4542,], output)
mod['func_4617'] = func_4617
mod = relay.transform.InferType()(mod)
var_4618 = relay.var("var_4618", dtype = "int64", shape = (3, 7, 11))#candidate|4618|(3, 7, 11)|var|int64
var_4619 = relay.var("var_4619", dtype = "int64", shape = (3, 7, 11))#candidate|4619|(3, 7, 11)|var|int64
var_4620 = relay.var("var_4620", dtype = "int64", shape = (3, 7, 11))#candidate|4620|(3, 7, 11)|var|int64
output = func_4617(var_4618,var_4619,var_4620,)
func_4621 = relay.Function([var_4618,var_4619,var_4620,], output)
mutated_mod['func_4621'] = func_4621
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4294_call = mod.get_global_var('func_4294')
func_4296_call = mutated_mod.get_global_var('func_4296')
call_4682 = relay.TupleGetItem(func_4294_call(), 0)
call_4683 = relay.TupleGetItem(func_4296_call(), 0)
func_971_call = mod.get_global_var('func_971')
func_973_call = mutated_mod.get_global_var('func_973')
call_4690 = relay.TupleGetItem(func_971_call(), 1)
call_4691 = relay.TupleGetItem(func_973_call(), 1)
output = relay.Tuple([call_4682,call_4690,])
output2 = relay.Tuple([call_4683,call_4691,])
func_4706 = relay.Function([], output)
mod['func_4706'] = func_4706
mod = relay.transform.InferType()(mod)
output = func_4706()
func_4707 = relay.Function([], output)
mutated_mod['func_4707'] = func_4707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1862_call = mod.get_global_var('func_1862')
func_1864_call = mutated_mod.get_global_var('func_1864')
call_4732 = relay.TupleGetItem(func_1862_call(), 3)
call_4733 = relay.TupleGetItem(func_1864_call(), 3)
const_4742 = relay.const([[10,-9,-6,-9,-9,-8,6,-3,-4]], dtype = "int64")#candidate|4742|(1, 9)|const|int64
bop_4743 = relay.not_equal(call_4732.astype('bool'), const_4742.astype('bool')) # shape=(1, 9)
bop_4746 = relay.not_equal(call_4733.astype('bool'), const_4742.astype('bool')) # shape=(1, 9)
func_4093_call = mod.get_global_var('func_4093')
func_4095_call = mutated_mod.get_global_var('func_4095')
call_4760 = relay.TupleGetItem(func_4093_call(), 2)
call_4761 = relay.TupleGetItem(func_4095_call(), 2)
uop_4763 = relay.sigmoid(const_4742.astype('float32')) # shape=(1, 9)
func_1255_call = mod.get_global_var('func_1255')
func_1256_call = mutated_mod.get_global_var('func_1256')
call_4776 = relay.TupleGetItem(func_1255_call(), 1)
call_4777 = relay.TupleGetItem(func_1256_call(), 1)
output = relay.Tuple([bop_4743,call_4760,uop_4763,call_4776,])
output2 = relay.Tuple([bop_4746,call_4761,uop_4763,call_4777,])
func_4804 = relay.Function([], output)
mod['func_4804'] = func_4804
mod = relay.transform.InferType()(mod)
output = func_4804()
func_4805 = relay.Function([], output)
mutated_mod['func_4805'] = func_4805
mutated_mod = relay.transform.InferType()(mutated_mod)
func_971_call = mod.get_global_var('func_971')
func_973_call = mutated_mod.get_global_var('func_973')
call_4830 = relay.TupleGetItem(func_971_call(), 0)
call_4831 = relay.TupleGetItem(func_973_call(), 0)
output = call_4830
output2 = call_4831
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
func_1308_call = mod.get_global_var('func_1308')
func_1310_call = mutated_mod.get_global_var('func_1310')
call_4909 = func_1308_call()
call_4910 = func_1308_call()
func_2376_call = mod.get_global_var('func_2376')
func_2377_call = mutated_mod.get_global_var('func_2377')
call_4982 = relay.TupleGetItem(func_2376_call(), 1)
call_4983 = relay.TupleGetItem(func_2377_call(), 1)
output = relay.Tuple([call_4909,call_4982,])
output2 = relay.Tuple([call_4910,call_4983,])
func_4992 = relay.Function([], output)
mod['func_4992'] = func_4992
mod = relay.transform.InferType()(mod)
mutated_mod['func_4992'] = func_4992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4992_call = mutated_mod.get_global_var('func_4992')
call_4993 = func_4992_call()
output = call_4993
func_4994 = relay.Function([], output)
mutated_mod['func_4994'] = func_4994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3386_call = mod.get_global_var('func_3386')
func_3388_call = mutated_mod.get_global_var('func_3388')
call_5008 = relay.TupleGetItem(func_3386_call(), 0)
call_5009 = relay.TupleGetItem(func_3388_call(), 0)
func_971_call = mod.get_global_var('func_971')
func_973_call = mutated_mod.get_global_var('func_973')
call_5018 = relay.TupleGetItem(func_971_call(), 0)
call_5019 = relay.TupleGetItem(func_973_call(), 0)
output = relay.Tuple([call_5008,call_5018,])
output2 = relay.Tuple([call_5009,call_5019,])
func_5032 = relay.Function([], output)
mod['func_5032'] = func_5032
mod = relay.transform.InferType()(mod)
output = func_5032()
func_5033 = relay.Function([], output)
mutated_mod['func_5033'] = func_5033
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5034 = relay.var("var_5034", dtype = "float64", shape = ())#candidate|5034|()|var|float64
var_5035 = relay.var("var_5035", dtype = "float64", shape = (11, 11, 11))#candidate|5035|(11, 11, 11)|var|float64
bop_5036 = relay.mod(var_5034.astype('float64'), var_5035.astype('float64')) # shape=(11, 11, 11)
func_4218_call = mod.get_global_var('func_4218')
func_4222_call = mutated_mod.get_global_var('func_4222')
const_5040 = relay.const([4,3,5,-2,9,-9,3,-4,-2,-10,-2,-2,7,6,-3,5,1,5,-9,-2,10,-3,-3,10,6,6,-9,6,-2,-8,-5,4,-8,-4,6,5,-1,-1,-5,-2,10,-8,-10,9,-7,9,-7,-10,2,3], dtype = "uint32")#candidate|5040|(50,)|const|uint32
call_5039 = func_4218_call(relay.reshape(var_5034.astype('uint32'), []), relay.reshape(const_5040.astype('uint32'), [5, 2, 5]), )
call_5041 = func_4218_call(relay.reshape(var_5034.astype('uint32'), []), relay.reshape(const_5040.astype('uint32'), [5, 2, 5]), )
func_2508_call = mod.get_global_var('func_2508')
func_2510_call = mutated_mod.get_global_var('func_2510')
var_5044 = relay.var("var_5044", dtype = "float64", shape = (490,))#candidate|5044|(490,)|var|float64
call_5043 = relay.TupleGetItem(func_2508_call(relay.reshape(var_5044.astype('float64'), [5, 14, 7])), 1)
call_5045 = relay.TupleGetItem(func_2510_call(relay.reshape(var_5044.astype('float64'), [5, 14, 7])), 1)
output = relay.Tuple([bop_5036,call_5039,const_5040,call_5043,var_5044,])
output2 = relay.Tuple([bop_5036,call_5041,const_5040,call_5045,var_5044,])
func_5051 = relay.Function([var_5034,var_5035,var_5044,], output)
mod['func_5051'] = func_5051
mod = relay.transform.InferType()(mod)
var_5052 = relay.var("var_5052", dtype = "float64", shape = ())#candidate|5052|()|var|float64
var_5053 = relay.var("var_5053", dtype = "float64", shape = (11, 11, 11))#candidate|5053|(11, 11, 11)|var|float64
var_5054 = relay.var("var_5054", dtype = "float64", shape = (490,))#candidate|5054|(490,)|var|float64
output = func_5051(var_5052,var_5053,var_5054,)
func_5055 = relay.Function([var_5052,var_5053,var_5054,], output)
mutated_mod['func_5055'] = func_5055
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5084 = relay.const([[[1.161108,6.478855,-6.514805,5.321088,9.707552,3.393219,-6.181170],[5.213421,-1.862039,9.562534,4.820470,6.647215,0.272727,-8.655977],[-4.827927,-5.702372,-3.491243,9.989799,4.161506,-4.166335,6.899589],[-5.333741,-4.909647,-6.058762,-4.305082,8.666619,9.035023,-8.313749],[-7.678893,-1.476328,-0.865167,-3.103802,-1.148412,3.483975,-6.331283],[-7.535080,3.922641,7.161860,-4.411780,-6.394883,-1.202462,-6.173502],[8.296080,-8.252567,6.237325,-4.715485,-3.587433,-7.884602,1.183698],[-5.132254,0.961259,8.214250,1.478756,-2.891996,1.266050,-7.763579],[-8.445751,3.814513,3.420377,-9.735409,-2.009845,0.225473,1.560499],[0.914980,9.048142,5.849550,-5.838149,-5.824948,9.021434,4.204917],[9.756978,-0.530536,-5.080766,7.760739,-2.143298,-3.594905,6.359187],[2.699950,1.615583,6.649944,-8.426168,3.862022,4.759341,-7.076805],[2.903720,5.477307,7.285007,-6.938511,-6.032858,-5.249223,9.663257],[4.748811,-3.413345,-9.589601,-4.280540,-3.924488,-4.148269,7.835726]],[[6.106904,-1.671081,-9.875988,-5.615739,-1.537675,5.583946,-9.883050],[4.173605,1.765151,-0.834227,7.245585,5.093049,-6.768102,-2.408669],[-2.348821,8.175372,1.893482,-6.266848,0.288725,5.115869,3.844047],[-8.296575,-1.224928,-2.064335,5.531526,9.295925,7.794350,-6.668723],[4.294288,-9.172364,-1.236119,9.862159,1.410082,6.703193,-9.030419],[-8.051818,-4.264529,-9.720960,-9.970686,-5.135818,4.648212,-2.338787],[-6.319792,9.547927,2.674846,3.508316,2.267567,2.705365,-3.795972],[3.683549,-7.930401,6.404186,0.026539,9.626584,-1.725782,7.740752],[-2.280293,-5.480577,-9.530208,-4.655569,9.514759,4.893611,-6.319770],[8.374770,-3.633976,-7.452352,9.243674,9.098066,3.839998,-0.348627],[-3.241648,9.194410,-5.248478,9.806363,5.930735,-8.861243,-6.766817],[3.160631,3.393478,8.544277,-6.592528,-3.501267,8.466088,-8.047511],[-3.553366,-0.071355,-2.335317,3.279222,5.592765,0.499694,-5.008687],[4.126389,2.663624,-5.716396,-1.523052,-5.658771,2.154757,-5.951791]],[[-7.619529,2.780809,2.178044,3.943235,4.772033,-6.438570,-1.233142],[-8.258715,-9.695371,4.456743,-6.935718,-8.328589,0.449092,0.465843],[2.405404,-3.504402,-2.558532,-4.051203,6.409502,6.521280,4.942458],[-8.150834,9.839067,-2.305173,-5.236118,-5.844345,8.563292,4.874697],[8.761498,1.430744,-7.837518,5.398141,9.701305,8.892639,5.501089],[-8.512887,-6.768545,-5.630572,2.530641,0.659018,-4.900107,-1.955419],[-4.438865,6.949789,3.669924,-8.902503,-0.436301,-9.990633,-6.347975],[-8.882561,9.536280,-6.216499,0.124912,0.590511,8.896566,0.387277],[-1.598806,-8.771631,2.466518,4.343000,-8.275973,4.153800,7.556648],[1.623428,3.348326,6.601281,-1.327016,-8.096319,4.930876,-2.788042],[2.163485,-5.657754,4.588685,-5.613808,-7.797166,6.698287,-0.417666],[0.869000,5.281221,0.229734,6.088025,6.966262,-3.944841,8.394853],[6.643778,-2.971318,4.594796,7.635683,2.289726,-8.696666,7.016380],[3.342802,-8.933801,7.615535,5.114687,-5.858200,7.249495,-6.636689]],[[2.308991,9.583612,1.203131,4.685289,7.164359,1.652441,5.553555],[-1.729741,-6.440137,-1.087582,1.661551,-2.060077,-3.419843,0.593372],[-5.622776,6.844129,4.540691,-8.766772,-9.492726,-8.326900,-4.458051],[0.210262,9.989945,-6.228954,7.440345,-7.129444,-4.530936,6.711081],[3.035495,0.525438,-4.775742,8.724909,9.327089,-0.022590,-8.890755],[5.141651,-2.838691,-0.139400,0.604261,5.398705,8.288363,6.026309],[-3.382726,-5.927496,9.141013,0.117569,-4.118229,6.933499,8.710327],[8.016117,-5.778672,-2.547107,9.627345,-9.761372,-1.464193,0.422531],[1.771561,9.138707,0.035688,4.437380,7.463947,-0.148550,-1.237781],[-0.465225,2.185318,2.405569,-9.248808,8.405414,-1.546607,-8.996975],[1.477118,-9.747312,-7.628909,7.952744,1.811712,-2.185959,1.275908],[-2.274522,7.858112,6.881490,-6.127259,-0.791008,5.728679,8.672004],[-9.817003,-2.900280,3.855242,-7.929441,-1.576205,-4.133244,2.153874],[5.487436,0.335049,-8.866841,-2.319575,-9.068564,-7.641107,0.963558]],[[-2.037236,4.399178,4.474172,-2.617214,-1.616005,-0.284848,-1.185019],[-9.289697,-0.967902,3.008725,4.966303,-4.069736,3.099751,-6.606348],[0.013926,7.597490,-0.287630,-6.982054,-2.543051,9.110100,-0.454826],[-8.943917,-0.880918,-1.787581,-7.879871,-4.394498,9.651102,3.552606],[3.684523,-0.414753,5.469428,-2.576884,-0.143447,6.288980,-0.041997],[9.791981,1.268364,3.326070,-0.689477,-2.833260,8.160374,-4.438683],[1.547407,-0.284309,2.533655,5.041951,-4.329328,5.860754,5.678206],[-4.804132,9.359574,-7.937996,6.649561,-0.643230,5.449435,-5.352496],[0.588473,7.011008,-4.779762,-7.438242,-4.020942,-1.520982,2.855415],[9.953781,8.135280,-6.324540,1.103653,7.604021,1.025270,-3.661044],[-2.345308,5.305795,7.853459,-3.388880,-7.719831,9.869660,-1.686437],[-1.096554,1.536630,-2.630376,4.473467,5.936505,7.462796,5.415480],[-4.162155,9.367685,-6.786321,2.119704,3.595342,8.552527,-3.512876],[-0.672009,-9.322006,-5.918383,-1.847786,-0.506357,-2.124827,-5.689156]],[[-6.685165,-5.601024,7.546040,1.707425,-2.152441,5.407894,-3.769725],[-2.971394,-6.246391,-6.736615,9.595872,-0.321180,9.455221,3.493207],[7.217582,-7.851218,0.230900,-7.085036,-1.545819,-1.983446,-2.538576],[4.978014,-7.248467,1.430278,-6.866176,6.872370,4.677891,-0.499748],[8.942327,-3.557198,2.224990,-9.997541,5.121553,-2.902283,7.322524],[-1.905742,-6.483737,-4.850997,3.872757,7.133954,7.025453,7.768791],[3.428600,-2.209849,2.924632,7.313948,9.360595,6.563942,-1.487259],[-7.478120,-8.460323,-4.510622,-4.502019,7.773003,-3.416986,-2.496486],[-2.584142,-5.646862,1.008757,-9.275864,3.892011,6.165274,2.246057],[6.208163,-7.141587,7.079987,2.903352,-3.764614,4.925801,2.194658],[-1.325516,4.655012,-1.227753,-5.051269,-2.628408,-4.362161,-9.218883],[-8.996159,7.938573,-2.951769,-5.229363,-0.269945,3.672679,0.396713],[5.039825,-8.808902,-4.343945,-2.399082,-6.153158,-6.104901,8.140142],[-5.398042,5.955219,3.386697,2.432036,-5.349956,-1.472064,5.631288]],[[2.598917,-0.216593,9.861350,5.392123,-8.898252,-4.261746,-0.661894],[-2.285822,-7.184197,-3.825060,9.018038,-9.002825,5.827486,-5.857142],[1.860341,1.729449,9.252385,4.435900,-8.956079,-2.113608,-4.214602],[7.811365,-4.917551,-6.054277,8.781049,-5.431652,7.030629,0.922376],[9.518721,-5.848151,0.418394,-0.256916,5.146276,6.938487,-8.189202],[-9.313435,5.591983,8.972652,8.431028,-1.693350,-2.850151,-3.681526],[5.667821,-8.442287,2.763403,4.352299,-0.851559,1.094197,-4.393471],[-7.333913,1.467712,5.326988,-9.478430,-7.720167,6.149202,-8.309060],[3.517517,5.725992,-9.372848,9.659115,-3.676217,-2.970777,-7.449927],[-3.816900,1.401806,0.085897,9.358070,8.855993,-9.687597,-0.672673],[-8.930174,9.324270,2.145084,-9.630557,7.372146,7.030504,-2.731673],[-4.176130,-6.048178,9.329375,1.657346,-2.658190,-7.986465,7.323265],[6.027922,-7.995513,-3.196552,6.336737,-5.438626,-3.434567,9.409812],[4.401172,3.381723,9.026146,-7.474609,3.087089,7.291925,-7.990436]],[[7.308599,-6.232104,3.060366,-3.415019,3.523485,0.728810,4.033886],[7.220428,-6.546314,0.876701,-6.903192,0.346737,7.710989,5.964464],[-2.598896,-5.532514,1.854337,-7.576376,6.268074,-4.046531,-7.544900],[-5.768700,8.352813,-8.572953,-4.305649,-7.981340,-0.080357,2.879557],[-9.010076,3.317897,9.979998,0.812215,-2.983309,5.186694,-0.474396],[-6.326136,-8.254126,6.867273,-9.584228,8.223727,5.077570,-1.812335],[6.251432,6.526805,-7.821000,-4.988746,3.370900,-8.855843,9.679578],[0.561733,6.775006,-4.602837,1.170085,-2.433257,3.906610,-1.372134],[0.139300,3.856684,4.717366,-7.305493,4.688004,4.994140,-8.119276],[-2.804641,4.478546,-0.728595,-6.031456,-9.887305,-5.556782,0.056207],[-0.519234,-9.644476,-9.074574,-4.411838,-6.333315,7.312029,7.590303],[-6.323781,-1.889466,6.955606,7.115881,2.096871,-4.027947,8.713327],[-3.889356,4.421139,-4.197399,-7.685960,6.894482,-8.874298,5.712867],[7.567238,-5.565350,5.087266,-4.626396,2.261168,-0.248556,2.809914]]], dtype = "float64")#candidate|5084|(8, 14, 7)|const|float64
uop_5085 = relay.erf(const_5084.astype('float64')) # shape=(8, 14, 7)
var_5089 = relay.var("var_5089", dtype = "float64", shape = (8, 14, 7))#candidate|5089|(8, 14, 7)|var|float64
bop_5090 = relay.divide(uop_5085.astype('float32'), relay.reshape(var_5089.astype('float32'), relay.shape_of(uop_5085))) # shape=(8, 14, 7)
bop_5096 = relay.bitwise_or(bop_5090.astype('uint64'), relay.reshape(const_5084.astype('uint64'), relay.shape_of(bop_5090))) # shape=(8, 14, 7)
bop_5100 = relay.greater_equal(var_5089.astype('bool'), relay.reshape(uop_5085.astype('bool'), relay.shape_of(var_5089))) # shape=(8, 14, 7)
bop_5104 = relay.bitwise_and(bop_5090.astype('uint64'), relay.reshape(var_5089.astype('uint64'), relay.shape_of(bop_5090))) # shape=(8, 14, 7)
func_1862_call = mod.get_global_var('func_1862')
func_1864_call = mutated_mod.get_global_var('func_1864')
call_5119 = relay.TupleGetItem(func_1862_call(), 1)
call_5120 = relay.TupleGetItem(func_1864_call(), 1)
func_2807_call = mod.get_global_var('func_2807')
func_2810_call = mutated_mod.get_global_var('func_2810')
const_5122 = relay.const([False,True,False,False,True,True,True,True,True,True,False,False,True,False,False,True,False,True,False,True,False,False,True,False,True,True,False,False,False,False,True,False,True,True,True,False,False,False,False,True,True,False,True,False,False,False,False,False,True,False,False,False,False,True,False,False,True,False,False,True,True,True,False,False,False,True,True,False,True,True,False,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,False,True,False,True,False,True,True,True,False,False,False,False,True,True,False,False,False,False,True,True,True,False,False,False,True,False,True,False,True,False,False,True,False,False,False,False,True,False,True,True,False,True,False,False,False,False,False,False], dtype = "bool")#candidate|5122|(135,)|const|bool
const_5123 = relay.const([[False,True,False,False,False,False,False,False,True,False,False,False,False,False,False,True,False,False,False,True,True,False,True,True,False,False,True,True,False,False,False,False,True,False,True,True,False,True,True,True,True,False,True,False,False,False,True,False,False,True,False,True,True,True,False,False,True,True,True,False,True,True,False,False,False,True,True,False,False,True,False,False,True,True,False,True,True,True,False,False,False,False,True,False,True,False,False,True,True,True,True,True,False,True,True,False,True,True,True,True,False,True,True,True,False,True,False,False,False,False,False,True,False,True,True,False,True,True,True,True,False,False,False,False,True,True,True,False,False,False,False,False,True,True,True,True,True,False,True,True,False,True,False,True,True,True,True,False,False,False,True,False,False,True,True,True,True,False,False,True,False,False,False,True,True,True,False,False,True,False,False,False,True,False,True,False,False,False,True,False,False,False,True,False,False,False,True,True,False,True,False,False,True,False,True,True,False,True,True,True,True,True,True,True,False,False,True,False,False,False,False,False,True,True,False,True,True,False,False,True,True,False,True,True,True,False,False,True,False,True,False,True,True,False,False,True,False,False,True,True,False,True,True,True,True,False,False,False,False,False,False,True,True,True,False,False,False,False,True,False,False,True,True,True,True,False,False,False,False,True,True,False,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,True,True,True,True,True,False,True,False,False,True,False,False,True,True,True,True,True,True,True,True,False,False,True,False,True,True,False,True,False,True,True,False,False,False,True,True,False,False,True,False,True,True,False,False,False,True,False,True,True,True,False,True,True,True,True,False,False,False,True,True,True,False,True,True],[False,False,False,True,True,True,True,False,False,False,True,False,True,True,True,False,False,False,True,False,True,True,False,False,True,False,True,False,False,False,True,True,False,True,False,True,False,True,False,False,True,True,False,True,False,True,True,False,True,True,False,True,False,True,True,True,True,False,True,True,False,False,False,False,True,False,False,True,False,False,True,True,True,True,False,True,False,False,True,False,True,False,True,True,True,False,False,False,False,True,True,False,True,False,False,False,False,False,True,False,False,False,False,True,True,False,False,True,False,False,True,True,False,False,False,True,False,False,True,False,True,False,False,False,False,True,False,True,True,True,True,False,True,True,True,False,False,False,False,False,False,True,False,False,False,False,True,False,True,False,True,False,False,True,True,True,False,True,False,False,True,True,False,False,True,True,True,True,True,True,True,True,False,True,True,False,False,False,True,True,False,False,True,True,True,False,False,False,False,False,False,True,True,False,True,False,True,False,True,True,True,True,False,False,False,False,False,False,False,True,True,True,True,True,False,True,True,False,True,True,False,True,False,True,True,False,False,False,False,True,True,False,False,False,False,True,False,False,True,False,False,True,True,True,False,True,False,True,True,True,True,True,False,True,True,True,True,True,False,False,False,True,False,True,True,False,False,True,False,True,False,False,False,True,False,False,True,False,False,False,False,True,False,False,False,True,False,False,False,False,False,False,True,False,True,True,False,True,False,False,True,False,True,True,False,True,False,True,True,False,True,True,True,True,False,True,False,False,True,False,False,True,True,True,True,False,False,True,False,True,False,True,True,True,False,True,False,False,False,True,False,False,True,True,True,True,True,False,True,False,False],[True,False,True,False,True,False,True,True,False,False,True,True,True,False,True,True,False,False,True,True,False,True,False,False,True,True,True,True,False,True,True,True,True,True,False,True,True,True,False,True,True,True,False,False,True,True,True,True,True,True,False,False,False,True,False,True,False,True,False,True,False,False,False,False,True,False,True,False,True,True,True,False,False,True,True,True,False,False,False,False,True,False,False,False,True,False,True,False,True,False,True,True,False,True,True,True,False,False,True,True,True,False,False,True,True,True,False,True,True,False,True,True,True,True,True,False,True,False,False,False,False,True,False,False,True,True,True,True,False,False,False,True,False,False,True,True,True,True,True,True,False,False,False,True,False,True,True,True,True,False,False,False,True,False,False,False,True,False,True,True,False,False,True,True,False,False,False,False,True,True,True,True,False,True,False,False,False,False,True,True,False,True,True,True,True,False,False,True,False,True,False,False,True,True,True,False,True,False,False,True,True,True,False,True,False,True,True,False,True,True,True,True,False,True,False,False,True,False,True,True,False,True,True,True,True,True,True,False,True,True,True,False,False,False,False,False,True,True,False,False,False,False,True,True,True,True,True,False,False,False,True,False,True,False,True,False,True,True,True,False,False,False,True,True,False,True,True,True,False,False,True,True,False,False,False,True,False,True,True,False,True,False,False,False,False,True,True,False,False,False,False,True,False,True,False,True,False,True,False,True,True,False,False,True,False,False,False,False,True,True,False,False,True,False,False,False,False,True,False,False,True,False,True,False,False,True,True,False,True,True,True,False,True,True,False,False,True,False,False,False,False,True,False,True,True,True,True,True,False,True,False],[False,False,True,False,False,True,True,False,False,False,False,False,False,True,False,False,True,True,False,True,True,True,False,False,True,True,False,False,True,True,False,True,True,False,True,True,True,False,False,True,True,False,True,True,True,False,True,False,True,True,False,False,True,False,False,False,True,False,False,False,False,True,False,True,True,True,True,False,False,True,True,True,True,False,False,False,False,True,True,True,False,True,True,True,True,False,True,False,False,False,False,False,True,False,False,False,False,True,False,False,False,True,True,True,True,True,True,False,False,False,True,False,True,True,False,False,True,True,False,True,True,True,False,False,True,False,False,True,True,False,True,True,True,False,False,True,True,True,True,True,False,False,False,True,True,False,False,False,True,False,False,True,True,False,True,True,False,False,False,True,False,False,False,False,False,False,True,False,True,False,True,True,False,True,True,False,True,True,False,True,True,False,False,True,False,True,False,False,True,False,True,False,False,True,False,True,True,True,True,True,True,False,False,True,False,True,True,True,False,False,False,False,False,False,True,True,False,True,True,True,True,True,True,False,False,True,True,False,False,False,True,True,False,True,True,False,True,False,False,True,False,False,True,True,True,False,False,True,True,True,False,True,False,False,True,True,True,False,True,False,False,False,True,False,True,False,True,False,True,True,False,True,True,True,False,False,False,False,True,True,False,False,False,False,False,True,True,True,True,False,True,True,False,True,False,False,True,True,False,False,False,False,False,True,False,False,False,False,True,True,True,True,True,False,True,True,True,True,True,True,True,False,False,False,True,False,False,True,True,False,True,True,True,True,True,True,False,True,True,True,False,False,False,False,False,True,True,False,False,False,True],[False,True,True,False,False,False,False,True,True,False,True,True,True,False,False,False,False,True,True,True,True,False,True,True,False,True,True,False,True,True,True,True,False,True,True,True,True,True,False,False,False,True,True,True,False,True,False,False,False,True,False,False,True,True,True,False,False,False,False,False,False,False,True,False,True,True,True,False,False,False,False,False,True,False,False,True,True,False,False,False,True,False,False,True,True,True,True,False,False,True,False,False,True,True,False,False,False,False,False,True,False,True,True,True,True,True,True,False,True,True,False,True,True,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,True,True,False,False,True,False,True,False,True,True,False,False,False,True,True,False,True,True,False,False,False,False,False,False,False,False,False,True,True,True,True,False,False,False,False,True,False,True,False,True,False,False,True,False,True,False,True,False,True,True,False,True,False,False,False,False,True,False,True,False,True,True,False,False,True,False,True,True,True,True,False,True,True,True,False,False,True,True,False,False,False,False,False,False,True,False,True,False,False,False,False,False,True,False,False,False,False,True,True,True,True,True,False,False,False,False,True,True,True,True,False,False,False,False,False,True,False,True,True,False,False,True,False,True,True,False,False,True,False,True,False,True,True,False,True,True,True,False,True,False,False,True,False,False,True,True,True,True,False,False,True,False,True,False,False,False,False,False,True,False,True,True,True,False,True,True,False,False,True,True,True,True,False,True,True,True,False,False,False,True,False,True,True,True,True,True,True,False,True,False,False,True,True,False,True,True,True,True,True,False,False,False,False,False,False,True,True,False,False,True,True,False,True,True,False,False,False,True,False,False,False,True]], dtype = "bool")#candidate|5123|(5, 351)|const|bool
call_5121 = relay.TupleGetItem(func_2807_call(relay.reshape(const_5122.astype('bool'), [9, 1, 15]), relay.reshape(const_5123.astype('bool'), [9, 13, 15]), ), 0)
call_5124 = relay.TupleGetItem(func_2810_call(relay.reshape(const_5122.astype('bool'), [9, 1, 15]), relay.reshape(const_5123.astype('bool'), [9, 13, 15]), ), 0)
output = relay.Tuple([bop_5096,bop_5100,bop_5104,call_5119,call_5121,const_5122,const_5123,])
output2 = relay.Tuple([bop_5096,bop_5100,bop_5104,call_5120,call_5124,const_5122,const_5123,])
func_5132 = relay.Function([var_5089,], output)
mod['func_5132'] = func_5132
mod = relay.transform.InferType()(mod)
var_5133 = relay.var("var_5133", dtype = "float64", shape = (8, 14, 7))#candidate|5133|(8, 14, 7)|var|float64
output = func_5132(var_5133)
func_5134 = relay.Function([var_5133], output)
mutated_mod['func_5134'] = func_5134
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5145 = relay.var("var_5145", dtype = "float32", shape = ())#candidate|5145|()|var|float32
var_5146 = relay.var("var_5146", dtype = "float32", shape = (15, 9, 6))#candidate|5146|(15, 9, 6)|var|float32
bop_5147 = relay.power(var_5145.astype('float32'), var_5146.astype('float32')) # shape=(15, 9, 6)
func_3250_call = mod.get_global_var('func_3250')
func_3253_call = mutated_mod.get_global_var('func_3253')
call_5165 = relay.TupleGetItem(func_3250_call(relay.reshape(var_5145.astype('int64'), [])), 6)
call_5166 = relay.TupleGetItem(func_3253_call(relay.reshape(var_5145.astype('int64'), [])), 6)
func_1488_call = mod.get_global_var('func_1488')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_5169 = func_1488_call()
call_5170 = func_1488_call()
output = relay.Tuple([bop_5147,call_5165,call_5169,])
output2 = relay.Tuple([bop_5147,call_5166,call_5170,])
func_5173 = relay.Function([var_5145,var_5146,], output)
mod['func_5173'] = func_5173
mod = relay.transform.InferType()(mod)
var_5174 = relay.var("var_5174", dtype = "float32", shape = ())#candidate|5174|()|var|float32
var_5175 = relay.var("var_5175", dtype = "float32", shape = (15, 9, 6))#candidate|5175|(15, 9, 6)|var|float32
output = func_5173(var_5174,var_5175,)
func_5176 = relay.Function([var_5174,var_5175,], output)
mutated_mod['func_5176'] = func_5176
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2523_call = mod.get_global_var('func_2523')
func_2525_call = mutated_mod.get_global_var('func_2525')
call_5203 = func_2523_call()
call_5204 = func_2523_call()
output = relay.Tuple([call_5203,])
output2 = relay.Tuple([call_5204,])
func_5205 = relay.Function([], output)
mod['func_5205'] = func_5205
mod = relay.transform.InferType()(mod)
output = func_5205()
func_5206 = relay.Function([], output)
mutated_mod['func_5206'] = func_5206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3933_call = mod.get_global_var('func_3933')
func_3935_call = mutated_mod.get_global_var('func_3935')
call_5217 = relay.TupleGetItem(func_3933_call(), 0)
call_5218 = relay.TupleGetItem(func_3935_call(), 0)
func_1110_call = mod.get_global_var('func_1110')
func_1113_call = mutated_mod.get_global_var('func_1113')
var_5220 = relay.var("var_5220", dtype = "int64", shape = ())#candidate|5220|()|var|int64
call_5219 = relay.TupleGetItem(func_1110_call(relay.reshape(var_5220.astype('int64'), []), relay.reshape(call_5217.astype('float64'), [1, 140]), ), 3)
call_5221 = relay.TupleGetItem(func_1113_call(relay.reshape(var_5220.astype('int64'), []), relay.reshape(call_5217.astype('float64'), [1, 140]), ), 3)
func_3386_call = mod.get_global_var('func_3386')
func_3388_call = mutated_mod.get_global_var('func_3388')
call_5229 = relay.TupleGetItem(func_3386_call(), 0)
call_5230 = relay.TupleGetItem(func_3388_call(), 0)
output = relay.Tuple([call_5217,call_5219,var_5220,call_5229,])
output2 = relay.Tuple([call_5218,call_5221,var_5220,call_5230,])
func_5237 = relay.Function([var_5220,], output)
mod['func_5237'] = func_5237
mod = relay.transform.InferType()(mod)
mutated_mod['func_5237'] = func_5237
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5238 = relay.var("var_5238", dtype = "int64", shape = ())#candidate|5238|()|var|int64
func_5237_call = mutated_mod.get_global_var('func_5237')
call_5239 = func_5237_call(var_5238)
output = call_5239
func_5240 = relay.Function([var_5238], output)
mutated_mod['func_5240'] = func_5240
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5250 = relay.var("var_5250", dtype = "float32", shape = (4, 2, 15))#candidate|5250|(4, 2, 15)|var|float32
uop_5251 = relay.asinh(var_5250.astype('float32')) # shape=(4, 2, 15)
func_2680_call = mod.get_global_var('func_2680')
func_2683_call = mutated_mod.get_global_var('func_2683')
var_5254 = relay.var("var_5254", dtype = "float32", shape = (12,))#candidate|5254|(12,)|var|float32
const_5255 = relay.const(6, dtype = "int64")#candidate|5255|()|const|int64
call_5253 = relay.TupleGetItem(func_2680_call(relay.reshape(var_5254.astype('float32'), [12,]), relay.reshape(const_5255.astype('int64'), []), ), 0)
call_5256 = relay.TupleGetItem(func_2683_call(relay.reshape(var_5254.astype('float32'), [12,]), relay.reshape(const_5255.astype('int64'), []), ), 0)
func_1070_call = mod.get_global_var('func_1070')
func_1072_call = mutated_mod.get_global_var('func_1072')
call_5257 = relay.TupleGetItem(func_1070_call(relay.reshape(call_5253.astype('float64'), [10, 7, 2])), 1)
call_5258 = relay.TupleGetItem(func_1072_call(relay.reshape(call_5253.astype('float64'), [10, 7, 2])), 1)
uop_5262 = relay.acos(uop_5251.astype('float64')) # shape=(4, 2, 15)
bop_5264 = relay.divide(uop_5262.astype('float32'), relay.reshape(uop_5251.astype('float32'), relay.shape_of(uop_5262))) # shape=(4, 2, 15)
uop_5269 = relay.cos(uop_5262.astype('float64')) # shape=(4, 2, 15)
uop_5272 = relay.sinh(uop_5269.astype('float32')) # shape=(4, 2, 15)
bop_5276 = relay.logical_or(uop_5272.astype('bool'), relay.reshape(uop_5269.astype('bool'), relay.shape_of(uop_5272))) # shape=(4, 2, 15)
func_2428_call = mod.get_global_var('func_2428')
func_2430_call = mutated_mod.get_global_var('func_2430')
call_5299 = func_2428_call()
call_5300 = func_2428_call()
var_5310 = relay.var("var_5310", dtype = "bool", shape = (4, 2, 15))#candidate|5310|(4, 2, 15)|var|bool
bop_5311 = relay.bitwise_xor(bop_5276.astype('uint8'), relay.reshape(var_5310.astype('uint8'), relay.shape_of(bop_5276))) # shape=(4, 2, 15)
output = relay.Tuple([call_5253,var_5254,const_5255,call_5257,bop_5264,call_5299,bop_5311,])
output2 = relay.Tuple([call_5256,var_5254,const_5255,call_5258,bop_5264,call_5300,bop_5311,])
func_5325 = relay.Function([var_5250,var_5254,var_5310,], output)
mod['func_5325'] = func_5325
mod = relay.transform.InferType()(mod)
var_5326 = relay.var("var_5326", dtype = "float32", shape = (4, 2, 15))#candidate|5326|(4, 2, 15)|var|float32
var_5327 = relay.var("var_5327", dtype = "float32", shape = (12,))#candidate|5327|(12,)|var|float32
var_5328 = relay.var("var_5328", dtype = "bool", shape = (4, 2, 15))#candidate|5328|(4, 2, 15)|var|bool
output = func_5325(var_5326,var_5327,var_5328,)
func_5329 = relay.Function([var_5326,var_5327,var_5328,], output)
mutated_mod['func_5329'] = func_5329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1717_call = mod.get_global_var('func_1717')
func_1718_call = mutated_mod.get_global_var('func_1718')
call_5403 = func_1717_call()
call_5404 = func_1717_call()
func_4706_call = mod.get_global_var('func_4706')
func_4707_call = mutated_mod.get_global_var('func_4707')
call_5407 = relay.TupleGetItem(func_4706_call(), 1)
call_5408 = relay.TupleGetItem(func_4707_call(), 1)
func_3118_call = mod.get_global_var('func_3118')
func_3120_call = mutated_mod.get_global_var('func_3120')
const_5410 = relay.const([-5.843002,-4.202441,3.121865,7.655861,5.869661,-2.102712,9.803983,3.760624,7.324217,5.876424,2.888416,1.318650,2.660431,-1.934960,-8.228767,4.358651,0.633871,3.756691,-0.153534,-3.347171,-0.770402,-8.848327,1.906895,-8.523115,1.950486,-4.682009,4.608164,-0.690526,9.341291,2.704721,-5.957577,-9.613683,-7.667706,-0.582292,5.107157,-2.813971,7.086596,8.688322,8.248434,1.402389,3.129282,6.307066,6.963090,0.067648,-5.296839,-3.429135,8.631491,-0.902344,3.631057,-0.483618,7.352122,-2.555994,3.470917,0.707198,8.437601,-2.571419,-7.621450,0.739875,3.561497,3.811017,8.765150,-5.114802,-3.713446,5.365307,-0.560118,-0.980020,-9.720799,-2.108371,-5.748851,-0.331001,3.413961,-8.326152,-1.768133,5.932653,-7.990350,-1.112132,9.807520,9.149994,4.061168,1.338922,-9.367393,-7.678735,-2.553715,9.464004,-0.663111,5.529167,-2.072090,-9.198194,8.741728,-8.582802,-1.530078,-4.611046,-5.644151,4.891993,-6.941207,4.440037,4.448208,1.353179,-7.988191,-6.054124,5.297713,-1.724214,-4.160543,-6.753101,5.715429,6.474992,3.514874,5.852249,8.954795,-2.543437,8.966624,1.846721,1.127525,-9.449120,0.177348,-9.731325,-3.267308,-1.487910,6.720737,9.860379,4.540494,-0.219917,-0.563188,-6.048915,8.379068,1.741910,-8.208316,6.019171,5.974897,-5.201242,-9.528604,0.173245,2.310686,0.970656,8.141768,0.824392,-2.847832,3.028265,3.080767,-0.790563,-0.886423,1.537676,-5.681627,-7.448345,4.721624,-5.669962,-6.289557,-9.115885,6.847906,-5.478169,-9.069569,-5.391290,-0.189629,8.265180,7.401709,-3.536511,5.358433,5.570508,-6.104246,-3.402010], dtype = "float64")#candidate|5410|(160,)|const|float64
call_5409 = relay.TupleGetItem(func_3118_call(relay.reshape(const_5410.astype('float64'), [16, 5, 2])), 1)
call_5411 = relay.TupleGetItem(func_3120_call(relay.reshape(const_5410.astype('float64'), [16, 5, 2])), 1)
output = relay.Tuple([call_5403,call_5407,call_5409,const_5410,])
output2 = relay.Tuple([call_5404,call_5408,call_5411,const_5410,])
func_5413 = relay.Function([], output)
mod['func_5413'] = func_5413
mod = relay.transform.InferType()(mod)
output = func_5413()
func_5414 = relay.Function([], output)
mutated_mod['func_5414'] = func_5414
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5441 = relay.var("var_5441", dtype = "float64", shape = (8, 4, 2))#candidate|5441|(8, 4, 2)|var|float64
uop_5442 = relay.cos(var_5441.astype('float64')) # shape=(8, 4, 2)
func_1308_call = mod.get_global_var('func_1308')
func_1310_call = mutated_mod.get_global_var('func_1310')
call_5448 = func_1308_call()
call_5449 = func_1308_call()
var_5454 = relay.var("var_5454", dtype = "float64", shape = (8, 4, 2))#candidate|5454|(8, 4, 2)|var|float64
bop_5455 = relay.greater_equal(uop_5442.astype('bool'), relay.reshape(var_5454.astype('bool'), relay.shape_of(uop_5442))) # shape=(8, 4, 2)
output = relay.Tuple([call_5448,bop_5455,])
output2 = relay.Tuple([call_5449,bop_5455,])
func_5461 = relay.Function([var_5441,var_5454,], output)
mod['func_5461'] = func_5461
mod = relay.transform.InferType()(mod)
mutated_mod['func_5461'] = func_5461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5461_call = mutated_mod.get_global_var('func_5461')
var_5463 = relay.var("var_5463", dtype = "float64", shape = (8, 4, 2))#candidate|5463|(8, 4, 2)|var|float64
var_5464 = relay.var("var_5464", dtype = "float64", shape = (8, 4, 2))#candidate|5464|(8, 4, 2)|var|float64
call_5462 = func_5461_call(var_5463,var_5464,)
output = call_5462
func_5465 = relay.Function([var_5463,var_5464,], output)
mutated_mod['func_5465'] = func_5465
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1754_call = mod.get_global_var('func_1754')
func_1756_call = mutated_mod.get_global_var('func_1756')
call_5499 = relay.TupleGetItem(func_1754_call(), 2)
call_5500 = relay.TupleGetItem(func_1756_call(), 2)
uop_5501 = relay.acosh(call_5499.astype('float32')) # shape=(10, 7, 2)
uop_5503 = relay.acosh(call_5500.astype('float32')) # shape=(10, 7, 2)
func_4526_call = mod.get_global_var('func_4526')
func_4530_call = mutated_mod.get_global_var('func_4530')
const_5505 = relay.const([-7,6,-7,10,-2,-5,-6,-6,-3,-5,-1,-5,5,-3,6,-2,-7,8,1,-4,-9,-7,6,-3,8,-5,-2,-1,-6,10,10,-6,4,-1,-4,-10,-3,-7,2,-8,-8,7,-3,9,-3,-3,2,-10,-5,-3,-5,9,2,7,-8,4,9,-5,2,-2,-4,-9,-6,3,1,10,1,-6,-7,-6,-7,10,2,8,1,10,-9,-2,-10,-8,-2,-7,-10,-7,5,4,2,7,1,-9,-7,10,7,-1,-8,8,-7,-7,9,6,7,-5,3,-4,-9,-1,-3,-2,-4,9,-4,-5,1,8,6,-3,3,2,2,-2,-1,9,5,-6,8,4,2,3,-1,-3,-6,-2,6,6,-1,1,3,-10,5,9,1,5,3,7,2,3,-8,-8,-10,-4,-3,7,-7,4,2,7,-7,7,2,-3,5,4,-2,10,7,5,7,7,8,7,-7,1,7,-3,1,-5,4,2,2,-8,-3,10,-4,5,-10,-1,-7,10,-2,6,9,-2,3,-8,3,5,-10,6,-1,5,-5,8,-9,-7,1,4,5,4,-9,2,-10,-8,3,6,6,5,10,-5,-2,-1,6,-5,-3,-8,3,4,8,-6,7,4,5,-7,5,-5,-4,1,2,-10,5,7,7,-1,-3,-7,3,6,-3,5,6,-4,-6,2,-1,5,8,3,-5,-4,3,1,-3,6,-1,-1,-10,-9,9,8,-2,5,-7,7,3,2,-3,4,9,1,8,7,8,-6,-7,-7,9,9,10,-10,9,1,-5,7,2,4,-1,-9,8,6,-2,-4,-6,-9,-3,9,10,-6,-2,9,-3,7,-5,-3,-6,10,-3,-10,-9,5,-7,6,4,-4,-4,-2,5,1,8,5,-4,-1,-9,-7,-10,-10,7,-8,-7,7,3,-10,-1,-10,-6,2,-10,-8,5,-9,8,-6,7,-5,-6,8,4,-10,9,-7,-7,-5,-3,9,-8,5,-10,-2,4,-1,-10,10,5,2,-1,8,-9,6,10,9,4,6,6,-10,3,-1,-10,-10,2,-10,-2,-1,-3,-2,6,1,-7,3,4,4,-7,-4,-7,-2,8,-9,10,3,1,-8,-9,7,5,1,-5,7,-1,9,-5,4,4,-6,-5,10,4,-3,9,9,1,-3,5,10,-3,2,1,5,-9,-2,10,2,-1,7,6,4,-5,8,1,6,7,3,-3,-3,-1,-9,-8,7,8,7,-9,5,-10,-6,9,4,-9,5,-7,-4,-3,9,6,1,9,9,-1,-6,5,3,-3,1,-7,-3,7,3,4,1,10,-1,-2,-1,-5,5,8,-6,-6,-2,-5,7,4,-2,-4,8,7,-6,-2,-1,3,-6,5,-3,-1,1,-10,8,10,4,-4,-1,4,9,4,2,7,10,2,-2,8,8,4,4,5,10,-2,10,8,-1,-9,-2,1,-10,-7,3,-10,5,-9,9,-9,-3,2,7,3,4,1,10,-10,-2,-5,-4,7,8,-8,-10,-8,10,-6,-9,6,-1,-9,-6,1,8,2,8,9,5,-3,-4,8,10,-10,-1,10,3,2,10,7,9,10,-1,3,6,-1,-6,4,-2,-5,-3,6,-6,-5,-2,-4,4,-6,3,-2,-7,1,3,1,4,-8,-1,-2,1,-5,10,1,5,10,1,9,5,3,-7,-3,10,-7,6,-2,-7,-9,6,2,1,9,3,10,-10,-8,-9,8,-2,2,4,-4,-1,-1,-7,8,4,2,9,-9,-4,6,8,3,-8,-8,1,5,-7,8,-9,3,-8,-5,6,-6,9,-6,-3], dtype = "uint16")#candidate|5505|(672,)|const|uint16
var_5506 = relay.var("var_5506", dtype = "float32", shape = (490,))#candidate|5506|(490,)|var|float32
call_5504 = relay.TupleGetItem(func_4526_call(relay.reshape(const_5505.astype('uint16'), [672,]), relay.reshape(var_5506.astype('float32'), [49, 10]), ), 0)
call_5507 = relay.TupleGetItem(func_4530_call(relay.reshape(const_5505.astype('uint16'), [672,]), relay.reshape(var_5506.astype('float32'), [49, 10]), ), 0)
func_5173_call = mod.get_global_var('func_5173')
func_5176_call = mutated_mod.get_global_var('func_5176')
const_5509 = relay.const(-0.054611, dtype = "float32")#candidate|5509|()|const|float32
var_5510 = relay.var("var_5510", dtype = "float32", shape = (810,))#candidate|5510|(810,)|var|float32
call_5508 = relay.TupleGetItem(func_5173_call(relay.reshape(const_5509.astype('float32'), []), relay.reshape(var_5510.astype('float32'), [15, 9, 6]), ), 1)
call_5511 = relay.TupleGetItem(func_5176_call(relay.reshape(const_5509.astype('float32'), []), relay.reshape(var_5510.astype('float32'), [15, 9, 6]), ), 1)
func_1110_call = mod.get_global_var('func_1110')
func_1113_call = mutated_mod.get_global_var('func_1113')
call_5518 = relay.TupleGetItem(func_1110_call(relay.reshape(const_5509.astype('int64'), []), relay.reshape(call_5504.astype('float64'), [1, 140]), ), 0)
call_5519 = relay.TupleGetItem(func_1113_call(relay.reshape(const_5509.astype('int64'), []), relay.reshape(call_5504.astype('float64'), [1, 140]), ), 0)
func_2807_call = mod.get_global_var('func_2807')
func_2810_call = mutated_mod.get_global_var('func_2810')
const_5546 = relay.const([False,True,False,True,True,False,False,False,True,False,False,False,False,False,True,False,True,False,True,True,False,False,False,False,True,True,True,False,False,True,False,False,True,False,True,False,True,True,False,False,True,False,False,False,False,True,False,True,False,True,True,False,True,True,True,True,False,False,True,False,True,True,False,False,False,True,False,True,False,False,True,True,False,True,True,False,True,True,False,True,True,True,True,False,False,False,True,False,False,True,False,False,False,False,False,False,True,True,True,True,True,False,False,False,False,False,False,True,True,False,False,False,True,True,True,True,False,False,True,False,True,True,False,False,True,True,False,False,False,False,True,True,False,False,True], dtype = "bool")#candidate|5546|(135,)|const|bool
const_5547 = relay.const([False,True,True,False,True,False,False,True,True,True,True,True,True,True,True,False,False,True,False,True,True,False,True,True,False,False,False,False,False,False,False,False,False,True,False,True,True,False,False,False,False,True,False,True,True,True,True,True,False,True,False,True,False,True,True,False,True,True,False,True,True,False,True,True,True,False,True,True,False,True,True,False,True,True,True,False,False,True,True,False,False,True,False,False,False,True,False,True,False,False,True,True,False,False,True,False,False,False,True,True,True,False,True,False,False,True,False,False,False,True,True,False,False,True,True,False,False,True,False,False,False,True,True,False,True,False,False,False,False,True,True,False,False,False,False,False,True,True,False,True,False,True,False,True,False,True,True,False,False,True,False,False,False,False,True,False,False,True,False,True,True,True,True,True,True,True,True,True,False,True,False,True,True,False,False,True,True,True,False,False,True,False,False,True,False,True,True,True,True,True,False,False,False,True,True,False,False,False,True,True,True,True,False,False,False,False,False,True,True,False,True,False,False,False,False,True,True,True,False,False,True,False,False,True,True,True,True,True,True,False,False,True,False,False,True,False,False,True,True,False,True,True,False,False,True,False,True,False,False,True,True,True,True,True,False,False,True,False,True,False,False,False,True,False,False,True,False,True,False,False,True,False,True,True,False,False,False,True,False,False,False,True,True,True,True,True,True,False,True,False,False,False,False,False,False,True,True,True,False,True,True,True,True,False,False,True,False,False,False,False,False,False,False,True,True,True,True,False,True,False,True,True,False,True,True,True,False,False,False,False,False,True,True,True,True,False,True,True,False,True,True,True,False,True,False,True,False,True,False,True,False,True,True,False,False,False,True,True,True,True,True,True,False,True,False,True,True,True,False,True,True,False,False,True,True,True,False,False,False,False,True,False,True,False,True,False,True,False,True,False,False,False,True,False,True,True,False,False,True,False,False,False,False,False,True,False,True,True,False,False,False,True,False,True,False,True,True,True,False,False,True,False,True,False,False,False,True,False,True,False,True,True,False,True,True,True,True,True,True,True,True,True,True,True,False,True,True,False,False,True,False,True,True,True,True,True,False,False,False,True,True,True,False,True,False,True,True,False,False,False,True,True,True,False,True,True,True,False,True,True,True,False,False,False,True,True,True,True,False,True,False,True,False,False,False,True,False,True,True,False,True,False,False,False,True,True,False,False,True,True,False,False,True,False,False,True,False,True,False,False,True,True,True,True,True,True,False,True,True,True,False,False,False,False,True,True,True,True,True,False,False,True,False,False,False,False,True,False,True,True,False,False,False,True,False,False,False,False,True,True,False,True,False,False,True,True,True,False,False,False,False,False,False,False,False,False,False,True,False,False,True,False,False,True,True,False,True,True,True,True,True,True,False,True,True,False,False,False,False,False,False,True,False,False,True,True,False,False,False,False,False,True,False,False,True,True,True,False,True,False,True,False,True,False,True,False,False,True,False,False,True,False,True,True,True,True,False,True,True,True,False,True,False,False,True,True,False,False,False,True,False,True,True,True,True,False,True,True,True,True,False,False,False,True,True,True,False,False,False,True,True,False,False,True,True,False,True,True,False,True,False,True,False,True,False,False,True,False,True,False,True,True,False,True,True,True,False,True,True,True,True,False,True,True,False,False,True,True,True,False,False,True,True,False,False,True,False,True,True,False,True,True,True,True,False,False,True,True,False,False,False,True,True,True,False,True,False,False,False,True,False,False,True,True,False,True,False,True,True,False,True,False,True,False,False,True,True,True,False,True,True,False,False,False,False,False,True,False,False,True,True,False,True,False,True,False,False,False,True,True,False,False,True,True,False,True,False,True,False,True,False,False,True,False,False,True,True,False,True,True,True,True,False,True,True,True,True,True,True,False,False,True,False,False,False,False,True,True,False,False,False,False,False,True,True,False,True,False,False,False,True,False,True,True,True,True,True,False,False,False,False,True,False,False,True,False,False,False,True,False,False,True,True,False,True,False,True,False,False,True,False,True,True,False,True,False,True,False,False,True,False,False,False,False,False,True,True,True,False,False,True,False,False,False,True,True,False,False,True,False,True,True,False,True,True,True,True,False,True,False,False,True,False,False,False,True,False,True,False,False,True,True,False,True,False,True,False,False,True,True,True,True,True,True,False,False,False,True,True,True,True,True,False,False,True,False,True,True,True,True,True,True,False,False,False,False,True,True,True,True,False,False,False,True,True,False,False,True,True,True,False,True,False,False,True,True,True,False,True,False,True,False,True,True,False,False,False,False,True,True,True,True,True,True,True,False,True,True,True,False,False,True,True,False,True,False,True,False,False,False,True,True,True,False,True,True,False,True,True,True,False,False,True,True,True,False,True,False,True,False,True,True,True,False,True,False,True,False,True,True,True,False,True,False,False,False,True,True,True,True,False,True,True,True,False,True,True,True,True,False,True,False,True,False,True,False,False,False,True,True,True,False,True,False,False,False,False,True,True,True,False,True,False,False,True,False,True,False,True,False,True,False,True,False,False,False,True,True,False,False,False,True,False,False,False,False,False,False,True,True,False,False,False,False,False,True,True,True,False,False,True,True,True,False,True,True,False,False,False,False,False,True,False,False,True,False,False,True,False,False,False,False,False,False,True,False,False,False,True,False,False,False,True,True,True,False,True,True,True,True,False,True,False,False,False,True,False,False,False,False,False,False,True,False,True,False,False,True,False,True,True,False,False,False,False,True,False,True,False,True,False,False,True,True,False,True,False,False,True,True,True,False,True,False,False,False,False,True,True,False,False,False,False,False,False,False,True,True,True,False,False,False,False,True,True,True,False,True,True,False,False,False,False,False,False,False,False,False,True,False,False,False,False,True,False,True,True,False,False,True,False,False,True,False,False,False,True,False,True,True,False,False,True,False,False,False,True,False,False,False,False,True,False,True,False,True,False,True,True,False,False,True,False,True,True,False,True,True,True,True,False,True,True,True,False,True,True,True,True,False,True,False,True,False,True,True,True,True,False,False,True,True,True,True,False,False,False,False,True,True,True,True,False,False,True,False,True,False,True,False,False,True,False,True,True,True,False,False,False,True,False,True,False,True,True,False,True,True,False,True,False,True,False,False,True,True,True,False,False,False,True,False,True,True,False,False,True,False,False,True,True,False,True,True,True,False,False,True,True,False,False,True,False,False,True,True,False,False,False,False,True,True,False,False,False,False,True,True,True,True,True,False,False,False,False,True,False,False,False,True,False,False,False,False,True,True,False,True,False,False,True,True,True,True,True,True,False,False,True,True,False,False,True,False,False,True,True,False,True,False,True,False,False,True,False,True,False,False,False,False,False,True,True,True,True,True,True,True,True,False,False,True,False,True,True,False,True,True,False,False,True,True,False,True,False,True,True,False,True,True,True,False,True,False,True,False,True,False,True,True,False,True,False,False,False,False,False,True,True,False,False,False,True,False,True,True,True,False,False,True,False,True,True,True,True,False,True,True,True,False,False,True,True,False,False,True,False,False,True,True,True,True,True,False,True,True,False,True,True,False,False,True,True,True,False,False,True,True,True,False,True,True,False,False,False,False,False,False,False,True,False,True,False,True,False,True,False,False,False,False,False,False,True,True,True,False,True,True,True,True,True,True,False,True,True,False,True,True,True,False,False,True,True,False,False,True,False,True,True,False,True,True,True,False,False,False,False,False,True,False,True,True,True,True,False,False,False,False,False,True,False,False,False,True,True,False,True,True,True,False,True,False,False,False,True,False,True,True,False,False,True,True,True,False,True,False,True,True,False,True,False,False,True,False,True,False,False,False,True,False,True,True,False,True,True,True,True,False,True,False,True,False,True,False,True,False,False,False,True,False,True,True,False,False,True,False,True,False,False,False,False,True,True,False,False,True,False,False,True,True,False,False,True,True,True,False,False,True,False,True,False,True,True,False,False,False,False,True,False,True,True,False,False,True,True,True,False,True,True,True,False,True,False,True,False,True,False,False,False,False,False,False,False,True,True,False,True,True,True,False,False,False,False,True,True,True,False,True,False,True,True,False,False,True,False], dtype = "bool")#candidate|5547|(1755,)|const|bool
call_5545 = relay.TupleGetItem(func_2807_call(relay.reshape(const_5546.astype('bool'), [9, 1, 15]), relay.reshape(const_5547.astype('bool'), [9, 13, 15]), ), 0)
call_5548 = relay.TupleGetItem(func_2810_call(relay.reshape(const_5546.astype('bool'), [9, 1, 15]), relay.reshape(const_5547.astype('bool'), [9, 13, 15]), ), 0)
var_5550 = relay.var("var_5550", dtype = "float32", shape = (10, 7, 2))#candidate|5550|(10, 7, 2)|var|float32
bop_5551 = relay.bitwise_or(uop_5501.astype('int8'), relay.reshape(var_5550.astype('int8'), relay.shape_of(uop_5501))) # shape=(10, 7, 2)
bop_5554 = relay.bitwise_or(uop_5503.astype('int8'), relay.reshape(var_5550.astype('int8'), relay.shape_of(uop_5503))) # shape=(10, 7, 2)
func_1569_call = mod.get_global_var('func_1569')
func_1571_call = mutated_mod.get_global_var('func_1571')
call_5567 = relay.TupleGetItem(func_1569_call(), 0)
call_5568 = relay.TupleGetItem(func_1571_call(), 0)
output = relay.Tuple([call_5504,const_5505,var_5506,call_5508,const_5509,var_5510,call_5518,call_5545,const_5546,const_5547,bop_5551,call_5567,])
output2 = relay.Tuple([call_5507,const_5505,var_5506,call_5511,const_5509,var_5510,call_5519,call_5548,const_5546,const_5547,bop_5554,call_5568,])
func_5571 = relay.Function([var_5506,var_5510,var_5550,], output)
mod['func_5571'] = func_5571
mod = relay.transform.InferType()(mod)
var_5572 = relay.var("var_5572", dtype = "float32", shape = (490,))#candidate|5572|(490,)|var|float32
var_5573 = relay.var("var_5573", dtype = "float32", shape = (810,))#candidate|5573|(810,)|var|float32
var_5574 = relay.var("var_5574", dtype = "float32", shape = (10, 7, 2))#candidate|5574|(10, 7, 2)|var|float32
output = func_5571(var_5572,var_5573,var_5574,)
func_5575 = relay.Function([var_5572,var_5573,var_5574,], output)
mutated_mod['func_5575'] = func_5575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2059_call = mod.get_global_var('func_2059')
func_2061_call = mutated_mod.get_global_var('func_2061')
call_5597 = relay.TupleGetItem(func_2059_call(), 0)
call_5598 = relay.TupleGetItem(func_2061_call(), 0)
output = relay.Tuple([call_5597,])
output2 = relay.Tuple([call_5598,])
func_5599 = relay.Function([], output)
mod['func_5599'] = func_5599
mod = relay.transform.InferType()(mod)
output = func_5599()
func_5600 = relay.Function([], output)
mutated_mod['func_5600'] = func_5600
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3976_call = mod.get_global_var('func_3976')
func_3978_call = mutated_mod.get_global_var('func_3978')
call_5642 = relay.TupleGetItem(func_3976_call(), 2)
call_5643 = relay.TupleGetItem(func_3978_call(), 2)
func_935_call = mod.get_global_var('func_935')
func_936_call = mutated_mod.get_global_var('func_936')
call_5650 = func_935_call()
call_5651 = func_935_call()
output = relay.Tuple([call_5642,call_5650,])
output2 = relay.Tuple([call_5643,call_5651,])
func_5655 = relay.Function([], output)
mod['func_5655'] = func_5655
mod = relay.transform.InferType()(mod)
output = func_5655()
func_5656 = relay.Function([], output)
mutated_mod['func_5656'] = func_5656
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4706_call = mod.get_global_var('func_4706')
func_4707_call = mutated_mod.get_global_var('func_4707')
call_5669 = relay.TupleGetItem(func_4706_call(), 0)
call_5670 = relay.TupleGetItem(func_4707_call(), 0)
func_5132_call = mod.get_global_var('func_5132')
func_5134_call = mutated_mod.get_global_var('func_5134')
const_5679 = relay.const([7.846741,4.886341,-7.064406,-3.402499,-6.314951,-5.217219,-6.806033,4.088846,0.629501,0.257552,-7.803529,-8.327321,9.549762,2.901106,8.486350,-2.836409,5.123938,5.858466,-8.468770,-1.872155,6.115442,-6.937010,8.907164,-0.436429,-6.862628,-8.734923,-3.424759,4.690987,2.229215,-6.437499,7.962561,-5.440095,-1.060299,-7.346587,7.086428,-6.277232,5.387329,-6.567637,-4.596729,-6.454225,0.614545,0.866735,7.729188,8.045013,1.155537,-2.924657,-1.333283,4.666112,-3.257574,9.384192,-0.199397,-6.426737,1.379595,-7.863223,-3.674043,-7.232044,-9.245558,9.982997,-2.606204,-4.665192,-8.969718,-8.808321,4.671217,6.251551,-4.068238,-0.674065,-5.402678,-7.467733,1.326520,-4.429545,7.000320,8.496965,-0.610590,-0.829803,2.907286,1.902174,7.934683,2.843175,0.294023,-0.495100,8.868181,5.453503,3.185368,3.236767,-8.303529,-6.729242,-1.805865,2.919474,-7.535044,7.482386,9.563018,4.200657,5.637058,0.919507,-5.838743,-1.566128,-1.905606,7.017723,5.590007,8.296674,-1.640901,-8.320359,5.222802,-8.251167,4.108962,-7.607684,-2.249756,7.620387,-6.031448,-6.020337,-8.111720,-3.645686,-5.165575,-2.580793,6.390544,-0.226302,-3.695361,-4.446128,-7.956604,3.446235,8.508700,-6.952508,-0.812314,5.642591,8.119909,0.871062,-9.106175,-7.145659,9.394759,-0.694127,-8.044922,8.567819,2.893597,2.386834,-1.114083,2.778946,-9.951454,2.814325,9.837825,5.448051,-3.462221,-2.199629,-6.204092,-3.286128,-1.008681,-9.064193,0.450124,5.100189,-6.917499,-5.552788,6.132646,-4.200206,-0.695803,-7.794731,-0.671150,-7.620531,-4.758358,3.087984,8.152390,3.748018,-8.877170,9.435180,2.796979,5.485003,2.886941,-9.052578,1.867429,-1.568832,-6.710306,-6.291667,-1.251783,2.095856,5.528441,9.119757,-9.053012,-2.834057,9.133757,-1.812285,-5.022756,-3.627935,-4.607122,3.890860,6.604192,8.271475,-9.108637,-4.766286,-3.502700,-0.357291,-1.644485,-7.567510,-7.575110,0.571365,-1.483377,-9.316715,6.338152,-1.348654,9.272588,-2.424643,1.655314,-9.920645,4.505432,-1.315146,-8.441379,9.139089,3.024966,-9.721445,3.395002,4.784441,6.788383,-7.618395,-5.319622,-1.333290,-8.913732,-8.151442,-3.549871,-4.283149,0.300240,4.907409,3.777980,-7.459928,6.278843,-5.079129,-2.938480,-2.357220,4.184109,2.339207,-4.955268,1.261227,-7.136310,-5.678659,-6.628724,-8.886933,-2.323332,3.981712,-6.935230,-6.523623,-3.325023,-5.705417,-6.048385,6.259555,-0.213743,1.357034,-1.642361,5.913302,-7.146253,-1.695370,-0.530111,-8.935341,-9.868687,-0.239011,0.716707,-8.696143,8.084322,-2.795279,-6.694370,3.957694,-2.776499,7.538728,9.741248,7.935064,-2.168721,-4.509255,-0.283742,1.240481,6.396350,-2.341412,-0.102849,-5.980547,0.294531,4.147352,-8.145770,-5.959726,4.497965,-0.049883,2.593164,-2.865310,2.074413,-5.024817,5.113222,-9.393890,-5.147814,4.611160,-0.692911,-1.831360,6.408437,8.922421,0.770174,-4.589317,6.944276,0.482039,0.989460,-7.416423,9.367455,-7.586661,6.026215,9.051083,3.771009,-6.873040,-7.741322,-1.260627,2.754352,-4.135278,9.301637,4.177500,5.785417,6.844758,5.756570,0.421390,1.784038,6.406225,-1.709256,-7.126531,-7.017011,2.690856,5.289433,-9.191223,5.613836,0.280116,2.029311,2.412454,-0.609677,8.639176,6.497370,-5.377360,3.922258,3.127166,-7.948854,2.977989,-2.294895,9.182683,-0.789408,-3.554723,-0.500605,8.233840,1.797943,-3.805950,3.259075,3.359933,-1.065619,6.387035,7.560517,-6.429715,-0.761565,-8.716323,-2.116324,6.924263,3.659508,1.414744,5.843085,-6.596585,5.453418,-4.066544,-3.675236,2.672072,7.224641,-4.820398,2.792818,-9.853319,4.614353,1.337035,3.055516,-9.071621,-2.682045,-9.185932,-5.043860,-5.775936,-1.524898,1.260259,-4.742845,0.614292,4.841370,0.220926,-2.516994,0.662284,-2.375139,-4.511291,1.594350,8.913269,-4.128333,2.023694,-2.286266,-8.587564,4.401038,4.437662,0.856882,9.716710,7.504536,5.474814,9.255015,5.344237,5.171194,7.314339,-8.778686,6.706486,-5.333736,-0.340756,-8.934874,6.504648,-4.505722,-6.604204,-1.368356,-4.582144,-6.400699,8.245980,-7.466183,3.669499,-9.658118,-3.722343,7.080132,2.459685,9.766407,-1.339666,2.920571,4.090108,4.828771,0.040991,3.710113,1.610047,2.647891,1.321837,3.161782,-3.827659,8.394703,-6.623527,-2.519305,7.509697,0.250306,4.027061,0.772662,-4.547590,-6.951037,-3.494718,-8.433745,9.830061,6.664026,4.062533,-9.483841,-2.165747,6.376388,-3.657753,8.905900,8.648295,-4.892176,0.976928,8.092503,-5.126578,0.783817,7.927722,-1.228238,5.421457,-7.692548,-8.751926,-4.576126,-1.999899,1.213328,2.166656,-3.447019,-7.837511,-7.397244,2.957644,7.312898,9.904608,-6.951856,-5.799152,-6.359849,-4.582340,4.947945,5.811518,-3.947132,4.011793,-8.245367,-2.702692,7.125612,2.549398,-8.651873,3.749889,-2.868820,-8.371945,2.146164,9.215708,-2.743028,-7.943685,-2.688115,-9.262758,-1.472247,6.478118,-0.528275,2.510567,-7.565572,0.359882,5.661662,-8.535749,-9.864368,4.082693,-8.709255,7.869555,-4.459184,-7.991303,1.989732,2.158184,-4.796739,-9.272643,-2.381616,-8.120868,8.198397,4.409276,-8.057511,-3.787303,-5.740848,-8.475076,7.424915,-2.704514,-2.835362,-6.414063,7.797541,3.486754,-8.623409,-8.777668,5.235255,8.274917,1.107038,-7.039366,5.230594,-4.801913,-0.439036,-1.734561,-4.154740,5.883220,2.020424,-2.926332,-6.536274,-1.131023,0.829755,3.492539,9.589144,5.283979,-4.964707,-4.712409,0.256358,4.404974,1.922840,1.081938,-7.890951,-1.285909,-2.774457,-6.822913,-0.838628,-0.999696,-4.966117,2.092088,-2.413339,-8.556150,-2.662775,-3.460005,1.096368,3.682548,0.865274,-8.250959,0.392885,8.003465,1.566718,-3.680453,-8.870901,5.083945,8.042862,-5.772820,-8.151266,-5.439087,1.400931,-9.698851,-9.977728,-3.054810,-3.133550,-9.521578,7.614832,3.988018,6.350007,9.924414,-5.341324,-3.543486,6.129785,-3.891210,9.233593,-9.753498,6.893425,3.117525,-3.942431,-0.173276,-3.134778,-3.951213,-5.155644,-9.426155,-7.699925,-8.472779,0.018518,-3.477786,7.471940,-7.934922,5.109953,-5.115834,5.037694,-4.753139,0.837409,-5.410560,5.486766,6.634743,-5.719967,-1.469319,5.918102,-5.286936,9.002098,7.593057,9.812322,-1.777735,-1.846280,5.422407,-4.200475,1.585619,-1.172933,-0.684903,8.872975,-1.819046,1.674686,-9.697892,3.842742,9.169025,3.989253,7.297049,-5.518390,4.584148,-1.315865,-7.543904,-5.248395,-0.426181,7.570694,8.362105,5.304415,3.247392,-2.141616,8.928370,-7.909906,-8.852981,-3.029082,-0.894404,4.781532,5.386490,-9.011280,4.655835,-1.589210,-1.643171,-1.316167,-9.998375,5.780374,-4.479997,5.616385,2.413495,9.135164,5.576042,7.708630,-2.780848,8.924945,2.926622,-1.480795,-3.842885,-3.385872,-5.614776,-9.328594,-0.739921,-6.099671,2.709655,4.122219,8.966569,6.812062,-9.670758,-4.423194,4.658634,-3.167255,-1.870395,3.761758,1.119108,3.305225,-0.699854,-3.966469,5.221405,-4.472248,-6.422141,8.389417,-7.241956,-3.918536,1.659151,3.484343,-4.823751,6.948062,-9.811859,-8.294811,5.445444,-4.555284,1.416921,-5.911236,5.024510,-4.287941,-9.412409,-1.090991,-0.109679,9.217504,2.284856,-8.432542,8.169981,-3.163002,2.720834,2.487988,-2.710931,-0.386807,7.000132,-5.106136,7.359440,-8.589736,-0.925820,-3.766364,-5.066693,8.457908,0.338717,0.836565,5.905590,-5.996194,-9.097849,3.683367,1.433597,0.139524,7.993093,-6.904081,-7.921569,-6.145881,7.886272,4.740310,5.917378,7.119301,-2.223003,8.800094,5.512940,-3.358407,5.152651,-8.023691,-6.279567,7.303558,-6.421071,-4.272973,5.508291,3.309506,-8.541555,-5.099141,6.251467,-4.973616,-1.602134,-3.640730,2.230234,-4.199110,-7.849728,-8.972208,-5.172065,-3.878878,4.004760,8.278964,-6.384231,2.649357,1.758604,-5.721609,4.857777,-9.353035,-2.859896,0.235541,-2.714113,-3.042651,4.052415,4.022460,8.427435,-7.379375,-9.496513,7.358058,-6.337478,4.340660,-2.732939,3.165538,-6.314427], dtype = "float64")#candidate|5679|(784,)|const|float64
call_5678 = relay.TupleGetItem(func_5132_call(relay.reshape(const_5679.astype('float64'), [8, 14, 7])), 2)
call_5680 = relay.TupleGetItem(func_5134_call(relay.reshape(const_5679.astype('float64'), [8, 14, 7])), 2)
func_896_call = mod.get_global_var('func_896')
func_899_call = mutated_mod.get_global_var('func_899')
const_5686 = relay.const([6,10,7,-6,1,-7,-1,-7,7,7,-4,-8,-6,-5,9,-8,10,-8,7,-4,-6,-9,7,4,-1,-2,10,1,6,-6,4,1,-1,10,3,-8,6,9,-5,-7,-2,1,-10,9,-6,2,-10,-5,10,-10,-1,3,8,-1,3,-9], dtype = "int32")#candidate|5686|(56,)|const|int32
call_5685 = relay.TupleGetItem(func_896_call(relay.reshape(const_5686.astype('int32'), [7, 2, 4]), relay.reshape(const_5686.astype('int32'), [7, 2, 4]), ), 1)
call_5687 = relay.TupleGetItem(func_899_call(relay.reshape(const_5686.astype('int32'), [7, 2, 4]), relay.reshape(const_5686.astype('int32'), [7, 2, 4]), ), 1)
output = relay.Tuple([call_5669,call_5678,const_5679,call_5685,const_5686,])
output2 = relay.Tuple([call_5670,call_5680,const_5679,call_5687,const_5686,])
func_5688 = relay.Function([], output)
mod['func_5688'] = func_5688
mod = relay.transform.InferType()(mod)
output = func_5688()
func_5689 = relay.Function([], output)
mutated_mod['func_5689'] = func_5689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_935_call = mod.get_global_var('func_935')
func_936_call = mutated_mod.get_global_var('func_936')
call_5753 = func_935_call()
call_5754 = func_935_call()
func_1027_call = mod.get_global_var('func_1027')
func_1030_call = mutated_mod.get_global_var('func_1030')
call_5778 = relay.TupleGetItem(func_1027_call(relay.reshape(call_5753.astype('float64'), [10, 7, 2])), 0)
call_5779 = relay.TupleGetItem(func_1030_call(relay.reshape(call_5753.astype('float64'), [10, 7, 2])), 0)
output = relay.Tuple([call_5753,call_5778,])
output2 = relay.Tuple([call_5754,call_5779,])
func_5783 = relay.Function([], output)
mod['func_5783'] = func_5783
mod = relay.transform.InferType()(mod)
mutated_mod['func_5783'] = func_5783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5783_call = mutated_mod.get_global_var('func_5783')
call_5784 = func_5783_call()
output = call_5784
func_5785 = relay.Function([], output)
mutated_mod['func_5785'] = func_5785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2376_call = mod.get_global_var('func_2376')
func_2377_call = mutated_mod.get_global_var('func_2377')
call_5890 = relay.TupleGetItem(func_2376_call(), 1)
call_5891 = relay.TupleGetItem(func_2377_call(), 1)
func_4218_call = mod.get_global_var('func_4218')
func_4222_call = mutated_mod.get_global_var('func_4222')
const_5893 = relay.const(2, dtype = "uint32")#candidate|5893|()|const|uint32
const_5894 = relay.const([-5,8,9,-9,-6,7,10,5,-1,6,-3,4,-2,9,5,2,-2,1,2,-10,-4,-10,-4,6,7,9,8,5,10,-3,1,-6,-6,6,8,-6,10,-7,-10,-2,-6,6,-6,-5,8,-3,5,-4,8,-9], dtype = "uint32")#candidate|5894|(50,)|const|uint32
call_5892 = func_4218_call(relay.reshape(const_5893.astype('uint32'), []), relay.reshape(const_5894.astype('uint32'), [5, 2, 5]), )
call_5895 = func_4218_call(relay.reshape(const_5893.astype('uint32'), []), relay.reshape(const_5894.astype('uint32'), [5, 2, 5]), )
bop_5905 = relay.mod(const_5894.astype('float64'), relay.reshape(call_5892.astype('float64'), relay.shape_of(const_5894))) # shape=(50,)
bop_5908 = relay.mod(const_5894.astype('float64'), relay.reshape(call_5895.astype('float64'), relay.shape_of(const_5894))) # shape=(50,)
output = relay.Tuple([call_5890,const_5893,bop_5905,])
output2 = relay.Tuple([call_5891,const_5893,bop_5908,])
func_5913 = relay.Function([], output)
mod['func_5913'] = func_5913
mod = relay.transform.InferType()(mod)
output = func_5913()
func_5914 = relay.Function([], output)
mutated_mod['func_5914'] = func_5914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4141_call = mod.get_global_var('func_4141')
func_4143_call = mutated_mod.get_global_var('func_4143')
call_5918 = relay.TupleGetItem(func_4141_call(), 0)
call_5919 = relay.TupleGetItem(func_4143_call(), 0)
func_4141_call = mod.get_global_var('func_4141')
func_4143_call = mutated_mod.get_global_var('func_4143')
call_5922 = relay.TupleGetItem(func_4141_call(), 0)
call_5923 = relay.TupleGetItem(func_4143_call(), 0)
func_4472_call = mod.get_global_var('func_4472')
func_4473_call = mutated_mod.get_global_var('func_4473')
call_5927 = relay.TupleGetItem(func_4472_call(), 8)
call_5928 = relay.TupleGetItem(func_4473_call(), 8)
var_5951 = relay.var("var_5951", dtype = "float64", shape = (10, 7, 2))#candidate|5951|(10, 7, 2)|var|float64
bop_5952 = relay.left_shift(call_5922.astype('uint8'), relay.reshape(var_5951.astype('uint8'), relay.shape_of(call_5922))) # shape=(10, 7, 2)
bop_5955 = relay.left_shift(call_5923.astype('uint8'), relay.reshape(var_5951.astype('uint8'), relay.shape_of(call_5923))) # shape=(10, 7, 2)
output = relay.Tuple([call_5918,call_5927,bop_5952,])
output2 = relay.Tuple([call_5919,call_5928,bop_5955,])
func_5956 = relay.Function([var_5951,], output)
mod['func_5956'] = func_5956
mod = relay.transform.InferType()(mod)
var_5957 = relay.var("var_5957", dtype = "float64", shape = (10, 7, 2))#candidate|5957|(10, 7, 2)|var|float64
output = func_5956(var_5957)
func_5958 = relay.Function([var_5957], output)
mutated_mod['func_5958'] = func_5958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2059_call = mod.get_global_var('func_2059')
func_2061_call = mutated_mod.get_global_var('func_2061')
call_6041 = relay.TupleGetItem(func_2059_call(), 0)
call_6042 = relay.TupleGetItem(func_2061_call(), 0)
func_3118_call = mod.get_global_var('func_3118')
func_3120_call = mutated_mod.get_global_var('func_3120')
const_6056 = relay.const([2.806066,-6.163521,1.930085,5.501080,9.921682,-2.670458,-8.351997,6.729753,-8.361744,3.881627,-4.285551,-8.681800,-7.031801,-5.235275,6.309922,7.624333,-3.149370,-6.824207,8.257438,3.345082,5.955869,-6.199705,8.397580,0.599782,-4.266926,-4.557406,-8.698119,1.842581,1.772073,-4.757217,9.646058,7.563392,3.725817,1.782839,-5.303664,-7.969754,1.041490,8.950965,-9.853408,-1.923033,8.622909,2.236721,3.240557,-9.578521,-0.762253,8.847856,-3.045092,5.965274,-9.551670,-7.236299,4.771250,-3.989588,9.843313,-8.679111,6.485835,3.173128,8.385871,-9.354425,8.111498,2.728542,-0.544814,2.014552,-8.629203,-9.781619,9.474169,7.001058,5.598872,2.483685,4.725511,-0.083896,-2.044708,3.043031,-3.133080,-4.487303,-3.187245,2.043285,-4.188243,-2.448645,9.254457,5.000887,2.025523,-8.698246,3.817525,-2.918542,0.756349,9.536300,-3.629809,9.528021,-0.644296,-3.947275,-7.627966,1.341794,-8.482627,4.387636,8.093967,-6.281917,9.188126,5.805666,0.212360,1.702235,9.915265,-5.099534,4.045006,-4.277939,-2.176943,-6.760568,3.548803,0.006992,9.373926,9.645879,-9.097572,-9.414090,-0.345871,-3.636471,3.755575,-2.912691,-5.080891,-4.644168,5.605615,1.381954,3.439257,-0.702779,-6.312417,-9.382040,-1.056297,-5.131494,1.571765,-6.437606,-4.709943,0.432734,-9.438627,-4.196647,5.026572,-6.052828,-9.465226,-2.391089,0.114853,-9.808025,-5.252448,-2.203527,-6.536328,9.366678,1.846943,-6.671084,-8.622218,2.956411,8.489272,9.777178,-5.554975,5.604326,-9.706540,-6.557009,-0.884026,0.778058,3.514992,7.034349,-8.963189,1.651447,-5.333047,6.770849], dtype = "float64")#candidate|6056|(160,)|const|float64
call_6055 = relay.TupleGetItem(func_3118_call(relay.reshape(const_6056.astype('float64'), [16, 5, 2])), 0)
call_6057 = relay.TupleGetItem(func_3120_call(relay.reshape(const_6056.astype('float64'), [16, 5, 2])), 0)
func_3353_call = mod.get_global_var('func_3353')
func_3355_call = mutated_mod.get_global_var('func_3355')
var_6061 = relay.var("var_6061", dtype = "int64", shape = ())#candidate|6061|()|var|int64
call_6060 = relay.TupleGetItem(func_3353_call(relay.reshape(var_6061.astype('int64'), [])), 4)
call_6062 = relay.TupleGetItem(func_3355_call(relay.reshape(var_6061.astype('int64'), [])), 4)
func_5571_call = mod.get_global_var('func_5571')
func_5575_call = mutated_mod.get_global_var('func_5575')
var_6067 = relay.var("var_6067", dtype = "float32", shape = (1, 490))#candidate|6067|(1, 490)|var|float32
var_6068 = relay.var("var_6068", dtype = "float32", shape = (810,))#candidate|6068|(810,)|var|float32
call_6066 = relay.TupleGetItem(func_5571_call(relay.reshape(var_6067.astype('float32'), [490,]), relay.reshape(var_6068.astype('float32'), [810,]), relay.reshape(call_6041.astype('float32'), [10, 7, 2]), ), 1)
call_6069 = relay.TupleGetItem(func_5575_call(relay.reshape(var_6067.astype('float32'), [490,]), relay.reshape(var_6068.astype('float32'), [810,]), relay.reshape(call_6041.astype('float32'), [10, 7, 2]), ), 1)
func_4286_call = mod.get_global_var('func_4286')
func_4287_call = mutated_mod.get_global_var('func_4287')
call_6070 = func_4286_call()
call_6071 = func_4286_call()
output = relay.Tuple([call_6041,call_6055,const_6056,call_6060,var_6061,call_6066,var_6067,var_6068,call_6070,])
output2 = relay.Tuple([call_6042,call_6057,const_6056,call_6062,var_6061,call_6069,var_6067,var_6068,call_6071,])
func_6072 = relay.Function([var_6061,var_6067,var_6068,], output)
mod['func_6072'] = func_6072
mod = relay.transform.InferType()(mod)
var_6073 = relay.var("var_6073", dtype = "int64", shape = ())#candidate|6073|()|var|int64
var_6074 = relay.var("var_6074", dtype = "float32", shape = (1, 490))#candidate|6074|(1, 490)|var|float32
var_6075 = relay.var("var_6075", dtype = "float32", shape = (810,))#candidate|6075|(810,)|var|float32
output = func_6072(var_6073,var_6074,var_6075,)
func_6076 = relay.Function([var_6073,var_6074,var_6075,], output)
mutated_mod['func_6076'] = func_6076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1468_call = mod.get_global_var('func_1468')
func_1470_call = mutated_mod.get_global_var('func_1470')
call_6150 = relay.TupleGetItem(func_1468_call(), 3)
call_6151 = relay.TupleGetItem(func_1470_call(), 3)
output = relay.Tuple([call_6150,])
output2 = relay.Tuple([call_6151,])
func_6164 = relay.Function([], output)
mod['func_6164'] = func_6164
mod = relay.transform.InferType()(mod)
output = func_6164()
func_6165 = relay.Function([], output)
mutated_mod['func_6165'] = func_6165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3153_call = mod.get_global_var('func_3153')
func_3154_call = mutated_mod.get_global_var('func_3154')
call_6209 = relay.TupleGetItem(func_3153_call(), 0)
call_6210 = relay.TupleGetItem(func_3154_call(), 0)
func_4804_call = mod.get_global_var('func_4804')
func_4805_call = mutated_mod.get_global_var('func_4805')
call_6211 = relay.TupleGetItem(func_4804_call(), 0)
call_6212 = relay.TupleGetItem(func_4805_call(), 0)
output = relay.Tuple([call_6209,call_6211,])
output2 = relay.Tuple([call_6210,call_6212,])
func_6232 = relay.Function([], output)
mod['func_6232'] = func_6232
mod = relay.transform.InferType()(mod)
output = func_6232()
func_6233 = relay.Function([], output)
mutated_mod['func_6233'] = func_6233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1308_call = mod.get_global_var('func_1308')
func_1310_call = mutated_mod.get_global_var('func_1310')
call_6240 = func_1308_call()
call_6241 = func_1308_call()
output = relay.Tuple([call_6240,])
output2 = relay.Tuple([call_6241,])
func_6247 = relay.Function([], output)
mod['func_6247'] = func_6247
mod = relay.transform.InferType()(mod)
output = func_6247()
func_6248 = relay.Function([], output)
mutated_mod['func_6248'] = func_6248
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3827_call = mod.get_global_var('func_3827')
func_3828_call = mutated_mod.get_global_var('func_3828')
call_6425 = relay.TupleGetItem(func_3827_call(), 0)
call_6426 = relay.TupleGetItem(func_3828_call(), 0)
output = relay.Tuple([call_6425,])
output2 = relay.Tuple([call_6426,])
func_6433 = relay.Function([], output)
mod['func_6433'] = func_6433
mod = relay.transform.InferType()(mod)
output = func_6433()
func_6434 = relay.Function([], output)
mutated_mod['func_6434'] = func_6434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5655_call = mod.get_global_var('func_5655')
func_5656_call = mutated_mod.get_global_var('func_5656')
call_6440 = relay.TupleGetItem(func_5655_call(), 0)
call_6441 = relay.TupleGetItem(func_5656_call(), 0)
output = relay.Tuple([call_6440,])
output2 = relay.Tuple([call_6441,])
func_6450 = relay.Function([], output)
mod['func_6450'] = func_6450
mod = relay.transform.InferType()(mod)
mutated_mod['func_6450'] = func_6450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6450_call = mutated_mod.get_global_var('func_6450')
call_6451 = func_6450_call()
output = call_6451
func_6452 = relay.Function([], output)
mutated_mod['func_6452'] = func_6452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2376_call = mod.get_global_var('func_2376')
func_2377_call = mutated_mod.get_global_var('func_2377')
call_6474 = relay.TupleGetItem(func_2376_call(), 2)
call_6475 = relay.TupleGetItem(func_2377_call(), 2)
output = call_6474
output2 = call_6475
func_6484 = relay.Function([], output)
mod['func_6484'] = func_6484
mod = relay.transform.InferType()(mod)
mutated_mod['func_6484'] = func_6484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6484_call = mutated_mod.get_global_var('func_6484')
call_6485 = func_6484_call()
output = call_6485
func_6486 = relay.Function([], output)
mutated_mod['func_6486'] = func_6486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4706_call = mod.get_global_var('func_4706')
func_4707_call = mutated_mod.get_global_var('func_4707')
call_6497 = relay.TupleGetItem(func_4706_call(), 1)
call_6498 = relay.TupleGetItem(func_4707_call(), 1)
output = relay.Tuple([call_6497,])
output2 = relay.Tuple([call_6498,])
func_6513 = relay.Function([], output)
mod['func_6513'] = func_6513
mod = relay.transform.InferType()(mod)
output = func_6513()
func_6514 = relay.Function([], output)
mutated_mod['func_6514'] = func_6514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3471_call = mod.get_global_var('func_3471')
func_3473_call = mutated_mod.get_global_var('func_3473')
call_6541 = relay.TupleGetItem(func_3471_call(), 0)
call_6542 = relay.TupleGetItem(func_3473_call(), 0)
func_1360_call = mod.get_global_var('func_1360')
func_1364_call = mutated_mod.get_global_var('func_1364')
var_6577 = relay.var("var_6577", dtype = "float32", shape = (6, 2))#candidate|6577|(6, 2)|var|float32
var_6578 = relay.var("var_6578", dtype = "int64", shape = ())#candidate|6578|()|var|int64
const_6579 = relay.const([2,-10,-4,-7,6,-1,9,7,5,6,-7,6,8,-8,-4,6,5,-3,8,-5,5,-5,2,-2,5,4,-8,-3,2,-9,-8,-2,-10,-3,-7,3,8,6,9,-9,-6,8,5,2,3,-4,6,-6,-3,5,9,1,5,7,7,-2], dtype = "int32")#candidate|6579|(56,)|const|int32
call_6576 = relay.TupleGetItem(func_1360_call(relay.reshape(var_6577.astype('float32'), [1, 4, 3]), relay.reshape(var_6578.astype('int64'), []), relay.reshape(const_6579.astype('int32'), [56,]), ), 1)
call_6580 = relay.TupleGetItem(func_1364_call(relay.reshape(var_6577.astype('float32'), [1, 4, 3]), relay.reshape(var_6578.astype('int64'), []), relay.reshape(const_6579.astype('int32'), [56,]), ), 1)
func_5413_call = mod.get_global_var('func_5413')
func_5414_call = mutated_mod.get_global_var('func_5414')
call_6590 = relay.TupleGetItem(func_5413_call(), 1)
call_6591 = relay.TupleGetItem(func_5414_call(), 1)
bop_6592 = relay.multiply(call_6590.astype('int64'), relay.reshape(call_6576.astype('int64'), relay.shape_of(call_6590))) # shape=(10, 7, 2)
bop_6595 = relay.multiply(call_6591.astype('int64'), relay.reshape(call_6580.astype('int64'), relay.shape_of(call_6591))) # shape=(10, 7, 2)
func_5956_call = mod.get_global_var('func_5956')
func_5958_call = mutated_mod.get_global_var('func_5958')
call_6599 = relay.TupleGetItem(func_5956_call(relay.reshape(call_6590.astype('float64'), [10, 7, 2])), 1)
call_6600 = relay.TupleGetItem(func_5958_call(relay.reshape(call_6590.astype('float64'), [10, 7, 2])), 1)
func_4992_call = mod.get_global_var('func_4992')
func_4994_call = mutated_mod.get_global_var('func_4994')
call_6620 = relay.TupleGetItem(func_4992_call(), 1)
call_6621 = relay.TupleGetItem(func_4994_call(), 1)
func_5599_call = mod.get_global_var('func_5599')
func_5600_call = mutated_mod.get_global_var('func_5600')
call_6632 = relay.TupleGetItem(func_5599_call(), 0)
call_6633 = relay.TupleGetItem(func_5600_call(), 0)
func_1896_call = mod.get_global_var('func_1896')
func_1898_call = mutated_mod.get_global_var('func_1898')
call_6638 = relay.TupleGetItem(func_1896_call(), 0)
call_6639 = relay.TupleGetItem(func_1898_call(), 0)
output = relay.Tuple([call_6541,var_6577,var_6578,const_6579,bop_6592,call_6599,call_6620,call_6632,call_6638,])
output2 = relay.Tuple([call_6542,var_6577,var_6578,const_6579,bop_6595,call_6600,call_6621,call_6633,call_6639,])
func_6641 = relay.Function([var_6577,var_6578,], output)
mod['func_6641'] = func_6641
mod = relay.transform.InferType()(mod)
mutated_mod['func_6641'] = func_6641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6641_call = mutated_mod.get_global_var('func_6641')
var_6643 = relay.var("var_6643", dtype = "float32", shape = (6, 2))#candidate|6643|(6, 2)|var|float32
var_6644 = relay.var("var_6644", dtype = "int64", shape = ())#candidate|6644|()|var|int64
call_6642 = func_6641_call(var_6643,var_6644,)
output = call_6642
func_6645 = relay.Function([var_6643,var_6644,], output)
mutated_mod['func_6645'] = func_6645
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6690 = relay.var("var_6690", dtype = "float64", shape = (5, 15, 6))#candidate|6690|(5, 15, 6)|var|float64
uop_6691 = relay.log2(var_6690.astype('float64')) # shape=(5, 15, 6)
uop_6695 = relay.log10(uop_6691.astype('float32')) # shape=(5, 15, 6)
output = relay.Tuple([uop_6695,])
output2 = relay.Tuple([uop_6695,])
func_6698 = relay.Function([var_6690,], output)
mod['func_6698'] = func_6698
mod = relay.transform.InferType()(mod)
mutated_mod['func_6698'] = func_6698
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6699 = relay.var("var_6699", dtype = "float64", shape = (5, 15, 6))#candidate|6699|(5, 15, 6)|var|float64
func_6698_call = mutated_mod.get_global_var('func_6698')
call_6700 = func_6698_call(var_6699)
output = call_6700
func_6701 = relay.Function([var_6699], output)
mutated_mod['func_6701'] = func_6701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3471_call = mod.get_global_var('func_3471')
func_3473_call = mutated_mod.get_global_var('func_3473')
call_6703 = relay.TupleGetItem(func_3471_call(), 2)
call_6704 = relay.TupleGetItem(func_3473_call(), 2)
func_896_call = mod.get_global_var('func_896')
func_899_call = mutated_mod.get_global_var('func_899')
const_6716 = relay.const([1,7,8,5,-4,4,5,-6,5,-1,-8,5,-5,-4,-6,-6,-4,-10,-10,2,10,-10,3,-1,-10,5,-5,7,-1,-8,4,6,1,-10,3,-7,-8,-1,4,1,-4,-2,-5,10,4,7,-4,-3,10,-5,7,-7,10,-6,-10,8], dtype = "int32")#candidate|6716|(56,)|const|int32
call_6715 = relay.TupleGetItem(func_896_call(relay.reshape(const_6716.astype('int32'), [7, 2, 4]), relay.reshape(const_6716.astype('int32'), [7, 2, 4]), ), 3)
call_6717 = relay.TupleGetItem(func_899_call(relay.reshape(const_6716.astype('int32'), [7, 2, 4]), relay.reshape(const_6716.astype('int32'), [7, 2, 4]), ), 3)
output = relay.Tuple([call_6703,call_6715,const_6716,])
output2 = relay.Tuple([call_6704,call_6717,const_6716,])
func_6746 = relay.Function([], output)
mod['func_6746'] = func_6746
mod = relay.transform.InferType()(mod)
output = func_6746()
func_6747 = relay.Function([], output)
mutated_mod['func_6747'] = func_6747
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3386_call = mod.get_global_var('func_3386')
func_3388_call = mutated_mod.get_global_var('func_3388')
call_6767 = relay.TupleGetItem(func_3386_call(), 0)
call_6768 = relay.TupleGetItem(func_3388_call(), 0)
func_1110_call = mod.get_global_var('func_1110')
func_1113_call = mutated_mod.get_global_var('func_1113')
const_6786 = relay.const(8, dtype = "int64")#candidate|6786|()|const|int64
call_6785 = relay.TupleGetItem(func_1110_call(relay.reshape(const_6786.astype('int64'), []), relay.reshape(call_6767.astype('float64'), [1, 140]), ), 0)
call_6787 = relay.TupleGetItem(func_1113_call(relay.reshape(const_6786.astype('int64'), []), relay.reshape(call_6767.astype('float64'), [1, 140]), ), 0)
uop_6790 = relay.log10(call_6785.astype('float32')) # shape=(14, 9, 7)
uop_6792 = relay.log10(call_6787.astype('float32')) # shape=(14, 9, 7)
output = relay.Tuple([call_6767,const_6786,uop_6790,])
output2 = relay.Tuple([call_6768,const_6786,uop_6792,])
func_6793 = relay.Function([], output)
mod['func_6793'] = func_6793
mod = relay.transform.InferType()(mod)
output = func_6793()
func_6794 = relay.Function([], output)
mutated_mod['func_6794'] = func_6794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4266_call = mod.get_global_var('func_4266')
func_4267_call = mutated_mod.get_global_var('func_4267')
call_6820 = func_4266_call()
call_6821 = func_4266_call()
func_4617_call = mod.get_global_var('func_4617')
func_4621_call = mutated_mod.get_global_var('func_4621')
var_6831 = relay.var("var_6831", dtype = "int64", shape = (231,))#candidate|6831|(231,)|var|int64
call_6830 = relay.TupleGetItem(func_4617_call(relay.reshape(var_6831.astype('int64'), [3, 7, 11]), relay.reshape(var_6831.astype('int64'), [3, 7, 11]), relay.reshape(var_6831.astype('int64'), [3, 7, 11]), ), 3)
call_6832 = relay.TupleGetItem(func_4621_call(relay.reshape(var_6831.astype('int64'), [3, 7, 11]), relay.reshape(var_6831.astype('int64'), [3, 7, 11]), relay.reshape(var_6831.astype('int64'), [3, 7, 11]), ), 3)
output = relay.Tuple([call_6820,call_6830,var_6831,])
output2 = relay.Tuple([call_6821,call_6832,var_6831,])
func_6838 = relay.Function([var_6831,], output)
mod['func_6838'] = func_6838
mod = relay.transform.InferType()(mod)
mutated_mod['func_6838'] = func_6838
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6839 = relay.var("var_6839", dtype = "int64", shape = (231,))#candidate|6839|(231,)|var|int64
func_6838_call = mutated_mod.get_global_var('func_6838')
call_6840 = func_6838_call(var_6839)
output = call_6840
func_6841 = relay.Function([var_6839], output)
mutated_mod['func_6841'] = func_6841
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1569_call = mod.get_global_var('func_1569')
func_1571_call = mutated_mod.get_global_var('func_1571')
call_6845 = relay.TupleGetItem(func_1569_call(), 0)
call_6846 = relay.TupleGetItem(func_1571_call(), 0)
func_5461_call = mod.get_global_var('func_5461')
func_5465_call = mutated_mod.get_global_var('func_5465')
const_6854 = relay.const([-4.808099,-1.130139,-8.695966,0.082770,1.003503,8.156900,-0.350120,9.153838,-3.595657,7.062735,-8.226994,6.788691,-5.309901,6.119383,-7.433471,4.498015,-7.821026,-3.986124,-3.015851,-0.738542,-6.250720,6.008926,4.801721,0.783174,-7.610635,5.138095,3.547473,-6.599708,4.181391,2.874375,4.950493,-1.400141,-3.658544,-9.485194,0.243724,-5.912019,2.417858,-9.420712,6.284500,-9.531218,-7.246864,-5.553221,-5.407692,0.573134,-1.009042,5.621698,1.362345,0.865451,-7.441049,-8.777908,1.155877,5.176594,-9.676926,7.430820,9.533165,-9.517286,-1.853392,8.285703,0.899101,-5.718083,-9.769697,8.018149,-7.782588,3.367716], dtype = "float64")#candidate|6854|(64,)|const|float64
call_6853 = relay.TupleGetItem(func_5461_call(relay.reshape(const_6854.astype('float64'), [8, 4, 2]), relay.reshape(const_6854.astype('float64'), [8, 4, 2]), ), 0)
call_6855 = relay.TupleGetItem(func_5465_call(relay.reshape(const_6854.astype('float64'), [8, 4, 2]), relay.reshape(const_6854.astype('float64'), [8, 4, 2]), ), 0)
output = relay.Tuple([call_6845,call_6853,const_6854,])
output2 = relay.Tuple([call_6846,call_6855,const_6854,])
func_6860 = relay.Function([], output)
mod['func_6860'] = func_6860
mod = relay.transform.InferType()(mod)
output = func_6860()
func_6861 = relay.Function([], output)
mutated_mod['func_6861'] = func_6861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2428_call = mod.get_global_var('func_2428')
func_2430_call = mutated_mod.get_global_var('func_2430')
call_6864 = func_2428_call()
call_6865 = func_2428_call()
func_3386_call = mod.get_global_var('func_3386')
func_3388_call = mutated_mod.get_global_var('func_3388')
call_6866 = relay.TupleGetItem(func_3386_call(), 0)
call_6867 = relay.TupleGetItem(func_3388_call(), 0)
output = relay.Tuple([call_6864,call_6866,])
output2 = relay.Tuple([call_6865,call_6867,])
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
func_5413_call = mod.get_global_var('func_5413')
func_5414_call = mutated_mod.get_global_var('func_5414')
call_6900 = relay.TupleGetItem(func_5413_call(), 0)
call_6901 = relay.TupleGetItem(func_5414_call(), 0)
output = relay.Tuple([call_6900,])
output2 = relay.Tuple([call_6901,])
func_6931 = relay.Function([], output)
mod['func_6931'] = func_6931
mod = relay.transform.InferType()(mod)
output = func_6931()
func_6932 = relay.Function([], output)
mutated_mod['func_6932'] = func_6932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3471_call = mod.get_global_var('func_3471')
func_3473_call = mutated_mod.get_global_var('func_3473')
call_6933 = relay.TupleGetItem(func_3471_call(), 2)
call_6934 = relay.TupleGetItem(func_3473_call(), 2)
func_4472_call = mod.get_global_var('func_4472')
func_4473_call = mutated_mod.get_global_var('func_4473')
call_6958 = relay.TupleGetItem(func_4472_call(), 3)
call_6959 = relay.TupleGetItem(func_4473_call(), 3)
output = relay.Tuple([call_6933,call_6958,])
output2 = relay.Tuple([call_6934,call_6959,])
func_6964 = relay.Function([], output)
mod['func_6964'] = func_6964
mod = relay.transform.InferType()(mod)
output = func_6964()
func_6965 = relay.Function([], output)
mutated_mod['func_6965'] = func_6965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1488_call = mod.get_global_var('func_1488')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_7003 = func_1488_call()
call_7004 = func_1488_call()
output = call_7003
output2 = call_7004
func_7008 = relay.Function([], output)
mod['func_7008'] = func_7008
mod = relay.transform.InferType()(mod)
mutated_mod['func_7008'] = func_7008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7008_call = mutated_mod.get_global_var('func_7008')
call_7009 = func_7008_call()
output = call_7009
func_7010 = relay.Function([], output)
mutated_mod['func_7010'] = func_7010
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1896_call = mod.get_global_var('func_1896')
func_1898_call = mutated_mod.get_global_var('func_1898')
call_7011 = relay.TupleGetItem(func_1896_call(), 0)
call_7012 = relay.TupleGetItem(func_1898_call(), 0)
output = relay.Tuple([call_7011,])
output2 = relay.Tuple([call_7012,])
func_7013 = relay.Function([], output)
mod['func_7013'] = func_7013
mod = relay.transform.InferType()(mod)
output = func_7013()
func_7014 = relay.Function([], output)
mutated_mod['func_7014'] = func_7014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7013_call = mod.get_global_var('func_7013')
func_7014_call = mutated_mod.get_global_var('func_7014')
call_7071 = relay.TupleGetItem(func_7013_call(), 0)
call_7072 = relay.TupleGetItem(func_7014_call(), 0)
func_2508_call = mod.get_global_var('func_2508')
func_2510_call = mutated_mod.get_global_var('func_2510')
const_7076 = relay.const([8.982359,-2.973262,-2.318210,-7.693295,-3.119353,-9.544914,-1.573447,4.215431,-2.734977,8.419820,-7.920339,-7.100222,-0.425571,-6.445846,-2.927857,-0.705592,0.801045,-0.723762,-2.367236,-8.408527,-8.810468,2.106210,-2.784546,-5.766074,7.480902,-6.189867,-2.292132,-4.994510,8.896646,6.861413,5.452382,-2.163451,-2.368064,-2.752564,6.790125,4.373573,2.836857,-7.201811,-7.397573,-5.590063,9.262785,6.647340,7.988747,-6.645776,-5.330133,-9.982471,-8.452109,-1.685040,5.680130,5.942267,1.444098,-7.699918,2.805968,7.830997,1.307568,-4.112926,-1.808769,5.615149,0.805326,8.389461,4.623596,6.549281,-2.498881,-7.818467,-5.710060,-9.043881,-6.141764,-3.952380,-7.382725,5.471389,9.455421,-5.470437,1.929804,5.663781,6.592726,-9.920156,-6.103253,-2.609058,6.693635,-9.346967,-7.902843,-5.042364,-0.116989,2.943650,-3.459491,-8.945302,-1.768193,4.540900,-4.014135,-6.966085,2.003474,-4.184445,-1.189141,-4.962076,2.071696,2.026016,-8.775080,1.180418,-3.450296,7.387471,4.612282,-9.926452,-1.511144,-8.017180,-3.826747,-6.391116,8.479487,9.805351,-4.871817,-4.887916,-3.324280,5.757613,1.338495,0.990197,9.415302,-5.845432,4.806681,-3.150907,-9.814712,-2.203649,3.308511,3.884678,-4.497645,-5.637757,-5.218098,-3.212740,-7.874389,4.561730,-6.990932,2.568347,6.496288,2.576745,-5.358911,-7.643615,-5.529421,3.262923,-8.140100,-0.229121,6.066538,0.648775,4.192175,9.891198,8.873266,5.604581,5.169295,-4.559255,-0.184608,9.823408,4.742356,-0.136936,5.828368,-0.358078,-4.199292,-0.348574,2.791155,1.323583,9.399927,9.657070,-8.928888,1.285005,5.905158,-9.026152,3.690667,9.891641,-7.547734,-5.946514,0.847171,1.105139,7.164807,-5.667968,8.549909,-4.262256,-9.481444,0.228032,-7.301181,-6.744488,-3.815337,-7.818759,5.349474,2.381651,6.100434,9.309760,-4.289210,-5.490953,-3.196718,-4.957674,-4.691998,-2.330205,-8.717927,5.269882,-6.808462,8.441460,6.844768,-9.319673,3.904873,-0.986676,4.061366,2.414863,-3.876699,-6.910936,-5.455229,-7.480384,6.891356,8.047681,-4.621104,-8.707439,2.507436,-2.287591,0.596804,0.913021,-9.385756,5.822726,6.866410,4.596079,-5.026579,-1.805060,-5.034744,-5.320970,4.804870,-4.513215,-6.971583,7.118908,-2.862951,-8.561498,-1.701108,-2.381371,7.342828,4.657528,-6.909374,-9.641616,-5.107574,-4.609398,1.354065,-2.049737,-5.332385,5.300525,1.470704,-3.780887,-3.501712,-6.994445,-0.513355,4.405999,-0.722352,-9.133731,2.224271,-2.970202,6.738732,-6.255218,7.937019,-5.975416,2.290181,-2.859165,-7.095471,-7.198576,-6.264724,8.767775,8.453854,-3.041891,8.094840,8.611071,-7.546304,-4.060807,-7.219893,-5.382068,2.415946,9.717907,-5.748570,-2.376555,1.052614,9.317472,9.163048,-6.812357,9.031948,-5.400425,-8.432620,6.096803,4.221147,-1.440302,1.016158,9.225722,9.175553,8.579590,0.558512,-7.843714,2.864352,-6.872371,9.040374,1.987026,3.027530,9.209598,6.378973,-7.434389,7.857275,-4.514617,-3.782306,3.939876,6.350835,4.759956,-5.191733,6.816302,-3.154706,-3.328578,-0.192250,-7.458065,-1.706076,0.955253,0.990737,-1.018438,0.553904,5.006724,6.702210,0.531336,5.103141,6.333828,6.322266,2.435386,-9.015273,9.112422,-3.368455,-8.212557,1.228328,-4.418345,-8.225500,5.119341,-8.494191,3.736560,-0.211455,-7.664002,9.088856,3.179009,-8.553650,-1.134999,3.771186,0.449081,-2.379302,-0.169554,-3.801551,-9.977892,1.942352,-4.149503,-1.088037,4.570784,-0.317079,-8.645328,7.505350,-4.957122,1.303748,-7.020492,-4.291066,-6.640473,-9.138026,3.312661,1.429191,2.887853,9.515078,-1.503667,8.500784,-3.403038,8.419215,5.313988,1.331258,-0.549283,5.231192,7.120453,3.096851,-4.600492,-0.592857,-9.993410,1.102265,-9.057523,5.509134,-8.187444,0.088268,-2.861112,2.084935,3.741322,-4.958326,5.211299,8.051072,5.529479,-9.623629,-0.005762,0.749270,6.759774,-1.530763,-2.543463,-3.736619,-8.953909,3.126377,2.944522,-8.796699,1.303265,-7.926006,-3.471490,6.598484,-3.983123,8.348493,-8.848294,2.200408,0.273101,-2.263682,1.219189,-3.335302,-8.751054,3.165704,2.855468,-4.093627,-4.236908,8.803643,-6.094134,-2.831777,8.969548,0.263779,7.914132,9.813927,-6.436821,-2.204637,-0.025802,4.255677,-1.053319,-9.904117,8.271494,2.699571,-5.851531,-4.027641,3.042284,5.332955,2.850439,2.553843,-9.764505,4.341947,-4.177344,-8.582917,7.278547,3.119011,-4.023806,7.783360,-5.357727,8.330221,1.655610,-9.200815,1.686035,4.695343,-9.319860,6.285639,6.620049,-9.745927,-6.304155,5.143664,-0.856964,6.342394,-6.207363,-2.606155,2.686436,3.331435,-7.098731,-6.390457,-4.160731,-3.214397,-6.667838,5.256364,-3.547388,6.920275,-8.516699,-4.960007,7.963687,-1.153933,-6.073769,-2.426056,-7.966596,9.051175,7.917321,-8.075604,7.766070,4.723456,-5.006681,-3.166670,-7.462360,8.763398,-4.674857,9.635351,-0.092777,6.394642,7.098839,-6.222716,-0.816616,-9.758296,8.842003,0.631789,8.037585], dtype = "float64")#candidate|7076|(490,)|const|float64
call_7075 = relay.TupleGetItem(func_2508_call(relay.reshape(const_7076.astype('float64'), [5, 14, 7])), 1)
call_7077 = relay.TupleGetItem(func_2510_call(relay.reshape(const_7076.astype('float64'), [5, 14, 7])), 1)
uop_7082 = relay.cosh(const_7076.astype('float32')) # shape=(490,)
func_6450_call = mod.get_global_var('func_6450')
func_6452_call = mutated_mod.get_global_var('func_6452')
call_7086 = relay.TupleGetItem(func_6450_call(), 0)
call_7087 = relay.TupleGetItem(func_6452_call(), 0)
output = relay.Tuple([call_7071,call_7075,uop_7082,call_7086,])
output2 = relay.Tuple([call_7072,call_7077,uop_7082,call_7087,])
func_7092 = relay.Function([], output)
mod['func_7092'] = func_7092
mod = relay.transform.InferType()(mod)
output = func_7092()
func_7093 = relay.Function([], output)
mutated_mod['func_7093'] = func_7093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3976_call = mod.get_global_var('func_3976')
func_3978_call = mutated_mod.get_global_var('func_3978')
call_7119 = relay.TupleGetItem(func_3976_call(), 2)
call_7120 = relay.TupleGetItem(func_3978_call(), 2)
func_4617_call = mod.get_global_var('func_4617')
func_4621_call = mutated_mod.get_global_var('func_4621')
var_7131 = relay.var("var_7131", dtype = "int64", shape = (231,))#candidate|7131|(231,)|var|int64
call_7130 = relay.TupleGetItem(func_4617_call(relay.reshape(var_7131.astype('int64'), [3, 7, 11]), relay.reshape(var_7131.astype('int64'), [3, 7, 11]), relay.reshape(var_7131.astype('int64'), [3, 7, 11]), ), 0)
call_7132 = relay.TupleGetItem(func_4621_call(relay.reshape(var_7131.astype('int64'), [3, 7, 11]), relay.reshape(var_7131.astype('int64'), [3, 7, 11]), relay.reshape(var_7131.astype('int64'), [3, 7, 11]), ), 0)
output = relay.Tuple([call_7119,call_7130,var_7131,])
output2 = relay.Tuple([call_7120,call_7132,var_7131,])
func_7150 = relay.Function([var_7131,], output)
mod['func_7150'] = func_7150
mod = relay.transform.InferType()(mod)
mutated_mod['func_7150'] = func_7150
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7151 = relay.var("var_7151", dtype = "int64", shape = (231,))#candidate|7151|(231,)|var|int64
func_7150_call = mutated_mod.get_global_var('func_7150')
call_7152 = func_7150_call(var_7151)
output = call_7152
func_7153 = relay.Function([var_7151], output)
mutated_mod['func_7153'] = func_7153
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1136_call = mod.get_global_var('func_1136')
func_1137_call = mutated_mod.get_global_var('func_1137')
call_7160 = func_1136_call()
call_7161 = func_1136_call()
func_4882_call = mod.get_global_var('func_4882')
func_4884_call = mutated_mod.get_global_var('func_4884')
call_7169 = func_4882_call()
call_7170 = func_4882_call()
func_1110_call = mod.get_global_var('func_1110')
func_1113_call = mutated_mod.get_global_var('func_1113')
var_7174 = relay.var("var_7174", dtype = "int64", shape = ())#candidate|7174|()|var|int64
call_7173 = relay.TupleGetItem(func_1110_call(relay.reshape(var_7174.astype('int64'), []), relay.reshape(call_7160.astype('float64'), [1, 140]), ), 1)
call_7175 = relay.TupleGetItem(func_1113_call(relay.reshape(var_7174.astype('int64'), []), relay.reshape(call_7160.astype('float64'), [1, 140]), ), 1)
func_5237_call = mod.get_global_var('func_5237')
func_5240_call = mutated_mod.get_global_var('func_5240')
call_7176 = relay.TupleGetItem(func_5237_call(relay.reshape(var_7174.astype('int64'), [])), 2)
call_7177 = relay.TupleGetItem(func_5240_call(relay.reshape(var_7174.astype('int64'), [])), 2)
output = relay.Tuple([call_7160,call_7169,call_7173,var_7174,call_7176,])
output2 = relay.Tuple([call_7161,call_7170,call_7175,var_7174,call_7177,])
func_7179 = relay.Function([var_7174,], output)
mod['func_7179'] = func_7179
mod = relay.transform.InferType()(mod)
mutated_mod['func_7179'] = func_7179
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7180 = relay.var("var_7180", dtype = "int64", shape = ())#candidate|7180|()|var|int64
func_7179_call = mutated_mod.get_global_var('func_7179')
call_7181 = func_7179_call(var_7180)
output = call_7181
func_7182 = relay.Function([var_7180], output)
mutated_mod['func_7182'] = func_7182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_935_call = mod.get_global_var('func_935')
func_936_call = mutated_mod.get_global_var('func_936')
call_7187 = func_935_call()
call_7188 = func_935_call()
func_1862_call = mod.get_global_var('func_1862')
func_1864_call = mutated_mod.get_global_var('func_1864')
call_7193 = relay.TupleGetItem(func_1862_call(), 1)
call_7194 = relay.TupleGetItem(func_1864_call(), 1)
output = relay.Tuple([call_7187,call_7193,])
output2 = relay.Tuple([call_7188,call_7194,])
func_7203 = relay.Function([], output)
mod['func_7203'] = func_7203
mod = relay.transform.InferType()(mod)
output = func_7203()
func_7204 = relay.Function([], output)
mutated_mod['func_7204'] = func_7204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_971_call = mod.get_global_var('func_971')
func_973_call = mutated_mod.get_global_var('func_973')
call_7205 = relay.TupleGetItem(func_971_call(), 1)
call_7206 = relay.TupleGetItem(func_973_call(), 1)
func_1717_call = mod.get_global_var('func_1717')
func_1718_call = mutated_mod.get_global_var('func_1718')
call_7226 = func_1717_call()
call_7227 = func_1717_call()
func_6793_call = mod.get_global_var('func_6793')
func_6794_call = mutated_mod.get_global_var('func_6794')
call_7237 = relay.TupleGetItem(func_6793_call(), 2)
call_7238 = relay.TupleGetItem(func_6794_call(), 2)
func_6793_call = mod.get_global_var('func_6793')
func_6794_call = mutated_mod.get_global_var('func_6794')
call_7255 = relay.TupleGetItem(func_6793_call(), 1)
call_7256 = relay.TupleGetItem(func_6794_call(), 1)
output = relay.Tuple([call_7205,call_7226,call_7237,call_7255,])
output2 = relay.Tuple([call_7206,call_7227,call_7238,call_7256,])
func_7261 = relay.Function([], output)
mod['func_7261'] = func_7261
mod = relay.transform.InferType()(mod)
mutated_mod['func_7261'] = func_7261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7261_call = mutated_mod.get_global_var('func_7261')
call_7262 = func_7261_call()
output = call_7262
func_7263 = relay.Function([], output)
mutated_mod['func_7263'] = func_7263
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7339 = relay.var("var_7339", dtype = "uint16", shape = (8, 11, 3))#candidate|7339|(8, 11, 3)|var|uint16
var_7340 = relay.var("var_7340", dtype = "uint16", shape = (8, 11, 3))#candidate|7340|(8, 11, 3)|var|uint16
bop_7341 = relay.subtract(var_7339.astype('uint16'), relay.reshape(var_7340.astype('uint16'), relay.shape_of(var_7339))) # shape=(8, 11, 3)
func_5237_call = mod.get_global_var('func_5237')
func_5240_call = mutated_mod.get_global_var('func_5240')
const_7348 = relay.const(-4, dtype = "int64")#candidate|7348|()|const|int64
call_7347 = relay.TupleGetItem(func_5237_call(relay.reshape(const_7348.astype('int64'), [])), 2)
call_7349 = relay.TupleGetItem(func_5240_call(relay.reshape(const_7348.astype('int64'), [])), 2)
output = relay.Tuple([bop_7341,call_7347,const_7348,])
output2 = relay.Tuple([bop_7341,call_7349,const_7348,])
func_7361 = relay.Function([var_7339,var_7340,], output)
mod['func_7361'] = func_7361
mod = relay.transform.InferType()(mod)
var_7362 = relay.var("var_7362", dtype = "uint16", shape = (8, 11, 3))#candidate|7362|(8, 11, 3)|var|uint16
var_7363 = relay.var("var_7363", dtype = "uint16", shape = (8, 11, 3))#candidate|7363|(8, 11, 3)|var|uint16
output = func_7361(var_7362,var_7363,)
func_7364 = relay.Function([var_7362,var_7363,], output)
mutated_mod['func_7364'] = func_7364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6232_call = mod.get_global_var('func_6232')
func_6233_call = mutated_mod.get_global_var('func_6233')
call_7411 = relay.TupleGetItem(func_6232_call(), 1)
call_7412 = relay.TupleGetItem(func_6233_call(), 1)
output = call_7411
output2 = call_7412
func_7437 = relay.Function([], output)
mod['func_7437'] = func_7437
mod = relay.transform.InferType()(mod)
mutated_mod['func_7437'] = func_7437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7437_call = mutated_mod.get_global_var('func_7437')
call_7438 = func_7437_call()
output = call_7438
func_7439 = relay.Function([], output)
mutated_mod['func_7439'] = func_7439
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7448 = relay.var("var_7448", dtype = "float32", shape = (6, 8, 9))#candidate|7448|(6, 8, 9)|var|float32
uop_7449 = relay.tan(var_7448.astype('float32')) # shape=(6, 8, 9)
output = uop_7449
output2 = uop_7449
func_7460 = relay.Function([var_7448,], output)
mod['func_7460'] = func_7460
mod = relay.transform.InferType()(mod)
mutated_mod['func_7460'] = func_7460
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7461 = relay.var("var_7461", dtype = "float32", shape = (6, 8, 9))#candidate|7461|(6, 8, 9)|var|float32
func_7460_call = mutated_mod.get_global_var('func_7460')
call_7462 = func_7460_call(var_7461)
output = call_7462
func_7463 = relay.Function([var_7461], output)
mutated_mod['func_7463'] = func_7463
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5413_call = mod.get_global_var('func_5413')
func_5414_call = mutated_mod.get_global_var('func_5414')
call_7465 = relay.TupleGetItem(func_5413_call(), 3)
call_7466 = relay.TupleGetItem(func_5414_call(), 3)
func_4882_call = mod.get_global_var('func_4882')
func_4884_call = mutated_mod.get_global_var('func_4884')
call_7475 = func_4882_call()
call_7476 = func_4882_call()
output = relay.Tuple([call_7465,call_7475,])
output2 = relay.Tuple([call_7466,call_7476,])
func_7526 = relay.Function([], output)
mod['func_7526'] = func_7526
mod = relay.transform.InferType()(mod)
output = func_7526()
func_7527 = relay.Function([], output)
mutated_mod['func_7527'] = func_7527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4472_call = mod.get_global_var('func_4472')
func_4473_call = mutated_mod.get_global_var('func_4473')
call_7581 = relay.TupleGetItem(func_4472_call(), 5)
call_7582 = relay.TupleGetItem(func_4473_call(), 5)
output = call_7581
output2 = call_7582
func_7589 = relay.Function([], output)
mod['func_7589'] = func_7589
mod = relay.transform.InferType()(mod)
output = func_7589()
func_7590 = relay.Function([], output)
mutated_mod['func_7590'] = func_7590
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7626 = relay.var("var_7626", dtype = "float32", shape = (1, 15, 11))#candidate|7626|(1, 15, 11)|var|float32
uop_7627 = relay.sigmoid(var_7626.astype('float32')) # shape=(1, 15, 11)
uop_7632 = relay.cosh(uop_7627.astype('float32')) # shape=(1, 15, 11)
func_4992_call = mod.get_global_var('func_4992')
func_4994_call = mutated_mod.get_global_var('func_4994')
call_7644 = relay.TupleGetItem(func_4992_call(), 0)
call_7645 = relay.TupleGetItem(func_4994_call(), 0)
var_7650 = relay.var("var_7650", dtype = "float32", shape = (7, 15, 11))#candidate|7650|(7, 15, 11)|var|float32
bop_7651 = relay.subtract(uop_7632.astype('uint64'), var_7650.astype('uint64')) # shape=(7, 15, 11)
func_6838_call = mod.get_global_var('func_6838')
func_6841_call = mutated_mod.get_global_var('func_6841')
var_7660 = relay.var("var_7660", dtype = "int64", shape = (231,))#candidate|7660|(231,)|var|int64
call_7659 = relay.TupleGetItem(func_6838_call(relay.reshape(var_7660.astype('int64'), [231,])), 2)
call_7661 = relay.TupleGetItem(func_6841_call(relay.reshape(var_7660.astype('int64'), [231,])), 2)
bop_7674 = relay.maximum(var_7650.astype('uint64'), var_7626.astype('uint64')) # shape=(7, 15, 11)
func_7437_call = mod.get_global_var('func_7437')
func_7439_call = mutated_mod.get_global_var('func_7439')
call_7681 = func_7437_call()
call_7682 = func_7437_call()
uop_7683 = relay.acos(uop_7627.astype('float32')) # shape=(1, 15, 11)
func_3471_call = mod.get_global_var('func_3471')
func_3473_call = mutated_mod.get_global_var('func_3473')
call_7690 = relay.TupleGetItem(func_3471_call(), 0)
call_7691 = relay.TupleGetItem(func_3473_call(), 0)
output = relay.Tuple([call_7644,bop_7651,call_7659,var_7660,bop_7674,call_7681,uop_7683,call_7690,])
output2 = relay.Tuple([call_7645,bop_7651,call_7661,var_7660,bop_7674,call_7682,uop_7683,call_7691,])
func_7696 = relay.Function([var_7626,var_7650,var_7660,], output)
mod['func_7696'] = func_7696
mod = relay.transform.InferType()(mod)
var_7697 = relay.var("var_7697", dtype = "float32", shape = (1, 15, 11))#candidate|7697|(1, 15, 11)|var|float32
var_7698 = relay.var("var_7698", dtype = "float32", shape = (7, 15, 11))#candidate|7698|(7, 15, 11)|var|float32
var_7699 = relay.var("var_7699", dtype = "int64", shape = (231,))#candidate|7699|(231,)|var|int64
output = func_7696(var_7697,var_7698,var_7699,)
func_7700 = relay.Function([var_7697,var_7698,var_7699,], output)
mutated_mod['func_7700'] = func_7700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_827_call = mod.get_global_var('func_827')
func_829_call = mutated_mod.get_global_var('func_829')
call_7719 = relay.TupleGetItem(func_827_call(), 1)
call_7720 = relay.TupleGetItem(func_829_call(), 1)
output = call_7719
output2 = call_7720
func_7744 = relay.Function([], output)
mod['func_7744'] = func_7744
mod = relay.transform.InferType()(mod)
output = func_7744()
func_7745 = relay.Function([], output)
mutated_mod['func_7745'] = func_7745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4882_call = mod.get_global_var('func_4882')
func_4884_call = mutated_mod.get_global_var('func_4884')
call_7838 = func_4882_call()
call_7839 = func_4882_call()
output = relay.Tuple([call_7838,])
output2 = relay.Tuple([call_7839,])
func_7845 = relay.Function([], output)
mod['func_7845'] = func_7845
mod = relay.transform.InferType()(mod)
output = func_7845()
func_7846 = relay.Function([], output)
mutated_mod['func_7846'] = func_7846
mutated_mod = relay.transform.InferType()(mutated_mod)
func_668_call = mod.get_global_var('func_668')
func_669_call = mutated_mod.get_global_var('func_669')
call_7868 = func_668_call()
call_7869 = func_668_call()
func_2763_call = mod.get_global_var('func_2763')
func_2764_call = mutated_mod.get_global_var('func_2764')
call_7878 = relay.TupleGetItem(func_2763_call(), 2)
call_7879 = relay.TupleGetItem(func_2764_call(), 2)
output = relay.Tuple([call_7868,call_7878,])
output2 = relay.Tuple([call_7869,call_7879,])
func_7885 = relay.Function([], output)
mod['func_7885'] = func_7885
mod = relay.transform.InferType()(mod)
mutated_mod['func_7885'] = func_7885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7885_call = mutated_mod.get_global_var('func_7885')
call_7886 = func_7885_call()
output = call_7886
func_7887 = relay.Function([], output)
mutated_mod['func_7887'] = func_7887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1136_call = mod.get_global_var('func_1136')
func_1137_call = mutated_mod.get_global_var('func_1137')
call_7926 = func_1136_call()
call_7927 = func_1136_call()
func_5132_call = mod.get_global_var('func_5132')
func_5134_call = mutated_mod.get_global_var('func_5134')
const_7929 = relay.const([3.428349,-2.870777,-1.911017,9.624619,3.735870,9.879555,-8.675741,-5.385919,-3.987796,-4.030623,-8.500775,3.578908,3.461364,-5.132689,-3.571256,2.019094,-6.469523,-6.890337,3.096411,-3.411456,-2.859863,-5.618774,-3.455292,7.272952,-6.307227,2.172757,1.021517,2.821723,8.200561,3.407984,-8.528201,8.513620,5.980147,1.026126,-3.803637,7.124490,3.361111,4.996709,-2.973391,-8.359942,-5.078549,-4.637813,5.952512,-8.737547,3.820438,-9.333323,1.723864,-8.512448,-0.780477,8.277204,2.736857,7.522948,-7.611322,-9.051305,-2.561024,2.324112,-9.459764,-1.436724,7.169996,-9.095232,9.598620,-6.444109,5.497740,4.378105,-1.157105,-9.506478,1.761391,7.871919,-6.212799,3.686638,-6.226231,0.953445,-4.568643,-4.760776,6.933525,-8.569108,-2.490581,9.258499,5.806663,4.326114,0.287526,9.866313,6.671306,-0.710547,-1.710607,-9.739027,-8.575513,5.223817,-5.260357,-9.346068,5.065143,-2.745886,7.442887,3.743215,-6.819096,-3.993278,-6.484484,-2.749931,-4.704211,1.182099,-3.684844,-5.845648,2.886140,9.679107,6.243284,4.029480,-0.754394,-1.169184,1.507553,-9.205010,-6.635178,5.386156,-7.144337,2.542791,-0.508615,3.701069,-7.719829,1.018087,-3.834042,5.973798,-6.172356,-4.490668,-4.512886,-8.489404,-9.030931,2.549951,-6.405353,7.874895,8.024863,0.759622,7.833248,-7.058788,-8.471182,0.306538,6.374383,6.136582,-7.194495,-9.185408,-5.278567,-3.003400,-1.453697,-8.082084,3.556321,2.034057,-6.227339,-7.765932,-8.492171,3.856603,0.454792,3.890258,-7.292558,-7.700151,-4.869313,8.533929,-8.652272,1.284080,-6.243973,1.881530,5.959656,-2.262197,8.411404,5.668068,2.102222,1.526003,0.624064,1.107102,4.494892,-8.642322,9.325296,-9.904757,-3.719540,-0.707706,8.089673,-7.020134,-5.287701,-9.918547,2.014768,3.971241,1.523201,6.337562,1.913433,-5.278210,4.921115,-5.246607,-0.213777,-4.918396,-5.095854,0.650186,-8.783915,-5.247776,-2.631748,-4.959392,-5.906305,2.812978,-4.252069,5.103789,3.137596,-5.125690,-6.836530,0.171555,-9.863115,6.526333,-6.551350,-7.143266,-3.540726,-5.752966,-1.027235,3.562997,-9.163677,-7.022586,8.253199,2.549164,3.181166,9.919561,-8.594832,-9.328001,-3.074533,-2.747456,0.511013,6.321197,4.993221,-5.562366,8.194324,0.427743,-8.517184,-4.476449,1.793763,9.764904,-7.288071,-5.579171,9.206190,7.900245,2.163106,5.682672,-8.044605,-0.677734,-2.056437,6.658791,-2.983538,1.150333,-8.348272,1.638739,2.436454,-6.629693,6.889579,8.736244,-8.680436,9.296399,-8.361505,-1.885807,6.453185,-4.608097,7.630741,3.278050,-1.950503,7.773489,2.041602,-8.923540,4.495935,-7.468457,-2.956654,6.500886,-5.818205,-3.410285,4.219101,3.882178,8.942295,-6.846729,-3.896673,0.388954,2.156638,8.103605,1.353531,5.401505,9.541729,3.706600,2.219403,-9.128325,9.461319,-6.841725,8.889162,-7.995479,-0.813082,7.185359,-0.621839,5.604601,5.529976,-0.462605,6.644074,9.746010,3.606512,-8.641719,-3.378229,-9.820678,4.756145,-0.611005,4.197989,8.728808,-3.870427,-9.248830,7.622981,-9.533565,-1.125775,0.900032,-0.663349,-2.188183,-9.661283,4.480274,7.946731,-5.477308,-3.981997,2.486503,9.906868,5.341694,-4.200039,5.521101,-6.383967,-4.459418,-1.530924,-7.583664,3.344073,6.690406,0.854484,-1.464119,-0.656073,0.281035,3.515328,-7.792033,7.714062,-6.753626,5.977044,-9.659641,6.337159,3.537587,-4.456464,2.853231,-1.492914,2.493634,4.285356,7.613638,2.617722,-9.316266,1.158021,3.254945,4.371971,-5.058998,0.202866,-0.845650,-1.835761,1.285672,5.243854,-8.909877,4.707027,9.840405,6.162540,-1.774706,4.727312,4.270731,-3.972031,3.582951,6.790568,-8.759804,-0.396523,9.225903,-2.157270,-5.642681,3.157999,-1.695273,-5.734515,4.036718,-8.856528,-0.223242,8.660651,-0.462406,0.375862,2.718969,-9.386141,4.644584,-9.045508,3.081426,1.439530,-2.224703,-9.415644,2.652409,-3.805239,-6.481789,6.421559,-6.195750,-2.581127,-4.419186,-7.558930,-3.864748,2.309979,-2.125027,8.669328,7.061766,0.786270,7.482026,-4.248910,-5.473580,-7.123173,1.503629,-9.403717,-5.606959,-6.272049,-9.399692,-6.310793,0.339011,-7.727143,7.573232,2.343911,7.811567,-2.137973,-0.186172,3.392482,8.725816,2.706206,6.509508,-5.352454,6.727940,-2.233817,3.115206,-1.190277,7.262221,-3.322117,-9.036782,8.898012,-5.957480,9.923129,-4.465345,-8.030773,-3.803878,-1.727575,0.780813,9.083659,8.767245,-9.105628,-2.620678,-6.572667,5.496349,-8.439315,-9.344731,6.885469,4.918497,-9.367330,-8.200768,4.307267,-8.130017,-8.568694,-7.006607,-9.647126,-5.241485,-5.615896,-6.989524,-0.677693,-6.869655,3.994889,-8.817339,0.697506,2.857772,4.897188,-2.626609,-0.910341,-8.231424,-5.485178,-4.051158,-1.967628,5.090575,7.211118,9.367259,-3.672359,-4.614604,7.416773,-9.063974,-8.691943,-5.010628,5.991116,-6.794963,7.716282,7.926792,7.211850,9.018480,-8.430998,8.105875,-8.804449,3.481338,-7.181152,-6.606538,-6.862592,-4.237086,8.236130,-8.301014,-5.855739,-2.347334,9.312700,4.993970,-5.036850,-0.519695,-5.957944,-5.368984,4.972818,3.981148,-9.696939,3.262821,-0.101404,0.621991,-8.724502,9.935411,3.987230,-5.466863,0.098744,1.476124,-8.654698,-8.729954,5.084864,9.499148,-3.000822,-6.150732,7.155047,4.054215,-2.830532,4.936674,-9.651380,5.444494,-9.629764,-5.236964,1.791255,0.826050,0.151259,-8.433901,1.298242,3.308104,-1.535490,-3.066886,9.146356,-4.561453,-9.252296,-0.277421,-0.241815,-5.490390,-2.483071,-0.588945,0.955126,4.973434,2.935055,1.772152,-9.128549,-7.859529,4.490050,-3.086001,-7.257292,-8.722387,-0.227765,7.141043,-1.075295,8.145067,-0.347783,-2.891942,-3.349762,-4.898452,-2.278152,-4.997905,5.636063,2.757281,7.640462,8.665705,-5.916907,-2.711961,5.477002,5.706975,-1.234040,-7.720996,-6.613168,-1.360603,-0.544719,-6.124785,-8.298911,5.107901,4.832489,-6.437939,-8.103934,-5.635906,8.438817,2.171657,-5.203083,-6.425415,-6.312667,2.333197,-3.136794,1.794980,7.183595,7.500402,-5.366317,1.461603,4.531825,-2.479808,1.587958,1.807898,9.106048,7.265928,2.604179,-0.672279,-1.783675,5.367383,2.721976,-8.000655,-8.168297,9.028765,-2.606143,2.992868,-8.777150,-3.578990,-1.506960,5.141673,-9.389720,-2.702046,-8.415075,3.395194,-4.495389,6.822982,6.298437,-7.464800,0.816124,-9.333586,-7.115913,-3.375696,2.246938,2.579062,-3.469362,-9.761585,5.909279,-6.879040,4.232924,2.135902,-7.980807,-4.821330,-0.676264,-4.546585,-3.579205,0.467778,-1.736151,3.306958,-7.840171,8.857600,0.312617,-3.170773,-1.729352,8.946639,-5.186782,-4.975426,6.027200,0.260469,8.122399,-0.835602,-1.291540,3.718338,3.112428,5.493815,8.630235,-4.766323,-0.995821,7.578259,6.292248,-6.620824,0.004773,9.094801,6.747369,-5.523322,-8.657038,-2.742666,1.060525,9.744356,5.690097,-7.892573,8.081338,0.175282,4.772442,7.778917,5.911180,4.469571,-3.936972,-0.274983,4.373607,-7.255841,0.662623,-4.910732,-1.404524,5.648559,-3.951768,-2.927690,-7.468678,5.443869,3.786383,-0.944297,3.226706,0.085282,-9.493788,3.339469,2.611917,0.100060,6.746976,5.287279,3.494608,4.960134,-2.573460,-0.233387,3.512945,8.120272,-9.375831,-3.502211,9.325602,1.291054,9.003285,6.253514,-8.720071,2.443627,-7.611760,-1.770390,4.928418,-8.420051,8.122767,-1.812177,-2.437362,2.993134,6.256148,-2.060093,-8.272103,2.634468,5.002328,-1.814674,8.470877,0.655914,-8.014248,-0.688589,2.802660,7.853300,9.001169,5.858117,8.040611,-8.000766,-1.143500,2.685556,-9.737410,-6.694856,4.526161,2.937289,-7.049229,5.920148,-7.294438,-1.663527,-2.713284,8.267255,5.052004,0.553709,6.449094,-6.396741,2.247583,-3.799835,-4.294412,0.554479,5.551875,-8.850096,6.436393,-4.177876,4.560940,7.371087,6.224272,6.670440,0.889790,2.357688,-7.351664,9.599702,-1.073672,5.521494,-7.879549,-1.035980,-6.541291,-4.704880,-9.480820,7.954135,1.727068,1.935592,2.459600,-2.314303], dtype = "float64")#candidate|7929|(784,)|const|float64
call_7928 = relay.TupleGetItem(func_5132_call(relay.reshape(const_7929.astype('float64'), [8, 14, 7])), 1)
call_7930 = relay.TupleGetItem(func_5134_call(relay.reshape(const_7929.astype('float64'), [8, 14, 7])), 1)
func_4294_call = mod.get_global_var('func_4294')
func_4296_call = mutated_mod.get_global_var('func_4296')
call_7938 = relay.TupleGetItem(func_4294_call(), 0)
call_7939 = relay.TupleGetItem(func_4296_call(), 0)
func_2817_call = mod.get_global_var('func_2817')
func_2819_call = mutated_mod.get_global_var('func_2819')
call_7945 = relay.TupleGetItem(func_2817_call(), 0)
call_7946 = relay.TupleGetItem(func_2819_call(), 0)
output = relay.Tuple([call_7926,call_7928,const_7929,call_7938,call_7945,])
output2 = relay.Tuple([call_7927,call_7930,const_7929,call_7939,call_7946,])
func_7962 = relay.Function([], output)
mod['func_7962'] = func_7962
mod = relay.transform.InferType()(mod)
output = func_7962()
func_7963 = relay.Function([], output)
mutated_mod['func_7963'] = func_7963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3386_call = mod.get_global_var('func_3386')
func_3388_call = mutated_mod.get_global_var('func_3388')
call_8064 = relay.TupleGetItem(func_3386_call(), 0)
call_8065 = relay.TupleGetItem(func_3388_call(), 0)
func_1569_call = mod.get_global_var('func_1569')
func_1571_call = mutated_mod.get_global_var('func_1571')
call_8104 = relay.TupleGetItem(func_1569_call(), 0)
call_8105 = relay.TupleGetItem(func_1571_call(), 0)
func_1468_call = mod.get_global_var('func_1468')
func_1470_call = mutated_mod.get_global_var('func_1470')
call_8113 = relay.TupleGetItem(func_1468_call(), 2)
call_8114 = relay.TupleGetItem(func_1470_call(), 2)
func_7261_call = mod.get_global_var('func_7261')
func_7263_call = mutated_mod.get_global_var('func_7263')
call_8120 = relay.TupleGetItem(func_7261_call(), 0)
call_8121 = relay.TupleGetItem(func_7263_call(), 0)
func_1717_call = mod.get_global_var('func_1717')
func_1718_call = mutated_mod.get_global_var('func_1718')
call_8153 = func_1717_call()
call_8154 = func_1717_call()
output = relay.Tuple([call_8064,call_8104,call_8113,call_8120,call_8153,])
output2 = relay.Tuple([call_8065,call_8105,call_8114,call_8121,call_8154,])
func_8167 = relay.Function([], output)
mod['func_8167'] = func_8167
mod = relay.transform.InferType()(mod)
output = func_8167()
func_8168 = relay.Function([], output)
mutated_mod['func_8168'] = func_8168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3471_call = mod.get_global_var('func_3471')
func_3473_call = mutated_mod.get_global_var('func_3473')
call_8192 = relay.TupleGetItem(func_3471_call(), 2)
call_8193 = relay.TupleGetItem(func_3473_call(), 2)
output = relay.Tuple([call_8192,])
output2 = relay.Tuple([call_8193,])
func_8218 = relay.Function([], output)
mod['func_8218'] = func_8218
mod = relay.transform.InferType()(mod)
mutated_mod['func_8218'] = func_8218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8218_call = mutated_mod.get_global_var('func_8218')
call_8219 = func_8218_call()
output = call_8219
func_8220 = relay.Function([], output)
mutated_mod['func_8220'] = func_8220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5032_call = mod.get_global_var('func_5032')
func_5033_call = mutated_mod.get_global_var('func_5033')
call_8229 = relay.TupleGetItem(func_5032_call(), 1)
call_8230 = relay.TupleGetItem(func_5033_call(), 1)
func_1070_call = mod.get_global_var('func_1070')
func_1072_call = mutated_mod.get_global_var('func_1072')
call_8244 = relay.TupleGetItem(func_1070_call(relay.reshape(call_8229.astype('float64'), [10, 7, 2])), 1)
call_8245 = relay.TupleGetItem(func_1072_call(relay.reshape(call_8229.astype('float64'), [10, 7, 2])), 1)
func_2763_call = mod.get_global_var('func_2763')
func_2764_call = mutated_mod.get_global_var('func_2764')
call_8263 = relay.TupleGetItem(func_2763_call(), 0)
call_8264 = relay.TupleGetItem(func_2764_call(), 0)
func_2763_call = mod.get_global_var('func_2763')
func_2764_call = mutated_mod.get_global_var('func_2764')
call_8266 = relay.TupleGetItem(func_2763_call(), 0)
call_8267 = relay.TupleGetItem(func_2764_call(), 0)
output = relay.Tuple([call_8229,call_8244,call_8263,call_8266,])
output2 = relay.Tuple([call_8230,call_8245,call_8264,call_8267,])
func_8281 = relay.Function([], output)
mod['func_8281'] = func_8281
mod = relay.transform.InferType()(mod)
output = func_8281()
func_8282 = relay.Function([], output)
mutated_mod['func_8282'] = func_8282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5913_call = mod.get_global_var('func_5913')
func_5914_call = mutated_mod.get_global_var('func_5914')
call_8313 = relay.TupleGetItem(func_5913_call(), 0)
call_8314 = relay.TupleGetItem(func_5914_call(), 0)
output = relay.Tuple([call_8313,])
output2 = relay.Tuple([call_8314,])
func_8315 = relay.Function([], output)
mod['func_8315'] = func_8315
mod = relay.transform.InferType()(mod)
mutated_mod['func_8315'] = func_8315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8315_call = mutated_mod.get_global_var('func_8315')
call_8316 = func_8315_call()
output = call_8316
func_8317 = relay.Function([], output)
mutated_mod['func_8317'] = func_8317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3097_call = mod.get_global_var('func_3097')
func_3099_call = mutated_mod.get_global_var('func_3099')
call_8357 = func_3097_call()
call_8358 = func_3097_call()
func_6793_call = mod.get_global_var('func_6793')
func_6794_call = mutated_mod.get_global_var('func_6794')
call_8368 = relay.TupleGetItem(func_6793_call(), 0)
call_8369 = relay.TupleGetItem(func_6794_call(), 0)
output = relay.Tuple([call_8357,call_8368,])
output2 = relay.Tuple([call_8358,call_8369,])
func_8376 = relay.Function([], output)
mod['func_8376'] = func_8376
mod = relay.transform.InferType()(mod)
output = func_8376()
func_8377 = relay.Function([], output)
mutated_mod['func_8377'] = func_8377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6876_call = mod.get_global_var('func_6876')
func_6878_call = mutated_mod.get_global_var('func_6878')
call_8408 = relay.TupleGetItem(func_6876_call(), 0)
call_8409 = relay.TupleGetItem(func_6878_call(), 0)
output = relay.Tuple([call_8408,])
output2 = relay.Tuple([call_8409,])
func_8416 = relay.Function([], output)
mod['func_8416'] = func_8416
mod = relay.transform.InferType()(mod)
mutated_mod['func_8416'] = func_8416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8416_call = mutated_mod.get_global_var('func_8416')
call_8417 = func_8416_call()
output = call_8417
func_8418 = relay.Function([], output)
mutated_mod['func_8418'] = func_8418
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8430 = relay.var("var_8430", dtype = "uint16", shape = (6, 16, 11))#candidate|8430|(6, 16, 11)|var|uint16
var_8431 = relay.var("var_8431", dtype = "uint16", shape = (6, 16, 11))#candidate|8431|(6, 16, 11)|var|uint16
bop_8432 = relay.multiply(var_8430.astype('uint16'), relay.reshape(var_8431.astype('uint16'), relay.shape_of(var_8430))) # shape=(6, 16, 11)
output = bop_8432
output2 = bop_8432
func_8438 = relay.Function([var_8430,var_8431,], output)
mod['func_8438'] = func_8438
mod = relay.transform.InferType()(mod)
var_8439 = relay.var("var_8439", dtype = "uint16", shape = (6, 16, 11))#candidate|8439|(6, 16, 11)|var|uint16
var_8440 = relay.var("var_8440", dtype = "uint16", shape = (6, 16, 11))#candidate|8440|(6, 16, 11)|var|uint16
output = func_8438(var_8439,var_8440,)
func_8441 = relay.Function([var_8439,var_8440,], output)
mutated_mod['func_8441'] = func_8441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5688_call = mod.get_global_var('func_5688')
func_5689_call = mutated_mod.get_global_var('func_5689')
call_8445 = relay.TupleGetItem(func_5688_call(), 3)
call_8446 = relay.TupleGetItem(func_5689_call(), 3)
uop_8453 = relay.log2(call_8445.astype('float32')) # shape=(7, 2, 4)
uop_8455 = relay.log2(call_8446.astype('float32')) # shape=(7, 2, 4)
output = uop_8453
output2 = uop_8455
func_8485 = relay.Function([], output)
mod['func_8485'] = func_8485
mod = relay.transform.InferType()(mod)
mutated_mod['func_8485'] = func_8485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8485_call = mutated_mod.get_global_var('func_8485')
call_8486 = func_8485_call()
output = call_8486
func_8487 = relay.Function([], output)
mutated_mod['func_8487'] = func_8487
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6931_call = mod.get_global_var('func_6931')
func_6932_call = mutated_mod.get_global_var('func_6932')
call_8546 = relay.TupleGetItem(func_6931_call(), 0)
call_8547 = relay.TupleGetItem(func_6932_call(), 0)
func_2523_call = mod.get_global_var('func_2523')
func_2525_call = mutated_mod.get_global_var('func_2525')
call_8593 = func_2523_call()
call_8594 = func_2523_call()
func_1862_call = mod.get_global_var('func_1862')
func_1864_call = mutated_mod.get_global_var('func_1864')
call_8602 = relay.TupleGetItem(func_1862_call(), 1)
call_8603 = relay.TupleGetItem(func_1864_call(), 1)
output = relay.Tuple([call_8546,call_8593,call_8602,])
output2 = relay.Tuple([call_8547,call_8594,call_8603,])
func_8604 = relay.Function([], output)
mod['func_8604'] = func_8604
mod = relay.transform.InferType()(mod)
mutated_mod['func_8604'] = func_8604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8604_call = mutated_mod.get_global_var('func_8604')
call_8605 = func_8604_call()
output = call_8605
func_8606 = relay.Function([], output)
mutated_mod['func_8606'] = func_8606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8604_call = mod.get_global_var('func_8604')
func_8606_call = mutated_mod.get_global_var('func_8606')
call_8701 = relay.TupleGetItem(func_8604_call(), 1)
call_8702 = relay.TupleGetItem(func_8606_call(), 1)
output = call_8701
output2 = call_8702
func_8710 = relay.Function([], output)
mod['func_8710'] = func_8710
mod = relay.transform.InferType()(mod)
mutated_mod['func_8710'] = func_8710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8710_call = mutated_mod.get_global_var('func_8710')
call_8711 = func_8710_call()
output = call_8711
func_8712 = relay.Function([], output)
mutated_mod['func_8712'] = func_8712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6793_call = mod.get_global_var('func_6793')
func_6794_call = mutated_mod.get_global_var('func_6794')
call_8752 = relay.TupleGetItem(func_6793_call(), 2)
call_8753 = relay.TupleGetItem(func_6794_call(), 2)
func_751_call = mod.get_global_var('func_751')
func_752_call = mutated_mod.get_global_var('func_752')
call_8756 = relay.TupleGetItem(func_751_call(), 1)
call_8757 = relay.TupleGetItem(func_752_call(), 1)
output = relay.Tuple([call_8752,call_8756,])
output2 = relay.Tuple([call_8753,call_8757,])
func_8761 = relay.Function([], output)
mod['func_8761'] = func_8761
mod = relay.transform.InferType()(mod)
mutated_mod['func_8761'] = func_8761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8761_call = mutated_mod.get_global_var('func_8761')
call_8762 = func_8761_call()
output = call_8762
func_8763 = relay.Function([], output)
mutated_mod['func_8763'] = func_8763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_668_call = mod.get_global_var('func_668')
func_669_call = mutated_mod.get_global_var('func_669')
call_8793 = func_668_call()
call_8794 = func_668_call()
func_4417_call = mod.get_global_var('func_4417')
func_4422_call = mutated_mod.get_global_var('func_4422')
const_8811 = relay.const([[8,-2,1,-3,9,-8,6,-2,-8,-3,-8,-8,-7,-9,4,-5,-5,9,5,7,-5,3,-4,6,-9,-4,1,-1,-8,-7,6,-5,1,5,3,9,6,1,-6,1,-6,-6,9,-7,-8,9,8,-4,-7,4,2,2,-7,9,2,1,-7,6,4,2,10,7,7,-7,-4,-8,6,6,5,-7,5,4,4,-7,1,-4,3,1,5,-6,-10,-3,6,-2,-5,5,-6,2,-7,2,-10,-1,8,-5,-1,-9,-7,9,-4,-2,7,-6,6,-5,-7,-3,3,-2,-7,3,-9,-8,7,-10,6,9,-3,8,-5,2,-4,-8,2,-10,-6,6,-5,2,2,4,-7,-5,10,-10,8,6,9,-9,-6,10,1,-7,-2,2,-2,6,-9,-10,4,-3,-3,6,-3,-5,-5,-2,2,-7,-10,-10,5,-4,5,-3,-3,3,5,8],[-4,8,-7,-6,-10,5,1,-4,9,1,1,5,2,2,5,7,4,-9,-8,9,-7,9,10,-4,-1,-5,1,-8,5,-10,1,-10,-5,-5,-3,4,-1,-9,8,9,8,-4,3,-2,4,-9,-9,8,-5,10,9,9,7,-10,1,4,5,-8,10,5,2,-8,2,-9,-1,6,-3,2,2,6,-3,-3,-10,5,3,-5,5,-7,1,5,-5,4,5,-7,-7,-2,-5,9,8,-7,-5,3,6,-6,-6,-7,-9,8,-6,-4,-9,-5,1,-10,-9,7,9,-3,-10,2,-9,6,1,-3,10,-3,-2,-3,-4,2,-2,-7,-9,-8,1,-8,8,-8,9,-7,9,-7,-8,-5,-5,-8,-6,-10,7,-7,-7,-9,-10,-7,8,-7,3,9,-4,6,3,-6,10,5,5,8,-8,8,-3,4,-8,10,3,-5,-6,-6,-6,8],[-10,3,-7,-7,5,-1,-2,-2,6,-4,-1,-7,1,-4,8,10,4,-3,-4,4,-8,10,9,-10,1,-5,-2,-9,-8,9,4,-5,-5,-9,-3,-10,9,-10,-9,-5,-6,-5,7,-3,-9,-2,-6,-3,-7,1,7,-10,-1,-7,5,-3,6,-9,-3,7,-9,-5,8,-7,10,7,-9,-8,-1,1,8,-5,3,7,-8,-6,-7,-1,10,-2,-6,-10,9,-5,2,4,-1,6,5,-8,2,-2,-6,4,1,-8,6,-3,-7,-3,4,1,-6,-9,-4,6,2,5,-2,-8,6,1,-4,-6,3,-2,-7,-4,3,8,2,-5,3,-6,10,10,-10,9,5,6,5,7,-2,8,6,-5,1,5,-2,9,-5,-2,-1,-10,6,-4,-4,4,-4,5,8,8,-2,3,6,-9,-2,5,-2,10,10,9,-7,-2,-5,8,-7,-5],[1,-6,-4,7,6,9,-6,-5,3,10,7,8,9,7,6,8,2,4,6,1,-3,9,-7,4,8,-9,-6,-5,7,-4,6,10,-5,-3,6,-5,4,6,8,-3,-6,9,1,8,8,9,-3,1,3,-8,-9,6,7,-9,4,1,-4,3,-6,1,4,-7,9,4,5,-9,-5,10,-6,6,10,-1,8,8,-4,8,-9,4,5,7,2,-4,10,-8,2,-8,3,-7,-5,5,-5,7,7,1,-1,-10,6,-9,-8,5,-5,2,-4,9,5,-9,6,-4,1,-5,-4,5,-8,8,-5,6,6,6,-1,9,8,4,-6,-8,-4,9,-5,9,3,9,-8,6,7,4,-8,1,3,-1,-6,7,-10,-7,3,10,1,3,-8,-3,-10,2,4,-5,3,-7,5,-6,-2,-1,6,2,3,-9,4,-8,3,-4,5,3]], dtype = "uint16")#candidate|8811|(4, 168)|const|uint16
call_8810 = relay.TupleGetItem(func_4417_call(relay.reshape(const_8811.astype('uint16'), [16, 14, 3]), relay.reshape(const_8811.astype('uint16'), [16, 14, 3]), relay.reshape(const_8811.astype('float64'), [16, 14, 3]), ), 2)
call_8812 = relay.TupleGetItem(func_4422_call(relay.reshape(const_8811.astype('uint16'), [16, 14, 3]), relay.reshape(const_8811.astype('uint16'), [16, 14, 3]), relay.reshape(const_8811.astype('float64'), [16, 14, 3]), ), 2)
output = relay.Tuple([call_8793,call_8810,const_8811,])
output2 = relay.Tuple([call_8794,call_8812,const_8811,])
func_8817 = relay.Function([], output)
mod['func_8817'] = func_8817
mod = relay.transform.InferType()(mod)
mutated_mod['func_8817'] = func_8817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8817_call = mutated_mod.get_global_var('func_8817')
call_8818 = func_8817_call()
output = call_8818
func_8819 = relay.Function([], output)
mutated_mod['func_8819'] = func_8819
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8761_call = mod.get_global_var('func_8761')
func_8763_call = mutated_mod.get_global_var('func_8763')
call_8831 = relay.TupleGetItem(func_8761_call(), 0)
call_8832 = relay.TupleGetItem(func_8763_call(), 0)
var_8835 = relay.var("var_8835", dtype = "float32", shape = (14, 9, 7))#candidate|8835|(14, 9, 7)|var|float32
bop_8836 = relay.power(call_8831.astype('float32'), relay.reshape(var_8835.astype('float32'), relay.shape_of(call_8831))) # shape=(14, 9, 7)
bop_8839 = relay.power(call_8832.astype('float32'), relay.reshape(var_8835.astype('float32'), relay.shape_of(call_8832))) # shape=(14, 9, 7)
output = bop_8836
output2 = bop_8839
func_8854 = relay.Function([var_8835,], output)
mod['func_8854'] = func_8854
mod = relay.transform.InferType()(mod)
mutated_mod['func_8854'] = func_8854
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8855 = relay.var("var_8855", dtype = "float32", shape = (14, 9, 7))#candidate|8855|(14, 9, 7)|var|float32
func_8854_call = mutated_mod.get_global_var('func_8854')
call_8856 = func_8854_call(var_8855)
output = call_8856
func_8857 = relay.Function([var_8855], output)
mutated_mod['func_8857'] = func_8857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8315_call = mod.get_global_var('func_8315')
func_8317_call = mutated_mod.get_global_var('func_8317')
call_8910 = relay.TupleGetItem(func_8315_call(), 0)
call_8911 = relay.TupleGetItem(func_8317_call(), 0)
output = call_8910
output2 = call_8911
func_8927 = relay.Function([], output)
mod['func_8927'] = func_8927
mod = relay.transform.InferType()(mod)
mutated_mod['func_8927'] = func_8927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8927_call = mutated_mod.get_global_var('func_8927')
call_8928 = func_8927_call()
output = call_8928
func_8929 = relay.Function([], output)
mutated_mod['func_8929'] = func_8929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3097_call = mod.get_global_var('func_3097')
func_3099_call = mutated_mod.get_global_var('func_3099')
call_8976 = func_3097_call()
call_8977 = func_3097_call()
func_7696_call = mod.get_global_var('func_7696')
func_7700_call = mutated_mod.get_global_var('func_7700')
var_8983 = relay.var("var_8983", dtype = "float32", shape = (165,))#candidate|8983|(165,)|var|float32
var_8984 = relay.var("var_8984", dtype = "float32", shape = (7, 165))#candidate|8984|(7, 165)|var|float32
var_8985 = relay.var("var_8985", dtype = "int64", shape = (231,))#candidate|8985|(231,)|var|int64
call_8982 = relay.TupleGetItem(func_7696_call(relay.reshape(var_8983.astype('float32'), [1, 15, 11]), relay.reshape(var_8984.astype('float32'), [7, 15, 11]), relay.reshape(var_8985.astype('int64'), [231,]), ), 2)
call_8986 = relay.TupleGetItem(func_7700_call(relay.reshape(var_8983.astype('float32'), [1, 15, 11]), relay.reshape(var_8984.astype('float32'), [7, 15, 11]), relay.reshape(var_8985.astype('int64'), [231,]), ), 2)
output = relay.Tuple([call_8976,call_8982,var_8983,var_8984,var_8985,])
output2 = relay.Tuple([call_8977,call_8986,var_8983,var_8984,var_8985,])
func_9002 = relay.Function([var_8983,var_8984,var_8985,], output)
mod['func_9002'] = func_9002
mod = relay.transform.InferType()(mod)
var_9003 = relay.var("var_9003", dtype = "float32", shape = (165,))#candidate|9003|(165,)|var|float32
var_9004 = relay.var("var_9004", dtype = "float32", shape = (7, 165))#candidate|9004|(7, 165)|var|float32
var_9005 = relay.var("var_9005", dtype = "int64", shape = (231,))#candidate|9005|(231,)|var|int64
output = func_9002(var_9003,var_9004,var_9005,)
func_9006 = relay.Function([var_9003,var_9004,var_9005,], output)
mutated_mod['func_9006'] = func_9006
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3065_call = mod.get_global_var('func_3065')
func_3066_call = mutated_mod.get_global_var('func_3066')
call_9028 = func_3065_call()
call_9029 = func_3065_call()
func_6433_call = mod.get_global_var('func_6433')
func_6434_call = mutated_mod.get_global_var('func_6434')
call_9047 = relay.TupleGetItem(func_6433_call(), 0)
call_9048 = relay.TupleGetItem(func_6434_call(), 0)
output = relay.Tuple([call_9028,call_9047,])
output2 = relay.Tuple([call_9029,call_9048,])
func_9062 = relay.Function([], output)
mod['func_9062'] = func_9062
mod = relay.transform.InferType()(mod)
output = func_9062()
func_9063 = relay.Function([], output)
mutated_mod['func_9063'] = func_9063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3976_call = mod.get_global_var('func_3976')
func_3978_call = mutated_mod.get_global_var('func_3978')
call_9101 = relay.TupleGetItem(func_3976_call(), 0)
call_9102 = relay.TupleGetItem(func_3978_call(), 0)
output = call_9101
output2 = call_9102
func_9103 = relay.Function([], output)
mod['func_9103'] = func_9103
mod = relay.transform.InferType()(mod)
mutated_mod['func_9103'] = func_9103
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9103_call = mutated_mod.get_global_var('func_9103')
call_9104 = func_9103_call()
output = call_9104
func_9105 = relay.Function([], output)
mutated_mod['func_9105'] = func_9105
mutated_mod = relay.transform.InferType()(mutated_mod)
func_827_call = mod.get_global_var('func_827')
func_829_call = mutated_mod.get_global_var('func_829')
call_9110 = relay.TupleGetItem(func_827_call(), 1)
call_9111 = relay.TupleGetItem(func_829_call(), 1)
func_1308_call = mod.get_global_var('func_1308')
func_1310_call = mutated_mod.get_global_var('func_1310')
call_9115 = func_1308_call()
call_9116 = func_1308_call()
output = relay.Tuple([call_9110,call_9115,])
output2 = relay.Tuple([call_9111,call_9116,])
func_9118 = relay.Function([], output)
mod['func_9118'] = func_9118
mod = relay.transform.InferType()(mod)
output = func_9118()
func_9119 = relay.Function([], output)
mutated_mod['func_9119'] = func_9119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7437_call = mod.get_global_var('func_7437')
func_7439_call = mutated_mod.get_global_var('func_7439')
call_9154 = func_7437_call()
call_9155 = func_7437_call()
output = relay.Tuple([call_9154,])
output2 = relay.Tuple([call_9155,])
func_9167 = relay.Function([], output)
mod['func_9167'] = func_9167
mod = relay.transform.InferType()(mod)
mutated_mod['func_9167'] = func_9167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9167_call = mutated_mod.get_global_var('func_9167')
call_9168 = func_9167_call()
output = call_9168
func_9169 = relay.Function([], output)
mutated_mod['func_9169'] = func_9169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3827_call = mod.get_global_var('func_3827')
func_3828_call = mutated_mod.get_global_var('func_3828')
call_9170 = relay.TupleGetItem(func_3827_call(), 1)
call_9171 = relay.TupleGetItem(func_3828_call(), 1)
func_4286_call = mod.get_global_var('func_4286')
func_4287_call = mutated_mod.get_global_var('func_4287')
call_9184 = func_4286_call()
call_9185 = func_4286_call()
output = relay.Tuple([call_9170,call_9184,])
output2 = relay.Tuple([call_9171,call_9185,])
func_9186 = relay.Function([], output)
mod['func_9186'] = func_9186
mod = relay.transform.InferType()(mod)
mutated_mod['func_9186'] = func_9186
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9186_call = mutated_mod.get_global_var('func_9186')
call_9187 = func_9186_call()
output = call_9187
func_9188 = relay.Function([], output)
mutated_mod['func_9188'] = func_9188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4992_call = mod.get_global_var('func_4992')
func_4994_call = mutated_mod.get_global_var('func_4994')
call_9205 = relay.TupleGetItem(func_4992_call(), 1)
call_9206 = relay.TupleGetItem(func_4994_call(), 1)
output = relay.Tuple([call_9205,])
output2 = relay.Tuple([call_9206,])
func_9227 = relay.Function([], output)
mod['func_9227'] = func_9227
mod = relay.transform.InferType()(mod)
output = func_9227()
func_9228 = relay.Function([], output)
mutated_mod['func_9228'] = func_9228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6746_call = mod.get_global_var('func_6746')
func_6747_call = mutated_mod.get_global_var('func_6747')
call_9310 = relay.TupleGetItem(func_6746_call(), 1)
call_9311 = relay.TupleGetItem(func_6747_call(), 1)
output = call_9310
output2 = call_9311
func_9318 = relay.Function([], output)
mod['func_9318'] = func_9318
mod = relay.transform.InferType()(mod)
mutated_mod['func_9318'] = func_9318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9318_call = mutated_mod.get_global_var('func_9318')
call_9319 = func_9318_call()
output = call_9319
func_9320 = relay.Function([], output)
mutated_mod['func_9320'] = func_9320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7885_call = mod.get_global_var('func_7885')
func_7887_call = mutated_mod.get_global_var('func_7887')
call_9400 = relay.TupleGetItem(func_7885_call(), 1)
call_9401 = relay.TupleGetItem(func_7887_call(), 1)
output = call_9400
output2 = call_9401
func_9413 = relay.Function([], output)
mod['func_9413'] = func_9413
mod = relay.transform.InferType()(mod)
output = func_9413()
func_9414 = relay.Function([], output)
mutated_mod['func_9414'] = func_9414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4286_call = mod.get_global_var('func_4286')
func_4287_call = mutated_mod.get_global_var('func_4287')
call_9423 = func_4286_call()
call_9424 = func_4286_call()
output = call_9423
output2 = call_9424
func_9438 = relay.Function([], output)
mod['func_9438'] = func_9438
mod = relay.transform.InferType()(mod)
output = func_9438()
func_9439 = relay.Function([], output)
mutated_mod['func_9439'] = func_9439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1717_call = mod.get_global_var('func_1717')
func_1718_call = mutated_mod.get_global_var('func_1718')
call_9467 = func_1717_call()
call_9468 = func_1717_call()
func_4417_call = mod.get_global_var('func_4417')
func_4422_call = mutated_mod.get_global_var('func_4422')
const_9490 = relay.const([-7,-7,-8,-10,-3,1,-1,6,-10,-6,-3,-4,-8,2,-6,1,3,-8,7,2,-10,-1,-3,-4,-3,-8,5,5,2,9,8,1,-1,4,5,-9,-8,6,9,-2,4,1,9,-3,7,9,3,9,-7,2,-1,-8,3,-8,-6,5,10,1,3,-2,-5,6,-1,2,9,1,-6,9,-1,-10,-7,8,2,-9,-3,-5,-2,-8,5,-10,-3,4,-9,9,-8,-8,-5,-4,-8,-3,-4,9,7,-10,7,-7,-2,-2,-4,1,-1,10,-7,-4,-5,-4,-5,-6,10,7,7,-10,6,10,-2,-3,9,-8,6,-9,-8,4,8,6,-8,-7,-6,4,8,2,-4,-2,8,9,-3,9,-3,-5,-2,3,1,-5,-7,-10,4,7,-9,-10,1,3,8,-5,6,6,-8,-8,-8,-7,3,-2,-1,4,9,7,3,-6,-3,-6,9,-6,8,10,-8,-3,-6,7,-3,5,5,4,1,3,-10,-4,-8,8,4,-3,4,-5,-10,-8,-5,7,-5,10,-10,2,1,-9,-6,-6,-6,5,7,-2,4,10,-3,9,-7,-5,-3,6,-5,-2,3,-3,9,1,-10,4,1,3,-10,-1,3,-5,5,8,-8,10,8,-2,-3,-4,-4,-7,2,-10,-2,1,-8,-10,8,2,-8,-7,8,-5,2,2,-10,2,6,-4,2,-4,2,3,3,5,-8,10,-2,6,6,10,6,-8,4,3,-7,-4,10,-10,3,-4,8,6,1,-5,-10,3,-7,-10,-10,6,-9,-10,-10,-4,6,5,-4,-5,2,9,7,10,10,-6,5,2,4,5,-4,6,-8,3,1,4,10,-9,-7,10,9,2,9,7,7,7,10,-1,-6,10,-4,5,10,-2,1,6,9,-3,3,-10,-2,2,-2,-4,-7,8,-9,-7,4,-9,1,-6,-5,-9,-9,-9,-7,6,-1,-10,5,2,-10,6,-8,3,-10,10,-8,-2,-7,9,-1,5,-7,2,4,5,-3,-2,-6,8,1,-9,-8,-5,3,1,3,8,3,-2,-4,-3,-10,5,7,9,-5,7,3,-8,-10,-2,5,2,10,4,-1,-10,-1,6,-2,6,-7,-1,-8,9,-8,-10,-1,-10,4,-6,1,7,-4,-10,2,-4,-2,9,3,-6,9,3,-8,-2,7,1,-7,-1,-5,-7,-8,6,-7,-8,5,1,-1,3,-7,6,-6,-3,-5,-1,-5,7,-1,-3,-8,-9,6,6,-4,1,-7,-5,-3,-3,3,9,4,1,-9,-2,-5,1,-10,-3,5,4,-10,-4,-9,1,10,-10,-8,-10,5,-5,2,6,-2,-6,4,10,1,6,8,2,9,-6,2,5,7,-10,5,-3,-4,5,-1,9,-8,1,-4,6,2,-10,8,-2,5,-6,-7,-9,-9,6,-1,1,-1,5,-3,9,-5,-2,2,9,-7,10,-5,-2,5,-4,6,-6,-8,-4,-4,-8,2,3,5,3,-9,5,-4,-10,-6,7,-10,1,-4,8,-8,10,-8,7,-4,-5,-5,-7,-7,10,-1,-7,10,8,-3,-3,-3,-2,-5,-4,1,-2,-10,-5,-5,-2,2,7,7,5,2,-2,2,-7,7,7,-1,-2,9,-9,4,1,3,5,3,-2,9,-1,-2,-9,-10,-4,-7,-1,6,1,3,6,-3,-6,3,3,-3,-5,3,-3,2,3,6,6,-7,-1,-2,-6,10,-1,-9,-6,-9,9,-7,-6,-8,8,4,-5,2,1,7,-7,9,-1,-2,-3,8,-4,2,3,8,5,7,3,8,-1,1,-1,8,9,8,1], dtype = "uint16")#candidate|9490|(672,)|const|uint16
call_9489 = relay.TupleGetItem(func_4417_call(relay.reshape(const_9490.astype('uint16'), [16, 14, 3]), relay.reshape(const_9490.astype('uint16'), [16, 14, 3]), relay.reshape(const_9490.astype('float64'), [16, 14, 3]), ), 2)
call_9491 = relay.TupleGetItem(func_4422_call(relay.reshape(const_9490.astype('uint16'), [16, 14, 3]), relay.reshape(const_9490.astype('uint16'), [16, 14, 3]), relay.reshape(const_9490.astype('float64'), [16, 14, 3]), ), 2)
uop_9495 = relay.acos(call_9489.astype('float64')) # shape=(49, 10)
uop_9497 = relay.acos(call_9491.astype('float64')) # shape=(49, 10)
output = relay.Tuple([call_9467,const_9490,uop_9495,])
output2 = relay.Tuple([call_9468,const_9490,uop_9497,])
func_9500 = relay.Function([], output)
mod['func_9500'] = func_9500
mod = relay.transform.InferType()(mod)
mutated_mod['func_9500'] = func_9500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9500_call = mutated_mod.get_global_var('func_9500')
call_9501 = func_9500_call()
output = call_9501
func_9502 = relay.Function([], output)
mutated_mod['func_9502'] = func_9502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7845_call = mod.get_global_var('func_7845')
func_7846_call = mutated_mod.get_global_var('func_7846')
call_9512 = relay.TupleGetItem(func_7845_call(), 0)
call_9513 = relay.TupleGetItem(func_7846_call(), 0)
func_1653_call = mod.get_global_var('func_1653')
func_1657_call = mutated_mod.get_global_var('func_1657')
const_9537 = relay.const([-3,9,-8,-3,-5,-2,-5,-3,9,2,-6,9,9,-10,-10,-9,9,-3,6,10,2,-4,6,-9,1,-4,8,-3,-3,-1,1,-8,-9,7,-8,9,-10,10,2,1,-3,-10,-2,-7,5,-10,2,-7,10,6,-1,-9,-10,7,8,-7,6,-3,10,3,-10,6,-10,2,-6,-9,3,-10,-7,-7,6,8,-1,10,1,-1,-4,-4,9,-6,4,4,3,2,-2,5,-3,1,3,7,3,-6,4,-1,6,8,3,9,7,-6,-2,-8,-5,1,8,-4,8,8,-10,5,-8,-5,-6,-7,-6,1,-3,3,7,7,-3,-8,9,-3,7,-4,-2,6,-5,-10,-3,9,1,5,7,5,1,3,9,10,5,-1,-6,4,9,2,-6,-9,4,-4,5,3,3,7,-3,8,-4,-6,7,2,3,-7,5,-3,-7,2,-6,-10,-2,-1,-8,6,1,2,1,1,10,-2,-1,3,-3,1,-9,-10,-10,9,-3,9,6,-9,7,-10,7,9,-8,9,-9,-3,-1,-1,-6,-8,7,3,9,10,-4,-1,4,-1,6,4,-10,4,-9,-4,-7,-6,-8,-8,10,2,-10,-5,7,-7,-7,6,7,1,-7,3,-7,-8,7,-1,6,1,8,-2,-3,8,7,7,4,-2,-5,4,-3,7,10,4,-3,6,10,-8,5,3,10,8,10,-4,4,-6,-4,-6,3,2,7,-9,6,-2,-3,-4,6,6,1,-10,-10,1,-3,8,-7,4,-10,10,10,4,-6,-6,-10,8,-2,6,9,6,4,-6,4,-6,-4,-8,-10,-8,3,-9,-6,-4,-7,8,10,6,8,7,-3], dtype = "uint32")#candidate|9537|(315,)|const|uint32
var_9538 = relay.var("var_9538", dtype = "float32", shape = (1, 12))#candidate|9538|(1, 12)|var|float32
var_9539 = relay.var("var_9539", dtype = "int32", shape = (56,))#candidate|9539|(56,)|var|int32
call_9536 = relay.TupleGetItem(func_1653_call(relay.reshape(const_9537.astype('uint32'), [5, 7, 9]), relay.reshape(var_9538.astype('float32'), [12,]), relay.reshape(var_9539.astype('int32'), [56,]), ), 7)
call_9540 = relay.TupleGetItem(func_1657_call(relay.reshape(const_9537.astype('uint32'), [5, 7, 9]), relay.reshape(var_9538.astype('float32'), [12,]), relay.reshape(var_9539.astype('int32'), [56,]), ), 7)
output = relay.Tuple([call_9512,call_9536,const_9537,var_9538,var_9539,])
output2 = relay.Tuple([call_9513,call_9540,const_9537,var_9538,var_9539,])
func_9548 = relay.Function([var_9538,var_9539,], output)
mod['func_9548'] = func_9548
mod = relay.transform.InferType()(mod)
mutated_mod['func_9548'] = func_9548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9548_call = mutated_mod.get_global_var('func_9548')
var_9550 = relay.var("var_9550", dtype = "float32", shape = (1, 12))#candidate|9550|(1, 12)|var|float32
var_9551 = relay.var("var_9551", dtype = "int32", shape = (56,))#candidate|9551|(56,)|var|int32
call_9549 = func_9548_call(var_9550,var_9551,)
output = call_9549
func_9552 = relay.Function([var_9550,var_9551,], output)
mutated_mod['func_9552'] = func_9552
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5205_call = mod.get_global_var('func_5205')
func_5206_call = mutated_mod.get_global_var('func_5206')
call_9572 = relay.TupleGetItem(func_5205_call(), 0)
call_9573 = relay.TupleGetItem(func_5206_call(), 0)
func_1070_call = mod.get_global_var('func_1070')
func_1072_call = mutated_mod.get_global_var('func_1072')
call_9576 = relay.TupleGetItem(func_1070_call(relay.reshape(call_9572.astype('float64'), [10, 7, 2])), 0)
call_9577 = relay.TupleGetItem(func_1072_call(relay.reshape(call_9572.astype('float64'), [10, 7, 2])), 0)
output = relay.Tuple([call_9572,call_9576,])
output2 = relay.Tuple([call_9573,call_9577,])
func_9580 = relay.Function([], output)
mod['func_9580'] = func_9580
mod = relay.transform.InferType()(mod)
output = func_9580()
func_9581 = relay.Function([], output)
mutated_mod['func_9581'] = func_9581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5688_call = mod.get_global_var('func_5688')
func_5689_call = mutated_mod.get_global_var('func_5689')
call_9585 = relay.TupleGetItem(func_5688_call(), 4)
call_9586 = relay.TupleGetItem(func_5689_call(), 4)
output = relay.Tuple([call_9585,])
output2 = relay.Tuple([call_9586,])
func_9588 = relay.Function([], output)
mod['func_9588'] = func_9588
mod = relay.transform.InferType()(mod)
mutated_mod['func_9588'] = func_9588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9588_call = mutated_mod.get_global_var('func_9588')
call_9589 = func_9588_call()
output = call_9589
func_9590 = relay.Function([], output)
mutated_mod['func_9590'] = func_9590
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9627 = relay.const([[[5.400228,-6.166980,-7.712934,1.247818,-5.878161,-6.920441],[4.049386,-7.137368,8.912601,-6.870857,1.180997,3.069262],[-9.514682,-8.250109,8.775705,9.959618,-3.863707,-6.988658]],[[-1.185562,4.236825,8.742996,4.420075,-6.601331,-3.090771],[0.567435,0.183054,0.396221,5.329885,8.289124,-2.459524],[6.858221,-8.802492,8.392943,8.550608,-5.960128,-5.539432]]], dtype = "float64")#candidate|9627|(2, 3, 6)|const|float64
var_9628 = relay.var("var_9628", dtype = "float64", shape = (2, 3, 6))#candidate|9628|(2, 3, 6)|var|float64
bop_9629 = relay.divide(const_9627.astype('float64'), relay.reshape(var_9628.astype('float64'), relay.shape_of(const_9627))) # shape=(2, 3, 6)
output = bop_9629
output2 = bop_9629
func_9632 = relay.Function([var_9628,], output)
mod['func_9632'] = func_9632
mod = relay.transform.InferType()(mod)
var_9633 = relay.var("var_9633", dtype = "float64", shape = (2, 3, 6))#candidate|9633|(2, 3, 6)|var|float64
output = func_9632(var_9633)
func_9634 = relay.Function([var_9633], output)
mutated_mod['func_9634'] = func_9634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1468_call = mod.get_global_var('func_1468')
func_1470_call = mutated_mod.get_global_var('func_1470')
call_9652 = relay.TupleGetItem(func_1468_call(), 0)
call_9653 = relay.TupleGetItem(func_1470_call(), 0)
func_1653_call = mod.get_global_var('func_1653')
func_1657_call = mutated_mod.get_global_var('func_1657')
const_9675 = relay.const([7,4,-3,10,4,-8,-4,-5,9,1,10,-1,-6,2,10,-1,-5,4,8,3,6,4,-4,-9,2,-8,-6,3,8,10,-5,2,6,10,-1,-7,-4,9,10,2,-5,-4,1,-7,-5,6,9,-1,-3,-10,-4,3,8,6,7,-1,10,5,3,10,-8,9,4,4,-1,-6,-3,-4,9,10,8,8,5,9,5,7,6,3,-7,1,-5,-4,-4,-1,8,8,-1,4,-2,-5,2,4,-9,2,-6,-6,10,1,-10,-8,4,-6,4,2,-5,-7,-8,-7,-8,2,1,-6,2,6,10,4,-10,8,2,-2,-6,4,-7,-10,1,10,-2,5,-6,9,5,-1,-4,8,8,3,-8,7,-9,2,-8,1,1,-5,-7,4,-8,6,3,-5,4,6,-4,-9,9,-2,4,-9,1,1,-10,1,-9,7,-1,-4,10,-8,4,-9,9,-1,7,9,6,8,-4,-4,-6,-4,3,1,-9,-10,-6,-5,10,-1,6,7,-9,-7,-3,-7,-2,-5,2,-10,5,-1,9,-10,-2,8,-1,1,9,5,1,-3,7,-7,4,-8,-9,3,-7,-9,-4,-8,-3,6,-8,-5,5,3,-6,10,10,-10,-9,9,8,6,6,-6,6,2,-3,5,9,-1,-8,6,1,7,8,7,-3,-7,-8,9,-7,9,9,9,10,2,10,-6,-3,10,-8,-9,-9,-9,9,2,8,-5,5,-7,-3,5,-7,4,-5,-1,-1,-3,7,9,1,-4,-3,9,5,3,5,3,8,-1,-2,-5,5,3,-1,9,-6,-2,-6,-6,-7,10,8,3,1,-8,-8,-5,-10,-6,3,-6,10], dtype = "uint32")#candidate|9675|(315,)|const|uint32
const_9676 = relay.const([8.186048,-1.198211,-6.912322,5.480088,-4.621312,-0.080837,2.633148,3.365163,-6.355817,9.669566,-3.040625,-0.224013], dtype = "float32")#candidate|9676|(12,)|const|float32
const_9677 = relay.const([7,1,-10,-4,-4,2,5,8,-10,9,-8,-6,6,2,-4,-2,-8,-7,-5,-5,-8,-9,-2,9,7,-10,10,3,-8,10,5,5,6,-4,-4,10,-7,-7,7,1,-3,-10,-10,10,9,2,-3,-9,-10,10,1,8,-8,-9,2,-10], dtype = "int32")#candidate|9677|(56,)|const|int32
call_9674 = relay.TupleGetItem(func_1653_call(relay.reshape(const_9675.astype('uint32'), [5, 7, 9]), relay.reshape(const_9676.astype('float32'), [12,]), relay.reshape(const_9677.astype('int32'), [56,]), ), 5)
call_9678 = relay.TupleGetItem(func_1657_call(relay.reshape(const_9675.astype('uint32'), [5, 7, 9]), relay.reshape(const_9676.astype('float32'), [12,]), relay.reshape(const_9677.astype('int32'), [56,]), ), 5)
var_9688 = relay.var("var_9688", dtype = "int32", shape = (56,))#candidate|9688|(56,)|var|int32
bop_9689 = relay.greater_equal(const_9677.astype('bool'), relay.reshape(var_9688.astype('bool'), relay.shape_of(const_9677))) # shape=(56,)
output = relay.Tuple([call_9652,call_9674,const_9675,const_9676,bop_9689,])
output2 = relay.Tuple([call_9653,call_9678,const_9675,const_9676,bop_9689,])
func_9696 = relay.Function([var_9688,], output)
mod['func_9696'] = func_9696
mod = relay.transform.InferType()(mod)
var_9697 = relay.var("var_9697", dtype = "int32", shape = (56,))#candidate|9697|(56,)|var|int32
output = func_9696(var_9697)
func_9698 = relay.Function([var_9697], output)
mutated_mod['func_9698'] = func_9698
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9700 = relay.var("var_9700", dtype = "int8", shape = ())#candidate|9700|()|var|int8
const_9701 = relay.const([[[6,4,7,6,6,-5,-7,2,-2,-2,-6,-1,-6,5,5],[3,-5,1,-9,-4,-8,3,-3,-9,-10,6,-3,1,8,-9],[8,-6,-10,-7,-4,2,-1,-7,2,1,-9,7,6,1,4],[8,-1,4,-1,-8,3,-7,7,-9,4,-2,-7,-4,5,-6],[3,-10,10,6,7,6,-8,-4,-1,-5,-5,5,-5,4,4],[10,3,4,6,-5,-7,-4,-8,-1,3,1,4,9,-6,-1]],[[2,2,5,-9,7,5,8,9,2,-2,-8,5,10,-1,-7],[-1,-8,-4,-6,-6,-10,-8,-4,2,-7,-3,9,6,1,8],[-2,9,-9,-4,8,1,-3,-6,-6,-1,3,7,-1,1,-10],[10,-9,5,1,-6,-9,9,-4,7,3,2,-1,10,-1,3],[-4,-7,-3,-1,-10,-5,4,1,1,7,-7,2,9,1,6],[3,-1,3,1,-10,2,1,1,1,1,6,8,-7,3,-7]],[[4,-1,10,-8,-9,-3,-6,-7,8,9,-8,9,-6,-3,4],[9,1,2,-5,2,9,-7,2,1,1,-1,-6,5,7,-10],[9,1,-1,-9,5,2,-9,-10,10,2,1,10,-4,-1,4],[-5,3,3,1,2,-5,2,3,6,-5,-7,-2,6,-4,10],[-8,-3,3,7,-7,-1,-5,-10,-7,2,-5,-8,5,-6,1],[-9,10,-2,-5,8,1,-8,-4,-5,-5,5,-7,8,9,3]],[[9,-8,3,2,10,3,9,8,-10,-6,-1,2,4,-1,3],[2,9,10,2,1,-4,-5,-8,8,-5,10,5,-3,-3,3],[-2,7,-7,-3,-1,-2,1,-9,10,6,4,-1,-7,10,-3],[-7,2,-4,2,-1,-4,-9,-2,-3,-8,8,-2,-10,5,10],[-7,-3,-2,9,4,9,2,-2,-10,7,-3,-9,5,-5,-3],[10,-5,-8,-10,1,8,-2,1,5,9,1,-6,-9,2,-3]],[[1,5,-4,3,2,8,7,10,-3,1,-6,6,-1,-5,8],[-7,9,7,7,-7,-5,8,-6,9,-5,3,-3,5,3,8],[-8,-4,-7,2,10,-2,6,-8,10,2,-10,-7,4,-6,2],[10,-10,-6,-3,2,2,2,-6,10,8,1,7,-8,10,7],[9,-1,-2,-8,9,-2,-4,9,-3,-5,-1,6,6,10,-9],[9,6,6,9,5,-4,9,9,5,6,-10,8,-8,1,2]],[[7,-7,3,1,7,-2,-10,8,-8,1,5,-3,-9,-9,9],[10,5,6,-1,10,2,-3,-4,4,-4,-7,10,3,-1,2],[6,-5,-9,10,2,2,-3,-8,3,-8,9,-7,-5,10,5],[-9,2,-3,-7,-3,-3,4,-9,3,-6,-1,6,6,8,-1],[-6,3,4,-2,-9,1,9,9,8,2,-3,-9,-10,-4,10],[9,-4,7,8,-1,4,8,5,-3,-9,7,7,5,-4,6]],[[-4,2,-9,6,-10,-6,-8,8,-2,-8,-8,-5,2,4,8],[-10,7,10,4,-5,4,-7,-6,6,9,-8,-9,-2,2,-9],[-6,-3,-4,2,9,-10,-1,-5,-5,-4,5,1,-5,-8,-9],[-9,7,-9,-5,7,-8,-8,8,-5,-4,-7,-1,4,-9,6],[1,-4,-7,9,4,9,5,-3,1,-5,-7,6,1,7,-4],[10,8,4,-9,-1,-9,6,-8,-8,-9,5,-9,5,3,-2]],[[6,-2,7,4,-9,8,-5,-3,-5,3,-7,-9,1,6,7],[1,-9,-10,1,10,-6,7,3,6,4,-10,-8,-7,5,3],[9,-7,-10,-5,-10,-8,-3,8,6,4,3,-1,6,-10,-1],[-5,8,1,1,-9,-10,5,-4,9,-9,2,-8,-3,-2,5],[5,-6,-4,-2,-10,3,-8,3,-5,3,-7,6,-7,2,-9],[5,-9,-8,5,-9,1,-4,2,10,-2,-1,-6,-4,3,4]],[[-5,7,-9,8,-7,10,-8,-6,4,10,-6,2,-8,-9,-4],[-7,4,-2,1,7,-4,-5,-1,-5,-6,10,-5,-6,-1,-8],[-9,-6,10,-8,-6,10,-3,-4,-7,-9,3,-5,-4,-5,-9],[1,-7,3,-3,-8,-5,10,-3,-2,5,-3,3,-1,2,-1],[1,7,9,5,10,-2,4,-2,-8,7,-6,-6,-10,-5,2],[-1,5,1,9,-5,-3,-3,1,-6,-10,4,5,4,-4,-8]],[[-4,-1,1,5,2,-1,7,2,1,-6,-10,8,8,-3,-10],[1,1,3,6,4,-7,2,2,3,1,6,-10,9,6,-4],[-2,-2,-9,-7,-4,2,7,-7,-10,-2,-2,4,-3,-3,2],[5,2,-7,2,-7,-4,-10,-5,-1,9,-7,4,-6,4,-3],[-7,-10,-8,2,-2,8,10,-8,5,1,3,-7,-9,3,10],[-10,6,6,1,-6,6,9,-10,-2,-6,-8,-1,5,6,3]],[[-4,5,-7,6,8,10,-3,-2,6,9,7,1,10,7,-4],[4,-7,7,-9,-1,4,4,10,2,2,-8,-9,-6,-2,7],[-5,-3,-1,8,5,8,3,-7,-10,1,-2,-8,5,-2,-8],[5,1,8,10,3,-7,3,2,3,10,-3,-2,-3,-6,-5],[5,10,8,9,3,-3,4,-10,-9,10,8,2,-6,-4,4],[-9,-9,-5,6,-9,8,1,10,-8,-6,-8,2,4,-9,-10]]], dtype = "int8")#candidate|9701|(11, 6, 15)|const|int8
bop_9702 = relay.less_equal(var_9700.astype('bool'), const_9701.astype('bool')) # shape=(11, 6, 15)
uop_9715 = relay.sinh(bop_9702.astype('float32')) # shape=(11, 6, 15)
output = uop_9715
output2 = uop_9715
func_9719 = relay.Function([var_9700,], output)
mod['func_9719'] = func_9719
mod = relay.transform.InferType()(mod)
mutated_mod['func_9719'] = func_9719
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9720 = relay.var("var_9720", dtype = "int8", shape = ())#candidate|9720|()|var|int8
func_9719_call = mutated_mod.get_global_var('func_9719')
call_9721 = func_9719_call(var_9720)
output = call_9721
func_9722 = relay.Function([var_9720], output)
mutated_mod['func_9722'] = func_9722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7437_call = mod.get_global_var('func_7437')
func_7439_call = mutated_mod.get_global_var('func_7439')
call_9755 = func_7437_call()
call_9756 = func_7437_call()
func_3386_call = mod.get_global_var('func_3386')
func_3388_call = mutated_mod.get_global_var('func_3388')
call_9770 = relay.TupleGetItem(func_3386_call(), 0)
call_9771 = relay.TupleGetItem(func_3388_call(), 0)
output = relay.Tuple([call_9755,call_9770,])
output2 = relay.Tuple([call_9756,call_9771,])
func_9788 = relay.Function([], output)
mod['func_9788'] = func_9788
mod = relay.transform.InferType()(mod)
mutated_mod['func_9788'] = func_9788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9788_call = mutated_mod.get_global_var('func_9788')
call_9789 = func_9788_call()
output = call_9789
func_9790 = relay.Function([], output)
mutated_mod['func_9790'] = func_9790
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9808 = relay.var("var_9808", dtype = "float64", shape = ())#candidate|9808|()|var|float64
var_9809 = relay.var("var_9809", dtype = "float64", shape = (12, 5, 16))#candidate|9809|(12, 5, 16)|var|float64
bop_9810 = relay.not_equal(var_9808.astype('bool'), var_9809.astype('bool')) # shape=(12, 5, 16)
output = relay.Tuple([bop_9810,])
output2 = relay.Tuple([bop_9810,])
func_9817 = relay.Function([var_9808,var_9809,], output)
mod['func_9817'] = func_9817
mod = relay.transform.InferType()(mod)
var_9818 = relay.var("var_9818", dtype = "float64", shape = ())#candidate|9818|()|var|float64
var_9819 = relay.var("var_9819", dtype = "float64", shape = (12, 5, 16))#candidate|9819|(12, 5, 16)|var|float64
output = func_9817(var_9818,var_9819,)
func_9820 = relay.Function([var_9818,var_9819,], output)
mutated_mod['func_9820'] = func_9820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6164_call = mod.get_global_var('func_6164')
func_6165_call = mutated_mod.get_global_var('func_6165')
call_9867 = relay.TupleGetItem(func_6164_call(), 0)
call_9868 = relay.TupleGetItem(func_6165_call(), 0)
output = relay.Tuple([call_9867,])
output2 = relay.Tuple([call_9868,])
func_9869 = relay.Function([], output)
mod['func_9869'] = func_9869
mod = relay.transform.InferType()(mod)
output = func_9869()
func_9870 = relay.Function([], output)
mutated_mod['func_9870'] = func_9870
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9899 = relay.const([[[8.198530,-0.740960,0.811950,-8.456514,0.038066,6.803010,-3.375831,8.193405,1.780824,-2.369030,5.076667,-9.461610,-5.740502,8.383643],[-9.048423,0.787588,6.404272,-6.043280,-4.330828,-5.292027,8.117067,3.124517,4.817408,-5.985254,6.469901,-2.272178,-8.678036,-8.319395],[-8.358327,4.268990,-6.720214,-5.654457,2.812086,9.923160,3.135695,8.764739,8.189958,5.262533,-5.108545,9.621724,-7.887476,-4.565498],[-4.869520,8.856846,-3.104766,2.388318,-3.381261,-2.161238,-3.295898,9.594752,-6.384896,5.316309,0.298690,-2.003308,-3.246887,0.539405],[4.883025,4.196575,-4.496813,-8.185234,-2.565685,-1.286500,4.647680,-9.008604,-4.765906,-0.782665,-2.959815,-3.316312,-7.538461,2.540741],[-2.585021,0.548528,-5.856929,-0.432776,7.144286,-0.942305,-0.070833,-4.204336,6.609334,-5.870182,-4.172178,-3.563580,-6.813326,-8.965830],[-8.053628,5.049574,-3.247484,-6.008970,-8.198566,-5.908230,-1.991624,7.330866,0.447372,-3.637856,-7.709406,-2.545090,4.492109,3.855173],[4.863877,-5.259317,-7.079930,-1.949153,-0.663350,2.254181,8.305139,0.667115,-1.611745,2.920575,-4.442855,3.033967,-5.159902,-9.917795],[-8.690496,3.113547,9.533701,5.467720,1.119380,4.178657,8.062924,-0.420750,-6.858872,-9.935583,-0.236036,-0.599149,6.990423,1.523340]],[[3.841258,-6.942922,-3.491448,4.531799,8.910221,3.962215,-2.807493,8.717041,4.636438,7.795831,8.501458,8.417620,7.043286,-4.871233],[3.965726,-2.194862,7.571802,-3.559859,-9.239422,-3.518274,8.631543,-0.784815,-6.529342,6.439874,-5.028451,1.854217,-6.567351,3.114978],[-9.225699,-1.689417,-4.548594,-1.635672,1.173734,9.852191,-8.626034,-7.925776,6.019315,6.072304,-0.284203,5.563499,8.527082,-2.021500],[4.922638,2.316039,1.836316,8.917089,-5.167248,-0.140202,2.019989,7.901775,4.892797,9.439126,8.512748,-5.734546,0.435513,-2.103730],[-1.764412,-4.074488,-2.303380,0.601100,7.092695,3.224935,-4.636309,-8.551387,8.774396,0.928099,6.579976,1.675865,4.281966,-4.749940],[-8.351027,-4.443829,6.334742,-7.278243,-5.513972,1.047754,3.465208,-1.802553,-0.099487,2.000200,-6.632676,-5.306822,4.181998,-5.114399],[4.376372,6.758969,5.653403,-8.449382,-8.866800,6.023393,-5.068296,-2.846652,6.496216,9.914897,7.589773,-6.316105,5.377182,5.112755],[-6.261848,-5.862266,-4.419331,0.298187,1.155479,-4.011574,6.766686,-5.476342,0.547758,2.292920,7.508877,-4.139006,9.262566,9.492453],[-6.850241,8.834533,-4.656035,-5.617697,3.061137,9.417458,-4.393795,-6.746853,3.962098,5.832094,5.633065,4.094896,-0.622763,-5.573074]],[[-3.993304,-5.699396,-1.539609,-7.527125,5.113227,-8.042730,-3.987034,7.582216,5.175390,-8.588299,3.162567,7.610348,-0.862296,0.239931],[4.876072,-0.908222,1.922139,-0.835652,-5.498429,9.480602,2.820054,-6.530123,8.654314,-9.393455,0.217194,2.217334,4.881415,-0.779894],[3.819211,-7.972336,7.266246,8.861938,9.877329,-1.379739,-9.179137,-6.242956,4.703276,2.461883,-4.812636,-2.321981,3.876022,-1.854435],[-4.471769,-7.107217,5.430730,-3.006523,-7.371921,1.019875,4.720623,6.081235,3.422406,-4.433923,6.803789,0.873136,4.199475,9.634018],[0.590114,6.820476,-6.106016,-4.749612,-7.164659,-1.447763,-1.423621,1.591596,-3.423459,8.170588,-5.816928,-5.266478,0.336919,1.911437],[2.699853,3.925905,7.978850,3.556038,2.520729,8.871272,-7.742924,-6.155950,5.481190,2.546577,-5.628466,-2.713845,-8.077666,-5.535549],[-0.440421,-5.581482,4.328952,3.317230,2.540022,-3.256073,-2.117480,-8.936284,-4.609647,4.475499,-2.657526,4.398864,9.542383,6.220987],[-0.115311,8.334936,-6.103737,4.857486,-3.930793,-7.123721,0.374494,-8.092850,-6.556479,-6.164092,5.724094,-0.418023,-9.080541,-1.946620],[0.351117,5.647533,-4.043133,7.073342,7.256531,-3.513356,7.239873,2.819612,2.794005,-9.113765,-6.827944,-6.528280,-0.266878,-3.478062]],[[-0.898686,-8.634388,-2.418841,-7.392990,-7.380109,6.639380,-3.862179,5.265207,-9.867374,-6.127520,-1.517431,3.682134,2.260245,-7.053345],[5.318775,1.522232,-1.641362,7.551817,6.408933,3.979441,9.468409,4.716674,-0.375990,8.255616,4.410644,-7.714566,-3.682147,4.923887],[-4.774301,4.780192,-8.809031,8.627879,-9.808006,0.458497,-1.297430,-8.982022,-6.965449,5.940971,-1.471119,3.975403,-6.358819,-7.499087],[-1.224214,2.596972,7.948730,-9.932402,8.105214,-6.487599,-3.992258,8.445211,-4.961444,9.055865,-4.569288,3.960260,1.964930,-1.396673],[6.475595,5.136540,-0.744277,-8.744541,5.629089,0.442808,-6.815695,4.716982,-3.224752,-6.223378,-3.652489,1.934764,-0.084050,6.331617],[3.967232,-2.544600,-1.933768,-7.336943,-8.101639,3.040948,1.929511,-1.842878,-5.493544,7.857253,-1.477357,-4.220767,4.066003,8.148502],[-8.591173,0.492073,2.740639,-9.782416,6.943938,-7.509418,1.630075,-8.453210,9.538711,2.421596,-0.729256,-7.836476,-3.386685,2.245458],[-4.541333,8.889026,1.813027,-5.633520,-6.206443,5.642728,-1.466850,2.743536,9.760964,-2.517254,-4.350055,-9.157961,-7.008756,-5.736787],[4.577028,-3.797809,-8.115867,9.268314,1.477193,-9.784520,-0.676856,9.816520,-1.721414,7.279584,-1.947456,-5.337483,3.100965,8.071697]],[[6.908833,-5.230070,4.388944,-0.522822,-4.644167,-1.952042,9.233107,-8.184039,-1.686539,-7.625606,-0.865180,-9.216642,-5.110562,-4.102131],[7.234641,0.649577,4.960498,-9.590923,1.273267,-8.659081,-8.119695,6.679820,-9.934237,9.764715,0.660772,6.590579,5.743698,2.095470],[-1.069007,0.202865,8.157631,-1.283596,-7.939861,-3.589130,2.234157,-6.715420,5.784650,6.622724,1.530317,-9.734416,6.938748,-1.057577],[2.667016,-4.817480,8.123213,4.989433,-1.341908,0.281939,-2.066703,-3.795426,3.426023,9.866259,-0.602286,-0.975082,-1.212459,6.400550],[-2.733839,-3.431782,9.057247,4.564035,9.587518,4.237293,-6.122808,-7.953643,-1.612859,-0.173074,4.655478,-1.077890,-2.025745,9.605544],[1.192126,-6.359531,9.191143,9.764035,8.153656,1.033678,-2.023896,9.743051,-5.018708,9.432452,-6.419125,-3.230793,-6.459002,-1.750881],[3.842471,2.007383,-8.365428,-4.165087,-1.238180,-9.600077,-2.301125,-4.109100,-1.296783,1.256157,-2.365416,-5.580105,-4.739211,-9.357075],[0.661745,8.131164,3.777121,-2.386138,7.241875,5.408501,-0.372888,9.010130,7.585727,1.555829,3.384525,-4.742648,-7.227180,7.068990],[0.993342,6.210557,-5.932026,3.315561,7.837239,1.970070,-6.421884,-7.370663,-4.926374,4.646392,-8.175768,3.253188,9.658156,3.624424]],[[-8.454671,-5.524653,-8.517003,2.013400,8.449527,-5.794211,-7.576544,9.938769,-0.040117,5.004882,7.167964,0.181607,-3.715867,-5.086085],[-5.873480,2.990286,-0.260359,6.250099,3.438352,0.702746,7.621282,6.633235,4.077849,8.893700,-7.313999,-7.731177,4.301341,2.215251],[-9.971000,-6.693337,7.997656,-6.686355,4.610604,7.372193,-7.231009,2.174814,-5.393076,5.919775,7.903263,-5.758011,2.743131,-9.423775],[-8.963464,-7.934291,2.791992,7.278155,-4.641840,-3.856877,4.355863,-7.567878,-3.822452,-0.155079,-9.779149,-5.715891,-3.341756,-4.896427],[9.829832,-0.816988,-5.282724,-3.314120,9.524460,9.050401,1.677636,-8.581424,3.027717,-3.060986,-1.729221,-8.943759,-7.776699,1.667678],[8.231338,8.094783,-6.697892,-8.964225,-7.202375,-5.745908,6.423502,-6.680667,2.584586,5.699371,3.936434,-7.506380,-0.969278,1.196382],[2.031229,7.562307,-0.449034,0.853259,3.718533,7.423743,-7.701023,1.869303,6.341382,1.652850,-1.821426,3.240824,-3.297606,-8.370526],[0.496334,-2.948904,-7.463005,3.221744,-5.637128,5.016159,1.714094,4.781240,-1.745914,5.612171,-4.720926,-7.699458,9.788340,5.098027],[2.228325,1.565054,1.696150,8.489348,7.820458,-0.432402,4.403098,2.487823,-2.401640,-7.336598,-7.477331,3.872822,-6.274042,7.188848]],[[6.668808,-7.766790,-7.566479,5.069075,5.158066,5.712120,-8.286238,-1.957644,9.093900,-1.147001,-8.029986,-9.832704,-2.695893,-9.927968],[0.931072,-5.866236,-3.835661,2.108325,-6.969933,-2.362108,7.122903,4.810810,0.401476,4.726939,9.674192,-6.589754,6.046651,-7.518334],[-7.418398,-7.553810,6.361059,7.173053,6.087312,-8.298732,8.460050,4.753390,2.382196,-9.203949,-4.387567,6.633784,7.604677,-2.736370],[2.455331,-4.181052,1.649538,6.081903,-2.227273,-7.238838,-4.790793,9.269495,8.804893,-8.274356,7.064694,5.102164,1.969484,-3.515682],[-1.373925,1.954030,0.434799,-3.933039,-1.692913,0.825271,-1.371270,0.204076,4.370490,-5.614377,7.116822,0.874179,-8.750667,7.419593],[5.150190,-6.335219,-0.715877,0.272407,-2.245424,-5.953202,-2.619734,4.508620,2.176820,5.107445,5.589248,1.209568,-7.854722,-4.965144],[7.203943,-3.400972,5.609267,-3.057815,-1.284024,5.604845,3.857245,-0.903745,-1.280482,-2.791498,-5.308747,-9.645332,-9.008111,-7.023610],[-7.777320,2.239961,-7.118101,-6.002922,-7.690468,1.993599,3.620979,6.719821,-1.268185,-7.041745,2.853599,-1.575150,-8.864427,-7.985307],[-9.178423,0.489749,7.308295,-7.615142,8.264727,7.919364,-5.554589,-7.471684,3.359734,-7.474474,4.560375,-2.337349,-7.457096,-0.398769]],[[3.622250,4.009711,-4.902141,-0.462825,3.317955,3.635873,-1.839350,-4.317314,-4.163307,-8.046319,4.147676,0.176668,8.176989,4.538097],[1.385710,-5.828425,-5.684322,-2.821094,-3.681033,-4.123357,-4.763177,-4.056541,-1.369039,3.903475,-8.709488,5.341481,-9.721312,-9.462824],[-8.636107,0.494186,-3.490605,9.665357,3.981524,0.607259,-7.283923,7.439991,7.783773,0.275562,4.959678,-1.199132,-8.197243,4.685318],[9.827933,-9.395435,5.106863,9.182958,2.667607,7.939217,-1.290935,6.809042,-5.531062,3.926591,-6.912417,-0.619481,5.632900,3.045671],[-3.523471,0.765587,3.903037,5.538446,5.393350,-2.744255,6.638069,-3.945626,-8.422740,7.856954,-6.042209,-5.905287,1.843311,-7.832942],[-9.434986,7.638719,-9.950409,-1.907598,-7.442482,9.618526,-3.275936,6.296783,5.787936,2.738201,4.370265,-2.826869,-2.621118,-2.475047],[6.198262,-0.005797,5.656663,-2.492117,-5.793281,1.505986,1.098469,8.331670,-6.966185,5.390234,-1.790966,6.243841,2.212430,8.592416],[-6.266163,-2.229771,9.224172,4.137262,-6.842190,-9.611865,-0.066575,4.590795,-2.610017,2.063207,0.281260,-2.894096,-8.583289,8.562687],[-0.787501,1.866492,9.353726,-7.574815,-3.852201,3.974412,-9.063351,-9.783360,8.821866,-1.883030,-6.277215,-5.243846,-2.616929,7.654579]],[[-5.213676,7.460304,9.734967,0.139798,-5.272093,7.486562,-3.201857,4.559959,8.651914,9.436268,2.554228,-5.979714,-7.662893,-8.814586],[-7.063078,1.737689,-4.003180,7.992503,6.866694,-4.472432,-6.989815,-0.428039,-6.342769,6.832016,8.345910,-4.283291,-0.018991,-4.511336],[3.146785,-0.238542,-8.139804,-1.553053,-9.411225,9.994663,3.761045,6.276009,4.852366,-1.246699,7.489121,6.585709,-4.000918,3.569189],[5.313237,2.289225,-7.059870,-1.108480,2.353024,-0.328360,-9.159019,4.524894,2.698749,5.777367,5.214238,2.450073,-8.748721,9.461225],[-9.518036,3.388457,8.101015,4.671023,-2.061013,-6.071000,-8.407208,4.922720,-2.308710,-5.340520,6.860380,2.523404,0.248889,8.988862],[5.391621,7.134074,-8.518997,9.257598,3.604582,4.991923,-4.772488,-2.047497,-5.778394,2.101300,-7.969200,7.301146,-1.825621,-8.464132],[2.974561,1.047864,6.962768,-3.802364,2.502765,6.172051,-0.846586,7.258926,-0.839774,-8.891295,0.531428,-3.751062,0.304444,-8.334995],[-1.086767,-1.975191,-7.439148,-5.290464,-4.838797,7.863254,2.697702,-0.378410,-6.904887,-8.627326,7.654473,7.972367,4.084031,6.732555],[4.912977,-3.607954,-9.776384,6.317772,-6.915770,-6.749067,4.464437,-9.641163,-1.945304,-7.074910,-9.051290,-2.893577,5.823917,7.542038]],[[9.971007,-6.447798,-7.863035,-9.397966,5.791217,3.626128,5.476132,-0.703344,-6.905400,3.517542,8.451810,5.479476,7.057938,-5.889902],[4.059868,2.486137,-4.247907,-3.381552,-2.360466,0.137067,-2.721414,9.063982,8.972651,-9.208023,-1.369083,-7.497714,-1.447865,-9.325470],[9.147950,-5.485188,-0.812198,5.775683,1.138085,2.494460,-2.473045,7.654286,3.031880,4.162962,-5.526820,-5.314670,3.425916,9.857437],[-2.234962,7.885838,-4.591664,7.735401,4.420580,7.720650,-7.389921,-9.278465,0.616492,5.230025,-4.389757,5.227423,6.404315,-3.047513],[0.758476,-0.357566,9.357341,9.058437,0.688141,-8.262780,-4.910683,-3.556453,-4.352241,7.257963,-0.732554,-9.170603,1.906475,-0.189196],[-9.142844,-7.317218,-5.603947,2.158964,-3.152737,2.107335,2.005412,1.521144,3.551858,-3.305067,-9.671821,8.260013,0.530101,-2.334503],[-9.715753,3.840834,7.637678,-4.589141,-0.111947,4.504881,-9.207253,-9.405370,-5.684449,8.642231,6.092457,0.919677,-9.116991,9.851964],[-3.520940,-9.990381,-9.585685,1.671666,0.714347,9.930236,-6.383817,6.576064,4.195004,-0.600147,8.970987,1.742435,-8.342210,-0.136904],[1.801280,-8.976706,8.170420,-7.021684,-5.912219,7.601492,1.412822,1.427001,8.111889,9.491552,-3.837978,-8.153874,3.204636,6.350437]],[[-9.388595,-8.774863,0.084522,-7.093443,-6.741471,-3.888846,-1.605938,-4.941990,-8.347786,0.539158,-0.142299,-3.575790,9.264028,-0.964233],[-5.539702,-5.617147,-7.529845,-3.643322,1.003529,-4.735818,-4.269489,-4.885004,2.778979,-8.551783,-0.995908,3.286237,-8.677817,8.772002],[5.680141,1.901002,6.197313,-2.715603,-7.544244,5.014032,0.516672,1.225209,-5.427198,1.913960,3.926149,1.497854,4.822360,-7.739882],[-6.026147,8.532549,-0.481759,5.355472,-5.621167,9.118198,6.205362,-3.546733,-0.531621,-4.000828,8.090361,-8.024884,9.090546,-8.254689],[9.772688,6.117451,7.595175,4.420174,7.674537,0.853557,-7.610724,-9.521595,-5.845924,2.395760,8.537699,5.278932,7.402260,0.953215],[-1.562786,9.682494,-0.714654,0.176535,-5.062542,4.311924,-8.145421,8.644569,3.293149,-5.267902,6.993672,1.664274,6.669743,8.399503],[-2.036782,7.890171,0.116376,-9.604880,0.324070,0.556249,-3.613028,5.261829,7.817779,-4.733467,3.604860,-0.166770,-0.036927,4.418582],[5.535675,-2.002450,8.611853,-0.671222,-4.160112,-1.510670,-3.372424,5.108647,5.066807,7.010242,-8.175037,7.528722,-1.384543,-6.950993],[6.012059,-5.988936,-8.690737,8.548323,3.489581,-3.125883,-1.829760,4.730683,-8.408596,-9.993435,-0.591512,4.270275,7.402754,-4.581698]],[[-5.655681,-3.166768,-2.553969,-6.660276,9.584791,-4.643826,0.999237,-3.055607,6.374569,6.712314,9.889594,2.440840,9.707366,-3.094962],[-1.572467,5.152626,8.922399,-7.431276,-8.097216,-5.828731,-5.080315,-8.161595,-5.574405,-3.922798,8.045864,4.367787,4.648008,-9.103968],[1.222800,0.355925,4.927385,3.168314,-9.394168,-3.197589,-5.616829,-1.274291,1.494340,2.283228,4.217164,1.537482,5.546113,0.446983],[-9.346787,3.330524,-0.988608,7.263614,2.188988,-2.319736,-1.030986,7.987638,-3.088101,-2.874334,-4.141312,5.805599,8.176827,-1.445794],[8.755758,9.924010,1.996097,-0.691445,0.621197,7.917169,-2.945388,-8.152069,-8.099938,3.475729,7.894918,-6.503109,9.006016,4.982197],[3.047023,2.656173,-6.602280,-5.240359,-5.534775,0.199556,-8.271633,-4.360519,5.656706,9.606026,-7.931312,-5.520859,-0.750760,-9.952910],[-8.235763,-5.856257,1.946181,-6.650420,-5.160998,-8.558080,9.341017,-9.318422,-3.772152,-0.113587,7.454556,-8.425881,4.262644,2.356649],[6.816660,3.276847,-3.060581,3.993163,-5.963821,4.196328,-7.012493,1.155727,1.185454,1.638053,-7.597868,8.378970,-8.916015,-4.420820],[-2.860246,0.625702,1.552469,2.798225,5.289931,8.784116,3.813028,-2.215327,-1.814908,8.209050,-4.912040,-8.721063,2.069448,-6.037188]]], dtype = "float64")#candidate|9899|(12, 9, 14)|const|float64
uop_9900 = relay.sinh(const_9899.astype('float64')) # shape=(12, 9, 14)
output = uop_9900
output2 = uop_9900
func_9905 = relay.Function([], output)
mod['func_9905'] = func_9905
mod = relay.transform.InferType()(mod)
mutated_mod['func_9905'] = func_9905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9905_call = mutated_mod.get_global_var('func_9905')
call_9906 = func_9905_call()
output = call_9906
func_9907 = relay.Function([], output)
mutated_mod['func_9907'] = func_9907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7885_call = mod.get_global_var('func_7885')
func_7887_call = mutated_mod.get_global_var('func_7887')
call_9914 = relay.TupleGetItem(func_7885_call(), 1)
call_9915 = relay.TupleGetItem(func_7887_call(), 1)
output = call_9914
output2 = call_9915
func_9918 = relay.Function([], output)
mod['func_9918'] = func_9918
mod = relay.transform.InferType()(mod)
mutated_mod['func_9918'] = func_9918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9918_call = mutated_mod.get_global_var('func_9918')
call_9919 = func_9918_call()
output = call_9919
func_9920 = relay.Function([], output)
mutated_mod['func_9920'] = func_9920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8817_call = mod.get_global_var('func_8817')
func_8819_call = mutated_mod.get_global_var('func_8819')
call_9927 = relay.TupleGetItem(func_8817_call(), 1)
call_9928 = relay.TupleGetItem(func_8819_call(), 1)
uop_9935 = relay.cos(call_9927.astype('float32')) # shape=(49, 10)
uop_9937 = relay.cos(call_9928.astype('float32')) # shape=(49, 10)
var_9952 = relay.var("var_9952", dtype = "float32", shape = (49, 10))#candidate|9952|(49, 10)|var|float32
bop_9953 = relay.mod(call_9927.astype('float32'), relay.reshape(var_9952.astype('float32'), relay.shape_of(call_9927))) # shape=(49, 10)
bop_9956 = relay.mod(call_9928.astype('float32'), relay.reshape(var_9952.astype('float32'), relay.shape_of(call_9928))) # shape=(49, 10)
output = relay.Tuple([uop_9935,bop_9953,])
output2 = relay.Tuple([uop_9937,bop_9956,])
func_9957 = relay.Function([var_9952,], output)
mod['func_9957'] = func_9957
mod = relay.transform.InferType()(mod)
mutated_mod['func_9957'] = func_9957
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9958 = relay.var("var_9958", dtype = "float32", shape = (49, 10))#candidate|9958|(49, 10)|var|float32
func_9957_call = mutated_mod.get_global_var('func_9957')
call_9959 = func_9957_call(var_9958)
output = call_9959
func_9960 = relay.Function([var_9958], output)
mutated_mod['func_9960'] = func_9960
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10034 = relay.var("var_10034", dtype = "int16", shape = (3, 10, 7))#candidate|10034|(3, 10, 7)|var|int16
var_10035 = relay.var("var_10035", dtype = "int16", shape = (3, 10, 7))#candidate|10035|(3, 10, 7)|var|int16
bop_10036 = relay.subtract(var_10034.astype('int16'), relay.reshape(var_10035.astype('int16'), relay.shape_of(var_10034))) # shape=(3, 10, 7)
func_1308_call = mod.get_global_var('func_1308')
func_1310_call = mutated_mod.get_global_var('func_1310')
call_10039 = func_1308_call()
call_10040 = func_1308_call()
func_7962_call = mod.get_global_var('func_7962')
func_7963_call = mutated_mod.get_global_var('func_7963')
call_10041 = relay.TupleGetItem(func_7962_call(), 4)
call_10042 = relay.TupleGetItem(func_7963_call(), 4)
func_7589_call = mod.get_global_var('func_7589')
func_7590_call = mutated_mod.get_global_var('func_7590')
call_10043 = func_7589_call()
call_10044 = func_7589_call()
bop_10063 = relay.not_equal(call_10039.astype('bool'), relay.reshape(call_10041.astype('bool'), relay.shape_of(call_10039))) # shape=(10, 7, 2)
bop_10066 = relay.not_equal(call_10040.astype('bool'), relay.reshape(call_10042.astype('bool'), relay.shape_of(call_10040))) # shape=(10, 7, 2)
output = relay.Tuple([bop_10036,call_10043,bop_10063,])
output2 = relay.Tuple([bop_10036,call_10044,bop_10066,])
func_10085 = relay.Function([var_10034,var_10035,], output)
mod['func_10085'] = func_10085
mod = relay.transform.InferType()(mod)
mutated_mod['func_10085'] = func_10085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10085_call = mutated_mod.get_global_var('func_10085')
var_10087 = relay.var("var_10087", dtype = "int16", shape = (3, 10, 7))#candidate|10087|(3, 10, 7)|var|int16
var_10088 = relay.var("var_10088", dtype = "int16", shape = (3, 10, 7))#candidate|10088|(3, 10, 7)|var|int16
call_10086 = func_10085_call(var_10087,var_10088,)
output = call_10086
func_10089 = relay.Function([var_10087,var_10088,], output)
mutated_mod['func_10089'] = func_10089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6513_call = mod.get_global_var('func_6513')
func_6514_call = mutated_mod.get_global_var('func_6514')
call_10104 = relay.TupleGetItem(func_6513_call(), 0)
call_10105 = relay.TupleGetItem(func_6514_call(), 0)
func_8854_call = mod.get_global_var('func_8854')
func_8857_call = mutated_mod.get_global_var('func_8857')
const_10109 = relay.const([[3.830113,0.442617,0.941954,3.030331,-9.956745,8.993291,7.992863,6.729869,4.048317,5.934794,7.014413,-2.695756,0.521606,1.065016,-2.145483,4.723716,6.837335,-0.335098,7.419164,-8.092460,-3.522009,7.573277,-2.389570,-3.395879,-7.166180,-3.913326,-7.244019,0.404854,-0.782978,1.636866,4.741026,-7.566678,6.636732,3.234555,-6.110076,3.771560,0.227241,-5.471788,4.645108,0.791289,-3.762672,9.706985,7.627453,-2.422845,-2.653159,-3.885393,8.101064,-0.545039,4.844106,1.907686,4.856206,-5.460961,6.469001,5.359061,-1.737661,-0.544065,-4.724436,3.333630,-7.174241,8.906014,2.941640,-4.651140,-4.187483,-8.096888,-9.704460,3.260895,-5.932893,2.148685,-0.839480,-7.164927,0.920577,-1.191342,6.619934,9.899039,2.791166,-2.883391,9.663312,1.945117,4.074480,9.834173,7.587772,6.603656,9.803362,4.448749,5.635334,-9.004129,-8.467433,-9.139857,-0.627768,-4.852484,-6.443439,-0.996733,8.012722,4.793591,2.572706,1.588866,3.701111,-5.093515,6.523513,2.155974,-4.949602,6.655354,-6.349830,-0.445736,-8.219811,-8.672684,7.254421,-4.403609,9.417261,7.294717,-8.229093,4.936544,2.568473,-6.918506,-5.747402,-9.013804,0.531131,5.968128,0.041734,-7.059306,-8.349356,0.217851,-4.506754,2.844255,3.302947,-0.752208],[0.797580,-5.090920,-4.616737,8.533697,-8.254791,2.335914,4.648770,1.208605,-1.635712,-2.114003,-2.498463,-2.940845,6.065702,-8.518520,-4.801433,3.950891,6.399756,-0.513758,-0.659532,-1.569143,9.774357,5.597257,-4.364177,-5.724436,-2.339186,-7.334517,-6.924748,9.125307,-0.899933,-6.810239,1.568869,-9.042202,4.545297,-1.500122,-6.500619,-8.180759,-0.858243,-2.002964,-6.044290,0.658809,-1.788023,-1.536298,-7.550038,-3.169400,8.884742,6.749816,-0.043693,8.215379,-4.622452,-3.482944,-8.906834,4.484967,-8.667610,-3.537633,-3.336680,7.607724,0.255412,2.060297,-1.260101,-7.464010,-5.868811,-3.366699,6.400722,4.481862,7.318279,-3.632632,-1.685597,-6.978810,5.472285,-2.943695,-4.206284,-0.731430,7.736398,2.846475,-7.289831,4.396341,6.422113,1.028637,-0.435484,-0.454592,-0.246373,2.750994,-1.553285,5.185464,-1.961918,5.013860,-0.047798,-6.579910,7.085869,4.952323,8.792705,9.663517,-8.969582,0.957788,7.476489,-5.649680,-9.445554,-4.842284,7.194069,9.400357,2.360731,-5.713271,-6.086412,2.054206,-4.698438,2.492013,-7.652889,-3.343775,-2.672008,5.332941,3.675538,9.950311,2.362477,9.543138,-8.490880,0.160467,9.618907,7.108320,-0.350006,-1.860839,2.494370,9.069791,-9.066467,-3.179816,7.452368,-6.411683],[8.207239,8.264079,7.476371,2.165169,2.237235,-2.832749,-7.085154,-6.276322,-5.609067,9.854571,8.399462,6.678522,-8.063143,-6.420160,0.615097,-5.983319,-8.234647,-3.163016,-6.969483,0.339178,-6.704886,9.037288,5.899963,8.265294,-4.670788,4.186935,9.816964,5.278188,-4.910423,-0.145778,-2.525874,-5.474778,-7.149679,-9.750616,-5.076356,-0.770284,3.796361,9.766576,7.730480,4.002854,6.515231,7.878605,2.705296,-9.792620,-6.647201,-3.264397,-4.651240,-1.206632,4.183440,1.939720,-1.228272,-1.334159,5.812869,2.349636,-6.393071,-9.305762,8.759350,7.079400,-5.748971,4.816368,-2.518162,1.169033,-0.571226,9.655917,5.257552,-0.935639,-4.057160,6.010771,-9.723457,-9.629889,8.971492,8.434229,1.130402,-0.346975,-2.248369,-1.148701,6.704363,2.454425,1.423702,4.177838,-3.209037,6.395257,-8.416454,-6.868317,6.530592,1.584449,-2.832607,8.045238,5.142009,6.117001,8.208431,-7.747603,-0.329708,9.145631,-4.251013,-2.605015,-1.188883,0.734523,-5.096244,2.775521,8.913775,5.758747,6.882395,8.996562,-4.198256,1.081146,-0.216025,-3.119631,7.683113,9.704617,-0.560428,-6.178019,1.758689,9.491205,-5.802916,5.786244,1.336449,6.457751,2.053839,-5.403249,4.797656,-7.997474,8.623458,-7.408717,-8.690613,9.463353],[9.928951,6.623370,9.608791,6.334530,2.695751,6.856891,4.771789,-0.549156,0.575979,-2.307243,-4.874485,2.060112,2.129350,-5.005103,5.814947,-8.748884,-0.807525,7.740783,-9.304766,4.215114,6.500530,-4.271862,0.805933,9.796116,3.748871,3.716883,-2.989590,-1.249007,9.296301,8.606769,-1.695232,0.152837,3.150851,-0.024298,7.950087,-7.117481,1.655390,6.567962,6.201995,5.634500,-2.676392,-6.844369,6.074340,-1.186810,1.590096,3.218626,8.330132,-5.429297,6.979433,-7.504441,-1.354838,0.292146,-3.224907,-4.309628,-3.833762,-2.182809,1.514048,0.472709,7.297186,3.740652,-9.870123,-7.678991,9.614075,-2.737693,-7.650441,-9.074511,2.298957,-3.349167,-4.745746,9.030767,-4.228902,-0.345991,-7.236347,0.591750,9.769747,6.877655,4.437189,-6.509496,-4.077029,-5.773675,1.004670,-4.811497,-2.351045,-9.620181,9.423328,5.388633,-8.819056,6.456278,-7.452557,-0.340300,4.289452,2.870829,-1.103047,-8.636003,-6.862810,2.899190,1.861022,6.101325,-6.327170,-5.311487,9.242443,3.976151,0.831753,5.020435,9.596326,-8.080183,3.359730,-4.480871,6.046038,-9.577262,8.969034,2.744865,9.556710,-0.214706,5.047011,-0.570116,1.462650,-4.592066,-9.304630,-1.336396,1.468700,9.288792,-5.297535,-0.622993,-0.401405,3.708469],[-3.076540,-6.627513,4.567361,1.417391,7.630073,-8.013841,-8.287880,-0.311748,-7.840527,-5.864570,6.599644,-6.665862,3.364385,1.225264,4.087428,0.643815,9.965815,-8.649760,1.304344,0.979797,7.152665,7.697712,-8.965062,-6.605746,-0.382898,1.543660,-1.647948,0.157830,-5.875905,0.622090,7.895885,-8.402441,-5.111690,-6.531829,-8.527720,3.226756,8.413392,4.321509,-1.452438,-9.111349,4.831292,-9.225644,3.656706,7.948743,-0.757148,9.764297,-5.515811,-4.649965,-3.474485,-9.520344,2.210598,-0.833614,-6.708492,-7.536470,-7.928996,6.449450,-3.914057,9.950092,3.655690,-4.424487,-8.226883,4.879958,4.985680,3.588646,-4.010364,-5.093789,5.258842,-6.080265,2.609375,-8.428576,6.139755,7.036092,6.934803,0.617961,4.017277,-0.157296,-6.315925,-4.401491,-8.851580,2.675039,8.112982,-8.691883,1.131441,-0.675854,9.445283,-3.765622,-7.048031,3.636354,-6.891342,-5.074315,-9.567984,6.750367,3.395019,-2.532595,-3.001565,-2.479315,1.603257,-6.683363,-5.296299,2.828671,-7.118642,-7.899720,3.943915,-1.404857,3.218517,-8.044394,-1.679523,-2.569939,7.341123,9.198039,-9.973823,-3.565341,-3.287958,-3.302040,3.014351,-8.129155,3.108457,7.585092,-3.751493,5.460303,-9.986386,7.935196,8.117555,-9.707459,-0.518242,-3.798076],[-7.842841,0.856350,-5.758959,2.687573,1.197628,2.340206,-1.552202,-7.115873,-4.143573,-4.548478,7.951933,2.138593,7.621317,8.336625,6.677689,7.583378,-7.300370,-0.884274,-9.933599,3.621602,-1.632485,7.965368,1.532425,5.197977,8.903441,-0.043800,-3.893563,2.545612,-8.211138,7.596047,8.796084,7.463462,7.466167,-6.191476,5.163609,-0.321174,-3.390342,-5.417200,0.764308,2.579115,-2.044178,3.751663,-0.103037,-2.431601,0.238238,-9.864063,-8.087165,2.518547,-4.949387,-3.695726,7.642704,8.284941,-7.430338,5.991676,7.200900,-1.390025,-8.012648,-5.094078,-3.599650,6.835184,0.035071,-1.765009,4.524156,8.115415,2.972050,5.860998,-5.275991,-0.534829,7.673273,-4.105308,5.219213,-9.418942,-6.521533,-7.621584,9.228668,3.855958,5.671843,1.868748,5.896628,-2.256415,-7.968170,3.757098,-1.057280,7.774020,3.465557,9.809752,-5.904225,-3.134284,-4.483210,1.191320,6.180927,-2.531894,4.438030,8.495505,3.994707,5.777326,-2.736182,-4.784677,3.383364,-4.060053,-5.617362,0.423991,1.506155,9.053429,-7.711079,8.986547,4.361780,-6.173194,2.721455,5.517024,-1.630941,-3.953621,8.441410,1.306146,-1.417831,7.174878,9.601226,6.360522,7.269348,1.971052,-4.175220,2.045496,-3.172813,-2.985173,3.303137,-5.429768],[-4.417992,-2.066259,-9.578981,-8.006043,6.665575,2.625469,-4.233369,3.725692,5.953156,8.895163,-6.594710,-5.077657,9.754037,-5.905502,-7.775399,-2.497338,-0.504657,1.471576,-6.730063,1.764924,5.206152,4.327468,-5.808367,6.743252,8.611513,5.936163,8.727829,-6.155352,-0.411919,-2.120481,-9.106571,5.961471,8.804151,3.384465,1.175008,-6.544312,3.078794,-8.109956,-9.371021,7.412096,6.634483,3.564610,-3.249960,6.841265,4.599737,-2.385519,-9.514178,-7.146219,-0.351154,1.699720,-9.918802,-3.606091,7.230843,1.312263,8.910779,4.378564,6.158647,2.099959,2.808605,-9.822059,-8.586854,-0.193660,9.190547,2.305818,-6.164624,6.567073,-0.011110,-2.867328,-7.548800,0.370432,-3.139021,-3.948881,-4.164991,-9.903230,-8.188288,-5.134637,3.709296,6.150734,9.673351,-3.196570,-7.687219,-3.227200,4.832411,-0.434633,8.565099,5.437049,6.437864,6.836657,-6.185797,9.840921,6.701352,0.977963,-0.022218,5.674844,9.676208,2.642063,4.939846,-3.282037,-8.889830,-0.185733,8.705390,6.231236,-2.559764,-9.230678,-4.315543,5.031852,6.348264,-5.787014,-4.640574,2.376346,9.431690,7.986728,-7.496019,-6.486952,-6.970990,-6.592733,-3.503524,-9.577693,7.997658,1.123602,-6.334543,3.653407,-0.820634,3.872218,7.532955,-5.758435]], dtype = "float32")#candidate|10109|(7, 126)|const|float32
call_10108 = func_8854_call(relay.reshape(const_10109.astype('float32'), [14, 9, 7]))
call_10110 = func_8854_call(relay.reshape(const_10109.astype('float32'), [14, 9, 7]))
func_3250_call = mod.get_global_var('func_3250')
func_3253_call = mutated_mod.get_global_var('func_3253')
var_10112 = relay.var("var_10112", dtype = "int64", shape = ())#candidate|10112|()|var|int64
call_10111 = relay.TupleGetItem(func_3250_call(relay.reshape(var_10112.astype('int64'), [])), 0)
call_10113 = relay.TupleGetItem(func_3253_call(relay.reshape(var_10112.astype('int64'), [])), 0)
output = relay.Tuple([call_10104,call_10108,const_10109,call_10111,var_10112,])
output2 = relay.Tuple([call_10105,call_10110,const_10109,call_10113,var_10112,])
func_10117 = relay.Function([var_10112,], output)
mod['func_10117'] = func_10117
mod = relay.transform.InferType()(mod)
mutated_mod['func_10117'] = func_10117
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10118 = relay.var("var_10118", dtype = "int64", shape = ())#candidate|10118|()|var|int64
func_10117_call = mutated_mod.get_global_var('func_10117')
call_10119 = func_10117_call(var_10118)
output = call_10119
func_10120 = relay.Function([var_10118], output)
mutated_mod['func_10120'] = func_10120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9580_call = mod.get_global_var('func_9580')
func_9581_call = mutated_mod.get_global_var('func_9581')
call_10146 = relay.TupleGetItem(func_9580_call(), 0)
call_10147 = relay.TupleGetItem(func_9581_call(), 0)
func_9632_call = mod.get_global_var('func_9632')
func_9634_call = mutated_mod.get_global_var('func_9634')
var_10207 = relay.var("var_10207", dtype = "float64", shape = (18, 2))#candidate|10207|(18, 2)|var|float64
call_10206 = func_9632_call(relay.reshape(var_10207.astype('float64'), [2, 3, 6]))
call_10208 = func_9632_call(relay.reshape(var_10207.astype('float64'), [2, 3, 6]))
output = relay.Tuple([call_10146,call_10206,var_10207,])
output2 = relay.Tuple([call_10147,call_10208,var_10207,])
func_10209 = relay.Function([var_10207,], output)
mod['func_10209'] = func_10209
mod = relay.transform.InferType()(mod)
var_10210 = relay.var("var_10210", dtype = "float64", shape = (18, 2))#candidate|10210|(18, 2)|var|float64
output = func_10209(var_10210)
func_10211 = relay.Function([var_10210], output)
mutated_mod['func_10211'] = func_10211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3386_call = mod.get_global_var('func_3386')
func_3388_call = mutated_mod.get_global_var('func_3388')
call_10228 = relay.TupleGetItem(func_3386_call(), 0)
call_10229 = relay.TupleGetItem(func_3388_call(), 0)
func_3065_call = mod.get_global_var('func_3065')
func_3066_call = mutated_mod.get_global_var('func_3066')
call_10232 = func_3065_call()
call_10233 = func_3065_call()
func_4882_call = mod.get_global_var('func_4882')
func_4884_call = mutated_mod.get_global_var('func_4884')
call_10234 = func_4882_call()
call_10235 = func_4882_call()
output = relay.Tuple([call_10228,call_10232,call_10234,])
output2 = relay.Tuple([call_10229,call_10233,call_10235,])
func_10240 = relay.Function([], output)
mod['func_10240'] = func_10240
mod = relay.transform.InferType()(mod)
mutated_mod['func_10240'] = func_10240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10240_call = mutated_mod.get_global_var('func_10240')
call_10241 = func_10240_call()
output = call_10241
func_10242 = relay.Function([], output)
mutated_mod['func_10242'] = func_10242
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8315_call = mod.get_global_var('func_8315')
func_8317_call = mutated_mod.get_global_var('func_8317')
call_10302 = relay.TupleGetItem(func_8315_call(), 0)
call_10303 = relay.TupleGetItem(func_8317_call(), 0)
output = call_10302
output2 = call_10303
func_10312 = relay.Function([], output)
mod['func_10312'] = func_10312
mod = relay.transform.InferType()(mod)
output = func_10312()
func_10313 = relay.Function([], output)
mutated_mod['func_10313'] = func_10313
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10337 = relay.var("var_10337", dtype = "uint16", shape = ())#candidate|10337|()|var|uint16
var_10338 = relay.var("var_10338", dtype = "uint16", shape = (10, 8, 9))#candidate|10338|(10, 8, 9)|var|uint16
bop_10339 = relay.less_equal(var_10337.astype('bool'), var_10338.astype('bool')) # shape=(10, 8, 9)
output = bop_10339
output2 = bop_10339
func_10345 = relay.Function([var_10337,var_10338,], output)
mod['func_10345'] = func_10345
mod = relay.transform.InferType()(mod)
var_10346 = relay.var("var_10346", dtype = "uint16", shape = ())#candidate|10346|()|var|uint16
var_10347 = relay.var("var_10347", dtype = "uint16", shape = (10, 8, 9))#candidate|10347|(10, 8, 9)|var|uint16
output = func_10345(var_10346,var_10347,)
func_10348 = relay.Function([var_10346,var_10347,], output)
mutated_mod['func_10348'] = func_10348
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10355 = relay.var("var_10355", dtype = "float64", shape = (7, 3, 14))#candidate|10355|(7, 3, 14)|var|float64
uop_10356 = relay.sqrt(var_10355.astype('float64')) # shape=(7, 3, 14)
bop_10359 = relay.bitwise_and(uop_10356.astype('int16'), relay.reshape(var_10355.astype('int16'), relay.shape_of(uop_10356))) # shape=(7, 3, 14)
func_7150_call = mod.get_global_var('func_7150')
func_7153_call = mutated_mod.get_global_var('func_7153')
const_10363 = relay.const([-2,4,-10,-2,7,1,-5,5,-5,-8,3,-9,-1,-2,7,-9,-10,-8,-10,-1,-8,4,-3,5,8,-5,7,1,-8,-2,-10,-3,4,1,4,2,4,-7,-5,-3,8,-5,1,-2,10,-3,4,9,9,-3,-1,7,3,10,-6,2,-10,-8,2,1,7,10,-4,-1,-10,8,-1,7,-6,-1,-2,8,-9,-7,10,1,-4,9,2,10,4,3,2,-1,-9,-3,-7,-4,-7,5,9,-3,9,-10,1,10,10,3,5,8,-6,4,-2,-10,-1,6,-3,4,10,2,6,7,5,-7,3,4,-8,5,-9,9,-3,2,4,7,-10,7,1,3,5,-8,-5,10,-3,1,1,3,-5,-2,-1,-6,10,-8,-9,-8,-10,5,-9,9,1,3,2,-7,-3,7,-8,4,8,8,4,2,-2,-1,3,2,-2,7,5,2,-5,-9,-3,2,6,9,-5,5,-9,10,-8,5,1,5,-9,1,7,-6,6,4,-7,-3,-3,4,9,-3,8,7,3,5,-1,6,8,-10,2,-8,6,-5,-2,-10,-1,-7,2,-8,8,-7,-10,8,-4,4,-4,-7,4,9,9,6,-4,-10,-9,-9,10,7,-8], dtype = "int64")#candidate|10363|(231,)|const|int64
call_10362 = relay.TupleGetItem(func_7150_call(relay.reshape(const_10363.astype('int64'), [231,])), 0)
call_10364 = relay.TupleGetItem(func_7153_call(relay.reshape(const_10363.astype('int64'), [231,])), 0)
var_10375 = relay.var("var_10375", dtype = "int64", shape = (231,))#candidate|10375|(231,)|var|int64
bop_10376 = relay.floor_divide(const_10363.astype('float32'), relay.reshape(var_10375.astype('float32'), relay.shape_of(const_10363))) # shape=(231,)
func_3471_call = mod.get_global_var('func_3471')
func_3473_call = mutated_mod.get_global_var('func_3473')
call_10379 = relay.TupleGetItem(func_3471_call(), 2)
call_10380 = relay.TupleGetItem(func_3473_call(), 2)
uop_10392 = relay.log2(uop_10356.astype('float32')) # shape=(7, 3, 14)
bop_10394 = relay.multiply(uop_10392.astype('float32'), relay.reshape(bop_10359.astype('float32'), relay.shape_of(uop_10392))) # shape=(7, 3, 14)
output = relay.Tuple([call_10362,bop_10376,call_10379,bop_10394,])
output2 = relay.Tuple([call_10364,bop_10376,call_10380,bop_10394,])
F = relay.Function([var_10355,var_10375,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_10355,var_10375,], output2)
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
