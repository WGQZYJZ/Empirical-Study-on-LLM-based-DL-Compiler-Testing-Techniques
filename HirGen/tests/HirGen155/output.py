import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_8 = relay.var("var_8", dtype = "float32", shape = (10, 9, 5))#candidate|8|(10, 9, 5)|var|float32
uop_9 = relay.log10(var_8.astype('float32')) # shape=(10, 9, 5)
output = relay.Tuple([uop_9,])
output2 = relay.Tuple([uop_9,])
func_11 = relay.Function([var_8,], output)
mod['func_11'] = func_11
mod = relay.transform.InferType()(mod)
mutated_mod['func_11'] = func_11
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12 = relay.var("var_12", dtype = "float32", shape = (10, 9, 5))#candidate|12|(10, 9, 5)|var|float32
func_11_call = mutated_mod.get_global_var('func_11')
call_13 = func_11_call(var_12)
output = call_13
func_14 = relay.Function([var_12], output)
mutated_mod['func_14'] = func_14
mutated_mod = relay.transform.InferType()(mutated_mod)
const_236 = relay.const(3, dtype = "uint32")#candidate|236|()|const|uint32
var_237 = relay.var("var_237", dtype = "uint32", shape = (3, 16, 12))#candidate|237|(3, 16, 12)|var|uint32
bop_238 = relay.logical_xor(const_236.astype('uint32'), var_237.astype('uint32')) # shape=(3, 16, 12)
uop_242 = relay.sin(bop_238.astype('float64')) # shape=(3, 16, 12)
output = uop_242
output2 = uop_242
func_253 = relay.Function([var_237,], output)
mod['func_253'] = func_253
mod = relay.transform.InferType()(mod)
var_254 = relay.var("var_254", dtype = "uint32", shape = (3, 16, 12))#candidate|254|(3, 16, 12)|var|uint32
output = func_253(var_254)
func_255 = relay.Function([var_254], output)
mutated_mod['func_255'] = func_255
mutated_mod = relay.transform.InferType()(mutated_mod)
var_411 = relay.var("var_411", dtype = "int16", shape = ())#candidate|411|()|var|int16
var_412 = relay.var("var_412", dtype = "int16", shape = (3, 1, 9))#candidate|412|(3, 1, 9)|var|int16
bop_413 = relay.not_equal(var_411.astype('bool'), var_412.astype('bool')) # shape=(3, 1, 9)
output = bop_413
output2 = bop_413
func_416 = relay.Function([var_411,var_412,], output)
mod['func_416'] = func_416
mod = relay.transform.InferType()(mod)
var_417 = relay.var("var_417", dtype = "int16", shape = ())#candidate|417|()|var|int16
var_418 = relay.var("var_418", dtype = "int16", shape = (3, 1, 9))#candidate|418|(3, 1, 9)|var|int16
output = func_416(var_417,var_418,)
func_419 = relay.Function([var_417,var_418,], output)
mutated_mod['func_419'] = func_419
mutated_mod = relay.transform.InferType()(mutated_mod)
var_791 = relay.var("var_791", dtype = "float32", shape = (6, 2, 16))#candidate|791|(6, 2, 16)|var|float32
var_792 = relay.var("var_792", dtype = "float32", shape = (6, 2, 16))#candidate|792|(6, 2, 16)|var|float32
bop_793 = relay.divide(var_791.astype('float32'), relay.reshape(var_792.astype('float32'), relay.shape_of(var_791))) # shape=(6, 2, 16)
uop_798 = relay.sin(var_792.astype('float32')) # shape=(6, 2, 16)
output = relay.Tuple([bop_793,uop_798,])
output2 = relay.Tuple([bop_793,uop_798,])
func_804 = relay.Function([var_791,var_792,], output)
mod['func_804'] = func_804
mod = relay.transform.InferType()(mod)
mutated_mod['func_804'] = func_804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_804_call = mutated_mod.get_global_var('func_804')
var_806 = relay.var("var_806", dtype = "float32", shape = (6, 2, 16))#candidate|806|(6, 2, 16)|var|float32
var_807 = relay.var("var_807", dtype = "float32", shape = (6, 2, 16))#candidate|807|(6, 2, 16)|var|float32
call_805 = func_804_call(var_806,var_807,)
output = call_805
func_808 = relay.Function([var_806,var_807,], output)
mutated_mod['func_808'] = func_808
mutated_mod = relay.transform.InferType()(mutated_mod)
var_946 = relay.var("var_946", dtype = "float32", shape = (9, 3, 5))#candidate|946|(9, 3, 5)|var|float32
uop_947 = relay.asin(var_946.astype('float32')) # shape=(9, 3, 5)
const_955 = relay.const([[[1.000546,-1.995966,2.197144,5.683829,-2.682322],[-4.471395,-5.814662,-3.904723,-9.962321,-9.056011],[1.275215,5.613545,2.104987,-9.555990,-9.214187]],[[5.512429,-4.977302,-0.099479,3.442350,4.763488],[-7.889374,9.109140,-6.955576,2.540689,2.815122],[7.974824,8.499834,-7.066499,0.355451,-8.260991]],[[-8.210013,5.654802,9.292365,-3.404199,-4.520221],[-4.438335,-3.820320,0.465127,5.015447,8.243688],[-6.322743,8.715568,3.125343,7.671924,-5.055883]],[[-1.993510,6.989149,-8.674981,4.966242,3.592684],[-3.212901,-0.422217,4.504128,-0.685646,7.429400],[3.811041,-4.897688,1.247382,8.249127,-6.833563]],[[-6.362592,-8.248997,6.851424,-7.473106,-3.270297],[-9.925836,4.453324,3.589970,-2.614161,-7.769711],[8.298463,-5.536208,-1.978992,5.301932,-7.263794]],[[-7.073573,-1.208746,-0.613582,5.818902,-4.500144],[-0.866490,-3.607385,-6.435294,3.079552,8.808061],[-8.616941,6.170821,1.777001,-9.137449,0.440958]],[[-1.216275,4.825093,6.670733,-2.236007,-9.240446],[-3.267656,5.406463,-3.009917,-0.165290,3.438934],[3.792332,-4.725969,-8.026106,7.698838,-3.700641]],[[7.162685,-6.209220,9.494164,-6.543054,-3.401831],[-4.436337,8.670496,4.605532,2.138031,9.763986],[-6.299423,-0.928309,-9.217341,-1.199167,4.083473]],[[-9.564012,3.300828,2.413353,-7.830473,4.232232],[-8.664250,7.533748,6.641686,-5.013162,-3.650584],[5.546125,-1.468284,2.878264,-0.043361,-5.015035]]], dtype = "float32")#candidate|955|(9, 3, 5)|const|float32
bop_956 = relay.mod(uop_947.astype('float32'), relay.reshape(const_955.astype('float32'), relay.shape_of(uop_947))) # shape=(9, 3, 5)
func_804_call = mod.get_global_var('func_804')
func_808_call = mutated_mod.get_global_var('func_808')
const_973 = relay.const([-1.123970,-9.840377,-6.980718,1.005990,-0.970687,7.418219,3.113235,-3.891524,3.803915,-3.838745,4.534629,4.494574,5.699126,-4.789259,-7.136971,-6.443883,-9.450470,7.487506,2.822939,-1.113622,0.680764,9.810393,-6.710607,-4.445741,-0.133530,1.127080,-7.709069,1.023027,6.012199,-7.437258,0.507709,-9.302525,-4.652355,-5.665957,9.672609,0.566786,-7.852855,6.815889,-0.573083,-6.902316,4.207057,-3.399959,-6.985268,3.090874,-9.256284,9.275798,-8.470928,6.564413,4.549149,-5.085957,-9.373636,-1.195469,-8.069025,-5.736425,8.268643,0.339051,-1.283078,-0.505471,4.125427,6.162928,-1.016943,3.382840,-0.068933,6.779906,-3.665385,-8.576041,0.472643,9.696365,0.242147,6.137570,7.558194,3.397423,-8.721583,-7.044146,0.543161,6.046021,5.556242,-6.423343,-1.259971,1.209424,1.189195,9.179473,-0.102807,-5.874028,-2.603926,6.269865,-9.256357,-4.644612,-4.234585,-8.967662,-3.004174,2.767400,2.155905,3.813202,5.554825,-2.345603,7.540277,-7.232034,2.019814,5.994900,-8.789235,0.825411,8.168781,9.364522,-6.958300,2.185773,-4.710611,-5.083147,-3.798790,8.133441,1.816762,-4.040153,1.266411,-7.300591,6.106317,4.791954,-4.260555,-4.912655,-7.999200,-9.364526,8.920503,5.822175,-4.569270,9.985610,0.946399,2.893932,9.763951,9.946084,-9.704700,3.248522,4.114238,6.451199,3.032366,4.611951,0.639981,-4.008332,4.169478,-0.918023,-1.313011,-6.616993,-7.026981,-1.747967,5.521231,0.614953,4.948904,2.602609,2.924733,3.200544,-7.404534,-1.266035,-5.265221,2.480542,-6.266611,3.532103,7.299893,-5.835140,2.719475,2.340101,0.815035,-9.695204,3.790506,9.524153,-2.183370,3.540604,-4.034507,8.535751,7.421535,-3.900011,-1.516112,-2.520590,-3.827270,-7.743737,0.376557,-4.087477,-5.569415,3.331659,6.697505,-0.666166,3.304782,-8.618499,0.650948,-1.668357,-0.828623,-5.601360,0.189092,7.174411,9.684580,1.763458,0.414722,2.696377,5.263090,-1.411685], dtype = "float32")#candidate|973|(192,)|const|float32
call_972 = relay.TupleGetItem(func_804_call(relay.reshape(const_973.astype('float32'), [6, 2, 16]), relay.reshape(const_973.astype('float32'), [6, 2, 16]), ), 0)
call_974 = relay.TupleGetItem(func_808_call(relay.reshape(const_973.astype('float32'), [6, 2, 16]), relay.reshape(const_973.astype('float32'), [6, 2, 16]), ), 0)
uop_975 = relay.tan(call_972.astype('float32')) # shape=(6, 2, 16)
uop_977 = relay.tan(call_974.astype('float32')) # shape=(6, 2, 16)
func_416_call = mod.get_global_var('func_416')
func_419_call = mutated_mod.get_global_var('func_419')
var_996 = relay.var("var_996", dtype = "int16", shape = ())#candidate|996|()|var|int16
const_997 = relay.const([[-9,4,-6,4,-1,3,3,1,7,4,-9,-6,6,1,-3,-2,9,-10,-5,8,-9,3,-2,3,2,-5,10]], dtype = "int16")#candidate|997|(1, 27)|const|int16
call_995 = func_416_call(relay.reshape(var_996.astype('int16'), []), relay.reshape(const_997.astype('int16'), [3, 1, 9]), )
call_998 = func_416_call(relay.reshape(var_996.astype('int16'), []), relay.reshape(const_997.astype('int16'), [3, 1, 9]), )
func_11_call = mod.get_global_var('func_11')
func_14_call = mutated_mod.get_global_var('func_14')
var_1010 = relay.var("var_1010", dtype = "float32", shape = (450,))#candidate|1010|(450,)|var|float32
call_1009 = relay.TupleGetItem(func_11_call(relay.reshape(var_1010.astype('float32'), [10, 9, 5])), 0)
call_1011 = relay.TupleGetItem(func_14_call(relay.reshape(var_1010.astype('float32'), [10, 9, 5])), 0)
var_1015 = relay.var("var_1015", dtype = "float32", shape = (9, 3, 5))#candidate|1015|(9, 3, 5)|var|float32
bop_1016 = relay.right_shift(uop_947.astype('uint16'), relay.reshape(var_1015.astype('uint16'), relay.shape_of(uop_947))) # shape=(9, 3, 5)
output = relay.Tuple([bop_956,const_973,uop_975,call_995,var_996,const_997,call_1009,var_1010,bop_1016,])
output2 = relay.Tuple([bop_956,const_973,uop_977,call_998,var_996,const_997,call_1011,var_1010,bop_1016,])
func_1021 = relay.Function([var_946,var_996,var_1010,var_1015,], output)
mod['func_1021'] = func_1021
mod = relay.transform.InferType()(mod)
var_1022 = relay.var("var_1022", dtype = "float32", shape = (9, 3, 5))#candidate|1022|(9, 3, 5)|var|float32
var_1023 = relay.var("var_1023", dtype = "int16", shape = ())#candidate|1023|()|var|int16
var_1024 = relay.var("var_1024", dtype = "float32", shape = (450,))#candidate|1024|(450,)|var|float32
var_1025 = relay.var("var_1025", dtype = "float32", shape = (9, 3, 5))#candidate|1025|(9, 3, 5)|var|float32
output = func_1021(var_1022,var_1023,var_1024,var_1025,)
func_1026 = relay.Function([var_1022,var_1023,var_1024,var_1025,], output)
mutated_mod['func_1026'] = func_1026
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1058 = relay.const([[4.966424,-7.968971,3.225037,-4.574459,-1.993815,5.704420,8.167760,1.840133,8.264647,-8.269380,-4.253294,9.931943,1.926634,-4.394133],[-3.059624,6.599669,-5.698382,-0.012310,-4.726825,-5.382157,9.162815,-0.870777,-3.551273,-2.968117,-6.875188,4.016927,8.587931,-5.584629],[-7.736850,-0.205775,-5.441660,-2.962810,5.464321,5.129849,3.118405,3.343038,2.649185,5.634999,7.389580,1.385767,6.061616,-7.850884],[7.110205,8.371388,1.891917,-0.161037,8.909081,8.322894,2.013626,-0.833607,-6.341285,0.564507,4.525539,5.740833,-3.432773,-1.864573],[3.117028,9.801613,0.138103,-0.192957,-8.689459,8.039356,9.542546,2.748065,9.800779,3.040420,8.958926,5.652655,-3.197871,0.080343],[2.126550,-3.088711,-6.944619,1.230582,-6.138385,0.191794,9.186417,-3.825628,0.225829,4.040285,8.928519,-6.196374,-8.257747,6.046677],[-8.207036,2.086512,4.337459,-5.609663,6.432763,5.614286,2.084251,4.497012,5.076951,0.553146,1.301005,1.288924,8.971904,0.175337],[7.219725,-7.115130,7.489686,9.129192,4.752364,-9.812214,-0.116906,-8.887268,-6.143504,-8.960968,1.605276,-7.200462,-3.467716,5.655571],[5.496975,2.774918,-7.652925,-6.372181,-0.271172,-4.391693,9.615205,-6.087007,-0.952056,3.146789,-5.329273,6.325763,2.686700,-9.876965],[7.218491,-1.308688,-2.172115,-1.901873,9.294305,-5.368595,-7.510984,-7.715327,-0.808204,1.803437,4.281504,8.449846,-4.465050,-8.543967],[3.299174,-1.094339,-1.568339,6.646731,-4.149362,9.384905,9.933290,6.279788,-7.101598,4.939556,3.702240,-6.979518,-7.326232,-1.308528],[-9.190568,-3.219651,-6.440972,-4.015074,3.946635,6.652073,6.314391,-5.206803,7.290193,1.022090,4.487778,-0.605833,8.379628,0.218106],[-8.802970,4.271094,-8.106628,-5.986972,-1.366879,-1.377957,3.522924,9.990987,-7.420002,2.204924,-7.524992,-4.609329,6.662406,-1.690143],[5.770222,-9.056232,5.420386,-6.072431,-0.006012,-4.184306,5.978684,-2.700875,4.532331,-5.084875,6.106256,2.528860,-5.998725,4.131524]], dtype = "float32")#candidate|1058|(14, 14)|const|float32
uop_1059 = relay.log2(const_1058.astype('float32')) # shape=(14, 14)
func_416_call = mod.get_global_var('func_416')
func_419_call = mutated_mod.get_global_var('func_419')
const_1062 = relay.const(10, dtype = "int16")#candidate|1062|()|const|int16
const_1063 = relay.const([2,-10,9,1,8,-9,-8,-8,-5,-7,-8,6,8,9,6,4,7,8,-5,-10,-4,9,-7,3,7,-2,-1], dtype = "int16")#candidate|1063|(27,)|const|int16
call_1061 = func_416_call(relay.reshape(const_1062.astype('int16'), []), relay.reshape(const_1063.astype('int16'), [3, 1, 9]), )
call_1064 = func_416_call(relay.reshape(const_1062.astype('int16'), []), relay.reshape(const_1063.astype('int16'), [3, 1, 9]), )
output = relay.Tuple([uop_1059,call_1061,const_1062,const_1063,])
output2 = relay.Tuple([uop_1059,call_1064,const_1062,const_1063,])
func_1072 = relay.Function([], output)
mod['func_1072'] = func_1072
mod = relay.transform.InferType()(mod)
output = func_1072()
func_1073 = relay.Function([], output)
mutated_mod['func_1073'] = func_1073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1072_call = mod.get_global_var('func_1072')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_1077 = relay.TupleGetItem(func_1072_call(), 2)
call_1078 = relay.TupleGetItem(func_1073_call(), 2)
output = relay.Tuple([call_1077,])
output2 = relay.Tuple([call_1078,])
func_1080 = relay.Function([], output)
mod['func_1080'] = func_1080
mod = relay.transform.InferType()(mod)
output = func_1080()
func_1081 = relay.Function([], output)
mutated_mod['func_1081'] = func_1081
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1080_call = mod.get_global_var('func_1080')
func_1081_call = mutated_mod.get_global_var('func_1081')
call_1085 = relay.TupleGetItem(func_1080_call(), 0)
call_1086 = relay.TupleGetItem(func_1081_call(), 0)
output = relay.Tuple([call_1085,])
output2 = relay.Tuple([call_1086,])
func_1107 = relay.Function([], output)
mod['func_1107'] = func_1107
mod = relay.transform.InferType()(mod)
output = func_1107()
func_1108 = relay.Function([], output)
mutated_mod['func_1108'] = func_1108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1080_call = mod.get_global_var('func_1080')
func_1081_call = mutated_mod.get_global_var('func_1081')
call_1130 = relay.TupleGetItem(func_1080_call(), 0)
call_1131 = relay.TupleGetItem(func_1081_call(), 0)
func_1107_call = mod.get_global_var('func_1107')
func_1108_call = mutated_mod.get_global_var('func_1108')
call_1164 = relay.TupleGetItem(func_1107_call(), 0)
call_1165 = relay.TupleGetItem(func_1108_call(), 0)
output = relay.Tuple([call_1130,call_1164,])
output2 = relay.Tuple([call_1131,call_1165,])
func_1170 = relay.Function([], output)
mod['func_1170'] = func_1170
mod = relay.transform.InferType()(mod)
mutated_mod['func_1170'] = func_1170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1170_call = mutated_mod.get_global_var('func_1170')
call_1171 = func_1170_call()
output = call_1171
func_1172 = relay.Function([], output)
mutated_mod['func_1172'] = func_1172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1107_call = mod.get_global_var('func_1107')
func_1108_call = mutated_mod.get_global_var('func_1108')
call_1176 = relay.TupleGetItem(func_1107_call(), 0)
call_1177 = relay.TupleGetItem(func_1108_call(), 0)
func_11_call = mod.get_global_var('func_11')
func_14_call = mutated_mod.get_global_var('func_14')
const_1227 = relay.const([0.010509,5.077603,9.996968,4.277533,8.918952,-0.514828,-7.631761,5.645476,2.209108,-5.110384,6.412867,-6.580257,-5.494974,-0.421133,8.940912,-1.689883,-8.257088,9.921999,-5.891400,-1.371071,-5.413144,7.019968,7.423578,5.465540,5.956293,9.256716,-9.734191,6.494141,1.770998,3.599578,9.272037,7.490095,9.493791,7.386806,7.215165,-1.356088,-8.688286,-8.419549,-8.502124,-2.476537,-4.006898,8.859913,0.027318,2.302464,-7.465019,-3.412041,4.764922,1.810179,-8.628730,-4.802769,1.654658,1.927354,-0.496143,4.222657,4.297551,5.644890,6.393229,1.251706,9.086436,3.979537,0.688631,6.281801,2.096486,4.575627,-1.241282,9.043449,-7.691782,9.479661,4.170544,-4.207471,6.991539,-8.897932,-9.230208,7.141880,-3.999256,2.294994,-0.673757,-2.624415,1.896514,7.896461,-1.298609,6.115795,2.582956,5.883665,8.657795,-1.762015,9.422852,4.077068,-6.600506,4.216282,7.712553,-6.567319,-8.245882,7.931476,-0.354383,3.349472,-5.589773,-5.895413,3.040460,-3.026169,1.743881,2.013799,7.825328,-6.717946,-3.899615,-2.210891,-8.618519,1.538348,-9.312327,-6.091790,-1.750246,4.939791,0.071097,-3.495417,7.538260,1.109565,5.775639,-8.271727,-4.098355,-1.753562,-0.498070,-7.200985,5.421088,8.017373,1.482709,1.440087,5.112438,-7.368412,-2.631613,-0.372146,5.794968,-3.521687,-3.189575,3.567307,9.956751,5.069121,-2.537963,-1.180199,-8.724758,3.881241,6.323208,3.163760,7.311418,4.769132,-4.568679,-9.582184,-2.096277,3.542174,7.673438,0.879121,-8.094749,-0.714348,-1.799994,2.001636,2.723943,-1.125159,1.456673,4.111988,8.696156,-9.626601,-5.999868,1.355652,1.407627,-0.934686,7.408528,9.508538,-3.354039,2.000660,-4.236867,3.487190,3.748363,-4.553050,9.233949,-9.138631,7.824092,4.980484,3.297128,-0.071062,7.267282,5.878280,-7.765186,-9.114142,-7.088596,8.596856,-0.388013,-6.427418,0.941381,-6.982309,4.845103,7.430130,2.114714,-1.076817,-8.575660,0.614830,5.334713,-4.667250,8.445808,9.906771,-9.635852,-3.622304,1.682271,6.970207,-6.922236,-7.120336,-0.331572,-6.298381,-4.936719,-8.312818,4.844020,-4.928137,-6.343721,-7.132988,4.155003,3.893702,-8.764005,6.559246,4.041805,-4.081464,-0.917773,0.587865,0.549297,4.356789,-3.624131,-5.580342,8.964567,6.061072,4.754989,-9.624982,5.844994,6.594820,1.810271,3.270274,8.405121,-2.496206,-4.494987,-8.467069,0.100393,9.595449,3.201264,0.048335,-9.580457,-1.717211,-9.021153,2.729424,-2.122871,-4.534936,4.594968,-3.169323,7.995014,-6.571488,-9.086692,3.273777,-7.681784,-8.926420,-6.754824,8.834232,-7.996298,1.266712,-9.735998,-4.062417,9.528907,-1.555328,-8.318847,2.739756,-2.015540,-6.215368,-3.010857,-7.618444,-6.155905,-7.514558,1.823122,-8.987714,0.640859,-1.637164,-5.385503,-6.269216,3.525403,-6.704052,-5.436713,-1.709616,0.086204,6.252508,-1.982569,9.455863,-4.892597,-4.010356,2.219332,8.786434,-8.726609,-5.158760,-7.120626,-4.141402,5.210896,-4.468709,-8.487844,-5.399393,6.687078,3.399761,-9.037832,-6.355503,-2.770804,-1.540212,4.238330,-3.286938,8.549070,-7.128683,7.401950,-5.576750,6.338535,-2.152934,6.799448,-1.445352,3.164983,-0.148811,-5.082788,-8.314729,7.875348,-8.183253,8.801635,-4.312143,9.651784,-8.463521,8.954768,7.281360,0.962228,-4.943632,5.560426,6.778064,-4.639067,-4.622356,7.796079,3.520574,7.128203,0.446382,-1.349861,4.472964,1.298620,1.821609,-9.732684,7.948214,-7.736915,-8.224681,-1.959408,-8.699522,-9.338395,3.985750,-9.633340,-7.192903,-5.907217,-8.743841,-2.753825,-7.936095,4.563279,-1.014228,0.805429,-2.949246,-1.350156,9.774443,-0.410400,7.223527,-6.568257,-7.731436,-2.042793,-5.902073,8.054683,3.196839,-2.415622,1.691745,5.441804,-1.889583,0.861244,0.025077,7.702631,4.233974,-7.737304,-8.299572,3.252002,5.501076,-9.073359,3.637971,-1.860500,3.100864,-4.516852,5.907830,-7.031083,-1.342163,-3.084174,6.115892,-3.870138,4.257654,-9.680727,0.721835,2.252485,2.152211,-0.534777,0.977701,7.915646,-2.804364,7.428887,-5.528241,0.795307,1.055454,-8.779744,6.211034,2.090288,6.061620,1.639685,-2.097215,-1.270970,-9.427697,-5.071674,4.812259,-9.055263,9.267513,7.906853,0.936755,1.475570,-8.027331,-1.442066,-6.384213,4.738516,3.615078,6.549851,6.402353,7.371326,-2.487443,2.312781,8.719772,3.192697,7.327486,-7.922253,2.000272,7.130615,0.315700,-9.993479,-7.907028,-7.637498,-5.655823,6.463068,4.035039,5.496063,-9.410997,5.121440,-0.678372,-5.459486,-5.952810,-6.558453,-3.633859,2.685598,6.228669], dtype = "float32")#candidate|1227|(450,)|const|float32
call_1226 = relay.TupleGetItem(func_11_call(relay.reshape(const_1227.astype('float32'), [10, 9, 5])), 0)
call_1228 = relay.TupleGetItem(func_14_call(relay.reshape(const_1227.astype('float32'), [10, 9, 5])), 0)
uop_1229 = relay.asin(const_1227.astype('float64')) # shape=(450,)
bop_1236 = relay.minimum(uop_1229.astype('float64'), relay.reshape(call_1226.astype('float64'), relay.shape_of(uop_1229))) # shape=(450,)
bop_1239 = relay.minimum(uop_1229.astype('float64'), relay.reshape(call_1228.astype('float64'), relay.shape_of(uop_1229))) # shape=(450,)
output = relay.Tuple([call_1176,bop_1236,])
output2 = relay.Tuple([call_1177,bop_1239,])
func_1249 = relay.Function([], output)
mod['func_1249'] = func_1249
mod = relay.transform.InferType()(mod)
mutated_mod['func_1249'] = func_1249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1249_call = mutated_mod.get_global_var('func_1249')
call_1250 = func_1249_call()
output = call_1250
func_1251 = relay.Function([], output)
mutated_mod['func_1251'] = func_1251
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1289 = relay.var("var_1289", dtype = "float32", shape = (16, 1, 9))#candidate|1289|(16, 1, 9)|var|float32
uop_1290 = relay.log(var_1289.astype('float32')) # shape=(16, 1, 9)
func_1080_call = mod.get_global_var('func_1080')
func_1081_call = mutated_mod.get_global_var('func_1081')
call_1294 = relay.TupleGetItem(func_1080_call(), 0)
call_1295 = relay.TupleGetItem(func_1081_call(), 0)
func_11_call = mod.get_global_var('func_11')
func_14_call = mutated_mod.get_global_var('func_14')
var_1300 = relay.var("var_1300", dtype = "float32", shape = (450,))#candidate|1300|(450,)|var|float32
call_1299 = relay.TupleGetItem(func_11_call(relay.reshape(var_1300.astype('float32'), [10, 9, 5])), 0)
call_1301 = relay.TupleGetItem(func_14_call(relay.reshape(var_1300.astype('float32'), [10, 9, 5])), 0)
output = relay.Tuple([uop_1290,call_1294,call_1299,var_1300,])
output2 = relay.Tuple([uop_1290,call_1295,call_1301,var_1300,])
func_1310 = relay.Function([var_1289,var_1300,], output)
mod['func_1310'] = func_1310
mod = relay.transform.InferType()(mod)
var_1311 = relay.var("var_1311", dtype = "float32", shape = (16, 1, 9))#candidate|1311|(16, 1, 9)|var|float32
var_1312 = relay.var("var_1312", dtype = "float32", shape = (450,))#candidate|1312|(450,)|var|float32
output = func_1310(var_1311,var_1312,)
func_1313 = relay.Function([var_1311,var_1312,], output)
mutated_mod['func_1313'] = func_1313
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1170_call = mod.get_global_var('func_1170')
func_1172_call = mutated_mod.get_global_var('func_1172')
call_1425 = relay.TupleGetItem(func_1170_call(), 0)
call_1426 = relay.TupleGetItem(func_1172_call(), 0)
func_11_call = mod.get_global_var('func_11')
func_14_call = mutated_mod.get_global_var('func_14')
var_1439 = relay.var("var_1439", dtype = "float32", shape = (450,))#candidate|1439|(450,)|var|float32
call_1438 = relay.TupleGetItem(func_11_call(relay.reshape(var_1439.astype('float32'), [10, 9, 5])), 0)
call_1440 = relay.TupleGetItem(func_14_call(relay.reshape(var_1439.astype('float32'), [10, 9, 5])), 0)
func_1072_call = mod.get_global_var('func_1072')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_1463 = relay.TupleGetItem(func_1072_call(), 2)
call_1464 = relay.TupleGetItem(func_1073_call(), 2)
func_1080_call = mod.get_global_var('func_1080')
func_1081_call = mutated_mod.get_global_var('func_1081')
call_1509 = relay.TupleGetItem(func_1080_call(), 0)
call_1510 = relay.TupleGetItem(func_1081_call(), 0)
func_1072_call = mod.get_global_var('func_1072')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_1512 = relay.TupleGetItem(func_1072_call(), 3)
call_1513 = relay.TupleGetItem(func_1073_call(), 3)
func_1080_call = mod.get_global_var('func_1080')
func_1081_call = mutated_mod.get_global_var('func_1081')
call_1528 = relay.TupleGetItem(func_1080_call(), 0)
call_1529 = relay.TupleGetItem(func_1081_call(), 0)
uop_1544 = relay.acosh(call_1438.astype('float64')) # shape=(10, 9, 5)
uop_1546 = relay.acosh(call_1440.astype('float64')) # shape=(10, 9, 5)
func_804_call = mod.get_global_var('func_804')
func_808_call = mutated_mod.get_global_var('func_808')
const_1551 = relay.const([9.962420,-5.762872,-4.284568,7.615261,-1.636704,4.161129,-2.050924,-0.346450,9.700074,-1.082995,-7.702700,5.335540,8.215376,9.982651,-9.665203,-6.455905,-4.464446,-8.327265,-6.893912,5.017806,5.852200,8.530822,-1.105598,-0.876544,-3.352220,1.475391,-2.588801,1.776407,-6.979573,5.191647,9.153577,-3.521836,-5.673758,4.722556,-2.764173,-8.638429,5.115591,5.409953,8.447378,8.168036,-9.109717,-4.214855,3.755143,-3.324683,-4.054404,-2.838989,8.052464,-0.400803,-3.980192,8.847911,-2.459473,-9.265813,2.316715,9.018302,9.232802,-0.357595,5.796227,-5.271287,8.982951,-5.374888,-4.760865,7.035075,7.221292,-6.838037,1.353411,-9.850177,5.531643,7.713887,4.895732,2.851640,9.397200,-9.874000,-2.935505,8.552577,-5.797595,-9.069669,7.133193,-6.695936,0.156758,-9.902996,-3.575923,-3.783425,2.563664,-0.838447,-8.287424,0.837549,-7.295035,-6.937479,-3.397630,-0.263906,-6.769022,-2.290664,-6.740323,-7.610763,7.701636,4.352309,-8.685681,0.917330,0.942934,-1.616231,8.791909,-9.787131,3.513285,-0.774841,-7.248976,-6.778341,9.059881,-3.732186,-1.519143,1.841733,9.640600,1.806785,-3.473542,8.466071,0.148084,0.902624,0.337982,-7.915942,3.766248,3.217020,3.186444,-9.714521,-5.632313,-5.590148,9.702026,-6.630894,-6.947676,-1.944157,-0.125581,9.966097,1.540193,-1.424018,-4.543773,-1.027229,1.635008,5.198899,4.848653,-5.653121,7.349654,-0.167071,-4.420571,0.020966,5.076821,-1.660905,-8.138971,1.548376,-9.496452,-1.621480,-4.082838,-1.344562,-7.437490,-8.117071,9.840208,1.188883,1.839589,-3.993644,-7.254994,3.428256,1.771852,3.832075,7.451539,-7.528905,-4.862486,-3.479970,6.351901,8.406876,-6.698381,7.152581,-4.537156,-5.509795,1.953203,4.236183,6.004095,5.743194,-5.173165,-2.527616,5.927435,-8.240428,6.597644,-9.612689,6.091510,9.985370,7.719880,-3.565668,9.752875,3.022844,0.541017,6.931032,0.875269,3.425467,5.596925,2.678528], dtype = "float32")#candidate|1551|(192,)|const|float32
call_1550 = relay.TupleGetItem(func_804_call(relay.reshape(const_1551.astype('float32'), [6, 2, 16]), relay.reshape(const_1551.astype('float32'), [6, 2, 16]), ), 0)
call_1552 = relay.TupleGetItem(func_808_call(relay.reshape(const_1551.astype('float32'), [6, 2, 16]), relay.reshape(const_1551.astype('float32'), [6, 2, 16]), ), 0)
output = relay.Tuple([call_1425,var_1439,call_1463,call_1509,call_1512,call_1528,uop_1544,call_1550,const_1551,])
output2 = relay.Tuple([call_1426,var_1439,call_1464,call_1510,call_1513,call_1529,uop_1546,call_1552,const_1551,])
func_1561 = relay.Function([var_1439,], output)
mod['func_1561'] = func_1561
mod = relay.transform.InferType()(mod)
var_1562 = relay.var("var_1562", dtype = "float32", shape = (450,))#candidate|1562|(450,)|var|float32
output = func_1561(var_1562)
func_1563 = relay.Function([var_1562], output)
mutated_mod['func_1563'] = func_1563
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1633 = relay.var("var_1633", dtype = "float64", shape = (8, 3, 11))#candidate|1633|(8, 3, 11)|var|float64
uop_1634 = relay.sigmoid(var_1633.astype('float64')) # shape=(8, 3, 11)
func_1080_call = mod.get_global_var('func_1080')
func_1081_call = mutated_mod.get_global_var('func_1081')
call_1648 = relay.TupleGetItem(func_1080_call(), 0)
call_1649 = relay.TupleGetItem(func_1081_call(), 0)
func_1170_call = mod.get_global_var('func_1170')
func_1172_call = mutated_mod.get_global_var('func_1172')
call_1651 = relay.TupleGetItem(func_1170_call(), 0)
call_1652 = relay.TupleGetItem(func_1172_call(), 0)
output = relay.Tuple([uop_1634,call_1648,call_1651,])
output2 = relay.Tuple([uop_1634,call_1649,call_1652,])
func_1666 = relay.Function([var_1633,], output)
mod['func_1666'] = func_1666
mod = relay.transform.InferType()(mod)
mutated_mod['func_1666'] = func_1666
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1667 = relay.var("var_1667", dtype = "float64", shape = (8, 3, 11))#candidate|1667|(8, 3, 11)|var|float64
func_1666_call = mutated_mod.get_global_var('func_1666')
call_1668 = func_1666_call(var_1667)
output = call_1668
func_1669 = relay.Function([var_1667], output)
mutated_mod['func_1669'] = func_1669
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1072_call = mod.get_global_var('func_1072')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_1673 = relay.TupleGetItem(func_1072_call(), 1)
call_1674 = relay.TupleGetItem(func_1073_call(), 1)
output = call_1673
output2 = call_1674
func_1677 = relay.Function([], output)
mod['func_1677'] = func_1677
mod = relay.transform.InferType()(mod)
output = func_1677()
func_1678 = relay.Function([], output)
mutated_mod['func_1678'] = func_1678
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1721 = relay.var("var_1721", dtype = "float64", shape = ())#candidate|1721|()|var|float64
const_1722 = relay.const([[[-2.864123,-7.874461,-9.177288,-3.889557,9.785929,-3.879934],[-6.864872,-4.987130,-2.202097,5.574800,6.289691,0.641482],[4.606279,-3.784349,0.337923,-2.177127,-6.968171,7.608657],[5.669866,2.213351,-4.879752,4.552726,-3.816921,4.510573],[4.327615,2.050590,-2.985516,1.096232,5.104982,5.344796],[-7.114155,-4.849791,3.169635,8.141435,5.912701,4.817004],[5.005710,-4.996393,-7.753005,-5.601238,-4.832861,-0.111543],[-3.544811,-7.091640,2.070574,1.488140,7.065749,-4.589427]]], dtype = "float64")#candidate|1722|(1, 8, 6)|const|float64
bop_1723 = relay.power(var_1721.astype('float64'), const_1722.astype('float64')) # shape=(1, 8, 6)
func_1080_call = mod.get_global_var('func_1080')
func_1081_call = mutated_mod.get_global_var('func_1081')
call_1734 = relay.TupleGetItem(func_1080_call(), 0)
call_1735 = relay.TupleGetItem(func_1081_call(), 0)
bop_1736 = relay.minimum(var_1721.astype('uint8'), bop_1723.astype('uint8')) # shape=(1, 8, 6)
output = relay.Tuple([call_1734,bop_1736,])
output2 = relay.Tuple([call_1735,bop_1736,])
func_1742 = relay.Function([var_1721,], output)
mod['func_1742'] = func_1742
mod = relay.transform.InferType()(mod)
mutated_mod['func_1742'] = func_1742
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1743 = relay.var("var_1743", dtype = "float64", shape = ())#candidate|1743|()|var|float64
func_1742_call = mutated_mod.get_global_var('func_1742')
call_1744 = func_1742_call(var_1743)
output = call_1744
func_1745 = relay.Function([var_1743], output)
mutated_mod['func_1745'] = func_1745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1072_call = mod.get_global_var('func_1072')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_1764 = relay.TupleGetItem(func_1072_call(), 1)
call_1765 = relay.TupleGetItem(func_1073_call(), 1)
output = call_1764
output2 = call_1765
func_1770 = relay.Function([], output)
mod['func_1770'] = func_1770
mod = relay.transform.InferType()(mod)
mutated_mod['func_1770'] = func_1770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1770_call = mutated_mod.get_global_var('func_1770')
call_1771 = func_1770_call()
output = call_1771
func_1772 = relay.Function([], output)
mutated_mod['func_1772'] = func_1772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1170_call = mod.get_global_var('func_1170')
func_1172_call = mutated_mod.get_global_var('func_1172')
call_1775 = relay.TupleGetItem(func_1170_call(), 0)
call_1776 = relay.TupleGetItem(func_1172_call(), 0)
func_1677_call = mod.get_global_var('func_1677')
func_1678_call = mutated_mod.get_global_var('func_1678')
call_1780 = func_1677_call()
call_1781 = func_1677_call()
bop_1791 = relay.multiply(call_1775.astype('int8'), call_1780.astype('int8')) # shape=(3, 1, 9)
bop_1794 = relay.multiply(call_1776.astype('int8'), call_1781.astype('int8')) # shape=(3, 1, 9)
bop_1795 = relay.right_shift(bop_1791.astype('int16'), call_1775.astype('int16')) # shape=(3, 1, 9)
bop_1798 = relay.right_shift(bop_1794.astype('int16'), call_1776.astype('int16')) # shape=(3, 1, 9)
bop_1799 = relay.greater(call_1780.astype('bool'), relay.reshape(bop_1791.astype('bool'), relay.shape_of(call_1780))) # shape=(3, 1, 9)
bop_1802 = relay.greater(call_1781.astype('bool'), relay.reshape(bop_1794.astype('bool'), relay.shape_of(call_1781))) # shape=(3, 1, 9)
bop_1844 = relay.minimum(bop_1791.astype('uint32'), relay.reshape(bop_1799.astype('uint32'), relay.shape_of(bop_1791))) # shape=(3, 1, 9)
bop_1847 = relay.minimum(bop_1794.astype('uint32'), relay.reshape(bop_1802.astype('uint32'), relay.shape_of(bop_1794))) # shape=(3, 1, 9)
uop_1852 = relay.acos(bop_1844.astype('float64')) # shape=(3, 1, 9)
uop_1854 = relay.acos(bop_1847.astype('float64')) # shape=(3, 1, 9)
func_1107_call = mod.get_global_var('func_1107')
func_1108_call = mutated_mod.get_global_var('func_1108')
call_1859 = relay.TupleGetItem(func_1107_call(), 0)
call_1860 = relay.TupleGetItem(func_1108_call(), 0)
output = relay.Tuple([bop_1795,uop_1852,call_1859,])
output2 = relay.Tuple([bop_1798,uop_1854,call_1860,])
func_1867 = relay.Function([], output)
mod['func_1867'] = func_1867
mod = relay.transform.InferType()(mod)
output = func_1867()
func_1868 = relay.Function([], output)
mutated_mod['func_1868'] = func_1868
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1677_call = mod.get_global_var('func_1677')
func_1678_call = mutated_mod.get_global_var('func_1678')
call_1871 = func_1677_call()
call_1872 = func_1677_call()
output = relay.Tuple([call_1871,])
output2 = relay.Tuple([call_1872,])
func_1884 = relay.Function([], output)
mod['func_1884'] = func_1884
mod = relay.transform.InferType()(mod)
output = func_1884()
func_1885 = relay.Function([], output)
mutated_mod['func_1885'] = func_1885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1249_call = mod.get_global_var('func_1249')
func_1251_call = mutated_mod.get_global_var('func_1251')
call_2004 = relay.TupleGetItem(func_1249_call(), 0)
call_2005 = relay.TupleGetItem(func_1251_call(), 0)
output = relay.Tuple([call_2004,])
output2 = relay.Tuple([call_2005,])
func_2016 = relay.Function([], output)
mod['func_2016'] = func_2016
mod = relay.transform.InferType()(mod)
mutated_mod['func_2016'] = func_2016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2016_call = mutated_mod.get_global_var('func_2016')
call_2017 = func_2016_call()
output = call_2017
func_2018 = relay.Function([], output)
mutated_mod['func_2018'] = func_2018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1677_call = mod.get_global_var('func_1677')
func_1678_call = mutated_mod.get_global_var('func_1678')
call_2038 = func_1677_call()
call_2039 = func_1677_call()
output = relay.Tuple([call_2038,])
output2 = relay.Tuple([call_2039,])
func_2042 = relay.Function([], output)
mod['func_2042'] = func_2042
mod = relay.transform.InferType()(mod)
output = func_2042()
func_2043 = relay.Function([], output)
mutated_mod['func_2043'] = func_2043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1770_call = mod.get_global_var('func_1770')
func_1772_call = mutated_mod.get_global_var('func_1772')
call_2075 = func_1770_call()
call_2076 = func_1770_call()
output = relay.Tuple([call_2075,])
output2 = relay.Tuple([call_2076,])
func_2081 = relay.Function([], output)
mod['func_2081'] = func_2081
mod = relay.transform.InferType()(mod)
output = func_2081()
func_2082 = relay.Function([], output)
mutated_mod['func_2082'] = func_2082
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2129 = relay.var("var_2129", dtype = "int8", shape = (7, 10, 11))#candidate|2129|(7, 10, 11)|var|int8
var_2130 = relay.var("var_2130", dtype = "int8", shape = (7, 10, 11))#candidate|2130|(7, 10, 11)|var|int8
bop_2131 = relay.equal(var_2129.astype('bool'), relay.reshape(var_2130.astype('bool'), relay.shape_of(var_2129))) # shape=(7, 10, 11)
func_804_call = mod.get_global_var('func_804')
func_808_call = mutated_mod.get_global_var('func_808')
const_2139 = relay.const([0.383322,-2.601320,6.161699,-7.738827,8.695176,8.364527,5.016581,0.680843,-2.688021,2.209338,6.616909,8.673630,7.400664,-6.977434,-1.659480,4.365254,-6.828673,3.522192,6.801504,-6.263317,-7.359934,-3.858157,2.463830,-7.274431,-1.078854,8.913530,-4.077099,5.775538,8.470670,-1.524793,1.795897,3.946554,0.610545,4.603603,-4.560959,0.744104,3.433711,-8.377634,1.280052,-0.827033,-1.821450,5.106815,-3.751056,5.432126,6.459167,-1.423563,9.390754,-4.854292,-3.426772,2.721442,-1.553798,4.247149,6.242943,-5.365605,6.670728,-2.217017,-7.679980,-4.783528,-7.230650,-7.189388,-3.916266,-3.907906,6.834432,-7.651466,-1.246344,-1.396307,5.841123,-9.925405,-0.638275,2.414246,-5.629444,3.541750,-2.033860,7.590586,8.827813,-9.405627,-6.284734,9.710331,9.157984,-4.348663,-0.577797,-4.215502,-8.219696,-1.445485,-1.797164,-8.112579,8.881185,9.002010,-1.794482,-7.541272,6.261269,6.613248,1.652940,5.119067,-5.921501,-2.036170,-9.807547,-8.099151,0.312139,0.889317,7.049630,-5.866171,-4.233755,-2.225569,0.500100,-9.713191,2.473917,-9.042578,2.308671,0.614332,9.327800,-0.823557,7.147248,2.520349,0.191880,-1.916330,-1.312826,2.777654,-2.392724,6.146280,-1.598282,-7.079799,9.875430,-9.225441,-5.049338,2.776674,7.278434,-8.704004,-8.198229,5.454172,-5.857699,-7.984329,2.578809,1.341908,2.325290,6.887936,9.181679,3.560901,-5.687802,8.508490,-7.558278,9.799733,-6.060068,-4.077258,8.640273,-0.503189,0.673862,-2.965214,-5.429652,-1.766212,7.023818,5.847802,-4.703858,1.475236,-0.717219,9.714148,0.545762,-0.714708,-9.865136,3.311847,-8.064769,-1.141242,-0.482404,-7.838738,-8.595455,0.045252,-8.714130,-2.787255,7.617906,-8.110333,-6.341213,-2.296112,-3.240933,0.882907,5.020771,-4.896009,-2.782098,1.286344,7.053419,9.442056,7.276570,7.511560,6.472361,-8.433678,-5.468934,-9.483259,-4.260153,-1.167532,2.815244,-3.749551,-4.176582,4.734384], dtype = "float32")#candidate|2139|(192,)|const|float32
call_2138 = relay.TupleGetItem(func_804_call(relay.reshape(const_2139.astype('float32'), [6, 2, 16]), relay.reshape(const_2139.astype('float32'), [6, 2, 16]), ), 0)
call_2140 = relay.TupleGetItem(func_808_call(relay.reshape(const_2139.astype('float32'), [6, 2, 16]), relay.reshape(const_2139.astype('float32'), [6, 2, 16]), ), 0)
output = relay.Tuple([bop_2131,call_2138,const_2139,])
output2 = relay.Tuple([bop_2131,call_2140,const_2139,])
func_2147 = relay.Function([var_2129,var_2130,], output)
mod['func_2147'] = func_2147
mod = relay.transform.InferType()(mod)
mutated_mod['func_2147'] = func_2147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2147_call = mutated_mod.get_global_var('func_2147')
var_2149 = relay.var("var_2149", dtype = "int8", shape = (7, 10, 11))#candidate|2149|(7, 10, 11)|var|int8
var_2150 = relay.var("var_2150", dtype = "int8", shape = (7, 10, 11))#candidate|2150|(7, 10, 11)|var|int8
call_2148 = func_2147_call(var_2149,var_2150,)
output = call_2148
func_2151 = relay.Function([var_2149,var_2150,], output)
mutated_mod['func_2151'] = func_2151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2016_call = mod.get_global_var('func_2016')
func_2018_call = mutated_mod.get_global_var('func_2018')
call_2186 = relay.TupleGetItem(func_2016_call(), 0)
call_2187 = relay.TupleGetItem(func_2018_call(), 0)
func_2147_call = mod.get_global_var('func_2147')
func_2151_call = mutated_mod.get_global_var('func_2151')
var_2193 = relay.var("var_2193", dtype = "int8", shape = (7, 110))#candidate|2193|(7, 110)|var|int8
call_2192 = relay.TupleGetItem(func_2147_call(relay.reshape(var_2193.astype('int8'), [7, 10, 11]), relay.reshape(var_2193.astype('int8'), [7, 10, 11]), ), 0)
call_2194 = relay.TupleGetItem(func_2151_call(relay.reshape(var_2193.astype('int8'), [7, 10, 11]), relay.reshape(var_2193.astype('int8'), [7, 10, 11]), ), 0)
func_1742_call = mod.get_global_var('func_1742')
func_1745_call = mutated_mod.get_global_var('func_1745')
call_2196 = relay.TupleGetItem(func_1742_call(relay.reshape(call_2186.astype('float64'), [])), 0)
call_2197 = relay.TupleGetItem(func_1745_call(relay.reshape(call_2186.astype('float64'), [])), 0)
func_2081_call = mod.get_global_var('func_2081')
func_2082_call = mutated_mod.get_global_var('func_2082')
call_2200 = relay.TupleGetItem(func_2081_call(), 0)
call_2201 = relay.TupleGetItem(func_2082_call(), 0)
output = relay.Tuple([call_2186,call_2192,var_2193,call_2196,call_2200,])
output2 = relay.Tuple([call_2187,call_2194,var_2193,call_2197,call_2201,])
func_2204 = relay.Function([var_2193,], output)
mod['func_2204'] = func_2204
mod = relay.transform.InferType()(mod)
var_2205 = relay.var("var_2205", dtype = "int8", shape = (7, 110))#candidate|2205|(7, 110)|var|int8
output = func_2204(var_2205)
func_2206 = relay.Function([var_2205], output)
mutated_mod['func_2206'] = func_2206
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2217 = relay.var("var_2217", dtype = "float64", shape = (8, 10, 13))#candidate|2217|(8, 10, 13)|var|float64
uop_2218 = relay.exp(var_2217.astype('float64')) # shape=(8, 10, 13)
func_253_call = mod.get_global_var('func_253')
func_255_call = mutated_mod.get_global_var('func_255')
var_2230 = relay.var("var_2230", dtype = "uint32", shape = (576,))#candidate|2230|(576,)|var|uint32
call_2229 = func_253_call(relay.reshape(var_2230.astype('uint32'), [3, 16, 12]))
call_2231 = func_253_call(relay.reshape(var_2230.astype('uint32'), [3, 16, 12]))
func_1677_call = mod.get_global_var('func_1677')
func_1678_call = mutated_mod.get_global_var('func_1678')
call_2233 = func_1677_call()
call_2234 = func_1677_call()
func_416_call = mod.get_global_var('func_416')
func_419_call = mutated_mod.get_global_var('func_419')
const_2239 = relay.const(-5, dtype = "int16")#candidate|2239|()|const|int16
call_2238 = func_416_call(relay.reshape(const_2239.astype('int16'), []), relay.reshape(call_2233.astype('int16'), [3, 1, 9]), )
call_2240 = func_416_call(relay.reshape(const_2239.astype('int16'), []), relay.reshape(call_2233.astype('int16'), [3, 1, 9]), )
func_1561_call = mod.get_global_var('func_1561')
func_1563_call = mutated_mod.get_global_var('func_1563')
const_2245 = relay.const([[-1.278905,2.572706,7.187217,-6.536541,-2.806071,6.173604,-3.346441,-7.910357,3.269197,1.011129,-2.597458,-8.501839,-3.608035,-8.404626,-8.211445,-7.358336,-3.778723,-3.281284,-8.890833,-0.714273,-3.993553,-0.116389,8.836742,-2.907405,-2.294815,-3.977369,-0.393328,7.028911,-0.163711,1.061311,-8.637011,-3.679672,2.314441,-6.956332,7.604766,3.328548,8.629665,-2.463316,-4.475716,9.689467,0.260029,3.445041,3.672335,-9.855387,-4.003728,-7.911222,-1.265997,8.557845,8.047375,7.352100,-0.625741,-1.493642,-1.374203,7.435210,-6.792560,-4.754734,-2.444374,2.897013,-2.537235,5.948859,-0.737420,-0.876849,-8.924429,-5.076572,2.449344,-6.827009,-7.637506,8.266059,-6.451328,-0.673367,-6.976401,-6.857222,-7.776744,-3.772259,0.072180,-0.986612,9.031735,-0.835103,-6.457404,9.955759,2.243310,-6.764834,5.680101,-1.721738,-4.684025,-0.234778,2.806557,6.382732,-2.444732,8.362298],[1.201281,5.655600,-3.237535,6.479786,2.396944,-7.059193,-7.701533,-2.621309,3.266839,6.139478,5.256469,-7.999017,-4.222003,9.443643,1.824806,4.238378,-0.861214,3.674426,-4.398497,0.667902,6.884065,-8.649841,-9.763205,0.711518,-0.619826,6.332926,-4.635484,-7.369108,3.297130,-2.795305,-6.293632,-3.651713,-3.062551,4.786835,-8.811784,-7.719370,4.353199,1.422254,-9.850585,5.902211,-3.546988,-3.516554,-0.493617,7.170930,-0.170213,-8.964421,2.274081,4.880445,-6.383516,2.175914,-7.266032,-4.022556,-7.375650,8.487394,3.758019,7.698213,-9.814458,-3.160999,6.488028,-2.386187,7.475532,-8.452941,0.589861,6.441578,9.363583,-6.601976,-2.115148,8.845305,7.713868,0.748270,1.052615,-9.247658,4.430633,-2.463498,-5.404853,-6.238856,6.502895,1.544039,1.799946,-7.332964,9.402264,-4.569434,6.428491,-1.565092,-4.747626,2.717565,5.657899,5.674808,0.288961,6.130045],[3.731529,9.154722,-7.349096,3.995360,0.524158,-4.603141,9.723755,6.355935,-7.106297,9.388283,6.826925,-6.270386,-4.382516,8.156849,3.738268,6.068724,9.606580,0.007054,9.850017,3.422745,-7.245927,3.316568,-6.027717,4.661674,0.536963,4.007436,4.030089,6.833716,-7.349676,0.646910,8.902870,-6.751753,-6.106528,-4.985293,-3.466187,-8.439252,-6.287153,-4.898758,-8.923951,1.697394,-9.646746,6.995026,2.277254,0.429959,0.451113,1.049278,-2.982893,0.892718,-7.229106,-6.705944,1.952494,7.391189,7.698641,-6.437904,9.405539,1.459630,9.727620,-0.253294,0.515521,-4.477397,-5.253138,5.131193,1.567843,7.535954,-7.237954,-1.337929,0.659047,2.400743,-9.790041,-7.205550,-6.041914,8.384062,-9.719046,-8.762291,-8.515508,2.439957,-6.200087,0.846250,9.104988,2.134751,-7.004814,-2.888992,-3.895214,-9.986058,1.560708,-1.272730,-8.115585,6.596211,1.909429,-0.139816],[-2.874092,7.500850,-6.487939,-8.838259,0.710103,-7.816103,-0.827717,6.176178,-5.108478,4.668028,1.728550,5.379910,3.584831,-2.082090,-3.583001,-0.170567,-6.553642,-9.759444,-8.703644,8.186163,-3.759072,-1.108022,-3.908710,6.001785,4.495638,-9.139543,9.594343,5.573358,8.617927,4.805788,-4.952196,-7.274240,6.662888,-1.103677,-3.886203,-9.918976,6.261181,4.699734,-7.601808,-0.847708,0.369900,-6.603500,4.344924,8.198314,-4.694711,-7.640630,3.656429,2.105269,4.957905,-5.147466,0.188366,1.537492,3.059763,-5.413223,4.478675,-3.241565,-4.074564,4.640096,-2.227883,-3.561459,-2.116396,5.206354,6.843807,-2.295226,-9.300489,-1.790685,4.117535,-6.317669,-0.283661,4.734133,-4.543709,-4.578835,-9.618770,-1.932512,8.930642,6.265873,2.460078,0.556513,-4.986011,-7.180239,-6.359108,-8.694049,-0.128169,9.965603,-0.153218,-5.193013,-6.000686,5.596414,2.014658,5.731215],[-4.342253,-1.355245,2.791937,-6.796850,7.634069,1.177965,-5.944179,-1.500385,-7.637212,6.446717,-0.348118,9.200513,8.892229,7.137849,-0.368950,4.002133,-7.702057,3.395666,9.343478,7.152967,-5.241530,-7.963373,-5.547070,2.020290,-1.948628,6.250934,-9.724006,4.560350,6.199681,-5.916815,3.402269,-8.082552,0.773822,-3.716608,-7.205765,-3.354258,-7.074308,2.838130,8.859119,4.059969,2.522354,-7.261133,-2.971461,7.108906,-2.376952,8.187114,0.756776,2.789553,3.966210,2.966569,4.524655,-9.559579,2.462921,5.178295,-7.062355,-5.432980,0.127366,-9.448464,1.233140,-1.003207,5.905275,0.406480,3.361487,-0.578464,-0.350601,-8.950208,2.837321,4.839089,-2.980620,5.628137,-0.665140,1.305561,-3.831485,4.006019,6.053349,7.697665,4.366457,-0.784905,-0.456710,-8.540504,-4.484089,-0.200677,1.627354,-5.510664,-7.009949,0.592533,-9.205140,8.534341,-2.357431,-3.842757]], dtype = "float32")#candidate|2245|(5, 90)|const|float32
call_2244 = relay.TupleGetItem(func_1561_call(relay.reshape(const_2245.astype('float32'), [450,])), 0)
call_2246 = relay.TupleGetItem(func_1563_call(relay.reshape(const_2245.astype('float32'), [450,])), 0)
func_1677_call = mod.get_global_var('func_1677')
func_1678_call = mutated_mod.get_global_var('func_1678')
call_2253 = func_1677_call()
call_2254 = func_1677_call()
func_1021_call = mod.get_global_var('func_1021')
func_1026_call = mutated_mod.get_global_var('func_1026')
var_2258 = relay.var("var_2258", dtype = "float32", shape = (135,))#candidate|2258|(135,)|var|float32
call_2257 = relay.TupleGetItem(func_1021_call(relay.reshape(var_2258.astype('float32'), [9, 3, 5]), relay.reshape(const_2239.astype('int16'), []), relay.reshape(const_2245.astype('float32'), [450,]), relay.reshape(var_2258.astype('float32'), [9, 3, 5]), ), 6)
call_2259 = relay.TupleGetItem(func_1026_call(relay.reshape(var_2258.astype('float32'), [9, 3, 5]), relay.reshape(const_2239.astype('int16'), []), relay.reshape(const_2245.astype('float32'), [450,]), relay.reshape(var_2258.astype('float32'), [9, 3, 5]), ), 6)
func_1884_call = mod.get_global_var('func_1884')
func_1885_call = mutated_mod.get_global_var('func_1885')
call_2265 = relay.TupleGetItem(func_1884_call(), 0)
call_2266 = relay.TupleGetItem(func_1885_call(), 0)
output = relay.Tuple([uop_2218,call_2229,var_2230,call_2233,call_2238,const_2239,call_2244,const_2245,call_2253,call_2257,var_2258,call_2265,])
output2 = relay.Tuple([uop_2218,call_2231,var_2230,call_2234,call_2240,const_2239,call_2246,const_2245,call_2254,call_2259,var_2258,call_2266,])
func_2272 = relay.Function([var_2217,var_2230,var_2258,], output)
mod['func_2272'] = func_2272
mod = relay.transform.InferType()(mod)
var_2273 = relay.var("var_2273", dtype = "float64", shape = (8, 10, 13))#candidate|2273|(8, 10, 13)|var|float64
var_2274 = relay.var("var_2274", dtype = "uint32", shape = (576,))#candidate|2274|(576,)|var|uint32
var_2275 = relay.var("var_2275", dtype = "float32", shape = (135,))#candidate|2275|(135,)|var|float32
output = func_2272(var_2273,var_2274,var_2275,)
func_2276 = relay.Function([var_2273,var_2274,var_2275,], output)
mutated_mod['func_2276'] = func_2276
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2322 = relay.var("var_2322", dtype = "float64", shape = (15, 3, 15))#candidate|2322|(15, 3, 15)|var|float64
uop_2323 = relay.atanh(var_2322.astype('float64')) # shape=(15, 3, 15)
func_2042_call = mod.get_global_var('func_2042')
func_2043_call = mutated_mod.get_global_var('func_2043')
call_2325 = relay.TupleGetItem(func_2042_call(), 0)
call_2326 = relay.TupleGetItem(func_2043_call(), 0)
func_1310_call = mod.get_global_var('func_1310')
func_1313_call = mutated_mod.get_global_var('func_1313')
var_2333 = relay.var("var_2333", dtype = "float32", shape = (144,))#candidate|2333|(144,)|var|float32
const_2334 = relay.const([-2.631471,-6.425092,1.958551,2.548497,7.575486,-2.485311,-3.720061,6.047844,9.300347,-9.181001,-2.656481,-6.721368,2.215156,3.420872,1.022594,-3.668133,4.971877,9.131470,-9.197946,2.746795,3.973204,-3.622712,-9.366530,6.439286,-9.111484,-3.228658,9.803144,4.439270,2.460110,0.991179,-5.953674,8.927581,-1.856134,4.286842,2.510015,-2.632472,-7.569457,-4.746012,-7.798795,-8.576649,3.477317,-7.029201,3.993929,-9.334145,-4.860495,-6.867788,9.610052,2.517783,-8.602678,-5.662211,9.913974,-4.557629,0.239119,-0.393395,8.744078,4.525358,2.713451,2.215914,7.535935,6.251279,2.889898,5.009100,6.736190,-9.278985,1.897841,-9.222728,5.913588,-3.505165,1.374799,6.346286,-4.118819,-0.054545,-0.039573,-3.274955,6.274161,4.958584,7.424461,3.701338,1.632890,-6.120032,7.626032,8.111434,-7.707541,9.153131,-3.087610,-6.901065,2.164375,-6.111928,-5.564578,-8.768498,1.302798,-3.286039,-1.638252,0.227069,6.347780,-9.311606,-7.375556,0.801739,3.868508,7.514434,2.368515,-5.848401,-5.929482,-5.841532,-8.222554,-8.362575,5.007532,-8.226336,-8.857516,9.148715,-1.385631,-0.944920,-9.546050,5.980197,9.141104,0.600635,-6.643092,5.516031,8.247615,3.699484,-5.048300,0.263672,-1.369973,3.969650,5.851769,-3.779285,-6.871692,5.845831,-3.445342,8.645599,9.244442,7.858725,-9.606127,-6.579769,-8.748503,2.770142,4.380540,-9.099888,3.486301,-2.044436,0.652835,-8.189712,-7.412493,-4.105487,-2.108848,-7.133334,-7.494302,0.124466,-1.144982,-7.889960,4.709676,-9.109713,-0.927707,-3.686317,-9.992983,3.151916,6.019581,-4.104880,9.536062,-3.771795,-6.680054,7.761420,-0.264557,4.347134,-5.073223,-1.394899,-9.501980,-8.635435,7.405525,-3.455348,7.789775,3.630447,0.387814,-5.637673,-0.796888,-7.749174,0.746959,-6.128840,-9.228130,9.695642,3.809988,-1.069412,-4.816864,2.842261,2.975596,1.838960,5.655179,8.553329,-6.254280,2.523771,-3.186285,4.102611,8.095963,-0.515140,-1.828908,-5.802038,3.888770,5.946258,4.795705,9.129972,-3.464566,6.903829,-3.990900,-1.234546,9.175912,8.514553,6.340294,5.012624,-8.792160,-5.413978,8.422725,6.164196,9.259505,-9.881268,3.345992,8.440660,4.489564,9.754640,4.954544,-5.841630,0.141120,-6.242368,4.212458,3.118569,0.073307,-3.930585,-6.356204,6.925230,-9.712433,-6.502630,-7.314045,3.108244,-1.427678,1.366823,-0.321457,-5.114969,7.926651,-9.824338,8.723753,5.194157,4.192191,6.554132,0.589732,6.346115,1.217610,8.364480,5.014007,1.618903,2.690349,0.326505,-2.288991,5.894186,-7.342663,-5.482095,0.410072,7.346139,8.666868,-2.761777,0.903824,-4.128700,5.593256,-9.788767,-7.229115,-6.584246,-9.290547,9.736304,-5.450889,1.403632,-0.879556,-1.079297,3.698256,-1.816489,-2.390970,3.920451,-2.783653,-1.677584,2.902876,-4.871488,-9.473944,1.448784,-2.272602,-4.777491,4.715450,-9.235172,8.517068,5.391912,-2.333491,-9.123328,-0.112365,-0.961726,9.521784,-4.395313,-2.150233,3.270330,9.391999,1.462396,5.978085,-9.113046,5.051757,0.013602,0.081215,5.020561,-2.380315,3.060926,3.695610,-5.936409,-1.474821,6.857357,8.887651,-4.216564,7.086967,1.269792,5.987966,6.628913,-6.863086,6.080484,5.810357,1.686147,-7.922127,-6.135071,-7.317155,0.299880,1.521408,9.517171,4.145919,-2.372673,-7.714772,4.172537,8.668094,-3.535847,3.161439,-6.675766,6.819110,0.213582,-8.603333,2.721769,-0.868528,6.521431,-6.902185,-2.472195,-3.641054,-9.334357,-3.907214,-1.489268,5.094881,6.620593,1.266987,0.376699,1.859320,-4.956796,2.648255,7.926889,-8.377728,8.749004,0.276860,-4.564747,-7.552084,-5.506851,7.049070,2.633102,-5.336831,7.928023,-0.227972,-3.501833,3.902249,3.680586,-1.872889,-1.748048,6.773160,4.193936,-4.600424,1.257147,6.327670,2.153900,-7.291776,7.254296,-7.397731,-9.613703,6.761182,-5.576876,-1.512772,1.561455,-5.251715,7.680435,-6.375912,6.383373,2.942075,1.179536,-2.982777,7.155623,0.869851,7.796929,4.183769,-8.070322,-3.637941,-4.130718,-7.634105,-5.048168,8.466652,2.153002,-2.687784,-9.125482,7.381131,-5.049544,4.364372,-3.604289,-2.820801,-9.566893,-8.007472,6.835450,0.297258,1.776921,9.825496,9.567751,8.477480,-4.275282,4.718089,3.634063,8.437363,-1.689404,0.672976,8.668793,2.015887,-6.164892,5.449891,-0.053257,5.672964,-2.724572,0.882894,6.249433,-5.492949,0.340572,5.370275,-8.329288,-0.761048,7.370582,-1.029876,-9.332703,-1.882708,1.887937,-2.531925,-0.988148,0.999863,-8.353599,-4.177279,2.202579,-6.851460,-4.995121,-9.341688,-5.854906], dtype = "float32")#candidate|2334|(450,)|const|float32
call_2332 = relay.TupleGetItem(func_1310_call(relay.reshape(var_2333.astype('float32'), [16, 1, 9]), relay.reshape(const_2334.astype('float32'), [450,]), ), 3)
call_2335 = relay.TupleGetItem(func_1313_call(relay.reshape(var_2333.astype('float32'), [16, 1, 9]), relay.reshape(const_2334.astype('float32'), [450,]), ), 3)
output = relay.Tuple([uop_2323,call_2325,call_2332,var_2333,const_2334,])
output2 = relay.Tuple([uop_2323,call_2326,call_2335,var_2333,const_2334,])
func_2340 = relay.Function([var_2322,var_2333,], output)
mod['func_2340'] = func_2340
mod = relay.transform.InferType()(mod)
var_2341 = relay.var("var_2341", dtype = "float64", shape = (15, 3, 15))#candidate|2341|(15, 3, 15)|var|float64
var_2342 = relay.var("var_2342", dtype = "float32", shape = (144,))#candidate|2342|(144,)|var|float32
output = func_2340(var_2341,var_2342,)
func_2343 = relay.Function([var_2341,var_2342,], output)
mutated_mod['func_2343'] = func_2343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1107_call = mod.get_global_var('func_1107')
func_1108_call = mutated_mod.get_global_var('func_1108')
call_2367 = relay.TupleGetItem(func_1107_call(), 0)
call_2368 = relay.TupleGetItem(func_1108_call(), 0)
func_1677_call = mod.get_global_var('func_1677')
func_1678_call = mutated_mod.get_global_var('func_1678')
call_2381 = func_1677_call()
call_2382 = func_1677_call()
output = relay.Tuple([call_2367,call_2381,])
output2 = relay.Tuple([call_2368,call_2382,])
func_2386 = relay.Function([], output)
mod['func_2386'] = func_2386
mod = relay.transform.InferType()(mod)
mutated_mod['func_2386'] = func_2386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2386_call = mutated_mod.get_global_var('func_2386')
call_2387 = func_2386_call()
output = call_2387
func_2388 = relay.Function([], output)
mutated_mod['func_2388'] = func_2388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1170_call = mod.get_global_var('func_1170')
func_1172_call = mutated_mod.get_global_var('func_1172')
call_2449 = relay.TupleGetItem(func_1170_call(), 0)
call_2450 = relay.TupleGetItem(func_1172_call(), 0)
output = relay.Tuple([call_2449,])
output2 = relay.Tuple([call_2450,])
func_2452 = relay.Function([], output)
mod['func_2452'] = func_2452
mod = relay.transform.InferType()(mod)
output = func_2452()
func_2453 = relay.Function([], output)
mutated_mod['func_2453'] = func_2453
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1072_call = mod.get_global_var('func_1072')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_2456 = relay.TupleGetItem(func_1072_call(), 2)
call_2457 = relay.TupleGetItem(func_1073_call(), 2)
func_1249_call = mod.get_global_var('func_1249')
func_1251_call = mutated_mod.get_global_var('func_1251')
call_2473 = relay.TupleGetItem(func_1249_call(), 1)
call_2474 = relay.TupleGetItem(func_1251_call(), 1)
output = relay.Tuple([call_2456,call_2473,])
output2 = relay.Tuple([call_2457,call_2474,])
func_2486 = relay.Function([], output)
mod['func_2486'] = func_2486
mod = relay.transform.InferType()(mod)
output = func_2486()
func_2487 = relay.Function([], output)
mutated_mod['func_2487'] = func_2487
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2507 = relay.const([[[9,-5,-6,2,8,-4,8,-1,-8,-2,-3],[-2,-5,2,-5,1,-2,9,-1,-9,-8,-6],[-4,1,-3,-4,6,-1,-7,8,7,-5,8],[-6,-5,-8,9,9,-8,5,3,-8,-9,10],[2,-7,-9,-8,8,-8,1,8,-9,-3,-7],[-2,10,-7,-9,-5,7,9,-4,-5,-1,7],[-10,-1,-2,-9,5,-9,-1,1,5,10,8],[10,-4,-6,1,-10,10,3,8,-1,3,-5],[8,4,-4,7,-2,5,5,5,-7,-8,-6],[9,3,6,-9,10,-9,-5,9,-6,-1,8],[-2,-4,8,4,-1,10,2,-9,7,10,-4],[-8,9,5,-2,-7,-8,3,-3,1,-9,-7],[5,2,9,-7,-1,7,8,9,3,-6,9],[6,-6,5,8,-4,1,-6,-2,-3,-7,-10],[-10,-6,-8,-5,-2,8,-10,1,6,2,5]],[[-6,-10,-9,-9,1,-1,2,9,-6,-10,9],[7,7,-9,-1,-6,1,-5,-2,-1,-4,10],[-2,5,2,-4,5,-10,5,3,4,-2,-7],[7,-3,-2,1,-7,3,-4,-9,-5,-8,-9],[4,10,3,-5,10,10,10,-2,-4,-5,1],[1,6,4,-10,-10,5,4,-1,-8,9,-4],[-8,10,-5,8,-6,6,4,7,-3,8,-6],[-5,1,8,9,-1,-10,10,7,1,-6,5],[-9,4,1,1,6,4,9,-9,4,7,2],[9,-7,5,9,3,-4,1,1,-3,-8,-4],[9,-7,-3,6,4,-7,6,-4,1,5,6],[-1,6,4,10,-10,1,-3,4,2,-7,-10],[-8,-9,2,4,-8,5,-8,-7,-8,1,-6],[6,6,-1,6,5,4,4,-6,5,3,7],[8,-4,-4,-6,1,-2,9,-9,3,-10,8]],[[4,-4,7,9,-3,-1,-5,-3,-5,2,-1],[-1,7,-4,2,3,-5,4,-6,-9,2,-5],[-5,8,3,9,5,6,-5,-1,6,4,-2],[-5,-1,-7,-6,-10,3,5,1,1,4,-8],[-2,8,6,9,-10,8,3,-6,8,-2,-5],[-6,-10,2,6,5,-2,8,-4,-6,3,6],[9,-5,-10,-7,-5,-3,2,3,9,8,10],[9,-2,8,9,1,10,5,4,-6,7,-6],[-7,6,8,5,-9,3,9,7,9,-6,-4],[8,-4,-9,-4,-7,5,-6,7,-10,-8,-10],[-4,7,-4,2,-5,-8,-3,-8,-3,9,-8],[2,8,6,4,-5,2,4,4,-6,6,-7],[-2,-7,10,6,1,-7,-9,-7,6,5,-3],[-6,7,-7,7,-4,-7,-5,-9,6,6,-10],[-6,-1,-8,-10,5,9,7,7,-8,-2,-3]],[[3,-7,-1,4,-9,-10,-3,-5,9,-1,6],[-2,4,3,6,-3,10,-10,3,4,-4,-2],[-3,4,-1,-10,-4,9,2,-6,-9,-7,-8],[-2,1,-7,-10,-6,8,-5,-4,7,7,10],[9,10,-4,9,-4,-7,6,-3,-2,9,8],[10,-1,4,2,-1,-7,-9,8,4,-6,10],[-2,-8,2,4,-3,4,1,4,-1,2,-6],[10,6,5,-7,-6,7,-3,1,-1,-4,-2],[4,-8,-3,-4,3,2,-9,3,-3,5,3],[9,9,-10,-6,10,10,-6,10,1,-5,5],[9,2,-7,2,-8,3,2,10,8,9,-6],[1,4,-1,5,4,2,-6,4,-8,-10,10],[8,1,8,6,-2,1,-10,-6,6,7,-10],[8,10,6,9,-1,4,3,-1,-7,7,-2],[2,-10,-9,-8,-1,-3,-6,-2,-7,-2,-6]]], dtype = "int16")#candidate|2507|(4, 15, 11)|const|int16
var_2508 = relay.var("var_2508", dtype = "int16", shape = (4, 15, 11))#candidate|2508|(4, 15, 11)|var|int16
bop_2509 = relay.less(const_2507.astype('bool'), relay.reshape(var_2508.astype('bool'), relay.shape_of(const_2507))) # shape=(4, 15, 11)
bop_2513 = relay.left_shift(bop_2509.astype('uint16'), relay.reshape(const_2507.astype('uint16'), relay.shape_of(bop_2509))) # shape=(4, 15, 11)
uop_2519 = relay.rsqrt(bop_2509.astype('float32')) # shape=(4, 15, 11)
uop_2524 = relay.log10(uop_2519.astype('float64')) # shape=(4, 15, 11)
var_2540 = relay.var("var_2540", dtype = "float64", shape = (4, 15, 11))#candidate|2540|(4, 15, 11)|var|float64
bop_2541 = relay.greater(uop_2524.astype('bool'), relay.reshape(var_2540.astype('bool'), relay.shape_of(uop_2524))) # shape=(4, 15, 11)
func_2204_call = mod.get_global_var('func_2204')
func_2206_call = mutated_mod.get_global_var('func_2206')
var_2545 = relay.var("var_2545", dtype = "int8", shape = (770,))#candidate|2545|(770,)|var|int8
call_2544 = relay.TupleGetItem(func_2204_call(relay.reshape(var_2545.astype('int8'), [7, 110])), 3)
call_2546 = relay.TupleGetItem(func_2206_call(relay.reshape(var_2545.astype('int8'), [7, 110])), 3)
output = relay.Tuple([bop_2513,bop_2541,call_2544,var_2545,])
output2 = relay.Tuple([bop_2513,bop_2541,call_2546,var_2545,])
func_2557 = relay.Function([var_2508,var_2540,var_2545,], output)
mod['func_2557'] = func_2557
mod = relay.transform.InferType()(mod)
var_2558 = relay.var("var_2558", dtype = "int16", shape = (4, 15, 11))#candidate|2558|(4, 15, 11)|var|int16
var_2559 = relay.var("var_2559", dtype = "float64", shape = (4, 15, 11))#candidate|2559|(4, 15, 11)|var|float64
var_2560 = relay.var("var_2560", dtype = "int8", shape = (770,))#candidate|2560|(770,)|var|int8
output = func_2557(var_2558,var_2559,var_2560,)
func_2561 = relay.Function([var_2558,var_2559,var_2560,], output)
mutated_mod['func_2561'] = func_2561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2386_call = mod.get_global_var('func_2386')
func_2388_call = mutated_mod.get_global_var('func_2388')
call_2615 = relay.TupleGetItem(func_2386_call(), 0)
call_2616 = relay.TupleGetItem(func_2388_call(), 0)
func_1249_call = mod.get_global_var('func_1249')
func_1251_call = mutated_mod.get_global_var('func_1251')
call_2653 = relay.TupleGetItem(func_1249_call(), 0)
call_2654 = relay.TupleGetItem(func_1251_call(), 0)
func_253_call = mod.get_global_var('func_253')
func_255_call = mutated_mod.get_global_var('func_255')
const_2658 = relay.const([-3,-9,6,7,-7,3,-5,-7,1,8,8,2,-7,7,-2,5,3,-8,2,-6,-8,4,-4,-6,10,-2,9,8,9,-5,8,-8,-4,2,2,4,1,-1,-8,9,-2,8,-4,-5,-2,4,2,10,10,1,-2,-2,-4,7,2,10,6,5,-4,3,-3,-3,8,-1,5,-10,9,-9,7,-5,-1,-2,10,-5,8,-10,4,5,7,2,-10,-7,6,-1,2,-9,10,-8,-9,-7,-2,7,10,-1,8,7,8,6,-1,-5,5,-6,7,7,10,4,-3,-1,3,-10,-5,-8,4,-9,10,-8,9,-2,-9,-6,-5,2,-1,2,4,4,10,4,-5,9,-8,2,4,-6,5,3,-2,7,-9,-7,1,-2,-5,-7,3,6,4,9,-2,-2,-8,-6,-1,4,-1,10,-4,3,3,10,7,-7,3,-10,10,-3,-6,-9,-1,-6,5,4,-2,-9,-8,-3,4,-5,-4,4,-6,4,-6,-10,5,-1,4,2,-4,-3,1,-5,-5,-3,-5,3,-6,3,10,-2,1,-9,-7,-3,3,3,-3,10,1,5,4,7,-6,3,4,-5,7,10,-3,6,10,-10,10,-8,-5,6,2,-9,-2,8,-10,-2,5,4,4,5,-1,-6,-7,1,9,3,-1,-4,7,-10,3,3,-4,7,8,4,9,10,6,9,-1,9,-5,4,2,-8,-5,-2,-9,-9,-1,6,-4,-7,10,-8,-8,-10,9,-6,7,6,8,-1,9,4,4,3,8,8,5,8,2,-8,-1,2,8,-10,-7,3,-2,9,9,-1,9,-7,-7,8,3,10,10,-2,9,-5,4,6,9,9,7,-6,-1,-1,-8,-10,6,-6,2,-5,1,-1,1,10,-3,9,3,6,-10,4,7,10,-4,10,-4,10,6,-2,-9,7,3,1,3,2,6,1,10,9,-6,3,-3,-5,4,-7,10,-6,2,-1,-5,-6,8,4,-7,-5,1,2,9,-4,5,-8,7,-7,1,4,10,-9,-7,8,6,-8,-1,3,-10,-5,-10,7,8,8,4,7,2,-4,-7,-5,-8,-1,5,-9,3,-7,8,4,-2,5,-4,1,6,-9,2,9,-8,10,-6,-6,4,4,1,-10,-10,-8,9,4,-9,-10,6,-2,2,6,3,-9,-9,-1,-2,-3,5,-9,-5,10,4,6,1,-4,1,3,6,-3,6,5,-4,-10,-2,-5,-10,2,7,5,9,3,1,-6,-9,-2,-2,10,-5,-4,9,-5,-4,-4,6,-1,9,7,-1,7,-1,-4,3,-8,4,9,-1,2,-3,6,-8,-6,-2,-6,-5,4,9,-8,2,5,6,-1,10,2,-10,5,-9,4,4,-6,-3,5,-8,6,-9,-6,-7,-3,10,10,-8,-9,-8,8,-7,10,-5,-3,10,-3,-2,-5,5,6,7,-9,-1,-2,5,10,2,-9,-9,-10,-4,9,1,5,-3,-3,-4,-5,-3,5,-5,-8,-7,6,1,-4,-6,-1,8,-2,4,1,-2,-7,3,2,7,9,-9,1,-10,7], dtype = "uint32")#candidate|2658|(576,)|const|uint32
call_2657 = func_253_call(relay.reshape(const_2658.astype('uint32'), [3, 16, 12]))
call_2659 = func_253_call(relay.reshape(const_2658.astype('uint32'), [3, 16, 12]))
func_1072_call = mod.get_global_var('func_1072')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_2661 = relay.TupleGetItem(func_1072_call(), 3)
call_2662 = relay.TupleGetItem(func_1073_call(), 3)
output = relay.Tuple([call_2615,call_2653,call_2657,const_2658,call_2661,])
output2 = relay.Tuple([call_2616,call_2654,call_2659,const_2658,call_2662,])
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
func_2668_call = mod.get_global_var('func_2668')
func_2670_call = mutated_mod.get_global_var('func_2670')
call_2690 = relay.TupleGetItem(func_2668_call(), 3)
call_2691 = relay.TupleGetItem(func_2670_call(), 3)
output = call_2690
output2 = call_2691
func_2694 = relay.Function([], output)
mod['func_2694'] = func_2694
mod = relay.transform.InferType()(mod)
output = func_2694()
func_2695 = relay.Function([], output)
mutated_mod['func_2695'] = func_2695
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2722 = relay.var("var_2722", dtype = "int16", shape = (11, 8, 5))#candidate|2722|(11, 8, 5)|var|int16
var_2723 = relay.var("var_2723", dtype = "int16", shape = (11, 8, 5))#candidate|2723|(11, 8, 5)|var|int16
bop_2724 = relay.equal(var_2722.astype('bool'), relay.reshape(var_2723.astype('bool'), relay.shape_of(var_2722))) # shape=(11, 8, 5)
func_2016_call = mod.get_global_var('func_2016')
func_2018_call = mutated_mod.get_global_var('func_2018')
call_2736 = relay.TupleGetItem(func_2016_call(), 0)
call_2737 = relay.TupleGetItem(func_2018_call(), 0)
output = relay.Tuple([bop_2724,call_2736,])
output2 = relay.Tuple([bop_2724,call_2737,])
func_2744 = relay.Function([var_2722,var_2723,], output)
mod['func_2744'] = func_2744
mod = relay.transform.InferType()(mod)
mutated_mod['func_2744'] = func_2744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2744_call = mutated_mod.get_global_var('func_2744')
var_2746 = relay.var("var_2746", dtype = "int16", shape = (11, 8, 5))#candidate|2746|(11, 8, 5)|var|int16
var_2747 = relay.var("var_2747", dtype = "int16", shape = (11, 8, 5))#candidate|2747|(11, 8, 5)|var|int16
call_2745 = func_2744_call(var_2746,var_2747,)
output = call_2745
func_2748 = relay.Function([var_2746,var_2747,], output)
mutated_mod['func_2748'] = func_2748
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2781 = relay.const([[[-5.634871,-7.298865,8.026994,-2.564066,0.767987,-3.898678,-9.368762,-8.655483],[2.469570,6.121051,-2.140228,7.949170,-2.061728,-1.353802,-5.760082,-6.500972],[-7.341723,3.323579,4.942584,8.908906,-0.242357,-2.424920,-1.437097,7.162352],[-6.315463,-9.503363,-8.314101,2.280154,-3.171732,8.728808,-7.114755,9.096882],[7.888040,-8.482999,-5.903495,6.753359,-9.662787,1.279504,-8.070604,-2.722650],[-6.728787,9.471374,-3.940378,9.900762,-9.139665,5.120642,-9.793113,8.146715],[1.305012,1.711829,-4.298315,-9.679375,-8.823420,2.019162,-7.707084,9.588341],[-5.638085,4.308748,-3.383266,-3.410822,-6.440009,3.952917,-6.732946,-8.775971],[-3.720912,-4.806545,-7.726695,0.710167,-9.462958,-9.833511,-2.529222,8.236777]],[[-8.644030,-6.090597,-2.194989,-2.827149,-5.306475,6.081684,-7.677726,6.638798],[9.948947,1.335692,-4.884875,5.264962,-7.673040,-4.739911,1.708305,1.955919],[-0.979153,-6.891726,-8.021529,2.359599,-9.182324,-5.062547,-8.003305,-3.392474],[0.654907,-6.870546,-8.570871,-5.422560,5.196209,-6.983868,0.808276,-0.432271],[0.216630,-8.622576,2.674470,-6.321289,-4.638066,3.754224,-1.740675,5.409217],[1.586407,-6.504650,1.087242,-3.113617,9.074392,0.651397,2.669244,-1.850775],[3.489552,-7.855001,1.810926,-3.897313,3.161811,-6.903676,4.527028,1.753864],[0.849035,7.014038,8.803372,7.815952,-4.942039,9.813398,8.085147,-9.578898],[-7.702392,0.943792,7.745634,7.126860,5.963093,7.853331,4.634317,-5.805270]],[[-1.408089,4.921507,4.117500,-1.382026,-9.643946,3.972540,7.548357,-1.222774],[2.071463,2.605040,4.028166,2.933301,7.484983,-5.963610,-7.542045,9.589939],[-8.834078,-6.027839,-6.564011,9.766678,-7.929526,-6.483003,-3.895509,0.088049],[-6.897769,-7.444662,9.406182,8.033450,-8.363922,-6.008375,-0.498381,1.974540],[-2.058689,-7.605309,-2.757875,0.674098,6.603553,1.204947,-3.147302,7.480316],[9.087344,7.803470,4.039332,3.078481,-6.814946,-6.064793,-5.870532,7.730513],[8.953204,4.988466,8.756081,-6.743811,-3.275954,-5.955433,-9.175416,1.868566],[4.405041,2.607148,8.522854,5.068687,-7.088638,-3.192884,3.089784,1.900449],[-9.799652,6.194583,-1.994144,-8.803237,9.733760,7.647244,-1.848574,0.205132]],[[6.474151,-0.334084,-9.173520,-8.385126,-2.830268,5.408702,-8.675928,-9.499496],[6.715472,-7.534734,-2.500715,-3.850327,5.075436,1.788480,-4.474887,-0.931885],[8.205999,1.718542,-1.416442,-3.160868,-9.185101,-9.079854,2.648383,3.479668],[-4.298861,-3.044613,-3.151354,-0.905341,-2.602616,6.476437,1.803404,2.290660],[4.266776,-9.642913,-0.308106,-2.600362,-2.190402,-6.366935,1.258369,-7.477541],[6.331151,-7.978512,9.838378,-4.386317,6.548234,-2.322873,8.789996,1.398766],[-9.495169,-2.246780,1.454845,-1.609730,0.485473,8.238681,-6.742403,7.467499],[-3.918450,-2.679952,-9.693071,7.201986,-2.492478,-7.304581,0.754025,-3.860726],[6.863072,5.822118,4.217798,-7.052010,-8.418751,-8.720134,9.615510,-9.403874]],[[0.637293,9.425626,8.492230,4.499391,8.645725,0.464742,-3.051710,-8.898130],[-1.812619,-1.371736,5.671441,1.767014,-7.922273,2.950798,9.178791,7.260926],[-0.332558,-1.599119,8.759148,8.429692,-1.417955,-7.246967,1.799324,-1.012157],[-9.820811,2.366530,-3.490912,1.683226,-3.180806,-9.381899,-1.285378,4.524047],[1.534707,6.715565,1.873071,9.532112,5.083699,-6.914525,-2.912717,1.308595],[8.091380,4.515911,2.229196,-9.250831,1.754699,4.423332,-9.289968,-1.604848],[-7.821238,8.710923,-5.213936,3.413402,-4.184383,-9.083164,0.303045,6.668808],[3.529210,-0.132867,2.218151,-3.630308,7.421369,-2.471555,-4.301731,4.686102],[-6.820506,1.362887,4.573147,0.083515,-2.462711,0.142314,9.763618,4.338461]],[[7.649810,5.284665,-6.159487,7.517257,6.634139,-2.450162,-6.149102,-6.272165],[-2.689706,2.250257,8.380706,1.969092,6.377937,1.539954,6.426691,3.499847],[-7.662907,7.190524,-1.155256,-3.743805,-2.216720,-4.571335,4.189257,-3.613164],[-0.908951,9.556442,-9.249788,8.970102,1.591573,-1.807160,9.844777,7.064032],[-9.185674,2.554805,8.825438,-6.565809,-1.638307,-4.618364,4.471116,5.539366],[4.352778,1.135702,4.829484,7.440289,1.948613,5.037460,4.432563,-9.655133],[6.569979,-7.862262,-7.569525,-2.892931,7.183435,-9.754708,3.464383,-7.137335],[-8.060796,-7.357545,5.040346,4.375556,0.592860,2.553830,7.021257,-9.936709],[2.627272,-1.255204,9.269453,-0.058005,8.230576,-7.902453,-2.661798,1.203421]]], dtype = "float32")#candidate|2781|(6, 9, 8)|const|float32
uop_2782 = relay.acosh(const_2781.astype('float32')) # shape=(6, 9, 8)
output = relay.Tuple([uop_2782,])
output2 = relay.Tuple([uop_2782,])
func_2802 = relay.Function([], output)
mod['func_2802'] = func_2802
mod = relay.transform.InferType()(mod)
mutated_mod['func_2802'] = func_2802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2802_call = mutated_mod.get_global_var('func_2802')
call_2803 = func_2802_call()
output = call_2803
func_2804 = relay.Function([], output)
mutated_mod['func_2804'] = func_2804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1249_call = mod.get_global_var('func_1249')
func_1251_call = mutated_mod.get_global_var('func_1251')
call_2814 = relay.TupleGetItem(func_1249_call(), 0)
call_2815 = relay.TupleGetItem(func_1251_call(), 0)
output = call_2814
output2 = call_2815
func_2816 = relay.Function([], output)
mod['func_2816'] = func_2816
mod = relay.transform.InferType()(mod)
mutated_mod['func_2816'] = func_2816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2816_call = mutated_mod.get_global_var('func_2816')
call_2817 = func_2816_call()
output = call_2817
func_2818 = relay.Function([], output)
mutated_mod['func_2818'] = func_2818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1770_call = mod.get_global_var('func_1770')
func_1772_call = mutated_mod.get_global_var('func_1772')
call_2825 = func_1770_call()
call_2826 = func_1770_call()
output = relay.Tuple([call_2825,])
output2 = relay.Tuple([call_2826,])
func_2827 = relay.Function([], output)
mod['func_2827'] = func_2827
mod = relay.transform.InferType()(mod)
mutated_mod['func_2827'] = func_2827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2827_call = mutated_mod.get_global_var('func_2827')
call_2828 = func_2827_call()
output = call_2828
func_2829 = relay.Function([], output)
mutated_mod['func_2829'] = func_2829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2042_call = mod.get_global_var('func_2042')
func_2043_call = mutated_mod.get_global_var('func_2043')
call_2881 = relay.TupleGetItem(func_2042_call(), 0)
call_2882 = relay.TupleGetItem(func_2043_call(), 0)
func_2386_call = mod.get_global_var('func_2386')
func_2388_call = mutated_mod.get_global_var('func_2388')
call_2892 = relay.TupleGetItem(func_2386_call(), 1)
call_2893 = relay.TupleGetItem(func_2388_call(), 1)
bop_2895 = relay.add(call_2892.astype('float64'), relay.reshape(call_2881.astype('float64'), relay.shape_of(call_2892))) # shape=(3, 1, 9)
bop_2898 = relay.add(call_2893.astype('float64'), relay.reshape(call_2882.astype('float64'), relay.shape_of(call_2893))) # shape=(3, 1, 9)
func_1561_call = mod.get_global_var('func_1561')
func_1563_call = mutated_mod.get_global_var('func_1563')
var_2904 = relay.var("var_2904", dtype = "float32", shape = (450,))#candidate|2904|(450,)|var|float32
call_2903 = relay.TupleGetItem(func_1561_call(relay.reshape(var_2904.astype('float32'), [450,])), 7)
call_2905 = relay.TupleGetItem(func_1563_call(relay.reshape(var_2904.astype('float32'), [450,])), 7)
func_2802_call = mod.get_global_var('func_2802')
func_2804_call = mutated_mod.get_global_var('func_2804')
call_2912 = relay.TupleGetItem(func_2802_call(), 0)
call_2913 = relay.TupleGetItem(func_2804_call(), 0)
output = relay.Tuple([bop_2895,call_2903,var_2904,call_2912,])
output2 = relay.Tuple([bop_2898,call_2905,var_2904,call_2913,])
func_2932 = relay.Function([var_2904,], output)
mod['func_2932'] = func_2932
mod = relay.transform.InferType()(mod)
mutated_mod['func_2932'] = func_2932
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2933 = relay.var("var_2933", dtype = "float32", shape = (450,))#candidate|2933|(450,)|var|float32
func_2932_call = mutated_mod.get_global_var('func_2932')
call_2934 = func_2932_call(var_2933)
output = call_2934
func_2935 = relay.Function([var_2933], output)
mutated_mod['func_2935'] = func_2935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2452_call = mod.get_global_var('func_2452')
func_2453_call = mutated_mod.get_global_var('func_2453')
call_2944 = relay.TupleGetItem(func_2452_call(), 0)
call_2945 = relay.TupleGetItem(func_2453_call(), 0)
output = relay.Tuple([call_2944,])
output2 = relay.Tuple([call_2945,])
func_2995 = relay.Function([], output)
mod['func_2995'] = func_2995
mod = relay.transform.InferType()(mod)
mutated_mod['func_2995'] = func_2995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2995_call = mutated_mod.get_global_var('func_2995')
call_2996 = func_2995_call()
output = call_2996
func_2997 = relay.Function([], output)
mutated_mod['func_2997'] = func_2997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2668_call = mod.get_global_var('func_2668')
func_2670_call = mutated_mod.get_global_var('func_2670')
call_3029 = relay.TupleGetItem(func_2668_call(), 1)
call_3030 = relay.TupleGetItem(func_2670_call(), 1)
output = call_3029
output2 = call_3030
func_3036 = relay.Function([], output)
mod['func_3036'] = func_3036
mod = relay.transform.InferType()(mod)
output = func_3036()
func_3037 = relay.Function([], output)
mutated_mod['func_3037'] = func_3037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3036_call = mod.get_global_var('func_3036')
func_3037_call = mutated_mod.get_global_var('func_3037')
call_3052 = func_3036_call()
call_3053 = func_3036_call()
output = relay.Tuple([call_3052,])
output2 = relay.Tuple([call_3053,])
func_3069 = relay.Function([], output)
mod['func_3069'] = func_3069
mod = relay.transform.InferType()(mod)
output = func_3069()
func_3070 = relay.Function([], output)
mutated_mod['func_3070'] = func_3070
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2386_call = mod.get_global_var('func_2386')
func_2388_call = mutated_mod.get_global_var('func_2388')
call_3088 = relay.TupleGetItem(func_2386_call(), 1)
call_3089 = relay.TupleGetItem(func_2388_call(), 1)
output = relay.Tuple([call_3088,])
output2 = relay.Tuple([call_3089,])
func_3091 = relay.Function([], output)
mod['func_3091'] = func_3091
mod = relay.transform.InferType()(mod)
mutated_mod['func_3091'] = func_3091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3091_call = mutated_mod.get_global_var('func_3091')
call_3092 = func_3091_call()
output = call_3092
func_3093 = relay.Function([], output)
mutated_mod['func_3093'] = func_3093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1867_call = mod.get_global_var('func_1867')
func_1868_call = mutated_mod.get_global_var('func_1868')
call_3143 = relay.TupleGetItem(func_1867_call(), 0)
call_3144 = relay.TupleGetItem(func_1868_call(), 0)
var_3155 = relay.var("var_3155", dtype = "int16", shape = (3, 15, 9))#candidate|3155|(3, 15, 9)|var|int16
bop_3156 = relay.multiply(call_3143.astype('float32'), var_3155.astype('float32')) # shape=(3, 15, 9)
bop_3159 = relay.multiply(call_3144.astype('float32'), var_3155.astype('float32')) # shape=(3, 15, 9)
uop_3162 = relay.cosh(var_3155.astype('float64')) # shape=(3, 15, 9)
uop_3165 = relay.exp(uop_3162.astype('float32')) # shape=(3, 15, 9)
output = relay.Tuple([bop_3156,uop_3165,])
output2 = relay.Tuple([bop_3159,uop_3165,])
func_3169 = relay.Function([var_3155,], output)
mod['func_3169'] = func_3169
mod = relay.transform.InferType()(mod)
var_3170 = relay.var("var_3170", dtype = "int16", shape = (3, 15, 9))#candidate|3170|(3, 15, 9)|var|int16
output = func_3169(var_3170)
func_3171 = relay.Function([var_3170], output)
mutated_mod['func_3171'] = func_3171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1170_call = mod.get_global_var('func_1170')
func_1172_call = mutated_mod.get_global_var('func_1172')
call_3201 = relay.TupleGetItem(func_1170_call(), 0)
call_3202 = relay.TupleGetItem(func_1172_call(), 0)
output = call_3201
output2 = call_3202
func_3203 = relay.Function([], output)
mod['func_3203'] = func_3203
mod = relay.transform.InferType()(mod)
output = func_3203()
func_3204 = relay.Function([], output)
mutated_mod['func_3204'] = func_3204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2081_call = mod.get_global_var('func_2081')
func_2082_call = mutated_mod.get_global_var('func_2082')
call_3214 = relay.TupleGetItem(func_2081_call(), 0)
call_3215 = relay.TupleGetItem(func_2082_call(), 0)
func_2042_call = mod.get_global_var('func_2042')
func_2043_call = mutated_mod.get_global_var('func_2043')
call_3220 = relay.TupleGetItem(func_2042_call(), 0)
call_3221 = relay.TupleGetItem(func_2043_call(), 0)
output = relay.Tuple([call_3214,call_3220,])
output2 = relay.Tuple([call_3215,call_3221,])
func_3231 = relay.Function([], output)
mod['func_3231'] = func_3231
mod = relay.transform.InferType()(mod)
mutated_mod['func_3231'] = func_3231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3231_call = mutated_mod.get_global_var('func_3231')
call_3232 = func_3231_call()
output = call_3232
func_3233 = relay.Function([], output)
mutated_mod['func_3233'] = func_3233
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3243 = relay.const([[[-9.953769,9.082701,4.847902,2.736633,-9.114988,5.577656],[-3.403081,9.860813,8.007587,5.589654,1.056557,9.317678],[-4.236688,1.433341,-8.568630,6.598426,-0.171538,7.397851],[2.916822,3.032539,-1.331460,4.831702,-1.050757,9.269675],[9.719597,-2.795022,-9.176663,6.074813,2.383969,-5.466103],[9.409589,-0.447291,-8.160945,5.530856,-1.156896,-6.905061],[6.222331,-1.812873,-4.985706,-5.151549,-3.920381,-2.637832],[-8.561878,-2.108961,-8.521664,0.203950,-6.616104,0.926186],[9.489160,6.220051,-7.077200,-4.533185,8.227773,5.217932],[-8.081908,7.333688,-5.503797,-8.479009,6.885838,-0.110443],[8.975591,6.056856,7.995740,-6.452482,-2.309052,-1.104637],[2.301999,-3.634234,8.684826,-9.707786,2.409540,7.549954],[9.052264,-7.886531,-9.512707,-5.609293,-9.087606,7.294507],[4.849873,-7.983201,4.631463,-4.290345,-4.261908,3.618541]],[[-9.685944,7.314561,-1.744686,2.305587,-6.106372,-3.363784],[-9.831218,-9.664497,5.732441,-3.134912,-4.727427,-0.785778],[6.883129,-1.252225,1.079992,-4.625025,-4.055179,-3.097567],[-6.311297,-9.793851,2.582975,0.883372,-0.909280,7.835923],[3.498472,-1.906839,-3.713455,-0.870772,5.189028,4.989255],[-5.359312,-0.524791,-2.936704,5.522534,-5.476151,1.727369],[3.677991,5.184380,1.752384,7.571139,-5.476069,-1.814075],[-1.415147,-1.276026,3.720391,-5.038931,3.017727,-4.240783],[1.682211,-8.515745,-8.510843,-6.311757,-9.420991,5.272541],[-6.663479,6.309734,-1.527962,2.092867,-4.761511,-5.599609],[-8.681247,8.038881,3.264703,9.891256,-1.447920,-5.369355],[3.891340,-8.492564,-6.455698,0.424275,-4.258572,6.570236],[-4.092047,9.146228,-2.873309,9.720781,-5.585770,1.894051],[-6.779889,9.154871,-8.047117,3.274814,-9.885199,-7.928763]],[[9.981410,6.294681,-3.532805,-8.595735,1.462114,0.341597],[6.075047,-1.058869,0.706809,5.741131,-4.334189,-8.600071],[-8.902058,3.390941,7.775260,5.843232,8.197702,-8.079844],[2.715370,3.077842,-0.436323,8.045741,1.303623,-8.208340],[5.448849,-5.427592,-5.857501,-7.409705,4.234669,0.821816],[9.246692,8.678678,3.341277,-1.702396,1.607096,9.913741],[-0.673665,7.121161,7.388909,6.001828,-8.734567,-6.067732],[-1.189208,9.547320,-3.009933,9.094954,-2.420345,2.756215],[-5.509813,-0.598204,1.826103,-7.592290,-5.083233,4.171919],[5.321828,-6.005882,-8.725353,-6.126304,-5.819084,-8.472550],[-1.790225,-5.315541,8.232244,-6.357637,-8.677895,1.814397],[-6.416614,4.709728,6.466645,-5.494855,9.246004,-2.554177],[-3.784374,3.383565,5.870932,2.809375,4.575334,-0.573034],[3.592688,-5.114073,6.649800,7.981720,1.507063,6.536380]],[[2.725764,6.630533,-5.302033,0.583432,-9.107809,3.131181],[-5.445877,3.806191,8.219137,-2.065354,-1.009302,-5.658538],[-9.965416,-2.504700,-9.601441,1.287350,9.219624,3.962735],[-4.094946,-2.723932,0.738945,-1.002446,5.176610,9.259482],[2.924087,3.769589,-4.943512,-3.804783,-9.688457,3.658310],[-3.259749,-5.221193,1.778730,1.756359,-6.638262,5.313108],[-0.798146,-8.136257,6.710771,-5.473517,9.815709,5.535260],[0.903431,9.177804,-9.622963,-1.980014,9.699224,-8.256268],[-3.023756,-1.807470,-9.809172,-8.496247,-9.939764,-9.951199],[-4.510700,-1.552463,-3.607186,-7.190741,8.694259,7.320033],[-6.323914,-6.982706,9.217773,-9.587207,2.755270,-3.278260],[-6.386568,-9.508144,9.269766,1.024264,2.395133,-0.372768],[1.497601,2.211581,-5.846311,-3.029365,-1.438161,-3.619492],[5.503869,-0.817011,8.647244,-0.241681,5.736105,-3.009735]],[[3.905437,2.121070,-6.447984,7.645677,-0.814906,-9.514210],[2.276959,2.062339,-6.977776,9.498346,-0.822356,-1.654589],[8.092439,-9.435287,7.950949,7.969178,-3.262101,5.004709],[-9.435315,-5.149534,7.062928,4.439980,9.875154,-2.438748],[-6.126603,3.267305,7.202219,8.625918,0.541866,-4.878841],[-8.473556,3.464598,-4.482460,5.477377,5.749319,4.882585],[9.741367,-1.050594,5.857035,-8.735653,-1.283669,-0.320059],[1.583617,-6.037270,1.693805,5.770760,0.917083,-9.041576],[8.804117,-7.753639,9.994741,6.441196,1.234521,2.406332],[-0.800409,-3.321080,-5.364997,1.661868,-1.293161,-9.659596],[-5.529476,-6.495862,-1.482048,9.655241,-8.619299,0.686611],[4.853612,-3.244524,-3.383123,1.377493,1.891557,2.107460],[-9.370678,3.657714,9.509977,9.699078,3.187139,2.694804],[-9.006729,5.909105,-7.929739,3.893106,5.394747,-3.441316]],[[8.476985,0.005151,-8.525718,-8.388857,9.003296,6.125639],[3.489344,-9.296101,-3.758314,5.072216,-0.925577,-5.268019],[6.698427,-5.908414,8.644668,-1.371467,-8.927178,-7.008908],[-2.104987,3.385564,-9.995424,-5.588176,8.707153,8.904452],[-4.098820,7.536049,7.151833,-8.929722,8.986429,-5.653135],[5.253907,5.552139,-9.398501,-6.562097,7.948506,-6.503765],[6.762370,7.513334,7.668966,-6.410717,3.603459,-5.170713],[1.363740,5.966866,7.989385,-1.056259,-0.192822,-6.222539],[6.795450,-8.787280,-0.883719,-8.921599,4.045914,5.039468],[-4.494199,7.509082,3.237228,0.705352,-7.532151,5.017612],[-2.118399,-7.877954,9.287756,5.352760,-5.837913,2.863248],[-1.304035,-0.797375,-9.243081,-1.984670,8.945528,-0.081974],[9.387068,-3.183193,3.530365,4.624769,4.207128,-8.785856],[-0.114522,7.481342,5.198903,3.939178,-3.160124,-9.591183]],[[9.327416,-9.387283,-6.456110,7.339845,-9.948134,6.886402],[7.000400,2.588385,-0.238204,-6.994670,0.113655,2.522851],[-3.283528,-6.324614,-6.960243,6.164614,3.377487,7.438407],[2.391988,9.164453,-3.321456,6.274294,4.377034,-7.978643],[-9.102791,-3.494182,-4.290417,9.648041,-7.371132,6.778790],[-4.918564,8.434715,-1.015643,6.454579,4.967239,5.148045],[2.601247,-1.641984,1.083939,-3.251255,3.318364,2.381411],[4.152812,-3.298155,-0.992296,-6.941441,7.581125,-4.420921],[-6.348316,6.155024,-9.311157,6.083746,3.930050,-3.965465],[-0.406396,-4.403250,1.138881,1.585478,-0.778095,2.648042],[-7.318489,8.649789,0.995058,2.884248,3.217540,4.875112],[-7.167654,1.006533,-9.350142,-8.666476,7.838679,-2.474919],[5.099026,5.810813,-8.461821,-4.984148,-4.205634,-0.274068],[-7.734330,-2.289955,-5.110285,7.770854,-9.070175,-3.287119]],[[7.805360,-7.132265,7.380006,1.351871,-1.494248,6.159781],[7.259353,5.487652,8.175517,2.983296,-8.430192,-3.638683],[-3.598313,1.414551,-0.506371,2.241041,-4.079894,-3.323643],[9.147064,-8.178264,-8.671116,-3.034638,-3.213683,-0.272562],[3.562661,3.655064,6.212220,-5.323906,0.764393,-5.149497],[7.413345,9.611080,2.534739,3.557254,-8.971464,7.117661],[4.910769,-5.449495,8.094054,-9.171439,3.089126,-5.162340],[2.554908,-8.286739,-6.494159,-6.932862,-2.348233,-7.047997],[-9.439445,-7.555784,4.563054,4.153174,4.044689,-8.691500],[-4.648747,4.995671,-9.060827,-6.875333,-8.522458,4.341293],[-0.773083,-9.479059,2.634308,-5.901100,3.526178,-5.903559],[-2.978840,6.154649,-4.569356,6.714662,-9.867979,-0.039548],[-2.009077,-5.093343,3.911679,-9.822288,-8.070940,-2.724532],[4.887054,1.615139,-3.386769,4.409701,4.977105,-0.317494]],[[8.986788,5.715615,4.608741,-0.506767,-9.708399,-7.558058],[-0.560525,0.476929,-6.261867,7.154739,2.676463,-8.901903],[-3.704266,-8.825253,-2.406510,5.364568,-0.339482,-7.507755],[-5.663686,-5.706869,3.857290,-4.993902,3.575164,-9.770878],[-0.105999,4.912254,-6.261106,8.429568,8.357162,7.588645],[-4.098565,6.300250,9.511775,-5.261111,9.522807,-7.057652],[-0.812239,-4.851610,7.651074,0.732759,-0.286872,7.559155],[-7.934001,-1.982256,-6.499614,6.349883,-4.554164,-5.404377],[-5.672077,-4.259620,4.741170,3.910255,3.583103,5.012073],[-4.202449,-7.248798,7.687708,-5.606263,-6.449226,1.284676],[-3.885921,-1.695931,-7.926012,-9.968597,7.789828,-3.008857],[4.255431,-3.484603,6.708255,0.765991,-2.144590,2.961131],[6.110300,6.992898,-9.020688,7.504628,-3.233788,2.149694],[-9.343952,7.623621,-7.117755,-5.999143,0.559393,6.395995]],[[-9.662412,1.705070,-0.778764,-0.663131,-9.164505,-2.438510],[-8.038788,8.131100,1.401036,8.908463,-5.415071,0.371367],[-2.418714,-6.645901,2.987279,8.561908,2.971575,-6.928010],[8.679822,5.103461,2.784456,-1.410128,8.092071,-5.575400],[-7.271500,-1.713186,-6.473155,-2.781045,0.329822,2.548341],[-5.046228,-3.566999,4.057195,9.178331,0.677259,-5.825601],[-3.655728,2.174213,-2.212554,-4.161517,3.309540,1.919027],[0.202523,9.748554,-0.491932,8.387758,2.677960,-6.336222],[-5.388302,8.528415,9.710542,-8.801641,-2.379679,3.847375],[2.817786,8.678139,9.071510,8.819759,-8.143431,4.903839],[9.739508,6.385139,8.872144,6.942282,-4.052093,9.586089],[-7.317218,8.683462,6.044943,6.699549,6.560114,-8.022168],[9.966192,9.196535,-6.532299,-6.081229,1.240837,-6.678332],[-6.125269,-4.167864,-9.090186,-7.174404,-9.915916,6.904919]],[[-9.612357,-8.479617,3.343298,-9.973728,-0.382914,5.286566],[4.260112,-0.233568,9.688491,4.517312,-3.969040,-9.505050],[2.419760,7.565543,8.593204,-1.472124,1.785564,3.744549],[8.931037,2.482831,7.007521,-1.833120,0.213199,1.542357],[0.980820,-4.221164,-7.307173,-5.174105,8.881915,1.261832],[-6.697408,-5.283346,1.877864,-7.094617,-1.373438,-0.051330],[-0.537053,-1.857105,-9.573052,7.221835,-8.765331,9.639215],[-3.349281,-2.547098,-5.115723,-3.597300,1.261594,-1.670194],[-1.101628,0.426187,6.893709,-3.605646,-7.170923,1.819690],[-5.274050,-3.126536,-1.687966,-7.973322,3.594280,-7.851372],[-6.407098,-5.941904,1.660158,-4.486903,-9.401889,-2.973638],[-1.568623,9.036936,6.235295,9.895247,5.376055,-1.100299],[1.510650,0.267696,-8.521196,-6.379928,-7.098866,-7.491252],[-8.684129,-4.021954,0.870557,-0.461741,3.624460,-2.948926]],[[-6.637188,8.279936,-5.543748,8.776975,-9.565435,-1.018419],[-3.715399,6.632327,-7.842151,-6.831666,8.843393,1.870713],[-3.328399,-0.081188,0.817613,-7.551342,-7.162101,-5.659635],[-0.690054,-1.424221,-9.759397,2.037783,-2.347755,3.516267],[-7.513912,2.304854,-2.306696,-4.845416,-8.850496,4.086952],[-3.630576,9.453995,8.764899,7.148997,0.453987,-8.511870],[-8.396500,-5.092389,-3.523304,9.690748,7.611516,-8.324184],[4.429178,-0.267812,3.184968,-9.448487,-7.575727,-3.378520],[4.024590,6.066063,-4.733160,-8.491236,8.159693,2.923262],[-9.870606,-8.934222,1.202116,-3.566124,-9.089793,-1.054706],[-7.176472,4.819155,-0.986888,-2.593805,5.830718,-7.610495],[3.370898,-1.671541,2.992540,-2.156269,2.195504,7.600924],[-5.534222,9.623838,9.455552,-6.788522,-8.893745,-1.673168],[-6.275793,-2.319619,-5.546364,1.498011,4.977190,-1.850453]],[[8.730906,6.581342,0.628406,9.030800,-3.338873,-3.888686],[-9.253533,6.850792,-5.023578,7.787008,-3.514798,-8.984611],[-8.920708,-1.496943,-4.396526,-4.566719,9.286365,-7.064693],[-6.514643,-2.924710,-4.565676,-9.177141,-4.838864,-7.305673],[5.711528,0.137564,6.368458,-2.714226,1.454125,-6.813939],[6.808999,0.731925,-8.850919,-8.861241,1.358804,5.344768],[1.061535,-7.599708,3.393480,4.001260,-5.975809,-7.683127],[-1.064164,2.803078,1.433096,2.944509,-2.612115,3.665302],[-5.921775,7.383950,9.064868,-8.938855,1.434554,-1.688022],[6.461030,9.499774,-0.633538,0.909095,3.950500,-6.327527],[-8.409209,7.101569,-3.573369,6.756336,-4.730607,-2.098165],[8.508893,0.968278,8.458912,6.570281,3.534423,-0.833744],[-6.705531,-5.394282,-0.051668,-5.797325,7.686070,6.254694],[2.037110,-9.378299,0.639327,3.914044,8.344414,4.027066]],[[-9.488647,7.421665,-8.379397,3.981763,-6.040340,-5.939750],[-4.766241,9.984400,-6.075680,4.703798,-4.428419,-9.986355],[-2.742891,-2.655854,-7.179875,-7.865021,0.064799,-0.652529],[7.371741,-2.499941,2.166033,-4.567668,-9.014643,0.535562],[-5.341892,-3.791942,2.271772,-1.362107,-0.055143,0.839437],[1.565814,7.302927,-5.723597,-5.648220,2.497060,0.934915],[7.021350,-7.704426,5.651285,-6.203876,-2.796656,-7.465857],[3.555674,8.764668,-9.666938,-9.090915,-2.401858,-2.700586],[5.210754,-9.125194,1.839527,-7.871803,1.553101,-6.366661],[-0.916837,-3.248388,9.206180,-6.722844,9.608479,-9.622862],[6.376149,6.139355,-4.203047,-8.181248,-8.930372,-8.576651],[-2.887497,-8.978507,5.190514,-7.085658,-2.892639,-5.416817],[-3.997027,-2.854482,-2.183669,0.599242,-6.693797,0.702414],[-3.463580,-9.576336,-5.657613,-2.510079,6.739583,-0.096303]],[[-3.054665,6.491961,9.392970,-9.750426,-7.231763,-6.011491],[-9.063246,-8.538332,-7.710795,0.463518,1.785363,-5.517675],[4.006727,-6.039337,7.415220,9.275513,-3.876925,-7.761694],[2.464638,0.388198,-2.654853,-6.867735,7.729356,6.420436],[3.033139,-7.028039,-2.051213,-9.718775,2.095822,3.738575],[-8.938090,-5.750502,9.724334,-6.972081,-3.052898,-0.170240],[1.245352,7.961683,-8.477242,3.589905,4.872332,-7.233098],[-5.015963,6.852510,-8.045910,-6.138334,-3.165110,7.617354],[-8.853873,-1.113994,9.977176,0.671670,1.534621,6.928206],[8.391742,6.851251,-7.642731,-5.310614,8.568414,-0.050987],[-8.968738,-9.561030,-3.587837,-7.385011,3.880118,1.026301],[-3.134994,-2.738121,1.262377,1.981065,-0.958829,2.571173],[-5.460165,5.092427,-2.668762,5.156409,-8.502690,2.446857],[2.990471,4.358283,-3.508183,4.721001,6.272961,-7.920474]],[[1.977891,8.425404,7.872727,-0.562540,7.718880,8.730248],[-0.826530,-4.073960,-4.771429,5.190872,-3.473367,-2.227031],[2.813594,1.774022,0.600743,9.814057,5.013013,-5.874018],[7.819346,-0.530368,-0.373612,-4.957877,6.051616,-2.827810],[-5.474395,0.988384,-3.032921,5.093799,-8.814878,3.170778],[7.569551,-9.895359,3.348705,2.157191,-6.931650,2.191401],[4.187741,7.548243,4.887978,-9.238290,8.427722,-1.109849],[4.955421,0.835342,-0.256499,-3.092048,7.192272,-6.484662],[8.532635,0.906226,0.866204,2.147909,8.329723,4.765108],[-4.756848,-0.323971,-3.514800,3.493940,9.611074,6.271937],[5.733747,4.992983,-5.537810,-3.458670,2.711104,0.425071],[-3.283943,2.122260,9.762968,-3.425205,-5.859395,8.222643],[1.298641,-7.847785,0.537224,-6.541095,7.697351,2.711559],[9.274665,-7.832890,-9.031100,-6.777606,-9.252878,-1.940388]]], dtype = "float64")#candidate|3243|(16, 14, 6)|const|float64
uop_3244 = relay.cosh(const_3243.astype('float64')) # shape=(16, 14, 6)
func_2386_call = mod.get_global_var('func_2386')
func_2388_call = mutated_mod.get_global_var('func_2388')
call_3250 = relay.TupleGetItem(func_2386_call(), 0)
call_3251 = relay.TupleGetItem(func_2388_call(), 0)
output = relay.Tuple([uop_3244,call_3250,])
output2 = relay.Tuple([uop_3244,call_3251,])
func_3258 = relay.Function([], output)
mod['func_3258'] = func_3258
mod = relay.transform.InferType()(mod)
mutated_mod['func_3258'] = func_3258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3258_call = mutated_mod.get_global_var('func_3258')
call_3259 = func_3258_call()
output = call_3259
func_3260 = relay.Function([], output)
mutated_mod['func_3260'] = func_3260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1072_call = mod.get_global_var('func_1072')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_3272 = relay.TupleGetItem(func_1072_call(), 0)
call_3273 = relay.TupleGetItem(func_1073_call(), 0)
output = relay.Tuple([call_3272,])
output2 = relay.Tuple([call_3273,])
func_3276 = relay.Function([], output)
mod['func_3276'] = func_3276
mod = relay.transform.InferType()(mod)
output = func_3276()
func_3277 = relay.Function([], output)
mutated_mod['func_3277'] = func_3277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2827_call = mod.get_global_var('func_2827')
func_2829_call = mutated_mod.get_global_var('func_2829')
call_3310 = relay.TupleGetItem(func_2827_call(), 0)
call_3311 = relay.TupleGetItem(func_2829_call(), 0)
output = call_3310
output2 = call_3311
func_3326 = relay.Function([], output)
mod['func_3326'] = func_3326
mod = relay.transform.InferType()(mod)
output = func_3326()
func_3327 = relay.Function([], output)
mutated_mod['func_3327'] = func_3327
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1677_call = mod.get_global_var('func_1677')
func_1678_call = mutated_mod.get_global_var('func_1678')
call_3446 = func_1677_call()
call_3447 = func_1677_call()
func_1666_call = mod.get_global_var('func_1666')
func_1669_call = mutated_mod.get_global_var('func_1669')
var_3458 = relay.var("var_3458", dtype = "float64", shape = (264,))#candidate|3458|(264,)|var|float64
call_3457 = relay.TupleGetItem(func_1666_call(relay.reshape(var_3458.astype('float64'), [8, 3, 11])), 1)
call_3459 = relay.TupleGetItem(func_1669_call(relay.reshape(var_3458.astype('float64'), [8, 3, 11])), 1)
uop_3462 = relay.sinh(call_3446.astype('float32')) # shape=(3, 1, 9)
uop_3464 = relay.sinh(call_3447.astype('float32')) # shape=(3, 1, 9)
func_1021_call = mod.get_global_var('func_1021')
func_1026_call = mutated_mod.get_global_var('func_1026')
var_3476 = relay.var("var_3476", dtype = "float32", shape = (135,))#candidate|3476|(135,)|var|float32
var_3477 = relay.var("var_3477", dtype = "float32", shape = (450,))#candidate|3477|(450,)|var|float32
call_3475 = relay.TupleGetItem(func_1021_call(relay.reshape(var_3476.astype('float32'), [9, 3, 5]), relay.reshape(call_3457.astype('int16'), []), relay.reshape(var_3477.astype('float32'), [450,]), relay.reshape(var_3476.astype('float32'), [9, 3, 5]), ), 7)
call_3478 = relay.TupleGetItem(func_1026_call(relay.reshape(var_3476.astype('float32'), [9, 3, 5]), relay.reshape(call_3457.astype('int16'), []), relay.reshape(var_3477.astype('float32'), [450,]), relay.reshape(var_3476.astype('float32'), [9, 3, 5]), ), 7)
func_2042_call = mod.get_global_var('func_2042')
func_2043_call = mutated_mod.get_global_var('func_2043')
call_3483 = relay.TupleGetItem(func_2042_call(), 0)
call_3484 = relay.TupleGetItem(func_2043_call(), 0)
output = relay.Tuple([call_3457,var_3458,uop_3462,call_3475,var_3476,var_3477,call_3483,])
output2 = relay.Tuple([call_3459,var_3458,uop_3464,call_3478,var_3476,var_3477,call_3484,])
func_3503 = relay.Function([var_3458,var_3476,var_3477,], output)
mod['func_3503'] = func_3503
mod = relay.transform.InferType()(mod)
mutated_mod['func_3503'] = func_3503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3503_call = mutated_mod.get_global_var('func_3503')
var_3505 = relay.var("var_3505", dtype = "float64", shape = (264,))#candidate|3505|(264,)|var|float64
var_3506 = relay.var("var_3506", dtype = "float32", shape = (135,))#candidate|3506|(135,)|var|float32
var_3507 = relay.var("var_3507", dtype = "float32", shape = (450,))#candidate|3507|(450,)|var|float32
call_3504 = func_3503_call(var_3505,var_3506,var_3507,)
output = call_3504
func_3508 = relay.Function([var_3505,var_3506,var_3507,], output)
mutated_mod['func_3508'] = func_3508
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3518 = relay.var("var_3518", dtype = "float64", shape = (16, 12, 11))#candidate|3518|(16, 12, 11)|var|float64
uop_3519 = relay.atanh(var_3518.astype('float64')) # shape=(16, 12, 11)
func_416_call = mod.get_global_var('func_416')
func_419_call = mutated_mod.get_global_var('func_419')
const_3522 = relay.const(6, dtype = "int16")#candidate|3522|()|const|int16
var_3523 = relay.var("var_3523", dtype = "int16", shape = (27,))#candidate|3523|(27,)|var|int16
call_3521 = func_416_call(relay.reshape(const_3522.astype('int16'), []), relay.reshape(var_3523.astype('int16'), [3, 1, 9]), )
call_3524 = func_416_call(relay.reshape(const_3522.astype('int16'), []), relay.reshape(var_3523.astype('int16'), [3, 1, 9]), )
output = relay.Tuple([uop_3519,call_3521,const_3522,var_3523,])
output2 = relay.Tuple([uop_3519,call_3524,const_3522,var_3523,])
func_3532 = relay.Function([var_3518,var_3523,], output)
mod['func_3532'] = func_3532
mod = relay.transform.InferType()(mod)
var_3533 = relay.var("var_3533", dtype = "float64", shape = (16, 12, 11))#candidate|3533|(16, 12, 11)|var|float64
var_3534 = relay.var("var_3534", dtype = "int16", shape = (27,))#candidate|3534|(27,)|var|int16
output = func_3532(var_3533,var_3534,)
func_3535 = relay.Function([var_3533,var_3534,], output)
mutated_mod['func_3535'] = func_3535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3091_call = mod.get_global_var('func_3091')
func_3093_call = mutated_mod.get_global_var('func_3093')
call_3575 = relay.TupleGetItem(func_3091_call(), 0)
call_3576 = relay.TupleGetItem(func_3093_call(), 0)
func_1072_call = mod.get_global_var('func_1072')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_3583 = relay.TupleGetItem(func_1072_call(), 2)
call_3584 = relay.TupleGetItem(func_1073_call(), 2)
func_3276_call = mod.get_global_var('func_3276')
func_3277_call = mutated_mod.get_global_var('func_3277')
call_3589 = relay.TupleGetItem(func_3276_call(), 0)
call_3590 = relay.TupleGetItem(func_3277_call(), 0)
func_3169_call = mod.get_global_var('func_3169')
func_3171_call = mutated_mod.get_global_var('func_3171')
var_3596 = relay.var("var_3596", dtype = "int16", shape = (405,))#candidate|3596|(405,)|var|int16
call_3595 = relay.TupleGetItem(func_3169_call(relay.reshape(var_3596.astype('int16'), [3, 15, 9])), 0)
call_3597 = relay.TupleGetItem(func_3171_call(relay.reshape(var_3596.astype('int16'), [3, 15, 9])), 0)
func_2744_call = mod.get_global_var('func_2744')
func_2748_call = mutated_mod.get_global_var('func_2748')
var_3609 = relay.var("var_3609", dtype = "int16", shape = (110, 4))#candidate|3609|(110, 4)|var|int16
call_3608 = relay.TupleGetItem(func_2744_call(relay.reshape(var_3609.astype('int16'), [11, 8, 5]), relay.reshape(var_3609.astype('int16'), [11, 8, 5]), ), 0)
call_3610 = relay.TupleGetItem(func_2748_call(relay.reshape(var_3609.astype('int16'), [11, 8, 5]), relay.reshape(var_3609.astype('int16'), [11, 8, 5]), ), 0)
func_1677_call = mod.get_global_var('func_1677')
func_1678_call = mutated_mod.get_global_var('func_1678')
call_3611 = func_1677_call()
call_3612 = func_1677_call()
uop_3615 = relay.acosh(call_3608.astype('float64')) # shape=(11, 8, 5)
uop_3617 = relay.acosh(call_3610.astype('float64')) # shape=(11, 8, 5)
func_3203_call = mod.get_global_var('func_3203')
func_3204_call = mutated_mod.get_global_var('func_3204')
call_3631 = func_3203_call()
call_3632 = func_3203_call()
func_2932_call = mod.get_global_var('func_2932')
func_2935_call = mutated_mod.get_global_var('func_2935')
var_3652 = relay.var("var_3652", dtype = "float32", shape = (450,))#candidate|3652|(450,)|var|float32
call_3651 = relay.TupleGetItem(func_2932_call(relay.reshape(var_3652.astype('float32'), [450,])), 3)
call_3653 = relay.TupleGetItem(func_2935_call(relay.reshape(var_3652.astype('float32'), [450,])), 3)
output = relay.Tuple([call_3575,call_3583,call_3589,call_3595,var_3596,var_3609,call_3611,uop_3615,call_3631,call_3651,var_3652,])
output2 = relay.Tuple([call_3576,call_3584,call_3590,call_3597,var_3596,var_3609,call_3612,uop_3617,call_3632,call_3653,var_3652,])
func_3655 = relay.Function([var_3596,var_3609,var_3652,], output)
mod['func_3655'] = func_3655
mod = relay.transform.InferType()(mod)
var_3656 = relay.var("var_3656", dtype = "int16", shape = (405,))#candidate|3656|(405,)|var|int16
var_3657 = relay.var("var_3657", dtype = "int16", shape = (110, 4))#candidate|3657|(110, 4)|var|int16
var_3658 = relay.var("var_3658", dtype = "float32", shape = (450,))#candidate|3658|(450,)|var|float32
output = func_3655(var_3656,var_3657,var_3658,)
func_3659 = relay.Function([var_3656,var_3657,var_3658,], output)
mutated_mod['func_3659'] = func_3659
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3679 = relay.var("var_3679", dtype = "float32", shape = (15, 14, 12))#candidate|3679|(15, 14, 12)|var|float32
uop_3680 = relay.acosh(var_3679.astype('float32')) # shape=(15, 14, 12)
func_2340_call = mod.get_global_var('func_2340')
func_2343_call = mutated_mod.get_global_var('func_2343')
var_3691 = relay.var("var_3691", dtype = "float64", shape = (675,))#candidate|3691|(675,)|var|float64
var_3692 = relay.var("var_3692", dtype = "float32", shape = (144,))#candidate|3692|(144,)|var|float32
call_3690 = relay.TupleGetItem(func_2340_call(relay.reshape(var_3691.astype('float64'), [15, 3, 15]), relay.reshape(var_3692.astype('float32'), [144,]), ), 0)
call_3693 = relay.TupleGetItem(func_2343_call(relay.reshape(var_3691.astype('float64'), [15, 3, 15]), relay.reshape(var_3692.astype('float32'), [144,]), ), 0)
func_2816_call = mod.get_global_var('func_2816')
func_2818_call = mutated_mod.get_global_var('func_2818')
call_3704 = func_2816_call()
call_3705 = func_2816_call()
uop_3710 = relay.erf(uop_3680.astype('float32')) # shape=(15, 14, 12)
output = relay.Tuple([call_3690,var_3691,var_3692,call_3704,uop_3710,])
output2 = relay.Tuple([call_3693,var_3691,var_3692,call_3705,uop_3710,])
func_3712 = relay.Function([var_3679,var_3691,var_3692,], output)
mod['func_3712'] = func_3712
mod = relay.transform.InferType()(mod)
mutated_mod['func_3712'] = func_3712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3712_call = mutated_mod.get_global_var('func_3712')
var_3714 = relay.var("var_3714", dtype = "float32", shape = (15, 14, 12))#candidate|3714|(15, 14, 12)|var|float32
var_3715 = relay.var("var_3715", dtype = "float64", shape = (675,))#candidate|3715|(675,)|var|float64
var_3716 = relay.var("var_3716", dtype = "float32", shape = (144,))#candidate|3716|(144,)|var|float32
call_3713 = func_3712_call(var_3714,var_3715,var_3716,)
output = call_3713
func_3717 = relay.Function([var_3714,var_3715,var_3716,], output)
mutated_mod['func_3717'] = func_3717
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3762 = relay.const(-6, dtype = "uint32")#candidate|3762|()|const|uint32
var_3763 = relay.var("var_3763", dtype = "uint32", shape = (1, 7))#candidate|3763|(1, 7)|var|uint32
bop_3764 = relay.add(const_3762.astype('uint32'), var_3763.astype('uint32')) # shape=(1, 7)
output = relay.Tuple([bop_3764,])
output2 = relay.Tuple([bop_3764,])
func_3767 = relay.Function([var_3763,], output)
mod['func_3767'] = func_3767
mod = relay.transform.InferType()(mod)
var_3768 = relay.var("var_3768", dtype = "uint32", shape = (1, 7))#candidate|3768|(1, 7)|var|uint32
output = func_3767(var_3768)
func_3769 = relay.Function([var_3768], output)
mutated_mod['func_3769'] = func_3769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1677_call = mod.get_global_var('func_1677')
func_1678_call = mutated_mod.get_global_var('func_1678')
call_3793 = func_1677_call()
call_3794 = func_1677_call()
uop_3796 = relay.asin(call_3793.astype('float64')) # shape=(3, 1, 9)
uop_3798 = relay.asin(call_3794.astype('float64')) # shape=(3, 1, 9)
func_2386_call = mod.get_global_var('func_2386')
func_2388_call = mutated_mod.get_global_var('func_2388')
call_3809 = relay.TupleGetItem(func_2386_call(), 0)
call_3810 = relay.TupleGetItem(func_2388_call(), 0)
var_3811 = relay.var("var_3811", dtype = "float64", shape = (3, 5, 9))#candidate|3811|(3, 5, 9)|var|float64
bop_3812 = relay.not_equal(uop_3796.astype('bool'), var_3811.astype('bool')) # shape=(3, 5, 9)
bop_3815 = relay.not_equal(uop_3798.astype('bool'), var_3811.astype('bool')) # shape=(3, 5, 9)
func_2557_call = mod.get_global_var('func_2557')
func_2561_call = mutated_mod.get_global_var('func_2561')
var_3827 = relay.var("var_3827", dtype = "int16", shape = (660,))#candidate|3827|(660,)|var|int16
var_3828 = relay.var("var_3828", dtype = "int8", shape = (770,))#candidate|3828|(770,)|var|int8
call_3826 = relay.TupleGetItem(func_2557_call(relay.reshape(var_3827.astype('int16'), [4, 15, 11]), relay.reshape(var_3827.astype('float64'), [4, 15, 11]), relay.reshape(var_3828.astype('int8'), [770,]), ), 2)
call_3829 = relay.TupleGetItem(func_2561_call(relay.reshape(var_3827.astype('int16'), [4, 15, 11]), relay.reshape(var_3827.astype('float64'), [4, 15, 11]), relay.reshape(var_3828.astype('int8'), [770,]), ), 2)
output = relay.Tuple([call_3809,bop_3812,call_3826,var_3827,var_3828,])
output2 = relay.Tuple([call_3810,bop_3815,call_3829,var_3827,var_3828,])
func_3834 = relay.Function([var_3811,var_3827,var_3828,], output)
mod['func_3834'] = func_3834
mod = relay.transform.InferType()(mod)
var_3835 = relay.var("var_3835", dtype = "float64", shape = (3, 5, 9))#candidate|3835|(3, 5, 9)|var|float64
var_3836 = relay.var("var_3836", dtype = "int16", shape = (660,))#candidate|3836|(660,)|var|int16
var_3837 = relay.var("var_3837", dtype = "int8", shape = (770,))#candidate|3837|(770,)|var|int8
output = func_3834(var_3835,var_3836,var_3837,)
func_3838 = relay.Function([var_3835,var_3836,var_3837,], output)
mutated_mod['func_3838'] = func_3838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2042_call = mod.get_global_var('func_2042')
func_2043_call = mutated_mod.get_global_var('func_2043')
call_3888 = relay.TupleGetItem(func_2042_call(), 0)
call_3889 = relay.TupleGetItem(func_2043_call(), 0)
var_3902 = relay.var("var_3902", dtype = "bool", shape = (3, 1, 9))#candidate|3902|(3, 1, 9)|var|bool
bop_3903 = relay.mod(call_3888.astype('float32'), relay.reshape(var_3902.astype('float32'), relay.shape_of(call_3888))) # shape=(3, 1, 9)
bop_3906 = relay.mod(call_3889.astype('float32'), relay.reshape(var_3902.astype('float32'), relay.shape_of(call_3889))) # shape=(3, 1, 9)
output = bop_3903
output2 = bop_3906
func_3907 = relay.Function([var_3902,], output)
mod['func_3907'] = func_3907
mod = relay.transform.InferType()(mod)
mutated_mod['func_3907'] = func_3907
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3908 = relay.var("var_3908", dtype = "bool", shape = (3, 1, 9))#candidate|3908|(3, 1, 9)|var|bool
func_3907_call = mutated_mod.get_global_var('func_3907')
call_3909 = func_3907_call(var_3908)
output = call_3909
func_3910 = relay.Function([var_3908], output)
mutated_mod['func_3910'] = func_3910
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1677_call = mod.get_global_var('func_1677')
func_1678_call = mutated_mod.get_global_var('func_1678')
call_3962 = func_1677_call()
call_3963 = func_1677_call()
const_3972 = relay.const([[[False,False,False,False,False,False,True,False,False],[True,False,False,True,False,False,False,True,False],[False,False,False,False,False,False,False,True,False],[True,True,False,True,True,False,True,True,False],[True,False,True,False,False,True,False,True,True],[True,True,False,True,True,True,True,False,True],[False,False,False,False,True,True,True,True,False],[True,False,False,False,False,False,True,False,False],[False,False,True,False,True,False,False,False,False],[True,False,False,False,False,False,True,False,False],[False,True,True,True,True,True,True,True,True],[True,False,True,False,False,False,True,False,True],[False,True,False,False,False,False,False,True,False],[False,False,False,False,False,False,True,True,True],[True,False,False,False,False,False,False,False,False]],[[False,True,True,True,True,False,True,True,False],[True,True,True,True,False,True,False,False,False],[False,False,True,True,True,False,True,True,False],[True,True,False,True,True,True,False,True,True],[False,False,False,True,False,False,False,True,False],[False,True,False,False,True,False,True,False,True],[True,True,True,True,False,False,True,False,False],[True,False,True,False,True,True,False,False,True],[False,False,True,False,False,False,True,False,False],[True,False,False,True,True,False,False,True,False],[False,False,False,False,True,True,True,True,False],[True,False,False,False,False,False,True,True,True],[False,False,True,False,True,True,False,False,True],[False,False,False,True,True,False,True,True,False],[False,True,True,False,False,True,False,False,False]],[[True,False,True,False,False,True,True,False,False],[True,False,True,False,True,True,False,False,False],[False,True,False,False,False,True,False,False,True],[True,True,True,True,False,True,False,False,True],[True,True,True,False,False,False,True,False,True],[False,False,True,True,True,False,True,True,False],[False,True,True,True,True,False,False,False,False],[False,True,False,True,False,True,True,False,False],[True,True,False,False,False,True,True,True,False],[True,False,True,False,False,True,True,True,False],[True,True,False,True,True,True,True,True,False],[False,False,False,False,True,False,True,True,False],[False,False,True,False,True,True,True,True,True],[False,False,False,False,True,True,True,False,True],[False,True,False,False,False,False,True,False,True]]], dtype = "bool")#candidate|3972|(3, 15, 9)|const|bool
bop_3973 = relay.less_equal(call_3962.astype('bool'), const_3972.astype('bool')) # shape=(3, 15, 9)
bop_3976 = relay.less_equal(call_3963.astype('bool'), const_3972.astype('bool')) # shape=(3, 15, 9)
uop_3984 = relay.acosh(const_3972.astype('float32')) # shape=(3, 15, 9)
func_1310_call = mod.get_global_var('func_1310')
func_1313_call = mutated_mod.get_global_var('func_1313')
var_3988 = relay.var("var_3988", dtype = "float32", shape = (72, 2))#candidate|3988|(72, 2)|var|float32
const_3989 = relay.const([4.772617,-0.971236,-2.651348,-1.952326,-1.263014,1.636711,-6.737575,9.150396,-5.765508,-1.950012,-1.474461,-4.792523,0.333058,-8.226804,1.465313,-4.484865,-7.686169,-1.990726,-4.340391,1.776215,6.113548,-5.168158,6.978792,-1.140367,-5.837726,6.150823,7.384852,2.425142,-0.429168,8.142129,-5.750629,-2.978198,3.127252,-1.494441,8.724603,-2.323765,-3.829021,-9.020744,3.652037,2.646006,0.703010,-2.279247,-7.005289,-5.252668,1.901096,-1.749817,3.468502,6.870151,3.487835,0.380402,2.837796,6.277972,-8.127465,-4.022395,-8.538252,0.478176,-8.699359,-8.491823,-0.162774,9.157104,6.217911,3.313045,-0.063008,2.707904,-1.357991,2.227601,-7.326787,3.580044,-0.607309,-8.246410,1.528050,5.992642,-7.006659,-4.773159,-1.088881,-4.800058,2.857514,-4.364265,-6.621984,1.628343,-2.563263,9.936581,5.813880,-0.909075,-6.885837,-6.172152,-4.939132,0.967359,-7.255504,7.481434,0.682518,-8.825309,-5.269068,-1.071510,-4.247776,8.790161,-6.765193,2.841983,-4.553799,-5.077949,5.184758,-3.604730,-1.658377,-6.095609,-3.269547,4.160864,4.427820,-2.271877,-4.098099,3.308680,9.155021,-6.153393,8.300908,4.300963,0.222281,-1.712802,1.192531,-8.215817,-5.052979,-5.030119,9.701008,-9.407200,5.394296,-3.245860,7.350959,-1.576756,-1.945537,4.935190,-9.736003,2.332689,-5.914724,-3.694560,6.645685,6.797928,4.853441,-3.991050,9.299992,-6.426055,1.892538,-9.144767,-7.323217,6.789691,0.211453,-9.715492,-2.358025,6.013212,1.593558,-4.093814,7.777230,-2.727001,1.827453,2.450883,5.134146,1.871676,-3.008071,8.044010,-9.921959,6.314283,0.049621,8.389678,-7.385966,-1.545066,5.415939,-9.165365,-0.158583,9.572205,5.351328,-6.766375,-7.052449,1.078743,-7.037157,4.607732,-9.018378,-7.234979,-0.693169,8.355054,5.959361,-3.465565,-9.396987,9.725265,8.809090,-7.382868,1.242077,9.592293,-9.004021,-9.688569,-4.686647,9.224119,-5.557417,-4.884316,5.594897,1.678587,-3.913054,2.349537,-9.284210,2.644026,-3.129672,-3.994425,5.595457,6.328007,1.663760,-4.749724,-7.254805,-3.414055,9.492770,8.329637,-8.437377,3.163456,6.276482,5.698474,7.175088,0.753173,-2.269962,4.251523,-9.027858,7.399742,-5.832015,5.058166,0.563261,-2.469043,-5.397382,4.947729,-2.037291,9.359228,-1.486289,-6.473057,-9.053371,8.078237,2.137397,-0.609355,0.270284,9.600467,7.857157,-1.781515,-2.842215,4.099319,2.923604,3.733318,-1.947383,9.747363,9.512389,-5.281851,9.232844,-0.561340,8.676222,-1.179227,-0.575831,-8.993763,-2.143471,-6.762445,5.484506,-2.081911,9.521760,2.949181,-0.598229,-5.073169,-1.375373,0.415027,-0.870013,-1.468176,-6.422264,-0.276922,4.636992,-7.606193,-4.141925,-2.712708,7.393425,-7.201753,6.513431,-9.611859,-3.337323,8.277447,3.325102,-9.480580,2.718902,4.567505,-0.227667,-6.797634,4.721344,0.303380,-6.722638,6.596039,-3.833680,-1.899464,5.170139,-6.810882,4.464273,-7.476548,-4.573863,-1.719907,-6.123982,-4.178289,9.002051,-2.714393,1.573486,-0.786252,9.542202,3.056613,6.666003,1.748252,-0.855872,-0.010666,-0.027176,6.732519,-2.432040,-8.875787,4.980404,0.424897,6.555737,1.724351,5.142571,-9.827943,-9.936644,2.708434,9.510191,-4.170825,-2.515666,2.240745,-8.258954,3.982336,-2.353307,4.935207,-5.446381,6.677500,-2.342530,2.874635,-4.268571,-2.687445,8.772243,8.526434,8.779087,4.562035,-9.946127,-3.550530,3.471376,5.458892,7.362491,0.120115,9.999270,3.596838,-2.465565,-1.806963,3.837612,8.776649,-4.610351,7.489286,-3.565922,7.730318,-2.430576,1.314204,3.774877,4.514405,8.951778,1.253006,7.048197,-8.160492,7.619017,9.381655,-3.016876,7.808114,0.484106,-1.288415,2.643255,-6.580190,0.807007,5.132722,8.243357,4.047466,-1.432541,3.879665,5.627936,2.112653,-3.413897,5.905958,2.449270,5.466822,-3.559394,-3.643997,7.424140,3.563773,9.840044,-2.334731,9.377009,4.007718,-1.575203,-9.662469,2.414431,-3.664404,-5.091279,-7.963356,-7.353366,-2.356910,3.686708,2.348472,6.607114,7.137924,7.359406,2.005311,4.222209,-6.178100,-1.284565,6.267659,-1.057536,6.854585,-1.865219,-9.740455,-3.886824,1.633765,-3.287924,-9.370128,5.801753,-4.126321,8.044839,2.089302,-9.614678,-2.150416,-2.686818,-6.661157,0.764629,1.238529,3.829682,7.015479,-4.301552,7.453935,0.232778,3.596681,7.468483,3.568350,1.033220,3.124880,1.978712,-9.328276,-5.705492,-1.961979,7.462818,4.907048,-4.252099,-4.599993,8.528410,0.965437,5.076230,0.498347,-5.606752,-7.892103,9.302797,9.416915,4.278321,9.970559,2.195217,-5.218731], dtype = "float32")#candidate|3989|(450,)|const|float32
call_3987 = relay.TupleGetItem(func_1310_call(relay.reshape(var_3988.astype('float32'), [16, 1, 9]), relay.reshape(const_3989.astype('float32'), [450,]), ), 1)
call_3990 = relay.TupleGetItem(func_1313_call(relay.reshape(var_3988.astype('float32'), [16, 1, 9]), relay.reshape(const_3989.astype('float32'), [450,]), ), 1)
func_3231_call = mod.get_global_var('func_3231')
func_3233_call = mutated_mod.get_global_var('func_3233')
call_3995 = relay.TupleGetItem(func_3231_call(), 1)
call_3996 = relay.TupleGetItem(func_3233_call(), 1)
func_3169_call = mod.get_global_var('func_3169')
func_3171_call = mutated_mod.get_global_var('func_3171')
call_3997 = relay.TupleGetItem(func_3169_call(relay.reshape(uop_3984.astype('int16'), [3, 15, 9])), 1)
call_3998 = relay.TupleGetItem(func_3171_call(relay.reshape(uop_3984.astype('int16'), [3, 15, 9])), 1)
uop_4003 = relay.sinh(uop_3984.astype('float64')) # shape=(3, 15, 9)
output = relay.Tuple([bop_3973,call_3987,var_3988,const_3989,call_3995,call_3997,uop_4003,])
output2 = relay.Tuple([bop_3976,call_3990,var_3988,const_3989,call_3996,call_3998,uop_4003,])
func_4024 = relay.Function([var_3988,], output)
mod['func_4024'] = func_4024
mod = relay.transform.InferType()(mod)
var_4025 = relay.var("var_4025", dtype = "float32", shape = (72, 2))#candidate|4025|(72, 2)|var|float32
output = func_4024(var_4025)
func_4026 = relay.Function([var_4025], output)
mutated_mod['func_4026'] = func_4026
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4028 = relay.const([[[-4,8,-1,-5,4,-3,-8,7,-8,4,-2,-5,-8,1,-5],[-5,-3,7,1,2,-2,2,6,9,-2,-8,-5,3,3,-3],[4,-7,10,-10,-8,8,-9,-1,10,9,-2,6,-1,3,3],[-2,3,-4,3,-5,8,10,-4,2,-2,-5,7,2,-10,-4]]], dtype = "int32")#candidate|4028|(1, 4, 15)|const|int32
const_4029 = relay.const([[[-10,5,-7,9,1,5,-7,-4,-10,8,-1,-7,-5,-7,-10],[4,7,7,2,-5,-5,4,-9,1,-5,7,5,6,-10,8],[-7,3,4,9,6,-6,-6,3,9,5,2,-7,-7,-7,-7],[9,7,-1,2,6,-5,8,-5,7,4,7,5,3,10,-8]],[[-4,2,-9,-4,-2,-8,5,10,-7,-5,10,-7,7,-8,-9],[-5,-3,6,-7,-4,3,5,10,-7,4,-9,3,9,5,8],[-4,-1,-9,3,-9,4,-3,-9,4,-1,7,3,6,-3,-1],[-7,5,4,-6,7,-3,7,-10,8,-4,4,-9,-3,-1,5]],[[9,-7,-9,6,7,1,6,6,6,-2,5,4,-3,8,-5],[-5,5,9,-10,-1,10,-7,-2,10,8,-8,8,-6,9,4],[-7,8,-1,-9,-2,10,-4,6,-1,-2,10,4,2,-10,6],[-4,-5,6,-7,-6,7,1,-4,-5,-7,6,9,-9,1,-1]],[[-5,1,-5,-3,2,-5,7,10,7,6,4,-3,-3,-3,2],[-3,-9,7,9,-10,1,-2,1,2,9,2,-2,-8,9,-9],[-7,8,-5,2,6,9,-7,-8,4,6,7,-1,-5,4,-10],[5,-5,5,-9,-8,-9,2,9,-2,-9,-8,-8,-5,-8,7]],[[2,-7,-6,-9,-9,9,3,4,3,-4,-6,-1,1,-7,5],[-9,7,-5,10,9,-8,-9,-2,-2,-9,-1,9,9,-10,-1],[4,3,9,8,10,1,8,1,-3,6,9,8,9,-10,-8],[5,4,-5,4,4,-9,-5,7,6,1,3,-1,-10,10,1]],[[-4,10,-2,10,-6,-3,-1,3,-6,-9,3,9,-5,-4,2],[3,-2,5,-7,4,-1,-8,5,8,10,-10,-1,7,-9,-1],[8,8,-6,-6,8,-6,-4,1,8,3,-9,3,10,-4,-2],[-4,8,10,5,-8,-5,3,-1,-1,4,-8,-4,2,10,-7]],[[-10,1,-10,-5,7,9,-10,-1,7,-3,-5,3,-2,5,1],[-4,-10,-1,8,-7,-1,-8,9,3,3,-6,-7,-8,-3,2],[-5,-7,3,-7,-5,-7,1,9,-5,3,-10,-8,7,7,1],[8,-6,-2,4,-10,-4,-7,-2,-2,-1,-9,-3,10,-3,1]],[[-8,9,-5,-5,-8,10,-3,6,5,6,-2,-1,-10,-6,9],[6,-8,3,3,2,2,5,9,3,-9,2,-2,10,-3,6],[6,1,-6,-7,10,-4,1,8,-1,4,9,-5,8,-4,2],[4,1,-1,-8,8,8,-10,1,9,-10,4,-10,2,-4,10]],[[8,3,-7,-8,5,-3,-6,-3,5,-9,-6,8,-3,5,-9],[-5,-9,6,-5,1,10,2,-10,-3,7,-2,8,-1,10,-10],[3,4,6,-7,6,-10,3,2,-8,-8,8,10,-8,7,-8],[-7,-4,10,2,-2,7,-5,-5,4,2,10,10,4,-2,-7]],[[7,9,6,-9,9,9,3,-6,10,4,10,2,6,1,6],[-8,4,2,9,8,-5,5,10,-8,1,-2,8,2,-9,-1],[3,-6,9,8,-1,7,3,4,3,-6,6,5,2,-9,2],[-6,1,3,9,-7,8,-4,6,-6,10,3,-10,1,8,4]]], dtype = "int32")#candidate|4029|(10, 4, 15)|const|int32
bop_4030 = relay.less(const_4028.astype('bool'), const_4029.astype('bool')) # shape=(10, 4, 15)
func_2016_call = mod.get_global_var('func_2016')
func_2018_call = mutated_mod.get_global_var('func_2018')
call_4038 = relay.TupleGetItem(func_2016_call(), 0)
call_4039 = relay.TupleGetItem(func_2018_call(), 0)
bop_4044 = relay.subtract(bop_4030.astype('int16'), relay.reshape(const_4029.astype('int16'), relay.shape_of(bop_4030))) # shape=(10, 4, 15)
output = relay.Tuple([call_4038,bop_4044,])
output2 = relay.Tuple([call_4039,bop_4044,])
func_4047 = relay.Function([], output)
mod['func_4047'] = func_4047
mod = relay.transform.InferType()(mod)
output = func_4047()
func_4048 = relay.Function([], output)
mutated_mod['func_4048'] = func_4048
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4056 = relay.var("var_4056", dtype = "float32", shape = (9, 15, 10))#candidate|4056|(9, 15, 10)|var|float32
uop_4057 = relay.sqrt(var_4056.astype('float32')) # shape=(9, 15, 10)
output = relay.Tuple([uop_4057,])
output2 = relay.Tuple([uop_4057,])
func_4061 = relay.Function([var_4056,], output)
mod['func_4061'] = func_4061
mod = relay.transform.InferType()(mod)
var_4062 = relay.var("var_4062", dtype = "float32", shape = (9, 15, 10))#candidate|4062|(9, 15, 10)|var|float32
output = func_4061(var_4062)
func_4063 = relay.Function([var_4062], output)
mutated_mod['func_4063'] = func_4063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3258_call = mod.get_global_var('func_3258')
func_3260_call = mutated_mod.get_global_var('func_3260')
call_4149 = relay.TupleGetItem(func_3258_call(), 0)
call_4150 = relay.TupleGetItem(func_3260_call(), 0)
uop_4152 = relay.tan(call_4149.astype('float32')) # shape=(16, 14, 6)
uop_4154 = relay.tan(call_4150.astype('float32')) # shape=(16, 14, 6)
bop_4160 = relay.add(uop_4152.astype('uint8'), relay.reshape(call_4149.astype('uint8'), relay.shape_of(uop_4152))) # shape=(16, 14, 6)
bop_4163 = relay.add(uop_4154.astype('uint8'), relay.reshape(call_4150.astype('uint8'), relay.shape_of(uop_4154))) # shape=(16, 14, 6)
output = bop_4160
output2 = bop_4163
func_4166 = relay.Function([], output)
mod['func_4166'] = func_4166
mod = relay.transform.InferType()(mod)
output = func_4166()
func_4167 = relay.Function([], output)
mutated_mod['func_4167'] = func_4167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2816_call = mod.get_global_var('func_2816')
func_2818_call = mutated_mod.get_global_var('func_2818')
call_4199 = func_2816_call()
call_4200 = func_2816_call()
output = relay.Tuple([call_4199,])
output2 = relay.Tuple([call_4200,])
func_4206 = relay.Function([], output)
mod['func_4206'] = func_4206
mod = relay.transform.InferType()(mod)
output = func_4206()
func_4207 = relay.Function([], output)
mutated_mod['func_4207'] = func_4207
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1249_call = mod.get_global_var('func_1249')
func_1251_call = mutated_mod.get_global_var('func_1251')
call_4247 = relay.TupleGetItem(func_1249_call(), 1)
call_4248 = relay.TupleGetItem(func_1251_call(), 1)
var_4249 = relay.var("var_4249", dtype = "float64", shape = (450,))#candidate|4249|(450,)|var|float64
bop_4250 = relay.left_shift(call_4247.astype('int64'), relay.reshape(var_4249.astype('int64'), relay.shape_of(call_4247))) # shape=(450,)
bop_4253 = relay.left_shift(call_4248.astype('int64'), relay.reshape(var_4249.astype('int64'), relay.shape_of(call_4248))) # shape=(450,)
func_2016_call = mod.get_global_var('func_2016')
func_2018_call = mutated_mod.get_global_var('func_2018')
call_4254 = relay.TupleGetItem(func_2016_call(), 0)
call_4255 = relay.TupleGetItem(func_2018_call(), 0)
func_1742_call = mod.get_global_var('func_1742')
func_1745_call = mutated_mod.get_global_var('func_1745')
call_4276 = relay.TupleGetItem(func_1742_call(relay.reshape(call_4254.astype('float64'), [])), 1)
call_4277 = relay.TupleGetItem(func_1745_call(relay.reshape(call_4254.astype('float64'), [])), 1)
output = relay.Tuple([bop_4250,call_4254,call_4276,])
output2 = relay.Tuple([bop_4253,call_4255,call_4277,])
func_4278 = relay.Function([var_4249,], output)
mod['func_4278'] = func_4278
mod = relay.transform.InferType()(mod)
var_4279 = relay.var("var_4279", dtype = "float64", shape = (450,))#candidate|4279|(450,)|var|float64
output = func_4278(var_4279)
func_4280 = relay.Function([var_4279], output)
mutated_mod['func_4280'] = func_4280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2016_call = mod.get_global_var('func_2016')
func_2018_call = mutated_mod.get_global_var('func_2018')
call_4314 = relay.TupleGetItem(func_2016_call(), 0)
call_4315 = relay.TupleGetItem(func_2018_call(), 0)
output = call_4314
output2 = call_4315
func_4320 = relay.Function([], output)
mod['func_4320'] = func_4320
mod = relay.transform.InferType()(mod)
output = func_4320()
func_4321 = relay.Function([], output)
mutated_mod['func_4321'] = func_4321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3203_call = mod.get_global_var('func_3203')
func_3204_call = mutated_mod.get_global_var('func_3204')
call_4338 = func_3203_call()
call_4339 = func_3203_call()
func_1677_call = mod.get_global_var('func_1677')
func_1678_call = mutated_mod.get_global_var('func_1678')
call_4359 = func_1677_call()
call_4360 = func_1677_call()
uop_4363 = relay.rsqrt(call_4359.astype('float64')) # shape=(3, 1, 9)
uop_4365 = relay.rsqrt(call_4360.astype('float64')) # shape=(3, 1, 9)
output = relay.Tuple([call_4338,uop_4363,])
output2 = relay.Tuple([call_4339,uop_4365,])
func_4370 = relay.Function([], output)
mod['func_4370'] = func_4370
mod = relay.transform.InferType()(mod)
mutated_mod['func_4370'] = func_4370
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4370_call = mutated_mod.get_global_var('func_4370')
call_4371 = func_4370_call()
output = call_4371
func_4372 = relay.Function([], output)
mutated_mod['func_4372'] = func_4372
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4206_call = mod.get_global_var('func_4206')
func_4207_call = mutated_mod.get_global_var('func_4207')
call_4414 = relay.TupleGetItem(func_4206_call(), 0)
call_4415 = relay.TupleGetItem(func_4207_call(), 0)
func_2386_call = mod.get_global_var('func_2386')
func_2388_call = mutated_mod.get_global_var('func_2388')
call_4420 = relay.TupleGetItem(func_2386_call(), 0)
call_4421 = relay.TupleGetItem(func_2388_call(), 0)
output = relay.Tuple([call_4414,call_4420,])
output2 = relay.Tuple([call_4415,call_4421,])
func_4437 = relay.Function([], output)
mod['func_4437'] = func_4437
mod = relay.transform.InferType()(mod)
output = func_4437()
func_4438 = relay.Function([], output)
mutated_mod['func_4438'] = func_4438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2016_call = mod.get_global_var('func_2016')
func_2018_call = mutated_mod.get_global_var('func_2018')
call_4453 = relay.TupleGetItem(func_2016_call(), 0)
call_4454 = relay.TupleGetItem(func_2018_call(), 0)
output = relay.Tuple([call_4453,])
output2 = relay.Tuple([call_4454,])
func_4471 = relay.Function([], output)
mod['func_4471'] = func_4471
mod = relay.transform.InferType()(mod)
output = func_4471()
func_4472 = relay.Function([], output)
mutated_mod['func_4472'] = func_4472
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4502 = relay.var("var_4502", dtype = "int8", shape = (10, 6, 8))#candidate|4502|(10, 6, 8)|var|int8
var_4503 = relay.var("var_4503", dtype = "int8", shape = (10, 6, 8))#candidate|4503|(10, 6, 8)|var|int8
bop_4504 = relay.minimum(var_4502.astype('int8'), relay.reshape(var_4503.astype('int8'), relay.shape_of(var_4502))) # shape=(10, 6, 8)
func_1170_call = mod.get_global_var('func_1170')
func_1172_call = mutated_mod.get_global_var('func_1172')
call_4516 = relay.TupleGetItem(func_1170_call(), 1)
call_4517 = relay.TupleGetItem(func_1172_call(), 1)
const_4521 = relay.const([[[-10,3,8,3,4,3,4,7],[5,-7,-2,-6,-7,-1,9,-4],[-10,6,-10,4,-9,-2,-8,-4],[-2,-9,10,-7,-8,-9,-8,3],[3,3,-10,-7,-5,-3,8,7],[-8,8,2,9,4,7,3,7]],[[1,9,-9,2,5,-9,5,-5],[-4,3,8,6,-9,3,4,10],[-2,-9,-5,-6,-6,-3,5,-6],[-3,-5,-10,-1,5,-3,-4,8],[-1,-6,8,7,9,7,-8,-10],[-1,-9,7,1,6,5,-8,5]],[[-2,8,-2,-5,2,4,-6,-10],[1,-9,-3,-4,-6,-8,-4,8],[5,5,10,10,-6,4,9,7],[5,-2,-8,-7,7,-3,-10,6],[-6,5,-3,-7,-9,8,-5,10],[3,-10,8,7,5,-6,-8,10]],[[-3,9,-10,-6,-7,7,-3,4],[8,-9,1,4,6,1,-2,10],[-6,5,7,-2,-8,-6,5,7],[6,-2,1,-3,7,3,-4,9],[1,-7,5,-3,-10,4,-1,-1],[-8,-3,10,-8,-9,8,-1,7]],[[-1,10,-6,9,-4,-3,3,-1],[8,9,-2,-7,-5,6,4,-10],[10,2,-5,-3,-3,3,10,-8],[9,-6,-4,2,10,9,-3,-10],[1,8,3,4,-8,4,10,-6],[-9,2,7,-7,3,-2,7,9]],[[2,-3,-3,-10,1,-10,-6,-3],[-1,2,-10,7,-7,10,-9,-9],[10,-5,-6,-3,1,-1,10,-3],[1,-10,-4,-4,4,-2,-3,-5],[4,6,-4,-10,-10,1,-7,2],[-2,8,-7,-7,-4,-5,4,2]],[[9,8,4,-8,9,8,-6,3],[-3,3,3,5,1,-8,8,-2],[7,10,-6,-10,2,2,-8,-5],[7,-3,10,-10,7,-7,-10,-4],[7,-10,6,1,-8,5,7,9],[10,6,1,2,-6,5,-5,10]],[[-4,-8,-2,8,1,8,-5,-4],[2,-4,6,2,-4,5,-7,3],[7,4,10,9,-7,-1,-5,-7],[3,-9,7,10,-8,1,9,-9],[-5,6,-6,9,4,-4,-5,6],[-2,8,4,-1,10,-8,-5,-7]],[[-1,-8,-10,10,8,-4,7,-2],[3,-8,-5,-1,-8,6,-7,4],[8,5,-10,3,-1,9,-7,6],[-1,8,3,3,-8,7,-3,-3],[2,8,-5,9,10,-1,-1,8],[1,-9,5,6,-2,9,3,-4]],[[-2,-8,-5,-10,-5,3,-9,-7],[5,5,-8,3,5,5,6,6],[4,-4,10,-6,-6,-2,-8,-5],[7,-4,2,-4,1,-6,9,-4],[7,1,-3,-4,-6,6,-5,8],[3,-6,-1,-6,10,-9,6,-3]]], dtype = "int8")#candidate|4521|(10, 6, 8)|const|int8
bop_4522 = relay.left_shift(var_4502.astype('uint32'), relay.reshape(const_4521.astype('uint32'), relay.shape_of(var_4502))) # shape=(10, 6, 8)
uop_4532 = relay.acos(bop_4522.astype('float32')) # shape=(10, 6, 8)
output = relay.Tuple([bop_4504,call_4516,uop_4532,])
output2 = relay.Tuple([bop_4504,call_4517,uop_4532,])
func_4538 = relay.Function([var_4502,var_4503,], output)
mod['func_4538'] = func_4538
mod = relay.transform.InferType()(mod)
var_4539 = relay.var("var_4539", dtype = "int8", shape = (10, 6, 8))#candidate|4539|(10, 6, 8)|var|int8
var_4540 = relay.var("var_4540", dtype = "int8", shape = (10, 6, 8))#candidate|4540|(10, 6, 8)|var|int8
output = func_4538(var_4539,var_4540,)
func_4541 = relay.Function([var_4539,var_4540,], output)
mutated_mod['func_4541'] = func_4541
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4437_call = mod.get_global_var('func_4437')
func_4438_call = mutated_mod.get_global_var('func_4438')
call_4585 = relay.TupleGetItem(func_4437_call(), 0)
call_4586 = relay.TupleGetItem(func_4438_call(), 0)
func_4061_call = mod.get_global_var('func_4061')
func_4063_call = mutated_mod.get_global_var('func_4063')
const_4603 = relay.const([-4.705222,-2.961912,3.798405,-3.470577,8.295895,-1.963701,-1.280120,7.408885,0.106684,9.150212,-6.172264,-5.519516,8.287139,5.531115,9.062383,-6.763443,-6.174396,-3.937026,-5.860663,7.784916,6.069111,6.649226,3.536311,6.517998,1.134516,-1.168491,-4.959690,6.767781,-0.475089,-7.513197,-5.835000,-1.966234,-6.304705,-7.204879,4.359880,-4.506391,-1.642786,-6.511964,-1.315411,-7.826482,2.914613,-7.868425,6.490698,3.394707,-2.822315,1.123826,6.604312,1.350545,-0.323950,-8.090446,8.825957,-5.088169,-2.036923,7.948317,5.593086,-3.026764,3.334005,-0.350645,-9.971979,-7.218560,-7.734827,3.752035,2.666686,5.170407,6.845834,8.020989,-8.333449,-3.462415,1.712243,-7.464384,4.371814,5.152026,3.058809,9.110169,0.503843,-8.889633,7.237940,8.661736,3.572821,-2.700532,-3.791683,9.413239,3.618077,4.486963,-4.490969,9.640192,6.696360,-5.718578,7.264718,-9.320437,1.084859,-8.029157,7.618221,-1.075775,-7.556802,5.726421,-9.068992,1.326311,-6.545198,-8.184710,-5.831105,-0.775556,-3.120162,-4.655633,-2.325123,1.045354,-6.942538,-0.651351,3.050041,-2.105031,4.193030,5.457419,-7.828792,7.423951,7.098965,5.265212,-8.290715,8.585461,-7.737329,-7.703859,6.520886,7.741919,6.666330,4.694380,-7.760395,-4.209949,6.372467,1.703874,-4.599582,-6.084192,5.477276,-7.801763,7.619753,-2.793666,6.934898,-3.711202,-4.249679,-1.239092,2.832123,7.006088,7.546674,7.814026,1.238795,0.784548,5.271255,0.209813,2.422377,-3.450453,-2.384541,6.165257,2.342649,-3.462738,3.841566,8.130566,-1.867531,-2.920131,-5.556837,-1.969952,-8.899578,-2.133265,2.636980,-7.256554,1.638820,2.215141,-2.394454,5.917790,-8.987469,8.193152,1.305431,-0.478778,1.370623,6.128698,-0.437388,0.502152,5.269969,-1.178348,-7.704840,-4.368278,-4.669150,0.041706,-8.096766,-7.861582,-4.831000,-4.074055,7.073318,5.988591,1.351520,-9.119909,-0.265253,-0.686610,5.635244,-0.259846,-9.316101,8.171394,-2.647620,3.720059,-4.104180,0.092646,8.201626,-3.190645,-0.891462,-6.556427,-4.694930,9.085109,-0.210459,5.155822,-8.749550,0.044130,-6.341750,7.155425,5.477454,0.088272,5.118822,-7.775900,-8.843424,8.691875,-9.598656,-0.154743,-8.351316,7.727825,2.882390,5.677138,-7.365549,-9.042027,3.870411,4.763110,-2.130143,-7.613825,2.949745,7.682964,1.243611,-1.926763,-2.154684,1.827769,-6.207897,9.226996,6.946671,-1.018966,-9.738165,-4.136391,-0.682884,-5.290697,-9.427839,-7.655645,-0.292992,1.019365,-8.555118,7.551251,-6.606760,-8.030149,-3.198465,-1.228001,-9.491590,6.423360,-8.558638,-6.688249,-8.865219,2.171144,-9.139249,-6.737083,2.682848,-2.203960,-8.072666,-6.900624,-1.234811,1.348535,9.972672,-9.046501,-7.591968,-6.809776,8.743563,-8.399367,2.316663,-1.550863,3.411311,-6.566892,-5.934624,8.048016,5.764232,2.016688,-1.247857,-3.885898,3.711065,3.568710,-6.188823,-7.625830,-3.373684,8.663391,-9.465890,4.016065,6.314188,1.446312,7.319474,-6.289802,-8.602763,-8.821444,-0.142875,-8.907183,-8.349254,-4.558349,9.511277,-4.790740,3.022873,-8.255786,-1.811473,5.986253,7.510801,1.290142,3.229275,3.680507,-6.123277,-9.787211,-0.069449,-1.452142,-2.272224,-5.187605,2.583721,-3.564384,-8.352122,-0.747264,-3.677128,-6.482178,-0.738439,-6.861871,2.167914,-1.259111,-7.348032,8.878077,6.015858,0.297507,-3.531126,-0.223719,-0.208563,-0.266749,8.621537,2.850078,-2.786851,1.581567,-2.431308,0.846177,-1.081510,2.529961,-9.247501,2.406343,-9.929678,-3.012156,-7.312952,-3.099435,7.939341,-4.339506,1.228629,-2.731972,5.746644,7.048770,-0.765121,-6.306581,-3.775979,3.533468,-1.523268,-7.626777,5.137063,5.968051,4.994897,-5.942017,-2.941999,1.216386,6.155056,3.530667,-7.993943,-6.389816,0.874742,8.043524,-6.129500,3.600823,6.347512,1.850975,-0.509707,6.411174,-1.259611,-5.082842,-5.806466,-6.914671,8.122253,-3.226071,-6.771755,-0.665824,3.202292,3.006233,-2.533603,-0.187199,3.930437,-0.447967,-6.913325,8.040103,-7.245098,3.786126,-8.614841,-6.932847,-3.217940,3.081360,8.141996,-0.184241,0.760521,-4.272874,-7.782802,4.999726,-2.352059,0.532999,9.317044,1.316122,-9.020005,-2.965527,-7.111215,0.686605,-4.770677,-5.750018,-4.098432,-1.033921,-3.167677,-8.207557,-0.433942,-9.137490,8.809771,8.043904,3.085977,-1.620729,-3.795128,-5.673578,0.376692,4.852259,-0.585050,2.398461,-6.803745,-9.607662,-0.211735,-7.947790,-8.004383,0.250505,-2.779912,8.296610,6.526579,-9.838129,-3.184673,6.133860,-8.783705,4.886902,-8.291313,6.441770,2.463198,8.700173,-8.099921,-3.663675,3.021801,6.443996,-7.075845,3.283947,-5.635931,6.160592,-0.752504,4.981567,8.741861,5.966411,1.631597,2.811823,-6.068245,3.616754,-7.435741,4.701512,5.396912,4.733753,2.716499,-4.029781,-1.614184,9.325614,-1.705249,6.444070,9.960975,7.303201,-1.442374,2.596825,2.849959,8.185992,-4.314301,1.323880,2.134410,-4.317315,7.133220,4.046041,-1.911422,-2.434661,7.741822,1.863393,-4.055993,1.973220,9.957053,7.088668,5.642892,-1.886460,-9.202117,-3.043414,-2.500305,-6.730672,3.563006,-0.004601,-4.813309,-1.021383,-9.826671,9.892694,-3.622167,2.347584,5.583386,-1.892725,-4.593125,2.408491,6.208006,-8.521613,-9.560501,8.308198,-5.954411,7.946228,6.685064,-4.604135,9.477123,-0.779134,1.764715,5.061758,0.579946,0.381430,-3.005614,-8.049711,-9.528459,-2.913253,4.103289,-7.536181,4.868587,1.617507,7.411620,-1.936556,0.512109,-1.193816,2.503322,5.625110,-1.667541,-5.834339,5.080972,-2.691792,1.282945,-3.653236,-9.537525,0.627163,6.446492,-5.448440,-9.913969,9.751750,-5.253197,-9.429500,-9.096878,-2.589866,0.057850,8.092686,5.085144,-5.290190,-2.555846,0.848215,-8.424983,-6.191762,1.387309,-8.285881,-4.400007,3.927692,-5.930703,-1.260845,-7.692079,2.808455,9.460168,-2.680999,-5.763129,4.215867,-0.791884,2.441438,7.579749,-9.730528,6.874572,7.142650,-8.599546,-3.353470,-9.521369,9.463867,4.118647,-6.321772,-5.579578,4.798835,-9.424785,7.145479,3.542381,0.178615,2.775593,-8.919611,-1.615884,-4.473600,-3.185502,7.802541,3.712924,2.230275,4.269399,1.213026,8.444052,-7.505061,6.924317,-3.388548,8.084563,-3.646835,6.785393,4.188137,-5.417424,-4.456608,-5.247355,7.270196,5.112080,-3.942282,0.115413,-9.203204,-5.925308,-0.781341,-6.753667,-1.243902,-4.698067,-6.771923,8.796253,6.408435,3.783121,5.599867,-2.478335,8.220223,3.525450,-5.003873,5.506117,4.861056,-2.348202,-7.439640,-8.207837,-8.884157,9.641733,-8.270519,-2.083598,-8.212004,-2.220718,2.175307,-3.220032,-4.192808,-5.332847,-7.257250,4.628697,0.412269,6.904926,-1.579301,-4.260532,-2.789197,-1.960458,1.584040,4.256718,-0.619330,1.443455,-9.709107,4.477686,2.097073,4.123042,8.321821,-0.445904,-4.956070,-3.472036,5.622619,9.303416,-1.137790,9.689908,-5.962522,1.420358,-4.287389,-6.690118,9.007448,5.457924,5.939693,-3.908697,5.136562,7.623924,6.823749,-3.415304,6.948175,-7.576268,0.632671,9.513877,-8.281042,2.837114,9.115486,6.208779,7.224745,8.224913,-4.486935,2.092954,-0.916116,2.412066,4.686772,4.837704,-9.016971,-4.736129,1.064437,4.894639,4.483679,-7.773567,9.405104,4.664711,-5.356042,2.525030,-4.244286,-0.072026,-2.765064,-0.791773,2.949212,-9.686282,-0.462539,-9.551156,-8.715675,8.690266,-1.314428,-6.734544,-1.995430,-5.700626,-3.502914,2.449526,-1.043707,-1.353455,8.329933,-6.008021,-4.345692,-2.469771,-8.036527,-2.604253,5.043190,-0.927023,0.818569,8.000404,-9.405658,-1.050739,1.497409,3.889006,1.571374,-5.670394,2.007413,2.081711,3.549492,-7.875568,-1.126349,-4.804044,-1.649095,8.705699,9.414220,5.268272,-1.035326,6.122677,0.500786,-0.242700,-2.363947,-2.305836,6.573160,0.083126,5.290982,-8.466677,-6.313430,7.683061,2.613216,-8.839795,9.238008,-3.225400,3.595985,-8.749642,4.546829,0.383510,6.019595,3.276349,3.109765,-0.072912,-2.858476,7.794294,3.264792,2.031834,7.560282,-1.722564,-0.141820,9.320561,-3.493156,-0.904830,-8.333471,7.276132,7.115046,-2.881180,8.211277,-2.365598,-0.814105,-9.975623,-2.329897,-7.058425,2.660952,5.453254,-9.756107,0.429989,-9.012126,-8.018241,7.752748,-0.513512,-9.517774,1.340490,2.010220,6.731113,8.859653,-0.777457,1.310937,-6.974575,8.479977,-0.733732,-6.284513,-5.354062,-7.593116,3.134901,-5.072024,-7.232984,-8.763776,-8.354514,0.288864,0.712536,6.053995,1.000183,0.384391,8.098514,2.077861,-8.673741,6.115432,-2.812198,0.833962,1.925543,3.758229,-5.319236,9.247263,-2.621923,-0.448807,-0.864422,0.258248,-3.015325,8.160487,8.567773,-4.613583,-2.084937,-8.801508,7.913231,-7.809540,1.249423,-7.466627,5.713548,-6.484740,6.733923,-5.377724,-1.933750,5.737728,-5.741618,-8.244448,0.444717,2.569662,-4.961096,-0.516340,3.171149,-8.743385,-1.678087,-0.268711,-1.456902,9.583433,8.901224,7.279853,0.223202,-1.538375,0.623379,0.989202,4.232521,-2.588931,-7.500359,3.330927,4.109434,-0.590370,4.339939,-4.226311,6.054375,1.181955,5.213158,-7.236479,1.702199,-9.973016,6.369228,6.845906,-7.931662,-6.032077,-7.697343,-2.805495,4.656768,2.534331,2.944792,7.435977,-0.346147,1.268170,0.706220,-3.720675,-6.985642,-1.481669,9.398873,5.406538,2.835079,-6.270121,4.163881,-8.931699,-1.781375,1.879367,8.045884,-3.964576,6.545293,5.070081,-8.435645,8.333887,-1.276098,-5.241613,2.452529,8.705618,-2.184687,-1.943506,-0.625938,-0.964769,2.204923,-6.608266,-6.510341,-0.044648,-7.986376,8.313776,3.376772,2.831432,-2.184690,9.945910,7.590098,-5.270188,1.589889,-5.139378,4.042145,-9.245185,-6.756785,5.054237,0.117460,6.871219,1.656056,-7.568230,9.082573,-6.251558,-0.436269,-8.777653,-1.120968,4.080077,0.977317,2.900817,-9.678969,0.916899,-9.719768,-4.335808,-3.013238,7.706273,-6.000094,9.174852,-7.396706,0.674102,3.434806,-0.851293,-9.773366,1.883347,7.665884,0.317595,-1.884495,1.398406,4.277490,8.350261,3.879448,-8.690440,-2.986552,1.626320,1.905721,8.259495,-0.620237,3.315200,7.976069,6.511631,9.656016,5.965045,0.011133,0.970163,-5.809890,7.391387,4.428883,8.799854,6.462736,-0.353380,4.050825,4.686057,-8.961086,-0.503146,-2.207758,-5.909570,-7.033304,9.590194,-0.054354,4.662146,7.964990,-6.919459,-1.461161,3.780684,5.694385,-6.359717,5.804890,-0.785118,-0.830366,-0.286127,-9.021651,3.528060,-3.282423,0.299026,2.220214,1.571344,0.537887,4.360938,5.451725,6.752456,2.980801,2.327554,6.671772,-7.259429,-5.760093,-0.056611,4.007489,-2.345563,3.990875,7.430908,-9.515937,7.180723,-1.497077,4.947048,3.833667,-4.916847,-1.977762,-3.326109,-0.786204,-6.503960,8.597809,4.134676,-6.136096,-8.117298,1.479937,-9.717099,-9.718219,2.404889,-0.516633,-0.648501,3.622355,-8.473129,-8.566957,-7.642227,2.302359,4.881057,3.996318,-6.450942,-6.177672,1.294996,-9.842507,2.590567,-7.050348,9.709227,3.212955,-0.640612,6.908146,9.967809,4.051429,-2.119555,-2.529769,8.353388,-8.443446,5.570499,-3.669221,3.975208,-2.915625,3.700655,8.543922,8.811947,-7.171965,-6.078264,2.361582,3.359703,4.053136,7.602743,-2.803339,7.876427,-8.113271,3.785034,-6.402169,1.722408,-3.746743,1.981306,-8.463387,-0.098504,-1.669768,-6.313823,-1.400408,1.542440,3.371435,4.936043,3.992727,-8.453628,8.144266,3.859304,-3.122677,-1.828504,5.440110,8.615832,6.794955,1.536019,-7.311716,9.754032,8.716011,-1.239333,5.455696,-5.115150,-1.571500,2.654722,5.682495,5.443159,7.143816,-1.066318,4.283238,-5.387178,5.072772,9.437611,2.935779,1.933587,7.295731,9.282131,1.662427,5.838653,5.084053,-7.730591,5.732639,-1.216571,7.527988,-6.307108,-3.086875,8.424583,-8.939684,5.265372,1.013200,-5.072437,-2.106457,-1.569512,-8.790304,-7.000864,-4.742579,-6.766300,-6.373196,-0.293897,5.184618,7.441898,-7.049236,4.152122,7.599555,-0.172674,4.570493,5.819334,5.966242,-7.480549,7.251551,2.750743,1.214428,-3.093270,-4.121368,3.507808,1.364901,-6.681268,-4.217232,-0.746058,-2.426310,-7.942531,5.049535,-9.344485,7.761293,-5.057132,5.656710,-4.368955,7.096415,-8.997845,-2.110361,5.508733,-4.311644,6.778472,-2.356011,-9.519660,-9.219578,-3.704023,-4.621655,-1.102479,9.625295,3.062042,-4.848541,8.303041,-5.191511,-8.796849,-3.169191,-3.555515,7.835193,8.820406,8.559711,-6.179240,-4.721720,4.705676,7.983201,0.769970,2.087766,1.516561,-5.826265,4.705991,7.007893,1.923244,-6.708001,-9.575809,4.470311,4.508657,-9.979951,5.253014,-8.667087,2.359315,-8.211574,3.865569,8.443754,-4.623180,1.811734,-7.502764,6.242272,-7.051031,3.869086,6.812613,-1.663157,7.279202,-4.494700,-8.869701,-8.741702,3.605087,-8.678707,-1.721594,7.213775,1.474260,-3.530288,5.375550,-1.114430,4.366120,3.213888,-8.233242,0.213684,-1.467680,-8.590879,6.956020,-5.770655,-8.583450,8.204067,1.602100,3.841969,6.146641,-9.490072,5.766058,1.017632,7.461240,9.198291,-5.478455,9.491644,-2.755911,7.039217,-3.983032,-6.377136,-9.108931,9.944998,7.500141,9.067136,3.632089,1.787179,-2.805670,9.094878,5.288936,5.453244,-7.915358,-3.703385,5.833196,-4.150846,-6.763475,-3.667179,-3.172287,-9.924530,-0.008296,-5.983085,7.300709,-6.525480,-7.664894,2.261705,-8.281218,-4.251580,-3.094640,7.010014,-2.802943,5.835430,0.531772,-8.658247,-7.271185,2.601899,-4.555044,-1.558249,4.277963,6.539396,-5.538209,-8.553407,9.613110,3.158942,5.813325,8.676078,-0.274431,-1.899252,-9.509869,9.557802,7.317761,7.293594,2.609929,-7.045004,-2.093433,-0.147175,-8.646614,4.748931,7.528304,9.573251,-0.154256,9.680585,-6.755817,-2.572016,-5.698062,3.910651,-9.587127,2.121333,-3.825940], dtype = "float32")#candidate|4603|(1350,)|const|float32
call_4602 = relay.TupleGetItem(func_4061_call(relay.reshape(const_4603.astype('float32'), [9, 15, 10])), 0)
call_4604 = relay.TupleGetItem(func_4063_call(relay.reshape(const_4603.astype('float32'), [9, 15, 10])), 0)
output = relay.Tuple([call_4585,call_4602,const_4603,])
output2 = relay.Tuple([call_4586,call_4604,const_4603,])
func_4617 = relay.Function([], output)
mod['func_4617'] = func_4617
mod = relay.transform.InferType()(mod)
mutated_mod['func_4617'] = func_4617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4617_call = mutated_mod.get_global_var('func_4617')
call_4618 = func_4617_call()
output = call_4618
func_4619 = relay.Function([], output)
mutated_mod['func_4619'] = func_4619
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3231_call = mod.get_global_var('func_3231')
func_3233_call = mutated_mod.get_global_var('func_3233')
call_4634 = relay.TupleGetItem(func_3231_call(), 1)
call_4635 = relay.TupleGetItem(func_3233_call(), 1)
uop_4652 = relay.acosh(call_4634.astype('float64')) # shape=(3, 1, 9)
uop_4654 = relay.acosh(call_4635.astype('float64')) # shape=(3, 1, 9)
uop_4662 = relay.sin(uop_4652.astype('float32')) # shape=(3, 1, 9)
uop_4664 = relay.sin(uop_4654.astype('float32')) # shape=(3, 1, 9)
output = relay.Tuple([uop_4662,])
output2 = relay.Tuple([uop_4664,])
func_4665 = relay.Function([], output)
mod['func_4665'] = func_4665
mod = relay.transform.InferType()(mod)
mutated_mod['func_4665'] = func_4665
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4665_call = mutated_mod.get_global_var('func_4665')
call_4666 = func_4665_call()
output = call_4666
func_4667 = relay.Function([], output)
mutated_mod['func_4667'] = func_4667
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2042_call = mod.get_global_var('func_2042')
func_2043_call = mutated_mod.get_global_var('func_2043')
call_4716 = relay.TupleGetItem(func_2042_call(), 0)
call_4717 = relay.TupleGetItem(func_2043_call(), 0)
var_4720 = relay.var("var_4720", dtype = "bool", shape = (3, 16, 9))#candidate|4720|(3, 16, 9)|var|bool
bop_4721 = relay.floor_divide(call_4716.astype('float32'), var_4720.astype('float32')) # shape=(3, 16, 9)
bop_4724 = relay.floor_divide(call_4717.astype('float32'), var_4720.astype('float32')) # shape=(3, 16, 9)
output = bop_4721
output2 = bop_4724
func_4725 = relay.Function([var_4720,], output)
mod['func_4725'] = func_4725
mod = relay.transform.InferType()(mod)
mutated_mod['func_4725'] = func_4725
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4726 = relay.var("var_4726", dtype = "bool", shape = (3, 16, 9))#candidate|4726|(3, 16, 9)|var|bool
func_4725_call = mutated_mod.get_global_var('func_4725')
call_4727 = func_4725_call(var_4726)
output = call_4727
func_4728 = relay.Function([var_4726], output)
mutated_mod['func_4728'] = func_4728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4471_call = mod.get_global_var('func_4471')
func_4472_call = mutated_mod.get_global_var('func_4472')
call_4738 = relay.TupleGetItem(func_4471_call(), 0)
call_4739 = relay.TupleGetItem(func_4472_call(), 0)
func_3258_call = mod.get_global_var('func_3258')
func_3260_call = mutated_mod.get_global_var('func_3260')
call_4754 = relay.TupleGetItem(func_3258_call(), 0)
call_4755 = relay.TupleGetItem(func_3260_call(), 0)
func_253_call = mod.get_global_var('func_253')
func_255_call = mutated_mod.get_global_var('func_255')
var_4758 = relay.var("var_4758", dtype = "uint32", shape = (576,))#candidate|4758|(576,)|var|uint32
call_4757 = func_253_call(relay.reshape(var_4758.astype('uint32'), [3, 16, 12]))
call_4759 = func_253_call(relay.reshape(var_4758.astype('uint32'), [3, 16, 12]))
output = relay.Tuple([call_4738,call_4754,call_4757,var_4758,])
output2 = relay.Tuple([call_4739,call_4755,call_4759,var_4758,])
func_4763 = relay.Function([var_4758,], output)
mod['func_4763'] = func_4763
mod = relay.transform.InferType()(mod)
var_4764 = relay.var("var_4764", dtype = "uint32", shape = (576,))#candidate|4764|(576,)|var|uint32
output = func_4763(var_4764)
func_4765 = relay.Function([var_4764], output)
mutated_mod['func_4765'] = func_4765
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4822 = relay.var("var_4822", dtype = "float32", shape = (16, 5, 8))#candidate|4822|(16, 5, 8)|var|float32
uop_4823 = relay.exp(var_4822.astype('float32')) # shape=(16, 5, 8)
uop_4827 = relay.acos(uop_4823.astype('float32')) # shape=(16, 5, 8)
var_4829 = relay.var("var_4829", dtype = "float32", shape = (16, 5, 8))#candidate|4829|(16, 5, 8)|var|float32
bop_4830 = relay.bitwise_and(uop_4827.astype('int8'), relay.reshape(var_4829.astype('int8'), relay.shape_of(uop_4827))) # shape=(16, 5, 8)
uop_4836 = relay.asin(uop_4827.astype('float64')) # shape=(16, 5, 8)
output = relay.Tuple([bop_4830,uop_4836,])
output2 = relay.Tuple([bop_4830,uop_4836,])
func_4843 = relay.Function([var_4822,var_4829,], output)
mod['func_4843'] = func_4843
mod = relay.transform.InferType()(mod)
mutated_mod['func_4843'] = func_4843
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4843_call = mutated_mod.get_global_var('func_4843')
var_4845 = relay.var("var_4845", dtype = "float32", shape = (16, 5, 8))#candidate|4845|(16, 5, 8)|var|float32
var_4846 = relay.var("var_4846", dtype = "float32", shape = (16, 5, 8))#candidate|4846|(16, 5, 8)|var|float32
call_4844 = func_4843_call(var_4845,var_4846,)
output = call_4844
func_4847 = relay.Function([var_4845,var_4846,], output)
mutated_mod['func_4847'] = func_4847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2386_call = mod.get_global_var('func_2386')
func_2388_call = mutated_mod.get_global_var('func_2388')
call_5018 = relay.TupleGetItem(func_2386_call(), 0)
call_5019 = relay.TupleGetItem(func_2388_call(), 0)
output = relay.Tuple([call_5018,])
output2 = relay.Tuple([call_5019,])
func_5042 = relay.Function([], output)
mod['func_5042'] = func_5042
mod = relay.transform.InferType()(mod)
mutated_mod['func_5042'] = func_5042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5042_call = mutated_mod.get_global_var('func_5042')
call_5043 = func_5042_call()
output = call_5043
func_5044 = relay.Function([], output)
mutated_mod['func_5044'] = func_5044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2042_call = mod.get_global_var('func_2042')
func_2043_call = mutated_mod.get_global_var('func_2043')
call_5099 = relay.TupleGetItem(func_2042_call(), 0)
call_5100 = relay.TupleGetItem(func_2043_call(), 0)
func_3655_call = mod.get_global_var('func_3655')
func_3659_call = mutated_mod.get_global_var('func_3659')
var_5120 = relay.var("var_5120", dtype = "int16", shape = (405,))#candidate|5120|(405,)|var|int16
const_5121 = relay.const([1,3,1,-9,7,-9,-1,-9,-3,10,-8,1,5,9,3,6,-3,-4,-7,9,-8,-6,-5,8,5,-9,2,3,10,-7,-6,-7,-2,-3,-5,-4,1,3,-4,-3,-10,-2,-4,2,-6,5,1,-3,4,-3,-8,-1,4,6,7,-7,-4,1,-5,-10,-3,-5,8,9,-3,2,-7,2,-6,-1,10,2,-10,-9,-10,-8,-3,-9,-8,-6,1,2,-10,-1,-5,-1,-4,-8,-8,1,-6,-2,9,-2,2,-10,4,10,8,-2,8,9,-8,4,2,5,4,8,3,-2,8,7,-2,7,2,5,3,-10,1,-9,1,2,3,9,-10,8,-1,-9,6,4,-5,6,5,1,1,-10,3,-6,-1,-10,-5,6,-7,-8,-1,9,-1,8,-10,-1,-8,-3,-2,7,3,-2,-10,-4,-3,8,-5,4,3,-4,-10,5,-8,10,7,-3,9,-1,-6,-3,-7,7,-9,10,2,6,10,3,-10,-8,-2,-9,8,9,-5,5,5,-4,2,8,-7,-7,6,3,-4,-2,3,9,-1,7,3,8,1,-4,-5,6,-7,-8,-4,-8,3,-5,1,-10,-2,-8,7,3,-9,1,-9,5,4,2,4,6,-2,-6,7,-5,10,-6,-1,-7,7,-4,8,6,-3,-10,8,6,1,3,7,8,3,-8,-4,7,-4,-10,2,-4,4,-4,2,-2,-4,-10,3,2,-6,4,-5,3,-4,2,1,-1,-2,7,8,8,4,-5,-9,-5,-7,-5,2,2,3,9,1,-10,6,-10,7,-6,-5,-10,-10,-9,7,-9,-2,-2,6,10,1,2,-9,4,10,9,-3,-2,-7,9,-3,-1,-1,3,-4,7,-2,5,-3,9,8,-1,-8,-3,-1,9,1,10,-2,-9,5,4,-7,1,5,-5,8,4,-6,1,7,3,1,-2,-6,1,-9,9,3,7,-9,-3,-8,-5,1,-4,-7,10,10,-2,5,6,-10,1,6,-1,2,-6,-10,7,-6,-2,7,2,6,-4,7,4,-6,1,4,-8,6,9,4,9,-10,-4,5,-4,10,-9,-7,-6,-9,-6,-1,-1,8,-4,7,-2,-4,-4,2,7,8,-1,-10,-10,4,-2,-2,-1,-5,3,-8,-9,-3,9,-2,7,4,-7,-3,-5,-4,-1,2,-7,8,-6,-6,7,7,5], dtype = "int16")#candidate|5121|(440,)|const|int16
var_5122 = relay.var("var_5122", dtype = "float32", shape = (450,))#candidate|5122|(450,)|var|float32
call_5119 = relay.TupleGetItem(func_3655_call(relay.reshape(var_5120.astype('int16'), [405,]), relay.reshape(const_5121.astype('int16'), [110, 4]), relay.reshape(var_5122.astype('float32'), [450,]), ), 4)
call_5123 = relay.TupleGetItem(func_3659_call(relay.reshape(var_5120.astype('int16'), [405,]), relay.reshape(const_5121.astype('int16'), [110, 4]), relay.reshape(var_5122.astype('float32'), [450,]), ), 4)
output = relay.Tuple([call_5099,call_5119,var_5120,const_5121,var_5122,])
output2 = relay.Tuple([call_5100,call_5123,var_5120,const_5121,var_5122,])
func_5126 = relay.Function([var_5120,var_5122,], output)
mod['func_5126'] = func_5126
mod = relay.transform.InferType()(mod)
mutated_mod['func_5126'] = func_5126
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5126_call = mutated_mod.get_global_var('func_5126')
var_5128 = relay.var("var_5128", dtype = "int16", shape = (405,))#candidate|5128|(405,)|var|int16
var_5129 = relay.var("var_5129", dtype = "float32", shape = (450,))#candidate|5129|(450,)|var|float32
call_5127 = func_5126_call(var_5128,var_5129,)
output = call_5127
func_5130 = relay.Function([var_5128,var_5129,], output)
mutated_mod['func_5130'] = func_5130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3231_call = mod.get_global_var('func_3231')
func_3233_call = mutated_mod.get_global_var('func_3233')
call_5138 = relay.TupleGetItem(func_3231_call(), 0)
call_5139 = relay.TupleGetItem(func_3233_call(), 0)
output = relay.Tuple([call_5138,])
output2 = relay.Tuple([call_5139,])
func_5142 = relay.Function([], output)
mod['func_5142'] = func_5142
mod = relay.transform.InferType()(mod)
mutated_mod['func_5142'] = func_5142
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5142_call = mutated_mod.get_global_var('func_5142')
call_5143 = func_5142_call()
output = call_5143
func_5144 = relay.Function([], output)
mutated_mod['func_5144'] = func_5144
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5216 = relay.const([[[-3.592872,9.171975,4.854221,1.375771,3.915468,-9.841997,5.939252,2.410858,8.733300,8.104112,6.929984,4.611501],[7.887615,0.109281,6.751550,-1.554489,-8.297936,5.978656,8.495009,-7.202804,-5.048740,-7.729330,-2.239213,9.292302],[-0.728428,-1.707316,-1.060716,-3.783598,2.265575,2.054981,-1.835599,-1.647636,4.298637,0.876064,5.415731,-6.088777],[-7.443111,7.742394,-1.611407,-3.816300,9.633939,6.111290,5.848296,7.615428,7.062742,4.347212,9.374484,-5.871075],[-7.446479,6.174776,-1.720837,6.000948,-2.954198,8.246875,8.768993,-7.666619,-1.005885,2.037649,5.933086,-3.890185],[5.779057,3.056317,-6.931227,-9.016353,3.323590,-1.250586,0.927167,-3.638039,-5.084296,-2.202519,1.611220,1.569368],[-5.077239,2.773993,4.934680,9.891357,-9.490731,9.046165,-3.357120,0.282107,-4.741260,4.125975,9.042823,9.430540],[-0.252660,1.959414,-2.131088,5.489025,7.981791,9.906726,3.244756,-7.146633,0.886005,-2.522794,1.742553,6.514253],[0.715591,0.600285,-1.867222,-4.167034,-6.659789,-0.174717,-6.095969,-5.686649,4.245775,4.840506,-8.389403,-7.991998],[1.158520,0.797940,-5.077846,-3.249533,-3.108919,-4.338984,5.513448,1.044390,-0.332882,-5.608727,1.631446,7.623577],[-1.544241,9.187436,-2.835847,-7.209945,-1.281082,-3.975957,-6.889857,-9.614059,-5.636820,1.128503,-8.450059,2.383244],[4.035178,5.845635,-4.066805,6.079225,1.476668,1.150951,-1.829879,-5.534650,-0.959924,5.449510,8.634143,5.482277]],[[-1.383284,3.815309,0.167742,7.308304,9.262540,3.566513,8.658952,-0.336718,-1.599715,-4.646983,-9.666663,3.871288],[4.253888,8.593921,0.552192,-8.295092,-6.458061,-8.553629,6.045662,-6.816788,-6.708950,-7.825619,-5.605568,0.408884],[6.333641,7.278847,-7.359291,-7.831187,2.874852,-4.136080,-3.223065,-6.761897,1.342735,-0.115189,-9.699606,6.033611],[-4.485978,9.480511,-6.295392,0.485319,-5.582642,5.934851,-5.549629,6.120741,-2.918822,-1.090617,-3.203842,2.927456],[5.619366,-2.123654,-6.252094,-8.043918,-6.698137,4.085370,-6.416589,-2.488867,4.721030,8.204078,5.855341,0.655889],[3.134790,-8.698340,-6.243591,9.400683,3.376838,7.273121,4.266244,-7.653313,4.158778,-5.560972,9.191967,2.212921],[8.723688,-3.866043,1.537946,-8.203719,4.186601,-0.811137,-5.706688,1.972904,-9.010909,8.261991,-9.634874,9.633935],[3.394138,-5.775308,-1.778050,5.926967,-1.705211,-7.743883,8.155854,-7.818575,2.061746,-9.406868,-7.524514,7.461613],[-5.401315,-8.415693,-1.648311,2.491561,-8.390237,-7.789627,3.089740,-3.820128,4.053778,4.582368,2.911075,7.797741],[-9.822413,-0.988021,7.316088,0.817989,-0.496828,3.763059,5.222629,-8.856915,-8.767208,-0.030102,-2.748336,9.765790],[9.666022,-1.615551,7.900008,6.609917,0.102285,-8.115901,0.899331,-2.124294,-6.153670,3.681299,-2.173857,3.281725],[-6.753499,-1.248434,-1.653998,6.219315,-8.931316,-5.262264,0.411359,-8.830829,8.945227,-7.551867,-0.740103,-2.846842]],[[-9.146382,1.323662,8.842865,9.328553,-7.977291,-9.641204,0.929925,0.097746,3.220319,5.683737,0.697893,6.087530],[4.312817,-2.350114,-6.130307,-0.254418,-2.602149,-6.421401,-3.985684,7.494236,2.647545,5.718311,6.369882,9.844978],[-2.114953,-2.439407,-8.666904,-4.418186,6.194054,7.507670,9.036833,-4.971911,4.622947,7.646304,-2.130749,7.257372],[-8.816473,-3.651593,5.416453,-4.002172,5.775122,9.662498,-6.075283,4.387476,-5.303080,7.012316,-5.551319,2.354744],[-4.998174,2.892265,-9.942900,1.817667,6.537151,-9.389505,7.828493,-5.313649,1.669064,-2.955328,1.318289,3.554119],[-8.791212,5.420415,-0.925996,7.380986,7.082344,9.630799,0.343073,-2.193007,0.212618,7.538727,5.430240,1.303020],[9.015001,-1.851610,9.661110,5.389736,-7.818656,-5.897275,9.313883,-7.384115,-1.195257,-6.518466,-7.477941,-1.746151],[-3.464599,-2.087538,1.444785,-2.136001,9.742593,1.466094,6.809205,-8.155899,5.860591,-4.560089,-3.479015,0.601046],[8.377767,-3.470012,-7.800131,1.777991,-2.443112,-2.722239,0.930737,7.325893,5.236943,1.482900,3.699875,-7.309614],[-7.512542,8.072030,5.105500,3.160785,7.903433,-6.011837,-3.021023,-4.410605,8.431195,-6.899698,0.892707,1.912073],[-0.098088,2.902289,7.404998,-0.165123,9.574341,-4.430460,-7.244269,4.352679,-2.632158,2.807114,9.322329,7.502268],[-6.098591,6.816802,2.013599,-9.534496,8.791986,6.022052,8.819223,-5.870643,-2.821446,-7.469633,-0.798928,-4.941031]],[[4.759004,3.764869,0.489834,-2.492709,-9.206336,7.723897,-0.189795,8.595369,-8.298095,-3.504044,-6.631453,-9.480983],[-1.706907,4.436269,-7.137648,9.387140,9.786107,-7.772131,6.734124,-2.972883,-8.132999,-2.785799,1.544927,-8.391835],[-5.768282,2.797078,7.369493,8.890900,-4.248117,-2.917542,-3.080428,2.194060,-9.845247,-3.837458,-0.238905,8.831597],[8.793520,1.461304,5.949901,-5.018201,0.740916,-2.603864,7.129310,-1.116088,-7.677544,-0.065785,-4.000062,-1.672460],[4.977168,-0.493766,3.818604,-0.229178,7.603487,1.678014,2.914743,6.913209,0.884236,5.307553,9.420735,6.818645],[-8.352080,7.098494,4.711688,6.199507,-0.494897,-2.336714,5.061654,-2.604253,-0.562877,1.357007,7.730137,-5.997690],[-5.487687,8.568137,7.410338,0.377565,-4.556279,-6.892439,-5.686381,-8.824157,-8.005066,-4.660337,8.163180,-8.557260],[-2.486823,1.063915,-5.137512,-9.858004,1.656612,5.201128,-2.785519,-0.355819,8.125422,-7.479677,-7.654682,-3.217955],[3.413084,-7.900839,-0.254431,2.638626,-0.867572,-4.891976,-4.911266,8.265962,9.651611,5.811236,7.502885,-1.616139],[-0.816021,-7.833885,-5.688450,2.644533,7.357544,-0.048911,1.253174,-8.506925,5.959603,-8.428142,-6.353062,5.337033],[-8.833150,3.874219,4.629316,-0.193864,1.369858,-2.792015,-5.470597,4.433100,-2.083047,6.662823,7.375322,2.595746],[-4.924940,1.498108,-4.726054,-6.368545,4.215917,-3.362101,-3.909287,-1.554112,-9.480956,1.147879,9.386832,-3.122659]],[[-2.879747,4.092665,-2.554180,-1.587698,-7.652221,8.875531,7.147597,-3.763083,4.484615,9.103756,3.403777,7.049365],[-8.123617,-3.715957,-7.266261,6.698335,-1.983808,-1.170202,-9.357804,-7.888588,-5.466629,7.386643,2.943827,-3.049771],[-8.836782,-8.044249,-8.538279,9.349784,-2.399427,-3.632774,4.969518,-7.824556,-5.892205,-3.686284,8.010647,2.836138],[-9.992196,1.924810,-8.852139,-0.402779,9.548012,9.973141,2.213733,5.206279,-0.360610,-7.075528,4.589041,-3.963098],[9.273806,-1.206568,6.023635,3.437314,-1.609584,4.388404,-9.928224,-2.598979,4.925083,6.473726,-1.128781,-4.218683],[-0.927937,-0.109874,2.931334,4.206857,1.367858,-8.747878,-4.983402,-2.564847,-1.381368,1.125992,-7.132036,1.107266],[9.918093,-8.979124,6.762856,1.147769,6.206420,3.985641,-2.119896,1.592219,3.281997,-1.383396,1.989139,-0.181225],[-2.623191,5.139470,7.761392,-1.470375,1.201088,7.726156,-6.403077,6.705311,-6.218909,-5.699634,9.113751,3.655597],[1.792673,-7.030203,-7.371434,5.150769,0.370713,3.876491,4.391502,0.849796,-7.741539,8.278108,6.368959,-1.773425],[5.953370,-6.654414,2.241729,6.762921,8.518761,1.556252,8.185903,9.879822,7.095052,0.426400,-7.893631,-7.561806],[3.669295,0.392522,-0.649518,9.329060,8.512650,-2.665991,9.904808,6.754697,-3.299864,-0.539145,3.864279,-9.047219],[4.903826,9.265206,-6.078402,-6.524522,2.498010,9.754984,-4.898285,-9.858076,-9.430036,-8.449996,-0.242912,7.686884]],[[-9.599781,-1.433311,2.854112,8.958674,3.580444,-0.881220,-5.544709,5.300355,9.584464,9.398520,6.382704,3.300049],[-2.334138,0.062019,2.864611,0.810516,0.082720,-0.581306,-3.607509,4.505025,-4.204743,-6.501943,-7.270106,0.360863],[-2.596337,2.776474,-8.142271,7.813793,-7.447450,3.232520,6.925213,-6.273014,7.596862,3.246726,-3.565846,0.829531],[9.753714,2.470956,4.911375,3.204870,2.766237,-5.486751,5.062011,-7.148770,-7.129707,6.531646,2.411182,-9.395897],[-6.940941,-8.911180,-9.119958,-4.366657,9.065819,-3.801540,-1.780682,-6.341130,-5.398507,7.233543,1.536287,-8.209209],[7.770248,2.005807,0.636748,4.271028,-3.481457,-2.597930,6.869395,-6.541913,-0.969886,-9.468786,-4.778871,-3.141727],[9.216737,-1.599926,4.518711,-1.255457,-2.500193,1.164210,-2.309907,-7.218239,0.312103,7.384027,0.266912,9.483454],[-8.393306,-5.392178,9.549173,-1.993608,-1.943803,0.774198,8.636103,-6.191785,7.656459,1.500075,6.792481,-4.689492],[-2.353168,6.430003,8.305796,4.111397,-7.861607,-4.918548,-2.417721,-3.126092,7.231800,-6.154431,-8.146492,5.026039],[6.319234,4.393144,-0.898712,6.449366,7.892206,-7.668984,1.386461,1.107799,4.495262,6.549143,-1.108661,-8.415532],[7.680127,-2.978474,2.367927,-8.716499,-4.766235,0.838028,2.365435,6.740689,-0.598502,-2.540797,4.720578,0.411120],[5.513217,-6.503027,2.407654,-8.658990,2.092165,-7.777794,-5.256243,5.172146,-1.474213,7.716134,9.586105,-0.880904]],[[-4.996185,-9.512351,-6.144282,-9.494561,-4.751067,0.578274,0.717210,3.437409,-0.134502,0.744872,-4.976078,9.028631],[-0.727665,-7.169877,6.938655,7.741538,1.118998,6.780504,3.654377,-6.008011,-4.709761,4.461669,3.243516,2.311982],[-8.366327,-0.528198,7.013426,2.501546,-5.117573,-6.507768,4.425399,8.402088,0.502972,-5.677422,-8.390990,-2.950375],[6.986392,-8.973459,-6.601649,-1.673275,-5.108084,1.468987,8.357704,1.852004,4.575650,2.076155,2.689993,3.442993],[-1.804680,-6.616613,-4.176028,5.486169,-0.351993,-8.465578,9.749385,-6.546536,9.839618,-7.866103,-3.654646,-5.801182],[5.031503,-6.984806,-1.495165,6.993018,-3.661741,0.804979,-8.610382,-4.365276,-8.131296,-1.832918,5.642524,-5.237237],[-7.852818,6.583210,-1.971630,-8.462006,-4.121180,4.670585,6.756499,4.457780,-6.675539,-6.235539,8.550607,7.704192],[-7.176325,-3.619280,-3.247641,-8.822757,8.912901,-1.653381,-4.328413,8.980758,3.180370,8.217995,6.703130,-2.860825],[-0.775458,-5.155883,4.974644,3.565323,3.633518,-2.471135,-5.258859,9.539197,-6.092621,-9.452058,-9.899843,6.892073],[-3.885880,-4.309701,4.251485,5.770848,-8.406097,-4.960737,3.610978,3.757836,4.476542,7.862496,-7.714546,6.227976],[-3.730014,0.317722,1.286355,-2.804341,-6.361297,1.809145,-2.545675,9.963169,-6.503446,-1.177239,5.603311,6.051722],[2.038489,2.691482,9.902163,0.689455,-6.509374,-3.948482,8.552897,6.585022,-9.515877,-5.029345,3.957371,3.537629]],[[1.046151,6.450918,1.657947,1.730845,9.265275,-3.716622,0.049698,-6.204972,9.682548,2.777638,-7.655415,-8.850483],[7.947778,3.902180,-2.013665,-4.737743,-3.243338,-6.100706,-7.199975,2.573731,-8.476346,-8.016924,7.954867,7.444546],[-8.231047,1.665693,2.665441,2.339482,-7.845423,0.054778,0.092354,-8.286625,-6.143105,2.883214,-4.749737,-9.889739],[-4.889137,-8.955720,-8.761375,-2.420898,-3.460023,6.681989,7.204860,-5.600997,3.180199,-0.689137,-1.696949,-3.580030],[-6.533324,9.782131,-1.560913,6.169425,4.578378,-7.450320,-5.368219,-4.036629,5.363743,-3.489221,-3.823716,-2.011460],[4.527940,-2.797930,-5.650798,-2.164937,-8.241000,3.838675,7.373086,9.087860,3.562934,-2.255114,2.454310,-8.391721],[-1.586174,6.245062,-5.644015,-5.371710,8.885072,4.104598,-7.616920,-5.838367,9.768160,6.506942,-1.009494,5.971023],[0.552591,2.578878,-1.789570,7.652455,3.567671,4.643421,-1.246648,5.090741,-0.160899,4.149197,-1.586882,9.674937],[-5.008115,-5.105468,-9.707607,-5.396326,-3.479184,-2.179374,7.776023,4.788669,-7.981408,-7.185578,6.239948,-0.155609],[-7.720565,-1.286772,7.353070,0.747089,-6.442123,6.079242,3.733722,-1.753379,7.592871,5.458242,-5.530665,3.698422],[3.315482,-3.390143,4.794716,6.290147,-8.462659,-7.710070,0.992025,6.882299,-4.559761,-0.004326,-8.966409,9.839953],[5.914039,2.147936,5.634924,7.873352,-5.789489,8.580365,-2.490446,-7.606626,-6.253266,6.975066,-1.423165,-9.756034]],[[8.716785,-4.249300,9.641997,3.651837,-7.643648,1.423182,-6.801882,2.361474,-7.105181,-2.545034,7.777001,4.550268],[-1.388377,8.435358,-0.952388,4.051003,2.846340,5.325800,2.186025,1.360518,0.803292,2.967376,3.938509,0.696548],[-8.284851,5.133234,-0.485466,5.543404,8.036800,2.902261,-3.632711,7.719684,-7.476294,9.985033,6.525361,-6.934691],[5.719355,-5.175792,-2.433261,-7.473162,-7.223703,-1.087680,-6.903184,4.475776,-6.183428,5.460680,9.736354,-9.736796],[-3.131168,6.194675,0.419751,-0.169265,6.855028,2.969164,-6.553739,-9.950581,1.223627,4.101438,9.245131,3.190567],[0.469502,-2.488857,3.778537,9.418054,-7.810604,-8.555998,-5.956464,-5.271132,6.693237,9.444233,7.999142,-6.075536],[-4.735426,1.030053,-7.022744,6.975281,5.302634,-3.639667,3.286443,-4.856459,-5.931518,2.601570,-8.337535,9.032451],[3.671766,8.324390,-3.155875,-7.587395,-1.616842,-9.066692,-0.654641,-8.956254,-0.798686,2.969182,-7.609681,5.292323],[-5.954506,9.114368,7.074682,-3.032548,3.742112,3.511534,-7.701697,-9.013151,4.541086,7.132194,9.637116,-2.174473],[6.180953,9.601100,4.984204,-7.354839,8.357498,-8.771574,-2.487359,6.143603,1.629680,-6.763015,-2.861273,-6.677216],[5.566259,-3.680962,9.218372,-3.275801,-4.927727,1.053245,1.360975,1.217662,7.197749,0.097138,-6.692152,-7.898312],[2.438735,3.606323,6.533214,-3.807479,-4.667447,0.205336,7.238582,-8.229451,7.967354,7.369181,4.287776,9.766134]]], dtype = "float32")#candidate|5216|(9, 12, 12)|const|float32
uop_5217 = relay.cos(const_5216.astype('float32')) # shape=(9, 12, 12)
bop_5219 = relay.maximum(const_5216.astype('float32'), relay.reshape(uop_5217.astype('float32'), relay.shape_of(const_5216))) # shape=(9, 12, 12)
bop_5227 = relay.bitwise_xor(bop_5219.astype('uint64'), relay.reshape(uop_5217.astype('uint64'), relay.shape_of(bop_5219))) # shape=(9, 12, 12)
uop_5236 = relay.sigmoid(uop_5217.astype('float64')) # shape=(9, 12, 12)
func_804_call = mod.get_global_var('func_804')
func_808_call = mutated_mod.get_global_var('func_808')
var_5242 = relay.var("var_5242", dtype = "float32", shape = (24, 8))#candidate|5242|(24, 8)|var|float32
call_5241 = relay.TupleGetItem(func_804_call(relay.reshape(var_5242.astype('float32'), [6, 2, 16]), relay.reshape(var_5242.astype('float32'), [6, 2, 16]), ), 1)
call_5243 = relay.TupleGetItem(func_808_call(relay.reshape(var_5242.astype('float32'), [6, 2, 16]), relay.reshape(var_5242.astype('float32'), [6, 2, 16]), ), 1)
output = relay.Tuple([bop_5227,uop_5236,call_5241,var_5242,])
output2 = relay.Tuple([bop_5227,uop_5236,call_5243,var_5242,])
func_5244 = relay.Function([var_5242,], output)
mod['func_5244'] = func_5244
mod = relay.transform.InferType()(mod)
var_5245 = relay.var("var_5245", dtype = "float32", shape = (24, 8))#candidate|5245|(24, 8)|var|float32
output = func_5244(var_5245)
func_5246 = relay.Function([var_5245], output)
mutated_mod['func_5246'] = func_5246
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5251 = relay.var("var_5251", dtype = "float32", shape = (13, 2, 7))#candidate|5251|(13, 2, 7)|var|float32
uop_5252 = relay.log(var_5251.astype('float32')) # shape=(13, 2, 7)
bop_5260 = relay.less(uop_5252.astype('bool'), relay.reshape(var_5251.astype('bool'), relay.shape_of(uop_5252))) # shape=(13, 2, 7)
output = relay.Tuple([bop_5260,])
output2 = relay.Tuple([bop_5260,])
func_5268 = relay.Function([var_5251,], output)
mod['func_5268'] = func_5268
mod = relay.transform.InferType()(mod)
var_5269 = relay.var("var_5269", dtype = "float32", shape = (13, 2, 7))#candidate|5269|(13, 2, 7)|var|float32
output = func_5268(var_5269)
func_5270 = relay.Function([var_5269], output)
mutated_mod['func_5270'] = func_5270
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5142_call = mod.get_global_var('func_5142')
func_5144_call = mutated_mod.get_global_var('func_5144')
call_5279 = relay.TupleGetItem(func_5142_call(), 0)
call_5280 = relay.TupleGetItem(func_5144_call(), 0)
var_5287 = relay.var("var_5287", dtype = "bool", shape = (3, 2, 9))#candidate|5287|(3, 2, 9)|var|bool
bop_5288 = relay.subtract(call_5279.astype('uint32'), var_5287.astype('uint32')) # shape=(3, 2, 9)
bop_5291 = relay.subtract(call_5280.astype('uint32'), var_5287.astype('uint32')) # shape=(3, 2, 9)
func_3091_call = mod.get_global_var('func_3091')
func_3093_call = mutated_mod.get_global_var('func_3093')
call_5295 = relay.TupleGetItem(func_3091_call(), 0)
call_5296 = relay.TupleGetItem(func_3093_call(), 0)
func_1249_call = mod.get_global_var('func_1249')
func_1251_call = mutated_mod.get_global_var('func_1251')
call_5299 = relay.TupleGetItem(func_1249_call(), 0)
call_5300 = relay.TupleGetItem(func_1251_call(), 0)
output = relay.Tuple([bop_5288,call_5295,call_5299,])
output2 = relay.Tuple([bop_5291,call_5296,call_5300,])
func_5301 = relay.Function([var_5287,], output)
mod['func_5301'] = func_5301
mod = relay.transform.InferType()(mod)
mutated_mod['func_5301'] = func_5301
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5302 = relay.var("var_5302", dtype = "bool", shape = (3, 2, 9))#candidate|5302|(3, 2, 9)|var|bool
func_5301_call = mutated_mod.get_global_var('func_5301')
call_5303 = func_5301_call(var_5302)
output = call_5303
func_5304 = relay.Function([var_5302], output)
mutated_mod['func_5304'] = func_5304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1677_call = mod.get_global_var('func_1677')
func_1678_call = mutated_mod.get_global_var('func_1678')
call_5306 = func_1677_call()
call_5307 = func_1677_call()
uop_5318 = relay.sqrt(call_5306.astype('float64')) # shape=(3, 1, 9)
uop_5320 = relay.sqrt(call_5307.astype('float64')) # shape=(3, 1, 9)
func_5244_call = mod.get_global_var('func_5244')
func_5246_call = mutated_mod.get_global_var('func_5246')
const_5336 = relay.const([-3.119017,6.401512,-9.064632,-3.190818,7.473661,2.861783,-7.792522,3.468884,-9.947101,-6.700577,-0.519949,2.001966,-0.546825,8.057890,1.348669,5.442085,2.114061,8.271022,-2.783078,1.270788,8.260802,7.997298,-4.305916,-4.686318,-0.692761,-8.981641,-7.568627,-0.881386,7.651427,-6.053792,-0.959688,-2.468767,9.787768,8.402753,6.287689,6.002686,9.144752,-7.538317,8.429285,-1.861836,3.831784,-8.864677,3.852007,-3.565665,-6.225245,2.904444,-1.986845,4.082685,3.430058,-2.850751,7.247184,6.294915,-5.412188,-8.147517,3.149513,-6.079959,7.903314,-2.196364,5.999417,7.690209,-2.849373,-5.460236,-3.479432,-1.555549,-1.787746,-3.915216,-2.969750,-8.399629,2.327506,0.425138,1.115531,9.973564,-0.475476,5.017141,-9.583507,-1.633080,8.501511,-6.940139,-7.138750,-4.810761,2.547227,-8.224982,-1.302354,-2.441193,0.854492,-3.488145,6.537547,-6.562169,-5.131968,0.848026,-7.403395,6.745593,-4.237214,-8.736932,-9.686417,1.111122,5.635268,2.906271,-5.084189,-2.372786,8.961596,4.819477,-6.595126,6.539623,1.002887,-2.254029,-7.750876,-9.219285,0.444832,4.875993,7.484451,9.551948,-4.394213,-2.982854,-3.317436,-3.256346,-4.476056,7.597833,1.580599,4.390706,3.202927,9.791196,6.390168,8.865073,-6.319385,-6.934532,0.051104,-6.387814,-0.506206,4.079351,8.970612,7.516163,1.269303,5.662134,8.990341,0.385601,-9.827740,-8.600596,-9.630512,-8.148730,-3.861030,-4.470229,-6.142389,4.957870,-6.894828,4.527877,-5.176125,5.815389,8.147753,7.949262,8.954562,-8.154153,1.736598,2.226189,-6.254792,-1.018249,-4.558231,-3.261740,0.832338,0.107451,-0.908413,-8.532945,0.296922,-6.645057,-4.225569,4.195062,9.444871,0.041594,-7.066618,-7.071784,-1.292354,5.123935,-9.451535,2.525754,5.300003,0.901663,3.653685,9.501162,7.983273,-2.486525,9.462095,3.250134,6.921412,8.933941,1.685498,-1.834182,-6.101892,-0.602763,2.956534,-6.746256,-5.113930,6.148608], dtype = "float32")#candidate|5336|(192,)|const|float32
call_5335 = relay.TupleGetItem(func_5244_call(relay.reshape(const_5336.astype('float32'), [24, 8])), 1)
call_5337 = relay.TupleGetItem(func_5246_call(relay.reshape(const_5336.astype('float32'), [24, 8])), 1)
output = relay.Tuple([uop_5318,call_5335,const_5336,])
output2 = relay.Tuple([uop_5320,call_5337,const_5336,])
func_5340 = relay.Function([], output)
mod['func_5340'] = func_5340
mod = relay.transform.InferType()(mod)
mutated_mod['func_5340'] = func_5340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5340_call = mutated_mod.get_global_var('func_5340')
call_5341 = func_5340_call()
output = call_5341
func_5342 = relay.Function([], output)
mutated_mod['func_5342'] = func_5342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4665_call = mod.get_global_var('func_4665')
func_4667_call = mutated_mod.get_global_var('func_4667')
call_5369 = relay.TupleGetItem(func_4665_call(), 0)
call_5370 = relay.TupleGetItem(func_4667_call(), 0)
var_5379 = relay.var("var_5379", dtype = "float32", shape = (3, 13, 9))#candidate|5379|(3, 13, 9)|var|float32
bop_5380 = relay.less_equal(call_5369.astype('bool'), var_5379.astype('bool')) # shape=(3, 13, 9)
bop_5383 = relay.less_equal(call_5370.astype('bool'), var_5379.astype('bool')) # shape=(3, 13, 9)
uop_5391 = relay.sigmoid(call_5369.astype('float32')) # shape=(3, 1, 9)
uop_5393 = relay.sigmoid(call_5370.astype('float32')) # shape=(3, 1, 9)
func_1107_call = mod.get_global_var('func_1107')
func_1108_call = mutated_mod.get_global_var('func_1108')
call_5410 = relay.TupleGetItem(func_1107_call(), 0)
call_5411 = relay.TupleGetItem(func_1108_call(), 0)
output = relay.Tuple([bop_5380,uop_5391,call_5410,])
output2 = relay.Tuple([bop_5383,uop_5393,call_5411,])
func_5413 = relay.Function([var_5379,], output)
mod['func_5413'] = func_5413
mod = relay.transform.InferType()(mod)
mutated_mod['func_5413'] = func_5413
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5414 = relay.var("var_5414", dtype = "float32", shape = (3, 13, 9))#candidate|5414|(3, 13, 9)|var|float32
func_5413_call = mutated_mod.get_global_var('func_5413')
call_5415 = func_5413_call(var_5414)
output = call_5415
func_5416 = relay.Function([var_5414], output)
mutated_mod['func_5416'] = func_5416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3036_call = mod.get_global_var('func_3036')
func_3037_call = mutated_mod.get_global_var('func_3037')
call_5487 = func_3036_call()
call_5488 = func_3036_call()
output = relay.Tuple([call_5487,])
output2 = relay.Tuple([call_5488,])
func_5493 = relay.Function([], output)
mod['func_5493'] = func_5493
mod = relay.transform.InferType()(mod)
output = func_5493()
func_5494 = relay.Function([], output)
mutated_mod['func_5494'] = func_5494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5493_call = mod.get_global_var('func_5493')
func_5494_call = mutated_mod.get_global_var('func_5494')
call_5500 = relay.TupleGetItem(func_5493_call(), 0)
call_5501 = relay.TupleGetItem(func_5494_call(), 0)
output = relay.Tuple([call_5500,])
output2 = relay.Tuple([call_5501,])
func_5504 = relay.Function([], output)
mod['func_5504'] = func_5504
mod = relay.transform.InferType()(mod)
mutated_mod['func_5504'] = func_5504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5504_call = mutated_mod.get_global_var('func_5504')
call_5505 = func_5504_call()
output = call_5505
func_5506 = relay.Function([], output)
mutated_mod['func_5506'] = func_5506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2995_call = mod.get_global_var('func_2995')
func_2997_call = mutated_mod.get_global_var('func_2997')
call_5540 = relay.TupleGetItem(func_2995_call(), 0)
call_5541 = relay.TupleGetItem(func_2997_call(), 0)
output = call_5540
output2 = call_5541
func_5542 = relay.Function([], output)
mod['func_5542'] = func_5542
mod = relay.transform.InferType()(mod)
output = func_5542()
func_5543 = relay.Function([], output)
mutated_mod['func_5543'] = func_5543
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5552 = relay.const(-5.487994, dtype = "float64")#candidate|5552|()|const|float64
var_5553 = relay.var("var_5553", dtype = "float64", shape = (16, 3, 5))#candidate|5553|(16, 3, 5)|var|float64
bop_5554 = relay.floor_divide(const_5552.astype('float64'), var_5553.astype('float64')) # shape=(16, 3, 5)
output = relay.Tuple([bop_5554,])
output2 = relay.Tuple([bop_5554,])
func_5568 = relay.Function([var_5553,], output)
mod['func_5568'] = func_5568
mod = relay.transform.InferType()(mod)
var_5569 = relay.var("var_5569", dtype = "float64", shape = (16, 3, 5))#candidate|5569|(16, 3, 5)|var|float64
output = func_5568(var_5569)
func_5570 = relay.Function([var_5569], output)
mutated_mod['func_5570'] = func_5570
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2668_call = mod.get_global_var('func_2668')
func_2670_call = mutated_mod.get_global_var('func_2670')
call_5582 = relay.TupleGetItem(func_2668_call(), 2)
call_5583 = relay.TupleGetItem(func_2670_call(), 2)
uop_5584 = relay.cosh(call_5582.astype('float64')) # shape=(3, 16, 12)
uop_5586 = relay.cosh(call_5583.astype('float64')) # shape=(3, 16, 12)
var_5595 = relay.var("var_5595", dtype = "float64", shape = (3, 16, 12))#candidate|5595|(3, 16, 12)|var|float64
bop_5596 = relay.bitwise_and(uop_5584.astype('uint32'), relay.reshape(var_5595.astype('uint32'), relay.shape_of(uop_5584))) # shape=(3, 16, 12)
bop_5599 = relay.bitwise_and(uop_5586.astype('uint32'), relay.reshape(var_5595.astype('uint32'), relay.shape_of(uop_5586))) # shape=(3, 16, 12)
uop_5608 = relay.tan(bop_5596.astype('float64')) # shape=(3, 16, 12)
uop_5610 = relay.tan(bop_5599.astype('float64')) # shape=(3, 16, 12)
func_1310_call = mod.get_global_var('func_1310')
func_1313_call = mutated_mod.get_global_var('func_1313')
var_5624 = relay.var("var_5624", dtype = "float32", shape = (144,))#candidate|5624|(144,)|var|float32
var_5625 = relay.var("var_5625", dtype = "float32", shape = (450,))#candidate|5625|(450,)|var|float32
call_5623 = relay.TupleGetItem(func_1310_call(relay.reshape(var_5624.astype('float32'), [16, 1, 9]), relay.reshape(var_5625.astype('float32'), [450,]), ), 1)
call_5626 = relay.TupleGetItem(func_1313_call(relay.reshape(var_5624.astype('float32'), [16, 1, 9]), relay.reshape(var_5625.astype('float32'), [450,]), ), 1)
uop_5628 = relay.log10(bop_5596.astype('float32')) # shape=(3, 16, 12)
uop_5630 = relay.log10(bop_5599.astype('float32')) # shape=(3, 16, 12)
uop_5637 = relay.log2(uop_5608.astype('float64')) # shape=(3, 16, 12)
uop_5639 = relay.log2(uop_5610.astype('float64')) # shape=(3, 16, 12)
func_5493_call = mod.get_global_var('func_5493')
func_5494_call = mutated_mod.get_global_var('func_5494')
call_5649 = relay.TupleGetItem(func_5493_call(), 0)
call_5650 = relay.TupleGetItem(func_5494_call(), 0)
output = relay.Tuple([call_5623,var_5624,var_5625,uop_5628,uop_5637,call_5649,])
output2 = relay.Tuple([call_5626,var_5624,var_5625,uop_5630,uop_5639,call_5650,])
func_5671 = relay.Function([var_5595,var_5624,var_5625,], output)
mod['func_5671'] = func_5671
mod = relay.transform.InferType()(mod)
var_5672 = relay.var("var_5672", dtype = "float64", shape = (3, 16, 12))#candidate|5672|(3, 16, 12)|var|float64
var_5673 = relay.var("var_5673", dtype = "float32", shape = (144,))#candidate|5673|(144,)|var|float32
var_5674 = relay.var("var_5674", dtype = "float32", shape = (450,))#candidate|5674|(450,)|var|float32
output = func_5671(var_5672,var_5673,var_5674,)
func_5675 = relay.Function([var_5672,var_5673,var_5674,], output)
mutated_mod['func_5675'] = func_5675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3091_call = mod.get_global_var('func_3091')
func_3093_call = mutated_mod.get_global_var('func_3093')
call_5745 = relay.TupleGetItem(func_3091_call(), 0)
call_5746 = relay.TupleGetItem(func_3093_call(), 0)
output = call_5745
output2 = call_5746
func_5753 = relay.Function([], output)
mod['func_5753'] = func_5753
mod = relay.transform.InferType()(mod)
output = func_5753()
func_5754 = relay.Function([], output)
mutated_mod['func_5754'] = func_5754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2042_call = mod.get_global_var('func_2042')
func_2043_call = mutated_mod.get_global_var('func_2043')
call_5785 = relay.TupleGetItem(func_2042_call(), 0)
call_5786 = relay.TupleGetItem(func_2043_call(), 0)
func_4047_call = mod.get_global_var('func_4047')
func_4048_call = mutated_mod.get_global_var('func_4048')
call_5790 = relay.TupleGetItem(func_4047_call(), 0)
call_5791 = relay.TupleGetItem(func_4048_call(), 0)
uop_5796 = relay.tan(call_5785.astype('float64')) # shape=(3, 1, 9)
uop_5798 = relay.tan(call_5786.astype('float64')) # shape=(3, 1, 9)
func_3503_call = mod.get_global_var('func_3503')
func_3508_call = mutated_mod.get_global_var('func_3508')
const_5802 = relay.const([[-2.938270,-6.863747,-1.245855,-2.633006,3.096387,9.374681,-8.778212,3.722513,-5.826660,0.397894,2.724253,-7.457976,-2.995351,7.157495,-2.547024,-7.382310,5.968686,5.218863,5.021346,6.029193,-7.653744,-6.378428,9.694351,-8.593012,-4.832210,-7.207076,1.054738,-3.331212,-3.037382,-8.003075,3.171487,0.009597,4.484397,5.236463,7.572107,-7.281403,6.773929,-5.586030,-2.233315,9.133125,-5.600100,-5.935378,-4.128157,6.097936,-4.196845,4.500452,-8.631585,-6.912749,6.365162,-7.701191,5.416148,3.623210,9.324769,2.997784,-5.945353,-3.080787,-7.251226,-0.624119,2.078105,8.030306,5.673834,-9.229150,1.205396,-1.356582,-3.294696,3.620626,3.214596,-0.216099,-2.248885,-5.169204,-7.538241,-1.564000,0.008040,9.126313,-1.197190,7.127558,8.774114,-2.387251,-3.469120,-2.242807,7.186494,-8.168736,-7.243691,-1.079163,-9.028918,5.444250,8.103400,0.157659],[7.373532,-2.989886,6.808583,8.188237,4.715054,-7.520392,-6.287969,-6.384028,-7.206135,-6.993511,3.532752,-9.970574,1.087971,0.703708,5.689168,-8.722179,0.071045,-9.446551,-4.506455,-7.279728,9.839999,4.645070,0.770267,-8.791760,2.372285,-3.580515,4.119233,-6.242759,-1.978505,3.113888,4.658072,-2.490587,-7.949768,9.355612,5.369612,-7.371061,-2.676572,-3.835637,7.348383,-6.891359,-7.702064,-7.839507,0.680501,-7.841641,-8.504170,3.992911,9.599274,-3.797601,-3.115028,-6.159967,6.592140,4.651961,6.452100,0.007820,-5.887282,8.039802,-1.688422,-7.603447,-8.301317,-6.253546,-2.808726,-9.182358,2.135775,-4.670936,6.160060,1.768566,1.287529,-1.243089,6.867223,-5.468989,9.789560,-1.085592,4.189155,9.814161,6.062226,-4.002872,9.263345,-9.276253,0.432657,6.141507,3.804880,-2.874449,8.423071,0.641281,-9.222615,-0.235979,8.761472,-5.812533],[2.681020,9.308900,0.985763,-1.551933,-4.166301,7.365802,3.080170,-6.529350,-8.368171,-5.311054,-1.814199,-6.128702,5.416219,-8.707529,9.176519,1.596133,9.370486,0.268682,-7.216158,2.849058,-8.875131,-5.021107,4.307998,0.017499,4.922156,0.966880,4.725815,3.108433,-9.249262,-8.748196,-2.947030,-1.909229,-5.950138,-9.332525,-5.435652,4.098613,-6.692493,-1.223073,1.593642,7.316402,0.373066,-0.851051,-9.361846,8.021209,5.396933,-4.239017,7.782533,9.574124,8.744960,-3.065498,-2.976232,-6.487838,-2.463382,-8.045370,-3.654874,-1.101291,1.803707,7.651801,-9.532737,-0.423007,-0.501031,8.587427,-1.375208,1.688319,-0.291962,8.329807,7.415166,-9.863570,-6.942625,2.968752,-5.689948,4.277127,-0.413073,-9.034766,2.396563,7.138358,9.657364,-8.843929,0.925966,1.499319,1.673754,-9.773072,7.815823,-7.239356,-4.798482,-3.448142,-4.571830,-3.199062]], dtype = "float64")#candidate|5802|(3, 88)|const|float64
var_5803 = relay.var("var_5803", dtype = "float32", shape = (135,))#candidate|5803|(135,)|var|float32
const_5804 = relay.const([-2.418328,-0.993734,1.877227,0.287364,-6.031438,-0.059524,-4.836754,-0.488175,-6.446079,-6.230688,-8.930845,-0.175700,2.530625,-2.679503,-5.917850,2.743676,7.418234,-8.754915,-8.627985,-0.044549,-6.611407,-1.207627,3.855078,2.300543,4.342229,-7.456697,-1.388840,5.577451,0.144985,-8.511271,1.818613,-7.757890,-9.907113,-7.427564,-9.549365,6.516418,9.222915,-9.052645,-1.993658,-9.322819,7.040638,0.788250,4.767602,9.826427,3.432310,-5.681748,5.573134,8.780031,-2.522607,-5.638048,-9.181068,6.952968,8.307537,0.584062,1.988518,-9.429839,-6.022988,-7.358251,-0.730240,-2.453200,3.001313,-2.814312,6.966712,-0.274615,0.415373,9.536950,6.558678,1.634407,-7.137786,-4.691643,6.448465,-3.183845,2.418752,8.296489,-6.751090,8.727772,6.999718,-4.779850,4.853576,-0.618596,-1.320239,2.489175,-1.257621,-6.862497,5.618403,-7.251284,0.384099,-8.406493,6.704541,-9.789471,-4.885148,8.859182,-2.446605,-6.957226,1.914697,-0.381978,-4.089429,4.702707,7.007197,6.538174,-8.984870,5.462694,-2.848265,-5.550315,8.120455,5.900830,-3.909992,2.649688,7.029380,6.338421,-1.020568,-7.247638,1.656090,7.965599,2.469851,4.894441,-0.337539,-0.563117,-5.266040,-1.589290,6.311274,8.403562,3.539549,-4.094045,0.133690,0.477388,-1.194852,-4.320206,4.664463,-1.180650,7.687669,-2.347740,-5.271021,-9.224846,-8.276752,-6.965995,1.183940,4.135322,7.793833,6.245081,1.242725,-4.636597,-2.351679,7.434634,0.667094,-3.089790,9.390905,-9.845428,9.068864,3.175637,-0.039851,-9.213860,0.148750,-5.464722,9.970034,3.430687,-3.312098,-2.588914,1.759944,-9.622710,5.888048,4.676165,8.203544,-2.360852,-5.512136,-3.395760,-8.807634,-3.204384,4.226714,-8.166945,-4.735090,6.843673,0.787628,0.854463,-4.580944,9.393112,6.134502,-8.435039,5.704342,0.513805,-4.470925,-5.387143,-7.543717,9.677928,8.054744,4.477919,2.646180,-6.498522,-5.335658,8.137558,7.495268,8.279922,0.994723,0.762972,-3.000349,7.652565,7.190335,1.403764,-9.076339,8.243335,-2.324879,-1.197665,1.014476,2.350473,-8.895259,-2.673199,7.926165,-4.592361,-7.707499,2.333360,0.272351,1.680865,-5.491965,-0.398468,2.403072,-0.278971,-6.569534,-4.713780,3.780408,-3.660794,-7.668046,7.681223,-0.091629,5.985791,-6.142539,3.668915,3.451803,-1.418708,-9.457996,-4.458023,-1.272869,1.676976,3.995086,-1.587232,4.803581,2.340443,-8.394968,-5.807991,-9.998240,1.812386,-5.977165,-2.829576,2.615269,-9.245783,-4.452632,-3.201267,5.090991,3.788722,5.364863,-0.419321,-6.307048,-7.411189,-4.907670,0.380899,-2.916004,9.699600,-4.663377,-0.676043,-7.894257,4.799940,-8.523581,6.597397,2.265939,-6.685359,6.016453,-4.901923,-5.935617,-3.449388,9.268393,-7.669853,-3.509223,-2.160294,0.145850,-5.595911,4.659694,-7.861041,4.353469,-8.034847,5.236007,6.653708,9.181312,-8.476028,3.897111,-3.795701,5.510065,-9.640175,5.342828,-9.335248,-0.656213,-1.865774,-0.578944,9.406197,1.592891,-2.700736,-3.685643,6.991453,8.617194,-7.356672,-9.876283,4.189276,5.450011,3.071956,4.000975,3.693086,-7.428241,4.760081,1.258283,4.603846,-5.662482,8.408881,6.726039,-2.351815,-3.386946,2.190180,-4.932268,-3.378633,5.602339,-6.889467,8.404034,-3.721034,4.508612,-9.064130,-7.636893,6.852311,-1.109542,8.029386,0.408995,-4.649269,-0.260933,-5.567411,9.246446,-3.218365,-8.290610,6.101818,5.925105,-5.680973,0.357840,5.637307,-3.889981,4.072893,8.860005,-5.300741,-2.578124,-7.419452,5.175184,9.123113,-6.818124,5.695002,-3.255964,-1.963651,-5.529837,3.148655,-3.531300,6.540073,6.277891,2.299669,3.922506,-4.902375,-0.016420,2.363339,6.920770,-8.350077,-5.055581,3.894434,-3.219718,-7.787052,-0.456023,6.450075,-5.690746,8.357625,7.601281,-1.546164,-8.832316,-5.523694,-6.388246,-2.428614,8.537551,2.691703,-6.665813,-4.201453,-6.493406,2.895530,-3.717792,9.479217,1.218346,5.151241,3.620847,-9.107637,-5.900388,2.306542,-2.692016,-4.642487,-7.436873,9.103283,-3.625710,-5.823702,8.028059,9.844215,-2.373579,-3.156361,5.922500,-0.991725,-2.677148,7.433786,2.491003,4.022813,-4.169395,9.407345,0.229187,-6.292734,8.683688,-9.724401,-3.755730,-3.157460,3.925788,4.438973,-2.560335,4.880856,-5.333322,4.627550,4.696344,5.565221,5.144308,6.732833,1.132890,-4.563627,-4.762707,0.388743,7.799710,3.424139,4.529830,9.221971,-5.879087,-5.095938,2.418447,-1.590215,-1.768201,2.135418,2.095830,-9.102513,-0.064681,2.180468,5.446823,3.139232,-6.396829,1.582799,8.499636,-0.568607,-1.477976,-5.808892], dtype = "float32")#candidate|5804|(450,)|const|float32
call_5801 = relay.TupleGetItem(func_3503_call(relay.reshape(const_5802.astype('float64'), [264,]), relay.reshape(var_5803.astype('float32'), [135,]), relay.reshape(const_5804.astype('float32'), [450,]), ), 4)
call_5805 = relay.TupleGetItem(func_3508_call(relay.reshape(const_5802.astype('float64'), [264,]), relay.reshape(var_5803.astype('float32'), [135,]), relay.reshape(const_5804.astype('float32'), [450,]), ), 4)
bop_5807 = relay.subtract(const_5802.astype('int16'), call_5790.astype('int16')) # shape=(3, 88)
bop_5810 = relay.subtract(const_5802.astype('int16'), call_5791.astype('int16')) # shape=(3, 88)
func_5493_call = mod.get_global_var('func_5493')
func_5494_call = mutated_mod.get_global_var('func_5494')
call_5813 = relay.TupleGetItem(func_5493_call(), 0)
call_5814 = relay.TupleGetItem(func_5494_call(), 0)
output = relay.Tuple([uop_5796,call_5801,var_5803,const_5804,bop_5807,call_5813,])
output2 = relay.Tuple([uop_5798,call_5805,var_5803,const_5804,bop_5810,call_5814,])
func_5822 = relay.Function([var_5803,], output)
mod['func_5822'] = func_5822
mod = relay.transform.InferType()(mod)
mutated_mod['func_5822'] = func_5822
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5823 = relay.var("var_5823", dtype = "float32", shape = (135,))#candidate|5823|(135,)|var|float32
func_5822_call = mutated_mod.get_global_var('func_5822')
call_5824 = func_5822_call(var_5823)
output = call_5824
func_5825 = relay.Function([var_5823], output)
mutated_mod['func_5825'] = func_5825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4665_call = mod.get_global_var('func_4665')
func_4667_call = mutated_mod.get_global_var('func_4667')
call_5843 = relay.TupleGetItem(func_4665_call(), 0)
call_5844 = relay.TupleGetItem(func_4667_call(), 0)
func_5268_call = mod.get_global_var('func_5268')
func_5270_call = mutated_mod.get_global_var('func_5270')
var_5874 = relay.var("var_5874", dtype = "float32", shape = (182,))#candidate|5874|(182,)|var|float32
call_5873 = relay.TupleGetItem(func_5268_call(relay.reshape(var_5874.astype('float32'), [13, 2, 7])), 0)
call_5875 = relay.TupleGetItem(func_5270_call(relay.reshape(var_5874.astype('float32'), [13, 2, 7])), 0)
uop_5881 = relay.sinh(var_5874.astype('float64')) # shape=(182,)
uop_5884 = relay.atanh(uop_5881.astype('float32')) # shape=(182,)
func_2386_call = mod.get_global_var('func_2386')
func_2388_call = mutated_mod.get_global_var('func_2388')
call_5897 = relay.TupleGetItem(func_2386_call(), 1)
call_5898 = relay.TupleGetItem(func_2388_call(), 1)
uop_5899 = relay.rsqrt(uop_5881.astype('float32')) # shape=(182,)
output = relay.Tuple([call_5843,call_5873,uop_5884,call_5897,uop_5899,])
output2 = relay.Tuple([call_5844,call_5875,uop_5884,call_5898,uop_5899,])
func_5904 = relay.Function([var_5874,], output)
mod['func_5904'] = func_5904
mod = relay.transform.InferType()(mod)
mutated_mod['func_5904'] = func_5904
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5905 = relay.var("var_5905", dtype = "float32", shape = (182,))#candidate|5905|(182,)|var|float32
func_5904_call = mutated_mod.get_global_var('func_5904')
call_5906 = func_5904_call(var_5905)
output = call_5906
func_5907 = relay.Function([var_5905], output)
mutated_mod['func_5907'] = func_5907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2827_call = mod.get_global_var('func_2827')
func_2829_call = mutated_mod.get_global_var('func_2829')
call_5947 = relay.TupleGetItem(func_2827_call(), 0)
call_5948 = relay.TupleGetItem(func_2829_call(), 0)
output = relay.Tuple([call_5947,])
output2 = relay.Tuple([call_5948,])
func_5954 = relay.Function([], output)
mod['func_5954'] = func_5954
mod = relay.transform.InferType()(mod)
output = func_5954()
func_5955 = relay.Function([], output)
mutated_mod['func_5955'] = func_5955
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5977 = relay.var("var_5977", dtype = "float64", shape = (4, 8, 8))#candidate|5977|(4, 8, 8)|var|float64
uop_5978 = relay.asinh(var_5977.astype('float64')) # shape=(4, 8, 8)
func_2081_call = mod.get_global_var('func_2081')
func_2082_call = mutated_mod.get_global_var('func_2082')
call_5985 = relay.TupleGetItem(func_2081_call(), 0)
call_5986 = relay.TupleGetItem(func_2082_call(), 0)
func_2827_call = mod.get_global_var('func_2827')
func_2829_call = mutated_mod.get_global_var('func_2829')
call_6000 = relay.TupleGetItem(func_2827_call(), 0)
call_6001 = relay.TupleGetItem(func_2829_call(), 0)
output = relay.Tuple([uop_5978,call_5985,call_6000,])
output2 = relay.Tuple([uop_5978,call_5986,call_6001,])
func_6002 = relay.Function([var_5977,], output)
mod['func_6002'] = func_6002
mod = relay.transform.InferType()(mod)
var_6003 = relay.var("var_6003", dtype = "float64", shape = (4, 8, 8))#candidate|6003|(4, 8, 8)|var|float64
output = func_6002(var_6003)
func_6004 = relay.Function([var_6003], output)
mutated_mod['func_6004'] = func_6004
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6006 = relay.const([[[-8,5,7,-5,-4,8,-10,-6],[-10,6,8,1,2,-1,-9,-8],[-2,-6,9,-5,-10,2,4,8],[5,-7,-8,3,8,-2,4,6],[4,-6,3,-5,-6,3,-7,6],[-7,-2,-3,4,10,-10,5,-10]],[[-8,-4,-10,4,-6,-6,7,2],[4,8,1,-1,-7,5,7,-3],[-4,5,-5,-9,-7,-5,-8,-10],[-3,2,-10,6,5,1,7,-8],[2,6,-4,10,2,8,2,-4],[6,-10,-10,4,-8,-9,9,-7]],[[-3,-8,-7,-2,4,9,-8,3],[-9,-8,7,-6,7,9,5,8],[-8,8,-7,-2,-10,8,-4,-10],[4,-1,10,-6,-3,4,3,-7],[-8,-6,-5,5,9,-1,-6,5],[-9,-1,-2,-7,-3,4,-2,-7]],[[-5,-5,-1,-4,-6,5,-6,-2],[-5,-7,1,3,-6,10,-7,8],[7,-2,4,1,1,-3,-6,-3],[1,1,3,-6,2,-6,-10,-3],[-6,9,3,1,6,2,-1,5],[4,-4,10,7,-3,-1,5,-3]],[[-10,-10,-2,8,5,10,-6,9],[-10,8,-2,-10,-6,-9,-6,2],[3,-1,-3,3,-1,-5,7,-7],[-7,-7,-2,2,-9,-8,3,4],[-2,-3,6,-4,-8,-5,10,-3],[9,-4,8,-8,8,5,8,1]]], dtype = "uint32")#candidate|6006|(5, 6, 8)|const|uint32
var_6007 = relay.var("var_6007", dtype = "uint32", shape = (5, 6, 8))#candidate|6007|(5, 6, 8)|var|uint32
bop_6008 = relay.less(const_6006.astype('bool'), relay.reshape(var_6007.astype('bool'), relay.shape_of(const_6006))) # shape=(5, 6, 8)
output = relay.Tuple([bop_6008,])
output2 = relay.Tuple([bop_6008,])
func_6012 = relay.Function([var_6007,], output)
mod['func_6012'] = func_6012
mod = relay.transform.InferType()(mod)
var_6013 = relay.var("var_6013", dtype = "uint32", shape = (5, 6, 8))#candidate|6013|(5, 6, 8)|var|uint32
output = func_6012(var_6013)
func_6014 = relay.Function([var_6013], output)
mutated_mod['func_6014'] = func_6014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1170_call = mod.get_global_var('func_1170')
func_1172_call = mutated_mod.get_global_var('func_1172')
call_6022 = relay.TupleGetItem(func_1170_call(), 0)
call_6023 = relay.TupleGetItem(func_1172_call(), 0)
func_4725_call = mod.get_global_var('func_4725')
func_4728_call = mutated_mod.get_global_var('func_4728')
var_6025 = relay.var("var_6025", dtype = "bool", shape = (432,))#candidate|6025|(432,)|var|bool
call_6024 = func_4725_call(relay.reshape(var_6025.astype('bool'), [3, 16, 9]))
call_6026 = func_4725_call(relay.reshape(var_6025.astype('bool'), [3, 16, 9]))
output = relay.Tuple([call_6022,call_6024,var_6025,])
output2 = relay.Tuple([call_6023,call_6026,var_6025,])
func_6028 = relay.Function([var_6025,], output)
mod['func_6028'] = func_6028
mod = relay.transform.InferType()(mod)
var_6029 = relay.var("var_6029", dtype = "bool", shape = (432,))#candidate|6029|(432,)|var|bool
output = func_6028(var_6029)
func_6030 = relay.Function([var_6029], output)
mutated_mod['func_6030'] = func_6030
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2802_call = mod.get_global_var('func_2802')
func_2804_call = mutated_mod.get_global_var('func_2804')
call_6057 = relay.TupleGetItem(func_2802_call(), 0)
call_6058 = relay.TupleGetItem(func_2804_call(), 0)
func_1080_call = mod.get_global_var('func_1080')
func_1081_call = mutated_mod.get_global_var('func_1081')
call_6061 = relay.TupleGetItem(func_1080_call(), 0)
call_6062 = relay.TupleGetItem(func_1081_call(), 0)
const_6072 = relay.const([[[1,2,-9,8,-8,-6,-1,-5,-4,8,7],[9,7,-2,9,1,-5,2,8,5,4,-7],[4,10,3,3,-8,-7,-6,-9,8,-6,3],[-10,9,-8,-7,-2,7,9,1,-9,4,1],[-4,-6,-10,-7,2,5,3,6,8,-10,-9],[-4,-1,-9,-6,-7,-1,-3,7,2,-9,3],[-10,-3,7,3,4,-8,10,-4,-8,-7,5],[-7,-3,-6,-8,8,7,8,7,-2,9,-10],[9,-5,4,-5,-5,-5,-5,-3,-9,-5,-2]],[[-10,4,-2,6,-4,-5,-4,-5,9,-3,-10],[-7,-5,6,1,-3,-9,-5,-4,2,-7,-8],[-7,10,-5,-2,3,-10,6,-8,-5,1,8],[4,8,1,-4,-4,4,-9,-7,5,-2,8],[-2,8,7,-1,3,8,-3,7,-8,10,-5],[10,-2,1,2,4,8,-9,-9,-2,6,-6],[-7,-8,-3,6,7,-9,-2,3,-4,8,-6],[6,7,-10,8,-4,8,-1,-8,9,4,4],[-10,10,1,5,4,3,-1,-6,8,5,2]],[[4,-4,7,1,-4,6,7,3,-5,5,-10],[-10,7,-8,3,-8,-2,-10,-10,8,-3,1],[2,-10,-3,-6,3,-3,3,3,-1,-2,5],[2,2,1,-4,3,-6,-4,10,-4,-5,5],[8,3,1,4,7,3,-6,7,9,-8,5],[-6,2,-1,-6,-5,4,-4,3,-5,4,4],[-4,-3,-2,-8,5,-3,-3,-1,1,-3,-4],[-2,-7,-1,-4,-4,-5,1,-8,-4,4,-7],[4,-6,-6,7,-8,-6,5,9,-2,8,-9]],[[-5,-10,9,8,1,-8,6,7,-1,-4,3],[4,-9,-4,6,-7,-2,1,3,9,-3,10],[-8,-5,-4,-6,8,-9,-10,5,-6,-8,1],[10,-1,5,-6,3,4,3,-7,-4,-2,-2],[-6,8,-1,-2,6,-4,3,-10,6,2,-3],[9,3,7,-6,6,7,-6,10,9,-4,-2],[-4,-5,-10,-10,10,-5,3,-8,2,-1,-8],[7,8,4,1,-8,-10,5,8,3,7,10],[-1,-8,-10,1,-7,8,6,-7,7,10,-6]],[[7,10,-1,9,6,-8,2,3,-10,4,8],[-1,5,-2,-5,-1,4,4,8,-7,-3,9],[6,1,-6,3,4,-1,-2,-5,-5,1,8],[7,9,2,-10,7,5,-2,-2,-5,9,-7],[-2,9,-9,-7,8,-2,-9,-6,7,4,1],[3,3,10,-7,-4,-9,6,-7,-2,-8,-9],[1,5,9,8,-7,1,-10,-1,-8,-5,10],[-3,-6,-10,-1,1,-4,-10,8,-3,10,3],[5,-6,-1,-9,2,-9,-1,5,10,6,6]],[[9,3,-7,5,4,7,4,2,-10,9,5],[8,2,7,4,-1,7,4,-8,7,-9,-3],[-2,-8,9,10,5,-3,-8,2,-6,-4,8],[7,6,-9,8,-10,7,3,-5,-10,-2,7],[7,-3,-4,-6,-6,-10,6,-9,-1,5,9],[4,10,4,8,4,-3,-6,6,1,4,-6],[1,9,4,-2,1,-7,-9,-6,4,-10,-9],[-6,-10,-8,-8,-9,10,3,-9,9,2,-4],[6,-7,10,-7,-6,5,-10,2,-7,-7,6]],[[-3,6,8,5,-8,-10,1,-4,10,-3,-8],[9,-9,1,-3,7,-6,7,10,4,5,2],[-5,-6,8,1,2,-6,-6,8,-7,-7,-7],[-5,-6,-4,-4,-7,-3,-5,4,-7,-7,7],[3,7,10,3,6,-6,-8,3,9,4,-5],[-4,-6,-5,-5,10,-8,8,-9,-7,8,9],[-6,-1,-4,-8,3,-10,-5,3,7,-8,8],[-5,8,4,-7,-3,7,9,-8,-4,1,1],[9,5,-7,1,10,4,9,-3,5,1,-1]],[[-5,7,9,3,1,-4,-8,-1,8,-6,-9],[-4,-1,-10,1,3,10,7,-8,-9,-2,7],[-4,10,10,-6,-1,3,9,4,-5,-6,-9],[-4,5,5,-8,9,3,-6,3,1,-2,6],[8,-1,-9,9,4,-4,-9,-6,3,9,-5],[10,6,-4,8,2,-1,8,-2,9,-10,-4],[-2,-6,-8,-3,-7,-2,6,3,-7,-7,-8],[10,4,7,-2,3,-1,-3,3,1,10,-6],[1,-8,4,9,-4,3,10,-2,-1,10,-5]],[[3,10,-1,-9,-7,-4,-9,2,-10,6,-4],[3,1,-2,-6,-4,6,-4,4,-2,4,-6],[8,-10,6,-4,-4,-8,-1,-6,7,7,-1],[8,4,6,10,10,4,6,10,2,-7,9],[-1,6,-2,-1,3,10,-3,-5,8,3,-9],[-4,1,1,6,-5,-4,7,5,10,-9,-7],[-5,-7,2,-7,-1,8,-6,-7,8,1,4],[-9,-6,-10,7,1,-2,7,8,-4,4,10],[-10,2,10,3,1,-6,-9,4,-4,8,-3]],[[1,-10,2,-9,-3,1,9,1,9,2,-9],[-2,6,9,-5,10,8,2,-5,-4,10,-8],[-9,10,8,-3,-4,-3,-4,-8,-7,-2,-10],[4,-5,-6,4,-3,10,2,7,7,2,-4],[4,-3,2,-5,2,-6,10,2,-5,-10,10],[4,-7,1,-3,-8,-8,-8,-8,1,-6,9],[-10,-3,-7,9,-5,7,4,-3,-2,3,-10],[10,-8,10,-9,-2,-3,5,8,-7,9,-4],[1,-1,6,7,-7,-6,8,-8,8,-10,-5]]], dtype = "int16")#candidate|6072|(10, 9, 11)|const|int16
bop_6073 = relay.logical_and(call_6061.astype('bool'), const_6072.astype('bool')) # shape=(10, 9, 11)
bop_6076 = relay.logical_and(call_6062.astype('bool'), const_6072.astype('bool')) # shape=(10, 9, 11)
uop_6084 = relay.cosh(const_6072.astype('float32')) # shape=(10, 9, 11)
uop_6090 = relay.asinh(const_6072.astype('float64')) # shape=(10, 9, 11)
bop_6092 = relay.less(uop_6090.astype('bool'), relay.reshape(bop_6073.astype('bool'), relay.shape_of(uop_6090))) # shape=(10, 9, 11)
bop_6095 = relay.less(uop_6090.astype('bool'), relay.reshape(bop_6076.astype('bool'), relay.shape_of(uop_6090))) # shape=(10, 9, 11)
bop_6098 = relay.left_shift(uop_6084.astype('uint64'), relay.reshape(bop_6073.astype('uint64'), relay.shape_of(uop_6084))) # shape=(10, 9, 11)
bop_6101 = relay.left_shift(uop_6084.astype('uint64'), relay.reshape(bop_6076.astype('uint64'), relay.shape_of(uop_6084))) # shape=(10, 9, 11)
uop_6108 = relay.acos(const_6072.astype('float64')) # shape=(10, 9, 11)
func_3907_call = mod.get_global_var('func_3907')
func_3910_call = mutated_mod.get_global_var('func_3910')
const_6116 = relay.const([False,True,True,True,True,False,False,False,True,True,True,True,False,False,False,True,True,True,True,True,False,True,True,False,False,False,True], dtype = "bool")#candidate|6116|(27,)|const|bool
call_6115 = func_3907_call(relay.reshape(const_6116.astype('bool'), [3, 1, 9]))
call_6117 = func_3907_call(relay.reshape(const_6116.astype('bool'), [3, 1, 9]))
output = relay.Tuple([call_6057,bop_6092,bop_6098,uop_6108,call_6115,const_6116,])
output2 = relay.Tuple([call_6058,bop_6095,bop_6101,uop_6108,call_6117,const_6116,])
func_6121 = relay.Function([], output)
mod['func_6121'] = func_6121
mod = relay.transform.InferType()(mod)
mutated_mod['func_6121'] = func_6121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6121_call = mutated_mod.get_global_var('func_6121')
call_6122 = func_6121_call()
output = call_6122
func_6123 = relay.Function([], output)
mutated_mod['func_6123'] = func_6123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3258_call = mod.get_global_var('func_3258')
func_3260_call = mutated_mod.get_global_var('func_3260')
call_6179 = relay.TupleGetItem(func_3258_call(), 0)
call_6180 = relay.TupleGetItem(func_3260_call(), 0)
func_5142_call = mod.get_global_var('func_5142')
func_5144_call = mutated_mod.get_global_var('func_5144')
call_6196 = relay.TupleGetItem(func_5142_call(), 0)
call_6197 = relay.TupleGetItem(func_5144_call(), 0)
output = relay.Tuple([call_6179,call_6196,])
output2 = relay.Tuple([call_6180,call_6197,])
func_6204 = relay.Function([], output)
mod['func_6204'] = func_6204
mod = relay.transform.InferType()(mod)
output = func_6204()
func_6205 = relay.Function([], output)
mutated_mod['func_6205'] = func_6205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5504_call = mod.get_global_var('func_5504')
func_5506_call = mutated_mod.get_global_var('func_5506')
call_6206 = relay.TupleGetItem(func_5504_call(), 0)
call_6207 = relay.TupleGetItem(func_5506_call(), 0)
output = call_6206
output2 = call_6207
func_6217 = relay.Function([], output)
mod['func_6217'] = func_6217
mod = relay.transform.InferType()(mod)
output = func_6217()
func_6218 = relay.Function([], output)
mutated_mod['func_6218'] = func_6218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5142_call = mod.get_global_var('func_5142')
func_5144_call = mutated_mod.get_global_var('func_5144')
call_6235 = relay.TupleGetItem(func_5142_call(), 0)
call_6236 = relay.TupleGetItem(func_5144_call(), 0)
func_2694_call = mod.get_global_var('func_2694')
func_2695_call = mutated_mod.get_global_var('func_2695')
call_6237 = func_2694_call()
call_6238 = func_2694_call()
func_5042_call = mod.get_global_var('func_5042')
func_5044_call = mutated_mod.get_global_var('func_5044')
call_6240 = relay.TupleGetItem(func_5042_call(), 0)
call_6241 = relay.TupleGetItem(func_5044_call(), 0)
func_3276_call = mod.get_global_var('func_3276')
func_3277_call = mutated_mod.get_global_var('func_3277')
call_6253 = relay.TupleGetItem(func_3276_call(), 0)
call_6254 = relay.TupleGetItem(func_3277_call(), 0)
output = relay.Tuple([call_6235,call_6237,call_6240,call_6253,])
output2 = relay.Tuple([call_6236,call_6238,call_6241,call_6254,])
func_6259 = relay.Function([], output)
mod['func_6259'] = func_6259
mod = relay.transform.InferType()(mod)
output = func_6259()
func_6260 = relay.Function([], output)
mutated_mod['func_6260'] = func_6260
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6280 = relay.var("var_6280", dtype = "float64", shape = (7, 8, 1))#candidate|6280|(7, 8, 1)|var|float64
var_6281 = relay.var("var_6281", dtype = "float64", shape = (7, 8, 4))#candidate|6281|(7, 8, 4)|var|float64
bop_6282 = relay.power(var_6280.astype('float64'), var_6281.astype('float64')) # shape=(7, 8, 4)
func_4665_call = mod.get_global_var('func_4665')
func_4667_call = mutated_mod.get_global_var('func_4667')
call_6301 = relay.TupleGetItem(func_4665_call(), 0)
call_6302 = relay.TupleGetItem(func_4667_call(), 0)
func_4538_call = mod.get_global_var('func_4538')
func_4541_call = mutated_mod.get_global_var('func_4541')
const_6304 = relay.const([-3,9,-9,3,4,-5,-10,8,-3,10,4,-3,3,2,-10,1,8,-5,-4,3,10,-4,7,6,4,4,-9,1,-5,-7,10,2,9,-6,-6,8,9,8,-4,5,-10,6,-8,-9,-3,-1,6,2,-9,-8,-1,4,-10,7,-9,-4,1,-6,10,-3,-6,6,6,-7,8,3,-2,1,-1,8,9,7,-3,-3,2,3,-10,10,-9,-4,-2,8,4,-8,8,-3,7,10,-6,-2,-9,-8,6,-5,-7,-5,6,5,-5,-4,-8,-1,-10,-4,2,-7,-10,9,3,2,5,-6,-1,10,3,-8,-5,-5,-9,-1,2,-1,-3,10,-6,-3,-8,-1,-2,-6,7,8,-2,-6,2,2,-7,8,-7,3,9,-2,7,-9,-6,-5,-8,6,-6,10,2,-3,9,9,10,-7,10,-9,7,-5,2,8,3,-9,-8,6,-3,1,10,7,-1,-10,-8,-7,6,5,-4,-7,7,-5,-9,5,3,5,5,5,8,9,4,-8,10,8,8,-10,-5,10,-9,5,10,-5,-10,2,-4,4,9,-8,-7,10,6,-8,6,-3,2,6,6,8,-10,5,-3,3,1,10,2,3,3,-6,-1,3,7,-7,9,-10,-10,-4,-4,-7,-2,4,1,1,1,3,6,-5,-5,5,-2,4,10,6,-7,-10,2,-5,1,6,-3,4,-5,2,3,-4,2,6,-6,-5,-5,-3,9,1,4,-4,6,-8,-8,1,-8,6,-2,2,-7,2,2,-1,5,-2,9,8,5,6,-6,7,-3,6,7,3,4,6,-3,6,-8,7,-6,5,-10,-7,10,-4,6,6,9,7,-7,9,3,5,6,1,8,-5,6,9,-3,7,-3,3,4,-5,-7,10,10,3,1,9,-7,10,-4,7,1,9,9,-8,-5,6,7,-4,-3,-4,9,4,8,9,-4,-1,2,-1,-3,-6,9,-2,9,-5,3,7,-3,-9,-4,4,7,-2,-7,-2,1,-1,-1,9,1,2,-3,5,9,-10,-2,-2,-10,-8,9,-1,9,3,7,9,7,-1,10,10,-9,4,-3,-10,1,3,-9,2,-6,-9,-8,10,-10,8,6,9,8,-7,-10,-5,-3,2,-5,-2,-9,6,7,-5,-9,-9,2,-10,-3,-1,-2,-5,7,8,10,-2,1,10,-4,-7,9,7,7,-2,-6,5,-9,4,-6,7,4,-6,-9,-3,1,-7,-7,2,6,6,6,8,10,3,-6,-1,-2,-5,5,-6,-9,9,-9,-2,6,5,-7,-7,-8,-2], dtype = "int8")#candidate|6304|(480,)|const|int8
call_6303 = relay.TupleGetItem(func_4538_call(relay.reshape(const_6304.astype('int8'), [10, 6, 8]), relay.reshape(const_6304.astype('int8'), [10, 6, 8]), ), 2)
call_6305 = relay.TupleGetItem(func_4541_call(relay.reshape(const_6304.astype('int8'), [10, 6, 8]), relay.reshape(const_6304.astype('int8'), [10, 6, 8]), ), 2)
output = relay.Tuple([bop_6282,call_6301,call_6303,const_6304,])
output2 = relay.Tuple([bop_6282,call_6302,call_6305,const_6304,])
func_6321 = relay.Function([var_6280,var_6281,], output)
mod['func_6321'] = func_6321
mod = relay.transform.InferType()(mod)
var_6322 = relay.var("var_6322", dtype = "float64", shape = (7, 8, 1))#candidate|6322|(7, 8, 1)|var|float64
var_6323 = relay.var("var_6323", dtype = "float64", shape = (7, 8, 4))#candidate|6323|(7, 8, 4)|var|float64
output = func_6321(var_6322,var_6323,)
func_6324 = relay.Function([var_6322,var_6323,], output)
mutated_mod['func_6324'] = func_6324
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6217_call = mod.get_global_var('func_6217')
func_6218_call = mutated_mod.get_global_var('func_6218')
call_6360 = func_6217_call()
call_6361 = func_6217_call()
const_6398 = relay.const([[[2],[-2],[5],[-10],[9],[8],[3],[-1],[2],[7],[1],[8],[-5]],[[-8],[6],[8],[3],[2],[-8],[-8],[2],[-4],[-5],[1],[-10],[-7]],[[10],[4],[-10],[8],[-2],[-3],[6],[7],[-10],[2],[3],[8],[-3]],[[-9],[-9],[6],[2],[7],[-2],[9],[3],[3],[7],[-5],[4],[-8]],[[5],[5],[7],[3],[-10],[5],[6],[-7],[1],[2],[-8],[-3],[-4]],[[-2],[8],[-3],[8],[-1],[4],[8],[10],[8],[-9],[4],[-1],[-4]],[[-3],[5],[-7],[-6],[-9],[-6],[-7],[-9],[-10],[4],[4],[7],[7]],[[3],[-2],[-8],[-6],[-4],[10],[-6],[9],[7],[10],[8],[4],[-1]],[[6],[-4],[-1],[-2],[6],[10],[4],[2],[2],[-4],[-3],[-8],[6]],[[-4],[-7],[-1],[-5],[9],[-3],[-9],[-2],[-8],[-2],[10],[-2],[6]],[[3],[8],[-9],[-2],[-9],[1],[-7],[8],[-1],[9],[-7],[-10],[9]],[[3],[-2],[9],[-5],[7],[-9],[-10],[3],[2],[2],[-9],[8],[-6]],[[7],[4],[-6],[9],[7],[7],[5],[4],[4],[-4],[-7],[-6],[6]],[[-2],[3],[9],[-6],[8],[-9],[-1],[-3],[8],[2],[-3],[10],[-3]]], dtype = "int16")#candidate|6398|(14, 13, 1)|const|int16
bop_6399 = relay.logical_and(call_6360.astype('bool'), const_6398.astype('bool')) # shape=(14, 13, 1)
bop_6402 = relay.logical_and(call_6361.astype('bool'), const_6398.astype('bool')) # shape=(14, 13, 1)
bop_6412 = relay.less(const_6398.astype('bool'), call_6360.astype('bool')) # shape=(14, 13, 1)
bop_6415 = relay.less(const_6398.astype('bool'), call_6361.astype('bool')) # shape=(14, 13, 1)
uop_6416 = relay.acosh(bop_6399.astype('float64')) # shape=(14, 13, 1)
uop_6418 = relay.acosh(bop_6402.astype('float64')) # shape=(14, 13, 1)
output = relay.Tuple([bop_6412,uop_6416,])
output2 = relay.Tuple([bop_6415,uop_6418,])
F = relay.Function([], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([], output2)
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
