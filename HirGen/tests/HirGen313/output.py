import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_211 = relay.const([[[9.305847],[4.634586],[-6.059246]],[[-1.957854],[-5.102613],[-5.479343]],[[8.602757],[-1.208926],[-1.101890]],[[1.593104],[-8.772382],[-8.562671]],[[1.154282],[7.196744],[7.787103]]], dtype = "float64")#candidate|211|(5, 3, 1)|const|float64
uop_212 = relay.sinh(const_211.astype('float64')) # shape=(5, 3, 1)
bop_223 = relay.bitwise_and(const_211.astype('int16'), relay.reshape(uop_212.astype('int16'), relay.shape_of(const_211))) # shape=(5, 3, 1)
uop_229 = relay.sin(bop_223.astype('float64')) # shape=(5, 3, 1)
var_234 = relay.var("var_234", dtype = "float64", shape = (5, 3, 16))#candidate|234|(5, 3, 16)|var|float64
bop_235 = relay.multiply(uop_212.astype('float64'), var_234.astype('float64')) # shape=(5, 3, 16)
output = relay.Tuple([uop_229,bop_235,])
output2 = relay.Tuple([uop_229,bop_235,])
func_244 = relay.Function([var_234,], output)
mod['func_244'] = func_244
mod = relay.transform.InferType()(mod)
var_245 = relay.var("var_245", dtype = "float64", shape = (5, 3, 16))#candidate|245|(5, 3, 16)|var|float64
output = func_244(var_245)
func_246 = relay.Function([var_245], output)
mutated_mod['func_246'] = func_246
mutated_mod = relay.transform.InferType()(mutated_mod)
var_808 = relay.var("var_808", dtype = "float32", shape = ())#candidate|808|()|var|float32
const_809 = relay.const([[[-6.405317],[-8.029310],[5.251588],[-2.162925],[2.338195]],[[2.532892],[6.183776],[-3.207998],[6.728114],[0.505388]],[[-5.575028],[-9.800409],[-8.208400],[5.036790],[5.537772]],[[-2.724089],[-8.711455],[7.964110],[-0.842424],[8.142195]]], dtype = "float32")#candidate|809|(4, 5, 1)|const|float32
bop_810 = relay.not_equal(var_808.astype('bool'), const_809.astype('bool')) # shape=(4, 5, 1)
output = bop_810
output2 = bop_810
func_845 = relay.Function([var_808,], output)
mod['func_845'] = func_845
mod = relay.transform.InferType()(mod)
var_846 = relay.var("var_846", dtype = "float32", shape = ())#candidate|846|()|var|float32
output = func_845(var_846)
func_847 = relay.Function([var_846], output)
mutated_mod['func_847'] = func_847
mutated_mod = relay.transform.InferType()(mutated_mod)
var_876 = relay.var("var_876", dtype = "float64", shape = (3, 6, 7))#candidate|876|(3, 6, 7)|var|float64
uop_877 = relay.cosh(var_876.astype('float64')) # shape=(3, 6, 7)
output = uop_877
output2 = uop_877
func_893 = relay.Function([var_876,], output)
mod['func_893'] = func_893
mod = relay.transform.InferType()(mod)
var_894 = relay.var("var_894", dtype = "float64", shape = (3, 6, 7))#candidate|894|(3, 6, 7)|var|float64
output = func_893(var_894)
func_895 = relay.Function([var_894], output)
mutated_mod['func_895'] = func_895
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1019 = relay.var("var_1019", dtype = "uint16", shape = (15, 4, 3))#candidate|1019|(15, 4, 3)|var|uint16
var_1020 = relay.var("var_1020", dtype = "uint16", shape = (15, 4, 3))#candidate|1020|(15, 4, 3)|var|uint16
bop_1021 = relay.left_shift(var_1019.astype('uint16'), relay.reshape(var_1020.astype('uint16'), relay.shape_of(var_1019))) # shape=(15, 4, 3)
uop_1024 = relay.log2(var_1019.astype('float32')) # shape=(15, 4, 3)
uop_1036 = relay.sigmoid(var_1020.astype('float64')) # shape=(15, 4, 3)
bop_1038 = relay.greater_equal(var_1020.astype('bool'), relay.reshape(uop_1036.astype('bool'), relay.shape_of(var_1020))) # shape=(15, 4, 3)
bop_1044 = relay.greater(bop_1021.astype('bool'), relay.reshape(bop_1038.astype('bool'), relay.shape_of(bop_1021))) # shape=(15, 4, 3)
output = relay.Tuple([uop_1024,bop_1044,])
output2 = relay.Tuple([uop_1024,bop_1044,])
func_1050 = relay.Function([var_1019,var_1020,], output)
mod['func_1050'] = func_1050
mod = relay.transform.InferType()(mod)
var_1051 = relay.var("var_1051", dtype = "uint16", shape = (15, 4, 3))#candidate|1051|(15, 4, 3)|var|uint16
var_1052 = relay.var("var_1052", dtype = "uint16", shape = (15, 4, 3))#candidate|1052|(15, 4, 3)|var|uint16
output = func_1050(var_1051,var_1052,)
func_1053 = relay.Function([var_1051,var_1052,], output)
mutated_mod['func_1053'] = func_1053
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1081 = relay.var("var_1081", dtype = "float64", shape = (8, 2, 10))#candidate|1081|(8, 2, 10)|var|float64
uop_1082 = relay.asinh(var_1081.astype('float64')) # shape=(8, 2, 10)
func_244_call = mod.get_global_var('func_244')
func_246_call = mutated_mod.get_global_var('func_246')
const_1095 = relay.const([2.941307,2.750133,8.810738,1.835521,-5.782476,-3.003661,2.510299,-3.306737,5.844010,-7.761137,-4.721828,9.742078,-9.351282,0.297889,-9.653291,-9.288652,-1.410299,5.826807,1.438424,-7.624767,-7.494712,-6.157869,2.773726,0.400438,-8.867351,0.441702,1.027199,-1.726258,-3.448115,7.089822,-9.973736,-7.294811,6.475570,-8.737416,-8.773403,-0.766009,-7.087676,-4.963013,1.344365,-5.233931,8.833350,-3.734691,-8.552614,-5.742470,-4.550568,7.737105,0.180830,0.571588,1.089126,-2.559309,-7.418631,-3.167668,4.279529,-0.075522,-4.961423,-6.344974,6.749639,-8.359649,-6.047424,-3.565713,-3.475159,2.157955,2.459567,-5.368431,-7.941958,-8.737451,4.154310,0.089599,-7.905582,5.250985,-3.950225,-0.385777,-9.139522,2.842486,-8.320940,-9.600628,1.917090,-6.774851,-4.025843,5.501310,4.372732,-4.575814,-4.461411,0.129924,4.449850,-0.151554,6.107870,4.028549,1.036793,-1.764433,-6.185388,2.861618,-7.672945,-3.056723,-7.072674,3.854999,-0.165384,4.893716,-3.589744,5.197083,6.804410,6.044147,-5.261944,6.793832,-9.332061,9.799541,-7.916595,-9.747421,1.893021,4.853272,3.756005,1.511834,-1.656769,-4.526221,-7.566158,6.263563,7.376132,-0.340941,6.553288,-4.845118,2.676590,9.900424,-0.700653,-8.069874,-2.139209,0.812956,-3.156956,4.214238,6.833414,5.295645,9.124495,-3.797672,-4.988943,6.721211,-7.359092,5.927324,2.561501,7.433647,-9.078004,4.360038,1.159692,-5.209932,-9.739391,2.809324,-9.737351,6.173381,6.548922,-6.665900,-7.770721,2.645461,8.287436,-6.836367,9.805992,-8.484486,2.972552,4.549367,9.519164,-3.123065,9.789554,6.822651,1.874773,-7.304252,-9.213963,-5.350147,-4.820786,0.476178,-8.667100,-8.599413,8.403172,7.636269,0.600024,-6.125075,2.803047,-2.134362,-6.055849,-3.959341,-2.783765,-0.715012,1.612344,0.495968,-9.275158,-4.450492,-8.491984,7.758657,5.020465,-1.622532,6.633624,4.839268,1.220929,3.748434,-3.172708,6.434817,-5.564065,0.189210,-4.815749,8.464924,-8.060411,1.970065,1.671684,-8.704628,-5.401036,7.416506,5.976755,-3.434630,-3.511617,-2.154790,1.911965,7.529572,4.938397,5.422319,1.519546,7.060477,-4.605443,-0.538849,7.380633,1.422438,9.187742,6.240226,7.560160,7.804187,8.249417,-8.634575,-2.436634,3.415838,0.975602,2.497479,2.371424,-7.798386,-3.414740,2.079947,0.366464,2.215042,5.127122,-1.461890,-2.633674,-0.562094,8.835231,-7.092900,-5.726579,-1.367863], dtype = "float64")#candidate|1095|(240,)|const|float64
call_1094 = relay.TupleGetItem(func_244_call(relay.reshape(const_1095.astype('float64'), [5, 3, 16])), 0)
call_1096 = relay.TupleGetItem(func_246_call(relay.reshape(const_1095.astype('float64'), [5, 3, 16])), 0)
output = relay.Tuple([uop_1082,call_1094,const_1095,])
output2 = relay.Tuple([uop_1082,call_1096,const_1095,])
func_1107 = relay.Function([var_1081,], output)
mod['func_1107'] = func_1107
mod = relay.transform.InferType()(mod)
var_1108 = relay.var("var_1108", dtype = "float64", shape = (8, 2, 10))#candidate|1108|(8, 2, 10)|var|float64
output = func_1107(var_1108)
func_1109 = relay.Function([var_1108], output)
mutated_mod['func_1109'] = func_1109
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1308 = relay.var("var_1308", dtype = "int32", shape = (3, 1, 2))#candidate|1308|(3, 1, 2)|var|int32
const_1309 = relay.const([[[-4,-6],[-5,2],[9,7],[8,3],[-5,-1],[-3,-6]],[[-5,-8],[6,2],[-4,6],[3,9],[3,-7],[-7,-6]],[[3,7],[-4,2],[3,-4],[-9,-8],[5,2],[6,-9]]], dtype = "int32")#candidate|1309|(3, 6, 2)|const|int32
bop_1310 = relay.less_equal(var_1308.astype('bool'), const_1309.astype('bool')) # shape=(3, 6, 2)
output = bop_1310
output2 = bop_1310
func_1330 = relay.Function([var_1308,], output)
mod['func_1330'] = func_1330
mod = relay.transform.InferType()(mod)
var_1331 = relay.var("var_1331", dtype = "int32", shape = (3, 1, 2))#candidate|1331|(3, 1, 2)|var|int32
output = func_1330(var_1331)
func_1332 = relay.Function([var_1331], output)
mutated_mod['func_1332'] = func_1332
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1699 = relay.const([[[2.222454,-9.504694,-7.264897,-1.943459,-6.266363,7.492692,-6.737458,-5.710980,-4.456436,6.987740],[8.086115,-4.853618,-4.869739,-7.699967,-7.778369,1.688677,-5.012216,0.179868,-3.007120,5.730281],[6.778756,3.797673,-8.858908,9.717088,8.320160,-9.484779,-1.526515,-9.951857,0.305560,-4.233059],[-0.080794,-9.973103,0.133522,7.123970,5.234112,-3.030416,-6.013647,8.115548,4.624362,4.358454],[6.840497,-1.123162,0.352157,-1.811639,9.268605,-5.129896,-2.365864,-9.069132,-1.268838,1.137738],[-2.186013,-7.676363,-0.227385,-9.321578,-6.840745,-0.846004,4.451534,-7.928019,4.923273,7.088252]],[[9.825278,8.396051,-0.257937,2.024130,0.463383,2.084442,-7.963941,-0.005208,4.005959,3.678474],[9.051715,3.821461,-8.698285,4.179246,-6.180446,-0.267376,-3.363516,-9.065262,0.772400,7.898768],[-1.189334,0.952473,-0.732433,7.748844,-0.948565,-6.559349,4.180161,-9.685695,8.489822,3.050558],[-1.382745,6.191642,3.854773,-2.696478,8.747257,-9.062893,-8.973159,-4.224453,9.285620,-5.804306],[-7.731130,5.463591,-6.537556,6.530969,0.799558,7.783683,-6.953149,-6.032555,-0.107963,2.772993],[-1.743423,-5.808463,7.946088,-9.267892,-6.393728,-4.767333,3.805081,-6.272832,5.723448,0.885695]],[[2.319839,-4.173571,1.308482,5.111656,8.878801,2.451235,-7.583615,-6.205822,-2.499667,2.905060],[3.429258,-6.351092,7.799736,-9.608464,-3.691073,-0.028326,4.961453,-7.988372,6.246511,-4.851542],[-7.586449,9.006970,9.714828,-2.552252,-0.434054,1.155851,9.046275,-1.627719,-0.373394,3.056685],[-9.180634,-7.433261,-6.748669,-4.168610,9.140678,8.402530,-8.508427,-2.431938,-4.342223,6.928802],[-2.049807,7.889057,-0.261786,3.309998,-3.275104,-6.796480,-3.803492,-7.629817,9.117065,-0.322566],[-4.291373,-9.034398,-1.688102,-1.398964,2.887164,4.608697,-4.527293,2.561210,-2.504623,-4.182005]],[[4.964665,1.957324,0.678386,-7.787499,-3.903889,5.793456,-4.164627,6.017039,4.549200,-7.130390],[-4.235976,-2.064968,-3.183254,4.012137,-3.111198,8.865990,-6.665283,1.223559,1.625893,-3.381327],[7.403115,-6.138245,3.866758,-5.408256,9.412306,4.786567,6.799949,8.704048,8.634388,-1.287021],[-2.046036,0.987676,1.823375,-8.083383,3.600356,-0.594631,2.374024,-1.157484,5.484194,3.692110],[2.331507,-8.064588,-6.024678,-3.476871,-6.129493,-8.000956,9.538885,-9.568252,-1.362028,5.465400],[3.466472,-4.914012,-5.366326,-1.537546,-9.918635,-5.030258,-9.894782,-8.351347,-2.951808,1.139989]],[[4.355019,1.329607,4.418419,3.478376,9.353923,1.891552,6.329884,2.360042,1.784247,9.464015],[1.151702,1.934309,-3.218617,-0.230945,3.010184,0.659076,3.471280,4.174615,-1.366557,2.146240],[5.739413,6.662852,-4.132854,-2.293198,-5.373564,9.661745,1.478396,9.983330,-3.107330,3.460196],[6.236163,9.250009,6.452771,-6.663555,4.210777,3.058777,-8.895360,6.232833,0.015861,-1.507402],[0.794509,4.643672,3.178424,-3.006642,4.527609,8.549715,4.234794,7.998239,0.329202,-0.098466],[8.648866,4.695575,-6.073014,5.905865,-5.200470,9.849240,0.330112,-2.244222,-9.456070,1.942205]],[[-8.893292,-0.813042,8.335539,8.268100,7.409959,1.604542,8.241816,4.758098,-1.200670,-8.844197],[-3.425820,-9.634647,-5.932369,-0.867521,-7.714215,-0.251601,-9.755788,-9.261382,3.984324,-4.270417],[5.337614,2.919771,-8.023245,3.877168,8.741362,4.148874,8.632405,-8.757044,0.991118,-6.849653],[-3.682047,-9.704458,-0.190680,-2.693782,-4.980009,-0.015027,-9.748920,9.317623,-1.096924,6.108204],[-9.564885,-7.599357,4.202680,9.072463,4.219138,-1.997625,7.414622,4.844921,0.523236,6.272697],[-4.205006,0.078727,0.974907,-7.548886,0.138175,-6.111937,-0.560345,-7.122097,6.752315,-8.083222]],[[3.908281,-9.900417,-1.795016,-1.352030,3.797341,3.349430,-4.228757,-1.130433,6.782759,5.465094],[6.218340,-8.384571,-5.958112,6.975253,0.117794,7.032883,-2.248249,6.320639,7.923978,-8.329054],[1.552380,-6.439637,-1.052561,5.358330,8.015507,5.902560,-6.926796,9.234630,-4.144444,-5.942643],[-5.717165,-2.874128,5.890584,3.632567,-7.138832,6.576552,-8.391121,4.702862,8.954066,-8.396838],[8.443738,2.122149,-6.251388,3.487770,2.393267,-5.635496,3.001714,-7.692083,-9.220315,3.483591],[4.079673,-5.006405,-1.472663,-0.511170,-0.430819,1.264510,-3.225653,-2.725465,2.795647,6.196370]]], dtype = "float32")#candidate|1699|(7, 6, 10)|const|float32
uop_1700 = relay.cos(const_1699.astype('float32')) # shape=(7, 6, 10)
output = relay.Tuple([uop_1700,])
output2 = relay.Tuple([uop_1700,])
func_1714 = relay.Function([], output)
mod['func_1714'] = func_1714
mod = relay.transform.InferType()(mod)
output = func_1714()
func_1715 = relay.Function([], output)
mutated_mod['func_1715'] = func_1715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1714_call = mod.get_global_var('func_1714')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_1769 = relay.TupleGetItem(func_1714_call(), 0)
call_1770 = relay.TupleGetItem(func_1715_call(), 0)
var_1778 = relay.var("var_1778", dtype = "float32", shape = (7, 6, 10))#candidate|1778|(7, 6, 10)|var|float32
bop_1779 = relay.equal(call_1769.astype('bool'), relay.reshape(var_1778.astype('bool'), relay.shape_of(call_1769))) # shape=(7, 6, 10)
bop_1782 = relay.equal(call_1770.astype('bool'), relay.reshape(var_1778.astype('bool'), relay.shape_of(call_1770))) # shape=(7, 6, 10)
func_1330_call = mod.get_global_var('func_1330')
func_1332_call = mutated_mod.get_global_var('func_1332')
const_1789 = relay.const([[10],[-5],[3],[5],[6],[1]], dtype = "int32")#candidate|1789|(6, 1)|const|int32
call_1788 = func_1330_call(relay.reshape(const_1789.astype('int32'), [3, 1, 2]))
call_1790 = func_1330_call(relay.reshape(const_1789.astype('int32'), [3, 1, 2]))
func_845_call = mod.get_global_var('func_845')
func_847_call = mutated_mod.get_global_var('func_847')
var_1794 = relay.var("var_1794", dtype = "float32", shape = ())#candidate|1794|()|var|float32
call_1793 = func_845_call(relay.reshape(var_1794.astype('float32'), []))
call_1795 = func_845_call(relay.reshape(var_1794.astype('float32'), []))
output = relay.Tuple([bop_1779,call_1788,const_1789,call_1793,var_1794,])
output2 = relay.Tuple([bop_1782,call_1790,const_1789,call_1795,var_1794,])
func_1800 = relay.Function([var_1778,var_1794,], output)
mod['func_1800'] = func_1800
mod = relay.transform.InferType()(mod)
mutated_mod['func_1800'] = func_1800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1800_call = mutated_mod.get_global_var('func_1800')
var_1802 = relay.var("var_1802", dtype = "float32", shape = (7, 6, 10))#candidate|1802|(7, 6, 10)|var|float32
var_1803 = relay.var("var_1803", dtype = "float32", shape = ())#candidate|1803|()|var|float32
call_1801 = func_1800_call(var_1802,var_1803,)
output = call_1801
func_1804 = relay.Function([var_1802,var_1803,], output)
mutated_mod['func_1804'] = func_1804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1714_call = mod.get_global_var('func_1714')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_1806 = relay.TupleGetItem(func_1714_call(), 0)
call_1807 = relay.TupleGetItem(func_1715_call(), 0)
uop_1822 = relay.asin(call_1806.astype('float64')) # shape=(7, 6, 10)
uop_1824 = relay.asin(call_1807.astype('float64')) # shape=(7, 6, 10)
func_1800_call = mod.get_global_var('func_1800')
func_1804_call = mutated_mod.get_global_var('func_1804')
var_1828 = relay.var("var_1828", dtype = "float32", shape = ())#candidate|1828|()|var|float32
call_1827 = relay.TupleGetItem(func_1800_call(relay.reshape(call_1806.astype('float32'), [7, 6, 10]), relay.reshape(var_1828.astype('float32'), []), ), 1)
call_1829 = relay.TupleGetItem(func_1804_call(relay.reshape(call_1806.astype('float32'), [7, 6, 10]), relay.reshape(var_1828.astype('float32'), []), ), 1)
output = relay.Tuple([uop_1822,call_1827,var_1828,])
output2 = relay.Tuple([uop_1824,call_1829,var_1828,])
func_1833 = relay.Function([var_1828,], output)
mod['func_1833'] = func_1833
mod = relay.transform.InferType()(mod)
var_1834 = relay.var("var_1834", dtype = "float32", shape = ())#candidate|1834|()|var|float32
output = func_1833(var_1834)
func_1835 = relay.Function([var_1834], output)
mutated_mod['func_1835'] = func_1835
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1714_call = mod.get_global_var('func_1714')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_1866 = relay.TupleGetItem(func_1714_call(), 0)
call_1867 = relay.TupleGetItem(func_1715_call(), 0)
func_1050_call = mod.get_global_var('func_1050')
func_1053_call = mutated_mod.get_global_var('func_1053')
var_1869 = relay.var("var_1869", dtype = "uint16", shape = (180,))#candidate|1869|(180,)|var|uint16
call_1868 = relay.TupleGetItem(func_1050_call(relay.reshape(var_1869.astype('uint16'), [15, 4, 3]), relay.reshape(var_1869.astype('uint16'), [15, 4, 3]), ), 0)
call_1870 = relay.TupleGetItem(func_1053_call(relay.reshape(var_1869.astype('uint16'), [15, 4, 3]), relay.reshape(var_1869.astype('uint16'), [15, 4, 3]), ), 0)
func_1800_call = mod.get_global_var('func_1800')
func_1804_call = mutated_mod.get_global_var('func_1804')
var_1877 = relay.var("var_1877", dtype = "float32", shape = ())#candidate|1877|()|var|float32
call_1876 = relay.TupleGetItem(func_1800_call(relay.reshape(call_1866.astype('float32'), [7, 6, 10]), relay.reshape(var_1877.astype('float32'), []), ), 0)
call_1878 = relay.TupleGetItem(func_1804_call(relay.reshape(call_1866.astype('float32'), [7, 6, 10]), relay.reshape(var_1877.astype('float32'), []), ), 0)
output = relay.Tuple([call_1866,call_1868,var_1869,call_1876,var_1877,])
output2 = relay.Tuple([call_1867,call_1870,var_1869,call_1878,var_1877,])
func_1881 = relay.Function([var_1869,var_1877,], output)
mod['func_1881'] = func_1881
mod = relay.transform.InferType()(mod)
mutated_mod['func_1881'] = func_1881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1881_call = mutated_mod.get_global_var('func_1881')
var_1883 = relay.var("var_1883", dtype = "uint16", shape = (180,))#candidate|1883|(180,)|var|uint16
var_1884 = relay.var("var_1884", dtype = "float32", shape = ())#candidate|1884|()|var|float32
call_1882 = func_1881_call(var_1883,var_1884,)
output = call_1882
func_1885 = relay.Function([var_1883,var_1884,], output)
mutated_mod['func_1885'] = func_1885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1714_call = mod.get_global_var('func_1714')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_1937 = relay.TupleGetItem(func_1714_call(), 0)
call_1938 = relay.TupleGetItem(func_1715_call(), 0)
uop_1942 = relay.acosh(call_1937.astype('float64')) # shape=(7, 6, 10)
uop_1944 = relay.acosh(call_1938.astype('float64')) # shape=(7, 6, 10)
uop_1951 = relay.atan(uop_1942.astype('float64')) # shape=(7, 6, 10)
uop_1953 = relay.atan(uop_1944.astype('float64')) # shape=(7, 6, 10)
bop_1954 = relay.mod(uop_1951.astype('float64'), relay.reshape(uop_1942.astype('float64'), relay.shape_of(uop_1951))) # shape=(7, 6, 10)
bop_1957 = relay.mod(uop_1953.astype('float64'), relay.reshape(uop_1944.astype('float64'), relay.shape_of(uop_1953))) # shape=(7, 6, 10)
func_1050_call = mod.get_global_var('func_1050')
func_1053_call = mutated_mod.get_global_var('func_1053')
const_1983 = relay.const([[9,3,4,3,-6,-6,-3,-2,8,10,-6,-3,-7,-5,-10,-8,-2,6,-8,4,2,-5,-8,-6,10,4,-6,6,-5,4],[3,2,-4,3,-1,-5,9,-6,6,5,-1,4,6,-1,-1,6,-8,1,-1,3,1,3,-6,1,4,-10,7,-4,-1,5],[9,-8,-2,-8,-5,-2,-7,-8,-7,-6,7,8,7,-6,-7,4,2,5,-3,6,-6,-4,-7,-7,-3,7,-9,1,-7,6],[-10,1,2,-6,1,-3,-10,9,1,-4,-10,-4,6,-7,-4,8,-3,4,7,2,-1,6,-4,-1,-2,9,5,-1,9,-3],[-10,5,-10,-1,-2,-6,8,6,-8,6,3,-3,7,7,-1,8,-1,-5,5,-1,-8,10,10,9,5,9,-9,6,6,1],[-6,-9,2,-2,-9,-4,10,7,7,10,-9,10,9,3,9,-3,3,-4,5,1,-8,4,-8,8,5,9,-4,2,-5,1]], dtype = "uint16")#candidate|1983|(6, 30)|const|uint16
call_1982 = relay.TupleGetItem(func_1050_call(relay.reshape(const_1983.astype('uint16'), [15, 4, 3]), relay.reshape(const_1983.astype('uint16'), [15, 4, 3]), ), 0)
call_1984 = relay.TupleGetItem(func_1053_call(relay.reshape(const_1983.astype('uint16'), [15, 4, 3]), relay.reshape(const_1983.astype('uint16'), [15, 4, 3]), ), 0)
bop_1993 = relay.add(uop_1942.astype('int64'), relay.reshape(bop_1954.astype('int64'), relay.shape_of(uop_1942))) # shape=(7, 6, 10)
bop_1996 = relay.add(uop_1944.astype('int64'), relay.reshape(bop_1957.astype('int64'), relay.shape_of(uop_1944))) # shape=(7, 6, 10)
bop_2001 = relay.greater(bop_1993.astype('bool'), relay.reshape(bop_1954.astype('bool'), relay.shape_of(bop_1993))) # shape=(7, 6, 10)
bop_2004 = relay.greater(bop_1996.astype('bool'), relay.reshape(bop_1957.astype('bool'), relay.shape_of(bop_1996))) # shape=(7, 6, 10)
output = relay.Tuple([call_1982,const_1983,bop_2001,])
output2 = relay.Tuple([call_1984,const_1983,bop_2004,])
func_2006 = relay.Function([], output)
mod['func_2006'] = func_2006
mod = relay.transform.InferType()(mod)
mutated_mod['func_2006'] = func_2006
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2006_call = mutated_mod.get_global_var('func_2006')
call_2007 = func_2006_call()
output = call_2007
func_2008 = relay.Function([], output)
mutated_mod['func_2008'] = func_2008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2006_call = mod.get_global_var('func_2006')
func_2008_call = mutated_mod.get_global_var('func_2008')
call_2077 = relay.TupleGetItem(func_2006_call(), 0)
call_2078 = relay.TupleGetItem(func_2008_call(), 0)
output = relay.Tuple([call_2077,])
output2 = relay.Tuple([call_2078,])
func_2079 = relay.Function([], output)
mod['func_2079'] = func_2079
mod = relay.transform.InferType()(mod)
output = func_2079()
func_2080 = relay.Function([], output)
mutated_mod['func_2080'] = func_2080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2006_call = mod.get_global_var('func_2006')
func_2008_call = mutated_mod.get_global_var('func_2008')
call_2081 = relay.TupleGetItem(func_2006_call(), 1)
call_2082 = relay.TupleGetItem(func_2008_call(), 1)
var_2091 = relay.var("var_2091", dtype = "uint16", shape = (6, 30))#candidate|2091|(6, 30)|var|uint16
bop_2092 = relay.left_shift(call_2081.astype('uint64'), relay.reshape(var_2091.astype('uint64'), relay.shape_of(call_2081))) # shape=(6, 30)
bop_2095 = relay.left_shift(call_2082.astype('uint64'), relay.reshape(var_2091.astype('uint64'), relay.shape_of(call_2082))) # shape=(6, 30)
output = bop_2092
output2 = bop_2095
func_2096 = relay.Function([var_2091,], output)
mod['func_2096'] = func_2096
mod = relay.transform.InferType()(mod)
mutated_mod['func_2096'] = func_2096
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2097 = relay.var("var_2097", dtype = "uint16", shape = (6, 30))#candidate|2097|(6, 30)|var|uint16
func_2096_call = mutated_mod.get_global_var('func_2096')
call_2098 = func_2096_call(var_2097)
output = call_2098
func_2099 = relay.Function([var_2097], output)
mutated_mod['func_2099'] = func_2099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2006_call = mod.get_global_var('func_2006')
func_2008_call = mutated_mod.get_global_var('func_2008')
call_2193 = relay.TupleGetItem(func_2006_call(), 2)
call_2194 = relay.TupleGetItem(func_2008_call(), 2)
func_1714_call = mod.get_global_var('func_1714')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_2200 = relay.TupleGetItem(func_1714_call(), 0)
call_2201 = relay.TupleGetItem(func_1715_call(), 0)
func_2096_call = mod.get_global_var('func_2096')
func_2099_call = mutated_mod.get_global_var('func_2099')
var_2207 = relay.var("var_2207", dtype = "uint16", shape = (180,))#candidate|2207|(180,)|var|uint16
call_2206 = func_2096_call(relay.reshape(var_2207.astype('uint16'), [6, 30]))
call_2208 = func_2096_call(relay.reshape(var_2207.astype('uint16'), [6, 30]))
output = relay.Tuple([call_2193,call_2200,call_2206,var_2207,])
output2 = relay.Tuple([call_2194,call_2201,call_2208,var_2207,])
func_2210 = relay.Function([var_2207,], output)
mod['func_2210'] = func_2210
mod = relay.transform.InferType()(mod)
mutated_mod['func_2210'] = func_2210
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2211 = relay.var("var_2211", dtype = "uint16", shape = (180,))#candidate|2211|(180,)|var|uint16
func_2210_call = mutated_mod.get_global_var('func_2210')
call_2212 = func_2210_call(var_2211)
output = call_2212
func_2213 = relay.Function([var_2211], output)
mutated_mod['func_2213'] = func_2213
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1714_call = mod.get_global_var('func_1714')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_2250 = relay.TupleGetItem(func_1714_call(), 0)
call_2251 = relay.TupleGetItem(func_1715_call(), 0)
var_2255 = relay.var("var_2255", dtype = "float32", shape = (7, 6, 10))#candidate|2255|(7, 6, 10)|var|float32
bop_2256 = relay.subtract(call_2250.astype('float32'), relay.reshape(var_2255.astype('float32'), relay.shape_of(call_2250))) # shape=(7, 6, 10)
bop_2259 = relay.subtract(call_2251.astype('float32'), relay.reshape(var_2255.astype('float32'), relay.shape_of(call_2251))) # shape=(7, 6, 10)
bop_2260 = relay.less(var_2255.astype('bool'), relay.reshape(bop_2256.astype('bool'), relay.shape_of(var_2255))) # shape=(7, 6, 10)
bop_2263 = relay.less(var_2255.astype('bool'), relay.reshape(bop_2259.astype('bool'), relay.shape_of(var_2255))) # shape=(7, 6, 10)
output = relay.Tuple([bop_2260,])
output2 = relay.Tuple([bop_2263,])
func_2264 = relay.Function([var_2255,], output)
mod['func_2264'] = func_2264
mod = relay.transform.InferType()(mod)
mutated_mod['func_2264'] = func_2264
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2265 = relay.var("var_2265", dtype = "float32", shape = (7, 6, 10))#candidate|2265|(7, 6, 10)|var|float32
func_2264_call = mutated_mod.get_global_var('func_2264')
call_2266 = func_2264_call(var_2265)
output = call_2266
func_2267 = relay.Function([var_2265], output)
mutated_mod['func_2267'] = func_2267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1714_call = mod.get_global_var('func_1714')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_2310 = relay.TupleGetItem(func_1714_call(), 0)
call_2311 = relay.TupleGetItem(func_1715_call(), 0)
func_1881_call = mod.get_global_var('func_1881')
func_1885_call = mutated_mod.get_global_var('func_1885')
var_2318 = relay.var("var_2318", dtype = "uint16", shape = (180,))#candidate|2318|(180,)|var|uint16
var_2319 = relay.var("var_2319", dtype = "float32", shape = ())#candidate|2319|()|var|float32
call_2317 = relay.TupleGetItem(func_1881_call(relay.reshape(var_2318.astype('uint16'), [180,]), relay.reshape(var_2319.astype('float32'), []), ), 1)
call_2320 = relay.TupleGetItem(func_1885_call(relay.reshape(var_2318.astype('uint16'), [180,]), relay.reshape(var_2319.astype('float32'), []), ), 1)
func_1714_call = mod.get_global_var('func_1714')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_2325 = relay.TupleGetItem(func_1714_call(), 0)
call_2326 = relay.TupleGetItem(func_1715_call(), 0)
bop_2331 = relay.less(call_2317.astype('bool'), relay.reshape(var_2318.astype('bool'), relay.shape_of(call_2317))) # shape=(15, 4, 3)
bop_2334 = relay.less(call_2320.astype('bool'), relay.reshape(var_2318.astype('bool'), relay.shape_of(call_2320))) # shape=(15, 4, 3)
func_1107_call = mod.get_global_var('func_1107')
func_1109_call = mutated_mod.get_global_var('func_1109')
const_2342 = relay.const([-8.704733,4.912504,-7.704831,-2.314183,-5.624028,-6.723905,4.852313,-6.150304,-3.590448,-7.523944,-7.230549,3.310268,9.397993,0.829479,0.310011,5.765833,5.062591,-4.190343,1.121162,3.975519,6.212158,2.586818,5.136459,3.222929,-7.697947,-4.166270,-2.914877,-4.391250,1.292272,6.845191,-0.024243,-9.421210,8.437191,-4.672710,-0.731637,-5.366061,1.052819,-0.893255,2.936910,8.691698,-6.579164,1.611153,9.599720,-9.256735,1.436590,8.644855,-7.090957,9.481852,-9.569050,-9.058139,6.912117,0.048987,7.004588,-9.446028,3.944033,-9.531576,1.750447,1.585466,4.647606,7.670195,5.632369,2.082942,-9.610140,5.481091,-9.968315,0.704077,-8.529775,-9.483064,4.640133,9.295319,-7.236354,-0.887689,8.603510,-5.069428,9.754261,8.116409,-1.520733,-9.858687,-1.811668,-1.020418,-8.334388,-6.287280,-9.659964,-1.960492,0.124733,-5.543851,3.880597,2.515019,-5.387993,8.227503,3.874769,-8.359516,0.943018,9.412990,-6.314869,-3.682855,4.216450,-3.612695,-1.303873,9.975810,-6.537428,9.635426,-7.185154,-8.130821,2.064065,-1.233269,-8.905962,-4.307462,-1.681355,2.571860,7.867438,4.437370,6.199544,-4.109877,-8.426424,9.419847,-6.474488,-7.985281,-3.527682,3.615765,-9.676259,-0.381648,0.755213,2.853734,-1.418964,-5.019113,-1.205905,9.045662,0.382619,7.894354,0.288720,-5.288225,-1.096289,1.840499,1.003437,-4.853879,-5.469468,0.030857,1.558902,6.340233,2.242118,-9.876652,0.724721,1.040218,7.479181,-0.559967,-8.606871,-0.403733,8.239484,7.573195,8.149458,3.382702,-0.586408,2.112743,1.261270,-3.106640,-9.659752,-6.971597,-2.853616,9.817371], dtype = "float64")#candidate|2342|(160,)|const|float64
call_2341 = relay.TupleGetItem(func_1107_call(relay.reshape(const_2342.astype('float64'), [8, 2, 10])), 0)
call_2343 = relay.TupleGetItem(func_1109_call(relay.reshape(const_2342.astype('float64'), [8, 2, 10])), 0)
func_1881_call = mod.get_global_var('func_1881')
func_1885_call = mutated_mod.get_global_var('func_1885')
call_2355 = relay.TupleGetItem(func_1881_call(relay.reshape(bop_2331.astype('uint16'), [180,]), relay.reshape(var_2319.astype('float32'), []), ), 2)
call_2356 = relay.TupleGetItem(func_1885_call(relay.reshape(bop_2331.astype('uint16'), [180,]), relay.reshape(var_2319.astype('float32'), []), ), 2)
output = relay.Tuple([call_2310,var_2319,call_2325,bop_2331,call_2341,const_2342,call_2355,])
output2 = relay.Tuple([call_2311,var_2319,call_2326,bop_2334,call_2343,const_2342,call_2356,])
func_2357 = relay.Function([var_2318,var_2319,], output)
mod['func_2357'] = func_2357
mod = relay.transform.InferType()(mod)
var_2358 = relay.var("var_2358", dtype = "uint16", shape = (180,))#candidate|2358|(180,)|var|uint16
var_2359 = relay.var("var_2359", dtype = "float32", shape = ())#candidate|2359|()|var|float32
output = func_2357(var_2358,var_2359,)
func_2360 = relay.Function([var_2358,var_2359,], output)
mutated_mod['func_2360'] = func_2360
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2400 = relay.var("var_2400", dtype = "float32", shape = (7, 1, 4))#candidate|2400|(7, 1, 4)|var|float32
uop_2401 = relay.acos(var_2400.astype('float32')) # shape=(7, 1, 4)
bop_2406 = relay.maximum(uop_2401.astype('int64'), relay.reshape(var_2400.astype('int64'), relay.shape_of(uop_2401))) # shape=(7, 1, 4)
output = relay.Tuple([bop_2406,])
output2 = relay.Tuple([bop_2406,])
func_2422 = relay.Function([var_2400,], output)
mod['func_2422'] = func_2422
mod = relay.transform.InferType()(mod)
var_2423 = relay.var("var_2423", dtype = "float32", shape = (7, 1, 4))#candidate|2423|(7, 1, 4)|var|float32
output = func_2422(var_2423)
func_2424 = relay.Function([var_2423], output)
mutated_mod['func_2424'] = func_2424
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2006_call = mod.get_global_var('func_2006')
func_2008_call = mutated_mod.get_global_var('func_2008')
call_2461 = relay.TupleGetItem(func_2006_call(), 1)
call_2462 = relay.TupleGetItem(func_2008_call(), 1)
output = relay.Tuple([call_2461,])
output2 = relay.Tuple([call_2462,])
func_2476 = relay.Function([], output)
mod['func_2476'] = func_2476
mod = relay.transform.InferType()(mod)
output = func_2476()
func_2477 = relay.Function([], output)
mutated_mod['func_2477'] = func_2477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2476_call = mod.get_global_var('func_2476')
func_2477_call = mutated_mod.get_global_var('func_2477')
call_2541 = relay.TupleGetItem(func_2476_call(), 0)
call_2542 = relay.TupleGetItem(func_2477_call(), 0)
output = relay.Tuple([call_2541,])
output2 = relay.Tuple([call_2542,])
func_2543 = relay.Function([], output)
mod['func_2543'] = func_2543
mod = relay.transform.InferType()(mod)
output = func_2543()
func_2544 = relay.Function([], output)
mutated_mod['func_2544'] = func_2544
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2617 = relay.var("var_2617", dtype = "uint16", shape = (10, 13, 3))#candidate|2617|(10, 13, 3)|var|uint16
var_2618 = relay.var("var_2618", dtype = "uint16", shape = (10, 13, 3))#candidate|2618|(10, 13, 3)|var|uint16
bop_2619 = relay.bitwise_or(var_2617.astype('uint16'), relay.reshape(var_2618.astype('uint16'), relay.shape_of(var_2617))) # shape=(10, 13, 3)
uop_2629 = relay.atan(bop_2619.astype('float64')) # shape=(10, 13, 3)
output = relay.Tuple([uop_2629,])
output2 = relay.Tuple([uop_2629,])
func_2637 = relay.Function([var_2617,var_2618,], output)
mod['func_2637'] = func_2637
mod = relay.transform.InferType()(mod)
mutated_mod['func_2637'] = func_2637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2637_call = mutated_mod.get_global_var('func_2637')
var_2639 = relay.var("var_2639", dtype = "uint16", shape = (10, 13, 3))#candidate|2639|(10, 13, 3)|var|uint16
var_2640 = relay.var("var_2640", dtype = "uint16", shape = (10, 13, 3))#candidate|2640|(10, 13, 3)|var|uint16
call_2638 = func_2637_call(var_2639,var_2640,)
output = call_2638
func_2641 = relay.Function([var_2639,var_2640,], output)
mutated_mod['func_2641'] = func_2641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2543_call = mod.get_global_var('func_2543')
func_2544_call = mutated_mod.get_global_var('func_2544')
call_2643 = relay.TupleGetItem(func_2543_call(), 0)
call_2644 = relay.TupleGetItem(func_2544_call(), 0)
output = call_2643
output2 = call_2644
func_2651 = relay.Function([], output)
mod['func_2651'] = func_2651
mod = relay.transform.InferType()(mod)
mutated_mod['func_2651'] = func_2651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2651_call = mutated_mod.get_global_var('func_2651')
call_2652 = func_2651_call()
output = call_2652
func_2653 = relay.Function([], output)
mutated_mod['func_2653'] = func_2653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2543_call = mod.get_global_var('func_2543')
func_2544_call = mutated_mod.get_global_var('func_2544')
call_2744 = relay.TupleGetItem(func_2543_call(), 0)
call_2745 = relay.TupleGetItem(func_2544_call(), 0)
func_2006_call = mod.get_global_var('func_2006')
func_2008_call = mutated_mod.get_global_var('func_2008')
call_2760 = relay.TupleGetItem(func_2006_call(), 2)
call_2761 = relay.TupleGetItem(func_2008_call(), 2)
output = relay.Tuple([call_2744,call_2760,])
output2 = relay.Tuple([call_2745,call_2761,])
func_2773 = relay.Function([], output)
mod['func_2773'] = func_2773
mod = relay.transform.InferType()(mod)
output = func_2773()
func_2774 = relay.Function([], output)
mutated_mod['func_2774'] = func_2774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1714_call = mod.get_global_var('func_1714')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_2781 = relay.TupleGetItem(func_1714_call(), 0)
call_2782 = relay.TupleGetItem(func_1715_call(), 0)
uop_2786 = relay.atanh(call_2781.astype('float32')) # shape=(7, 6, 10)
uop_2788 = relay.atanh(call_2782.astype('float32')) # shape=(7, 6, 10)
func_1833_call = mod.get_global_var('func_1833')
func_1835_call = mutated_mod.get_global_var('func_1835')
var_2799 = relay.var("var_2799", dtype = "float32", shape = ())#candidate|2799|()|var|float32
call_2798 = relay.TupleGetItem(func_1833_call(relay.reshape(var_2799.astype('float32'), [])), 2)
call_2800 = relay.TupleGetItem(func_1835_call(relay.reshape(var_2799.astype('float32'), [])), 2)
output = relay.Tuple([uop_2786,call_2798,var_2799,])
output2 = relay.Tuple([uop_2788,call_2800,var_2799,])
func_2808 = relay.Function([var_2799,], output)
mod['func_2808'] = func_2808
mod = relay.transform.InferType()(mod)
var_2809 = relay.var("var_2809", dtype = "float32", shape = ())#candidate|2809|()|var|float32
output = func_2808(var_2809)
func_2810 = relay.Function([var_2809], output)
mutated_mod['func_2810'] = func_2810
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2821 = relay.var("var_2821", dtype = "float64", shape = (12, 1, 8))#candidate|2821|(12, 1, 8)|var|float64
uop_2822 = relay.sinh(var_2821.astype('float64')) # shape=(12, 1, 8)
output = relay.Tuple([uop_2822,])
output2 = relay.Tuple([uop_2822,])
func_2832 = relay.Function([var_2821,], output)
mod['func_2832'] = func_2832
mod = relay.transform.InferType()(mod)
mutated_mod['func_2832'] = func_2832
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2833 = relay.var("var_2833", dtype = "float64", shape = (12, 1, 8))#candidate|2833|(12, 1, 8)|var|float64
func_2832_call = mutated_mod.get_global_var('func_2832')
call_2834 = func_2832_call(var_2833)
output = call_2834
func_2835 = relay.Function([var_2833], output)
mutated_mod['func_2835'] = func_2835
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2543_call = mod.get_global_var('func_2543')
func_2544_call = mutated_mod.get_global_var('func_2544')
call_2842 = relay.TupleGetItem(func_2543_call(), 0)
call_2843 = relay.TupleGetItem(func_2544_call(), 0)
uop_2845 = relay.cosh(call_2842.astype('float64')) # shape=(6, 30)
uop_2847 = relay.cosh(call_2843.astype('float64')) # shape=(6, 30)
func_845_call = mod.get_global_var('func_845')
func_847_call = mutated_mod.get_global_var('func_847')
const_2849 = relay.const(-1.554670, dtype = "float32")#candidate|2849|()|const|float32
call_2848 = func_845_call(relay.reshape(const_2849.astype('float32'), []))
call_2850 = func_845_call(relay.reshape(const_2849.astype('float32'), []))
output = relay.Tuple([uop_2845,call_2848,const_2849,])
output2 = relay.Tuple([uop_2847,call_2850,const_2849,])
func_2852 = relay.Function([], output)
mod['func_2852'] = func_2852
mod = relay.transform.InferType()(mod)
output = func_2852()
func_2853 = relay.Function([], output)
mutated_mod['func_2853'] = func_2853
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1714_call = mod.get_global_var('func_1714')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_2858 = relay.TupleGetItem(func_1714_call(), 0)
call_2859 = relay.TupleGetItem(func_1715_call(), 0)
output = call_2858
output2 = call_2859
func_2866 = relay.Function([], output)
mod['func_2866'] = func_2866
mod = relay.transform.InferType()(mod)
output = func_2866()
func_2867 = relay.Function([], output)
mutated_mod['func_2867'] = func_2867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2651_call = mod.get_global_var('func_2651')
func_2653_call = mutated_mod.get_global_var('func_2653')
call_2904 = func_2651_call()
call_2905 = func_2651_call()
const_2908 = relay.const([[5,-5,-2,1,-7,2,9,-6,8,-2,6,3,-7,-1,-1,-4,-10,7,10,-7,9,6,-5,-3,-4,9,8,-5,6,9],[-2,-6,-4,8,1,4,-7,7,3,-8,-4,9,10,-6,-10,6,10,6,-4,-9,-2,-6,3,4,3,5,10,1,7,-10],[4,9,-9,7,1,-10,-9,3,-10,-2,-8,2,10,-10,3,-2,-6,-1,7,-10,-6,-3,-9,-10,5,1,6,1,-9,3],[-1,-10,-5,3,1,-2,8,-3,-4,-5,3,-2,1,7,6,-3,4,-5,-4,-2,-6,1,4,10,-5,8,-2,10,-6,5],[-6,9,10,8,-6,9,7,-5,-2,-10,9,8,8,7,5,-4,-10,9,-10,-4,-9,8,2,8,8,2,6,1,8,-6],[9,3,4,9,-1,8,-7,8,10,3,6,9,7,-3,-9,-7,-8,8,-2,-4,10,-5,-10,6,10,10,-5,5,-9,7]], dtype = "uint16")#candidate|2908|(6, 30)|const|uint16
bop_2909 = relay.right_shift(call_2904.astype('int32'), relay.reshape(const_2908.astype('int32'), relay.shape_of(call_2904))) # shape=(6, 30)
bop_2912 = relay.right_shift(call_2905.astype('int32'), relay.reshape(const_2908.astype('int32'), relay.shape_of(call_2905))) # shape=(6, 30)
bop_2914 = relay.logical_and(const_2908.astype('bool'), relay.reshape(call_2904.astype('bool'), relay.shape_of(const_2908))) # shape=(6, 30)
bop_2917 = relay.logical_and(const_2908.astype('bool'), relay.reshape(call_2905.astype('bool'), relay.shape_of(const_2908))) # shape=(6, 30)
output = relay.Tuple([bop_2909,bop_2914,])
output2 = relay.Tuple([bop_2912,bop_2917,])
func_2923 = relay.Function([], output)
mod['func_2923'] = func_2923
mod = relay.transform.InferType()(mod)
mutated_mod['func_2923'] = func_2923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2923_call = mutated_mod.get_global_var('func_2923')
call_2924 = func_2923_call()
output = call_2924
func_2925 = relay.Function([], output)
mutated_mod['func_2925'] = func_2925
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2773_call = mod.get_global_var('func_2773')
func_2774_call = mutated_mod.get_global_var('func_2774')
call_3028 = relay.TupleGetItem(func_2773_call(), 0)
call_3029 = relay.TupleGetItem(func_2774_call(), 0)
var_3044 = relay.var("var_3044", dtype = "uint16", shape = (6, 30))#candidate|3044|(6, 30)|var|uint16
bop_3045 = relay.floor_divide(call_3028.astype('float64'), relay.reshape(var_3044.astype('float64'), relay.shape_of(call_3028))) # shape=(6, 30)
bop_3048 = relay.floor_divide(call_3029.astype('float64'), relay.reshape(var_3044.astype('float64'), relay.shape_of(call_3029))) # shape=(6, 30)
output = bop_3045
output2 = bop_3048
func_3052 = relay.Function([var_3044,], output)
mod['func_3052'] = func_3052
mod = relay.transform.InferType()(mod)
var_3053 = relay.var("var_3053", dtype = "uint16", shape = (6, 30))#candidate|3053|(6, 30)|var|uint16
output = func_3052(var_3053)
func_3054 = relay.Function([var_3053], output)
mutated_mod['func_3054'] = func_3054
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3066 = relay.const([[[False,False,False,True,True,False,True,True,False,False,False,True,True,False]],[[False,False,False,True,False,True,False,False,True,False,True,False,True,False]],[[False,True,False,False,True,True,False,False,True,True,True,False,True,True]],[[True,False,True,True,True,False,True,True,True,True,True,False,True,False]],[[False,True,False,False,False,True,True,True,False,True,True,True,False,False]],[[True,False,True,True,False,True,False,True,True,True,True,False,True,False]],[[False,False,True,False,True,True,False,True,False,True,False,False,False,True]],[[False,True,True,True,True,True,False,True,False,True,True,True,False,False]],[[True,True,False,True,False,True,True,True,True,True,True,True,True,True]],[[False,True,True,False,False,False,True,True,True,False,True,True,True,False]]], dtype = "bool")#candidate|3066|(10, 1, 14)|const|bool
var_3067 = relay.var("var_3067", dtype = "bool", shape = (10, 9, 14))#candidate|3067|(10, 9, 14)|var|bool
bop_3068 = relay.logical_or(const_3066.astype('bool'), var_3067.astype('bool')) # shape=(10, 9, 14)
func_2543_call = mod.get_global_var('func_2543')
func_2544_call = mutated_mod.get_global_var('func_2544')
call_3082 = relay.TupleGetItem(func_2543_call(), 0)
call_3083 = relay.TupleGetItem(func_2544_call(), 0)
func_1050_call = mod.get_global_var('func_1050')
func_1053_call = mutated_mod.get_global_var('func_1053')
call_3098 = relay.TupleGetItem(func_1050_call(relay.reshape(call_3082.astype('uint16'), [15, 4, 3]), relay.reshape(call_3082.astype('uint16'), [15, 4, 3]), ), 1)
call_3099 = relay.TupleGetItem(func_1053_call(relay.reshape(call_3082.astype('uint16'), [15, 4, 3]), relay.reshape(call_3082.astype('uint16'), [15, 4, 3]), ), 1)
output = relay.Tuple([bop_3068,call_3082,call_3098,])
output2 = relay.Tuple([bop_3068,call_3083,call_3099,])
func_3111 = relay.Function([var_3067,], output)
mod['func_3111'] = func_3111
mod = relay.transform.InferType()(mod)
var_3112 = relay.var("var_3112", dtype = "bool", shape = (10, 9, 14))#candidate|3112|(10, 9, 14)|var|bool
output = func_3111(var_3112)
func_3113 = relay.Function([var_3112], output)
mutated_mod['func_3113'] = func_3113
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1714_call = mod.get_global_var('func_1714')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_3159 = relay.TupleGetItem(func_1714_call(), 0)
call_3160 = relay.TupleGetItem(func_1715_call(), 0)
func_2006_call = mod.get_global_var('func_2006')
func_2008_call = mutated_mod.get_global_var('func_2008')
call_3182 = relay.TupleGetItem(func_2006_call(), 2)
call_3183 = relay.TupleGetItem(func_2008_call(), 2)
var_3187 = relay.var("var_3187", dtype = "float32", shape = (7, 6, 10))#candidate|3187|(7, 6, 10)|var|float32
bop_3188 = relay.less_equal(call_3159.astype('bool'), relay.reshape(var_3187.astype('bool'), relay.shape_of(call_3159))) # shape=(7, 6, 10)
bop_3191 = relay.less_equal(call_3160.astype('bool'), relay.reshape(var_3187.astype('bool'), relay.shape_of(call_3160))) # shape=(7, 6, 10)
output = relay.Tuple([call_3182,bop_3188,])
output2 = relay.Tuple([call_3183,bop_3191,])
func_3195 = relay.Function([var_3187,], output)
mod['func_3195'] = func_3195
mod = relay.transform.InferType()(mod)
mutated_mod['func_3195'] = func_3195
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3196 = relay.var("var_3196", dtype = "float32", shape = (7, 6, 10))#candidate|3196|(7, 6, 10)|var|float32
func_3195_call = mutated_mod.get_global_var('func_3195')
call_3197 = func_3195_call(var_3196)
output = call_3197
func_3198 = relay.Function([var_3196], output)
mutated_mod['func_3198'] = func_3198
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3231 = relay.var("var_3231", dtype = "int16", shape = (10, 1, 15))#candidate|3231|(10, 1, 15)|var|int16
const_3232 = relay.const([[[-2,-10,10,-1,-5,10,-1,-7,-5,-4,2,-7,-2,-6,9],[-7,-5,-4,-10,1,-9,9,-5,8,1,-2,-9,-2,7,-5],[8,-5,-6,-9,5,4,-2,5,-9,9,6,-5,-2,7,-6],[6,-2,-8,-2,-7,-8,-3,1,-8,-3,-10,-2,-4,-3,6],[1,3,4,2,-10,-5,9,9,-5,10,-5,5,-7,-4,9],[-2,-1,-6,8,-3,8,-7,3,8,-2,-4,-1,6,9,2]],[[9,2,9,-7,7,-7,7,1,9,-7,-8,-10,1,10,-8],[-2,6,-1,2,-4,-7,4,-5,3,4,7,-3,2,-4,6],[5,-1,3,-6,9,4,10,-9,2,-1,9,8,-4,6,5],[2,-3,10,4,-1,-5,8,-4,10,-6,-2,-8,9,-3,2],[10,-9,-6,8,-5,4,5,-3,8,7,-6,-2,-1,8,7],[-3,3,-1,1,10,8,3,-7,-4,-4,10,-2,-4,-5,-9]],[[2,1,-6,-6,-2,2,-2,5,5,-6,-2,9,-1,7,3],[10,1,-3,-6,3,-7,9,-4,-1,-8,8,-5,4,-7,-6],[8,-10,-9,-6,-1,-4,6,10,-2,8,9,-9,-10,4,5],[-2,6,-2,2,-2,8,3,-3,-5,3,-4,9,1,-6,9],[-3,-4,2,5,-5,8,7,9,-4,5,-8,-4,-2,-6,-7],[2,7,-2,4,-6,-6,-2,6,5,4,9,-8,-8,-7,-1]],[[-1,-6,-8,1,6,1,-2,9,4,7,-3,-1,1,-5,6],[-1,-8,-7,-5,-8,-6,7,2,5,9,4,-10,6,6,8],[-7,9,7,-4,6,7,1,-7,9,8,4,1,1,-5,-9],[7,1,-3,-3,3,7,9,-4,-2,10,1,6,-8,-9,3],[6,-6,-5,-5,4,-8,-8,2,5,2,-5,-9,-7,7,-10],[6,10,2,10,6,5,-8,10,2,-1,-1,9,7,-9,-2]],[[7,-6,1,-4,5,-7,-3,1,3,1,8,-2,5,3,-8],[-2,6,-1,6,-9,5,-1,-1,4,-6,9,10,-2,-5,-9],[-3,-5,1,-5,-1,-7,-10,-7,-1,-6,9,-2,1,3,1],[6,-5,5,6,2,-4,-6,-9,9,3,10,3,10,-6,-9],[-5,2,-5,-5,-7,-10,7,-9,-8,-10,-4,-10,2,2,-3],[6,-5,7,7,2,-10,-9,10,-5,6,9,6,8,1,6]],[[8,-1,4,2,-1,-7,9,-8,-4,7,-10,8,6,-4,6],[1,3,7,-2,-9,5,6,2,3,8,-5,-4,4,9,-7],[7,-8,-9,-8,-6,-6,4,5,5,-3,-7,3,1,1,5],[-4,-5,-5,-9,-5,-1,-8,-4,-3,10,-4,-2,8,4,3],[1,-2,-4,-1,9,10,9,-6,-10,2,3,-8,-2,-8,10],[-8,3,-7,8,-9,-4,-8,8,7,-3,1,6,-2,-8,7]],[[-4,-8,6,3,3,-2,5,-1,-5,3,7,3,5,-2,-6],[10,-5,-8,-4,-4,4,-6,-5,2,-5,-8,-8,6,6,6],[-8,-3,-7,-1,-1,9,-10,-4,2,-6,10,-9,-7,-2,4],[7,8,-2,-1,7,-7,-9,1,-5,9,10,-7,8,4,9],[9,10,5,2,5,2,-6,-3,4,10,9,-3,-8,2,-10],[-2,6,8,-1,9,-2,2,-2,8,10,1,9,8,4,1]],[[-1,-7,-4,8,7,-3,-8,10,-9,10,-6,9,-7,-3,6],[-7,9,-2,10,8,7,8,-8,7,-7,-7,10,-10,-2,9],[9,7,-1,10,-8,9,-4,3,5,9,9,-7,-1,-5,2],[-3,10,-10,8,4,-10,3,10,-6,-8,-9,1,5,2,7],[1,-6,9,-6,8,4,3,-2,7,-7,6,-1,1,9,3],[-1,5,9,-3,-10,5,9,-3,-10,-2,5,-3,3,2,1]],[[-7,2,-10,-5,-6,-4,-10,6,5,-4,-2,-2,-5,1,8],[-3,-4,8,-5,-9,-1,1,-5,5,-4,-6,9,-3,5,-4],[-8,10,5,10,-5,3,9,5,3,-5,-2,5,-8,-8,4],[8,2,-8,7,6,-4,-8,-5,8,-5,-6,3,-8,2,6],[9,-2,3,7,7,-4,4,-5,-4,-6,-7,8,8,2,4],[-7,-1,6,-8,-6,6,-5,9,-9,4,-6,2,10,-1,-9]],[[10,8,7,-7,-6,-10,-10,-3,7,-6,9,-2,5,10,-2],[-1,-9,6,-4,2,4,2,-9,5,-9,6,2,-1,-8,4],[-4,-4,5,-10,1,-9,-4,-8,-8,-8,3,-6,-4,3,10],[3,4,8,7,10,-7,-4,-2,3,-7,-6,7,-5,-1,-2],[-8,6,2,1,1,9,10,1,6,-1,-7,3,-9,4,9],[-10,10,-6,1,4,-1,-1,8,5,6,-7,3,6,8,-1]]], dtype = "int16")#candidate|3232|(10, 6, 15)|const|int16
bop_3233 = relay.right_shift(var_3231.astype('int16'), const_3232.astype('int16')) # shape=(10, 6, 15)
output = relay.Tuple([bop_3233,])
output2 = relay.Tuple([bop_3233,])
func_3246 = relay.Function([var_3231,], output)
mod['func_3246'] = func_3246
mod = relay.transform.InferType()(mod)
mutated_mod['func_3246'] = func_3246
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3247 = relay.var("var_3247", dtype = "int16", shape = (10, 1, 15))#candidate|3247|(10, 1, 15)|var|int16
func_3246_call = mutated_mod.get_global_var('func_3246')
call_3248 = func_3246_call(var_3247)
output = call_3248
func_3249 = relay.Function([var_3247], output)
mutated_mod['func_3249'] = func_3249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2006_call = mod.get_global_var('func_2006')
func_2008_call = mutated_mod.get_global_var('func_2008')
call_3281 = relay.TupleGetItem(func_2006_call(), 0)
call_3282 = relay.TupleGetItem(func_2008_call(), 0)
uop_3298 = relay.tan(call_3281.astype('float32')) # shape=(15, 4, 3)
uop_3300 = relay.tan(call_3282.astype('float32')) # shape=(15, 4, 3)
func_1881_call = mod.get_global_var('func_1881')
func_1885_call = mutated_mod.get_global_var('func_1885')
const_3321 = relay.const(1.527519, dtype = "float32")#candidate|3321|()|const|float32
call_3320 = relay.TupleGetItem(func_1881_call(relay.reshape(uop_3298.astype('uint16'), [180,]), relay.reshape(const_3321.astype('float32'), []), ), 2)
call_3322 = relay.TupleGetItem(func_1885_call(relay.reshape(uop_3298.astype('uint16'), [180,]), relay.reshape(const_3321.astype('float32'), []), ), 2)
func_1330_call = mod.get_global_var('func_1330')
func_1332_call = mutated_mod.get_global_var('func_1332')
const_3330 = relay.const([-2,10,-7,-3,-4,-9], dtype = "int32")#candidate|3330|(6,)|const|int32
call_3329 = func_1330_call(relay.reshape(const_3330.astype('int32'), [3, 1, 2]))
call_3331 = func_1330_call(relay.reshape(const_3330.astype('int32'), [3, 1, 2]))
func_893_call = mod.get_global_var('func_893')
func_895_call = mutated_mod.get_global_var('func_895')
const_3333 = relay.const([-8.753614,1.004173,1.766789,6.863900,-0.126822,-8.363404,4.978971,-7.456352,-3.715690,-9.527193,6.398216,-0.325311,-3.937170,3.261079,-2.464322,6.430877,1.526868,-3.264707,2.786734,7.173245,8.330336,1.150586,7.693081,-4.937276,-9.775090,8.797557,9.603079,-2.001478,-9.288989,-8.028771,5.884897,1.134948,-0.174282,6.703185,9.546436,8.235322,2.666858,-7.177208,3.636341,-0.998161,0.437437,4.539956,6.813933,-1.356123,-7.636544,-4.410846,-4.533818,-3.746396,3.161837,-5.258850,-1.343729,4.865107,-4.811762,-1.276604,8.011105,1.570400,-6.926185,3.498081,7.967542,1.685104,-9.115619,3.919661,-7.619971,5.704170,1.892731,-2.900530,-1.644339,0.552929,9.467278,-1.572622,-0.244256,-4.277332,-9.843000,-3.538674,7.926809,5.863386,-5.390956,8.665162,-1.374345,-0.822361,-2.860772,-3.965865,0.727814,-2.838527,2.473549,6.265578,-6.376799,6.444075,4.066283,-9.382077,1.646449,3.676763,-2.847408,-7.203093,3.192959,9.823129,-6.468308,-5.258845,4.046696,-7.171697,4.962434,1.391273,4.606856,0.706282,-1.390218,-3.378034,8.264744,8.775850,-3.186422,9.008315,5.413553,1.857189,-7.801209,0.457233,-8.018879,-8.618885,7.311087,-1.596517,-8.548913,9.690135,8.994001,2.474860,3.809849,6.827861,-8.312542,-2.678767], dtype = "float64")#candidate|3333|(126,)|const|float64
call_3332 = func_893_call(relay.reshape(const_3333.astype('float64'), [3, 6, 7]))
call_3334 = func_893_call(relay.reshape(const_3333.astype('float64'), [3, 6, 7]))
bop_3335 = relay.maximum(uop_3298.astype('int16'), relay.reshape(call_3320.astype('int16'), relay.shape_of(uop_3298))) # shape=(15, 4, 3)
bop_3338 = relay.maximum(uop_3300.astype('int16'), relay.reshape(call_3322.astype('int16'), relay.shape_of(uop_3300))) # shape=(15, 4, 3)
output = relay.Tuple([const_3321,call_3329,const_3330,call_3332,const_3333,bop_3335,])
output2 = relay.Tuple([const_3321,call_3331,const_3330,call_3334,const_3333,bop_3338,])
func_3340 = relay.Function([], output)
mod['func_3340'] = func_3340
mod = relay.transform.InferType()(mod)
mutated_mod['func_3340'] = func_3340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3340_call = mutated_mod.get_global_var('func_3340')
call_3341 = func_3340_call()
output = call_3341
func_3342 = relay.Function([], output)
mutated_mod['func_3342'] = func_3342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2866_call = mod.get_global_var('func_2866')
func_2867_call = mutated_mod.get_global_var('func_2867')
call_3376 = func_2866_call()
call_3377 = func_2866_call()
func_3195_call = mod.get_global_var('func_3195')
func_3198_call = mutated_mod.get_global_var('func_3198')
call_3386 = relay.TupleGetItem(func_3195_call(relay.reshape(call_3376.astype('float32'), [7, 6, 10])), 1)
call_3387 = relay.TupleGetItem(func_3198_call(relay.reshape(call_3376.astype('float32'), [7, 6, 10])), 1)
func_3340_call = mod.get_global_var('func_3340')
func_3342_call = mutated_mod.get_global_var('func_3342')
call_3409 = relay.TupleGetItem(func_3340_call(), 5)
call_3410 = relay.TupleGetItem(func_3342_call(), 5)
func_1050_call = mod.get_global_var('func_1050')
func_1053_call = mutated_mod.get_global_var('func_1053')
call_3428 = relay.TupleGetItem(func_1050_call(relay.reshape(call_3409.astype('uint16'), [15, 4, 3]), relay.reshape(call_3409.astype('uint16'), [15, 4, 3]), ), 1)
call_3429 = relay.TupleGetItem(func_1053_call(relay.reshape(call_3409.astype('uint16'), [15, 4, 3]), relay.reshape(call_3409.astype('uint16'), [15, 4, 3]), ), 1)
func_2637_call = mod.get_global_var('func_2637')
func_2641_call = mutated_mod.get_global_var('func_2641')
const_3433 = relay.const([7,-2,-10,-5,1,-9,-2,6,1,-4,7,-6,1,6,9,-3,-5,3,9,-4,1,-7,-2,-5,-2,3,-6,-4,-9,2,-2,-6,9,-4,-7,-1,2,1,9,-8,-6,2,-1,9,-9,-10,6,-9,5,-3,10,1,2,-7,-10,3,7,8,-4,-8,7,-5,3,-8,-7,-9,7,-10,-3,-1,3,9,-1,-8,7,7,3,9,-6,-4,-9,10,4,6,-9,10,-1,2,7,9,7,8,-8,5,3,6,4,-8,6,-6,1,6,5,5,9,6,2,7,-2,-5,-4,8,7,-4,2,-7,-6,-6,-3,2,7,-2,-5,-8,-1,-3,3,1,-7,-4,-7,-9,-6,-3,-8,-2,7,1,-3,9,3,9,3,-6,8,-9,-1,-7,5,-5,-7,5,3,5,8,-1,8,-5,-3,1,-2,-6,1,9,5,7,3,5,-2,1,6,9,4,-7,8,8,-10,-3,10,-7,6,-9,7,-4,-8,-9,8,10,-5,-9,-7,-10,-1,-8,-3,-10,-8,-7,-6,-6,-7,-9,-4,-7,6,-9,-2,1,-2,-6,5,-5,6,-10,4,-5,10,3,4,2,-5,4,1,-3,-6,1,7,-4,7,-5,1,-1,-5,6,6,9,2,9,1,-8,10,-8,-5,-10,-8,5,-7,2,-1,-9,-10,-8,-4,-6,8,-9,5,-7,-2,5,4,-3,6,-10,6,6,10,6,1,-8,-10,-9,-6,5,3,-10,-10,7,10,5,-1,-10,4,-4,2,4,-8,-6,9,-4,1,-1,-9,-9,8,-3,-4,1,-2,1,-6,5,9,-10,-3,3,8,-7,6,6,-9,-4,-3,-10,-9,-9,7,-1,-5,7,7,2,-7,4,4,-7,8,-5,-6,8,-8,-10,-10,3,4,-3,-1,-6,-3,-2,-10,-9,10,-3,-3,-2,7,7,-3,-5,4,7,5,6,6,7,6,-6,4,-5,-2,7,6,-7,6,-5,-1,6,8,4,-9,-9,8,3,7,-6,-4,-8,-9,-1,-8,5,-1,-5,-4,-2,-1,10,-8,-1], dtype = "uint16")#candidate|3433|(390,)|const|uint16
call_3432 = relay.TupleGetItem(func_2637_call(relay.reshape(const_3433.astype('uint16'), [10, 13, 3]), relay.reshape(const_3433.astype('uint16'), [10, 13, 3]), ), 0)
call_3434 = relay.TupleGetItem(func_2641_call(relay.reshape(const_3433.astype('uint16'), [10, 13, 3]), relay.reshape(const_3433.astype('uint16'), [10, 13, 3]), ), 0)
output = relay.Tuple([call_3376,call_3386,call_3409,call_3428,call_3432,const_3433,])
output2 = relay.Tuple([call_3377,call_3387,call_3410,call_3429,call_3434,const_3433,])
func_3435 = relay.Function([], output)
mod['func_3435'] = func_3435
mod = relay.transform.InferType()(mod)
output = func_3435()
func_3436 = relay.Function([], output)
mutated_mod['func_3436'] = func_3436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2852_call = mod.get_global_var('func_2852')
func_2853_call = mutated_mod.get_global_var('func_2853')
call_3511 = relay.TupleGetItem(func_2852_call(), 0)
call_3512 = relay.TupleGetItem(func_2853_call(), 0)
output = call_3511
output2 = call_3512
func_3530 = relay.Function([], output)
mod['func_3530'] = func_3530
mod = relay.transform.InferType()(mod)
output = func_3530()
func_3531 = relay.Function([], output)
mutated_mod['func_3531'] = func_3531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3435_call = mod.get_global_var('func_3435')
func_3436_call = mutated_mod.get_global_var('func_3436')
call_3542 = relay.TupleGetItem(func_3435_call(), 3)
call_3543 = relay.TupleGetItem(func_3436_call(), 3)
func_2476_call = mod.get_global_var('func_2476')
func_2477_call = mutated_mod.get_global_var('func_2477')
call_3546 = relay.TupleGetItem(func_2476_call(), 0)
call_3547 = relay.TupleGetItem(func_2477_call(), 0)
output = relay.Tuple([call_3542,call_3546,])
output2 = relay.Tuple([call_3543,call_3547,])
func_3554 = relay.Function([], output)
mod['func_3554'] = func_3554
mod = relay.transform.InferType()(mod)
mutated_mod['func_3554'] = func_3554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3554_call = mutated_mod.get_global_var('func_3554')
call_3555 = func_3554_call()
output = call_3555
func_3556 = relay.Function([], output)
mutated_mod['func_3556'] = func_3556
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3560 = relay.var("var_3560", dtype = "int32", shape = (11, 16, 16))#candidate|3560|(11, 16, 16)|var|int32
var_3561 = relay.var("var_3561", dtype = "int32", shape = (11, 16, 16))#candidate|3561|(11, 16, 16)|var|int32
bop_3562 = relay.left_shift(var_3560.astype('int32'), relay.reshape(var_3561.astype('int32'), relay.shape_of(var_3560))) # shape=(11, 16, 16)
func_3340_call = mod.get_global_var('func_3340')
func_3342_call = mutated_mod.get_global_var('func_3342')
call_3569 = relay.TupleGetItem(func_3340_call(), 3)
call_3570 = relay.TupleGetItem(func_3342_call(), 3)
output = relay.Tuple([bop_3562,call_3569,])
output2 = relay.Tuple([bop_3562,call_3570,])
func_3571 = relay.Function([var_3560,var_3561,], output)
mod['func_3571'] = func_3571
mod = relay.transform.InferType()(mod)
mutated_mod['func_3571'] = func_3571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3571_call = mutated_mod.get_global_var('func_3571')
var_3573 = relay.var("var_3573", dtype = "int32", shape = (11, 16, 16))#candidate|3573|(11, 16, 16)|var|int32
var_3574 = relay.var("var_3574", dtype = "int32", shape = (11, 16, 16))#candidate|3574|(11, 16, 16)|var|int32
call_3572 = func_3571_call(var_3573,var_3574,)
output = call_3572
func_3575 = relay.Function([var_3573,var_3574,], output)
mutated_mod['func_3575'] = func_3575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2651_call = mod.get_global_var('func_2651')
func_2653_call = mutated_mod.get_global_var('func_2653')
call_3617 = func_2651_call()
call_3618 = func_2651_call()
func_2096_call = mod.get_global_var('func_2096')
func_2099_call = mutated_mod.get_global_var('func_2099')
call_3620 = func_2096_call(relay.reshape(call_3617.astype('uint16'), [6, 30]))
call_3621 = func_2096_call(relay.reshape(call_3617.astype('uint16'), [6, 30]))
var_3631 = relay.var("var_3631", dtype = "uint16", shape = (6, 30))#candidate|3631|(6, 30)|var|uint16
bop_3632 = relay.multiply(call_3617.astype('uint32'), relay.reshape(var_3631.astype('uint32'), relay.shape_of(call_3617))) # shape=(6, 30)
bop_3635 = relay.multiply(call_3618.astype('uint32'), relay.reshape(var_3631.astype('uint32'), relay.shape_of(call_3618))) # shape=(6, 30)
uop_3640 = relay.sin(bop_3632.astype('float32')) # shape=(6, 30)
uop_3642 = relay.sin(bop_3635.astype('float32')) # shape=(6, 30)
func_1800_call = mod.get_global_var('func_1800')
func_1804_call = mutated_mod.get_global_var('func_1804')
const_3646 = relay.const([7.354623,-4.234219,-8.756030,-8.777557,-7.068062,7.520463,-9.447850,3.831357,0.048372,-9.792692,3.960709,-3.508239,7.909331,5.094290,9.107517,7.059207,2.904758,2.562019,0.651861,5.693083,-5.162741,-1.298057,5.670376,-4.064600,-6.614900,-8.558855,0.879241,0.488864,1.999036,7.291221,3.098406,-7.548792,-7.090873,-6.499596,1.605354,5.498061,-0.942159,-5.527193,-8.128684,-1.583746,6.485789,-9.553889,-7.039350,-4.691279,-4.272929,-6.288393,-4.731813,-7.620293,-9.929083,-4.966953,-5.966332,-0.920906,0.466134,8.583086,8.723474,-5.421325,-2.886331,8.261235,-1.460175,-7.935434,6.852603,-3.055186,3.685653,-1.357902,4.782713,-1.300377,-0.783525,-8.731699,2.817796,3.922755,-1.779200,-1.261980,-4.768628,9.668759,1.685274,4.825013,-3.958729,-6.779696,-0.437041,4.036610,5.204799,-5.585623,-4.900298,1.483474,-3.101243,-4.498868,1.098689,9.694185,-1.134740,-3.069832,-8.361621,-3.371030,-1.273803,3.115730,2.796177,-1.145841,-4.402213,4.503970,-4.913901,-5.157554,9.901082,4.641990,7.736690,5.126812,1.870018,0.540696,8.490071,-9.498673,-5.387485,0.290599,-8.394152,-7.154976,-4.514375,-3.186412,1.670521,6.035906,8.035004,1.204276,4.621834,2.889675,-1.859869,-6.991380,-3.751972,9.766729,-8.238537,1.713907,7.545105,8.051634,5.681328,-2.352711,9.835642,0.197508,-4.289586,1.944156,7.868805,-8.692244,-8.736910,-7.912964,2.160655,6.184299,-3.973651,-1.027315,1.999868,7.206491,7.704680,6.468090,2.672779,-3.908832,7.338699,1.802173,-7.565520,-2.296791,-5.405501,1.000452,9.743948,-3.069721,0.625753,1.484155,-0.523755,6.639380,-9.129911,-9.066794,-0.382156,4.200042,4.145687,-6.130446,-2.227632,-1.615505,8.610922,-6.087991,-6.836422,-5.271181,5.808525,-3.240622,-1.784443,-1.700125,-8.427953,-6.978374,7.328327,-4.314654,-0.763548,-4.453676,-9.667167,-7.282324,-3.196278,-2.738428,9.173448,8.681798,-3.990790,-5.068820,7.093858,0.205003,-7.951469,-3.510754,0.088267,-2.193918,-7.153015,-2.374944,6.666095,-1.304686,9.366665,-4.720746,-7.784935,9.478403,-4.831215,8.362564,-0.312000,6.609818,0.815328,-4.843879,0.984850,-3.386311,6.403499,-2.893325,8.080698,0.925847,7.216440,1.670684,3.238025,-3.016992,4.967106,0.124420,-7.807664,-8.911182,2.531067,-2.678143,6.446413,-9.836934,7.516705,1.981952,1.884956,3.869828,-0.613177,-9.854646,4.210968,4.849801,8.841425,4.078133,-3.365930,1.026413,-0.854682,-6.018808,-0.117558,9.426149,1.046404,1.399630,9.385611,3.613084,5.953185,2.990703,-3.750492,3.693606,8.986167,2.569346,-9.464057,0.337270,-6.602672,-8.059147,-4.231710,-7.143559,-7.515836,4.830863,-5.154087,-2.709256,-7.858325,-4.671439,-2.434443,-9.405979,-6.606886,1.779205,-3.502550,-6.435010,-9.591765,-0.449049,-8.916300,-8.208875,-2.284840,-8.611519,-7.586416,-0.399792,-2.142037,2.612604,9.717375,-7.449656,4.222721,-0.016293,0.249133,-8.973247,-3.782133,-2.407657,4.785317,7.848197,-3.934176,-4.840159,-6.091374,-9.747240,-3.561243,-8.689035,6.941366,7.511846,-5.347109,3.326999,-0.855021,-6.213333,-7.908782,4.747283,7.496285,8.199939,-0.467420,7.451627,-3.177393,8.886748,2.996432,-9.968476,9.868629,-1.646727,-8.225968,7.390673,5.915511,2.055657,-4.969300,-0.083198,8.398302,-4.894310,9.045844,9.671778,4.790385,-2.451117,-4.300404,5.939508,0.953458,9.882110,9.120091,-5.084317,-2.175931,-2.332144,5.008701,9.094736,-1.176053,-9.360991,0.071841,-8.935502,3.896112,1.465512,4.246480,1.276506,-8.097081,-4.957723,3.795519,8.398545,-9.858127,-2.330533,-1.734618,1.693501,9.846745,-3.733483,7.531408,0.147542,-1.533250,-5.436991,-3.081685,-5.369255,-5.856721,-2.450767,9.940319,-6.165844,-2.774986,8.724875,-0.374727,4.634793,4.787342,-4.196809,-2.410484,1.981251,-0.207176,2.994123,1.732302,-3.382412,-1.106979,1.067373,-0.747160,-7.023662,-2.307978,4.745721,-6.273928,0.165979,-4.023172,-0.377041,4.904543,0.620728,0.836394,-3.267654,-9.622532,-7.718425,-4.678778,6.489164,1.568479,4.819462,5.826357,-8.506792,6.302924,7.411738,9.241396,1.439348,8.902869,5.715267,5.264204,5.071146,-7.222486,-1.368892,7.715923,3.971827,6.357242,2.908354,3.366451,-6.456926,0.752975,-8.280150,2.415379,3.028185], dtype = "float32")#candidate|3646|(420,)|const|float32
const_3647 = relay.const(9.073857, dtype = "float32")#candidate|3647|()|const|float32
call_3645 = relay.TupleGetItem(func_1800_call(relay.reshape(const_3646.astype('float32'), [7, 6, 10]), relay.reshape(const_3647.astype('float32'), []), ), 2)
call_3648 = relay.TupleGetItem(func_1804_call(relay.reshape(const_3646.astype('float32'), [7, 6, 10]), relay.reshape(const_3647.astype('float32'), []), ), 2)
uop_3654 = relay.sqrt(uop_3640.astype('float32')) # shape=(6, 30)
uop_3656 = relay.sqrt(uop_3642.astype('float32')) # shape=(6, 30)
uop_3658 = relay.rsqrt(var_3631.astype('float64')) # shape=(6, 30)
bop_3661 = relay.minimum(uop_3658.astype('int32'), relay.reshape(var_3631.astype('int32'), relay.shape_of(uop_3658))) # shape=(6, 30)
func_1881_call = mod.get_global_var('func_1881')
func_1885_call = mutated_mod.get_global_var('func_1885')
call_3674 = relay.TupleGetItem(func_1881_call(relay.reshape(uop_3654.astype('uint16'), [180,]), relay.reshape(const_3647.astype('float32'), []), ), 1)
call_3675 = relay.TupleGetItem(func_1885_call(relay.reshape(uop_3654.astype('uint16'), [180,]), relay.reshape(const_3647.astype('float32'), []), ), 1)
bop_3678 = relay.floor_mod(uop_3640.astype('float32'), relay.reshape(bop_3632.astype('float32'), relay.shape_of(uop_3640))) # shape=(6, 30)
bop_3681 = relay.floor_mod(uop_3642.astype('float32'), relay.reshape(bop_3635.astype('float32'), relay.shape_of(uop_3642))) # shape=(6, 30)
output = relay.Tuple([call_3620,call_3645,const_3646,const_3647,uop_3654,bop_3661,call_3674,bop_3678,])
output2 = relay.Tuple([call_3621,call_3648,const_3646,const_3647,uop_3656,bop_3661,call_3675,bop_3681,])
func_3693 = relay.Function([var_3631,], output)
mod['func_3693'] = func_3693
mod = relay.transform.InferType()(mod)
mutated_mod['func_3693'] = func_3693
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3694 = relay.var("var_3694", dtype = "uint16", shape = (6, 30))#candidate|3694|(6, 30)|var|uint16
func_3693_call = mutated_mod.get_global_var('func_3693')
call_3695 = func_3693_call(var_3694)
output = call_3695
func_3696 = relay.Function([var_3694], output)
mutated_mod['func_3696'] = func_3696
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2476_call = mod.get_global_var('func_2476')
func_2477_call = mutated_mod.get_global_var('func_2477')
call_3729 = relay.TupleGetItem(func_2476_call(), 0)
call_3730 = relay.TupleGetItem(func_2477_call(), 0)
func_3435_call = mod.get_global_var('func_3435')
func_3436_call = mutated_mod.get_global_var('func_3436')
call_3743 = relay.TupleGetItem(func_3435_call(), 4)
call_3744 = relay.TupleGetItem(func_3436_call(), 4)
var_3769 = relay.var("var_3769", dtype = "uint16", shape = (6, 30))#candidate|3769|(6, 30)|var|uint16
bop_3770 = relay.divide(call_3729.astype('float32'), relay.reshape(var_3769.astype('float32'), relay.shape_of(call_3729))) # shape=(6, 30)
bop_3773 = relay.divide(call_3730.astype('float32'), relay.reshape(var_3769.astype('float32'), relay.shape_of(call_3730))) # shape=(6, 30)
uop_3774 = relay.erf(bop_3770.astype('float32')) # shape=(6, 30)
uop_3776 = relay.erf(bop_3773.astype('float32')) # shape=(6, 30)
output = relay.Tuple([call_3743,uop_3774,])
output2 = relay.Tuple([call_3744,uop_3776,])
func_3783 = relay.Function([var_3769,], output)
mod['func_3783'] = func_3783
mod = relay.transform.InferType()(mod)
var_3784 = relay.var("var_3784", dtype = "uint16", shape = (6, 30))#candidate|3784|(6, 30)|var|uint16
output = func_3783(var_3784)
func_3785 = relay.Function([var_3784], output)
mutated_mod['func_3785'] = func_3785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3554_call = mod.get_global_var('func_3554')
func_3556_call = mutated_mod.get_global_var('func_3556')
call_3809 = relay.TupleGetItem(func_3554_call(), 0)
call_3810 = relay.TupleGetItem(func_3556_call(), 0)
output = relay.Tuple([call_3809,])
output2 = relay.Tuple([call_3810,])
func_3816 = relay.Function([], output)
mod['func_3816'] = func_3816
mod = relay.transform.InferType()(mod)
output = func_3816()
func_3817 = relay.Function([], output)
mutated_mod['func_3817'] = func_3817
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3874 = relay.var("var_3874", dtype = "float32", shape = (1, 4, 6))#candidate|3874|(1, 4, 6)|var|float32
uop_3875 = relay.erf(var_3874.astype('float32')) # shape=(1, 4, 6)
output = uop_3875
output2 = uop_3875
func_3877 = relay.Function([var_3874,], output)
mod['func_3877'] = func_3877
mod = relay.transform.InferType()(mod)
mutated_mod['func_3877'] = func_3877
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3878 = relay.var("var_3878", dtype = "float32", shape = (1, 4, 6))#candidate|3878|(1, 4, 6)|var|float32
func_3877_call = mutated_mod.get_global_var('func_3877')
call_3879 = func_3877_call(var_3878)
output = call_3879
func_3880 = relay.Function([var_3878], output)
mutated_mod['func_3880'] = func_3880
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2923_call = mod.get_global_var('func_2923')
func_2925_call = mutated_mod.get_global_var('func_2925')
call_4003 = relay.TupleGetItem(func_2923_call(), 0)
call_4004 = relay.TupleGetItem(func_2925_call(), 0)
uop_4015 = relay.asinh(call_4003.astype('float32')) # shape=(6, 30)
uop_4017 = relay.asinh(call_4004.astype('float32')) # shape=(6, 30)
output = relay.Tuple([uop_4015,])
output2 = relay.Tuple([uop_4017,])
func_4018 = relay.Function([], output)
mod['func_4018'] = func_4018
mod = relay.transform.InferType()(mod)
mutated_mod['func_4018'] = func_4018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4018_call = mutated_mod.get_global_var('func_4018')
call_4019 = func_4018_call()
output = call_4019
func_4020 = relay.Function([], output)
mutated_mod['func_4020'] = func_4020
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2079_call = mod.get_global_var('func_2079')
func_2080_call = mutated_mod.get_global_var('func_2080')
call_4042 = relay.TupleGetItem(func_2079_call(), 0)
call_4043 = relay.TupleGetItem(func_2080_call(), 0)
var_4051 = relay.var("var_4051", dtype = "float32", shape = (15, 4, 3))#candidate|4051|(15, 4, 3)|var|float32
bop_4052 = relay.less_equal(call_4042.astype('bool'), relay.reshape(var_4051.astype('bool'), relay.shape_of(call_4042))) # shape=(15, 4, 3)
bop_4055 = relay.less_equal(call_4043.astype('bool'), relay.reshape(var_4051.astype('bool'), relay.shape_of(call_4043))) # shape=(15, 4, 3)
func_4018_call = mod.get_global_var('func_4018')
func_4020_call = mutated_mod.get_global_var('func_4020')
call_4064 = relay.TupleGetItem(func_4018_call(), 0)
call_4065 = relay.TupleGetItem(func_4020_call(), 0)
output = relay.Tuple([bop_4052,call_4064,])
output2 = relay.Tuple([bop_4055,call_4065,])
func_4067 = relay.Function([var_4051,], output)
mod['func_4067'] = func_4067
mod = relay.transform.InferType()(mod)
var_4068 = relay.var("var_4068", dtype = "float32", shape = (15, 4, 3))#candidate|4068|(15, 4, 3)|var|float32
output = func_4067(var_4068)
func_4069 = relay.Function([var_4068], output)
mutated_mod['func_4069'] = func_4069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1714_call = mod.get_global_var('func_1714')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_4184 = relay.TupleGetItem(func_1714_call(), 0)
call_4185 = relay.TupleGetItem(func_1715_call(), 0)
var_4189 = relay.var("var_4189", dtype = "float32", shape = (7, 6, 10))#candidate|4189|(7, 6, 10)|var|float32
bop_4190 = relay.maximum(call_4184.astype('int64'), relay.reshape(var_4189.astype('int64'), relay.shape_of(call_4184))) # shape=(7, 6, 10)
bop_4193 = relay.maximum(call_4185.astype('int64'), relay.reshape(var_4189.astype('int64'), relay.shape_of(call_4185))) # shape=(7, 6, 10)
output = relay.Tuple([bop_4190,])
output2 = relay.Tuple([bop_4193,])
func_4200 = relay.Function([var_4189,], output)
mod['func_4200'] = func_4200
mod = relay.transform.InferType()(mod)
mutated_mod['func_4200'] = func_4200
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4201 = relay.var("var_4201", dtype = "float32", shape = (7, 6, 10))#candidate|4201|(7, 6, 10)|var|float32
func_4200_call = mutated_mod.get_global_var('func_4200')
call_4202 = func_4200_call(var_4201)
output = call_4202
func_4203 = relay.Function([var_4201], output)
mutated_mod['func_4203'] = func_4203
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2651_call = mod.get_global_var('func_2651')
func_2653_call = mutated_mod.get_global_var('func_2653')
call_4208 = func_2651_call()
call_4209 = func_2651_call()
output = relay.Tuple([call_4208,])
output2 = relay.Tuple([call_4209,])
func_4211 = relay.Function([], output)
mod['func_4211'] = func_4211
mod = relay.transform.InferType()(mod)
mutated_mod['func_4211'] = func_4211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4211_call = mutated_mod.get_global_var('func_4211')
call_4212 = func_4211_call()
output = call_4212
func_4213 = relay.Function([], output)
mutated_mod['func_4213'] = func_4213
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2006_call = mod.get_global_var('func_2006')
func_2008_call = mutated_mod.get_global_var('func_2008')
call_4222 = relay.TupleGetItem(func_2006_call(), 0)
call_4223 = relay.TupleGetItem(func_2008_call(), 0)
func_2651_call = mod.get_global_var('func_2651')
func_2653_call = mutated_mod.get_global_var('func_2653')
call_4226 = func_2651_call()
call_4227 = func_2651_call()
output = relay.Tuple([call_4222,call_4226,])
output2 = relay.Tuple([call_4223,call_4227,])
func_4229 = relay.Function([], output)
mod['func_4229'] = func_4229
mod = relay.transform.InferType()(mod)
output = func_4229()
func_4230 = relay.Function([], output)
mutated_mod['func_4230'] = func_4230
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4231 = relay.var("var_4231", dtype = "uint16", shape = (7, 15, 5))#candidate|4231|(7, 15, 5)|var|uint16
var_4232 = relay.var("var_4232", dtype = "uint16", shape = (7, 15, 5))#candidate|4232|(7, 15, 5)|var|uint16
bop_4233 = relay.greater_equal(var_4231.astype('bool'), relay.reshape(var_4232.astype('bool'), relay.shape_of(var_4231))) # shape=(7, 15, 5)
func_4200_call = mod.get_global_var('func_4200')
func_4203_call = mutated_mod.get_global_var('func_4203')
var_4240 = relay.var("var_4240", dtype = "float32", shape = (420,))#candidate|4240|(420,)|var|float32
call_4239 = relay.TupleGetItem(func_4200_call(relay.reshape(var_4240.astype('float32'), [7, 6, 10])), 0)
call_4241 = relay.TupleGetItem(func_4203_call(relay.reshape(var_4240.astype('float32'), [7, 6, 10])), 0)
func_4229_call = mod.get_global_var('func_4229')
func_4230_call = mutated_mod.get_global_var('func_4230')
call_4246 = relay.TupleGetItem(func_4229_call(), 0)
call_4247 = relay.TupleGetItem(func_4230_call(), 0)
output = relay.Tuple([bop_4233,call_4239,var_4240,call_4246,])
output2 = relay.Tuple([bop_4233,call_4241,var_4240,call_4247,])
func_4258 = relay.Function([var_4231,var_4232,var_4240,], output)
mod['func_4258'] = func_4258
mod = relay.transform.InferType()(mod)
var_4259 = relay.var("var_4259", dtype = "uint16", shape = (7, 15, 5))#candidate|4259|(7, 15, 5)|var|uint16
var_4260 = relay.var("var_4260", dtype = "uint16", shape = (7, 15, 5))#candidate|4260|(7, 15, 5)|var|uint16
var_4261 = relay.var("var_4261", dtype = "float32", shape = (420,))#candidate|4261|(420,)|var|float32
output = func_4258(var_4259,var_4260,var_4261,)
func_4262 = relay.Function([var_4259,var_4260,var_4261,], output)
mutated_mod['func_4262'] = func_4262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2543_call = mod.get_global_var('func_2543')
func_2544_call = mutated_mod.get_global_var('func_2544')
call_4287 = relay.TupleGetItem(func_2543_call(), 0)
call_4288 = relay.TupleGetItem(func_2544_call(), 0)
func_3816_call = mod.get_global_var('func_3816')
func_3817_call = mutated_mod.get_global_var('func_3817')
call_4293 = relay.TupleGetItem(func_3816_call(), 0)
call_4294 = relay.TupleGetItem(func_3817_call(), 0)
func_1107_call = mod.get_global_var('func_1107')
func_1109_call = mutated_mod.get_global_var('func_1109')
var_4304 = relay.var("var_4304", dtype = "float64", shape = (16, 10))#candidate|4304|(16, 10)|var|float64
call_4303 = relay.TupleGetItem(func_1107_call(relay.reshape(var_4304.astype('float64'), [8, 2, 10])), 0)
call_4305 = relay.TupleGetItem(func_1109_call(relay.reshape(var_4304.astype('float64'), [8, 2, 10])), 0)
func_3195_call = mod.get_global_var('func_3195')
func_3198_call = mutated_mod.get_global_var('func_3198')
var_4316 = relay.var("var_4316", dtype = "float32", shape = (420,))#candidate|4316|(420,)|var|float32
call_4315 = relay.TupleGetItem(func_3195_call(relay.reshape(var_4316.astype('float32'), [7, 6, 10])), 1)
call_4317 = relay.TupleGetItem(func_3198_call(relay.reshape(var_4316.astype('float32'), [7, 6, 10])), 1)
output = relay.Tuple([call_4287,call_4293,call_4303,var_4304,call_4315,var_4316,])
output2 = relay.Tuple([call_4288,call_4294,call_4305,var_4304,call_4317,var_4316,])
func_4322 = relay.Function([var_4304,var_4316,], output)
mod['func_4322'] = func_4322
mod = relay.transform.InferType()(mod)
mutated_mod['func_4322'] = func_4322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4322_call = mutated_mod.get_global_var('func_4322')
var_4324 = relay.var("var_4324", dtype = "float64", shape = (16, 10))#candidate|4324|(16, 10)|var|float64
var_4325 = relay.var("var_4325", dtype = "float32", shape = (420,))#candidate|4325|(420,)|var|float32
call_4323 = func_4322_call(var_4324,var_4325,)
output = call_4323
func_4326 = relay.Function([var_4324,var_4325,], output)
mutated_mod['func_4326'] = func_4326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2079_call = mod.get_global_var('func_2079')
func_2080_call = mutated_mod.get_global_var('func_2080')
call_4378 = relay.TupleGetItem(func_2079_call(), 0)
call_4379 = relay.TupleGetItem(func_2080_call(), 0)
uop_4383 = relay.acos(call_4378.astype('float64')) # shape=(15, 4, 3)
uop_4385 = relay.acos(call_4379.astype('float64')) # shape=(15, 4, 3)
output = uop_4383
output2 = uop_4385
func_4390 = relay.Function([], output)
mod['func_4390'] = func_4390
mod = relay.transform.InferType()(mod)
output = func_4390()
func_4391 = relay.Function([], output)
mutated_mod['func_4391'] = func_4391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2866_call = mod.get_global_var('func_2866')
func_2867_call = mutated_mod.get_global_var('func_2867')
call_4451 = func_2866_call()
call_4452 = func_2866_call()
output = call_4451
output2 = call_4452
func_4464 = relay.Function([], output)
mod['func_4464'] = func_4464
mod = relay.transform.InferType()(mod)
output = func_4464()
func_4465 = relay.Function([], output)
mutated_mod['func_4465'] = func_4465
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4229_call = mod.get_global_var('func_4229')
func_4230_call = mutated_mod.get_global_var('func_4230')
call_4519 = relay.TupleGetItem(func_4229_call(), 1)
call_4520 = relay.TupleGetItem(func_4230_call(), 1)
func_4322_call = mod.get_global_var('func_4322')
func_4326_call = mutated_mod.get_global_var('func_4326')
var_4524 = relay.var("var_4524", dtype = "float64", shape = (160,))#candidate|4524|(160,)|var|float64
var_4525 = relay.var("var_4525", dtype = "float32", shape = (420,))#candidate|4525|(420,)|var|float32
call_4523 = relay.TupleGetItem(func_4322_call(relay.reshape(var_4524.astype('float64'), [16, 10]), relay.reshape(var_4525.astype('float32'), [420,]), ), 4)
call_4526 = relay.TupleGetItem(func_4326_call(relay.reshape(var_4524.astype('float64'), [16, 10]), relay.reshape(var_4525.astype('float32'), [420,]), ), 4)
output = relay.Tuple([call_4519,call_4523,var_4524,var_4525,])
output2 = relay.Tuple([call_4520,call_4526,var_4524,var_4525,])
func_4531 = relay.Function([var_4524,var_4525,], output)
mod['func_4531'] = func_4531
mod = relay.transform.InferType()(mod)
mutated_mod['func_4531'] = func_4531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4531_call = mutated_mod.get_global_var('func_4531')
var_4533 = relay.var("var_4533", dtype = "float64", shape = (160,))#candidate|4533|(160,)|var|float64
var_4534 = relay.var("var_4534", dtype = "float32", shape = (420,))#candidate|4534|(420,)|var|float32
call_4532 = func_4531_call(var_4533,var_4534,)
output = call_4532
func_4535 = relay.Function([var_4533,var_4534,], output)
mutated_mod['func_4535'] = func_4535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2476_call = mod.get_global_var('func_2476')
func_2477_call = mutated_mod.get_global_var('func_2477')
call_4568 = relay.TupleGetItem(func_2476_call(), 0)
call_4569 = relay.TupleGetItem(func_2477_call(), 0)
output = relay.Tuple([call_4568,])
output2 = relay.Tuple([call_4569,])
func_4578 = relay.Function([], output)
mod['func_4578'] = func_4578
mod = relay.transform.InferType()(mod)
output = func_4578()
func_4579 = relay.Function([], output)
mutated_mod['func_4579'] = func_4579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4018_call = mod.get_global_var('func_4018')
func_4020_call = mutated_mod.get_global_var('func_4020')
call_4583 = relay.TupleGetItem(func_4018_call(), 0)
call_4584 = relay.TupleGetItem(func_4020_call(), 0)
func_2210_call = mod.get_global_var('func_2210')
func_2213_call = mutated_mod.get_global_var('func_2213')
call_4587 = relay.TupleGetItem(func_2210_call(relay.reshape(call_4583.astype('uint16'), [180,])), 2)
call_4588 = relay.TupleGetItem(func_2213_call(relay.reshape(call_4583.astype('uint16'), [180,])), 2)
output = relay.Tuple([call_4583,call_4587,])
output2 = relay.Tuple([call_4584,call_4588,])
func_4608 = relay.Function([], output)
mod['func_4608'] = func_4608
mod = relay.transform.InferType()(mod)
output = func_4608()
func_4609 = relay.Function([], output)
mutated_mod['func_4609'] = func_4609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4608_call = mod.get_global_var('func_4608')
func_4609_call = mutated_mod.get_global_var('func_4609')
call_4618 = relay.TupleGetItem(func_4608_call(), 1)
call_4619 = relay.TupleGetItem(func_4609_call(), 1)
var_4620 = relay.var("var_4620", dtype = "uint64", shape = (6, 30))#candidate|4620|(6, 30)|var|uint64
bop_4621 = relay.bitwise_and(call_4618.astype('int32'), relay.reshape(var_4620.astype('int32'), relay.shape_of(call_4618))) # shape=(6, 30)
bop_4624 = relay.bitwise_and(call_4619.astype('int32'), relay.reshape(var_4620.astype('int32'), relay.shape_of(call_4619))) # shape=(6, 30)
bop_4628 = relay.bitwise_xor(call_4618.astype('int32'), relay.reshape(bop_4621.astype('int32'), relay.shape_of(call_4618))) # shape=(6, 30)
bop_4631 = relay.bitwise_xor(call_4619.astype('int32'), relay.reshape(bop_4624.astype('int32'), relay.shape_of(call_4619))) # shape=(6, 30)
uop_4634 = relay.atanh(var_4620.astype('float64')) # shape=(6, 30)
output = relay.Tuple([bop_4628,uop_4634,])
output2 = relay.Tuple([bop_4631,uop_4634,])
func_4637 = relay.Function([var_4620,], output)
mod['func_4637'] = func_4637
mod = relay.transform.InferType()(mod)
mutated_mod['func_4637'] = func_4637
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4638 = relay.var("var_4638", dtype = "uint64", shape = (6, 30))#candidate|4638|(6, 30)|var|uint64
func_4637_call = mutated_mod.get_global_var('func_4637')
call_4639 = func_4637_call(var_4638)
output = call_4639
func_4640 = relay.Function([var_4638], output)
mutated_mod['func_4640'] = func_4640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3554_call = mod.get_global_var('func_3554')
func_3556_call = mutated_mod.get_global_var('func_3556')
call_4761 = relay.TupleGetItem(func_3554_call(), 0)
call_4762 = relay.TupleGetItem(func_3556_call(), 0)
func_3554_call = mod.get_global_var('func_3554')
func_3556_call = mutated_mod.get_global_var('func_3556')
call_4765 = relay.TupleGetItem(func_3554_call(), 0)
call_4766 = relay.TupleGetItem(func_3556_call(), 0)
bop_4767 = relay.logical_or(call_4765.astype('bool'), relay.reshape(call_4761.astype('bool'), relay.shape_of(call_4765))) # shape=(15, 4, 3)
bop_4770 = relay.logical_or(call_4766.astype('bool'), relay.reshape(call_4762.astype('bool'), relay.shape_of(call_4766))) # shape=(15, 4, 3)
func_4211_call = mod.get_global_var('func_4211')
func_4213_call = mutated_mod.get_global_var('func_4213')
call_4780 = relay.TupleGetItem(func_4211_call(), 0)
call_4781 = relay.TupleGetItem(func_4213_call(), 0)
uop_4788 = relay.acosh(call_4780.astype('float32')) # shape=(6, 30)
uop_4790 = relay.acosh(call_4781.astype('float32')) # shape=(6, 30)
output = relay.Tuple([bop_4767,uop_4788,])
output2 = relay.Tuple([bop_4770,uop_4790,])
func_4791 = relay.Function([], output)
mod['func_4791'] = func_4791
mod = relay.transform.InferType()(mod)
mutated_mod['func_4791'] = func_4791
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4791_call = mutated_mod.get_global_var('func_4791')
call_4792 = func_4791_call()
output = call_4792
func_4793 = relay.Function([], output)
mutated_mod['func_4793'] = func_4793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1714_call = mod.get_global_var('func_1714')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_4829 = relay.TupleGetItem(func_1714_call(), 0)
call_4830 = relay.TupleGetItem(func_1715_call(), 0)
output = relay.Tuple([call_4829,])
output2 = relay.Tuple([call_4830,])
func_4838 = relay.Function([], output)
mod['func_4838'] = func_4838
mod = relay.transform.InferType()(mod)
output = func_4838()
func_4839 = relay.Function([], output)
mutated_mod['func_4839'] = func_4839
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4873 = relay.var("var_4873", dtype = "bool", shape = (4, 12, 5))#candidate|4873|(4, 12, 5)|var|bool
var_4874 = relay.var("var_4874", dtype = "bool", shape = (4, 12, 5))#candidate|4874|(4, 12, 5)|var|bool
bop_4875 = relay.logical_or(var_4873.astype('bool'), relay.reshape(var_4874.astype('bool'), relay.shape_of(var_4873))) # shape=(4, 12, 5)
uop_4880 = relay.asinh(var_4874.astype('float32')) # shape=(4, 12, 5)
uop_4895 = relay.cosh(var_4874.astype('float64')) # shape=(4, 12, 5)
uop_4920 = relay.exp(var_4873.astype('float32')) # shape=(4, 12, 5)
output = relay.Tuple([bop_4875,uop_4880,uop_4895,uop_4920,])
output2 = relay.Tuple([bop_4875,uop_4880,uop_4895,uop_4920,])
func_4929 = relay.Function([var_4873,var_4874,], output)
mod['func_4929'] = func_4929
mod = relay.transform.InferType()(mod)
var_4930 = relay.var("var_4930", dtype = "bool", shape = (4, 12, 5))#candidate|4930|(4, 12, 5)|var|bool
var_4931 = relay.var("var_4931", dtype = "bool", shape = (4, 12, 5))#candidate|4931|(4, 12, 5)|var|bool
output = func_4929(var_4930,var_4931,)
func_4932 = relay.Function([var_4930,var_4931,], output)
mutated_mod['func_4932'] = func_4932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4578_call = mod.get_global_var('func_4578')
func_4579_call = mutated_mod.get_global_var('func_4579')
call_4947 = relay.TupleGetItem(func_4578_call(), 0)
call_4948 = relay.TupleGetItem(func_4579_call(), 0)
func_4211_call = mod.get_global_var('func_4211')
func_4213_call = mutated_mod.get_global_var('func_4213')
call_4964 = relay.TupleGetItem(func_4211_call(), 0)
call_4965 = relay.TupleGetItem(func_4213_call(), 0)
output = relay.Tuple([call_4947,call_4964,])
output2 = relay.Tuple([call_4948,call_4965,])
func_4970 = relay.Function([], output)
mod['func_4970'] = func_4970
mod = relay.transform.InferType()(mod)
output = func_4970()
func_4971 = relay.Function([], output)
mutated_mod['func_4971'] = func_4971
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2866_call = mod.get_global_var('func_2866')
func_2867_call = mutated_mod.get_global_var('func_2867')
call_4974 = func_2866_call()
call_4975 = func_2866_call()
uop_4982 = relay.rsqrt(call_4974.astype('float32')) # shape=(7, 6, 10)
uop_4984 = relay.rsqrt(call_4975.astype('float32')) # shape=(7, 6, 10)
bop_4985 = relay.floor_divide(uop_4982.astype('float32'), relay.reshape(call_4974.astype('float32'), relay.shape_of(uop_4982))) # shape=(7, 6, 10)
bop_4988 = relay.floor_divide(uop_4984.astype('float32'), relay.reshape(call_4975.astype('float32'), relay.shape_of(uop_4984))) # shape=(7, 6, 10)
output = relay.Tuple([bop_4985,])
output2 = relay.Tuple([bop_4988,])
func_5012 = relay.Function([], output)
mod['func_5012'] = func_5012
mod = relay.transform.InferType()(mod)
mutated_mod['func_5012'] = func_5012
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5012_call = mutated_mod.get_global_var('func_5012')
call_5013 = func_5012_call()
output = call_5013
func_5014 = relay.Function([], output)
mutated_mod['func_5014'] = func_5014
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5015 = relay.const([[[-8.857793,-7.177400,-9.990100,-1.780424,6.976219,5.636294,4.899342,-0.839774,-4.438485,2.324212,1.074343,4.614668,-1.999711],[2.656884,-7.488757,6.153385,-3.273425,0.770620,-7.140506,-5.670604,3.344672,6.079459,7.227746,6.393790,6.869161,7.823372],[-2.018997,-0.936641,-3.132641,-9.242863,-1.014355,2.983229,2.164849,8.908998,-2.914542,-8.559168,8.339955,-2.921724,6.111133],[5.765802,2.983287,8.509743,6.179579,-9.992928,-4.843572,2.282691,-1.078191,2.853345,5.860203,4.892926,-7.131986,6.176004],[1.007839,-1.970422,5.524675,-8.172949,-9.849281,-2.079034,1.759810,7.864074,7.842361,-9.808828,-9.698722,-8.487400,-4.036577],[3.656825,0.969451,-2.787596,3.754362,5.964928,-8.318765,7.128243,7.931013,4.738575,-2.726694,-3.904878,3.005909,0.488112],[-2.465403,2.638565,8.466660,8.898232,4.474084,2.668471,-0.704782,9.032442,-7.154757,-6.205392,-0.185540,-7.107649,-3.203000]]], dtype = "float64")#candidate|5015|(1, 7, 13)|const|float64
uop_5016 = relay.cosh(const_5015.astype('float64')) # shape=(1, 7, 13)
uop_5018 = relay.log10(uop_5016.astype('float64')) # shape=(1, 7, 13)
uop_5026 = relay.asinh(uop_5018.astype('float32')) # shape=(1, 7, 13)
func_3195_call = mod.get_global_var('func_3195')
func_3198_call = mutated_mod.get_global_var('func_3198')
var_5029 = relay.var("var_5029", dtype = "float32", shape = (420,))#candidate|5029|(420,)|var|float32
call_5028 = relay.TupleGetItem(func_3195_call(relay.reshape(var_5029.astype('float32'), [7, 6, 10])), 0)
call_5030 = relay.TupleGetItem(func_3198_call(relay.reshape(var_5029.astype('float32'), [7, 6, 10])), 0)
bop_5038 = relay.less(uop_5026.astype('bool'), relay.reshape(uop_5016.astype('bool'), relay.shape_of(uop_5026))) # shape=(1, 7, 13)
uop_5056 = relay.acosh(bop_5038.astype('float32')) # shape=(1, 7, 13)
uop_5064 = relay.asin(uop_5026.astype('float32')) # shape=(1, 7, 13)
func_845_call = mod.get_global_var('func_845')
func_847_call = mutated_mod.get_global_var('func_847')
var_5067 = relay.var("var_5067", dtype = "float32", shape = ())#candidate|5067|()|var|float32
call_5066 = func_845_call(relay.reshape(var_5067.astype('float32'), []))
call_5068 = func_845_call(relay.reshape(var_5067.astype('float32'), []))
output = relay.Tuple([call_5028,var_5029,uop_5056,uop_5064,call_5066,var_5067,])
output2 = relay.Tuple([call_5030,var_5029,uop_5056,uop_5064,call_5068,var_5067,])
func_5070 = relay.Function([var_5029,var_5067,], output)
mod['func_5070'] = func_5070
mod = relay.transform.InferType()(mod)
mutated_mod['func_5070'] = func_5070
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5070_call = mutated_mod.get_global_var('func_5070')
var_5072 = relay.var("var_5072", dtype = "float32", shape = (420,))#candidate|5072|(420,)|var|float32
var_5073 = relay.var("var_5073", dtype = "float32", shape = ())#candidate|5073|()|var|float32
call_5071 = func_5070_call(var_5072,var_5073,)
output = call_5071
func_5074 = relay.Function([var_5072,var_5073,], output)
mutated_mod['func_5074'] = func_5074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3435_call = mod.get_global_var('func_3435')
func_3436_call = mutated_mod.get_global_var('func_3436')
call_5115 = relay.TupleGetItem(func_3435_call(), 2)
call_5116 = relay.TupleGetItem(func_3436_call(), 2)
func_2210_call = mod.get_global_var('func_2210')
func_2213_call = mutated_mod.get_global_var('func_2213')
call_5118 = relay.TupleGetItem(func_2210_call(relay.reshape(call_5115.astype('uint16'), [180,])), 2)
call_5119 = relay.TupleGetItem(func_2213_call(relay.reshape(call_5115.astype('uint16'), [180,])), 2)
output = relay.Tuple([call_5115,call_5118,])
output2 = relay.Tuple([call_5116,call_5119,])
func_5124 = relay.Function([], output)
mod['func_5124'] = func_5124
mod = relay.transform.InferType()(mod)
output = func_5124()
func_5125 = relay.Function([], output)
mutated_mod['func_5125'] = func_5125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2651_call = mod.get_global_var('func_2651')
func_2653_call = mutated_mod.get_global_var('func_2653')
call_5153 = func_2651_call()
call_5154 = func_2651_call()
func_4637_call = mod.get_global_var('func_4637')
func_4640_call = mutated_mod.get_global_var('func_4640')
call_5180 = relay.TupleGetItem(func_4637_call(relay.reshape(call_5153.astype('uint64'), [6, 30])), 1)
call_5181 = relay.TupleGetItem(func_4640_call(relay.reshape(call_5153.astype('uint64'), [6, 30])), 1)
func_3877_call = mod.get_global_var('func_3877')
func_3880_call = mutated_mod.get_global_var('func_3880')
const_5184 = relay.const([[-3.882347,-7.380984,-7.470941,-3.977431],[-1.624336,8.281785,-0.201413,1.214117],[-8.041420,-0.357504,-7.049410,8.768002],[1.321044,9.709985,6.419215,-6.364724],[-1.835469,-7.156217,-7.702477,-4.138188],[1.675302,1.522703,1.424128,-0.221836]], dtype = "float32")#candidate|5184|(6, 4)|const|float32
call_5183 = func_3877_call(relay.reshape(const_5184.astype('float32'), [1, 4, 6]))
call_5185 = func_3877_call(relay.reshape(const_5184.astype('float32'), [1, 4, 6]))
output = relay.Tuple([call_5153,call_5180,call_5183,const_5184,])
output2 = relay.Tuple([call_5154,call_5181,call_5185,const_5184,])
func_5188 = relay.Function([], output)
mod['func_5188'] = func_5188
mod = relay.transform.InferType()(mod)
output = func_5188()
func_5189 = relay.Function([], output)
mutated_mod['func_5189'] = func_5189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3816_call = mod.get_global_var('func_3816')
func_3817_call = mutated_mod.get_global_var('func_3817')
call_5190 = relay.TupleGetItem(func_3816_call(), 0)
call_5191 = relay.TupleGetItem(func_3817_call(), 0)
func_4791_call = mod.get_global_var('func_4791')
func_4793_call = mutated_mod.get_global_var('func_4793')
call_5192 = relay.TupleGetItem(func_4791_call(), 1)
call_5193 = relay.TupleGetItem(func_4793_call(), 1)
func_4531_call = mod.get_global_var('func_4531')
func_4535_call = mutated_mod.get_global_var('func_4535')
var_5210 = relay.var("var_5210", dtype = "float64", shape = (160,))#candidate|5210|(160,)|var|float64
const_5211 = relay.const([-5.679245,3.701902,-8.668082,-9.030825,1.834617,7.314729,8.571375,-1.272865,0.779647,-4.086437,-6.664380,4.729285,7.974158,9.960264,-1.242985,-1.598443,3.192051,-1.149050,-0.405638,5.874527,4.201546,6.264428,-6.317000,7.644468,-0.869368,2.044333,-8.513915,3.611237,-4.541145,5.110370,7.291058,1.277018,2.625417,-3.320902,-5.955588,0.681680,1.727108,3.080763,-6.065399,1.720588,-9.371636,-3.750417,3.043344,-1.337602,-6.709472,-3.024207,7.688671,6.754117,-2.460084,-5.847355,1.136238,-8.118326,3.997296,-3.624060,-8.659945,-4.262611,-2.150420,-8.216591,-5.047361,7.748744,-4.247219,-7.289454,-5.898660,-3.803312,-8.072201,5.428086,-7.294293,-9.113106,7.658505,7.329938,-5.753586,6.358798,-7.712089,-2.512376,-4.742027,-0.861047,2.835623,5.578988,-8.278824,-3.493358,-0.667413,-5.737030,1.778065,-3.234901,7.451950,9.276234,6.481204,-1.603754,-7.546148,-5.092904,8.885699,1.509309,-2.465392,-1.070337,-4.800932,9.170600,-4.213336,5.583979,-2.142973,8.812475,8.228102,0.868681,2.761704,1.220658,-8.254657,-8.920914,-7.934930,-1.354990,-2.788727,6.319625,-9.954504,-5.709652,-3.324430,-0.080181,6.279077,-3.772874,-8.583891,-7.259965,8.396124,5.428967,7.008436,4.417373,7.488015,-2.690511,-2.408091,-0.063432,-1.838189,-1.666415,-2.285183,9.479912,-3.871237,3.785130,3.650315,-8.257058,8.512345,-7.560458,4.552945,-8.483817,-4.378462,8.659957,-1.718996,8.304483,-7.910196,9.971911,-7.231379,-3.737823,-1.318242,-7.780597,2.751584,-2.016532,-5.326035,-8.106033,9.110383,6.905305,7.777511,-4.045560,-2.356004,0.868652,8.991138,-6.139461,2.600032,-5.206463,-2.215822,-4.735586,1.768219,-7.523309,3.444265,-0.333258,0.903174,-8.193023,-3.775195,-1.742481,-0.590044,8.135271,-7.206643,-4.863885,-1.891861,7.146228,5.371393,4.686902,-7.867463,-7.668545,-0.197099,-6.591205,-4.298031,-4.496123,-1.937856,-2.511261,-6.369610,-4.985121,8.307647,3.507702,-0.882563,-1.004708,-6.229822,-3.985706,6.464183,-0.138234,8.770853,9.512147,-2.611442,-1.041770,-2.893278,7.789782,-9.754940,0.526652,-6.077602,-8.841747,0.947736,-7.286189,-9.603614,-7.221460,-7.097607,5.413822,-0.090400,0.699147,-6.668105,3.451440,-1.854337,-3.070939,-6.048294,-2.973553,-8.789622,6.093227,1.044035,4.816120,2.688262,4.897882,-7.875341,4.168010,0.799725,8.415054,6.483430,-4.080088,-1.465469,-3.716993,-6.295853,5.745876,3.493991,-3.971449,7.409912,-1.386472,-4.476178,-2.142834,-6.788108,0.433853,-9.446217,-7.202717,5.015375,-9.655413,0.878623,-4.841349,9.609789,-9.333390,7.780425,-2.985117,-4.893420,4.657574,-6.571600,2.580048,6.107983,0.497454,-2.015503,8.260625,-7.887813,4.568770,0.301635,-4.811756,1.702633,6.249542,0.378036,6.249508,6.178229,-6.684244,-5.306374,-1.106720,-6.231556,-5.205269,5.123817,-0.404830,2.737032,8.971190,-1.781796,6.127053,-9.518495,-8.554299,-5.136540,3.664195,-5.698496,-0.296883,-0.255692,-0.024302,-5.932108,7.691776,0.288479,5.451313,5.367472,9.442566,-2.051388,1.187282,3.106777,0.980799,-6.585993,5.360551,-1.279617,0.084589,8.348556,-2.323135,-1.432061,2.359214,7.127832,-6.268252,-5.074868,-9.895556,3.393876,3.768878,8.122046,-0.551012,-3.596773,-3.955937,8.222027,4.414067,-6.560667,-3.065884,8.600851,-0.222874,6.112911,3.681462,-8.937806,-8.118251,7.852112,-2.967399,-6.257648,-3.096681,9.739752,-5.043983,7.233011,3.909028,4.932847,-6.626511,6.840810,0.566123,-5.316217,-4.976789,2.758040,-9.331452,1.794752,0.529427,5.799410,-5.373079,0.173337,-7.167025,-4.695300,-7.472733,5.166524,-8.831049,0.269999,4.893432,-3.762080,-2.386094,0.328291,-7.729361,0.312782,-8.856855,-5.752231,9.472850,1.120304,-6.530292,8.273725,8.958022,7.520003,-8.091985,-3.584303,-2.263950,7.925971,-5.316494,0.389200,0.010775,-5.328510,-8.030837,-6.501777,-8.745043,6.015608,1.838327,9.035361,5.078515,-3.685260,6.913613,-4.126147,7.189815,-3.140402,-1.776959,0.894636,0.065670,2.141659,-7.101438,7.856849,-9.417676,1.201243,-8.441942,-9.261058,8.550281,3.755962,9.379706,1.846558,4.648248,-5.640759,9.585285,-6.474644,-4.427709,-4.174585,5.561426,9.010177,-2.266473,-8.075886,-3.774667,5.810749,3.077135,-0.592981,-7.499084], dtype = "float32")#candidate|5211|(420,)|const|float32
call_5209 = relay.TupleGetItem(func_4531_call(relay.reshape(var_5210.astype('float64'), [160,]), relay.reshape(const_5211.astype('float32'), [420,]), ), 3)
call_5212 = relay.TupleGetItem(func_4535_call(relay.reshape(var_5210.astype('float64'), [160,]), relay.reshape(const_5211.astype('float32'), [420,]), ), 3)
output = relay.Tuple([call_5190,call_5192,call_5209,var_5210,const_5211,])
output2 = relay.Tuple([call_5191,call_5193,call_5212,var_5210,const_5211,])
func_5213 = relay.Function([var_5210,], output)
mod['func_5213'] = func_5213
mod = relay.transform.InferType()(mod)
var_5214 = relay.var("var_5214", dtype = "float64", shape = (160,))#candidate|5214|(160,)|var|float64
output = func_5213(var_5214)
func_5215 = relay.Function([var_5214], output)
mutated_mod['func_5215'] = func_5215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4608_call = mod.get_global_var('func_4608')
func_4609_call = mutated_mod.get_global_var('func_4609')
call_5217 = relay.TupleGetItem(func_4608_call(), 1)
call_5218 = relay.TupleGetItem(func_4609_call(), 1)
output = call_5217
output2 = call_5218
func_5219 = relay.Function([], output)
mod['func_5219'] = func_5219
mod = relay.transform.InferType()(mod)
output = func_5219()
func_5220 = relay.Function([], output)
mutated_mod['func_5220'] = func_5220
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5229 = relay.const([[[-1,8,4,-7,-5,-2,-6],[5,9,4,8,4,-4,-8],[-6,-2,9,-1,5,-5,-8]],[[5,5,-3,-7,-4,5,-6],[-6,10,3,-3,2,-5,-3],[-1,9,-6,5,-1,-6,-9]],[[3,-2,2,-5,3,-9,-1],[6,-7,4,3,2,-1,10],[8,-10,7,-1,3,-5,-3]],[[1,-1,5,-4,-5,1,6],[-2,1,6,-10,3,-3,9],[-3,4,-6,3,-6,4,-5]],[[-1,-7,7,-1,-1,-9,6],[1,10,10,9,3,-1,10],[-10,-10,-8,-2,-9,2,-7]],[[2,-3,-1,-8,8,-10,1],[10,9,-8,1,-10,-3,-7],[6,-5,9,3,2,-2,-1]],[[1,-6,-5,1,3,-1,6],[-1,2,6,6,-7,7,2],[-10,-4,7,4,-4,-7,-8]],[[2,-6,-4,8,6,-7,-5],[-10,4,2,-1,-9,-2,9],[-1,-10,10,6,4,5,-10]],[[-5,-9,-3,-5,4,-7,2],[-5,1,-9,-9,-8,-2,-8],[4,-3,6,4,-8,6,8]],[[2,-5,10,-1,6,7,-4],[6,-9,-4,9,-6,-9,3],[-4,-1,8,3,9,-10,-5]],[[-8,-7,-3,-5,1,-6,7],[1,3,1,-6,-9,1,-3],[4,6,-9,8,-1,10,1]]], dtype = "uint32")#candidate|5229|(11, 3, 7)|const|uint32
var_5230 = relay.var("var_5230", dtype = "uint32", shape = (11, 3, 7))#candidate|5230|(11, 3, 7)|var|uint32
bop_5231 = relay.maximum(const_5229.astype('uint32'), relay.reshape(var_5230.astype('uint32'), relay.shape_of(const_5229))) # shape=(11, 3, 7)
func_4018_call = mod.get_global_var('func_4018')
func_4020_call = mutated_mod.get_global_var('func_4020')
call_5234 = relay.TupleGetItem(func_4018_call(), 0)
call_5235 = relay.TupleGetItem(func_4020_call(), 0)
func_4578_call = mod.get_global_var('func_4578')
func_4579_call = mutated_mod.get_global_var('func_4579')
call_5239 = relay.TupleGetItem(func_4578_call(), 0)
call_5240 = relay.TupleGetItem(func_4579_call(), 0)
var_5270 = relay.var("var_5270", dtype = "uint16", shape = (6, 30))#candidate|5270|(6, 30)|var|uint16
bop_5271 = relay.bitwise_or(call_5239.astype('uint64'), relay.reshape(var_5270.astype('uint64'), relay.shape_of(call_5239))) # shape=(6, 30)
bop_5274 = relay.bitwise_or(call_5240.astype('uint64'), relay.reshape(var_5270.astype('uint64'), relay.shape_of(call_5240))) # shape=(6, 30)
func_2543_call = mod.get_global_var('func_2543')
func_2544_call = mutated_mod.get_global_var('func_2544')
call_5292 = relay.TupleGetItem(func_2543_call(), 0)
call_5293 = relay.TupleGetItem(func_2544_call(), 0)
output = relay.Tuple([bop_5231,call_5234,bop_5271,call_5292,])
output2 = relay.Tuple([bop_5231,call_5235,bop_5274,call_5293,])
func_5312 = relay.Function([var_5230,var_5270,], output)
mod['func_5312'] = func_5312
mod = relay.transform.InferType()(mod)
var_5313 = relay.var("var_5313", dtype = "uint32", shape = (11, 3, 7))#candidate|5313|(11, 3, 7)|var|uint32
var_5314 = relay.var("var_5314", dtype = "uint16", shape = (6, 30))#candidate|5314|(6, 30)|var|uint16
output = func_5312(var_5313,var_5314,)
func_5315 = relay.Function([var_5313,var_5314,], output)
mutated_mod['func_5315'] = func_5315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4229_call = mod.get_global_var('func_4229')
func_4230_call = mutated_mod.get_global_var('func_4230')
call_5364 = relay.TupleGetItem(func_4229_call(), 1)
call_5365 = relay.TupleGetItem(func_4230_call(), 1)
output = relay.Tuple([call_5364,])
output2 = relay.Tuple([call_5365,])
func_5410 = relay.Function([], output)
mod['func_5410'] = func_5410
mod = relay.transform.InferType()(mod)
output = func_5410()
func_5411 = relay.Function([], output)
mutated_mod['func_5411'] = func_5411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3554_call = mod.get_global_var('func_3554')
func_3556_call = mutated_mod.get_global_var('func_3556')
call_5416 = relay.TupleGetItem(func_3554_call(), 0)
call_5417 = relay.TupleGetItem(func_3556_call(), 0)
output = call_5416
output2 = call_5417
func_5429 = relay.Function([], output)
mod['func_5429'] = func_5429
mod = relay.transform.InferType()(mod)
mutated_mod['func_5429'] = func_5429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5429_call = mutated_mod.get_global_var('func_5429')
call_5430 = func_5429_call()
output = call_5430
func_5431 = relay.Function([], output)
mutated_mod['func_5431'] = func_5431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2543_call = mod.get_global_var('func_2543')
func_2544_call = mutated_mod.get_global_var('func_2544')
call_5438 = relay.TupleGetItem(func_2543_call(), 0)
call_5439 = relay.TupleGetItem(func_2544_call(), 0)
output = relay.Tuple([call_5438,])
output2 = relay.Tuple([call_5439,])
func_5443 = relay.Function([], output)
mod['func_5443'] = func_5443
mod = relay.transform.InferType()(mod)
output = func_5443()
func_5444 = relay.Function([], output)
mutated_mod['func_5444'] = func_5444
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5497 = relay.var("var_5497", dtype = "uint16", shape = ())#candidate|5497|()|var|uint16
var_5498 = relay.var("var_5498", dtype = "uint16", shape = (1, 11, 1))#candidate|5498|(1, 11, 1)|var|uint16
bop_5499 = relay.maximum(var_5497.astype('uint16'), var_5498.astype('uint16')) # shape=(1, 11, 1)
func_3530_call = mod.get_global_var('func_3530')
func_3531_call = mutated_mod.get_global_var('func_3531')
call_5503 = func_3530_call()
call_5504 = func_3530_call()
bop_5513 = relay.left_shift(bop_5499.astype('uint32'), var_5497.astype('uint32')) # shape=(1, 11, 1)
bop_5519 = relay.logical_or(var_5498.astype('bool'), relay.reshape(bop_5499.astype('bool'), relay.shape_of(var_5498))) # shape=(1, 11, 1)
bop_5522 = relay.power(bop_5513.astype('float32'), var_5497.astype('float32')) # shape=(1, 11, 1)
bop_5525 = relay.floor_mod(var_5497.astype('float64'), bop_5499.astype('float64')) # shape=(1, 11, 1)
func_5124_call = mod.get_global_var('func_5124')
func_5125_call = mutated_mod.get_global_var('func_5125')
call_5539 = relay.TupleGetItem(func_5124_call(), 1)
call_5540 = relay.TupleGetItem(func_5125_call(), 1)
uop_5546 = relay.cosh(bop_5513.astype('float64')) # shape=(1, 11, 1)
func_4390_call = mod.get_global_var('func_4390')
func_4391_call = mutated_mod.get_global_var('func_4391')
call_5554 = func_4390_call()
call_5555 = func_4390_call()
uop_5557 = relay.erf(uop_5546.astype('float32')) # shape=(1, 11, 1)
output = relay.Tuple([call_5503,bop_5519,bop_5522,bop_5525,call_5539,call_5554,uop_5557,])
output2 = relay.Tuple([call_5504,bop_5519,bop_5522,bop_5525,call_5540,call_5555,uop_5557,])
func_5566 = relay.Function([var_5497,var_5498,], output)
mod['func_5566'] = func_5566
mod = relay.transform.InferType()(mod)
var_5567 = relay.var("var_5567", dtype = "uint16", shape = ())#candidate|5567|()|var|uint16
var_5568 = relay.var("var_5568", dtype = "uint16", shape = (1, 11, 1))#candidate|5568|(1, 11, 1)|var|uint16
output = func_5566(var_5567,var_5568,)
func_5569 = relay.Function([var_5567,var_5568,], output)
mutated_mod['func_5569'] = func_5569
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4229_call = mod.get_global_var('func_4229')
func_4230_call = mutated_mod.get_global_var('func_4230')
call_5654 = relay.TupleGetItem(func_4229_call(), 0)
call_5655 = relay.TupleGetItem(func_4230_call(), 0)
output = relay.Tuple([call_5654,])
output2 = relay.Tuple([call_5655,])
func_5657 = relay.Function([], output)
mod['func_5657'] = func_5657
mod = relay.transform.InferType()(mod)
mutated_mod['func_5657'] = func_5657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5657_call = mutated_mod.get_global_var('func_5657')
call_5658 = func_5657_call()
output = call_5658
func_5659 = relay.Function([], output)
mutated_mod['func_5659'] = func_5659
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5665 = relay.const([[[-9.682362,3.061187,2.496986,6.019108,3.267980,-4.949285,3.013596,-1.594765,9.366343,-7.810033,0.678818],[2.749918,-1.063470,9.895654,6.081547,2.818602,6.973630,-5.821817,8.417375,-3.415238,-0.252926,8.249428],[4.086665,7.298220,4.510075,3.902783,-0.784564,2.830965,4.679451,-5.231612,4.850915,-1.918241,-9.898577],[1.007402,-9.709450,6.401460,4.892643,4.182911,-9.265736,7.123352,-3.074503,-5.875876,4.272593,8.483000],[-6.131386,6.798074,3.005760,-4.998956,-3.465929,2.262337,0.293467,5.011413,9.641526,0.944107,5.065917],[3.832588,1.862657,-8.613424,-4.999794,7.060154,-3.771349,-9.936486,-2.298016,3.002090,2.039368,-5.502715],[1.819875,0.815484,-4.247399,-1.703876,2.700122,9.477055,-5.341916,9.392414,9.334138,8.710712,8.507693],[3.449854,9.697061,-3.091239,2.313574,9.178412,9.490709,3.489104,-6.172493,1.052265,-8.356111,-9.054855],[6.771470,7.101338,8.061662,-7.218155,-2.636101,-3.683636,-1.312975,-1.746457,7.268346,9.252914,-3.235810],[-8.145597,-2.480268,-1.995987,-7.953417,2.937599,-6.715729,-6.468692,-9.079055,-9.072476,-5.596479,-4.449498],[-0.257834,-5.885398,-9.999993,-3.451099,8.867630,4.279901,-4.921502,-3.294301,3.664221,-9.389501,-9.950754],[3.986806,6.318243,4.497299,-2.049088,8.537141,6.362447,4.445503,8.088957,-6.644886,-4.749691,-5.157762],[-4.800854,-3.106491,2.560812,8.847583,4.851332,-5.433715,4.148854,3.365484,2.162900,-1.328990,-0.477903],[-8.674841,9.924239,-0.364739,0.090017,-2.184382,2.029559,0.200420,-9.013449,-5.735160,0.303493,-9.968365],[8.113626,-5.576650,-9.608463,3.890400,-0.635960,-8.915063,-1.114935,-2.380366,-7.733091,5.407629,2.407654]],[[-5.285733,-9.852139,8.125931,5.508172,-5.186066,4.215523,4.035330,8.769829,3.244223,-3.136314,8.967091],[-3.373396,-6.108726,-3.556263,4.169993,-3.175870,1.744121,-3.854974,-7.948097,4.753330,-8.576616,-8.893489],[-6.016752,-9.993790,5.957864,-1.116889,-8.715628,-4.605948,2.488595,-3.284987,-4.715125,-3.502426,8.772208],[1.010853,-7.030363,-4.207825,1.720181,-5.640950,-8.799047,8.489881,7.142256,-0.763544,9.664347,8.280643],[-2.933650,3.007048,-9.251980,-0.089796,-1.190174,-9.036806,-7.872322,-7.056878,8.038200,-8.851822,9.437794],[2.393946,3.029058,-5.438098,0.519138,5.126968,-1.380653,-7.598684,-5.781046,-8.399513,-2.884510,4.408217],[-4.600973,3.567189,-4.751328,5.393225,5.316577,-8.895540,3.504447,7.536916,-0.028036,-8.740031,1.047731],[-7.662158,1.125279,4.052481,0.531267,8.678418,-8.349691,4.507984,-0.555325,-6.956244,0.713078,-7.666317],[-5.453785,9.402365,-3.899894,1.544025,2.129903,1.286912,-2.772798,-6.275287,3.586824,6.450585,-8.977010],[-2.332846,-9.434961,1.061892,6.291866,-2.164240,4.360429,4.832455,8.744924,-8.010086,-7.525972,7.946528],[-5.709565,-8.411216,7.681107,1.786835,-4.357524,-8.365821,-9.918330,-4.488011,2.658151,0.578013,9.438998],[-2.586476,5.676839,4.477827,-7.362463,7.659985,-8.718859,-3.420391,9.535423,-7.410023,3.880212,-0.839022],[-3.015894,-0.808473,2.203005,-8.037821,-5.413640,7.112709,2.592844,5.946507,-5.400627,-7.794075,-8.308418],[-4.662161,-7.019371,7.883803,-0.406947,-5.150200,-3.309073,-2.620516,-0.866860,-2.431696,-2.936057,2.969647],[-4.520703,4.206543,4.407615,-5.272759,1.685966,8.835707,1.791655,5.349955,7.015301,-0.128310,-4.399825]],[[9.133212,1.534800,0.134384,-2.116516,-7.913902,6.404404,1.090963,1.130394,-0.883847,-4.338409,7.271478],[-1.908558,5.306061,-9.635518,-7.728101,0.005473,7.727742,1.770346,-1.777918,8.718547,8.043876,-9.618120],[9.802816,-4.300594,-7.140700,-5.343945,-8.221310,9.904280,-6.937117,2.061538,-6.699617,-3.696996,4.057995],[7.752507,7.291253,-9.748448,5.146719,1.913313,0.249771,3.935165,2.996167,7.106268,-1.729252,1.970033],[-9.351903,6.510231,0.967925,-9.017253,-0.634157,-9.051358,4.309074,-8.429599,-7.379057,4.504456,4.457689],[7.136663,-4.890232,-7.630372,5.578699,8.873598,-6.936539,9.588389,2.915465,-2.942176,8.848471,3.597383],[-7.277817,8.460508,-6.745709,-4.381361,8.119776,-1.698883,-2.498408,1.147645,-8.784729,8.102698,8.736755],[2.721643,-5.172449,-6.304984,-0.084959,-4.492864,2.578007,4.511328,6.080598,6.704015,-9.423593,-0.904844],[-8.758617,-4.962173,8.076481,3.194567,-3.708425,2.779458,4.331506,-3.308029,9.884886,-4.382695,7.772914],[-1.969720,4.643366,6.303436,0.359278,-3.454258,6.131802,7.354101,-3.974782,-5.806657,5.980934,4.307251],[6.574488,-4.774115,7.913326,-5.456264,0.731791,3.219506,-3.485970,-4.542073,-7.449601,-5.420708,3.138087],[-0.765379,-1.580129,2.474770,-0.337779,-9.244306,-6.827606,1.115204,4.842592,-3.302899,-5.712135,9.066900],[8.995032,4.822481,-7.606656,8.381359,2.174171,5.553745,-4.508911,9.173630,-2.066149,5.325781,-8.092548],[-5.199831,-4.663479,-4.850805,-2.021932,2.032474,4.325767,4.036292,-7.288485,-5.646948,6.663519,-5.491401],[-3.681205,-1.713145,9.578350,6.278502,-2.189395,-5.426267,7.319427,-3.765422,-8.454966,7.306414,-3.661966]],[[-6.785714,4.197546,-6.046112,-2.728818,3.123618,-8.955263,9.242592,6.509503,6.185220,-2.315566,-3.590357],[6.392277,6.748581,-5.868337,9.571610,-8.101466,-8.777773,-5.204904,-2.136442,3.923572,5.215544,5.106746],[2.416383,-9.700150,7.467565,-3.656844,-1.256636,-5.940735,-1.970158,-3.671220,4.163350,9.714900,-2.951204],[-5.736103,-2.585418,-8.775844,1.694917,9.866588,-2.537865,8.361117,-8.648374,6.763560,4.319641,6.758919],[6.047788,-1.687362,-1.827685,-3.718038,2.494603,0.118592,-3.946979,-5.379734,3.322137,-4.305008,0.225182],[4.246067,-8.783718,-6.744811,-3.555810,7.135241,8.563105,-5.426171,3.083602,-0.027135,6.311487,-6.960949],[-9.153148,6.501548,-7.221611,2.445537,-0.294290,-5.526868,-4.363209,-1.565214,-1.241966,-4.980593,1.414131],[2.432819,5.379185,-3.012070,6.306897,-7.936161,0.821449,5.660573,3.952631,0.829055,-1.936250,-6.321735],[-9.315821,4.301816,-8.277676,-1.969804,2.099565,-3.099600,1.502225,1.036233,-6.248352,-1.074001,-0.941821],[1.803267,2.588117,3.459915,-9.731637,-8.818447,-0.171044,6.676719,6.855192,6.160509,9.646452,6.843482],[-7.866165,5.790087,-0.213151,-3.179584,-7.790894,-6.736644,-4.024003,4.072176,-5.280869,7.795776,2.198227],[4.746459,-1.359236,9.690288,1.068782,-1.301400,-6.903788,-0.047029,-6.591885,7.640048,-7.815261,-2.777482],[1.930162,-4.799566,2.888524,-3.626992,-8.989558,2.365166,-4.161041,9.649028,4.532547,7.201492,6.492020],[-6.184147,-5.429462,-3.011229,9.116836,5.376571,-2.725294,-2.592627,5.866043,8.522221,7.865415,-8.185015],[4.439212,3.757106,-7.891122,-4.704507,-3.238864,4.601957,-0.486680,9.448792,-5.606813,-7.976185,-1.995378]],[[-2.985526,-4.542967,-3.733403,-2.124962,4.011439,-8.060663,-0.628125,-4.834935,-7.675526,3.114673,0.630385],[-5.953971,2.276382,-6.395556,3.989941,1.446894,-0.206383,3.021377,4.463122,-2.329056,-4.496379,8.679254],[9.123054,8.825928,-6.700568,9.608451,6.506473,-6.630929,-5.951181,-4.857874,-7.868368,5.844753,3.892893],[2.426630,-0.037758,-5.745973,-0.753651,5.981555,6.599377,0.620376,4.524276,9.426727,-8.157061,0.960212],[-3.548402,3.747430,0.196329,-4.950045,7.882043,7.003370,6.337881,-8.359183,9.331353,4.058617,2.958106],[-2.506679,5.960886,9.490438,-1.965789,-9.586498,-9.660293,1.183965,-8.854135,5.633014,1.372624,1.144562],[-5.270561,-0.126564,7.094334,-8.504341,-4.438963,5.197378,-3.147033,-2.926174,4.940103,-8.279468,-4.584799],[-9.201620,8.857044,-4.123259,-7.853370,7.519707,-0.191274,8.443051,9.294044,-8.086189,-7.469887,2.782560],[-0.454675,6.532170,-9.180270,2.606413,5.398656,8.303752,6.117156,7.255647,8.588069,-4.035861,-9.286234],[2.815082,1.924361,-1.158527,7.945940,5.559652,3.295647,6.978545,-3.252027,-2.059479,-6.614972,-5.438252],[8.248153,-8.387984,-8.349835,-3.089046,-1.544708,-3.881357,7.097029,8.192152,-7.624679,-1.897469,-5.318185],[9.886551,0.185653,-4.984388,6.047834,4.301887,5.219241,9.540899,5.337994,-7.138538,9.171554,8.647814],[2.197731,4.906967,0.778643,9.201917,1.714386,-8.109966,-0.294003,3.231661,9.526024,5.033736,-3.996869],[-2.399657,-3.550445,9.486313,7.246744,2.303394,4.061321,-8.681382,-3.334006,-1.749550,-5.679898,-5.665932],[-6.200802,-5.310925,0.506612,-2.603725,-7.067234,2.875382,6.936807,-4.934562,0.137165,-3.568436,-8.408683]],[[-4.129251,-4.143108,9.301134,9.113399,-0.540332,6.086256,-0.876652,-9.781578,-5.327243,5.719791,9.419657],[-0.829863,-1.650560,5.974924,-2.405893,9.447091,2.749972,-5.731271,3.972723,-2.097948,2.011912,-4.629716],[-2.761208,-9.805616,-7.125429,-2.059844,-2.289908,9.034278,5.986927,1.649021,7.534197,-8.042943,6.698426],[6.885189,-1.863553,-6.005841,5.069284,8.060883,7.761020,-8.189016,-5.853035,4.395935,2.762747,9.547738],[-9.124967,-5.547788,7.760911,-9.223382,1.394567,7.281210,2.290871,4.563949,3.364452,4.154480,-9.906598],[-6.669780,-7.905832,-2.591564,-5.882302,-2.397057,-4.524887,-4.947017,5.244213,-4.102481,-7.745819,3.079086],[5.530628,-1.913972,3.543010,8.371158,3.266921,-1.904343,-2.244560,4.286069,-5.394117,2.623004,2.393256],[9.931926,-2.596036,7.480443,1.304411,-5.729059,-9.621111,2.177506,-7.988548,9.946161,-8.428555,-2.598176],[-5.175098,-7.731893,1.626121,-2.302611,9.364309,-1.521831,9.113909,4.401187,-7.198695,-9.645979,-3.929611],[-8.408924,-4.932060,3.569627,-4.313209,8.215937,8.924406,1.618668,0.782762,0.428804,2.979051,-4.247714],[-9.411873,-0.995333,-9.229913,6.181945,-5.230083,5.967713,3.853407,-4.560717,-3.476097,6.112918,6.370867],[0.862088,-1.527563,8.174455,-2.837981,-4.438176,5.382445,1.676338,1.828357,5.460133,-5.415660,8.370351],[5.984211,1.145330,7.975042,7.967211,-2.355365,-1.371453,-1.629663,-8.092309,2.136930,5.082064,3.057570],[-9.660927,8.137581,5.144824,0.728134,0.946719,-4.690598,-3.136799,9.338481,-8.131180,-1.752105,-9.243648],[-5.364156,1.291478,-8.014559,2.329917,0.560737,-8.649849,1.896943,6.903569,-6.756396,6.204270,9.970823]],[[2.843156,6.422720,-9.988105,-4.953519,-7.680897,-9.780996,-7.476486,-4.024622,-6.801751,-0.030183,-4.630504],[-4.292220,-3.367598,2.712712,7.924544,3.961967,4.364629,-0.682581,7.818083,2.153107,-1.626947,2.832886],[-6.417211,-5.506005,-7.074633,7.868693,-9.321083,-8.560870,4.849371,-1.341029,-5.155442,3.019550,-0.396763],[-3.802541,-7.751104,-6.654825,3.436798,2.805297,1.676135,-3.173595,-7.850581,0.312441,-1.140065,1.452986],[4.894991,-2.997767,-2.029366,3.746205,-5.252399,-2.201383,1.235726,2.866556,-7.326930,-9.848586,-7.249441],[3.292131,4.008009,2.977342,-2.846217,7.007522,-9.869555,-9.990991,6.067683,2.196682,1.594256,-6.574565],[-5.982747,0.438882,-3.267369,0.247067,-8.567074,-9.542117,4.054405,1.991051,-9.334076,9.082344,4.494015],[5.600661,3.452179,-6.945356,-4.205375,-5.440102,-1.931260,-5.367631,9.214432,6.238669,-9.753197,6.989439],[3.042245,-5.385045,4.789080,-3.369455,2.890645,6.507069,-3.147342,0.253731,-4.317263,-9.023632,2.507800],[-0.296033,-4.847782,-5.660644,1.427480,-2.225440,2.306334,-6.914504,-9.722074,4.810847,7.661755,-6.565027],[-4.585343,-6.760492,7.849478,1.738118,5.395217,-7.394835,4.575461,7.042995,-7.676837,4.527426,-9.851619],[8.469817,-8.428640,-3.410069,8.942853,1.669267,-5.963383,4.954488,-7.046967,-8.448285,-3.922874,0.608543],[6.362433,-7.906738,-8.523258,1.778911,4.394584,2.462077,3.686945,7.163985,5.806178,-4.975974,5.718432],[8.020976,-5.387699,1.618967,-8.998478,-0.854137,1.690495,-6.898350,-2.843074,-5.159784,-0.199579,0.109083],[9.431387,-8.234297,-0.271075,-9.802501,-0.959348,0.931957,6.199694,8.681182,-3.871339,-7.331598,-9.461562]]], dtype = "float64")#candidate|5665|(7, 15, 11)|const|float64
const_5666 = relay.const([[[-9.395169,3.441577,-3.418565,3.796585,2.808641,-7.764179,-7.770821,9.797789,-2.534000,-8.685759,-0.817650],[-6.120139,6.429667,-7.659588,2.140336,7.202869,-5.769014,-2.388495,6.928538,-3.970918,2.064339,-7.890932],[-9.198797,1.931895,7.111481,-4.056671,7.260714,-2.060767,3.017671,5.010800,-2.932621,2.036806,7.459427],[0.961219,4.497434,6.141122,-6.067057,-5.845319,-9.801300,-6.837722,4.978467,2.855385,6.477428,-5.806472],[-9.146510,6.461410,-2.712153,4.377651,-1.879019,-1.023098,0.057797,-3.131583,-1.603482,-2.388745,-3.439653],[-8.183092,8.779227,4.085697,8.954714,-8.478707,3.674003,-3.432574,-5.811433,4.255034,1.505469,-6.728397],[4.349075,-8.494760,1.225718,-2.871883,5.721393,-2.445645,-7.163417,4.391948,1.048773,-8.150749,6.384364],[-9.946138,-1.325125,-6.767153,1.130288,-2.800970,-0.164112,-1.082458,5.338075,0.356299,9.016534,-0.600620],[4.645630,4.027602,4.567464,5.281384,6.502251,-7.341726,6.117194,5.205895,2.404596,-4.801259,-7.303832],[4.821096,1.437753,1.137531,-1.102037,9.920436,9.337203,-0.703569,-7.584357,-7.136776,8.863512,8.879097],[3.080503,-6.733068,4.101451,-6.261812,4.192344,5.589342,4.199822,-1.074327,-7.769449,0.162859,-1.714127],[-5.170148,-1.630506,-1.017605,5.068093,-7.435202,-1.138975,8.100444,8.830728,-3.505486,-2.001022,-1.641644],[-4.868661,9.196027,-4.629891,-0.590826,5.689921,0.996122,3.887216,0.538591,0.687847,-5.548084,-6.005725],[5.700318,1.457776,7.864758,-1.859249,7.443346,-3.014848,3.521219,-9.372155,6.922595,3.246176,2.150040],[7.707087,3.476918,-2.295198,-7.925391,-6.116410,8.471963,2.962310,3.318341,-0.220085,-9.890863,4.896822]],[[7.560337,-6.218263,2.475112,5.369965,-8.609080,-3.452901,6.490535,9.571308,3.287623,-9.895781,-9.229968],[2.529527,7.120379,-5.676236,-5.447531,0.071779,7.718844,5.545495,9.906592,0.622553,8.144914,-0.144625],[4.801247,-5.167839,9.562803,1.718814,6.502806,2.693714,-5.085824,-4.605329,1.096052,-7.419467,1.444225],[-5.005401,-5.797088,6.726673,4.189568,-9.224544,4.032464,8.619299,9.999520,-8.771162,-4.745219,7.395663],[-7.210904,7.909733,-3.697303,-3.104089,3.940924,-7.423665,1.248346,4.655988,2.287428,4.175028,6.355567],[6.512354,3.033289,1.661556,7.740482,-7.479993,-5.773022,-2.006862,4.225592,6.544569,9.733084,-5.664894],[2.547921,1.730915,0.580463,7.616833,1.133305,-6.338798,5.885723,-1.380689,-8.212949,-3.685498,7.393167],[3.696492,5.163863,4.755772,5.712988,2.801056,-6.970250,1.266260,0.742471,-7.701477,-6.387661,2.471289],[-5.779251,-1.544475,-1.994582,1.848610,6.331714,-1.975060,8.104756,7.548991,1.986310,2.593850,0.236163],[-4.742486,-7.366487,-3.076313,1.934780,-8.403483,0.249810,-2.973226,9.346531,5.356546,2.473964,3.086404],[-2.965314,2.626099,-1.878978,8.850481,9.924541,-1.993880,-5.090786,-6.385940,2.619093,9.102532,-0.509043],[-4.352020,2.381153,-6.521019,-2.828615,-4.488046,7.748625,-1.776045,-8.012035,4.357308,6.889482,4.853371],[-9.417757,7.664574,-9.224455,6.535944,9.564049,-2.837757,8.084949,4.864465,7.502916,-3.120931,5.739453],[-2.824934,-8.145755,7.381367,6.610278,1.021472,2.739716,6.653240,7.303228,-5.731142,8.757095,-2.039646],[6.857223,-8.781225,5.020082,9.070869,9.824671,-7.726167,-4.504090,-6.065111,9.918739,5.300620,-8.292706]],[[-6.363180,9.037858,-3.824349,-9.699093,-7.520626,-4.355556,-3.640319,6.436758,-8.015788,0.438507,5.610084],[2.257926,6.337330,3.878909,9.786505,-2.491442,-4.250549,-7.068885,-4.725281,0.948005,-4.205074,3.943134],[0.966972,1.964503,7.268702,-2.286063,-0.867061,-7.163023,-2.188868,-1.644790,-3.730564,-3.675541,0.913811],[1.944904,1.363426,-6.833966,8.182834,-4.538233,-1.305354,-3.375587,-6.130223,-2.744543,-1.654452,-3.046006],[1.410102,-5.348067,5.250876,-0.313701,3.920073,-3.915898,-0.195032,1.983182,-0.879029,-4.343826,1.404544],[0.450330,9.622906,-3.690106,-9.986598,6.732170,0.599442,9.814310,-8.231590,8.516350,-6.805182,-1.479090],[-8.293878,-5.186126,0.926019,-2.944860,2.123525,-2.132995,1.696465,1.894561,3.199012,0.574562,-4.515017],[-5.108892,-7.629230,8.039564,7.161765,7.654069,0.787533,2.668835,-3.467535,6.912395,0.670790,2.635443],[-8.204534,-2.358319,3.592078,-6.086167,0.163391,-1.117144,1.658908,-5.209681,8.186890,-0.240279,8.924338],[6.212871,5.388909,5.771600,-9.704995,-3.561195,3.619297,-0.640778,-3.990830,2.984875,9.911360,-0.726080],[7.971718,-5.901000,-2.491574,7.152955,-3.346948,-7.335440,5.651111,-7.493551,-7.547602,-2.120317,2.104473],[-5.666989,4.846832,7.164379,9.085799,8.729510,-8.088830,8.539498,9.147330,-7.504160,1.448323,5.323191],[1.759950,-0.370636,-9.046822,2.412613,4.957988,-9.506811,3.080403,-4.854325,2.677126,1.422401,7.575968],[-0.577364,0.004815,-6.208665,4.782851,8.313989,0.914630,-3.158480,-3.526911,6.137569,2.085003,1.573879],[-5.360741,0.264089,7.151178,3.417253,0.602382,8.663078,5.342290,6.925653,-3.434572,2.039548,-1.799151]],[[5.045112,4.452277,3.050442,-5.293240,-5.668763,-2.431193,-4.758125,-8.456457,-3.811737,-0.160551,8.276401],[3.440491,-3.603264,8.268203,2.259781,-1.748681,1.394223,7.049315,-5.052909,2.061708,-6.095181,5.170014],[9.438138,1.860233,9.139616,-6.984829,8.243976,-0.392344,4.654439,3.070331,5.722049,4.120329,4.628504],[1.053742,4.836361,-4.302874,-6.000300,-4.902455,-2.061365,2.513006,9.909984,-1.553453,6.995985,6.416236],[-5.562794,8.674111,-0.397256,-0.548345,-8.107564,6.981699,-1.860540,8.384027,6.814268,9.774902,7.555122],[-9.613475,-9.048261,8.955665,6.575966,-8.079162,3.947780,3.780509,-2.183703,-6.214270,-2.268130,-6.370079],[6.822763,0.674200,-0.283052,-9.736888,-6.617802,-5.311023,1.470110,-0.426575,-1.615452,7.682182,1.220959],[6.733222,-9.535009,-6.497139,-7.261053,-0.358217,-7.216310,-4.878578,-1.863498,9.436692,3.071177,4.661998],[2.592858,7.823954,-0.058072,-7.998443,-2.317084,7.348694,6.420272,2.720355,2.102542,3.450137,4.582961],[-1.149610,2.250895,-4.070941,0.464854,3.596351,-4.193356,7.997088,9.212965,-0.616397,5.208254,7.231887],[4.424323,-5.505436,-0.560396,-0.195072,-5.591689,1.895365,-9.441158,-8.030774,1.471174,1.598319,3.324264],[-5.878851,-7.045462,-9.207894,-1.485598,-9.786131,-2.424604,-9.537533,-9.984810,-8.734459,2.485581,-0.678659],[-8.345941,-8.004604,8.439798,1.024537,-1.596220,5.303058,-9.543908,-2.478732,0.114870,-0.047819,-1.474662],[-8.045885,1.881450,1.902441,-9.900793,6.251589,-6.633373,-0.898294,5.137982,-9.523311,4.683735,-0.559329],[8.710185,9.346837,9.018455,-8.727124,-3.019340,-7.254090,-1.930083,3.153225,-2.780194,2.092636,-2.674428]],[[-7.655974,7.780240,2.222231,-7.206201,-9.506649,-3.648876,4.717315,8.076359,3.373244,-5.914180,0.096595],[9.747183,-6.853528,5.181624,6.679270,7.960874,3.077148,-4.259028,-3.137500,-4.681318,0.243736,-8.048602],[-0.314432,-2.963042,2.648014,-6.517192,0.995321,3.094273,8.347014,0.295431,-6.199830,-6.382576,2.685186],[-0.331733,7.391458,-2.396963,-3.656785,5.797577,-5.392275,-8.198337,0.976229,4.143460,6.723447,-9.095658],[2.139352,5.506318,-4.779815,-9.664742,-7.989227,3.355513,2.593755,-4.111811,-7.457796,9.168918,-2.094810],[0.671214,-7.330757,-1.638950,2.904619,-3.915756,7.432773,2.085571,1.432407,4.909801,-7.849288,4.123095],[9.383892,8.929676,-9.203772,-8.402533,4.521978,-3.352420,-0.951739,6.094091,7.923886,0.176938,0.399028],[-3.143741,-9.270793,-4.068483,3.589203,-8.229245,-0.426696,-8.726688,-9.280059,6.415589,-9.407859,7.750513],[-2.778806,2.276713,-7.995383,-4.164708,8.317889,-1.200828,2.533408,-4.895525,7.868513,1.512252,6.994176],[-2.899718,-7.370843,4.118575,6.056806,-3.201802,4.461686,4.816405,-3.519025,0.253225,-9.583234,1.036111],[-9.335373,-5.973195,-2.311279,9.344032,-1.846336,-5.748717,4.150046,8.638561,-5.429811,2.943411,6.357778],[-3.168760,-1.842510,0.030004,3.175867,-0.477323,2.570448,5.990121,-8.953745,1.608989,-1.198731,-9.621309],[6.993914,-9.999241,7.311701,4.530888,-7.255916,-9.780702,0.587136,-8.553817,-0.109369,-0.352527,4.592062],[0.708583,2.383344,-9.214917,-0.976617,4.709349,0.994039,-6.686411,5.656172,5.443623,7.767514,7.937220],[-5.980918,5.004210,-8.772703,-6.835920,-8.858278,-0.994776,-3.767240,1.727594,3.192415,-8.269168,4.539759]],[[0.009772,-2.824693,-6.497312,-6.920402,-2.195252,6.931655,7.935610,9.730727,-4.546733,8.650961,2.338964],[3.541103,3.689430,-5.331896,3.252896,-1.831990,-3.083649,-5.912170,-5.157136,-1.981652,0.925590,-2.617992],[-2.043451,-8.150012,9.788173,8.299189,2.258726,-3.310747,7.429273,-9.835653,-6.155435,3.415408,7.912505],[0.880349,-9.774975,-4.149794,-2.195491,-3.274168,-3.714649,0.592944,-2.480327,3.529995,3.789212,-8.481519],[-1.268726,-3.638983,5.498099,1.781198,0.550228,-9.374187,2.281031,3.510830,-0.792668,-7.633764,-4.668867],[-4.543085,-9.099334,-4.798473,0.585621,-1.254832,0.194001,-0.806860,-0.349442,6.999621,7.822585,3.122877],[-4.224916,-4.297515,-1.577717,8.579992,-5.795307,1.512020,9.045460,-9.960045,7.072272,-2.374782,5.398168],[8.295488,0.165719,1.921533,1.083917,2.225082,0.320185,-8.726330,-5.070050,-1.250786,6.042119,0.686850],[8.895611,-4.841780,-0.963299,7.881414,9.881916,6.813172,0.054079,3.276196,4.644771,-0.541421,-0.836741],[-5.915571,5.068725,8.110794,-3.076871,4.065696,6.467370,-0.583308,3.111053,3.185972,0.519054,1.856520],[-7.133042,6.248841,8.861623,-0.449708,-6.772612,-9.092965,-5.654132,-8.083484,-7.571881,-1.949043,7.356664],[5.197987,6.455933,-3.853871,8.056257,8.125808,-8.616356,7.387284,2.825236,-2.638523,-3.381604,4.959131],[-8.418676,9.803244,1.228901,-4.572499,2.157884,8.189140,4.911740,8.304898,0.295164,-2.861974,7.774008],[1.975997,6.678810,-4.349249,-6.046573,-4.215151,8.276269,7.984753,-1.959717,-3.494761,0.174752,-3.485553],[3.830416,0.905889,-3.038727,-1.099187,7.872974,-8.853680,9.343875,-4.649513,-6.978944,8.361771,7.534128]],[[4.650107,-4.262716,0.993955,7.169293,-5.115497,9.852181,-2.988530,6.577199,7.697286,-5.541283,-7.742119],[-7.278412,-7.652396,3.591061,-0.258157,-7.595301,-0.758675,7.111178,2.852126,0.764703,6.056745,5.983191],[3.895452,7.218790,-0.325718,-0.647849,5.066322,8.944844,-9.461643,2.710423,2.636359,-7.602255,2.694723],[6.494366,-4.395085,-9.933032,3.517595,3.558140,6.495120,1.634423,9.471825,-4.011285,-5.582362,-5.976912],[-1.480897,-3.732937,5.144598,-7.801350,-3.251056,0.816792,-0.217783,9.063197,-2.313021,-8.013333,2.467108],[3.780998,-2.683763,2.054851,9.697406,5.645649,-9.604489,-1.576945,-2.976250,-3.260880,-0.924091,1.530170],[9.038710,7.247642,-3.026621,4.258435,7.715097,-3.152521,-6.774245,8.726288,4.860904,-1.256816,-4.700011],[5.404903,3.368392,3.763331,-7.888429,-0.888619,7.714385,0.400597,-9.502776,6.225516,7.070952,1.598829],[-5.822174,0.055435,3.487386,3.022846,-6.970138,-7.865017,-1.239266,-1.495294,-7.025046,-3.155558,-2.105722],[1.341851,1.607359,-9.089061,-4.475686,-7.295031,-4.148946,-2.509502,0.843639,1.779254,5.365550,1.068530],[-8.245274,-5.773724,9.873796,-7.817391,-2.766213,-3.918162,0.023578,-8.492007,-1.971535,-0.745444,-8.362683],[-7.833815,-2.356468,-6.906841,0.096325,7.142502,1.826726,-7.852137,-3.983360,-3.250451,9.646013,-1.826732],[3.957713,-4.925592,-9.919159,3.334423,-7.690425,-3.290491,1.008406,-0.285704,6.624060,-5.085611,8.378330],[2.603227,-4.567977,-7.195441,-5.995608,-4.133999,2.700364,1.023400,3.461305,-5.542720,-2.993456,-8.940090],[2.539875,-9.187106,-5.998364,8.864370,1.962256,8.327356,-3.173407,6.527088,1.944657,1.565421,0.630737]]], dtype = "float64")#candidate|5666|(7, 15, 11)|const|float64
bop_5667 = relay.less(const_5665.astype('bool'), relay.reshape(const_5666.astype('bool'), relay.shape_of(const_5665))) # shape=(7, 15, 11)
bop_5676 = relay.equal(const_5666.astype('bool'), relay.reshape(const_5665.astype('bool'), relay.shape_of(const_5666))) # shape=(7, 15, 11)
func_5124_call = mod.get_global_var('func_5124')
func_5125_call = mutated_mod.get_global_var('func_5125')
call_5687 = relay.TupleGetItem(func_5124_call(), 0)
call_5688 = relay.TupleGetItem(func_5125_call(), 0)
uop_5689 = relay.cos(bop_5676.astype('float64')) # shape=(7, 15, 11)
func_1330_call = mod.get_global_var('func_1330')
func_1332_call = mutated_mod.get_global_var('func_1332')
const_5695 = relay.const([2,10,-1,-3,-7,-1], dtype = "int32")#candidate|5695|(6,)|const|int32
call_5694 = func_1330_call(relay.reshape(const_5695.astype('int32'), [3, 1, 2]))
call_5696 = func_1330_call(relay.reshape(const_5695.astype('int32'), [3, 1, 2]))
uop_5698 = relay.asin(uop_5689.astype('float64')) # shape=(7, 15, 11)
bop_5704 = relay.floor_divide(uop_5698.astype('float32'), relay.reshape(const_5665.astype('float32'), relay.shape_of(uop_5698))) # shape=(7, 15, 11)
uop_5707 = relay.sin(uop_5698.astype('float64')) # shape=(7, 15, 11)
func_4258_call = mod.get_global_var('func_4258')
func_4262_call = mutated_mod.get_global_var('func_4262')
const_5711 = relay.const([9,4,-2,7,-4,2,7,-6,5,-10,10,-5,8,7,4,-7,9,-6,-6,-2,-3,-8,-6,-7,-2,5,1,-3,9,-7,5,-7,5,7,8,10,4,2,-4,10,5,8,-5,-7,2,-9,-9,-1,-10,6,8,9,-5,1,-1,-5,-8,2,-3,-10,-6,2,-5,-10,1,-3,5,10,-5,9,-2,10,-7,-3,-5,7,-2,-7,-2,-2,-4,-4,6,-8,5,-5,-4,-6,1,-3,-2,8,-9,-9,-1,-6,5,-5,-5,4,-4,6,-7,-1,4,3,-6,10,-5,10,9,2,-5,-8,3,10,-2,7,3,-6,-4,2,1,7,10,-1,-3,-4,-1,1,-6,-1,-1,8,6,10,-4,-2,-2,-10,-8,1,5,4,-2,1,-7,-6,3,-4,-9,-1,-5,-9,-3,9,-1,5,-10,3,-3,9,9,2,-9,-10,-9,1,-5,-2,1,-10,-6,6,5,7,4,-9,1,-4,6,-7,7,10,10,8,3,-2,4,-4,-9,-6,7,7,-9,-6,-7,9,-5,-3,10,6,3,4,-10,-8,-9,4,-2,-4,4,-5,5,4,-4,6,-10,9,2,1,-2,-3,-3,-9,-1,-5,2,-5,-3,-8,-6,1,7,-7,5,-5,7,10,-6,-5,9,-4,-2,-10,8,4,-2,-1,-6,10,-8,-8,2,5,4,-8,3,-8,1,-10,7,4,-10,10,5,9,4,8,-5,7,6,4,7,2,1,-8,7,-8,9,5,8,7,1,-10,-10,-6,2,6,4,-7,2,-3,-7,8,-9,-10,-8,10,2,-6,7,-1,-3,-8,4,2,-9,9,-8,-2,1,-3,-8,-8,3,7,5,-8,-4,5,-10,-8,-4,6,3,8,-9,2,-5,8,-4,7,2,10,-2,5,-4,4,9,1,-6,-5,1,2,10,4,-6,5,-8,5,-2,3,-5,-5,5,-6,4,-7,1,-10,3,4,5,-9,-6,3,7,5,3,6,-3,-10,-6,-1,10,7,-5,3,10,-3,8,-6,3,9,-1,-3,-9,-3,-2,1,6,-5,9,-3,2,7,3,5,5,10,-8,10,8,4,10,3,-5,6,-6,5,4,-6,-5,1,-6,8,7,-3,3,-6,5,6,-8,6,-3,2,10,4,-10,9,-9,-9,-5,1,2,-9,-7,-8,1,-6,2,-4,7,-2,-7,2,8,-2,4,10,-1,4,8,-10,4,5,-6,-10,7,10,3,-9,5,-3,-5,6,4,3,-10,10,2,1,2,-3,-5,4,4,10,-7,8,-8,9,4,3,-6,9,-6,-8,-4,-1,1,-1,-9,6,-6,7,1,-3,7,-1,8,-2,10,5,8,-7,1,8,8,7,10,-7,1,8,-7,2,-6,-10,-4,-4,-2,3,-8,-3,-5], dtype = "uint16")#candidate|5711|(525,)|const|uint16
var_5712 = relay.var("var_5712", dtype = "float32", shape = (10, 42))#candidate|5712|(10, 42)|var|float32
call_5710 = relay.TupleGetItem(func_4258_call(relay.reshape(const_5711.astype('uint16'), [7, 15, 5]), relay.reshape(const_5711.astype('uint16'), [7, 15, 5]), relay.reshape(var_5712.astype('float32'), [420,]), ), 1)
call_5713 = relay.TupleGetItem(func_4262_call(relay.reshape(const_5711.astype('uint16'), [7, 15, 5]), relay.reshape(const_5711.astype('uint16'), [7, 15, 5]), relay.reshape(var_5712.astype('float32'), [420,]), ), 1)
uop_5714 = relay.tan(uop_5707.astype('float64')) # shape=(7, 15, 11)
func_4929_call = mod.get_global_var('func_4929')
func_4932_call = mutated_mod.get_global_var('func_4932')
var_5728 = relay.var("var_5728", dtype = "bool", shape = (240,))#candidate|5728|(240,)|var|bool
call_5727 = relay.TupleGetItem(func_4929_call(relay.reshape(var_5728.astype('bool'), [4, 12, 5]), relay.reshape(var_5728.astype('bool'), [4, 12, 5]), ), 2)
call_5729 = relay.TupleGetItem(func_4932_call(relay.reshape(var_5728.astype('bool'), [4, 12, 5]), relay.reshape(var_5728.astype('bool'), [4, 12, 5]), ), 2)
var_5731 = relay.var("var_5731", dtype = "uint16", shape = (525,))#candidate|5731|(525,)|var|uint16
bop_5732 = relay.left_shift(const_5711.astype('uint32'), relay.reshape(var_5731.astype('uint32'), relay.shape_of(const_5711))) # shape=(525,)
output = relay.Tuple([bop_5667,call_5687,call_5694,const_5695,bop_5704,call_5710,var_5712,uop_5714,call_5727,var_5728,bop_5732,])
output2 = relay.Tuple([bop_5667,call_5688,call_5696,const_5695,bop_5704,call_5713,var_5712,uop_5714,call_5729,var_5728,bop_5732,])
func_5736 = relay.Function([var_5712,var_5728,var_5731,], output)
mod['func_5736'] = func_5736
mod = relay.transform.InferType()(mod)
mutated_mod['func_5736'] = func_5736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5736_call = mutated_mod.get_global_var('func_5736')
var_5738 = relay.var("var_5738", dtype = "float32", shape = (10, 42))#candidate|5738|(10, 42)|var|float32
var_5739 = relay.var("var_5739", dtype = "bool", shape = (240,))#candidate|5739|(240,)|var|bool
var_5740 = relay.var("var_5740", dtype = "uint16", shape = (525,))#candidate|5740|(525,)|var|uint16
call_5737 = func_5736_call(var_5738,var_5739,var_5740,)
output = call_5737
func_5741 = relay.Function([var_5738,var_5739,var_5740,], output)
mutated_mod['func_5741'] = func_5741
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5743 = relay.var("var_5743", dtype = "float32", shape = (6, 9, 10))#candidate|5743|(6, 9, 10)|var|float32
var_5744 = relay.var("var_5744", dtype = "float32", shape = (6, 9, 10))#candidate|5744|(6, 9, 10)|var|float32
bop_5745 = relay.power(var_5743.astype('float32'), relay.reshape(var_5744.astype('float32'), relay.shape_of(var_5743))) # shape=(6, 9, 10)
uop_5751 = relay.log2(var_5744.astype('float32')) # shape=(6, 9, 10)
bop_5756 = relay.bitwise_and(uop_5751.astype('int16'), relay.reshape(var_5743.astype('int16'), relay.shape_of(uop_5751))) # shape=(6, 9, 10)
output = relay.Tuple([bop_5745,bop_5756,])
output2 = relay.Tuple([bop_5745,bop_5756,])
func_5766 = relay.Function([var_5743,var_5744,], output)
mod['func_5766'] = func_5766
mod = relay.transform.InferType()(mod)
var_5767 = relay.var("var_5767", dtype = "float32", shape = (6, 9, 10))#candidate|5767|(6, 9, 10)|var|float32
var_5768 = relay.var("var_5768", dtype = "float32", shape = (6, 9, 10))#candidate|5768|(6, 9, 10)|var|float32
output = func_5766(var_5767,var_5768,)
func_5769 = relay.Function([var_5767,var_5768,], output)
mutated_mod['func_5769'] = func_5769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2923_call = mod.get_global_var('func_2923')
func_2925_call = mutated_mod.get_global_var('func_2925')
call_5771 = relay.TupleGetItem(func_2923_call(), 0)
call_5772 = relay.TupleGetItem(func_2925_call(), 0)
output = relay.Tuple([call_5771,])
output2 = relay.Tuple([call_5772,])
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
func_5443_call = mod.get_global_var('func_5443')
func_5444_call = mutated_mod.get_global_var('func_5444')
call_5817 = relay.TupleGetItem(func_5443_call(), 0)
call_5818 = relay.TupleGetItem(func_5444_call(), 0)
uop_5826 = relay.log(call_5817.astype('float64')) # shape=(6, 30)
uop_5828 = relay.log(call_5818.astype('float64')) # shape=(6, 30)
output = uop_5826
output2 = uop_5828
func_5845 = relay.Function([], output)
mod['func_5845'] = func_5845
mod = relay.transform.InferType()(mod)
mutated_mod['func_5845'] = func_5845
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5845_call = mutated_mod.get_global_var('func_5845')
call_5846 = func_5845_call()
output = call_5846
func_5847 = relay.Function([], output)
mutated_mod['func_5847'] = func_5847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3530_call = mod.get_global_var('func_3530')
func_3531_call = mutated_mod.get_global_var('func_3531')
call_5864 = func_3530_call()
call_5865 = func_3530_call()
output = call_5864
output2 = call_5865
func_5872 = relay.Function([], output)
mod['func_5872'] = func_5872
mod = relay.transform.InferType()(mod)
output = func_5872()
func_5873 = relay.Function([], output)
mutated_mod['func_5873'] = func_5873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5012_call = mod.get_global_var('func_5012')
func_5014_call = mutated_mod.get_global_var('func_5014')
call_5972 = relay.TupleGetItem(func_5012_call(), 0)
call_5973 = relay.TupleGetItem(func_5014_call(), 0)
output = call_5972
output2 = call_5973
func_5975 = relay.Function([], output)
mod['func_5975'] = func_5975
mod = relay.transform.InferType()(mod)
output = func_5975()
func_5976 = relay.Function([], output)
mutated_mod['func_5976'] = func_5976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5429_call = mod.get_global_var('func_5429')
func_5431_call = mutated_mod.get_global_var('func_5431')
call_6015 = func_5429_call()
call_6016 = func_5429_call()
uop_6032 = relay.asin(call_6015.astype('float32')) # shape=(15, 4, 3)
uop_6034 = relay.asin(call_6016.astype('float32')) # shape=(15, 4, 3)
uop_6036 = relay.atanh(uop_6032.astype('float32')) # shape=(15, 4, 3)
uop_6038 = relay.atanh(uop_6034.astype('float32')) # shape=(15, 4, 3)
uop_6045 = relay.erf(uop_6032.astype('float32')) # shape=(15, 4, 3)
uop_6047 = relay.erf(uop_6034.astype('float32')) # shape=(15, 4, 3)
output = relay.Tuple([uop_6036,uop_6045,])
output2 = relay.Tuple([uop_6038,uop_6047,])
func_6050 = relay.Function([], output)
mod['func_6050'] = func_6050
mod = relay.transform.InferType()(mod)
mutated_mod['func_6050'] = func_6050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6050_call = mutated_mod.get_global_var('func_6050')
call_6051 = func_6050_call()
output = call_6051
func_6052 = relay.Function([], output)
mutated_mod['func_6052'] = func_6052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6050_call = mod.get_global_var('func_6050')
func_6052_call = mutated_mod.get_global_var('func_6052')
call_6066 = relay.TupleGetItem(func_6050_call(), 0)
call_6067 = relay.TupleGetItem(func_6052_call(), 0)
output = call_6066
output2 = call_6067
func_6073 = relay.Function([], output)
mod['func_6073'] = func_6073
mod = relay.transform.InferType()(mod)
mutated_mod['func_6073'] = func_6073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6073_call = mutated_mod.get_global_var('func_6073')
call_6074 = func_6073_call()
output = call_6074
func_6075 = relay.Function([], output)
mutated_mod['func_6075'] = func_6075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3530_call = mod.get_global_var('func_3530')
func_3531_call = mutated_mod.get_global_var('func_3531')
call_6112 = func_3530_call()
call_6113 = func_3530_call()
output = call_6112
output2 = call_6113
func_6135 = relay.Function([], output)
mod['func_6135'] = func_6135
mod = relay.transform.InferType()(mod)
mutated_mod['func_6135'] = func_6135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6135_call = mutated_mod.get_global_var('func_6135')
call_6136 = func_6135_call()
output = call_6136
func_6137 = relay.Function([], output)
mutated_mod['func_6137'] = func_6137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4229_call = mod.get_global_var('func_4229')
func_4230_call = mutated_mod.get_global_var('func_4230')
call_6190 = relay.TupleGetItem(func_4229_call(), 1)
call_6191 = relay.TupleGetItem(func_4230_call(), 1)
var_6201 = relay.var("var_6201", dtype = "uint16", shape = (6, 30))#candidate|6201|(6, 30)|var|uint16
bop_6202 = relay.not_equal(call_6190.astype('bool'), relay.reshape(var_6201.astype('bool'), relay.shape_of(call_6190))) # shape=(6, 30)
bop_6205 = relay.not_equal(call_6191.astype('bool'), relay.reshape(var_6201.astype('bool'), relay.shape_of(call_6191))) # shape=(6, 30)
output = relay.Tuple([bop_6202,])
output2 = relay.Tuple([bop_6205,])
func_6211 = relay.Function([var_6201,], output)
mod['func_6211'] = func_6211
mod = relay.transform.InferType()(mod)
var_6212 = relay.var("var_6212", dtype = "uint16", shape = (6, 30))#candidate|6212|(6, 30)|var|uint16
output = func_6211(var_6212)
func_6213 = relay.Function([var_6212], output)
mutated_mod['func_6213'] = func_6213
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3554_call = mod.get_global_var('func_3554')
func_3556_call = mutated_mod.get_global_var('func_3556')
call_6268 = relay.TupleGetItem(func_3554_call(), 1)
call_6269 = relay.TupleGetItem(func_3556_call(), 1)
output = relay.Tuple([call_6268,])
output2 = relay.Tuple([call_6269,])
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
var_6278 = relay.var("var_6278", dtype = "float32", shape = (4, 2, 12))#candidate|6278|(4, 2, 12)|var|float32
uop_6279 = relay.sigmoid(var_6278.astype('float32')) # shape=(4, 2, 12)
func_3554_call = mod.get_global_var('func_3554')
func_3556_call = mutated_mod.get_global_var('func_3556')
call_6286 = relay.TupleGetItem(func_3554_call(), 0)
call_6287 = relay.TupleGetItem(func_3556_call(), 0)
output = relay.Tuple([uop_6279,call_6286,])
output2 = relay.Tuple([uop_6279,call_6287,])
func_6293 = relay.Function([var_6278,], output)
mod['func_6293'] = func_6293
mod = relay.transform.InferType()(mod)
mutated_mod['func_6293'] = func_6293
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6294 = relay.var("var_6294", dtype = "float32", shape = (4, 2, 12))#candidate|6294|(4, 2, 12)|var|float32
func_6293_call = mutated_mod.get_global_var('func_6293')
call_6295 = func_6293_call(var_6294)
output = call_6295
func_6296 = relay.Function([var_6294], output)
mutated_mod['func_6296'] = func_6296
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6349 = relay.var("var_6349", dtype = "float64", shape = (16, 8, 1))#candidate|6349|(16, 8, 1)|var|float64
uop_6350 = relay.log(var_6349.astype('float64')) # shape=(16, 8, 1)
var_6352 = relay.var("var_6352", dtype = "float64", shape = (16, 8, 8))#candidate|6352|(16, 8, 8)|var|float64
bop_6353 = relay.logical_xor(var_6349.astype('uint8'), var_6352.astype('uint8')) # shape=(16, 8, 8)
output = relay.Tuple([uop_6350,bop_6353,])
output2 = relay.Tuple([uop_6350,bop_6353,])
F = relay.Function([var_6349,var_6352,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_6349,var_6352,], output2)
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
