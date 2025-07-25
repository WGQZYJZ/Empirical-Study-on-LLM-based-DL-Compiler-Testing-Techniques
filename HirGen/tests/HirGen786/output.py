import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_135 = relay.var("var_135", dtype = "float32", shape = (15, 1, 15))#candidate|135|(15, 1, 15)|var|float32
var_136 = relay.var("var_136", dtype = "float32", shape = (15, 16, 15))#candidate|136|(15, 16, 15)|var|float32
bop_137 = relay.multiply(var_135.astype('float32'), var_136.astype('float32')) # shape=(15, 16, 15)
output = relay.Tuple([bop_137,])
output2 = relay.Tuple([bop_137,])
func_150 = relay.Function([var_135,var_136,], output)
mod['func_150'] = func_150
mod = relay.transform.InferType()(mod)
mutated_mod['func_150'] = func_150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_150_call = mutated_mod.get_global_var('func_150')
var_152 = relay.var("var_152", dtype = "float32", shape = (15, 1, 15))#candidate|152|(15, 1, 15)|var|float32
var_153 = relay.var("var_153", dtype = "float32", shape = (15, 16, 15))#candidate|153|(15, 16, 15)|var|float32
call_151 = func_150_call(var_152,var_153,)
output = call_151
func_154 = relay.Function([var_152,var_153,], output)
mutated_mod['func_154'] = func_154
mutated_mod = relay.transform.InferType()(mutated_mod)
var_573 = relay.var("var_573", dtype = "float32", shape = (9, 12, 2))#candidate|573|(9, 12, 2)|var|float32
uop_574 = relay.sigmoid(var_573.astype('float32')) # shape=(9, 12, 2)
uop_585 = relay.asin(var_573.astype('float32')) # shape=(9, 12, 2)
uop_601 = relay.atanh(var_573.astype('float64')) # shape=(9, 12, 2)
func_150_call = mod.get_global_var('func_150')
func_154_call = mutated_mod.get_global_var('func_154')
var_604 = relay.var("var_604", dtype = "float32", shape = (25, 9))#candidate|604|(25, 9)|var|float32
var_605 = relay.var("var_605", dtype = "float32", shape = (3600,))#candidate|605|(3600,)|var|float32
call_603 = relay.TupleGetItem(func_150_call(relay.reshape(var_604.astype('float32'), [15, 1, 15]), relay.reshape(var_605.astype('float32'), [15, 16, 15]), ), 0)
call_606 = relay.TupleGetItem(func_154_call(relay.reshape(var_604.astype('float32'), [15, 1, 15]), relay.reshape(var_605.astype('float32'), [15, 16, 15]), ), 0)
func_150_call = mod.get_global_var('func_150')
func_154_call = mutated_mod.get_global_var('func_154')
call_610 = relay.TupleGetItem(func_150_call(relay.reshape(var_604.astype('float32'), [15, 1, 15]), relay.reshape(call_603.astype('float32'), [15, 16, 15]), ), 0)
call_611 = relay.TupleGetItem(func_154_call(relay.reshape(var_604.astype('float32'), [15, 1, 15]), relay.reshape(call_603.astype('float32'), [15, 16, 15]), ), 0)
func_150_call = mod.get_global_var('func_150')
func_154_call = mutated_mod.get_global_var('func_154')
call_625 = relay.TupleGetItem(func_150_call(relay.reshape(var_604.astype('float32'), [15, 1, 15]), relay.reshape(var_605.astype('float32'), [15, 16, 15]), ), 0)
call_626 = relay.TupleGetItem(func_154_call(relay.reshape(var_604.astype('float32'), [15, 1, 15]), relay.reshape(var_605.astype('float32'), [15, 16, 15]), ), 0)
bop_636 = relay.not_equal(uop_574.astype('bool'), relay.reshape(uop_601.astype('bool'), relay.shape_of(uop_574))) # shape=(9, 12, 2)
func_150_call = mod.get_global_var('func_150')
func_154_call = mutated_mod.get_global_var('func_154')
call_645 = relay.TupleGetItem(func_150_call(relay.reshape(var_604.astype('float32'), [15, 1, 15]), relay.reshape(var_605.astype('float32'), [15, 16, 15]), ), 0)
call_646 = relay.TupleGetItem(func_154_call(relay.reshape(var_604.astype('float32'), [15, 1, 15]), relay.reshape(var_605.astype('float32'), [15, 16, 15]), ), 0)
output = relay.Tuple([uop_585,call_603,var_604,var_605,call_610,call_625,bop_636,call_645,])
output2 = relay.Tuple([uop_585,call_606,var_604,var_605,call_611,call_626,bop_636,call_646,])
func_650 = relay.Function([var_573,var_604,var_605,], output)
mod['func_650'] = func_650
mod = relay.transform.InferType()(mod)
mutated_mod['func_650'] = func_650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_650_call = mutated_mod.get_global_var('func_650')
var_652 = relay.var("var_652", dtype = "float32", shape = (9, 12, 2))#candidate|652|(9, 12, 2)|var|float32
var_653 = relay.var("var_653", dtype = "float32", shape = (25, 9))#candidate|653|(25, 9)|var|float32
var_654 = relay.var("var_654", dtype = "float32", shape = (3600,))#candidate|654|(3600,)|var|float32
call_651 = func_650_call(var_652,var_653,var_654,)
output = call_651
func_655 = relay.Function([var_652,var_653,var_654,], output)
mutated_mod['func_655'] = func_655
mutated_mod = relay.transform.InferType()(mutated_mod)
const_669 = relay.const([[[-4.605664],[2.426614],[8.268672],[-8.079884],[2.127834],[-8.187938],[2.566127]],[[-0.240409],[-8.331188],[-5.481459],[-1.357357],[-6.248587],[-5.824945],[8.001852]]], dtype = "float32")#candidate|669|(2, 7, 1)|const|float32
uop_670 = relay.sqrt(const_669.astype('float32')) # shape=(2, 7, 1)
output = uop_670
output2 = uop_670
func_675 = relay.Function([], output)
mod['func_675'] = func_675
mod = relay.transform.InferType()(mod)
mutated_mod['func_675'] = func_675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_675_call = mutated_mod.get_global_var('func_675')
call_676 = func_675_call()
output = call_676
func_677 = relay.Function([], output)
mutated_mod['func_677'] = func_677
mutated_mod = relay.transform.InferType()(mutated_mod)
func_675_call = mod.get_global_var('func_675')
func_677_call = mutated_mod.get_global_var('func_677')
call_733 = func_675_call()
call_734 = func_675_call()
output = call_733
output2 = call_734
func_753 = relay.Function([], output)
mod['func_753'] = func_753
mod = relay.transform.InferType()(mod)
mutated_mod['func_753'] = func_753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_753_call = mutated_mod.get_global_var('func_753')
call_754 = func_753_call()
output = call_754
func_755 = relay.Function([], output)
mutated_mod['func_755'] = func_755
mutated_mod = relay.transform.InferType()(mutated_mod)
func_675_call = mod.get_global_var('func_675')
func_677_call = mutated_mod.get_global_var('func_677')
call_839 = func_675_call()
call_840 = func_675_call()
uop_856 = relay.atan(call_839.astype('float32')) # shape=(2, 7, 1)
uop_858 = relay.atan(call_840.astype('float32')) # shape=(2, 7, 1)
output = relay.Tuple([uop_856,])
output2 = relay.Tuple([uop_858,])
func_861 = relay.Function([], output)
mod['func_861'] = func_861
mod = relay.transform.InferType()(mod)
output = func_861()
func_862 = relay.Function([], output)
mutated_mod['func_862'] = func_862
mutated_mod = relay.transform.InferType()(mutated_mod)
const_893 = relay.const([[[7,-3,8,-10,8,-2,-7,3,-9],[2,9,-2,-6,1,2,-9,2,5],[5,-9,-1,4,-10,-8,3,3,-1],[-4,-4,2,-3,-6,5,6,-7,3],[-4,6,5,2,-3,9,4,2,-8],[-5,-7,7,2,-4,-8,7,-5,7],[6,-7,8,2,1,9,10,2,3],[-9,-5,-4,-9,5,5,-5,1,9],[-10,-1,-6,-10,-2,-4,-4,-2,8],[-1,10,-3,8,-5,10,8,6,8]],[[-10,10,3,-9,-9,-5,10,3,2],[6,-4,8,-4,3,-8,3,1,9],[7,8,-2,2,1,-5,-3,-10,1],[-10,-6,4,6,-1,-1,1,-2,-4],[4,-8,1,-5,-4,3,4,-10,-8],[6,4,-3,10,2,2,6,-10,-10],[-10,7,-1,1,4,8,8,8,-1],[-8,2,3,-4,2,5,-8,7,3],[6,5,-7,-5,-7,8,3,-9,6],[1,-2,5,-4,-4,-10,9,3,9]],[[-7,5,-7,-1,9,-5,3,4,-10],[-3,-3,3,6,-9,-6,-6,-3,6],[-4,-8,1,7,-3,9,1,6,-1],[-9,-3,-3,-9,3,-2,1,7,10],[-5,2,-9,9,-1,5,-6,-8,-5],[7,3,-5,10,-10,5,5,-6,-10],[-7,6,6,1,-8,-10,-1,-4,-8],[9,4,4,-9,1,-7,-2,-2,2],[2,9,-2,10,9,-8,-4,6,6],[9,-1,5,-1,-2,-7,-10,-10,8]],[[1,7,-5,-6,2,9,2,-7,10],[2,-1,6,-3,-7,-7,-6,7,10],[-8,1,8,10,-9,6,-9,1,-5],[7,3,-8,3,1,-7,1,7,7],[-3,-9,6,-4,-4,-6,-1,-4,9],[7,7,-1,10,10,-6,-5,6,3],[-9,-8,1,-9,-6,-9,6,8,-7],[-8,1,-6,-4,7,-7,3,-9,-9],[4,-5,3,-9,1,2,6,-6,-7],[5,-3,3,-3,6,-7,4,-2,-4]],[[-2,-4,10,-2,-6,-3,-1,6,1],[4,6,-7,6,6,10,-5,-5,-7],[4,1,-10,-5,-5,4,10,1,9],[-1,-1,3,1,6,-6,10,6,2],[-6,-4,-7,8,-6,5,8,2,-5],[5,-4,9,-5,2,2,7,10,-10],[10,4,6,-5,5,8,-2,-5,5],[6,5,-3,-1,-5,-2,10,3,-9],[-5,-5,-2,2,5,10,-1,2,-6],[3,3,-8,2,-6,4,-4,-2,9]]], dtype = "int8")#candidate|893|(5, 10, 9)|const|int8
var_894 = relay.var("var_894", dtype = "int8", shape = (5, 10, 9))#candidate|894|(5, 10, 9)|var|int8
bop_895 = relay.bitwise_and(const_893.astype('int8'), relay.reshape(var_894.astype('int8'), relay.shape_of(const_893))) # shape=(5, 10, 9)
output = relay.Tuple([bop_895,])
output2 = relay.Tuple([bop_895,])
func_898 = relay.Function([var_894,], output)
mod['func_898'] = func_898
mod = relay.transform.InferType()(mod)
mutated_mod['func_898'] = func_898
mutated_mod = relay.transform.InferType()(mutated_mod)
var_899 = relay.var("var_899", dtype = "int8", shape = (5, 10, 9))#candidate|899|(5, 10, 9)|var|int8
func_898_call = mutated_mod.get_global_var('func_898')
call_900 = func_898_call(var_899)
output = call_900
func_901 = relay.Function([var_899], output)
mutated_mod['func_901'] = func_901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_675_call = mod.get_global_var('func_675')
func_677_call = mutated_mod.get_global_var('func_677')
call_938 = func_675_call()
call_939 = func_675_call()
func_650_call = mod.get_global_var('func_650')
func_655_call = mutated_mod.get_global_var('func_655')
var_944 = relay.var("var_944", dtype = "float32", shape = (216,))#candidate|944|(216,)|var|float32
const_945 = relay.const([[6.559598,8.520937,3.376526,2.103347,-4.472567,5.197752,9.229617,-6.879451,-3.899565,3.415231,3.631903,9.392408,8.949609,-9.653353,6.432199,-2.877481,-1.633675,6.199146,4.854012,-6.250662,4.148684,-9.030411,-4.765673,0.374287,1.324068,-2.067525,6.990380,-4.925399,-2.086549,-3.276029,-6.203713,-1.708010,5.237820,-8.210632,-7.644854,-3.081389,-2.951151,5.680741,-9.051908,4.688384,9.159912,-5.254097,-5.178243,5.223164,5.552762,-9.728413,-2.504194,-1.919790,-3.237858,6.389251,4.715017,-8.529993,-0.363364,3.779561,6.667659,1.626202,-1.208949,9.332608,-2.642141,4.258297,-8.254250,8.795625,0.299313,-7.284441,5.311462,-5.581879,-8.119444,-6.509700,-5.013044,8.800820,1.043990,-3.591487,-6.965473,-7.745305,-5.318079,-8.386434,5.586394,-9.405722,1.905362,-9.776605,-5.247929,-2.469826,-6.917796,6.726198,-0.517225,-3.867971,5.080889,7.378630,-1.340604,-5.748111,5.795443,7.253480,7.199463,5.354781,8.530856,1.878777,5.473012,-3.357613,-0.602114,-6.137267,-0.030155,-1.020638,-4.073204,5.806221,8.542498,1.127224,-4.198015,0.684134,-9.693260,-0.126029,2.225528,9.105535,0.043778,-7.459648,-8.186905,-9.814538,4.759872,-2.833462,-0.105462,-6.528225,-2.737118,8.689735,-0.172541,-4.931845,3.632089,-0.449123,-0.153069,6.385344,2.718592,3.316202,8.346689,-4.090578,7.785066,-4.076442,-8.173646,2.105309,-1.643826,0.985404,-3.361557,-7.687151,3.243955,-7.832724,-0.122888,2.511040,6.017212,7.166807,6.607884,7.958660,0.402300,-3.764510,-0.582334,-4.750868,-7.787128,4.849621,3.237370,7.408510,1.428315,-7.621799,1.411392,3.456984,-6.619016,5.787539,9.357446,-3.872778,-4.044429,-0.869277,5.956449,-2.813230,2.060262,-5.721184,3.272428,7.693655,7.348717,-2.806401,3.032229,6.821644,6.662105,6.822813,9.856793,1.987540,6.842357,-5.558177,-3.665445,-1.408539,-2.174910,-9.503057,-8.228380,-2.345745,2.357027,5.097911,1.125008,-3.756033,4.889547,1.919641,-6.825074,8.690051,-7.549171,-8.984523,-9.575228,-6.456239,4.514120,-5.181667,-4.986564,6.288061,6.628680,2.210392,7.768257,4.318597,5.734095,4.822855,1.734193,5.066141,-2.903906,-0.644723,2.960729,4.492629,9.334339,-5.538204,7.257615,8.019438,-6.017206,3.300969,2.531278,5.537197,3.170948]], dtype = "float32")#candidate|945|(1, 225)|const|float32
var_946 = relay.var("var_946", dtype = "float32", shape = (3600,))#candidate|946|(3600,)|var|float32
call_943 = relay.TupleGetItem(func_650_call(relay.reshape(var_944.astype('float32'), [9, 12, 2]), relay.reshape(const_945.astype('float32'), [25, 9]), relay.reshape(var_946.astype('float32'), [3600,]), ), 7)
call_947 = relay.TupleGetItem(func_655_call(relay.reshape(var_944.astype('float32'), [9, 12, 2]), relay.reshape(const_945.astype('float32'), [25, 9]), relay.reshape(var_946.astype('float32'), [3600,]), ), 7)
func_675_call = mod.get_global_var('func_675')
func_677_call = mutated_mod.get_global_var('func_677')
call_949 = func_675_call()
call_950 = func_675_call()
uop_953 = relay.tan(const_945.astype('float32')) # shape=(1, 225)
func_898_call = mod.get_global_var('func_898')
func_901_call = mutated_mod.get_global_var('func_901')
var_960 = relay.var("var_960", dtype = "int8", shape = (5, 90))#candidate|960|(5, 90)|var|int8
call_959 = relay.TupleGetItem(func_898_call(relay.reshape(var_960.astype('int8'), [5, 10, 9])), 0)
call_961 = relay.TupleGetItem(func_901_call(relay.reshape(var_960.astype('int8'), [5, 10, 9])), 0)
func_861_call = mod.get_global_var('func_861')
func_862_call = mutated_mod.get_global_var('func_862')
call_970 = relay.TupleGetItem(func_861_call(), 0)
call_971 = relay.TupleGetItem(func_862_call(), 0)
output = relay.Tuple([call_938,call_943,var_944,var_946,call_949,uop_953,call_959,var_960,call_970,])
output2 = relay.Tuple([call_939,call_947,var_944,var_946,call_950,uop_953,call_961,var_960,call_971,])
func_974 = relay.Function([var_944,var_946,var_960,], output)
mod['func_974'] = func_974
mod = relay.transform.InferType()(mod)
mutated_mod['func_974'] = func_974
mutated_mod = relay.transform.InferType()(mutated_mod)
func_974_call = mutated_mod.get_global_var('func_974')
var_976 = relay.var("var_976", dtype = "float32", shape = (216,))#candidate|976|(216,)|var|float32
var_977 = relay.var("var_977", dtype = "float32", shape = (3600,))#candidate|977|(3600,)|var|float32
var_978 = relay.var("var_978", dtype = "int8", shape = (5, 90))#candidate|978|(5, 90)|var|int8
call_975 = func_974_call(var_976,var_977,var_978,)
output = call_975
func_979 = relay.Function([var_976,var_977,var_978,], output)
mutated_mod['func_979'] = func_979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_861_call = mod.get_global_var('func_861')
func_862_call = mutated_mod.get_global_var('func_862')
call_1023 = relay.TupleGetItem(func_861_call(), 0)
call_1024 = relay.TupleGetItem(func_862_call(), 0)
func_753_call = mod.get_global_var('func_753')
func_755_call = mutated_mod.get_global_var('func_755')
call_1030 = func_753_call()
call_1031 = func_753_call()
bop_1039 = relay.logical_xor(call_1030.astype('int32'), relay.reshape(call_1023.astype('int32'), relay.shape_of(call_1030))) # shape=(2, 7, 1)
bop_1042 = relay.logical_xor(call_1031.astype('int32'), relay.reshape(call_1024.astype('int32'), relay.shape_of(call_1031))) # shape=(2, 7, 1)
func_898_call = mod.get_global_var('func_898')
func_901_call = mutated_mod.get_global_var('func_901')
const_1055 = relay.const([4,-7,9,10,-8,-5,-7,-2,-3,5,-7,6,-5,-9,6,10,-5,10,6,8,-2,4,-7,-8,-3,8,8,-2,-4,7,-1,10,7,10,10,5,10,3,-8,-10,4,3,-1,-6,-7,5,-4,-4,4,2,1,-8,-1,-10,2,1,7,9,-8,5,9,-5,-6,4,4,-6,7,8,4,8,8,-1,3,5,4,9,9,-6,5,-6,8,-6,5,3,-9,-5,-10,2,-6,-7,6,-6,3,1,-4,9,-7,8,-8,-1,-2,6,3,-7,4,3,-1,-6,-3,-4,-1,10,9,-2,-9,-4,9,2,7,-5,3,-2,7,3,-4,-6,2,-7,-3,8,1,-10,-1,6,-4,-10,9,5,1,-5,-5,-1,6,-7,-6,1,-8,-2,5,-6,9,8,-7,5,1,2,10,4,-3,6,-8,1,-8,-5,-10,-4,7,10,-4,-2,4,4,1,-1,9,-8,-4,4,-1,-5,-8,-4,2,10,9,-3,-8,-9,5,5,-9,2,1,5,3,-5,-10,9,-2,-8,-1,-6,-9,9,-4,7,-9,-7,5,4,-4,2,-9,6,7,4,6,-8,4,-9,4,-2,-7,5,10,1,-10,8,1,5,-9,-6,1,-3,1,-3,-8,-10,-3,6,-6,-9,-7,10,-2,-5,-5,9,-5,1,4,5,-9,8,1,9,-10,-8,5,4,2,-2,2,-1,4,5,5,2,6,-10,-4,6,5,-1,-1,-10,6,-10,-5,-7,4,-9,-1,-5,-2,6,1,-10,-8,-9,-9,2,2,6,-4,8,-5,6,-1,3,-5,-9,-2,3,3,-9,-2,8,4,3,4,-3,-10,5,10,-5,10,1,5,10,-7,-8,1,-5,9,10,-1,4,-1,-3,10,4,-1,10,1,4,10,-9,10,-5,-3,-6,-7,6,-1,9,-8,-9,-9,7,-10,8,-4,2,-10,-7,-1,7,-3,-10,-3,-4,-3,10,-4,2,9,-6,6,9,5,8,8,6,8,4,4,-10,10,8,8,-8,1,-2,-9,2,-6,10,6,3,-3,-5,4,-3,-7,10,5,4,1,-3,-6,4,7,-8,-3,7,10,2,-7,-10,-8,-4,8,8,-4,10,8,-6,10,-10,-4,9,-10,8,8,4,8,-10,5,-6,1,-3,-9,-5,-10,4,-1,8,5,-1,-7,10,2,-4,10,-10,-3,1,1,-1], dtype = "int8")#candidate|1055|(450,)|const|int8
call_1054 = relay.TupleGetItem(func_898_call(relay.reshape(const_1055.astype('int8'), [5, 10, 9])), 0)
call_1056 = relay.TupleGetItem(func_901_call(relay.reshape(const_1055.astype('int8'), [5, 10, 9])), 0)
bop_1057 = relay.less_equal(call_1023.astype('bool'), const_1055.astype('bool')) # shape=(2, 7, 450)
bop_1060 = relay.less_equal(call_1024.astype('bool'), const_1055.astype('bool')) # shape=(2, 7, 450)
bop_1080 = relay.power(bop_1057.astype('float32'), bop_1039.astype('float32')) # shape=(2, 7, 450)
bop_1083 = relay.power(bop_1060.astype('float32'), bop_1042.astype('float32')) # shape=(2, 7, 450)
uop_1084 = relay.sqrt(call_1054.astype('float32')) # shape=(5, 10, 9)
uop_1086 = relay.sqrt(call_1056.astype('float32')) # shape=(5, 10, 9)
func_861_call = mod.get_global_var('func_861')
func_862_call = mutated_mod.get_global_var('func_862')
call_1089 = relay.TupleGetItem(func_861_call(), 0)
call_1090 = relay.TupleGetItem(func_862_call(), 0)
output = relay.Tuple([bop_1080,uop_1084,call_1089,])
output2 = relay.Tuple([bop_1083,uop_1086,call_1090,])
func_1095 = relay.Function([], output)
mod['func_1095'] = func_1095
mod = relay.transform.InferType()(mod)
mutated_mod['func_1095'] = func_1095
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1095_call = mutated_mod.get_global_var('func_1095')
call_1096 = func_1095_call()
output = call_1096
func_1097 = relay.Function([], output)
mutated_mod['func_1097'] = func_1097
mutated_mod = relay.transform.InferType()(mutated_mod)
func_753_call = mod.get_global_var('func_753')
func_755_call = mutated_mod.get_global_var('func_755')
call_1104 = func_753_call()
call_1105 = func_753_call()
output = relay.Tuple([call_1104,])
output2 = relay.Tuple([call_1105,])
func_1119 = relay.Function([], output)
mod['func_1119'] = func_1119
mod = relay.transform.InferType()(mod)
output = func_1119()
func_1120 = relay.Function([], output)
mutated_mod['func_1120'] = func_1120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_753_call = mod.get_global_var('func_753')
func_755_call = mutated_mod.get_global_var('func_755')
call_1124 = func_753_call()
call_1125 = func_753_call()
func_898_call = mod.get_global_var('func_898')
func_901_call = mutated_mod.get_global_var('func_901')
const_1155 = relay.const([-4,9,8,2,-8,-2,4,-7,-8,5,-1,1,-7,-5,6,6,-2,1,8,-2,6,7,7,-2,-4,-6,-3,-9,2,3,10,7,6,-4,1,-1,1,6,3,-2,9,3,4,10,8,1,5,-9,-6,-3,10,-4,5,6,10,-6,5,10,-5,-5,-6,-8,4,9,-2,-7,-8,3,2,1,9,-10,-9,6,-3,-7,-5,7,4,-1,8,-1,8,-10,-5,-2,-10,-1,-7,3,5,-6,-6,-2,-10,-9,1,-5,-5,-1,7,5,10,-6,-10,-4,10,-7,-4,9,4,-2,-9,5,-3,-4,-2,8,4,6,7,-1,1,-5,7,-8,-3,7,9,-8,8,7,-5,-1,-10,-3,6,-6,-1,1,5,10,-10,-2,9,-5,5,9,6,-9,7,-5,-7,10,-10,-8,10,4,5,3,9,-2,-8,6,-3,2,8,-2,6,5,-3,-2,-10,-5,4,8,-5,-10,1,9,-1,-3,8,-6,-7,2,-3,-5,3,-8,9,2,6,9,8,-1,-8,-9,-10,-1,-5,1,7,5,-7,9,-8,-1,3,-2,-7,9,9,-4,-3,8,-9,-8,-6,-8,-5,-8,-6,-7,-9,9,6,-3,-7,4,1,-8,2,7,-10,-10,10,9,-8,-6,-7,-5,4,-8,5,1,-5,-8,-6,6,10,2,-5,-9,-7,-4,-1,-7,-8,-7,6,-1,-6,1,-4,7,-2,-7,2,-2,10,-5,-4,5,7,7,10,8,8,8,-6,-7,6,7,-9,-6,4,9,4,-10,-6,8,-4,1,-6,4,-4,10,7,7,-6,-3,6,6,6,3,-4,9,7,-10,7,-5,-6,-2,-2,-9,5,7,-3,-1,3,-10,-5,3,-9,5,8,8,4,-9,2,-3,9,6,6,-9,-1,4,-10,-10,-1,-4,2,4,-3,-2,-10,-9,6,-9,5,1,-8,4,1,6,6,2,-3,5,1,8,4,-8,-5,5,6,-5,-1,4,-10,6,2,7,-4,1,2,7,-1,8,-4,5,9,8,-1,-1,-5,-9,5,-4,8,4,-7,6,6,3,7,1,9,5,2,-1,5,5,5,8,-5,5,-3,-9,7,8,9,1,7,-6,-3,5,8,-7,9,8,6,-5,6,-8,3,8,-5,10,4,2,-4,7,-9,4,-8,2,-6,4,1,7,-8,-8,2,7,-3,-5,-8,-6], dtype = "int8")#candidate|1155|(450,)|const|int8
call_1154 = relay.TupleGetItem(func_898_call(relay.reshape(const_1155.astype('int8'), [5, 10, 9])), 0)
call_1156 = relay.TupleGetItem(func_901_call(relay.reshape(const_1155.astype('int8'), [5, 10, 9])), 0)
output = relay.Tuple([call_1124,call_1154,const_1155,])
output2 = relay.Tuple([call_1125,call_1156,const_1155,])
func_1171 = relay.Function([], output)
mod['func_1171'] = func_1171
mod = relay.transform.InferType()(mod)
mutated_mod['func_1171'] = func_1171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1171_call = mutated_mod.get_global_var('func_1171')
call_1172 = func_1171_call()
output = call_1172
func_1173 = relay.Function([], output)
mutated_mod['func_1173'] = func_1173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_861_call = mod.get_global_var('func_861')
func_862_call = mutated_mod.get_global_var('func_862')
call_1188 = relay.TupleGetItem(func_861_call(), 0)
call_1189 = relay.TupleGetItem(func_862_call(), 0)
output = call_1188
output2 = call_1189
func_1190 = relay.Function([], output)
mod['func_1190'] = func_1190
mod = relay.transform.InferType()(mod)
output = func_1190()
func_1191 = relay.Function([], output)
mutated_mod['func_1191'] = func_1191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1171_call = mod.get_global_var('func_1171')
func_1173_call = mutated_mod.get_global_var('func_1173')
call_1222 = relay.TupleGetItem(func_1171_call(), 2)
call_1223 = relay.TupleGetItem(func_1173_call(), 2)
func_1119_call = mod.get_global_var('func_1119')
func_1120_call = mutated_mod.get_global_var('func_1120')
call_1250 = relay.TupleGetItem(func_1119_call(), 0)
call_1251 = relay.TupleGetItem(func_1120_call(), 0)
uop_1254 = relay.cosh(call_1250.astype('float32')) # shape=(2, 7, 1)
uop_1256 = relay.cosh(call_1251.astype('float32')) # shape=(2, 7, 1)
output = relay.Tuple([call_1222,uop_1254,])
output2 = relay.Tuple([call_1223,uop_1256,])
func_1264 = relay.Function([], output)
mod['func_1264'] = func_1264
mod = relay.transform.InferType()(mod)
output = func_1264()
func_1265 = relay.Function([], output)
mutated_mod['func_1265'] = func_1265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1095_call = mod.get_global_var('func_1095')
func_1097_call = mutated_mod.get_global_var('func_1097')
call_1292 = relay.TupleGetItem(func_1095_call(), 2)
call_1293 = relay.TupleGetItem(func_1097_call(), 2)
output = relay.Tuple([call_1292,])
output2 = relay.Tuple([call_1293,])
func_1324 = relay.Function([], output)
mod['func_1324'] = func_1324
mod = relay.transform.InferType()(mod)
output = func_1324()
func_1325 = relay.Function([], output)
mutated_mod['func_1325'] = func_1325
mutated_mod = relay.transform.InferType()(mutated_mod)
func_675_call = mod.get_global_var('func_675')
func_677_call = mutated_mod.get_global_var('func_677')
call_1368 = func_675_call()
call_1369 = func_675_call()
func_1264_call = mod.get_global_var('func_1264')
func_1265_call = mutated_mod.get_global_var('func_1265')
call_1374 = relay.TupleGetItem(func_1264_call(), 1)
call_1375 = relay.TupleGetItem(func_1265_call(), 1)
output = relay.Tuple([call_1368,call_1374,])
output2 = relay.Tuple([call_1369,call_1375,])
func_1384 = relay.Function([], output)
mod['func_1384'] = func_1384
mod = relay.transform.InferType()(mod)
mutated_mod['func_1384'] = func_1384
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1384_call = mutated_mod.get_global_var('func_1384')
call_1385 = func_1384_call()
output = call_1385
func_1386 = relay.Function([], output)
mutated_mod['func_1386'] = func_1386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_861_call = mod.get_global_var('func_861')
func_862_call = mutated_mod.get_global_var('func_862')
call_1402 = relay.TupleGetItem(func_861_call(), 0)
call_1403 = relay.TupleGetItem(func_862_call(), 0)
func_753_call = mod.get_global_var('func_753')
func_755_call = mutated_mod.get_global_var('func_755')
call_1416 = func_753_call()
call_1417 = func_753_call()
bop_1421 = relay.bitwise_and(call_1416.astype('uint16'), relay.reshape(call_1402.astype('uint16'), relay.shape_of(call_1416))) # shape=(2, 7, 1)
bop_1424 = relay.bitwise_and(call_1417.astype('uint16'), relay.reshape(call_1403.astype('uint16'), relay.shape_of(call_1417))) # shape=(2, 7, 1)
func_1119_call = mod.get_global_var('func_1119')
func_1120_call = mutated_mod.get_global_var('func_1120')
call_1452 = relay.TupleGetItem(func_1119_call(), 0)
call_1453 = relay.TupleGetItem(func_1120_call(), 0)
func_1119_call = mod.get_global_var('func_1119')
func_1120_call = mutated_mod.get_global_var('func_1120')
call_1456 = relay.TupleGetItem(func_1119_call(), 0)
call_1457 = relay.TupleGetItem(func_1120_call(), 0)
output = relay.Tuple([bop_1421,call_1452,call_1456,])
output2 = relay.Tuple([bop_1424,call_1453,call_1457,])
func_1460 = relay.Function([], output)
mod['func_1460'] = func_1460
mod = relay.transform.InferType()(mod)
mutated_mod['func_1460'] = func_1460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1460_call = mutated_mod.get_global_var('func_1460')
call_1461 = func_1460_call()
output = call_1461
func_1462 = relay.Function([], output)
mutated_mod['func_1462'] = func_1462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1190_call = mod.get_global_var('func_1190')
func_1191_call = mutated_mod.get_global_var('func_1191')
call_1483 = func_1190_call()
call_1484 = func_1190_call()
output = relay.Tuple([call_1483,])
output2 = relay.Tuple([call_1484,])
func_1489 = relay.Function([], output)
mod['func_1489'] = func_1489
mod = relay.transform.InferType()(mod)
output = func_1489()
func_1490 = relay.Function([], output)
mutated_mod['func_1490'] = func_1490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1119_call = mod.get_global_var('func_1119')
func_1120_call = mutated_mod.get_global_var('func_1120')
call_1600 = relay.TupleGetItem(func_1119_call(), 0)
call_1601 = relay.TupleGetItem(func_1120_call(), 0)
func_1324_call = mod.get_global_var('func_1324')
func_1325_call = mutated_mod.get_global_var('func_1325')
call_1609 = relay.TupleGetItem(func_1324_call(), 0)
call_1610 = relay.TupleGetItem(func_1325_call(), 0)
func_974_call = mod.get_global_var('func_974')
func_979_call = mutated_mod.get_global_var('func_979')
var_1613 = relay.var("var_1613", dtype = "float32", shape = (216,))#candidate|1613|(216,)|var|float32
var_1614 = relay.var("var_1614", dtype = "float32", shape = (3600,))#candidate|1614|(3600,)|var|float32
var_1615 = relay.var("var_1615", dtype = "int8", shape = (450,))#candidate|1615|(450,)|var|int8
call_1612 = relay.TupleGetItem(func_974_call(relay.reshape(var_1613.astype('float32'), [216,]), relay.reshape(var_1614.astype('float32'), [3600,]), relay.reshape(var_1615.astype('int8'), [5, 90]), ), 6)
call_1616 = relay.TupleGetItem(func_979_call(relay.reshape(var_1613.astype('float32'), [216,]), relay.reshape(var_1614.astype('float32'), [3600,]), relay.reshape(var_1615.astype('int8'), [5, 90]), ), 6)
output = relay.Tuple([call_1600,call_1609,call_1612,var_1613,var_1614,var_1615,])
output2 = relay.Tuple([call_1601,call_1610,call_1616,var_1613,var_1614,var_1615,])
func_1628 = relay.Function([var_1613,var_1614,var_1615,], output)
mod['func_1628'] = func_1628
mod = relay.transform.InferType()(mod)
mutated_mod['func_1628'] = func_1628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1628_call = mutated_mod.get_global_var('func_1628')
var_1630 = relay.var("var_1630", dtype = "float32", shape = (216,))#candidate|1630|(216,)|var|float32
var_1631 = relay.var("var_1631", dtype = "float32", shape = (3600,))#candidate|1631|(3600,)|var|float32
var_1632 = relay.var("var_1632", dtype = "int8", shape = (450,))#candidate|1632|(450,)|var|int8
call_1629 = func_1628_call(var_1630,var_1631,var_1632,)
output = call_1629
func_1633 = relay.Function([var_1630,var_1631,var_1632,], output)
mutated_mod['func_1633'] = func_1633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1324_call = mod.get_global_var('func_1324')
func_1325_call = mutated_mod.get_global_var('func_1325')
call_1675 = relay.TupleGetItem(func_1324_call(), 0)
call_1676 = relay.TupleGetItem(func_1325_call(), 0)
func_1171_call = mod.get_global_var('func_1171')
func_1173_call = mutated_mod.get_global_var('func_1173')
call_1687 = relay.TupleGetItem(func_1171_call(), 1)
call_1688 = relay.TupleGetItem(func_1173_call(), 1)
output = relay.Tuple([call_1675,call_1687,])
output2 = relay.Tuple([call_1676,call_1688,])
func_1691 = relay.Function([], output)
mod['func_1691'] = func_1691
mod = relay.transform.InferType()(mod)
mutated_mod['func_1691'] = func_1691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1691_call = mutated_mod.get_global_var('func_1691')
call_1692 = func_1691_call()
output = call_1692
func_1693 = relay.Function([], output)
mutated_mod['func_1693'] = func_1693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1264_call = mod.get_global_var('func_1264')
func_1265_call = mutated_mod.get_global_var('func_1265')
call_1725 = relay.TupleGetItem(func_1264_call(), 0)
call_1726 = relay.TupleGetItem(func_1265_call(), 0)
output = relay.Tuple([call_1725,])
output2 = relay.Tuple([call_1726,])
func_1753 = relay.Function([], output)
mod['func_1753'] = func_1753
mod = relay.transform.InferType()(mod)
output = func_1753()
func_1754 = relay.Function([], output)
mutated_mod['func_1754'] = func_1754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_753_call = mod.get_global_var('func_753')
func_755_call = mutated_mod.get_global_var('func_755')
call_1761 = func_753_call()
call_1762 = func_753_call()
func_1264_call = mod.get_global_var('func_1264')
func_1265_call = mutated_mod.get_global_var('func_1265')
call_1768 = relay.TupleGetItem(func_1264_call(), 1)
call_1769 = relay.TupleGetItem(func_1265_call(), 1)
output = relay.Tuple([call_1761,call_1768,])
output2 = relay.Tuple([call_1762,call_1769,])
func_1778 = relay.Function([], output)
mod['func_1778'] = func_1778
mod = relay.transform.InferType()(mod)
mutated_mod['func_1778'] = func_1778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1778_call = mutated_mod.get_global_var('func_1778')
call_1779 = func_1778_call()
output = call_1779
func_1780 = relay.Function([], output)
mutated_mod['func_1780'] = func_1780
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1781 = relay.var("var_1781", dtype = "uint32", shape = (12, 5, 10))#candidate|1781|(12, 5, 10)|var|uint32
const_1782 = relay.const([[[-1,6,-8,9,-1,6,-5,5,-2,1],[9,-7,-9,1,9,10,4,-3,10,10],[2,-9,4,-1,1,2,-7,10,7,-7],[-9,8,7,-6,5,2,1,2,-9,4],[6,-9,6,-10,3,1,6,-5,-1,4]],[[6,3,7,-3,-10,-6,2,9,7,10],[9,-1,-3,10,7,9,-9,-3,10,5],[-2,8,8,-1,-9,4,6,-2,2,-2],[5,-4,-6,1,4,7,8,-9,3,1],[5,-9,-3,-8,3,3,1,-10,-6,-2]],[[6,-6,5,1,7,1,9,1,-10,-6],[10,9,-9,-8,-2,7,2,-4,-7,4],[-1,6,-4,2,7,-7,9,10,-6,5],[1,-10,5,9,-3,8,7,-3,-10,-4],[-7,5,8,-4,-4,-4,2,9,10,-9]],[[-8,-6,-10,5,-6,-6,2,8,7,-4],[-2,-7,2,2,-3,-4,10,7,9,-2],[2,7,-1,2,7,-8,-6,-3,-2,-10],[-10,5,4,-1,-3,7,3,9,-9,10],[9,-4,7,-3,4,4,-10,5,-3,9]],[[9,3,-2,-6,5,6,5,1,7,1],[-9,-9,-5,5,1,6,-9,-4,3,-1],[-5,4,-5,6,-9,7,-3,9,1,8],[7,3,-4,7,6,-6,5,5,-5,3],[-7,1,7,9,-3,9,2,-6,-9,-2]],[[2,-8,-7,8,1,5,-2,-9,6,4],[-5,-9,-4,-3,-1,8,4,2,-8,-1],[-10,8,-3,-10,4,-10,8,8,-8,5],[-10,3,-8,5,-5,-6,3,6,10,6],[-3,-5,-10,3,7,-7,10,1,7,5]],[[-2,-7,-4,2,-3,9,9,-7,10,6],[7,-4,-5,6,-1,-6,-1,-10,9,10],[-4,-8,-5,-3,2,-2,-5,5,-3,4],[1,9,-4,-10,2,-5,-10,-1,-5,-2],[4,-5,2,8,2,-9,3,-8,6,-10]],[[-7,-5,5,2,10,8,-7,10,-4,5],[2,10,4,2,3,8,-6,-4,1,-2],[9,-7,-4,8,-7,3,-10,5,-10,-2],[1,-2,-7,10,4,10,-4,4,4,-6],[-6,10,-2,8,4,-5,-3,9,-3,7]],[[3,-3,-2,6,8,7,-1,-9,-4,4],[-10,10,-6,-1,-10,-10,-4,1,-9,-4],[-9,2,9,-2,2,-10,7,-4,-9,-3],[3,-3,6,7,-10,-4,-3,8,2,5],[-8,-4,5,9,5,4,-7,7,2,1]],[[-4,-1,-3,-10,-1,-7,-2,-5,1,2],[7,-1,2,8,-3,-5,3,-3,7,1],[8,10,-9,6,10,-5,3,-1,-6,-8],[7,-6,-1,7,2,-7,-4,-2,-1,-4],[-6,8,-4,6,-10,-9,-10,-5,3,9]],[[8,10,3,8,10,-7,-8,10,5,-2],[-10,2,-5,3,1,-5,-9,2,7,-8],[-1,-7,-1,2,3,-3,-6,-5,3,1],[9,2,3,10,3,8,4,-4,-2,-4],[-2,-10,-1,-1,2,-6,-10,-8,2,2]],[[7,-9,7,7,10,6,8,8,2,4],[1,-4,-8,-3,-10,4,-7,8,6,5],[7,-8,1,4,7,-7,8,9,-4,4],[9,1,3,-10,-5,7,-10,6,-2,3],[8,10,-1,-2,3,-9,6,-8,9,9]]], dtype = "uint32")#candidate|1782|(12, 5, 10)|const|uint32
bop_1783 = relay.not_equal(var_1781.astype('bool'), relay.reshape(const_1782.astype('bool'), relay.shape_of(var_1781))) # shape=(12, 5, 10)
func_898_call = mod.get_global_var('func_898')
func_901_call = mutated_mod.get_global_var('func_901')
var_1788 = relay.var("var_1788", dtype = "int8", shape = (1, 450))#candidate|1788|(1, 450)|var|int8
call_1787 = relay.TupleGetItem(func_898_call(relay.reshape(var_1788.astype('int8'), [5, 10, 9])), 0)
call_1789 = relay.TupleGetItem(func_901_call(relay.reshape(var_1788.astype('int8'), [5, 10, 9])), 0)
func_974_call = mod.get_global_var('func_974')
func_979_call = mutated_mod.get_global_var('func_979')
const_1795 = relay.const([7.747522,3.648443,4.232542,2.091401,0.043523,-2.934896,-2.663358,-2.344469,0.390629,2.440211,9.790977,4.331220,-5.798835,-7.930827,7.579219,9.381309,9.111128,1.754478,5.622252,2.918329,-7.218557,-2.065093,-6.573872,-4.404091,3.822197,5.936920,0.750713,2.289667,-3.234538,-6.867783,-8.732475,4.696588,-0.565034,-9.187449,3.727572,-4.353363,-3.739521,2.237373,-5.719122,-7.754529,5.993066,-2.591912,-1.767704,3.220139,5.111534,2.580285,5.199198,9.426342,3.498395,5.978298,3.532010,-6.656753,-8.400333,-5.160420,5.436212,2.337229,4.214249,-5.666084,3.930781,-8.665158,4.514771,-7.069376,-7.930227,-0.465156,-1.663608,7.582905,-4.301162,8.597248,0.510826,0.350235,-1.908995,7.850172,-2.971355,-5.565924,2.784434,0.655472,-2.348572,-5.381975,5.705657,-8.055049,-8.729279,-3.183661,6.068637,-4.693456,8.435432,3.360533,-1.541280,2.670940,-4.457175,-4.110126,7.777940,-6.861327,-7.243706,-1.008737,-4.025070,4.899283,-5.291027,2.153999,2.319760,-1.434423,9.750052,-3.985400,6.957939,-0.736090,3.264029,5.107051,-3.909260,-1.381153,-8.956131,7.152836,8.135365,-4.184664,-8.098731,6.977647,7.424719,-6.046273,-5.467503,-2.137022,7.664133,9.626790,9.193354,5.919562,4.418603,-2.197333,-7.911262,-3.157669,-6.431535,-7.799163,-1.221688,-0.173674,9.125856,-0.020311,-1.284068,3.135831,1.656072,-2.161128,-4.899816,1.743020,-7.137299,1.829772,0.604232,-1.603207,-9.813019,-4.851108,3.789449,-3.235200,4.157628,-4.246231,2.364460,7.194947,-7.941781,-5.965995,2.019947,-8.198968,8.394630,6.579823,8.537692,7.715037,-4.969110,-5.527049,-6.558543,-2.563181,1.393169,3.923296,1.890750,-0.376027,6.390651,-5.394663,-7.425212,-8.695475,-8.399404,-1.537109,6.062737,-2.637054,4.738386,1.983894,6.173854,7.227148,-2.456009,-7.797669,-8.841847,-9.112454,7.424940,-3.244300,5.166115,9.443546,-6.649783,-3.827990,5.911311,9.783063,0.117150,7.177145,9.934783,-1.963381,7.445516,9.606404,5.181553,6.402719,-7.625895,-6.156951,-3.947764,6.845851,0.743137,2.703435,-3.887757,7.301277,7.690813,2.911065,2.139742,4.826854,-2.435757,-2.379609,-6.782715,-6.828640,-9.759770,-1.587444], dtype = "float32")#candidate|1795|(216,)|const|float32
var_1796 = relay.var("var_1796", dtype = "float32", shape = (3600,))#candidate|1796|(3600,)|var|float32
call_1794 = relay.TupleGetItem(func_974_call(relay.reshape(const_1795.astype('float32'), [216,]), relay.reshape(var_1796.astype('float32'), [3600,]), relay.reshape(var_1788.astype('int8'), [5, 90]), ), 1)
call_1797 = relay.TupleGetItem(func_979_call(relay.reshape(const_1795.astype('float32'), [216,]), relay.reshape(var_1796.astype('float32'), [3600,]), relay.reshape(var_1788.astype('int8'), [5, 90]), ), 1)
bop_1798 = relay.logical_and(var_1788.astype('bool'), relay.reshape(call_1787.astype('bool'), relay.shape_of(var_1788))) # shape=(1, 450)
bop_1801 = relay.logical_and(var_1788.astype('bool'), relay.reshape(call_1789.astype('bool'), relay.shape_of(var_1788))) # shape=(1, 450)
uop_1806 = relay.erf(var_1796.astype('float64')) # shape=(3600,)
uop_1813 = relay.sin(uop_1806.astype('float64')) # shape=(3600,)
bop_1815 = relay.not_equal(uop_1813.astype('bool'), relay.reshape(uop_1806.astype('bool'), relay.shape_of(uop_1813))) # shape=(3600,)
output = relay.Tuple([bop_1783,call_1794,const_1795,bop_1798,bop_1815,])
output2 = relay.Tuple([bop_1783,call_1797,const_1795,bop_1801,bop_1815,])
func_1819 = relay.Function([var_1781,var_1788,var_1796,], output)
mod['func_1819'] = func_1819
mod = relay.transform.InferType()(mod)
var_1820 = relay.var("var_1820", dtype = "uint32", shape = (12, 5, 10))#candidate|1820|(12, 5, 10)|var|uint32
var_1821 = relay.var("var_1821", dtype = "int8", shape = (1, 450))#candidate|1821|(1, 450)|var|int8
var_1822 = relay.var("var_1822", dtype = "float32", shape = (3600,))#candidate|1822|(3600,)|var|float32
output = func_1819(var_1820,var_1821,var_1822,)
func_1823 = relay.Function([var_1820,var_1821,var_1822,], output)
mutated_mod['func_1823'] = func_1823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_753_call = mod.get_global_var('func_753')
func_755_call = mutated_mod.get_global_var('func_755')
call_1856 = func_753_call()
call_1857 = func_753_call()
func_1778_call = mod.get_global_var('func_1778')
func_1780_call = mutated_mod.get_global_var('func_1780')
call_1877 = relay.TupleGetItem(func_1778_call(), 0)
call_1878 = relay.TupleGetItem(func_1780_call(), 0)
func_1171_call = mod.get_global_var('func_1171')
func_1173_call = mutated_mod.get_global_var('func_1173')
call_1885 = relay.TupleGetItem(func_1171_call(), 1)
call_1886 = relay.TupleGetItem(func_1173_call(), 1)
output = relay.Tuple([call_1856,call_1877,call_1885,])
output2 = relay.Tuple([call_1857,call_1878,call_1886,])
func_1887 = relay.Function([], output)
mod['func_1887'] = func_1887
mod = relay.transform.InferType()(mod)
mutated_mod['func_1887'] = func_1887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1887_call = mutated_mod.get_global_var('func_1887')
call_1888 = func_1887_call()
output = call_1888
func_1889 = relay.Function([], output)
mutated_mod['func_1889'] = func_1889
mutated_mod = relay.transform.InferType()(mutated_mod)
func_753_call = mod.get_global_var('func_753')
func_755_call = mutated_mod.get_global_var('func_755')
call_1893 = func_753_call()
call_1894 = func_753_call()
func_675_call = mod.get_global_var('func_675')
func_677_call = mutated_mod.get_global_var('func_677')
call_1897 = func_675_call()
call_1898 = func_675_call()
output = relay.Tuple([call_1893,call_1897,])
output2 = relay.Tuple([call_1894,call_1898,])
func_1899 = relay.Function([], output)
mod['func_1899'] = func_1899
mod = relay.transform.InferType()(mod)
mutated_mod['func_1899'] = func_1899
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1899_call = mutated_mod.get_global_var('func_1899')
call_1900 = func_1899_call()
output = call_1900
func_1901 = relay.Function([], output)
mutated_mod['func_1901'] = func_1901
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1902 = relay.var("var_1902", dtype = "int16", shape = ())#candidate|1902|()|var|int16
var_1903 = relay.var("var_1903", dtype = "int16", shape = (12, 15, 15))#candidate|1903|(12, 15, 15)|var|int16
bop_1904 = relay.right_shift(var_1902.astype('int16'), var_1903.astype('int16')) # shape=(12, 15, 15)
output = relay.Tuple([bop_1904,])
output2 = relay.Tuple([bop_1904,])
func_1907 = relay.Function([var_1902,var_1903,], output)
mod['func_1907'] = func_1907
mod = relay.transform.InferType()(mod)
mutated_mod['func_1907'] = func_1907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1907_call = mutated_mod.get_global_var('func_1907')
var_1909 = relay.var("var_1909", dtype = "int16", shape = ())#candidate|1909|()|var|int16
var_1910 = relay.var("var_1910", dtype = "int16", shape = (12, 15, 15))#candidate|1910|(12, 15, 15)|var|int16
call_1908 = func_1907_call(var_1909,var_1910,)
output = call_1908
func_1911 = relay.Function([var_1909,var_1910,], output)
mutated_mod['func_1911'] = func_1911
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1931 = relay.var("var_1931", dtype = "float64", shape = (15, 6, 10))#candidate|1931|(15, 6, 10)|var|float64
uop_1932 = relay.sin(var_1931.astype('float64')) # shape=(15, 6, 10)
func_1907_call = mod.get_global_var('func_1907')
func_1911_call = mutated_mod.get_global_var('func_1911')
var_1950 = relay.var("var_1950", dtype = "int16", shape = ())#candidate|1950|()|var|int16
var_1951 = relay.var("var_1951", dtype = "int16", shape = (2700,))#candidate|1951|(2700,)|var|int16
call_1949 = relay.TupleGetItem(func_1907_call(relay.reshape(var_1950.astype('int16'), []), relay.reshape(var_1951.astype('int16'), [12, 15, 15]), ), 0)
call_1952 = relay.TupleGetItem(func_1911_call(relay.reshape(var_1950.astype('int16'), []), relay.reshape(var_1951.astype('int16'), [12, 15, 15]), ), 0)
output = relay.Tuple([uop_1932,call_1949,var_1950,var_1951,])
output2 = relay.Tuple([uop_1932,call_1952,var_1950,var_1951,])
func_1971 = relay.Function([var_1931,var_1950,var_1951,], output)
mod['func_1971'] = func_1971
mod = relay.transform.InferType()(mod)
mutated_mod['func_1971'] = func_1971
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1971_call = mutated_mod.get_global_var('func_1971')
var_1973 = relay.var("var_1973", dtype = "float64", shape = (15, 6, 10))#candidate|1973|(15, 6, 10)|var|float64
var_1974 = relay.var("var_1974", dtype = "int16", shape = ())#candidate|1974|()|var|int16
var_1975 = relay.var("var_1975", dtype = "int16", shape = (2700,))#candidate|1975|(2700,)|var|int16
call_1972 = func_1971_call(var_1973,var_1974,var_1975,)
output = call_1972
func_1976 = relay.Function([var_1973,var_1974,var_1975,], output)
mutated_mod['func_1976'] = func_1976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1190_call = mod.get_global_var('func_1190')
func_1191_call = mutated_mod.get_global_var('func_1191')
call_1987 = func_1190_call()
call_1988 = func_1190_call()
var_1994 = relay.var("var_1994", dtype = "float32", shape = (2, 7, 15))#candidate|1994|(2, 7, 15)|var|float32
bop_1995 = relay.floor_mod(call_1987.astype('float32'), var_1994.astype('float32')) # shape=(2, 7, 15)
bop_1998 = relay.floor_mod(call_1988.astype('float32'), var_1994.astype('float32')) # shape=(2, 7, 15)
uop_1999 = relay.sinh(var_1994.astype('float32')) # shape=(2, 7, 15)
output = relay.Tuple([bop_1995,uop_1999,])
output2 = relay.Tuple([bop_1998,uop_1999,])
func_2011 = relay.Function([var_1994,], output)
mod['func_2011'] = func_2011
mod = relay.transform.InferType()(mod)
mutated_mod['func_2011'] = func_2011
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2012 = relay.var("var_2012", dtype = "float32", shape = (2, 7, 15))#candidate|2012|(2, 7, 15)|var|float32
func_2011_call = mutated_mod.get_global_var('func_2011')
call_2013 = func_2011_call(var_2012)
output = call_2013
func_2014 = relay.Function([var_2012], output)
mutated_mod['func_2014'] = func_2014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1264_call = mod.get_global_var('func_1264')
func_1265_call = mutated_mod.get_global_var('func_1265')
call_2042 = relay.TupleGetItem(func_1264_call(), 1)
call_2043 = relay.TupleGetItem(func_1265_call(), 1)
func_1628_call = mod.get_global_var('func_1628')
func_1633_call = mutated_mod.get_global_var('func_1633')
var_2052 = relay.var("var_2052", dtype = "float32", shape = (216,))#candidate|2052|(216,)|var|float32
var_2053 = relay.var("var_2053", dtype = "float32", shape = (10, 360))#candidate|2053|(10, 360)|var|float32
var_2054 = relay.var("var_2054", dtype = "int8", shape = (5, 90))#candidate|2054|(5, 90)|var|int8
call_2051 = relay.TupleGetItem(func_1628_call(relay.reshape(var_2052.astype('float32'), [216,]), relay.reshape(var_2053.astype('float32'), [3600,]), relay.reshape(var_2054.astype('int8'), [450,]), ), 1)
call_2055 = relay.TupleGetItem(func_1633_call(relay.reshape(var_2052.astype('float32'), [216,]), relay.reshape(var_2053.astype('float32'), [3600,]), relay.reshape(var_2054.astype('int8'), [450,]), ), 1)
output = relay.Tuple([call_2042,call_2051,var_2052,var_2053,var_2054,])
output2 = relay.Tuple([call_2043,call_2055,var_2052,var_2053,var_2054,])
func_2056 = relay.Function([var_2052,var_2053,var_2054,], output)
mod['func_2056'] = func_2056
mod = relay.transform.InferType()(mod)
mutated_mod['func_2056'] = func_2056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2056_call = mutated_mod.get_global_var('func_2056')
var_2058 = relay.var("var_2058", dtype = "float32", shape = (216,))#candidate|2058|(216,)|var|float32
var_2059 = relay.var("var_2059", dtype = "float32", shape = (10, 360))#candidate|2059|(10, 360)|var|float32
var_2060 = relay.var("var_2060", dtype = "int8", shape = (5, 90))#candidate|2060|(5, 90)|var|int8
call_2057 = func_2056_call(var_2058,var_2059,var_2060,)
output = call_2057
func_2061 = relay.Function([var_2058,var_2059,var_2060,], output)
mutated_mod['func_2061'] = func_2061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1171_call = mod.get_global_var('func_1171')
func_1173_call = mutated_mod.get_global_var('func_1173')
call_2071 = relay.TupleGetItem(func_1171_call(), 1)
call_2072 = relay.TupleGetItem(func_1173_call(), 1)
output = relay.Tuple([call_2071,])
output2 = relay.Tuple([call_2072,])
func_2077 = relay.Function([], output)
mod['func_2077'] = func_2077
mod = relay.transform.InferType()(mod)
mutated_mod['func_2077'] = func_2077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2077_call = mutated_mod.get_global_var('func_2077')
call_2078 = func_2077_call()
output = call_2078
func_2079 = relay.Function([], output)
mutated_mod['func_2079'] = func_2079
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1384_call = mod.get_global_var('func_1384')
func_1386_call = mutated_mod.get_global_var('func_1386')
call_2098 = relay.TupleGetItem(func_1384_call(), 1)
call_2099 = relay.TupleGetItem(func_1386_call(), 1)
func_150_call = mod.get_global_var('func_150')
func_154_call = mutated_mod.get_global_var('func_154')
var_2103 = relay.var("var_2103", dtype = "float32", shape = (225,))#candidate|2103|(225,)|var|float32
const_2104 = relay.const([-2.681406,4.863077,-5.477080,-1.012833,7.575492,-9.541395,8.150898,8.497204,-8.127962,-4.307174,-6.039726,-9.294473,-7.454225,7.697223,1.944280,7.523090,6.572846,2.694716,4.434151,6.887257,3.222806,-6.034154,1.576789,-0.096641,6.027960,4.860112,-0.404688,-4.855155,2.043938,-9.472077,-9.709402,-3.229149,-1.458437,2.927122,4.097513,0.563379,-7.602723,-6.375683,0.821525,8.913410,9.649302,-3.186100,-3.578612,8.731760,-0.211558,8.363402,0.259304,-3.232058,7.324137,-7.292781,9.206370,5.239155,9.943332,7.416296,-8.848776,2.359531,5.793673,9.187913,4.131534,9.389975,-4.482988,-5.447478,-8.116315,-2.292783,5.544133,-5.645064,-4.101983,-4.639338,3.070259,-5.733890,6.148722,-7.449696,1.681729,-4.377758,-2.205613,-8.538357,-2.333646,-4.914348,-7.763257,5.830268,6.614479,-2.712040,9.857598,0.588799,-5.511686,5.644678,-4.386773,-4.230402,9.519388,-6.010794,-5.740929,2.482732,9.924641,7.818238,-8.745328,3.735819,-5.376973,8.008263,9.688371,8.239112,-1.509586,8.625816,-0.944663,-5.272222,-5.142545,7.968927,5.470206,-3.996815,-8.296590,-4.492777,-1.607666,5.262985,3.769564,-0.917664,0.837715,-1.962108,-2.028044,-3.759888,6.993988,6.864845,7.161599,-5.842807,2.542209,-2.657823,-6.984754,-1.461947,-3.804280,-6.829040,-2.148641,-7.607107,-4.509983,9.532475,-0.522022,5.021912,-2.325471,-6.441663,4.652005,-5.544885,3.314998,-3.513375,-5.247925,-6.758918,-2.184137,-1.719516,4.609693,5.111701,-9.570675,1.365515,-2.320526,-7.809176,9.152955,9.969251,-4.790606,1.461492,-1.001201,7.969121,-3.167982,4.006531,-3.449730,5.108774,3.960844,3.871739,4.237429,-2.042626,3.045889,-5.441198,0.848847,1.147076,9.141831,9.096092,1.281550,-6.659339,-4.426132,-6.970318,-2.766080,2.845690,-4.768412,0.378951,0.254467,-4.745514,-7.513993,1.000634,-6.627472,6.382030,8.627454,9.921461,-4.332413,-4.736451,0.528319,3.061816,-1.023773,7.323785,-3.334040,-2.654545,1.831031,-9.021157,8.584894,6.741568,0.321128,1.506526,-1.306373,8.412508,6.563688,5.014903,-5.188005,-8.740606,8.945759,-9.956723,-1.776295,1.040794,9.318476,8.039686,5.045319,-8.391607,-8.239103,3.551623,-2.426434,7.548124,-8.739217,-0.589820,9.503779,1.567306,6.220182,-6.619190,-7.857959,1.114716,-2.477572,-2.964091,2.595207,-1.858428,8.629010,-9.107648,-5.822326,1.136608,4.696074,8.088275,-5.536727,9.380341,-7.459961,3.285042,-3.535680,-1.586160,8.257020,-6.442133,1.703823,-0.478352,6.180394,-4.811735,-7.974252,-1.203435,-7.660332,6.741789,6.125187,-6.818690,-4.243344,-2.882558,-7.164268,2.418395,-4.712410,-5.448478,-8.613138,-6.843355,-0.382381,6.663192,-4.599883,-8.514297,-8.253637,8.498393,-8.156967,8.869142,3.978743,7.665922,3.835746,6.800534,7.406435,2.806614,6.902081,1.585939,5.588247,-3.970911,-1.547814,-5.975276,-6.495312,-4.454070,4.142059,-6.423996,-0.729643,-2.401454,-6.357673,0.344305,9.891154,-0.895931,-9.289828,-8.412290,-4.885119,7.158817,9.534892,1.671789,2.689027,0.006254,-9.950327,5.411077,9.150665,-7.495581,6.014593,8.141337,-3.384317,3.369442,5.639511,-0.121007,1.018604,0.069197,7.915594,-9.780215,-4.014593,4.096879,1.633505,9.647734,-6.171707,6.365415,5.931871,8.596201,-1.554018,-0.419507,-9.574022,8.413242,-5.242166,2.809785,-5.570711,-7.105985,8.379381,0.964077,-5.418147,0.939501,-9.315166,0.725517,-0.693981,9.535667,6.068094,-6.075697,4.368636,8.527886,-1.608344,7.704824,4.515081,-6.265723,-8.787841,2.237012,-1.389936,4.604539,4.647088,5.435571,5.147134,-8.969598,-7.491560,4.665775,8.895700,-4.722954,7.298632,-3.080106,2.550632,8.015788,-3.357658,0.317409,6.030106,0.228124,1.991116,-7.957090,4.910202,1.800024,-8.863522,3.303268,-5.876704,7.855218,-9.906697,-6.840446,-8.765423,4.967908,-5.763662,-8.578187,8.327314,6.588608,-3.799181,-8.119599,-3.157980,1.971232,-8.634763,-7.316449,-7.632885,-2.652134,7.746775,2.100018,-7.299963,-5.911236,4.025198,-8.208395,-2.748229,3.144145,-0.108621,0.639988,3.041871,4.789398,8.482758,-2.302794,0.451054,-3.051689,6.831680,9.165410,-2.569213,1.641026,-4.806221,7.007589,4.244440,3.183965,-5.558799,-9.300773,8.855764,4.434152,-2.236373,0.152587,-5.792430,-5.568777,9.267728,4.685594,-3.476631,5.774372,-0.119332,5.881856,0.997873,9.769400,7.641362,7.192976,7.920760,-3.050382,3.424441,-8.058867,9.399111,4.556762,-6.141832,2.545564,0.337347,4.333605,5.407195,0.939405,9.655135,-1.719943,0.101144,7.276724,-9.799894,-6.466936,5.437543,7.557987,8.544006,3.327289,4.463621,-3.916515,1.129950,-5.001117,8.987511,2.143908,5.946355,9.221866,-6.873948,2.172736,-7.048096,-2.336880,-3.708565,0.717932,-6.534102,3.758210,2.616997,6.511742,5.808216,5.746665,3.411230,9.057243,-2.218696,2.473578,-7.454295,1.560342,-1.006225,-9.704667,8.955331,1.211324,2.238575,5.533342,-1.177748,4.614395,-5.375014,-1.022457,-0.349267,-8.281667,2.646290,2.427641,1.981883,-6.249120,-1.580733,-1.037529,-6.041400,2.321501,3.896027,-6.048429,6.014213,7.196771,-4.274714,-3.921423,-7.938885,3.439174,-9.550412,0.029648,6.344481,-2.010054,-7.778425,7.254760,-9.793825,-9.152861,2.692565,6.804429,3.599078,0.404389,1.435128,-0.952423,-5.968040,2.528313,-9.218640,-8.138491,-6.001507,2.151454,-4.194199,-9.014810,8.839410,-8.118738,7.749360,-9.696346,-8.651498,0.829447,6.540311,4.265640,7.054859,-3.895341,1.643806,-1.956430,8.187286,1.855741,-5.715195,-2.108982,-4.421105,8.753441,5.319403,-9.204566,8.795483,2.711711,1.857135,-0.473763,6.364848,-5.409501,-7.621853,-3.691083,-9.577980,3.691384,2.675409,8.700545,-9.146554,-4.666615,-9.766422,0.342669,-2.109252,-7.964467,-2.738155,-5.995940,3.248916,-2.505628,9.887987,-1.145683,-7.972813,9.048004,0.676365,-5.612922,9.237907,7.728678,4.793218,0.428699,3.584195,-9.906111,-0.957080,5.172573,9.387760,2.468636,3.808108,5.823596,4.905179,3.933354,6.154038,-4.120257,-0.497564,-6.939808,2.014379,6.103629,3.874825,-6.290018,6.361910,4.591486,8.397241,0.272223,-5.352319,2.865767,9.802270,0.185919,-3.698980,2.853658,9.109397,-3.236668,6.315397,-8.220167,3.769406,3.613475,-8.354063,-0.783354,2.114703,-2.619016,-4.107543,-7.342724,5.383909,-2.227849,7.559074,-1.430479,6.457934,0.060834,3.454981,4.321064,-8.207451,5.900377,5.836685,1.380089,0.166772,2.276546,1.504980,-4.914395,2.728970,-5.304262,-1.235859,0.355085,3.285727,4.447482,-4.662086,-5.056889,1.628682,-1.419040,2.884971,6.427173,4.514695,-4.540099,-4.433386,6.885809,2.421963,5.810729,8.948242,3.403378,2.991780,1.403561,0.410244,9.840996,0.253387,6.315081,7.970217,4.899675,1.908833,7.583030,-8.301901,0.284107,-7.347662,-4.855922,-9.065342,-0.512647,-2.209339,7.510551,6.701846,-7.334542,-0.273855,3.471999,-8.538183,1.081320,-5.270898,-3.525212,5.397426,-3.409908,-7.514320,5.859504,-5.617174,-2.529005,9.374431,-9.316184,-1.298422,6.202722,2.774481,-1.793636,-7.669337,2.902758,-3.984605,4.623409,-1.589746,2.007001,-1.547586,8.410429,8.697529,1.993992,6.898993,7.824150,-0.932677,8.460480,-8.187298,-6.480303,7.849136,7.140537,3.402806,2.819327,7.859696,-8.772860,-6.469562,-2.252424,2.154986,-1.149239,-2.096802,8.479805,0.177777,-6.320522,-8.950206,-9.561591,-9.009635,-8.468734,-0.200134,2.984637,-2.066951,-1.841441,1.560047,-9.072263,-5.059916,-9.116519,7.123913,-5.573901,-1.590906,-0.858280,7.469362,-3.791612,-2.546819,1.138535,-5.405420,-9.274992,-0.279588,1.230099,-0.555071,-8.721145,3.113958,8.342992,-2.171252,1.116692,-2.907639,-4.232436,-7.379942,5.248383,9.057285,4.696371,-8.267935,-5.997313,-5.710624,-4.897592,-2.645374,-2.712965,6.615496,-7.032067,5.361205,-1.765737,3.116045,3.923168,8.668220,-3.091254,4.616042,8.734378,-4.191856,-7.088731,8.408296,5.447861,8.059409,5.029526,5.298837,3.598519,9.647301,-9.556945,-2.634722,-0.384252,-1.267693,-6.422670,9.069895,2.991673,1.297592,-2.643025,0.406261,-5.644634,8.273872,4.319612,9.362038,8.342465,7.043205,0.898613,0.298956,7.698646,9.733793,6.036358,2.529179,-0.261723,-0.230377,-9.583864,-7.506183,1.414225,-9.327745,-0.259508,9.649650,7.904732,8.169007,-0.624214,-1.385665,-3.085398,5.688972,-0.707564,3.406095,3.915513,-3.826885,6.688506,9.674174,-4.930196,8.845530,2.421422,0.593700,5.950514,-3.635984,1.838886,-5.960466,-7.848983,-8.763693,-9.781215,7.999177,7.543207,9.876198,-0.518737,5.119388,7.963366,7.488971,3.855368,9.870544,6.037820,-0.380953,-9.822874,-1.857799,-6.667228,-6.041356,-9.664378,6.739510,0.944828,-3.323584,8.423237,-9.762176,1.795206,7.483630,-1.380422,0.008269,-1.726189,7.586937,-7.721055,9.615576,-9.410298,-7.324461,8.404505,-5.972857,-8.517488,-2.976221,9.676501,-8.368122,-5.375754,3.207838,-6.252897,-4.930607,9.876298,-0.082303,-3.301780,-5.276003,5.561719,8.810419,-9.939106,8.687895,7.120069,-6.652366,-2.646882,1.651694,6.114363,-1.994561,5.899783,-1.347735,-7.611997,7.406081,6.113542,7.725929,-0.627723,7.698386,-7.492219,7.131305,5.713846,-9.207932,2.962652,-8.202935,9.491766,-8.389618,-8.204152,1.097044,2.287643,7.164719,-3.004912,2.120030,2.082361,-5.471491,3.032884,4.873355,9.050898,5.090178,0.031247,1.107532,-6.695903,-2.440280,9.078686,0.020976,-6.777109,2.193471,6.734552,6.540722,8.217841,-0.664226,3.755232,8.449033,-9.937617,6.720895,6.998976,-4.360903,9.560268,-9.094720,-3.935381,8.390954,-9.714832,7.339493,-4.965005,-4.426015,-0.332305,-8.366894,4.868447,2.808449,-4.527561,2.400027,8.584892,4.056528,-7.493525,5.160895,0.319601,6.387975,4.898516,5.383584,7.743920,-0.024287,8.024058,-1.084582,-2.660229,-7.207900,-0.254242,-9.167690,0.055855,-7.361240,1.299705,-6.029245,9.330790,-9.360255,-3.523767,-5.657133,-8.021904,-0.361344,8.390716,-7.682949,-2.647270,5.185427,-5.481979,-6.442813,1.827502,-0.027157,6.714853,-9.959731,-4.049351,5.225059,-3.899761,6.924260,-5.478281,-5.884719,-7.814075,-7.887160,8.255576,4.408829,1.927511,6.025697,2.183551,-7.543436,-0.982171,3.239149,6.314506,-1.879280,-3.604053,-5.242719,8.683190,-4.593604,4.068556,-1.784196,-9.301946,5.674915,1.886562,0.521639,-0.698657,1.081582,-5.487510,5.901382,-7.589862,3.655860,9.844076,1.588635,6.801737,-5.438862,-0.435496,3.923046,9.354126,0.933013,-0.358694,6.711391,-6.293301,8.124955,3.118732,-0.691486,-7.052986,-4.368458,-6.615770,-9.723084,3.922848,-6.665863,8.436092,5.715168,-8.699382,-2.629357,3.277739,2.549453,-2.267093,-4.741745,-9.316652,0.056750,-2.989776,-4.244709,-2.719346,-7.917222,-5.466598,2.379081,8.239175,-6.802281,4.658192,-1.120007,-5.820150,-7.637593,-4.444131,-4.733021,-5.132185,-0.473746,5.074533,5.029447,9.136805,3.718685,-8.263731,-0.174640,7.442490,-4.839061,3.429889,7.859914,-9.570847,-3.553260,-5.636143,2.833781,8.917312,-0.723317,9.305569,-1.090424,2.315774,-3.919901,-6.558318,3.145603,8.670802,4.015162,-0.175883,-3.712732,-6.980616,-2.859045,8.638475,1.005473,2.375065,6.247094,5.664690,7.635294,7.712442,4.437496,-4.983412,-1.912138,-8.924279,-8.899987,-5.194341,1.526814,-4.287695,-7.965541,-7.473999,-5.338487,9.247992,-0.927200,7.436608,4.396235,4.418130,-0.510585,-4.091985,2.322226,-9.658242,0.973411,-1.723771,-9.512861,-1.600455,-8.977868,-1.922784,-5.805663,-4.711351,1.575723,8.696744,-6.567881,3.309788,-4.027504,6.486306,-3.815374,-2.360070,4.623142,-6.391415,6.230596,-1.487121,8.655965,-8.246466,-1.874382,-6.324218,-5.667412,-4.481101,-9.629728,2.499262,3.287265,-2.251458,7.313116,-2.837550,0.206676,-8.253862,1.486383,-9.539255,3.049781,1.665138,3.538340,0.422515,1.059559,4.191262,2.546073,-5.382492,5.304246,-2.737793,2.381238,4.077829,-6.147048,0.157001,-3.459248,-8.524806,-2.856910,6.714220,-4.061981,0.297835,8.831111,9.215140,-2.010590,4.575345,3.233134,-3.099164,-6.899139,3.196200,2.032272,9.479925,0.132871,1.533502,3.430320,8.236421,-5.774008,3.264648,6.279424,-3.100097,-2.149496,-8.333214,-8.939375,6.277002,-2.553005,4.700912,6.013407,-3.943612,-7.048956,1.923444,-9.055896,3.653303,7.611728,-6.321954,-7.743063,-7.469085,0.451273,-8.449848,5.874803,-6.049502,-5.652059,7.792736,-3.622976,-2.068833,-4.437815,-5.394105,9.135708,3.215257,-0.269823,7.801439,-9.252995,-0.842249,-1.139296,3.911872,-6.712997,-5.650831,0.826479,-9.075457,1.101869,0.075854,-5.283291,-1.946022,0.512730,4.869484,-0.714850,-1.601326,-8.295769,-1.364554,8.137852,3.089761,7.043268,0.255775,4.090979,8.289541,-0.997240,-5.841522,-1.284595,-8.188204,-9.160737,-4.443960,7.945401,-7.230358,2.205691,-9.904595,-2.760586,-3.809186,2.375599,8.265495,2.206253,4.050016,7.724293,4.001529,2.970446,4.306455,2.257777,-5.213145,4.369103,-5.703247,8.640460,3.755960,-6.685738,2.898760,7.531183,3.741404,6.917921,2.666994,-4.533742,2.393597,-2.637759,-2.313166,-9.024609,-0.680198,0.891422,-9.510595,-2.957513,-5.365391,2.215388,-3.225969,-2.455022,6.293710,2.219747,-1.683153,3.759967,7.980494,6.677792,9.462330,-3.137061,8.522398,9.395640,-4.165368,1.988725,-9.597977,-9.625752,-2.183994,-4.680416,6.922474,-3.240393,-6.082321,5.987103,8.331566,1.679793,-2.656780,5.346097,8.183324,3.974533,-1.889705,-5.041254,6.441328,4.667614,-5.453127,3.580748,3.299719,6.178158,-9.965139,8.123817,7.441145,-9.463172,-1.616584,8.511289,-5.814716,9.511141,-3.666011,-9.868808,7.611464,1.862802,2.551124,7.825427,-5.944233,-3.691835,7.005898,-6.305448,-3.585383,-8.053047,-0.577615,-9.448361,-9.996898,8.529986,-5.943779,-2.000273,-8.972810,1.872918,-4.924633,-5.381024,3.463676,4.040437,9.464639,-2.173032,4.380573,-0.738904,-2.608199,-1.201068,9.801704,6.827355,7.765760,9.413208,4.479796,-4.796707,5.919929,-8.281030,4.346208,6.666627,-4.047504,3.404445,-3.316191,3.832094,-1.371348,8.170486,-8.194581,2.149839,-0.796523,4.472826,4.457714,7.926381,-4.143876,-7.619683,-1.951878,-3.244470,3.665499,-2.057522,-9.056064,-4.088278,7.328305,-0.827896,8.511813,-0.253030,-3.125623,0.649484,0.083428,-3.997044,4.282290,3.530293,-5.098320,-0.221257,6.573939,8.195953,-3.842267,2.454677,2.688577,8.762981,5.180314,-2.116071,6.497731,-3.404516,-3.967790,3.890713,3.925480,5.222319,-5.241475,6.923597,-5.160014,2.752810,-6.279417,0.885637,-6.370156,-4.846853,-9.296162,0.824588,2.792386,-8.584467,-3.208966,6.333322,-5.285618,5.061334,-0.759192,8.663124,8.836924,0.421514,0.207314,7.944572,-7.479506,7.292570,-1.702803,-1.244208,-3.773110,-4.960349,-2.918646,-7.332099,-1.731266,-4.597176,-9.636567,-7.387637,-7.160024,-3.769465,-3.483239,-7.850716,6.502721,7.091496,-7.284918,3.982165,-5.191015,-3.577641,8.975275,4.687799,-6.806524,-5.632324,3.997314,7.786807,6.541557,1.793409,6.771760,-1.640477,-9.839944,8.871334,2.164675,7.151033,-8.336606,0.791654,6.683813,8.477239,-3.231366,-6.260510,-1.654180,2.099022,7.722163,5.321802,-7.646297,-7.732064,6.669294,-9.820659,-1.549140,-4.413466,3.135910,8.090030,5.936441,-7.189713,-8.706499,9.393679,-8.478806,-4.303738,-5.615132,3.618794,3.109353,7.252193,5.967498,-4.746305,4.426705,-5.302235,-9.998989,3.744246,-6.228823,2.362190,7.141080,-5.135789,1.059257,3.186468,-7.597196,2.499912,-7.505429,7.971881,-1.520516,-5.506097,-7.986993,-6.640923,-9.528148,-1.091404,7.258567,3.450556,0.657123,0.354015,8.587216,-3.468139,3.323949,1.443245,-5.983637,8.087491,-5.884843,-0.164235,-7.588669,1.790334,8.304560,7.821753,3.278638,8.095013,-1.653370,-1.186145,2.409682,-2.884412,-5.564986,2.864173,-5.031937,8.743867,-6.323291,5.999846,-0.141142,3.611125,1.803739,-5.965904,5.708343,1.511162,-9.995213,1.745341,-1.460978,-0.008131,-3.268539,4.574378,-1.204323,2.194013,-9.884733,0.162551,-8.300318,-7.905741,-8.903301,-5.571276,-6.351553,2.288262,6.738882,8.799256,-3.458367,-6.583583,7.403839,7.899833,-5.002704,-3.003107,-5.350785,1.380260,-0.124580,-5.243204,0.661139,-0.015195,-5.259817,-0.660463,7.075088,5.453895,-5.234314,-7.811871,5.100024,2.315989,-7.319701,-8.586679,-2.802014,1.350528,-4.853057,7.271545,0.243224,5.085909,4.064332,5.179799,6.468152,8.089141,1.225632,5.313238,6.124575,-9.787809,-5.602476,-7.830021,5.285832,7.912123,8.213165,5.552216,8.446260,-1.131968,-2.864272,4.921639,-5.586940,2.356928,-1.439545,-0.872773,-0.714558,6.396508,-4.994562,9.694132,-2.088475,9.057576,0.206201,-1.251106,7.950758,0.461199,-6.514966,-8.775526,7.259530,-5.053161,-2.798710,-3.255460,-0.705118,-7.207914,4.836425,-3.781915,-4.050607,-0.794030,-6.282670,-6.296941,5.506712,0.104627,-3.429018,3.316601,-9.322474,7.156249,-4.435275,9.935680,-4.294800,7.763582,7.611719,7.397990,1.646862,3.887336,-4.694545,-3.041196,0.835697,2.851366,2.154686,-8.143758,8.669449,-4.832192,8.733397,-6.915596,9.043357,3.683930,1.300946,1.394533,-3.293816,-7.029558,-2.327784,4.405836,-7.208897,-2.315981,3.557604,9.195334,-7.683999,-0.510297,5.093361,5.902928,7.791419,3.598646,0.275090,7.429665,6.856439,-3.313311,-5.481144,-2.012283,2.466113,-5.834864,5.150222,5.432033,-5.146703,9.759998,-4.382493,-1.160233,7.192021,-3.449528,-1.089018,1.842123,0.005207,-7.080338,3.409032,-6.054916,5.766246,0.342697,1.294202,-7.287202,-1.442720,6.797737,3.353303,-9.447244,-3.329580,8.353231,1.507848,-8.927002,7.025156,-7.278938,5.241607,6.029585,-8.487574,0.080360,2.858942,5.628577,0.697093,-7.732168,-4.959288,-0.955380,8.572500,-2.069568,-5.883076,8.011443,8.469201,-0.895354,-0.066584,4.398617,-2.757136,-8.296586,-5.847173,3.792730,0.432047,-6.580679,5.907338,-2.768647,0.828785,5.783696,3.987072,9.729659,-8.898736,-2.991051,6.733027,3.298746,-9.660418,9.632078,5.390820,1.240699,-1.372022,3.786254,-3.013713,-6.508713,-3.831696,6.061704,-5.059294,-0.107505,-5.463989,3.225927,-9.762622,8.324617,1.669927,9.811911,0.789052,7.416004,8.774356,4.012044,-4.191968,2.227082,7.927671,-4.803936,2.235700,3.320299,6.710156,0.289843,1.170174,9.461941,1.404877,-5.669189,9.897382,-1.698989,-4.787086,-4.861645,9.571201,7.668461,-6.689330,-2.331274,-0.467745,4.268156,-9.755133,4.367588,1.856009,-8.781030,8.312431,0.644345,-7.366647,5.559721,-3.078410,1.059675,5.096829,-6.358802,2.562883,7.697065,-3.269909,2.814448,0.029075,5.583285,4.971186,8.185077,-1.693816,2.785680,-4.463743,3.704568,-4.306255,-4.999430,0.617021,7.132879,1.420888,-4.175845,1.232856,2.760028,-5.298564,3.686886,-3.739612,-6.732464,-3.422183,-8.604998,9.269751,5.051776,-0.154607,1.068899,-5.029440,-3.415518,-0.806563,-1.444816,0.249045,-0.655751,-4.478929,2.869438,5.935820,9.241380,-4.585690,-3.461454,7.861355,7.915730,-1.495575,6.456871,-9.996568,-3.783015,-0.039927,-1.626630,-8.467628,1.582975,7.448895,-2.863032,-2.295003,-1.766200,5.314891,-4.950562,-1.847907,-6.688016,9.018455,9.933608,-0.376553,-5.225244,-1.943880,-1.171245,0.906703,4.895829,-3.712517,3.342625,7.783354,8.839711,3.640522,0.707123,-2.362715,-7.454064,0.976181,3.064922,7.514197,-1.801473,-7.500276,6.079321,-2.391366,-2.386138,-6.055616,-4.643890,5.192346,-6.048970,2.884198,-6.203010,8.393134,4.274259,6.861728,-2.678146,-4.137765,-3.660059,8.431098,1.040003,5.754771,1.684128,3.045404,2.075408,1.624668,7.110041,-9.746862,-8.418010,-7.066436,-8.003151,-9.240003,8.462858,-7.957140,-0.613689,8.252777,0.778341,0.536085,-4.672575,-7.172690,-4.253327,5.034055,8.865514,0.642299,1.220218,0.501748,8.866066,1.357150,7.499405,0.710787,2.355324,7.461714,3.806113,5.837256,0.760120,6.416953,-1.725246,-1.703894,-3.840623,2.118642,6.245186,-4.626335,0.327879,9.095324,1.479171,-8.326865,5.688459,2.941428,-8.658066,-1.372627,1.478634,6.649870,-4.823489,7.231159,-2.398019,4.376306,2.198338,-5.984923,5.108187,1.586643,-6.326041,8.821126,2.042594,-4.548814,-6.220473,-8.967372,4.763024,3.899199,8.454347,-7.204503,5.032290,0.776293,4.656454,0.728508,-8.640216,9.506970,-0.392186,-4.323657,-4.515678,-4.509883,-9.994503,-9.722532,-8.412107,1.606915,-0.735384,9.560045,3.109164,-5.728021,5.319417,1.823704,8.737499,-5.026586,-6.302771,5.525496,-5.270463,8.705061,-4.935011,-7.684541,9.912802,-5.230138,5.094752,6.307699,9.030061,-3.116171,-5.732546,-5.057081,-3.303346,8.819300,9.084395,2.798061,-3.095718,-5.134325,-1.295562,-2.191174,0.472182,6.930146,-3.973199,9.232528,7.437937,-6.418486,-7.374061,8.722402,-9.797181,3.307448,5.345361,4.493781,6.564671,0.504430,-0.521487,8.977994,-5.048315,-8.058128,0.709400,-7.762835,7.952673,-1.714931,0.539615,8.465970,5.953472,-3.850816,4.544670,-7.783747,7.028314,9.560068,0.136588,5.655334,6.811382,4.993637,-6.277218,4.791667,-8.140926,7.771928,3.369004,0.944436,2.608139,-5.675404,4.991973,9.392318,-9.827024,-6.896045,9.296782,7.949133,-3.180953,8.293253,1.916348,-9.526957,9.115908,1.292880,-0.891049,7.593324,-9.566357,7.763320,-4.083517,7.670539,6.766030,3.272033,8.998437,9.048112,5.746927,-3.438468,-3.572615,-8.880502,-4.781147,-6.997331,0.228881,-3.284917,8.858536,8.009291,-3.258075,-0.222601,1.748467,-8.911967,6.117271,-5.795588,4.594139,2.952370,0.517465,3.858184,4.624966,4.161610,2.685874,4.663215,4.452538,-9.998830,6.705356,2.769889,-7.617539,8.985023,2.842101,-6.335341,6.737624,-8.858576,-0.923532,-2.107659,-5.940119,-8.689647,-2.549428,-8.349342,-2.996901,9.697041,-5.899469,-0.677402,4.838164,-6.149239,7.335471,8.455268,-7.817578,-7.908777,1.192177,-4.036235,-3.662561,9.015957,-0.850685,-3.817214,-7.269263,-3.985606,-6.678966,-4.193147,8.391724,-7.469430,5.642674,6.934691,-2.584097,-0.577316,-0.748820,4.442354,8.909410,2.056491,-0.751961,6.400625,-9.008430,3.820873,-6.362781,-6.129892,-0.816465,5.329686,-3.910299,0.973729,-2.078076,-2.035711,1.521418,4.079680,-8.659733,-6.948726,-5.388526,6.634887,-6.589929,7.279166,-3.018461,-7.607788,-5.678040,2.801466,-2.351784,9.824146,-7.827968,1.994670,0.606074,7.556966,-4.121561,6.250842,9.826559,9.569543,8.083034,-5.765147,-3.878224,9.425538,-6.726727,1.555743,2.665213,9.607786,-9.938703,2.927577,5.147017,3.744006,4.931030,-8.997668,8.288232,-8.003841,-8.800884,3.620477,5.218633,-1.012409,1.045814,-0.395973,-4.506424,-9.500641,-9.699013,2.065179,-7.522618,5.900925,6.043342,-6.840685,6.487321,3.220260,-8.188808,-1.036708,0.394965,9.850074,-2.235065,-2.015839,-6.863309,7.697051,-9.501482,-3.512328,4.732880,-0.689595,-5.306357,-5.897827,7.296415,8.994510,-0.700543,4.435026,-4.500311,-4.208406,-2.869104,-6.115954,2.951419,-1.021093,-0.429342,4.572091,-6.831751,-7.273379,-0.494709,7.359034,-1.390679,6.038256,-9.577779,2.665116,-3.575075,-5.031695,-6.443657,3.020694,-7.264096,8.004444,-6.538105,5.677881,6.425587,5.021511,-4.151162,2.033395,-2.675936,7.071236,-9.522481,0.084719,-6.572961,5.440035,-5.245648,-5.246832,-1.604370,2.227243,-4.944510,-7.064297,-7.918525,-5.018400,-6.683267,-5.195306,-8.660947,5.363755,-4.542271,0.918152,-1.690443,4.964422,5.581125,-0.478571,7.255453,8.365213,-2.918812,9.057704,3.749703,3.003401,-9.938344,-0.810845,9.370137,0.305655,9.797060,-5.134932,6.789250,-0.747069,3.918291,4.927563,2.181458,5.004958,-2.408605,-5.350234,-3.293097,1.971768,4.725791,4.274715,4.955665,-2.496763,-2.809374,4.548216,-8.446184,-8.152812,-4.153308,0.930222,-1.147905,6.230213,2.438981,5.919677,4.008649,-8.266381,-7.153484,6.251351,-0.986112,-1.791031,-1.624331,1.515471,-0.937153,-8.976190,4.755966,-4.354313,-1.212004,-0.089953,5.226568,8.364955,-3.905807,-0.107264,-8.381309,-1.545216,9.368395,4.128741,-2.719906,0.117683,-2.903274,0.876301,5.109475,-6.956153,9.882379,7.711958,-4.187594,6.317099,0.461013,2.473874,8.302269,-3.934702,3.278973,-2.886573,-7.501021,-4.335884,-1.297945,-4.208246,5.441768,0.409388,7.428306,3.339998,-6.366912,-6.997889,-5.098051,9.272899,-5.126117,2.929485,2.628728,5.740728,3.335295,-0.298033,-4.894838,1.980711,5.603725,-4.262559,8.031795,-0.119954,1.116161,9.517107,0.266829,1.366142,5.352790,2.017671,0.142457,-1.316459,-1.446833,-1.003255,-7.553788,-2.654132,-7.598751,-8.502392,-4.474468,5.696094,-7.960823,-3.281929,0.542711,4.579916,-5.188488,5.778185,4.169419,-8.796614,6.126966,-6.391934,-5.991030,5.867135,-4.185585,-6.303406,6.534588,-8.098178,8.331814,0.399982,-0.078960,9.804942,2.309660,-9.321652,-9.836587,-3.977180,8.727089,9.759001,2.704605,3.210454,5.749659,-2.478378,8.883205,-6.737824,3.981703,-2.659475,-9.829446,-7.111781,-6.238106,-2.068370,6.991507,-6.140674,-8.229038,-9.123085,7.226065,2.741549,-3.269709,3.399655,-1.965664,-7.487106,7.878941,3.950397,-5.728924,3.214090,5.193443,7.059493,-0.287957,1.262734,-8.054725,-3.520807,5.929141,-7.531394,7.005607,-9.594673,1.163049,-2.967362,0.641734,-9.240061,3.126039,-3.575979,7.340644,-6.693641,-8.454145,-6.799938,7.715864,-1.863585,-3.013332,-3.205448,-7.463415,6.931986,1.915608,-9.825952,-3.772235,-0.646947,-3.796511,-7.864477,8.694888,9.102612,-7.617129,-7.618124,-8.837369,5.716196,2.100550,-2.695105,-5.548093,5.101628,1.047064,-9.423233,-7.751934,-6.393129,8.017026,-4.118958,2.713695,-4.427497,-8.823450,9.103562,2.338620,0.748015,1.416083,-9.372735,-9.002963,6.726398,1.515131,3.221334,4.627012,-3.443159,-6.079086,1.961417,-5.924121,3.066279,-1.465755,7.902099,4.651592,-2.623938,8.347365,-2.546130,-4.969806,2.279913,8.532688,9.768833,-1.741836,-9.957634,-0.361744,-7.026749,4.483676,2.118655,1.405031,-2.579149,-2.194337,2.893039,4.733267,8.237919,9.205855,-5.633951,0.168173,5.641752,3.147713,-2.242097,5.071384,7.009696,-4.893945,-3.982659,3.386687,7.478672,7.485315,7.194793,-6.392342,-2.788837,-8.525522,4.585457,-2.135541,1.380573,-6.721513,-2.758633,0.973938,-2.725403,-1.685602,9.642581,8.164387,0.756800,0.110106,-1.162982,3.483857,1.628539,1.153069,9.496270,-9.379086,2.474847,-8.838075,-4.681439,7.679294,-0.172470,-4.289364,-6.401749,-4.350482,-9.984422,-5.283141,1.589032,-4.819946,6.935796,8.789617,2.363492,-4.208113,-4.262272,-0.962603,-1.487820,-7.368627,-2.065335,-5.947016,-0.291258,-4.906273,-3.873408,1.986378,4.706840,-6.263410,9.880075,6.331719,6.258330,-6.879348,8.065234,7.427620,-4.490339,-6.402597,-6.499807,8.972671,6.210766,7.675769,6.335956,1.549388,-7.231915,8.411480,-8.484153,6.543832,-6.097333,2.971923,-5.152309,9.621080,-0.122694,9.082176,-4.058734,-7.839796,1.495122,7.769351,-8.781692,2.039105,8.034780,2.296817,5.784895,3.327674,-4.517186,0.656568,7.452727,5.258889,-1.369384,-0.425882,-0.240311,-1.875213,4.326068,-0.768536,9.977629,-8.324797,-0.423368,-1.717239,-0.166592,-1.869136,-5.856314,-3.171827,-1.380977,-1.881025,-7.262772,-5.216479,5.051677,-5.491914,-7.537570,-0.323982,-3.531124,-8.884996,-4.948653,8.753293,4.705438,2.346427,2.463692,9.026718,-7.237293,1.650284,8.276567,4.534947,-1.799175,7.002517,-3.558289,-0.940978,-6.287352,7.129402,0.910671,-7.515333,-6.836663,8.957587,4.751482,-3.234124,-2.634231,-3.708370,1.423900,-0.214561,-9.603425,-6.080777,5.127368,3.168975,-2.116315,4.454720,8.404968,-1.692447,7.852027,-1.514426,-5.307581,-1.937445,-3.338556,-4.676971,-6.936100,0.017363,-6.578255,6.379688,6.746561,-4.785970,-5.721810,9.353636,4.928878,7.802280,9.467545,6.158465,-2.085750,-5.135654,-3.632412,-7.738587,7.034653,5.565486,-0.675971,-2.299171,-2.248139,8.076314,-4.771687,-7.034225,-5.192307,-2.957485,2.421846,9.486941,-6.497187,-5.067625,4.755906,7.326343,6.081661,-4.579110,-6.484105,6.142498,6.623435,7.345382,6.152010,2.887183,1.431647,-7.841933,1.146998,6.141992,8.318869,9.218672,-6.632911,-6.861613,0.192421,2.687527,2.562494,-6.806232,9.151955,-3.472355,-6.338508,-9.798651,7.121269,-6.716292,1.839734,-6.218863,-8.678267,0.283102,0.306021,-8.433252,-0.518109,-6.783488,-5.794484,2.223902,-0.231382,-5.424646,6.257347,-7.476398,4.750015,-0.506662,-6.035121,-6.847031,-5.860691,-4.614182,5.148802,-7.083322,-9.393296,3.358932,-3.132126,8.088647,-7.109139,0.919273,-5.186142,-1.868636,-9.193185,-7.039046,-3.845555,7.848536,-4.500002,-8.509970,-9.513088,-6.034097,5.374379,6.521507,-0.679585,-1.596205,1.226802,-0.994898,5.489995,7.556753,6.475608,4.956912,-3.378311,-3.005217,-2.417777,-5.276305,-4.380747,8.849764,-6.201928,1.552062,1.450567,8.660145,1.742152,4.245429,4.946833,-5.248058,-5.482919,-6.496452,7.093084,-2.948131,8.454189,-7.603123,2.768974,8.829719,1.022866,-0.225362,-2.176841,6.214645,4.358798,-1.393763,6.987312,-0.802213,-3.302380,1.083956,4.610881,8.522383,-6.917374,-1.489023,-7.512846,-7.505372,-2.263419,-8.710368,-2.779471,-4.105404,-4.553723,-4.785088,-3.215029,-6.507692,4.740982,-5.438893,2.323179,1.780283,3.315449,6.041830,0.559317,9.889140,-2.450425,-8.038304,4.981872,-5.670249,-5.915407,-9.412928,6.664282,3.980431,-7.242941,-2.060176,-8.296293,6.435807,4.517583,4.358535,-1.574829,1.086953,-4.619778,-2.342978,-5.427804,-4.712036,8.395577,0.826340,1.910554,-8.695044,-2.734243,5.224177,-2.769923,5.786926,3.262944,4.036649,6.712237,-2.438041,-4.331459,-3.405921,5.252797,8.278896,0.999695,-3.898561,-4.316916,-8.913724,6.051740,1.219776,-5.708934,6.403002,9.976540,-4.695906,4.832992,-1.885817,4.071429,7.080794,7.545509,7.674292,0.987810,8.505410,-2.840943,5.606059,2.972879,-3.588824,1.596842,3.365989,-6.768133,7.898343,-4.802080,6.561465,-2.541414,8.152707,-9.083781,-9.440514,-2.272880,0.671272,2.350917,-8.041605,8.582001,5.950893,-0.537680,1.401694,-9.087629,2.875979,-7.371745,-7.011656,1.802633,9.471671,-4.632128,5.085689,9.792127,-5.961358,7.507911,-3.487857,3.778104,4.875183,-2.659295,-8.014387,-4.975710,-1.224389,-7.280292,7.462054,-7.694282,2.540147,1.815551,6.093368,3.074328,6.225557,-9.712708,0.921286,3.392701,7.767833,0.771744,-0.334151,0.738850,9.722273,3.732390,0.621772,5.376998,8.591100,-6.263642,4.306528,-0.233796,-1.275699,-5.401891,-1.458386,7.304858,-7.219634,6.677109,-7.141356,2.331256,-4.448920,-5.432983,-3.712810,7.872914,-8.323113,-0.693395,1.125289,9.986576,7.159755,-1.616698,2.472693,3.133835,-0.047359,6.498558,-3.479449,-8.176023,8.575891,-4.902988,-6.781985,6.627245,0.787464,6.906644,-2.945510,8.750691,-0.923573,6.515493,9.172711,2.813992,9.460914,-4.010211,4.496596,0.425975,6.210485,-6.817270,7.577274,6.876101,8.046497,5.640292,4.972369,8.159919,-6.557939,9.762071,-9.961134,-0.810285,4.329001,0.960309,6.636832,-6.962273,-3.832587,0.534195,-2.473504,4.737663,5.145430,-2.178568,8.008618,-1.890608,-9.568916,4.805221,5.150032,2.087765,-4.255966,7.239566,5.586993,-2.883552,0.832483,6.065707,-7.839570,9.402560,8.243946,-1.605452,-3.313990,7.995072,2.632715,7.837014,-0.620539,4.916806,4.437953,-7.572506,-7.016717,-1.736178,-5.964085,-4.562875,-6.630835,-2.770739,0.286045,-6.313833,-8.045330,-7.639015,-1.525292,-4.608473,-3.257918,3.313079,-0.711970,-1.755856,4.623475,-7.152493,-6.326906,-0.718549,3.639106,3.826004,-9.996022,-1.313934,8.852435,-7.276880,-0.875356,-8.120222,-2.524344,-5.901590,9.454882,-3.262145,2.427777,0.399677,2.409294,3.179271,-5.590350,2.959304,-2.031746,3.816797,-0.677045,-2.428569,-0.175360,-6.198124,-5.364830,-0.733858,2.262471,-7.838411,4.476587,6.362100,-4.363112,3.522241,4.305916,5.906643,-2.375246,0.806653,-8.579635,3.574283,-7.035186,8.864054,-2.408444,-6.620236,-1.932402,0.581052,-3.710977,-0.117377,0.523736,-3.558066,-7.141948,-0.555012,-2.811478,-3.226509,9.717409,-9.960084,4.165345,1.823880,2.811808,8.268677,-1.460190,2.660517,1.008853,3.561071,-3.189754,5.802917,8.127345,0.097883,2.120729,-2.830949,-0.671134,-0.706988,4.387685,5.974471,-4.492323,-6.047743,0.763508,4.124587,-1.071330,4.545785,-2.837734,4.171275,8.705904,-4.580519,-3.673821,4.635078,2.596795,-5.245557,8.744374,6.787847,9.570327,3.911864,4.674793,4.430876,3.512917,-3.955307,-8.933547,-7.187374,9.071458,-5.623055,9.959246,-6.704162,-8.331418,5.130758,-0.860112,9.682994,9.281368,2.473849,2.172667,-0.953909,1.472297,0.935726,-9.049237,9.318664,-9.432713,-6.724574,-5.027961,-4.432444,1.741744,-9.704950,-5.825925,6.651301,-9.595042,-5.640372,-0.608202,7.699708,-8.979254,4.089058,-6.620900,-7.509976,-9.038137,-9.597978,5.684523,3.684451,2.779683,-2.952477,0.253397,3.567282,-4.677390,-2.025220,-1.178828,7.834575,-5.232478,8.769390,4.189776,0.090644,-4.390837,-8.300786,-9.350855,8.697662,-6.216449,6.865525,8.018454,0.573792,-3.269546,-7.049413,4.299411,9.544506,-5.865719,-3.172663,-3.316808,-5.390059,-6.135396,-3.199388,-1.386717,-0.965979,-8.144895,7.254331,-7.005031,1.159671,-1.079934,1.266864,0.400867,5.658161,5.171931,-7.561222,4.639074,8.599111,5.574381,-3.874355,4.270654,-2.015757,-3.285063,4.038633,4.179652,0.211207,8.936143,4.164785,-6.379221,-5.373666,2.767291,7.105274,9.830877,-3.200754,0.513517,9.452914,5.216400,-9.791662,3.869413,-4.060528,-3.948394,-5.407317,-5.659592,5.832831,-0.258615,-2.829002,-2.466318,-6.178088,-6.755087,-6.474151,1.366761,-4.487154,-4.599854,-4.285359,7.642399,-6.820599,-3.205226,9.434074,-7.500382,9.637243,-1.382350,-5.918577,-3.993753,7.364848,1.503080,-3.989217,4.921003,0.823998,1.079858,0.450537,-4.618271,-2.871234,-6.245209,9.414011,-5.124347,6.790384,0.054072,4.763422,-7.555305,-9.931708,4.507160,-2.731507,-6.027868,-2.509171,7.618199,-6.050007,4.773940,-4.679934,-4.088593,-8.448633,8.977828,1.240785,-2.630268,-7.552097,9.320079,-5.024516,6.489977,0.579927,3.312366,8.113172,5.511267,-7.679515,-2.962251,-5.404406,4.720208,-6.542074,-1.504029,4.705915,-3.636904,0.953304,-8.475883,-4.862074,-6.964154,9.089443,5.488912,-0.184420,-8.270055,6.043393,-3.204252,6.464257,5.442643,-9.413846,-4.754254,-4.415044,4.420651,-0.606957,4.060893,7.342966,0.136309,6.898151,2.429304,4.235671,3.596985,-1.692299,7.090989,5.609101,8.246321,-4.907413,6.311664,7.433423,5.606860,-4.478231,-2.780391,-8.261872,0.564098,6.562372,-6.873045,-7.284562,7.901772,8.135622,5.063452,1.294599,-3.982047,-5.805043,-3.095756,-7.305644,1.568688,2.558328,-1.614422,2.593777,8.428168,-8.027728,-0.829709,1.743914,7.626150,-5.184083,8.080043,-2.670774,9.605506,7.502869,-0.783833,1.079139,5.304922,9.847645,1.242186,4.837702,4.175103,-6.415913,-8.188038,-6.905638,-3.481703,-5.529176,-4.284073,2.718813,4.588589,-2.802777,-6.724069,-3.902397,-4.224521,1.433137,-6.217856,-3.483916,-7.146433,6.852759,6.725681,-0.351518,-6.597225,0.136719,1.479936,8.984426,-3.330154,-1.567886,6.622043,-1.327050,2.153252,3.540402,-9.773592,1.288489,-2.372891,7.764644,-0.967599,0.732314,2.007935,-3.258544,7.026285,1.565932,6.772464,-2.491875,-9.786544,-9.577922,-8.810789,-7.441054,1.790532,6.810218,-5.862284,9.347700,7.941483,-1.938112,-6.977999,3.199284,-2.768328,6.490034,9.114245,-4.028310,-5.569458,2.995934,1.608442,2.871133,6.284302,-9.358395,4.227496,0.626406,1.184962,1.542664,-1.247177,7.523426,-8.841237,-7.068152,5.845425,6.230704,5.414318,-4.786973,-8.260675,5.131532,3.564936,-6.786169,-5.303055,1.302675,5.458362,7.310279,9.322100,-5.586679,9.509179,9.979206,2.254600,-8.519578,3.784991,9.322750,-5.347948,-4.827812,2.037999,-5.400521,-8.251556,2.037555,5.279122,6.215156,0.970254,-8.077183,-2.791660,8.667789,-0.537935,-5.894661,7.921861,-9.648974,-3.327975,1.803044,2.719900,3.041868,3.600224,8.396617,3.047850,7.518667,-4.641501,2.395030,-8.442400,-9.706958,-7.938368,-5.036055,5.697604,1.213884,2.230562,6.291215,2.137052,-4.353364,6.030352,8.336982,-5.544556,7.736567,-5.198229,3.508339,-3.744814,1.581748,-6.827370,-6.878619,-4.361199,-5.791989,-7.346508,-6.922216,-0.534992,-4.100902,-3.875075,7.099121,-0.197318,0.922652,5.072187,1.130502,7.346475,5.480288,0.519583,6.172862], dtype = "float32")#candidate|2104|(3600,)|const|float32
call_2102 = relay.TupleGetItem(func_150_call(relay.reshape(var_2103.astype('float32'), [15, 1, 15]), relay.reshape(const_2104.astype('float32'), [15, 16, 15]), ), 0)
call_2105 = relay.TupleGetItem(func_154_call(relay.reshape(var_2103.astype('float32'), [15, 1, 15]), relay.reshape(const_2104.astype('float32'), [15, 16, 15]), ), 0)
output = relay.Tuple([call_2098,call_2102,var_2103,const_2104,])
output2 = relay.Tuple([call_2099,call_2105,var_2103,const_2104,])
func_2109 = relay.Function([var_2103,], output)
mod['func_2109'] = func_2109
mod = relay.transform.InferType()(mod)
mutated_mod['func_2109'] = func_2109
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2110 = relay.var("var_2110", dtype = "float32", shape = (225,))#candidate|2110|(225,)|var|float32
func_2109_call = mutated_mod.get_global_var('func_2109')
call_2111 = func_2109_call(var_2110)
output = call_2111
func_2112 = relay.Function([var_2110], output)
mutated_mod['func_2112'] = func_2112
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1095_call = mod.get_global_var('func_1095')
func_1097_call = mutated_mod.get_global_var('func_1097')
call_2117 = relay.TupleGetItem(func_1095_call(), 2)
call_2118 = relay.TupleGetItem(func_1097_call(), 2)
func_150_call = mod.get_global_var('func_150')
func_154_call = mutated_mod.get_global_var('func_154')
const_2145 = relay.const([3.166808,-1.161823,0.921323,-5.134254,-9.998293,3.950060,1.436143,-0.457705,-6.676344,-4.496433,9.631258,-7.865083,4.820805,6.018838,2.228120,8.379576,5.115157,-8.261102,4.339332,9.892143,-0.520816,5.944299,7.597735,1.160085,-8.406191,7.627309,2.748166,-1.619459,-8.308239,7.750965,8.581376,-1.551932,-7.083953,8.474609,9.998034,3.747509,9.768254,4.623125,-0.017462,-7.785346,0.023250,-2.525469,9.842786,2.680188,1.515651,8.261812,1.730226,7.996757,-8.882268,0.565334,8.804926,0.312694,-6.915097,8.139713,-4.407179,6.070490,6.049026,-9.615004,-7.737541,-7.531920,-6.483632,1.599607,-3.561590,3.782689,0.910008,-4.998997,-2.569810,-1.422034,6.738218,3.755254,8.154479,2.994766,2.276270,-5.211948,8.755327,9.764722,-6.729549,0.964331,9.815308,-9.442147,5.141248,1.198172,-6.166931,-5.990548,-5.737391,6.580730,-4.866218,-8.383716,-1.884302,-2.468016,-9.515550,7.777769,-0.779259,4.454590,-2.272802,-9.111038,-5.472815,8.127168,0.716790,-7.560152,1.314269,-4.743033,-6.745753,8.583050,8.368991,-4.680173,5.785381,-9.210678,-4.999941,4.788551,8.803969,0.080908,-3.594144,5.860295,-9.381545,7.537110,6.600942,-0.951832,-9.480925,9.874484,0.207649,9.573031,1.482153,-8.710732,2.589724,-8.565894,3.156112,1.915528,-7.826912,-7.321937,-5.482762,4.679475,4.611586,-8.253549,1.845905,3.918609,5.778230,-8.574623,-9.030471,3.164614,-2.364006,0.395272,4.448860,4.157161,2.635613,-3.131617,8.427904,7.724495,0.999727,5.410256,8.189906,1.393263,7.822112,-1.768197,-9.690539,-2.593473,6.953289,1.110383,-4.056791,0.098282,-2.368875,6.913288,7.979168,-5.651851,-8.351274,6.942636,-4.223346,3.271252,-2.666956,9.588452,6.571028,-8.356685,0.342449,3.911779,-7.994182,8.617324,-5.961687,0.168254,-7.827870,1.483086,6.142761,-1.260782,2.409251,6.220438,6.405898,7.643434,-8.626303,-8.254325,1.685441,3.870890,-1.671697,-5.410133,-8.163463,-3.247391,3.514931,0.655547,-7.112316,-8.603913,1.835129,-9.333372,-4.761346,5.837714,8.799491,9.849629,4.653690,-6.679185,4.564699,5.951483,-9.425930,-2.944622,8.375380,-3.280426,-6.948110,5.064537,8.227059,-4.295266,8.049707,-8.220111,0.146194,4.260101,9.104274,-4.411687,-4.233506,-1.936118,9.342003], dtype = "float32")#candidate|2145|(225,)|const|float32
var_2146 = relay.var("var_2146", dtype = "float32", shape = (100, 36))#candidate|2146|(100, 36)|var|float32
call_2144 = relay.TupleGetItem(func_150_call(relay.reshape(const_2145.astype('float32'), [15, 1, 15]), relay.reshape(var_2146.astype('float32'), [15, 16, 15]), ), 0)
call_2147 = relay.TupleGetItem(func_154_call(relay.reshape(const_2145.astype('float32'), [15, 1, 15]), relay.reshape(var_2146.astype('float32'), [15, 16, 15]), ), 0)
func_1460_call = mod.get_global_var('func_1460')
func_1462_call = mutated_mod.get_global_var('func_1462')
call_2148 = relay.TupleGetItem(func_1460_call(), 0)
call_2149 = relay.TupleGetItem(func_1462_call(), 0)
bop_2152 = relay.maximum(const_2145.astype('uint16'), call_2148.astype('uint16')) # shape=(2, 7, 225)
bop_2155 = relay.maximum(const_2145.astype('uint16'), call_2149.astype('uint16')) # shape=(2, 7, 225)
output = relay.Tuple([call_2117,call_2144,var_2146,bop_2152,])
output2 = relay.Tuple([call_2118,call_2147,var_2146,bop_2155,])
func_2162 = relay.Function([var_2146,], output)
mod['func_2162'] = func_2162
mod = relay.transform.InferType()(mod)
var_2163 = relay.var("var_2163", dtype = "float32", shape = (100, 36))#candidate|2163|(100, 36)|var|float32
output = func_2162(var_2163)
func_2164 = relay.Function([var_2163], output)
mutated_mod['func_2164'] = func_2164
mutated_mod = relay.transform.InferType()(mutated_mod)
func_753_call = mod.get_global_var('func_753')
func_755_call = mutated_mod.get_global_var('func_755')
call_2193 = func_753_call()
call_2194 = func_753_call()
func_1899_call = mod.get_global_var('func_1899')
func_1901_call = mutated_mod.get_global_var('func_1901')
call_2205 = relay.TupleGetItem(func_1899_call(), 1)
call_2206 = relay.TupleGetItem(func_1901_call(), 1)
output = relay.Tuple([call_2193,call_2205,])
output2 = relay.Tuple([call_2194,call_2206,])
func_2210 = relay.Function([], output)
mod['func_2210'] = func_2210
mod = relay.transform.InferType()(mod)
mutated_mod['func_2210'] = func_2210
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2210_call = mutated_mod.get_global_var('func_2210')
call_2211 = func_2210_call()
output = call_2211
func_2212 = relay.Function([], output)
mutated_mod['func_2212'] = func_2212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_861_call = mod.get_global_var('func_861')
func_862_call = mutated_mod.get_global_var('func_862')
call_2241 = relay.TupleGetItem(func_861_call(), 0)
call_2242 = relay.TupleGetItem(func_862_call(), 0)
output = relay.Tuple([call_2241,])
output2 = relay.Tuple([call_2242,])
func_2258 = relay.Function([], output)
mod['func_2258'] = func_2258
mod = relay.transform.InferType()(mod)
mutated_mod['func_2258'] = func_2258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2258_call = mutated_mod.get_global_var('func_2258')
call_2259 = func_2258_call()
output = call_2259
func_2260 = relay.Function([], output)
mutated_mod['func_2260'] = func_2260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1190_call = mod.get_global_var('func_1190')
func_1191_call = mutated_mod.get_global_var('func_1191')
call_2269 = func_1190_call()
call_2270 = func_1190_call()
output = relay.Tuple([call_2269,])
output2 = relay.Tuple([call_2270,])
func_2272 = relay.Function([], output)
mod['func_2272'] = func_2272
mod = relay.transform.InferType()(mod)
mutated_mod['func_2272'] = func_2272
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2272_call = mutated_mod.get_global_var('func_2272')
call_2273 = func_2272_call()
output = call_2273
func_2274 = relay.Function([], output)
mutated_mod['func_2274'] = func_2274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1171_call = mod.get_global_var('func_1171')
func_1173_call = mutated_mod.get_global_var('func_1173')
call_2322 = relay.TupleGetItem(func_1171_call(), 1)
call_2323 = relay.TupleGetItem(func_1173_call(), 1)
func_1489_call = mod.get_global_var('func_1489')
func_1490_call = mutated_mod.get_global_var('func_1490')
call_2334 = relay.TupleGetItem(func_1489_call(), 0)
call_2335 = relay.TupleGetItem(func_1490_call(), 0)
func_2210_call = mod.get_global_var('func_2210')
func_2212_call = mutated_mod.get_global_var('func_2212')
call_2336 = relay.TupleGetItem(func_2210_call(), 1)
call_2337 = relay.TupleGetItem(func_2212_call(), 1)
bop_2340 = relay.right_shift(call_2334.astype('int64'), relay.reshape(call_2336.astype('int64'), relay.shape_of(call_2334))) # shape=(2, 7, 1)
bop_2343 = relay.right_shift(call_2335.astype('int64'), relay.reshape(call_2337.astype('int64'), relay.shape_of(call_2335))) # shape=(2, 7, 1)
uop_2344 = relay.sigmoid(call_2334.astype('float64')) # shape=(2, 7, 1)
uop_2346 = relay.sigmoid(call_2335.astype('float64')) # shape=(2, 7, 1)
func_650_call = mod.get_global_var('func_650')
func_655_call = mutated_mod.get_global_var('func_655')
const_2368 = relay.const([-9.173242,-1.057621,-5.714305,-6.446110,2.413053,-1.051282,-5.932358,-2.331614,7.718889,6.292142,-2.953048,3.839592,4.033052,-2.064836,-3.936285,-0.223049,-1.610726,4.382144,0.419149,0.152257,5.499999,4.145305,3.027334,-1.039965,-8.417597,1.065009,-6.957266,4.364350,-8.804899,7.656610,3.536393,-1.898958,-6.941522,-0.410759,2.721459,-5.293190,-8.897425,-5.509705,2.716644,-4.560144,9.980974,-7.247095,-6.013228,8.829975,6.401063,6.740123,-4.258354,2.533103,9.021278,1.584295,7.060055,8.668937,0.926984,1.675430,-6.571133,8.329922,-5.838415,-0.867980,2.247342,3.868958,-5.568128,-0.239914,-0.468011,4.226313,7.185920,0.151547,-4.151175,-7.085237,-0.827792,-9.221437,4.919681,-9.991292,3.884240,-8.144131,8.163176,0.499022,-5.567916,-1.309879,0.247563,9.057805,-5.415400,9.137992,6.085384,1.805319,-9.496402,3.283873,5.582098,9.299021,-5.757826,8.344355,6.123849,6.589341,-4.984992,9.930574,9.815968,7.933216,3.509264,-6.762235,-4.904391,-4.576403,9.287012,4.140789,-9.047966,9.773434,-2.885156,-6.447415,9.749382,-9.010776,0.594270,-5.404960,-1.557268,7.134910,-4.026791,-4.087458,2.668125,7.323797,-7.725007,4.878824,7.749576,4.944230,7.970104,-2.066894,6.699348,1.838389,-3.507514,3.085359,6.104036,-3.294401,-2.930304,-5.066255,8.107818,-6.149272,-0.683388,-5.383781,-6.918317,-4.386476,4.369791,0.800454,1.751405,-5.368462,-9.886963,-3.092565,-2.572495,0.805018,0.177326,-3.170790,-1.092291,7.988546,-2.145845,-5.341868,7.131755,-0.893237,7.905462,-9.247805,-6.070145,-4.437686,-1.854568,-6.760173,2.809208,-5.764525,-3.332380,-3.337469,9.235501,8.818091,6.569889,8.883140,-6.211425,-6.367607,5.810136,-1.651362,5.054804,-5.224871,3.461818,-0.425456,-5.930935,-4.325801,7.485515,9.368106,-6.748267,-2.287830,1.806619,-7.824224,9.392940,1.756160,8.072503,8.659864,2.555825,1.587506,-5.395355,2.592835,-2.539692,1.243460,-8.178408,-5.224459,-5.255039,9.022901,-5.915655,4.497090,-6.069987,-3.539370,2.279570,-8.739799,5.385059,0.995653,5.998580,4.509346,-3.491853,3.028940,4.036779,7.397282,-4.356685,5.481265,2.998906,-9.790795,-2.229056,2.878640], dtype = "float32")#candidate|2368|(216,)|const|float32
var_2369 = relay.var("var_2369", dtype = "float32", shape = (225,))#candidate|2369|(225,)|var|float32
const_2370 = relay.const([-2.276019,-0.188077,-5.893535,-8.163839,-4.332724,9.682234,-1.364681,6.304403,-8.839915,1.940255,3.897755,-1.757828,-5.346285,9.234650,-8.639367,-8.253091,9.789995,-0.651400,-4.428923,-6.078255,-9.052073,7.556742,-9.140262,-8.896702,-2.691353,2.068861,1.053124,-1.243321,-1.060541,4.658064,6.220675,-4.345088,7.226326,-5.673032,7.966006,-2.419793,7.647526,-5.116732,-3.174148,-3.909599,-0.822639,-9.929539,3.736767,2.160179,6.391627,-9.721235,-3.054823,6.344583,6.536965,6.315832,-6.408429,8.055639,1.192455,-8.858896,-1.394012,-8.205339,-5.418772,-1.645473,0.966866,-5.610127,1.645592,8.479894,3.849459,0.010236,3.845254,6.555820,-6.009519,9.768825,-1.771495,2.069903,-9.230794,8.058444,2.695405,-1.958706,6.216409,3.119315,3.505919,-8.581245,4.252550,-9.605779,-3.146122,4.894043,-4.743341,-0.616907,-5.117225,2.474950,3.867634,7.217342,0.790661,-2.631776,-0.080643,6.919143,-7.637572,-7.818074,7.383634,-0.181573,-5.925097,-5.147650,-3.377030,2.936083,-2.648623,6.727543,2.862665,-2.963713,-4.717959,5.938083,-0.477567,5.078359,-0.695142,5.047653,-5.457057,7.363457,2.046167,1.490569,-8.173145,-8.629830,3.318231,3.492108,-8.879146,0.845566,-5.798672,-6.525040,1.546846,0.350454,4.735088,2.679132,7.427274,3.893008,-7.501422,-5.421213,8.342750,-7.727637,0.053330,-0.211339,1.911328,-5.692436,-5.535177,3.903362,-4.796790,-5.796830,9.725308,3.378953,-9.596491,2.311909,6.954724,-2.572445,-9.071678,-0.890707,-4.978647,4.365794,-4.779721,8.468190,-2.500950,2.750338,3.365142,0.513673,2.738022,7.833121,1.593248,2.239270,6.582272,8.981877,-1.755376,7.998749,-0.140360,-9.507200,-6.064711,-1.847265,-1.340480,-1.503716,7.572089,-6.608413,-1.892968,-7.703349,-2.229480,7.888216,8.040334,2.699678,-1.085727,-8.284670,-5.189409,4.536271,-4.770370,6.735617,4.019196,2.792991,0.965361,-0.393336,9.530642,1.329266,-5.787272,5.022562,-9.119634,8.107942,7.983465,2.928593,-0.696317,4.780643,-8.452120,-0.725043,-0.151762,-2.839233,3.285553,0.047723,-5.339774,7.759845,3.143135,-3.495180,8.289803,-1.720279,-6.693014,-3.423546,0.780218,4.870726,3.938421,5.680060,7.122709,7.961223,-9.312202,-8.796864,-5.402125,5.465422,-0.997917,8.168785,0.204031,9.126304,8.603020,8.773386,8.925826,1.998910,-7.497189,-7.042266,-8.291564,-8.182902,-1.505792,5.512286,-2.822613,8.840532,9.364819,3.673262,-6.258096,-0.499997,-4.862523,-5.779846,-1.708727,-4.580502,5.891397,7.911980,9.570466,-7.309921,-3.168037,-4.192212,0.949184,0.708649,-6.519104,7.402385,4.569732,-1.656215,2.069164,2.843085,-7.400548,-4.528018,-1.141000,-8.464992,-3.444165,-2.634624,-3.894425,1.685194,-3.372293,-5.145628,8.927212,1.043565,1.634228,0.762826,1.167347,9.637705,-9.157776,4.552155,7.992612,-9.028877,-1.553051,-2.582307,8.226220,-7.256905,-5.545579,-6.840296,5.911303,5.929079,-0.194478,4.814175,1.777722,3.883537,2.266942,9.250967,-9.391107,-8.412801,-5.085912,-7.446599,-3.573135,9.044096,7.740163,4.501584,4.153838,-0.443921,3.129542,7.631077,-4.954224,-8.466036,2.599846,-0.821736,-1.383307,4.298732,4.425454,-4.909336,-0.344837,-0.853063,-9.704635,-5.547663,-8.728796,4.711258,1.684406,5.010266,5.146766,5.528399,1.438501,4.584822,-1.625754,-9.619338,-9.710066,8.752493,-6.596139,-7.728073,3.932105,-1.470826,6.538081,3.701071,8.865033,-2.879682,0.723716,8.881688,5.302807,-1.079669,2.056759,6.524370,7.303926,4.117702,1.081174,-0.023694,-2.096280,-0.548329,-5.222503,-4.650432,-6.459574,8.147979,-7.459091,-8.007534,5.519827,8.804336,1.483367,-2.370658,-4.433099,-0.116041,7.704331,-0.907505,-2.221276,-9.562914,9.834201,-6.393446,7.708077,3.135958,-4.400332,-8.611757,-2.220455,6.364022,-4.489480,-4.198517,6.949863,-0.845622,-2.818884,-3.102348,-4.162377,7.017294,-4.447039,0.045779,3.674476,6.876939,4.245374,0.788310,-7.441592,6.503521,-9.288802,5.475269,4.879020,8.381849,-8.644408,-0.065607,-7.582710,-4.456000,8.532221,-5.613183,-2.834842,-5.245389,6.089086,8.810688,-2.789278,4.767495,6.924860,-0.868104,-3.521456,-0.511829,-4.966247,2.834242,-1.329618,8.103494,-3.845840,8.234200,7.131806,-0.445608,5.286699,-0.962352,-0.110465,1.544338,-1.214404,-6.689685,7.702339,-0.782863,3.370173,-5.530996,0.911858,4.594919,4.737859,9.620651,7.459604,-6.669225,2.701027,-0.204299,-4.023593,2.746735,-5.681443,4.296215,-0.398406,1.104306,-3.702941,-4.836079,6.102845,2.914905,-9.484101,5.918311,-1.567354,-6.709705,6.603428,7.853788,-5.260017,-6.399630,2.525574,-5.105838,4.663544,8.888443,0.930337,-3.136577,-7.594202,-7.744017,-5.769055,-8.364633,6.713895,-5.904970,8.220405,-8.918019,3.932787,-2.703487,-2.693469,-4.730944,-4.269949,3.522060,3.741078,-2.748366,2.071290,-4.659024,3.646804,-9.162860,-3.587559,4.663856,3.320555,2.382130,-3.049928,2.971863,9.340828,3.790584,5.354283,5.708826,-8.374205,-0.900976,-4.942527,6.179492,2.117329,-8.613751,-6.687991,-4.943486,6.649571,-7.406891,1.289041,3.445937,-1.563119,0.099781,9.141260,-1.514960,-9.599440,-9.057549,-1.026438,-1.141277,6.306549,9.281327,-6.549750,5.571653,7.848940,-7.004216,2.025955,3.707411,-1.992884,-1.374606,-0.240583,3.144324,3.136824,7.206361,4.467717,-7.313746,4.949525,-0.354049,8.396055,1.186077,-9.799860,9.835406,5.443243,3.440358,0.132802,-5.517916,-7.933358,6.435282,2.435536,2.694148,-5.703330,3.916494,1.517774,-1.117212,-1.090685,-5.754374,3.273578,-3.887810,-1.652448,-6.116848,6.271572,0.821095,-8.219968,-4.298495,-0.784409,-7.665711,9.455523,-6.848686,5.637578,5.844907,-1.441615,-9.310178,9.433876,8.290043,-0.999702,-8.014801,-3.249467,-7.604472,-6.635655,-3.064933,-8.720780,1.085266,-4.866940,8.488936,-4.803413,4.723586,-4.599227,-6.854551,2.532427,9.515570,5.888572,0.384143,-0.959107,-4.823036,-6.361906,4.141034,2.057011,-6.817405,-4.637275,-3.807712,-8.276273,0.467617,9.676427,0.332649,2.653977,2.811198,-1.610453,-2.163735,-5.900430,1.475571,2.693515,5.665120,8.180396,0.224818,5.521662,4.889217,2.072914,-0.317817,-4.906396,2.799618,5.942838,1.657389,-9.653917,-8.573757,-1.441895,0.490865,-1.455062,4.679086,5.038590,1.943939,-3.398515,-6.826537,3.784769,-5.929655,-7.592503,-2.404776,-6.192286,6.606151,0.654174,6.949157,8.120613,-0.745684,-1.553105,-6.493582,-2.392769,-5.782859,-3.011276,-2.785979,-6.041449,3.726708,3.594206,-0.408918,1.201098,-8.131706,2.660982,1.265098,-2.088705,-4.785595,2.239190,-2.266235,-6.410658,-2.182475,-2.867861,-5.480150,0.359711,3.202071,8.475224,0.620435,-3.571767,-4.147414,3.083899,-1.958131,7.163503,-8.990726,6.000751,-3.576213,-3.430912,-5.152273,3.842127,9.955394,9.202566,5.109776,-4.733058,7.107595,-8.649289,-1.093469,8.453385,-0.592961,7.938992,4.274375,0.605680,-0.997061,-7.554352,-1.679300,4.381107,9.539987,0.131811,-6.254136,8.781403,-1.949071,6.213326,7.218077,4.241349,8.628973,0.484902,-2.650585,-3.679758,-6.117770,0.247738,-1.443032,-1.435992,5.963115,3.079263,4.245275,-6.781426,-6.822153,-5.602546,-3.211349,5.611057,-8.428483,6.139874,-0.991851,4.474308,-1.428316,1.249644,8.177535,-1.371756,8.728675,-0.392887,-5.535652,-0.236277,-0.358191,2.125148,3.381603,-1.495839,0.769396,-7.957510,5.992044,-8.287976,-7.373251,7.667736,2.710749,3.581338,5.254750,9.322382,-6.354244,-5.282772,-5.714933,2.632973,6.363436,6.592374,7.280720,-9.988788,4.214382,1.014077,-5.295474,0.450042,-1.390732,8.683689,4.000453,-7.571213,-8.584083,-5.913790,-6.132918,-8.868331,-8.185547,-4.525745,6.381073,-5.950516,5.336197,2.854356,-4.675902,2.088708,0.115898,-7.757612,2.145077,-3.057452,-0.357004,-5.759589,-7.077490,-5.383065,-3.054428,9.564016,6.778743,-9.322748,9.251323,-3.807684,-2.855629,-0.452925,-3.548817,-8.319490,4.136702,-5.292475,-6.845645,-6.429100,8.850213,4.102706,7.887949,-1.730492,-8.079111,8.241448,-7.608702,-0.324952,1.593403,-3.493466,9.334199,3.911022,6.157115,-4.304140,-9.376575,-7.147681,9.262556,1.285375,-4.090368,1.181972,-1.807698,-9.923425,0.779520,-2.338817,-0.806782,-0.206664,6.577784,-1.109691,3.728752,-2.259088,-0.304231,-1.983010,-7.700020,-9.066432,9.530676,-7.098630,4.916794,-5.957005,6.091545,2.143609,2.086560,7.845018,-7.835173,2.462525,3.876538,5.380161,-7.561215,6.772327,-6.555722,-1.390341,-6.718611,5.329236,3.447062,-8.457809,-8.243300,-1.502689,0.005454,5.911429,-1.706679,-9.012921,-0.897599,6.420089,4.793319,-7.679427,-6.632065,0.448841,6.042195,-3.209134,-2.842320,5.266405,4.271384,-4.998424,9.800518,-6.136883,-9.027873,5.857207,-0.443737,7.503742,-0.633896,6.559413,-5.201926,2.235492,-2.722042,8.659472,-3.879904,5.548939,-9.300001,-0.893178,9.354548,8.784257,6.185415,5.316321,9.837040,6.710602,-6.943355,1.202880,2.551733,-5.241281,-1.902394,-8.830088,-1.856859,-8.479103,2.294085,-4.039013,6.244782,-2.945605,4.399818,3.779164,3.241643,-0.053501,5.045676,-3.544425,-0.455280,-1.428094,-0.586412,9.269646,4.261375,-6.759077,-4.886862,6.798182,-9.279083,6.982982,9.883336,0.290352,0.026097,-4.108972,1.387028,-9.245825,3.100041,-1.721437,8.893404,-2.812013,-4.456647,-4.006463,-9.426102,-9.238775,3.907271,-0.165502,-2.986645,5.393217,0.518241,6.363210,1.356134,-9.159767,-8.527889,-5.618935,-2.728219,-1.454554,5.637912,2.138918,1.767705,7.736908,3.000261,2.200889,3.808922,-4.347672,7.336546,6.356726,8.068764,0.883446,-1.736951,7.904564,7.822142,4.549672,-2.025855,-8.628151,4.156615,7.005839,2.025045,-1.184515,0.835704,7.743390,-5.674619,3.443570,-6.854129,-4.640810,9.242869,2.200681,6.421786,8.493597,8.531447,7.503068,5.277321,-8.885237,-0.007892,1.034293,0.667668,-8.868733,4.759671,8.877342,-1.273034,8.225704,6.259761,-3.862995,2.850051,8.045569,2.489044,4.327414,8.913910,0.842311,2.032129,8.642197,0.414713,-6.188275,-7.056711,-0.258915,7.682656,-2.065176,-6.026345,-1.799339,-6.163294,2.259676,-4.733972,8.772572,-8.617147,5.019504,7.137575,-3.757146,-2.507962,-1.875661,-5.330894,-1.695576,-7.491202,-8.980097,9.813650,-2.938169,-8.204879,-2.088397,0.109840,-0.105759,-3.108898,1.475647,2.333917,3.133575,-6.215521,-5.086178,-4.947134,2.255279,4.114709,-8.853755,-3.444123,-3.069486,-8.565582,0.679441,-8.414171,1.995065,-4.065566,1.663547,-5.260020,1.835742,-1.848125,4.939873,-9.227667,2.843134,-4.090254,7.349416,-8.492593,-0.333752,-4.921313,-3.412361,0.992189,2.531945,-2.380162,2.120372,7.993170,-0.455916,-1.244277,6.608819,-4.797383,-7.898321,-0.208969,7.790342,-4.373618,6.976721,2.489097,9.042816,6.921474,-1.120248,6.923796,-0.619016,8.704886,-7.740282,-5.822290,-7.963922,-9.881432,6.232267,-5.537946,-7.306729,-2.981504,1.456913,9.840678,7.788018,-0.382738,6.279392,1.188502,-2.786861,-8.398401,1.790203,-5.193830,7.501114,-3.849564,3.492537,3.833189,5.967684,1.002629,6.921085,-3.056349,7.985622,3.878947,-7.593504,-5.719968,5.225408,-4.663182,5.246834,-9.828720,6.463283,-7.788116,-7.909183,-0.120608,0.716330,-0.065885,5.417881,1.992713,6.663748,5.518576,-6.034427,1.691635,-9.152800,-0.130936,-7.580647,-4.733080,4.249260,2.063604,-1.588181,-7.400913,9.211487,-3.818679,3.197315,-3.802662,-2.624465,-5.767566,2.794000,-7.007230,5.436940,-0.955458,-7.517734,-8.510378,7.555126,9.727405,1.389664,3.196156,-8.793594,6.475831,-3.542348,0.396389,5.847278,9.441024,4.101596,-0.475809,-9.899214,-0.514942,8.677622,-8.777939,-8.077789,-4.802977,2.741735,3.791382,-5.793349,4.356994,-5.395915,0.469186,4.157353,-5.363257,3.401156,0.823363,1.963208,-6.734607,-9.271815,7.222811,-4.954816,3.939472,-6.208233,8.880689,9.068907,7.026245,3.940277,-8.129575,4.351907,8.358102,4.510826,-4.989980,0.939904,-3.908755,1.133218,-5.083932,5.872099,-1.249396,-8.747884,-1.665422,-6.195260,7.547549,3.747968,-2.890602,2.640253,7.423764,3.068001,5.474576,-2.253697,-0.338279,-9.494067,4.932725,-0.908748,5.916058,8.170511,4.993191,1.449056,-9.252612,-2.290527,4.468004,-4.971447,-4.582155,-3.861144,-4.350285,1.560949,-7.881832,-5.441444,-9.149458,7.986535,8.538057,6.000917,4.049520,-7.220932,1.439344,-5.852763,-3.141396,1.373562,-3.891723,-2.730976,-0.263804,-5.457990,3.455454,-7.582991,8.163402,0.630959,4.210302,2.414412,4.698462,-2.917880,-7.678696,1.001637,0.390035,-4.033215,-7.551377,1.741200,-4.838563,-2.770043,-1.222294,5.833846,-1.538160,-5.037912,-6.012720,-5.121306,4.120836,-4.411767,-7.086712,-4.238837,4.632304,7.884915,-9.313200,-7.342913,-7.494457,-8.136803,-6.970047,7.040471,8.567356,-7.666497,6.718118,8.760194,6.942249,3.037210,-8.305016,9.971525,-9.848185,6.229631,9.367890,4.086123,-2.130521,-7.619065,-9.231894,-5.237975,-2.369998,2.771282,7.720354,-1.234102,-6.575244,-5.997843,-1.752673,-6.488009,8.460741,1.166888,-8.990356,-1.292476,-0.457184,4.055278,-8.336524,-2.860920,-0.823598,0.427589,9.636713,-8.299068,0.183546,-1.252987,-6.840424,-6.028994,-1.938876,0.869587,-8.002965,-0.555051,-1.712842,4.230197,7.280433,4.174480,1.958949,5.004917,4.966840,9.382801,0.092860,-2.368892,-7.934577,4.899127,-0.666564,2.728685,-2.622085,6.601382,3.370225,-9.122388,8.881157,-0.236681,-5.286992,6.740804,1.366732,-5.643914,-5.000977,8.376460,2.317575,7.788573,5.925920,-7.074131,-2.413367,-9.196969,4.098628,-4.092466,3.682779,1.451821,5.195454,1.891332,7.249266,8.851202,-6.487594,3.256202,5.994275,6.479942,2.931331,-8.715352,0.871414,-6.233284,4.396928,8.892311,4.959156,-2.662015,8.006717,-6.537441,4.184374,-2.633363,-7.411686,0.418993,8.379024,-7.161599,5.858786,-5.029149,8.420539,0.199155,-6.550151,0.510605,7.030772,-1.495637,0.847254,-7.472970,-7.549247,-8.680006,-7.237304,-3.932259,-3.236509,-8.496235,0.818933,9.601278,1.402424,-6.496999,6.635539,-5.404815,6.847767,-2.765151,9.877178,-0.872808,1.001511,-7.003936,-4.728151,5.004646,9.448579,-7.974052,3.795479,8.303189,-0.495566,-4.130491,-2.291235,7.817227,5.639985,-6.779148,-8.275498,-8.784768,-6.302846,3.426424,2.745765,7.668727,-8.299617,9.878985,6.283728,7.201887,-3.704177,-4.402696,-4.731010,2.916882,3.227208,-6.622817,-5.196146,6.572802,1.941080,5.162732,-8.825429,8.543674,2.205895,-8.155394,6.180884,-3.706084,6.961192,-8.866930,-7.057499,9.704363,-7.492557,4.180301,-6.627513,5.098427,3.306690,-0.529878,2.822863,5.937398,-1.255704,-2.147512,7.259939,-1.017392,3.962857,-0.482099,-3.911565,6.815374,0.317041,3.465732,4.145221,4.241913,7.106676,-0.022589,1.239519,6.618798,9.890009,4.859585,6.537581,6.826575,3.948557,-2.501041,1.844073,-6.571682,3.778320,-5.192717,-1.272586,8.207047,0.071911,-9.368751,9.297653,5.302778,9.993193,7.039314,-6.621942,4.899614,-7.038100,4.037305,0.084018,-0.478849,4.347166,-3.238274,-9.606976,6.952436,0.170668,-3.602338,-6.081608,-5.329336,5.302871,-4.899625,-6.272629,8.375101,4.006735,1.410167,-0.943728,3.131786,-0.597048,9.808294,-5.982460,0.319969,-6.063877,-6.995249,1.344719,9.153268,1.696561,-4.798476,7.446522,-2.404399,-9.690357,-2.442516,-7.528896,-4.987323,0.090332,6.182666,-0.178214,9.858182,4.163224,5.014812,-9.646231,9.016567,-6.063565,-2.166496,3.853042,3.230716,-4.134237,-2.754004,4.663963,8.864455,-5.956123,-1.396506,5.654768,1.643077,-3.822670,9.869479,4.431434,-6.856934,-0.538086,-3.066171,0.140680,2.460758,5.948666,-2.267852,-4.422545,6.710061,4.948680,-6.166123,4.018069,5.450618,-4.455780,8.409573,8.266919,-8.427044,-9.499363,4.248115,-9.024593,1.052603,-6.548910,-6.280019,9.132846,5.138156,-6.045532,-3.912025,1.991425,7.525076,-3.599765,-0.410640,-0.726929,-6.340138,9.748144,-5.101398,-6.146811,1.953167,-3.734341,-9.697201,5.043001,-9.326341,7.017700,6.457749,-0.876472,-1.379144,4.190251,-4.839050,5.671390,-5.305910,-3.096985,-9.042784,-0.531553,4.620144,-2.459686,4.914525,7.973591,3.564840,-9.646676,9.672883,9.568465,7.036950,-3.694601,-1.741146,-7.980888,-7.936349,3.557184,-1.367644,-2.702747,-0.032368,8.625786,-5.492797,6.694427,2.228728,0.271652,-5.429215,-0.698781,6.901579,3.158092,8.920296,2.800756,-7.458282,-4.512994,-5.730126,-8.532438,0.799070,-9.534580,-2.297282,2.368368,1.575056,5.847565,7.655163,-9.284544,-7.102404,-1.230489,0.660123,-0.431005,6.059907,-4.928679,7.819861,-0.512215,-9.675694,2.276775,7.140577,-5.824220,9.854163,-8.926924,-7.980699,1.859743,8.635398,-5.330563,8.239195,-7.765399,6.481056,7.951581,-2.178231,-3.745800,-4.164628,4.425720,-9.916943,9.682307,8.936235,4.679753,-5.952696,9.036622,-1.627385,-1.872809,-4.020819,-0.965126,-9.847585,-7.448257,-5.886727,1.182808,-7.138512,-7.273515,9.475276,-4.470386,5.737486,-9.700988,2.464915,1.191722,8.360266,7.118875,4.898741,7.219630,5.482572,-7.006383,-6.801119,0.708065,-9.053097,-3.193485,9.313341,1.148169,-1.680269,-3.675492,7.782178,3.897852,7.116034,-8.309239,0.650546,-1.525326,4.856958,-5.968769,8.299156,2.556528,9.610629,7.753670,-1.054055,3.439574,-9.230303,-5.454044,-9.743480,-0.864909,0.869645,-6.622288,-1.567297,3.068321,1.729545,-4.003189,8.885229,-8.770636,7.877185,0.988079,-7.304018,-6.146728,-7.497997,-0.071809,-9.031177,4.894442,2.559446,-3.713760,-3.624316,-2.411017,7.565129,-0.945935,-4.730055,2.443247,-1.891647,4.168493,-1.159308,0.865833,7.277219,6.131573,-5.555561,5.800253,-4.350093,-8.463693,2.278921,-1.669192,5.404962,-0.837263,1.578966,6.647608,-5.767654,0.344627,-0.914161,-8.050338,-8.290842,3.521429,-9.096034,2.588745,8.154815,6.673029,-4.071829,9.151768,3.682831,7.727061,-3.115122,-1.413897,9.883489,3.892924,0.515033,5.310430,9.131452,-9.724541,7.490679,-1.941683,4.898720,-3.383969,1.744355,5.335716,7.460708,2.451746,4.054531,-9.992875,6.862131,-0.637630,8.053099,3.045754,5.963733,-4.961881,3.208616,7.468083,7.406921,-0.450101,9.122623,6.964404,-2.655331,-8.141625,-4.731911,-3.967240,-1.584903,-4.455642,3.902699,-4.242642,-0.315355,5.272351,5.650956,-5.327442,-5.088758,0.207484,9.133485,-2.649019,-0.050919,3.091719,-2.730640,-6.447517,8.664191,-4.334143,-1.019710,9.860005,-1.963141,-2.521994,7.153457,-5.254976,2.054737,0.178932,-0.525019,-9.641896,6.960972,2.963510,-1.648386,-0.194120,6.382042,-9.643907,-0.259161,-5.949038,-6.805987,-0.329666,3.409540,-6.770171,4.881443,9.310480,4.928196,-8.252408,-1.140888,-0.910228,4.876517,-4.005372,-0.881814,9.908400,-5.002133,0.810969,-8.565569,-9.444112,-8.238651,9.926304,-7.579245,5.671220,-8.830409,-0.709372,6.682208,4.946429,-2.753974,3.296685,-8.129488,4.697321,-1.649399,-7.766960,-2.512824,6.819143,6.596455,-7.335577,3.711846,3.562694,6.321423,-6.662565,8.020104,-9.122217,4.052672,-8.149552,-9.650792,-2.565877,-4.551678,1.301735,0.005356,9.867841,9.763289,9.804127,7.901856,0.979758,-2.927482,6.428499,8.287871,8.067114,-7.137242,2.110392,3.267166,8.438883,-4.924407,6.472466,5.761476,-9.851420,-3.644203,-1.889016,-5.710812,4.637110,9.512318,-9.686698,-3.172882,-6.514311,4.785399,1.481333,5.791076,-6.080656,4.572876,-2.792233,-2.698737,-3.915603,-2.660662,-1.363113,-9.156287,9.566711,6.595646,-3.888993,-0.708106,-8.677903,-1.693103,-4.470431,-3.270860,0.228821,-8.171832,6.733389,-9.328775,-4.225382,-4.102755,-0.622293,-2.695077,-9.703256,2.559266,5.579829,2.326447,-0.217813,8.978615,-6.425040,7.211003,6.226739,3.066199,2.383923,-1.270922,-9.702121,-8.372648,3.126626,-1.319638,-1.108676,6.300350,7.220275,7.670818,-6.692328,0.494246,2.210561,4.099201,-7.610859,2.926357,-9.073313,9.621339,-4.415928,7.288985,-9.809374,9.552005,-4.160779,-3.063468,-6.155187,9.852773,-9.415243,1.550685,6.558439,8.708862,7.680987,8.281981,-4.011977,-8.611669,5.473747,6.415449,4.273569,-6.274693,1.446078,-7.721903,0.231915,-7.002968,-7.486312,2.389446,-9.233111,4.800887,3.395176,-5.656498,-3.154250,-9.543517,-4.268165,3.170675,-3.994039,3.969247,7.120255,9.556636,9.417843,-2.754853,4.086293,-0.843997,-5.792028,3.394092,-9.818564,-2.988742,-8.862878,-6.338579,-0.317896,1.583278,-5.959839,-7.198330,-6.738141,-2.981503,3.609241,9.353834,-0.063527,4.443054,2.524733,-3.484382,-7.809461,-8.001601,2.298619,6.869102,1.659830,-6.897567,-6.826675,0.311348,9.174320,-0.978858,-6.889213,1.019823,8.352521,-2.923547,-5.201575,8.116835,6.849043,4.906600,-0.737571,-2.638235,8.187055,9.696357,7.629999,-5.834127,-9.074467,5.136356,-3.788655,0.687764,3.998100,5.915835,-3.168585,-8.441219,-1.232098,-2.654288,6.446745,-4.980460,-7.057869,-0.103795,-9.634225,-7.293236,6.975568,-9.479587,-1.447758,-6.915217,8.280284,4.738502,-5.855314,1.527179,-7.279763,7.820043,-2.983277,-0.049470,-8.787032,-6.772542,-8.263256,8.171837,-6.587957,6.329483,-8.485209,2.848222,2.253455,3.561196,-5.414639,1.642933,0.673152,-7.397258,-3.235222,-4.724770,5.289900,-2.151572,0.282932,-4.256271,6.119032,-3.301275,9.953061,4.357205,2.486094,-1.801029,4.878070,-3.821141,-0.236912,-0.121360,0.202950,4.674943,8.039895,-3.511002,-5.926184,-5.160430,6.112530,8.827902,-9.026614,8.627069,9.571225,-4.895954,5.973423,5.537086,2.802977,8.423810,-8.973815,-6.682164,-6.524978,-0.806471,9.049696,-4.326824,-7.085322,8.157615,-6.651696,-6.634055,-9.166936,-1.275396,1.987540,8.561791,3.716732,0.789255,-1.672562,3.800737,6.951583,4.807329,-1.816621,5.284060,4.226174,-9.647703,2.834385,0.891553,1.768688,-6.305213,-4.032154,6.416493,-2.991741,3.678145,-1.503314,7.071420,8.949232,-7.984356,-6.904892,-7.884110,-2.177469,8.864699,4.758228,5.623704,-0.456199,3.859878,-8.611184,-7.412872,7.020459,3.262794,-3.930124,9.172679,8.890014,9.439636,8.716540,6.485949,-9.498837,-8.038875,6.050579,-9.837796,0.995759,-5.209724,5.158743,-4.084739,3.663678,-2.359569,-3.988370,3.419117,-4.828711,5.290976,-2.396641,9.200934,4.311549,-0.261230,-8.723141,-5.967998,-8.714410,9.800778,2.754867,-8.272355,1.210863,-4.270311,3.379961,5.617668,-5.241490,0.813322,9.824150,-5.653530,-1.003459,6.530675,8.123113,-8.523837,6.226202,0.602342,2.862730,9.348840,7.314544,-7.954883,6.214403,-0.904444,-6.352951,-7.889836,-8.789198,-2.749177,5.338532,9.653548,0.688920,-5.945476,4.611428,8.924080,1.544945,8.186756,-6.904085,1.423449,6.550744,-4.073532,-2.005525,2.929501,4.321828,6.058906,-3.889403,7.588844,1.236226,-1.864177,-4.564806,7.186291,-1.924215,-8.212067,4.976763,-4.024948,9.750969,-5.552627,1.883591,-8.114959,-7.961223,8.737272,2.268827,-6.227564,-8.426717,1.345415,2.836886,-3.315653,-3.794659,-5.965174,2.542966,-4.571564,7.747912,-6.965922,7.704331,7.122083,-6.877714,-9.095684,-2.425131,-8.836995,5.765586,1.908082,9.399980,-5.238787,-8.840755,7.534160,8.910669,-7.726359,-3.102876,5.166191,5.998014,5.256000,0.044340,9.252492,1.001549,-5.739775,-3.129671,2.610840,4.060491,2.510911,-9.540638,6.393705,-9.536951,1.306128,-2.114277,-2.299614,1.121605,-4.801713,4.673990,-7.824000,6.976012,6.883511,-1.299607,2.022293,-8.890423,0.106426,0.880848,-4.584405,-2.902830,7.669170,-7.982539,2.712816,9.917681,-6.391853,6.075647,5.113868,2.435076,-5.399289,8.125752,-4.946731,-7.788513,4.195944,-6.072588,-0.594046,6.015672,-4.598336,8.118966,1.809075,6.050643,-2.977895,2.835274,4.120735,-4.261062,-1.666422,-1.923619,-6.200889,0.779763,-0.281865,5.285805,-3.677174,-7.010666,0.214565,-4.039346,4.339985,-8.941135,6.175356,3.002099,8.154304,-3.459238,-8.686069,-0.616709,-3.215788,-1.875564,6.433661,9.142345,-2.369552,-5.472776,3.952023,-3.714814,-5.712033,-1.887056,-9.692683,9.340394,-6.265857,-5.356996,-8.377113,5.484765,-7.150114,1.939242,7.214585,9.254800,7.888937,3.600396,5.213344,2.500329,5.092045,9.495479,8.566684,1.345077,-1.018010,-2.970639,-0.441571,1.948076,4.027764,-7.851161,3.162579,-1.812050,-7.283205,-8.303881,-4.869034,1.362037,3.807566,7.990864,8.158949,-3.236805,-3.367010,-4.097366,-1.464782,5.704681,6.572641,0.286740,-3.549683,9.763073,4.481743,-6.329236,4.618830,3.029068,-8.182856,6.586001,1.804999,6.604073,6.171327,-8.942264,-3.166297,7.075009,-8.601053,-5.332870,7.299251,7.865987,0.640856,-2.726158,2.635724,-6.746073,-1.406546,-2.506525,6.359124,-6.999223,7.986875,9.217039,-8.094464,2.480046,0.887090,1.148491,1.904379,0.969588,-3.359876,3.211653,-4.564345,9.165434,-9.447504,-0.180964,-3.287239,-2.750580,-1.333590,2.174125,-2.103186,1.078854,-9.909897,-0.685837,0.359056,3.650266,1.922385,0.219930,-0.222270,7.532352,-6.844220,-1.669826,-5.587205,9.990377,-2.333384,1.638293,5.977247,-1.554428,-1.103928,-5.761631,3.079524,1.225507,-1.041839,-6.473950,-6.351283,2.920428,7.122413,1.394573,-2.851169,-1.981911,2.612865,-7.187634,-4.629040,-9.807363,5.453423,-9.956762,-3.713167,-3.105358,2.489886,1.057781,-5.615571,-0.968450,5.222930,7.532607,-4.078777,-6.689980,7.608639,5.109540,-5.084015,-2.801118,-4.807120,-7.150203,7.415148,6.948357,2.859186,-3.271267,-1.401210,6.668465,-6.717439,5.167481,8.990231,-6.311677,-1.229064,-4.760517,2.249362,5.735335,-2.607921,8.541694,-3.604806,-9.110638,6.816817,4.072543,6.360097,4.765338,4.819670,7.051435,9.489120,3.690252,5.565651,-2.783453,6.523578,-0.494934,6.701688,4.748935,-8.988987,9.458208,-0.995232,4.751402,1.282973,5.546814,-5.528224,1.548989,-1.239192,9.281125,6.717296,-4.651691,7.818762,-6.051740,-4.153558,-1.920391,3.468913,3.097737,-3.000143,3.244060,4.145045,-5.193589,2.393220,1.840155,0.006497,7.519126,-5.883066,8.690769,-8.254922,-2.938025,4.891651,-4.080015,-5.987306,-5.523211,-3.317032,0.228620,-1.841208,1.803109,1.367390,8.520962,-1.149284,8.290142,-7.747705,-7.197082,-5.435917,-8.355326,-0.612160,-7.978746,-1.928994,9.733298,5.695980,-7.000883,1.994644,2.789900,9.760660,8.249778,-9.510700,-3.391367,7.872834,4.401765,-2.567618,6.843849,-3.888801,3.472504,-1.884149,-6.993820,9.570174,8.834314,-0.568766,-6.731257,4.608132,1.685305,-7.020404,-4.544576,5.361095,-6.596863,1.753952,-9.718543,1.470009,-3.784394,-1.509681,1.132077,-6.257549,-4.305537,-9.838041,-4.034123,-5.684886,3.594021,5.178890,-8.941220,6.722643,-8.695340,-1.912062,2.077662,1.818867,9.906049,-8.568284,4.523753,0.882997,7.049470,-7.030868,1.036792,-2.636062,-3.279580,5.540662,-0.999412,4.181212,6.650103,8.593060,7.238823,6.678419,-4.616328,-6.605774,-8.019263,-0.421160,2.137830,1.409964,4.569800,9.182558,5.798906,6.947343,3.257544,3.270079,-7.174104,2.179983,6.008571,6.031315,-2.784539,5.997812,9.310935,5.134015,8.961350,-6.305028,-9.577885,-6.656538,-0.815154,1.058491,-9.028332,-9.850264,7.254782,-2.283388,-8.554550,-1.020609,3.872434,1.525710,9.885517,4.970471,4.728758,-5.376519,9.813532,-7.145074,-4.829166,-4.314007,-2.540389,8.107984,-2.796648,-9.668304,7.679511,-9.203250,-3.112552,-2.500331,-5.847559,-2.874063,5.720678,6.268592,4.718614,-9.971688,7.670372,-6.764856,4.934738,6.101270,-0.171232,9.118117,-5.266135,-6.133219,2.461427,0.918179,9.132689,-4.719125,-3.467422,5.354852,5.168429,2.732752,-8.811801,-2.935005,7.025965,-6.511480,7.519322,-7.989455,2.604743,-2.585219,9.065250,-4.143086,-4.385984,7.475496,-1.005326,-4.759982,-0.163736,-7.285781,-4.902384,-8.051754,-5.642441,6.785326,-7.282917,4.665286,-2.861701,0.700064,1.951301,-9.726556,-1.296742,-9.298953,6.958446,-4.699305,-9.246942,-2.142339,3.065592,2.561026,8.308292,8.019563,-7.726323,0.960789,-8.096020,-9.484689,-6.546523,7.163981,-6.480589,3.569791,1.793172,1.290871,-5.445756,-4.279643,-0.013903,3.304175,-3.802047,-3.512659,-0.284329,5.213795,-2.169931,-6.091719,6.902236,3.243789,-9.353496,7.290027,-1.015329,0.444244,-6.645821,-7.999369,5.357068,0.973536,-6.292057,-5.053847,4.242380,7.135783,4.919158,1.643210,-4.552707,-0.599679,6.477472,-5.906012,-2.821279,6.915542,6.958672,-7.675066,2.825259,-0.290902,6.576423,-4.155880,-5.067012,-7.794541,-1.615601,-9.225833,-6.744958,7.919593,-5.575377,9.482148,7.241262,-8.274783,-0.724796,-6.525566,-6.455526,6.958669,9.833452,-8.963616,2.467678,-6.963691,-2.426654,-2.399858,1.877778,0.131121,7.831547,9.703854,2.199039,2.693513,-6.986400,9.717971,-5.552196,-7.069446,4.534435,-0.805863,9.513186,-8.575947,2.485129,-4.238395,-9.356329,6.233681,-1.721702,-6.859831,-6.841745,1.684505,5.586117,2.283493,7.452428,-8.238197,-9.539288,6.934294,0.751619,-5.453064,6.931495,7.847282,-1.173165,0.714840,3.076199,-7.541188,-0.248411,-9.987745,-7.555561,8.687098,3.293714,-5.833105,-2.824043,2.667631,4.094196,9.326065,-4.044530,-2.565965,1.157058,6.251877,-7.585510,-2.747561,6.493555,-2.183119,-7.576821,2.276099,0.146938,9.784922,-3.604428,3.013464,-6.466827,-5.954251,-2.551738,5.675498,-2.840356,-4.412297,-3.128306,3.770288,-4.366096,-3.791112,-3.050978,-4.877533,8.300989,3.102234,9.637274,-0.583240,7.918672,-3.757540,2.606384,1.259347,2.117179,-4.015454,-7.529153,5.922818,-6.899201,2.637578,-1.562168,-2.713425,-3.547314,0.464553,7.560699,6.643568,-0.753457,-4.982168,-9.053554,9.121702,5.277590,3.596148,-7.397748,-7.426700,-0.297115,5.004883,-0.520742,5.293084,9.062135,-4.987888,-1.133948,-7.954311,1.259269,-6.704821,-9.533694,1.083019,-2.202109,-2.913897,-7.902271,9.840985,-6.399010,9.315711,-2.603715,2.138787,8.527098,-5.022281,-3.831825,-2.835522,4.208737,7.518336,-2.902484,-8.304192,6.114623,3.360881,3.971727,1.439181,0.721824,-1.939546,1.738522,-9.680449,0.743370,-1.091122,1.176067,-6.278815,8.810771,-8.077916,-6.849316,-8.766709,8.887549,9.525800,-0.906378,3.315290,9.019713,-5.624149,5.812979,3.420255,9.716802,-3.337008,-8.517627,-6.243904,-8.235976,-8.450844,1.798899,1.089722,-7.321533,5.773063,6.341922,3.992510,3.630352,6.786594,-3.963733,6.355645,-6.799178,-1.649912,-9.765341,-3.662414,5.494806,-9.933752,-2.342316,-3.954671,-4.906004,3.394450,-8.698692,6.875878,-8.305948,-9.876416,1.944276,7.617463,-3.683705,9.870539,-7.813968,1.172767,-9.214478,-9.459193,3.327707,7.534972,-3.928019,9.875655,4.183114,-4.218126,1.646974,-7.857171,4.593866,-0.100750,9.077736,-2.821581,-8.705193,-9.078945,6.849229,8.619333,2.463474,8.558063,8.027647,-3.520168,5.232184,6.544915,5.784566,8.257827,9.543456,-8.532376,7.396930,-2.002192,8.054770,-5.601296,4.870707,7.474458,3.346957,-7.761511,-7.383770,1.950356,-7.765829,-4.553594,5.033743,-1.938445,-3.304107,8.889408,5.954312,2.138799,-3.978985,-5.580441,6.749266,-2.709511,-4.952148,8.536300,7.664571,-3.904123,3.322547,-9.660844,-9.237009,3.566507,7.417552,2.236055,-7.299547,2.995973,-9.125626,-4.958444,-6.003353,-5.738000,-0.269451,6.888575,2.465022,9.186846,-0.445874,3.368733,-9.541114,3.589937,0.819989,-8.089610,3.068794,6.399573,4.437488,1.412033,-6.811472,-0.989718,-6.981885,8.617627,3.387088,-8.316033,-0.912708,2.744176,1.427166,-5.697228,0.750702,-2.286688,3.423385,-6.191206,-6.747199,-1.141681,-2.910019,1.265587,-3.063754,-9.567662,3.482835,0.864666,-3.941569,-3.866387,-9.907804,-1.765999,7.670658,-4.834858,-8.383696,-7.236923,0.058699,-1.347814,9.976945,-7.255308,-6.854784,-5.726728,5.569526,8.880450,-0.817436,5.202345,-1.754101,-6.027898,6.181330,-8.345536,3.033109,-2.903551,4.350315,-1.259180,-8.276333,-8.483176,6.689941,-4.537209,1.985251,-6.912592,4.419548,-1.099972,-4.337340,1.634956,1.326392,5.517302,-7.582926,6.829211,-2.096314,4.999177,-1.681618,5.469595,-9.213700,8.209761,4.309765,8.339488,8.242139,6.820072,-2.406413,9.925367,-4.251515,-2.514641,-3.618087,3.965385,-5.746824,8.902906,-8.292237,-7.313294,-7.557762,-2.760168,-1.025861,-0.695988,4.188113,3.678911,4.775818,-8.409325,2.213731,-8.067479,-7.273924,5.332421,-3.204865,-1.502496,0.540686,5.458557,-5.139844,-2.368067,4.828012,-0.473058,-2.686973,-7.007180,2.792169,3.260349,-9.152077,-1.674151,5.633657,3.943745,4.570467,2.091467,-7.830460,-5.025286,-6.292206,4.499173,-4.428503,7.269733,8.751309,-8.184281,-1.922005,-9.325199,5.459643,4.714146,-8.295852,8.897768,-7.490889,-2.230547,0.128528,7.262331,5.725404,-4.691160,8.681149,-9.178701,1.055146,5.708674,9.075016,-7.298279,-2.066912,7.535806,-4.070452,-2.880456,0.356731,-5.782139,-0.737408,2.195051,-2.227130,7.351613,5.123569,1.586594,-0.904036,-2.963186,-2.011300,-6.366274,-3.951986,7.710867,-9.524659,-9.159960,-3.190137,2.123507,-3.417229,6.401095,-7.164676,-9.011637,-2.426248,-3.586662,-2.835266,-4.052626,-4.116314,-2.482784,9.848183,9.734604,6.306766,3.694992,-0.829382,-5.745841,8.121984,-9.673151,-1.922578,0.360629,-3.475860,5.921848,-1.416896,9.538995,6.575154,-2.784747,0.354502,-2.807936,1.593681,-0.488168,-6.369543,-5.892735,-4.318695,2.102904,-1.772060,-9.175034,3.977469,9.331497,4.154278,-1.572638,-7.982735,1.601134,-2.631690,2.343892,-8.698284,-7.188732,-9.922105,-3.452555,6.373398,-1.085255,7.749028,-4.558642,-6.939578,-1.565299,-3.792547,-2.984179,4.214141,-9.323119,-0.193373,1.811293,7.828493,0.547953,2.176653,1.850883,-6.573506,-5.395772,-6.861400,-8.489004,-9.125925,-6.621970,6.386320,-5.986120,4.910391,-6.459525,-8.030341,-5.010140,0.244433,5.645167,8.797467,7.121600,-9.533174,1.581394,-0.623073,-7.109629,4.989654,6.772020,3.207649,0.162255,-3.282244,-7.817051,-0.769544,0.342195,8.243965,-3.111901,8.599085,-7.348484,6.325806,-8.336549,5.968383,-3.028142,7.734192,1.150297,7.284474,1.839715,-2.707786,-5.922276,-8.501933,1.269835,0.440409,2.179910,3.629104,-5.692503,7.624947,5.060433,6.741724,3.154946,5.104351,-1.611492,-5.275950,7.383782,2.815760,2.321716,5.925527,0.041632,-7.868978,9.689347,-8.063729,-3.288699,-7.140427,-6.697724,1.507641,-5.702678,-6.241805,-7.073304,8.032719,-8.384425,4.059059,-9.599519,-3.842845,5.248723,-0.247485,-1.807256,5.519231,6.627239,-4.272926,3.438656,4.085126,1.323271,-9.350369,-0.800863,2.134744,1.867283,-0.469004,0.653238,0.309038,0.568491,9.245740,8.658954,-2.370387,-5.103177,-3.255758,5.908377,8.649774,-2.645856,-3.599022,8.878079,3.328958,-7.756340,8.161553,-1.542631,1.957386,-2.065751,1.395453,0.341680,-0.694464,3.253890,1.667116,5.893536,9.589288,5.970889,-6.180002,6.574254,3.464857,-0.722857,7.842933,9.678873,-6.233987,0.130884,0.726563,-4.054229,-8.173496,4.310702,-8.934982,-3.078851,-5.505616,3.586495,8.765832,-6.944601,-1.406830,3.804918,5.376394,-6.490434,-3.099970,3.690875,-7.877437,-8.166590,2.371408,5.374206,-1.274001,4.049879,5.087360,2.130578,0.791020,8.761322,-8.241329,5.581961,4.883986,-3.570234,8.791060,-7.905868,0.652218,-5.404776,-4.716436,-7.223269,-9.917149,4.004715,-0.137300,-5.367690,-3.981829,6.731706,-5.163882,-4.551365,9.400285,4.956801,-2.787620,-9.003532,-6.654583,0.441627,-9.859911,5.818959,0.116657,-2.704400,-6.410208,-1.994943,-8.585122,3.610256,-2.555890,8.657827,-6.439643,2.852610,-3.762171,-1.545921,-5.216802,8.405248,2.417400,3.973757,3.527682,-6.597632,-2.966484,-9.207047,7.770756,3.912176,4.073335,5.441472,-1.494611,-3.411285,-1.126874,3.436186,-4.675944,-4.290970,-2.050020,5.575504,4.298947,2.603640,-8.181835,0.777119,2.083963,9.656254,0.711011,3.582281,3.075260,-1.096615,-7.437510,1.593915,-9.774025,3.796184,1.954510,-8.212726,-2.059798,6.280294,8.498759,-3.023365,7.555780,0.844491,-0.483919,-6.275431,-2.754004,-7.667809,0.093618,-6.519340,5.699464,-0.644813,-9.897256,4.695236,-8.640002,0.240454,9.595585,-1.297946,4.656667,1.622418,-1.583864,-7.476317,-8.773094,-6.157697,-2.232955,8.927913,-1.461488,-8.824906,-2.297262,1.084751,-3.748820,-0.104855,7.938306,9.099688,-9.114633,-0.395304,-7.777733,-1.021820,9.038014,-1.205581,6.056793,4.637552,9.642843,-8.250364,-8.761957,-4.144823,-6.994406,-1.389630,-7.510730,-3.636672,9.117534,1.907263,4.169033,-2.166878,-6.733883,-9.067330,7.227395,7.880885,-8.458496,-6.898099,-2.104422,8.331087,-2.224186,-9.277150,8.129409], dtype = "float32")#candidate|2370|(3600,)|const|float32
call_2367 = relay.TupleGetItem(func_650_call(relay.reshape(const_2368.astype('float32'), [9, 12, 2]), relay.reshape(var_2369.astype('float32'), [25, 9]), relay.reshape(const_2370.astype('float32'), [3600,]), ), 5)
call_2371 = relay.TupleGetItem(func_655_call(relay.reshape(const_2368.astype('float32'), [9, 12, 2]), relay.reshape(var_2369.astype('float32'), [25, 9]), relay.reshape(const_2370.astype('float32'), [3600,]), ), 5)
uop_2373 = relay.acos(bop_2340.astype('float32')) # shape=(2, 7, 1)
uop_2375 = relay.acos(bop_2343.astype('float32')) # shape=(2, 7, 1)
uop_2417 = relay.tan(uop_2344.astype('float32')) # shape=(2, 7, 1)
uop_2419 = relay.tan(uop_2346.astype('float32')) # shape=(2, 7, 1)
func_1899_call = mod.get_global_var('func_1899')
func_1901_call = mutated_mod.get_global_var('func_1901')
call_2420 = relay.TupleGetItem(func_1899_call(), 1)
call_2421 = relay.TupleGetItem(func_1901_call(), 1)
func_1171_call = mod.get_global_var('func_1171')
func_1173_call = mutated_mod.get_global_var('func_1173')
call_2424 = relay.TupleGetItem(func_1171_call(), 2)
call_2425 = relay.TupleGetItem(func_1173_call(), 2)
func_753_call = mod.get_global_var('func_753')
func_755_call = mutated_mod.get_global_var('func_755')
call_2426 = func_753_call()
call_2427 = func_753_call()
bop_2443 = relay.minimum(uop_2417.astype('float32'), var_2369.astype('float32')) # shape=(2, 7, 225)
bop_2446 = relay.minimum(uop_2419.astype('float32'), var_2369.astype('float32')) # shape=(2, 7, 225)
func_1119_call = mod.get_global_var('func_1119')
func_1120_call = mutated_mod.get_global_var('func_1120')
call_2447 = relay.TupleGetItem(func_1119_call(), 0)
call_2448 = relay.TupleGetItem(func_1120_call(), 0)
output = relay.Tuple([call_2322,call_2367,const_2368,const_2370,uop_2373,call_2420,call_2424,call_2426,bop_2443,call_2447,])
output2 = relay.Tuple([call_2323,call_2371,const_2368,const_2370,uop_2375,call_2421,call_2425,call_2427,bop_2446,call_2448,])
func_2453 = relay.Function([var_2369,], output)
mod['func_2453'] = func_2453
mod = relay.transform.InferType()(mod)
var_2454 = relay.var("var_2454", dtype = "float32", shape = (225,))#candidate|2454|(225,)|var|float32
output = func_2453(var_2454)
func_2455 = relay.Function([var_2454], output)
mutated_mod['func_2455'] = func_2455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1489_call = mod.get_global_var('func_1489')
func_1490_call = mutated_mod.get_global_var('func_1490')
call_2466 = relay.TupleGetItem(func_1489_call(), 0)
call_2467 = relay.TupleGetItem(func_1490_call(), 0)
func_1460_call = mod.get_global_var('func_1460')
func_1462_call = mutated_mod.get_global_var('func_1462')
call_2472 = relay.TupleGetItem(func_1460_call(), 2)
call_2473 = relay.TupleGetItem(func_1462_call(), 2)
output = relay.Tuple([call_2466,call_2472,])
output2 = relay.Tuple([call_2467,call_2473,])
func_2480 = relay.Function([], output)
mod['func_2480'] = func_2480
mod = relay.transform.InferType()(mod)
output = func_2480()
func_2481 = relay.Function([], output)
mutated_mod['func_2481'] = func_2481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1324_call = mod.get_global_var('func_1324')
func_1325_call = mutated_mod.get_global_var('func_1325')
call_2527 = relay.TupleGetItem(func_1324_call(), 0)
call_2528 = relay.TupleGetItem(func_1325_call(), 0)
output = relay.Tuple([call_2527,])
output2 = relay.Tuple([call_2528,])
func_2563 = relay.Function([], output)
mod['func_2563'] = func_2563
mod = relay.transform.InferType()(mod)
output = func_2563()
func_2564 = relay.Function([], output)
mutated_mod['func_2564'] = func_2564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1887_call = mod.get_global_var('func_1887')
func_1889_call = mutated_mod.get_global_var('func_1889')
call_2698 = relay.TupleGetItem(func_1887_call(), 1)
call_2699 = relay.TupleGetItem(func_1889_call(), 1)
output = call_2698
output2 = call_2699
func_2731 = relay.Function([], output)
mod['func_2731'] = func_2731
mod = relay.transform.InferType()(mod)
output = func_2731()
func_2732 = relay.Function([], output)
mutated_mod['func_2732'] = func_2732
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2210_call = mod.get_global_var('func_2210')
func_2212_call = mutated_mod.get_global_var('func_2212')
call_2733 = relay.TupleGetItem(func_2210_call(), 1)
call_2734 = relay.TupleGetItem(func_2212_call(), 1)
output = call_2733
output2 = call_2734
func_2759 = relay.Function([], output)
mod['func_2759'] = func_2759
mod = relay.transform.InferType()(mod)
mutated_mod['func_2759'] = func_2759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2759_call = mutated_mod.get_global_var('func_2759')
call_2760 = func_2759_call()
output = call_2760
func_2761 = relay.Function([], output)
mutated_mod['func_2761'] = func_2761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2563_call = mod.get_global_var('func_2563')
func_2564_call = mutated_mod.get_global_var('func_2564')
call_2797 = relay.TupleGetItem(func_2563_call(), 0)
call_2798 = relay.TupleGetItem(func_2564_call(), 0)
func_1691_call = mod.get_global_var('func_1691')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_2805 = relay.TupleGetItem(func_1691_call(), 1)
call_2806 = relay.TupleGetItem(func_1693_call(), 1)
var_2812 = relay.var("var_2812", dtype = "int8", shape = (5, 10, 9))#candidate|2812|(5, 10, 9)|var|int8
bop_2813 = relay.less(call_2805.astype('bool'), relay.reshape(var_2812.astype('bool'), relay.shape_of(call_2805))) # shape=(5, 10, 9)
bop_2816 = relay.less(call_2806.astype('bool'), relay.reshape(var_2812.astype('bool'), relay.shape_of(call_2806))) # shape=(5, 10, 9)
func_675_call = mod.get_global_var('func_675')
func_677_call = mutated_mod.get_global_var('func_677')
call_2820 = func_675_call()
call_2821 = func_675_call()
bop_2827 = relay.less(call_2820.astype('bool'), relay.reshape(call_2797.astype('bool'), relay.shape_of(call_2820))) # shape=(2, 7, 1)
bop_2830 = relay.less(call_2821.astype('bool'), relay.reshape(call_2798.astype('bool'), relay.shape_of(call_2821))) # shape=(2, 7, 1)
func_2011_call = mod.get_global_var('func_2011')
func_2014_call = mutated_mod.get_global_var('func_2014')
const_2837 = relay.const([-0.707657,-7.136717,5.155803,5.418981,3.429157,3.260617,4.107876,7.549215,9.168576,-4.780967,-7.900899,-4.251190,-7.708116,1.730553,-5.187533,-1.134069,-0.856772,-2.330637,7.140124,2.963091,-1.223115,-4.598071,0.822670,3.050971,9.649272,4.149345,0.514637,-2.506484,8.134317,1.279595,7.235859,-3.124306,-4.256909,8.716188,-9.895566,-5.881551,-1.379818,2.522941,-9.130562,-5.208109,-9.243511,3.409912,-3.499630,-1.650990,3.773612,6.710397,7.597204,-2.836353,-8.334588,-8.637072,-7.972815,-0.239429,3.482744,-1.051190,-0.795569,-0.283498,-5.139493,-0.755135,9.697118,-7.078311,-5.714080,-2.061330,9.314633,6.336472,-3.170174,2.933842,-4.179695,6.071866,8.291524,0.230797,3.819574,-9.510702,8.820813,-7.489654,8.274266,6.368943,-3.438759,-7.185505,-7.065733,-1.907933,2.214807,6.572002,0.788753,8.015444,-9.137295,-8.325248,-7.522827,4.875301,6.684696,6.127213,3.336196,-5.656171,-0.555818,3.828254,-2.127041,0.889792,3.375921,5.966226,-6.337465,7.922647,8.498717,-9.742050,6.421410,3.671461,5.303194,6.295711,7.336647,-2.577780,-7.138557,-2.857946,9.118430,-3.636951,-7.126819,9.060323,0.704721,3.506465,-7.582826,-2.200142,1.139346,-4.590709,-9.873360,1.843377,0.766600,7.874780,-0.770038,-2.764284,-1.598169,-8.634032,-8.298974,1.753128,9.998115,-4.382220,-2.239155,5.622527,-2.916779,-8.756829,3.792105,-9.438847,4.434586,9.711001,5.707798,-4.453643,-9.010633,-6.663964,-9.279553,-3.664865,-9.783943,-7.373096,-8.839219,3.584651,1.227852,7.890658,9.240822,-7.680372,-4.912384,-4.962150,8.384573,3.239262,-1.855375,7.827380,7.388323,-0.828387,-8.545318,-7.157933,-3.612199,-9.573476,5.208748,-9.101549,5.888585,1.160084,-6.051107,-9.469948,-0.145400,-1.468572,7.864729,-4.481579,5.190901,8.744858,2.650871,-2.182341,3.891758,6.261445,2.152625,6.365166,-3.920606,-0.448277,0.486929,4.982881,-3.073694,-9.427970,9.920142,-7.769068,0.354037,-7.288930,1.131270,-2.759876,3.163044,1.287766,2.682883,-1.824867,4.418262,5.921413,5.551736,5.843188,-3.025300,0.398840,-4.497990,-3.890510,5.585133,-8.387908], dtype = "float32")#candidate|2837|(210,)|const|float32
call_2836 = relay.TupleGetItem(func_2011_call(relay.reshape(const_2837.astype('float32'), [2, 7, 15])), 1)
call_2838 = relay.TupleGetItem(func_2014_call(relay.reshape(const_2837.astype('float32'), [2, 7, 15])), 1)
output = relay.Tuple([bop_2813,bop_2827,call_2836,const_2837,])
output2 = relay.Tuple([bop_2816,bop_2830,call_2838,const_2837,])
func_2854 = relay.Function([var_2812,], output)
mod['func_2854'] = func_2854
mod = relay.transform.InferType()(mod)
mutated_mod['func_2854'] = func_2854
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2855 = relay.var("var_2855", dtype = "int8", shape = (5, 10, 9))#candidate|2855|(5, 10, 9)|var|int8
func_2854_call = mutated_mod.get_global_var('func_2854')
call_2856 = func_2854_call(var_2855)
output = call_2856
func_2857 = relay.Function([var_2855], output)
mutated_mod['func_2857'] = func_2857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2731_call = mod.get_global_var('func_2731')
func_2732_call = mutated_mod.get_global_var('func_2732')
call_2915 = func_2731_call()
call_2916 = func_2731_call()
output = relay.Tuple([call_2915,])
output2 = relay.Tuple([call_2916,])
func_2933 = relay.Function([], output)
mod['func_2933'] = func_2933
mod = relay.transform.InferType()(mod)
output = func_2933()
func_2934 = relay.Function([], output)
mutated_mod['func_2934'] = func_2934
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1264_call = mod.get_global_var('func_1264')
func_1265_call = mutated_mod.get_global_var('func_1265')
call_2990 = relay.TupleGetItem(func_1264_call(), 1)
call_2991 = relay.TupleGetItem(func_1265_call(), 1)
var_2997 = relay.var("var_2997", dtype = "float32", shape = (2, 7, 10))#candidate|2997|(2, 7, 10)|var|float32
bop_2998 = relay.bitwise_and(call_2990.astype('uint16'), var_2997.astype('uint16')) # shape=(2, 7, 10)
bop_3001 = relay.bitwise_and(call_2991.astype('uint16'), var_2997.astype('uint16')) # shape=(2, 7, 10)
output = bop_2998
output2 = bop_3001
func_3017 = relay.Function([var_2997,], output)
mod['func_3017'] = func_3017
mod = relay.transform.InferType()(mod)
var_3018 = relay.var("var_3018", dtype = "float32", shape = (2, 7, 10))#candidate|3018|(2, 7, 10)|var|float32
output = func_3017(var_3018)
func_3019 = relay.Function([var_3018], output)
mutated_mod['func_3019'] = func_3019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1691_call = mod.get_global_var('func_1691')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_3066 = relay.TupleGetItem(func_1691_call(), 0)
call_3067 = relay.TupleGetItem(func_1693_call(), 0)
output = relay.Tuple([call_3066,])
output2 = relay.Tuple([call_3067,])
func_3084 = relay.Function([], output)
mod['func_3084'] = func_3084
mod = relay.transform.InferType()(mod)
mutated_mod['func_3084'] = func_3084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3084_call = mutated_mod.get_global_var('func_3084')
call_3085 = func_3084_call()
output = call_3085
func_3086 = relay.Function([], output)
mutated_mod['func_3086'] = func_3086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2210_call = mod.get_global_var('func_2210')
func_2212_call = mutated_mod.get_global_var('func_2212')
call_3090 = relay.TupleGetItem(func_2210_call(), 1)
call_3091 = relay.TupleGetItem(func_2212_call(), 1)
output = call_3090
output2 = call_3091
func_3092 = relay.Function([], output)
mod['func_3092'] = func_3092
mod = relay.transform.InferType()(mod)
mutated_mod['func_3092'] = func_3092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3092_call = mutated_mod.get_global_var('func_3092')
call_3093 = func_3092_call()
output = call_3093
func_3094 = relay.Function([], output)
mutated_mod['func_3094'] = func_3094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_861_call = mod.get_global_var('func_861')
func_862_call = mutated_mod.get_global_var('func_862')
call_3149 = relay.TupleGetItem(func_861_call(), 0)
call_3150 = relay.TupleGetItem(func_862_call(), 0)
func_675_call = mod.get_global_var('func_675')
func_677_call = mutated_mod.get_global_var('func_677')
call_3157 = func_675_call()
call_3158 = func_675_call()
output = relay.Tuple([call_3149,call_3157,])
output2 = relay.Tuple([call_3150,call_3158,])
func_3181 = relay.Function([], output)
mod['func_3181'] = func_3181
mod = relay.transform.InferType()(mod)
output = func_3181()
func_3182 = relay.Function([], output)
mutated_mod['func_3182'] = func_3182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1171_call = mod.get_global_var('func_1171')
func_1173_call = mutated_mod.get_global_var('func_1173')
call_3220 = relay.TupleGetItem(func_1171_call(), 1)
call_3221 = relay.TupleGetItem(func_1173_call(), 1)
output = relay.Tuple([call_3220,])
output2 = relay.Tuple([call_3221,])
func_3224 = relay.Function([], output)
mod['func_3224'] = func_3224
mod = relay.transform.InferType()(mod)
output = func_3224()
func_3225 = relay.Function([], output)
mutated_mod['func_3225'] = func_3225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1324_call = mod.get_global_var('func_1324')
func_1325_call = mutated_mod.get_global_var('func_1325')
call_3280 = relay.TupleGetItem(func_1324_call(), 0)
call_3281 = relay.TupleGetItem(func_1325_call(), 0)
output = call_3280
output2 = call_3281
func_3291 = relay.Function([], output)
mod['func_3291'] = func_3291
mod = relay.transform.InferType()(mod)
mutated_mod['func_3291'] = func_3291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3291_call = mutated_mod.get_global_var('func_3291')
call_3292 = func_3291_call()
output = call_3292
func_3293 = relay.Function([], output)
mutated_mod['func_3293'] = func_3293
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1171_call = mod.get_global_var('func_1171')
func_1173_call = mutated_mod.get_global_var('func_1173')
call_3360 = relay.TupleGetItem(func_1171_call(), 1)
call_3361 = relay.TupleGetItem(func_1173_call(), 1)
output = relay.Tuple([call_3360,])
output2 = relay.Tuple([call_3361,])
func_3370 = relay.Function([], output)
mod['func_3370'] = func_3370
mod = relay.transform.InferType()(mod)
output = func_3370()
func_3371 = relay.Function([], output)
mutated_mod['func_3371'] = func_3371
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3181_call = mod.get_global_var('func_3181')
func_3182_call = mutated_mod.get_global_var('func_3182')
call_3417 = relay.TupleGetItem(func_3181_call(), 0)
call_3418 = relay.TupleGetItem(func_3182_call(), 0)
uop_3419 = relay.atanh(call_3417.astype('float32')) # shape=(2, 7, 1)
uop_3421 = relay.atanh(call_3418.astype('float32')) # shape=(2, 7, 1)
bop_3426 = relay.minimum(uop_3419.astype('uint16'), relay.reshape(call_3417.astype('uint16'), relay.shape_of(uop_3419))) # shape=(2, 7, 1)
bop_3429 = relay.minimum(uop_3421.astype('uint16'), relay.reshape(call_3418.astype('uint16'), relay.shape_of(uop_3421))) # shape=(2, 7, 1)
output = bop_3426
output2 = bop_3429
func_3438 = relay.Function([], output)
mod['func_3438'] = func_3438
mod = relay.transform.InferType()(mod)
mutated_mod['func_3438'] = func_3438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3438_call = mutated_mod.get_global_var('func_3438')
call_3439 = func_3438_call()
output = call_3439
func_3440 = relay.Function([], output)
mutated_mod['func_3440'] = func_3440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1778_call = mod.get_global_var('func_1778')
func_1780_call = mutated_mod.get_global_var('func_1780')
call_3566 = relay.TupleGetItem(func_1778_call(), 0)
call_3567 = relay.TupleGetItem(func_1780_call(), 0)
func_3370_call = mod.get_global_var('func_3370')
func_3371_call = mutated_mod.get_global_var('func_3371')
call_3573 = relay.TupleGetItem(func_3370_call(), 0)
call_3574 = relay.TupleGetItem(func_3371_call(), 0)
func_1095_call = mod.get_global_var('func_1095')
func_1097_call = mutated_mod.get_global_var('func_1097')
call_3588 = relay.TupleGetItem(func_1095_call(), 1)
call_3589 = relay.TupleGetItem(func_1097_call(), 1)
output = relay.Tuple([call_3566,call_3573,call_3588,])
output2 = relay.Tuple([call_3567,call_3574,call_3589,])
func_3597 = relay.Function([], output)
mod['func_3597'] = func_3597
mod = relay.transform.InferType()(mod)
output = func_3597()
func_3598 = relay.Function([], output)
mutated_mod['func_3598'] = func_3598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2272_call = mod.get_global_var('func_2272')
func_2274_call = mutated_mod.get_global_var('func_2274')
call_3626 = relay.TupleGetItem(func_2272_call(), 0)
call_3627 = relay.TupleGetItem(func_2274_call(), 0)
output = relay.Tuple([call_3626,])
output2 = relay.Tuple([call_3627,])
func_3643 = relay.Function([], output)
mod['func_3643'] = func_3643
mod = relay.transform.InferType()(mod)
mutated_mod['func_3643'] = func_3643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3643_call = mutated_mod.get_global_var('func_3643')
call_3644 = func_3643_call()
output = call_3644
func_3645 = relay.Function([], output)
mutated_mod['func_3645'] = func_3645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1324_call = mod.get_global_var('func_1324')
func_1325_call = mutated_mod.get_global_var('func_1325')
call_3646 = relay.TupleGetItem(func_1324_call(), 0)
call_3647 = relay.TupleGetItem(func_1325_call(), 0)
output = call_3646
output2 = call_3647
func_3649 = relay.Function([], output)
mod['func_3649'] = func_3649
mod = relay.transform.InferType()(mod)
mutated_mod['func_3649'] = func_3649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3649_call = mutated_mod.get_global_var('func_3649')
call_3650 = func_3649_call()
output = call_3650
func_3651 = relay.Function([], output)
mutated_mod['func_3651'] = func_3651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2759_call = mod.get_global_var('func_2759')
func_2761_call = mutated_mod.get_global_var('func_2761')
call_3676 = func_2759_call()
call_3677 = func_2759_call()
func_3092_call = mod.get_global_var('func_3092')
func_3094_call = mutated_mod.get_global_var('func_3094')
call_3680 = func_3092_call()
call_3681 = func_3092_call()
func_1819_call = mod.get_global_var('func_1819')
func_1823_call = mutated_mod.get_global_var('func_1823')
var_3686 = relay.var("var_3686", dtype = "uint32", shape = (600,))#candidate|3686|(600,)|var|uint32
var_3687 = relay.var("var_3687", dtype = "int8", shape = (150, 3))#candidate|3687|(150, 3)|var|int8
const_3688 = relay.const([[-1.463846,-5.873420,6.953748,3.273168,-9.244067,-4.193930,7.181128,-5.155677,4.601256,-1.188377,-2.462543,5.860722],[-5.242711,-8.724355,-9.022783,5.600758,-3.345002,-5.940661,-6.901683,-8.730276,4.032268,4.817305,-8.240274,8.552256],[7.741988,-3.706735,-2.188167,2.423128,-2.365247,-5.481342,5.241637,7.181792,1.136028,4.118150,9.653532,-0.383746],[-0.294453,1.394016,9.870073,-8.956151,-6.585421,-5.203205,-4.623272,1.315075,-9.778320,3.556208,3.589415,2.701661],[-1.589969,-4.296146,-5.133927,6.744709,-3.299674,-6.080896,8.293524,3.083825,5.610418,-9.455381,7.670035,-4.373694],[4.199215,7.079882,-8.559124,-5.541875,7.686538,-3.891430,1.122385,-3.748333,-5.829350,-1.803592,-9.257010,4.847637],[0.814426,6.818705,-8.475296,-1.292652,-3.512724,-7.092484,2.497941,6.665312,-8.851350,-2.779282,2.404009,9.371457],[4.837197,0.401802,5.087761,4.268839,3.791124,-4.879263,-2.506484,0.599195,-0.411649,1.314692,-7.301147,5.204855],[-7.956869,8.006364,-8.900839,8.476532,-7.094443,9.156472,-3.967208,-7.918747,-5.791480,8.571402,-8.798413,2.568798],[-1.374083,-0.205390,7.037554,9.236934,7.964565,-6.225921,-3.937532,-3.063788,-2.035589,-1.586398,-0.261665,-7.807918],[7.449767,-2.229227,1.824861,7.218424,-4.965019,-1.174107,7.699735,-4.075918,-7.879163,-5.747052,-4.936844,2.426835],[0.982210,0.032997,6.262832,-4.994856,0.139488,-3.181039,-3.305263,2.133989,1.967487,-5.420164,1.365862,6.642064],[9.689466,-1.365974,-5.295459,3.975413,-1.584099,-0.824648,-4.499950,-2.388782,0.235463,-1.894750,-1.020778,-2.769321],[-9.395349,-7.486420,1.805934,1.008946,-9.614347,4.954421,-3.437017,-0.851299,4.154489,-4.502903,9.249135,-1.389496],[7.694007,-9.729247,-5.934218,6.179990,9.961514,-0.010766,2.208321,-8.592988,-7.001668,3.357948,-7.842049,1.928465],[-2.892803,0.614086,-6.619787,-0.380459,2.172608,-8.179753,5.718116,-9.120538,6.447475,-9.064339,-9.217089,-2.240659],[-9.552941,7.753997,4.426063,-8.843095,-2.451917,4.943398,9.187147,-1.299111,-5.932011,-5.132564,-2.544928,0.132468],[-1.020970,7.872419,-1.095917,6.860745,1.270166,2.881930,7.496946,-7.254232,6.343359,-4.641751,5.020958,1.203417],[1.443441,6.223640,-6.603819,-4.618562,-0.442833,-9.589006,7.971178,5.732676,-5.414238,-8.189478,4.310458,-0.666547],[-4.859567,4.896197,9.440146,-6.628728,6.497984,1.431645,-1.513724,-2.863909,7.615849,3.880071,-3.841727,6.608972],[9.572730,-5.296080,-0.389845,1.306216,3.796737,-7.331240,-1.473069,-6.925390,-6.201759,6.710753,9.534669,-1.665652],[-2.479852,2.665800,-4.807852,-0.405192,-2.848144,-6.997403,8.258667,-4.271346,0.816962,9.542858,8.638969,4.330872],[1.875337,-4.215233,-3.026720,4.856454,-1.766993,5.236216,6.438612,-5.381638,-1.520385,-0.128039,-4.571370,-0.698432],[1.530016,3.920071,7.979298,8.538436,-2.729979,7.228362,-6.791586,9.520910,-4.839293,9.928454,-3.422791,8.909787],[3.150385,-1.487555,-1.660082,7.339170,1.237251,-9.100853,4.579855,0.551544,8.597424,-1.015354,-5.365317,-4.506657],[-2.833129,-6.046380,4.509478,3.187058,-7.462869,2.752417,-7.642533,-6.384053,0.689068,3.233680,-6.528081,-9.282699],[6.203652,3.432481,2.053065,-2.031505,-8.334174,-3.218907,9.384578,-5.730345,-3.558534,-6.266176,-5.085480,-8.754360],[-1.684080,-3.621910,-5.543239,-9.265625,2.012925,8.915950,-8.934707,-1.730628,2.413840,-9.203079,-3.105637,-3.040722],[-7.872002,7.640864,0.263205,1.549768,3.884414,4.794565,-5.954585,-3.298699,9.330590,-0.063056,7.747930,-4.829229],[-4.727625,5.554243,8.400153,8.826136,6.644868,-8.645222,-9.313201,-8.153570,8.371377,5.866705,6.032189,3.608815],[-6.775976,-2.715559,-8.430055,-1.722040,-0.513516,6.028305,4.883652,5.510873,-6.409850,2.061788,0.005268,-7.035777],[9.577175,6.893298,4.979424,-1.677789,-8.711290,-0.324069,4.821036,2.202314,-7.452083,-6.009591,4.305896,-2.598622],[8.212328,-1.323223,5.759669,-1.787369,5.262590,-2.210961,-6.669085,-5.744663,2.274132,-4.370803,9.355076,-1.587655],[-7.557226,8.527365,8.439147,5.196420,7.365425,4.299545,8.635779,-5.954148,0.090936,9.935578,7.438641,8.373697],[-6.758877,9.027703,5.295509,-0.385491,-9.331365,-9.060351,5.236761,5.597262,3.587542,-7.951781,-0.274130,2.511311],[6.989659,7.818060,-4.042617,4.560308,-1.093730,-2.687313,1.631792,-6.916292,-2.277939,5.311741,-1.723642,3.742528],[4.672834,-4.798935,-2.247930,-7.699034,2.715039,-4.805789,-6.009281,-5.716969,-2.650674,-8.080254,2.226602,-9.952515],[8.123218,-3.162893,-6.917963,-6.095831,5.705883,4.427219,-2.096099,9.283078,5.969917,-5.783711,1.802089,8.530637],[8.994374,9.129978,-7.628547,8.638054,9.417904,9.780849,3.736777,-0.873622,7.515212,-9.090293,6.509077,7.867992],[3.871118,-3.479947,-7.467876,-8.768986,8.305366,5.524715,9.358635,-4.905098,-0.035817,-0.732864,8.886860,-2.889581],[-7.058622,-4.427013,-3.891415,4.960385,0.105212,-0.330147,7.959570,-8.472902,0.372155,-7.687120,-8.429341,7.475192],[-3.539872,-1.787542,-2.709138,-0.170140,7.590899,-0.931028,-4.304608,1.222109,6.864145,-0.750466,-4.394841,-4.512950],[-0.102339,5.638001,1.973840,1.357042,-4.702341,3.883602,-2.555046,-3.807721,-7.756707,4.646461,-1.982987,6.904392],[-0.214218,-4.685175,-4.764999,-1.095687,2.951699,4.591275,0.989257,-3.242152,-0.962252,-2.155977,-2.912682,-0.682425],[-4.147550,3.082005,-0.089892,-5.909812,-4.142177,8.122679,6.507923,5.827707,6.967461,9.305238,6.210444,7.631143],[3.388335,-3.660423,-9.202149,3.142234,-6.714400,6.443612,5.092212,-0.913850,-0.702407,-2.882536,0.296772,-6.108848],[-2.033799,2.487961,3.066588,6.592639,5.270315,-5.100437,-2.820341,-0.145115,8.696145,1.806828,7.044819,-5.612617],[0.538736,-3.267626,1.721140,-5.921163,-1.023776,0.285964,-8.165680,4.928499,6.433611,9.309645,6.986053,-4.409293],[5.054918,7.736121,2.797598,-6.955348,-5.087514,-4.874617,7.764422,1.744274,-3.120394,6.272253,6.376081,-8.436161],[7.835614,-6.399687,4.901715,2.186570,-7.644352,-7.523088,-8.422571,-7.243308,6.238303,-7.635393,8.347369,-5.817864],[7.308446,-0.216227,-2.127004,6.752764,-5.229085,-4.770870,-5.628867,-9.286948,-8.262198,0.002863,4.999688,7.581835],[-5.945549,8.162780,3.443330,2.660506,-1.204744,7.515744,9.515369,-9.852115,-3.499572,7.578656,-8.026593,0.971602],[-0.854981,4.940595,5.695387,-7.297504,7.237221,7.234695,-4.272498,2.342615,0.826462,1.922855,9.018234,-3.987219],[7.977420,-2.821464,-2.839378,-2.578734,-3.137889,-4.795241,5.026241,3.303303,8.468908,2.833640,-1.224610,-4.903499],[-0.785921,-0.936854,1.497535,1.398319,-2.913380,-1.105323,-7.613947,-4.007759,-6.364405,-8.177487,8.984795,-2.951589],[-2.278702,-5.300408,-2.738146,-0.547667,2.467540,-5.214445,-4.141144,5.294253,-2.445899,2.674816,-9.217669,1.144036],[-9.298786,-3.636120,-7.136820,-8.496106,2.010578,7.985592,1.705886,-2.110279,-3.204042,9.847230,-7.097156,6.418958],[-1.510854,8.283329,-3.774844,-6.229934,-9.593961,4.897315,0.394098,-3.570987,-8.714065,1.978075,8.688412,-9.246723],[-4.536535,-1.586879,-4.915099,1.991286,-9.900461,-2.380146,-1.821209,-7.168522,6.893584,2.041703,7.294696,6.865505],[5.041115,-8.138412,-3.518030,-4.307047,-6.933578,-8.761390,-3.636670,-9.122756,-5.114345,-9.079815,7.450210,-3.824622],[-2.818264,9.485745,0.872221,4.546934,8.606249,9.993167,3.210994,1.821264,9.852570,-3.956868,0.236804,-9.762165],[5.720748,-8.418105,2.621218,-1.447562,-7.223717,-7.059319,-1.965761,-0.482881,8.418726,-4.322263,6.366630,-9.569298],[3.723367,7.797445,9.059461,-4.470930,-4.748490,1.087024,4.403706,7.882181,-4.332566,8.182538,4.097002,-1.183792],[-6.704289,6.576121,-7.580037,-8.369050,6.015703,9.471841,3.245255,9.678403,-2.443481,-6.386662,-0.930493,-6.275230],[1.049873,-9.467737,3.962373,1.198950,9.696602,-1.868080,-5.239463,4.301245,-8.901434,8.222208,-6.299521,2.116034],[7.595102,8.475994,4.453570,-6.429306,7.014486,5.861192,-4.559064,-7.211611,-3.530175,1.935265,9.827355,-5.186157],[5.391414,-8.758161,-4.000375,6.846127,3.918531,-9.573653,-0.494910,5.275179,1.119755,-5.375639,8.548658,6.226564],[2.113860,-7.976581,7.652329,-4.630446,-5.865924,-4.728808,-6.914440,4.196542,-2.767502,-4.490647,-4.528335,5.343884],[9.855309,4.654090,-5.297941,-3.141640,-7.740305,3.395308,7.682435,-1.350173,-8.450483,-5.511786,-6.137314,-3.084593],[0.508518,8.215497,-4.298327,7.914252,0.537462,-0.886201,3.961868,7.511458,4.279861,9.644230,2.179629,2.080167],[6.297723,-3.250402,1.837416,-1.756360,-6.584335,-5.731910,-6.674519,-4.707783,8.602355,-8.171163,9.785706,-2.079107],[-3.046669,0.143042,0.729453,1.022483,-8.812859,0.561091,-1.168074,6.995477,7.002704,7.904994,2.520460,6.972201],[-6.869350,-2.188135,-3.853152,-5.026338,-1.712899,-4.391707,-9.471754,-2.019786,5.599210,-6.725315,-8.630591,-3.413514],[-8.800059,1.951378,3.935572,-6.210189,-0.102547,7.265667,6.852697,1.743614,0.977317,4.744945,0.362091,2.137328],[9.954158,-4.079973,1.827216,-7.476298,-0.047389,0.107033,-3.772836,8.293348,-2.735766,7.966837,6.453732,-3.668855],[-5.917297,-6.114363,2.168087,0.747402,-1.613912,-9.937151,-3.236597,3.651084,9.821540,6.576655,-6.633496,-2.064149],[3.729931,-4.651889,6.244734,-0.856268,-6.379305,1.031870,-5.048326,7.087488,6.381490,-9.873935,-4.008365,-9.538567],[-5.404000,6.701471,5.848933,-6.888076,-1.858895,5.842272,0.831687,1.454609,-8.050759,9.333246,9.994293,4.401207],[4.182934,2.239177,2.219058,6.547876,7.819233,-7.761275,-0.952231,5.710099,1.556832,-0.805792,-2.765860,6.284245],[0.209027,1.517850,0.930245,7.152397,-0.698166,-6.930333,-4.517129,-9.784670,-4.758379,-7.970829,4.684978,7.845463],[-4.084882,5.910334,-5.503332,-5.687926,9.859280,-5.331251,-6.895975,4.684928,-4.914770,8.355167,2.913133,-2.542300],[-6.377529,8.010570,5.575865,2.941496,-3.213915,-6.082148,9.758359,-7.670795,2.377523,2.809566,-5.964877,-9.491337],[-5.817619,-8.503730,4.229714,5.474866,9.540219,4.986135,-5.504466,7.865659,7.885400,5.891680,-9.877095,-6.919264],[-4.785800,3.025403,-6.329704,-9.460505,3.523613,0.372943,0.641673,1.971707,2.791016,1.170283,7.171449,-1.836885],[4.568934,3.999296,-1.333389,5.564764,2.016230,2.498213,-9.689330,-1.270317,-0.771271,5.851903,-4.387438,4.103092],[1.586266,2.038412,0.344770,-4.339056,3.614676,-1.643182,4.786890,2.509199,-4.616311,-3.446138,-8.539300,4.258821],[-5.009691,-0.355360,4.170702,-8.797844,4.165823,6.504674,-7.660305,8.239400,7.212507,3.277803,8.690633,8.757335],[7.778568,-9.423413,-2.882297,2.734672,-4.550913,8.832869,0.735271,9.370501,-7.510546,7.096389,-4.886685,-3.421866],[-9.369488,-4.651435,-2.058458,4.882261,8.087635,5.287408,0.280776,1.173719,0.847999,6.472043,-0.011218,0.160507],[3.406767,5.435380,4.160112,2.182181,7.604622,3.179857,6.645497,-8.801980,-3.573687,-1.292823,-8.467550,-8.377863],[0.821223,-5.578032,-8.258418,-9.346708,-2.887336,7.178839,1.237156,0.006425,-9.682250,4.845492,3.579776,-3.784835],[4.812758,-6.118522,-8.042813,0.551285,-8.974381,-7.233481,5.770012,4.686242,-6.655577,3.519128,7.113191,6.795287],[5.170260,-2.951470,-0.062200,7.661015,7.682102,4.594603,-7.125922,8.291735,-9.905957,7.069842,-3.426917,3.918297],[7.512013,2.166000,5.707713,-8.996886,4.308072,5.427775,4.891819,2.457156,-2.353710,6.498817,-1.012812,-8.735097],[-5.987643,-8.802323,-2.358721,2.423060,6.703282,-8.635794,7.362260,1.221458,3.476264,-7.327353,1.174076,-6.407822],[-1.152637,-8.476939,-2.403470,6.497602,-4.377428,-6.377421,7.328841,-1.056497,-2.463586,8.398070,4.750231,-8.553848],[-2.649718,-9.365815,-4.728002,8.013392,-5.445039,8.508828,-7.021364,6.957572,3.197565,6.847563,3.908847,8.473726],[6.767889,-0.881139,8.904792,6.650477,4.078552,-8.873733,-3.490113,5.612886,9.620462,-5.955783,9.052962,6.614139],[6.623676,-0.278884,-9.312232,-3.515794,-8.221679,8.545989,5.804795,1.553923,-3.372516,-6.752642,-1.432419,4.662557],[3.586965,5.945747,4.093245,4.300750,-0.449820,7.037261,8.747514,-3.470824,-4.768418,0.915412,-1.397339,8.979046],[-5.241498,-4.114382,4.171163,1.940855,9.670581,3.765480,6.841459,9.447964,-7.805195,-2.900006,-8.120467,-0.525283],[-4.826643,-2.081751,-1.190938,2.191484,8.561650,0.876629,6.696115,8.247729,-0.697879,2.767948,2.717269,9.473044],[-4.542398,0.552938,-0.479448,5.590131,-3.973065,8.794816,2.143315,2.216175,-6.876649,8.235387,7.308023,-0.003114],[-5.288568,3.092631,-4.522485,1.389547,3.198273,5.850444,-4.946052,-4.923225,-6.034815,-4.419225,8.802890,3.621325],[-8.802463,0.909870,7.098517,5.717601,-3.323066,-8.061165,4.775095,8.819383,-8.686653,-5.212253,0.123200,7.853656],[9.244811,-3.630853,-7.580732,-2.741949,-1.699335,-4.391387,-0.043069,9.945938,9.968948,4.803034,-2.418786,4.628494],[-7.955999,7.538710,-1.728002,7.858128,-0.061621,-3.161872,1.270369,-8.185821,5.191466,-0.771881,-3.777685,-0.581491],[3.271073,8.268250,-4.363912,-1.605046,-8.991412,-8.350668,1.523940,-4.346433,8.746953,-5.460015,-9.324266,5.136123],[3.235190,2.040551,4.296107,0.803110,6.256125,-2.524013,8.596034,-3.135726,8.168684,0.141842,1.884538,-5.539089],[-5.597498,9.191165,6.552574,-7.350198,-4.947514,2.899870,3.796846,-3.400946,0.525810,-1.137273,-7.886729,-4.486437],[-5.802037,-3.816271,-0.741696,-6.122913,7.730267,6.125254,-6.930631,6.610260,6.604030,3.426293,-1.832719,4.618457],[-0.795761,-3.789976,5.723648,-8.639157,-3.960053,2.679459,-8.446671,-7.333414,7.289217,-0.700236,4.538489,0.547924],[-5.409605,-6.044138,-3.236629,-6.092230,2.596335,5.184090,-6.432190,-3.391668,-7.686399,8.413520,-0.930459,-8.280694],[3.667897,0.151088,3.453858,3.768195,7.394362,-4.020269,0.795721,5.165116,2.648668,4.175321,-4.426686,5.968330],[8.287491,7.263413,-9.418410,-8.635142,8.918019,-1.347052,-9.468583,-1.003441,7.490875,4.253169,-3.994604,-1.693516],[-8.999268,3.300772,5.927870,2.285888,9.296750,-1.031959,7.158519,5.331874,0.292795,5.328752,2.333286,7.588247],[-6.856673,9.381961,3.866450,-4.575874,-0.578130,0.811444,-8.090352,-6.523092,2.511669,4.968642,1.883043,1.337462],[9.757872,-0.160688,6.413274,4.944291,3.120486,-3.851328,-7.032487,-0.649687,-9.038215,1.806874,-1.218693,-7.405285],[-1.427414,-1.735053,-0.988733,-4.676272,-7.898703,-5.621564,3.456372,7.517160,-2.237005,2.608127,3.349832,4.807982],[2.339594,-4.212860,3.552485,-8.436567,2.870559,7.928047,-4.263604,2.527381,3.933725,-8.742930,8.181005,7.492078],[8.990072,9.092260,-4.251864,-2.605039,3.436062,7.406828,5.752493,-0.705671,1.041239,-9.851572,-0.324557,-7.070236],[9.507217,-9.409001,7.338524,0.664824,-8.520035,2.583997,7.942873,8.497988,-1.372509,7.601089,-4.128381,-0.823537],[-1.358884,8.902777,-7.026381,-8.618277,6.759373,5.182924,-3.587244,2.461805,2.560523,5.958289,2.224179,0.541916],[2.478672,3.548294,-9.310844,7.170027,1.718717,9.896526,5.361166,3.704632,-7.824411,1.947554,2.121997,-5.117882],[3.196559,-3.734882,-9.476128,-4.197630,-5.618993,5.423736,-3.802799,8.646873,1.970390,1.326237,-9.581629,0.377436],[2.285129,7.820615,-4.457035,8.041222,8.626521,-0.909118,6.918965,-2.773046,-3.035249,8.624744,-5.830579,-7.686623],[3.181865,-5.380273,8.581739,4.480563,-5.358642,6.760959,-7.033479,-0.327762,-0.993591,2.596201,-6.731757,-2.025783],[8.378573,0.904138,-0.373662,7.195956,9.512737,-5.843441,-6.109585,-7.721227,-9.039897,6.063701,-7.647603,0.044942],[-6.180776,1.415791,-5.271585,7.581173,9.701681,4.289557,1.991518,3.384727,1.314268,3.368640,4.685334,-1.675035],[2.227507,-2.066235,-9.491981,7.615371,-3.448473,3.861019,-4.929538,-1.445625,5.701887,8.333025,4.876829,9.394632],[-0.763423,-9.426512,-3.250799,-7.244363,-0.823279,-3.320138,-9.168869,4.429152,-5.207926,5.831998,8.433453,-3.825645],[3.673909,9.695764,-1.703998,4.920282,8.097490,4.155716,2.574103,-5.755263,-8.918025,-6.185742,-7.301445,-9.201949],[-4.502861,2.422452,8.349443,-3.975334,1.644431,9.771543,-5.754829,8.651417,-0.568857,-7.000516,-2.632798,1.288035],[7.335930,1.298672,0.174052,-2.870727,2.244558,-4.254671,6.442301,2.606569,-9.531772,-0.216819,-4.890425,1.307894],[-4.813830,-8.079395,-4.119703,-6.083005,8.934381,6.751852,6.259603,-6.757495,6.238422,0.085670,7.269199,3.674765],[-4.841442,-6.024724,6.633260,8.278093,1.046060,-3.987836,-7.502993,1.503660,-1.169748,-7.539327,-1.458611,-2.470204],[6.614740,-7.636710,7.927840,8.052642,-8.876713,-0.108703,3.745962,5.516481,9.441324,-5.774047,-6.261205,1.234030],[-5.180356,-6.928495,-6.026076,-2.413781,1.766074,-8.811826,-3.417642,-4.880413,4.251188,4.037502,-1.382923,-8.963553],[-2.228747,3.010699,-2.435507,-4.575866,8.953998,-5.306939,5.298529,6.019634,6.840789,1.338561,1.238852,-8.426001],[-2.804996,4.753447,4.678938,-1.873862,-6.436323,-9.086676,-9.194474,9.659612,-0.626964,1.644142,-7.584593,-1.349337],[-4.925830,-9.958228,8.781570,5.427965,-4.210660,-5.752227,-0.554587,4.594182,8.743819,2.339651,-6.398308,3.396314],[-3.174656,2.658989,4.684505,8.034658,4.412272,-7.143416,-4.384884,0.747423,-5.322155,-1.893247,-4.947530,-3.694717],[-3.155465,-4.534006,-0.489394,5.834679,-3.015320,-3.821736,-6.640864,-1.648868,4.107746,-4.788053,-3.043208,-6.519060],[6.941548,9.608281,-7.821927,0.127797,7.640745,-1.946977,0.986075,8.699626,-6.312050,-9.706183,2.604694,-1.499123],[5.554018,-5.071067,-4.926916,-9.222675,-2.275049,-6.270959,4.027869,1.486202,5.167868,7.294215,4.733170,-1.417601],[-4.687234,-0.718612,3.852491,-2.614276,0.323074,-2.349774,2.061188,3.217752,-3.560393,-7.257793,-4.957407,0.589437],[8.582066,-8.334720,3.028963,-9.702900,2.933867,3.425490,-1.592143,2.780029,-1.927032,1.654524,9.686713,0.980668],[-9.795283,0.735263,7.149499,-4.535456,9.153636,3.509478,-5.386469,-8.116642,-8.066557,-8.621778,9.683933,-2.156529],[-9.255082,2.888444,7.281200,5.232491,3.655953,-8.202441,1.969179,8.710390,9.730942,0.708310,2.981890,-9.281666],[1.883979,-5.066459,-7.658373,6.184878,-3.985493,-8.892971,6.052231,-3.522390,7.042457,-6.447632,6.299674,3.492640],[-6.639982,-4.727139,2.157201,-2.893303,-8.020029,9.253825,4.673752,2.462010,-7.961870,9.483220,6.823530,-4.367786],[-0.139640,-6.437796,-3.100400,9.871804,-6.394514,-3.844534,-8.277984,5.659571,0.310084,0.823547,3.068830,6.600171],[4.365062,9.992838,-1.402797,1.641437,-2.757134,-2.340854,4.880364,-5.262261,-8.352133,2.961735,9.966913,6.834928],[-2.624685,3.782847,1.204721,7.186151,-8.083177,7.050946,-3.264849,4.402229,-8.392399,7.857602,2.432608,-8.966965],[9.599292,-0.589542,-9.093693,2.598677,1.494510,-0.325485,4.443415,0.924072,-9.611484,-3.614968,4.733825,-0.444511],[-9.494396,5.152346,7.048877,2.036354,-2.785935,3.478983,6.933211,9.452421,0.278240,3.617085,6.113253,-1.190038],[7.013449,-9.342219,4.305166,5.684276,-6.912318,5.942475,-4.481543,-9.726023,1.293194,7.968379,4.049414,7.735877],[-8.280570,0.806048,2.720144,1.714586,6.320175,4.219493,-9.613501,-3.777505,5.937833,-8.892104,-6.772375,-3.125157],[-7.675258,-4.446801,-5.480964,4.472437,-5.684523,-5.974746,-1.991788,-5.461310,9.391491,-5.599232,-2.151209,8.367730],[3.955504,9.734246,-9.088333,6.462267,2.936371,-2.135244,9.861766,-7.415326,3.297571,7.912450,5.014299,8.315216],[0.207222,-3.209102,-1.111226,1.456747,-1.401413,1.456058,1.581451,9.719024,-0.224439,-5.074446,4.172377,9.271998],[-1.852102,5.053050,-8.527632,-9.230384,-2.690071,-8.538522,-4.023827,-1.178140,-6.747476,-7.780003,-4.191867,7.734078],[0.634745,-4.506104,-4.329114,7.809333,-2.961859,-5.279691,4.478003,-5.807609,-5.572814,-8.912321,7.259738,5.406546],[-4.832480,3.322177,0.331429,5.850884,-5.589895,-5.826282,5.005892,0.952986,-0.717167,3.275114,9.487982,0.967815],[-6.896450,-3.612918,0.895396,2.747064,9.673001,-9.079376,9.690848,-5.648495,-9.592811,2.363060,-2.159556,0.906390],[-7.341545,1.394600,4.817789,4.191963,-1.648018,0.958155,7.443908,-7.880746,5.204481,-2.522839,-2.503427,-1.782937],[7.566774,8.145001,6.584722,-6.201807,7.655591,1.153331,-8.031226,-0.699467,-5.577212,-9.508079,-2.686239,7.168843],[-0.886546,9.019525,-3.795718,1.882376,1.999122,9.322854,0.325914,-2.487089,9.114065,8.168641,7.937307,1.161484],[2.636264,9.513474,-7.858821,5.740038,-2.327298,0.009478,2.882152,-5.595041,1.241095,7.776043,3.218016,1.203892],[2.002642,7.696087,-5.223658,-8.027149,-1.850429,-9.300260,-1.715217,7.260530,-4.528509,0.354057,7.912488,-3.587372],[-0.604051,-3.074169,1.963864,-1.398329,-4.140003,7.463140,-7.194196,9.430241,-8.697228,0.808069,7.891858,1.033881],[-2.602881,4.804057,1.382450,-3.527887,5.153584,3.337338,7.369460,8.609905,1.282142,-8.593806,9.653957,2.293807],[4.474412,-6.221067,8.222550,-1.772441,2.688524,-3.232944,8.340110,-8.295290,6.321006,-7.767356,2.326049,-8.305631],[-9.996111,7.360864,-7.294238,0.184887,3.430539,0.719859,-1.385695,-1.013451,6.509965,-5.261737,-4.199920,-1.342492],[-3.867138,-9.889453,-8.515017,4.468746,9.098013,-5.789276,7.024410,-6.590558,-0.896687,6.012649,4.625332,-3.171353],[-8.673508,-0.859098,9.227202,-3.020433,5.619929,3.687971,-3.542369,-1.070667,1.553840,9.164631,4.516699,-2.154923],[5.957475,-7.423803,4.042416,-9.640716,3.137001,-5.884192,2.656277,-5.314609,9.654169,-9.278544,-0.139068,-0.219028],[-6.373329,-5.151181,1.771377,6.701208,1.018494,8.456008,-6.932436,-8.952026,-2.766008,-3.810336,-8.904389,-5.048040],[-6.457510,6.848149,-4.219139,5.615467,7.085168,-1.848435,-5.694162,-5.902372,7.459025,-1.362341,8.413351,5.875860],[-2.258954,1.710501,-8.093944,-2.542959,-8.598788,-5.081604,0.185039,4.374229,0.047856,8.008307,8.432492,7.902548],[-3.662917,-2.334404,2.695236,2.957236,8.132489,-6.702077,7.848397,5.838912,-5.389188,-3.079900,8.267162,-6.063539],[4.782258,-9.528037,5.846559,6.616415,6.002278,3.576374,2.169411,-3.475935,3.842529,-8.393002,-0.917854,4.195263],[7.661535,-5.457362,7.219447,-6.613135,4.674262,-5.381602,-6.159135,-6.871520,4.309532,-5.199482,-5.190182,-4.196950],[2.269144,-1.812314,-3.862543,-1.298360,6.832891,-2.910424,-6.271478,7.733760,2.641397,-6.439119,6.500261,5.713324],[5.182029,6.444964,8.693388,2.606270,8.441425,-5.176058,3.843115,3.232546,4.564554,-1.440908,-2.437182,1.942689],[1.962244,-7.015869,-5.872609,8.415378,3.409289,-5.897158,-7.691357,-6.433384,3.136609,3.266392,5.265685,-4.923272],[-6.194537,-2.075087,-2.213649,-2.641423,-7.569469,0.319430,5.970687,-7.269719,6.851145,0.302424,-4.721713,0.113026],[-8.943844,2.191256,-3.667430,-2.942294,-9.148491,2.998819,3.670537,-0.413500,-4.272674,-7.666733,-1.851539,1.918674],[4.315562,-4.081634,-9.904682,-6.193556,-0.808459,-1.621080,5.603552,-5.199972,-0.607770,-3.357612,1.547227,7.425695],[-9.166793,7.293160,-0.028820,7.045310,3.798516,1.596415,5.553556,-3.320353,7.420108,-9.559989,-3.564597,-9.161746],[2.511315,-9.406093,9.258096,-8.149925,6.594566,4.211426,-2.028960,-3.228506,-3.199403,2.718909,1.704675,1.459482],[9.998342,4.887772,-5.676991,-5.508343,-9.353786,6.550501,-0.506082,-3.561280,1.255944,3.520328,-6.331130,-9.523589],[9.910117,-5.611019,7.367904,-3.565290,-0.790154,-6.419046,3.756843,-8.717658,0.909990,-5.693898,5.262988,-9.611994],[-6.895358,0.168673,6.337077,6.738514,1.817972,1.559734,3.003217,6.629883,3.891490,7.839017,-8.602748,-1.525986],[1.045311,7.372037,1.440773,0.618859,4.395575,-1.573420,-0.460449,-8.669835,-0.930943,2.594694,1.702834,2.790548],[-2.113386,1.604331,-0.311057,6.858096,-2.953773,-3.200598,-3.646256,4.152593,-5.020129,-3.419931,3.666460,4.133672],[-4.873295,-0.415642,3.828877,-8.183051,-1.887899,6.260136,4.425008,-7.827474,6.781051,-8.201020,-2.624657,-9.672834],[0.761688,-2.246165,8.634199,-3.466681,-6.599203,7.434004,-4.173791,6.436940,8.338086,7.026031,3.327905,1.927607],[4.325793,-7.216101,0.704155,-6.455461,3.053952,-5.391266,-7.614476,-4.225325,0.857509,8.919097,1.890935,-5.169957],[1.810463,-7.231441,0.490505,4.621989,7.903383,-5.104682,-7.672590,4.165159,7.417905,-8.882509,0.036850,-4.890468],[-0.379602,-6.089652,0.437965,3.855324,3.659309,6.298537,6.942940,5.545564,5.286450,7.794029,-4.505980,5.733897],[-7.885576,-2.620161,5.520569,-0.207767,-9.254200,2.275435,3.715394,-9.875089,-1.431797,8.298597,-5.966597,-9.432977],[7.432089,-7.082557,1.129229,4.214512,9.487951,4.701272,7.468850,3.212044,-6.081611,9.278406,5.532940,-0.478915],[5.508065,6.704483,-5.051059,3.364032,4.347276,-6.602759,-5.871267,1.146796,3.521387,-6.965072,-1.455528,-2.112696],[-9.867737,8.718256,1.030614,-0.189500,0.637230,-7.535869,7.093632,1.435096,4.666403,8.268117,-8.105465,-4.288786],[5.712649,-8.434934,-2.969220,7.954890,-1.683044,-6.737666,-7.653940,-7.152477,-1.926242,-4.805647,6.763161,-0.500056],[9.891002,-6.740684,-0.582172,9.134494,7.421805,-0.237236,-4.515783,-9.253823,-2.186507,-6.412047,9.477975,-8.826526],[1.431636,-2.431287,2.583161,-2.665083,-4.362311,-3.697909,9.692489,1.360108,3.663812,-0.811553,7.057678,-2.228160],[5.944769,-3.079818,2.893447,-0.758035,4.205083,6.464839,8.778879,6.536042,-2.301183,9.117169,4.604959,-5.993173],[-7.971652,-7.625498,-2.154407,3.023656,4.779876,-9.204622,-2.422773,-5.636099,1.464030,-8.621779,2.176252,8.916285],[0.062217,5.879329,6.716755,8.732958,-2.479807,3.522216,-0.550508,-1.505843,-3.599680,5.941045,8.786490,6.270840],[1.604534,0.221807,7.763447,2.859537,7.667430,-4.058414,-0.268246,-5.480528,7.852228,1.906200,-3.727964,-6.848979],[5.756455,-9.767788,0.590224,6.865411,7.589963,6.875790,6.071742,-8.170175,1.540957,5.613401,-3.564486,-4.922379],[4.489475,-9.844564,5.097082,7.687100,-6.339793,5.525722,9.436436,-1.436759,3.269751,9.289762,-1.565903,-6.065541],[-6.811801,-2.564000,8.135283,2.647529,-2.571018,7.338587,-5.422463,-5.735804,-9.678843,-5.739537,6.220701,-2.393635],[-4.901653,2.736657,3.900015,-9.407045,-9.278836,7.447999,6.114187,-7.363798,-8.162441,4.011083,-0.528397,7.776966],[4.764888,-1.458458,-6.003832,6.356017,0.116752,-9.950443,-1.749982,-7.573538,7.770531,4.218254,-5.700860,-9.120814],[3.661664,6.604106,-6.405153,-2.931571,-1.943237,-5.409289,6.564170,0.935331,-3.240030,-8.621695,-6.232421,0.316758],[-4.675181,-1.459664,2.993485,8.581078,-9.725603,-2.983868,1.534216,-2.880961,-7.731155,-4.787648,7.288516,-7.966017],[0.020829,-8.817631,9.072049,1.662473,-5.617315,7.449090,3.551665,-6.287520,2.161071,-5.106711,6.836258,5.055394],[6.403071,-8.623003,2.845987,-1.574466,8.317259,7.171434,4.389093,-5.835012,-3.311667,4.387635,-1.788017,-7.569455],[-5.704980,-0.243975,3.059044,9.169609,6.324632,5.596989,-9.351634,-5.180642,8.008740,1.331452,-6.022199,-1.136283],[1.964006,-9.450007,-9.000762,2.736560,3.822397,-3.968290,6.822474,6.217227,2.485655,-4.301890,6.222993,0.911275],[-2.287985,1.260529,-7.198907,3.572971,9.921896,9.898282,-6.626266,-5.365726,-9.512673,3.184067,8.875126,9.814584],[4.365288,-1.883592,-1.143868,0.705661,-6.795330,1.717508,4.843528,-4.110929,9.917144,-8.242971,1.624957,8.057379],[9.550740,6.522412,-9.745844,-8.039106,-5.076647,-1.769437,-4.592600,1.421344,-6.858992,-9.957102,-6.178609,-2.617896],[-2.826327,3.991822,6.800294,-2.647527,1.360085,5.487334,-8.714674,-5.189739,1.713625,5.539343,-4.187558,-7.284397],[6.052347,-5.458115,-2.009625,4.898145,0.761878,-4.648078,-4.313538,-9.168480,-6.285668,7.922597,1.465178,-0.190897],[-2.252603,-5.161012,-6.140391,9.469391,0.733107,3.372034,-8.831123,8.485694,-8.184419,-8.477030,-6.264957,-7.213971],[4.292870,7.809898,2.841334,2.718034,8.398026,4.955259,-6.824608,4.400420,-5.950131,3.446874,-8.351151,0.128424],[-4.034670,7.658628,-6.848260,-6.093269,3.763206,-7.391478,6.261160,-7.459813,8.789286,-2.541448,-6.060882,-6.711636],[4.122734,9.425255,-3.143299,-4.037869,-0.670692,7.985195,0.188523,-0.251968,6.674115,-3.728619,-2.230439,5.094425],[-2.058416,-5.209921,6.727302,7.699910,-5.867539,-7.303366,9.899186,-6.914883,-0.588844,-0.594772,8.712306,-2.674279],[4.844500,4.227623,2.112869,-7.948598,-8.994821,-0.246788,5.814711,-2.868734,-5.994108,-0.646876,0.637932,-6.977819],[-9.498489,-5.708155,8.243789,-1.802849,0.519220,8.897073,-6.925167,-3.086863,-3.043525,-2.764954,-1.460911,6.582337],[-2.693057,1.537216,-4.462252,1.725171,-3.682194,-0.498797,1.176202,7.192923,-3.959322,2.167881,-9.004240,-9.783630],[6.828600,-8.870679,0.310205,-5.383192,7.969066,-0.680498,4.931781,-1.716603,6.469222,-9.818580,3.586960,1.446582],[-3.501208,-0.338725,-7.060779,5.690106,8.440382,4.617976,6.936144,-7.377021,8.718497,4.053639,5.644461,0.861300],[-0.636126,4.295571,9.643037,-4.206191,0.892081,-7.304284,0.266512,9.080624,2.688897,4.039896,5.380187,6.509228],[-2.694382,7.454358,-2.082052,-0.887129,-3.744739,-7.116087,-9.303850,6.074831,8.100007,8.166812,2.511030,7.905483],[-4.166286,-4.276716,9.072765,-9.497687,-1.367933,3.047001,-5.532924,6.550301,3.256849,-5.965804,-2.626804,9.892311],[8.313721,-4.184859,-6.231091,6.863287,1.856796,-7.450418,1.565187,-8.222985,-4.489943,-5.237040,-9.658011,-7.839798],[8.419315,2.889149,-7.468971,6.008998,-1.583428,5.821429,-6.446915,5.833279,-0.419020,-2.621558,-8.863302,1.130383],[-5.781418,-0.859268,5.958603,-2.498719,9.085722,8.533805,-7.320872,-7.222497,-1.718635,7.057943,-5.542235,-6.468196],[-9.439588,9.964999,-7.505007,-1.851623,-9.936689,4.630776,1.621815,2.611769,3.517613,-4.615475,7.605867,-8.449474],[-7.690631,-6.217479,-9.789790,9.092739,7.465124,-0.862493,4.770764,-9.177616,9.113577,-3.993107,9.157522,0.383736],[-9.339736,8.481330,-9.195797,1.436756,6.742661,-1.127123,7.364378,7.402231,-8.881419,-1.887682,-7.691808,0.996650],[-9.613682,-8.901082,6.450737,-7.849243,5.249363,-0.211426,-4.115038,6.733875,8.784823,3.764569,9.974110,-0.046067],[-3.363612,-4.604383,9.736718,-1.655086,8.299953,-3.644513,7.684925,-6.740682,-0.112060,-4.490489,-7.332261,-5.537052],[8.896803,-0.998997,-2.741489,-4.651698,1.086329,0.964966,0.345110,-5.378939,-8.388348,0.898591,-7.831385,8.093189],[-9.551017,2.358442,3.456183,7.626226,0.325899,0.204270,-4.225378,1.356408,-3.674454,-9.921769,-2.097752,-9.103227],[1.258288,-3.153818,6.055494,-7.985153,-6.592460,1.336100,-1.923661,-8.132278,-5.664044,9.371809,-1.635551,7.818961],[-5.583686,-7.332138,-7.032921,9.252868,-0.002826,5.849353,1.987660,-6.100449,3.176593,4.872235,-8.936282,-3.937170],[-9.323387,2.440225,-1.091930,8.426825,-7.560481,8.046379,0.758766,6.851406,2.433860,2.761335,-7.909851,-4.194496],[2.934096,6.673947,5.424355,1.105660,-5.205258,-1.944507,0.881111,3.204787,3.147543,-6.820450,7.795482,9.312807],[2.234589,-1.877696,-0.969688,4.032979,-3.405953,3.139860,-4.339743,3.856030,5.414771,4.847383,-9.635273,-6.433449],[-4.838599,-6.712477,-0.950712,-9.172242,-0.974870,-8.635502,4.794546,9.744798,-4.254412,3.167455,9.178048,3.061186],[0.211229,0.535791,1.971192,5.444128,-2.255719,-8.437059,6.586687,-5.593638,2.839204,-0.083510,9.123147,-5.623825],[-0.631682,-9.597647,5.028172,-7.931032,5.956869,-2.093973,-1.366681,-1.105774,8.080659,0.276889,1.543261,-3.775699],[-2.888304,6.858917,-3.770206,-4.731722,0.255977,-0.093931,-7.225818,6.339480,-5.861364,2.265829,-8.330380,-8.270169],[-9.877897,-1.769324,6.154310,-9.436268,-5.194204,4.973035,2.999871,2.330767,8.254557,2.915211,1.548101,0.194138],[-0.839134,-1.510682,-7.887123,-9.260489,-1.261108,-8.998428,-5.160917,-5.384885,-9.865295,4.149130,4.559158,-8.231344],[5.747902,-0.522730,6.763903,-9.532728,-4.856948,-6.978200,2.898318,5.585844,1.483237,-1.881704,-9.286427,-3.577095],[-6.344092,6.449280,4.959476,-3.857773,9.897021,7.690441,-7.237771,0.396188,-5.833971,8.670647,-3.467515,9.855836],[-3.483380,2.177561,-0.044087,4.648764,-8.092059,-7.547916,6.586475,-8.188201,-5.154031,0.813638,3.980077,0.816444],[-2.567321,-4.698508,-1.576786,-8.377053,7.823327,4.329599,-8.360565,-7.608850,3.028958,-8.876782,-9.351638,-0.327462],[-2.629651,0.870199,-1.394095,3.325215,-3.729733,7.067309,3.856322,1.824881,-1.036386,3.474994,-0.864915,7.055129],[-7.979775,-8.324540,-9.027466,8.870256,-5.159508,-6.706092,-4.288109,3.538832,0.559412,8.322086,-2.792829,3.653348],[2.536290,5.155940,8.894735,-1.759746,-3.662888,-8.505806,4.442225,3.001849,-4.053854,-2.919033,7.075818,1.451837],[-7.940158,-5.034461,-9.047863,1.499817,-2.515418,8.826696,8.646964,0.617005,-8.037988,-4.689383,-4.491766,8.202087],[-1.034438,8.661153,9.946087,-7.617646,6.772057,-1.050141,6.783221,1.068896,1.413574,2.029474,-9.419473,-1.034900],[-7.284911,-9.892127,9.606263,1.598702,7.623088,6.585977,-5.007638,9.974091,-8.217510,7.074882,7.604586,1.704644],[0.012009,-8.057913,-9.831944,-6.313268,3.282437,3.455435,-0.876799,-9.531834,8.870637,-3.578281,-4.608438,8.351585],[2.696722,-4.622534,9.004911,2.292098,-3.886552,9.025549,7.554479,3.047936,-1.704040,4.751596,5.051849,5.873916],[1.520385,-3.799298,8.730749,1.870738,-0.060124,7.050170,0.197962,-1.503114,-0.064705,-3.183841,3.462216,1.259338],[-2.825961,-9.649510,-9.563010,-3.498944,2.314760,5.080765,-3.783397,-5.658057,-9.342398,0.315305,-2.024284,1.374398],[3.000380,-9.303911,9.064922,-0.044071,-6.016864,-0.056623,-1.572767,5.658686,7.712750,-7.174599,1.412133,9.078708],[3.471498,8.969773,-0.112284,-2.778558,2.892197,8.745817,-9.988009,-7.849997,-7.035267,-9.970695,-2.690482,2.510249],[-7.475831,5.295035,-5.778955,-0.229056,4.868067,6.831147,-1.557158,2.384065,2.478966,0.719303,6.633420,-6.735491],[-2.414669,-0.434315,-7.661196,-6.478842,-3.561158,-5.875629,-9.810644,-9.733420,3.274806,-2.370959,0.498197,3.380155],[-4.364847,2.724261,-2.771033,8.171958,-4.695004,8.382273,7.430601,3.145787,-3.623369,-1.543170,-0.479285,-2.203849],[1.356859,-9.036899,2.599009,9.229138,-8.300192,4.985150,-3.702382,5.329688,-3.030724,-3.801237,-9.202481,3.054532],[9.442552,-8.756793,-4.988688,8.159499,7.511085,9.204744,0.700969,-8.372051,6.695122,6.653100,-2.887999,-0.305614],[3.382062,5.820663,-2.294722,-7.321672,-1.969348,-3.266213,-6.892094,-1.632021,3.905997,-6.732190,-9.020878,-6.052842],[-8.346162,-8.633749,-1.924045,5.430442,0.975745,4.003017,-6.354423,1.139087,-6.564412,0.940290,-0.103349,-3.944715],[2.015158,-9.598846,8.704149,1.018375,-6.120342,7.584712,-2.314908,3.246059,3.812372,-7.004305,-1.571977,-2.381990],[2.014995,8.240406,-5.500981,7.646200,-0.699411,3.161432,-1.824400,0.220045,-6.583529,2.407670,-6.686101,-5.422055],[4.123944,2.834907,6.509198,9.269003,4.946475,-0.645068,-7.004556,-3.942385,3.030673,2.430672,-6.219026,6.837917],[5.648134,-6.160905,0.044330,4.296834,4.452289,-6.201564,-9.037462,6.899500,2.468072,3.954962,2.455182,-7.646208],[-3.706018,-1.055986,4.407958,7.631607,-8.362334,-9.530337,1.990669,-7.966309,-2.786774,1.640179,-2.681779,-9.841518],[-4.496700,-1.827965,0.671123,-3.369147,-7.230141,9.872378,-4.028339,-1.858489,-3.427423,-3.630086,-5.397625,-4.425287],[-3.835450,2.116583,-3.446637,-5.156128,-6.447378,-7.706689,2.925993,0.287285,9.933538,1.372736,5.978776,-4.964274],[-1.601881,3.747556,3.449159,1.835361,2.792092,3.046157,6.818722,-2.046797,-8.389765,7.856072,-5.149790,0.538314],[5.552477,0.454887,-1.771878,-0.484703,7.147089,6.708916,0.620076,-8.828290,2.610083,-9.640678,6.805625,-9.956831],[4.307606,2.945489,-8.297668,1.667791,-5.577224,5.950696,-5.924441,8.709054,0.355926,6.888176,-1.597890,-6.247932],[4.615276,-4.732831,9.097662,-0.264571,-8.774723,-6.961957,-0.449347,1.733088,6.203963,1.780578,-5.342849,1.846578],[2.319600,9.137542,-3.266748,2.648302,-9.905627,-7.329692,6.788831,3.879353,-4.117720,-8.051268,5.729029,5.822782],[-8.260082,2.133920,-3.972756,2.778663,9.073776,5.180810,-5.094186,5.295813,-5.956821,-9.074788,-9.776115,3.130648],[-7.006920,4.713072,2.433146,-1.798391,2.618319,2.013747,-1.601657,2.584723,8.249674,4.625269,5.038805,-3.319336],[-0.340089,1.831486,-1.770059,6.534476,4.609702,5.640690,-5.407518,-5.347558,6.744262,4.190519,-2.597563,0.732284]], dtype = "float32")#candidate|3688|(300, 12)|const|float32
call_3685 = relay.TupleGetItem(func_1819_call(relay.reshape(var_3686.astype('uint32'), [12, 5, 10]), relay.reshape(var_3687.astype('int8'), [1, 450]), relay.reshape(const_3688.astype('float32'), [3600,]), ), 0)
call_3689 = relay.TupleGetItem(func_1823_call(relay.reshape(var_3686.astype('uint32'), [12, 5, 10]), relay.reshape(var_3687.astype('int8'), [1, 450]), relay.reshape(const_3688.astype('float32'), [3600,]), ), 0)
func_2563_call = mod.get_global_var('func_2563')
func_2564_call = mutated_mod.get_global_var('func_2564')
call_3694 = relay.TupleGetItem(func_2563_call(), 0)
call_3695 = relay.TupleGetItem(func_2564_call(), 0)
func_3649_call = mod.get_global_var('func_3649')
func_3651_call = mutated_mod.get_global_var('func_3651')
call_3700 = func_3649_call()
call_3701 = func_3649_call()
output = relay.Tuple([call_3676,call_3680,call_3685,var_3686,var_3687,const_3688,call_3694,call_3700,])
output2 = relay.Tuple([call_3677,call_3681,call_3689,var_3686,var_3687,const_3688,call_3695,call_3701,])
func_3702 = relay.Function([var_3686,var_3687,], output)
mod['func_3702'] = func_3702
mod = relay.transform.InferType()(mod)
mutated_mod['func_3702'] = func_3702
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3702_call = mutated_mod.get_global_var('func_3702')
var_3704 = relay.var("var_3704", dtype = "uint32", shape = (600,))#candidate|3704|(600,)|var|uint32
var_3705 = relay.var("var_3705", dtype = "int8", shape = (150, 3))#candidate|3705|(150, 3)|var|int8
call_3703 = func_3702_call(var_3704,var_3705,)
output = call_3703
func_3706 = relay.Function([var_3704,var_3705,], output)
mutated_mod['func_3706'] = func_3706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2933_call = mod.get_global_var('func_2933')
func_2934_call = mutated_mod.get_global_var('func_2934')
call_3774 = relay.TupleGetItem(func_2933_call(), 0)
call_3775 = relay.TupleGetItem(func_2934_call(), 0)
output = call_3774
output2 = call_3775
func_3781 = relay.Function([], output)
mod['func_3781'] = func_3781
mod = relay.transform.InferType()(mod)
output = func_3781()
func_3782 = relay.Function([], output)
mutated_mod['func_3782'] = func_3782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1753_call = mod.get_global_var('func_1753')
func_1754_call = mutated_mod.get_global_var('func_1754')
call_3814 = relay.TupleGetItem(func_1753_call(), 0)
call_3815 = relay.TupleGetItem(func_1754_call(), 0)
func_3092_call = mod.get_global_var('func_3092')
func_3094_call = mutated_mod.get_global_var('func_3094')
call_3889 = func_3092_call()
call_3890 = func_3092_call()
output = relay.Tuple([call_3814,call_3889,])
output2 = relay.Tuple([call_3815,call_3890,])
func_3891 = relay.Function([], output)
mod['func_3891'] = func_3891
mod = relay.transform.InferType()(mod)
mutated_mod['func_3891'] = func_3891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3891_call = mutated_mod.get_global_var('func_3891')
call_3892 = func_3891_call()
output = call_3892
func_3893 = relay.Function([], output)
mutated_mod['func_3893'] = func_3893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3597_call = mod.get_global_var('func_3597')
func_3598_call = mutated_mod.get_global_var('func_3598')
call_3908 = relay.TupleGetItem(func_3597_call(), 0)
call_3909 = relay.TupleGetItem(func_3598_call(), 0)
output = relay.Tuple([call_3908,])
output2 = relay.Tuple([call_3909,])
func_3929 = relay.Function([], output)
mod['func_3929'] = func_3929
mod = relay.transform.InferType()(mod)
mutated_mod['func_3929'] = func_3929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3929_call = mutated_mod.get_global_var('func_3929')
call_3930 = func_3929_call()
output = call_3930
func_3931 = relay.Function([], output)
mutated_mod['func_3931'] = func_3931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1324_call = mod.get_global_var('func_1324')
func_1325_call = mutated_mod.get_global_var('func_1325')
call_3940 = relay.TupleGetItem(func_1324_call(), 0)
call_3941 = relay.TupleGetItem(func_1325_call(), 0)
const_3968 = relay.const([[[-3.085615,7.322790,-1.762823,9.453733,-0.963813,0.099174,3.936652,-4.721571,-0.948108,8.887265,-8.410795,-9.343770,8.743490,3.761406,-8.373733],[-3.800052,1.827063,-0.814776,-5.577678,-7.948213,-4.745198,-8.819765,3.465175,3.778178,3.456523,-6.012147,7.503422,7.500418,7.369846,1.297512],[7.743524,6.666914,9.466163,-7.368247,8.900924,8.616941,5.977808,1.268069,-5.147039,-2.046992,0.776173,8.163414,8.189738,8.065267,-4.387988],[-7.659365,-1.071372,-1.132554,-0.482241,8.870632,3.947195,5.347282,9.380642,9.644084,-8.923100,3.486876,-9.450952,-6.827377,9.700295,7.980855],[-4.950874,-0.202725,6.442077,-7.783450,5.433389,0.466488,-2.887504,9.338715,9.068798,4.340848,-2.157031,7.246140,-7.554816,-9.388631,-7.822228],[0.645120,-6.343317,0.702689,-4.443453,8.958847,-5.815733,-3.252115,5.496360,-3.306357,-5.833413,-5.101628,-1.167010,-0.641259,3.861473,-4.319868],[-2.660563,-2.033925,0.355040,-1.538357,-5.829604,-6.629645,-1.095211,7.976378,-2.285626,-2.587125,-7.010472,-7.017887,-5.533862,1.615592,1.800944]],[[3.286799,5.154902,-2.512641,-5.604316,-8.001645,-8.505869,3.139889,6.821225,7.890542,-6.711159,-9.426632,-7.017130,3.304479,3.093987,0.143150],[-6.691022,-4.258476,-4.693764,7.149352,8.510268,0.929379,-3.433769,-8.786054,-2.700041,7.043040,2.667593,6.501766,-4.227949,9.252608,0.268039],[8.491171,8.417314,1.108632,-2.376864,-7.048612,-4.973078,-1.331235,-7.151830,-4.342013,-7.388159,9.165906,9.392963,8.751571,7.265954,-5.290770],[2.611278,7.153214,4.169553,3.983874,2.913630,-3.331574,4.501196,-1.048854,0.379106,-4.891642,-3.912693,-0.028182,-4.884887,-4.186374,-7.839033],[-0.411655,-3.625313,-0.738121,-1.114946,7.679825,-7.088053,8.796436,-4.136843,5.726693,-6.992185,7.029042,-4.072524,6.852074,-1.316528,-7.813232],[-8.879245,-1.735358,-2.388885,-2.785822,-4.355837,-9.252492,8.516971,7.235019,4.621444,-2.932536,-3.955169,5.304043,2.167478,-9.155726,-5.103627],[-4.732500,5.568735,8.093230,8.764165,3.751117,5.960904,-4.938769,9.642318,5.056927,4.220402,1.941429,5.952351,-6.354323,8.782699,-4.953224]]], dtype = "float32")#candidate|3968|(2, 7, 15)|const|float32
bop_3969 = relay.not_equal(call_3940.astype('bool'), const_3968.astype('bool')) # shape=(2, 7, 15)
bop_3972 = relay.not_equal(call_3941.astype('bool'), const_3968.astype('bool')) # shape=(2, 7, 15)
output = relay.Tuple([bop_3969,])
output2 = relay.Tuple([bop_3972,])
func_3996 = relay.Function([], output)
mod['func_3996'] = func_3996
mod = relay.transform.InferType()(mod)
mutated_mod['func_3996'] = func_3996
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3996_call = mutated_mod.get_global_var('func_3996')
call_3997 = func_3996_call()
output = call_3997
func_3998 = relay.Function([], output)
mutated_mod['func_3998'] = func_3998
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1691_call = mod.get_global_var('func_1691')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_4059 = relay.TupleGetItem(func_1691_call(), 0)
call_4060 = relay.TupleGetItem(func_1693_call(), 0)
output = relay.Tuple([call_4059,])
output2 = relay.Tuple([call_4060,])
func_4065 = relay.Function([], output)
mod['func_4065'] = func_4065
mod = relay.transform.InferType()(mod)
output = func_4065()
func_4066 = relay.Function([], output)
mutated_mod['func_4066'] = func_4066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2933_call = mod.get_global_var('func_2933')
func_2934_call = mutated_mod.get_global_var('func_2934')
call_4090 = relay.TupleGetItem(func_2933_call(), 0)
call_4091 = relay.TupleGetItem(func_2934_call(), 0)
output = relay.Tuple([call_4090,])
output2 = relay.Tuple([call_4091,])
func_4096 = relay.Function([], output)
mod['func_4096'] = func_4096
mod = relay.transform.InferType()(mod)
output = func_4096()
func_4097 = relay.Function([], output)
mutated_mod['func_4097'] = func_4097
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3092_call = mod.get_global_var('func_3092')
func_3094_call = mutated_mod.get_global_var('func_3094')
call_4119 = func_3092_call()
call_4120 = func_3092_call()
func_4065_call = mod.get_global_var('func_4065')
func_4066_call = mutated_mod.get_global_var('func_4066')
call_4135 = relay.TupleGetItem(func_4065_call(), 0)
call_4136 = relay.TupleGetItem(func_4066_call(), 0)
func_1119_call = mod.get_global_var('func_1119')
func_1120_call = mutated_mod.get_global_var('func_1120')
call_4145 = relay.TupleGetItem(func_1119_call(), 0)
call_4146 = relay.TupleGetItem(func_1120_call(), 0)
func_3597_call = mod.get_global_var('func_3597')
func_3598_call = mutated_mod.get_global_var('func_3598')
call_4180 = relay.TupleGetItem(func_3597_call(), 0)
call_4181 = relay.TupleGetItem(func_3598_call(), 0)
output = relay.Tuple([call_4119,call_4135,call_4145,call_4180,])
output2 = relay.Tuple([call_4120,call_4136,call_4146,call_4181,])
func_4188 = relay.Function([], output)
mod['func_4188'] = func_4188
mod = relay.transform.InferType()(mod)
output = func_4188()
func_4189 = relay.Function([], output)
mutated_mod['func_4189'] = func_4189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2759_call = mod.get_global_var('func_2759')
func_2761_call = mutated_mod.get_global_var('func_2761')
call_4190 = func_2759_call()
call_4191 = func_2759_call()
func_3370_call = mod.get_global_var('func_3370')
func_3371_call = mutated_mod.get_global_var('func_3371')
call_4194 = relay.TupleGetItem(func_3370_call(), 0)
call_4195 = relay.TupleGetItem(func_3371_call(), 0)
func_1460_call = mod.get_global_var('func_1460')
func_1462_call = mutated_mod.get_global_var('func_1462')
call_4198 = relay.TupleGetItem(func_1460_call(), 0)
call_4199 = relay.TupleGetItem(func_1462_call(), 0)
func_4065_call = mod.get_global_var('func_4065')
func_4066_call = mutated_mod.get_global_var('func_4066')
call_4206 = relay.TupleGetItem(func_4065_call(), 0)
call_4207 = relay.TupleGetItem(func_4066_call(), 0)
output = relay.Tuple([call_4190,call_4194,call_4198,call_4206,])
output2 = relay.Tuple([call_4191,call_4195,call_4199,call_4207,])
func_4219 = relay.Function([], output)
mod['func_4219'] = func_4219
mod = relay.transform.InferType()(mod)
mutated_mod['func_4219'] = func_4219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4219_call = mutated_mod.get_global_var('func_4219')
call_4220 = func_4219_call()
output = call_4220
func_4221 = relay.Function([], output)
mutated_mod['func_4221'] = func_4221
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4231 = relay.var("var_4231", dtype = "float32", shape = (2, 13, 11))#candidate|4231|(2, 13, 11)|var|float32
uop_4232 = relay.exp(var_4231.astype('float32')) # shape=(2, 13, 11)
output = relay.Tuple([uop_4232,])
output2 = relay.Tuple([uop_4232,])
func_4256 = relay.Function([var_4231,], output)
mod['func_4256'] = func_4256
mod = relay.transform.InferType()(mod)
var_4257 = relay.var("var_4257", dtype = "float32", shape = (2, 13, 11))#candidate|4257|(2, 13, 11)|var|float32
output = func_4256(var_4257)
func_4258 = relay.Function([var_4257], output)
mutated_mod['func_4258'] = func_4258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1384_call = mod.get_global_var('func_1384')
func_1386_call = mutated_mod.get_global_var('func_1386')
call_4360 = relay.TupleGetItem(func_1384_call(), 1)
call_4361 = relay.TupleGetItem(func_1386_call(), 1)
output = call_4360
output2 = call_4361
func_4363 = relay.Function([], output)
mod['func_4363'] = func_4363
mod = relay.transform.InferType()(mod)
mutated_mod['func_4363'] = func_4363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4363_call = mutated_mod.get_global_var('func_4363')
call_4364 = func_4363_call()
output = call_4364
func_4365 = relay.Function([], output)
mutated_mod['func_4365'] = func_4365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4188_call = mod.get_global_var('func_4188')
func_4189_call = mutated_mod.get_global_var('func_4189')
call_4378 = relay.TupleGetItem(func_4188_call(), 0)
call_4379 = relay.TupleGetItem(func_4189_call(), 0)
output = relay.Tuple([call_4378,])
output2 = relay.Tuple([call_4379,])
func_4386 = relay.Function([], output)
mod['func_4386'] = func_4386
mod = relay.transform.InferType()(mod)
output = func_4386()
func_4387 = relay.Function([], output)
mutated_mod['func_4387'] = func_4387
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3781_call = mod.get_global_var('func_3781')
func_3782_call = mutated_mod.get_global_var('func_3782')
call_4441 = func_3781_call()
call_4442 = func_3781_call()
output = call_4441
output2 = call_4442
func_4454 = relay.Function([], output)
mod['func_4454'] = func_4454
mod = relay.transform.InferType()(mod)
output = func_4454()
func_4455 = relay.Function([], output)
mutated_mod['func_4455'] = func_4455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1190_call = mod.get_global_var('func_1190')
func_1191_call = mutated_mod.get_global_var('func_1191')
call_4524 = func_1190_call()
call_4525 = func_1190_call()
var_4531 = relay.var("var_4531", dtype = "float32", shape = (2, 7, 16))#candidate|4531|(2, 7, 16)|var|float32
bop_4532 = relay.maximum(call_4524.astype('float64'), var_4531.astype('float64')) # shape=(2, 7, 16)
bop_4535 = relay.maximum(call_4525.astype('float64'), var_4531.astype('float64')) # shape=(2, 7, 16)
bop_4550 = relay.bitwise_and(call_4524.astype('uint64'), bop_4532.astype('uint64')) # shape=(2, 7, 16)
bop_4553 = relay.bitwise_and(call_4525.astype('uint64'), bop_4535.astype('uint64')) # shape=(2, 7, 16)
output = relay.Tuple([bop_4550,])
output2 = relay.Tuple([bop_4553,])
func_4558 = relay.Function([var_4531,], output)
mod['func_4558'] = func_4558
mod = relay.transform.InferType()(mod)
mutated_mod['func_4558'] = func_4558
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4559 = relay.var("var_4559", dtype = "float32", shape = (2, 7, 16))#candidate|4559|(2, 7, 16)|var|float32
func_4558_call = mutated_mod.get_global_var('func_4558')
call_4560 = func_4558_call(var_4559)
output = call_4560
func_4561 = relay.Function([var_4559], output)
mutated_mod['func_4561'] = func_4561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2759_call = mod.get_global_var('func_2759')
func_2761_call = mutated_mod.get_global_var('func_2761')
call_4635 = func_2759_call()
call_4636 = func_2759_call()
func_4096_call = mod.get_global_var('func_4096')
func_4097_call = mutated_mod.get_global_var('func_4097')
call_4641 = relay.TupleGetItem(func_4096_call(), 0)
call_4642 = relay.TupleGetItem(func_4097_call(), 0)
uop_4644 = relay.log10(call_4635.astype('float64')) # shape=(2, 7, 1)
uop_4646 = relay.log10(call_4636.astype('float64')) # shape=(2, 7, 1)
func_2453_call = mod.get_global_var('func_2453')
func_2455_call = mutated_mod.get_global_var('func_2455')
const_4661 = relay.const([-9.695051,-6.415581,-7.652355,3.158587,-5.779400,3.153890,4.763649,-0.559091,2.841017,9.921696,8.586545,4.239676,4.799135,-9.918219,-7.989123,-2.346624,5.248574,-3.355804,-3.066549,2.815693,-4.361796,-6.897124,6.711074,4.696425,4.450063,-7.770070,-4.206747,-7.747774,-0.875066,0.811371,-7.865802,7.598639,-6.383443,4.614544,9.128896,6.396785,9.913804,9.978837,-6.696947,-5.147771,2.034679,-9.105133,-4.957200,-7.711913,0.754386,3.527774,1.892604,9.822362,-4.052809,-1.008852,9.729326,-4.300107,1.858467,-1.252460,-7.042742,0.268592,3.026824,0.130108,-7.469021,-2.036440,1.238993,-3.240798,-5.447131,-1.745781,-3.000669,-1.612044,-3.844808,7.709498,7.864212,0.645134,-2.743648,2.784323,-6.110765,7.240119,-9.309712,-7.267969,-8.345323,-8.676736,-0.661721,4.667539,-0.838739,6.338580,-1.815429,-9.356735,-0.599301,1.025459,9.806518,-1.757450,-7.388837,-1.209111,8.215579,-7.985464,5.540904,-9.706129,-9.837276,4.868088,1.951505,9.903500,2.545451,3.401754,-1.110548,-5.394124,-2.656128,2.493011,-2.349321,3.865629,3.134414,9.471877,5.717401,-4.809682,-6.615988,-6.863213,-8.087493,0.051313,5.388959,2.078644,-2.374014,7.940226,-8.673611,4.675147,9.290660,-5.119029,-0.519948,6.060247,2.478099,9.202239,2.732020,-3.474629,-0.352321,2.609920,-4.861706,8.342101,-4.055410,6.739450,1.939066,-1.280130,-5.772149,2.146593,-6.360592,-1.056398,0.053396,3.900136,5.656255,-7.358165,-0.426074,9.524256,3.632795,3.239731,-8.420790,-8.995828,8.873717,-3.901604,-0.439164,-1.770496,-8.011915,-0.272874,5.796655,0.613316,3.375171,-0.153939,4.763264,1.236469,-1.813741,8.586447,9.484456,-9.040259,-9.016093,-4.394885,2.162193,9.780428,2.274283,5.292643,-6.690914,1.361964,-5.618502,9.767135,-2.036224,-0.360190,1.101169,5.454510,-6.867135,0.201176,-4.570421,4.471135,-0.555845,7.072408,-4.535815,-0.204304,3.805418,5.296864,7.560751,-9.745721,9.295356,-9.503285,-4.052629,8.643458,-7.564063,7.226579,3.985535,-2.035053,3.065975,8.135255,-0.901986,-9.512117,-7.499639,1.975950,-0.093739,5.971710,8.861028,-9.220970,8.580058,-0.450606,-3.053908,-4.280569,-1.919848,-6.754728,-8.239007,5.175586,8.577660,7.185810,6.036869,-7.897283,-1.520604,7.083947,6.923265], dtype = "float32")#candidate|4661|(225,)|const|float32
call_4660 = relay.TupleGetItem(func_2453_call(relay.reshape(const_4661.astype('float32'), [225,])), 6)
call_4662 = relay.TupleGetItem(func_2455_call(relay.reshape(const_4661.astype('float32'), [225,])), 6)
output = relay.Tuple([call_4641,uop_4644,call_4660,const_4661,])
output2 = relay.Tuple([call_4642,uop_4646,call_4662,const_4661,])
func_4663 = relay.Function([], output)
mod['func_4663'] = func_4663
mod = relay.transform.InferType()(mod)
output = func_4663()
func_4664 = relay.Function([], output)
mutated_mod['func_4664'] = func_4664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3181_call = mod.get_global_var('func_3181')
func_3182_call = mutated_mod.get_global_var('func_3182')
call_4682 = relay.TupleGetItem(func_3181_call(), 1)
call_4683 = relay.TupleGetItem(func_3182_call(), 1)
func_2077_call = mod.get_global_var('func_2077')
func_2079_call = mutated_mod.get_global_var('func_2079')
call_4690 = relay.TupleGetItem(func_2077_call(), 0)
call_4691 = relay.TupleGetItem(func_2079_call(), 0)
func_2011_call = mod.get_global_var('func_2011')
func_2014_call = mutated_mod.get_global_var('func_2014')
const_4703 = relay.const([[-5.396654,-7.016903],[4.990673,2.403343],[2.423488,-2.545947],[7.923509,-6.492128],[5.914164,-4.490350],[-6.722047,-4.222713],[7.651948,-9.895737],[8.810667,0.296477],[7.431260,6.125998],[1.151104,0.953736],[1.432481,-5.883335],[-3.304091,-4.773823],[0.733307,1.474957],[3.963506,0.358009],[5.795931,-2.633901],[0.463309,8.291751],[-6.018606,1.460979],[7.883379,-0.701859],[-0.925841,0.649370],[-1.716237,-3.092174],[5.184053,2.125635],[2.735879,3.317002],[-2.668412,-4.262529],[8.772779,7.076997],[-7.153137,3.708472],[8.225712,1.158446],[7.269686,-8.554373],[-5.088788,6.265682],[-4.467934,-9.295495],[7.358460,7.242013],[-6.790891,-3.226870],[7.454977,9.493630],[-9.036167,7.230630],[-5.734052,-6.016402],[3.289483,1.493222],[0.933740,6.378022],[5.114326,-3.959927],[7.888540,1.109070],[6.409623,1.394982],[9.459872,-0.701638],[-6.751561,7.397831],[-9.276656,-3.194749],[-1.450044,9.815224],[-2.720492,-2.649651],[1.755203,1.219778],[-0.574673,-2.181411],[-6.579437,-6.152216],[-2.500756,6.747160],[-7.223365,0.750356],[-6.773634,-5.829320],[-6.914869,4.006392],[0.562763,-1.023316],[-4.730486,9.605521],[-4.876891,-8.737075],[-3.427588,-5.335301],[1.279148,8.538993],[-3.716464,9.730501],[-3.005471,-5.001565],[1.629713,6.510971],[3.274010,3.370857],[5.859040,-3.928638],[-9.406265,-5.345501],[5.951594,2.119977],[4.146405,-2.791347],[-7.142282,-2.777814],[3.860205,2.046491],[-7.178312,5.380688],[-1.146560,0.782984],[-9.813012,-5.901572],[-7.156803,3.686066],[4.027338,8.156624],[8.502223,0.284421],[1.746991,-0.072840],[-0.404042,9.296172],[-9.868615,-7.417365],[-5.922755,8.074817],[0.121350,5.198841],[-5.192204,5.371995],[-9.575393,-3.276933],[-5.751723,7.577677],[-7.422570,-2.650893],[5.135084,9.420578],[7.657032,-6.601253],[-8.011127,-0.643655],[6.696181,2.475008],[-6.516409,-3.384656],[6.837959,-1.877426],[-5.531182,0.411558],[2.551023,1.366054],[-8.867916,-2.325037],[-4.085188,9.231681],[-1.641877,-1.571295],[3.653503,-7.820731],[-9.625885,-4.360702],[0.399524,1.174482],[-2.985342,-4.030260],[-8.069247,-7.879532],[1.690383,-8.472255],[-9.039690,-9.781317],[4.003026,-2.595820],[-3.062047,-1.259051],[9.284631,6.340940],[8.491100,-5.366909],[7.751210,3.790087],[-9.117395,-9.952396]], dtype = "float32")#candidate|4703|(105, 2)|const|float32
call_4702 = relay.TupleGetItem(func_2011_call(relay.reshape(const_4703.astype('float32'), [2, 7, 15])), 1)
call_4704 = relay.TupleGetItem(func_2014_call(relay.reshape(const_4703.astype('float32'), [2, 7, 15])), 1)
func_4065_call = mod.get_global_var('func_4065')
func_4066_call = mutated_mod.get_global_var('func_4066')
call_4705 = relay.TupleGetItem(func_4065_call(), 0)
call_4706 = relay.TupleGetItem(func_4066_call(), 0)
output = relay.Tuple([call_4682,call_4690,call_4702,const_4703,call_4705,])
output2 = relay.Tuple([call_4683,call_4691,call_4704,const_4703,call_4706,])
func_4708 = relay.Function([], output)
mod['func_4708'] = func_4708
mod = relay.transform.InferType()(mod)
output = func_4708()
func_4709 = relay.Function([], output)
mutated_mod['func_4709'] = func_4709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2759_call = mod.get_global_var('func_2759')
func_2761_call = mutated_mod.get_global_var('func_2761')
call_4766 = func_2759_call()
call_4767 = func_2759_call()
func_1489_call = mod.get_global_var('func_1489')
func_1490_call = mutated_mod.get_global_var('func_1490')
call_4770 = relay.TupleGetItem(func_1489_call(), 0)
call_4771 = relay.TupleGetItem(func_1490_call(), 0)
func_1887_call = mod.get_global_var('func_1887')
func_1889_call = mutated_mod.get_global_var('func_1889')
call_4773 = relay.TupleGetItem(func_1887_call(), 0)
call_4774 = relay.TupleGetItem(func_1889_call(), 0)
var_4780 = relay.var("var_4780", dtype = "float32", shape = (2, 7, 12))#candidate|4780|(2, 7, 12)|var|float32
bop_4781 = relay.subtract(call_4770.astype('float32'), var_4780.astype('float32')) # shape=(2, 7, 12)
bop_4784 = relay.subtract(call_4771.astype('float32'), var_4780.astype('float32')) # shape=(2, 7, 12)
func_4219_call = mod.get_global_var('func_4219')
func_4221_call = mutated_mod.get_global_var('func_4221')
call_4814 = relay.TupleGetItem(func_4219_call(), 1)
call_4815 = relay.TupleGetItem(func_4221_call(), 1)
uop_4827 = relay.sqrt(bop_4781.astype('float32')) # shape=(2, 7, 12)
uop_4829 = relay.sqrt(bop_4784.astype('float32')) # shape=(2, 7, 12)
func_4708_call = mod.get_global_var('func_4708')
func_4709_call = mutated_mod.get_global_var('func_4709')
call_4840 = relay.TupleGetItem(func_4708_call(), 0)
call_4841 = relay.TupleGetItem(func_4709_call(), 0)
func_3597_call = mod.get_global_var('func_3597')
func_3598_call = mutated_mod.get_global_var('func_3598')
call_4857 = relay.TupleGetItem(func_3597_call(), 0)
call_4858 = relay.TupleGetItem(func_3598_call(), 0)
func_3092_call = mod.get_global_var('func_3092')
func_3094_call = mutated_mod.get_global_var('func_3094')
call_4861 = func_3092_call()
call_4862 = func_3092_call()
func_2731_call = mod.get_global_var('func_2731')
func_2732_call = mutated_mod.get_global_var('func_2732')
call_4865 = func_2731_call()
call_4866 = func_2731_call()
output = relay.Tuple([call_4766,call_4773,call_4814,uop_4827,call_4840,call_4857,call_4861,call_4865,])
output2 = relay.Tuple([call_4767,call_4774,call_4815,uop_4829,call_4841,call_4858,call_4862,call_4866,])
func_4869 = relay.Function([var_4780,], output)
mod['func_4869'] = func_4869
mod = relay.transform.InferType()(mod)
mutated_mod['func_4869'] = func_4869
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4870 = relay.var("var_4870", dtype = "float32", shape = (2, 7, 12))#candidate|4870|(2, 7, 12)|var|float32
func_4869_call = mutated_mod.get_global_var('func_4869')
call_4871 = func_4869_call(var_4870)
output = call_4871
func_4872 = relay.Function([var_4870], output)
mutated_mod['func_4872'] = func_4872
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4899 = relay.var("var_4899", dtype = "float64", shape = (8, 1, 13))#candidate|4899|(8, 1, 13)|var|float64
var_4900 = relay.var("var_4900", dtype = "float64", shape = (8, 2, 13))#candidate|4900|(8, 2, 13)|var|float64
bop_4901 = relay.floor_mod(var_4899.astype('float64'), var_4900.astype('float64')) # shape=(8, 2, 13)
func_1628_call = mod.get_global_var('func_1628')
func_1633_call = mutated_mod.get_global_var('func_1633')
const_4905 = relay.const([[-8.164727],[-8.544650],[9.454458],[6.388324],[-7.180596],[7.314592],[3.101040],[-6.244986],[-5.598569],[9.094881],[0.756218],[8.297409],[-5.481135],[-9.360669],[5.217383],[-4.501431],[-7.491143],[-3.425066],[7.535462],[-7.369484],[6.633783],[3.017404],[1.691955],[-0.742617],[-6.957780],[-7.842258],[-0.565776],[-6.346853],[-9.915277],[6.692907],[-8.165962],[9.419179],[3.120482],[-0.789529],[4.810243],[-0.110847],[4.099200],[0.660543],[2.771270],[-6.575573],[-1.623144],[6.963218],[-8.771631],[4.655704],[3.275234],[-1.367400],[-3.394190],[-9.902376],[-1.334058],[3.420950],[-0.422111],[-2.649002],[7.701329],[-1.046845],[1.656529],[-6.228126],[-7.092798],[3.232625],[8.954341],[1.261712],[4.473261],[0.008620],[-1.541973],[4.204426],[-7.260760],[-9.347309],[-3.843800],[-1.662840],[3.889872],[4.942394],[5.892366],[-7.275403],[3.723667],[-7.636928],[-2.737067],[4.574316],[-7.891443],[-9.438932],[0.044495],[7.734220],[-6.842574],[-0.392767],[-0.626461],[-8.509775],[1.495442],[-9.318523],[0.295349],[-4.447576],[-7.602319],[-2.425381],[6.673935],[5.329643],[-4.190688],[-1.365053],[7.483811],[4.080492],[3.580260],[4.301585],[7.586029],[7.164284],[5.964237],[3.804117],[-5.946320],[9.929555],[9.344723],[-1.031117],[-4.639665],[-7.433518],[5.296455],[-6.849946],[-0.651498],[-0.414184],[6.002746],[3.439027],[4.356639],[1.007524],[-8.573391],[8.474057],[3.925770],[-4.315801],[-0.174311],[1.398397],[-2.562281],[1.343723],[-5.190502],[-3.567100],[-2.202668],[-1.433845],[-5.374588],[-8.448480],[9.401925],[-6.541729],[-5.263109],[-7.298323],[5.581926],[-8.033372],[7.987866],[-1.495281],[0.715304],[2.122928],[1.819199],[-5.431382],[-6.144352],[7.201923],[-7.896733],[-4.739499],[1.644769],[-6.977898],[3.816796],[9.214775],[8.559061],[-7.265486],[7.310059],[-4.167202],[5.143475],[-8.043628],[6.050416],[-8.314531],[-2.220312],[0.409710],[5.751113],[-0.567691],[-5.895748],[-5.158163],[5.707835],[-4.303263],[-2.212980],[-2.187426],[0.851021],[-8.928279],[-9.910151],[3.373509],[-1.096062],[-9.237672],[8.516740],[4.272430],[4.597805],[-2.678831],[-2.219922],[1.279140],[-2.416475],[-2.789089],[3.582066],[1.939613],[7.248675],[9.719543],[-9.116389],[-4.170179],[-6.043801],[7.353620],[-2.977183],[-2.226485],[-2.273648],[4.360192],[9.282339],[0.255400],[9.814980],[-6.186722],[-2.132395],[7.870290],[-7.758085],[1.012770],[-7.132439],[0.441453],[-6.182459],[-1.270545],[4.651446],[3.727782],[3.860854],[7.948765],[5.215229],[8.189176],[-3.022172],[4.379865],[0.050628],[1.986215]], dtype = "float32")#candidate|4905|(216, 1)|const|float32
const_4906 = relay.const([-7.727174,-5.486657,7.857528,8.051926,0.902159,-3.999938,7.158812,-9.720536,-7.438495,6.137722,3.562573,0.732021,-7.731966,-3.249484,-8.215831,8.089793,-2.145057,5.123827,-2.630125,0.736181,9.046329,4.049344,3.886143,-0.156875,3.212796,-6.027815,-6.264881,3.804419,-2.321666,4.205226,-0.858289,2.195026,-2.497571,-1.949406,5.873783,4.391283,-6.759536,-1.670432,-6.092158,4.675228,-6.281775,-9.592988,-3.332623,0.763470,-5.547046,6.719968,3.192673,0.777452,3.876637,9.974807,5.545526,-7.846500,7.255337,2.404892,6.012382,8.360472,7.396271,-8.985248,3.612716,-7.989028,-4.315431,-8.413343,5.214474,-8.985604,-5.823105,7.330414,-5.070076,3.243399,-2.545616,0.659841,8.676183,-5.731756,-9.081348,-2.466592,-7.434884,6.011237,-7.713972,7.590875,-7.432132,3.914345,2.556650,-2.869833,-5.792975,7.911386,1.992639,-1.975651,3.295749,0.145542,1.111686,1.133641,-3.340575,2.480994,-7.070944,-6.770791,-4.754469,4.538650,7.903225,3.578742,0.505035,-1.706223,1.575184,-2.158901,8.488519,-1.994886,4.743556,4.352253,0.135302,5.483179,3.151819,-8.810195,7.471379,1.020107,8.679434,-2.617704,5.360061,6.474554,8.730450,3.245321,1.135946,6.574191,8.983997,6.567710,8.931652,-5.889046,-3.049424,-0.742398,4.914623,-2.179114,-9.566537,0.153376,-3.994188,-2.027313,-8.686122,-2.644961,-8.137082,0.547487,-6.889823,-9.590747,4.809241,-2.975460,4.713202,6.053749,-6.087933,6.011147,-0.439763,-3.629739,-5.923604,-0.426462,-2.423282,-9.796515,-0.005557,-7.630812,-8.719770,2.277037,-6.987329,-9.329518,-5.415486,-9.129623,3.662348,-2.638701,-5.739726,-0.065702,6.094651,-5.609626,-8.000279,-3.920607,-9.519204,6.546672,7.445869,-0.665891,8.646152,5.142447,-6.994593,-9.075327,-0.684980,1.292153,-0.637915,9.570463,-8.809855,2.490180,-9.804452,9.998346,3.378528,-9.482825,8.626821,-4.170529,3.757612,6.519329,9.252592,0.496388,-4.270817,-5.607263,5.765300,-6.922128,2.564805,-2.028309,-6.706952,-9.334806,-8.529420,-5.185513,5.072507,-1.850734,6.607526,-8.539547,-4.069855,-8.890252,-5.364871,9.144961,-5.894767,2.249627,6.325229,8.585564,-3.758039,5.568773,-0.528700,-7.718008,-2.255079,-5.946723,-9.461781,-9.726755,5.423313,3.030437,-5.286415,4.429082,4.090012,-9.128838,-8.887097,-4.469198,-2.901387,5.481519,0.336234,-1.952811,4.712057,2.278334,-7.239427,-4.920708,-4.238447,1.230074,-2.683177,6.401802,-9.577384,-8.976105,-8.141466,4.290553,2.292866,6.325269,-0.389230,-0.417090,8.469051,-5.684300,-3.665673,8.469279,-6.520012,9.015992,0.519021,-1.841573,-9.909735,-0.676272,5.836414,9.234311,-8.399214,-7.490240,4.212329,-2.755692,-8.584711,-3.824017,6.177423,-8.075626,-4.163247,-5.581844,-0.782269,9.442808,-0.272420,5.713228,9.058911,-9.326456,-7.829022,8.321957,7.497479,-2.453272,-7.645345,-5.083831,-2.802534,4.497452,-0.011649,-7.152319,6.449078,-2.133112,0.835603,1.408569,-6.557211,-1.219692,-7.871218,-3.978472,-6.640488,-6.522686,3.457749,-2.350984,2.942031,0.252556,-6.710447,-8.531689,6.400484,0.073403,6.508470,-9.195539,-4.878793,-2.988565,-3.168741,-9.950751,7.637575,5.727752,-4.328661,-7.946612,4.535856,5.572604,8.233036,5.549738,-7.933766,7.170737,-1.526021,-1.516462,-4.181332,5.196067,0.382417,4.745537,-3.187310,-3.778581,0.223645,-6.277962,-5.614546,-7.233798,-4.292956,-7.966341,-6.873370,-3.064718,9.467587,3.702602,6.281703,-1.591990,-1.256056,0.165754,-1.875136,8.641085,-7.130187,1.059470,-3.365906,-2.194640,4.649176,6.364290,-3.918763,-2.868034,-0.624221,0.125912,0.829999,6.928869,-9.572458,-8.459745,-8.448707,-5.148932,-0.314995,6.779022,2.833554,5.337895,-7.208426,-6.317013,-0.269390,5.051307,-4.438258,-1.638551,-3.617728,4.815025,-5.034529,-8.379075,-8.809533,1.932486,-6.212399,9.219915,-7.929249,-7.607344,6.550449,3.358949,-7.868845,8.482105,3.575886,-8.350138,1.179603,-6.180478,0.941604,-2.159901,6.115389,-2.154506,-2.998678,8.457454,-8.526108,8.720803,-5.771766,7.665565,9.972210,3.539783,-3.194847,7.522578,-7.779457,6.591128,-0.865459,8.782183,6.793594,2.297585,6.235013,-7.299124,-8.582272,9.091245,-2.507619,0.202802,2.880203,4.990671,-4.845024,8.095733,-9.991083,3.417371,-5.377827,9.122086,-1.911747,6.063092,8.945760,-5.908965,-7.940316,4.675795,-7.461944,-8.464486,1.902518,-6.070705,-4.332391,-8.792349,-0.781714,8.591484,-3.860324,6.327802,2.862192,-9.043793,-4.344706,6.720629,7.928414,-3.291435,3.729677,6.409101,-0.850279,8.881631,-9.260139,8.917554,5.795006,4.143039,1.635787,-7.137886,-4.879456,-2.564193,0.043639,1.833688,-0.186398,5.526785,-7.318467,-0.185963,-0.614504,-8.708429,-5.688098,1.113089,-9.112431,7.076386,0.580541,1.584307,7.506039,6.402144,2.141078,6.302770,-2.936172,0.818466,3.913205,1.814252,9.729543,-1.261509,3.870005,7.865316,6.063490,-8.801926,1.062528,-1.328420,5.363547,6.307511,-9.334009,-7.639843,0.620762,7.715646,7.418706,-0.384313,-3.921079,-0.306559,4.851656,-7.346929,6.311633,9.723257,-9.708864,3.563963,8.478719,-9.198297,7.109687,-6.864635,-7.910862,1.286710,-1.185579,3.482553,5.050217,7.092436,8.489143,0.903533,-8.202768,5.296806,-2.143927,-2.069267,-6.166479,6.219832,5.205929,-1.005699,9.888036,9.291697,-7.019331,5.137022,8.944257,-8.980429,-3.162250,1.496620,-8.615514,9.749372,2.667624,9.994249,-3.302594,2.142644,-7.826478,3.567978,5.367235,-3.299139,3.706957,0.016527,-8.620699,-8.962392,2.570483,9.027592,-5.789683,-0.754083,-4.342786,4.999997,-4.770874,-8.541156,4.919434,7.924631,-2.720507,-8.961133,1.821338,-8.473205,7.609717,-0.694196,-5.078442,-8.538882,-4.835398,-7.647349,-4.722347,5.468347,-3.116826,-0.442361,6.221720,6.761358,4.701504,-8.832795,9.710384,-2.778067,8.014050,-1.711024,-2.900108,-7.930844,5.401096,9.226521,1.919518,6.396949,-0.504304,4.171272,1.202585,6.127802,-7.019552,9.770562,0.186977,-9.388720,-6.926907,-5.828343,6.940519,9.266449,-1.076932,7.419787,9.089957,9.367234,-3.492806,1.547323,7.342325,-7.169912,-9.189502,-0.768555,5.288944,-8.273230,0.805146,-2.888401,-8.977537,0.316564,-6.509320,-3.849264,2.121916,6.352738,-6.026499,3.751906,7.186846,8.557595,9.518014,3.543790,-2.555240,-4.071497,3.603201,-8.289799,-4.747236,-3.700382,-1.384296,-5.416886,-9.484501,2.773952,3.020557,7.314543,-9.415048,-5.452812,-3.439408,-8.995846,-4.837574,-5.485547,7.638159,9.819489,-7.928660,-1.654319,-4.249618,2.558572,-6.990960,7.407605,1.443321,0.251839,4.016753,-4.367705,5.452808,-0.321984,1.351781,5.602458,3.158820,6.762914,-0.425758,6.420468,-9.901641,-6.520450,0.067057,-8.293841,-4.772106,5.085949,-1.133664,6.085716,-9.479081,7.805276,-2.086560,7.344076,5.581660,9.944052,-8.873514,-7.143010,8.045226,-5.082562,-7.680910,-1.999622,-8.067375,-2.172209,3.902277,-3.440752,8.907262,2.821929,6.938080,2.983766,3.478261,-8.257571,6.698328,9.565884,7.212886,-3.529425,-9.568855,-1.661694,-4.661211,7.960914,-2.781039,7.737799,0.267306,4.106548,2.202103,8.401395,-0.543607,8.631516,-9.421772,-6.634669,-7.103252,0.826557,7.048790,4.732487,-3.882664,9.178233,-3.252831,-4.342874,-9.537588,-7.568398,5.424723,-4.344525,-2.787197,1.304189,-3.815506,-1.809889,-8.236494,-9.397296,-8.045102,0.537827,-5.858581,0.025398,-8.417389,4.825287,-0.946659,-8.206990,7.681437,3.502988,-6.438457,2.635282,-3.348554,2.305582,3.415177,2.838699,4.417677,6.008836,2.658173,4.712053,-4.418417,-0.057933,-4.602374,-8.543607,-5.069111,2.870119,2.574671,3.512610,1.179150,-5.361369,-3.201747,-0.753992,7.559076,-7.523600,-9.361716,-8.580788,-8.779862,6.865580,6.079126,-6.805240,5.696132,0.412804,-8.939220,5.664138,6.504493,1.500692,6.327002,-7.468297,3.355309,9.516159,-2.417926,-0.382562,6.734823,1.255547,-2.257283,-2.342101,-0.988063,-0.349595,-9.325488,-4.230263,9.749129,-3.106614,0.213944,7.119439,6.499221,-1.338662,-3.193787,-1.667809,7.599168,0.476366,1.374023,8.508943,3.403794,1.987085,2.332937,8.774865,9.245134,1.362570,-7.849751,0.327531,-5.169243,9.975227,-3.949583,-1.969321,-9.182440,2.591942,5.603947,5.852449,-5.100274,-1.164068,-6.165836,9.577196,9.804811,-0.065306,2.095373,3.475865,5.086690,2.376410,-0.011566,8.069981,7.162135,4.296034,-7.813090,3.921359,5.799125,-4.122417,8.453691,5.950304,2.735118,1.079056,7.728190,-8.650665,4.177385,-5.251900,1.212438,-5.917161,5.778226,5.927885,-3.336368,-3.913268,-7.370373,8.062166,-3.779647,9.341013,-7.642309,8.565399,7.157961,3.065071,0.449077,1.817124,2.726210,8.615226,5.291038,-3.575409,5.221556,4.261375,-5.183837,2.315110,0.346025,-4.121659,1.531073,6.658819,3.976104,-4.068072,-9.294016,8.092128,5.723868,-3.602851,9.269734,4.502187,-8.623736,-7.353263,0.206766,2.904906,-9.613042,3.490773,4.133293,0.679553,6.554726,0.646799,3.081600,6.142783,1.671479,4.636227,4.607936,0.571219,9.880575,-2.434914,-6.845274,2.533670,3.948553,-9.907549,6.344725,8.305668,3.169741,-4.458141,9.022069,-5.839296,-7.625540,1.255541,-6.577949,7.424221,-2.111943,-1.163821,8.483123,-7.385739,-7.304190,-0.087438,-0.683320,-6.784059,-9.472029,-3.008655,8.275502,4.906206,-1.364926,2.781941,7.616265,-0.708416,-6.579274,-5.122248,-0.401265,-7.456510,-2.733776,-5.107042,-0.195895,-9.748652,7.689384,-3.259179,3.506353,-8.091051,-4.971467,-1.511992,-3.574340,8.822486,-5.954652,4.033015,-9.948333,6.235884,-2.429989,1.159890,5.104521,6.457428,-3.386816,3.638165,2.699317,6.540508,2.813826,-8.218973,-4.296285,-6.589359,8.565216,3.874227,6.082024,-3.258230,-4.844046,-0.827986,-2.716455,3.559589,0.401948,-4.046395,-6.621696,-9.394942,-9.344136,-2.816066,-9.613195,7.867600,-5.279593,-4.342426,3.231099,2.534203,-6.862909,6.170918,6.420775,-8.279170,4.847356,-8.397751,-0.379570,1.197682,8.978310,-1.010166,-5.536968,3.727444,-6.995481,-5.461359,8.426566,-8.523388,3.203985,-7.766943,-4.366751,0.532362,7.511284,2.518150,-2.996518,-3.415184,-4.548970,-1.644226,-8.009951,8.756662,7.458584,9.634987,4.303474,-9.062622,1.669610,-2.065677,5.283707,-6.584723,9.326614,5.647784,-3.581331,4.715375,-1.673883,-0.031707,6.518976,0.063069,5.946059,6.950079,-6.420173,-6.081599,-9.765065,3.240514,-2.935335,5.563958,-7.076846,-6.197289,-4.072277,3.188970,1.313654,-5.229025,-6.217117,0.198124,-8.800182,-4.871239,-9.405870,-9.880898,2.671840,6.575813,7.094247,4.867755,1.907417,3.989380,6.264627,-1.638581,-3.305369,-8.531850,-3.482638,-5.045101,-4.212378,-3.136574,2.606718,-9.572295,-6.226264,7.902274,-1.154413,9.276717,-0.966112,4.609657,-8.384402,-5.849092,-6.552838,4.912027,-0.652937,6.372846,-6.508377,7.180856,0.477598,2.741631,5.262854,5.881707,9.014539,6.395516,7.574648,-0.482979,-1.433879,-3.683571,5.243257,-6.237543,-5.986708,-5.982946,1.738923,-2.676655,8.937855,-5.357584,-5.523982,-4.062302,5.612996,6.853311,3.606090,-9.332551,-2.409594,-9.496036,-7.569813,1.218353,9.285595,6.760079,-1.637236,8.455588,6.996387,-8.255596,8.639174,-7.543269,6.458728,-3.365808,5.277776,-3.734769,4.393274,9.406926,0.588834,-2.302584,-6.404390,6.131837,-7.925572,9.831862,5.387236,4.397367,-5.935438,3.838350,-9.068032,-9.138134,-9.221304,0.754835,-4.231901,6.132296,-0.084862,-4.447632,6.839499,5.926009,-8.896001,-7.859576,-4.581293,-0.792641,4.213843,-1.629876,2.840263,7.858089,-9.196431,-3.228087,4.848352,-3.002003,8.445035,-5.977911,8.551721,-8.565746,-2.710828,5.376473,0.005582,-7.468969,0.199724,-8.362067,4.322806,-5.691836,-8.870498,-3.818607,-0.356580,9.227115,8.924850,-7.750443,6.631241,-1.156234,6.558490,8.127737,-1.576280,8.930830,-9.222957,-5.197733,5.745030,1.535769,7.520086,0.860217,5.555790,-4.447224,9.766917,6.313847,1.233351,-9.496622,1.967796,7.904415,1.180944,5.134244,-5.644914,-8.786748,-5.552248,-2.110781,0.387841,1.094014,-4.019893,-2.584375,-3.372827,9.224460,7.526161,2.501394,9.468437,-7.082726,0.481127,-7.134079,-6.357991,-3.874109,8.515612,-9.238366,-1.304462,2.971687,4.708931,-0.389539,9.226302,-8.405007,-0.371820,5.073808,-0.039037,-1.442023,1.240080,-6.531635,7.638553,-5.016679,7.166639,-0.880521,-4.416538,-9.883122,5.991341,4.002019,-8.384224,1.700395,0.564132,-4.848543,5.112042,-9.615324,-0.048000,-5.788395,1.429910,-3.695351,5.046905,-8.934625,-2.356932,-7.817377,-1.369399,-4.317938,9.114685,9.080577,-3.848207,-8.712273,-2.550148,-4.125651,6.395689,0.325253,7.209994,5.257813,-8.384540,-0.133418,6.110972,-8.558300,-5.380979,-8.230995,-8.769719,2.883323,-5.188584,-2.216826,-4.364730,6.572211,8.170943,-1.697462,-6.861505,-1.285790,2.941306,2.663518,3.911539,-4.221548,-3.570493,7.177348,-8.256461,7.423373,-7.535294,-0.941020,-9.209992,7.711618,-7.517923,-8.085082,0.364624,8.974910,0.834696,7.514147,-7.628392,-2.704096,9.322845,9.543183,-8.710758,-4.715835,4.855438,4.634352,-4.714318,4.831171,-1.485560,3.612179,-9.249621,5.146426,4.950087,-0.647245,-7.225735,-1.491712,-1.364505,-5.061339,-4.848433,-2.644382,4.563397,2.765813,-5.331112,-9.160791,-2.621827,-2.132485,-4.474406,-4.303584,8.714287,3.386682,8.416872,2.842223,5.370617,9.709613,-8.975372,0.949704,6.124750,1.462264,-4.753567,6.133287,8.098657,1.963061,0.328873,7.089265,2.081174,-7.836452,-6.598884,-6.842855,2.931458,6.976201,5.992322,1.791165,6.348749,-7.394073,-5.334741,-1.791524,-5.176655,0.700970,4.543766,-8.410101,7.597393,1.072308,-3.870461,-5.058097,2.356004,3.109280,-1.003535,-3.587175,6.939380,2.370755,-8.694003,9.681698,-0.035925,-9.733886,5.878181,-6.774499,6.871766,-1.843731,6.345392,-8.094677,-3.601558,-3.843820,-9.146272,-2.012454,6.810677,-5.487198,5.190159,-8.594575,-2.306409,1.605944,3.791226,0.281097,3.373018,-5.442791,-7.640335,-0.113633,-6.917057,3.595145,8.574357,-0.222866,-9.418928,-2.273771,-9.030372,9.838411,5.765885,-0.460775,-4.317491,5.560367,5.792603,-9.621767,-5.562824,-2.311141,5.530679,-2.063282,7.152030,-7.348505,1.721412,1.304896,9.302297,-0.217709,5.246267,-1.642137,-6.462743,-0.701464,0.178582,0.351756,0.994902,4.748942,-8.062253,9.158182,-2.092533,4.647926,-3.630684,-1.111983,3.485187,-7.269451,5.061481,-5.309362,-0.487376,-0.729252,5.389634,-1.614974,8.591544,-7.679685,8.492286,-6.899885,1.708375,3.979650,-7.509696,9.569982,-2.215310,0.952297,-8.073802,-0.378377,-0.972465,9.362512,-5.840190,-9.487770,0.416307,1.815284,-7.473925,-3.435618,1.845722,9.705893,1.089305,5.384989,-6.514781,-1.711219,-6.843445,4.105558,1.244619,9.113644,-1.155134,7.876065,-0.676231,-1.673149,-8.804145,-7.224856,-0.662577,-8.923168,-5.315355,-9.252656,-2.772310,-5.850196,1.931244,6.739169,-2.464020,-2.097724,-6.584300,-8.240471,8.828316,1.270582,6.874177,8.341465,6.388476,-4.140473,-0.344201,-1.647987,3.814823,5.098683,-5.187752,3.974045,8.699034,-9.143881,2.934675,-9.575718,8.452570,4.674832,0.368124,5.626582,-7.937966,1.103639,-4.354288,8.703129,-7.810011,-7.624596,6.115795,5.040749,5.867701,-8.210343,-8.745806,6.160312,-9.796727,-1.768449,-5.076619,-9.991393,6.157923,4.546480,8.608055,6.493288,1.544077,-9.222530,4.155358,-4.939472,3.052924,-8.419204,5.577167,-4.127074,-5.814713,-3.905685,-2.417262,4.144221,-2.680605,8.138755,8.097304,4.811283,-7.929059,6.051361,9.697943,-1.607559,-9.812156,-3.940069,0.050766,2.651455,0.473646,-3.994986,-5.785544,-8.791926,-4.093239,-0.841336,-4.666895,-8.311878,7.593980,6.650850,7.228659,-1.329308,-8.238474,-7.110230,1.061637,4.166943,4.106296,-2.141422,1.003074,-2.611016,-4.898130,6.472362,-0.896828,1.517744,7.385186,-2.607442,-7.648050,-2.411213,5.105483,-8.626916,-3.369433,4.180888,9.582085,3.760822,-6.418561,-9.589662,-0.031997,-8.254930,-4.276923,-5.425094,-5.634802,-2.873445,5.431990,6.380811,0.095433,8.206550,2.714727,9.689724,-6.653588,8.603611,-8.577020,4.098896,1.328088,3.701021,0.120977,8.315537,-8.970967,4.850106,-5.976607,-0.534397,-5.819417,1.681320,8.944966,5.376005,4.601048,-9.612691,-2.840639,-0.240763,7.400447,5.604345,9.442636,-4.995743,8.742807,-0.662096,-1.412158,1.223594,-9.530391,-4.109034,-6.855445,-3.993370,-2.049574,0.459109,-8.996241,-0.217498,-3.024409,1.889516,-0.512752,7.952518,2.714229,7.308943,5.872767,-5.594910,1.989632,0.773041,-6.105472,3.205296,-5.167039,-0.675009,-0.274478,0.614826,-4.996655,1.143214,-7.611912,-8.756666,-3.789893,-5.351936,2.047789,2.101841,9.044237,-1.866044,-1.833515,0.982461,-2.593496,-8.407683,-9.219924,6.527476,-6.508341,-5.728925,-4.184965,-6.295131,-2.607484,-5.198796,4.748316,7.196050,-4.636582,4.368894,3.119121,6.785563,-3.901709,5.911610,2.997985,0.730021,2.932395,0.627911,2.290824,-0.810272,-6.645669,1.527379,-4.162588,-2.097468,-9.688473,-6.408175,-5.243136,3.257576,0.832312,-4.361985,-5.684748,-1.842612,7.174384,2.989870,2.766107,-9.665420,-1.115492,7.666498,-2.604619,6.376534,9.703551,7.664656,4.188507,-7.672460,9.865759,-3.514836,6.416649,9.317947,-4.468916,5.638369,-3.523681,1.060989,8.595824,8.480807,-3.874136,-2.277960,-6.911404,-5.645419,-9.697024,-3.525639,4.435124,6.160976,5.045057,6.978025,5.470345,9.242140,-4.647673,-8.743440,-8.139631,-8.362454,-7.954766,-1.246483,-4.181183,5.024456,-9.753318,-0.875211,-0.447308,-3.034056,-4.284711,1.777661,-0.580069,0.958938,8.020350,-8.147662,7.560884,-4.476173,6.565238,9.662531,0.234691,-4.965285,-5.264589,7.668881,5.616200,3.241927,8.248148,0.492223,2.477019,4.974916,0.854193,-5.887177,-4.940838,-4.305755,-8.015654,6.072872,-5.137101,3.722080,-6.514371,9.628028,-7.758613,5.053316,0.138467,8.925879,6.140686,5.421578,-2.807110,5.539181,3.990762,-5.454125,5.070448,2.732427,0.832209,1.985017,-7.847051,6.223764,7.817557,-5.346808,-6.819507,7.686618,-1.612880,-5.596964,9.291495,5.147569,4.653449,-7.483840,9.798295,3.334793,-9.419407,-9.046536,8.901774,2.018316,-0.222158,-2.025606,2.908266,-5.369373,-9.094018,-7.891780,7.418635,-1.279515,0.191783,5.616280,3.343650,7.082256,7.980257,-3.868223,-9.630229,5.408345,9.434690,6.975602,-1.488076,9.792872,-2.830941,-5.773476,8.716808,-0.537067,9.162230,-6.071387,-1.443495,-6.437809,1.262072,1.489488,-0.385107,8.252414,-8.199317,-7.230336,-3.505039,2.543819,4.365982,-8.634459,2.741128,9.029299,3.848183,7.377279,6.057633,2.060774,-4.228152,-4.354922,-4.845473,-9.982313,-6.560699,4.062365,-6.521673,2.427403,-1.443261,8.472138,0.996111,-7.488095,-9.181011,-8.520892,5.363423,-0.365235,-0.764151,-2.371999,-5.743871,6.632592,3.836114,-6.122465,-5.971268,6.434949,3.034158,-6.050396,0.395383,7.560887,-8.170689,0.246852,-0.695537,7.680764,3.055249,6.964567,-7.602509,-2.758167,2.205708,-3.648046,7.734110,-1.586932,-5.340901,5.172194,8.588339,1.213664,-7.466543,0.352782,-9.386311,-6.747424,-4.191081,-5.200851,-8.311855,-5.042381,5.389514,0.889344,-2.508881,7.025182,-7.937570,-2.641937,-4.955332,2.119104,-8.734882,8.448620,2.211864,-1.290228,3.039315,5.009976,-7.710985,7.985768,-5.817910,-4.775605,-2.283264,1.098677,-2.403352,-1.622966,0.243077,1.474992,-5.364858,-2.763729,-7.003373,6.930598,0.962459,-5.930621,-3.754173,6.882137,-2.556874,6.291422,-6.933644,-1.475290,-9.012313,1.185160,-3.749363,0.745480,2.330025,2.606719,5.942059,0.993639,1.978715,-8.195790,8.205179,-4.217534,2.618322,-4.969169,-5.856357,-4.727367,8.822551,-3.853453,-4.107336,-6.663486,3.371519,-0.567499,-9.985272,-9.292718,3.961414,7.547021,-8.876693,-2.560805,7.754807,1.648782,7.725162,-9.907072,3.580232,1.226370,-2.490780,5.693875,7.597036,-0.221958,0.300841,7.205190,8.969280,4.451913,-8.359458,9.731787,-4.030272,6.497234,-4.745374,-2.960736,-6.358313,-4.097892,2.343891,-0.654165,0.002636,-7.611045,0.765827,4.170688,-7.298268,7.904813,-5.556931,-2.585578,9.933067,1.727191,0.179000,-0.495505,8.785298,1.834312,-2.215966,1.317333,-2.960907,2.719510,3.937030,6.764330,1.583420,-5.964817,0.018451,8.215576,-8.295277,4.573611,-5.037060,8.066388,-3.235876,0.448380,-3.667121,-6.874234,-3.555236,7.750963,-6.777637,-1.748722,9.563901,9.793247,4.992753,9.944609,5.663895,-1.594182,-3.887317,8.545709,-0.055884,-7.495862,4.033011,4.925859,-1.705455,2.779244,5.133326,-6.117012,-3.076154,-9.490060,-9.104041,5.038416,-3.603853,-9.279288,5.685118,0.513647,-6.443609,7.997991,-8.675063,9.140370,1.294690,0.839670,-8.324606,3.163541,4.803664,4.285874,4.205807,-9.550626,-4.026725,3.846583,-4.395625,8.176586,-1.331580,4.107037,8.563705,9.863944,1.196601,-1.801155,-9.100394,4.400134,9.744786,-0.547414,9.730970,-2.924136,4.329129,-0.392792,-1.243816,-8.911012,-5.474059,3.790999,-2.263764,-2.606643,9.564878,-6.490050,-7.581500,6.624402,-8.091959,-2.456798,-3.021429,8.986672,-9.956067,-0.039600,3.864590,1.860632,-5.486778,6.482325,8.820047,-1.076096,-0.374591,3.095600,-1.700224,-6.897269,-4.477665,6.513716,2.020398,-5.798975,-9.022787,-2.229270,9.704226,8.946881,-0.009868,-4.646789,-1.692901,-1.131970,2.092426,8.037035,8.384609,-5.384279,-2.553982,-0.272271,-7.388455,-7.823299,6.856352,-9.417647,-6.599288,-8.862846,7.706402,1.833470,-1.704640,-8.257174,6.503621,8.607999,-0.835018,-5.309406,1.480867,-6.363009,2.213807,-5.485951,-9.766385,4.622588,-0.001567,4.620008,-1.824159,3.697766,8.975622,1.400108,6.333084,8.853380,-3.848629,9.316966,-5.032025,-3.340599,-3.947951,4.452621,8.184041,9.594909,-1.210951,8.240347,7.351233,1.299622,2.136449,9.852302,-5.660033,-3.480442,-0.583389,-8.419754,9.597453,-7.423174,-2.521734,-6.126745,-9.829353,9.888134,3.106571,-4.089756,-8.082758,5.615745,-9.517601,-0.585391,9.242335,1.564020,-9.206432,-3.844906,-1.148372,4.033350,-3.366274,3.523400,-1.683520,-7.919333,9.527639,-6.395662,-5.912475,3.366758,3.017096,9.238098,-1.411309,-6.032397,9.454375,2.120184,-8.574103,-6.650598,-6.242976,9.538663,-8.301257,-2.278453,-8.301974,5.788538,-9.664811,9.563130,0.503822,-4.152626,-4.053055,-3.759562,-5.577580,2.680995,4.176257,6.606423,3.632372,-4.374872,-5.364816,-7.757495,4.732710,-0.663305,-4.289761,6.894859,-3.323413,-3.908613,7.754513,-3.122959,-1.847280,-0.794303,1.401064,4.785739,-4.150589,8.731889,1.164131,-7.268958,9.476624,-5.945530,-1.536712,4.636500,-1.109445,4.547258,2.990503,4.727026,-9.831620,4.870165,1.846440,-9.322682,-5.041545,8.571443,4.558339,-9.704021,-0.787038,5.508051,0.328613,1.803732,-9.193101,8.819292,6.383727,7.678647,-5.427083,7.719044,0.301054,7.573934,8.782260,2.812436,-7.826908,-2.488146,6.668208,-3.249233,-2.554890,-7.982066,-5.392006,-9.894439,-6.663322,6.224774,-4.270173,-9.726105,4.673567,4.576314,-4.712727,9.146811,5.573098,6.441534,8.501770,1.641401,-1.623084,-1.645102,5.931163,-8.072234,-9.350797,-2.640610,-7.269872,9.387686,-5.889627,0.132943,7.772069,-4.269647,-2.358042,2.890450,2.308715,1.507585,-2.939415,-2.600073,7.159782,0.096688,5.590139,-5.555655,4.403156,4.867761,9.467252,-1.347544,0.601302,3.334525,8.697232,-8.203321,2.368101,-5.096247,6.075218,9.247469,7.204826,3.606564,-4.542986,-6.254510,4.706421,5.310907,-6.296909,9.145213,-3.774603,1.588296,-2.248967,-5.433803,-5.403987,4.019629,-6.484939,-1.714760,-1.698842,-2.805839,2.995536,-3.305777,-5.237803,2.163410,2.640925,-8.166931,4.610778,0.189091,9.078629,1.312948,-5.653888,-6.260533,8.740649,-6.882380,-0.776347,-9.601168,-8.658578,-9.006933,5.479156,0.186778,-4.527301,-2.145769,-5.613172,0.092499,-1.915882,9.516085,-7.801920,6.380191,-5.964652,7.657563,-3.839041,-0.515019,-2.227998,0.402373,4.998948,-1.938924,-8.574395,5.925744,2.874794,6.805106,-4.836900,-1.191330,-5.851897,-3.581243,-6.503928,6.490629,-9.874869,7.421458,-3.743923,-4.988491,3.440909,1.422152,8.665600,-8.401115,-4.874636,-9.679287,-9.711386,1.520498,-5.533742,8.545915,9.325613,0.887189,4.177239,-4.113103,6.479913,3.442414,0.816138,6.142476,3.123380,3.624385,8.476474,-2.964509,1.038202,-8.966239,-1.555557,-9.578958,-9.516548,3.405630,-4.784658,6.341452,-5.662311,-6.180462,7.581014,-4.829906,-0.858391,-2.489197,-5.302449,9.262171,-8.464589,2.617047,-9.592370,-5.953703,-6.057318,-5.051550,9.533292,-1.919457,-7.622289,-1.004938,-3.341475,-0.939676,-5.586284,-8.710476,-8.169444,-0.010334,9.053114,9.415980,7.531651,-1.537105,0.244938,-9.753771,-9.678204,-8.523173,-4.340358,1.420453,2.646058,2.371010,-3.693978,-7.653075,3.341135,-1.796353,1.678015,-5.441595,9.047709,-1.631837,6.295934,-9.354752,2.151234,-9.942432,6.719135,7.710800,-7.189933,-3.254958,-9.455946,7.510816,-8.274219,7.222076,7.472341,-4.940574,-0.686838,0.923527,-8.770190,-3.781455,-4.639602,1.144301,-4.008438,-2.988473,2.046011,6.895973,-7.639312,4.510563,-2.403251,-8.975530,1.664593,7.232808,2.393421,9.903063,-5.422144,6.332321,5.882688,-6.782113,3.183415,-5.528997,9.518688,8.677280,-6.184933,-8.995812,4.454156,-2.581350,-6.241532,-5.697137,-8.893173,2.592471,5.385750,0.463339,5.186688,-1.522124,-7.451658,1.025580,1.599598,0.284605,6.559044,-0.542561,-3.787705,6.369140,-2.803231,-4.656757,-7.770334,8.244887,1.709274,-3.952748,-2.051368,0.397318,2.337336,1.237609,5.778572,-3.708684,-5.940785,6.926906,2.999751,4.479521,0.611329,-5.681218,7.496787,9.637269,-6.956363,7.052048,3.649722,1.905249,0.880219,0.193723,-1.832435,-5.349435,-1.795738,1.230518,-4.844968,-5.532892,9.646703,2.352616,-2.448464,4.545137,-6.496363,-8.217918,2.880719,-8.493248,-8.599837,-8.666279,6.838906,7.940804,-6.876446,1.855626,-0.867731,-1.274793,-7.818479,-8.320223,5.257007,4.839012,6.430116,1.874589,-4.572648,4.234932,4.638007,4.322063,-9.177010,-0.687625,4.953771,-7.854398,5.618443,5.392293,-5.111939,1.468016,7.555423,-5.140153,-9.836198,-1.964338,0.426263,7.816540,7.979713,-3.270847,0.966045,-5.707855,-3.018260,-9.950089,-9.994816,-5.215176,-8.622252,-5.833216,-7.798050,-9.565692,-4.306330,7.656100,-9.637100,-8.662957,2.777040,-1.893587,2.341774,-5.828363,8.775829,-0.628771,-0.345906,-8.883856,-2.081970,8.130240,3.233853,7.009397,-8.627029,-4.020111,9.914844,-6.109021,5.111566,8.268039,2.662349,-5.953768,3.436014,-1.123201,3.861703,-2.100493,0.447728,9.406987,8.652407,-9.699383,2.450145,-5.718060,2.574329,-2.604444,8.224611,-3.139259,2.889848,3.644153,6.952159,-9.002836,5.478061,-1.172111,-0.572591,8.188619,-0.665914,5.698736,-2.551044,-3.467225,-1.994993,-9.130263,-7.171547,1.108854,-8.075762,-9.169578,-3.712046,-4.436371,1.482302,9.947597,-3.077641,4.883043,-9.732705,5.884680,8.997214,3.232849,-5.875705,3.360017,-4.943537,-4.072877,-8.115568,-0.997502,4.269861,-1.233460,6.079050,9.350211,-6.186809,-1.711957,9.762401,-9.858314,5.428954,5.298881,3.484362,-8.655731,3.456007,-8.108047,-4.990964,-4.096373,-9.857580,-2.873121,-2.134342,1.414967,5.037518,-1.839876,9.018594,3.336120,-7.353317,-2.225665,5.859172,1.966527,0.908114,-5.358907,-3.275493,-3.453691,4.973670,-8.547569,-2.168303,1.309370,1.975136,-0.364491,-2.313315,9.427974,-2.218153,-0.112208,-6.110636,-4.844424,-7.516045,6.821033,-4.929980,0.571109,5.423871,7.565693,5.371881,2.788084,-0.757877,-3.480577,9.018603,1.366755,9.659333,7.487956,5.141815,-7.705513,9.051351,-0.149988,2.030852,3.703823,7.309108,-1.338034,1.249424,7.497615,1.633931,-9.202417,9.376101,0.593678,-5.333809,5.847357,-7.450074,0.624657,9.163009,1.887075,4.970993,2.470719,-2.329892,4.447440,5.253982,1.141208,-8.567894,3.613910,-3.935687,9.826889,-5.080441,-0.668084,-4.843206,-9.878190,-1.337544,-2.536527,-6.913381,-1.524987,0.532082,3.082457,6.441317,4.079417,-1.037927,0.855376,4.167881,4.351631,0.325499,4.733253,0.656487,-9.287059,4.632154,1.934311,-8.296996,-6.494983,-9.519184,4.432851,4.485598,6.325255,9.411288,-3.900163,9.501066,-8.108471,0.062932,-0.210885,8.838185,-7.796063,9.796359,1.805083,-7.421401,6.134305,9.798734,-4.082877,-0.055187,-4.182900,-3.580112,-8.237929,0.063569,4.446728,-2.346383,4.970242,-9.904251,1.617346,-2.843047,9.390700,-7.356332,6.775913,6.989814,-8.065682,5.041707,-8.722016,9.723309,-3.059045,5.391725,-8.439121,5.038359,-0.100195,4.380249,-8.391364,-4.740134,-3.432540,-2.447121,-1.584154,1.754411,7.512414,2.686912,4.144473,3.816330,0.885641,4.842776,-7.162548,-9.745441,-0.028874,-9.322760,5.145172,-3.907652,-6.048892,2.955924,7.502367,1.064638,8.785715,-9.996650,-9.736407,-4.098253,-4.827835,6.300349,3.756732,7.185988,9.711288,-9.859632,-4.030187,7.548330,0.914530,8.395086,4.561910,-8.631103,-2.625821,2.408792,-5.928685,-4.568511,2.525474,1.936640,2.540963,-2.952933,1.409313,2.576536,-2.591164,-1.826722,1.842928,-6.181361,-7.307899,-7.102637,4.318101,8.717722,5.738443,-7.648333,8.821669,0.941255,1.896834,-0.438400,-8.692316,-5.742354,-7.904844,1.373468,6.927046,-8.935297,-1.449514,-1.126118,7.574479,1.885341,7.876642,3.774445,5.844409,-7.286017,3.377617,2.590377,-7.999297,-3.593354,-5.597247,7.752749,7.248806,-2.572449,-8.647013,8.929496,-6.743930,-8.245822,-7.931128,4.892469,9.826709,-4.411499,-9.963257,-2.297311,-5.965478,9.270683,-4.622031,-3.996497,-6.694123,3.260665,1.619279,-0.956800,7.057741,7.558281,3.284602,-2.088730,-1.463010,1.661221,-6.316414,-3.720837,-6.048263,-3.197344,-1.423442,-1.587889,8.652983,4.758283,-8.790328,-9.192531,-6.052532,0.117954,-3.095339,-3.211352,4.466097,3.355627,-3.948201,-1.364757,6.923974,3.578991,5.138990,6.304348,-2.977342,2.487799,-4.242092,-8.654171,4.608663,-4.884557,6.770275,3.880842,-5.058784,4.780936,-6.430036,5.409334,-9.841716,7.541225,-2.416934,-1.181287,0.042908,7.161957,2.677763,-4.358627,-7.683911,9.046874,-3.613025,-9.582926,5.978453,8.568764,4.030574,-0.449956,8.454189,3.603319,-7.090800,-3.419906,8.373940,9.102677,-4.162881,2.012122,2.996020,-8.368140,6.131228,-4.130000,-5.760202,-6.929460,9.462762,8.898123,-0.195642,-8.790621,-1.695749,-4.333759,4.959424,2.639174,-4.027589,-6.509698,4.079676,3.012067,5.537120,2.598542,7.416671,8.941055,-7.427455,4.643129,3.183480,6.840861,7.803061,7.917391,-2.983424,-6.600043,3.386712,-3.045065,1.157529,-4.683957,3.376452,6.294918,4.009569,9.836972,3.083804,8.057588,6.112882,2.280799,-0.337925,9.334336,1.864762,7.879881,-2.593069,8.862478,3.762395,-9.924395,0.634275,8.346894,-1.474373,4.853610,-0.804552,-6.506999,9.527656,-1.636917,-8.548358,-4.309167,8.634353,-0.885964,1.029670,3.892992,6.333983,-4.828836,0.439366,-9.800379,-6.898784,-5.449022,-0.813756,-0.736347,-7.719929,2.079682,-8.028411,-5.310484,-1.620447,4.878994,-9.633941,-8.477605,-0.001990,-9.381484,8.657322,9.324028,-6.369708,-8.075855,-4.542235,8.131581,5.793608,6.438002,-9.521875,1.500528,2.053829,5.050691,8.574022,6.670563,-7.662603,-6.805964,-9.250241,7.790915,3.735254,1.393083,0.950502,-5.571932,-1.959494,-0.993183,9.254576,9.840490,0.289641,-6.661519,-4.765387,-2.675350,0.859118,-6.591103,4.562263,5.367444,5.081698,-1.213029,4.874534,8.998654,8.536158,-8.388955,0.780404,9.505428,-1.963730,-7.123429,2.133865,4.076201,9.464011,3.231630,-9.851300,8.790329,4.322973,-6.309633,-3.292686,-1.612199,7.621381,-2.137629,-7.074128,4.881133,4.497982,-2.623178,9.140338,1.410322,1.155210,3.541309,6.878123,-9.729119,-8.826913,6.344957,-6.434745,-1.422228,0.183748,1.384940,-0.849828,-8.066271,-7.253687,3.187783,0.171623,-6.273654,4.487525,-6.413906,-5.439771,2.476797,9.784315,4.131956,3.164782,8.450383,-0.871521,-4.385854,-3.512305,-6.997991,4.855818,-8.117517,-7.513339,-0.297648,-4.525611,0.033865,8.975511,9.481640,9.308633,-4.413708,1.210076,6.472468,-9.992156,-3.721576,6.295495,7.446620,-2.826592,5.191133,-6.555551,-8.564072,-8.585199,0.984017,1.956717,-9.923948,9.679870,1.548787,-4.327537,-5.374494,-2.282577,0.072177,1.996314,2.288057,-2.266847,1.710685,-8.562129,5.485629,7.495475,-7.955408,-4.595069,7.118472,8.834479,-3.932326,-1.795293,4.558756,2.893436,-2.599031,4.954458,3.916827,-4.856397,2.444202,-2.522969,4.755238,2.864182,-5.759965,-5.607692,-1.296630,-4.660135,6.962303,2.855125,-3.009622,-8.763464,-6.076822,-3.343835,9.342790,-0.958467,2.511489,-6.694806,-9.786978,-4.799119,2.185106,-6.875207,-4.753842,-6.010197,2.354680,-5.586611,-0.531225,-5.617099,2.586938,-1.861588,1.053744,4.168539,-3.382193,8.422774,7.179164,2.377029,-1.866998,-7.081262,9.887999,5.657400,9.567030,-6.120794,-6.512573,-0.345908,2.957359,-0.413015,5.618619,3.615981,1.120214,-6.865187,-2.243728,7.616200,2.596395,6.243351,-8.015855,-2.786585,5.507893,-3.031721,2.319279,5.259128,4.693134,-7.637618,7.529749,-8.440302,-0.384614,4.105056,3.438019,-1.625656,3.978048,5.793564,-0.129338,2.138269,-9.059729,4.209202,-1.546154,-7.125004,-9.856064,-3.287356,-7.546801,3.963928,8.148831,8.711632,9.397074,9.778264,3.211186,7.288713,-3.927961,8.231413,-2.066764,6.664041,9.088927,-0.033751,-0.552668,1.625582,-2.094451,5.991828,-0.491092,-6.558725,-1.148074,-7.119830,-5.812876,1.850169,-6.490113,2.108522,9.191788,5.597152,-1.622701,8.493715,-3.862652,3.328701,8.475368,-9.572675,1.925087,6.760209,-9.418037,3.215040,1.928846,-8.365472,-6.352714,-1.923976,-6.942207,-0.120268,-7.263297,5.349295,6.537020,1.260980,8.185536,-7.780160,-3.750975,3.099320,8.877122,3.630553,5.448592,-3.015501,6.383723,-1.643793,-1.774225,-1.177620,-2.175174,8.119257,-8.126468,-5.596871,-2.124231,-5.724034,-3.407162,7.283353,-8.894411,2.627433,-2.405809,9.737396,-2.194996,1.773028,5.642935,3.890665,5.203739,7.223943,9.970227,-0.554907,-9.648680,-8.538511,-5.983386,-8.050908,-1.220031,-8.326591,8.468485,-2.013660,7.912317,-2.873404,8.211730,-1.432652,-0.624071,-7.559389,1.466247,2.509466,4.373919,6.235146,9.423898,0.639359,3.151551,7.538890,5.984633,-0.888641,7.179819,3.364832,8.116494,-4.327193,8.175932,2.072343,9.158564,-4.299448,4.547396,-2.425566,6.923350,-1.831722,1.724355,0.690314,-2.732323,-2.801643,-7.337610,-0.914141,4.865145,1.292465,-9.995089,-8.660315,1.539750,-1.260165,-4.189933,-5.763105,-0.501429,-1.747863,-7.764048,1.942047,0.005311,-6.209228,6.452451,8.738747,5.712105,-5.176328,-0.726826,0.680228,6.240668,-7.175771,-0.421203,-5.480816,6.483749,3.133007,-5.921219,-6.275377,-6.542707,-7.553618,-9.027310,-7.893064,-7.685506,1.841332,7.520038,3.011703,-5.168601,-8.468312,-0.508422,-5.253561,8.450086,9.270692,-8.773295,-2.043670,-7.689632,-7.575175,-2.845384,4.607875,7.901390,2.180875,5.668396,-1.670525,-8.792169,2.085912,7.265487,5.056344,4.194269,-9.068926,-2.601652,-6.412656,6.034421,2.120211,1.036296,2.008040,7.081421,-0.596631,1.860926,5.199340,7.099183,-9.961174,-9.537081,-4.839671,-6.584256,6.166494,1.408395,0.299998,-1.096806,-1.330879,3.135950,3.396912,9.026171,-4.708204,-7.580204,-3.363951,-1.263416,-2.166145,-4.144558,-3.938718,7.242607,-1.771143,2.328404,-7.212740,-3.448464,2.036117,-3.044407,3.042938,-7.257000,-6.911442,7.520287,8.360655,3.872090,-3.087388,-5.295916,-3.201786,-0.479121,-7.679751,-2.473797,7.405275,9.548708,7.618169,9.125420,2.725959,-4.315699,-9.561550,0.884897,8.574558,6.706825,-0.280023,-5.377524,-8.318425,7.246058,-3.539856,3.857190,8.750246,-8.489163,-0.863475,1.601801,-8.532296,7.909312,0.765837,-7.743434,3.213772,-5.271472,4.335519,-3.501082,6.301430,-8.364423,7.071180,3.238518,-9.303123,2.766717,-1.015553,0.965205,-9.479566,2.314563,8.639493,-6.275926,-9.392675,-2.499534,5.890959,0.001041,0.745571,-4.551197,1.995931,0.779298,-9.272192,-9.107557,8.420741,0.459112,-8.734952,6.234172,-1.438752,-8.553643,-9.441929,-4.587356,7.035066,-8.032293,2.410415,7.881441,-9.477031,-2.540763,-2.895536,8.910009,-1.265722,4.672658,-7.881214,-2.539320,0.830755,0.056286,-9.390833,6.318396,1.691777,-4.827135,4.497248,9.932346,-2.497314,-2.824861,-5.845073], dtype = "float32")#candidate|4906|(3600,)|const|float32
var_4907 = relay.var("var_4907", dtype = "int8", shape = (450,))#candidate|4907|(450,)|var|int8
call_4904 = relay.TupleGetItem(func_1628_call(relay.reshape(const_4905.astype('float32'), [216,]), relay.reshape(const_4906.astype('float32'), [3600,]), relay.reshape(var_4907.astype('int8'), [450,]), ), 3)
call_4908 = relay.TupleGetItem(func_1633_call(relay.reshape(const_4905.astype('float32'), [216,]), relay.reshape(const_4906.astype('float32'), [3600,]), relay.reshape(var_4907.astype('int8'), [450,]), ), 3)
bop_4926 = relay.bitwise_and(var_4899.astype('uint64'), bop_4901.astype('uint64')) # shape=(8, 2, 13)
output = relay.Tuple([call_4904,const_4905,const_4906,var_4907,bop_4926,])
output2 = relay.Tuple([call_4908,const_4905,const_4906,var_4907,bop_4926,])
func_4929 = relay.Function([var_4899,var_4900,var_4907,], output)
mod['func_4929'] = func_4929
mod = relay.transform.InferType()(mod)
mutated_mod['func_4929'] = func_4929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4929_call = mutated_mod.get_global_var('func_4929')
var_4931 = relay.var("var_4931", dtype = "float64", shape = (8, 1, 13))#candidate|4931|(8, 1, 13)|var|float64
var_4932 = relay.var("var_4932", dtype = "float64", shape = (8, 2, 13))#candidate|4932|(8, 2, 13)|var|float64
var_4933 = relay.var("var_4933", dtype = "int8", shape = (450,))#candidate|4933|(450,)|var|int8
call_4930 = func_4929_call(var_4931,var_4932,var_4933,)
output = call_4930
func_4934 = relay.Function([var_4931,var_4932,var_4933,], output)
mutated_mod['func_4934'] = func_4934
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4363_call = mod.get_global_var('func_4363')
func_4365_call = mutated_mod.get_global_var('func_4365')
call_4967 = func_4363_call()
call_4968 = func_4363_call()
output = relay.Tuple([call_4967,])
output2 = relay.Tuple([call_4968,])
func_4970 = relay.Function([], output)
mod['func_4970'] = func_4970
mod = relay.transform.InferType()(mod)
output = func_4970()
func_4971 = relay.Function([], output)
mutated_mod['func_4971'] = func_4971
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4363_call = mod.get_global_var('func_4363')
func_4365_call = mutated_mod.get_global_var('func_4365')
call_4995 = func_4363_call()
call_4996 = func_4363_call()
output = call_4995
output2 = call_4996
func_5031 = relay.Function([], output)
mod['func_5031'] = func_5031
mod = relay.transform.InferType()(mod)
output = func_5031()
func_5032 = relay.Function([], output)
mutated_mod['func_5032'] = func_5032
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5059 = relay.var("var_5059", dtype = "int64", shape = (16, 5, 5))#candidate|5059|(16, 5, 5)|var|int64
var_5060 = relay.var("var_5060", dtype = "int64", shape = (16, 5, 5))#candidate|5060|(16, 5, 5)|var|int64
bop_5061 = relay.minimum(var_5059.astype('int64'), relay.reshape(var_5060.astype('int64'), relay.shape_of(var_5059))) # shape=(16, 5, 5)
output = relay.Tuple([bop_5061,])
output2 = relay.Tuple([bop_5061,])
func_5073 = relay.Function([var_5059,var_5060,], output)
mod['func_5073'] = func_5073
mod = relay.transform.InferType()(mod)
var_5074 = relay.var("var_5074", dtype = "int64", shape = (16, 5, 5))#candidate|5074|(16, 5, 5)|var|int64
var_5075 = relay.var("var_5075", dtype = "int64", shape = (16, 5, 5))#candidate|5075|(16, 5, 5)|var|int64
output = func_5073(var_5074,var_5075,)
func_5076 = relay.Function([var_5074,var_5075,], output)
mutated_mod['func_5076'] = func_5076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2563_call = mod.get_global_var('func_2563')
func_2564_call = mutated_mod.get_global_var('func_2564')
call_5086 = relay.TupleGetItem(func_2563_call(), 0)
call_5087 = relay.TupleGetItem(func_2564_call(), 0)
const_5089 = relay.const([[[-6.442581,5.509890,-3.057618,9.275927,0.982242,0.347560,6.954767,9.150540,3.326567,4.611167,5.512333,4.271826,-9.211687],[-2.128982,7.326277,-4.533429,-2.737708,-3.246771,-1.458621,-7.597285,-6.479076,2.491150,4.188487,-0.361693,-5.005402,8.653914],[-7.755443,2.237861,5.623824,-0.415962,3.992143,-5.013832,9.630462,-0.541226,-4.308685,4.300460,-3.969628,1.700676,9.765524],[-5.887742,1.350465,-5.330350,-0.794674,-2.041368,6.231034,-7.285877,6.885049,-5.318399,-5.304257,-8.224124,-2.292261,4.474079],[-3.704348,-2.195763,-9.637727,-9.066115,-1.608669,0.661698,-8.039081,-2.819050,2.833746,-3.797638,-1.394380,7.508749,5.939955],[6.839111,0.830477,9.074522,8.980165,-3.048017,-3.462364,8.936220,8.673288,-5.221419,-9.313191,6.007743,9.153910,-8.986930],[-6.209849,-9.825872,-4.009473,2.199173,-6.819098,5.081425,-5.326369,-2.717829,-1.571147,-5.882671,-3.249339,0.445164,3.929711]],[[-8.581797,-4.304838,-8.418501,-5.417076,4.605582,5.565467,7.565321,3.052159,6.659751,-0.599655,-8.443513,-6.818467,-2.844833],[2.924113,2.987530,-9.954186,-6.152158,9.025953,2.788639,2.926660,-1.827375,-1.573334,3.995651,-2.126833,9.196706,-9.122528],[-4.673489,-8.814231,5.474873,-6.284801,9.577907,0.584792,-3.101733,-4.415938,-4.287878,-8.946789,-0.915643,-6.644512,-0.633803],[8.661091,1.921998,0.699594,-9.265291,-6.039676,-8.936665,-4.946377,5.205204,8.213502,-9.855467,-7.675874,8.093058,2.115806],[9.527473,2.814705,7.330242,2.379638,-1.694516,-4.774423,2.732536,0.739580,1.041976,6.319302,6.968540,-8.220217,-9.016806],[-4.556644,2.545341,-8.681628,-6.937165,-7.215002,-4.776662,-7.578426,0.362430,0.340330,-4.776639,-8.403058,-3.205111,-7.734844],[-4.787836,-9.577209,2.282383,-9.711501,-8.477778,9.245578,5.528638,-9.540445,-6.784981,-8.926283,1.666210,-6.289854,-2.210765]]], dtype = "float32")#candidate|5089|(2, 7, 13)|const|float32
bop_5090 = relay.greater(call_5086.astype('bool'), const_5089.astype('bool')) # shape=(2, 7, 13)
bop_5093 = relay.greater(call_5087.astype('bool'), const_5089.astype('bool')) # shape=(2, 7, 13)
func_5031_call = mod.get_global_var('func_5031')
func_5032_call = mutated_mod.get_global_var('func_5032')
call_5120 = func_5031_call()
call_5121 = func_5031_call()
func_1691_call = mod.get_global_var('func_1691')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_5137 = relay.TupleGetItem(func_1691_call(), 1)
call_5138 = relay.TupleGetItem(func_1693_call(), 1)
const_5141 = relay.const([[[True,False,True,False,True,False,True,True,True,True,False,False,False],[False,True,False,True,True,True,True,True,True,True,False,False,True],[False,True,True,True,False,False,True,True,True,True,True,False,False],[True,False,False,True,False,True,True,False,False,False,True,True,True],[False,False,True,False,True,False,False,False,True,False,True,False,True],[False,True,True,False,False,False,False,False,True,False,True,False,True],[False,False,False,True,False,True,False,True,True,True,True,True,False]],[[False,True,True,True,True,True,False,False,True,False,False,False,True],[True,False,False,False,True,False,False,False,False,False,True,False,False],[False,True,True,False,True,False,True,False,True,False,True,True,False],[True,False,False,True,True,False,True,True,False,True,False,False,True],[False,True,False,False,True,False,True,False,False,True,False,False,True],[True,False,True,True,True,False,True,True,True,False,True,False,True],[True,True,True,False,False,True,True,False,True,False,True,True,False]]], dtype = "bool")#candidate|5141|(2, 7, 13)|const|bool
bop_5142 = relay.left_shift(bop_5090.astype('int16'), relay.reshape(const_5141.astype('int16'), relay.shape_of(bop_5090))) # shape=(2, 7, 13)
bop_5145 = relay.left_shift(bop_5093.astype('int16'), relay.reshape(const_5141.astype('int16'), relay.shape_of(bop_5093))) # shape=(2, 7, 13)
output = relay.Tuple([call_5120,call_5137,bop_5142,])
output2 = relay.Tuple([call_5121,call_5138,bop_5145,])
func_5148 = relay.Function([], output)
mod['func_5148'] = func_5148
mod = relay.transform.InferType()(mod)
mutated_mod['func_5148'] = func_5148
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5148_call = mutated_mod.get_global_var('func_5148')
call_5149 = func_5148_call()
output = call_5149
func_5150 = relay.Function([], output)
mutated_mod['func_5150'] = func_5150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3643_call = mod.get_global_var('func_3643')
func_3645_call = mutated_mod.get_global_var('func_3645')
call_5164 = relay.TupleGetItem(func_3643_call(), 0)
call_5165 = relay.TupleGetItem(func_3645_call(), 0)
func_1119_call = mod.get_global_var('func_1119')
func_1120_call = mutated_mod.get_global_var('func_1120')
call_5166 = relay.TupleGetItem(func_1119_call(), 0)
call_5167 = relay.TupleGetItem(func_1120_call(), 0)
output = relay.Tuple([call_5164,call_5166,])
output2 = relay.Tuple([call_5165,call_5167,])
func_5176 = relay.Function([], output)
mod['func_5176'] = func_5176
mod = relay.transform.InferType()(mod)
mutated_mod['func_5176'] = func_5176
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5176_call = mutated_mod.get_global_var('func_5176')
call_5177 = func_5176_call()
output = call_5177
func_5178 = relay.Function([], output)
mutated_mod['func_5178'] = func_5178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_675_call = mod.get_global_var('func_675')
func_677_call = mutated_mod.get_global_var('func_677')
call_5185 = func_675_call()
call_5186 = func_675_call()
func_3781_call = mod.get_global_var('func_3781')
func_3782_call = mutated_mod.get_global_var('func_3782')
call_5192 = func_3781_call()
call_5193 = func_3781_call()
func_2854_call = mod.get_global_var('func_2854')
func_2857_call = mutated_mod.get_global_var('func_2857')
var_5196 = relay.var("var_5196", dtype = "int8", shape = (450,))#candidate|5196|(450,)|var|int8
call_5195 = relay.TupleGetItem(func_2854_call(relay.reshape(var_5196.astype('int8'), [5, 10, 9])), 2)
call_5197 = relay.TupleGetItem(func_2857_call(relay.reshape(var_5196.astype('int8'), [5, 10, 9])), 2)
func_1691_call = mod.get_global_var('func_1691')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_5216 = relay.TupleGetItem(func_1691_call(), 1)
call_5217 = relay.TupleGetItem(func_1693_call(), 1)
output = relay.Tuple([call_5185,call_5192,call_5195,var_5196,call_5216,])
output2 = relay.Tuple([call_5186,call_5193,call_5197,var_5196,call_5217,])
func_5236 = relay.Function([var_5196,], output)
mod['func_5236'] = func_5236
mod = relay.transform.InferType()(mod)
mutated_mod['func_5236'] = func_5236
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5237 = relay.var("var_5237", dtype = "int8", shape = (450,))#candidate|5237|(450,)|var|int8
func_5236_call = mutated_mod.get_global_var('func_5236')
call_5238 = func_5236_call(var_5237)
output = call_5238
func_5239 = relay.Function([var_5237], output)
mutated_mod['func_5239'] = func_5239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1324_call = mod.get_global_var('func_1324')
func_1325_call = mutated_mod.get_global_var('func_1325')
call_5247 = relay.TupleGetItem(func_1324_call(), 0)
call_5248 = relay.TupleGetItem(func_1325_call(), 0)
func_2759_call = mod.get_global_var('func_2759')
func_2761_call = mutated_mod.get_global_var('func_2761')
call_5256 = func_2759_call()
call_5257 = func_2759_call()
func_3702_call = mod.get_global_var('func_3702')
func_3706_call = mutated_mod.get_global_var('func_3706')
const_5260 = relay.const([[-5,-5,4,7,3,-6,-7,6,1,-1,-2,9,9,-9,-1,-6,-3,5,-9,1,-4,-9,-9,5,2,4,-4,-2,-3,7,-1,2,4,-1,10,8,-10,-9,1,1,-9,-9,-10,-9,1,6,-8,8,-6,6,-5,-3,1,-4,-5,10,-1,-8,-2,-3,2,-7,-10,10,-7,1,1,7,-6,-6,7,5,-5,-9,10,1,3,-10,-4,6,-9,3,3,-5,2,-9,7,5,7,-10,5,-10,-1,1,3,9,8,-5,4,1],[-1,-5,4,-2,-3,1,6,-8,2,-4,-7,-8,-9,-6,-2,8,-7,4,2,-6,8,7,-7,-3,-2,-5,-4,-4,7,-5,-8,4,6,9,-4,7,2,-8,-6,-1,9,-9,-10,-3,4,-8,1,-10,-10,6,-5,5,-6,-10,3,-3,7,5,-7,-4,6,-7,-2,5,7,-5,6,-2,3,7,3,-10,3,8,4,5,2,9,9,7,5,8,3,4,-2,-2,2,-5,-7,-9,3,-3,7,8,-5,-2,8,-2,10,5],[-8,6,2,6,-4,-2,-10,1,-6,3,-5,-2,7,-4,-9,-8,9,-8,7,10,-1,-8,7,10,10,7,-10,-10,2,-3,-4,-9,-7,2,2,-5,4,8,3,-5,3,10,-2,2,6,-6,-8,-1,-3,-1,5,-10,9,10,-7,-7,-8,4,1,3,-3,6,-3,8,-2,-3,-5,7,2,-6,-4,-9,-1,-2,1,10,6,7,4,7,4,-4,4,3,-9,-7,1,7,1,6,7,-5,-1,4,8,1,3,1,7,5],[2,-8,8,-6,-5,10,-8,6,-5,-3,2,-5,9,2,1,-1,9,-7,-7,5,-7,5,-10,-3,1,-10,-1,-8,2,-6,7,-5,1,3,-6,9,3,-9,4,8,9,10,2,10,-8,-6,-8,-1,-4,4,-1,1,6,7,-1,7,2,2,3,-9,-10,8,-7,-4,1,8,10,8,-1,-8,-1,-4,10,8,-8,8,3,8,3,10,2,8,1,-10,2,-7,-2,-5,-7,-10,9,6,4,-1,-6,2,2,9,-5,-8],[-10,-9,5,7,-4,-8,-6,4,-8,6,-7,1,-8,5,-1,2,7,4,-3,6,1,-2,-10,-7,-1,-10,1,10,-4,-3,-7,6,6,5,-4,-9,-5,-10,-7,-1,9,-7,-5,-10,-1,3,9,9,1,7,5,8,8,4,6,4,-9,6,9,2,-2,-5,6,8,-9,3,-2,-3,9,-8,3,10,4,-5,-5,-2,-3,8,2,-7,1,-3,8,-5,-3,4,4,7,2,-10,10,2,8,3,7,1,9,-1,1,-6],[9,-10,5,-3,-9,2,7,-3,5,7,7,10,-3,4,8,-8,-1,-2,-4,-3,-9,2,-8,-1,4,-5,-7,8,-5,-3,6,2,8,6,-8,-6,-2,3,5,5,3,10,-6,-9,5,-5,-1,-8,10,4,-1,-5,7,4,-1,1,10,3,4,-8,3,-7,10,-7,7,8,-10,-2,-10,-10,9,6,-5,-7,10,7,9,-10,-9,-9,6,6,-2,-4,-9,5,6,-9,-10,-1,2,-6,1,-9,-2,-9,-8,6,-5,4]], dtype = "uint32")#candidate|5260|(6, 100)|const|uint32
const_5261 = relay.const([-2,-1,-1,7,-1,-9,1,-4,-2,-9,-5,-6,-8,-9,7,-2,-2,-1,-3,-6,-9,-5,7,-1,4,-8,6,1,-6,-6,4,-3,-2,1,5,4,-2,-6,-6,6,6,10,1,-8,4,2,-2,4,1,1,-3,-2,2,2,5,-8,5,3,-1,-2,4,1,-1,2,-2,-10,8,8,7,7,-1,3,5,1,-6,1,1,10,8,-5,-4,5,-4,3,-6,-5,7,4,-3,-10,-10,-3,-4,2,-4,4,2,2,-4,-9,-7,-9,4,8,8,10,-10,8,5,-8,9,-7,-3,6,5,-10,-2,9,-2,-5,7,-8,-8,3,-6,-2,-4,5,1,-7,-9,-1,7,8,6,-10,1,-10,-4,-2,-5,-7,-5,-8,-6,-3,5,-7,-3,-2,2,-2,1,2,6,-8,-10,1,7,-2,-8,9,10,-6,3,-3,-1,6,8,7,-3,6,10,-9,-1,-2,-7,-2,9,1,5,6,9,-10,-1,-3,-2,6,-10,-2,5,10,7,10,-10,-7,-4,-5,-5,4,-1,-10,7,8,-10,-8,4,-8,10,8,-8,-6,-8,-7,-5,-8,-7,-1,4,-2,10,1,6,7,-7,7,-8,8,-6,-8,6,-9,-6,-7,-10,7,7,-3,7,-2,-3,-10,3,-6,4,2,-1,5,1,-10,-3,8,4,4,1,8,6,-6,7,-10,7,-3,4,8,9,6,-4,1,-8,-3,-4,3,-10,-9,-1,8,-4,8,8,-3,5,-9,4,9,9,-10,-3,-3,4,-10,4,4,-8,3,-10,2,-6,6,-5,1,-7,6,-6,4,2,4,1,-3,-2,-6,-5,-10,1,10,-1,9,5,-1,-8,-2,9,8,4,1,-10,-10,5,-7,-6,-2,1,6,-1,-7,-1,1,5,-2,-3,-6,-9,-9,6,3,-2,-10,10,-8,-2,2,-4,-5,-2,-7,-7,-9,1,5,3,-1,6,-7,9,7,-10,7,2,2,-7,1,6,-4,-8,-6,8,-6,-1,1,10,-1,9,-6,-10,-6,-9,-2,-9,-2,7,5,-5,10,-6,6,-8,-8,-5,-7,5,3,-2,-1,-3,-7,-2,6,3,-5,-4,7,-6,-9,1,7,9,4,-6,2,9,-2,2,-10,3,-8,-4,10,-9,-4,-3,8,2,-5,8,-10,9,-10,9,9,-3,10,9,-1,9,1,-4,-5,-3,-5,-2,-8], dtype = "int8")#candidate|5261|(450,)|const|int8
call_5259 = relay.TupleGetItem(func_3702_call(relay.reshape(const_5260.astype('uint32'), [600,]), relay.reshape(const_5261.astype('int8'), [150, 3]), ), 5)
call_5262 = relay.TupleGetItem(func_3706_call(relay.reshape(const_5260.astype('uint32'), [600,]), relay.reshape(const_5261.astype('int8'), [150, 3]), ), 5)
func_3702_call = mod.get_global_var('func_3702')
func_3706_call = mutated_mod.get_global_var('func_3706')
call_5273 = relay.TupleGetItem(func_3702_call(relay.reshape(const_5260.astype('uint32'), [600,]), relay.reshape(const_5261.astype('int8'), [150, 3]), ), 0)
call_5274 = relay.TupleGetItem(func_3706_call(relay.reshape(const_5260.astype('uint32'), [600,]), relay.reshape(const_5261.astype('int8'), [150, 3]), ), 0)
func_1384_call = mod.get_global_var('func_1384')
func_1386_call = mutated_mod.get_global_var('func_1386')
call_5278 = relay.TupleGetItem(func_1384_call(), 0)
call_5279 = relay.TupleGetItem(func_1386_call(), 0)
func_1753_call = mod.get_global_var('func_1753')
func_1754_call = mutated_mod.get_global_var('func_1754')
call_5286 = relay.TupleGetItem(func_1753_call(), 0)
call_5287 = relay.TupleGetItem(func_1754_call(), 0)
output = relay.Tuple([call_5247,call_5256,call_5259,const_5260,const_5261,call_5273,call_5278,call_5286,])
output2 = relay.Tuple([call_5248,call_5257,call_5262,const_5260,const_5261,call_5274,call_5279,call_5287,])
func_5308 = relay.Function([], output)
mod['func_5308'] = func_5308
mod = relay.transform.InferType()(mod)
mutated_mod['func_5308'] = func_5308
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5308_call = mutated_mod.get_global_var('func_5308')
call_5309 = func_5308_call()
output = call_5309
func_5310 = relay.Function([], output)
mutated_mod['func_5310'] = func_5310
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5355 = relay.var("var_5355", dtype = "float32", shape = (14, 16, 6))#candidate|5355|(14, 16, 6)|var|float32
uop_5356 = relay.exp(var_5355.astype('float32')) # shape=(14, 16, 6)
output = relay.Tuple([uop_5356,])
output2 = relay.Tuple([uop_5356,])
func_5376 = relay.Function([var_5355,], output)
mod['func_5376'] = func_5376
mod = relay.transform.InferType()(mod)
var_5377 = relay.var("var_5377", dtype = "float32", shape = (14, 16, 6))#candidate|5377|(14, 16, 6)|var|float32
output = func_5376(var_5377)
func_5378 = relay.Function([var_5377], output)
mutated_mod['func_5378'] = func_5378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1899_call = mod.get_global_var('func_1899')
func_1901_call = mutated_mod.get_global_var('func_1901')
call_5397 = relay.TupleGetItem(func_1899_call(), 1)
call_5398 = relay.TupleGetItem(func_1901_call(), 1)
output = call_5397
output2 = call_5398
func_5421 = relay.Function([], output)
mod['func_5421'] = func_5421
mod = relay.transform.InferType()(mod)
output = func_5421()
func_5422 = relay.Function([], output)
mutated_mod['func_5422'] = func_5422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4096_call = mod.get_global_var('func_4096')
func_4097_call = mutated_mod.get_global_var('func_4097')
call_5464 = relay.TupleGetItem(func_4096_call(), 0)
call_5465 = relay.TupleGetItem(func_4097_call(), 0)
const_5472 = relay.const([[[-3.338106,3.442032,-6.513440,-9.802898,8.272124,-3.954039,-3.621631,-0.065039,1.025262],[-1.000063,-3.011782,-8.763243,-2.745143,5.857017,-2.854761,-0.260535,3.706544,-3.814859],[-3.250403,-1.081170,7.003179,-8.359805,7.102433,5.464496,8.695407,5.495640,9.119234],[8.169995,-6.020289,3.521130,2.728338,9.746161,4.714695,-7.374481,3.602494,2.639855],[3.795392,-9.484941,1.959666,1.681924,-3.183824,-4.322354,-9.549911,7.690281,3.839985],[-4.630381,6.358979,3.733870,4.346379,-2.903914,-8.026319,8.503446,-7.689153,-3.761421],[-3.587432,-4.605223,-0.617014,-5.633284,9.398126,5.611072,4.085559,2.202516,8.656715]],[[2.271367,5.751976,4.442545,-0.824589,7.034458,3.496317,-8.419792,-4.433316,-5.739367],[2.628331,2.838006,-2.341882,1.336638,-1.440656,-1.788589,0.933647,6.106323,-4.835994],[-5.671257,0.486058,5.628992,9.872284,-3.122886,-7.959711,-7.349394,-9.267665,-5.726682],[-7.323183,-1.497466,5.910096,5.789836,-2.591543,2.094561,4.005610,7.507879,2.386253],[9.463796,-6.535184,-5.073562,-9.371006,5.322002,8.097970,-6.686052,8.368367,-7.606837],[0.286002,-5.308079,-6.542007,-4.603481,6.618556,6.848285,-2.550954,-7.455719,-1.350013],[-5.388081,0.307143,2.030761,1.602011,5.378561,-9.235924,5.960631,5.402317,-4.308467]]], dtype = "float32")#candidate|5472|(2, 7, 9)|const|float32
bop_5473 = relay.right_shift(call_5464.astype('int64'), const_5472.astype('int64')) # shape=(2, 7, 9)
bop_5476 = relay.right_shift(call_5465.astype('int64'), const_5472.astype('int64')) # shape=(2, 7, 9)
func_4096_call = mod.get_global_var('func_4096')
func_4097_call = mutated_mod.get_global_var('func_4097')
call_5485 = relay.TupleGetItem(func_4096_call(), 0)
call_5486 = relay.TupleGetItem(func_4097_call(), 0)
func_5073_call = mod.get_global_var('func_5073')
func_5076_call = mutated_mod.get_global_var('func_5076')
var_5491 = relay.var("var_5491", dtype = "int64", shape = (400,))#candidate|5491|(400,)|var|int64
call_5490 = relay.TupleGetItem(func_5073_call(relay.reshape(var_5491.astype('int64'), [16, 5, 5]), relay.reshape(var_5491.astype('int64'), [16, 5, 5]), ), 0)
call_5492 = relay.TupleGetItem(func_5076_call(relay.reshape(var_5491.astype('int64'), [16, 5, 5]), relay.reshape(var_5491.astype('int64'), [16, 5, 5]), ), 0)
func_3092_call = mod.get_global_var('func_3092')
func_3094_call = mutated_mod.get_global_var('func_3094')
call_5501 = func_3092_call()
call_5502 = func_3092_call()
func_1887_call = mod.get_global_var('func_1887')
func_1889_call = mutated_mod.get_global_var('func_1889')
call_5510 = relay.TupleGetItem(func_1887_call(), 1)
call_5511 = relay.TupleGetItem(func_1889_call(), 1)
func_5376_call = mod.get_global_var('func_5376')
func_5378_call = mutated_mod.get_global_var('func_5378')
const_5552 = relay.const([-5.469001,-2.046313,7.011493,8.911190,-4.077829,0.983629,-1.148567,1.043535,2.494177,5.213555,-6.914259,-1.472488,9.749917,2.186387,0.356077,-2.759323,-4.847161,-4.885076,-4.009506,-7.000581,-2.478582,-1.191857,-3.317583,-1.295469,-6.657242,5.628212,-8.898341,8.076509,0.840961,-4.995122,0.962657,-9.003213,-8.296047,-4.759997,-6.781478,1.644796,-5.132966,4.104064,8.757679,-8.372440,8.088312,-6.304857,4.646210,2.088097,-0.608370,7.815092,5.767054,7.251248,0.399875,-7.351758,-0.164320,-8.545579,5.887705,5.563361,-6.015717,6.292540,6.697305,3.846304,9.095800,1.816918,-5.819444,4.012585,6.488025,1.596504,-5.507761,-6.296373,6.674213,4.589013,2.980292,1.967021,5.729946,1.843453,-2.001813,0.656224,-1.264129,6.066866,-6.815817,-6.297194,6.838581,-8.617360,8.957746,-0.524428,1.220871,8.991391,-3.654606,-0.026075,1.376872,-0.865780,-7.703307,0.002719,6.728619,-3.873989,-1.288568,0.854316,-7.755913,2.405978,-6.836925,2.766255,-1.853188,-1.656856,4.163076,-7.528595,7.604512,9.499393,-0.731956,-8.743488,2.708521,8.402597,0.672417,-3.399515,-5.725801,0.074310,6.977272,3.614315,5.782647,6.854134,-0.311481,-9.533728,-8.504840,-5.295467,-3.185064,-6.098188,2.552934,7.602536,-5.103857,-0.190552,-3.763617,-0.020072,-3.219333,2.306149,5.965641,1.980372,-7.271854,8.308412,6.071928,0.899653,-5.361269,9.985228,-8.464797,-1.751515,-4.114185,5.546499,-4.617223,0.556796,3.016770,9.230411,8.559670,4.912007,-8.909688,-5.638579,-7.585037,8.733068,-0.930734,-3.899040,-8.380292,1.589868,5.191996,7.975141,-4.901463,4.936557,1.274581,1.165226,8.039700,-2.403638,8.980363,1.202517,-9.106310,1.379827,5.894709,5.266329,-9.026913,5.679163,-4.810841,-5.166300,1.770900,-0.001377,-4.825250,4.917142,-7.605520,7.629991,-6.142061,0.334821,3.298611,6.184029,-4.835673,-6.757711,-0.263373,4.570569,-5.861969,7.670197,2.928566,-7.544933,6.767525,4.229553,6.016447,-8.975046,8.527415,9.133172,-9.659385,3.498369,1.020000,2.789821,7.846240,-1.115766,-3.502846,6.894733,-8.225576,4.429474,6.924595,9.595690,8.875425,3.198087,-9.250616,-1.424182,2.080838,4.896837,9.841552,-8.305514,2.953543,2.504779,1.205987,3.903739,-8.220782,5.369490,9.538919,7.812071,-8.091177,7.248035,0.376680,6.114951,-9.163757,4.346490,-0.231273,-9.934206,1.591706,9.104663,9.618021,-8.918885,-3.856814,7.530193,-4.252735,-1.874966,8.341818,1.872740,8.368398,-1.554129,-0.836027,-8.678378,1.189238,-3.788171,-3.030413,3.444965,1.912726,6.502714,-7.355743,0.921194,1.839632,7.383767,-4.281693,1.758142,-8.706130,7.987977,-4.179867,3.537640,-8.201957,-8.284964,7.663318,-7.467607,7.498218,-8.076389,6.438384,-9.657021,-7.992540,7.567277,0.583597,-7.997168,-1.855585,-9.005809,3.063503,5.818796,2.752629,-3.353761,3.161094,5.383725,7.435553,-3.465826,-6.761731,6.222983,8.808242,6.631811,-6.785655,-5.557104,2.728177,2.285701,-5.583937,-4.231828,-2.420184,-5.432553,-1.881215,-1.847612,-6.821480,-1.091464,0.748705,3.084314,-6.648553,4.030881,-5.558823,-0.993512,-4.956012,0.416675,-1.477431,1.510433,-2.489174,-9.345712,3.551647,-2.579304,-2.384411,-9.832252,9.913047,-8.897688,-3.125806,-4.338981,2.276489,-2.762087,-9.084687,-5.571692,-5.880825,6.336255,7.972946,2.740677,-4.438644,-4.630006,-5.642389,-8.919344,-4.825115,9.219245,4.173809,-1.331214,-1.268305,-3.954380,-4.892161,6.815847,-6.131716,3.351413,0.885386,5.995285,5.271885,-6.053596,-3.084106,3.340904,8.858180,-6.319425,-1.432914,9.233941,2.995458,1.142553,-2.873446,-9.380169,5.537233,-9.975622,-6.118120,-9.761728,-2.062978,8.383973,3.295071,4.533909,-9.296846,6.979921,-7.543527,1.454764,2.870151,7.462186,-0.605279,-8.189324,-0.327623,-4.122621,-2.548648,-3.593375,4.005007,-0.033505,-0.660045,1.362741,1.743012,2.091186,6.088004,7.991862,9.920598,-7.514776,5.604899,5.604213,3.945071,-5.569606,-0.233499,-9.025251,0.156757,-5.571048,0.688257,-2.955380,0.201200,-5.686581,-8.392898,4.844307,3.633463,1.572125,-0.394345,-4.649910,-3.012184,-0.149262,3.164298,-9.525015,9.220586,-3.331364,-7.233434,7.209452,-1.930778,-6.973067,9.769487,-4.675079,6.759471,7.815715,-4.418073,-6.180295,3.863755,3.649810,3.648873,0.183254,-2.422700,7.768599,-8.657535,-6.864149,9.704309,3.358984,-0.103456,7.612475,-5.893521,-2.410414,-6.669410,1.864026,0.841341,-2.601448,2.043381,7.153792,3.910737,-2.526825,4.043777,-6.684097,-5.113476,4.417355,2.929707,-3.131206,-2.940499,-8.400314,8.791833,-4.578377,-6.317721,-8.740706,-6.024478,4.019585,-7.432011,2.699387,3.274909,-9.938382,1.919917,-3.388057,-8.559505,-5.369712,6.933869,4.204403,5.134760,9.652109,-9.195665,8.625958,7.375223,-0.018651,-0.974856,0.424199,0.506745,3.083433,-8.165384,2.566789,4.427350,7.114932,-4.511048,6.247030,-7.552881,2.124590,-8.128794,9.991721,-9.486038,-6.212655,8.290697,-3.857873,0.902121,3.229730,2.282944,8.893950,1.557413,-1.147280,3.645067,2.644155,-5.487645,7.789271,4.647357,6.014143,-8.221924,-5.955348,4.330745,9.555362,4.750053,-1.251592,5.978624,2.508412,-6.347410,2.309453,8.799057,6.455322,4.943707,1.593851,7.901969,-9.361576,-5.307105,2.396287,3.438760,-9.837053,-1.339252,-3.048721,-6.913753,-5.915488,7.801679,2.532367,-9.982985,-2.343719,4.346355,-8.268598,-0.320190,-9.460993,4.401787,3.804637,-9.896657,9.452758,-4.775966,9.407854,5.195980,-2.825298,6.790527,-5.861969,-5.156366,6.262261,-4.110180,6.335751,8.468924,4.975855,0.505892,4.764911,-5.072976,-2.041813,-2.491373,-6.194186,6.230719,-8.540849,-9.663967,-5.389526,-9.804993,-4.612933,3.881148,1.429935,7.779426,-2.163207,9.307874,8.750561,-9.547448,5.204273,7.929333,4.946366,-7.517427,9.135036,-9.594067,0.922724,8.295794,6.364449,2.068205,6.502011,8.353932,-7.510446,-2.713809,-7.448826,4.111083,0.558698,6.263413,-8.025565,4.811245,-4.859141,4.671237,-9.446472,7.564799,-4.807815,-7.569516,-5.986680,5.898673,6.950843,-2.436822,-5.726758,7.965944,-2.515333,-8.821963,-5.943863,-3.310070,1.740125,-0.164954,-8.177298,9.898472,5.459971,7.877424,4.875459,-5.209101,-9.217689,6.116772,-7.700374,-3.345807,2.779069,0.719444,-8.130001,5.415277,-9.772332,8.104889,9.389025,8.334583,9.050886,-8.326193,5.806184,5.455926,7.334632,-7.192954,4.080686,-6.447195,-6.086859,-1.338686,0.971147,-5.165008,1.315571,5.567456,7.066629,5.152766,4.052171,6.454642,-1.921388,-4.693699,4.409339,-8.361756,9.958392,-0.434262,-2.682369,2.149138,-3.674866,8.776186,4.839487,-7.764740,9.440452,3.674374,-1.112914,6.430117,7.876850,-7.783521,4.597627,5.164610,-1.898754,-7.827191,-3.105102,-8.654544,1.078360,8.549638,-6.897707,7.262752,1.232023,-0.724636,-7.470390,5.389723,0.157952,-0.182988,-4.570214,-2.419422,7.633165,7.093989,-6.361582,-7.241363,-8.627417,-8.992093,-8.432335,-3.744010,3.673999,6.041026,8.861409,9.034802,-8.824975,6.705370,-5.804911,3.572359,-8.334502,8.832680,7.773119,-1.606169,3.208249,-1.483280,3.935315,-3.961241,-8.582197,-5.143394,-4.179358,-8.613765,7.039555,4.725935,8.882866,-3.523202,5.282164,-9.555702,6.561814,-9.349785,-1.899615,-1.470248,-9.799993,-7.916673,-0.182545,-3.468801,-9.706780,-1.003201,-6.954557,2.866366,-8.086669,4.701107,-5.322034,-0.171534,-7.096853,-0.756393,-9.649771,-1.417287,7.400104,2.717895,2.794583,-2.139690,-0.403691,-3.818409,-6.010523,3.456960,2.241975,5.500504,-5.213783,2.200214,-4.703971,6.910376,9.158882,9.918184,-7.578800,-1.712790,-2.258927,-1.845991,4.497341,8.341268,-7.053169,2.509201,7.731534,1.670896,-5.740988,7.752618,2.945433,3.943414,-9.210520,8.810677,7.728396,2.433571,8.966009,5.031002,-9.933429,-8.595926,4.257469,-0.111492,-9.313309,-1.071057,-6.710360,-1.767857,4.833775,-9.795122,-2.537011,-9.577578,-0.816790,-8.415958,6.837255,-7.271614,-6.380213,1.621603,-4.566728,0.368441,4.776854,-4.314630,3.256669,6.726221,-9.963379,-1.046542,-4.839027,7.592722,-0.418915,-6.529708,8.076579,5.227810,9.257484,2.304404,-0.930410,0.799617,-5.420138,-8.300206,-0.687948,-9.920679,2.474760,5.450382,-9.634629,-0.809122,-3.017695,-4.243771,-1.339647,-0.742507,-9.754940,2.139129,-4.946511,1.844843,-1.206768,-4.860468,7.976698,-0.288943,4.529810,-4.765608,-8.723033,5.302998,7.958126,-1.025682,0.239644,-4.513834,-5.874875,0.555193,-9.007441,7.304615,-3.043706,9.909719,5.874122,-9.991410,4.529130,-5.301030,-1.698576,4.633407,7.286705,6.961421,-9.885010,5.220171,8.931395,1.464477,2.430096,8.570068,-5.475597,1.657942,-5.611727,-7.980668,9.552106,1.281139,-7.998776,9.727091,-7.668795,7.263523,-7.000312,9.516588,9.736929,1.901542,5.527150,-7.969311,0.934562,8.510412,8.068691,-3.468469,-3.059448,-0.722701,-7.683874,4.326127,-1.832789,1.221962,3.361338,5.095647,4.580328,1.080973,5.473647,-1.005927,1.552854,-3.835877,6.166002,5.171241,-6.386248,6.483097,-0.101074,8.369090,6.871128,8.285470,4.164444,5.148994,-8.801847,1.575673,-6.506193,-6.914635,-6.647479,-0.659002,0.657116,2.598856,-2.456543,-9.151118,4.074426,1.796694,-8.886158,4.555809,6.051008,-6.722572,5.081399,3.267683,1.054656,-3.045333,-2.042834,-0.917981,-0.578790,4.925084,-4.749578,5.478502,6.992883,-9.691684,-3.271779,1.510414,-8.523431,4.801413,-8.935580,5.434016,-6.815251,6.635976,-3.477804,4.206521,6.018517,1.196212,-1.470485,-2.045232,-3.856908,-3.929465,-7.939022,-2.009002,2.539877,9.121549,2.731084,-4.037588,-6.039023,-5.874659,6.048738,2.266289,2.288108,-2.730572,-2.055581,7.577451,8.465091,7.539169,-0.322928,-6.312483,1.690146,9.958954,-7.499064,-7.715351,3.422843,9.447842,-1.156962,8.415081,-7.318731,-7.567749,-7.700750,3.664862,0.704838,-4.708531,-4.308557,4.923393,-0.120737,-2.116478,-6.861424,9.289110,-9.684724,-3.773201,9.657356,-9.452037,3.236570,-8.946115,-8.041646,5.414142,-4.300534,1.399947,-7.627877,-0.156123,9.136597,2.571812,-3.107152,6.548337,-8.960870,2.779727,-0.292500,6.334003,-8.422745,0.049105,6.155954,-2.408901,-0.686396,-1.427885,7.075958,1.353272,-4.551021,-1.163178,8.859539,0.392364,-0.341023,-0.328106,-1.570102,-9.516505,6.593155,5.119648,1.452237,4.389218,-9.526982,-8.680143,-0.850074,-0.249464,1.688748,0.583024,5.094005,-5.415761,-1.238358,-1.252918,-1.721091,3.814321,-5.775915,-6.273096,7.786727,-5.990905,3.366035,0.624335,-7.237015,-4.990217,-4.803891,9.797966,-7.202590,9.731862,-5.640060,3.396283,7.391308,-9.971647,-9.495438,6.756460,-8.290507,3.101460,-4.350669,-3.148292,-6.775890,-2.040880,-5.439975,-7.649191,3.282484,5.516702,2.848020,-1.223522,-2.327119,8.230320,8.577664,-9.709042,-5.322160,-2.728595,-0.306159,0.855309,7.652684,1.484959,1.636180,0.703881,-1.044166,-0.264281,0.950350,-3.300057,-2.520728,-9.219924,-1.883647,8.905216,-6.443629,9.728769,-3.160332,-8.072138,1.652243,-6.988956,7.138155,1.120434,-1.418746,-7.241144,9.897614,8.548912,-2.653063,6.753872,-0.747668,6.125258,-0.652137,8.295742,5.087163,2.884970,-0.400786,-6.110537,7.261998,1.824014,7.022502,0.342046,-9.841787,-6.875209,5.878719,0.017505,0.483925,-9.383120,2.608172,-7.658235,1.836343,2.537400,7.925535,-2.148136,-0.342734,8.619373,4.944766,-5.036032,1.240803,-8.509468,-4.669519,4.447448,-6.035643,-2.112394,7.981841,-9.047686,-1.824406,-9.638681,7.669806,-6.142305,-3.858116,-9.243398,-9.973091,8.210604,8.148944,-7.781983,8.891126,4.227288,-5.738062,-5.438716,4.145592,-6.821081,-3.630317,0.210123,1.368995,1.546482,7.147956,8.081537,-2.167226,-7.773528,-0.888520,-1.531592,-7.804094,9.943495,9.445865,-9.497512,0.832841,-6.043308,-1.110423,9.042412,9.562490,7.092978,-2.337383,-2.113803,-8.026737,8.551216,-4.846454,-2.082770,4.896247,3.559620,5.794069,7.302218,-3.408229,4.021308,-0.857506,2.130379,3.001036,-3.354255,0.849715,9.697381,3.246960,4.761605,-3.729061,-0.676190,7.326506,-2.316939,-1.282540,4.116285,3.832148,4.308806,-3.000180,0.677643,2.417994,0.861626,-5.005927,-7.649613,2.830834,6.695924,-0.496706,-8.930865,2.094620,-3.572550,-3.715566,2.598378,-9.816256,2.604875,9.209762,6.257485,6.368252,4.847633,1.018813,3.934617,7.773739,-6.023578,5.890363,-8.753320,9.818397,-1.964314,-9.341921,7.926529,-9.686026,0.750735,5.604908,-3.390532,-7.327368,-7.119228,-6.220426,-8.771175,9.905209,6.104287,1.403715,7.479873,-9.537300,8.429844,2.652924,-5.093799,4.244831,5.054854,-0.201660,6.812428,-4.560438,-6.472555,-6.173199,-6.166251,3.726859,-1.061713,4.227337,6.567020,0.222388,3.752877,1.895573,-9.392162,8.525821,5.204643,0.134277,-1.283161,-0.365857,-4.005606,-3.113494,-8.813902,-0.109283,-1.660004,2.259545,-3.701737,-6.250092,6.881541,8.591411,5.173437,-0.662236,-1.831135,8.234594,1.091287,5.721518,-1.251992,-2.706867,0.746684,7.413677,8.607811,6.583559,1.243485,5.635099,2.017125,-5.798935,9.723514,3.098939,4.294608,6.648187,-7.524600,-4.879937,-3.359687,-3.415786,-8.736793,5.669355,-9.654361,8.181113,3.097650,-4.313433,6.201496,4.737142,2.511371,-0.105538,7.705828,3.540234,-5.032077,8.817532,7.499747,-3.443629,3.772945,0.583830,-3.101649,-1.634450,7.627201,-0.476931,0.263344,7.108303,-9.419687,9.267051,6.160511,1.090737,6.406826,-9.297726,-7.686357,-6.668573,2.063651,2.129994,-1.572469,4.493263,1.262637,-9.695699,4.746072,4.692837,7.389309,4.431626,-9.019535,-9.908179,3.153596,-6.856354], dtype = "float32")#candidate|5552|(1344,)|const|float32
call_5551 = relay.TupleGetItem(func_5376_call(relay.reshape(const_5552.astype('float32'), [14, 16, 6])), 0)
call_5553 = relay.TupleGetItem(func_5378_call(relay.reshape(const_5552.astype('float32'), [14, 16, 6])), 0)
func_5148_call = mod.get_global_var('func_5148')
func_5150_call = mutated_mod.get_global_var('func_5150')
call_5559 = relay.TupleGetItem(func_5148_call(), 2)
call_5560 = relay.TupleGetItem(func_5150_call(), 2)
bop_5569 = relay.greater(call_5485.astype('bool'), bop_5473.astype('bool')) # shape=(2, 7, 9)
bop_5572 = relay.greater(call_5486.astype('bool'), bop_5476.astype('bool')) # shape=(2, 7, 9)
bop_5575 = relay.logical_and(var_5491.astype('bool'), call_5510.astype('bool')) # shape=(2, 7, 400)
bop_5578 = relay.logical_and(var_5491.astype('bool'), call_5511.astype('bool')) # shape=(2, 7, 400)
bop_5580 = relay.equal(bop_5575.astype('bool'), var_5491.astype('bool')) # shape=(2, 7, 400)
bop_5583 = relay.equal(bop_5578.astype('bool'), var_5491.astype('bool')) # shape=(2, 7, 400)
func_1778_call = mod.get_global_var('func_1778')
func_1780_call = mutated_mod.get_global_var('func_1780')
call_5592 = relay.TupleGetItem(func_1778_call(), 0)
call_5593 = relay.TupleGetItem(func_1780_call(), 0)
func_1171_call = mod.get_global_var('func_1171')
func_1173_call = mutated_mod.get_global_var('func_1173')
call_5597 = relay.TupleGetItem(func_1171_call(), 0)
call_5598 = relay.TupleGetItem(func_1173_call(), 0)
output = relay.Tuple([call_5490,call_5501,call_5551,const_5552,call_5559,bop_5569,bop_5580,call_5592,call_5597,])
output2 = relay.Tuple([call_5492,call_5502,call_5553,const_5552,call_5560,bop_5572,bop_5583,call_5593,call_5598,])
func_5602 = relay.Function([var_5491,], output)
mod['func_5602'] = func_5602
mod = relay.transform.InferType()(mod)
mutated_mod['func_5602'] = func_5602
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5603 = relay.var("var_5603", dtype = "int64", shape = (400,))#candidate|5603|(400,)|var|int64
func_5602_call = mutated_mod.get_global_var('func_5602')
call_5604 = func_5602_call(var_5603)
output = call_5604
func_5605 = relay.Function([var_5603], output)
mutated_mod['func_5605'] = func_5605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1691_call = mod.get_global_var('func_1691')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_5634 = relay.TupleGetItem(func_1691_call(), 1)
call_5635 = relay.TupleGetItem(func_1693_call(), 1)
output = relay.Tuple([call_5634,])
output2 = relay.Tuple([call_5635,])
func_5636 = relay.Function([], output)
mod['func_5636'] = func_5636
mod = relay.transform.InferType()(mod)
output = func_5636()
func_5637 = relay.Function([], output)
mutated_mod['func_5637'] = func_5637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_675_call = mod.get_global_var('func_675')
func_677_call = mutated_mod.get_global_var('func_677')
call_5638 = func_675_call()
call_5639 = func_675_call()
output = relay.Tuple([call_5638,])
output2 = relay.Tuple([call_5639,])
func_5645 = relay.Function([], output)
mod['func_5645'] = func_5645
mod = relay.transform.InferType()(mod)
output = func_5645()
func_5646 = relay.Function([], output)
mutated_mod['func_5646'] = func_5646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1324_call = mod.get_global_var('func_1324')
func_1325_call = mutated_mod.get_global_var('func_1325')
call_5736 = relay.TupleGetItem(func_1324_call(), 0)
call_5737 = relay.TupleGetItem(func_1325_call(), 0)
output = call_5736
output2 = call_5737
func_5738 = relay.Function([], output)
mod['func_5738'] = func_5738
mod = relay.transform.InferType()(mod)
mutated_mod['func_5738'] = func_5738
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5738_call = mutated_mod.get_global_var('func_5738')
call_5739 = func_5738_call()
output = call_5739
func_5740 = relay.Function([], output)
mutated_mod['func_5740'] = func_5740
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3929_call = mod.get_global_var('func_3929')
func_3931_call = mutated_mod.get_global_var('func_3931')
call_5790 = relay.TupleGetItem(func_3929_call(), 0)
call_5791 = relay.TupleGetItem(func_3931_call(), 0)
var_5828 = relay.var("var_5828", dtype = "float32", shape = (2, 7, 1))#candidate|5828|(2, 7, 1)|var|float32
bop_5829 = relay.divide(call_5790.astype('float32'), relay.reshape(var_5828.astype('float32'), relay.shape_of(call_5790))) # shape=(2, 7, 1)
bop_5832 = relay.divide(call_5791.astype('float32'), relay.reshape(var_5828.astype('float32'), relay.shape_of(call_5791))) # shape=(2, 7, 1)
output = bop_5829
output2 = bop_5832
func_5849 = relay.Function([var_5828,], output)
mod['func_5849'] = func_5849
mod = relay.transform.InferType()(mod)
var_5850 = relay.var("var_5850", dtype = "float32", shape = (2, 7, 1))#candidate|5850|(2, 7, 1)|var|float32
output = func_5849(var_5850)
func_5851 = relay.Function([var_5850], output)
mutated_mod['func_5851'] = func_5851
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4663_call = mod.get_global_var('func_4663')
func_4664_call = mutated_mod.get_global_var('func_4664')
call_5880 = relay.TupleGetItem(func_4663_call(), 0)
call_5881 = relay.TupleGetItem(func_4664_call(), 0)
output = relay.Tuple([call_5880,])
output2 = relay.Tuple([call_5881,])
func_5885 = relay.Function([], output)
mod['func_5885'] = func_5885
mod = relay.transform.InferType()(mod)
mutated_mod['func_5885'] = func_5885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5885_call = mutated_mod.get_global_var('func_5885')
call_5886 = func_5885_call()
output = call_5886
func_5887 = relay.Function([], output)
mutated_mod['func_5887'] = func_5887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5738_call = mod.get_global_var('func_5738')
func_5740_call = mutated_mod.get_global_var('func_5740')
call_5894 = func_5738_call()
call_5895 = func_5738_call()
output = relay.Tuple([call_5894,])
output2 = relay.Tuple([call_5895,])
func_5903 = relay.Function([], output)
mod['func_5903'] = func_5903
mod = relay.transform.InferType()(mod)
mutated_mod['func_5903'] = func_5903
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5903_call = mutated_mod.get_global_var('func_5903')
call_5904 = func_5903_call()
output = call_5904
func_5905 = relay.Function([], output)
mutated_mod['func_5905'] = func_5905
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5953 = relay.var("var_5953", dtype = "float64", shape = (1, 13, 2))#candidate|5953|(1, 13, 2)|var|float64
uop_5954 = relay.erf(var_5953.astype('float64')) # shape=(1, 13, 2)
output = relay.Tuple([uop_5954,])
output2 = relay.Tuple([uop_5954,])
func_5957 = relay.Function([var_5953,], output)
mod['func_5957'] = func_5957
mod = relay.transform.InferType()(mod)
mutated_mod['func_5957'] = func_5957
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5958 = relay.var("var_5958", dtype = "float64", shape = (1, 13, 2))#candidate|5958|(1, 13, 2)|var|float64
func_5957_call = mutated_mod.get_global_var('func_5957')
call_5959 = func_5957_call(var_5958)
output = call_5959
func_5960 = relay.Function([var_5958], output)
mutated_mod['func_5960'] = func_5960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4454_call = mod.get_global_var('func_4454')
func_4455_call = mutated_mod.get_global_var('func_4455')
call_6047 = func_4454_call()
call_6048 = func_4454_call()
output = relay.Tuple([call_6047,])
output2 = relay.Tuple([call_6048,])
func_6053 = relay.Function([], output)
mod['func_6053'] = func_6053
mod = relay.transform.InferType()(mod)
output = func_6053()
func_6054 = relay.Function([], output)
mutated_mod['func_6054'] = func_6054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1489_call = mod.get_global_var('func_1489')
func_1490_call = mutated_mod.get_global_var('func_1490')
call_6061 = relay.TupleGetItem(func_1489_call(), 0)
call_6062 = relay.TupleGetItem(func_1490_call(), 0)
var_6080 = relay.var("var_6080", dtype = "float32", shape = (2, 7, 16))#candidate|6080|(2, 7, 16)|var|float32
bop_6081 = relay.less_equal(call_6061.astype('bool'), var_6080.astype('bool')) # shape=(2, 7, 16)
bop_6084 = relay.less_equal(call_6062.astype('bool'), var_6080.astype('bool')) # shape=(2, 7, 16)
output = bop_6081
output2 = bop_6084
func_6085 = relay.Function([var_6080,], output)
mod['func_6085'] = func_6085
mod = relay.transform.InferType()(mod)
var_6086 = relay.var("var_6086", dtype = "float32", shape = (2, 7, 16))#candidate|6086|(2, 7, 16)|var|float32
output = func_6085(var_6086)
func_6087 = relay.Function([var_6086], output)
mutated_mod['func_6087'] = func_6087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6053_call = mod.get_global_var('func_6053')
func_6054_call = mutated_mod.get_global_var('func_6054')
call_6176 = relay.TupleGetItem(func_6053_call(), 0)
call_6177 = relay.TupleGetItem(func_6054_call(), 0)
output = call_6176
output2 = call_6177
func_6196 = relay.Function([], output)
mod['func_6196'] = func_6196
mod = relay.transform.InferType()(mod)
mutated_mod['func_6196'] = func_6196
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6196_call = mutated_mod.get_global_var('func_6196')
call_6197 = func_6196_call()
output = call_6197
func_6198 = relay.Function([], output)
mutated_mod['func_6198'] = func_6198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_675_call = mod.get_global_var('func_675')
func_677_call = mutated_mod.get_global_var('func_677')
call_6451 = func_675_call()
call_6452 = func_675_call()
func_3891_call = mod.get_global_var('func_3891')
func_3893_call = mutated_mod.get_global_var('func_3893')
call_6462 = relay.TupleGetItem(func_3891_call(), 0)
call_6463 = relay.TupleGetItem(func_3893_call(), 0)
func_3438_call = mod.get_global_var('func_3438')
func_3440_call = mutated_mod.get_global_var('func_3440')
call_6465 = func_3438_call()
call_6466 = func_3438_call()
output = relay.Tuple([call_6451,call_6462,call_6465,])
output2 = relay.Tuple([call_6452,call_6463,call_6466,])
func_6474 = relay.Function([], output)
mod['func_6474'] = func_6474
mod = relay.transform.InferType()(mod)
output = func_6474()
func_6475 = relay.Function([], output)
mutated_mod['func_6475'] = func_6475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5645_call = mod.get_global_var('func_5645')
func_5646_call = mutated_mod.get_global_var('func_5646')
call_6525 = relay.TupleGetItem(func_5645_call(), 0)
call_6526 = relay.TupleGetItem(func_5646_call(), 0)
func_2056_call = mod.get_global_var('func_2056')
func_2061_call = mutated_mod.get_global_var('func_2061')
const_6533 = relay.const([-9.935861,-5.162805,-7.119739,-2.422225,1.286835,-7.484987,2.172125,-2.655983,4.622312,1.997104,-4.391382,5.646582,6.574502,-9.734856,0.777257,-7.799888,9.111303,-9.150962,-7.881352,0.714763,4.824277,8.283299,-5.692804,5.523244,-1.522003,2.314341,-6.146385,-9.505594,-2.280559,-0.039844,2.875045,-2.585791,8.329931,-9.546402,6.388441,-4.026529,6.436241,-4.568060,0.972017,-1.716140,-1.217787,-8.926632,-7.261852,-0.179963,-0.025207,-6.421672,9.931945,-5.001056,-0.838065,-4.252120,0.095519,-1.012914,-7.135081,-5.431671,-1.813194,0.344303,-5.379657,8.057895,1.269236,-3.567825,9.991737,5.753946,6.259653,7.925309,4.279708,4.786959,-9.226744,8.770128,-8.517214,3.199911,-4.812884,4.852477,-4.501073,-9.340667,9.993314,1.487149,5.841690,1.212937,6.553285,-2.161352,8.443126,3.758624,8.824586,-3.717063,-0.652855,-9.734796,5.066641,0.384296,7.020662,0.485920,-5.779271,2.468596,5.636944,-3.013580,2.735169,3.643885,8.245442,6.219338,-2.599945,-9.141076,3.664011,5.318672,7.857709,-0.081658,-3.101724,1.721426,0.841732,4.684973,4.386787,5.748760,-1.853722,5.895129,5.869567,4.404283,1.937270,-7.215994,-9.415066,4.380578,-0.221880,-3.060620,4.655823,-7.333088,-6.769784,2.613984,7.358633,9.009693,-0.343572,8.272300,2.077590,8.321153,4.568188,9.358391,8.668627,4.176332,-5.037031,8.798854,3.032775,-6.130562,3.329404,8.890520,-4.497565,-6.054341,-2.631893,-3.288779,-7.837730,-8.898342,4.381787,-2.187637,-8.980549,1.175580,6.583485,-4.810936,-3.901697,7.879534,-1.886521,-0.727754,2.065711,6.230684,5.606149,4.149468,6.543003,0.795056,0.928483,-0.683177,3.397969,-3.495707,-7.452957,6.328346,-1.784035,-8.196314,6.681763,5.416829,3.110548,-4.284162,0.075923,3.825850,3.338042,5.723404,-4.332907,-9.707515,9.201300,-0.728536,2.043837,-3.132043,-2.439410,8.620522,-8.436732,-0.839012,3.040384,-0.128723,-7.758008,-3.577798,-1.238469,-1.877625,6.833515,-4.836440,-4.399682,-1.936838,-6.364885,6.160451,4.321425,-9.949701,5.326105,7.023621,-9.049176,3.545859,9.673065,-4.441782,-1.415880,-5.569339,-9.900220,-0.949919,-1.477209,-4.413420,-5.410400,5.597655], dtype = "float32")#candidate|6533|(216,)|const|float32
var_6534 = relay.var("var_6534", dtype = "float32", shape = (3600,))#candidate|6534|(3600,)|var|float32
const_6535 = relay.const([-2,10,-10,6,7,1,8,1,-10,3,-7,-6,3,5,5,-9,-2,10,7,7,9,7,10,5,6,5,-2,10,-3,1,6,-5,-8,-4,1,10,-7,-9,-4,-8,-2,-4,6,-2,-1,-8,-4,7,8,-8,3,10,2,9,-4,8,2,2,8,-6,8,7,-7,-3,-6,-7,-8,8,-6,8,8,8,10,5,-6,6,-8,-8,-7,-1,2,1,5,-10,10,5,-5,-5,4,10,4,-6,9,7,-4,9,6,-8,9,4,-7,7,-3,-7,-2,-7,-5,9,6,9,4,-8,8,-3,-3,8,5,3,8,5,7,6,-4,5,1,-1,-4,7,-2,-10,-7,-6,6,2,-9,3,10,5,6,-5,-6,2,-3,3,-9,-2,-3,-1,-8,-2,2,3,7,-6,-10,10,5,-5,10,6,10,6,-8,4,-1,-5,4,-5,-7,-3,-1,-2,-4,-7,-6,-4,2,-4,8,-6,-6,4,-8,2,1,2,-8,-10,-3,9,-1,10,2,4,9,2,1,-7,6,-4,-7,-3,-3,9,2,-9,-10,6,10,5,10,-7,3,9,7,10,-4,-9,6,4,8,8,-2,-10,-4,4,-2,4,6,7,-1,-7,10,1,-6,3,-10,-9,-7,5,-4,5,9,-1,5,10,7,-10,-3,-4,-7,2,9,-2,-2,10,-5,4,-6,-2,-7,8,8,-2,8,10,4,-3,-5,3,-1,5,-10,3,-8,-1,-5,-8,5,-6,9,-8,-7,-9,-5,10,-5,-5,6,3,3,8,2,-3,-7,10,2,-10,-9,1,-9,-4,-6,1,7,7,-9,7,2,-8,8,6,6,-1,4,10,5,-10,-3,4,-7,7,5,-5,6,7,-1,-8,-10,1,2,-9,-5,7,-10,-7,1,2,10,4,-1,3,-3,-9,9,7,1,-6,7,-4,4,5,-5,-1,4,-4,6,9,6,4,-7,-7,-1,3,-6,-4,-8,6,-3,10,-2,-4,-2,2,10,3,1,4,-3,-7,-5,9,-7,9,-2,9,5,-4,6,-5,4,-6,8,-4,-8,-7,-1,8,-1,-1,-8,-9,-4,2,-1,-10,4,7,-3,-10,3,4,6,-5,9,-4,-4,1,-5,10,9,8,-6,-3,7,2,5,-5,7,9,-6,4,5,-10,8,6,-1,-9,1,-6,9,10,3,4,5,-8,8,1,-7,4], dtype = "int8")#candidate|6535|(450,)|const|int8
call_6532 = relay.TupleGetItem(func_2056_call(relay.reshape(const_6533.astype('float32'), [216,]), relay.reshape(var_6534.astype('float32'), [10, 360]), relay.reshape(const_6535.astype('int8'), [5, 90]), ), 3)
call_6536 = relay.TupleGetItem(func_2061_call(relay.reshape(const_6533.astype('float32'), [216,]), relay.reshape(var_6534.astype('float32'), [10, 360]), relay.reshape(const_6535.astype('int8'), [5, 90]), ), 3)
uop_6544 = relay.sqrt(var_6534.astype('float64')) # shape=(3600,)
output = relay.Tuple([call_6525,call_6532,const_6533,const_6535,uop_6544,])
output2 = relay.Tuple([call_6526,call_6536,const_6533,const_6535,uop_6544,])
func_6549 = relay.Function([var_6534,], output)
mod['func_6549'] = func_6549
mod = relay.transform.InferType()(mod)
mutated_mod['func_6549'] = func_6549
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6550 = relay.var("var_6550", dtype = "float32", shape = (3600,))#candidate|6550|(3600,)|var|float32
func_6549_call = mutated_mod.get_global_var('func_6549')
call_6551 = func_6549_call(var_6550)
output = call_6551
func_6552 = relay.Function([var_6550], output)
mutated_mod['func_6552'] = func_6552
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1489_call = mod.get_global_var('func_1489')
func_1490_call = mutated_mod.get_global_var('func_1490')
call_6594 = relay.TupleGetItem(func_1489_call(), 0)
call_6595 = relay.TupleGetItem(func_1490_call(), 0)
func_650_call = mod.get_global_var('func_650')
func_655_call = mutated_mod.get_global_var('func_655')
var_6606 = relay.var("var_6606", dtype = "float32", shape = (36, 6))#candidate|6606|(36, 6)|var|float32
const_6607 = relay.const([-9.529701,-1.906592,0.518408,-3.842319,4.699665,1.067708,-4.170741,-5.823795,-3.854617,-7.990721,-4.956322,8.478581,8.903549,-3.988627,-9.208119,-5.305413,2.853985,-1.261933,-6.363723,-9.852656,-9.472906,7.267862,-4.654031,9.816382,1.078989,-1.076316,-6.654842,5.745967,1.700811,-0.542874,1.543534,-0.261010,3.849838,3.443210,-9.427463,2.671975,-1.195036,2.585349,-7.097709,1.022272,-2.726703,0.528767,-5.503501,1.859809,-5.055507,4.907610,-7.822511,-6.478171,-4.285869,7.596602,3.243490,5.319084,-9.710101,-8.214508,2.883570,-2.035960,-3.966899,-0.056294,-5.826278,-2.035954,-3.742988,7.429316,-7.455193,-7.950719,7.896447,9.415983,6.285580,-0.402023,1.393855,-7.158494,0.152786,0.931275,2.850303,-7.191911,7.061075,-4.238561,-5.904306,-3.207312,-4.834668,8.298022,-5.467071,-9.957999,-8.700371,3.006153,-5.279402,-1.980772,9.014665,4.705692,-6.772369,-0.131761,-0.140818,1.549088,-7.907098,9.432385,-2.590996,0.793370,7.564043,-6.780929,-2.721554,-8.830933,-7.495627,-6.073378,-5.690891,-4.822213,5.030071,-2.833931,5.947741,-6.668703,4.044309,-6.595459,3.348852,-9.468729,-4.703502,-3.169292,5.042069,3.192042,4.203400,5.209739,3.976330,-9.909019,-4.539281,-1.760094,-1.462541,-1.278746,2.075127,-4.606099,-9.362997,7.102303,8.996900,0.935762,-3.824860,-9.110913,5.891011,3.986943,0.820658,2.172517,-2.764994,-3.090039,2.467738,-7.073042,6.852094,8.393044,-4.803151,-2.609229,-2.563874,-0.164938,-3.620702,-7.815249,-9.224432,-7.396939,-9.999569,4.551450,-7.667203,9.783754,-9.202801,-1.792312,-5.545494,0.857860,-3.163765,8.224066,-9.219026,-6.478245,-7.594013,-6.845151,-5.210486,1.920681,-0.004376,-8.277749,-4.868127,-3.432504,0.170284,-3.102465,-1.096629,-6.821519,-9.674862,3.209393,5.252770,7.717759,3.417572,-1.592476,7.610349,-5.488522,8.492770,-4.880217,-4.617667,-4.736348,9.001813,-4.282503,1.067299,-8.240866,-5.999877,-3.227645,3.555192,7.906970,8.053195,3.047995,2.850428,-5.692562,-3.114391,-9.177987,-2.597463,-4.017736,-8.371618,2.342058,-3.894080,4.988917,-4.044975,-6.789361,1.495671,-4.172191,-9.441811,7.382626,3.151908,-7.524822,-5.672553,-2.342920,1.922810,-7.989731,6.575056,6.385211,-2.179168,-9.914438,-5.366106,-5.809716,3.285275], dtype = "float32")#candidate|6607|(225,)|const|float32
var_6608 = relay.var("var_6608", dtype = "float32", shape = (3600, 1))#candidate|6608|(3600, 1)|var|float32
call_6605 = relay.TupleGetItem(func_650_call(relay.reshape(var_6606.astype('float32'), [9, 12, 2]), relay.reshape(const_6607.astype('float32'), [25, 9]), relay.reshape(var_6608.astype('float32'), [3600,]), ), 0)
call_6609 = relay.TupleGetItem(func_655_call(relay.reshape(var_6606.astype('float32'), [9, 12, 2]), relay.reshape(const_6607.astype('float32'), [25, 9]), relay.reshape(var_6608.astype('float32'), [3600,]), ), 0)
output = relay.Tuple([call_6594,call_6605,var_6606,const_6607,var_6608,])
output2 = relay.Tuple([call_6595,call_6609,var_6606,const_6607,var_6608,])
func_6613 = relay.Function([var_6606,var_6608,], output)
mod['func_6613'] = func_6613
mod = relay.transform.InferType()(mod)
var_6614 = relay.var("var_6614", dtype = "float32", shape = (36, 6))#candidate|6614|(36, 6)|var|float32
var_6615 = relay.var("var_6615", dtype = "float32", shape = (3600, 1))#candidate|6615|(3600, 1)|var|float32
output = func_6613(var_6614,var_6615,)
func_6616 = relay.Function([var_6614,var_6615,], output)
mutated_mod['func_6616'] = func_6616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3891_call = mod.get_global_var('func_3891')
func_3893_call = mutated_mod.get_global_var('func_3893')
call_6649 = relay.TupleGetItem(func_3891_call(), 1)
call_6650 = relay.TupleGetItem(func_3893_call(), 1)
output = relay.Tuple([call_6649,])
output2 = relay.Tuple([call_6650,])
func_6654 = relay.Function([], output)
mod['func_6654'] = func_6654
mod = relay.transform.InferType()(mod)
output = func_6654()
func_6655 = relay.Function([], output)
mutated_mod['func_6655'] = func_6655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3781_call = mod.get_global_var('func_3781')
func_3782_call = mutated_mod.get_global_var('func_3782')
call_6686 = func_3781_call()
call_6687 = func_3781_call()
output = relay.Tuple([call_6686,])
output2 = relay.Tuple([call_6687,])
func_6694 = relay.Function([], output)
mod['func_6694'] = func_6694
mod = relay.transform.InferType()(mod)
output = func_6694()
func_6695 = relay.Function([], output)
mutated_mod['func_6695'] = func_6695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1190_call = mod.get_global_var('func_1190')
func_1191_call = mutated_mod.get_global_var('func_1191')
call_6770 = func_1190_call()
call_6771 = func_1190_call()
func_3891_call = mod.get_global_var('func_3891')
func_3893_call = mutated_mod.get_global_var('func_3893')
call_6779 = relay.TupleGetItem(func_3891_call(), 1)
call_6780 = relay.TupleGetItem(func_3893_call(), 1)
func_1819_call = mod.get_global_var('func_1819')
func_1823_call = mutated_mod.get_global_var('func_1823')
var_6785 = relay.var("var_6785", dtype = "uint32", shape = (6, 100))#candidate|6785|(6, 100)|var|uint32
const_6786 = relay.const([1,-1,-1,3,-3,-8,3,8,2,-4,10,7,-2,8,-1,-7,9,5,10,-2,8,6,10,3,-1,-10,-1,-8,-5,-6,-5,1,10,4,5,-10,5,-4,-10,-8,4,-4,4,7,-10,8,-5,-9,-6,-2,8,3,2,8,-4,2,4,-4,-8,8,3,5,-6,2,7,10,-10,7,-2,-3,-3,6,-1,-8,1,-8,1,-4,-8,-8,4,8,-2,-7,4,-1,-5,4,7,-8,7,7,-9,-6,1,2,5,1,-7,-2,-8,-7,3,-2,5,-1,6,-4,-10,2,6,7,3,9,-6,-2,7,9,1,10,-1,-10,-10,-4,5,-2,-1,2,-8,-6,3,1,5,8,3,-6,1,-3,-10,-1,-2,-6,5,7,-9,10,-10,2,2,3,-9,10,-5,-1,10,10,7,7,5,5,-8,8,7,3,-1,5,-7,8,-9,-9,-10,-3,8,-1,5,-9,-3,10,8,-9,2,-8,8,5,6,-8,-4,5,2,-6,-4,-1,3,-8,7,-3,1,1,9,9,-9,-2,-8,6,-5,-1,9,-7,-3,7,-4,2,2,-5,7,-6,8,3,5,10,-4,-10,-2,9,-3,7,7,-3,1,1,1,-8,5,7,-1,-1,-7,-1,-9,-6,7,10,-3,2,-10,-3,10,9,3,7,-4,-2,-9,-2,1,9,-1,1,-3,-7,-8,3,4,-5,-10,2,9,7,-4,6,-6,5,-5,1,-9,-10,-9,-7,5,-1,-4,-10,-6,3,-7,7,-4,-3,9,1,-4,-9,6,-7,7,7,-8,4,-6,-4,-6,10,-5,2,-9,-4,-4,6,-8,-10,-1,-6,-3,-3,-9,-4,1,-6,-9,2,1,-2,8,2,3,1,-8,2,-9,-2,3,-3,2,-3,-8,-10,1,-4,10,-5,8,6,4,1,5,4,-9,-4,-8,3,-2,-5,-5,-9,4,9,-1,2,-4,-1,-4,9,-3,8,10,9,4,-2,-2,-5,7,2,10,-3,7,-3,8,6,-5,-3,6,8,6,1,2,-8,-2,7,4,-6,4,4,3,3,6,6,8,2,-3,3,8,4,-2,10,1,-9,-9,-6,2,-4,-5,-10,2,6,4,-3,-1,-10,10,-2,-10,-7,-3,1,2,4,6,8,-8,5,4,-4,-7,-1,-6,9,4,-5,8,-2,3,-8,2,9,4,9,4,-4,-8,7], dtype = "int8")#candidate|6786|(450,)|const|int8
var_6787 = relay.var("var_6787", dtype = "float32", shape = (3600,))#candidate|6787|(3600,)|var|float32
call_6784 = relay.TupleGetItem(func_1819_call(relay.reshape(var_6785.astype('uint32'), [12, 5, 10]), relay.reshape(const_6786.astype('int8'), [1, 450]), relay.reshape(var_6787.astype('float32'), [3600,]), ), 1)
call_6788 = relay.TupleGetItem(func_1823_call(relay.reshape(var_6785.astype('uint32'), [12, 5, 10]), relay.reshape(const_6786.astype('int8'), [1, 450]), relay.reshape(var_6787.astype('float32'), [3600,]), ), 1)
uop_6796 = relay.asin(var_6785.astype('float32')) # shape=(6, 100)
func_2258_call = mod.get_global_var('func_2258')
func_2260_call = mutated_mod.get_global_var('func_2260')
call_6802 = relay.TupleGetItem(func_2258_call(), 0)
call_6803 = relay.TupleGetItem(func_2260_call(), 0)
func_2759_call = mod.get_global_var('func_2759')
func_2761_call = mutated_mod.get_global_var('func_2761')
call_6807 = func_2759_call()
call_6808 = func_2759_call()
bop_6810 = relay.greater(call_6779.astype('bool'), const_6786.astype('bool')) # shape=(2, 7, 450)
bop_6813 = relay.greater(call_6780.astype('bool'), const_6786.astype('bool')) # shape=(2, 7, 450)
output = relay.Tuple([call_6770,call_6784,var_6787,uop_6796,call_6802,call_6807,bop_6810,])
output2 = relay.Tuple([call_6771,call_6788,var_6787,uop_6796,call_6803,call_6808,bop_6813,])
func_6831 = relay.Function([var_6785,var_6787,], output)
mod['func_6831'] = func_6831
mod = relay.transform.InferType()(mod)
mutated_mod['func_6831'] = func_6831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6831_call = mutated_mod.get_global_var('func_6831')
var_6833 = relay.var("var_6833", dtype = "uint32", shape = (6, 100))#candidate|6833|(6, 100)|var|uint32
var_6834 = relay.var("var_6834", dtype = "float32", shape = (3600,))#candidate|6834|(3600,)|var|float32
call_6832 = func_6831_call(var_6833,var_6834,)
output = call_6832
func_6835 = relay.Function([var_6833,var_6834,], output)
mutated_mod['func_6835'] = func_6835
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1887_call = mod.get_global_var('func_1887')
func_1889_call = mutated_mod.get_global_var('func_1889')
call_6866 = relay.TupleGetItem(func_1887_call(), 1)
call_6867 = relay.TupleGetItem(func_1889_call(), 1)
func_3996_call = mod.get_global_var('func_3996')
func_3998_call = mutated_mod.get_global_var('func_3998')
call_6874 = relay.TupleGetItem(func_3996_call(), 0)
call_6875 = relay.TupleGetItem(func_3998_call(), 0)
output = relay.Tuple([call_6866,call_6874,])
output2 = relay.Tuple([call_6867,call_6875,])
func_6904 = relay.Function([], output)
mod['func_6904'] = func_6904
mod = relay.transform.InferType()(mod)
mutated_mod['func_6904'] = func_6904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6904_call = mutated_mod.get_global_var('func_6904')
call_6905 = func_6904_call()
output = call_6905
func_6906 = relay.Function([], output)
mutated_mod['func_6906'] = func_6906
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6919 = relay.var("var_6919", dtype = "float32", shape = (9, 14, 1))#candidate|6919|(9, 14, 1)|var|float32
var_6920 = relay.var("var_6920", dtype = "float32", shape = (9, 14, 1))#candidate|6920|(9, 14, 1)|var|float32
bop_6921 = relay.divide(var_6919.astype('float32'), relay.reshape(var_6920.astype('float32'), relay.shape_of(var_6919))) # shape=(9, 14, 1)
var_6924 = relay.var("var_6924", dtype = "float32", shape = (9, 14, 1))#candidate|6924|(9, 14, 1)|var|float32
bop_6925 = relay.logical_and(bop_6921.astype('bool'), relay.reshape(var_6924.astype('bool'), relay.shape_of(bop_6921))) # shape=(9, 14, 1)
func_2453_call = mod.get_global_var('func_2453')
func_2455_call = mutated_mod.get_global_var('func_2455')
var_6931 = relay.var("var_6931", dtype = "float32", shape = (75, 3))#candidate|6931|(75, 3)|var|float32
call_6930 = relay.TupleGetItem(func_2453_call(relay.reshape(var_6931.astype('float32'), [225,])), 7)
call_6932 = relay.TupleGetItem(func_2455_call(relay.reshape(var_6931.astype('float32'), [225,])), 7)
output = relay.Tuple([bop_6925,call_6930,var_6931,])
output2 = relay.Tuple([bop_6925,call_6932,var_6931,])
func_6934 = relay.Function([var_6919,var_6920,var_6924,var_6931,], output)
mod['func_6934'] = func_6934
mod = relay.transform.InferType()(mod)
var_6935 = relay.var("var_6935", dtype = "float32", shape = (9, 14, 1))#candidate|6935|(9, 14, 1)|var|float32
var_6936 = relay.var("var_6936", dtype = "float32", shape = (9, 14, 1))#candidate|6936|(9, 14, 1)|var|float32
var_6937 = relay.var("var_6937", dtype = "float32", shape = (9, 14, 1))#candidate|6937|(9, 14, 1)|var|float32
var_6938 = relay.var("var_6938", dtype = "float32", shape = (75, 3))#candidate|6938|(75, 3)|var|float32
output = func_6934(var_6935,var_6936,var_6937,var_6938,)
func_6939 = relay.Function([var_6935,var_6936,var_6937,var_6938,], output)
mutated_mod['func_6939'] = func_6939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1324_call = mod.get_global_var('func_1324')
func_1325_call = mutated_mod.get_global_var('func_1325')
call_6955 = relay.TupleGetItem(func_1324_call(), 0)
call_6956 = relay.TupleGetItem(func_1325_call(), 0)
func_2854_call = mod.get_global_var('func_2854')
func_2857_call = mutated_mod.get_global_var('func_2857')
var_6958 = relay.var("var_6958", dtype = "int8", shape = (450,))#candidate|6958|(450,)|var|int8
call_6957 = relay.TupleGetItem(func_2854_call(relay.reshape(var_6958.astype('int8'), [5, 10, 9])), 2)
call_6959 = relay.TupleGetItem(func_2857_call(relay.reshape(var_6958.astype('int8'), [5, 10, 9])), 2)
output = relay.Tuple([call_6955,call_6957,var_6958,])
output2 = relay.Tuple([call_6956,call_6959,var_6958,])
func_6968 = relay.Function([var_6958,], output)
mod['func_6968'] = func_6968
mod = relay.transform.InferType()(mod)
var_6969 = relay.var("var_6969", dtype = "int8", shape = (450,))#candidate|6969|(450,)|var|int8
output = func_6968(var_6969)
func_6970 = relay.Function([var_6969], output)
mutated_mod['func_6970'] = func_6970
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4708_call = mod.get_global_var('func_4708')
func_4709_call = mutated_mod.get_global_var('func_4709')
call_7013 = relay.TupleGetItem(func_4708_call(), 0)
call_7014 = relay.TupleGetItem(func_4709_call(), 0)
output = relay.Tuple([call_7013,])
output2 = relay.Tuple([call_7014,])
func_7017 = relay.Function([], output)
mod['func_7017'] = func_7017
mod = relay.transform.InferType()(mod)
output = func_7017()
func_7018 = relay.Function([], output)
mutated_mod['func_7018'] = func_7018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1171_call = mod.get_global_var('func_1171')
func_1173_call = mutated_mod.get_global_var('func_1173')
call_7032 = relay.TupleGetItem(func_1171_call(), 1)
call_7033 = relay.TupleGetItem(func_1173_call(), 1)
output = call_7032
output2 = call_7033
func_7039 = relay.Function([], output)
mod['func_7039'] = func_7039
mod = relay.transform.InferType()(mod)
mutated_mod['func_7039'] = func_7039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7039_call = mutated_mod.get_global_var('func_7039')
call_7040 = func_7039_call()
output = call_7040
func_7041 = relay.Function([], output)
mutated_mod['func_7041'] = func_7041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3781_call = mod.get_global_var('func_3781')
func_3782_call = mutated_mod.get_global_var('func_3782')
call_7045 = func_3781_call()
call_7046 = func_3781_call()
func_5148_call = mod.get_global_var('func_5148')
func_5150_call = mutated_mod.get_global_var('func_5150')
call_7070 = relay.TupleGetItem(func_5148_call(), 0)
call_7071 = relay.TupleGetItem(func_5150_call(), 0)
func_753_call = mod.get_global_var('func_753')
func_755_call = mutated_mod.get_global_var('func_755')
call_7074 = func_753_call()
call_7075 = func_753_call()
func_4065_call = mod.get_global_var('func_4065')
func_4066_call = mutated_mod.get_global_var('func_4066')
call_7076 = relay.TupleGetItem(func_4065_call(), 0)
call_7077 = relay.TupleGetItem(func_4066_call(), 0)
output = relay.Tuple([call_7045,call_7070,call_7074,call_7076,])
output2 = relay.Tuple([call_7046,call_7071,call_7075,call_7077,])
func_7081 = relay.Function([], output)
mod['func_7081'] = func_7081
mod = relay.transform.InferType()(mod)
mutated_mod['func_7081'] = func_7081
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7081_call = mutated_mod.get_global_var('func_7081')
call_7082 = func_7081_call()
output = call_7082
func_7083 = relay.Function([], output)
mutated_mod['func_7083'] = func_7083
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1899_call = mod.get_global_var('func_1899')
func_1901_call = mutated_mod.get_global_var('func_1901')
call_7111 = relay.TupleGetItem(func_1899_call(), 0)
call_7112 = relay.TupleGetItem(func_1901_call(), 0)
func_1971_call = mod.get_global_var('func_1971')
func_1976_call = mutated_mod.get_global_var('func_1976')
var_7127 = relay.var("var_7127", dtype = "float64", shape = (900,))#candidate|7127|(900,)|var|float64
var_7128 = relay.var("var_7128", dtype = "int16", shape = ())#candidate|7128|()|var|int16
var_7129 = relay.var("var_7129", dtype = "int16", shape = (2700,))#candidate|7129|(2700,)|var|int16
call_7126 = relay.TupleGetItem(func_1971_call(relay.reshape(var_7127.astype('float64'), [15, 6, 10]), relay.reshape(var_7128.astype('int16'), []), relay.reshape(var_7129.astype('int16'), [2700,]), ), 3)
call_7130 = relay.TupleGetItem(func_1976_call(relay.reshape(var_7127.astype('float64'), [15, 6, 10]), relay.reshape(var_7128.astype('int16'), []), relay.reshape(var_7129.astype('int16'), [2700,]), ), 3)
output = relay.Tuple([call_7111,call_7126,var_7127,var_7128,var_7129,])
output2 = relay.Tuple([call_7112,call_7130,var_7127,var_7128,var_7129,])
func_7136 = relay.Function([var_7127,var_7128,var_7129,], output)
mod['func_7136'] = func_7136
mod = relay.transform.InferType()(mod)
mutated_mod['func_7136'] = func_7136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7136_call = mutated_mod.get_global_var('func_7136')
var_7138 = relay.var("var_7138", dtype = "float64", shape = (900,))#candidate|7138|(900,)|var|float64
var_7139 = relay.var("var_7139", dtype = "int16", shape = ())#candidate|7139|()|var|int16
var_7140 = relay.var("var_7140", dtype = "int16", shape = (2700,))#candidate|7140|(2700,)|var|int16
call_7137 = func_7136_call(var_7138,var_7139,var_7140,)
output = call_7137
func_7141 = relay.Function([var_7138,var_7139,var_7140,], output)
mutated_mod['func_7141'] = func_7141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3084_call = mod.get_global_var('func_3084')
func_3086_call = mutated_mod.get_global_var('func_3086')
call_7257 = relay.TupleGetItem(func_3084_call(), 0)
call_7258 = relay.TupleGetItem(func_3086_call(), 0)
func_1778_call = mod.get_global_var('func_1778')
func_1780_call = mutated_mod.get_global_var('func_1780')
call_7265 = relay.TupleGetItem(func_1778_call(), 0)
call_7266 = relay.TupleGetItem(func_1780_call(), 0)
bop_7274 = relay.floor_mod(call_7257.astype('float64'), relay.reshape(call_7265.astype('float64'), relay.shape_of(call_7257))) # shape=(2, 7, 1)
bop_7277 = relay.floor_mod(call_7258.astype('float64'), relay.reshape(call_7266.astype('float64'), relay.shape_of(call_7258))) # shape=(2, 7, 1)
func_7081_call = mod.get_global_var('func_7081')
func_7083_call = mutated_mod.get_global_var('func_7083')
call_7290 = relay.TupleGetItem(func_7081_call(), 2)
call_7291 = relay.TupleGetItem(func_7083_call(), 2)
func_1887_call = mod.get_global_var('func_1887')
func_1889_call = mutated_mod.get_global_var('func_1889')
call_7292 = relay.TupleGetItem(func_1887_call(), 2)
call_7293 = relay.TupleGetItem(func_1889_call(), 2)
func_5885_call = mod.get_global_var('func_5885')
func_5887_call = mutated_mod.get_global_var('func_5887')
call_7303 = relay.TupleGetItem(func_5885_call(), 0)
call_7304 = relay.TupleGetItem(func_5887_call(), 0)
func_1819_call = mod.get_global_var('func_1819')
func_1823_call = mutated_mod.get_global_var('func_1823')
var_7314 = relay.var("var_7314", dtype = "uint32", shape = (12, 50))#candidate|7314|(12, 50)|var|uint32
var_7315 = relay.var("var_7315", dtype = "float32", shape = (3600,))#candidate|7315|(3600,)|var|float32
call_7313 = relay.TupleGetItem(func_1819_call(relay.reshape(var_7314.astype('uint32'), [12, 5, 10]), relay.reshape(call_7292.astype('int8'), [1, 450]), relay.reshape(var_7315.astype('float32'), [3600,]), ), 2)
call_7316 = relay.TupleGetItem(func_1823_call(relay.reshape(var_7314.astype('uint32'), [12, 5, 10]), relay.reshape(call_7292.astype('int8'), [1, 450]), relay.reshape(var_7315.astype('float32'), [3600,]), ), 2)
bop_7340 = relay.bitwise_or(call_7257.astype('uint8'), var_7315.astype('uint8')) # shape=(2, 7, 3600)
bop_7343 = relay.bitwise_or(call_7258.astype('uint8'), var_7315.astype('uint8')) # shape=(2, 7, 3600)
func_1691_call = mod.get_global_var('func_1691')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_7344 = relay.TupleGetItem(func_1691_call(), 0)
call_7345 = relay.TupleGetItem(func_1693_call(), 0)
output = relay.Tuple([bop_7274,call_7290,call_7292,call_7303,call_7313,var_7314,bop_7340,call_7344,])
output2 = relay.Tuple([bop_7277,call_7291,call_7293,call_7304,call_7316,var_7314,bop_7343,call_7345,])
func_7354 = relay.Function([var_7314,var_7315,], output)
mod['func_7354'] = func_7354
mod = relay.transform.InferType()(mod)
var_7355 = relay.var("var_7355", dtype = "uint32", shape = (12, 50))#candidate|7355|(12, 50)|var|uint32
var_7356 = relay.var("var_7356", dtype = "float32", shape = (3600,))#candidate|7356|(3600,)|var|float32
output = func_7354(var_7355,var_7356,)
func_7357 = relay.Function([var_7355,var_7356,], output)
mutated_mod['func_7357'] = func_7357
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7430 = relay.var("var_7430", dtype = "int64", shape = ())#candidate|7430|()|var|int64
var_7431 = relay.var("var_7431", dtype = "int64", shape = (9, 4, 7))#candidate|7431|(9, 4, 7)|var|int64
bop_7432 = relay.add(var_7430.astype('int64'), var_7431.astype('int64')) # shape=(9, 4, 7)
output = bop_7432
output2 = bop_7432
func_7446 = relay.Function([var_7430,var_7431,], output)
mod['func_7446'] = func_7446
mod = relay.transform.InferType()(mod)
mutated_mod['func_7446'] = func_7446
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7446_call = mutated_mod.get_global_var('func_7446')
var_7448 = relay.var("var_7448", dtype = "int64", shape = ())#candidate|7448|()|var|int64
var_7449 = relay.var("var_7449", dtype = "int64", shape = (9, 4, 7))#candidate|7449|(9, 4, 7)|var|int64
call_7447 = func_7446_call(var_7448,var_7449,)
output = call_7447
func_7450 = relay.Function([var_7448,var_7449,], output)
mutated_mod['func_7450'] = func_7450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3643_call = mod.get_global_var('func_3643')
func_3645_call = mutated_mod.get_global_var('func_3645')
call_7497 = relay.TupleGetItem(func_3643_call(), 0)
call_7498 = relay.TupleGetItem(func_3645_call(), 0)
func_1119_call = mod.get_global_var('func_1119')
func_1120_call = mutated_mod.get_global_var('func_1120')
call_7499 = relay.TupleGetItem(func_1119_call(), 0)
call_7500 = relay.TupleGetItem(func_1120_call(), 0)
output = relay.Tuple([call_7497,call_7499,])
output2 = relay.Tuple([call_7498,call_7500,])
func_7508 = relay.Function([], output)
mod['func_7508'] = func_7508
mod = relay.transform.InferType()(mod)
mutated_mod['func_7508'] = func_7508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7508_call = mutated_mod.get_global_var('func_7508')
call_7509 = func_7508_call()
output = call_7509
func_7510 = relay.Function([], output)
mutated_mod['func_7510'] = func_7510
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7571 = relay.var("var_7571", dtype = "int32", shape = ())#candidate|7571|()|var|int32
var_7572 = relay.var("var_7572", dtype = "int32", shape = (4, 3, 1))#candidate|7572|(4, 3, 1)|var|int32
bop_7573 = relay.logical_xor(var_7571.astype('int32'), var_7572.astype('int32')) # shape=(4, 3, 1)
bop_7589 = relay.less(bop_7573.astype('bool'), var_7571.astype('bool')) # shape=(4, 3, 1)
output = relay.Tuple([bop_7589,])
output2 = relay.Tuple([bop_7589,])
func_7594 = relay.Function([var_7571,var_7572,], output)
mod['func_7594'] = func_7594
mod = relay.transform.InferType()(mod)
mutated_mod['func_7594'] = func_7594
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7594_call = mutated_mod.get_global_var('func_7594')
var_7596 = relay.var("var_7596", dtype = "int32", shape = ())#candidate|7596|()|var|int32
var_7597 = relay.var("var_7597", dtype = "int32", shape = (4, 3, 1))#candidate|7597|(4, 3, 1)|var|int32
call_7595 = func_7594_call(var_7596,var_7597,)
output = call_7595
func_7598 = relay.Function([var_7596,var_7597,], output)
mutated_mod['func_7598'] = func_7598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3929_call = mod.get_global_var('func_3929')
func_3931_call = mutated_mod.get_global_var('func_3931')
call_7622 = relay.TupleGetItem(func_3929_call(), 0)
call_7623 = relay.TupleGetItem(func_3931_call(), 0)
func_5176_call = mod.get_global_var('func_5176')
func_5178_call = mutated_mod.get_global_var('func_5178')
call_7640 = relay.TupleGetItem(func_5176_call(), 1)
call_7641 = relay.TupleGetItem(func_5178_call(), 1)
output = relay.Tuple([call_7622,call_7640,])
output2 = relay.Tuple([call_7623,call_7641,])
func_7650 = relay.Function([], output)
mod['func_7650'] = func_7650
mod = relay.transform.InferType()(mod)
output = func_7650()
func_7651 = relay.Function([], output)
mutated_mod['func_7651'] = func_7651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3781_call = mod.get_global_var('func_3781')
func_3782_call = mutated_mod.get_global_var('func_3782')
call_7744 = func_3781_call()
call_7745 = func_3781_call()
output = relay.Tuple([call_7744,])
output2 = relay.Tuple([call_7745,])
func_7753 = relay.Function([], output)
mod['func_7753'] = func_7753
mod = relay.transform.InferType()(mod)
mutated_mod['func_7753'] = func_7753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7753_call = mutated_mod.get_global_var('func_7753')
call_7754 = func_7753_call()
output = call_7754
func_7755 = relay.Function([], output)
mutated_mod['func_7755'] = func_7755
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7784 = relay.var("var_7784", dtype = "float64", shape = (6, 11, 2))#candidate|7784|(6, 11, 2)|var|float64
uop_7785 = relay.rsqrt(var_7784.astype('float64')) # shape=(6, 11, 2)
uop_7800 = relay.sqrt(uop_7785.astype('float64')) # shape=(6, 11, 2)
func_753_call = mod.get_global_var('func_753')
func_755_call = mutated_mod.get_global_var('func_755')
call_7816 = func_753_call()
call_7817 = func_753_call()
output = relay.Tuple([uop_7800,call_7816,])
output2 = relay.Tuple([uop_7800,call_7817,])
func_7823 = relay.Function([var_7784,], output)
mod['func_7823'] = func_7823
mod = relay.transform.InferType()(mod)
mutated_mod['func_7823'] = func_7823
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7824 = relay.var("var_7824", dtype = "float64", shape = (6, 11, 2))#candidate|7824|(6, 11, 2)|var|float64
func_7823_call = mutated_mod.get_global_var('func_7823')
call_7825 = func_7823_call(var_7824)
output = call_7825
func_7826 = relay.Function([var_7824], output)
mutated_mod['func_7826'] = func_7826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5308_call = mod.get_global_var('func_5308')
func_5310_call = mutated_mod.get_global_var('func_5310')
call_7858 = relay.TupleGetItem(func_5308_call(), 3)
call_7859 = relay.TupleGetItem(func_5310_call(), 3)
var_7862 = relay.var("var_7862", dtype = "uint32", shape = (6, 100))#candidate|7862|(6, 100)|var|uint32
bop_7863 = relay.floor_mod(call_7858.astype('float32'), relay.reshape(var_7862.astype('float32'), relay.shape_of(call_7858))) # shape=(6, 100)
bop_7866 = relay.floor_mod(call_7859.astype('float32'), relay.reshape(var_7862.astype('float32'), relay.shape_of(call_7859))) # shape=(6, 100)
output = bop_7863
output2 = bop_7866
func_7872 = relay.Function([var_7862,], output)
mod['func_7872'] = func_7872
mod = relay.transform.InferType()(mod)
var_7873 = relay.var("var_7873", dtype = "uint32", shape = (6, 100))#candidate|7873|(6, 100)|var|uint32
output = func_7872(var_7873)
func_7874 = relay.Function([var_7873], output)
mutated_mod['func_7874'] = func_7874
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5148_call = mod.get_global_var('func_5148')
func_5150_call = mutated_mod.get_global_var('func_5150')
call_7918 = relay.TupleGetItem(func_5148_call(), 0)
call_7919 = relay.TupleGetItem(func_5150_call(), 0)
func_4558_call = mod.get_global_var('func_4558')
func_4561_call = mutated_mod.get_global_var('func_4561')
const_7925 = relay.const([-5.490073,-1.292816,7.056178,8.925970,-0.313387,1.304224,-5.482352,-3.564878,8.382683,5.673347,0.047078,-3.396065,-3.226570,-5.539632,-5.745994,-1.171929,-6.941694,-1.373808,-3.076269,-2.416625,9.311340,6.732754,3.699351,1.329944,-7.291413,-3.615947,-9.011916,1.265382,9.097750,-6.374930,2.795890,-5.892775,-9.667452,2.700261,-4.773268,9.488231,3.362564,1.577429,-5.005178,5.392103,-1.694164,1.681980,1.779873,6.220437,-6.956515,-6.767750,-1.605141,6.222077,1.828705,4.549447,-1.326217,1.350742,7.517891,-2.824562,6.076489,1.188532,-9.127914,-8.082956,1.453987,-5.878598,-9.811653,2.868568,-9.445046,1.236344,1.905880,6.788147,9.312759,5.930342,-9.400234,-0.990060,-0.221767,6.521240,-1.561016,-6.933095,6.785434,1.295169,0.322287,-8.064185,-8.360360,0.595675,9.651928,9.644396,-0.933778,8.749050,9.347687,-9.135458,2.447742,-0.091681,-1.900286,7.554946,5.082292,1.561111,6.520349,-1.822767,5.667971,3.343118,3.867943,1.432697,-1.121708,-2.125375,-2.272143,5.560059,-3.880306,-9.129446,-1.858476,-1.680999,-5.861345,-5.596398,6.407902,7.751007,-6.501349,3.175265,-4.914637,7.780590,-3.645652,-7.967427,2.792341,-9.077872,7.733383,-4.555162,5.029769,5.488723,-8.195091,3.542508,5.363151,-9.071369,-7.678442,6.730317,-8.690165,3.100230,-0.947263,2.343471,4.381070,5.448025,-2.349541,-2.458060,-1.735664,-4.335983,4.157080,-0.786713,-5.093126,-9.249595,3.250835,4.251972,5.917196,-8.770603,-7.970009,9.742154,4.202970,-1.830785,-3.632260,6.223467,5.338489,0.318860,-7.400702,6.154969,-3.557478,5.664478,3.922977,5.250408,2.453710,-8.222381,4.626899,1.740937,-6.518490,0.611044,-5.824985,3.154647,-7.886099,-2.912096,-2.620363,7.966763,8.442066,-4.743783,-2.868865,2.791994,2.064584,7.270963,3.370979,-3.159618,8.228427,-3.611562,-5.378177,6.532212,-6.266727,2.477597,1.413196,8.594206,0.292080,5.913162,2.099842,0.327233,-5.148453,-4.974078,2.324565,2.023630,-9.597162,-7.280501,5.459834,5.616705,6.748621,-9.519201,3.495154,-2.638473,-6.885599,-7.753074,-5.616991,-9.580391,6.140636,7.248903,8.842350,2.599224,-3.095195,9.269472,9.969377,-4.018499,7.103710,7.286779,-9.377668,-9.037994,7.399292,1.557644,-9.119131,-0.733527], dtype = "float32")#candidate|7925|(224,)|const|float32
call_7924 = relay.TupleGetItem(func_4558_call(relay.reshape(const_7925.astype('float32'), [2, 7, 16])), 0)
call_7926 = relay.TupleGetItem(func_4561_call(relay.reshape(const_7925.astype('float32'), [2, 7, 16])), 0)
output = relay.Tuple([call_7918,call_7924,const_7925,])
output2 = relay.Tuple([call_7919,call_7926,const_7925,])
func_7932 = relay.Function([], output)
mod['func_7932'] = func_7932
mod = relay.transform.InferType()(mod)
mutated_mod['func_7932'] = func_7932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7932_call = mutated_mod.get_global_var('func_7932')
call_7933 = func_7932_call()
output = call_7933
func_7934 = relay.Function([], output)
mutated_mod['func_7934'] = func_7934
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4065_call = mod.get_global_var('func_4065')
func_4066_call = mutated_mod.get_global_var('func_4066')
call_8023 = relay.TupleGetItem(func_4065_call(), 0)
call_8024 = relay.TupleGetItem(func_4066_call(), 0)
output = call_8023
output2 = call_8024
func_8032 = relay.Function([], output)
mod['func_8032'] = func_8032
mod = relay.transform.InferType()(mod)
output = func_8032()
func_8033 = relay.Function([], output)
mutated_mod['func_8033'] = func_8033
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7650_call = mod.get_global_var('func_7650')
func_7651_call = mutated_mod.get_global_var('func_7651')
call_8159 = relay.TupleGetItem(func_7650_call(), 0)
call_8160 = relay.TupleGetItem(func_7651_call(), 0)
func_1887_call = mod.get_global_var('func_1887')
func_1889_call = mutated_mod.get_global_var('func_1889')
call_8161 = relay.TupleGetItem(func_1887_call(), 0)
call_8162 = relay.TupleGetItem(func_1889_call(), 0)
func_2210_call = mod.get_global_var('func_2210')
func_2212_call = mutated_mod.get_global_var('func_2212')
call_8163 = relay.TupleGetItem(func_2210_call(), 0)
call_8164 = relay.TupleGetItem(func_2212_call(), 0)
func_1628_call = mod.get_global_var('func_1628')
func_1633_call = mutated_mod.get_global_var('func_1633')
const_8168 = relay.const([[9.387907,-5.630938],[-2.202869,-4.976456],[-8.070598,-1.501814],[-0.619747,-1.971597],[7.720203,-2.913042],[-2.012645,3.158927],[-1.616962,2.445567],[-5.237395,9.436675],[-2.486768,6.535212],[-8.127057,-0.273977],[-1.701846,7.137850],[-7.695132,6.434500],[7.602199,-8.822802],[2.394623,2.832557],[-5.142802,-8.586252],[3.897636,-5.120785],[0.304315,4.681465],[-7.054948,7.516963],[-1.130004,5.076620],[-7.022156,-0.406914],[8.359273,9.154198],[-7.182428,-6.518132],[4.476206,5.561884],[-6.486003,9.940837],[0.683518,6.609642],[-7.656242,5.151961],[4.581111,5.624392],[5.850022,-3.713268],[-4.126959,-1.471341],[-2.161626,6.920271],[6.360518,2.733240],[8.006590,-6.425874],[5.845189,-5.292567],[-8.595856,-3.013232],[-3.606759,4.058673],[-9.791102,-1.741178],[8.704337,0.137929],[6.870062,-5.323978],[-5.355537,-0.265060],[-1.702153,-1.172991],[-4.016840,6.827574],[-8.379256,6.506340],[6.341512,4.946823],[-5.901375,-1.955431],[-2.771783,9.525122],[-0.097816,-0.031152],[2.341734,-9.376527],[4.737163,9.064976],[5.632341,-8.301878],[7.514431,9.586621],[-8.125351,-5.567829],[-3.866018,0.347644],[-3.911200,1.504181],[-4.585275,9.502505],[-9.945958,4.298145],[3.694409,-6.522146],[1.963965,-2.623754],[-9.355473,7.088197],[-2.915842,1.779097],[-6.455874,3.062889],[4.697332,8.541667],[6.930206,-2.752849],[5.485386,8.433466],[-0.723765,0.122112],[8.343099,-0.808611],[6.174233,-3.891824],[5.995076,5.645852],[-3.957802,7.795877],[5.850869,5.166502],[4.925988,-7.813880],[6.807731,5.689774],[0.234573,8.603982],[0.904306,-3.140447],[7.145379,-9.689339],[-5.253025,-3.034476],[7.551469,6.285407],[2.903389,0.598883],[-4.797303,7.133582],[5.789036,3.690282],[8.636915,5.606324],[4.737855,-8.440700],[5.384816,1.353080],[-8.171469,-8.193695],[2.285091,-1.782132],[6.119368,-5.525157],[8.391556,9.649132],[-2.236058,-1.636550],[-4.091687,-5.012313],[9.825719,-0.499641],[-3.171174,8.881474],[-6.545030,-2.058671],[3.665921,-7.555055],[-3.891784,-4.249025],[-1.243227,-1.204548],[-1.724375,-3.793648],[6.274684,-9.172963],[1.259341,0.430170],[5.819266,-3.578513],[-4.021388,4.536171],[4.961884,-0.827275],[-8.209047,-8.108990],[7.871767,-1.672579],[2.542559,-1.856342],[3.201871,6.131465],[1.525712,-2.398062],[5.624181,-6.344393],[5.035246,0.548916],[4.295814,-2.290398]], dtype = "float32")#candidate|8168|(108, 2)|const|float32
var_8169 = relay.var("var_8169", dtype = "float32", shape = (20, 180))#candidate|8169|(20, 180)|var|float32
var_8170 = relay.var("var_8170", dtype = "int8", shape = (5, 90))#candidate|8170|(5, 90)|var|int8
call_8167 = relay.TupleGetItem(func_1628_call(relay.reshape(const_8168.astype('float32'), [216,]), relay.reshape(var_8169.astype('float32'), [3600,]), relay.reshape(var_8170.astype('int8'), [450,]), ), 4)
call_8171 = relay.TupleGetItem(func_1633_call(relay.reshape(const_8168.astype('float32'), [216,]), relay.reshape(var_8169.astype('float32'), [3600,]), relay.reshape(var_8170.astype('int8'), [450,]), ), 4)
func_6968_call = mod.get_global_var('func_6968')
func_6970_call = mutated_mod.get_global_var('func_6970')
call_8184 = relay.TupleGetItem(func_6968_call(relay.reshape(var_8170.astype('int8'), [450,])), 1)
call_8185 = relay.TupleGetItem(func_6970_call(relay.reshape(var_8170.astype('int8'), [450,])), 1)
uop_8186 = relay.sqrt(var_8169.astype('float64')) # shape=(20, 180)
output = relay.Tuple([call_8159,call_8161,call_8163,call_8167,const_8168,var_8170,call_8184,uop_8186,])
output2 = relay.Tuple([call_8160,call_8162,call_8164,call_8171,const_8168,var_8170,call_8185,uop_8186,])
func_8199 = relay.Function([var_8169,var_8170,], output)
mod['func_8199'] = func_8199
mod = relay.transform.InferType()(mod)
mutated_mod['func_8199'] = func_8199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8199_call = mutated_mod.get_global_var('func_8199')
var_8201 = relay.var("var_8201", dtype = "float32", shape = (20, 180))#candidate|8201|(20, 180)|var|float32
var_8202 = relay.var("var_8202", dtype = "int8", shape = (5, 90))#candidate|8202|(5, 90)|var|int8
call_8200 = func_8199_call(var_8201,var_8202,)
output = call_8200
func_8203 = relay.Function([var_8201,var_8202,], output)
mutated_mod['func_8203'] = func_8203
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1095_call = mod.get_global_var('func_1095')
func_1097_call = mutated_mod.get_global_var('func_1097')
call_8205 = relay.TupleGetItem(func_1095_call(), 2)
call_8206 = relay.TupleGetItem(func_1097_call(), 2)
func_4970_call = mod.get_global_var('func_4970')
func_4971_call = mutated_mod.get_global_var('func_4971')
call_8213 = relay.TupleGetItem(func_4970_call(), 0)
call_8214 = relay.TupleGetItem(func_4971_call(), 0)
func_2109_call = mod.get_global_var('func_2109')
func_2112_call = mutated_mod.get_global_var('func_2112')
const_8216 = relay.const([5.418007,6.186670,-2.729001,-0.513953,3.376517,-0.244472,-6.095056,-7.553049,1.473450,6.905257,-4.547676,-7.120592,-6.657705,-9.285649,-0.064523,-1.991008,8.307319,5.472898,-4.847816,-0.619573,4.369548,3.573144,5.021338,4.464328,-6.655654,-1.113019,-5.793605,7.012431,-7.925215,-7.208275,6.970528,-5.344922,3.974876,-1.199242,-1.834325,2.961647,4.722858,0.537621,-7.099140,2.976159,6.691620,8.143870,-5.470709,3.364387,-9.458228,-1.672351,-5.399938,-7.377798,-1.765015,4.420075,8.429555,-7.822311,-4.474033,-5.202527,-3.563301,9.601308,8.197887,5.163506,-4.182049,-0.923697,8.939735,-0.033464,-8.301882,1.893669,-6.091329,7.779859,3.893469,-0.275073,1.541867,-8.114946,3.649708,4.588289,9.315063,-9.062667,2.215194,-5.490793,6.547939,7.167472,-6.523391,-5.788790,4.432415,-6.176865,7.541348,-3.363516,3.363924,0.071159,7.800266,4.390480,3.413163,-6.191461,7.669699,5.238188,2.134766,-2.444385,9.561285,-0.652342,-5.769151,4.549871,-0.636817,-8.960906,8.611684,-1.461928,-1.233537,0.740672,5.462446,2.473045,-2.733078,-0.610252,5.251353,5.067981,9.994895,3.239791,4.570723,-9.386467,4.346577,3.027945,-4.638989,0.989168,-9.803089,-2.486081,-2.688188,-9.281380,9.459404,-5.581398,5.045274,3.843433,-3.516106,-3.927687,-5.882848,2.722298,8.082213,-3.786356,-9.546893,-2.152156,-5.074956,-7.834885,-3.029237,1.597068,1.419719,-4.676765,-1.679237,-7.988424,7.728575,-1.314776,2.007343,4.490476,-0.984394,-4.560907,0.793738,0.972601,6.092727,-0.327141,-1.561895,6.123455,4.658170,-7.572135,-0.341630,-6.287181,2.213607,7.626458,-8.470662,9.626174,-1.766330,1.464467,9.269558,1.179096,1.301056,-9.916742,5.528472,9.372520,-6.047652,-6.030970,-5.236801,-1.987378,1.980300,-5.867851,-6.557946,9.434145,1.412615,-0.091576,3.239406,-8.843205,3.455334,0.263431,-8.191786,4.201296,-9.813104,0.760109,8.383268,6.003187,1.323680,-6.580409,1.545281,-9.096610,0.570838,4.419066,-2.129321,3.911988,6.969937,4.737537,0.348444,-1.915763,-1.372138,5.361844,6.603096,0.583335,-7.970127,-7.677433,7.342447,9.479156,0.509646,3.584428,-2.874640,6.695704,0.704381,7.008452,4.952093,5.661828,-0.558203,7.073017,7.209342,-5.433693,8.072354,5.622959,-8.364637], dtype = "float32")#candidate|8216|(225,)|const|float32
call_8215 = relay.TupleGetItem(func_2109_call(relay.reshape(const_8216.astype('float32'), [225,])), 0)
call_8217 = relay.TupleGetItem(func_2112_call(relay.reshape(const_8216.astype('float32'), [225,])), 0)
output = relay.Tuple([call_8205,call_8213,call_8215,const_8216,])
output2 = relay.Tuple([call_8206,call_8214,call_8217,const_8216,])
func_8218 = relay.Function([], output)
mod['func_8218'] = func_8218
mod = relay.transform.InferType()(mod)
output = func_8218()
func_8219 = relay.Function([], output)
mutated_mod['func_8219'] = func_8219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1778_call = mod.get_global_var('func_1778')
func_1780_call = mutated_mod.get_global_var('func_1780')
call_8236 = relay.TupleGetItem(func_1778_call(), 1)
call_8237 = relay.TupleGetItem(func_1780_call(), 1)
output = relay.Tuple([call_8236,])
output2 = relay.Tuple([call_8237,])
func_8238 = relay.Function([], output)
mod['func_8238'] = func_8238
mod = relay.transform.InferType()(mod)
mutated_mod['func_8238'] = func_8238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8238_call = mutated_mod.get_global_var('func_8238')
call_8239 = func_8238_call()
output = call_8239
func_8240 = relay.Function([], output)
mutated_mod['func_8240'] = func_8240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4188_call = mod.get_global_var('func_4188')
func_4189_call = mutated_mod.get_global_var('func_4189')
call_8302 = relay.TupleGetItem(func_4188_call(), 1)
call_8303 = relay.TupleGetItem(func_4189_call(), 1)
func_2854_call = mod.get_global_var('func_2854')
func_2857_call = mutated_mod.get_global_var('func_2857')
const_8310 = relay.const([-8,-4,-9,2,1,-3,1,-7,-4,4,1,10,-6,6,-3,-1,-7,7,-3,-5,10,-3,9,-4,6,3,-3,-5,-3,8,-2,-6,-6,-7,1,-3,10,-4,7,4,-5,3,1,6,7,-10,4,7,7,9,6,1,-10,-6,2,-2,-6,-4,3,9,-5,-10,-4,-9,1,-9,1,-4,4,10,8,4,9,1,9,1,-8,2,-9,3,10,8,3,-2,10,4,6,-3,7,6,-5,-9,-9,7,4,8,3,3,8,4,9,-7,7,7,-4,-9,1,2,-8,8,8,-4,-1,-10,4,6,-3,8,3,-3,10,5,-9,-1,-5,-9,-6,5,-1,8,-8,-1,-9,2,-4,-10,6,-6,-2,4,-8,10,7,1,10,-5,6,-1,5,-9,-8,-3,-4,-1,-8,4,5,9,-9,10,-2,8,-3,4,-2,-8,2,7,2,10,3,5,-8,-2,5,-6,8,-4,5,-10,-3,-9,2,8,-6,-4,-4,6,1,9,-1,4,1,2,-8,-4,3,-5,-3,-6,3,7,9,1,3,-8,9,6,10,7,-2,-8,-8,9,5,-10,7,10,-3,8,3,10,9,-1,6,6,10,-5,8,10,1,-6,7,6,8,-4,1,-2,-4,7,4,-9,1,3,-8,-5,-10,7,8,5,-7,-5,-7,-7,4,2,-9,-2,-5,-2,-7,9,-1,-7,10,-2,-3,3,8,4,6,-1,4,-7,-8,1,-9,5,9,-8,-3,5,-7,-9,-10,6,6,-3,1,-1,-3,6,-3,2,2,10,-10,5,-5,2,-7,1,8,-6,-6,-9,9,10,8,-1,-4,10,-6,-1,9,-6,6,2,3,-4,-4,7,10,-5,-1,-3,-9,-9,7,-8,5,-5,-3,-6,4,7,-3,-3,-2,-5,9,8,-10,5,-6,6,-8,2,-5,-10,-6,-8,9,-6,-2,-4,9,-10,-8,8,9,3,4,-1,-4,9,7,-3,-1,-9,-1,5,-6,1,-8,-6,-5,-6,-6,10,-7,-4,-8,-3,7,1,7,-8,-9,-7,-9,5,3,3,-8,1,-3,10,-3,10,4,-6,7,4,-2,-6,3,5,5,-7,-4,-8,5,-6,-10,-8,10,-7,-7,-5,-3,2,-4,-6,-8,2,3,-6,-10,9,-1,-8,1,7,8,9,-3,-9,-9,-8,8,-6,1,-3,6,-3,-9,7,-6,-9], dtype = "int8")#candidate|8310|(450,)|const|int8
call_8309 = relay.TupleGetItem(func_2854_call(relay.reshape(const_8310.astype('int8'), [5, 10, 9])), 0)
call_8311 = relay.TupleGetItem(func_2857_call(relay.reshape(const_8310.astype('int8'), [5, 10, 9])), 0)
func_2056_call = mod.get_global_var('func_2056')
func_2061_call = mutated_mod.get_global_var('func_2061')
var_8313 = relay.var("var_8313", dtype = "float32", shape = (36, 6))#candidate|8313|(36, 6)|var|float32
var_8314 = relay.var("var_8314", dtype = "float32", shape = (3600,))#candidate|8314|(3600,)|var|float32
call_8312 = relay.TupleGetItem(func_2056_call(relay.reshape(var_8313.astype('float32'), [216,]), relay.reshape(var_8314.astype('float32'), [10, 360]), relay.reshape(call_8309.astype('int8'), [5, 90]), ), 2)
call_8315 = relay.TupleGetItem(func_2061_call(relay.reshape(var_8313.astype('float32'), [216,]), relay.reshape(var_8314.astype('float32'), [10, 360]), relay.reshape(call_8309.astype('int8'), [5, 90]), ), 2)
func_675_call = mod.get_global_var('func_675')
func_677_call = mutated_mod.get_global_var('func_677')
call_8316 = func_675_call()
call_8317 = func_675_call()
output = relay.Tuple([call_8302,call_8309,const_8310,call_8312,var_8313,var_8314,call_8316,])
output2 = relay.Tuple([call_8303,call_8311,const_8310,call_8315,var_8313,var_8314,call_8317,])
func_8319 = relay.Function([var_8313,var_8314,], output)
mod['func_8319'] = func_8319
mod = relay.transform.InferType()(mod)
mutated_mod['func_8319'] = func_8319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8319_call = mutated_mod.get_global_var('func_8319')
var_8321 = relay.var("var_8321", dtype = "float32", shape = (36, 6))#candidate|8321|(36, 6)|var|float32
var_8322 = relay.var("var_8322", dtype = "float32", shape = (3600,))#candidate|8322|(3600,)|var|float32
call_8320 = func_8319_call(var_8321,var_8322,)
output = call_8320
func_8323 = relay.Function([var_8321,var_8322,], output)
mutated_mod['func_8323'] = func_8323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7039_call = mod.get_global_var('func_7039')
func_7041_call = mutated_mod.get_global_var('func_7041')
call_8344 = func_7039_call()
call_8345 = func_7039_call()
uop_8349 = relay.sinh(call_8344.astype('float32')) # shape=(5, 10, 9)
uop_8351 = relay.sinh(call_8345.astype('float32')) # shape=(5, 10, 9)
output = uop_8349
output2 = uop_8351
func_8354 = relay.Function([], output)
mod['func_8354'] = func_8354
mod = relay.transform.InferType()(mod)
output = func_8354()
func_8355 = relay.Function([], output)
mutated_mod['func_8355'] = func_8355
mutated_mod = relay.transform.InferType()(mutated_mod)
func_753_call = mod.get_global_var('func_753')
func_755_call = mutated_mod.get_global_var('func_755')
call_8371 = func_753_call()
call_8372 = func_753_call()
output = call_8371
output2 = call_8372
func_8377 = relay.Function([], output)
mod['func_8377'] = func_8377
mod = relay.transform.InferType()(mod)
output = func_8377()
func_8378 = relay.Function([], output)
mutated_mod['func_8378'] = func_8378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4219_call = mod.get_global_var('func_4219')
func_4221_call = mutated_mod.get_global_var('func_4221')
call_8437 = relay.TupleGetItem(func_4219_call(), 3)
call_8438 = relay.TupleGetItem(func_4221_call(), 3)
output = relay.Tuple([call_8437,])
output2 = relay.Tuple([call_8438,])
func_8454 = relay.Function([], output)
mod['func_8454'] = func_8454
mod = relay.transform.InferType()(mod)
output = func_8454()
func_8455 = relay.Function([], output)
mutated_mod['func_8455'] = func_8455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4363_call = mod.get_global_var('func_4363')
func_4365_call = mutated_mod.get_global_var('func_4365')
call_8466 = func_4363_call()
call_8467 = func_4363_call()
output = call_8466
output2 = call_8467
func_8477 = relay.Function([], output)
mod['func_8477'] = func_8477
mod = relay.transform.InferType()(mod)
output = func_8477()
func_8478 = relay.Function([], output)
mutated_mod['func_8478'] = func_8478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8218_call = mod.get_global_var('func_8218')
func_8219_call = mutated_mod.get_global_var('func_8219')
call_8482 = relay.TupleGetItem(func_8218_call(), 1)
call_8483 = relay.TupleGetItem(func_8219_call(), 1)
func_6904_call = mod.get_global_var('func_6904')
func_6906_call = mutated_mod.get_global_var('func_6906')
call_8495 = relay.TupleGetItem(func_6904_call(), 1)
call_8496 = relay.TupleGetItem(func_6906_call(), 1)
func_5236_call = mod.get_global_var('func_5236')
func_5239_call = mutated_mod.get_global_var('func_5239')
const_8508 = relay.const([[4,8,-3,-5,2,-7,-2,-7,4,5,1,-9,-9,6,-6,9,8,-1,-2,5,-6,2,-5,-3,2,1,7,6,-2,9,1,-7,-9,9,-7,-7,7,10,-8,-4,-10,-6,7,-4,-4],[-5,5,5,-4,-5,-1,5,4,3,-8,-4,4,-7,10,9,6,-9,8,5,10,-5,4,10,-7,2,2,6,-4,6,-4,-9,9,-3,4,10,-10,5,-9,4,10,1,-9,-5,-2,8],[5,8,5,-2,-9,-3,9,5,-4,4,-4,-5,4,8,2,1,5,-1,1,1,8,-1,3,7,-4,3,-7,-10,8,-8,6,-8,-3,1,-4,5,8,1,3,-1,10,-4,-4,-2,6],[3,-1,3,1,7,-8,-9,10,8,-9,-2,-6,-8,3,-1,9,-3,6,-6,3,4,10,10,5,-5,8,5,-4,-2,-2,7,10,4,7,-5,-5,-4,6,7,1,-8,-7,-2,-6,1],[-1,1,-10,9,7,2,7,-9,7,4,5,-8,7,-7,-8,10,7,-3,6,-8,6,-5,3,5,7,9,-3,8,9,-2,-2,-6,-6,9,9,-5,5,-9,5,2,3,-5,10,-6,-9],[-6,3,-1,1,10,-7,-6,-8,-5,-10,4,8,-2,5,7,-8,-6,-5,9,6,5,-6,-8,-7,-7,9,2,3,8,-4,3,-8,-1,5,-8,-1,6,5,2,-8,8,-2,-5,-6,4],[-7,-10,-7,7,-2,5,-7,3,-7,-3,3,4,-4,10,-1,-10,3,-5,-2,10,-9,-9,8,-8,6,9,7,-5,-2,2,9,-6,-3,-3,-5,-1,8,1,-4,10,-2,-9,4,-9,1],[4,5,-2,-10,3,8,10,-6,3,-1,7,-3,4,2,-6,9,3,-9,-10,10,6,7,-5,6,10,2,-5,-6,4,6,-3,9,7,-10,9,-10,1,9,-10,-5,-6,-8,4,2,5],[10,-3,3,9,8,-7,-10,-6,6,8,6,10,7,-1,-4,10,-4,2,-4,-3,8,-1,-8,-1,-4,-8,5,8,2,4,6,9,-5,-7,2,1,2,10,10,-6,2,-9,-10,8,4],[7,4,-2,-8,9,-1,-2,4,-2,-3,3,10,2,-6,-3,2,2,7,8,3,5,-10,8,9,10,-8,-9,2,-2,2,1,-7,-4,9,10,-1,-7,-2,-5,-4,-4,8,5,-3,-10]], dtype = "int8")#candidate|8508|(10, 45)|const|int8
call_8507 = relay.TupleGetItem(func_5236_call(relay.reshape(const_8508.astype('int8'), [450,])), 0)
call_8509 = relay.TupleGetItem(func_5239_call(relay.reshape(const_8508.astype('int8'), [450,])), 0)
var_8513 = relay.var("var_8513", dtype = "int8", shape = (10, 45))#candidate|8513|(10, 45)|var|int8
bop_8514 = relay.add(const_8508.astype('uint16'), relay.reshape(var_8513.astype('uint16'), relay.shape_of(const_8508))) # shape=(10, 45)
output = relay.Tuple([call_8482,call_8495,call_8507,bop_8514,])
output2 = relay.Tuple([call_8483,call_8496,call_8509,bop_8514,])
func_8517 = relay.Function([var_8513,], output)
mod['func_8517'] = func_8517
mod = relay.transform.InferType()(mod)
mutated_mod['func_8517'] = func_8517
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8518 = relay.var("var_8518", dtype = "int8", shape = (10, 45))#candidate|8518|(10, 45)|var|int8
func_8517_call = mutated_mod.get_global_var('func_8517')
call_8519 = func_8517_call(var_8518)
output = call_8519
func_8520 = relay.Function([var_8518], output)
mutated_mod['func_8520'] = func_8520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4970_call = mod.get_global_var('func_4970')
func_4971_call = mutated_mod.get_global_var('func_4971')
call_8557 = relay.TupleGetItem(func_4970_call(), 0)
call_8558 = relay.TupleGetItem(func_4971_call(), 0)
func_5849_call = mod.get_global_var('func_5849')
func_5851_call = mutated_mod.get_global_var('func_5851')
call_8560 = func_5849_call(relay.reshape(call_8557.astype('float32'), [2, 7, 1]))
call_8561 = func_5849_call(relay.reshape(call_8557.astype('float32'), [2, 7, 1]))
func_8319_call = mod.get_global_var('func_8319')
func_8323_call = mutated_mod.get_global_var('func_8323')
var_8563 = relay.var("var_8563", dtype = "float32", shape = (216,))#candidate|8563|(216,)|var|float32
const_8564 = relay.const([[-8.633756,5.100563,-2.093006,-4.995274,7.116858,6.739188,-1.273776,-0.174178,7.917198,-8.015892,3.004684,-6.660768,-7.497596,-8.566512,3.895687,3.967274,2.166662,-0.204456,-5.487961,-0.957847,2.922609,-5.246679,-8.696058,-1.468666,8.877435,8.996377,-3.697241,3.917853,5.728197,6.239039,3.486915,-1.549030,-8.672903,-7.521959,9.235763,-3.772308,9.149299,4.320591,3.390656,7.707237,-5.849701,6.445366,-8.221640,7.642621,-4.207227,-4.138593,3.817999,5.872301,-0.134866,-5.239094,-8.343650,-4.048208,7.361733,-6.780856,-7.804592,1.172674,-5.571658,8.418670,2.116521,4.861872,2.371888,-0.681714,-8.517698,-0.634173,1.710053,7.379971,7.758870,4.390772,9.351112,8.508230,0.700630,-1.122892,0.116454,-9.939894,-9.319019,2.694597,-8.562663,-4.512855,1.945210,2.199591,5.301913,-3.546930,-8.776983,0.998715,7.714344,4.672296,9.559943,1.089823,5.084594,-0.152905,8.723533,-0.523056,1.690818,-0.286202,7.180650,2.599056,-6.532009,-7.565843,-0.458077,-3.781978,-4.155353,-0.559317,7.340854,1.155097,-4.033339,-7.573405,8.079828,9.086924,0.324439,6.574032,4.216472,0.260841,-0.494596,-2.293431,5.658181,6.184618,3.148970,-5.200512,7.422909,5.949859,7.878828,1.940068,-1.503531,5.424658,-1.402960,1.724355,9.730198,-1.496240,-1.355213,-8.076524,5.256224,3.774666,-7.051321,-7.947002,5.632053,4.060458,5.556962,5.043932,8.687291,-2.222000,3.992157,7.630557,-5.582937,4.954107,-3.112675,4.524134,2.535819,-6.847765,-4.781231,2.076787,0.203188,-0.242038,9.435954,-6.600922,-1.603135,-1.735951,-2.216218,-9.186125,1.726780,1.992447,-7.951043,-7.667777,-5.146451,4.880562,3.421249,-5.791879,0.493533,6.195543,4.788246,4.139382,-0.835786,1.205275,8.693497,-0.086805,4.764087,-0.902838,-0.284363,8.985398,-4.698568,0.208555,9.059159,-6.375032,-6.979610,6.600314,7.740280,0.182804,6.902500,6.959560,-7.206223,5.519160,2.215232,8.527262,-8.733605,-9.426329,9.597289,-4.147136,-8.705897,0.225594,1.459972,-8.792834,5.071431,-2.084862,-4.512146,2.696803,7.751412,3.333940,5.972258,-3.302359,3.683430,-4.293155,-7.413129,-5.114767,3.348493,2.903099,-9.535614,1.608352,1.160713,-7.489112,0.097493,5.927088,1.904549,-3.373146,6.236847,-8.281937,3.027982,-9.847832,-3.584697,-8.511289,-3.218436,-2.015552,9.756647,8.900905,4.713815,0.520173,9.456107,-9.689741,9.047531,7.798050,3.796225,2.215996,-5.711939,5.643052,-2.361067,-3.879709,9.467229,-9.017773,5.880171,-2.268575,7.721133,9.850180,-0.967656,9.421554,-0.549584,-0.505459,5.362183,7.104051,9.255711,-8.027039,-5.415102,5.129181,6.226531,8.032435,9.360648,1.372670,1.140130,3.837470,-8.745078,6.285719,-5.972231,5.229272,4.459239,8.781508,6.011011,5.819764,5.228649,3.762951,-9.477318,6.454365,-8.856267,-3.113163,0.750272,0.624008,5.257238,3.163071,4.808637,2.668352,5.396196,4.344315,-3.511874,-4.021277,7.443348,-5.071229,-5.900187,2.326003,-6.686597,-8.241613,-1.123192,-8.837597,-9.738139,7.837111,-7.040470,8.243890,4.650774,-5.932772,4.143189,9.674941,-3.685281,-5.416398,6.860157,-7.542979,7.477297,-0.965145,-4.684058,8.189669,-0.471365,-9.958601,1.286743,-0.889879,5.857565,-0.778169,6.748344,4.104001,6.649620,3.718344,-4.383916,1.632373,-4.177769,1.140996,-0.687182,-9.553064,1.359290,1.959241,-4.321657,4.734329,-7.125717,-5.679115,-8.639324,3.889381,8.655585,-3.685549,-4.289412,0.601593,0.460943,-3.542682,-1.572684,-4.957928,7.811899,-0.336793,1.009625,4.760159,-3.186262,-6.579942,-8.079881,-5.066959,-2.990644,0.010431,-3.506420,6.079704,8.544192,2.904978,-4.902615,2.762361,2.992763,3.865097,2.686317,-1.114967,-1.205298,-6.372609,9.502182,-6.704053,-5.297578,-1.216905,3.521371,-2.531696,6.954617,-8.864228,-0.113525,-1.501611,6.883916,-2.531455,-9.072898,-4.748694,1.044036,0.602049,-1.607014,-2.316776,5.419514,2.677691,6.075639,5.050858,-2.000405,-1.793305,1.760436,-6.882945,1.704960,-9.984068,-3.694231,-4.132004,3.262689,-6.157008,-8.691036,-8.934541,2.266261,-7.248486,-4.304293,-0.525438,4.863987,3.756201,9.419284,6.065160,-1.192392,-3.037474,9.612043,1.477640,1.301659,-6.492495,-7.815466,2.179956,-6.301242,-7.604753,-8.009561,6.680514,-2.503474,-0.122004,9.017915,-9.265168,6.798558,-8.037155,2.204812,-1.733081,2.013742,-8.707793,5.465220,3.644295,2.974946,-8.342277,-3.223278,7.507701,-5.512783,-6.739059,-0.736796,-7.204925,-4.787473,-0.873671,-3.029654,-0.353663,5.625321,6.360038,-0.044508,-5.359695,5.117270,7.905046,2.881576,-8.707620,3.697065,8.371147,3.883068,7.414398,-8.531345,4.891448,-9.742693,-7.520888,8.367441,7.187897,-7.842790,6.565556,-5.752240,-2.479473,-8.222492,-0.501785,3.406180,8.560252,2.420325,-7.754595,-0.004898,-4.650435,8.146643,-7.773289,-1.139944,8.792812,0.882950,-1.992522,8.864985,0.758156,0.911046,9.532092,4.179388,9.264219,-2.453009,-8.558085,-1.357150,0.062046,8.610208,-9.727469,7.903204,6.257690,-2.993035,9.151441,-2.185489,1.002230,-5.785913,-2.747985,2.553937,-9.734181,-9.639347,-7.270134,6.583184,-8.759285,9.632266,-9.337171,-1.821100,-5.540136,-0.715632,8.592545,-0.260925,-7.847642,8.772454,7.983230,8.257858,-2.041791,-5.083094,-5.408279,9.138311,2.318689,6.088083,7.311010,9.427982,-2.966114,9.322521,-8.319689,6.056506,-2.489429,9.149712,6.484352,9.411659,-0.512426,8.570767,6.705140,-7.273583,9.633751,2.046086,7.699733,-4.672608,-5.159739,7.427135,-3.455801,9.438440,-2.513112,-2.807920,4.528556,4.757597,7.254229,-2.487834,3.298902,0.379338,-2.403220,-8.174721,0.990560,-2.122837,-4.528239,-0.222528,-2.058322,-9.184497,0.709752,-4.749694,-8.565654,-2.105671,-5.516363,8.964320,0.060298,1.730136,2.391648,-9.121771,-6.980348,-0.827831,-5.441386,6.118172,-4.064413,6.130518,-6.284254,1.762199,-8.744720,7.697713,-6.084690,-1.586330,7.124367,-0.936100,2.157033,-3.016088,7.308581,6.836497,1.519787,-7.154085,-4.588476,1.102655,9.881386,2.984100,2.769996,4.333454,6.677836,5.805313,7.680009,1.419931,-7.949909,-4.466706,-2.836782,-5.181080,9.015033,-0.572306,-5.770215,-5.521221,-9.531064,4.113820,-6.673215,4.541042,4.501344,3.645642,-9.790441,7.008963,-5.036912,-2.843053,4.695329,-8.452100,1.015730,-1.458531,4.990156,-1.263242,2.901259,0.839412,-3.077019,8.867326,6.694508,-7.192977,-8.613787,8.464604,8.881254,0.909733,-0.776139,4.305684,-8.961655,2.589132,8.227527,6.718533,-2.484415,-2.563427,-6.599571,-8.001841,-6.803961,4.285164,-6.063973,0.177057,1.815454,3.092396,6.472590,1.724117,-1.840017,3.449540,-9.087151,-2.168160,0.103256,2.948653,1.167884,6.537520,-9.949328,-0.689336,6.775211,2.078966,-3.782783,-7.182812,3.075566,-0.442979,1.183262,9.501029,-5.566833,-2.895314,5.593410,8.074541,1.681106,-6.375367,-8.920067,-2.737423,8.322646,-5.998452,-8.810347,9.538243,-6.411494,-2.017408,7.303791,-6.880123,8.600742,2.889759,-3.223541,4.476211,6.845252,-2.697795,-1.352805,-9.825222,-7.093920,-2.020301,0.732088,-9.768865,4.227255,0.275013,9.813572,-7.454332,-9.581423,1.111994,8.062497,-0.477926,-9.357545,-1.873885,-7.301183,-3.193024,9.458862,7.149623,-3.177683,-4.384025,-5.200022,-6.599198,2.133277,0.207820,-4.148234,4.099989,4.126801,4.201336,-6.666422,3.541845,-2.870039,3.243506,-6.329215,-1.212737,-8.115908,-2.197467,6.734464,-1.348025,7.425336,-0.897677,-8.419106,5.262187,-2.502676,-8.543675,-7.268222,4.238202,4.322567,-7.197572,9.626699,6.762803,-6.472810,1.443004,-0.889655,-1.605621,5.838755,-8.175398,-4.217255,3.341284,-0.989318,3.635661,6.185127,4.464185,8.345714,-2.021392,-0.986087,2.942352,9.921891,-5.022311,-7.123140,-3.939337,-6.043656,-6.714090,-9.486208,2.068827,5.398423,-4.637571,5.608859,4.501662,8.702128,4.101353,0.632687,-4.721762,2.209289,0.365852,-2.474302,1.419777,-8.203973,6.404735,-6.390906,5.261252,-1.840156,-1.888319,6.668177,-3.151401,-2.356455,-1.673275,-2.282034,-8.256131,-0.521654,-8.955915,3.902833,6.427779,8.008115,0.114273,3.944758,6.461424,-7.037820,5.339703,2.480746,-6.771390,3.679535,-2.858907,-4.039693,-9.397355,-4.047223,4.721498,-7.846171,3.601706,3.820470,5.645821,7.383568,-0.858891,4.367503,4.048515,-9.856699,-5.617274,-5.377495,0.860731,8.992936,4.227114,-6.234920,-3.347876,3.474259,-2.641746,-2.744462,2.037003,-6.737584,7.901146,6.578737,8.501376,-4.774168,-4.483692,-7.004870,7.429244,3.533356,6.365982,4.562108,-1.212760,8.361279,-8.442061,5.979309,7.248826,5.911964,7.798408,9.101866,-0.645006,-6.401782,-3.034096,6.111345,-6.666820,2.959576,-3.288470,2.568160,4.887739,-0.407094,-1.720154,-2.655482,5.027893,-3.616125,-4.537273,9.504146,-5.641916,8.954668,-3.148608,-3.347014,9.180007,-9.216156,7.209888,0.069258,-4.918413,-1.499882,7.614704,-9.581314,-6.236611,5.054589,-4.693839,-2.496505,-1.266690,-0.313571,-7.689217,1.582673,-9.296441,8.322432,-5.003510,-3.097927,-8.330537,8.319258,7.366895,5.639819,4.577333,6.167535,2.342369,-9.660468,6.757312,9.065817,2.548130,-0.146125,-6.082391,0.581770,-5.580525,-0.619513,-2.143342,-0.660160,4.130309,-8.488485,-4.776309,5.136066,8.367085,9.815498,-1.652798,-3.749791,2.011030,3.815975,-4.548222,-2.845879,-5.314244,-5.662694,3.204557,8.735081,-7.951220,7.741456,2.565040,-2.433518,-4.868475,5.845599,-7.079288,-0.346688,-3.947640,-3.245994,8.619723,2.619558,6.089733,-2.630020,-4.903555,7.737195,5.740397,1.637026,1.816294,4.683603,8.235850,-4.862013,-4.018474,-3.780907,-6.918163,-0.719399,6.688346,-6.343147,6.925061,5.732319,-0.790271,-0.920602,5.016269,-3.928579,5.556130,-5.955174,-5.590965,4.197009,-2.708928,-3.009148,-9.303441,-3.718968,-3.770204,-6.958366,9.147582,-7.991703,-7.444746,-5.829424,-5.862856,2.340110,-0.887224,1.382032,-2.413997,-2.502505,-6.671191,-5.008096,4.412006,-7.699507,6.975126,8.201069,5.182173,-8.151822,-4.663328,7.181404,6.991346,-3.755268,1.727381,-9.817755,-0.948675,-3.339649,9.773485,2.171031,9.881237,1.385952,-7.826542,8.483697,-4.003278,-4.424144,-5.219384,0.302864,-4.361743,-4.248106,9.277616,3.704405,0.478747,-3.188495,-5.978497,3.904756,-5.774248,-5.494917,2.573932,-7.779925,3.995240,-2.218081,-2.081970,3.311904,5.604394,-5.752892,0.928749,5.916659,0.154424,0.641092,4.086407,6.339693,0.440410,3.556711,-2.710795,-2.824805,-9.089470,0.197650,5.658641,5.289947,-1.391458,8.184760,4.845666,-3.807952,4.441933,0.422554,-1.772030,-6.118666,-7.797709,-7.157035,6.238254,5.616206,5.724792,-9.382030,7.073698,-5.259694,-8.568044,1.277056,-3.384444,-0.953502,-0.460637,-7.184892,2.174419,-1.556489,-3.127314,-9.567274,-1.265612,9.158330,-4.320096,-9.209340,2.280938,-4.039044,-3.057567,-8.118862,8.061261,-4.479188,-8.148168,7.309317,4.677310,9.582446,-8.909419,3.743500,7.852467,3.107048,3.551078,-1.018977,-9.968680,-8.434193,-0.458265,1.134557,1.629218,7.785688,-2.723503,2.166811,8.873485,-2.944638,-6.876957,-8.808814,-0.276013,-3.410485,1.791794,0.756851,8.709706,-3.333254,-0.989556,1.460367,-7.183592,6.955894,8.690027,-8.500566,7.344966,5.840429,4.043887,-4.311580,0.319017,5.083595,4.491097,-8.266605,-9.555357,-9.315098,-7.886959,-9.265779,2.764818,6.391508,3.274359,4.796064,-6.660997,-7.319235,-4.863975,-9.679255,2.729593,-7.203478,-6.461534,2.506034,9.138321,7.575099,-0.473726,-9.802388,6.757891,-2.476284,-9.152309,6.066511,-3.820289,-6.162156,-1.349713,-2.644087,-0.404179,-0.055210,0.780083,4.309189,-9.096844,-0.635053,-7.208323,-5.368638,7.038177,-6.427095,-1.765200,-9.765308,-1.176063,6.243653,7.486605,-9.890421,-3.083065,-5.301329,3.722073,-1.471823,-9.533973,-7.105272,-9.033756,-3.509033,7.920433,2.554977,0.267406,5.204074,-5.134774,-7.555884,-7.154974,7.684485,-8.748126,5.561098,6.762949,7.407822,-8.783746,-4.237566,-7.650467,-7.948395,-5.436502,6.204011,-9.622022,9.089862,3.208554,-7.411381,-8.612322,-8.230647,-7.107614,-3.939338,3.753070,4.868441,7.308582,-0.370806,0.206514,-9.088533,-0.814088,7.203960,-6.668423,3.152948,-7.262845,0.648933,9.718851,6.807858,2.868200,2.492504,3.445725,8.978255,3.647739,-6.200349,-9.846856,-0.365068,-2.694453,5.524608,-2.496784,-5.450222,2.587022,8.335731,1.854419,-6.447388,7.661243,-5.899036,-7.917596,6.612459,7.378455,-9.223985,-6.072385,8.408191,-6.862687,3.752986,9.585309,-2.020439,-1.664506,-8.539562,-9.738251,-5.774681,-6.352282,2.055718,-9.896813,-5.186995,-9.129170,-9.825505,9.784884,-7.659283,-7.238760,-1.644523,8.022970,-6.169316,0.542007,-5.510489,1.321846,1.571887,4.709481,8.093993,5.820093,5.650510,-1.940659,4.413793,3.873595,-1.863678,7.080976,-8.544890,4.946007,-4.382030,0.254905,-5.645252,-7.751195,-4.677821,-2.910735,1.869415,-1.322774,-4.791035,-7.203056,-0.295219,2.665504,-9.923146,-0.911208,6.297608,2.307694,-9.433449,-6.656411,-9.080762,-3.652237,-1.081654,-4.198948,-4.546165,7.009131,6.919209,-6.691720,2.021467,-3.017339,5.074284,-1.587245,-7.050464,-9.497239,-2.242203,-1.811788,1.112020,-6.075143,2.888961,-1.352812,7.268656,-4.228999,4.896469,-0.808204,-5.596027,-3.805477,1.435538,1.264813,6.572614,-1.449211,-2.544062,-4.221396,6.319315,-7.334755,7.022755,5.172537,-2.871998,0.254923,-4.856718,-9.000981,6.205678,-4.447984,-1.055974,-1.886311,-4.863517,7.540760,1.036542,-1.766852,-7.446046,-3.916668,9.330845,-5.327774,1.429975,-7.683126,-4.167079,8.653949,2.286808,-1.146025,7.867335,9.699178,-3.975972,-8.369530,-6.357883,-4.880442,2.195164,-3.079943,-4.032707,-6.166030,7.961999,-8.538050,-8.545513,8.574892,5.446757,6.073766,-9.067131,-3.960885,2.122544,0.015225,-7.601805,1.864911,-2.211130,-2.756967,-9.366469,-1.638356,0.475322,4.196597,-2.337978,-4.284400,3.205911,-6.561239,-0.503595,-5.352073,-8.351446,-2.473060,0.054259,-8.431414,6.113317,4.873997,-2.597248,2.598645,-4.371300,1.569586,8.543478,-8.951542,1.020710,9.569897,-7.862907,4.509481,8.587936,1.643259,7.966044,-5.977121,-3.339741,2.407719,7.421377,3.635284,2.923070,9.624141,-5.850760,4.912235,-5.792168,2.686380,-2.207170,7.970283,-8.351479,0.188396,4.858919,4.423476,9.249334,-2.911148,1.799647,-2.937233,-5.768898,-8.707157,9.863116,-0.943024,-0.847491,-1.081721,-6.913528,-7.783086,-3.386029,6.545008,1.277102,-5.871808,2.338268,7.691973,-6.793260,2.636058,6.134719,9.763294,-2.813490,0.460198,6.739202,6.664547,5.213768,0.732096,9.537668,8.632149,8.136004,6.378126,-8.403433,2.277954,-4.596106,0.727126,-4.480878,4.516216,-8.911753,5.236826,-0.447777,-6.976411,-1.683536,-4.455215,-4.646803,-9.759374,9.630542,-8.704585,2.581692,-4.525590,-4.618059,5.393538,-7.518186,4.091557,3.680906,-4.418164,-0.810376,-8.925577,-4.971564,-9.283082,-1.703451,-9.684257,6.005822,-4.145318,7.930015,-5.715134,-1.727436,-9.873113,-3.634405,-7.960884,3.369305,-8.953541,6.527522,-9.393002,9.170334,-5.085011,-7.943458,8.644283,8.355569,-2.563093,-8.403305,-9.320972,-8.799592,6.159005,6.782793,4.610030,-2.543796,-6.687694,-1.874047,-3.898581,0.090848,8.888229,7.629226,4.019992,-6.901639,6.520388,4.635392,-6.986771,6.185349,-1.958525,3.379687,2.399672,6.198139,1.795728,-9.106476,5.040950,-2.252018,3.329440,1.360094,-7.488202,-3.571660,-8.918958,9.453855,-8.829639,-5.662878,7.036725,-8.414782,-2.298555,-9.731414,6.329473,1.159779,7.814883,8.898931,9.487687,6.167934,2.607328,-1.587485,0.125051,-0.952442,-1.245123,5.564922,-2.967556,-7.657443,2.343906,-2.658771,6.329290,-3.938251,3.866266,-1.708295,-4.218160,-3.614414,1.588878,-3.438183,-9.540580,-4.265364,4.521349,6.610650,4.039459,-1.298001,-4.700959,7.552910,-4.012062,-9.810066,-2.837924,4.447009,3.247099,-1.603834,-8.294510,7.598846,7.012267,8.626892,1.459653,-1.374522,-2.398286,-3.264842,7.830564,-1.379182,7.331660,5.047288,8.532738,-4.840631,-2.590029,-1.265602,1.712995,6.650793,8.894976,-1.291467,2.212812,-0.059257,0.596396,7.765995,-8.742409,8.295576,-8.753973,6.433058,9.187933,-6.300606,-5.484035,-6.207537,4.607986,-6.337377,-5.057975,2.994773,5.956407,0.646948,-1.168215,7.067450,-5.733439,-9.931113,6.018457,9.140346,-3.642117,-7.079297,-8.173898,-4.747849,7.509515,-2.781667,2.128501,2.958358,2.665763,-4.656040,3.598110,0.063552,-7.277747,9.130819,4.774633,-9.352998,-5.988956,2.950698,2.513414,-3.187799,-4.845770,-8.627006,6.010405,8.166785,-1.436268,-2.712474,9.491067,7.398504,-3.711833,-1.289226,7.789820,4.373445,6.886867,-7.257675,-1.383820,0.790755,-9.949532,3.916610,-7.419170,-5.025367,-1.048221,-4.038445,-2.138736,1.000310,-2.234256,5.543976,-4.179688,-0.733239,1.776866,-7.347795,9.797620,-4.142435,9.174598,6.519845,-4.530559,-1.605932,3.984624,5.317397,-1.495789,-1.973896,-1.666152,9.201821,-1.653084,-4.647190,-5.784101,8.262087,8.941691,9.881022,2.473279,-7.131701,2.155608,-5.998754,6.517970,-9.537349,-0.696794,2.904002,-5.065267,0.952830,-4.438065,-8.130340,-6.202759,-1.085015,-5.681739,-1.547552,3.393472,8.328265,6.621375,1.634925,0.237193,8.924381,-6.277343,-6.974996,5.224040,2.568979,-0.629232,-3.180294,3.806802,-6.719850,7.521575,-0.110805,9.486212,4.045661,6.773487,4.362268,-6.839235,2.613875,2.888633,-8.013074,7.187845,-2.812458,8.261071,0.078061,-9.822762,-2.853265,-5.014044,-3.722904,3.954737,0.973444,-7.888332,1.257017,8.276547,9.787688,9.775904,9.407307,7.725852,-3.660661,-3.560908,6.504308,5.929304,-3.373338,-0.982374,2.802213,-6.978052,5.618145,0.191891,-3.162780,8.758695,-9.763812,2.083765,1.900013,8.263671,2.231750,5.194380,-5.443907,1.364945,7.722134,0.162217,4.525108,3.108400,-7.470560,9.882888,2.138973,-7.386626,9.029678,7.077527,-1.102124,-6.508397,-9.963527,3.513391,-8.270739,-6.659148,-0.679643,-1.521284,6.667541,-6.768406,9.983162,-5.250514,-8.400012,-9.894154,-3.529633,2.858698,-4.406314,0.950862,4.696706,-2.045430,8.347635,1.882284,-3.398632,1.792215,5.183775,-5.647528,9.080313,2.389985,1.018535,-0.079306,4.942659],[6.991296,5.824387,3.105183,7.993935,8.685908,-5.345888,-2.347174,-1.111875,-9.226473,-8.442311,-1.633747,-0.012913,2.337575,1.015623,7.377383,7.782374,1.280410,4.394458,-6.202347,-0.199589,8.728872,-9.934084,2.858845,1.124373,7.238933,-4.728077,-6.656619,1.803120,7.522784,3.914276,-9.326831,2.895658,2.841736,-3.950524,5.057397,1.486249,6.996778,-0.693539,5.617744,-0.670242,2.266826,-2.426146,7.351415,-1.934751,5.476115,-4.599928,-4.575038,3.238780,-4.193766,1.430064,-4.423713,3.779346,5.094009,-8.170148,8.589064,3.758624,-0.061708,-4.115739,1.832502,-8.915176,-6.983487,-7.948837,-9.891581,7.395880,2.470654,-5.163479,9.906318,2.974963,4.610155,2.169034,5.894578,-4.403597,6.398835,2.069216,3.510766,1.163003,-4.025880,-2.397342,9.418699,-1.956356,7.522366,-6.693596,-5.103310,2.045800,9.749361,-3.595685,1.140566,-0.236767,-7.106547,9.623505,6.043037,5.366562,5.404642,-5.824598,2.508882,9.426751,1.120102,-9.660632,-8.534394,-3.912715,-1.704678,-9.960984,3.787455,-3.501568,-4.082934,3.860417,-4.762786,-2.133449,-3.299121,-5.013893,3.463845,-1.229566,0.775615,-7.631038,-0.100303,-7.226541,8.322328,-9.587827,7.767097,-3.120346,1.850117,-9.718100,6.862655,3.366567,3.885992,1.172912,0.307814,-9.465561,-1.203919,-4.018550,1.364512,-2.781189,4.560702,7.444469,3.713142,3.713998,0.651739,1.766131,-3.887580,-6.216934,-2.760508,-7.815171,-0.213629,6.707813,4.382625,9.644821,-8.275857,5.524523,2.304185,-8.035150,6.178434,9.065809,9.829493,3.343230,4.487984,-7.945939,9.071627,4.420826,9.058166,6.867566,5.125212,0.150784,-9.899471,2.945752,7.716080,-7.402109,8.263501,4.506211,-9.855071,-5.403112,-7.423621,-2.259224,6.285623,5.943621,-8.473668,7.973609,-3.766531,5.407221,-6.084928,-3.521071,-6.171473,-7.310578,-9.626634,1.580617,-8.883920,-1.001862,-1.853209,-2.094676,-0.915310,-6.377936,-6.561372,-8.756504,-5.688952,8.158306,1.769082,-5.545746,7.218226,1.636086,-0.414290,-3.506486,7.830922,1.658416,3.085127,9.338837,-6.887784,-3.049120,-5.837022,6.441348,-4.885496,7.357602,-0.480691,-2.278419,-6.261026,3.202984,-2.385054,0.507934,-3.288214,3.261760,-1.107607,1.848775,-1.532720,-8.135585,9.374196,4.244310,-3.069519,6.916842,-1.810271,-1.355494,0.777968,2.074567,-7.065030,1.725462,0.663930,-0.878364,-5.626845,-9.497577,-9.102983,0.706070,-7.382641,5.025402,8.077557,2.807173,-3.516133,-4.518296,0.780547,4.644113,-7.290924,-6.651761,4.658189,5.477127,0.004546,-7.347188,-6.614945,2.742404,-8.199096,-7.200501,5.428094,7.593182,4.061788,9.072960,4.541360,-1.137940,-8.150621,-4.288037,-6.195512,6.342075,3.643180,1.997449,7.002525,4.456750,5.114898,9.531003,3.649140,1.581726,-5.504000,-1.168127,8.313283,3.655684,1.432722,-7.749717,9.435383,2.814269,4.171876,2.526357,3.710607,0.581719,-3.153987,7.385084,8.882177,-3.620877,-7.689723,-7.040322,-9.673198,7.690346,9.295687,1.468596,2.071780,6.928915,3.899323,8.228121,1.247284,2.767237,2.998453,-1.433162,7.610576,-7.670803,6.327121,-9.358579,-3.756473,6.004442,1.980260,-1.531241,-7.239608,2.628079,-5.962001,-0.924650,6.127446,9.018433,1.600138,-1.905764,1.747865,-2.463015,2.256478,-3.688768,-8.214043,1.298548,-1.448185,-7.510550,7.471110,-9.790700,-1.591255,-5.120465,-4.266755,-5.310598,6.819258,1.351503,7.573763,2.790791,-3.947642,-1.477628,7.613424,-2.479727,1.502207,-1.964022,-6.599676,7.147942,-6.191597,2.954194,3.827798,-7.791206,-3.510906,5.725729,2.215368,-6.143060,-5.229753,-3.818534,-3.635500,5.909930,1.274346,-5.016267,-0.796770,-2.483073,5.298003,-7.098673,3.865562,3.887638,-8.149818,1.384606,5.027467,3.238343,-3.127048,-9.225282,-7.291731,-1.134032,8.860022,8.392294,-9.172098,-1.726350,9.273073,9.621110,0.747841,-1.119475,2.628304,6.299425,8.163299,7.558785,-3.960570,-3.246487,6.102007,-5.748625,-4.815640,5.540414,6.384165,-2.636270,-7.909825,0.822324,3.194061,0.481595,2.037133,1.317938,7.419384,-0.931835,-7.754866,-2.678847,-7.773894,8.472698,-6.741763,8.638291,-8.178625,3.289094,4.069903,8.948753,-8.198531,-4.907180,9.504365,6.020095,-9.828066,1.345586,-6.648581,-7.428109,-0.520581,4.408968,-0.357501,2.524056,9.978662,4.517334,7.921030,3.247536,1.903985,-9.805731,7.946191,0.934147,0.329039,2.738840,-3.988561,-0.121726,1.411750,-6.891588,7.581221,-2.372682,-6.508927,8.433836,-5.367103,2.963617,-6.200502,8.037608,3.748974,6.263572,4.045422,8.377322,5.827153,-1.716972,5.069184,-8.347645,-7.354316,7.434403,7.444062,1.106373,0.566684,9.938506,-8.325125,-1.153644,-4.055883,-0.341878,-2.325405,3.762780,-1.585302,-8.842577,-4.994992,-9.015332,8.035301,1.602292,-0.835948,8.340699,-1.070397,-9.152396,6.986334,-7.323667,-9.293910,4.815212,-6.766762,-9.670973,-1.181241,0.804317,-9.878234,-1.209015,0.208460,-4.461788,-1.915876,-6.029017,-1.069834,2.553181,0.919144,8.742047,-7.931410,-0.501818,-0.459435,7.345377,4.885959,6.440650,-9.440541,1.652810,-9.162842,-7.424118,0.830755,7.102997,6.361395,7.551448,-5.910503,-6.706788,3.101628,-6.368129,-2.761818,9.517278,-9.686015,1.491794,-8.854711,-4.840152,-9.996327,0.454170,3.522840,0.852971,6.847526,3.022664,-8.178169,-3.957419,-6.485509,2.126559,3.019798,-2.509427,7.816134,-5.172085,6.922402,-2.882996,6.040655,1.683983,-9.236216,2.464147,-1.169781,-8.756892,3.503942,-6.821788,4.194467,-6.462257,-8.601955,-7.169957,-9.426479,2.258093,6.682245,3.516089,1.146500,-4.049784,4.656866,1.412478,-6.533236,-6.923729,0.684084,-2.131116,-2.073515,1.049976,2.037665,3.828747,-1.544976,0.760361,-8.802696,2.872712,-1.079292,-6.335268,0.674609,6.587586,0.265522,0.985054,-2.946642,8.949472,-0.576165,-4.347026,-0.250124,2.705248,-3.596583,-7.227498,7.171902,5.621274,8.100623,-3.038022,9.601127,1.211793,0.753378,8.607081,-6.296023,0.155445,9.661830,-1.312005,1.490312,3.416113,1.148270,-8.506876,2.792736,-1.439769,7.892657,5.616141,-6.037831,8.335386,-3.472844,1.794485,6.279326,0.488049,-1.115670,-9.816293,-8.632224,-1.564238,-9.681906,-9.923344,-4.569105,-3.353236,7.858431,-1.834336,-7.037454,-0.262647,2.367583,9.003666,-1.126189,9.150357,7.719713,-7.125604,5.768888,6.043734,8.836820,3.358084,-8.270271,-7.889142,-8.044798,3.202948,-9.517481,1.962779,6.230473,6.112929,7.701323,9.285871,-0.625025,-9.705269,-7.513887,4.096678,-9.943131,5.098115,7.620291,-7.746527,-8.637929,-2.996631,0.925148,-1.532902,9.005669,-3.643765,9.307072,3.955567,2.153631,3.913128,8.361070,-1.405253,-6.555046,-5.797526,4.419951,8.356552,-9.245540,-0.011893,7.932780,-8.091445,-5.284107,9.461539,-6.214283,-1.397111,7.687579,0.691012,-6.193050,-7.758432,0.598569,-0.720358,5.728048,9.771756,-5.423072,-8.870269,-7.435575,-1.204427,2.681323,-0.521264,-0.467573,-9.259737,5.653696,-5.269984,6.394272,-0.442010,0.429206,1.559855,-9.301510,-0.009655,-0.439141,-9.635976,0.508502,-8.426708,-6.517445,4.989638,8.172303,-2.418909,1.810641,-4.519761,4.597042,-3.883484,-5.952448,-7.501113,-4.668812,4.764725,6.739822,5.807689,-5.237300,7.311283,8.099625,5.769265,-6.075726,2.336662,-5.874465,-0.407714,-0.145237,-4.123358,-1.929238,4.406649,9.963318,-0.308036,-9.091246,2.266409,4.728329,9.507827,7.747017,0.037414,5.059251,-6.946697,-9.054790,9.237166,6.222830,6.198968,-3.973039,-0.591017,9.095500,-8.593521,-1.899100,-9.411877,7.172694,-0.124353,-4.917613,-1.940319,-3.024914,0.471091,-0.970887,6.330986,-9.485656,9.694536,2.928867,-9.708971,-1.897054,-6.712801,5.983854,-1.590166,0.549856,7.385388,-7.821203,2.471363,-4.934958,-6.302294,8.419456,-4.696547,-9.652141,5.673612,4.731091,6.144703,-1.385179,1.760756,-5.812505,-5.795646,-3.729337,-5.353637,-6.685339,-4.262295,-2.555105,5.955899,-2.282894,-3.739046,8.612895,9.712159,2.454566,8.457058,-8.305056,1.713161,-7.302648,-1.637631,-2.324774,-9.507263,-5.754649,3.709096,3.878717,8.229853,7.848710,-8.210851,4.977302,1.542487,-5.040188,-0.632752,2.400943,-0.459762,-2.567977,6.374941,2.534522,6.484161,-1.602468,-3.437835,1.810308,6.272453,7.378263,8.771196,8.337012,-2.758256,2.979045,6.971961,-4.870170,2.260398,-2.094283,9.360829,-7.748531,-6.555814,-9.306953,-3.344561,-1.498583,-8.559741,4.614396,-3.022909,-6.499607,7.723490,2.640739,7.914609,-5.971032,-6.028823,4.277156,-3.906147,-8.936785,-7.393327,6.466143,-7.703102,-4.198556,-3.978152,6.335799,0.676365,5.550845,9.754442,9.571555,-4.550893,6.834316,-4.303572,4.980976,-2.210165,2.491756,-3.555257,8.767199,-2.440168,9.631804,-4.144751,8.406596,-6.285126,-7.306030,-3.518237,-5.338739,5.973753,0.073635,-3.105824,-5.428083,9.320302,8.738871,-6.960924,-8.821072,7.183180,0.603768,-5.519391,3.445821,3.489854,7.255607,5.547135,0.127111,3.620588,-3.430204,1.030667,5.133525,4.721135,-8.912258,7.787450,-8.717346,-3.910842,-2.930926,2.525165,9.922450,1.916913,-3.853259,8.647596,9.403596,-6.907758,-5.740170,-6.852536,-1.713084,4.103704,-4.631684,-2.552617,1.630572,-8.110018,1.009293,5.213979,1.757821,8.066029,0.578051,0.637473,-2.690618,-1.592712,5.057560,-0.718253,-0.175225,-3.877123,-6.002006,-5.167663,8.851343,-1.331454,-3.124992,7.672986,-8.554774,1.893799,3.362141,0.333592,-9.203421,0.564497,-4.936533,-8.605381,9.139820,8.914134,9.738471,5.431028,2.297375,8.951986,5.212505,5.117842,-0.272657,1.255551,6.160226,8.797992,-0.016442,9.075323,-2.801430,-7.942104,-3.724796,6.984760,7.231091,-6.151697,-4.875170,-3.711256,-8.449682,-1.836476,-2.032081,7.087128,-9.698685,3.790826,7.582478,9.383509,-1.074761,8.385541,-6.869466,-8.622540,4.748201,-1.744841,1.395636,4.302258,-5.728974,-9.484612,0.787987,-5.841146,-2.529417,-9.852232,-8.827547,1.958222,4.391373,8.055569,4.620040,5.244724,-4.826650,2.926155,-3.763464,8.614207,-6.506201,1.996478,5.485803,5.729500,-6.946392,8.644307,4.487607,7.298937,9.577528,-2.448968,1.281603,6.058279,7.230921,0.038923,3.950171,-6.833296,-4.793046,1.324818,4.924472,2.017699,4.875694,-3.496881,8.666691,7.929851,-5.808217,2.462183,-2.789334,3.545104,0.121629,4.772889,-7.762016,-3.811845,-1.263977,-9.197277,-5.002663,2.426529,4.064653,0.099874,6.306481,4.594999,-6.214035,3.895276,-0.241427,7.985301,0.405878,-4.473191,-1.878600,-2.121526,3.935227,5.496851,-0.352679,1.719464,-7.310153,-4.642799,3.179181,-2.770225,6.991069,-5.738607,-8.284969,1.597124,3.753966,9.984286,7.992166,-3.254778,4.773633,-9.623335,-5.350713,3.988057,-0.023979,-9.798938,2.943295,-2.720959,2.974937,-0.890649,-6.054529,6.586338,-9.420286,3.543412,9.400541,-8.521155,7.692282,-3.346840,-6.730198,8.381803,-8.541847,-3.795930,-9.141771,-3.879258,-2.693502,3.128690,-7.167161,-1.839531,-3.053143,-9.839558,7.614766,-8.699219,-5.235782,-2.449586,-5.521212,8.551032,9.081502,-5.857291,-2.353391,7.252710,-3.469638,7.633050,-8.060555,0.282319,-6.655368,-2.507747,-9.922789,-7.406808,2.820260,1.326453,-8.972957,-1.819568,-4.763833,2.698101,1.987980,4.444613,-9.824909,0.686316,-5.184075,7.914707,-9.418929,-7.417173,-2.533527,8.809347,7.181977,1.420420,-2.750516,-3.329660,-3.449913,2.883408,-5.896443,5.951925,-4.085586,5.809955,2.998196,7.202157,-9.147090,-6.519558,-9.008027,8.501212,-7.398190,-5.020576,-2.998093,-5.086652,-6.653962,7.460881,-0.302803,9.137912,0.325302,-9.260772,2.725501,-4.370832,4.878226,-1.751955,8.426176,-3.547240,-5.098798,-6.148646,6.800189,-1.080619,-9.432445,-2.785457,-4.960099,2.188982,3.196972,4.772869,9.151942,-5.282026,-8.705368,4.349347,-8.141205,-9.771458,-7.256582,-6.870996,9.777468,9.590690,-9.874953,-5.734766,-3.624908,-3.281532,9.901673,-4.689093,3.534673,-1.385747,-6.097754,4.809414,3.723426,0.410416,-9.341501,3.774905,-8.401056,-3.709178,-2.538139,-1.423909,-9.242426,-8.198455,-5.321253,2.160421,-9.047787,3.860052,3.710746,5.072357,-0.295119,-2.674361,-7.536747,-2.191305,-3.691085,3.248243,-5.397593,7.373081,-3.944659,-9.157236,6.296916,8.757533,8.517568,-9.295717,6.231025,2.872541,-4.173826,9.636299,3.336494,-7.891598,-5.578263,2.070211,2.693131,9.846387,-7.705828,-8.367110,7.018131,5.201447,-6.415219,6.577592,-7.149119,-7.881386,-6.516708,0.455473,3.647756,-3.087164,-3.365519,-0.431036,-2.233087,7.249138,-5.842830,-2.559313,5.199780,-3.011757,1.257299,-0.652503,3.877415,7.847031,-7.247974,1.081864,-8.273733,5.972292,5.443533,-5.389403,3.552278,2.302157,2.945179,-7.250669,7.243762,-1.888687,-6.879475,-5.300564,8.292199,-1.442182,9.823015,-1.379950,3.250581,-4.678970,4.407157,-4.518051,-7.667109,-3.276415,-0.663959,1.006208,-2.042489,-8.041102,-7.093252,-2.496789,-1.284577,3.095815,-5.139980,2.020083,8.482714,9.464481,-6.874267,4.705475,4.498137,-2.213720,-5.277756,3.814314,-5.165236,-1.007509,3.509171,-6.270805,4.781647,9.609387,2.519041,8.258064,-7.026457,-9.658975,-5.572264,4.130268,6.836029,2.904473,9.727442,-7.286783,3.213038,-1.680073,9.476190,-0.073962,-8.160283,9.698330,9.378194,-7.824783,2.669068,-6.940984,0.659839,4.795030,-2.000210,-6.514059,8.744088,1.257359,9.716273,2.462929,-7.251490,3.676402,0.658913,8.299708,0.697486,-6.289329,-4.249979,2.123814,7.473825,-7.944864,9.210125,0.007038,-2.316292,9.734056,2.234963,-4.967655,7.558725,-5.621393,-4.747758,6.686074,-6.753094,-5.093991,-3.142820,-0.098637,-0.905837,2.013028,5.136067,0.352652,4.549061,-5.500680,6.609549,1.161780,-2.816145,-8.017003,0.128358,9.970426,6.821027,-0.253135,3.801673,0.959798,6.488756,0.275785,-4.900508,-0.039007,-3.825621,-8.848957,-1.953982,-5.628101,3.638542,0.139513,-9.732040,-8.840646,4.319136,3.585396,5.229016,-5.263599,-4.766948,-2.804181,-3.859352,-8.502920,5.166221,1.303873,-8.505948,-4.490811,-1.599387,-4.116236,-7.806191,-2.349978,4.414425,-0.578681,8.019282,-6.711187,6.151641,-3.020830,2.294666,-4.859316,9.187271,-3.302428,3.701734,9.549747,6.835082,-0.289546,0.995706,9.453632,-0.084355,4.154682,-2.809347,8.779658,-0.013211,-4.685095,1.775186,-3.382133,-5.265613,-0.708475,-0.083685,4.895112,-7.224648,3.467605,-2.588276,-1.702502,2.037835,-0.945605,0.790366,7.730546,6.543292,-6.295573,-8.295914,8.938429,6.940506,-2.433288,-6.892625,5.488951,2.099925,-7.345641,7.366396,-7.881325,-2.436550,6.787545,4.419637,-0.121965,-1.615880,4.495444,1.309065,6.506233,-0.084032,-4.049098,2.115622,1.055311,3.805639,-4.605398,1.777751,6.393167,-6.775211,6.925070,6.991320,-9.334510,-8.892525,-8.868710,0.768246,5.780968,9.973575,-4.697171,4.390861,1.747148,7.508932,-4.303866,-5.152230,-4.255222,-5.070695,-7.025062,4.709673,1.700344,-8.226641,-4.949955,4.700374,-3.738275,6.122539,3.748699,-1.764769,4.910417,-0.372930,-9.730355,4.615109,5.312103,7.199888,2.969794,0.688450,-3.154133,-8.022407,2.867293,-9.276167,-6.605872,-9.547332,7.189254,-3.109784,-2.172225,-4.861352,-1.910477,0.179095,3.828343,3.695572,-8.240251,6.626420,2.518861,2.130939,7.533308,-1.378805,1.669482,3.379890,2.267866,-9.290662,-9.161310,4.524646,-7.703245,3.857235,0.612826,1.028849,4.279438,-7.867314,-9.237168,6.623927,-2.230047,-7.373687,-1.865607,-5.544403,7.087799,2.999757,4.867307,-9.498165,5.397668,4.448306,0.011730,-4.518418,9.773997,3.099764,-3.532602,8.130258,-3.542177,5.221640,7.531964,-6.233355,-9.007326,-9.971011,-3.215182,5.333531,-5.417289,-7.427066,5.354645,-2.743552,-4.896766,0.752314,-0.001649,2.163038,-0.810340,3.100113,-9.743891,-6.126536,2.376353,-5.461594,-6.583850,-2.102985,-0.280761,-0.638741,5.638621,-8.442104,-5.076730,9.887410,-4.054524,0.792917,3.577118,-0.981531,-6.221046,-7.857984,5.994606,-8.952459,-1.980891,8.321368,7.422986,1.387071,-5.709080,-8.128719,4.226962,-6.290000,-3.248873,-0.805691,-9.679394,4.980788,4.701332,5.991241,-0.899443,-9.631429,-1.162503,8.749735,8.931750,-6.678114,-2.155261,-9.481528,-0.973048,8.898253,-2.013117,-5.047301,-3.941829,-6.595006,5.758395,8.133420,6.514277,2.320520,7.991552,3.520668,0.993164,-3.304593,5.755611,4.736054,9.412690,-7.324072,-4.118732,9.089637,8.334192,-9.009576,5.446194,-6.530983,-5.962678,-6.542830,6.705343,-6.261144,2.616604,-7.621906,-2.297676,4.747775,5.218433,9.219679,-3.251445,-5.347984,-1.495909,9.322049,-2.550097,-7.941757,8.039459,-9.692366,9.400751,1.188457,-8.534409,7.881066,3.535709,-0.029741,-7.527298,-6.090591,-4.674992,-0.450718,1.410320,-5.072937,-3.295409,-9.890818,7.017234,-8.701852,-4.326771,-2.486287,2.355186,2.921451,-0.923374,1.417637,0.073284,4.509062,1.596022,6.282401,7.908033,-1.742409,-3.588853,4.556593,-9.882888,-8.188722,1.631168,9.135935,-6.220510,4.307045,-3.681318,-9.202953,-2.153752,-8.228502,5.238126,5.777868,8.568506,-8.740388,-6.465876,-8.102225,8.669493,3.766347,0.176570,-6.696824,9.887949,-0.656744,-6.591399,-5.607697,-2.569158,-6.175657,-4.150388,5.540007,-9.883348,6.816744,9.083614,1.900409,0.460502,-6.483761,4.145687,-1.865696,-5.854763,-2.977369,9.993882,-1.498574,5.838295,-7.408457,-8.144411,-6.362134,1.273908,7.284427,7.381934,-0.746089,-7.453558,0.761682,4.046506,-8.865656,-1.788499,-5.735279,6.327687,7.740373,-6.711459,-1.043914,1.650020,3.375996,6.161327,-8.843233,6.360406,6.586079,3.461097,0.996832,-1.162988,-2.205400,-6.054084,7.222098,0.485457,4.358792,-8.673021,-8.688204,-8.983772,-5.136738,7.870490,-9.314520,3.667033,-0.409725,-6.672797,1.052204,9.233172,9.807209,6.938974,-1.297436,7.856435,-3.740444,8.045652,-9.415388,-6.420159,3.954766,8.988665,-4.048831,5.552402,8.648567,-0.577527,2.875715,-3.579695,9.712439,4.940252,2.714849,4.454268,-6.697314,-2.700436,-9.185156,6.773485,-2.713665,8.426255,-7.689665,4.636891,-5.714866,-8.232215,-3.976927,-1.856326,-1.949898,5.206797,1.759492,2.747221,3.066250,-5.418166,-5.935627,-7.519163,-9.999013,8.573061,-4.761668,-7.355160,-0.479675,-1.182198,0.349067,4.961293,-0.002808,0.908429]], dtype = "float32")#candidate|8564|(2, 1800)|const|float32
call_8562 = relay.TupleGetItem(func_8319_call(relay.reshape(var_8563.astype('float32'), [36, 6]), relay.reshape(const_8564.astype('float32'), [3600,]), ), 5)
call_8565 = relay.TupleGetItem(func_8323_call(relay.reshape(var_8563.astype('float32'), [36, 6]), relay.reshape(const_8564.astype('float32'), [3600,]), ), 5)
func_3929_call = mod.get_global_var('func_3929')
func_3931_call = mutated_mod.get_global_var('func_3931')
call_8574 = relay.TupleGetItem(func_3929_call(), 0)
call_8575 = relay.TupleGetItem(func_3931_call(), 0)
uop_8579 = relay.log2(const_8564.astype('float32')) # shape=(2, 1800)
bop_8585 = relay.floor_divide(uop_8579.astype('float64'), relay.reshape(const_8564.astype('float64'), relay.shape_of(uop_8579))) # shape=(2, 1800)
uop_8592 = relay.asin(bop_8585.astype('float64')) # shape=(2, 1800)
output = relay.Tuple([call_8557,call_8560,call_8562,var_8563,call_8574,uop_8592,])
output2 = relay.Tuple([call_8558,call_8561,call_8565,var_8563,call_8575,uop_8592,])
func_8597 = relay.Function([var_8563,], output)
mod['func_8597'] = func_8597
mod = relay.transform.InferType()(mod)
var_8598 = relay.var("var_8598", dtype = "float32", shape = (216,))#candidate|8598|(216,)|var|float32
output = func_8597(var_8598)
func_8599 = relay.Function([var_8598], output)
mutated_mod['func_8599'] = func_8599
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5903_call = mod.get_global_var('func_5903')
func_5905_call = mutated_mod.get_global_var('func_5905')
call_8610 = relay.TupleGetItem(func_5903_call(), 0)
call_8611 = relay.TupleGetItem(func_5905_call(), 0)
output = call_8610
output2 = call_8611
func_8617 = relay.Function([], output)
mod['func_8617'] = func_8617
mod = relay.transform.InferType()(mod)
output = func_8617()
func_8618 = relay.Function([], output)
mutated_mod['func_8618'] = func_8618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5031_call = mod.get_global_var('func_5031')
func_5032_call = mutated_mod.get_global_var('func_5032')
call_8648 = func_5031_call()
call_8649 = func_5031_call()
output = relay.Tuple([call_8648,])
output2 = relay.Tuple([call_8649,])
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
var_8782 = relay.var("var_8782", dtype = "float32", shape = (8, 2, 13))#candidate|8782|(8, 2, 13)|var|float32
uop_8783 = relay.atan(var_8782.astype('float32')) # shape=(8, 2, 13)
func_4096_call = mod.get_global_var('func_4096')
func_4097_call = mutated_mod.get_global_var('func_4097')
call_8788 = relay.TupleGetItem(func_4096_call(), 0)
call_8789 = relay.TupleGetItem(func_4097_call(), 0)
uop_8797 = relay.sqrt(uop_8783.astype('float64')) # shape=(8, 2, 13)
func_5738_call = mod.get_global_var('func_5738')
func_5740_call = mutated_mod.get_global_var('func_5740')
call_8807 = func_5738_call()
call_8808 = func_5738_call()
bop_8811 = relay.equal(uop_8797.astype('bool'), relay.reshape(uop_8783.astype('bool'), relay.shape_of(uop_8797))) # shape=(8, 2, 13)
uop_8830 = relay.sinh(uop_8797.astype('float32')) # shape=(8, 2, 13)
func_4558_call = mod.get_global_var('func_4558')
func_4561_call = mutated_mod.get_global_var('func_4561')
var_8833 = relay.var("var_8833", dtype = "float32", shape = (1, 224))#candidate|8833|(1, 224)|var|float32
call_8832 = relay.TupleGetItem(func_4558_call(relay.reshape(var_8833.astype('float32'), [2, 7, 16])), 0)
call_8834 = relay.TupleGetItem(func_4561_call(relay.reshape(var_8833.astype('float32'), [2, 7, 16])), 0)
func_7039_call = mod.get_global_var('func_7039')
func_7041_call = mutated_mod.get_global_var('func_7041')
call_8837 = func_7039_call()
call_8838 = func_7039_call()
bop_8861 = relay.divide(uop_8797.astype('float32'), relay.reshape(uop_8830.astype('float32'), relay.shape_of(uop_8797))) # shape=(8, 2, 13)
func_1095_call = mod.get_global_var('func_1095')
func_1097_call = mutated_mod.get_global_var('func_1097')
call_8866 = relay.TupleGetItem(func_1095_call(), 1)
call_8867 = relay.TupleGetItem(func_1097_call(), 1)
func_6694_call = mod.get_global_var('func_6694')
func_6695_call = mutated_mod.get_global_var('func_6695')
call_8875 = relay.TupleGetItem(func_6694_call(), 0)
call_8876 = relay.TupleGetItem(func_6695_call(), 0)
func_1899_call = mod.get_global_var('func_1899')
func_1901_call = mutated_mod.get_global_var('func_1901')
call_8883 = relay.TupleGetItem(func_1899_call(), 0)
call_8884 = relay.TupleGetItem(func_1901_call(), 0)
func_5148_call = mod.get_global_var('func_5148')
func_5150_call = mutated_mod.get_global_var('func_5150')
call_8894 = relay.TupleGetItem(func_5148_call(), 0)
call_8895 = relay.TupleGetItem(func_5150_call(), 0)
func_7753_call = mod.get_global_var('func_7753')
func_7755_call = mutated_mod.get_global_var('func_7755')
call_8901 = relay.TupleGetItem(func_7753_call(), 0)
call_8902 = relay.TupleGetItem(func_7755_call(), 0)
func_5957_call = mod.get_global_var('func_5957')
func_5960_call = mutated_mod.get_global_var('func_5960')
var_8907 = relay.var("var_8907", dtype = "float64", shape = (13, 2))#candidate|8907|(13, 2)|var|float64
call_8906 = relay.TupleGetItem(func_5957_call(relay.reshape(var_8907.astype('float64'), [1, 13, 2])), 0)
call_8908 = relay.TupleGetItem(func_5960_call(relay.reshape(var_8907.astype('float64'), [1, 13, 2])), 0)
output = relay.Tuple([call_8788,call_8807,bop_8811,call_8832,var_8833,call_8837,bop_8861,call_8866,call_8875,call_8883,call_8894,call_8901,call_8906,var_8907,])
output2 = relay.Tuple([call_8789,call_8808,bop_8811,call_8834,var_8833,call_8838,bop_8861,call_8867,call_8876,call_8884,call_8895,call_8902,call_8908,var_8907,])
func_8911 = relay.Function([var_8782,var_8833,var_8907,], output)
mod['func_8911'] = func_8911
mod = relay.transform.InferType()(mod)
var_8912 = relay.var("var_8912", dtype = "float32", shape = (8, 2, 13))#candidate|8912|(8, 2, 13)|var|float32
var_8913 = relay.var("var_8913", dtype = "float32", shape = (1, 224))#candidate|8913|(1, 224)|var|float32
var_8914 = relay.var("var_8914", dtype = "float64", shape = (13, 2))#candidate|8914|(13, 2)|var|float64
output = func_8911(var_8912,var_8913,var_8914,)
func_8915 = relay.Function([var_8912,var_8913,var_8914,], output)
mutated_mod['func_8915'] = func_8915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7753_call = mod.get_global_var('func_7753')
func_7755_call = mutated_mod.get_global_var('func_7755')
call_8958 = relay.TupleGetItem(func_7753_call(), 0)
call_8959 = relay.TupleGetItem(func_7755_call(), 0)
output = call_8958
output2 = call_8959
func_8962 = relay.Function([], output)
mod['func_8962'] = func_8962
mod = relay.transform.InferType()(mod)
mutated_mod['func_8962'] = func_8962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8962_call = mutated_mod.get_global_var('func_8962')
call_8963 = func_8962_call()
output = call_8963
func_8964 = relay.Function([], output)
mutated_mod['func_8964'] = func_8964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8477_call = mod.get_global_var('func_8477')
func_8478_call = mutated_mod.get_global_var('func_8478')
call_8988 = func_8477_call()
call_8989 = func_8477_call()
output = call_8988
output2 = call_8989
func_8992 = relay.Function([], output)
mod['func_8992'] = func_8992
mod = relay.transform.InferType()(mod)
output = func_8992()
func_8993 = relay.Function([], output)
mutated_mod['func_8993'] = func_8993
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8999 = relay.const([[[-8.702613,-7.977909,-1.016912,2.299862,7.306828,-5.372223,2.001194,7.271210,-7.563662,-6.121856,3.320653,5.224747,1.147315,8.343649,3.702134,-4.339530],[-3.039498,0.422387,-3.868719,7.333579,8.764940,0.295090,7.391137,8.957251,5.424127,-3.700852,-4.921770,5.393342,-2.426489,9.023861,7.102216,-2.794287],[-6.689241,3.268345,-5.063415,-1.296052,-0.411023,-1.549273,-2.225060,0.847930,-4.757604,-7.295727,4.737940,-0.610176,6.818930,3.046055,1.543166,-3.755994],[-1.508775,4.670636,-2.744317,-7.561664,7.736522,-9.581274,-4.486305,5.143651,9.228431,-7.152357,4.833655,1.723741,-2.019532,-3.808682,-0.916309,-9.831777],[-5.423769,9.666233,0.818357,3.783675,-8.420175,6.494772,-7.615407,5.509585,-0.745565,-8.862043,1.762527,-2.685292,7.227416,0.548532,6.115859,-5.312429],[3.479247,-1.547724,1.231660,-7.926868,9.221608,3.179117,-3.948260,-5.626033,-6.686265,6.969016,-0.396527,8.145145,-3.490132,4.167680,-8.900571,1.835606],[4.086319,0.068009,0.507062,-4.725692,5.660506,-0.455711,7.272802,-5.317579,-3.887701,2.398941,-5.309822,-2.843293,7.344037,-4.844995,4.866286,-9.929388],[-6.199900,7.543648,9.737211,-5.812686,5.455132,-0.208610,4.351273,-1.934991,-0.215347,-7.725835,4.781335,0.401619,-1.729877,-8.195860,0.947007,-4.114702],[-6.435418,-2.584028,-4.072118,-4.138815,5.642216,-2.337599,-0.043276,-7.289857,-0.857110,7.292298,9.629222,-9.272677,-8.655543,0.571357,0.148043,9.866715],[-0.673590,1.314590,7.972147,-3.726109,5.869245,8.904355,-3.945824,-0.248044,3.618507,-2.573462,3.925633,-9.064081,4.583531,3.650601,-6.116537,8.457030],[-4.274636,5.592976,-1.199720,9.482630,-9.085652,3.050285,-0.130032,4.420397,6.077802,9.802907,-7.150175,5.986129,0.592382,7.666281,1.221734,-5.881802],[1.390203,0.093616,-9.138117,2.703474,-3.991124,0.500147,2.306976,-4.142604,-6.832519,0.129504,0.547248,-9.887340,7.530516,-8.438326,-3.645925,6.678958],[-6.759381,-3.092888,3.541725,3.853394,-4.385500,-1.967479,6.212639,0.127690,-0.056389,1.231756,3.576859,2.805114,6.945401,8.312274,-1.866395,7.855093]],[[-9.822460,3.559754,-7.735803,9.227786,7.338956,-4.258711,-8.621486,-1.424998,-8.945375,-4.254172,-7.345448,-3.030448,-8.730889,7.710941,-0.760059,4.180746],[-7.987546,-9.512379,-7.811930,-0.334111,-8.444126,-3.241968,-5.045800,9.728733,-2.312675,-1.236886,2.072289,-2.097868,-9.165019,5.855482,3.791828,3.370672],[5.613779,-9.377901,7.604751,-0.581281,0.744668,-1.573274,2.619072,-7.263191,-4.936686,-5.519043,3.864674,2.852969,4.498055,2.600417,9.857003,-3.897101],[-6.493024,-3.287758,1.808869,1.951935,-4.826503,-5.817895,-4.257908,2.100049,2.708380,-2.050290,2.299894,1.328725,-5.191315,5.125875,6.633661,0.250081],[-8.955562,-2.548468,-1.159036,-7.450722,2.602974,-4.291195,2.301158,-0.588277,-6.899769,8.233611,-7.226456,-5.207732,7.753897,3.104247,7.836185,3.832021],[-1.681162,-5.040088,4.508232,6.168799,6.720504,-7.399195,-1.085639,-9.368812,-2.351242,-2.725640,-7.323214,3.714530,-7.215609,-9.156605,7.249831,9.560037],[9.700398,-1.346726,-7.995112,-4.197403,-9.364776,-0.477817,7.955173,2.138596,-4.817833,2.871193,-5.347096,0.815975,5.357175,-3.151267,5.386557,-2.908191],[0.282590,8.414980,1.561436,-4.067113,0.235879,-7.100799,7.095266,-5.322490,0.239268,-7.248488,-0.738614,-0.281674,0.440764,4.507475,-4.989323,-8.342698],[-6.244282,2.565807,4.345592,5.873307,-2.414069,9.773968,8.386295,2.831063,9.671454,-7.605931,2.004446,1.982998,-6.657182,7.628847,5.646377,-5.120484],[-5.597103,8.953196,1.756035,-3.667664,-2.835639,3.583144,5.044971,-9.132005,-5.766077,-1.165195,3.225912,9.256383,-7.842143,-8.315867,-3.012906,-0.841015],[-2.094047,-5.694131,-6.995919,2.589912,-4.115529,4.337256,7.545902,7.124620,-5.503630,-7.615478,5.082779,8.078964,-5.326283,9.656878,4.944862,0.269463],[6.167798,0.367493,-5.677471,-0.356041,-0.063398,-5.362833,4.940550,0.072105,-5.165290,2.416431,2.000936,4.638267,-7.782229,-5.728686,-6.375588,8.591542],[1.583638,-8.388314,6.257288,4.593818,-9.391112,-3.713107,5.991401,9.110469,9.137249,8.865681,-8.653372,-1.030222,-3.853801,-9.404730,9.602020,-7.917239]],[[-7.927928,-1.800040,-2.675688,1.691049,-2.651940,-3.526968,-2.463553,4.911140,9.648868,-0.706885,9.732331,-2.311705,-3.856000,6.866152,0.321947,-1.992978],[-5.146311,4.443745,-8.375502,2.431049,-0.124748,-5.895926,1.706822,-0.752798,7.733434,-1.194733,-1.758712,-2.445173,6.035452,-3.240146,7.476357,4.783353],[4.612673,-2.634585,0.976668,-1.438262,-2.700762,-6.244988,-9.697585,-3.057226,-2.807560,2.966629,7.194926,5.625434,0.509997,8.854921,-3.453562,-7.653771],[-6.898789,-6.848234,-3.662145,8.798604,5.779785,-9.145448,3.191047,4.729973,-0.599702,-2.041228,-8.459190,-5.554772,9.693700,5.727367,-6.931267,7.109367],[-6.380263,9.345047,5.824411,3.712747,-3.152893,-8.837699,-4.181699,8.923397,-4.152837,5.625881,9.360315,-0.031612,2.639070,6.638447,4.561508,-5.747525],[-2.239126,-1.890778,3.198482,-2.047695,-9.040891,0.236701,3.811770,1.029665,-1.721326,-6.034852,-2.521960,-1.114716,-8.676322,-4.357756,-0.019501,-9.649663],[-0.298199,-6.827959,-1.986244,4.859890,-4.016362,-3.276695,-0.634973,8.303627,-5.823106,-0.006203,4.903672,-8.480078,-2.012037,8.315036,-3.075703,5.282373],[7.115426,-3.508335,0.587187,-2.854113,-9.609795,3.539766,-7.155726,1.081323,-6.319222,4.268257,-1.586553,-2.352753,-0.211782,6.122876,2.565905,1.092038],[5.494543,-5.941069,-2.857927,-2.952699,8.760818,8.333625,-0.398786,-1.437732,-8.251293,-4.295931,-4.518961,-7.816935,1.037416,6.247342,-4.530772,2.089425],[-7.750722,-3.250155,-5.897647,2.340150,-4.826143,2.711379,5.722216,-9.823111,3.475120,-6.208733,8.402644,2.846430,-4.457025,6.215451,9.196360,-9.953008],[-2.632858,-6.039028,4.164075,2.197045,-0.230698,8.048987,-0.082664,-0.921914,-8.432114,1.456414,0.493557,-1.141657,5.537872,-7.106563,-8.380714,-6.738356],[-3.081183,7.006901,-9.165383,1.678269,1.356764,-3.923276,-8.091231,-2.383596,0.788105,-8.451507,-7.713454,9.642690,-9.259069,-3.244518,-4.455943,-5.148702],[-9.302210,2.367309,-6.900788,0.111588,3.889951,4.466388,-0.664608,-9.147803,-5.489095,-9.008646,-0.559342,-8.049742,-4.384114,4.239360,-7.236686,9.227108]],[[-4.631167,8.979876,7.303314,-3.077043,9.504998,9.537294,9.310864,3.184496,-3.941574,-5.687887,9.287717,-2.004491,-5.612709,6.058174,9.378738,5.235863],[8.301251,-1.976126,8.820684,7.840077,-1.203409,2.396521,-0.386845,2.614694,-4.445743,9.122775,6.001663,1.701864,-8.550569,-0.666336,6.168316,4.686049],[-4.167222,-5.648694,-0.599921,-2.184116,-1.109641,7.033840,9.435795,2.026950,-7.368579,9.760076,-4.822677,3.887273,5.341736,-6.493463,6.491382,3.386051],[4.593543,-1.082988,5.527753,1.875430,-7.347459,7.061431,8.565571,1.554966,2.049686,9.494567,-3.879458,-2.862661,-9.450852,-5.590404,-5.391561,-5.069174],[0.173389,-0.825394,7.270681,-5.652792,-2.736631,9.404941,5.608458,2.866585,-4.673463,-9.785420,-9.781259,-3.492104,-0.736238,-2.759621,0.708380,-7.046866],[1.781718,0.395214,-4.024679,-2.919027,8.723949,4.476481,4.195481,-9.357554,1.182280,-5.526857,6.477478,9.802363,3.196402,0.112176,-9.037017,-9.263478],[-5.716363,-6.169755,5.910646,4.890725,0.640052,5.058732,0.415060,-6.752573,8.702193,-2.220544,1.221402,-2.867914,-5.565249,0.713936,8.365243,-8.978389],[-3.225688,9.276383,-9.776022,-7.314296,6.179212,-2.124587,7.580196,6.778501,0.705779,-6.470278,7.480881,4.142616,-7.979880,-9.355571,-5.100038,6.415256],[-5.841880,2.788875,9.076413,-8.500107,8.468221,4.730779,7.836782,3.708848,5.659124,5.595384,-8.234859,-7.720631,-8.818443,8.578734,5.427677,5.658093],[9.698995,-6.120909,-1.230761,8.736037,2.128132,9.051852,1.110513,7.319095,-0.764113,-2.656331,-7.215098,3.442994,8.346430,7.373760,7.521500,-9.105396],[3.365518,3.519361,1.851480,-8.344542,7.002414,7.730123,-5.890336,2.409803,-5.467419,-2.710028,-3.883809,4.279394,-2.953566,2.972353,9.223787,-9.974605],[-7.262170,-8.815881,-2.426531,2.908038,-6.050248,-6.595348,6.093604,2.801833,1.519393,-8.748187,5.794898,-6.861087,2.873815,2.298484,6.354316,9.732823],[3.777292,-7.549725,-0.718296,-7.392164,-1.849271,-2.565500,-2.079333,5.645370,3.241996,-2.832616,9.916646,-1.189289,-6.338354,4.034140,4.347854,9.403596]],[[4.661296,-3.763745,3.160668,-9.054208,1.009793,-6.480098,2.958697,-1.994183,9.101742,8.071563,4.467447,1.297226,-3.051039,2.071106,-3.801474,-4.200626],[-3.828174,8.854571,0.671130,-1.130079,-0.652606,3.768082,-5.079080,-0.859562,-9.993427,3.816541,0.037236,8.653942,7.218840,7.386236,1.011077,5.269533],[-9.915907,-1.077882,4.171102,3.874622,5.486084,7.329337,-0.891473,1.798862,9.990772,-0.469358,-0.757614,-4.180687,-8.344788,8.892930,-1.559464,-5.311947],[6.033232,-3.080100,1.493844,5.956792,-2.225831,-1.911106,-2.868429,3.961607,-6.084247,6.061362,1.609880,6.294235,5.034209,-5.083353,5.667191,2.799471],[5.705793,4.211704,6.738227,5.243542,4.630601,-8.268657,4.741693,-5.085952,6.909428,-7.958028,8.832314,-3.115713,-8.585966,-2.549986,5.659911,8.259029],[-5.410076,8.765949,5.817305,0.125617,7.595662,-0.577308,-8.854114,-6.378386,-5.675353,-2.516170,-1.688765,4.311232,7.114551,2.321396,7.365993,2.326791],[6.592971,8.160021,1.540594,-3.658069,-8.635952,-0.672209,8.613420,-7.509002,2.005048,4.308490,9.680374,4.115489,3.067436,-4.986734,7.015007,-4.970633],[-2.056313,4.468883,-4.054005,-7.586127,-9.522470,7.925036,-3.292422,-8.051600,1.512305,7.195092,-1.300242,9.543272,5.431663,-1.924356,-3.459008,-0.029038],[-9.970052,-5.400851,1.641606,6.214572,5.716453,4.646372,-5.625619,-2.873065,6.196070,-6.327649,-0.471359,3.715048,1.856162,-6.040026,-4.193962,0.546987],[-7.315024,-1.190280,-1.432397,5.706050,-2.680339,1.691216,-8.522943,-1.554102,-6.126314,0.493941,2.343259,-8.743775,-2.446590,-2.588258,7.822138,6.547117],[0.711397,6.695690,8.546389,-7.565162,2.457864,-8.734043,6.390944,-9.497646,-7.728869,-5.308113,-7.754299,-5.862938,8.960114,-2.770209,-9.454816,-3.022590],[4.378632,-3.967800,-5.189150,-1.113002,-1.335569,-5.109817,-8.624231,2.436420,-0.545044,-8.816122,6.460913,-9.658024,0.122401,0.066436,-7.365097,3.010693],[-5.937687,8.176703,-6.558857,-3.880707,-2.066970,-2.555091,3.913445,7.922070,8.277211,1.399065,0.777172,2.757061,-7.917886,-3.137944,-0.851544,-3.450553]],[[0.061311,-4.564260,1.535577,0.015798,0.136755,-4.062174,5.220248,-3.868791,5.768062,9.074335,1.274368,1.552367,-6.395555,9.928169,-0.807855,3.940153],[6.114929,7.639823,-7.349295,-0.433060,6.085934,5.955801,8.076012,0.967991,2.684611,4.299838,-1.479603,-2.465180,-7.689927,7.838922,7.127938,0.781277],[-3.488335,4.815256,0.078599,-8.636688,7.552861,5.958175,-0.292079,0.250880,-3.034480,-7.111238,-0.353479,6.818845,-3.820298,5.389406,6.738485,-0.228503],[5.603859,-3.498260,-7.815379,4.747566,-8.355449,-5.163665,-9.889260,-8.094774,-2.320644,4.617183,5.035202,5.446862,2.133942,7.169808,4.323565,7.969002],[-0.753402,8.313771,-2.123314,-9.935121,-1.605290,0.564445,-3.322752,6.506856,9.950590,7.190465,4.232434,-9.374174,2.628945,6.522008,-2.464677,-1.689501],[-8.334836,0.169565,-4.925836,-4.199433,-5.331680,3.687975,0.528383,3.237177,4.640107,-1.678566,9.261273,-4.543397,-3.307685,-0.207004,-4.163896,6.539980],[-5.382091,5.363146,-3.874825,0.325601,-3.430598,-5.020827,3.655746,-7.078471,-5.323892,7.548561,4.986523,0.456318,0.943339,-2.690269,-0.230723,8.634546],[-5.136799,6.326614,-8.044496,3.263963,-2.721605,-7.238419,8.540135,-7.389158,0.726099,-9.502190,4.094371,6.122297,2.410622,-8.056250,6.275910,-5.872937],[1.991603,8.324163,9.548374,-5.818469,-4.215681,3.499856,7.244481,0.532771,-6.141595,9.395210,2.230532,-1.587922,6.860847,-3.795569,-5.066234,-1.757862],[0.966429,7.049303,4.259045,-5.681324,2.482705,6.388520,5.155243,0.445422,-2.580774,-3.074108,0.914419,-3.122248,2.405254,-1.960802,-9.627836,6.448163],[-6.249729,-5.109018,-0.515794,2.850662,-9.898639,-2.577898,9.890825,0.592612,1.083184,-4.100921,4.919010,7.204709,6.814121,-6.570339,-3.123168,9.218879],[3.275378,-1.233697,-1.948550,2.036393,1.952691,8.283421,5.968662,-6.578016,-9.453486,-7.729175,-9.642625,-1.331048,6.387013,5.409692,2.160502,-4.427050],[-1.277081,-0.359848,-3.532655,0.477222,-3.850098,-5.306747,-4.235368,-7.240859,8.242310,-2.781164,-8.038671,-6.697008,1.511514,7.315662,-9.184553,3.716410]],[[9.027494,-6.499750,3.038844,2.880611,-6.521967,-2.119224,-6.038945,1.462346,4.566498,2.717931,-4.158515,6.113700,5.710511,-1.370435,-8.149977,-4.402000],[-3.419020,8.317841,8.174266,6.516989,-8.274182,-5.698776,-5.728009,6.109942,1.691863,0.186342,-1.912314,4.967088,3.330175,6.048887,-2.507976,4.396472],[-1.298142,-0.825373,4.571713,3.072585,2.235308,7.144754,9.736115,6.445720,3.582001,9.204388,7.240340,-8.773720,-3.759843,-3.850228,5.596991,2.016118],[-1.885523,6.717422,8.678761,-0.590875,-6.564722,-2.533758,-7.897480,-6.188972,-1.863864,7.247256,2.372314,1.495003,8.506800,-4.088845,0.119389,0.463982],[8.435348,-5.885616,5.618798,-9.133067,-2.578439,-4.163886,-2.625839,-6.523953,-0.630928,8.173992,6.375585,5.162816,-1.752594,-9.588920,-5.670406,-5.874971],[-9.772608,-7.114485,5.708907,-0.842754,-5.863579,-9.881510,2.610603,9.117017,-3.305908,1.301944,5.441290,-8.531923,-5.078597,-5.540970,-5.051929,5.627763],[8.675724,5.074343,-8.854091,-9.295589,-1.458077,8.611447,5.163239,7.049874,0.760646,-0.989110,6.902477,8.786255,7.874412,-5.548176,-6.067748,-6.795835],[-8.498014,-9.807399,2.114384,0.858973,1.128935,-3.045551,4.908865,-0.663267,-4.266495,-0.643964,5.703142,-8.053903,6.936259,2.654621,-4.057594,9.962879],[7.809622,9.854702,-6.800894,-8.178173,5.370466,-8.891360,-7.192322,-4.599744,3.601122,-5.937568,-2.744902,2.087635,-7.037490,1.269644,0.192470,4.358694],[-8.087076,1.672703,5.121860,-2.424855,-2.401627,7.735464,5.983501,-6.875242,-2.304430,8.028444,8.371396,-9.003897,2.085096,-7.102634,-8.112727,6.993683],[-7.604336,6.039110,-9.703389,-2.176959,2.845666,7.199187,2.936863,3.580141,6.630658,-5.708759,-0.838308,-4.454620,-8.965515,-5.471431,-4.502854,6.929729],[-4.609042,-0.913344,-1.950299,-6.701048,-0.940171,-7.611577,8.613451,-4.245901,3.458361,8.895240,0.614093,5.188162,-9.934459,6.401239,-6.908148,9.445553],[0.314212,5.509606,-8.375866,1.341128,-9.864087,3.923483,-0.177338,-5.715979,-4.376678,0.241610,6.048701,-9.095753,-1.788735,-5.762188,-7.689938,7.661944]],[[3.840908,-7.721324,-4.494789,-1.569487,3.400450,-5.737124,3.292912,5.776534,-9.885354,-6.358726,-9.483460,9.936365,-2.578943,1.865033,9.821520,-4.506971],[5.017411,8.280381,8.157371,-3.323886,4.079560,-5.388994,0.247144,-8.526363,-4.402117,2.323363,1.675814,8.806683,-7.017980,8.271358,0.528203,-2.856625],[-6.379885,0.086039,-7.002735,-1.528834,-9.134316,-5.554101,4.065584,-1.452217,2.282622,-3.573592,-1.477331,-1.715714,-3.554460,4.841611,-2.102248,-5.842634],[4.680993,-5.174000,-6.381256,4.704527,0.569383,-7.528166,-2.070659,-0.239280,6.332999,3.709095,-5.924610,-3.004213,2.747656,-6.565327,-3.073108,-6.579632],[-9.910574,0.385277,2.086594,-2.629894,-1.788880,7.196360,8.541669,3.640218,-3.728030,-6.818176,-2.670787,9.060090,-0.948322,4.420671,2.550106,-1.363373],[-3.344153,-7.783504,-9.451854,-9.661383,3.547467,-1.438732,1.085871,5.558742,-6.496230,-6.615558,2.295090,-7.967304,-6.134749,-8.991300,4.994572,5.874340],[-3.506395,0.014778,-8.100057,5.859144,-4.932183,-4.450385,4.709901,9.717283,-3.741723,5.752058,-7.312024,5.584007,7.043967,-3.188413,9.670639,2.418622],[1.997394,-8.313567,-5.349256,1.143220,0.363178,0.760640,-1.980577,-4.577633,-0.658268,-9.071695,3.267093,4.899591,8.769442,3.957590,-0.035531,-3.744070],[-3.993603,3.003316,-3.439790,9.712967,9.302841,0.109141,0.778069,-4.177852,8.237533,-1.460474,-1.649543,7.695657,4.813485,-8.499688,3.145925,7.376514],[-4.434268,8.299176,-3.430070,-7.309400,9.724127,2.615856,-6.365878,-9.897579,-0.224690,-9.220868,5.093699,-1.382694,8.753857,-0.648944,0.197991,-3.900688],[-9.375309,-2.928199,-6.536197,-8.277558,-0.868543,-6.632900,2.589468,-1.015666,-9.023202,3.815040,6.151158,-2.574563,-1.616234,7.305507,8.050416,4.137789],[9.377046,-1.801140,6.654087,7.518988,-4.944760,-7.390705,5.011100,4.536983,7.841028,4.552832,-5.405266,9.829689,-5.964819,-5.241013,-9.925318,9.415504],[0.213776,8.166807,2.991094,8.136504,0.642801,2.398973,-0.391885,-2.772036,6.195446,-3.077002,9.890909,9.834270,7.446862,9.885088,0.256604,1.799998]],[[-4.907882,8.819413,-0.266353,8.779419,-5.481499,-4.132836,2.887599,9.549581,-9.332935,-0.653940,4.482700,4.207689,4.854421,0.169160,6.052086,-8.917321],[0.187592,3.366255,-2.397365,8.431060,-7.562664,8.302765,-1.464394,-6.680094,0.113048,7.142566,-9.614043,7.352781,5.151386,5.592561,3.740952,9.456758],[9.418677,-4.213475,4.038806,7.519602,6.564622,-2.323541,2.710675,-2.293486,4.795483,6.917405,-3.148180,-5.298620,0.023238,4.135980,5.860704,-2.666556],[7.076569,-0.605753,-1.330238,-2.146160,-2.501577,-3.178324,-8.846431,-1.514328,-8.155162,3.712653,-2.594995,-3.839513,4.832335,2.800805,-9.278415,-9.316897],[-0.454627,9.873550,-4.967293,6.634665,-7.100605,-3.377833,-3.279839,-9.051534,-0.494891,-1.326524,2.579245,7.065774,-0.388606,8.314965,-0.402892,-5.211477],[-7.932668,0.079636,-1.412039,-0.644358,-0.297279,4.605424,0.369171,5.916155,1.924780,2.239567,2.832856,-9.946302,5.592013,-2.063735,7.209922,-9.547941],[-5.825961,-8.033875,-3.336238,7.789892,0.235059,-7.475281,5.283472,-6.239006,1.093598,2.812775,-0.606473,-7.367881,-2.822969,9.222424,2.804104,4.535734],[-2.670112,-0.669957,-8.475312,3.564699,-1.897890,2.714627,-1.345525,7.405468,0.302418,-9.694939,-7.665878,0.776072,6.652682,-8.818263,-8.331843,6.395346],[3.971241,-4.829486,1.918079,4.359357,7.842059,8.906940,-9.348519,5.221696,-8.869547,-9.803026,-5.015921,0.498698,-3.062970,-1.781204,8.765611,8.672119],[-1.608461,7.811413,-2.735495,5.833770,5.083645,6.263233,5.101099,0.587061,-5.555739,-5.659061,7.004367,-2.424856,3.686388,-0.767133,-4.690909,3.636850],[4.041963,2.886127,4.381303,5.920148,1.876817,4.725634,5.200293,-1.155710,-6.586842,-4.594351,-6.141834,0.369811,-6.127720,9.383136,-0.777565,3.993177],[5.120067,5.793495,4.366166,8.547304,2.808365,-3.084548,7.164359,-0.782743,3.116227,0.517786,3.246257,-4.871539,-2.120756,0.024333,-3.635524,6.070875],[1.622752,3.311611,2.038385,3.822047,4.690069,-3.475254,9.848834,-8.693514,3.403764,-1.714011,-9.648161,-5.216773,-8.754981,0.402634,-1.462157,-4.580147]]], dtype = "float32")#candidate|8999|(9, 13, 16)|const|float32
uop_9000 = relay.log10(const_8999.astype('float32')) # shape=(9, 13, 16)
output = uop_9000
output2 = uop_9000
func_9004 = relay.Function([], output)
mod['func_9004'] = func_9004
mod = relay.transform.InferType()(mod)
mutated_mod['func_9004'] = func_9004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9004_call = mutated_mod.get_global_var('func_9004')
call_9005 = func_9004_call()
output = call_9005
func_9006 = relay.Function([], output)
mutated_mod['func_9006'] = func_9006
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8218_call = mod.get_global_var('func_8218')
func_8219_call = mutated_mod.get_global_var('func_8219')
call_9051 = relay.TupleGetItem(func_8218_call(), 0)
call_9052 = relay.TupleGetItem(func_8219_call(), 0)
output = relay.Tuple([call_9051,])
output2 = relay.Tuple([call_9052,])
func_9054 = relay.Function([], output)
mod['func_9054'] = func_9054
mod = relay.transform.InferType()(mod)
mutated_mod['func_9054'] = func_9054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9054_call = mutated_mod.get_global_var('func_9054')
call_9055 = func_9054_call()
output = call_9055
func_9056 = relay.Function([], output)
mutated_mod['func_9056'] = func_9056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3224_call = mod.get_global_var('func_3224')
func_3225_call = mutated_mod.get_global_var('func_3225')
call_9068 = relay.TupleGetItem(func_3224_call(), 0)
call_9069 = relay.TupleGetItem(func_3225_call(), 0)
output = relay.Tuple([call_9068,])
output2 = relay.Tuple([call_9069,])
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
func_8238_call = mod.get_global_var('func_8238')
func_8240_call = mutated_mod.get_global_var('func_8240')
call_9115 = relay.TupleGetItem(func_8238_call(), 0)
call_9116 = relay.TupleGetItem(func_8240_call(), 0)
func_3181_call = mod.get_global_var('func_3181')
func_3182_call = mutated_mod.get_global_var('func_3182')
call_9125 = relay.TupleGetItem(func_3181_call(), 0)
call_9126 = relay.TupleGetItem(func_3182_call(), 0)
func_5957_call = mod.get_global_var('func_5957')
func_5960_call = mutated_mod.get_global_var('func_5960')
var_9145 = relay.var("var_9145", dtype = "float64", shape = (26,))#candidate|9145|(26,)|var|float64
call_9144 = relay.TupleGetItem(func_5957_call(relay.reshape(var_9145.astype('float64'), [1, 13, 2])), 0)
call_9146 = relay.TupleGetItem(func_5960_call(relay.reshape(var_9145.astype('float64'), [1, 13, 2])), 0)
func_2056_call = mod.get_global_var('func_2056')
func_2061_call = mutated_mod.get_global_var('func_2061')
var_9156 = relay.var("var_9156", dtype = "float32", shape = (216,))#candidate|9156|(216,)|var|float32
var_9157 = relay.var("var_9157", dtype = "float32", shape = (3600,))#candidate|9157|(3600,)|var|float32
const_9158 = relay.const([[-9,-2,5,3,7,6,-10,8,5,7,-5,7,-9,6,-4,10,9,6,-1,1,10,-4,6,8,1,5,-4,-9,3,-3,-4,-10,-6,-10,-5,5,-10,-8,2,-2,-3,-2,-9,4,-8],[9,-9,-8,7,-9,9,-8,2,7,-1,-10,4,-5,-5,-5,3,7,-4,4,3,2,9,2,5,7,6,2,1,5,4,9,3,-1,2,-8,1,10,-9,1,-10,10,8,-8,-9,5],[2,-3,1,-3,1,2,1,-2,-2,6,3,-10,8,-10,-2,2,-8,-8,-1,5,-2,2,7,-6,6,3,-8,10,2,4,-2,7,-3,2,7,4,4,-5,-1,-2,-2,8,-1,-7,8],[-6,-2,-2,-9,9,-4,5,2,-1,-10,-1,1,4,8,4,7,-8,-4,-3,7,-10,6,10,-7,2,7,2,3,-7,-7,8,-2,2,7,10,-9,6,6,-5,9,10,1,4,-8,-6],[4,1,-10,-2,10,2,10,7,6,-1,-9,2,5,-3,-7,-9,5,-6,5,-6,8,6,-8,8,-5,10,9,4,-8,-6,8,-7,-7,1,-1,-9,-5,-10,8,-6,4,6,9,-7,9],[-3,9,3,5,8,-9,6,1,-6,4,1,1,1,-9,9,4,-6,-4,-8,3,6,4,7,-7,-2,6,-9,1,8,-10,10,1,-6,-5,3,-2,-1,10,-2,10,8,-9,4,6,-2],[9,10,-7,4,-1,-9,7,-1,-7,-5,-1,4,1,2,10,-6,7,10,2,-6,-4,-8,-7,9,6,-1,-9,6,3,-9,-3,3,-1,-2,10,6,6,-4,-4,7,6,-6,-4,-5,2],[1,7,5,-10,8,6,-1,-7,5,5,3,3,6,-4,6,3,1,-3,7,-5,1,-1,6,-7,-3,-5,6,6,7,3,5,-1,7,5,9,-10,-3,-5,3,10,-6,2,4,4,-7],[-5,4,-3,1,-4,7,-3,7,9,-9,5,5,7,-5,-3,9,-7,5,3,-7,8,-1,6,8,7,6,3,9,-3,3,7,5,7,3,7,7,3,6,-5,7,-2,-5,-4,-4,-9],[4,-1,9,10,7,9,5,-1,3,5,-7,-3,-3,7,6,4,-9,3,-4,9,10,-7,-1,-6,-6,4,-2,-8,-6,10,-10,-3,3,8,-9,-3,4,-4,10,-1,4,2,2,9,-6]], dtype = "int8")#candidate|9158|(10, 45)|const|int8
call_9155 = relay.TupleGetItem(func_2056_call(relay.reshape(var_9156.astype('float32'), [216,]), relay.reshape(var_9157.astype('float32'), [10, 360]), relay.reshape(const_9158.astype('int8'), [5, 90]), ), 1)
call_9159 = relay.TupleGetItem(func_2061_call(relay.reshape(var_9156.astype('float32'), [216,]), relay.reshape(var_9157.astype('float32'), [10, 360]), relay.reshape(const_9158.astype('int8'), [5, 90]), ), 1)
output = relay.Tuple([call_9115,call_9125,call_9144,var_9145,call_9155,var_9156,var_9157,const_9158,])
output2 = relay.Tuple([call_9116,call_9126,call_9146,var_9145,call_9159,var_9156,var_9157,const_9158,])
func_9162 = relay.Function([var_9145,var_9156,var_9157,], output)
mod['func_9162'] = func_9162
mod = relay.transform.InferType()(mod)
mutated_mod['func_9162'] = func_9162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9162_call = mutated_mod.get_global_var('func_9162')
var_9164 = relay.var("var_9164", dtype = "float64", shape = (26,))#candidate|9164|(26,)|var|float64
var_9165 = relay.var("var_9165", dtype = "float32", shape = (216,))#candidate|9165|(216,)|var|float32
var_9166 = relay.var("var_9166", dtype = "float32", shape = (3600,))#candidate|9166|(3600,)|var|float32
call_9163 = func_9162_call(var_9164,var_9165,var_9166,)
output = call_9163
func_9167 = relay.Function([var_9164,var_9165,var_9166,], output)
mutated_mod['func_9167'] = func_9167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3438_call = mod.get_global_var('func_3438')
func_3440_call = mutated_mod.get_global_var('func_3440')
call_9186 = func_3438_call()
call_9187 = func_3438_call()
uop_9188 = relay.acosh(call_9186.astype('float32')) # shape=(2, 7, 1)
uop_9190 = relay.acosh(call_9187.astype('float32')) # shape=(2, 7, 1)
func_8032_call = mod.get_global_var('func_8032')
func_8033_call = mutated_mod.get_global_var('func_8033')
call_9194 = func_8032_call()
call_9195 = func_8032_call()
output = relay.Tuple([uop_9188,call_9194,])
output2 = relay.Tuple([uop_9190,call_9195,])
func_9203 = relay.Function([], output)
mod['func_9203'] = func_9203
mod = relay.transform.InferType()(mod)
mutated_mod['func_9203'] = func_9203
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9203_call = mutated_mod.get_global_var('func_9203')
call_9204 = func_9203_call()
output = call_9204
func_9205 = relay.Function([], output)
mutated_mod['func_9205'] = func_9205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1753_call = mod.get_global_var('func_1753')
func_1754_call = mutated_mod.get_global_var('func_1754')
call_9211 = relay.TupleGetItem(func_1753_call(), 0)
call_9212 = relay.TupleGetItem(func_1754_call(), 0)
output = relay.Tuple([call_9211,])
output2 = relay.Tuple([call_9212,])
func_9232 = relay.Function([], output)
mod['func_9232'] = func_9232
mod = relay.transform.InferType()(mod)
output = func_9232()
func_9233 = relay.Function([], output)
mutated_mod['func_9233'] = func_9233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1324_call = mod.get_global_var('func_1324')
func_1325_call = mutated_mod.get_global_var('func_1325')
call_9242 = relay.TupleGetItem(func_1324_call(), 0)
call_9243 = relay.TupleGetItem(func_1325_call(), 0)
output = call_9242
output2 = call_9243
func_9250 = relay.Function([], output)
mod['func_9250'] = func_9250
mod = relay.transform.InferType()(mod)
output = func_9250()
func_9251 = relay.Function([], output)
mutated_mod['func_9251'] = func_9251
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9269 = relay.var("var_9269", dtype = "int8", shape = ())#candidate|9269|()|var|int8
var_9270 = relay.var("var_9270", dtype = "int8", shape = (2, 1, 2))#candidate|9270|(2, 1, 2)|var|int8
bop_9271 = relay.right_shift(var_9269.astype('int8'), var_9270.astype('int8')) # shape=(2, 1, 2)
uop_9276 = relay.acosh(var_9270.astype('float64')) # shape=(2, 1, 2)
output = relay.Tuple([bop_9271,uop_9276,])
output2 = relay.Tuple([bop_9271,uop_9276,])
func_9279 = relay.Function([var_9269,var_9270,], output)
mod['func_9279'] = func_9279
mod = relay.transform.InferType()(mod)
mutated_mod['func_9279'] = func_9279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9279_call = mutated_mod.get_global_var('func_9279')
var_9281 = relay.var("var_9281", dtype = "int8", shape = ())#candidate|9281|()|var|int8
var_9282 = relay.var("var_9282", dtype = "int8", shape = (2, 1, 2))#candidate|9282|(2, 1, 2)|var|int8
call_9280 = func_9279_call(var_9281,var_9282,)
output = call_9280
func_9283 = relay.Function([var_9281,var_9282,], output)
mutated_mod['func_9283'] = func_9283
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5031_call = mod.get_global_var('func_5031')
func_5032_call = mutated_mod.get_global_var('func_5032')
call_9395 = func_5031_call()
call_9396 = func_5031_call()
func_8666_call = mod.get_global_var('func_8666')
func_8668_call = mutated_mod.get_global_var('func_8668')
call_9410 = relay.TupleGetItem(func_8666_call(), 0)
call_9411 = relay.TupleGetItem(func_8668_call(), 0)
func_5849_call = mod.get_global_var('func_5849')
func_5851_call = mutated_mod.get_global_var('func_5851')
call_9416 = func_5849_call(relay.reshape(call_9410.astype('float32'), [2, 7, 1]))
call_9417 = func_5849_call(relay.reshape(call_9410.astype('float32'), [2, 7, 1]))
func_8617_call = mod.get_global_var('func_8617')
func_8618_call = mutated_mod.get_global_var('func_8618')
call_9437 = func_8617_call()
call_9438 = func_8617_call()
func_1691_call = mod.get_global_var('func_1691')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_9441 = relay.TupleGetItem(func_1691_call(), 0)
call_9442 = relay.TupleGetItem(func_1693_call(), 0)
output = relay.Tuple([call_9395,call_9410,call_9416,call_9437,call_9441,])
output2 = relay.Tuple([call_9396,call_9411,call_9417,call_9438,call_9442,])
func_9449 = relay.Function([], output)
mod['func_9449'] = func_9449
mod = relay.transform.InferType()(mod)
output = func_9449()
func_9450 = relay.Function([], output)
mutated_mod['func_9450'] = func_9450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9070_call = mod.get_global_var('func_9070')
func_9072_call = mutated_mod.get_global_var('func_9072')
call_9451 = relay.TupleGetItem(func_9070_call(), 0)
call_9452 = relay.TupleGetItem(func_9072_call(), 0)
func_3084_call = mod.get_global_var('func_3084')
func_3086_call = mutated_mod.get_global_var('func_3086')
call_9460 = relay.TupleGetItem(func_3084_call(), 0)
call_9461 = relay.TupleGetItem(func_3086_call(), 0)
func_4219_call = mod.get_global_var('func_4219')
func_4221_call = mutated_mod.get_global_var('func_4221')
call_9496 = relay.TupleGetItem(func_4219_call(), 0)
call_9497 = relay.TupleGetItem(func_4221_call(), 0)
output = relay.Tuple([call_9451,call_9460,call_9496,])
output2 = relay.Tuple([call_9452,call_9461,call_9497,])
func_9498 = relay.Function([], output)
mod['func_9498'] = func_9498
mod = relay.transform.InferType()(mod)
output = func_9498()
func_9499 = relay.Function([], output)
mutated_mod['func_9499'] = func_9499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4454_call = mod.get_global_var('func_4454')
func_4455_call = mutated_mod.get_global_var('func_4455')
call_9537 = func_4454_call()
call_9538 = func_4454_call()
func_9498_call = mod.get_global_var('func_9498')
func_9499_call = mutated_mod.get_global_var('func_9499')
call_9546 = relay.TupleGetItem(func_9498_call(), 0)
call_9547 = relay.TupleGetItem(func_9499_call(), 0)
func_9232_call = mod.get_global_var('func_9232')
func_9233_call = mutated_mod.get_global_var('func_9233')
call_9561 = relay.TupleGetItem(func_9232_call(), 0)
call_9562 = relay.TupleGetItem(func_9233_call(), 0)
func_7753_call = mod.get_global_var('func_7753')
func_7755_call = mutated_mod.get_global_var('func_7755')
call_9596 = relay.TupleGetItem(func_7753_call(), 0)
call_9597 = relay.TupleGetItem(func_7755_call(), 0)
output = relay.Tuple([call_9537,call_9546,call_9561,call_9596,])
output2 = relay.Tuple([call_9538,call_9547,call_9562,call_9597,])
func_9600 = relay.Function([], output)
mod['func_9600'] = func_9600
mod = relay.transform.InferType()(mod)
mutated_mod['func_9600'] = func_9600
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9600_call = mutated_mod.get_global_var('func_9600')
call_9601 = func_9600_call()
output = call_9601
func_9602 = relay.Function([], output)
mutated_mod['func_9602'] = func_9602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2077_call = mod.get_global_var('func_2077')
func_2079_call = mutated_mod.get_global_var('func_2079')
call_9605 = relay.TupleGetItem(func_2077_call(), 0)
call_9606 = relay.TupleGetItem(func_2079_call(), 0)
output = call_9605
output2 = call_9606
func_9617 = relay.Function([], output)
mod['func_9617'] = func_9617
mod = relay.transform.InferType()(mod)
mutated_mod['func_9617'] = func_9617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9617_call = mutated_mod.get_global_var('func_9617')
call_9618 = func_9617_call()
output = call_9618
func_9619 = relay.Function([], output)
mutated_mod['func_9619'] = func_9619
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4663_call = mod.get_global_var('func_4663')
func_4664_call = mutated_mod.get_global_var('func_4664')
call_9628 = relay.TupleGetItem(func_4663_call(), 3)
call_9629 = relay.TupleGetItem(func_4664_call(), 3)
func_2210_call = mod.get_global_var('func_2210')
func_2212_call = mutated_mod.get_global_var('func_2212')
call_9644 = relay.TupleGetItem(func_2210_call(), 1)
call_9645 = relay.TupleGetItem(func_2212_call(), 1)
output = relay.Tuple([call_9628,call_9644,])
output2 = relay.Tuple([call_9629,call_9645,])
func_9653 = relay.Function([], output)
mod['func_9653'] = func_9653
mod = relay.transform.InferType()(mod)
output = func_9653()
func_9654 = relay.Function([], output)
mutated_mod['func_9654'] = func_9654
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1899_call = mod.get_global_var('func_1899')
func_1901_call = mutated_mod.get_global_var('func_1901')
call_9662 = relay.TupleGetItem(func_1899_call(), 0)
call_9663 = relay.TupleGetItem(func_1901_call(), 0)
output = call_9662
output2 = call_9663
func_9667 = relay.Function([], output)
mod['func_9667'] = func_9667
mod = relay.transform.InferType()(mod)
output = func_9667()
func_9668 = relay.Function([], output)
mutated_mod['func_9668'] = func_9668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8617_call = mod.get_global_var('func_8617')
func_8618_call = mutated_mod.get_global_var('func_8618')
call_9717 = func_8617_call()
call_9718 = func_8617_call()
output = call_9717
output2 = call_9718
func_9726 = relay.Function([], output)
mod['func_9726'] = func_9726
mod = relay.transform.InferType()(mod)
mutated_mod['func_9726'] = func_9726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9726_call = mutated_mod.get_global_var('func_9726')
call_9727 = func_9726_call()
output = call_9727
func_9728 = relay.Function([], output)
mutated_mod['func_9728'] = func_9728
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9973 = relay.var("var_9973", dtype = "int64", shape = (2, 3, 6))#candidate|9973|(2, 3, 6)|var|int64
var_9974 = relay.var("var_9974", dtype = "int64", shape = (2, 3, 6))#candidate|9974|(2, 3, 6)|var|int64
bop_9975 = relay.bitwise_xor(var_9973.astype('int64'), relay.reshape(var_9974.astype('int64'), relay.shape_of(var_9973))) # shape=(2, 3, 6)
func_3017_call = mod.get_global_var('func_3017')
func_3019_call = mutated_mod.get_global_var('func_3019')
var_9987 = relay.var("var_9987", dtype = "float32", shape = (140,))#candidate|9987|(140,)|var|float32
call_9986 = func_3017_call(relay.reshape(var_9987.astype('float32'), [2, 7, 10]))
call_9988 = func_3017_call(relay.reshape(var_9987.astype('float32'), [2, 7, 10]))
func_150_call = mod.get_global_var('func_150')
func_154_call = mutated_mod.get_global_var('func_154')
const_10000 = relay.const([[6.340914,2.547923,0.162299,9.822712,-7.814190,1.847489,-4.465274,2.110597,9.852957],[-8.124409,9.367333,-7.527266,-0.208309,5.147058,-7.195132,-0.795359,-8.222225,2.168219],[2.786615,-3.578615,2.496809,5.701676,0.363495,3.832087,-5.621761,8.591887,3.157136],[5.306529,1.788460,3.976777,-2.449910,3.023813,8.781862,9.433557,2.477437,-9.380515],[1.018751,-0.626394,-4.703707,7.672890,9.708571,-4.188497,8.863817,1.211260,6.591339],[-7.751189,-2.804517,-2.559050,-4.820472,5.364466,6.457545,2.382721,2.219102,4.364275],[8.775881,4.089924,-2.092798,-9.184875,0.293568,-0.581624,-9.982080,-8.856912,8.761158],[-7.168549,-0.358436,5.930926,7.439843,-8.134115,2.063230,-8.182434,5.712365,4.074566],[0.231542,8.599237,6.492197,4.965422,-7.134501,0.338689,-7.800983,-1.223727,5.800643],[9.008037,-2.872794,7.091036,9.000261,-9.313740,8.180917,-8.570168,4.697969,6.082989],[-1.246320,-1.231203,1.955596,-3.193112,1.044588,-4.125463,-5.185882,5.719406,-5.527622],[-4.571019,-4.261778,-7.786209,3.887398,8.396620,-5.996185,4.257928,7.496857,2.387548],[5.359917,6.895686,-8.107424,2.164084,1.613664,9.361338,-5.129242,0.560540,0.586924],[-9.749925,9.666649,9.558083,5.430094,-5.554491,7.899351,0.466609,9.979085,1.028657],[-2.850810,-2.553873,-8.781508,9.930969,-7.264207,7.494448,-6.492897,-1.040584,8.908096],[3.671144,-6.438302,-6.256114,-0.818318,8.772574,-7.720002,1.442362,4.798762,-0.763579],[-4.299156,-0.103560,-6.512181,-5.041217,-8.344487,-2.808746,-3.806407,-2.357681,3.795629],[-2.087707,-0.894654,0.615443,3.300158,7.520639,7.142340,-8.730169,-6.757143,-7.267917],[-8.393188,0.665988,9.433766,3.380014,-6.288600,-4.289365,-7.551280,7.341527,-7.225240],[8.714953,0.274233,2.370875,-4.368102,-9.428706,-0.825129,8.336320,2.748507,6.870835],[6.787022,1.731942,-1.658317,8.382653,-3.879936,9.122902,-2.608687,-5.283640,-1.678177],[-1.918922,3.504008,7.481791,0.525618,9.590662,4.106621,5.754564,4.939099,-0.275438],[-5.330807,-1.870081,-3.354144,-6.048208,-3.691188,4.194585,-0.560761,4.247872,-4.489270],[4.540089,7.580040,8.794567,-2.860957,5.674037,9.538475,0.072299,-6.494864,-3.443956],[-4.199929,6.497895,-8.724416,1.093159,-0.837368,-1.561780,0.883894,-3.100441,-7.590912]], dtype = "float32")#candidate|10000|(25, 9)|const|float32
const_10001 = relay.const([-7.896652,3.548391,3.066456,9.773557,-5.793429,-9.513523,-5.199113,-8.188666,9.322554,-1.266297,-4.132910,-4.918038,0.603285,-5.840715,4.127179,7.919651,-8.688583,3.724651,-2.745440,9.541171,-2.245391,-3.190726,-8.567415,-4.715378,4.718593,-4.452895,-1.898466,-7.104713,0.575492,6.640329,6.954771,4.755521,9.635955,-4.367455,8.671317,-5.985943,5.942995,3.237275,-9.237821,-0.647551,-7.707231,9.614075,9.734218,-7.678792,-1.936033,7.018063,6.661604,1.551993,5.382736,-5.379420,4.708525,4.662930,-6.395543,2.714715,-4.629111,-7.972123,-1.515145,-9.790043,-0.952193,-0.827729,-5.212058,-7.689576,-2.907026,-9.062062,5.861183,6.596688,8.379672,-8.478444,6.600253,-9.931571,7.576002,-3.304014,-5.033002,9.467647,-2.885930,0.065566,5.535485,-1.194827,0.600735,2.910423,1.101166,-1.885705,8.876159,-1.682266,-0.590007,3.404455,-8.134167,8.416714,-6.691941,7.800531,-8.545122,0.384704,-6.992089,-9.655782,-2.007176,1.633086,-9.799365,-5.639577,-3.487291,-8.528819,-9.194765,-2.106268,7.620348,1.916613,-0.371862,-0.142053,-5.531698,-4.826336,1.761073,-8.560951,-8.164999,-7.768184,4.828118,5.288071,6.754005,-4.584353,7.084363,-8.944642,-2.147948,-3.891689,-5.641905,-2.707608,-2.522340,-7.721317,3.596886,5.767085,-9.606468,-9.487770,-8.200434,3.349874,6.286321,4.085929,-9.361644,9.518845,-7.228495,5.875553,0.150087,4.837506,-4.994895,1.434435,-6.413108,6.739544,-8.591782,8.815159,7.577485,7.401480,-6.868578,6.507686,-4.743254,-1.582681,-9.385363,-0.362054,9.524222,6.260714,0.011355,7.142154,9.472171,-7.032066,-2.663757,2.016347,-1.367887,-7.686618,8.870422,2.112687,-2.629969,-6.194579,0.922470,-4.930381,-3.345546,-2.609558,5.655632,-4.363994,-1.388033,-9.600603,-2.552613,7.048020,-3.216880,7.442493,6.572992,-1.109177,-0.219850,9.866313,8.514100,-8.213061,9.724162,8.959206,-0.145738,-2.485492,-4.721552,5.648421,-2.211313,8.880011,-2.588524,-7.579469,0.706866,-1.469252,-5.052059,0.600483,4.947451,5.846581,-8.474806,8.026693,-0.328649,9.538249,3.409853,1.418761,8.951989,-3.196162,-1.010802,-9.756513,6.992907,3.950812,-1.599988,8.232603,6.144536,-6.161953,8.027849,-0.312831,8.307266,-6.350609,8.320022,-4.762622,-7.551430,-3.129036,-3.143002,-1.155640,4.368852,9.337588,-6.829367,-7.265833,8.316020,9.661817,-6.234688,7.583144,-3.858596,-8.857032,3.345273,-0.485766,-5.440926,-7.939926,4.012387,-5.047882,7.137131,-9.637869,1.691437,7.423731,-0.742827,9.162930,-7.336962,-8.256426,2.181931,-1.032127,-4.636645,-7.708818,-1.739867,0.504550,-4.294503,-6.781663,1.210275,5.741416,1.584205,9.206996,-3.330816,4.126642,2.959560,9.968071,-5.777528,-5.565812,-9.251657,4.455139,7.225134,9.663275,3.612156,9.470944,-3.985380,4.991102,5.937643,1.323921,1.855242,7.926768,5.042263,1.437143,-7.472996,-7.960262,8.761033,2.281293,-5.223503,-9.007943,9.403645,-2.564963,-8.299313,2.069005,-1.738016,8.792756,7.504769,4.046841,7.026412,0.027648,-4.552653,2.149035,6.426452,-0.560775,9.607784,4.018868,7.679878,-8.503941,5.403654,1.018555,4.683216,-7.692717,0.832704,1.351101,-0.856893,4.421537,-4.323010,-0.506702,8.128970,6.418933,2.569617,7.385270,-8.423466,7.567514,-9.109198,5.697843,1.074865,-9.657960,2.095971,-0.271932,-3.764020,-4.175682,-2.809608,4.808751,-7.121633,-0.649722,7.672776,-3.724766,8.969645,-3.326598,-7.087844,0.769116,1.503334,4.198659,2.123539,-6.600695,1.259980,-4.012939,-2.167365,0.143729,-4.741316,-4.685006,-9.754489,1.108216,-5.717279,2.159703,-5.078621,9.969751,-3.323398,-5.346045,-8.895524,-9.762266,-2.050237,9.649838,-8.681248,8.400461,-4.297501,-0.404050,-5.595907,-6.647860,2.579441,9.071676,2.181266,9.968313,9.380097,7.453485,0.363018,0.588967,8.575167,-4.180346,-6.762350,-5.943402,7.746713,2.505438,2.329340,6.535772,1.593123,-9.537740,9.984861,-0.971208,9.969914,-7.295831,3.882080,-5.865883,-8.066968,-0.628368,-4.078712,6.200949,-9.091194,3.772944,-7.580888,-1.586955,-6.916011,-5.209365,8.472643,-2.149250,2.687207,8.551863,2.362958,6.083040,-4.082780,-0.002394,-9.284632,-1.621356,-1.482563,-6.911134,-9.134092,-5.422665,0.487454,-0.505941,8.963641,-0.808257,8.827441,-0.139917,4.004250,-8.857479,9.880971,9.872390,-7.626526,-7.851293,0.284348,-6.735559,-1.776563,-8.581238,7.308269,-2.038893,-7.924425,3.983278,-7.175680,-9.990338,2.349887,6.298639,6.203340,6.960712,-6.844584,-1.449955,-9.376587,-1.984213,1.049130,4.045890,4.514790,9.046833,-8.703730,-2.365450,-9.404191,-0.327119,3.659698,3.728350,-4.443901,8.526126,-7.171076,0.718603,-3.398914,1.755200,-7.233151,-6.404804,-4.234799,8.305073,6.372957,5.420461,-2.130761,7.547764,9.205259,-8.178031,7.569091,8.642143,7.995932,6.140241,-4.877221,1.557208,1.147603,-3.127980,-4.025277,-9.331400,0.566351,2.550334,5.924993,-1.917729,0.955142,2.304805,-8.133604,9.325486,9.252023,4.199092,8.536229,-5.688860,-6.191450,6.038620,4.721632,-4.575036,7.154685,-4.751986,0.965509,-0.807209,-0.253156,7.903765,-6.132195,-4.141847,1.439089,6.918607,0.390169,4.792114,-0.811225,-6.691504,-8.624558,6.113371,-8.462555,1.791632,-1.377835,2.237732,2.844267,9.200946,2.854976,8.198793,5.234229,2.300315,-9.921361,-7.481418,6.326873,-8.999495,-5.294145,-2.989955,-4.189203,-8.822876,5.044397,7.005863,-3.219021,-2.325109,-4.789240,7.452472,-9.111559,-3.165135,2.504701,8.028579,6.939685,1.035299,8.495515,9.814005,0.058104,-8.192024,2.223071,7.496053,-5.256564,6.088601,0.755753,-0.482917,3.132656,-0.150837,-3.152643,-8.591698,-9.656311,9.761957,4.588475,8.531230,-6.063571,9.864385,5.372448,5.187111,-5.282229,-8.772884,9.986564,4.028883,-5.904851,-7.929462,4.188899,-3.699623,-0.407461,-0.334394,-3.461119,-1.345216,7.347695,-6.843739,-8.678763,5.317765,-2.085490,-9.601622,-5.956442,9.977891,7.509485,7.180346,-8.816300,-1.474236,9.078043,-8.865453,-0.614689,-8.985892,-6.738898,-7.848772,9.452327,3.101659,-2.496251,9.193450,8.493143,9.104646,-4.551183,9.785973,-8.167813,4.606515,-3.932063,-1.693326,-0.628929,2.398531,2.493339,3.794452,0.947537,2.462976,-5.504279,-7.767167,1.295467,3.506631,1.385514,-2.510663,-4.635768,4.015553,9.714210,-6.664351,6.803809,-0.350297,7.825515,2.189303,-1.677509,-2.707408,8.492954,-7.408900,-2.778311,2.571670,-5.201250,-1.762822,3.470911,-3.413857,7.822549,0.219756,-6.714456,1.642736,3.595017,-4.291240,1.174881,0.602811,9.069909,3.596842,0.759629,6.073593,-0.718946,-8.992953,-0.996039,-4.049039,5.938854,-0.286768,8.636570,-2.205140,-9.246605,-3.254349,3.559240,-8.743458,1.283684,5.672114,-5.624110,7.617469,-7.373034,9.415226,-6.183110,-9.598842,2.763499,8.033998,-3.161830,3.970480,-7.237999,8.633216,5.064295,-0.291422,4.361208,7.315473,5.067264,7.467461,4.293197,-2.384103,-5.479128,8.732532,7.291892,9.952582,-1.068464,-7.686225,-1.871285,4.787942,1.186951,9.863696,0.867300,7.709022,6.701395,-6.683748,7.762915,-1.263753,5.857152,8.622466,-3.361944,-6.619931,2.729385,9.820673,-5.628167,-6.545284,-3.755719,0.976099,-7.130753,-0.443723,7.058381,-9.538660,1.725843,-6.527565,9.499547,6.098803,-5.591141,-9.662446,-0.362934,-6.223614,-6.419773,3.137127,-9.075699,-0.861894,1.748290,-5.847541,5.692514,0.682543,5.309679,5.900841,4.756913,-1.910024,0.166321,6.763993,-2.941102,-3.597767,-8.333636,4.765085,-2.288682,-8.575076,1.720364,-3.388853,8.069908,8.450732,-0.765998,8.298371,-8.728809,1.536905,6.367790,4.954315,-2.787800,-1.115601,6.689522,6.065446,-8.554560,6.775389,-5.582461,-5.220981,1.051743,-1.154325,6.759902,2.456863,4.793030,8.957553,-2.093430,-5.379530,-0.551577,8.039507,5.385136,-9.606466,-8.331611,8.281904,8.669254,7.636356,0.115547,-5.871510,7.716919,-0.961095,0.262985,9.829711,2.109102,-4.895860,4.143946,6.884920,1.868637,-9.576670,-9.075908,-4.073611,5.913051,-7.148583,-6.566121,3.586926,0.187386,-2.865111,2.669532,-3.153083,-8.634229,3.358685,-7.602593,-3.343309,-1.786868,-1.932487,-6.944952,-5.267415,-8.001858,-1.071005,-2.793270,-7.680801,-2.599880,-5.131104,2.353338,-7.687267,7.328573,4.703440,-1.882163,6.187825,-4.000673,6.035258,4.729543,-7.989565,5.003548,-6.646363,2.086254,5.629787,9.192279,5.299309,-3.683852,-2.942622,5.765034,5.227012,0.161669,-3.166391,-5.002704,-6.278069,-7.884333,0.489688,-3.430520,9.794882,1.056323,1.068754,-1.335824,2.277091,-4.119334,-4.579980,0.346501,3.944760,5.514856,-2.922084,-4.072322,2.389535,9.342105,-7.384762,-7.047249,6.506219,-5.312511,-0.437941,-5.989090,2.697276,-2.225446,-0.078790,3.308242,-0.710516,-2.830772,7.014996,-3.628970,7.266317,8.361243,2.012143,1.858062,9.348374,5.777427,-1.693107,2.210630,-5.296541,4.099127,6.407843,-1.017818,0.281669,-7.428509,7.304266,5.733419,6.730114,-0.287958,-3.577598,3.984384,4.683731,-9.129852,-8.731346,9.018990,2.911217,-5.210499,-9.171184,-3.328684,8.472746,-1.779549,0.482778,4.468126,-1.696895,7.046191,3.637987,8.484495,2.191522,-1.710275,5.714814,-5.147180,-0.113079,-0.808635,-1.059057,0.665305,5.128344,-3.577672,8.930072,7.592603,-5.722824,9.389139,-2.500741,-8.783816,-9.449359,7.116459,7.842032,-6.587432,-1.753651,-5.560279,0.980892,-8.007588,4.725416,-9.679001,-1.969184,-2.507258,-3.588963,-3.370200,-1.215887,3.985460,1.955273,9.625145,-6.763623,8.260710,-8.320736,1.915245,8.065932,-1.325493,0.442130,6.137927,0.429900,-0.373016,5.443256,-4.300344,7.304038,-7.072273,-0.401223,4.407167,8.721674,-4.857433,-2.670699,-4.706631,5.874979,-0.751478,3.539311,9.748749,-3.620856,-0.421860,-9.084737,9.277597,-1.758236,8.973051,6.413539,-9.412214,1.843865,-7.188131,-8.976655,8.813528,-4.961202,-2.655048,4.911721,-1.346269,4.671763,-4.059066,8.217240,-9.379369,5.887477,-7.848910,-0.051150,-1.590012,6.895838,-9.449134,0.827760,-5.776725,1.741112,5.919108,-9.801303,-1.495979,-1.138412,5.954694,4.164388,-7.495058,3.752650,4.459220,5.160398,1.146641,9.572748,-0.437086,8.855002,-2.901612,-4.706839,-1.998912,7.680088,-5.174322,7.091485,0.148563,8.690963,0.466360,-5.693140,8.403848,-9.800665,5.755179,-9.323238,-6.237274,-6.158376,-3.991668,-6.971903,7.247499,-1.095989,-8.863329,8.288648,-0.018522,6.994765,-6.796961,-7.053542,9.970545,-0.495976,-3.263726,-0.208721,7.412107,7.922330,2.038913,-1.608295,8.627592,0.814690,-4.225872,7.519919,4.762707,-5.721323,5.863180,7.825993,-3.805626,5.369698,-8.777260,9.665770,-9.756641,-3.975169,3.337439,-6.067566,2.498616,-0.346302,-6.102873,-2.808252,-6.958591,1.768764,1.964269,-3.811399,1.882251,1.054308,1.464254,0.114725,6.142819,-5.589463,-7.921603,-3.070217,-8.813311,7.781970,-3.153385,-7.211581,-5.406738,-5.994747,2.907574,4.353004,-0.699583,-4.776933,-1.610881,5.915408,6.234040,-5.656072,-0.251294,4.470050,0.913305,-8.606478,-6.951275,-7.166287,-8.635372,8.209692,3.068553,-4.456062,8.502191,8.333036,-7.510015,0.387600,-0.169631,5.283584,-1.719379,9.871872,5.213971,-4.384882,8.070069,8.034231,6.979653,1.621659,1.328390,6.867782,-9.852738,-2.474759,9.223317,7.619215,1.816569,2.900280,3.160288,0.930468,-5.948998,5.856852,-5.388502,8.635267,5.953179,-8.842550,8.054795,0.690866,7.426503,-3.130394,2.377044,-9.337447,5.192278,7.563873,1.258738,4.835401,-9.064696,8.440116,8.460607,-8.872736,0.519920,-2.976110,-7.645819,-8.292213,1.937925,2.227170,-4.332779,-7.082764,0.163358,0.397030,-8.662356,-4.046053,3.531489,-6.312626,-2.281252,3.511312,0.269808,-6.312264,4.665558,6.672354,-5.270594,1.052916,1.812485,-8.048131,0.264039,0.924858,-0.387186,-0.700949,4.577455,3.000568,-0.845776,9.232484,-7.589649,9.992060,-2.598647,-0.018589,0.214682,-5.302122,2.222279,0.567722,-4.064042,3.566531,-2.144049,-7.815090,-7.864033,-7.135934,-9.248125,-5.177530,5.463267,-6.478806,8.345115,-5.405180,-4.376472,1.791583,8.000801,2.873306,0.172068,3.704129,-2.960281,9.492810,6.022107,9.958998,0.279759,-5.672384,-2.404993,-4.054637,2.860055,-1.449410,6.535636,-6.779108,4.996950,-2.514998,-3.762607,-4.192533,7.723117,8.598463,7.349768,-5.560893,-1.405094,-3.180705,9.962609,-3.157059,3.833462,3.362250,-0.719745,-5.206683,6.711447,-5.172795,-3.550996,-5.505278,-0.759194,-7.292616,8.351587,-7.423198,6.715778,-9.615955,-9.034371,1.531445,8.969733,-1.623871,-3.374182,8.573567,-5.823983,6.969723,7.751565,-4.268547,2.469735,2.548426,-3.285099,5.068455,-0.687472,-5.387173,-5.637547,1.795558,-5.108295,-2.818754,-4.689113,-1.249103,6.270002,0.389901,-0.751717,5.092201,-4.126055,-4.596506,-6.641765,-3.445439,3.514338,6.769464,-5.710117,3.071432,9.579596,-4.255133,-8.743203,-7.227055,-5.748270,-9.608481,0.760619,9.898145,-3.571595,-3.507599,4.908470,-9.167172,-9.887515,-0.727109,-1.443230,4.310621,0.700335,6.048025,0.467006,-0.052631,2.705822,-2.851540,-2.563292,-0.048517,1.664301,8.696809,0.622571,2.293815,-4.864191,-4.941827,9.110621,-7.364262,6.102293,-2.050966,5.233544,2.438926,7.794192,4.689728,2.374590,1.758710,4.221184,8.287981,-2.421317,-4.771344,-9.997713,3.195890,-0.811465,3.307909,9.041565,-0.645071,-7.815499,8.346642,9.277603,7.384440,-3.704741,5.237963,7.767982,-1.106571,4.240952,-8.736106,6.421797,-4.322984,8.814444,-6.551511,4.496674,0.317089,-7.006331,-4.609190,-7.647634,-8.799124,-5.165920,-0.085437,-8.317211,2.317477,4.112858,3.084999,3.073736,-8.283454,4.949883,4.851421,-0.044884,-7.405775,0.817647,-8.594504,-4.439778,-7.481957,2.610955,7.165814,3.612319,7.180187,-1.534577,8.092602,-1.259961,2.801284,-8.537828,0.430964,3.451535,3.283178,-4.320290,-7.664854,-6.390353,0.966640,3.932387,5.072662,5.794619,0.566241,-0.024027,4.774366,1.634709,-5.899930,4.744828,-8.998053,-9.332873,6.948920,0.630630,1.267986,-1.830289,2.767546,2.608920,-7.397397,-1.614312,8.627934,-6.641879,0.243800,2.764147,-6.781459,7.224503,8.480194,-1.554951,-6.001820,7.667097,-2.975952,-6.607534,7.894343,-8.587755,-6.750456,-2.497396,1.203657,-6.519389,-7.267338,8.561318,-4.933457,3.795252,-3.639676,-9.071332,6.286235,-2.284169,8.807882,-8.237330,2.831726,-5.798364,7.941982,3.724657,-7.349607,3.337567,5.657007,9.991562,-7.218494,1.315045,-6.098339,3.447610,2.691920,5.786256,2.083397,-9.963134,6.838033,-3.102511,9.233294,4.591355,-4.669058,-7.382751,2.707020,0.113393,-4.647291,-8.887505,9.927879,-7.113305,-6.018684,0.826257,7.187577,-1.659137,4.797766,0.249000,-9.634291,-7.360031,-3.009365,-5.678700,-7.018358,0.902019,-3.426673,0.841301,4.378513,4.490439,-7.245610,7.032365,-0.539179,-3.140302,4.435274,-7.674506,-3.848939,-2.748731,8.088038,7.405214,-3.053534,-1.803827,-1.125357,-5.185619,9.976962,2.319486,7.989928,-1.643231,-6.568312,4.939171,-6.257419,7.378356,-9.436401,9.303528,-9.252531,0.980861,7.259976,-0.086737,4.528199,-0.725318,-1.218411,-6.337655,-8.586906,1.841772,6.440524,-3.318723,-1.128043,4.427255,4.756533,-9.676765,6.939202,2.398425,6.659758,-7.903408,-4.447846,3.903542,5.434745,-5.657062,-9.699818,-2.163849,-2.993799,-5.293584,1.604491,4.762507,-0.218745,-3.601319,9.385956,6.646221,1.799335,-1.028925,-5.881360,-2.615368,0.632376,0.021765,-3.102166,-0.877069,4.898373,0.465868,-5.080128,6.095968,-8.071233,-9.647648,6.062738,-3.577831,4.179377,6.747900,0.662933,3.990745,-4.194250,-8.860343,2.502790,-1.172323,1.135095,4.162710,-7.918905,5.419678,-4.973514,3.142504,9.887542,8.499123,-6.092485,-5.295018,-1.751897,-0.986986,-4.414339,-6.379077,8.362874,-0.071683,-4.547749,-5.985724,2.461882,-7.346505,5.385769,2.141446,3.801658,-0.669719,0.442495,9.946426,-5.569386,3.652188,7.074498,-9.071970,-5.463019,2.512790,-0.465139,2.352403,1.208804,-7.415752,0.505624,4.560006,-1.221380,-7.351860,-8.773002,0.241327,-1.536039,-9.254625,-8.310544,-8.158745,7.031398,-2.903570,-6.652479,4.957528,7.286879,-2.061807,-2.803690,5.837407,4.835702,-9.552376,-5.591217,0.682751,-8.702249,-0.202460,-2.299950,8.661827,-0.929599,-5.351967,-5.436809,7.034256,1.021415,-4.590913,7.436065,-1.584734,-8.400635,5.446604,-7.640541,7.532678,-5.686519,-5.136242,-6.194451,-5.736803,8.833679,2.990300,9.682736,0.560857,6.680021,-8.791330,2.783101,9.837236,0.564736,-9.216718,8.035186,5.710151,6.480179,6.857864,9.268458,3.633730,-7.866053,-6.682568,6.304649,-3.925481,-2.258381,7.667207,5.832446,5.377654,9.786242,-5.184455,4.266493,-0.409002,3.600040,-4.769023,-0.951440,0.509433,6.726641,-5.605257,9.750778,5.054026,1.499487,-5.594194,7.478464,5.012685,6.717485,-0.320055,9.929315,-1.019603,-2.714881,-5.883807,-3.858572,1.009705,2.346164,-9.046765,-4.184318,-2.671660,-9.196100,-3.569401,-3.991425,9.656400,3.963246,-9.314136,-6.188716,-2.383166,-2.025644,1.090803,-8.890331,-9.841034,-3.684881,2.651390,-8.262925,-2.704183,-1.744483,-6.440783,4.558475,-3.987572,2.934463,8.172122,4.544644,-7.254186,-9.100202,-0.391343,-7.773726,0.034942,8.972754,2.097819,-0.706013,6.405295,-3.350830,-4.700751,2.772452,1.956575,9.527901,-4.586738,-7.132409,-9.621013,8.599788,4.354280,6.491689,-0.442459,8.818985,-9.456267,-7.482760,-5.809529,-3.517541,-9.716997,-0.013922,-6.778211,-8.243247,-6.831004,-3.754219,-5.043203,-0.701750,1.119126,-4.173235,-1.740151,-5.866714,0.843158,-2.768460,2.196445,-5.600833,-0.292687,2.632956,3.498745,-9.271175,-2.055006,-9.686653,-3.693841,8.870453,9.955927,2.822038,1.045023,-5.080239,-0.389679,7.089636,8.038647,7.305198,-4.153942,4.812637,9.066402,6.422940,-6.841189,-8.563832,-6.031352,-6.002976,4.233933,-0.018855,2.484873,0.850948,4.013246,-1.161271,7.853773,7.547417,-4.508344,7.261386,-6.295921,-7.292066,-7.606862,5.703147,-8.817926,-7.848568,5.110636,-7.644250,-2.172458,9.811521,-2.991347,-3.348861,5.506494,7.384142,-4.797650,1.032777,-1.016821,2.978892,-2.717331,5.195482,9.949122,-2.732500,-6.494476,8.963825,6.233911,7.941585,-6.668380,7.730770,8.699416,-6.236574,7.927489,-2.713901,4.162037,-0.829201,-0.626477,-3.779633,-8.352611,-6.730935,6.450081,5.891303,-7.787621,4.964728,-2.061751,0.591916,2.746979,-9.479935,5.836033,-2.919802,-0.165249,2.637972,9.174423,-4.792571,-1.032767,-0.277601,6.663376,-5.894215,-5.712081,-3.911901,-3.037081,-7.503085,2.075527,-1.896962,9.530675,0.106565,-6.419568,-1.630768,-3.720816,0.513781,-9.223704,0.134216,9.940104,9.952109,2.160989,-9.715728,0.461145,0.858285,8.877430,-4.783893,8.985995,4.729698,-6.334325,1.869101,-7.284347,1.099898,-9.492082,-3.115427,5.978818,-2.717094,-3.299373,-0.818770,5.979288,-3.081643,-9.242848,-3.785099,6.127897,0.181431,7.115616,-0.588331,6.554141,-1.674531,-3.429472,1.682759,6.666418,-9.782111,-5.953874,6.421087,4.496476,5.408576,-9.501332,1.290458,2.059985,4.819308,1.509614,-4.259866,-6.323489,-3.318847,-0.134422,-4.704841,5.930618,7.307530,8.246961,-9.445117,-7.815641,-0.474264,1.119297,-4.945038,-7.142383,2.589715,-7.021774,-7.427751,9.326318,5.058090,-2.505955,5.648744,0.915078,-1.582724,1.912431,3.928050,-4.814875,6.235528,0.006529,-6.333184,4.944351,2.937907,5.801173,-1.445341,-2.588890,-3.805008,9.271267,0.397126,-9.704820,-2.218631,-4.659603,-5.951720,4.648942,-2.918815,8.020472,6.656085,-5.504342,-4.175057,-2.541514,-2.006389,5.041922,-8.186193,-3.139275,3.141879,5.567774,6.336909,2.279117,-8.328965,9.700729,0.983034,3.372513,2.547746,9.685665,9.347401,1.254209,-3.256903,5.538083,8.540906,-7.804971,-6.637008,-2.901283,2.618299,2.623009,1.772606,-7.139522,-6.240879,7.805994,-0.072164,1.021278,-7.367110,3.861140,3.947906,5.745951,9.335317,6.195095,3.102445,3.599030,0.242507,-8.308065,5.489865,1.358289,-9.209170,6.406176,2.988954,1.409820,5.308577,4.507828,9.575297,-1.873028,-2.701357,-6.404609,2.631519,9.633393,7.204228,2.917161,-5.319405,-0.680075,7.282460,5.867337,-4.581925,9.670727,-2.964569,4.083478,4.606098,-0.250448,2.109648,-7.036371,-7.770787,-6.869116,4.289053,-5.645766,-4.471793,8.257304,-7.256963,6.131337,9.591533,8.065615,3.082263,6.703802,-1.126297,-2.037950,-8.138981,-9.231652,-1.594913,-3.715320,5.182780,-0.872263,7.506754,3.589838,-0.050134,9.127063,7.241524,0.446363,2.554805,-7.153604,-0.342102,3.766949,1.879408,6.595099,-7.636186,4.393919,-3.882655,-5.868928,2.603573,-7.048639,-4.834210,8.568288,-2.929025,-4.261363,8.567468,3.456432,2.697111,5.982010,-4.409031,4.196197,-7.585939,-1.620070,-1.560332,3.343128,6.039550,5.956301,1.397864,7.936424,-3.823931,4.779007,-8.736488,0.297726,1.331346,-7.365318,-6.787052,1.212783,1.604195,6.146615,-1.646147,2.918388,-9.341780,5.888819,-3.370052,8.419797,-6.866536,-8.856060,9.805299,-8.096709,-2.531556,6.675123,-5.884650,-8.551900,-8.752363,1.065757,-0.818225,-3.942374,-7.074641,-1.990115,4.739973,0.697664,-2.267039,-8.625038,2.006692,-3.741188,-7.900607,-5.510788,-4.692074,-1.256019,3.196857,1.927384,-4.182022,-1.389763,7.045311,7.611050,9.998830,-7.982095,9.878008,6.302673,-8.458499,-2.576315,3.235680,8.851036,0.651493,9.864576,-8.670558,-0.326753,-9.132826,3.792258,5.081962,-9.105635,0.049991,-0.023042,-8.948751,7.224081,-5.980211,2.738316,8.166781,3.919891,-7.986143,2.642153,-3.707506,1.995692,-4.753080,-3.025173,-2.792691,-2.085115,-9.578564,-5.122634,4.271809,1.680067,2.182697,5.661262,3.441884,-4.448645,2.313459,-1.263199,1.528086,7.603948,-6.605693,-7.327355,-9.590145,-3.823361,7.078854,1.730934,7.957138,-6.834512,6.233731,3.107352,6.021944,-9.907019,4.264081,-6.385392,9.296785,-6.910547,0.822813,-1.652399,-2.190642,-5.802552,9.898139,-7.503415,-3.597696,4.004750,-4.441637,8.912236,-3.451234,9.072157,-1.651693,5.458992,4.168425,-4.810836,-6.127945,-4.502381,0.098405,-9.440092,2.701382,0.828422,-8.270151,8.033034,4.650667,-5.521849,2.208900,4.423489,7.337419,0.566571,0.594906,5.380730,-0.366714,-4.207979,6.131630,-8.302030,4.559752,-7.419601,-9.541339,-4.557899,-2.177281,-8.028294,-6.489578,-6.491133,-4.332456,-8.744000,3.042200,3.626303,-4.183620,7.737824,-4.626647,-3.204551,-9.245906,2.408608,-0.852954,-7.709868,-4.241471,-7.664871,9.957313,-2.795882,-2.340083,5.678023,8.277054,2.967113,-9.830001,9.395576,-2.417886,-4.436093,-1.317851,-0.533745,1.574218,-1.007527,2.663284,3.624490,5.109826,-3.665048,-6.736362,5.716103,-4.914260,3.636586,6.515133,4.834398,-0.020839,-3.444289,-3.713243,-5.516259,-2.072337,9.246310,2.939609,-0.528894,2.776016,8.553974,-4.809113,6.604957,3.930031,1.193052,7.777676,7.194529,-3.422959,-4.155607,-0.586914,-1.974060,0.712145,-0.571363,-2.118593,0.196108,5.373297,-5.804045,6.925008,-2.108955,-4.073567,-7.540501,-9.174499,-1.031202,7.932302,7.114960,2.981584,-3.123356,-7.651741,1.858603,3.710612,-1.204690,7.428659,-3.219514,-9.039965,-8.462375,-5.007560,-2.810387,-9.545792,7.928005,2.033832,9.126416,8.744020,-0.124188,-6.335139,-2.519592,-7.879523,-5.179505,7.218685,2.891303,6.615285,7.608999,-3.907165,-5.488885,-7.033811,-0.478604,7.589434,-2.713475,-8.099962,-0.224540,-9.861195,-1.682687,8.387131,2.578623,-0.167569,-1.499969,-3.925203,9.921095,0.689068,8.680256,-2.517483,9.940847,4.953103,-4.190474,-1.304725,-4.070425,1.559300,-9.475649,4.788004,-7.356532,-3.820240,9.824869,-4.052167,7.514736,-7.565076,0.023371,-1.864290,-0.864122,-5.560573,3.633017,7.488842,9.108056,4.218366,2.377327,1.650395,-5.185389,-2.715782,-8.282378,-2.525543,-7.340283,-5.167041,5.531689,3.673612,-1.438372,-9.567391,-6.867925,4.173497,0.641372,6.434471,0.183461,-6.228963,-3.381765,8.493160,2.471654,-6.137140,4.252396,5.110909,-7.917396,-2.176680,-8.269667,-4.470485,7.757101,-2.430889,-0.235341,6.003577,8.263032,9.613201,9.268273,-2.276837,8.213719,-4.820106,-0.605061,2.445634,-5.590180,3.625796,9.802920,-9.312409,-7.381188,1.570904,-1.542385,-6.816026,-1.073650,-5.934102,8.350129,-4.434158,4.297467,3.317417,-6.512010,-5.955796,-8.498734,6.752341,-6.232059,-7.101397,-9.902630,8.268348,8.056142,-1.118878,-9.177634,4.133355,-8.417171,-2.903789,-1.405688,4.641787,-1.500850,-8.196136,8.436871,-3.985992,9.620958,-1.339499,-9.620075,-4.433976,-5.102234,5.876432,3.726204,-8.912430,-2.834149,-8.566708,-0.382706,2.044679,9.679838,1.667472,4.020882,-1.767082,8.488076,6.322916,7.206390,7.641321,-7.616185,-9.915487,1.386792,7.716966,5.548393,-8.146381,4.618909,-8.597362,5.592289,-3.372429,-2.080129,6.330384,6.367919,6.846681,0.440775,-3.368538,-3.965333,6.622949,4.242731,7.396330,-7.087422,-1.427443,-4.694712,1.588386,5.224570,-3.296160,-3.005724,8.874820,-2.260954,-5.246157,7.369043,-8.564173,4.788853,8.544519,-9.741035,9.489048,-1.720641,6.377126,8.257888,2.733988,-2.169509,-3.720347,1.688212,-3.401312,-2.849736,3.685443,-8.937842,3.384275,-3.206377,-1.023264,-0.330867,6.288623,-5.632014,3.686850,8.382613,-8.266790,-5.367665,0.223604,-7.715778,-6.768485,-4.515665,-9.204727,3.812871,9.545516,-3.716602,-0.174878,5.649385,5.925653,-5.763061,4.223175,5.757674,9.443531,-9.102217,-9.143557,6.803476,-0.064134,-5.401707,-0.017911,-7.615766,1.319549,2.441024,7.221629,-3.437094,-0.656715,2.335477,-6.980942,7.952101,9.482180,-6.400003,-8.408627,-0.974130,-4.718997,9.405604,-1.870964,-7.785711,-8.741599,8.524339,-9.720902,6.948207,3.477646,2.756255,0.275638,9.459363,-3.449630,-6.952128,9.075884,7.658916,-4.221524,-3.316435,0.664179,-2.694205,8.214483,9.687170,9.581924,-2.247381,-0.673830,0.482590,0.740250,-9.638455,-4.502783,-6.608088,8.222356,3.533320,2.683125,-6.313538,-3.264857,-9.597293,-4.558936,-9.800359,-1.421575,-2.213943,-4.341450,8.048526,8.306662,6.739971,-3.785362,3.985508,-2.124005,8.913362,4.744956,-0.969157,2.001456,0.415732,-7.659820,2.237783,-4.343271,7.537650,5.867335,-3.648017,-8.225822,1.368174,-3.654659,-7.955333,3.812725,-2.654143,9.620845,1.599819,9.409773,4.286412,-8.108806,3.811779,-3.448242,1.906959,8.282850,-9.999296,4.586876,-7.490460,9.590358,-4.683619,0.201027,1.011172,9.371237,3.696009,7.183116,2.979746,8.084449,-5.255142,3.423044,-3.371394,-1.151151,6.419806,-6.114315,8.441184,-7.098230,-2.809397,-5.871965,5.410149,-8.295174,-9.576308,8.323698,5.310289,-1.245881,-2.056810,0.946977,-8.592677,-0.362113,-6.178883,-6.319422,-9.531051,1.529933,-6.963226,-4.861044,-7.626214,-6.556504,-5.007871,-5.789687,-3.147893,4.172770,-8.284195,5.908855,-3.999201,-5.260458,-3.850276,-3.989440,-0.530714,-4.463031,1.449131,-4.390658,3.721179,2.333973,-8.440304,-3.755240,-0.226076,5.733738,-3.831624,-1.631741,-9.168897,4.293091,5.081752,0.317572,-2.252812,-5.090069,-9.753896,0.004452,9.396153,9.761555,-8.768886,-9.134436,-3.490575,0.155238,7.999782,0.935379,3.001995,-5.932583,0.569158,-3.527968,1.107577,5.610760,9.362628,-5.503499,2.985329,-4.126397,8.929770,5.307404,-8.238469,-8.784109,-7.499716,-3.316215,1.117566,-8.468476,-9.691459,-3.266643,3.087567,-8.295114,-0.330258,1.764559,-7.680381,3.429745,-4.997053,5.071084,3.799767,-0.570496,-3.515556,9.202526,-0.757553,-7.598994,-3.018199,-5.113954,-6.196319,-3.832475,2.735037,4.962837,9.086483,6.995599,5.530093,3.850891,7.832026,-6.053164,-9.830066,5.243606,8.245172,9.839085,-1.238899,4.933315,-7.209581,4.046081,8.960149,-9.400246,3.868265,-9.121025,-3.472717,9.126474,-8.762587,9.638048,-9.676065,6.838770,-0.040818,1.916740,-9.987681,-6.649839,7.550043,7.197384,-5.374145,0.733197,8.195006,-1.263929,6.419816,9.471181,0.726614,-1.075414,4.713579,9.631704,6.129410,-9.712894,2.754331,-4.486552,-8.722085,0.059204,0.379810,-9.231655,-9.537549,5.241376,2.526228,1.749485,9.785050,-6.511192,2.013107,1.619166,-5.630347,6.473652,-8.783430,-3.527209,7.871031,5.934433,4.446588,0.812241,-3.890188,6.584943,-1.988217,-5.695819,6.237035,-8.007206,-4.729246,8.366725,-2.206158,-3.349229,-8.094965,8.264344,-1.728762,7.511259,2.083338,3.705368,8.598511,0.756993,-3.461232,7.834781,-5.888996,-9.922585,8.771106,1.924460,-4.073924,-5.822763,8.398993,-9.708708,-4.913463,7.317257,0.075497,1.944162,1.738557,-2.967380,-9.928148,3.454124,0.435370,3.008745,6.822903,-5.725863,-2.822304,2.436463,2.221923,8.574791,9.772887,6.473400,-5.977379,1.024492,6.108552,0.361143,2.609465,-5.077909,-1.500092,-8.464602,-0.385392,-4.048890,1.945796,-8.864089,6.681857,0.501319,-7.197242,9.844508,7.362402,5.696211,-1.111673,1.196532,7.608972,7.188921,1.904183,-8.894443,-9.058332,3.683004,-2.307507,-3.085973,8.194149,-0.501207,-1.818091,-5.975066,-4.262595,-7.113561,-1.500054,-3.667274,3.311138,-0.369071,5.944900,2.850268,7.659748,-1.024710,-3.326271,8.255505,-8.166647,-6.666401,-1.729400,-2.699950,-0.896044,9.252953,-1.993171,-7.547062,2.346132,7.965528,0.048198,0.204891,2.689636,-3.318312,-8.788127,2.791014,3.117682,-6.640655,2.169371,-9.070679,6.651548,-9.958781,-8.337354,-7.021968,4.042765,-5.107404,-6.525792,7.584382,4.520459,2.914920,-3.982212,-9.793213,-5.105353,3.238482,-8.870794,7.033963,5.767920,2.343251,4.563402,-1.867421,9.021083,4.339801,-0.245215,4.681672,5.833445,0.561247,-4.068671,8.559662,-4.543180,-8.623977,5.361711,3.630115,6.146968,-7.774849,-1.355130,-8.360581,5.849603,1.174316,-4.593772,-3.440048,8.752576,9.780119,3.129981,3.703011,4.687640,-2.319844,8.163201,-6.829621,8.365180,3.255336,8.731952,8.683104,-5.522019,-9.894344,-8.149737,-2.418606,-9.441147,2.287515,-3.931053,-3.347160,-5.107844,-9.116648,-3.104695,-6.625848,7.185215,0.005430,9.097579,-0.113495,7.070292,0.126200,4.069080,8.138035,3.643311,6.560121,0.508304,-5.103329,8.562090,-2.242769,0.352880,1.125085,-5.817222,9.639207,1.297113,3.093873,-8.084317,-1.627061,-6.223678,9.018027,-8.305510,-0.954023,-0.310917,6.820948,4.184032,6.129529,3.046568,-0.483971,2.702197,4.553674,3.668036,5.889485,9.349354,4.159351,-3.981309,-6.928407,0.586428,-6.705443,7.173246,0.368576,5.427976,2.716128,4.861532,3.395522,1.912515,-8.856211,9.185893,-8.585459,4.290451,3.153261,-3.602777,8.592339,-5.702346,-9.300883,0.346626,-8.345138,-9.309010,3.821922,3.784065,8.308231,-4.196088,8.331538,2.215271,-1.834882,0.714030,-6.347833,8.780965,-4.178329,-3.237888,5.660034,-7.656410,-9.723775,5.789023,0.923310,-2.996979,2.180439,-3.166690,8.163706,-0.867745,-7.609819,9.658473,-8.617183,-8.050888,-4.384305,4.545912,4.055793,7.074726,-4.651233,1.398425,-3.591112,-9.217315,-9.147488,-4.564939,6.011971,-7.718413,6.581871,-0.631785,-3.965319,-5.644447,2.745822,3.969253,6.119806,7.953206,4.578970,0.588906,-3.714591,-2.595403,-6.325059,-7.222481,2.646397,-5.788377,-4.224846,-0.747629,3.708910,1.749347,-1.575208,7.435272,-7.139481,-9.794151,-3.338394,9.049015,7.082881,9.558630,-5.214730,2.379358,-4.629094,-3.825160,6.811622,-0.859970,7.375866,0.936879,-5.614653,-4.812010,1.972520,-9.943375,-0.567914,2.781509,3.162553,-0.425745,-7.771483,-0.821932,0.788517,-5.316470,1.434236,6.716432,-1.579566,6.798005,-6.756457,5.403055,-7.543492,9.582843,3.141975,-0.523691,3.063359,7.555562,2.144946,5.531160,-8.523400,2.091061,-8.465374,5.055554,0.722210,7.791829,-9.847369,-1.708802,-5.931612,3.785054,-2.722557,5.639438,-2.339705,5.827110,-4.479760,-1.482636,-5.069543,-4.391890,9.925916,-5.826632,-5.440227,-0.914173,-8.481754,4.487230,-1.336397,9.137021,5.122417,-9.554211,6.415585,8.327634,-8.857214,-4.699286,1.757332,5.114264,-1.279141,7.108496,9.676605,9.019519,-0.692531,6.548627,-3.421153,2.062906,9.007658,2.080901,-9.615206,-1.590071,2.743709,8.658497,5.613652,4.300034,-9.815903,4.140716,-2.132472,-1.794087,2.670376,4.342921,-3.916437,6.405843,-8.872251,-9.221721,7.868592,-9.364723,5.832005,7.119663,-3.865492,7.365323,-2.068943,4.239806,5.414209,7.013737,3.624555,-0.513567,-9.485860,4.012419,7.370466,1.271405,-1.458908,8.243145,1.284894,-0.152352,9.193812,4.271887,-6.262721,-5.200745,-0.720918,1.742871,-6.269828,5.162572,3.694998,3.201559,-1.736932,-3.273163,-2.735270,-7.022969,-3.201524,-2.937378,-2.969691,8.892877,-2.800391,4.027817,-9.116261,-9.425033,-2.684794,6.385488,-8.909376,-8.179217,8.035364,3.952685,-9.288645,1.085533,-1.462963,-4.047056,1.624075,-0.370994,8.153468,-4.945133,-9.056718,-5.109661,-0.703692,-8.052280,3.322380,8.710911,2.612803,-8.181743,6.645637,1.321476,7.695942,-6.542459,1.199921,-6.759007,-6.739999,-4.923821,3.162751,-3.830411,-2.052457,-8.075471,4.186828,-1.361106,-6.145707,8.156805,6.414283,-8.910338,-5.387264,9.582901,5.330567,8.939339,3.242557,-9.192418,-2.888457,-4.344411,2.421307,-4.485480,0.556537,-6.641547,-6.529184,4.123036,-4.087998,-2.578588,-7.917271,-5.278035,-4.037552,-5.885013,-5.932891,-2.035130,5.163429,9.006222,-1.793866,6.994932,7.149806,6.662839,5.678715,2.887947,-9.729021,5.287024,4.387960,-7.612154,1.246971,5.322831,7.517175,-1.384004,2.250050,-0.901574,-8.330910,8.951678,0.173387,0.517026,1.405963,-8.764148,-7.264558,-1.770962,6.894808,7.804962,0.763417,-0.340852,3.240160,8.930921,3.708896,-5.839261,-5.637224,3.460835,-0.411431,-3.733987,2.994179,-6.104700,-7.029852,4.055784,6.756353,-5.958378,-9.786615,-4.823658,-7.383619,-3.079247,8.729053,9.653854,-7.246806,8.864546,1.026690,-0.919613,-4.278968,-1.721627,1.381734,-8.272329,8.660809,-1.813969,-8.613867,7.918900,-7.582119,-5.138320,-7.249198,8.218708,-2.137165,2.592005,4.164266,-0.423705,-3.358182,-3.560801,-1.112131,3.559746,-7.510023,3.335981,-5.374535,7.006465,-7.915011,-9.587895,9.653444,6.796380,-2.100670,0.364792,-7.958895,3.363793,-6.373908,4.608897,-3.760442,-0.827108,-2.972817,2.703049,-2.526621,5.933754,-2.322973,6.059385,-4.879742,0.937774,-3.285309,-5.822098,-8.524697,8.310019,4.080448,-4.604481,8.104379,-2.506005,-5.152591,-1.079475,-2.101281,-7.378016,0.216468,-8.902077,-6.073609,-1.316343,-7.836246,-1.121236,-2.712415,-2.058772,-2.922679,-7.954654,1.087101,1.032384,-7.173387,5.267805,0.762090,-7.794950,8.680840,-6.880129,-6.354706,-6.159209,0.013483,-4.955767,5.981577,-5.571438,3.608865,4.884772,8.341405,-5.827367,2.079692,0.959935,9.402734,6.888196,-3.332639,2.671083,2.457795,-0.491961,-3.671561,-9.841354,4.346734,5.710556,8.825131,4.719090,2.508047,6.373225,0.156153,4.447556,-4.912352,-3.136684,0.785650,6.034914,1.872696,5.451287,-9.379500,5.748297,-5.716345,-5.518405,-7.325600,7.258664,-2.741659,-1.760484,3.874397,-2.727994,-8.609499,-0.200053,-1.457171,-2.410122,2.436311,4.131950,-9.118237,5.684214,4.823516,-2.142334,-0.068769,7.247540,-8.665802,-5.342230,-5.338116,8.427087,5.726219,-3.247783,-5.030415,-6.216906,-7.125895,1.046026,-1.881882,-3.088220,7.162159,6.373386,-6.642883,-3.372731,-0.874998,-1.717330,1.811928,-6.019444,9.888159,8.780089,1.574193,-4.929733,8.915428,-9.651293,-5.996845,-7.258722,-1.534242,0.108322,-1.064192,1.109423,4.243615,5.356496,-1.476331,6.706841,-9.090706,6.548227,-9.496068,-3.928761,8.156915,-0.270756,3.527406,9.470866,-1.162641,-8.358114,-5.646371,-8.277153,8.782888,7.844308,4.462989,0.643838,0.301620,5.092472,-5.552758,9.833517,6.617690,-2.164384,-8.312951,-9.187266,-0.961616,-8.969491,-1.177495,-0.972715,-4.715732,0.823615,1.579986,-7.998844,4.891872,-6.136718,9.900444,-2.968777,6.121608,7.020273,-4.526339,3.565417,-1.582222,-1.608620,-5.768041,-3.132510,-0.682892,-8.657073,-3.667460,-4.548162,-9.405309,-7.810624,-9.128425,-9.367929,7.430036,-7.493670,4.384039,-9.048788,2.865164,5.421923,-7.097317,-5.970306,7.223820,-6.420018,3.781620,-9.354200,3.129908,3.283639,1.212067,-1.721122,1.226591,-6.239908,-7.969995,-0.486885,9.236679,7.327730,7.401021,-0.369149,-3.731231,0.426208,0.417741,3.909711,-2.062818,1.225243,8.799303,-1.070671,-3.341293,6.784510,2.376688,-2.105651,9.150804,-3.119532,2.523721,-4.274410,8.168694,-7.125512,7.767400], dtype = "float32")#candidate|10001|(3600,)|const|float32
call_9999 = relay.TupleGetItem(func_150_call(relay.reshape(const_10000.astype('float32'), [15, 1, 15]), relay.reshape(const_10001.astype('float32'), [15, 16, 15]), ), 0)
call_10002 = relay.TupleGetItem(func_154_call(relay.reshape(const_10000.astype('float32'), [15, 1, 15]), relay.reshape(const_10001.astype('float32'), [15, 16, 15]), ), 0)
func_8454_call = mod.get_global_var('func_8454')
func_8455_call = mutated_mod.get_global_var('func_8455')
call_10006 = relay.TupleGetItem(func_8454_call(), 0)
call_10007 = relay.TupleGetItem(func_8455_call(), 0)
output = relay.Tuple([bop_9975,call_9986,var_9987,call_9999,const_10000,const_10001,call_10006,])
output2 = relay.Tuple([bop_9975,call_9988,var_9987,call_10002,const_10000,const_10001,call_10007,])
func_10010 = relay.Function([var_9973,var_9974,var_9987,], output)
mod['func_10010'] = func_10010
mod = relay.transform.InferType()(mod)
mutated_mod['func_10010'] = func_10010
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10010_call = mutated_mod.get_global_var('func_10010')
var_10012 = relay.var("var_10012", dtype = "int64", shape = (2, 3, 6))#candidate|10012|(2, 3, 6)|var|int64
var_10013 = relay.var("var_10013", dtype = "int64", shape = (2, 3, 6))#candidate|10013|(2, 3, 6)|var|int64
var_10014 = relay.var("var_10014", dtype = "float32", shape = (140,))#candidate|10014|(140,)|var|float32
call_10011 = func_10010_call(var_10012,var_10013,var_10014,)
output = call_10011
func_10015 = relay.Function([var_10012,var_10013,var_10014,], output)
mutated_mod['func_10015'] = func_10015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4363_call = mod.get_global_var('func_4363')
func_4365_call = mutated_mod.get_global_var('func_4365')
call_10022 = func_4363_call()
call_10023 = func_4363_call()
func_1095_call = mod.get_global_var('func_1095')
func_1097_call = mutated_mod.get_global_var('func_1097')
call_10050 = relay.TupleGetItem(func_1095_call(), 0)
call_10051 = relay.TupleGetItem(func_1097_call(), 0)
func_1819_call = mod.get_global_var('func_1819')
func_1823_call = mutated_mod.get_global_var('func_1823')
var_10055 = relay.var("var_10055", dtype = "uint32", shape = (600,))#candidate|10055|(600,)|var|uint32
var_10056 = relay.var("var_10056", dtype = "int8", shape = (450,))#candidate|10056|(450,)|var|int8
var_10057 = relay.var("var_10057", dtype = "float32", shape = (3600,))#candidate|10057|(3600,)|var|float32
call_10054 = relay.TupleGetItem(func_1819_call(relay.reshape(var_10055.astype('uint32'), [12, 5, 10]), relay.reshape(var_10056.astype('int8'), [1, 450]), relay.reshape(var_10057.astype('float32'), [3600,]), ), 2)
call_10058 = relay.TupleGetItem(func_1823_call(relay.reshape(var_10055.astype('uint32'), [12, 5, 10]), relay.reshape(var_10056.astype('int8'), [1, 450]), relay.reshape(var_10057.astype('float32'), [3600,]), ), 2)
func_7508_call = mod.get_global_var('func_7508')
func_7510_call = mutated_mod.get_global_var('func_7510')
call_10066 = relay.TupleGetItem(func_7508_call(), 1)
call_10067 = relay.TupleGetItem(func_7510_call(), 1)
func_3017_call = mod.get_global_var('func_3017')
func_3019_call = mutated_mod.get_global_var('func_3019')
var_10069 = relay.var("var_10069", dtype = "float32", shape = (140,))#candidate|10069|(140,)|var|float32
call_10068 = func_3017_call(relay.reshape(var_10069.astype('float32'), [2, 7, 10]))
call_10070 = func_3017_call(relay.reshape(var_10069.astype('float32'), [2, 7, 10]))
output = relay.Tuple([call_10022,call_10050,call_10054,var_10055,var_10056,var_10057,call_10066,call_10068,var_10069,])
output2 = relay.Tuple([call_10023,call_10051,call_10058,var_10055,var_10056,var_10057,call_10067,call_10070,var_10069,])
func_10074 = relay.Function([var_10055,var_10056,var_10057,var_10069,], output)
mod['func_10074'] = func_10074
mod = relay.transform.InferType()(mod)
mutated_mod['func_10074'] = func_10074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10074_call = mutated_mod.get_global_var('func_10074')
var_10076 = relay.var("var_10076", dtype = "uint32", shape = (600,))#candidate|10076|(600,)|var|uint32
var_10077 = relay.var("var_10077", dtype = "int8", shape = (450,))#candidate|10077|(450,)|var|int8
var_10078 = relay.var("var_10078", dtype = "float32", shape = (3600,))#candidate|10078|(3600,)|var|float32
var_10079 = relay.var("var_10079", dtype = "float32", shape = (140,))#candidate|10079|(140,)|var|float32
call_10075 = func_10074_call(var_10076,var_10077,var_10078,var_10079,)
output = call_10075
func_10080 = relay.Function([var_10076,var_10077,var_10078,var_10079,], output)
mutated_mod['func_10080'] = func_10080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1899_call = mod.get_global_var('func_1899')
func_1901_call = mutated_mod.get_global_var('func_1901')
call_10088 = relay.TupleGetItem(func_1899_call(), 0)
call_10089 = relay.TupleGetItem(func_1901_call(), 0)
output = relay.Tuple([call_10088,])
output2 = relay.Tuple([call_10089,])
func_10092 = relay.Function([], output)
mod['func_10092'] = func_10092
mod = relay.transform.InferType()(mod)
output = func_10092()
func_10093 = relay.Function([], output)
mutated_mod['func_10093'] = func_10093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9726_call = mod.get_global_var('func_9726')
func_9728_call = mutated_mod.get_global_var('func_9728')
call_10099 = func_9726_call()
call_10100 = func_9726_call()
output = relay.Tuple([call_10099,])
output2 = relay.Tuple([call_10100,])
func_10101 = relay.Function([], output)
mod['func_10101'] = func_10101
mod = relay.transform.InferType()(mod)
output = func_10101()
func_10102 = relay.Function([], output)
mutated_mod['func_10102'] = func_10102
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10103 = relay.const([[[-8,6,1,-9,-1,-2,7,-3,8,7,1,-6,-5],[7,6,3,-6,-9,-1,2,9,6,-7,-9,2,-1],[-3,-5,-2,2,-8,-5,2,-3,-2,-8,10,-7,1],[-6,-1,8,-5,-4,5,6,-3,-8,-3,-9,-8,6],[-10,-7,-10,-4,9,6,-4,1,-8,-5,-6,-5,3],[-5,-2,-1,5,-3,-2,-7,10,-6,-6,6,-4,5],[3,2,-8,9,8,-2,9,-10,-4,-3,-8,1,-6],[8,-9,1,-6,9,9,-4,1,10,1,10,-6,-2],[-4,10,1,1,2,-1,6,-2,2,-2,2,-1,-1],[-10,8,3,6,-1,1,6,-5,-2,9,-3,-10,1],[8,-6,-7,-8,-10,-6,-2,1,10,-9,-6,-5,4],[7,-5,-9,4,-2,4,5,-10,-10,7,-8,-1,-3],[7,-4,-8,-9,9,5,-3,-4,8,-3,-10,3,-4],[-8,7,2,9,-6,-4,9,-3,9,-5,5,4,-2]],[[-10,-4,5,9,-1,-7,-6,-7,-8,-6,-5,8,-9],[1,-2,-8,9,7,3,-7,7,-7,5,-5,-2,-5],[-7,-7,6,10,3,10,-9,6,-3,6,-5,4,7],[-4,-10,6,-1,-6,2,-5,-3,7,-2,-3,5,6],[2,-3,-9,8,7,-9,-8,7,2,-5,7,-8,-6],[-5,-10,-3,10,3,-5,9,6,2,6,4,-1,4],[2,8,-2,-8,-1,7,9,1,3,-7,1,-5,-1],[4,9,-10,9,-8,1,3,9,5,2,-3,7,3],[3,4,6,-4,5,5,-3,5,9,8,-10,7,1],[4,-3,-4,5,-8,8,-6,-9,-9,4,-8,3,-2],[-1,4,8,-7,-7,5,1,-2,9,-1,1,-1,-3],[-9,-5,9,7,-5,5,5,-5,3,8,-4,-5,3],[5,2,-3,4,1,1,1,6,9,6,-4,7,-6],[6,6,-9,3,8,-4,3,8,-5,1,-4,3,-2]],[[1,-6,10,10,3,-6,-3,-4,9,-4,3,-5,-1],[5,-9,10,8,-8,-1,-6,-10,-1,-7,3,4,2],[-5,2,-7,1,-5,5,8,-2,4,1,10,-10,-1],[-2,8,-2,2,10,-2,5,-1,-9,-8,6,-8,-7],[-3,5,9,8,-5,10,-6,-9,3,-4,-8,3,-3],[-7,10,-1,-10,6,8,-5,-6,-10,-9,-1,-5,-5],[7,7,9,-4,8,1,-2,5,4,-2,-7,3,1],[8,-8,-9,3,8,1,-10,-5,-7,9,-8,-4,-5],[3,6,-3,-10,-7,7,-4,-1,-7,4,-3,3,-2],[7,1,4,-2,-8,7,8,-4,4,-10,-2,6,-10],[-6,-3,4,-2,-3,-9,-1,10,4,9,-2,7,-8],[10,-7,-6,-5,-9,10,4,-2,-10,9,-8,-7,2],[-2,3,7,5,-8,-7,10,2,9,-5,2,-3,-7],[-5,-10,4,-3,3,2,4,-10,3,-6,2,-4,8]],[[4,6,-4,6,5,7,6,-9,-1,10,-3,1,-9],[-9,-2,6,8,-7,-2,-8,2,-4,9,-1,-8,10],[-4,-5,6,6,10,-5,-4,3,-7,3,-8,2,-2],[-8,5,-6,-10,4,2,3,-1,-2,-5,3,6,5],[-4,-3,-1,-1,-6,-5,-5,-2,8,10,-8,-8,-7],[-4,6,-9,6,9,1,-4,-6,-5,6,9,-7,-5],[3,-7,-4,-3,10,-5,4,-6,5,-5,-6,1,10],[-10,-10,9,10,-4,-6,-7,9,-7,-7,9,2,10],[-4,4,2,10,-8,-3,-4,-5,4,-1,5,7,10],[1,-1,1,-3,-1,8,-6,2,-7,6,9,3,4],[-7,-9,10,10,-2,-9,6,1,-3,2,-6,-4,-8],[-6,-2,-10,-3,7,-10,5,7,-8,-3,-7,-6,2],[6,6,-8,9,-3,10,-8,9,3,10,7,-3,5],[-7,-6,2,-4,10,-1,3,-7,-9,-1,3,-2,3]],[[8,-10,-3,5,5,-5,-8,-10,-1,-2,-5,3,1],[9,8,-3,-8,-3,-9,4,6,4,4,2,8,-4],[-8,8,-5,-3,10,1,-10,-1,-3,-4,4,-2,1],[-4,9,-1,-6,-6,-9,-4,-6,9,9,4,6,-10],[3,9,-7,2,-4,3,-3,3,-8,1,3,-10,9],[-4,-10,-5,6,7,-8,1,2,-4,-3,-5,3,6],[5,8,-8,6,7,-10,-5,8,6,7,-3,2,-7],[8,-4,-6,10,2,-8,-5,10,-10,10,10,9,-5],[8,10,-8,-5,-5,-1,7,-3,2,10,3,6,-1],[-1,-4,5,-6,7,-7,6,5,9,1,-9,-9,-4],[10,-8,-4,3,5,-2,-5,5,-3,-4,-8,-4,-4],[-1,-1,-7,-5,-6,-4,-9,-7,2,-9,-5,-9,3],[-1,-6,8,-2,-4,-4,6,8,-8,-2,7,8,10],[10,-2,7,-10,2,4,-8,5,-9,-1,2,5,6]],[[-8,8,8,9,1,-5,1,-8,1,5,-10,-6,1],[-4,-4,8,5,-1,-6,-4,6,-9,-5,4,-4,10],[3,-9,-6,1,-1,1,7,-10,-2,-1,4,-7,-4],[4,4,-4,-2,3,5,-9,5,4,-1,6,-1,-2],[-4,3,-4,7,-1,-4,5,-2,-3,7,-10,-1,-7],[4,3,-2,-9,-6,2,-10,6,7,-1,-2,-1,-2],[9,-3,10,6,-7,10,-3,-8,10,9,10,-9,-6],[-5,9,-7,-1,-7,-10,-6,-3,-1,-3,-1,-7,-10],[8,-9,-10,1,-2,-10,-1,-5,3,-5,8,-1,9],[3,-4,-2,-2,-7,5,-6,6,-9,-4,-7,-8,1],[2,-6,-8,4,3,6,-9,2,3,-1,3,-8,-8],[5,-9,3,-10,10,-9,-2,4,-10,3,9,9,4],[1,8,-7,7,-9,5,9,-9,-2,3,-1,9,6],[-1,-7,6,7,9,-6,9,-7,9,2,6,-3,1]],[[3,-9,5,1,-4,-2,-2,-6,1,6,-2,6,4],[-1,1,2,-10,-3,10,-1,-3,-5,5,-3,-7,-4],[5,4,-4,-8,-4,8,-1,3,7,4,-6,-4,10],[-7,8,5,-5,-5,-3,3,3,-3,4,-6,9,-2],[-8,-6,-6,7,-8,9,3,-10,7,6,-5,-4,7],[2,9,9,-2,10,-9,4,-9,-1,-7,7,-2,-3],[3,8,7,-4,-5,8,9,7,-2,7,6,-2,-9],[-8,-3,10,10,6,9,6,6,-3,-1,-4,3,-2],[1,5,-4,-1,-4,5,-10,-3,-2,4,4,-4,8],[-6,1,-4,-4,10,-10,7,3,-9,-4,1,3,5],[-5,-2,6,5,-8,10,6,1,3,1,1,-9,4],[4,-7,5,-9,4,5,-5,-8,4,-8,-9,5,7],[2,5,-7,-3,10,-8,-5,4,-2,4,5,4,-2],[-6,-5,-5,10,2,6,6,5,5,-4,1,-10,-8]],[[2,-10,-4,-3,9,7,5,9,-7,9,8,-4,-5],[-10,2,9,7,10,4,-2,3,-2,-9,2,-7,7],[-7,8,8,4,-6,-3,10,6,-1,7,-8,-10,2],[-2,-5,4,2,3,-10,7,1,8,-7,7,3,-10],[5,-9,-4,-7,1,-2,-3,-2,-3,6,-1,5,-9],[6,6,-2,-5,-1,-1,1,-2,-5,-7,6,6,-6],[-8,-6,3,6,7,-4,8,-5,-4,1,9,-10,2],[8,10,8,-5,3,-8,1,9,-2,-9,-8,-3,-8],[6,9,-4,10,3,1,2,-7,-5,8,4,-2,4],[7,-10,8,-2,6,5,1,-3,5,-8,-6,3,-8],[-1,-9,2,-4,10,2,10,10,-3,-3,-5,4,5],[6,-3,2,-7,-2,-6,5,8,-9,-5,-6,-2,-7],[-9,8,-10,-9,-1,8,3,-8,4,-4,9,3,-4],[4,-7,-1,-1,-10,5,3,-4,3,1,-6,-5,9]],[[6,9,10,6,-4,4,5,-4,7,6,8,-9,-1],[6,-7,-1,9,-5,-3,6,7,3,-6,-2,-6,-4],[-8,-5,-8,-6,-8,-2,-8,5,9,1,1,-9,2],[-10,10,3,7,-8,1,-3,-2,5,3,1,1,-7],[-5,7,-8,6,-3,7,-8,-6,-2,7,4,-3,-4],[-9,8,7,-2,3,-3,1,7,-5,-4,2,-10,9],[-5,-2,-7,-3,-7,-10,-7,3,9,6,-2,1,-4],[4,-3,9,-5,6,2,-9,-2,-9,2,-8,4,9],[7,-1,-2,-6,-8,-5,-7,-7,2,7,-6,2,-8],[9,4,-9,-7,-3,-7,-5,3,-8,-3,-9,-4,1],[-5,-8,-3,5,4,-10,6,9,2,6,6,-8,-2],[5,3,6,7,1,10,9,1,2,-1,-1,-4,10],[5,-8,5,3,-9,8,-4,8,-6,-7,-4,-6,-1],[-10,4,-7,-8,-5,10,2,8,5,-6,3,8,1]],[[-10,-1,-2,8,-10,4,-9,2,-9,-9,2,-7,5],[-2,-2,8,-8,5,-7,5,-7,9,9,5,6,5],[8,-8,-3,-9,-3,-9,4,-10,-6,-2,5,-8,3],[-2,-9,-6,-8,1,5,8,-7,-9,-2,3,4,-10],[-5,5,4,-4,6,-10,-4,-8,3,7,7,-2,-4],[7,-8,-9,5,-10,3,2,6,4,6,-3,9,10],[7,-5,7,-1,8,8,3,-2,4,6,5,3,3],[2,-5,10,-4,-3,4,6,1,5,3,-2,1,-10],[9,10,7,-6,2,-4,-10,7,-8,-7,-8,7,-10],[-10,-9,9,-2,-2,9,-3,3,-9,-6,-6,-1,5],[5,-1,-1,6,-1,-7,-4,-6,-6,-3,-8,-1,-9],[9,2,-9,8,-2,3,10,-4,1,-8,8,5,3],[6,-8,-3,-6,4,9,-7,4,10,-6,-3,-2,-3],[2,-6,1,-9,6,9,4,-7,-7,6,6,3,2]],[[-8,-4,-9,-9,3,6,3,3,-3,-5,-2,5,-2],[-5,1,-3,-6,-2,-5,-9,-4,-8,6,-9,8,9],[4,7,-3,3,2,6,2,2,-2,-4,5,-3,5],[3,-4,3,-6,-6,-5,-6,-4,4,2,-3,-6,-9],[9,5,4,9,-8,-9,-5,5,3,-8,4,3,7],[-10,-3,3,3,-7,-3,6,-1,10,-10,-7,-6,4],[-8,-6,4,-5,5,10,5,6,6,-3,-6,2,-8],[3,-5,-4,3,-7,5,4,1,9,-3,-7,-6,-5],[-3,-10,-9,3,-9,8,-8,-9,-8,-7,6,6,1],[-8,4,-9,2,6,-4,5,9,-5,8,-1,4,-5],[4,-10,5,-1,-1,3,-2,5,1,1,-3,8,10],[-8,-7,-7,-4,-5,-4,5,-7,-1,1,-6,5,-4],[-4,2,2,-8,-2,-2,-3,5,-1,5,3,10,-1],[8,-6,4,5,-3,5,7,-8,6,-6,-9,5,7]],[[-1,2,3,-5,2,-8,5,-5,-7,-10,3,-6,-8],[8,-2,-1,-3,-2,3,-7,9,2,-9,6,1,-10],[-1,5,-5,3,7,-8,-7,9,10,-4,1,4,-5],[5,8,10,4,-1,8,4,-7,8,-5,-3,10,7],[-3,1,-3,4,2,3,1,4,-7,5,-3,10,-9],[-6,-2,8,3,-3,-6,8,-3,3,-4,-1,5,6],[10,-7,-1,-8,3,-8,7,-3,-10,-10,-1,-7,10],[-5,-6,3,9,7,-1,2,-4,2,-6,6,-3,9],[1,-8,-3,-4,-4,-9,6,-2,4,5,-8,9,10],[-10,-2,-9,-4,-4,10,10,-6,8,6,3,5,7],[-2,7,-2,7,7,-8,2,2,9,-7,-10,9,4],[5,9,-5,8,5,1,5,7,-3,-5,-5,4,1],[7,-1,3,2,-7,3,1,5,-9,1,6,-8,-8],[7,-5,7,8,4,-3,-3,5,6,-1,7,-3,-7]],[[4,-2,-8,-4,7,4,-9,-9,5,1,-6,-6,-9],[-1,5,5,-3,2,4,-4,-9,-6,-9,1,7,-5],[-10,-1,4,-3,-10,-8,5,-4,-8,-10,9,5,3],[1,7,-2,-7,-8,-5,-1,9,-5,1,-3,-10,-6],[-1,6,-9,3,-2,-3,-5,1,-3,-2,2,-9,1],[-2,7,9,-10,-3,1,-5,8,-4,-10,-3,-5,-5],[4,-10,6,-5,1,-2,-8,-10,-10,2,4,10,-10],[6,10,4,5,-1,7,5,-2,9,-5,-9,-3,-2],[-8,10,7,-5,7,-3,5,-5,-9,-10,-1,-1,7],[9,2,6,6,-7,-2,-10,-4,-3,-6,-3,9,8],[-4,6,10,1,7,-1,3,-3,-10,6,-5,-3,7],[8,1,8,6,7,7,5,5,-6,3,5,-6,7],[10,-4,8,-5,-9,-2,-4,10,-7,7,10,10,7],[-7,6,6,-6,5,2,10,-2,6,-3,9,-1,4]],[[4,-7,9,5,9,-3,2,8,-9,-7,5,7,10],[-10,6,4,-9,-4,6,6,-1,-2,-9,8,1,7],[9,-5,-3,1,10,1,6,-8,5,8,4,-10,10],[-9,5,8,3,2,10,-7,-9,-2,2,-7,-3,-4],[5,-10,-3,-8,6,-2,-9,6,8,-2,10,3,-3],[10,5,4,7,9,-4,6,-2,10,-3,-3,-10,1],[8,-5,-2,6,8,-9,4,4,-4,-8,1,2,-6],[8,-1,-7,10,-9,-6,2,-6,10,-1,-10,9,5],[-7,7,-3,1,-1,-2,-10,-7,-9,2,-2,-7,-1],[1,-4,9,5,-7,10,-2,-8,-5,-7,-7,-1,-2],[-3,7,-6,1,7,5,7,-8,-2,9,-7,8,-5],[2,4,-1,5,-1,8,-4,6,-7,-3,-2,-7,5],[-5,10,10,8,-8,-2,-6,-7,-7,-1,10,7,-5],[8,-8,-8,8,5,-1,-3,-1,-3,2,-3,-1,-1]]], dtype = "int8")#candidate|10103|(14, 14, 13)|const|int8
var_10104 = relay.var("var_10104", dtype = "int8", shape = (14, 14, 13))#candidate|10104|(14, 14, 13)|var|int8
bop_10105 = relay.logical_xor(const_10103.astype('int8'), relay.reshape(var_10104.astype('int8'), relay.shape_of(const_10103))) # shape=(14, 14, 13)
func_8319_call = mod.get_global_var('func_8319')
func_8323_call = mutated_mod.get_global_var('func_8323')
var_10119 = relay.var("var_10119", dtype = "float32", shape = (216,))#candidate|10119|(216,)|var|float32
const_10120 = relay.const([0.480550,-2.485168,-5.374696,8.021545,-0.992692,-4.816244,-8.798136,-4.205346,-7.649221,6.423069,-1.515521,-2.919953,-7.793549,2.527288,-5.487993,-6.039004,8.895973,7.608041,-2.216743,6.098049,-2.929007,6.014183,2.431113,6.548671,8.882625,9.997576,-0.688344,-5.309842,-5.244433,-7.362417,-5.601953,-7.404372,-6.924042,-0.921718,-2.168953,6.419938,3.184587,4.023780,2.049457,-1.329186,0.449199,-7.974868,-7.397953,-9.330236,-0.145662,2.358728,0.021186,-5.894023,7.702794,2.489826,-1.016653,-0.295045,1.229395,0.646351,4.258194,3.418642,1.092913,-2.304788,-9.545027,-7.402222,-7.254355,-5.252574,6.702914,7.040116,6.486447,-8.759241,7.778086,0.595893,-7.134499,5.655611,-2.837745,-1.101654,-0.149395,1.475598,9.577376,0.132930,4.437146,-3.733691,-0.637154,-6.926577,-6.426583,-7.653163,5.088487,-4.610869,-2.452491,1.157176,5.041106,-4.968379,6.378716,-2.101242,9.086616,-9.105059,1.901319,6.447081,-1.096516,0.714411,-0.516390,-5.800929,9.029482,3.861425,6.987285,8.234348,-4.518157,-7.437160,5.328881,-8.082864,8.126699,-0.982212,2.978057,-3.425036,2.354622,-1.799959,6.083745,0.075954,-7.766917,-0.123256,-5.782803,-9.384788,7.942593,-1.199021,2.991233,8.329981,9.052606,-5.050604,7.371985,-1.827108,-5.771456,-7.814889,2.895306,8.560674,-9.279503,3.769086,3.526752,9.096018,9.553754,2.623469,5.591876,8.596952,-3.699712,0.909838,-7.061524,-4.863258,2.060322,8.117412,9.965461,-6.051481,-6.573151,-9.276206,0.871913,6.792873,4.303982,0.684959,8.235395,2.926341,-6.991352,-8.729056,-1.170505,-1.467350,7.598296,-3.317389,-4.852272,8.319789,6.559539,-7.689131,8.562579,6.025970,-2.137523,8.806819,7.259285,-8.530972,-3.324472,-5.866861,1.215477,-1.526891,-1.146707,2.761891,1.700597,-7.181554,-3.400411,6.258963,-1.393159,-3.791554,5.191224,-1.668898,-7.277775,2.400028,4.587182,4.453023,-6.072099,-6.346998,8.028842,3.817471,-6.589168,0.294199,-9.434407,-2.702920,5.150619,3.366523,9.452114,1.963874,-5.756567,-5.315883,-0.483166,2.875234,6.108527,-6.898959,0.873229,3.565648,7.621115,4.726911,9.260724,-7.139369,-9.474484,1.988496,1.664725,-9.262168,1.372397,-6.624304,-0.835953,-1.371603,3.778029,-3.967094,-0.308618,-7.781756,-8.897184,1.952010,6.441983,-3.579198,-7.786603,1.107138,-4.788954,6.454621,-4.963839,-6.003414,7.605209,-7.854934,7.604013,-3.254682,-3.727358,4.747572,-4.337753,-5.879849,-7.972296,2.562264,8.187646,-2.114136,-1.802045,8.931460,1.898367,-6.279369,4.357765,7.691214,9.489897,-2.073918,-5.682237,9.166457,0.184411,2.559342,-9.174088,-5.219386,4.306346,-0.471415,-7.136680,5.027301,5.147396,6.377684,-9.165704,0.724774,-1.499364,-3.591594,4.469176,2.854481,6.809504,-7.173516,9.722757,3.856288,5.260019,0.077274,-1.801711,-1.232296,-2.496102,-9.453708,-6.719688,-8.530591,6.176547,-6.960824,-9.828442,6.707496,-9.914663,-8.967931,-2.981931,-0.738200,2.076092,-5.527914,-5.758153,9.433787,-3.188233,-1.682273,9.159271,1.891739,1.272715,4.360424,0.421733,9.180472,-1.193091,2.731193,-2.227998,-9.535842,1.780287,6.835022,2.352732,-2.139967,-9.580604,0.559992,-3.956893,-0.140590,-8.246538,1.584160,4.883587,2.401878,-0.241776,-8.164204,-8.711858,-7.817236,4.522393,-0.539138,-3.857245,-7.226508,2.296565,-3.761226,-2.725675,8.326688,-6.180503,-1.678488,6.155705,1.343046,7.733674,-0.004127,5.749888,0.618462,-8.788488,0.975110,5.773227,8.257378,6.362215,-4.640773,3.674343,-3.664938,-5.891601,5.047681,-4.045838,-9.171442,-6.272386,-5.209082,8.574400,7.993197,8.419548,1.112733,-5.083247,0.228377,-4.317697,-7.309219,6.844633,-9.334827,6.988326,9.951772,-0.764054,9.134495,8.070933,-8.657130,-9.656445,-5.060118,9.550239,-3.892923,6.524693,5.355880,3.928228,6.880304,0.975556,-3.374466,4.024897,-0.552585,8.178609,-2.121570,7.302375,-9.266295,-0.851078,9.548732,-9.908035,-3.641342,3.183005,9.205648,8.375630,1.747889,-5.921741,4.485201,-5.322786,-8.216722,-0.988003,-5.211214,0.712029,9.178359,9.138720,5.014264,-1.765080,5.092881,-7.795458,-4.182209,7.029453,-7.770738,2.989138,5.963721,8.825239,-3.991656,0.022845,-9.722653,9.927065,-8.121360,-2.377169,-8.082939,1.827663,5.498345,-9.312423,0.243074,1.837654,-5.105282,-0.167817,-9.244470,3.722717,2.629822,9.401818,5.311428,9.789521,-3.940306,-0.960403,-6.564768,-6.458979,6.852601,4.491565,0.413417,-0.973986,0.063604,4.378439,-8.761116,-4.303417,8.493332,5.663393,-3.106992,3.687519,7.301600,0.188410,6.489460,6.869073,0.131612,-3.663739,0.318961,-6.702234,6.494225,4.990168,-8.044320,4.518250,1.244387,-3.111962,6.661483,-8.838780,1.727912,-1.328489,-3.849655,6.873766,-9.154668,-6.596947,-6.938471,-0.271408,-3.013192,-8.275324,-9.753884,5.354436,-4.653978,9.425599,0.768628,-0.414589,-4.993655,8.967791,-9.441874,-8.192416,-7.721266,2.199465,5.443796,-4.130953,8.976671,-7.738680,-5.529609,8.425641,5.367815,-7.987137,4.225450,-7.268463,8.300232,-0.667691,-3.301814,-9.464613,6.468218,-1.568231,-0.810058,-2.984830,6.373591,3.186301,-5.418167,-9.771388,5.526007,-2.484845,-9.836003,-8.757327,6.111255,5.848168,6.349376,-0.562470,2.276539,6.779107,-4.669011,6.028231,-4.359117,2.345802,-1.178067,4.385449,4.385094,-0.551683,-3.022946,5.005553,5.717794,0.213600,1.681780,3.524576,-3.455860,-7.104143,-0.183516,-0.638907,-6.469344,-0.080120,-2.421938,-1.120873,0.033847,2.554410,-5.852241,0.648902,4.340377,-6.695263,7.275646,-0.860280,1.287575,-0.475530,-5.072584,-6.549333,-5.310919,7.421280,-7.012954,-9.519770,-5.757235,1.213804,9.225428,-5.414420,-7.776137,2.348380,-8.660669,1.702547,-0.397480,-5.708545,2.365702,7.957262,2.258265,-1.013649,-6.089958,5.685075,-9.307662,5.304113,-8.970269,-5.737054,5.703722,-5.819008,5.659610,1.586727,7.289033,7.862686,-1.742627,-1.120714,5.602998,-3.387196,-0.829559,5.920906,-1.467547,-1.687930,-0.110065,7.830274,-4.607409,-7.406405,-8.665503,3.898773,2.818379,-8.004941,9.592100,4.336855,0.845337,-1.454974,7.995403,-0.647659,4.556336,-8.447094,5.598129,7.609535,4.149166,-2.069066,4.575395,7.824300,-5.044660,-3.699132,6.372263,-0.713423,0.804637,-0.827481,-7.760145,6.078771,0.794266,-5.153737,5.862762,-0.060624,1.576069,-0.501981,-4.348867,9.372431,5.604252,-0.206920,8.079456,2.586195,4.331363,4.082210,-8.644737,9.631134,0.622203,1.733959,4.728594,1.419775,-8.116286,4.034973,-6.575145,9.936296,7.194896,-9.422370,-2.412804,1.749522,2.741076,-6.699476,5.378628,3.836091,6.859232,-8.224100,-1.759874,2.291968,5.938021,7.290606,7.358953,-7.072541,-9.046013,9.393793,-7.006913,-0.444802,8.781830,-6.361199,7.717931,7.495597,-8.309989,4.332576,-2.554891,3.970007,-1.843582,9.112261,4.346206,-8.291425,-8.690684,-0.099103,-5.264602,-0.341736,1.451966,5.563624,-4.924627,1.379612,-5.287045,7.321102,2.302337,-1.483808,5.861432,1.288866,3.356249,-9.386571,6.680681,2.663298,7.515813,-6.947474,-5.222110,2.871284,-8.112063,9.057789,-1.041162,7.357509,0.721721,2.541511,0.420261,2.237076,-2.189186,-2.586279,-6.447059,9.178406,0.323782,3.527159,6.610084,-4.157329,6.077638,-6.072764,-6.155967,-5.569298,-4.146163,-5.436379,-6.132949,-3.586894,1.080456,9.989765,-9.065180,-5.233462,-2.650185,0.633472,-8.317051,9.029959,6.726927,1.776196,-4.226742,5.026987,2.282675,-0.192431,0.117874,-5.690187,-7.453826,9.531128,4.087658,-9.131519,7.771661,9.938855,-7.387638,0.106452,5.142276,3.069558,-3.040360,-5.133971,2.970245,-9.307072,3.777447,7.296592,-6.048603,9.952464,-8.385333,6.802784,8.236532,-4.551483,5.695990,-2.454360,-1.777090,-4.518288,-3.641954,6.624052,-6.344331,4.114658,-4.142183,1.335399,1.462016,-2.698543,-2.121140,4.943812,9.126099,9.070639,9.651179,7.783894,-0.801041,9.015744,-6.223699,-9.545984,-9.772861,-0.863489,-7.615717,1.389757,-8.215641,-6.694314,8.624363,3.605997,5.813445,7.897411,-2.868594,-7.321951,5.331804,2.139426,-5.599600,-5.537330,5.731806,-5.028825,-9.105569,7.709937,5.900956,4.509003,3.299624,8.452611,-6.073414,-3.906137,7.291886,7.995235,-8.611474,-5.386149,-9.525046,7.184617,-8.935244,6.653010,1.286966,5.146279,-3.298524,7.439362,2.164146,-2.763811,2.868121,-8.881524,-5.765388,9.852755,0.052893,9.768323,-0.340190,1.231123,-3.850302,5.485644,-1.874278,7.835348,-7.058679,-5.278569,9.590355,0.706137,0.902066,-0.926721,1.414571,-9.121031,5.703348,-6.657430,-6.786810,-9.753300,-8.390321,-3.095141,3.041642,-6.291422,-8.951971,3.517113,4.103688,9.597545,2.804183,-2.756708,4.477178,2.561258,9.219263,6.558804,2.956156,-0.916223,9.465986,-5.272959,-6.639837,-1.925332,-8.051536,9.835867,-1.412509,-0.971773,-9.355230,-4.362204,-1.777173,-6.625952,9.543143,2.617982,-4.710199,6.897300,2.910398,-6.006203,-0.865620,-3.454075,-8.475216,-1.129153,-5.827012,-9.972625,-5.660619,3.798703,-7.966923,-5.484739,2.486909,8.492223,2.529512,2.222055,-5.346547,9.799751,8.931855,0.230735,3.104177,-2.054308,4.997217,-9.401436,-3.958965,-5.907118,9.000152,-6.140259,-3.641416,-1.537239,-5.135711,-8.878235,0.647051,7.857050,-5.881162,3.083028,4.310970,8.217575,-7.447438,-1.113236,9.240002,-9.493217,6.455782,0.599962,-7.759907,2.387392,-3.408924,4.375532,8.628976,-2.583303,-3.895758,7.068846,8.431421,-9.935878,-7.205007,-3.897145,2.515116,7.062150,-4.088097,-3.547152,-6.527660,6.888212,-0.222318,2.906092,-8.053075,4.005553,1.156687,-7.800001,2.238697,-7.371301,6.648021,-8.898714,3.668445,8.478841,-7.931759,-8.063679,8.511426,0.682821,0.632851,-7.048612,-9.930448,-7.721832,-2.672959,7.736606,5.796486,-9.467300,-4.112399,3.070362,-0.965054,0.876011,-0.097710,0.883034,-4.282663,8.063553,6.301592,5.833078,7.583028,5.226872,-2.994748,-5.884782,6.724132,-8.016016,3.613731,4.980724,-6.913971,-1.963305,0.009757,-1.103819,0.624159,7.676549,6.446577,-2.078758,-0.097140,8.738343,-2.876486,-0.461088,-8.406817,-9.067421,-2.167744,8.456865,-6.386293,7.634821,5.729873,4.121704,-2.262890,-6.051627,8.347534,-1.520326,-3.891493,-8.629506,9.054418,-9.592587,9.563509,8.497788,6.394094,-7.595903,0.689051,4.752595,-8.796253,6.232064,0.487664,-5.106305,-1.092378,-4.163270,-5.413630,-3.351807,2.524727,7.694663,5.380242,-9.381187,4.001145,-7.238680,-7.025887,-3.423283,7.293902,4.748188,7.305314,4.170311,7.034247,-1.842307,1.749221,4.123551,-2.399322,9.299464,-2.923821,-4.229760,3.699388,-8.046949,-3.410760,-3.774478,-9.330843,-0.191557,4.586154,0.676137,7.293432,6.632484,-6.871256,6.509187,3.510994,-4.141045,-7.122126,-6.698749,-7.709847,6.446221,6.373090,-6.109047,-3.144896,5.079777,-8.100978,-4.324040,-7.791761,-9.286051,-0.266030,6.910665,8.387605,5.567107,-5.734425,6.342451,-2.902792,1.877477,-3.057845,5.626102,-4.430816,-1.825754,-2.513136,-6.695755,-7.313571,5.178709,-3.230239,3.494830,4.430140,9.972028,-7.837094,-8.325981,-3.561717,-2.559389,7.358524,8.560072,-0.523813,-2.713894,-3.853393,8.303465,-3.532508,8.017914,-8.658759,-0.007195,-9.023660,7.656600,-9.496148,9.806997,-2.461327,3.699641,-4.478852,9.263913,-4.813969,5.809978,2.098914,-0.606917,5.680661,-8.718835,-8.809516,3.130620,0.935934,3.139426,-8.913682,-6.503784,-0.529812,-1.280170,-8.410638,6.196338,-4.089045,0.376035,8.029616,7.324726,6.363644,-8.524695,-0.229562,-5.417608,5.382457,8.487955,3.356501,-0.613984,1.012794,-7.171408,-7.538993,-7.197808,-2.286036,-8.943983,2.684681,-6.732403,-0.291149,-4.810225,4.913605,-6.216020,-8.939325,-5.184518,8.228028,3.545290,-3.477438,-0.812021,2.472462,2.426391,-6.484148,-8.607500,1.027144,-0.699242,2.854359,-4.120951,-6.506527,1.002835,-4.372718,-7.757640,-6.675386,-6.973422,2.836924,-2.203050,8.348938,-1.689797,9.629745,-2.646437,6.726498,-8.981403,3.933344,6.204205,1.917994,8.517508,5.465139,5.978731,9.922409,-1.977541,-4.255666,-3.321460,-7.563545,7.225063,7.586071,-9.943744,7.268140,5.929390,5.920119,-3.497878,-6.090857,-4.147624,3.131412,0.178622,5.981521,3.822264,-6.209350,3.551578,-1.848046,9.640226,-2.818850,-5.776095,-9.843309,1.887776,5.758238,1.465996,0.941181,0.638761,0.057285,8.882571,-8.490493,9.017370,-5.464798,9.910808,5.759233,-6.501013,-9.056440,4.664350,5.240249,-5.315098,-2.364012,-9.706210,1.524158,-4.813136,-6.340243,6.305693,-0.585454,-5.091312,8.303159,7.139491,-7.039783,3.619006,6.484585,8.760109,7.009648,4.933777,6.024493,3.113272,8.386864,-1.121568,0.385384,-7.283928,-0.399102,4.563603,-2.642195,-4.025757,-6.020407,2.923784,2.623404,-3.154061,-1.565475,-5.363947,2.260020,-0.174926,-7.809056,1.882647,-1.023031,1.723490,-2.203085,-3.354583,-1.831303,8.558916,-0.742403,-1.868444,8.520748,-7.935256,-8.204878,-8.391417,-3.520732,-2.681787,4.087199,1.122677,1.622471,-9.163030,1.102016,-4.527627,3.199462,-1.952452,-6.107539,5.143487,-1.311864,3.292103,5.301887,-1.686927,-6.963771,-6.730810,-1.174426,8.128985,-9.421731,9.031307,-0.939135,6.331593,0.525959,-4.976008,-5.697295,-1.030787,8.948911,8.968966,6.806073,4.985983,-9.917200,5.965055,6.040603,-0.583545,-7.395565,9.057674,6.034961,-4.117228,-3.829361,-5.997762,3.162856,1.273446,-6.861428,0.756425,5.277591,0.008583,-5.914959,-3.257228,8.888261,7.088327,6.677153,3.930403,-7.094443,9.276868,-6.468324,9.582775,-7.419808,-7.823854,-3.527828,-0.050949,-3.069328,8.122316,-9.021702,-1.000874,8.264198,7.313722,-7.689587,2.110268,1.347413,-0.944627,4.463493,7.110444,-5.214980,-8.748464,0.331477,-3.808466,9.743368,-2.651677,-2.174558,1.324714,-9.359122,-4.468844,3.810702,6.990285,-9.547188,-9.721754,-3.524170,-2.216055,-1.346887,5.084946,7.333466,5.464639,9.283922,4.674204,0.492564,0.785692,4.831495,-6.679911,-2.489751,4.549015,3.677815,-2.399317,3.827978,1.173363,5.690615,0.261858,-1.088590,4.527713,-9.471635,5.616458,-3.788326,-6.190128,-6.600948,-3.736611,-9.505101,-5.512735,-4.739720,2.827587,4.020471,9.268195,2.625299,8.032285,3.057097,-2.323697,3.481722,2.133837,-0.680159,-2.858594,7.279211,6.361497,-6.797943,3.847138,-2.284171,8.037395,0.909095,7.093212,1.065306,7.749273,5.709087,0.754337,5.860766,-2.817903,-8.085284,4.401067,-8.129211,6.232302,-8.833925,7.706963,-1.639730,-2.136476,4.394108,-8.092921,-0.346207,0.703840,3.895471,9.687968,-0.953687,4.373916,-3.912122,-6.634000,7.235888,7.269313,-1.941418,1.222482,5.960972,7.492658,8.060937,-4.675183,4.434914,8.493743,-3.859249,0.177444,7.146954,2.898370,9.377630,-5.471190,3.466362,-6.409350,-2.724949,-4.298727,6.482001,-3.741757,-4.623865,1.993546,-0.019166,-6.066905,5.796374,6.777676,-7.718661,-1.343535,-0.183647,8.892513,-8.680347,-6.388513,6.731286,1.254932,-5.889982,3.418461,-1.796799,-7.441050,3.138873,8.735643,-3.192407,6.709902,0.270990,3.465534,-5.479401,8.407565,-9.211983,8.865239,1.721590,7.222881,-9.802954,-1.520219,3.138453,-5.128971,3.516840,4.965842,-1.270806,4.143697,-2.956698,-5.348050,4.414955,7.452684,5.709449,7.638847,8.633230,-9.600346,4.340007,-4.501297,0.426034,4.801449,-6.079629,-0.106317,-5.569978,-4.435897,-9.503328,7.468149,9.368857,-0.141716,-7.523429,3.223024,-3.460232,0.422181,-2.441362,-6.578551,-6.243135,-1.554550,-2.323153,-3.165751,-8.612525,1.692682,2.095366,-8.690550,6.898248,8.399169,-7.690859,-6.649947,-2.532773,-3.940835,3.872623,-4.736800,8.902560,7.267521,4.554138,-9.071588,-0.252453,1.943142,-8.690681,-3.357393,-6.274279,2.307155,-1.546645,8.713220,-2.363432,5.792874,-8.054700,2.384601,0.261661,5.006041,-1.154186,-5.004821,2.955514,-6.385636,-6.862301,2.991261,-6.022019,0.989317,-0.517164,0.316058,1.323648,6.592795,-7.120192,1.420577,5.921196,5.146609,-3.921821,-3.311594,0.511064,1.065153,-4.012190,-9.562270,-2.059181,7.407009,-0.727796,0.192852,-7.070243,5.527049,8.380837,-7.029109,8.807213,5.595540,7.987652,6.635943,-9.593149,-5.740102,2.841832,-1.256272,7.658566,2.525725,-5.720413,3.387261,1.640316,-2.897181,3.864114,7.651909,-4.174994,-0.383134,-1.762687,-1.275907,-0.198066,8.268531,6.739527,8.500946,-3.686114,-9.455102,5.789640,9.972033,-5.947068,-7.728323,-2.850068,-6.546390,-1.025410,-4.618096,-8.075786,2.961212,-6.234920,-8.912676,-1.940521,-6.169241,-2.200778,-2.468082,-3.352104,-5.849737,9.840578,-6.219384,-2.285299,-0.921332,2.545321,-5.912169,9.958097,-1.356293,-8.229826,4.568515,3.843988,1.929902,-8.373251,8.857443,9.627694,2.321383,-4.786271,-7.131677,-8.779553,6.128863,-9.975628,4.315771,-0.751810,5.834909,-5.416126,2.828450,-1.977355,-6.204637,-2.326654,9.789193,4.686247,-0.276282,-1.200378,4.024275,8.105078,-7.318247,-6.427397,5.061401,1.283814,1.094023,1.856852,5.023559,-6.250387,-4.027367,-4.198561,-4.938730,-1.311374,9.881971,-5.392555,4.541245,-6.621860,1.513043,5.112082,4.276289,2.045858,0.630164,5.376692,-8.242982,-6.358546,9.539067,-3.745953,-7.392098,-2.919376,4.471801,-4.368540,4.507773,-3.322636,7.911106,7.573691,-9.339564,-7.840335,-9.362221,0.487950,1.640542,3.527955,-0.404521,-5.182746,6.002837,-3.896452,7.094579,9.012229,5.805194,5.279316,-5.605279,0.497933,0.339040,-7.280080,-8.446840,-9.327142,8.540272,-8.915545,7.922139,-0.232683,1.302719,4.312834,-1.177968,7.972351,-2.141300,-0.880630,-6.638302,-1.809597,6.780624,4.985553,-1.263652,8.329260,4.511169,0.609472,4.438336,4.082717,-9.661382,8.836463,-6.137001,2.442052,-6.579355,9.912987,6.193007,-0.226791,-5.668801,-4.128556,-9.906501,-7.954226,4.475331,-2.257013,0.490105,-0.366275,5.876174,-7.078252,-8.712192,-7.319494,-3.768240,4.319117,6.595364,-1.948545,4.994645,-1.081481,9.886251,-3.192134,-9.413402,7.901785,-3.797944,-5.706251,8.319119,9.093723,-2.274267,-8.947716,8.108330,-2.699258,-1.637559,-5.335276,-2.484136,5.007498,1.779185,-3.518528,-8.307900,-2.120111,8.734663,-9.835646,6.058605,6.554314,-9.690932,-8.150317,9.645285,-2.587354,-4.133078,-9.043809,-8.140322,-1.062126,6.302878,1.482935,-0.628930,-5.698054,-4.231888,-0.609371,7.500137,0.936852,-8.621163,4.496271,6.506503,8.964391,9.215106,-4.272189,8.532303,2.951478,2.433247,-2.928270,-5.927099,-2.671652,-8.578771,9.942139,-5.226094,7.607505,-8.262797,-1.664310,-1.415212,4.649395,4.276343,9.313682,-4.410111,3.105501,-9.997249,3.124131,6.489635,2.165024,1.486059,0.987878,-6.063824,-6.786974,7.464071,-6.136272,-6.656435,4.703540,6.390538,-8.904211,-3.352297,8.441520,3.852278,8.482360,-2.168292,-8.092621,7.541929,2.736789,-4.993792,7.893724,1.186518,-2.124026,3.624770,3.562655,-8.667821,6.704846,-1.893043,7.081160,2.671717,-9.090308,-5.555310,7.714112,-0.158146,2.008565,-3.311783,-8.825098,-6.301448,2.033701,7.799649,-8.269399,-6.759577,-7.928470,-4.502680,1.418985,-7.838932,-0.594025,-7.698416,3.908691,-9.818412,-7.391596,1.908803,-0.261315,5.226202,7.911149,0.458635,-1.571111,2.225041,-8.498213,5.648059,-6.414029,2.921568,-1.494647,-3.026539,-2.378498,-8.533793,-7.346163,0.062864,5.362237,-3.157811,1.788380,-7.131864,-5.415669,-6.062952,4.021042,-0.357135,-2.780992,-4.044817,4.686850,-4.816634,-9.628248,-0.214703,-2.271977,4.390525,-2.287909,-0.235318,1.152725,-8.031364,9.946056,-7.183259,-4.461274,-1.290985,-5.475639,1.270395,7.569727,0.717098,-3.204813,-5.102861,-9.920776,-1.277169,-6.555664,-4.299283,1.922489,3.223554,-4.444598,2.685748,-2.126071,0.890305,4.743904,-9.251427,-6.122274,-3.990262,-3.710587,6.355862,-0.703861,3.121104,-7.912330,2.007661,-1.412351,-2.144514,-4.980060,4.332230,5.813445,-4.020793,2.531439,-8.297485,-7.642403,-4.752926,2.384303,5.618176,8.795925,-9.169246,7.149508,0.402170,-3.677557,-6.848086,-6.435695,8.897406,-0.099747,-5.452014,6.612770,8.989310,4.130142,-2.388072,9.279499,-6.653177,-1.300777,-3.493429,-8.774315,-0.416495,-8.469672,-5.334924,-6.670503,-0.034576,9.669158,1.165260,3.830253,-8.432082,-3.823036,-5.393772,9.220935,6.835533,4.368755,0.946690,8.284371,6.745317,-8.468456,-1.624254,1.489749,3.856230,6.722587,4.841030,5.976861,3.923758,-6.735539,5.357393,0.141734,-7.435430,-3.186843,-7.202582,5.878786,9.182701,9.945428,-1.662894,5.948041,7.345797,-7.654673,7.816042,4.927495,-1.519210,-1.943818,8.193427,-0.094093,3.038755,9.044213,-1.298896,4.021082,-8.516034,-2.048965,5.159393,-4.954604,-2.546160,-2.177070,-3.099388,9.948081,2.602616,-2.796600,6.268122,-6.390213,2.701942,-2.691937,-4.844929,-5.172102,6.696870,-9.728319,-3.166560,0.313711,5.854277,-2.558173,1.245579,-2.964258,-3.283157,0.691821,9.336001,-7.570838,3.794651,1.171024,-7.730494,-9.600129,-5.470265,-6.430531,5.963063,8.422086,1.404298,-9.462287,6.832577,-8.776456,3.439474,4.789802,2.998829,-0.767389,3.413736,9.440067,2.460892,4.209033,-9.236155,-8.004453,4.939357,-7.207212,3.088921,-8.374738,-3.359469,-1.566642,-5.079735,-6.314873,7.247843,9.957045,-9.312485,-2.283043,-9.139299,3.177038,-2.824233,1.379671,-7.865303,-9.765476,-7.619081,-0.067202,8.529143,8.410277,2.681215,-9.407900,-1.792211,2.090236,-0.481501,-2.263107,5.263598,3.150108,4.964870,9.373964,-6.979572,8.036213,-8.871519,1.134770,9.626905,-5.054910,2.526438,2.140062,-0.689609,-6.047992,2.078884,8.575930,8.324471,-7.934614,6.173882,-9.010519,1.288768,3.851176,4.062911,-7.750843,5.751109,3.172398,0.481606,-2.003572,1.685840,-1.912224,0.911761,7.122022,-7.187751,7.918277,-4.470342,6.781097,0.484844,8.223110,-6.911726,0.300658,-1.399983,-4.070534,-1.650108,3.178696,3.597644,-4.668522,-8.792749,9.989345,6.138914,-5.938071,-7.789929,1.683261,-1.841398,8.710499,-2.032101,-3.236797,3.700399,-8.828106,7.280492,-4.411189,3.484004,6.311427,-3.267641,-5.759431,5.246597,0.064333,9.919612,-6.475994,-3.700679,-3.120746,-2.920953,3.223642,3.334261,2.493096,-5.126049,1.115374,-6.930736,6.771321,-5.399096,-6.779293,-0.829446,1.215676,7.262258,-7.118391,3.455230,-2.646147,0.844258,-7.618783,-5.267905,-0.252927,5.146165,-2.209500,-1.851006,-4.826941,-4.847811,8.575075,8.128467,-4.578406,-7.643260,-1.410930,8.150826,8.833814,-3.680423,3.290602,-4.822293,5.011262,9.365243,1.491396,0.358366,-7.238831,4.369433,8.050367,5.514322,3.285587,-4.078866,9.881639,-6.777995,-9.492990,-3.703886,4.870085,1.609165,-1.084216,5.376521,8.648655,-9.509065,-6.359654,5.101942,-0.703200,1.585812,-2.236941,0.068206,4.667653,-6.377043,-3.250176,0.230904,1.581896,1.682113,9.575714,-6.786284,8.915726,7.590578,-6.157797,7.918505,4.540372,-3.554399,-5.196503,1.578945,9.768093,-5.393816,8.063312,-3.220555,-8.608154,-4.443507,-3.907622,-6.654511,8.732631,6.059080,-2.066710,-3.746750,7.911753,9.047277,-6.664862,7.708939,0.954626,-7.665526,3.409673,6.920627,-4.737265,2.869945,-6.998575,-5.915783,9.188053,9.535851,5.398602,5.033097,-4.567309,-9.914641,-0.670529,9.827214,6.329964,-6.631091,-3.124966,3.387734,1.842185,6.650878,-2.225494,-0.506474,5.504676,-4.379006,8.614328,2.599059,-6.751675,5.446516,5.684230,-5.467712,-4.399717,0.100353,5.870554,0.633678,5.040037,-6.240568,-6.519714,-7.831675,1.532444,-4.317270,-2.853179,-6.194404,-6.878707,2.925181,-2.908349,-6.787081,-2.017892,9.322762,-9.383347,3.199623,2.837629,-9.142583,-9.673903,3.920144,0.739211,-4.770284,8.770379,-6.340561,-0.254368,0.561185,-4.392646,8.593438,9.833054,-5.310152,9.550517,-9.707703,8.628214,6.615456,1.154714,4.505591,-6.306345,-2.910526,6.460428,2.206289,2.489043,-0.615649,7.091651,-3.970959,7.964844,-2.368248,-1.642225,5.566734,0.019343,8.470948,-1.178319,5.879713,2.812106,-2.293662,6.736561,-0.688856,4.501768,-1.066407,0.448161,0.195725,2.126375,7.326834,-5.811336,6.995302,7.627869,-0.354341,-4.911662,0.997187,-8.859338,-9.458895,1.420374,-5.425941,6.684914,5.414625,2.499782,1.959552,3.887772,7.286573,-6.941391,7.662446,6.706476,6.144823,-7.723571,3.064186,-1.465570,-9.778893,6.982911,-3.372944,2.394626,6.362976,7.642906,2.444655,8.743877,-8.723032,3.620880,-9.351498,-5.935060,-1.381737,-5.566237,9.411887,5.569799,-9.720461,-4.839657,-8.582624,4.141564,-4.295742,-6.592703,7.759607,-4.868155,4.587492,8.107790,3.710681,8.822141,-1.408734,2.664743,5.228634,2.067765,1.927977,-0.398262,1.790681,6.260780,-7.562281,7.870308,-8.130673,-7.709996,-1.565710,0.734868,8.925866,4.228921,-2.680837,4.924224,-8.288732,7.263019,-8.071155,7.175680,9.023274,9.289657,-6.062755,5.696998,3.155782,6.342976,-9.110290,5.161229,1.199797,8.000890,0.969023,0.832752,-6.248241,-4.579289,2.850446,-4.825070,-0.352542,-3.118018,6.418589,1.926578,0.375304,-3.390729,3.368270,4.973579,-7.941679,-7.515696,9.748937,3.850763,3.079580,-7.450848,2.448330,9.293126,9.314005,0.065175,-8.870174,0.745514,4.091044,0.532471,3.821321,3.208337,0.543274,0.842040,-1.313233,-0.009454,-0.558378,-8.360205,-8.289206,-3.819070,7.137679,-0.108388,-2.982694,-5.201709,3.981952,4.863218,-0.476676,-2.128384,-5.582682,5.154605,3.966368,-4.727672,-5.211639,3.795945,4.879875,-1.317966,5.216357,-0.494022,-6.217468,6.940271,-0.801842,-6.518800,-6.019414,-6.817567,2.881896,5.098693,-7.566780,-9.585446,-6.090072,5.412321,8.846629,-7.113237,-9.446245,9.928217,9.086944,-6.046761,0.104876,6.442384,5.621209,-3.798005,2.158167,1.405277,-6.630143,-7.130372,-3.331155,-0.467933,-7.215686,-2.064179,3.453927,4.158946,3.801988,-1.815302,2.108334,-3.360918,0.621946,1.715893,-4.916833,-4.560012,-0.401020,6.375136,-4.575062,2.596741,-8.238049,3.846626,6.206875,9.923187,-2.151379,7.161117,7.690121,6.243792,-4.029331,7.262812,7.107404,6.641069,-8.956450,-6.427553,-9.577685,3.892910,-2.646738,-3.055108,-3.735555,-9.126017,5.802910,-9.924025,6.270282,-9.157554,-0.555318,-3.877729,0.999522,3.046822,-9.423593,3.784543,1.492046,5.155644,9.317343,4.586338,7.741414,4.991456,9.649798,1.862969,9.394076,4.597531,3.579662,3.334197,8.066509,3.122561,2.918407,4.190635,9.658888,-2.003709,-9.887634,-7.702887,4.798308,8.754501,8.112340,2.897352,-5.087123,-9.043726,-0.279922,-5.418249,2.639104,7.288796,-4.336520,6.114309,8.706440,6.672246,-1.527641,-6.642881,4.185150,-6.200395,-2.243949,8.215659,-9.114286,3.676897,3.943220,1.153647,6.734652,5.167183,9.157045,0.762146,-4.282516,-9.368023,1.931866,-7.329540,-6.576224,1.909261,-0.506977,9.959095,4.714675,3.948588,1.392133,7.671146,0.818983,-7.516374,1.591771,-2.041878,-0.739344,-5.930799,0.769948,-0.347978,-0.972232,-7.808000,-8.241492,1.727818,-6.550058,9.364211,7.670645,-8.999040,2.333146,4.450382,2.726169,4.151176,3.732663,4.147407,-0.961203,-8.850278,0.089300,-0.889558,8.790741,9.618687,-9.799213,2.703956,3.311151,9.569356,-8.185189,-2.073086,-2.033040,-4.634447,8.647417,-5.030236,8.070278,-8.268061,4.841452,3.528165,6.013265,1.761288,2.285543,4.698788,-7.961531,3.719208,-8.044709,-9.295418,0.462258,-7.013925,-1.623785,1.733621,9.475462,7.920815,-4.355769,8.357039,0.520018,1.099284,6.658544,-2.882347,2.376832,2.683074,1.155308,-4.900744,-9.788648,3.061483,5.441814,-6.141366,6.180565,-1.701486,-3.719800,4.160188,-5.171383,-2.596326,8.078694,2.806291,0.246618,-1.119649,2.047333,7.372449,9.088148,-6.113361,3.141953,-4.370431,-1.390816,-3.492890,-5.646265,4.099971,3.762433,9.689567,-5.213071,0.705632,2.555161,-3.730495,3.624361,-5.230658,-7.101008,9.233732,4.326516,-9.192587,-2.196032,2.859927,-0.408359,8.684243,-9.565552,0.595064,-4.114089,-8.797533,-8.445536,-1.853773,0.222633,3.687235,6.837075,7.139130,-7.217587,7.084635,5.090049,3.590948,9.046992,5.856156,2.928444,-0.994813,9.717775,5.802208,9.528443,7.839128,-8.549229,-8.649604,-7.155936,3.894186,-8.786280,1.106379,6.335526,6.929870,-1.209338,-8.697000,2.579784,9.655627,-8.293104,7.035450,-7.762606,-1.220728,0.250290,-4.686423,-5.764806,-5.496844,-5.982969,-7.219284,-5.592402,-8.075987,-9.855066,7.824727,2.601673,1.814942,5.665917,5.586084,6.194653,4.381220,8.604852,-5.609048,6.490396,-8.576169,8.351902,4.096757,-8.601924,-5.363447,-2.370466,0.248096,-2.997047,8.925964,0.267341,7.247245,-9.335771,8.132724,-4.206141,-9.724142,-2.603123,-5.888520,3.429742,2.640175,8.357383,9.750001,8.011202,-1.282055,6.042686,-7.877642,-2.482949,2.224969,-6.007627,-6.725942,3.788176,-4.649479,8.344328,2.921780,-4.508974,5.079982,-7.225269,5.936571,6.318769,4.257135,-1.474710,7.169740,9.616771,8.818117,6.973085,-5.342070,-8.543440,-1.413916,5.260082,7.407478,-1.414331,-4.607031,5.187825,4.296045,0.104448,3.491393,-1.215025,-6.047478,8.022384,7.676915,-1.332136,4.092488,-9.415785,-6.798278,7.590164,1.166553,-4.764387,-2.744696,9.974859,-2.569440,-6.059204,-1.799245,-2.345556,-0.817114,0.382421,-7.478087,-3.915680,-5.681014,7.798401,-1.666139,-7.431999,7.567202,9.671447,-6.804472,9.715172,4.865482,-4.006525,-3.794532,5.058152,6.196307,-7.152204,-8.320714,9.067739,3.837150,6.172734,-6.530172,7.687041,9.984519,0.311877,9.840451,-4.711844,4.367699,3.961717,-9.018789,-5.463810,6.369052,1.994763,2.806750,-2.040192,-5.075375,4.249637,-6.518857,-1.860338,6.121647,1.807589,-1.921550,-8.019246,7.107079,9.203484,-1.293641,9.721869,-4.612850,3.384121,3.040765,-8.605669,2.350579,-1.672180,-2.465255,1.876525,3.919472,-0.370179,1.761412,0.938186,-2.517598,-9.943999,-8.298321,-4.985580,-9.086405,2.018154,-7.046825,8.761404,0.549532,8.253241,-0.026808,5.263472,9.078496,4.072007,-3.333984,5.290907,8.674139,6.820771,5.740648,-7.191584,4.912976,-4.211135,4.659494,-2.535645,1.230242,-1.310271,-4.868552,8.839902,-8.427392,-2.144036,9.886906,5.342787,4.104385,2.439788,3.518562,3.170224,3.979125,-4.823418,4.748482,3.820038,-4.715711,7.455837,0.706999,-1.625759,9.133837,5.436157,3.986726,-2.628892,2.236717,1.859199,6.525223,-5.354380,-4.066206,-1.606181,0.792745,7.123130,1.841260,-1.493618,4.802391,-8.010034,-1.268010,-0.451680,6.295420,-5.121953,-0.145746,1.237107,-5.909243,-1.965925,-4.566598,0.044823,-9.138038,1.280467,6.257478,-8.760185,-3.537992,7.341422,-5.318283,-9.474283,-0.920210,6.159918,2.244071,6.524743,-1.975454,-1.464889,-9.453015,-4.588562,-9.378406,-9.412850,1.432931,5.538458,-5.479487,-6.759488,-7.959495,-4.984151,-3.758912,6.301884,-6.551740,5.925393,-8.368192,3.172526,8.827582,6.561920,8.186598,6.549207,-6.723713,-5.691698,-3.075210,-8.658720,-7.727477,0.765455,-6.925698,-8.254568,4.359776,1.697971,1.384333,-3.818607,-9.618762,5.169544,-6.205961,-3.742670,0.641576,6.178668,-6.001623,-5.848547,-0.064408,8.212379,-3.251855,2.091110,4.396897,3.068138,0.578855,-9.193627,2.721902,6.526572,-8.173736,-6.319072,-1.970148,0.839756,7.761593,3.269289,-9.459786,-7.373372,-0.086483,-1.883764,-6.235223,3.728178,-3.898710,8.060698,1.291851,8.325152,9.199621,1.976292,0.003153,-4.681406,-9.374165,-9.518211,-2.166202,3.121053,-1.325228,-4.997199,6.352307,-5.417077,1.854617,1.853431,-8.782341,4.797537,-1.861782,9.172729,9.419419,7.091532,-2.785328,-2.801053,-1.253077,7.087465,-9.972732,-6.592127,4.092765,8.650061,-7.654587,5.180604,7.128306,-0.105341,1.630036,1.210721,3.474545,-2.177079,-3.780886,-3.910421,-0.302751,7.120882,-4.430602,-6.187032,-6.451680,-6.774626,-3.779344,9.406927,-3.497614,-3.814397,1.268617,9.530116,-8.487540,-4.035924,-2.407232,4.748177,8.525750,9.493990,-8.300160,2.802850,0.560966,-8.631341,-5.199040,3.202183,0.138769,-8.709796,8.057273,-2.048738,-3.538060,-2.905978,9.114259,7.462154,-9.824417,-2.279193,3.541071,0.845469,-8.722731,-6.336144,5.268429,1.664307,7.708403,-5.099479,8.055627,-8.608471,7.881707,8.636796,6.737914,5.368952,7.082152,-3.591798,-8.049664,-4.004340,3.464795,5.825192,-4.435499,-5.556581,-5.091327,6.258527,3.430577,0.918158,-2.826845,1.232054,-4.196245,-6.339061,5.031930,-5.193688,-6.042828,-4.137531,0.828117,2.513094,-5.081974,-0.430957,-0.273810,2.111460,8.589752,-1.043498,0.442007,3.225602,0.184611,4.314602,3.214442,-0.189247,-4.734714,6.527425,-2.877837,-4.268123,-1.388106,8.656874,-1.321681,-3.688313,-0.138060,3.069241,4.312989,8.408896,-4.088801,6.455003,-0.256933,-9.436717,-4.529058,-6.086478,-8.730891,9.373721,6.488861,5.746148,3.380961,-6.676754,-6.426804,6.228219,-2.518884,-7.373480,-4.313057,-5.992881,6.759284,4.487971,5.196619,-6.333094,-1.075097,-5.182324,0.781551,3.117871,-2.890925,-9.281627,-9.583914,-5.919464,-7.860626,1.728591,-7.297336,0.715295,-8.181743,9.522225,-2.426093,2.066427,9.276093,8.657975,4.966105,-6.960598,-2.475804,3.591869,-2.063202,9.273913,-4.043743,1.420970,1.686443,0.544664,-9.098386,5.434639,-8.501079,3.694752,-0.256377,-3.137939,-5.047397,1.818409,9.345207,8.856983,-1.920455,-7.727852,2.227433,7.563225,-3.976438,1.281078,4.210138,-9.511090,2.466570,-9.334330,-9.656006,-6.881206,9.611049,8.170030,-2.553928,-2.722139,7.425068,7.426608,7.031299,2.763529,2.080928,-3.644369,4.246629,5.998562,-7.606143,4.773090,-2.537966,2.594009,2.026262,4.024947,8.842273,4.138491,-7.075031,-6.192675,6.970439,-9.185377,-4.340287,-1.825774,7.202476,-8.035425,4.746841,-0.887963,6.579479,2.010334,-3.170029,-2.696174,-7.625539,-8.808303,1.690451,-5.810029,6.652291,4.199113,7.917690,0.225416,6.843521,4.225804,9.921747,7.899547,9.517898,-0.586642,5.965248,-6.466639,-4.888598,-0.491045,1.761685,-5.305959,2.125221,-6.013814,0.170605,2.217496,8.589568,9.884370,-1.218456,-0.014671,2.386467,3.259676,4.916361,0.877436,2.836630,9.875719,-4.042303,2.093626,-8.205171,2.360235,0.995022,-1.132647,1.095646,-8.482432,-5.207180,8.992409,6.306126,-9.718535,-2.278067,-3.550046,-6.604734,-8.470812,9.810272,-3.762713,3.811679,-6.276265,5.967289,-1.392934,-6.407495,-4.018833,0.437124,9.940756,8.257838,8.671766,1.659347,7.662967,-0.750410,-1.929605,5.511480,5.376394,-9.299361,6.448868,-0.187750,-1.875227,-5.433647,-0.264103,8.315016,-7.888602,4.194839,-9.641057,0.116207,-1.654938,-2.594635,-6.770872,-1.606642,-5.951084,3.336790,-8.079838,5.078997,-4.064740,9.046699,3.060502,-8.244131,1.463365,-8.588922,-6.161084,4.046800,9.026378,-6.441297,4.006755,0.982296,1.398199,-2.675897,-3.042795,7.319815,8.286790,8.228591,8.071862,1.245136,-2.701307,-1.384840,5.176918,4.762532,3.961370,-9.788108,-9.335834,8.993944,-4.687861,5.137456,4.133542,-1.491098,-2.989720,-8.658424,4.986563,-8.797035,6.954596,3.619665,5.564554,9.609797,-7.272222,9.395461,3.244711,-2.700809,-5.600940,-3.272740,-6.438338,6.552915,0.165604,-5.612531,4.522625,-1.424975,-1.716987,9.932249,-7.534536,-4.247601,4.754436,-6.129086,-2.579728,-2.798926,-1.128078,7.097156,2.126456,1.262365,-1.103263,-0.282638,4.869839,-9.490724,-0.229852,9.363364,-2.900211,8.224169,2.366565,-3.201402,-0.979006,2.450037,0.993116,-3.710551,2.874246,1.797240,5.135966,0.748319,-7.427800,-7.665543,7.937038,-9.677137,-2.173057,7.841012,4.279520,9.177329,2.510851,-0.526709,0.024716,2.054487,9.031225,-8.871667,-3.486777,4.982690,8.697109,1.980716,4.703028,-2.792284,7.759010,3.113025,7.462369,4.602556,7.601021,-3.629295,-8.526420,9.050079,-7.819434,-7.455217,8.634417,-2.120386,-6.137251,-9.781256,8.267092,0.435001,-7.893008,2.794423,3.575589,-3.378185,-0.487300,-2.535333,0.775407,-2.788278,0.732652,-2.912130,-0.768664,-2.666071,6.942386,-4.388174,7.114191,4.261447,5.813341,-6.078144,7.307491,4.774543,4.385092,-7.042173,-7.319014,-5.764248,-2.405976,-5.404330,7.426279,4.096805,8.235291,0.789808,2.032904,1.516523,9.728060,1.295734,-8.198154,6.561997,-9.602744,-2.847532,-7.560810,8.329053,-4.537674,-9.460108,-7.943086,-3.046658,4.669162,-4.719395,-8.767617,5.587748,2.224131,3.028838,-2.138008,3.304893,-1.017014,0.010402,2.069530,0.345133,-2.225724,7.229470,7.114805,6.707698,-0.300859,3.589699,2.856449,-1.033979,-9.998986,-9.491573,-0.649111,9.231000], dtype = "float32")#candidate|10120|(3600,)|const|float32
call_10118 = relay.TupleGetItem(func_8319_call(relay.reshape(var_10119.astype('float32'), [36, 6]), relay.reshape(const_10120.astype('float32'), [3600,]), ), 6)
call_10121 = relay.TupleGetItem(func_8323_call(relay.reshape(var_10119.astype('float32'), [36, 6]), relay.reshape(const_10120.astype('float32'), [3600,]), ), 6)
output = relay.Tuple([bop_10105,call_10118,var_10119,const_10120,])
output2 = relay.Tuple([bop_10105,call_10121,var_10119,const_10120,])
func_10126 = relay.Function([var_10104,var_10119,], output)
mod['func_10126'] = func_10126
mod = relay.transform.InferType()(mod)
var_10127 = relay.var("var_10127", dtype = "int8", shape = (14, 14, 13))#candidate|10127|(14, 14, 13)|var|int8
var_10128 = relay.var("var_10128", dtype = "float32", shape = (216,))#candidate|10128|(216,)|var|float32
output = func_10126(var_10127,var_10128,)
func_10129 = relay.Function([var_10127,var_10128,], output)
mutated_mod['func_10129'] = func_10129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9449_call = mod.get_global_var('func_9449')
func_9450_call = mutated_mod.get_global_var('func_9450')
call_10163 = relay.TupleGetItem(func_9449_call(), 1)
call_10164 = relay.TupleGetItem(func_9450_call(), 1)
output = relay.Tuple([call_10163,])
output2 = relay.Tuple([call_10164,])
func_10184 = relay.Function([], output)
mod['func_10184'] = func_10184
mod = relay.transform.InferType()(mod)
mutated_mod['func_10184'] = func_10184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10184_call = mutated_mod.get_global_var('func_10184')
call_10185 = func_10184_call()
output = call_10185
func_10186 = relay.Function([], output)
mutated_mod['func_10186'] = func_10186
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8238_call = mod.get_global_var('func_8238')
func_8240_call = mutated_mod.get_global_var('func_8240')
call_10218 = relay.TupleGetItem(func_8238_call(), 0)
call_10219 = relay.TupleGetItem(func_8240_call(), 0)
func_8199_call = mod.get_global_var('func_8199')
func_8203_call = mutated_mod.get_global_var('func_8203')
var_10243 = relay.var("var_10243", dtype = "float32", shape = (2, 1800))#candidate|10243|(2, 1800)|var|float32
const_10244 = relay.const([[-10,2,4],[2,-1,5],[8,-8,-4],[-4,2,-3],[5,10,3],[7,9,-3],[7,3,6],[7,10,2],[8,6,6],[-7,-7,4],[2,-3,-3],[8,-4,8],[-8,8,10],[-2,8,8],[-9,4,-9],[6,-2,-4],[7,-2,2],[-3,-7,-6],[10,5,6],[-9,8,3],[-2,1,-9],[-8,7,-7],[2,-7,10],[-5,-1,-8],[4,2,-3],[-1,3,10],[9,8,7],[-4,7,7],[-7,10,3],[-3,-7,10],[9,6,5],[5,3,-9],[1,1,-5],[5,-3,9],[5,6,6],[-4,9,-8],[8,-8,9],[3,-1,5],[-3,9,5],[3,-8,2],[6,1,-7],[-10,4,-8],[-5,2,3],[3,10,-3],[8,7,-6],[-3,6,-8],[5,-10,7],[-4,6,10],[5,-9,-7],[-2,-2,-4],[9,-1,-9],[9,-8,-5],[-6,-9,2],[4,-5,4],[7,9,-4],[-8,-8,7],[-9,-3,3],[3,-6,-4],[4,-6,10],[4,-6,7],[-6,3,5],[3,-6,2],[-6,-9,-9],[-9,-10,5],[8,9,2],[4,-2,-10],[-8,-10,1],[4,-9,8],[-7,-5,5],[-8,9,7],[-5,9,-9],[-6,-4,-1],[-10,-2,7],[9,8,-10],[-3,-6,-8],[-4,-3,2],[-2,10,5],[-10,-4,4],[-2,-7,6],[-5,-8,1],[-3,10,-10],[1,3,9],[-1,-2,3],[8,10,8],[-3,-5,4],[-8,5,-5],[2,-8,-7],[2,-7,-5],[-2,-8,8],[-8,-8,3],[-3,1,1],[-2,3,-8],[8,-10,-6],[-7,-8,1],[-2,-9,4],[-2,-5,4],[10,8,5],[-6,8,7],[-9,-2,-1],[4,-2,4],[5,4,1],[-7,-1,6],[3,-8,-8],[-4,-3,-5],[-7,-8,10],[-8,7,8],[-7,1,-9],[5,-9,-4],[-10,-3,3],[7,-4,1],[-4,10,1],[1,2,6],[-7,5,4],[2,-6,-8],[10,10,-2],[-10,2,-10],[-10,10,3],[5,-9,-5],[-10,8,1],[-6,3,6],[1,-2,6],[5,-2,-7],[-3,4,-3],[-4,7,10],[9,-8,-3],[8,10,8],[-3,-3,-10],[-2,3,6],[9,8,1],[4,3,4],[8,-2,5],[6,3,-5],[-10,-7,-4],[-8,2,-9],[-3,4,-8],[-3,-4,7],[-7,9,2],[4,-2,-6],[3,-1,9],[9,-4,-7],[-3,9,7],[9,10,-3],[-2,6,-7],[2,6,6],[-3,7,-8],[-10,-5,10],[-6,8,-7],[-10,-8,-4],[-9,-9,-2],[-2,8,2]], dtype = "int8")#candidate|10244|(150, 3)|const|int8
call_10242 = relay.TupleGetItem(func_8199_call(relay.reshape(var_10243.astype('float32'), [20, 180]), relay.reshape(const_10244.astype('int8'), [5, 90]), ), 4)
call_10245 = relay.TupleGetItem(func_8203_call(relay.reshape(var_10243.astype('float32'), [20, 180]), relay.reshape(const_10244.astype('int8'), [5, 90]), ), 4)
func_5031_call = mod.get_global_var('func_5031')
func_5032_call = mutated_mod.get_global_var('func_5032')
call_10259 = func_5031_call()
call_10260 = func_5031_call()
output = relay.Tuple([call_10218,call_10242,var_10243,const_10244,call_10259,])
output2 = relay.Tuple([call_10219,call_10245,var_10243,const_10244,call_10260,])
func_10265 = relay.Function([var_10243,], output)
mod['func_10265'] = func_10265
mod = relay.transform.InferType()(mod)
var_10266 = relay.var("var_10266", dtype = "float32", shape = (2, 1800))#candidate|10266|(2, 1800)|var|float32
output = func_10265(var_10266)
func_10267 = relay.Function([var_10266], output)
mutated_mod['func_10267'] = func_10267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8032_call = mod.get_global_var('func_8032')
func_8033_call = mutated_mod.get_global_var('func_8033')
call_10285 = func_8032_call()
call_10286 = func_8032_call()
output = relay.Tuple([call_10285,])
output2 = relay.Tuple([call_10286,])
func_10299 = relay.Function([], output)
mod['func_10299'] = func_10299
mod = relay.transform.InferType()(mod)
output = func_10299()
func_10300 = relay.Function([], output)
mutated_mod['func_10300'] = func_10300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1264_call = mod.get_global_var('func_1264')
func_1265_call = mutated_mod.get_global_var('func_1265')
call_10315 = relay.TupleGetItem(func_1264_call(), 1)
call_10316 = relay.TupleGetItem(func_1265_call(), 1)
output = call_10315
output2 = call_10316
func_10336 = relay.Function([], output)
mod['func_10336'] = func_10336
mod = relay.transform.InferType()(mod)
output = func_10336()
func_10337 = relay.Function([], output)
mutated_mod['func_10337'] = func_10337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5308_call = mod.get_global_var('func_5308')
func_5310_call = mutated_mod.get_global_var('func_5310')
call_10344 = relay.TupleGetItem(func_5308_call(), 5)
call_10345 = relay.TupleGetItem(func_5310_call(), 5)
func_8666_call = mod.get_global_var('func_8666')
func_8668_call = mutated_mod.get_global_var('func_8668')
call_10350 = relay.TupleGetItem(func_8666_call(), 0)
call_10351 = relay.TupleGetItem(func_8668_call(), 0)
func_1907_call = mod.get_global_var('func_1907')
func_1911_call = mutated_mod.get_global_var('func_1911')
var_10362 = relay.var("var_10362", dtype = "int16", shape = ())#candidate|10362|()|var|int16
var_10363 = relay.var("var_10363", dtype = "int16", shape = (2700,))#candidate|10363|(2700,)|var|int16
call_10361 = relay.TupleGetItem(func_1907_call(relay.reshape(var_10362.astype('int16'), []), relay.reshape(var_10363.astype('int16'), [12, 15, 15]), ), 0)
call_10364 = relay.TupleGetItem(func_1911_call(relay.reshape(var_10362.astype('int16'), []), relay.reshape(var_10363.astype('int16'), [12, 15, 15]), ), 0)
output = relay.Tuple([call_10344,call_10350,call_10361,var_10362,var_10363,])
output2 = relay.Tuple([call_10345,call_10351,call_10364,var_10362,var_10363,])
func_10367 = relay.Function([var_10362,var_10363,], output)
mod['func_10367'] = func_10367
mod = relay.transform.InferType()(mod)
mutated_mod['func_10367'] = func_10367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10367_call = mutated_mod.get_global_var('func_10367')
var_10369 = relay.var("var_10369", dtype = "int16", shape = ())#candidate|10369|()|var|int16
var_10370 = relay.var("var_10370", dtype = "int16", shape = (2700,))#candidate|10370|(2700,)|var|int16
call_10368 = func_10367_call(var_10369,var_10370,)
output = call_10368
func_10371 = relay.Function([var_10369,var_10370,], output)
mutated_mod['func_10371'] = func_10371
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7753_call = mod.get_global_var('func_7753')
func_7755_call = mutated_mod.get_global_var('func_7755')
call_10377 = relay.TupleGetItem(func_7753_call(), 0)
call_10378 = relay.TupleGetItem(func_7755_call(), 0)
func_1628_call = mod.get_global_var('func_1628')
func_1633_call = mutated_mod.get_global_var('func_1633')
const_10380 = relay.const([6.436624,-1.118078,-1.351238,-8.270131,-7.189097,-2.781380,-4.567708,-4.305030,1.959369,-7.077935,-5.861513,7.895894,1.580232,-1.639436,8.818620,-1.461447,-9.022543,-5.262993,-3.445268,0.145348,-8.949135,-1.526639,-7.434023,9.039215,7.679981,-0.088624,-0.755485,-4.903335,8.838582,-4.849755,-3.209451,-8.085240,7.692986,4.814689,4.037340,-3.707386,-6.534324,5.076227,7.347687,2.450949,-4.338549,0.693493,2.525499,8.630727,-0.471447,0.163787,-7.442710,-6.123688,6.542310,8.032812,-2.682147,-5.194935,8.381987,7.437601,-4.579905,2.131178,1.687885,-8.223306,-3.499303,1.963133,6.591987,5.962654,-6.033829,-2.336379,-5.137527,6.441514,5.320200,0.844242,2.201317,-3.193837,0.157937,-2.612200,-0.889224,-4.471963,-6.377674,0.542370,-4.065277,4.267579,-5.027299,-6.842276,-3.938935,4.522186,7.041234,-6.850174,-6.621725,8.018466,-9.172232,-7.767419,-5.386503,-0.688633,-6.565397,-8.367880,-9.879694,-2.655279,7.883287,7.658491,-8.746482,-2.200305,-9.913197,-5.704336,6.865272,-7.273701,5.845093,-7.606732,7.508751,6.943783,-8.663538,0.591985,8.949277,-6.763050,-4.131679,-3.734697,-4.760742,7.514727,6.716093,6.343114,1.781453,6.801365,-7.648658,-2.105169,-8.710050,-6.975716,6.603338,5.306202,2.045264,-0.633885,-7.928997,-4.524938,0.050026,5.863951,3.316618,3.254570,-9.952672,7.440650,-7.032531,7.968944,7.427842,1.227011,9.543785,-6.843792,-3.727242,-2.277919,1.190538,-0.982453,-9.200133,-0.473282,-1.799268,-7.679508,-0.419201,-4.172961,4.908813,0.260412,3.528778,-2.486572,1.783697,6.836593,4.996521,-7.414329,-4.940284,6.071542,-0.993955,-6.401281,2.892703,-8.670621,-6.698700,-7.531429,-6.340649,8.625601,-0.826956,-0.967813,-8.497519,-6.845499,8.600229,-4.199122,0.492439,0.688316,9.556129,-1.370532,-5.303100,-6.619336,1.424513,7.239829,-9.739330,5.742151,-2.641466,6.046885,0.783765,-3.907210,-1.214091,-3.107127,-0.942932,-4.182898,8.769231,-3.657950,4.641031,5.289409,5.863779,-5.957438,9.088769,-2.004964,3.631920,-7.440651,9.202089,6.742337,9.274621,2.682222,5.882375,-3.747792,9.230318,4.217404,1.630353,1.099554,8.012838,5.113895,-4.609869,-5.479386], dtype = "float32")#candidate|10380|(216,)|const|float32
const_10381 = relay.const([[-8.735924,-7.648360,-9.565642,8.507547,-3.026995,0.875027,9.750751,-3.199092,9.529012,-1.201978,-0.316712,-3.691347,-1.408826,3.315354,7.495472,2.618906,-3.953154,9.634263,6.408128,5.292665,3.683722,6.304283,3.427534,-2.882968,9.803799,8.271763,0.117552,-6.162724,3.658912,-6.854856,-7.995925,3.963331,2.504717,2.896885,0.907307,3.870615,8.163641,-6.774910,-4.107572,6.114164,7.492903,-2.250627,1.956866,5.276887,-8.388350,4.745610,6.580991,3.032635,2.851325,0.543663,9.102699,-7.016154,-3.772872,-3.723521,3.818065,-4.620258,-4.291994,4.681712,-2.680229,5.846687,-8.219469,4.317669,9.668453,1.764089,-5.009030,3.195909,0.348031,-6.596389,-3.156766,-6.988528,1.843394,2.133424,2.651218,2.103708,5.293295,2.518133,0.907857,9.983077,5.901942,2.276405,8.342790,-7.310973,-9.604827,-8.506571,3.016281,-7.159943,-3.300910,-3.834676,-4.934091,6.045270,-5.317874,-8.419438,9.876513,-7.478218,-2.350346,-9.599849,1.128766,-1.007372,-0.489348,-7.031408,3.056633,-5.353574,-0.342240,-7.272509,-6.945088,-3.523278,-2.422202,-0.667287,-4.365014,-0.119573,-9.697911,3.993545,5.425190,-7.532687,-5.160846,1.220992,3.046303,5.629301,0.535094,5.064352,6.954289,-2.835433,-9.337480,-8.673812,-8.305059,4.231575,0.939790,-5.164220,-4.811532,-8.085443,4.843977,-8.660416,4.271368,1.007467,0.418307,-8.965386,-4.728010,-0.596867,1.787527,-4.810908,-7.044060,4.676753,-1.022131,-9.463453,-8.972886,3.934627,5.685574,-1.217747,-2.329669,9.901087,-7.623209,-2.931453,-8.203904,6.481334,6.816340,8.093970,9.437808,-0.745192,-5.012719,-9.893304,1.307326,8.947955,-0.840451,-0.509695,2.846796,-3.779503,7.849943,-2.270066,-2.109882,-6.719106,4.542576,2.363608,-0.745901,-6.468760,-6.591701,0.882288,9.017560,-0.738860,-3.170180,-3.268221],[-3.313678,-0.989737,2.983272,-9.241231,-8.097606,-9.976418,-2.189747,2.806914,5.864800,-4.056123,-4.971397,7.168327,-3.324632,6.248284,-5.788268,-2.821537,1.397046,7.495657,6.312343,-8.664495,-3.028821,-0.728634,-4.158212,0.826590,4.603320,5.602033,7.741215,8.931286,3.027834,-8.711887,-5.280216,-0.624116,5.320050,3.411690,7.621554,2.003520,-1.414645,9.721386,5.389036,-3.750520,-6.629964,-8.749012,-1.154388,9.700640,5.840557,-8.294769,-4.641499,9.872258,-8.219153,-1.319862,-7.673009,4.437305,4.712921,9.016765,7.341216,-7.360095,3.449858,6.847080,-4.210070,2.085219,-8.946913,-9.130584,9.226344,7.941272,-9.160039,3.268702,4.846592,5.610835,9.125735,5.496497,-4.660819,-1.127250,-9.202692,0.975490,-2.644322,-4.339719,-4.573551,4.486803,-5.585846,0.801612,8.534707,0.125098,4.981838,6.128877,9.548227,4.630328,-9.904509,-6.067694,4.851615,-9.875843,-6.405209,8.877319,7.137457,-7.867128,4.923841,-3.130323,8.577841,4.874098,-1.172006,7.726739,3.348225,5.014763,2.224370,-8.283242,6.111882,-6.731401,-8.155832,3.713459,7.240168,7.598480,4.070312,1.945374,-2.344217,-5.577680,0.256817,-6.025834,-5.851057,3.807387,5.230649,9.797034,-5.771299,3.228957,7.817778,-8.690664,-9.964635,0.194312,4.519487,-0.427331,9.813656,-1.874822,5.251535,7.485607,-9.306971,0.528818,-4.645251,-1.447096,-2.854243,4.659721,-4.901500,-8.355669,-4.422438,4.867817,-7.069164,9.000358,-2.627295,7.242454,-0.802472,4.491728,2.832902,2.595789,4.058487,-0.986843,0.319501,0.293649,1.217438,-6.289162,2.750799,8.055060,-6.006864,3.638263,-6.466401,-7.343686,2.256692,3.448799,-4.160403,2.045292,-9.733602,5.610541,9.420135,-9.706046,6.671535,-9.861611,-8.722961,-6.612888,-9.863889,9.586552,-3.674344,-2.826246,1.763550,-4.312075],[-6.178463,-1.782574,0.042855,-3.943156,-2.078728,9.391987,5.531035,5.895939,4.729469,-5.814824,5.954593,-1.076520,4.305497,-2.433476,-2.615565,-0.438059,-3.712796,-0.586974,1.674540,-7.826973,8.108741,7.052887,-7.279173,-9.916172,-0.874249,5.249434,-0.147825,-4.155367,-4.565445,-7.904511,4.769231,2.353673,3.488377,-3.519366,-8.850963,3.611379,-6.779734,3.100888,5.809449,0.356097,-1.208301,3.847043,-4.215862,3.513559,-6.026326,-3.934329,-3.797217,2.614878,0.673329,-2.670199,1.492199,6.132290,-0.437409,-9.416839,-3.739799,-4.519437,-6.548536,2.054012,9.772337,-8.443960,-5.110971,5.369713,-1.688804,1.518102,-2.477392,-6.651803,5.856765,-9.986438,-7.061402,4.249904,-4.093333,4.970406,5.123105,5.953885,8.564205,3.441197,-1.200359,2.475437,5.597492,-5.679696,-7.578557,7.926569,-6.536561,-9.704281,-2.212629,5.767529,4.665576,-3.987864,7.487463,2.915059,1.682473,7.310642,1.556340,-7.369009,9.399818,8.867339,8.914730,8.817131,-2.574964,-4.100050,1.586257,6.653547,7.245585,3.227012,0.965296,4.015657,5.440458,6.886307,1.374050,-6.896480,-4.941399,1.316127,-6.067087,-0.703512,-5.036857,-5.365240,-4.349558,-0.632726,0.933528,6.419475,-1.248174,8.402894,1.258212,-0.199366,-3.500090,7.620767,-6.857671,8.784255,3.517995,4.494539,-3.414464,4.417695,8.210996,-0.503082,4.762086,-2.788927,0.748490,-5.624679,-2.991704,0.849762,3.049468,4.983073,9.502672,-2.685609,-9.235993,-2.371079,2.524574,-2.008061,6.527138,7.880112,-6.531872,-4.113648,8.350195,-5.564688,-0.590862,2.051770,-8.716232,2.385473,9.324910,-0.178623,-4.996654,-4.578528,-7.340772,-4.459776,-6.438210,-4.409311,5.551287,-0.150960,5.601089,-1.419787,-0.037538,8.254996,0.802289,1.452144,8.031090,-3.504364,-3.990262,4.087532,5.249714,0.765309],[-0.245893,-4.620039,-0.673812,-3.928347,1.009498,5.007517,-4.102053,-4.103679,-4.823257,-7.693778,7.942021,3.481677,-3.839040,-3.331605,-9.091867,5.877063,-1.621351,7.611522,-4.524454,-2.347493,-9.994254,5.233377,9.000364,-1.571353,8.853636,2.097281,-5.911302,4.086795,4.367139,-2.187821,6.353762,-1.559264,-0.826709,-8.694918,-9.595965,-5.094009,4.192000,7.777004,-0.244916,-2.608347,6.332848,-1.597501,-5.268816,-3.684205,-4.023241,7.565647,-5.048663,1.866255,9.598558,0.627109,-1.282839,6.530622,1.655651,-4.162113,-4.395239,-8.979049,-8.306978,6.701274,-8.230439,0.150674,4.823402,-4.232643,-9.213923,-7.438364,3.578919,4.121955,3.500957,4.165569,-8.686067,-4.402581,-4.837343,-8.466805,-1.368059,5.856758,4.471099,9.830016,-2.288819,-0.811917,9.199751,-3.441686,-6.827453,-1.721638,-2.891540,-1.710660,-3.290860,-1.775714,2.322992,4.370523,-6.366861,-3.717574,3.688320,-6.055869,9.252303,4.677100,5.960803,-8.341886,1.738525,-3.224032,-3.231161,-1.039791,0.944806,-9.537627,8.832539,-4.386719,-9.339267,0.464544,-7.974576,2.676741,-3.540323,-2.506861,4.958220,7.449670,-7.615139,-6.632397,0.841327,1.850732,9.080581,1.194977,5.890878,9.401469,2.887078,-6.090782,-2.344401,6.723102,-0.236870,5.788468,-0.419966,-1.040592,-0.377908,-3.897846,-0.094828,-6.322224,1.239994,-7.577535,-8.236817,-8.831865,7.623415,2.577213,7.179497,-1.885673,1.200344,2.527413,7.052510,-1.827018,-9.439489,0.717764,-3.427959,7.191127,0.791115,-6.333943,0.962683,1.279539,2.825981,-2.927576,-8.266142,-6.262630,-4.553603,3.140011,-5.669672,9.533633,-3.435740,1.079534,0.593820,-3.865360,-0.207740,-6.473357,-0.603549,-9.533798,-1.835203,-9.323943,-1.827098,-1.264380,-4.894361,-8.944492,1.455069,3.431452,-4.090818,-4.884944,7.929905,-2.142667],[-9.605392,3.347411,7.766980,-3.207234,5.713388,-4.697755,-0.761118,-2.814792,-9.584514,5.678262,5.657310,-9.757882,8.568312,9.828195,1.815667,-0.961079,-0.945790,-8.346862,-0.076719,3.797515,9.209491,4.322106,1.047998,-0.298735,-4.937092,6.046545,6.144571,0.170843,1.858538,1.320816,-3.962758,-0.451791,-4.781837,-8.399065,7.299755,-4.529791,6.589532,-8.461755,1.635563,0.256132,-2.850924,5.283387,-3.327346,-6.026674,6.758661,-0.772820,-3.026562,-2.968705,-1.697465,2.799007,9.371366,-2.525705,9.251203,4.805293,-0.323361,-4.652157,0.996141,-5.040262,-7.265689,0.117492,-0.693531,0.537423,-6.331340,5.126623,1.605815,9.310618,-6.240051,2.151569,-0.978100,3.590167,0.838362,-1.931600,6.149300,-1.578738,9.733955,-9.731397,-0.059298,-7.860079,6.763594,4.329482,-6.014518,8.735342,-8.318931,-0.869164,2.716319,2.200279,0.600878,-3.566294,-1.026228,-7.306845,-3.395874,-9.748502,7.704108,-4.209069,-1.956141,6.428788,-4.856817,-4.132305,7.599036,1.736730,-4.590771,-1.435826,-2.674997,-4.061375,4.463310,7.910060,7.496003,-9.265780,-1.106061,-9.941155,-1.342470,-5.046242,-4.946633,-7.768724,3.220036,5.709462,-3.400308,-9.641668,-1.218537,-1.216955,0.974532,3.681161,8.215995,6.445926,-3.277094,-7.935077,5.081475,2.278481,5.143743,-3.195176,-5.477601,-4.427442,7.956842,1.593492,-1.304963,3.771004,5.353633,-7.463407,5.038157,6.702507,0.314295,-3.972175,-2.476809,2.313187,1.372427,-4.038296,7.844213,6.271905,8.411713,-6.068235,-8.009539,-9.441213,-4.819707,-4.010727,-4.222824,-9.174576,1.163714,6.725043,-1.436854,-7.711509,-3.816020,9.148364,8.404275,-8.437978,-1.919399,-1.272752,-3.374800,-1.345294,-0.357568,-7.522021,-7.654480,-1.062796,-0.838466,6.287350,-7.931812,-6.033675,1.419905,-4.705819,-9.443948,1.358328],[7.423512,3.302310,-8.840239,9.209843,-5.111554,-3.455482,-9.572782,6.009358,-9.694292,9.339420,-7.897998,7.946643,-1.686918,-9.962576,-5.247063,0.227779,-7.045525,0.728431,-4.009471,7.869385,6.468304,-2.725558,-1.598876,-7.948179,-2.058050,-7.507078,5.236062,-9.635800,6.303421,8.074392,3.055925,-3.759829,3.134682,-5.979491,-2.133043,1.221751,8.857523,4.113331,3.631119,-4.586012,2.525510,-2.863754,-7.097122,-3.284330,9.224952,2.726651,-8.019225,-6.060319,-8.628179,-8.910492,-3.884998,-3.808830,7.446092,-8.590633,7.452955,-4.087222,2.175153,3.630494,-4.433522,6.269509,0.064934,-0.907031,-6.660633,-4.556005,3.964318,4.693990,-0.508347,-0.200941,4.123105,-7.774997,0.208292,-7.476254,6.101683,1.362401,0.549957,7.934355,3.596403,2.515575,7.086680,-1.998485,-2.762881,-6.877959,1.423283,-8.152632,6.311020,5.428439,8.104672,3.562066,-0.646764,-2.891569,-0.180109,-0.690440,8.085932,9.572559,8.358612,-9.418824,-3.145007,-4.975368,9.766356,-0.111355,1.639302,4.953013,4.113195,6.215725,0.022016,-4.142672,-7.766256,-9.089681,-4.014327,-5.222648,1.467512,3.911150,1.028092,-9.918640,-2.468771,-3.843400,-0.280410,-8.806512,-7.892721,2.064902,-7.035452,7.325181,8.042770,-0.330745,-6.281470,2.805217,0.963363,9.873512,5.246022,4.889690,-5.620807,2.862503,-1.560776,9.066023,-1.239084,-7.816324,-7.088390,9.090549,3.514957,9.389929,-4.406209,-3.945475,4.806550,-7.862334,7.131536,-9.777612,2.360976,-6.044671,1.192775,5.111775,4.773727,-7.283697,8.812732,5.944876,-4.105576,-5.751533,2.339839,-3.780621,-5.381944,7.376869,8.277252,-7.049398,-1.888515,-1.390229,-7.434938,9.835622,0.739990,2.779354,3.118827,-8.144137,0.797063,-3.478827,0.967364,1.843291,5.783406,6.374897,-5.922169,-2.669580,-8.810261,-5.845282],[-1.469700,-5.997227,-4.408406,-4.963246,-5.879644,5.221568,-0.661557,5.148804,-2.256419,9.403898,9.648222,-0.604176,-2.285571,-5.300762,8.091974,4.145480,-1.511537,-2.640391,7.691941,-5.331156,5.132614,7.905978,1.149082,1.661159,9.073757,-2.879087,5.726093,-1.530360,0.057980,-3.592280,-9.968792,-1.722287,-6.046110,7.828953,3.255681,6.830567,9.967406,-3.390985,8.435769,-3.622938,1.353143,-3.481789,-8.036085,-3.289372,6.693260,-6.899730,1.702951,0.971760,9.174968,3.187504,-2.065477,5.878726,-4.294769,3.451421,4.879273,-2.034302,-6.844404,7.044344,-4.980650,-1.060978,1.842554,3.243337,4.838528,-7.575105,8.129542,2.819644,-1.286952,4.709992,2.093823,0.988081,-2.666151,0.239925,-7.540168,2.896109,-3.880598,-4.443136,1.601944,-9.573850,-4.051161,2.206259,5.684432,-7.957349,-0.005975,-9.651280,-1.717229,-8.002295,4.122890,6.694168,5.829945,-9.913963,-7.586769,7.713938,-8.905241,-4.299653,-4.751662,-4.718917,-8.910690,2.214533,-4.177642,-3.284013,2.780092,-6.546090,-8.727261,-1.189720,-3.054112,-8.690007,-9.595774,-8.298405,4.862537,9.109847,6.745028,7.881761,-3.501047,-5.605758,-5.709410,9.707157,4.068151,2.841716,5.989209,9.913508,-8.970888,-8.092777,9.729506,-9.450536,8.508939,-3.309176,1.138428,7.526371,7.034485,5.130677,-6.798408,9.324935,-6.849717,-8.493564,7.104907,7.599603,0.475213,-3.777331,3.713473,0.169955,-2.484536,6.364554,-9.538530,-3.958203,-7.579916,4.778560,-9.098102,-5.747673,6.772302,5.459744,3.407024,7.851665,-8.346940,8.260749,-8.731382,3.641728,3.642002,-4.114496,7.450626,6.523509,-5.651988,-1.084839,3.715906,3.549592,9.140318,3.516292,-9.361716,0.478942,-1.285829,-7.769529,-6.711278,-8.972476,-8.876102,8.799694,3.165591,3.904095,1.039828,-8.928100,-8.860234,-0.536132],[-0.141960,-5.498475,-0.876540,-2.835220,3.996488,6.688255,-9.487578,6.688745,-9.862105,-1.337864,6.698420,-6.098430,7.786254,9.954756,-3.308259,-1.686265,-7.423117,8.418544,-3.205065,0.851409,-1.729686,8.580723,-7.504292,1.603091,1.275817,-5.479091,2.925064,-6.112466,-8.306851,9.222709,4.182233,8.839369,-6.377959,-1.135186,-5.773370,-8.930849,-7.932174,7.870942,-3.715224,5.597165,-3.328598,-0.432922,-1.422298,3.463439,2.818391,-9.447601,-6.627534,-9.385668,-3.076402,4.455758,-1.751243,-1.771186,-1.239456,-3.450079,-9.181260,-2.707915,3.358760,6.861912,7.995118,-1.178376,8.316762,5.507567,6.786495,-2.023803,-2.678122,-9.797690,-5.744090,3.152181,8.432517,4.861843,-3.689105,-3.573489,5.848780,4.860519,-6.252891,5.588851,-8.855822,1.754369,-4.938659,-6.478173,-3.855589,0.568085,8.151400,8.417174,-2.558410,-9.947112,-7.137113,0.916407,-5.020936,5.857821,-1.884309,-3.594731,4.056995,-9.295016,-9.455547,9.892548,-8.257845,8.062443,5.907815,-9.272244,2.944350,-6.563540,2.302567,4.992082,4.502975,5.534269,4.458451,-5.835383,7.382528,-9.369695,8.121104,-0.404921,6.494503,5.543962,-9.278700,-5.788794,3.573747,-3.329315,-4.249434,-0.560866,-1.973693,-5.600415,-4.287457,-3.820244,6.388027,1.507075,-9.516129,-1.555486,1.390429,1.448405,1.610477,8.635043,-1.830038,-9.886894,-0.553500,-3.431942,-7.950350,-9.462204,-3.522020,-8.423961,-6.457426,-3.676237,-6.070666,-1.366151,0.364922,0.887713,9.277531,9.244683,-1.375487,6.197215,-8.770279,1.532106,-3.451974,6.523937,2.074518,-0.056932,2.327647,-5.349604,-9.797786,8.079713,-2.167323,-5.158046,-7.624142,-8.888926,4.915831,3.990584,3.700872,-5.152995,-6.239523,-6.069706,-5.316439,6.667405,-5.175195,9.310827,-6.736310,-7.766203,5.422061,0.473176,-3.532811,7.505202],[9.038278,3.372855,6.358291,-5.112298,-8.574933,6.553418,1.973133,-5.909184,9.123486,-6.975144,1.999520,-3.938506,-1.465543,-1.417366,4.748612,-0.227628,-7.798221,-8.338969,-3.805980,2.130742,8.934381,4.539917,-0.933847,-1.282592,8.308646,1.879797,6.260647,3.137743,6.954986,-5.873864,2.714549,0.980350,7.379188,-7.069601,-5.196266,-7.241430,-0.901658,5.026394,3.677096,-0.767552,-1.397451,2.605391,-8.715152,4.153747,-8.923674,-8.416094,2.834997,5.480125,4.088943,-1.014464,-9.981235,-1.026924,-2.744797,2.661948,7.372136,-8.951268,9.321227,-6.943916,-6.472996,-4.439050,0.763717,9.040463,-7.493919,4.807180,-4.473917,-3.565833,-1.895347,6.842730,-0.329911,6.562765,7.514604,4.486811,3.825085,-3.421191,-7.873000,9.347633,1.127312,-8.396777,3.253486,-5.621725,3.319988,-5.912418,5.657668,-9.054890,-1.796985,7.681616,6.839895,4.279193,-2.656429,-1.809996,-9.246730,4.496003,-9.729865,4.527646,2.477398,9.416015,-1.079593,3.198667,-9.650197,9.099361,8.043577,-8.982781,-0.396812,1.836120,3.235432,4.931357,1.479365,8.069950,-9.616446,-3.694999,-1.175914,-8.047719,3.904056,-9.678374,5.174357,9.729058,8.757104,2.460266,9.027650,-7.029684,-9.568637,-7.610723,-0.332957,-4.567988,-5.536162,1.402308,-4.064212,-0.756960,0.408991,0.480842,-0.919980,0.631617,-1.464130,7.223020,0.771830,-4.823788,4.255505,-3.333748,9.655453,-8.729065,2.409615,-1.094757,7.516273,4.801897,-4.289660,4.897447,7.409442,-7.605022,1.042433,9.781979,1.153185,8.753248,-0.025865,0.427451,-3.214792,-4.897377,1.927279,9.110064,3.402519,0.602681,-3.726362,-3.155743,0.482201,4.836874,1.176734,3.099574,3.447464,5.700343,-1.069995,3.844794,6.239248,-0.483197,-7.451975,9.178444,7.323293,2.924822,-1.396633,6.286807,-0.435707,-2.435666],[-1.809309,5.314160,-6.490236,8.494820,1.984667,6.927465,-1.042996,5.885458,-0.847680,-8.642718,1.494594,3.608695,-6.577877,2.348463,0.351149,-1.328809,9.930909,5.925398,-2.169056,0.174426,0.957142,-9.898327,-7.424355,8.317329,0.337091,-4.420051,5.328150,-6.961402,8.815651,7.608570,1.532154,-5.297213,3.526902,4.228833,-3.930998,2.597824,6.796625,-6.127167,8.517737,-5.011627,7.406981,3.965193,-1.947147,-8.223601,0.973333,8.515615,2.930185,5.945222,3.229438,1.962097,5.534103,-3.575599,-1.647712,4.065673,-5.188600,-8.378031,-7.328731,-6.951771,0.327245,-4.831260,-5.039673,-8.944287,4.903957,-5.597136,-9.503195,1.529092,-8.709618,-0.451939,-9.403535,-3.705044,-1.721083,-0.598511,-1.190892,0.569566,-7.429839,-5.269100,9.561266,-4.426318,2.485599,-4.167578,-2.967515,5.267617,3.265482,-8.756534,6.592274,-8.595295,1.875584,1.536213,1.164300,-3.398342,-2.423981,9.651751,8.356082,6.588029,-1.071528,-0.313655,1.003691,-2.872273,9.365343,-0.839876,3.496952,-8.097016,5.122436,0.769498,6.258177,-0.371556,-8.882453,8.244565,-5.360297,-1.316252,-9.695170,8.741503,4.164260,-3.852767,-2.889868,1.018432,7.957224,0.097702,0.277515,-4.262719,-1.175473,6.038308,-8.901134,-2.200101,9.975234,0.828683,0.682652,3.125282,-2.024810,3.350585,-9.363011,7.918992,8.713022,-4.688629,6.935736,7.326012,-4.318512,-1.473773,9.710001,2.271620,-8.321304,1.654658,0.390985,-6.785098,-4.042509,8.761451,-1.536398,4.611529,0.099003,9.570342,-8.846771,-3.448857,6.963267,8.142130,9.460169,3.922817,4.110341,0.715049,0.603580,0.457584,8.623529,-1.036076,5.664751,5.871209,5.242308,7.390273,6.865297,-0.946422,-7.561728,-7.091280,-8.037652,4.435962,-2.033700,9.862917,-2.522568,0.206323,0.350828,-3.555045,4.422078,9.253681],[-3.649567,-5.469738,-8.233918,-2.602125,-0.192749,-4.101383,-1.200775,5.760995,-2.485434,-8.469657,9.542275,-7.924636,0.350954,0.585931,5.609803,8.119181,1.283075,7.910887,4.309478,-8.405897,-6.743378,-9.319053,8.032453,9.578078,-0.144853,-9.345063,-5.275392,-4.046304,3.532020,-0.374376,-3.889830,-7.945545,-2.477435,1.866357,5.265866,3.437924,-9.901982,-9.406135,1.450109,2.768883,3.157103,5.347863,5.763946,1.689827,0.378472,2.125690,-9.942771,5.605136,6.182270,-1.764929,7.317176,8.142330,2.560480,6.996808,5.874062,6.332678,-6.537851,-4.944999,-7.726530,9.947648,-1.427044,-0.875363,-6.182434,6.048231,-7.711492,8.085750,9.905011,-2.743254,-8.746181,-7.121656,-0.710703,4.672151,-3.728608,-4.435437,2.609144,4.395669,-1.035714,-4.756004,3.215482,9.989850,4.157678,0.665578,9.693011,-7.512445,8.606834,3.119231,-5.071752,1.403455,9.439915,3.232354,4.659069,-3.575149,-5.313532,-4.292298,-0.342785,-3.402284,-2.493686,-4.036418,1.076090,-5.825773,5.857196,-9.715037,-6.903775,5.964147,-9.434088,-5.567812,9.557621,0.356128,-9.527986,5.590697,6.210180,-4.940473,-5.680880,4.221073,6.185931,-0.539979,-9.722313,-3.354950,-6.477432,-8.188741,6.241594,-6.363493,5.135588,-0.681484,-0.154310,-0.429549,0.530191,8.367028,3.961049,0.817262,-3.042747,-6.838675,3.431034,9.830751,-2.662297,-5.056414,5.279262,-1.539128,-4.677562,-8.066913,-4.856423,4.471828,0.850302,6.217076,0.431855,-0.517517,1.239755,-5.321054,9.773051,-5.651266,7.698420,9.009073,-8.377845,2.121857,5.132406,4.602625,-7.494009,5.521734,2.094821,8.607633,-9.335075,1.597403,-1.006289,-6.966274,4.002625,5.486844,9.561057,0.680758,-2.071273,-3.328051,-1.436836,1.358039,-7.066271,7.964092,-8.196147,8.007479,-1.572347,-9.528803,-0.216757,-4.644225],[5.181955,1.757095,9.384647,-0.854799,3.111548,1.063948,-2.510791,8.632121,4.545512,1.028800,8.642094,-3.479467,0.928254,-2.126913,7.881321,2.402077,-7.919548,7.779897,-6.680392,6.444983,1.808805,8.829506,1.258965,-5.289215,6.771633,-2.555783,-2.848169,-0.513068,1.820652,-5.946407,-6.027714,-6.379721,-1.653828,-5.773007,1.543352,-1.177800,-4.242036,1.963394,-3.802292,-9.398431,2.769444,-8.276204,-0.635313,7.850086,3.729397,-6.854534,5.329003,-0.747729,8.281567,-8.713975,-8.057401,0.848076,0.640383,0.796378,-4.697778,5.873556,-3.496512,-9.317080,8.721277,0.132814,4.838644,-6.879217,-6.725568,-5.146353,4.270250,-1.629153,5.029579,-1.584604,-1.636691,3.018562,0.439038,-5.367307,-3.518907,-5.566691,-3.044417,9.190835,-1.195676,1.128220,-9.129732,-3.585419,-1.928911,-1.763122,-1.860089,-9.046379,-9.372556,9.550514,6.968627,0.388894,-5.478937,6.975861,5.345466,-4.244639,-3.564972,-2.419618,7.811596,-8.820161,-1.840752,-8.719278,0.947043,4.986876,-2.869290,1.175498,4.696605,4.448641,7.102198,-6.260020,6.192122,-9.912028,-1.997232,4.729968,6.830014,-0.531848,-0.883980,-9.924394,1.820473,6.868733,-0.899497,7.001217,5.856860,-8.500266,0.475581,-6.624177,0.728256,-5.856348,9.826499,-0.607950,3.537467,-9.785975,7.514829,5.442561,5.196906,-0.242643,-9.702909,8.705345,-7.133887,-0.195475,-7.550218,3.110267,5.269273,-9.419995,2.016565,4.151260,3.353570,-5.684827,-9.089198,9.761975,-0.597154,4.521972,-8.795074,-4.040417,-4.794995,-4.988807,8.651071,4.935095,-8.210195,-3.771085,-7.774724,-9.026001,2.620663,-5.040595,7.542554,3.415659,6.049528,-5.663974,4.996734,-9.889372,6.452163,5.725894,-5.398500,4.033266,-1.348261,-2.495207,3.472119,-1.690541,5.965157,-8.792187,-1.411692,-2.494791,-0.081519,1.486258],[-6.542450,-4.833348,4.595884,-4.569041,-5.475798,-8.673041,6.263686,4.770108,6.814342,-4.303922,-9.012103,3.993675,-8.137924,-9.095465,-9.704298,9.226074,3.762111,-7.718590,6.698753,3.545382,-5.358207,-8.469021,-0.961334,-5.591012,2.093198,4.767166,3.578677,-8.549248,-5.677027,2.328690,9.217595,8.732836,-0.583914,6.727199,3.756012,2.845478,-4.772343,7.161333,5.153619,-4.884076,-3.671030,-9.866286,7.089496,-5.595174,8.518904,-9.836392,-4.880444,1.635535,-8.232112,-6.976151,0.589433,3.242764,7.580634,9.787718,5.504958,6.250838,2.932397,7.838347,-1.247653,-1.555375,6.642346,-7.152049,8.879957,-8.569454,-4.687282,0.940452,-6.585823,1.325748,5.477804,-9.548390,0.605320,2.630467,9.536423,3.373236,-0.900428,8.838797,-9.174770,6.879681,-0.121241,6.315550,-8.157086,-0.495903,-7.210626,-7.163122,-8.032617,-4.769385,-9.241014,-1.293900,-4.795464,2.458436,-8.735203,3.250013,2.055867,-2.440369,-3.548334,-8.503084,-1.533535,-4.961333,5.305905,-4.916409,2.183853,4.460584,-6.876933,-3.404609,1.763129,2.573475,-3.264759,-5.020076,1.271315,0.488805,3.641885,-8.637685,3.748097,-6.483267,4.560724,-6.712917,8.718418,-1.112942,-6.617229,-9.077168,7.519126,4.205370,-2.251740,4.153682,-8.598442,-4.092352,-1.791005,6.688767,3.115510,-2.941703,-1.307149,4.082367,-5.079233,-4.709549,-4.434225,-6.022108,-1.032578,-3.032669,-1.293447,7.692341,-3.702548,-2.080299,-3.960055,-5.685512,7.554222,3.783095,-4.461332,8.599450,-6.155908,1.276392,-7.556011,-8.286640,5.338814,-5.877023,-3.790412,-5.630169,3.057473,-6.401856,-4.947414,2.786918,2.085709,7.737265,4.706255,5.878864,-9.324094,2.552915,-2.538426,-8.964980,-2.533752,4.249455,-7.883756,6.304831,-4.917956,4.767089,6.080340,-1.546203,7.841372,-3.477026,-2.782574,2.517291],[-7.023555,-6.695414,-4.228946,-9.289259,8.983190,-5.853244,2.739945,3.348644,8.748050,-1.958058,7.520907,3.491939,-2.073599,1.230803,1.357035,-9.146744,1.971104,4.955495,4.150351,-1.794942,0.946119,-7.983889,0.768746,5.122615,-2.523401,0.798399,-5.102179,0.548435,-7.210030,-1.091803,6.067626,6.827154,1.351772,-8.804242,-5.209153,1.978492,8.906528,-1.531584,4.848682,7.750072,8.856057,2.373276,-5.064219,-5.568104,3.066407,-2.211055,5.212002,-6.442790,-6.204950,3.857194,1.512442,1.311209,-8.113653,5.404383,5.130143,-9.836629,5.965961,-1.123490,-8.851657,-5.541234,4.755582,-6.184483,-7.529609,9.187126,6.348480,0.664544,7.506908,-7.041923,-8.962810,3.196330,-7.378063,-7.851080,6.323338,0.664610,-6.982431,-3.854831,7.768082,-9.968463,7.225808,-9.084840,4.403377,5.962579,-1.653774,-0.406972,-9.748388,-6.352773,9.969142,-6.331718,-0.893143,-2.384775,-6.017467,-9.074519,5.351790,0.062583,3.263843,-3.702247,-0.845411,9.672756,5.206382,6.102326,-0.333864,-1.455731,5.127297,-4.536802,0.096015,-1.565005,4.797508,8.459569,2.826354,9.053841,-7.428078,3.747777,-0.268331,-3.880182,5.675081,2.540500,6.351265,5.968442,-4.733951,-5.590820,3.445769,9.606024,-2.747260,5.121773,-8.560170,-6.423425,-5.815142,9.512609,-3.650088,-0.922349,8.712682,4.590173,-9.452908,1.294239,5.857644,-0.673083,-1.366658,7.189897,-9.454808,9.437735,-9.046211,5.780332,5.350796,7.143588,-8.450733,7.220652,1.791521,9.007592,-3.958077,-6.854278,-1.666616,-5.731298,4.602257,1.282990,-7.180564,-5.879413,-2.514994,-8.369973,-5.574025,-4.719093,6.532307,-1.628717,-1.787408,-1.078596,6.877805,-7.164982,7.151116,-9.342535,3.304903,-4.064777,-9.034133,-3.653302,3.812341,5.457170,-6.671580,-4.864527,8.729017,-4.238955,-2.092125,-4.294379],[4.873029,-5.534047,9.064703,9.582350,-6.835681,8.442492,-8.294169,-2.055827,-2.707401,2.909252,1.403203,-3.184359,4.647825,-5.716701,-4.770597,7.130711,-9.799347,-5.087892,-1.187429,-2.597624,-9.765421,-3.398686,1.445231,-5.032819,-7.775624,-5.445109,2.995752,-1.997217,9.788984,8.524511,-2.512111,4.141778,-7.117342,-9.194201,-5.997117,5.901554,-7.784372,4.302399,-5.813835,0.404861,-5.839176,-9.767829,1.300445,-5.817346,-5.796033,-8.219178,-0.479341,0.559486,2.257138,2.010295,-8.038570,-1.017938,-8.202278,-9.794115,9.312767,3.542848,9.028908,-0.675697,0.355171,8.979300,-5.378277,-2.737383,7.559731,1.880504,9.692310,-2.123138,9.726004,1.465125,2.630225,0.919788,8.555082,-8.917859,-1.862035,6.985675,4.134946,0.745260,-1.116613,-5.126658,6.256950,5.220628,-4.663724,-5.839142,-7.695991,-4.828936,6.040437,0.544483,-2.764540,6.382441,-6.138912,-3.118013,3.174166,5.572885,2.319318,-2.286744,3.420284,-6.504684,8.306970,0.882663,-7.607351,6.493922,0.573512,-3.037271,-3.768937,0.447515,7.764564,-7.028724,2.791263,-9.827877,8.381948,-7.463488,-2.466949,5.680368,0.104253,-0.605981,-0.894137,-1.586973,-5.192400,9.608267,-7.049922,0.198348,9.148395,2.622951,1.836550,3.832405,-9.142165,3.611647,-8.321002,-9.596450,4.383612,8.230960,2.856306,-8.416077,7.698120,-9.062171,-4.770085,1.251010,-2.658414,-0.758039,-5.184944,-0.432486,4.393321,-1.076403,-8.646615,-4.726174,5.948292,8.065502,6.928978,-0.227703,-4.309741,-4.426166,-0.535859,-7.263224,-6.631567,-9.580008,-6.044462,4.824231,-3.707442,-2.909364,6.872843,-8.965983,-9.527564,6.447189,7.284707,-4.587323,-5.282940,-3.920607,-2.364283,5.324491,-0.432196,-8.488311,7.131488,-1.505952,5.709047,-1.271116,7.028532,6.515252,8.297042,8.875762,-0.785280,-1.118528],[7.873715,7.550886,3.264154,-4.674416,-3.686478,-3.586298,3.348755,7.683994,9.067851,6.491949,-6.442090,6.866758,7.246089,1.513172,-8.046248,-8.109027,-3.071335,-9.996800,5.621594,8.253880,9.484605,7.538295,2.528104,0.670859,-7.451090,3.700331,6.484524,-8.398559,-2.377413,-5.388097,9.666738,-4.513182,-8.047064,0.686051,7.437195,2.615283,6.034966,0.454313,0.964543,8.668677,6.887908,-1.678830,9.501865,1.743675,-4.503999,7.858737,6.230390,-2.065760,-4.107264,0.443673,-1.613724,-1.451989,6.311630,-6.739334,-7.576905,-6.640713,8.256555,-2.717960,-5.068264,-3.873146,4.755989,-0.457832,0.089407,-6.245970,0.199908,4.595200,-6.640765,3.496526,-6.160554,-3.720879,6.746416,-1.299646,4.399972,-4.653573,0.945828,1.319557,-4.165485,6.080678,-3.553857,1.815176,6.460004,1.658839,-1.360231,9.529984,2.424428,6.134260,-1.485349,5.253279,-2.608039,0.024126,-8.423534,-7.412839,7.544467,-0.557518,7.387268,3.557228,-8.027024,-6.641107,1.512390,7.667849,1.372258,6.253157,7.342418,6.103813,-2.353325,8.696320,6.646156,3.003753,5.261730,-9.052889,0.416930,9.606116,4.374964,-4.165096,6.793730,5.948221,-6.639778,-9.349399,4.235259,8.076507,1.333225,-0.429643,-9.505968,3.362717,1.407885,-5.625130,7.679692,-8.658856,5.263677,8.919000,5.995516,3.130405,9.827075,2.196630,-4.253727,3.703023,0.022757,-8.471941,0.010393,5.390742,-5.727001,-8.331559,1.105436,-1.282927,0.992218,0.037580,-9.976421,0.712429,-8.761636,-9.242291,0.267874,-6.433881,5.356789,0.775439,-8.199908,9.115448,-6.665972,-8.552254,-3.675604,0.525745,-5.194397,-4.101340,8.400789,1.092525,-5.065066,-6.641781,1.070303,-4.226548,-3.169732,7.930681,-7.431787,3.005537,-3.421924,-6.506856,-2.429953,8.396928,-6.434653,4.382033,9.159084,-2.327584],[-6.517218,6.711830,4.777792,-6.932948,5.679394,2.687122,-2.302541,6.593355,-4.044362,2.190075,7.283238,-5.776243,9.064101,8.213192,-2.118778,-9.386690,9.467473,-9.515982,-4.931864,-8.737978,-0.105322,9.100804,-1.109103,-4.590086,8.268009,9.487859,-4.664285,-0.820054,4.557942,-8.049208,3.915631,-5.873713,-6.205112,-0.504928,5.418451,6.427264,-5.151591,-4.879850,8.000382,0.648993,-2.895326,8.982092,-4.989060,-7.999467,6.400094,9.540831,-2.498250,4.582424,-1.481060,0.993327,-9.221150,-0.258176,8.122986,6.842275,7.866213,8.918838,0.370923,-5.853766,0.640183,7.229665,2.111768,4.586299,-9.346818,-4.207180,-6.840228,-1.943071,-5.242981,5.640736,3.579939,-6.361166,-5.715888,3.248115,-4.835964,6.889588,-6.208279,7.928063,-4.810338,0.118474,5.381857,4.855047,8.189473,7.485810,-7.830485,-0.880270,0.352312,-5.406676,-0.266002,-6.410055,7.162882,-4.931846,-7.796904,6.164591,8.330948,-0.400416,1.896219,-4.812054,3.023106,-1.727392,6.605711,-8.450408,-1.093908,-7.636868,-7.663666,0.982079,-3.718718,9.016441,3.215521,6.723022,-7.859927,-9.751542,-7.858687,-7.474077,-3.956267,5.394118,2.076954,-6.094651,1.183298,4.584616,4.382959,0.355004,-2.244550,8.312128,-7.515901,-2.550132,-8.999799,-6.689977,-6.185156,-6.550331,1.346080,-8.046283,2.796407,-6.883682,8.420680,-6.072364,6.449715,-5.255667,7.997382,4.437451,3.287367,-2.255140,-9.938959,-4.312075,5.492521,4.776420,-7.186773,-3.959859,1.713764,-5.424721,-0.247261,2.845555,0.374032,5.232874,7.757314,-9.837093,8.459460,-5.928242,1.149487,-7.433273,-9.108753,5.688853,3.361515,-1.563347,6.867070,5.919883,-4.983042,5.667186,-9.491842,-3.979885,1.723188,-7.143450,1.373630,5.364928,8.507081,5.001939,4.415583,8.968742,-9.824584,5.165076,-0.272873,8.064343],[-8.763438,-0.861873,-3.114349,-1.087612,8.888703,-0.248543,-0.688779,9.312118,8.907777,2.648431,-0.121363,7.011599,-0.618156,-3.682304,9.806779,9.931762,-0.301011,-5.395689,-8.374643,-7.422948,-4.737823,-3.902764,-4.820900,-5.580736,4.746655,6.129543,-1.599929,-3.422260,0.551821,-6.333624,4.046597,-9.622844,2.075037,-3.491365,-6.794155,-3.885199,8.023090,4.104676,-8.436658,0.185492,6.401103,9.396612,3.275956,-6.261513,-9.242416,1.981739,1.744888,4.939928,-9.963427,-4.876957,6.463381,6.440476,-4.211545,-9.342082,9.540636,-0.189715,-3.632865,-7.462189,6.197350,2.215202,7.653065,6.530129,-0.352850,-3.117670,-1.443071,0.918889,1.825232,-3.849866,1.886709,-6.120198,-0.050197,2.443361,8.672615,-9.839207,3.178400,-5.114114,-5.953640,8.668421,5.615253,-5.935492,-7.278038,3.463295,-3.802302,1.922583,-7.125998,-4.924739,-5.366438,-0.173229,-7.226880,6.399971,-9.989281,-1.467766,3.702781,2.765188,9.653299,5.651156,-9.225231,0.780675,-4.131488,-2.236163,3.647288,-7.891372,3.924431,7.010489,4.101661,3.217291,-6.982679,1.912507,3.172593,-8.029725,-9.475253,-3.148239,-0.668652,4.528437,8.490762,-5.130850,1.505852,-5.707825,8.426336,-0.697025,-0.809654,-8.658565,0.860019,4.206799,-3.287327,-8.561874,9.360931,5.645995,-8.628632,-3.585724,5.761180,-5.028565,1.460038,4.604962,-6.165412,-9.263873,5.930943,-9.536863,-8.266458,3.487813,3.487371,3.127500,-1.737858,9.096565,1.443768,-7.965047,-7.435423,2.662250,-7.807407,-0.237381,-3.097600,2.908247,9.894772,6.862417,3.929070,-9.259116,-7.896664,9.787737,1.971766,4.698316,0.450719,9.340222,9.514893,1.893193,2.826220,-0.616095,-7.572798,8.111080,8.662314,5.754936,8.469047,-5.349509,8.368548,-2.887840,-6.106598,-1.497379,-2.751630,5.610778,-6.782148,9.776087],[-7.682858,-1.639828,3.078533,-9.331949,-8.286063,-7.473845,9.628636,6.085229,-1.859079,2.689172,7.681670,-6.824728,2.425877,6.234401,6.512140,5.239018,0.445139,-8.701417,3.658508,1.442744,2.536526,5.532765,-0.107923,1.848880,2.552744,7.638012,-6.620261,-4.718265,1.193537,-6.273946,-8.185097,-7.974924,6.882547,-4.519790,7.941916,-3.368248,2.922249,-2.617481,-7.064916,2.489993,-2.770985,-5.383792,-1.554968,8.898160,6.409794,-2.532053,2.469372,3.547970,-4.661046,-5.163736,4.740518,-9.069280,-0.487009,4.653068,-7.188342,-6.496713,2.677728,-5.940601,9.444496,-4.890560,5.693946,-2.079741,2.916946,3.390738,-7.107944,-3.549338,-2.667916,-7.995713,2.226453,5.204767,-8.610774,-3.850706,-0.694313,-7.744277,-9.218202,-9.103915,0.790151,5.726744,-6.609316,-0.408496,-4.249716,8.300011,4.182162,8.057898,1.501246,6.032476,2.268566,0.677048,-2.562133,5.591673,-8.726268,-3.120905,4.686372,6.008739,-2.851481,-0.317662,-8.916336,8.676261,3.807900,-4.506345,8.871056,3.004787,7.301611,-1.031850,-3.208987,7.124567,-7.642369,-2.138064,7.613166,1.104568,-7.128212,-0.510839,1.588777,-3.660482,-8.721796,5.825133,-2.193811,-0.492834,-4.783798,0.212997,1.820839,8.273533,-8.017674,1.490172,4.228640,9.634178,-2.007225,-8.128190,0.506033,-4.773005,1.375307,9.642169,-1.887458,-1.960612,8.301696,5.551193,-4.300539,-7.379047,2.270256,-3.483639,-1.675097,-3.409197,2.495912,9.682424,0.815806,-6.093758,2.052135,0.201725,-0.987937,-1.492182,1.055163,-1.455327,2.361912,7.698901,-2.605423,6.794938,4.576371,1.997875,1.550162,-0.840319,-9.428804,3.745333,-4.356153,-1.075912,-8.729302,-4.689664,-0.419765,1.712499,5.669305,-3.737684,-6.661473,8.883814,3.638540,-2.964141,8.314581,-5.524079,-0.515220,3.457823,-3.301173,6.057211],[3.450426,-3.120546,-0.852444,9.990900,-7.225770,9.727543,7.886951,7.542428,9.289637,4.567163,-5.118615,-6.278632,-5.592998,0.462303,7.541780,3.714043,9.091702,5.319113,-9.125257,5.792677,-9.841997,6.847701,7.883658,3.836329,2.994160,0.264199,-7.508637,-4.101511,-6.846107,4.341726,-2.018509,-1.069266,-9.654768,4.355407,-9.381052,-3.406097,0.119623,-5.259261,-6.426139,6.092042,1.292281,1.755975,-2.734017,-0.936617,6.156860,9.097518,-6.135696,4.227381,6.549623,3.374282,-9.467417,-8.227408,-7.331283,-1.600398,-4.666611,-0.297819,3.108924,3.503991,8.936912,-6.790022,1.921585,-8.473433,3.175281,6.002464,-0.006177,-6.409239,-6.589701,-8.226456,2.454419,0.800497,-3.158169,3.618807,4.025526,5.227888,-4.648192,7.716469,7.591449,-0.265658,-3.607375,9.010295,-8.906025,2.671445,8.132343,8.028917,-1.117498,-3.461043,-8.537402,-9.471278,3.823125,-7.061916,7.771022,3.151896,7.976211,0.024307,0.538480,-9.728313,-5.639241,-9.244510,6.324745,8.368175,-5.511113,-4.652926,6.780009,-2.115945,3.136436,7.397264,7.622699,2.031707,-3.083759,-1.563609,-2.851033,1.413180,-7.418516,-2.950981,-9.004549,8.690106,7.298561,9.204836,7.889775,2.719497,4.709704,2.703005,-8.166081,4.871473,-2.648575,-6.012296,6.499790,8.491753,-2.063824,4.319923,2.703960,2.336749,4.316039,-6.315685,4.317267,8.621299,-2.030603,9.084150,1.536147,1.981207,-0.008369,-9.239584,1.743882,2.298037,3.683480,-5.395718,8.887674,-6.650138,6.628019,1.907989,-4.696219,7.290190,-5.597634,2.624799,6.123589,0.239841,4.269426,3.730958,8.994575,-4.943899,-2.439991,-4.827180,-3.948534,-0.513200,4.943399,-1.614526,-9.380209,-6.783569,-9.777586,-7.484426,-1.817516,5.740036,-9.560081,-5.687876,5.925307,-4.802206,-7.275925,-1.125988,3.257274,-2.285473]], dtype = "float32")#candidate|10381|(20, 180)|const|float32
var_10382 = relay.var("var_10382", dtype = "int8", shape = (450,))#candidate|10382|(450,)|var|int8
call_10379 = relay.TupleGetItem(func_1628_call(relay.reshape(const_10380.astype('float32'), [216,]), relay.reshape(const_10381.astype('float32'), [3600,]), relay.reshape(var_10382.astype('int8'), [450,]), ), 5)
call_10383 = relay.TupleGetItem(func_1633_call(relay.reshape(const_10380.astype('float32'), [216,]), relay.reshape(const_10381.astype('float32'), [3600,]), relay.reshape(var_10382.astype('int8'), [450,]), ), 5)
func_8992_call = mod.get_global_var('func_8992')
func_8993_call = mutated_mod.get_global_var('func_8993')
call_10387 = func_8992_call()
call_10388 = func_8992_call()
func_9004_call = mod.get_global_var('func_9004')
func_9006_call = mutated_mod.get_global_var('func_9006')
call_10390 = func_9004_call()
call_10391 = func_9004_call()
uop_10412 = relay.log(const_10381.astype('float32')) # shape=(20, 180)
uop_10417 = relay.log10(uop_10412.astype('float64')) # shape=(20, 180)
output = relay.Tuple([call_10377,call_10379,const_10380,var_10382,call_10387,call_10390,uop_10417,])
output2 = relay.Tuple([call_10378,call_10383,const_10380,var_10382,call_10388,call_10391,uop_10417,])
func_10429 = relay.Function([var_10382,], output)
mod['func_10429'] = func_10429
mod = relay.transform.InferType()(mod)
var_10430 = relay.var("var_10430", dtype = "int8", shape = (450,))#candidate|10430|(450,)|var|int8
output = func_10429(var_10430)
func_10431 = relay.Function([var_10430], output)
mutated_mod['func_10431'] = func_10431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6654_call = mod.get_global_var('func_6654')
func_6655_call = mutated_mod.get_global_var('func_6655')
call_10435 = relay.TupleGetItem(func_6654_call(), 0)
call_10436 = relay.TupleGetItem(func_6655_call(), 0)
func_3291_call = mod.get_global_var('func_3291')
func_3293_call = mutated_mod.get_global_var('func_3293')
call_10445 = func_3291_call()
call_10446 = func_3291_call()
func_9498_call = mod.get_global_var('func_9498')
func_9499_call = mutated_mod.get_global_var('func_9499')
call_10447 = relay.TupleGetItem(func_9498_call(), 0)
call_10448 = relay.TupleGetItem(func_9499_call(), 0)
bop_10449 = relay.floor_divide(call_10435.astype('float32'), relay.reshape(call_10445.astype('float32'), relay.shape_of(call_10435))) # shape=(2, 7, 1)
bop_10452 = relay.floor_divide(call_10436.astype('float32'), relay.reshape(call_10446.astype('float32'), relay.shape_of(call_10436))) # shape=(2, 7, 1)
func_2109_call = mod.get_global_var('func_2109')
func_2112_call = mutated_mod.get_global_var('func_2112')
const_10473 = relay.const([-9.440311,-6.868029,-0.687457,-4.670442,-2.106501,-0.982858,8.627938,-8.690099,3.752959,8.717092,-2.048453,-7.845518,-0.787501,2.954491,-8.383367,5.570974,-5.273159,-2.622385,1.605788,5.235976,-3.753333,1.019723,3.423699,5.267477,-7.325620,8.626808,7.524711,-8.906225,-9.699804,1.811471,-7.749538,7.606210,-9.146785,-0.333975,-1.274204,-8.735443,0.569823,-2.457919,3.748384,-6.414792,-0.694040,-8.965371,8.925419,-5.286035,3.142091,-9.390850,-5.885559,-8.749663,6.916586,-3.095353,-7.221691,1.640238,2.536696,-7.924461,2.873809,-4.310096,-7.880285,-2.065639,7.456023,7.164599,-9.987314,5.515016,-6.094122,-3.931398,-4.381036,8.369958,9.908796,-9.170126,5.660421,5.681119,2.312220,-4.984906,4.547772,-5.237238,5.306617,8.967138,6.389832,-6.644829,-5.904176,-5.034061,-1.227169,4.159403,-7.956188,-4.496749,-3.975059,-2.483628,3.350901,-8.874279,1.195972,7.285195,-8.453768,6.818256,3.005468,0.958937,-7.853770,-0.699606,-3.296118,-9.860498,-4.126207,-7.745830,-1.882977,-4.138927,2.527323,-7.365039,0.245400,-9.049479,-9.184075,-5.323728,1.081053,3.093969,4.197055,-1.163913,2.583413,-5.905902,4.736635,7.098224,1.434284,0.031599,-7.773475,-3.463384,-5.347931,6.960455,-0.458588,-6.404523,-1.504412,2.068749,-6.027414,9.807192,-2.655282,1.155081,-0.838258,0.552548,-4.198888,-4.019624,6.172621,5.270460,0.215518,-6.161354,-8.038800,-8.442746,9.371555,-2.630791,3.191552,0.693544,2.184487,-4.867174,4.001624,7.652284,-0.853825,-4.962228,-3.145285,9.069603,2.987780,2.425966,2.171457,-4.399617,2.033606,-5.121692,-3.147255,-9.727362,-6.164433,5.716249,3.342302,1.817276,-9.377694,7.936474,5.144360,1.082319,-2.463775,-6.586627,-1.768828,-2.142182,7.037520,-3.764346,9.687428,9.677763,9.821641,2.793128,-4.581009,0.992232,8.315162,3.663276,9.167881,3.516993,-5.680356,9.216064,-5.737965,-3.373737,-9.793968,9.070956,-4.532263,5.632466,0.273502,-6.409734,-3.887075,-2.821288,-9.930487,-9.331829,-5.598198,2.727481,-0.203922,9.152351,2.455262,-8.264815,4.776999,1.426864,1.839130,5.014538,5.693055,-1.264043,9.828163,7.202339,-2.888721,-8.181154,9.476134,9.903728,-3.044377,-8.708627,2.281752,-4.506039,-5.665506,-0.898691,-7.294199,-8.786965,2.304864], dtype = "float32")#candidate|10473|(225,)|const|float32
call_10472 = relay.TupleGetItem(func_2109_call(relay.reshape(const_10473.astype('float32'), [225,])), 3)
call_10474 = relay.TupleGetItem(func_2112_call(relay.reshape(const_10473.astype('float32'), [225,])), 3)
output = relay.Tuple([call_10447,bop_10449,call_10472,const_10473,])
output2 = relay.Tuple([call_10448,bop_10452,call_10474,const_10473,])
func_10498 = relay.Function([], output)
mod['func_10498'] = func_10498
mod = relay.transform.InferType()(mod)
mutated_mod['func_10498'] = func_10498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10498_call = mutated_mod.get_global_var('func_10498')
call_10499 = func_10498_call()
output = call_10499
func_10500 = relay.Function([], output)
mutated_mod['func_10500'] = func_10500
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10507 = relay.const([[[-0.950341,-5.989178,-8.695153,-8.721067,-7.782202,2.135634,-9.389200,1.198595,9.166067,-5.531511,7.943894,5.929985],[-9.170556,-1.884649,8.230613,1.469478,-3.041304,7.047310,7.641626,9.083822,-8.149096,6.030422,7.352027,3.871940],[1.082556,-1.743562,-6.881968,-2.823975,-6.314680,3.826574,-6.278278,6.621396,9.249434,-8.867850,-3.816320,-6.093751],[-7.062319,6.229405,-8.510192,-7.807571,5.040824,-9.916128,-1.552357,-5.648624,-2.818074,0.011066,9.680916,9.050161],[8.486256,1.372391,-4.281519,-1.381426,5.469923,-3.760344,0.628942,2.729728,9.833617,-0.465414,2.194152,-0.779834],[0.634187,-0.817835,-0.482102,3.864224,5.160980,6.881907,-7.694733,-0.362640,-3.893153,8.736361,3.462707,-7.395888],[-7.913187,7.131453,7.436959,0.731262,9.001006,6.445255,-3.856035,5.829400,7.517858,4.056158,4.964012,7.322074],[-8.068711,0.215972,-5.162337,-3.012558,-2.171096,-1.454707,2.734209,-0.778360,7.474594,-4.439906,-1.358458,-7.274246],[-8.222515,6.653455,3.008397,4.612831,2.784474,-4.040265,-8.993897,3.605042,-7.851998,9.164970,0.457926,-6.255207]],[[2.254438,-7.055225,-8.327787,-7.588661,-7.448605,-1.862876,-0.906178,8.558326,-3.688863,8.138867,-0.396539,-7.647618],[-5.425681,-4.914616,2.929178,2.126419,2.660585,1.814106,-4.438292,1.378259,3.168274,-0.506661,2.622679,-4.527975],[1.857743,3.365969,-6.448498,-5.119430,5.035299,-0.967658,0.143215,3.488485,-0.089855,9.523703,-7.255817,7.995770],[-1.474381,-3.085379,-3.373533,-6.758842,-0.083489,1.072926,4.424583,-4.631822,3.541749,7.898309,-9.022280,0.067928],[8.033914,1.176822,5.478011,-6.492300,-2.938887,-6.984657,6.874000,3.357702,-3.083561,-4.488585,-5.794775,-9.001484],[9.140965,3.979743,-2.436052,-8.182820,5.236692,-9.037151,8.846268,-2.103861,5.955065,-7.668404,2.270149,-1.398831],[-1.485222,4.268631,8.597592,-0.885480,-3.869772,-6.929846,0.899979,-4.758390,-2.386138,7.081506,9.235916,-6.945250],[-0.637136,1.473607,-8.259203,3.951501,-7.520949,9.709082,-2.939790,6.183960,4.953888,-8.431680,-0.418594,6.506448],[4.505643,-5.850616,6.327056,5.741290,9.672672,3.013328,-8.119355,5.752890,-4.000005,8.963606,-1.235269,3.706491]],[[-1.560174,-8.819932,-4.123378,-4.347199,0.865006,8.537143,0.576500,-2.633941,4.868213,-0.006068,7.768764,5.149686],[-3.506157,-1.884905,4.956096,7.826918,5.454366,-7.029868,1.052813,4.606585,-5.263098,6.811130,6.986596,-2.870944],[-4.863066,4.634311,-1.844087,2.072730,9.881526,-8.211491,9.412688,-8.113211,0.611784,-9.915649,6.701514,3.232107],[-5.126582,2.545806,2.895256,0.160163,-1.921330,0.985497,6.174773,-2.934606,-2.046426,7.536245,-8.003695,2.453204],[-0.600317,-8.258647,0.534647,2.149183,9.648520,-4.413475,7.816591,-2.005326,-2.490154,-2.163690,-4.289886,-8.131662],[2.721417,-0.251408,4.578005,-3.602881,9.427841,-4.601680,-2.361115,2.338178,-9.630489,-9.162554,8.464324,-5.205050],[-3.053763,6.178135,8.515283,-4.063907,9.490539,-2.762406,-7.870924,-0.523700,8.369122,-9.817287,7.498566,2.871891],[8.223832,3.847916,-7.918518,-3.899415,-4.268868,7.382148,5.296249,0.623605,-9.058802,-8.975872,-5.182994,7.845741],[1.492990,3.602408,6.100689,-4.713216,1.196085,7.190052,7.605534,-9.992796,4.134719,8.709251,9.717653,6.776314]],[[-9.213963,-5.206820,-3.142028,9.636077,-1.149278,-7.218046,8.333505,-8.412453,-4.162036,6.347722,-5.564350,-5.272296],[0.473846,-4.754076,-5.148375,2.916597,0.681136,8.674331,7.427491,0.705444,3.540781,9.296768,8.595615,8.531431],[3.035148,6.226922,4.227088,6.831335,-4.779033,3.861204,0.111686,6.074872,5.756404,-8.772121,3.612627,-6.500701],[-6.224940,-2.985660,7.874737,9.793935,-3.183935,-1.892080,-0.687755,-7.572386,-5.479943,8.994437,-5.558655,-0.533703],[8.457535,-6.517535,2.004538,-6.549213,-7.792679,1.750378,-7.242492,-3.382605,2.685756,-9.874389,-4.839472,-2.922856],[9.780480,-0.731559,1.388647,4.151199,-0.712795,3.387976,-1.946940,2.768155,-7.285482,-6.261731,7.449246,1.317520],[-9.025794,7.605729,0.187185,1.236263,8.293430,-5.612628,-0.794275,-4.716465,-7.906495,-0.359361,3.356266,8.940239],[-4.023904,-1.007868,0.179287,2.736689,-8.164303,-2.770674,-3.472421,-0.583941,-3.774469,-4.512882,-3.918931,8.440051],[1.493831,7.743739,9.304901,-3.035735,-0.777301,4.602581,9.264929,1.511915,2.964222,9.637397,5.909608,-8.375095]],[[-2.028459,2.924525,2.040123,0.687126,-3.854414,7.260632,-0.590245,-5.039449,-5.364773,-0.816287,-5.355627,1.844326],[2.893807,9.904558,-4.805371,-1.471388,1.276634,9.565008,-3.778673,3.029099,5.257825,-6.852991,-9.102684,0.714814],[6.478314,-3.502853,6.957810,0.324046,-3.497273,-3.034574,-0.026961,-9.907725,-5.951611,-8.114623,-2.677857,8.111177],[-3.790777,1.428469,-6.480335,-0.854213,-6.165543,6.630123,-9.950758,0.348316,-6.745375,-7.044474,-0.746379,-0.088429],[-3.866059,-0.296722,-6.060070,0.595559,9.422344,3.004899,2.624227,4.972983,2.993857,7.962209,-8.937546,-3.467208],[-3.569651,1.502968,7.836583,9.095814,3.816564,5.045113,-3.045335,-8.395440,9.986326,0.386764,7.851823,7.560681],[-6.964957,1.729897,4.789202,5.207506,-6.709628,-8.266053,-7.880396,6.176611,8.688492,7.536293,2.340742,-0.216083],[9.300501,5.558953,-7.415782,4.609088,-6.963170,3.753869,0.602981,6.573315,-8.144098,8.148256,-4.232089,-1.999362],[8.664695,2.761860,4.397198,-6.351539,9.012624,-8.368269,-0.323707,-3.869360,-4.146060,-2.539335,-8.700135,7.238959]],[[7.726239,3.029084,2.342223,-2.551829,4.456976,-6.863129,7.595457,-4.714888,-1.292836,-4.014651,-2.923200,6.157312],[3.935868,-9.755672,-9.832813,-8.892110,9.363438,7.843818,4.906341,9.405459,7.557134,9.808106,-0.473777,5.157535],[-0.455878,5.608782,9.751469,9.035426,-3.608388,-9.724436,4.527448,6.330003,0.567986,-9.717505,-1.872893,7.233417],[8.461622,-1.296919,-9.970549,-0.946129,0.648322,-0.961579,8.596702,9.569289,3.312204,-5.597007,-9.904355,3.113967],[-4.849998,-2.722194,-0.129865,-1.090355,8.615305,9.989055,-2.705087,-2.020224,-5.229547,-3.393543,9.525912,3.198415],[-4.223315,8.852350,1.793287,-8.784329,-6.231789,-0.942436,-5.794537,-5.679716,9.082922,-0.685455,-7.962586,-2.351273],[7.599148,-5.632812,-1.342615,6.168003,9.037064,-1.481878,-2.276287,-4.961815,1.821083,2.388104,2.739922,1.165793],[6.206783,-7.861721,0.694598,-9.920107,-5.191920,1.018084,1.671156,0.503602,7.355877,4.831120,-0.884159,2.833915],[6.641291,3.918963,-3.066241,7.630185,-3.777943,6.887949,-4.274976,-5.850578,-8.350151,-1.002496,3.413099,-9.991830]],[[1.230568,-7.123462,0.653740,2.177410,-8.912637,0.531694,-3.739434,-8.124958,5.057786,-0.384648,-1.996034,-3.776817],[-5.749035,-9.520061,-2.187394,-8.773628,-0.299055,7.055819,-4.442591,-3.811290,9.932106,-6.651295,5.076108,7.923361],[-7.970172,-2.517436,-9.956365,-2.570842,9.691093,-4.396643,4.682252,6.269158,3.075914,-2.805996,-8.029687,-8.783071],[-3.280549,5.949842,-3.345554,-4.389905,-4.034761,6.832369,0.781775,1.466323,-8.759332,-0.812150,-9.890731,1.364157],[-8.202047,-1.058193,1.426988,7.721248,6.757439,2.705796,3.159018,-0.595656,-9.855605,-8.808067,3.702339,3.365334],[-0.143063,-7.077285,2.078376,-2.397010,0.516906,-1.806617,-8.676528,-1.265372,-8.932067,4.362984,-6.823929,3.736334],[4.397515,-7.672097,0.521149,-3.516519,-6.847239,6.145294,-7.822360,7.618426,-1.164636,-6.331964,5.505576,-9.854514],[-9.227644,8.619985,2.980401,-9.057664,0.233654,-4.391337,-2.735166,-0.215922,5.052619,-6.532530,6.073200,5.222304],[-1.783658,-4.528446,-7.913170,5.486724,-6.600101,2.636517,-4.435029,-5.652026,6.663046,-0.920828,5.618049,-3.000033]],[[-6.252018,6.443450,-1.953811,1.924775,-7.622072,8.888596,-6.957959,-8.673411,6.515083,0.636162,7.161182,4.532038],[-9.357480,-6.468413,-2.339192,-3.258029,2.175503,7.608592,-4.950270,-0.433500,-7.193665,7.023774,5.856358,-1.687215],[-8.638005,-7.084872,1.824084,-1.915868,2.764776,-8.689835,6.673358,0.409922,-1.385671,-0.074054,3.912675,7.168687],[-3.352578,1.527791,-4.246533,7.646116,1.719412,-4.381748,0.146379,-5.034244,5.275453,4.447000,9.059907,-5.387426],[2.553698,-7.777048,4.795019,-9.030828,-4.021613,3.762281,9.168097,1.496933,-6.928765,-6.824065,-3.955304,9.742610],[7.980915,-8.682931,6.436787,-7.053547,-7.420675,2.396710,-6.441797,4.860575,2.407375,-8.388251,4.042815,0.569566],[1.651112,-5.027683,-9.953844,-5.727241,-0.708347,-2.630285,0.729379,-5.336943,3.734687,3.164295,0.755109,8.979531],[-2.726986,-1.401640,2.936951,0.869660,2.304723,7.973697,2.485750,0.475160,-1.614607,2.395370,-6.908308,5.658824],[-4.606301,8.436611,-5.313991,-9.752040,-9.399208,-6.584608,0.299486,8.536484,4.430631,-5.603978,-8.906109,-6.641897]],[[-7.782945,-1.090803,1.282467,-7.879973,-4.674325,-9.981960,-5.052523,9.084155,2.129826,2.558726,-7.607263,0.401489],[9.468291,-4.067120,1.566077,-3.741962,9.715951,-7.171392,0.356610,-6.540318,-0.894207,-0.334652,4.726555,-2.705612],[5.685562,0.046131,-2.716973,-0.183598,4.973028,1.875881,5.049513,-8.728034,-8.179283,-0.389294,9.853857,2.441948],[4.753104,5.832814,-0.658374,3.824966,8.250083,1.899727,7.531220,9.248900,-2.898273,6.242344,-1.460615,-9.672804],[-3.588457,-7.520680,9.014784,6.895109,1.301661,-0.629772,-7.863845,-3.033125,-1.339860,1.060037,1.321532,-6.561996],[7.639236,0.355455,9.740129,-1.421912,-8.019699,-4.993638,3.793940,-9.264079,-1.345568,-4.359640,-5.564976,-5.483640],[-2.330005,-9.837678,-0.199332,0.084993,-4.283350,9.330307,9.088216,7.556709,5.598798,6.254959,-7.835038,7.739271],[-8.579257,9.543207,-9.000071,-1.186418,-2.537214,-4.638412,1.627722,-1.260989,9.405003,-7.937282,-9.387906,-4.540081],[7.982984,-9.580623,-5.629609,-2.605321,0.874993,9.946066,3.281022,-6.839608,5.843117,-8.503154,-5.997022,-4.489683]],[[-6.976293,-3.680246,1.536856,-3.829959,4.559567,-7.835212,8.742369,-2.960035,-2.253206,-5.824849,0.043620,9.023627],[-0.686270,-2.057982,6.550676,-4.413011,6.091664,-1.312408,9.814674,1.231716,0.868091,-9.912352,-5.303381,3.143218],[3.601998,-5.528299,-6.277532,0.026176,8.752517,4.122211,-5.284151,-0.972980,9.991173,-2.488592,-4.914211,6.063859],[9.696296,-6.214386,-1.422776,6.005240,0.001979,3.563697,8.773229,-7.717208,-5.772895,2.322517,6.408198,-1.675758],[-9.723531,-9.567381,-9.771461,-3.514120,2.846934,7.622715,-1.347080,8.175203,-2.574500,4.510684,1.701053,-3.478714],[-8.558089,0.269437,0.501166,-7.605779,-9.769189,-3.644734,-9.732778,1.253485,6.875123,7.717463,5.485987,-6.146395],[8.753728,5.378462,0.245021,-4.665648,-5.130880,-7.739616,9.368843,3.649222,9.958607,-0.205775,5.576135,1.124963],[-7.910944,-3.564720,-7.011841,9.810290,9.049173,-7.922730,-8.025483,-1.998395,-8.092288,5.110412,4.343328,-4.805645],[-1.627349,-5.437178,-9.663226,7.263560,-8.478988,-0.610603,-1.443409,9.817323,-2.408820,-0.465316,-3.022326,3.549242]],[[6.495753,9.921307,-3.397008,1.327620,-1.263961,-2.065518,-7.366663,-1.755572,1.264764,9.028574,-4.533769,1.391937],[-1.748579,-2.513872,-3.261112,-4.635861,-7.914855,-8.706247,6.665607,6.918108,5.997819,-3.486281,8.271600,2.282848],[4.230718,-4.858281,8.248813,-7.671755,-1.335861,-7.979267,4.166295,-4.085652,-9.510657,-4.123088,2.464398,-9.900841],[3.302095,-8.989952,4.502695,5.534735,-1.973610,-2.478153,-5.496408,6.824957,9.020022,5.057892,-9.308131,-0.629535],[0.035073,-3.693977,3.993168,8.695433,7.282634,3.568210,3.854231,5.318203,3.231337,7.584827,5.721034,-4.486460],[7.147383,2.599747,7.064792,-5.689531,-8.586210,8.655500,7.818121,-9.691875,-3.943415,0.673206,-5.290977,9.368732],[5.824802,9.104556,-4.984423,2.333785,-6.018513,5.942658,3.717316,-4.787541,3.619766,8.694439,-1.336599,5.294956],[3.940612,0.015862,-3.860594,9.585661,2.998577,-0.406280,-3.654252,5.266810,-7.136111,7.811406,0.886792,8.008817],[8.590195,1.339590,-5.506974,5.340039,-8.387066,9.372306,3.583862,-1.474159,-1.324099,-4.472909,-8.471586,5.093072]],[[8.376383,-9.873986,-9.694431,2.879078,-4.664144,2.490618,1.057569,5.890520,3.115996,-1.927079,8.931421,-3.695010],[5.445425,6.271339,-8.280415,-0.988742,9.146909,-0.950954,-0.637745,8.299456,5.762843,4.757963,4.524635,-5.549230],[-3.611563,-6.494725,1.695112,5.848709,1.659985,-1.182550,1.149858,5.016961,-2.518895,-7.552504,2.881295,0.614852],[-9.485045,-8.113247,8.034073,5.748816,1.842265,-5.870937,-0.068393,-9.193964,-6.328273,3.519959,5.222295,-3.435520],[1.858619,4.859384,-6.890875,4.154005,8.003635,5.546318,-3.461231,-3.579149,-9.401630,-7.782586,-7.207018,-8.125966],[0.793867,-1.291031,9.693298,-6.146454,0.509047,9.402333,8.939041,5.609660,-5.003329,0.043205,7.725830,2.927939],[-8.324151,-9.252152,-8.513955,8.447829,-6.692331,-9.982534,-3.986604,-3.870723,-6.448645,-9.349513,-4.035119,4.055108],[-3.576312,8.027417,-4.281291,1.626752,-8.131061,-8.054549,-8.485414,6.145868,5.938067,-7.113071,-6.720642,-7.297538],[4.630260,-0.398704,-7.767155,-6.050123,7.794736,-5.049156,-9.120532,-0.875872,2.998053,5.725468,1.581277,-5.118265]]], dtype = "float32")#candidate|10507|(12, 9, 12)|const|float32
uop_10508 = relay.atan(const_10507.astype('float32')) # shape=(12, 9, 12)
func_1190_call = mod.get_global_var('func_1190')
func_1191_call = mutated_mod.get_global_var('func_1191')
call_10512 = func_1190_call()
call_10513 = func_1190_call()
func_7508_call = mod.get_global_var('func_7508')
func_7510_call = mutated_mod.get_global_var('func_7510')
call_10520 = relay.TupleGetItem(func_7508_call(), 1)
call_10521 = relay.TupleGetItem(func_7510_call(), 1)
func_8199_call = mod.get_global_var('func_8199')
func_8203_call = mutated_mod.get_global_var('func_8203')
const_10523 = relay.const([2.112249,8.272934,5.823061,4.972689,-9.601153,8.262586,-1.510943,1.723597,-2.067810,-6.930160,-0.861943,2.752382,-2.844665,4.824803,7.279420,-3.978033,-0.634819,-7.497374,8.560548,-5.366043,9.173894,6.080493,-9.554307,0.852992,6.887836,3.286702,-3.858257,7.836717,9.750818,-5.238933,8.899420,9.994077,-7.191255,-2.226553,5.757886,-9.772584,-6.462186,-6.241328,-0.729780,0.240040,-3.146080,-2.846470,-4.675555,3.148701,-0.683394,-8.389987,-3.463595,7.476041,9.722554,-3.489963,-2.448652,-2.002764,-8.982069,-8.396956,-7.225441,-3.720790,-1.126569,8.183861,1.001818,-7.850483,8.516061,6.438413,-7.415153,-6.743482,-4.570396,-7.145983,8.847428,3.441465,-2.144181,3.652614,-4.534579,7.503242,-0.803420,3.183019,2.449826,2.542752,-5.526477,3.059629,1.449297,1.406109,-5.844095,-9.920595,-0.085709,-3.868902,9.027985,8.578580,2.283240,2.385442,-2.645378,5.490488,-6.919063,-0.111153,-6.236107,-9.345511,9.548432,3.151445,3.690756,-1.322994,-5.886867,-5.934826,-1.859875,3.856860,-5.742084,1.116500,5.626942,7.216576,7.912127,-5.574040,3.214281,6.500304,-3.601455,-5.276127,-8.862232,6.168022,4.594717,2.624674,-7.542522,-3.298586,1.598576,6.864300,-4.547428,-8.872048,-5.449875,3.277432,7.147206,-1.631181,-9.034044,-8.322346,0.325578,9.442265,1.953136,-3.668103,1.529510,4.787787,-8.461515,6.031947,6.497704,-3.573172,-4.711152,4.967544,-0.023784,-8.279268,-4.704760,-3.841467,-4.693476,7.623659,-5.903074,6.237968,-0.952126,-3.121228,1.006256,7.461726,0.333068,-8.439062,-6.222623,-5.666422,-0.573944,4.666230,7.658796,-8.226364,4.236384,6.415722,-8.777343,5.833326,3.129186,0.429498,8.631269,1.960504,4.484099,-0.742308,8.714036,-9.488212,5.753298,8.480785,5.326196,8.249297,5.032043,-3.445633,3.581508,-9.713434,2.002671,-5.512463,-9.657674,-7.630306,8.101855,9.819802,2.874598,-6.645849,1.927499,8.671488,-2.053255,7.699754,1.150855,5.017756,0.967092,-6.090592,9.487889,5.030013,-2.913805,9.921238,7.340977,4.533700,8.121224,2.878032,3.835257,0.408749,3.603376,0.703645,0.659761,-5.242345,-0.579394,6.941635,4.927540,1.469620,-0.351304,2.890059,-7.034338,-7.326493,7.413919,-3.858975,-6.620260,-1.576445,1.798706,8.769906,-7.651521,3.559704,-1.403169,-1.889508,-0.997143,6.470340,5.728107,-1.662695,2.198633,3.800906,-7.068290,9.566430,4.661589,6.147094,8.593676,6.247759,-0.098870,-9.224532,-8.883241,-6.086118,2.048359,6.762074,-5.595411,-6.582642,7.443497,-7.223007,7.783721,-2.434015,7.313547,4.237156,-7.835567,-3.352543,-3.862664,9.962531,-1.604193,2.687853,-4.639015,-5.916836,-4.537887,-4.717287,-7.486865,7.678922,8.764164,-4.003916,3.625105,1.826924,6.354494,-5.786832,2.212756,-0.803893,1.507005,6.356356,-0.628294,3.316608,-3.949631,-7.763185,-2.311170,-6.253704,-4.610785,9.970968,9.848604,3.985548,-1.538546,-3.208826,-1.013172,9.268827,-1.628284,4.872213,-0.108829,2.973027,-9.418158,9.841612,3.766513,-0.379276,9.779809,-8.203768,1.618711,4.559499,2.560949,5.889369,-3.854643,-8.387020,7.708209,4.142211,-1.395682,-3.354101,6.916558,7.817587,7.470482,-3.990467,6.463330,2.189471,-0.657343,3.258235,-0.215932,6.311565,0.810624,1.298516,7.626548,7.685661,9.484227,4.425313,2.732770,-7.743427,-2.422228,0.740667,4.397031,-2.505356,4.525215,4.798095,-5.524576,-9.359631,-7.576519,-3.362059,6.417361,5.900800,9.862466,2.948741,-1.772284,-5.678263,-0.629894,-9.364262,-6.489824,4.685642,-9.088672,-0.272250,-6.697592,9.089833,-5.954607,-7.239563,5.248795,0.412391,-1.017609,1.223754,-8.221340,-7.227242,-7.171930,-8.608572,5.067796,-5.966031,-1.910042,7.828739,-9.727814,-3.424266,-0.926615,-5.939479,-8.986623,5.071103,-0.398611,6.876087,-6.944881,9.753035,8.661496,5.608211,3.126128,-9.170063,-6.051206,-7.306921,-0.050609,-6.556338,-1.605913,-0.819784,-0.569079,6.298112,9.052526,6.115797,-0.740994,-9.060225,-5.954998,5.091083,5.152470,0.894762,0.766163,-9.123562,-3.572756,-1.059901,0.033833,-2.270399,-1.248978,-1.845193,-2.937452,2.967918,-9.081027,-4.046498,-3.525579,9.339021,-5.543900,8.894967,-7.681101,1.222615,-0.532756,3.102869,5.780586,2.821884,-5.069753,5.166049,2.105850,7.708515,-6.101521,-2.448440,2.096585,-5.264303,9.858475,1.291317,-4.084883,-7.878747,9.934945,-5.671490,1.539867,-4.953904,-6.847490,5.848782,8.416677,4.502968,-8.030904,-5.097794,5.365703,0.801579,-7.314877,1.329345,-0.186029,-2.857020,9.683662,-8.950874,-3.228644,-9.221680,-0.987990,6.318985,9.709307,0.633344,-8.353581,3.601901,-6.855351,-6.359445,-9.201273,3.999051,-2.624956,-0.466605,3.958219,-6.981528,3.454068,-4.497513,-8.503519,2.958167,-8.968652,-4.036280,-0.091106,9.323993,-9.358688,-3.074903,5.662741,6.434613,0.283983,4.857015,-3.594217,-3.185568,9.662323,9.141787,-9.204457,0.394451,0.304620,-5.800720,0.590851,8.139291,1.922115,-3.288748,5.037888,-7.938723,4.985162,9.666968,-7.230291,-5.925677,-1.006323,0.233574,-3.974989,-9.700577,-4.152669,-7.716240,-8.910570,-2.170536,5.730356,-6.061164,-7.203090,6.736725,-0.948898,-3.256674,-6.541125,-7.987203,-3.724951,-6.415651,-8.770657,0.030706,1.354741,2.214189,2.286070,2.243929,-9.941656,7.126115,0.053448,8.299936,-2.284761,-6.273497,-7.352929,9.087675,-5.546913,6.169472,-3.309467,-6.148142,-6.678307,5.139162,1.661109,-4.652287,-3.518542,-1.561163,-1.820314,-0.872359,3.060441,-8.305625,7.597597,6.641205,0.410687,7.150295,8.356242,9.852555,3.506008,7.711483,0.465589,-1.121800,7.349693,1.345052,-4.856861,-4.252116,-8.349115,1.903996,9.083229,-2.512746,-7.004222,-3.166816,1.070728,7.951083,0.741889,9.672167,0.168188,-7.354372,-9.667631,-3.383184,9.001509,4.188002,4.718306,-4.558115,9.986197,9.296724,-7.006650,4.606087,8.445856,-4.364502,8.438750,-1.255990,6.837745,0.094700,-7.474372,2.519428,7.738169,-6.132392,0.915220,1.483683,4.518409,-8.709239,-2.235075,3.641630,7.343411,-9.095105,2.269333,1.170081,-5.796444,-0.781463,-8.793660,-5.024296,-4.654680,5.255645,0.897105,-0.466445,5.894310,-1.898316,-3.580888,-4.210344,5.930455,-7.075758,5.788542,-5.651922,3.822155,-3.688620,-2.112899,8.664263,6.206027,-3.602964,9.742073,1.317675,-4.832905,-8.989859,9.519573,-0.583772,-8.299302,6.595249,-8.953175,9.485042,6.997669,6.392063,-7.824159,-2.987252,6.072424,4.076090,-3.282293,-6.936451,-7.015774,9.449026,2.084192,3.168667,1.463658,9.955049,-6.572729,1.037425,-6.766333,0.699906,0.642982,7.573446,-9.394659,6.202117,5.582192,7.372005,-1.184758,-6.806649,-9.100940,6.122641,-2.482218,4.431032,7.526606,-4.953992,-9.446141,3.213818,-2.690110,-5.230619,7.629603,7.645157,9.628572,-0.175795,2.084361,6.213673,-0.937827,7.976341,2.535686,4.721385,8.218206,9.348456,8.063205,7.530342,2.493091,3.403589,4.827572,3.513961,0.673090,1.656836,-8.718046,9.095275,8.726295,-4.967788,8.513432,-2.400843,7.215699,-1.593954,-0.653987,-9.123382,-6.286221,-4.963401,-4.962850,-2.329862,5.146037,2.219118,6.185987,9.833461,8.149647,0.287336,4.321716,-6.012367,5.092696,-0.991047,-1.195810,6.185825,-3.058434,3.695090,-5.923830,-1.871319,4.153916,3.366989,-0.330635,2.817403,-8.309652,3.816093,-5.028696,1.697631,-8.753509,2.196975,-6.620031,8.483022,-0.763393,-6.973561,4.426454,4.194002,-5.595461,3.100519,9.770423,-6.696075,8.313379,4.562480,5.337727,-1.407364,-6.717524,6.751537,-1.117855,4.098780,2.282090,9.049809,6.413250,1.226878,-8.658220,-6.789590,9.959421,5.551359,-9.653617,2.178044,4.456956,-5.076744,6.557564,5.035525,-6.115546,1.137000,-9.082702,-5.737074,1.484010,7.556688,-7.594342,6.611931,-9.500580,0.686096,1.442812,7.759335,-0.341014,7.385032,1.159130,3.405144,4.409852,1.279519,-8.588794,9.920542,9.954545,2.654253,5.446456,2.429141,3.769486,-5.120524,4.694546,-8.939336,8.928462,-1.168858,-3.674625,1.752629,-2.837532,3.821533,-3.952495,-8.779638,4.786967,-2.641363,-6.788824,-9.030481,-8.802777,-2.981339,-8.856262,5.883320,-0.506585,-9.107429,2.413620,5.918193,-9.692697,-0.663839,6.827864,-5.015190,-6.873976,2.691080,5.310698,5.127742,7.802263,1.507231,-3.157609,1.522655,-1.530479,2.034615,6.834495,3.623463,4.232144,9.547089,-7.905457,4.096662,-7.305025,6.523029,-7.681822,3.212805,3.852905,-4.952384,1.537604,-8.375188,0.786358,6.237142,-4.483945,5.657534,9.588363,0.491653,-5.710229,-3.281236,4.165501,-5.950049,-0.624087,0.303843,3.615196,3.156460,-5.430362,-8.831933,5.272493,-6.029201,3.045389,6.177223,-8.091110,-2.072278,4.609157,2.484927,6.495932,1.020401,0.437465,4.793256,-3.573648,0.084283,-9.587826,-2.575288,-0.105588,-3.827079,-9.827628,-5.866448,-6.238441,-1.625434,8.463604,-3.661568,6.058367,6.855812,0.231548,4.859212,3.897393,-1.183830,9.878691,-1.553755,2.335435,2.477973,-1.556341,1.567911,-1.820318,3.273659,7.766523,-7.254044,9.831647,-0.684108,-3.929848,-8.703389,-1.844247,-1.263547,4.064619,7.390587,1.366424,7.343945,-3.188786,-3.631585,-5.517782,7.099715,9.259953,-0.884858,5.103249,0.112358,1.610361,4.635821,-8.301092,5.836317,-7.028717,9.790276,1.563877,-3.317868,6.698833,-9.054836,-1.078725,4.349544,-2.898223,-0.901091,-8.038048,7.904954,7.488219,-1.563324,-8.230791,7.428638,-4.629779,-7.577061,2.594338,-3.349704,9.711651,-7.721754,-1.861071,-8.374382,-2.985370,-9.710216,-5.234509,-8.658235,-4.292854,-1.516735,-7.749669,-0.940337,-5.184688,-5.497652,1.277303,-2.736914,2.660650,-9.338214,-4.566045,-7.475496,4.419202,-9.893898,6.890025,8.300348,6.829720,-1.878145,9.935702,-3.025058,-2.314898,-5.127990,7.077317,-9.280166,8.982565,-8.531413,2.846589,-1.973455,4.894527,1.877892,7.584466,1.621557,-2.056983,-2.015325,-3.125324,9.727740,1.972252,-8.380309,-2.424585,-8.941379,0.126958,0.570984,4.526586,9.103660,-6.937656,5.462095,4.961670,-5.256538,2.791199,8.018327,-8.788477,-5.246678,-8.976595,-8.029881,8.723632,4.558320,-0.086518,-6.633651,-8.927257,-9.371762,-9.003304,5.324337,-3.901842,1.576952,-5.520068,7.403532,1.999071,5.717478,-9.124887,-6.882833,-5.868951,-6.286481,-4.241724,-2.770676,-8.079865,-7.997399,5.951405,-1.827598,2.781674,0.066423,1.493254,-6.586790,-6.462891,-4.022590,-4.533704,-7.067483,-9.468893,3.842638,8.002692,-4.896397,-7.480462,-9.709902,-3.564329,-7.362790,-1.493580,9.503680,-8.528540,-2.176564,2.577926,-9.528637,2.480937,-1.180862,7.802391,2.162934,-6.940017,7.722876,-5.886011,-5.151705,-3.006639,-8.721062,-5.282766,-7.452308,-8.388039,2.226199,-2.720600,1.697394,-2.547005,2.587577,9.127854,8.407380,-8.772644,-6.483746,-4.911904,9.530652,1.644793,-1.635665,-9.753893,4.140417,7.312427,-2.525602,-7.579771,-2.475304,-9.518767,-0.898689,-9.252745,6.170557,-8.137545,0.402527,-3.599901,-5.230478,-9.322450,0.031079,2.216569,5.085917,6.813650,-2.088062,8.212304,-9.681091,6.571821,3.252482,-8.972949,-6.707438,1.633362,-2.002678,4.300811,9.709070,0.103801,-8.068444,1.058935,5.117109,8.505024,-5.578617,-7.075061,-0.882979,-9.746255,9.223471,-7.091283,4.589907,7.707308,4.468504,-3.181073,6.726610,6.901700,0.706595,4.212701,1.056946,-7.243110,-0.651819,4.696683,-5.134923,-2.578886,-4.297848,-1.157931,-1.913727,9.216866,-6.010165,3.665314,7.565170,9.800337,6.040058,-0.035439,7.125168,8.683600,3.199569,1.769253,-2.890102,-4.948801,-8.985106,-0.929923,-0.706588,1.777795,-4.870662,-6.480842,1.543563,-3.160707,2.075275,-6.465051,3.812716,-5.654563,-6.729900,6.463685,6.353353,2.596618,-7.241172,6.557244,-4.044501,2.840003,8.512573,-7.280646,7.788960,9.525224,6.814006,7.319137,8.318199,-1.139121,5.064015,-9.986252,9.900254,5.701149,-7.344197,-9.742501,1.889219,4.726219,-6.675962,1.980770,-4.519666,-0.570930,-1.651143,-0.881038,4.954987,6.654147,-9.396310,8.282443,-8.962388,6.240020,1.904952,1.734488,5.371269,1.365726,-5.700929,3.253632,-7.745104,4.383615,-8.145767,-2.596130,-8.337530,-7.807309,-7.827374,-8.641557,-4.322486,7.837494,4.208768,-4.119651,0.421191,-4.576627,9.110948,-0.971877,1.628092,-0.892239,1.769799,8.082971,5.369247,6.330635,-6.520435,-6.613355,6.355295,-9.577701,-7.829462,-6.504093,6.107628,1.446703,-2.216542,-1.781633,9.803419,7.863464,7.386898,-4.730442,3.089743,-6.093775,2.507868,-1.507881,-2.058655,-3.222350,-9.468463,-2.966961,1.193818,-1.751399,8.078175,-7.957667,0.145839,-1.340648,-6.584302,5.833974,-1.215890,3.456373,-1.438137,-7.719492,1.195278,2.363589,7.166559,2.561664,-4.132984,9.369233,-0.087383,-2.124146,4.634593,-7.030980,-4.300416,7.958314,-7.258416,-1.109235,2.162705,2.607176,5.539657,-6.119430,0.598559,-5.831348,1.501094,8.893984,1.841967,4.031424,-1.031612,-8.045065,-8.723976,8.113426,5.147965,8.670712,1.280530,9.248092,-2.341578,5.814431,8.252249,4.230319,5.018615,-8.764432,-7.634472,-3.417986,1.401601,7.384832,-0.177121,-1.696980,5.109260,-2.735207,1.144742,6.825613,7.447470,9.475536,-8.421044,9.722128,7.548185,-1.832814,-2.756150,2.266793,-1.364133,9.982020,4.244804,-9.702996,1.057410,5.234296,-2.516488,-1.877665,-0.929360,-7.325964,-3.416458,-0.529076,3.101924,-7.141230,6.393576,2.363047,-4.597965,3.745327,1.175240,-4.621614,-0.672121,0.412324,2.277681,5.568563,3.438295,-5.044980,4.091500,3.748228,-6.862202,-8.597187,4.361318,1.995537,-6.514438,-8.904038,-5.910207,7.120306,-9.186992,4.610829,-3.715781,9.537339,-7.027595,-8.791756,3.175325,-0.481445,5.399409,3.243796,-5.426853,-1.863488,5.316727,-9.228732,-3.237090,7.320085,-6.655172,-2.425530,2.821032,-2.436877,1.833920,3.889809,1.005941,-2.655409,0.862279,1.695019,-4.988859,-5.877402,-6.315117,5.812023,-0.598972,-6.148411,3.077658,-7.422039,-0.385568,-1.064880,6.408237,-6.097083,4.675696,0.230561,4.785294,2.539978,-0.213579,0.309393,-7.067275,8.890707,0.997492,-2.459718,-7.605782,8.176205,5.255553,2.875107,-7.751321,7.460585,-8.463200,-1.500558,-1.300797,-9.139832,6.723535,1.465516,-6.822295,3.336944,-5.159196,7.112728,-8.077876,-9.573833,-5.718714,-3.902168,3.088227,3.128088,-5.050430,3.863250,3.348080,4.374762,-1.385174,-9.122139,-9.493092,-8.149543,8.922491,4.028524,8.629699,-1.095972,5.326015,-5.893064,-1.972801,5.537085,5.724274,4.008275,-9.427562,4.782735,-9.173349,1.197078,2.929534,2.329327,2.489243,-1.269747,-3.406813,7.956532,8.696998,2.242203,6.217044,-4.812799,2.041200,8.714007,9.051298,-0.340808,-0.322674,-8.152047,-9.915964,8.104691,-1.898290,-3.608785,-7.534473,8.493372,8.593239,8.804051,0.138604,4.007072,-2.898390,-8.676255,9.108112,1.490501,-4.661736,-7.804188,9.140582,8.542931,7.310841,9.717978,6.231408,-1.798587,4.251658,6.132632,7.120742,4.398941,2.242609,0.697579,2.556190,-8.778977,-3.701809,-0.564892,-4.097353,-9.038459,1.511587,2.631327,-0.132585,6.664514,-4.653025,-4.524610,2.214324,5.464771,1.709814,0.145656,3.781744,-2.036228,-6.912308,3.151701,-6.879901,1.732442,8.653830,-0.731470,-5.554472,8.779268,-1.272150,-6.983142,-9.616653,-4.341854,2.368639,-5.654005,-3.297420,-2.747895,7.905048,9.486799,7.559877,5.143973,-8.959581,-5.969631,3.355870,0.879607,5.010330,1.097495,6.983286,1.256771,9.432952,4.895483,9.992796,8.957448,2.740363,-0.786517,4.266036,-6.308564,-5.711676,-8.354515,-4.180296,1.334226,2.245145,3.556230,8.464429,0.238173,-6.676779,-9.597531,1.528784,-4.057659,-6.891961,0.133163,-5.921555,8.305948,5.991961,-7.388987,7.914681,1.252516,-0.831690,8.643716,-9.172333,7.616798,5.430325,-8.539849,0.972842,-7.729686,7.426418,6.749231,7.669659,-6.766585,-9.405061,-4.281657,4.310386,-4.499730,9.345431,2.197377,9.352515,-8.076805,-3.495004,4.591034,-1.987157,0.502242,5.336545,8.392293,-7.873141,1.622534,1.833725,-3.051628,-5.189470,-2.943291,3.482188,7.980380,-0.300637,9.755803,-7.336978,-7.181477,-0.194325,-5.651099,-2.283248,-9.273192,-2.063830,0.036803,-3.591429,-5.449038,7.375218,-3.081207,-7.729341,8.260637,6.769433,9.867224,6.703914,-6.061609,5.078674,7.328542,0.809079,-2.239400,-4.451970,2.393300,-8.028049,4.775765,-3.011098,-1.912245,3.295753,-9.806046,-3.687946,-0.282455,2.999144,-7.990112,9.046931,5.950008,8.782790,-5.071954,6.402716,-1.450652,7.715994,7.979601,9.318142,-4.164097,3.911198,-7.684516,-2.489320,1.074087,9.273982,5.124033,-1.584798,9.542234,-5.908041,8.338089,0.127025,4.092570,1.990952,9.192205,-2.797097,8.406221,-6.564613,-7.714397,-6.905166,-1.799845,0.950729,-6.054146,-9.369509,5.657299,-5.350226,9.564350,4.011258,-8.883748,8.142637,3.343794,-9.771132,-4.310594,-1.404778,9.353205,-4.723093,9.961127,1.334502,1.625187,2.777915,4.684331,6.581943,-8.284297,9.799215,8.272966,-6.456229,9.531988,7.551729,5.157599,-4.694488,-0.963098,-4.654796,-9.300489,-6.917205,-4.728356,-8.019227,1.013466,-5.274881,-3.925104,-2.824279,-1.298468,0.665639,7.217123,9.645060,-4.650210,-9.406854,5.162399,-9.966689,-3.774151,7.185390,2.965865,-8.102087,-1.863109,-4.915164,0.985860,-0.909056,6.031129,7.021454,2.044590,8.434400,-6.645188,-4.149596,-6.048696,1.462671,9.345512,3.148991,-3.148289,5.083707,-4.404277,-9.156458,4.949753,-7.433962,-5.614751,8.283693,-0.214961,5.308315,-5.878571,-9.909768,1.498031,-6.799406,2.022069,1.566721,0.502604,-9.471869,-4.890222,1.709170,2.449282,-0.538294,2.493934,1.558913,-9.703806,-8.974626,4.188178,3.759247,-3.046600,8.986368,-0.195074,-8.282591,-7.821993,3.860670,1.787707,-1.302422,-2.594823,-8.569536,-3.592797,-3.229351,-8.172798,-1.313314,6.863112,-3.835412,0.959299,1.274179,-6.521233,9.442870,-2.536766,3.455973,-8.858490,3.563484,-5.968860,-6.141017,2.227036,0.762752,-2.418190,8.471092,-8.174181,3.865027,-6.656769,1.352069,-4.791495,3.419641,8.007412,-6.142174,-0.740744,6.309292,9.479598,4.930034,-4.751715,8.678074,-3.998494,-9.561482,-8.243994,-9.490231,6.054019,-3.048335,8.839810,-8.041580,-4.789273,-5.293841,-4.686461,-8.554743,6.454266,7.618772,-5.786714,-1.934056,5.134740,6.303366,3.264925,-2.163786,4.705275,-4.757289,-2.833268,-2.731131,-4.479365,0.103447,-2.911334,-8.697960,-8.031904,3.569244,-2.961691,9.773098,-2.034289,-5.719462,0.728910,-3.985498,7.036691,6.248945,-7.959206,-1.804913,-4.440610,8.982248,3.660531,-7.909851,9.376585,1.330501,-5.921519,-4.544891,7.467472,-0.508524,4.174715,-8.411766,0.438943,1.103100,9.120677,-6.606520,4.486189,-7.412473,-8.016128,-1.964719,-5.096232,2.744012,2.407362,4.270465,-8.637452,6.604101,2.661439,-3.923036,1.484498,-8.477199,-4.759996,-7.617181,-0.588594,-2.644292,1.556979,8.137264,-1.300944,-7.708678,-9.189228,5.196169,8.144344,-4.213362,-0.550311,-9.538463,-5.551309,-1.392142,8.593411,6.072974,9.018300,-1.797765,-0.631888,-2.946865,2.418477,-8.335152,-9.727667,-3.551261,-1.693429,-3.330414,-0.139381,-7.875785,6.045933,9.861717,3.786984,5.522747,-6.200906,-5.867672,5.186827,-1.528367,0.224218,-4.061899,-5.985679,-7.322038,1.427493,3.907536,7.269009,8.280567,-7.111357,2.363120,3.499815,-3.635255,0.049383,-8.922560,6.393980,5.870409,-9.953487,-3.323067,-5.759464,1.134444,-9.132191,0.398529,0.928144,-9.141944,7.244633,1.787819,-3.097268,7.840966,-6.124750,-1.344294,-8.064743,3.848643,9.032993,3.046307,-3.914677,-1.671483,6.457912,-5.851331,-5.247331,-5.562644,-5.520622,-6.605533,3.373363,-8.821495,4.162655,1.493729,-2.008288,-3.649273,-2.848854,-5.158272,4.447582,6.450425,-6.735323,5.908350,3.980399,2.129335,8.915441,-7.636900,3.663241,4.877416,-9.341767,-6.167171,3.945760,-0.797169,-5.689151,-5.935266,6.679534,-9.744100,9.260099,-6.616207,8.043924,-1.421067,3.888664,7.042718,-3.763944,-6.427175,6.078430,6.118607,1.026000,-4.742591,-5.729704,9.403406,6.035366,-2.333223,3.640058,6.198390,-6.752354,-7.740143,-9.763202,-9.202310,-3.703155,9.729169,4.834012,-1.127334,2.809541,-6.477955,9.450203,9.610283,3.148278,8.275876,3.155722,8.436917,-9.879293,2.170129,8.080017,4.468377,-4.198668,1.853059,-2.627108,0.660545,-6.298840,0.120846,2.946042,-6.706886,-6.272776,-3.645312,-2.074378,0.417062,4.938213,-4.728067,-7.152359,-4.054422,-6.684533,-3.405566,2.328471,-4.422296,2.933817,0.554931,5.242773,9.812534,0.156482,2.536559,6.382477,-3.314710,8.015286,6.017299,4.128651,1.869785,4.626870,-0.725942,2.585609,6.971889,-5.163722,3.424930,-9.655012,-2.278859,-7.669611,-0.959213,-4.774156,-2.663354,1.456407,-6.834219,3.400349,-1.908845,4.128393,5.670049,-5.351438,-7.530572,7.316445,-9.178652,-8.230475,0.354195,-2.158546,5.188831,3.807447,-7.499262,2.584136,3.122837,-1.177172,-6.639231,-9.700964,-3.147854,-2.767940,3.872059,8.903762,6.797415,-9.930258,-9.037308,-2.198500,-1.818634,-4.593983,-4.901734,6.024797,-3.091518,-5.246946,0.588845,3.647179,2.757963,-0.587135,8.476913,-1.648625,-0.784732,-8.494981,8.402232,-8.330727,-6.018644,-1.974088,-3.141860,-2.449758,-5.966090,9.306210,1.925890,3.895348,-8.992793,5.505605,5.600377,1.298149,8.770892,0.406012,-3.272680,-9.437013,-8.676027,-4.643202,-5.966522,8.360651,4.544594,-1.034830,5.179368,0.099282,-2.103760,-8.854117,-3.285261,2.406999,4.940827,-6.001235,-5.262429,-2.911498,9.314610,8.857319,1.351356,-5.713775,-5.960333,8.476774,3.833562,6.683597,8.428086,7.821182,1.906923,4.542440,6.181838,8.760188,-6.178085,-3.816874,-8.235602,6.217962,0.719814,-5.638563,7.192914,0.760375,-1.343184,-6.207720,-5.762173,4.490206,-5.897660,-0.219660,-4.612659,2.579993,1.964444,-3.248194,9.702195,8.934435,-3.203425,-6.263395,8.768616,-7.406271,7.296228,-2.922882,-9.896695,8.448887,-8.996375,4.276209,3.821492,-2.751025,-3.870695,-0.968221,-4.649904,-0.183116,5.761254,-3.888883,1.917536,-4.828156,7.903501,-9.243366,-2.089458,-0.031013,-5.161836,0.180482,-7.558806,-5.313259,2.244457,3.266540,3.443786,-6.050329,-6.032894,6.036449,3.032828,-4.484442,-1.100744,-4.598066,7.319975,-5.130626,-4.167416,1.535979,8.404877,-7.965029,7.504740,-8.962479,8.046734,7.904820,-5.554247,3.944893,1.825594,-7.206607,4.140622,-9.449600,-5.964840,-4.529951,3.338547,8.864162,0.677956,5.386721,8.408137,2.934670,-1.132096,1.851850,-3.894043,-6.757349,-5.886820,6.254810,5.188853,-3.604147,-2.123006,1.186196,2.590617,-6.217170,-5.361896,5.621771,-0.751436,-7.224457,3.885411,1.165913,6.738363,7.054066,-2.665478,6.478073,9.600228,3.527235,-5.907470,4.288122,-1.643571,-2.096453,2.204430,-0.057478,2.495979,-2.264726,-3.802614,-2.128842,1.443138,-4.917778,-1.740448,7.260545,3.753038,-7.529074,8.858196,8.943323,7.388064,-6.141755,5.723393,-5.423157,-7.763959,-5.013158,-4.265368,-8.554348,-9.089325,-1.447110,-6.685435,-6.044396,-5.870691,4.401395,-6.429315,5.368401,-9.177199,-5.946942,3.517353,-0.366769,5.428827,-3.419045,1.207549,1.676387,0.774332,8.929542,-7.794689,-8.603480,-8.534912,-5.331399,-5.108981,-9.204122,-0.150089,3.414251,-9.594937,5.622487,-6.310750,8.615836,-9.162009,4.914379,-3.670145,8.124576,8.586536,-5.691269,3.536354,-6.242733,-8.439932,-1.930876,-0.710119,-2.754321,-2.775164,-0.687185,-5.725184,-5.480270,3.400301,-1.209357,-4.039841,-9.942594,3.204572,2.307212,1.251992,2.439000,2.601392,-8.617007,1.962201,-0.689780,-7.772326,-2.811567,-2.003903,5.673270,-6.862590,-6.847538,7.203139,-4.273539,1.399186,7.024398,-5.321159,-5.825000,0.999649,3.314450,-1.145611,-4.255824,-9.476944,4.939297,9.480000,-9.287655,-7.695113,7.946328,1.922659,4.193992,0.496316,-3.826211,9.409172,3.819563,1.622898,3.125954,-2.013973,5.869353,-1.222699,-8.102016,4.169459,0.585882,5.178548,-3.495458,2.432323,7.087880,-9.914911,-1.485095,-5.506904,-4.928530,-6.296771,0.077144,4.807294,4.242200,2.066131,-6.147007,3.811133,1.621433,-6.145645,5.623942,4.402616,-2.157542,-9.717516,9.005853,0.390010,9.251630,7.604509,-0.840437,5.946575,-6.817639,1.054355,0.924006,-0.886437,0.463521,-4.503500,-8.545844,5.551622,-2.368867,7.546900,8.301263,9.355356,-8.472762,0.472429,-8.489915,8.371040,-4.775967,1.473128,5.486412,-5.432743,-1.974085,9.626895,-4.802349,9.044480,2.184355,-2.735990,0.867718,9.266045,-9.554519,7.485388,6.892190,7.883895,0.538293,2.474661,-1.502654,-2.687129,8.036504,-3.288577,-8.313684,-9.773757,-6.165312,-0.557002,-5.465379,-3.809133,3.919765,4.961587,-5.310221,-8.361517,5.850356,-8.081204,9.737065,-6.616785,-3.652888,-5.698146,9.184522,-7.597464,4.735476,4.415850,-0.192454,-3.817807,2.329276,-1.506395,-6.770061,-6.083254,8.304072,0.295398,5.483309,2.751484,-5.073324,-6.058655,-6.791574,-0.635216,-1.882973,7.266082,5.498223,-3.292494,-3.453477,-7.402539,4.810899,-5.654847,4.623059,1.131408,-6.029329,-2.618715,-8.814704,-7.700331,-3.856119,-5.607052,-4.866743,5.208569,7.381763,0.635924,0.613851,-6.779054,-3.192715,6.136580,-2.950186,-3.221097,3.939728,-4.631300,2.835668,-9.831609,4.100060,-1.845059,-8.308642,2.949380,8.789638,9.549655,-1.873966,1.963321,8.532446,-6.346158,3.154189,-5.926907,5.463964,-6.672293,6.395142,-3.976244,4.719622,-9.181112,3.279035,6.200958,-7.481794,2.227281,-9.805014,7.225014,4.806193,-3.084732,-9.698621,2.852149,4.589805,8.731176,-4.526064,9.634728,-1.424363,3.286216,1.596147,4.872676,-2.113855,-3.880161,2.981418,-8.283624,1.349374,-8.924772,2.158968,4.711454,5.287604,2.282332,7.572467,-5.206293,-7.031180,1.273154,-1.573447,-3.220524,7.698370,-0.893282,-3.867347,8.596725,4.927166,-1.399448,1.244202,9.385574,-4.798693,-8.708002,9.796093,6.877446,-3.924633,2.341926,8.412175,6.937700,-7.443476,-8.265864,-2.720778,-2.529178,3.402047,-4.510416,-4.127378,1.763179,-6.690865,-8.367510,-6.360438,-6.442608,-6.892104,-6.013362,1.523664,-0.456213,2.856991,-5.459423,-8.514979,9.808414,0.588270,-1.773291,0.271197,-9.729900,5.936506,6.308094,2.825782,5.868612,4.452295,6.770383,9.102170,-9.708579,-9.443194,1.830307,5.309714,-3.510775,-7.528241,-9.715869,7.649195,-7.398451,-9.002509,-4.121340,3.238270,6.966557,9.986797,9.941502,9.804207,4.918737,-6.177466,-8.905014,4.191866,1.273494,-6.061254,9.581778,-1.147362,-6.807802,5.331541,-6.169399,-6.316476,2.293608,2.076171,3.313577,-2.103131,-9.698098,2.837285,-9.720484,-9.703446,-7.649604,-0.018962,-0.577285,0.668835,4.289694,8.021312,4.399529,8.815661,-6.208086,5.643119,1.076800,-4.868996,4.332889,6.005576,3.093723,1.962381,-2.029309,1.959041,-7.920078,2.891524,-7.885198,-2.888205,9.945913,-0.477055,-6.340783,8.889115,-3.355029,9.470693,9.922045,3.277288,-8.344821,-9.022325,-9.420085,5.976379,9.898750,-6.756270,-1.560495,5.662027,9.044423,9.694616,-3.596455,1.748199,-3.899485,-9.588332,2.640968,-7.364789,-1.684593,-9.446005,8.748506,3.808512,9.038195,-5.899188,-4.406477,9.560964,9.341443,5.151518,8.170731,-6.238922,-2.885108,9.124071,6.178619,6.402303,-1.990557,-1.459371,-9.995429,-7.250078,-5.084125,7.805296,3.356286,-5.641438,9.859173,-3.377757,-6.071989,-0.729614,0.051340,4.564017,-8.163602,-9.786751,-1.242075,-9.265923,-1.764618,-9.243899,5.012239,-9.188444,-1.091412,2.589010,-7.824259,-3.317494,3.482530,0.827635,-3.794223,0.404173,-6.790623,-5.136942,-8.415884,5.751219,5.829656,9.809295,0.439528,5.956138,-7.014794,4.646522,-1.059903,-1.374561,-5.135503,-1.422428,-5.275486,5.436734,7.059348,6.478620,-5.394957,7.643615,2.340468,-1.655979,-2.470795,-7.029653,6.916649,8.496031,-0.242289,3.640393,-0.937468,7.716604,1.906159,2.575416,-5.555845,-6.523283,9.884623,4.609072,5.876976,3.091093,5.669700,-2.129378,6.606713,5.190727,9.509040,-4.454307,-6.843591,-5.364966,6.197766,3.814393,5.557124,-4.480326,6.805393,3.388270,-0.992801,-6.320362,-1.161614,-1.616069,-3.247685,2.936920,-0.080101,0.127900,-3.297375,-1.626349,5.182073,7.606594,7.071657,0.291890,6.151826,8.706263,2.384072,-0.588099,4.811913,2.473824,-3.178107,4.880461,0.252740,0.551421,2.154494,4.727839,3.644581,6.920484,-3.947112,9.723661,0.144251,1.350846,-7.731285,-3.264260,-6.285254,-5.173767,3.202162,5.353253,-2.390939,-8.919470,-4.352131,5.595477,-5.558212,2.962369,5.950185,3.503124,5.081113,-2.041331,-6.718135,1.841699,-9.042245,6.507682,-6.155617,-2.387821,1.656762,-4.262044,-4.698126,-2.380927,-7.403223,-3.697159,-7.413655,-1.374825,-4.934041,-1.629479,2.161679,-5.723708,4.476643,9.402311,-2.387129,-9.416717,-7.248601,-9.535233,-9.847211,-4.606277,-4.937629,4.330562,-1.846005,-4.085583,-0.251190,3.840800,4.303615,2.547186,2.004321,-4.899162,7.774378,3.567855,6.720552,-0.657902,-4.087625,-0.009174,8.201528,-8.136919,4.937864,8.001342,1.501645,9.357547,-2.149551,1.526205,-3.842108,4.263087,-9.035630,5.217403,-4.350452,-0.922775,-8.927030,1.459617,-4.854734,7.344935,8.847350,2.159574,3.624351,4.004785,1.571204,6.945036,-5.266347,9.181974,-7.321656,-9.493219,2.302406,5.615496,1.770526,8.321192,-4.596781,1.928524,1.911766,-2.254116,5.497633,-2.276273,-8.956753,-0.922470,1.914520,-8.084541,4.119723,-8.847043,2.624488,-1.511156,4.888630,-3.169436,9.007096,1.505409,-5.792175,4.449336,9.537263,-8.110529,-8.231136,-1.769992,5.053803,6.347973,1.037407,0.575819,9.408636,4.379945,5.091460,8.816250,2.313154,-2.139044,-0.311014,9.429028,7.689647,-1.515059,2.008804,1.811162,1.055602,7.098937,8.413395,4.149795,-3.691544,3.868820,-7.589217,-4.319492,9.121087,2.384251,8.977826,1.021500,-6.769424,-9.353155,-5.776422,-3.268347,-5.269774,-3.594660,-3.045238,-1.815969,-8.990015,8.376249,-9.380761,-4.244775,-2.860320,-5.438454,-5.397794,-6.337750,1.908871,-2.409412,9.909833,4.950016,-6.183573,5.516217,2.344436,-0.799427,5.736165,-7.123134,6.284948,3.029714,-8.761727,6.703642,1.865395,3.287775,-9.063381,-0.024592,2.745095,0.425136,0.636368,-8.140729,0.193507,-2.146141,-3.181651,-9.971222,6.859395,4.082393,3.835505,-8.043113,2.738771,5.949260,-5.398758,4.057089,6.336400,5.589058,5.792005,2.855163,-7.478855,3.633034,-2.337449,2.173659,6.864432,6.259642,6.453322,1.942388,-8.995520,5.008046,-3.484686,-4.739190,2.135334,-8.480495,3.724146,8.686941,0.433698,7.568414,7.907494,0.718344,8.526819,8.757283,-1.164375,9.800283,-0.429887,5.961752,9.363246,-3.685382,-7.427255,3.855476,8.528053,6.710249,3.738922,-7.815480,8.844533,2.459791,6.285420,-9.345686,4.366206,-9.323394,-3.398225,-6.975697,0.644056,-3.377268,1.362191,9.049505,7.791938,0.937572,7.831438,7.402310,9.473605,-1.030151,4.327482,1.424498,-6.120032,-6.272114,3.870712,0.800048,-3.655990,-3.860321,9.701253,-9.705855,6.136045,-8.098570,9.858497,9.591100,-0.744572,1.625382,-7.115375,2.835342,-3.493096,8.502657,-9.578811,-6.039686,4.790676,5.059027,2.129572,3.203895,5.975322,7.889155,0.873940,-4.701122,-0.018173,8.819373,-3.366941,-3.594582,0.556733,-0.628323,-3.334304,-1.017065,-6.415301,-3.633586,6.516224,-3.639418,6.162730,2.858175,-1.613669,6.845151,-6.596766,-0.015705,8.677152,5.690719,-1.776193,-3.659341,5.701849,-4.649102,-6.094451,0.384960,-3.889053,7.361175,6.329920,-8.439948,-5.377940,0.055298,0.276003,4.273255,-9.150301,7.763338,-8.265229,6.715036,-2.934236,0.632784,-9.043256,-1.634263,-8.593287,7.714033,-2.424094,-5.387230,9.522526,5.418152,0.944720,7.401330,-7.512637,-5.894277,-0.691182,-2.639278,-2.979494,-9.261789,-3.412079,2.184895,-2.006246,-4.874111,6.211419,6.980329,-5.362987,0.367709,7.974720,9.567955,2.585212,-5.235652,7.781564,-8.999906,8.595073,1.889613,0.313443,-6.206672,1.629796,-3.693859,0.072211,4.774554,9.643508,2.996777,0.631817,-0.529435,8.136061,-9.395516,6.236120,-5.737461,5.852142,-8.886365,-5.290066,-7.523316,8.760548,-8.236255,-2.959000,1.714243,-8.502709,-9.644637,1.568025,-5.438704,-1.525265,-2.289045,5.534110,-0.495490,-8.539545,0.929027,1.569214,-7.593343,4.855503,-1.541999,-6.584960,4.552128,-0.084763,-2.538295,-5.327793,-4.744160,9.436802,-8.396927,9.220125,-4.791716,5.980156,3.023408,7.567272,9.774980,-9.569873,9.084050,4.259991,-9.700071,-9.652279,-2.560488,3.265447,2.297454,8.096778,-4.277615,-8.878383,-1.696622,-4.420968,1.831762,8.192616,-8.449197,-5.483456,-5.028425,-6.966566,0.709195,1.943844,0.089411,9.209124,3.426081,-4.069413,0.031754,-7.334557,-3.264520,1.407750,6.910258,1.339085,7.534460,2.516014,4.412445,-0.067774,-3.104799,-5.971318,-3.493877,6.292723,-5.783313,8.631357,-0.395936,1.326934,7.775541,-3.887202,2.048962,-7.110852,6.871094,-3.237630,-7.726768,-2.825681,-8.682094,-7.094750,-9.608803,0.926668,-7.416005,-9.054490,-9.886692,7.288969,9.636573,-5.029326,9.902964,8.470297,-8.896349,-9.483321,-2.274269,-7.038113,5.759131,4.086178,-3.721760,3.242318,-7.034442,5.308165,1.639952,-7.111656,1.978281,-6.165066,7.089633,6.856297,9.983168,-7.746904,-9.707821,7.774278,-2.465844,9.402909,9.080632,0.251680,4.458628,-4.683800,7.912323,4.813535,-8.045613,-5.198095,4.775404,6.449340,8.070939,-3.773167,-1.448665,6.613024,-5.653798,1.745587,3.770382,9.956978,-3.940415,-8.132286,-6.962200,-3.146485,2.109055,2.661811,-0.313531,2.117518,-2.501835,-7.368635,2.236035,1.936993,-9.031255,9.626469,6.900784,-5.318526,8.052399,-1.665748,-5.225177,-5.641471,5.566051,-5.272893,-3.406508,5.621082,4.210218,-5.567894,1.888097,6.180184,-4.379355,-4.343097,7.161169,7.272983,2.760433,1.088737,-5.404161,3.236497,5.521460,-9.801790,6.039310,-2.974452,2.814753,-9.312902,4.260687,-7.297913,-4.458557,6.389146,-7.928001,-3.920142,-5.560273,9.386059,1.144770,-6.785604,4.232415,6.170209,-4.223030,5.747951,-1.648110,0.456096,6.442118,2.415859,-7.476046,-7.490923,-5.268236,-8.378157,-5.120000,6.878374,-5.559349,-2.531617,-7.001601,-0.499843,9.358110,-4.726270,5.515313,4.500131,-7.028945,5.790272,-0.418003,5.344818,-5.777001,2.092350,6.775557,4.994568,1.130039,1.588784,0.517670,-1.926910,-2.174323,-3.864603,-8.598301,-7.706819,-9.947156,9.222218,1.072195,6.073989,-4.927662,-5.465545,-5.615459,8.037804,6.028451,9.637235,4.245997,-3.681365,5.875236,9.117281,-6.902384,-1.867254,5.937172,5.377906,-3.895046,8.045629,-8.239645,-8.832512,0.325860,-6.100799,8.962851,3.610127,5.383792,-2.033667,-3.945345,9.659678,1.328413,4.213349,6.507865,-3.411685,-7.169856,4.315397,8.663005,7.994302,9.321801,-2.468197,3.917143,4.794115,0.027341,3.768421,-1.004242,-2.667513,-5.830670,-3.799713,0.935416,0.424245,-5.160841,-8.256735,0.997062,-3.745602,2.320739,1.624042,-5.709188,7.243738,-5.688989,2.579054,0.034979,-3.368982,-0.707546,-3.857954,9.526179,5.850358,-4.236385,-5.874833,8.714904,-4.137913,3.434858,6.736623,0.708581,3.014036,-1.618493,-2.240102,-9.666430,1.146179,7.195050,-6.203487,-5.268701,6.768457,1.425262,-0.663311,-4.857457,4.313455,-4.764037,-5.229780,-7.160725,1.121302,-4.790477,-2.285173,-6.815884,7.176064,0.427755,0.848535,3.349037,-8.645062,-5.316899,1.867210,-8.161192,-8.681694,-0.293633,-2.408048,-1.926830,3.147918,9.822669,5.212291,3.421217,4.290276,7.524140,-3.232036,0.396240,9.359345,4.459965,2.301256,-9.993059,-5.657546,-8.819156,0.765647,-0.592045,1.417166,-3.991411,-5.750166,-4.638268,5.369104,-3.760256,-6.788687,-5.416140,7.004220,9.832822,7.911585,-8.105684,-5.196681,-5.454873,3.056024,-8.361197,-5.236672,0.725740,-6.250309,0.803847,7.575807,-6.907576,1.970003,-9.097253,-1.841979,0.609967,2.925180,-5.522766,-5.976919,6.384150,0.552849,3.929106,-4.495794,-2.600893,-7.891140,-9.051626,7.230908,8.316744,-9.108682,0.457473,8.024387,-6.712849,-5.900074,-3.501253,-3.406900,-2.254020,4.595159,5.088345,5.271543,5.517406,7.755225,3.424796,-5.670548,-9.652351,-0.737849,5.639331,-8.688951,-2.646548,-5.995482,-4.166660,-8.766593,8.063968,-3.398215,-8.941723,-5.327119,4.061341,3.775889,0.589330,6.097768,-8.157424,2.103242,-7.977530,-9.048042,8.769877,4.005063,5.792571,-1.315084,-5.486712,2.088624,-5.767191,-6.490909,-4.305250,2.827933,7.931525,9.906145], dtype = "float32")#candidate|10523|(3600,)|const|float32
var_10524 = relay.var("var_10524", dtype = "int8", shape = (450,))#candidate|10524|(450,)|var|int8
call_10522 = relay.TupleGetItem(func_8199_call(relay.reshape(const_10523.astype('float32'), [20, 180]), relay.reshape(var_10524.astype('int8'), [5, 90]), ), 7)
call_10525 = relay.TupleGetItem(func_8203_call(relay.reshape(const_10523.astype('float32'), [20, 180]), relay.reshape(var_10524.astype('int8'), [5, 90]), ), 7)
uop_10527 = relay.acosh(uop_10508.astype('float64')) # shape=(12, 9, 12)
output = relay.Tuple([call_10512,call_10520,call_10522,const_10523,var_10524,uop_10527,])
output2 = relay.Tuple([call_10513,call_10521,call_10525,const_10523,var_10524,uop_10527,])
func_10535 = relay.Function([var_10524,], output)
mod['func_10535'] = func_10535
mod = relay.transform.InferType()(mod)
mutated_mod['func_10535'] = func_10535
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10536 = relay.var("var_10536", dtype = "int8", shape = (450,))#candidate|10536|(450,)|var|int8
func_10535_call = mutated_mod.get_global_var('func_10535')
call_10537 = func_10535_call(var_10536)
output = call_10537
func_10538 = relay.Function([var_10536], output)
mutated_mod['func_10538'] = func_10538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2258_call = mod.get_global_var('func_2258')
func_2260_call = mutated_mod.get_global_var('func_2260')
call_10540 = relay.TupleGetItem(func_2258_call(), 0)
call_10541 = relay.TupleGetItem(func_2260_call(), 0)
func_3224_call = mod.get_global_var('func_3224')
func_3225_call = mutated_mod.get_global_var('func_3225')
call_10549 = relay.TupleGetItem(func_3224_call(), 0)
call_10550 = relay.TupleGetItem(func_3225_call(), 0)
output = relay.Tuple([call_10540,call_10549,])
output2 = relay.Tuple([call_10541,call_10550,])
func_10589 = relay.Function([], output)
mod['func_10589'] = func_10589
mod = relay.transform.InferType()(mod)
output = func_10589()
func_10590 = relay.Function([], output)
mutated_mod['func_10590'] = func_10590
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2731_call = mod.get_global_var('func_2731')
func_2732_call = mutated_mod.get_global_var('func_2732')
call_10600 = func_2731_call()
call_10601 = func_2731_call()
func_9279_call = mod.get_global_var('func_9279')
func_9283_call = mutated_mod.get_global_var('func_9283')
const_10622 = relay.const(-2, dtype = "int8")#candidate|10622|()|const|int8
const_10623 = relay.const([5,-6,8,-3], dtype = "int8")#candidate|10623|(4,)|const|int8
call_10621 = relay.TupleGetItem(func_9279_call(relay.reshape(const_10622.astype('int8'), []), relay.reshape(const_10623.astype('int8'), [2, 1, 2]), ), 0)
call_10624 = relay.TupleGetItem(func_9283_call(relay.reshape(const_10622.astype('int8'), []), relay.reshape(const_10623.astype('int8'), [2, 1, 2]), ), 0)
func_3084_call = mod.get_global_var('func_3084')
func_3086_call = mutated_mod.get_global_var('func_3086')
call_10626 = relay.TupleGetItem(func_3084_call(), 0)
call_10627 = relay.TupleGetItem(func_3086_call(), 0)
output = relay.Tuple([call_10600,call_10621,const_10622,const_10623,call_10626,])
output2 = relay.Tuple([call_10601,call_10624,const_10622,const_10623,call_10627,])
func_10629 = relay.Function([], output)
mod['func_10629'] = func_10629
mod = relay.transform.InferType()(mod)
output = func_10629()
func_10630 = relay.Function([], output)
mutated_mod['func_10630'] = func_10630
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1489_call = mod.get_global_var('func_1489')
func_1490_call = mutated_mod.get_global_var('func_1490')
call_10649 = relay.TupleGetItem(func_1489_call(), 0)
call_10650 = relay.TupleGetItem(func_1490_call(), 0)
output = call_10649
output2 = call_10650
func_10651 = relay.Function([], output)
mod['func_10651'] = func_10651
mod = relay.transform.InferType()(mod)
output = func_10651()
func_10652 = relay.Function([], output)
mutated_mod['func_10652'] = func_10652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_861_call = mod.get_global_var('func_861')
func_862_call = mutated_mod.get_global_var('func_862')
call_10691 = relay.TupleGetItem(func_861_call(), 0)
call_10692 = relay.TupleGetItem(func_862_call(), 0)
func_5885_call = mod.get_global_var('func_5885')
func_5887_call = mutated_mod.get_global_var('func_5887')
call_10698 = relay.TupleGetItem(func_5885_call(), 0)
call_10699 = relay.TupleGetItem(func_5887_call(), 0)
output = relay.Tuple([call_10691,call_10698,])
output2 = relay.Tuple([call_10692,call_10699,])
func_10707 = relay.Function([], output)
mod['func_10707'] = func_10707
mod = relay.transform.InferType()(mod)
output = func_10707()
func_10708 = relay.Function([], output)
mutated_mod['func_10708'] = func_10708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8617_call = mod.get_global_var('func_8617')
func_8618_call = mutated_mod.get_global_var('func_8618')
call_10747 = func_8617_call()
call_10748 = func_8617_call()
func_9653_call = mod.get_global_var('func_9653')
func_9654_call = mutated_mod.get_global_var('func_9654')
call_10749 = relay.TupleGetItem(func_9653_call(), 0)
call_10750 = relay.TupleGetItem(func_9654_call(), 0)
bop_10752 = relay.logical_and(call_10747.astype('bool'), call_10749.astype('bool')) # shape=(2, 7, 225)
bop_10755 = relay.logical_and(call_10748.astype('bool'), call_10750.astype('bool')) # shape=(2, 7, 225)
bop_10759 = relay.floor_divide(bop_10752.astype('float32'), call_10747.astype('float32')) # shape=(2, 7, 225)
bop_10762 = relay.floor_divide(bop_10755.astype('float32'), call_10748.astype('float32')) # shape=(2, 7, 225)
func_10535_call = mod.get_global_var('func_10535')
func_10538_call = mutated_mod.get_global_var('func_10538')
const_10765 = relay.const([5,-7,3,-8,-4,-6,-2,3,-7,1,8,8,-2,1,4,-2,8,-10,9,-10,3,-8,-2,-7,9,2,9,-5,10,-10,-6,5,-4,-6,5,8,4,2,-6,7,-8,-5,3,-9,5,-7,-2,6,-7,8,10,7,3,2,-10,-5,1,5,-9,7,4,5,-6,1,-3,5,-7,9,-4,9,9,-2,3,4,-2,6,-5,-1,1,-6,10,-10,-6,9,10,-5,4,-1,5,-1,-6,-4,-7,2,6,4,9,-5,3,-6,1,-1,-1,4,-8,4,1,3,-4,7,4,5,5,8,-5,-8,8,-3,-4,6,9,3,9,-7,-4,-2,-6,-2,9,7,-8,2,6,6,10,1,-1,1,-4,-2,5,-7,-3,1,10,-7,5,-4,-5,-3,10,6,10,-1,8,-5,7,3,2,3,-2,-8,-2,-9,3,-3,8,4,7,-6,-9,7,4,10,-5,-8,5,-5,-10,-3,-8,6,6,-6,7,7,3,-6,5,3,-8,7,6,-8,8,-9,-8,2,7,6,-2,-4,8,-3,5,-4,-6,-6,-5,-9,8,9,5,1,-9,-9,-9,-7,-2,-3,-6,-10,10,-5,2,9,-3,7,10,-1,-2,-2,-3,1,7,2,1,-6,-10,9,6,-4,-6,1,9,-7,-2,4,-5,-1,-9,6,7,-4,-4,8,10,-10,-3,4,-3,-2,7,-10,-1,7,-4,-1,-4,5,-7,-9,-7,5,10,-1,-8,9,1,2,-8,3,1,-10,-8,-4,-2,-1,-1,-10,-6,5,-5,1,-2,9,1,4,7,-6,1,-1,-4,1,-9,-8,3,8,6,6,-2,9,-9,5,9,3,3,2,-6,-5,-7,9,4,7,-7,-1,-10,-4,5,6,-3,3,-3,-5,9,4,-1,-5,-2,-7,7,-10,8,9,3,5,-6,-2,-5,-8,5,10,6,-2,-8,-7,-7,-6,-1,8,10,-10,4,-3,-8,-3,4,-10,-9,-9,1,3,-1,3,-2,7,-4,8,10,-7,4,-5,1,9,8,-6,3,7,8,7,-8,-4,3,2,-3,4,-7,6,-4,10,4,-3,7,1,1,-5,-2,3,9,1,-4,-1,-5,3,-3,-5,8,2,-9,1,10,-1,5,2,-9,9,-9,8,-7,-5,-1,5,-8,7,1,9,3,6,4,-3,-8,-8,-3,2,7,-8,10,10,-4,7], dtype = "int8")#candidate|10765|(450,)|const|int8
call_10764 = relay.TupleGetItem(func_10535_call(relay.reshape(const_10765.astype('int8'), [450,])), 0)
call_10766 = relay.TupleGetItem(func_10538_call(relay.reshape(const_10765.astype('int8'), [450,])), 0)
output = relay.Tuple([bop_10759,call_10764,const_10765,])
output2 = relay.Tuple([bop_10762,call_10766,const_10765,])
func_10767 = relay.Function([], output)
mod['func_10767'] = func_10767
mod = relay.transform.InferType()(mod)
output = func_10767()
func_10768 = relay.Function([], output)
mutated_mod['func_10768'] = func_10768
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3781_call = mod.get_global_var('func_3781')
func_3782_call = mutated_mod.get_global_var('func_3782')
call_10773 = func_3781_call()
call_10774 = func_3781_call()
func_1171_call = mod.get_global_var('func_1171')
func_1173_call = mutated_mod.get_global_var('func_1173')
call_10775 = relay.TupleGetItem(func_1171_call(), 1)
call_10776 = relay.TupleGetItem(func_1173_call(), 1)
output = relay.Tuple([call_10773,call_10775,])
output2 = relay.Tuple([call_10774,call_10776,])
func_10790 = relay.Function([], output)
mod['func_10790'] = func_10790
mod = relay.transform.InferType()(mod)
mutated_mod['func_10790'] = func_10790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10790_call = mutated_mod.get_global_var('func_10790')
call_10791 = func_10790_call()
output = call_10791
func_10792 = relay.Function([], output)
mutated_mod['func_10792'] = func_10792
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10831 = relay.var("var_10831", dtype = "float64", shape = (7, 5, 16))#candidate|10831|(7, 5, 16)|var|float64
uop_10832 = relay.sinh(var_10831.astype('float64')) # shape=(7, 5, 16)
func_4188_call = mod.get_global_var('func_4188')
func_4189_call = mutated_mod.get_global_var('func_4189')
call_10836 = relay.TupleGetItem(func_4188_call(), 0)
call_10837 = relay.TupleGetItem(func_4189_call(), 0)
output = relay.Tuple([uop_10832,call_10836,])
output2 = relay.Tuple([uop_10832,call_10837,])
func_10839 = relay.Function([var_10831,], output)
mod['func_10839'] = func_10839
mod = relay.transform.InferType()(mod)
mutated_mod['func_10839'] = func_10839
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10840 = relay.var("var_10840", dtype = "float64", shape = (7, 5, 16))#candidate|10840|(7, 5, 16)|var|float64
func_10839_call = mutated_mod.get_global_var('func_10839')
call_10841 = func_10839_call(var_10840)
output = call_10841
func_10842 = relay.Function([var_10840], output)
mutated_mod['func_10842'] = func_10842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1190_call = mod.get_global_var('func_1190')
func_1191_call = mutated_mod.get_global_var('func_1191')
call_10855 = func_1190_call()
call_10856 = func_1190_call()
func_7081_call = mod.get_global_var('func_7081')
func_7083_call = mutated_mod.get_global_var('func_7083')
call_10869 = relay.TupleGetItem(func_7081_call(), 2)
call_10870 = relay.TupleGetItem(func_7083_call(), 2)
func_10010_call = mod.get_global_var('func_10010')
func_10015_call = mutated_mod.get_global_var('func_10015')
const_10873 = relay.const([-1,5,-5,-2,-6,7,10,6,-8,-2,7,-10,-9,8,-2,-4,5,9,-6,10,4,3,7,-7,-8,9,-4,-8,5,3,-8,-2,-10,-6,6,8], dtype = "int64")#candidate|10873|(36,)|const|int64
const_10874 = relay.const([9.325775,1.913747,9.883171,4.837728,-7.424303,3.470231,1.133011,-4.179997,-7.805960,1.184147,7.627041,-2.278112,5.651598,9.112485,-6.615337,3.653651,-3.496513,6.582818,0.932765,6.504940,5.667627,-7.525465,-6.566982,-6.477931,3.817431,6.144356,9.033470,7.731823,1.150648,7.355135,2.871097,-6.902446,9.654972,-2.143936,-4.977611,2.572530,-8.431636,-8.985692,-9.585275,9.124713,-9.242910,8.247592,-0.092744,3.475269,0.650222,8.462650,9.287412,2.001185,-2.504071,1.640932,9.573982,-7.998693,5.263072,7.908277,6.424545,0.675949,3.303443,9.749158,-3.339403,5.534045,-2.544603,-4.084307,-2.718769,-3.433562,5.773969,5.890348,-3.111092,-8.841075,1.986676,-1.620468,2.789699,-9.975135,-0.065208,-1.690512,-9.707811,-3.906403,0.176463,7.190159,-8.143389,-2.844567,1.300401,3.593191,0.334483,2.194176,3.362338,7.575232,-0.111385,4.312678,2.269150,8.527235,5.911459,-5.797164,-1.562307,0.535696,-9.757522,8.056581,2.511211,6.102172,-9.771106,2.789546,-7.369142,-7.644218,0.696425,5.465555,-0.409565,-6.497149,7.757150,-7.118301,-2.658829,-3.268912,2.499499,6.409150,-8.808257,2.244364,8.891524,-9.998775,9.973177,-2.715483,-6.122857,1.666249,-2.508885,9.454952,8.940463,-0.376383,1.718213,-4.849393,-3.657327,0.870048,-1.104137,0.368891,-6.215515,-0.884762,1.859038,-1.603194,-3.488630,-7.474842,5.412736,-8.229095,9.932480,0.848828], dtype = "float32")#candidate|10874|(140,)|const|float32
call_10872 = relay.TupleGetItem(func_10010_call(relay.reshape(const_10873.astype('int64'), [2, 3, 6]), relay.reshape(const_10873.astype('int64'), [2, 3, 6]), relay.reshape(const_10874.astype('float32'), [140,]), ), 1)
call_10875 = relay.TupleGetItem(func_10015_call(relay.reshape(const_10873.astype('int64'), [2, 3, 6]), relay.reshape(const_10873.astype('int64'), [2, 3, 6]), relay.reshape(const_10874.astype('float32'), [140,]), ), 1)
output = relay.Tuple([call_10855,call_10869,call_10872,const_10873,const_10874,])
output2 = relay.Tuple([call_10856,call_10870,call_10875,const_10873,const_10874,])
func_10879 = relay.Function([], output)
mod['func_10879'] = func_10879
mod = relay.transform.InferType()(mod)
mutated_mod['func_10879'] = func_10879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10879_call = mutated_mod.get_global_var('func_10879')
call_10880 = func_10879_call()
output = call_10880
func_10881 = relay.Function([], output)
mutated_mod['func_10881'] = func_10881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3291_call = mod.get_global_var('func_3291')
func_3293_call = mutated_mod.get_global_var('func_3293')
call_10904 = func_3291_call()
call_10905 = func_3291_call()
func_3224_call = mod.get_global_var('func_3224')
func_3225_call = mutated_mod.get_global_var('func_3225')
call_10920 = relay.TupleGetItem(func_3224_call(), 0)
call_10921 = relay.TupleGetItem(func_3225_call(), 0)
output = relay.Tuple([call_10904,call_10920,])
output2 = relay.Tuple([call_10905,call_10921,])
func_10944 = relay.Function([], output)
mod['func_10944'] = func_10944
mod = relay.transform.InferType()(mod)
mutated_mod['func_10944'] = func_10944
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10944_call = mutated_mod.get_global_var('func_10944')
call_10945 = func_10944_call()
output = call_10945
func_10946 = relay.Function([], output)
mutated_mod['func_10946'] = func_10946
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11019 = relay.var("var_11019", dtype = "int32", shape = (9, 6, 12))#candidate|11019|(9, 6, 12)|var|int32
var_11020 = relay.var("var_11020", dtype = "int32", shape = (9, 6, 12))#candidate|11020|(9, 6, 12)|var|int32
bop_11021 = relay.minimum(var_11019.astype('int32'), relay.reshape(var_11020.astype('int32'), relay.shape_of(var_11019))) # shape=(9, 6, 12)
output = bop_11021
output2 = bop_11021
func_11028 = relay.Function([var_11019,var_11020,], output)
mod['func_11028'] = func_11028
mod = relay.transform.InferType()(mod)
mutated_mod['func_11028'] = func_11028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11028_call = mutated_mod.get_global_var('func_11028')
var_11030 = relay.var("var_11030", dtype = "int32", shape = (9, 6, 12))#candidate|11030|(9, 6, 12)|var|int32
var_11031 = relay.var("var_11031", dtype = "int32", shape = (9, 6, 12))#candidate|11031|(9, 6, 12)|var|int32
call_11029 = func_11028_call(var_11030,var_11031,)
output = call_11029
func_11032 = relay.Function([var_11030,var_11031,], output)
mutated_mod['func_11032'] = func_11032
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2563_call = mod.get_global_var('func_2563')
func_2564_call = mutated_mod.get_global_var('func_2564')
call_11071 = relay.TupleGetItem(func_2563_call(), 0)
call_11072 = relay.TupleGetItem(func_2564_call(), 0)
func_7823_call = mod.get_global_var('func_7823')
func_7826_call = mutated_mod.get_global_var('func_7826')
const_11099 = relay.const([-9.373103,-0.321767,0.802437,3.498262,7.855993,8.262526,3.759921,-5.618868,7.105628,-1.184012,5.780697,4.827038,-1.931246,-6.646343,-3.215466,0.243423,-7.124722,-5.792305,-9.781438,0.822342,5.757099,-1.588638,1.105420,3.465906,1.070231,8.308033,6.592631,9.770055,7.282685,9.479740,-1.115618,-4.119468,1.580188,-7.728932,-1.138682,8.260878,-8.266365,-9.215115,-6.193792,-2.518158,-0.948897,-8.625530,-7.404460,3.001399,5.807323,-7.706149,6.608766,-7.081157,9.778547,-9.962346,1.802204,9.075382,8.498526,5.778838,5.827186,6.384593,8.280920,3.538417,7.227750,8.300948,7.272990,-2.331705,-2.724619,5.806195,-5.047617,7.730622,4.232986,4.227883,0.810119,-5.171311,0.291048,-7.263190,1.415213,-8.190773,-3.408399,-7.136616,3.885114,-9.857584,4.566032,2.490658,5.515679,8.713278,9.462820,1.894688,-4.771226,3.568379,4.581629,-6.655165,7.878103,-5.748992,0.349162,-5.896497,2.100053,-5.561302,-5.218931,-6.188682,9.854963,0.017464,7.036253,7.490229,-5.002186,2.607912,-7.104779,6.405909,-2.309765,2.618066,-5.724329,0.066480,-4.397488,-2.700765,2.375996,-1.656077,2.542298,-1.762618,-7.385361,-1.132795,-6.464222,-4.662178,6.890980,3.801980,5.751911,2.069626,-7.483995,-3.663628,4.927552,3.733170,4.556043,0.710691,3.120017,0.173044,6.212540,6.152631], dtype = "float64")#candidate|11099|(132,)|const|float64
call_11098 = relay.TupleGetItem(func_7823_call(relay.reshape(const_11099.astype('float64'), [6, 11, 2])), 0)
call_11100 = relay.TupleGetItem(func_7826_call(relay.reshape(const_11099.astype('float64'), [6, 11, 2])), 0)
func_5885_call = mod.get_global_var('func_5885')
func_5887_call = mutated_mod.get_global_var('func_5887')
call_11117 = relay.TupleGetItem(func_5885_call(), 0)
call_11118 = relay.TupleGetItem(func_5887_call(), 0)
bop_11130 = relay.power(call_11071.astype('float32'), relay.reshape(call_11117.astype('float32'), relay.shape_of(call_11071))) # shape=(2, 7, 1)
bop_11133 = relay.power(call_11072.astype('float32'), relay.reshape(call_11118.astype('float32'), relay.shape_of(call_11072))) # shape=(2, 7, 1)
func_2272_call = mod.get_global_var('func_2272')
func_2274_call = mutated_mod.get_global_var('func_2274')
call_11139 = relay.TupleGetItem(func_2272_call(), 0)
call_11140 = relay.TupleGetItem(func_2274_call(), 0)
output = relay.Tuple([call_11098,const_11099,bop_11130,call_11139,])
output2 = relay.Tuple([call_11100,const_11099,bop_11133,call_11140,])
func_11146 = relay.Function([], output)
mod['func_11146'] = func_11146
mod = relay.transform.InferType()(mod)
output = func_11146()
func_11147 = relay.Function([], output)
mutated_mod['func_11147'] = func_11147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7081_call = mod.get_global_var('func_7081')
func_7083_call = mutated_mod.get_global_var('func_7083')
call_11170 = relay.TupleGetItem(func_7081_call(), 2)
call_11171 = relay.TupleGetItem(func_7083_call(), 2)
output = relay.Tuple([call_11170,])
output2 = relay.Tuple([call_11171,])
func_11200 = relay.Function([], output)
mod['func_11200'] = func_11200
mod = relay.transform.InferType()(mod)
output = func_11200()
func_11201 = relay.Function([], output)
mutated_mod['func_11201'] = func_11201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1691_call = mod.get_global_var('func_1691')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_11257 = relay.TupleGetItem(func_1691_call(), 0)
call_11258 = relay.TupleGetItem(func_1693_call(), 0)
output = call_11257
output2 = call_11258
func_11263 = relay.Function([], output)
mod['func_11263'] = func_11263
mod = relay.transform.InferType()(mod)
mutated_mod['func_11263'] = func_11263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11263_call = mutated_mod.get_global_var('func_11263')
call_11264 = func_11263_call()
output = call_11264
func_11265 = relay.Function([], output)
mutated_mod['func_11265'] = func_11265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8354_call = mod.get_global_var('func_8354')
func_8355_call = mutated_mod.get_global_var('func_8355')
call_11276 = func_8354_call()
call_11277 = func_8354_call()
func_1324_call = mod.get_global_var('func_1324')
func_1325_call = mutated_mod.get_global_var('func_1325')
call_11278 = relay.TupleGetItem(func_1324_call(), 0)
call_11279 = relay.TupleGetItem(func_1325_call(), 0)
output = relay.Tuple([call_11276,call_11278,])
output2 = relay.Tuple([call_11277,call_11279,])
func_11295 = relay.Function([], output)
mod['func_11295'] = func_11295
mod = relay.transform.InferType()(mod)
output = func_11295()
func_11296 = relay.Function([], output)
mutated_mod['func_11296'] = func_11296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10767_call = mod.get_global_var('func_10767')
func_10768_call = mutated_mod.get_global_var('func_10768')
call_11322 = relay.TupleGetItem(func_10767_call(), 1)
call_11323 = relay.TupleGetItem(func_10768_call(), 1)
func_2011_call = mod.get_global_var('func_2011')
func_2014_call = mutated_mod.get_global_var('func_2014')
var_11328 = relay.var("var_11328", dtype = "float32", shape = (210,))#candidate|11328|(210,)|var|float32
call_11327 = relay.TupleGetItem(func_2011_call(relay.reshape(var_11328.astype('float32'), [2, 7, 15])), 0)
call_11329 = relay.TupleGetItem(func_2014_call(relay.reshape(var_11328.astype('float32'), [2, 7, 15])), 0)
output = relay.Tuple([call_11322,call_11327,var_11328,])
output2 = relay.Tuple([call_11323,call_11329,var_11328,])
func_11339 = relay.Function([var_11328,], output)
mod['func_11339'] = func_11339
mod = relay.transform.InferType()(mod)
var_11340 = relay.var("var_11340", dtype = "float32", shape = (210,))#candidate|11340|(210,)|var|float32
output = func_11339(var_11340)
func_11341 = relay.Function([var_11340], output)
mutated_mod['func_11341'] = func_11341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1691_call = mod.get_global_var('func_1691')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_11359 = relay.TupleGetItem(func_1691_call(), 1)
call_11360 = relay.TupleGetItem(func_1693_call(), 1)
output = relay.Tuple([call_11359,])
output2 = relay.Tuple([call_11360,])
func_11367 = relay.Function([], output)
mod['func_11367'] = func_11367
mod = relay.transform.InferType()(mod)
output = func_11367()
func_11368 = relay.Function([], output)
mutated_mod['func_11368'] = func_11368
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4454_call = mod.get_global_var('func_4454')
func_4455_call = mutated_mod.get_global_var('func_4455')
call_11378 = func_4454_call()
call_11379 = func_4454_call()
func_1489_call = mod.get_global_var('func_1489')
func_1490_call = mutated_mod.get_global_var('func_1490')
call_11393 = relay.TupleGetItem(func_1489_call(), 0)
call_11394 = relay.TupleGetItem(func_1490_call(), 0)
output = relay.Tuple([call_11378,call_11393,])
output2 = relay.Tuple([call_11379,call_11394,])
func_11397 = relay.Function([], output)
mod['func_11397'] = func_11397
mod = relay.transform.InferType()(mod)
output = func_11397()
func_11398 = relay.Function([], output)
mutated_mod['func_11398'] = func_11398
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11437 = relay.var("var_11437", dtype = "float64", shape = (15, 7, 4))#candidate|11437|(15, 7, 4)|var|float64
uop_11438 = relay.exp(var_11437.astype('float64')) # shape=(15, 7, 4)
output = uop_11438
output2 = uop_11438
func_11440 = relay.Function([var_11437,], output)
mod['func_11440'] = func_11440
mod = relay.transform.InferType()(mod)
var_11441 = relay.var("var_11441", dtype = "float64", shape = (15, 7, 4))#candidate|11441|(15, 7, 4)|var|float64
output = func_11440(var_11441)
func_11442 = relay.Function([var_11441], output)
mutated_mod['func_11442'] = func_11442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5031_call = mod.get_global_var('func_5031')
func_5032_call = mutated_mod.get_global_var('func_5032')
call_11446 = func_5031_call()
call_11447 = func_5031_call()
output = call_11446
output2 = call_11447
func_11449 = relay.Function([], output)
mod['func_11449'] = func_11449
mod = relay.transform.InferType()(mod)
output = func_11449()
func_11450 = relay.Function([], output)
mutated_mod['func_11450'] = func_11450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6694_call = mod.get_global_var('func_6694')
func_6695_call = mutated_mod.get_global_var('func_6695')
call_11481 = relay.TupleGetItem(func_6694_call(), 0)
call_11482 = relay.TupleGetItem(func_6695_call(), 0)
func_6549_call = mod.get_global_var('func_6549')
func_6552_call = mutated_mod.get_global_var('func_6552')
const_11488 = relay.const([9.863815,4.198392,-2.747815,5.196139,-8.510792,1.133150,-8.339180,-1.201694,4.161338,-1.386186,-0.776008,-2.959107,1.353838,-4.710638,8.397976,-0.919429,-5.501885,9.522563,6.475234,-3.690613,5.270045,2.882758,-8.481018,0.187895,9.360965,4.305985,-3.056175,8.775503,-0.718328,-3.792726,-4.793553,-9.175285,-7.724691,8.142173,-8.401960,8.510080,7.963705,6.612837,-4.694884,8.609976,-3.760184,7.006560,-7.562863,-0.429399,-5.992375,-6.269089,2.464855,1.453743,-2.726597,5.896012,7.063483,-7.910567,5.511222,-2.877674,-1.652605,1.781344,-4.764513,-2.212973,7.755579,6.340692,0.792915,-1.603662,-3.482133,4.837763,2.041004,8.803070,4.593037,7.865582,5.160691,1.236146,-3.387011,-1.962360,6.571374,7.077121,3.862569,0.599257,1.120387,9.456246,8.683927,-0.919371,7.364124,5.945306,-5.452907,-3.417848,-4.034027,3.333421,-3.667328,7.935846,-4.680159,8.518387,4.642282,2.178566,-0.847562,-9.923862,4.920658,-5.017311,-2.076057,0.829197,7.876588,-6.095170,7.920438,-7.152153,8.327503,-5.102845,-4.208047,0.254769,-2.762275,-6.433082,5.419261,-3.358408,-7.246434,-9.708008,4.209406,1.825999,3.995336,-0.721335,7.938826,-3.467633,8.231332,2.170743,-8.507195,4.966622,9.356349,-2.762488,1.965514,5.292217,6.988270,-9.524398,8.685219,7.132300,-6.271895,-6.429376,-6.959366,-5.943478,9.344103,-9.707150,4.608075,-6.270480,6.408828,7.606969,5.065688,-0.397134,-1.367413,8.442402,-3.154535,-2.451936,3.528927,5.071005,-9.116031,5.253590,4.896918,8.509173,9.752435,0.111271,-3.143696,1.329331,7.104883,6.347343,4.776882,5.277878,0.875213,-3.693051,-5.793106,6.672743,1.055337,-0.465665,-8.773097,0.169009,2.479790,-2.356621,-3.636185,-2.864337,-8.133597,1.251765,-5.926986,1.405772,7.814306,-8.932144,2.141484,-0.777643,-2.320283,2.709880,-9.880719,3.107308,5.986548,-8.883646,9.420160,0.562461,-4.319705,1.486793,-3.483069,-8.455073,-7.488398,7.526590,-5.773004,6.536509,5.532442,4.015275,5.197811,1.839700,9.563018,-4.832068,-4.318932,-7.395206,3.816015,-3.278103,-0.204414,2.937136,5.235551,7.990473,-4.785365,9.928259,7.425993,3.418877,4.049465,-1.672173,-8.953561,2.534965,-0.296934,7.963120,-6.754410,2.876617,9.390110,4.698284,-4.865103,-2.940531,6.088022,-1.090798,7.399037,-6.831865,-4.517206,0.223718,6.618004,-8.131578,-6.138889,3.328668,5.043759,4.296569,0.281930,0.029822,5.103389,-5.153579,6.280173,-7.691491,5.096555,0.038027,5.143307,-0.504014,-8.185379,-8.942084,7.197968,3.027868,6.759280,3.848873,7.354221,-8.223928,-6.249095,-0.995810,0.175592,-5.385636,6.287832,-0.317872,-7.936959,7.049267,6.290324,9.947601,-8.104261,0.864694,-1.196483,-0.770990,-1.500595,-6.991792,-8.131810,-6.671666,2.537760,-8.558639,2.163701,9.442557,6.918554,-5.247587,9.215108,2.026041,-6.047898,5.487462,1.505486,-2.822419,-8.392810,7.061261,9.972049,-9.534112,-0.969094,2.391134,2.129593,-3.067532,-0.557998,-7.439566,-7.417449,6.684551,-8.077259,6.349472,-9.573149,4.780394,6.914613,3.257616,9.657335,1.713270,-0.043941,4.553981,-3.058459,8.668523,-7.180517,-6.655269,2.585110,7.022878,-1.097441,-0.128537,-2.904421,7.145523,-4.028546,9.302983,-1.793505,9.910778,8.758070,-9.516335,-9.908660,-4.960948,9.399497,-6.089571,-5.625345,1.829697,-5.093785,-1.758778,8.075403,-7.261297,-9.886118,3.881891,1.569838,-5.314933,6.633191,-9.903938,-1.547240,-9.705869,1.406337,-1.500544,-9.518078,-7.632881,3.819761,-5.737435,-1.707027,-6.628005,-7.256455,8.657226,0.684045,-5.682135,-3.245384,-4.187287,-1.943759,5.132990,4.517932,3.710407,3.377555,9.682333,-1.432207,8.920814,-7.282192,-5.434244,-6.271456,-5.664209,9.012771,-1.190005,0.292194,-9.418271,-4.238107,1.473362,9.600677,8.788021,-5.204810,-4.227642,-4.734280,7.531981,5.624245,6.250662,0.645304,0.176608,0.007833,0.632648,9.271635,-7.134604,1.544767,4.824068,-0.962268,4.492023,5.767677,-9.636348,8.419341,0.828773,1.709416,-2.357968,-8.109895,8.088750,-7.977875,4.028461,-4.148689,1.769804,6.763522,-8.076053,9.652919,9.201827,8.678265,5.944650,5.010102,-6.565334,9.836491,-5.903000,-4.789308,3.586510,-1.817464,-1.340503,-8.181684,-5.574609,3.147402,-4.541315,-4.613311,1.940528,7.690547,-2.354081,9.835151,5.713574,-7.417072,3.181778,2.928486,7.792362,9.532157,-4.426837,2.600047,8.905444,2.976315,2.399427,3.084622,-1.012871,7.419795,-4.856679,2.959649,-9.623457,6.003986,-3.744014,-8.147528,-3.832445,-1.987543,-3.385122,7.210762,-7.465623,7.991598,-7.254475,-6.367172,6.102320,8.970971,9.282263,0.036207,-5.057819,3.663619,4.295588,-3.690575,4.699641,-5.985925,-4.941663,1.625144,-6.779733,9.947105,-2.203557,6.101223,5.694092,1.296895,7.004724,-2.375191,9.625702,4.597490,-5.801809,-6.023733,-4.640639,1.736636,-8.146365,4.388775,7.376020,5.846002,-6.112445,7.995777,1.700359,-4.275797,6.109724,4.465727,-3.246528,2.059085,-6.794572,-0.976639,-7.732592,-7.004275,5.018356,4.382669,-4.416847,-6.055983,-3.265748,-1.298779,-8.595738,-4.936116,-5.787649,-2.762290,-6.809871,2.011849,8.560170,7.419815,5.883069,-7.972024,9.597738,8.173992,-8.796409,2.932078,2.996408,-3.398548,-5.398676,4.945687,-8.625174,-7.121701,8.861840,-2.932771,1.880679,-8.602640,8.516037,7.985258,-3.228389,-3.337606,-0.832497,3.999468,3.314198,4.916279,7.241180,-4.505728,-5.894121,-7.604736,-0.745154,-1.800691,7.019588,-1.029011,7.089891,9.952143,-0.399765,-1.335637,2.153093,-8.726809,-7.125092,8.216319,-9.374743,6.856823,-3.977471,-3.508832,-5.660864,-6.153538,4.996752,-4.964157,3.638157,4.923264,5.438234,-5.802704,4.660094,-8.395122,5.171847,8.668151,4.246663,-7.909578,6.530416,4.391096,-6.508268,7.982705,-9.686173,-6.558481,4.033543,-3.129167,-8.294027,-4.954411,7.832759,7.684211,-3.001346,9.475504,3.963723,2.423804,-2.469268,2.725433,-9.208007,8.390052,-4.023436,-7.431576,3.030635,3.154122,-1.529131,7.985719,-0.069160,-1.870089,-0.510148,-7.717878,5.723031,-7.218450,-1.758161,-7.601626,-9.820393,-0.972353,-1.594147,-7.607555,4.182425,3.585050,9.868416,4.163369,2.380427,-4.165360,0.583521,3.091784,-7.119625,1.928902,0.211900,-8.375738,2.188534,0.970704,7.277258,1.746032,7.425877,-8.946098,4.560630,-8.758486,7.438664,-1.073383,0.667757,-2.587821,2.914951,9.663948,2.482717,-2.019280,-4.940720,-9.200601,-8.043348,-5.749150,-2.373406,-3.502358,-7.364941,-2.018806,-5.885534,1.437438,6.676856,3.726043,8.799559,5.175823,-4.633837,1.786524,4.035952,3.639296,6.707538,9.947980,-9.624124,8.630236,-3.870049,3.264608,4.551809,7.981931,-8.618679,0.771743,4.607756,-0.423159,4.469105,-7.574515,-4.316906,-8.865518,3.931417,1.190144,2.873739,-3.585331,2.560801,-4.242830,-0.251800,6.222706,3.139527,-8.966948,3.826788,-0.534126,-2.497997,-6.846254,-7.433955,-0.021044,-8.207934,-1.818023,9.777471,-3.810232,-4.331179,0.035671,-3.829134,6.072286,3.220112,-9.381033,-6.887782,3.846619,9.001912,9.673561,-2.625958,0.238275,-1.228602,2.659254,-9.857161,-7.574002,-4.741946,-8.603947,-7.714791,-7.918322,1.171382,-9.887464,-8.071950,5.080087,4.594311,2.537357,-3.852879,5.469454,-6.325480,-9.710605,-4.381548,4.789234,-0.363642,3.312719,8.821591,9.754722,-2.705759,1.394250,1.671375,-0.122277,8.871504,1.044079,-1.798020,-6.760465,4.140251,3.111591,1.937993,-3.519279,-2.151994,-2.617259,-7.623029,5.501153,-7.932769,7.654045,1.674398,-1.134807,2.623005,-9.232424,-6.276137,7.602371,-9.423734,5.489238,2.442822,5.540092,0.431668,-8.897398,7.603186,-2.970386,-3.961618,-9.472584,9.581804,-9.204534,-5.164305,-4.603429,-6.110862,-7.702925,8.467509,-2.658564,3.576114,-5.824435,-8.996731,-7.045351,-0.712590,2.698883,-4.793248,-9.052499,-2.037966,8.178368,-1.615800,-7.452174,5.717367,8.121682,-5.909137,6.828993,5.021609,8.783127,-2.127600,-6.841928,-2.186745,6.902138,4.561963,7.741343,9.792270,-9.602740,-9.628997,-0.512223,0.417715,-7.810766,9.374323,8.754496,-5.861803,-8.155764,0.057070,7.663274,-2.217969,-9.862241,7.698873,-8.077541,-1.589957,-1.882657,4.362102,-7.904251,-5.274352,-8.413384,8.007036,-4.114265,-1.582700,-8.549178,7.902126,-3.013914,7.953054,9.861957,-1.095186,4.067362,-3.497787,8.332541,-3.924859,-2.477157,5.351973,-3.843329,1.578441,-8.737392,-7.432536,9.444428,-0.122445,7.672388,-8.685440,-8.685460,-5.803161,-2.989678,8.786467,-8.189233,2.409107,-7.897255,-2.052968,7.960276,-1.964913,7.279111,7.555511,-9.075938,-4.840616,4.554436,7.743768,0.446786,7.018158,-2.415792,-3.461782,-2.865083,-1.563927,-8.433364,3.866352,-4.378079,7.464170,-8.484779,-5.702970,-4.275336,0.966473,6.075346,-4.276823,-3.522640,-5.338702,-9.756317,-3.904021,4.524219,-7.113581,0.044172,2.446288,3.348619,2.830509,2.775120,-6.888536,7.065111,5.138120,-4.745230,7.208003,2.267567,-3.222934,-4.283308,-2.378098,2.628338,6.906789,4.676622,-9.560003,5.651752,-5.311887,9.411451,3.047309,-9.928386,3.787009,-3.411249,-3.345132,3.111779,9.386808,0.467044,6.842604,-8.241038,4.421321,9.419026,-3.407646,4.212779,-3.470559,-5.653251,2.420949,-9.927517,4.453291,-1.288190,0.621620,-4.895931,4.405941,-4.255482,-5.959487,-1.081266,-1.077264,6.251672,-3.840679,-6.970289,3.398633,-5.558959,0.548840,-8.128896,3.329350,-7.085428,-0.204996,-9.707310,-7.751590,-7.332845,1.903371,-4.073163,-4.786005,8.899752,3.161742,3.676141,-8.151079,6.972042,8.859492,-7.714524,-0.650698,7.966809,-6.275170,1.967112,-6.088780,2.149103,-7.710919,-1.499713,-5.227273,1.223521,4.575903,-1.195718,2.531769,7.387059,8.835480,8.105791,5.808541,-2.445798,-5.553790,-0.549480,4.089480,6.408756,-8.227581,7.203252,6.962021,-8.863703,0.047165,-5.066546,-8.424549,7.062592,2.940623,-0.274677,6.076791,-3.069521,-6.010148,4.279932,1.017482,4.271325,-4.247646,-0.863482,9.733951,-5.651075,2.206942,6.613488,-7.342046,-7.382480,-1.714022,-1.512395,6.949904,0.724149,-6.855874,-7.394844,2.734846,8.272763,-9.556390,6.954451,-3.379532,-2.913704,-9.284180,9.162691,6.152020,4.049691,-1.842542,7.344025,-1.307738,1.250268,8.135910,-9.417964,1.498147,-7.661708,3.290047,-2.272072,7.611709,-7.515686,-6.474089,5.888210,8.128477,0.777277,-6.870244,1.551687,-5.919715,3.407266,-8.022021,-5.152655,0.218790,0.313023,4.838395,-5.315577,8.799896,-6.990267,9.876811,7.037458,-0.750572,-8.514288,9.509654,-0.327024,6.789170,-5.296206,2.302330,2.078023,6.626505,-4.081733,-1.217302,-2.934215,7.020194,-1.819580,-6.474680,0.002922,-6.909774,2.009110,3.665886,4.057364,-3.297072,5.972879,3.295537,-8.328414,3.435941,4.779899,-5.060497,8.144158,-1.225304,-9.080063,1.090873,-0.628050,6.349813,-4.677548,7.210568,0.093512,8.878692,9.776917,-1.543905,1.019225,-0.906709,3.426785,-3.618084,-1.358074,-1.508668,4.296883,-7.897350,-8.343863,-7.606195,8.919276,-7.867058,1.520003,5.116217,-9.621943,-3.171783,9.669137,-0.939285,6.091558,-5.550315,-2.515082,-4.459893,-4.015300,4.290597,5.990792,3.543165,4.565291,4.344989,9.888180,5.379124,-9.579526,-6.765573,4.896100,4.246683,2.084279,-5.483412,-6.529142,-4.793569,-2.387982,6.053221,9.403280,-3.680170,2.780672,0.921688,-2.757331,-7.343200,-2.444326,-8.827969,-7.032069,5.509348,4.135544,8.946222,-4.652854,4.175731,8.256546,-4.447580,9.727670,7.999634,6.403677,-0.911635,0.441835,-8.291425,8.222500,3.690646,-5.560292,9.109362,4.375646,-3.847000,-3.281957,-1.972359,-8.849120,-4.030277,6.361105,-6.068490,-6.271109,-7.806226,-5.682986,-6.309520,9.971918,6.129117,-3.822864,-6.722233,5.123345,2.539080,-8.797008,9.211148,0.559552,-8.640853,1.810879,9.735500,3.163288,0.374805,-3.974868,7.954317,-7.809161,-7.056842,-1.514565,-2.444258,8.929135,6.256714,7.672013,-3.789732,3.648917,5.153557,-6.326750,-5.307695,-8.719915,4.078567,5.946245,-8.050452,3.552852,-4.883559,5.632531,3.265477,4.918300,-9.292742,7.175447,0.102605,-8.886472,4.988676,5.549774,-4.240467,2.343938,-4.030285,7.432606,-4.243436,4.153505,-0.132498,2.921505,1.681381,-0.723121,8.994282,5.241818,-1.966526,6.454600,-9.329342,-0.924946,-8.979579,-5.821143,-2.990607,-6.909179,-4.315300,-4.266766,-8.066970,-4.494774,-2.071228,-4.342286,-0.076459,-6.420258,9.247742,-2.808248,-7.108725,-4.764929,-9.925190,0.537413,-0.706121,-8.661065,-2.353631,7.339720,-3.556806,-6.989680,8.795952,9.941382,-8.174443,-8.706075,2.668018,4.263431,5.846374,7.099593,-4.973551,9.181002,-5.218970,4.114245,-5.472088,2.983035,-2.813071,4.800861,-6.247215,2.667030,-5.719437,-8.816418,-0.221839,5.683644,-1.447158,-6.115903,8.488057,9.448715,7.244348,-2.846754,-1.172746,-2.521096,-2.390810,-2.177091,-0.838445,3.476237,2.620296,1.802973,-1.694719,-8.851198,5.179965,7.058948,-0.909387,-6.815497,-0.029032,7.732648,-0.663061,5.528931,6.166976,-9.627885,-5.352162,-6.059349,5.105111,3.406442,-7.189443,-1.900936,-3.157385,-9.275486,3.880725,-1.175988,-9.172156,-8.089889,-6.083970,3.026402,3.456516,8.570831,3.066704,6.898418,4.732954,-9.826525,-8.699338,3.185593,9.371844,9.785167,-1.554610,-3.137574,6.794131,-1.771130,-9.503730,8.459267,0.758056,8.440312,-9.013233,6.916097,-6.609717,1.138135,5.247423,4.807279,5.609092,7.546324,2.104019,-8.813249,-3.953633,-8.092061,-0.565499,-4.231822,-0.294704,-5.463073,-2.145561,3.983889,-6.622244,-7.260456,1.426057,-0.799458,-8.660333,6.102001,1.204228,7.357840,-0.035584,-7.464273,1.970676,-0.922019,5.830340,7.009101,-0.205063,-8.920414,9.902365,-4.470350,-6.485626,1.046933,-7.239664,-4.618692,-7.864061,6.479116,7.378019,1.557474,-8.945374,3.985908,9.917117,-5.811688,4.726274,-5.364709,0.855236,2.162147,4.974147,-8.166190,9.417891,5.315681,-3.999196,-5.828913,-9.266105,7.308962,5.469253,-0.529661,9.208153,3.006230,1.026848,5.796742,-6.974556,6.575025,-1.430109,-2.834885,-2.497815,7.962727,-1.292172,4.537378,-0.031683,-6.247303,6.214626,-3.168126,7.245389,2.986386,8.531539,2.861696,9.023826,6.763292,-7.464885,-8.884208,4.540633,-7.156686,1.319434,-7.064186,-2.563545,-9.937632,-6.503459,-7.774368,-4.462861,-8.461204,-3.403879,4.370708,-5.508563,1.975961,-8.597769,-5.409132,-9.102857,-3.218632,-8.422811,5.242057,5.343980,-0.810587,-1.024085,2.360911,-6.496101,-6.616571,9.617296,-5.982343,-5.240112,-2.519131,7.499372,-5.875069,6.865465,-0.283388,9.202776,-8.134028,6.992866,-1.301884,3.005962,-6.529281,-0.160972,3.861857,-3.071281,4.331170,3.820110,-2.197374,-6.666563,-3.647904,6.771010,4.629360,-9.727597,5.483586,-0.354801,6.922922,6.437422,3.577376,-7.486629,7.930832,2.510005,5.432856,-6.578693,8.224885,-3.547809,7.439848,-5.686243,4.659170,-8.300117,-5.591827,-6.029609,1.800842,0.936443,4.135877,6.083651,9.678387,-7.989182,3.385111,-8.381581,3.831285,4.384314,-1.971361,-0.100015,-1.528473,-5.857041,3.509671,9.887887,-1.838134,-9.792816,-0.733292,-3.273393,-1.154032,2.624290,7.926527,-4.923864,-3.402132,8.489381,-7.567658,-6.217549,3.661881,5.947800,-2.255364,1.420832,-9.018789,-0.602611,1.817481,-3.632134,4.309491,9.861200,0.669275,-5.766151,0.163697,-5.425307,9.297479,2.287648,5.914620,1.318734,6.087379,-6.121475,-2.074401,-6.063544,5.315279,0.196408,-8.131647,4.398435,1.483595,-7.981983,-9.473003,-9.345182,1.643944,-9.392149,-7.898629,-7.534693,-9.366490,0.536562,-7.414785,-1.107690,-7.447129,-7.549859,-9.643217,-6.179416,8.131625,4.398275,1.793640,8.390665,8.107867,7.350142,-3.707801,0.525041,-2.853193,8.714626,-6.400633,-1.507199,-6.686069,-0.798489,3.893821,-1.482886,3.003244,-8.471771,6.925402,6.280931,6.832396,-2.371381,6.575012,-2.078811,9.045619,-3.573853,1.306051,-1.109643,8.383517,-1.942956,-8.057761,-9.857202,-9.187968,-2.298586,-7.175204,-0.716771,2.205845,2.710294,-2.358082,-9.507538,-9.197130,-1.801899,-0.408503,4.688526,9.334914,-0.150422,-8.830232,7.538694,5.072890,-7.247554,9.225877,5.776672,7.160798,3.769891,-6.013823,9.312728,-1.745363,-4.487305,2.921118,4.101729,1.895674,-3.137824,-2.063825,6.032680,4.022350,5.709050,-1.915535,7.783435,-3.470454,-4.907151,5.402847,5.611088,6.891266,-8.309862,8.113031,4.148376,6.584853,-0.223286,2.068568,0.575078,9.264351,7.345850,4.305280,1.588492,-8.008240,-5.647500,-9.614308,4.228546,7.151542,-0.527546,6.261533,7.050021,0.069325,-5.028927,3.402405,9.054722,4.707522,2.743106,-3.192144,-3.565457,-8.293421,-4.037145,-5.229731,-0.550698,7.880162,-8.261416,-0.485182,8.349553,9.755722,-9.081403,3.942167,5.834123,-9.536492,9.413331,3.504205,6.868574,-6.210378,-6.375478,-1.615412,-0.804114,7.382892,-4.711156,-3.598764,9.394929,-7.764063,3.485392,-3.611466,-4.478410,2.912916,7.614963,6.437097,-5.458105,-0.633404,-2.656924,2.556061,-1.184644,5.500465,-1.556278,-3.612055,5.574566,4.002399,-7.364213,5.945198,-7.034189,-0.806940,5.979060,6.129016,0.981431,1.989787,-0.871463,-4.005479,4.267378,3.971466,0.991828,-6.849727,-4.362101,6.544972,1.110386,9.897154,3.627394,1.654381,8.530293,-0.649998,-2.962013,-8.277659,-4.138514,5.765277,-8.295553,0.494204,-0.229537,-5.769838,6.071976,0.872688,-2.409948,9.088237,-7.626336,9.585546,6.237971,-4.855121,7.148648,-8.103661,1.805201,1.415392,-3.692609,9.372042,-8.587987,-1.222225,-2.069319,-4.262967,-1.718498,-6.049635,-2.513838,4.605339,-6.737955,2.402168,-9.540108,5.719853,1.205886,-0.252789,-6.402063,-4.655769,6.719490,-7.789451,-8.084847,7.432514,-7.519345,6.321956,1.979336,-5.526508,-3.768787,1.798183,9.573792,-1.952350,7.454037,1.017595,4.202129,5.536548,-9.737781,-8.851224,-3.668008,8.292875,8.789987,-5.737347,9.902938,-8.031725,-6.782951,7.418900,5.552293,2.891025,-1.340764,-3.564235,-0.547459,-9.986651,9.492918,-6.226356,-0.805826,0.005479,-0.147618,-6.170990,-7.021705,-6.905144,-8.887322,5.522982,0.851030,0.667204,5.336087,1.373259,5.529260,-3.175103,-0.380121,-4.812022,-0.520226,8.252311,2.596205,5.147101,-3.288556,8.585646,6.580189,-2.837902,1.545967,-0.906952,6.779267,-3.644688,2.353894,-5.881966,1.463269,0.179417,-4.550712,4.862452,-3.774766,9.344416,-8.122479,-3.709422,6.715630,-0.524199,-6.701033,9.000099,6.314805,-9.323756,-4.444648,-9.919401,5.807386,-8.326981,-3.125945,-5.773662,-0.538310,-8.064685,-2.673345,-2.497842,1.529469,-7.874748,7.181398,-9.471976,3.621689,0.970733,0.888950,-3.189047,8.790456,-9.079323,-4.419484,0.830633,-1.119475,8.523475,-2.086087,0.393189,-4.492007,3.817621,5.051498,-7.160194,-9.765623,1.041559,-2.812780,-1.331881,-0.304780,0.558837,0.567457,5.585768,-0.586263,-0.642353,-3.671296,2.151626,2.810776,-9.721017,-1.288755,-3.546570,-8.622894,-6.348773,4.025730,3.389630,6.050684,-5.109472,8.410004,-7.245873,-0.993169,-0.287743,-0.921178,0.828075,-6.925533,3.234025,6.500231,5.760071,3.388067,-6.236517,-8.562923,-6.590258,-1.722482,4.306031,-7.810181,-6.780768,-0.593235,6.827197,-3.731396,7.179507,-4.129888,6.581273,-6.151199,4.104639,-5.484122,-0.342246,9.847752,-2.193943,7.237889,9.176496,1.554962,-6.160406,-1.624365,1.021909,-8.539760,4.980988,8.264704,-4.159664,9.224423,7.957199,0.551254,2.223272,-4.429400,8.727649,4.982283,3.450697,-9.608183,-5.571065,0.983481,1.341051,-0.146470,-1.387671,6.088356,7.977901,-2.391622,-2.125874,-2.425477,5.896084,0.206155,-2.831679,2.539128,8.327166,3.987803,5.582536,2.236512,1.128044,2.047717,7.332727,-2.340460,-6.705566,8.112921,5.350233,-0.605444,-5.141108,4.145340,-4.172107,-7.251629,-9.642150,5.744315,-6.103194,-5.217808,8.265156,0.370146,-8.536750,9.759891,4.756149,5.595055,2.940635,7.305785,7.203091,-2.660944,4.461679,4.525240,3.288630,0.663634,-5.974549,0.311948,-2.384721,-9.988463,-5.733840,4.076535,1.736359,-0.707296,-8.358292,-4.286389,-7.370660,6.961915,-7.540219,7.635692,3.116379,6.618408,-9.562732,9.915374,-8.208141,7.478382,-0.182044,-2.383358,7.463187,-5.761368,-1.902818,6.279551,8.890615,-8.341111,-9.946811,9.915535,6.072748,5.365730,0.078836,-4.909782,-2.808819,9.160644,-1.786644,-0.380103,-5.689460,4.780649,-7.061070,-2.085169,9.601587,3.393791,-2.514103,3.485115,4.757244,-0.754623,-0.614720,-0.713665,-0.115795,4.997948,2.297028,2.665107,-6.393106,-4.313347,6.114743,-6.698397,-8.866314,-2.870614,2.596951,-1.539324,-0.165674,6.201321,3.271331,-4.550617,3.691790,-8.075352,4.637968,2.189691,-6.519040,-7.714212,-5.644726,-2.297479,-6.183943,4.087239,-4.168883,5.253624,-0.795912,3.388858,-5.033209,-9.912270,4.039958,2.614145,-3.706144,-3.521199,-5.351048,-9.610738,-0.894550,8.092696,-1.148513,-7.919649,-4.804809,8.876210,-3.510797,-0.947370,-2.366463,3.914584,0.239890,6.112084,6.602270,-2.631584,-4.265987,-1.770716,4.977095,-6.598107,-2.921082,3.030847,-9.912015,-1.052329,8.121977,4.126527,7.692924,-1.097826,9.459457,-9.847243,3.602114,8.384923,8.160854,-4.803819,0.042730,-9.143176,1.439379,7.152612,2.321953,9.500491,-6.372177,-2.024347,6.432752,4.801079,-6.791068,2.773605,-8.020499,-3.937232,-8.349673,5.511849,2.466575,8.220989,2.915671,-7.407266,-5.649194,4.415143,-4.273626,-2.251943,-7.869717,5.895178,9.808584,5.726183,1.847642,-7.529817,-9.313385,1.506181,4.612666,6.473085,6.475002,1.934437,4.339014,5.334978,2.743640,0.162137,3.210805,-5.714425,9.716007,-7.859415,5.852937,-0.046162,-8.217543,9.084911,-3.837100,-6.667538,-9.998415,-4.283022,8.325955,-8.410839,3.650141,-5.073522,-1.737844,-9.996995,-6.470672,-9.628868,5.828462,-8.319149,-9.919124,1.783257,-9.507338,6.925483,-5.716333,-1.445488,7.007245,-5.758778,-3.772066,9.495537,7.812183,-3.286895,-5.275916,-1.816011,8.875772,-1.406868,-8.924529,-6.658301,9.615716,-5.786849,8.249759,3.265136,7.086547,-8.749122,7.777810,-6.540977,7.035986,-9.199722,6.934913,3.674401,6.621386,-8.707319,9.298771,-2.807382,-0.292243,-8.178344,0.920177,-7.341073,3.793931,-3.137713,-4.289712,-0.425402,4.692063,-1.150102,6.549230,8.306473,7.728541,-7.667767,1.781727,6.800314,5.656675,8.281256,-0.444874,1.464787,-0.246961,-7.728305,-3.675344,-0.089079,6.864855,-1.344787,-5.712006,-8.694045,-2.323574,9.122963,7.111924,9.445223,-0.189056,-2.074097,9.354251,9.026051,4.388704,-1.928905,-5.635236,-0.633903,6.178689,-2.190369,-3.017449,0.994583,6.438558,-5.572169,-1.911665,-2.681303,2.710116,9.225376,-9.471039,-3.454124,-7.088506,-1.622545,-1.097845,-5.192846,6.243485,3.081442,3.249942,-1.861125,0.776124,-4.642968,5.376993,2.351652,1.695086,2.508706,3.971489,3.843832,-2.871175,-5.605297,-7.206477,0.673941,1.795618,-0.056099,3.763736,1.142720,2.421622,-6.370610,-9.155282,7.941008,-6.417621,-9.976824,5.700897,4.005439,2.657643,-5.090555,5.899916,9.977932,-9.182395,3.062093,2.236510,3.985137,-5.266644,8.296704,7.869955,-2.416742,7.662207,6.922788,6.643494,-2.142189,-9.781176,-8.053724,-1.369192,-0.993507,1.490774,3.421986,-6.992554,-8.097754,-8.498203,-5.959631,-5.141565,-0.612513,5.225564,-0.595603,-5.372606,2.208383,3.033356,-0.438403,1.187682,1.472204,1.569246,0.284973,4.958529,-4.524365,0.191348,8.237390,-9.408765,5.785716,5.669236,-3.743064,7.386363,-2.082253,2.547767,-9.648666,2.293054,-9.513741,-7.372856,-8.266555,0.895761,-9.389202,0.437415,-7.584363,3.607829,6.520929,-8.955421,-1.313908,3.569271,-6.847847,-1.400307,-8.625815,-6.535517,-2.091980,-5.727275,-9.212318,5.936999,2.014088,-1.671436,-4.951168,4.102742,-3.136019,8.798874,9.684344,6.245156,-1.070769,9.624002,0.835081,7.245353,-7.022045,1.658712,3.692864,5.454645,6.740350,-6.590686,5.168344,-1.025932,4.404504,9.420789,-5.304560,4.947881,-8.609673,3.508823,-1.894948,9.775961,0.712913,-4.662546,0.243310,7.636077,6.970226,7.677291,6.885028,7.119322,0.672548,-1.694628,8.590909,-9.272799,-9.544652,-9.734007,-0.172353,6.417974,-7.865783,-9.253989,-6.257713,-3.860838,-8.192369,-6.768899,0.123268,-6.143923,-5.078169,1.984007,-6.445818,5.949403,5.973993,-7.167688,6.349645,1.695320,3.420797,-2.474961,6.679004,1.543028,-7.910229,-3.496093,6.212874,-8.159553,3.871496,-7.157956,-5.560110,-6.035722,0.545675,1.075661,-1.411164,-1.558644,5.372129,5.084021,2.606605,-0.295071,8.346971,-3.637841,5.594366,-3.580355,-7.089987,5.509052,4.870562,-5.384436,-6.275822,6.806618,0.772167,-5.002909,-4.401446,0.692529,-8.401290,2.256049,-9.958809,2.378174,2.116224,-5.044579,-9.536097,-7.440529,4.871027,-4.187698,-9.880855,9.052031,3.417123,-6.909461,5.092652,2.328545,3.887867,7.848620,-6.428055,-4.600624,7.424037,1.758037,-9.942367,3.471737,6.840079,6.422444,2.145750,9.013062,-0.661785,9.678572,5.581550,9.598172,6.711159,1.501063,9.847151,6.186188,-7.410797,-1.930865,-1.952274,1.068287,6.374648,-5.781179,1.213068,2.125371,8.587363,5.986993,-3.571342,-5.635920,-9.501253,7.686991,1.275975,-8.625450,-5.837847,-4.860506,-9.564408,-6.653020,-0.013196,-9.309058,-7.981726,8.338656,-8.232256,-5.665211,1.846680,9.146683,-3.978765,-0.150377,2.523432,-2.025398,7.364585,8.336689,-2.553356,-6.629919,-1.799682,-5.715228,-9.900593,-2.408335,-3.079179,9.967643,8.024331,9.963478,-2.787338,5.357321,-8.034306,9.258500,-9.278315,0.233855,-0.338462,8.739528,4.643689,1.500042,9.093545,-3.238935,-1.120395,-3.699365,-5.445563,-3.752650,7.935037,8.405354,5.252274,3.433694,5.554949,-4.886460,-2.815573,-2.195581,9.055932,-7.276668,1.243165,-9.979374,-9.407847,-4.743230,3.076092,1.687713,-6.305380,-0.286915,7.716397,-7.065765,6.008200,-6.557862,-4.008020,7.531099,-8.610025,4.030417,-6.088964,-7.601575,-8.013759,-1.613916,2.754928,-3.756431,-6.230952,2.904160,-8.518350,-9.652123,-8.555446,-9.314520,4.301972,-9.971609,5.829144,5.611347,5.015616,-0.872063,-2.824812,0.603563,8.912479,-8.520185,0.791161,7.756566,1.943641,6.734097,8.296626,-0.231326,9.132250,-8.237327,-6.004894,-8.526339,9.362449,2.097054,2.041339,4.731899,-4.481290,-2.980542,5.375589,-8.467202,9.184112,-6.453018,4.178045,4.249638,4.878462,0.590820,-3.142033,-2.466970,-2.749181,9.293132,-5.355643,-5.997501,-0.624683,-9.911648,9.585840,-7.118147,-3.023322,5.515501,-9.175331,-2.837879,-2.099560,3.069177,-5.574751,1.888921,-5.101589,-2.675832,8.938231,9.604290,-6.539977,-0.683963,-4.269247,-7.903663,9.692533,-2.615800,7.071349,-4.460870,-2.566874,-5.262942,7.717244,-6.642387,-3.638812,-8.342908,4.265145,-1.706218,-8.969094,9.825615,3.501107,2.635664,0.174840,-2.747473,3.818389,4.695737,2.816758,-5.792111,2.562786,-9.193955,5.463101,8.117244,-2.790317,-8.384843,-1.299888,-0.583198,-9.333234,6.032511,7.695243,-7.693085,-4.448766,4.905454,4.455728,-5.227650,-7.848622,-8.585612,2.469611,-4.526821,3.631623,-8.275746,3.892750,-5.376009,5.522824,5.728107,5.969584,9.876015,0.171147,5.453592,-1.950838,1.144353,-6.701686,-8.360763,-4.719689,-9.772882,-9.361069,4.018055,9.211909,8.938343,3.127583,9.894714,-6.124695,-5.287758,4.583228,-8.943475,3.347079,-6.469302,1.393871,-3.026627,-2.132478,-2.327623,6.524021,-8.752720,0.045519,3.951785,-4.305810,2.456038,7.852374,5.710570,-9.090047,-6.099133,1.745618,6.216675,-7.571850,-7.642157,-5.077587,7.124422,9.682530,-9.458345,2.320433,4.224964,4.503687,-2.796867,0.497135,2.122243,0.226054,0.307357,7.045165,3.666426,-2.134652,-0.481263,-7.873279,4.979424,1.750445,-3.691003,4.659393,-8.934975,1.732815,-1.526013,-6.229235,-5.454894,5.154177,4.871361,-9.026841,-1.464735,-8.157405,-0.440712,-7.641103,-4.563521,9.443689,-8.533774,7.419850,1.955131,9.451655,6.070580,-9.984463,4.284509,1.608544,-9.240375,-2.408578,7.669327,8.167924,4.774052,8.524669,9.544030,3.285682,5.362621,-8.580528,0.802239,-0.694181,-0.743191,-6.898533,6.473672,-7.529485,6.029749,-9.655872,3.279181,-2.875805,-9.488909,4.521541,1.232118,5.242753,3.302271,9.825972,-2.205352,1.670477,-1.573406,-1.716759,3.931341,5.470650,7.697936,4.708860,6.831512,-7.928474,0.312510,1.444058,-5.291981,-0.722215,6.614792,-5.346167,4.466385,-5.060875,1.369546,5.207795,1.543201,5.845724,9.731347,8.887835,4.500486,-9.641855,4.786032,9.326104,-3.216735,7.495213,9.009734,6.598005,2.785878,2.104072,7.976597,-6.595174,4.658155,3.066994,-4.035063,-9.694625,-9.579933,3.529389,-1.667512,7.454264,-9.626694,-4.298227,-4.350042,-5.715374,3.484546,-7.229972,4.615901,8.429232,3.629387,8.880696,-5.291842,3.656682,-0.479859,-8.499500,9.934113,4.032285,4.032520,9.648738,-3.438883,1.449741,2.576166,-5.790685,-1.484902,-8.335804,-6.572256,-5.894739,9.401783,-2.536591,-8.678370,-3.323348,-9.656565,8.552236,-3.476464,-0.960191,-5.941779,-0.319582,0.436673,-5.323091,4.424771,3.392841,-9.790783,-1.296730,1.242442,4.898889,7.941904,1.890599,-5.101630,9.613092,-0.511741,4.513368,-0.102571,-5.952345,-3.818147,9.312136,6.363403,2.220555,-0.364809,1.756223,-7.308074,5.529616,3.544671,-7.360085,7.003863,-8.299637,1.342052,6.523571,2.564798,2.592244,-0.299105,1.594275,-1.953370,-6.638988,-4.213724,-9.962731,-9.110268,7.725521,7.441796,5.669172,8.167622,-4.057235,5.868688,-0.016711,7.569413,-1.730812,1.837678,-8.381938,1.105541,-6.450380,-5.104175,-9.637280,3.103716,-6.907268,2.846361,9.681562,0.500113,5.496876,5.423746,-8.088417,-3.175211,8.462351,-1.026346,3.209844,-0.377606,-7.028338,-9.879982,8.782824,-1.678296,-1.250259,-3.801708,-8.629083,6.696267,-1.245277,-2.796808,-2.817243,-4.544066,-1.789955,4.738112,-3.331733,7.987710,-0.320157,1.785801,4.303458,-8.053470,-0.157595,-0.734036,-0.780128,-3.803302,-4.910719,9.827579,4.041125,-3.251470,8.972718,9.587760,6.745555,-9.253587,3.272031,-9.973356,2.833294,-1.131256,0.309183,-7.939565,9.091271,-5.875777,2.613741,-7.897511,7.767129,-8.450336,-4.235533,-7.091209,2.484601,0.100368,0.408471,0.306190,-9.778837,-4.505611,-8.030331,-9.558606,5.945797,-4.837656,-2.081196,-7.488271,8.799433,-7.763197,-5.347630,-4.294256,8.602732,-8.706557,3.819935,5.510780,-1.277354,9.182334,9.454277,-4.592534,-0.135386,0.592333,6.453874,1.725502,4.214881,-3.781805,-9.530217,4.233973,-2.737506,-1.145469,8.210378,-3.083062,2.771454,7.442938,1.256913,-9.334052,-7.526191,-9.781969,9.401756,-7.773584,-8.360582,-3.640914,8.776358,-3.635071,-6.620836,2.056197,7.906199,7.701974,3.062114,8.714925,-3.990261,3.606795,1.495767,-1.167433,8.176394,5.205313,1.129145,-5.003484,0.819896,-0.715787,-5.440811,-7.903412,2.521162,-2.834967,-3.082992,3.229191,5.404291,1.737387,5.823959,5.790690,-5.854884,-0.610436,1.761608,3.115944,3.649437,-1.127835,8.519474,2.790157,-6.648812,-1.024826,2.096191,9.503679,-1.541477,-9.894688,-4.492499,-4.569433,-6.712736,-2.934987,7.422569,2.501092,1.503435,-3.438799,-8.363947,-2.724213,-3.994698,4.819093,-9.788766,-4.512522,5.544196,-8.146573,1.221253,-3.845510,6.780174,1.106235,-7.540577,-1.859359,-6.626474,1.251194,-7.454257,0.738707,-1.581232,9.334043,6.623485,8.607353,-9.359098,-7.671409,-9.096203,1.721487,4.511358,-9.789460,4.929898,1.472021,-7.154710,-8.152449,-3.572293,4.714307,-6.191819,-1.766840,-8.884589,-3.154534,5.209523,-1.005213,-5.337132,-5.448816,-9.320926,2.430196,9.424467,3.466716,4.547863,-1.216400,8.602578,-6.289450,-8.995787,3.862409,-0.511714,9.829686,-9.314424,2.150847,-5.114219,-7.448328,6.865826,-5.454887,4.173944,-1.251786,-4.669819,-6.475833,-7.941628,0.627128,3.425304,6.630032,7.252398,-9.406555,5.176806,-5.245999,0.945290,-8.069974,-1.224163,4.314944,8.876541,8.031260,-8.471132,9.834886,-7.238515,-9.544501,-3.842904,-4.352895,-2.597695,9.824038,-2.728848,8.570691,6.316540,-2.958018,4.621819,5.731101,6.206222,-4.143701,-9.368571,-3.899941,-8.000068,0.405284,2.750148,-4.709495,-4.890880,3.585146,5.775320,-0.341575,-8.552407,7.231051,-0.692479,-9.387160,6.411955,9.084475,0.567292,-0.470493,-2.428927,-9.606975,8.092011,-3.752306,-8.475535,7.185766,-4.868741,-5.244735,-4.801983,-4.517713,-1.579872,5.661301,2.149536,-5.925531,-5.680592,2.962605,-0.236761,-4.715181,-0.242635,0.251521,-5.726106,3.195191,-5.285724,-9.923603,6.330662,9.338536,8.343665,7.793097,1.409327,4.802119,-2.634442,6.417860,-4.155137,7.322090,-4.938188,-7.716411,6.839095,4.293244,6.898702,-0.219840,9.571831,1.790808,-5.397729,3.074696,-6.018596,-0.830162,2.532029,9.605934,1.565122,8.979122,7.531937,2.951072,4.784326,-5.428308,-6.763177,5.894092,-0.077220,-0.548132,3.348129,-0.141954,8.631501,-3.212054,-4.458286,-8.373101,-4.370775,7.020922,2.937840,-7.816580,-7.532308,-1.277441,-5.052492,-9.527800,-2.522295,6.907510,-2.114833,5.757214,-1.238038,5.483882,3.509875,1.675045,9.490175,2.251741,4.667420,2.157904,-2.982310,-1.266522,5.116759,8.825713,7.969219,2.617575,-4.551176,8.220924,-6.873011,-1.230296,0.378074,-0.252707,-5.829559,1.899164,3.691589,2.332106,-0.289108,-3.041683,-0.717186,1.423506,1.931364,-2.918618,1.151748,-0.766494,-2.052037,9.462170,-8.993938,-4.826987,8.457072,-7.587187,-9.316565,-1.830369,1.223731,-4.400429,-7.683473,-9.277286,-2.785284,-9.860429,-2.454562,6.674071,5.423903,-5.737082,-9.356552,-9.828135,8.233623,9.442075,8.101053,-6.008587,-0.270023,-1.886367,7.497412,-0.990350,2.418673,1.545889,-9.780344,-8.280426,-5.998120,7.188196,7.649174,-5.878633,6.131506,-1.116343,-1.451598,4.316648,2.417609,8.306117,-1.860982,-6.660677,-8.487532,-6.349997,0.223130,-3.856923,7.133052,-8.579481,-2.472965,4.610691,-4.889492,-4.825799,9.201786,-3.301225,0.767320,0.121526,0.337598,-6.063625,0.379702,-6.925570,9.579774,-1.716081,3.507805,-6.512645,-3.541469,3.567083,1.169482,8.605798,1.966643,-7.242684,4.650334,2.869923,7.409279,1.587732,-8.387147,0.707370,-3.026374,-3.189160,9.606959,9.406204,3.156776,-0.360638,-2.977115,2.869392,1.912019,3.290251,3.099531,-2.882568,-3.162113,5.842462,6.236335,-0.625718,5.806022,5.803981,1.169555,-4.446538,5.984960,-5.426297,-7.312893,-3.420184,1.032887,-8.031452,-9.164372,2.142077,-4.626655,4.174636,-9.863112,-3.703098,-5.219958,-7.096103,-4.432620,-3.631224,0.593270,-4.239013,-9.755448,-4.167178,-0.748959,-9.289106,6.617014,6.958513,6.858952,9.395522,-2.843507,2.520498,-3.964304,2.280992,-5.266430,-0.887825,-3.126168,1.362231,4.379643,-2.988432,-8.399320,-3.202320,-8.349557,-6.673311,-4.986835,3.407284,4.345697,-7.513192,-2.370951,-9.318670,7.584667,5.496854,9.745108,4.574564,-8.550332,-3.823892,-3.443934,-0.527366,-3.620044,-3.897247,-0.413483,-3.994495,-8.918202,2.438548,-2.738262,1.979989,6.276462,2.015643,6.797437,5.127751,-3.864724,0.099145,4.155602,3.214544,-8.806349,-1.481872,-7.001009,-8.850508,4.422875,3.770361,7.359050,-7.951241,7.144217,-6.257372,-6.571793,-2.217575,4.934008,0.306611,6.931368,9.689376,0.306169,7.434210,-2.778764,-4.399804,7.663453,0.473863,6.278247,1.859963,0.340143,2.492316,-0.028456,-5.489161,3.322177,-7.158837,-8.572748,-3.503916,7.731006,5.096007,2.939687,-8.593998,-3.479019,-8.432954,6.099034,-2.769557,8.373415,-0.423419,-3.504826,6.616737,-7.145098,-2.079542,4.949905,-4.931359,-2.928840,-4.945074,-9.810228,4.132491,-0.336417,-0.939698,1.712330,-9.391119,-6.445247,-2.314697,9.462973,1.137182,6.120764,6.018482,-5.114708,-2.853267,9.745729,7.959261,2.253392,-9.902673,-2.147069,8.510189,-6.537282,-3.267827,-9.153204,1.231968,-1.654468,7.300716,-7.623993,8.516857,6.009918,-7.033288,-3.411969,-6.387440,-1.366072,-5.201263,6.174973,-1.200735,1.293504,-3.286914,-0.149225,-5.301759,-8.196813,-9.729730,-4.355756,-7.149511,1.913171,-0.036883,-8.950238,8.771217,-9.719160,1.024973,3.424373,0.049151,-4.166964,-7.107822,4.922580,2.774380,1.056353,-6.073150,8.666705,4.488479,9.464141,6.813899,-9.293934,-9.779863,-2.155286,-9.082629,-7.415644,-7.444150,9.819776,9.753196,6.724136,8.646430,-8.178474,-8.368805,-9.704076,0.755281,-8.487435,7.029294,4.940472,8.881741,4.665073,-5.780570,6.335476,-8.912198,3.679946,7.809150,-8.636659], dtype = "float32")#candidate|11488|(3600,)|const|float32
call_11487 = relay.TupleGetItem(func_6549_call(relay.reshape(const_11488.astype('float32'), [3600,])), 1)
call_11489 = relay.TupleGetItem(func_6552_call(relay.reshape(const_11488.astype('float32'), [3600,])), 1)
output = relay.Tuple([call_11481,call_11487,const_11488,])
output2 = relay.Tuple([call_11482,call_11489,const_11488,])
func_11511 = relay.Function([], output)
mod['func_11511'] = func_11511
mod = relay.transform.InferType()(mod)
output = func_11511()
func_11512 = relay.Function([], output)
mutated_mod['func_11512'] = func_11512
mutated_mod = relay.transform.InferType()(mutated_mod)
const_11534 = relay.const([[[5,9,-4,8,-4,4,-7,6,3,-3,-9,-2],[-1,-1,-8,7,10,5,-4,7,9,-7,4,2],[-9,8,3,-6,-9,-9,7,-2,1,-1,2,2]],[[1,10,3,5,-6,-1,-4,-7,-3,2,4,6],[-3,10,-5,9,-2,-1,2,8,-8,-8,3,7],[-2,5,-3,1,6,-3,4,6,10,10,3,1]],[[6,-6,-7,-6,-2,-4,1,-4,7,-9,9,8],[3,3,-7,-1,-4,-1,-10,9,-7,10,10,-7],[9,-9,-1,10,-6,-2,-5,-5,10,9,4,-3]],[[-3,-1,6,2,-3,-6,10,10,6,9,7,-10],[2,8,-9,9,5,-5,-9,6,7,-8,-7,3],[2,-5,-7,-7,-8,7,7,7,9,3,-10,9]],[[3,4,-8,3,2,1,5,-8,-3,10,4,-2],[-1,10,5,9,-1,-6,-4,10,-7,3,7,6],[-10,-1,-4,-9,7,-6,-1,10,10,10,5,7]],[[-9,5,-4,9,7,-10,3,8,9,4,-1,-1],[-2,-4,-10,-10,-3,-8,-8,-3,-7,6,4,-1],[7,2,-2,8,5,1,-3,6,-8,5,1,8]],[[4,-7,-7,-1,4,2,-6,9,4,-7,-1,-5],[7,-4,1,-6,8,-3,-2,1,8,3,6,5],[2,-7,7,3,-3,4,-10,10,4,3,8,1]],[[9,-9,-5,-7,8,-1,7,1,-2,-5,-5,-10],[-8,4,-1,1,-10,7,5,-4,7,10,-1,3],[7,-6,4,-5,1,8,6,-1,8,-4,1,7]],[[-3,-1,1,-8,3,3,1,2,9,5,-9,-4],[6,1,-7,-5,-7,-7,-10,9,10,-3,-1,-7],[4,6,10,-10,7,4,-2,-4,-5,9,5,-1]],[[9,-8,-8,9,-8,-5,4,-7,-1,-6,-1,-3],[-1,-4,-10,3,-8,10,-7,9,-3,-6,-4,-9],[-5,7,5,-2,2,-5,10,2,9,7,-10,-3]],[[-1,-1,1,9,2,10,5,4,-10,2,6,-10],[-7,-5,3,1,7,8,-9,-2,2,10,5,-9],[-4,-7,-6,-7,3,-1,8,-10,-1,2,5,4]],[[-7,-7,10,-9,6,5,2,6,-4,2,8,-8],[10,10,4,-5,10,-5,-9,-5,4,-8,3,-4],[10,8,7,6,6,3,1,2,3,4,-6,6]]], dtype = "int8")#candidate|11534|(12, 3, 12)|const|int8
var_11535 = relay.var("var_11535", dtype = "int8", shape = (12, 3, 12))#candidate|11535|(12, 3, 12)|var|int8
bop_11536 = relay.bitwise_and(const_11534.astype('int8'), relay.reshape(var_11535.astype('int8'), relay.shape_of(const_11534))) # shape=(12, 3, 12)
uop_11541 = relay.asinh(var_11535.astype('float32')) # shape=(12, 3, 12)
output = relay.Tuple([bop_11536,uop_11541,])
output2 = relay.Tuple([bop_11536,uop_11541,])
func_11545 = relay.Function([var_11535,], output)
mod['func_11545'] = func_11545
mod = relay.transform.InferType()(mod)
var_11546 = relay.var("var_11546", dtype = "int8", shape = (12, 3, 12))#candidate|11546|(12, 3, 12)|var|int8
output = func_11545(var_11546)
func_11547 = relay.Function([var_11546], output)
mutated_mod['func_11547'] = func_11547
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2210_call = mod.get_global_var('func_2210')
func_2212_call = mutated_mod.get_global_var('func_2212')
call_11559 = relay.TupleGetItem(func_2210_call(), 1)
call_11560 = relay.TupleGetItem(func_2212_call(), 1)
func_3092_call = mod.get_global_var('func_3092')
func_3094_call = mutated_mod.get_global_var('func_3094')
call_11561 = func_3092_call()
call_11562 = func_3092_call()
output = relay.Tuple([call_11559,call_11561,])
output2 = relay.Tuple([call_11560,call_11562,])
func_11567 = relay.Function([], output)
mod['func_11567'] = func_11567
mod = relay.transform.InferType()(mod)
output = func_11567()
func_11568 = relay.Function([], output)
mutated_mod['func_11568'] = func_11568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1190_call = mod.get_global_var('func_1190')
func_1191_call = mutated_mod.get_global_var('func_1191')
call_11576 = func_1190_call()
call_11577 = func_1190_call()
var_11582 = relay.var("var_11582", dtype = "float32", shape = (2, 7, 11))#candidate|11582|(2, 7, 11)|var|float32
bop_11583 = relay.greater_equal(call_11576.astype('bool'), var_11582.astype('bool')) # shape=(2, 7, 11)
bop_11586 = relay.greater_equal(call_11577.astype('bool'), var_11582.astype('bool')) # shape=(2, 7, 11)
func_2210_call = mod.get_global_var('func_2210')
func_2212_call = mutated_mod.get_global_var('func_2212')
call_11588 = relay.TupleGetItem(func_2210_call(), 0)
call_11589 = relay.TupleGetItem(func_2212_call(), 0)
output = relay.Tuple([bop_11583,call_11588,])
output2 = relay.Tuple([bop_11586,call_11589,])
func_11590 = relay.Function([var_11582,], output)
mod['func_11590'] = func_11590
mod = relay.transform.InferType()(mod)
mutated_mod['func_11590'] = func_11590
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11591 = relay.var("var_11591", dtype = "float32", shape = (2, 7, 11))#candidate|11591|(2, 7, 11)|var|float32
func_11590_call = mutated_mod.get_global_var('func_11590')
call_11592 = func_11590_call(var_11591)
output = call_11592
func_11593 = relay.Function([var_11591], output)
mutated_mod['func_11593'] = func_11593
mutated_mod = relay.transform.InferType()(mutated_mod)
const_11602 = relay.const([[[8,-10,-1,4,4,1,10,-3,-7,6,7,-4],[-10,6,3,-9,-3,-6,8,2,1,-5,7,3]],[[-9,2,5,-2,2,-8,7,-8,8,7,-5,7],[2,8,2,-5,-2,-8,3,-2,8,-2,7,7]],[[7,3,-3,-9,-4,6,10,-6,8,-1,-4,10],[3,8,3,5,-7,1,9,-7,-8,-9,-6,-1]],[[9,-9,-5,4,2,-5,-5,-4,-1,4,-6,-2],[-6,3,6,-10,3,5,-8,-5,-2,5,3,2]],[[8,-3,-1,-9,6,10,-5,6,-10,8,-3,-8],[3,2,7,-9,2,-9,7,-9,-1,8,1,-4]],[[6,-9,-4,3,4,-3,-9,-4,-4,-5,3,5],[-5,8,8,7,5,-2,6,-8,1,9,-4,3]],[[8,-1,4,-4,1,-6,-5,3,-2,-3,-2,-7],[2,5,1,-6,-7,-9,-4,-1,7,4,-2,-6]],[[-3,3,7,8,-5,7,-10,4,-9,10,6,-10],[1,-6,4,9,8,3,-9,-5,4,2,-5,3]],[[9,-9,7,1,7,10,9,9,1,-3,2,7],[-1,2,-7,-2,-10,-3,-4,4,-2,-5,6,-8]],[[-5,-9,10,3,-7,9,-9,10,4,8,-10,1],[9,-2,-7,3,-1,9,8,-5,8,-9,-7,-8]],[[-6,10,9,5,5,-4,-8,-6,-9,2,-8,2],[-3,3,-4,10,7,6,-1,-3,-10,1,-4,-7]]], dtype = "uint16")#candidate|11602|(11, 2, 12)|const|uint16
var_11603 = relay.var("var_11603", dtype = "uint16", shape = (11, 2, 12))#candidate|11603|(11, 2, 12)|var|uint16
bop_11604 = relay.bitwise_and(const_11602.astype('uint16'), relay.reshape(var_11603.astype('uint16'), relay.shape_of(const_11602))) # shape=(11, 2, 12)
output = relay.Tuple([bop_11604,])
output2 = relay.Tuple([bop_11604,])
F = relay.Function([var_11603,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_11603,], output2)
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
