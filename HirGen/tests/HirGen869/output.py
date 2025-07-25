import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_633 = relay.var("var_633", dtype = "uint64", shape = (4, 5, 8))#candidate|633|(4, 5, 8)|var|uint64
var_634 = relay.var("var_634", dtype = "uint64", shape = (4, 5, 8))#candidate|634|(4, 5, 8)|var|uint64
bop_635 = relay.not_equal(var_633.astype('bool'), relay.reshape(var_634.astype('bool'), relay.shape_of(var_633))) # shape=(4, 5, 8)
output = relay.Tuple([bop_635,])
output2 = relay.Tuple([bop_635,])
func_697 = relay.Function([var_633,var_634,], output)
mod['func_697'] = func_697
mod = relay.transform.InferType()(mod)
mutated_mod['func_697'] = func_697
mutated_mod = relay.transform.InferType()(mutated_mod)
func_697_call = mutated_mod.get_global_var('func_697')
var_699 = relay.var("var_699", dtype = "uint64", shape = (4, 5, 8))#candidate|699|(4, 5, 8)|var|uint64
var_700 = relay.var("var_700", dtype = "uint64", shape = (4, 5, 8))#candidate|700|(4, 5, 8)|var|uint64
call_698 = func_697_call(var_699,var_700,)
output = call_698
func_701 = relay.Function([var_699,var_700,], output)
mutated_mod['func_701'] = func_701
mutated_mod = relay.transform.InferType()(mutated_mod)
const_937 = relay.const([[[-8.685961,8.966655,9.190684,6.844387,0.727451,5.681121,5.935616,2.795748,3.059952,-3.610591,9.763461,2.828027,2.641544]],[[0.601052,3.593349,-7.552300,6.043915,1.225555,8.431996,0.566931,1.596083,3.912554,-8.947935,0.294713,8.102651,-0.972152]],[[-5.730634,-2.850386,-9.094948,-6.526427,-1.309657,1.219564,-2.998016,5.332889,6.153080,8.445205,3.076543,3.893719,9.821212]],[[0.827774,-4.782910,9.572963,-6.059895,-0.422146,-9.799745,-9.774005,9.246970,-0.979094,-5.156911,8.525022,9.635156,2.874137]]], dtype = "float64")#candidate|937|(4, 1, 13)|const|float64
var_938 = relay.var("var_938", dtype = "float64", shape = (4, 16, 13))#candidate|938|(4, 16, 13)|var|float64
bop_939 = relay.equal(const_937.astype('bool'), var_938.astype('bool')) # shape=(4, 16, 13)
func_697_call = mod.get_global_var('func_697')
func_701_call = mutated_mod.get_global_var('func_701')
const_952 = relay.const([[9],[-2],[4],[4],[1],[-1],[7],[7],[6],[-9],[-3],[9],[-1],[10],[6],[8],[-3],[-4],[-10],[-8],[10],[-1],[9],[-6],[-4],[-6],[-7],[6],[9],[10],[1],[1],[-2],[2],[-5],[4],[2],[-10],[-3],[-6],[5],[-6],[10],[10],[10],[-3],[2],[7],[-8],[8],[1],[-9],[-7],[-4],[7],[-7],[-5],[-5],[-5],[-2],[-7],[-5],[8],[-4],[1],[10],[-4],[-5],[-9],[-1],[-2],[-1],[9],[9],[2],[-8],[6],[-9],[5],[3],[-5],[-10],[-3],[10],[-5],[-8],[-7],[-3],[4],[-2],[-3],[5],[-4],[-8],[-8],[-9],[-5],[2],[5],[9],[2],[6],[-6],[-6],[10],[7],[8],[7],[-8],[3],[7],[1],[-2],[-7],[6],[4],[3],[5],[-10],[10],[-1],[-7],[2],[-3],[10],[-8],[-1],[-6],[-3],[-7],[-1],[7],[4],[3],[-5],[5],[-3],[6],[-8],[-8],[8],[-7],[7],[9],[8],[-1],[8],[3],[1],[3],[-9],[3],[5],[-7],[-10],[-3],[-1],[7],[-6],[9]], dtype = "uint64")#candidate|952|(160, 1)|const|uint64
call_951 = relay.TupleGetItem(func_697_call(relay.reshape(const_952.astype('uint64'), [4, 5, 8]), relay.reshape(const_952.astype('uint64'), [4, 5, 8]), ), 0)
call_953 = relay.TupleGetItem(func_701_call(relay.reshape(const_952.astype('uint64'), [4, 5, 8]), relay.reshape(const_952.astype('uint64'), [4, 5, 8]), ), 0)
func_697_call = mod.get_global_var('func_697')
func_701_call = mutated_mod.get_global_var('func_701')
call_978 = relay.TupleGetItem(func_697_call(relay.reshape(call_951.astype('uint64'), [4, 5, 8]), relay.reshape(call_951.astype('uint64'), [4, 5, 8]), ), 0)
call_979 = relay.TupleGetItem(func_701_call(relay.reshape(call_951.astype('uint64'), [4, 5, 8]), relay.reshape(call_951.astype('uint64'), [4, 5, 8]), ), 0)
output = relay.Tuple([bop_939,call_951,const_952,call_978,])
output2 = relay.Tuple([bop_939,call_953,const_952,call_979,])
func_982 = relay.Function([var_938,], output)
mod['func_982'] = func_982
mod = relay.transform.InferType()(mod)
var_983 = relay.var("var_983", dtype = "float64", shape = (4, 16, 13))#candidate|983|(4, 16, 13)|var|float64
output = func_982(var_983)
func_984 = relay.Function([var_983], output)
mutated_mod['func_984'] = func_984
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1207 = relay.var("var_1207", dtype = "float32", shape = (9, 11, 4))#candidate|1207|(9, 11, 4)|var|float32
uop_1208 = relay.sin(var_1207.astype('float32')) # shape=(9, 11, 4)
output = relay.Tuple([uop_1208,])
output2 = relay.Tuple([uop_1208,])
func_1211 = relay.Function([var_1207,], output)
mod['func_1211'] = func_1211
mod = relay.transform.InferType()(mod)
mutated_mod['func_1211'] = func_1211
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1212 = relay.var("var_1212", dtype = "float32", shape = (9, 11, 4))#candidate|1212|(9, 11, 4)|var|float32
func_1211_call = mutated_mod.get_global_var('func_1211')
call_1213 = func_1211_call(var_1212)
output = call_1213
func_1214 = relay.Function([var_1212], output)
mutated_mod['func_1214'] = func_1214
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1397 = relay.const(-4, dtype = "int64")#candidate|1397|()|const|int64
var_1398 = relay.var("var_1398", dtype = "int64", shape = (6, 6, 1))#candidate|1398|(6, 6, 1)|var|int64
bop_1399 = relay.left_shift(const_1397.astype('int64'), var_1398.astype('int64')) # shape=(6, 6, 1)
func_982_call = mod.get_global_var('func_982')
func_984_call = mutated_mod.get_global_var('func_984')
var_1405 = relay.var("var_1405", dtype = "float64", shape = (832,))#candidate|1405|(832,)|var|float64
call_1404 = relay.TupleGetItem(func_982_call(relay.reshape(var_1405.astype('float64'), [4, 16, 13])), 0)
call_1406 = relay.TupleGetItem(func_984_call(relay.reshape(var_1405.astype('float64'), [4, 16, 13])), 0)
output = relay.Tuple([bop_1399,call_1404,var_1405,])
output2 = relay.Tuple([bop_1399,call_1406,var_1405,])
func_1409 = relay.Function([var_1398,var_1405,], output)
mod['func_1409'] = func_1409
mod = relay.transform.InferType()(mod)
mutated_mod['func_1409'] = func_1409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1409_call = mutated_mod.get_global_var('func_1409')
var_1411 = relay.var("var_1411", dtype = "int64", shape = (6, 6, 1))#candidate|1411|(6, 6, 1)|var|int64
var_1412 = relay.var("var_1412", dtype = "float64", shape = (832,))#candidate|1412|(832,)|var|float64
call_1410 = func_1409_call(var_1411,var_1412,)
output = call_1410
func_1413 = relay.Function([var_1411,var_1412,], output)
mutated_mod['func_1413'] = func_1413
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2220 = relay.var("var_2220", dtype = "uint32", shape = ())#candidate|2220|()|var|uint32
var_2221 = relay.var("var_2221", dtype = "uint32", shape = (12, 1, 2))#candidate|2221|(12, 1, 2)|var|uint32
bop_2222 = relay.logical_xor(var_2220.astype('uint32'), var_2221.astype('uint32')) # shape=(12, 1, 2)
output = bop_2222
output2 = bop_2222
func_2225 = relay.Function([var_2220,var_2221,], output)
mod['func_2225'] = func_2225
mod = relay.transform.InferType()(mod)
var_2226 = relay.var("var_2226", dtype = "uint32", shape = ())#candidate|2226|()|var|uint32
var_2227 = relay.var("var_2227", dtype = "uint32", shape = (12, 1, 2))#candidate|2227|(12, 1, 2)|var|uint32
output = func_2225(var_2226,var_2227,)
func_2228 = relay.Function([var_2226,var_2227,], output)
mutated_mod['func_2228'] = func_2228
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2704 = relay.var("var_2704", dtype = "float32", shape = (1, 3, 6))#candidate|2704|(1, 3, 6)|var|float32
uop_2705 = relay.acosh(var_2704.astype('float32')) # shape=(1, 3, 6)
bop_2708 = relay.bitwise_xor(var_2704.astype('int64'), relay.reshape(uop_2705.astype('int64'), relay.shape_of(var_2704))) # shape=(1, 3, 6)
output = relay.Tuple([bop_2708,])
output2 = relay.Tuple([bop_2708,])
func_2726 = relay.Function([var_2704,], output)
mod['func_2726'] = func_2726
mod = relay.transform.InferType()(mod)
mutated_mod['func_2726'] = func_2726
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2727 = relay.var("var_2727", dtype = "float32", shape = (1, 3, 6))#candidate|2727|(1, 3, 6)|var|float32
func_2726_call = mutated_mod.get_global_var('func_2726')
call_2728 = func_2726_call(var_2727)
output = call_2728
func_2729 = relay.Function([var_2727], output)
mutated_mod['func_2729'] = func_2729
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3079 = relay.var("var_3079", dtype = "float64", shape = (4, 12, 10))#candidate|3079|(4, 12, 10)|var|float64
uop_3080 = relay.log2(var_3079.astype('float64')) # shape=(4, 12, 10)
uop_3108 = relay.cos(var_3079.astype('float32')) # shape=(4, 12, 10)
output = relay.Tuple([uop_3080,uop_3108,])
output2 = relay.Tuple([uop_3080,uop_3108,])
func_3117 = relay.Function([var_3079,], output)
mod['func_3117'] = func_3117
mod = relay.transform.InferType()(mod)
mutated_mod['func_3117'] = func_3117
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3118 = relay.var("var_3118", dtype = "float64", shape = (4, 12, 10))#candidate|3118|(4, 12, 10)|var|float64
func_3117_call = mutated_mod.get_global_var('func_3117')
call_3119 = func_3117_call(var_3118)
output = call_3119
func_3120 = relay.Function([var_3118], output)
mutated_mod['func_3120'] = func_3120
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3388 = relay.var("var_3388", dtype = "float64", shape = (9, 8, 14))#candidate|3388|(9, 8, 14)|var|float64
var_3389 = relay.var("var_3389", dtype = "float64", shape = (9, 8, 14))#candidate|3389|(9, 8, 14)|var|float64
bop_3390 = relay.floor_divide(var_3388.astype('float64'), relay.reshape(var_3389.astype('float64'), relay.shape_of(var_3388))) # shape=(9, 8, 14)
output = relay.Tuple([bop_3390,])
output2 = relay.Tuple([bop_3390,])
func_3395 = relay.Function([var_3388,var_3389,], output)
mod['func_3395'] = func_3395
mod = relay.transform.InferType()(mod)
var_3396 = relay.var("var_3396", dtype = "float64", shape = (9, 8, 14))#candidate|3396|(9, 8, 14)|var|float64
var_3397 = relay.var("var_3397", dtype = "float64", shape = (9, 8, 14))#candidate|3397|(9, 8, 14)|var|float64
output = func_3395(var_3396,var_3397,)
func_3398 = relay.Function([var_3396,var_3397,], output)
mutated_mod['func_3398'] = func_3398
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3481 = relay.var("var_3481", dtype = "uint64", shape = (10, 13, 1))#candidate|3481|(10, 13, 1)|var|uint64
var_3482 = relay.var("var_3482", dtype = "uint64", shape = (10, 13, 10))#candidate|3482|(10, 13, 10)|var|uint64
bop_3483 = relay.bitwise_xor(var_3481.astype('uint64'), var_3482.astype('uint64')) # shape=(10, 13, 10)
output = bop_3483
output2 = bop_3483
func_3494 = relay.Function([var_3481,var_3482,], output)
mod['func_3494'] = func_3494
mod = relay.transform.InferType()(mod)
var_3495 = relay.var("var_3495", dtype = "uint64", shape = (10, 13, 1))#candidate|3495|(10, 13, 1)|var|uint64
var_3496 = relay.var("var_3496", dtype = "uint64", shape = (10, 13, 10))#candidate|3496|(10, 13, 10)|var|uint64
output = func_3494(var_3495,var_3496,)
func_3497 = relay.Function([var_3495,var_3496,], output)
mutated_mod['func_3497'] = func_3497
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3522 = relay.var("var_3522", dtype = "float64", shape = (9, 11, 7))#candidate|3522|(9, 11, 7)|var|float64
uop_3523 = relay.sin(var_3522.astype('float64')) # shape=(9, 11, 7)
func_1211_call = mod.get_global_var('func_1211')
func_1214_call = mutated_mod.get_global_var('func_1214')
var_3549 = relay.var("var_3549", dtype = "float32", shape = (396,))#candidate|3549|(396,)|var|float32
call_3548 = relay.TupleGetItem(func_1211_call(relay.reshape(var_3549.astype('float32'), [9, 11, 4])), 0)
call_3550 = relay.TupleGetItem(func_1214_call(relay.reshape(var_3549.astype('float32'), [9, 11, 4])), 0)
func_3395_call = mod.get_global_var('func_3395')
func_3398_call = mutated_mod.get_global_var('func_3398')
const_3553 = relay.const([6.625990,0.132876,-8.631669,4.784700,-2.629641,9.448651,3.324548,2.252367,2.007797,4.988603,7.390930,-9.167301,7.907730,-6.390839,2.142641,-3.239173,-0.396156,-3.148806,8.360277,5.399365,-3.246955,3.960482,-3.478177,-6.717482,-7.850794,0.405955,-3.236457,9.934137,3.418601,-5.265727,-3.847565,9.423786,-3.028879,1.867952,1.829890,9.425063,2.715694,8.876216,8.080694,4.231141,-8.520660,-0.042918,-3.717672,-3.433027,1.589544,7.116377,4.522230,-1.220277,-4.168629,-1.394770,-8.033226,4.383511,-7.249429,9.318620,8.465883,-2.302804,-3.711647,-3.260940,-3.919711,-9.480751,5.967747,-2.190115,-8.928277,1.767316,-5.474617,2.548694,5.692782,9.115642,4.073108,-5.724362,4.690885,-7.349295,5.681825,5.999505,5.929872,8.279353,4.788698,-1.228990,-7.322040,-4.894996,5.078311,0.630851,5.727171,-5.592375,-3.644166,4.527899,5.255981,2.797749,-1.880920,4.231444,-5.309786,-9.563068,-6.430734,6.096409,-0.065241,3.555173,6.804263,0.776365,4.728139,-8.085514,-8.299571,-2.943516,2.456932,-6.447057,-8.400872,-1.250238,-9.996847,-4.083152,9.936890,3.997737,6.061405,4.147742,4.720391,5.534068,-3.825538,-1.947878,3.465690,0.675422,-8.149070,-2.269634,3.405444,9.843475,-3.845806,-0.756505,-3.981323,5.256099,-7.857332,-3.706596,2.333884,2.719213,5.112206,-1.669693,-2.177259,-9.887114,2.613689,4.785671,9.962811,-3.558760,-5.440180,5.446885,-0.735630,-3.981047,0.031100,0.772884,9.034082,-1.289952,-7.843811,9.677387,-3.837274,-7.141730,1.592756,-4.560858,-2.825640,-7.009117,8.478976,1.633498,-9.778638,0.070184,0.577226,3.799302,0.327310,1.524586,-8.021631,-7.306648,-4.085138,2.376563,-3.370134,-9.493758,-3.059711,7.259971,-6.173211,-4.280029,-2.217633,-3.042213,-6.468213,-0.249099,-7.954782,6.780855,4.202550,8.875216,-6.686288,8.205012,4.101947,-0.537731,-3.029849,3.294173,-3.076565,5.532345,8.568482,-7.516350,3.651531,6.744289,4.598273,4.793322,-1.419326,-8.194312,7.401905,7.217244,-7.253664,-7.303782,2.717528,5.322159,1.572351,5.754433,6.635766,-4.620747,-1.175487,-8.121721,6.229907,-4.398656,-6.686182,-1.792737,-9.355337,-4.235882,8.424005,8.721319,9.292589,3.167775,-7.330612,7.502715,-8.111319,-8.793151,-3.202747,-5.346323,-5.901942,0.165023,-8.664922,-3.783820,-6.922241,1.442419,-1.833188,-4.225213,3.250265,-8.127577,-2.385489,2.015642,-7.048586,-5.947206,-0.974445,-6.068243,9.485111,-0.771468,2.926217,8.418931,0.901406,-4.714025,2.784727,1.787934,-3.848753,-8.586452,-2.367952,0.722621,-1.378256,5.261029,2.365957,0.681622,9.695157,-4.920078,5.793997,-9.407670,-9.874251,-1.154540,-8.894175,-0.716752,5.235095,8.346531,8.223776,-7.401222,-7.290121,-6.121538,4.557920,2.603220,9.522732,-1.920370,1.678709,-2.696614,9.143377,2.642631,-2.101849,-5.260039,2.126895,9.790409,-0.796283,-2.729948,9.660951,-4.697604,-9.840299,-9.519244,9.364414,-0.362136,4.879827,-9.600034,6.544471,-2.619928,-2.958179,-7.392407,8.395473,-8.541969,2.073075,-6.850200,9.754962,-0.482760,-0.771535,-3.251034,4.640621,-7.234239,9.062164,9.307405,8.346090,-7.219097,-6.390915,6.041944,9.108792,1.361812,-7.328268,3.739649,8.473984,0.234393,-7.220483,3.030351,7.965972,9.536737,8.457868,0.414901,-5.828528,-1.046116,-6.451125,-1.372730,8.407279,6.335738,-8.378845,4.138526,-1.925320,4.506685,-7.803307,-7.947689,0.525899,-8.153669,-4.784914,4.552304,-4.900558,3.240061,0.574666,-9.887608,4.677381,-5.767842,-1.255099,5.727801,-0.927392,-7.513241,-6.625620,-9.579174,-8.511076,-6.464859,8.637291,5.954955,2.306456,-1.733456,2.846228,1.015002,-1.044046,-7.344079,7.011444,5.946374,-1.793564,6.525983,-4.535177,-2.041318,-3.947394,0.618924,-9.068297,7.468731,5.438750,-1.425577,-8.885754,-0.194955,7.094062,-1.918437,-8.386086,7.688723,4.329825,2.831216,-6.047805,-2.341054,-5.432861,-7.792248,-1.132008,-2.753542,-6.946120,-1.466175,-1.381880,9.682441,4.703565,8.881439,-9.524954,6.974210,6.934177,4.787197,-6.638384,-6.027726,-0.541389,-1.086158,6.914401,-8.597614,4.822653,-7.908126,4.264999,-9.013386,8.113180,6.364988,-9.423616,1.568822,9.888821,4.560117,-4.306890,8.358245,1.140589,-2.842899,-5.001253,-5.498779,1.476343,-7.155374,-4.469777,-2.653918,-8.093291,7.571129,-0.073524,-9.570755,-3.964350,3.413124,7.903024,9.996879,-3.703499,6.544797,-7.189200,1.307388,2.319904,5.713728,-0.224121,9.139620,8.126155,4.428719,-5.551553,9.406887,5.575020,2.202527,9.347264,2.100086,-9.821859,4.372980,-3.663122,6.298198,-4.880949,-0.812610,-5.994878,3.102873,-4.957725,0.006639,-3.121220,3.052558,8.543525,-0.898769,7.572674,1.146583,5.620194,8.981870,3.339000,4.800062,2.791216,-6.754933,2.415489,9.314516,-7.635316,-6.568630,0.699374,-7.427751,4.274099,-3.290285,0.661385,-8.584142,-6.802726,-7.479463,-1.009126,6.083139,2.472518,9.200271,3.032925,0.840873,0.392817,-5.512182,6.916929,-0.276404,8.963511,-7.575026,-7.433447,2.627559,-2.639546,-8.509418,6.318049,-6.456115,2.602605,-3.482340,-1.274015,-4.404022,9.472230,-8.187584,6.058689,0.229625,4.473365,4.736268,0.305300,-7.883400,6.465790,-2.444251,-8.971088,4.591207,2.576583,-8.026645,6.801726,9.660961,7.328296,-5.211751,-0.191979,-2.292477,7.527175,3.975862,-7.572613,-6.929005,-4.399665,2.727019,9.218197,-3.624826,-4.321679,-9.370713,5.660879,-5.424831,8.259926,-6.809906,7.949685,-9.347402,-6.608958,7.769092,7.862465,-1.019075,-6.497450,7.017759,5.149311,-5.544708,-1.037397,5.105242,3.223082,1.562753,-6.484680,-6.006722,-7.970342,-7.010869,7.836626,2.984887,4.984122,-9.600321,8.493172,9.045044,-3.669306,-7.585239,-2.624657,-6.305433,-4.774668,1.629800,1.092631,-9.500861,-6.759527,1.110065,-0.393401,-2.817408,-5.591184,9.739599,-1.715306,-0.526124,5.245573,-5.387860,6.677359,0.162520,-1.075169,-9.918153,-8.987960,5.737151,-3.422370,-6.290893,4.573981,-8.872924,-3.732310,-7.123176,5.694698,2.339019,3.854669,-1.426280,-9.073940,-8.815244,-3.698251,2.565754,1.944804,7.533040,5.249387,-6.374590,1.781351,-6.388337,3.422336,-3.338766,-4.573348,2.538100,5.184322,-5.732775,5.411904,-8.951708,1.191067,-8.433840,-4.958754,-3.932684,-9.145658,7.199914,-6.702420,5.302538,-7.514176,-0.535532,7.848449,-6.445611,3.570707,-8.513669,-1.631021,9.476653,-4.645330,-6.519325,1.022776,-5.232011,-5.104599,5.062020,-8.065003,-7.549743,6.807751,3.369386,-6.328451,7.299653,-6.766143,-6.593014,4.045803,-7.693876,3.874995,-5.956281,-9.044151,-2.179016,-2.209143,8.168069,-5.066759,0.275020,-1.389763,-3.305288,5.048664,-4.724057,-7.268464,-4.315522,-1.597736,7.777806,9.682028,8.841412,6.696731,-0.912013,4.139646,-6.610329,0.814874,1.700005,-3.848849,-1.338158,-1.932537,4.625274,4.675169,-0.533303,-3.992708,-1.876417,9.086704,9.724771,9.242778,0.917899,7.188253,8.969675,6.173616,-0.473563,-9.330848,3.717901,-4.197579,7.869243,-8.870896,3.092754,-3.429873,6.235208,0.090067,-0.081890,-5.238214,-3.651615,7.212565,6.935301,-7.330136,-2.860586,-7.938071,1.449026,-1.967269,5.467027,-2.881076,4.602799,-2.652684,4.362275,-7.217990,-8.946214,0.618819,-0.182349,-4.261519,3.651996,-5.051443,-3.637526,-8.901285,0.806963,-7.220206,4.380867,9.732978,1.844032,8.626161,-2.823123,-7.439101,6.867454,8.161555,-2.847334,5.725246,-0.967630,7.102621,-7.169939,1.651558,-6.297007,-0.013760,-9.360406,5.721639,1.590801,-8.311674,-7.419439,6.241890,-6.408088,5.298254,-7.503451,1.640448,-1.921017,2.225880,-8.483104,-8.824015,0.507141,-4.342307,4.478200,8.420646,9.712661,-9.070229,4.154068,2.452697,-8.859799,-4.982174,4.443580,1.633844,6.944532,-4.361628,4.275212,-5.738632,-0.684084,5.747695,-9.502054,-8.519087,-6.972478,9.943174,-8.624607,-3.776236,-4.232971,-2.148349,-9.270826,7.628587,-2.001466,1.641223,3.946170,-3.421357,-9.642747,5.059282,2.997083,-7.161243,-0.805501,1.183184,-6.454416,9.696179,-2.590863,-1.258816,1.984206,-7.779393,-7.771802,-0.425686,-7.641280,5.802447,-2.391529,0.039011,-2.652053,2.042155,-2.950269,-3.753336,-0.900579,6.383360,9.801311,6.492989,9.208866,-6.651479,9.304251,3.255794,-7.106626,7.610313,0.950598,-0.730546,-3.904810,-7.722818,-5.112665,-8.072423,-3.251814,8.714072,6.333499,9.870509,0.779070,-4.451579,-2.508537,-7.287329,-2.585681,5.188135,-7.186022,-6.194045,1.632755,1.539991,4.212557,6.339778,1.251122,1.077567,6.620933,-7.493033,-5.182984,-8.369781,-1.409126,2.811540,-0.610216,0.992519,-1.954249,6.214052,-0.880052,1.053780,-1.005714,-5.251503,-4.815703,4.478055,-4.024094,-9.406378,-9.506388,1.415663,9.914602,-2.928412,2.143466,-7.834113,8.007821,6.425564,5.450589,8.080439,6.497965,5.931159,3.891901,-8.302353,-8.147863,-6.770937,2.937129,-7.324150,3.661927,-9.312770,-9.012648,-0.994587,-4.134033,2.602927,9.153875,-3.211529,-6.168340,-1.000321,-6.891089,2.630431,2.057521,9.993981,1.825091,4.808649,-3.368670,3.806039,-9.680464,-8.664408,-8.564843,-0.433579,-6.534417,-5.562139,7.322748,-9.794147,1.573275,-2.958888,-5.143120,4.716059,7.427542,-2.238973,-0.694669,-5.482110,9.048907,-7.850911,1.323803,1.388816,7.940084,-6.814546,-0.115268,-4.727888,6.619699,-7.841710,-5.131570,7.012486,-1.764793,-7.390729,-3.638162,-1.064450,1.870184,7.405107,9.823742,5.359181,-5.422664,7.628868,-5.743771,6.530254,1.973530,2.787956,8.591932,9.447314,-9.156250,9.560334,5.625474,3.917675,-9.248235,6.758320,1.734055,-5.869350,-1.069209,2.258203,5.326435,-0.771739,-6.053691,-8.395864,4.687620,-6.616574,6.765777,-1.069453,1.242491,-4.920852,-6.440932,4.551559,-9.866805,5.923248,-7.723178,8.462539,9.911056,-9.419725,-4.609662,-1.012735,-4.913123,4.511692,-1.875668,-0.930881,9.686561,3.688267,-1.819963,-8.995699,-9.129533,-1.415923,-9.047966,-8.453681,1.571678,1.692408,7.741946,2.553698,-0.415958,-6.638367,-5.207147,-6.309698,8.291914,9.063120,6.585732,-3.170245,-9.914841,-6.089060,-9.484027,-3.328131,5.165134,3.257620,4.814525,-6.468576,-5.152546,-6.203635,-2.217699,-9.885399,-7.300818,1.141282,5.782293,7.506256,-2.494580], dtype = "float64")#candidate|3553|(1008,)|const|float64
call_3552 = relay.TupleGetItem(func_3395_call(relay.reshape(const_3553.astype('float64'), [9, 8, 14]), relay.reshape(const_3553.astype('float64'), [9, 8, 14]), ), 0)
call_3554 = relay.TupleGetItem(func_3398_call(relay.reshape(const_3553.astype('float64'), [9, 8, 14]), relay.reshape(const_3553.astype('float64'), [9, 8, 14]), ), 0)
uop_3564 = relay.rsqrt(call_3552.astype('float32')) # shape=(9, 8, 14)
uop_3566 = relay.rsqrt(call_3554.astype('float32')) # shape=(9, 8, 14)
func_3494_call = mod.get_global_var('func_3494')
func_3497_call = mutated_mod.get_global_var('func_3497')
var_3581 = relay.var("var_3581", dtype = "uint64", shape = (130,))#candidate|3581|(130,)|var|uint64
const_3582 = relay.const([-5,1,2,-7,1,6,6,6,-2,9,1,2,2,1,6,-9,9,-3,7,1,4,9,5,-7,-2,3,-6,9,4,4,-10,-3,4,-9,5,-8,9,9,7,-1,10,2,-8,6,5,-3,4,1,3,-10,1,-7,9,4,-2,5,-8,10,2,-9,-9,-9,8,2,1,10,-3,-2,-7,-8,-1,10,2,5,-7,8,-7,-10,8,-8,5,-2,-9,1,-9,4,2,9,-6,-5,-1,9,-1,-4,-1,7,-4,-6,-3,8,4,4,-8,7,9,4,-6,-7,4,-5,8,4,-10,5,-5,-7,-7,-4,-6,-6,4,7,7,-6,-9,-7,-10,-7,9,-8,-6,-5,8,7,-2,-10,-5,8,-3,2,-3,7,7,-8,9,-5,10,8,-1,3,10,-4,2,-6,4,5,4,-3,-7,1,6,10,8,-8,-7,-4,6,-1,-8,3,2,3,1,10,6,5,7,-2,5,4,10,-8,-4,5,5,-7,-8,-4,-6,-9,4,-6,9,-6,7,8,-7,-4,-5,-4,8,7,4,7,4,4,-9,-10,10,7,-7,-5,-1,-5,9,-7,5,-5,5,-8,-7,10,-5,-6,-8,4,-8,-2,-9,5,8,-5,10,-1,1,6,4,-3,8,-7,2,6,2,9,4,-9,10,5,-3,6,8,9,-10,4,-4,6,2,-6,-9,6,-10,6,-9,1,9,-6,-9,-2,9,-7,-5,-9,-7,1,-1,-1,-2,-3,10,-2,9,-10,5,7,6,-5,1,9,-8,-5,-9,-9,5,-3,6,-6,5,5,-5,-4,-8,-3,-4,8,3,10,-10,-5,5,-10,3,-7,-1,10,7,-7,2,6,2,-7,-7,-7,10,-4,1,-5,9,5,-6,-5,7,-10,2,5,9,-9,1,-3,-1,5,10,-6,-3,10,6,-4,7,-1,9,-5,10,-5,3,1,7,-3,7,8,2,9,3,-10,7,-1,9,-5,3,9,7,9,-7,1,-6,4,-6,4,8,10,-5,-4,-1,1,-10,-10,-10,3,5,-3,-2,9,-2,7,-6,9,-8,-6,-3,-2,9,10,-5,9,6,1,1,-7,-2,6,9,-1,-8,5,6,-4,1,8,-6,8,-1,1,-8,4,3,9,-5,9,9,-5,-5,-2,5,-2,9,5,8,1,-4,-9,-6,9,1,5,3,-7,-10,-5,-10,-6,-9,-10,-6,-7,7,7,6,-7,3,-9,3,-7,6,8,10,-7,-4,8,-10,-10,10,-2,-3,-5,10,-5,1,-6,3,-5,7,-4,8,2,-6,7,-2,-2,8,1,3,-9,-9,1,8,-5,-9,9,-10,5,5,-9,1,-2,-1,6,-1,10,9,-2,-9,-3,5,-6,-5,10,-5,7,-2,-6,1,1,-7,2,2,5,10,-10,2,-3,-8,-6,-1,10,1,-10,-8,-6,2,10,-1,-5,-5,-9,2,-5,-4,5,4,-3,-1,-7,4,3,1,-9,-10,-7,-1,3,8,-6,-7,-10,-6,5,-7,-6,8,-8,3,-3,-2,-8,-7,-8,9,1,-3,-6,-5,-6,-7,-5,10,-4,-1,-7,-9,5,6,-3,7,10,7,9,-10,6,5,-10,5,9,-3,8,-1,-8,-8,3,-6,-5,10,-7,-7,6,6,-9,2,-6,2,4,1,-2,4,-6,8,-3,5,9,-5,-4,-10,2,10,-6,-4,-8,4,-5,5,7,1,2,-2,-8,5,-7,-4,9,-7,-6,7,7,6,-8,-3,6,6,2,10,-8,3,-4,-4,-10,-7,-3,4,6,4,-3,-10,1,-9,-8,2,-6,1,9,-2,-8,9,7,-3,-3,6,2,-5,6,5,-4,9,-9,1,-6,10,4,-7,-3,4,7,-4,-8,3,2,7,4,-8,-6,4,-2,8,-4,-6,7,-6,2,5,-8,5,8,-6,9,7,2,9,-6,1,4,-8,9,-5,-4,10,-1,-2,8,1,-3,-5,10,3,3,-5,-1,-9,-8,1,7,2,10,-6,3,6,-6,2,-4,-9,9,5,-8,2,9,6,7,-5,-3,5,-8,3,-1,9,10,-2,3,-8,-2,-5,-4,-10,-10,-5,-5,10,-1,-7,-7,-8,4,5,9,-6,-2,5,-3,-6,-9,-7,-3,-8,-1,-9,-1,7,-8,1,-6,10,10,-3,-8,6,-1,-2,2,-9,4,3,-4,9,3,-1,10,6,-5,-3,-9,2,3,-4,-3,10,-2,1,3,10,-1,-6,10,-1,2,-10,2,-3,-6,-2,4,4,-2,2,4,-5,10,-8,-3,7,-2,10,-9,-10,2,3,1,1,-2,-3,4,-5,-7,-7,1,-8,1,6,-1,-6,-10,10,-6,-7,6,9,5,-8,-5,3,-1,9,-10,-3,-3,5,-7,5,10,4,-1,7,6,-8,-2,-7,3,4,-2,6,7,-9,8,10,7,5,-8,1,8,5,2,1,-9,-9,-4,-6,-6,-5,-2,-4,10,4,2,4,-7,-9,2,-4,-7,-3,8,1,-8,-10,-3,7,4,5,-1,3,7,-6,-4,-1,-5,-1,4,7,-2,2,1,-1,3,8,-5,3,-3,-1,1,-7,6,7,3,4,1,1,5,5,-9,3,4,-6,-5,5,10,-10,3,8,1,1,6,-4,-5,-1,1,-8,10,-3,2,-10,-1,9,-10,-2,-9,-5,-5,7,7,4,-4,3,6,-10,6,-1,4,3,-6,-7,5,9,-8,-10,6,2,-6,-5,-1,-1,7,-5,1,-5,2,10,-3,-9,-9,5,-5,-7,-4,-3,7,3,7,7,6,3,-5,7,-5,-8,-5,10,-1,-3,9,-1,2,-2,-2,5,4,-7,-4,-4,1,3,-6,8,-10,-2,6,5,5,-7,10,-6,1,-3,8,-3,-1,4,9,-5,-2,-8,-8,6,-4,-2,-6,-1,4,3,-3,-8,3,2,-6,3,-3,4,-7,7,-3,8,-9,-8,2,2,8,-2,6,6,-2,-9,1,-6,-4,-10,2,-8,-6,4,8,3,-10,8,10,7,3,7,-9,-2,8,4,9,-2,8,3,4,3,-3,-9,3,5,3,-9,6,7,-1,-5,3,-7,1,-7,6,-8,-1,3,4,9,3,10,-9,-5,-6,-3,8,-9,10,4,8,-6,-1,-4,-9,2,2,3,-9,-2,-9,-5,4,5,-4,9,-3,2,6,-10,-10,8,6,-1,-2,-1,9,7,4,9,-3,1,-5,-3,-10,9,7,1,-1,-8,7,-3,9,-4,-3,2,-3,-3,7,-1,-9,6,8,-9,2,-1,9,9,-3,3,-8,-2,-8,-1,-3,2,5,-9,-7,-1,6,-10,-5,6,-2,3,-2,10,10,-4,4,-4,-6,-1,1,-2,7,5,2,9,8,3,7,-1,5,-9,-3,-7,7,-4,3,7,-9,-1,4,3,1,4,-9,2,-2,2,-5,-6,10,-3,5,2,-2,5,2,10,5,-9,8,-10,-4,8,3,6,-2], dtype = "uint64")#candidate|3582|(1300,)|const|uint64
call_3580 = func_3494_call(relay.reshape(var_3581.astype('uint64'), [10, 13, 1]), relay.reshape(const_3582.astype('uint64'), [10, 13, 10]), )
call_3583 = func_3494_call(relay.reshape(var_3581.astype('uint64'), [10, 13, 1]), relay.reshape(const_3582.astype('uint64'), [10, 13, 10]), )
func_697_call = mod.get_global_var('func_697')
func_701_call = mutated_mod.get_global_var('func_701')
var_3597 = relay.var("var_3597", dtype = "uint64", shape = (160,))#candidate|3597|(160,)|var|uint64
call_3596 = relay.TupleGetItem(func_697_call(relay.reshape(var_3597.astype('uint64'), [4, 5, 8]), relay.reshape(var_3597.astype('uint64'), [4, 5, 8]), ), 0)
call_3598 = relay.TupleGetItem(func_701_call(relay.reshape(var_3597.astype('uint64'), [4, 5, 8]), relay.reshape(var_3597.astype('uint64'), [4, 5, 8]), ), 0)
func_3395_call = mod.get_global_var('func_3395')
func_3398_call = mutated_mod.get_global_var('func_3398')
call_3607 = relay.TupleGetItem(func_3395_call(relay.reshape(uop_3564.astype('float64'), [9, 8, 14]), relay.reshape(uop_3564.astype('float64'), [9, 8, 14]), ), 0)
call_3608 = relay.TupleGetItem(func_3398_call(relay.reshape(uop_3564.astype('float64'), [9, 8, 14]), relay.reshape(uop_3564.astype('float64'), [9, 8, 14]), ), 0)
output = relay.Tuple([uop_3523,call_3548,var_3549,const_3553,uop_3564,call_3580,var_3581,const_3582,call_3596,var_3597,call_3607,])
output2 = relay.Tuple([uop_3523,call_3550,var_3549,const_3553,uop_3566,call_3583,var_3581,const_3582,call_3598,var_3597,call_3608,])
func_3611 = relay.Function([var_3522,var_3549,var_3581,var_3597,], output)
mod['func_3611'] = func_3611
mod = relay.transform.InferType()(mod)
mutated_mod['func_3611'] = func_3611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3611_call = mutated_mod.get_global_var('func_3611')
var_3613 = relay.var("var_3613", dtype = "float64", shape = (9, 11, 7))#candidate|3613|(9, 11, 7)|var|float64
var_3614 = relay.var("var_3614", dtype = "float32", shape = (396,))#candidate|3614|(396,)|var|float32
var_3615 = relay.var("var_3615", dtype = "uint64", shape = (130,))#candidate|3615|(130,)|var|uint64
var_3616 = relay.var("var_3616", dtype = "uint64", shape = (160,))#candidate|3616|(160,)|var|uint64
call_3612 = func_3611_call(var_3613,var_3614,var_3615,var_3616,)
output = call_3612
func_3617 = relay.Function([var_3613,var_3614,var_3615,var_3616,], output)
mutated_mod['func_3617'] = func_3617
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4962 = relay.var("var_4962", dtype = "bool", shape = ())#candidate|4962|()|var|bool
const_4963 = relay.const([[[False,True,False,True,True,False,False,True,True,False,False],[False,True,True,True,True,False,False,False,False,False,True],[False,False,True,False,True,True,True,True,True,False,False],[True,True,True,True,True,False,False,True,False,True,False],[True,False,False,False,False,False,False,True,True,False,True],[False,True,True,True,False,False,False,False,True,True,True],[False,False,False,True,True,True,True,False,False,True,False],[False,True,True,False,True,False,True,True,True,True,False],[False,True,True,True,True,True,False,True,True,False,True],[True,True,False,True,True,False,True,False,True,True,True],[False,True,False,False,False,True,True,True,False,False,False],[True,True,False,False,True,True,True,True,False,True,True],[True,False,False,True,True,False,False,False,True,False,True],[True,False,True,False,False,False,False,False,True,True,True]],[[True,False,False,False,True,True,False,False,False,True,False],[False,True,True,False,True,True,True,False,False,False,False],[True,True,False,False,True,False,True,True,True,False,True],[True,False,False,True,False,True,True,False,True,False,True],[True,False,False,False,False,False,True,False,True,False,True],[True,False,True,False,True,False,True,True,True,True,True],[True,False,False,False,True,False,False,True,True,True,False],[True,True,False,False,False,False,True,True,False,False,True],[True,False,True,True,False,False,False,True,False,True,True],[False,False,False,False,False,False,True,True,False,False,False],[False,False,True,False,True,False,False,False,True,True,False],[False,False,False,True,False,True,True,False,False,True,False],[True,True,False,True,False,True,True,False,True,True,True],[False,True,False,False,False,False,False,True,True,False,False]],[[True,True,False,True,False,False,True,True,False,False,False],[False,True,False,True,False,True,True,True,False,True,True],[False,False,True,True,False,False,False,False,False,True,False],[True,False,False,True,False,False,False,False,False,False,False],[True,False,False,False,True,False,False,False,True,False,False],[False,True,False,False,True,True,True,True,True,False,True],[True,True,True,True,True,False,False,False,False,True,False],[False,True,True,False,True,True,True,True,False,True,True],[False,False,False,True,True,True,False,True,True,False,False],[False,True,False,False,True,False,False,False,False,True,True],[True,True,False,False,True,False,False,False,True,True,False],[True,False,True,True,True,False,False,True,True,False,False],[True,True,False,True,True,False,True,False,False,False,False],[False,False,True,False,True,True,True,False,False,True,False]],[[True,False,True,False,False,False,True,False,True,False,True],[True,True,True,True,False,True,True,False,True,False,False],[False,False,True,False,False,True,False,True,False,True,True],[True,True,True,False,False,True,True,False,True,False,True],[False,True,True,True,True,True,True,True,False,True,True],[True,True,True,True,True,False,True,True,True,False,False],[False,False,True,False,True,True,True,True,True,True,True],[False,False,False,False,True,True,False,True,False,True,False],[False,False,False,False,True,True,False,False,True,False,False],[False,False,False,False,True,True,True,False,False,True,True],[False,True,False,True,True,True,False,True,False,False,True],[False,False,True,True,False,True,False,True,True,True,True],[True,True,True,True,False,True,True,True,False,False,True],[True,True,False,False,True,True,False,True,True,False,False]],[[False,True,False,True,False,True,False,True,True,False,False],[False,True,False,True,False,True,False,False,False,True,False],[True,True,True,False,False,True,True,False,True,True,False],[True,False,False,True,True,True,False,True,True,False,False],[True,True,False,False,True,True,True,False,True,False,False],[False,False,False,True,False,False,False,True,False,False,False],[False,True,True,True,True,False,False,True,False,True,False],[False,False,False,True,True,False,False,True,False,True,True],[False,False,True,True,True,True,True,True,True,False,False],[False,True,True,False,False,False,False,True,False,False,True],[False,False,False,True,False,True,True,True,True,False,False],[False,True,True,True,False,False,False,False,False,False,False],[True,False,False,True,False,True,True,True,True,False,True],[True,True,True,True,False,True,False,False,True,False,True]],[[False,False,False,False,False,False,False,True,False,True,True],[False,False,False,False,True,True,True,True,False,False,False],[True,True,True,False,True,True,True,False,True,True,False],[True,True,False,True,True,True,False,False,True,False,False],[True,False,False,False,True,True,False,False,False,True,True],[True,False,True,False,True,True,True,True,True,False,False],[True,False,False,True,False,False,False,False,True,True,True],[True,True,False,False,True,False,False,False,False,True,False],[True,False,False,False,True,True,True,False,True,False,False],[True,True,False,False,True,False,True,False,True,False,True],[False,False,False,False,True,True,False,False,True,True,False],[True,True,False,False,False,False,False,True,False,True,False],[False,True,False,False,False,False,False,False,False,False,True],[False,False,False,True,True,False,True,False,True,False,False]],[[True,True,False,True,True,True,True,False,False,True,False],[False,True,False,False,True,True,False,True,False,True,False],[False,False,True,False,True,True,True,False,True,False,True],[False,True,False,True,False,False,True,True,False,True,True],[True,False,False,False,False,False,False,True,False,False,False],[True,False,True,False,False,True,False,False,False,False,False],[False,True,False,True,True,False,True,False,True,False,False],[True,False,True,True,False,False,True,False,False,False,True],[False,True,True,True,True,True,False,True,True,False,False],[False,True,True,False,True,False,True,True,False,False,False],[True,False,False,False,True,True,False,False,False,False,True],[True,False,False,False,False,True,False,False,True,False,False],[True,False,True,True,True,False,True,True,False,True,True],[True,True,True,False,True,True,False,False,False,True,False]],[[False,True,False,True,True,False,False,True,False,True,True],[True,False,False,False,False,False,False,True,True,True,False],[False,True,True,True,True,True,True,False,True,True,False],[True,False,True,False,True,True,False,False,False,False,True],[True,False,True,True,False,False,False,False,False,True,True],[True,False,True,True,False,True,False,True,True,False,False],[True,False,True,False,False,True,False,False,False,True,False],[True,False,True,True,True,True,True,False,False,True,False],[True,False,False,True,False,False,False,False,False,True,False],[True,True,True,False,False,True,True,True,False,False,False],[True,False,True,False,True,True,False,False,True,False,False],[False,True,True,False,True,True,False,True,False,True,False],[True,True,False,False,False,False,False,True,False,True,True],[True,True,False,False,False,True,True,False,True,True,True]],[[False,True,False,False,True,True,False,False,False,True,False],[False,True,False,False,False,True,False,True,False,True,True],[True,True,True,False,True,True,True,False,False,False,False],[False,False,True,False,False,False,False,True,False,False,False],[False,True,False,False,True,False,False,True,True,True,False],[False,True,True,True,True,False,True,True,False,True,True],[True,True,True,True,True,False,True,False,False,False,True],[True,False,False,True,False,True,False,False,False,False,True],[True,True,False,True,False,True,True,True,False,True,True],[True,False,False,True,False,False,False,False,True,True,False],[False,False,False,True,False,False,True,False,False,True,True],[False,False,True,False,False,False,False,True,True,False,True],[False,True,True,False,True,True,False,False,True,False,False],[False,True,False,False,True,False,False,False,True,True,False]],[[False,True,False,True,True,True,False,True,True,False,True],[False,True,False,False,True,True,True,True,True,True,False],[False,False,True,False,False,True,False,True,False,False,False],[False,True,False,False,False,True,True,False,False,True,True],[True,True,False,False,True,True,True,False,False,True,False],[True,False,True,True,False,False,True,False,True,True,False],[True,True,False,False,False,False,True,False,False,False,True],[False,False,False,False,True,True,False,True,True,True,True],[False,False,True,True,True,True,False,True,True,True,False],[True,True,True,False,False,True,False,False,False,False,False],[True,False,False,False,False,True,True,False,False,False,False],[True,True,False,False,True,True,False,False,True,True,True],[False,True,False,True,True,False,False,False,True,True,False],[True,True,True,False,False,True,False,False,True,True,True]]], dtype = "bool")#candidate|4963|(10, 14, 11)|const|bool
bop_4964 = relay.logical_or(var_4962.astype('bool'), const_4963.astype('bool')) # shape=(10, 14, 11)
func_3117_call = mod.get_global_var('func_3117')
func_3120_call = mutated_mod.get_global_var('func_3120')
var_4974 = relay.var("var_4974", dtype = "float64", shape = (480,))#candidate|4974|(480,)|var|float64
call_4973 = relay.TupleGetItem(func_3117_call(relay.reshape(var_4974.astype('float64'), [4, 12, 10])), 0)
call_4975 = relay.TupleGetItem(func_3120_call(relay.reshape(var_4974.astype('float64'), [4, 12, 10])), 0)
func_3395_call = mod.get_global_var('func_3395')
func_3398_call = mutated_mod.get_global_var('func_3398')
var_4984 = relay.var("var_4984", dtype = "float64", shape = (1008,))#candidate|4984|(1008,)|var|float64
call_4983 = relay.TupleGetItem(func_3395_call(relay.reshape(var_4984.astype('float64'), [9, 8, 14]), relay.reshape(var_4984.astype('float64'), [9, 8, 14]), ), 0)
call_4985 = relay.TupleGetItem(func_3398_call(relay.reshape(var_4984.astype('float64'), [9, 8, 14]), relay.reshape(var_4984.astype('float64'), [9, 8, 14]), ), 0)
output = relay.Tuple([bop_4964,call_4973,var_4974,call_4983,var_4984,])
output2 = relay.Tuple([bop_4964,call_4975,var_4974,call_4985,var_4984,])
func_4987 = relay.Function([var_4962,var_4974,var_4984,], output)
mod['func_4987'] = func_4987
mod = relay.transform.InferType()(mod)
mutated_mod['func_4987'] = func_4987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4987_call = mutated_mod.get_global_var('func_4987')
var_4989 = relay.var("var_4989", dtype = "bool", shape = ())#candidate|4989|()|var|bool
var_4990 = relay.var("var_4990", dtype = "float64", shape = (480,))#candidate|4990|(480,)|var|float64
var_4991 = relay.var("var_4991", dtype = "float64", shape = (1008,))#candidate|4991|(1008,)|var|float64
call_4988 = func_4987_call(var_4989,var_4990,var_4991,)
output = call_4988
func_4992 = relay.Function([var_4989,var_4990,var_4991,], output)
mutated_mod['func_4992'] = func_4992
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5267 = relay.const([[[-4.932288,0.305737,9.335418,0.392327,-4.847139,7.093818,6.591783,-0.212320],[-1.261270,-9.562411,5.466102,9.399066,-7.780765,-9.932304,-0.729721,7.799166],[-8.014917,8.003076,-9.702389,-9.107816,4.436694,8.643526,5.908344,-3.317638],[-9.563813,-5.552082,6.823662,-9.641123,-9.873766,-5.230297,9.406425,9.575732],[9.015655,5.458245,8.683965,-8.920110,3.936104,-9.473738,9.980359,-3.484123],[5.142969,0.841845,-9.322239,6.617129,-6.698444,4.816282,6.316712,4.854974],[-8.365754,5.626479,7.775425,-4.151241,1.188162,7.093430,2.692174,-9.589589]],[[-8.871753,-7.451422,6.603910,3.613856,7.310227,3.999637,0.796000,0.173290],[-2.255574,1.670062,4.552426,-0.367694,-5.456686,5.244492,-7.819170,4.946277],[-9.038211,4.351170,4.477520,1.730807,-1.763480,2.838545,-7.579362,0.612085],[0.655262,-1.708851,-0.581600,5.200661,-0.650861,-1.082076,-2.256550,3.021976],[5.182492,9.526116,1.732765,-9.859783,1.553839,3.117847,-0.878246,-2.902146],[2.856934,-9.409919,-1.177933,4.929958,5.993963,8.770229,6.423353,-9.957207],[6.408274,0.385210,-1.420421,-6.470554,0.775453,9.948963,-1.643677,-4.046435]],[[-9.605239,6.243968,-8.713476,0.432968,6.793426,-9.881670,1.016041,9.847359],[-7.292633,3.095443,-8.050372,-1.618067,0.494250,-2.462866,-2.699940,-6.591634],[3.233337,3.886557,-3.536195,5.287711,9.788451,-7.378076,-5.861369,5.916312],[-8.779959,-6.272853,8.101891,-4.694511,-4.652396,-8.451179,0.909434,-5.098075],[0.834074,6.805211,-1.283923,7.005088,-3.947271,1.714051,6.297266,8.853112],[4.084575,7.065404,-5.572227,-4.124722,-1.887465,2.764599,2.502561,-3.958805],[0.927487,-8.125249,7.079913,9.477815,6.980683,-8.162408,-2.902907,-2.573285]],[[8.250084,-6.011655,8.158386,1.978713,9.104408,-8.238903,-7.662272,5.558477],[-3.019982,9.965632,9.343819,1.606923,3.780050,-9.879399,0.876689,-1.780515],[-8.113573,-8.366811,3.668815,0.186579,6.411069,4.358798,-0.057636,4.473300],[-8.626088,-1.133064,-3.134008,-2.313684,-2.183028,4.008707,4.869756,-5.292573],[-2.605484,5.183874,-7.513918,-8.437392,-4.826894,1.972017,6.965118,9.914844],[-0.845273,1.907345,1.407292,-4.933217,-9.587067,8.800327,1.354758,4.338789],[7.011834,4.847390,8.864608,0.993902,7.249841,7.104869,8.749943,-9.640449]],[[-1.022714,-6.738037,8.995526,3.697526,-9.184887,1.192303,0.646832,5.800372],[-6.016902,-0.530450,3.030892,1.204144,7.903621,6.702564,-4.663988,-1.328070],[9.659824,-6.945157,6.309574,9.909821,5.312596,-9.905209,7.239852,3.034147],[-2.257355,-5.039626,8.633839,7.249458,-1.372595,1.034224,-6.671536,9.828072],[5.964513,9.719001,-9.879473,-8.123912,1.437399,-3.364663,3.007749,-1.481263],[5.566617,8.709841,0.338470,7.185305,6.348624,-7.749958,-5.040885,3.168186],[9.635870,3.689424,0.800410,2.168679,-4.351444,-0.037954,2.589318,4.968364]],[[1.019043,4.352374,0.097696,-3.118301,-6.260178,1.322334,-2.388838,-6.252301],[4.746686,1.938925,0.067977,0.027156,-2.945844,9.069572,1.520371,1.975301],[5.857002,1.302422,8.831124,1.412247,-7.570267,6.333626,-4.667604,-8.285791],[9.987621,-4.077159,8.857908,-4.403070,0.641373,2.092708,-8.038188,6.910338],[-5.754715,9.300835,-0.241328,2.284638,6.408314,-1.417276,-3.571803,9.511195],[-4.441694,-0.437384,3.796767,-4.630601,3.124563,2.898338,-3.605012,2.128166],[7.873669,-5.723258,-4.343556,-1.666213,-5.348711,9.007651,-8.443645,-4.075407]],[[-8.668058,-4.289702,2.043513,6.998506,-8.170628,6.443918,4.293899,5.809959],[1.801125,4.627739,0.752406,6.507819,-5.449190,-4.769007,5.093968,1.775451],[-0.231933,9.238274,-0.356758,-1.680845,-6.615717,0.291491,-3.021460,-4.511064],[5.569686,4.257737,-2.444311,-7.893065,7.249960,6.183472,-5.069529,4.942799],[-5.167786,-0.656427,3.135868,3.774491,-7.501221,6.270228,-0.035268,-5.954804],[5.653893,-6.203983,-8.015078,-0.752981,-7.331078,-2.026312,4.401877,7.025459],[8.067674,-0.440551,-1.619254,-2.534485,9.777805,2.202844,2.567268,0.088703]],[[-1.037054,-9.186742,-2.362946,-7.950991,-8.897585,3.686272,-4.092958,9.379309],[4.383134,-1.169354,-9.811351,-9.660984,2.533011,0.774502,-1.720525,3.249923],[-9.787734,1.128286,8.858411,0.319383,5.605933,4.310929,3.799374,8.970836],[-7.391664,-6.925038,-4.066177,-0.961694,7.631347,-9.015160,-3.645089,-9.533684],[-5.688690,-4.352347,5.767572,6.575618,-1.649552,1.009287,-4.742280,-5.645693],[-1.020939,5.180772,-0.413272,-7.188209,0.967601,1.782554,8.499977,-1.018002],[9.501913,4.129808,8.953266,4.805828,3.651142,2.368936,9.550957,-0.872984]],[[4.383437,-2.507445,-7.115286,0.379061,-8.024146,3.848519,-3.951042,0.160765],[-0.153607,-5.916053,4.147158,-5.300526,-9.298971,-2.862839,2.585709,-6.788846],[-4.080385,-1.210766,4.937783,-4.281389,-0.222527,1.518712,-4.228835,9.824599],[6.448699,-6.285343,7.385674,5.179074,-9.672388,-0.952826,7.940994,-8.475285],[4.102705,-7.600732,-5.528065,-7.974711,-5.415313,7.107673,-4.457073,-8.892577],[8.033481,8.769195,3.694264,-4.612762,-4.513334,3.985071,2.733217,-1.943783],[3.808100,-0.226010,9.385309,-1.290802,-1.193586,-2.753098,-1.860802,9.213831]],[[2.001169,9.561140,9.853486,6.198545,-8.213569,0.578304,-2.923574,-6.404318],[-2.064777,-9.669722,-5.452374,-0.137256,-3.552233,2.755221,0.840444,-1.841118],[3.606775,9.806015,-0.059532,2.148868,4.679252,-1.807047,-9.981321,9.339753],[0.178509,-5.177172,1.676219,9.227072,-5.791127,-7.422119,6.231346,-8.906406],[-0.028963,0.509183,-1.119372,2.324545,-2.766985,-2.155635,5.771049,8.159135],[2.513927,-3.092886,-5.966349,-5.267685,-6.703537,-7.743535,-8.877425,7.857212],[-5.909144,4.807253,1.844684,9.417106,-5.383965,-0.547680,3.713749,7.376907]],[[2.414927,3.969273,1.460966,-8.129429,1.843469,1.493489,-7.254662,-6.350718],[7.878159,7.599836,2.782746,-3.033181,-1.817517,3.936845,1.876610,-9.001258],[-0.482319,-9.318603,-8.659789,9.164949,-4.489819,8.339018,4.612443,3.233043],[2.140773,2.307094,1.824478,-4.344030,-1.781254,-4.242471,-1.127901,0.405409],[-7.771652,-4.713455,-6.597604,-9.438094,-9.623083,5.877341,-7.682743,8.013155],[-0.256668,-7.536244,-7.753576,0.912835,-3.997308,-2.315709,5.152913,2.460417],[-5.452934,-6.217617,3.919769,7.298402,-7.331543,-2.654328,5.815877,-6.914548]]], dtype = "float32")#candidate|5267|(11, 7, 8)|const|float32
uop_5268 = relay.log10(const_5267.astype('float32')) # shape=(11, 7, 8)
func_3494_call = mod.get_global_var('func_3494')
func_3497_call = mutated_mod.get_global_var('func_3497')
var_5273 = relay.var("var_5273", dtype = "uint64", shape = (130,))#candidate|5273|(130,)|var|uint64
const_5274 = relay.const([[1,7,-4,5,4,-6,-7,2,1,5],[1,5,-2,-1,-1,6,-3,-7,2,6],[7,-7,-8,8,-5,3,4,9,3,1],[-1,9,9,-2,8,-7,1,1,-2,-1],[3,-4,4,-3,3,4,-2,-9,-6,2],[-2,9,4,5,3,5,-1,-1,10,3],[-9,-9,-7,9,-3,7,1,-9,10,-3],[9,6,-6,-5,2,-2,-3,1,-1,-3],[-1,-8,-10,9,8,-2,-9,6,-7,2],[9,2,6,1,-4,-10,9,-9,-4,9],[-10,8,9,-5,-5,8,2,5,3,-5],[-4,-2,-2,2,-9,7,-9,-9,1,5],[-2,1,4,3,-5,4,3,4,5,1],[-8,3,7,8,-5,-7,7,-2,5,-8],[-6,-4,8,-2,6,7,4,-3,-2,-1],[5,6,6,-5,-7,-3,-5,10,7,-6],[-9,-8,5,-6,-6,7,-2,5,3,9],[3,3,-1,9,6,4,8,-8,5,1],[-8,-3,1,10,-8,-6,-3,6,3,-5],[-1,-2,-10,4,-4,-9,3,-7,-1,-2],[6,-9,8,-6,-3,8,9,-6,4,-4],[-5,3,6,4,-6,8,4,-2,5,3],[-8,-5,-3,-6,1,5,5,-3,9,10],[-6,7,6,-2,7,2,-6,-4,9,8],[-2,-5,-3,9,8,5,-8,3,4,-8],[3,-8,-10,-10,2,7,10,-10,10,3],[1,-1,-2,4,2,-9,-3,-3,-9,1],[10,-5,10,3,9,10,-6,8,5,-8],[-5,1,-3,-2,-9,4,-1,-2,-6,-4],[3,-4,5,8,5,7,2,9,-4,6],[6,-3,-10,-1,-7,3,7,8,-1,-1],[4,-8,8,2,10,3,9,-4,-8,9],[-10,-7,2,-8,-6,9,9,-8,5,-8],[9,3,-7,9,4,5,10,10,1,-5],[8,-9,-1,5,7,3,5,2,-4,1],[10,-9,-10,-4,-8,-8,-3,3,-1,2],[-2,-4,4,10,8,6,-7,-8,-4,8],[1,8,2,-10,10,3,-10,10,2,9],[-3,-9,10,9,-10,-7,4,7,-7,-1],[10,2,10,3,3,-3,7,-7,9,-4],[-3,-4,-6,-3,9,-3,-9,-8,-6,2],[-4,-4,-6,9,-6,-6,4,6,-2,-5],[4,-9,-1,-1,-7,4,7,-4,8,-10],[-8,3,-8,-2,-9,-9,-4,-3,5,-10],[6,-6,4,6,5,6,2,-5,-10,9],[5,10,6,4,9,6,10,8,1,-5],[8,10,-1,-8,-6,-8,-7,-10,-6,-4],[8,2,-1,-3,-2,9,-8,-10,7,-9],[7,4,10,6,-8,-2,-2,6,3,-6],[-6,5,-7,6,-2,-5,-4,4,-2,-1],[3,-7,-10,-6,2,9,8,-5,-10,-9],[8,3,2,8,-8,-6,-4,3,8,6],[3,2,-1,8,-8,4,-8,7,-4,6],[6,10,7,-6,5,6,9,-3,5,-2],[6,-10,-4,-8,4,10,-8,-3,-6,-9],[-3,10,3,4,5,-2,5,7,8,8],[9,-5,-8,1,7,6,-5,2,10,-5],[-4,-5,-6,8,8,-8,-6,6,-1,-8],[9,8,10,1,8,4,10,2,-4,1],[-6,10,4,-6,7,3,9,1,1,-1],[7,-2,-9,-4,-5,-4,8,3,-4,-6],[4,-6,-1,4,8,-5,-3,3,-1,4],[3,-9,3,-2,-10,5,-8,-10,-7,-4],[-2,-9,6,-8,10,5,9,2,-5,-9],[3,-10,7,1,-6,1,6,2,2,10],[-1,5,10,-2,-4,-9,-6,-9,1,-7],[6,5,-7,-5,7,3,2,-8,7,-5],[-2,9,7,3,7,5,9,5,-6,-7],[6,1,-1,-10,2,1,-2,-3,6,7],[5,7,1,-10,-2,2,-10,-8,3,-9],[-3,-10,-9,-2,-9,8,-10,-10,9,-9],[-8,9,-3,8,4,4,8,-10,7,3],[2,3,-8,-4,4,6,-4,1,3,-7],[5,-4,-5,1,8,-9,-5,4,-7,8],[6,3,-2,-9,-4,-2,8,-3,10,-5],[5,-1,-8,2,7,-7,6,3,4,1],[-8,6,-10,-7,10,1,5,6,8,9],[7,-8,-5,1,3,-9,6,7,4,-8],[-7,2,10,-7,7,8,1,-9,7,8],[-1,-2,-2,-4,-6,-3,-1,5,4,-4],[8,-4,-7,5,-2,-7,10,3,10,-8],[-2,-9,7,-8,6,1,3,-2,10,-6],[2,9,-3,-4,10,1,-3,6,-6,1],[6,7,9,2,1,-4,-1,5,-5,-9],[10,-8,-2,-3,9,-10,7,-4,1,8],[4,-2,-6,9,5,6,-9,8,-9,8],[4,2,-9,8,4,1,7,-3,2,2],[-1,3,-3,9,-4,9,-9,9,-7,8],[-2,-7,2,-2,3,4,-4,-4,-9,-10],[-2,-1,8,-10,7,-6,9,-10,5,-7],[-7,2,7,-10,-9,-1,9,-3,-2,-2],[3,1,-1,-4,2,7,-2,1,-3,8],[-1,-2,-1,-5,-9,3,7,3,5,-6],[-7,-4,-2,-10,6,-6,7,5,-4,-2],[-9,5,10,-4,5,2,3,-3,-1,-9],[-1,1,-4,5,-7,10,-3,-2,3,6],[7,2,-3,4,-7,10,9,-5,10,-10],[-8,-4,7,4,3,-10,7,10,-6,-6],[7,-1,9,-9,8,5,2,-9,-5,-1],[-2,-9,-2,10,3,-10,-2,-9,7,-10],[-9,-4,-4,4,-3,-8,-5,-3,5,-4],[9,-1,5,4,9,-10,8,-1,-5,2],[7,3,8,-10,1,-3,8,-3,-5,-4],[8,-1,7,9,-7,2,-10,8,2,4],[2,4,-3,-2,2,1,1,8,-5,2],[7,-8,10,8,-5,-7,-10,-6,8,9],[5,1,3,-6,8,4,3,-4,-9,-6],[3,-3,4,3,-9,-1,-4,2,2,10],[5,5,6,-10,-10,-1,-10,5,6,-6],[-4,-1,9,-10,1,-3,5,-4,-7,-8],[-3,-1,5,-8,8,8,-1,2,2,3],[1,-2,3,-7,-2,-9,-6,-1,8,4],[5,8,8,-8,-10,-4,8,-7,-1,1],[-1,-2,1,-10,3,5,-3,-4,10,3],[-4,1,2,2,6,1,-6,-6,6,-7],[9,5,-2,-5,2,2,-5,-7,-5,-2],[-4,8,-6,8,2,1,7,3,6,2],[6,-3,9,7,8,-4,-4,6,-9,-2],[-2,-2,10,8,3,-1,4,-9,-3,-8],[8,7,6,-2,8,6,8,6,-3,-3],[4,7,-9,4,5,-4,6,4,5,-7],[-1,-2,10,6,-4,-2,-4,-8,-7,6],[-6,6,-2,-4,-6,9,-7,-6,-8,-2],[3,3,-3,10,-5,4,7,-3,-8,-7],[1,2,6,7,-2,8,-3,3,-2,-7],[-1,8,1,-8,-10,7,-2,1,9,-6],[5,6,-5,-7,6,-3,7,7,-5,-8],[2,8,4,-4,5,6,3,1,5,-4],[2,-7,1,6,9,-10,-1,4,8,-10],[7,-5,10,-8,-4,3,10,-2,4,-6]], dtype = "uint64")#candidate|5274|(130, 10)|const|uint64
call_5272 = func_3494_call(relay.reshape(var_5273.astype('uint64'), [10, 13, 1]), relay.reshape(const_5274.astype('uint64'), [10, 13, 10]), )
call_5275 = func_3494_call(relay.reshape(var_5273.astype('uint64'), [10, 13, 1]), relay.reshape(const_5274.astype('uint64'), [10, 13, 10]), )
func_697_call = mod.get_global_var('func_697')
func_701_call = mutated_mod.get_global_var('func_701')
var_5295 = relay.var("var_5295", dtype = "uint64", shape = (160,))#candidate|5295|(160,)|var|uint64
call_5294 = relay.TupleGetItem(func_697_call(relay.reshape(var_5295.astype('uint64'), [4, 5, 8]), relay.reshape(var_5295.astype('uint64'), [4, 5, 8]), ), 0)
call_5296 = relay.TupleGetItem(func_701_call(relay.reshape(var_5295.astype('uint64'), [4, 5, 8]), relay.reshape(var_5295.astype('uint64'), [4, 5, 8]), ), 0)
output = relay.Tuple([uop_5268,call_5272,var_5273,const_5274,call_5294,var_5295,])
output2 = relay.Tuple([uop_5268,call_5275,var_5273,const_5274,call_5296,var_5295,])
func_5306 = relay.Function([var_5273,var_5295,], output)
mod['func_5306'] = func_5306
mod = relay.transform.InferType()(mod)
var_5307 = relay.var("var_5307", dtype = "uint64", shape = (130,))#candidate|5307|(130,)|var|uint64
var_5308 = relay.var("var_5308", dtype = "uint64", shape = (160,))#candidate|5308|(160,)|var|uint64
output = func_5306(var_5307,var_5308,)
func_5309 = relay.Function([var_5307,var_5308,], output)
mutated_mod['func_5309'] = func_5309
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5920 = relay.var("var_5920", dtype = "float64", shape = (13, 16, 13))#candidate|5920|(13, 16, 13)|var|float64
uop_5921 = relay.tan(var_5920.astype('float64')) # shape=(13, 16, 13)
output = relay.Tuple([uop_5921,])
output2 = relay.Tuple([uop_5921,])
func_5923 = relay.Function([var_5920,], output)
mod['func_5923'] = func_5923
mod = relay.transform.InferType()(mod)
var_5924 = relay.var("var_5924", dtype = "float64", shape = (13, 16, 13))#candidate|5924|(13, 16, 13)|var|float64
output = func_5923(var_5924)
func_5925 = relay.Function([var_5924], output)
mutated_mod['func_5925'] = func_5925
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6382 = relay.var("var_6382", dtype = "int16", shape = ())#candidate|6382|()|var|int16
const_6383 = relay.const([[[6,5,-2,-3,5,7,-9,9,1,-2,-6,-6,-7,4,-6],[8,-6,7,9,4,-5,1,4,-1,3,-8,10,-9,-8,5],[-8,7,-7,10,4,1,7,-3,-3,5,-10,4,-9,-9,6],[1,8,-5,-2,-2,-1,6,-6,-10,-3,-2,10,-5,8,7],[9,-9,-6,3,-1,6,9,-1,-1,3,-8,9,2,8,-9],[6,-1,-6,-9,-8,-5,2,8,-8,-6,5,7,-1,-7,8],[4,-5,-7,3,-1,6,-7,9,-4,6,-9,6,-4,-2,6],[6,-4,-4,-3,6,-9,-9,3,-6,6,-8,3,-8,1,-8],[10,8,5,4,10,-4,-4,-7,-3,-3,5,4,5,6,4],[4,8,-9,-3,-2,4,-2,-1,5,-4,-2,10,-6,10,1],[-6,1,7,8,4,3,-8,-6,5,-2,10,7,-10,4,-7],[-7,2,-6,9,-10,-7,-2,-9,-3,-10,5,-9,-1,-7,2],[-2,6,6,-4,9,-7,-9,1,-7,-4,9,8,-4,-8,4],[5,-8,9,-5,8,-8,-8,4,-5,-4,-10,10,3,-9,-5],[1,-8,-10,-3,-3,-9,-8,8,-10,4,5,9,6,-7,2]],[[-5,-1,4,-3,8,-9,-6,8,10,-8,2,-2,9,4,10],[-10,-1,-9,4,-3,7,1,-1,-7,5,-7,1,9,-5,7],[-10,-2,10,5,3,-6,2,-4,-6,-5,-6,-9,4,-8,2],[-6,-4,3,-10,-10,8,5,-5,4,8,4,4,1,-3,6],[-4,-10,-9,-4,1,3,-4,-3,7,-10,-9,-9,10,-10,10],[-10,8,-5,-1,9,-7,-5,-1,7,6,-3,4,9,-3,-6],[-6,-9,6,-3,-5,3,5,10,-6,5,6,10,-1,5,7],[9,10,8,-2,-5,5,6,5,7,-4,-7,10,2,6,7],[9,-7,-4,4,-7,-2,6,2,3,-5,2,7,1,7,-7],[1,10,6,2,-9,-9,-1,8,-6,-5,-8,-5,2,6,-3],[2,10,3,-6,-6,-6,-8,7,2,-5,-6,-5,7,9,5],[-6,-8,-10,4,6,5,-2,8,-6,-5,-9,-7,-6,-2,-8],[6,7,-4,-5,-5,8,-2,2,2,-2,3,1,-8,4,9],[8,-10,9,3,2,-4,9,-1,-6,1,1,1,-3,7,10],[1,-3,-4,5,-8,-5,-7,6,5,2,-2,-9,-5,4,4]],[[-9,-4,8,-5,-3,-1,-5,3,8,-5,-2,-5,4,7,-1],[-3,-6,3,5,6,-2,8,-7,1,7,-8,-7,-1,-3,10],[-9,-6,-2,-8,10,-8,-1,2,-7,3,-10,-4,4,-9,-8],[-2,-6,2,9,6,4,-2,2,2,8,7,8,7,9,-8],[-7,-3,-9,10,7,-7,-3,5,-4,7,4,-10,-5,6,-4],[-2,5,5,-2,-5,-2,9,1,3,3,-5,-3,-1,3,6],[-2,-8,6,4,-8,-9,9,-6,-2,-8,-8,-3,-10,-3,10],[8,-8,10,10,3,10,8,10,2,4,6,-4,7,3,-7],[-9,-6,3,-2,9,3,-9,-1,-9,-10,4,7,7,4,-3],[-5,-7,-1,9,7,9,9,3,7,-2,4,-3,4,8,1],[8,-4,-9,7,-8,-7,-6,-5,4,-8,-8,-2,7,2,5],[-7,-1,10,-7,9,-3,4,-3,-6,-10,-3,1,1,3,-3],[7,1,-2,10,-10,-5,-5,2,-8,3,5,8,5,-5,-1],[9,10,-9,-3,-2,-8,-5,7,-9,6,-5,-1,-8,-10,-5],[1,2,3,6,10,8,6,-9,9,-10,-3,5,-7,10,-7]],[[-2,-8,2,6,9,5,-4,-9,3,-2,-2,-9,-8,-1,6],[5,8,2,7,5,6,3,10,2,9,-8,10,1,6,10],[2,9,9,10,-1,-1,-5,-6,6,10,-5,-10,8,7,-5],[-7,10,-7,-9,-4,3,9,10,5,-5,-5,5,-5,9,10],[-7,-3,3,6,8,-6,5,-9,1,5,10,6,7,2,-5],[4,-7,1,-8,4,6,8,-5,8,-2,-4,7,10,5,-2],[2,2,-2,1,-9,7,-7,9,-4,10,4,-8,5,-4,10],[1,-1,-3,-8,-4,-9,6,-8,10,4,7,3,8,5,-10],[-8,-9,6,4,6,4,-3,-3,-5,-4,-10,-6,8,5,-6],[10,-6,4,1,-9,-10,-2,3,-3,-8,-9,7,3,1,-9],[-3,-10,-8,-2,-4,3,5,-6,-3,-9,3,-9,-3,-6,-10],[-1,5,-3,-8,1,-7,-6,2,-3,9,3,-7,-4,7,-5],[6,2,-7,-4,10,-7,-2,1,6,-8,-5,-9,-7,5,3],[-1,-7,-10,-7,-9,10,4,-2,-5,-9,3,7,-6,-5,6],[-2,6,-1,-4,-1,-5,-1,-2,-6,-9,-1,10,-4,-2,-9]],[[8,-7,-1,-1,7,7,2,3,-3,2,-7,-4,-2,-3,-9],[3,4,-2,-10,-9,4,3,8,-1,-6,-2,-5,-7,-7,1],[3,-3,-6,3,7,-7,9,-10,-5,-5,3,3,4,-7,2],[-8,4,3,6,9,9,-6,-3,7,-7,-6,-10,8,-1,-8],[5,-10,-5,10,-1,5,-3,10,9,-4,10,5,-1,5,-2],[-6,8,5,-1,5,5,1,4,6,9,-8,-9,8,-9,-1],[7,-7,3,8,-10,5,-4,-5,-10,-2,8,7,-6,-5,-1],[6,-4,-2,-9,-1,3,4,6,8,10,-6,-1,-4,-9,1],[-5,-7,4,-8,-10,-1,6,-4,7,-10,-1,3,-9,-8,6],[-8,8,4,5,-2,10,9,1,10,-5,-4,7,10,-4,4],[-8,3,-8,-6,8,7,3,7,9,-1,10,-3,-3,-2,-1],[-7,1,-3,-8,1,8,7,5,-5,-3,-1,4,-1,6,3],[2,-6,-3,-1,9,8,-9,9,1,8,-2,9,4,-2,3],[-10,7,-9,7,1,1,1,6,-6,4,3,5,-2,1,-1],[-1,-1,-7,9,10,7,-1,3,-8,6,-5,10,10,10,5]],[[-6,-2,-5,9,2,3,-5,10,2,9,4,7,-3,-3,6],[4,-8,-3,5,8,3,9,-6,8,-10,7,8,-5,1,-5],[10,3,4,-3,-7,-6,-2,10,5,7,-2,7,-8,-2,4],[10,-5,-2,-6,-9,3,5,10,3,-1,1,7,-3,4,-6],[5,2,8,10,-10,6,4,-1,5,2,-4,-9,-4,-6,2],[-7,-9,-6,5,-10,4,-8,-7,3,-3,-10,-9,-10,5,-1],[9,3,-9,4,4,-10,-9,-7,9,10,4,-1,-3,7,-8],[-5,8,-6,7,-2,-3,9,3,10,-5,-4,-2,-5,-7,-5],[1,-3,-9,8,8,-7,4,-4,-2,-9,-5,-10,-7,4,-5],[8,-8,-7,-9,-3,6,-9,-7,-7,5,8,8,-9,-10,10],[1,-3,8,-7,6,-5,1,-1,7,7,-4,4,-4,-7,-5],[2,-5,-6,-7,-2,-5,5,3,4,6,3,-8,-1,1,7],[-3,3,-5,10,4,-9,1,4,-2,5,10,9,9,2,-6],[-6,-9,-8,10,8,-2,-10,1,-10,-4,2,-6,-4,10,5],[-5,6,1,-10,-4,2,7,10,10,2,6,8,4,-5,9]],[[2,-2,-10,2,4,8,1,-10,3,2,3,-9,8,-4,10],[4,7,-10,-8,5,-8,8,8,2,-9,7,2,3,-9,-4],[10,1,-3,6,-3,3,-6,3,-2,-5,1,3,8,-3,6],[-8,-7,-6,9,-4,-3,-4,-10,2,1,-5,9,-4,-5,-6],[8,9,-2,-6,5,3,-8,6,1,-2,-5,-3,-4,-3,-5],[1,-2,9,-3,7,6,9,-7,4,5,10,-2,6,1,-6],[-6,-2,-7,-4,-7,-2,3,8,6,-5,7,-1,-8,6,4],[-8,9,3,-10,-8,-10,-1,-2,10,-3,1,2,-1,-6,-2],[9,5,7,-5,4,5,6,6,8,-9,3,-1,1,5,-10],[-10,-4,-8,2,1,9,-10,3,6,-2,-2,-5,9,-6,-3],[-9,5,7,-8,7,5,-5,-10,10,10,10,-8,5,-9,2],[-7,-5,6,-8,-1,2,-8,2,5,-3,-6,9,8,-1,-6],[8,-6,8,7,6,8,5,-5,5,8,7,2,10,-9,-6],[-6,10,7,3,3,-5,7,10,-6,-4,-2,-2,8,-4,-5],[-3,3,2,-1,-8,-4,7,3,-3,-2,-7,7,-1,-1,1]]], dtype = "int16")#candidate|6383|(7, 15, 15)|const|int16
bop_6384 = relay.left_shift(var_6382.astype('int16'), const_6383.astype('int16')) # shape=(7, 15, 15)
func_1211_call = mod.get_global_var('func_1211')
func_1214_call = mutated_mod.get_global_var('func_1214')
const_6389 = relay.const([7.664268,-3.374421,-2.146634,-6.989809,-1.742337,-7.846521,-9.310463,8.434450,-0.104409,4.667634,-5.585388,-1.315983,-4.696889,6.981115,-7.561909,-3.732271,-8.301157,0.996158,-5.571501,3.367780,7.766960,-7.095478,-4.043976,5.170817,0.718275,8.589616,3.467460,-7.741723,-8.369836,5.612913,-7.652229,5.559102,6.470071,7.197427,-1.963526,-9.124539,8.023572,6.964269,-9.280579,-7.015984,1.251492,-0.216232,9.155346,3.596686,-2.119846,6.162826,-2.810937,8.661837,8.970050,8.172844,8.178667,4.221101,1.114041,-4.078835,3.320994,3.501576,-4.895431,-4.215531,-8.330697,-2.235178,-1.017545,8.753979,-9.109597,-6.959027,2.315238,9.871545,-4.631856,3.285560,4.373846,5.608918,-4.413549,3.649180,-4.800671,6.845178,1.930334,2.863399,7.319869,8.861694,-7.883481,3.376890,7.116773,-7.151232,4.135649,4.279166,-4.999852,-0.062983,5.159816,2.418866,0.337964,-9.500182,-3.528439,-4.306687,-4.442989,6.443888,-3.224428,7.238864,0.365074,2.887498,6.025639,5.404761,9.262076,7.429021,-2.666780,6.031076,2.591534,-6.084545,9.907883,6.642845,-5.364897,-6.290794,4.896687,8.770141,-5.339141,8.507576,5.087938,0.335228,-5.754729,-8.194878,3.453298,-2.642592,5.232326,3.113051,-4.103362,0.991553,4.225112,5.852483,0.973979,-6.197800,5.485997,4.454207,-7.042532,6.579709,0.991560,6.054290,1.133837,4.676440,6.359982,-9.579311,4.484580,-8.884186,9.542617,6.307629,-6.595701,-1.726063,-2.054696,2.985946,-7.406240,6.379032,-1.024858,9.038970,1.443995,-9.114254,4.590418,-8.755488,-5.782544,8.866085,-0.599626,-6.347284,-1.913884,-1.714186,6.402812,-8.606296,-4.660987,9.787640,-2.270804,2.621962,-9.444545,-0.368342,-3.532961,-0.857535,-9.399845,-2.550781,2.162204,1.059715,-9.306201,-9.759214,3.004249,9.607914,-0.187906,-7.526624,1.594706,-2.896167,-5.476526,1.117676,1.365523,8.296320,-0.488042,-6.055188,9.806444,2.966356,5.264358,7.666214,-1.817900,7.548597,1.201686,-0.500468,2.571172,-8.986509,6.318286,-0.595868,-2.109064,-0.805922,8.317679,-4.498022,0.013266,-5.403381,0.879283,2.250645,0.907660,-3.702059,9.965420,8.648248,-6.848420,-6.954596,-1.750833,-8.580288,-0.975739,2.476390,-9.547278,-9.854855,2.410073,-1.574372,-3.059304,6.230619,-5.471306,9.118522,-9.036455,-7.364176,-7.261593,-4.227150,4.991497,6.815575,-6.207950,-8.088597,-9.373982,-8.467077,0.756680,-6.280225,-2.147295,4.488717,-9.464719,-1.980169,-4.965313,5.883740,2.754013,1.465074,-7.589409,1.918329,9.489156,4.402157,-4.259065,5.009309,5.240420,-0.291628,3.688916,-9.405281,-9.511188,-0.482623,-2.868101,7.117665,-5.045020,-0.801067,-0.237543,5.590605,3.152511,2.953334,-4.218336,-8.819136,5.748624,1.193294,-8.607987,-4.442396,8.814009,1.958493,-3.837172,6.321767,8.596682,5.066442,7.483625,6.609551,-9.783329,0.597312,-3.911666,-8.928845,-6.635349,-8.276566,2.827519,1.398363,-3.501083,-1.188237,8.091996,2.054268,-2.470389,-3.059397,7.830625,-2.443812,8.036927,-5.275462,5.325987,9.881389,-7.858560,7.746447,-6.264352,-2.606794,7.180558,5.696304,1.577068,-1.120051,1.438744,7.440812,-5.766037,-4.646954,3.227345,5.912289,9.462263,-5.557102,3.819329,-8.942983,-6.713374,-0.682623,8.984673,8.581229,-5.566964,-5.884223,-0.099595,-1.423023,-5.504103,-6.285242,2.971107,-0.798541,-5.681523,-1.283330,-1.389333,5.123463,-6.607539,0.802341,8.301756,-6.325170,-8.101502,-2.519096,-2.504151,9.912467,5.988438,0.560050,-5.274079,-1.963652,-2.124388,-1.566591,5.143205,-9.324349,4.135456,5.865307,-6.171191,-4.757466,7.891948,5.231848,7.124776,-7.105813,1.361014,9.036784,9.114136,-1.841376,-4.221076,6.384549,8.329760,2.413364,2.021584,2.369319,-3.090356,-2.188202,-0.451828,-4.904439,-8.664151,9.982700,-7.843096,9.252425,-7.875299,0.101890,-0.751153,-9.606825,-2.295774,-8.480530,-2.901131,2.486643,0.826080,-5.071382,-9.999926,9.367016,1.758435,-7.501339,3.698874,-7.974421,3.792039,9.025462,-1.862116,7.134462], dtype = "float32")#candidate|6389|(396,)|const|float32
call_6388 = relay.TupleGetItem(func_1211_call(relay.reshape(const_6389.astype('float32'), [9, 11, 4])), 0)
call_6390 = relay.TupleGetItem(func_1214_call(relay.reshape(const_6389.astype('float32'), [9, 11, 4])), 0)
output = relay.Tuple([bop_6384,call_6388,const_6389,])
output2 = relay.Tuple([bop_6384,call_6390,const_6389,])
func_6391 = relay.Function([var_6382,], output)
mod['func_6391'] = func_6391
mod = relay.transform.InferType()(mod)
var_6392 = relay.var("var_6392", dtype = "int16", shape = ())#candidate|6392|()|var|int16
output = func_6391(var_6392)
func_6393 = relay.Function([var_6392], output)
mutated_mod['func_6393'] = func_6393
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6537 = relay.const([[[4.357835,5.395491,6.815687,-6.105217,-3.319299,4.310120],[2.050260,9.866190,-8.476643,6.745604,-0.143369,6.021556],[6.027972,5.895189,-4.285847,-6.351885,-6.884748,0.374889]],[[-6.034741,6.692052,5.428086,-7.747110,-0.938647,0.183107],[4.361996,-5.278540,-9.989512,2.682975,-7.899728,-6.401460],[-3.913960,-2.446947,-0.501309,-1.269784,0.285880,-7.809776]],[[-3.115341,4.843857,-5.053476,-0.253899,-8.700426,7.097219],[-7.104211,-4.106311,6.986120,2.619780,7.776191,1.712327],[8.549762,-7.121255,3.308882,-3.612094,2.353975,-0.489585]],[[-3.886799,3.071853,3.771168,-1.922370,-3.119759,-6.788106],[8.827122,1.973934,-2.427033,-0.147188,-7.393133,-3.962926],[6.568691,9.197801,5.031402,-3.665802,-6.108078,-2.970826]],[[-0.969912,-4.044275,7.099152,3.958111,-8.450793,5.567185],[6.130709,5.706266,-5.110779,1.880343,-9.629503,3.022877],[-3.621626,7.717759,6.776106,0.064698,-4.404759,-0.611659]],[[-9.450385,-1.885119,-3.411987,8.497669,-9.312534,8.479926],[4.810030,-8.043327,-9.029071,2.981961,-8.367783,6.010704],[-9.919511,9.481157,-5.259188,-6.500025,2.419808,-8.625327]],[[-2.566776,3.140262,-0.222885,4.389822,1.451535,7.926679],[8.222291,7.528566,1.735027,-3.584024,1.829822,8.819287],[8.844678,-2.915531,-0.123704,6.223718,0.932161,3.026125]],[[6.847381,7.190445,0.155485,-0.773462,9.526640,-2.387911],[0.356311,-5.438655,-0.643298,-2.300961,1.797467,9.835468],[2.719652,-8.513836,7.487033,-2.165184,-5.790890,-5.530582]],[[-5.270828,1.269802,-0.898374,2.256294,-4.632571,-9.922538],[9.627889,-5.563292,5.895951,-6.479147,-2.129014,5.877618],[3.785618,7.038278,9.043000,9.326334,-6.753333,4.770444]]], dtype = "float32")#candidate|6537|(9, 3, 6)|const|float32
uop_6538 = relay.cosh(const_6537.astype('float32')) # shape=(9, 3, 6)
func_3395_call = mod.get_global_var('func_3395')
func_3398_call = mutated_mod.get_global_var('func_3398')
var_6546 = relay.var("var_6546", dtype = "float64", shape = (1008,))#candidate|6546|(1008,)|var|float64
call_6545 = relay.TupleGetItem(func_3395_call(relay.reshape(var_6546.astype('float64'), [9, 8, 14]), relay.reshape(var_6546.astype('float64'), [9, 8, 14]), ), 0)
call_6547 = relay.TupleGetItem(func_3398_call(relay.reshape(var_6546.astype('float64'), [9, 8, 14]), relay.reshape(var_6546.astype('float64'), [9, 8, 14]), ), 0)
func_3117_call = mod.get_global_var('func_3117')
func_3120_call = mutated_mod.get_global_var('func_3120')
const_6564 = relay.const([[5.855662,9.870991,1.010448,5.733177,5.800170,7.672453,6.953151,3.624903,3.583792,9.699107,0.518044,-8.884262,-6.592037,-4.498432,6.808343,1.493724,0.789766,9.161000,7.906572,-8.128624,5.131393,9.492930,-9.973489,1.434965,7.198688,-4.862487,0.407375,7.855841,1.374271,-8.489501,2.829300,7.299818,-3.943082,9.894364,9.667766,0.822176,6.360658,4.668467,9.443389,1.901654,5.865660,0.942366,-8.052035,0.769785,2.138018,-0.057714,9.158102,5.626655,4.783852,-2.703204,-5.718803,1.944943,-1.672941,-8.316826,4.106527,-8.067489,8.338805,8.156747,-0.638732,2.199458,6.375755,-1.477686,4.741694,-7.676017,-2.802825,-6.897705,-3.498310,-6.003483,-4.779950,-9.987265,-2.070639,1.918075,5.720673,4.008551,4.309296,6.374135,-7.186870,0.568403,9.351058,-2.503548,-6.925759,-1.449521,-7.966646,2.553400,4.158389,-3.306319,-8.473190,-2.483363,2.954500,6.621300,-4.547602,1.637226,-1.207986,3.967235,-8.860579,1.686908,-4.659968,-2.656366,-8.314963,7.519096,2.854996,7.075222,8.454116,7.984187,2.636068,3.277365,1.916419,3.757457,-7.847940,4.252873,-3.455431,5.503565,1.756303,-1.724918,-7.046841,7.229337,9.136305,3.257577,-0.022206,2.659015],[-9.595887,-3.070153,2.397085,0.429006,-5.630252,2.005046,-1.086191,3.009220,-7.299374,7.631893,5.600940,-3.059105,-6.737040,-0.239542,3.312186,-7.842808,-2.841758,7.403414,-1.525957,2.754963,-2.620665,-2.771258,-9.819030,-0.174144,9.886382,3.864607,-3.164062,1.571217,7.478202,-1.333738,-9.133567,-2.344586,9.045294,-2.595748,1.833786,-7.106788,-8.467105,-6.926854,-1.140526,9.942071,-9.044347,-3.506695,1.293514,6.837474,9.391851,5.526706,8.442754,7.296399,2.173995,-9.636806,5.141899,-2.438942,3.302937,-4.505103,1.632916,9.392322,-4.536421,4.779831,-5.778729,9.526977,-1.361061,3.737944,-0.456934,-3.283188,-0.032610,-8.016047,6.041699,-4.957237,4.592303,-5.392629,-1.525504,2.579378,3.877876,-3.213580,1.478979,-5.754804,-2.867146,8.912156,-5.647745,9.182791,7.990412,-0.870904,-3.794440,5.307391,-6.905213,6.397492,-2.184776,8.773580,5.365392,6.831647,7.373471,-1.723436,6.250592,6.866365,6.739460,-0.598887,-8.534343,6.948431,4.562444,4.160511,-3.023142,8.371694,1.995629,-4.140181,-3.107061,1.624421,6.650083,-1.712436,-1.206477,-8.338142,-9.181504,-3.439074,-8.809528,8.193519,-5.980603,4.392844,5.628288,4.098230,2.706794,2.230697],[2.218278,-4.014557,-6.385122,2.740613,-4.048767,-7.361522,7.140646,4.942574,-5.350196,3.529604,3.104824,8.728340,3.593106,6.507223,1.720555,0.966519,-1.400363,0.487154,-8.157243,0.191786,5.606323,8.509376,-8.063893,-7.904036,7.227176,5.148274,-5.254213,-3.455707,-1.561647,-0.595398,-2.833108,-3.643787,9.928408,-0.665353,5.609766,-8.132099,0.529164,9.726242,1.802384,7.327520,1.392510,0.476403,1.802224,-2.332326,-5.841665,5.974865,-0.478100,6.012844,-4.497651,7.521536,2.142836,-7.236866,1.810282,-9.041237,0.939963,1.362958,-4.268660,-8.323794,-9.506730,6.273471,5.501803,-3.209544,6.009817,-7.691733,4.339062,3.808346,9.288892,4.992480,4.287216,2.748598,1.454574,0.702333,-0.903508,-3.778268,-0.095837,8.650108,-3.215202,3.656757,4.185605,3.380974,4.814194,6.268600,-8.072069,7.087062,-5.479141,-6.945456,-6.516447,3.015807,9.354510,3.461732,-5.681562,-3.396636,-2.021612,-1.846017,7.051411,-9.702525,-8.726095,6.475619,2.600292,-7.927448,-0.524842,9.012635,-1.394766,7.591542,-6.660630,-5.076036,3.935978,-6.514593,-0.975367,6.900008,-6.169398,9.551003,9.872780,-4.378706,3.792003,-2.526356,2.614272,-8.688836,-4.082741,-5.412381],[2.955243,1.085377,1.310556,-9.123303,-8.186885,8.257699,-0.847396,2.887028,2.967788,-8.255419,-9.527471,-9.660575,-9.129637,-7.452667,-6.178351,-7.511950,2.710340,-8.661051,4.707056,-9.233820,-0.162971,-3.412396,-5.540932,-0.476141,0.634137,9.193193,7.177153,-5.159075,-0.895257,5.605207,2.327350,-1.012895,9.376458,6.515501,-5.246328,6.695396,3.167231,6.035666,4.104022,5.750547,-2.825387,8.660743,3.256907,2.846752,-1.512943,-6.891570,-4.661526,-7.610410,-5.858081,-2.893413,2.248931,8.009367,-5.021808,8.742522,8.414559,-1.489442,2.542796,8.940500,2.106309,-8.615093,9.373811,4.400949,-3.793339,-6.305567,2.970803,5.257993,-4.242239,9.177933,3.136615,-5.912446,-9.303055,-4.422419,-7.888486,-2.385903,-9.653202,2.045986,5.882691,-0.245317,-3.442719,-2.338318,3.454156,2.487466,0.305628,-4.292948,6.294242,1.296694,-2.149240,0.660803,8.991632,-2.092684,-1.772768,-9.804715,0.486698,8.818692,8.555288,5.794311,0.208361,-2.334749,-1.535528,7.050186,7.775209,3.153665,-4.602449,2.398674,-2.131641,-8.751270,5.983930,-6.523429,7.041692,3.162666,-8.727509,8.501180,1.243402,-7.195864,5.651671,8.313990,-3.106461,-9.757078,7.458018,-9.329686]], dtype = "float64")#candidate|6564|(4, 120)|const|float64
call_6563 = relay.TupleGetItem(func_3117_call(relay.reshape(const_6564.astype('float64'), [4, 12, 10])), 0)
call_6565 = relay.TupleGetItem(func_3120_call(relay.reshape(const_6564.astype('float64'), [4, 12, 10])), 0)
func_5306_call = mod.get_global_var('func_5306')
func_5309_call = mutated_mod.get_global_var('func_5309')
var_6575 = relay.var("var_6575", dtype = "uint64", shape = (130,))#candidate|6575|(130,)|var|uint64
const_6576 = relay.const([[2,-7,9,-10,-7,8,7,-10,7,10,9,7,2,10,-9,-1,-4,-7,-2,-9,9,8,5,7,-10,-9,9,-2,-3,7,3,-3,10,1,-9,1,-10,-4,-7,-8],[-7,5,4,1,2,-9,7,1,4,-9,4,2,9,8,8,2,-2,-5,8,4,-5,-4,-7,-10,-9,-7,-9,7,-5,-3,-1,-10,5,3,-1,-3,2,-9,-6,-3],[9,8,-8,-7,9,8,6,7,3,-5,7,-9,7,9,6,-8,1,-5,8,4,2,1,9,-9,8,-7,2,-5,3,-2,-7,5,4,-6,4,4,-3,-3,-5,-7],[6,1,7,9,-9,10,-1,3,-7,-2,1,8,-2,-8,-5,3,6,-1,7,6,3,3,1,1,-7,10,10,-3,8,3,-6,-5,8,9,8,-3,-1,4,4,-9]], dtype = "uint64")#candidate|6576|(4, 40)|const|uint64
call_6574 = relay.TupleGetItem(func_5306_call(relay.reshape(var_6575.astype('uint64'), [130,]), relay.reshape(const_6576.astype('uint64'), [160,]), ), 5)
call_6577 = relay.TupleGetItem(func_5309_call(relay.reshape(var_6575.astype('uint64'), [130,]), relay.reshape(const_6576.astype('uint64'), [160,]), ), 5)
output = relay.Tuple([uop_6538,call_6545,var_6546,call_6563,const_6564,call_6574,var_6575,const_6576,])
output2 = relay.Tuple([uop_6538,call_6547,var_6546,call_6565,const_6564,call_6577,var_6575,const_6576,])
func_6589 = relay.Function([var_6546,var_6575,], output)
mod['func_6589'] = func_6589
mod = relay.transform.InferType()(mod)
var_6590 = relay.var("var_6590", dtype = "float64", shape = (1008,))#candidate|6590|(1008,)|var|float64
var_6591 = relay.var("var_6591", dtype = "uint64", shape = (130,))#candidate|6591|(130,)|var|uint64
output = func_6589(var_6590,var_6591,)
func_6592 = relay.Function([var_6590,var_6591,], output)
mutated_mod['func_6592'] = func_6592
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6661 = relay.var("var_6661", dtype = "float64", shape = (8, 5, 8))#candidate|6661|(8, 5, 8)|var|float64
uop_6662 = relay.log10(var_6661.astype('float64')) # shape=(8, 5, 8)
output = uop_6662
output2 = uop_6662
func_6665 = relay.Function([var_6661,], output)
mod['func_6665'] = func_6665
mod = relay.transform.InferType()(mod)
var_6666 = relay.var("var_6666", dtype = "float64", shape = (8, 5, 8))#candidate|6666|(8, 5, 8)|var|float64
output = func_6665(var_6666)
func_6667 = relay.Function([var_6666], output)
mutated_mod['func_6667'] = func_6667
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6918 = relay.var("var_6918", dtype = "float32", shape = (15, 5, 10))#candidate|6918|(15, 5, 10)|var|float32
uop_6919 = relay.asinh(var_6918.astype('float32')) # shape=(15, 5, 10)
output = relay.Tuple([uop_6919,])
output2 = relay.Tuple([uop_6919,])
func_6921 = relay.Function([var_6918,], output)
mod['func_6921'] = func_6921
mod = relay.transform.InferType()(mod)
mutated_mod['func_6921'] = func_6921
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6922 = relay.var("var_6922", dtype = "float32", shape = (15, 5, 10))#candidate|6922|(15, 5, 10)|var|float32
func_6921_call = mutated_mod.get_global_var('func_6921')
call_6923 = func_6921_call(var_6922)
output = call_6923
func_6924 = relay.Function([var_6922], output)
mutated_mod['func_6924'] = func_6924
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7033 = relay.var("var_7033", dtype = "float64", shape = (13, 1, 14))#candidate|7033|(13, 1, 14)|var|float64
uop_7034 = relay.erf(var_7033.astype('float64')) # shape=(13, 1, 14)
output = relay.Tuple([uop_7034,])
output2 = relay.Tuple([uop_7034,])
func_7045 = relay.Function([var_7033,], output)
mod['func_7045'] = func_7045
mod = relay.transform.InferType()(mod)
var_7046 = relay.var("var_7046", dtype = "float64", shape = (13, 1, 14))#candidate|7046|(13, 1, 14)|var|float64
output = func_7045(var_7046)
func_7047 = relay.Function([var_7046], output)
mutated_mod['func_7047'] = func_7047
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7370 = relay.var("var_7370", dtype = "uint8", shape = ())#candidate|7370|()|var|uint8
const_7371 = relay.const([[[7,3,1,7,-2,4,4,-1],[6,2,2,8,10,1,-9,1],[6,5,9,-1,3,-9,1,8],[1,3,-7,-5,2,6,5,-7],[-5,-10,6,-7,9,8,5,-7],[-7,10,-3,1,-1,7,8,8],[-6,-8,-10,-3,-3,8,6,-4],[10,-7,9,8,-6,-5,-9,-8],[1,-7,-2,-9,1,1,-7,-8],[-1,9,2,-7,10,-3,-6,4],[-6,8,1,-1,7,8,10,-10]],[[-3,-8,-4,-5,8,-5,-6,2],[10,-2,-7,3,-6,9,-9,5],[-8,8,10,10,1,4,4,1],[-6,-5,5,-1,9,9,1,-3],[-8,2,-4,8,8,5,6,6],[-9,6,-10,-9,7,8,-1,-8],[2,9,-2,3,8,4,4,-7],[2,10,-2,-1,-6,-8,2,8],[-4,1,-3,-8,2,7,3,-10],[-9,6,-9,2,-8,2,4,3],[6,-6,6,-4,-7,6,-4,4]],[[7,7,-9,-1,7,4,-5,1],[-10,-2,2,-7,-6,-10,9,6],[-6,-4,-9,-1,-10,10,-3,-7],[-10,1,5,-3,-1,1,-9,-6],[9,-1,4,-9,-8,-8,-9,-5],[-3,1,4,-1,6,-5,-1,1],[2,8,-5,-10,5,-7,-4,5],[9,-7,1,8,-2,-4,3,-2],[-9,-10,-7,-1,-2,-1,1,8],[-2,-2,5,-10,-2,-9,-10,-1],[1,-5,-6,3,5,6,9,-7]],[[-9,6,1,-10,-2,10,-7,-3],[4,7,6,-10,5,10,-10,-7],[-6,-4,2,-1,-2,-8,-4,7],[1,-10,7,2,7,-6,-9,-7],[-7,-3,2,3,5,-3,2,-6],[8,-10,7,-5,-3,3,-5,6],[-9,10,3,7,5,-6,4,10],[10,-6,-3,3,-5,8,7,1],[5,1,-7,5,-10,8,4,7],[7,5,6,6,4,-1,-9,9],[8,-1,8,-8,8,-6,6,-10]],[[-7,-3,-3,-4,4,-10,-8,7],[8,-2,6,7,-5,-10,-6,-4],[-3,8,9,-3,-7,-5,1,-2],[10,7,1,-3,9,-9,-4,-10],[3,5,9,-4,10,-1,1,-3],[-7,-8,8,-9,7,-4,3,1],[3,6,3,-8,9,-7,-5,1],[3,-2,-5,8,9,4,-9,7],[-3,1,5,1,9,4,10,-7],[7,4,8,-3,-7,8,3,5],[8,-2,-5,7,-10,-9,-6,-3]],[[-6,2,-10,-3,-1,-10,-6,-8],[1,9,2,-4,-7,-5,9,-6],[7,-9,1,4,4,-6,-9,7],[6,-9,-4,-3,6,-5,-5,10],[-9,9,-2,3,4,-6,-6,6],[3,-10,-8,9,10,9,-7,7],[9,-5,8,-6,-9,-7,7,7],[-9,-6,-2,1,1,7,-10,-3],[2,-1,-7,-3,3,-1,3,10],[-9,-9,5,4,7,-5,8,7],[5,-8,-6,1,1,10,2,-6]]], dtype = "uint8")#candidate|7371|(6, 11, 8)|const|uint8
bop_7372 = relay.bitwise_xor(var_7370.astype('uint8'), const_7371.astype('uint8')) # shape=(6, 11, 8)
func_982_call = mod.get_global_var('func_982')
func_984_call = mutated_mod.get_global_var('func_984')
var_7379 = relay.var("var_7379", dtype = "float64", shape = (832,))#candidate|7379|(832,)|var|float64
call_7378 = relay.TupleGetItem(func_982_call(relay.reshape(var_7379.astype('float64'), [4, 16, 13])), 2)
call_7380 = relay.TupleGetItem(func_984_call(relay.reshape(var_7379.astype('float64'), [4, 16, 13])), 2)
func_7045_call = mod.get_global_var('func_7045')
func_7047_call = mutated_mod.get_global_var('func_7047')
const_7395 = relay.const([4.796163,6.776283,7.628936,-3.687636,5.468685,-4.793376,4.519200,-0.159265,9.264477,-2.866468,0.867793,-3.123498,8.469393,8.038421,-1.514926,-5.276154,-9.600846,2.065524,-8.627158,3.841972,0.876472,0.389081,-5.356059,3.398922,-4.692012,-0.592420,5.952612,-2.082746,-5.696138,-3.220749,-9.173566,-5.398261,-6.522499,-3.525746,4.050078,-4.279180,-8.740554,-1.162412,0.352587,-9.034260,2.503708,9.458720,2.231932,8.382098,-3.177705,-4.098366,4.437112,1.449544,9.312696,-8.961345,-8.149719,7.933159,6.979383,3.743118,4.055555,-4.234504,-8.396021,6.855897,1.621421,6.349238,-4.405698,-4.054298,8.542700,5.489644,-0.892973,2.903137,-4.988431,7.680968,-7.996579,-3.828568,-2.182662,3.624003,1.638048,-6.559119,7.414827,-4.406163,4.113845,1.316431,-9.525183,2.537380,9.049678,4.515830,0.289198,9.405902,1.802232,3.569577,-8.709369,-4.927975,-0.446232,0.793089,8.147900,3.731658,-4.995749,2.470573,-1.375924,3.142772,0.447519,1.055365,9.534624,1.095777,1.879310,-6.464660,0.051333,3.713289,5.212664,0.872700,-4.266281,-6.410886,-8.692877,6.948487,-0.216881,-8.111281,-6.836605,2.319680,-7.432051,-0.978316,1.906793,1.019346,-8.370133,-5.304408,1.341877,-7.962612,3.286461,3.838489,-1.522615,-2.752830,6.801064,-8.362044,-9.418647,-7.760089,-8.873347,-6.802100,9.280009,-5.218579,-1.025686,-5.495625,9.929537,7.934368,6.925654,-5.875437,-0.403280,-3.193184,5.616587,7.233656,-6.562575,-7.563917,-7.526183,4.201569,-8.885743,1.407009,-8.929373,1.441089,-5.067302,-4.800923,5.573642,7.358161,9.758127,2.255362,4.154613,4.596367,-1.180604,-8.233438,-8.090975,1.952395,-9.330383,-5.262192,-3.321866,-9.849085,-2.124643,-5.083926,1.268801,5.074331,5.245195,8.990588,9.018225,3.104007,-9.616931,2.094494,7.793235,0.106411,2.945214,-7.774434], dtype = "float64")#candidate|7395|(182,)|const|float64
call_7394 = relay.TupleGetItem(func_7045_call(relay.reshape(const_7395.astype('float64'), [13, 1, 14])), 0)
call_7396 = relay.TupleGetItem(func_7047_call(relay.reshape(const_7395.astype('float64'), [13, 1, 14])), 0)
output = relay.Tuple([bop_7372,call_7378,var_7379,call_7394,const_7395,])
output2 = relay.Tuple([bop_7372,call_7380,var_7379,call_7396,const_7395,])
func_7397 = relay.Function([var_7370,var_7379,], output)
mod['func_7397'] = func_7397
mod = relay.transform.InferType()(mod)
mutated_mod['func_7397'] = func_7397
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7397_call = mutated_mod.get_global_var('func_7397')
var_7399 = relay.var("var_7399", dtype = "uint8", shape = ())#candidate|7399|()|var|uint8
var_7400 = relay.var("var_7400", dtype = "float64", shape = (832,))#candidate|7400|(832,)|var|float64
call_7398 = func_7397_call(var_7399,var_7400,)
output = call_7398
func_7401 = relay.Function([var_7399,var_7400,], output)
mutated_mod['func_7401'] = func_7401
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7759 = relay.var("var_7759", dtype = "float64", shape = (6, 4, 11))#candidate|7759|(6, 4, 11)|var|float64
uop_7760 = relay.tan(var_7759.astype('float64')) # shape=(6, 4, 11)
bop_7763 = relay.less(uop_7760.astype('bool'), relay.reshape(var_7759.astype('bool'), relay.shape_of(uop_7760))) # shape=(6, 4, 11)
func_6921_call = mod.get_global_var('func_6921')
func_6924_call = mutated_mod.get_global_var('func_6924')
var_7774 = relay.var("var_7774", dtype = "float32", shape = (1, 750))#candidate|7774|(1, 750)|var|float32
call_7773 = relay.TupleGetItem(func_6921_call(relay.reshape(var_7774.astype('float32'), [15, 5, 10])), 0)
call_7775 = relay.TupleGetItem(func_6924_call(relay.reshape(var_7774.astype('float32'), [15, 5, 10])), 0)
bop_7782 = relay.multiply(var_7774.astype('int8'), relay.reshape(call_7773.astype('int8'), relay.shape_of(var_7774))) # shape=(1, 750)
bop_7785 = relay.multiply(var_7774.astype('int8'), relay.reshape(call_7775.astype('int8'), relay.shape_of(var_7774))) # shape=(1, 750)
output = relay.Tuple([bop_7763,bop_7782,])
output2 = relay.Tuple([bop_7763,bop_7785,])
func_7792 = relay.Function([var_7759,var_7774,], output)
mod['func_7792'] = func_7792
mod = relay.transform.InferType()(mod)
mutated_mod['func_7792'] = func_7792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7792_call = mutated_mod.get_global_var('func_7792')
var_7794 = relay.var("var_7794", dtype = "float64", shape = (6, 4, 11))#candidate|7794|(6, 4, 11)|var|float64
var_7795 = relay.var("var_7795", dtype = "float32", shape = (1, 750))#candidate|7795|(1, 750)|var|float32
call_7793 = func_7792_call(var_7794,var_7795,)
output = call_7793
func_7796 = relay.Function([var_7794,var_7795,], output)
mutated_mod['func_7796'] = func_7796
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7909 = relay.var("var_7909", dtype = "float32", shape = (12, 2, 15))#candidate|7909|(12, 2, 15)|var|float32
var_7910 = relay.var("var_7910", dtype = "float32", shape = (12, 2, 15))#candidate|7910|(12, 2, 15)|var|float32
bop_7911 = relay.power(var_7909.astype('float32'), relay.reshape(var_7910.astype('float32'), relay.shape_of(var_7909))) # shape=(12, 2, 15)
output = relay.Tuple([bop_7911,])
output2 = relay.Tuple([bop_7911,])
func_7918 = relay.Function([var_7909,var_7910,], output)
mod['func_7918'] = func_7918
mod = relay.transform.InferType()(mod)
mutated_mod['func_7918'] = func_7918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7918_call = mutated_mod.get_global_var('func_7918')
var_7920 = relay.var("var_7920", dtype = "float32", shape = (12, 2, 15))#candidate|7920|(12, 2, 15)|var|float32
var_7921 = relay.var("var_7921", dtype = "float32", shape = (12, 2, 15))#candidate|7921|(12, 2, 15)|var|float32
call_7919 = func_7918_call(var_7920,var_7921,)
output = call_7919
func_7922 = relay.Function([var_7920,var_7921,], output)
mutated_mod['func_7922'] = func_7922
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9473 = relay.var("var_9473", dtype = "float64", shape = (6, 9, 8))#candidate|9473|(6, 9, 8)|var|float64
const_9474 = relay.const([[[0.913320,-0.772753,3.550128,0.995632,-4.001048,-3.990464,5.385422,0.945638],[-8.957512,4.061971,-9.683114,3.832283,-6.043347,-1.780215,-7.630984,-8.698894],[-5.744260,0.116833,1.237807,-1.876687,-1.356569,2.088961,2.272760,1.086977],[2.167701,-1.146315,2.123520,1.927452,8.778278,8.675732,5.115682,6.758806],[-6.886343,4.054809,1.529241,-2.162338,9.117831,-7.110708,-5.206035,-7.650176],[-8.404891,2.971922,-1.473505,9.399685,7.397602,9.575506,-2.077131,-3.945332],[0.111309,-3.220045,7.556414,-2.338481,-5.310160,0.784273,2.453218,-3.805948],[-0.701589,8.734786,-8.183844,6.829633,5.195177,5.845169,3.480543,-0.693403],[7.538080,-9.026382,5.669289,0.109142,8.800581,-4.055037,-8.516024,-9.114030]],[[9.747341,1.958418,-2.723917,0.855566,-9.661614,1.759838,-1.191995,-1.321038],[-5.402869,-7.029150,-7.271892,-3.163054,-6.631387,-1.624405,0.723675,7.832728],[-3.445174,5.167083,9.818198,-6.802004,5.480066,-3.809126,8.510361,8.083192],[4.955450,-1.005037,-9.651322,1.376108,1.372955,1.839616,-9.143208,1.129381],[-1.948551,1.688218,6.064734,5.099836,6.466823,-3.423477,-1.874234,-3.744955],[8.461719,6.332172,2.538846,-0.389736,-9.130836,-4.137590,7.385424,5.869882],[-8.970606,5.652711,-8.518680,-3.205338,-2.492147,5.962191,-7.588579,-9.219653],[-5.727056,5.106655,-9.620831,-7.959502,-5.881350,1.520692,9.973987,9.777140],[5.253933,6.258795,2.451641,3.528970,1.859176,-9.484213,1.867285,1.373009]],[[6.807671,8.000035,3.639479,-9.264779,-2.902872,6.161715,9.787218,1.113314],[0.057385,-7.240199,-0.269998,1.745139,-4.788168,-9.645204,-4.185389,5.315377],[-3.626068,-3.719812,9.732830,9.451735,-5.878642,9.194322,2.828371,3.087925],[4.971575,8.411063,0.097295,3.744373,7.739380,9.177477,-8.526523,3.325212],[-1.752726,-6.560231,-2.790339,7.301618,-4.960142,-4.310067,-6.002555,-4.511130],[-0.655880,1.198256,-0.631825,0.337522,-5.742382,-1.123382,-8.845020,-8.203777],[0.847803,-8.409057,-5.720876,-7.274030,-5.679771,3.795850,-0.188495,-4.442755],[0.151333,8.237615,6.152314,9.720985,0.600721,-9.261530,7.372788,-8.664000],[0.793608,7.730570,8.347548,-7.937130,-1.841052,-5.374558,9.513567,4.780313]],[[-0.017457,1.543987,-4.764346,-9.581142,-7.104743,3.095510,3.684291,-8.648704],[-4.390797,-0.881059,5.329919,4.717215,-1.988393,9.644033,-5.974408,3.869128],[2.006869,-7.693725,9.757093,1.479177,4.065595,-8.955324,2.913849,6.516635],[-1.013906,5.399800,-7.384623,9.131371,-7.528065,1.076635,-6.002047,5.840547],[0.004495,8.158224,-2.011757,-4.581192,4.140626,-7.042465,2.853859,-4.028785],[-3.058484,5.138343,-3.095630,7.351076,5.942481,0.919844,0.120558,1.835102],[5.864110,-7.803505,-9.657841,8.910026,8.216487,-1.791461,-5.071116,-2.100702],[-2.032630,0.140080,-7.609451,3.057338,6.770070,0.617199,9.675500,8.019838],[1.966767,6.252146,-6.357018,5.041011,-5.759962,-0.993423,-1.249647,3.385573]],[[9.697654,2.143949,-9.005503,4.734898,-8.047775,-4.212469,-2.927651,-7.966177],[4.036356,2.966445,-9.255614,9.023746,-8.425492,3.890374,-1.290047,8.175788],[-1.905187,-8.565282,7.537206,-5.596601,-6.178317,8.972036,7.704821,9.486656],[8.498725,-0.746845,4.663942,2.528157,-1.372549,0.290645,7.278278,-0.443436],[4.026024,-1.815611,-5.719506,-8.674577,-7.170637,7.553148,5.753649,-3.438305],[4.833028,5.011691,0.984473,-3.514579,5.954524,-8.567133,-9.013582,-8.187096],[9.670692,-9.131730,-9.281994,9.645845,2.141852,-6.191809,8.551621,8.915098],[8.032272,3.649838,2.164863,-4.746642,0.403595,-0.316856,8.962723,-3.350560],[7.353533,6.153181,6.511441,-8.067912,9.751410,-3.308577,-3.145265,-2.489657]],[[-1.544445,-3.482372,3.244598,-7.713984,6.068846,0.772628,-0.447445,-1.500005],[-6.738259,8.058294,-4.192706,-7.920718,-0.434125,-7.683528,8.079798,-8.944013],[-5.949994,7.675789,-0.319441,9.886399,-5.909184,-5.990229,-4.674797,9.462065],[-5.157262,-9.901837,-2.728915,7.126639,4.109798,2.202505,-8.393278,-8.654783],[-8.202113,-7.747230,-3.797080,7.006405,-7.144269,9.164192,-1.171517,-6.286248],[0.582554,0.642984,3.956361,-0.574911,-3.840423,8.182097,9.537114,0.156304],[-0.223087,-2.198584,2.185950,1.887258,-3.287860,-4.266420,6.758799,2.594276],[-7.596834,7.271868,0.969034,-6.076500,4.544680,-2.819722,-3.155969,9.086426],[-1.219456,9.938654,6.004763,4.249786,2.073355,-8.419949,-2.743441,5.666792]]], dtype = "float64")#candidate|9474|(6, 9, 8)|const|float64
bop_9475 = relay.floor_mod(var_9473.astype('float64'), relay.reshape(const_9474.astype('float64'), relay.shape_of(var_9473))) # shape=(6, 9, 8)
output = relay.Tuple([bop_9475,])
output2 = relay.Tuple([bop_9475,])
func_9478 = relay.Function([var_9473,], output)
mod['func_9478'] = func_9478
mod = relay.transform.InferType()(mod)
mutated_mod['func_9478'] = func_9478
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9479 = relay.var("var_9479", dtype = "float64", shape = (6, 9, 8))#candidate|9479|(6, 9, 8)|var|float64
func_9478_call = mutated_mod.get_global_var('func_9478')
call_9480 = func_9478_call(var_9479)
output = call_9480
func_9481 = relay.Function([var_9479], output)
mutated_mod['func_9481'] = func_9481
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9501 = relay.var("var_9501", dtype = "float32", shape = (12, 7, 4))#candidate|9501|(12, 7, 4)|var|float32
uop_9502 = relay.exp(var_9501.astype('float32')) # shape=(12, 7, 4)
output = relay.Tuple([uop_9502,])
output2 = relay.Tuple([uop_9502,])
func_9509 = relay.Function([var_9501,], output)
mod['func_9509'] = func_9509
mod = relay.transform.InferType()(mod)
var_9510 = relay.var("var_9510", dtype = "float32", shape = (12, 7, 4))#candidate|9510|(12, 7, 4)|var|float32
output = func_9509(var_9510)
func_9511 = relay.Function([var_9510], output)
mutated_mod['func_9511'] = func_9511
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9640 = relay.var("var_9640", dtype = "float64", shape = (1, 15, 2))#candidate|9640|(1, 15, 2)|var|float64
uop_9641 = relay.sqrt(var_9640.astype('float64')) # shape=(1, 15, 2)
func_3494_call = mod.get_global_var('func_3494')
func_3497_call = mutated_mod.get_global_var('func_3497')
const_9647 = relay.const([6,1,-8,-6,-10,8,10,-4,2,-2,8,5,-1,1,8,-4,8,10,6,5,-5,-4,9,-1,-2,1,6,5,3,-7,-4,5,-6,-5,3,2,3,2,6,4,8,-5,3,4,-8,5,1,1,7,2,8,-7,-10,4,4,-3,3,-7,-9,-10,-3,6,-7,3,-5,-3,9,-3,-8,-6,-4,5,6,-4,4,-2,1,2,9,5,10,-8,-7,-9,-9,-9,3,-2,7,-8,2,-9,1,4,-5,-3,-6,-4,-3,9,-8,-5,-4,4,5,-4,3,1,-3,4,-3,-4,10,-3,1,-5,2,-3,-10,-8,10,-1,3,5,-10,-7,5,-3,9,8], dtype = "uint64")#candidate|9647|(130,)|const|uint64
var_9648 = relay.var("var_9648", dtype = "uint64", shape = (1300,))#candidate|9648|(1300,)|var|uint64
call_9646 = func_3494_call(relay.reshape(const_9647.astype('uint64'), [10, 13, 1]), relay.reshape(var_9648.astype('uint64'), [10, 13, 10]), )
call_9649 = func_3494_call(relay.reshape(const_9647.astype('uint64'), [10, 13, 1]), relay.reshape(var_9648.astype('uint64'), [10, 13, 10]), )
output = relay.Tuple([uop_9641,call_9646,const_9647,var_9648,])
output2 = relay.Tuple([uop_9641,call_9649,const_9647,var_9648,])
func_9658 = relay.Function([var_9640,var_9648,], output)
mod['func_9658'] = func_9658
mod = relay.transform.InferType()(mod)
mutated_mod['func_9658'] = func_9658
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9658_call = mutated_mod.get_global_var('func_9658')
var_9660 = relay.var("var_9660", dtype = "float64", shape = (1, 15, 2))#candidate|9660|(1, 15, 2)|var|float64
var_9661 = relay.var("var_9661", dtype = "uint64", shape = (1300,))#candidate|9661|(1300,)|var|uint64
call_9659 = func_9658_call(var_9660,var_9661,)
output = call_9659
func_9662 = relay.Function([var_9660,var_9661,], output)
mutated_mod['func_9662'] = func_9662
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10166 = relay.const([[[6,-5,7,1,2,10,6,7,-7,-6,3,3,5,-8],[-1,-8,-8,5,10,7,-2,9,-3,7,7,-10,5,2],[-9,8,-1,-7,1,6,-10,3,-10,-1,-1,2,4,-10],[-9,9,-7,6,-5,-8,-8,8,-9,-1,-3,3,-3,-2],[9,5,6,-6,3,10,-6,4,3,2,-1,1,7,8],[1,6,1,7,-5,10,-4,6,9,4,2,-5,8,8],[2,-5,3,-2,-3,2,6,8,2,-2,3,-6,1,-9],[9,-6,3,-5,-1,3,-10,3,-6,-5,-4,3,2,-4],[3,2,3,7,9,6,-1,-3,-3,6,-7,10,-10,9],[-4,-5,-10,-1,4,1,-9,3,-6,-10,5,10,1,-3],[5,-2,-9,-8,-5,2,-4,-5,3,-3,-6,-8,1,3],[10,-2,2,-5,-3,9,-1,-7,5,-8,-10,7,-3,7],[5,-7,-7,-1,7,9,-9,7,-9,-5,-8,5,3,4]],[[-9,4,-10,-10,-4,-8,-6,-10,-5,-5,3,1,2,-7],[-9,4,1,-3,-1,-2,1,3,-8,2,-1,-8,-6,4],[-6,-4,-4,-3,6,-10,7,1,1,-7,8,2,8,-2],[10,4,-10,1,9,-3,-9,4,-4,-6,-9,-3,6,-6],[7,9,-7,7,3,3,3,-9,-6,10,7,4,3,-5],[-5,1,1,3,-5,7,-8,10,-6,-6,1,2,-4,-8],[-6,-3,-3,4,6,-4,-8,9,-1,7,-9,10,1,-9],[-10,1,9,-8,-10,-8,2,7,3,5,-6,-1,-7,4],[3,-2,-10,1,-7,-2,5,-5,-4,-6,10,-10,4,-1],[10,-1,-9,-10,-6,-8,1,-1,-2,3,1,-2,1,-7],[-3,7,4,-10,1,-3,10,1,3,-10,-8,-2,4,-10],[-8,-9,-7,-8,-4,-3,-8,-1,8,-10,4,8,4,-5],[-6,3,-3,-6,-1,-9,-1,-2,-9,-7,-7,-9,-8,-6]],[[-9,-3,5,-8,10,-9,6,-10,2,-8,-8,-9,-4,7],[7,6,-6,10,7,-2,-2,10,10,-7,-3,-5,-1,-6],[-5,9,-10,-8,8,-10,6,3,-4,5,4,-6,8,8],[8,-6,-8,-6,2,7,-10,4,-8,3,10,5,2,1],[-7,-3,4,9,-4,2,-7,-7,-3,-4,-6,4,6,1],[5,10,-2,6,-2,-8,9,4,7,4,2,3,-4,-5],[-8,-10,10,-2,3,-6,2,3,2,-7,1,-10,-9,3],[10,6,6,-1,-6,-7,-1,-3,-7,-4,6,-9,-5,9],[4,7,-10,1,1,-10,-5,5,10,-10,-6,5,8,-8],[4,6,7,-1,-8,-3,-6,-5,10,8,-2,4,-5,-2],[6,5,-7,-8,-4,-1,5,3,-7,-4,-2,6,3,2],[2,2,-3,-7,-7,7,4,-8,-4,-2,-3,7,-1,9],[-4,3,-6,3,3,10,-3,-3,-4,7,4,-10,-8,-10]],[[1,-4,-2,-10,-3,8,3,5,-6,4,-9,-10,2,10],[7,10,1,5,-2,-2,10,-2,9,-8,8,-6,4,-2],[6,-6,-1,-2,-10,-6,2,9,7,4,1,-10,3,-5],[-4,3,8,4,6,2,3,-8,5,8,1,7,-3,10],[-4,2,2,7,-5,-7,-7,6,-6,-8,4,-2,-7,6],[7,7,-10,9,-4,-10,-7,9,10,7,-2,9,-10,-2],[2,-8,-3,-10,4,5,-6,-9,5,-9,5,-1,1,-4],[10,8,1,1,-1,-7,2,4,-8,-3,3,6,-9,5],[-4,1,-3,6,-6,-10,-9,3,10,1,2,-10,9,-1],[2,8,-4,-2,7,1,-6,-10,9,-8,1,-6,5,-8],[-4,3,-4,4,8,-5,5,-8,-10,-5,2,-7,-5,5],[-10,6,-3,-10,10,5,1,4,-9,-6,-1,-5,6,-5],[6,1,-5,8,6,5,3,5,-1,9,-3,6,-7,6]],[[-4,2,-3,5,-10,5,2,-1,1,8,-6,1,-3,-5],[9,-2,2,-4,7,-2,6,-2,-7,-5,8,10,2,5],[-10,4,2,6,-9,7,-2,2,6,6,6,6,7,-10],[-9,4,7,-1,-5,-1,9,-2,-8,-9,-8,-2,8,-10],[3,-4,7,2,-6,-1,1,-7,1,-9,4,3,-5,-8],[-10,10,10,-4,1,-9,10,-10,-3,9,-6,10,8,-6],[8,-8,4,-2,1,9,1,-1,-9,1,-9,5,1,-7],[-1,-6,9,-7,-3,5,-4,-5,4,7,-8,7,-9,5],[2,-10,7,1,-1,8,7,7,-8,8,10,-7,-4,-8],[-9,-4,6,-3,10,-10,-4,5,2,5,-4,-3,-10,5],[-7,6,7,-8,-6,10,8,-8,-8,6,-5,-3,-7,5],[9,9,4,-5,-7,-6,7,-8,-7,7,-9,7,-7,-3],[7,10,-10,3,8,5,-2,-10,-8,-3,-5,2,5,-10]],[[-10,-7,-2,6,-9,6,-8,3,-1,-8,-1,5,1,-4],[7,-9,8,7,-4,-2,1,-8,-8,-8,6,-9,6,5],[-3,4,-2,6,-10,1,-5,4,-10,4,5,-8,-9,8],[-5,5,-3,-6,5,-6,-7,6,10,6,4,10,4,-10],[7,2,-2,-7,-9,9,-7,6,2,3,-4,1,-1,-7],[1,1,5,9,10,10,3,3,4,3,1,-7,-9,3],[1,6,-7,-1,10,-8,10,-2,-7,2,-2,7,-4,-10],[-5,2,5,8,-7,-2,3,-9,-10,-5,-4,10,3,-3],[4,-2,8,-4,4,-5,-3,9,-1,-8,-7,-7,9,1],[9,-10,9,9,-6,2,-7,2,-8,-5,-9,-7,5,1],[5,7,-6,-4,-1,-4,-8,-10,5,-4,-4,1,3,10],[-6,-3,3,-3,-10,-5,4,9,-6,-8,10,-6,-2,-8],[7,-6,-10,-1,10,3,-5,-1,8,2,7,-8,1,-1]]], dtype = "uint16")#candidate|10166|(6, 13, 14)|const|uint16
var_10167 = relay.var("var_10167", dtype = "uint16", shape = (6, 13, 14))#candidate|10167|(6, 13, 14)|var|uint16
bop_10168 = relay.left_shift(const_10166.astype('uint16'), relay.reshape(var_10167.astype('uint16'), relay.shape_of(const_10166))) # shape=(6, 13, 14)
output = relay.Tuple([bop_10168,])
output2 = relay.Tuple([bop_10168,])
func_10179 = relay.Function([var_10167,], output)
mod['func_10179'] = func_10179
mod = relay.transform.InferType()(mod)
mutated_mod['func_10179'] = func_10179
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10180 = relay.var("var_10180", dtype = "uint16", shape = (6, 13, 14))#candidate|10180|(6, 13, 14)|var|uint16
func_10179_call = mutated_mod.get_global_var('func_10179')
call_10181 = func_10179_call(var_10180)
output = call_10181
func_10182 = relay.Function([var_10180], output)
mutated_mod['func_10182'] = func_10182
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10323 = relay.var("var_10323", dtype = "uint64", shape = (14, 10, 1))#candidate|10323|(14, 10, 1)|var|uint64
var_10324 = relay.var("var_10324", dtype = "uint64", shape = (14, 10, 12))#candidate|10324|(14, 10, 12)|var|uint64
bop_10325 = relay.minimum(var_10323.astype('uint64'), var_10324.astype('uint64')) # shape=(14, 10, 12)
output = bop_10325
output2 = bop_10325
func_10329 = relay.Function([var_10323,var_10324,], output)
mod['func_10329'] = func_10329
mod = relay.transform.InferType()(mod)
mutated_mod['func_10329'] = func_10329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10329_call = mutated_mod.get_global_var('func_10329')
var_10331 = relay.var("var_10331", dtype = "uint64", shape = (14, 10, 1))#candidate|10331|(14, 10, 1)|var|uint64
var_10332 = relay.var("var_10332", dtype = "uint64", shape = (14, 10, 12))#candidate|10332|(14, 10, 12)|var|uint64
call_10330 = func_10329_call(var_10331,var_10332,)
output = call_10330
func_10333 = relay.Function([var_10331,var_10332,], output)
mutated_mod['func_10333'] = func_10333
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10485 = relay.var("var_10485", dtype = "float64", shape = (2, 16, 16))#candidate|10485|(2, 16, 16)|var|float64
uop_10486 = relay.acosh(var_10485.astype('float64')) # shape=(2, 16, 16)
output = uop_10486
output2 = uop_10486
func_10501 = relay.Function([var_10485,], output)
mod['func_10501'] = func_10501
mod = relay.transform.InferType()(mod)
var_10502 = relay.var("var_10502", dtype = "float64", shape = (2, 16, 16))#candidate|10502|(2, 16, 16)|var|float64
output = func_10501(var_10502)
func_10503 = relay.Function([var_10502], output)
mutated_mod['func_10503'] = func_10503
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10702 = relay.var("var_10702", dtype = "bool", shape = (8, 9, 7))#candidate|10702|(8, 9, 7)|var|bool
var_10703 = relay.var("var_10703", dtype = "bool", shape = (8, 9, 7))#candidate|10703|(8, 9, 7)|var|bool
bop_10704 = relay.logical_and(var_10702.astype('bool'), relay.reshape(var_10703.astype('bool'), relay.shape_of(var_10702))) # shape=(8, 9, 7)
output = relay.Tuple([bop_10704,])
output2 = relay.Tuple([bop_10704,])
func_10716 = relay.Function([var_10702,var_10703,], output)
mod['func_10716'] = func_10716
mod = relay.transform.InferType()(mod)
mutated_mod['func_10716'] = func_10716
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10716_call = mutated_mod.get_global_var('func_10716')
var_10718 = relay.var("var_10718", dtype = "bool", shape = (8, 9, 7))#candidate|10718|(8, 9, 7)|var|bool
var_10719 = relay.var("var_10719", dtype = "bool", shape = (8, 9, 7))#candidate|10719|(8, 9, 7)|var|bool
call_10717 = func_10716_call(var_10718,var_10719,)
output = call_10717
func_10720 = relay.Function([var_10718,var_10719,], output)
mutated_mod['func_10720'] = func_10720
mutated_mod = relay.transform.InferType()(mutated_mod)
const_11090 = relay.const([[[-1.090864,2.573874,-6.606448,5.617128,-6.901250,-2.204196,8.605194,0.810156,-7.370350,-7.677295,7.170333,-4.978387,-2.652931,1.463032],[7.681512,-8.250801,2.761740,-4.432047,-4.483338,4.966984,-9.095876,-4.787756,5.648204,2.696317,5.525947,-3.736756,-7.334424,8.270657],[-4.172455,3.414361,-1.489882,9.041792,5.514927,3.407230,-6.109310,3.359561,7.002044,-3.690416,5.882527,-6.575391,7.103250,9.089281],[0.660576,-5.989392,-7.327079,8.187431,7.071624,-4.594222,-7.632468,-8.390963,-9.056474,2.439594,-1.416328,-4.474783,-2.327636,-9.313535],[9.846589,4.140707,8.651916,-1.171927,-0.295323,-0.498720,9.205492,-1.381409,-0.730315,-6.863717,-1.953224,-9.691927,7.605656,1.551767]],[[6.449593,2.125277,5.532422,2.275368,-9.150531,-9.858784,4.915318,-2.702809,-0.072923,2.597305,2.663419,5.326291,7.751714,-9.886052],[1.147695,-2.933706,-9.590379,8.211662,9.298526,-0.994294,9.855041,-6.730571,5.437646,5.063839,3.479043,-7.940568,-5.952117,0.174518],[-8.849426,-3.189340,5.283235,-7.113513,-6.622311,7.755404,0.972523,0.798469,8.730082,8.860066,-2.082475,-0.160259,4.307205,-7.666451],[-6.468789,-5.889218,-0.263579,-6.892804,2.337713,8.113777,5.205332,3.283124,-0.253987,2.400745,-7.648311,-4.688722,2.227490,8.280755],[1.262587,-8.526537,2.222237,-0.227068,6.021723,7.634272,-4.604752,-0.392511,8.316405,-7.153182,-0.303185,5.959581,-2.342885,9.072053]],[[-1.087941,3.580161,-5.594666,-6.868932,-3.339295,0.551683,9.116702,-0.586558,6.250005,6.266191,0.933072,-0.954682,0.838937,-1.428121],[3.986727,6.320526,-5.012981,-6.982321,-3.240591,-8.075080,3.507302,-0.066618,-6.795151,-0.182088,5.227843,4.906239,9.119731,-7.950991],[0.187721,3.958018,-0.913730,2.832043,2.489137,-4.720212,-2.853533,-5.227010,-7.074367,-4.226276,7.357567,6.449593,5.451100,9.780660],[-0.654987,8.737045,6.547237,0.516140,-7.116817,-4.338191,-4.455491,8.927565,-3.555930,-0.147294,6.575965,6.131522,-7.178734,2.735265],[9.056860,-3.885959,4.419457,-1.725763,-2.737042,-6.880791,-3.407517,-8.427641,2.761502,2.966348,3.689286,2.062098,-6.446252,-3.867786]],[[6.517312,-7.615204,-9.934781,-1.524423,6.716571,-6.340034,-3.289688,-9.731847,-5.834919,4.972623,-8.784239,8.890885,8.801397,-9.854185],[7.295831,-7.270773,6.163312,-0.100692,9.017765,4.899501,1.250477,7.604618,-8.536926,-0.769864,-5.661222,2.416304,-3.472027,9.339740],[1.254113,8.821986,-1.110312,5.455230,6.257932,6.968134,-5.792351,3.068514,6.655420,-7.430155,-5.514162,-5.146018,-8.131506,0.077573],[-4.736804,-6.677866,8.604516,-0.599575,4.107389,4.188189,0.127440,-0.358181,9.883422,1.927552,-9.970059,-0.832276,-6.039312,4.858222],[-9.009749,9.414300,3.340391,-0.739328,-5.801702,-9.954210,-3.790776,-3.095939,9.256775,-7.744530,-5.773072,7.559287,8.689536,4.611487]],[[-1.233793,-5.690703,4.444312,5.030193,-1.791694,2.190265,-5.898707,-0.002007,3.045547,2.521472,3.653299,1.851706,9.780962,-9.672582],[4.745130,6.817512,1.679510,-5.653354,8.886364,7.855901,-0.927424,-0.373241,4.658593,2.707539,8.693681,5.776878,-5.920376,-1.177520],[5.226047,-8.869465,-7.937608,-4.298696,-9.435560,2.297947,-3.531782,9.229397,0.227342,6.072796,-3.017042,-6.796836,4.967100,3.912262],[-2.060911,-3.000233,-8.145855,-5.456805,-7.576383,-6.446527,-1.322020,-8.068467,7.905045,8.718669,-3.586335,7.849202,3.385264,-9.267445],[4.170469,8.908223,-8.400649,7.051943,-5.003879,5.467352,-1.698527,9.916598,9.864813,9.817374,3.840963,-6.933324,6.763199,1.145172]],[[6.774558,-8.133434,6.741783,-4.254185,1.135726,-1.443713,-3.469611,-0.987675,-2.308499,7.606455,7.613465,-7.821872,4.023686,-7.930508],[-1.158483,0.224311,-5.005272,-0.604174,3.627550,6.894657,-3.567370,9.843880,0.848120,8.485256,8.566602,-7.927765,2.931790,-9.382102],[1.076281,8.859414,-5.493766,5.003374,-8.579838,-5.975439,-5.380702,-6.853967,9.724492,5.261229,2.170823,-3.273574,3.020233,-1.603180],[4.790083,0.504220,6.336505,-7.925116,-6.519956,-6.907480,2.568817,-7.329065,-9.370783,-4.492956,-9.570845,4.663605,-3.249406,5.783097],[-4.282910,-9.827757,-6.074009,-7.290815,9.381034,9.715786,-1.737414,-4.302064,-2.144191,2.273859,-2.452924,-5.263470,-8.982332,-8.713846]],[[-6.333898,-4.195686,4.106688,-1.871283,1.326258,-9.177305,-7.193328,-5.237258,0.502467,-0.373444,9.815446,7.765052,-7.710132,3.068408],[9.799001,7.729884,4.197845,-8.166425,5.102955,-4.391036,5.691127,6.711822,-5.257646,-8.868160,-8.759365,2.083866,-4.916162,4.400580],[-5.510238,6.705137,9.074217,2.455273,0.003943,8.103514,0.539118,7.660953,-2.857367,-0.845463,-4.058909,0.436149,7.607542,-2.054804],[6.284662,-6.705566,-3.916204,7.059753,2.202115,-0.855465,-2.569084,7.380512,8.496411,-1.508651,6.959583,-6.633165,4.733413,-7.318483],[-9.373432,-9.713488,2.312612,-9.740805,7.365357,4.742917,-6.129296,6.792941,0.156436,-1.375605,9.800726,0.061483,9.859535,-7.229180]],[[2.434044,-4.401916,9.792054,5.018948,5.285381,0.856401,2.916151,0.171566,-8.595501,-9.927552,3.409779,9.530692,2.309899,8.735937],[-3.921580,0.074809,8.483233,-5.343052,-4.744028,1.339048,3.422770,-9.476662,1.825820,-1.205469,-1.981186,4.424954,-7.792708,-6.592754],[6.020016,-4.448774,4.904718,8.054350,5.806228,-4.090192,3.438379,-3.065265,-3.572977,3.775671,-3.582783,4.293423,-8.507991,2.191591],[8.475767,-7.851720,9.643045,1.583469,-9.696753,8.235430,-2.099137,-9.648627,9.869450,-2.619066,9.214088,6.157680,1.145013,5.778208],[-0.128325,-1.216444,-3.243652,-7.256112,-0.329826,1.820716,9.769695,-5.273898,-4.469727,2.024381,8.170110,3.072018,-8.062833,3.526736]],[[3.682497,3.951576,5.936093,-2.437470,1.679191,1.812616,-0.079408,-6.851684,-5.001357,5.180926,3.976917,-0.442082,-2.465539,-7.736291],[1.062696,-0.304963,-3.969807,-8.155625,-2.980188,7.574611,1.618432,0.988326,7.535453,8.959576,-8.880504,-7.806287,-4.448898,7.336215],[-8.546168,1.307430,9.198044,2.425525,4.659843,5.098902,-3.849365,5.931589,0.618082,6.109665,1.183433,-5.512259,4.112424,0.231742],[-4.423741,-4.625387,-5.343030,-7.966406,2.693028,5.663924,3.277933,-7.294706,-8.496729,7.183949,-9.361392,-2.732706,-7.512325,-6.158142],[-0.426691,3.941783,-9.855871,3.781722,2.938995,-7.928327,7.583739,6.339046,-0.199740,-0.885027,-7.521063,-6.113505,-4.081975,-6.474151]]], dtype = "float32")#candidate|11090|(9, 5, 14)|const|float32
uop_11091 = relay.sin(const_11090.astype('float32')) # shape=(9, 5, 14)
output = uop_11091
output2 = uop_11091
func_11095 = relay.Function([], output)
mod['func_11095'] = func_11095
mod = relay.transform.InferType()(mod)
output = func_11095()
func_11096 = relay.Function([], output)
mutated_mod['func_11096'] = func_11096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11095_call = mod.get_global_var('func_11095')
func_11096_call = mutated_mod.get_global_var('func_11096')
call_11115 = func_11095_call()
call_11116 = func_11095_call()
func_7918_call = mod.get_global_var('func_7918')
func_7922_call = mutated_mod.get_global_var('func_7922')
const_11139 = relay.const([7.967965,-8.509901,-2.450539,6.438587,6.393619,5.219156,-5.301899,-6.433484,-1.207832,6.868648,4.025422,-8.182266,-2.479174,-4.109691,-3.719339,-6.763259,7.611458,-8.288151,5.333632,7.428981,-6.443855,0.404913,-2.103133,4.047615,-6.469967,-0.242434,-5.021401,-3.293936,8.410233,-0.251254,-5.759148,-5.792935,-2.007431,-2.996500,-9.856594,-5.198281,-7.679122,1.868828,5.543457,7.407406,7.601759,-5.370891,-3.124366,-9.173970,6.866690,-8.618742,3.491235,7.063468,6.584553,0.645353,4.250413,-4.855782,7.494787,0.558912,8.197607,-1.832928,-6.072042,-1.809343,7.520896,-2.268848,7.241379,4.101421,9.528053,-6.466718,-4.511687,-4.282331,-9.457223,6.270472,-3.825816,-0.014268,7.164665,-1.565348,1.379080,-1.723604,-5.464339,0.910653,3.222200,-7.749094,-8.598746,-1.866695,1.125602,-0.180279,7.651842,2.336026,-1.032796,8.682984,5.078558,0.499890,-1.389242,3.134369,3.180843,3.585607,5.212623,5.226950,-4.004341,-5.958551,9.688555,7.931687,-9.228469,-9.199225,2.464436,-2.144977,-3.686156,7.965446,-2.261578,7.724857,-5.274371,-0.469709,-2.469780,0.758737,7.795659,-2.313903,-4.654268,-9.668352,4.659564,-6.550933,-8.533560,0.496985,-5.558277,-0.829478,8.853097,-3.188658,-5.781370,-2.089504,9.567507,1.058736,4.144907,6.171547,-7.129865,3.312129,-9.224538,-6.648221,-3.287032,4.193542,-3.416766,4.615765,6.119747,6.295003,9.078137,1.710980,2.181160,2.801075,-2.645937,7.992282,-5.784440,-3.125692,-8.441142,-4.507890,-6.530599,8.561356,7.855712,1.561268,1.056858,-8.084332,-5.569429,7.505120,-5.788213,-1.787490,4.555079,8.350335,-3.877605,-3.922090,-8.845245,-8.386605,3.479134,-1.195838,-5.141200,7.554227,-9.332971,-8.333823,7.740863,6.777432,8.925808,0.116737,5.037987,-3.466164,-2.584735,-7.012236,2.975760,-1.923528,-1.119269,1.143055,-6.801484,-8.014145,-4.396487,0.788039,-1.493532,-3.699299,-2.820062,-5.237755,-4.194265,-5.916145,-6.691453,-7.247395,8.325503,-7.410547,4.717515,-8.666380,-9.798402,-5.140122,-9.628891,4.426303,-9.637132,-3.254903,9.317745,-1.605604,0.209744,-3.682551,0.706848,-2.090276,2.016669,8.947167,-2.759207,-0.663775,-2.984208,-9.410575,-4.209116,-4.761351,5.385020,-4.564001,9.691990,-6.072088,8.479972,-8.261395,2.273924,9.695537,3.348244,0.104709,-7.165866,6.692197,4.788629,5.603364,7.023735,-5.629815,-2.988081,1.735339,-3.733196,1.418204,-6.530628,-8.408789,-8.704352,5.842611,-9.207278,0.397237,-8.683361,-4.721714,-1.291014,-7.350968,7.259099,-1.916188,8.053704,0.740142,-7.635665,6.846087,7.991895,-9.374492,8.937121,3.473024,5.153059,-6.606587,4.923661,3.320277,5.373322,5.605223,-8.140462,-5.376067,0.688992,1.504534,-0.283951,4.242271,6.801526,0.618576,2.849948,-1.726717,-7.308701,-5.985297,8.691532,2.345840,7.292024,8.324715,5.146563,1.123755,-0.960752,-9.788051,5.024383,-5.419585,0.317705,0.575226,-0.544711,1.973247,9.314883,2.861159,1.638748,2.999614,9.226054,4.315491,-5.649045,-0.054502,2.508706,-6.412283,-3.894043,6.710141,-6.009527,-8.967154,1.773791,6.774116,7.490609,3.706562,-0.377670,-5.557861,-2.369577,-7.696111,-6.429183,5.863281,7.799936,4.369311,-5.334443,0.975804,3.016792,2.496901,-3.974747,2.936630,3.533808,-8.985615,6.261401,-8.127577,-6.253739,9.988642,5.163518,1.015908,-0.467042,-2.073352,5.126714,9.853295,0.301328,4.418855,-9.468229,3.367511,-9.180605,1.106074,-8.841232,3.209364,-2.257100,-0.763644,7.548489,-1.749282,-5.082302,-8.089487,-7.210690,-3.896207,-9.520640,9.682419,4.459440,2.365172,2.736128,7.692412,-5.803073,-7.001845,9.153841,-8.565861], dtype = "float32")#candidate|11139|(360,)|const|float32
call_11138 = relay.TupleGetItem(func_7918_call(relay.reshape(const_11139.astype('float32'), [12, 2, 15]), relay.reshape(const_11139.astype('float32'), [12, 2, 15]), ), 0)
call_11140 = relay.TupleGetItem(func_7922_call(relay.reshape(const_11139.astype('float32'), [12, 2, 15]), relay.reshape(const_11139.astype('float32'), [12, 2, 15]), ), 0)
func_7397_call = mod.get_global_var('func_7397')
func_7401_call = mutated_mod.get_global_var('func_7401')
const_11142 = relay.const(3, dtype = "uint8")#candidate|11142|()|const|uint8
var_11143 = relay.var("var_11143", dtype = "float64", shape = (832,))#candidate|11143|(832,)|var|float64
call_11141 = relay.TupleGetItem(func_7397_call(relay.reshape(const_11142.astype('uint8'), []), relay.reshape(var_11143.astype('float64'), [832,]), ), 4)
call_11144 = relay.TupleGetItem(func_7401_call(relay.reshape(const_11142.astype('uint8'), []), relay.reshape(var_11143.astype('float64'), [832,]), ), 4)
output = relay.Tuple([call_11115,call_11138,const_11139,call_11141,const_11142,var_11143,])
output2 = relay.Tuple([call_11116,call_11140,const_11139,call_11144,const_11142,var_11143,])
func_11147 = relay.Function([var_11143,], output)
mod['func_11147'] = func_11147
mod = relay.transform.InferType()(mod)
var_11148 = relay.var("var_11148", dtype = "float64", shape = (832,))#candidate|11148|(832,)|var|float64
output = func_11147(var_11148)
func_11149 = relay.Function([var_11148], output)
mutated_mod['func_11149'] = func_11149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11095_call = mod.get_global_var('func_11095')
func_11096_call = mutated_mod.get_global_var('func_11096')
call_11202 = func_11095_call()
call_11203 = func_11095_call()
var_11211 = relay.var("var_11211", dtype = "float32", shape = (9, 5, 14))#candidate|11211|(9, 5, 14)|var|float32
bop_11212 = relay.mod(call_11202.astype('float64'), relay.reshape(var_11211.astype('float64'), relay.shape_of(call_11202))) # shape=(9, 5, 14)
bop_11215 = relay.mod(call_11203.astype('float64'), relay.reshape(var_11211.astype('float64'), relay.shape_of(call_11203))) # shape=(9, 5, 14)
output = relay.Tuple([bop_11212,])
output2 = relay.Tuple([bop_11215,])
func_11220 = relay.Function([var_11211,], output)
mod['func_11220'] = func_11220
mod = relay.transform.InferType()(mod)
mutated_mod['func_11220'] = func_11220
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11221 = relay.var("var_11221", dtype = "float32", shape = (9, 5, 14))#candidate|11221|(9, 5, 14)|var|float32
func_11220_call = mutated_mod.get_global_var('func_11220')
call_11222 = func_11220_call(var_11221)
output = call_11222
func_11223 = relay.Function([var_11221], output)
mutated_mod['func_11223'] = func_11223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11095_call = mod.get_global_var('func_11095')
func_11096_call = mutated_mod.get_global_var('func_11096')
call_11236 = func_11095_call()
call_11237 = func_11095_call()
uop_11238 = relay.log2(call_11236.astype('float32')) # shape=(9, 5, 14)
uop_11240 = relay.log2(call_11237.astype('float32')) # shape=(9, 5, 14)
func_9509_call = mod.get_global_var('func_9509')
func_9511_call = mutated_mod.get_global_var('func_9511')
var_11244 = relay.var("var_11244", dtype = "float32", shape = (336,))#candidate|11244|(336,)|var|float32
call_11243 = relay.TupleGetItem(func_9509_call(relay.reshape(var_11244.astype('float32'), [12, 7, 4])), 0)
call_11245 = relay.TupleGetItem(func_9511_call(relay.reshape(var_11244.astype('float32'), [12, 7, 4])), 0)
output = relay.Tuple([uop_11238,call_11243,var_11244,])
output2 = relay.Tuple([uop_11240,call_11245,var_11244,])
func_11267 = relay.Function([var_11244,], output)
mod['func_11267'] = func_11267
mod = relay.transform.InferType()(mod)
mutated_mod['func_11267'] = func_11267
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11268 = relay.var("var_11268", dtype = "float32", shape = (336,))#candidate|11268|(336,)|var|float32
func_11267_call = mutated_mod.get_global_var('func_11267')
call_11269 = func_11267_call(var_11268)
output = call_11269
func_11270 = relay.Function([var_11268], output)
mutated_mod['func_11270'] = func_11270
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11095_call = mod.get_global_var('func_11095')
func_11096_call = mutated_mod.get_global_var('func_11096')
call_11280 = func_11095_call()
call_11281 = func_11095_call()
output = relay.Tuple([call_11280,])
output2 = relay.Tuple([call_11281,])
func_11288 = relay.Function([], output)
mod['func_11288'] = func_11288
mod = relay.transform.InferType()(mod)
mutated_mod['func_11288'] = func_11288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11288_call = mutated_mod.get_global_var('func_11288')
call_11289 = func_11288_call()
output = call_11289
func_11290 = relay.Function([], output)
mutated_mod['func_11290'] = func_11290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11095_call = mod.get_global_var('func_11095')
func_11096_call = mutated_mod.get_global_var('func_11096')
call_11298 = func_11095_call()
call_11299 = func_11095_call()
output = call_11298
output2 = call_11299
func_11305 = relay.Function([], output)
mod['func_11305'] = func_11305
mod = relay.transform.InferType()(mod)
mutated_mod['func_11305'] = func_11305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11305_call = mutated_mod.get_global_var('func_11305')
call_11306 = func_11305_call()
output = call_11306
func_11307 = relay.Function([], output)
mutated_mod['func_11307'] = func_11307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11095_call = mod.get_global_var('func_11095')
func_11096_call = mutated_mod.get_global_var('func_11096')
call_11327 = func_11095_call()
call_11328 = func_11095_call()
func_2225_call = mod.get_global_var('func_2225')
func_2228_call = mutated_mod.get_global_var('func_2228')
var_11338 = relay.var("var_11338", dtype = "uint32", shape = ())#candidate|11338|()|var|uint32
const_11339 = relay.const([5,-4,-7,7,1,-3,-10,-5,-3,2,-4,3,3,8,-4,-1,-2,-9,5,-8,-8,5,-1,-10], dtype = "uint32")#candidate|11339|(24,)|const|uint32
call_11337 = func_2225_call(relay.reshape(var_11338.astype('uint32'), []), relay.reshape(const_11339.astype('uint32'), [12, 1, 2]), )
call_11340 = func_2225_call(relay.reshape(var_11338.astype('uint32'), []), relay.reshape(const_11339.astype('uint32'), [12, 1, 2]), )
func_5306_call = mod.get_global_var('func_5306')
func_5309_call = mutated_mod.get_global_var('func_5309')
var_11342 = relay.var("var_11342", dtype = "uint64", shape = (130,))#candidate|11342|(130,)|var|uint64
const_11343 = relay.const([6,-8,-8,7,-1,5,-9,-10,-1,10,4,10,4,1,4,1,9,-4,-10,-4,-4,-4,-3,7,-7,-3,7,-5,7,-10,1,8,-1,-8,3,-1,2,9,10,-9,-1,1,8,-8,3,4,1,3,-4,2,4,-2,9,-4,-7,7,7,-7,-4,-10,5,1,7,10,9,-7,-3,9,-2,2,-6,-9,-7,-10,3,9,5,6,6,-3,5,-7,-1,-4,-9,-4,5,8,10,-2,7,1,-3,-3,-4,-5,-8,-9,9,6,10,-3,-3,-9,-8,-6,-4,8,-5,-6,9,7,-4,-8,2,10,-4,-8,-5,-8,10,7,-10,-9,6,-3,7,-2,-6,3,-6,1,8,-5,-8,6,-6,10,-10,10,-6,-2,-2,-5,7,-8,5,-1,1,-5,-10,7,-6,1,-7,1,-5,-10,7,7], dtype = "uint64")#candidate|11343|(160,)|const|uint64
call_11341 = relay.TupleGetItem(func_5306_call(relay.reshape(var_11342.astype('uint64'), [130,]), relay.reshape(const_11343.astype('uint64'), [160,]), ), 5)
call_11344 = relay.TupleGetItem(func_5309_call(relay.reshape(var_11342.astype('uint64'), [130,]), relay.reshape(const_11343.astype('uint64'), [160,]), ), 5)
func_6391_call = mod.get_global_var('func_6391')
func_6393_call = mutated_mod.get_global_var('func_6393')
call_11352 = relay.TupleGetItem(func_6391_call(relay.reshape(var_11338.astype('int16'), [])), 2)
call_11353 = relay.TupleGetItem(func_6393_call(relay.reshape(var_11338.astype('int16'), [])), 2)
output = relay.Tuple([call_11327,call_11337,var_11338,const_11339,call_11341,var_11342,const_11343,call_11352,])
output2 = relay.Tuple([call_11328,call_11340,var_11338,const_11339,call_11344,var_11342,const_11343,call_11353,])
func_11358 = relay.Function([var_11338,var_11342,], output)
mod['func_11358'] = func_11358
mod = relay.transform.InferType()(mod)
mutated_mod['func_11358'] = func_11358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11358_call = mutated_mod.get_global_var('func_11358')
var_11360 = relay.var("var_11360", dtype = "uint32", shape = ())#candidate|11360|()|var|uint32
var_11361 = relay.var("var_11361", dtype = "uint64", shape = (130,))#candidate|11361|(130,)|var|uint64
call_11359 = func_11358_call(var_11360,var_11361,)
output = call_11359
func_11362 = relay.Function([var_11360,var_11361,], output)
mutated_mod['func_11362'] = func_11362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11288_call = mod.get_global_var('func_11288')
func_11290_call = mutated_mod.get_global_var('func_11290')
call_11425 = relay.TupleGetItem(func_11288_call(), 0)
call_11426 = relay.TupleGetItem(func_11290_call(), 0)
func_6665_call = mod.get_global_var('func_6665')
func_6667_call = mutated_mod.get_global_var('func_6667')
var_11433 = relay.var("var_11433", dtype = "float64", shape = (320,))#candidate|11433|(320,)|var|float64
call_11432 = func_6665_call(relay.reshape(var_11433.astype('float64'), [8, 5, 8]))
call_11434 = func_6665_call(relay.reshape(var_11433.astype('float64'), [8, 5, 8]))
output = relay.Tuple([call_11425,call_11432,var_11433,])
output2 = relay.Tuple([call_11426,call_11434,var_11433,])
func_11438 = relay.Function([var_11433,], output)
mod['func_11438'] = func_11438
mod = relay.transform.InferType()(mod)
mutated_mod['func_11438'] = func_11438
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11439 = relay.var("var_11439", dtype = "float64", shape = (320,))#candidate|11439|(320,)|var|float64
func_11438_call = mutated_mod.get_global_var('func_11438')
call_11440 = func_11438_call(var_11439)
output = call_11440
func_11441 = relay.Function([var_11439], output)
mutated_mod['func_11441'] = func_11441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11288_call = mod.get_global_var('func_11288')
func_11290_call = mutated_mod.get_global_var('func_11290')
call_11446 = relay.TupleGetItem(func_11288_call(), 0)
call_11447 = relay.TupleGetItem(func_11290_call(), 0)
output = relay.Tuple([call_11446,])
output2 = relay.Tuple([call_11447,])
func_11459 = relay.Function([], output)
mod['func_11459'] = func_11459
mod = relay.transform.InferType()(mod)
output = func_11459()
func_11460 = relay.Function([], output)
mutated_mod['func_11460'] = func_11460
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11479 = relay.var("var_11479", dtype = "float32", shape = (7, 3, 9))#candidate|11479|(7, 3, 9)|var|float32
uop_11480 = relay.asin(var_11479.astype('float32')) # shape=(7, 3, 9)
func_11438_call = mod.get_global_var('func_11438')
func_11441_call = mutated_mod.get_global_var('func_11441')
var_11490 = relay.var("var_11490", dtype = "float64", shape = (320,))#candidate|11490|(320,)|var|float64
call_11489 = relay.TupleGetItem(func_11438_call(relay.reshape(var_11490.astype('float64'), [320,])), 1)
call_11491 = relay.TupleGetItem(func_11441_call(relay.reshape(var_11490.astype('float64'), [320,])), 1)
output = relay.Tuple([uop_11480,call_11489,var_11490,])
output2 = relay.Tuple([uop_11480,call_11491,var_11490,])
func_11495 = relay.Function([var_11479,var_11490,], output)
mod['func_11495'] = func_11495
mod = relay.transform.InferType()(mod)
mutated_mod['func_11495'] = func_11495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11495_call = mutated_mod.get_global_var('func_11495')
var_11497 = relay.var("var_11497", dtype = "float32", shape = (7, 3, 9))#candidate|11497|(7, 3, 9)|var|float32
var_11498 = relay.var("var_11498", dtype = "float64", shape = (320,))#candidate|11498|(320,)|var|float64
call_11496 = func_11495_call(var_11497,var_11498,)
output = call_11496
func_11499 = relay.Function([var_11497,var_11498,], output)
mutated_mod['func_11499'] = func_11499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11288_call = mod.get_global_var('func_11288')
func_11290_call = mutated_mod.get_global_var('func_11290')
call_11506 = relay.TupleGetItem(func_11288_call(), 0)
call_11507 = relay.TupleGetItem(func_11290_call(), 0)
func_4987_call = mod.get_global_var('func_4987')
func_4992_call = mutated_mod.get_global_var('func_4992')
const_11510 = relay.const(True, dtype = "bool")#candidate|11510|()|const|bool
var_11511 = relay.var("var_11511", dtype = "float64", shape = (480,))#candidate|11511|(480,)|var|float64
var_11512 = relay.var("var_11512", dtype = "float64", shape = (4, 252))#candidate|11512|(4, 252)|var|float64
call_11509 = relay.TupleGetItem(func_4987_call(relay.reshape(const_11510.astype('bool'), []), relay.reshape(var_11511.astype('float64'), [480,]), relay.reshape(var_11512.astype('float64'), [1008,]), ), 3)
call_11513 = relay.TupleGetItem(func_4992_call(relay.reshape(const_11510.astype('bool'), []), relay.reshape(var_11511.astype('float64'), [480,]), relay.reshape(var_11512.astype('float64'), [1008,]), ), 3)
func_5306_call = mod.get_global_var('func_5306')
func_5309_call = mutated_mod.get_global_var('func_5309')
const_11522 = relay.const([-3,3,-5,1,-9,-2,2,-5,-10,-8,-6,4,-10,-7,3,4,-8,-5,10,-7,-7,-9,4,2,7,-2,4,-8,8,-9,-9,8,9,-4,-9,7,9,-7,-10,-9,-10,1,7,-8,-3,6,1,-3,7,-1,-8,4,-4,2,-3,-2,4,-7,-3,7,-4,-1,-9,7,-2,4,-7,-7,3,-5,-4,9,10,-10,3,-2,2,-1,-8,7,-7,9,-3,-4,-8,3,6,2,10,-3,-9,9,8,2,-10,-5,-4,-2,-3,-3,5,-4,10,9,8,-10,-6,-8,-10,-2,1,-9,2,-2,-10,-7,-3,-8,-7,-2,10,1,2,2,-2,-2,2,10,5,-8], dtype = "uint64")#candidate|11522|(130,)|const|uint64
var_11523 = relay.var("var_11523", dtype = "uint64", shape = (160, 1))#candidate|11523|(160, 1)|var|uint64
call_11521 = relay.TupleGetItem(func_5306_call(relay.reshape(const_11522.astype('uint64'), [130,]), relay.reshape(var_11523.astype('uint64'), [160,]), ), 5)
call_11524 = relay.TupleGetItem(func_5309_call(relay.reshape(const_11522.astype('uint64'), [130,]), relay.reshape(var_11523.astype('uint64'), [160,]), ), 5)
output = relay.Tuple([call_11506,call_11509,const_11510,var_11511,var_11512,call_11521,const_11522,var_11523,])
output2 = relay.Tuple([call_11507,call_11513,const_11510,var_11511,var_11512,call_11524,const_11522,var_11523,])
func_11534 = relay.Function([var_11511,var_11512,var_11523,], output)
mod['func_11534'] = func_11534
mod = relay.transform.InferType()(mod)
var_11535 = relay.var("var_11535", dtype = "float64", shape = (480,))#candidate|11535|(480,)|var|float64
var_11536 = relay.var("var_11536", dtype = "float64", shape = (4, 252))#candidate|11536|(4, 252)|var|float64
var_11537 = relay.var("var_11537", dtype = "uint64", shape = (160, 1))#candidate|11537|(160, 1)|var|uint64
output = func_11534(var_11535,var_11536,var_11537,)
func_11538 = relay.Function([var_11535,var_11536,var_11537,], output)
mutated_mod['func_11538'] = func_11538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11095_call = mod.get_global_var('func_11095')
func_11096_call = mutated_mod.get_global_var('func_11096')
call_11563 = func_11095_call()
call_11564 = func_11095_call()
output = relay.Tuple([call_11563,])
output2 = relay.Tuple([call_11564,])
func_11578 = relay.Function([], output)
mod['func_11578'] = func_11578
mod = relay.transform.InferType()(mod)
output = func_11578()
func_11579 = relay.Function([], output)
mutated_mod['func_11579'] = func_11579
mutated_mod = relay.transform.InferType()(mutated_mod)
const_11597 = relay.const([[[True,False,False,False,False,True,False,False],[False,True,True,False,True,False,False,False]],[[True,True,True,False,False,True,False,True],[False,True,False,True,True,False,True,False]],[[False,True,False,False,False,True,True,False],[False,False,False,True,True,False,True,False]]], dtype = "bool")#candidate|11597|(3, 2, 8)|const|bool
var_11598 = relay.var("var_11598", dtype = "bool", shape = (3, 2, 8))#candidate|11598|(3, 2, 8)|var|bool
bop_11599 = relay.logical_or(const_11597.astype('bool'), relay.reshape(var_11598.astype('bool'), relay.shape_of(const_11597))) # shape=(3, 2, 8)
uop_11606 = relay.cosh(bop_11599.astype('float32')) # shape=(3, 2, 8)
uop_11608 = relay.atanh(uop_11606.astype('float32')) # shape=(3, 2, 8)
output = uop_11608
output2 = uop_11608
func_11617 = relay.Function([var_11598,], output)
mod['func_11617'] = func_11617
mod = relay.transform.InferType()(mod)
mutated_mod['func_11617'] = func_11617
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11618 = relay.var("var_11618", dtype = "bool", shape = (3, 2, 8))#candidate|11618|(3, 2, 8)|var|bool
func_11617_call = mutated_mod.get_global_var('func_11617')
call_11619 = func_11617_call(var_11618)
output = call_11619
func_11620 = relay.Function([var_11618], output)
mutated_mod['func_11620'] = func_11620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11459_call = mod.get_global_var('func_11459')
func_11460_call = mutated_mod.get_global_var('func_11460')
call_11631 = relay.TupleGetItem(func_11459_call(), 0)
call_11632 = relay.TupleGetItem(func_11460_call(), 0)
func_11495_call = mod.get_global_var('func_11495')
func_11499_call = mutated_mod.get_global_var('func_11499')
var_11637 = relay.var("var_11637", dtype = "float32", shape = (189,))#candidate|11637|(189,)|var|float32
const_11638 = relay.const([[3.642088],[8.049315],[1.820538],[-7.830614],[0.143893],[4.018711],[4.057635],[-9.585350],[6.930223],[3.445390],[-0.022247],[1.036552],[0.643683],[4.265643],[6.004987],[-3.108129],[-1.166945],[1.241871],[7.781213],[0.001750],[1.073075],[-2.376693],[0.927525],[-2.383452],[-7.936147],[7.089722],[1.329056],[-9.637233],[-9.145415],[0.474057],[-0.755522],[-7.467690],[3.325857],[-7.839773],[-5.828963],[6.094343],[-0.027788],[-9.185137],[6.985822],[-5.188860],[-7.291234],[-3.613125],[1.482734],[-2.458188],[7.564390],[1.615045],[-7.372088],[-9.221361],[-8.208896],[-9.068093],[-4.822223],[-8.254648],[9.846484],[-7.295731],[6.775364],[2.650339],[8.464005],[-7.962789],[-3.014566],[-1.832037],[-3.715053],[3.516726],[0.638064],[-0.275925],[-4.500696],[-4.232934],[8.027871],[-9.453947],[-7.646001],[7.654091],[2.830649],[5.993343],[-8.987886],[8.536759],[4.275565],[-8.433556],[-3.308430],[-5.227847],[3.698476],[0.361214],[3.878473],[6.749925],[-6.937635],[0.242275],[-8.071770],[1.949827],[8.613484],[-0.750560],[-2.675183],[7.184707],[0.028877],[8.912441],[3.587194],[-7.801987],[-7.609852],[1.376216],[1.283699],[-3.081273],[-1.182471],[-8.797635],[-2.281678],[-7.739960],[0.357624],[-5.910265],[9.134344],[0.455881],[7.539126],[-6.637202],[-1.056945],[-9.544264],[-5.244320],[-6.084424],[-6.657435],[4.934124],[-8.945817],[2.099786],[3.510974],[9.984429],[4.471746],[-4.496357],[4.379097],[8.763250],[-7.493726],[4.291334],[-8.375340],[-3.535619],[0.956558],[4.688499],[1.128085],[-6.219433],[-0.978935],[9.060656],[-5.749539],[-2.582417],[-8.621768],[-5.100249],[-4.099015],[-7.163914],[2.083854],[6.552905],[0.918327],[-9.310883],[-5.837358],[-6.305655],[-3.310961],[-2.882754],[6.566262],[7.876146],[-5.527489],[3.493997],[-8.940297],[-6.210380],[9.487895],[-3.092527],[-9.392121],[7.083046],[7.739672],[0.134648],[2.971741],[8.332500],[-8.964345],[-4.941617],[7.271472],[4.438873],[-2.172963],[-4.831054],[-6.583539],[2.551910],[-9.489585],[-0.383335],[-1.776986],[-7.414930],[8.893713],[7.532514],[-1.149761],[0.654319],[-6.932540],[-1.855514],[9.931396],[1.670657],[-5.668712],[-8.901270],[-5.883079],[-8.615609],[3.453477],[-4.137237],[-7.897501],[1.469934],[-4.492702],[-7.402942],[-1.836323],[9.691117],[-7.454849],[-4.715834],[-0.298893],[4.112297],[-1.034806],[1.071197],[3.072480],[9.788587],[1.187402],[-0.551431],[-5.363880],[2.057087],[5.423133],[3.176726],[3.901900],[-2.645033],[-3.301720],[1.584228],[2.108600],[9.612913],[2.303260],[-6.645847],[2.931118],[4.109951],[2.824533],[-9.728825],[-1.453267],[-6.348663],[-0.213481],[5.867248],[6.526175],[8.521683],[-1.568832],[-2.039912],[4.089053],[6.754188],[-2.430208],[8.117120],[2.256324],[-0.394319],[4.758319],[4.543499],[9.889076],[5.856097],[6.685759],[5.543123],[-5.677605],[0.109410],[-6.940861],[-3.063188],[7.726199],[-4.939592],[-4.430486],[7.152804],[-2.392455],[-0.215235],[6.573987],[6.408499],[-6.504724],[-2.925706],[6.141616],[-5.357463],[-4.366772],[5.192000],[9.581058],[-9.890719],[4.974861],[-0.671946],[-1.278733],[-0.889049],[-7.807258],[-8.010171],[-1.222822],[-4.477230],[-1.748827],[-3.466989],[-0.795139],[-0.986015],[-4.168942],[1.775275],[5.452967],[5.066808],[-8.954458],[-8.779553],[8.377249],[-8.627915],[-6.724699],[0.203263],[-5.147733],[5.915290],[-7.780936],[3.377579],[-5.354321],[9.814323],[7.174099],[-2.487885],[-5.414594],[0.219841],[7.986811],[-3.305077],[-0.398105],[-7.020120],[7.595530],[9.852332],[4.804655],[4.273799],[5.605511],[3.249666],[-3.981456],[-8.190438],[9.227988],[-4.724516],[-6.551137],[4.141059],[-1.926267],[7.658589],[-5.715765],[7.924312],[0.733866],[9.032967],[0.143169],[8.615315],[5.615340],[-7.954948],[0.058357],[8.376477],[4.140245],[5.166535]], dtype = "float64")#candidate|11638|(320, 1)|const|float64
call_11636 = relay.TupleGetItem(func_11495_call(relay.reshape(var_11637.astype('float32'), [7, 3, 9]), relay.reshape(const_11638.astype('float64'), [320,]), ), 1)
call_11639 = relay.TupleGetItem(func_11499_call(relay.reshape(var_11637.astype('float32'), [7, 3, 9]), relay.reshape(const_11638.astype('float64'), [320,]), ), 1)
uop_11642 = relay.sinh(var_11637.astype('float64')) # shape=(189,)
func_11147_call = mod.get_global_var('func_11147')
func_11149_call = mutated_mod.get_global_var('func_11149')
var_11650 = relay.var("var_11650", dtype = "float64", shape = (832, 1))#candidate|11650|(832, 1)|var|float64
call_11649 = relay.TupleGetItem(func_11147_call(relay.reshape(var_11650.astype('float64'), [832,])), 2)
call_11651 = relay.TupleGetItem(func_11149_call(relay.reshape(var_11650.astype('float64'), [832,])), 2)
output = relay.Tuple([call_11631,call_11636,const_11638,uop_11642,call_11649,var_11650,])
output2 = relay.Tuple([call_11632,call_11639,const_11638,uop_11642,call_11651,var_11650,])
func_11659 = relay.Function([var_11637,var_11650,], output)
mod['func_11659'] = func_11659
mod = relay.transform.InferType()(mod)
mutated_mod['func_11659'] = func_11659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11659_call = mutated_mod.get_global_var('func_11659')
var_11661 = relay.var("var_11661", dtype = "float32", shape = (189,))#candidate|11661|(189,)|var|float32
var_11662 = relay.var("var_11662", dtype = "float64", shape = (832, 1))#candidate|11662|(832, 1)|var|float64
call_11660 = func_11659_call(var_11661,var_11662,)
output = call_11660
func_11663 = relay.Function([var_11661,var_11662,], output)
mutated_mod['func_11663'] = func_11663
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11459_call = mod.get_global_var('func_11459')
func_11460_call = mutated_mod.get_global_var('func_11460')
call_11737 = relay.TupleGetItem(func_11459_call(), 0)
call_11738 = relay.TupleGetItem(func_11460_call(), 0)
output = call_11737
output2 = call_11738
func_11742 = relay.Function([], output)
mod['func_11742'] = func_11742
mod = relay.transform.InferType()(mod)
mutated_mod['func_11742'] = func_11742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11742_call = mutated_mod.get_global_var('func_11742')
call_11743 = func_11742_call()
output = call_11743
func_11744 = relay.Function([], output)
mutated_mod['func_11744'] = func_11744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11459_call = mod.get_global_var('func_11459')
func_11460_call = mutated_mod.get_global_var('func_11460')
call_11747 = relay.TupleGetItem(func_11459_call(), 0)
call_11748 = relay.TupleGetItem(func_11460_call(), 0)
output = relay.Tuple([call_11747,])
output2 = relay.Tuple([call_11748,])
func_11751 = relay.Function([], output)
mod['func_11751'] = func_11751
mod = relay.transform.InferType()(mod)
mutated_mod['func_11751'] = func_11751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11751_call = mutated_mod.get_global_var('func_11751')
call_11752 = func_11751_call()
output = call_11752
func_11753 = relay.Function([], output)
mutated_mod['func_11753'] = func_11753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11742_call = mod.get_global_var('func_11742')
func_11744_call = mutated_mod.get_global_var('func_11744')
call_11791 = func_11742_call()
call_11792 = func_11742_call()
output = relay.Tuple([call_11791,])
output2 = relay.Tuple([call_11792,])
func_11804 = relay.Function([], output)
mod['func_11804'] = func_11804
mod = relay.transform.InferType()(mod)
mutated_mod['func_11804'] = func_11804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11804_call = mutated_mod.get_global_var('func_11804')
call_11805 = func_11804_call()
output = call_11805
func_11806 = relay.Function([], output)
mutated_mod['func_11806'] = func_11806
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11751_call = mod.get_global_var('func_11751')
func_11753_call = mutated_mod.get_global_var('func_11753')
call_11822 = relay.TupleGetItem(func_11751_call(), 0)
call_11823 = relay.TupleGetItem(func_11753_call(), 0)
output = relay.Tuple([call_11822,])
output2 = relay.Tuple([call_11823,])
func_11833 = relay.Function([], output)
mod['func_11833'] = func_11833
mod = relay.transform.InferType()(mod)
mutated_mod['func_11833'] = func_11833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11833_call = mutated_mod.get_global_var('func_11833')
call_11834 = func_11833_call()
output = call_11834
func_11835 = relay.Function([], output)
mutated_mod['func_11835'] = func_11835
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11095_call = mod.get_global_var('func_11095')
func_11096_call = mutated_mod.get_global_var('func_11096')
call_11934 = func_11095_call()
call_11935 = func_11095_call()
func_9509_call = mod.get_global_var('func_9509')
func_9511_call = mutated_mod.get_global_var('func_9511')
var_11953 = relay.var("var_11953", dtype = "float32", shape = (336,))#candidate|11953|(336,)|var|float32
call_11952 = relay.TupleGetItem(func_9509_call(relay.reshape(var_11953.astype('float32'), [12, 7, 4])), 0)
call_11954 = relay.TupleGetItem(func_9511_call(relay.reshape(var_11953.astype('float32'), [12, 7, 4])), 0)
func_4987_call = mod.get_global_var('func_4987')
func_4992_call = mutated_mod.get_global_var('func_4992')
const_11960 = relay.const(True, dtype = "bool")#candidate|11960|()|const|bool
var_11961 = relay.var("var_11961", dtype = "float64", shape = (480,))#candidate|11961|(480,)|var|float64
var_11962 = relay.var("var_11962", dtype = "float64", shape = (1008,))#candidate|11962|(1008,)|var|float64
call_11959 = relay.TupleGetItem(func_4987_call(relay.reshape(const_11960.astype('bool'), []), relay.reshape(var_11961.astype('float64'), [480,]), relay.reshape(var_11962.astype('float64'), [1008,]), ), 1)
call_11963 = relay.TupleGetItem(func_4992_call(relay.reshape(const_11960.astype('bool'), []), relay.reshape(var_11961.astype('float64'), [480,]), relay.reshape(var_11962.astype('float64'), [1008,]), ), 1)
output = relay.Tuple([call_11934,call_11952,var_11953,call_11959,const_11960,var_11961,var_11962,])
output2 = relay.Tuple([call_11935,call_11954,var_11953,call_11963,const_11960,var_11961,var_11962,])
func_11970 = relay.Function([var_11953,var_11961,var_11962,], output)
mod['func_11970'] = func_11970
mod = relay.transform.InferType()(mod)
var_11971 = relay.var("var_11971", dtype = "float32", shape = (336,))#candidate|11971|(336,)|var|float32
var_11972 = relay.var("var_11972", dtype = "float64", shape = (480,))#candidate|11972|(480,)|var|float64
var_11973 = relay.var("var_11973", dtype = "float64", shape = (1008,))#candidate|11973|(1008,)|var|float64
output = func_11970(var_11971,var_11972,var_11973,)
func_11974 = relay.Function([var_11971,var_11972,var_11973,], output)
mutated_mod['func_11974'] = func_11974
mutated_mod = relay.transform.InferType()(mutated_mod)
const_11976 = relay.const([[[-5.680697,-0.940484,-2.741198,-1.854379,-6.812020],[0.571952,8.441172,1.090401,-1.710009,-1.198790],[-1.376057,7.409691,4.315558,2.245731,-2.017799],[3.474489,-8.111526,1.429522,8.197959,-4.120631],[6.613508,5.892153,-2.868901,2.032447,1.698046]],[[9.096601,-6.587874,-3.852612,2.788201,-3.973337],[-2.698454,-8.602080,4.475301,-4.534638,-4.115299],[-5.755361,-2.956983,-9.932278,2.126774,9.478621],[0.025066,-8.313206,0.084555,9.046459,-5.921567],[-9.783403,-5.082967,-6.003717,5.862257,-4.600554]],[[0.146939,4.958367,-5.009132,-6.842165,2.803028],[4.665329,-1.690146,-0.156431,-6.506741,6.112737],[0.918678,7.655455,-4.002182,-6.867236,-6.577606],[3.181856,9.627659,6.691311,2.226872,7.410830],[-0.827647,8.430664,-9.888414,-3.263633,-2.876720]],[[-5.240934,-8.462061,4.691006,3.568490,-4.682056],[-5.424045,4.012300,-9.329750,-6.998213,-6.692259],[4.897695,-2.675045,-1.746014,-4.243275,4.265738],[-8.337709,5.691896,6.748701,8.685364,-7.454169],[9.086339,-6.760296,-3.957780,2.819305,-3.857038]],[[1.614639,-1.130126,-8.764579,-9.235828,-9.566410],[6.499908,7.389694,0.234133,4.761023,6.482888],[-6.222823,3.535243,9.375272,1.792264,-3.608212],[7.200750,0.600720,7.949487,-6.451321,1.971394],[2.214236,9.636356,6.076443,2.856594,2.923069]],[[-7.102183,9.923523,-7.154595,0.795876,-2.306493],[7.350770,4.631518,9.255743,9.840056,3.245487],[-7.247913,3.038475,8.665218,-8.577024,-1.900248],[-3.399769,3.604878,-2.723274,-6.250021,-2.226421],[0.010131,-0.887138,-4.871768,8.568818,3.817355]],[[-2.088969,3.575405,2.147516,-1.126150,5.626720],[-8.279962,1.311525,-7.511742,6.587479,-2.514184],[9.125123,-2.913474,-9.653869,0.404172,-9.454257],[-7.534760,7.809180,-6.188669,5.357723,-4.079598],[3.169226,-9.237438,4.122836,-5.932056,1.590954]],[[-5.705726,-9.544486,0.858775,6.831063,-1.758108],[0.810697,0.610159,-2.886852,-6.936094,-8.384256],[2.915184,3.716939,7.891147,-8.757772,7.512652],[-1.200819,-6.194120,-1.166868,2.121274,-2.798412],[3.153691,6.884903,-8.596067,2.813562,0.999396]],[[-6.645124,3.068980,-7.169323,-6.014375,0.179993],[-4.742231,8.459652,-5.520497,-1.483381,4.178688],[-2.421911,9.267337,5.482739,6.167547,-7.022640],[9.670749,2.303218,-3.424268,8.108177,-4.665784],[-2.689751,-7.720915,9.660933,-7.276642,-2.996603]],[[8.317959,-4.863343,-6.108673,-5.276274,-8.004216],[-0.170977,9.371721,1.881594,7.432333,-2.060518],[9.522865,4.719083,-9.615378,-3.916907,-7.380249],[3.159381,3.484974,-3.483126,0.573948,-5.207485],[1.860445,8.756032,-8.994739,-6.660318,4.573076]],[[-0.989696,-9.754204,-7.880028,-7.695809,3.606105],[-1.016854,-2.901250,-6.409495,6.672253,-9.232296],[-9.995360,6.583814,-1.754379,-2.760077,3.469399],[-7.299924,-8.184464,4.147497,0.652676,6.826995],[5.231954,6.308246,-9.206486,-0.192298,-5.748541]],[[1.588697,8.335648,-8.399030,-9.952890,-2.885976],[2.920628,8.282077,0.939633,-9.162900,9.708389],[8.153546,2.449628,-0.761423,9.076410,-2.542653],[9.866783,-1.740682,-4.806455,1.364057,5.537527],[-2.117556,-7.192530,-0.882913,5.912134,-2.961321]],[[-5.561907,6.433533,3.151018,4.181839,-6.923835],[-6.292204,3.783765,-8.650203,5.262311,6.627183],[-5.114663,8.389565,1.276472,-1.205962,8.304474],[5.158441,4.569843,9.449737,2.978612,9.881757],[-6.587153,3.283515,-2.005723,1.247293,9.544433]],[[-6.200318,4.635565,-7.676929,0.129012,6.644396],[-1.379518,-5.953964,1.059019,-4.672934,7.432914],[-4.175747,5.838687,0.733732,-4.410496,3.753897],[9.423655,4.307983,-9.981759,-7.405031,-8.895671],[-1.622802,-0.246307,-8.337822,-4.112249,-8.844931]],[[-8.348729,-4.167697,2.596954,7.660553,-7.899851],[4.012578,-3.772143,-5.025621,7.206388,-5.276910],[-8.305045,-0.716752,-6.721660,-6.546406,0.727387],[-2.943649,-0.881924,1.514284,-5.961072,9.043188],[8.281702,1.095796,9.646119,-6.204147,-3.844487]]], dtype = "float64")#candidate|11976|(15, 5, 5)|const|float64
uop_11977 = relay.sigmoid(const_11976.astype('float64')) # shape=(15, 5, 5)
output = uop_11977
output2 = uop_11977
func_11979 = relay.Function([], output)
mod['func_11979'] = func_11979
mod = relay.transform.InferType()(mod)
output = func_11979()
func_11980 = relay.Function([], output)
mutated_mod['func_11980'] = func_11980
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11742_call = mod.get_global_var('func_11742')
func_11744_call = mutated_mod.get_global_var('func_11744')
call_12007 = func_11742_call()
call_12008 = func_11742_call()
uop_12036 = relay.sinh(call_12007.astype('float64')) # shape=(9, 5, 14)
uop_12038 = relay.sinh(call_12008.astype('float64')) # shape=(9, 5, 14)
uop_12051 = relay.erf(uop_12036.astype('float64')) # shape=(9, 5, 14)
uop_12053 = relay.erf(uop_12038.astype('float64')) # shape=(9, 5, 14)
output = relay.Tuple([uop_12051,])
output2 = relay.Tuple([uop_12053,])
func_12065 = relay.Function([], output)
mod['func_12065'] = func_12065
mod = relay.transform.InferType()(mod)
mutated_mod['func_12065'] = func_12065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12065_call = mutated_mod.get_global_var('func_12065')
call_12066 = func_12065_call()
output = call_12066
func_12067 = relay.Function([], output)
mutated_mod['func_12067'] = func_12067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11742_call = mod.get_global_var('func_11742')
func_11744_call = mutated_mod.get_global_var('func_11744')
call_12086 = func_11742_call()
call_12087 = func_11742_call()
func_6391_call = mod.get_global_var('func_6391')
func_6393_call = mutated_mod.get_global_var('func_6393')
var_12091 = relay.var("var_12091", dtype = "int16", shape = ())#candidate|12091|()|var|int16
call_12090 = relay.TupleGetItem(func_6391_call(relay.reshape(var_12091.astype('int16'), [])), 1)
call_12092 = relay.TupleGetItem(func_6393_call(relay.reshape(var_12091.astype('int16'), [])), 1)
func_697_call = mod.get_global_var('func_697')
func_701_call = mutated_mod.get_global_var('func_701')
var_12111 = relay.var("var_12111", dtype = "uint64", shape = (160,))#candidate|12111|(160,)|var|uint64
call_12110 = relay.TupleGetItem(func_697_call(relay.reshape(var_12111.astype('uint64'), [4, 5, 8]), relay.reshape(var_12111.astype('uint64'), [4, 5, 8]), ), 0)
call_12112 = relay.TupleGetItem(func_701_call(relay.reshape(var_12111.astype('uint64'), [4, 5, 8]), relay.reshape(var_12111.astype('uint64'), [4, 5, 8]), ), 0)
output = relay.Tuple([call_12086,call_12090,var_12091,call_12110,var_12111,])
output2 = relay.Tuple([call_12087,call_12092,var_12091,call_12112,var_12111,])
func_12133 = relay.Function([var_12091,var_12111,], output)
mod['func_12133'] = func_12133
mod = relay.transform.InferType()(mod)
mutated_mod['func_12133'] = func_12133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12133_call = mutated_mod.get_global_var('func_12133')
var_12135 = relay.var("var_12135", dtype = "int16", shape = ())#candidate|12135|()|var|int16
var_12136 = relay.var("var_12136", dtype = "uint64", shape = (160,))#candidate|12136|(160,)|var|uint64
call_12134 = func_12133_call(var_12135,var_12136,)
output = call_12134
func_12137 = relay.Function([var_12135,var_12136,], output)
mutated_mod['func_12137'] = func_12137
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12185 = relay.var("var_12185", dtype = "int8", shape = (9, 4, 1))#candidate|12185|(9, 4, 1)|var|int8
const_12186 = relay.const([[[-7,-2,-7,8,7,-1,7,-6,-2,4,8,8,-4,-6,-4],[-3,-7,-3,-9,2,-10,-2,10,9,10,-10,7,-6,10,10],[-10,-7,1,1,-3,-5,-5,-2,-6,-7,-4,-5,-4,4,2],[10,-10,-10,6,-8,-6,4,9,-8,-6,-1,1,-3,-6,1]],[[-2,1,7,-10,5,-4,2,-4,-3,-6,-7,-1,-5,-5,1],[1,6,-5,5,6,7,5,-9,10,3,-2,5,1,10,-2],[-2,6,5,1,-9,4,-8,-3,9,-10,3,3,7,-9,9],[-10,2,-9,7,1,-8,2,-3,6,10,4,-9,-3,-2,5]],[[-2,4,-3,5,4,6,2,-9,-4,-6,-10,10,-7,8,-5],[-1,-2,-3,8,2,5,-4,-7,1,-8,8,7,-9,-10,4],[-4,2,-1,-8,2,-3,-2,-3,1,-10,1,7,5,2,3],[-1,-2,2,6,4,-1,-7,3,-2,4,-3,2,-2,-4,-2]],[[-10,-5,-6,6,6,-3,7,10,2,4,5,-2,5,-4,6],[-9,1,-9,-10,10,-4,-3,-3,-1,-4,-2,2,6,5,10],[7,10,-3,6,3,-9,9,8,-4,8,5,7,-5,9,-2],[-3,-10,9,-1,9,3,1,-10,5,-9,2,-6,-5,3,-10]],[[3,-5,6,6,-1,1,3,-7,10,-8,6,5,10,-10,2],[-7,-5,7,8,-1,10,-2,-4,7,10,1,5,7,-5,-6],[9,3,-6,7,6,3,-2,1,4,7,1,-2,-5,-2,8],[-9,-5,-2,3,-5,1,-8,-4,6,5,4,5,-4,4,3]],[[8,-10,-2,-4,-4,-7,10,8,2,-4,9,-5,-5,-5,9],[-3,-9,1,-5,-8,7,-4,9,-1,-5,-10,-2,-1,7,7],[5,6,3,3,4,7,-7,6,-2,-6,1,-3,4,1,-1],[9,8,-8,-3,-9,2,-6,-6,4,-9,-6,10,-3,-5,-6]],[[-5,-10,10,-4,-1,-10,8,2,10,1,-8,-10,-8,3,-9],[10,5,7,-10,-8,5,-5,-6,4,-5,-5,-5,3,2,-7],[-6,5,10,5,-6,-10,3,-1,-2,-6,1,2,-8,9,3],[-1,6,-8,-1,-6,-10,-5,2,3,-10,-3,-10,-8,1,8]],[[-7,1,-4,-10,6,9,2,10,-9,-10,-1,3,9,10,3],[2,-5,-3,-5,-6,-9,-6,1,7,-8,1,1,1,-7,7],[-6,-10,-5,-2,6,-9,4,-7,1,5,2,-9,1,-2,8],[8,10,7,-1,-6,-8,5,4,5,6,5,7,1,-3,-6]],[[-2,-6,-4,-2,3,-3,4,-1,10,4,-7,5,4,-1,9],[-9,-2,7,-10,-3,6,-4,-6,1,-2,-3,3,-2,-6,-5],[10,9,-10,10,-7,1,-6,6,-9,-9,1,1,-2,2,-5],[4,-2,7,-9,-10,-7,2,7,9,-4,-8,-8,10,9,7]]], dtype = "int8")#candidate|12186|(9, 4, 15)|const|int8
bop_12187 = relay.not_equal(var_12185.astype('bool'), const_12186.astype('bool')) # shape=(9, 4, 15)
func_12065_call = mod.get_global_var('func_12065')
func_12067_call = mutated_mod.get_global_var('func_12067')
call_12190 = relay.TupleGetItem(func_12065_call(), 0)
call_12191 = relay.TupleGetItem(func_12067_call(), 0)
func_4987_call = mod.get_global_var('func_4987')
func_4992_call = mutated_mod.get_global_var('func_4992')
var_12206 = relay.var("var_12206", dtype = "bool", shape = ())#candidate|12206|()|var|bool
var_12207 = relay.var("var_12207", dtype = "float64", shape = (480,))#candidate|12207|(480,)|var|float64
const_12208 = relay.const([-3.589180,6.911279,2.799932,9.841324,-5.833802,-3.865322,4.239663,-6.887373,3.884336,-1.894406,5.955579,0.984864,-7.942230,-5.076217,2.562791,-3.549049,-7.904898,-5.742080,9.297892,-3.109117,3.243692,0.756725,-4.640585,1.120014,7.741986,-6.659616,-2.921171,-1.188104,3.849667,0.941213,2.921971,5.123358,6.219457,-0.050913,1.914584,-3.761247,7.836287,4.744306,-9.204625,9.072629,7.899318,-5.028625,-4.647694,-5.979446,-4.294343,-6.488038,1.755038,9.200486,6.316145,3.594975,-8.909338,-9.762733,2.067882,6.014226,-1.454320,3.967330,8.072418,5.281825,-9.744621,8.589596,8.021372,7.105930,6.151364,5.970737,-6.702252,6.573637,1.403709,-6.391456,-3.865065,-9.035402,-0.381988,-4.024193,1.228466,8.655564,8.852806,-9.724549,2.320265,-3.133329,-5.493063,2.403305,-1.368616,-5.013740,-3.670895,3.518899,-0.604618,2.452372,5.132315,-9.960165,-8.873263,6.775723,4.404187,-0.120032,8.609697,8.717188,6.989877,-4.671102,-2.236423,0.799409,9.324295,1.211502,-1.133875,-6.334854,-7.050374,-1.307158,6.922687,-8.647192,-7.381198,3.668917,3.505519,4.756878,4.300917,7.318398,-2.572270,7.910925,2.473729,-9.079279,3.794849,9.088529,1.544949,-3.322813,9.923021,0.573953,-4.533191,4.412888,-2.698426,-9.351926,-7.131750,2.917704,-3.226468,-9.677654,0.974748,6.205608,-8.378522,-0.167994,-1.960691,-5.050240,4.841584,6.147644,-7.583121,-8.060430,-6.041641,-0.647369,-0.434603,1.995833,-6.576749,-3.489696,-8.982145,1.640061,-4.080667,4.254726,-8.067775,0.575483,4.315367,0.623171,7.363443,-4.909304,-3.795061,4.543557,-4.465421,8.753964,-1.962143,-0.204638,5.553841,6.951102,7.365098,0.211773,-7.093677,-1.380433,8.163429,5.608007,1.246514,-8.007866,3.654108,-2.474746,3.158430,-5.236321,3.816770,-7.988816,-1.108027,-8.152945,-0.755128,-4.511569,-0.222115,9.049761,-8.033484,2.204389,-9.168085,-4.084723,7.407505,-6.487928,-9.924328,-7.381594,0.757460,5.432953,5.593140,-2.377330,7.081292,-6.118301,8.317180,7.849031,9.269316,0.249582,1.825908,0.333554,-5.237470,0.655598,-3.319471,-9.468583,-2.624519,-3.630172,4.426912,-0.077046,7.595568,0.762505,-5.810190,-2.158065,7.635596,8.679738,7.941114,3.123370,-6.703151,3.305587,-1.745234,2.814400,3.493879,-3.134353,-5.885786,9.936649,-2.202331,-4.401170,7.533194,-1.880560,-3.482629,9.400390,-5.916354,7.049698,9.014936,9.682704,-1.971816,7.495362,-0.414923,-5.135760,-4.240360,-6.956086,-6.415243,2.761191,-9.196765,-5.028481,5.796378,-8.503712,-5.340651,3.197223,-9.661614,-4.148548,2.508405,-3.879693,7.237849,-3.733154,-2.500258,-0.866908,2.955688,7.554571,3.317911,-8.065933,5.610893,-0.822432,-4.733718,-8.778556,7.703157,3.913591,-4.286255,-4.114255,-9.853633,7.588522,-9.901137,-3.173828,2.690921,5.418458,8.984970,4.493667,-6.038581,9.376050,3.724015,-4.454129,-8.052041,8.766056,5.652266,-8.173822,-7.129101,5.742370,-3.045561,-7.130377,0.874169,-8.175456,9.108914,3.556137,-5.928557,-1.474915,-3.987183,-0.089068,-6.454230,5.413929,0.105752,-7.306242,8.421591,-0.541625,1.307534,2.963106,-2.546724,6.417794,-6.982861,-1.383102,2.685584,-2.096277,9.330774,-6.259769,8.203891,8.103231,-6.386420,-5.022613,6.174755,1.530814,-7.977623,1.932824,-6.145819,-2.703582,-0.090925,7.946882,-3.380150,9.604225,-2.425995,2.913018,-1.401568,0.409333,-7.478424,-6.194221,-7.030127,-2.872286,2.627317,-2.635858,1.512033,-7.000617,4.669244,0.984747,2.978152,6.651360,2.846633,2.290111,0.081873,-1.646114,8.733669,-2.326634,-1.363217,-7.207687,-4.875864,0.478174,0.515476,4.772470,-2.846276,-5.986115,-0.145193,5.914656,7.261886,8.522389,6.834865,-0.654346,-8.039327,3.344261,-5.866617,-6.516908,-9.285112,-9.000560,8.953053,-1.448859,-3.214643,-1.576180,-4.327011,-1.225572,-6.122844,-5.221584,0.689833,-5.048649,3.588656,-4.999724,2.898153,5.348869,7.211735,-6.412147,0.507607,-6.443069,6.453847,-9.772408,-5.371292,9.776525,-1.237273,2.623408,9.967449,-6.066638,0.200835,-9.125347,1.066610,-2.038778,7.034445,-0.852026,4.888902,-1.692523,1.989426,-5.549340,-6.629603,-7.634794,2.103154,-4.918807,-6.367364,-8.149951,-7.632584,-6.686683,-4.501191,-4.792141,6.489787,-2.788292,6.568916,-8.613012,-5.946706,-4.471761,-7.510711,9.552169,-5.354341,-3.311555,-5.282366,-2.507994,1.738164,3.833417,2.043468,9.627454,-4.738521,0.691543,9.187689,-1.485853,-9.213347,-6.506190,2.255201,7.595607,0.658811,-3.028353,-6.309052,-4.109841,-3.508730,8.910454,8.202343,-0.114269,-8.437694,3.793909,1.978591,4.702449,3.750796,5.612010,-3.452746,-4.486467,-2.332163,8.271453,-1.757145,8.831552,0.229406,-2.275603,2.396093,-1.691292,6.818437,7.611400,3.427247,-6.438043,-7.058296,-2.457958,-4.950613,7.448702,8.519489,1.980113,-1.636876,-6.733497,2.925451,7.710631,-5.071610,6.060378,7.067240,-0.299797,6.183863,3.347470,-3.369904,-4.732303,3.947666,-4.838211,2.237581,-2.599295,-6.976519,8.164997,5.603274,-8.779208,1.209110,4.415301,2.139017,7.723281,3.379014,-6.839482,-7.611794,-8.171315,-1.338865,3.397097,1.370465,-8.434111,-7.488365,6.929860,-7.328257,4.696617,2.629232,-3.131012,6.287140,-9.675341,6.500386,-8.764843,2.660339,9.132103,4.535972,1.553617,-8.856962,-8.441984,-3.750775,-3.547220,-3.328277,-4.421617,9.364762,-8.109689,-2.555318,7.146733,9.557585,-6.970331,-8.090125,6.790947,-5.117921,-5.830189,-4.424098,1.663945,2.088610,3.181115,-3.136442,1.452954,-9.074933,-4.313689,-1.735730,-3.597215,2.133378,3.022458,-1.494188,-5.183233,9.337890,8.899844,4.723022,-4.029618,5.498245,-2.258819,2.278769,9.926952,1.566589,5.685803,8.795525,-3.965686,-9.745545,-5.058581,-5.784268,6.101541,-5.586199,2.598806,4.447966,-5.770552,0.919330,-1.948268,-9.619161,-1.637535,5.029493,-4.250549,-0.813129,-7.064264,-8.825736,2.437502,9.104589,-6.256144,-6.448192,3.970184,-1.176323,-3.627434,2.894227,-6.973667,-5.222809,2.660286,-8.348181,-5.241761,-6.826615,6.091104,1.517380,4.653583,8.123853,-5.548276,7.225536,-5.455791,3.954155,9.740948,3.044088,8.794153,7.639756,-3.655678,-2.509758,-3.731532,2.327686,3.309289,-7.932395,6.403724,-6.045619,2.467803,9.077454,4.210016,-6.465723,3.482058,7.713087,0.570545,-0.277220,-0.043264,-3.322695,7.939555,0.429951,9.625416,-3.391358,7.956531,-7.663709,-5.350899,-1.763549,9.983068,3.701129,2.053872,2.538218,6.771896,-7.314158,-0.711303,-4.381891,-2.176038,-9.848822,3.884654,-0.194659,8.738240,-3.795194,-1.715044,-5.406353,6.845185,9.337865,-3.025616,-3.315292,-5.098764,8.372503,5.191342,-5.254633,9.763566,1.179987,9.403913,-5.365937,1.486521,1.775600,1.230582,1.211850,5.702315,6.644139,0.147579,2.037567,-3.665153,-5.913322,-0.707434,2.370528,0.440651,-4.771651,-0.404866,6.325627,0.387770,-5.306370,-0.462470,-1.669703,-1.011154,8.989633,8.262646,9.230237,-8.780307,3.958676,-8.419660,-4.447236,-2.485296,8.822509,1.544475,-7.620613,3.084677,-8.780530,-8.222956,4.503700,-2.351340,-2.250353,8.426678,-5.114366,5.838769,-8.103809,-8.646757,2.869107,8.490572,-8.109263,4.103345,-0.690681,8.811750,7.213540,4.034988,-2.074486,8.787615,7.977542,-7.796264,-5.960027,6.223688,3.710773,-1.979016,-8.296430,5.183579,-3.648250,4.142753,8.648788,6.176227,-2.513971,6.001966,7.644498,5.884017,7.207106,-1.258118,0.653587,-4.376172,1.852854,4.137830,8.389020,-1.752140,-8.122154,-2.266462,-9.238135,-5.726246,-9.107685,0.121273,-6.470657,-4.818197,-4.487209,-1.076065,-9.022536,7.821765,7.708372,-4.396207,1.100748,-2.837520,-9.335026,-7.671375,1.887645,-7.559640,-1.886740,3.322031,-7.977257,7.845354,-0.431336,0.495903,-5.286845,-0.283855,5.131890,-7.328550,-8.179257,-2.370967,0.914679,9.498039,5.383560,-6.445584,-0.230954,6.569307,0.601490,0.305968,-3.349767,0.863383,7.854615,-2.890614,-9.014391,-7.384556,2.282121,6.395974,5.605941,8.109966,-5.408703,-2.128697,8.156634,-2.259980,-0.727449,-2.548671,-8.319926,-3.642078,-6.746956,-1.212877,6.521312,9.471754,-9.280146,-1.706671,4.669156,-9.095513,6.515890,-6.059051,-4.713556,-0.710439,9.160109,8.658469,-8.991479,9.790942,-7.704771,6.587929,-7.089458,9.051031,6.292083,-6.961916,3.178746,6.937131,-4.729152,-2.609126,-3.676900,3.258596,5.761242,0.264933,-7.584680,-1.361365,-2.943844,9.667103,-6.343423,3.270710,-6.021790,7.846846,5.076832,-0.167095,-9.943168,-6.867954,3.461928,-7.562099,6.406205,-5.857413,6.564812,-8.007369,-4.465584,-6.488694,-6.829581,2.009530,-7.249539,3.051596,1.566564,5.429907,-5.034522,-1.222740,0.378185,-3.681311,-3.134942,3.921461,-3.757895,1.342804,4.992509,1.127067,-1.772520,-5.201816,6.705637,-1.230440,1.840323,0.624523,3.811885,-4.695384,-9.783286,8.909626,1.976252,-0.051447,8.982452,7.952559,-4.419328,-8.852620,7.349282,0.699176,-5.143904,6.337263,4.257369,6.399354,-5.271721,2.291256,9.757088,7.661197,2.907259,-4.101961,2.349094,2.099444,-7.736432,-2.519384,-8.684509,1.408482,1.526946,5.960259,2.932282,-7.110411,-7.518451,-7.047182,-9.208643,-6.282595,-3.655171,-7.860702,-2.094439,3.494893,-0.415538,-4.730238,6.330755,7.026353,-4.771312,4.108620,-8.199648,4.068531,8.972448,-6.505474,0.766191,-6.402496,0.037980,-7.877562,-5.134851,-6.477898,9.136770,-2.307163,-7.215558,-6.472727,-6.515006,-9.607682,6.179803,3.381962,-6.283684,-0.672582,-1.349789,2.727225,-3.123454,-2.527377,6.523255,0.073878,4.276500,4.656156,8.091481,9.641153,2.973231,-0.379302,0.335160,4.544362,5.641414,-4.293357,-9.404822,5.406137,3.151312,-8.697550,0.202337,2.007418,8.327425,-6.125128,-0.699785,-1.440456,-8.364166,-8.791478,-5.478314,6.037369,-6.723406,2.865742,6.912676,4.406226,-7.442306,6.213628,7.207849,4.915280,9.732939,8.622841,4.979021,6.744936,7.784154,0.983214,6.123620,0.361916,-7.948127,5.618599,-4.134887,-2.505761,-4.471114,-5.513449,8.801609,-4.431027,5.560135,-0.210899,0.902027,-6.435552,-1.398720,-8.401437,-7.124048,9.129408,-0.880374,-0.388602,7.672444,-4.491194,-7.262877,9.568799,-0.046639,-5.917719,8.560850,-3.634917,-0.101902,4.453855], dtype = "float64")#candidate|12208|(1008,)|const|float64
call_12205 = relay.TupleGetItem(func_4987_call(relay.reshape(var_12206.astype('bool'), []), relay.reshape(var_12207.astype('float64'), [480,]), relay.reshape(const_12208.astype('float64'), [1008,]), ), 2)
call_12209 = relay.TupleGetItem(func_4992_call(relay.reshape(var_12206.astype('bool'), []), relay.reshape(var_12207.astype('float64'), [480,]), relay.reshape(const_12208.astype('float64'), [1008,]), ), 2)
func_9509_call = mod.get_global_var('func_9509')
func_9511_call = mutated_mod.get_global_var('func_9511')
const_12214 = relay.const([[5.371319,5.918957,-2.325478,7.254936,9.169293,3.035961,-5.868368,4.306581,-2.682896,3.220608,1.915728,3.255072,2.976203,1.440166,-5.879476,-8.405336,9.133250,1.938447,-6.064738,-5.731293,2.578128,0.927062,-6.169289,8.646492,9.779255,7.751778,4.907961,7.528065,-3.729525,8.571343,1.944395,-5.814674,0.155928,-1.271134,1.551142,-5.014453,-4.412717,-3.719617,-5.450100,2.043704,-7.111675,-1.279610,6.108105,-0.016798,-7.984704,-9.700860,1.241397,9.760987,-4.776737,3.746384,-4.911031,3.234970,3.113861,-5.866781,0.894321,8.020892,-2.839402,-5.398615,7.882139,8.063283,-1.066085,6.258254,2.395153,-6.701894,-7.498357,1.016709,7.770125,2.733210,-8.985205,-6.447433,9.919204,1.527653,8.529146,9.395932,6.977604,1.126416,-8.333763,2.907608,2.489077,2.926392,0.304359,-3.543733,3.451997,6.273027,9.429724,-0.596784,4.695497,8.310312,6.611121,4.918694,0.729189,-7.653803,4.449294,5.467636,1.967024,-6.400672,3.609733,-6.958079,-2.868391,-6.719213,6.461208,-9.855212,9.068426,-0.669495,-1.553538,6.221565,-6.551202,1.472994,6.047749,-5.561570,-3.014002,-8.630925,9.509587,-1.259293,-4.840222,-3.881802,0.184025,7.723925,-9.669320,7.846723,3.799822,-3.492896,-9.878624,-9.827589,8.220739,9.485075,7.125916,1.226216,-0.579903,3.773009,8.725622,-0.019654,-8.416003,4.862716,4.241678,-9.110920,5.027715,-2.192713,-2.357941,2.303046,4.478357,3.295062,-7.221948,-8.920441,6.136444,-1.701962,6.970452,2.492134,-1.228075,-0.315640,-0.775896,-4.300692,4.917901,5.988739,1.010016,8.522720,5.883869,-1.363216,-6.346681,-4.009101,-4.544525,-8.360878,-6.639607,3.683346,-7.729244,-7.572512,-9.681536,-3.785888,-7.132322,-0.962848,-9.666325,-1.268821,-6.163530,-7.046840,5.793350,-1.110210,9.898030,8.355143,7.702308,-1.954711,-1.677715,-8.592224,8.864483,0.565282,-5.327592,-3.402860,6.320968,1.833878,3.063914,-8.966018,-5.953448,-6.794737,1.439965,6.080641,-5.157360,-6.310220,0.303855,-8.239868,2.993412,-9.382465,1.673037,4.967467,3.087886,-5.581982,-2.606734,-1.766953,-7.523291,-3.713035,-3.487338,-8.731901,6.974772,-2.545992,4.529741,1.222302,-0.798945,-0.323637,-4.655896,-9.671195,-6.819750,-4.212946,-9.385952,-7.023581,0.139031,-2.322400,-4.875580,0.084219,-6.498701,-3.960662,-1.107796,-6.786561,6.968727,-0.958676,-0.071369,-8.837780,8.714294,7.445906,2.470318,-1.512771,-7.059031,-6.047805,8.365611,-8.036457,1.921298,0.556411,8.758087,-0.183903,6.108580,-4.821498,-1.932377,-8.552823,-8.329389,6.733140,4.118950,-0.059608,-1.098108,9.943975,-2.023393,0.931665,-0.245471,7.144336,2.356557,0.513718,-3.381823,-9.817422,-9.863688,5.338033,7.116195,-4.959274,-0.447666,-2.255523,8.265513,8.443566,-4.446674,-5.938445,7.231512,-3.374971,5.149192,8.237073,9.705802,-9.195577,5.175534,-8.940682,-3.241106,2.405745,-2.978820,-5.029157,0.551889,7.628351,-7.096465,2.351690,-2.021827,-4.056743,2.377902,5.286562,-5.808003,-5.061215,4.346837,-8.329140,2.155049,2.649309,0.595152,9.906167,5.643082,-3.277851,-0.726389,8.295693,6.457456,5.928764,-3.842576,-5.568347,-2.545400,-6.107822,6.897122,-8.187668,-5.031574,-5.762126,2.671512,2.481328,4.407001,-9.669789,9.336746,-7.899023,-6.178531,1.654788,-5.030415,3.363362,-7.925726,4.525635,-6.116666,-7.131705,4.291127,-8.887733,-5.026073,9.185677,-8.470943,-6.092633]], dtype = "float32")#candidate|12214|(1, 336)|const|float32
call_12213 = relay.TupleGetItem(func_9509_call(relay.reshape(const_12214.astype('float32'), [12, 7, 4])), 0)
call_12215 = relay.TupleGetItem(func_9511_call(relay.reshape(const_12214.astype('float32'), [12, 7, 4])), 0)
func_2726_call = mod.get_global_var('func_2726')
func_2729_call = mutated_mod.get_global_var('func_2729')
var_12217 = relay.var("var_12217", dtype = "float32", shape = (18,))#candidate|12217|(18,)|var|float32
call_12216 = relay.TupleGetItem(func_2726_call(relay.reshape(var_12217.astype('float32'), [1, 3, 6])), 0)
call_12218 = relay.TupleGetItem(func_2729_call(relay.reshape(var_12217.astype('float32'), [1, 3, 6])), 0)
output = relay.Tuple([bop_12187,call_12190,call_12205,var_12206,var_12207,const_12208,call_12213,const_12214,call_12216,var_12217,])
output2 = relay.Tuple([bop_12187,call_12191,call_12209,var_12206,var_12207,const_12208,call_12215,const_12214,call_12218,var_12217,])
func_12223 = relay.Function([var_12185,var_12206,var_12207,var_12217,], output)
mod['func_12223'] = func_12223
mod = relay.transform.InferType()(mod)
var_12224 = relay.var("var_12224", dtype = "int8", shape = (9, 4, 1))#candidate|12224|(9, 4, 1)|var|int8
var_12225 = relay.var("var_12225", dtype = "bool", shape = ())#candidate|12225|()|var|bool
var_12226 = relay.var("var_12226", dtype = "float64", shape = (480,))#candidate|12226|(480,)|var|float64
var_12227 = relay.var("var_12227", dtype = "float32", shape = (18,))#candidate|12227|(18,)|var|float32
output = func_12223(var_12224,var_12225,var_12226,var_12227,)
func_12228 = relay.Function([var_12224,var_12225,var_12226,var_12227,], output)
mutated_mod['func_12228'] = func_12228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11578_call = mod.get_global_var('func_11578')
func_11579_call = mutated_mod.get_global_var('func_11579')
call_12279 = relay.TupleGetItem(func_11578_call(), 0)
call_12280 = relay.TupleGetItem(func_11579_call(), 0)
var_12291 = relay.var("var_12291", dtype = "float32", shape = (9, 5, 14))#candidate|12291|(9, 5, 14)|var|float32
bop_12292 = relay.equal(call_12279.astype('bool'), relay.reshape(var_12291.astype('bool'), relay.shape_of(call_12279))) # shape=(9, 5, 14)
bop_12295 = relay.equal(call_12280.astype('bool'), relay.reshape(var_12291.astype('bool'), relay.shape_of(call_12280))) # shape=(9, 5, 14)
func_11979_call = mod.get_global_var('func_11979')
func_11980_call = mutated_mod.get_global_var('func_11980')
call_12346 = func_11979_call()
call_12347 = func_11979_call()
output = relay.Tuple([bop_12292,call_12346,])
output2 = relay.Tuple([bop_12295,call_12347,])
func_12381 = relay.Function([var_12291,], output)
mod['func_12381'] = func_12381
mod = relay.transform.InferType()(mod)
mutated_mod['func_12381'] = func_12381
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12382 = relay.var("var_12382", dtype = "float32", shape = (9, 5, 14))#candidate|12382|(9, 5, 14)|var|float32
func_12381_call = mutated_mod.get_global_var('func_12381')
call_12383 = func_12381_call(var_12382)
output = call_12383
func_12384 = relay.Function([var_12382], output)
mutated_mod['func_12384'] = func_12384
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11751_call = mod.get_global_var('func_11751')
func_11753_call = mutated_mod.get_global_var('func_11753')
call_12443 = relay.TupleGetItem(func_11751_call(), 0)
call_12444 = relay.TupleGetItem(func_11753_call(), 0)
var_12454 = relay.var("var_12454", dtype = "float32", shape = (9, 5, 14))#candidate|12454|(9, 5, 14)|var|float32
bop_12455 = relay.multiply(call_12443.astype('int64'), relay.reshape(var_12454.astype('int64'), relay.shape_of(call_12443))) # shape=(9, 5, 14)
bop_12458 = relay.multiply(call_12444.astype('int64'), relay.reshape(var_12454.astype('int64'), relay.shape_of(call_12444))) # shape=(9, 5, 14)
output = bop_12455
output2 = bop_12458
func_12460 = relay.Function([var_12454,], output)
mod['func_12460'] = func_12460
mod = relay.transform.InferType()(mod)
var_12461 = relay.var("var_12461", dtype = "float32", shape = (9, 5, 14))#candidate|12461|(9, 5, 14)|var|float32
output = func_12460(var_12461)
func_12462 = relay.Function([var_12461], output)
mutated_mod['func_12462'] = func_12462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11751_call = mod.get_global_var('func_11751')
func_11753_call = mutated_mod.get_global_var('func_11753')
call_12596 = relay.TupleGetItem(func_11751_call(), 0)
call_12597 = relay.TupleGetItem(func_11753_call(), 0)
output = call_12596
output2 = call_12597
func_12617 = relay.Function([], output)
mod['func_12617'] = func_12617
mod = relay.transform.InferType()(mod)
mutated_mod['func_12617'] = func_12617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12617_call = mutated_mod.get_global_var('func_12617')
call_12618 = func_12617_call()
output = call_12618
func_12619 = relay.Function([], output)
mutated_mod['func_12619'] = func_12619
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11305_call = mod.get_global_var('func_11305')
func_11307_call = mutated_mod.get_global_var('func_11307')
call_12631 = func_11305_call()
call_12632 = func_11305_call()
output = call_12631
output2 = call_12632
func_12653 = relay.Function([], output)
mod['func_12653'] = func_12653
mod = relay.transform.InferType()(mod)
mutated_mod['func_12653'] = func_12653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12653_call = mutated_mod.get_global_var('func_12653')
call_12654 = func_12653_call()
output = call_12654
func_12655 = relay.Function([], output)
mutated_mod['func_12655'] = func_12655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11578_call = mod.get_global_var('func_11578')
func_11579_call = mutated_mod.get_global_var('func_11579')
call_12659 = relay.TupleGetItem(func_11578_call(), 0)
call_12660 = relay.TupleGetItem(func_11579_call(), 0)
output = call_12659
output2 = call_12660
func_12669 = relay.Function([], output)
mod['func_12669'] = func_12669
mod = relay.transform.InferType()(mod)
output = func_12669()
func_12670 = relay.Function([], output)
mutated_mod['func_12670'] = func_12670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12669_call = mod.get_global_var('func_12669')
func_12670_call = mutated_mod.get_global_var('func_12670')
call_12789 = func_12669_call()
call_12790 = func_12669_call()
func_11459_call = mod.get_global_var('func_11459')
func_11460_call = mutated_mod.get_global_var('func_11460')
call_12792 = relay.TupleGetItem(func_11459_call(), 0)
call_12793 = relay.TupleGetItem(func_11460_call(), 0)
func_6589_call = mod.get_global_var('func_6589')
func_6592_call = mutated_mod.get_global_var('func_6592')
const_12796 = relay.const([-4.141802,-3.035640,-4.456425,9.563608,1.306582,-2.280725,-5.642276,-6.022404,-2.257341,6.553893,-5.626477,0.721425,-1.162562,5.400004,-5.277975,-8.175668,-3.351857,-3.148847,-6.259571,0.976884,-5.562528,7.093225,8.340220,-7.569305,-1.591638,-6.602273,-4.836548,-3.923450,1.694262,7.622534,0.524414,3.909873,-0.558938,-2.961162,7.327844,8.612355,0.430523,2.063493,-9.295881,4.119181,7.824899,1.644445,4.550517,-9.553479,5.007985,-2.540659,-2.278424,0.190198,5.340012,5.574582,1.465289,-3.607897,-5.612894,1.437391,7.664409,4.453217,-0.870595,2.842791,8.780057,0.823736,6.096937,1.159881,3.378246,-4.193651,-3.127099,6.446703,-9.002633,3.888437,0.548361,-4.439906,2.959807,4.895414,-2.227029,1.909712,7.221670,9.354610,-6.848379,-1.210765,3.756461,-8.799101,-5.042219,7.292214,0.216736,5.986097,6.440896,0.533569,-0.738820,5.954683,6.970270,-3.045741,1.287350,3.827513,-4.878402,4.141869,7.812499,6.786935,7.979110,-1.911873,3.511718,-7.504477,1.990691,8.215706,-2.761929,1.321786,6.432261,-8.737120,6.924869,-4.564758,0.204019,9.125837,8.558533,9.719259,4.034912,1.778589,9.412079,5.756609,-0.106375,-7.002856,6.139120,-0.365401,8.671286,2.163064,1.032297,-1.757065,9.913192,1.809369,2.797210,-7.195465,-0.891079,7.886241,7.602931,8.634232,-4.778106,-2.149870,3.857350,-4.860979,-0.944403,2.603962,-7.939555,-2.650587,3.612605,-6.387045,-5.226225,2.957062,3.343276,6.968296,7.926203,-0.297252,-9.253919,-7.744455,8.292393,0.597647,-8.396444,7.571934,-2.683334,3.660190,8.713370,-2.072897,-2.527991,5.585468,6.799861,-2.585084,2.035545,-3.609257,8.443497,6.010072,0.496192,-3.511308,6.678798,-4.033997,-2.297509,6.245196,-6.680080,1.649556,3.160940,-5.484911,4.471511,1.547841,9.778607,4.852060,-7.693099,5.494867,2.458026,-8.651250,-4.066830,-5.792189,-6.249755,-7.774528,-7.046508,8.530405,-3.628617,-8.518383,-3.751390,-6.333800,7.093894,-8.317386,-6.650219,7.222450,-8.026261,-7.909712,6.738235,8.001538,-2.755643,-1.217094,3.129392,-6.794600,4.799162,-4.794767,0.494732,1.161028,-3.946396,-7.015152,1.034933,-0.741624,2.741466,-9.550050,1.148096,-6.235359,-2.752350,-2.128546,-9.230810,4.550640,9.313865,8.107743,8.200269,2.598559,5.021703,-3.683703,-9.179451,-5.391996,-0.026682,-0.898593,-3.306319,7.785117,6.756427,-2.460046,2.530423,2.011334,0.761928,1.766556,2.408719,-8.313544,-4.413134,8.140406,6.895909,2.848529,0.107699,-8.547517,-8.498916,-3.019806,1.803277,-7.694957,-5.178905,-0.615883,-9.626174,-1.243456,-9.825199,-0.999761,-2.365460,7.385597,9.421130,3.910381,-4.166222,-7.579056,9.542292,-8.280152,-2.353074,2.303202,-4.375232,-0.461550,6.186207,-0.494572,-2.238516,7.057067,4.796339,-4.436309,1.055517,3.861246,1.566399,-8.313682,-2.644378,-3.929060,0.500761,4.647739,7.580347,9.300958,3.317849,-5.813426,-4.720000,-0.599362,6.112659,6.271264,-9.365581,-6.115657,-2.627445,-2.616743,-5.841278,0.254275,9.811447,7.078665,5.921962,2.483028,3.550299,-6.481024,2.362618,5.887691,0.272436,4.602290,1.145447,-9.476263,8.341351,-8.865862,5.984921,8.535968,-3.185229,3.938895,6.687194,-8.678044,-0.404760,2.813510,4.680039,-8.238409,4.668247,-9.101932,-4.365282,-1.454422,-3.125829,4.544984,2.951089,-3.050947,7.914318,4.435994,-9.170894,1.425493,-3.413901,4.251636,0.326861,-6.957765,0.508354,7.369106,6.388184,0.125177,-7.397823,5.641592,-8.748669,-8.879122,6.504603,-3.180352,9.542202,2.445540,-5.640033,-2.714306,-8.484009,-8.625161,6.700572,8.546144,-8.127909,-1.353480,4.318481,-4.310544,2.254879,-2.579379,-8.986964,8.467984,-4.577373,4.988196,3.760862,4.136953,-1.186044,4.384576,7.282826,1.338524,-1.961737,3.665361,2.861822,4.697987,-2.028918,-9.437136,-8.826548,-3.771309,-6.341669,-6.902976,0.740234,8.715213,7.640389,-5.797780,-4.000688,-2.318635,2.348394,-3.215574,3.145786,-1.328128,8.423222,-6.261846,-4.651418,8.997989,-6.482680,-5.224376,7.769780,-2.490852,-6.254417,6.280892,-8.130708,6.259496,0.591467,-1.148117,6.204268,-7.467613,3.393447,1.804956,-1.958790,-4.590371,-8.303127,-5.652817,5.251322,-4.223634,4.362914,-9.489089,-5.893793,-1.512839,9.419001,-9.171394,5.099011,-4.906652,-5.825428,-2.818672,-9.561823,6.838193,0.005186,-6.645859,-3.410733,-2.939776,-1.300625,4.324984,7.479669,3.945595,6.316140,7.926999,-9.673505,3.822063,9.722627,1.802742,5.934728,-5.682659,1.079809,7.294432,-2.471698,1.676951,-3.684533,0.901282,-6.205994,-9.076879,-9.908703,-0.623671,9.913289,3.861033,9.136760,-2.374548,-9.137483,3.378457,6.445838,3.599451,4.964254,7.778791,-8.085588,7.453267,0.948305,-6.172435,0.998772,-2.241269,-5.738918,-4.534785,1.225297,-4.258532,2.707417,4.503306,-3.115697,-8.530310,7.518331,4.240115,-6.369743,3.875675,5.289945,-9.897362,-0.246677,3.355834,-3.233141,8.465328,9.473940,1.254031,5.411215,8.467937,-6.665425,4.114480,9.510079,9.234777,3.393414,8.474252,-1.368032,-9.770625,8.236484,6.425694,3.407469,8.364515,4.028606,4.720887,7.562610,-7.668987,9.905420,3.686134,2.117101,-2.691876,5.343719,7.638955,8.983420,0.726145,5.000693,1.323904,7.519874,7.249498,8.442632,1.965159,-5.268103,-1.792415,-8.070105,-8.603860,-5.240744,-8.841211,3.698789,1.227047,6.565904,4.801826,-8.897659,5.073846,7.167160,-1.369475,-5.247353,3.937217,7.456338,-5.362972,8.018771,6.759884,5.450797,-4.237689,1.648968,-9.995878,-2.399690,-6.584069,-7.300266,-0.488683,-4.225323,-1.844857,-1.244916,8.097405,-9.255646,7.893746,4.661586,1.420367,3.888923,2.821129,-6.350184,1.597013,6.849517,4.309141,-5.869094,2.724539,-8.006006,7.352148,3.109201,-5.913083,-5.305292,9.139485,2.190839,-6.940620,-2.233040,6.207908,0.761240,8.213025,-5.172177,-3.306959,-3.598292,-7.770243,-4.893097,-3.981979,-5.546229,3.427430,-5.528337,-0.632487,9.065405,-7.830248,-8.479261,-6.609084,4.136484,-4.003223,-6.109930,-0.185121,-2.583879,4.592528,-4.802500,-3.994830,5.459883,5.294816,4.818668,9.127642,-9.196898,-3.223212,9.537914,4.634006,1.525590,1.169338,-7.105433,-6.473131,-1.155891,6.159606,7.187527,8.511206,3.825784,5.604451,4.823327,-7.913842,-3.150389,-9.612108,8.596758,-4.875811,-3.842793,3.909412,3.726217,8.432454,7.728436,-0.202459,3.659732,9.870589,-7.087983,9.102621,4.694198,-1.311710,-3.102444,-0.439875,-8.499213,-9.327971,-2.566280,0.295082,-5.804297,6.303689,-2.101891,-5.849448,2.655284,-4.759524,-1.894076,8.271870,1.529382,-7.330322,6.264942,-6.899961,4.729194,-2.409116,-6.083571,-0.190619,-8.012240,-1.592659,0.731463,-3.934970,5.073178,5.457036,-0.098190,2.197789,-5.185626,-7.987527,-9.133513,6.416888,0.932109,6.855478,5.621276,-3.393606,2.760406,-2.757541,-6.459369,-9.692838,-4.974838,3.195212,-1.763246,-0.192799,-9.215580,-3.326460,8.352473,9.825334,0.197347,-5.296101,-0.212689,6.639649,-7.447113,-5.063599,-8.261899,-2.054377,-9.283603,-7.938679,-7.397807,4.717707,6.300169,-5.108974,0.074075,8.141983,-0.958183,-8.231559,0.817464,5.552495,6.188209,-3.506467,-5.279783,-7.458538,-4.980367,0.223454,-7.516037,-9.590268,2.638486,-8.482180,-2.857526,0.133945,-0.276507,2.426346,3.821360,7.040085,-5.488015,0.502182,-5.122977,-9.863844,-3.200817,8.237800,-8.067798,-7.929117,-6.545948,8.661873,-7.382376,-0.493225,-6.105711,-2.904238,-8.494022,-0.074980,1.558935,0.717313,-6.043632,5.477516,6.908442,8.922685,-5.365479,2.521037,-3.235334,9.936804,-1.858640,7.306280,8.048101,-0.352223,1.474151,-8.147561,-8.061432,-5.964136,7.935611,7.036633,5.413258,0.270726,-8.218994,-0.623643,0.420751,-6.393169,3.400345,-2.645356,0.405026,-9.173375,8.653320,-2.958987,-7.964327,-0.416194,-8.715814,7.795528,-7.400767,6.602409,8.999222,-2.674380,5.676487,-3.667480,-5.794541,7.070049,-4.142825,9.667273,-7.207714,1.264183,-5.856331,4.335729,-9.533811,-8.308127,5.704841,6.074566,-8.680523,9.340924,-7.284688,-0.573502,-8.987943,8.515415,-3.444563,-2.356633,-5.009793,6.142654,-8.855723,7.462506,4.078378,9.521494,4.856260,-9.872969,-1.830325,1.175404,1.851910,-3.476757,9.372191,-8.802665,-5.634390,-4.154269,4.259437,6.466284,-1.062441,-3.186325,3.859782,-5.584139,-2.763625,-5.188414,-6.061039,-2.960106,5.217740,9.211258,-6.980297,-6.414897,8.319719,6.154770,8.745101,-7.887370,5.776698,5.723553,-7.403158,0.140945,-8.619522,-0.995390,0.896599,6.467388,6.309476,2.656840,-0.207368,-0.825164,-1.138130,-8.751415,-2.494815,-5.300676,7.737703,-1.357235,0.833908,2.172219,2.941908,2.951329,-2.765441,-4.592339,2.516810,0.352995,2.001621,7.969263,6.938630,3.216082,-9.839030,0.862968,-3.724640,-3.968478,1.522927,2.235512,3.118684,6.131286,5.715642,6.974245,6.144666,3.849626,-2.795650,-8.851274,-9.406084,1.990965,4.419869,3.639253,1.534186,-9.736708,4.502630,3.130739,-3.730822,-9.783056,-1.314693,-2.647863,-9.434405,4.882800,7.531852,-4.093942,7.381569,-5.951868,-6.321114,-7.523667,0.971069,-7.653997,0.649508,6.143814,-6.814303,1.302532,4.780717,-2.654440,7.066159,-4.796371,4.346237,0.980631,8.168727,-0.757027,4.934114,7.225667,7.405160,7.726938,5.599745,-0.095850,-9.390064,5.598991,3.148774,3.191413,0.740437,7.011300,-6.734944,4.464308,7.838849,2.759789,7.398420,0.231030,-0.648609,5.744054,-6.968787,0.664221,9.482008,-5.737022,-9.409200,-8.367074,-7.927985,-3.792182,-4.956617,-6.442329,7.106111,-8.597077,-4.432086,2.700627,-3.255891,-6.038480,-5.111804,7.019777,-8.254178,4.248120,6.594494,-5.025315,6.839689,-3.716921,1.143701,3.744789,-2.426800,7.914634,-8.327236,0.771725,5.948687,1.427534,4.030402,5.167097,-2.261892,-6.412181,-5.954973,9.041444,1.830806,2.511371,-3.060267,-9.657762,-0.928427,9.441124,-8.987012,3.660999,7.198149,-6.266660,7.400648,-3.615502,-2.211049,9.354925,-5.547162,-7.440724,-1.538886,-2.357808,4.617004,9.228345,-4.222325,-9.539109,4.177104,-9.930743,-6.886872,1.082229,-3.679030,2.530695,-4.269738,-6.894293,-9.170663,5.432894,-4.599414,1.214797,-4.051605,-4.901793,-6.614891,1.571301], dtype = "float64")#candidate|12796|(1008,)|const|float64
var_12797 = relay.var("var_12797", dtype = "uint64", shape = (13, 10))#candidate|12797|(13, 10)|var|uint64
call_12795 = relay.TupleGetItem(func_6589_call(relay.reshape(const_12796.astype('float64'), [1008,]), relay.reshape(var_12797.astype('uint64'), [130,]), ), 3)
call_12798 = relay.TupleGetItem(func_6592_call(relay.reshape(const_12796.astype('float64'), [1008,]), relay.reshape(var_12797.astype('uint64'), [130,]), ), 3)
func_1211_call = mod.get_global_var('func_1211')
func_1214_call = mutated_mod.get_global_var('func_1214')
var_12802 = relay.var("var_12802", dtype = "float32", shape = (396,))#candidate|12802|(396,)|var|float32
call_12801 = relay.TupleGetItem(func_1211_call(relay.reshape(var_12802.astype('float32'), [9, 11, 4])), 0)
call_12803 = relay.TupleGetItem(func_1214_call(relay.reshape(var_12802.astype('float32'), [9, 11, 4])), 0)
func_3117_call = mod.get_global_var('func_3117')
func_3120_call = mutated_mod.get_global_var('func_3120')
call_12826 = relay.TupleGetItem(func_3117_call(relay.reshape(call_12795.astype('float64'), [4, 12, 10])), 1)
call_12827 = relay.TupleGetItem(func_3120_call(relay.reshape(call_12795.astype('float64'), [4, 12, 10])), 1)
output = relay.Tuple([call_12789,call_12792,call_12795,const_12796,var_12797,call_12801,var_12802,call_12826,])
output2 = relay.Tuple([call_12790,call_12793,call_12798,const_12796,var_12797,call_12803,var_12802,call_12827,])
func_12828 = relay.Function([var_12797,var_12802,], output)
mod['func_12828'] = func_12828
mod = relay.transform.InferType()(mod)
mutated_mod['func_12828'] = func_12828
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12828_call = mutated_mod.get_global_var('func_12828')
var_12830 = relay.var("var_12830", dtype = "uint64", shape = (13, 10))#candidate|12830|(13, 10)|var|uint64
var_12831 = relay.var("var_12831", dtype = "float32", shape = (396,))#candidate|12831|(396,)|var|float32
call_12829 = func_12828_call(var_12830,var_12831,)
output = call_12829
func_12832 = relay.Function([var_12830,var_12831,], output)
mutated_mod['func_12832'] = func_12832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11095_call = mod.get_global_var('func_11095')
func_11096_call = mutated_mod.get_global_var('func_11096')
call_12846 = func_11095_call()
call_12847 = func_11095_call()
output = call_12846
output2 = call_12847
func_12848 = relay.Function([], output)
mod['func_12848'] = func_12848
mod = relay.transform.InferType()(mod)
mutated_mod['func_12848'] = func_12848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12848_call = mutated_mod.get_global_var('func_12848')
call_12849 = func_12848_call()
output = call_12849
func_12850 = relay.Function([], output)
mutated_mod['func_12850'] = func_12850
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12653_call = mod.get_global_var('func_12653')
func_12655_call = mutated_mod.get_global_var('func_12655')
call_12915 = func_12653_call()
call_12916 = func_12653_call()
func_5923_call = mod.get_global_var('func_5923')
func_5925_call = mutated_mod.get_global_var('func_5925')
const_12925 = relay.const([-6.340808,-3.193092,5.710952,-7.759701,7.707081,-0.945189,-6.154058,1.664626,-2.792582,8.390508,-9.722904,0.252346,-8.950524,1.070499,-5.937096,6.046193,-0.916055,4.080999,-3.366866,0.112640,-5.327069,7.609076,-7.197950,7.177741,-7.610931,4.059633,0.193049,-0.509931,-2.122558,-4.784670,-3.043841,8.074494,0.219994,-2.826776,-8.739878,2.792532,4.715970,0.997176,6.933654,4.902948,-4.629635,-2.467161,8.907928,0.312087,-6.526010,-3.119863,5.105521,-4.168208,-1.273847,3.234467,-8.198228,-8.716905,3.554877,4.336371,-3.103876,-5.146605,-1.939815,1.263958,3.261028,4.112176,-6.960995,-1.053694,-2.172963,-6.229796,2.173849,9.408915,-0.300326,-3.949824,-9.145083,-6.253416,-6.102075,8.729026,9.634497,-2.331334,7.553811,7.285333,2.953380,9.054452,-5.168424,6.017235,1.743750,6.228824,-6.983876,-9.579649,-4.516408,9.565401,3.769165,8.188829,8.435368,-2.847088,3.709157,-9.842466,8.636833,-6.836323,1.812989,-4.926103,3.315464,-2.615693,1.625758,-8.013926,5.995419,-0.354568,-7.685752,-0.801585,7.014994,-3.145256,-5.550032,4.447578,-0.842895,9.825307,4.772131,9.504089,8.180918,-9.735247,-2.809828,-3.763544,9.049800,-0.568536,-1.384174,9.918867,5.941429,5.639865,6.592412,-5.866311,-0.879778,0.792832,4.130117,-8.097870,4.464124,8.808254,2.851074,6.374002,-8.905467,-0.176105,-8.817953,-7.226784,8.002459,8.502054,-9.803883,6.391460,5.125275,8.043405,9.959881,-3.078690,-0.703708,-3.791510,4.058039,-6.032048,5.398130,8.165788,5.288050,-9.770519,3.665563,6.642839,1.622192,-3.655138,2.841554,0.128346,-8.764011,2.911771,4.300566,-8.508346,-4.657185,-4.912237,-3.265267,0.942983,8.235607,-5.517019,-6.448577,-3.023936,-5.455323,-4.686194,-1.087759,-2.183491,8.096204,-3.526666,0.618844,-9.213255,5.771915,-8.101933,-4.316123,0.409250,3.745859,-7.514731,5.269652,0.982262,6.612243,-4.882993,7.510417,-8.566886,-9.520613,3.856029,-8.878453,2.269182,-8.240717,1.571643,-7.074438,-1.247040,-0.673259,2.428865,7.888638,-1.145622,-1.382231,9.722422,9.295579,9.807833,-2.095672,-3.730204,-0.294510,-0.091719,3.785444,8.815257,3.946597,4.603037,-7.672742,7.244550,3.332513,-1.992735,-8.336491,9.773858,-0.873951,-1.342110,9.197342,8.819200,-1.307914,-8.997672,8.801727,4.317026,2.500021,-1.690145,6.166019,5.367029,7.218928,4.980566,9.463405,-7.834847,4.844613,-5.563734,0.460157,-5.012840,-7.929877,4.636265,-8.024804,-2.070403,0.314850,0.420212,-7.003832,2.813866,-8.692058,-5.757288,2.883417,7.825245,4.558812,7.105970,0.001658,-4.444049,-2.002360,3.933416,6.969088,-5.347776,1.142968,2.221869,-8.209988,5.963751,4.196796,2.251260,-1.318985,7.784470,-9.812473,-3.648167,-8.856520,1.458410,-5.413915,8.662497,-6.025039,-9.308435,7.993172,-7.107566,-7.392952,9.925517,2.298912,-8.616177,3.151965,3.812414,-4.730657,-0.859195,-7.851411,6.919649,-8.241768,-2.999804,-7.194263,-8.920771,0.501180,-7.873939,0.185211,3.634621,-0.192375,-0.375650,-8.652985,3.078418,-4.930478,5.045627,-4.112584,2.821711,-9.599335,4.191663,0.186860,-5.182221,-8.958703,-6.522839,-9.268646,-9.781642,-9.192118,2.693177,-1.348899,6.882696,-8.834722,-7.023980,-1.886796,0.303062,3.589597,2.523206,1.378658,1.966683,-9.523801,8.086280,-6.694142,5.379709,-8.004402,2.777039,-4.844103,4.465770,3.864987,0.673542,-3.617679,-4.546065,7.682513,-5.853655,-9.365641,5.356001,7.989397,0.116000,-1.348716,-7.331335,8.027679,-4.296698,0.696335,-0.826263,4.497278,-2.677261,5.251224,5.543007,-2.312060,3.135383,-2.346950,-7.113334,4.574517,8.721722,-0.391589,-8.824565,1.316150,2.107714,6.908936,5.195203,0.419703,-8.608967,2.905515,-7.384396,9.550795,-6.658152,-1.083392,7.428156,-1.126739,3.830500,2.389940,9.567084,-0.608614,7.419044,-5.389865,-3.727074,-7.364944,-3.628151,2.729973,0.479195,-0.679260,-4.824950,-2.259902,-3.855429,-2.304081,-1.011288,-5.400097,-1.500336,-4.489532,-9.177476,-8.430622,6.941802,7.843708,-3.707075,-8.452998,7.532687,3.840116,6.850310,1.776542,9.057275,4.095340,1.239635,8.438437,3.344580,8.330119,-4.799481,-6.596565,-5.771835,-4.331780,-7.052083,0.458179,5.556121,3.598253,-1.850449,5.795108,-9.705388,0.460107,-8.989347,9.280003,3.912976,9.314548,6.090699,2.461444,4.817088,-6.782095,-5.067339,1.828364,0.433472,-9.147202,8.550103,2.448211,-0.125277,-0.323670,4.491909,-6.203162,-8.580577,-4.091439,-4.577620,-4.890086,9.098271,0.579821,-5.324231,-9.274575,-7.458492,2.202126,-7.088357,9.284464,-0.796189,3.766535,-8.029347,-1.719912,7.996327,-1.173380,-7.121724,4.364695,1.328342,7.644586,6.372984,0.696175,-8.650920,0.322260,1.555349,4.833224,-9.554296,4.249576,6.396915,-9.356410,1.837418,-0.772714,3.513683,2.809338,-0.550339,-6.197615,-9.476766,7.783081,-7.129244,5.527987,-7.518020,9.703495,4.620316,7.876190,-9.156404,6.514322,-8.106294,2.820191,5.632297,-6.046534,1.039185,8.326296,9.371281,-5.026453,-5.062901,4.647371,3.777343,8.407009,-7.459466,1.963148,-8.706846,-3.252018,-8.709313,-8.461547,-8.040883,4.531247,2.028079,-1.775940,-8.749775,1.332514,-8.585887,1.925866,1.585431,3.124368,7.388756,4.880169,8.709323,-4.813562,7.146687,-2.237401,0.343213,-5.469910,-2.234073,4.255918,1.585015,5.186585,-7.108713,7.523765,-2.318700,6.156610,9.802069,4.202846,-5.042766,-6.707853,7.018797,3.718821,6.400079,8.722141,-2.342688,-5.334376,0.859916,-5.666907,-4.320792,-8.509747,-0.468695,-4.141205,-3.795437,-6.951125,7.214387,-3.021962,1.730810,3.652846,1.257095,2.588346,-6.891600,-9.174123,1.891549,1.827379,-6.947291,-0.004140,1.275867,5.433153,2.378240,-6.051404,-7.447652,8.331272,-0.732122,-0.192449,4.337599,-9.370460,8.211521,-2.054155,3.045706,-4.644904,1.669386,-9.455547,0.498543,-9.372249,3.077526,8.935911,0.035773,-7.141285,-4.127269,-3.769392,-1.309454,6.234143,8.810901,-4.702102,1.382021,-3.980098,-7.022140,0.973139,-0.290104,-3.030332,-2.853691,-3.461536,-8.959854,4.439509,1.339857,-9.490972,-0.251241,-7.087656,1.494688,-8.333346,6.419681,7.713241,7.563468,-9.671707,-9.501918,-5.813801,-2.644422,8.178373,1.432798,1.210050,-3.566939,-5.548708,3.835828,-9.447358,9.733506,5.049285,3.723635,-9.053896,6.910250,0.357251,2.687212,-8.194608,-4.936036,-8.390867,7.060732,-5.971742,-0.392715,-4.367929,2.072721,-6.732481,-6.036652,-2.347839,2.693559,-9.417331,5.990013,-4.010542,7.452091,-3.830027,-2.865807,7.248476,4.969133,0.106558,-5.828610,0.760784,-2.004522,3.053079,-8.941653,8.925633,-3.035746,-3.813258,8.993118,5.391033,-4.310698,-0.259346,-5.286006,-0.057508,2.460405,5.507705,6.370136,-6.222869,5.977995,-4.976895,8.292712,5.154864,-9.716731,2.278295,-0.985946,-0.326621,-9.584742,-3.695873,3.729732,-6.246734,-3.387668,-4.688439,6.993281,-4.007864,-2.714769,-3.076026,-5.684788,-6.753857,4.956561,-7.227784,-0.710992,-8.922515,2.947025,3.145917,8.616900,6.676761,-2.642845,-3.742573,-0.371807,-1.804975,5.865290,-1.812325,-5.684509,-2.765050,-6.208055,5.734299,-6.295363,-3.661205,-5.235867,-3.616541,1.591273,-1.057156,7.990642,6.545624,4.899202,6.040910,-4.214185,-3.390222,-9.816490,6.621427,2.798864,4.674819,-1.605525,3.986989,3.226512,2.412892,0.706022,-5.281846,-2.536357,1.097256,9.275248,-5.364261,-9.017097,-9.140637,-3.873933,-2.838967,0.684425,4.616956,0.487899,-3.447138,-1.581358,4.930246,4.397073,-0.959533,-1.863489,1.280075,-3.987118,0.782261,-6.952095,7.609726,7.043706,-0.529494,5.542781,0.022708,-2.754717,-2.765729,4.759706,3.110181,4.655019,-0.559621,2.426583,-7.641274,2.715642,-1.894405,2.717019,-7.690913,4.286379,4.951345,-4.862784,1.509427,9.413915,7.152790,-6.116502,6.663718,9.527249,2.266993,-0.693866,-6.251837,4.289867,5.252041,4.826965,-1.124325,8.425676,3.109273,-6.413852,-9.300021,-9.610082,-1.039990,-0.371665,7.985580,0.016445,-6.313354,-3.053714,1.611135,-0.383797,-2.989401,4.651440,-0.008760,5.516556,-8.364439,5.360981,8.616482,5.628141,-3.707075,5.758060,2.300438,-6.170681,-9.872641,-6.979955,-4.345017,7.218599,-4.509632,3.166239,9.338182,3.506157,-0.115205,-1.675780,-8.236783,1.846763,-2.671339,-3.315887,5.271389,8.705756,3.494390,-6.517477,-5.682460,3.803161,-8.575194,-3.898960,5.996326,4.076023,-1.352787,9.913155,7.213976,9.554374,2.110812,6.127896,-6.951250,7.172049,6.813608,5.557511,9.958006,-9.973254,-7.247528,5.734204,-3.857232,3.341541,-6.600295,-3.738939,-7.177835,5.441112,4.098601,-4.270159,-1.454545,-7.123005,4.113552,1.339359,-2.883080,-8.159386,-8.270514,-9.571289,3.573016,2.241161,-1.057374,9.831998,5.789302,-5.238134,-7.308788,-8.965117,-6.391567,-2.699175,4.329389,-1.667919,4.907219,-2.512373,-1.822523,7.660024,-7.335629,-4.460250,-6.957242,2.003639,-0.859608,-6.843244,4.805368,5.135658,0.075024,2.134487,-2.237811,-0.697352,7.725253,1.602895,8.260553,1.126393,-7.748182,-9.894939,5.493714,-7.101302,-1.622087,-3.044336,-2.671884,2.581168,7.039601,-7.240624,8.380753,-9.125235,0.379447,-8.823467,-6.520271,-3.207380,7.286144,0.295878,0.358121,3.631670,-2.591871,1.625745,5.809050,9.961059,1.465595,-7.013674,-7.498026,6.672375,1.340811,2.150729,2.462550,-2.558945,-2.152665,-8.646492,2.006553,2.726111,4.955275,-4.370066,-5.777871,-4.689982,1.168935,-6.802146,7.069363,1.836445,9.143300,-0.824842,6.443456,-0.137488,-5.072961,7.817518,-5.827474,7.539563,2.268631,-4.738430,2.423044,1.739439,-1.497269,4.638139,-8.994917,-9.504799,5.089208,-6.488093,3.810170,-8.701684,6.733665,1.950371,8.942229,-9.517186,5.557465,-7.958582,3.148262,0.989368,8.686221,2.890238,-6.275940,1.623919,-6.178770,-0.910193,-6.955865,5.608217,-4.480345,2.368605,9.780289,-2.797605,9.649138,-6.765880,-4.257452,-8.678878,-6.344433,3.627355,5.185628,-1.312035,4.525556,0.402431,6.459976,0.636959,5.292719,3.903887,-5.501684,7.403021,-2.510796,-2.478722,-9.206628,-9.351674,-7.115874,2.105843,7.271509,8.555176,-4.930757,-3.875588,9.219638,3.935158,0.371145,-1.953771,-7.376313,9.136119,4.131240,6.657069,-5.203411,-2.315646,-4.657356,-1.088371,3.000983,-0.922701,-6.335396,0.749641,-9.668028,-9.527752,-8.123526,-9.044350,9.969443,6.995868,2.542729,-7.576664,2.348792,8.408385,-7.063436,2.670223,2.969810,9.322515,-8.687464,-1.933434,0.294840,-7.234347,1.297971,-0.840519,-7.832492,9.017117,-4.225078,6.026188,-2.874831,0.300182,-6.422156,-9.512405,-6.041882,6.470473,-2.624253,-1.213403,8.212151,1.293651,2.384232,1.856103,-4.946806,7.982939,-7.676833,-8.498574,1.664723,0.833339,-2.246093,-4.139904,5.100984,9.272011,4.534421,3.527407,6.035991,0.955783,-8.895608,-8.132600,9.828807,4.130212,5.901016,-6.807013,-9.838569,-0.321075,3.152137,5.945390,3.761512,-9.614032,-4.485348,8.781713,2.238693,-2.511268,3.601716,-8.477817,6.612291,-8.233339,1.322935,9.211981,-4.410046,-8.330095,-3.019905,-7.379627,-9.985140,-2.553005,-8.140472,-8.889094,-1.832302,3.668494,-1.756490,-3.719620,8.351852,-5.777907,2.129205,-8.625325,0.373819,8.184560,0.393021,0.374661,3.063612,-1.543310,7.965480,7.900485,-5.809345,1.996494,-0.763393,-2.983138,-9.840781,-1.464922,-5.554056,2.637714,9.937921,-7.392457,-0.889068,-1.485196,2.157902,5.822453,-9.813775,8.241067,0.973368,0.037428,-9.459048,-8.939707,-9.237776,1.993554,7.924253,-8.353027,7.624867,5.114150,0.669176,8.065536,7.795064,4.766229,3.125776,-9.577340,-5.090352,-3.505221,2.227881,1.175219,5.170488,-3.745217,-9.344106,3.113992,0.711549,4.161486,5.155321,-9.605467,-3.538752,-1.739687,-4.759942,-9.820248,-5.649785,6.307034,3.342520,0.850993,4.955103,-4.798593,-7.355809,-8.327917,-6.163258,-6.517824,-5.437974,-8.715886,4.580964,0.023400,5.412587,-2.012210,-1.666070,1.928986,-3.257297,2.699521,7.100285,5.668467,0.208588,6.150185,-8.043981,7.441104,-9.250787,6.377412,-6.954569,5.959301,-3.547773,9.516087,-9.643922,9.241636,0.948352,-5.742689,-6.011127,4.725692,3.848466,3.890983,-0.403451,0.057987,4.404946,-2.794535,9.751065,3.718616,3.080490,-1.955952,-0.631351,0.175371,-8.502410,-3.492283,2.111372,0.232336,-6.473830,-7.599539,0.441922,-3.708659,-2.662907,7.810092,-8.773329,-0.783941,7.038813,7.785393,-6.491720,-0.279342,6.756401,7.878001,-0.418392,5.908855,8.850587,8.920538,7.801370,9.416738,8.189714,1.444556,-7.442968,9.107095,1.203761,2.128703,7.271661,-6.733591,-8.168220,-7.693418,-5.838009,2.570004,7.426602,3.947989,-9.300762,5.265854,8.682833,-2.060986,-5.688677,0.544627,-5.210408,3.475631,-1.579823,-9.397865,9.748707,7.242809,4.817505,8.946768,-9.365243,0.081930,-3.514585,-6.653418,-8.231926,4.745785,-8.379263,-3.542080,9.102539,0.604663,7.276818,-5.684752,-8.100789,0.973554,-1.329425,-5.034378,2.258117,-9.884589,-8.504167,0.258654,1.839129,4.707724,8.819226,-8.982194,8.794078,0.467679,-5.153003,7.470560,3.681386,-3.610507,-4.865660,-8.462411,-1.446573,2.195246,8.015468,2.591742,2.556363,1.447448,-0.963139,9.390640,2.287099,3.947415,-0.223476,-6.925291,7.514096,2.457847,7.103738,8.261495,-1.796353,5.193420,9.001855,-1.965747,6.783720,0.966277,-3.064676,-1.013272,9.611425,5.036163,-1.557747,-0.908217,-6.779517,5.386877,4.651705,2.219683,6.739598,-6.188978,-6.892671,1.297576,-0.092791,9.336204,5.204277,-8.844563,3.732114,-5.293041,6.178019,1.145821,8.303229,8.128710,9.132867,-1.067879,1.092653,6.318107,-2.430508,-0.402733,-5.507168,3.174397,1.743954,-8.261053,4.510612,-2.234838,5.752672,-2.920564,6.536551,-2.625392,-9.496292,2.660600,5.761449,0.426427,-3.190217,-0.454857,-1.159886,-1.229133,9.123313,-7.096990,-1.141576,1.360046,7.581530,-9.278434,7.246634,0.556599,7.586839,-7.431034,-3.574816,-6.829892,1.139388,1.605202,-9.815273,8.193474,-2.354790,-0.890082,-7.267356,2.089488,4.207513,-9.177583,-5.688633,7.390284,0.180476,-1.815474,2.266792,-6.386896,5.770306,-2.935707,8.706665,2.376037,-9.363125,-0.948833,2.297357,-4.959291,6.628495,6.310814,-6.802111,-1.447591,-2.538170,0.940581,4.411716,-9.242820,4.959616,8.598899,-1.104426,4.669002,-2.934699,-2.387668,2.097701,1.186971,1.551543,-9.476507,9.515586,1.235120,6.582385,6.842790,-3.846560,5.108201,1.774587,8.760882,3.217509,-2.411082,-2.805549,3.082394,5.385959,0.425929,2.979335,-6.890691,-5.766632,0.341882,7.759946,-5.529684,-8.886586,3.741619,-8.087183,-6.482028,2.240863,-2.417884,6.815336,6.913403,-9.900011,9.464691,-8.660478,-4.088751,-1.815452,-0.173389,-0.053027,3.273395,-2.210637,-5.900633,5.095917,-2.479327,8.803588,0.196377,-8.866194,2.618755,6.592742,0.434360,5.031181,-6.555299,6.404343,0.903928,9.824479,-4.270768,9.862450,0.271786,1.634166,-2.123603,-6.137856,2.778475,-4.213871,3.000838,-1.643648,-6.732029,-7.721281,6.075674,3.366876,5.117065,7.486202,3.410219,4.534510,-3.445926,-2.883682,3.327419,-3.628905,-9.861664,-5.715923,-9.419808,-1.842670,-4.161036,1.331384,-8.227420,-7.675570,5.002164,5.781125,-3.625067,3.092745,-4.106126,5.041045,-6.311138,-6.856354,0.864815,-0.501962,4.638789,-5.430295,4.910233,9.835775,-4.922329,-5.797245,-7.688528,-4.742155,-3.870091,6.543699,-1.770141,-2.817746,-6.800268,3.132559,1.457739,0.427661,-2.994613,-1.224733,5.520904,6.520988,8.274802,2.463008,4.755647,7.601797,-6.689713,-9.021433,5.616592,6.648048,-3.174610,3.886460,4.513270,-6.111594,-4.477569,6.106056,8.467927,-5.236188,-8.875536,-6.390331,5.051663,0.186868,-9.454310,-1.906591,4.215824,7.708830,-1.200780,5.400308,9.817372,1.867744,9.898046,1.853211,1.236860,4.204355,3.854778,-7.049606,2.306398,-5.467359,2.058401,-7.742047,8.108605,-9.791469,-8.967151,2.482413,-6.942427,-7.941271,2.073950,-8.590922,3.900803,6.139417,9.619505,4.699446,4.884343,-0.366473,4.582311,1.180059,-7.090114,-7.671677,-4.454343,-7.098025,6.365818,-0.065413,-8.746523,9.594433,-7.199260,-8.539914,-6.420240,9.331545,-1.072732,7.396671,-1.521215,-7.208202,-7.255546,1.922096,-6.751400,0.477090,-8.582054,-5.797075,-2.729822,-9.337291,-4.983801,-1.118633,0.760692,6.252504,1.377066,5.685656,2.405916,-2.240230,-6.949643,-2.977621,8.146588,-6.470757,2.826895,-1.168493,2.736965,2.980604,-5.615091,-2.092067,3.829147,6.510531,-6.654201,-9.693823,-8.342271,-7.207807,-0.643836,5.716648,-4.741963,-5.620044,-7.438519,-7.896463,1.543883,-6.993142,7.260071,2.755008,-5.608749,-3.783192,4.047961,-5.713851,5.710257,3.329032,-8.694647,-4.086758,-9.111698,-0.442012,8.873900,-6.003312,-2.776015,-2.358416,-2.176658,-6.923226,-3.200156,3.308579,0.805742,6.550085,-8.933635,8.848655,5.235200,-6.915191,-9.123444,3.153162,3.155497,-0.637847,-7.112937,5.991691,5.988845,0.184612,-7.447014,9.626835,-2.021538,2.500419,9.245644,9.324657,-3.103996,2.040004,3.577022,-0.808420,-4.504080,-8.712096,-7.254719,1.726300,-8.640022,0.774912,-9.494174,-5.565544,-7.558930,8.662531,-5.085323,-0.561652,-7.174272,4.435988,-7.635068,-8.659136,8.982147,9.456650,2.535596,8.547153,7.773105,-3.000920,8.365106,8.856697,-8.590278,-1.602577,0.877363,4.830663,-8.165845,9.874508,3.475903,1.755509,3.199327,-9.200186,-9.356393,-8.374969,-5.293727,7.038028,1.164995,6.616652,1.235614,2.068793,7.502489,1.801961,5.724299,-6.184794,-5.333204,6.952016,6.882711,-1.190237,3.587920,9.136895,-5.628287,-9.637829,5.066163,6.012943,2.055266,-8.524942,-5.311314,-3.956563,-5.272996,-9.512925,-2.855482,-9.759918,3.430008,4.432120,0.989841,-6.344384,6.930152,-1.780332,7.059740,-1.094661,-9.870156,2.638782,-3.275366,-5.558603,-2.903740,0.177321,0.861607,-7.369265,7.351336,6.230097,0.723543,-3.410064,-6.954881,1.555892,-7.808314,-5.957885,-1.298947,1.626557,8.178240,-2.356683,-3.886189,9.460656,1.828170,-8.205979,4.921463,-1.518608,-7.118127,-5.153197,9.802654,-8.013883,6.693567,-8.978209,-7.277455,-2.494235,4.388042,6.321738,-5.482874,9.321382,3.479925,-6.532208,-4.144171,1.687102,7.890325,1.370983,2.577750,8.147020,4.878086,0.278952,3.123351,0.667906,-6.145295,5.393611,2.252001,-0.014066,-6.756232,-1.606579,3.574121,3.193510,6.258804,4.969666,-5.931148,1.488953,-1.353921,3.026093,-9.194173,6.061276,-9.800931,4.040104,2.020838,-9.664941,2.695970,-0.987806,-5.055670,8.696164,2.902495,-5.946308,6.114804,8.027970,-9.817542,-7.657433,4.014479,2.135195,-6.645457,-5.378473,7.706153,4.668256,0.928355,7.207379,-8.738469,6.035606,-8.074209,7.139033,3.201805,5.693946,-0.740357,-1.938727,1.845907,2.748874,-6.236267,-5.951380,-0.571161,-6.308829,1.234598,4.438489,3.256208,6.223415,-3.191156,5.213045,3.748091,-2.986949,-8.578951,-0.442395,-1.001966,3.583682,0.175900,-7.067295,-5.298900,6.742840,0.974196,2.993952,8.111012,-7.036549,8.397843,1.639956,-7.166660,-6.714265,-3.361793,5.037881,-4.976540,5.302143,-3.723378,7.984797,0.631446,-5.389033,5.132883,0.040118,0.456437,6.525308,0.262045,1.774313,-0.221591,5.660248,-1.379299,9.899941,5.333078,-9.678768,7.536166,-7.154900,-8.892575,5.959543,-3.000885,-2.409102,-8.753664,3.814705,-4.395652,2.797096,-7.330125,8.998785,2.085262,-3.829695,-9.938718,-3.139651,-3.169813,-0.940202,-6.234358,5.865369,-8.872156,-7.933835,1.882671,-5.474061,-3.341387,-4.642838,-7.915992,-0.905227,-4.588523,4.907756,6.867778,-5.273333,-3.881504,8.089792,-7.576574,-7.119340,-8.823217,8.705578,-0.122322,-2.500230,-5.346294,3.923471,-3.467749,-9.046078,-2.723385,9.312771,-6.985888,-4.112232,-3.186033,1.555003,-6.076752,5.380267,-9.269026,-8.152408,6.112961,8.365253,9.307350,-5.746196,-8.664357,-3.213699,-7.876488,2.004178,-5.533684,-0.942322,0.124494,3.901666,4.351260,-7.968968,-3.489677,-6.011077,2.726943,9.770759,-3.643930,3.278544,-9.366173,-6.399595,0.690220,0.308523,7.773642,4.847629,3.161444,-7.029438,4.185670,-8.216513,2.171631,0.052583,6.635462,3.672185,7.987548,-1.442145,-0.271195,-7.674308,-4.921868,4.237188,8.681910,-2.940306,-6.349104,8.785921,-4.662808,9.207414,-4.558146,-5.677764,1.067078,-6.056710,-2.777176,-6.524047,2.478939,5.560485,7.211743,1.978308,2.302946,1.013439,-0.835101,8.546155,9.598600,-4.633850,-9.485781,7.823877,-9.025752,-8.134615,-4.921398,0.610162,2.964121,-4.248958,-0.899985,-2.417232,8.827431,7.378408,-5.933367,-5.688356,6.547594,-4.385324,-7.813877,9.752667,1.490336,4.572104,-1.150337,5.953026,6.425362,-9.419277,8.108811,7.652192,9.849625,-3.520445,-7.454864,1.370645,5.825482,2.098779,2.557956,-3.346333,-4.233970,-5.659984,-1.386951,-4.709344,1.271029,9.209190,4.959970,-2.486134,2.346168,4.099802,7.284014,7.238290,-9.741048,-7.279042,1.825196,-4.167166,4.968997,8.471512,-9.091615,2.853905,-9.325558,-2.719455,-9.697428,-3.020570,1.500648,3.083444,-8.044438,1.174829,5.473575,-3.968875,-6.047099,-3.152877,-6.283393,6.120997,8.772049,-6.779522,-7.988508,-5.049400,5.911388,-7.176360,-2.613363,-6.359098,4.965003,0.148543,2.908833,0.560809,-6.390617,3.087070,6.048571,8.405936,-0.371878,4.560673,-4.513259,4.059029,-8.915547,-4.822539,5.622748,-1.483849,-5.576454,3.820284,4.038216,2.171902,-7.513012,-6.486189,2.148206,-5.541289,-6.413059,-5.939038,7.936141,-0.489970,-3.968906,-5.824554,3.860524,-6.414029,-5.386470,-2.934809,-1.188510,5.231992,-6.469832,0.384410,3.327803,0.203041,8.922720,-5.528502,6.719204,-1.935845,6.085470,4.409767,5.557219,-0.445566,0.257710,-9.511030,-8.356977,-8.616434,7.550499,8.862661,-5.250190,-3.514277,-5.998189,-7.152090,-6.478208,9.385512,-3.323741,-8.870364,-1.699651,7.814033,5.091415,-0.545331,-3.526609,4.455015,-2.164781,-8.752565,5.819069,-9.894767,-8.211569,-0.454880,5.791921,-5.233106,-9.297404,-0.018189,-6.423033,8.791605,8.642502,5.219378,-4.709368,8.714377,8.284288,4.913778,3.994757,4.881122,6.303369,-3.579575,2.134510,-8.222020,2.472949,6.141273,-8.684354,-3.702025,-3.560348,8.907602,-7.592112,1.056323,4.750590,-7.721244,-4.377950,-6.711429,2.378941,-1.127400,0.560166,1.768238,0.048234,-4.827171,2.886690,9.123577,9.971320,-4.737665,-5.288973,6.668267,6.842065,-5.455354,2.395670,1.115766,2.071153,-5.101697,-8.787864,8.294821,-0.977431,4.615640,-9.497013,8.570491,-8.357936,4.761150,8.621697,-3.842280,9.601102,-4.742959,2.617994,1.580033,2.027993,9.203763,3.879972,-7.612880,3.209543,7.918896,-1.648218,1.556740,2.949099,7.929577,3.711113,9.867022,-9.984256,-8.997489,9.034668,-2.419246,1.298374,-3.050796,1.325866,-8.670019,-0.863910,-3.621361,-9.558517,7.538121,9.159318,-0.339575,-6.226480,9.840865,2.237617,-8.719821,2.207519,6.343068,4.838627,-8.342744,-5.854840,4.491081,-4.196125,-2.095325,0.426904,-1.850765,-2.574381,0.089793,-8.903823,-9.019839,-9.497331,-6.616241,4.648426,-2.660314,5.371831,4.128912,4.028447,0.528287,2.537945,-1.169957,1.630983,8.139062,9.860380,2.660778,8.156727,2.557975,-1.071239,9.788083,-9.310309,-9.432693,-4.885101,4.731097,-0.273774,-6.687352,-4.891355,-8.770891,7.477851,-3.839100,9.279036,5.309781,6.447087,-3.069042,-1.418904,0.195760,-3.373571,1.657403,-4.482138,-3.957567,0.300347,-8.737986,-9.820288,5.831175,-0.940638,-7.708267,1.516116,-3.785004,9.204480,1.551421,-5.257650,-0.139719,-4.951519,-1.795507,-4.623484,-7.930486,2.146070,-1.348969,0.908224,9.458798,7.454543,6.118179,0.027499,6.813338,1.353095,8.502775,8.486848,-4.134014,2.058375,-9.545563,5.966539,2.135229,6.084579,-8.173772,0.414164,-0.748848,-7.976583,-8.059225,6.143447,-1.275599,-4.796896,0.032781,1.764547,8.363341,-2.825787,-1.935538,-5.144186,-2.018150,0.023022,6.917208,-3.680352,0.063411,6.143101,0.789616,7.341594,9.809232,4.595586,-4.359442,-7.699920,3.332922,0.099154,7.562756,8.544305,-4.533193,-4.456496,4.299624,5.816950,0.837722,-7.588068,-1.642277,-1.124548,9.060335,-5.326887,-1.992225,-8.952850,5.077693,-1.159935,3.014458,-5.434730,-3.801212,5.489467,7.964373,4.041116,-1.574874,4.197062,7.021468,-9.675850,5.403912,-2.181970,-5.204537,9.421258,2.040261,-5.897725,7.617950,-9.517256,6.414115,-0.385500,-9.303964,-1.083919,7.918401,3.677583,0.689466,-7.528370,-3.463915,4.243222,0.964427,-5.364128,-9.746955,4.637225,5.641635,1.399888,-6.538845,-4.282556,2.749301,1.412310,-8.282530,-2.663927,-1.870518,7.093897,3.486949,2.827914,0.060137,9.789979,-2.732547,-3.544045,-3.977469,5.458969,6.422444,-3.617755,-4.457989,3.358206,-3.261406,-1.257096,-8.416980,-4.860703,-7.829015,-4.823255,3.696792,5.574662,7.896962,-5.783113,-3.058633,-0.610665,5.830203,-1.716701,-0.634533,-9.376666,6.645094,0.247430,-2.179383,-0.776648,-1.498562,8.439334,-8.996521,6.767352,-6.402479,-2.102381,9.118873,-0.953028,8.721681,-4.672719,-5.136211,-8.571974,-5.869535,-7.181078,0.402501,9.062084,5.837170,-9.395254,-4.435385,9.438568,1.442177,9.073621,-1.127393,1.935973,-9.026324,2.945209,-7.384078,7.244710,-3.890409,-2.819436,-6.364080,1.793801,-2.840683,4.617091,2.268093,4.808387,-9.638887,-1.459962,-3.429089,-5.929642,2.846458,7.127185,-2.497552,-5.829203,-3.128932,-4.819167,2.564001,8.343238,4.937063,-1.324286,1.747546,8.983291,-9.223934,1.097224,1.712728,2.376532,9.162270,5.779715,9.250933,-8.606389,-9.625324,-0.156007,-0.892255,5.850979,6.667949,6.753955,1.956108,-5.864152,-6.526382,-2.349214,-4.068862,-8.381168,-6.485840,4.357796,-2.662009,-5.176056,-6.384333,-0.673578,-2.740233,6.847240,6.841398,-3.992822,9.203481,-6.339758,-0.975388,-5.739403,-8.228644,4.043667,-3.665593,7.370468,-4.977335,8.431896,-2.559708,-6.527803,1.419807,-0.258551,-2.097761,2.845936,-2.183557,4.228653,-8.658957,7.087463,-7.617229,0.572076,4.805582,5.865663,-2.739990,-6.064505,-0.015688,2.010976,-6.239087,-4.639472,8.986102,7.799444,0.106425,-5.085724,-2.973293,3.748806,-4.457023,6.085635,2.191544,-0.041444,4.463196,-4.886885,2.544180,7.560185,-9.550738,-8.833707,6.814164,3.904372,-6.482453,-6.211781,6.481585,3.466639,-9.918635,7.863027,-8.673970,-7.478482,-9.166734,1.285678,-6.580995,-6.326980,0.687707,-0.716319,-3.852249,4.444194,-6.854784,2.664336,9.967483,0.816364,5.857134,6.389623,-4.189878,9.887060,2.142003,-9.236600,1.803473,-9.948587,3.434096,7.430445,-7.153617,-2.128578,-2.157304,-3.840889,3.343204,7.804204,-0.257170,-3.376132,-7.487432,7.983037,-0.690038,-6.839665,-4.745670,-2.232525,9.757092,6.563313,7.330294,-4.492755,6.693778,5.776365,2.251886,0.290497,-0.855573,-1.670897,0.597691,-4.658344,-9.723882,4.785891,2.974657,-8.001554,8.526603,-2.782374,-4.917895,-0.112249,5.632566,-8.974506,9.798184,-1.404356,4.629511,-5.924163,-9.377031,-7.902795,3.177466,-0.836760,-0.634373,-6.083854,-6.175291,-6.517505,3.279442,2.035041,-2.439879,5.282098,7.126977,8.748366,0.788520,-6.616214,-5.735956,-2.175119,-8.583929,-8.107624,2.305699,8.468732,1.696890,-4.941226,-3.579175,5.098880,4.957535,-8.784652,-2.638112,4.476120,-4.883028,-1.365236,7.353666,-9.177095,0.277837,-9.698338,8.628822,-4.858426,9.914875,-2.812200,-3.972220,-8.642469], dtype = "float64")#candidate|12925|(2704,)|const|float64
call_12924 = relay.TupleGetItem(func_5923_call(relay.reshape(const_12925.astype('float64'), [13, 16, 13])), 0)
call_12926 = relay.TupleGetItem(func_5925_call(relay.reshape(const_12925.astype('float64'), [13, 16, 13])), 0)
func_12065_call = mod.get_global_var('func_12065')
func_12067_call = mutated_mod.get_global_var('func_12067')
call_12948 = relay.TupleGetItem(func_12065_call(), 0)
call_12949 = relay.TupleGetItem(func_12067_call(), 0)
output = relay.Tuple([call_12915,call_12924,const_12925,call_12948,])
output2 = relay.Tuple([call_12916,call_12926,const_12925,call_12949,])
func_12956 = relay.Function([], output)
mod['func_12956'] = func_12956
mod = relay.transform.InferType()(mod)
mutated_mod['func_12956'] = func_12956
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12956_call = mutated_mod.get_global_var('func_12956')
call_12957 = func_12956_call()
output = call_12957
func_12958 = relay.Function([], output)
mutated_mod['func_12958'] = func_12958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12669_call = mod.get_global_var('func_12669')
func_12670_call = mutated_mod.get_global_var('func_12670')
call_12970 = func_12669_call()
call_12971 = func_12669_call()
output = call_12970
output2 = call_12971
func_12987 = relay.Function([], output)
mod['func_12987'] = func_12987
mod = relay.transform.InferType()(mod)
output = func_12987()
func_12988 = relay.Function([], output)
mutated_mod['func_12988'] = func_12988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11979_call = mod.get_global_var('func_11979')
func_11980_call = mutated_mod.get_global_var('func_11980')
call_13098 = func_11979_call()
call_13099 = func_11979_call()
func_9658_call = mod.get_global_var('func_9658')
func_9662_call = mutated_mod.get_global_var('func_9662')
var_13104 = relay.var("var_13104", dtype = "float64", shape = (30,))#candidate|13104|(30,)|var|float64
const_13105 = relay.const([[-8,-8,9,-8,4,8,4,5,-1,6,4,1,-1,10,-10,3,-3,6,10,-4,6,6,-9,-6,10,8,-1,9,-4,4,-9,2,7,3,-2,4,8,1,-5,-8,10,8,-7,-3,-5,-4,1,-8,4,10,10,-7,5,6,5,-4,9,8,10,8,-8,2,10,10,1,1,5,10,6,-2,7,5,10,6,3,-7,-8,-10,7,2,1,9,-3,-6,4,-7,-3,-9,-6,-3,10,-9,9,9,-3,-5,-6,8,3,8,1,-8,-10,7,3,4,-2,-4,-4,8,-5,2,9,-3,-6,-10,8,1,-7,1,-2,5,-10,6,1,-3,-1,8,-5,-2,3,5,-2,-9,-9,-10,7,-7,-4,3,9,2,9,9,2,-4,-3,-6,9,5,6,-9,1,-2,-8,-10,10,-6,5,-4,7,2,9,7,3,-6,-5,4,8,3,-10,3,-7,1,-6,-9,-5,5,10,1,-1,-2,1,-6,-3,-5,10,-5,10,-10,-10,-1,9,8,7,-3,-8,9,-3,8,-2,1,4,-10,3,-1,9,10,8,-9,7,3,9,7,-7,-9,10,10,9,8,-1,5,-1,-2,-2,3,-3,7,10,-3,10,5,-4,-6,8,3,5,1,-4,6,-4,-7,7,6,-9,4,10,1,-6,-7,3,4,-9,-3,-10,10,7,-8,1,-4],[4,2,-9,10,-10,-10,8,-10,-10,1,-3,1,-8,6,4,4,8,-4,8,2,2,10,7,6,-4,-7,-9,9,-9,9,-5,-3,-8,9,2,2,5,-1,-4,8,-5,-7,5,-2,-2,-8,-3,-1,-2,4,6,-8,-2,1,-8,-5,6,-5,-9,3,-7,10,6,10,-4,1,-2,8,6,1,-10,6,8,5,10,1,-3,-9,2,6,-6,5,4,4,-5,-5,-1,9,4,-9,5,4,-8,-6,4,6,9,-10,7,6,-10,6,-3,3,2,2,9,-5,10,-7,3,4,7,6,1,7,-4,3,2,7,-7,9,-6,2,6,-8,-5,3,-8,9,3,-1,10,6,-1,4,-1,-3,-9,-1,-6,-6,-3,6,-9,1,10,-1,-9,10,10,-7,9,8,-6,-3,-9,-5,7,2,-6,-8,-6,-5,-5,-6,-9,8,4,3,6,-4,4,-7,-3,-7,-3,-3,3,5,-3,5,-5,-7,10,9,-6,2,4,-1,8,4,-2,-4,7,4,-2,9,1,-6,-5,-8,-10,3,10,9,-1,-3,1,7,-9,-7,10,-8,-3,-6,9,-3,4,1,9,4,-4,-4,-4,-7,4,4,2,-6,4,7,-6,2,-6,6,4,7,6,-5,4,5,-5,-1,1,-4,-9,-8,-1,5,-3,3,8,5,1,6,3,-3,-10,-7],[-2,-6,2,-6,-6,10,-9,-7,3,2,-4,-9,-2,7,-9,-1,-5,-3,-10,-2,9,6,-5,6,-6,3,-1,-9,7,4,-10,8,-1,4,2,-10,10,-1,-10,4,-9,8,-9,2,-4,-1,-3,-10,2,8,4,4,-5,-10,4,-2,2,3,-8,-9,-3,-5,-1,-1,-2,6,-6,-9,-5,-7,-4,-4,-9,-10,-1,-7,1,-9,8,-5,8,6,10,-6,-6,-6,1,9,-6,-5,7,-1,6,1,1,-6,-5,-4,10,2,4,6,-7,-3,3,-9,-2,9,2,1,5,-2,-2,7,-8,-9,8,-6,-10,7,-9,-6,-1,-8,-6,-6,-10,3,-7,-5,-9,5,-10,2,2,-7,-10,-3,-7,-3,3,6,-10,-7,-7,-1,-7,-4,9,-10,5,-3,8,5,-10,2,6,7,5,4,-6,-10,1,-1,8,-3,-9,-10,-6,-6,-1,-10,-4,-4,10,-3,-3,1,-5,-6,6,-9,-10,5,4,-2,10,4,10,-5,8,-9,10,-6,-4,1,-4,6,9,-7,3,-10,3,6,-5,-4,-10,-3,2,-7,-2,8,-9,9,6,-3,-7,-1,-8,-4,10,6,-10,10,10,10,-6,-9,3,-4,-6,-9,9,-5,-6,10,8,6,4,-10,3,-8,8,-5,7,-1,4,8,-9,10,4,3,-5,10,5,6,9,9,1,-8],[1,1,-9,-1,-4,6,-1,1,-8,-5,-10,2,-5,9,-5,4,8,5,6,8,7,1,-2,5,-3,2,-3,5,7,6,10,-10,-7,6,1,7,-5,-7,1,7,-4,7,7,-5,-3,6,1,10,9,5,-9,7,9,10,-5,3,-10,-7,10,9,3,7,-1,3,-4,-9,9,6,1,-7,7,-8,-10,-1,-4,-4,-6,-10,9,-7,2,-5,-6,-10,-10,-5,-8,-1,-5,9,-3,-8,-5,5,4,6,-10,8,3,-2,6,8,-10,2,-3,5,-3,6,3,-3,-5,-2,9,10,-7,-5,-2,5,-3,-7,8,-2,-7,1,10,-7,-3,2,9,6,-6,9,7,10,-2,8,-9,3,9,-5,9,5,-1,6,9,-9,6,-3,-3,4,-9,7,1,5,-5,-10,-2,-8,10,-6,9,-3,3,-7,10,2,-4,-1,-9,6,7,-2,-10,4,6,8,3,-10,9,3,-9,-3,3,7,-10,-10,8,6,2,-8,7,-4,7,-7,1,8,-4,-2,-4,-1,-3,-1,-10,-9,-6,1,-2,6,-6,8,4,9,6,4,-10,4,5,6,-10,-10,-3,2,5,-7,-10,2,10,1,-1,-5,2,-6,-3,-6,9,-1,-8,-8,-10,8,9,-3,9,6,-1,-3,-8,-3,3,-6,-7,5,-10,8,9,2,-6,-8,1,5],[2,-8,-10,3,-10,8,-6,3,-9,7,-9,-7,-4,-9,8,6,5,2,4,-1,-4,2,-3,9,-7,9,3,-10,10,1,-5,-7,2,-6,-7,-1,-7,5,9,1,10,4,5,-2,3,-2,-2,-1,-2,-1,5,4,-8,-1,2,-4,3,6,2,-4,1,7,8,-8,-6,-1,-2,2,-3,8,4,-8,2,4,9,-2,5,4,9,4,-2,8,-10,-3,-3,10,4,4,-1,-3,8,3,-7,7,-8,1,5,-3,10,-2,8,2,-10,-2,-7,-1,10,-8,-10,3,5,-9,3,-9,-9,-8,3,-3,-6,-3,-9,8,10,-6,-9,2,3,6,3,-1,-4,-1,8,-9,-10,9,-9,-9,-3,9,4,-5,3,2,-7,-10,3,8,-9,8,-9,7,6,-7,2,10,-9,2,-8,-10,9,-6,5,-6,2,2,-2,1,6,6,6,-6,3,-9,-4,8,8,8,9,-6,9,-4,8,9,-3,-1,-1,6,-5,-8,3,-6,1,4,9,1,-9,-9,10,8,10,-4,8,-8,-6,-4,2,10,4,-1,4,-3,7,-10,9,-2,-9,2,8,-10,4,-1,-4,8,-5,-2,-3,1,-6,-10,-1,4,9,-7,5,9,-1,-8,1,2,-6,-6,9,2,-10,-10,3,1,1,-8,5,-8,8,-9,1,-7,-8,-10,10,-4]], dtype = "uint64")#candidate|13105|(5, 260)|const|uint64
call_13103 = relay.TupleGetItem(func_9658_call(relay.reshape(var_13104.astype('float64'), [1, 15, 2]), relay.reshape(const_13105.astype('uint64'), [1300,]), ), 1)
call_13106 = relay.TupleGetItem(func_9662_call(relay.reshape(var_13104.astype('float64'), [1, 15, 2]), relay.reshape(const_13105.astype('uint64'), [1300,]), ), 1)
func_2726_call = mod.get_global_var('func_2726')
func_2729_call = mutated_mod.get_global_var('func_2729')
const_13132 = relay.const([-0.612875,1.374688,-4.331664,1.087950,6.961371,1.669647,9.795197,8.908719,-8.793548,-4.061825,-5.045475,-1.421136,2.643082,2.775695,7.751928,-6.750331,7.392843,-9.472340], dtype = "float32")#candidate|13132|(18,)|const|float32
call_13131 = relay.TupleGetItem(func_2726_call(relay.reshape(const_13132.astype('float32'), [1, 3, 6])), 0)
call_13133 = relay.TupleGetItem(func_2729_call(relay.reshape(const_13132.astype('float32'), [1, 3, 6])), 0)
uop_13141 = relay.tan(const_13105.astype('float32')) # shape=(5, 260)
func_11147_call = mod.get_global_var('func_11147')
func_11149_call = mutated_mod.get_global_var('func_11149')
var_13145 = relay.var("var_13145", dtype = "float64", shape = (832,))#candidate|13145|(832,)|var|float64
call_13144 = relay.TupleGetItem(func_11147_call(relay.reshape(var_13145.astype('float64'), [832,])), 3)
call_13146 = relay.TupleGetItem(func_11149_call(relay.reshape(var_13145.astype('float64'), [832,])), 3)
uop_13151 = relay.atan(uop_13141.astype('float32')) # shape=(5, 260)
uop_13154 = relay.sinh(uop_13151.astype('float64')) # shape=(5, 260)
func_3117_call = mod.get_global_var('func_3117')
func_3120_call = mutated_mod.get_global_var('func_3120')
var_13174 = relay.var("var_13174", dtype = "float64", shape = (480,))#candidate|13174|(480,)|var|float64
call_13173 = relay.TupleGetItem(func_3117_call(relay.reshape(var_13174.astype('float64'), [4, 12, 10])), 0)
call_13175 = relay.TupleGetItem(func_3120_call(relay.reshape(var_13174.astype('float64'), [4, 12, 10])), 0)
bop_13208 = relay.floor_mod(uop_13154.astype('float64'), relay.reshape(uop_13141.astype('float64'), relay.shape_of(uop_13154))) # shape=(5, 260)
func_12669_call = mod.get_global_var('func_12669')
func_12670_call = mutated_mod.get_global_var('func_12670')
call_13215 = func_12669_call()
call_13216 = func_12669_call()
uop_13217 = relay.log2(bop_13208.astype('float64')) # shape=(5, 260)
output = relay.Tuple([call_13098,call_13103,var_13104,call_13131,const_13132,call_13144,var_13145,call_13173,var_13174,call_13215,uop_13217,])
output2 = relay.Tuple([call_13099,call_13106,var_13104,call_13133,const_13132,call_13146,var_13145,call_13175,var_13174,call_13216,uop_13217,])
func_13220 = relay.Function([var_13104,var_13145,var_13174,], output)
mod['func_13220'] = func_13220
mod = relay.transform.InferType()(mod)
mutated_mod['func_13220'] = func_13220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13220_call = mutated_mod.get_global_var('func_13220')
var_13222 = relay.var("var_13222", dtype = "float64", shape = (30,))#candidate|13222|(30,)|var|float64
var_13223 = relay.var("var_13223", dtype = "float64", shape = (832,))#candidate|13223|(832,)|var|float64
var_13224 = relay.var("var_13224", dtype = "float64", shape = (480,))#candidate|13224|(480,)|var|float64
call_13221 = func_13220_call(var_13222,var_13223,var_13224,)
output = call_13221
func_13225 = relay.Function([var_13222,var_13223,var_13224,], output)
mutated_mod['func_13225'] = func_13225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11459_call = mod.get_global_var('func_11459')
func_11460_call = mutated_mod.get_global_var('func_11460')
call_13307 = relay.TupleGetItem(func_11459_call(), 0)
call_13308 = relay.TupleGetItem(func_11460_call(), 0)
func_11534_call = mod.get_global_var('func_11534')
func_11538_call = mutated_mod.get_global_var('func_11538')
const_13332 = relay.const([6.825061,-8.272569,4.706123,-2.990176,6.598793,2.962870,8.962147,7.478997,-2.116887,4.082976,6.625053,-4.132664,8.381368,5.463266,-8.928033,5.205691,9.523595,-7.629250,-8.213559,9.344445,-2.237507,-7.800502,-1.042761,-5.548210,1.098668,6.879328,5.944647,-9.499181,0.158644,-0.915138,-1.239387,2.603071,0.522817,3.162454,7.249850,-4.943528,7.129667,5.130495,-7.864654,4.390772,-2.102266,-0.723670,-8.430040,-9.978465,-5.827390,4.865106,-5.258820,9.654714,-4.725969,6.269203,4.097743,-2.576635,-6.248442,-3.789105,2.965804,-0.139595,-1.493327,8.524382,5.405706,-4.085015,-4.696552,9.865162,1.591896,6.194866,1.373554,1.804315,-9.459533,5.172167,1.840093,4.311948,5.616125,-8.682239,-5.069798,3.314813,-7.059059,-5.458172,7.292728,9.335669,-8.610253,2.377181,-2.453080,-1.704868,-2.552204,4.344528,0.664748,-6.874961,2.145723,5.503285,-8.631944,4.328934,-9.886635,-9.622302,0.503506,-1.003229,-0.871123,6.997373,-0.856330,4.395544,-1.019249,2.698860,9.934727,-7.532899,-6.293950,-4.641446,-9.295629,9.538307,4.210880,0.776214,-8.185859,-2.311612,9.388422,7.469693,4.884445,-1.344481,7.392642,-3.136806,3.535321,4.356862,-0.730934,-6.681852,-6.536923,7.126931,9.859430,-0.218643,3.529532,-7.075211,5.934477,-2.509163,-2.725315,-5.889244,-4.965447,-9.481709,6.030097,-6.950339,-1.918346,7.274998,-5.271174,-1.982805,3.102008,0.625501,-2.342716,4.514783,0.702346,-0.794410,-2.949660,-6.897676,8.633004,-3.476801,-6.050276,-1.128827,8.219770,7.745174,5.354571,-4.859380,9.231670,6.955169,5.755655,7.388493,-7.443802,0.923316,-1.863072,-4.944908,-8.997723,-8.099779,9.552073,7.411566,-4.474698,-0.175942,5.805893,-2.590966,2.937675,-4.778473,-7.203399,3.441434,3.938365,4.120148,-1.201715,-0.638107,-2.685114,-8.517079,5.879539,8.327668,-3.205934,3.019343,-3.633320,-2.931165,4.558392,-3.296081,-6.951833,4.760394,-4.273776,3.063749,-8.671604,-1.908951,8.662126,-2.799428,-8.590952,-5.438909,5.300239,-3.923499,-7.385998,2.729951,1.980754,1.898204,-7.969080,-6.342671,-7.550036,3.513876,4.962290,0.646680,-2.781880,4.005377,9.215294,-8.161251,-1.966386,-8.596178,1.479092,-7.411211,-2.065364,3.670930,-9.124262,0.709595,8.630219,3.586419,-5.254662,5.820775,-2.870667,-2.755667,8.410335,0.201881,8.211150,-5.760934,8.173130,-5.929759,-6.927494,-7.570007,8.658961,6.268112,8.384490,3.475122,-9.632976,-6.463756,5.550062,-4.445016,3.782775,-8.318976,-1.123878,-6.186484,-9.045294,7.959380,-4.814851,0.699011,7.635957,-0.041655,-3.622416,6.373578,6.225999,4.709932,-7.028281,0.435593,2.090523,-1.829830,-3.140355,-8.333108,9.754991,3.707228,5.588046,9.938624,-2.989833,0.958546,6.070921,7.388168,6.477316,-6.133203,-8.115849,8.921599,4.379817,2.215876,-3.828303,-0.493250,4.375103,1.374627,7.936722,-9.324016,1.447566,-0.652786,-0.993233,4.104442,-2.621746,3.232177,7.550947,8.979110,-3.542689,-9.682005,-9.948436,1.525796,-9.063831,-8.552472,4.718211,2.212894,5.096025,-6.209682,6.159571,4.300235,0.102197,3.508311,4.769162,0.521928,0.837495,8.873839,6.098495,-1.054406,9.414667,5.003246,2.621863,0.729420,-0.407622,-8.800918,7.387831,6.329045,-0.430498,2.598596,7.339801,1.996276,-5.615010,-1.691795,9.622430,-4.314760,-1.913969,-1.364622,-6.803611,-5.671559,0.834018,1.033525,-0.692720,6.000877,2.783589,-2.487682,1.208367,5.537089,-2.606090,7.610728,-6.237442,5.619814,1.064733,-3.930709,8.485494,-3.044241,9.980362,-3.821809,0.447233,-0.731627,-2.637497,9.047016,8.903067,-7.131586,5.790479,1.396135,4.472379,-0.937305,-8.758798,-2.204809,8.782333,-6.825699,-4.148068,-7.805710,-4.232180,-5.670724,6.794504,1.530774,9.790147,4.724518,1.586579,-2.744900,4.951606,-9.899946,-4.377081,1.799870,8.228930,-8.660244,-9.068154,0.601424,-2.320437,-7.191575,-2.822892,-5.593869,4.502331,-4.675978,-9.440626,0.394864,9.340574,-4.115621,-4.249306,0.137954,0.076286,-0.330955,-6.958908,5.866024,0.488777,-4.511159,7.349954,4.790419,-5.470721,5.559950,2.339953,-7.183120,-9.894267,-4.774907,6.213692,2.557229,1.989206,-9.647148,7.225080,-3.874020,4.140256,-6.816172,0.711190,1.936474,6.004379,2.073357,4.600345,5.039205,-1.988887,4.159975,6.136064,-3.201207,-9.653860,-6.985685,-3.579583,-1.710944,-3.596173,-4.749274,9.880642,6.949607,7.496938,8.677036,4.194920,-9.062455,-0.968306,1.865200,-2.670116,-6.813180,-2.135169,3.120475,-5.834196,8.503561,-3.140978,-1.791367,7.559940,1.794651,-9.558462,-8.824913,6.841434,0.708817,-7.539416,-2.860252,9.000874,6.949774,5.988637,-8.205289,-4.350990,-6.814008,-0.414036,-0.937546,5.329251,-7.566097,-1.389590,4.697434,5.976976,7.280468,4.550531,4.630619,4.597686,-2.795960,1.698225,-5.387441,-5.280158,-6.250483,6.891092,6.246963], dtype = "float64")#candidate|13332|(480,)|const|float64
var_13333 = relay.var("var_13333", dtype = "float64", shape = (1008,))#candidate|13333|(1008,)|var|float64
var_13334 = relay.var("var_13334", dtype = "uint64", shape = (160,))#candidate|13334|(160,)|var|uint64
call_13331 = relay.TupleGetItem(func_11534_call(relay.reshape(const_13332.astype('float64'), [480,]), relay.reshape(var_13333.astype('float64'), [4, 252]), relay.reshape(var_13334.astype('uint64'), [160, 1]), ), 0)
call_13335 = relay.TupleGetItem(func_11538_call(relay.reshape(const_13332.astype('float64'), [480,]), relay.reshape(var_13333.astype('float64'), [4, 252]), relay.reshape(var_13334.astype('uint64'), [160, 1]), ), 0)
output = relay.Tuple([call_13307,call_13331,const_13332,var_13333,var_13334,])
output2 = relay.Tuple([call_13308,call_13335,const_13332,var_13333,var_13334,])
func_13349 = relay.Function([var_13333,var_13334,], output)
mod['func_13349'] = func_13349
mod = relay.transform.InferType()(mod)
mutated_mod['func_13349'] = func_13349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13349_call = mutated_mod.get_global_var('func_13349')
var_13351 = relay.var("var_13351", dtype = "float64", shape = (1008,))#candidate|13351|(1008,)|var|float64
var_13352 = relay.var("var_13352", dtype = "uint64", shape = (160,))#candidate|13352|(160,)|var|uint64
call_13350 = func_13349_call(var_13351,var_13352,)
output = call_13350
func_13353 = relay.Function([var_13351,var_13352,], output)
mutated_mod['func_13353'] = func_13353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11751_call = mod.get_global_var('func_11751')
func_11753_call = mutated_mod.get_global_var('func_11753')
call_13369 = relay.TupleGetItem(func_11751_call(), 0)
call_13370 = relay.TupleGetItem(func_11753_call(), 0)
func_2726_call = mod.get_global_var('func_2726')
func_2729_call = mutated_mod.get_global_var('func_2729')
const_13379 = relay.const([-7.066111,-5.207191,7.393756,5.710005,-4.655967,-1.960099,-4.193035,8.390298,2.914803,1.349214,5.055367,1.947922,-3.528374,-5.560375,3.317225,8.646398,5.556491,8.586778], dtype = "float32")#candidate|13379|(18,)|const|float32
call_13378 = relay.TupleGetItem(func_2726_call(relay.reshape(const_13379.astype('float32'), [1, 3, 6])), 0)
call_13380 = relay.TupleGetItem(func_2729_call(relay.reshape(const_13379.astype('float32'), [1, 3, 6])), 0)
func_11979_call = mod.get_global_var('func_11979')
func_11980_call = mutated_mod.get_global_var('func_11980')
call_13381 = func_11979_call()
call_13382 = func_11979_call()
func_12653_call = mod.get_global_var('func_12653')
func_12655_call = mutated_mod.get_global_var('func_12655')
call_13393 = func_12653_call()
call_13394 = func_12653_call()
func_12065_call = mod.get_global_var('func_12065')
func_12067_call = mutated_mod.get_global_var('func_12067')
call_13399 = relay.TupleGetItem(func_12065_call(), 0)
call_13400 = relay.TupleGetItem(func_12067_call(), 0)
output = relay.Tuple([call_13369,call_13378,const_13379,call_13381,call_13393,call_13399,])
output2 = relay.Tuple([call_13370,call_13380,const_13379,call_13382,call_13394,call_13400,])
func_13402 = relay.Function([], output)
mod['func_13402'] = func_13402
mod = relay.transform.InferType()(mod)
mutated_mod['func_13402'] = func_13402
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13402_call = mutated_mod.get_global_var('func_13402')
call_13403 = func_13402_call()
output = call_13403
func_13404 = relay.Function([], output)
mutated_mod['func_13404'] = func_13404
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12065_call = mod.get_global_var('func_12065')
func_12067_call = mutated_mod.get_global_var('func_12067')
call_13416 = relay.TupleGetItem(func_12065_call(), 0)
call_13417 = relay.TupleGetItem(func_12067_call(), 0)
func_3395_call = mod.get_global_var('func_3395')
func_3398_call = mutated_mod.get_global_var('func_3398')
const_13430 = relay.const([6.313610,-9.071390,-4.928422,-8.079986,4.878917,-9.089281,-7.352942,-9.926092,7.815632,9.530567,-7.907618,-0.629287,-0.717676,-0.996385,4.018455,6.020419,-3.149528,7.800954,8.898045,-9.925404,-4.023271,5.085644,7.706036,5.248909,-7.744714,-4.605234,4.452373,5.637686,6.570784,6.591299,-0.994148,-9.840086,-1.177905,8.371417,5.273573,2.661589,0.424857,-8.044698,-1.232206,4.186059,7.751342,6.945529,-0.041093,-1.992269,2.156572,-5.298312,-4.269806,-3.615647,-5.190545,1.122496,1.952220,3.207131,0.655626,-9.008070,6.688192,-3.926280,4.666083,-6.485769,-7.594009,-7.302629,-9.734647,8.282253,5.929516,-4.371158,-1.523136,1.016418,-3.412507,-2.107949,7.410694,5.928631,-9.040908,3.058867,1.268112,0.373291,-4.572627,7.717899,9.185467,-2.964877,2.773538,-7.070173,-0.854625,6.892012,4.768227,-4.338172,-0.563502,2.474909,8.622390,3.233353,-9.034602,-6.425721,-2.593054,-9.888817,-8.557220,-9.123816,3.757770,1.539246,-8.719447,-8.533238,-1.298668,-7.939878,-3.784994,7.238793,-8.427245,-5.194681,-0.677202,-7.298503,1.582431,-2.151366,6.995028,0.592140,8.997784,-2.349183,2.828408,8.090785,0.242215,1.809341,-4.813613,3.050868,0.631896,5.776321,-8.690495,-7.615909,-2.761162,0.801395,7.927819,-0.742258,-8.590447,-7.786922,1.166250,2.063965,-0.421663,-3.615273,-3.971735,2.942725,-5.381274,8.128437,-2.670755,-1.762622,-2.573837,-6.024967,-6.928203,-4.240204,8.945795,-1.786599,8.267562,3.892074,-5.095534,-1.287198,4.204956,-2.352683,-2.450035,-2.811395,6.313729,-9.240714,4.907795,5.422521,8.524261,-2.373725,6.590719,-0.196427,-4.293846,-5.340370,6.763619,6.885941,-8.007957,-9.397525,4.811108,-4.041042,9.683083,-9.896327,6.091486,-4.323706,-5.452181,-9.246369,-0.949053,-1.905413,-4.000199,3.472773,1.426707,1.713973,1.504729,-2.073800,-0.620528,0.502271,0.128686,-3.082042,-7.167117,-4.874591,1.738892,-2.812216,2.981348,2.934095,3.855639,0.769789,8.705005,-8.925580,1.361709,-1.603784,3.945859,8.012797,3.322238,-1.948319,9.953781,-1.544393,0.753390,-9.077119,3.754488,-2.320724,-3.479659,7.260585,-3.404991,-5.706039,5.222918,-9.958165,8.654886,5.822682,6.339395,-2.526753,-7.043159,-9.113873,6.729172,-8.446094,-9.733102,4.899914,9.663552,-6.564737,-1.936209,7.080783,9.776329,5.725323,4.766132,-8.165251,-1.405216,9.705522,8.354353,-4.050160,-4.807175,-7.982422,8.098798,-2.280905,-5.232876,7.961375,6.713337,-7.783530,-2.775821,0.188465,0.862534,-3.784576,-9.205606,-0.555314,6.347865,-6.949730,-5.605600,-8.091232,-9.548050,-9.605788,-8.020222,-3.798004,-8.997553,-9.091119,-5.010974,-6.606636,3.787383,5.032956,5.017780,-4.941658,-1.910462,-7.136523,0.131951,-9.830732,4.613519,-1.861913,-2.849419,-9.322607,-9.217001,7.330618,-3.292145,-8.156528,9.742129,-5.108310,4.638169,5.956976,2.137605,-4.449273,6.742216,2.072018,9.814620,-0.423603,-3.082369,-1.188509,6.639295,1.699761,-6.402477,-5.782669,2.449318,-6.525872,3.529482,-5.399949,6.586135,4.622204,3.822926,-0.647847,-3.698027,3.407407,0.301137,3.951536,1.448707,-8.110548,-3.874240,0.314509,0.186479,5.542808,-7.786972,-1.691663,-9.087030,-3.510714,-9.346402,9.382955,8.172644,2.360630,-4.408287,6.754112,5.581548,2.331769,-7.351196,8.989779,-9.243639,-6.103642,-6.960546,5.798844,-6.077503,-9.730648,-6.762646,-5.542865,-6.755929,-5.060368,-7.067186,5.693719,7.776912,-9.574668,7.455696,-8.652100,-9.454275,-7.410189,1.839048,9.883311,1.296016,-0.419992,3.100474,1.267206,-1.165959,0.981282,-4.722449,-1.257961,2.858237,4.222449,-8.074656,6.978312,4.565111,5.770946,7.585448,-6.123974,-5.838401,-2.370913,9.429717,-0.469807,0.896136,0.984860,-1.887587,4.117213,-0.363164,-4.641115,-5.547332,8.852719,-5.072643,-6.378664,2.152691,-1.510743,2.049051,-8.068421,9.075212,-2.704100,-6.675376,-3.121177,3.078040,-5.239987,-5.801166,-5.375209,-2.102815,-1.945162,-7.051839,-7.218089,-4.273070,-3.892672,4.873077,-7.031739,3.077756,1.449104,-8.859598,-2.842249,-9.356702,9.733347,1.697609,7.435332,8.409153,-1.999524,1.704283,-7.593363,-6.776051,5.571518,5.613984,-6.818411,0.956798,-7.599024,9.756638,1.687326,0.355199,-6.642333,4.453078,7.100063,-1.756718,-2.618064,-5.799498,9.633809,3.598277,6.983871,-0.275055,0.308535,0.537401,-5.892820,-8.399597,-6.512824,-2.537100,9.946175,8.076968,9.596233,-2.717865,6.132245,-0.594098,6.353422,3.037578,-7.690264,-0.126911,6.150926,7.603109,-3.597594,-4.755045,4.322814,-3.927501,-8.645494,8.563321,2.206675,1.458394,8.962570,1.022267,-0.347839,4.744501,-9.735465,-2.773033,3.290861,9.978941,-8.848630,0.250111,9.660118,-2.663977,3.561671,3.772200,7.047068,2.631368,-9.482387,-6.450539,8.086493,0.893690,7.845563,-2.839365,4.322784,2.968049,3.053666,7.103151,-5.577894,-5.673912,-6.157992,-8.640742,-6.143254,-9.218170,-0.108560,3.693056,-8.036887,5.070616,1.501117,-1.911789,-4.159007,-8.384016,-7.132246,-4.918060,5.499748,-8.771741,-6.970993,9.350465,-5.272806,6.565637,-2.322971,1.736642,8.877264,6.603632,-8.627031,4.000693,7.153004,-3.111647,8.084857,-1.743369,8.164345,-2.895955,3.059575,-8.987116,7.503201,-3.829177,9.271313,-0.866213,-2.914572,1.589729,-4.394993,1.310112,-0.703435,7.570337,-4.907435,-0.539242,7.960277,2.698252,-7.696800,-5.341119,6.466390,-8.376563,-5.496312,4.851885,-7.761284,9.349656,4.867990,-4.323872,-0.317989,-1.391188,7.526186,-8.999445,1.007572,6.250514,-9.257252,-8.841092,-5.615105,-1.128330,5.374496,7.477114,-9.891818,-1.407347,-1.844706,9.308121,1.380743,0.028857,-6.968444,5.504401,-5.049136,8.371643,-4.366859,-1.529809,-5.324444,-9.687807,3.034077,2.682119,-0.093479,2.909620,-0.813282,-5.884137,-1.300466,-8.674221,2.571431,1.663023,-1.886182,-2.929581,-0.614054,0.613337,5.262622,-4.108175,-7.575984,-0.913255,-4.795586,4.522801,-5.713081,-8.454008,9.353565,2.521823,-8.837794,-3.943579,-1.325456,9.700973,-4.443716,2.880481,-4.406312,-9.382745,-2.513922,-7.962795,-2.828773,9.137637,1.985041,-2.384282,9.771003,6.234511,-8.903837,-3.658328,0.928495,6.410722,9.965495,3.990776,-4.017015,-8.957353,2.503495,8.003253,-4.579667,-2.810321,-3.081898,-7.676448,4.432399,5.103023,-9.085026,-7.334709,-8.645569,2.570420,-7.941599,8.137311,-4.134972,1.062718,-4.385409,3.838399,-3.903828,-1.444470,-4.562292,-7.175394,7.995805,1.848054,8.050244,0.995232,6.976887,3.534386,7.330911,2.213225,-3.083787,3.027973,2.185415,2.819927,5.895873,1.082626,5.785885,0.784406,4.320188,-7.758151,-2.857106,-9.960049,-9.588532,9.048498,5.428430,6.145147,-1.279194,-9.222956,9.062400,6.657609,-7.583090,4.267756,-2.052409,-6.898370,3.702972,-6.353825,-0.896257,-1.100903,1.484556,-4.971751,-6.995134,-4.874125,5.422944,-3.499696,0.468130,3.487926,-2.386975,1.989520,3.134531,9.730562,-8.236659,-0.830381,-4.026449,0.765110,-8.266163,-1.025929,0.836043,8.539962,-6.700847,9.398736,1.812047,7.424202,6.119915,-3.600267,-2.904440,-9.410161,-6.029647,3.088699,9.079671,-9.295055,-8.907061,-3.923458,7.393049,-6.757751,0.310625,7.450322,-0.093574,0.654599,9.868280,-9.300739,3.107974,-1.998005,8.655362,-1.218306,-2.269397,7.048184,-4.389144,-8.999303,6.688725,7.719624,0.435516,-4.864155,6.168847,5.965674,7.678127,-4.460955,-3.624189,-8.891847,-4.010928,-5.717460,2.334090,2.155810,8.401225,-5.011345,1.506235,-0.545618,-4.871468,-7.538929,-8.631054,3.808225,-1.658305,-0.821460,-2.142688,-9.479178,1.198456,-2.987375,-7.939759,-2.622556,8.358344,4.834918,-1.347072,7.609253,-4.574035,-9.000371,-7.956890,-4.852113,7.699077,9.277745,-9.763906,-0.693343,2.258735,-7.082602,6.017542,6.984918,1.045426,1.976457,-3.444465,7.904718,-0.586002,6.289020,1.813225,4.888962,-3.773409,-1.878539,0.526371,7.271715,3.996043,-8.619738,-0.419745,-8.166480,-6.013755,-9.416416,-7.182811,5.117467,6.373059,8.064064,2.044801,-6.381835,-4.136555,-3.011933,4.101186,-0.041398,7.478819,4.968036,-6.434630,-1.437022,1.718282,-9.323629,-9.684068,2.875840,-1.194249,-0.430137,6.512576,-4.925069,6.457516,1.647291,-7.406770,-1.370988,3.927095,8.719182,8.979249,-5.980181,-5.318419,-4.865886,4.740341,5.238103,9.761327,1.639196,-1.351369,-3.978243,-8.460108,-5.880932,9.695187,-2.601047,1.633120,-2.525748,4.513720,5.852927,6.459058,-2.096409,7.447894,3.277723,5.377135,-8.697129,-6.660602,-2.701745,-6.269446,3.365304,9.562779,-8.411672,4.716941,3.937313,-0.038037,1.933754,-0.386292,-9.437258,1.416156,-6.147289,-6.963714,-2.769175,8.144190,1.826103,1.242978,5.089788,-7.813116,8.054992,1.049282,6.485660,-0.626817,9.053396,-3.674568,-6.087831,7.424778,9.606513,0.863006,-2.602030,-3.107867,1.963913,-9.383131,-2.966495,-4.856875,6.565935,-7.984988,4.602002,1.263144,5.318566,-2.100545,5.365337,0.684208,5.593553,-5.472868,7.042307,0.531454,-8.262397,-1.629079,3.891705,9.663236,-2.430869,6.799212,-0.016133,-1.425920,-6.842976,3.954012,1.488436,-0.609795,-4.854442,-6.842617,2.837266,-5.907746,-6.353001,-0.069746,7.804928,-3.125772,0.109738,-6.172041,-3.076228,-5.970451,5.982322,-6.233004,-7.005670,-3.143227,6.326071,-7.804156,-8.176000,-7.571110,9.004804,-0.757847,-1.772319,-5.119366,-7.305315,0.247487,-3.758803,-1.571831,-8.018333,-3.764738,8.252615,0.806950,2.103221,-1.808331,-5.903711,-7.944058,9.394967,-3.943878,1.840560,-2.585161,5.353464,-3.645664,8.079985,-0.783421,0.874389,-8.558387,6.233160,0.472759,1.633903,-7.715445,9.911985,-8.230160,-6.391178,-6.354016,2.142832,5.854085,4.239276,-4.605533,-9.473559,-4.679603,9.486810,0.170790,-4.191184,-3.726854,-7.071710,3.655458,4.013886,-4.633888,-7.534511,-7.302409,6.861093,2.365310,8.319902,7.748811,-1.979684,-4.496457,-1.835174,-2.833649,-0.569838,9.968111,1.267079,-1.898981,-0.448011,-9.407065,-9.718675,-4.472804,0.598648,-6.548848,-4.731204,-1.140799,6.351533,-9.822799,-4.476679,-0.596269,8.462239,6.130084,-4.148700,-2.761401,1.925139,0.098219,0.319447,4.897476,3.833216,2.369335,-3.962568,-4.904031,-3.698485,0.831037,3.490731,-5.007562], dtype = "float64")#candidate|13430|(1008,)|const|float64
call_13429 = relay.TupleGetItem(func_3395_call(relay.reshape(const_13430.astype('float64'), [9, 8, 14]), relay.reshape(const_13430.astype('float64'), [9, 8, 14]), ), 0)
call_13431 = relay.TupleGetItem(func_3398_call(relay.reshape(const_13430.astype('float64'), [9, 8, 14]), relay.reshape(const_13430.astype('float64'), [9, 8, 14]), ), 0)
output = relay.Tuple([call_13416,call_13429,const_13430,])
output2 = relay.Tuple([call_13417,call_13431,const_13430,])
func_13432 = relay.Function([], output)
mod['func_13432'] = func_13432
mod = relay.transform.InferType()(mod)
mutated_mod['func_13432'] = func_13432
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13432_call = mutated_mod.get_global_var('func_13432')
call_13433 = func_13432_call()
output = call_13433
func_13434 = relay.Function([], output)
mutated_mod['func_13434'] = func_13434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12653_call = mod.get_global_var('func_12653')
func_12655_call = mutated_mod.get_global_var('func_12655')
call_13435 = func_12653_call()
call_13436 = func_12653_call()
func_9478_call = mod.get_global_var('func_9478')
func_9481_call = mutated_mod.get_global_var('func_9481')
var_13460 = relay.var("var_13460", dtype = "float64", shape = (432,))#candidate|13460|(432,)|var|float64
call_13459 = relay.TupleGetItem(func_9478_call(relay.reshape(var_13460.astype('float64'), [6, 9, 8])), 0)
call_13461 = relay.TupleGetItem(func_9481_call(relay.reshape(var_13460.astype('float64'), [6, 9, 8])), 0)
func_11459_call = mod.get_global_var('func_11459')
func_11460_call = mutated_mod.get_global_var('func_11460')
call_13502 = relay.TupleGetItem(func_11459_call(), 0)
call_13503 = relay.TupleGetItem(func_11460_call(), 0)
output = relay.Tuple([call_13435,call_13459,var_13460,call_13502,])
output2 = relay.Tuple([call_13436,call_13461,var_13460,call_13503,])
func_13516 = relay.Function([var_13460,], output)
mod['func_13516'] = func_13516
mod = relay.transform.InferType()(mod)
var_13517 = relay.var("var_13517", dtype = "float64", shape = (432,))#candidate|13517|(432,)|var|float64
output = func_13516(var_13517)
func_13518 = relay.Function([var_13517], output)
mutated_mod['func_13518'] = func_13518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12065_call = mod.get_global_var('func_12065')
func_12067_call = mutated_mod.get_global_var('func_12067')
call_13546 = relay.TupleGetItem(func_12065_call(), 0)
call_13547 = relay.TupleGetItem(func_12067_call(), 0)
func_7792_call = mod.get_global_var('func_7792')
func_7796_call = mutated_mod.get_global_var('func_7796')
var_13571 = relay.var("var_13571", dtype = "float64", shape = (264,))#candidate|13571|(264,)|var|float64
var_13572 = relay.var("var_13572", dtype = "float32", shape = (50, 15))#candidate|13572|(50, 15)|var|float32
call_13570 = relay.TupleGetItem(func_7792_call(relay.reshape(var_13571.astype('float64'), [6, 4, 11]), relay.reshape(var_13572.astype('float32'), [1, 750]), ), 0)
call_13573 = relay.TupleGetItem(func_7796_call(relay.reshape(var_13571.astype('float64'), [6, 4, 11]), relay.reshape(var_13572.astype('float32'), [1, 750]), ), 0)
func_12065_call = mod.get_global_var('func_12065')
func_12067_call = mutated_mod.get_global_var('func_12067')
call_13580 = relay.TupleGetItem(func_12065_call(), 0)
call_13581 = relay.TupleGetItem(func_12067_call(), 0)
func_12617_call = mod.get_global_var('func_12617')
func_12619_call = mutated_mod.get_global_var('func_12619')
call_13584 = func_12617_call()
call_13585 = func_12617_call()
output = relay.Tuple([call_13546,call_13570,var_13571,var_13572,call_13580,call_13584,])
output2 = relay.Tuple([call_13547,call_13573,var_13571,var_13572,call_13581,call_13585,])
func_13592 = relay.Function([var_13571,var_13572,], output)
mod['func_13592'] = func_13592
mod = relay.transform.InferType()(mod)
mutated_mod['func_13592'] = func_13592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13592_call = mutated_mod.get_global_var('func_13592')
var_13594 = relay.var("var_13594", dtype = "float64", shape = (264,))#candidate|13594|(264,)|var|float64
var_13595 = relay.var("var_13595", dtype = "float32", shape = (50, 15))#candidate|13595|(50, 15)|var|float32
call_13593 = func_13592_call(var_13594,var_13595,)
output = call_13593
func_13596 = relay.Function([var_13594,var_13595,], output)
mutated_mod['func_13596'] = func_13596
mutated_mod = relay.transform.InferType()(mutated_mod)
const_13598 = relay.const([[[4.091957,9.184206,2.010578,-4.806675,2.331313,-0.192236,-8.688057,-6.796841,-0.466839],[-1.418576,8.530394,-3.763650,-6.160893,0.852899,0.784008,-8.029914,-2.896193,3.099410],[3.674749,-9.473021,3.010516,3.393103,-9.503726,7.200944,3.876126,-5.334621,8.223868],[2.674347,-3.451115,0.451421,6.084535,-7.842104,-7.153236,2.795424,9.000990,-8.982117],[-3.125995,6.413280,1.000069,1.064610,-7.394771,6.853270,-0.299558,2.034832,8.309482],[-0.791715,-6.196105,-6.978083,-4.075522,-8.004251,8.634836,4.537753,-6.022571,-8.536214],[9.131859,-3.731930,-2.619075,5.694817,-9.537147,5.536075,-8.219151,-8.712179,-6.273495],[3.697387,3.783531,7.283562,-6.144466,-6.316273,5.235720,-3.764152,9.871448,-4.509621],[8.440568,-9.915392,-5.117598,8.673557,-9.630131,5.555222,5.344206,3.969888,-5.003341],[1.423588,6.243486,-8.297116,4.476565,-9.659465,3.999857,-6.928693,-2.302822,4.053358],[-9.125217,1.565554,-6.945135,9.648170,1.909504,-0.386098,2.634502,-1.770878,-2.394258],[0.090937,-6.906045,-8.834408,-2.768421,-3.759332,5.172797,9.654853,-3.265701,-4.982057]]], dtype = "float64")#candidate|13598|(1, 12, 9)|const|float64
uop_13599 = relay.acos(const_13598.astype('float64')) # shape=(1, 12, 9)
func_9478_call = mod.get_global_var('func_9478')
func_9481_call = mutated_mod.get_global_var('func_9481')
var_13604 = relay.var("var_13604", dtype = "float64", shape = (4, 108))#candidate|13604|(4, 108)|var|float64
call_13603 = relay.TupleGetItem(func_9478_call(relay.reshape(var_13604.astype('float64'), [6, 9, 8])), 0)
call_13605 = relay.TupleGetItem(func_9481_call(relay.reshape(var_13604.astype('float64'), [6, 9, 8])), 0)
func_13592_call = mod.get_global_var('func_13592')
func_13596_call = mutated_mod.get_global_var('func_13596')
var_13621 = relay.var("var_13621", dtype = "float64", shape = (264,))#candidate|13621|(264,)|var|float64
var_13622 = relay.var("var_13622", dtype = "float32", shape = (750,))#candidate|13622|(750,)|var|float32
call_13620 = relay.TupleGetItem(func_13592_call(relay.reshape(var_13621.astype('float64'), [264,]), relay.reshape(var_13622.astype('float32'), [50, 15]), ), 2)
call_13623 = relay.TupleGetItem(func_13596_call(relay.reshape(var_13621.astype('float64'), [264,]), relay.reshape(var_13622.astype('float32'), [50, 15]), ), 2)
output = relay.Tuple([uop_13599,call_13603,var_13604,call_13620,var_13621,var_13622,])
output2 = relay.Tuple([uop_13599,call_13605,var_13604,call_13623,var_13621,var_13622,])
func_13629 = relay.Function([var_13604,var_13621,var_13622,], output)
mod['func_13629'] = func_13629
mod = relay.transform.InferType()(mod)
var_13630 = relay.var("var_13630", dtype = "float64", shape = (4, 108))#candidate|13630|(4, 108)|var|float64
var_13631 = relay.var("var_13631", dtype = "float64", shape = (264,))#candidate|13631|(264,)|var|float64
var_13632 = relay.var("var_13632", dtype = "float32", shape = (750,))#candidate|13632|(750,)|var|float32
output = func_13629(var_13630,var_13631,var_13632,)
func_13633 = relay.Function([var_13630,var_13631,var_13632,], output)
mutated_mod['func_13633'] = func_13633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12065_call = mod.get_global_var('func_12065')
func_12067_call = mutated_mod.get_global_var('func_12067')
call_13695 = relay.TupleGetItem(func_12065_call(), 0)
call_13696 = relay.TupleGetItem(func_12067_call(), 0)
output = relay.Tuple([call_13695,])
output2 = relay.Tuple([call_13696,])
func_13697 = relay.Function([], output)
mod['func_13697'] = func_13697
mod = relay.transform.InferType()(mod)
mutated_mod['func_13697'] = func_13697
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13697_call = mutated_mod.get_global_var('func_13697')
call_13698 = func_13697_call()
output = call_13698
func_13699 = relay.Function([], output)
mutated_mod['func_13699'] = func_13699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11804_call = mod.get_global_var('func_11804')
func_11806_call = mutated_mod.get_global_var('func_11806')
call_13731 = relay.TupleGetItem(func_11804_call(), 0)
call_13732 = relay.TupleGetItem(func_11806_call(), 0)
func_11438_call = mod.get_global_var('func_11438')
func_11441_call = mutated_mod.get_global_var('func_11441')
const_13743 = relay.const([6.283844,2.126126,9.009707,3.747286,3.430253,0.886055,-4.198965,-1.568319,-8.439063,8.384715,1.612717,0.759499,-3.364984,3.629100,-8.581135,3.375083,-0.350909,7.176643,-4.718808,-0.204977,8.675765,7.013313,-3.102043,-7.495681,8.012853,-4.040007,-2.012556,-0.835673,-8.655643,-7.095542,-8.490782,8.575890,-7.904689,-8.999273,1.643108,-2.041882,8.144334,-6.663194,8.788349,-3.660587,-4.867043,-2.322482,-6.966197,4.732739,-3.787248,-7.545553,4.554492,-1.762402,-6.779642,-8.979681,2.013589,0.424890,5.078161,-3.348183,-9.736790,7.984566,-9.366616,7.792634,-6.339047,8.021616,7.062492,-3.247877,3.055770,-6.189452,8.486839,6.618195,-4.066718,9.178010,-1.776030,-9.725358,-1.883758,4.496905,0.902101,-9.586295,-2.688624,2.392609,0.461815,-0.206057,-6.727881,-8.238970,-2.594974,-4.739711,-8.244822,-8.749684,2.018334,7.727710,-4.876651,-9.581343,-9.183366,3.095402,2.898029,-2.487205,-0.055498,8.003865,0.930281,1.192656,-7.205945,-3.922266,7.416353,0.937967,-5.992779,8.288898,-2.614351,-1.521493,-9.213846,6.623020,-7.131607,-2.944232,-6.453859,4.733116,4.584483,3.535328,-2.741984,1.217645,-1.946119,7.540087,5.616007,1.777726,-4.584617,-8.563173,-0.472932,-6.774830,4.021060,5.080652,3.283768,-8.740315,7.291496,-6.949716,7.800451,-7.410304,-2.865961,-8.538744,-3.235032,2.562603,-4.350695,2.344758,7.331112,8.230373,-9.994159,5.202378,-5.945529,-8.854190,5.902439,1.632242,-0.484531,4.855025,0.601969,4.706812,7.720171,5.571343,-0.345365,-9.212841,-9.596424,7.897070,0.608833,-3.621619,-9.471418,5.688161,1.448458,-3.919435,-6.087621,2.184652,-2.511454,7.584847,8.588271,6.199412,2.063990,-4.789210,6.742743,-4.570719,-0.744674,-1.840991,-3.587349,-2.722831,7.327788,8.426565,-3.860102,4.210345,7.803262,7.140382,2.497349,5.252569,-9.373218,6.534634,1.759686,-6.069980,-2.541197,-0.976876,0.794334,6.568326,4.494141,-8.795935,2.252158,-6.765865,7.380010,5.570565,-7.736381,4.063788,-2.299744,2.071819,0.910131,6.489513,-9.101195,-6.124510,3.356332,-8.508395,-7.847190,-8.835273,4.757610,9.287898,-5.224627,7.713343,0.952576,-8.856560,4.693369,9.123438,5.594104,0.283689,-1.842439,4.418431,3.379724,-0.166531,0.698075,9.772034,-3.883985,4.975825,2.025992,3.900433,5.655784,5.856144,0.397546,8.062556,4.619606,6.223591,-8.503800,3.453382,-8.039085,-1.374876,3.587655,-5.716314,-1.680595,-9.007240,5.510621,-2.437637,5.346341,8.890273,-3.366749,-1.028096,3.176408,3.688081,-7.417867,9.526426,-9.835480,-5.494193,4.645747,4.109486,-3.002540,-5.559413,-0.944974,8.834859,-7.559322,-5.881334,5.476177,-4.017435,-1.767075,9.794747,3.429694,-8.821207,-8.297092,2.704869,8.024475,5.809635,-7.225733,0.163074,-1.615342,5.157447,-2.146828,2.876814,-4.730027,-8.522815,9.144521,1.848728,1.422961,-5.176252,6.018594,1.479472,8.297009,-6.445281,-9.060028,-2.112024,-0.369904,5.953112,3.014657,1.533082,6.499777,0.622218,2.160955,4.111494,-6.158055,-0.261160,1.197564,-2.410593,-8.443908,-2.767555,8.948971,5.490661,-1.827957,-5.994743,0.307749,6.576605,9.663792,9.023757,-6.533294,4.831925,-1.854560,-8.998959,-0.412943,-1.601366,9.643319,8.407779], dtype = "float64")#candidate|13743|(320,)|const|float64
call_13742 = relay.TupleGetItem(func_11438_call(relay.reshape(const_13743.astype('float64'), [320,])), 1)
call_13744 = relay.TupleGetItem(func_11441_call(relay.reshape(const_13743.astype('float64'), [320,])), 1)
var_13757 = relay.var("var_13757", dtype = "float64", shape = (8, 5, 8))#candidate|13757|(8, 5, 8)|var|float64
bop_13758 = relay.greater_equal(call_13742.astype('bool'), relay.reshape(var_13757.astype('bool'), relay.shape_of(call_13742))) # shape=(8, 5, 8)
bop_13761 = relay.greater_equal(call_13744.astype('bool'), relay.reshape(var_13757.astype('bool'), relay.shape_of(call_13744))) # shape=(8, 5, 8)
func_12848_call = mod.get_global_var('func_12848')
func_12850_call = mutated_mod.get_global_var('func_12850')
call_13776 = func_12848_call()
call_13777 = func_12848_call()
output = relay.Tuple([call_13731,const_13743,bop_13758,call_13776,])
output2 = relay.Tuple([call_13732,const_13743,bop_13761,call_13777,])
func_13782 = relay.Function([var_13757,], output)
mod['func_13782'] = func_13782
mod = relay.transform.InferType()(mod)
mutated_mod['func_13782'] = func_13782
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13783 = relay.var("var_13783", dtype = "float64", shape = (8, 5, 8))#candidate|13783|(8, 5, 8)|var|float64
func_13782_call = mutated_mod.get_global_var('func_13782')
call_13784 = func_13782_call(var_13783)
output = call_13784
func_13785 = relay.Function([var_13783], output)
mutated_mod['func_13785'] = func_13785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12617_call = mod.get_global_var('func_12617')
func_12619_call = mutated_mod.get_global_var('func_12619')
call_13843 = func_12617_call()
call_13844 = func_12617_call()
output = call_13843
output2 = call_13844
func_13858 = relay.Function([], output)
mod['func_13858'] = func_13858
mod = relay.transform.InferType()(mod)
output = func_13858()
func_13859 = relay.Function([], output)
mutated_mod['func_13859'] = func_13859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12617_call = mod.get_global_var('func_12617')
func_12619_call = mutated_mod.get_global_var('func_12619')
call_13874 = func_12617_call()
call_13875 = func_12617_call()
output = call_13874
output2 = call_13875
func_13876 = relay.Function([], output)
mod['func_13876'] = func_13876
mod = relay.transform.InferType()(mod)
mutated_mod['func_13876'] = func_13876
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13876_call = mutated_mod.get_global_var('func_13876')
call_13877 = func_13876_call()
output = call_13877
func_13878 = relay.Function([], output)
mutated_mod['func_13878'] = func_13878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12653_call = mod.get_global_var('func_12653')
func_12655_call = mutated_mod.get_global_var('func_12655')
call_13995 = func_12653_call()
call_13996 = func_12653_call()
func_12223_call = mod.get_global_var('func_12223')
func_12228_call = mutated_mod.get_global_var('func_12228')
const_14017 = relay.const([9,-2,-5,-8,10,10,-5,9,-3,-9,-10,-10,2,-9,7,2,6,-6,7,-5,-9,-7,2,-4,-10,-1,3,-7,5,1,-8,9,-7,4,-10,10], dtype = "int8")#candidate|14017|(36,)|const|int8
var_14018 = relay.var("var_14018", dtype = "bool", shape = ())#candidate|14018|()|var|bool
var_14019 = relay.var("var_14019", dtype = "float64", shape = (240, 2))#candidate|14019|(240, 2)|var|float64
var_14020 = relay.var("var_14020", dtype = "float32", shape = (18,))#candidate|14020|(18,)|var|float32
call_14016 = relay.TupleGetItem(func_12223_call(relay.reshape(const_14017.astype('int8'), [9, 4, 1]), relay.reshape(var_14018.astype('bool'), []), relay.reshape(var_14019.astype('float64'), [480,]), relay.reshape(var_14020.astype('float32'), [18,]), ), 1)
call_14021 = relay.TupleGetItem(func_12228_call(relay.reshape(const_14017.astype('int8'), [9, 4, 1]), relay.reshape(var_14018.astype('bool'), []), relay.reshape(var_14019.astype('float64'), [480,]), relay.reshape(var_14020.astype('float32'), [18,]), ), 1)
output = relay.Tuple([call_13995,call_14016,const_14017,var_14018,var_14019,var_14020,])
output2 = relay.Tuple([call_13996,call_14021,const_14017,var_14018,var_14019,var_14020,])
func_14050 = relay.Function([var_14018,var_14019,var_14020,], output)
mod['func_14050'] = func_14050
mod = relay.transform.InferType()(mod)
var_14051 = relay.var("var_14051", dtype = "bool", shape = ())#candidate|14051|()|var|bool
var_14052 = relay.var("var_14052", dtype = "float64", shape = (240, 2))#candidate|14052|(240, 2)|var|float64
var_14053 = relay.var("var_14053", dtype = "float32", shape = (18,))#candidate|14053|(18,)|var|float32
output = func_14050(var_14051,var_14052,var_14053,)
func_14054 = relay.Function([var_14051,var_14052,var_14053,], output)
mutated_mod['func_14054'] = func_14054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11288_call = mod.get_global_var('func_11288')
func_11290_call = mutated_mod.get_global_var('func_11290')
call_14075 = relay.TupleGetItem(func_11288_call(), 0)
call_14076 = relay.TupleGetItem(func_11290_call(), 0)
func_11438_call = mod.get_global_var('func_11438')
func_11441_call = mutated_mod.get_global_var('func_11441')
const_14122 = relay.const([-5.423878,0.901759,7.436598,3.287214,2.892205,-1.520286,-1.247911,-7.200328,-7.920245,-9.757216,-5.051369,-7.087866,-4.670112,4.788433,-8.424815,-7.532205,-2.223890,-4.524789,-1.571654,-2.914657,-3.692614,0.380405,6.105608,0.111641,-0.956287,-0.997228,-9.456331,9.845146,6.096037,-9.031497,2.757514,-7.741415,-2.426609,3.932328,3.928452,-3.596873,6.968888,-0.764451,4.775590,-0.172130,6.490795,-7.512837,5.891892,-4.058464,6.214674,0.664436,-0.857759,-1.106798,-9.389682,0.721371,2.745364,8.411105,2.546844,6.583890,1.582459,-9.352134,-1.482443,-6.868794,3.057765,-5.782716,2.114701,3.004987,-9.429681,2.547844,-1.424513,-8.570100,-4.389402,-6.219586,7.534730,1.719353,2.654193,-7.107369,-5.318633,5.836195,3.931064,-3.333548,9.131832,-3.836137,2.259871,6.868462,-7.556907,0.843509,2.248273,3.828579,3.603126,-3.957656,-2.218486,6.201940,3.857699,-0.039344,-0.674604,-3.473601,6.662131,0.374051,-3.704465,-7.507513,-9.653864,9.257293,9.980411,9.308999,0.295195,4.650463,-9.803444,0.427056,7.222786,-8.102483,-9.531945,-8.013383,-1.579071,6.883175,-7.933229,0.278374,1.689091,-9.181698,6.904013,-8.866735,3.647874,6.700352,-0.958799,-8.157304,-0.217446,6.635866,1.854863,-3.454254,-9.097283,-5.447572,6.634712,8.538767,-0.444929,0.636032,3.695809,9.811227,3.092225,-7.682944,0.044275,-3.687214,-9.266690,-9.345730,3.627449,2.320442,-2.073941,-4.587004,5.828328,4.112140,0.852552,-5.454907,-5.067844,-8.215305,-4.297436,4.454008,7.459225,2.482859,3.249484,9.515941,3.041333,-2.584911,-0.393455,2.111926,4.096488,5.457445,-7.686668,1.154239,8.510082,-6.269668,3.837124,2.252052,8.565631,-0.783698,6.252895,4.746132,-5.500206,-5.172781,-0.938511,-8.113279,-1.918915,2.886109,9.571664,2.046735,-1.053882,-8.515346,6.859264,-4.001338,5.323263,-5.616413,-5.674582,0.993071,4.718485,6.525991,1.369305,8.836372,0.476148,-5.960426,-7.734424,-2.068230,-3.664965,-5.112882,-7.483955,-6.516679,1.495138,-1.586008,2.340404,-3.646463,-1.567436,-2.746883,3.046852,4.708851,-3.357203,-0.430290,-0.543401,4.842022,7.174835,-2.801899,-3.922678,0.802326,2.728520,3.461398,1.213187,-2.379670,2.217589,-1.622878,-6.047747,-6.347603,3.406772,0.100958,5.800236,-4.985731,-0.078745,-4.612934,-9.153659,-2.253588,-2.725717,-2.692588,2.601371,2.585817,3.020120,-5.961936,0.902520,4.615715,8.102422,-9.492753,7.162792,9.682088,-9.921378,8.205799,-5.054510,-8.546220,4.043650,-4.383318,0.427588,-3.292014,1.522121,4.861506,5.888437,-7.777950,6.450567,7.718622,8.347029,2.361232,-3.489446,-7.988919,-5.659919,6.331042,7.148576,9.345969,3.715938,-4.196804,-7.716192,-3.561336,-3.429706,-7.329129,8.903338,-1.242313,-0.457461,-6.405944,-7.418100,1.797077,-9.261820,8.187447,1.273998,-4.183111,-6.701100,2.068359,-4.753552,-5.881185,-9.301605,8.808619,-0.869964,8.754326,9.858757,9.225314,-3.486432,-6.200599,-8.308323,1.204657,-6.148075,-2.814939,-2.704892,2.740750,5.407938,7.957985,-2.820678,-1.690476,-8.109223,-0.003087,3.985901,-0.389206,-4.920755,-8.635784,-3.356979,-5.262363,-3.387897,4.548365,5.329468,8.804899,-5.665908,-9.945081,3.190721,1.853146,-0.275968,5.775441], dtype = "float64")#candidate|14122|(320,)|const|float64
call_14121 = relay.TupleGetItem(func_11438_call(relay.reshape(const_14122.astype('float64'), [320,])), 2)
call_14123 = relay.TupleGetItem(func_11441_call(relay.reshape(const_14122.astype('float64'), [320,])), 2)
output = relay.Tuple([call_14075,call_14121,const_14122,])
output2 = relay.Tuple([call_14076,call_14123,const_14122,])
func_14127 = relay.Function([], output)
mod['func_14127'] = func_14127
mod = relay.transform.InferType()(mod)
mutated_mod['func_14127'] = func_14127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14127_call = mutated_mod.get_global_var('func_14127')
call_14128 = func_14127_call()
output = call_14128
func_14129 = relay.Function([], output)
mutated_mod['func_14129'] = func_14129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12987_call = mod.get_global_var('func_12987')
func_12988_call = mutated_mod.get_global_var('func_12988')
call_14186 = func_12987_call()
call_14187 = func_12987_call()
func_14127_call = mod.get_global_var('func_14127')
func_14129_call = mutated_mod.get_global_var('func_14129')
call_14189 = relay.TupleGetItem(func_14127_call(), 0)
call_14190 = relay.TupleGetItem(func_14129_call(), 0)
func_3117_call = mod.get_global_var('func_3117')
func_3120_call = mutated_mod.get_global_var('func_3120')
var_14194 = relay.var("var_14194", dtype = "float64", shape = (480,))#candidate|14194|(480,)|var|float64
call_14193 = relay.TupleGetItem(func_3117_call(relay.reshape(var_14194.astype('float64'), [4, 12, 10])), 0)
call_14195 = relay.TupleGetItem(func_3120_call(relay.reshape(var_14194.astype('float64'), [4, 12, 10])), 0)
output = relay.Tuple([call_14186,call_14189,call_14193,var_14194,])
output2 = relay.Tuple([call_14187,call_14190,call_14195,var_14194,])
func_14196 = relay.Function([var_14194,], output)
mod['func_14196'] = func_14196
mod = relay.transform.InferType()(mod)
var_14197 = relay.var("var_14197", dtype = "float64", shape = (480,))#candidate|14197|(480,)|var|float64
output = func_14196(var_14197)
func_14198 = relay.Function([var_14197], output)
mutated_mod['func_14198'] = func_14198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11751_call = mod.get_global_var('func_11751')
func_11753_call = mutated_mod.get_global_var('func_11753')
call_14291 = relay.TupleGetItem(func_11751_call(), 0)
call_14292 = relay.TupleGetItem(func_11753_call(), 0)
output = call_14291
output2 = call_14292
func_14297 = relay.Function([], output)
mod['func_14297'] = func_14297
mod = relay.transform.InferType()(mod)
output = func_14297()
func_14298 = relay.Function([], output)
mutated_mod['func_14298'] = func_14298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11751_call = mod.get_global_var('func_11751')
func_11753_call = mutated_mod.get_global_var('func_11753')
call_14302 = relay.TupleGetItem(func_11751_call(), 0)
call_14303 = relay.TupleGetItem(func_11753_call(), 0)
output = call_14302
output2 = call_14303
func_14330 = relay.Function([], output)
mod['func_14330'] = func_14330
mod = relay.transform.InferType()(mod)
mutated_mod['func_14330'] = func_14330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14330_call = mutated_mod.get_global_var('func_14330')
call_14331 = func_14330_call()
output = call_14331
func_14332 = relay.Function([], output)
mutated_mod['func_14332'] = func_14332
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11095_call = mod.get_global_var('func_11095')
func_11096_call = mutated_mod.get_global_var('func_11096')
call_14363 = func_11095_call()
call_14364 = func_11095_call()
output = relay.Tuple([call_14363,])
output2 = relay.Tuple([call_14364,])
func_14375 = relay.Function([], output)
mod['func_14375'] = func_14375
mod = relay.transform.InferType()(mod)
output = func_14375()
func_14376 = relay.Function([], output)
mutated_mod['func_14376'] = func_14376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14297_call = mod.get_global_var('func_14297')
func_14298_call = mutated_mod.get_global_var('func_14298')
call_14407 = func_14297_call()
call_14408 = func_14297_call()
output = relay.Tuple([call_14407,])
output2 = relay.Tuple([call_14408,])
func_14417 = relay.Function([], output)
mod['func_14417'] = func_14417
mod = relay.transform.InferType()(mod)
output = func_14417()
func_14418 = relay.Function([], output)
mutated_mod['func_14418'] = func_14418
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12669_call = mod.get_global_var('func_12669')
func_12670_call = mutated_mod.get_global_var('func_12670')
call_14421 = func_12669_call()
call_14422 = func_12669_call()
output = call_14421
output2 = call_14422
func_14426 = relay.Function([], output)
mod['func_14426'] = func_14426
mod = relay.transform.InferType()(mod)
output = func_14426()
func_14427 = relay.Function([], output)
mutated_mod['func_14427'] = func_14427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12848_call = mod.get_global_var('func_12848')
func_12850_call = mutated_mod.get_global_var('func_12850')
call_14446 = func_12848_call()
call_14447 = func_12848_call()
output = call_14446
output2 = call_14447
func_14457 = relay.Function([], output)
mod['func_14457'] = func_14457
mod = relay.transform.InferType()(mod)
output = func_14457()
func_14458 = relay.Function([], output)
mutated_mod['func_14458'] = func_14458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11288_call = mod.get_global_var('func_11288')
func_11290_call = mutated_mod.get_global_var('func_11290')
call_14565 = relay.TupleGetItem(func_11288_call(), 0)
call_14566 = relay.TupleGetItem(func_11290_call(), 0)
func_11617_call = mod.get_global_var('func_11617')
func_11620_call = mutated_mod.get_global_var('func_11620')
const_14571 = relay.const([True,True,False,False,False,True,True,False,True,False,True,False,True,False,False,False,True,True,True,False,False,True,True,True,False,True,True,True,True,False,True,True,True,False,True,True,True,False,True,False,False,False,False,False,False,False,False,False], dtype = "bool")#candidate|14571|(48,)|const|bool
call_14570 = func_11617_call(relay.reshape(const_14571.astype('bool'), [3, 2, 8]))
call_14572 = func_11617_call(relay.reshape(const_14571.astype('bool'), [3, 2, 8]))
func_7792_call = mod.get_global_var('func_7792')
func_7796_call = mutated_mod.get_global_var('func_7796')
var_14578 = relay.var("var_14578", dtype = "float64", shape = (264,))#candidate|14578|(264,)|var|float64
const_14579 = relay.const([[6.871199,-5.670531,2.549867,-9.907541,-2.539296,-9.538548,-7.167700,-2.812640,-4.102964,-3.847997,7.928219,-4.918608,-0.446118,3.968116,-3.473226,6.033259,0.215563,-8.622662,9.522174,0.081090,2.914149,-5.405430,-8.156055,5.909232,9.962992,1.789401,-5.490968,-5.047625,6.369633,9.271132,-2.971821,0.245836,-8.373325,-1.602448,-7.404916,-3.238653,7.643320,-6.105566,4.194901,-7.284308,2.385124,-1.936995,-0.178158,-5.832448,-9.444416,5.289160,-6.087408,4.279799,-6.630324,-7.411228,7.987932,-4.498340,9.574412,-4.745526,-5.521549,-5.334829,-3.032348,4.840628,7.939595,-0.571491,4.404397,-1.223585,-4.117889,8.440823,5.378908,-6.632045,-1.065833,-6.445513,6.580974,-2.088735,2.932452,6.432342,4.612712,-7.972800,-3.107225,5.586654,7.612671,9.561774,6.136249,-8.781098,-2.757997,8.848625,-5.343629,6.634476,-6.606767,8.648729,-1.301372,8.740307,-0.181106,-5.452936,-2.252120,-7.375835,9.077083,5.594605,-9.549563,9.597924,-2.124259,5.580493,-9.343903,-7.344340,0.982989,5.182711,-8.818904,4.380615,-2.410582,8.608828,7.027474,-9.416085,4.018146,9.174230,-3.823011,5.721794,8.173266,1.493964,5.005600,-6.907045,0.443845,-1.371643,-7.924805,-9.108422,9.688537,9.800540,-7.722566,5.067942,-4.793656,6.971231,1.070964,9.862882,-6.727910,1.357938,5.885424,-0.966862,2.668797,-9.135206,-1.940920,-2.337979,8.708843,4.963698,-2.424024,4.227622,0.918798,6.164496,6.183100,-5.530488,0.081392,6.775307,0.357023,7.399843,-4.130638,5.533176,6.611834,-0.095889,6.899636,-3.554399,-8.130283,-3.538261,-6.883806,6.651443,1.359583,3.434819,9.241254,1.904055,-3.167854,9.277450,-1.167704,-4.679305,-9.156960,-4.846834,-7.877534,8.604097,2.017573,-9.906448,5.115926,9.302082,3.731097,2.010985,-0.771886,-7.294898,-0.985083,9.010292,-1.409268,-8.936346,1.784396,-7.902645,0.559139,-6.581419,-7.616009,-2.385240,-7.332909,-9.023348,6.044363,-9.900682,-0.005037,-3.513415,-7.094259,3.982425,7.234723,-3.692984,0.512249,-3.051771,-7.036258,9.697120,-7.540363,3.811042,5.979526,-9.861588,3.123939,-3.405299,6.773702,-7.731152,4.373610,-1.410887,2.721022,5.730537,-5.299077,7.619511,-4.996478,0.255884,8.801735,-2.526992,-6.023342,8.366537,0.641851,6.307527,-2.123810,8.713602,0.460742,3.936664,-1.260264,4.985211,-4.388732,3.915657,7.279319,2.028744,5.523933,-4.578172,3.995388,-7.177809,9.423578,3.443452,3.614259,3.174367,0.977049,-4.050149,8.455576,-9.296904,-4.642248,9.816289,-0.542080,-2.083415,-6.441519,5.131447,-2.819693,-1.534963,4.946656,-1.215607,-7.757601,6.182355,-2.750859,6.038382,-6.915021,2.484761,-4.221588,-7.431787,-0.224394,-5.608094,9.712317,-3.187727,9.537751,-0.803066,-5.559789,-9.463244,-8.747126,-9.269668,4.552354,1.497714,4.277576,-0.957659,1.609315,-0.482497,-2.216859,-3.006602,-5.579539,0.131356,3.288279,-1.948193,-3.270588,1.373265,9.286809,7.374268,1.156797,-2.241606,-5.259868,-1.285243,7.523699,8.181800,-3.720430,-0.785210,-0.584285,-6.876994,4.931736,8.455766,0.684281,-7.233593,3.816127,3.482208,-8.000846,3.034590,2.213380,-0.058384,2.686509,-0.864885,6.206273,-5.673184,-0.771128,-2.783142,-7.495962,-9.732603,-4.666000,-2.180808,-1.458692,-4.691628,4.127115,8.032280,-9.426651,7.594120,3.935956,3.790138,-3.893724,-7.912827,-9.931091,-2.641681,2.421941,9.732051,-1.551982,6.372619,1.313548,6.221982,3.607894,5.874824,9.318738,5.886850,-0.454215,5.702127,4.186375,-8.174806,-8.501180,-7.753484,3.891711,2.948184,1.238052,-7.723755,1.222772,1.583027,9.070997,-1.897613,5.746853,5.122935,-8.820349,8.267757,7.671165,9.717813,-1.076929,7.494996,9.879556,6.767777,4.971064,-2.392974,-7.795682,0.249589,-6.531995,-1.175129,-0.460748,-1.874388,-1.732944,-2.872522,4.275597,-0.449007,8.416750,2.035955,-4.937142,6.684684,-7.454322,-7.074366,1.912894,-7.323971,3.104186,3.512200,4.697814,-3.802974,3.871145,7.811941,0.180411,2.375090,9.116174,2.831575,7.612889,9.716763,-8.729901,-2.752017,9.597979,-1.607568,8.248245,-6.830983,3.030417,0.558136,4.059245,2.169573,-1.321947,2.339744,2.881655,1.832871,0.376279,-0.853421,6.418376,8.755940,-2.460715,8.280723,-1.042496,-4.027395,3.961921,-0.401313,-7.362709,8.667004,-2.668680,-9.879486,3.522982,3.611562,-5.025777,4.193005,-8.048320,-3.765114,-3.928170,6.042996,-5.327426,-1.189372,4.015051,-8.677181,-3.218604,-7.875014,8.689800,-5.389762,-7.008726,8.533847,4.079250,-7.968802,-3.003647,-9.128219,4.958794,2.770356,5.897713,5.842584,-7.008526,-6.393354,7.482472,-9.192438,6.652135,9.051599,-2.211367,-0.234151,1.374054,4.873430,-9.243086,-3.735656,0.703273,4.271932,8.727609,2.344479,-9.035026,-5.837609,-4.473891,-2.476664,7.670052,-3.120595,0.974374,-9.299686,3.455902,-6.228813,7.862168,2.062818,-3.172870,-0.326996,2.738902,6.966683,3.570968,3.907936,-0.349960,-7.293658,-2.303154,4.935980,9.854353,-4.386063,-7.479531,-8.063300,-8.940038,-8.183746,-1.961503,-0.118180,3.076739,-8.038416,-3.569883,-3.230539,4.111972,-0.355115,6.735374,1.549377,1.309916,-6.716503,-5.197791,-9.394731,-5.122602,3.453219,6.891664,1.284544,-6.009472,2.708788,5.411567,2.886427,-0.698956,-9.505527,-0.732212,0.414422,-8.123736,5.464287,-9.114212,9.169132,-3.924486,-7.958069,-7.707739,-9.666677,7.332397,4.411632,-0.588630,1.195220,4.419354,-8.266342,-0.903428,6.043925,4.877995,6.127848,-5.374816,6.290876,-6.621272,-0.810090,6.588553,9.203144,4.126681,4.483280,6.978726,-0.274338,9.742107,-4.524724,-6.353954,-6.387819,-8.849710,-4.293608,-8.851734,-8.005398,3.149276,2.959481,9.286183,4.106868,-7.372567,-7.297787,5.063668,-5.856709,-5.353759,-9.089591,-6.979245,-9.018494,8.700269,-8.177257,-3.733330,-1.451518,2.677419,-9.804864,-3.411318,3.109076,9.052206,-7.298386,1.043667,9.306818,-1.613663,-7.067964,-6.822753,0.711289,7.234687,4.664193,-6.784880,2.988064,2.452340,2.424336,4.472141,-0.304281,-3.078320,-8.706963,1.704047,5.862295,3.063802,8.249993,9.288792,9.740990,-7.567903,-2.338282,-3.948143,-3.683318,-7.411716,8.760785,7.793584,-6.138513,3.442393,5.883119,-5.459690,-7.873375,-7.729717,9.341496,-8.105602,3.775641,0.866677,-3.146872,2.077276,5.920457,-3.828669,-2.617274,8.708049,5.869210,4.793328,4.185600,-6.747476,3.210818,7.615925,-6.183230,-1.176533,-8.980015,5.799010,7.681918,-7.644716,-9.963924,-5.620966,-7.763434,7.417972,-3.724497,-3.108270,-1.118706,9.627176,5.650181,-3.992637,-5.110713,4.557071,-6.184124,7.274337,-2.752344,9.866077,-9.813752,4.675375,8.902901,8.645099,7.185410,8.022785,-0.431013,2.898392,-6.681440,4.534386,-8.484604,1.880953,1.842988,3.050571,-7.782858,9.181860,-4.957268,4.610466,4.979919,1.759140,-4.468766,2.819332,4.183792,5.726653,-2.451351,-8.374648,8.028623,-2.809373,1.479615,-8.854893,-9.979708,-6.206935,-3.318231,-6.308215,-2.719702,-7.520566,-4.872516,8.004890,1.413733,1.562930,0.074264,-4.246621,-5.658753,-4.500431,-3.782367,8.976619,-2.663155,6.394073,-7.145344,-4.591950,4.625619,6.789164,-4.936668,0.248746,2.829078,-8.040811,4.136222,-7.764301,3.658053,1.825471,2.868230,-7.978293,-3.660716,4.624159,7.702967,-1.118009,-4.284432,-9.206611,-3.752199,-9.192705,9.724949,2.864438,-9.607547,-7.703301,-1.878225,7.319835,-5.725958,3.531070,-2.209760,1.702382,-0.325345,-4.098155,-8.288495,-0.222889,2.874257,-9.184873,4.816216,7.130092,9.636053,5.525375,2.356608,-2.694823,-7.887119,-0.687228,-4.247266,-8.068637,0.634445]], dtype = "float32")#candidate|14579|(1, 750)|const|float32
call_14577 = relay.TupleGetItem(func_7792_call(relay.reshape(var_14578.astype('float64'), [6, 4, 11]), relay.reshape(const_14579.astype('float32'), [1, 750]), ), 1)
call_14580 = relay.TupleGetItem(func_7796_call(relay.reshape(var_14578.astype('float64'), [6, 4, 11]), relay.reshape(const_14579.astype('float32'), [1, 750]), ), 1)
func_11267_call = mod.get_global_var('func_11267')
func_11270_call = mutated_mod.get_global_var('func_11270')
var_14592 = relay.var("var_14592", dtype = "float32", shape = (336,))#candidate|14592|(336,)|var|float32
call_14591 = relay.TupleGetItem(func_11267_call(relay.reshape(var_14592.astype('float32'), [336,])), 0)
call_14593 = relay.TupleGetItem(func_11270_call(relay.reshape(var_14592.astype('float32'), [336,])), 0)
func_11742_call = mod.get_global_var('func_11742')
func_11744_call = mutated_mod.get_global_var('func_11744')
call_14594 = func_11742_call()
call_14595 = func_11742_call()
func_12653_call = mod.get_global_var('func_12653')
func_12655_call = mutated_mod.get_global_var('func_12655')
call_14596 = func_12653_call()
call_14597 = func_12653_call()
func_13349_call = mod.get_global_var('func_13349')
func_13353_call = mutated_mod.get_global_var('func_13353')
var_14608 = relay.var("var_14608", dtype = "float64", shape = (2, 504))#candidate|14608|(2, 504)|var|float64
const_14609 = relay.const([10,-7,-1,9,7,4,3,-1,-4,-3,5,5,9,-5,4,2,-5,5,9,-7,-9,-2,-4,-7,10,-9,5,2,-6,4,5,6,-3,8,-2,-8,8,5,5,-2,-1,-1,-9,-2,-2,-6,2,-8,2,7,-3,-9,7,2,-6,-8,-9,3,3,-2,-2,1,2,-1,7,10,-4,-8,-3,-2,7,5,-10,4,4,6,8,-3,9,7,-1,4,8,-8,-4,-9,2,-9,-10,4,10,-3,-1,9,10,6,2,9,-3,10,-7,2,-1,-2,5,9,9,-4,-8,-10,10,2,-7,-4,9,-10,3,8,3,6,-7,3,-9,-4,-1,-7,-2,5,-3,-10,2,-9,-3,8,-6,-4,-1,6,-6,-9,7,-10,-7,8,3,-10,-9,-10,5,-8,4,3,9,-7,10,-5,-2,-7,9,6], dtype = "uint64")#candidate|14609|(160,)|const|uint64
call_14607 = relay.TupleGetItem(func_13349_call(relay.reshape(var_14608.astype('float64'), [1008,]), relay.reshape(const_14609.astype('uint64'), [160,]), ), 4)
call_14610 = relay.TupleGetItem(func_13353_call(relay.reshape(var_14608.astype('float64'), [1008,]), relay.reshape(const_14609.astype('uint64'), [160,]), ), 4)
func_10716_call = mod.get_global_var('func_10716')
func_10720_call = mutated_mod.get_global_var('func_10720')
var_14621 = relay.var("var_14621", dtype = "bool", shape = (504,))#candidate|14621|(504,)|var|bool
call_14620 = relay.TupleGetItem(func_10716_call(relay.reshape(var_14621.astype('bool'), [8, 9, 7]), relay.reshape(var_14621.astype('bool'), [8, 9, 7]), ), 0)
call_14622 = relay.TupleGetItem(func_10720_call(relay.reshape(var_14621.astype('bool'), [8, 9, 7]), relay.reshape(var_14621.astype('bool'), [8, 9, 7]), ), 0)
output = relay.Tuple([call_14565,call_14570,const_14571,call_14577,var_14578,const_14579,call_14591,var_14592,call_14594,call_14596,call_14607,var_14608,const_14609,call_14620,var_14621,])
output2 = relay.Tuple([call_14566,call_14572,const_14571,call_14580,var_14578,const_14579,call_14593,var_14592,call_14595,call_14597,call_14610,var_14608,const_14609,call_14622,var_14621,])
func_14638 = relay.Function([var_14578,var_14592,var_14608,var_14621,], output)
mod['func_14638'] = func_14638
mod = relay.transform.InferType()(mod)
var_14639 = relay.var("var_14639", dtype = "float64", shape = (264,))#candidate|14639|(264,)|var|float64
var_14640 = relay.var("var_14640", dtype = "float32", shape = (336,))#candidate|14640|(336,)|var|float32
var_14641 = relay.var("var_14641", dtype = "float64", shape = (2, 504))#candidate|14641|(2, 504)|var|float64
var_14642 = relay.var("var_14642", dtype = "bool", shape = (504,))#candidate|14642|(504,)|var|bool
output = func_14638(var_14639,var_14640,var_14641,var_14642,)
func_14643 = relay.Function([var_14639,var_14640,var_14641,var_14642,], output)
mutated_mod['func_14643'] = func_14643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11751_call = mod.get_global_var('func_11751')
func_11753_call = mutated_mod.get_global_var('func_11753')
call_14663 = relay.TupleGetItem(func_11751_call(), 0)
call_14664 = relay.TupleGetItem(func_11753_call(), 0)
output = call_14663
output2 = call_14664
func_14665 = relay.Function([], output)
mod['func_14665'] = func_14665
mod = relay.transform.InferType()(mod)
mutated_mod['func_14665'] = func_14665
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14665_call = mutated_mod.get_global_var('func_14665')
call_14666 = func_14665_call()
output = call_14666
func_14667 = relay.Function([], output)
mutated_mod['func_14667'] = func_14667
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13432_call = mod.get_global_var('func_13432')
func_13434_call = mutated_mod.get_global_var('func_13434')
call_14731 = relay.TupleGetItem(func_13432_call(), 1)
call_14732 = relay.TupleGetItem(func_13434_call(), 1)
func_12617_call = mod.get_global_var('func_12617')
func_12619_call = mutated_mod.get_global_var('func_12619')
call_14748 = func_12617_call()
call_14749 = func_12617_call()
output = relay.Tuple([call_14731,call_14748,])
output2 = relay.Tuple([call_14732,call_14749,])
func_14750 = relay.Function([], output)
mod['func_14750'] = func_14750
mod = relay.transform.InferType()(mod)
mutated_mod['func_14750'] = func_14750
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14750_call = mutated_mod.get_global_var('func_14750')
call_14751 = func_14750_call()
output = call_14751
func_14752 = relay.Function([], output)
mutated_mod['func_14752'] = func_14752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14297_call = mod.get_global_var('func_14297')
func_14298_call = mutated_mod.get_global_var('func_14298')
call_14758 = func_14297_call()
call_14759 = func_14297_call()
output = relay.Tuple([call_14758,])
output2 = relay.Tuple([call_14759,])
func_14760 = relay.Function([], output)
mod['func_14760'] = func_14760
mod = relay.transform.InferType()(mod)
mutated_mod['func_14760'] = func_14760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14760_call = mutated_mod.get_global_var('func_14760')
call_14761 = func_14760_call()
output = call_14761
func_14762 = relay.Function([], output)
mutated_mod['func_14762'] = func_14762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14750_call = mod.get_global_var('func_14750')
func_14752_call = mutated_mod.get_global_var('func_14752')
call_14826 = relay.TupleGetItem(func_14750_call(), 1)
call_14827 = relay.TupleGetItem(func_14752_call(), 1)
func_13220_call = mod.get_global_var('func_13220')
func_13225_call = mutated_mod.get_global_var('func_13225')
var_14835 = relay.var("var_14835", dtype = "float64", shape = (30,))#candidate|14835|(30,)|var|float64
var_14836 = relay.var("var_14836", dtype = "float64", shape = (832,))#candidate|14836|(832,)|var|float64
var_14837 = relay.var("var_14837", dtype = "float64", shape = (480,))#candidate|14837|(480,)|var|float64
call_14834 = relay.TupleGetItem(func_13220_call(relay.reshape(var_14835.astype('float64'), [30,]), relay.reshape(var_14836.astype('float64'), [832,]), relay.reshape(var_14837.astype('float64'), [480,]), ), 1)
call_14838 = relay.TupleGetItem(func_13225_call(relay.reshape(var_14835.astype('float64'), [30,]), relay.reshape(var_14836.astype('float64'), [832,]), relay.reshape(var_14837.astype('float64'), [480,]), ), 1)
output = relay.Tuple([call_14826,call_14834,var_14835,var_14836,var_14837,])
output2 = relay.Tuple([call_14827,call_14838,var_14835,var_14836,var_14837,])
func_14839 = relay.Function([var_14835,var_14836,var_14837,], output)
mod['func_14839'] = func_14839
mod = relay.transform.InferType()(mod)
var_14840 = relay.var("var_14840", dtype = "float64", shape = (30,))#candidate|14840|(30,)|var|float64
var_14841 = relay.var("var_14841", dtype = "float64", shape = (832,))#candidate|14841|(832,)|var|float64
var_14842 = relay.var("var_14842", dtype = "float64", shape = (480,))#candidate|14842|(480,)|var|float64
output = func_14839(var_14840,var_14841,var_14842,)
func_14843 = relay.Function([var_14840,var_14841,var_14842,], output)
mutated_mod['func_14843'] = func_14843
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12065_call = mod.get_global_var('func_12065')
func_12067_call = mutated_mod.get_global_var('func_12067')
call_14868 = relay.TupleGetItem(func_12065_call(), 0)
call_14869 = relay.TupleGetItem(func_12067_call(), 0)
func_9509_call = mod.get_global_var('func_9509')
func_9511_call = mutated_mod.get_global_var('func_9511')
var_14871 = relay.var("var_14871", dtype = "float32", shape = (336,))#candidate|14871|(336,)|var|float32
call_14870 = relay.TupleGetItem(func_9509_call(relay.reshape(var_14871.astype('float32'), [12, 7, 4])), 0)
call_14872 = relay.TupleGetItem(func_9511_call(relay.reshape(var_14871.astype('float32'), [12, 7, 4])), 0)
output = relay.Tuple([call_14868,call_14870,var_14871,])
output2 = relay.Tuple([call_14869,call_14872,var_14871,])
func_14879 = relay.Function([var_14871,], output)
mod['func_14879'] = func_14879
mod = relay.transform.InferType()(mod)
mutated_mod['func_14879'] = func_14879
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14880 = relay.var("var_14880", dtype = "float32", shape = (336,))#candidate|14880|(336,)|var|float32
func_14879_call = mutated_mod.get_global_var('func_14879')
call_14881 = func_14879_call(var_14880)
output = call_14881
func_14882 = relay.Function([var_14880], output)
mutated_mod['func_14882'] = func_14882
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14417_call = mod.get_global_var('func_14417')
func_14418_call = mutated_mod.get_global_var('func_14418')
call_14886 = relay.TupleGetItem(func_14417_call(), 0)
call_14887 = relay.TupleGetItem(func_14418_call(), 0)
func_10329_call = mod.get_global_var('func_10329')
func_10333_call = mutated_mod.get_global_var('func_10333')
const_14905 = relay.const([9,-4,-5,3,-7,-3,2,-5,-10,5,9,-5,-7,8,-6,-2,9,1,-10,1,7,-10,2,10,-4,9,6,2,3,-9,-3,7,-7,-7,5,4,-1,-10,10,5,6,-7,-8,-8,-7,3,8,-3,8,-1,9,4,-10,3,4,-3,-3,-3,-1,3,9,-9,4,1,-3,5,-6,4,-3,5,4,-8,-2,8,-3,1,-7,-9,4,4,-10,1,-10,-3,9,-8,10,2,6,-5,-10,-1,7,-1,9,10,6,7,-6,7,-2,10,3,-4,-1,10,-5,10,2,-5,-7,-10,6,-7,2,8,10,-8,2,-4,10,4,-4,9,6,-4,-7,-7,6,5,-9,1,-3,-4,10,-5,1,-8,-6,10], dtype = "uint64")#candidate|14905|(140,)|const|uint64
const_14906 = relay.const([8,-1,-10,9,4,-8,-9,4,3,-3,-4,2,9,1,1,-4,-1,-1,3,-8,-10,-3,-7,-4,9,-3,-2,-9,10,-10,1,9,2,-4,-2,3,-9,2,-1,8,-6,7,5,-10,-5,7,8,-9,-8,5,-5,3,-3,10,5,-8,-1,10,-10,-3,3,-10,-8,9,-9,-7,3,8,6,3,-10,-2,-5,-8,-3,7,-3,-4,5,-6,-10,-1,-2,2,-9,-1,6,-1,-6,-4,-10,-4,10,-5,-3,-3,3,-7,-5,6,4,4,-1,-10,3,-5,-7,-7,8,3,-2,-4,10,-3,10,10,9,5,8,6,-9,4,1,-2,5,10,-2,6,8,9,-1,4,-1,-9,-4,10,-9,9,10,-10,-1,-4,-5,-6,-2,-2,4,-4,-7,-5,9,6,2,7,-9,8,-7,2,5,-6,-5,-3,-6,-3,9,4,5,-7,5,10,-10,3,-3,1,5,6,-8,8,-5,7,-10,5,10,4,-5,-9,-5,4,9,7,-5,-3,-1,6,-3,3,1,1,-7,7,3,6,-10,5,8,-5,-4,-5,-1,-4,-2,-8,-4,-4,-5,-2,-9,-8,1,-8,7,9,4,-8,-4,9,-9,9,-7,-4,-6,-3,-9,3,4,6,-7,-3,-10,5,-3,-8,-1,-8,1,-5,2,-1,-8,-8,6,-4,-10,1,9,-2,10,7,-8,-2,-8,-4,-4,9,9,-4,3,5,6,3,-4,8,-6,5,-1,-3,-3,-9,-3,-7,-8,-7,-1,-6,10,4,4,-6,-8,-6,-8,-10,-7,-8,-9,-3,7,10,2,-7,-5,6,3,-2,5,-4,7,5,-2,4,-7,-2,7,-4,-8,-1,2,-2,1,9,-2,-8,4,-2,-6,2,3,8,6,7,3,-6,-7,-1,4,4,-3,-4,-8,5,-1,7,-9,-4,-9,8,10,10,-4,-6,10,-6,-2,10,-5,2,-2,-1,-6,-5,-7,8,6,-5,-8,1,-8,-3,-7,10,9,-9,-3,-9,9,-3,-6,-6,-10,5,1,-7,4,1,4,3,-3,2,5,4,-7,10,9,-8,-6,-8,10,10,-7,3,-2,5,-1,1,10,9,2,5,-7,2,-5,-4,6,-8,5,-4,-10,-2,6,6,-1,-7,6,6,-2,-1,-1,-3,7,1,5,-8,-4,5,-6,-8,-5,7,5,-9,4,-8,-2,-1,4,-10,-7,5,9,-1,-10,1,4,-9,3,-7,-7,-1,6,10,6,-1,10,-2,4,3,2,9,4,-4,7,4,-6,3,-9,-4,-2,-7,10,1,-3,-10,-10,1,-9,1,-6,-8,-1,6,3,-6,6,-5,-3,10,1,-2,-1,5,8,5,-10,-8,-3,3,-4,-1,4,-7,-2,-2,-9,6,-7,-9,6,1,-7,8,-3,6,-2,8,-2,-3,-3,7,-1,-1,3,-5,2,-6,-7,8,5,-7,-10,-5,1,-9,4,8,9,6,-9,-3,-9,1,1,-5,-5,7,7,-10,-1,5,-4,-3,-2,9,9,2,8,5,-5,10,-3,7,-1,10,-5,9,6,4,-10,9,4,-9,-7,6,7,3,-4,-9,7,-9,4,4,2,10,-3,-1,-2,-1,-7,4,2,-5,8,-3,5,9,-4,1,-3,5,-4,4,9,7,-2,-1,6,3,9,-9,2,4,-3,9,10,5,-10,-9,4,-4,-7,-3,10,9,3,-4,7,10,-4,7,3,-7,-1,-2,10,-1,1,-2,-1,-10,8,-1,3,5,10,-3,-6,-6,5,-1,-3,4,8,5,-6,6,-3,8,-8,-5,-9,-1,-9,9,4,10,2,-9,1,-10,3,10,-10,-1,-3,7,5,6,-5,-7,-5,-6,3,5,-1,1,-10,-9,-1,-3,7,8,-9,3,9,5,-8,-1,6,5,3,-3,-8,7,3,8,9,-1,10,2,-5,-5,8,4,-2,-5,-6,9,-1,7,-4,7,1,-2,3,2,3,-10,3,-6,4,1,-10,-6,-7,-8,-6,-4,2,-9,10,-2,1,3,-6,3,10,10,4,-10,10,2,2,4,2,6,7,4,-10,5,5,7,-2,5,4,-7,-5,10,-6,1,8,-1,-5,-4,-1,-2,5,-4,-6,-4,-6,5,-1,9,7,-7,-7,-1,-3,-9,4,-3,-1,-7,-5,7,4,-3,7,4,1,-1,2,-5,7,-1,5,9,2,5,8,1,4,-7,-5,4,-4,6,-7,3,5,6,-2,8,-2,3,4,10,-5,8,-9,8,7,1,5,9,-10,9,-9,-5,-9,1,-2,1,9,1,-10,-3,-1,3,8,5,9,9,-1,1,5,-3,-4,-8,2,4,8,-10,-4,6,-7,10,-5,5,7,7,-9,-1,-5,-9,10,-10,1,-7,3,6,4,-5,7,6,6,-6,-4,-8,-7,5,-8,-6,-4,-5,8,-6,-9,1,9,-10,1,-9,-4,-5,2,2,4,3,3,-5,-9,-3,-10,-4,4,-5,1,-1,1,-10,5,-4,-10,-6,-5,3,-10,2,-3,-10,-10,3,8,-8,1,3,10,6,6,-2,-3,-9,-3,4,7,2,-10,1,-8,-9,9,-6,1,8,4,-2,-6,9,-10,-5,8,6,-2,-7,10,-1,10,-5,-9,-10,-4,9,1,-1,-2,2,6,9,-7,-10,4,5,1,7,-4,3,1,-1,-8,5,-1,-2,-5,4,-7,10,-8,-7,4,8,-3,9,1,-6,2,-10,8,-1,1,6,2,9,-10,8,10,-1,7,7,-10,8,4,-7,10,-5,5,-10,9,6,8,1,-2,-1,4,8,10,-6,-3,-7,2,5,5,-2,-7,-2,-6,2,-9,8,2,-7,-9,-7,7,5,-9,-5,-8,-9,-7,9,-7,-1,8,8,-3,-4,-8,-7,6,4,-2,10,-6,-4,-3,8,8,4,9,5,9,-8,-10,-1,7,-4,4,1,-4,-5,-10,4,-2,-1,2,-5,-7,7,-8,-6,4,5,3,-8,-1,-3,-3,8,-9,8,-6,4,8,1,-2,2,-8,-3,-1,9,5,-4,2,6,2,5,-7,-1,2,2,2,9,-8,-2,-5,-2,6,-9,-9,-2,-8,-9,5,1,-6,9,-6,-8,3,5,3,-10,-5,-9,-5,5,5,-8,4,8,-2,-7,-7,3,7,10,7,-10,1,9,8,9,6,6,7,-1,4,7,3,3,-8,-1,-5,7,2,-9,-10,6,6,-7,7,-1,-5,2,6,9,10,-9,3,-8,4,5,-8,1,4,-6,-7,2,5,10,-1,7,9,6,-4,6,4,3,4,-5,-3,1,-7,-1,-9,6,-10,-5,1,-2,6,2,-1,1,10,-4,-8,-2,-10,-9,-4,2,10,-2,7,-5,-1,-4,-3,-8,2,7,-8,6,3,-8,-2,10,6,-2,-7,-7,-5,3,-5,-2,-6,6,7,-4,7,7,10,3,3,-10,-4,3,5,9,8,6,8,7,-6,-8,-3,-4,4,1,-5,-10,-6,-10,8,1,-9,-1,1,-6,9,1,9,-6,-7,2,8,2,-6,4,-4,-3,4,-1,2,-5,1,4,3,3,-7,-3,1,-8,10,3,9,-6,-10,9,6,2,9,-7,5,6,9,8,5,-6,-2,-8,7,-3,4,-8,7,8,-5,2,-9,4,6,-5,-10,7,-4,-2,-2,9,-10,-6,6,-4,-1,10,5,-7,6,3,4,7,-6,10,-3,-1,5,-9,-3,1,9,3,3,-4,-1,4,-8,5,7,1,-6,4,-2,-4,6,-9,7,9,-4,-1,-2,2,6,-4,-5,-7,-9,-2,-4,6,-10,-4,-8,8,-8,7,-6,1,-8,-4,-2,-2,2,10,10,5,-10,8,-4,10,-7,-3,7,4,-1,-8,9,-1,-6,6,-6,8,2,4,4,9,2,-4,-7,6,-9,8,8,1,-10,-2,10,4,5,9,1,-3,-1,2,7,6,4,-4,-5,8,1,-4,9,-2,-4,-4,-8,-10,5,-7,-1,6,6,10,6,9,-8,-8,-10,1,-3,1,-3,-2,-2,-1,-1,10,9,-1,8,2,-2,2,5,6,-2,9,7,-4,-10,1,1,3,1,-5,-3,-4,-9,6,2,2,-10,-9,-4,-5,-5,-8,-8,-6,-4,-6,10,-1,-8,5,-1,-4,-1,8,-6,-10,9,-9,8,4,8,10,-1,1,9,9,-6,-1,-8,10,1,-8,9,-7,-3,-10,10,3,10,1,1,-9,5,-3,10,8,5,-4,-3,3,2,9,3,3,7,5,4,-6,-6,1,-4,9,-4,6,-4,5,4,7,-7,3,6,3,-1,-8,-10,3,9,3,-7,-3,8,6,-2,-9,5,5,9,-3,7,-9,2,10,6,-7,10,1,-7,-10,-1,-10,-1,2,-2,-2,6,-5,3,-2,-7,-1,10,-7,-2,8,3,2,2,6,8,-5,9,-5,-5,3,-7,-1,10,-3,-4,-4,10,5,-9,-8,-6,1,2,10,-2,-1,9,5,-1,-10], dtype = "uint64")#candidate|14906|(1680,)|const|uint64
call_14904 = func_10329_call(relay.reshape(const_14905.astype('uint64'), [14, 10, 1]), relay.reshape(const_14906.astype('uint64'), [14, 10, 12]), )
call_14907 = func_10329_call(relay.reshape(const_14905.astype('uint64'), [14, 10, 1]), relay.reshape(const_14906.astype('uint64'), [14, 10, 12]), )
output = relay.Tuple([call_14886,call_14904,const_14905,const_14906,])
output2 = relay.Tuple([call_14887,call_14907,const_14905,const_14906,])
func_14930 = relay.Function([], output)
mod['func_14930'] = func_14930
mod = relay.transform.InferType()(mod)
mutated_mod['func_14930'] = func_14930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14930_call = mutated_mod.get_global_var('func_14930')
call_14931 = func_14930_call()
output = call_14931
func_14932 = relay.Function([], output)
mutated_mod['func_14932'] = func_14932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11751_call = mod.get_global_var('func_11751')
func_11753_call = mutated_mod.get_global_var('func_11753')
call_14978 = relay.TupleGetItem(func_11751_call(), 0)
call_14979 = relay.TupleGetItem(func_11753_call(), 0)
func_14665_call = mod.get_global_var('func_14665')
func_14667_call = mutated_mod.get_global_var('func_14667')
call_14986 = func_14665_call()
call_14987 = func_14665_call()
output = relay.Tuple([call_14978,call_14986,])
output2 = relay.Tuple([call_14979,call_14987,])
func_14992 = relay.Function([], output)
mod['func_14992'] = func_14992
mod = relay.transform.InferType()(mod)
output = func_14992()
func_14993 = relay.Function([], output)
mutated_mod['func_14993'] = func_14993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14992_call = mod.get_global_var('func_14992')
func_14993_call = mutated_mod.get_global_var('func_14993')
call_14994 = relay.TupleGetItem(func_14992_call(), 0)
call_14995 = relay.TupleGetItem(func_14993_call(), 0)
output = call_14994
output2 = call_14995
func_14996 = relay.Function([], output)
mod['func_14996'] = func_14996
mod = relay.transform.InferType()(mod)
mutated_mod['func_14996'] = func_14996
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14996_call = mutated_mod.get_global_var('func_14996')
call_14997 = func_14996_call()
output = call_14997
func_14998 = relay.Function([], output)
mutated_mod['func_14998'] = func_14998
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11833_call = mod.get_global_var('func_11833')
func_11835_call = mutated_mod.get_global_var('func_11835')
call_15035 = relay.TupleGetItem(func_11833_call(), 0)
call_15036 = relay.TupleGetItem(func_11835_call(), 0)
output = relay.Tuple([call_15035,])
output2 = relay.Tuple([call_15036,])
func_15046 = relay.Function([], output)
mod['func_15046'] = func_15046
mod = relay.transform.InferType()(mod)
output = func_15046()
func_15047 = relay.Function([], output)
mutated_mod['func_15047'] = func_15047
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14417_call = mod.get_global_var('func_14417')
func_14418_call = mutated_mod.get_global_var('func_14418')
call_15060 = relay.TupleGetItem(func_14417_call(), 0)
call_15061 = relay.TupleGetItem(func_14418_call(), 0)
output = call_15060
output2 = call_15061
func_15065 = relay.Function([], output)
mod['func_15065'] = func_15065
mod = relay.transform.InferType()(mod)
output = func_15065()
func_15066 = relay.Function([], output)
mutated_mod['func_15066'] = func_15066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12956_call = mod.get_global_var('func_12956')
func_12958_call = mutated_mod.get_global_var('func_12958')
call_15069 = relay.TupleGetItem(func_12956_call(), 3)
call_15070 = relay.TupleGetItem(func_12958_call(), 3)
func_6391_call = mod.get_global_var('func_6391')
func_6393_call = mutated_mod.get_global_var('func_6393')
const_15078 = relay.const(-7, dtype = "int16")#candidate|15078|()|const|int16
call_15077 = relay.TupleGetItem(func_6391_call(relay.reshape(const_15078.astype('int16'), [])), 1)
call_15079 = relay.TupleGetItem(func_6393_call(relay.reshape(const_15078.astype('int16'), [])), 1)
output = relay.Tuple([call_15069,call_15077,const_15078,])
output2 = relay.Tuple([call_15070,call_15079,const_15078,])
func_15084 = relay.Function([], output)
mod['func_15084'] = func_15084
mod = relay.transform.InferType()(mod)
output = func_15084()
func_15085 = relay.Function([], output)
mutated_mod['func_15085'] = func_15085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15084_call = mod.get_global_var('func_15084')
func_15085_call = mutated_mod.get_global_var('func_15085')
call_15142 = relay.TupleGetItem(func_15084_call(), 2)
call_15143 = relay.TupleGetItem(func_15085_call(), 2)
output = call_15142
output2 = call_15143
func_15174 = relay.Function([], output)
mod['func_15174'] = func_15174
mod = relay.transform.InferType()(mod)
mutated_mod['func_15174'] = func_15174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15174_call = mutated_mod.get_global_var('func_15174')
call_15175 = func_15174_call()
output = call_15175
func_15176 = relay.Function([], output)
mutated_mod['func_15176'] = func_15176
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11578_call = mod.get_global_var('func_11578')
func_11579_call = mutated_mod.get_global_var('func_11579')
call_15247 = relay.TupleGetItem(func_11578_call(), 0)
call_15248 = relay.TupleGetItem(func_11579_call(), 0)
func_14297_call = mod.get_global_var('func_14297')
func_14298_call = mutated_mod.get_global_var('func_14298')
call_15254 = func_14297_call()
call_15255 = func_14297_call()
output = relay.Tuple([call_15247,call_15254,])
output2 = relay.Tuple([call_15248,call_15255,])
func_15257 = relay.Function([], output)
mod['func_15257'] = func_15257
mod = relay.transform.InferType()(mod)
output = func_15257()
func_15258 = relay.Function([], output)
mutated_mod['func_15258'] = func_15258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12617_call = mod.get_global_var('func_12617')
func_12619_call = mutated_mod.get_global_var('func_12619')
call_15321 = func_12617_call()
call_15322 = func_12617_call()
func_12848_call = mod.get_global_var('func_12848')
func_12850_call = mutated_mod.get_global_var('func_12850')
call_15332 = func_12848_call()
call_15333 = func_12848_call()
func_13629_call = mod.get_global_var('func_13629')
func_13633_call = mutated_mod.get_global_var('func_13633')
const_15342 = relay.const([4.365504,1.457310,7.923404,6.693483,-0.461019,7.219194,-7.211788,-9.618983,-4.086334,-3.029713,-3.205456,-3.507616,-6.261186,8.720806,8.135219,6.805280,-0.558976,4.979640,3.071045,7.438653,8.946861,5.476174,3.027309,-8.080791,1.705188,-1.984356,2.635214,3.893005,-0.332070,0.042082,-5.136424,-7.492538,4.371954,-9.824640,3.676092,5.704686,-1.945511,-1.758908,-7.393892,6.453881,4.011181,-8.003466,2.799004,7.753730,-3.141980,9.409714,2.568520,3.880080,5.419997,-8.432822,-4.574629,5.683380,-3.418897,-6.921877,-3.970547,-5.075404,9.783197,-4.916818,-1.205622,-1.398854,-9.060901,8.440086,6.607384,5.458838,-4.070985,0.693753,8.541581,0.952511,-6.973568,-9.963511,-7.351046,4.577769,3.257657,-3.572716,6.315218,0.384612,-8.617383,6.395436,5.935932,-4.103243,-7.604259,-4.132682,-6.969799,8.474488,0.631142,5.455665,-9.368864,2.544247,8.450256,-5.088343,-3.952024,-9.818322,-5.906605,9.416838,-8.836078,-2.137388,5.739273,-9.384884,-0.500521,4.452164,-3.245534,5.399349,0.833287,-6.915208,-5.958431,2.157777,-0.548376,7.826119,2.570257,7.743794,-8.874372,5.663412,-2.819836,4.726722,0.129539,9.484733,-5.710839,0.680037,5.907345,-2.350420,-6.664872,9.467420,7.660512,0.751002,7.300339,0.119024,-6.223663,8.671218,-8.591566,-5.515472,6.434956,1.686620,-6.541453,4.790931,4.265958,-5.860046,3.635548,-9.764072,-0.010039,-4.132489,-9.864308,-5.809332,-7.570391,-3.481992,-7.991707,-7.521802,-8.057632,1.279432,-2.068185,-8.412092,-7.217774,4.551169,-2.402149,9.560620,-0.975404,-9.639391,2.637384,9.437962,7.375283,-1.694292,-5.652832,7.806549,8.705008,-0.318796,-1.279138,8.615469,6.784737,-7.194480,-4.188092,-8.018779,3.079057,-9.334006,3.303850,-1.166576,8.616853,8.799194,-7.688561,-3.584493,1.746470,9.396521,4.066301,4.333774,-8.497088,2.705582,9.227251,2.296820,-5.048079,9.694255,1.625594,-7.529211,-2.866428,2.876942,8.182369,-9.563420,-9.024957,-1.053213,-5.696193,-2.692616,9.839532,-7.285849,0.942536,-2.020069,3.254498,-9.335791,1.273690,6.399819,-3.468429,-2.549347,-7.687738,-6.394951,0.355206,-2.283318,-3.000844,-9.119561,-2.374886,-8.666248,-5.448948,-6.001192,-3.644767,-9.379668,5.084449,-7.804108,-6.478248,7.580958,5.677954,5.147798,-6.712280,0.100923,-1.452066,6.907743,-6.809156,6.537056,-0.807302,-7.647677,-7.110016,-1.206202,-0.433042,5.238849,-2.164072,8.256039,-9.518054,-5.417061,-6.082897,-6.318108,6.795127,-7.537418,4.115775,-3.050484,1.786694,2.926567,8.887657,8.243627,-9.854393,3.909286,-3.569088,-7.329577,0.416716,5.691886,-7.884646,9.710863,5.357873,5.460823,7.474341,-0.427604,-5.212456,-3.192565,-3.976772,6.661259,-4.431801,8.568377,0.877397,6.883274,-0.336876,9.342874,-8.904558,-2.949750,-3.491804,4.421578,3.673453,-3.524383,7.759204,2.046278,-3.615498,-5.153363,9.303618,2.080781,9.050947,-7.356205,-8.176646,4.154585,-6.941019,-3.070686,1.091023,-8.254552,-4.762006,4.533529,7.875651,5.486297,5.290804,-2.019912,5.378607,-1.514043,-4.880766,-7.440176,-0.515891,-2.334465,7.227111,0.567743,-0.020453,5.096563,-4.775261,-1.973362,6.896643,6.369675,7.131964,-7.803937,-1.721202,1.764794,7.491824,0.141873,8.216393,-2.892299,-3.981548,-7.641399,1.409525,4.130745,-1.826067,2.363108,9.890120,-5.249840,-2.727002,1.725779,2.501309,8.276670,-9.625489,-4.246750,-4.142169,-5.249825,-3.873819,2.043775,-9.541101,3.058377,-5.594038,9.599648,-7.196690,-1.860515,-3.792447,5.407287,9.731288,-1.269011,9.493495,9.857908,4.293390,-3.215012,-1.305791,2.813130,2.173130,1.490835,9.428352,3.433073,7.494462,-3.779640,-4.136630,4.757606,-9.385706,3.126347,4.105684,-4.630771,0.170141,-2.200081,-7.416563,-1.814161,1.538968,-1.955712,-2.173535,-2.018721,4.134401,6.293143,-4.154637,1.128863,-3.795075,-9.725974,-0.282535,-7.000882,3.099366,5.369445,-1.833666,0.047864,-0.072306,-3.099121,-5.247148,-1.493312,0.005828,0.864443,-1.542348,8.903844,6.121085,-1.801937,-7.389140,1.609470,-1.274665,8.240843,8.718381,-6.409318,-8.405292,-6.356677,4.680019,0.634118,3.541499,-7.687724,5.992968,-3.359260,1.977915,-9.936183,-4.072153,0.743267,8.741639,2.614578,-9.623720,-8.749784,0.301199,2.029968,4.693992,1.254072,2.838693,-7.728348,4.042874,5.206849,-3.797447,-2.862683,-3.614734,6.444397], dtype = "float64")#candidate|15342|(432,)|const|float64
const_15343 = relay.const([-6.273369,-0.853973,7.022428,-3.043053,-7.496354,1.276045,5.326119,7.836348,3.755471,7.012737,-2.031639,-2.398312,4.660205,-5.704169,-2.372826,-4.765510,2.452986,-1.363657,-1.704771,3.437533,9.778764,-7.949132,1.060248,1.182527,6.516479,-2.539790,6.034851,-7.728241,-8.835665,5.732319,8.858981,0.413065,-1.679371,5.875427,-5.054728,-5.496165,-1.267635,-7.562822,-9.141389,-3.487573,-0.986401,1.515617,4.337604,-5.798318,9.371908,-8.056956,-7.866104,9.254544,-1.885800,6.373963,-2.831756,-4.000787,4.829205,-4.326301,-2.437177,9.047088,2.651580,-9.052114,-3.835655,-3.802738,-5.887147,-1.837392,-1.901359,-5.685953,-1.758022,3.378613,6.445050,7.226188,-5.575417,-2.294732,-1.868208,6.464073,-1.279443,-9.375945,-1.029313,-3.605102,-3.038564,3.870305,5.789869,0.061333,-7.230946,-9.862422,-4.838624,-5.689800,5.582258,5.523838,-2.091629,2.956474,4.999792,1.105529,-6.779110,-3.008645,-6.288131,1.298869,3.581685,7.304271,1.708188,6.331152,-8.482008,-7.971370,-1.427324,4.672627,-1.694162,-8.961229,0.850942,0.114269,6.263631,-2.528093,-0.737908,1.192015,-9.131932,9.542646,-6.450825,1.389457,-9.570319,-0.813144,1.076188,6.214965,-8.481551,2.481672,0.537869,6.958842,3.232046,-1.004540,2.231248,5.371023,-0.130462,7.938133,-4.596157,2.870990,-6.913540,2.770729,-9.028741,0.380364,-7.916740,-4.091216,-4.361864,4.150110,8.462477,0.561126,5.147240,-4.031920,4.180569,0.940712,-2.199733,-7.625941,-7.821822,-9.596550,-4.713526,-8.751754,7.433868,-7.155694,-4.102013,6.824745,3.523865,1.325828,0.414967,-3.315572,6.139952,-0.041446,4.181569,2.786776,2.065151,-6.368981,0.239262,-4.640452,3.915761,-5.067010,-5.235766,9.573245,-9.804150,3.974098,-7.537451,-0.289641,4.402049,4.348332,8.112430,-2.660679,-1.771109,-1.997661,3.516783,-9.510458,9.023553,7.332124,-9.346165,0.577268,9.009452,6.925754,1.726086,4.846313,-0.699504,4.710818,2.632527,-0.173427,-9.003852,-5.780577,-1.960164,-5.109611,0.586453,0.586907,-3.222162,2.762981,1.655237,8.369121,-2.103021,7.326559,8.031649,7.715278,6.567657,-0.785784,-5.691896,4.589117,-5.955784,1.179384,0.643162,3.629072,6.745278,9.611741,8.636299,8.622862,-6.782621,9.455931,7.989742,-0.067969,-4.528005,-9.937482,5.253679,8.876324,3.182859,-3.094352,-1.451329,-6.583973,-4.335367,-0.419959,-2.442898,1.883894,5.486313,-8.938390,1.869306,4.316455,-5.275066,4.397799,4.070900,2.772787,6.120611,-0.345786,2.639240,4.785362,-1.908432,-4.692209,-4.447270,5.456132,-4.530346,-8.726345,2.888334,9.628868,-1.711072,9.885631,-8.327848,-5.209820,-6.899597,2.473742,-5.960907,7.653182], dtype = "float64")#candidate|15343|(264,)|const|float64
var_15344 = relay.var("var_15344", dtype = "float32", shape = (750,))#candidate|15344|(750,)|var|float32
call_15341 = relay.TupleGetItem(func_13629_call(relay.reshape(const_15342.astype('float64'), [4, 108]), relay.reshape(const_15343.astype('float64'), [264,]), relay.reshape(var_15344.astype('float32'), [750,]), ), 4)
call_15345 = relay.TupleGetItem(func_13633_call(relay.reshape(const_15342.astype('float64'), [4, 108]), relay.reshape(const_15343.astype('float64'), [264,]), relay.reshape(var_15344.astype('float32'), [750,]), ), 4)
func_7045_call = mod.get_global_var('func_7045')
func_7047_call = mutated_mod.get_global_var('func_7047')
var_15347 = relay.var("var_15347", dtype = "float64", shape = (13, 14))#candidate|15347|(13, 14)|var|float64
call_15346 = relay.TupleGetItem(func_7045_call(relay.reshape(var_15347.astype('float64'), [13, 1, 14])), 0)
call_15348 = relay.TupleGetItem(func_7047_call(relay.reshape(var_15347.astype('float64'), [13, 1, 14])), 0)
output = relay.Tuple([call_15321,call_15332,call_15341,const_15342,const_15343,var_15344,call_15346,var_15347,])
output2 = relay.Tuple([call_15322,call_15333,call_15345,const_15342,const_15343,var_15344,call_15348,var_15347,])
func_15367 = relay.Function([var_15344,var_15347,], output)
mod['func_15367'] = func_15367
mod = relay.transform.InferType()(mod)
var_15368 = relay.var("var_15368", dtype = "float32", shape = (750,))#candidate|15368|(750,)|var|float32
var_15369 = relay.var("var_15369", dtype = "float64", shape = (13, 14))#candidate|15369|(13, 14)|var|float64
output = func_15367(var_15368,var_15369,)
func_15370 = relay.Function([var_15368,var_15369,], output)
mutated_mod['func_15370'] = func_15370
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12653_call = mod.get_global_var('func_12653')
func_12655_call = mutated_mod.get_global_var('func_12655')
call_15391 = func_12653_call()
call_15392 = func_12653_call()
const_15409 = relay.const([[[6.772666,-8.648662,4.360128,-2.598410,3.278125,-4.572058,-2.554574,3.445874,-7.670968,8.503075,-4.983966,0.469902,5.544944,0.882318],[7.864438,5.402007,6.759480,9.215106,-4.996484,9.435493,-5.491772,6.329165,2.484597,4.805009,-9.038634,6.168192,5.668978,-2.482798],[3.298946,-9.012332,-9.610671,-2.280167,1.807268,-2.306381,9.921709,2.294393,8.741140,6.689459,-0.079970,3.992169,7.883211,7.711082],[1.924053,1.474683,8.340655,0.584897,-7.747344,-3.427442,-3.508059,4.034085,-0.020639,8.920940,0.131058,-8.758186,6.354708,-7.757683],[-1.534194,8.080727,-6.687504,-3.515894,-2.752735,4.970420,7.869630,-8.962283,8.155649,-8.647294,9.844570,6.112519,-1.628977,-5.406123]],[[4.746643,-0.987595,-6.649267,5.568693,5.045804,-1.970283,-9.851016,-8.693964,1.010746,9.862467,-3.225963,-4.835351,0.691730,1.720774],[3.781372,1.283207,-2.774532,-8.315025,-2.160544,8.578720,-1.497257,5.542435,-2.145877,-2.921122,5.922636,-4.234535,5.561321,2.448249],[-4.150131,-8.917359,-3.583099,4.649123,-7.867850,7.759382,8.801358,-7.306840,-3.716143,-0.977641,4.779524,0.472703,-7.194983,-8.959424],[-1.099216,-1.635360,-5.456269,7.636061,7.113603,-4.213242,-1.160878,-2.430261,-7.879458,3.406066,-2.497121,0.443816,2.993533,-8.321748],[-8.646066,5.846123,-6.066893,-2.121012,6.564133,9.729881,-5.828650,-3.056310,9.248781,-9.475741,8.047569,2.995730,-0.309291,9.269578]],[[2.265126,3.061112,-6.042392,-3.745254,3.746276,-3.162149,-6.145283,4.561472,3.507135,-3.584819,-4.338600,-8.311775,-2.327561,7.743045],[8.536872,-1.791933,3.522618,-0.333016,4.036529,-8.895122,4.237353,1.467655,9.950171,-8.048142,-1.773475,2.036653,-2.312796,-1.031387],[3.415337,2.553192,-7.443235,7.406764,3.538692,7.134861,7.074672,0.526297,-0.988918,-1.178032,5.392030,-9.097442,3.722887,-7.666429],[-0.467926,2.998354,7.361555,-8.233859,-2.414324,8.870947,7.056880,-0.761692,-1.296808,-2.346278,-3.676187,-6.853167,3.831137,3.717486],[4.753000,-7.904983,-7.273435,8.155257,-0.376162,0.322052,-2.535197,3.468131,-4.932980,-2.054270,7.842852,2.647294,8.238426,-3.778821]],[[0.232657,-4.784013,8.400392,-6.201725,-0.665216,9.600043,5.055862,7.810621,2.625733,8.637769,1.296683,9.036279,-4.040747,-0.067336],[-4.314965,0.052332,7.842317,-8.144655,-9.549478,-6.830761,9.754733,-8.677477,0.157161,-3.706753,-5.471526,-9.410437,5.579928,-0.030399],[-0.913505,8.251654,2.626711,-1.816424,-8.527835,-4.066964,5.986792,0.984503,-4.084723,9.504943,-1.885384,9.181766,-6.030079,-8.488539],[3.483948,7.547436,3.753213,-3.286150,3.322318,8.430798,-1.568630,2.428172,8.614921,-1.415064,-5.620398,9.944938,9.872437,0.714106],[-2.796917,5.368275,-0.218882,7.198638,9.687392,6.571673,6.842072,7.121115,-0.476808,4.804873,3.279672,2.523046,-1.826953,-4.454441]],[[2.607190,3.059165,1.251006,6.602433,2.964970,-1.976977,0.663006,-8.882060,-2.418751,-9.026525,-4.802445,-7.901740,2.439842,0.499410],[-1.655206,0.711307,1.752282,0.429467,0.508016,-4.230156,-3.642810,6.677533,-5.485786,-6.472840,6.835032,2.079416,-3.375574,-8.772164],[-4.964198,5.526358,3.907943,-9.392483,9.318926,-1.443210,2.183248,-1.866581,4.939885,2.519902,1.956347,-8.190922,-5.798466,-2.762924],[-8.845944,-3.434364,-3.447033,2.204861,-8.987217,-5.176673,-0.260977,-0.700331,7.401173,7.890195,-1.824669,1.003116,-3.307448,3.652267],[9.236820,5.722398,-5.675221,-4.777418,-9.100913,-7.303621,-4.728503,-7.943316,8.194217,-2.629470,4.462598,2.533299,-4.608969,6.300208]],[[7.883896,1.477790,-3.674215,-0.969692,-7.739155,4.832614,-4.433090,1.607586,-3.554622,8.344126,-5.453836,5.149595,5.329563,5.462515],[2.910387,-1.793797,6.814957,7.391753,9.311727,-3.584101,1.903018,-5.622266,-9.313104,-5.781547,3.564629,-0.852119,0.293579,-6.585868],[7.496751,-8.959762,-6.394905,1.118870,-8.003540,-9.491832,-1.741659,4.793877,-0.100555,1.941628,3.583483,-7.368736,-9.466575,-9.887418],[-9.599264,-7.562870,-1.169988,-5.936875,-4.811900,5.721544,-5.039026,-0.755991,-1.490808,-2.732357,0.016115,8.581563,0.440211,3.538850],[1.306020,4.379802,-3.409041,7.963114,-5.360120,-0.329505,8.041237,0.588715,6.149219,-9.690433,2.220653,-7.218642,-5.010682,0.245439]],[[8.462683,8.058014,-4.087104,-9.059017,2.363787,-7.760748,8.146593,-1.815258,-2.510077,0.847974,4.239084,5.412159,-3.804134,2.211671],[-1.226579,2.828954,8.727003,-8.187307,7.508582,8.827516,-4.834321,7.938009,-4.150444,-1.855232,5.951481,-2.298586,2.087985,-1.362796],[4.109242,-2.227570,-2.939040,-4.437744,6.875618,-4.960756,3.546147,0.365612,4.797815,-1.954676,-3.811373,-3.635329,-4.459854,-3.710295],[-7.623766,6.815424,-5.842023,4.407595,2.772602,-5.416901,-2.184352,-6.656236,-0.345775,3.024052,-0.450606,1.242868,-3.370593,-2.561948],[-9.494032,-9.576190,1.024035,0.510908,-3.387269,5.214923,-3.592553,-5.394737,-9.187500,-2.240824,-3.656579,-0.176089,0.804967,8.663369]],[[6.369727,-4.282660,-3.200819,-9.306053,9.271053,3.907305,1.262026,6.593166,-7.464600,-5.725465,-9.336633,-5.176758,4.368246,0.125422],[-3.098238,-7.402565,2.584952,-7.480603,-7.677473,8.652094,-7.387284,0.799020,1.198506,9.946433,-6.618706,-8.882487,-8.093125,2.904877],[2.651270,1.449714,7.477351,3.673247,-8.322463,-8.828523,8.551346,-7.408928,-5.766643,9.183879,7.694146,3.940026,-9.232352,-4.318330],[-7.989973,-2.229954,7.634311,-8.337718,-0.807798,9.352197,3.255012,3.998845,5.320778,-4.002441,9.581527,-8.348883,-8.058263,-3.360535],[9.955831,6.825165,-4.654011,-8.238848,9.232122,-8.113220,-0.748492,3.445891,7.888635,-9.741350,-6.721995,-2.386312,-2.188709,-5.720077]],[[-1.655513,-4.278505,-4.715443,-8.245178,0.797734,-5.205292,7.799923,-1.954090,-4.969668,5.568586,-9.703438,-2.317134,-8.758013,-3.051461],[1.220405,8.380171,8.710733,-4.830266,0.772957,-6.541209,7.947376,-4.592992,7.927801,-8.393805,-1.350441,2.791733,-6.113571,5.042737],[-0.930157,9.246947,1.538483,-1.300960,-0.346806,-9.388823,0.903621,5.495414,4.834593,6.294358,-4.109846,-3.590190,0.071392,-7.699236],[1.653542,-8.507407,2.190398,-6.737047,-4.307235,-2.262524,6.686089,-4.848984,7.242477,5.389750,0.647821,-8.739155,-5.346714,-3.407685],[-2.634772,9.331693,9.405509,-4.895916,-1.914947,5.237901,4.300584,6.597378,-2.845641,0.742178,7.135456,-5.184549,3.522424,1.510694]]], dtype = "float32")#candidate|15409|(9, 5, 14)|const|float32
bop_15410 = relay.not_equal(call_15391.astype('bool'), relay.reshape(const_15409.astype('bool'), relay.shape_of(call_15391))) # shape=(9, 5, 14)
bop_15413 = relay.not_equal(call_15392.astype('bool'), relay.reshape(const_15409.astype('bool'), relay.shape_of(call_15392))) # shape=(9, 5, 14)
output = bop_15410
output2 = bop_15413
func_15426 = relay.Function([], output)
mod['func_15426'] = func_15426
mod = relay.transform.InferType()(mod)
mutated_mod['func_15426'] = func_15426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15426_call = mutated_mod.get_global_var('func_15426')
call_15427 = func_15426_call()
output = call_15427
func_15428 = relay.Function([], output)
mutated_mod['func_15428'] = func_15428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14930_call = mod.get_global_var('func_14930')
func_14932_call = mutated_mod.get_global_var('func_14932')
call_15431 = relay.TupleGetItem(func_14930_call(), 3)
call_15432 = relay.TupleGetItem(func_14932_call(), 3)
func_13592_call = mod.get_global_var('func_13592')
func_13596_call = mutated_mod.get_global_var('func_13596')
var_15440 = relay.var("var_15440", dtype = "float64", shape = (264,))#candidate|15440|(264,)|var|float64
var_15441 = relay.var("var_15441", dtype = "float32", shape = (750,))#candidate|15441|(750,)|var|float32
call_15439 = relay.TupleGetItem(func_13592_call(relay.reshape(var_15440.astype('float64'), [264,]), relay.reshape(var_15441.astype('float32'), [50, 15]), ), 5)
call_15442 = relay.TupleGetItem(func_13596_call(relay.reshape(var_15440.astype('float64'), [264,]), relay.reshape(var_15441.astype('float32'), [50, 15]), ), 5)
output = relay.Tuple([call_15431,call_15439,var_15440,var_15441,])
output2 = relay.Tuple([call_15432,call_15442,var_15440,var_15441,])
func_15458 = relay.Function([var_15440,var_15441,], output)
mod['func_15458'] = func_15458
mod = relay.transform.InferType()(mod)
mutated_mod['func_15458'] = func_15458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15458_call = mutated_mod.get_global_var('func_15458')
var_15460 = relay.var("var_15460", dtype = "float64", shape = (264,))#candidate|15460|(264,)|var|float64
var_15461 = relay.var("var_15461", dtype = "float32", shape = (750,))#candidate|15461|(750,)|var|float32
call_15459 = func_15458_call(var_15460,var_15461,)
output = call_15459
func_15462 = relay.Function([var_15460,var_15461,], output)
mutated_mod['func_15462'] = func_15462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11288_call = mod.get_global_var('func_11288')
func_11290_call = mutated_mod.get_global_var('func_11290')
call_15487 = relay.TupleGetItem(func_11288_call(), 0)
call_15488 = relay.TupleGetItem(func_11290_call(), 0)
output = relay.Tuple([call_15487,])
output2 = relay.Tuple([call_15488,])
func_15496 = relay.Function([], output)
mod['func_15496'] = func_15496
mod = relay.transform.InferType()(mod)
mutated_mod['func_15496'] = func_15496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15496_call = mutated_mod.get_global_var('func_15496')
call_15497 = func_15496_call()
output = call_15497
func_15498 = relay.Function([], output)
mutated_mod['func_15498'] = func_15498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12848_call = mod.get_global_var('func_12848')
func_12850_call = mutated_mod.get_global_var('func_12850')
call_15562 = func_12848_call()
call_15563 = func_12848_call()
func_11220_call = mod.get_global_var('func_11220')
func_11223_call = mutated_mod.get_global_var('func_11223')
call_15567 = relay.TupleGetItem(func_11220_call(relay.reshape(call_15562.astype('float32'), [9, 5, 14])), 0)
call_15568 = relay.TupleGetItem(func_11223_call(relay.reshape(call_15562.astype('float32'), [9, 5, 14])), 0)
output = relay.Tuple([call_15562,call_15567,])
output2 = relay.Tuple([call_15563,call_15568,])
func_15578 = relay.Function([], output)
mod['func_15578'] = func_15578
mod = relay.transform.InferType()(mod)
mutated_mod['func_15578'] = func_15578
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15578_call = mutated_mod.get_global_var('func_15578')
call_15579 = func_15578_call()
output = call_15579
func_15580 = relay.Function([], output)
mutated_mod['func_15580'] = func_15580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11979_call = mod.get_global_var('func_11979')
func_11980_call = mutated_mod.get_global_var('func_11980')
call_15586 = func_11979_call()
call_15587 = func_11979_call()
output = call_15586
output2 = call_15587
func_15594 = relay.Function([], output)
mod['func_15594'] = func_15594
mod = relay.transform.InferType()(mod)
mutated_mod['func_15594'] = func_15594
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15594_call = mutated_mod.get_global_var('func_15594')
call_15595 = func_15594_call()
output = call_15595
func_15596 = relay.Function([], output)
mutated_mod['func_15596'] = func_15596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15084_call = mod.get_global_var('func_15084')
func_15085_call = mutated_mod.get_global_var('func_15085')
call_15610 = relay.TupleGetItem(func_15084_call(), 1)
call_15611 = relay.TupleGetItem(func_15085_call(), 1)
output = relay.Tuple([call_15610,])
output2 = relay.Tuple([call_15611,])
func_15613 = relay.Function([], output)
mod['func_15613'] = func_15613
mod = relay.transform.InferType()(mod)
mutated_mod['func_15613'] = func_15613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15613_call = mutated_mod.get_global_var('func_15613')
call_15614 = func_15613_call()
output = call_15614
func_15615 = relay.Function([], output)
mutated_mod['func_15615'] = func_15615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12653_call = mod.get_global_var('func_12653')
func_12655_call = mutated_mod.get_global_var('func_12655')
call_15639 = func_12653_call()
call_15640 = func_12653_call()
output = relay.Tuple([call_15639,])
output2 = relay.Tuple([call_15640,])
func_15647 = relay.Function([], output)
mod['func_15647'] = func_15647
mod = relay.transform.InferType()(mod)
mutated_mod['func_15647'] = func_15647
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15647_call = mutated_mod.get_global_var('func_15647')
call_15648 = func_15647_call()
output = call_15648
func_15649 = relay.Function([], output)
mutated_mod['func_15649'] = func_15649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12617_call = mod.get_global_var('func_12617')
func_12619_call = mutated_mod.get_global_var('func_12619')
call_15653 = func_12617_call()
call_15654 = func_12617_call()
func_10329_call = mod.get_global_var('func_10329')
func_10333_call = mutated_mod.get_global_var('func_10333')
var_15666 = relay.var("var_15666", dtype = "uint64", shape = (140,))#candidate|15666|(140,)|var|uint64
var_15667 = relay.var("var_15667", dtype = "uint64", shape = (1680,))#candidate|15667|(1680,)|var|uint64
call_15665 = func_10329_call(relay.reshape(var_15666.astype('uint64'), [14, 10, 1]), relay.reshape(var_15667.astype('uint64'), [14, 10, 12]), )
call_15668 = func_10329_call(relay.reshape(var_15666.astype('uint64'), [14, 10, 1]), relay.reshape(var_15667.astype('uint64'), [14, 10, 12]), )
output = relay.Tuple([call_15653,call_15665,var_15666,var_15667,])
output2 = relay.Tuple([call_15654,call_15668,var_15666,var_15667,])
func_15669 = relay.Function([var_15666,var_15667,], output)
mod['func_15669'] = func_15669
mod = relay.transform.InferType()(mod)
var_15670 = relay.var("var_15670", dtype = "uint64", shape = (140,))#candidate|15670|(140,)|var|uint64
var_15671 = relay.var("var_15671", dtype = "uint64", shape = (1680,))#candidate|15671|(1680,)|var|uint64
output = func_15669(var_15670,var_15671,)
func_15672 = relay.Function([var_15670,var_15671,], output)
mutated_mod['func_15672'] = func_15672
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11305_call = mod.get_global_var('func_11305')
func_11307_call = mutated_mod.get_global_var('func_11307')
call_15700 = func_11305_call()
call_15701 = func_11305_call()
func_15174_call = mod.get_global_var('func_15174')
func_15176_call = mutated_mod.get_global_var('func_15176')
call_15717 = func_15174_call()
call_15718 = func_15174_call()
output = relay.Tuple([call_15700,call_15717,])
output2 = relay.Tuple([call_15701,call_15718,])
func_15721 = relay.Function([], output)
mod['func_15721'] = func_15721
mod = relay.transform.InferType()(mod)
output = func_15721()
func_15722 = relay.Function([], output)
mutated_mod['func_15722'] = func_15722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12653_call = mod.get_global_var('func_12653')
func_12655_call = mutated_mod.get_global_var('func_12655')
call_15777 = func_12653_call()
call_15778 = func_12653_call()
output = relay.Tuple([call_15777,])
output2 = relay.Tuple([call_15778,])
func_15795 = relay.Function([], output)
mod['func_15795'] = func_15795
mod = relay.transform.InferType()(mod)
mutated_mod['func_15795'] = func_15795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15795_call = mutated_mod.get_global_var('func_15795')
call_15796 = func_15795_call()
output = call_15796
func_15797 = relay.Function([], output)
mutated_mod['func_15797'] = func_15797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14330_call = mod.get_global_var('func_14330')
func_14332_call = mutated_mod.get_global_var('func_14332')
call_15828 = func_14330_call()
call_15829 = func_14330_call()
func_15613_call = mod.get_global_var('func_15613')
func_15615_call = mutated_mod.get_global_var('func_15615')
call_15844 = relay.TupleGetItem(func_15613_call(), 0)
call_15845 = relay.TupleGetItem(func_15615_call(), 0)
func_12065_call = mod.get_global_var('func_12065')
func_12067_call = mutated_mod.get_global_var('func_12067')
call_15846 = relay.TupleGetItem(func_12065_call(), 0)
call_15847 = relay.TupleGetItem(func_12067_call(), 0)
func_2225_call = mod.get_global_var('func_2225')
func_2228_call = mutated_mod.get_global_var('func_2228')
var_15863 = relay.var("var_15863", dtype = "uint32", shape = ())#candidate|15863|()|var|uint32
var_15864 = relay.var("var_15864", dtype = "uint32", shape = (24,))#candidate|15864|(24,)|var|uint32
call_15862 = func_2225_call(relay.reshape(var_15863.astype('uint32'), []), relay.reshape(var_15864.astype('uint32'), [12, 1, 2]), )
call_15865 = func_2225_call(relay.reshape(var_15863.astype('uint32'), []), relay.reshape(var_15864.astype('uint32'), [12, 1, 2]), )
func_11358_call = mod.get_global_var('func_11358')
func_11362_call = mutated_mod.get_global_var('func_11362')
var_15869 = relay.var("var_15869", dtype = "uint64", shape = (130,))#candidate|15869|(130,)|var|uint64
call_15868 = relay.TupleGetItem(func_11358_call(relay.reshape(var_15863.astype('uint32'), []), relay.reshape(var_15869.astype('uint64'), [130,]), ), 4)
call_15870 = relay.TupleGetItem(func_11362_call(relay.reshape(var_15863.astype('uint32'), []), relay.reshape(var_15869.astype('uint64'), [130,]), ), 4)
func_14457_call = mod.get_global_var('func_14457')
func_14458_call = mutated_mod.get_global_var('func_14458')
call_15898 = func_14457_call()
call_15899 = func_14457_call()
output = relay.Tuple([call_15828,call_15844,call_15846,call_15862,var_15863,var_15864,call_15868,var_15869,call_15898,])
output2 = relay.Tuple([call_15829,call_15845,call_15847,call_15865,var_15863,var_15864,call_15870,var_15869,call_15899,])
func_15911 = relay.Function([var_15863,var_15864,var_15869,], output)
mod['func_15911'] = func_15911
mod = relay.transform.InferType()(mod)
var_15912 = relay.var("var_15912", dtype = "uint32", shape = ())#candidate|15912|()|var|uint32
var_15913 = relay.var("var_15913", dtype = "uint32", shape = (24,))#candidate|15913|(24,)|var|uint32
var_15914 = relay.var("var_15914", dtype = "uint64", shape = (130,))#candidate|15914|(130,)|var|uint64
output = func_15911(var_15912,var_15913,var_15914,)
func_15915 = relay.Function([var_15912,var_15913,var_15914,], output)
mutated_mod['func_15915'] = func_15915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14375_call = mod.get_global_var('func_14375')
func_14376_call = mutated_mod.get_global_var('func_14376')
call_15935 = relay.TupleGetItem(func_14375_call(), 0)
call_15936 = relay.TupleGetItem(func_14376_call(), 0)
output = relay.Tuple([call_15935,])
output2 = relay.Tuple([call_15936,])
func_15937 = relay.Function([], output)
mod['func_15937'] = func_15937
mod = relay.transform.InferType()(mod)
mutated_mod['func_15937'] = func_15937
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15937_call = mutated_mod.get_global_var('func_15937')
call_15938 = func_15937_call()
output = call_15938
func_15939 = relay.Function([], output)
mutated_mod['func_15939'] = func_15939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15578_call = mod.get_global_var('func_15578')
func_15580_call = mutated_mod.get_global_var('func_15580')
call_15948 = relay.TupleGetItem(func_15578_call(), 1)
call_15949 = relay.TupleGetItem(func_15580_call(), 1)
func_11833_call = mod.get_global_var('func_11833')
func_11835_call = mutated_mod.get_global_var('func_11835')
call_15962 = relay.TupleGetItem(func_11833_call(), 0)
call_15963 = relay.TupleGetItem(func_11835_call(), 0)
func_11833_call = mod.get_global_var('func_11833')
func_11835_call = mutated_mod.get_global_var('func_11835')
call_15980 = relay.TupleGetItem(func_11833_call(), 0)
call_15981 = relay.TupleGetItem(func_11835_call(), 0)
output = relay.Tuple([call_15948,call_15962,call_15980,])
output2 = relay.Tuple([call_15949,call_15963,call_15981,])
func_15992 = relay.Function([], output)
mod['func_15992'] = func_15992
mod = relay.transform.InferType()(mod)
mutated_mod['func_15992'] = func_15992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15992_call = mutated_mod.get_global_var('func_15992')
call_15993 = func_15992_call()
output = call_15993
func_15994 = relay.Function([], output)
mutated_mod['func_15994'] = func_15994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11742_call = mod.get_global_var('func_11742')
func_11744_call = mutated_mod.get_global_var('func_11744')
call_16027 = func_11742_call()
call_16028 = func_11742_call()
output = call_16027
output2 = call_16028
func_16030 = relay.Function([], output)
mod['func_16030'] = func_16030
mod = relay.transform.InferType()(mod)
output = func_16030()
func_16031 = relay.Function([], output)
mutated_mod['func_16031'] = func_16031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15174_call = mod.get_global_var('func_15174')
func_15176_call = mutated_mod.get_global_var('func_15176')
call_16059 = func_15174_call()
call_16060 = func_15174_call()
func_15937_call = mod.get_global_var('func_15937')
func_15939_call = mutated_mod.get_global_var('func_15939')
call_16069 = relay.TupleGetItem(func_15937_call(), 0)
call_16070 = relay.TupleGetItem(func_15939_call(), 0)
func_10179_call = mod.get_global_var('func_10179')
func_10182_call = mutated_mod.get_global_var('func_10182')
const_16089 = relay.const([10,2,7,-5,5,6,5,8,3,2,2,9,-6,-6,-1,-7,8,-8,9,-3,-1,-2,-2,6,4,-5,7,-2,8,1,-8,-2,-8,-1,-6,-3,3,5,6,3,1,-8,-4,1,-8,-3,3,-3,6,9,-8,10,6,7,9,3,7,-8,2,3,6,-8,-1,-1,5,-10,-2,4,-10,-1,-10,10,-4,8,-10,7,7,6,-6,-5,-6,-4,9,-4,1,-7,10,6,-6,1,5,3,-1,2,-3,-8,3,-5,2,-9,-7,-3,6,2,-6,-9,8,5,-10,-9,-3,3,-1,-8,10,-5,8,5,-9,-5,9,-8,-7,-10,-9,9,6,-1,2,9,9,-10,-3,-10,-3,7,-10,-3,-9,1,2,3,-3,2,-4,-7,4,-1,-6,9,-7,-3,5,-3,9,-4,5,6,10,5,-8,8,-4,10,1,9,-10,-6,-8,-7,2,-7,-9,-8,4,4,8,5,2,-1,-5,-4,3,-7,-8,10,-8,-10,4,7,-1,-8,-2,2,8,-10,4,-7,-1,-7,-3,-10,6,9,7,-5,-4,9,8,3,-5,-1,6,-3,6,-7,-9,-1,6,-4,-5,-1,-4,6,-2,-9,3,-3,10,7,7,7,10,10,8,-1,3,-2,4,10,-9,4,-1,-1,4,10,-2,9,5,-10,-3,5,-4,-4,7,6,-5,7,9,10,8,9,7,3,-7,-4,-3,8,-6,-6,8,-8,-2,2,5,-7,2,-4,-3,-10,10,-1,-2,2,3,10,2,6,-5,9,2,4,1,-4,4,5,7,9,-6,9,3,-3,-9,10,9,3,-5,-7,6,-1,5,-6,-3,-2,-8,-10,-10,5,-4,-3,-4,6,5,6,-5,2,2,-2,5,-5,7,-3,6,6,4,-3,-6,-6,2,-2,8,7,-4,-6,-7,1,4,-10,-3,-2,-8,5,-6,4,-4,5,4,3,-4,-6,-10,4,-2,-8,-1,-4,-7,-2,2,9,6,-10,-9,-8,-4,4,9,7,2,-6,6,-3,-9,-4,-5,-8,10,-1,1,-3,-2,-8,-7,-4,-2,4,-2,-1,-4,-3,1,-9,-7,1,8,4,3,2,-7,-6,1,-7,9,-4,-4,-1,8,7,8,5,3,7,1,3,10,-7,1,1,-3,-10,-4,3,1,-9,-9,7,6,-8,-5,-3,10,5,-3,1,3,-4,-4,-9,8,-4,-4,8,6,5,7,-8,9,10,10,-9,-7,-10,-9,-8,8,-5,-4,2,-9,1,6,-4,-3,-8,-10,-3,-9,7,-1,6,-6,4,4,-10,-5,-10,2,-8,10,5,-1,6,3,-10,8,-6,5,-6,5,1,-1,-3,-4,-8,-4,-4,-5,-7,-4,3,-2,-8,-8,-7,2,-7,10,-6,8,9,-10,1,3,-2,-6,1,-5,-7,3,7,6,6,3,-10,-7,5,4,-3,-3,-6,-1,6,-5,-8,-1,-2,1,10,-2,-7,1,-6,-7,6,3,10,8,-9,-1,9,-4,-8,1,-8,-10,1,6,-8,6,6,5,-3,-2,-8,-9,-4,10,-7,9,3,10,-3,-1,3,5,7,3,-7,-2,7,-1,-2,2,3,7,-5,10,-5,-8,-6,-8,-7,3,-6,-6,-4,-6,2,-10,-3,1,-1,-3,1,7,-8,-2,-5,-6,10,6,3,-4,1,-9,8,2,2,10,-9,-3,-9,10,2,7,-10,-7,6,-7,5,3,6,7,-1,3,1,4,3,-5,2,6,-8,4,-6,3,6,7,9,2,-8,-7,9,10,-7,-6,1,-10,6,-3,4,-4,-9,-4,4,8,9,4,9,1,-10,-5,-8,10,-1,-6,6,-7,10,3,7,7,-7,5,6,-1,2,9,-5,4,1,-2,10,2,-1,4,-8,-4,-4,2,3,-8,1,7,-6,1,10,2,1,10,3,-9,-8,6,2,-4,1,-1,9,8,10,-1,-1,2,9,5,7,2,9,-7,-6,-7,1,1,8,3,9,8,-9,5,2,9,-5,3,9,-6,-9,3,-1,-1,-4,-4,-10,-4,-3,-6,-6,-4,-6,-7,-7,9,4,-7,6,3,-4,-10,1,1,2,9,-2,1,10,-2,-10,4,-5,-10,-10,-9,-4,-7,5,-1,7,5,2,5,5,-10,10,-9,-4,-4,-6,9,5,4,-5,-7,4,-2,-1,10,-6,-10,-4,-1,-10,3,9,-3,-9,4,-2,6,4,-4,-5,-10,-5,-7,-9,-9,3,-4,-3,7,-6,6,2,5,10,-3,-4,-5,-3,-1,-1,3,2,8,-6,7,-6,1,-7,-7,8,1,3,2,-10,-8,1,7,-9,-9,10,9,1,5,8,4,-2,-7,-2,-10,-2,-5,10,-6,-9,-3,3,6,-4,3,-2,10,-1,-8,-6,5,-7,-2,-4,-3,5,3,-10,3,1,7,-2,-9,2,6,-6,-7,-5,9,7,-4,9,-2,8,2,1,3,4,6,1,-7,5,9,3,9,9,-4,-3,-5,2,-10,-7,-8,-7,9,8,-5,10,-5,2,-2,-1,9,-3,-5,-4,-9,10,-3,4,4,-10,9,5,-2,9,-7,-10,-4,-3,-7,-6,9,4,4,4,1,9,3,-3,-10,-8,-5,-5,3,-10,6,-9,-3,-5,-2,-4,-4,-1,8,1,-8,-7,1,-2,2,7,7,1,10,6,8,2,-5,-10,-9,-1,1,-8,1,-7,3,1,9,-1,-1,-10,6,-2,7,4,-10,-2,6,-5,1,10,-5,5,6,-4,2,-5,-6,-9,-6,10,1,-8,4,-2,5,-1,6,6,-2,6,-6,2,7,-6,8,10,8,4,3,-6,-1,-1,-3,-6,1,8,-4,-9,6,7,-3,-3,7,4,-5,-10,-7,3,2,-4,-3,8,5,-2,5,4,6,-1,-5,5,-5,-8,8,4,-1,2], dtype = "uint16")#candidate|16089|(1092,)|const|uint16
call_16088 = relay.TupleGetItem(func_10179_call(relay.reshape(const_16089.astype('uint16'), [6, 13, 14])), 0)
call_16090 = relay.TupleGetItem(func_10182_call(relay.reshape(const_16089.astype('uint16'), [6, 13, 14])), 0)
func_15613_call = mod.get_global_var('func_15613')
func_15615_call = mutated_mod.get_global_var('func_15615')
call_16091 = relay.TupleGetItem(func_15613_call(), 0)
call_16092 = relay.TupleGetItem(func_15615_call(), 0)
output = relay.Tuple([call_16059,call_16069,call_16088,const_16089,call_16091,])
output2 = relay.Tuple([call_16060,call_16070,call_16090,const_16089,call_16092,])
func_16094 = relay.Function([], output)
mod['func_16094'] = func_16094
mod = relay.transform.InferType()(mod)
output = func_16094()
func_16095 = relay.Function([], output)
mutated_mod['func_16095'] = func_16095
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14127_call = mod.get_global_var('func_14127')
func_14129_call = mutated_mod.get_global_var('func_14129')
call_16181 = relay.TupleGetItem(func_14127_call(), 2)
call_16182 = relay.TupleGetItem(func_14129_call(), 2)
output = relay.Tuple([call_16181,])
output2 = relay.Tuple([call_16182,])
func_16188 = relay.Function([], output)
mod['func_16188'] = func_16188
mod = relay.transform.InferType()(mod)
mutated_mod['func_16188'] = func_16188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16188_call = mutated_mod.get_global_var('func_16188')
call_16189 = func_16188_call()
output = call_16189
func_16190 = relay.Function([], output)
mutated_mod['func_16190'] = func_16190
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14750_call = mod.get_global_var('func_14750')
func_14752_call = mutated_mod.get_global_var('func_14752')
call_16194 = relay.TupleGetItem(func_14750_call(), 1)
call_16195 = relay.TupleGetItem(func_14752_call(), 1)
output = relay.Tuple([call_16194,])
output2 = relay.Tuple([call_16195,])
func_16198 = relay.Function([], output)
mod['func_16198'] = func_16198
mod = relay.transform.InferType()(mod)
mutated_mod['func_16198'] = func_16198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16198_call = mutated_mod.get_global_var('func_16198')
call_16199 = func_16198_call()
output = call_16199
func_16200 = relay.Function([], output)
mutated_mod['func_16200'] = func_16200
mutated_mod = relay.transform.InferType()(mutated_mod)
const_16270 = relay.const([[[2.617741,2.268598,6.194072,-7.732223,0.647759,6.487365,0.437177,4.477382,3.846612,9.698382,-2.459705]]], dtype = "float64")#candidate|16270|(1, 1, 11)|const|float64
var_16271 = relay.var("var_16271", dtype = "float64", shape = (3, 9, 11))#candidate|16271|(3, 9, 11)|var|float64
bop_16272 = relay.floor_mod(const_16270.astype('float64'), var_16271.astype('float64')) # shape=(3, 9, 11)
bop_16280 = relay.greater(bop_16272.astype('bool'), const_16270.astype('bool')) # shape=(3, 9, 11)
uop_16284 = relay.rsqrt(const_16270.astype('float32')) # shape=(1, 1, 11)
output = relay.Tuple([bop_16280,uop_16284,])
output2 = relay.Tuple([bop_16280,uop_16284,])
func_16286 = relay.Function([var_16271,], output)
mod['func_16286'] = func_16286
mod = relay.transform.InferType()(mod)
var_16287 = relay.var("var_16287", dtype = "float64", shape = (3, 9, 11))#candidate|16287|(3, 9, 11)|var|float64
output = func_16286(var_16287)
func_16288 = relay.Function([var_16287], output)
mutated_mod['func_16288'] = func_16288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13402_call = mod.get_global_var('func_13402')
func_13404_call = mutated_mod.get_global_var('func_13404')
call_16314 = relay.TupleGetItem(func_13402_call(), 5)
call_16315 = relay.TupleGetItem(func_13404_call(), 5)
output = call_16314
output2 = call_16315
func_16338 = relay.Function([], output)
mod['func_16338'] = func_16338
mod = relay.transform.InferType()(mod)
output = func_16338()
func_16339 = relay.Function([], output)
mutated_mod['func_16339'] = func_16339
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15046_call = mod.get_global_var('func_15046')
func_15047_call = mutated_mod.get_global_var('func_15047')
call_16419 = relay.TupleGetItem(func_15046_call(), 0)
call_16420 = relay.TupleGetItem(func_15047_call(), 0)
func_15174_call = mod.get_global_var('func_15174')
func_15176_call = mutated_mod.get_global_var('func_15176')
call_16426 = func_15174_call()
call_16427 = func_15174_call()
func_12381_call = mod.get_global_var('func_12381')
func_12384_call = mutated_mod.get_global_var('func_12384')
call_16431 = relay.TupleGetItem(func_12381_call(relay.reshape(call_16419.astype('float32'), [9, 5, 14])), 0)
call_16432 = relay.TupleGetItem(func_12384_call(relay.reshape(call_16419.astype('float32'), [9, 5, 14])), 0)
func_13782_call = mod.get_global_var('func_13782')
func_13785_call = mutated_mod.get_global_var('func_13785')
const_16448 = relay.const([[-3.652116,7.648921,0.100006,6.693238,5.074897,3.580576,8.768661,-1.476027,-9.897593,8.337705,2.462706,3.339383,-4.988930,-2.263120,0.627863,4.457974,-3.703863,-7.028247,-6.100208,-1.686879,-2.713035,-0.699549,4.367679,3.793957,-7.763065,-0.791096,-2.619082,-9.016966,-1.512605,2.756962,5.155486,8.481694,9.237779,4.660147,3.838425,2.342434,-1.228801,-7.544606,4.984855,2.384090],[-9.495824,4.326577,7.031159,-0.854957,-1.920843,6.960198,-6.355961,0.208164,-9.048582,4.619155,5.705955,-8.013255,-7.614247,5.529233,-9.721142,-3.266170,8.435322,6.955044,2.700117,-2.151714,3.198854,1.212038,7.733967,-1.120316,-6.532274,1.293885,-7.791898,0.690970,-2.086696,-1.797366,8.577161,-6.814896,-4.265172,-2.879651,2.364191,6.215141,-5.274994,-9.666715,-2.776238,-3.245823],[-6.946952,-5.866027,2.970703,1.826792,-2.454124,-1.628458,-7.960181,-3.052378,9.223884,-9.599677,-5.572667,8.536503,1.580097,-1.371913,-3.094489,-3.324816,-3.143850,-8.835710,-5.923114,-6.484478,6.207270,-9.652203,5.147036,4.939474,1.920018,6.059886,8.618569,8.131082,-3.481138,-9.843611,-4.093196,7.156886,7.367004,-0.971961,6.246276,6.791735,4.455335,6.470673,-4.937249,9.037790],[-2.578542,6.789856,-0.672492,-0.857933,-0.716364,7.514378,5.847301,-9.865591,-1.470288,-1.520139,4.343132,3.733401,-9.866401,1.825663,0.012557,-5.971005,1.912673,7.484522,-8.864084,-9.459251,9.501601,5.748457,-1.383535,2.359613,-8.871026,-1.040563,3.277654,8.192120,-1.594922,1.666292,8.080599,-0.845844,1.152288,-2.357594,1.978240,9.946142,8.519791,-5.782767,-4.675036,-9.292549],[4.712514,-6.307288,-0.546362,-2.591624,-2.554902,-6.404598,-1.513523,-4.720754,5.516707,6.769502,8.214822,1.312190,-0.106135,-8.883131,5.664109,2.760486,8.671558,-1.333235,8.821658,0.801974,-3.021870,-5.162747,-5.759308,-9.841328,8.807988,-1.107041,-8.787322,4.317460,9.447197,6.773122,7.973756,-0.136464,-7.762056,-4.815041,5.828900,2.793054,-2.339686,-4.216107,-9.256644,-8.244233],[5.510626,-3.874633,-3.307970,-3.390341,0.414361,-8.432186,-5.139871,-1.898648,5.917741,7.560511,-0.623520,-7.790332,-3.140343,5.487434,-5.303499,-9.980646,-0.433981,3.239414,3.881001,6.857282,-5.999884,0.021710,-0.789227,9.928497,-2.713130,-0.910112,-9.985231,4.298566,-3.831631,9.205496,-2.261178,-0.584993,6.764615,9.093617,0.975556,7.842065,5.652277,-2.058090,-5.486897,7.890351],[-5.567477,0.085195,1.130100,7.408400,5.119213,-3.913477,5.675198,8.759449,-2.451726,0.847691,2.281201,2.258080,8.747963,-6.719237,-8.412786,-7.465066,4.631771,5.575766,8.326580,-4.910505,7.497401,-3.023167,1.588570,6.723983,9.489536,4.367016,-8.528226,0.050769,1.907643,2.614603,8.505804,-2.362117,-1.568763,8.331343,3.042860,-5.874355,-9.791477,0.120365,-8.647116,-0.408173],[2.240940,-9.234021,-2.026778,2.909939,0.446206,2.842102,-4.969403,-4.849018,8.653340,-9.310504,9.925920,-0.335689,-6.703965,-9.319482,-9.641606,-8.521417,-5.760634,9.416313,-8.278697,-5.620447,-4.607624,-2.231736,-2.141165,2.986806,0.414445,-0.102372,-9.541476,-5.731844,-9.412225,-2.707657,8.859129,-4.667624,8.876647,3.395730,-8.829672,-7.400025,9.186164,9.742844,7.347954,-0.681753]], dtype = "float64")#candidate|16448|(8, 40)|const|float64
call_16447 = relay.TupleGetItem(func_13782_call(relay.reshape(const_16448.astype('float64'), [8, 5, 8])), 1)
call_16449 = relay.TupleGetItem(func_13785_call(relay.reshape(const_16448.astype('float64'), [8, 5, 8])), 1)
func_14417_call = mod.get_global_var('func_14417')
func_14418_call = mutated_mod.get_global_var('func_14418')
call_16451 = relay.TupleGetItem(func_14417_call(), 0)
call_16452 = relay.TupleGetItem(func_14418_call(), 0)
func_5306_call = mod.get_global_var('func_5306')
func_5309_call = mutated_mod.get_global_var('func_5309')
const_16479 = relay.const([-4,-3,-4,-2,5,6,-5,-3,9,5,-7,-10,3,-5,3,-4,-8,7,1,4,9,7,6,7,3,5,4,-7,5,3,-1,-6,3,2,3,9,-7,-5,6,8,5,-9,9,7,7,1,-8,-6,2,-4,3,4,4,3,-3,-9,-4,-9,-6,6,-6,-1,6,5,5,-3,-5,-8,-6,8,2,8,-8,9,-3,7,-6,4,-6,-1,10,-9,9,-3,6,4,1,-4,-1,2,1,-5,-8,8,10,4,1,5,9,-7,-1,3,-7,10,-1,3,-2,9,-7,-3,-6,7,8,-1,9,-4,-1,10,-5,7,3,-9,8,6,-5,-2,-5,10,10,2], dtype = "uint64")#candidate|16479|(130,)|const|uint64
const_16480 = relay.const([10,2,-9,10,-2,6,1,-7,9,5,-5,-2,-6,8,4,2,1,-3,9,-8,10,2,8,-6,5,10,-2,7,-5,-3,-6,2,-1,10,8,-2,-2,8,6,-6,-7,-1,9,6,4,-4,8,-6,10,-8,-3,-7,-5,-6,-2,9,1,8,-7,5,-6,10,4,3,-3,2,-1,1,-7,4,1,9,-3,-1,3,-10,4,3,7,2,6,5,5,1,5,1,9,8,-7,2,3,-9,1,5,-9,-7,-10,-4,10,-7,3,1,-6,-5,7,2,-9,-9,2,-10,10,8,2,7,9,7,1,-3,-8,-1,6,-5,4,-7,7,-1,-5,-10,-3,8,-2,2,-4,4,5,-7,1,-10,-7,3,-2,-4,3,5,3,-8,8,-10,-6,6,-2,-6,6,-5,-1,-8,5,4,-6,-4], dtype = "uint64")#candidate|16480|(160,)|const|uint64
call_16478 = relay.TupleGetItem(func_5306_call(relay.reshape(const_16479.astype('uint64'), [130,]), relay.reshape(const_16480.astype('uint64'), [160,]), ), 0)
call_16481 = relay.TupleGetItem(func_5309_call(relay.reshape(const_16479.astype('uint64'), [130,]), relay.reshape(const_16480.astype('uint64'), [160,]), ), 0)
func_13858_call = mod.get_global_var('func_13858')
func_13859_call = mutated_mod.get_global_var('func_13859')
call_16486 = func_13858_call()
call_16487 = func_13858_call()
func_13592_call = mod.get_global_var('func_13592')
func_13596_call = mutated_mod.get_global_var('func_13596')
var_16509 = relay.var("var_16509", dtype = "float64", shape = (1, 264))#candidate|16509|(1, 264)|var|float64
const_16510 = relay.const([[-3.162422,5.357949,-0.567903,3.850942,-0.684655,7.233931,5.943486,-7.580394,4.975956,8.485361,-5.984100,6.833093,-0.732330,2.199586,-9.173851,2.320281,-4.418968,4.704550,6.187324,-0.780439,-1.855736,-4.735766,3.856514,4.615556,-9.465920,-4.344637,-0.685625,-2.128098,-5.281400,8.265817,-5.856510,7.875298,-9.140902,9.819974,7.448559,3.047470,-0.339476,-5.329633,-3.926580,-7.787834,-1.740372,-8.347375,6.385588,5.029975,-7.534000,-3.674989,9.098783,-1.897467,-4.324843,5.711507,5.378033,-3.235545,4.124566,4.740843,-3.398609,-8.741891,-3.941557,-1.166164,1.292246,7.398357,-4.881199,3.074234,-8.460139,3.176208,8.883365,-4.246497,7.325402,-2.978616,3.492089,3.945966,-3.132341,-8.981776,-3.517179,-2.881899,8.062298,2.980449,3.452940,8.443220,-3.696886,5.957916,-3.332234,-6.931939,-7.381697,-2.333014,-2.321326,4.071348,8.386809,6.806832,-3.157339,1.332725,-0.870041,-8.841042,6.371272,8.311128,-1.552710,-3.765675,-1.909097,0.521473,1.857870,2.159230,2.322387,-2.356512,-7.780996,-6.272009,4.136271,-8.817779,-9.533639,-0.331407,7.587011,-1.706203,-4.215737,-1.442897,6.358165,9.214563,0.311159,4.108238,6.355666,5.812042,1.884368,0.904026,6.566283,-3.159680,-2.988454,-7.559053,-9.807683,2.631161,2.574676,-8.202696,6.187698,5.906447,-9.876692,6.640183,9.119429,5.390061,-0.142784,1.491766,6.772638,-5.287305,-2.405775,3.343859,8.237334,3.809453,-8.135348,9.502620,7.520533,-4.996064,5.874872,-8.125320,-9.154502,-4.799236,-8.641184,-7.217164,6.461979,0.503473,4.902748,8.712480,8.355526,0.216241,-4.238304,-2.522811,-5.469209,2.296730,-3.544728,-2.969632,6.445684,-3.193610,-2.762604,9.224600,9.080850,-5.518822,7.625361,9.423202,-5.666604,-9.608559,5.629487,4.439973,4.843177,-4.524391,-1.687563,-9.411163,9.715796,8.090575,-7.508026,2.080166,7.597831,-5.655468,8.615107,3.386222,1.603161,-6.799893,-2.414270,-8.285331,-4.013871,-9.968957,1.868355,0.498024,8.402763,-3.740782,6.376449,1.507191,8.242004,-3.515823,7.057231,6.906757,8.259270,4.361111,4.646806,-2.704396,-8.383373,-4.244854,5.002716,-4.416348,-7.004649,-4.239126,7.370337,-3.501755,-3.533353,1.920238,-3.920869,-3.028733,5.675181,-5.811162,3.241257,-8.054068,4.151315,8.001158,-3.194988,2.255808,-7.180589,2.689717,6.741433,6.161668,-9.465393,9.476633,4.360080,-5.807391,1.145300,1.910063,5.370718,7.892522,-2.495657,-4.724003,-6.020460,8.953670,4.157849,-8.859976,-1.030279,-2.845428,5.145980,8.681595,0.834190,9.365213,-0.498447,9.882781,-6.395777,-2.261220,1.244836,-0.112511,-8.829482,1.705762,-1.260720,-8.643322,3.953470,8.748674,-2.175804,1.580818,-2.673273,8.892000,5.647140,4.443289,9.622872,-7.183645,-1.312008,-0.717236,-4.673626,-2.922766,-3.280519,2.806070,-8.910833,-7.982817,7.535978,-8.141228,-0.216940,8.165750,4.404259,5.129924,-3.567399,0.433651,-4.195723,-5.127223,0.466905,1.291352,7.609717,8.097485,6.405404,0.874203,6.559854,0.889253,7.982811,6.283971,3.753449,4.050810,-3.288361,-0.710358,-8.796746,5.439524,1.592681,6.025197,9.706682,-8.406901,-6.758568,-5.210529,-5.638185,3.698364,-1.758903,-4.635754,-5.383599,9.068313,-5.156136,2.768116,-5.264143,8.104339,-3.666353,7.721924,4.470194,-2.655068,2.444137,-6.557552,-2.219268,0.182791,-0.231274,-9.138822,2.871499,-3.808995,3.509280,-5.396850,-6.711657,-3.662939,5.514874,9.970399,1.219106,-9.186270,-3.269926,-7.237943,9.485884,7.741913,4.514515,-9.872526,2.314164,3.314682,-4.884842,2.086992,0.720439,9.248947,7.115423,8.788581,4.632440,7.985865,-6.080771,-1.184327,1.091801,-2.488120,-1.090362,2.376481,3.757447,-5.398156,-3.750840,-4.070511,8.707130,-4.876754,-2.316843,-3.428760,-7.240830,7.408461,3.135411,-0.499029,1.439228,-0.138267,8.835274,-4.686200,-9.304099,-3.138968,-8.712900,-3.382043,2.647276,-4.847111,-8.471931,5.817496,-7.729500,-4.268384,-1.641433,-3.490317,8.066416,0.742171,-6.935765,3.417942,1.486503,9.174265,-9.250726,6.828389,5.268298,-9.870567,-0.165930,-9.252848,-6.300301,5.420986,2.523357,4.812166,-6.193449,2.391062,-6.210174,5.939275,-2.747160,7.864784,-9.013869,-2.190285,-9.024499,0.691351,-5.005111,2.514327,-7.430713,-8.071682,-8.782247,-0.669590,-9.483798,2.582062,-0.547449,-8.418129,9.777254,-9.483909,8.973234,1.622347,4.351704,-5.908909,-0.001250,-3.725002,-1.037642,-9.404351,-9.733550,5.941049,-5.783955,5.438208,1.212176,-3.880741,9.976997,-3.447125,3.398998,-1.853016,8.973156,0.158614,-6.315697,-7.290148,-5.814207,2.742015,-6.058891,4.068641,7.815563,4.990455,5.516954,-5.148477,-5.856974,9.275345,-9.516617,-7.252715,-8.957485,-8.685140,-4.743147,-6.024651,3.206808,3.544442,-9.800066,5.296457,-3.940347,3.146193,-1.313404,-3.884350,-0.648770,-1.478009,-9.552297,-2.120809,-3.377017,9.169826,-5.710635,7.473470,-5.674711,1.743865,-6.667904,-5.740421,8.020651,-2.938107,6.392503,2.180872,-4.747096,8.688789,-0.837159,3.056996,-1.156097,9.016821,-5.660022,-0.658285,-3.973798,-7.496943,-9.900334,8.044585,-6.206120,1.967665,-1.656608,5.794143,9.468472,2.542677,8.002792,-2.339016,-7.115151,-8.701630,2.124016,9.175066,-7.539601,-1.392944,-2.266747,-3.193717,3.273281,5.336510,-7.815359,-8.442623,6.783819,-7.631741,-1.462524,-1.480623,-7.039716,-4.223947,9.617217,4.078447,8.413881,0.031146,3.710813,-2.278550,6.356746,8.549322,-9.450857,9.296789,5.632726,-9.858910,5.259012,-5.315431,6.965590,5.067838,-8.005922,-9.752111,-3.489056,-6.698460,-3.524546,-3.339468,-0.168453,9.163277,5.320508,-5.695138,-6.922076,-4.758050,3.238420,-4.852407,2.602804,0.901987,-9.558639,4.141329,4.287480,8.651667,-4.054462,-0.536244,7.774142,-3.297330,-2.841300,5.105244,4.296895,-5.097241,8.920730,-1.263840,-5.538888,-0.352011,9.450070,5.501059,4.783811,-3.905088,-7.619157,-6.705039,2.729219,-2.716814,4.066313,-3.444526,-8.845433,3.695646,3.169240,-8.190741,-9.593255,4.352404,2.288469,-8.311717,8.964275,-4.992705,2.733046,8.192463,0.222788,5.576669,6.871026,-0.241318,-9.850276,5.008502,5.730542,-0.971136,3.035002,5.037503,-8.047956,6.747496,3.858623,-5.743411,7.809768,2.376603,7.842509,9.854800,-0.378863,-8.016341,-2.444598,3.528929,-5.298085,3.231803,8.326211,-3.932373,-8.618511,1.642922,4.945758,0.098897,4.547499,-8.824439,4.738153,6.526731,1.247794,-9.931133,-4.622613,3.938589,5.472756,-9.363278,8.786582,9.854628,-7.031863,7.678576,-1.094153,-9.906077,1.478075,-0.045647,4.816149,9.794966,-6.227340,-4.280999,9.094481,7.031541,-6.578835,8.934117,-2.322637,4.215703,5.237992,-3.221839,0.596136,3.324971,2.044901,8.752504,0.101256,3.962376,8.227904,-9.128264,1.347471,8.297732,6.410819,-7.481193,1.555167,2.018441,-8.750024,-8.745859,-7.180803,9.087240,-7.040391,-6.212421,9.974707,4.843712,8.710979,9.597868,9.760789,-2.883784,2.689797,-3.157994,8.702970,9.150484,6.256872,2.915727,4.713195,-3.249137,-7.564783,6.125842,-9.517072,-4.079352,9.823071,9.303325,-1.845372,6.279740,-0.352408,8.938052,1.390006,5.309919,-9.305442,9.189233,5.351861,8.096366,-6.136035,1.735462,6.629849,5.983997,8.130015,1.664270,-3.165489,6.410635,-6.399464,-6.430520,1.700189,2.337635,7.192444,3.321134,-8.148420,-7.219951,-1.203962,5.952655,0.284160,-5.770955,1.035350,-2.227421,-3.226863,-0.508996,-7.383454,4.974216,4.567295,-4.025823,8.195913,0.961094,-8.488961,-8.821966,-3.468427,7.909725,-1.841305,-9.851878,9.039124,-1.081565,1.821135,4.394983]], dtype = "float32")#candidate|16510|(1, 750)|const|float32
call_16508 = relay.TupleGetItem(func_13592_call(relay.reshape(var_16509.astype('float64'), [264,]), relay.reshape(const_16510.astype('float32'), [50, 15]), ), 1)
call_16511 = relay.TupleGetItem(func_13596_call(relay.reshape(var_16509.astype('float64'), [264,]), relay.reshape(const_16510.astype('float32'), [50, 15]), ), 1)
output = relay.Tuple([call_16419,call_16426,call_16431,call_16447,const_16448,call_16451,call_16478,const_16479,const_16480,call_16486,call_16508,var_16509,const_16510,])
output2 = relay.Tuple([call_16420,call_16427,call_16432,call_16449,const_16448,call_16452,call_16481,const_16479,const_16480,call_16487,call_16511,var_16509,const_16510,])
func_16513 = relay.Function([var_16509,], output)
mod['func_16513'] = func_16513
mod = relay.transform.InferType()(mod)
var_16514 = relay.var("var_16514", dtype = "float64", shape = (1, 264))#candidate|16514|(1, 264)|var|float64
output = func_16513(var_16514)
func_16515 = relay.Function([var_16514], output)
mutated_mod['func_16515'] = func_16515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12848_call = mod.get_global_var('func_12848')
func_12850_call = mutated_mod.get_global_var('func_12850')
call_16521 = func_12848_call()
call_16522 = func_12848_call()
output = relay.Tuple([call_16521,])
output2 = relay.Tuple([call_16522,])
func_16523 = relay.Function([], output)
mod['func_16523'] = func_16523
mod = relay.transform.InferType()(mod)
mutated_mod['func_16523'] = func_16523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16523_call = mutated_mod.get_global_var('func_16523')
call_16524 = func_16523_call()
output = call_16524
func_16525 = relay.Function([], output)
mutated_mod['func_16525'] = func_16525
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16615 = relay.var("var_16615", dtype = "int32", shape = (12, 13, 15))#candidate|16615|(12, 13, 15)|var|int32
var_16616 = relay.var("var_16616", dtype = "int32", shape = (12, 13, 15))#candidate|16616|(12, 13, 15)|var|int32
bop_16617 = relay.equal(var_16615.astype('bool'), relay.reshape(var_16616.astype('bool'), relay.shape_of(var_16615))) # shape=(12, 13, 15)
func_15911_call = mod.get_global_var('func_15911')
func_15915_call = mutated_mod.get_global_var('func_15915')
const_16628 = relay.const(7, dtype = "uint32")#candidate|16628|()|const|uint32
const_16629 = relay.const([8,5,-4,6,-9,9,10,-6,4,7,-3,1,-2,-8,-10,10,-4,-2,9,4,-10,-4,7,-9], dtype = "uint32")#candidate|16629|(24,)|const|uint32
const_16630 = relay.const([-4,-8,10,4,10,-2,-4,5,-5,-1,-2,1,5,6,-1,-1,5,10,9,7,9,-10,-6,-6,-9,7,10,-7,-8,-9,2,-3,-9,-6,10,8,3,-2,-2,9,9,-3,7,-4,-1,-3,-4,1,3,2,1,3,-7,-4,-7,-10,-10,-5,-3,2,-3,8,-3,-3,-6,-10,-4,-2,9,-9,8,5,2,-5,-1,10,1,-3,7,-3,-10,2,5,6,10,4,-7,-6,-9,4,9,5,-2,-6,-4,-3,-1,8,-9,-4,10,-6,7,5,-4,-5,5,-3,-8,-7,8,-7,-7,7,-9,-4,8,-5,-4,10,-1,9,7,-6,-2,7,3,1,7,5], dtype = "uint64")#candidate|16630|(130,)|const|uint64
call_16627 = relay.TupleGetItem(func_15911_call(relay.reshape(const_16628.astype('uint32'), []), relay.reshape(const_16629.astype('uint32'), [24,]), relay.reshape(const_16630.astype('uint64'), [130,]), ), 4)
call_16631 = relay.TupleGetItem(func_15915_call(relay.reshape(const_16628.astype('uint32'), []), relay.reshape(const_16629.astype('uint32'), [24,]), relay.reshape(const_16630.astype('uint64'), [130,]), ), 4)
output = relay.Tuple([bop_16617,call_16627,const_16628,const_16629,const_16630,])
output2 = relay.Tuple([bop_16617,call_16631,const_16628,const_16629,const_16630,])
func_16632 = relay.Function([var_16615,var_16616,], output)
mod['func_16632'] = func_16632
mod = relay.transform.InferType()(mod)
var_16633 = relay.var("var_16633", dtype = "int32", shape = (12, 13, 15))#candidate|16633|(12, 13, 15)|var|int32
var_16634 = relay.var("var_16634", dtype = "int32", shape = (12, 13, 15))#candidate|16634|(12, 13, 15)|var|int32
output = func_16632(var_16633,var_16634,)
func_16635 = relay.Function([var_16633,var_16634,], output)
mutated_mod['func_16635'] = func_16635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14992_call = mod.get_global_var('func_14992')
func_14993_call = mutated_mod.get_global_var('func_14993')
call_16683 = relay.TupleGetItem(func_14992_call(), 0)
call_16684 = relay.TupleGetItem(func_14993_call(), 0)
output = call_16683
output2 = call_16684
func_16705 = relay.Function([], output)
mod['func_16705'] = func_16705
mod = relay.transform.InferType()(mod)
mutated_mod['func_16705'] = func_16705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16705_call = mutated_mod.get_global_var('func_16705')
call_16706 = func_16705_call()
output = call_16706
func_16707 = relay.Function([], output)
mutated_mod['func_16707'] = func_16707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15496_call = mod.get_global_var('func_15496')
func_15498_call = mutated_mod.get_global_var('func_15498')
call_16810 = relay.TupleGetItem(func_15496_call(), 0)
call_16811 = relay.TupleGetItem(func_15498_call(), 0)
output = call_16810
output2 = call_16811
func_16813 = relay.Function([], output)
mod['func_16813'] = func_16813
mod = relay.transform.InferType()(mod)
output = func_16813()
func_16814 = relay.Function([], output)
mutated_mod['func_16814'] = func_16814
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14297_call = mod.get_global_var('func_14297')
func_14298_call = mutated_mod.get_global_var('func_14298')
call_16844 = func_14297_call()
call_16845 = func_14297_call()
func_12828_call = mod.get_global_var('func_12828')
func_12832_call = mutated_mod.get_global_var('func_12832')
const_16866 = relay.const([-1,-3,-2,-10,-2,-7,-3,-2,4,8,8,7,-2,4,-5,4,-5,-6,-4,7,-5,10,5,-2,7,-3,4,9,-4,-7,-5,2,-10,9,7,9,-2,1,-2,-8,-3,-4,-10,4,9,2,-4,5,5,7,2,5,6,3,6,-7,-4,-7,7,8,-5,-9,5,5,8,3,8,7,-3,-4,-2,8,-5,10,-6,-5,9,10,-7,-7,6,8,7,2,4,8,8,-1,1,-2,-2,-8,2,-6,-2,4,10,-4,7,-6,1,-8,10,-1,-3,-7,-1,-5,-2,9,-1,-4,5,1,-5,3,-10,4,-10,-10,7,7,2,-10,-10,-10,2,-5,1,10], dtype = "uint64")#candidate|16866|(130,)|const|uint64
var_16867 = relay.var("var_16867", dtype = "float32", shape = (396,))#candidate|16867|(396,)|var|float32
call_16865 = relay.TupleGetItem(func_12828_call(relay.reshape(const_16866.astype('uint64'), [13, 10]), relay.reshape(var_16867.astype('float32'), [396,]), ), 7)
call_16868 = relay.TupleGetItem(func_12832_call(relay.reshape(const_16866.astype('uint64'), [13, 10]), relay.reshape(var_16867.astype('float32'), [396,]), ), 7)
func_16030_call = mod.get_global_var('func_16030')
func_16031_call = mutated_mod.get_global_var('func_16031')
call_16908 = func_16030_call()
call_16909 = func_16030_call()
func_9509_call = mod.get_global_var('func_9509')
func_9511_call = mutated_mod.get_global_var('func_9511')
var_16913 = relay.var("var_16913", dtype = "float32", shape = (336,))#candidate|16913|(336,)|var|float32
call_16912 = relay.TupleGetItem(func_9509_call(relay.reshape(var_16913.astype('float32'), [12, 7, 4])), 0)
call_16914 = relay.TupleGetItem(func_9511_call(relay.reshape(var_16913.astype('float32'), [12, 7, 4])), 0)
func_10179_call = mod.get_global_var('func_10179')
func_10182_call = mutated_mod.get_global_var('func_10182')
var_16917 = relay.var("var_16917", dtype = "uint16", shape = (1092,))#candidate|16917|(1092,)|var|uint16
call_16916 = relay.TupleGetItem(func_10179_call(relay.reshape(var_16917.astype('uint16'), [6, 13, 14])), 0)
call_16918 = relay.TupleGetItem(func_10182_call(relay.reshape(var_16917.astype('uint16'), [6, 13, 14])), 0)
output = relay.Tuple([call_16844,call_16865,const_16866,var_16867,call_16908,call_16912,var_16913,call_16916,var_16917,])
output2 = relay.Tuple([call_16845,call_16868,const_16866,var_16867,call_16909,call_16914,var_16913,call_16918,var_16917,])
func_16940 = relay.Function([var_16867,var_16913,var_16917,], output)
mod['func_16940'] = func_16940
mod = relay.transform.InferType()(mod)
var_16941 = relay.var("var_16941", dtype = "float32", shape = (396,))#candidate|16941|(396,)|var|float32
var_16942 = relay.var("var_16942", dtype = "float32", shape = (336,))#candidate|16942|(336,)|var|float32
var_16943 = relay.var("var_16943", dtype = "uint16", shape = (1092,))#candidate|16943|(1092,)|var|uint16
output = func_16940(var_16941,var_16942,var_16943,)
func_16944 = relay.Function([var_16941,var_16942,var_16943,], output)
mutated_mod['func_16944'] = func_16944
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17060 = relay.var("var_17060", dtype = "bool", shape = ())#candidate|17060|()|var|bool
var_17061 = relay.var("var_17061", dtype = "bool", shape = (8, 16, 13))#candidate|17061|(8, 16, 13)|var|bool
bop_17062 = relay.logical_and(var_17060.astype('bool'), var_17061.astype('bool')) # shape=(8, 16, 13)
func_697_call = mod.get_global_var('func_697')
func_701_call = mutated_mod.get_global_var('func_701')
const_17072 = relay.const([9,-3,-8,-5,-5,-9,-2,-2,-5,7,-5,-9,-8,-5,-3,7,4,4,-10,-5,5,10,6,10,6,1,2,2,-9,10,5,3,1,9,4,4,2,9,-7,9,8,5,-2,-9,3,-2,-9,8,-2,-9,5,-6,-1,-2,3,2,-5,-1,-5,7,-2,-6,4,10,3,2,7,4,4,4,9,-9,2,-1,-2,5,-7,-4,-7,7,-4,-7,-9,-6,-6,8,-6,-2,-9,-7,3,-5,-3,3,1,-9,9,5,6,8,-2,9,-7,8,4,-9,7,7,-2,7,10,-10,1,-6,-7,-9,5,8,-9,-8,-2,-9,-10,9,9,-5,4,-10,1,10,-2,-6,6,-1,-10,7,-7,-3,7,10,9,-4,1,6,10,9,-6,3,8,-9,4,-2,-6,-7,-6,6,-2,-8,4,8], dtype = "uint64")#candidate|17072|(160,)|const|uint64
call_17071 = relay.TupleGetItem(func_697_call(relay.reshape(const_17072.astype('uint64'), [4, 5, 8]), relay.reshape(const_17072.astype('uint64'), [4, 5, 8]), ), 0)
call_17073 = relay.TupleGetItem(func_701_call(relay.reshape(const_17072.astype('uint64'), [4, 5, 8]), relay.reshape(const_17072.astype('uint64'), [4, 5, 8]), ), 0)
func_13858_call = mod.get_global_var('func_13858')
func_13859_call = mutated_mod.get_global_var('func_13859')
call_17076 = func_13858_call()
call_17077 = func_13858_call()
output = relay.Tuple([bop_17062,call_17071,const_17072,call_17076,])
output2 = relay.Tuple([bop_17062,call_17073,const_17072,call_17077,])
func_17078 = relay.Function([var_17060,var_17061,], output)
mod['func_17078'] = func_17078
mod = relay.transform.InferType()(mod)
mutated_mod['func_17078'] = func_17078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17078_call = mutated_mod.get_global_var('func_17078')
var_17080 = relay.var("var_17080", dtype = "bool", shape = ())#candidate|17080|()|var|bool
var_17081 = relay.var("var_17081", dtype = "bool", shape = (8, 16, 13))#candidate|17081|(8, 16, 13)|var|bool
call_17079 = func_17078_call(var_17080,var_17081,)
output = call_17079
func_17082 = relay.Function([var_17080,var_17081,], output)
mutated_mod['func_17082'] = func_17082
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14457_call = mod.get_global_var('func_14457')
func_14458_call = mutated_mod.get_global_var('func_14458')
call_17131 = func_14457_call()
call_17132 = func_14457_call()
func_11147_call = mod.get_global_var('func_11147')
func_11149_call = mutated_mod.get_global_var('func_11149')
const_17134 = relay.const([-8.553284,6.260199,-4.134075,8.568904,5.773588,-3.436342,-7.962514,-7.315951,4.580111,7.419098,-6.463748,-0.837446,-8.822479,-0.501058,-8.975294,6.003087,2.737751,7.885048,-2.864907,1.105884,-1.014102,0.215081,-3.235102,-3.904225,7.340652,4.058876,-9.609845,0.417481,-2.820760,-8.446273,0.636109,-3.524167,-8.894566,-6.362375,-4.477457,7.251726,6.715771,6.043913,-8.803036,7.912226,1.156480,4.327016,7.933152,-6.299421,9.854378,-2.738983,1.021017,2.907270,7.749597,-9.713403,-7.923399,-9.078421,-6.819482,7.646487,-7.349780,2.544639,5.536049,7.092884,7.877831,1.167676,0.281188,4.969004,-4.109390,-9.246409,-1.327582,1.270235,-8.992544,8.329999,4.932644,1.186627,8.894774,7.226391,-3.637500,0.159831,2.787075,-5.630728,8.394534,1.378865,-2.778836,4.301963,-9.614665,0.044567,-5.924007,7.365613,-2.492838,9.037191,9.304612,-8.038947,-9.133092,8.095364,-4.334584,-6.729543,3.430990,5.041756,0.304630,6.085166,9.195664,8.954733,4.929515,6.746565,7.224925,3.933564,-7.845604,-0.972543,-4.650989,-8.540940,6.486818,-3.421476,-9.936291,6.530848,-8.130092,2.675830,2.462422,7.334795,4.269413,-6.602698,-5.866477,-6.490839,-5.291322,0.507060,-6.293316,5.632964,-5.929229,8.030717,-1.379892,-9.623557,0.227195,-8.665486,-4.857316,4.923723,2.291187,1.085529,8.979962,-1.459252,-4.595694,-6.111642,1.978346,1.234164,1.289345,-8.458197,4.432576,-9.977990,-7.517376,8.361251,3.677060,-5.029106,0.761300,-5.027033,8.161503,-8.710433,-2.131732,6.909485,-3.246032,9.355813,4.302114,8.521158,-2.268604,5.788648,9.304927,-7.249974,7.972328,4.196237,-1.391433,5.047215,-7.512076,4.311761,5.777804,-1.490603,1.585534,7.267471,4.390739,5.647848,1.634791,-6.737377,-0.972425,8.393760,7.163348,-8.864336,-9.856730,-3.573897,4.547863,6.130750,-5.173032,-6.842458,1.949716,-5.152531,7.112219,-8.400443,-2.903515,2.245422,7.955866,-0.356255,0.894440,-1.684671,-4.819467,-5.464277,3.829801,-1.612242,9.873720,5.680013,3.369940,6.348014,-7.472899,2.395120,-2.711536,0.728967,8.036537,-5.539637,-0.724636,-2.196566,6.155887,-9.048293,-3.630295,-4.780067,3.688939,-5.792741,3.387481,6.833431,0.509516,-6.764743,5.035622,-7.497295,8.199465,9.546040,4.943953,9.170792,-3.998758,0.573182,-8.931383,-6.296754,-7.048233,-8.068372,-9.017352,9.381698,-7.406038,7.570442,2.557333,-6.930945,7.252263,-5.549584,9.380310,0.489106,3.794727,-5.094622,8.621525,5.602650,8.183169,9.523159,-2.990476,-3.313386,6.352351,-5.085803,6.843564,1.845880,3.183643,9.770189,5.298556,-0.884981,-4.493365,6.538742,-3.931811,2.513042,-3.461452,6.716317,0.325678,-0.825742,-0.011374,3.592375,0.811477,-8.818098,-3.023514,-8.233355,-0.409853,-1.745974,5.602161,-3.236107,-7.082915,-9.852384,4.133338,5.417571,7.068884,1.805193,5.028043,7.681322,2.751651,1.983530,0.965925,-2.211263,-0.934428,-2.628131,-1.934472,1.637590,-6.492402,6.933656,-2.082448,-2.974237,-2.917114,5.417897,-5.585542,1.026686,-0.495246,2.063740,-8.677573,1.462436,-9.580752,-5.518427,9.624321,-0.632405,0.950647,3.775875,-2.828012,6.915842,3.647169,-8.544666,5.239601,2.091540,-8.664634,-8.094016,-1.938662,-4.732027,7.622949,8.394183,-9.258448,7.637789,-3.474553,1.813908,-0.070093,4.116703,4.696797,-1.984863,9.090514,-6.873294,-2.944547,-8.792289,5.556683,-9.179197,-4.033301,1.642618,2.376960,-2.554695,8.481371,-9.020950,9.131291,6.294652,-3.194783,5.333859,5.037185,6.556664,-1.735247,6.646145,-3.614719,6.394141,4.834370,-7.872827,3.527603,-2.088347,-0.692381,-9.568078,0.314976,6.537700,8.223277,9.613113,-6.400508,6.871821,0.168674,-2.467649,-8.078615,-8.467726,-6.794244,-7.542453,7.309574,-3.609569,1.031411,5.000273,-0.764400,-9.540485,-9.328819,2.195338,4.868825,5.003150,8.498457,-5.870012,7.643938,4.622586,6.230494,8.398171,9.108135,7.269166,9.359680,8.809660,4.889280,0.427635,8.244055,-1.674924,8.309468,9.463265,-8.697565,-9.448646,-1.940032,9.389702,8.574659,9.986864,7.940910,-3.966267,4.060876,-2.174026,0.715343,-2.722850,-6.593723,2.711142,5.831881,-8.510721,9.944657,6.255923,7.732377,8.073566,-8.603601,6.469693,5.902259,-9.035109,6.190079,8.739449,-0.396229,7.447612,1.880092,6.377878,-9.539323,-0.834497,-9.989676,5.516741,-7.926284,7.318919,9.731309,-1.372716,-4.858712,-2.304169,-6.121242,-4.044836,5.228391,1.867984,7.307351,3.951537,0.668319,6.857118,-0.779160,9.601517,1.353876,4.305929,1.569560,-1.827531,-5.629249,5.389940,-5.599886,8.521652,7.771530,-8.271387,5.331914,-4.908476,0.507861,5.728901,8.130623,2.344755,6.024253,2.223808,-4.845069,-5.301922,-1.773969,2.545891,9.669594,8.543693,-9.723494,8.570041,3.776238,-6.334329,1.364088,-5.245122,-2.475447,-8.347139,-3.287854,-2.616573,3.062832,6.119148,-9.216640,-4.299143,-4.240392,-4.357897,-0.661680,-1.915513,-9.076979,-9.809958,-4.588114,-1.444572,-8.094823,-9.764573,-3.342239,-9.274342,4.630752,-5.660229,-4.005971,-0.480829,-5.641113,1.033780,-3.342716,-7.732813,-1.186482,4.573726,-0.102918,9.634056,-4.162771,2.509598,-3.234016,-4.473152,-1.806289,3.923113,4.897175,4.480296,7.883915,-6.418003,-3.092412,-7.541662,-8.026100,-6.217110,9.389143,6.317339,3.612236,-7.738361,-4.574574,-5.241736,9.971800,-1.402261,7.983234,-5.962630,-6.808216,-8.537988,-9.639383,-3.324375,-3.470243,1.270760,-8.950096,8.619505,7.812390,-7.129434,-9.323824,-6.020808,-7.660419,5.396328,-0.264428,-6.368478,-0.192383,-4.683739,1.520573,7.474951,6.529751,6.903125,-3.292203,7.051007,0.279909,6.292121,-4.541619,5.852886,-4.780470,-7.424843,2.820214,-6.650352,-0.417882,-6.145008,9.262100,7.080704,-6.299242,-5.072387,-2.894583,-4.273281,2.711483,5.844789,-2.968950,2.116343,6.226089,7.863526,-1.672579,8.372050,-0.740744,6.725325,2.383348,-6.023630,0.968441,-0.660858,8.428474,6.730407,8.568666,-8.827960,-0.250850,-7.191976,-5.584846,-4.716996,4.561342,8.115328,4.072562,1.938686,9.350469,-7.620019,8.133146,-0.754752,6.134272,4.777253,8.370662,-1.206425,2.709774,6.577418,8.544158,7.211339,0.079794,-6.530690,4.391877,-5.284376,-0.881331,9.909733,6.085390,-5.521085,-0.308291,8.635526,0.557327,3.166327,0.176415,-4.536380,-1.450603,7.512784,-3.074186,-8.812239,-9.485726,6.623411,0.897033,-0.651567,-5.913698,3.728437,-8.246334,-8.479411,9.961577,4.803838,7.019895,6.450821,6.309727,5.427208,-0.688604,4.770158,-2.387477,5.111680,7.516391,9.851842,-5.251566,-1.499465,9.192723,3.870665,-1.041275,7.772340,-9.244639,9.448960,-2.273665,-7.184786,-9.151259,1.971220,-2.577808,-7.734225,-2.889711,1.948488,8.924937,4.173466,4.816824,0.783666,5.752545,9.697371,9.175847,9.615951,9.002077,-5.701654,1.185180,3.894381,5.455642,-1.592299,3.821749,-5.885517,2.422186,4.668432,-1.445702,4.919917,-0.459733,-9.003317,0.715334,9.391713,7.242882,0.407920,6.901544,-3.475678,-9.772505,-7.097228,-7.031606,-0.275193,-3.086129,-9.428114,-8.424502,4.110224,-5.321744,-0.182751,0.913150,4.207814,-5.611920,-9.615124,6.277601,-2.020097,3.651027,1.476702,4.207761,3.030108,7.038933,3.843444,9.331799,-6.944800,-9.339201,-2.020445,-4.066208,-6.450021,-1.268559,-9.638907,2.262786,1.297941,8.251537,-5.333957,7.561485,2.596060,-0.484144,-7.060826,4.481831,6.385836,-4.974019,2.815463,8.596674,5.946960,-5.948918,8.943421,-3.554100,-5.522834,9.958171,-1.381660,1.842283,-1.024236,-3.269383,1.580960,2.551270,7.816084,-5.969897,9.299357,-0.560161,7.579482,-9.897453,-8.189174,-8.743850,6.100711,-3.101374,-4.007009,1.790620,5.115643,9.399638,7.914791,8.617249,-4.742035,7.029020,-7.911643,-8.017699,6.044782,-3.883388,9.447891,-4.726146,4.926111,6.751223,-4.814255,-9.452197,-0.116538,7.452390,-9.211566,4.350385,-8.287348,-2.533248,-6.212967,7.643082,-1.455324,-3.458832,-8.376225,-4.647301,3.880132,0.412646,-1.702105,4.607971,8.456929,-2.475143,2.461356,1.700438,-6.647070,-0.437710,-5.033857,-3.863494,-1.762459,8.604244,-2.557770,-2.483335,2.292996,2.934078,6.136809,-6.386086,5.432434,-5.353715,-6.829288,8.483732,-0.555286,-2.823546,7.522337,9.859607,8.235525,-8.936529,-3.555923,0.355589,-2.715852,0.215151,2.644974,-7.083862,-1.624271,0.670118,-7.311476,9.721986,6.296231,-8.335723,1.747999,-4.293135,-4.699887], dtype = "float64")#candidate|17134|(832,)|const|float64
call_17133 = relay.TupleGetItem(func_11147_call(relay.reshape(const_17134.astype('float64'), [832,])), 5)
call_17135 = relay.TupleGetItem(func_11149_call(relay.reshape(const_17134.astype('float64'), [832,])), 5)
bop_17156 = relay.add(call_17133.astype('int8'), relay.reshape(const_17134.astype('int8'), relay.shape_of(call_17133))) # shape=(832,)
bop_17159 = relay.add(call_17135.astype('int8'), relay.reshape(const_17134.astype('int8'), relay.shape_of(call_17135))) # shape=(832,)
output = relay.Tuple([call_17131,bop_17156,])
output2 = relay.Tuple([call_17132,bop_17159,])
func_17173 = relay.Function([], output)
mod['func_17173'] = func_17173
mod = relay.transform.InferType()(mod)
output = func_17173()
func_17174 = relay.Function([], output)
mutated_mod['func_17174'] = func_17174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11095_call = mod.get_global_var('func_11095')
func_11096_call = mutated_mod.get_global_var('func_11096')
call_17203 = func_11095_call()
call_17204 = func_11095_call()
func_15594_call = mod.get_global_var('func_15594')
func_15596_call = mutated_mod.get_global_var('func_15596')
call_17206 = func_15594_call()
call_17207 = func_15594_call()
func_15578_call = mod.get_global_var('func_15578')
func_15580_call = mutated_mod.get_global_var('func_15580')
call_17218 = relay.TupleGetItem(func_15578_call(), 1)
call_17219 = relay.TupleGetItem(func_15580_call(), 1)
output = relay.Tuple([call_17203,call_17206,call_17218,])
output2 = relay.Tuple([call_17204,call_17207,call_17219,])
func_17224 = relay.Function([], output)
mod['func_17224'] = func_17224
mod = relay.transform.InferType()(mod)
output = func_17224()
func_17225 = relay.Function([], output)
mutated_mod['func_17225'] = func_17225
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17285 = relay.var("var_17285", dtype = "bool", shape = (1, 10, 6))#candidate|17285|(1, 10, 6)|var|bool
var_17286 = relay.var("var_17286", dtype = "bool", shape = (6, 10, 6))#candidate|17286|(6, 10, 6)|var|bool
bop_17287 = relay.logical_or(var_17285.astype('bool'), var_17286.astype('bool')) # shape=(6, 10, 6)
func_3611_call = mod.get_global_var('func_3611')
func_3617_call = mutated_mod.get_global_var('func_3617')
const_17291 = relay.const([6.297420,-4.134835,4.100342,-1.475316,5.732122,-5.958545,-4.853353,0.904312,4.972183,-2.427194,6.468781,2.874539,-3.813188,2.931799,-8.676549,-4.747611,-6.573131,-5.533019,9.265108,3.014893,4.988030,-6.075349,1.357393,-5.423790,-3.334185,-7.386557,1.868286,-8.881501,-9.149234,-2.681761,-8.618547,-7.823856,2.244894,-3.545902,1.594515,-0.713224,-4.932834,9.123415,-2.964078,-5.706032,-8.198151,-5.042769,8.825613,2.173790,-1.757793,-6.783169,3.245486,-2.955805,-3.007308,1.893693,-4.231478,-5.940048,9.362095,-8.563935,-8.763965,-8.676419,8.070168,-4.968995,0.660242,-5.231960,8.995689,2.818431,7.350216,-4.753828,-3.124769,0.306317,4.523963,8.982965,6.523317,-7.893980,9.411031,-9.005296,-0.770065,2.174865,3.849451,7.245857,-9.449777,0.719855,-5.393674,8.054122,7.768417,8.572419,4.566316,9.062416,-7.488535,-0.641645,7.164981,-7.866722,5.584723,7.391089,0.752250,-5.382861,7.009727,3.011395,4.641957,9.196873,-1.960272,1.307988,4.593914,-4.176500,-4.018288,0.369445,-0.413989,0.755228,2.336728,-9.242952,-7.422971,8.839126,-3.980606,1.767263,3.080498,-3.167070,-8.725030,8.324935,6.893108,0.551373,-1.868484,3.589115,2.483596,2.864149,1.442899,4.598783,-1.544418,-4.551816,-1.189910,-9.420317,-9.791150,7.566298,-8.071179,-1.556079,-2.508496,2.670273,1.922558,3.964689,-8.262006,4.443617,-9.692202,9.080133,9.954127,3.225543,1.739755,-3.416018,7.891566,-5.338672,-4.403777,5.211808,4.588597,-2.309796,4.753828,9.328110,-8.250815,3.651851,1.518333,8.926076,-4.266391,-0.672703,-8.574395,7.547720,-1.390930,5.760943,2.353248,-6.180903,6.909612,3.405083,-8.610910,-5.205280,2.392816,-1.221698,-0.719614,-1.411978,-1.349596,3.757584,8.538828,-1.979313,-1.700078,-8.107634,-7.294209,-2.762496,8.477424,-9.880842,-1.906213,-9.422420,5.799950,0.099148,-2.563852,-7.731567,-8.300705,4.368886,9.024677,-0.575135,6.275743,0.953891,1.284089,-4.842430,5.992952,-0.959332,5.530262,0.823206,4.295824,7.963964,-4.162268,1.809263,2.798518,-6.868239,-9.153904,-9.997706,-4.347646,-4.011206,-5.321784,-2.093556,5.696111,9.971263,-7.447905,1.914872,9.582734,4.900314,9.831121,7.051766,-7.452082,3.615790,-9.894328,-3.449356,0.924545,-4.797034,4.041896,4.714512,9.840690,-0.092416,9.271323,-5.262708,-2.358969,1.666187,-3.060897,-5.734963,-4.700155,6.038729,7.350627,6.686312,-9.060629,-7.978037,0.511506,2.272611,4.046443,-3.409252,8.733203,0.178962,-8.647095,4.274477,1.468675,2.674463,1.416055,-0.609453,8.037509,5.163650,1.029046,6.319227,4.920626,-4.871041,-1.520879,-8.121222,7.948459,6.522300,-4.983160,-9.129047,-6.877245,3.353653,-2.537622,1.207524,-4.957305,-6.900985,-8.807040,-5.771938,-5.447966,-6.426906,7.297385,-1.367245,1.748650,-1.957517,8.538392,1.826453,7.371893,6.349941,3.080653,6.916895,-3.282840,6.313941,4.404590,-7.677432,-4.434667,6.389090,3.257855,-0.346606,1.442498,-7.566575,5.745564,7.095962,0.212200,8.212554,4.176810,-9.255104,-8.859627,-2.248717,9.389467,9.100192,-1.476991,2.590552,-2.963677,-8.965926,-8.207212,-9.917064,-2.395782,-1.735283,3.553473,-2.539488,-7.015735,-0.345981,0.751870,5.845685,3.990467,-3.981353,5.518655,-1.809405,-0.557157,9.338751,9.357292,-6.883309,0.755658,5.860977,-6.896237,2.723275,-4.694692,6.056193,1.082530,-4.623799,0.615251,-4.480295,-0.571361,5.193560,5.197662,-0.854239,-4.036408,-6.300147,5.666690,-0.971201,-0.503412,8.790463,3.875996,-3.480855,2.618023,-8.860262,3.573365,2.041679,0.110985,-7.688660,3.670547,3.343915,-3.235319,-9.189260,-8.316342,2.803585,-6.258008,8.882619,-2.175463,-6.160216,5.485843,-5.046786,7.834781,-3.345927,-3.698731,5.457330,6.444768,-2.624229,4.604400,-9.759289,9.245917,-9.650974,-3.423975,-8.705865,9.095713,-9.768117,6.530937,1.098593,-8.590513,8.422254,3.263401,-4.438422,3.965334,-9.312655,4.224506,-8.256198,-9.448816,3.784325,2.290217,1.582589,-8.310592,8.906944,6.929179,8.517895,-5.600934,-1.169445,4.648185,4.131380,2.634486,1.187361,-9.790301,-0.731417,-1.237770,3.302647,9.834859,-1.039853,-8.165536,2.606469,8.630827,1.192917,4.237736,9.344449,-8.508896,3.411085,-0.096073,7.629101,6.428629,9.681607,0.818498,2.438281,-4.705435,-1.596039,8.715411,-6.507173,-7.920519,-6.028579,2.918299,2.497036,-5.874454,-2.270832,2.345010,4.898219,0.878883,2.426984,6.864171,3.640245,-7.142831,-1.763766,8.052186,-8.406450,-9.513463,5.203730,-7.304720,-9.943221,5.260249,6.258343,-3.364046,0.302918,-9.318695,-2.365070,8.925736,2.157608,4.769399,8.885683,-3.134925,0.734984,2.023961,-5.782545,9.464747,-2.762772,6.946224,3.830529,8.188944,9.864952,8.287502,2.232856,8.337765,8.666248,0.108663,2.441843,-3.528765,-8.306503,3.274289,-2.079016,1.652426,-5.320061,-6.446767,-1.537358,-5.625058,7.575910,8.443622,0.876163,5.058501,-7.064701,9.238019,-2.908147,-6.635241,3.864486,-7.536906,-0.270400,3.588304,-3.302220,-4.384936,2.129743,4.260648,6.283905,1.593739,7.172202,3.278337,5.971027,-5.703418,-1.578347,4.439819,-9.667611,4.131062,9.785422,6.499741,2.698295,0.971465,5.649978,1.731483,9.826537,8.945079,-8.322956,-5.074598,6.736045,6.056271,8.590562,-9.944790,-4.501459,-5.924202,-1.124835,-0.794607,-0.564500,-0.288121,-3.958962,-4.930201,-3.015608,-2.674392,-5.943114,2.265882,0.465926,7.490044,0.374279,6.703626,-3.250448,3.324103,7.658330,-8.883625,7.042949,6.387806,-2.075813,-4.502335,8.148431,7.707396,9.801843,-0.239298,-4.513782,-1.582636,0.936924,6.796865,9.930610,-8.728535,-3.115153,-7.917712,5.045704,6.649221,7.423013,-8.389160,2.450258,-3.555702,-3.047580,1.228128,0.985110,-5.730767,8.622394,-4.335768,9.703188,-0.447167,5.099204,7.180198,-1.286296,-7.443073,-8.930280,6.008835,0.884270,5.728675,-5.703524,-3.789763,-1.773775,-3.973921,-2.122333,-5.651583,6.831723,-8.478294,-3.482162,9.025519,-8.286895,-1.701534,-9.906825,-1.233102,-6.473512,-6.606470,6.043463,-4.142628,3.612371,5.141680,6.694995,6.729414,-9.953578,4.232931,-8.238390,-2.678080,-8.961925,0.668723,-3.708074,-3.741350,2.813377,8.824838,2.645909,-5.548262,-2.413266,0.727069,-3.010771,-9.613363,-7.032644,5.576815,-4.850346,9.130434,-6.908783,8.361992,3.126999,6.885152,-3.538957,6.006945,-4.226644,9.246553,7.813986,-9.229560,0.544047,8.320673,-4.917805,-8.180822,-0.722056,-3.686737,1.728019,3.661132,5.353832,5.859257,2.961720,-8.855228,2.922025,-8.950012,-1.762942,-8.279082,4.885983,1.463989,-5.592071,-5.295481,0.309779,6.069189,-0.186842,5.537904,-5.686382,-5.872595,9.858621,1.771030,-8.971093,-6.210520,1.401225,-1.998354,-6.366230,-8.481043,-3.055612,4.310261,8.243533,-1.043509,7.529332,-6.640949,-3.574571,6.017389,1.326504,-5.054165,-8.493020,-6.951441,9.736952,-9.675060,-9.102194,-5.840749,8.119216,-7.791052,0.283303,-8.710845,6.955535,-8.246271,8.605279,9.640743,-0.003558,-9.461094], dtype = "float64")#candidate|17291|(693,)|const|float64
var_17292 = relay.var("var_17292", dtype = "float32", shape = (396,))#candidate|17292|(396,)|var|float32
var_17293 = relay.var("var_17293", dtype = "uint64", shape = (130,))#candidate|17293|(130,)|var|uint64
var_17294 = relay.var("var_17294", dtype = "uint64", shape = (160,))#candidate|17294|(160,)|var|uint64
call_17290 = relay.TupleGetItem(func_3611_call(relay.reshape(const_17291.astype('float64'), [9, 11, 7]), relay.reshape(var_17292.astype('float32'), [396,]), relay.reshape(var_17293.astype('uint64'), [130,]), relay.reshape(var_17294.astype('uint64'), [160,]), ), 8)
call_17295 = relay.TupleGetItem(func_3617_call(relay.reshape(const_17291.astype('float64'), [9, 11, 7]), relay.reshape(var_17292.astype('float32'), [396,]), relay.reshape(var_17293.astype('uint64'), [130,]), relay.reshape(var_17294.astype('uint64'), [160,]), ), 8)
output = relay.Tuple([bop_17287,call_17290,const_17291,var_17292,var_17293,var_17294,])
output2 = relay.Tuple([bop_17287,call_17295,const_17291,var_17292,var_17293,var_17294,])
func_17300 = relay.Function([var_17285,var_17286,var_17292,var_17293,var_17294,], output)
mod['func_17300'] = func_17300
mod = relay.transform.InferType()(mod)
mutated_mod['func_17300'] = func_17300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17300_call = mutated_mod.get_global_var('func_17300')
var_17302 = relay.var("var_17302", dtype = "bool", shape = (1, 10, 6))#candidate|17302|(1, 10, 6)|var|bool
var_17303 = relay.var("var_17303", dtype = "bool", shape = (6, 10, 6))#candidate|17303|(6, 10, 6)|var|bool
var_17304 = relay.var("var_17304", dtype = "float32", shape = (396,))#candidate|17304|(396,)|var|float32
var_17305 = relay.var("var_17305", dtype = "uint64", shape = (130,))#candidate|17305|(130,)|var|uint64
var_17306 = relay.var("var_17306", dtype = "uint64", shape = (160,))#candidate|17306|(160,)|var|uint64
call_17301 = func_17300_call(var_17302,var_17303,var_17304,var_17305,var_17306,)
output = call_17301
func_17307 = relay.Function([var_17302,var_17303,var_17304,var_17305,var_17306,], output)
mutated_mod['func_17307'] = func_17307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14426_call = mod.get_global_var('func_14426')
func_14427_call = mutated_mod.get_global_var('func_14427')
call_17315 = func_14426_call()
call_17316 = func_14426_call()
func_12828_call = mod.get_global_var('func_12828')
func_12832_call = mutated_mod.get_global_var('func_12832')
const_17366 = relay.const([[-8,-1,-4,-4,-2],[7,7,1,-2,-2],[6,-6,-4,9,-2],[6,-9,-10,6,5],[-5,7,4,-5,-10],[-1,-6,-1,1,-2],[8,-4,7,-2,-8],[-2,-1,8,-6,-4],[-7,5,10,-6,6],[6,8,-1,-4,7],[-9,-6,7,-6,4],[-1,4,6,10,5],[-2,9,2,4,-4],[7,-9,6,6,10],[1,-3,-5,-9,3],[-2,6,4,5,6],[-8,-5,-8,4,4],[-6,-3,-1,1,5],[5,-10,1,3,-1],[-5,1,-7,-2,5],[-5,2,3,6,3],[-8,9,3,2,-5],[-4,4,-2,-6,-2],[-10,-3,2,-6,-10],[2,-9,-7,-2,-10],[-2,9,8,6,4]], dtype = "uint64")#candidate|17366|(26, 5)|const|uint64
const_17367 = relay.const([-0.462531,9.030289,-6.074552,-4.986045,-0.949902,9.502484,8.482126,7.790846,5.328411,-6.353545,5.061409,1.748978,8.020124,0.762053,-2.609364,-6.824200,8.295589,-4.725886,7.739221,-5.261025,3.043489,-0.459965,-4.818027,-0.189616,-6.851816,9.782906,-4.819036,9.392425,-0.495846,-1.256300,0.727890,9.030289,1.239120,7.550723,-0.165749,-6.811508,1.683943,-4.115798,-6.312967,7.127052,1.976524,-8.744652,-7.855347,7.032566,-2.528169,7.081399,-3.849421,-9.646973,-0.392968,3.151022,7.565470,-8.235027,-8.199740,-9.524249,8.959247,0.734164,3.936406,2.259621,9.372934,-3.495921,-1.532156,8.760044,-9.713006,-8.662149,3.966603,-7.932535,8.729203,-1.348789,9.131006,-2.617770,-3.171160,-0.327004,1.749645,9.094772,-1.266840,9.537034,-1.329156,-7.155057,-9.569248,1.157432,-0.888591,2.114113,4.440903,6.948064,-6.501621,5.386911,6.865280,-5.317232,1.407467,9.549267,0.067886,0.180221,8.912009,2.073812,-9.057369,-0.747212,-1.703994,3.162507,5.149933,-3.331449,-0.410556,-0.732645,7.615842,4.206316,4.237169,8.317276,7.539269,-6.126344,-8.032847,-5.728170,-7.407700,2.710781,-3.403883,-3.771103,9.473915,-1.276813,7.835473,2.872780,4.040544,8.240426,3.524863,-6.539835,1.128372,7.097162,-9.287246,4.613972,-5.863249,3.706961,2.408441,-7.520890,-0.407823,-7.488486,-4.682818,9.889608,-9.426289,-6.854676,3.895957,-8.592290,7.661190,-5.222902,-6.961504,-0.357947,-9.402558,5.712584,-4.718062,-4.522795,-2.811239,-6.951842,-9.494049,1.745063,-1.311670,-5.800556,-4.159049,1.089395,-2.165323,6.890039,8.065840,-8.527623,3.976672,7.206064,0.797645,-9.369126,-1.286179,-6.961955,-6.616867,-4.332308,8.854691,-9.470216,7.984344,0.902421,6.043546,-0.009051,8.094197,-6.870364,3.999816,-0.939178,5.393037,-7.270959,7.947257,-8.209465,-0.304012,-2.163930,0.292491,7.646456,-9.613690,5.485837,3.386384,-9.669391,-7.169009,9.328183,-2.916120,-8.690711,7.625693,-4.668445,-6.331928,-6.802634,0.775181,-6.987265,-0.707779,5.839691,3.934262,-1.813490,7.252476,9.479564,-7.767987,9.985928,-8.912721,-2.224584,-2.214946,-6.449944,-9.925821,-7.372384,5.795188,-9.101993,-7.161771,7.693703,-9.602284,0.490486,-7.162406,2.164175,4.804712,-0.232659,0.291513,4.146979,1.361495,-5.708415,2.878604,9.259807,2.144864,-2.794875,0.207919,2.886175,8.018176,3.572748,8.125626,-9.828390,3.450231,-3.127245,-0.407136,3.519020,5.749603,6.844516,-2.167441,-5.606744,-4.915113,8.575379,-1.714999,-2.604303,1.124058,9.150053,-8.458885,-6.715172,-5.755631,-0.776722,-0.694534,-0.168828,3.121536,-0.057099,-2.721039,-8.672437,9.715243,4.644887,-1.769149,-5.348208,2.752624,1.514072,4.392930,-0.803932,-4.807553,-1.087051,-5.860918,1.538877,-9.532067,7.284283,-4.725508,-7.597334,5.464376,7.121133,9.723150,-5.109452,8.500122,-1.486312,1.598534,6.910085,-8.627896,-8.155118,-5.509608,-1.651157,-9.749802,-9.142750,4.073359,-8.425819,-5.996904,3.832758,9.397189,-5.866407,9.467016,-7.078867,2.088915,-6.449729,3.414170,-5.992619,-4.165883,6.931303,-4.172447,3.566024,-6.428003,7.400293,9.759542,-4.009860,-3.314276,-5.801384,1.718208,-6.753564,-2.110991,-6.189061,7.379380,7.005034,-8.308411,-6.224275,-0.896705,-8.848111,-4.032348,9.267008,-5.705530,-3.969346,4.503835,-2.960143,6.979238,9.135058,-4.470944,-3.921671,6.273600,7.956001,-4.488621,-2.162364,-4.343144,6.499880,-8.584220,-3.078963,-3.223911,7.754252,5.521310,-2.138139,-5.242177,-5.742813,-6.533961,8.411539,4.085497,0.704934,-9.004364,-1.992648,-6.140797,9.528621,1.756241,-1.106216,5.676880,3.736565,6.799771,7.780203,2.705774,-3.069072,-4.076053,8.676441,6.646697,0.971611,7.568211,-0.382839,8.439191,-9.556749,5.700603,-9.785425,2.617555,-4.201264,-9.974166,-5.412640,0.574544,5.721518,-4.681284,1.077052,7.716495,-0.698252,7.121738,-5.943274,-1.143531,0.311960,7.732922,-3.389465,8.141051,-6.834597,3.990212,1.836588,8.697567,-6.957783,-6.553338,9.464045], dtype = "float32")#candidate|17367|(396,)|const|float32
call_17365 = relay.TupleGetItem(func_12828_call(relay.reshape(const_17366.astype('uint64'), [13, 10]), relay.reshape(const_17367.astype('float32'), [396,]), ), 3)
call_17368 = relay.TupleGetItem(func_12832_call(relay.reshape(const_17366.astype('uint64'), [13, 10]), relay.reshape(const_17367.astype('float32'), [396,]), ), 3)
output = relay.Tuple([call_17315,call_17365,const_17366,const_17367,])
output2 = relay.Tuple([call_17316,call_17368,const_17366,const_17367,])
func_17376 = relay.Function([], output)
mod['func_17376'] = func_17376
mod = relay.transform.InferType()(mod)
output = func_17376()
func_17377 = relay.Function([], output)
mutated_mod['func_17377'] = func_17377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15084_call = mod.get_global_var('func_15084')
func_15085_call = mutated_mod.get_global_var('func_15085')
call_17406 = relay.TupleGetItem(func_15084_call(), 0)
call_17407 = relay.TupleGetItem(func_15085_call(), 0)
func_3494_call = mod.get_global_var('func_3494')
func_3497_call = mutated_mod.get_global_var('func_3497')
const_17415 = relay.const([-8,2,8,3,4,8,-6,10,-8,2,-1,-7,3,-3,9,-5,-4,-2,10,-2,7,-8,7,-2,5,5,7,7,3,2,1,-9,-6,-9,8,-5,-3,7,10,-7,5,3,5,-6,9,8,-5,6,10,2,-7,3,7,-2,-1,-4,-10,-10,6,-1,4,-6,8,4,5,6,-10,-6,10,8,8,10,10,2,6,2,7,-10,-7,-3,-8,-8,1,-7,-1,-2,6,8,-2,1,-6,-7,-10,7,1,2,2,-8,-4,-4,10,6,10,2,-4,1,8,4,6,5,-3,7,-9,-10,3,-9,-2,1,-1,-5,7,-7,-3,-3,4,6,-7,5,-1,-8], dtype = "uint64")#candidate|17415|(130,)|const|uint64
const_17416 = relay.const([[-10,-7,-6,6,-9,-1,4,10,6,-1,-7,2,-7,-2,6,8,4,8,8,-4,-6,4,8,-3,3,1,1,3,-10,10,3,-3,-5,1,-6,2,1,1,10,-4,-10,-3,10,2,9,7,1,-2,-10,2,7,-9,10,8,6,2,-8,-10,1,8,3,5,-5,2,10,-5,-6,7,-4,5,-6,-7,-4,-5,-6,-8,-10,7,-1,-3,1,-2,-2,-4,-4,4,7,-6,-8,-7,-6,7,7,-1,1,1,-4,10,2,10,-2,-7,8,10,-6,2,2,-8,-1,7,-5,-5,-1,-4,-8,6,3,-1,-7,-8,-7,-5,-2,-8,-3,7,5,-6,-7,-9],[7,9,1,2,10,-2,-2,8,9,-9,4,10,-7,8,-9,3,2,-7,-9,-2,-10,-9,-1,-8,-4,-5,-2,8,3,5,2,-9,9,9,6,-8,6,-3,-4,-7,10,7,-7,1,-2,2,-4,10,9,-1,3,-3,7,-3,-9,-9,4,-8,10,1,-8,8,5,7,-9,9,10,-8,8,-9,-4,5,-2,-1,6,8,6,-8,-4,-3,7,-5,-5,-5,-6,1,1,-10,-1,-9,2,1,-3,-8,-5,-2,-4,9,-1,2,9,9,-1,4,9,-9,3,10,-10,-3,-1,7,-1,7,-3,9,-2,3,-7,-5,2,-9,5,-1,10,-10,-8,-8,-5,10],[4,1,6,-1,-1,-9,-10,8,-10,10,2,10,-7,8,1,-2,-7,-1,7,8,-8,-10,7,-6,6,4,-4,-7,-3,2,3,1,7,3,-3,1,-7,-2,3,-1,1,-9,2,-7,1,2,-5,3,4,7,6,1,-3,10,-2,-4,-8,10,-9,6,-6,5,1,5,-4,5,4,-7,-2,2,-8,6,1,6,3,-1,10,2,6,9,4,3,-3,-5,-5,-6,5,-1,-6,-8,8,-9,7,-4,-9,-4,8,-10,-6,-3,-2,-8,-10,3,5,-6,3,3,-5,3,-9,-8,4,7,3,-5,-8,-3,-9,6,-10,-8,6,-2,-8,6,4,6,3,10],[-3,2,7,10,4,1,-8,4,10,-6,3,-8,7,-6,7,-6,-2,-2,6,8,-9,1,-10,1,2,-10,1,-3,4,-1,-9,1,-7,-4,-6,10,-3,-3,7,3,-1,-6,3,-3,1,9,-2,3,5,2,-10,-7,5,-6,-3,-4,3,9,1,4,5,-4,-4,-6,-4,10,-3,7,-4,10,1,2,-4,-2,2,-7,-9,-3,7,2,10,-5,7,-10,-2,-8,4,7,-2,5,4,2,2,-6,7,-2,10,-9,-9,7,9,4,-9,3,1,5,9,-1,-3,2,5,-6,-9,-1,3,-10,5,-6,-9,4,-5,7,4,-5,-5,6,10,2,-8,10],[10,2,5,10,6,-8,-4,-7,3,7,8,7,-7,9,-3,-5,-8,10,6,1,-3,3,2,-8,-1,-4,-8,8,9,9,6,-4,-2,10,-4,9,8,7,-1,6,7,4,-10,-9,2,2,3,-2,10,-4,-1,-4,-5,10,3,10,9,-5,6,9,-5,6,6,-4,10,-1,-1,1,-3,9,-10,-7,-3,-7,8,7,-4,1,10,4,-3,10,-9,7,-3,-7,-7,1,7,-1,1,-8,10,5,-5,10,6,-2,-3,5,9,-1,8,-6,-10,-10,4,8,-7,6,3,-2,7,4,-6,8,-2,-2,2,7,-7,-7,-7,7,-7,8,8,-9,-5,-7],[-1,-6,5,-5,-8,-1,9,7,4,-2,6,2,-9,1,5,6,-2,-1,10,5,10,4,5,-7,-7,9,8,-9,4,2,-7,-7,1,-5,-6,1,-6,7,-10,10,5,1,3,-10,-10,-6,1,6,-3,-4,-1,7,4,1,-10,1,2,-7,-2,2,1,8,3,-5,7,5,6,7,6,4,-1,-9,7,-10,5,2,1,-10,-6,-1,6,-10,6,4,5,7,-3,1,-2,-8,4,-3,-1,-1,7,9,8,6,7,5,8,-10,-8,-10,3,-5,9,3,-10,7,6,1,-5,7,8,6,6,8,6,-4,7,5,7,6,-2,-5,8,10,6,5],[-1,-2,6,3,-8,-2,-6,3,-5,-3,5,-5,7,-6,5,6,2,-5,8,2,-4,-2,-1,6,-7,5,8,-5,-7,7,-2,-10,-9,-5,-4,2,1,-10,1,10,-4,10,-5,6,-5,4,4,-2,-10,1,-3,-3,8,-7,-7,9,-2,-3,3,10,2,3,-9,-10,-3,-4,5,9,9,2,-2,9,-9,2,-2,8,-8,2,8,-8,-5,7,10,-3,1,6,6,9,8,7,-6,7,-8,5,3,6,8,7,-9,-8,8,6,-9,-9,-10,8,9,-4,-4,-2,-2,4,4,-7,-2,3,-7,3,-8,3,-7,8,6,-5,-8,-7,9,-10,3,-4],[-10,-6,-10,5,1,7,-10,-8,-6,-7,3,-7,-5,3,-2,-2,6,1,7,5,3,8,7,-10,-10,-9,2,3,-1,-5,5,-7,-7,6,-2,4,5,9,-9,-6,7,-1,-9,6,3,5,1,9,-8,-2,8,-8,-9,4,7,8,-5,-2,-3,6,-2,-4,-1,-10,9,-1,-9,1,-5,7,-7,7,2,-6,-10,5,-1,4,3,3,6,-1,3,3,7,2,-3,-5,8,3,4,-1,-6,-1,1,-1,9,1,1,2,6,-1,-4,-5,10,2,6,10,-10,-1,6,9,-1,7,-6,10,-6,-10,-9,-5,-5,-2,-4,-4,-5,7,-8,-7,7,-3],[-7,-5,-5,-3,4,-3,7,-1,-10,-5,-2,8,-7,9,1,8,-4,-8,10,3,-1,2,-4,9,9,-8,-6,-1,1,10,-1,-9,1,-5,-1,4,7,-10,-8,2,4,-8,-8,5,10,-3,-4,-7,-2,-6,1,4,6,8,4,-3,3,9,2,-3,1,-5,-8,10,3,2,-3,-3,-10,-3,2,-3,9,6,-9,-4,-5,-3,-1,5,-8,9,3,10,-4,10,-1,3,-6,-1,-8,-5,-6,-7,3,1,1,3,-4,9,-10,-6,-3,-10,7,-6,-8,9,-1,-1,2,-6,-3,-7,1,-7,-7,1,3,1,-7,-9,7,-9,8,-3,-3,1,7,5],[4,-9,6,-10,-5,2,-9,-7,1,-7,7,7,-8,-5,6,2,-1,-2,-5,7,7,-10,-10,-3,4,-8,-9,-10,-5,1,-7,5,6,-7,2,-10,5,5,8,6,9,2,1,8,-1,9,-4,7,2,2,10,-4,4,10,-9,-6,10,-8,-2,-9,5,-2,-10,10,3,-5,6,5,9,1,-2,8,-7,-5,3,3,-9,9,-1,1,-3,-4,8,-8,-5,-4,-8,-8,-9,3,4,1,8,-5,1,3,-4,2,6,-6,-8,7,5,10,-10,-7,8,10,-10,-5,10,-6,4,-6,-9,-3,-5,5,-8,3,8,4,7,-2,-8,-9,-4,5,-6,-8]], dtype = "uint64")#candidate|17416|(10, 130)|const|uint64
call_17414 = func_3494_call(relay.reshape(const_17415.astype('uint64'), [10, 13, 1]), relay.reshape(const_17416.astype('uint64'), [10, 13, 10]), )
call_17417 = func_3494_call(relay.reshape(const_17415.astype('uint64'), [10, 13, 1]), relay.reshape(const_17416.astype('uint64'), [10, 13, 10]), )
uop_17420 = relay.atanh(const_17416.astype('float64')) # shape=(10, 130)
func_13782_call = mod.get_global_var('func_13782')
func_13785_call = mutated_mod.get_global_var('func_13785')
const_17428 = relay.const([[4.260583],[-6.857775],[9.406663],[-2.257079],[7.827563],[4.514940],[-4.814649],[3.896375],[-4.560506],[1.832591],[-3.913623],[0.848225],[-7.449245],[-8.565597],[1.112802],[-3.710555],[0.781740],[-6.588239],[6.162078],[-6.358088],[8.531830],[7.884681],[-5.396099],[-3.936664],[1.099213],[-4.391849],[-2.940899],[6.723164],[-7.037906],[-3.816229],[-2.507497],[8.779222],[7.250031],[-8.718531],[-0.399894],[-9.480671],[6.338595],[3.930836],[-3.851733],[-2.987530],[1.692052],[-2.400543],[-3.586216],[-2.074239],[1.107510],[-0.211343],[3.789198],[4.057802],[-6.264802],[-3.199385],[-8.047001],[-4.001303],[-9.282190],[9.159744],[8.575418],[-1.691433],[-9.283017],[0.599601],[-3.223391],[3.122459],[-0.812358],[-1.979758],[0.786655],[-0.522218],[3.063045],[-2.841094],[4.262137],[6.901444],[-7.683118],[4.313976],[6.933724],[-9.022924],[-5.347644],[-8.032420],[0.236353],[-3.568077],[-5.773557],[-6.530806],[-6.241440],[2.586635],[9.631346],[2.445522],[-5.277344],[-3.087039],[2.525213],[-8.374422],[0.637038],[-8.867002],[-5.120473],[-7.977052],[-6.161196],[9.188794],[9.402263],[5.870358],[7.219434],[-5.226767],[-7.174839],[5.496168],[-5.081630],[-9.329101],[6.507026],[-1.561086],[2.401899],[-2.782883],[-5.034886],[-8.039023],[7.752679],[8.316264],[6.472292],[-1.387162],[3.836142],[4.256451],[-7.340065],[-4.497381],[-7.602223],[-9.400376],[6.825954],[-3.228478],[1.670339],[3.021092],[5.677016],[1.598233],[1.480616],[-7.295899],[5.049457],[1.794646],[2.798403],[-1.368603],[-6.547599],[-1.430353],[1.317219],[-0.415628],[-5.864400],[-1.099166],[-7.707231],[1.803446],[6.583528],[-5.579435],[6.901971],[2.735089],[-2.075665],[6.629531],[2.314839],[6.747288],[-0.538807],[-4.793493],[0.760628],[-4.936612],[2.498165],[5.666884],[-2.483173],[1.153436],[3.036440],[0.846723],[-2.905705],[1.751360],[5.187765],[-6.896704],[5.510651],[-8.096152],[-6.707493],[2.764288],[-8.716441],[2.882457],[-3.256329],[8.349701],[1.783343],[-6.804959],[-2.527261],[5.446257],[-4.724962],[8.888925],[5.626967],[-9.639673],[-5.446513],[-7.545129],[5.537679],[-7.439222],[0.057988],[8.490073],[-0.521353],[7.892230],[-6.842616],[1.402893],[5.301078],[7.766243],[6.983652],[7.593745],[5.484412],[8.373905],[8.473402],[-5.680038],[-0.524191],[-6.870077],[-4.468709],[3.144123],[-9.974617],[-0.218611],[2.136870],[9.071629],[-4.825828],[-7.532943],[-3.352412],[-1.338719],[-6.037211],[6.911660],[2.601751],[-9.209536],[-4.156438],[6.787664],[4.171307],[6.524285],[1.009410],[-7.558768],[8.870056],[6.491521],[-2.259973],[-4.690051],[-8.713185],[-6.475658],[-3.949987],[-6.261074],[3.862970],[2.368630],[8.314721],[-9.822568],[-7.430139],[-3.272521],[1.351011],[-3.763877],[-6.535779],[-4.948113],[7.788530],[6.258927],[7.468852],[-6.871574],[1.422057],[4.979347],[-5.797495],[-5.759285],[-6.191380],[-1.431402],[1.766207],[-2.722078],[0.098452],[8.930619],[8.652019],[-8.359341],[-0.588029],[-1.284474],[-0.183747],[-4.262219],[0.401549],[-0.016480],[-0.044053],[5.550004],[-7.165216],[3.252708],[-0.331732],[-7.684156],[-0.654836],[0.067446],[-2.500902],[6.779595],[-3.262081],[-9.408906],[-1.959859],[-0.307062],[8.977077],[2.483758],[-6.544737],[-5.136157],[-1.396826],[-5.076726],[2.685261],[-0.326746],[-3.376729],[1.196743],[-2.904733],[-3.755247],[-4.928704],[4.181164],[8.269842],[-3.766129],[-2.917945],[-8.539357],[-0.468406],[0.005808],[6.473365],[7.782741],[5.428458],[-9.214878],[-5.434404],[-2.032368],[-7.452687],[1.859230],[3.303420],[-8.902082],[-1.451187],[0.573972],[-0.244708],[8.019987],[-0.891808],[-3.111955],[-1.009273],[2.285851],[8.438226],[-6.987314],[4.800256],[-0.928165],[5.997572],[6.424493],[-9.755806],[0.168684],[-4.943168],[-3.987585],[-4.708731],[-6.045411],[-6.311923],[-1.080041]], dtype = "float64")#candidate|17428|(320, 1)|const|float64
call_17427 = relay.TupleGetItem(func_13782_call(relay.reshape(const_17428.astype('float64'), [8, 5, 8])), 0)
call_17429 = relay.TupleGetItem(func_13785_call(relay.reshape(const_17428.astype('float64'), [8, 5, 8])), 0)
func_12133_call = mod.get_global_var('func_12133')
func_12137_call = mutated_mod.get_global_var('func_12137')
const_17435 = relay.const(-6, dtype = "int16")#candidate|17435|()|const|int16
var_17436 = relay.var("var_17436", dtype = "uint64", shape = (8, 20))#candidate|17436|(8, 20)|var|uint64
call_17434 = relay.TupleGetItem(func_12133_call(relay.reshape(const_17435.astype('int16'), []), relay.reshape(var_17436.astype('uint64'), [160,]), ), 2)
call_17437 = relay.TupleGetItem(func_12137_call(relay.reshape(const_17435.astype('int16'), []), relay.reshape(var_17436.astype('uint64'), [160,]), ), 2)
uop_17438 = relay.acos(uop_17420.astype('float64')) # shape=(10, 130)
func_12848_call = mod.get_global_var('func_12848')
func_12850_call = mutated_mod.get_global_var('func_12850')
call_17446 = func_12848_call()
call_17447 = func_12848_call()
bop_17449 = relay.greater(uop_17438.astype('bool'), relay.reshape(const_17416.astype('bool'), relay.shape_of(uop_17438))) # shape=(10, 130)
func_13349_call = mod.get_global_var('func_13349')
func_13353_call = mutated_mod.get_global_var('func_13353')
var_17457 = relay.var("var_17457", dtype = "float64", shape = (1008,))#candidate|17457|(1008,)|var|float64
call_17456 = relay.TupleGetItem(func_13349_call(relay.reshape(var_17457.astype('float64'), [1008,]), relay.reshape(var_17436.astype('uint64'), [160,]), ), 0)
call_17458 = relay.TupleGetItem(func_13353_call(relay.reshape(var_17457.astype('float64'), [1008,]), relay.reshape(var_17436.astype('uint64'), [160,]), ), 0)
output = relay.Tuple([call_17406,call_17414,const_17415,call_17427,const_17428,call_17434,const_17435,var_17436,call_17446,bop_17449,call_17456,var_17457,])
output2 = relay.Tuple([call_17407,call_17417,const_17415,call_17429,const_17428,call_17437,const_17435,var_17436,call_17447,bop_17449,call_17458,var_17457,])
func_17461 = relay.Function([var_17436,var_17457,], output)
mod['func_17461'] = func_17461
mod = relay.transform.InferType()(mod)
mutated_mod['func_17461'] = func_17461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17461_call = mutated_mod.get_global_var('func_17461')
var_17463 = relay.var("var_17463", dtype = "uint64", shape = (8, 20))#candidate|17463|(8, 20)|var|uint64
var_17464 = relay.var("var_17464", dtype = "float64", shape = (1008,))#candidate|17464|(1008,)|var|float64
call_17462 = func_17461_call(var_17463,var_17464,)
output = call_17462
func_17465 = relay.Function([var_17463,var_17464,], output)
mutated_mod['func_17465'] = func_17465
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14996_call = mod.get_global_var('func_14996')
func_14998_call = mutated_mod.get_global_var('func_14998')
call_17488 = func_14996_call()
call_17489 = func_14996_call()
output = relay.Tuple([call_17488,])
output2 = relay.Tuple([call_17489,])
func_17500 = relay.Function([], output)
mod['func_17500'] = func_17500
mod = relay.transform.InferType()(mod)
output = func_17500()
func_17501 = relay.Function([], output)
mutated_mod['func_17501'] = func_17501
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11804_call = mod.get_global_var('func_11804')
func_11806_call = mutated_mod.get_global_var('func_11806')
call_17602 = relay.TupleGetItem(func_11804_call(), 0)
call_17603 = relay.TupleGetItem(func_11806_call(), 0)
output = relay.Tuple([call_17602,])
output2 = relay.Tuple([call_17603,])
func_17630 = relay.Function([], output)
mod['func_17630'] = func_17630
mod = relay.transform.InferType()(mod)
mutated_mod['func_17630'] = func_17630
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17630_call = mutated_mod.get_global_var('func_17630')
call_17631 = func_17630_call()
output = call_17631
func_17632 = relay.Function([], output)
mutated_mod['func_17632'] = func_17632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11804_call = mod.get_global_var('func_11804')
func_11806_call = mutated_mod.get_global_var('func_11806')
call_17697 = relay.TupleGetItem(func_11804_call(), 0)
call_17698 = relay.TupleGetItem(func_11806_call(), 0)
output = relay.Tuple([call_17697,])
output2 = relay.Tuple([call_17698,])
func_17702 = relay.Function([], output)
mod['func_17702'] = func_17702
mod = relay.transform.InferType()(mod)
mutated_mod['func_17702'] = func_17702
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17702_call = mutated_mod.get_global_var('func_17702')
call_17703 = func_17702_call()
output = call_17703
func_17704 = relay.Function([], output)
mutated_mod['func_17704'] = func_17704
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17734 = relay.var("var_17734", dtype = "int16", shape = (10, 4, 5))#candidate|17734|(10, 4, 5)|var|int16
var_17735 = relay.var("var_17735", dtype = "int16", shape = (10, 4, 5))#candidate|17735|(10, 4, 5)|var|int16
bop_17736 = relay.greater(var_17734.astype('bool'), relay.reshape(var_17735.astype('bool'), relay.shape_of(var_17734))) # shape=(10, 4, 5)
func_12617_call = mod.get_global_var('func_12617')
func_12619_call = mutated_mod.get_global_var('func_12619')
call_17740 = func_12617_call()
call_17741 = func_12617_call()
output = relay.Tuple([bop_17736,call_17740,])
output2 = relay.Tuple([bop_17736,call_17741,])
func_17742 = relay.Function([var_17734,var_17735,], output)
mod['func_17742'] = func_17742
mod = relay.transform.InferType()(mod)
var_17743 = relay.var("var_17743", dtype = "int16", shape = (10, 4, 5))#candidate|17743|(10, 4, 5)|var|int16
var_17744 = relay.var("var_17744", dtype = "int16", shape = (10, 4, 5))#candidate|17744|(10, 4, 5)|var|int16
output = func_17742(var_17743,var_17744,)
func_17745 = relay.Function([var_17743,var_17744,], output)
mutated_mod['func_17745'] = func_17745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11833_call = mod.get_global_var('func_11833')
func_11835_call = mutated_mod.get_global_var('func_11835')
call_17782 = relay.TupleGetItem(func_11833_call(), 0)
call_17783 = relay.TupleGetItem(func_11835_call(), 0)
output = relay.Tuple([call_17782,])
output2 = relay.Tuple([call_17783,])
func_17788 = relay.Function([], output)
mod['func_17788'] = func_17788
mod = relay.transform.InferType()(mod)
output = func_17788()
func_17789 = relay.Function([], output)
mutated_mod['func_17789'] = func_17789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11459_call = mod.get_global_var('func_11459')
func_11460_call = mutated_mod.get_global_var('func_11460')
call_17821 = relay.TupleGetItem(func_11459_call(), 0)
call_17822 = relay.TupleGetItem(func_11460_call(), 0)
func_6921_call = mod.get_global_var('func_6921')
func_6924_call = mutated_mod.get_global_var('func_6924')
const_17834 = relay.const([-7.490870,0.831366,-9.076397,-6.199417,7.665553,-5.554320,-8.622730,5.160361,-9.081433,-1.408618,-3.744674,0.601365,6.971711,0.986110,1.485399,-7.038655,-3.700641,0.791498,4.616503,8.969349,2.103982,5.485221,7.926840,-1.926498,-5.643454,7.842518,2.613804,7.820548,-2.436160,9.252328,8.550196,-8.018193,2.319710,-6.849295,1.026002,3.156937,-2.847259,-5.336173,-7.174476,4.244553,-3.110657,0.376342,4.325310,-8.806094,4.788117,0.119498,8.161370,-5.136306,9.153462,2.796824,7.406943,-8.253619,5.068187,4.380315,0.591549,7.843391,-3.128027,3.037551,8.897559,8.388991,9.387342,8.650502,-3.263780,2.136525,-1.860306,-2.337323,-9.890190,1.670920,-3.311452,1.817868,3.189342,5.253368,4.639675,8.892770,-8.273338,9.719979,-0.151895,-4.346840,-6.306322,-2.755877,-6.554812,-3.300784,6.646678,5.304224,2.004776,1.421667,5.049171,-1.823260,4.855296,5.490245,-9.626102,5.297245,0.666350,-3.448176,-1.816476,-7.452666,6.063161,3.101237,3.928756,-8.664531,3.299211,6.295085,-8.302801,2.422858,-5.682980,9.269657,3.451632,7.111257,-8.192234,-9.375704,-2.686705,-1.173404,-3.294219,3.892750,-7.119745,-2.332663,8.302383,-4.663962,6.020754,-1.158921,-0.817893,-7.348968,-5.843269,-0.389477,5.189676,4.235958,4.975450,-5.161783,9.916159,8.954498,3.416700,6.216295,-6.694413,7.924809,2.904914,3.702358,0.653485,2.955101,7.653493,7.262395,9.037852,-0.812435,-9.365639,-7.690895,-1.108044,2.893643,0.506630,7.634861,-8.521592,1.496575,-3.166582,3.685256,-4.499702,1.126500,-1.780625,7.933049,-5.174946,-9.040993,-6.894906,-8.666850,5.431465,-9.381029,0.155270,-5.096835,-6.543863,4.293036,-4.106931,2.919793,-8.883008,-8.117375,9.468594,-1.911768,7.793269,-1.318657,8.859157,0.517559,-5.311025,4.296255,5.805969,9.811681,2.239545,-1.389789,5.443513,-5.312762,-2.972603,-9.085221,-2.371656,5.853437,5.961959,4.127719,7.184385,4.033905,8.145710,4.684083,-2.948880,-0.938448,1.000095,0.355484,-3.185621,-7.422422,-6.108772,-7.623706,0.682374,3.450463,4.096173,4.008975,0.319122,-6.700676,9.865382,1.978987,-6.280699,4.060414,-1.355151,-3.544590,3.473748,7.581201,0.079781,-6.861271,-5.789889,-0.808188,5.705407,-8.425420,-0.336596,9.179898,-1.236850,-6.617063,-4.580650,-0.495982,-7.770917,-9.325991,-0.287616,-5.708924,4.338398,-5.129377,-8.947723,-9.878425,7.485067,-8.111249,8.862358,6.003216,-0.031054,4.833751,-8.488992,2.377068,-6.715299,-1.565058,5.254659,7.956925,4.500928,-3.644916,-7.710421,0.008416,6.003298,7.332661,8.865361,-2.364212,-0.417827,9.475359,-4.133698,-9.918793,-8.646598,3.537368,7.351722,-9.384978,-2.917063,-5.916534,7.700920,-2.143746,7.012649,-6.168357,8.954700,-8.890620,-9.706187,-6.437049,-9.726539,3.698932,4.072935,-9.866033,2.961826,8.862952,-5.891158,-4.439688,-7.048176,-0.128818,2.234684,-9.185906,-5.800569,-2.615385,-6.099538,5.006732,9.190217,5.130582,2.962962,2.615388,1.839515,-4.903134,-0.778346,2.603803,-1.984467,-7.334155,-0.550806,-4.293408,0.756093,6.315721,7.239562,-2.003895,-9.094338,6.255908,-2.660759,-2.502270,4.704426,4.063769,-7.139821,-9.741383,-6.129590,-6.783397,-3.366689,6.068826,4.718115,5.591147,7.806224,-7.494393,-6.537694,6.523718,-4.128795,-1.344249,8.592358,-4.132306,-9.923287,-7.555970,6.440543,-9.550074,5.758235,-3.851083,-6.836700,3.998441,1.336275,1.769370,4.883906,-0.398532,8.966709,1.483754,-3.092546,-6.681497,5.666658,-2.648282,3.942390,-5.801891,-1.789913,3.608762,-3.512740,3.826871,-0.661354,1.623129,0.293775,-9.648429,-8.438775,7.313073,3.465810,-4.318259,-1.845008,4.941614,7.341163,-6.081503,-7.868019,-7.750612,-6.621531,2.345167,9.156624,-7.106881,-3.867204,1.890207,0.996310,-9.944646,-2.705221,0.605255,0.562083,-5.594672,-4.711516,-3.789557,-2.780788,4.899694,-8.806197,-1.494901,-5.580268,8.278574,1.462896,8.326381,5.356189,1.663057,-5.116308,7.685861,7.315527,-3.501843,-2.287475,1.220417,-8.633063,-8.938092,5.643666,-4.806787,9.718963,-3.655545,-2.908239,3.069530,2.402297,7.979786,5.144879,5.360352,-7.894092,-8.717407,5.247935,5.604190,2.931823,-5.973682,-6.050099,-9.315668,-6.561634,-9.324752,-6.365416,3.575271,-1.147565,-3.429032,0.309491,3.108623,7.308784,-9.185659,7.073920,-3.997637,0.058611,5.870587,5.769143,-3.897537,-0.740487,-8.647900,-9.898678,1.228587,-1.935081,5.101776,0.603815,3.263228,-9.782829,0.636655,-1.054098,-3.560733,0.194316,9.239207,0.697346,-4.596866,8.631390,0.909038,-2.083334,-1.100942,-3.484766,-5.623345,-5.952657,-2.034933,-1.324798,-9.575136,-7.998837,-9.471385,-8.966849,-9.190063,4.881122,-0.185676,-8.606038,0.976126,-4.793893,1.019998,9.560311,-8.154466,-6.442160,-6.274297,7.989395,8.575739,-8.585183,9.535380,9.324999,-5.173607,-1.657808,9.814016,-9.739392,-4.616929,0.344657,7.130594,7.812012,-0.834535,5.698724,-2.300153,-9.002350,-2.936636,-8.994620,9.962499,1.960283,-9.585982,-2.561539,-2.972134,-1.510649,8.919551,8.720746,-7.239955,0.802208,-8.399553,-4.310540,8.796769,-9.295867,8.370844,5.390587,-7.945832,-4.619714,-2.905099,8.555790,-1.069671,4.427537,6.045365,-9.725453,-7.244511,-3.795463,-7.327658,2.109334,3.702557,1.449765,-8.571910,-5.998218,-8.796095,-4.213620,5.252719,8.193503,3.130550,-8.531697,5.849922,8.533183,-7.779339,-5.825882,-5.450012,-5.349581,1.103107,-4.010378,-4.484163,5.087175,8.173912,8.618872,6.482838,-2.138270,-1.907635,0.865389,-4.478069,1.849060,-2.709856,7.903322,9.820113,0.660591,-5.597591,7.658233,-1.314657,9.230463,-5.863664,-0.098291,7.385978,-9.396283,2.161770,-8.176954,-5.926303,-4.489333,6.038453,2.300242,4.341086,-4.312641,-1.185127,-6.952360,-1.364671,2.803355,8.740017,-4.598230,-2.970988,-1.730144,-8.487907,0.333641,-1.155935,1.127320,-9.028712,-5.513938,5.789073,1.401663,-5.099427,-4.247377,6.703231,9.927365,-5.213929,6.532678,4.859346,-0.931025,-0.451458,-7.986034,-8.002978,2.942089,3.558322,-3.131286,-2.177333,-1.646521,-2.905768,7.562619,-5.974405,-5.181220,-1.033586,-8.077895,6.366121,4.917915,-3.375481,-8.467985,7.326138,2.611264,4.471292,-1.797593,2.337688,3.495251,7.422512,4.543742,1.092752,-5.950946,-7.732491,1.621955,-0.841803,9.702871,5.962940,6.677037,8.806148,9.323854,-7.295034,-6.787452,-2.814572,2.676933,-6.518857,-3.735154,-5.730524,0.642810,4.592267,-6.532904,6.855734,-2.959314,9.944413,-4.863427,1.990229,-0.564694,5.085073,2.152147,-7.019994,6.990818,-7.345693,-5.028455,6.580055,6.133126,0.305954,-5.644936,9.444342,0.642169,-9.250390,-9.379462,6.295158,2.197100,6.118372,-2.722055,-4.925466,5.515335,4.812285,3.280434,2.997727,0.588677,5.718229,-0.515212,2.101700,2.807760,4.514619,9.290742,-5.990925,8.512161,1.963813,6.954749,2.667064,-3.828528,4.858878,9.042286,-8.762626,4.962232,-7.970281,9.413807,3.902115,8.351567,-6.977472,7.446397,-6.452428,-8.272653,-4.187665,9.878444,-5.411747,6.366354,8.798989,4.600139,3.007116,2.836985,-4.941909,5.193562,-0.044492,-0.232059,6.337914,1.470741,-0.990635,-5.839465,-5.965472,-2.925429,7.135637,-0.769160,6.867033,4.428516,-9.226948,-1.719726,4.417563,-7.854838,4.000105,-4.722071,-1.144226,-5.437623,9.813910,7.081599,-1.181110,2.133167,9.065670,-2.246838,3.112539,-4.562831,0.567602,-4.340132,-0.778390,-2.366893,0.182287,3.184750,-1.745634,-3.650179,-6.326738,6.295019,4.117696,-3.015920,-4.286347,3.559227,-3.986316,9.681743,3.481135,-5.446206,-9.089469,5.941245,0.645453], dtype = "float32")#candidate|17834|(750,)|const|float32
call_17833 = relay.TupleGetItem(func_6921_call(relay.reshape(const_17834.astype('float32'), [15, 5, 10])), 0)
call_17835 = relay.TupleGetItem(func_6924_call(relay.reshape(const_17834.astype('float32'), [15, 5, 10])), 0)
func_12956_call = mod.get_global_var('func_12956')
func_12958_call = mutated_mod.get_global_var('func_12958')
call_17838 = relay.TupleGetItem(func_12956_call(), 0)
call_17839 = relay.TupleGetItem(func_12958_call(), 0)
output = relay.Tuple([call_17821,call_17833,const_17834,call_17838,])
output2 = relay.Tuple([call_17822,call_17835,const_17834,call_17839,])
func_17844 = relay.Function([], output)
mod['func_17844'] = func_17844
mod = relay.transform.InferType()(mod)
output = func_17844()
func_17845 = relay.Function([], output)
mutated_mod['func_17845'] = func_17845
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11804_call = mod.get_global_var('func_11804')
func_11806_call = mutated_mod.get_global_var('func_11806')
call_17855 = relay.TupleGetItem(func_11804_call(), 0)
call_17856 = relay.TupleGetItem(func_11806_call(), 0)
output = relay.Tuple([call_17855,])
output2 = relay.Tuple([call_17856,])
func_17861 = relay.Function([], output)
mod['func_17861'] = func_17861
mod = relay.transform.InferType()(mod)
mutated_mod['func_17861'] = func_17861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17861_call = mutated_mod.get_global_var('func_17861')
call_17862 = func_17861_call()
output = call_17862
func_17863 = relay.Function([], output)
mutated_mod['func_17863'] = func_17863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15647_call = mod.get_global_var('func_15647')
func_15649_call = mutated_mod.get_global_var('func_15649')
call_17864 = relay.TupleGetItem(func_15647_call(), 0)
call_17865 = relay.TupleGetItem(func_15649_call(), 0)
func_15367_call = mod.get_global_var('func_15367')
func_15370_call = mutated_mod.get_global_var('func_15370')
const_17871 = relay.const([1.863748,3.055675,-3.079250,-4.445007,-0.414189,1.768248,8.852324,8.907214,2.231651,6.913852,0.460693,7.326977,3.914132,-7.024590,1.820261,1.804716,-2.272159,-6.368451,2.783311,-2.973735,-8.583928,7.019200,-2.833339,5.919549,5.292030,-7.989662,-1.211914,7.379975,-1.856411,-1.757672,9.214441,-4.542955,0.511422,-5.850983,7.182877,-5.286710,-8.318081,-5.594774,-4.528342,5.471662,-3.747485,-8.126357,4.887054,-3.392167,2.007707,1.970684,-0.522387,-4.307058,-3.959997,-1.421648,-4.628235,-9.525810,6.877225,1.401406,-8.992257,8.827211,-5.145488,2.358533,6.509391,6.481448,0.433492,8.035907,-0.855154,8.096954,0.743718,8.904452,-6.241592,-8.407524,-3.754760,5.574487,-3.583333,9.714362,-5.825233,2.543543,-3.961756,-0.101598,9.834117,-6.182282,5.935706,7.972967,5.957406,-6.970228,-0.255519,3.453391,6.962388,4.609896,-0.134119,-1.382165,-2.040419,-7.325008,0.892810,-5.848158,6.628054,-3.330987,-9.414331,6.629615,-1.126930,3.696498,-4.344326,9.303839,9.720004,-1.532509,4.196013,-9.423267,-7.310671,6.088340,3.744171,-0.506879,-1.214798,4.945545,-2.679437,-9.102406,9.081703,3.505082,5.568944,4.155957,-5.671010,-5.298372,-3.469287,0.846907,9.357059,-4.143975,-2.372664,0.044877,-9.935272,6.975969,2.174737,5.160410,8.317415,1.495735,-3.443940,1.221782,-8.490111,-6.315126,-8.853442,4.433884,-9.019991,-9.330929,-3.183932,6.476322,-8.501705,-0.888954,0.196471,-7.170405,-9.680034,3.701858,-0.507605,4.050425,-9.688006,-5.756343,6.093357,-0.425532,9.034721,-5.949597,2.186079,-6.802348,-8.255771,4.310135,7.092908,-6.069236,0.403945,-3.185291,-0.293005,-3.371284,6.096984,3.947529,-2.730204,4.354332,-5.982992,-8.309470,3.576307,-5.642600,9.697349,2.518533,0.095960,-9.826125,8.889331,5.047812,0.699787,-0.535129,-8.751637,3.043422,-6.887499,-3.870358,4.059888,-2.208698,-3.645028,-7.718917,-6.495040,-8.474023,-8.412585,1.867733,2.817103,4.292708,-7.202006,4.425715,-5.253571,-5.706370,7.834361,6.875616,6.494458,-3.648754,-4.921034,8.440370,-1.215417,3.341978,-7.329360,7.950704,8.262821,-8.965789,-0.498798,-5.756237,4.973528,1.557567,4.924282,4.166650,-7.691775,-4.402602,-8.180108,-8.073546,7.886399,6.899498,-8.303149,2.655956,-4.377189,3.614373,-1.902068,2.475384,-1.212563,-3.326611,3.594219,-0.121733,5.462078,0.258013,-8.805113,4.772398,3.789795,-3.533903,9.209556,7.996068,5.218471,-9.088146,-5.693960,2.035218,2.020048,-1.327521,1.068007,-2.180784,-8.082339,8.064069,2.177800,-5.276754,4.934085,-0.990718,9.703700,-0.215290,1.237865,-7.911810,-3.676133,-7.452463,4.829042,6.623020,-4.756591,-3.568587,7.704367,9.033812,-2.456648,8.374591,-3.939632,-9.311298,9.568294,0.758947,1.416808,-2.205263,9.915489,6.277903,1.787513,-1.674154,4.372777,-0.921588,-1.295172,9.094463,-2.857581,-8.766494,3.306751,-9.433818,-6.519304,3.844746,9.961291,5.969062,-8.045317,4.011744,4.930208,8.973434,-6.769675,7.564601,-0.798233,4.711651,5.338434,9.422109,-0.121329,7.854004,1.093581,8.652420,-8.195522,-9.495581,2.032202,4.929012,4.508230,9.505249,-3.664458,-2.187965,-9.201817,7.479331,2.852556,-1.949610,-2.825951,-2.632785,-6.895130,-9.452950,0.956029,2.258139,2.041725,6.950248,-8.659421,-6.545444,-2.459302,3.618747,0.255348,-0.256638,8.831001,-5.889203,7.090230,-2.916098,-0.514174,-1.327406,7.350863,6.583679,-4.613735,0.685248,6.632212,-8.244571,-7.602248,-1.846605,-0.759214,-6.744822,7.045436,-4.984924,-1.202181,-1.378012,7.944527,-4.642903,8.062308,4.018191,-1.479193,-4.600219,8.978226,6.082285,-6.234724,5.535321,9.358447,-1.302985,-5.885202,3.800474,5.476858,-7.088747,-2.644992,7.068328,-4.221612,-3.479849,1.736524,-1.951627,4.766654,-3.305330,-1.001487,-1.667565,-4.544557,-8.732090,1.785428,6.588065,-2.649716,-6.996885,-8.743616,-3.297319,-5.657286,2.770003,9.258785,-6.516247,-4.724646,-3.469180,-9.660023,-1.790319,5.819090,-0.014914,-3.697421,-3.296362,7.532864,7.646312,-0.879207,-5.164039,-2.622860,6.336779,3.841726,-7.036371,-3.597895,-6.286480,-4.230346,2.947921,-8.920433,-6.208599,6.559186,0.021534,5.380800,-5.623327,-4.695718,5.554244,8.594456,-5.172283,-7.412733,-1.820306,7.372593,-2.505440,4.236219,4.067862,3.231130,-8.216090,-8.500603,8.260146,-0.801355,-3.003043,-1.353044,-7.569587,-5.633142,-3.769837,5.876558,1.816279,-5.837577,-2.817393,-1.952904,6.405486,-8.072954,-3.192958,3.399417,-7.804884,-3.199430,-7.428357,-0.558360,-9.393798,5.514080,-4.696490,0.247342,6.739671,3.269991,6.256743,0.873682,7.010109,-1.533420,2.252581,4.752853,5.181650,-3.266997,-3.448625,-8.538404,1.326581,1.988252,0.969974,6.558707,-8.236532,-0.675035,-5.242855,-5.116164,7.598904,-2.523966,-7.758740,8.171148,5.902058,8.836709,-3.102331,-1.532143,0.334325,5.495220,-8.455017,1.315683,6.644540,-1.728063,-6.112901,0.333390,3.199465,-7.598584,1.722879,2.047025,8.338028,-7.745109,4.443392,0.131689,2.125655,8.111789,8.367980,-6.589208,-7.380362,9.284295,-7.145173,6.422926,-6.576548,6.407800,2.220719,-6.532867,-0.639005,-6.292597,3.818028,-9.935526,0.714405,-1.220119,3.145032,9.868866,7.450003,-1.337030,-7.907289,6.890166,3.360906,-8.723700,2.041740,0.564169,-0.489419,7.338972,8.657210,-7.803644,2.364602,6.831174,8.447468,6.799985,1.186662,-9.522112,8.556004,-0.889566,3.228714,2.734753,5.252098,-3.485080,-0.735174,2.933155,5.114136,-6.019654,-4.579979,4.944666,0.347907,-8.501961,-0.976323,-6.303070,-6.441125,-9.880519,0.036656,8.264391,-5.595415,-8.079955,9.152591,-2.792959,3.807389,-1.680195,4.067063,-6.328396,-1.704620,1.155401,2.569116,-2.636578,2.771607,4.504101,-5.024487,1.675533,-4.241112,2.008270,-1.249042,5.463484,6.857027,0.226617,5.193869,2.693511,9.455471,2.663266,-6.984264,-5.490515,-1.282219,-2.910258,-4.010831,-9.968454,-8.328400,9.402904,9.970546,-2.033072,-9.188323,1.412291,4.076350,6.855776,-4.188315,-8.270267,-0.511809,-8.077214,-1.056649,8.843827,-9.725163,-4.659980,1.479782,9.758903,-6.360148,0.627338,-2.697353,-2.464883,9.298144,-6.586771,-5.820973,-0.871114,3.003206,-2.669645,-4.987961,1.656767,9.762933,9.825482,0.173602,9.944604,-1.548434,-9.366423,-1.496866,8.286624,-0.408498,4.740994,-5.287279,8.944486,-8.851278,4.503456,1.690453,2.759281,-5.296064,6.674986,-1.905450,5.365625,-6.785997,1.897681,4.059123,-6.229458,-3.012403,-5.636630,-0.834112,-5.945234,4.573226,9.850102,-9.313357,4.099825,1.052592,-1.014613,-8.698993,-4.778906,1.384913,8.871552,-8.817204,-2.268773,0.589200,4.513543,-2.776383,-9.986721,-9.166458,-8.356689,-7.784174,4.488434,5.723090,1.715970,-2.466440,-2.078695,1.864748,-5.361501,2.490622,-0.063588,1.563344,-9.267111,-8.033894,-1.327469,-2.026633,9.527014,-6.463824,-0.985839,7.049623,3.343893,-2.712625,7.790226,0.734083,8.166345,6.180114,6.964367,-5.961760,-1.857867,-6.867390,7.992344,-2.917230,-1.143774,2.802970,-8.509802,-4.811886,-0.820254,1.011434,5.332342,4.475177,0.487721,-8.916814,-8.761982,2.758649,5.551566,0.214395,-6.409444,-1.179835,-7.463832,-3.391334,-0.169950,8.408428,9.235462,-4.071876,4.426301,8.367872,-6.413666,-8.754430,-5.454203,-2.070975,1.858154,-9.598190,5.946156,-9.684009,5.036044,-9.572193,-7.356329,-4.686946,-0.299515,-8.893831,8.088718,-5.507847,3.528077,-4.258792,-7.967091,-3.861710,-3.871239,-3.328440,7.939290,2.929446,1.452815,-8.833127,7.042678,5.992812,5.674764,-5.680470,6.236759,4.027019,8.514744,7.752653], dtype = "float32")#candidate|17871|(750,)|const|float32
var_17872 = relay.var("var_17872", dtype = "float64", shape = (182,))#candidate|17872|(182,)|var|float64
call_17870 = relay.TupleGetItem(func_15367_call(relay.reshape(const_17871.astype('float32'), [750,]), relay.reshape(var_17872.astype('float64'), [13, 14]), ), 4)
call_17873 = relay.TupleGetItem(func_15370_call(relay.reshape(const_17871.astype('float32'), [750,]), relay.reshape(var_17872.astype('float64'), [13, 14]), ), 4)
func_12669_call = mod.get_global_var('func_12669')
func_12670_call = mutated_mod.get_global_var('func_12670')
call_17877 = func_12669_call()
call_17878 = func_12669_call()
output = relay.Tuple([call_17864,call_17870,const_17871,var_17872,call_17877,])
output2 = relay.Tuple([call_17865,call_17873,const_17871,var_17872,call_17878,])
func_17953 = relay.Function([var_17872,], output)
mod['func_17953'] = func_17953
mod = relay.transform.InferType()(mod)
mutated_mod['func_17953'] = func_17953
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17954 = relay.var("var_17954", dtype = "float64", shape = (182,))#candidate|17954|(182,)|var|float64
func_17953_call = mutated_mod.get_global_var('func_17953')
call_17955 = func_17953_call(var_17954)
output = call_17955
func_17956 = relay.Function([var_17954], output)
mutated_mod['func_17956'] = func_17956
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16338_call = mod.get_global_var('func_16338')
func_16339_call = mutated_mod.get_global_var('func_16339')
call_17976 = func_16338_call()
call_17977 = func_16338_call()
output = call_17976
output2 = call_17977
func_17982 = relay.Function([], output)
mod['func_17982'] = func_17982
mod = relay.transform.InferType()(mod)
output = func_17982()
func_17983 = relay.Function([], output)
mutated_mod['func_17983'] = func_17983
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17788_call = mod.get_global_var('func_17788')
func_17789_call = mutated_mod.get_global_var('func_17789')
call_17996 = relay.TupleGetItem(func_17788_call(), 0)
call_17997 = relay.TupleGetItem(func_17789_call(), 0)
output = call_17996
output2 = call_17997
func_18019 = relay.Function([], output)
mod['func_18019'] = func_18019
mod = relay.transform.InferType()(mod)
output = func_18019()
func_18020 = relay.Function([], output)
mutated_mod['func_18020'] = func_18020
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12653_call = mod.get_global_var('func_12653')
func_12655_call = mutated_mod.get_global_var('func_12655')
call_18028 = func_12653_call()
call_18029 = func_12653_call()
output = relay.Tuple([call_18028,])
output2 = relay.Tuple([call_18029,])
func_18037 = relay.Function([], output)
mod['func_18037'] = func_18037
mod = relay.transform.InferType()(mod)
mutated_mod['func_18037'] = func_18037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18037_call = mutated_mod.get_global_var('func_18037')
call_18038 = func_18037_call()
output = call_18038
func_18039 = relay.Function([], output)
mutated_mod['func_18039'] = func_18039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14375_call = mod.get_global_var('func_14375')
func_14376_call = mutated_mod.get_global_var('func_14376')
call_18048 = relay.TupleGetItem(func_14375_call(), 0)
call_18049 = relay.TupleGetItem(func_14376_call(), 0)
output = call_18048
output2 = call_18049
func_18051 = relay.Function([], output)
mod['func_18051'] = func_18051
mod = relay.transform.InferType()(mod)
mutated_mod['func_18051'] = func_18051
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18051_call = mutated_mod.get_global_var('func_18051')
call_18052 = func_18051_call()
output = call_18052
func_18053 = relay.Function([], output)
mutated_mod['func_18053'] = func_18053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13858_call = mod.get_global_var('func_13858')
func_13859_call = mutated_mod.get_global_var('func_13859')
call_18081 = func_13858_call()
call_18082 = func_13858_call()
uop_18089 = relay.asin(call_18081.astype('float32')) # shape=(9, 5, 14)
uop_18091 = relay.asin(call_18082.astype('float32')) # shape=(9, 5, 14)
func_17953_call = mod.get_global_var('func_17953')
func_17956_call = mutated_mod.get_global_var('func_17956')
var_18094 = relay.var("var_18094", dtype = "float64", shape = (182,))#candidate|18094|(182,)|var|float64
call_18093 = relay.TupleGetItem(func_17953_call(relay.reshape(var_18094.astype('float64'), [182,])), 0)
call_18095 = relay.TupleGetItem(func_17956_call(relay.reshape(var_18094.astype('float64'), [182,])), 0)
output = relay.Tuple([uop_18089,call_18093,var_18094,])
output2 = relay.Tuple([uop_18091,call_18095,var_18094,])
func_18119 = relay.Function([var_18094,], output)
mod['func_18119'] = func_18119
mod = relay.transform.InferType()(mod)
var_18120 = relay.var("var_18120", dtype = "float64", shape = (182,))#candidate|18120|(182,)|var|float64
output = func_18119(var_18120)
func_18121 = relay.Function([var_18120], output)
mutated_mod['func_18121'] = func_18121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15084_call = mod.get_global_var('func_15084')
func_15085_call = mutated_mod.get_global_var('func_15085')
call_18147 = relay.TupleGetItem(func_15084_call(), 2)
call_18148 = relay.TupleGetItem(func_15085_call(), 2)
func_17788_call = mod.get_global_var('func_17788')
func_17789_call = mutated_mod.get_global_var('func_17789')
call_18151 = relay.TupleGetItem(func_17788_call(), 0)
call_18152 = relay.TupleGetItem(func_17789_call(), 0)
output = relay.Tuple([call_18147,call_18151,])
output2 = relay.Tuple([call_18148,call_18152,])
func_18176 = relay.Function([], output)
mod['func_18176'] = func_18176
mod = relay.transform.InferType()(mod)
mutated_mod['func_18176'] = func_18176
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18176_call = mutated_mod.get_global_var('func_18176')
call_18177 = func_18176_call()
output = call_18177
func_18178 = relay.Function([], output)
mutated_mod['func_18178'] = func_18178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18037_call = mod.get_global_var('func_18037')
func_18039_call = mutated_mod.get_global_var('func_18039')
call_18363 = relay.TupleGetItem(func_18037_call(), 0)
call_18364 = relay.TupleGetItem(func_18039_call(), 0)
func_11659_call = mod.get_global_var('func_11659')
func_11663_call = mutated_mod.get_global_var('func_11663')
const_18372 = relay.const([-6.904413,-6.355793,8.102001,3.033933,-0.360838,-6.650457,-0.385426,3.113004,-2.119535,5.221098,5.664684,9.734772,-2.082257,-5.997021,2.223997,8.412836,-2.792664,0.016457,5.005130,4.770675,-5.402171,-4.089170,2.619021,-7.102169,8.084761,1.746441,-4.119443,-3.545504,4.064001,-9.285067,-5.202436,-8.753267,3.020789,-5.679846,-0.413753,5.052089,7.973820,4.426074,3.389784,-3.562369,-5.574202,1.465854,4.493890,6.438023,-5.197264,3.268404,2.149986,2.421242,3.505049,0.621061,0.910021,-4.972164,8.563300,7.591466,5.286800,7.171184,-9.241226,-0.634547,-0.042993,-0.084244,0.551028,5.356218,5.930478,-8.506788,-8.827194,-2.377441,-0.993090,-9.279097,4.074026,-8.032503,-7.627722,-2.155645,-8.367416,-5.978601,-6.734055,-0.248700,-7.560289,9.794394,-4.334767,-1.627162,0.278689,5.203458,7.180960,9.382342,6.954971,-8.190219,0.476497,-1.844896,4.632862,-0.916963,0.537827,-1.381776,-2.204457,0.817987,9.719965,8.445167,3.860078,-8.138437,1.421703,7.709785,6.550490,-6.568291,-7.535339,-2.495657,6.173034,9.652752,8.444458,-3.981524,3.412503,1.211934,1.473362,-6.072087,3.943002,6.100224,-0.814711,7.851843,-9.082614,7.195023,2.501240,8.089443,-4.009767,8.980611,-8.883950,-9.005027,-4.222973,-1.515146,-1.203254,-0.741386,4.702450,-0.275517,-2.024696,1.425926,7.463829,3.131492,-2.489337,1.537117,0.577799,2.112884,-8.756380,-8.225986,1.315925,-5.896907,8.788122,3.312382,3.988009,-1.178661,9.550911,-6.361209,-2.459616,6.185868,-0.478602,-9.762224,-4.978039,8.310932,2.428753,3.650535,-2.683958,-6.484131,-8.968532,-3.585496,-6.504781,2.489273,-4.358593,-1.394331,5.863143,-5.844660,8.860887,0.399782,-9.204951,-0.587375,-9.657786,-5.344035,-6.047590,-5.173840,-1.149750,-4.469823,-1.277020,-4.091357,0.191936,0.791079,8.701387,4.833952,-0.554038,-8.816592,9.716805,-5.640742,-3.551230,8.042961,-8.818994], dtype = "float32")#candidate|18372|(189,)|const|float32
const_18373 = relay.const([0.622684,2.140240,-8.754887,-5.213024,0.889622,9.876650,-6.712085,5.810014,-0.810400,-1.348293,0.420781,9.585173,4.715539,-6.562200,-6.807198,-1.086361,1.071152,6.804835,-4.970878,-8.227853,7.105840,-3.944886,7.201653,-7.433325,5.828386,8.243235,5.067862,9.376499,-3.812336,0.756890,-8.191220,-2.365080,1.334622,4.480676,5.768079,5.634297,9.854885,8.384527,-3.338274,-5.237714,-4.767336,-6.251092,-6.534046,-1.499740,3.765600,6.698215,7.860476,-3.897659,-3.194037,-2.516206,6.899438,-5.447620,-0.637742,5.341373,-4.279661,-9.948640,8.873353,-0.615947,-3.381193,-1.296420,1.210859,5.272570,7.003601,0.503051,-0.305120,-6.038453,-2.777374,-0.446695,-1.932399,4.757197,-6.641086,4.663636,-5.512586,3.280209,-1.424318,-2.528085,-4.399714,-0.956562,7.836469,3.501162,9.279228,2.549413,-3.586068,-9.255015,-1.244665,5.332377,8.932224,-4.625655,0.980435,-8.703707,-4.585585,6.065406,1.963389,-6.975561,8.346819,-4.748573,6.386307,-6.949091,0.266956,-9.314839,-8.125701,-1.924169,-7.625784,8.771569,0.456489,4.871027,3.368504,-9.949816,-7.928546,8.792734,-2.189795,4.958936,-7.585628,1.391489,-9.040700,1.180061,-2.928684,0.538412,-3.700291,-7.399371,-8.454291,4.902127,-7.894711,-0.412361,0.669451,-9.982547,4.065763,8.868335,-1.956773,-0.243027,2.886861,8.772057,9.115025,-5.722950,-9.762401,5.783265,2.121666,-6.348835,-4.768268,-6.149810,-6.758094,9.870443,-1.982306,9.073842,-5.612811,-5.491404,8.484554,5.637423,-5.563878,9.709531,-5.843073,6.854077,4.431675,1.094043,3.801765,4.539674,-9.290348,8.591974,-9.940947,4.119257,-8.194681,-6.167723,-8.418478,6.929056,4.674233,5.815779,3.597778,2.451921,-4.662637,9.054475,5.846900,1.778578,7.720590,-8.704072,-7.393558,-4.639068,2.811903,-6.518867,-9.835662,-9.975156,-4.075042,0.924110,3.515650,2.614472,3.753547,2.417476,4.620320,5.862570,4.553508,-8.910770,1.891247,9.544561,7.509047,-9.237824,7.083189,-3.760127,-3.455999,5.129828,-5.043244,8.400806,3.489244,-2.420505,-5.994951,-5.164958,-3.625247,5.264237,7.177088,-9.403276,-2.482933,2.744849,-9.043076,-8.006439,9.665563,-9.992847,-6.180973,-8.034273,-0.522667,-7.951635,-7.511921,-4.509802,-4.628957,-1.597397,-3.583670,-6.325809,-7.155270,-9.364409,8.747119,8.866645,1.115724,3.574335,-2.549910,6.758056,-6.147354,2.927654,-2.137777,8.768850,6.638619,8.093101,9.268116,-4.689672,6.790962,-9.080609,2.429251,1.888507,0.634615,-2.072291,-0.173052,-1.536545,-2.191321,6.026807,2.032382,4.701733,2.268455,4.254454,-3.091760,-1.681280,-3.895484,7.412856,-5.715025,-9.167018,6.252974,3.850411,5.221646,-2.213692,7.033315,-8.579772,4.875439,4.647778,-6.732881,5.928821,3.162920,-9.015951,-7.443205,7.493852,7.121943,-9.013606,3.508692,-0.708810,1.664511,-0.806879,5.024287,8.691456,-2.595507,1.375637,7.506875,2.293337,-5.459940,1.518847,1.079410,3.132504,-8.547256,5.001429,-5.935610,-7.745025,9.837616,-8.659466,-4.612640,2.755092,5.469155,4.496798,0.558939,9.535612,5.400058,-1.893468,9.184916,8.885928,6.604479,3.544230,-4.373114,3.926104,-8.250654,-3.536690,0.987690,4.442881,-6.160469,-2.349017,-0.634007,1.798600,-9.997811,-7.746004,-0.665958,6.031558,0.416526,7.444761,1.577501,2.947266,-2.905748,-8.827575,4.238986,-2.018103,-3.709587,0.376369,-4.441294,-4.870205,-1.744004,3.731101,-8.339765,-5.039208,2.778920,-1.891337,-3.120252,8.923905,6.529551,-8.117557,5.927704,5.714494,2.951273,-2.923811,7.229035,-6.284593,-9.002266,-8.789742,5.104893,-5.545790,-4.885297,6.698332,-8.753020,-9.496446,-0.383986,-5.945004,5.642901,7.653998,-8.444283,2.761022,8.518145,2.337796,1.180609,-4.238319,-8.899969,2.419567,1.512031,2.360332,8.276174,-9.233962,-5.832209,-7.757247,-3.670509,8.557739,5.479128,-7.663328,-2.950192,-0.120920,-4.191829,-2.748162,5.285147,5.789580,-5.568854,-5.873792,-0.986074,2.079249,6.238743,3.403504,-1.283709,-9.705597,0.089482,-0.282091,-8.895868,1.418414,3.041346,5.362087,5.320813,-4.130795,4.688612,-3.584920,9.675428,6.503438,0.803982,-3.961747,6.490094,5.160025,6.095015,-4.818484,8.430860,-7.524801,-9.702823,0.958163,2.278598,2.391817,7.751697,-4.007250,-0.883202,3.993491,-1.918589,1.007075,5.404323,-6.405558,-0.619787,-0.313442,-6.600927,-4.918456,8.515715,6.126749,2.031513,8.989573,-6.878034,4.488793,7.173704,-3.766736,-2.465068,7.276564,-8.659970,2.662771,7.075154,-3.738693,-6.230122,-3.724298,1.817670,-7.028648,-5.549974,4.425590,-7.199572,0.622687,9.323177,1.588505,0.716575,8.952568,0.124867,-0.211294,7.602624,-3.481390,-3.880923,0.812413,-4.887906,-4.343354,8.855335,8.900160,7.159160,-1.752971,-1.136643,-5.063214,-0.276291,-7.633734,-2.149209,-0.380347,1.340229,-7.978956,6.892321,7.718393,3.900430,0.054099,5.663505,-7.091099,2.788768,-9.569598,3.229818,-4.953183,-5.936930,4.042113,4.751342,-1.281578,-9.086270,-1.838804,-3.495214,-1.940466,-9.106187,8.082354,-5.412913,-2.404111,-3.803618,-1.016563,4.203559,9.941586,5.062245,3.211049,6.657541,1.254788,-7.744462,0.748675,-1.808348,-8.587634,8.763546,-6.602011,-6.846652,-7.206173,8.073162,-8.733204,4.838240,1.348007,-4.359747,7.501387,-6.170294,1.316016,0.473927,-4.928204,-5.713567,-8.130380,-2.018793,-4.811824,0.189380,3.779803,6.267000,2.491684,1.174360,3.998708,7.664950,7.745072,6.101047,-3.632707,-8.775948,-9.008545,-1.596847,-4.407706,-0.048220,9.582551,9.612640,-5.696415,-3.472330,0.704233,-3.279026,2.089965,-8.219637,-1.210849,7.879289,-0.757688,9.892381,6.430739,5.462531,-8.086431,-5.270217,2.293942,-0.734054,-5.433955,4.730078,-9.514172,-1.067622,-0.668592,9.153606,-5.923141,5.661586,-8.081710,-8.452203,-8.421272,0.492393,0.828925,-0.879048,-8.805432,-6.807520,6.179728,-3.312747,-7.906059,7.857641,2.871693,9.343928,-8.785636,-5.547514,5.082271,-6.123593,-2.283523,-7.655964,4.302609,-3.689113,6.915007,-4.685821,2.095340,-5.127219,4.144601,-3.968630,-4.201344,-9.429708,-8.911885,1.382376,4.050219,-9.979217,-8.243642,7.009744,9.049475,1.295633,2.906114,-7.000259,-4.437180,-6.258049,-2.861175,9.627277,-8.158116,9.056043,-9.288673,-6.366456,-5.064755,-3.987183,5.186676,-3.824387,4.235956,7.695292,8.746192,0.336147,-4.444845,2.021427,-0.163081,-0.686142,0.543172,-0.666270,-6.885985,4.801651,5.794873,3.424107,-0.198302,7.082027,8.611666,-4.518241,-1.846879,9.888313,8.781954,-8.289134,1.038376,-2.710128,-2.552674,-6.357659,3.590167,-6.765119,1.829635,0.128391,1.101080,-2.498719,0.175672,-7.878101,-2.700565,-3.233917,-0.454917,-2.944761,7.116928,-4.333610,4.256907,0.739909,0.647723,5.194204,8.804844,-0.177671,3.479046,-1.641104,9.374170,7.777049,-6.726066,3.861491,-0.872817,-8.430354,-0.756185,2.310424,5.948017,-8.372153,-0.674319,-6.825373,-9.716597,5.032786,4.104548,-8.442729,-6.557566,-9.032985,2.686031,8.812620,5.767887,-5.817202,4.226506,6.862844,-1.562998,7.670783,6.584328,-7.517426,-9.848971,-9.958510,2.189574,-3.264296,-7.282349,-1.195653,-6.369519,4.750513,8.725373,6.359767,7.863827,-2.953925,-6.980129,9.032930,6.435824,0.862584,9.106276,2.426518,-5.042939,-6.496533,-2.505197,-5.662268,-9.297208,9.277276,2.076367,-4.083080,1.250838,-3.670983,-5.647067,-4.023714,-3.352790,7.482343,8.097203,-2.670838,-7.998426,-1.780496,-4.362904,7.566845,-2.710107,-7.274304,5.298933,-9.601981,6.241132,-8.852792,-1.284098,2.370988,-1.312973,-8.393409,5.760988,9.313241,1.368416,3.850076,7.581003,1.391144,3.171134,6.167734,-0.398024,8.689742,8.660898,-5.814108,-0.039167,-7.439315,-4.012165,-8.416372,4.593569,-7.217569,1.836548,-5.732686,-8.020597,-8.593725,-7.642777,5.900930,-1.435955,-3.969060,-3.625689,1.524609,7.321270,-1.631878,5.258048,2.496517,-1.719936,2.796627,2.963657,-2.907157,5.553534,3.468055,1.186907,8.692524,-8.703640,7.215187,-0.699274,0.222066,-6.662640,6.217188,6.886638,-9.396014,-0.846401,6.259262,-8.820027,-5.258177,3.389271,9.938117,-3.151453,-0.844009,-1.751957,9.399185,-2.053221,-0.534028,-4.817326,-0.285841,8.323292,-8.444086,2.670149,4.484359,3.133966,0.130106,-4.708391,2.249352,7.653263,4.236358,1.963161,-3.052431,2.189265,-4.039281,6.943575,5.272344,-1.642856,-5.689272,-7.598204,2.932007,4.469654,-8.461296,1.778695,-4.703556,5.082633], dtype = "float64")#candidate|18373|(832,)|const|float64
call_18371 = relay.TupleGetItem(func_11659_call(relay.reshape(const_18372.astype('float32'), [189,]), relay.reshape(const_18373.astype('float64'), [832, 1]), ), 1)
call_18374 = relay.TupleGetItem(func_11663_call(relay.reshape(const_18372.astype('float32'), [189,]), relay.reshape(const_18373.astype('float64'), [832, 1]), ), 1)
output = relay.Tuple([call_18363,call_18371,const_18372,const_18373,])
output2 = relay.Tuple([call_18364,call_18374,const_18372,const_18373,])
func_18391 = relay.Function([], output)
mod['func_18391'] = func_18391
mod = relay.transform.InferType()(mod)
output = func_18391()
func_18392 = relay.Function([], output)
mutated_mod['func_18392'] = func_18392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14996_call = mod.get_global_var('func_14996')
func_14998_call = mutated_mod.get_global_var('func_14998')
call_18408 = func_14996_call()
call_18409 = func_14996_call()
output = relay.Tuple([call_18408,])
output2 = relay.Tuple([call_18409,])
func_18428 = relay.Function([], output)
mod['func_18428'] = func_18428
mod = relay.transform.InferType()(mod)
mutated_mod['func_18428'] = func_18428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18428_call = mutated_mod.get_global_var('func_18428')
call_18429 = func_18428_call()
output = call_18429
func_18430 = relay.Function([], output)
mutated_mod['func_18430'] = func_18430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13697_call = mod.get_global_var('func_13697')
func_13699_call = mutated_mod.get_global_var('func_13699')
call_18502 = relay.TupleGetItem(func_13697_call(), 0)
call_18503 = relay.TupleGetItem(func_13699_call(), 0)
output = relay.Tuple([call_18502,])
output2 = relay.Tuple([call_18503,])
func_18510 = relay.Function([], output)
mod['func_18510'] = func_18510
mod = relay.transform.InferType()(mod)
mutated_mod['func_18510'] = func_18510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18510_call = mutated_mod.get_global_var('func_18510')
call_18511 = func_18510_call()
output = call_18511
func_18512 = relay.Function([], output)
mutated_mod['func_18512'] = func_18512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17173_call = mod.get_global_var('func_17173')
func_17174_call = mutated_mod.get_global_var('func_17174')
call_18518 = relay.TupleGetItem(func_17173_call(), 1)
call_18519 = relay.TupleGetItem(func_17174_call(), 1)
output = call_18518
output2 = call_18519
func_18541 = relay.Function([], output)
mod['func_18541'] = func_18541
mod = relay.transform.InferType()(mod)
mutated_mod['func_18541'] = func_18541
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18541_call = mutated_mod.get_global_var('func_18541')
call_18542 = func_18541_call()
output = call_18542
func_18543 = relay.Function([], output)
mutated_mod['func_18543'] = func_18543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17788_call = mod.get_global_var('func_17788')
func_17789_call = mutated_mod.get_global_var('func_17789')
call_18555 = relay.TupleGetItem(func_17788_call(), 0)
call_18556 = relay.TupleGetItem(func_17789_call(), 0)
output = call_18555
output2 = call_18556
func_18580 = relay.Function([], output)
mod['func_18580'] = func_18580
mod = relay.transform.InferType()(mod)
mutated_mod['func_18580'] = func_18580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18580_call = mutated_mod.get_global_var('func_18580')
call_18581 = func_18580_call()
output = call_18581
func_18582 = relay.Function([], output)
mutated_mod['func_18582'] = func_18582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18580_call = mod.get_global_var('func_18580')
func_18582_call = mutated_mod.get_global_var('func_18582')
call_18589 = func_18580_call()
call_18590 = func_18580_call()
func_10179_call = mod.get_global_var('func_10179')
func_10182_call = mutated_mod.get_global_var('func_10182')
const_18595 = relay.const([-3,2,7,-6,-5,9,6,-8,-5,10,8,6,-9,1,-4,-9,-3,-8,-2,-3,9,1,-5,-4,1,-10,10,-9,3,-4,-4,5,1,-8,-10,-1,6,2,-2,-2,10,2,-10,-8,10,-1,2,-2,9,-9,-4,8,4,-9,-6,-1,-5,-4,-1,1,4,-6,7,-3,-7,-9,-3,-8,7,-5,-10,-7,9,-3,6,2,3,-8,5,1,4,-2,5,5,-1,4,7,8,5,-8,5,-2,-9,1,4,5,-1,4,-1,9,1,5,7,6,7,4,4,-10,-8,7,4,9,-1,3,-4,-3,-6,-5,-4,-6,4,2,-7,1,3,9,-9,3,3,-3,-8,4,-7,-8,1,-1,-3,-3,3,-6,-3,4,-3,-4,-2,-5,-5,6,-7,2,-6,3,8,-10,1,9,-10,7,-9,10,-8,-4,4,-5,-2,-9,2,10,9,10,5,-3,2,8,1,-5,-3,-9,6,-5,1,-9,-7,10,8,-5,9,7,8,-3,3,7,6,10,2,-2,-1,-5,-1,-2,6,3,-5,-7,6,-3,9,-5,-8,8,-10,2,-3,-10,1,-5,-9,-2,-1,-9,-8,-7,4,3,5,-3,-2,-8,1,1,-10,-9,-7,5,-10,8,-9,-5,7,9,9,-8,-7,6,-4,10,-3,3,9,-9,-4,-5,2,-10,-9,-10,10,-9,-6,-5,-2,-4,-1,9,7,-9,7,-6,5,7,-4,2,6,-1,6,3,-10,-5,6,-2,-3,5,-4,-8,-6,3,-1,4,-4,-10,-2,8,-1,-2,8,9,-5,-9,3,10,-2,9,-7,1,-9,-4,5,10,7,-3,10,-6,4,5,-3,-9,7,-8,-3,10,1,3,-7,4,-9,-1,-6,-3,2,-2,-3,10,10,-8,7,7,1,-6,4,-6,-6,9,4,4,10,-1,-8,-4,-10,-5,10,7,-1,4,4,10,7,-1,3,-6,-5,7,9,4,-4,6,-1,7,-5,-9,1,8,9,6,9,5,1,7,-5,-1,8,-5,10,2,3,6,-1,9,-6,-1,8,-6,10,-3,4,4,-1,2,-10,-9,-6,-6,-9,-8,-3,9,7,-2,-1,-3,-9,9,-5,1,7,-10,-7,9,-5,-3,8,-2,9,3,9,7,5,7,-8,7,10,-8,8,-5,6,3,-1,-8,-9,2,-9,5,2,-5,-10,-6,2,9,1,2,3,-1,10,-5,-4,-6,-4,6,3,-8,4,5,-8,-5,-8,8,4,-6,-1,-1,9,-8,8,-1,-7,-8,-5,-6,-9,1,10,1,-9,8,9,4,7,-1,8,-8,2,-6,10,9,-5,-9,10,-8,-6,-8,6,-4,-4,7,-8,-6,2,-9,-4,-4,-1,-1,-10,9,-5,-2,8,3,-1,-5,9,1,-3,-6,1,3,10,2,-5,9,-9,-3,6,-1,8,10,-7,-9,-3,5,-2,7,-4,-5,1,1,4,7,1,9,-3,-7,9,-9,8,8,4,-5,4,9,3,-7,5,-6,-1,-6,-3,-5,6,7,-1,7,10,-4,-3,4,-3,2,3,4,3,2,-2,10,-2,3,4,9,-5,10,3,1,-3,4,1,3,8,1,2,-8,-10,10,-5,8,9,6,-2,-8,2,-2,-9,-10,-10,-5,-4,-9,-5,10,5,10,6,7,-6,4,8,2,10,-2,-3,-3,1,-3,10,-8,3,-10,-5,8,4,9,7,9,3,10,-10,5,6,2,3,-10,2,-5,6,8,3,-10,-3,10,2,-4,-2,6,8,3,-9,-6,-2,8,4,6,7,10,6,-8,9,-1,-2,10,-6,-1,-5,-6,10,4,1,-1,-5,8,2,-10,-7,-1,-9,-9,5,9,-7,-8,-8,10,2,10,6,-1,-6,-9,-3,4,-3,-6,-2,-10,-10,7,1,-9,-3,-2,-9,-7,-5,9,-7,9,-5,10,-8,8,1,5,-5,6,-3,6,1,-8,10,-4,10,6,-6,3,-9,3,-8,-3,-3,2,-7,-2,4,7,-7,10,2,-3,4,-6,8,-10,-8,-9,2,-8,2,9,10,-9,-7,-6,-4,-9,6,-1,3,-3,6,3,-5,-9,1,-2,-6,-1,9,1,-6,-4,-4,-9,6,-9,5,-2,-2,-7,1,-5,-10,7,4,5,-8,4,-3,2,-6,4,2,-2,-7,1,-8,-4,-5,-10,-8,-8,-3,2,-9,5,-5,7,-5,6,-7,9,-3,6,3,-4,-10,-9,9,8,6,-3,2,-10,10,8,-1,5,-9,10,4,5,10,-6,5,-7,7,2,2,8,-6,-1,5,-10,4,8,-8,3,-5,7,5,3,-5,-1,6,9,8,-10,-6,9,4,10,-8,-10,-4,-7,10,-10,4,2,-1,-4,2,3,-6,-8,10,2,2,3,8,4,-9,-3,-6,-2,9,-7,10,9,-2,8,-6,2,-2,-6,6,-8,-2,9,-9,4,-9,-7,1,-6,-6,9,-5,-1,-5,-7,5,-7,10,7,-8,-5,2,-5,9,-9,8,-8,6,-1,-4,-5,6,8,-7,3,-5,-2,2,1,-1,-8,-8,-3,6,7,-2,1,-4,4,-5,9,-7,7,8,-1,-10,-9,7,-3,8,3,4,-10,4,-2,-2,6,-1,7,5,-10,8,3,3,-8,-8,1,-6,2,4,6,-6,5,9,9,-1,7,8,7,-8,4,-6,9,7,-2,7,9,2,3,6,-5,8,-8,-4,2,2,5,5,9,-7,-5,1,-8,-5,-6,10,10,3,-8,5,-6,-8,-4,-7,4,-6,-8,2,1,8,10,9,8,10,-9,-8,1,-10,-10,9,-2,-5,-3,-8,-6,-2,-6,8,2,-2,2,-10,9,-7,-10,4,-1,-4,-6,9,-1,-10,-1,-3,-6,-8,6,-1,-9,-5,-7,2,-8,4,-1,5,3,10,-4], dtype = "uint16")#candidate|18595|(1092,)|const|uint16
call_18594 = relay.TupleGetItem(func_10179_call(relay.reshape(const_18595.astype('uint16'), [6, 13, 14])), 0)
call_18596 = relay.TupleGetItem(func_10182_call(relay.reshape(const_18595.astype('uint16'), [6, 13, 14])), 0)
output = relay.Tuple([call_18589,call_18594,const_18595,])
output2 = relay.Tuple([call_18590,call_18596,const_18595,])
func_18601 = relay.Function([], output)
mod['func_18601'] = func_18601
mod = relay.transform.InferType()(mod)
output = func_18601()
func_18602 = relay.Function([], output)
mutated_mod['func_18602'] = func_18602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14375_call = mod.get_global_var('func_14375')
func_14376_call = mutated_mod.get_global_var('func_14376')
call_18609 = relay.TupleGetItem(func_14375_call(), 0)
call_18610 = relay.TupleGetItem(func_14376_call(), 0)
func_14375_call = mod.get_global_var('func_14375')
func_14376_call = mutated_mod.get_global_var('func_14376')
call_18637 = relay.TupleGetItem(func_14375_call(), 0)
call_18638 = relay.TupleGetItem(func_14376_call(), 0)
func_14996_call = mod.get_global_var('func_14996')
func_14998_call = mutated_mod.get_global_var('func_14998')
call_18657 = func_14996_call()
call_18658 = func_14996_call()
output = relay.Tuple([call_18609,call_18637,call_18657,])
output2 = relay.Tuple([call_18610,call_18638,call_18658,])
func_18659 = relay.Function([], output)
mod['func_18659'] = func_18659
mod = relay.transform.InferType()(mod)
output = func_18659()
func_18660 = relay.Function([], output)
mutated_mod['func_18660'] = func_18660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11742_call = mod.get_global_var('func_11742')
func_11744_call = mutated_mod.get_global_var('func_11744')
call_18704 = func_11742_call()
call_18705 = func_11742_call()
output = call_18704
output2 = call_18705
func_18723 = relay.Function([], output)
mod['func_18723'] = func_18723
mod = relay.transform.InferType()(mod)
output = func_18723()
func_18724 = relay.Function([], output)
mutated_mod['func_18724'] = func_18724
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11833_call = mod.get_global_var('func_11833')
func_11835_call = mutated_mod.get_global_var('func_11835')
call_18733 = relay.TupleGetItem(func_11833_call(), 0)
call_18734 = relay.TupleGetItem(func_11835_call(), 0)
output = call_18733
output2 = call_18734
func_18736 = relay.Function([], output)
mod['func_18736'] = func_18736
mod = relay.transform.InferType()(mod)
mutated_mod['func_18736'] = func_18736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18736_call = mutated_mod.get_global_var('func_18736')
call_18737 = func_18736_call()
output = call_18737
func_18738 = relay.Function([], output)
mutated_mod['func_18738'] = func_18738
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18019_call = mod.get_global_var('func_18019')
func_18020_call = mutated_mod.get_global_var('func_18020')
call_18757 = func_18019_call()
call_18758 = func_18019_call()
func_18119_call = mod.get_global_var('func_18119')
func_18121_call = mutated_mod.get_global_var('func_18121')
const_18805 = relay.const([[-5.003862,-8.404062,4.355399,4.240811,4.489132,-4.462556,-4.420851,-7.545467,5.132318,-1.725515,1.361690,-4.417216,-2.813487,7.392759,1.187969,-5.537829,1.903054,5.675069,6.215935,3.245958,3.458162,5.216524,-3.949258,-9.721974,-9.441083,8.586204,5.864456,-7.322999,1.674670,-6.851850,-1.452892,-7.253076,4.464325,-1.707130,-9.308861,-9.635003,5.812733,6.279449,4.904728,8.919891,-5.421009,0.928684,7.670754,-7.700135,-7.052712,6.930752,0.416219,-5.489390,-1.937247,9.021170,6.417722,-9.623248,9.798827,-5.973591,2.777981,0.317544,-5.229378,8.008213,-2.231970,4.694755,8.256280,0.797091,-6.257886,1.631516,-4.479054,-7.460414,-0.443292,9.313750,-5.455999,3.156500,7.899859,-1.754244,1.657116,2.195864,0.777170,-4.770780,-4.008534,3.279238,-2.272685,9.847028,4.071787,-8.027831,-5.030907,5.141507,6.725707,-9.767922,8.688496,-6.763227,2.576955,-8.631212,-1.021911,3.651267,-7.572848,-6.231152,8.038489,-7.703574,7.666066,5.544509,-9.254975,-1.904126,8.739891,-9.938135,7.471574,6.987709,6.181197,7.055211,3.881170,-4.898009,4.163693,-0.411209,-8.694162,1.223202,2.753164,1.388564,-4.238907,2.875060,-6.488746,-7.745075,-2.061710,-4.466069,-8.270386,-4.770941,-6.306501,7.033186,4.811673,0.497637,-9.563180,0.985426,0.380143,0.028185,-1.182567,3.049534,7.060704,0.027831,3.507896,1.706729,9.868085,3.732289,-8.046300,-6.979125,-8.964297,4.995152,-3.062811,-3.784228,8.979998,9.249719,-3.277973,-4.996276,6.661140,-3.783966,-8.120806,-0.384081,7.914474,2.138763,-6.351160,8.635977,1.811332,-2.949636,9.050628,9.010732,-0.930324,-9.220558,1.564361,-8.311560,-8.166713,-2.247099,-9.385274,8.961746,-0.621942,1.202816,-5.992989,-8.726479,9.397283,1.109171,9.062573,1.243308,-9.895000,9.665383,5.853128,-3.004688,-0.251375,-3.454986]], dtype = "float64")#candidate|18805|(1, 182)|const|float64
call_18804 = relay.TupleGetItem(func_18119_call(relay.reshape(const_18805.astype('float64'), [182,])), 2)
call_18806 = relay.TupleGetItem(func_18121_call(relay.reshape(const_18805.astype('float64'), [182,])), 2)
func_14196_call = mod.get_global_var('func_14196')
func_14198_call = mutated_mod.get_global_var('func_14198')
const_18814 = relay.const([9.628064,-1.789899,-7.407158,-2.757255,-0.686624,-3.618501,7.879544,-2.291656,-2.544577,-3.641544,-2.646525,-6.854094,-8.635356,4.987190,-6.214691,-8.065141,9.315952,1.466692,-8.489912,9.415946,-0.096447,8.834685,1.920529,-7.213422,6.804096,-0.998620,6.907758,2.168567,9.223791,2.074971,6.073197,4.578028,1.903662,-4.102951,-3.988444,-4.169328,9.187012,-0.070538,6.361329,1.927336,1.018345,-2.155780,-1.934643,8.918625,1.764352,1.183535,-8.474550,6.544258,8.960326,-4.955647,3.191813,2.742310,-7.834086,-4.158891,-8.805443,-0.683119,1.577112,-5.224387,1.798140,-9.064992,1.440118,0.401521,-7.570129,7.237280,-7.278202,-9.115831,-7.053329,4.685293,8.907307,-4.587468,0.957085,-3.930864,3.009628,-4.186765,-7.831084,8.950150,3.173047,9.435811,-3.517456,9.188055,-2.741525,-1.701336,8.033546,-7.572205,9.709375,3.895032,6.429565,-0.708058,-3.825535,7.657868,6.650052,-1.889808,1.894716,-4.682648,-0.871427,2.563280,7.638592,9.124374,4.375923,-7.605281,-4.197140,3.636711,0.151580,7.301106,-7.385422,-5.795325,6.722339,-3.214991,-6.424151,-4.256134,3.292859,-6.822430,-7.878591,8.754879,0.531359,-6.075359,8.802046,3.917680,1.509610,7.712505,-5.208614,4.927938,-5.429949,-0.460983,6.674058,-3.568011,-9.759326,2.065439,-2.120285,-3.534754,-1.777588,-3.660250,-9.409609,-8.224223,-0.571152,-3.031206,7.504904,-1.986443,6.161024,3.442944,-7.289962,5.641040,-6.384495,3.924695,-4.900135,-9.509361,-0.939141,-2.101639,-7.484044,9.105247,-3.677084,8.404924,8.908492,-5.353345,5.419445,8.129467,5.921640,-3.251341,-0.714352,-7.734567,-4.431727,6.511392,7.868923,6.247391,5.312307,-3.054849,-5.831087,3.559326,-6.644038,5.963677,0.011803,4.937089,8.822275,-8.274173,3.816079,-7.970588,9.193932,-9.975052,-1.019821,0.011087,-0.012337,2.347495,2.551667,8.327787,-0.189367,5.176612,0.152641,-6.394740,4.068432,-9.245509,-7.091555,-0.169551,7.661943,-0.897939,-9.760708,7.654848,-6.316375,-4.368958,4.762919,3.223638,-7.619573,-8.128502,2.693221,-6.087384,1.402696,1.736349,-4.275787,-8.623072,-4.078504,0.771288,-6.727405,-8.424703,7.953356,-8.511475,-4.889571,5.291685,7.690978,-7.641577,-3.059722,0.775683,-5.642714,5.516713,-0.840991,-4.762646,9.532859,6.301408,-2.355354,-1.709639,-1.223106,-6.366313,-9.545994,4.255252,4.502081,-7.383712,7.424459,-7.616121,-6.197474,-6.077818,1.247671,0.284015,-0.023192,-8.931050,-4.376378,-3.423063,6.610462,1.979268,-2.706735,3.635709,5.577426,-4.892978,2.370634,-4.009893,-5.311208,-2.935383,7.065368,-8.600717,1.423210,-8.154307,5.391430,-4.901652,7.452365,-5.250082,7.581507,-7.400908,0.757023,9.115278,5.627157,-6.195545,-3.314311,0.368319,5.408767,8.014201,-3.156605,-6.745472,-8.758281,-0.438224,7.484336,-5.017923,1.848118,4.436736,6.793712,1.738464,-8.331187,-4.425671,0.195066,-5.846653,-0.711078,0.224118,7.894535,-5.870847,-1.575562,2.882280,-0.907550,-2.609240,-7.554560,-2.807681,-7.531881,-0.524978,-9.015727,1.819767,-8.984172,-3.106154,9.025768,8.226395,5.641297,7.232918,2.603606,9.103661,-2.854294,3.252940,6.089012,-2.300948,5.739681,-8.658959,6.725408,3.538599,1.409168,-5.077738,0.309463,8.238685,-6.203439,8.344352,-7.386418,8.016118,-7.040587,7.528005,-4.498086,-0.782520,3.899562,4.666504,-5.726508,-0.427525,-3.721850,0.080029,3.594488,1.226729,9.181595,4.203018,4.856402,-7.530006,8.436506,-9.667073,6.125250,4.103576,7.336354,6.565172,-8.222020,-5.366972,6.217088,-8.042495,-4.916923,-3.948120,-3.893401,8.668917,-3.278286,-6.243478,-0.957731,4.167538,1.305739,-7.176174,-2.373870,-7.339467,4.334063,5.370072,-7.277938,1.808458,7.866993,-6.966829,2.063595,-7.517209,3.060496,4.809165,0.609921,8.342451,-4.188335,7.024409,-7.543976,1.160062,-2.930802,-4.413416,-2.160364,-1.583714,7.786530,-8.428853,-7.502951,-2.628482,2.253365,4.871407,-7.007275,2.500248,-9.778439,2.838252,-3.380121,8.375246,-6.772750,-7.259179,8.473601,-9.021311,1.394267,-5.375062,8.063199,-7.983881,-8.890379,0.860971,-1.195844,9.512580,-5.629641,5.702745,6.903896,3.816589,-7.733364,6.129970,-9.111241,-0.915321,-7.357773,-3.024305,5.403811,-2.060119,-6.141427,6.404235,-6.199605,-6.015388,6.180884,3.115401,-8.304218,-6.056236,-2.868186,-4.770456,-0.270909,3.946344,7.492009,-7.853556,-6.726761,4.944627,4.119332,5.459940,7.187188,-5.836125,-5.130026,-5.428373,-2.015205,0.048611,-7.803564,-4.292807,3.416281,7.809438,5.406500,1.297849,-1.627468,-6.933989,5.959645,8.261520,5.684687,-5.960718,9.180891,-6.133958,5.544268,3.877968,-4.699577,-4.331011,7.747095,-1.397654,-9.672731,-0.707773,-2.818986,-6.910254,-2.314512,4.454225,9.078385,0.437297,-6.472104,-4.782558,-2.565171,7.612722,6.330308,-3.147770,5.893752,9.422847,-3.649244,-5.486622], dtype = "float64")#candidate|18814|(480,)|const|float64
call_18813 = relay.TupleGetItem(func_14196_call(relay.reshape(const_18814.astype('float64'), [480,])), 1)
call_18815 = relay.TupleGetItem(func_14198_call(relay.reshape(const_18814.astype('float64'), [480,])), 1)
output = relay.Tuple([call_18757,call_18804,const_18805,call_18813,const_18814,])
output2 = relay.Tuple([call_18758,call_18806,const_18805,call_18815,const_18814,])
func_18827 = relay.Function([], output)
mod['func_18827'] = func_18827
mod = relay.transform.InferType()(mod)
mutated_mod['func_18827'] = func_18827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18827_call = mutated_mod.get_global_var('func_18827')
call_18828 = func_18827_call()
output = call_18828
func_18829 = relay.Function([], output)
mutated_mod['func_18829'] = func_18829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17982_call = mod.get_global_var('func_17982')
func_17983_call = mutated_mod.get_global_var('func_17983')
call_18882 = func_17982_call()
call_18883 = func_17982_call()
output = relay.Tuple([call_18882,])
output2 = relay.Tuple([call_18883,])
func_18887 = relay.Function([], output)
mod['func_18887'] = func_18887
mod = relay.transform.InferType()(mod)
mutated_mod['func_18887'] = func_18887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18887_call = mutated_mod.get_global_var('func_18887')
call_18888 = func_18887_call()
output = call_18888
func_18889 = relay.Function([], output)
mutated_mod['func_18889'] = func_18889
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11095_call = mod.get_global_var('func_11095')
func_11096_call = mutated_mod.get_global_var('func_11096')
call_18922 = func_11095_call()
call_18923 = func_11095_call()
func_15046_call = mod.get_global_var('func_15046')
func_15047_call = mutated_mod.get_global_var('func_15047')
call_18943 = relay.TupleGetItem(func_15046_call(), 0)
call_18944 = relay.TupleGetItem(func_15047_call(), 0)
output = relay.Tuple([call_18922,call_18943,])
output2 = relay.Tuple([call_18923,call_18944,])
func_18951 = relay.Function([], output)
mod['func_18951'] = func_18951
mod = relay.transform.InferType()(mod)
mutated_mod['func_18951'] = func_18951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18951_call = mutated_mod.get_global_var('func_18951')
call_18952 = func_18951_call()
output = call_18952
func_18953 = relay.Function([], output)
mutated_mod['func_18953'] = func_18953
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15721_call = mod.get_global_var('func_15721')
func_15722_call = mutated_mod.get_global_var('func_15722')
call_19060 = relay.TupleGetItem(func_15721_call(), 1)
call_19061 = relay.TupleGetItem(func_15722_call(), 1)
func_14638_call = mod.get_global_var('func_14638')
func_14643_call = mutated_mod.get_global_var('func_14643')
const_19063 = relay.const([6.630031,-3.318734,0.267775,-6.418538,-5.702575,-0.364434,-1.314989,3.411385,0.682586,-2.357226,0.445762,6.531889,3.404547,-5.776651,8.580623,7.401027,-2.331122,-0.653491,-3.975522,7.213636,0.850717,9.517792,-1.049243,8.123192,1.219660,1.137855,-2.879793,-0.711658,4.295591,-2.274947,2.474372,-1.575352,-6.567622,5.531192,9.627835,8.092100,-1.199028,-5.458394,-1.262922,6.909782,-4.812322,-3.539433,2.033840,-9.156642,1.059327,8.460748,6.976405,-7.768239,2.419289,-5.303077,4.444586,6.808571,-6.587505,-4.144624,9.997210,4.523794,-1.360315,0.554449,-8.643220,-9.799221,-4.138797,-5.866798,6.337172,0.268007,5.917524,7.026027,-9.312348,-8.517441,3.331518,3.606666,-4.029196,-8.272287,-5.630146,0.035856,9.861052,-1.956634,5.456411,7.606517,4.863136,5.138566,-8.492990,8.041317,4.363966,-2.817206,-1.221655,-1.947586,-4.502325,0.414690,-8.952824,3.410408,7.381804,0.843577,-3.208321,5.510691,-3.778559,-6.658991,-0.988748,1.001970,-2.648682,-5.434627,4.155562,6.509903,8.907480,-4.064949,2.823189,0.758345,6.680105,-0.546964,-4.346362,8.768813,-0.486815,2.526517,-7.458076,7.455368,-2.022107,9.813938,-0.928692,4.817193,-2.107682,1.582970,6.916587,-4.154467,0.630830,5.673103,-6.191798,-6.241104,-6.802864,3.270104,-5.279940,2.923047,-9.121208,-2.843305,-6.552725,-4.274809,6.727721,-4.807333,5.756633,1.441545,6.589301,-7.946848,-9.624996,3.321978,-3.145129,5.043020,4.532812,-0.894791,6.054438,-5.314479,-2.301689,-8.834718,-4.984184,9.819452,9.999800,-8.696799,1.819961,0.927908,-0.211207,-5.727220,4.869074,1.118707,6.618536,6.853079,3.524863,-0.094426,-2.976356,3.522319,6.882175,-7.221168,-1.113333,-4.660994,4.959540,9.119980,-2.390982,3.719525,7.189944,-9.030879,-5.578219,7.506557,3.543606,5.172616,4.313354,-9.299146,1.798114,8.407886,2.780144,5.911223,9.682632,-0.784025,5.911531,-7.992870,0.218045,5.615599,-7.671084,3.315891,-6.691266,0.947911,3.295827,-7.693095,8.228224,-3.000772,1.280863,3.877601,-6.246341,-0.504584,0.922955,-4.503901,2.810794,-8.777032,3.464968,9.449972,3.777772,2.806962,-7.298561,1.004219,9.291809,1.804463,-3.208236,-2.166476,-0.071278,-1.944423,7.632509,-8.375536,-4.992316,-0.886682,-0.626853,3.255405,-4.555648,9.010574,-0.718015,-0.333506,-6.655879,8.032838,6.588116,-8.240431,-5.569228,8.611825,1.520584,2.392642,2.169370,3.988222,3.762237,1.151545,5.463284,3.314001,7.189575,-6.360309,4.774764,-6.625864,3.226700,-8.539917,9.563908,5.331778,-9.686038,-9.584251,-1.478796,3.863753,-3.842481,6.233135,9.523758,-4.499932,3.907943,5.840214,-0.811175,8.183334], dtype = "float64")#candidate|19063|(264,)|const|float64
var_19064 = relay.var("var_19064", dtype = "float32", shape = (336,))#candidate|19064|(336,)|var|float32
const_19065 = relay.const([8.213525,9.690973,5.805565,-6.405595,1.863288,8.016406,-0.326209,-7.322840,-4.956100,-3.090613,0.996112,-0.476973,4.111003,-3.765167,-9.751284,-8.730388,4.589349,3.009449,6.801751,8.424375,-1.742441,0.452575,-0.748096,-8.942499,1.604637,4.565047,-8.781172,-5.056953,4.354755,-8.406367,-4.680462,-6.001078,5.758148,-9.777842,9.976874,2.069737,-4.797154,-3.193809,-8.547629,-7.525142,6.609548,7.686474,8.002939,8.313538,-7.764139,6.583172,0.576733,-7.766729,1.588635,1.592803,-0.012087,-0.020729,0.402970,0.956325,0.165072,-7.997753,3.367889,-5.427471,0.394745,-3.610161,-5.253637,-6.888034,6.192106,-4.977155,4.503012,6.877306,-0.489383,6.793645,-6.908369,-5.536022,-6.246836,-8.487383,-6.771319,-0.941096,-8.946805,4.483293,-0.124885,-3.127556,-1.776817,3.367171,-9.974633,-0.402444,-3.096002,9.494119,-0.667886,0.648395,-7.976257,7.506053,-1.926381,-4.576762,-2.973096,4.993741,-4.555857,-4.861613,-1.510478,-7.406226,-6.053313,-8.027448,-1.052037,3.353819,2.531377,1.866473,-5.972863,-5.429832,4.652522,3.841967,-9.380623,-6.490834,0.426322,4.472522,-1.587354,-3.594387,-3.404398,-5.997451,-0.304867,-7.926359,-1.729913,7.225392,-8.218990,3.864830,2.522313,2.633883,-4.795800,-3.464041,-6.319551,3.870973,9.373316,5.423438,-5.275941,3.506273,8.482626,-2.627428,7.152947,-4.061857,4.007241,7.251772,-4.691675,-6.719701,5.444579,-1.901142,4.251360,-7.365776,-7.182943,-3.076618,6.490925,0.439369,3.992481,-1.750065,-7.088708,-1.989797,3.959320,-0.282453,-8.924386,-3.629368,3.720831,6.305368,-6.204550,1.489658,1.221553,-5.442409,4.721984,0.076285,8.112501,-2.449708,-7.802804,-0.509942,-6.125494,-6.667120,8.061569,-0.519725,5.149582,8.396644,-6.430379,-6.817224,5.548554,-8.563448,4.715249,3.800325,-1.267917,-3.366922,4.358471,-6.676512,9.319479,-6.134210,4.777108,6.326417,8.897687,-8.018322,5.254744,5.830179,8.555541,-2.273841,-3.355181,-6.687167,0.518644,4.746475,4.939388,-2.573284,-6.574085,3.840987,-7.657910,3.111703,-1.451899,0.049090,-6.504912,-9.391465,-5.981132,-3.748354,-5.845409,3.562956,8.956075,-4.355453,-1.636726,3.159533,-5.329834,-3.921309,9.357492,-7.276425,-6.146249,-0.750660,-1.519989,-8.282124,5.397138,9.427674,2.321301,6.614042,-4.567212,4.817674,-0.722608,1.254837,-1.181251,9.804854,5.917960,5.747127,2.513866,0.669465,-1.505620,4.578916,-4.310686,4.321288,7.991317,7.294145,3.272443,9.332804,1.392227,-1.919860,-7.089920,-1.535976,9.081554,4.559388,0.141731,-6.658307,9.816118,1.280678,8.430991,2.021907,6.054768,-3.133140,-3.599661,-0.855958,-7.609690,5.473566,6.301364,5.673108,8.095097,3.250177,7.635551,-0.829274,1.836099,-3.945480,-0.255090,-8.881403,-1.591368,-0.685144,-4.726451,1.786417,5.661993,7.259743,-8.343327,9.363304,-0.330543,-6.295057,7.725501,-7.643349,-8.526893,6.472593,-7.233405,-1.635966,-5.819790,6.787559,3.706203,6.887995,2.450186,9.749587,2.338062,8.143959,-6.926280,4.282681,-0.572638,-0.970460,6.201156,-3.167602,9.590436,-8.578031,7.520572,-1.369745,-6.704115,-7.471519,4.698418,6.244015,-8.111529,-0.939054,-8.668079,-5.210378,3.142179,7.385842,-7.962313,-6.647448,-4.525869,2.054207,8.667633,3.966818,-1.119952,9.857467,8.072524,-3.852917,-1.213814,-4.274554,2.463726,1.040356,-4.976237,5.919657,-5.148019,-8.667845,-0.683189,7.121837,-0.941616,-7.539349,-3.523786,-7.179337,-9.069266,3.453482,0.692076,-3.548437,5.138002,5.135253,-5.066498,-1.052419,-2.073714,-3.060988,5.922550,-8.861994,-7.950950,-3.775737,7.878162,-0.422341,3.277790,-8.091582,-1.334852,2.548879,-7.837399,2.926844,9.183554,-2.166884,-2.389699,7.467195,-3.817115,9.874061,-4.018426,2.144658,-1.556816,7.011449,8.470318,-6.030427,-3.443101,6.863559,-9.809166,-2.196513,7.879642,-4.727805,9.010828,3.364252,6.610326,-6.269694,-1.051906,2.822947,9.870822,-5.943034,-1.412429,-2.423224,3.643922,-7.114078,-8.042982,5.229165,6.175367,-2.762854,6.801819,-7.654380,-4.171390,-9.932530,-0.745178,-0.458319,3.108429,-4.313922,7.729245,-0.505896,0.777359,4.939527,3.875096,6.031957,-4.455553,6.778293,3.600312,-4.318844,-9.390430,-9.966879,2.189195,6.201428,8.841458,-6.544626,-5.573701,6.253600,0.674886,-1.690768,-3.823945,5.289121,4.017331,-6.528332,-6.184834,-0.436084,-0.807511,4.469369,2.887978,-3.275936,9.050793,-6.234924,0.329049,2.752512,-2.891135,-7.358407,0.802157,6.651076,-5.465328,0.258322,-3.545497,-1.492467,-1.503225,-7.429713,-4.112271,-1.990337,-5.863125,7.574310,6.767470,-7.602368,-0.811004,-7.890955,6.555988,-4.862914,7.330440,-1.525180,-8.726938,-8.569407,3.389573,-9.485413,1.458131,1.033484,6.173926,-2.928670,1.327879,-7.905976,0.374327,9.029039,-6.802354,-3.983286,1.866819,-5.801132,9.626296,-2.736848,2.594809,-5.505654,4.245948,-6.154044,0.625888,5.679575,-4.876393,-8.271560,-7.347916,-8.189422,-1.307517,1.346532,7.639943,9.639531,-3.477101,0.100023,-3.633610,9.744720,1.151531,6.157241,-0.485626,4.837887,-1.316745,-7.253090,4.981919,-2.587823,2.055937,7.068466,4.947444,-1.002784,-7.616335,3.516180,4.384257,8.756895,2.057571,3.453871,7.198309,-5.687418,3.888421,8.192705,8.148999,-5.465316,6.651413,6.001413,-3.775119,-7.951094,-9.703782,3.808096,-8.991079,-9.261872,4.123322,8.360841,8.414131,7.590424,-7.000143,3.999478,-0.224893,4.014299,-7.908272,-0.529850,-8.932735,9.170880,-1.834098,-1.132496,1.332853,-1.933633,6.652816,-8.602692,4.072642,1.075692,-3.460640,1.107694,-1.751034,-7.006825,-4.864049,1.901988,1.658949,7.109865,7.947639,7.849286,-6.560608,-8.456496,3.731537,-1.945564,-1.087129,5.188117,9.727767,0.177024,9.138431,-2.568612,-7.820636,-8.580094,-4.459624,0.776614,5.664492,5.643984,3.499114,6.418201,-4.513350,2.721867,9.754479,4.614114,-9.649945,-4.424437,-9.523043,6.662112,-8.788148,-4.785627,5.146463,6.759547,-7.001286,-6.392442,-0.939323,5.580145,-0.094621,3.823452,9.290752,-3.175225,8.093320,9.894190,7.458781,-6.469677,-7.252207,-0.144813,-9.939137,-7.219932,-5.599859,-5.571939,0.801146,8.490899,2.795540,9.780094,2.271120,-0.535049,4.016424,-6.096347,-3.150104,-0.078837,-0.233801,-6.838602,-4.382682,1.667293,6.469523,6.622186,7.329219,-6.437547,9.189300,5.735965,4.098084,5.169503,7.195261,0.973658,-6.603495,-3.792590,3.225403,-9.088987,-2.481448,-1.600388,7.614811,-1.858492,2.706596,0.465345,-7.401923,2.558108,-5.814264,-0.499012,4.120404,2.900563,-2.963715,-6.450212,-3.583126,5.470320,-7.973636,6.475868,-4.339083,3.987354,-0.209181,-1.502439,2.454275,4.823616,6.754837,-3.840455,3.080276,-8.321334,6.092300,1.041924,0.422511,-9.335438,5.809291,-6.326035,9.542213,1.181232,-2.632829,5.811458,2.340820,-9.491388,-2.152011,5.186605,-9.142799,7.771053,-6.946450,-6.521482,-8.315611,-0.106049,-0.633883,2.338004,-2.597273,9.270528,-4.231497,-0.678199,3.416628,-8.353014,2.828080,-4.071324,-9.779713,-4.163785,-6.790805,-2.802422,0.233221,-2.352062,2.441636,-4.817383,-0.303441,2.863494,-4.247782,1.387668,-5.151042,9.909103,5.195562,2.184026,-3.047862,9.918076,-9.311088,6.716616,-3.610434,8.293191,1.693845,1.496019,-4.992160,-2.446591,-0.040321,-5.442765,-3.538623,5.078645,0.942440,4.602146,-8.533355,8.408453,-0.386978,-5.025885,-2.783680,9.714157,1.332437,-2.051612,3.659480,-5.490533,-4.658039,-3.232669,7.207222,-1.269647,-5.708375,-4.764055,-2.852065,-0.808603,-0.642425,2.878445,-0.320276,-8.548347,8.999526,7.010501,4.515016,9.154981,1.904142,-2.323793,1.602781,4.691548,-8.924633,-3.333412,3.692437,-5.533807,5.687098,2.698221,-1.864687,-1.018146,-2.240944,-2.590651,3.392862,8.408323,6.845246,6.458330,-5.595561,-4.134437,-7.414819,-8.684733,2.403245,7.224323,-4.223469,6.002163,-3.310463,7.819554,4.629169,9.263110,6.299162,3.785834,-9.081410,5.580988,-1.279255,-7.511031,-6.687806,-8.859599,9.784525,-1.309330,-0.752857,-0.130859,3.810948,2.670937,4.498045,-1.309207,4.914527,8.956147,-7.836354,1.956334,-4.921243,-6.191155,-4.007004,8.778116,-4.772882,0.870312,6.669991,-3.384541,8.744391,4.088654,-6.980036,1.264360,-1.731425,3.979025,2.673522,4.719311,-7.142354,-9.720500,-6.857387,-3.515914,-5.219437,-5.688582,6.034909,-3.971137,-1.071875,1.304491,8.100488,2.143044,9.241083,5.365732,7.769004,5.470667,-2.314622,-5.747178,3.672417,8.402077,-5.931885,9.944598,-0.897768,0.822434,2.055335,8.601829,7.863517,-2.920526,-3.461288,-4.973319,-6.395775,8.524317,6.073569,-5.581054,7.030563,-7.535817,6.829252,1.943743,-3.621873,-3.289605,-8.545094,-0.852666,-5.582117,-7.009065,-1.954215,-1.362948,-8.348452,2.249935,3.575160,-5.175614,-2.134905,6.142854,-2.267039,1.975592,8.666401,9.692223,-5.872997,2.864303,-2.011323,8.345899,-3.587227,-9.447801,6.667440,4.008701,0.354030,4.664912,-2.131767,4.884888,-9.273602,7.975547,-1.279431,9.070391,7.980171,-0.632761,-5.628448,-2.364182,6.626527,-1.579238,0.152087,-8.023451,9.066891,-6.377536,-3.384017,3.216328,-7.147052,-8.792998,0.631521,3.417791,-3.556015,-8.490321,2.109797,-1.913468,1.504643,-2.463408,-3.530897,5.394966,-8.474487,9.803578,7.553359,9.432329,-3.220935,2.650938,0.209602,-2.284479,-3.246521,3.103263,9.319229,-0.237348,-4.764379,2.304836,7.555099,-1.345541,-2.776221,-4.146610,-2.360582,-5.658036,5.501423,-0.758399,-2.161132,1.186483,-1.610872,0.308144,-1.275257,-7.080924,-1.244157,3.940582,7.507949,9.146982,6.812381,5.186643,-7.363195,-8.224083,2.372274,-2.841505,8.624961,-6.497263,-5.684371,-8.977333,-8.575008,9.929061,-2.890719,-7.751701,8.761857,-7.482104,-9.545479,-6.464621,2.157216,-0.545135,-5.005838,-0.890231,-9.256221,3.871664,-1.599534,7.441443,-8.623005,8.337366,3.516562,-0.892211,-5.789688,-8.971585,7.831622,9.622679,8.931767,5.583105,-6.662545,-2.194130,4.129356,-6.686707,6.531809,-8.825526,-4.351523,-4.532704,8.283084,-9.336138,1.839298,-0.881474,-6.890860,1.555253,-5.458055,3.816388,4.875071,3.851349,7.537056,-5.164010,-4.060736,-8.779577,9.216338,-1.131601,-0.359541,-4.964717,9.327801,-5.685162], dtype = "float64")#candidate|19065|(1008,)|const|float64
var_19066 = relay.var("var_19066", dtype = "bool", shape = (504,))#candidate|19066|(504,)|var|bool
call_19062 = relay.TupleGetItem(func_14638_call(relay.reshape(const_19063.astype('float64'), [264,]), relay.reshape(var_19064.astype('float32'), [336,]), relay.reshape(const_19065.astype('float64'), [2, 504]), relay.reshape(var_19066.astype('bool'), [504,]), ), 7)
call_19067 = relay.TupleGetItem(func_14643_call(relay.reshape(const_19063.astype('float64'), [264,]), relay.reshape(var_19064.astype('float32'), [336,]), relay.reshape(const_19065.astype('float64'), [2, 504]), relay.reshape(var_19066.astype('bool'), [504,]), ), 7)
func_12828_call = mod.get_global_var('func_12828')
func_12832_call = mutated_mod.get_global_var('func_12832')
const_19083 = relay.const([-6,4,-9,-1,10,-7,2,5,2,2,-5,-3,4,-8,-8,8,3,-3,-6,5,2,1,9,-7,-3,8,-1,-7,-7,-9,-2,-8,-1,-9,-7,-3,8,3,1,10,-9,4,-9,7,5,-10,5,2,-1,2,-5,7,2,-3,-9,9,-1,-10,-3,8,-2,-5,-8,-2,-7,-7,1,8,-5,8,-3,-4,9,7,-10,10,-5,7,-3,2,-3,-4,6,-10,10,9,-5,10,-6,4,1,-7,10,-2,1,2,-7,-10,8,-6,-8,-4,7,-6,10,-10,-5,-9,-9,5,7,7,4,6,9,-2,6,-9,7,-7,-7,-8,-4,-9,-8,-4,-4,8,10,9], dtype = "uint64")#candidate|19083|(130,)|const|uint64
var_19084 = relay.var("var_19084", dtype = "float32", shape = (396,))#candidate|19084|(396,)|var|float32
call_19082 = relay.TupleGetItem(func_12828_call(relay.reshape(const_19083.astype('uint64'), [13, 10]), relay.reshape(var_19084.astype('float32'), [396,]), ), 2)
call_19085 = relay.TupleGetItem(func_12832_call(relay.reshape(const_19083.astype('uint64'), [13, 10]), relay.reshape(var_19084.astype('float32'), [396,]), ), 2)
func_12223_call = mod.get_global_var('func_12223')
func_12228_call = mutated_mod.get_global_var('func_12228')
const_19096 = relay.const([[3,-3,5,-9,-4,-2,10,3,2,-3,-2,-2,-8,-8,7,5,6,-4,-5,7,6,4,-1,2,-1,-8,9,5,-10,-10,-4,8,7,2,7,-1]], dtype = "int8")#candidate|19096|(1, 36)|const|int8
var_19097 = relay.var("var_19097", dtype = "float32", shape = (18,))#candidate|19097|(18,)|var|float32
call_19095 = relay.TupleGetItem(func_12223_call(relay.reshape(const_19096.astype('int8'), [9, 4, 1]), relay.reshape(call_19060.astype('bool'), []), relay.reshape(call_19082.astype('float64'), [480,]), relay.reshape(var_19097.astype('float32'), [18,]), ), 4)
call_19098 = relay.TupleGetItem(func_12228_call(relay.reshape(const_19096.astype('int8'), [9, 4, 1]), relay.reshape(call_19060.astype('bool'), []), relay.reshape(call_19082.astype('float64'), [480,]), relay.reshape(var_19097.astype('float32'), [18,]), ), 4)
func_17844_call = mod.get_global_var('func_17844')
func_17845_call = mutated_mod.get_global_var('func_17845')
call_19105 = relay.TupleGetItem(func_17844_call(), 1)
call_19106 = relay.TupleGetItem(func_17845_call(), 1)
output = relay.Tuple([call_19060,call_19062,const_19063,var_19064,const_19065,var_19066,call_19082,const_19083,var_19084,call_19095,const_19096,var_19097,call_19105,])
output2 = relay.Tuple([call_19061,call_19067,const_19063,var_19064,const_19065,var_19066,call_19085,const_19083,var_19084,call_19098,const_19096,var_19097,call_19106,])
func_19107 = relay.Function([var_19064,var_19066,var_19084,var_19097,], output)
mod['func_19107'] = func_19107
mod = relay.transform.InferType()(mod)
var_19108 = relay.var("var_19108", dtype = "float32", shape = (336,))#candidate|19108|(336,)|var|float32
var_19109 = relay.var("var_19109", dtype = "bool", shape = (504,))#candidate|19109|(504,)|var|bool
var_19110 = relay.var("var_19110", dtype = "float32", shape = (396,))#candidate|19110|(396,)|var|float32
var_19111 = relay.var("var_19111", dtype = "float32", shape = (18,))#candidate|19111|(18,)|var|float32
output = func_19107(var_19108,var_19109,var_19110,var_19111,)
func_19112 = relay.Function([var_19108,var_19109,var_19110,var_19111,], output)
mutated_mod['func_19112'] = func_19112
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17982_call = mod.get_global_var('func_17982')
func_17983_call = mutated_mod.get_global_var('func_17983')
call_19126 = func_17982_call()
call_19127 = func_17982_call()
output = call_19126
output2 = call_19127
func_19128 = relay.Function([], output)
mod['func_19128'] = func_19128
mod = relay.transform.InferType()(mod)
output = func_19128()
func_19129 = relay.Function([], output)
mutated_mod['func_19129'] = func_19129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13858_call = mod.get_global_var('func_13858')
func_13859_call = mutated_mod.get_global_var('func_13859')
call_19209 = func_13858_call()
call_19210 = func_13858_call()
output = call_19209
output2 = call_19210
func_19218 = relay.Function([], output)
mod['func_19218'] = func_19218
mod = relay.transform.InferType()(mod)
mutated_mod['func_19218'] = func_19218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19218_call = mutated_mod.get_global_var('func_19218')
call_19219 = func_19218_call()
output = call_19219
func_19220 = relay.Function([], output)
mutated_mod['func_19220'] = func_19220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14930_call = mod.get_global_var('func_14930')
func_14932_call = mutated_mod.get_global_var('func_14932')
call_19276 = relay.TupleGetItem(func_14930_call(), 2)
call_19277 = relay.TupleGetItem(func_14932_call(), 2)
func_18037_call = mod.get_global_var('func_18037')
func_18039_call = mutated_mod.get_global_var('func_18039')
call_19292 = relay.TupleGetItem(func_18037_call(), 0)
call_19293 = relay.TupleGetItem(func_18039_call(), 0)
output = relay.Tuple([call_19276,call_19292,])
output2 = relay.Tuple([call_19277,call_19293,])
func_19297 = relay.Function([], output)
mod['func_19297'] = func_19297
mod = relay.transform.InferType()(mod)
output = func_19297()
func_19298 = relay.Function([], output)
mutated_mod['func_19298'] = func_19298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16523_call = mod.get_global_var('func_16523')
func_16525_call = mutated_mod.get_global_var('func_16525')
call_19405 = relay.TupleGetItem(func_16523_call(), 0)
call_19406 = relay.TupleGetItem(func_16525_call(), 0)
func_12987_call = mod.get_global_var('func_12987')
func_12988_call = mutated_mod.get_global_var('func_12988')
call_19443 = func_12987_call()
call_19444 = func_12987_call()
func_12133_call = mod.get_global_var('func_12133')
func_12137_call = mutated_mod.get_global_var('func_12137')
const_19464 = relay.const(6, dtype = "int16")#candidate|19464|()|const|int16
var_19465 = relay.var("var_19465", dtype = "uint64", shape = (160,))#candidate|19465|(160,)|var|uint64
call_19463 = relay.TupleGetItem(func_12133_call(relay.reshape(const_19464.astype('int16'), []), relay.reshape(var_19465.astype('uint64'), [160,]), ), 0)
call_19466 = relay.TupleGetItem(func_12137_call(relay.reshape(const_19464.astype('int16'), []), relay.reshape(var_19465.astype('uint64'), [160,]), ), 0)
func_18510_call = mod.get_global_var('func_18510')
func_18512_call = mutated_mod.get_global_var('func_18512')
call_19468 = relay.TupleGetItem(func_18510_call(), 0)
call_19469 = relay.TupleGetItem(func_18512_call(), 0)
func_18019_call = mod.get_global_var('func_18019')
func_18020_call = mutated_mod.get_global_var('func_18020')
call_19472 = func_18019_call()
call_19473 = func_18019_call()
func_13220_call = mod.get_global_var('func_13220')
func_13225_call = mutated_mod.get_global_var('func_13225')
const_19478 = relay.const([-0.428395,-8.736162,-6.642833,-3.156821,-9.090593,2.341842,4.021034,0.972800,3.888688,-3.703150,5.883572,-6.371709,-8.285455,-3.027640,3.396213,1.907279,1.864779,5.779893,-1.137719,-1.655681,1.166372,-6.690337,-6.216265,3.782168,-0.617116,-9.879436,-1.664006,-0.309874,-5.072709,5.181106], dtype = "float64")#candidate|19478|(30,)|const|float64
var_19479 = relay.var("var_19479", dtype = "float64", shape = (832,))#candidate|19479|(832,)|var|float64
var_19480 = relay.var("var_19480", dtype = "float64", shape = (480,))#candidate|19480|(480,)|var|float64
call_19477 = relay.TupleGetItem(func_13220_call(relay.reshape(const_19478.astype('float64'), [30,]), relay.reshape(var_19479.astype('float64'), [832,]), relay.reshape(var_19480.astype('float64'), [480,]), ), 2)
call_19481 = relay.TupleGetItem(func_13225_call(relay.reshape(const_19478.astype('float64'), [30,]), relay.reshape(var_19479.astype('float64'), [832,]), relay.reshape(var_19480.astype('float64'), [480,]), ), 2)
output = relay.Tuple([call_19405,call_19443,call_19463,const_19464,var_19465,call_19468,call_19472,call_19477,const_19478,var_19479,var_19480,])
output2 = relay.Tuple([call_19406,call_19444,call_19466,const_19464,var_19465,call_19469,call_19473,call_19481,const_19478,var_19479,var_19480,])
func_19487 = relay.Function([var_19465,var_19479,var_19480,], output)
mod['func_19487'] = func_19487
mod = relay.transform.InferType()(mod)
var_19488 = relay.var("var_19488", dtype = "uint64", shape = (160,))#candidate|19488|(160,)|var|uint64
var_19489 = relay.var("var_19489", dtype = "float64", shape = (832,))#candidate|19489|(832,)|var|float64
var_19490 = relay.var("var_19490", dtype = "float64", shape = (480,))#candidate|19490|(480,)|var|float64
output = func_19487(var_19488,var_19489,var_19490,)
func_19491 = relay.Function([var_19488,var_19489,var_19490,], output)
mutated_mod['func_19491'] = func_19491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19218_call = mod.get_global_var('func_19218')
func_19220_call = mutated_mod.get_global_var('func_19220')
call_19578 = func_19218_call()
call_19579 = func_19218_call()
func_14426_call = mod.get_global_var('func_14426')
func_14427_call = mutated_mod.get_global_var('func_14427')
call_19594 = func_14426_call()
call_19595 = func_14426_call()
output = relay.Tuple([call_19578,call_19594,])
output2 = relay.Tuple([call_19579,call_19595,])
func_19599 = relay.Function([], output)
mod['func_19599'] = func_19599
mod = relay.transform.InferType()(mod)
mutated_mod['func_19599'] = func_19599
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19599_call = mutated_mod.get_global_var('func_19599')
call_19600 = func_19599_call()
output = call_19600
func_19601 = relay.Function([], output)
mutated_mod['func_19601'] = func_19601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14760_call = mod.get_global_var('func_14760')
func_14762_call = mutated_mod.get_global_var('func_14762')
call_19626 = relay.TupleGetItem(func_14760_call(), 0)
call_19627 = relay.TupleGetItem(func_14762_call(), 0)
uop_19644 = relay.cos(call_19626.astype('float32')) # shape=(9, 5, 14)
uop_19646 = relay.cos(call_19627.astype('float32')) # shape=(9, 5, 14)
output = uop_19644
output2 = uop_19646
func_19655 = relay.Function([], output)
mod['func_19655'] = func_19655
mod = relay.transform.InferType()(mod)
output = func_19655()
func_19656 = relay.Function([], output)
mutated_mod['func_19656'] = func_19656
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15046_call = mod.get_global_var('func_15046')
func_15047_call = mutated_mod.get_global_var('func_15047')
call_19660 = relay.TupleGetItem(func_15046_call(), 0)
call_19661 = relay.TupleGetItem(func_15047_call(), 0)
func_3395_call = mod.get_global_var('func_3395')
func_3398_call = mutated_mod.get_global_var('func_3398')
var_19686 = relay.var("var_19686", dtype = "float64", shape = (1008,))#candidate|19686|(1008,)|var|float64
call_19685 = relay.TupleGetItem(func_3395_call(relay.reshape(var_19686.astype('float64'), [9, 8, 14]), relay.reshape(var_19686.astype('float64'), [9, 8, 14]), ), 0)
call_19687 = relay.TupleGetItem(func_3398_call(relay.reshape(var_19686.astype('float64'), [9, 8, 14]), relay.reshape(var_19686.astype('float64'), [9, 8, 14]), ), 0)
func_13629_call = mod.get_global_var('func_13629')
func_13633_call = mutated_mod.get_global_var('func_13633')
var_19693 = relay.var("var_19693", dtype = "float64", shape = (432,))#candidate|19693|(432,)|var|float64
var_19694 = relay.var("var_19694", dtype = "float64", shape = (264,))#candidate|19694|(264,)|var|float64
const_19695 = relay.const([0.755588,9.135544,-9.696495,3.582687,-3.742891,9.398918,-9.929577,-0.807370,0.336316,8.105487,0.028573,2.454633,-3.767372,5.975568,1.203537,-0.405917,-4.411801,-7.795969,-6.633335,-0.547599,0.470569,4.610397,9.860446,0.334565,2.696375,7.582905,7.142456,7.446269,1.485171,2.773870,5.581864,3.002095,3.848407,4.870918,3.489172,8.874755,6.487152,-0.283719,-8.132798,7.407972,-9.309618,-8.112609,-2.482271,9.783269,-7.100477,-0.868538,-7.593916,6.441071,9.605488,7.821920,-3.043671,8.048574,-6.067693,1.071416,5.771455,-8.149423,3.106526,0.084633,-7.120697,2.774882,5.900082,1.069072,5.909356,-5.282858,0.934589,7.330680,-4.250479,5.893944,-1.309573,0.803053,-0.929932,7.580535,8.356773,3.854749,1.807633,-6.913776,-8.375684,4.823768,3.103633,-7.977790,4.620725,-0.995652,9.929355,-5.064230,-8.018088,8.804174,-8.243771,-1.935144,-9.976230,9.644341,-7.062851,-7.793198,8.463328,-9.614685,0.858158,6.517557,-9.978461,-9.650219,-3.390281,2.527475,8.636906,2.006849,5.297225,4.677238,4.704147,-8.175018,-5.150935,-5.166257,-1.538797,-8.885847,4.374954,-8.429509,-0.889383,3.771919,-0.909586,6.692197,-0.208454,2.507184,6.541225,7.599323,7.623591,-2.750196,-6.009885,-8.459733,-4.880213,2.825786,-7.288436,8.350013,-5.583986,9.736216,-5.195130,-5.964923,1.721553,-6.711923,-0.660788,4.516382,5.649929,-8.751901,-7.892284,-7.732604,7.419820,6.917847,-0.644525,-3.622252,6.679144,2.277434,4.467138,-3.610295,1.581369,8.816034,-4.040836,1.735712,-9.340852,-3.083122,-4.087926,5.584949,-0.713290,-1.817186,-2.713097,7.832040,-1.325808,6.466781,9.810125,1.428918,-8.729689,-0.007019,1.543786,3.629161,1.861438,7.703439,-1.908580,-6.794451,0.288169,2.539256,0.336907,6.349323,9.348078,3.965267,5.078827,8.146383,4.427173,-9.753946,-7.764729,2.052171,0.681235,6.609446,3.006841,-4.857075,-1.088522,-1.449871,4.005305,-9.411707,-7.480813,7.657278,-0.689981,-2.033051,-3.731327,-5.949374,-3.386258,8.157751,-3.176729,6.658981,-9.524407,-1.348081,-2.610053,-6.568634,9.458917,-1.259316,0.205706,9.258756,7.694443,0.448626,-0.561032,-0.881162,4.083411,8.212991,-8.460165,-3.161423,-0.133362,-3.204143,7.358072,-5.121507,7.763040,3.651618,-3.755253,-9.295460,-5.923738,-3.675177,3.975844,4.156105,-8.031893,2.137185,2.764806,8.716985,-0.287433,-1.957002,-1.969972,-4.455942,-4.259827,-9.677585,-7.054789,-7.082825,8.514042,-3.948413,0.123974,1.183095,-9.695950,-7.531374,-9.530239,3.701802,4.894964,7.604913,8.082306,1.433052,3.829761,-4.925449,-7.095341,-4.368791,4.070265,5.822231,-3.635351,-2.047118,3.392144,-7.117670,-7.649350,-6.061515,-6.471380,-2.744354,-9.779052,9.897164,7.417218,6.059053,-9.223582,5.800538,-1.104765,-9.037417,-5.309079,9.168956,8.412383,6.634743,-0.288611,-3.081011,2.080320,-5.019784,-6.425147,6.335164,8.835013,-6.994552,-9.993123,-9.357253,-2.184385,0.143100,7.698705,-3.147564,0.495342,7.981470,6.634441,-8.524736,-8.057674,-0.022557,-0.930413,-4.787734,9.648107,9.891132,9.914412,-9.646459,-8.707409,-9.049806,2.306916,-0.245964,-1.530494,-4.310993,7.367053,1.155905,2.525023,5.067925,2.947276,0.200208,-8.371562,5.960314,-2.159617,6.228085,1.486883,5.241052,-5.033004,6.252321,9.055649,-6.264199,-5.102148,-7.404038,-5.290425,3.608725,2.020813,-7.836632,5.547086,5.182595,8.912603,-7.413558,-3.685057,3.746980,-4.957952,-0.733704,-1.423651,-0.917888,-7.863854,-1.339772,-9.470276,-2.950374,3.072614,0.672025,-8.594255,-5.090499,4.850464,1.020288,-5.283977,-4.129018,8.183939,-5.876278,-9.851184,8.975063,7.503328,4.326564,0.313399,-7.326734,-8.913100,-5.667661,-6.864732,-2.561827,6.603268,-9.479353,9.027573,-4.183033,5.729023,-2.733344,-0.668804,-2.150779,-9.135533,6.350768,1.255714,-6.613646,-4.149762,5.895600,6.071109,-3.658342,7.132936,8.020271,-3.839885,4.090434,-4.889366,2.749462,4.044862,3.195634,3.307885,-8.314568,-1.296292,-6.907241,2.952124,8.294989,3.510007,2.708763,-0.837730,3.975614,9.977356,-0.987548,2.968503,-0.798516,7.277545,-4.306745,-2.237442,-8.008012,9.442178,0.251698,-3.016240,0.933199,6.717880,-5.655655,7.381450,-2.228261,-1.069662,2.360345,-8.311865,9.731487,5.740578,-6.874979,-4.184695,-8.787325,5.256070,-2.804637,-2.780494,7.395922,-5.790233,-3.907490,-1.925750,-7.277584,3.032229,-9.182223,0.375309,-9.027613,7.947379,0.283630,4.016141,8.030043,4.337734,-1.840471,9.326311,9.980520,9.701849,-6.029703,-7.122808,-0.954341,-7.832447,2.118437,-4.726686,-8.628196,-1.307949,6.153753,1.833167,-3.826602,-9.868524,-6.128187,4.935767,-4.379950,4.035287,-6.326174,3.769396,-8.097394,1.764945,-2.600897,0.112641,2.893621,-6.872600,5.176892,7.401744,-2.787476,-8.743413,4.891501,7.811114,-3.748613,-3.745055,-0.508147,7.551146,5.632462,9.768191,8.000686,-4.058182,-8.982283,5.970847,-5.877524,-2.975358,1.388560,-2.910087,-6.720290,-3.763882,-1.453721,5.961418,-5.285811,5.271694,7.741701,1.239987,0.577119,6.519162,-4.321144,7.038789,0.708790,-8.485238,-8.737333,2.198207,-8.386929,1.841463,3.354185,3.826579,-6.726493,2.231760,7.729412,-0.161448,5.595858,6.941764,-8.698032,-8.858988,-3.343986,-7.125595,0.963117,1.315510,4.144746,4.867962,2.859907,2.045086,4.248297,7.118594,3.586733,-0.940504,9.320722,3.464279,-9.326252,6.525400,-7.342010,-0.137426,6.825599,7.712046,-6.723535,1.183589,8.370436,8.243855,-2.667282,-7.880826,-0.744465,-0.924699,-2.930634,-1.753775,2.002946,1.519873,0.015996,-1.225636,8.453096,-0.778954,-7.154343,5.519356,-7.210020,-8.813922,9.086439,-4.906763,6.433850,0.574661,-0.140785,3.143531,5.989437,8.920457,-0.152825,3.754229,1.216730,4.789841,-0.419165,-7.806505,-3.304715,9.985447,6.505187,9.673882,-2.027928,-7.004538,-9.512189,-8.218900,-7.596645,6.783581,8.387671,-2.774773,-2.748045,-7.777196,-2.184684,3.000127,-4.352342,-8.380528,-1.100082,-4.769386,-3.711968,-8.882692,-8.671917,-0.575198,-7.359622,1.312451,-8.571388,8.945994,-1.105093,9.503368,-1.587971,4.749421,9.579798,-1.961528,5.693414,-3.672957,1.258633,9.572733,-6.259877,-9.761486,9.586328,-1.266148,8.734083,-8.382864,-4.611391,-7.868391,-5.960396,1.664650,7.918043,7.309958,-9.910435,-6.375303,-7.821716,-9.145571,7.524967,-6.909614,-8.183149,-3.712464,-6.559263,0.282093,6.813758,3.865349,1.339557,7.866529,-8.486897,-4.430504,4.363187,-2.573205,-7.429225,-5.542536,8.446636,-9.039882,1.109860,5.866792,1.697600,-3.857040,-1.637471,-5.703176,-9.182896,-9.217117,-2.777565,-9.101142,4.744887,-9.038870,1.046220,2.483810,0.932358,-0.373784,-2.471587,-2.131156,8.635429,-2.458267,-0.609914,6.791173,3.638714,8.900430,-8.647649,9.000022,-2.525963,5.310099,-9.520680,-3.165972,-2.778034,-6.695774,-1.339567,-7.609785,-3.276672,8.502787,7.940084,5.586550,-6.805315,4.626493,-1.961633,-1.862896,-4.028504,-5.159943,-5.274240,-2.850868,-9.330685,5.849772,1.865341,-7.881572,2.508003,-3.982128,-5.398680,4.999760,-5.893889,-6.334510,1.326848,6.174456,-8.630954,-7.364079,-5.844896,-9.953999,9.105756,3.236832,6.008976,-3.044212,0.764432,-1.421218,7.429134,-9.852216,-0.566514,-6.159752,2.704769,5.176231,-7.148692,-9.085224,-9.248519,9.022245,-0.745154,-9.564919,-5.262833,-5.040620,2.408772,5.795938,-9.725541,-8.958349,-0.111986,-0.913490,-4.375497,-4.032583,5.215351,4.456522,6.589332,-4.854770,2.769383,7.118735,1.835149,1.325663,-5.911061,3.093982,-1.573904,7.859577,3.629130,-0.820256,5.095983], dtype = "float32")#candidate|19695|(750,)|const|float32
call_19692 = relay.TupleGetItem(func_13629_call(relay.reshape(var_19693.astype('float64'), [4, 108]), relay.reshape(var_19694.astype('float64'), [264,]), relay.reshape(const_19695.astype('float32'), [750,]), ), 4)
call_19696 = relay.TupleGetItem(func_13633_call(relay.reshape(var_19693.astype('float64'), [4, 108]), relay.reshape(var_19694.astype('float64'), [264,]), relay.reshape(const_19695.astype('float32'), [750,]), ), 4)
output = relay.Tuple([call_19660,call_19685,var_19686,call_19692,var_19693,var_19694,const_19695,])
output2 = relay.Tuple([call_19661,call_19687,var_19686,call_19696,var_19693,var_19694,const_19695,])
func_19709 = relay.Function([var_19686,var_19693,var_19694,], output)
mod['func_19709'] = func_19709
mod = relay.transform.InferType()(mod)
mutated_mod['func_19709'] = func_19709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19709_call = mutated_mod.get_global_var('func_19709')
var_19711 = relay.var("var_19711", dtype = "float64", shape = (1008,))#candidate|19711|(1008,)|var|float64
var_19712 = relay.var("var_19712", dtype = "float64", shape = (432,))#candidate|19712|(432,)|var|float64
var_19713 = relay.var("var_19713", dtype = "float64", shape = (264,))#candidate|19713|(264,)|var|float64
call_19710 = func_19709_call(var_19711,var_19712,var_19713,)
output = call_19710
func_19714 = relay.Function([var_19711,var_19712,var_19713,], output)
mutated_mod['func_19714'] = func_19714
mutated_mod = relay.transform.InferType()(mutated_mod)
var_19744 = relay.var("var_19744", dtype = "float64", shape = ())#candidate|19744|()|var|float64
var_19745 = relay.var("var_19745", dtype = "float64", shape = (8, 8, 1))#candidate|19745|(8, 8, 1)|var|float64
bop_19746 = relay.mod(var_19744.astype('float64'), var_19745.astype('float64')) # shape=(8, 8, 1)
output = bop_19746
output2 = bop_19746
func_19749 = relay.Function([var_19744,var_19745,], output)
mod['func_19749'] = func_19749
mod = relay.transform.InferType()(mod)
mutated_mod['func_19749'] = func_19749
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19749_call = mutated_mod.get_global_var('func_19749')
var_19751 = relay.var("var_19751", dtype = "float64", shape = ())#candidate|19751|()|var|float64
var_19752 = relay.var("var_19752", dtype = "float64", shape = (8, 8, 1))#candidate|19752|(8, 8, 1)|var|float64
call_19750 = func_19749_call(var_19751,var_19752,)
output = call_19750
func_19753 = relay.Function([var_19751,var_19752,], output)
mutated_mod['func_19753'] = func_19753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18051_call = mod.get_global_var('func_18051')
func_18053_call = mutated_mod.get_global_var('func_18053')
call_19792 = func_18051_call()
call_19793 = func_18051_call()
func_13858_call = mod.get_global_var('func_13858')
func_13859_call = mutated_mod.get_global_var('func_13859')
call_19802 = func_13858_call()
call_19803 = func_13858_call()
output = relay.Tuple([call_19792,call_19802,])
output2 = relay.Tuple([call_19793,call_19803,])
func_19811 = relay.Function([], output)
mod['func_19811'] = func_19811
mod = relay.transform.InferType()(mod)
output = func_19811()
func_19812 = relay.Function([], output)
mutated_mod['func_19812'] = func_19812
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18723_call = mod.get_global_var('func_18723')
func_18724_call = mutated_mod.get_global_var('func_18724')
call_19874 = func_18723_call()
call_19875 = func_18723_call()
func_18659_call = mod.get_global_var('func_18659')
func_18660_call = mutated_mod.get_global_var('func_18660')
call_19892 = relay.TupleGetItem(func_18659_call(), 1)
call_19893 = relay.TupleGetItem(func_18660_call(), 1)
output = relay.Tuple([call_19874,call_19892,])
output2 = relay.Tuple([call_19875,call_19893,])
func_19894 = relay.Function([], output)
mod['func_19894'] = func_19894
mod = relay.transform.InferType()(mod)
output = func_19894()
func_19895 = relay.Function([], output)
mutated_mod['func_19895'] = func_19895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18887_call = mod.get_global_var('func_18887')
func_18889_call = mutated_mod.get_global_var('func_18889')
call_19930 = relay.TupleGetItem(func_18887_call(), 0)
call_19931 = relay.TupleGetItem(func_18889_call(), 0)
output = relay.Tuple([call_19930,])
output2 = relay.Tuple([call_19931,])
func_19939 = relay.Function([], output)
mod['func_19939'] = func_19939
mod = relay.transform.InferType()(mod)
mutated_mod['func_19939'] = func_19939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19939_call = mutated_mod.get_global_var('func_19939')
call_19940 = func_19939_call()
output = call_19940
func_19941 = relay.Function([], output)
mutated_mod['func_19941'] = func_19941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19811_call = mod.get_global_var('func_19811')
func_19812_call = mutated_mod.get_global_var('func_19812')
call_20008 = relay.TupleGetItem(func_19811_call(), 0)
call_20009 = relay.TupleGetItem(func_19812_call(), 0)
func_15174_call = mod.get_global_var('func_15174')
func_15176_call = mutated_mod.get_global_var('func_15176')
call_20010 = func_15174_call()
call_20011 = func_15174_call()
output = relay.Tuple([call_20008,call_20010,])
output2 = relay.Tuple([call_20009,call_20011,])
func_20019 = relay.Function([], output)
mod['func_20019'] = func_20019
mod = relay.transform.InferType()(mod)
output = func_20019()
func_20020 = relay.Function([], output)
mutated_mod['func_20020'] = func_20020
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15613_call = mod.get_global_var('func_15613')
func_15615_call = mutated_mod.get_global_var('func_15615')
call_20062 = relay.TupleGetItem(func_15613_call(), 0)
call_20063 = relay.TupleGetItem(func_15615_call(), 0)
uop_20065 = relay.log(call_20062.astype('float32')) # shape=(9, 11, 4)
uop_20067 = relay.log(call_20063.astype('float32')) # shape=(9, 11, 4)
output = uop_20065
output2 = uop_20067
func_20068 = relay.Function([], output)
mod['func_20068'] = func_20068
mod = relay.transform.InferType()(mod)
output = func_20068()
func_20069 = relay.Function([], output)
mutated_mod['func_20069'] = func_20069
mutated_mod = relay.transform.InferType()(mutated_mod)
var_20080 = relay.var("var_20080", dtype = "uint16", shape = (14, 2, 5))#candidate|20080|(14, 2, 5)|var|uint16
const_20081 = relay.const([[[-7,-9,-9,-9,2],[-2,2,7,4,8]],[[7,3,2,-5,9],[6,-3,9,3,-4]],[[-1,-3,-6,8,-8],[-3,-10,-1,8,-5]],[[-3,4,-5,9,2],[-4,-2,6,7,-5]],[[-10,-10,-5,-5,8],[-1,-2,-7,10,6]],[[1,-7,-6,8,6],[-8,2,-7,10,9]],[[1,-9,4,9,-3],[-6,-2,5,5,-1]],[[7,-7,7,5,3],[3,3,-6,-9,-9]],[[-9,-5,7,1,5],[4,1,-10,-3,-6]],[[-8,-2,-3,8,-5],[-4,-3,7,1,3]],[[-10,-8,6,9,-3],[-10,4,-4,2,8]],[[-2,-4,-1,4,-7],[-6,3,7,-1,1]],[[-9,-9,-2,-1,6],[4,10,-2,8,-3]],[[-2,-3,-2,-6,-7],[9,9,3,2,8]]], dtype = "uint16")#candidate|20081|(14, 2, 5)|const|uint16
bop_20082 = relay.greater_equal(var_20080.astype('bool'), relay.reshape(const_20081.astype('bool'), relay.shape_of(var_20080))) # shape=(14, 2, 5)
func_11358_call = mod.get_global_var('func_11358')
func_11362_call = mutated_mod.get_global_var('func_11362')
const_20086 = relay.const(-6, dtype = "uint32")#candidate|20086|()|const|uint32
var_20087 = relay.var("var_20087", dtype = "uint64", shape = (130,))#candidate|20087|(130,)|var|uint64
call_20085 = relay.TupleGetItem(func_11358_call(relay.reshape(const_20086.astype('uint32'), []), relay.reshape(var_20087.astype('uint64'), [130,]), ), 3)
call_20088 = relay.TupleGetItem(func_11362_call(relay.reshape(const_20086.astype('uint32'), []), relay.reshape(var_20087.astype('uint64'), [130,]), ), 3)
func_19487_call = mod.get_global_var('func_19487')
func_19491_call = mutated_mod.get_global_var('func_19491')
const_20100 = relay.const([[8],[10],[-1],[9],[1],[-7],[7],[9],[3],[10],[2],[-2],[2],[6],[-9],[-5],[6],[4],[6],[-7],[-7],[7],[-6],[-1],[2],[3],[-3],[-8],[10],[-10],[6],[-5],[-3],[-2],[-6],[-5],[-3],[-7],[1],[-10],[-9],[6],[5],[-6],[-9],[5],[4],[-10],[10],[-5],[2],[1],[4],[-6],[6],[-7],[-8],[-7],[-6],[9],[9],[-1],[-3],[9],[4],[2],[-8],[5],[9],[-7],[7],[9],[7],[-10],[9],[10],[-3],[-3],[3],[-10],[8],[5],[4],[-7],[1],[-7],[-10],[-8],[4],[-3],[7],[-5],[4],[7],[-1],[-6],[-10],[6],[3],[5],[9],[-4],[2],[-7],[-2],[-9],[4],[1],[1],[-7],[6],[3],[6],[-8],[-5],[5],[-8],[-5],[3],[-5],[2],[3],[-10],[-4],[-4],[-5],[-4],[-6],[8],[-9],[8],[-6],[-3],[7],[3],[-10],[-7],[-1],[-9],[10],[-5],[4],[3],[-2],[-6],[5],[5],[2],[-2],[-3],[-10],[2],[-5],[-6],[7],[10],[1],[3],[-5],[-5]], dtype = "uint64")#candidate|20100|(160, 1)|const|uint64
var_20101 = relay.var("var_20101", dtype = "float64", shape = (832,))#candidate|20101|(832,)|var|float64
const_20102 = relay.const([9.951909,-1.679648,-3.636339,6.295460,-3.136352,-1.354806,-9.632497,2.863045,7.356190,8.685491,1.195216,5.991849,-1.712998,4.199555,-1.219827,-5.204638,3.463821,0.736712,8.485285,8.634849,0.036572,1.945052,-6.469477,-6.830976,5.711192,-4.451315,7.511590,-1.985419,-6.217068,9.042730,9.191526,8.084584,9.965367,-2.741746,6.553234,-3.745132,2.426247,-6.452266,-3.070441,5.374486,9.257710,8.195615,8.749989,-9.268924,8.670215,8.164053,-1.504251,8.520602,5.739042,-5.646642,-3.606952,-2.348868,-4.694571,3.789398,8.955368,-3.958713,-9.969256,6.024195,8.086912,6.849820,-9.283274,5.584234,0.997669,-3.023449,-7.731180,8.744794,9.493819,-7.490711,2.599997,-5.968814,-7.460888,4.416518,-0.629758,2.515059,-2.505823,-7.167769,2.246046,0.279689,7.769410,0.694929,-3.094453,-5.976154,-4.096719,-6.056297,-2.089695,-8.816540,8.232975,2.384946,8.068910,-1.432684,8.326277,-5.917603,-4.120364,-3.019455,9.426707,-8.625279,-7.201024,0.078577,5.944661,-4.393132,-3.040822,3.092792,-7.447645,-4.354723,9.226715,-6.946057,1.214854,5.744045,-9.759781,4.519220,2.365464,-8.169808,-5.436167,9.772572,0.311367,8.609288,-5.494218,7.192886,9.458360,-6.946207,-0.747773,-7.650292,5.244200,-7.219687,8.602291,4.109216,4.181553,-5.847595,4.145976,6.407260,-4.411580,5.168837,4.711638,7.591012,-6.686775,8.230240,-0.267343,-0.961011,4.039238,-3.991835,7.766301,-6.919689,1.182056,-7.779595,-0.008452,4.471891,6.135989,8.206912,4.174622,1.604741,1.524468,4.594161,-1.715967,8.285943,-6.382391,-7.030546,-4.741508,-6.251280,-7.007591,-1.819111,-7.377271,5.340366,-3.702659,6.704778,9.511898,8.525923,1.992426,2.969469,7.681931,-0.505303,-1.654299,0.300438,4.172052,-3.144940,-9.771807,-1.782821,-1.272025,-2.951021,-0.886289,-2.599092,4.774751,-1.366229,-1.223225,-4.388022,1.432340,2.886831,-0.381970,-9.952397,-1.666457,1.787664,2.004255,-3.150227,7.411477,2.104382,-5.866592,4.698102,9.784110,-1.126707,0.159555,4.776127,9.485759,-7.672080,0.028646,0.192211,5.223383,8.975236,-5.288494,-9.262509,-8.371456,-5.467917,-6.829484,-8.806100,0.597052,7.910913,-8.456722,0.293663,-3.311344,6.380621,-0.878313,6.802554,0.405630,9.518396,-8.138317,5.825754,4.153536,6.306554,9.725718,5.234332,6.644971,-6.218644,-2.975570,5.991568,6.033131,-8.165024,-9.296749,-3.048544,-8.701659,4.308796,9.080706,-5.148547,-7.991322,-8.355269,0.214936,3.893985,0.381502,-9.921024,1.386313,-9.038576,-3.296149,3.460771,-9.384844,-9.904589,8.113881,-0.157418,-4.325450,6.577408,-9.518458,8.141190,2.182916,-0.629463,-3.243989,-0.507505,0.643351,-7.808082,-9.537398,-6.453123,5.056882,4.060496,-8.474042,-7.605440,-8.893045,-5.461017,0.519621,0.476055,-8.836925,6.355709,-1.202570,-7.308747,-1.011331,-2.898164,-2.444959,-0.323644,8.534497,-0.402117,7.001580,9.034885,-1.392752,-7.396521,9.460211,1.210906,-6.638072,-1.212039,-8.829655,-9.391466,7.554523,0.374147,9.327537,-7.095679,-4.430415,-6.697753,2.610987,3.274782,0.222624,7.775945,6.615274,-2.953320,-7.892516,5.004377,-2.595598,2.243215,-0.401718,2.106623,-0.458209,-1.343351,3.018560,-8.306557,-6.218750,-2.529796,-8.402732,-3.088394,-9.121968,7.627231,3.964405,-4.907348,-1.666682,-0.564306,-5.600170,-7.915863,4.670235,8.088978,6.176538,7.600993,-3.048606,-0.135378,8.220258,-3.990723,6.501159,-4.299092,-8.869546,-8.246637,1.687654,3.368046,9.002500,-9.351939,1.651510,8.515577,-8.648407,-3.106940,-9.212847,8.069051,-7.299202,-5.438422,0.776708,-0.792381,0.184584,-9.195674,5.619504,-5.203387,5.429027,9.068842,2.916354,0.782293,0.507268,-2.640594,-0.420808,-6.995840,5.675992,6.334244,8.115697,5.471611,-9.878220,2.412516,9.589288,-5.715783,4.155633,2.724353,-2.239117,-1.195115,4.294448,-4.515227,-6.597155,-9.389791,0.732321,-7.898149,1.971988,3.249725,0.461007,-4.165228,-8.451679,4.070681,-5.330749,-0.793686,6.792908,6.846396,7.059695,4.510500,-2.776391,-3.605120,9.529493,-0.062044,-8.448354,-2.469229,1.009068,-7.483527,-2.756782,1.681229,8.312468,0.543941,-8.717878,9.349497,-0.272614,2.565663,-6.674226,-8.748180,-4.728929,-3.662228,-5.845542,-7.878847,4.745785,-1.971961,-4.524539,3.890013,8.175801,-0.882223,9.648085,-6.624752,-9.065765,-8.675996,8.485824,-2.908635,0.704116,-3.492506,-8.922815,0.618246,3.655307,0.084847,8.998732,2.910516,7.355493,-4.891032,4.808050,1.478206,-9.595597,-2.793513,-6.548587,8.824754,-0.224302,-9.225820,-6.508026,-6.065510,4.955475,5.047448,-2.739277,5.871788,6.818984,-4.056002,-6.667104,-0.395153,4.958733,-7.940792,-4.329701,-1.592401,4.116756,7.757232,-8.343060,-5.548011,6.691202,7.192423,-6.533747,0.553893,-6.505991,0.477445,4.001549,-8.315226,-7.734874,6.475247,-3.022177,8.130004,-7.717543,-9.120949], dtype = "float64")#candidate|20102|(480,)|const|float64
call_20099 = relay.TupleGetItem(func_19487_call(relay.reshape(const_20100.astype('uint64'), [160,]), relay.reshape(var_20101.astype('float64'), [832,]), relay.reshape(const_20102.astype('float64'), [480,]), ), 6)
call_20103 = relay.TupleGetItem(func_19491_call(relay.reshape(const_20100.astype('uint64'), [160,]), relay.reshape(var_20101.astype('float64'), [832,]), relay.reshape(const_20102.astype('float64'), [480,]), ), 6)
func_15046_call = mod.get_global_var('func_15046')
func_15047_call = mutated_mod.get_global_var('func_15047')
call_20108 = relay.TupleGetItem(func_15046_call(), 0)
call_20109 = relay.TupleGetItem(func_15047_call(), 0)
func_11833_call = mod.get_global_var('func_11833')
func_11835_call = mutated_mod.get_global_var('func_11835')
call_20112 = relay.TupleGetItem(func_11833_call(), 0)
call_20113 = relay.TupleGetItem(func_11835_call(), 0)
output = relay.Tuple([bop_20082,call_20085,const_20086,var_20087,call_20099,const_20100,var_20101,const_20102,call_20108,call_20112,])
output2 = relay.Tuple([bop_20082,call_20088,const_20086,var_20087,call_20103,const_20100,var_20101,const_20102,call_20109,call_20113,])
func_20115 = relay.Function([var_20080,var_20087,var_20101,], output)
mod['func_20115'] = func_20115
mod = relay.transform.InferType()(mod)
var_20116 = relay.var("var_20116", dtype = "uint16", shape = (14, 2, 5))#candidate|20116|(14, 2, 5)|var|uint16
var_20117 = relay.var("var_20117", dtype = "uint64", shape = (130,))#candidate|20117|(130,)|var|uint64
var_20118 = relay.var("var_20118", dtype = "float64", shape = (832,))#candidate|20118|(832,)|var|float64
output = func_20115(var_20116,var_20117,var_20118,)
func_20119 = relay.Function([var_20116,var_20117,var_20118,], output)
mutated_mod['func_20119'] = func_20119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16705_call = mod.get_global_var('func_16705')
func_16707_call = mutated_mod.get_global_var('func_16707')
call_20269 = func_16705_call()
call_20270 = func_16705_call()
output = relay.Tuple([call_20269,])
output2 = relay.Tuple([call_20270,])
func_20303 = relay.Function([], output)
mod['func_20303'] = func_20303
mod = relay.transform.InferType()(mod)
mutated_mod['func_20303'] = func_20303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20303_call = mutated_mod.get_global_var('func_20303')
call_20304 = func_20303_call()
output = call_20304
func_20305 = relay.Function([], output)
mutated_mod['func_20305'] = func_20305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15647_call = mod.get_global_var('func_15647')
func_15649_call = mutated_mod.get_global_var('func_15649')
call_20384 = relay.TupleGetItem(func_15647_call(), 0)
call_20385 = relay.TupleGetItem(func_15649_call(), 0)
func_12065_call = mod.get_global_var('func_12065')
func_12067_call = mutated_mod.get_global_var('func_12067')
call_20389 = relay.TupleGetItem(func_12065_call(), 0)
call_20390 = relay.TupleGetItem(func_12067_call(), 0)
output = relay.Tuple([call_20384,call_20389,])
output2 = relay.Tuple([call_20385,call_20390,])
func_20391 = relay.Function([], output)
mod['func_20391'] = func_20391
mod = relay.transform.InferType()(mod)
output = func_20391()
func_20392 = relay.Function([], output)
mutated_mod['func_20392'] = func_20392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12987_call = mod.get_global_var('func_12987')
func_12988_call = mutated_mod.get_global_var('func_12988')
call_20422 = func_12987_call()
call_20423 = func_12987_call()
func_17953_call = mod.get_global_var('func_17953')
func_17956_call = mutated_mod.get_global_var('func_17956')
var_20425 = relay.var("var_20425", dtype = "float64", shape = (182,))#candidate|20425|(182,)|var|float64
call_20424 = relay.TupleGetItem(func_17953_call(relay.reshape(var_20425.astype('float64'), [182,])), 1)
call_20426 = relay.TupleGetItem(func_17956_call(relay.reshape(var_20425.astype('float64'), [182,])), 1)
func_6391_call = mod.get_global_var('func_6391')
func_6393_call = mutated_mod.get_global_var('func_6393')
var_20432 = relay.var("var_20432", dtype = "int16", shape = ())#candidate|20432|()|var|int16
call_20431 = relay.TupleGetItem(func_6391_call(relay.reshape(var_20432.astype('int16'), [])), 2)
call_20433 = relay.TupleGetItem(func_6393_call(relay.reshape(var_20432.astype('int16'), [])), 2)
output = relay.Tuple([call_20422,call_20424,var_20425,call_20431,var_20432,])
output2 = relay.Tuple([call_20423,call_20426,var_20425,call_20433,var_20432,])
func_20439 = relay.Function([var_20425,var_20432,], output)
mod['func_20439'] = func_20439
mod = relay.transform.InferType()(mod)
var_20440 = relay.var("var_20440", dtype = "float64", shape = (182,))#candidate|20440|(182,)|var|float64
var_20441 = relay.var("var_20441", dtype = "int16", shape = ())#candidate|20441|()|var|int16
output = func_20439(var_20440,var_20441,)
func_20442 = relay.Function([var_20440,var_20441,], output)
mutated_mod['func_20442'] = func_20442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14760_call = mod.get_global_var('func_14760')
func_14762_call = mutated_mod.get_global_var('func_14762')
call_20531 = relay.TupleGetItem(func_14760_call(), 0)
call_20532 = relay.TupleGetItem(func_14762_call(), 0)
output = call_20531
output2 = call_20532
func_20566 = relay.Function([], output)
mod['func_20566'] = func_20566
mod = relay.transform.InferType()(mod)
output = func_20566()
func_20567 = relay.Function([], output)
mutated_mod['func_20567'] = func_20567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12065_call = mod.get_global_var('func_12065')
func_12067_call = mutated_mod.get_global_var('func_12067')
call_20747 = relay.TupleGetItem(func_12065_call(), 0)
call_20748 = relay.TupleGetItem(func_12067_call(), 0)
output = call_20747
output2 = call_20748
func_20775 = relay.Function([], output)
mod['func_20775'] = func_20775
mod = relay.transform.InferType()(mod)
mutated_mod['func_20775'] = func_20775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20775_call = mutated_mod.get_global_var('func_20775')
call_20776 = func_20775_call()
output = call_20776
func_20777 = relay.Function([], output)
mutated_mod['func_20777'] = func_20777
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18736_call = mod.get_global_var('func_18736')
func_18738_call = mutated_mod.get_global_var('func_18738')
call_20858 = func_18736_call()
call_20859 = func_18736_call()
func_18119_call = mod.get_global_var('func_18119')
func_18121_call = mutated_mod.get_global_var('func_18121')
var_20861 = relay.var("var_20861", dtype = "float64", shape = (182,))#candidate|20861|(182,)|var|float64
call_20860 = relay.TupleGetItem(func_18119_call(relay.reshape(var_20861.astype('float64'), [182,])), 2)
call_20862 = relay.TupleGetItem(func_18121_call(relay.reshape(var_20861.astype('float64'), [182,])), 2)
func_12848_call = mod.get_global_var('func_12848')
func_12850_call = mutated_mod.get_global_var('func_12850')
call_20913 = func_12848_call()
call_20914 = func_12848_call()
output = relay.Tuple([call_20858,call_20860,var_20861,call_20913,])
output2 = relay.Tuple([call_20859,call_20862,var_20861,call_20914,])
func_20922 = relay.Function([var_20861,], output)
mod['func_20922'] = func_20922
mod = relay.transform.InferType()(mod)
var_20923 = relay.var("var_20923", dtype = "float64", shape = (182,))#candidate|20923|(182,)|var|float64
output = func_20922(var_20923)
func_20924 = relay.Function([var_20923], output)
mutated_mod['func_20924'] = func_20924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16705_call = mod.get_global_var('func_16705')
func_16707_call = mutated_mod.get_global_var('func_16707')
call_20980 = func_16705_call()
call_20981 = func_16705_call()
output = call_20980
output2 = call_20981
func_20992 = relay.Function([], output)
mod['func_20992'] = func_20992
mod = relay.transform.InferType()(mod)
output = func_20992()
func_20993 = relay.Function([], output)
mutated_mod['func_20993'] = func_20993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11979_call = mod.get_global_var('func_11979')
func_11980_call = mutated_mod.get_global_var('func_11980')
call_21063 = func_11979_call()
call_21064 = func_11979_call()
output = relay.Tuple([call_21063,])
output2 = relay.Tuple([call_21064,])
func_21070 = relay.Function([], output)
mod['func_21070'] = func_21070
mod = relay.transform.InferType()(mod)
output = func_21070()
func_21071 = relay.Function([], output)
mutated_mod['func_21071'] = func_21071
mutated_mod = relay.transform.InferType()(mutated_mod)
var_21094 = relay.var("var_21094", dtype = "uint32", shape = ())#candidate|21094|()|var|uint32
var_21095 = relay.var("var_21095", dtype = "uint32", shape = (3, 11, 16))#candidate|21095|(3, 11, 16)|var|uint32
bop_21096 = relay.bitwise_xor(var_21094.astype('uint32'), var_21095.astype('uint32')) # shape=(3, 11, 16)
output = bop_21096
output2 = bop_21096
func_21099 = relay.Function([var_21094,var_21095,], output)
mod['func_21099'] = func_21099
mod = relay.transform.InferType()(mod)
mutated_mod['func_21099'] = func_21099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21099_call = mutated_mod.get_global_var('func_21099')
var_21101 = relay.var("var_21101", dtype = "uint32", shape = ())#candidate|21101|()|var|uint32
var_21102 = relay.var("var_21102", dtype = "uint32", shape = (3, 11, 16))#candidate|21102|(3, 11, 16)|var|uint32
call_21100 = func_21099_call(var_21101,var_21102,)
output = call_21100
func_21103 = relay.Function([var_21101,var_21102,], output)
mutated_mod['func_21103'] = func_21103
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17788_call = mod.get_global_var('func_17788')
func_17789_call = mutated_mod.get_global_var('func_17789')
call_21136 = relay.TupleGetItem(func_17788_call(), 0)
call_21137 = relay.TupleGetItem(func_17789_call(), 0)
output = call_21136
output2 = call_21137
func_21141 = relay.Function([], output)
mod['func_21141'] = func_21141
mod = relay.transform.InferType()(mod)
output = func_21141()
func_21142 = relay.Function([], output)
mutated_mod['func_21142'] = func_21142
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19297_call = mod.get_global_var('func_19297')
func_19298_call = mutated_mod.get_global_var('func_19298')
call_21164 = relay.TupleGetItem(func_19297_call(), 0)
call_21165 = relay.TupleGetItem(func_19298_call(), 0)
output = call_21164
output2 = call_21165
func_21208 = relay.Function([], output)
mod['func_21208'] = func_21208
mod = relay.transform.InferType()(mod)
mutated_mod['func_21208'] = func_21208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21208_call = mutated_mod.get_global_var('func_21208')
call_21209 = func_21208_call()
output = call_21209
func_21210 = relay.Function([], output)
mutated_mod['func_21210'] = func_21210
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15065_call = mod.get_global_var('func_15065')
func_15066_call = mutated_mod.get_global_var('func_15066')
call_21228 = func_15065_call()
call_21229 = func_15065_call()
func_14839_call = mod.get_global_var('func_14839')
func_14843_call = mutated_mod.get_global_var('func_14843')
const_21249 = relay.const([-6.842447,-4.909809,-0.717275,2.963597,7.006176,-7.709710,2.743500,6.372137,-0.010395,8.673230,-3.780298,-2.200523,1.251785,-2.857135,-1.901767,9.964452,-2.365000,-7.575241,4.284340,-2.583065,7.849348,4.503553,-0.686264,-9.636577,6.337618,4.662155,-1.140507,7.270400,6.731693,8.312984], dtype = "float64")#candidate|21249|(30,)|const|float64
var_21250 = relay.var("var_21250", dtype = "float64", shape = (832,))#candidate|21250|(832,)|var|float64
var_21251 = relay.var("var_21251", dtype = "float64", shape = (480,))#candidate|21251|(480,)|var|float64
call_21248 = relay.TupleGetItem(func_14839_call(relay.reshape(const_21249.astype('float64'), [30,]), relay.reshape(var_21250.astype('float64'), [832,]), relay.reshape(var_21251.astype('float64'), [480,]), ), 1)
call_21252 = relay.TupleGetItem(func_14843_call(relay.reshape(const_21249.astype('float64'), [30,]), relay.reshape(var_21250.astype('float64'), [832,]), relay.reshape(var_21251.astype('float64'), [480,]), ), 1)
output = relay.Tuple([call_21228,call_21248,const_21249,var_21250,var_21251,])
output2 = relay.Tuple([call_21229,call_21252,const_21249,var_21250,var_21251,])
func_21260 = relay.Function([var_21250,var_21251,], output)
mod['func_21260'] = func_21260
mod = relay.transform.InferType()(mod)
var_21261 = relay.var("var_21261", dtype = "float64", shape = (832,))#candidate|21261|(832,)|var|float64
var_21262 = relay.var("var_21262", dtype = "float64", shape = (480,))#candidate|21262|(480,)|var|float64
output = func_21260(var_21261,var_21262,)
func_21263 = relay.Function([var_21261,var_21262,], output)
mutated_mod['func_21263'] = func_21263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11742_call = mod.get_global_var('func_11742')
func_11744_call = mutated_mod.get_global_var('func_11744')
call_21279 = func_11742_call()
call_21280 = func_11742_call()
output = relay.Tuple([call_21279,])
output2 = relay.Tuple([call_21280,])
func_21290 = relay.Function([], output)
mod['func_21290'] = func_21290
mod = relay.transform.InferType()(mod)
mutated_mod['func_21290'] = func_21290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21290_call = mutated_mod.get_global_var('func_21290')
call_21291 = func_21290_call()
output = call_21291
func_21292 = relay.Function([], output)
mutated_mod['func_21292'] = func_21292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16198_call = mod.get_global_var('func_16198')
func_16200_call = mutated_mod.get_global_var('func_16200')
call_21362 = relay.TupleGetItem(func_16198_call(), 0)
call_21363 = relay.TupleGetItem(func_16200_call(), 0)
func_17630_call = mod.get_global_var('func_17630')
func_17632_call = mutated_mod.get_global_var('func_17632')
call_21364 = relay.TupleGetItem(func_17630_call(), 0)
call_21365 = relay.TupleGetItem(func_17632_call(), 0)
func_15594_call = mod.get_global_var('func_15594')
func_15596_call = mutated_mod.get_global_var('func_15596')
call_21377 = func_15594_call()
call_21378 = func_15594_call()
func_15911_call = mod.get_global_var('func_15911')
func_15915_call = mutated_mod.get_global_var('func_15915')
var_21388 = relay.var("var_21388", dtype = "uint32", shape = ())#candidate|21388|()|var|uint32
const_21389 = relay.const([[7],[6],[1],[5],[-6],[-8],[6],[-1],[-7],[-1],[10],[-4],[8],[5],[-1],[10],[-3],[4],[-2],[5],[-9],[-6],[-4],[9]], dtype = "uint32")#candidate|21389|(24, 1)|const|uint32
var_21390 = relay.var("var_21390", dtype = "uint64", shape = (130, 1))#candidate|21390|(130, 1)|var|uint64
call_21387 = relay.TupleGetItem(func_15911_call(relay.reshape(var_21388.astype('uint32'), []), relay.reshape(const_21389.astype('uint32'), [24,]), relay.reshape(var_21390.astype('uint64'), [130,]), ), 4)
call_21391 = relay.TupleGetItem(func_15915_call(relay.reshape(var_21388.astype('uint32'), []), relay.reshape(const_21389.astype('uint32'), [24,]), relay.reshape(var_21390.astype('uint64'), [130,]), ), 4)
output = relay.Tuple([call_21362,call_21364,call_21377,call_21387,var_21388,const_21389,var_21390,])
output2 = relay.Tuple([call_21363,call_21365,call_21378,call_21391,var_21388,const_21389,var_21390,])
func_21394 = relay.Function([var_21388,var_21390,], output)
mod['func_21394'] = func_21394
mod = relay.transform.InferType()(mod)
mutated_mod['func_21394'] = func_21394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21394_call = mutated_mod.get_global_var('func_21394')
var_21396 = relay.var("var_21396", dtype = "uint32", shape = ())#candidate|21396|()|var|uint32
var_21397 = relay.var("var_21397", dtype = "uint64", shape = (130, 1))#candidate|21397|(130, 1)|var|uint64
call_21395 = func_21394_call(var_21396,var_21397,)
output = call_21395
func_21398 = relay.Function([var_21396,var_21397,], output)
mutated_mod['func_21398'] = func_21398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11305_call = mod.get_global_var('func_11305')
func_11307_call = mutated_mod.get_global_var('func_11307')
call_21471 = func_11305_call()
call_21472 = func_11305_call()
func_18736_call = mod.get_global_var('func_18736')
func_18738_call = mutated_mod.get_global_var('func_18738')
call_21492 = func_18736_call()
call_21493 = func_18736_call()
func_18659_call = mod.get_global_var('func_18659')
func_18660_call = mutated_mod.get_global_var('func_18660')
call_21497 = relay.TupleGetItem(func_18659_call(), 0)
call_21498 = relay.TupleGetItem(func_18660_call(), 0)
output = relay.Tuple([call_21471,call_21492,call_21497,])
output2 = relay.Tuple([call_21472,call_21493,call_21498,])
func_21502 = relay.Function([], output)
mod['func_21502'] = func_21502
mod = relay.transform.InferType()(mod)
mutated_mod['func_21502'] = func_21502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21502_call = mutated_mod.get_global_var('func_21502')
call_21503 = func_21502_call()
output = call_21503
func_21504 = relay.Function([], output)
mutated_mod['func_21504'] = func_21504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12065_call = mod.get_global_var('func_12065')
func_12067_call = mutated_mod.get_global_var('func_12067')
call_21546 = relay.TupleGetItem(func_12065_call(), 0)
call_21547 = relay.TupleGetItem(func_12067_call(), 0)
func_4987_call = mod.get_global_var('func_4987')
func_4992_call = mutated_mod.get_global_var('func_4992')
const_21572 = relay.const(True, dtype = "bool")#candidate|21572|()|const|bool
var_21573 = relay.var("var_21573", dtype = "float64", shape = (480,))#candidate|21573|(480,)|var|float64
var_21574 = relay.var("var_21574", dtype = "float64", shape = (1008,))#candidate|21574|(1008,)|var|float64
call_21571 = relay.TupleGetItem(func_4987_call(relay.reshape(const_21572.astype('bool'), []), relay.reshape(var_21573.astype('float64'), [480,]), relay.reshape(var_21574.astype('float64'), [1008,]), ), 0)
call_21575 = relay.TupleGetItem(func_4992_call(relay.reshape(const_21572.astype('bool'), []), relay.reshape(var_21573.astype('float64'), [480,]), relay.reshape(var_21574.astype('float64'), [1008,]), ), 0)
output = relay.Tuple([call_21546,call_21571,const_21572,var_21573,var_21574,])
output2 = relay.Tuple([call_21547,call_21575,const_21572,var_21573,var_21574,])
func_21589 = relay.Function([var_21573,var_21574,], output)
mod['func_21589'] = func_21589
mod = relay.transform.InferType()(mod)
mutated_mod['func_21589'] = func_21589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21589_call = mutated_mod.get_global_var('func_21589')
var_21591 = relay.var("var_21591", dtype = "float64", shape = (480,))#candidate|21591|(480,)|var|float64
var_21592 = relay.var("var_21592", dtype = "float64", shape = (1008,))#candidate|21592|(1008,)|var|float64
call_21590 = func_21589_call(var_21591,var_21592,)
output = call_21590
func_21593 = relay.Function([var_21591,var_21592,], output)
mutated_mod['func_21593'] = func_21593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18736_call = mod.get_global_var('func_18736')
func_18738_call = mutated_mod.get_global_var('func_18738')
call_21595 = func_18736_call()
call_21596 = func_18736_call()
func_13432_call = mod.get_global_var('func_13432')
func_13434_call = mutated_mod.get_global_var('func_13434')
call_21599 = relay.TupleGetItem(func_13432_call(), 1)
call_21600 = relay.TupleGetItem(func_13434_call(), 1)
output = relay.Tuple([call_21595,call_21599,])
output2 = relay.Tuple([call_21596,call_21600,])
func_21648 = relay.Function([], output)
mod['func_21648'] = func_21648
mod = relay.transform.InferType()(mod)
output = func_21648()
func_21649 = relay.Function([], output)
mutated_mod['func_21649'] = func_21649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20303_call = mod.get_global_var('func_20303')
func_20305_call = mutated_mod.get_global_var('func_20305')
call_21663 = relay.TupleGetItem(func_20303_call(), 0)
call_21664 = relay.TupleGetItem(func_20305_call(), 0)
func_14196_call = mod.get_global_var('func_14196')
func_14198_call = mutated_mod.get_global_var('func_14198')
const_21670 = relay.const([[-7.355126,-5.454520,9.289843,6.700617,-6.534690,-4.887576,-8.680281,-7.032221,0.202361,2.992242,8.045570,2.853627,6.296328,8.429722,-1.758678,1.348935,-2.413877,1.702307,2.737363,6.870136,7.555886,5.601478,-8.475346,5.402362,5.862954,4.311251,-7.513505,6.276687,-5.134184,-4.903374,4.899737,3.399834,5.848310,3.180896,7.554458,-0.594282,-9.489410,-5.453925,8.490140,-1.360084,7.995594,3.303401,6.433392,0.068671,-0.332445,-8.979072,2.675097,6.012124,-6.177512,-2.339731,-9.626592,-9.650049,-9.919248,7.081724,-6.096159,-0.902828,4.473012,-0.718513,6.329825,-0.702507,8.453379,6.057024,-6.275654,4.514830,-9.326226,-3.262154,-7.868448,4.335501,-1.543107,-4.431965,3.506788,-4.262472,0.726987,5.113458,-7.739924,-4.704684,-2.712789,4.931355,-9.313715,-1.916183,-6.994083,2.329442,4.804864,5.309120,2.229686,5.560638,-6.450931,-7.708888,-9.192804,-1.622516,0.085252,-1.434081,9.735238,8.381590,-5.937907,-4.414513,-1.685604,0.841599,-3.209368,2.491175,-6.222618,-0.837475,-0.716713,-3.351365,-1.242255,-4.564583,2.628821,-2.803664,-4.548207,2.096825,9.774962,5.529232,0.667824,6.973812,7.574144,-1.894845,1.145879,-8.438391,0.177491,-4.203705,-8.591296,5.133389,5.235412,-0.343451,9.728406,-4.499547,5.522682,3.706389,-6.295243,-7.022188,7.685883,-5.257292,-1.717584,4.375434,6.888830,2.708333,-9.794732,-7.970715,-9.545894,1.170933,-7.443815,-2.408708,9.523873,-4.175662,3.910417,1.820296,7.042390,5.654106,-2.496699,0.998978,8.967265,4.825028,-8.994970,6.593678,-9.720912,-7.008198,5.959453,-5.990938,-0.205460,-2.456328,-2.959039,2.879839,0.448234,4.070601,4.708607,-8.407240,8.431601,-0.855138,1.177217,8.286156,-2.687836,-3.928761,-9.740358,-7.289808,2.762911,-9.700116,-5.504545,-0.389893,8.779315,6.714534,-6.443931,2.481701,-8.563680,9.613507,1.515048,6.396008,7.126985,4.258253,8.784240,-8.199669,4.567698,-9.524699,-9.848536,2.262603,-8.450303,-9.614010,-2.229301,-2.768159,5.277709,-8.389979,-7.285543,-7.054066,5.189402,-5.642735,9.625102,-2.447140,7.702314,-1.111992,6.817374,0.331595,5.088551,-2.886038,2.682168,-6.899952,8.329690,-3.283196,-8.694573,7.064732,-8.554786,-8.049553,-9.630287,-4.703026,0.218300,-1.546867,6.765701,-6.061832,4.155883,-0.139988,-5.878621,-6.764751,-6.554554,9.892878,0.233659,-7.840474,-3.488288,-8.959265,5.306065,3.512003,5.166808,6.242918,6.644840,6.990593,6.287605,-1.974563,-6.740850,8.573132,0.977455,-6.709237,5.535529,-1.517085,0.961169,-4.195486,-0.143972,-7.096934,7.902440,-0.537156,4.335484,-7.735104,9.701067,-0.181976,3.267930,-4.208692,4.917065,9.709054,-0.973765,-0.255903,-0.605857,-4.203120,-8.526866,3.006205,8.806712,3.347068,8.944622,1.771125,-2.666770,8.152969,1.441095,-5.963902,-3.686072,4.682502,5.265936,-7.280963,-3.139437,-8.182437,8.567252,8.268461,9.864190,-4.121223,-2.274102,-9.151737,6.363028,-1.951838,5.160574,6.664947,-0.124738,-0.105743,7.980625,-4.946550,-5.047789,-5.810714,-6.961582,-4.625801,-7.391800,-9.395320,-9.120152,9.432292,-3.353490,-2.070030,-8.663011,9.269466,-0.824247,5.602666,0.809079,0.560806,-3.703910,3.135916,1.651634,4.273481,-3.546560,-9.270685,-5.768181,7.093421,9.663452,-7.580333,8.789271,4.900886,-5.342354,9.757549,-6.378384,7.201526,4.657030,8.709526,-3.180321,-6.869115,-3.075819,4.887548,4.361537,-3.819220,-9.695651,-4.532640,-5.595074,1.335609,-4.223828,-3.277268,6.762396,-6.925791,5.777270,-2.083894,-2.738631,-2.827621,9.425296,2.256005,-7.454043,-9.828827,-2.590074,8.954905,-8.645168,6.061612,4.354533,7.473271,8.242835,9.867459,7.615169,-0.793160,1.141890,-6.774239,-2.891081,7.721754,6.636460,1.132196,-1.408063,8.458250,3.205550,-1.611529,-0.644509,-7.182597,6.174316,-5.241990,1.683056,-2.223795,-1.456792,4.440729,-6.029537,9.926607,-7.414621,5.043131,0.353025,1.063366,-6.923043,-9.140214,7.363932,-7.096493,-9.387835,1.849831,-8.008520,-6.153418,2.158883,4.888794,-2.560993,2.677246,-2.656794,-0.482233,1.517854,-1.572483,3.709976,4.399755,5.301921,6.735312,-7.495750,8.436974,-9.115488,5.874908,-1.618086,5.672343,-0.990380,0.233937,2.745955,-5.822105,-0.978967,-1.032397,7.265022,-8.576800,-6.576071,7.439828,2.974484,6.486642,-9.779649,9.910366,3.632046,-2.435360,7.470233,-2.654613,7.001718,-2.928177,-9.914555,1.195887,-0.297435,-8.135485,8.210547,4.350325,8.838557,-1.115200,-0.261039,-1.951739,-6.139780,4.424650,-1.248144,-5.516468,-1.404695,2.421951,-2.532074,9.642598,7.818969,1.787292,7.991739,3.110809,9.693093,-2.694930,0.988217,9.636087,0.619562,9.339143,6.822332,2.064845,-9.749217,-5.821033,8.212630,5.150512,8.828597,5.260818,-1.163878,1.645485,-4.431279,9.260707,-2.142968,0.625996,8.555838,-1.031287,2.239523,-1.789109]], dtype = "float64")#candidate|21670|(1, 480)|const|float64
call_21669 = relay.TupleGetItem(func_14196_call(relay.reshape(const_21670.astype('float64'), [480,])), 2)
call_21671 = relay.TupleGetItem(func_14198_call(relay.reshape(const_21670.astype('float64'), [480,])), 2)
func_7918_call = mod.get_global_var('func_7918')
func_7922_call = mutated_mod.get_global_var('func_7922')
const_21685 = relay.const([-1.650902,-4.535757,0.201604,-1.877293,2.782678,4.857934,5.696861,3.195398,2.116166,0.158262,2.096319,-6.939532,4.515521,3.407060,-9.511230,-8.107122,-0.590621,-9.493901,-0.711914,-7.715826,7.441297,6.305560,9.386448,-9.163834,9.182874,-6.177723,-1.415690,6.065532,-3.755904,3.674949,1.277217,-4.890692,-4.400139,0.672741,7.273964,-3.294641,7.596224,9.268779,1.721915,0.824434,-6.082903,5.243757,-9.551472,-8.255083,9.552404,7.103414,7.796106,-8.552343,0.957223,-1.526731,3.797625,5.732086,-3.311205,9.628254,1.764971,-9.306300,6.593956,-8.048968,0.712939,-7.079910,-0.898311,6.400195,6.557738,6.789709,4.923242,8.488995,4.797307,0.419525,-3.185487,4.292772,1.401100,0.873649,9.354941,-3.011403,-3.657470,4.124240,3.828797,5.150399,-8.805787,0.523177,-4.623614,-6.355865,3.850999,-1.496694,-0.596318,3.394151,0.040244,-6.530843,4.295161,8.538906,-7.787441,-2.151847,3.857254,-8.794465,2.711071,5.150883,6.606364,3.245599,0.908857,-6.417586,6.579026,4.722001,-1.282088,2.362853,4.893936,2.560088,5.500077,6.349932,0.280767,-0.557478,3.073748,2.802866,1.556552,1.963682,-9.221400,-8.723522,-9.754768,-0.296956,-0.108176,-2.215191,8.639582,0.845908,1.999582,2.690391,-8.674062,0.497837,-1.447733,-8.556119,0.552220,-4.096294,5.115428,5.342851,0.033632,-3.036537,6.838108,6.202112,9.965509,6.673142,3.079731,8.516997,-0.397820,5.323498,5.288120,-7.369174,1.653282,-4.382007,-4.733364,-2.071342,-0.094502,5.117922,8.404078,-6.935624,1.278354,-5.132564,-6.449695,-2.854522,-7.446016,5.936218,-4.758333,0.525027,8.594392,-6.496994,1.298316,9.735019,-4.224321,-5.088677,1.845346,-9.383923,-7.100885,3.781852,-2.621937,-0.364941,3.005303,7.069356,3.703583,2.657246,-4.735293,-5.924245,6.094758,5.926956,-9.009366,1.689219,-6.694235,-2.657031,-1.637699,-2.010152,-9.975787,-5.095497,-8.984713,1.956532,-0.703622,-1.410783,-0.718307,-7.018299,-5.717782,6.750120,6.976207,-0.420583,-5.082173,4.335494,-9.212019,-6.514520,-3.490270,-0.898328,-0.470651,-0.734810,8.657636,5.306846,-1.348455,7.786613,-5.284681,3.419186,0.775326,1.828305,4.656150,1.973125,-7.472784,-6.735056,-9.664189,-1.129721,-0.877304,7.252538,5.015406,8.870480,-6.883301,6.175012,-6.309818,9.948532,-1.248165,1.430768,5.193501,-8.901877,-9.486464,-2.430583,7.453313,6.082953,5.409805,5.222466,-5.141572,-9.302551,0.346322,2.561029,1.369113,-6.318559,3.429671,5.191617,-1.212231,9.100463,-4.283352,5.020235,-0.638431,5.412597,2.363788,-3.502671,5.111650,-3.177563,-0.522375,-6.807390,-3.085083,-3.888283,7.236676,-7.121775,3.393697,-7.026782,7.493568,5.308216,5.265652,-4.040681,-0.715450,-0.983635,6.953345,-3.312777,-3.361433,6.629526,5.531756,-4.002127,1.449120,-1.657822,-5.902222,-1.239210,-5.226484,8.540692,-0.378292,-1.717498,2.976802,8.999093,-3.530880,-8.553546,-9.506550,8.067251,6.644215,-6.150868,1.124938,1.226749,-1.112261,7.781391,-5.874734,-9.610217,-4.137594,6.206256,9.064520,5.181363,-2.580032,-9.208486,8.229189,8.734144,5.842944,-3.533516,-5.027263,2.602372,5.739022,-9.150928,4.577476,4.779343,1.599145,8.760016,2.087704,-9.630661,2.512903,-5.687103,2.187525,9.211717,-4.069644,5.140878,-6.244802,0.828412,5.193763,1.055123,-8.040567,8.677608,8.401730,-9.990357,0.990026,-7.251982,7.991014,2.149498,-3.980470,3.415004,-7.870264,-7.368493,2.674520,4.388944,8.718044,-0.116550,7.001925,7.987859,-8.049594,9.058423,9.297005,-8.372392,-2.023533,4.164447,7.242908,5.169892,7.156986,-6.220163,6.057284,3.198171,-5.058454,-2.641619], dtype = "float32")#candidate|21685|(360,)|const|float32
call_21684 = relay.TupleGetItem(func_7918_call(relay.reshape(const_21685.astype('float32'), [12, 2, 15]), relay.reshape(const_21685.astype('float32'), [12, 2, 15]), ), 0)
call_21686 = relay.TupleGetItem(func_7922_call(relay.reshape(const_21685.astype('float32'), [12, 2, 15]), relay.reshape(const_21685.astype('float32'), [12, 2, 15]), ), 0)
output = relay.Tuple([call_21663,call_21669,const_21670,call_21684,const_21685,])
output2 = relay.Tuple([call_21664,call_21671,const_21670,call_21686,const_21685,])
func_21687 = relay.Function([], output)
mod['func_21687'] = func_21687
mod = relay.transform.InferType()(mod)
mutated_mod['func_21687'] = func_21687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21687_call = mutated_mod.get_global_var('func_21687')
call_21688 = func_21687_call()
output = call_21688
func_21689 = relay.Function([], output)
mutated_mod['func_21689'] = func_21689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14426_call = mod.get_global_var('func_14426')
func_14427_call = mutated_mod.get_global_var('func_14427')
call_21718 = func_14426_call()
call_21719 = func_14426_call()
func_1409_call = mod.get_global_var('func_1409')
func_1413_call = mutated_mod.get_global_var('func_1413')
const_21723 = relay.const([-8,-3,8,7,-10,3,8,-10,6,8,-9,5,-4,-9,5,8,-6,2,-2,-2,-5,2,4,-4,9,-8,3,-8,-6,1,-4,-5,-3,4,3,10], dtype = "int64")#candidate|21723|(36,)|const|int64
var_21724 = relay.var("var_21724", dtype = "float64", shape = (832,))#candidate|21724|(832,)|var|float64
call_21722 = relay.TupleGetItem(func_1409_call(relay.reshape(const_21723.astype('int64'), [6, 6, 1]), relay.reshape(var_21724.astype('float64'), [832,]), ), 2)
call_21725 = relay.TupleGetItem(func_1413_call(relay.reshape(const_21723.astype('int64'), [6, 6, 1]), relay.reshape(var_21724.astype('float64'), [832,]), ), 2)
func_17742_call = mod.get_global_var('func_17742')
func_17745_call = mutated_mod.get_global_var('func_17745')
var_21736 = relay.var("var_21736", dtype = "int16", shape = (200,))#candidate|21736|(200,)|var|int16
call_21735 = relay.TupleGetItem(func_17742_call(relay.reshape(var_21736.astype('int16'), [10, 4, 5]), relay.reshape(var_21736.astype('int16'), [10, 4, 5]), ), 0)
call_21737 = relay.TupleGetItem(func_17745_call(relay.reshape(var_21736.astype('int16'), [10, 4, 5]), relay.reshape(var_21736.astype('int16'), [10, 4, 5]), ), 0)
func_11833_call = mod.get_global_var('func_11833')
func_11835_call = mutated_mod.get_global_var('func_11835')
call_21740 = relay.TupleGetItem(func_11833_call(), 0)
call_21741 = relay.TupleGetItem(func_11835_call(), 0)
output = relay.Tuple([call_21718,call_21722,const_21723,var_21724,call_21735,var_21736,call_21740,])
output2 = relay.Tuple([call_21719,call_21725,const_21723,var_21724,call_21737,var_21736,call_21741,])
func_21747 = relay.Function([var_21724,var_21736,], output)
mod['func_21747'] = func_21747
mod = relay.transform.InferType()(mod)
mutated_mod['func_21747'] = func_21747
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21747_call = mutated_mod.get_global_var('func_21747')
var_21749 = relay.var("var_21749", dtype = "float64", shape = (832,))#candidate|21749|(832,)|var|float64
var_21750 = relay.var("var_21750", dtype = "int16", shape = (200,))#candidate|21750|(200,)|var|int16
call_21748 = func_21747_call(var_21749,var_21750,)
output = call_21748
func_21751 = relay.Function([var_21749,var_21750,], output)
mutated_mod['func_21751'] = func_21751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20992_call = mod.get_global_var('func_20992')
func_20993_call = mutated_mod.get_global_var('func_20993')
call_21771 = func_20992_call()
call_21772 = func_20992_call()
func_15458_call = mod.get_global_var('func_15458')
func_15462_call = mutated_mod.get_global_var('func_15462')
var_21777 = relay.var("var_21777", dtype = "float64", shape = (264, 1))#candidate|21777|(264, 1)|var|float64
var_21778 = relay.var("var_21778", dtype = "float32", shape = (750,))#candidate|21778|(750,)|var|float32
call_21776 = relay.TupleGetItem(func_15458_call(relay.reshape(var_21777.astype('float64'), [264,]), relay.reshape(var_21778.astype('float32'), [750,]), ), 3)
call_21779 = relay.TupleGetItem(func_15462_call(relay.reshape(var_21777.astype('float64'), [264,]), relay.reshape(var_21778.astype('float32'), [750,]), ), 3)
uop_21781 = relay.atan(var_21777.astype('float64')) # shape=(264, 1)
const_21792 = relay.const([[9.046354],[-1.396773],[-1.571124],[1.143572],[5.142129],[6.306830],[-1.455583],[-0.204061],[-0.635213],[5.540380],[0.558957],[-8.225996],[-8.954416],[-0.191147],[0.383276],[4.317913],[-3.900298],[0.096136],[-1.374036],[-7.348523],[-5.125959],[6.692587],[2.840396],[-2.832443],[-2.973130],[-3.435228],[-0.689612],[-9.234891],[-6.724057],[-2.892924],[-5.554749],[-6.454183],[3.610668],[-9.489788],[-2.450856],[7.499141],[-1.070746],[8.718673],[-8.195645],[7.343278],[8.351381],[-0.546601],[-2.012756],[-4.531374],[-5.865521],[-4.428674],[-5.175072],[1.632350],[-6.141521],[1.902227],[-7.588862],[-3.641830],[4.668364],[-5.688618],[7.442883],[5.558705],[9.010476],[-3.925804],[-9.302435],[-6.868084],[5.387471],[9.984145],[8.945602],[8.056438],[-5.885349],[-3.750531],[-1.586901],[-9.762062],[-7.606643],[2.687356],[-9.835583],[-1.111884],[4.523934],[-8.561714],[5.221125],[-1.883493],[8.379478],[-9.248766],[-9.880151],[3.177460],[-9.000159],[6.221087],[-3.377920],[5.639456],[-3.338135],[-9.974005],[8.405308],[-1.126055],[-1.652509],[-4.186172],[2.656027],[-3.908135],[-6.218479],[4.214501],[2.688091],[-1.739259],[-7.043748],[-1.376421],[6.472582],[7.806685],[-7.200452],[-1.718323],[-3.787811],[-7.046439],[0.982898],[-2.675290],[9.639178],[-5.210688],[0.776261],[-8.120719],[-6.898073],[-3.034362],[-3.643742],[9.028308],[-1.344386],[6.008294],[-4.565260],[-8.922974],[-3.483311],[3.796344],[8.834448],[-5.742881],[9.527810],[4.792027],[-4.044742],[2.277979],[-1.398616],[3.387969],[-7.025031],[-2.213749],[6.035288],[9.275398],[7.874128],[-6.644120],[4.558251],[-4.271680],[9.558830],[8.391698],[4.230777],[5.042083],[2.214251],[-8.680606],[4.782214],[-0.989316],[-0.680376],[-7.028581],[7.433289],[7.210617],[-8.384955],[-5.282943],[-6.842452],[-1.934578],[-7.368165],[-5.237863],[-3.388980],[5.356293],[-5.642642],[8.441086],[-1.003594],[7.365822],[-8.696084],[-7.567707],[3.128791],[8.486008],[-2.800483],[4.952088],[-0.922392],[-4.165218],[-6.752220],[-5.776396],[8.842483],[-5.667452],[1.333159],[5.817659],[8.444328],[-0.070867],[-5.950170],[9.672221],[-6.798665],[7.274226],[8.686688],[5.686448],[3.018103],[-9.880379],[-1.827588],[-5.060068],[-5.609210],[5.078786],[4.264794],[3.215714],[3.332590],[-2.453895],[5.365108],[-9.142569],[-0.353195],[-7.252738],[-7.092348],[8.279692],[3.206392],[1.234574],[-6.715367],[4.480178],[-3.238702],[-3.504201],[9.752508],[2.382262],[0.293386],[8.982713],[9.701484],[2.417201],[4.846182],[7.752250],[6.403838],[1.052855],[-0.386167],[5.007960],[3.763074],[-7.209345],[0.800926],[0.511334],[-3.048183],[-3.269873],[-5.194677],[-7.518597],[6.334880],[-9.410461],[8.767731],[-4.521008],[-0.578653],[-6.879867],[8.106970],[-5.934732],[-6.171788],[-4.174309],[4.431750],[6.659481],[-0.321834],[-2.205360],[0.159951],[1.145465],[-9.741982],[0.506287],[6.265231],[-7.291317],[-4.325300],[6.246233],[-2.209847],[-2.350608],[-7.825263],[7.376832],[-4.349079],[5.190186],[-9.688095],[2.598045],[7.312272],[-0.437653],[-2.563137],[7.140651],[0.311641],[-7.499440],[-9.847469],[4.175452],[8.977716],[-9.687134]], dtype = "float64")#candidate|21792|(264, 1)|const|float64
bop_21793 = relay.logical_xor(uop_21781.astype('uint32'), relay.reshape(const_21792.astype('uint32'), relay.shape_of(uop_21781))) # shape=(264, 1)
output = relay.Tuple([call_21771,call_21776,var_21778,bop_21793,])
output2 = relay.Tuple([call_21772,call_21779,var_21778,bop_21793,])
func_21796 = relay.Function([var_21777,var_21778,], output)
mod['func_21796'] = func_21796
mod = relay.transform.InferType()(mod)
var_21797 = relay.var("var_21797", dtype = "float64", shape = (264, 1))#candidate|21797|(264, 1)|var|float64
var_21798 = relay.var("var_21798", dtype = "float32", shape = (750,))#candidate|21798|(750,)|var|float32
output = func_21796(var_21797,var_21798,)
func_21799 = relay.Function([var_21797,var_21798,], output)
mutated_mod['func_21799'] = func_21799
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18887_call = mod.get_global_var('func_18887')
func_18889_call = mutated_mod.get_global_var('func_18889')
call_21832 = relay.TupleGetItem(func_18887_call(), 0)
call_21833 = relay.TupleGetItem(func_18889_call(), 0)
func_19894_call = mod.get_global_var('func_19894')
func_19895_call = mutated_mod.get_global_var('func_19895')
call_21834 = relay.TupleGetItem(func_19894_call(), 1)
call_21835 = relay.TupleGetItem(func_19895_call(), 1)
output = relay.Tuple([call_21832,call_21834,])
output2 = relay.Tuple([call_21833,call_21835,])
func_21842 = relay.Function([], output)
mod['func_21842'] = func_21842
mod = relay.transform.InferType()(mod)
output = func_21842()
func_21843 = relay.Function([], output)
mutated_mod['func_21843'] = func_21843
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18037_call = mod.get_global_var('func_18037')
func_18039_call = mutated_mod.get_global_var('func_18039')
call_21907 = relay.TupleGetItem(func_18037_call(), 0)
call_21908 = relay.TupleGetItem(func_18039_call(), 0)
func_1211_call = mod.get_global_var('func_1211')
func_1214_call = mutated_mod.get_global_var('func_1214')
var_21910 = relay.var("var_21910", dtype = "float32", shape = (396,))#candidate|21910|(396,)|var|float32
call_21909 = relay.TupleGetItem(func_1211_call(relay.reshape(var_21910.astype('float32'), [9, 11, 4])), 0)
call_21911 = relay.TupleGetItem(func_1214_call(relay.reshape(var_21910.astype('float32'), [9, 11, 4])), 0)
uop_21917 = relay.log10(call_21909.astype('float32')) # shape=(9, 11, 4)
uop_21919 = relay.log10(call_21911.astype('float32')) # shape=(9, 11, 4)
output = relay.Tuple([call_21907,var_21910,uop_21917,])
output2 = relay.Tuple([call_21908,var_21910,uop_21919,])
func_21923 = relay.Function([var_21910,], output)
mod['func_21923'] = func_21923
mod = relay.transform.InferType()(mod)
mutated_mod['func_21923'] = func_21923
mutated_mod = relay.transform.InferType()(mutated_mod)
var_21924 = relay.var("var_21924", dtype = "float32", shape = (396,))#candidate|21924|(396,)|var|float32
func_21923_call = mutated_mod.get_global_var('func_21923')
call_21925 = func_21923_call(var_21924)
output = call_21925
func_21926 = relay.Function([var_21924], output)
mutated_mod['func_21926'] = func_21926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15721_call = mod.get_global_var('func_15721')
func_15722_call = mutated_mod.get_global_var('func_15722')
call_21991 = relay.TupleGetItem(func_15721_call(), 1)
call_21992 = relay.TupleGetItem(func_15722_call(), 1)
func_14879_call = mod.get_global_var('func_14879')
func_14882_call = mutated_mod.get_global_var('func_14882')
var_22015 = relay.var("var_22015", dtype = "float32", shape = (336,))#candidate|22015|(336,)|var|float32
call_22014 = relay.TupleGetItem(func_14879_call(relay.reshape(var_22015.astype('float32'), [336,])), 2)
call_22016 = relay.TupleGetItem(func_14882_call(relay.reshape(var_22015.astype('float32'), [336,])), 2)
output = relay.Tuple([call_21991,call_22014,var_22015,])
output2 = relay.Tuple([call_21992,call_22016,var_22015,])
func_22020 = relay.Function([var_22015,], output)
mod['func_22020'] = func_22020
mod = relay.transform.InferType()(mod)
mutated_mod['func_22020'] = func_22020
mutated_mod = relay.transform.InferType()(mutated_mod)
var_22021 = relay.var("var_22021", dtype = "float32", shape = (336,))#candidate|22021|(336,)|var|float32
func_22020_call = mutated_mod.get_global_var('func_22020')
call_22022 = func_22020_call(var_22021)
output = call_22022
func_22023 = relay.Function([var_22021], output)
mutated_mod['func_22023'] = func_22023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16523_call = mod.get_global_var('func_16523')
func_16525_call = mutated_mod.get_global_var('func_16525')
call_22114 = relay.TupleGetItem(func_16523_call(), 0)
call_22115 = relay.TupleGetItem(func_16525_call(), 0)
func_3611_call = mod.get_global_var('func_3611')
func_3617_call = mutated_mod.get_global_var('func_3617')
const_22123 = relay.const([9.787966,-3.289811,-7.012690,4.587714,4.570418,9.002116,-3.213791,-3.328130,4.166034,-3.498476,9.037250,3.769679,-4.652337,6.315501,-5.066819,2.905732,6.080449,-3.503464,6.775446,1.162173,-8.616350,-3.020141,6.994062,1.602776,-8.226356,4.269155,-5.185595,3.589699,0.668626,-6.686561,1.358824,8.144183,0.819148,-2.505070,-3.473831,-1.088231,2.569277,2.857574,1.293248,5.626003,-1.121661,1.893623,-9.410083,7.970640,0.637621,4.799823,9.267188,3.202478,-9.310573,0.046742,6.296241,-5.306509,2.046617,1.251150,-1.547661,-1.477964,1.236311,8.915568,-0.313784,-2.711070,3.838422,4.935127,-6.964078,1.888964,-9.424140,7.390472,-4.804656,-1.294111,-0.897240,-2.643294,8.374468,3.170093,-8.926919,-1.220232,-7.897992,-2.336104,-9.167761,-2.711300,-5.198333,0.419940,6.252069,-6.554384,-5.076667,3.913684,1.856670,-8.303218,-0.781133,9.015269,-8.947906,3.610639,-7.175727,-8.953355,5.277976,-3.995190,2.419718,6.431570,-1.501302,-0.381793,-2.601170,4.586400,-8.578969,-3.568993,-2.629325,0.297893,8.725810,8.125863,6.027322,-8.370607,-2.928857,-0.234706,8.302994,-8.273626,-7.057752,-3.149545,-4.044362,-9.322711,5.398098,2.827423,-4.034348,8.981964,-1.168161,-9.527702,-4.240136,-4.376437,4.024273,-4.629306,-9.802709,-6.830828,-5.086221,-8.691718,3.450091,4.542484,9.694642,-9.346081,0.504717,-3.712945,-6.116560,6.472727,7.221594,9.262081,0.349845,4.687708,4.726786,-6.690712,4.421614,-9.377161,1.812531,3.144048,5.401982,-2.801156,8.958775,-0.296933,2.930420,5.455406,9.662521,3.097628,-1.239313,8.502642,3.159619,0.641218,-7.721475,2.501198,2.317156,-9.563499,-6.202295,-4.443896,7.892081,6.129235,-5.871465,-0.700750,9.165301,-4.994744,-8.165900,7.856083,3.028096,-0.901138,5.904855,4.749328,8.833602,0.777955,1.317966,6.501363,-5.415485,1.032208,3.860969,-7.816227,-7.543013,2.073418,-4.072863,-5.601688,7.505613,9.738751,-7.175458,-8.145149,2.066867,3.726354,0.896523,5.015781,3.912206,-1.690867,-6.399395,7.000411,-6.639041,-4.143430,-6.733959,-2.741527,8.748035,-8.532710,9.763233,2.633778,-9.411350,9.227904,-2.806958,9.312066,2.227299,-4.979181,-0.572611,-7.226203,-0.503529,-7.116076,6.058771,6.669380,-4.156635,-9.017770,-9.907115,-0.810619,-3.158433,-2.362683,2.527115,-7.679039,7.699367,-7.514015,0.424887,-5.039938,5.730495,-1.466396,-0.303230,-8.450549,5.364559,-7.324137,-0.716029,-8.773916,-8.999367,7.299487,-6.337423,-3.824037,8.616988,6.959909,-7.429404,-4.522637,-8.621451,-5.084204,-4.810401,-7.196671,-2.197128,4.486524,9.572381,9.091649,-2.697775,6.694352,5.499662,1.986801,9.591199,8.200422,-7.092120,0.192161,-6.030848,1.405932,-4.148896,-6.829934,-8.161636,-5.270052,3.221084,3.534382,-6.834871,-0.659807,5.213522,-9.252712,-1.155920,-1.609909,-7.953975,-6.376334,6.345362,1.923418,2.807560,-0.380029,-4.574076,3.262056,6.805334,8.422487,-8.336932,3.878524,9.514375,-2.360495,4.504700,2.121619,-9.087609,-1.603225,0.853355,-1.958456,5.601109,5.634414,8.258046,2.987518,3.144817,-3.647023,-9.889966,9.178763,-7.450500,0.314251,-0.715525,7.868115,-9.980235,6.043244,4.465962,-0.924037,-1.625249,-7.608087,2.546513,-2.901152,5.079486,-7.624476,-0.102503,7.945059,8.693365,-6.854954,1.215208,-3.346308,6.157614,-1.689769,5.756310,7.349332,-8.238036,7.452496,6.674288,-4.447455,3.918435,-4.341959,2.794463,-1.408955,7.490719,-6.837592,-9.669919,-4.290168,-8.715506,-5.276594,-2.261425,-3.820270,-1.662441,-6.874020,8.384151,-6.220789,7.123975,0.783886,-7.025750,1.343750,-8.155555,5.359495,-5.654792,0.156934,-7.879364,7.715022,0.119982,7.752019,0.460414,-6.528069,-7.822187,0.763237,6.799757,-0.957487,-6.529910,7.479219,-9.322800,8.679358,2.852503,1.049392,5.159373,-8.796568,-4.081908,-6.951732,0.043616,3.919763,1.271816,5.303679,6.892747,-9.042406,7.236456,-2.512677,-5.318254,-4.866362,-2.257558,3.355139,-1.867554,7.352423,9.513342,2.434237,-8.253874,8.171534,2.213906,-3.764522,-2.924245,7.644823,6.074303,0.020921,5.390530,0.207446,-4.645163,1.503829,-1.575068,1.107920,-6.905731,-7.962799,0.130807,-4.162412,-5.547165,2.230570,-3.762909,-5.540920,3.045514,8.578309,2.631282,-6.547064,-4.501431,6.897319,-5.026394,-4.466963,8.876737,2.436736,-5.140093,8.189664,2.719452,-5.004575,5.983993,6.464329,-1.662933,-4.178433,2.546850,2.166782,-4.013706,-9.816481,-8.698434,-0.973605,9.874363,-9.177150,9.538644,-0.178369,2.875245,-2.482099,8.989757,8.005933,0.702760,0.496489,-9.802319,-3.189923,3.680681,-4.376497,3.636543,0.434479,-7.410489,5.105445,-3.450766,-2.667273,-9.938830,-1.349276,-7.652080,3.110396,9.607425,-1.714221,-3.437101,8.434401,8.674563,0.381533,-3.809940,2.004927,-3.895159,-5.447410,-9.472208,-0.241918,-4.955605,-2.799162,-0.903461,-9.165262,6.343539,-5.370338,5.602710,3.665542,9.235221,9.849510,-7.194506,-6.414383,7.040740,9.241449,-1.122077,-6.217171,-4.879655,4.535815,6.855185,7.393765,7.109410,-5.485214,6.486116,3.272572,-8.966347,-4.796969,-9.510638,5.426464,8.769541,1.387255,7.017072,-4.581661,3.081267,-2.665667,1.777355,8.347634,8.396679,1.612927,5.348709,2.562010,-4.309623,-4.678186,4.199464,-5.293529,-5.212427,-9.601488,-4.397010,-8.652243,-9.118899,-8.746488,-0.665053,-1.288830,1.658707,-9.709945,6.052803,-8.189531,8.824581,-3.379585,-9.530022,0.583568,-8.632333,-1.053147,0.403328,-8.913351,-4.185356,3.576502,-5.564921,-2.769239,-2.245940,2.039421,4.468947,9.867035,-6.441345,1.123911,-7.051585,-0.029084,-2.848256,5.288231,4.192118,3.450424,-2.520946,-0.482059,7.068695,-0.003867,4.860156,7.239129,4.686369,9.191135,-1.182303,2.924723,6.708855,9.689779,-7.046109,7.648576,6.817398,8.403613,-3.386703,-9.887070,3.893394,0.938692,-1.840680,2.349021,4.216215,-7.266239,3.930801,-8.331991,7.118997,-6.045997,4.680581,8.692890,-2.640618,-4.360063,-9.636865,-2.526247,-3.571853,-5.227532,-6.543267,-7.266973,-7.151290,4.707699,-5.011094,-6.622330,-8.426084,-2.165343,0.993774,-8.929371,-2.659549,-8.347056,1.311966,-7.154694,-1.507155,8.248313,-1.813788,-4.163128,-6.627991,-2.831164,3.886951,-1.806746,7.487728,8.620092,-5.947688,2.282996,5.021713,1.541981,-5.949575,-8.554147,-2.241154,-7.574863,5.118039,7.179637,-4.843066,2.070389,-7.715740,3.033593,-7.904069,-2.333349,-2.367620,2.982633,1.768561,6.136077,1.151431,-9.862653,5.526654,-7.992023,9.220202,-1.451292,-2.164395,-6.248553,8.522065,-5.914052,-4.989546,-1.796051,-2.792317,-9.918744,-0.421211,-1.800232,9.269024,0.925846,1.149098,-5.952937,0.598557,-5.371330,-2.934574,-8.606640,3.646063,3.439052,-9.871859,-2.398888,0.251317,-1.688226,-1.960183,1.592412,-3.573866,-6.290499,8.365876,-8.567365,2.463507,-8.331282,1.265804,0.160928,7.458826,6.778696,-6.736533,1.679902,-0.040903,3.687152,-0.957925,6.791969,3.106721,-7.002705,-3.546513,3.162886,6.122316,3.463471,3.497359], dtype = "float64")#candidate|22123|(693,)|const|float64
const_22124 = relay.const([-6.622295,5.691512,5.799291,4.660932,-4.480253,-4.687852,-6.302714,-6.512036,-8.102313,-5.301423,-5.743957,7.304033,-8.486816,8.724476,7.050713,-7.916474,-5.334978,7.891722,-5.468933,6.879578,-6.296495,-0.552069,2.167010,4.652055,5.886423,-2.377807,-3.209101,3.260893,-3.206625,-8.318560,4.086669,6.402395,-5.782179,4.123272,8.058098,-1.841484,-1.455688,0.796857,2.097306,3.225503,-5.603462,-4.443728,4.168309,2.406765,-6.895310,-5.178771,3.687632,-9.429211,-7.389193,-2.090825,-1.225634,-6.982154,2.792480,-7.137175,-2.548678,1.775512,4.167441,8.199875,3.735986,-7.911145,4.913592,2.469915,-5.707637,-6.310556,7.482631,8.517602,4.268448,4.970133,4.236788,8.062393,1.940573,-6.745603,4.693957,-7.394464,-3.378704,-4.152843,1.839173,-5.994957,8.160497,-8.906511,0.753822,-0.685438,9.331155,2.884488,-2.717331,3.426261,9.071804,-5.576850,5.921880,0.057833,-3.799518,7.681870,4.441480,3.847717,9.943649,-2.959187,8.815404,3.491948,-2.293513,7.370730,-0.119584,-8.724450,-8.751733,-0.309952,1.110631,-0.993648,9.494739,0.985026,8.075073,-3.702342,7.591950,-5.380268,9.924012,2.817547,-1.790720,-5.539375,7.963596,0.231148,-1.153801,-0.475949,3.815050,1.091010,-9.459042,-0.879810,8.527084,-4.926689,5.072467,-8.363514,0.969521,-3.058646,-6.231081,-1.566269,9.347524,-9.686208,6.439741,-2.415182,4.123485,2.760086,-4.944476,4.370970,-2.897733,-6.923247,-4.501203,8.303968,9.234278,-6.159711,-3.497782,7.619088,-0.674267,1.477620,-9.683464,-4.634394,5.335725,-9.487711,7.742418,-1.198654,1.760950,1.839591,9.917505,1.056752,-8.240979,-1.595754,-8.200971,5.348722,4.168374,-5.655862,-7.973693,4.571208,9.408184,7.796201,-3.638914,-2.337194,9.295678,7.409093,-2.331044,9.064116,-8.322997,-2.081262,4.106881,3.101627,-7.552037,8.217738,9.436052,2.808279,-5.804605,4.241212,-4.100429,-8.289801,-8.087444,-7.680275,0.170195,2.382996,3.835560,-6.161121,1.084262,-4.911250,-7.842377,-2.285675,-3.846242,-7.289564,4.465946,4.461258,6.831559,2.716012,-4.722695,4.597056,0.476169,9.094678,-0.499760,3.831256,-9.171216,8.969246,6.275662,-5.382078,7.950184,-6.554671,-2.635962,-9.082914,-5.716694,9.309432,9.388852,-6.093378,-1.759916,-1.925129,0.682495,-5.306429,9.141071,-3.041142,-7.416532,-2.087285,9.515970,-6.202969,7.298655,-2.296798,-9.158384,-0.252803,-4.717467,-4.669452,-7.754724,9.563189,-0.506877,5.778270,7.415284,0.801584,-4.333058,-8.052227,-9.331068,-2.965482,1.489424,7.571241,-8.519347,-5.969416,-8.028999,7.321798,5.070404,1.454321,9.993661,7.387041,-2.706194,-2.250670,-2.151335,4.332728,1.794482,-8.189949,-0.968201,-5.318500,3.938449,8.307030,7.806563,6.106982,7.242678,-1.476029,2.642337,0.951306,-1.287099,0.616956,-7.024716,-7.919404,-4.105817,4.721707,-4.526460,3.569285,-8.728011,-5.717845,-0.673986,-8.347515,-2.185159,-5.929378,-9.571822,6.884784,0.834158,2.093488,1.363431,2.666216,8.959919,-0.207710,-6.616283,3.131050,-4.037735,-6.247251,5.924070,-6.887781,9.711007,-4.057486,8.349546,4.358223,-6.240126,-1.216151,-5.245661,8.922832,-5.228782,3.549078,3.723709,5.512981,-3.125208,-2.043015,-2.191023,2.125267,1.376744,1.519375,-5.140421,3.115750,-1.667880,-9.473786,7.561290,-0.466152,-9.842982,-5.097458,-5.915851,6.471399,6.284722,7.362070,4.496095,-5.950047,-5.739566,5.735069,-1.664263,8.668068,-8.259730,7.673777,3.912967,-9.552731,5.319942,8.455831,-5.299426,6.099791,6.102903,-4.250377,2.175436,0.010304,-9.312122,-4.991219,-1.968854,6.335411,-5.475845,-0.637228,-5.971046,4.589199,-3.604579,-1.035169,3.938729,-8.730271,-6.004747,8.717324,7.541042,9.364549,8.084773,-7.956103,3.616403,7.691407,-2.848460,0.439904,-3.445746,7.021869,3.781905,0.763397,9.099977,9.635476,-4.741901,4.737822,-9.736163,-4.900081,2.662975,2.461003,-2.481200,-1.992439,-6.220498,-6.683006,-9.088786,6.299332,0.200563,-7.484086,1.816872,-3.969934,0.692450,4.206203], dtype = "float32")#candidate|22124|(396,)|const|float32
var_22125 = relay.var("var_22125", dtype = "uint64", shape = (130,))#candidate|22125|(130,)|var|uint64
const_22126 = relay.const([-3,-4,-2,-7,-3,-9,1,2,2,10,-10,-4,-3,-4,-7,9,-8,9,7,7,6,2,9,-9,-4,4,1,4,5,4,-3,-1,5,10,-7,4,2,-1,4,3,-2,-3,-7,6,6,-5,2,-1,6,-2,8,-8,-6,1,-10,7,3,4,10,3,9,-7,4,1,7,4,-1,-6,-1,6,-5,-3,4,10,5,-10,-3,-7,-4,8,-2,-7,-3,8,3,-5,-7,-7,-6,-7,-2,7,-5,-2,-3,-10,-3,5,-3,-9,-9,5,5,-8,-10,-1,-5,8,1,9,-10,-8,-8,-8,8,-7,4,-2,5,9,9,10,6,-4,-7,2,1,-2,-3,-8,-10,7,-9,4,-2,-1,-10,-5,-8,3,9,5,-5,9,-9,-8,-3,2,7,6,-8,-2,-10,5,3,5,5,-4,-9,8], dtype = "uint64")#candidate|22126|(160,)|const|uint64
call_22122 = relay.TupleGetItem(func_3611_call(relay.reshape(const_22123.astype('float64'), [9, 11, 7]), relay.reshape(const_22124.astype('float32'), [396,]), relay.reshape(var_22125.astype('uint64'), [130,]), relay.reshape(const_22126.astype('uint64'), [160,]), ), 9)
call_22127 = relay.TupleGetItem(func_3617_call(relay.reshape(const_22123.astype('float64'), [9, 11, 7]), relay.reshape(const_22124.astype('float32'), [396,]), relay.reshape(var_22125.astype('uint64'), [130,]), relay.reshape(const_22126.astype('uint64'), [160,]), ), 9)
output = relay.Tuple([call_22114,call_22122,const_22123,const_22124,var_22125,const_22126,])
output2 = relay.Tuple([call_22115,call_22127,const_22123,const_22124,var_22125,const_22126,])
func_22132 = relay.Function([var_22125,], output)
mod['func_22132'] = func_22132
mod = relay.transform.InferType()(mod)
mutated_mod['func_22132'] = func_22132
mutated_mod = relay.transform.InferType()(mutated_mod)
var_22133 = relay.var("var_22133", dtype = "uint64", shape = (130,))#candidate|22133|(130,)|var|uint64
func_22132_call = mutated_mod.get_global_var('func_22132')
call_22134 = func_22132_call(var_22133)
output = call_22134
func_22135 = relay.Function([var_22133], output)
mutated_mod['func_22135'] = func_22135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12653_call = mod.get_global_var('func_12653')
func_12655_call = mutated_mod.get_global_var('func_12655')
call_22219 = func_12653_call()
call_22220 = func_12653_call()
output = relay.Tuple([call_22219,])
output2 = relay.Tuple([call_22220,])
func_22232 = relay.Function([], output)
mod['func_22232'] = func_22232
mod = relay.transform.InferType()(mod)
mutated_mod['func_22232'] = func_22232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_22232_call = mutated_mod.get_global_var('func_22232')
call_22233 = func_22232_call()
output = call_22233
func_22234 = relay.Function([], output)
mutated_mod['func_22234'] = func_22234
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18827_call = mod.get_global_var('func_18827')
func_18829_call = mutated_mod.get_global_var('func_18829')
call_22238 = relay.TupleGetItem(func_18827_call(), 2)
call_22239 = relay.TupleGetItem(func_18829_call(), 2)
func_11659_call = mod.get_global_var('func_11659')
func_11663_call = mutated_mod.get_global_var('func_11663')
const_22259 = relay.const([-0.664697,-0.768115,-0.414322,5.462237,-0.361966,0.150203,7.354863,-6.550308,-3.020686,5.618088,-8.389990,2.000762,8.353701,5.724697,8.713795,-0.014179,6.496342,3.745529,6.050908,-1.020061,3.836878,-2.192595,-7.326079,7.274017,-3.303906,1.078448,3.954026,-5.809723,8.067040,8.070483,9.667318,7.571843,-1.928427,-2.479841,1.684232,-3.696716,-5.012387,6.936072,5.590457,3.711239,-2.997384,-2.779289,9.817319,-1.595072,-0.684381,-9.139948,-2.856317,-8.483270,-2.739234,-6.413220,3.553809,2.744848,9.706252,3.559676,1.421949,7.796360,4.535956,5.231587,-8.326040,6.538923,8.735294,-2.624955,7.336835,6.438347,0.146606,7.293317,-2.779017,8.349370,-0.791515,-8.824813,5.859605,4.937148,0.250803,-1.264885,-8.408609,-6.074593,8.674892,8.369922,4.509650,-7.373339,-0.899882,4.412288,-7.880646,3.860908,9.195735,9.341749,2.395675,4.517522,3.915869,-5.028089,-5.656717,-3.056778,8.514920,-2.090576,-4.245100,0.899139,9.401095,6.309713,2.010425,-4.511062,-4.502183,-8.643451,-8.751174,-7.968536,2.933149,9.925529,7.484968,7.976838,-4.478107,3.599164,-9.610570,2.227666,4.403062,-0.026938,5.996876,-7.847624,-3.622805,6.554130,-1.246689,-3.802272,-5.918240,0.726830,8.066179,-0.699490,4.876326,-9.405811,9.705662,9.240460,-7.583975,0.196692,-7.490097,5.828529,-5.220068,5.155160,-2.289758,-6.591808,0.902362,-6.185184,-4.159396,-9.383251,-7.861198,-7.635746,6.223008,9.789786,1.741195,9.349202,-4.348537,-2.971518,-1.159882,0.047880,3.737618,9.669168,-1.626724,-0.177593,4.841360,-1.526603,6.619682,7.176217,-4.323765,2.029319,1.049765,1.068099,5.426333,8.209225,5.839045,9.222578,-4.568940,5.805214,-5.017688,-1.741956,0.502825,-4.688791,7.808265,9.854490,-7.248180,7.875701,8.535220,9.495684,-5.179559,-5.498590,0.572176,-2.217385,6.161153,-1.681898,6.468962,9.937393,7.688780,-4.979494,6.706982], dtype = "float32")#candidate|22259|(189,)|const|float32
var_22260 = relay.var("var_22260", dtype = "float64", shape = (832,))#candidate|22260|(832,)|var|float64
call_22258 = relay.TupleGetItem(func_11659_call(relay.reshape(const_22259.astype('float32'), [189,]), relay.reshape(var_22260.astype('float64'), [832, 1]), ), 2)
call_22261 = relay.TupleGetItem(func_11663_call(relay.reshape(const_22259.astype('float32'), [189,]), relay.reshape(var_22260.astype('float64'), [832, 1]), ), 2)
output = relay.Tuple([call_22238,call_22258,const_22259,var_22260,])
output2 = relay.Tuple([call_22239,call_22261,const_22259,var_22260,])
func_22274 = relay.Function([var_22260,], output)
mod['func_22274'] = func_22274
mod = relay.transform.InferType()(mod)
var_22275 = relay.var("var_22275", dtype = "float64", shape = (832,))#candidate|22275|(832,)|var|float64
output = func_22274(var_22275)
func_22276 = relay.Function([var_22275], output)
mutated_mod['func_22276'] = func_22276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11804_call = mod.get_global_var('func_11804')
func_11806_call = mutated_mod.get_global_var('func_11806')
call_22280 = relay.TupleGetItem(func_11804_call(), 0)
call_22281 = relay.TupleGetItem(func_11806_call(), 0)
output = call_22280
output2 = call_22281
func_22320 = relay.Function([], output)
mod['func_22320'] = func_22320
mod = relay.transform.InferType()(mod)
output = func_22320()
func_22321 = relay.Function([], output)
mutated_mod['func_22321'] = func_22321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12653_call = mod.get_global_var('func_12653')
func_12655_call = mutated_mod.get_global_var('func_12655')
call_22361 = func_12653_call()
call_22362 = func_12653_call()
func_13402_call = mod.get_global_var('func_13402')
func_13404_call = mutated_mod.get_global_var('func_13404')
call_22380 = relay.TupleGetItem(func_13402_call(), 1)
call_22381 = relay.TupleGetItem(func_13404_call(), 1)
output = relay.Tuple([call_22361,call_22380,])
output2 = relay.Tuple([call_22362,call_22381,])
func_22393 = relay.Function([], output)
mod['func_22393'] = func_22393
mod = relay.transform.InferType()(mod)
mutated_mod['func_22393'] = func_22393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_22393_call = mutated_mod.get_global_var('func_22393')
call_22394 = func_22393_call()
output = call_22394
func_22395 = relay.Function([], output)
mutated_mod['func_22395'] = func_22395
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14127_call = mod.get_global_var('func_14127')
func_14129_call = mutated_mod.get_global_var('func_14129')
call_22418 = relay.TupleGetItem(func_14127_call(), 1)
call_22419 = relay.TupleGetItem(func_14129_call(), 1)
func_2726_call = mod.get_global_var('func_2726')
func_2729_call = mutated_mod.get_global_var('func_2729')
const_22436 = relay.const([-3.085419,1.159434,-0.680142,2.144384,-7.877095,-9.911750,7.835652,3.709947,3.818220,8.810247,3.732226,5.167796,5.982922,3.061850,2.702869,-7.748677,4.031171,-4.301568], dtype = "float32")#candidate|22436|(18,)|const|float32
call_22435 = relay.TupleGetItem(func_2726_call(relay.reshape(const_22436.astype('float32'), [1, 3, 6])), 0)
call_22437 = relay.TupleGetItem(func_2729_call(relay.reshape(const_22436.astype('float32'), [1, 3, 6])), 0)
uop_22449 = relay.atanh(const_22436.astype('float32')) # shape=(18,)
output = relay.Tuple([call_22418,call_22435,uop_22449,])
output2 = relay.Tuple([call_22419,call_22437,uop_22449,])
func_22452 = relay.Function([], output)
mod['func_22452'] = func_22452
mod = relay.transform.InferType()(mod)
mutated_mod['func_22452'] = func_22452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_22452_call = mutated_mod.get_global_var('func_22452')
call_22453 = func_22452_call()
output = call_22453
func_22454 = relay.Function([], output)
mutated_mod['func_22454'] = func_22454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18887_call = mod.get_global_var('func_18887')
func_18889_call = mutated_mod.get_global_var('func_18889')
call_22475 = relay.TupleGetItem(func_18887_call(), 0)
call_22476 = relay.TupleGetItem(func_18889_call(), 0)
func_11147_call = mod.get_global_var('func_11147')
func_11149_call = mutated_mod.get_global_var('func_11149')
var_22484 = relay.var("var_22484", dtype = "float64", shape = (832,))#candidate|22484|(832,)|var|float64
call_22483 = relay.TupleGetItem(func_11147_call(relay.reshape(var_22484.astype('float64'), [832,])), 5)
call_22485 = relay.TupleGetItem(func_11149_call(relay.reshape(var_22484.astype('float64'), [832,])), 5)
output = relay.Tuple([call_22475,call_22483,var_22484,])
output2 = relay.Tuple([call_22476,call_22485,var_22484,])
func_22490 = relay.Function([var_22484,], output)
mod['func_22490'] = func_22490
mod = relay.transform.InferType()(mod)
var_22491 = relay.var("var_22491", dtype = "float64", shape = (832,))#candidate|22491|(832,)|var|float64
output = func_22490(var_22491)
func_22492 = relay.Function([var_22491], output)
mutated_mod['func_22492'] = func_22492
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19599_call = mod.get_global_var('func_19599')
func_19601_call = mutated_mod.get_global_var('func_19601')
call_22640 = relay.TupleGetItem(func_19599_call(), 1)
call_22641 = relay.TupleGetItem(func_19601_call(), 1)
output = call_22640
output2 = call_22641
func_22649 = relay.Function([], output)
mod['func_22649'] = func_22649
mod = relay.transform.InferType()(mod)
mutated_mod['func_22649'] = func_22649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_22649_call = mutated_mod.get_global_var('func_22649')
call_22650 = func_22649_call()
output = call_22650
func_22651 = relay.Function([], output)
mutated_mod['func_22651'] = func_22651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15992_call = mod.get_global_var('func_15992')
func_15994_call = mutated_mod.get_global_var('func_15994')
call_22689 = relay.TupleGetItem(func_15992_call(), 1)
call_22690 = relay.TupleGetItem(func_15994_call(), 1)
func_3117_call = mod.get_global_var('func_3117')
func_3120_call = mutated_mod.get_global_var('func_3120')
const_22693 = relay.const([-3.944449,-8.249860,-2.423273,7.513530,-6.393578,-4.725774,7.626872,0.400860,-1.082063,2.334029,-9.143019,-0.051950,1.628698,4.145219,-5.283534,-9.653727,0.130576,5.705751,-5.709927,2.892435,-7.050362,2.980452,-5.577202,7.042647,2.099158,7.342804,-9.533184,4.405062,6.913084,-3.599610,3.929904,-9.470514,6.258774,7.791080,3.302435,-7.407466,-3.053255,0.089175,-4.755612,2.035816,-5.916486,9.389480,-9.757461,-0.111899,7.728349,-8.279134,6.268199,-6.817631,-9.456261,7.922844,-9.919793,-5.438835,4.287630,4.466331,-7.984209,7.678625,9.421706,8.864077,-5.846115,-6.445446,-8.799836,-4.147960,3.952086,-4.190774,-3.643666,9.744502,-8.900307,2.068129,-2.868363,6.185276,9.380887,8.933516,-4.987818,3.844483,-7.194539,-1.145702,-8.540907,-4.972703,6.425471,2.606997,-2.462331,-7.002383,-6.988492,-4.166918,3.572959,-5.577434,5.010503,0.123132,-1.664347,-7.816274,-6.050226,-2.070705,4.097477,6.899257,0.312079,5.799500,7.707379,-2.201335,9.310707,-1.282345,3.163485,-5.877292,-2.077378,-8.974741,-6.116157,2.899540,7.116850,9.518874,3.706497,-0.988519,1.196241,-5.702968,5.476293,0.935000,-9.761588,2.757329,-5.922983,-9.627169,-0.217174,6.804223,2.095035,9.704593,-1.899699,0.856262,1.169973,0.852737,6.922867,-1.100922,-7.521461,-0.938599,3.658827,-0.178520,1.148750,8.082240,7.325443,-6.367540,3.385540,-3.700617,-8.164512,8.335735,7.789719,-7.797696,1.308679,6.413441,-6.722082,-1.546265,-8.228304,0.465607,3.092422,3.717915,-6.827280,9.646051,4.294863,7.784166,0.939865,-7.919278,8.919216,-7.878851,6.224537,0.212743,3.305599,8.366501,-7.517715,7.033753,1.089876,7.988037,-9.814767,-3.810723,-5.699971,1.004616,-9.890590,-9.774606,-4.406605,-4.413897,-5.028342,-8.659808,3.066476,1.942865,-0.444745,6.606327,3.029590,1.007211,2.767959,-3.995215,-4.567804,-6.095915,4.770892,-2.215745,7.151385,4.610648,-2.877520,9.280392,4.231987,-1.421265,3.955512,-0.912430,-2.445923,-7.201098,9.223018,3.248800,-0.072436,-3.167243,-6.012730,3.323100,-3.019555,3.332840,-8.297032,-2.705351,-2.958065,-3.125403,0.861029,-8.954463,-8.183554,4.238821,7.618876,0.359631,-0.999482,0.835434,4.460420,-2.923421,8.155576,-0.625127,-6.679254,-9.783724,3.121839,-3.305221,3.052437,-5.064363,2.543406,1.180388,-7.320213,-3.789873,-7.825303,2.466634,1.250881,8.678225,-6.315500,-7.817502,3.169275,6.322518,6.863237,6.686078,-5.198398,9.702210,6.757836,1.550002,7.101520,8.434419,6.720772,3.414257,-2.109284,-1.826869,7.278969,-3.188193,2.230780,6.049372,4.262513,7.523598,8.340167,-5.744829,4.756869,-6.375224,1.138297,-5.895805,2.657355,9.205931,6.434346,-0.669151,9.282223,8.539054,-6.196283,5.235907,2.004449,0.890124,9.937485,7.835840,6.988119,-7.138582,2.939796,-6.186936,-8.906055,4.635134,2.739216,-5.570084,-4.703564,0.527967,8.297694,-6.066279,1.816904,2.566173,4.384547,3.305453,-6.314815,-7.419218,-9.567414,-1.577847,-6.673300,-6.176961,7.799522,-0.086852,-7.329272,-9.244789,6.523955,-3.903091,2.352338,8.420847,8.690953,6.270220,-6.949850,8.451415,-1.374678,-3.541431,7.145541,-7.295745,4.881723,-5.630554,-6.880920,1.174006,-0.142125,-4.611074,4.030830,-2.568157,-1.266548,4.195744,4.083392,-9.631988,-0.037857,8.745407,7.328260,7.454378,-1.894810,4.691131,-4.997131,-2.004222,-5.730948,-3.589650,0.468232,-8.559691,4.150305,-7.424238,9.019408,-3.164418,9.152458,7.187343,-6.945032,-1.488913,0.964207,5.004892,-5.948448,-8.129961,3.469677,3.416861,2.300433,-1.909540,6.419532,-5.831043,9.674469,-0.184727,-3.569488,-3.123717,-7.300198,6.605071,-5.183425,-3.633168,2.286531,8.675687,9.721935,7.271506,7.556915,8.560159,-2.956873,7.535840,9.177889,2.512349,8.546342,-4.014095,-3.544074,3.448638,-8.287471,7.558683,-5.396249,-1.411760,2.686465,4.300551,-7.090416,5.486825,-4.748665,-9.435575,3.868472,6.116215,3.001497,-4.923736,2.116918,-9.609110,5.484269,1.525525,4.554575,-9.315968,3.371291,6.484932,-8.840800,4.811416,1.114982,-5.335519,7.572333,4.840980,3.236333,-9.775509,-6.570280,8.484916,-2.959571,3.648280,-2.421532,0.008539,2.238949,4.134896,3.600190,-6.641176,4.922962,5.373161,-4.932432,6.359109,8.520697,1.686725,4.364209,8.929469,4.598103,8.114471,-0.059143,-9.026584,9.501079,-8.695674,-2.438636,7.076437,4.685717,-8.291149,2.914694,-6.547111,0.774259,-9.639889,-9.946633,-6.082357,5.398851,4.614590,-2.193198,4.558631,-0.705138,2.072561,0.829935,-9.172837,9.144521,-4.129062,-3.994097,5.294237,-2.192665,-6.824205,-5.876542,4.383684,-5.098021,4.189675,-6.328571,-3.686072,-2.350772,7.405030,-2.202417,8.040635,-0.066488,3.938350,-8.821335,-9.833301,-0.703574,5.291257,0.153643,-5.999260,9.097495,2.645935,6.668258,-2.664481,9.635082,6.028866], dtype = "float64")#candidate|22693|(480,)|const|float64
call_22692 = relay.TupleGetItem(func_3117_call(relay.reshape(const_22693.astype('float64'), [4, 12, 10])), 0)
call_22694 = relay.TupleGetItem(func_3120_call(relay.reshape(const_22693.astype('float64'), [4, 12, 10])), 0)
output = relay.Tuple([call_22689,call_22692,const_22693,])
output2 = relay.Tuple([call_22690,call_22694,const_22693,])
func_22725 = relay.Function([], output)
mod['func_22725'] = func_22725
mod = relay.transform.InferType()(mod)
output = func_22725()
func_22726 = relay.Function([], output)
mutated_mod['func_22726'] = func_22726
mutated_mod = relay.transform.InferType()(mutated_mod)
const_22727 = relay.const(-5.173857, dtype = "float64")#candidate|22727|()|const|float64
const_22728 = relay.const([[[-3.605449,7.290800,2.647766,4.082498,3.575345,-4.944912,-7.223638,-5.793410],[5.478993,3.408422,9.564309,3.296124,0.089481,-7.712009,-7.236921,-4.916174],[-8.229814,-9.617106,-3.032221,-1.077051,6.470575,-7.727685,-7.515113,7.675816],[7.506690,0.250843,-2.794285,-0.528743,8.677966,7.618536,9.871968,-9.460970],[4.372908,9.910714,-9.153145,-9.282978,4.073069,-5.909458,7.600380,2.855978],[-3.020771,3.600703,7.682120,-1.665506,-4.273120,4.569146,7.401545,6.652888],[-3.624639,-4.765388,0.946944,-6.476625,-1.168008,-6.236996,-1.713284,-6.024248]],[[8.585071,-3.361069,8.894535,6.559952,-8.429086,6.630403,4.838875,9.573834],[-8.202993,-8.486789,-3.767005,-0.028661,4.698973,-4.614387,-4.778241,-5.728532],[-0.309202,-6.401672,5.443306,3.837420,-5.181612,4.337474,9.255936,2.937901],[0.485429,4.064519,-4.629522,-8.932181,8.769931,-5.090877,8.335535,4.622788],[2.951476,9.822113,1.430021,-6.712686,-0.982320,6.664693,-9.919948,9.063459],[5.987283,9.695475,-1.222216,1.572834,-3.704973,0.969570,2.769651,2.466508],[-8.559709,4.012932,4.542844,-2.911463,-3.288554,-5.481765,-6.116924,-2.276964]],[[-7.660494,-1.266827,7.857552,-6.013647,7.423679,4.745362,-5.398722,9.804329],[8.193692,2.839309,-1.087389,-7.810929,7.384547,-8.112415,-1.740308,4.034487],[-8.283212,9.794045,-9.372121,-7.882470,6.004340,-6.941829,-0.376969,4.421651],[-3.355742,1.182483,-4.561093,6.419113,-2.756847,5.187778,-5.769135,3.709711],[-1.251074,-7.148797,9.785048,-5.418749,-7.953946,-7.842901,-4.520258,3.653329],[-8.915134,-7.572722,-0.338721,7.602426,6.168918,-4.518116,3.577996,-1.996305],[-0.532288,-2.795395,7.815366,6.564134,6.137165,5.508148,7.206246,6.526783]],[[7.022508,-5.592627,7.277179,-3.376450,-7.001297,1.327104,-5.718333,-6.308188],[-6.245879,-6.319190,1.389434,-7.427669,-1.202794,3.184771,-4.486736,7.585519],[-6.208463,3.339429,1.829312,-0.669924,-3.531367,-5.647206,6.424760,-7.084607],[1.324487,-5.672179,-1.130920,-9.371085,-0.489895,-9.753555,-8.428638,-3.351845],[4.804266,-7.365180,9.385687,-2.708860,-8.920515,-3.144634,4.896378,-3.546804],[-4.797449,-6.333318,7.858145,6.832598,-0.819505,-9.531237,0.176174,5.801200],[-0.797914,-7.540529,-1.733260,-0.003053,8.081344,-2.294661,1.802358,8.042676]]], dtype = "float64")#candidate|22728|(4, 7, 8)|const|float64
bop_22729 = relay.mod(const_22727.astype('float64'), const_22728.astype('float64')) # shape=(4, 7, 8)
output = relay.Tuple([bop_22729,])
output2 = relay.Tuple([bop_22729,])
func_22751 = relay.Function([], output)
mod['func_22751'] = func_22751
mod = relay.transform.InferType()(mod)
mutated_mod['func_22751'] = func_22751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_22751_call = mutated_mod.get_global_var('func_22751')
call_22752 = func_22751_call()
output = call_22752
func_22753 = relay.Function([], output)
mutated_mod['func_22753'] = func_22753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14665_call = mod.get_global_var('func_14665')
func_14667_call = mutated_mod.get_global_var('func_14667')
call_22779 = func_14665_call()
call_22780 = func_14665_call()
output = relay.Tuple([call_22779,])
output2 = relay.Tuple([call_22780,])
func_22783 = relay.Function([], output)
mod['func_22783'] = func_22783
mod = relay.transform.InferType()(mod)
output = func_22783()
func_22784 = relay.Function([], output)
mutated_mod['func_22784'] = func_22784
mutated_mod = relay.transform.InferType()(mutated_mod)
var_22838 = relay.var("var_22838", dtype = "float32", shape = (1, 3, 9))#candidate|22838|(1, 3, 9)|var|float32
uop_22839 = relay.cos(var_22838.astype('float32')) # shape=(1, 3, 9)
output = uop_22839
output2 = uop_22839
func_22846 = relay.Function([var_22838,], output)
mod['func_22846'] = func_22846
mod = relay.transform.InferType()(mod)
mutated_mod['func_22846'] = func_22846
mutated_mod = relay.transform.InferType()(mutated_mod)
var_22847 = relay.var("var_22847", dtype = "float32", shape = (1, 3, 9))#candidate|22847|(1, 3, 9)|var|float32
func_22846_call = mutated_mod.get_global_var('func_22846')
call_22848 = func_22846_call(var_22847)
output = call_22848
func_22849 = relay.Function([var_22847], output)
mutated_mod['func_22849'] = func_22849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18019_call = mod.get_global_var('func_18019')
func_18020_call = mutated_mod.get_global_var('func_18020')
call_22870 = func_18019_call()
call_22871 = func_18019_call()
func_19487_call = mod.get_global_var('func_19487')
func_19491_call = mutated_mod.get_global_var('func_19491')
var_22901 = relay.var("var_22901", dtype = "uint64", shape = (160,))#candidate|22901|(160,)|var|uint64
const_22902 = relay.const([2.301691,9.299776,-4.057427,-1.398263,-5.645543,-2.420256,7.920991,-5.345463,4.061316,-5.482652,1.873021,5.157668,-5.480471,1.517607,-5.366538,1.479325,7.085390,3.972845,-1.300046,4.960252,4.908554,1.297837,-1.158676,3.005370,6.748326,-6.861448,7.761919,-3.754106,-7.066447,8.906216,-0.979686,-2.948454,-3.150068,-0.737014,8.775779,9.912902,0.734258,5.000176,-7.831353,9.607793,-1.906930,-8.891641,6.997991,6.696144,6.522684,-5.304785,-0.713444,1.726290,-5.322401,3.718195,1.536930,-1.669384,6.590830,-5.764691,9.858243,8.769616,7.393780,4.240014,-5.951864,-0.337320,9.491382,4.767187,7.031307,-2.885467,-6.231844,7.892066,-1.505725,-9.344089,7.867688,6.296820,-8.032748,-4.751211,0.831453,5.869197,9.264399,7.039608,-7.336625,-0.997702,8.111274,-0.617250,-5.532107,3.726672,0.069345,-8.305840,-0.175099,1.466511,-5.456692,-8.101284,6.146104,2.560430,-2.526493,-7.362309,6.612383,-2.545200,7.763729,1.508824,3.469379,3.924396,-4.576209,1.652402,2.068651,-9.994893,7.828213,8.970153,-5.512385,9.359446,1.268322,4.112369,-3.078928,4.938648,-3.868911,7.195509,7.601762,4.118119,-9.896783,-6.321197,2.233523,1.334268,-3.993231,-7.891055,1.133998,3.205133,3.083985,8.718870,-4.714720,1.814315,6.926151,-3.642616,4.824405,7.297995,1.826697,-1.743771,-2.350784,5.468673,-1.655500,9.780024,1.676732,5.773547,8.495975,-5.993019,9.065334,5.318880,-8.998966,-6.502500,1.697928,6.491696,3.686267,7.321977,9.567923,-2.775365,-3.323650,7.980025,-7.184782,-6.379481,3.250384,-6.688704,6.850152,-4.174264,6.324732,2.838101,-9.382658,7.747400,-8.456360,2.988992,1.574322,-5.124784,0.351181,4.029084,-5.892062,5.842502,-3.758059,-4.116389,5.279746,4.634878,6.811444,1.583141,8.334687,-7.371655,-3.502479,2.791233,1.461047,9.469689,9.548940,6.650164,1.346398,-8.381656,-0.233178,2.953273,4.481175,-9.533159,3.965830,-6.709955,7.174119,7.386941,-0.743917,2.641064,-4.109529,-1.064438,-5.853573,4.938518,-0.971587,4.816293,-1.666051,0.985708,-4.646566,7.951859,9.570850,-8.447563,-0.903079,-2.247186,0.598902,-1.647972,7.287514,6.553218,-6.053182,4.682543,-2.955457,9.056654,0.107799,-6.990863,8.356688,1.961307,1.817906,6.029239,9.441247,-7.513146,1.012246,-4.691889,7.809393,-9.174702,-8.328574,9.801362,8.752785,-8.513434,4.816792,-0.876752,-0.202743,6.974007,9.886401,9.751088,0.242934,5.720522,-8.308061,2.305441,-0.945647,-1.917801,1.779175,8.168937,-4.585014,0.995482,3.184650,-3.744813,0.853335,4.060306,-3.285761,-5.415685,0.255890,9.574736,5.352716,6.379865,-5.718800,7.092891,6.612558,-9.204084,-3.922131,8.547298,3.168141,8.358420,-4.387601,-1.499000,6.319160,-3.278874,-3.306298,-2.473266,-8.505991,0.077435,0.652293,-7.072338,-5.221629,2.823539,-7.012327,-7.360914,-6.247185,-0.372641,-7.760173,-6.961267,3.569146,-6.793613,-7.109124,-6.258744,7.153610,8.937675,-7.648453,0.781417,8.403290,6.057196,-7.979802,5.042465,3.720125,5.096194,-0.010980,1.794399,-7.840604,-7.465070,-8.576727,6.090315,-9.510516,4.353208,-5.738577,7.362718,5.574889,0.739592,-5.591467,-2.648593,-9.835288,-4.447680,2.620853,3.875102,2.649672,-6.782988,-9.273737,6.222271,3.517780,5.973786,-4.402525,5.497362,2.916695,8.004877,2.546400,0.319930,6.720583,9.867595,1.390678,-5.798106,-2.881687,-5.732089,-9.849374,4.992542,-4.640501,0.692968,-4.630303,-2.885106,7.211354,2.996383,-9.273393,-0.725842,-4.745460,-8.585778,-2.310388,4.330665,-3.497332,2.687768,7.294622,-8.141700,4.245580,-4.273281,-8.873809,5.170869,-6.397588,-0.521850,0.866356,-4.703739,-4.440975,8.172709,5.228357,7.017585,9.046734,-9.864092,-3.522829,-1.028768,-2.631704,8.584781,-0.039789,-6.505221,3.934112,4.555411,-1.004008,0.932066,-9.452881,4.889446,5.388921,7.578668,-9.566369,1.760163,-0.656853,-5.365434,9.190852,8.451893,0.146216,-5.605661,5.486025,4.662365,-7.731799,-5.383017,-9.614254,-2.946829,1.530330,-4.523906,-5.421714,-3.166734,7.797195,2.939227,-5.264835,-3.616798,0.152156,-5.487718,-5.089168,-1.501347,-7.927712,-8.902708,-6.989131,-3.790436,-6.691176,6.715023,4.442090,-5.406532,3.502179,3.345899,-3.714746,6.474440,-7.845583,-7.775628,0.506464,4.243238,-1.236844,-9.004441,0.290109,-0.289689,0.130766,-4.031185,4.413580,-3.904117,-3.337923,-1.959972,6.070573,-4.140623,0.023825,5.448296,1.749292,5.154786,-1.953102,3.648611,-1.694807,1.573394,2.189780,-6.870338,-3.610143,9.625188,-7.546328,-7.524951,8.891835,-0.749751,5.329762,-7.967903,-4.364011,-4.933554,0.154716,-8.964784,6.120727,-5.012729,8.555928,4.711729,1.324657,9.563457,-5.206279,9.635954,-7.120217,8.809816,6.935100,6.844062,7.036858,-9.971206,8.696842,-9.916021,8.921423,4.615954,-2.016211,-5.356397,-8.846436,9.836849,8.635877,-0.737115,-8.622588,-2.305220,9.096545,-1.284582,2.052269,-2.078759,0.672004,-3.365990,9.830779,-0.904797,-2.267551,0.032694,-7.614133,-7.892132,6.535622,3.308540,-9.188666,-9.229089,3.231987,-1.159014,1.658723,6.672159,0.134955,4.948616,-3.132921,-9.572846,8.863562,3.928720,2.658342,8.646249,-4.255922,-6.557064,-1.333374,0.893907,8.218463,3.694020,-9.064034,-6.945373,-3.002053,-5.838066,3.921854,0.152203,-7.096220,-4.655566,-9.371782,-2.918957,-1.834224,6.721329,5.113174,1.382509,-2.671640,-4.204279,7.794017,8.604328,-1.933291,-2.560824,-3.495660,-4.295697,-7.294524,-9.682971,5.936467,-4.643252,-7.800414,-7.873316,-0.407152,-7.629611,-7.598522,5.487297,0.625118,7.278897,-5.489733,9.691403,-3.208933,5.133158,-2.788212,7.041389,-2.079098,-7.171940,-9.429761,2.587994,-8.416484,9.992600,-4.020961,-1.667981,3.511491,8.544649,-8.144748,0.817289,5.072464,4.915431,-9.460227,7.010017,-6.984281,5.684011,-0.280320,5.064214,9.991489,-2.931237,8.429196,7.428516,-3.518072,-0.172109,-1.674965,5.890443,-3.814680,2.384799,-5.622422,-2.684224,-9.025270,9.357954,-4.709698,8.053765,1.347426,3.622608,7.622917,-0.226009,4.757429,-1.039668,-8.100173,5.019535,-9.184007,8.966173,5.730761,-2.965728,-8.421053,1.423234,-6.968258,-8.718380,-0.553704,5.556252,-8.534904,0.452668,-8.850413,0.244366,-4.226156,-3.296782,-0.689214,9.681100,3.877420,9.705284,1.953986,-0.723187,-7.251969,3.648846,-3.989857,-3.239964,-7.764229,-0.022941,8.161830,0.277605,1.908909,-0.746483,-6.986869,1.854835,4.794239,7.519868,6.845625,5.424688,-8.772222,-8.927144,6.440015,6.956068,6.254640,-3.153529,-0.671648,-2.488805,3.478688,2.395390,-9.442806,1.201118,3.481390,-6.208520,-8.696945,-4.014746,-2.128128,4.341347,4.037143,-0.708376,0.976098,3.645407,-3.241039,3.376839,0.484785,1.369865,6.734732,5.623321,8.666905,-9.780348,5.975370,-9.704509,2.738777,2.514023,3.154218,1.205048,6.507760,-6.608051,-2.079276,0.888263,-2.975907,2.083949,-0.289185,-5.766722,-0.411676,7.213056,-6.010476,-8.534871,-4.405772,-3.627992,3.974492,-7.185593,5.917172,-8.489509,-4.577850,1.290822,4.107421,-4.244309,2.034847,8.924693,0.282411,-4.671134,0.448139,-5.626154,-5.586526,7.310132,-0.364932,-2.555929,-0.687748,-0.105527,8.119308,4.229578,-4.414229,-6.088894,-4.889748,-7.539633,-8.294159,5.329726,8.330350,4.388724,0.807800,1.297925,-3.548709,3.318028,-7.547272,2.795473,9.392629,-9.760402,2.267312,2.889582,9.949639,7.930896,-3.943119,1.535684,-1.570054,-0.413561,2.183799,-1.636060,4.256386,-9.953528,5.980371,6.852264,-6.157833,-0.444364,-2.941225,5.808659,3.295249,-1.709259,-8.200768,1.469417,-1.527824,-5.357062,6.689782,-8.751089,-5.945338,5.221880,-1.454314,-6.727418,-7.789333,-8.460795,-4.734690,-2.622530,8.240561,-1.476580,-9.286886,-8.411352,6.861722,-3.205431,8.842265,3.762289,7.033936,4.985101,-2.207204,-1.570541,8.131252,2.413460,0.906100,8.144058,-7.395789,-4.384117,-2.442255,-2.459828,5.289733,-2.185142,3.129070,-0.213629,-4.295242,-8.392887,2.314318,-5.922895,-8.307368,-4.359767,8.313030,-4.338131,1.324385,6.150674,2.139383,5.309056,-8.660960,-2.629945,-8.285576,2.408530,-7.139682,6.700388,-6.285808,-0.681745,9.761428,-0.148370,2.355593,2.112307,1.589302,-4.386575,-2.967625,5.547083,1.312845,-6.822247,-6.974694,1.618779,8.909728,-2.994675,-4.860342,-5.864055,-0.992030,-4.349381,8.562174,-4.119956,-3.200567,-3.896748,8.510901,-0.903278,3.721954,-8.698472], dtype = "float64")#candidate|22902|(832,)|const|float64
var_22903 = relay.var("var_22903", dtype = "float64", shape = (480, 1))#candidate|22903|(480, 1)|var|float64
call_22900 = relay.TupleGetItem(func_19487_call(relay.reshape(var_22901.astype('uint64'), [160,]), relay.reshape(const_22902.astype('float64'), [832,]), relay.reshape(var_22903.astype('float64'), [480,]), ), 0)
call_22904 = relay.TupleGetItem(func_19491_call(relay.reshape(var_22901.astype('uint64'), [160,]), relay.reshape(const_22902.astype('float64'), [832,]), relay.reshape(var_22903.astype('float64'), [480,]), ), 0)
output = relay.Tuple([call_22870,call_22900,var_22901,const_22902,var_22903,])
output2 = relay.Tuple([call_22871,call_22904,var_22901,const_22902,var_22903,])
func_22911 = relay.Function([var_22901,var_22903,], output)
mod['func_22911'] = func_22911
mod = relay.transform.InferType()(mod)
mutated_mod['func_22911'] = func_22911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_22911_call = mutated_mod.get_global_var('func_22911')
var_22913 = relay.var("var_22913", dtype = "uint64", shape = (160,))#candidate|22913|(160,)|var|uint64
var_22914 = relay.var("var_22914", dtype = "float64", shape = (480, 1))#candidate|22914|(480, 1)|var|float64
call_22912 = func_22911_call(var_22913,var_22914,)
output = call_22912
func_22915 = relay.Function([var_22913,var_22914,], output)
mutated_mod['func_22915'] = func_22915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_22649_call = mod.get_global_var('func_22649')
func_22651_call = mutated_mod.get_global_var('func_22651')
call_22958 = func_22649_call()
call_22959 = func_22649_call()
output = call_22958
output2 = call_22959
func_22961 = relay.Function([], output)
mod['func_22961'] = func_22961
mod = relay.transform.InferType()(mod)
output = func_22961()
func_22962 = relay.Function([], output)
mutated_mod['func_22962'] = func_22962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13402_call = mod.get_global_var('func_13402')
func_13404_call = mutated_mod.get_global_var('func_13404')
call_22985 = relay.TupleGetItem(func_13402_call(), 5)
call_22986 = relay.TupleGetItem(func_13404_call(), 5)
func_13516_call = mod.get_global_var('func_13516')
func_13518_call = mutated_mod.get_global_var('func_13518')
var_22995 = relay.var("var_22995", dtype = "float64", shape = (432,))#candidate|22995|(432,)|var|float64
call_22994 = relay.TupleGetItem(func_13516_call(relay.reshape(var_22995.astype('float64'), [432,])), 2)
call_22996 = relay.TupleGetItem(func_13518_call(relay.reshape(var_22995.astype('float64'), [432,])), 2)
func_13858_call = mod.get_global_var('func_13858')
func_13859_call = mutated_mod.get_global_var('func_13859')
call_22997 = func_13858_call()
call_22998 = func_13858_call()
func_18887_call = mod.get_global_var('func_18887')
func_18889_call = mutated_mod.get_global_var('func_18889')
call_23029 = relay.TupleGetItem(func_18887_call(), 0)
call_23030 = relay.TupleGetItem(func_18889_call(), 0)
func_13402_call = mod.get_global_var('func_13402')
func_13404_call = mutated_mod.get_global_var('func_13404')
call_23054 = relay.TupleGetItem(func_13402_call(), 5)
call_23055 = relay.TupleGetItem(func_13404_call(), 5)
output = relay.Tuple([call_22985,call_22994,var_22995,call_22997,call_23029,call_23054,])
output2 = relay.Tuple([call_22986,call_22996,var_22995,call_22998,call_23030,call_23055,])
func_23077 = relay.Function([var_22995,], output)
mod['func_23077'] = func_23077
mod = relay.transform.InferType()(mod)
var_23078 = relay.var("var_23078", dtype = "float64", shape = (432,))#candidate|23078|(432,)|var|float64
output = func_23077(var_23078)
func_23079 = relay.Function([var_23078], output)
mutated_mod['func_23079'] = func_23079
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13876_call = mod.get_global_var('func_13876')
func_13878_call = mutated_mod.get_global_var('func_13878')
call_23095 = func_13876_call()
call_23096 = func_13876_call()
output = relay.Tuple([call_23095,])
output2 = relay.Tuple([call_23096,])
func_23149 = relay.Function([], output)
mod['func_23149'] = func_23149
mod = relay.transform.InferType()(mod)
output = func_23149()
func_23150 = relay.Function([], output)
mutated_mod['func_23150'] = func_23150
mutated_mod = relay.transform.InferType()(mutated_mod)
var_23151 = relay.var("var_23151", dtype = "float32", shape = (16, 13, 4))#candidate|23151|(16, 13, 4)|var|float32
uop_23152 = relay.log10(var_23151.astype('float32')) # shape=(16, 13, 4)
output = uop_23152
output2 = uop_23152
func_23156 = relay.Function([var_23151,], output)
mod['func_23156'] = func_23156
mod = relay.transform.InferType()(mod)
var_23157 = relay.var("var_23157", dtype = "float32", shape = (16, 13, 4))#candidate|23157|(16, 13, 4)|var|float32
output = func_23156(var_23157)
func_23158 = relay.Function([var_23157], output)
mutated_mod['func_23158'] = func_23158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17702_call = mod.get_global_var('func_17702')
func_17704_call = mutated_mod.get_global_var('func_17704')
call_23173 = relay.TupleGetItem(func_17702_call(), 0)
call_23174 = relay.TupleGetItem(func_17704_call(), 0)
func_10501_call = mod.get_global_var('func_10501')
func_10503_call = mutated_mod.get_global_var('func_10503')
const_23200 = relay.const([1.778807,-2.593581,5.679221,1.045984,-2.832753,8.860571,8.423542,5.289537,-6.011968,-2.439022,-5.979560,8.796453,-9.824891,5.136011,3.430829,-0.503023,8.785142,2.368059,-9.720730,3.767960,4.074514,6.583564,-3.404769,-5.111602,3.980544,6.602574,1.260253,-9.682361,-1.856259,9.985656,-1.590238,-3.213308,-9.274309,-0.458932,4.960276,-6.090075,-3.837785,9.414838,-5.093806,8.215011,-9.334717,9.620733,-9.097555,-8.617158,9.433664,-1.321752,7.383347,8.270369,-4.480296,-2.034988,2.245623,-8.143678,-2.222555,8.648306,5.147690,-2.756874,3.073962,9.113835,-3.216532,-5.648391,9.968433,5.299100,-3.927413,1.780864,-9.750412,-0.793363,-8.599790,1.594907,-7.117032,3.916490,-6.190445,1.133273,-1.862767,4.237601,-4.121745,-3.521212,-4.301895,4.080901,2.332789,-7.938100,-9.387018,7.020831,5.896070,-8.756983,7.114161,-1.918954,1.298131,-9.295363,-9.484132,-1.937663,3.470766,6.954168,-5.089589,-7.969030,4.068338,9.692570,8.412531,-4.059372,-6.772809,-2.667850,-1.113103,4.325363,1.950422,3.455499,5.046579,-8.202247,0.056908,-2.504874,-4.625599,9.533853,5.214279,-8.177002,1.785201,-4.165723,1.271785,-1.286542,6.805906,6.674061,9.322267,-9.583626,6.675257,8.347848,-9.383752,-0.499175,6.051398,-7.035770,0.955080,0.861745,2.376308,-2.314029,7.009616,3.283511,-6.319975,1.081334,0.218114,-7.932116,-7.246229,8.217339,9.373432,-9.516379,7.091328,-1.430465,7.413945,-0.769218,2.936001,0.321542,6.404870,2.330472,1.480725,1.331368,-8.834846,1.961333,5.844782,-3.350056,1.747062,6.789229,1.662832,3.018679,-9.207292,-2.903188,-0.349264,-3.239828,-5.272402,7.996528,-2.341918,-0.942035,-7.255152,3.940958,9.388379,-1.013508,-9.106466,6.331545,4.743290,-3.531089,-9.812087,9.093589,-3.817077,-2.308317,1.368726,3.344501,-6.176255,2.775203,0.308757,8.597959,-4.098216,7.295375,0.513268,-9.882373,0.537987,-2.613445,8.119164,-6.964379,2.252737,-0.470301,-3.080044,-2.848161,-2.600643,0.379427,4.076967,-2.775083,6.726596,-6.294855,-8.542407,2.263520,-9.958282,-6.150376,-8.404309,1.850283,6.556793,-2.006418,5.073729,9.806138,-4.617135,-1.382431,0.870481,2.257691,-9.047707,3.407064,5.913567,4.777069,6.950270,2.188963,-0.977739,2.545319,9.018348,-5.145919,6.461815,-1.647046,-9.877698,9.834845,2.273761,-4.041755,-6.420619,-0.495695,7.904479,5.396044,3.430684,-2.370427,-8.239765,-8.611240,6.104038,-4.038063,-7.401618,4.451639,2.155341,-9.626860,9.264071,5.190799,-9.234411,4.652205,4.901804,-9.770230,-0.943265,-6.691262,1.401321,-1.559459,8.391989,8.740458,3.861200,0.995543,4.273327,1.797222,-0.030126,-3.200712,-8.864572,-8.688874,4.467246,4.216341,6.045293,-9.064999,-5.407093,-1.170826,9.189464,1.687144,-2.832394,-4.146797,-8.921114,-7.416071,-4.391056,4.603649,7.264380,-3.763503,5.505953,-7.605111,2.224107,9.674213,7.366912,-2.964550,3.314616,3.605437,-3.922638,6.094924,5.057536,0.308315,-9.090574,-8.911223,8.671453,-6.324029,-3.484502,9.339824,0.229255,8.273918,-0.605771,-4.825696,3.246797,7.333003,4.896725,-8.221154,4.305970,-1.830677,2.554001,6.486568,2.942102,3.873637,-2.051098,6.002962,9.853570,-4.324582,-7.333146,8.483371,-4.703890,2.150180,4.468886,-3.363176,-0.268415,-2.650755,3.957690,-1.510915,-3.230700,3.936116,-3.458383,-6.806711,7.988605,-0.198801,9.061898,-1.117495,-5.005927,6.634543,2.169136,-1.480608,-8.329333,7.797975,-9.758790,-3.527479,9.883698,1.216649,7.937269,0.836514,-3.538920,-5.672407,4.813185,9.115621,9.117260,4.258449,-6.435374,-4.449794,4.500486,2.837186,8.458985,-5.955535,9.920033,-6.019868,6.359224,5.969779,8.225451,-2.920819,-0.439405,0.552870,-1.864511,8.595190,-0.421044,-8.434125,3.733386,-7.996289,1.547514,-1.799018,-1.040728,1.475202,-0.258087,-1.231718,3.886351,0.486694,-3.722585,9.774318,9.901105,-5.167943,-1.433429,5.845357,-0.241433,-0.194819,-6.763197,-4.754966,1.840480,3.855856,-4.370809,-8.568185,-7.123260,-4.681397,-2.434494,5.718485,-1.442480,7.347972,-2.554418,-9.944625,-7.674142,2.676319,3.298800,-6.845070,3.785466,0.560303,5.644946,7.394792,4.890483,-9.171855,6.367023,4.277114,6.074266,-7.742915,-1.079739,-2.535476,6.051143,4.842162,1.759671,-0.945719,2.288903,4.674639,8.614819,-3.506962,-9.639899,-8.306363,0.194673,3.840247,-9.853179,-4.259889,-3.446921,-3.324402,-7.738163,4.244296,8.075155,0.822828,4.064883,8.544947,1.050476,2.601769,-3.176263,-7.105152,8.996554,1.805564,1.270854,-2.596135,-4.219339,-3.900210,6.474140,2.243586,8.920491,2.205177,0.825758,9.321580,5.744702,-0.161403,-7.994446,1.147300,-5.331338,9.174805,-4.864297,7.081272,-5.377120,-0.037175,7.633021,-9.648483,-4.421149,9.898082,-0.762251,-0.605622,6.784326,-5.750848,7.432105,-4.486652,-9.495539,-6.272594,1.042192,9.655094,3.365086,2.284265,5.636073,1.441346,-5.198969,9.716634,2.837186,-3.341336,-1.202542,-1.374119,-2.277717,4.507142,-4.357806,7.520016,-5.375015,-7.109144,-0.120030,-8.468240,5.442794,0.657178,5.840705,7.330169,3.753025,3.827694,-3.351704,0.554685,-3.592987,9.497087,-4.769494,3.625881], dtype = "float64")#candidate|23200|(512,)|const|float64
call_23199 = func_10501_call(relay.reshape(const_23200.astype('float64'), [2, 16, 16]))
call_23201 = func_10501_call(relay.reshape(const_23200.astype('float64'), [2, 16, 16]))
func_14638_call = mod.get_global_var('func_14638')
func_14643_call = mutated_mod.get_global_var('func_14643')
const_23206 = relay.const([4.174481,-7.629991,-3.615189,7.029706,-9.670615,4.242604,8.590405,-9.999718,9.809280,4.983056,5.473154,8.843243,7.570385,2.686599,8.802530,4.151192,-3.674698,-0.168573,5.388427,7.266928,-8.047219,5.670291,-0.073915,3.583488,1.441791,1.302096,-0.195926,6.729570,6.167982,-8.878969,9.253689,9.349913,2.197186,-8.600224,1.277545,-1.696294,-4.578932,7.691495,-1.006111,-4.546916,-9.583475,-9.874038,8.769850,-8.193953,0.608867,5.348042,-5.935789,-5.504165,-8.083541,-4.055176,-8.304704,9.388757,-3.687718,7.368228,-5.186025,7.050180,-4.066633,9.708657,1.819975,-5.416570,-6.799036,0.528748,-8.136722,-3.338973,-1.013509,1.164683,2.654423,-0.891467,2.031529,-9.527516,1.706215,-8.441403,-7.179583,0.688840,4.979884,-4.826586,6.935991,-3.539804,0.585696,2.720835,-5.445447,-3.789933,8.779770,1.317537,-7.740594,-2.417249,5.410170,1.871902,-0.907024,4.246804,-0.915425,6.884802,5.554969,-5.264043,-2.256790,9.124104,-0.021934,7.415999,-5.240310,-4.877000,-9.263792,-1.926685,-4.056732,0.563989,5.756143,-2.455205,-5.904013,0.830866,-1.814404,-8.253869,7.182145,0.958553,7.254722,-1.762547,5.048775,8.855384,1.539954,-8.353881,3.849827,6.801002,-3.442849,6.269458,0.459680,9.384519,-3.481450,2.023915,6.761841,5.522365,5.071122,-3.323574,-0.665852,-2.297339,1.300904,3.923091,4.376643,5.854047,5.074472,-1.803277,-8.440254,-4.065679,-0.286172,-1.095184,-2.757552,-6.885763,2.456611,-7.370542,-0.121061,-8.897027,7.427174,5.246220,-3.875430,1.483114,5.945747,-4.169223,4.876238,-8.684132,-6.483280,7.848842,-9.450069,-7.387358,-3.785298,3.127778,-7.297862,-2.227899,-8.721664,-5.025512,2.645874,-8.678597,0.806049,-9.086248,3.114821,-6.455579,3.910069,-3.981252,-1.714108,-2.941875,1.050736,4.396668,9.808600,-5.075376,5.330279,-4.510858,-1.112988,9.072505,5.990239,-6.327611,-7.757496,2.427209,-7.081590,2.240122,-1.027527,7.775666,-6.914174,7.224670,-1.809697,6.090288,-4.045325,-9.892752,-0.495527,4.616337,8.838518,-2.627110,-2.139394,-7.154678,0.745596,1.756274,9.228903,8.085409,-3.947313,3.751297,-8.802550,-2.398432,-0.625202,7.843635,2.638668,-0.840454,-9.296520,-0.729528,-0.266167,3.236304,0.398333,-6.627932,7.670597,-3.365848,-7.374723,2.272243,-0.836416,-1.880305,-1.879251,2.908253,-1.237141,2.387184,-1.709936,6.826555,-2.147869,-1.866694,-9.496073,-8.863817,-3.395372,7.663413,-8.739592,-8.992289,-5.051333,7.692650,-4.241812,-9.897820,-5.797219,-5.673537,-3.551868,-7.962520,-5.448349,-8.956972,3.652402,3.933215,2.024532,-1.393196,7.808668,-4.799372,3.916244,-0.526336,-7.752664,-1.562968,-2.609771,8.421675], dtype = "float64")#candidate|23206|(264,)|const|float64
const_23207 = relay.const([-9.065455,-5.643915,-0.426100,9.090313,-3.692849,2.139860,-2.418727,6.245212,9.838983,-9.756334,2.224141,7.242466,6.691645,-9.784886,-7.731795,-2.351178,9.800234,-3.082837,-4.638190,4.841303,8.196121,-6.011273,-3.944401,-4.592574,-6.777743,5.434764,2.890257,7.795286,0.770640,8.668485,-9.105452,-7.371918,-6.236865,8.719888,-5.628151,0.178034,-0.378592,-8.464907,-7.497080,-0.402844,3.897450,-7.079855,-9.151197,3.542805,6.363917,2.197303,-3.334080,1.028994,-4.895724,-5.268487,1.502976,9.654229,6.938113,-1.403547,-6.311350,-8.244630,-7.145671,-7.993303,9.722357,-9.700703,2.309037,-4.306605,0.625957,-5.180253,-6.277860,-2.127668,6.483442,3.026718,6.404434,-9.503983,7.713740,7.713631,8.303025,-0.179840,0.143997,2.484717,8.413537,6.033168,9.417774,-6.826173,-9.748101,4.872060,-8.344713,-3.613626,-6.679128,7.482688,-7.687843,8.364965,2.024635,-7.017151,-5.611770,9.750591,4.442934,-5.581992,-4.592476,-8.804909,6.311286,-2.850165,6.918668,-7.303610,4.060906,8.988740,-8.283694,4.316719,-0.954591,7.193621,1.835199,-7.919787,1.743795,4.531807,-7.715680,-1.307589,6.178977,0.749962,2.056417,-0.010794,-6.009302,-2.989803,-1.003500,-6.823480,9.316186,5.238777,-7.509472,7.563324,-3.157880,9.598915,9.960247,0.073582,1.998187,6.611440,-7.161036,7.458399,4.108766,8.950502,-5.357959,-6.808851,5.527138,-7.609178,-0.555057,2.680258,0.814563,3.637461,-2.723230,9.428865,7.821812,2.243871,6.048217,-4.724778,-9.114725,-5.445564,7.866432,1.070566,4.130113,-5.288767,5.690322,-5.878055,2.445361,5.419585,-6.064333,6.899065,5.419946,9.567459,0.304168,4.301182,-9.984560,-4.369654,9.158108,-3.826733,-4.359542,-9.575353,3.705949,-8.360243,-6.207462,-3.556167,-2.284372,-4.803847,-3.349549,-9.427750,-5.345477,-2.942252,-0.572100,-8.123677,-2.952840,-3.561369,-6.373793,-4.392476,7.498638,-1.593747,1.536807,6.272331,-4.823455,6.763903,9.560159,-5.217475,-9.581314,-6.119178,-1.551083,-2.619184,-3.261775,3.158186,3.108514,-2.313171,-8.561423,-1.151692,9.444919,3.549820,8.018458,7.100175,4.755904,-1.701233,-5.700308,-9.868518,-7.986117,6.268331,0.559562,3.479112,-4.802777,6.516553,-6.510939,-8.678938,1.509010,0.354170,4.360595,-2.490457,-6.168706,-3.467652,1.996626,0.425002,9.609505,-0.641952,1.758714,4.092582,7.374641,-7.200731,-1.184936,-0.196073,1.448159,-6.766879,-0.861570,7.963429,-5.599724,7.928509,-9.936524,6.228118,9.953066,-6.338825,7.160524,-5.471547,-5.625243,-0.316772,-4.555719,4.725650,-2.234878,-8.047265,-0.261823,5.390594,5.739917,-2.015485,-2.672196,7.921963,-9.379372,-3.106337,2.797549,-8.523405,-4.967823,-9.028858,3.396750,-2.795973,7.050835,-0.965757,-0.085098,-9.705614,-0.343681,1.626654,-8.998522,-9.959362,-5.785801,-4.004025,-8.525846,8.974736,9.569165,9.833769,7.089509,-7.208797,-9.439409,-5.289065,0.582891,-8.405036,-8.576401,-2.003387,-1.819878,9.573109,5.808729,-8.922788,-8.847911,-6.468759,3.101171,3.095513,1.565035,2.271033,-7.199769,-1.449999,6.470956,-1.504991,-9.421777,-6.946765,9.544250,7.243810,-8.623979,-2.606507,-3.238364,-8.424202,-2.375486,-9.825292,-2.274935,5.846285,-0.764970,-8.257556,-2.418235,9.484893,2.654135,2.669839,0.565881,1.295899,-8.226653,-7.020102,8.335386,-3.958526,-4.872164,7.588428,3.665159,-5.290679,4.192781,2.871146,3.890445,-1.151974], dtype = "float32")#candidate|23207|(336,)|const|float32
var_23208 = relay.var("var_23208", dtype = "float64", shape = (1008,))#candidate|23208|(1008,)|var|float64
const_23209 = relay.const([False,True,False,True,False,True,False,True,False,True,True,False,False,True,False,True,True,False,True,False,True,True,True,True,True,True,False,False,False,False,True,False,True,True,True,False,False,True,True,False,True,True,False,True,False,False,False,True,True,True,False,False,False,True,True,True,True,True,False,True,False,True,True,True,False,False,True,False,False,True,False,True,False,False,False,False,False,False,False,True,False,False,True,False,True,False,False,False,False,False,True,False,True,False,True,True,True,True,True,True,False,True,False,False,True,False,False,True,False,False,True,False,False,False,True,False,True,True,False,True,True,False,True,False,False,False,True,True,True,False,False,True,True,False,True,False,False,False,True,True,False,False,True,True,True,False,True,False,True,True,True,False,True,False,False,False,False,True,True,False,True,False,True,False,False,True,False,True,True,False,False,True,False,True,False,True,False,True,True,True,True,False,False,False,False,False,False,True,False,False,True,True,False,False,False,False,True,False,True,False,False,True,False,True,True,False,False,True,False,False,False,True,False,False,True,True,True,False,False,True,False,True,False,False,True,False,False,True,True,False,True,True,True,True,False,False,False,True,True,False,True,False,True,True,False,False,False,True,False,False,False,False,True,True,False,True,True,True,False,False,True,True,False,False,True,False,True,True,True,False,True,False,False,False,False,True,False,False,False,True,True,True,True,False,False,False,True,True,True,True,False,False,True,False,False,False,False,True,True,False,False,False,False,False,False,False,True,False,True,False,True,False,True,True,False,True,True,False,False,False,True,False,False,False,False,False,False,True,False,True,True,False,True,True,False,True,False,False,False,True,False,True,True,True,False,True,False,True,True,False,True,True,True,True,True,True,False,False,False,False,True,True,False,True,True,False,False,True,False,False,False,False,False,True,True,False,False,True,False,False,False,True,True,True,True,False,False,True,False,True,True,False,False,True,True,True,True,True,False,False,False,False,False,False,True,False,False,False,True,False,False,True,False,True,False,True,True,True,False,False,False,True,False,False,False,True,False,True,False,False,True,False,True,False,False,False,False,True,False,True,True,False,True,True,True,True,False,True,False,False,True,False,True,True,True,True,False,True,True,False,True,False,True,False,False,True,True,False,False,True,False,False,False,True,True,True,False,False,False,True,False,True,True,False,False,False,True,False,True,False,True,True,True,False,True,True,True,False,False,False,False,False,False,False], dtype = "bool")#candidate|23209|(504,)|const|bool
call_23205 = relay.TupleGetItem(func_14638_call(relay.reshape(const_23206.astype('float64'), [264,]), relay.reshape(const_23207.astype('float32'), [336,]), relay.reshape(var_23208.astype('float64'), [2, 504]), relay.reshape(const_23209.astype('bool'), [504,]), ), 6)
call_23210 = relay.TupleGetItem(func_14643_call(relay.reshape(const_23206.astype('float64'), [264,]), relay.reshape(const_23207.astype('float32'), [336,]), relay.reshape(var_23208.astype('float64'), [2, 504]), relay.reshape(const_23209.astype('bool'), [504,]), ), 6)
var_23216 = relay.var("var_23216", dtype = "float64", shape = (2, 16, 16))#candidate|23216|(2, 16, 16)|var|float64
bop_23217 = relay.logical_xor(call_23199.astype('uint8'), relay.reshape(var_23216.astype('uint8'), relay.shape_of(call_23199))) # shape=(2, 16, 16)
bop_23220 = relay.logical_xor(call_23201.astype('uint8'), relay.reshape(var_23216.astype('uint8'), relay.shape_of(call_23201))) # shape=(2, 16, 16)
uop_23226 = relay.cosh(bop_23217.astype('float32')) # shape=(2, 16, 16)
uop_23228 = relay.cosh(bop_23220.astype('float32')) # shape=(2, 16, 16)
output = relay.Tuple([call_23173,const_23200,call_23205,const_23206,const_23207,var_23208,const_23209,uop_23226,])
output2 = relay.Tuple([call_23174,const_23200,call_23210,const_23206,const_23207,var_23208,const_23209,uop_23228,])
func_23236 = relay.Function([var_23208,var_23216,], output)
mod['func_23236'] = func_23236
mod = relay.transform.InferType()(mod)
mutated_mod['func_23236'] = func_23236
mutated_mod = relay.transform.InferType()(mutated_mod)
func_23236_call = mutated_mod.get_global_var('func_23236')
var_23238 = relay.var("var_23238", dtype = "float64", shape = (1008,))#candidate|23238|(1008,)|var|float64
var_23239 = relay.var("var_23239", dtype = "float64", shape = (2, 16, 16))#candidate|23239|(2, 16, 16)|var|float64
call_23237 = func_23236_call(var_23238,var_23239,)
output = call_23237
func_23240 = relay.Function([var_23238,var_23239,], output)
mutated_mod['func_23240'] = func_23240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18580_call = mod.get_global_var('func_18580')
func_18582_call = mutated_mod.get_global_var('func_18582')
call_23257 = func_18580_call()
call_23258 = func_18580_call()
func_14417_call = mod.get_global_var('func_14417')
func_14418_call = mutated_mod.get_global_var('func_14418')
call_23269 = relay.TupleGetItem(func_14417_call(), 0)
call_23270 = relay.TupleGetItem(func_14418_call(), 0)
output = relay.Tuple([call_23257,call_23269,])
output2 = relay.Tuple([call_23258,call_23270,])
func_23274 = relay.Function([], output)
mod['func_23274'] = func_23274
mod = relay.transform.InferType()(mod)
output = func_23274()
func_23275 = relay.Function([], output)
mutated_mod['func_23275'] = func_23275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12669_call = mod.get_global_var('func_12669')
func_12670_call = mutated_mod.get_global_var('func_12670')
call_23303 = func_12669_call()
call_23304 = func_12669_call()
func_19487_call = mod.get_global_var('func_19487')
func_19491_call = mutated_mod.get_global_var('func_19491')
const_23321 = relay.const([-3,1,3,-1,-9,-9,-7,4,-7,-8,3,10,-3,10,-10,8,-4,-5,9,5,8,2,-8,-5,9,3,-3,8,9,-2,10,2,-8,-4,-5,-7,-2,10,5,6,-9,8,3,9,-3,-1,-2,-9,-2,-7,4,1,5,8,7,4,5,1,7,8,-3,-4,-5,-5,-8,5,-8,-9,-10,-1,-3,6,-6,-3,-6,-2,3,-2,-9,-5,-1,10,-9,-2,-8,-7,-7,-6,-7,-5,-2,-2,5,1,-10,2,9,9,-2,4,-4,-10,3,6,-5,-2,10,-1,-7,10,1,9,5,-5,-10,7,-1,7,-5,3,-3,-8,-1,9,-3,5,10,-5,3,4,-10,-7,9,6,-6,5,-6,-2,2,-4,10,-3,7,-7,-8,4,-3,-1,-5,-8,6,10,-6,10,6,5,5,-6,5,-3], dtype = "uint64")#candidate|23321|(160,)|const|uint64
var_23322 = relay.var("var_23322", dtype = "float64", shape = (4, 208))#candidate|23322|(4, 208)|var|float64
const_23323 = relay.const([8.191557,-3.174646,3.692274,-7.864214,2.171927,3.011688,9.365682,3.227935,-0.408325,9.092045,4.277753,1.602167,-5.781722,5.541424,-9.349782,8.327696,8.837322,9.847272,8.669960,5.069986,-6.438379,-7.455513,-7.663088,-4.451930,-9.816338,9.476306,-3.898888,3.735060,6.148285,-2.006839,-9.970076,5.872561,8.804963,-6.639799,0.926021,8.485632,-3.305997,8.404790,-6.256471,-1.687474,-2.889901,-4.985124,-0.612248,6.863899,-1.599786,-8.096814,7.839835,7.147634,-6.860910,-8.006633,0.948767,4.577526,8.374241,-8.943969,2.187591,3.917363,3.253177,-8.657978,4.133440,3.504266,2.697323,-2.080554,-2.492309,2.504683,-7.877643,-7.046677,2.304353,9.615063,-0.772242,-8.069194,-6.419667,6.842676,2.797505,-8.106261,-8.042275,6.052171,1.086365,-7.855133,1.509481,-9.384640,8.946517,2.353645,-6.205097,-3.160944,0.580202,-3.152498,-1.878654,1.963498,7.816791,-2.180008,1.591942,1.946215,-9.135509,-1.853696,4.907792,7.564894,2.262404,-4.800767,4.154248,3.144047,3.143907,9.593880,0.198146,-9.288591,-6.974621,-6.573136,-2.691045,-0.762949,-1.541107,-7.904133,9.234559,-1.076222,-6.059331,-4.004561,4.423815,-3.714442,-0.936879,-0.586607,-1.769377,-3.216731,-1.708044,5.904477,7.873622,1.503453,-9.807031,7.465819,3.657641,7.879806,-1.504327,7.984819,6.139657,6.536224,0.849496,2.229184,-2.078972,-5.479857,4.515079,6.563137,5.067141,-1.159853,-1.735531,4.772373,0.500436,3.868883,5.031669,-8.633914,9.448957,-3.090783,3.162116,-5.988882,4.222232,-7.704877,-9.250925,0.310185,-8.265553,-4.792122,-7.903234,-5.309795,-8.322911,6.389599,7.141671,-8.560305,6.622667,0.426887,-3.485315,-1.740566,6.468452,-6.955606,-8.004456,5.548399,9.212214,6.734096,-2.904843,-6.981018,-8.593325,-6.303972,4.136250,-7.723963,6.767471,1.544490,5.313278,6.875399,5.876597,1.060758,-5.670907,-1.747804,-1.342080,0.664472,-4.463054,7.700310,5.661688,-2.296769,-4.088997,-1.866433,-2.693961,3.510862,1.457207,-1.317459,5.588597,2.785182,0.082484,2.727835,0.778783,-8.398193,-5.104824,-1.366221,2.547368,-3.605504,4.929122,7.357454,1.688360,-0.833851,5.169048,2.857775,-5.077301,-5.884178,-9.237365,3.248812,-7.638445,8.986026,1.967722,1.470088,-4.696851,-7.749895,-9.841221,-2.295664,-6.510915,-0.193771,9.590916,-2.954749,-9.482733,7.660028,6.788556,7.819769,-0.342851,-0.407712,-8.895424,-8.047582,-8.666165,9.482376,-9.198954,-0.951773,-0.374274,9.507050,-0.375300,2.013938,-8.036256,3.543753,5.229584,-8.616940,-7.342037,2.986630,-6.330844,9.672963,-3.414755,3.493665,-3.261596,2.115105,-4.325726,2.071214,7.358265,-7.135744,2.124285,8.124211,-8.117593,6.184240,-0.371422,2.986802,-3.688668,7.497780,6.511374,-7.571315,-8.900967,-2.348327,-7.246656,8.135943,-9.325544,2.877563,-1.080301,-3.484124,-9.530118,3.736949,-3.655962,6.066752,7.505707,2.088473,2.073052,7.820391,-8.710613,6.023127,7.779242,-2.818111,-4.224192,8.251518,-7.846594,3.926199,0.613601,1.921326,6.146922,9.274796,-8.922669,-7.245764,-3.134243,2.176387,8.222630,0.915758,-7.389644,6.366707,3.348897,0.352684,-2.563471,7.248753,2.438127,-5.801142,8.863396,6.533019,-6.018564,-3.467478,3.935908,3.225387,-9.077289,6.449911,-7.166854,0.655333,-0.802155,4.438528,8.730577,-6.621641,-6.349618,6.215561,-5.769335,9.972741,-8.017741,8.312252,4.648459,7.212456,3.998361,-3.305135,4.510470,-1.419448,-4.617864,-6.128031,-8.973734,-3.532274,9.395655,-5.953129,5.397188,8.948209,8.008200,3.598113,6.052018,-6.521008,-7.536570,3.127842,-8.823549,4.059979,7.504739,-3.071893,-4.498571,-9.387792,1.877285,-3.484915,-9.601710,-1.261846,-4.545616,1.769803,-5.389660,3.805361,-8.281147,-8.644354,-1.901448,-2.038878,-9.912846,8.112804,5.669014,-6.214409,-2.614498,7.119199,-4.370997,6.025298,-3.103707,8.292864,-3.566810,5.390412,0.818048,-6.049085,1.778973,4.298712,0.999547,-6.650639,1.442297,6.605315,0.580045,-0.915358,8.086300,5.987804,-4.701624,-6.077408,2.938979,-5.638377,-8.583089,-6.113224,8.433667,6.807198,-7.810571,2.564823,-2.517946,3.707959,-4.731836,-1.500981,5.864050,5.858157,-8.327093,8.307265,2.826475,-2.253061,-5.676015,6.394922,-9.162945,-1.258841,-2.724420,-5.135523,3.749987,3.290500,-5.392490,7.848483,0.972939,0.877784,-8.495793,1.486647,-9.536678,4.785112,-5.243800,-8.483541,3.098026,8.016179,4.416542,3.128320,4.302460,-8.042449,-9.031255,-9.654904,-3.988344,9.557694,-3.530051,-1.913449,-1.675500,7.245295,-5.016679,8.801001,-3.150351,1.918968,0.839452,-8.389748,7.436832,-1.279664,-1.221511,5.643117,-8.017278,-5.805957,7.680328,-7.748516,-0.154937,-6.808992,1.781835,6.810564,-3.314895,8.847426,4.905369,3.628867,-3.590889,-6.801339,-0.342391,9.494314,-7.297767,1.497198,-2.709186,9.867307,0.359003,1.096154], dtype = "float64")#candidate|23323|(480,)|const|float64
call_23320 = relay.TupleGetItem(func_19487_call(relay.reshape(const_23321.astype('uint64'), [160,]), relay.reshape(var_23322.astype('float64'), [832,]), relay.reshape(const_23323.astype('float64'), [480,]), ), 5)
call_23324 = relay.TupleGetItem(func_19491_call(relay.reshape(const_23321.astype('uint64'), [160,]), relay.reshape(var_23322.astype('float64'), [832,]), relay.reshape(const_23323.astype('float64'), [480,]), ), 5)
func_11095_call = mod.get_global_var('func_11095')
func_11096_call = mutated_mod.get_global_var('func_11096')
call_23327 = func_11095_call()
call_23328 = func_11095_call()
output = relay.Tuple([call_23303,call_23320,const_23321,var_23322,const_23323,call_23327,])
output2 = relay.Tuple([call_23304,call_23324,const_23321,var_23322,const_23323,call_23328,])
func_23334 = relay.Function([var_23322,], output)
mod['func_23334'] = func_23334
mod = relay.transform.InferType()(mod)
mutated_mod['func_23334'] = func_23334
mutated_mod = relay.transform.InferType()(mutated_mod)
var_23335 = relay.var("var_23335", dtype = "float64", shape = (4, 208))#candidate|23335|(4, 208)|var|float64
func_23334_call = mutated_mod.get_global_var('func_23334')
call_23336 = func_23334_call(var_23335)
output = call_23336
func_23337 = relay.Function([var_23335], output)
mutated_mod['func_23337'] = func_23337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18601_call = mod.get_global_var('func_18601')
func_18602_call = mutated_mod.get_global_var('func_18602')
call_23367 = relay.TupleGetItem(func_18601_call(), 2)
call_23368 = relay.TupleGetItem(func_18602_call(), 2)
func_20068_call = mod.get_global_var('func_20068')
func_20069_call = mutated_mod.get_global_var('func_20069')
call_23372 = func_20068_call()
call_23373 = func_20068_call()
var_23379 = relay.var("var_23379", dtype = "uint16", shape = (1092,))#candidate|23379|(1092,)|var|uint16
bop_23380 = relay.subtract(call_23367.astype('float64'), relay.reshape(var_23379.astype('float64'), relay.shape_of(call_23367))) # shape=(1092,)
bop_23383 = relay.subtract(call_23368.astype('float64'), relay.reshape(var_23379.astype('float64'), relay.shape_of(call_23368))) # shape=(1092,)
func_17702_call = mod.get_global_var('func_17702')
func_17704_call = mutated_mod.get_global_var('func_17704')
call_23386 = relay.TupleGetItem(func_17702_call(), 0)
call_23387 = relay.TupleGetItem(func_17704_call(), 0)
output = relay.Tuple([call_23372,bop_23380,call_23386,])
output2 = relay.Tuple([call_23373,bop_23383,call_23387,])
func_23388 = relay.Function([var_23379,], output)
mod['func_23388'] = func_23388
mod = relay.transform.InferType()(mod)
var_23389 = relay.var("var_23389", dtype = "uint16", shape = (1092,))#candidate|23389|(1092,)|var|uint16
output = func_23388(var_23389)
func_23390 = relay.Function([var_23389], output)
mutated_mod['func_23390'] = func_23390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11095_call = mod.get_global_var('func_11095')
func_11096_call = mutated_mod.get_global_var('func_11096')
call_23415 = func_11095_call()
call_23416 = func_11095_call()
func_15065_call = mod.get_global_var('func_15065')
func_15066_call = mutated_mod.get_global_var('func_15066')
call_23440 = func_15065_call()
call_23441 = func_15065_call()
output = relay.Tuple([call_23415,call_23440,])
output2 = relay.Tuple([call_23416,call_23441,])
func_23455 = relay.Function([], output)
mod['func_23455'] = func_23455
mod = relay.transform.InferType()(mod)
mutated_mod['func_23455'] = func_23455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_23455_call = mutated_mod.get_global_var('func_23455')
call_23456 = func_23455_call()
output = call_23456
func_23457 = relay.Function([], output)
mutated_mod['func_23457'] = func_23457
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12956_call = mod.get_global_var('func_12956')
func_12958_call = mutated_mod.get_global_var('func_12958')
call_23458 = relay.TupleGetItem(func_12956_call(), 0)
call_23459 = relay.TupleGetItem(func_12958_call(), 0)
func_12617_call = mod.get_global_var('func_12617')
func_12619_call = mutated_mod.get_global_var('func_12619')
call_23490 = func_12617_call()
call_23491 = func_12617_call()
output = relay.Tuple([call_23458,call_23490,])
output2 = relay.Tuple([call_23459,call_23491,])
func_23492 = relay.Function([], output)
mod['func_23492'] = func_23492
mod = relay.transform.InferType()(mod)
mutated_mod['func_23492'] = func_23492
mutated_mod = relay.transform.InferType()(mutated_mod)
func_23492_call = mutated_mod.get_global_var('func_23492')
call_23493 = func_23492_call()
output = call_23493
func_23494 = relay.Function([], output)
mutated_mod['func_23494'] = func_23494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17630_call = mod.get_global_var('func_17630')
func_17632_call = mutated_mod.get_global_var('func_17632')
call_23495 = relay.TupleGetItem(func_17630_call(), 0)
call_23496 = relay.TupleGetItem(func_17632_call(), 0)
output = relay.Tuple([call_23495,])
output2 = relay.Tuple([call_23496,])
func_23513 = relay.Function([], output)
mod['func_23513'] = func_23513
mod = relay.transform.InferType()(mod)
mutated_mod['func_23513'] = func_23513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_23513_call = mutated_mod.get_global_var('func_23513')
call_23514 = func_23513_call()
output = call_23514
func_23515 = relay.Function([], output)
mutated_mod['func_23515'] = func_23515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11804_call = mod.get_global_var('func_11804')
func_11806_call = mutated_mod.get_global_var('func_11806')
call_23532 = relay.TupleGetItem(func_11804_call(), 0)
call_23533 = relay.TupleGetItem(func_11806_call(), 0)
func_21648_call = mod.get_global_var('func_21648')
func_21649_call = mutated_mod.get_global_var('func_21649')
call_23553 = relay.TupleGetItem(func_21648_call(), 0)
call_23554 = relay.TupleGetItem(func_21649_call(), 0)
output = relay.Tuple([call_23532,call_23553,])
output2 = relay.Tuple([call_23533,call_23554,])
func_23569 = relay.Function([], output)
mod['func_23569'] = func_23569
mod = relay.transform.InferType()(mod)
mutated_mod['func_23569'] = func_23569
mutated_mod = relay.transform.InferType()(mutated_mod)
func_23569_call = mutated_mod.get_global_var('func_23569')
call_23570 = func_23569_call()
output = call_23570
func_23571 = relay.Function([], output)
mutated_mod['func_23571'] = func_23571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16813_call = mod.get_global_var('func_16813')
func_16814_call = mutated_mod.get_global_var('func_16814')
call_23644 = func_16813_call()
call_23645 = func_16813_call()
func_11833_call = mod.get_global_var('func_11833')
func_11835_call = mutated_mod.get_global_var('func_11835')
call_23661 = relay.TupleGetItem(func_11833_call(), 0)
call_23662 = relay.TupleGetItem(func_11835_call(), 0)
output = relay.Tuple([call_23644,call_23661,])
output2 = relay.Tuple([call_23645,call_23662,])
func_23666 = relay.Function([], output)
mod['func_23666'] = func_23666
mod = relay.transform.InferType()(mod)
mutated_mod['func_23666'] = func_23666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_23666_call = mutated_mod.get_global_var('func_23666')
call_23667 = func_23666_call()
output = call_23667
func_23668 = relay.Function([], output)
mutated_mod['func_23668'] = func_23668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14750_call = mod.get_global_var('func_14750')
func_14752_call = mutated_mod.get_global_var('func_14752')
call_23713 = relay.TupleGetItem(func_14750_call(), 1)
call_23714 = relay.TupleGetItem(func_14752_call(), 1)
func_20992_call = mod.get_global_var('func_20992')
func_20993_call = mutated_mod.get_global_var('func_20993')
call_23719 = func_20992_call()
call_23720 = func_20992_call()
func_15257_call = mod.get_global_var('func_15257')
func_15258_call = mutated_mod.get_global_var('func_15258')
call_23728 = relay.TupleGetItem(func_15257_call(), 1)
call_23729 = relay.TupleGetItem(func_15258_call(), 1)
output = relay.Tuple([call_23713,call_23719,call_23728,])
output2 = relay.Tuple([call_23714,call_23720,call_23729,])
func_23747 = relay.Function([], output)
mod['func_23747'] = func_23747
mod = relay.transform.InferType()(mod)
output = func_23747()
func_23748 = relay.Function([], output)
mutated_mod['func_23748'] = func_23748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_22320_call = mod.get_global_var('func_22320')
func_22321_call = mutated_mod.get_global_var('func_22321')
call_23824 = func_22320_call()
call_23825 = func_22320_call()
output = relay.Tuple([call_23824,])
output2 = relay.Tuple([call_23825,])
func_23832 = relay.Function([], output)
mod['func_23832'] = func_23832
mod = relay.transform.InferType()(mod)
mutated_mod['func_23832'] = func_23832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_23832_call = mutated_mod.get_global_var('func_23832')
call_23833 = func_23832_call()
output = call_23833
func_23834 = relay.Function([], output)
mutated_mod['func_23834'] = func_23834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20019_call = mod.get_global_var('func_20019')
func_20020_call = mutated_mod.get_global_var('func_20020')
call_23842 = relay.TupleGetItem(func_20019_call(), 1)
call_23843 = relay.TupleGetItem(func_20020_call(), 1)
output = call_23842
output2 = call_23843
func_23844 = relay.Function([], output)
mod['func_23844'] = func_23844
mod = relay.transform.InferType()(mod)
output = func_23844()
func_23845 = relay.Function([], output)
mutated_mod['func_23845'] = func_23845
mutated_mod = relay.transform.InferType()(mutated_mod)
var_23921 = relay.var("var_23921", dtype = "float32", shape = (3, 1, 9))#candidate|23921|(3, 1, 9)|var|float32
uop_23922 = relay.atanh(var_23921.astype('float32')) # shape=(3, 1, 9)
func_21796_call = mod.get_global_var('func_21796')
func_21799_call = mutated_mod.get_global_var('func_21799')
var_23933 = relay.var("var_23933", dtype = "float64", shape = (264,))#candidate|23933|(264,)|var|float64
const_23934 = relay.const([0.651787,-9.039387,-2.293046,-9.660229,-5.064368,-1.644668,9.020377,1.362852,-1.707568,-8.807230,0.132582,-0.411468,0.685624,8.402968,3.870544,4.793330,4.580721,-2.136698,-5.801051,7.414896,8.351578,3.012059,2.039003,-6.207099,-0.025279,-0.429989,-1.005524,8.327807,-2.465120,-1.568833,7.783439,-2.774000,9.197921,-7.117198,6.482876,-2.662509,8.050793,-2.894855,-3.048814,4.817293,1.964040,-6.282995,-4.794085,7.810118,-7.660723,-5.139039,7.234532,1.968779,2.290360,-2.992399,2.390396,8.773540,4.100771,4.324307,-9.177003,-9.671499,-7.051679,7.558246,-7.628440,-5.450110,-3.883834,4.697251,9.184768,-0.354168,-9.651566,-2.408173,5.384609,5.743070,9.435429,-4.587822,8.151805,6.620549,8.871997,-9.120389,1.798604,5.434442,2.344016,-8.538741,8.765172,-6.381227,4.362144,2.742387,-4.436392,5.769894,-3.212754,-1.750985,-5.815224,6.961335,-7.465458,-3.301295,-5.724979,-7.079555,-8.036467,7.512418,8.893089,6.525032,-8.876705,-6.491523,2.867996,-0.160617,5.629574,9.051480,-3.726989,-0.877286,-6.876931,-5.968290,-4.323250,0.293681,4.242860,-9.090452,-9.953613,-9.945214,-6.730027,0.533382,-3.945338,4.206513,-1.129683,-6.804522,-8.932625,-4.469223,2.807901,6.550081,4.311555,-5.731052,4.792666,7.666745,-8.542180,-7.558386,-0.463271,7.044744,5.325242,6.969095,9.763380,-6.786338,-5.725366,0.819895,-1.392311,6.294838,8.920400,-6.934160,-6.625567,-0.523049,7.962303,5.717542,-9.925603,1.488205,-9.127573,-6.797284,-0.779024,0.062188,1.490612,-6.785195,9.930321,3.139030,8.654381,-7.849146,1.641982,-3.086690,2.386341,5.865083,-8.515627,-5.383944,6.595388,2.798976,5.831008,-8.951164,9.924390,-3.195226,-7.594336,7.575027,-7.328400,0.809511,-7.035642,-8.290728,2.103638,5.267458,-0.624620,-4.999881,-3.989284,3.614673,-5.708230,-5.625848,-5.056420,7.051242,-4.123800,-1.292911,-7.653652,0.824084,-4.692309,-9.751849,8.692448,8.319068,6.237720,6.486516,0.216224,-1.587675,-3.325744,7.063961,5.369183,3.572722,6.854021,-8.557388,1.037860,-1.203086,-1.600228,5.719289,9.891201,0.695468,5.267355,-4.641850,-2.397277,-4.168471,-6.921453,1.526201,-6.398422,3.405459,3.822828,0.549878,7.843882,-0.669330,4.926577,1.962399,-5.002689,2.248182,9.225793,9.410258,-3.438729,-8.082631,2.958852,2.775131,-3.878490,-6.151071,-3.511402,-9.622799,5.867313,3.505746,5.564301,3.760792,-8.552368,9.161190,3.431033,6.002127,-3.651898,-8.653938,3.002259,-1.132164,-8.325407,1.386938,-9.972864,8.905045,-3.834159,-1.002050,9.475072,-1.881057,2.162106,-1.777903,-5.385598,-8.867207,0.472307,-8.334536,-4.508836,4.840348,9.954984,-4.936685,-9.117965,-3.615186,-9.721432,-4.603846,-9.498313,2.366972,-3.238001,-4.000567,3.702624,-7.873605,4.690962,-5.440455,0.212442,1.313447,-8.207839,-6.635907,5.831438,-4.703295,-2.605116,7.456882,7.129823,-6.736996,-1.558260,-4.144653,9.799339,5.473350,5.389248,2.268142,1.230121,-1.791744,-1.122707,-5.377781,4.818327,5.205974,-6.646122,-9.195556,-2.012939,9.559245,-9.427238,-0.637183,-0.815404,-9.992639,1.153848,-6.101386,-4.219836,8.625961,-8.502716,-8.205452,-4.619717,9.435209,5.769386,-8.566508,-9.953131,-1.991792,7.550838,-0.225048,-0.145037,9.876835,-0.701674,-3.766132,-2.317684,2.757571,-0.169649,-5.812258,-6.672466,8.301110,-2.745669,3.470956,4.473405,0.325051,-1.275265,5.586969,-4.506350,1.099371,-1.640653,-7.107056,2.668075,4.237987,1.619756,-9.931016,4.142127,2.719579,2.559646,-8.133971,5.200447,2.180902,-8.990033,-2.930080,8.928022,2.661686,-9.025477,3.705367,-7.560959,8.852369,-9.613956,9.193395,6.429867,5.582928,6.481972,8.176412,3.441770,-4.925919,0.538367,3.734174,-0.635652,8.977169,-0.492556,-1.777942,1.376642,-2.237589,0.991877,-0.059454,7.260761,8.311222,3.094273,4.275634,2.049589,-1.620297,-7.675804,-7.578708,7.543728,0.314752,-7.246486,-9.937731,1.738304,2.543230,-1.976313,3.505933,-1.754847,-5.039747,-6.435398,-7.166422,2.946462,-7.746862,-9.032649,9.003272,-4.076744,5.751789,-1.580687,2.539618,7.415192,5.006393,-6.067361,5.456835,1.534317,-2.238564,6.215840,-2.649914,-9.492537,-4.161141,8.885844,-4.015679,0.543854,-7.123907,5.634765,6.452310,-5.257973,-3.826738,-0.566501,3.334322,1.184060,5.961091,9.466568,7.361411,-0.792371,-9.286225,4.573665,-7.984973,5.303435,9.790890,-5.247332,8.003079,1.373204,0.540606,0.297773,8.491098,-7.535826,4.658099,-4.985871,3.593441,-0.236324,-8.980663,-3.131912,-8.602569,5.020987,-2.208769,7.064054,4.753658,6.643590,-4.748671,9.799782,7.453422,-1.292580,1.208506,-9.898849,7.723035,3.445625,-5.754587,-4.138694,3.873990,-0.271893,9.071931,1.964395,-2.514114,7.408221,3.939822,1.394287,8.312024,1.034849,-5.553346,5.811547,-0.906708,-7.345934,4.713574,-6.859364,-5.159827,-3.068849,-8.711143,-8.801236,1.409850,3.626449,0.692286,5.329689,-0.598022,1.446471,-1.649724,-0.326596,2.212796,-1.043154,-2.645258,8.551962,2.048778,-1.661959,3.645624,0.246962,0.156497,8.990129,1.953755,1.776411,1.071335,-6.166551,8.143440,0.991804,3.312032,7.445683,-1.522153,5.137797,6.684122,5.472071,-0.284819,0.053096,0.195051,-2.404463,5.864167,-8.046703,9.342990,2.838665,4.588601,1.656390,-6.555744,-6.158478,-1.353908,-7.195588,-2.857553,-7.245519,-4.178340,-1.844888,6.430071,-1.049985,-2.192048,2.822508,-9.005530,-6.962395,9.740565,-7.535984,1.471507,-7.344891,-4.271538,5.934603,-7.391825,-9.198049,0.694476,-6.035414,9.341632,3.170282,9.832921,8.102864,6.706263,-0.547297,-9.160832,-9.321390,4.922042,2.251485,-6.362080,-6.451041,-0.243420,1.369306,5.226210,-3.365572,5.414403,-8.368977,6.659588,-1.902098,-6.387480,3.660720,3.021490,-1.067610,6.120855,8.305636,-3.009953,-8.011503,-9.137432,-2.911422,-4.900161,-5.191821,-5.786362,-5.604210,4.199099,5.480859,6.352830,-1.476934,-5.894225,-9.177160,-2.424211,2.767975,9.055222,3.306320,-0.894866,-8.712544,9.788184,-5.855257,9.478050,7.741476,7.056050,-4.719753,4.462595,7.633057,1.382244,5.625707,1.492821,-0.862005,3.147855,-1.639601,8.480569,-4.496374,-6.928823,2.276545,5.710120,-1.871449,1.671262,-8.415517,6.800438,-9.811553,3.005270,-6.745422,2.828827,9.265594,-7.917984,-6.252306,-8.537571,-0.737295,1.457855,9.731183,-3.919802,4.779368,-8.995225,3.704610,6.641371,3.644353,0.229978,-6.201066,-7.453416,1.092892,1.852574,9.739540,-4.065755,-4.920054,3.978866,6.574688,6.246532,3.511424,-7.983775,6.201721,-9.931983,-5.809965,-2.046181,-5.326717,-3.319535,-7.462415,3.683078,-2.188732,1.791040,2.933037,-8.889497,3.219724,5.103092,1.267696,2.361727,-6.353781,1.368497,9.317766,2.890075,3.289831,-8.363991,2.344009,6.002339,1.112087,9.489333,4.814175,9.451443,5.640151,9.864944,-5.372205,-4.479263,-5.005577,7.020725,7.357622,-4.050046,2.627161,-2.164218,-0.658077,-6.151870,0.195710,1.114114,0.126639,3.602895,5.000167,2.462490,5.833282,-4.974938,-5.245664,3.828946,-0.934849,-7.009639,-2.832298,7.023701,-0.506447,7.126925,3.265948,-1.950118,2.323222,3.291223,-1.661424,0.377055,-4.116151,8.743940,0.122800,5.855602,-0.619572,2.800892,-6.153944,-7.569183,-2.592140,-3.198481,-0.856636,-3.875563,-5.829130,-0.645753,1.663122,-4.538679,-3.874186,-0.398391,9.014133,7.902328,0.359493,-4.162598,7.258127,-8.557880,-7.832467,4.906514,1.419938,9.153244,-1.359376,-1.666962,3.649592,6.276594,-9.140799,3.048850,9.099282,-0.768464,-2.126272,7.209882,2.013609,8.017485,-9.244199,-0.120097], dtype = "float32")#candidate|23934|(750,)|const|float32
call_23932 = relay.TupleGetItem(func_21796_call(relay.reshape(var_23933.astype('float64'), [264, 1]), relay.reshape(const_23934.astype('float32'), [750,]), ), 2)
call_23935 = relay.TupleGetItem(func_21799_call(relay.reshape(var_23933.astype('float64'), [264, 1]), relay.reshape(const_23934.astype('float32'), [750,]), ), 2)
output = relay.Tuple([uop_23922,call_23932,var_23933,const_23934,])
output2 = relay.Tuple([uop_23922,call_23935,var_23933,const_23934,])
func_23942 = relay.Function([var_23921,var_23933,], output)
mod['func_23942'] = func_23942
mod = relay.transform.InferType()(mod)
var_23943 = relay.var("var_23943", dtype = "float32", shape = (3, 1, 9))#candidate|23943|(3, 1, 9)|var|float32
var_23944 = relay.var("var_23944", dtype = "float64", shape = (264,))#candidate|23944|(264,)|var|float64
output = func_23942(var_23943,var_23944,)
func_23945 = relay.Function([var_23943,var_23944,], output)
mutated_mod['func_23945'] = func_23945
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14750_call = mod.get_global_var('func_14750')
func_14752_call = mutated_mod.get_global_var('func_14752')
call_23958 = relay.TupleGetItem(func_14750_call(), 1)
call_23959 = relay.TupleGetItem(func_14752_call(), 1)
output = call_23958
output2 = call_23959
func_24001 = relay.Function([], output)
mod['func_24001'] = func_24001
mod = relay.transform.InferType()(mod)
output = func_24001()
func_24002 = relay.Function([], output)
mutated_mod['func_24002'] = func_24002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12848_call = mod.get_global_var('func_12848')
func_12850_call = mutated_mod.get_global_var('func_12850')
call_24006 = func_12848_call()
call_24007 = func_12848_call()
output = call_24006
output2 = call_24007
func_24010 = relay.Function([], output)
mod['func_24010'] = func_24010
mod = relay.transform.InferType()(mod)
mutated_mod['func_24010'] = func_24010
mutated_mod = relay.transform.InferType()(mutated_mod)
func_24010_call = mutated_mod.get_global_var('func_24010')
call_24011 = func_24010_call()
output = call_24011
func_24012 = relay.Function([], output)
mutated_mod['func_24012'] = func_24012
mutated_mod = relay.transform.InferType()(mutated_mod)
const_24030 = relay.const([[[8,9,2,6,-10,7,-6,-10,4],[-6,-9,-1,-2,-1,-9,-10,-2,6],[6,-3,-5,-10,5,-10,1,-10,-3],[-7,-7,-2,3,-5,5,-6,-3,5],[-1,3,-4,7,-8,-8,-9,8,5],[2,5,2,9,9,9,4,-1,-6],[-7,-2,3,8,7,7,9,2,7],[4,-2,-9,-10,-10,9,8,2,-3],[-2,-6,8,-2,1,2,8,3,10],[-2,5,9,-8,2,-7,-5,-9,-7],[-4,-5,-5,-4,-3,-4,9,1,-7],[-9,-9,7,9,6,-4,-4,-4,-5],[6,-1,-6,-1,-2,-10,5,6,-4],[2,6,1,3,-10,6,3,5,-2]],[[10,8,6,-10,1,6,8,9,8],[-6,9,7,1,9,5,-7,-5,-6],[4,5,-2,1,3,-4,1,-3,5],[-8,-9,2,-8,-10,5,7,3,-5],[3,3,-7,6,-8,-10,8,-1,5],[-4,6,8,-1,3,7,7,5,5],[-10,3,9,-2,3,5,-1,-3,-2],[-8,-5,6,-10,-1,4,10,8,-1],[9,5,9,10,-10,6,-3,4,-7],[2,-5,4,-1,-3,-10,-6,-8,-10],[1,-8,2,-3,-8,5,-9,-3,-9],[4,-3,-7,-1,-1,3,7,-1,7],[7,-8,-8,10,-7,-4,2,-6,-4],[10,-7,-4,4,6,-4,-9,-2,-6]],[[8,-8,9,-3,9,-5,-4,8,-8],[2,2,7,9,-9,-1,-1,-10,-7],[-2,-9,-2,6,3,-9,-6,3,9],[6,-4,-10,9,-7,10,-10,-6,3],[-7,-6,-3,-9,8,-7,-10,8,9],[10,-9,10,10,-2,-1,4,6,-6],[7,-7,7,-5,-8,-4,8,8,-2],[-9,-8,-9,-7,-7,-5,9,-8,8],[-10,-6,-3,-9,6,-2,-6,9,1],[-3,10,-9,-2,-6,5,-10,6,-5],[-8,-4,2,3,5,9,1,-4,1],[6,2,-4,6,1,-9,3,-1,-2],[-4,-8,-8,-5,-1,9,-2,5,-7],[-10,4,6,-8,-3,-7,3,-1,-2]],[[-9,7,8,4,-9,4,10,10,5],[-1,7,3,10,-7,8,1,6,7],[-2,-2,10,8,9,-5,-1,9,-2],[-2,-8,-5,-8,-4,-2,6,2,6],[3,-3,1,-9,6,-10,8,-1,3],[-5,-2,-5,9,-10,-9,-4,-10,9],[9,-4,3,5,8,-2,-4,3,-5],[10,-10,-9,-7,-3,2,-8,7,-7],[-6,4,8,8,-2,-8,1,-4,-8],[-10,-6,2,7,8,-2,6,7,5],[-5,-9,-5,-5,5,-5,-2,10,10],[-5,-3,-2,-8,-4,-8,10,1,-4],[6,-3,1,-4,5,-9,5,3,-7],[-5,-1,9,8,-7,-1,-7,10,-6]],[[8,-4,-5,7,8,-9,4,1,-3],[-7,2,-1,-4,-7,-8,7,-6,-8],[-3,2,4,-6,7,4,-6,10,6],[10,-2,6,2,6,4,1,-9,-7],[-6,3,-8,1,1,-5,-7,-9,-2],[8,10,-3,8,-10,-7,-3,-9,4],[5,-5,-1,3,5,-4,7,-2,6],[1,-1,4,-9,-1,-1,-8,-2,-3],[3,-8,6,-5,6,1,-7,7,-3],[-6,-7,-3,-1,7,5,-6,-3,-7],[10,3,-1,9,9,6,8,6,-6],[-4,-1,-2,-10,-5,7,-4,-5,-3],[3,4,10,6,9,-5,-3,6,1],[-10,-8,-4,6,2,-4,8,8,1]],[[-2,-8,-3,10,2,-9,5,4,4],[-6,5,-4,2,-10,3,-8,10,-8],[9,-8,5,5,-7,-1,6,-3,-7],[2,8,2,3,10,8,-8,-7,9],[6,-10,-3,-5,-2,2,7,1,-5],[-1,-2,6,9,6,-2,8,9,10],[10,-2,8,-2,-7,-2,-5,-5,-2],[-5,-4,-6,6,-4,-3,6,4,8],[10,-6,-4,-1,9,-5,6,-3,3],[-9,-7,-3,-1,-4,4,6,-3,-5],[9,5,2,3,2,-8,-9,-3,2],[-5,-2,8,2,-2,-4,-3,2,5],[7,-4,3,-3,1,-9,9,-3,-4],[9,-5,-2,-9,-4,-2,-7,-4,-8]],[[-2,-1,7,5,-1,-9,1,4,10],[-5,-2,1,7,-3,-10,-9,-3,7],[-8,8,-1,6,-4,10,-8,-2,-3],[2,-3,-8,-9,-5,-7,4,3,5],[-10,9,-3,7,-1,2,4,-1,-1],[7,-8,-4,-3,10,-4,-1,10,-6],[7,6,4,4,-2,-2,6,4,-2],[-10,-1,-2,-7,-7,2,-2,1,-9],[-6,3,-9,-10,6,2,-4,-4,5],[10,-8,-1,-4,-1,10,10,-4,3],[-9,10,-7,-7,3,8,7,1,4],[-6,-4,-3,-1,-2,7,-8,-8,-6],[-9,8,4,1,3,-7,-4,7,-3],[6,-5,-7,-6,1,-3,1,-7,5]],[[6,-3,10,5,-4,-5,5,9,2],[2,-4,3,7,-1,-2,8,-6,6],[10,1,-6,-2,-10,10,-8,-1,7],[-10,-8,1,-9,8,9,-9,-7,-4],[9,-1,7,-2,-6,-7,-4,7,8],[-2,6,-10,5,-5,-4,-3,-3,1],[-8,4,3,-6,10,1,-3,5,-2],[-6,8,9,-8,-4,-9,-2,-7,4],[10,1,5,-8,-2,8,1,4,5],[1,8,-6,-2,5,-5,-3,8,2],[3,-2,4,2,-5,-5,10,4,3],[6,-6,-5,9,-5,2,-2,7,2],[5,-7,10,1,-7,-9,-4,-6,-3],[1,-10,1,-4,-7,-9,4,-4,-4]],[[-2,6,9,10,8,4,-8,5,1],[-10,-1,6,7,-3,1,-5,4,4],[5,-9,-1,-4,7,-7,-7,3,-5],[7,-9,2,10,2,-1,7,2,8],[-8,2,-6,-6,-7,3,10,-3,2],[8,5,4,-8,-1,-7,-4,5,-2],[7,4,-9,-6,-8,-9,-6,-2,8],[-8,-9,9,-10,-2,-2,-6,2,-1],[-8,1,5,6,-6,-2,-4,-3,1],[-10,-8,8,5,-9,5,-2,-8,-10],[-1,-4,-7,-3,1,6,1,-3,-6],[-9,4,-2,9,-3,-4,-1,1,4],[-6,-1,-5,6,-2,-5,7,-1,-3],[9,4,-10,-5,5,-6,4,-8,-6]],[[-1,-6,-1,-3,-6,-9,-7,2,10],[-2,-3,-1,-8,1,-1,8,1,-8],[7,-3,6,-2,2,-6,6,-7,7],[-7,6,-2,7,10,-3,2,-10,3],[-1,-10,-10,5,-6,-4,2,-9,-1],[5,8,10,4,1,9,9,-10,-2],[5,6,-10,4,4,-8,4,-7,-9],[-6,-8,-8,-3,-8,-5,-1,8,2],[8,7,9,8,-1,8,9,4,10],[-6,-10,-6,-7,-7,-2,10,-7,1],[4,-1,-4,6,10,-3,-3,-5,-5],[8,-6,4,4,-10,-3,-6,2,-4],[4,-10,-2,-9,1,-8,3,-6,-2],[8,6,-6,-1,-8,10,1,-1,-2]],[[-3,-10,3,1,-7,-4,1,5,-2],[-6,3,-9,-3,-1,-1,-1,-4,-1],[10,-2,2,6,-1,-1,-1,-7,-9],[9,7,10,3,-4,-2,-3,-8,-9],[-2,-4,-5,-6,-9,1,9,4,2],[-4,3,9,5,-8,-8,3,-2,-2],[1,-3,1,2,6,6,8,-2,-9],[8,4,7,5,-9,-9,5,-9,4],[-4,9,-10,9,-8,3,-1,-3,9],[6,-4,-2,-8,-4,-7,6,-5,-5],[-4,7,5,-1,-2,-3,6,6,6],[2,-7,10,7,7,-5,-8,-7,2],[4,-8,10,9,3,-6,3,3,-6],[-6,-1,2,-5,6,7,4,1,-10]],[[-3,7,-4,5,10,-9,-10,-9,8],[-8,4,-7,-2,-2,2,4,-1,-3],[3,-2,5,1,-8,8,-2,1,2],[8,-10,5,-4,-9,-1,2,2,8],[7,5,-2,1,1,1,-1,-5,9],[3,10,-10,6,-4,-6,-6,-4,8],[5,-9,1,-2,-8,3,9,-3,-8],[2,5,-2,10,5,8,1,5,2],[1,10,10,-1,1,-10,8,-5,-9],[7,-5,-5,-8,-8,6,8,-3,9],[4,-2,3,-6,-3,-6,-7,2,-5],[-5,-1,5,3,7,2,9,5,10],[3,-8,6,9,-7,3,7,-7,5],[8,-3,-5,-10,-2,-4,-2,8,-5]],[[8,-6,-4,8,-1,10,5,3,4],[5,-2,8,9,5,3,-2,2,5],[10,-7,-8,-8,-6,1,1,-3,-2],[9,4,1,-3,-8,4,3,9,-9],[-9,-8,-8,-5,6,1,1,-3,3],[-2,-10,3,6,-10,-8,-9,-5,-1],[9,-1,-4,-7,2,1,4,6,-6],[8,5,-8,-6,-9,6,-4,-6,2],[-9,6,-6,1,-2,6,5,1,-3],[-4,-6,9,-3,-8,2,-10,6,-4],[-2,-6,1,-4,5,10,-4,6,7],[1,2,8,9,7,-3,2,6,-2],[10,-7,1,5,-10,-3,-8,-7,-6],[-6,-3,2,4,1,-2,10,9,6]]], dtype = "uint32")#candidate|24030|(13, 14, 9)|const|uint32
var_24031 = relay.var("var_24031", dtype = "uint32", shape = (13, 14, 9))#candidate|24031|(13, 14, 9)|var|uint32
bop_24032 = relay.bitwise_and(const_24030.astype('uint32'), relay.reshape(var_24031.astype('uint32'), relay.shape_of(const_24030))) # shape=(13, 14, 9)
output = bop_24032
output2 = bop_24032
func_24042 = relay.Function([var_24031,], output)
mod['func_24042'] = func_24042
mod = relay.transform.InferType()(mod)
var_24043 = relay.var("var_24043", dtype = "uint32", shape = (13, 14, 9))#candidate|24043|(13, 14, 9)|var|uint32
output = func_24042(var_24043)
func_24044 = relay.Function([var_24043], output)
mutated_mod['func_24044'] = func_24044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20992_call = mod.get_global_var('func_20992')
func_20993_call = mutated_mod.get_global_var('func_20993')
call_24049 = func_20992_call()
call_24050 = func_20992_call()
output = relay.Tuple([call_24049,])
output2 = relay.Tuple([call_24050,])
func_24098 = relay.Function([], output)
mod['func_24098'] = func_24098
mod = relay.transform.InferType()(mod)
mutated_mod['func_24098'] = func_24098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_24098_call = mutated_mod.get_global_var('func_24098')
call_24099 = func_24098_call()
output = call_24099
func_24100 = relay.Function([], output)
mutated_mod['func_24100'] = func_24100
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21290_call = mod.get_global_var('func_21290')
func_21292_call = mutated_mod.get_global_var('func_21292')
call_24135 = relay.TupleGetItem(func_21290_call(), 0)
call_24136 = relay.TupleGetItem(func_21292_call(), 0)
output = relay.Tuple([call_24135,])
output2 = relay.Tuple([call_24136,])
func_24159 = relay.Function([], output)
mod['func_24159'] = func_24159
mod = relay.transform.InferType()(mod)
mutated_mod['func_24159'] = func_24159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_24159_call = mutated_mod.get_global_var('func_24159')
call_24160 = func_24159_call()
output = call_24160
func_24161 = relay.Function([], output)
mutated_mod['func_24161'] = func_24161
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14930_call = mod.get_global_var('func_14930')
func_14932_call = mutated_mod.get_global_var('func_14932')
call_24179 = relay.TupleGetItem(func_14930_call(), 2)
call_24180 = relay.TupleGetItem(func_14932_call(), 2)
uop_24186 = relay.asin(call_24179.astype('float32')) # shape=(140,)
uop_24188 = relay.asin(call_24180.astype('float32')) # shape=(140,)
func_15367_call = mod.get_global_var('func_15367')
func_15370_call = mutated_mod.get_global_var('func_15370')
const_24215 = relay.const([-6.827089,-4.861898,-0.964720,6.103846,-5.065957,-2.202369,0.727448,-8.895600,-0.228265,6.828545,0.967715,0.025473,6.132643,7.116199,-5.292850,0.388471,9.781184,8.460411,-2.978662,-0.533431,9.607439,-7.982437,7.608156,-2.796661,-9.428563,-0.292958,-0.863823,0.204886,-9.705672,-8.532389,-0.978449,7.145999,5.204873,-4.299809,-1.904326,1.993479,6.265354,-5.433879,-0.683382,-8.092844,-4.365967,-6.132192,-8.132530,8.667846,-8.845976,1.986596,9.980182,-0.173838,-8.253451,-0.096768,9.529389,-8.362171,1.974118,2.368150,-0.977333,6.732549,5.945858,5.046853,5.871544,-4.483518,-5.779060,-9.851379,-0.489081,-9.556440,8.850766,7.370290,-1.925393,9.285610,0.245572,9.256985,-2.445888,-7.039847,-6.092855,6.919151,-0.424758,-5.986496,-1.381391,5.950049,8.808452,8.389829,-7.763999,-4.268895,-5.470504,1.647552,-5.102533,5.558374,5.391392,-5.944273,7.511021,4.826604,7.787630,-5.913083,-1.143075,7.426072,-8.848277,1.012526,1.988884,0.585100,0.846411,7.217892,-9.420677,7.270861,9.213311,7.959300,6.904327,-4.018615,-9.135100,-8.598055,-6.260778,4.281975,-0.063758,-7.127055,-3.198843,-0.125162,-3.468083,4.650392,-5.116873,-7.961494,0.538133,2.650407,-4.912516,0.336946,-5.156258,9.657023,8.160315,6.519786,4.702498,-2.231964,-5.720182,-8.777280,-4.402453,5.740033,-3.254539,-7.319247,4.078257,-7.050800,-2.864808,0.492205,-4.785672,6.890235,4.497688,9.357388,-4.251867,-3.952703,-6.213461,4.704983,-8.801052,-0.190548,-7.321715,-6.229454,-5.353305,3.226670,0.553620,0.067509,-7.396713,9.092832,-4.420375,-3.394572,-7.924675,5.090321,2.266261,-3.479414,6.090966,-8.397225,4.828423,0.921087,-3.601448,-1.424515,3.397951,8.951591,4.570817,8.315627,0.955447,-5.724363,-6.291195,4.463252,6.054043,-1.184606,-5.742866,-6.033285,6.142481,7.839258,2.495885,9.318155,5.267282,-4.356671,-8.712607,-5.480591,7.086540,4.579667,-8.913126,-4.195931,-3.283562,-6.382338,3.895972,0.773930,5.901388,-3.088626,-4.939259,7.661424,-8.414659,-6.945879,-4.930267,2.253555,-8.962257,5.496745,5.510883,-0.392216,-5.738691,-3.905039,0.416616,9.513012,-0.331458,7.384139,9.598333,-5.094896,-8.949345,-9.658155,-6.603858,3.512779,3.295206,0.366482,-1.769107,-3.284832,7.728832,-4.473758,-2.053151,5.124503,-7.798620,-8.469445,3.576600,3.069112,2.689082,-9.085649,6.219526,-1.295079,2.343613,8.473959,7.715088,-5.016914,-5.566928,-2.618985,-3.155725,7.942791,-3.032352,5.499182,8.319207,-0.922714,-3.063434,-4.355614,-8.606428,-0.447478,-9.476224,8.364926,-7.111234,-4.583606,-3.619013,9.514679,-6.606309,1.789601,-3.058728,1.541472,-9.132589,5.241046,-0.035519,-5.834185,-7.936243,-2.819977,1.924021,0.027283,-3.367416,-8.163519,-2.935482,0.091461,1.908726,9.463917,7.289830,2.699698,-2.121149,9.453518,-8.639764,9.424040,-0.581570,2.045662,9.655384,3.136129,7.633880,1.327858,-4.343318,-8.297428,4.289551,3.248395,-7.041357,-5.074594,5.773545,-9.408175,-3.300110,6.699517,5.097428,-2.198801,1.906261,-4.329363,5.408354,-5.990723,1.226285,1.050898,-5.002069,0.893905,7.885883,-0.917911,9.737138,-8.566120,-3.602500,3.602713,1.219101,1.481945,7.748360,9.939366,8.654664,-4.200192,-3.045543,5.165767,2.403706,-7.498829,6.760522,6.412897,7.782738,-2.612174,5.629131,8.655660,5.035777,8.747925,2.052572,6.209077,-0.878864,0.545514,-2.220905,-5.129478,1.224964,-7.666132,4.828925,-2.362944,-2.008724,-6.100130,-7.551342,-8.158761,-2.550363,-6.967017,-7.690888,-5.078780,-1.610968,2.136407,0.946678,-5.603354,-3.036344,6.827087,-5.147082,-2.652497,-8.042095,7.645448,5.235365,-5.348098,1.169251,0.184892,-1.399588,4.363047,4.777545,9.933957,-0.173738,7.926400,4.930627,-5.733520,-5.246906,-8.402320,6.928307,6.019315,7.043749,4.289515,0.318197,-6.085254,-1.344577,-9.817010,-1.995573,-8.025413,5.626380,-7.927522,-7.725832,-0.664715,3.402966,5.025260,-1.907989,9.109363,-9.039004,7.055442,6.623203,-3.164099,0.637142,6.961915,-4.446369,-5.026885,-6.957384,-0.386543,5.792563,4.331422,3.582875,4.518158,-3.279466,0.752828,0.655615,-1.125444,-5.967545,4.161827,1.948585,-2.502681,-3.079351,6.192959,2.080274,-5.329744,-1.331594,1.124523,-9.474983,-0.777687,-7.674657,-2.044261,-1.881916,-2.017675,8.878308,-9.266168,4.677233,-7.168694,4.596431,-8.839612,-3.550335,8.296335,-3.307745,-3.921415,1.165254,6.673709,1.806019,-6.758646,-5.174043,-0.621644,-9.984652,-1.294993,7.388623,0.910372,-6.207419,2.403587,-4.379012,-3.633512,-6.833310,-5.547750,2.874817,9.975722,7.164342,-3.623472,-0.780241,1.462355,4.981663,-6.931770,-2.009497,1.279507,5.441564,7.664589,3.883165,5.549431,5.532270,6.080154,0.897074,3.749948,-0.321352,4.727317,-9.792172,9.697303,-0.157777,8.466337,-3.966810,-3.990479,9.797381,7.622296,8.026644,-6.158705,-3.271008,7.991029,-5.624461,-4.232729,-2.394470,-1.255548,-8.748858,-6.642013,2.331375,-4.440250,-3.780087,-2.540155,-5.909681,-2.465686,-9.085133,-5.730211,-8.137709,-4.904201,-3.191041,-7.255444,-8.707590,-3.876491,-0.895475,-7.435755,-8.753388,7.868495,7.466464,-3.272549,-6.590407,9.736255,-4.065805,9.415505,6.818179,7.703401,1.994974,-2.936516,-8.934881,-7.317824,0.372944,7.889240,2.800696,-6.204546,-2.143139,7.202631,7.837359,0.700876,-4.806182,-8.018419,-1.277887,-5.206524,1.577014,-7.435894,0.027094,6.739648,7.232677,-3.861385,3.836223,2.143908,8.593567,-9.888114,8.160218,-3.414038,4.502867,8.083037,5.241510,0.048080,-2.665386,-7.905287,-1.337513,-1.997077,-9.427027,4.198427,1.033687,1.959815,2.271494,9.266502,6.958231,-7.189676,-8.466048,0.531246,4.435181,7.069189,-3.326884,3.742482,7.416550,-9.478956,-2.643729,0.834209,-1.874988,0.792076,1.609737,-1.615303,-7.816148,9.106443,-5.067364,-2.373858,6.680713,6.489164,-5.036026,-0.482944,-5.102271,5.355268,-3.666575,-8.129967,-0.870624,-0.700433,-9.116796,-7.986494,-7.021161,6.911389,-1.872904,-9.363274,4.943460,6.190683,7.582942,8.617066,-8.110932,-5.883898,-0.481228,6.788433,-5.436292,-3.689149,-3.067352,-9.494989,-2.595412,6.860940,0.431374,-5.870808,1.774827,-1.744894,7.571693,-1.739171,6.049185,7.598956,9.097936,-3.687024,-8.229773,-3.803763,8.417874,9.790796,6.989041,3.180406,6.987538,9.274871,3.708180,4.006142,-6.561353,0.915077,-4.903934,2.862468,5.339816,-2.449088,-1.080022,5.122564,4.426712,0.502632,5.241966,1.775264,-5.626742,-5.696333,8.365139,-2.757092,6.582660,7.186338,-6.545932,-2.050471,-2.621510,-9.442592,8.149313,-7.584612,-3.650830,0.845949,-2.331836,-7.726439,-7.671493,4.663734,-1.923084,6.081851,3.539815,-8.390232,1.183429,3.584722,6.864693,-6.653823,6.980144,1.760537,-6.702826,-3.182473,4.661728,5.008529,0.880701,6.147509,-6.692725,4.632686,1.564490,-0.785302,-9.520212,-1.358728,5.125185,9.174889,-2.784627,-3.649264,0.589395,5.784647,-2.868760,-8.913392,6.502114,6.258337,-9.116144,2.571257,-0.295812,-7.598875,-9.180034,-5.309022,7.531044,-6.356578,-7.148667,-4.532918,3.967670,8.239391,-7.266706,7.716468,5.164700,-1.140705,-3.700636,-1.911021,2.236390,9.401216,8.556922,4.666162,4.461063,-0.360355,-3.784363,-1.434595,6.431103,6.032103,8.327335,8.940106,-5.235839,5.826455,-8.634383,1.047919,-9.536699,0.702886,0.029247,5.558896,-9.270454,-0.865569,-1.934209,3.587322,-4.854525,-5.451326,9.968048,5.701910,5.357226,-6.333842,-6.713586,7.137807,5.966875,-0.336294,0.825230,4.610262,-4.545753,-7.954437,-9.096807,-7.567507,7.798676,0.770928], dtype = "float32")#candidate|24215|(750,)|const|float32
var_24216 = relay.var("var_24216", dtype = "float64", shape = (182,))#candidate|24216|(182,)|var|float64
call_24214 = relay.TupleGetItem(func_15367_call(relay.reshape(const_24215.astype('float32'), [750,]), relay.reshape(var_24216.astype('float64'), [13, 14]), ), 5)
call_24217 = relay.TupleGetItem(func_15370_call(relay.reshape(const_24215.astype('float32'), [750,]), relay.reshape(var_24216.astype('float64'), [13, 14]), ), 5)
func_17461_call = mod.get_global_var('func_17461')
func_17465_call = mutated_mod.get_global_var('func_17465')
var_24243 = relay.var("var_24243", dtype = "uint64", shape = (160,))#candidate|24243|(160,)|var|uint64
var_24244 = relay.var("var_24244", dtype = "float64", shape = (1008,))#candidate|24244|(1008,)|var|float64
call_24242 = relay.TupleGetItem(func_17461_call(relay.reshape(var_24243.astype('uint64'), [8, 20]), relay.reshape(var_24244.astype('float64'), [1008,]), ), 0)
call_24245 = relay.TupleGetItem(func_17465_call(relay.reshape(var_24243.astype('uint64'), [8, 20]), relay.reshape(var_24244.astype('float64'), [1008,]), ), 0)
func_18887_call = mod.get_global_var('func_18887')
func_18889_call = mutated_mod.get_global_var('func_18889')
call_24252 = relay.TupleGetItem(func_18887_call(), 0)
call_24253 = relay.TupleGetItem(func_18889_call(), 0)
func_21208_call = mod.get_global_var('func_21208')
func_21210_call = mutated_mod.get_global_var('func_21210')
call_24254 = func_21208_call()
call_24255 = func_21208_call()
output = relay.Tuple([uop_24186,call_24214,const_24215,var_24216,call_24242,var_24243,var_24244,call_24252,call_24254,])
output2 = relay.Tuple([uop_24188,call_24217,const_24215,var_24216,call_24245,var_24243,var_24244,call_24253,call_24255,])
func_24264 = relay.Function([var_24216,var_24243,var_24244,], output)
mod['func_24264'] = func_24264
mod = relay.transform.InferType()(mod)
var_24265 = relay.var("var_24265", dtype = "float64", shape = (182,))#candidate|24265|(182,)|var|float64
var_24266 = relay.var("var_24266", dtype = "uint64", shape = (160,))#candidate|24266|(160,)|var|uint64
var_24267 = relay.var("var_24267", dtype = "float64", shape = (1008,))#candidate|24267|(1008,)|var|float64
output = func_24264(var_24265,var_24266,var_24267,)
func_24268 = relay.Function([var_24265,var_24266,var_24267,], output)
mutated_mod['func_24268'] = func_24268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19297_call = mod.get_global_var('func_19297')
func_19298_call = mutated_mod.get_global_var('func_19298')
call_24330 = relay.TupleGetItem(func_19297_call(), 0)
call_24331 = relay.TupleGetItem(func_19298_call(), 0)
output = relay.Tuple([call_24330,])
output2 = relay.Tuple([call_24331,])
func_24341 = relay.Function([], output)
mod['func_24341'] = func_24341
mod = relay.transform.InferType()(mod)
output = func_24341()
func_24342 = relay.Function([], output)
mutated_mod['func_24342'] = func_24342
mutated_mod = relay.transform.InferType()(mutated_mod)
const_24375 = relay.const([[[-1.162350,-3.553993,8.055348,6.169027,-7.575596,1.510507]],[[5.018127,-5.288417,1.143545,-1.010511,6.710481,-6.683790]],[[-5.178922,1.334793,-8.981156,-2.885519,-2.530183,7.670401]],[[4.308290,7.145035,3.400252,8.303400,8.563165,6.803660]],[[2.848464,6.997275,-4.686593,0.004324,4.109669,9.202196]],[[-0.865880,-0.342262,-5.707518,-0.568830,-4.361392,1.715388]],[[6.133216,-8.071428,-5.857604,2.239290,-2.619120,-0.657907]],[[0.122960,1.908956,-9.938587,-3.631915,-1.489134,-2.618289]],[[-1.155204,6.769377,-9.536211,-6.980258,1.949905,3.480171]],[[-1.006228,1.214123,5.610882,6.057580,-8.600038,9.506293]],[[-9.168672,1.883271,0.150548,8.181867,-2.569448,-3.150747]],[[-1.534986,-7.160422,-1.427193,9.811881,4.384860,3.274050]],[[6.146056,1.628792,7.785411,-1.351067,-9.397079,2.623843]]], dtype = "float32")#candidate|24375|(13, 1, 6)|const|float32
uop_24376 = relay.sin(const_24375.astype('float32')) # shape=(13, 1, 6)
func_17630_call = mod.get_global_var('func_17630')
func_17632_call = mutated_mod.get_global_var('func_17632')
call_24391 = relay.TupleGetItem(func_17630_call(), 0)
call_24392 = relay.TupleGetItem(func_17632_call(), 0)
func_9478_call = mod.get_global_var('func_9478')
func_9481_call = mutated_mod.get_global_var('func_9481')
var_24396 = relay.var("var_24396", dtype = "float64", shape = (432,))#candidate|24396|(432,)|var|float64
call_24395 = relay.TupleGetItem(func_9478_call(relay.reshape(var_24396.astype('float64'), [6, 9, 8])), 0)
call_24397 = relay.TupleGetItem(func_9481_call(relay.reshape(var_24396.astype('float64'), [6, 9, 8])), 0)
output = relay.Tuple([uop_24376,call_24391,call_24395,var_24396,])
output2 = relay.Tuple([uop_24376,call_24392,call_24397,var_24396,])
func_24398 = relay.Function([var_24396,], output)
mod['func_24398'] = func_24398
mod = relay.transform.InferType()(mod)
var_24399 = relay.var("var_24399", dtype = "float64", shape = (432,))#candidate|24399|(432,)|var|float64
output = func_24398(var_24399)
func_24400 = relay.Function([var_24399], output)
mutated_mod['func_24400'] = func_24400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14750_call = mod.get_global_var('func_14750')
func_14752_call = mutated_mod.get_global_var('func_14752')
call_24416 = relay.TupleGetItem(func_14750_call(), 0)
call_24417 = relay.TupleGetItem(func_14752_call(), 0)
func_11459_call = mod.get_global_var('func_11459')
func_11460_call = mutated_mod.get_global_var('func_11460')
call_24431 = relay.TupleGetItem(func_11459_call(), 0)
call_24432 = relay.TupleGetItem(func_11460_call(), 0)
output = relay.Tuple([call_24416,call_24431,])
output2 = relay.Tuple([call_24417,call_24432,])
func_24467 = relay.Function([], output)
mod['func_24467'] = func_24467
mod = relay.transform.InferType()(mod)
mutated_mod['func_24467'] = func_24467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_24467_call = mutated_mod.get_global_var('func_24467')
call_24468 = func_24467_call()
output = call_24468
func_24469 = relay.Function([], output)
mutated_mod['func_24469'] = func_24469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11288_call = mod.get_global_var('func_11288')
func_11290_call = mutated_mod.get_global_var('func_11290')
call_24488 = relay.TupleGetItem(func_11288_call(), 0)
call_24489 = relay.TupleGetItem(func_11290_call(), 0)
func_15721_call = mod.get_global_var('func_15721')
func_15722_call = mutated_mod.get_global_var('func_15722')
call_24490 = relay.TupleGetItem(func_15721_call(), 1)
call_24491 = relay.TupleGetItem(func_15722_call(), 1)
func_11147_call = mod.get_global_var('func_11147')
func_11149_call = mutated_mod.get_global_var('func_11149')
var_24497 = relay.var("var_24497", dtype = "float64", shape = (832,))#candidate|24497|(832,)|var|float64
call_24496 = relay.TupleGetItem(func_11147_call(relay.reshape(var_24497.astype('float64'), [832,])), 3)
call_24498 = relay.TupleGetItem(func_11149_call(relay.reshape(var_24497.astype('float64'), [832,])), 3)
func_20303_call = mod.get_global_var('func_20303')
func_20305_call = mutated_mod.get_global_var('func_20305')
call_24520 = relay.TupleGetItem(func_20303_call(), 0)
call_24521 = relay.TupleGetItem(func_20305_call(), 0)
output = relay.Tuple([call_24488,call_24490,call_24496,var_24497,call_24520,])
output2 = relay.Tuple([call_24489,call_24491,call_24498,var_24497,call_24521,])
func_24526 = relay.Function([var_24497,], output)
mod['func_24526'] = func_24526
mod = relay.transform.InferType()(mod)
mutated_mod['func_24526'] = func_24526
mutated_mod = relay.transform.InferType()(mutated_mod)
var_24527 = relay.var("var_24527", dtype = "float64", shape = (832,))#candidate|24527|(832,)|var|float64
func_24526_call = mutated_mod.get_global_var('func_24526')
call_24528 = func_24526_call(var_24527)
output = call_24528
func_24529 = relay.Function([var_24527], output)
mutated_mod['func_24529'] = func_24529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14297_call = mod.get_global_var('func_14297')
func_14298_call = mutated_mod.get_global_var('func_14298')
call_24602 = func_14297_call()
call_24603 = func_14297_call()
func_20115_call = mod.get_global_var('func_20115')
func_20119_call = mutated_mod.get_global_var('func_20119')
const_24607 = relay.const([-2,2,-5,10,2,6,-9,-6,-6,4,1,2,8,-8,-3,-2,1,-4,-7,-4,2,-10,9,-3,-6,-10,10,-2,-7,5,-3,-4,-3,1,-3,-8,-6,-6,-6,-7,-6,9,2,6,2,-1,8,-7,6,-10,-2,-1,-9,-3,-8,5,-9,1,6,1,9,-2,7,-8,7,1,-8,-2,-1,-4,-5,-4,5,-6,-3,8,-10,8,10,-10,6,10,6,-5,-5,8,7,-6,7,3,10,-1,10,8,7,-8,-1,-1,8,-4,2,-5,-3,-1,-3,-2,4,3,-7,7,-3,9,3,3,-7,-4,-10,-9,-10,-7,5,-5,-5,4,-1,7,5,-2,-7,10,3,-4,5,-7,-2,-7,6,-7,-10,4], dtype = "uint16")#candidate|24607|(140,)|const|uint16
const_24608 = relay.const([[7,-10,5,-5,-9,-3,8,1,-8,9,1,-1,-1,7,-4,3,6,8,9,-10,-8,1,1,-7,6,-5,5,3,1,-1,-9,-8,-10,-4,4,9,-9,5,10,-8,-7,7,-1,8,-10,-8,-3,-4,7,-2,-6,-10,-1,6,8,-10,-9,6,9,3,-1,10,9,7,-4,6,1,-4,2,4,1,8,-4,1,8,-3,-7,5,7,-2,2,-8,6,5,-9,10,6,-2,-2,-2,-7,1,7,9,-7,-4,1,-4,-3,4,10,4,2,6,8,-6,4,8,3,-7,10,-1,-3,-5,6,8,5,-3,7,3,-9,4,-6,5,2,10,-3,-3,4,3]], dtype = "uint64")#candidate|24608|(1, 130)|const|uint64
const_24609 = relay.const([5.861191,-2.762236,7.144285,3.653145,8.667984,6.583962,7.801922,7.219732,9.946183,-4.183023,2.678323,2.448612,-6.055165,-8.424394,-0.852907,-3.661000,-7.607081,1.999446,-6.999453,1.639849,5.322927,3.577551,1.664941,0.949500,-4.487068,-3.191832,-2.820078,-9.418617,-3.887336,-5.032934,2.231573,-1.600754,2.120768,5.812746,-2.301025,-0.875312,-3.258859,1.040362,-7.997381,-7.767490,-8.106869,-5.470624,-9.368967,9.080546,-3.913015,1.062140,-7.324631,1.336719,5.068227,2.013554,-9.161836,-2.264425,6.093371,-0.439241,-6.222376,-2.188924,3.843542,9.729932,6.965160,-6.079775,5.610365,-7.222725,1.509126,0.384387,-4.687178,-7.726744,-3.721396,6.101833,-2.038752,-1.229581,1.548155,6.401733,6.900872,-8.548712,4.175064,-6.359862,8.274167,-9.728216,3.887631,7.303506,5.731830,-6.025696,-8.013957,5.742238,9.690597,-9.479546,4.796858,0.098358,-2.590522,6.951679,-5.006402,-1.213824,-2.417409,-9.607143,6.824579,-1.022980,7.701943,-9.489031,-4.462608,0.234731,6.535081,-6.331714,7.691144,-1.161029,-0.887705,-4.409839,2.848257,-6.975162,0.505217,3.680871,-6.641024,0.031400,-6.532587,-8.779485,-1.570503,-0.160617,9.356904,-2.718252,-9.389738,-5.203074,-9.844709,4.996461,-6.120652,-3.017293,-9.514776,-6.715671,9.260605,6.465546,3.637231,-3.360764,9.215555,-0.424054,-0.248895,9.781212,4.078440,7.251207,-9.409618,4.480984,-0.212346,3.978253,-9.075906,5.144766,5.958653,1.576714,-1.126214,-5.499595,3.105765,-6.372758,0.071106,-4.275091,-9.107062,4.631664,5.388042,1.558528,-3.358879,-6.025839,-2.641442,-0.716231,-1.970939,-7.548738,3.246538,-1.794601,1.855000,-4.655566,0.350211,5.967122,-5.558996,-9.674605,-6.726882,4.815602,-2.795342,7.509493,-7.294326,5.706738,9.513269,2.025840,-6.536346,9.924595,6.593930,9.675624,8.132127,-2.522210,9.216623,3.411002,-9.048624,-6.439884,-4.155694,2.731843,8.496718,-1.309855,-1.492608,3.925128,0.158996,7.124258,1.599145,6.187858,7.133874,-2.602838,7.015367,-9.382751,1.256445,-1.886323,-0.291671,-6.008594,-1.961804,5.691206,-3.135695,-6.190391,5.907994,-7.343543,-5.545466,1.322814,3.077442,-9.081426,7.051168,-8.004357,7.883625,3.761876,-8.247303,0.588066,-6.754015,-6.991934,0.509190,-1.885889,-5.542034,7.340217,4.118140,-8.436259,2.884102,3.437965,-4.142384,6.402783,-7.704099,0.394014,-4.629270,-0.731597,6.329382,4.593855,8.598392,-4.880529,0.527116,-9.441725,-7.631199,9.135960,9.837418,8.173863,2.496726,9.920312,6.350803,-4.432163,8.562292,-1.850015,2.591962,0.233292,2.025305,-6.845883,-3.500771,4.890235,-1.571453,-7.517797,7.319626,5.366625,-9.325479,0.259155,3.684245,4.308545,-6.520649,-5.736893,2.581715,-3.428223,8.538616,7.268632,1.292573,-8.846390,-1.428325,2.642544,-7.067945,-9.727392,4.292130,-3.651538,7.708297,0.035208,8.874556,-7.657197,7.081846,-2.561538,1.874772,-6.177522,-0.948418,-6.808275,2.320511,2.980453,-8.359527,-3.503424,5.522272,3.098115,-4.904334,-4.820627,-2.667959,9.058911,2.442852,-3.159677,1.649605,5.227920,4.609251,-3.341929,6.006131,0.638621,9.886066,5.203664,-8.105080,-5.336125,7.409230,9.331783,7.067100,1.526693,-6.445996,9.752442,1.828372,0.572792,5.784346,8.203189,0.025259,-9.747856,4.127479,9.923907,-4.642948,-1.406653,-4.460944,1.674454,-4.240951,-0.785404,-7.564696,9.750073,-5.060317,1.421572,-9.192994,-9.656367,7.465290,0.452393,-4.654852,-4.829788,-2.339788,-2.016385,-0.399752,-3.803909,8.351757,4.394662,-7.077038,4.541542,-5.348384,-1.377366,1.403189,-1.104347,-9.300341,8.637449,2.784401,1.993460,4.919574,-6.915225,-3.900341,-4.245312,-0.592707,2.396544,-2.488049,3.434863,6.951947,-9.501536,2.017208,5.143058,-1.451807,-7.275438,3.327768,5.964553,-9.006949,-3.960360,-8.182258,-9.608940,6.093434,4.483792,-1.680437,-5.699526,2.388253,-0.898444,6.413249,-6.903927,9.432165,1.351970,-0.820373,4.294598,5.208860,5.660512,-6.948072,-8.815181,-7.970598,-8.831895,-8.706240,-5.598124,5.544670,-8.081078,6.661930,-3.773604,-3.538248,8.226105,-9.580897,1.461250,-2.068641,3.504812,-9.150840,-1.420081,0.283321,8.246556,5.844306,3.009197,-6.720019,-2.745588,-7.997820,-3.009854,-1.181757,-0.129575,-0.960346,-5.087089,-7.343039,-8.161820,6.871033,9.369439,1.636847,6.027476,5.832579,8.666273,-4.265847,7.751444,-6.584283,7.008172,4.635928,4.525406,0.524925,-4.381370,9.989435,-7.835047,-3.722507,8.695119,-7.117284,-7.149470,-4.851300,-7.544511,9.776837,7.305915,3.418969,0.951141,-4.170220,2.710931,-2.643898,-9.119061,-6.445873,5.635111,-2.632089,-5.477217,8.459604,-9.318688,-4.343938,-0.893833,-5.995969,5.475778,3.282585,-0.551754,3.692530,3.924982,-3.982239,3.949665,2.453225,2.925198,2.062974,-3.060919,-8.752811,-3.686259,3.375451,1.636572,5.403463,-6.428397,3.369337,-3.221109,-8.174349,-6.096846,9.980954,3.932431,-4.335904,3.543073,-3.811007,-8.672754,-7.338109,1.593185,-8.209200,-4.509487,5.191771,-6.152618,6.110218,4.090321,-3.106441,-2.252392,9.685941,-4.265182,-6.976268,6.255311,-8.260177,-4.354019,6.658576,-7.749288,-2.673127,8.984601,8.107898,-1.140039,-8.723219,-0.576496,5.443211,6.218780,-7.413992,6.340171,0.202023,7.456958,-2.486316,-0.970478,9.664211,0.825786,4.406418,2.335330,-6.469551,-0.921803,7.607313,-9.307941,8.792807,9.245828,3.872012,4.059037,-9.677044,-1.588248,-3.074218,-0.022765,-6.634296,7.974692,-0.284838,-8.661080,-5.243684,6.545518,-7.495185,-1.888890,0.657285,8.066511,-7.148288,3.804102,-5.240199,-5.556673,3.376707,-2.966299,-5.616346,3.531395,1.024650,-1.686704,-0.391876,7.889921,7.482933,4.014624,-1.093091,1.430995,7.715729,9.457901,4.764258,-2.800816,-7.384041,-7.601776,-1.440465,7.245924,3.653484,2.348825,3.796504,-0.619070,-0.393449,-3.586382,5.090176,-0.157730,-1.412002,-1.967540,1.988485,-5.626924,2.911349,-2.814884,8.632179,2.651770,5.129653,-0.262288,-5.545269,0.562758,-0.755447,3.422649,-3.741489,-2.193238,4.950698,-7.993377,1.783581,-9.357604,9.087161,-7.866336,-5.550834,7.286013,-4.585322,-2.259502,6.703248,-1.356715,3.748119,4.603102,4.072800,4.104607,-0.482214,3.705299,-8.636594,-0.489101,-5.983335,-4.720099,0.843261,1.867978,-7.355438,-2.392166,1.295306,1.458751,-6.191825,-7.874251,7.735822,-6.011619,1.243565,8.590597,7.485192,3.139326,3.200395,-8.394738,-3.244314,-7.550962,4.030779,-1.709340,3.458063,-5.780310,-5.781287,4.564034,-4.468638,5.599653,6.038576,5.477849,-9.786806,4.627226,5.481396,-4.667275,0.762915,-4.760084,6.620758,0.385159,-0.887165,-3.916533,1.476839,-2.700893,8.257517,5.784044,8.995313,5.609400,-4.646131,9.018191,-6.508463,0.223835,-2.851597,9.739895,-2.871689,8.034725,-5.668530,7.715975,1.105575,8.581411,4.408301,-6.459797,0.378528,-8.830467,-0.886925,0.297026,-9.652159,-5.105083,-5.913560,-1.269376,-6.320749,-1.856724,-3.946497,-7.781448,2.053426,-0.202849,1.806342,9.449762,1.290216,-1.447934,9.946989,-5.707843,-1.364723,4.993690,-9.798339,5.999344,4.792041,6.743138,5.411120,5.045857,0.588133,3.874879,-7.283917,-2.347008,-7.191545,1.042158,-1.349024,0.790338,-9.903642,-2.742177,9.162790,-1.346734,8.782212,-6.785464,3.514784,8.444140,1.169285,7.733803,-7.250657,4.246115,-9.369038,-0.330057,7.139094,7.406109,-9.609212,-4.426522,0.162344,-0.320826,8.320080,6.415857,6.428039,0.761791,3.113363,-8.949487,-6.637360,9.330932,6.505778,-0.301394,2.592477,-9.565431,9.807264,6.781805,0.706594,3.275770,-4.752697,-8.827996,8.321582,7.861260,-0.944012,-5.621423,1.013660,-0.095325,-7.693854,0.839160,-7.057778,6.440828,8.468941,2.103764,8.144106,2.002815,6.410117,1.655626,8.059898,-2.911408,-3.978703,2.162531,-3.060928,-8.074456,-3.987066,-4.251482,-7.712321,-9.845619,8.489388,-7.806757,-0.530095,-6.174310,0.348451,-1.283320,-9.216052,3.783670,-3.446221,5.210153,-2.340385,2.723510,9.354510,9.367256,6.478878,7.513261,0.183629,8.987128,0.557762,-7.993910,7.968724,-0.980056,9.260411,2.661419,-4.954444,-3.282977,-0.911544,1.867995,5.531704,7.548474,-5.554408,4.750975,9.655067,6.534888,4.459586,6.655634,-8.530081,-4.927894,2.091466,4.929999,-8.784369,-3.392229,6.578318,0.805558,4.121210,-5.179258,1.352147,7.237084,-8.841179,-5.372420,-7.463661,3.188852,6.478478,-5.516186,7.680695,-8.229168], dtype = "float64")#candidate|24609|(832,)|const|float64
call_24606 = relay.TupleGetItem(func_20115_call(relay.reshape(const_24607.astype('uint16'), [14, 2, 5]), relay.reshape(const_24608.astype('uint64'), [130,]), relay.reshape(const_24609.astype('float64'), [832,]), ), 7)
call_24610 = relay.TupleGetItem(func_20119_call(relay.reshape(const_24607.astype('uint16'), [14, 2, 5]), relay.reshape(const_24608.astype('uint64'), [130,]), relay.reshape(const_24609.astype('float64'), [832,]), ), 7)
output = relay.Tuple([call_24602,call_24606,const_24607,const_24608,const_24609,])
output2 = relay.Tuple([call_24603,call_24610,const_24607,const_24608,const_24609,])
func_24616 = relay.Function([], output)
mod['func_24616'] = func_24616
mod = relay.transform.InferType()(mod)
mutated_mod['func_24616'] = func_24616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_24616_call = mutated_mod.get_global_var('func_24616')
call_24617 = func_24616_call()
output = call_24617
func_24618 = relay.Function([], output)
mutated_mod['func_24618'] = func_24618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15426_call = mod.get_global_var('func_15426')
func_15428_call = mutated_mod.get_global_var('func_15428')
call_24670 = func_15426_call()
call_24671 = func_15426_call()
output = relay.Tuple([call_24670,])
output2 = relay.Tuple([call_24671,])
func_24674 = relay.Function([], output)
mod['func_24674'] = func_24674
mod = relay.transform.InferType()(mod)
output = func_24674()
func_24675 = relay.Function([], output)
mutated_mod['func_24675'] = func_24675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21842_call = mod.get_global_var('func_21842')
func_21843_call = mutated_mod.get_global_var('func_21843')
call_24682 = relay.TupleGetItem(func_21842_call(), 1)
call_24683 = relay.TupleGetItem(func_21843_call(), 1)
func_7792_call = mod.get_global_var('func_7792')
func_7796_call = mutated_mod.get_global_var('func_7796')
var_24697 = relay.var("var_24697", dtype = "float64", shape = (264,))#candidate|24697|(264,)|var|float64
var_24698 = relay.var("var_24698", dtype = "float32", shape = (750,))#candidate|24698|(750,)|var|float32
call_24696 = relay.TupleGetItem(func_7792_call(relay.reshape(var_24697.astype('float64'), [6, 4, 11]), relay.reshape(var_24698.astype('float32'), [1, 750]), ), 1)
call_24699 = relay.TupleGetItem(func_7796_call(relay.reshape(var_24697.astype('float64'), [6, 4, 11]), relay.reshape(var_24698.astype('float32'), [1, 750]), ), 1)
uop_24701 = relay.sinh(call_24696.astype('float64')) # shape=(1, 750)
uop_24703 = relay.sinh(call_24699.astype('float64')) # shape=(1, 750)
var_24720 = relay.var("var_24720", dtype = "float64", shape = (10, 750))#candidate|24720|(10, 750)|var|float64
bop_24721 = relay.right_shift(uop_24701.astype('int32'), var_24720.astype('int32')) # shape=(10, 750)
bop_24724 = relay.right_shift(uop_24703.astype('int32'), var_24720.astype('int32')) # shape=(10, 750)
output = relay.Tuple([call_24682,var_24697,var_24698,bop_24721,])
output2 = relay.Tuple([call_24683,var_24697,var_24698,bop_24724,])
func_24729 = relay.Function([var_24697,var_24698,var_24720,], output)
mod['func_24729'] = func_24729
mod = relay.transform.InferType()(mod)
var_24730 = relay.var("var_24730", dtype = "float64", shape = (264,))#candidate|24730|(264,)|var|float64
var_24731 = relay.var("var_24731", dtype = "float32", shape = (750,))#candidate|24731|(750,)|var|float32
var_24732 = relay.var("var_24732", dtype = "float64", shape = (10, 750))#candidate|24732|(10, 750)|var|float64
output = func_24729(var_24730,var_24731,var_24732,)
func_24733 = relay.Function([var_24730,var_24731,var_24732,], output)
mutated_mod['func_24733'] = func_24733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19297_call = mod.get_global_var('func_19297')
func_19298_call = mutated_mod.get_global_var('func_19298')
call_24738 = relay.TupleGetItem(func_19297_call(), 1)
call_24739 = relay.TupleGetItem(func_19298_call(), 1)
func_22490_call = mod.get_global_var('func_22490')
func_22492_call = mutated_mod.get_global_var('func_22492')
var_24777 = relay.var("var_24777", dtype = "float64", shape = (832,))#candidate|24777|(832,)|var|float64
call_24776 = relay.TupleGetItem(func_22490_call(relay.reshape(var_24777.astype('float64'), [832,])), 0)
call_24778 = relay.TupleGetItem(func_22492_call(relay.reshape(var_24777.astype('float64'), [832,])), 0)
output = relay.Tuple([call_24738,call_24776,var_24777,])
output2 = relay.Tuple([call_24739,call_24778,var_24777,])
func_24780 = relay.Function([var_24777,], output)
mod['func_24780'] = func_24780
mod = relay.transform.InferType()(mod)
var_24781 = relay.var("var_24781", dtype = "float64", shape = (832,))#candidate|24781|(832,)|var|float64
output = func_24780(var_24781)
func_24782 = relay.Function([var_24781], output)
mutated_mod['func_24782'] = func_24782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12653_call = mod.get_global_var('func_12653')
func_12655_call = mutated_mod.get_global_var('func_12655')
call_24798 = func_12653_call()
call_24799 = func_12653_call()
output = relay.Tuple([call_24798,])
output2 = relay.Tuple([call_24799,])
func_24815 = relay.Function([], output)
mod['func_24815'] = func_24815
mod = relay.transform.InferType()(mod)
output = func_24815()
func_24816 = relay.Function([], output)
mutated_mod['func_24816'] = func_24816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14426_call = mod.get_global_var('func_14426')
func_14427_call = mutated_mod.get_global_var('func_14427')
call_24836 = func_14426_call()
call_24837 = func_14426_call()
output = relay.Tuple([call_24836,])
output2 = relay.Tuple([call_24837,])
func_24869 = relay.Function([], output)
mod['func_24869'] = func_24869
mod = relay.transform.InferType()(mod)
mutated_mod['func_24869'] = func_24869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_24869_call = mutated_mod.get_global_var('func_24869')
call_24870 = func_24869_call()
output = call_24870
func_24871 = relay.Function([], output)
mutated_mod['func_24871'] = func_24871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17982_call = mod.get_global_var('func_17982')
func_17983_call = mutated_mod.get_global_var('func_17983')
call_24911 = func_17982_call()
call_24912 = func_17982_call()
output = relay.Tuple([call_24911,])
output2 = relay.Tuple([call_24912,])
func_24930 = relay.Function([], output)
mod['func_24930'] = func_24930
mod = relay.transform.InferType()(mod)
output = func_24930()
func_24931 = relay.Function([], output)
mutated_mod['func_24931'] = func_24931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17173_call = mod.get_global_var('func_17173')
func_17174_call = mutated_mod.get_global_var('func_17174')
call_24976 = relay.TupleGetItem(func_17173_call(), 0)
call_24977 = relay.TupleGetItem(func_17174_call(), 0)
output = relay.Tuple([call_24976,])
output2 = relay.Tuple([call_24977,])
func_25024 = relay.Function([], output)
mod['func_25024'] = func_25024
mod = relay.transform.InferType()(mod)
output = func_25024()
func_25025 = relay.Function([], output)
mutated_mod['func_25025'] = func_25025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17702_call = mod.get_global_var('func_17702')
func_17704_call = mutated_mod.get_global_var('func_17704')
call_25031 = relay.TupleGetItem(func_17702_call(), 0)
call_25032 = relay.TupleGetItem(func_17704_call(), 0)
func_15911_call = mod.get_global_var('func_15911')
func_15915_call = mutated_mod.get_global_var('func_15915')
var_25037 = relay.var("var_25037", dtype = "uint32", shape = ())#candidate|25037|()|var|uint32
var_25038 = relay.var("var_25038", dtype = "uint32", shape = (24,))#candidate|25038|(24,)|var|uint32
var_25039 = relay.var("var_25039", dtype = "uint64", shape = (26, 5))#candidate|25039|(26, 5)|var|uint64
call_25036 = relay.TupleGetItem(func_15911_call(relay.reshape(var_25037.astype('uint32'), []), relay.reshape(var_25038.astype('uint32'), [24,]), relay.reshape(var_25039.astype('uint64'), [130,]), ), 0)
call_25040 = relay.TupleGetItem(func_15915_call(relay.reshape(var_25037.astype('uint32'), []), relay.reshape(var_25038.astype('uint32'), [24,]), relay.reshape(var_25039.astype('uint64'), [130,]), ), 0)
func_7792_call = mod.get_global_var('func_7792')
func_7796_call = mutated_mod.get_global_var('func_7796')
var_25052 = relay.var("var_25052", dtype = "float64", shape = (264,))#candidate|25052|(264,)|var|float64
var_25053 = relay.var("var_25053", dtype = "float32", shape = (1, 750))#candidate|25053|(1, 750)|var|float32
call_25051 = relay.TupleGetItem(func_7792_call(relay.reshape(var_25052.astype('float64'), [6, 4, 11]), relay.reshape(var_25053.astype('float32'), [1, 750]), ), 1)
call_25054 = relay.TupleGetItem(func_7796_call(relay.reshape(var_25052.astype('float64'), [6, 4, 11]), relay.reshape(var_25053.astype('float32'), [1, 750]), ), 1)
output = relay.Tuple([call_25031,call_25036,var_25037,var_25038,var_25039,call_25051,var_25052,var_25053,])
output2 = relay.Tuple([call_25032,call_25040,var_25037,var_25038,var_25039,call_25054,var_25052,var_25053,])
func_25059 = relay.Function([var_25037,var_25038,var_25039,var_25052,var_25053,], output)
mod['func_25059'] = func_25059
mod = relay.transform.InferType()(mod)
mutated_mod['func_25059'] = func_25059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_25059_call = mutated_mod.get_global_var('func_25059')
var_25061 = relay.var("var_25061", dtype = "uint32", shape = ())#candidate|25061|()|var|uint32
var_25062 = relay.var("var_25062", dtype = "uint32", shape = (24,))#candidate|25062|(24,)|var|uint32
var_25063 = relay.var("var_25063", dtype = "uint64", shape = (26, 5))#candidate|25063|(26, 5)|var|uint64
var_25064 = relay.var("var_25064", dtype = "float64", shape = (264,))#candidate|25064|(264,)|var|float64
var_25065 = relay.var("var_25065", dtype = "float32", shape = (1, 750))#candidate|25065|(1, 750)|var|float32
call_25060 = func_25059_call(var_25061,var_25062,var_25063,var_25064,var_25065,)
output = call_25060
func_25066 = relay.Function([var_25061,var_25062,var_25063,var_25064,var_25065,], output)
mutated_mod['func_25066'] = func_25066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11459_call = mod.get_global_var('func_11459')
func_11460_call = mutated_mod.get_global_var('func_11460')
call_25157 = relay.TupleGetItem(func_11459_call(), 0)
call_25158 = relay.TupleGetItem(func_11460_call(), 0)
func_19749_call = mod.get_global_var('func_19749')
func_19753_call = mutated_mod.get_global_var('func_19753')
var_25160 = relay.var("var_25160", dtype = "float64", shape = ())#candidate|25160|()|var|float64
const_25161 = relay.const([[4.652774,3.285549,-4.966490,-9.992493,6.358382,-4.109320,-4.566955,-0.474408,1.303692,-0.776274,6.502639,0.354876,-3.160224,-2.979652,8.494218,-9.563692,-9.731023,-6.719305,-9.998663,-5.181124,9.538713,-9.438122,3.366607,-9.162647,9.471970,-6.012009,2.898281,-7.182939,-5.351691,8.087357,9.995905,9.177769],[1.394601,8.906999,-3.644471,1.736096,-4.299251,-2.777801,-3.592985,-0.488147,9.470827,5.532280,-0.619990,-0.161283,-7.261194,0.967008,3.993186,9.432078,-5.213811,7.061888,6.266850,-8.825014,-5.192728,5.946583,4.747010,-7.424626,5.010411,6.303529,-7.511940,-6.209772,8.061619,-2.231073,-7.377486,5.599805]], dtype = "float64")#candidate|25161|(2, 32)|const|float64
call_25159 = func_19749_call(relay.reshape(var_25160.astype('float64'), []), relay.reshape(const_25161.astype('float64'), [8, 8, 1]), )
call_25162 = func_19749_call(relay.reshape(var_25160.astype('float64'), []), relay.reshape(const_25161.astype('float64'), [8, 8, 1]), )
output = relay.Tuple([call_25157,call_25159,var_25160,const_25161,])
output2 = relay.Tuple([call_25158,call_25162,var_25160,const_25161,])
func_25179 = relay.Function([var_25160,], output)
mod['func_25179'] = func_25179
mod = relay.transform.InferType()(mod)
mutated_mod['func_25179'] = func_25179
mutated_mod = relay.transform.InferType()(mutated_mod)
var_25180 = relay.var("var_25180", dtype = "float64", shape = ())#candidate|25180|()|var|float64
func_25179_call = mutated_mod.get_global_var('func_25179')
call_25181 = func_25179_call(var_25180)
output = call_25181
func_25182 = relay.Function([var_25180], output)
mutated_mod['func_25182'] = func_25182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21502_call = mod.get_global_var('func_21502')
func_21504_call = mutated_mod.get_global_var('func_21504')
call_25186 = relay.TupleGetItem(func_21502_call(), 2)
call_25187 = relay.TupleGetItem(func_21504_call(), 2)
output = relay.Tuple([call_25186,])
output2 = relay.Tuple([call_25187,])
func_25190 = relay.Function([], output)
mod['func_25190'] = func_25190
mod = relay.transform.InferType()(mod)
mutated_mod['func_25190'] = func_25190
mutated_mod = relay.transform.InferType()(mutated_mod)
func_25190_call = mutated_mod.get_global_var('func_25190')
call_25191 = func_25190_call()
output = call_25191
func_25192 = relay.Function([], output)
mutated_mod['func_25192'] = func_25192
mutated_mod = relay.transform.InferType()(mutated_mod)
var_25195 = relay.var("var_25195", dtype = "bool", shape = ())#candidate|25195|()|var|bool
var_25196 = relay.var("var_25196", dtype = "bool", shape = (9, 5, 5))#candidate|25196|(9, 5, 5)|var|bool
bop_25197 = relay.logical_and(var_25195.astype('bool'), var_25196.astype('bool')) # shape=(9, 5, 5)
func_24042_call = mod.get_global_var('func_24042')
func_24044_call = mutated_mod.get_global_var('func_24044')
const_25202 = relay.const([[3,-8,3,-10,-1,6,10,-2,-1,-3,5,-6,-8,2,6,-8,-1,9,-10,1,-7,1,-6,-8,-9,-3,-1,-7,-9,-10,2,-5,-6,-1,3,-10,-6,8,4,-8,7,1,10,6,6,4,5,3,4,-10,3,-7,-10,2,1,9,1,5,-8,1,-6,-2,-4,4,8,-5,3,1,-7,7,4,3,6,9,8,7,-4,-8,-3,-8,-8,1,7,5,6,-3,10,10,-3,-1,8,8,7,4,-10,-1,7,10,-6,1,6,4,9,1,2,6,10,-4,10,8,-10,8,1,-5,-10,-8,-10,2,8,-3,7,-2,3,-5,4,5,-10,-5,-1,-7,9,-9,10,10,7,8,-5,1,6,3,9,6,-10,-10,3,2,-3,-3,-4,-10,-6,-7,7,-9,5,-3,-7,-4,9,-8,3,4,-2,-10,-8,1,7,7,7,-8,-7,7,-9,-2,6,1,-1,7,2,4,-8,-5,1,10,7,2,-9,9,1,8,-3,-7,4,10,1,-5,6,-5,-4,-7,-3,7,8,-3,5,-6,-10,3,-7,1,8,9,8,3,9,4,-10,7,5,9,-1,10,-10,-7,-9,-6,-4,1,9,5,7,-1,10,-7],[5,-9,-2,8,-4,-8,-3,10,-1,1,-6,-7,6,9,5,-3,3,9,-2,7,3,-9,-2,-4,-1,-5,1,-7,2,-5,4,-9,1,-4,6,9,1,-4,8,-5,4,5,2,2,-9,-10,8,-2,7,2,-9,3,-10,2,6,8,-7,-3,4,-4,-6,-6,6,-3,-3,-8,-7,-2,-7,-6,2,-1,6,2,3,5,-4,4,-10,-5,-4,-7,2,-8,6,2,-10,10,8,10,-10,3,-7,-6,-5,-9,-3,-2,8,6,7,-3,-2,5,-5,-3,9,10,2,2,-8,10,9,-10,1,-2,-3,-5,6,-5,6,-7,-4,2,5,-5,7,6,-7,-5,-2,9,2,10,-6,10,-3,-1,-5,4,7,5,-7,1,7,6,-3,-5,-1,-2,4,-10,-10,-5,-4,-7,8,-6,-2,1,-1,9,10,-8,2,7,-3,-2,-8,7,4,4,7,7,4,-1,2,10,7,-4,-7,3,-10,2,2,1,-5,-7,2,4,-3,3,-6,-1,9,1,6,6,1,-5,7,-8,-10,5,-1,10,-5,-1,-3,3,8,10,10,-2,-3,-1,-3,-5,3,5,-10,-10,-7,5,1,-6,3,-3,-3,1,3,8,-10,9],[2,9,-10,-6,-10,-8,10,2,-9,4,1,10,9,10,-1,-5,6,7,-5,-2,4,7,-4,-7,5,5,-9,10,10,-7,2,6,-8,-5,-5,-9,8,5,5,3,1,6,2,8,-7,-5,-9,-8,-5,3,1,-1,5,9,5,-10,1,-8,1,4,-5,8,1,2,-10,-8,-6,-7,6,-3,-9,9,10,-2,-7,10,7,-5,-5,-6,1,-3,4,10,-8,-1,7,-7,-9,-7,-7,-6,6,-3,-10,7,3,-10,1,-7,4,-4,-7,-9,1,-5,-4,1,4,-4,-2,-6,10,4,-6,10,10,-3,6,5,8,4,-1,-4,10,7,-9,-9,-9,-2,-5,-4,-6,-3,-9,-10,8,-8,10,6,-4,-1,8,-3,4,-1,-10,3,-2,-10,5,-7,-3,-6,1,-10,6,7,3,8,-7,-6,4,5,-8,-8,-5,7,-1,9,-4,-4,-2,2,-3,3,-1,-9,8,4,8,-8,6,1,10,-9,10,-5,-6,-8,-9,-1,7,9,3,-3,5,6,-9,-9,6,5,3,8,7,8,-6,8,8,-1,1,6,7,7,8,7,6,-9,10,-6,-3,4,-3,5,10,-4,1,-6,1,-4,-9,-2,3,-4],[9,1,-6,3,7,-3,-5,-7,9,5,-7,9,-2,-3,-2,-9,8,-5,4,6,-8,-8,7,1,1,6,-7,-7,7,5,8,-2,-3,-1,-7,-10,-7,1,-6,-10,8,-6,-2,-5,3,-8,-3,9,9,7,-8,-2,5,-7,-6,9,-2,1,10,-2,-6,-5,-3,7,6,-8,8,7,3,-8,2,3,6,9,9,-8,2,-4,-10,6,4,10,4,-7,3,6,-5,-1,-4,-7,-2,8,2,8,4,8,8,9,-5,-8,6,-6,-2,3,7,-9,-7,-2,10,1,-4,1,4,3,-10,10,3,-6,2,3,1,8,-8,7,8,3,4,5,5,9,-9,1,2,-8,-9,6,2,8,-2,-7,10,4,3,-3,-9,4,-9,1,2,-8,2,-1,-7,4,1,-10,3,-6,-7,-7,-9,-4,7,4,7,-10,-5,3,7,1,-3,10,9,4,-5,2,-3,-4,2,-10,9,9,-1,8,-2,-8,4,-10,-4,-8,-7,-4,-7,-9,-6,9,8,-1,-10,9,-10,8,-6,6,3,10,-4,-10,-3,-1,7,2,10,6,-2,4,1,5,-10,-9,3,-5,-4,-10,-4,-5,5,-8,-3,-6,7,-7,4,8],[-1,9,6,4,6,8,7,1,-3,6,3,-2,-4,1,-1,1,5,9,-1,5,7,7,9,5,-9,9,-4,2,-10,-5,-1,-6,-4,10,-7,5,8,-7,2,-10,-4,-2,-8,6,9,-10,6,9,-10,-7,5,1,4,2,-2,6,1,-6,-4,8,4,4,-3,-1,-3,10,-2,1,10,5,-6,-8,1,-8,6,8,4,-1,-6,-2,3,-7,4,5,3,-6,1,8,9,6,-1,-7,-6,-6,1,1,1,-10,-6,-8,3,10,7,-7,-5,4,-5,3,-7,4,-6,-1,3,-3,-6,-7,-5,4,-8,-10,2,-9,5,10,10,2,-9,4,-6,-10,-7,1,8,6,6,9,2,-7,-1,-10,3,8,9,-3,-8,-7,-9,-9,-6,3,2,2,-1,10,-7,4,6,-1,5,-2,-6,9,7,-4,-4,-5,-10,-2,-7,2,7,-4,-9,10,9,-8,8,2,-9,8,-5,2,1,6,-6,-10,6,6,8,-1,7,-6,1,10,-6,3,-5,-7,-9,-2,1,10,7,5,3,6,7,4,-10,8,-5,7,8,-6,-5,5,-2,5,2,-9,-8,-2,-7,-5,-3,2,3,-7,1,9,-2,4,-1,5],[9,-6,-9,1,7,2,8,7,1,-4,9,-10,10,-7,3,4,-8,-8,-1,2,7,-7,5,-8,-9,-1,-10,9,5,10,-8,9,-7,2,9,5,5,1,-7,8,-3,-2,2,-2,-7,-6,-9,2,3,3,7,8,-1,4,1,-3,5,-7,9,7,-6,-5,-9,10,-3,5,-2,-6,3,-10,-5,9,10,-8,-7,-7,7,9,-10,-9,-3,-7,-7,-5,-4,-5,10,7,-1,-9,10,-3,-9,-1,1,-4,-4,9,-3,-4,-1,-5,4,-1,7,-7,-7,3,5,6,6,10,10,-1,-6,-1,-5,-8,-8,-8,-8,-3,-5,10,2,8,6,6,-7,-1,6,-10,8,-2,6,5,-2,8,5,-9,-5,-5,-5,9,9,-7,-3,8,4,2,-7,-3,-5,10,2,-9,6,-8,-4,-5,8,-10,10,4,5,3,3,4,-8,10,-4,6,10,3,10,6,1,-9,-3,4,-9,1,2,1,-10,9,-7,-7,9,-10,-9,7,2,10,8,-3,-10,2,2,3,2,7,9,6,-4,-8,-3,-3,-10,-2,9,-9,2,3,3,-5,2,-6,-5,-10,1,10,-1,-10,-7,1,-8,5,10,-3,5,-9,9,7],[-8,-1,-5,2,7,8,4,10,-8,1,4,-2,-1,6,-6,2,-10,-2,7,10,6,7,-7,-4,-3,-4,9,6,9,-10,4,9,-6,-10,5,-8,-10,-2,4,-4,1,4,8,-9,-3,-1,2,3,-9,2,7,-6,7,-5,-6,-5,-1,-8,-10,-5,6,10,-4,-8,7,8,2,-2,3,-7,8,-5,-3,-5,10,8,4,5,-2,-2,5,-3,-3,5,4,-7,5,9,-5,-3,-6,2,-8,9,-2,-8,-10,-3,8,1,9,4,9,2,-10,10,5,-8,-1,-10,10,9,1,-5,1,10,-3,3,-8,6,7,3,-8,-4,2,3,4,-3,5,1,-5,5,3,-10,1,8,3,-2,6,3,2,9,-7,8,-10,7,1,-3,-10,-5,2,2,7,-10,2,1,7,-1,-4,-6,9,2,-7,-4,2,9,7,9,7,-8,-3,6,-1,-4,-5,3,-6,-6,10,10,-1,5,-2,1,6,-10,-10,-10,-3,-8,-7,-4,6,5,-10,-9,4,9,10,7,1,6,-6,-2,3,7,3,-2,-1,-6,-10,2,-10,-1,-2,8,-10,5,-3,4,9,5,-5,2,3,-7,-4,8,3,-6,-2,8,-1,5]], dtype = "uint32")#candidate|25202|(7, 234)|const|uint32
call_25201 = func_24042_call(relay.reshape(const_25202.astype('uint32'), [13, 14, 9]))
call_25203 = func_24042_call(relay.reshape(const_25202.astype('uint32'), [13, 14, 9]))
bop_25210 = relay.power(var_25195.astype('float32'), const_25202.astype('float32')) # shape=(7, 234)
uop_25214 = relay.cos(const_25202.astype('float64')) # shape=(7, 234)
output = relay.Tuple([bop_25197,call_25201,bop_25210,uop_25214,])
output2 = relay.Tuple([bop_25197,call_25203,bop_25210,uop_25214,])
func_25219 = relay.Function([var_25195,var_25196,], output)
mod['func_25219'] = func_25219
mod = relay.transform.InferType()(mod)
mutated_mod['func_25219'] = func_25219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_25219_call = mutated_mod.get_global_var('func_25219')
var_25221 = relay.var("var_25221", dtype = "bool", shape = ())#candidate|25221|()|var|bool
var_25222 = relay.var("var_25222", dtype = "bool", shape = (9, 5, 5))#candidate|25222|(9, 5, 5)|var|bool
call_25220 = func_25219_call(var_25221,var_25222,)
output = call_25220
func_25223 = relay.Function([var_25221,var_25222,], output)
mutated_mod['func_25223'] = func_25223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16094_call = mod.get_global_var('func_16094')
func_16095_call = mutated_mod.get_global_var('func_16095')
call_25265 = relay.TupleGetItem(func_16094_call(), 2)
call_25266 = relay.TupleGetItem(func_16095_call(), 2)
uop_25267 = relay.exp(call_25265.astype('float64')) # shape=(6, 13, 14)
uop_25269 = relay.exp(call_25266.astype('float64')) # shape=(6, 13, 14)
func_697_call = mod.get_global_var('func_697')
func_701_call = mutated_mod.get_global_var('func_701')
const_25273 = relay.const([9,-6,-2,6,-10,-1,-9,-6,-10,-8,-4,-9,-3,2,-3,4,-7,-2,3,-10,-9,4,1,-2,-9,-3,9,7,-1,5,6,-3,-8,-1,-2,-6,4,-8,-1,8,-3,2,3,4,-8,9,6,8,-6,7,-2,9,-2,-2,7,3,-3,10,4,-1,2,-10,-1,-2,-7,-6,-1,-6,-10,-8,-10,-9,-7,10,-2,6,10,-2,-4,9,3,-10,-8,9,-7,-9,7,-10,6,8,1,-1,1,4,-8,-7,-6,-5,-3,6,-1,-7,-2,5,-8,-7,-8,-2,4,2,-6,-2,6,-1,-4,-1,4,7,6,4,-6,3,-9,-1,-8,6,-4,8,-8,2,-6,8,2,5,-7,2,-2,-7,9,-6,5,-2,-10,10,9,-9,5,-6,3,7,-2,5,-3,5,-4,-8,2,-7,-10,10], dtype = "uint64")#candidate|25273|(160,)|const|uint64
call_25272 = relay.TupleGetItem(func_697_call(relay.reshape(const_25273.astype('uint64'), [4, 5, 8]), relay.reshape(const_25273.astype('uint64'), [4, 5, 8]), ), 0)
call_25274 = relay.TupleGetItem(func_701_call(relay.reshape(const_25273.astype('uint64'), [4, 5, 8]), relay.reshape(const_25273.astype('uint64'), [4, 5, 8]), ), 0)
func_16632_call = mod.get_global_var('func_16632')
func_16635_call = mutated_mod.get_global_var('func_16635')
const_25284 = relay.const([8,4,-6,-10,-2,2,-4,-6,1,6,-8,8,-2,-2,-3,-3,-10,5,-2,9,-8,1,-7,2,-9,-5,-9,9,-7,8,-3,-3,8,9,4,5,10,-3,10,-6,6,-10,-6,8,-9,5,9,-6,-7,6,-4,3,-4,-8,-4,5,-8,4,-5,9,-1,7,2,5,-8,-1,2,6,-10,2,9,-5,4,2,4,-5,-8,2,-6,1,10,8,-4,9,9,10,-9,-6,4,4,1,-10,-2,9,1,-3,10,4,6,-9,-5,2,2,8,-7,-2,2,7,6,3,4,10,-7,-9,8,-7,-7,-6,8,6,8,4,-2,5,7,-5,4,-6,-10,4,-4,-10,10,3,1,5,-7,-9,-2,-7,2,9,-7,-7,-3,-6,1,-10,-1,-1,2,10,-7,-8,-5,7,7,3,2,-3,-8,1,-5,2,-6,10,9,9,1,4,-4,-1,-6,9,4,-2,-2,-4,6,5,-9,3,-5,3,-2,9,-7,-1,7,-10,1,-3,-4,10,-1,5,-9,7,3,-9,-8,-2,-1,5,-2,-8,6,6,8,-4,-10,-8,-9,3,6,6,-10,-8,-3,8,-9,-6,8,7,-9,-5,-9,-10,-10,10,-4,-4,9,7,5,5,4,9,5,-5,6,-3,-5,-5,5,4,6,-6,-8,-6,10,8,-5,5,-4,4,2,-7,10,1,1,-7,-1,-1,7,3,9,1,-10,-1,7,-4,-3,-6,-3,8,-2,1,9,-6,9,4,-3,-9,-3,5,8,-1,-10,-5,3,7,10,1,-9,-4,8,-4,4,4,-6,9,10,-6,-6,3,6,-7,9,-4,6,-7,-9,-5,-6,2,8,5,-3,8,2,9,3,-4,5,-1,7,5,-8,-1,-9,-6,4,7,-2,7,6,4,3,2,-6,-8,10,1,4,-2,-2,-10,-2,6,-1,10,10,-1,-1,-8,5,-10,-9,-2,-10,6,7,-2,4,-4,10,6,-7,-10,7,5,-6,-6,-3,-2,7,7,-5,-2,5,-5,10,-5,-6,7,-7,-7,5,-9,-6,-3,8,-6,7,1,-3,-8,-8,2,-10,-9,-9,-9,2,5,1,-2,6,-4,-5,6,1,-1,-9,-3,1,-5,10,7,3,1,-9,-5,-10,-9,-3,-3,1,5,6,-8,-2,7,8,-4,-5,-7,8,9,-2,-3,3,1,-9,-3,-4,3,-5,-6,6,6,-6,6,-6,10,-5,-2,8,-2,10,3,8,10,6,-8,9,-6,10,7,-8,3,1,-2,9,-5,1,4,3,7,-1,4,1,-5,1,-7,8,-2,7,7,8,-6,-3,2,-4,7,-4,-7,2,-7,1,-2,6,-9,10,1,-1,8,-7,10,-7,-9,10,7,-8,-5,-8,10,-2,7,7,9,4,2,10,-3,10,10,-9,-2,-1,6,7,-3,6,-3,7,5,-1,-5,8,10,1,8,6,7,-10,-7,10,5,10,-1,2,-8,-2,6,2,-9,-5,-3,8,10,-10,2,7,-7,7,-3,5,-4,6,-8,5,9,4,-2,-1,-10,-9,10,4,-2,7,-2,7,-9,5,1,-5,-9,-4,1,3,-6,-4,10,-6,-8,8,-3,-5,9,-10,-7,1,-3,-7,10,-4,4,-3,-7,-9,-9,-7,5,7,-2,-4,-1,7,2,6,5,8,-1,6,-9,-3,5,3,1,-3,6,-2,-6,10,-2,-10,10,6,9,9,10,-6,-1,-4,8,5,-7,-2,-7,-3,-1,-6,2,-4,8,9,-5,-3,-6,1,6,-10,5,8,-4,-1,-3,-8,10,4,-5,-6,-9,-9,5,9,-5,4,10,-2,-2,-1,-1,-8,3,9,-6,-10,-3,2,-6,9,1,-3,-7,5,-9,2,9,3,1,-10,6,-6,9,-6,10,-8,1,9,-8,5,5,9,7,-4,1,-9,-5,5,2,9,-7,2,8,-3,-8,-6,-8,-6,5,7,-5,-5,3,6,-1,9,4,5,-5,-10,1,-7,-9,5,-3,1,1,2,-6,-9,-3,-7,2,-1,-2,-9,7,1,-8,-1,9,1,-10,3,-1,-2,-1,-3,1,-9,7,6,-5,-3,3,8,-7,-1,-3,-2,-7,1,3,2,-10,-9,-10,-2,-1,-1,-8,-6,9,-2,2,-7,8,8,1,-7,10,7,-10,6,-3,-6,6,-8,1,-5,5,3,-9,-5,10,9,-10,9,-7,-1,-2,3,-1,10,2,7,9,-1,1,-7,9,-1,4,9,7,-4,-9,6,2,3,5,-1,10,-3,9,-3,5,7,6,-3,-8,-3,-5,-6,-8,3,7,-8,-8,-9,10,-7,-6,6,-2,8,-7,-6,1,-1,1,2,8,6,-10,2,6,5,-4,7,-2,-6,3,3,-4,-3,-8,2,5,-1,4,7,3,-4,-4,10,6,-7,8,5,6,-6,2,-2,5,-6,-7,8,4,6,5,-6,-4,9,4,-5,-1,7,-8,-2,2,-3,-10,8,5,6,2,8,-6,7,9,10,-2,5,4,2,-7,5,-5,3,-9,-9,-10,6,-4,-6,6,2,3,-7,-5,4,-5,9,-4,-2,-1,5,-8,9,-3,-4,9,6,-5,8,1,4,-3,-7,-7,-1,2,2,-6,-1,-4,-7,-4,6,5,9,-7,3,6,-6,-1,-3,-2,2,-6,6,-9,-4,5,2,3,7,6,10,10,-5,3,-3,-3,-5,-7,10,6,-10,-5,3,6,9,-8,4,-5,10,-8,-4,-7,1,-2,3,-6,-8,-7,-10,9,-5,-8,-8,9,-10,-2,-10,-5,-6,-4,4,-1,-1,-3,1,10,-10,2,-9,7,-8,6,-9,-8,10,1,-2,-4,3,3,9,10,2,-9,-5,-2,7,-10,3,-9,-8,4,-5,4,-6,-3,-2,6,5,7,-4,-10,9,5,-7,-2,9,6,6,3,9,-7,-7,5,8,1,-10,-3,2,-2,4,-4,2,8,-10,-8,-7,9,7,7,7,7,10,8,-10,2,4,9,-8,2,6,-6,-6,-8,-1,10,4,5,9,-7,-2,5,5,-2,8,10,3,-8,4,-3,2,3,3,9,1,-1,7,9,-9,-6,4,-3,-3,-7,9,-2,-5,7,10,10,-4,-4,-6,-4,5,-1,5,7,7,4,6,-6,-10,-9,-9,-4,9,-5,-3,1,8,-9,8,-2,2,10,4,10,-1,6,5,6,-10,-10,-9,-2,-3,-1,-9,-7,-10,10,4,-8,9,6,4,8,2,-6,9,9,1,4,-4,-2,7,-8,3,8,10,8,4,9,-5,9,2,-5,-10,4,9,8,-9,-9,-2,6,8,7,9,-10,-10,-8,6,7,4,10,9,-9,4,-3,-4,-10,1,6,5,6,-6,-10,-10,8,10,7,-6,8,-6,-8,-9,3,-8,-2,7,-8,4,5,9,-8,-3,-10,5,1,-10,2,-9,-1,-7,10,3,-9,8,-1,-9,-7,7,-1,7,4,5,9,2,-1,-3,3,8,2,-5,-4,5,-7,9,3,-2,-5,2,10,-4,-10,-9,2,6,5,9,4,-1,6,-8,9,-7,-8,-8,2,-7,-8,7,6,-6,-5,-10,-10,-1,-2,7,-1,-8,3,7,-8,8,-1,-8,8,-7,8,1,8,-6,1,4,8,-2,7,-4,2,-3,-9,-1,4,10,-3,1,5,4,1,-9,-7,7,8,9,5,4,-2,1,-1,9,3,7,-7,3,8,-6,3,-1,7,1,-3,-8,-10,-10,-3,8,8,6,-6,-3,1,1,3,4,-3,3,-2,8,1,6,8,-10,7,2,-4,-2,-4,-10,-7,6,3,-4,10,8,4,5,-6,-10,10,-10,9,-1,7,10,8,-3,-5,6,1,-9,10,8,-9,-10,-2,-3,-4,-4,6,4,9,-6,6,-2,-8,1,2,-3,-8,10,-3,1,-7,-8,-8,-8,-2,3,-8,5,3,3,7,-6,9,7,9,1,2,1,-4,8,5,1,4,9,-4,-3,-10,-6,-5,3,2,1,5,-5,-3,6,6,-1,-5,-8,-5,-8,1,4,-10,3,-2,5,8,-8,-6,-9,4,-3,-2,-8,3,10,1,-2,-2,2,-1,1,10,10,-6,8,-3,-8,1,2,3,10,7,-6,10,2,6,1,-5,-4,2,-2,3,9,-8,-10,4,-7,-5,-1,1,-6,-7,5,-8,4,10,-6,-9,-9,-8,10,-2,-5,7,1,7,7,2,5,-10,1,-6,7,2,4,6,1,10,4,-10,-7,2,-3,5,-4,7,-9,2,10,-1,-3,-8,-6,10,10,-4,-9,1,1,-9,5,2,-1,-1,10,7,10,8,6,5,-10,-2,-5,2,-3,3,-9,5,1,2,7,-5,-5,-2,-10,8,5,-8,5,6,-1,7,4,-1,-7,4,-2,-10,1,9,-8,-9,9,3,9,5,6,1,3,5,-5,-5,-8,-6,-8,10,4,-10,1,10,-3,-10,-6,-9,3,10,-2,6,9,-1,-9,-6,2,-7,-9,1,-1,-3,3,5,-5,-3,9,9,1,6,10,-4,-9,-5,9,2,-10,4,-6,-9,-3,10,-4,-9,-8,7,-8,2,4,-6,7,1,-3,-1,4,-10,2,7,8,3,3,-5,10,10,9,7,6,-3,4,7,-4,5,8,4,-9,3,-6,7,-8,-2,-3,-2,8,9,9,-10,-7,-9,-6,-1,9,-1,2,2,4,-6,-4,7,4,-2,4,-6,-4,5,9,8,-10,6,6,-4,4,1,-8,8,6,7,-1,-10,1,6,1,-9,-5,-5,-2,3,-8,-4,3,-10,-1,9,-9,6,2,9,7,4,-2,-5,5,2,2,-10,5,6,-7,7,-1,6,-4,9,-5,-5,10,-5,8,10,3,-7,-8,-4,5,10,4,-3,5,2,-3,-10,7,-9,3,6,-9,-6,-5,3,2,8,-1,4,3,7,5,10,-3,8,10,3,9,6,10,4,5,7,4,-4,-1,2,10,-7,-1,-10,1,10,-5,-1,-8,-8,-10,-8,8,1,5,-5,-5,8,9,9,-3,9,-7,-4,7,5,7,-2,-7,4,8,5,-4,-3,2,3,3,5,2,3,9,9,-5,-1,-5,4,-6,9,3,3,6,-5,7,6,-9,-1,1,6,-2,-8,-4,10,-3,-2,-3,-4,-10,-7,-8,6,-6,-8,8,4,-3,-7,-7,10,10,-6,4,3,6,-1,-4,2,6,8,-5,4,-7,8,-9,-3,8,-1,9,6,-5,10,4,1,3,1,-4,-8,5,-6,-4,-1,-10,5,-6,7,-6,1,10,-9,5,-2,5,1,-8,4,6,2,-8,5,8,7,10,5,2,-4,-1,6,-8,8,4,8,7,-5,-9,-1,4,-10,-8,4,-6,-6,5,-5,-1,-1,-4,4,-10,-6,-3,3,-7,-2,7,-4,6,-4,-4,-4,-1,-9,-3,-8,-3,-2,-3,6,10,-2,5,2,8,2,4,-6,-2,-3,1,10,6,-2,8,7,-5,-5,-7,-4,4,6,4,4,-10,-3,-6,4,-6,1,4,2,-8,-10,5,-1,-9,-6,10,1,4,-8,-8,4,-9,-9,-4,-2,7,1,-7,-8,9,9,3,9,5,-10,2,-8,1,-5,6,9,-1,-5,3,5,7,-9,-4,-8,8,2,3,10,-7,1,2,9,10,-2,-7,-3,10,5,-2,5,-2,-7,-8,1,4,1,9,1,-5,-2,-1,9,9,-5,8,9,8,-6,-7,-2,-8,8,4,-9,-4,3,6,-7,7,-5,4,8,-2,-6,1,9,-10,7,8,-5,6,8,-2,-8,6,8,7,-10,10,7,2,1,5,-8,-7,-5,-10,7,-5,3,-6,9,-4,-2,5,-6,-7,2,8,-5,2,-7,5,4,-7,-1,-7,6,-3,6,8,-6,-2,7,6,-6,-3,3,-7,10,-4,-6,-3,-4,1,-4,-3,-3,9,-6,3,-5,5,6,5,-5,-7,1,5,8,-5,-4,5,3,9,-8,1,1,-3,5,3,8,1,1,7,2,4,-10,3,-10,3,5,5,-10,-2,-6,-5,4,6,-3,-7,-2,-1,7,-8,-8,-8,6,8,-2,1,5,4,3,7,2,-9,2,-9,-5,9,-9,-8,-2,9,9,4,5,5,10,1,5,-8,-3,-7,5,4,5,-9,2,-3,-9,7,6,1,4,-8,6,-6,-5,9,-1,4,-7,-4,-2,-8,-5,6,-8,7,-2,1,-3,9,1,9,-9], dtype = "int32")#candidate|25284|(2340,)|const|int32
call_25283 = relay.TupleGetItem(func_16632_call(relay.reshape(const_25284.astype('int32'), [12, 13, 15]), relay.reshape(const_25284.astype('int32'), [12, 13, 15]), ), 4)
call_25285 = relay.TupleGetItem(func_16635_call(relay.reshape(const_25284.astype('int32'), [12, 13, 15]), relay.reshape(const_25284.astype('int32'), [12, 13, 15]), ), 4)
output = relay.Tuple([uop_25267,call_25272,const_25273,call_25283,const_25284,])
output2 = relay.Tuple([uop_25269,call_25274,const_25273,call_25285,const_25284,])
func_25302 = relay.Function([], output)
mod['func_25302'] = func_25302
mod = relay.transform.InferType()(mod)
output = func_25302()
func_25303 = relay.Function([], output)
mutated_mod['func_25303'] = func_25303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21648_call = mod.get_global_var('func_21648')
func_21649_call = mutated_mod.get_global_var('func_21649')
call_25363 = relay.TupleGetItem(func_21648_call(), 1)
call_25364 = relay.TupleGetItem(func_21649_call(), 1)
func_18580_call = mod.get_global_var('func_18580')
func_18582_call = mutated_mod.get_global_var('func_18582')
call_25371 = func_18580_call()
call_25372 = func_18580_call()
func_12223_call = mod.get_global_var('func_12223')
func_12228_call = mutated_mod.get_global_var('func_12228')
var_25386 = relay.var("var_25386", dtype = "int8", shape = (36, 1))#candidate|25386|(36, 1)|var|int8
var_25387 = relay.var("var_25387", dtype = "bool", shape = ())#candidate|25387|()|var|bool
var_25388 = relay.var("var_25388", dtype = "float64", shape = (4, 120))#candidate|25388|(4, 120)|var|float64
const_25389 = relay.const([4.609329,-0.890424,9.895047,-0.191918,-8.114488,-1.191869,-5.514253,1.053543,-9.504821,-1.702328,3.575026,4.112887,0.688401,-6.250665,7.169209,-1.456807,9.117969,-3.472530], dtype = "float32")#candidate|25389|(18,)|const|float32
call_25385 = relay.TupleGetItem(func_12223_call(relay.reshape(var_25386.astype('int8'), [9, 4, 1]), relay.reshape(var_25387.astype('bool'), []), relay.reshape(var_25388.astype('float64'), [480,]), relay.reshape(const_25389.astype('float32'), [18,]), ), 0)
call_25390 = relay.TupleGetItem(func_12228_call(relay.reshape(var_25386.astype('int8'), [9, 4, 1]), relay.reshape(var_25387.astype('bool'), []), relay.reshape(var_25388.astype('float64'), [480,]), relay.reshape(const_25389.astype('float32'), [18,]), ), 0)
func_12133_call = mod.get_global_var('func_12133')
func_12137_call = mutated_mod.get_global_var('func_12137')
const_25394 = relay.const([-9,6,-10,-9,-4,8,-8,-8,5,7,2,8,-8,7,1,9,-2,9,1,-1,-10,7,-1,4,-9,-9,7,-10,-8,2,-8,-1,-7,-2,-8,-3,4,-8,-7,1,3,6,9,8,5,-9,2,3,10,-10,-10,9,-5,9,9,-7,-1,-4,-10,-10,-10,-10,-10,-4,10,-3,6,-4,-6,4,-4,8,3,8,4,-2,10,9,-5,-2,-4,5,6,-3,-2,-10,8,-4,1,6,-9,-10,-10,-10,-1,-2,-9,8,-8,-8,8,7,-5,8,-2,-1,-5,-1,-3,2,5,-10,-2,-8,9,-1,3,2,-10,5,-7,4,-1,-6,7,-8,-3,5,-7,6,-10,-5,-6,4,-9,9,-7,-7,1,1,-1,-10,-7,10,9,-4,-2,1,-9,-5,4,-6,8,-9,5,6,-9,8,3,-2], dtype = "uint64")#candidate|25394|(160,)|const|uint64
call_25393 = relay.TupleGetItem(func_12133_call(relay.reshape(var_25387.astype('int16'), []), relay.reshape(const_25394.astype('uint64'), [160,]), ), 0)
call_25395 = relay.TupleGetItem(func_12137_call(relay.reshape(var_25387.astype('int16'), []), relay.reshape(const_25394.astype('uint64'), [160,]), ), 0)
output = relay.Tuple([call_25363,call_25371,call_25385,var_25386,var_25387,var_25388,const_25389,call_25393,const_25394,])
output2 = relay.Tuple([call_25364,call_25372,call_25390,var_25386,var_25387,var_25388,const_25389,call_25395,const_25394,])
func_25399 = relay.Function([var_25386,var_25387,var_25388,], output)
mod['func_25399'] = func_25399
mod = relay.transform.InferType()(mod)
mutated_mod['func_25399'] = func_25399
mutated_mod = relay.transform.InferType()(mutated_mod)
func_25399_call = mutated_mod.get_global_var('func_25399')
var_25401 = relay.var("var_25401", dtype = "int8", shape = (36, 1))#candidate|25401|(36, 1)|var|int8
var_25402 = relay.var("var_25402", dtype = "bool", shape = ())#candidate|25402|()|var|bool
var_25403 = relay.var("var_25403", dtype = "float64", shape = (4, 120))#candidate|25403|(4, 120)|var|float64
call_25400 = func_25399_call(var_25401,var_25402,var_25403,)
output = call_25400
func_25404 = relay.Function([var_25401,var_25402,var_25403,], output)
mutated_mod['func_25404'] = func_25404
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21290_call = mod.get_global_var('func_21290')
func_21292_call = mutated_mod.get_global_var('func_21292')
call_25481 = relay.TupleGetItem(func_21290_call(), 0)
call_25482 = relay.TupleGetItem(func_21292_call(), 0)
func_20439_call = mod.get_global_var('func_20439')
func_20442_call = mutated_mod.get_global_var('func_20442')
var_25488 = relay.var("var_25488", dtype = "float64", shape = (182,))#candidate|25488|(182,)|var|float64
const_25489 = relay.const(-9, dtype = "int16")#candidate|25489|()|const|int16
call_25487 = relay.TupleGetItem(func_20439_call(relay.reshape(var_25488.astype('float64'), [182,]), relay.reshape(const_25489.astype('int16'), []), ), 1)
call_25490 = relay.TupleGetItem(func_20442_call(relay.reshape(var_25488.astype('float64'), [182,]), relay.reshape(const_25489.astype('int16'), []), ), 1)
output = relay.Tuple([call_25481,call_25487,var_25488,const_25489,])
output2 = relay.Tuple([call_25482,call_25490,var_25488,const_25489,])
func_25492 = relay.Function([var_25488,], output)
mod['func_25492'] = func_25492
mod = relay.transform.InferType()(mod)
var_25493 = relay.var("var_25493", dtype = "float64", shape = (182,))#candidate|25493|(182,)|var|float64
output = func_25492(var_25493)
func_25494 = relay.Function([var_25493], output)
mutated_mod['func_25494'] = func_25494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17844_call = mod.get_global_var('func_17844')
func_17845_call = mutated_mod.get_global_var('func_17845')
call_25513 = relay.TupleGetItem(func_17844_call(), 0)
call_25514 = relay.TupleGetItem(func_17845_call(), 0)
output = call_25513
output2 = call_25514
func_25537 = relay.Function([], output)
mod['func_25537'] = func_25537
mod = relay.transform.InferType()(mod)
output = func_25537()
func_25538 = relay.Function([], output)
mutated_mod['func_25538'] = func_25538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14457_call = mod.get_global_var('func_14457')
func_14458_call = mutated_mod.get_global_var('func_14458')
call_25568 = func_14457_call()
call_25569 = func_14457_call()
func_25190_call = mod.get_global_var('func_25190')
func_25192_call = mutated_mod.get_global_var('func_25192')
call_25600 = relay.TupleGetItem(func_25190_call(), 0)
call_25601 = relay.TupleGetItem(func_25192_call(), 0)
func_25024_call = mod.get_global_var('func_25024')
func_25025_call = mutated_mod.get_global_var('func_25025')
call_25609 = relay.TupleGetItem(func_25024_call(), 0)
call_25610 = relay.TupleGetItem(func_25025_call(), 0)
func_18119_call = mod.get_global_var('func_18119')
func_18121_call = mutated_mod.get_global_var('func_18121')
const_25616 = relay.const([[-9.410939,1.656974,3.128787,-7.334363,2.973338,7.452023,6.729406,-7.635292,8.643839,-5.320077,2.045338,4.416056,6.159861,9.453357],[-3.083152,-5.159783,3.495662,-8.751195,7.940048,-5.167099,9.229902,6.923686,-0.728259,-7.208954,-7.248722,-0.036611,-6.713695,9.656930],[-5.545780,-9.200793,6.305883,8.732715,-1.959590,8.666363,2.879032,-5.015580,2.288251,4.654401,3.279250,-0.692599,5.667785,-8.929070],[-0.500456,4.141703,-8.637084,4.563478,-6.573811,-4.646347,-2.195841,6.313032,6.970236,-4.836897,3.266341,-6.987363,5.921663,-0.498370],[8.705660,-5.064273,7.774554,3.551357,1.581065,9.065348,7.146216,-7.175545,7.379513,1.992687,2.172259,-8.314540,-0.027951,-1.955474],[2.668347,-3.754805,0.482739,-1.092335,-8.781702,-0.488348,-1.477540,-1.994334,6.298823,1.808156,-6.608303,7.184179,-0.488237,-0.308957],[0.834700,-3.168492,1.654065,5.732096,0.292500,9.819704,6.756922,-6.138135,8.151188,-5.483599,4.680235,-2.835764,-7.043698,-6.377724],[2.877683,8.490833,0.390649,3.080278,-2.564146,8.553737,-4.832807,-7.750127,-8.192918,3.481011,0.238350,-6.323585,9.771527,-4.584192],[-7.411769,-7.476955,1.975498,-2.129364,2.159628,1.589105,2.621684,0.780901,-8.220411,9.526080,-4.347854,-1.583115,-1.235042,1.268341],[4.051362,-6.845154,-8.684255,0.038077,-7.800018,-5.551656,3.974909,-6.254687,-1.776028,-5.611556,7.638152,6.418544,-4.061610,1.100203],[-1.284621,-0.156685,-1.404093,1.222621,6.991484,-7.194603,5.773681,1.598843,-8.270400,8.203502,-7.941324,0.852127,0.662516,9.192392],[2.897858,7.194154,3.420705,0.835213,-6.718443,-8.027295,-2.525802,8.180933,2.575958,-7.544840,-2.632371,-2.661199,-5.175204,-4.717299],[-2.870792,2.439131,-2.870356,3.028186,5.491486,3.884484,-5.285583,9.378585,-4.710662,-7.968614,-2.319782,-1.501030,-4.286281,3.223676]], dtype = "float64")#candidate|25616|(13, 14)|const|float64
call_25615 = relay.TupleGetItem(func_18119_call(relay.reshape(const_25616.astype('float64'), [182,])), 2)
call_25617 = relay.TupleGetItem(func_18121_call(relay.reshape(const_25616.astype('float64'), [182,])), 2)
output = relay.Tuple([call_25568,call_25600,call_25609,call_25615,const_25616,])
output2 = relay.Tuple([call_25569,call_25601,call_25610,call_25617,const_25616,])
func_25619 = relay.Function([], output)
mod['func_25619'] = func_25619
mod = relay.transform.InferType()(mod)
output = func_25619()
func_25620 = relay.Function([], output)
mutated_mod['func_25620'] = func_25620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14750_call = mod.get_global_var('func_14750')
func_14752_call = mutated_mod.get_global_var('func_14752')
call_25621 = relay.TupleGetItem(func_14750_call(), 0)
call_25622 = relay.TupleGetItem(func_14752_call(), 0)
func_23747_call = mod.get_global_var('func_23747')
func_23748_call = mutated_mod.get_global_var('func_23748')
call_25623 = relay.TupleGetItem(func_23747_call(), 1)
call_25624 = relay.TupleGetItem(func_23748_call(), 1)
uop_25639 = relay.log(call_25621.astype('float32')) # shape=(9, 8, 14)
uop_25641 = relay.log(call_25622.astype('float32')) # shape=(9, 8, 14)
uop_25656 = relay.tan(uop_25639.astype('float32')) # shape=(9, 8, 14)
uop_25658 = relay.tan(uop_25641.astype('float32')) # shape=(9, 8, 14)
output = relay.Tuple([call_25623,uop_25656,])
output2 = relay.Tuple([call_25624,uop_25658,])
func_25660 = relay.Function([], output)
mod['func_25660'] = func_25660
mod = relay.transform.InferType()(mod)
output = func_25660()
func_25661 = relay.Function([], output)
mutated_mod['func_25661'] = func_25661
mutated_mod = relay.transform.InferType()(mutated_mod)
var_25683 = relay.var("var_25683", dtype = "float32", shape = (16, 5, 2))#candidate|25683|(16, 5, 2)|var|float32
var_25684 = relay.var("var_25684", dtype = "float32", shape = (16, 5, 2))#candidate|25684|(16, 5, 2)|var|float32
bop_25685 = relay.mod(var_25683.astype('float32'), relay.reshape(var_25684.astype('float32'), relay.shape_of(var_25683))) # shape=(16, 5, 2)
func_15594_call = mod.get_global_var('func_15594')
func_15596_call = mutated_mod.get_global_var('func_15596')
call_25698 = func_15594_call()
call_25699 = func_15594_call()
var_25700 = relay.var("var_25700", dtype = "float64", shape = (15, 5, 5))#candidate|25700|(15, 5, 5)|var|float64
bop_25701 = relay.less(call_25698.astype('bool'), relay.reshape(var_25700.astype('bool'), relay.shape_of(call_25698))) # shape=(15, 5, 5)
bop_25704 = relay.less(call_25699.astype('bool'), relay.reshape(var_25700.astype('bool'), relay.shape_of(call_25699))) # shape=(15, 5, 5)
output = relay.Tuple([bop_25685,bop_25701,])
output2 = relay.Tuple([bop_25685,bop_25704,])
func_25707 = relay.Function([var_25683,var_25684,var_25700,], output)
mod['func_25707'] = func_25707
mod = relay.transform.InferType()(mod)
mutated_mod['func_25707'] = func_25707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_25707_call = mutated_mod.get_global_var('func_25707')
var_25709 = relay.var("var_25709", dtype = "float32", shape = (16, 5, 2))#candidate|25709|(16, 5, 2)|var|float32
var_25710 = relay.var("var_25710", dtype = "float32", shape = (16, 5, 2))#candidate|25710|(16, 5, 2)|var|float32
var_25711 = relay.var("var_25711", dtype = "float64", shape = (15, 5, 5))#candidate|25711|(15, 5, 5)|var|float64
call_25708 = func_25707_call(var_25709,var_25710,var_25711,)
output = call_25708
func_25712 = relay.Function([var_25709,var_25710,var_25711,], output)
mutated_mod['func_25712'] = func_25712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11833_call = mod.get_global_var('func_11833')
func_11835_call = mutated_mod.get_global_var('func_11835')
call_25728 = relay.TupleGetItem(func_11833_call(), 0)
call_25729 = relay.TupleGetItem(func_11835_call(), 0)
func_10716_call = mod.get_global_var('func_10716')
func_10720_call = mutated_mod.get_global_var('func_10720')
const_25751 = relay.const([False,True,False,False,True,True,True,True,True,False,False,False,False,True,False,True,False,False,True,False,True,False,False,True,True,True,False,False,False,False,True,False,False,False,False,True,True,True,False,False,True,True,False,False,False,True,True,False,True,False,True,False,False,True,True,True,False,True,True,False,False,True,True,False,True,True,True,False,True,True,False,False,False,False,False,False,True,True,True,False,True,False,False,True,True,False,True,False,True,False,False,True,True,True,True,False,True,False,False,False,False,False,False,False,True,True,True,False,False,False,True,False,False,True,True,True,True,False,True,True,True,False,False,False,True,False,True,False,False,True,False,False,False,True,True,True,False,False,True,False,False,False,False,False,False,False,True,True,False,True,False,True,True,True,False,False,True,True,True,True,False,True,False,False,False,True,True,False,True,True,True,True,True,True,True,True,True,False,True,False,True,True,True,False,False,True,True,True,False,False,True,True,True,True,True,False,False,True,False,True,False,True,False,True,True,True,True,False,True,False,False,True,True,False,True,False,True,False,True,False,False,False,True,False,True,False,False,True,True,False,False,True,False,False,True,True,True,False,True,True,False,False,False,True,False,True,True,True,False,True,True,False,True,False,False,True,True,False,False,False,True,True,False,True,True,True,False,True,True,True,False,True,True,False,False,True,True,False,True,True,True,False,False,False,True,False,True,False,True,False,False,False,True,False,True,False,True,True,True,False,False,True,True,False,True,False,True,True,False,False,False,True,True,False,True,False,True,True,False,False,True,False,False,False,True,True,False,False,False,False,True,False,True,False,False,True,False,False,False,False,False,False,True,True,True,True,True,False,False,True,False,True,False,False,True,True,True,True,True,True,True,False,True,True,True,False,False,True,False,False,False,False,False,True,False,True,False,True,True,False,True,True,True,True,True,False,False,False,False,True,True,True,False,True,False,True,True,False,False,True,False,False,True,True,False,True,False,False,True,False,True,False,True,False,True,True,True,True,True,True,False,True,False,False,False,True,True,True,True,False,False,False,False,True,True,False,True,True,True,False,True,False,False,True,False,True,False,True,False,True,False,False,False,True,True,False,False,False,True,True,False,True,True,True,True,False,True,False,False,False,False,True,False,False,False,True,True,False,False,True,False,True,True,False,False,False,True,False,True,False,True,True,False,True,False,True,True,False,True,True,False,True,True,True], dtype = "bool")#candidate|25751|(504,)|const|bool
call_25750 = relay.TupleGetItem(func_10716_call(relay.reshape(const_25751.astype('bool'), [8, 9, 7]), relay.reshape(const_25751.astype('bool'), [8, 9, 7]), ), 0)
call_25752 = relay.TupleGetItem(func_10720_call(relay.reshape(const_25751.astype('bool'), [8, 9, 7]), relay.reshape(const_25751.astype('bool'), [8, 9, 7]), ), 0)
func_21141_call = mod.get_global_var('func_21141')
func_21142_call = mutated_mod.get_global_var('func_21142')
call_25760 = func_21141_call()
call_25761 = func_21141_call()
output = relay.Tuple([call_25728,call_25750,const_25751,call_25760,])
output2 = relay.Tuple([call_25729,call_25752,const_25751,call_25761,])
func_25762 = relay.Function([], output)
mod['func_25762'] = func_25762
mod = relay.transform.InferType()(mod)
mutated_mod['func_25762'] = func_25762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_25762_call = mutated_mod.get_global_var('func_25762')
call_25763 = func_25762_call()
output = call_25763
func_25764 = relay.Function([], output)
mutated_mod['func_25764'] = func_25764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_24159_call = mod.get_global_var('func_24159')
func_24161_call = mutated_mod.get_global_var('func_24161')
call_25787 = relay.TupleGetItem(func_24159_call(), 0)
call_25788 = relay.TupleGetItem(func_24161_call(), 0)
func_13876_call = mod.get_global_var('func_13876')
func_13878_call = mutated_mod.get_global_var('func_13878')
call_25806 = func_13876_call()
call_25807 = func_13876_call()
output = relay.Tuple([call_25787,call_25806,])
output2 = relay.Tuple([call_25788,call_25807,])
func_25820 = relay.Function([], output)
mod['func_25820'] = func_25820
mod = relay.transform.InferType()(mod)
output = func_25820()
func_25821 = relay.Function([], output)
mutated_mod['func_25821'] = func_25821
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20068_call = mod.get_global_var('func_20068')
func_20069_call = mutated_mod.get_global_var('func_20069')
call_25888 = func_20068_call()
call_25889 = func_20068_call()
uop_25895 = relay.acos(call_25888.astype('float64')) # shape=(9, 11, 4)
uop_25897 = relay.acos(call_25889.astype('float64')) # shape=(9, 11, 4)
output = relay.Tuple([uop_25895,])
output2 = relay.Tuple([uop_25897,])
func_25907 = relay.Function([], output)
mod['func_25907'] = func_25907
mod = relay.transform.InferType()(mod)
mutated_mod['func_25907'] = func_25907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_25907_call = mutated_mod.get_global_var('func_25907')
call_25908 = func_25907_call()
output = call_25908
func_25909 = relay.Function([], output)
mutated_mod['func_25909'] = func_25909
mutated_mod = relay.transform.InferType()(mutated_mod)
func_22751_call = mod.get_global_var('func_22751')
func_22753_call = mutated_mod.get_global_var('func_22753')
call_25916 = relay.TupleGetItem(func_22751_call(), 0)
call_25917 = relay.TupleGetItem(func_22753_call(), 0)
output = call_25916
output2 = call_25917
func_25929 = relay.Function([], output)
mod['func_25929'] = func_25929
mod = relay.transform.InferType()(mod)
output = func_25929()
func_25930 = relay.Function([], output)
mutated_mod['func_25930'] = func_25930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16094_call = mod.get_global_var('func_16094')
func_16095_call = mutated_mod.get_global_var('func_16095')
call_25944 = relay.TupleGetItem(func_16094_call(), 0)
call_25945 = relay.TupleGetItem(func_16095_call(), 0)
output = relay.Tuple([call_25944,])
output2 = relay.Tuple([call_25945,])
func_25948 = relay.Function([], output)
mod['func_25948'] = func_25948
mod = relay.transform.InferType()(mod)
mutated_mod['func_25948'] = func_25948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_25948_call = mutated_mod.get_global_var('func_25948')
call_25949 = func_25948_call()
output = call_25949
func_25950 = relay.Function([], output)
mutated_mod['func_25950'] = func_25950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_23513_call = mod.get_global_var('func_23513')
func_23515_call = mutated_mod.get_global_var('func_23515')
call_25976 = relay.TupleGetItem(func_23513_call(), 0)
call_25977 = relay.TupleGetItem(func_23515_call(), 0)
func_25929_call = mod.get_global_var('func_25929')
func_25930_call = mutated_mod.get_global_var('func_25930')
call_25987 = func_25929_call()
call_25988 = func_25929_call()
func_24526_call = mod.get_global_var('func_24526')
func_24529_call = mutated_mod.get_global_var('func_24529')
const_25994 = relay.const([-9.065796,-0.845263,9.668667,-0.361602,2.076442,4.301450,8.650051,-4.948052,2.239907,1.198124,1.568020,-8.109905,9.510103,-1.167726,5.923533,4.040299,6.515628,2.385151,-4.151066,-0.560746,7.488980,1.099947,9.373750,7.510168,-5.584077,-7.970465,-1.151994,3.680713,0.762554,-3.869374,-6.135142,-8.127755,-3.024130,-4.617695,4.759846,-7.645175,-0.039838,4.252674,5.206108,4.602294,3.108835,-1.303790,-5.086274,2.929205,0.679967,-4.512832,6.110396,9.467289,-5.073371,-7.609826,-9.439382,-4.286015,-9.290104,9.041281,-9.232449,-6.205668,-8.443809,9.759715,-3.190839,-4.213668,4.480197,-2.879002,0.092539,-6.846909,9.611745,8.766314,6.963114,9.409725,5.441458,5.559376,5.460613,-5.548786,-3.716510,-9.760939,-2.131228,-6.300759,0.971965,2.086308,1.044567,-5.924653,-1.066520,-1.590348,3.565293,-9.693162,-0.788851,-1.292796,1.528246,0.805711,4.304074,-0.193979,-3.814345,4.145944,1.262213,-4.372384,-4.031009,-1.113851,-2.265871,-9.279086,-6.953599,9.973205,-2.907653,-1.862979,-6.363535,-3.814582,4.558220,2.621334,3.506503,4.338489,2.805452,4.127628,-3.723508,2.630963,5.023419,-4.333527,-0.824223,-1.616124,1.689646,-4.909498,9.233811,7.735562,4.853805,-4.551069,8.949043,-2.571561,-4.538769,-5.128470,6.591267,7.776471,2.908964,-8.118557,2.120427,6.867614,9.924051,-1.479647,-9.122299,0.433826,8.106828,-6.833495,0.155748,1.838638,1.247334,-0.361410,9.855632,0.029678,7.274600,-0.866313,-0.907600,7.645175,6.761366,-4.176507,-0.428651,-4.474913,-4.732842,-8.005071,0.188783,5.846518,-6.539604,6.177670,1.962285,-7.469122,-3.451900,-1.718268,-7.535574,-7.264024,9.953604,7.493280,-8.298937,8.664832,4.904730,-9.346978,-6.548076,0.209500,7.869885,-6.153388,5.988259,1.412355,-2.877647,-2.726707,3.892637,-0.627888,-9.110914,-7.593367,2.503806,0.582525,-4.837658,8.169071,3.676624,7.355232,0.722873,5.150025,-3.531368,-4.903951,-7.873979,-7.643363,8.582827,7.012046,-6.378781,-7.423925,9.894075,-7.384082,9.752273,-4.362440,-5.633198,3.592841,-8.672808,-6.102259,7.016437,6.818706,-3.189258,-9.504062,-8.337222,4.023535,1.186640,7.274721,4.916004,-9.218146,3.472710,0.559050,-3.111182,-6.966204,1.155197,-1.465813,6.747301,3.846273,5.636529,-7.976213,7.997569,-8.314525,9.124653,0.543193,-3.498033,-6.209743,4.704128,8.518648,-0.601272,-5.312869,2.299283,0.861244,-5.037317,-0.302968,-6.571110,9.417694,-6.785419,-4.991231,1.751969,-0.220269,-7.363080,-1.307547,-9.967222,7.477476,1.188155,-8.017011,-3.457490,1.454257,-5.225234,-5.253608,-1.557456,-0.436515,-7.518275,2.105939,6.388148,2.221169,-4.380729,9.447956,9.252342,2.165864,-3.882811,4.510739,3.342243,9.023279,-3.703414,-8.768828,5.004186,1.710132,-5.021855,-3.463265,-0.707237,4.486461,6.217095,4.687905,0.148399,3.887372,5.307794,7.892885,8.006213,-9.295718,-9.251642,9.407404,-3.473792,6.859065,1.726129,-0.842780,5.193763,-5.598816,-6.185111,-1.362720,-7.941102,9.702568,-7.287351,0.606191,8.558711,-8.117430,-3.631700,5.111349,-3.887453,7.645330,-2.887160,-6.543159,6.165637,-7.778961,-6.625362,-1.296362,-1.297145,-4.052680,-3.410425,1.300536,-0.568752,2.775897,2.146310,8.849850,-0.444766,3.065315,-1.065050,-5.884666,-6.565122,1.634302,7.231123,5.898939,9.243910,8.090842,1.690596,6.961352,-0.578237,7.708801,8.017722,7.449324,0.927829,4.064803,-2.816893,-1.544617,-7.299000,-5.726119,6.093965,-8.742986,8.011140,-2.694307,-1.581867,-2.465950,-3.299941,-9.409083,-1.265689,5.787981,-9.810195,1.607497,7.391689,0.196679,9.682171,3.836920,6.126716,9.758137,6.092348,-3.095790,3.870553,-2.805014,-5.320927,-0.513840,4.698517,-6.993471,-8.394041,-5.582765,4.842590,0.413005,3.770100,0.146482,-9.190418,-5.586075,-8.435927,9.777146,7.153114,-8.165710,-6.675382,2.424887,-1.851141,3.767586,3.101427,-9.142492,0.490976,-7.236930,1.017750,-4.782063,-9.089472,3.076875,9.732182,4.567320,3.971332,-6.642892,-1.095868,9.445288,7.391072,8.965737,-3.153540,-3.068260,6.440358,1.863039,-4.174714,1.036383,-3.409543,-1.173856,0.471077,-4.908156,1.915983,8.655069,-9.882121,-1.927018,1.207075,3.831947,-7.844993,-0.600586,-3.443454,-9.227604,8.357073,9.945187,-1.733260,2.599219,4.792229,-3.583004,-9.935421,-5.912433,-3.351520,-7.896628,-8.646123,-7.864593,8.257996,8.733656,-7.794123,4.073162,1.903594,7.738602,-6.283423,6.178959,-2.362446,-7.449694,0.062001,-9.686929,5.822131,-9.839044,-1.085181,-8.462921,8.514351,2.710295,5.639726,1.330147,6.232369,1.579083,7.924047,-8.656918,-8.380978,-5.925650,6.747053,-9.572167,3.438367,5.331991,4.810185,-4.921849,9.896812,-3.344888,-9.336148,2.740447,-5.140419,8.540607,7.287125,9.159021,-6.818342,-7.813160,-0.024220,-3.874718,3.229258,9.409770,-8.414387,1.543993,9.897312,-5.694799,2.125859,-6.627639,-1.299448,1.220341,7.901259,-7.345210,-6.411577,7.426806,4.009847,-1.017970,5.550253,3.910250,5.398656,9.836312,-4.000495,-2.434999,8.928107,0.762057,-3.898610,-7.896822,1.699593,9.154515,6.977416,3.372377,3.160724,2.996327,4.892465,-9.677154,5.894791,-7.907710,2.746756,4.630465,2.307173,6.414078,1.785607,8.700160,-4.482448,-9.400331,2.597065,-7.661818,9.998333,-7.529252,-9.772039,-9.648888,-4.952372,2.973190,5.077637,7.358367,3.114821,7.931781,-5.173378,7.365248,1.292905,-4.415752,8.418572,5.775381,-3.899211,-4.867680,-3.083570,-4.000485,9.682749,4.616516,-1.214795,0.674214,4.774303,-5.424584,3.373106,-5.553552,9.280105,6.014118,6.242755,0.468047,-6.043504,-0.837666,-7.129270,-9.088390,-8.464185,9.386796,-7.918637,-9.340415,3.688805,2.260901,-0.802666,6.021918,-3.548477,3.639103,-3.205946,4.077251,-0.844000,6.192670,-4.991720,-4.311957,3.761044,3.275582,-6.074628,1.207268,-9.458069,-1.979105,-9.417795,-5.543603,-0.192082,-1.627672,-1.887856,-0.864330,4.242040,-3.801150,9.377166,-2.474054,-7.515543,-4.647601,6.432829,-0.636008,-9.793238,2.742746,-4.912735,7.104983,9.147736,8.275071,2.948520,-9.460238,-2.454875,-2.804322,8.614232,-3.023700,-2.546946,-8.676381,1.247924,7.752356,5.891994,-2.208340,-4.708403,-7.121956,-1.551340,3.242483,8.851973,-7.902744,-7.337498,8.959513,-2.342259,8.709961,-4.077853,-0.290550,-3.201378,5.637199,-4.267249,-8.266710,9.529242,-3.909385,-2.129323,2.829375,9.156158,7.668162,-5.427970,4.241497,6.575748,5.799065,-0.004162,7.066890,4.046572,-1.097177,-9.063235,-6.619408,-0.484380,2.117279,0.662954,-7.125876,2.484416,-5.004470,0.008967,-1.373511,1.503525,-5.942134,6.840177,-3.627386,6.411290,3.074699,1.079942,4.980069,-3.555755,1.065897,-3.213204,6.301638,1.661331,8.206576,8.163870,9.599615,-3.053032,3.292060,8.559808,-2.675712,-4.163046,1.818916,-0.212196,2.686011,5.031015,-8.203753,0.459360,2.717154,1.693740,7.264865,-2.176499,3.486386,-7.954738,1.104793,9.244073,-4.900939,8.082413,6.726870,9.920674,-1.630196,0.480869,-5.489435,-6.780173,-3.372578,-3.763833,3.942396,-2.239310,2.673014,6.385173,1.725050,0.334103,-0.279613,6.940915,-0.557272,9.804175,0.900615,2.977771,2.101597,-0.710882,5.618362,2.142662,0.780250,-1.413510,-8.569392,6.924665,-4.134979,-6.879447,4.658703,-5.730023,-6.137113,3.368072,2.602506,6.147778,-1.854496,-3.434113,-5.618618,-8.872391,1.407743,9.218155,-5.897910,2.600359,7.378158,-0.832003,4.524653,-3.667441,-8.976747,-6.217208,-7.683186,-4.252242,7.039923,-5.567998,-9.203833,3.474391,3.412278,7.440561,-8.923339,-8.225923,-8.421743,-5.103307,-7.328809,0.186150,-4.312441,-4.175091,9.972826,-0.515574,9.519406,2.898134,6.153665,6.319864,4.411649,6.091297,-3.888179,9.385123,-1.692410,-9.102465,-6.231095,3.455935,0.095300,8.709363,-0.935602,6.799666,-5.213207,0.422020,-8.318988,8.327526,5.115337,8.235378,-1.663510,8.135099,-7.592464,2.194444,8.969205,-1.164991,-3.524123,-5.433360,4.947812,-9.265855,-5.913840,5.856138,0.230344,-6.465090,7.058204,-7.282793,-4.139258,-6.652380,5.972675,7.682944,-2.818213,-1.357827,5.598359,5.891656,-3.631887,-7.083640,6.479378,5.897952,-5.247991,-6.392412,5.508931,-5.283386,-2.046114,9.856101,-1.890027,-6.441001,-1.421486,-8.420329,2.813143,-9.549585,2.914614,-5.296298,-7.633073,3.647583,1.853722,6.346882,-6.669603,-2.085406,-2.087067,8.453720,-1.063911,-1.379233,-4.077025], dtype = "float64")#candidate|25994|(832,)|const|float64
call_25993 = relay.TupleGetItem(func_24526_call(relay.reshape(const_25994.astype('float64'), [832,])), 1)
call_25995 = relay.TupleGetItem(func_24529_call(relay.reshape(const_25994.astype('float64'), [832,])), 1)
output = relay.Tuple([call_25976,call_25987,call_25993,const_25994,])
output2 = relay.Tuple([call_25977,call_25988,call_25995,const_25994,])
func_25998 = relay.Function([], output)
mod['func_25998'] = func_25998
mod = relay.transform.InferType()(mod)
output = func_25998()
func_25999 = relay.Function([], output)
mutated_mod['func_25999'] = func_25999
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14665_call = mod.get_global_var('func_14665')
func_14667_call = mutated_mod.get_global_var('func_14667')
call_26100 = func_14665_call()
call_26101 = func_14665_call()
output = relay.Tuple([call_26100,])
output2 = relay.Tuple([call_26101,])
func_26109 = relay.Function([], output)
mod['func_26109'] = func_26109
mod = relay.transform.InferType()(mod)
output = func_26109()
func_26110 = relay.Function([], output)
mutated_mod['func_26110'] = func_26110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20068_call = mod.get_global_var('func_20068')
func_20069_call = mutated_mod.get_global_var('func_20069')
call_26164 = func_20068_call()
call_26165 = func_20068_call()
const_26176 = relay.const([[[1.241243,-9.083683,5.930396,0.034970],[-4.178294,7.005493,-0.945741,4.613003],[6.014089,-6.092613,9.409982,-0.946010],[6.011505,-2.232562,1.294824,-1.324731],[3.783556,1.080103,-4.798035,-1.117767],[1.689011,-9.391738,6.924454,2.364570],[-2.180435,-0.026598,-5.202025,5.294876],[-8.979214,4.412837,8.772053,-7.757640],[-6.487008,2.734267,8.335053,7.506540],[5.806058,-0.603961,-4.651569,-5.211551],[8.012012,-6.147159,4.554765,7.871495]],[[0.449340,-4.707833,6.372774,0.972282],[-0.727542,-8.591655,-3.404953,-5.220288],[-5.675886,2.939065,-7.058849,2.725007],[-0.220793,-2.092484,9.004009,9.659604],[-2.850681,7.212203,-0.036506,-0.681869],[-4.825138,-0.157458,-7.955024,-8.793154],[-3.974496,2.913806,6.652802,-6.706012],[4.922457,-9.386644,8.712050,5.473109],[1.438427,9.843007,-4.523166,-8.489968],[-4.002057,6.654821,-5.558957,8.404787],[2.148683,7.860586,4.954611,-3.563912]],[[-7.537273,7.682043,-5.247971,-8.161099],[-6.494570,-7.184601,9.491843,0.333301],[1.292667,-8.558354,-8.279777,-9.112716],[4.688879,6.105785,-0.709443,7.344466],[-3.708029,-2.676983,0.257615,-0.663766],[-4.300776,-4.411152,3.984813,1.159526],[0.722632,-8.303144,-0.634041,9.677245],[1.532146,-6.513800,4.027698,-5.481223],[1.716274,-0.430289,7.584592,-7.287080],[4.486161,8.433099,-1.310288,-6.018280],[6.836657,7.919839,9.667446,8.525091]],[[1.062429,-7.620310,6.737571,-9.914129],[3.452256,8.235287,1.969426,-3.189506],[7.981304,-4.437936,2.145407,9.628011],[3.349016,-8.904526,7.150686,5.881287],[1.016393,4.136846,6.220676,3.752055],[9.062170,4.442649,-8.097066,6.465638],[-5.640374,1.673434,-9.887070,-7.200041],[-9.529928,9.526497,-1.788958,-7.710906],[-2.428268,-0.147014,-4.098250,6.727820],[-1.613846,-0.343310,-5.666311,-6.681720],[9.308781,-6.449021,-6.819806,-9.075581]],[[9.125849,8.926478,-6.463038,-4.952961],[7.750282,-7.340092,-5.478419,3.037984],[3.696884,-4.679794,-2.266518,-3.237111],[-7.564288,6.178643,1.452177,1.150821],[8.158991,-1.349734,3.969181,9.294799],[3.196605,-0.680408,5.034005,-8.369045],[4.494616,-4.599109,-3.914103,-8.982935],[-9.925564,3.156757,6.318481,-5.873209],[7.318345,-6.029481,6.588930,-1.582146],[-2.839069,6.011846,-7.025413,-9.454262],[-2.815291,6.633900,9.131208,2.765804]],[[-5.229807,4.986435,-7.561652,-9.372211],[-6.708201,-6.072768,-6.762762,-9.617869],[2.016865,-8.415566,2.675272,7.007925],[-3.862949,-0.944762,-0.310534,6.101676],[8.861089,-6.351543,-5.398478,7.677751],[-2.179454,8.798437,-4.778026,4.646901],[2.800306,-4.473932,-0.281605,-1.078427],[-4.300537,-3.771450,-1.041220,1.225433],[-6.400228,2.570483,0.908674,0.202350],[-1.534596,-3.909164,-4.367774,-4.535758],[-6.840858,-4.321920,3.363493,5.153259]],[[-2.266432,-5.292271,3.061253,-7.623785],[-8.892831,-1.680704,-2.964118,0.293522],[-9.693014,-3.183459,9.987772,-6.338965],[6.557009,-1.540732,5.381107,-4.591318],[9.776118,8.041166,5.516160,-2.553905],[3.455626,0.344730,-1.714608,2.625628],[-6.166379,4.269575,-0.685636,8.278376],[-2.056157,-1.505712,4.586110,1.609379],[-6.285310,8.672138,-7.509045,1.665373],[6.729500,-3.815453,5.615945,-2.999899],[0.294074,3.100493,-3.298130,0.903017]],[[-4.631393,-5.827279,-7.872245,-9.028722],[-9.585332,-7.595024,4.207109,5.959768],[-0.889664,-9.670897,8.151997,-6.430663],[-1.828681,-2.652803,-8.288173,3.938628],[-1.057623,8.355947,-8.020171,4.988965],[4.726502,1.426562,9.515349,1.063777],[-7.562624,1.441395,2.978865,-1.269208],[0.593116,-3.799060,-4.199835,-5.756893],[6.180875,-7.697587,7.171107,7.160019],[9.499658,7.230137,6.594408,1.363913],[-3.955812,7.298803,-6.144575,2.781760]],[[-7.964679,2.258905,1.633932,2.570818],[0.387724,-2.899588,4.125814,-6.519221],[9.119139,6.600710,-8.420366,-4.435521],[4.559687,-7.517959,-2.686987,2.673076],[9.409414,0.846584,-0.926842,-1.108844],[-3.101731,-1.226625,-8.300247,5.332998],[-0.930131,-9.287203,4.597227,0.031814],[-8.783918,-5.980152,1.187439,6.636806],[-1.312641,-3.760794,-4.653941,6.193615],[2.827776,-2.556980,-7.213405,4.259150],[7.340121,8.444945,9.553613,9.941125]]], dtype = "float32")#candidate|26176|(9, 11, 4)|const|float32
bop_26177 = relay.equal(call_26164.astype('bool'), relay.reshape(const_26176.astype('bool'), relay.shape_of(call_26164))) # shape=(9, 11, 4)
bop_26180 = relay.equal(call_26165.astype('bool'), relay.reshape(const_26176.astype('bool'), relay.shape_of(call_26165))) # shape=(9, 11, 4)
func_16094_call = mod.get_global_var('func_16094')
func_16095_call = mutated_mod.get_global_var('func_16095')
call_26185 = relay.TupleGetItem(func_16094_call(), 3)
call_26186 = relay.TupleGetItem(func_16095_call(), 3)
output = relay.Tuple([bop_26177,call_26185,])
output2 = relay.Tuple([bop_26180,call_26186,])
func_26193 = relay.Function([], output)
mod['func_26193'] = func_26193
mod = relay.transform.InferType()(mod)
mutated_mod['func_26193'] = func_26193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_26193_call = mutated_mod.get_global_var('func_26193')
call_26194 = func_26193_call()
output = call_26194
func_26195 = relay.Function([], output)
mutated_mod['func_26195'] = func_26195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18723_call = mod.get_global_var('func_18723')
func_18724_call = mutated_mod.get_global_var('func_18724')
call_26218 = func_18723_call()
call_26219 = func_18723_call()
func_23844_call = mod.get_global_var('func_23844')
func_23845_call = mutated_mod.get_global_var('func_23845')
call_26252 = func_23844_call()
call_26253 = func_23844_call()
output = relay.Tuple([call_26218,call_26252,])
output2 = relay.Tuple([call_26219,call_26253,])
func_26257 = relay.Function([], output)
mod['func_26257'] = func_26257
mod = relay.transform.InferType()(mod)
output = func_26257()
func_26258 = relay.Function([], output)
mutated_mod['func_26258'] = func_26258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_22725_call = mod.get_global_var('func_22725')
func_22726_call = mutated_mod.get_global_var('func_22726')
call_26271 = relay.TupleGetItem(func_22725_call(), 1)
call_26272 = relay.TupleGetItem(func_22726_call(), 1)
func_15647_call = mod.get_global_var('func_15647')
func_15649_call = mutated_mod.get_global_var('func_15649')
call_26274 = relay.TupleGetItem(func_15647_call(), 0)
call_26275 = relay.TupleGetItem(func_15649_call(), 0)
func_14426_call = mod.get_global_var('func_14426')
func_14427_call = mutated_mod.get_global_var('func_14427')
call_26280 = func_14426_call()
call_26281 = func_14426_call()
func_25707_call = mod.get_global_var('func_25707')
func_25712_call = mutated_mod.get_global_var('func_25712')
const_26286 = relay.const([-4.020319,-6.125670,0.844700,-6.416444,6.336485,1.750697,2.316216,-3.254441,-2.763642,-5.597322,-0.591917,3.328795,-8.190123,4.526699,6.289987,-4.685177,7.323790,-7.694763,9.038041,4.412756,-5.031235,2.179293,2.173905,3.035031,-6.848387,4.783756,-3.050054,-9.324336,5.554846,-0.301576,-8.279445,-6.468898,-2.355931,3.047071,8.367570,-0.349213,8.181302,5.145540,8.177171,-8.767324,-4.432965,-4.135757,9.659921,-0.951311,-7.221208,3.899071,8.273997,-4.774607,-5.729366,-5.583213,-6.332830,7.403619,-2.053717,6.320033,5.731563,9.923978,7.881038,-3.489510,-0.531319,2.183129,-2.204365,-4.650369,-1.527026,2.264646,-5.510316,-9.451745,-8.835874,-2.017193,-4.573978,-8.624701,-7.812981,2.616348,-5.931846,-9.893461,-8.241219,9.938677,-2.760427,7.801365,1.067132,-7.453341,-1.738071,-3.107769,-1.489575,1.922911,-5.956771,1.038977,8.043680,-7.084376,-4.968733,-1.896793,-9.586959,8.612753,0.192541,3.938337,7.904408,-4.330443,-1.745197,-1.539270,-4.685019,6.143698,-6.006272,7.710213,-1.818640,2.485681,-8.043752,6.307223,6.422335,0.869438,5.936484,6.358909,-4.815813,-0.557492,1.876225,-3.410985,-4.593331,-8.551686,-6.250051,-1.757218,-2.178837,7.329360,-8.422479,8.078977,-8.488579,-5.086803,-9.594985,-5.966199,-0.235172,1.673368,-2.582054,0.545009,-1.254841,0.463771,6.869883,7.250761,7.970425,-1.699737,6.713519,4.244653,-6.462352,-6.881954,-3.592447,-4.500603,2.867339,-7.084953,2.532032,7.790809,2.314546,-7.847922,-4.644726,-6.701778,-9.570858,9.218331,2.342091,1.076565,7.050402,-6.339535,5.662284,-7.714063,-4.602056,-8.935134], dtype = "float32")#candidate|26286|(160,)|const|float32
const_26287 = relay.const([-7.794046,4.125000,-6.685117,5.403115,-1.634158,-9.724926,-4.604184,2.354434,5.013600,4.180554,4.488522,-2.557633,5.244854,9.976881,8.268182,-2.533387,8.952394,-7.553970,-0.966654,0.120967,-1.130851,-9.791207,8.414014,7.136302,-1.866035,-3.323462,7.839386,7.547961,3.409732,9.492689,-1.673770,-2.186875,-3.475486,9.721897,-8.241661,5.703913,2.165941,-3.576640,4.270687,5.784441,-8.534238,7.082167,6.478152,5.498408,-0.473385,6.587790,-0.228419,-9.190642,-2.411903,9.194975,-1.970800,-2.366234,0.251198,6.832001,-0.199447,-4.073042,-2.741910,-2.314477,3.855071,9.771370,4.488702,-2.923537,-0.754675,-0.487337,9.134364,-1.601691,-9.431220,4.344971,0.660152,-0.126951,1.025761,-2.734522,-1.472279,5.061606,-6.315582,1.815378,2.541040,-6.024553,-0.153146,4.625688,-9.557317,-1.023761,-1.672864,-6.172001,-1.824959,5.415287,-1.183009,5.419610,5.205402,-4.645396,3.303632,5.455062,0.234355,2.408190,-8.592423,8.338865,-0.119726,4.429351,8.418853,-5.172120,-8.412826,-3.564796,1.042089,2.321344,-5.451455,2.801653,-1.090609,7.580658,-4.919660,1.756567,5.291310,3.244115,-2.839205,-9.053153,8.158820,1.167022,-0.001169,-8.878630,-3.524440,-3.863109,4.874117,-1.210172,-5.081723,8.285098,-9.057646,3.491848,-3.969595,0.500427,7.906762,-5.791399,-1.194790,-2.600557,4.544440,9.926656,3.805095,6.492669,6.483088,-1.543514,8.632823,-3.614456,-2.277954,5.779789,-7.608944,-2.566001,-5.442445,-2.127947,-5.606527,6.556497,3.939417,7.591490,6.078271,5.134988,4.927620,-4.804778,-3.800892,-3.221217,3.232413,9.023532,9.852010,0.736279,-4.218041,-1.715935,0.301818,8.895085,-5.028109,6.470897,1.640708,-9.412704,-2.043729,7.235245,4.371044,9.868442,5.480294,7.594801,-3.449857,-3.995515,-3.437858,-9.184821,-7.430258,8.061621,-6.651788,-3.502366,2.214126,-7.329645,-4.802846,-5.234218,-1.798805,-9.743959,-1.666522,-7.210219,-2.783611,-2.989633,6.644206,-0.832864,-9.079085,1.932121,-0.500494,-8.192174,-7.940797,9.098291,-4.407338,1.943376,-8.438249,-8.023265,3.216462,9.461890,7.272391,-5.179913,-7.843371,-8.429939,-7.483257,-0.879837,-5.095326,4.633437,8.429653,3.898362,-8.186090,-3.634927,-8.948193,-5.815145,9.111187,4.268092,4.391105,-3.787003,1.556796,-0.629015,-7.593118,-5.744095,8.432738,0.437861,7.740298,-2.622760,6.262270,-2.050557,4.695498,4.734545,-4.452345,4.343438,0.102730,-3.705058,-3.375096,-6.732013,0.587632,0.057782,-0.570927,0.684595,0.490828,-9.901417,1.135295,-1.698647,3.934965,5.005795,4.391170,0.036701,-3.176937,3.021573,-3.064951,4.777426,-0.942212,-7.049022,-8.558718,-6.333024,1.431908,-8.175649,9.218971,5.475778,2.024273,8.088510,7.858834,7.538811,-0.072687,-6.049660,-2.515533,-4.049101,9.595164,-0.566992,-2.491169,2.821033,6.152331,-3.944521,9.151128,1.445799,1.573355,6.029329,6.005561,-3.382857,4.396239,-1.713593,2.374277,-1.508634,6.312265,-0.280115,-0.168905,8.395768,6.180573,-3.883479,8.761103,1.856735,-7.062559,9.951432,4.482099,8.816083,-1.552960,9.824062,-8.156551,-1.576305,-5.908921,-4.118335,2.891354,-6.115063,1.137065,1.688174,-3.167592,1.471420,5.533723,-9.566695,1.206569,0.656775,2.721466,4.117219,-2.682539,4.135953,-6.353090,6.745178,9.653621,-0.262536,3.868739,1.029969,8.252685,-5.224874,2.402081,5.391110,7.162040,-7.443337,2.285691,-7.706185,-4.933716,-2.995088,5.801842,-3.559651,7.769629,-0.622191,-6.166084,-8.719676,-2.673997,-2.171177,5.043779,-2.282356,-2.666059,7.684994,-5.075881,8.219141,0.681801,0.288903,-7.992106,7.322829,4.376776,-5.110902,5.674152,0.669818,8.031093,3.682591,1.157251,4.103753,1.297698,-2.857062,8.183845,-8.998690,3.838615,0.902426,6.910086,-6.715277,-3.138477,-3.682164,1.745567], dtype = "float64")#candidate|26287|(375,)|const|float64
call_26285 = relay.TupleGetItem(func_25707_call(relay.reshape(const_26286.astype('float32'), [16, 5, 2]), relay.reshape(const_26286.astype('float32'), [16, 5, 2]), relay.reshape(const_26287.astype('float64'), [15, 5, 5]), ), 0)
call_26288 = relay.TupleGetItem(func_25712_call(relay.reshape(const_26286.astype('float32'), [16, 5, 2]), relay.reshape(const_26286.astype('float32'), [16, 5, 2]), relay.reshape(const_26287.astype('float64'), [15, 5, 5]), ), 0)
func_14665_call = mod.get_global_var('func_14665')
func_14667_call = mutated_mod.get_global_var('func_14667')
call_26304 = func_14665_call()
call_26305 = func_14665_call()
output = relay.Tuple([call_26271,call_26274,call_26280,call_26285,const_26286,const_26287,call_26304,])
output2 = relay.Tuple([call_26272,call_26275,call_26281,call_26288,const_26286,const_26287,call_26305,])
func_26310 = relay.Function([], output)
mod['func_26310'] = func_26310
mod = relay.transform.InferType()(mod)
output = func_26310()
func_26311 = relay.Function([], output)
mutated_mod['func_26311'] = func_26311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14750_call = mod.get_global_var('func_14750')
func_14752_call = mutated_mod.get_global_var('func_14752')
call_26444 = relay.TupleGetItem(func_14750_call(), 1)
call_26445 = relay.TupleGetItem(func_14752_call(), 1)
func_21747_call = mod.get_global_var('func_21747')
func_21751_call = mutated_mod.get_global_var('func_21751')
var_26461 = relay.var("var_26461", dtype = "float64", shape = (832,))#candidate|26461|(832,)|var|float64
const_26462 = relay.const([7,10,2,10,-7,-1,-9,-4,-3,7,4,5,-3,-4,4,-9,-9,-5,-5,4,-3,8,6,-5,6,-6,7,-10,2,-9,5,7,5,7,-8,-3,-8,3,10,-2,-9,1,-10,8,4,6,3,5,5,1,3,-4,-4,-4,2,-3,4,9,-4,6,2,9,-7,-7,-6,-6,2,-1,-7,-3,3,-2,-1,-1,-7,4,10,5,8,10,10,-5,7,1,3,7,-1,2,-1,8,1,5,7,-9,-4,9,6,-8,-1,9,4,-9,6,-10,6,4,2,-1,1,-4,-10,3,-10,-10,-2,5,6,5,-5,10,-3,-1,4,-3,-1,-4,-3,-8,7,-2,-1,-9,2,1,-6,-9,3,-3,-1,6,5,-6,4,-9,-3,4,-9,1,6,9,2,1,9,4,2,3,-9,-4,-4,-8,6,-3,4,6,-7,-1,2,-6,-8,2,-2,7,-5,-4,4,6,-3,-4,-4,-6,5,7,1,-10,-6,9,7,-7,5,-3,-5,-10,9,-7,8,1,-1,3,-4,1], dtype = "int16")#candidate|26462|(200,)|const|int16
call_26460 = relay.TupleGetItem(func_21747_call(relay.reshape(var_26461.astype('float64'), [832,]), relay.reshape(const_26462.astype('int16'), [200,]), ), 5)
call_26463 = relay.TupleGetItem(func_21751_call(relay.reshape(var_26461.astype('float64'), [832,]), relay.reshape(const_26462.astype('int16'), [200,]), ), 5)
output = relay.Tuple([call_26444,call_26460,var_26461,const_26462,])
output2 = relay.Tuple([call_26445,call_26463,var_26461,const_26462,])
func_26515 = relay.Function([var_26461,], output)
mod['func_26515'] = func_26515
mod = relay.transform.InferType()(mod)
var_26516 = relay.var("var_26516", dtype = "float64", shape = (832,))#candidate|26516|(832,)|var|float64
output = func_26515(var_26516)
func_26517 = relay.Function([var_26516], output)
mutated_mod['func_26517'] = func_26517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20303_call = mod.get_global_var('func_20303')
func_20305_call = mutated_mod.get_global_var('func_20305')
call_26553 = relay.TupleGetItem(func_20303_call(), 0)
call_26554 = relay.TupleGetItem(func_20305_call(), 0)
output = call_26553
output2 = call_26554
func_26576 = relay.Function([], output)
mod['func_26576'] = func_26576
mod = relay.transform.InferType()(mod)
output = func_26576()
func_26577 = relay.Function([], output)
mutated_mod['func_26577'] = func_26577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18723_call = mod.get_global_var('func_18723')
func_18724_call = mutated_mod.get_global_var('func_18724')
call_26604 = func_18723_call()
call_26605 = func_18723_call()
func_15046_call = mod.get_global_var('func_15046')
func_15047_call = mutated_mod.get_global_var('func_15047')
call_26612 = relay.TupleGetItem(func_15046_call(), 0)
call_26613 = relay.TupleGetItem(func_15047_call(), 0)
output = relay.Tuple([call_26604,call_26612,])
output2 = relay.Tuple([call_26605,call_26613,])
func_26615 = relay.Function([], output)
mod['func_26615'] = func_26615
mod = relay.transform.InferType()(mod)
output = func_26615()
func_26616 = relay.Function([], output)
mutated_mod['func_26616'] = func_26616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15578_call = mod.get_global_var('func_15578')
func_15580_call = mutated_mod.get_global_var('func_15580')
call_26780 = relay.TupleGetItem(func_15578_call(), 1)
call_26781 = relay.TupleGetItem(func_15580_call(), 1)
output = call_26780
output2 = call_26781
func_26809 = relay.Function([], output)
mod['func_26809'] = func_26809
mod = relay.transform.InferType()(mod)
mutated_mod['func_26809'] = func_26809
mutated_mod = relay.transform.InferType()(mutated_mod)
func_26809_call = mutated_mod.get_global_var('func_26809')
call_26810 = func_26809_call()
output = call_26810
func_26811 = relay.Function([], output)
mutated_mod['func_26811'] = func_26811
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14330_call = mod.get_global_var('func_14330')
func_14332_call = mutated_mod.get_global_var('func_14332')
call_26916 = func_14330_call()
call_26917 = func_14330_call()
output = relay.Tuple([call_26916,])
output2 = relay.Tuple([call_26917,])
func_26925 = relay.Function([], output)
mod['func_26925'] = func_26925
mod = relay.transform.InferType()(mod)
output = func_26925()
func_26926 = relay.Function([], output)
mutated_mod['func_26926'] = func_26926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_25907_call = mod.get_global_var('func_25907')
func_25909_call = mutated_mod.get_global_var('func_25909')
call_26968 = relay.TupleGetItem(func_25907_call(), 0)
call_26969 = relay.TupleGetItem(func_25909_call(), 0)
var_26978 = relay.var("var_26978", dtype = "float64", shape = (9, 11, 4))#candidate|26978|(9, 11, 4)|var|float64
bop_26979 = relay.subtract(call_26968.astype('uint16'), relay.reshape(var_26978.astype('uint16'), relay.shape_of(call_26968))) # shape=(9, 11, 4)
bop_26982 = relay.subtract(call_26969.astype('uint16'), relay.reshape(var_26978.astype('uint16'), relay.shape_of(call_26969))) # shape=(9, 11, 4)
output = bop_26979
output2 = bop_26982
func_26984 = relay.Function([var_26978,], output)
mod['func_26984'] = func_26984
mod = relay.transform.InferType()(mod)
var_26985 = relay.var("var_26985", dtype = "float64", shape = (9, 11, 4))#candidate|26985|(9, 11, 4)|var|float64
output = func_26984(var_26985)
func_26986 = relay.Function([var_26985], output)
mutated_mod['func_26986'] = func_26986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17630_call = mod.get_global_var('func_17630')
func_17632_call = mutated_mod.get_global_var('func_17632')
call_27038 = relay.TupleGetItem(func_17630_call(), 0)
call_27039 = relay.TupleGetItem(func_17632_call(), 0)
output = relay.Tuple([call_27038,])
output2 = relay.Tuple([call_27039,])
func_27040 = relay.Function([], output)
mod['func_27040'] = func_27040
mod = relay.transform.InferType()(mod)
output = func_27040()
func_27041 = relay.Function([], output)
mutated_mod['func_27041'] = func_27041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18541_call = mod.get_global_var('func_18541')
func_18543_call = mutated_mod.get_global_var('func_18543')
call_27223 = func_18541_call()
call_27224 = func_18541_call()
func_14127_call = mod.get_global_var('func_14127')
func_14129_call = mutated_mod.get_global_var('func_14129')
call_27234 = relay.TupleGetItem(func_14127_call(), 1)
call_27235 = relay.TupleGetItem(func_14129_call(), 1)
func_25059_call = mod.get_global_var('func_25059')
func_25066_call = mutated_mod.get_global_var('func_25066')
var_27237 = relay.var("var_27237", dtype = "uint32", shape = ())#candidate|27237|()|var|uint32
const_27238 = relay.const([-6,8,6,-3,3,-10,-9,-7,3,2,-3,-3,-7,-6,-3,-8,-1,9,4,-6,3,-1,8,-5], dtype = "uint32")#candidate|27238|(24,)|const|uint32
var_27239 = relay.var("var_27239", dtype = "uint64", shape = (130,))#candidate|27239|(130,)|var|uint64
var_27240 = relay.var("var_27240", dtype = "float64", shape = (6, 44))#candidate|27240|(6, 44)|var|float64
var_27241 = relay.var("var_27241", dtype = "float32", shape = (750,))#candidate|27241|(750,)|var|float32
call_27236 = relay.TupleGetItem(func_25059_call(relay.reshape(var_27237.astype('uint32'), []), relay.reshape(const_27238.astype('uint32'), [24,]), relay.reshape(var_27239.astype('uint64'), [26, 5]), relay.reshape(var_27240.astype('float64'), [264,]), relay.reshape(var_27241.astype('float32'), [1, 750]), ), 2)
call_27242 = relay.TupleGetItem(func_25066_call(relay.reshape(var_27237.astype('uint32'), []), relay.reshape(const_27238.astype('uint32'), [24,]), relay.reshape(var_27239.astype('uint64'), [26, 5]), relay.reshape(var_27240.astype('float64'), [264,]), relay.reshape(var_27241.astype('float32'), [1, 750]), ), 2)
func_19811_call = mod.get_global_var('func_19811')
func_19812_call = mutated_mod.get_global_var('func_19812')
call_27250 = relay.TupleGetItem(func_19811_call(), 0)
call_27251 = relay.TupleGetItem(func_19812_call(), 0)
output = relay.Tuple([call_27223,call_27234,call_27236,var_27237,const_27238,var_27239,var_27240,var_27241,call_27250,])
output2 = relay.Tuple([call_27224,call_27235,call_27242,var_27237,const_27238,var_27239,var_27240,var_27241,call_27251,])
func_27252 = relay.Function([var_27237,var_27239,var_27240,var_27241,], output)
mod['func_27252'] = func_27252
mod = relay.transform.InferType()(mod)
mutated_mod['func_27252'] = func_27252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_27252_call = mutated_mod.get_global_var('func_27252')
var_27254 = relay.var("var_27254", dtype = "uint32", shape = ())#candidate|27254|()|var|uint32
var_27255 = relay.var("var_27255", dtype = "uint64", shape = (130,))#candidate|27255|(130,)|var|uint64
var_27256 = relay.var("var_27256", dtype = "float64", shape = (6, 44))#candidate|27256|(6, 44)|var|float64
var_27257 = relay.var("var_27257", dtype = "float32", shape = (750,))#candidate|27257|(750,)|var|float32
call_27253 = func_27252_call(var_27254,var_27255,var_27256,var_27257,)
output = call_27253
func_27258 = relay.Function([var_27254,var_27255,var_27256,var_27257,], output)
mutated_mod['func_27258'] = func_27258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_24674_call = mod.get_global_var('func_24674')
func_24675_call = mutated_mod.get_global_var('func_24675')
call_27278 = relay.TupleGetItem(func_24674_call(), 0)
call_27279 = relay.TupleGetItem(func_24675_call(), 0)
output = call_27278
output2 = call_27279
func_27290 = relay.Function([], output)
mod['func_27290'] = func_27290
mod = relay.transform.InferType()(mod)
mutated_mod['func_27290'] = func_27290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_27290_call = mutated_mod.get_global_var('func_27290')
call_27291 = func_27290_call()
output = call_27291
func_27292 = relay.Function([], output)
mutated_mod['func_27292'] = func_27292
mutated_mod = relay.transform.InferType()(mutated_mod)
var_27385 = relay.var("var_27385", dtype = "float32", shape = (1, 2, 3))#candidate|27385|(1, 2, 3)|var|float32
uop_27386 = relay.acosh(var_27385.astype('float32')) # shape=(1, 2, 3)
output = uop_27386
output2 = uop_27386
F = relay.Function([var_27385,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_27385,], output2)
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
