import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_442 = relay.var("var_442", dtype = "uint8", shape = ())#candidate|442|()|var|uint8
var_443 = relay.var("var_443", dtype = "uint8", shape = (12, 9, 1))#candidate|443|(12, 9, 1)|var|uint8
bop_444 = relay.right_shift(var_442.astype('uint8'), var_443.astype('uint8')) # shape=(12, 9, 1)
output = relay.Tuple([bop_444,])
output2 = relay.Tuple([bop_444,])
func_455 = relay.Function([var_442,var_443,], output)
mod['func_455'] = func_455
mod = relay.transform.InferType()(mod)
mutated_mod['func_455'] = func_455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_455_call = mutated_mod.get_global_var('func_455')
var_457 = relay.var("var_457", dtype = "uint8", shape = ())#candidate|457|()|var|uint8
var_458 = relay.var("var_458", dtype = "uint8", shape = (12, 9, 1))#candidate|458|(12, 9, 1)|var|uint8
call_456 = func_455_call(var_457,var_458,)
output = call_456
func_459 = relay.Function([var_457,var_458,], output)
mutated_mod['func_459'] = func_459
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1125 = relay.var("var_1125", dtype = "uint64", shape = (9, 15))#candidate|1125|(9, 15)|var|uint64
var_1126 = relay.var("var_1126", dtype = "uint64", shape = (9, 15))#candidate|1126|(9, 15)|var|uint64
bop_1127 = relay.greater(var_1125.astype('bool'), relay.reshape(var_1126.astype('bool'), relay.shape_of(var_1125))) # shape=(9, 15)
func_455_call = mod.get_global_var('func_455')
func_459_call = mutated_mod.get_global_var('func_459')
var_1137 = relay.var("var_1137", dtype = "uint8", shape = ())#candidate|1137|()|var|uint8
const_1138 = relay.const([[-1,-2,-8,-4,-7,-10,-2,9,5,7,-6,-10,10,10,-8,-1,-3,-7,-3,3,5,2,-10,-1,4,4,-5,-4,-10,5,1,8,-10,-5,8,-2],[1,-2,-6,6,9,9,4,-10,-2,-4,-2,8,-9,-6,1,10,1,-5,-3,8,10,-7,-3,-1,-4,9,-9,-2,10,-5,-6,-6,-5,6,3,9],[1,10,-4,10,-5,-8,6,3,7,-8,1,10,5,3,9,-3,-9,-8,-3,-1,-9,-5,8,-10,7,8,4,-5,5,6,1,8,-2,3,5,6]], dtype = "uint8")#candidate|1138|(3, 36)|const|uint8
call_1136 = relay.TupleGetItem(func_455_call(relay.reshape(var_1137.astype('uint8'), []), relay.reshape(const_1138.astype('uint8'), [12, 9, 1]), ), 0)
call_1139 = relay.TupleGetItem(func_459_call(relay.reshape(var_1137.astype('uint8'), []), relay.reshape(const_1138.astype('uint8'), [12, 9, 1]), ), 0)
func_455_call = mod.get_global_var('func_455')
func_459_call = mutated_mod.get_global_var('func_459')
call_1149 = relay.TupleGetItem(func_455_call(relay.reshape(var_1137.astype('uint8'), []), relay.reshape(const_1138.astype('uint8'), [12, 9, 1]), ), 0)
call_1150 = relay.TupleGetItem(func_459_call(relay.reshape(var_1137.astype('uint8'), []), relay.reshape(const_1138.astype('uint8'), [12, 9, 1]), ), 0)
func_455_call = mod.get_global_var('func_455')
func_459_call = mutated_mod.get_global_var('func_459')
call_1155 = relay.TupleGetItem(func_455_call(relay.reshape(var_1137.astype('uint8'), []), relay.reshape(call_1149.astype('uint8'), [12, 9, 1]), ), 0)
call_1156 = relay.TupleGetItem(func_459_call(relay.reshape(var_1137.astype('uint8'), []), relay.reshape(call_1149.astype('uint8'), [12, 9, 1]), ), 0)
func_455_call = mod.get_global_var('func_455')
func_459_call = mutated_mod.get_global_var('func_459')
call_1159 = relay.TupleGetItem(func_455_call(relay.reshape(var_1137.astype('uint8'), []), relay.reshape(call_1136.astype('uint8'), [12, 9, 1]), ), 0)
call_1160 = relay.TupleGetItem(func_459_call(relay.reshape(var_1137.astype('uint8'), []), relay.reshape(call_1136.astype('uint8'), [12, 9, 1]), ), 0)
var_1165 = relay.var("var_1165", dtype = "uint8", shape = (3, 36))#candidate|1165|(3, 36)|var|uint8
bop_1166 = relay.subtract(const_1138.astype('int16'), relay.reshape(var_1165.astype('int16'), relay.shape_of(const_1138))) # shape=(3, 36)
uop_1173 = relay.cos(bop_1127.astype('float64')) # shape=(9, 15)
func_455_call = mod.get_global_var('func_455')
func_459_call = mutated_mod.get_global_var('func_459')
call_1177 = relay.TupleGetItem(func_455_call(relay.reshape(var_1137.astype('uint8'), []), relay.reshape(call_1136.astype('uint8'), [12, 9, 1]), ), 0)
call_1178 = relay.TupleGetItem(func_459_call(relay.reshape(var_1137.astype('uint8'), []), relay.reshape(call_1136.astype('uint8'), [12, 9, 1]), ), 0)
func_455_call = mod.get_global_var('func_455')
func_459_call = mutated_mod.get_global_var('func_459')
call_1180 = relay.TupleGetItem(func_455_call(relay.reshape(var_1137.astype('uint8'), []), relay.reshape(var_1165.astype('uint8'), [12, 9, 1]), ), 0)
call_1181 = relay.TupleGetItem(func_459_call(relay.reshape(var_1137.astype('uint8'), []), relay.reshape(var_1165.astype('uint8'), [12, 9, 1]), ), 0)
output = relay.Tuple([call_1136,var_1137,call_1149,call_1155,call_1159,bop_1166,uop_1173,call_1177,call_1180,])
output2 = relay.Tuple([call_1139,var_1137,call_1150,call_1156,call_1160,bop_1166,uop_1173,call_1178,call_1181,])
func_1192 = relay.Function([var_1125,var_1126,var_1137,var_1165,], output)
mod['func_1192'] = func_1192
mod = relay.transform.InferType()(mod)
var_1193 = relay.var("var_1193", dtype = "uint64", shape = (9, 15))#candidate|1193|(9, 15)|var|uint64
var_1194 = relay.var("var_1194", dtype = "uint64", shape = (9, 15))#candidate|1194|(9, 15)|var|uint64
var_1195 = relay.var("var_1195", dtype = "uint8", shape = ())#candidate|1195|()|var|uint8
var_1196 = relay.var("var_1196", dtype = "uint8", shape = (3, 36))#candidate|1196|(3, 36)|var|uint8
output = func_1192(var_1193,var_1194,var_1195,var_1196,)
func_1197 = relay.Function([var_1193,var_1194,var_1195,var_1196,], output)
mutated_mod['func_1197'] = func_1197
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1234 = relay.var("var_1234", dtype = "float64", shape = (6, 7, 13))#candidate|1234|(6, 7, 13)|var|float64
uop_1235 = relay.tan(var_1234.astype('float64')) # shape=(6, 7, 13)
func_455_call = mod.get_global_var('func_455')
func_459_call = mutated_mod.get_global_var('func_459')
const_1240 = relay.const(-10, dtype = "uint8")#candidate|1240|()|const|uint8
var_1241 = relay.var("var_1241", dtype = "uint8", shape = (3, 36))#candidate|1241|(3, 36)|var|uint8
call_1239 = relay.TupleGetItem(func_455_call(relay.reshape(const_1240.astype('uint8'), []), relay.reshape(var_1241.astype('uint8'), [12, 9, 1]), ), 0)
call_1242 = relay.TupleGetItem(func_459_call(relay.reshape(const_1240.astype('uint8'), []), relay.reshape(var_1241.astype('uint8'), [12, 9, 1]), ), 0)
output = relay.Tuple([uop_1235,call_1239,const_1240,var_1241,])
output2 = relay.Tuple([uop_1235,call_1242,const_1240,var_1241,])
func_1246 = relay.Function([var_1234,var_1241,], output)
mod['func_1246'] = func_1246
mod = relay.transform.InferType()(mod)
mutated_mod['func_1246'] = func_1246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1246_call = mutated_mod.get_global_var('func_1246')
var_1248 = relay.var("var_1248", dtype = "float64", shape = (6, 7, 13))#candidate|1248|(6, 7, 13)|var|float64
var_1249 = relay.var("var_1249", dtype = "uint8", shape = (3, 36))#candidate|1249|(3, 36)|var|uint8
call_1247 = func_1246_call(var_1248,var_1249,)
output = call_1247
func_1250 = relay.Function([var_1248,var_1249,], output)
mutated_mod['func_1250'] = func_1250
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1347 = relay.var("var_1347", dtype = "int64", shape = (10, 12, 4))#candidate|1347|(10, 12, 4)|var|int64
var_1348 = relay.var("var_1348", dtype = "int64", shape = (10, 12, 4))#candidate|1348|(10, 12, 4)|var|int64
bop_1349 = relay.left_shift(var_1347.astype('int64'), relay.reshape(var_1348.astype('int64'), relay.shape_of(var_1347))) # shape=(10, 12, 4)
var_1353 = relay.var("var_1353", dtype = "int64", shape = (10, 12, 4))#candidate|1353|(10, 12, 4)|var|int64
bop_1354 = relay.mod(var_1348.astype('float32'), relay.reshape(var_1353.astype('float32'), relay.shape_of(var_1348))) # shape=(10, 12, 4)
uop_1357 = relay.log2(var_1347.astype('float32')) # shape=(10, 12, 4)
bop_1368 = relay.equal(uop_1357.astype('bool'), relay.reshape(bop_1354.astype('bool'), relay.shape_of(uop_1357))) # shape=(10, 12, 4)
output = relay.Tuple([bop_1349,bop_1368,])
output2 = relay.Tuple([bop_1349,bop_1368,])
func_1388 = relay.Function([var_1347,var_1348,var_1353,], output)
mod['func_1388'] = func_1388
mod = relay.transform.InferType()(mod)
var_1389 = relay.var("var_1389", dtype = "int64", shape = (10, 12, 4))#candidate|1389|(10, 12, 4)|var|int64
var_1390 = relay.var("var_1390", dtype = "int64", shape = (10, 12, 4))#candidate|1390|(10, 12, 4)|var|int64
var_1391 = relay.var("var_1391", dtype = "int64", shape = (10, 12, 4))#candidate|1391|(10, 12, 4)|var|int64
output = func_1388(var_1389,var_1390,var_1391,)
func_1392 = relay.Function([var_1389,var_1390,var_1391,], output)
mutated_mod['func_1392'] = func_1392
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1660 = relay.var("var_1660", dtype = "int16", shape = (6, 4, 12))#candidate|1660|(6, 4, 12)|var|int16
var_1661 = relay.var("var_1661", dtype = "int16", shape = (6, 4, 12))#candidate|1661|(6, 4, 12)|var|int16
bop_1662 = relay.less_equal(var_1660.astype('bool'), relay.reshape(var_1661.astype('bool'), relay.shape_of(var_1660))) # shape=(6, 4, 12)
uop_1666 = relay.tan(var_1660.astype('float32')) # shape=(6, 4, 12)
func_455_call = mod.get_global_var('func_455')
func_459_call = mutated_mod.get_global_var('func_459')
var_1672 = relay.var("var_1672", dtype = "uint8", shape = ())#candidate|1672|()|var|uint8
var_1673 = relay.var("var_1673", dtype = "uint8", shape = (6, 18))#candidate|1673|(6, 18)|var|uint8
call_1671 = relay.TupleGetItem(func_455_call(relay.reshape(var_1672.astype('uint8'), []), relay.reshape(var_1673.astype('uint8'), [12, 9, 1]), ), 0)
call_1674 = relay.TupleGetItem(func_459_call(relay.reshape(var_1672.astype('uint8'), []), relay.reshape(var_1673.astype('uint8'), [12, 9, 1]), ), 0)
func_1246_call = mod.get_global_var('func_1246')
func_1250_call = mutated_mod.get_global_var('func_1250')
const_1677 = relay.const([[-5.498275,-2.541509,-1.992875,-0.284206,4.394462,0.799404,0.138016,6.896043,-2.301339,-7.375558,4.159051,-8.149619,2.137146,-1.787335,-1.773571,3.471450,6.683764,2.199379,-8.458325,7.185838,8.712674,9.188612,8.839935,-7.785442,-7.825561,6.106871,-1.807912,1.178199,2.448667,0.595957,1.114578,-2.116935,-1.520131,-2.997336,5.482936,7.323390,-0.583410,-2.817221,7.825080,6.808778,5.683757,1.537477,-8.599996,5.073706,-2.419210,9.542547,3.621305,4.373214,3.341148,-6.606948,4.615727,6.828452,7.734089,2.367975,-3.183452,-8.156864,-9.307528,-0.870860,-3.442386,-8.883782,-0.339591,-7.111685,-6.382608,-7.849366,4.224109,-1.675135,-6.984449,-6.576448,1.799032,-3.016552,-7.000954,-7.770727,-4.851881,0.366606,-6.893302,7.083667,4.124738,5.349783],[7.017511,0.863273,-2.432225,-2.350506,-4.973464,-0.121457,-3.116703,1.413286,6.065286,6.726012,-1.500423,3.255974,7.710349,-2.563478,-6.287889,-3.581009,6.430023,4.751472,7.485054,-3.243728,-2.223869,-1.212684,4.957087,-6.482762,7.317325,-8.312346,-2.663742,-3.380850,-2.886521,0.207322,-1.301812,6.036096,8.580478,-6.538007,-8.069103,-9.807945,5.765362,2.237226,9.145026,-4.352241,-0.002902,-1.295658,-4.678333,-6.753474,2.373267,8.188706,4.457822,9.108667,0.559279,1.565145,-0.489807,8.220522,-8.854698,-3.394892,-8.800039,-6.006805,0.390596,5.435041,-7.987499,3.042062,8.305819,8.142162,8.432203,-3.348202,-5.675007,-7.140316,6.828950,4.043869,-0.543339,4.586171,-0.610450,1.863403,7.371361,2.244845,-7.854268,4.144704,9.687854,-4.652986],[-4.325927,-2.978573,7.875112,6.909070,-2.956285,-8.312667,3.628134,0.168946,-1.274980,2.832470,7.948751,3.135534,6.861539,-2.861248,2.798386,5.304201,1.765846,8.820830,-7.689669,8.661860,3.551626,-5.242826,-9.536310,-8.263582,-3.722120,-3.265031,-7.039888,-6.755970,-5.663362,-4.741408,0.870887,1.299748,4.165218,8.003079,-9.383183,-9.618600,6.053546,-8.316209,-0.382070,-6.515282,-6.216977,1.703596,-9.905385,7.418804,-4.330173,-6.864518,6.732095,-2.948526,-8.377805,1.530317,-6.602268,-0.477070,-2.185740,6.384899,4.611534,4.221261,-5.854362,-2.658376,-0.266702,-5.931303,-0.755960,4.772926,-5.132344,-2.476865,5.773879,5.053926,-1.718301,1.376035,-9.808104,4.359497,-2.605149,-6.981697,1.207655,1.311801,-0.342709,-4.374974,7.017729,-1.457405],[7.590874,-1.671853,-7.213312,0.487535,-6.414642,4.750900,5.756858,-6.858073,-8.332816,0.968450,-7.225534,8.613299,-0.681909,7.845514,9.289130,6.856276,-1.284890,-0.354115,-2.459049,0.740544,-2.800631,3.706032,-7.393747,-6.585393,-2.653446,-0.658549,-7.093719,1.741712,-1.684799,-9.197764,1.510817,-2.455386,-4.456893,-0.152581,-3.971127,1.639497,4.626774,8.262609,-3.179775,-0.631000,0.309002,9.532387,-8.899994,-9.161148,2.713565,3.772217,-5.668281,2.132015,-1.438977,8.829041,0.076030,8.329509,-4.291987,-3.109471,-7.647508,5.118266,-7.143695,-0.033405,-5.633609,4.859930,9.651686,-4.282093,-8.413808,-8.172033,1.940068,-1.360952,-3.985464,5.631916,-4.751260,-3.796667,-1.050507,-9.463065,-8.673453,-8.194567,5.660630,0.396207,-1.370316,-8.226112],[8.225394,5.204399,2.949889,3.910718,7.144972,-5.551914,5.862275,9.769855,-5.274437,-0.164112,-1.200223,0.751778,-1.682596,-9.324441,-1.980195,6.567524,-3.482818,0.276306,-7.987435,1.342132,1.809513,9.219420,-3.085835,2.507209,-8.583438,-6.869862,-0.806091,-9.992272,-0.760184,1.759761,-5.385278,-6.619439,2.413530,-5.088411,-0.802481,1.322718,2.203181,-2.304225,1.804186,-2.323250,0.233546,-4.257914,6.647402,-4.131811,-4.300095,-6.265316,9.290242,2.360368,-3.816329,-6.846622,6.334734,0.655178,5.480799,8.019722,9.563439,-7.706112,-8.904408,-4.569928,-1.932855,8.269175,-1.956718,6.812058,-8.765273,-5.636855,-3.035575,9.284730,-2.961150,-5.416530,7.732627,9.654264,7.880709,0.475470,-7.319275,3.284440,9.152606,4.474231,3.671333,7.862714],[4.653939,-0.995770,-7.855004,-2.996112,-9.755704,-7.766129,-9.329058,-3.544533,-0.560277,5.743558,9.254528,6.463032,7.158837,-0.056645,1.816646,-1.050960,0.808272,-6.923148,-3.550013,4.448719,6.574421,-2.745307,5.505895,6.061851,2.116306,-9.348312,-1.754715,7.039931,0.333921,-5.018039,5.189491,7.655449,6.228770,-1.767108,-9.369015,3.657601,-1.640925,9.868832,-5.746400,4.156978,9.317090,7.170669,2.969666,1.648158,-6.139298,0.369868,-3.277821,5.181140,-7.791580,-7.751268,2.562846,-1.197214,7.998608,5.241574,-8.765093,9.542913,-1.355720,7.381579,1.783939,-3.190806,-0.782659,4.513869,5.896920,1.493082,2.084349,-1.157447,8.237151,-1.587774,2.013557,-3.352431,-5.852427,9.070061,-3.625553,-9.519946,-7.179183,-2.646404,-1.217020,9.528830],[-0.876103,2.186493,-6.784973,-5.891191,-9.479316,8.351328,-5.419748,7.094134,4.280162,6.141651,-2.136217,-1.156188,6.514984,6.646531,-5.829571,9.773256,4.331274,-1.564174,-6.842245,3.369771,3.374578,-6.619006,5.500186,-4.670905,7.519007,-5.161899,7.630619,-3.443123,4.460487,-5.581613,-8.050789,-9.175292,-4.467193,-9.981867,9.056187,1.045240,-2.556228,-8.574243,-5.272125,-8.970196,9.974797,3.242664,8.725291,1.052063,7.145086,7.274321,4.781504,-6.732039,-2.675076,-1.160678,-1.818614,9.862362,-1.095769,-7.712691,-7.316462,-2.676231,-7.405769,6.349407,1.085558,-0.873406,-5.085376,-2.229595,-9.178231,-5.443317,3.232496,-4.447581,-8.662410,-0.832841,-8.940775,9.148885,-9.070657,-8.822610,1.515935,-3.101184,-3.532136,-4.540048,-7.640163,-9.745137]], dtype = "float64")#candidate|1677|(7, 78)|const|float64
call_1676 = relay.TupleGetItem(func_1246_call(relay.reshape(const_1677.astype('float64'), [6, 7, 13]), relay.reshape(var_1673.astype('uint8'), [3, 36]), ), 3)
call_1678 = relay.TupleGetItem(func_1250_call(relay.reshape(const_1677.astype('float64'), [6, 7, 13]), relay.reshape(var_1673.astype('uint8'), [3, 36]), ), 3)
func_1192_call = mod.get_global_var('func_1192')
func_1197_call = mutated_mod.get_global_var('func_1197')
const_1683 = relay.const([-7,-4,-5,-1,1,3,6,9,-3,1,-4,4,-2,8,-4,-1,-5,9,-10,-4,-4,3,6,-9,6,1,-6,7,-7,-7,-7,2,-3,-3,-1,-4,-3,4,-2,10,-5,-7,3,9,1,1,-4,2,-3,-10,2,-9,2,6,-8,-1,7,-4,-4,-10,-8,-2,5,-10,9,-5,4,9,7,2,-2,-8,3,-9,2,-1,-2,3,-9,8,-2,10,-6,2,4,1,-8,-5,9,-7,3,1,3,5,-8,-9,-7,-4,7,6,-1,9,6,-10,8,-5,-5,6,-4,-9,5,1,-8,5,-3,9,10,5,10,10,-3,8,-5,8,-7,-10,-5,-6,-7,8,-6,6,-3,-3,-8], dtype = "uint64")#candidate|1683|(135,)|const|uint64
call_1682 = relay.TupleGetItem(func_1192_call(relay.reshape(const_1683.astype('uint64'), [9, 15]), relay.reshape(const_1683.astype('uint64'), [9, 15]), relay.reshape(var_1672.astype('uint8'), []), relay.reshape(call_1676.astype('uint8'), [3, 36]), ), 0)
call_1684 = relay.TupleGetItem(func_1197_call(relay.reshape(const_1683.astype('uint64'), [9, 15]), relay.reshape(const_1683.astype('uint64'), [9, 15]), relay.reshape(var_1672.astype('uint8'), []), relay.reshape(call_1676.astype('uint8'), [3, 36]), ), 0)
var_1687 = relay.var("var_1687", dtype = "uint8", shape = (3, 36))#candidate|1687|(3, 36)|var|uint8
bop_1688 = relay.add(call_1676.astype('uint64'), relay.reshape(var_1687.astype('uint64'), relay.shape_of(call_1676))) # shape=(3, 36)
bop_1691 = relay.add(call_1678.astype('uint64'), relay.reshape(var_1687.astype('uint64'), relay.shape_of(call_1678))) # shape=(3, 36)
bop_1704 = relay.bitwise_xor(uop_1666.astype('uint16'), relay.reshape(bop_1662.astype('uint16'), relay.shape_of(uop_1666))) # shape=(6, 4, 12)
output = relay.Tuple([call_1671,var_1672,var_1673,const_1677,call_1682,const_1683,bop_1688,bop_1704,])
output2 = relay.Tuple([call_1674,var_1672,var_1673,const_1677,call_1684,const_1683,bop_1691,bop_1704,])
func_1707 = relay.Function([var_1660,var_1661,var_1672,var_1673,var_1687,], output)
mod['func_1707'] = func_1707
mod = relay.transform.InferType()(mod)
mutated_mod['func_1707'] = func_1707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1707_call = mutated_mod.get_global_var('func_1707')
var_1709 = relay.var("var_1709", dtype = "int16", shape = (6, 4, 12))#candidate|1709|(6, 4, 12)|var|int16
var_1710 = relay.var("var_1710", dtype = "int16", shape = (6, 4, 12))#candidate|1710|(6, 4, 12)|var|int16
var_1711 = relay.var("var_1711", dtype = "uint8", shape = ())#candidate|1711|()|var|uint8
var_1712 = relay.var("var_1712", dtype = "uint8", shape = (6, 18))#candidate|1712|(6, 18)|var|uint8
var_1713 = relay.var("var_1713", dtype = "uint8", shape = (3, 36))#candidate|1713|(3, 36)|var|uint8
call_1708 = func_1707_call(var_1709,var_1710,var_1711,var_1712,var_1713,)
output = call_1708
func_1714 = relay.Function([var_1709,var_1710,var_1711,var_1712,var_1713,], output)
mutated_mod['func_1714'] = func_1714
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1968 = relay.var("var_1968", dtype = "float64", shape = (11, 9, 2))#candidate|1968|(11, 9, 2)|var|float64
uop_1969 = relay.erf(var_1968.astype('float64')) # shape=(11, 9, 2)
output = relay.Tuple([uop_1969,])
output2 = relay.Tuple([uop_1969,])
func_1975 = relay.Function([var_1968,], output)
mod['func_1975'] = func_1975
mod = relay.transform.InferType()(mod)
var_1976 = relay.var("var_1976", dtype = "float64", shape = (11, 9, 2))#candidate|1976|(11, 9, 2)|var|float64
output = func_1975(var_1976)
func_1977 = relay.Function([var_1976], output)
mutated_mod['func_1977'] = func_1977
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2011 = relay.var("var_2011", dtype = "int16", shape = (4, 12, 4))#candidate|2011|(4, 12, 4)|var|int16
var_2012 = relay.var("var_2012", dtype = "int16", shape = (4, 12, 4))#candidate|2012|(4, 12, 4)|var|int16
bop_2013 = relay.multiply(var_2011.astype('int16'), relay.reshape(var_2012.astype('int16'), relay.shape_of(var_2011))) # shape=(4, 12, 4)
output = bop_2013
output2 = bop_2013
func_2020 = relay.Function([var_2011,var_2012,], output)
mod['func_2020'] = func_2020
mod = relay.transform.InferType()(mod)
var_2021 = relay.var("var_2021", dtype = "int16", shape = (4, 12, 4))#candidate|2021|(4, 12, 4)|var|int16
var_2022 = relay.var("var_2022", dtype = "int16", shape = (4, 12, 4))#candidate|2022|(4, 12, 4)|var|int16
output = func_2020(var_2021,var_2022,)
func_2023 = relay.Function([var_2021,var_2022,], output)
mutated_mod['func_2023'] = func_2023
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2025 = relay.var("var_2025", dtype = "float64", shape = (3, 9, 8))#candidate|2025|(3, 9, 8)|var|float64
uop_2026 = relay.asinh(var_2025.astype('float64')) # shape=(3, 9, 8)
uop_2036 = relay.sqrt(var_2025.astype('float64')) # shape=(3, 9, 8)
output = relay.Tuple([uop_2026,uop_2036,])
output2 = relay.Tuple([uop_2026,uop_2036,])
func_2040 = relay.Function([var_2025,], output)
mod['func_2040'] = func_2040
mod = relay.transform.InferType()(mod)
var_2041 = relay.var("var_2041", dtype = "float64", shape = (3, 9, 8))#candidate|2041|(3, 9, 8)|var|float64
output = func_2040(var_2041)
func_2042 = relay.Function([var_2041], output)
mutated_mod['func_2042'] = func_2042
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2501 = relay.const([[[3.720024,1.106343,-8.404663,-5.955272,6.158328,-8.411190],[-0.865122,-5.084409,-1.045351,-0.637629,6.540957,4.861838]],[[-6.861860,4.930518,-4.407901,-9.358164,-8.918852,4.624848],[-3.367301,-3.327202,-5.480906,9.766804,-0.481688,-1.566048]],[[7.139544,-3.455132,-2.142901,3.203094,5.977536,9.580140],[0.886633,-2.445857,2.874593,8.801833,5.409425,1.571874]],[[-1.799622,3.812475,5.192013,1.199470,-5.179505,5.875164],[-7.077960,0.357191,-1.716002,5.593404,-9.400121,9.661328]],[[1.169095,5.114592,-6.277478,5.861767,1.006486,-7.609637],[-8.743846,0.479426,7.391846,9.010835,9.705784,1.885914]],[[-4.711857,9.795525,-6.917867,-6.289912,3.066042,5.155629],[4.693265,-6.157000,5.770556,4.883551,9.369938,-4.340982]],[[6.055285,-8.353701,-4.381240,-2.797385,-8.714007,1.639359],[-0.960824,6.089229,9.932442,-6.415304,8.355515,3.607266]],[[1.366888,-0.255531,9.536833,6.700054,5.409598,3.974344],[4.254438,-4.778960,2.751120,7.642100,2.076313,-0.767610]],[[6.454410,9.285535,4.397490,4.158150,6.967977,1.603850],[-0.089110,-3.672253,-5.490831,4.705388,6.470286,-9.328331]],[[0.972866,6.887649,-3.080124,2.116137,-7.077840,-6.714232],[2.706605,-3.276724,7.284762,4.616261,-7.035001,0.758304]],[[4.166840,-5.763334,-9.076228,3.682964,-5.414003,3.945077],[-7.556571,-3.686284,6.860614,7.460419,-1.197539,-7.737586]],[[7.979432,3.391670,3.283382,9.591707,0.667725,9.736380],[-5.001565,3.136829,2.411602,7.841229,6.366074,-6.506521]],[[-6.574839,8.222034,9.930290,-7.821232,6.715792,-2.309722],[9.103960,0.799829,-9.825092,-1.279798,-2.611787,2.689156]]], dtype = "float32")#candidate|2501|(13, 2, 6)|const|float32
uop_2502 = relay.log(const_2501.astype('float32')) # shape=(13, 2, 6)
output = relay.Tuple([uop_2502,])
output2 = relay.Tuple([uop_2502,])
func_2518 = relay.Function([], output)
mod['func_2518'] = func_2518
mod = relay.transform.InferType()(mod)
mutated_mod['func_2518'] = func_2518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2518_call = mutated_mod.get_global_var('func_2518')
call_2519 = func_2518_call()
output = call_2519
func_2520 = relay.Function([], output)
mutated_mod['func_2520'] = func_2520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2518_call = mod.get_global_var('func_2518')
func_2520_call = mutated_mod.get_global_var('func_2520')
call_2526 = relay.TupleGetItem(func_2518_call(), 0)
call_2527 = relay.TupleGetItem(func_2520_call(), 0)
output = relay.Tuple([call_2526,])
output2 = relay.Tuple([call_2527,])
func_2528 = relay.Function([], output)
mod['func_2528'] = func_2528
mod = relay.transform.InferType()(mod)
output = func_2528()
func_2529 = relay.Function([], output)
mutated_mod['func_2529'] = func_2529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2518_call = mod.get_global_var('func_2518')
func_2520_call = mutated_mod.get_global_var('func_2520')
call_2541 = relay.TupleGetItem(func_2518_call(), 0)
call_2542 = relay.TupleGetItem(func_2520_call(), 0)
var_2548 = relay.var("var_2548", dtype = "float32", shape = (13, 2, 6))#candidate|2548|(13, 2, 6)|var|float32
bop_2549 = relay.not_equal(call_2541.astype('bool'), relay.reshape(var_2548.astype('bool'), relay.shape_of(call_2541))) # shape=(13, 2, 6)
bop_2552 = relay.not_equal(call_2542.astype('bool'), relay.reshape(var_2548.astype('bool'), relay.shape_of(call_2542))) # shape=(13, 2, 6)
func_2518_call = mod.get_global_var('func_2518')
func_2520_call = mutated_mod.get_global_var('func_2520')
call_2553 = relay.TupleGetItem(func_2518_call(), 0)
call_2554 = relay.TupleGetItem(func_2520_call(), 0)
output = relay.Tuple([bop_2549,call_2553,])
output2 = relay.Tuple([bop_2552,call_2554,])
func_2556 = relay.Function([var_2548,], output)
mod['func_2556'] = func_2556
mod = relay.transform.InferType()(mod)
mutated_mod['func_2556'] = func_2556
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2557 = relay.var("var_2557", dtype = "float32", shape = (13, 2, 6))#candidate|2557|(13, 2, 6)|var|float32
func_2556_call = mutated_mod.get_global_var('func_2556')
call_2558 = func_2556_call(var_2557)
output = call_2558
func_2559 = relay.Function([var_2557], output)
mutated_mod['func_2559'] = func_2559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2518_call = mod.get_global_var('func_2518')
func_2520_call = mutated_mod.get_global_var('func_2520')
call_2561 = relay.TupleGetItem(func_2518_call(), 0)
call_2562 = relay.TupleGetItem(func_2520_call(), 0)
func_2518_call = mod.get_global_var('func_2518')
func_2520_call = mutated_mod.get_global_var('func_2520')
call_2568 = relay.TupleGetItem(func_2518_call(), 0)
call_2569 = relay.TupleGetItem(func_2520_call(), 0)
output = relay.Tuple([call_2561,call_2568,])
output2 = relay.Tuple([call_2562,call_2569,])
func_2570 = relay.Function([], output)
mod['func_2570'] = func_2570
mod = relay.transform.InferType()(mod)
output = func_2570()
func_2571 = relay.Function([], output)
mutated_mod['func_2571'] = func_2571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2528_call = mod.get_global_var('func_2528')
func_2529_call = mutated_mod.get_global_var('func_2529')
call_2597 = relay.TupleGetItem(func_2528_call(), 0)
call_2598 = relay.TupleGetItem(func_2529_call(), 0)
uop_2615 = relay.tan(call_2597.astype('float32')) # shape=(13, 2, 6)
uop_2617 = relay.tan(call_2598.astype('float32')) # shape=(13, 2, 6)
func_1975_call = mod.get_global_var('func_1975')
func_1977_call = mutated_mod.get_global_var('func_1977')
var_2621 = relay.var("var_2621", dtype = "float64", shape = (198,))#candidate|2621|(198,)|var|float64
call_2620 = relay.TupleGetItem(func_1975_call(relay.reshape(var_2621.astype('float64'), [11, 9, 2])), 0)
call_2622 = relay.TupleGetItem(func_1977_call(relay.reshape(var_2621.astype('float64'), [11, 9, 2])), 0)
uop_2626 = relay.log10(uop_2615.astype('float32')) # shape=(13, 2, 6)
uop_2628 = relay.log10(uop_2617.astype('float32')) # shape=(13, 2, 6)
func_2040_call = mod.get_global_var('func_2040')
func_2042_call = mutated_mod.get_global_var('func_2042')
var_2634 = relay.var("var_2634", dtype = "float64", shape = (216,))#candidate|2634|(216,)|var|float64
call_2633 = relay.TupleGetItem(func_2040_call(relay.reshape(var_2634.astype('float64'), [3, 9, 8])), 0)
call_2635 = relay.TupleGetItem(func_2042_call(relay.reshape(var_2634.astype('float64'), [3, 9, 8])), 0)
output = relay.Tuple([call_2620,var_2621,uop_2626,call_2633,var_2634,])
output2 = relay.Tuple([call_2622,var_2621,uop_2628,call_2635,var_2634,])
func_2638 = relay.Function([var_2621,var_2634,], output)
mod['func_2638'] = func_2638
mod = relay.transform.InferType()(mod)
mutated_mod['func_2638'] = func_2638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2638_call = mutated_mod.get_global_var('func_2638')
var_2640 = relay.var("var_2640", dtype = "float64", shape = (198,))#candidate|2640|(198,)|var|float64
var_2641 = relay.var("var_2641", dtype = "float64", shape = (216,))#candidate|2641|(216,)|var|float64
call_2639 = func_2638_call(var_2640,var_2641,)
output = call_2639
func_2642 = relay.Function([var_2640,var_2641,], output)
mutated_mod['func_2642'] = func_2642
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2646 = relay.var("var_2646", dtype = "float64", shape = (14, 2, 16))#candidate|2646|(14, 2, 16)|var|float64
uop_2647 = relay.cos(var_2646.astype('float64')) # shape=(14, 2, 16)
output = relay.Tuple([uop_2647,])
output2 = relay.Tuple([uop_2647,])
func_2654 = relay.Function([var_2646,], output)
mod['func_2654'] = func_2654
mod = relay.transform.InferType()(mod)
mutated_mod['func_2654'] = func_2654
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2655 = relay.var("var_2655", dtype = "float64", shape = (14, 2, 16))#candidate|2655|(14, 2, 16)|var|float64
func_2654_call = mutated_mod.get_global_var('func_2654')
call_2656 = func_2654_call(var_2655)
output = call_2656
func_2657 = relay.Function([var_2655], output)
mutated_mod['func_2657'] = func_2657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2528_call = mod.get_global_var('func_2528')
func_2529_call = mutated_mod.get_global_var('func_2529')
call_2675 = relay.TupleGetItem(func_2528_call(), 0)
call_2676 = relay.TupleGetItem(func_2529_call(), 0)
var_2701 = relay.var("var_2701", dtype = "float32", shape = (13, 2, 6))#candidate|2701|(13, 2, 6)|var|float32
bop_2702 = relay.bitwise_xor(call_2675.astype('int32'), relay.reshape(var_2701.astype('int32'), relay.shape_of(call_2675))) # shape=(13, 2, 6)
bop_2705 = relay.bitwise_xor(call_2676.astype('int32'), relay.reshape(var_2701.astype('int32'), relay.shape_of(call_2676))) # shape=(13, 2, 6)
func_2040_call = mod.get_global_var('func_2040')
func_2042_call = mutated_mod.get_global_var('func_2042')
var_2708 = relay.var("var_2708", dtype = "float64", shape = (216,))#candidate|2708|(216,)|var|float64
call_2707 = relay.TupleGetItem(func_2040_call(relay.reshape(var_2708.astype('float64'), [3, 9, 8])), 1)
call_2709 = relay.TupleGetItem(func_2042_call(relay.reshape(var_2708.astype('float64'), [3, 9, 8])), 1)
output = relay.Tuple([bop_2702,call_2707,var_2708,])
output2 = relay.Tuple([bop_2705,call_2709,var_2708,])
func_2713 = relay.Function([var_2701,var_2708,], output)
mod['func_2713'] = func_2713
mod = relay.transform.InferType()(mod)
mutated_mod['func_2713'] = func_2713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2713_call = mutated_mod.get_global_var('func_2713')
var_2715 = relay.var("var_2715", dtype = "float32", shape = (13, 2, 6))#candidate|2715|(13, 2, 6)|var|float32
var_2716 = relay.var("var_2716", dtype = "float64", shape = (216,))#candidate|2716|(216,)|var|float64
call_2714 = func_2713_call(var_2715,var_2716,)
output = call_2714
func_2717 = relay.Function([var_2715,var_2716,], output)
mutated_mod['func_2717'] = func_2717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2570_call = mod.get_global_var('func_2570')
func_2571_call = mutated_mod.get_global_var('func_2571')
call_2738 = relay.TupleGetItem(func_2570_call(), 0)
call_2739 = relay.TupleGetItem(func_2571_call(), 0)
const_2740 = relay.const([[[-9.222983,8.111748,7.695326,-1.346335,4.103967,4.991564],[-2.321627,-7.008984,-9.756891,-5.562547,-2.794022,-3.406258]],[[5.661369,-1.404049,4.670839,-9.807758,2.937502,9.450320],[-7.999347,4.381351,2.615271,3.200927,9.798181,-6.308162]],[[-7.337472,-1.709097,1.556038,7.156941,-5.262388,-1.719953],[7.756922,7.719307,-5.129631,8.181445,-4.916220,0.323486]],[[6.354793,-8.911084,-8.088972,8.480488,2.782674,-3.629455],[-1.168970,8.786090,8.445309,3.757166,8.738616,-4.889756]],[[5.582692,-0.630024,-4.663661,8.095411,-3.372571,-2.394902],[5.178459,4.133634,-1.401602,9.635619,7.923683,3.663748]],[[-0.966878,1.953764,6.143867,1.922792,8.410787,-5.962289],[2.407203,-8.509653,5.283124,5.925033,-2.824041,-3.079277]],[[-6.170011,8.185065,-5.576077,-1.076495,1.971639,-5.700159],[6.371797,-0.378850,1.660637,3.336549,-3.820275,1.418517]],[[-2.328116,-6.136635,1.052793,4.275124,-1.917109,-3.080070],[8.992306,3.065048,-6.467061,9.204091,-3.478463,4.452726]],[[2.451535,-1.507071,-7.862164,3.037280,-9.224242,1.436370],[-7.487249,8.625529,3.680327,-2.131435,7.213263,-1.234111]],[[8.298020,1.793733,4.318215,-9.069725,6.450596,-2.410401],[-0.410599,7.904432,-6.869733,-6.443829,5.916316,8.228143]],[[3.783338,-7.086909,-3.766049,9.412838,-4.016668,3.159161],[0.138235,-5.794779,-0.570264,-0.595664,2.232391,-5.485399]],[[-2.760976,-5.584575,-1.493595,-3.899119,8.117020,-6.210169],[3.085201,-4.669050,2.673867,5.401255,0.027860,9.795097]],[[4.886187,-5.910659,5.379752,-1.118558,9.843986,-0.931882],[-4.274255,-7.865476,8.828146,0.794249,-8.504869,-6.979399]]], dtype = "float32")#candidate|2740|(13, 2, 6)|const|float32
bop_2741 = relay.less(call_2738.astype('bool'), relay.reshape(const_2740.astype('bool'), relay.shape_of(call_2738))) # shape=(13, 2, 6)
bop_2744 = relay.less(call_2739.astype('bool'), relay.reshape(const_2740.astype('bool'), relay.shape_of(call_2739))) # shape=(13, 2, 6)
func_2570_call = mod.get_global_var('func_2570')
func_2571_call = mutated_mod.get_global_var('func_2571')
call_2745 = relay.TupleGetItem(func_2570_call(), 0)
call_2746 = relay.TupleGetItem(func_2571_call(), 0)
output = relay.Tuple([bop_2741,call_2745,])
output2 = relay.Tuple([bop_2744,call_2746,])
func_2751 = relay.Function([], output)
mod['func_2751'] = func_2751
mod = relay.transform.InferType()(mod)
mutated_mod['func_2751'] = func_2751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2751_call = mutated_mod.get_global_var('func_2751')
call_2752 = func_2751_call()
output = call_2752
func_2753 = relay.Function([], output)
mutated_mod['func_2753'] = func_2753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2518_call = mod.get_global_var('func_2518')
func_2520_call = mutated_mod.get_global_var('func_2520')
call_2763 = relay.TupleGetItem(func_2518_call(), 0)
call_2764 = relay.TupleGetItem(func_2520_call(), 0)
output = call_2763
output2 = call_2764
func_2765 = relay.Function([], output)
mod['func_2765'] = func_2765
mod = relay.transform.InferType()(mod)
mutated_mod['func_2765'] = func_2765
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2765_call = mutated_mod.get_global_var('func_2765')
call_2766 = func_2765_call()
output = call_2766
func_2767 = relay.Function([], output)
mutated_mod['func_2767'] = func_2767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2570_call = mod.get_global_var('func_2570')
func_2571_call = mutated_mod.get_global_var('func_2571')
call_2861 = relay.TupleGetItem(func_2570_call(), 0)
call_2862 = relay.TupleGetItem(func_2571_call(), 0)
output = relay.Tuple([call_2861,])
output2 = relay.Tuple([call_2862,])
func_2863 = relay.Function([], output)
mod['func_2863'] = func_2863
mod = relay.transform.InferType()(mod)
output = func_2863()
func_2864 = relay.Function([], output)
mutated_mod['func_2864'] = func_2864
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2882 = relay.const([[[-7,-3,-10,10,5,-6,1,10],[-6,1,-9,6,9,-8,7,10],[1,-5,-6,-8,-3,7,4,6]],[[-2,-5,-10,-7,-2,1,7,1],[7,-8,-3,6,-9,-9,-10,-6],[6,5,4,-4,-5,6,-6,-9]],[[-5,6,1,7,4,-6,-3,-9],[6,4,6,-8,2,-4,-1,1],[-9,-5,8,-2,-7,1,3,-10]],[[3,-8,-1,1,-8,-4,-5,-6],[-2,7,-2,4,-9,1,6,10],[-7,-10,7,-4,4,6,2,6]],[[-3,-8,1,-4,9,-4,-9,4],[-5,6,4,6,9,9,-2,-9],[-5,-9,9,9,-1,2,-7,9]],[[1,-3,7,-2,1,-2,-6,9],[-8,-10,-2,-6,3,-6,-4,-2],[2,9,5,8,3,-9,2,10]],[[6,6,10,4,10,4,7,-9],[1,8,9,10,-7,1,-6,-9],[3,-10,-9,-4,4,-5,4,-10]],[[3,-3,-6,-6,-3,-4,10,-1],[1,3,8,1,7,-5,-1,10],[-2,8,-5,3,-1,-6,10,-1]],[[-3,-1,4,-4,-7,4,3,3],[6,-7,6,-8,9,-8,-5,2],[-5,-8,-4,-2,3,-2,-1,-4]],[[-8,7,-1,1,-10,10,7,-3],[4,3,-8,-2,2,-7,-9,-7],[2,-1,8,-2,10,-6,-4,1]],[[-4,6,1,1,4,-6,9,-1],[9,3,-3,-8,6,2,-4,-8],[9,-8,-3,-4,7,9,-5,-8]],[[-2,4,5,-8,5,-3,-5,7],[6,-4,4,-8,-8,-10,7,9],[-8,-5,-2,-6,-5,8,-3,-1]],[[10,-9,-3,-9,4,-8,-7,10],[-8,8,8,-9,-6,-2,-1,7],[-8,8,-1,-6,6,6,9,-7]],[[-1,-8,-1,-3,-3,-4,-7,10],[7,-1,-4,-5,-1,6,-9,8],[9,10,-3,7,-7,2,3,-1]]], dtype = "int32")#candidate|2882|(14, 3, 8)|const|int32
const_2883 = relay.const([[[3,5,-7,3,3,-7,2,-4],[6,2,3,-5,2,8,10,-5],[9,-4,-6,-6,-10,5,8,3]],[[-5,1,2,-2,3,-10,-10,-8],[5,-5,-9,-10,-3,-3,4,-4],[-10,-8,2,7,-2,10,1,10]],[[10,-7,-10,9,1,4,-7,8],[-7,10,-8,5,-5,3,3,-2],[-3,-3,7,6,-6,-7,1,2]],[[4,7,10,-4,-7,3,-2,-2],[-7,8,10,1,-4,-9,-6,5],[5,-1,-4,-2,-4,8,3,3]],[[-8,1,4,-4,-2,5,3,7],[-2,3,-5,-6,1,5,7,-1],[8,2,7,2,6,7,-7,-9]],[[3,8,8,-7,7,10,-1,-8],[-4,10,-4,-1,10,-4,-4,-10],[7,-7,2,-4,7,3,-7,-4]],[[3,4,-10,10,7,-9,-8,-2],[-8,10,4,-1,9,6,6,1],[-7,7,-4,-7,2,5,-6,-7]],[[-5,-6,-2,-7,-10,-1,4,6],[-8,9,9,-4,2,2,-4,4],[-5,-10,5,10,-2,-2,2,8]],[[-10,-2,2,1,-5,4,2,-1],[-8,6,8,-1,-6,7,-2,9],[-1,-2,-9,9,-7,-3,8,-6]],[[3,-2,-9,-1,5,-4,-2,-10],[4,-10,-6,-4,9,-2,1,3],[-1,5,5,6,6,8,2,3]],[[-1,-8,-1,8,2,-6,9,7],[4,1,-9,-1,4,3,1,-2],[10,-7,-2,10,6,-7,5,6]],[[-7,9,1,-1,1,-1,-3,-5],[2,-5,-9,-10,-10,2,10,-3],[3,3,3,-1,9,7,6,8]],[[-3,6,-9,-9,-3,4,-8,-8],[-10,7,6,-8,-1,-8,8,-6],[-8,-3,7,6,2,3,9,-1]],[[2,-4,7,3,8,4,9,7],[10,-6,3,-9,4,-4,-3,3],[6,-4,-9,10,10,1,2,7]]], dtype = "int32")#candidate|2883|(14, 3, 8)|const|int32
bop_2884 = relay.less(const_2882.astype('bool'), relay.reshape(const_2883.astype('bool'), relay.shape_of(const_2882))) # shape=(14, 3, 8)
uop_2897 = relay.sinh(bop_2884.astype('float32')) # shape=(14, 3, 8)
output = uop_2897
output2 = uop_2897
func_2899 = relay.Function([], output)
mod['func_2899'] = func_2899
mod = relay.transform.InferType()(mod)
mutated_mod['func_2899'] = func_2899
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2899_call = mutated_mod.get_global_var('func_2899')
call_2900 = func_2899_call()
output = call_2900
func_2901 = relay.Function([], output)
mutated_mod['func_2901'] = func_2901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2528_call = mod.get_global_var('func_2528')
func_2529_call = mutated_mod.get_global_var('func_2529')
call_2944 = relay.TupleGetItem(func_2528_call(), 0)
call_2945 = relay.TupleGetItem(func_2529_call(), 0)
const_2955 = relay.const([[[3.752690,2.103530,-9.846602,-9.840021,7.749148,-0.589858],[-4.853142,0.129031,-0.110089,5.424010,-9.247314,-3.674814]],[[-3.976911,3.015782,1.442009,-6.269619,-5.356452,-9.207644],[-3.560405,-5.670984,-8.999725,4.549232,3.156621,-1.795920]],[[9.794544,7.930437,7.032933,-8.714328,1.040866,7.974611],[-4.442857,2.571796,0.043105,1.682478,-9.789965,2.333334]],[[3.701305,6.757117,-0.135563,-6.000567,2.542224,6.218146],[0.085453,-9.088267,2.293019,0.199900,7.729821,-7.974782]],[[7.352877,-6.813415,2.425204,-6.397677,1.041450,-8.302976],[-3.992104,7.252554,-2.450057,-2.782485,-4.931978,-4.184286]],[[-2.285609,0.001643,-1.272661,-3.292244,7.389350,-8.528637],[8.246861,0.213821,-7.182023,-5.648839,-1.519639,0.743198]],[[-0.462600,-6.392254,-6.192781,6.886317,2.652649,1.049417],[-9.963094,0.280930,-6.232060,1.084022,-5.362668,-8.970674]],[[-2.767530,8.356824,-1.023803,5.729086,-9.938437,3.475607],[-5.424286,9.224889,4.373706,6.390379,2.728436,-2.666497]],[[-1.873846,9.480379,-7.083459,-6.258629,-3.963759,-9.858742],[-1.010445,7.466632,3.739006,7.320117,4.720911,2.420587]],[[3.254384,0.371997,4.444001,8.094741,2.458727,3.755983],[-2.227429,-1.335926,0.424670,-9.552959,-5.436135,7.187050]],[[-3.010600,2.699225,1.627959,0.134418,9.830270,2.993066],[-2.537120,1.388271,7.351027,2.720886,-7.817628,-0.268409]],[[-2.190997,7.818231,7.389445,9.958322,4.771061,3.112284],[4.125705,-2.180848,5.710401,-0.239643,-8.935071,8.993202]],[[-6.543375,4.500329,-6.945180,-6.139440,-8.081548,3.362735],[-0.202512,-5.597175,1.715595,3.138843,-0.911284,-1.929639]]], dtype = "float32")#candidate|2955|(13, 2, 6)|const|float32
bop_2956 = relay.minimum(call_2944.astype('uint32'), relay.reshape(const_2955.astype('uint32'), relay.shape_of(call_2944))) # shape=(13, 2, 6)
bop_2959 = relay.minimum(call_2945.astype('uint32'), relay.reshape(const_2955.astype('uint32'), relay.shape_of(call_2945))) # shape=(13, 2, 6)
output = bop_2956
output2 = bop_2959
func_2969 = relay.Function([], output)
mod['func_2969'] = func_2969
mod = relay.transform.InferType()(mod)
output = func_2969()
func_2970 = relay.Function([], output)
mutated_mod['func_2970'] = func_2970
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2977 = relay.var("var_2977", dtype = "uint64", shape = ())#candidate|2977|()|var|uint64
var_2978 = relay.var("var_2978", dtype = "uint64", shape = (11, 11, 2))#candidate|2978|(11, 11, 2)|var|uint64
bop_2979 = relay.less(var_2977.astype('bool'), var_2978.astype('bool')) # shape=(11, 11, 2)
uop_2999 = relay.erf(bop_2979.astype('float64')) # shape=(11, 11, 2)
func_2899_call = mod.get_global_var('func_2899')
func_2901_call = mutated_mod.get_global_var('func_2901')
call_3001 = func_2899_call()
call_3002 = func_2899_call()
uop_3006 = relay.log(uop_2999.astype('float32')) # shape=(11, 11, 2)
func_2969_call = mod.get_global_var('func_2969')
func_2970_call = mutated_mod.get_global_var('func_2970')
call_3011 = func_2969_call()
call_3012 = func_2969_call()
output = relay.Tuple([call_3001,uop_3006,call_3011,])
output2 = relay.Tuple([call_3002,uop_3006,call_3012,])
func_3015 = relay.Function([var_2977,var_2978,], output)
mod['func_3015'] = func_3015
mod = relay.transform.InferType()(mod)
mutated_mod['func_3015'] = func_3015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3015_call = mutated_mod.get_global_var('func_3015')
var_3017 = relay.var("var_3017", dtype = "uint64", shape = ())#candidate|3017|()|var|uint64
var_3018 = relay.var("var_3018", dtype = "uint64", shape = (11, 11, 2))#candidate|3018|(11, 11, 2)|var|uint64
call_3016 = func_3015_call(var_3017,var_3018,)
output = call_3016
func_3019 = relay.Function([var_3017,var_3018,], output)
mutated_mod['func_3019'] = func_3019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2969_call = mod.get_global_var('func_2969')
func_2970_call = mutated_mod.get_global_var('func_2970')
call_3037 = func_2969_call()
call_3038 = func_2969_call()
const_3052 = relay.const([[[9,3,6,4,4,10],[1,8,-9,-5,-1,8]],[[8,2,-4,7,2,5],[-10,1,-6,10,10,3]],[[2,2,6,3,-9,-9],[1,-10,6,2,-4,-1]],[[-4,10,-3,-5,-2,-10],[8,-2,8,2,7,-4]],[[-7,10,9,-4,4,-7],[8,2,1,-8,-5,8]],[[2,-3,-3,-4,3,-4],[5,3,3,-4,4,-10]],[[-10,-3,-7,-10,-2,1],[-2,-6,9,7,-9,3]],[[2,2,7,-10,10,-4],[4,-7,-9,-2,5,5]],[[-7,10,-5,-7,-4,5],[-2,-8,8,-9,-8,-9]],[[-7,7,8,-8,8,-10],[-2,-2,-7,-10,9,1]],[[-2,2,-1,8,-1,-9],[-8,-1,-6,-9,-9,7]],[[-7,-6,4,6,10,-7],[-8,-8,-9,7,6,4]],[[-10,-2,-6,-4,5,3],[-9,-5,-8,9,-5,-4]]], dtype = "uint32")#candidate|3052|(13, 2, 6)|const|uint32
bop_3053 = relay.floor_mod(call_3037.astype('float64'), relay.reshape(const_3052.astype('float64'), relay.shape_of(call_3037))) # shape=(13, 2, 6)
bop_3056 = relay.floor_mod(call_3038.astype('float64'), relay.reshape(const_3052.astype('float64'), relay.shape_of(call_3038))) # shape=(13, 2, 6)
uop_3057 = relay.cos(call_3037.astype('float32')) # shape=(13, 2, 6)
uop_3059 = relay.cos(call_3038.astype('float32')) # shape=(13, 2, 6)
uop_3065 = relay.cosh(uop_3057.astype('float64')) # shape=(13, 2, 6)
uop_3067 = relay.cosh(uop_3059.astype('float64')) # shape=(13, 2, 6)
func_2969_call = mod.get_global_var('func_2969')
func_2970_call = mutated_mod.get_global_var('func_2970')
call_3072 = func_2969_call()
call_3073 = func_2969_call()
func_1975_call = mod.get_global_var('func_1975')
func_1977_call = mutated_mod.get_global_var('func_1977')
const_3078 = relay.const([4.598318,8.313368,-2.918183,8.935052,-3.314251,0.555122,-0.833920,-0.850525,-7.786747,-2.288915,0.969171,3.703104,-5.433929,-1.454527,6.891092,-0.690078,1.542313,1.845113,-6.481006,-3.820377,2.753068,-3.163307,9.229404,-7.307292,-4.388634,-9.331254,7.987845,-9.022425,-9.385675,9.824148,1.478836,-4.601340,-5.700073,1.836111,9.574274,3.577227,3.927948,-1.475501,-5.175860,-2.104069,4.031281,9.261168,-5.495538,-1.315414,-1.113476,-7.345224,-9.803052,-7.795975,3.844934,9.983931,3.848695,5.008073,-3.429777,-6.114822,-8.503459,-2.114620,0.614382,-7.119763,6.244357,-8.931321,2.913212,-9.472362,-5.918262,-0.284073,-1.831315,-2.149969,-9.908909,-2.735398,5.406445,4.581678,3.585245,7.994127,6.813329,-1.379580,-1.703565,-4.877406,-2.012596,6.395321,4.575642,-7.212194,9.292200,-8.235314,-3.875315,9.396921,9.218693,7.495604,-8.811732,5.715231,-4.307473,-0.708215,-3.297970,-4.545764,0.663746,7.412528,8.552011,-5.427641,-0.453532,-9.486028,8.454273,-0.356950,2.463652,8.078491,-3.511541,3.359672,4.136766,-9.755455,4.308923,-3.394616,-8.827425,0.331125,3.884111,5.288342,-9.913990,-6.661847,8.970120,-6.429551,-1.296334,-5.775856,-7.093076,1.095571,4.801697,-4.538798,1.324723,-7.579599,-8.459185,2.221150,0.269333,-6.666263,3.565280,-8.800963,0.292224,5.214441,-2.303068,4.369875,8.808217,-5.122186,-8.274587,7.974953,2.703209,6.438780,-5.422141,9.999089,4.299030,7.680094,-9.701263,1.416771,9.176944,4.744007,-4.876091,-1.601081,-6.929566,4.740494,9.963168,-8.124599,-4.833158,1.082281,-8.914404,-4.072136,-8.688416,-0.679440,7.496977,-9.561596,-7.434311,1.278371,-3.726904,8.961766,-2.565831,7.662258,2.753296,4.037791,-3.307049,-6.664880,3.547830,-7.262638,9.154491,5.318081,6.813130,4.757691,6.093831,-8.579379,-6.580853,-3.465440,-0.050963,0.802487,5.887841,3.037050,7.119215,2.372203,3.382398,-6.728081,-2.380428,0.475741,5.025399,-8.486133,4.211836,3.562554,-3.196690,3.742100], dtype = "float64")#candidate|3078|(198,)|const|float64
call_3077 = relay.TupleGetItem(func_1975_call(relay.reshape(const_3078.astype('float64'), [11, 9, 2])), 0)
call_3079 = relay.TupleGetItem(func_1977_call(relay.reshape(const_3078.astype('float64'), [11, 9, 2])), 0)
output = relay.Tuple([bop_3053,uop_3065,call_3072,call_3077,const_3078,])
output2 = relay.Tuple([bop_3056,uop_3067,call_3073,call_3079,const_3078,])
func_3082 = relay.Function([], output)
mod['func_3082'] = func_3082
mod = relay.transform.InferType()(mod)
mutated_mod['func_3082'] = func_3082
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3082_call = mutated_mod.get_global_var('func_3082')
call_3083 = func_3082_call()
output = call_3083
func_3084 = relay.Function([], output)
mutated_mod['func_3084'] = func_3084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3082_call = mod.get_global_var('func_3082')
func_3084_call = mutated_mod.get_global_var('func_3084')
call_3085 = relay.TupleGetItem(func_3082_call(), 2)
call_3086 = relay.TupleGetItem(func_3084_call(), 2)
uop_3099 = relay.rsqrt(call_3085.astype('float64')) # shape=(13, 2, 6)
uop_3101 = relay.rsqrt(call_3086.astype('float64')) # shape=(13, 2, 6)
output = uop_3099
output2 = uop_3101
func_3106 = relay.Function([], output)
mod['func_3106'] = func_3106
mod = relay.transform.InferType()(mod)
mutated_mod['func_3106'] = func_3106
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3106_call = mutated_mod.get_global_var('func_3106')
call_3107 = func_3106_call()
output = call_3107
func_3108 = relay.Function([], output)
mutated_mod['func_3108'] = func_3108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2528_call = mod.get_global_var('func_2528')
func_2529_call = mutated_mod.get_global_var('func_2529')
call_3166 = relay.TupleGetItem(func_2528_call(), 0)
call_3167 = relay.TupleGetItem(func_2529_call(), 0)
output = relay.Tuple([call_3166,])
output2 = relay.Tuple([call_3167,])
func_3178 = relay.Function([], output)
mod['func_3178'] = func_3178
mod = relay.transform.InferType()(mod)
output = func_3178()
func_3179 = relay.Function([], output)
mutated_mod['func_3179'] = func_3179
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3180 = relay.var("var_3180", dtype = "int8", shape = ())#candidate|3180|()|var|int8
var_3181 = relay.var("var_3181", dtype = "int8", shape = (1, 14, 13))#candidate|3181|(1, 14, 13)|var|int8
bop_3182 = relay.less(var_3180.astype('bool'), var_3181.astype('bool')) # shape=(1, 14, 13)
output = relay.Tuple([bop_3182,])
output2 = relay.Tuple([bop_3182,])
func_3196 = relay.Function([var_3180,var_3181,], output)
mod['func_3196'] = func_3196
mod = relay.transform.InferType()(mod)
mutated_mod['func_3196'] = func_3196
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3196_call = mutated_mod.get_global_var('func_3196')
var_3198 = relay.var("var_3198", dtype = "int8", shape = ())#candidate|3198|()|var|int8
var_3199 = relay.var("var_3199", dtype = "int8", shape = (1, 14, 13))#candidate|3199|(1, 14, 13)|var|int8
call_3197 = func_3196_call(var_3198,var_3199,)
output = call_3197
func_3200 = relay.Function([var_3198,var_3199,], output)
mutated_mod['func_3200'] = func_3200
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3212 = relay.var("var_3212", dtype = "float64", shape = (14, 1, 5))#candidate|3212|(14, 1, 5)|var|float64
uop_3213 = relay.atanh(var_3212.astype('float64')) # shape=(14, 1, 5)
var_3222 = relay.var("var_3222", dtype = "float64", shape = (14, 15, 5))#candidate|3222|(14, 15, 5)|var|float64
bop_3223 = relay.power(var_3212.astype('float32'), var_3222.astype('float32')) # shape=(14, 15, 5)
uop_3229 = relay.acosh(uop_3213.astype('float64')) # shape=(14, 1, 5)
output = relay.Tuple([bop_3223,uop_3229,])
output2 = relay.Tuple([bop_3223,uop_3229,])
func_3258 = relay.Function([var_3212,var_3222,], output)
mod['func_3258'] = func_3258
mod = relay.transform.InferType()(mod)
mutated_mod['func_3258'] = func_3258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3258_call = mutated_mod.get_global_var('func_3258')
var_3260 = relay.var("var_3260", dtype = "float64", shape = (14, 1, 5))#candidate|3260|(14, 1, 5)|var|float64
var_3261 = relay.var("var_3261", dtype = "float64", shape = (14, 15, 5))#candidate|3261|(14, 15, 5)|var|float64
call_3259 = func_3258_call(var_3260,var_3261,)
output = call_3259
func_3262 = relay.Function([var_3260,var_3261,], output)
mutated_mod['func_3262'] = func_3262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3106_call = mod.get_global_var('func_3106')
func_3108_call = mutated_mod.get_global_var('func_3108')
call_3268 = func_3106_call()
call_3269 = func_3106_call()
const_3271 = relay.const([[[8.665756,6.353060,-0.650682,3.267448,1.744526,-7.509693],[-1.350408,0.542301,9.461367,-8.565365,7.831281,3.347395]],[[1.079037,1.535640,3.083160,1.230431,5.207809,-9.675503],[7.281356,3.844466,-0.977599,2.672599,6.711299,-3.980553]],[[7.802391,6.688743,0.452871,-0.270613,-2.173572,4.841356],[-4.650102,-8.892757,0.474112,0.051762,-8.132315,9.068300]],[[-4.062735,0.531611,3.133276,-8.613997,6.970041,-4.189818],[-6.234435,8.854713,-8.863973,7.330143,3.213480,-5.624762]],[[-9.088382,2.550048,-5.175089,8.175401,-7.540761,-6.024263],[5.035875,-2.567698,-7.741997,8.404616,5.794720,9.813537]],[[9.276205,-7.579899,-1.795556,0.617511,-9.808531,8.797001],[-5.047850,-3.771504,-5.919359,-0.566909,8.890999,-3.432256]],[[8.685089,3.655036,-0.293911,-3.298375,3.755165,8.946686],[4.502292,-6.055564,4.185903,8.298984,-1.624091,-4.840164]],[[-9.522936,-9.038993,0.585991,-2.650263,-9.403956,0.980952],[-7.209602,-4.507768,-4.585508,-2.106778,9.551674,-6.979241]],[[-1.525153,-9.048092,4.329103,7.710730,3.010787,5.008067],[-4.079434,-8.484005,9.308056,-6.766746,8.836557,4.886388]],[[-2.916169,-1.666190,-3.612825,-3.003658,-7.792163,-1.401273],[-4.086029,0.817618,6.543282,-0.129535,-5.330869,6.970045]],[[2.045151,-4.264485,-2.277652,-6.757265,8.643749,-1.251192],[7.383100,-6.002275,6.987936,3.084757,4.553639,-5.181349]],[[-7.630287,-3.051623,0.548030,-2.901338,1.846960,4.716521],[8.133415,-8.946967,-6.556230,-0.449766,-4.917613,5.345293]],[[0.758273,9.225252,-1.345560,-7.447618,-9.107280,4.047336],[-7.553565,-8.688923,-9.271127,5.726648,-8.600416,-3.586223]]], dtype = "float64")#candidate|3271|(13, 2, 6)|const|float64
bop_3272 = relay.maximum(call_3268.astype('int64'), relay.reshape(const_3271.astype('int64'), relay.shape_of(call_3268))) # shape=(13, 2, 6)
bop_3275 = relay.maximum(call_3269.astype('int64'), relay.reshape(const_3271.astype('int64'), relay.shape_of(call_3269))) # shape=(13, 2, 6)
bop_3276 = relay.logical_or(const_3271.astype('bool'), relay.reshape(call_3268.astype('bool'), relay.shape_of(const_3271))) # shape=(13, 2, 6)
bop_3279 = relay.logical_or(const_3271.astype('bool'), relay.reshape(call_3269.astype('bool'), relay.shape_of(const_3271))) # shape=(13, 2, 6)
bop_3280 = relay.subtract(call_3268.astype('int16'), relay.reshape(bop_3272.astype('int16'), relay.shape_of(call_3268))) # shape=(13, 2, 6)
bop_3283 = relay.subtract(call_3269.astype('int16'), relay.reshape(bop_3275.astype('int16'), relay.shape_of(call_3269))) # shape=(13, 2, 6)
uop_3291 = relay.log2(call_3268.astype('float32')) # shape=(13, 2, 6)
uop_3293 = relay.log2(call_3269.astype('float32')) # shape=(13, 2, 6)
output = relay.Tuple([bop_3276,bop_3280,uop_3291,])
output2 = relay.Tuple([bop_3279,bop_3283,uop_3293,])
func_3294 = relay.Function([], output)
mod['func_3294'] = func_3294
mod = relay.transform.InferType()(mod)
output = func_3294()
func_3295 = relay.Function([], output)
mutated_mod['func_3295'] = func_3295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2528_call = mod.get_global_var('func_2528')
func_2529_call = mutated_mod.get_global_var('func_2529')
call_3323 = relay.TupleGetItem(func_2528_call(), 0)
call_3324 = relay.TupleGetItem(func_2529_call(), 0)
func_2863_call = mod.get_global_var('func_2863')
func_2864_call = mutated_mod.get_global_var('func_2864')
call_3337 = relay.TupleGetItem(func_2863_call(), 0)
call_3338 = relay.TupleGetItem(func_2864_call(), 0)
func_3258_call = mod.get_global_var('func_3258')
func_3262_call = mutated_mod.get_global_var('func_3262')
const_3341 = relay.const([[0.367901,-6.792556,-0.361936,0.714619,-7.495053,-3.624835,2.745468,-4.918664,2.095869,2.792096,7.743645,-4.079367,-5.188162,8.830728,-9.251451,-8.076790,-6.334517,5.081458,5.319467,8.036629,9.170036,9.037841,-6.927380,1.744296,-2.163786,-9.386592,-4.079038,9.026978,-4.078586,-0.939530,9.829062,-7.925445,0.556852,-8.201274,-2.833900,-6.105172,4.118873,-0.893582,6.395997,7.443175,-3.251857,6.930481,-7.249881,-1.830456,5.212960,4.246902,0.464242,-3.219762,-9.004573,3.442460,7.954567,-7.960507,7.024346,-0.531952,-4.562419,-0.418812,7.941979,-7.848389,-3.655954,-8.236756,9.887742,-0.656565,1.279436,9.307220,2.859661,-3.120254,-3.424084,6.281494,7.952925,-7.590199]], dtype = "float64")#candidate|3341|(1, 70)|const|float64
const_3342 = relay.const([-2.588189,2.685911,-9.200763,-4.489629,4.972056,-1.946250,9.524396,-2.649534,-9.551474,7.225247,6.172932,7.257300,-7.834650,0.621757,-3.088336,-0.783869,-6.596461,-1.925991,2.270019,-3.793305,3.110980,8.047996,-4.663372,-2.828296,-5.914261,2.460130,-7.977617,7.132949,-9.230050,8.824446,1.624095,9.567526,4.596503,-2.454494,-9.100248,2.224589,1.428950,-6.218118,8.058355,-9.899699,9.350496,8.883438,-0.106988,-0.938904,5.466608,-4.255767,-9.657034,-9.105068,3.080872,-9.411689,5.147983,5.787013,5.753800,-6.436435,-9.634531,-3.029805,-1.743956,-0.807701,-8.022686,4.559552,-2.568207,-1.217354,5.346232,-1.928264,8.913662,-0.349490,-5.224089,4.299519,-2.763639,-5.213928,5.141510,-9.304119,0.917613,-1.170344,6.294300,0.413813,3.834166,-9.696734,1.414813,4.386467,-4.696379,7.466915,-7.889988,-9.421298,4.430232,4.175401,5.735020,-5.883371,-2.479725,3.790154,4.332816,1.418336,-2.967372,7.228757,-1.341916,3.277029,1.971628,-6.848025,8.593906,-7.230769,3.691073,3.428728,4.254218,4.279435,5.477931,1.488269,-9.124800,2.618590,8.813763,-2.055808,-2.220071,-9.115116,-5.449495,4.793928,2.508134,-7.316870,1.825212,7.462893,-4.301556,6.508961,0.753828,-5.041901,4.158660,5.790247,-7.653325,2.754040,0.898342,-0.379102,-4.754622,1.497029,2.690690,-9.014382,-6.571402,4.110366,0.681779,-9.379007,-7.627549,-6.919436,-9.489407,-4.833282,8.793356,1.889960,9.672437,-9.413299,6.219955,3.219404,-6.746415,-9.830009,6.180161,4.145608,-7.978513,-6.050725,-8.758901,-5.466782,-3.082936,8.190990,-9.314155,-5.273091,3.626242,8.306772,-0.549184,8.498753,4.878003,4.014757,-4.295395,8.280826,-4.688605,5.037796,-7.386103,-6.103384,-4.306057,-3.985373,-3.348967,-0.633381,6.761415,1.844816,-6.231604,-2.816363,-4.913938,-3.319653,-8.290620,2.290718,3.691245,1.367333,-5.623019,-6.519833,-8.759814,-7.404031,1.303944,-1.668082,-5.942052,3.490349,-2.746397,-0.478360,5.917876,4.515161,-6.033632,9.910749,7.604469,7.225979,-2.191566,-1.556761,-4.787966,0.289669,2.830356,7.383113,2.455782,-5.232225,-8.818134,-8.857458,-2.237125,-0.769744,-8.993827,-7.815808,-6.369682,-2.682907,-5.484318,6.977097,3.362696,-1.761617,-6.887816,-6.339026,-4.375862,-8.663090,-4.261351,8.840116,-6.345113,9.571469,8.571063,6.905675,-3.973968,-2.149140,-4.718524,3.245453,-0.529598,6.045937,5.645678,6.269600,-8.428549,5.458031,-7.140835,4.440360,-3.283330,-6.699241,0.215682,9.262723,3.180026,-5.523848,-5.712978,4.129370,8.050646,2.247444,-3.369705,8.882055,-2.511165,3.083059,7.217631,-4.957533,-5.041361,2.602462,-0.720927,4.523769,-3.268832,0.422537,5.694848,7.981111,8.434192,-5.700902,5.940428,4.388623,-1.870910,5.548998,3.300157,6.828458,-1.208966,9.890120,0.803293,-8.088214,-4.604455,-3.790329,-7.648578,5.612826,9.511107,9.931178,0.255840,-9.309047,-2.574646,6.281935,5.605893,6.253120,5.778041,-5.573608,7.759156,-7.970868,3.344904,8.529673,-2.971680,5.305975,-1.817943,6.465831,7.690084,3.152492,7.716748,-6.246363,1.716601,-4.409028,-9.535248,-3.447745,4.661878,-3.611735,9.494015,-1.587149,-5.332760,1.740807,-3.883219,-7.612047,3.935471,8.664243,-5.574578,8.995385,3.393360,-9.173041,3.420835,9.483084,1.538406,3.645536,-3.875301,-3.006981,6.848061,3.624805,-2.784840,-1.733833,-1.364360,-4.990738,1.586168,-2.852143,3.175474,-0.947277,6.500591,5.869485,3.478414,-0.142074,-6.570284,-7.554814,-6.759408,-6.180463,7.229812,-3.098222,-5.512654,-1.447393,7.695159,4.212013,7.000048,5.810700,4.669797,5.014128,1.796531,-6.303704,0.892953,7.073416,0.671883,-6.910000,-5.452069,-6.582598,-5.489215,-8.364296,3.795371,-3.081770,-6.254822,-1.096420,6.817389,-4.930659,0.858257,-5.850495,-1.130444,-2.247404,9.797709,-2.175451,-6.452288,8.663220,-7.570456,-2.791537,3.766872,-4.208113,-5.610341,3.627520,0.682098,-3.062511,8.997640,2.628158,-3.373645,8.399004,-9.862710,-8.950626,-9.631040,7.851836,7.157810,-2.977511,0.326541,-0.459360,1.528111,4.736885,-9.233664,5.627182,-2.126406,3.859658,5.683480,8.262679,-4.690557,-9.937370,4.671992,5.089681,2.188583,2.482714,2.337827,-9.519739,5.419059,5.600928,9.847551,6.132348,7.659065,-4.946044,0.188709,-0.848456,0.555739,-0.745326,4.485957,-9.283563,-4.861567,3.153627,0.025381,-9.562195,4.222089,-1.820419,8.964558,-7.096830,-1.128136,1.410775,-2.702462,-9.274446,-8.444409,-9.975592,-4.770462,-6.208127,-5.328034,-2.513747,3.286157,1.974388,-3.982811,7.617231,1.255424,-0.551789,-3.434467,-6.482599,-1.949256,3.453895,4.950192,-6.551010,-6.375273,-8.454972,-6.463552,-5.187686,-9.482340,-7.156612,-4.506275,-4.429107,6.594964,0.382932,-3.276021,2.966251,-6.260399,0.825171,-2.709847,-6.183476,-7.357229,-3.399416,4.586962,-2.567443,-7.712979,6.265025,-9.219078,-1.974343,-9.413491,0.281355,4.662308,0.119980,6.523755,-5.690393,-0.473305,-0.138266,6.077438,0.709908,-3.685221,-0.407159,-7.647864,1.760382,5.623748,9.999012,5.043891,-8.221493,9.335909,2.636087,-3.451684,-5.505632,-1.841783,8.832171,9.031137,-4.038043,-9.876893,-4.818993,-1.916731,3.981402,-5.062218,-2.923423,-0.274844,-1.686204,-5.709356,-6.312164,6.104540,-7.264582,-2.264020,-3.773972,-9.211995,9.296270,6.007918,-4.327730,0.518373,-2.056287,-1.966804,1.761070,1.453719,-0.652426,7.564705,9.476448,2.915402,-5.337310,6.389052,-7.443130,-4.826799,7.111075,7.340911,8.107215,6.000110,-0.868581,-5.819816,-6.562274,-5.812536,-2.915266,-4.867378,-6.652675,4.039575,9.283830,7.908604,-5.330989,5.726657,-0.628364,0.865909,4.169008,9.618288,-6.484950,7.899628,0.211180,4.260754,-8.438503,7.735007,-1.240365,9.951833,-8.774410,8.859960,-7.481606,-3.864931,8.916101,5.201324,-4.215410,1.346743,-8.443821,-3.660576,-4.871210,3.739205,8.562385,5.618309,3.190797,8.424820,-3.099923,0.899945,9.467389,1.518784,9.315644,1.067617,8.594844,4.458277,0.858995,0.401199,3.187067,-7.966589,-3.274826,-8.674788,8.049536,4.395157,-4.734960,-3.308765,-9.578602,8.305077,-3.610999,0.333225,3.419991,-7.544613,-1.339178,-8.233400,-4.224498,-2.882276,-4.390461,1.217116,-5.764573,1.135327,8.257385,-8.885986,0.811107,7.685620,-4.032008,4.408449,1.071526,8.017510,-3.397237,-8.350413,-3.314236,2.873640,3.375252,-6.922675,8.495818,5.285138,-8.130793,-0.797399,0.965431,6.742605,-1.603237,0.274753,-6.475492,-9.506439,-6.110908,-8.035673,3.377532,2.641764,-9.935650,0.734329,-2.469304,-9.350292,-8.452784,-6.545419,-7.691047,-4.505490,5.371583,5.608756,-6.831909,-7.469011,-3.290925,7.360348,-4.782248,-3.131721,2.572041,-6.027826,-7.123217,-4.687408,7.122356,-0.365940,-7.911831,-6.572792,-1.589133,-1.302763,9.541352,2.826080,9.122586,-0.353981,-9.585447,-3.677090,-4.153129,2.498999,8.819649,3.000582,-5.485192,-6.263846,-7.306740,-8.112627,-9.795126,7.013532,4.217662,2.669384,-0.328201,-6.543958,9.044123,-9.125271,2.502973,-0.070680,0.372023,2.617069,-6.274317,-1.008061,9.048939,3.900672,8.533537,3.811875,-7.651279,3.432659,-2.538589,3.781653,-0.974084,5.705486,5.609669,-1.274874,-7.398159,-7.357597,-0.428558,1.009195,-8.829195,6.302280,-7.437240,-1.855173,-4.980920,9.167061,-7.282720,-5.516994,-9.016269,-2.279106,0.956398,-6.742841,8.958051,-3.541352,3.835511,9.462854,9.437503,-7.947065,5.600766,-3.378596,-2.388134,2.947352,-6.218243,-1.577188,6.531428,-6.033057,0.290877,-1.144010,9.263743,-2.434983,8.621051,-0.924180,9.904571,-5.846208,-2.022368,-0.360482,-6.265835,2.086247,9.063477,1.712329,-1.413356,8.713903,-2.784465,-0.539127,6.725926,-6.682890,-1.375914,2.670516,0.441981,7.371715,-5.915118,7.899178,7.508326,4.027230,-5.162880,6.373427,-6.382404,-3.730421,7.867448,-6.309961,-5.544909,3.384862,-9.247926,-9.886203,-0.785831,3.294313,0.188327,6.772735,1.877928,5.900085,0.931066,-9.259602,8.623424,-8.248957,-5.582447,1.726319,9.563415,0.796496,6.992323,-8.515207,1.562607,-6.036026,-2.940659,1.298513,-9.262858,7.337318,-9.105016,8.212313,-0.114917,-1.985830,9.737055,8.433526,-3.296879,-5.849356,-9.298072,4.587098,-9.295716,-5.183040,3.156939,-5.449596,-5.613839,1.364412,4.885274,7.635039,-8.764059,-7.497143,8.741733,-2.530844,4.241604,-6.896202,6.501181,1.126542,0.571099,-0.641150,-9.272451,0.353198,-7.127002,0.045697,5.419590,-6.315967,-5.770960,0.850707,-4.779608,6.253434,-2.571721,-6.528100,5.752529,4.314209,5.557847,4.317497,-1.298054,1.971262,5.507677,0.716296,4.322964,-9.871036,-7.760950,9.837650,2.478173,-4.871280,-0.102879,-3.821629,7.148775,2.158504,7.828252,-6.344638,9.450703,8.556035,-9.595302,0.592913,-5.880509,4.901878,-6.580365,4.453791,3.902851,6.952484,-4.716658,3.262248,-4.309830,3.773425,0.743248,3.033820,6.120825,6.475990,4.794683,8.627699,-7.327863,9.959511,1.266714,-7.926990,-7.584222,9.782057,2.662202,-1.430550,1.200207,-8.517587,9.655366,1.996824,-2.728138,-5.832723,6.096848,9.910773,-2.058747,-4.438677,7.058264,-2.139724,6.629855,3.030910,-2.150595,-0.876537,7.927459,-2.393328,-7.706540,5.196896,-6.274786,6.723907,7.655772,3.408833,3.000006,1.091834,2.061958,-8.748377,7.148134,2.819687,-6.373145,1.590846,-6.234733,-2.817189,2.320510,7.711189,-3.262444,-6.544198,2.214897,2.113396,0.939071,-9.633301,7.756238,7.944609,-0.429751,-9.431899,-0.888591,-8.319405,-9.091759,-4.535345,-0.418358,4.083632,-7.734708,-6.816268,-6.950074,-2.599474,-1.103210,-7.648291,0.186076,5.043186,-1.913335,-4.670212,7.430480,-2.559074,-6.480281,-1.287018,-2.159671,5.267811,1.947747,6.578637,9.164632,6.072111,-2.286490,9.863458,-3.633153,8.297587,4.555228,9.328537,-7.160854,-1.113015,-6.091145,0.099278,-6.493701,5.283929,-8.284169,7.673917,-4.700834,8.773962,-6.474986,5.758278,8.388042,-4.483225,-8.603891,-0.291715,9.046034,3.625467,3.003564,-5.010430,4.472581,6.278382,-4.256018,-6.561345,1.282991,1.344692,-5.060198,-8.829034,7.324187,-5.268410,7.942211,-1.831733,3.210533,-1.293337,-6.770723,1.386255,2.884402,8.023200,5.513171,-6.211666,-1.403309,6.652539,-1.600415,-0.495110,-1.534216,-8.161762,0.805438,-5.391041,-4.882677,0.574703,6.987005,9.405637,9.949282,3.271404,-3.542055,-7.477975,2.026458,0.868894,7.277919,-0.549330,0.676521,7.853860,8.176940,5.108662,3.725496,3.000140,5.660246,9.088365,0.027049,-6.657995,-4.490574,-2.415701,-5.765129,-6.993032,-6.949159,3.627238,6.741516,-8.567052,-1.455676,-8.011414,9.135410,-3.700239,-0.635345,5.908646,-6.357290], dtype = "float64")#candidate|3342|(1050,)|const|float64
call_3340 = relay.TupleGetItem(func_3258_call(relay.reshape(const_3341.astype('float64'), [14, 1, 5]), relay.reshape(const_3342.astype('float64'), [14, 15, 5]), ), 1)
call_3343 = relay.TupleGetItem(func_3262_call(relay.reshape(const_3341.astype('float64'), [14, 1, 5]), relay.reshape(const_3342.astype('float64'), [14, 15, 5]), ), 1)
uop_3348 = relay.erf(call_3337.astype('float32')) # shape=(13, 2, 6)
uop_3350 = relay.erf(call_3338.astype('float32')) # shape=(13, 2, 6)
output = relay.Tuple([call_3323,call_3340,const_3341,const_3342,uop_3348,])
output2 = relay.Tuple([call_3324,call_3343,const_3341,const_3342,uop_3350,])
func_3353 = relay.Function([], output)
mod['func_3353'] = func_3353
mod = relay.transform.InferType()(mod)
output = func_3353()
func_3354 = relay.Function([], output)
mutated_mod['func_3354'] = func_3354
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3082_call = mod.get_global_var('func_3082')
func_3084_call = mutated_mod.get_global_var('func_3084')
call_3374 = relay.TupleGetItem(func_3082_call(), 0)
call_3375 = relay.TupleGetItem(func_3084_call(), 0)
func_3258_call = mod.get_global_var('func_3258')
func_3262_call = mutated_mod.get_global_var('func_3262')
const_3381 = relay.const([-3.698979,-1.000327,8.360494,-0.187800,-7.638906,-2.238498,4.620363,-8.710535,-6.199645,7.589810,-7.482487,9.465554,-5.609837,2.447265,9.059007,2.991805,-3.713022,8.896678,7.384060,-9.445813,8.894052,7.170469,1.280347,-6.914356,7.708986,-4.739485,3.860092,-7.840384,2.436701,6.282150,-1.860067,3.212376,-7.150631,-7.061304,-6.802318,-2.355132,2.797256,-3.406098,7.944827,-7.029648,-0.353718,0.081536,-2.240754,1.132538,9.221290,9.561101,2.516755,-7.097910,4.533274,6.987747,-1.681852,-3.700198,7.031409,-7.634983,7.322934,3.947544,2.650763,6.925202,3.021128,3.473930,-8.412035,-5.792622,1.284357,9.980190,-7.780482,-0.113324,-9.127829,-9.391132,4.314897,0.960527], dtype = "float64")#candidate|3381|(70,)|const|float64
var_3382 = relay.var("var_3382", dtype = "float64", shape = (1050,))#candidate|3382|(1050,)|var|float64
call_3380 = relay.TupleGetItem(func_3258_call(relay.reshape(const_3381.astype('float64'), [14, 1, 5]), relay.reshape(var_3382.astype('float64'), [14, 15, 5]), ), 1)
call_3383 = relay.TupleGetItem(func_3262_call(relay.reshape(const_3381.astype('float64'), [14, 1, 5]), relay.reshape(var_3382.astype('float64'), [14, 15, 5]), ), 1)
bop_3398 = relay.power(call_3380.astype('float32'), relay.reshape(const_3381.astype('float32'), relay.shape_of(call_3380))) # shape=(14, 1, 5)
bop_3401 = relay.power(call_3383.astype('float32'), relay.reshape(const_3381.astype('float32'), relay.shape_of(call_3383))) # shape=(14, 1, 5)
uop_3405 = relay.sqrt(const_3381.astype('float32')) # shape=(70,)
func_1707_call = mod.get_global_var('func_1707')
func_1714_call = mutated_mod.get_global_var('func_1714')
var_3414 = relay.var("var_3414", dtype = "int16", shape = (288,))#candidate|3414|(288,)|var|int16
const_3415 = relay.const(-10, dtype = "uint8")#candidate|3415|()|const|uint8
var_3416 = relay.var("var_3416", dtype = "uint8", shape = (108,))#candidate|3416|(108,)|var|uint8
call_3413 = relay.TupleGetItem(func_1707_call(relay.reshape(var_3414.astype('int16'), [6, 4, 12]), relay.reshape(var_3414.astype('int16'), [6, 4, 12]), relay.reshape(const_3415.astype('uint8'), []), relay.reshape(var_3416.astype('uint8'), [6, 18]), relay.reshape(var_3416.astype('uint8'), [3, 36]), ), 2)
call_3417 = relay.TupleGetItem(func_1714_call(relay.reshape(var_3414.astype('int16'), [6, 4, 12]), relay.reshape(var_3414.astype('int16'), [6, 4, 12]), relay.reshape(const_3415.astype('uint8'), []), relay.reshape(var_3416.astype('uint8'), [6, 18]), relay.reshape(var_3416.astype('uint8'), [3, 36]), ), 2)
func_3106_call = mod.get_global_var('func_3106')
func_3108_call = mutated_mod.get_global_var('func_3108')
call_3451 = func_3106_call()
call_3452 = func_3106_call()
uop_3455 = relay.acosh(var_3382.astype('float32')) # shape=(1050,)
output = relay.Tuple([call_3374,bop_3398,uop_3405,call_3413,var_3414,const_3415,var_3416,call_3451,uop_3455,])
output2 = relay.Tuple([call_3375,bop_3401,uop_3405,call_3417,var_3414,const_3415,var_3416,call_3452,uop_3455,])
func_3461 = relay.Function([var_3382,var_3414,var_3416,], output)
mod['func_3461'] = func_3461
mod = relay.transform.InferType()(mod)
mutated_mod['func_3461'] = func_3461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3461_call = mutated_mod.get_global_var('func_3461')
var_3463 = relay.var("var_3463", dtype = "float64", shape = (1050,))#candidate|3463|(1050,)|var|float64
var_3464 = relay.var("var_3464", dtype = "int16", shape = (288,))#candidate|3464|(288,)|var|int16
var_3465 = relay.var("var_3465", dtype = "uint8", shape = (108,))#candidate|3465|(108,)|var|uint8
call_3462 = func_3461_call(var_3463,var_3464,var_3465,)
output = call_3462
func_3466 = relay.Function([var_3463,var_3464,var_3465,], output)
mutated_mod['func_3466'] = func_3466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2863_call = mod.get_global_var('func_2863')
func_2864_call = mutated_mod.get_global_var('func_2864')
call_3478 = relay.TupleGetItem(func_2863_call(), 0)
call_3479 = relay.TupleGetItem(func_2864_call(), 0)
uop_3483 = relay.sinh(call_3478.astype('float64')) # shape=(13, 2, 6)
uop_3485 = relay.sinh(call_3479.astype('float64')) # shape=(13, 2, 6)
output = relay.Tuple([uop_3483,])
output2 = relay.Tuple([uop_3485,])
func_3487 = relay.Function([], output)
mod['func_3487'] = func_3487
mod = relay.transform.InferType()(mod)
mutated_mod['func_3487'] = func_3487
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3487_call = mutated_mod.get_global_var('func_3487')
call_3488 = func_3487_call()
output = call_3488
func_3489 = relay.Function([], output)
mutated_mod['func_3489'] = func_3489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2518_call = mod.get_global_var('func_2518')
func_2520_call = mutated_mod.get_global_var('func_2520')
call_3501 = relay.TupleGetItem(func_2518_call(), 0)
call_3502 = relay.TupleGetItem(func_2520_call(), 0)
var_3520 = relay.var("var_3520", dtype = "float32", shape = (13, 2, 6))#candidate|3520|(13, 2, 6)|var|float32
bop_3521 = relay.add(call_3501.astype('int16'), relay.reshape(var_3520.astype('int16'), relay.shape_of(call_3501))) # shape=(13, 2, 6)
bop_3524 = relay.add(call_3502.astype('int16'), relay.reshape(var_3520.astype('int16'), relay.shape_of(call_3502))) # shape=(13, 2, 6)
func_2040_call = mod.get_global_var('func_2040')
func_2042_call = mutated_mod.get_global_var('func_2042')
const_3527 = relay.const([-8.865999,7.794871,-0.912972,0.197657,0.761010,-6.498776,3.101093,-0.517387,5.659964,8.453575,9.622655,-2.692795,6.212462,5.014956,-9.187489,2.000978,-9.583872,-4.948030,-2.177678,1.564850,3.447434,-6.280536,-5.424814,-8.131594,8.273831,6.973062,7.858461,-4.681049,-8.710753,3.764186,7.855451,4.116307,-5.194551,-2.114981,2.609090,-7.170625,-2.827922,1.467245,9.621614,-5.643589,-6.746746,7.444200,-0.390286,-8.958358,6.689116,6.367560,-6.291177,-1.286577,-9.832534,4.384362,-7.190017,-7.680082,7.100214,7.272582,6.059532,0.687058,-0.400983,-9.142356,4.607992,2.932545,-0.457842,8.519156,9.084642,0.337106,-8.306720,1.250869,-4.279360,1.715319,5.304782,6.519130,0.276487,-0.259948,1.712571,-5.609208,5.455426,-3.425297,-6.978181,3.926443,7.210114,1.676235,7.761246,6.556373,-5.407991,2.390738,6.012502,6.126434,-5.120323,-2.486375,-2.426740,-1.954324,-0.250089,9.008285,-4.844230,-3.763220,-8.689091,6.596038,-8.711276,0.338643,-0.591286,9.403877,2.519108,-6.044574,-8.665377,-1.953329,5.455931,2.298713,8.309652,-1.766530,7.857089,6.302249,-6.557257,4.835356,8.788910,8.222005,-6.949242,-8.449450,1.412934,9.056116,6.691912,-2.466615,-2.076910,3.916365,7.592897,3.539508,-4.323888,-5.782645,1.597951,-1.955067,-7.065101,-9.268851,-5.569987,7.536492,8.426208,4.518441,-6.324442,1.540710,8.791400,-8.153394,-2.273367,9.382870,-0.202448,9.644237,-2.765639,3.040930,-1.879403,6.469931,-1.766356,-3.068568,0.634706,-6.040566,-0.462867,-3.111061,-7.008105,-4.514319,-7.069166,-1.746808,3.706033,-1.372701,0.327250,-4.938787,-0.485820,-2.848760,-1.410914,-4.200661,-1.718600,0.082379,2.596200,9.669421,-3.519499,-2.426473,3.116953,-7.285021,2.081985,-7.215314,-7.238710,-2.398373,-8.022796,7.244091,7.093307,-1.431230,-0.869375,-6.114920,8.420829,-9.124309,9.072743,-7.588148,2.483184,5.338427,-3.818023,4.870855,6.905428,0.503314,-8.892982,-0.591251,-6.211070,1.683795,4.244980,-5.340390,1.525185,-8.210135,-3.896512,-9.306480,8.141255,-4.761495,9.459700,-3.919113,2.855137,4.088512,-6.546544,3.252005,-1.471554,-2.034263,1.102183,1.013874,2.613481,7.900875], dtype = "float64")#candidate|3527|(216,)|const|float64
call_3526 = relay.TupleGetItem(func_2040_call(relay.reshape(const_3527.astype('float64'), [3, 9, 8])), 0)
call_3528 = relay.TupleGetItem(func_2042_call(relay.reshape(const_3527.astype('float64'), [3, 9, 8])), 0)
func_2765_call = mod.get_global_var('func_2765')
func_2767_call = mutated_mod.get_global_var('func_2767')
call_3531 = func_2765_call()
call_3532 = func_2765_call()
func_2020_call = mod.get_global_var('func_2020')
func_2023_call = mutated_mod.get_global_var('func_2023')
const_3538 = relay.const([-7,10,-5,-10,-10,-10,-4,8,-3,8,-7,2,9,-9,-5,-2,9,-8,-5,-9,-1,-7,4,-10,10,-2,8,-5,9,-7,10,7,-5,4,-5,7,3,-10,7,-5,-6,6,-1,5,4,-6,-3,-6,8,-10,-4,-7,-9,4,-7,-5,-8,-10,-9,-2,-7,9,-1,-10,-6,2,-5,7,-7,2,-3,-8,-5,3,1,8,4,-8,4,-4,8,10,-6,-9,-1,-7,-7,7,-3,-5,6,2,3,-4,10,5,5,-3,-4,4,-3,-10,-5,-2,7,-5,-3,2,-9,-10,4,8,1,-2,6,-2,8,1,1,4,-1,1,-5,7,-9,4,-2,-5,-8,2,3,-4,8,-4,9,6,-6,5,2,-5,10,-4,-4,7,-6,-5,-5,-1,6,-1,-5,4,-6,3,2,-8,-9,-5,1,-4,-3,7,-10,8,-4,-1,-7,-10,-6,2,-3,8,-3,7,-7,9,2,5,-4,7,3,9,-5,-7,-4,-6,-9,10,-9,4,-8,3], dtype = "int16")#candidate|3538|(192,)|const|int16
call_3537 = func_2020_call(relay.reshape(const_3538.astype('int16'), [4, 12, 4]), relay.reshape(const_3538.astype('int16'), [4, 12, 4]), )
call_3539 = func_2020_call(relay.reshape(const_3538.astype('int16'), [4, 12, 4]), relay.reshape(const_3538.astype('int16'), [4, 12, 4]), )
func_2638_call = mod.get_global_var('func_2638')
func_2642_call = mutated_mod.get_global_var('func_2642')
var_3546 = relay.var("var_3546", dtype = "float64", shape = (1, 198))#candidate|3546|(1, 198)|var|float64
call_3545 = relay.TupleGetItem(func_2638_call(relay.reshape(var_3546.astype('float64'), [198,]), relay.reshape(const_3527.astype('float64'), [216,]), ), 2)
call_3547 = relay.TupleGetItem(func_2642_call(relay.reshape(var_3546.astype('float64'), [198,]), relay.reshape(const_3527.astype('float64'), [216,]), ), 2)
output = relay.Tuple([bop_3521,call_3526,const_3527,call_3531,call_3537,const_3538,call_3545,var_3546,])
output2 = relay.Tuple([bop_3524,call_3528,const_3527,call_3532,call_3539,const_3538,call_3547,var_3546,])
func_3550 = relay.Function([var_3520,var_3546,], output)
mod['func_3550'] = func_3550
mod = relay.transform.InferType()(mod)
var_3551 = relay.var("var_3551", dtype = "float32", shape = (13, 2, 6))#candidate|3551|(13, 2, 6)|var|float32
var_3552 = relay.var("var_3552", dtype = "float64", shape = (1, 198))#candidate|3552|(1, 198)|var|float64
output = func_3550(var_3551,var_3552,)
func_3553 = relay.Function([var_3551,var_3552,], output)
mutated_mod['func_3553'] = func_3553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3106_call = mod.get_global_var('func_3106')
func_3108_call = mutated_mod.get_global_var('func_3108')
call_3579 = func_3106_call()
call_3580 = func_3106_call()
uop_3581 = relay.sin(call_3579.astype('float32')) # shape=(13, 2, 6)
uop_3583 = relay.sin(call_3580.astype('float32')) # shape=(13, 2, 6)
var_3585 = relay.var("var_3585", dtype = "float32", shape = (13, 2, 6))#candidate|3585|(13, 2, 6)|var|float32
bop_3586 = relay.right_shift(uop_3581.astype('int32'), relay.reshape(var_3585.astype('int32'), relay.shape_of(uop_3581))) # shape=(13, 2, 6)
bop_3589 = relay.right_shift(uop_3583.astype('int32'), relay.reshape(var_3585.astype('int32'), relay.shape_of(uop_3583))) # shape=(13, 2, 6)
func_3196_call = mod.get_global_var('func_3196')
func_3200_call = mutated_mod.get_global_var('func_3200')
const_3598 = relay.const(-9, dtype = "int8")#candidate|3598|()|const|int8
var_3599 = relay.var("var_3599", dtype = "int8", shape = (182,))#candidate|3599|(182,)|var|int8
call_3597 = relay.TupleGetItem(func_3196_call(relay.reshape(const_3598.astype('int8'), []), relay.reshape(var_3599.astype('int8'), [1, 14, 13]), ), 0)
call_3600 = relay.TupleGetItem(func_3200_call(relay.reshape(const_3598.astype('int8'), []), relay.reshape(var_3599.astype('int8'), [1, 14, 13]), ), 0)
func_2899_call = mod.get_global_var('func_2899')
func_2901_call = mutated_mod.get_global_var('func_2901')
call_3606 = func_2899_call()
call_3607 = func_2899_call()
func_3082_call = mod.get_global_var('func_3082')
func_3084_call = mutated_mod.get_global_var('func_3084')
call_3612 = relay.TupleGetItem(func_3082_call(), 1)
call_3613 = relay.TupleGetItem(func_3084_call(), 1)
output = relay.Tuple([bop_3586,call_3597,const_3598,var_3599,call_3606,call_3612,])
output2 = relay.Tuple([bop_3589,call_3600,const_3598,var_3599,call_3607,call_3613,])
func_3628 = relay.Function([var_3585,var_3599,], output)
mod['func_3628'] = func_3628
mod = relay.transform.InferType()(mod)
mutated_mod['func_3628'] = func_3628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3628_call = mutated_mod.get_global_var('func_3628')
var_3630 = relay.var("var_3630", dtype = "float32", shape = (13, 2, 6))#candidate|3630|(13, 2, 6)|var|float32
var_3631 = relay.var("var_3631", dtype = "int8", shape = (182,))#candidate|3631|(182,)|var|int8
call_3629 = func_3628_call(var_3630,var_3631,)
output = call_3629
func_3632 = relay.Function([var_3630,var_3631,], output)
mutated_mod['func_3632'] = func_3632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3353_call = mod.get_global_var('func_3353')
func_3354_call = mutated_mod.get_global_var('func_3354')
call_3677 = relay.TupleGetItem(func_3353_call(), 2)
call_3678 = relay.TupleGetItem(func_3354_call(), 2)
const_3690 = relay.const([[2.314162,-7.163268,5.549039,9.235758,-5.536759,-5.007480,6.877068,-7.238746,4.290316,-4.828050,-3.244307,-5.005661,4.051562,9.217460,3.240619,-5.322460,0.665497,7.165780,9.846419,-6.779280,9.376271,-3.936698,-6.197408,-4.210645,-5.088637,7.433822,1.922302,6.744263,-9.412748,5.910185,1.566054,-7.453842,1.755424,6.154992,-5.450540,-3.999550,-1.144871,-2.714198,3.080115,-3.864921,3.531608,-6.255899,6.205519,5.767968,8.770673,-5.204588,-4.166356,9.091705,-0.395410,-1.379668,-2.531130,-6.160945,0.574881,2.411005,6.927165,9.552665,-3.482298,9.524065,2.112280,4.794366,-8.203151,3.733740,-7.906597,-9.683295,-3.526612,4.347576,1.693229,6.325917,1.598174,7.739348]], dtype = "float64")#candidate|3690|(1, 70)|const|float64
bop_3691 = relay.add(call_3677.astype('uint16'), relay.reshape(const_3690.astype('uint16'), relay.shape_of(call_3677))) # shape=(1, 70)
bop_3694 = relay.add(call_3678.astype('uint16'), relay.reshape(const_3690.astype('uint16'), relay.shape_of(call_3678))) # shape=(1, 70)
func_2765_call = mod.get_global_var('func_2765')
func_2767_call = mutated_mod.get_global_var('func_2767')
call_3715 = func_2765_call()
call_3716 = func_2765_call()
var_3724 = relay.var("var_3724", dtype = "float32", shape = (13, 2, 6))#candidate|3724|(13, 2, 6)|var|float32
bop_3725 = relay.floor_divide(call_3715.astype('float64'), relay.reshape(var_3724.astype('float64'), relay.shape_of(call_3715))) # shape=(13, 2, 6)
bop_3728 = relay.floor_divide(call_3716.astype('float64'), relay.reshape(var_3724.astype('float64'), relay.shape_of(call_3716))) # shape=(13, 2, 6)
output = relay.Tuple([bop_3691,bop_3725,])
output2 = relay.Tuple([bop_3694,bop_3728,])
func_3733 = relay.Function([var_3724,], output)
mod['func_3733'] = func_3733
mod = relay.transform.InferType()(mod)
var_3734 = relay.var("var_3734", dtype = "float32", shape = (13, 2, 6))#candidate|3734|(13, 2, 6)|var|float32
output = func_3733(var_3734)
func_3735 = relay.Function([var_3734], output)
mutated_mod['func_3735'] = func_3735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3487_call = mod.get_global_var('func_3487')
func_3489_call = mutated_mod.get_global_var('func_3489')
call_3740 = relay.TupleGetItem(func_3487_call(), 0)
call_3741 = relay.TupleGetItem(func_3489_call(), 0)
func_2638_call = mod.get_global_var('func_2638')
func_2642_call = mutated_mod.get_global_var('func_2642')
const_3757 = relay.const([3.781162,1.091704,-6.367961,6.585975,-4.386287,9.127910,2.785212,9.592105,4.103956,6.221054,-7.321727,-2.420367,5.387692,1.593174,6.287786,-0.714899,1.458623,-2.018571,-9.281359,-7.493404,-7.640751,-6.923854,9.630406,-6.886145,5.672960,6.547326,-5.454211,-2.093739,-8.710689,5.332180,6.995026,0.063603,1.771136,-5.437921,9.348975,-2.811939,-5.101782,1.755085,6.015341,7.820619,7.170831,-7.380587,-3.887852,2.861422,3.314007,-9.137754,-2.278488,6.936061,2.266375,2.152880,6.517101,9.714125,-0.660088,3.770488,-4.975613,5.148653,2.168934,-3.558383,-4.720964,9.922471,-9.864943,5.891020,6.377205,-1.437675,-4.179512,2.453314,-5.064501,-8.403584,-1.563441,-5.385800,-4.571866,-7.175662,2.385798,2.591709,8.309214,0.500454,-1.831184,-6.690477,-7.125250,5.953043,4.595262,-4.893644,5.630530,-3.386496,-7.913639,-3.056714,-5.292119,5.482462,1.307210,-0.755376,1.877471,-9.365977,-3.766633,0.884887,-1.219921,7.699094,7.348587,4.244477,-8.574353,-2.748748,-1.615742,1.595742,-8.431318,-8.854346,8.838560,-3.130908,0.287783,7.534738,4.417464,-3.926001,6.315925,6.036744,1.145035,0.034864,0.139104,-5.374537,-3.688807,-8.057723,-8.894207,1.046217,6.053828,-3.774753,-7.295345,-5.369631,-1.448006,1.067302,1.366272,1.261913,1.956308,-7.230019,-5.380509,-0.357660,4.621093,9.258206,-6.136875,2.286927,-0.038133,-3.154875,0.003435,4.758765,7.157908,7.391613,5.450865,0.329134,2.541810,2.298197,-2.847490,7.670540,3.683794,-0.142544,2.433300,1.989542,6.541244,-3.743914,6.267010,5.339870,0.237848,7.007361,8.201466,1.431277,-6.306163,-5.815258,0.050890,-4.027547,5.401160,-3.660405,5.779691,-4.629011,3.016686,5.671912,-1.569770,5.857682,-0.023891,4.098855,4.678857,-1.604438,7.082867,-7.258364,-9.969608,0.688000,2.321870,-3.717354,-3.941651,-5.057626,-4.178926,-4.005422,-9.789179,-0.245263,-9.741283,-6.400764,-4.317933,2.402822,8.371736,-8.394378,8.497231,3.758772,3.638371,8.436434], dtype = "float64")#candidate|3757|(198,)|const|float64
const_3758 = relay.const([9.629348,-5.879346,1.950775,-8.862054,-5.300114,3.168471,-7.631439,0.062022,7.870273,2.343911,0.029988,9.337449,1.942399,-8.015299,-5.620950,-9.036853,7.107170,8.492616,3.535318,-5.972633,-4.279433,-2.610945,0.922158,1.289251,-0.282198,6.546757,5.244105,-7.541578,8.977445,7.130025,9.163166,6.528587,6.653009,7.398428,5.292520,-5.092278,-8.670139,-9.955354,-8.163816,-8.515746,-7.924731,3.648115,-1.781792,-7.262644,-2.583366,-3.786369,0.658071,2.515119,-6.261173,0.484136,-2.462266,-3.744146,2.601921,-4.055409,-4.880883,-4.215413,-3.503063,-5.468167,4.944615,-7.794316,6.384152,1.236864,7.707506,2.853072,-5.804098,4.057857,-3.211331,9.946028,-4.212903,-8.184737,-6.141207,8.541175,-6.930086,1.926802,3.652225,8.454086,-0.655422,4.740694,0.264875,-9.476722,-0.710666,1.741831,8.222045,-8.948317,-5.511661,-5.480064,9.044402,-1.570535,3.824902,0.907938,7.097229,2.200261,-3.436742,2.225199,1.495685,2.716077,1.235207,4.375907,0.918022,-1.077950,-8.927369,-1.010534,1.869022,0.541847,-1.855979,5.577795,9.608486,-9.397338,6.540741,-2.795858,9.423169,-1.746332,-9.349737,1.459101,9.368961,9.865468,-1.580138,0.747118,-9.374635,-2.239178,-3.366203,2.955348,4.165182,2.565583,2.859262,4.097153,3.439023,-5.827198,9.477984,8.104443,0.699035,-3.619510,-3.937016,1.451692,-3.432901,2.814240,2.582835,9.688692,-4.222298,-5.645200,-3.241093,-5.586650,6.415168,1.982404,-9.450268,-1.240505,5.336414,1.223834,-8.905848,1.318601,4.558946,1.770787,7.952390,8.505791,7.280815,5.277435,5.045322,7.882274,-8.486798,-2.755938,1.672808,6.176210,5.826239,-4.794567,2.364920,2.712272,9.248451,-7.648495,7.100692,-3.222353,8.422190,-4.372583,-4.551805,1.103986,-4.829804,2.362697,-8.997522,-8.529962,-9.129712,-1.875464,-5.176001,-7.948393,-7.378500,-9.694839,-5.309405,7.850145,2.355710,-9.384776,7.219132,-8.379133,4.762056,-5.270651,-5.738048,-2.232588,3.401778,0.449596,-2.849182,9.097213,-3.994757,-8.955852,6.344872,-0.686210,2.014434,-4.999806,-6.037028,-7.753409,-9.682641,-3.839727,6.223330,8.551073,6.899966,0.094828,-1.979464,-1.266477,-4.299891,1.214362], dtype = "float64")#candidate|3758|(216,)|const|float64
call_3756 = relay.TupleGetItem(func_2638_call(relay.reshape(const_3757.astype('float64'), [198,]), relay.reshape(const_3758.astype('float64'), [216,]), ), 2)
call_3759 = relay.TupleGetItem(func_2642_call(relay.reshape(const_3757.astype('float64'), [198,]), relay.reshape(const_3758.astype('float64'), [216,]), ), 2)
bop_3770 = relay.greater_equal(call_3756.astype('bool'), relay.reshape(call_3740.astype('bool'), relay.shape_of(call_3756))) # shape=(13, 2, 6)
bop_3773 = relay.greater_equal(call_3759.astype('bool'), relay.reshape(call_3741.astype('bool'), relay.shape_of(call_3759))) # shape=(13, 2, 6)
output = relay.Tuple([const_3757,const_3758,bop_3770,])
output2 = relay.Tuple([const_3757,const_3758,bop_3773,])
func_3775 = relay.Function([], output)
mod['func_3775'] = func_3775
mod = relay.transform.InferType()(mod)
mutated_mod['func_3775'] = func_3775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3775_call = mutated_mod.get_global_var('func_3775')
call_3776 = func_3775_call()
output = call_3776
func_3777 = relay.Function([], output)
mutated_mod['func_3777'] = func_3777
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3106_call = mod.get_global_var('func_3106')
func_3108_call = mutated_mod.get_global_var('func_3108')
call_3783 = func_3106_call()
call_3784 = func_3106_call()
func_1975_call = mod.get_global_var('func_1975')
func_1977_call = mutated_mod.get_global_var('func_1977')
var_3827 = relay.var("var_3827", dtype = "float64", shape = (198,))#candidate|3827|(198,)|var|float64
call_3826 = relay.TupleGetItem(func_1975_call(relay.reshape(var_3827.astype('float64'), [11, 9, 2])), 0)
call_3828 = relay.TupleGetItem(func_1977_call(relay.reshape(var_3827.astype('float64'), [11, 9, 2])), 0)
uop_3841 = relay.asin(var_3827.astype('float32')) # shape=(198,)
func_2863_call = mod.get_global_var('func_2863')
func_2864_call = mutated_mod.get_global_var('func_2864')
call_3845 = relay.TupleGetItem(func_2863_call(), 0)
call_3846 = relay.TupleGetItem(func_2864_call(), 0)
func_2570_call = mod.get_global_var('func_2570')
func_2571_call = mutated_mod.get_global_var('func_2571')
call_3848 = relay.TupleGetItem(func_2570_call(), 1)
call_3849 = relay.TupleGetItem(func_2571_call(), 1)
output = relay.Tuple([call_3783,call_3826,uop_3841,call_3845,call_3848,])
output2 = relay.Tuple([call_3784,call_3828,uop_3841,call_3846,call_3849,])
func_3855 = relay.Function([var_3827,], output)
mod['func_3855'] = func_3855
mod = relay.transform.InferType()(mod)
mutated_mod['func_3855'] = func_3855
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3856 = relay.var("var_3856", dtype = "float64", shape = (198,))#candidate|3856|(198,)|var|float64
func_3855_call = mutated_mod.get_global_var('func_3855')
call_3857 = func_3855_call(var_3856)
output = call_3857
func_3858 = relay.Function([var_3856], output)
mutated_mod['func_3858'] = func_3858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3178_call = mod.get_global_var('func_3178')
func_3179_call = mutated_mod.get_global_var('func_3179')
call_3886 = relay.TupleGetItem(func_3178_call(), 0)
call_3887 = relay.TupleGetItem(func_3179_call(), 0)
output = relay.Tuple([call_3886,])
output2 = relay.Tuple([call_3887,])
func_3892 = relay.Function([], output)
mod['func_3892'] = func_3892
mod = relay.transform.InferType()(mod)
output = func_3892()
func_3893 = relay.Function([], output)
mutated_mod['func_3893'] = func_3893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2969_call = mod.get_global_var('func_2969')
func_2970_call = mutated_mod.get_global_var('func_2970')
call_3894 = func_2969_call()
call_3895 = func_2969_call()
func_1975_call = mod.get_global_var('func_1975')
func_1977_call = mutated_mod.get_global_var('func_1977')
const_3908 = relay.const([[5.611533,-3.107557],[-0.578827,2.857849],[2.263480,-0.070159],[5.753623,4.864962],[2.108573,7.181810],[-0.576507,9.728453],[5.348837,-6.016437],[-8.777186,-5.493241],[-1.817278,4.732314],[-5.934628,0.282137],[1.686911,-1.195239],[8.534659,-2.021382],[-1.738506,8.682664],[9.036167,6.069166],[7.483843,5.105141],[-6.242142,3.472037],[-7.198903,-6.401949],[-5.194899,-0.939719],[2.828387,-9.821402],[7.238433,7.866501],[-5.081751,-3.748644],[7.791488,-0.326541],[8.898574,8.359707],[7.894844,-5.626435],[8.978304,-1.481889],[-1.778195,0.986842],[8.912115,-9.797182],[-6.399248,-6.633489],[-2.064015,-3.038035],[-5.396342,1.201652],[-4.831395,-1.829321],[0.040886,-1.149734],[2.505265,-1.318042],[9.996838,8.356227],[4.406297,6.656664],[6.001577,-1.279991],[-2.928895,-2.763284],[7.812097,-7.569538],[-0.114224,8.302747],[7.428952,-4.027278],[-7.241453,-7.928362],[-9.522324,4.088090],[4.837728,8.278026],[-1.430778,9.629295],[-6.326061,-9.369796],[2.042596,-2.317664],[4.138990,0.730989],[3.357564,7.354571],[4.245949,5.031068],[8.020890,4.280523],[-5.055799,0.093796],[6.691357,9.259655],[-8.302890,5.866696],[5.542887,6.770536],[-0.972145,6.790317],[-4.513995,4.936434],[2.877906,6.182803],[6.310504,0.645415],[7.529362,2.368389],[9.029956,1.552818],[-5.630194,5.338883],[-1.041646,-9.323313],[-4.970907,-8.451842],[-0.632052,-5.331888],[-7.251528,-8.408119],[-0.339810,8.690507],[-5.428169,-3.783324],[-4.875715,-2.669321],[6.155753,-3.945084],[-9.803750,-6.253544],[-2.010600,-1.037943],[-9.024441,-8.453713],[-6.456578,7.822226],[4.477642,1.395545],[2.494765,0.779621],[4.083763,-2.654229],[-9.531716,-6.911126],[3.531981,2.360122],[1.959925,-1.144172],[-2.994143,-2.513275],[0.453000,3.646760],[8.434358,-4.770238],[0.927805,-3.140044],[0.018408,5.867359],[5.084734,2.239593],[-1.815735,-7.809654],[-3.987807,7.582698],[-6.895546,1.137575],[5.196049,-1.168441],[5.319048,6.554355],[-7.389024,7.472715],[-4.833565,4.870444],[-4.835310,-9.705240],[2.634328,-1.351652],[1.995995,-4.941732],[-7.037021,6.981605],[4.496245,-5.502239],[8.613201,0.659837],[2.601398,1.471390]], dtype = "float64")#candidate|3908|(99, 2)|const|float64
call_3907 = relay.TupleGetItem(func_1975_call(relay.reshape(const_3908.astype('float64'), [11, 9, 2])), 0)
call_3909 = relay.TupleGetItem(func_1977_call(relay.reshape(const_3908.astype('float64'), [11, 9, 2])), 0)
uop_3910 = relay.log10(const_3908.astype('float64')) # shape=(99, 2)
func_3733_call = mod.get_global_var('func_3733')
func_3735_call = mutated_mod.get_global_var('func_3735')
call_3914 = relay.TupleGetItem(func_3733_call(relay.reshape(call_3894.astype('float32'), [13, 2, 6])), 1)
call_3915 = relay.TupleGetItem(func_3735_call(relay.reshape(call_3894.astype('float32'), [13, 2, 6])), 1)
func_1975_call = mod.get_global_var('func_1975')
func_1977_call = mutated_mod.get_global_var('func_1977')
call_3918 = relay.TupleGetItem(func_1975_call(relay.reshape(call_3907.astype('float64'), [11, 9, 2])), 0)
call_3919 = relay.TupleGetItem(func_1977_call(relay.reshape(call_3907.astype('float64'), [11, 9, 2])), 0)
func_2040_call = mod.get_global_var('func_2040')
func_2042_call = mutated_mod.get_global_var('func_2042')
var_3934 = relay.var("var_3934", dtype = "float64", shape = (216,))#candidate|3934|(216,)|var|float64
call_3933 = relay.TupleGetItem(func_2040_call(relay.reshape(var_3934.astype('float64'), [3, 9, 8])), 0)
call_3935 = relay.TupleGetItem(func_2042_call(relay.reshape(var_3934.astype('float64'), [3, 9, 8])), 0)
uop_3936 = relay.sqrt(uop_3910.astype('float64')) # shape=(99, 2)
func_1192_call = mod.get_global_var('func_1192')
func_1197_call = mutated_mod.get_global_var('func_1197')
const_3943 = relay.const([-2,7,5,-2,-5,-5,-8,-5,10,-4,3,1,6,3,2,3,2,-9,-1,-1,9,-3,-9,-8,6,9,10,9,2,10,-9,5,-7,10,7,-6,9,5,-10,6,7,-5,7,-4,9,-2,1,10,4,-7,3,-7,-3,-10,-9,8,2,-4,-9,-8,4,-7,-7,-2,8,2,-3,6,3,-10,10,8,-1,-1,-1,-1,8,10,6,6,9,7,-7,7,-9,-2,-5,1,5,8,-2,2,6,7,2,-8,-1,5,10,-8,9,7,10,-1,3,-2,-6,-7,6,4,7,-1,9,-6,7,7,6,1,-6,-3,-10,4,-9,10,-4,3,8,-10,9,-7,2,2,2,3,6], dtype = "uint64")#candidate|3943|(135,)|const|uint64
const_3944 = relay.const(1, dtype = "uint8")#candidate|3944|()|const|uint8
const_3945 = relay.const([2,-5,-8,8,2,5,5,-6,8,6,3,-7,-7,6,3,-8,-3,-1,-3,8,-8,7,-7,-2,-2,2,-8,-6,-1,3,-2,-1,7,-7,-5,-6,-10,-8,-5,-1,-1,-4,-1,5,5,-8,-2,1,2,-10,2,10,8,-8,-10,-1,1,1,-8,-6,6,-9,2,8,7,-3,-1,-1,-4,-1,6,-7,-9,-9,-7,-9,8,3,-7,7,6,-3,4,-5,10,5,10,-5,2,-8,-8,4,-7,9,6,10,-6,9,6,10,-2,6,-7,-2,4,8,9,9], dtype = "uint8")#candidate|3945|(108,)|const|uint8
call_3942 = relay.TupleGetItem(func_1192_call(relay.reshape(const_3943.astype('uint64'), [9, 15]), relay.reshape(const_3943.astype('uint64'), [9, 15]), relay.reshape(const_3944.astype('uint8'), []), relay.reshape(const_3945.astype('uint8'), [3, 36]), ), 3)
call_3946 = relay.TupleGetItem(func_1197_call(relay.reshape(const_3943.astype('uint64'), [9, 15]), relay.reshape(const_3943.astype('uint64'), [9, 15]), relay.reshape(const_3944.astype('uint8'), []), relay.reshape(const_3945.astype('uint8'), [3, 36]), ), 3)
func_3461_call = mod.get_global_var('func_3461')
func_3466_call = mutated_mod.get_global_var('func_3466')
const_3949 = relay.const([[-0.778232,1.760250,8.816189,-6.469874,-6.394199,8.952309,-4.475667,6.488625,5.092562,6.348077,-8.170008,8.669031,-1.196469,-2.360628,1.128147],[-1.447773,-0.136898,8.831587,-5.395072,-4.670206,-4.538235,-4.142053,-1.017874,9.942594,0.471750,-9.695333,-5.920928,-4.451108,-2.214822,7.107051],[-5.320824,1.395180,1.166393,-2.754718,-2.708296,-9.734752,7.010839,5.146973,-4.377017,1.558282,-3.138900,6.551155,8.291778,6.721542,-9.214969],[-9.947306,4.736090,9.581446,-1.951141,-6.460663,-3.111765,7.221692,9.851997,-2.725301,-9.801751,-9.581890,6.077247,3.513520,9.315837,-9.967026],[3.415880,-5.390197,-4.072438,-0.162828,-7.768184,-8.626704,9.464145,-5.432008,-1.575962,5.830588,-7.614583,0.005887,0.027420,-8.701576,-2.220940],[0.328955,0.161501,-2.112230,2.119880,5.461958,4.563306,0.157273,8.497620,1.776768,-1.302158,-4.172295,-4.867032,-4.571247,-9.115546,4.915833],[1.985273,2.465090,-4.315630,-4.047266,-9.068063,8.041305,8.405458,-6.510071,-5.622219,3.823729,-0.218363,0.889235,2.014185,4.916522,4.709124],[-7.431736,2.323746,8.897683,0.493302,8.770348,5.954494,5.077583,6.514826,-4.397645,-9.690878,-1.004611,6.875463,6.620694,0.811809,4.407651],[9.699028,7.476538,1.193541,8.944740,5.984466,-0.992032,3.126021,1.498363,4.887544,0.439469,8.667079,4.663292,3.607227,-9.897455,7.713712],[9.138669,5.421132,9.256170,-2.545809,-9.341082,8.454205,-6.061398,-2.548453,-1.036495,4.043073,6.664013,8.117738,-7.482365,-9.294601,-3.537729],[-4.103755,-5.206946,-5.932970,-0.505599,-2.019418,-1.193479,5.922855,3.625281,9.956312,3.079093,1.994200,3.001416,9.337835,6.510138,-5.401646],[8.038697,-9.276127,5.255222,4.859677,5.313489,-5.171131,-6.440820,-0.486522,7.594502,5.829103,9.498227,-1.823082,9.109635,-4.639265,0.860668],[-3.186514,2.144188,-0.519769,-2.955629,-1.586570,-3.716191,0.597244,-1.016659,-3.906613,3.039752,-1.903028,-4.409644,-2.153556,7.470678,-9.822042],[1.240675,7.976457,0.195978,5.077665,-6.217768,8.524720,-7.099091,4.003310,5.812708,6.775497,9.791134,4.687330,-0.391080,6.561520,-1.706835],[-3.974561,3.871747,-7.176999,3.080605,-1.877609,0.530532,-3.773953,-2.193681,-5.675441,7.550009,7.154195,2.463742,-0.318226,-0.265383,4.951653],[-3.781180,-3.354514,-9.467156,-1.384467,0.415690,1.539418,7.417219,-0.002110,6.276504,5.739587,-3.384724,7.872674,1.396125,9.073568,1.114207],[-9.463450,-1.939625,5.154343,1.337365,4.237476,-6.536740,8.003480,-3.040461,-6.259248,-2.954814,2.262918,-8.224587,-9.267980,-0.209416,4.115727],[1.061027,5.200128,-0.599107,-5.982088,7.877178,-5.049483,-3.430452,8.238339,-8.664262,-7.014684,8.881603,7.766872,-0.988713,5.530800,-2.669365],[-4.554531,-9.738878,7.439308,7.935259,-9.203515,2.945239,-1.203290,-2.790983,6.605396,1.030410,5.230322,6.969553,-2.115879,-8.853692,-2.222066],[-9.308783,-1.646222,7.701886,-1.252163,8.417585,0.416588,1.473149,-5.318504,8.695278,-5.071931,1.536442,2.373969,7.012284,-8.269198,3.937513],[-1.181130,-9.545811,-1.646708,-8.134045,-1.654177,1.129857,0.436159,8.839042,-2.140568,2.892616,-0.875913,-0.792129,9.556145,7.781978,8.449135],[-9.882169,0.332576,9.873373,-4.152277,-7.934663,3.999487,-4.017251,-4.544483,0.386034,-5.154570,-3.838637,6.186890,-8.531321,-9.158758,5.081245],[-4.092308,6.622549,-5.311329,3.789140,-9.246170,3.031135,1.068666,-5.620495,0.656937,-2.436732,-7.865611,-4.885645,4.727672,-6.556286,9.986735],[-1.510253,-0.374054,7.034127,-8.890075,3.823529,-5.035723,-2.693272,4.560536,0.325531,-8.052882,-6.200880,-9.548894,3.468933,-7.950834,5.838193],[1.973282,0.057919,7.101651,-0.145950,-7.516046,7.446372,-4.021062,-7.783927,-8.164048,-9.055921,-6.549996,-3.364425,-0.250782,-4.445584,1.448955],[-1.442876,5.950135,-4.630967,-3.896523,-3.656939,0.399200,8.070109,-6.601984,2.217878,1.360162,7.822711,-8.180650,4.429058,0.338850,3.056084],[8.084592,0.292222,-7.086089,-7.338286,-9.802247,2.041521,-7.457889,8.820270,-5.029936,3.869482,8.162998,5.307039,-9.411770,-2.750041,8.668902],[1.419824,5.821364,4.730911,-1.948733,-7.670928,3.045851,-7.467604,-3.651075,-6.628186,-8.174126,-4.008953,-4.431895,-9.777629,-3.036374,0.222631],[-8.553624,4.403909,8.286543,9.013355,-9.913210,1.168715,8.586864,2.871939,8.727382,9.886471,9.012491,0.059532,2.576412,5.864646,-0.992249],[8.699379,5.704223,-1.488421,-9.533286,-3.927419,4.606631,-7.654815,-8.917958,-9.720524,9.530426,2.294136,-8.995606,-3.563937,-7.760190,0.707194],[-6.559986,-1.587639,3.160679,5.536968,-1.768613,-0.852277,6.996504,6.499198,-8.071219,7.360972,3.439766,7.037562,-5.728117,3.598102,5.428199],[5.508521,-3.995589,9.199019,4.861694,0.338220,-5.347113,3.414903,-3.296861,6.682230,1.489089,-4.337319,-8.741827,-0.113302,2.714678,3.773842],[-9.055555,4.823915,-3.314092,8.167787,4.545708,-8.345783,-9.998484,9.054949,-1.802405,-1.635649,6.799226,-1.328591,-2.561671,-9.514739,-9.729414],[-0.577025,3.311898,9.178147,-2.184598,7.478139,9.289925,5.603889,7.782868,-7.445357,-0.577436,1.925707,0.514096,4.307507,-1.660622,-9.547167],[1.140678,-8.410002,-6.233514,7.679571,-3.474377,-0.376143,-7.741564,5.880212,-2.722693,9.441595,-0.016692,-5.076677,-2.459872,5.231278,-8.779030],[4.680048,-5.853949,-3.177151,-9.333862,7.133335,-8.611751,-5.672073,-9.708396,-7.549294,-0.361216,4.671697,8.613478,-5.967419,8.691328,-1.530270],[7.665290,9.973102,1.469213,-3.236104,1.851864,-6.282497,4.290150,-3.566514,4.830523,-2.808004,-3.984901,-0.525730,-4.934363,3.710229,8.772200],[3.837971,-5.495117,-1.180969,-2.931646,6.369391,8.419878,9.600339,-7.610934,-0.593836,-0.641969,2.578719,-6.282633,-1.577813,4.539678,-6.852472],[-1.426204,2.742824,-7.924251,-9.167592,4.387037,7.043391,-4.032041,9.414035,-0.906964,-4.173574,8.989014,-8.892539,0.302812,-2.081508,-7.756749],[6.398862,-1.128259,5.644857,7.610983,4.137485,8.604045,2.413161,9.449614,5.024832,-0.679687,-4.509766,9.448922,2.529315,-8.181455,3.772200],[-7.872495,7.147872,-1.811014,7.463356,-8.435947,-4.509404,2.263725,4.809881,-2.007862,1.553877,-5.863167,-8.241983,-2.486087,0.220713,6.000249],[1.608424,3.806007,-2.532807,-0.063917,3.546776,-0.357415,-5.247968,8.375537,-0.423648,-7.281772,-6.722946,-2.343837,3.613143,-8.950592,3.512578],[2.319544,8.557851,8.735955,-3.317321,-4.699211,-2.169958,1.315442,-9.528814,3.618153,2.563922,-4.122698,-0.940021,-3.625082,6.861299,-7.149075],[7.813914,-3.006820,4.978979,-4.551092,0.427113,6.936205,-6.234570,-6.025825,-7.990153,3.026531,-4.929796,7.070745,-0.395830,-6.421797,9.384102],[-3.018208,-3.329521,2.218453,-1.761282,-3.647688,-3.308121,-5.283279,-0.681478,-7.088828,-4.985709,-1.016133,0.931588,0.706149,-3.379770,-5.326823],[5.562566,-2.895238,8.419691,2.043892,1.958225,0.024582,0.694480,-0.772621,-8.023460,-2.332164,9.043783,3.419562,2.056130,-7.485495,-8.516311],[0.201561,-4.654486,-7.071561,6.308386,5.951794,4.081236,0.411434,-5.291716,-5.833945,-4.226285,5.617225,-6.774989,-2.911431,-3.885833,7.341617],[0.124170,-2.030441,-2.113403,2.727399,-8.082639,-3.175798,6.682510,-9.968368,-9.124943,2.176109,-6.624097,-1.579610,7.471915,-1.577748,2.843670],[2.711666,-7.438613,-5.590251,-2.069846,-1.113319,2.315100,-9.749069,-8.459965,-8.518171,0.604771,2.794131,2.120709,-6.642318,4.990574,-3.219763],[-5.051253,1.707738,2.148288,9.245984,-6.719274,-6.458984,5.784439,-1.457463,6.250433,-9.349520,-5.163891,-2.855931,9.701191,1.331084,2.273028],[0.345180,5.346873,-7.679842,9.013704,-7.777933,-2.332575,9.669442,1.404915,9.990618,-8.823080,1.040453,-6.860922,-7.298270,6.417291,-1.640111],[7.122896,-1.151794,-2.899035,7.288495,3.185953,7.317303,-1.188379,3.841207,6.117718,9.153663,-6.181903,-0.062029,-2.894239,-0.740794,-5.108268],[5.574015,-5.668967,-4.384051,-4.259924,-3.278323,3.507659,3.240396,-0.344355,4.702703,-0.160931,-5.529558,-0.626060,3.080141,9.816404,-5.276624],[-9.358854,-9.911411,7.174322,4.575500,-9.641900,0.647967,-2.165109,-2.966340,9.220034,-8.923213,-7.083491,-6.614339,2.984389,1.452329,2.636553],[1.983731,8.832046,4.182494,-5.142227,6.424222,-7.197690,1.725654,2.500933,-5.583982,9.225083,-6.778497,7.368822,-4.192884,-8.145476,5.684461],[2.972674,7.498572,-5.939057,-9.523949,-2.583576,-5.759519,-3.507190,9.125087,4.280738,3.515644,-5.066833,-1.427511,-6.228117,-0.269220,-1.712383],[0.779906,-4.732712,7.840128,7.280733,-7.596136,2.178650,-3.343853,-0.162608,3.619962,4.424914,-6.612330,9.172274,4.262917,-8.926918,-7.401834],[-2.002103,-8.842003,6.901452,6.584484,7.337363,-1.951649,-1.850696,0.404578,-6.268878,-7.515690,4.216447,4.355402,8.070234,-8.647444,-9.991604],[5.874572,-9.762023,-6.605703,3.194809,-3.770292,4.276985,5.213097,-0.634321,-7.747286,2.388675,-6.449564,7.351038,4.315228,5.124557,-9.232125],[6.510416,-5.434814,-3.376651,5.704247,-5.385101,-4.512541,-2.672826,-3.777648,-8.376274,3.066653,5.273384,-8.801529,0.765571,-0.096735,-0.859883],[-6.958608,-4.090395,2.498173,4.010210,-2.135186,0.322953,1.463728,-7.412975,-8.774500,-2.067447,-8.439102,2.821446,3.622348,0.550003,9.026441],[-1.129444,2.015504,-4.366198,1.592320,6.225482,-4.602291,2.945127,-1.784765,8.425125,-5.509837,-6.784377,7.733677,-5.275725,-5.974204,-9.566178],[3.914034,7.901354,9.307070,5.483475,-3.364164,-7.404105,9.236661,-0.918992,1.713911,-5.295791,-6.044386,7.689168,1.084930,-8.257709,8.385680],[3.463829,6.171372,1.710212,5.295195,-4.090055,1.732777,-9.831413,-4.556051,-9.319809,-0.753931,9.704267,1.249350,-7.882787,-0.919229,-5.508548],[-5.831026,-8.694155,-8.173433,-2.169916,9.172698,1.550597,-4.341256,0.013620,6.885851,-0.998195,2.263358,-6.283003,-8.131471,3.789395,4.842532],[-2.654156,6.828848,9.178671,-0.955065,1.795243,-9.602370,-7.162932,-6.478011,1.402550,4.047804,6.571540,-4.075054,4.470625,9.764842,9.705459],[-3.571216,-5.384618,5.792748,-8.016544,7.339141,0.923677,-9.412885,-3.089038,2.636675,-8.720318,-4.865272,7.668790,1.406736,3.068134,4.353523],[4.306553,1.939638,-5.807472,-9.212178,-4.789013,-7.540078,9.534257,-1.793059,-9.996352,-4.836892,-0.432252,-3.196068,4.373424,5.602765,-0.217621],[2.801602,-2.884318,9.694133,0.151376,9.111711,-2.020593,9.455137,6.511116,9.081284,-2.703852,-7.641297,-9.462427,-1.210607,1.952721,1.570704],[1.361536,6.412873,1.282960,-6.146212,-4.367077,-2.365879,0.117193,2.255588,1.253217,-3.995886,-4.475037,4.850902,-2.082765,-6.015463,3.972120]], dtype = "float64")#candidate|3949|(70, 15)|const|float64
const_3950 = relay.const([-8,1,9,1,-10,-7,8,4,1,-4,-1,3,7,-2,-3,-8,-1,10,-2,-10,-4,7,-6,-7,6,-3,10,2,7,8,3,1,-6,-6,2,1,2,7,-6,6,-6,10,-7,3,8,-4,-7,7,-5,-2,-8,2,10,9,-2,1,-3,3,-3,6,8,-4,-2,-10,3,-4,4,2,-5,-3,3,-6,5,8,6,9,3,-10,-4,4,2,-10,-5,-2,1,-9,9,3,-3,-2,-7,4,6,-9,-6,-10,2,-7,-10,7,-6,8,-10,-1,-5,5,-8,4,-4,-6,5,-3,6,3,-2,-1,-7,-6,-1,-3,2,8,6,5,4,-4,-7,-7,-6,-3,1,9,-3,6,-3,-8,-4,4,10,-1,1,5,-10,-5,1,7,9,9,-10,-6,3,-8,2,-8,-3,7,2,-4,-2,-1,6,-6,-5,-9,-1,7,-10,-2,9,5,7,-6,3,3,8,10,-3,10,-1,-2,3,8,-4,-8,-8,-5,-6,-6,-10,6,-3,3,-3,4,2,-8,-7,10,5,-4,-2,10,9,-9,-4,-10,-1,5,-6,8,6,6,-10,-5,-6,-10,8,-8,-5,-10,2,-8,-1,-5,-3,-8,8,-2,-10,-5,-8,7,-4,-4,2,8,4,-6,-10,-3,-5,3,6,-4,-4,5,2,7,8,5,-7,-5,2,5,4,6,-10,-3,-4,-3,5,-10,1,-5,1,1,4,9,9,7,-6,1,1,4,-2,-4,6,-6,-1,8,-10,2,-6,1,6,7,2,-10], dtype = "int16")#candidate|3950|(288,)|const|int16
call_3948 = relay.TupleGetItem(func_3461_call(relay.reshape(const_3949.astype('float64'), [1050,]), relay.reshape(const_3950.astype('int16'), [288,]), relay.reshape(const_3945.astype('uint8'), [108,]), ), 6)
call_3951 = relay.TupleGetItem(func_3466_call(relay.reshape(const_3949.astype('float64'), [1050,]), relay.reshape(const_3950.astype('int16'), [288,]), relay.reshape(const_3945.astype('uint8'), [108,]), ), 6)
output = relay.Tuple([call_3894,call_3907,call_3914,call_3918,call_3933,var_3934,uop_3936,call_3942,const_3943,const_3944,const_3945,call_3948,const_3949,const_3950,])
output2 = relay.Tuple([call_3895,call_3909,call_3915,call_3919,call_3935,var_3934,uop_3936,call_3946,const_3943,const_3944,const_3945,call_3951,const_3949,const_3950,])
func_3965 = relay.Function([var_3934,], output)
mod['func_3965'] = func_3965
mod = relay.transform.InferType()(mod)
var_3966 = relay.var("var_3966", dtype = "float64", shape = (216,))#candidate|3966|(216,)|var|float64
output = func_3965(var_3966)
func_3967 = relay.Function([var_3966], output)
mutated_mod['func_3967'] = func_3967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3353_call = mod.get_global_var('func_3353')
func_3354_call = mutated_mod.get_global_var('func_3354')
call_4012 = relay.TupleGetItem(func_3353_call(), 0)
call_4013 = relay.TupleGetItem(func_3354_call(), 0)
func_2518_call = mod.get_global_var('func_2518')
func_2520_call = mutated_mod.get_global_var('func_2520')
call_4032 = relay.TupleGetItem(func_2518_call(), 0)
call_4033 = relay.TupleGetItem(func_2520_call(), 0)
output = relay.Tuple([call_4012,call_4032,])
output2 = relay.Tuple([call_4013,call_4033,])
func_4052 = relay.Function([], output)
mod['func_4052'] = func_4052
mod = relay.transform.InferType()(mod)
mutated_mod['func_4052'] = func_4052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4052_call = mutated_mod.get_global_var('func_4052')
call_4053 = func_4052_call()
output = call_4053
func_4054 = relay.Function([], output)
mutated_mod['func_4054'] = func_4054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3082_call = mod.get_global_var('func_3082')
func_3084_call = mutated_mod.get_global_var('func_3084')
call_4108 = relay.TupleGetItem(func_3082_call(), 0)
call_4109 = relay.TupleGetItem(func_3084_call(), 0)
func_2570_call = mod.get_global_var('func_2570')
func_2571_call = mutated_mod.get_global_var('func_2571')
call_4117 = relay.TupleGetItem(func_2570_call(), 1)
call_4118 = relay.TupleGetItem(func_2571_call(), 1)
func_3178_call = mod.get_global_var('func_3178')
func_3179_call = mutated_mod.get_global_var('func_3179')
call_4119 = relay.TupleGetItem(func_3178_call(), 0)
call_4120 = relay.TupleGetItem(func_3179_call(), 0)
func_3106_call = mod.get_global_var('func_3106')
func_3108_call = mutated_mod.get_global_var('func_3108')
call_4131 = func_3106_call()
call_4132 = func_3106_call()
output = relay.Tuple([call_4108,call_4117,call_4119,call_4131,])
output2 = relay.Tuple([call_4109,call_4118,call_4120,call_4132,])
func_4140 = relay.Function([], output)
mod['func_4140'] = func_4140
mod = relay.transform.InferType()(mod)
output = func_4140()
func_4141 = relay.Function([], output)
mutated_mod['func_4141'] = func_4141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3487_call = mod.get_global_var('func_3487')
func_3489_call = mutated_mod.get_global_var('func_3489')
call_4270 = relay.TupleGetItem(func_3487_call(), 0)
call_4271 = relay.TupleGetItem(func_3489_call(), 0)
output = call_4270
output2 = call_4271
func_4281 = relay.Function([], output)
mod['func_4281'] = func_4281
mod = relay.transform.InferType()(mod)
output = func_4281()
func_4282 = relay.Function([], output)
mutated_mod['func_4282'] = func_4282
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4317 = relay.const([[[True,True,False,False,True,False,False,False],[False,False,False,True,True,False,False,True],[False,True,True,True,True,True,False,True],[False,False,True,True,False,False,False,True],[True,False,True,False,False,True,True,True]],[[False,True,False,True,False,False,False,False],[True,True,True,False,False,False,False,False],[False,True,True,True,True,True,False,False],[False,False,True,False,True,False,True,True],[True,True,False,True,True,False,False,False]],[[True,True,True,True,True,True,True,False],[False,True,True,True,False,True,True,False],[True,False,True,True,False,False,False,False],[False,True,True,True,True,True,False,True],[True,True,False,False,False,False,False,False]],[[True,True,True,True,True,False,False,False],[True,True,True,True,True,False,True,True],[True,True,True,False,False,True,True,True],[False,False,False,False,False,False,False,True],[False,True,False,True,True,False,True,False]],[[True,True,False,True,True,True,False,False],[False,True,False,True,False,False,False,False],[False,False,False,False,True,False,True,True],[True,True,False,True,False,True,True,True],[False,True,False,True,True,True,True,True]],[[False,False,False,True,False,True,True,False],[True,False,False,False,False,True,True,False],[False,True,True,False,True,False,False,True],[False,False,True,True,True,False,False,False],[False,True,True,False,False,False,False,True]],[[False,False,False,True,True,True,True,False],[True,False,False,False,False,False,True,False],[True,False,True,False,True,False,False,True],[True,True,False,True,False,False,False,False],[True,False,True,False,False,False,False,True]],[[False,True,True,True,True,False,True,False],[True,True,True,False,True,True,True,False],[True,True,True,True,False,True,True,True],[False,True,True,False,True,False,True,False],[True,False,True,False,False,False,True,True]],[[True,False,True,False,True,True,False,False],[False,True,True,False,True,True,True,True],[False,True,True,True,True,False,True,False],[False,False,False,False,True,True,False,False],[True,True,True,True,False,True,True,True]],[[True,True,True,False,False,True,True,False],[False,False,True,True,False,True,True,False],[True,True,False,False,True,False,True,False],[False,False,True,False,True,True,True,False],[False,True,False,False,False,True,False,False]],[[True,True,True,True,False,False,True,False],[True,False,False,False,False,True,True,False],[True,False,True,True,True,False,True,True],[True,False,True,True,True,True,True,True],[True,False,False,True,False,False,True,False]],[[False,False,False,False,True,True,True,True],[False,False,False,True,False,True,True,False],[True,False,True,True,False,True,False,True],[True,False,False,False,False,False,False,False],[False,False,True,True,False,False,False,False]],[[False,False,True,False,False,False,False,True],[True,False,False,True,True,False,False,False],[True,False,False,True,False,False,False,False],[True,True,False,True,True,False,True,True],[True,False,True,True,True,False,False,False]],[[False,True,True,True,True,True,True,False],[True,False,False,False,False,False,False,True],[True,False,False,False,True,True,True,False],[False,False,True,True,False,True,True,False],[False,False,True,False,True,True,False,False]],[[True,False,False,True,False,True,True,True],[True,True,True,False,True,False,False,True],[True,True,False,True,True,True,False,True],[True,True,True,False,False,False,False,True],[False,True,True,True,False,False,False,True]],[[True,False,False,False,False,False,True,True],[False,True,True,True,False,True,False,True],[False,False,True,True,False,False,False,False],[True,True,True,True,True,False,False,True],[False,False,True,False,True,True,False,True]]], dtype = "bool")#candidate|4317|(16, 5, 8)|const|bool
const_4318 = relay.const([[[True,False,True,False,False,False,False,False],[False,True,False,False,False,True,True,True],[False,False,True,False,False,False,False,True],[True,True,False,False,True,True,True,False],[True,False,False,True,False,False,False,False]],[[False,False,False,False,True,True,True,False],[True,False,False,False,False,True,True,False],[False,True,False,True,False,True,True,True],[True,True,False,False,True,False,False,True],[True,True,True,False,False,True,False,False]],[[True,True,False,False,False,True,False,False],[False,False,True,False,False,False,True,True],[True,True,True,False,False,False,False,True],[True,True,True,True,False,False,True,False],[True,True,False,True,False,False,True,False]],[[False,False,False,False,False,True,False,True],[True,True,True,True,True,True,False,False],[True,True,False,True,True,True,True,False],[True,True,True,True,True,False,False,False],[False,False,False,False,False,False,True,True]],[[False,True,False,True,False,False,False,True],[True,False,True,True,True,False,True,False],[False,True,False,True,True,False,True,False],[False,False,False,False,False,False,True,False],[True,True,False,True,True,False,True,True]],[[False,False,False,True,False,True,False,False],[False,False,False,False,False,True,False,False],[True,False,True,False,False,False,False,True],[False,False,True,True,False,False,False,False],[False,False,False,False,False,False,True,False]],[[False,True,False,False,False,False,False,False],[True,True,False,True,False,False,True,False],[True,False,True,True,False,False,False,False],[False,False,False,False,False,True,True,False],[False,True,False,True,False,False,True,True]],[[False,True,False,False,True,True,False,False],[True,True,False,True,True,False,True,False],[False,False,False,False,True,True,False,False],[True,False,True,True,False,False,False,False],[True,False,False,False,False,False,True,True]],[[False,True,True,True,True,False,True,True],[False,False,True,False,True,True,False,False],[True,True,True,True,True,True,False,False],[False,False,False,False,True,True,True,True],[False,False,False,True,True,False,False,True]],[[False,True,True,True,False,True,False,True],[False,True,True,True,True,True,True,True],[True,False,True,False,True,False,True,False],[True,False,True,False,False,False,True,False],[True,True,True,False,False,True,True,True]],[[True,False,False,False,True,False,True,True],[False,False,True,True,False,True,True,True],[True,True,True,True,True,True,True,False],[False,False,False,False,False,False,True,True],[False,False,True,False,False,False,True,False]],[[False,False,True,False,True,True,False,False],[False,True,True,True,False,False,True,False],[True,False,True,True,False,False,False,False],[False,True,False,False,True,True,False,True],[False,False,True,True,True,True,False,True]],[[True,True,False,True,False,True,False,True],[True,True,False,True,True,False,False,False],[True,False,False,False,False,True,True,False],[True,False,True,False,False,True,True,True],[True,True,False,True,False,False,False,False]],[[True,False,True,True,False,True,True,True],[False,True,True,False,False,False,False,True],[False,True,True,False,True,False,True,False],[True,False,True,False,False,True,False,False],[True,True,True,True,True,False,False,True]],[[True,True,True,False,True,True,True,True],[False,True,False,True,True,True,True,True],[True,False,True,False,True,True,False,False],[False,True,True,True,True,True,False,False],[False,True,False,True,False,False,True,True]],[[True,True,False,False,False,False,True,False],[False,False,False,False,True,False,False,False],[True,False,True,False,True,False,False,False],[True,True,True,False,True,False,True,False],[True,True,False,False,True,False,False,False]]], dtype = "bool")#candidate|4318|(16, 5, 8)|const|bool
bop_4319 = relay.logical_or(const_4317.astype('bool'), relay.reshape(const_4318.astype('bool'), relay.shape_of(const_4317))) # shape=(16, 5, 8)
func_2765_call = mod.get_global_var('func_2765')
func_2767_call = mutated_mod.get_global_var('func_2767')
call_4322 = func_2765_call()
call_4323 = func_2765_call()
func_3178_call = mod.get_global_var('func_3178')
func_3179_call = mutated_mod.get_global_var('func_3179')
call_4326 = relay.TupleGetItem(func_3178_call(), 0)
call_4327 = relay.TupleGetItem(func_3179_call(), 0)
output = relay.Tuple([bop_4319,call_4322,call_4326,])
output2 = relay.Tuple([bop_4319,call_4323,call_4327,])
func_4334 = relay.Function([], output)
mod['func_4334'] = func_4334
mod = relay.transform.InferType()(mod)
mutated_mod['func_4334'] = func_4334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4334_call = mutated_mod.get_global_var('func_4334')
call_4335 = func_4334_call()
output = call_4335
func_4336 = relay.Function([], output)
mutated_mod['func_4336'] = func_4336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2969_call = mod.get_global_var('func_2969')
func_2970_call = mutated_mod.get_global_var('func_2970')
call_4395 = func_2969_call()
call_4396 = func_2969_call()
func_2570_call = mod.get_global_var('func_2570')
func_2571_call = mutated_mod.get_global_var('func_2571')
call_4436 = relay.TupleGetItem(func_2570_call(), 0)
call_4437 = relay.TupleGetItem(func_2571_call(), 0)
func_2969_call = mod.get_global_var('func_2969')
func_2970_call = mutated_mod.get_global_var('func_2970')
call_4445 = func_2969_call()
call_4446 = func_2969_call()
output = relay.Tuple([call_4395,call_4436,call_4445,])
output2 = relay.Tuple([call_4396,call_4437,call_4446,])
func_4457 = relay.Function([], output)
mod['func_4457'] = func_4457
mod = relay.transform.InferType()(mod)
mutated_mod['func_4457'] = func_4457
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4457_call = mutated_mod.get_global_var('func_4457')
call_4458 = func_4457_call()
output = call_4458
func_4459 = relay.Function([], output)
mutated_mod['func_4459'] = func_4459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4281_call = mod.get_global_var('func_4281')
func_4282_call = mutated_mod.get_global_var('func_4282')
call_4468 = func_4281_call()
call_4469 = func_4281_call()
output = call_4468
output2 = call_4469
func_4471 = relay.Function([], output)
mod['func_4471'] = func_4471
mod = relay.transform.InferType()(mod)
output = func_4471()
func_4472 = relay.Function([], output)
mutated_mod['func_4472'] = func_4472
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3775_call = mod.get_global_var('func_3775')
func_3777_call = mutated_mod.get_global_var('func_3777')
call_4497 = relay.TupleGetItem(func_3775_call(), 0)
call_4498 = relay.TupleGetItem(func_3777_call(), 0)
output = call_4497
output2 = call_4498
func_4499 = relay.Function([], output)
mod['func_4499'] = func_4499
mod = relay.transform.InferType()(mod)
mutated_mod['func_4499'] = func_4499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4499_call = mutated_mod.get_global_var('func_4499')
call_4500 = func_4499_call()
output = call_4500
func_4501 = relay.Function([], output)
mutated_mod['func_4501'] = func_4501
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2528_call = mod.get_global_var('func_2528')
func_2529_call = mutated_mod.get_global_var('func_2529')
call_4574 = relay.TupleGetItem(func_2528_call(), 0)
call_4575 = relay.TupleGetItem(func_2529_call(), 0)
func_1707_call = mod.get_global_var('func_1707')
func_1714_call = mutated_mod.get_global_var('func_1714')
const_4579 = relay.const([6,9,-7,-8,-6,-2,-3,-1,-5,3,-8,-7,-5,9,4,6,-7,-6,7,-1,8,-10,-2,1,1,-3,-7,2,-9,2,2,-3,-6,5,-4,8,10,1,8,-1,-4,-8,5,6,10,9,-9,2,5,9,-4,9,5,-5,-2,4,3,10,1,-3,-4,-2,9,8,-1,-1,-4,-8,2,3,-2,-3,-8,-4,-9,-9,-1,7,5,2,-2,1,-5,6,2,3,-8,-10,9,5,-3,10,5,2,3,-6,-8,1,-3,3,8,-9,2,3,5,9,2,2,9,7,-9,-6,-9,-4,-6,10,-3,-8,-10,6,9,-3,-7,8,10,-5,-10,10,10,4,1,9,4,-10,-8,-10,-4,-8,2,4,-3,1,-3,-5,-4,-10,4,10,-7,-2,9,-4,7,-3,-7,-10,-9,8,-3,5,-3,-4,-6,-4,-3,10,10,-4,-5,7,7,4,10,7,4,-3,-7,-7,9,6,10,5,-9,7,9,5,9,9,-3,5,8,-8,4,10,7,-7,-5,4,-3,-7,3,6,5,-5,4,6,7,9,-7,3,8,-10,-2,4,-5,8,6,4,-1,-10,9,7,9,-5,6,2,-10,4,9,7,-2,4,9,9,-6,-3,6,1,7,-4,8,6,10,-9,-9,-3,-3,8,4,10,-8,-9,4,-2,7,-3,-1,2,8,-10,-10,-5,-1,-5,-2,-7,9,-7,-7,5,4,-1,-8,8,-6,10,-3,-1,9,9,10,-4,-5,3,9,-8,-7,-1], dtype = "int16")#candidate|4579|(288,)|const|int16
const_4580 = relay.const(8, dtype = "uint8")#candidate|4580|()|const|uint8
var_4581 = relay.var("var_4581", dtype = "uint8", shape = (108,))#candidate|4581|(108,)|var|uint8
call_4578 = relay.TupleGetItem(func_1707_call(relay.reshape(const_4579.astype('int16'), [6, 4, 12]), relay.reshape(const_4579.astype('int16'), [6, 4, 12]), relay.reshape(const_4580.astype('uint8'), []), relay.reshape(var_4581.astype('uint8'), [6, 18]), relay.reshape(var_4581.astype('uint8'), [3, 36]), ), 0)
call_4582 = relay.TupleGetItem(func_1714_call(relay.reshape(const_4579.astype('int16'), [6, 4, 12]), relay.reshape(const_4579.astype('int16'), [6, 4, 12]), relay.reshape(const_4580.astype('uint8'), []), relay.reshape(var_4581.astype('uint8'), [6, 18]), relay.reshape(var_4581.astype('uint8'), [3, 36]), ), 0)
func_2654_call = mod.get_global_var('func_2654')
func_2657_call = mutated_mod.get_global_var('func_2657')
const_4584 = relay.const([6.830360,-8.678457,-2.995765,-0.535859,-7.999318,5.142108,2.196424,5.465140,-4.873305,4.958574,6.259589,-1.598291,0.083310,-4.034406,0.829968,2.234031,8.381390,-8.396159,-1.632195,-7.545664,-2.163870,4.189364,-5.132357,2.882637,2.599157,-3.465413,-0.293053,-1.179856,1.688262,5.867954,-6.406837,8.638804,-2.454836,3.480163,0.930432,9.726963,-0.101422,9.198314,2.289612,9.985208,-8.336407,-9.808680,0.340262,-2.006039,2.328920,6.804248,3.283060,-2.124456,-6.271532,-4.615625,0.717651,7.707911,1.439815,-2.341059,2.877152,5.122440,4.998283,1.178435,6.237894,2.660250,5.857347,-4.680659,-6.238269,-6.759663,-8.563899,-3.938556,-8.399627,7.458559,-9.254167,7.563533,-2.804222,2.627357,-7.627111,-7.942635,4.054534,-8.544534,-4.107630,3.553872,1.994571,-1.986918,-3.713680,6.311147,-3.385109,-5.065381,-7.347872,9.531640,4.941168,1.403310,6.281519,3.459009,8.792215,2.997820,-1.505718,-3.074948,-3.674473,7.343553,0.433256,8.662580,-8.573391,8.231709,4.895884,2.910163,6.654615,-5.672733,-0.915037,0.898581,-1.477215,1.972400,8.279219,-3.873646,-0.606700,9.716630,6.864974,-5.284090,-6.002977,-2.817503,-1.034698,-7.966992,-9.430480,-7.070144,-8.946973,5.731623,-0.611318,7.933912,-8.269378,1.075086,-5.566272,7.801121,1.573992,9.269737,4.547635,-4.414466,5.039669,8.420977,3.481725,-3.556188,-3.020764,-9.325128,-6.627457,-4.736265,-8.746849,-0.081471,-2.572031,-8.015725,2.434324,-6.082588,0.201395,-7.135791,3.252620,6.721602,6.657874,7.414369,9.281271,-5.913819,4.140724,-9.475444,-0.615465,-4.575363,-1.094268,-9.770268,-1.716067,-6.146660,6.990495,-3.155609,3.673005,-1.394144,4.744751,-6.630799,6.297423,3.914524,7.839250,-0.666097,-3.705176,7.459494,9.150992,-8.705464,-3.920240,-4.541528,5.909255,-2.100178,-1.002588,5.315864,-9.468950,-9.534507,-4.007716,4.386022,6.882935,0.180108,-4.178999,3.752110,-9.594643,-8.281704,-4.468424,8.085537,9.780459,-9.237958,-9.627654,-7.350803,0.842066,-9.557005,-8.593265,-1.758016,-8.831889,2.521324,-5.649305,-9.076303,-0.857918,9.578308,7.213988,-1.455998,-8.646938,-7.675805,-1.054778,-7.321262,2.764121,9.827916,-9.390452,-0.577072,5.673119,8.945430,-1.756919,-4.371779,-9.178115,1.099718,-5.648349,5.076396,5.307367,7.995573,-7.212747,1.826023,8.999869,4.742966,-8.149872,-1.603926,9.831858,9.948272,9.312163,-1.297789,7.902402,-4.052151,7.294645,4.490668,1.969707,-5.326093,-2.634284,-7.056988,-3.826687,3.543433,3.809323,-8.602221,2.545052,-5.098027,8.719204,8.716238,-9.967252,3.194184,9.954577,-8.820866,3.820424,-8.407609,1.312887,5.263721,-2.451212,-0.565116,-8.974788,-4.173506,8.691087,6.439094,4.647742,4.482787,-6.635588,0.255591,1.169074,-1.485817,-1.204255,-9.347143,5.392008,2.153335,-0.908709,4.056565,-2.324292,3.002273,-3.905539,-5.353859,7.477862,-9.867402,-7.421100,9.423508,7.889080,8.763094,-2.303681,2.708589,8.967849,4.352541,3.184008,9.266551,-1.461851,7.865771,4.865470,-9.716170,0.782399,-1.211182,-0.667893,-3.482520,7.508952,5.089109,2.866818,-1.778906,4.048328,3.796516,-0.443456,-7.899956,4.618460,-2.350391,7.236609,6.200833,8.534386,4.941865,3.949248,7.036624,3.759711,-2.678078,-4.900991,3.507937,-2.769860,-6.428660,5.081898,6.160375,-0.186411,8.585919,-7.116983,-5.546309,-1.669064,6.112113,3.384774,2.078669,2.410604,-3.198447,-8.377904,2.203161,-3.784372,6.022489,-7.114126,-0.797343,-2.783698,-4.504002,-9.644234,-8.021668,-0.738999,-5.108267,4.177421,-5.508335,4.810596,-0.807919,3.752198,-2.009697,9.674180,0.420813,-2.104409,-8.271444,-2.323800,8.413973,4.940896,9.539404,2.111194,-9.123981,7.455776,7.055568,9.038460,-7.689673,1.529812,-6.963399,6.966071,-9.616082,5.619777,-9.360145,8.800868,-5.438521,-9.398588,0.689571,4.660244,-0.712565,-7.413510,0.791963,5.393844,-7.278222,-1.752519,2.958028,5.996830,2.306515,-6.823233,-5.876977,2.878703,-7.368804,-8.050151,7.972875,2.646203,8.595878,7.466808,0.187777,-4.656239,9.520989,-0.499812,-4.398338,-9.319100,-2.665808,-5.864630,-8.766889,2.125614,2.722272,-7.959965,1.061239,-7.996791,-0.232854,9.663364,-1.803463,9.335857,-9.500075,-3.271278,2.719455,-2.798387,5.234991,-0.484954,-5.973490,-2.987591,-6.280458,-1.723614,8.879709,-9.085547,-7.418616,3.708543,5.346199,-5.817345,8.370201,2.675483,6.905866,-5.730066,-8.776756,7.598607,5.216737,-5.472523,-3.244306,2.064660,7.798469,4.634151,-4.407211,-0.983980,-6.968003], dtype = "float64")#candidate|4584|(448,)|const|float64
call_4583 = relay.TupleGetItem(func_2654_call(relay.reshape(const_4584.astype('float64'), [14, 2, 16])), 0)
call_4585 = relay.TupleGetItem(func_2657_call(relay.reshape(const_4584.astype('float64'), [14, 2, 16])), 0)
output = relay.Tuple([call_4574,call_4578,const_4579,const_4580,var_4581,call_4583,const_4584,])
output2 = relay.Tuple([call_4575,call_4582,const_4579,const_4580,var_4581,call_4585,const_4584,])
func_4602 = relay.Function([var_4581,], output)
mod['func_4602'] = func_4602
mod = relay.transform.InferType()(mod)
var_4603 = relay.var("var_4603", dtype = "uint8", shape = (108,))#candidate|4603|(108,)|var|uint8
output = func_4602(var_4603)
func_4604 = relay.Function([var_4603], output)
mutated_mod['func_4604'] = func_4604
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4622 = relay.var("var_4622", dtype = "uint16", shape = (4, 7, 4))#candidate|4622|(4, 7, 4)|var|uint16
var_4623 = relay.var("var_4623", dtype = "uint16", shape = (4, 7, 4))#candidate|4623|(4, 7, 4)|var|uint16
bop_4624 = relay.subtract(var_4622.astype('uint16'), relay.reshape(var_4623.astype('uint16'), relay.shape_of(var_4622))) # shape=(4, 7, 4)
output = bop_4624
output2 = bop_4624
func_4635 = relay.Function([var_4622,var_4623,], output)
mod['func_4635'] = func_4635
mod = relay.transform.InferType()(mod)
mutated_mod['func_4635'] = func_4635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4635_call = mutated_mod.get_global_var('func_4635')
var_4637 = relay.var("var_4637", dtype = "uint16", shape = (4, 7, 4))#candidate|4637|(4, 7, 4)|var|uint16
var_4638 = relay.var("var_4638", dtype = "uint16", shape = (4, 7, 4))#candidate|4638|(4, 7, 4)|var|uint16
call_4636 = func_4635_call(var_4637,var_4638,)
output = call_4636
func_4639 = relay.Function([var_4637,var_4638,], output)
mutated_mod['func_4639'] = func_4639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2751_call = mod.get_global_var('func_2751')
func_2753_call = mutated_mod.get_global_var('func_2753')
call_4686 = relay.TupleGetItem(func_2751_call(), 0)
call_4687 = relay.TupleGetItem(func_2753_call(), 0)
output = relay.Tuple([call_4686,])
output2 = relay.Tuple([call_4687,])
func_4731 = relay.Function([], output)
mod['func_4731'] = func_4731
mod = relay.transform.InferType()(mod)
output = func_4731()
func_4732 = relay.Function([], output)
mutated_mod['func_4732'] = func_4732
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3294_call = mod.get_global_var('func_3294')
func_3295_call = mutated_mod.get_global_var('func_3295')
call_4794 = relay.TupleGetItem(func_3294_call(), 1)
call_4795 = relay.TupleGetItem(func_3295_call(), 1)
func_4471_call = mod.get_global_var('func_4471')
func_4472_call = mutated_mod.get_global_var('func_4472')
call_4844 = func_4471_call()
call_4845 = func_4471_call()
bop_4856 = relay.less_equal(call_4794.astype('bool'), relay.reshape(call_4844.astype('bool'), relay.shape_of(call_4794))) # shape=(13, 2, 6)
bop_4859 = relay.less_equal(call_4795.astype('bool'), relay.reshape(call_4845.astype('bool'), relay.shape_of(call_4795))) # shape=(13, 2, 6)
uop_4865 = relay.acosh(bop_4856.astype('float64')) # shape=(13, 2, 6)
uop_4867 = relay.acosh(bop_4859.astype('float64')) # shape=(13, 2, 6)
output = relay.Tuple([uop_4865,])
output2 = relay.Tuple([uop_4867,])
func_4879 = relay.Function([], output)
mod['func_4879'] = func_4879
mod = relay.transform.InferType()(mod)
mutated_mod['func_4879'] = func_4879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4879_call = mutated_mod.get_global_var('func_4879')
call_4880 = func_4879_call()
output = call_4880
func_4881 = relay.Function([], output)
mutated_mod['func_4881'] = func_4881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3082_call = mod.get_global_var('func_3082')
func_3084_call = mutated_mod.get_global_var('func_3084')
call_4905 = relay.TupleGetItem(func_3082_call(), 4)
call_4906 = relay.TupleGetItem(func_3084_call(), 4)
output = call_4905
output2 = call_4906
func_4907 = relay.Function([], output)
mod['func_4907'] = func_4907
mod = relay.transform.InferType()(mod)
mutated_mod['func_4907'] = func_4907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4907_call = mutated_mod.get_global_var('func_4907')
call_4908 = func_4907_call()
output = call_4908
func_4909 = relay.Function([], output)
mutated_mod['func_4909'] = func_4909
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4910 = relay.var("var_4910", dtype = "float32", shape = (11, 10, 15))#candidate|4910|(11, 10, 15)|var|float32
uop_4911 = relay.sinh(var_4910.astype('float32')) # shape=(11, 10, 15)
func_4731_call = mod.get_global_var('func_4731')
func_4732_call = mutated_mod.get_global_var('func_4732')
call_4926 = relay.TupleGetItem(func_4731_call(), 0)
call_4927 = relay.TupleGetItem(func_4732_call(), 0)
bop_4930 = relay.greater(uop_4911.astype('bool'), relay.reshape(var_4910.astype('bool'), relay.shape_of(uop_4911))) # shape=(11, 10, 15)
uop_4937 = relay.atanh(bop_4930.astype('float32')) # shape=(11, 10, 15)
func_4907_call = mod.get_global_var('func_4907')
func_4909_call = mutated_mod.get_global_var('func_4909')
call_4949 = func_4907_call()
call_4950 = func_4907_call()
func_4879_call = mod.get_global_var('func_4879')
func_4881_call = mutated_mod.get_global_var('func_4881')
call_4952 = relay.TupleGetItem(func_4879_call(), 0)
call_4953 = relay.TupleGetItem(func_4881_call(), 0)
output = relay.Tuple([call_4926,uop_4937,call_4949,call_4952,])
output2 = relay.Tuple([call_4927,uop_4937,call_4950,call_4953,])
func_4957 = relay.Function([var_4910,], output)
mod['func_4957'] = func_4957
mod = relay.transform.InferType()(mod)
var_4958 = relay.var("var_4958", dtype = "float32", shape = (11, 10, 15))#candidate|4958|(11, 10, 15)|var|float32
output = func_4957(var_4958)
func_4959 = relay.Function([var_4958], output)
mutated_mod['func_4959'] = func_4959
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5041 = relay.var("var_5041", dtype = "int8", shape = (4, 13, 16))#candidate|5041|(4, 13, 16)|var|int8
var_5042 = relay.var("var_5042", dtype = "int8", shape = (4, 13, 16))#candidate|5042|(4, 13, 16)|var|int8
bop_5043 = relay.multiply(var_5041.astype('int8'), relay.reshape(var_5042.astype('int8'), relay.shape_of(var_5041))) # shape=(4, 13, 16)
func_4052_call = mod.get_global_var('func_4052')
func_4054_call = mutated_mod.get_global_var('func_4054')
call_5053 = relay.TupleGetItem(func_4052_call(), 1)
call_5054 = relay.TupleGetItem(func_4054_call(), 1)
output = relay.Tuple([bop_5043,call_5053,])
output2 = relay.Tuple([bop_5043,call_5054,])
func_5085 = relay.Function([var_5041,var_5042,], output)
mod['func_5085'] = func_5085
mod = relay.transform.InferType()(mod)
mutated_mod['func_5085'] = func_5085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5085_call = mutated_mod.get_global_var('func_5085')
var_5087 = relay.var("var_5087", dtype = "int8", shape = (4, 13, 16))#candidate|5087|(4, 13, 16)|var|int8
var_5088 = relay.var("var_5088", dtype = "int8", shape = (4, 13, 16))#candidate|5088|(4, 13, 16)|var|int8
call_5086 = func_5085_call(var_5087,var_5088,)
output = call_5086
func_5089 = relay.Function([var_5087,var_5088,], output)
mutated_mod['func_5089'] = func_5089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2899_call = mod.get_global_var('func_2899')
func_2901_call = mutated_mod.get_global_var('func_2901')
call_5100 = func_2899_call()
call_5101 = func_2899_call()
func_3628_call = mod.get_global_var('func_3628')
func_3632_call = mutated_mod.get_global_var('func_3632')
var_5119 = relay.var("var_5119", dtype = "float32", shape = (156,))#candidate|5119|(156,)|var|float32
var_5120 = relay.var("var_5120", dtype = "int8", shape = (182,))#candidate|5120|(182,)|var|int8
call_5118 = relay.TupleGetItem(func_3628_call(relay.reshape(var_5119.astype('float32'), [13, 2, 6]), relay.reshape(var_5120.astype('int8'), [182,]), ), 5)
call_5121 = relay.TupleGetItem(func_3632_call(relay.reshape(var_5119.astype('float32'), [13, 2, 6]), relay.reshape(var_5120.astype('int8'), [182,]), ), 5)
output = relay.Tuple([call_5100,call_5118,var_5119,var_5120,])
output2 = relay.Tuple([call_5101,call_5121,var_5119,var_5120,])
func_5122 = relay.Function([var_5119,var_5120,], output)
mod['func_5122'] = func_5122
mod = relay.transform.InferType()(mod)
mutated_mod['func_5122'] = func_5122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5122_call = mutated_mod.get_global_var('func_5122')
var_5124 = relay.var("var_5124", dtype = "float32", shape = (156,))#candidate|5124|(156,)|var|float32
var_5125 = relay.var("var_5125", dtype = "int8", shape = (182,))#candidate|5125|(182,)|var|int8
call_5123 = func_5122_call(var_5124,var_5125,)
output = call_5123
func_5126 = relay.Function([var_5124,var_5125,], output)
mutated_mod['func_5126'] = func_5126
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5134 = relay.var("var_5134", dtype = "uint32", shape = (14, 6, 10))#candidate|5134|(14, 6, 10)|var|uint32
var_5135 = relay.var("var_5135", dtype = "uint32", shape = (14, 6, 10))#candidate|5135|(14, 6, 10)|var|uint32
bop_5136 = relay.bitwise_or(var_5134.astype('uint32'), relay.reshape(var_5135.astype('uint32'), relay.shape_of(var_5134))) # shape=(14, 6, 10)
output = relay.Tuple([bop_5136,])
output2 = relay.Tuple([bop_5136,])
func_5154 = relay.Function([var_5134,var_5135,], output)
mod['func_5154'] = func_5154
mod = relay.transform.InferType()(mod)
mutated_mod['func_5154'] = func_5154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5154_call = mutated_mod.get_global_var('func_5154')
var_5156 = relay.var("var_5156", dtype = "uint32", shape = (14, 6, 10))#candidate|5156|(14, 6, 10)|var|uint32
var_5157 = relay.var("var_5157", dtype = "uint32", shape = (14, 6, 10))#candidate|5157|(14, 6, 10)|var|uint32
call_5155 = func_5154_call(var_5156,var_5157,)
output = call_5155
func_5158 = relay.Function([var_5156,var_5157,], output)
mutated_mod['func_5158'] = func_5158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2751_call = mod.get_global_var('func_2751')
func_2753_call = mutated_mod.get_global_var('func_2753')
call_5194 = relay.TupleGetItem(func_2751_call(), 1)
call_5195 = relay.TupleGetItem(func_2753_call(), 1)
func_2899_call = mod.get_global_var('func_2899')
func_2901_call = mutated_mod.get_global_var('func_2901')
call_5200 = func_2899_call()
call_5201 = func_2899_call()
func_3550_call = mod.get_global_var('func_3550')
func_3553_call = mutated_mod.get_global_var('func_3553')
var_5203 = relay.var("var_5203", dtype = "float64", shape = (198,))#candidate|5203|(198,)|var|float64
call_5202 = relay.TupleGetItem(func_3550_call(relay.reshape(call_5194.astype('float32'), [13, 2, 6]), relay.reshape(var_5203.astype('float64'), [1, 198]), ), 0)
call_5204 = relay.TupleGetItem(func_3553_call(relay.reshape(call_5194.astype('float32'), [13, 2, 6]), relay.reshape(var_5203.astype('float64'), [1, 198]), ), 0)
func_3892_call = mod.get_global_var('func_3892')
func_3893_call = mutated_mod.get_global_var('func_3893')
call_5213 = relay.TupleGetItem(func_3892_call(), 0)
call_5214 = relay.TupleGetItem(func_3893_call(), 0)
bop_5217 = relay.bitwise_and(call_5213.astype('int8'), relay.reshape(call_5202.astype('int8'), relay.shape_of(call_5213))) # shape=(13, 2, 6)
bop_5220 = relay.bitwise_and(call_5214.astype('int8'), relay.reshape(call_5204.astype('int8'), relay.shape_of(call_5214))) # shape=(13, 2, 6)
func_2654_call = mod.get_global_var('func_2654')
func_2657_call = mutated_mod.get_global_var('func_2657')
const_5236 = relay.const([-6.145312,-6.774414,-5.747678,5.678608,-1.795673,-5.674319,-7.654043,-1.883902,6.588018,-8.766658,2.397365,-5.737323,1.828197,-2.795173,-8.724816,-4.261769,-8.499797,7.799313,8.115802,3.450739,-5.065634,3.660510,1.532816,-5.394154,8.872007,6.862558,-0.048109,-3.964975,9.336561,-4.475702,7.661796,1.184073,2.823249,-9.097344,8.620719,-4.021602,-7.997509,5.751926,7.139515,-3.270935,-2.930610,1.227194,5.181415,-8.486487,8.859795,-2.398776,3.757501,-3.705509,-3.129732,9.469112,-5.198901,-7.098226,2.662144,8.697974,9.592618,-0.202965,9.694309,-6.776186,0.087919,-9.779447,1.015675,9.465347,-1.257394,0.772390,-7.190156,-3.446047,5.944848,1.359404,-5.152016,1.206062,-8.055372,0.997742,-1.613681,-5.611681,-4.830732,-6.393193,6.379411,-3.286490,6.001083,6.579174,3.151434,1.921556,-5.994221,4.810023,8.690616,-8.291970,-0.006303,8.349920,-6.767017,-8.067594,-0.899074,-6.289577,-7.697713,3.716322,7.703937,-7.996352,6.297851,1.245851,-7.391620,-6.435998,9.249274,-1.182698,5.867292,-4.347867,4.279690,-6.769057,3.815555,-6.760382,-4.710608,-6.679159,-7.312550,-8.037974,-1.342923,3.207382,-0.559536,-1.683833,-5.595568,-6.616620,-8.097431,3.345601,7.240219,-1.086484,9.633015,5.918998,-8.699111,2.638200,-2.001255,-0.204543,6.471864,9.417067,-7.791603,6.325431,-9.202753,-2.959151,7.555983,1.084928,4.309314,2.588998,-3.793917,-0.880009,-5.223015,6.330725,8.250984,3.984389,8.192594,0.376147,-0.222342,-8.141997,-2.517143,-5.783449,2.617773,-8.723654,5.828156,2.679521,-2.605640,-4.384919,3.452687,1.254609,-9.031690,8.252305,-9.379107,4.983579,8.924797,8.122613,-3.486752,7.517182,1.298038,-2.161832,-6.747625,-5.283640,-3.899532,7.583512,-8.090712,-5.693625,-2.321605,-7.535826,-8.393290,8.251411,-9.581965,3.726645,-7.758259,-0.389836,6.069885,-8.763698,-0.025673,-1.088070,-0.256779,-1.646595,9.278206,0.085960,-7.357220,-4.805837,8.709123,-4.565106,-6.294545,-0.331480,9.826392,0.468657,3.002134,-5.147938,-3.839761,-4.683440,-1.583252,-9.001587,-6.803930,8.172093,4.112584,1.557365,-1.630549,-6.891341,-0.831240,7.179882,4.963605,-0.172252,9.693671,-4.251487,0.037074,-8.118560,5.673132,3.313278,-6.870672,-4.906014,-1.061244,-7.160140,-4.389232,-8.204326,9.364966,-1.944411,-4.249604,8.736798,5.256994,5.066467,5.782492,-8.261436,-5.285504,-0.082082,0.894164,0.173746,-1.829047,-7.329767,-4.331592,2.436313,-1.170033,0.456072,-1.761657,-6.434049,-6.174989,7.224181,5.553697,3.626806,5.451452,-8.199591,-1.618518,6.132119,2.559140,0.437163,-4.670827,0.170721,-7.849563,6.903736,-2.018988,-0.124645,9.966388,-7.980423,-9.392893,6.128108,9.683772,-3.927495,0.901515,-1.750785,3.424691,-2.660428,4.697845,-0.607362,-4.409278,-0.061537,-8.956712,-9.533245,-3.313843,-1.766822,-3.901935,6.882268,-8.715762,9.347556,8.487649,-7.662020,-0.405101,-2.715175,1.842221,8.187532,-1.332704,-5.777162,8.022166,-2.514557,9.238356,-3.179595,-6.064922,5.330712,7.478230,-9.408868,-4.964796,3.038646,-2.756266,-2.223245,-3.337435,9.701183,-3.730670,1.971112,-0.052426,1.376980,7.145342,4.874007,2.354847,-0.064236,-7.434775,2.610491,0.838264,5.090365,-1.021511,3.114308,2.557024,3.144166,-5.931843,2.317555,5.528640,-3.002468,-4.178682,-0.979865,-2.053972,-7.650619,-3.548776,-4.943461,-3.680917,4.314286,0.863020,-8.657558,3.146192,-6.288989,-4.366486,0.606727,5.845873,-6.087319,5.068847,9.411233,2.681867,-7.878733,-7.534048,-2.299790,-7.194057,9.634712,-0.834794,3.976842,-6.654554,-2.627860,6.855300,-3.348837,7.298655,1.392154,4.941272,2.689315,-9.093052,-6.815199,-2.965462,-6.355464,-3.075246,-0.778528,8.540129,0.908717,-4.480235,-2.653604,8.676439,-7.470699,-4.036171,6.588950,-9.042441,-7.680996,5.686057,9.857379,6.435559,-8.835238,-6.668889,9.271979,-6.039093,0.231796,-6.762522,6.304949,-6.250307,-2.567165,0.965366,-2.115373,-8.236179,-2.614425,-2.073320,9.150715,7.755752,0.921646,2.006692,9.395182,5.105043,-7.168188,9.685232,6.128057,0.172464,-2.862740,-7.936174,-4.805584,3.858455,-2.787487,0.165919,-5.818099,3.915770,-4.809781,-0.052841,0.616502,-3.734663,7.228011,2.270621,8.385956,-0.152690,6.637458,-8.935480,-0.350459,-2.070571,1.641822,-3.942986,9.018621,-3.588914,-3.800124,9.449408,-6.858479,7.268336,8.615910,6.642059,4.152829,-0.037565,-5.281662,8.399048,4.584942,3.107782,8.616123,-2.529499,7.477814,-8.513775,1.237382,2.196189,8.906642,4.895829,3.053737], dtype = "float64")#candidate|5236|(448,)|const|float64
call_5235 = relay.TupleGetItem(func_2654_call(relay.reshape(const_5236.astype('float64'), [14, 2, 16])), 0)
call_5237 = relay.TupleGetItem(func_2657_call(relay.reshape(const_5236.astype('float64'), [14, 2, 16])), 0)
output = relay.Tuple([call_5194,call_5200,var_5203,bop_5217,call_5235,const_5236,])
output2 = relay.Tuple([call_5195,call_5201,var_5203,bop_5220,call_5237,const_5236,])
func_5248 = relay.Function([var_5203,], output)
mod['func_5248'] = func_5248
mod = relay.transform.InferType()(mod)
mutated_mod['func_5248'] = func_5248
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5249 = relay.var("var_5249", dtype = "float64", shape = (198,))#candidate|5249|(198,)|var|float64
func_5248_call = mutated_mod.get_global_var('func_5248')
call_5250 = func_5248_call(var_5249)
output = call_5250
func_5251 = relay.Function([var_5249], output)
mutated_mod['func_5251'] = func_5251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2899_call = mod.get_global_var('func_2899')
func_2901_call = mutated_mod.get_global_var('func_2901')
call_5330 = func_2899_call()
call_5331 = func_2899_call()
output = call_5330
output2 = call_5331
func_5333 = relay.Function([], output)
mod['func_5333'] = func_5333
mod = relay.transform.InferType()(mod)
output = func_5333()
func_5334 = relay.Function([], output)
mutated_mod['func_5334'] = func_5334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2528_call = mod.get_global_var('func_2528')
func_2529_call = mutated_mod.get_global_var('func_2529')
call_5392 = relay.TupleGetItem(func_2528_call(), 0)
call_5393 = relay.TupleGetItem(func_2529_call(), 0)
func_1192_call = mod.get_global_var('func_1192')
func_1197_call = mutated_mod.get_global_var('func_1197')
const_5401 = relay.const([[-5,-6,7,3,2,4,4,8,8,5,6,4,-3,-6,7,9,-4,-6,-4,10,-7,-5,6,-4,-9,10,-2,-3,-3,4,-2,-2,1,1,9,3,-6,8,10,-8,-2,-8,-5,1,-9,8,1,-10,-7,8,-2,3,-7,-2,4,-10,8,-3,7,1,-1,9,-8,-6,10,3,5,2,9,-3,-3,9,8,-6,-6,-3,5,-10,-1,-8,-10,-4,6,-9,3,-8,-4,10,1,-9,3,5,-1,1,-3,4,-9,-8,-8,10,10,8,8,-6,-1,7,6,-2,-1,1,-1,7,5,6,4,-5,-5,8,10,-4,8,7,-7,3,1,2,-10,3,-6,-1,5,3,-8,7,5]], dtype = "uint64")#candidate|5401|(1, 135)|const|uint64
var_5402 = relay.var("var_5402", dtype = "uint8", shape = ())#candidate|5402|()|var|uint8
const_5403 = relay.const([9,3,10,7,-7,2,-4,-9,7,2,7,-2,-7,6,-2,-10,2,4,-9,-7,7,6,-8,-8,-2,8,10,4,9,-3,-10,3,-8,6,-7,6,10,7,9,-4,8,10,2,-7,5,-3,5,-7,-2,-2,5,4,10,-5,1,-1,1,-8,7,-3,5,7,3,-5,-6,5,5,-9,5,5,1,-6,9,-5,-9,-9,8,4,-2,6,6,-1,3,9,2,-3,-1,-7,-2,5,5,-6,1,-2,-1,-1,10,-9,2,10,-1,8,9,-10,-10,-2,2,7], dtype = "uint8")#candidate|5403|(108,)|const|uint8
call_5400 = relay.TupleGetItem(func_1192_call(relay.reshape(const_5401.astype('uint64'), [9, 15]), relay.reshape(const_5401.astype('uint64'), [9, 15]), relay.reshape(var_5402.astype('uint8'), []), relay.reshape(const_5403.astype('uint8'), [3, 36]), ), 0)
call_5404 = relay.TupleGetItem(func_1197_call(relay.reshape(const_5401.astype('uint64'), [9, 15]), relay.reshape(const_5401.astype('uint64'), [9, 15]), relay.reshape(var_5402.astype('uint8'), []), relay.reshape(const_5403.astype('uint8'), [3, 36]), ), 0)
output = relay.Tuple([call_5392,call_5400,const_5401,var_5402,const_5403,])
output2 = relay.Tuple([call_5393,call_5404,const_5401,var_5402,const_5403,])
func_5405 = relay.Function([var_5402,], output)
mod['func_5405'] = func_5405
mod = relay.transform.InferType()(mod)
mutated_mod['func_5405'] = func_5405
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5406 = relay.var("var_5406", dtype = "uint8", shape = ())#candidate|5406|()|var|uint8
func_5405_call = mutated_mod.get_global_var('func_5405')
call_5407 = func_5405_call(var_5406)
output = call_5407
func_5408 = relay.Function([var_5406], output)
mutated_mod['func_5408'] = func_5408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4052_call = mod.get_global_var('func_4052')
func_4054_call = mutated_mod.get_global_var('func_4054')
call_5428 = relay.TupleGetItem(func_4052_call(), 1)
call_5429 = relay.TupleGetItem(func_4054_call(), 1)
output = call_5428
output2 = call_5429
func_5447 = relay.Function([], output)
mod['func_5447'] = func_5447
mod = relay.transform.InferType()(mod)
output = func_5447()
func_5448 = relay.Function([], output)
mutated_mod['func_5448'] = func_5448
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5503 = relay.var("var_5503", dtype = "float32", shape = (9, 5, 15))#candidate|5503|(9, 5, 15)|var|float32
uop_5504 = relay.cos(var_5503.astype('float32')) # shape=(9, 5, 15)
func_2528_call = mod.get_global_var('func_2528')
func_2529_call = mutated_mod.get_global_var('func_2529')
call_5519 = relay.TupleGetItem(func_2528_call(), 0)
call_5520 = relay.TupleGetItem(func_2529_call(), 0)
output = relay.Tuple([uop_5504,call_5519,])
output2 = relay.Tuple([uop_5504,call_5520,])
func_5528 = relay.Function([var_5503,], output)
mod['func_5528'] = func_5528
mod = relay.transform.InferType()(mod)
mutated_mod['func_5528'] = func_5528
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5529 = relay.var("var_5529", dtype = "float32", shape = (9, 5, 15))#candidate|5529|(9, 5, 15)|var|float32
func_5528_call = mutated_mod.get_global_var('func_5528')
call_5530 = func_5528_call(var_5529)
output = call_5530
func_5531 = relay.Function([var_5529], output)
mutated_mod['func_5531'] = func_5531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2969_call = mod.get_global_var('func_2969')
func_2970_call = mutated_mod.get_global_var('func_2970')
call_5560 = func_2969_call()
call_5561 = func_2969_call()
uop_5588 = relay.sigmoid(call_5560.astype('float32')) # shape=(13, 2, 6)
uop_5590 = relay.sigmoid(call_5561.astype('float32')) # shape=(13, 2, 6)
func_3082_call = mod.get_global_var('func_3082')
func_3084_call = mutated_mod.get_global_var('func_3084')
call_5593 = relay.TupleGetItem(func_3082_call(), 2)
call_5594 = relay.TupleGetItem(func_3084_call(), 2)
output = relay.Tuple([uop_5588,call_5593,])
output2 = relay.Tuple([uop_5590,call_5594,])
func_5603 = relay.Function([], output)
mod['func_5603'] = func_5603
mod = relay.transform.InferType()(mod)
output = func_5603()
func_5604 = relay.Function([], output)
mutated_mod['func_5604'] = func_5604
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5651 = relay.const([[[-2,9],[7,-5],[-1,1],[-9,-2],[-5,6],[-6,-2]],[[-6,-1],[-2,3],[6,-9],[-4,-5],[-3,-2],[3,-5]],[[-10,-10],[2,9],[-3,-10],[-5,-8],[-5,-2],[-3,-3]],[[7,-1],[1,3],[-8,10],[-8,-5],[9,-5],[-10,-5]],[[-2,-3],[-8,-1],[6,-7],[7,8],[2,-5],[-7,1]],[[-8,10],[7,-3],[2,4],[-6,5],[7,7],[-2,1]],[[-5,6],[7,-7],[2,-2],[-3,-10],[5,-7],[8,-3]],[[5,-1],[6,-3],[-8,-2],[4,9],[9,7],[-8,-8]],[[-10,4],[-10,5],[6,4],[-9,5],[-4,2],[8,-6]],[[-3,-8],[-9,-6],[3,8],[-8,1],[-10,9],[2,7]],[[-3,-5],[-8,-6],[3,6],[10,2],[-5,-9],[5,8]]], dtype = "int8")#candidate|5651|(11, 6, 2)|const|int8
var_5652 = relay.var("var_5652", dtype = "int8", shape = (11, 6, 2))#candidate|5652|(11, 6, 2)|var|int8
bop_5653 = relay.left_shift(const_5651.astype('int8'), relay.reshape(var_5652.astype('int8'), relay.shape_of(const_5651))) # shape=(11, 6, 2)
bop_5658 = relay.logical_xor(bop_5653.astype('int32'), relay.reshape(var_5652.astype('int32'), relay.shape_of(bop_5653))) # shape=(11, 6, 2)
func_3461_call = mod.get_global_var('func_3461')
func_3466_call = mutated_mod.get_global_var('func_3466')
var_5673 = relay.var("var_5673", dtype = "float64", shape = (1050,))#candidate|5673|(1050,)|var|float64
const_5674 = relay.const([-7,-1,9,-1,-8,-7,7,9,6,3,-8,9,-4,3,9,6,-7,5,9,-2,5,8,-7,8,-8,-9,5,-2,-7,10,1,1,5,7,-4,-10,8,8,7,-3,8,-5,10,-1,4,-2,-9,4,-1,-9,10,5,-9,7,1,-5,2,4,-7,6,6,8,-2,-1,-5,-9,10,-7,7,9,2,8,1,-5,-5,-2,10,8,4,5,10,6,-6,-10,-5,-10,2,2,-10,-4,7,-5,5,6,-5,-9,-5,-6,8,-5,-7,-1,-4,2,9,8,1,-10,9,8,-9,10,5,-8,-5,7,9,-1,-10,-9,-9,4,2,-10,2,-6,8,6,3,-6,8,-10,-1,1,6,-10,-9,-6,-10,4,8,-2,8,-8,3,-1,7,-9,-2,10,2,-2,-6,-2,9,-8,-5,-3,-10,4,-7,6,6,-2,8,8,-4,1,-3,6,-10,-8,5,-10,2,-2,-8,-5,-6,5,-1,-3,5,6,-8,9,7,7,-9,-10,-10,2,-1,-6,-3,8,-6,-10,-5,-9,9,5,7,9,-10,1,-1,9,9,8,6,8,9,3,4,-10,-1,-10,-8,6,-8,-9,-9,3,-6,2,1,4,-7,5,-10,-4,-2,9,3,-10,-2,4,-9,-9,-9,7,-10,9,9,-9,-1,-1,-9,-6,8,5,-7,1,-5,-3,1,4,2,-1,1,1,4,8,-2,6,-2,-10,-10,-7,1,-1,9,-6,-1,3,8,6,3,5,-8,-5,-4,9,6,-8,7,9], dtype = "int16")#candidate|5674|(288,)|const|int16
const_5675 = relay.const([8,-3,-9,-4,3,9,-5,1,-7,-5,-8,6,7,-5,1,5,-7,-10,-9,3,4,-2,-9,10,-7,-6,-7,-10,6,-3,9,-6,-6,5,3,-7,-10,-9,-9,6,-6,-2,-5,-7,10,-7,10,7,2,-9,-10,3,3,-8,10,2,-8,-7,7,-5,-8,7,-6,1,-6,2,-7,5,-6,6,-9,-2,-1,4,-4,6,-1,-9,-7,6,3,9,-4,1,9,8,4,-7,-8,4,9,-6,-2,9,5,5,7,7,-8,3,-6,5,10,8,2,2,1,-4], dtype = "uint8")#candidate|5675|(108,)|const|uint8
call_5672 = relay.TupleGetItem(func_3461_call(relay.reshape(var_5673.astype('float64'), [1050,]), relay.reshape(const_5674.astype('int16'), [288,]), relay.reshape(const_5675.astype('uint8'), [108,]), ), 2)
call_5676 = relay.TupleGetItem(func_3466_call(relay.reshape(var_5673.astype('float64'), [1050,]), relay.reshape(const_5674.astype('int16'), [288,]), relay.reshape(const_5675.astype('uint8'), [108,]), ), 2)
output = relay.Tuple([bop_5658,call_5672,var_5673,const_5674,const_5675,])
output2 = relay.Tuple([bop_5658,call_5676,var_5673,const_5674,const_5675,])
func_5681 = relay.Function([var_5652,var_5673,], output)
mod['func_5681'] = func_5681
mod = relay.transform.InferType()(mod)
var_5682 = relay.var("var_5682", dtype = "int8", shape = (11, 6, 2))#candidate|5682|(11, 6, 2)|var|int8
var_5683 = relay.var("var_5683", dtype = "float64", shape = (1050,))#candidate|5683|(1050,)|var|float64
output = func_5681(var_5682,var_5683,)
func_5684 = relay.Function([var_5682,var_5683,], output)
mutated_mod['func_5684'] = func_5684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5603_call = mod.get_global_var('func_5603')
func_5604_call = mutated_mod.get_global_var('func_5604')
call_5689 = relay.TupleGetItem(func_5603_call(), 1)
call_5690 = relay.TupleGetItem(func_5604_call(), 1)
func_5681_call = mod.get_global_var('func_5681')
func_5684_call = mutated_mod.get_global_var('func_5684')
const_5709 = relay.const([-10,-5,4,-8,-9,-10,-9,-10,2,3,2,-3,4,5,-1,-2,-7,1,8,-6,8,-3,7,-7,1,-7,1,6,-1,-7,-3,-3,-5,-6,8,10,-6,-2,-6,1,6,-2,10,-10,1,7,-8,6,7,-6,4,8,9,-4,-8,4,-5,-10,-6,-9,-10,3,-7,1,1,-8,3,4,7,-9,-4,-8,9,5,-8,4,-9,8,-8,-9,-6,5,-2,-3,8,3,-3,9,8,-1,8,-6,4,2,-3,-10,-7,-10,5,-5,3,3,8,-2,-7,5,-8,-2,-5,6,-5,-6,-3,-1,-8,-1,6,-9,-7,-3,3,10,6,-6,8,8,-8,8,-1,-10,-7,1], dtype = "int8")#candidate|5709|(132,)|const|int8
const_5710 = relay.const([-4.699501,6.665764,-5.807367,-2.110608,-0.987516,6.792125,-1.387199,9.756130,5.758188,9.745577,-0.472217,-9.062413,5.715050,5.489627,-0.689600,-1.708003,0.405523,-8.451883,2.767513,-4.927774,-3.295219,0.876197,-1.583039,4.038025,-1.690559,-3.636395,-4.686726,4.007861,-5.476902,-0.246113,0.032808,0.489440,5.543143,9.505596,-0.733063,-1.399718,5.088979,6.312936,2.819958,0.784668,-7.768854,-9.849163,-3.862807,-3.655435,-7.045410,5.939334,8.713248,4.238353,-2.258808,-7.499800,-7.253306,1.529939,-9.734888,4.603440,6.909889,-2.554489,7.090339,1.786439,-5.098072,-4.946708,-4.912752,-9.716114,4.289105,-3.662420,-8.751413,-6.136425,-2.013398,-2.667399,8.777529,-4.918886,-6.782821,-3.701777,8.873043,2.980977,4.935065,-7.862477,-7.148424,0.257715,-4.644504,3.415318,-4.782831,-9.897818,-9.870948,-9.745913,-1.192818,-3.514224,5.107798,-8.650341,-5.056657,-6.999790,-6.704374,-3.426899,1.002409,-5.837730,5.331061,1.679957,1.517600,-7.325801,-9.048540,7.011980,6.809491,-6.439081,-0.108659,4.002703,-5.788150,-3.340585,8.733651,1.099766,4.279536,-0.792363,-9.875695,-2.964485,0.493045,9.851589,0.887753,5.195138,-8.996951,8.210164,-4.972910,-9.663730,-2.051250,1.136393,8.265113,1.073083,-4.536168,9.484509,6.023513,3.942270,1.623544,-1.798234,8.437378,9.347373,5.955287,7.374903,-0.979265,8.197748,-7.368194,-0.299693,4.219031,-8.949371,3.799771,-2.321371,-8.853229,-9.784302,-2.876631,-9.139791,-8.150414,-6.423490,3.855609,6.554331,2.537150,-3.163260,-0.792761,8.323008,-2.598121,2.799776,1.700468,-1.120303,4.849075,5.361197,-4.322199,-3.718859,-7.015234,-9.099220,-3.439134,9.358471,-5.326390,3.972242,-3.065032,0.224704,3.579780,-4.715961,-1.570440,-0.148880,3.198210,-4.034386,8.998950,-8.979280,7.724137,0.340706,1.031923,6.142231,8.204762,-7.022340,7.107592,-0.381846,-5.323713,5.829314,-4.224625,2.284438,-2.194236,9.256662,-8.857818,3.623973,-1.447116,4.031306,4.754915,-1.222481,5.028171,-3.859030,-0.675645,6.365232,5.125913,6.291105,-8.512039,-6.933312,-1.175052,5.466983,9.859447,-0.599919,3.927771,1.906935,-6.958754,2.283603,-4.274267,-1.746387,1.573531,-4.062570,0.863907,-4.370685,-4.676089,-1.990714,-2.603975,8.535796,-7.056183,2.179221,9.283285,-0.280434,-1.593996,9.741412,0.199286,5.467653,-7.517084,2.272459,-0.394856,8.901490,-6.933603,9.880165,5.739267,9.246799,2.470851,-2.216566,1.747822,-7.610173,-0.640942,3.174957,-6.148125,-5.586915,-8.279228,-6.922808,4.331628,9.279337,0.963119,-4.870079,8.504496,-6.907993,3.239684,4.620258,6.707374,-7.886022,8.508982,5.560535,5.810634,-2.760309,4.921273,-8.387438,9.077243,2.904361,-1.385845,7.594164,7.524378,-3.982417,-1.174923,3.116217,-2.039886,-0.087929,0.143187,4.033829,5.874650,-6.485499,-7.666219,-7.373902,-8.489608,-5.426232,0.337618,-8.777419,9.256674,1.318298,-2.182686,5.125417,6.961214,7.805361,4.725840,0.259068,-7.258365,7.317079,-0.298769,-2.886780,2.035478,7.855280,3.989820,3.138205,7.210270,-0.571350,-8.134167,-5.690501,7.730196,-3.054610,-9.958197,-7.499651,-5.016664,5.346195,3.149044,2.047388,-4.048511,8.261308,8.336040,-0.334061,-9.901699,-3.639784,-8.884481,-3.700177,-3.013365,-7.434116,-5.691241,-1.573855,-9.919181,7.101038,0.950950,7.351229,4.188060,2.833535,3.837088,0.212250,4.290668,-6.777814,-2.621251,9.883384,-4.213315,0.538510,-2.679833,4.658151,8.816634,-1.131761,6.926752,-8.710139,6.818885,4.701641,7.908455,-2.358336,2.731478,-0.048567,8.393197,-0.165566,5.131547,-8.205257,6.050700,3.744261,-8.395137,-7.874109,4.933822,-0.350654,-1.485245,8.337270,8.152958,-8.805489,7.206444,-9.935221,4.937939,-1.449055,1.745702,-8.042332,-6.765698,1.603171,-1.143256,-7.065626,0.945906,-9.828282,7.647614,7.251977,9.278644,5.050067,1.699904,4.856596,-1.323463,0.239002,-8.763993,8.717862,7.648612,3.322864,-8.026633,8.874518,-6.544420,6.667351,-3.437398,-9.295177,1.638241,-7.220017,-6.432752,5.674148,0.197237,-0.014459,-8.524004,-9.477635,-1.090915,9.112010,2.750009,-9.371358,-8.385481,0.024647,3.611778,-0.160962,9.449202,2.204695,-1.401694,6.339393,1.126543,0.122901,1.917403,-7.062051,8.713261,-5.517870,-3.184414,2.953929,-6.577754,0.255329,-6.372931,-8.477477,-2.044849,9.082516,-8.628394,-6.178111,-7.088819,-1.216056,6.994960,-5.108726,-0.334007,-0.012474,3.086271,-3.667472,-5.660080,7.115990,2.731973,4.819746,4.639770,3.207572,7.309040,-7.006810,9.562881,9.517999,1.385277,-7.959682,-5.577222,-2.038074,-3.461338,1.485683,3.092708,0.038413,5.939570,-6.685121,-9.004082,-5.009237,-5.073642,2.009471,5.275267,-3.742054,-8.465587,5.885037,9.720940,3.588557,-6.059891,2.818896,6.118148,-1.208651,9.033376,-4.383452,-1.322708,7.987151,5.807239,8.768697,5.367017,8.351233,-6.044662,-8.066992,-5.275866,8.312353,-8.275213,-9.824139,9.170632,-2.572820,-3.329929,-1.617132,-8.963388,5.016130,6.390800,-0.972024,-7.939445,-2.769080,-1.868650,0.225273,-6.924040,3.974580,3.088551,4.575590,5.845179,1.976721,-5.802018,-0.119378,0.139535,-1.891353,-3.916592,7.163606,-4.287886,5.429579,-1.453414,2.301215,6.510674,7.517182,7.043480,-1.367395,7.577035,-6.247375,5.374120,-6.383101,-5.800388,3.773536,8.381018,5.185614,5.891971,8.267074,0.936022,-3.416621,2.804969,0.691379,-0.711337,6.840907,7.716724,8.547764,4.656412,5.160451,-5.784629,-8.067252,9.570405,3.987198,1.417613,-8.711563,-4.720659,7.854944,5.327162,-1.546885,-8.970718,8.820948,4.311519,7.671606,-2.509933,-6.975461,9.002066,-9.747266,-0.569234,5.621739,-0.739088,9.977203,3.732443,8.448486,0.001826,-9.975190,9.559886,-3.822461,7.665200,3.166221,-1.110180,-4.097295,6.873496,6.626217,4.677555,2.525730,-4.420791,-2.453257,4.401510,-1.664306,1.741075,6.147284,-2.453702,1.808781,6.963504,8.087944,-5.996303,4.206824,9.465956,6.595471,-9.617975,-0.994154,3.512067,-3.661056,-5.227192,-1.756804,2.512297,6.374381,3.462538,8.184900,9.206489,-2.686632,5.206517,4.822089,-2.855996,9.298540,4.016590,-1.476251,-2.376803,-6.279020,9.829150,-6.755101,-9.788319,6.930872,-7.215771,-8.599328,0.089861,9.474591,-7.005179,8.845763,2.960042,9.358414,8.610843,-2.941514,-9.797668,-1.839324,1.650997,9.297184,-3.678597,0.793144,6.187020,9.993338,-3.574570,5.937399,9.257254,-5.399728,9.057297,-9.750639,8.138635,-5.857294,6.859002,6.933107,8.250285,-5.347607,3.717727,-8.835919,9.893254,-3.780815,-8.514634,-4.231266,-4.568959,3.407280,7.208208,-0.883195,-4.269683,-6.290851,-1.612140,-4.568615,-2.972550,5.027719,-4.338675,2.372360,1.002446,2.091579,4.963914,-3.378958,-2.920371,-2.376400,0.400116,-1.345951,1.165135,1.165088,4.876872,-4.749394,-0.747002,1.565061,8.155494,-3.460464,-0.331809,0.913122,8.340039,-0.544774,2.937533,5.138140,0.255488,-8.944145,7.430515,-2.014634,4.243979,-7.361374,5.419156,-2.469713,-3.023667,1.749856,-3.941360,0.813615,-3.669082,-9.133100,-7.248559,-6.885494,7.053840,-5.791047,-8.621537,6.309007,5.484133,4.989302,-5.832546,-2.373916,-7.793208,9.304925,-4.077280,5.417006,-9.024987,-7.520530,4.263237,2.389916,4.550955,0.680192,-5.601618,0.493460,4.372120,-2.577884,-0.540815,-1.224035,6.072657,0.912922,-1.757735,-4.424790,-4.323562,9.905610,-2.762525,7.399563,1.546766,0.549946,8.207802,4.784677,-5.713818,-2.448802,-4.405970,1.529087,8.743400,9.854571,3.487290,-0.898610,-8.011209,-0.871645,-2.132421,-9.713396,-3.762734,-8.686972,-0.290016,-5.500667,9.438956,5.557359,-2.037879,5.913633,-3.787954,7.477702,2.633157,8.955709,-5.803088,-1.606559,9.027758,-6.786466,-0.876019,-7.267566,-8.373302,1.015456,5.804258,-3.232765,-8.056370,5.910876,-6.929627,-2.105912,3.086086,-3.528192,1.165250,-3.242058,2.446931,3.262111,8.546919,9.425806,-0.191076,-6.111413,9.864646,3.706455,-8.652244,-0.225030,-4.466007,-3.130366,4.318462,1.817582,9.799433,6.749261,-3.059929,9.291875,-9.291558,0.604505,4.851491,2.807840,-3.156206,-0.574036,0.358441,-4.477146,-5.987299,3.108245,7.127594,-1.339259,4.948980,4.152034,-1.301934,4.136704,0.178433,-7.465103,-8.017075,-0.080769,-7.361398,-7.188101,4.899378,0.399775,5.660112,5.145299,0.023031,-8.951676,-0.995526,-8.274948,-1.216077,3.872917,2.924306,-0.980429,1.772297,-7.072281,-7.449161,-1.388541,5.085836,0.791694,-4.867305,9.381346,-1.163049,-6.135793,-5.026656,-2.122574,7.224667,-1.364235,7.249306,-0.367302,7.885792,-9.116203,9.186976,-7.675764,8.037569,-4.239157,-7.253287,6.593959,1.998824,0.168260,2.600454,-3.822398,-2.603252,5.202505,2.558058,-7.593935,-4.423674,-5.361454,8.573496,4.558171,-2.880014,6.034389,2.658420,-8.584118,-0.406384,-3.560252,4.177738,-7.731214,-4.968880,9.049533,-1.909941,-8.443150,-7.530483,-2.835578,4.753976,-9.242889,6.331667,4.330949,5.831444,3.057794,1.690316,6.174381,-9.681549,-0.406523,9.723308,1.640144,-6.700146,-8.920306,-6.518624,-3.163022,-2.296838,-5.956877,-2.316296,2.378382,0.067134,-2.556165,-2.053231,8.600640,0.943830,3.518948,5.814719,-1.197499,8.792491,-8.600698,-6.728534,7.961101,-5.770768,-8.737329,7.177851,-1.109135,6.618311,-4.984344,-2.052355,-7.392796,7.185438,-4.320238,-2.255226,-5.770887,9.490930,-4.540560,-5.826847,4.016359,7.380949,8.815201,1.820209,7.520906,-3.353610,-2.418253,2.198291,0.219490,8.557074,9.264638,-6.427931,3.459521,-4.704247,2.033012,1.078993,5.347057,8.338398,-6.518476,-8.131666,7.498925,6.493272,1.418801,-7.326064,0.496270,-3.083645,-6.557076,0.059832,3.685566,1.750330,-7.150911,9.848503,0.653601,-4.483909,9.580004,6.849376,-4.055227,-5.439136,5.349419,-1.236192,-3.629064,2.501528,8.140188,-0.709534,-3.613356,-4.040732,0.364829,8.996760,-4.784895,-1.029028,-7.735779,-7.269811,-3.340787,0.730843,3.415315,-3.859384,-8.243034,-6.930859,-2.768730,-6.378891,-1.106935,9.134069,-3.509553,-7.758098,5.790671,-9.973536,-0.543130,-7.383831,-4.338774,-1.889472,4.502012,4.112978,-6.328231,2.424277,3.862826,-8.629651,-8.795832,7.961641,-8.075688,8.748846,-0.015839,3.537698,-3.379515,3.901281,1.449285,1.131032,-6.206996,8.158130,-7.000753,-2.894286,-6.330470,-0.500957,-1.401121,-0.200957,1.547853,-2.920848,4.384485,5.925439,6.564367,-7.230364,-2.011501,7.589827,2.805258,-5.004697,-0.375386,4.331302,0.634053,6.618184,0.743067,-7.168065,-1.679002,-9.273044,-4.117209,3.384389,-4.089299,1.164138,5.994085,7.216925,4.583304,3.544493,-9.378898,-8.055636,-0.715363], dtype = "float64")#candidate|5710|(1050,)|const|float64
call_5708 = relay.TupleGetItem(func_5681_call(relay.reshape(const_5709.astype('int8'), [11, 6, 2]), relay.reshape(const_5710.astype('float64'), [1050,]), ), 3)
call_5711 = relay.TupleGetItem(func_5684_call(relay.reshape(const_5709.astype('int8'), [11, 6, 2]), relay.reshape(const_5710.astype('float64'), [1050,]), ), 3)
func_5603_call = mod.get_global_var('func_5603')
func_5604_call = mutated_mod.get_global_var('func_5604')
call_5717 = relay.TupleGetItem(func_5603_call(), 1)
call_5718 = relay.TupleGetItem(func_5604_call(), 1)
func_2751_call = mod.get_global_var('func_2751')
func_2753_call = mutated_mod.get_global_var('func_2753')
call_5732 = relay.TupleGetItem(func_2751_call(), 1)
call_5733 = relay.TupleGetItem(func_2753_call(), 1)
func_2751_call = mod.get_global_var('func_2751')
func_2753_call = mutated_mod.get_global_var('func_2753')
call_5736 = relay.TupleGetItem(func_2751_call(), 1)
call_5737 = relay.TupleGetItem(func_2753_call(), 1)
func_4957_call = mod.get_global_var('func_4957')
func_4959_call = mutated_mod.get_global_var('func_4959')
const_5741 = relay.const([-0.764197,-0.950115,3.968848,6.075040,-0.372287,-5.332018,-9.976919,-9.364262,8.034801,9.358859,-1.715444,9.510468,1.939027,3.742922,-2.554895,0.554020,-2.893328,3.754550,0.615920,3.015685,-6.939960,-0.619596,8.175148,9.658145,-8.093378,-5.539746,4.278815,7.117803,-6.169696,6.990960,-5.088211,8.778289,7.322493,-7.665978,9.344988,-9.808163,-8.743630,-5.450342,-5.883044,-4.276656,4.774814,1.896465,1.933378,5.647513,9.472114,-0.813431,5.007113,-7.268835,-5.215949,2.414808,5.374747,4.954982,-2.609416,5.870641,-8.308182,-7.611220,-3.420104,-2.065341,-2.599627,9.691625,-0.493751,9.875536,8.477442,-1.665497,2.941378,3.302114,-1.784846,-7.638139,4.427998,3.098854,0.106858,1.142166,0.977591,8.683579,8.116080,9.499642,-7.465122,9.709956,-0.770420,-1.424350,-6.574450,-6.540923,-6.565537,8.127284,-6.802680,0.248721,-7.595933,-1.339420,-2.635720,-7.761613,-0.057524,-4.621014,-0.024690,4.057818,4.269993,-3.731754,9.951854,-8.986090,9.386008,4.266476,-0.137059,-9.182685,6.224429,-7.191100,-7.979162,3.697670,-4.892675,-6.220479,-4.302705,-3.714105,2.930664,5.826390,8.725872,-3.970891,9.873308,9.627538,6.980992,2.072905,-2.938288,-5.668557,-2.939710,6.269439,6.454788,6.275444,4.616351,-0.715108,4.347428,-6.550330,6.567528,5.770472,-8.586229,7.224569,-4.019408,4.302639,-0.638568,-7.997811,4.612221,-1.797023,3.191118,-7.551726,9.569648,6.174688,-2.605396,1.681584,-6.744863,0.402064,5.945626,-7.283286,0.313574,-0.065253,-3.421842,-6.905090,9.886603,-8.457429,-8.173240,3.688643,7.860521,-8.031502,-8.759648,-1.669849,1.283286,-7.794887,-4.339788,-0.395122,-4.560304,2.591099,8.637766,-9.180407,-8.367570,3.020182,-4.734989,-1.792759,2.100932,7.840332,2.009696,9.126253,1.637617,1.719580,-7.031618,4.842085,6.041758,9.120060,-3.538826,5.755896,2.176761,-2.221420,2.754297,2.553789,2.508156,9.437613,-6.142457,0.392618,-9.617535,4.994399,3.234366,1.720261,-6.223587,4.853296,-6.901043,5.606814,-4.366368,9.768846,5.181428,-3.497184,-7.423346,8.121700,-1.462493,-7.812875,7.161740,-7.420259,7.238593,4.149865,-5.474017,-1.185804,8.949552,-6.025455,7.057944,-4.153736,4.314264,-1.056302,-8.580556,-2.178250,-3.818649,6.990141,7.888608,-2.172500,3.096183,-3.714967,8.405631,-6.314069,-8.194649,-8.306365,6.413281,-6.725228,4.131632,-3.394527,-3.964885,4.021251,8.495651,8.058212,-0.393344,8.021316,4.769928,7.448329,3.651596,-2.400330,5.558498,3.135639,4.288010,8.606973,-1.367225,-0.043374,-6.765474,-7.541359,-6.378911,-5.101045,2.471540,-9.230981,4.666832,3.287986,3.963449,3.282336,-2.000516,6.013137,-8.006472,4.859559,-0.691432,-1.833342,5.290155,6.573392,-3.111094,-2.521709,5.119171,-6.222781,-6.282534,4.561454,7.684118,-9.443017,-0.769093,5.215704,-8.996193,8.592523,-7.049653,-4.078910,-0.349669,0.473462,9.476828,2.084776,-3.604433,-8.733171,6.282849,0.648198,-0.561184,9.560865,2.619456,6.059807,5.143479,3.837658,-7.209030,9.357878,4.261921,6.111208,-0.782317,0.111746,6.788904,7.576293,-0.353474,4.623334,1.019441,0.261747,-1.101640,-1.880381,4.709504,6.346508,4.831974,8.658249,-8.174704,-5.885179,6.067547,6.525131,2.458128,0.370423,1.410341,-6.576066,1.866529,-5.229803,-1.290841,4.198999,-2.199041,-3.576314,1.534091,-6.567158,-6.858022,-5.801286,-7.941189,-1.960598,7.041255,5.512525,8.051093,4.332920,8.130067,-6.835748,-4.343560,-6.160737,-7.097715,3.668537,-2.610714,6.070192,-9.788425,-9.196231,-3.788324,-2.186536,-5.999312,-2.070149,7.885738,6.702404,6.401430,-0.290755,1.782805,-3.445749,3.289852,-5.598500,0.910923,6.448672,2.384849,6.140190,-3.744198,0.509677,8.763980,-1.285490,9.924383,-6.593693,8.957996,0.166059,5.034997,8.005591,6.835033,-3.128015,8.079243,-1.717390,7.573651,-1.800854,3.745856,-0.998902,-3.035873,9.974908,-9.853519,-6.825898,-6.534928,6.650560,-0.537150,4.630009,-8.948201,-4.388567,9.496026,-7.912033,-5.603013,-4.067329,9.086598,8.034409,-6.452020,5.780189,-3.382612,-6.875536,0.509663,-3.333690,-5.755380,9.104683,5.669144,8.261439,-4.302949,2.107600,-8.984278,-5.464407,-3.583930,1.763358,-8.014830,-6.353367,6.711694,-6.053312,-8.147671,-9.715588,-2.229603,1.085459,4.912626,-5.652300,-3.230139,1.724337,1.886912,-7.100911,8.536687,-2.566741,0.067437,-3.077159,-5.483666,1.169802,4.119195,3.232405,-3.001197,2.396675,8.014041,6.524048,2.413426,7.901071,4.518808,-3.565752,3.959170,-2.887752,0.334705,5.258882,1.247567,-9.518305,-4.822166,-9.255162,-2.777270,6.269525,7.283173,-9.448782,4.286676,-4.272589,9.591175,7.893657,2.729099,9.565799,-9.970140,-0.118116,-7.158163,-3.667553,8.769339,4.476997,-5.399345,2.283692,9.907437,-7.346554,0.335822,6.830751,5.448272,-5.659184,0.472292,-2.542326,-9.423556,4.457873,1.523395,-3.826155,3.464658,7.308974,-8.729613,8.750309,-0.860701,-2.900849,-8.770732,-5.168371,-1.058816,4.362864,9.403946,6.599903,-8.273377,-8.199220,-2.077800,-4.055314,-4.792072,4.818125,4.750010,-5.581999,-5.822982,9.948975,7.571620,-6.238951,-8.526104,4.955552,2.557421,-9.594774,7.968301,-1.851102,5.754373,1.215903,-2.834506,-1.671173,-5.553387,0.975324,4.768392,6.153708,-2.641535,-3.085168,3.639454,-0.735555,-7.146746,5.090942,3.837442,6.966742,-0.742937,-2.947310,3.999107,-4.074990,-7.132791,-3.214682,5.927082,-9.086604,9.989756,-8.829786,-4.855987,-4.933632,9.353710,-7.484185,9.473424,6.716875,3.381708,-6.715912,-2.179870,-7.564074,-7.545097,-3.547729,-9.547169,8.899997,6.142830,7.783973,5.408000,-7.514798,9.675798,0.510003,-3.265254,-6.298018,1.174930,-2.280972,-4.429637,-0.060053,9.226788,-6.533805,5.737798,-6.117098,7.716396,-6.210669,7.912731,-5.534717,2.541385,9.924913,-1.681365,9.491373,-2.944458,-0.439853,-1.753501,2.111155,3.157235,-1.597963,0.061075,-1.189857,-1.868295,9.171606,6.162211,-3.639173,-3.985559,9.612665,3.840095,-0.623817,-0.270886,-7.351801,9.912451,5.826240,9.920678,5.095583,-3.236337,-4.252369,-3.565815,-3.534778,0.999067,-2.307907,-9.409571,-6.069133,8.771616,1.881085,8.522480,-1.422538,1.962217,-7.657893,4.450361,4.258108,4.715324,-7.458687,-0.774202,4.699707,8.561239,1.197101,9.441600,-1.707331,-6.932512,3.198366,8.226624,-5.906564,8.351040,-5.354525,-3.187023,-8.903806,2.462181,3.877578,9.116055,2.103437,-9.294607,-7.020926,-1.875773,-9.943704,-7.219191,7.022700,-7.364236,-9.303508,-0.082456,-0.396794,-9.776875,-0.865129,-8.466197,0.164274,-6.380455,-1.742791,8.785746,1.451351,1.254064,-9.628826,4.177686,-3.506802,7.004297,4.562311,6.136912,-6.739776,-5.924925,4.496338,-8.520035,-3.025339,6.995648,-8.638924,1.198237,-8.365616,0.759439,-0.141285,-3.386101,-8.211395,6.261240,1.352613,-0.003368,-3.006563,-0.253211,8.563292,9.596743,-4.113018,-2.656940,8.934842,-9.893426,3.829989,8.264916,-1.434116,-9.656745,7.889590,-0.335587,-2.548218,9.470609,9.373323,-0.157070,-7.182099,-3.748480,-6.025640,4.685919,-1.565499,8.051828,-9.441835,4.647191,9.896058,7.367332,2.761900,0.015014,-6.658799,-4.106474,3.097961,-5.531093,-0.991817,-7.721443,-1.374233,8.576012,2.432545,-1.667194,7.021453,-8.564784,2.746169,3.343396,5.960318,-4.036079,4.397450,0.595388,0.802557,5.305712,-4.905902,-2.069884,8.549834,5.419727,-5.655953,-2.866906,0.869357,-7.471049,6.192814,7.228606,5.565190,-1.460830,-2.371899,8.662987,-1.731715,-9.088422,-8.638923,3.174264,-3.733928,-3.600509,-3.890833,-4.974317,4.191910,-3.519955,-8.690937,0.435846,9.196324,0.100474,4.759843,8.843800,4.692221,-0.640162,-6.501343,2.377132,-8.453598,3.713658,3.371611,-2.405144,4.178793,7.802410,-4.670839,1.955031,-1.057517,0.136548,9.546346,4.668139,-5.161089,-3.478037,3.634493,2.159726,7.131884,-0.175042,-3.491774,2.963547,4.059501,-1.164584,0.780218,6.377413,-1.086242,9.643002,7.924252,-6.856805,-5.232473,-0.911388,-2.594028,2.835609,8.790397,-4.427499,-6.991467,1.871385,-2.764206,3.259841,9.702632,-4.345890,7.961830,9.328541,-4.558297,5.431738,-2.618520,4.090276,4.666028,-3.899040,-8.986887,7.254757,-0.677108,7.037247,-5.747105,-3.005848,6.014840,3.092782,-7.821486,-5.692148,-4.676143,9.435823,7.832971,4.541088,2.221728,8.617853,8.965107,-0.607324,3.072145,-9.449825,-7.117504,7.427238,3.365601,-7.144772,0.470913,9.613207,-2.186224,-3.660603,2.590614,9.688059,0.274336,-1.891059,6.580982,-2.146272,-4.633766,-9.065425,4.926070,0.745644,-4.927668,-5.425898,-4.206283,2.390914,-8.611385,-2.786840,5.792832,-3.562715,3.576518,8.706865,7.759967,4.537395,7.165265,-6.497668,-7.249675,1.535460,-5.112729,-2.597743,9.759436,1.658884,-6.430127,4.257834,8.619975,-3.248703,4.539843,7.412134,-9.923815,-8.705524,-1.026000,-0.380237,-1.346097,0.612035,-3.039912,4.822915,9.882930,0.573636,8.409795,-7.732769,1.484412,8.375683,-8.936430,4.429138,1.046657,-0.297450,2.004529,-6.964549,0.164667,-3.181498,-7.614385,3.450107,-0.043689,2.094110,-3.446944,3.525947,-6.300862,-9.182398,3.157641,8.009164,1.116212,4.784820,4.354878,2.128914,1.360556,-5.381738,0.405051,-1.471754,-8.670224,1.390991,7.263982,-7.644194,1.539938,-9.328847,8.607360,-0.159247,-0.475827,9.058047,1.308992,-9.509523,-4.633717,-7.255031,-9.333547,3.991199,-4.646103,7.977371,8.164346,-9.428985,-7.116421,-3.403536,-8.965565,3.666801,-3.176195,-5.045719,5.946811,-5.805049,8.586645,2.270003,5.577479,0.307575,-4.508676,4.485285,-0.682746,-7.799703,5.789818,-6.541546,1.183919,-1.359554,-2.541063,-5.908133,0.065177,7.882350,2.597172,-6.562974,-7.052219,0.751694,9.208573,-0.980079,-2.780860,-4.740468,4.208823,1.563896,-1.119390,-3.453451,0.036237,-6.686791,-0.680564,5.369456,7.767507,-6.239467,1.958311,-0.645016,9.551227,7.928472,8.019720,0.747623,-8.767541,-4.741105,-4.085678,-4.771806,9.625451,-3.371047,-7.756350,1.014541,6.213483,7.637221,4.382842,2.213459,9.382968,-6.884694,2.712613,2.392956,1.861957,-7.811256,9.122818,9.568162,-9.946907,-3.783462,5.183749,-4.853040,7.930499,-1.242911,4.183573,1.047402,-7.732700,6.713594,0.022548,4.050270,-5.865972,-5.696951,-8.008901,-2.758565,7.308315,-2.016562,4.351117,-7.837110,-0.300551,9.655418,-3.895898,-3.307543,0.124449,-6.516142,8.616975,4.202544,-6.123400,5.725129,0.822305,9.363120,-2.498378,6.337605,-7.626104,-0.146376,-8.934917,-8.127946,1.707301,9.874384,-8.247418,7.044774,-5.435419,-0.533603,3.825096,2.572649,0.618503,8.912467,-0.333337,5.445502,-7.962044,-6.457944,-8.207983,-6.810970,2.945800,-2.769332,9.147072,5.114321,-6.316744,-6.688807,3.050308,-3.473240,-6.478608,-5.532669,-7.645865,9.676060,-4.401645,-5.890652,-4.528590,-2.997501,-7.713992,-2.631775,-6.536371,4.230498,5.412074,-3.748788,-0.639599,2.500702,2.842022,2.305232,-7.122212,-0.259933,-3.574597,0.080247,3.904238,7.806991,-9.757843,-8.880013,1.207726,4.919699,9.252692,-0.776764,-5.409853,6.000608,5.684368,1.379863,6.630381,-0.195875,-4.969845,5.691910,0.689557,-5.551561,-6.088871,9.894354,-0.791104,-7.378639,-6.993890,0.954507,-1.992430,-9.410885,-3.405299,6.050480,-7.526441,7.403915,0.883095,-7.917766,4.080827,-5.601509,0.587039,-0.957304,-6.486642,-5.265937,6.492370,7.558360,-3.889277,0.838625,-2.240399,-6.575347,1.287033,0.856662,-8.172509,9.430434,-7.220289,1.854616,0.150185,-3.860992,-9.895047,3.610837,-9.186703,-5.686055,-0.882817,7.384107,-8.122758,6.642516,-6.950093,8.572041,8.202614,-3.546390,-1.314304,5.991765,7.688663,-2.241359,-1.144943,9.318641,-5.554592,6.387517,-3.333594,2.521227,6.869027,-8.268312,-4.782302,-1.062216,-0.564435,8.467687,3.310401,0.757220,-6.332130,-9.840132,8.855148,-8.822129,9.076637,-3.869302,-5.761743,1.173105,2.988261,9.033686,6.291820,1.909654,6.579662,-3.882905,9.984461,1.071849,7.772125,9.078431,-0.824501,1.739757,8.627351,0.257925,3.820919,6.378625,-2.171538,-7.923654,4.685941,7.656103,6.179688,8.218469,1.413033,-8.054359,-0.770541,8.977125,7.660369,6.735504,6.082108,6.235675,8.868814,5.129299,6.771260,9.300055,2.456421,2.262085,-3.079348,2.270921,-4.433083,0.054871,8.771144,4.789081,8.290998,-8.319293,2.307162,0.923185,-1.611755,-7.608923,9.094628,-8.118845,-9.133102,6.489720,-4.371302,0.397960,-7.561487,-9.774632,8.754625,9.655954,-3.124074,7.411012,3.416023,-9.362007,2.441097,5.061143,-8.726432,2.810213,-4.443119,3.553372,-2.617017,0.876052,3.026044,-3.879100,6.623313,5.969538,2.110040,2.795073,-6.854059,7.591463,-8.850893,-3.357394,-4.560634,8.768956,-4.266023,-9.323866,9.463188,4.895320,8.776395,-5.436491,6.827091,-9.112596,-7.836243,7.004457,4.168267,3.340786,-0.252223,-7.944599,3.636973,2.414751,-1.312467,-1.384221,9.301493,9.738776,-8.347472,2.676332,3.951093,-5.757871,5.375502,-5.521404,-6.932212,-0.945354,1.384517,-1.723905,-9.919753,-9.906970,5.096743,2.355600,7.277050,6.376668,-6.149294,5.611545,-4.913094,4.131483,-3.972551,-4.510002,5.436082,0.901725,1.298272,-3.164117,1.494404,-0.604957,0.679194,1.741233,-3.417685,-4.349318,5.190178,5.260421,-1.997993,2.966738,-9.993113,3.342410,-6.273146,9.758823,-5.914696,6.623992,-9.508433,-1.877204,6.090419,-9.047387,-1.790536,-6.789488,2.826187,8.752507,8.531330,-9.064343,-6.174321,0.276552,-1.775104,-0.164788,-8.860415,-9.401563,-7.533851,8.079430,-0.281968,7.266738,-4.744580,-0.580314,4.131421,1.526439,-1.643565,2.097036,-5.973056,2.012265,6.060890,4.936130,9.180717,-0.751381,5.358779,-4.601316,-7.572851,-1.372058,8.041700,-0.536910,6.439901,3.588749,6.780513,-2.198607,-2.856519,-1.874449,-9.300152,2.848986,2.914862,8.521449,5.791973,-9.344592,6.238741,6.271137,5.128698,-8.198763,2.216556,-1.182196,-4.584880,-1.816875,-6.549809,-4.916572,8.948414,-8.921430,7.222950,7.612054,7.206220,-7.468754,-7.212461,-8.029225,0.382697,-2.978047,-3.419843,1.470574,-7.420999,8.771882,-8.648576,9.357566,-7.004054,-9.954758,4.467615,-0.046194,9.425513,8.994662,-7.057614,9.595340,-0.664114,8.489975,-9.147908,4.068946,-5.725984,1.865273,-7.232524,-5.846897,7.869988,1.700333,-1.257472,9.462872,-0.815458,-4.536065,-0.948535,1.103805,9.847468,-6.178709,8.164548,-7.286396,-1.067265,6.783055,-9.911862,5.217046,-2.658016,-6.351310,3.918219,5.994544,0.038439,-8.194855,9.820781,-1.817258,-0.459269,9.994501,1.939012,-3.872363,3.858781,-8.156602,4.525161,5.669671,-4.804968,4.173891,-3.019395,-5.061357,-5.741423,6.001795,-2.589734,-3.313922,-8.557272,-4.391452,-1.769441,-0.665775,-8.579501,2.981121,-8.212697,-2.186849,6.325102,-4.852045,-8.807860,3.515685,-7.711823,-8.820061,-2.959054,6.044754,-7.132936,-1.770381,-8.694507,2.001535,-1.192313,4.622475,1.667777,3.885251,2.098794,-3.722695,-7.223660,-3.129616,4.782554,2.290764,0.043522,-9.975534,9.977024,-8.282054,1.103805,-9.800777,7.905970,0.019844,3.559222,2.316007,-8.971111,-8.326953,8.680788,2.948438,-1.077208,-7.974539,-1.288301,5.265717,-0.629077,2.248729,4.779432,3.751838,5.762180,-3.798731,5.928061,8.707484,3.160985,3.893776,-2.503441,8.661725,6.058683,4.287362,2.674744,7.001305,-6.145624,6.373528,1.524621,-0.679883,8.782023,6.327554,-4.194427,4.392478,8.743115,-5.388807,7.062508,-9.222663,-8.412906,-2.026383,-1.257568,1.862926,5.163965,9.858053,1.347168,8.155777,-2.434535,4.732499,-1.048680,-1.264962,3.449890,2.802319,4.978984,-7.756685,4.885651,3.869415,-0.227277,1.798418,6.673917,-7.668363,-9.561158,-4.789319,0.767131,-5.790925,-1.435268,8.263268,0.295128,-5.314999,-8.257207,-1.509357,-4.455343,6.871961,-5.915731,-1.590506,2.697393,-4.362287,-4.965278,-9.062598,6.680948,5.131186,-8.564831,8.538201,-7.252158,-4.758158,-1.935438,-9.735353,-3.032687,-3.010891,-8.846064,-1.611645,6.731466,-5.319861,3.782859,5.247914,6.241482,-4.301444,9.840711,9.082690,-6.405457,-7.058668,0.562105,6.660524,1.067814,-1.300640,-7.322236,9.148734,-2.720300,8.262230,2.465060,-4.755113,-2.917177,-3.868207,-6.739815,9.394273,0.841804,-9.767105,-7.120334,-2.461596,7.491042,-0.392303,5.464788,7.591671,9.094934,-2.738865,-2.672061,4.542400,6.327584,-4.970080,3.404166,-2.170790,-7.102192,2.417428,-0.627396,-7.338874,1.771018,5.751399,-9.822579,-6.530612,-5.662131,-1.684145,0.207632,4.894712,1.490042,-5.265390,4.779403,1.780355,4.351688,-1.268952,-3.769523,5.839694,5.464253,2.210141,-2.861470,8.205441,-8.686979,1.812853,5.113236,-2.528011,-6.831551,-9.738426,-5.323184], dtype = "float32")#candidate|5741|(1650,)|const|float32
call_5740 = relay.TupleGetItem(func_4957_call(relay.reshape(const_5741.astype('float32'), [11, 10, 15])), 3)
call_5742 = relay.TupleGetItem(func_4959_call(relay.reshape(const_5741.astype('float32'), [11, 10, 15])), 3)
output = relay.Tuple([call_5689,call_5708,const_5709,const_5710,call_5717,call_5732,call_5736,call_5740,const_5741,])
output2 = relay.Tuple([call_5690,call_5711,const_5709,const_5710,call_5718,call_5733,call_5737,call_5742,const_5741,])
func_5750 = relay.Function([], output)
mod['func_5750'] = func_5750
mod = relay.transform.InferType()(mod)
mutated_mod['func_5750'] = func_5750
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5750_call = mutated_mod.get_global_var('func_5750')
call_5751 = func_5750_call()
output = call_5751
func_5752 = relay.Function([], output)
mutated_mod['func_5752'] = func_5752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4334_call = mod.get_global_var('func_4334')
func_4336_call = mutated_mod.get_global_var('func_4336')
call_5756 = relay.TupleGetItem(func_4334_call(), 2)
call_5757 = relay.TupleGetItem(func_4336_call(), 2)
output = call_5756
output2 = call_5757
func_5758 = relay.Function([], output)
mod['func_5758'] = func_5758
mod = relay.transform.InferType()(mod)
mutated_mod['func_5758'] = func_5758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5758_call = mutated_mod.get_global_var('func_5758')
call_5759 = func_5758_call()
output = call_5759
func_5760 = relay.Function([], output)
mutated_mod['func_5760'] = func_5760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4281_call = mod.get_global_var('func_4281')
func_4282_call = mutated_mod.get_global_var('func_4282')
call_5767 = func_4281_call()
call_5768 = func_4281_call()
output = relay.Tuple([call_5767,])
output2 = relay.Tuple([call_5768,])
func_5770 = relay.Function([], output)
mod['func_5770'] = func_5770
mod = relay.transform.InferType()(mod)
mutated_mod['func_5770'] = func_5770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5770_call = mutated_mod.get_global_var('func_5770')
call_5771 = func_5770_call()
output = call_5771
func_5772 = relay.Function([], output)
mutated_mod['func_5772'] = func_5772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2765_call = mod.get_global_var('func_2765')
func_2767_call = mutated_mod.get_global_var('func_2767')
call_5780 = func_2765_call()
call_5781 = func_2765_call()
func_1975_call = mod.get_global_var('func_1975')
func_1977_call = mutated_mod.get_global_var('func_1977')
const_5790 = relay.const([3.822034,-3.116560,-8.155387,5.766910,-6.290582,-6.035268,-9.642822,0.676329,9.121449,1.997125,8.206446,-9.589550,-7.044308,8.789300,7.665392,-1.197053,-3.744552,4.413622,-9.166578,-9.884792,-7.682754,-8.280072,-8.187262,8.754573,3.963374,9.080516,-5.057716,5.293953,3.794335,-1.315494,-5.185025,8.563987,-4.674989,-3.298771,7.026767,1.231963,1.741219,-3.988572,1.494300,6.576957,-0.470688,0.563589,-9.899571,-7.545117,4.205632,5.875108,9.933577,-7.335536,4.292285,-3.180282,1.817325,9.859821,6.032339,-9.558284,2.006745,-7.259824,-8.920802,-4.082300,-8.790803,-2.697468,3.433426,-4.016756,2.269037,-3.933061,7.358954,6.647370,0.063581,1.617472,4.997090,0.169055,-3.745069,-3.930227,-7.574048,4.554579,8.843770,-2.973538,0.488604,-9.841251,-5.743968,-3.392276,3.096931,-2.535974,-9.817911,-4.955625,-1.785897,-0.044578,9.822045,2.882325,2.604196,-6.953981,9.139965,7.915210,6.087983,7.689249,0.983657,3.669258,6.241482,9.651509,-3.530814,3.689248,8.621612,8.542665,8.011685,-6.280952,8.395535,8.367230,-4.506811,-2.276049,-6.180226,7.358168,9.524384,2.321020,-4.746761,-4.358546,-9.648178,8.980983,5.465654,-4.434450,-2.824621,0.108215,9.438435,-5.198714,2.730318,-8.581418,-2.087126,4.849849,-9.133973,-9.592796,3.840064,1.586250,1.694159,-3.116664,7.121040,9.140276,5.318541,-1.615864,2.867938,-9.222210,3.479171,5.806178,-6.564075,9.388378,3.929599,-2.909703,-9.155610,-0.665693,-1.218329,-0.534521,9.905113,3.096912,-5.365093,6.928207,-0.622862,-7.032009,-9.034842,7.567713,5.399918,-2.044248,1.826169,2.165068,-3.673233,4.120433,-9.197562,3.210713,1.454434,7.075244,-5.935020,1.872172,-1.181325,-3.687835,6.812363,-3.456190,-4.654919,9.562394,4.663943,2.889887,-8.272958,-2.004451,-5.583930,-6.763526,6.729194,4.059076,3.735484,-9.856295,-0.365827,-5.495797,5.876707,-3.842544,6.793280,6.469228,8.170243,3.414514,8.257104,-0.644036,2.954056,5.898452,-6.011772,-1.381906], dtype = "float64")#candidate|5790|(198,)|const|float64
call_5789 = relay.TupleGetItem(func_1975_call(relay.reshape(const_5790.astype('float64'), [11, 9, 2])), 0)
call_5791 = relay.TupleGetItem(func_1977_call(relay.reshape(const_5790.astype('float64'), [11, 9, 2])), 0)
func_3965_call = mod.get_global_var('func_3965')
func_3967_call = mutated_mod.get_global_var('func_3967')
var_5793 = relay.var("var_5793", dtype = "float64", shape = (216,))#candidate|5793|(216,)|var|float64
call_5792 = relay.TupleGetItem(func_3965_call(relay.reshape(var_5793.astype('float64'), [216,])), 4)
call_5794 = relay.TupleGetItem(func_3967_call(relay.reshape(var_5793.astype('float64'), [216,])), 4)
output = relay.Tuple([call_5780,call_5789,const_5790,call_5792,var_5793,])
output2 = relay.Tuple([call_5781,call_5791,const_5790,call_5794,var_5793,])
func_5799 = relay.Function([var_5793,], output)
mod['func_5799'] = func_5799
mod = relay.transform.InferType()(mod)
var_5800 = relay.var("var_5800", dtype = "float64", shape = (216,))#candidate|5800|(216,)|var|float64
output = func_5799(var_5800)
func_5801 = relay.Function([var_5800], output)
mutated_mod['func_5801'] = func_5801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3775_call = mod.get_global_var('func_3775')
func_3777_call = mutated_mod.get_global_var('func_3777')
call_5826 = relay.TupleGetItem(func_3775_call(), 0)
call_5827 = relay.TupleGetItem(func_3777_call(), 0)
output = call_5826
output2 = call_5827
func_5848 = relay.Function([], output)
mod['func_5848'] = func_5848
mod = relay.transform.InferType()(mod)
output = func_5848()
func_5849 = relay.Function([], output)
mutated_mod['func_5849'] = func_5849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4499_call = mod.get_global_var('func_4499')
func_4501_call = mutated_mod.get_global_var('func_4501')
call_5889 = func_4499_call()
call_5890 = func_4499_call()
output = relay.Tuple([call_5889,])
output2 = relay.Tuple([call_5890,])
func_5900 = relay.Function([], output)
mod['func_5900'] = func_5900
mod = relay.transform.InferType()(mod)
output = func_5900()
func_5901 = relay.Function([], output)
mutated_mod['func_5901'] = func_5901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4907_call = mod.get_global_var('func_4907')
func_4909_call = mutated_mod.get_global_var('func_4909')
call_5902 = func_4907_call()
call_5903 = func_4907_call()
output = call_5902
output2 = call_5903
func_5905 = relay.Function([], output)
mod['func_5905'] = func_5905
mod = relay.transform.InferType()(mod)
mutated_mod['func_5905'] = func_5905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5905_call = mutated_mod.get_global_var('func_5905')
call_5906 = func_5905_call()
output = call_5906
func_5907 = relay.Function([], output)
mutated_mod['func_5907'] = func_5907
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5936 = relay.var("var_5936", dtype = "float64", shape = (5, 1, 16))#candidate|5936|(5, 1, 16)|var|float64
uop_5937 = relay.log2(var_5936.astype('float64')) # shape=(5, 1, 16)
output = uop_5937
output2 = uop_5937
func_5940 = relay.Function([var_5936,], output)
mod['func_5940'] = func_5940
mod = relay.transform.InferType()(mod)
mutated_mod['func_5940'] = func_5940
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5941 = relay.var("var_5941", dtype = "float64", shape = (5, 1, 16))#candidate|5941|(5, 1, 16)|var|float64
func_5940_call = mutated_mod.get_global_var('func_5940')
call_5942 = func_5940_call(var_5941)
output = call_5942
func_5943 = relay.Function([var_5941], output)
mutated_mod['func_5943'] = func_5943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4731_call = mod.get_global_var('func_4731')
func_4732_call = mutated_mod.get_global_var('func_4732')
call_5972 = relay.TupleGetItem(func_4731_call(), 0)
call_5973 = relay.TupleGetItem(func_4732_call(), 0)
output = call_5972
output2 = call_5973
func_5986 = relay.Function([], output)
mod['func_5986'] = func_5986
mod = relay.transform.InferType()(mod)
output = func_5986()
func_5987 = relay.Function([], output)
mutated_mod['func_5987'] = func_5987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5447_call = mod.get_global_var('func_5447')
func_5448_call = mutated_mod.get_global_var('func_5448')
call_6007 = func_5447_call()
call_6008 = func_5447_call()
func_3353_call = mod.get_global_var('func_3353')
func_3354_call = mutated_mod.get_global_var('func_3354')
call_6015 = relay.TupleGetItem(func_3353_call(), 2)
call_6016 = relay.TupleGetItem(func_3354_call(), 2)
var_6019 = relay.var("var_6019", dtype = "float64", shape = (5, 70))#candidate|6019|(5, 70)|var|float64
bop_6020 = relay.power(call_6015.astype('float64'), var_6019.astype('float64')) # shape=(5, 70)
bop_6023 = relay.power(call_6016.astype('float64'), var_6019.astype('float64')) # shape=(5, 70)
output = relay.Tuple([call_6007,bop_6020,])
output2 = relay.Tuple([call_6008,bop_6023,])
func_6031 = relay.Function([var_6019,], output)
mod['func_6031'] = func_6031
mod = relay.transform.InferType()(mod)
mutated_mod['func_6031'] = func_6031
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6032 = relay.var("var_6032", dtype = "float64", shape = (5, 70))#candidate|6032|(5, 70)|var|float64
func_6031_call = mutated_mod.get_global_var('func_6031')
call_6033 = func_6031_call(var_6032)
output = call_6033
func_6034 = relay.Function([var_6032], output)
mutated_mod['func_6034'] = func_6034
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6060 = relay.var("var_6060", dtype = "uint16", shape = (8, 14, 5))#candidate|6060|(8, 14, 5)|var|uint16
var_6061 = relay.var("var_6061", dtype = "uint16", shape = (8, 14, 5))#candidate|6061|(8, 14, 5)|var|uint16
bop_6062 = relay.greater_equal(var_6060.astype('bool'), relay.reshape(var_6061.astype('bool'), relay.shape_of(var_6060))) # shape=(8, 14, 5)
uop_6069 = relay.erf(var_6060.astype('float32')) # shape=(8, 14, 5)
uop_6076 = relay.sigmoid(uop_6069.astype('float32')) # shape=(8, 14, 5)
bop_6078 = relay.greater(uop_6076.astype('bool'), relay.reshape(bop_6062.astype('bool'), relay.shape_of(uop_6076))) # shape=(8, 14, 5)
output = bop_6078
output2 = bop_6078
func_6089 = relay.Function([var_6060,var_6061,], output)
mod['func_6089'] = func_6089
mod = relay.transform.InferType()(mod)
mutated_mod['func_6089'] = func_6089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6089_call = mutated_mod.get_global_var('func_6089')
var_6091 = relay.var("var_6091", dtype = "uint16", shape = (8, 14, 5))#candidate|6091|(8, 14, 5)|var|uint16
var_6092 = relay.var("var_6092", dtype = "uint16", shape = (8, 14, 5))#candidate|6092|(8, 14, 5)|var|uint16
call_6090 = func_6089_call(var_6091,var_6092,)
output = call_6090
func_6093 = relay.Function([var_6091,var_6092,], output)
mutated_mod['func_6093'] = func_6093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4879_call = mod.get_global_var('func_4879')
func_4881_call = mutated_mod.get_global_var('func_4881')
call_6111 = relay.TupleGetItem(func_4879_call(), 0)
call_6112 = relay.TupleGetItem(func_4881_call(), 0)
func_3550_call = mod.get_global_var('func_3550')
func_3553_call = mutated_mod.get_global_var('func_3553')
var_6115 = relay.var("var_6115", dtype = "float64", shape = (198,))#candidate|6115|(198,)|var|float64
call_6114 = relay.TupleGetItem(func_3550_call(relay.reshape(call_6111.astype('float32'), [13, 2, 6]), relay.reshape(var_6115.astype('float64'), [1, 198]), ), 6)
call_6116 = relay.TupleGetItem(func_3553_call(relay.reshape(call_6111.astype('float32'), [13, 2, 6]), relay.reshape(var_6115.astype('float64'), [1, 198]), ), 6)
output = relay.Tuple([call_6111,call_6114,var_6115,])
output2 = relay.Tuple([call_6112,call_6116,var_6115,])
func_6120 = relay.Function([var_6115,], output)
mod['func_6120'] = func_6120
mod = relay.transform.InferType()(mod)
mutated_mod['func_6120'] = func_6120
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6121 = relay.var("var_6121", dtype = "float64", shape = (198,))#candidate|6121|(198,)|var|float64
func_6120_call = mutated_mod.get_global_var('func_6120')
call_6122 = func_6120_call(var_6121)
output = call_6122
func_6123 = relay.Function([var_6121], output)
mutated_mod['func_6123'] = func_6123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4731_call = mod.get_global_var('func_4731')
func_4732_call = mutated_mod.get_global_var('func_4732')
call_6143 = relay.TupleGetItem(func_4731_call(), 0)
call_6144 = relay.TupleGetItem(func_4732_call(), 0)
uop_6152 = relay.asinh(call_6143.astype('float32')) # shape=(13, 2, 6)
uop_6154 = relay.asinh(call_6144.astype('float32')) # shape=(13, 2, 6)
bop_6161 = relay.logical_and(uop_6152.astype('bool'), relay.reshape(call_6143.astype('bool'), relay.shape_of(uop_6152))) # shape=(13, 2, 6)
bop_6164 = relay.logical_and(uop_6154.astype('bool'), relay.reshape(call_6144.astype('bool'), relay.shape_of(uop_6154))) # shape=(13, 2, 6)
output = bop_6161
output2 = bop_6164
func_6165 = relay.Function([], output)
mod['func_6165'] = func_6165
mod = relay.transform.InferType()(mod)
mutated_mod['func_6165'] = func_6165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6165_call = mutated_mod.get_global_var('func_6165')
call_6166 = func_6165_call()
output = call_6166
func_6167 = relay.Function([], output)
mutated_mod['func_6167'] = func_6167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4471_call = mod.get_global_var('func_4471')
func_4472_call = mutated_mod.get_global_var('func_4472')
call_6168 = func_4471_call()
call_6169 = func_4471_call()
func_1707_call = mod.get_global_var('func_1707')
func_1714_call = mutated_mod.get_global_var('func_1714')
var_6176 = relay.var("var_6176", dtype = "int16", shape = (288,))#candidate|6176|(288,)|var|int16
const_6177 = relay.const(6, dtype = "uint8")#candidate|6177|()|const|uint8
const_6178 = relay.const([-8,-9,-7,-10,-8,4,10,-10,10,-7,-2,6,-5,-6,-6,9,7,6,-9,-4,-7,-4,4,4,-4,5,-3,2,7,-9,6,6,-8,-7,9,3,-10,7,-3,-8,-3,4,3,-6,-5,3,4,7,2,-8,-5,-6,-10,-9,-3,9,-1,4,9,6,4,7,9,-10,8,-9,-9,-8,-10,-1,5,9,-2,-9,10,7,5,1,-8,4,-9,8,1,-8,-2,-4,-10,2,5,-7,7,10,-7,-9,-4,-8,-7,2,2,-9,-10,1,5,5,5,6,3,-7], dtype = "uint8")#candidate|6178|(108,)|const|uint8
call_6175 = relay.TupleGetItem(func_1707_call(relay.reshape(var_6176.astype('int16'), [6, 4, 12]), relay.reshape(var_6176.astype('int16'), [6, 4, 12]), relay.reshape(const_6177.astype('uint8'), []), relay.reshape(const_6178.astype('uint8'), [6, 18]), relay.reshape(const_6178.astype('uint8'), [3, 36]), ), 6)
call_6179 = relay.TupleGetItem(func_1714_call(relay.reshape(var_6176.astype('int16'), [6, 4, 12]), relay.reshape(var_6176.astype('int16'), [6, 4, 12]), relay.reshape(const_6177.astype('uint8'), []), relay.reshape(const_6178.astype('uint8'), [6, 18]), relay.reshape(const_6178.astype('uint8'), [3, 36]), ), 6)
output = relay.Tuple([call_6168,call_6175,var_6176,const_6177,const_6178,])
output2 = relay.Tuple([call_6169,call_6179,var_6176,const_6177,const_6178,])
func_6188 = relay.Function([var_6176,], output)
mod['func_6188'] = func_6188
mod = relay.transform.InferType()(mod)
var_6189 = relay.var("var_6189", dtype = "int16", shape = (288,))#candidate|6189|(288,)|var|int16
output = func_6188(var_6189)
func_6190 = relay.Function([var_6189], output)
mutated_mod['func_6190'] = func_6190
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6195 = relay.const([[[-7.653790,4.654240,1.469531,-3.528144,0.926204,-8.296531,5.955611,-8.654683,6.896434,4.895325,-1.620140,-6.580769],[3.882746,1.175693,7.388586,2.841050,-8.051254,-2.521565,2.075605,6.507064,-8.896105,0.854341,0.961528,-9.356203],[-0.980280,-9.381355,7.776451,7.926020,-6.995441,-6.397290,2.323984,4.975891,-7.649979,-5.573605,-6.153423,-6.398644],[1.718981,-1.241256,-2.392067,-4.361440,1.201672,4.914522,9.459503,4.932051,6.780472,6.449915,1.326530,3.183931],[-5.080078,4.722236,9.008855,1.014145,-4.467896,-9.378660,-4.640213,6.133816,4.602607,3.746586,1.846701,-0.245381],[-8.310538,-8.726524,1.296794,-8.699189,9.572952,-7.389785,1.634296,8.021308,-8.993176,-7.671550,-8.166629,-2.918341],[4.848646,-6.957056,-7.974513,1.620724,-9.402995,1.425838,7.022534,8.697554,2.208976,-8.961325,7.695264,-0.592569],[0.252876,7.167697,-6.608974,2.204187,2.875059,0.772502,1.856979,-6.485913,-5.104741,5.011373,1.133116,-2.078616],[-8.644883,-3.107035,-3.047605,8.443768,8.454677,-7.623489,-5.293825,9.348050,4.149205,-8.178265,-8.792848,4.675856],[-0.832001,-1.392632,5.371231,-3.089814,1.975064,-1.436951,-5.821464,7.407318,-4.060880,7.733642,-0.713119,-8.652757]],[[2.790017,-9.724424,8.150408,-4.496831,-5.430760,-6.136437,2.661725,6.247633,0.689290,1.092533,-9.392490,8.392983],[-9.305711,6.345975,-7.143641,-3.254717,-4.582626,0.498419,-7.942457,5.739700,-7.671586,4.655094,1.819696,0.432171],[-2.444397,-1.712462,0.005058,8.913741,-8.457173,-5.547203,-4.989421,5.266620,0.249901,-1.267443,-8.018028,-9.844676],[5.550473,4.711567,4.430406,3.384235,8.891161,-7.012058,-0.561482,-5.556617,-1.853306,6.868200,3.989327,-1.843660],[3.195276,7.921360,-7.143879,-8.989016,6.137176,-8.939539,-3.605199,-5.974449,6.934148,5.934983,-2.991826,4.605609],[-5.395901,7.426615,7.183026,5.978532,-4.859463,-7.317028,-1.738353,8.778738,-1.225123,-6.915045,2.036049,-5.204647],[5.875205,-8.055208,8.823940,4.275034,-4.450750,-0.874326,-2.657559,-8.497646,-1.230109,8.096866,-4.748368,-1.766095],[2.694315,1.861330,9.998790,8.829679,3.805434,-4.770144,9.390789,8.308601,-6.878592,7.898560,7.377540,2.013935],[4.498282,-3.558327,7.782990,-3.572503,-5.084876,-3.991456,-6.414759,-5.080397,5.155651,-3.665794,-3.649298,8.419964],[6.733541,1.719361,-7.497142,-8.307368,-8.469045,8.553347,2.609787,-6.471864,-8.880836,2.505330,-8.723445,-7.401954]],[[-9.829052,1.084514,-0.326945,7.640823,4.961993,-6.356194,-6.726171,2.877681,-9.829068,-3.329787,0.493558,8.349827],[7.152486,-1.956728,-9.476292,-4.487131,3.376149,-6.783347,-6.451737,-6.759825,-1.614144,2.010350,8.284392,7.847670],[-9.231940,-3.961882,-8.353097,1.887873,-7.602784,-9.225598,-1.374305,-6.017281,-4.051792,-4.393997,-6.778179,-1.198615],[7.208955,4.556759,8.517362,-9.737892,8.910911,5.081912,-9.943704,5.900140,-4.517606,-4.549582,-1.672045,-2.709810],[7.142468,2.555083,0.905919,-2.069301,-7.412167,-8.000641,3.927512,1.523216,6.068822,-4.862543,0.839255,-4.146898],[7.206908,-1.686592,5.674308,-0.321508,4.047686,5.907179,-8.028931,-5.283653,8.938019,-9.767020,4.308500,6.187052],[-8.725819,6.545907,-9.172651,9.233243,-6.028884,8.090026,-4.710474,-4.574671,-9.241584,1.101526,9.269822,8.962170],[-6.149154,7.636272,3.151958,-6.385440,6.090063,4.399322,8.591794,9.698434,-6.837600,-8.368692,0.779481,7.110400],[-9.780090,-3.687592,-0.344088,-0.906111,5.818383,-8.145367,2.456027,-4.772282,-7.256219,-5.931732,-1.615800,2.851069],[-1.633298,7.158854,-2.387485,9.599255,1.332262,9.920485,4.804592,-6.041206,5.846439,2.250603,9.808016,1.986021]],[[7.873228,-0.182572,-8.952348,5.142855,7.497606,-9.280601,7.016126,-9.201072,6.271549,-2.042123,7.073754,1.756120],[7.839431,8.086855,-6.001868,9.456115,-4.271887,5.715869,1.219264,-6.239129,6.005805,8.688936,-7.603379,-4.754904],[9.712569,9.182482,4.338488,9.877417,9.427313,-6.333111,-7.241796,-3.423492,3.701605,8.302114,-0.180974,1.498565],[-7.344520,-0.024629,-9.459255,-9.040465,0.873365,-6.480530,-0.503025,2.744275,3.093587,9.376792,3.284340,-4.858875],[4.539591,-6.707625,2.213935,1.219434,-6.887876,5.232157,-1.822545,-5.431550,3.497879,2.858953,-8.290814,3.758515],[-3.476751,9.864376,-3.529384,-6.498689,3.873836,3.291573,-4.553953,-1.361293,-8.353267,5.981172,5.678024,-7.726861],[-6.292951,-9.757792,0.673377,-0.188579,-2.336049,2.026395,-8.913566,-4.153374,-1.412762,-8.747460,8.353321,4.139949],[-1.667079,-1.682832,-5.178950,-2.618228,-7.332947,-4.920163,0.677638,6.855327,-8.085115,-2.458723,-9.928482,0.234872],[0.773102,5.634857,-2.039792,-1.209306,4.221009,6.987417,-2.245265,2.736881,-6.210171,-3.767924,-2.541798,-9.193159],[-7.960029,9.540339,3.840725,-2.259570,4.449159,8.371541,-0.167453,-2.669356,2.790782,-4.787773,-5.430308,-4.490031]],[[7.704425,-8.842301,0.778681,-5.885246,2.410204,-6.732432,-0.963548,7.709466,5.063847,-3.577814,5.958055,7.718910],[-3.297908,-6.770638,1.036630,0.711643,2.842851,6.959243,-0.401894,-5.423525,7.362065,6.401849,4.586888,3.499659],[5.050974,2.074315,3.603670,4.057271,-7.924362,-3.679672,4.875947,-4.344467,8.744703,2.631761,2.600627,2.704118],[-0.268302,2.645597,-1.903490,-6.255320,-6.642776,-1.123039,5.408684,9.878732,7.845168,2.355173,8.436492,8.078731],[3.669930,3.765976,-2.148067,-0.498866,9.760212,4.865794,-1.098647,7.208880,1.746081,-9.329092,-8.656427,-6.161694],[3.042709,-7.178473,6.950316,9.722488,-3.351222,4.228298,-6.450624,1.038866,0.293106,7.822215,4.124482,-3.024482],[-3.747620,6.983451,-7.559700,-1.284728,4.167350,1.889395,-8.277078,-0.037098,3.331763,1.745685,8.446028,6.953948],[1.960757,-8.828070,9.007973,4.918422,-5.081195,-9.012161,-2.805265,-2.751964,4.596433,-0.860304,3.557932,-8.505590],[6.005030,-3.332266,5.809940,1.122376,-7.129752,6.452510,8.840288,0.510120,9.497306,-0.855505,-6.272364,5.178155],[-4.686465,9.404187,-5.132638,-0.446500,6.407872,-2.805836,-9.406994,-7.835702,-6.669845,8.131230,-5.410548,7.217402]],[[-6.764386,-5.338285,-6.628440,1.765772,2.304474,-0.897507,-6.676247,2.312785,9.831885,-6.162814,-7.481391,-8.762313],[-0.463932,-2.390969,-3.927169,-6.673475,9.181982,5.440012,1.317371,4.295259,7.728061,-6.667060,-2.188364,-8.165248],[-9.311415,-7.033508,4.524202,9.409123,-8.206631,-6.227674,2.912872,4.806459,9.955859,-4.361841,7.276209,-9.633103],[-7.419847,9.295406,-0.202777,-6.888826,-5.782738,3.831881,-4.241979,-7.189372,-4.676367,5.724027,3.345541,9.699732],[-4.972321,5.021439,4.760691,-0.044671,6.480568,-1.186652,5.415107,-0.838289,8.730277,6.255404,-8.154762,-3.777319],[5.196361,-9.750419,6.801017,4.703189,2.342097,2.885978,-8.191623,-4.753715,3.346963,-8.241554,-9.919431,6.488756],[-7.771746,8.898020,-9.304930,-6.552886,3.213490,-2.716942,-4.129669,-0.706680,3.888918,-8.562420,-0.465577,2.428120],[9.035136,-8.269973,-7.142608,-2.687398,7.674966,2.779213,3.794890,2.395676,-4.228428,7.787202,3.523875,-3.333137],[-9.202666,1.864338,-6.217380,-5.935896,-4.774202,4.524542,-6.922883,4.353217,9.297520,0.324212,-6.505031,6.236450],[4.534291,0.261798,9.215255,8.638836,-2.140764,-6.899554,8.857879,7.174790,0.897479,-4.057472,-1.165308,0.948031]],[[-3.063867,-8.290611,0.352105,9.054684,9.289260,-3.711410,-8.678395,-1.887357,-9.171087,9.678503,2.540713,2.911958],[6.675031,0.945072,1.829080,1.571539,1.920408,2.035656,-3.110346,8.154169,3.281078,-4.912765,7.367011,0.277606],[4.611706,8.114927,6.800500,5.622268,-1.108530,-1.939680,-7.010085,1.665172,2.181419,-3.139025,8.881993,4.476422],[6.015139,4.207656,-9.297443,-1.185355,9.409349,1.549820,-5.844232,-1.312318,9.318840,4.865037,-3.062948,1.977760],[3.202141,0.976340,-3.050381,9.291210,-5.531180,-0.447251,7.838721,-5.452754,6.903288,1.538626,7.045443,-1.985346],[-3.447912,-2.326837,9.361357,3.691418,5.600988,9.775756,3.363563,-5.136152,7.695424,4.770843,4.875022,-3.767017],[1.262799,8.253154,3.266525,2.379082,8.428870,-1.411333,4.320789,3.803384,8.464408,-6.193812,6.591262,-5.507065],[-2.242545,-1.984162,-6.234831,-8.691303,-1.517745,-6.435532,6.099163,-5.780909,5.673515,4.367857,-3.300659,0.553659],[-9.512890,-2.222501,-9.143721,-2.625619,-5.861975,6.790136,9.264871,-3.950840,7.751728,5.630417,-4.651518,1.520331],[1.838379,0.542151,3.400380,8.965973,-5.473362,1.894150,-9.377334,9.292114,-8.940280,7.450453,-1.783897,-3.694535]],[[-2.263350,2.963882,8.257216,-9.146817,6.654137,-4.730380,3.067873,-2.090248,7.923445,-0.782863,-1.507996,5.587407],[-7.785465,-1.940547,-4.728473,-2.186599,9.881221,-2.596034,-9.880284,5.187770,-0.368728,-9.764431,6.252762,7.673641],[6.309087,-3.851006,-6.876859,-4.485621,1.528803,6.811360,0.051424,-5.251946,1.047432,6.071745,-7.415218,-7.163101],[-2.913968,-9.978286,5.363863,2.759294,1.271028,-0.610475,5.795303,5.251143,-2.558491,-7.962566,-4.115137,-9.773025],[8.439629,-6.445933,-1.310935,-2.880705,7.450735,-9.331530,7.215712,8.503496,0.205897,-7.899094,8.830537,1.845750],[-8.986731,7.032877,2.531451,8.989242,-7.045506,-2.711828,-2.471206,3.823389,9.146528,-2.827262,1.066217,5.181401],[-1.839222,7.337592,1.311815,3.620633,2.838766,7.548709,-5.938953,5.156984,-9.207377,8.035763,2.142792,-5.519479],[-4.833001,7.765356,6.491075,-1.389891,-5.842573,6.789048,9.106051,2.540155,7.859198,3.491371,9.214419,-9.595668],[-5.514345,-4.632251,5.189806,-4.408664,-3.459052,0.089391,-8.789453,8.253820,-6.954027,3.509427,5.501534,-7.965270],[6.817495,-1.338621,-5.867347,-6.160346,-3.410704,-8.455676,1.803950,5.153662,-7.831057,1.096054,-9.600733,4.868566]],[[0.628490,-7.471854,-2.153734,-0.844986,-2.914853,-1.852591,7.454911,5.871634,-8.049349,7.163138,-0.433833,3.216147],[-9.605506,-9.712598,3.539872,0.129148,-9.019202,5.915732,-7.106662,-5.532761,-2.647848,2.628415,0.737486,8.390042],[4.151648,1.946601,5.944717,-2.819857,-9.770229,-4.317205,6.204762,-5.898718,-0.339562,-9.934247,0.023266,4.508598],[4.166875,-8.897530,-4.515839,-5.838466,-6.181718,9.549227,-3.239145,4.276464,-3.902738,-8.841984,4.092543,1.034341],[-9.341016,-9.978997,-0.182975,3.088830,2.375774,-0.449529,3.663885,6.334262,8.078233,2.260759,-8.594364,-6.550849],[3.625902,-8.072540,1.207935,-9.423464,6.513734,-4.246806,-1.088178,-7.324504,5.052294,0.474658,2.862688,-2.073075],[-5.295040,1.419247,0.150019,8.908356,-8.792049,7.642952,-9.753675,-9.578656,1.395011,3.865974,-1.069595,9.855896],[1.743789,6.052436,7.984422,8.179140,8.307072,-4.900731,-2.096609,3.503538,-6.218202,-5.567091,-7.087211,-3.626204],[7.628720,-6.312460,2.913320,2.483469,-7.653231,-7.880766,6.882745,6.761352,-1.213887,7.146992,-0.304363,3.525723],[6.893131,6.510336,-4.012417,6.279193,2.677116,-3.823398,5.089566,6.416604,-8.211179,8.287668,3.660314,-4.193194]],[[8.114653,-0.978039,2.090646,-6.465501,-5.327851,-0.317476,3.257553,-5.087748,7.379780,-2.454261,9.816427,9.477241],[8.700858,4.506516,3.131341,-4.559429,7.896504,-1.692517,-1.278189,9.314593,-9.926567,-6.078743,-0.940777,7.698759],[1.873449,-9.119972,2.015907,-0.587111,7.661524,-2.705361,3.540184,7.564563,1.102671,3.831444,-7.497057,-0.590666],[0.828738,-9.178797,-3.140866,7.367191,8.298200,-4.063704,5.097648,7.041841,-6.219402,-2.186865,-1.904574,-4.881089],[1.871274,-4.507668,-5.831034,0.259154,2.431364,2.663693,5.050327,0.816988,2.595960,6.039772,-8.522021,3.146407],[-2.064115,-4.290664,7.374260,8.737983,3.309935,-3.902981,-6.287404,8.994746,5.883330,0.907282,5.773806,-7.720312],[-5.662077,-8.005472,-8.586598,6.436621,6.902887,-3.369949,-7.136621,9.957274,4.802051,-3.337714,9.253111,7.538119],[-3.873454,4.967534,5.959730,-9.616914,-1.929900,-4.762279,-4.254682,0.895040,9.049896,-8.313978,0.571136,0.742411],[4.629991,7.594790,1.077089,-8.464766,1.094016,-4.562412,2.574247,6.718831,4.606928,-7.361717,9.241248,2.045184],[9.154400,6.899594,5.959421,7.969086,-4.655791,-1.969410,9.471034,5.376691,-8.791353,5.880901,7.271104,1.445752]],[[-5.548749,-8.670287,-0.161660,3.699271,-8.406471,-5.464471,8.267261,-0.396767,-9.601814,-5.191691,1.526197,0.770559],[1.074912,4.760826,2.047329,5.949950,8.581473,1.465799,7.817996,4.308874,8.957999,9.535004,-0.086936,-9.791723],[-5.881401,-9.747126,3.594280,-5.471614,3.247840,6.980519,-3.168969,-6.082167,-6.209817,6.134316,-5.013315,8.312570],[5.945491,7.247702,1.835463,-6.938908,-2.566540,8.127398,-2.258247,-2.281386,-8.379744,-6.424829,-6.095163,-0.241236],[1.501463,-0.516679,-7.329896,0.153948,-1.198458,9.572438,1.705308,-6.088237,8.361762,2.077085,6.069780,9.100624],[3.832968,-8.982678,-5.841678,-8.632280,6.140705,-6.148766,7.583239,7.232797,-2.469378,7.353890,-2.194951,1.928233],[5.573173,-0.810217,-2.536025,-9.841135,2.728159,9.939419,9.213195,9.685243,-3.030276,5.121985,-4.206315,1.257070],[6.078141,-9.871579,-0.521070,9.516602,-6.549624,-8.015004,8.857711,-3.312539,-1.692284,3.616613,8.628515,-9.878405],[-8.860301,0.690157,-4.040048,0.518545,8.623733,7.590902,4.413299,-3.796791,-9.906553,-5.133536,4.021191,0.031359],[-0.130509,-4.346789,5.738400,8.457871,-0.171692,-1.395296,9.747515,-7.506945,8.719486,3.503265,2.210462,-5.552855]],[[-9.414737,8.388531,6.455971,2.476953,7.509845,-6.561929,-8.339143,-4.211168,-4.003336,6.215841,-4.546512,2.965117],[-7.163433,-2.798982,-1.168336,7.668823,9.515373,-1.791597,1.773555,-7.802805,1.614810,-2.220593,-3.868699,-6.115002],[3.526961,6.129763,-5.447973,-5.380014,5.414058,-6.725983,8.177457,-5.488819,-7.782504,-2.432036,3.095831,0.635213],[7.846525,-6.849250,-9.274685,-7.999261,9.061553,-0.822792,-8.580282,-3.604057,8.926949,3.235387,-8.793689,-5.108991],[7.042910,3.812568,0.465535,5.612009,-8.504093,2.450064,8.052017,-3.848175,5.790762,-1.428871,9.563150,1.485482],[7.832760,-9.317517,-5.077044,-0.004320,3.369295,-0.275160,-8.315895,8.309786,-9.058927,-1.153719,-9.345271,-7.148216],[8.188101,-6.387117,4.544002,0.252772,-0.645238,-5.973032,-0.552519,-0.671338,-1.000726,5.737106,9.861390,1.184483],[5.035162,4.440944,8.201097,8.127849,-6.817378,2.767442,9.206404,-3.971438,-8.170279,-1.394462,5.026959,-5.307433],[-1.895230,2.555415,-2.480915,6.502327,-0.952297,-5.310683,-8.066721,-4.399035,2.951940,-7.046191,-1.636371,-1.803158],[0.136643,-1.066675,-1.086611,6.973336,-7.019810,-7.853322,8.480100,-1.929811,-2.067759,4.193199,-6.725266,2.642177]],[[-9.034730,-9.977541,-4.922462,6.958809,6.860437,-2.229731,6.605292,-5.728143,-3.849612,-3.496234,-5.096711,9.760693],[7.104982,2.783502,-7.579704,8.380549,-5.496129,-3.262954,2.646075,2.986762,8.848695,-1.046099,4.052544,-8.235571],[1.564354,2.336146,4.682395,-9.084157,-9.732485,-5.630442,-1.678330,9.445731,8.360350,1.235607,7.941306,7.288104],[-1.775377,8.014668,4.794257,-6.162007,5.757088,-6.633293,-9.961925,1.225279,9.549742,-2.701991,-8.797015,-8.498093],[7.251562,-3.211487,-9.469238,4.389051,5.946880,-0.372613,-8.030389,2.181203,9.350164,-5.959342,-6.753276,-7.929756],[1.702702,6.717589,-1.730615,9.143480,6.481287,-6.126092,7.934092,-4.771894,3.387665,0.322486,9.439505,1.490321],[2.560256,4.298760,7.655877,1.879995,-9.955387,-9.354741,-9.958530,-8.230135,9.009270,-6.200902,-1.806274,8.005149],[1.493332,6.990011,8.496458,2.862965,-7.071449,-5.455240,-1.985223,-9.332572,-5.701863,3.471997,-4.339235,-5.509945],[0.335225,-5.453714,-7.335553,7.447416,1.964258,-1.605111,1.566624,8.653074,-6.621733,2.373213,2.300629,0.499138],[3.219036,-4.254527,-7.978597,7.960274,5.750444,1.128040,-5.606605,-3.451266,6.305168,-5.584582,-5.135437,-4.588206]],[[-1.312070,-0.043975,2.871296,0.059456,-2.193309,-6.320305,9.082464,-6.949222,-6.721156,-2.447687,-1.801098,-4.074903],[6.554561,-1.719054,-8.698845,2.080006,1.589579,-2.936867,9.534307,7.152615,4.631163,6.028364,7.416413,-7.124537],[8.250134,-2.368362,8.940137,-3.380966,-5.285862,-6.515995,4.021343,7.442878,3.038227,-0.382007,5.778114,3.699914],[3.068819,1.290289,-3.590439,-0.601463,-3.561341,-2.300232,3.898665,5.396169,0.894970,-1.078760,4.550036,4.080916],[5.895123,2.641852,7.350297,-2.001055,1.566822,-6.081782,9.853320,-4.346901,9.011563,9.664355,5.892593,-0.406386],[-3.686783,5.050389,-9.644249,6.622055,-3.443075,8.414610,4.976139,0.848686,2.154663,-6.037998,-9.747467,8.865475],[7.723768,6.064890,4.403039,-5.974599,-1.187149,7.424775,-6.256273,7.741964,4.278377,8.331248,-9.132839,-5.828226],[-9.865997,-3.825198,8.180902,-1.623481,-7.434237,9.859976,-7.382740,7.791382,8.649407,1.115550,9.805880,4.887531],[2.110267,2.381374,0.559554,-7.537500,5.646580,-8.998504,-8.083961,6.651047,-6.234397,-6.181355,-2.103847,-0.475772],[-8.129188,-5.438296,-2.214563,-9.783032,-0.898098,1.871135,5.610323,4.712754,-5.544719,8.691472,-7.797453,6.127988]],[[9.603734,5.788315,5.117741,-0.753095,-1.878924,-1.079898,-7.174552,-9.081028,-0.824383,-1.521389,2.622643,-4.296123],[0.915208,-5.909781,9.257103,9.592868,5.570018,-1.416550,-9.977214,-4.282660,2.159805,9.188525,-9.665248,-9.498848],[6.847378,-8.863278,-3.948290,-7.017672,0.804270,-4.295074,-7.036908,2.094694,-5.104184,-5.680328,-9.615579,2.331242],[5.427121,2.023107,6.796953,8.067972,-5.061974,8.918783,-8.100490,9.811140,3.955409,-9.673187,1.825543,4.260294],[-6.411402,-2.616303,6.972993,-4.183091,-6.287432,-0.292823,-9.467613,-2.024222,8.341995,6.535261,2.675630,5.471529],[-4.637605,-3.238485,-5.271320,-0.669653,4.333266,9.610586,-6.515882,-9.795096,-8.896482,-9.372418,-7.894245,4.141075],[5.191658,1.769412,6.063820,6.384558,2.531862,0.825760,9.689584,-1.365790,-7.836728,6.396485,4.423816,0.471640],[-1.068399,-6.716081,-4.341764,6.125911,2.319146,-1.060160,4.131699,-2.850522,6.023093,-3.916127,6.156146,-4.670653],[9.031685,0.532678,2.919318,-9.751278,-6.477354,-2.580399,-1.022180,-3.685318,-8.694550,1.982282,-9.566204,-4.548931],[1.669909,2.764620,5.539598,9.613344,2.805240,-4.514515,7.287561,4.264463,2.868107,7.387593,5.700414,5.375216]],[[-9.844822,7.937077,0.211507,2.821698,0.045029,2.365622,-2.985572,2.358690,1.888100,-8.289748,-3.994296,2.104191],[4.413166,2.187002,-6.692045,-2.819574,1.276503,-3.903831,-2.071747,-9.363304,-1.032815,-9.176721,-6.013633,-2.001207],[9.379174,-3.977623,-3.402688,-2.676838,-3.511466,-5.286950,-8.405214,-0.755986,1.735291,-2.417990,-4.037973,8.984650],[0.519886,6.760682,7.092953,4.190187,-9.680718,-5.201516,4.549834,-1.867254,-3.318996,2.920145,2.829802,0.079855],[-3.187161,-9.690165,-3.200957,0.909709,-0.322150,8.686441,-9.928114,-3.364595,-8.811358,-3.896623,1.586724,-6.505271],[0.251463,0.878580,0.052525,4.865186,-0.270217,-5.958346,6.831372,-0.483392,-7.710999,0.567023,2.227258,3.904902],[-3.135547,5.906595,-6.054846,-6.710304,5.844811,-9.039382,-5.293295,-4.529826,-6.405307,6.193513,-1.453267,4.880320],[7.694162,-4.649217,-3.190856,-1.363889,1.682872,1.031873,8.625858,9.658716,7.202418,7.216132,-4.496122,-6.192340],[-4.674145,-8.048658,-9.566099,6.297027,0.503792,-1.403287,2.651082,-1.224736,-0.610071,-5.752335,1.807582,1.925596],[-8.829014,-8.712920,-9.699443,5.950512,-4.200665,-2.676805,7.278302,-3.436783,9.780012,-4.286822,-8.248013,4.106677]]], dtype = "float32")#candidate|6195|(16, 10, 12)|const|float32
uop_6196 = relay.sigmoid(const_6195.astype('float32')) # shape=(16, 10, 12)
output = relay.Tuple([uop_6196,])
output2 = relay.Tuple([uop_6196,])
func_6199 = relay.Function([], output)
mod['func_6199'] = func_6199
mod = relay.transform.InferType()(mod)
output = func_6199()
func_6200 = relay.Function([], output)
mutated_mod['func_6200'] = func_6200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4879_call = mod.get_global_var('func_4879')
func_4881_call = mutated_mod.get_global_var('func_4881')
call_6294 = relay.TupleGetItem(func_4879_call(), 0)
call_6295 = relay.TupleGetItem(func_4881_call(), 0)
output = relay.Tuple([call_6294,])
output2 = relay.Tuple([call_6295,])
func_6304 = relay.Function([], output)
mod['func_6304'] = func_6304
mod = relay.transform.InferType()(mod)
output = func_6304()
func_6305 = relay.Function([], output)
mutated_mod['func_6305'] = func_6305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4457_call = mod.get_global_var('func_4457')
func_4459_call = mutated_mod.get_global_var('func_4459')
call_6347 = relay.TupleGetItem(func_4457_call(), 2)
call_6348 = relay.TupleGetItem(func_4459_call(), 2)
func_3294_call = mod.get_global_var('func_3294')
func_3295_call = mutated_mod.get_global_var('func_3295')
call_6352 = relay.TupleGetItem(func_3294_call(), 0)
call_6353 = relay.TupleGetItem(func_3295_call(), 0)
func_1192_call = mod.get_global_var('func_1192')
func_1197_call = mutated_mod.get_global_var('func_1197')
const_6358 = relay.const([9,1,-3,-2,-5,6,-2,3,5,-8,-5,4,-8,9,5,-2,-8,-2,9,7,5,-5,2,-8,7,10,8,8,-7,5,-8,6,2,-8,2,-5,7,-3,10,-8,7,1,-1,3,-3,-10,7,-9,-4,10,-2,-6,-6,8,10,3,5,5,4,-2,6,9,7,-2,7,-10,8,-8,5,-10,-3,4,-10,3,-7,-10,6,4,-9,8,-10,-5,-2,-5,-8,-2,10,8,-7,2,6,4,-1,-9,7,-6,-4,7,1,-5,-7,-1,-4,-6,2,2,-2,-3,-9,3,8,2,8,9,1,10,10,-2,-4,3,8,5,-6,-3,1,-8,3,10,-1,-3,-1,-10,-6,-5,-3], dtype = "uint64")#candidate|6358|(135,)|const|uint64
var_6359 = relay.var("var_6359", dtype = "uint8", shape = ())#candidate|6359|()|var|uint8
var_6360 = relay.var("var_6360", dtype = "uint8", shape = (108,))#candidate|6360|(108,)|var|uint8
call_6357 = relay.TupleGetItem(func_1192_call(relay.reshape(const_6358.astype('uint64'), [9, 15]), relay.reshape(const_6358.astype('uint64'), [9, 15]), relay.reshape(var_6359.astype('uint8'), []), relay.reshape(var_6360.astype('uint8'), [3, 36]), ), 3)
call_6361 = relay.TupleGetItem(func_1197_call(relay.reshape(const_6358.astype('uint64'), [9, 15]), relay.reshape(const_6358.astype('uint64'), [9, 15]), relay.reshape(var_6359.astype('uint8'), []), relay.reshape(var_6360.astype('uint8'), [3, 36]), ), 3)
func_5750_call = mod.get_global_var('func_5750')
func_5752_call = mutated_mod.get_global_var('func_5752')
call_6368 = relay.TupleGetItem(func_5750_call(), 4)
call_6369 = relay.TupleGetItem(func_5752_call(), 4)
uop_6382 = relay.atanh(call_6357.astype('float32')) # shape=(12, 9, 1)
uop_6384 = relay.atanh(call_6361.astype('float32')) # shape=(12, 9, 1)
func_2570_call = mod.get_global_var('func_2570')
func_2571_call = mutated_mod.get_global_var('func_2571')
call_6385 = relay.TupleGetItem(func_2570_call(), 1)
call_6386 = relay.TupleGetItem(func_2571_call(), 1)
bop_6387 = relay.subtract(uop_6382.astype('uint16'), const_6358.astype('uint16')) # shape=(12, 9, 135)
bop_6390 = relay.subtract(uop_6384.astype('uint16'), const_6358.astype('uint16')) # shape=(12, 9, 135)
func_455_call = mod.get_global_var('func_455')
func_459_call = mutated_mod.get_global_var('func_459')
call_6393 = relay.TupleGetItem(func_455_call(relay.reshape(var_6359.astype('uint8'), []), relay.reshape(uop_6382.astype('uint8'), [12, 9, 1]), ), 0)
call_6394 = relay.TupleGetItem(func_459_call(relay.reshape(var_6359.astype('uint8'), []), relay.reshape(uop_6382.astype('uint8'), [12, 9, 1]), ), 0)
uop_6402 = relay.acos(bop_6387.astype('float64')) # shape=(12, 9, 135)
uop_6404 = relay.acos(bop_6390.astype('float64')) # shape=(12, 9, 135)
var_6405 = relay.var("var_6405", dtype = "float64", shape = (12, 9, 135))#candidate|6405|(12, 9, 135)|var|float64
bop_6406 = relay.bitwise_or(uop_6402.astype('int64'), relay.reshape(var_6405.astype('int64'), relay.shape_of(uop_6402))) # shape=(12, 9, 135)
bop_6409 = relay.bitwise_or(uop_6404.astype('int64'), relay.reshape(var_6405.astype('int64'), relay.shape_of(uop_6404))) # shape=(12, 9, 135)
func_5154_call = mod.get_global_var('func_5154')
func_5158_call = mutated_mod.get_global_var('func_5158')
const_6415 = relay.const([-2,4,-7,-5,6,6,4,-9,-6,-3,-4,-1,8,-3,-5,-6,9,8,-4,-1,-5,-6,4,1,-4,3,9,7,9,8,6,-2,6,1,3,10,-10,-6,2,8,-2,-6,-4,-8,-4,-8,2,7,10,-8,1,4,4,6,7,-4,5,-4,2,4,8,-8,2,10,5,-8,6,8,9,-8,7,9,-9,-1,-5,-8,-6,5,4,-1,-3,-5,-8,9,-6,8,-8,-5,10,-7,-2,-9,-1,-6,2,-4,-4,-4,-10,2,9,-9,-6,3,2,-2,4,3,-10,2,6,-4,5,-5,-2,-2,6,9,6,10,1,4,-7,-3,-8,8,-9,6,-2,-10,9,-5,-3,-9,-4,9,-4,3,10,8,-8,-1,9,-2,2,3,-4,-8,-1,-8,-7,2,-7,-3,-8,-4,7,5,5,-5,1,-8,-4,-4,5,-2,8,-6,-1,-4,1,-7,-5,2,-2,-7,-5,-10,1,-8,7,-9,-5,1,-5,7,5,4,-8,10,-5,7,-1,-1,-2,-9,8,-5,4,-1,1,6,-3,5,-7,5,9,-2,-10,3,1,-2,-9,-3,3,3,-3,-9,9,2,-9,8,9,-10,-2,-1,-4,-1,2,-7,2,-10,-1,3,-4,-8,2,-3,-7,-1,6,3,7,-5,9,-5,-4,-6,-3,-6,6,10,-9,10,-5,-6,-3,1,4,10,-7,-4,7,5,1,-6,5,-6,8,2,-4,-4,-9,8,10,7,-10,-8,3,8,-5,2,4,-4,-1,-6,9,4,7,-9,10,4,-7,9,-6,-3,-5,10,-10,-2,3,7,-1,9,-5,-5,-4,-4,-1,-2,-4,-5,9,-10,2,-3,-1,-8,-3,2,-5,10,-6,-2,-9,-4,-9,-4,6,9,-6,-2,3,1,7,4,10,3,8,3,-2,-2,7,1,-8,1,5,10,5,5,-5,-4,-3,-9,4,10,-10,-7,8,2,10,-7,9,4,1,6,8,-8,-8,-4,2,10,-6,-9,-7,-10,4,-2,7,7,-5,1,-4,6,8,6,-4,2,-3,6,-3,7,-4,-10,-6,8,-1,-9,-1,-9,-3,-9,-1,-8,-5,6,-1,-7,3,7,-6,5,5,4,-6,-5,10,-7,6,-7,2,-8,8,7,3,-3,8,-8,-9,-8,-5,-4,-6,8,-8,4,-10,-2,-8,-10,-4,3,8,-6,-4,-1,-7,6,6,7,8,-6,6,7,-1,-6,-9,-9,-10,3,1,-5,-9,-2,-2,10,2,10,-6,-1,-5,1,8,2,-7,4,-9,6,7,-4,9,-10,-2,9,1,-4,-9,-2,-7,6,9,1,6,-5,-7,3,3,-7,6,-10,5,3,10,-2,-8,-4,8,-5,5,1,-9,8,-8,6,10,-2,1,-1,-1,-2,3,5,1,10,-2,-8,5,-2,10,8,-3,6,-6,-6,4,-5,4,-2,4,3,-3,6,8,1,-7,1,-1,-5,-8,3,1,-10,-10,3,2,-9,-8,5,4,-7,6,2,-7,-4,9,6,5,-8,6,-8,-7,5,1,-5,-7,5,-2,-3,-3,-1,-6,4,-1,-8,-2,-7,-1,-8,4,7,-6,5,9,-5,6,-7,-5,6,3,-4,10,6,4,6,-7,-9,7,-1,3,1,3,4,10,5,3,8,1,-7,-8,-2,7,-8,-7,-3,4,-2,3,-7,7,8,-1,5,2,6,-6,5,-2,-8,-1,-1,-6,-5,10,-3,6,-7,8,9,-6,10,-7,-5,-9,8,-5,-8,-4,3,-7,-1,8,9,1,-7,-7,9,3,3,-1,5,-1,-1,6,-1,10,5,1,5,-6,-9,1,-6,-5,8,9,-4,-6,7,6,-4,-7,4,5,-10,-4,-5,-8,-9,8,-9,-1,-7,-7,-9,-2,9,6,-7,-5,-3,7,-3,-6,2,-2,-3,3,9,6,-2,5,-8,-5,1,4,-8,-1,-10,3,-5,2,-7,-9,6,6,-2,9,1,6,3,-7,3,-4,-9,4,2,-3,10,7,7,-5,-6,10,-10,3,-6,-6,10,-3,-7,-6,-2,9,-1,9,-4,1,-9,-9,-9,2,-5,-6,8,-8,6,-5,-3,10,3,-3,4,-8,7,3,2,-1,6,3,-7,-1,3,9,2,-1,1,-5,10,-9,3,-2,7,-1,1,1,5,8,9,5,9,10,1,-4,-9,7,4,4,-3,6,-10,-1,-8,4,-10,-1,-4,8,6,-8,6,-6,7,4,6,-5,7,-3,6,-4,-6], dtype = "uint32")#candidate|6415|(840,)|const|uint32
call_6414 = relay.TupleGetItem(func_5154_call(relay.reshape(const_6415.astype('uint32'), [14, 6, 10]), relay.reshape(const_6415.astype('uint32'), [14, 6, 10]), ), 0)
call_6416 = relay.TupleGetItem(func_5158_call(relay.reshape(const_6415.astype('uint32'), [14, 6, 10]), relay.reshape(const_6415.astype('uint32'), [14, 6, 10]), ), 0)
func_5333_call = mod.get_global_var('func_5333')
func_5334_call = mutated_mod.get_global_var('func_5334')
call_6426 = func_5333_call()
call_6427 = func_5333_call()
func_455_call = mod.get_global_var('func_455')
func_459_call = mutated_mod.get_global_var('func_459')
call_6428 = relay.TupleGetItem(func_455_call(relay.reshape(var_6359.astype('uint8'), []), relay.reshape(uop_6382.astype('uint8'), [12, 9, 1]), ), 0)
call_6429 = relay.TupleGetItem(func_459_call(relay.reshape(var_6359.astype('uint8'), []), relay.reshape(uop_6382.astype('uint8'), [12, 9, 1]), ), 0)
uop_6430 = relay.asinh(bop_6406.astype('float64')) # shape=(12, 9, 135)
uop_6432 = relay.asinh(bop_6409.astype('float64')) # shape=(12, 9, 135)
uop_6435 = relay.sinh(var_6405.astype('float64')) # shape=(12, 9, 135)
bop_6440 = relay.logical_or(uop_6402.astype('bool'), relay.reshape(var_6405.astype('bool'), relay.shape_of(uop_6402))) # shape=(12, 9, 135)
bop_6443 = relay.logical_or(uop_6404.astype('bool'), relay.reshape(var_6405.astype('bool'), relay.shape_of(uop_6404))) # shape=(12, 9, 135)
var_6445 = relay.var("var_6445", dtype = "float64", shape = (12, 9, 135))#candidate|6445|(12, 9, 135)|var|float64
bop_6446 = relay.less(uop_6430.astype('bool'), relay.reshape(var_6445.astype('bool'), relay.shape_of(uop_6430))) # shape=(12, 9, 135)
bop_6449 = relay.less(uop_6432.astype('bool'), relay.reshape(var_6445.astype('bool'), relay.shape_of(uop_6432))) # shape=(12, 9, 135)
uop_6450 = relay.sqrt(bop_6446.astype('float64')) # shape=(12, 9, 135)
uop_6452 = relay.sqrt(bop_6449.astype('float64')) # shape=(12, 9, 135)
output = relay.Tuple([call_6347,call_6352,var_6359,var_6360,call_6368,call_6385,call_6393,call_6414,const_6415,call_6426,call_6428,uop_6435,bop_6440,uop_6450,])
output2 = relay.Tuple([call_6348,call_6353,var_6359,var_6360,call_6369,call_6386,call_6394,call_6416,const_6415,call_6427,call_6429,uop_6435,bop_6443,uop_6452,])
func_6456 = relay.Function([var_6359,var_6360,var_6405,var_6445,], output)
mod['func_6456'] = func_6456
mod = relay.transform.InferType()(mod)
var_6457 = relay.var("var_6457", dtype = "uint8", shape = ())#candidate|6457|()|var|uint8
var_6458 = relay.var("var_6458", dtype = "uint8", shape = (108,))#candidate|6458|(108,)|var|uint8
var_6459 = relay.var("var_6459", dtype = "float64", shape = (12, 9, 135))#candidate|6459|(12, 9, 135)|var|float64
var_6460 = relay.var("var_6460", dtype = "float64", shape = (12, 9, 135))#candidate|6460|(12, 9, 135)|var|float64
output = func_6456(var_6457,var_6458,var_6459,var_6460,)
func_6461 = relay.Function([var_6457,var_6458,var_6459,var_6460,], output)
mutated_mod['func_6461'] = func_6461
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6573 = relay.var("var_6573", dtype = "uint16", shape = (3, 9, 13))#candidate|6573|(3, 9, 13)|var|uint16
var_6574 = relay.var("var_6574", dtype = "uint16", shape = (3, 9, 13))#candidate|6574|(3, 9, 13)|var|uint16
bop_6575 = relay.logical_xor(var_6573.astype('uint16'), relay.reshape(var_6574.astype('uint16'), relay.shape_of(var_6573))) # shape=(3, 9, 13)
bop_6579 = relay.divide(var_6574.astype('float32'), relay.reshape(var_6573.astype('float32'), relay.shape_of(var_6574))) # shape=(3, 9, 13)
output = relay.Tuple([bop_6575,bop_6579,])
output2 = relay.Tuple([bop_6575,bop_6579,])
func_6583 = relay.Function([var_6573,var_6574,], output)
mod['func_6583'] = func_6583
mod = relay.transform.InferType()(mod)
var_6584 = relay.var("var_6584", dtype = "uint16", shape = (3, 9, 13))#candidate|6584|(3, 9, 13)|var|uint16
var_6585 = relay.var("var_6585", dtype = "uint16", shape = (3, 9, 13))#candidate|6585|(3, 9, 13)|var|uint16
output = func_6583(var_6584,var_6585,)
func_6586 = relay.Function([var_6584,var_6585,], output)
mutated_mod['func_6586'] = func_6586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4471_call = mod.get_global_var('func_4471')
func_4472_call = mutated_mod.get_global_var('func_4472')
call_6726 = func_4471_call()
call_6727 = func_4471_call()
func_6583_call = mod.get_global_var('func_6583')
func_6586_call = mutated_mod.get_global_var('func_6586')
var_6740 = relay.var("var_6740", dtype = "uint16", shape = (351,))#candidate|6740|(351,)|var|uint16
call_6739 = relay.TupleGetItem(func_6583_call(relay.reshape(var_6740.astype('uint16'), [3, 9, 13]), relay.reshape(var_6740.astype('uint16'), [3, 9, 13]), ), 1)
call_6741 = relay.TupleGetItem(func_6586_call(relay.reshape(var_6740.astype('uint16'), [3, 9, 13]), relay.reshape(var_6740.astype('uint16'), [3, 9, 13]), ), 1)
func_4602_call = mod.get_global_var('func_4602')
func_4604_call = mutated_mod.get_global_var('func_4604')
var_6763 = relay.var("var_6763", dtype = "uint8", shape = (108,))#candidate|6763|(108,)|var|uint8
call_6762 = relay.TupleGetItem(func_4602_call(relay.reshape(var_6763.astype('uint8'), [108,])), 4)
call_6764 = relay.TupleGetItem(func_4604_call(relay.reshape(var_6763.astype('uint8'), [108,])), 4)
uop_6780 = relay.asinh(var_6740.astype('float64')) # shape=(351,)
output = relay.Tuple([call_6726,call_6739,call_6762,var_6763,uop_6780,])
output2 = relay.Tuple([call_6727,call_6741,call_6764,var_6763,uop_6780,])
func_6788 = relay.Function([var_6740,var_6763,], output)
mod['func_6788'] = func_6788
mod = relay.transform.InferType()(mod)
mutated_mod['func_6788'] = func_6788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6788_call = mutated_mod.get_global_var('func_6788')
var_6790 = relay.var("var_6790", dtype = "uint16", shape = (351,))#candidate|6790|(351,)|var|uint16
var_6791 = relay.var("var_6791", dtype = "uint8", shape = (108,))#candidate|6791|(108,)|var|uint8
call_6789 = func_6788_call(var_6790,var_6791,)
output = call_6789
func_6792 = relay.Function([var_6790,var_6791,], output)
mutated_mod['func_6792'] = func_6792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6199_call = mod.get_global_var('func_6199')
func_6200_call = mutated_mod.get_global_var('func_6200')
call_6824 = relay.TupleGetItem(func_6199_call(), 0)
call_6825 = relay.TupleGetItem(func_6200_call(), 0)
func_3733_call = mod.get_global_var('func_3733')
func_3735_call = mutated_mod.get_global_var('func_3735')
var_6831 = relay.var("var_6831", dtype = "float32", shape = (156,))#candidate|6831|(156,)|var|float32
call_6830 = relay.TupleGetItem(func_3733_call(relay.reshape(var_6831.astype('float32'), [13, 2, 6])), 1)
call_6832 = relay.TupleGetItem(func_3735_call(relay.reshape(var_6831.astype('float32'), [13, 2, 6])), 1)
uop_6841 = relay.acos(var_6831.astype('float32')) # shape=(156,)
output = relay.Tuple([call_6824,call_6830,uop_6841,])
output2 = relay.Tuple([call_6825,call_6832,uop_6841,])
func_6843 = relay.Function([var_6831,], output)
mod['func_6843'] = func_6843
mod = relay.transform.InferType()(mod)
var_6844 = relay.var("var_6844", dtype = "float32", shape = (156,))#candidate|6844|(156,)|var|float32
output = func_6843(var_6844)
func_6845 = relay.Function([var_6844], output)
mutated_mod['func_6845'] = func_6845
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5905_call = mod.get_global_var('func_5905')
func_5907_call = mutated_mod.get_global_var('func_5907')
call_6850 = func_5905_call()
call_6851 = func_5905_call()
func_2899_call = mod.get_global_var('func_2899')
func_2901_call = mutated_mod.get_global_var('func_2901')
call_6879 = func_2899_call()
call_6880 = func_2899_call()
output = relay.Tuple([call_6850,call_6879,])
output2 = relay.Tuple([call_6851,call_6880,])
func_6883 = relay.Function([], output)
mod['func_6883'] = func_6883
mod = relay.transform.InferType()(mod)
mutated_mod['func_6883'] = func_6883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6883_call = mutated_mod.get_global_var('func_6883')
call_6884 = func_6883_call()
output = call_6884
func_6885 = relay.Function([], output)
mutated_mod['func_6885'] = func_6885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5905_call = mod.get_global_var('func_5905')
func_5907_call = mutated_mod.get_global_var('func_5907')
call_6959 = func_5905_call()
call_6960 = func_5905_call()
uop_6961 = relay.tan(call_6959.astype('float64')) # shape=(198,)
uop_6963 = relay.tan(call_6960.astype('float64')) # shape=(198,)
var_6967 = relay.var("var_6967", dtype = "float64", shape = (198,))#candidate|6967|(198,)|var|float64
bop_6968 = relay.subtract(uop_6961.astype('uint8'), relay.reshape(var_6967.astype('uint8'), relay.shape_of(uop_6961))) # shape=(198,)
bop_6971 = relay.subtract(uop_6963.astype('uint8'), relay.reshape(var_6967.astype('uint8'), relay.shape_of(uop_6963))) # shape=(198,)
output = relay.Tuple([bop_6968,])
output2 = relay.Tuple([bop_6971,])
func_6972 = relay.Function([var_6967,], output)
mod['func_6972'] = func_6972
mod = relay.transform.InferType()(mod)
var_6973 = relay.var("var_6973", dtype = "float64", shape = (198,))#candidate|6973|(198,)|var|float64
output = func_6972(var_6973)
func_6974 = relay.Function([var_6973], output)
mutated_mod['func_6974'] = func_6974
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4499_call = mod.get_global_var('func_4499')
func_4501_call = mutated_mod.get_global_var('func_4501')
call_7025 = func_4499_call()
call_7026 = func_4499_call()
func_2020_call = mod.get_global_var('func_2020')
func_2023_call = mutated_mod.get_global_var('func_2023')
var_7035 = relay.var("var_7035", dtype = "int16", shape = (192,))#candidate|7035|(192,)|var|int16
call_7034 = func_2020_call(relay.reshape(var_7035.astype('int16'), [4, 12, 4]), relay.reshape(var_7035.astype('int16'), [4, 12, 4]), )
call_7036 = func_2020_call(relay.reshape(var_7035.astype('int16'), [4, 12, 4]), relay.reshape(var_7035.astype('int16'), [4, 12, 4]), )
output = relay.Tuple([call_7025,call_7034,var_7035,])
output2 = relay.Tuple([call_7026,call_7036,var_7035,])
func_7037 = relay.Function([var_7035,], output)
mod['func_7037'] = func_7037
mod = relay.transform.InferType()(mod)
mutated_mod['func_7037'] = func_7037
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7038 = relay.var("var_7038", dtype = "int16", shape = (192,))#candidate|7038|(192,)|var|int16
func_7037_call = mutated_mod.get_global_var('func_7037')
call_7039 = func_7037_call(var_7038)
output = call_7039
func_7040 = relay.Function([var_7038], output)
mutated_mod['func_7040'] = func_7040
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4457_call = mod.get_global_var('func_4457')
func_4459_call = mutated_mod.get_global_var('func_4459')
call_7042 = relay.TupleGetItem(func_4457_call(), 0)
call_7043 = relay.TupleGetItem(func_4459_call(), 0)
output = call_7042
output2 = call_7043
func_7052 = relay.Function([], output)
mod['func_7052'] = func_7052
mod = relay.transform.InferType()(mod)
output = func_7052()
func_7053 = relay.Function([], output)
mutated_mod['func_7053'] = func_7053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7052_call = mod.get_global_var('func_7052')
func_7053_call = mutated_mod.get_global_var('func_7053')
call_7086 = func_7052_call()
call_7087 = func_7052_call()
func_5900_call = mod.get_global_var('func_5900')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_7092 = relay.TupleGetItem(func_5900_call(), 0)
call_7093 = relay.TupleGetItem(func_5901_call(), 0)
output = relay.Tuple([call_7086,call_7092,])
output2 = relay.Tuple([call_7087,call_7093,])
func_7095 = relay.Function([], output)
mod['func_7095'] = func_7095
mod = relay.transform.InferType()(mod)
output = func_7095()
func_7096 = relay.Function([], output)
mutated_mod['func_7096'] = func_7096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6883_call = mod.get_global_var('func_6883')
func_6885_call = mutated_mod.get_global_var('func_6885')
call_7119 = relay.TupleGetItem(func_6883_call(), 0)
call_7120 = relay.TupleGetItem(func_6885_call(), 0)
uop_7124 = relay.atan(call_7119.astype('float32')) # shape=(198,)
uop_7126 = relay.atan(call_7120.astype('float32')) # shape=(198,)
func_4334_call = mod.get_global_var('func_4334')
func_4336_call = mutated_mod.get_global_var('func_4336')
call_7132 = relay.TupleGetItem(func_4334_call(), 1)
call_7133 = relay.TupleGetItem(func_4336_call(), 1)
func_5940_call = mod.get_global_var('func_5940')
func_5943_call = mutated_mod.get_global_var('func_5943')
const_7135 = relay.const([9.898061,-4.283419,-1.859140,4.503243,1.905702,0.275411,7.111581,-9.725356,-5.718016,3.860203,4.284246,3.018869,6.458999,6.150901,-1.739229,5.686738,-0.452923,1.492180,1.614362,1.829033,-1.660086,9.506523,5.702017,6.549722,-9.775312,-7.282953,-5.225451,2.052894,4.162203,-6.773764,0.112074,-9.951241,5.112059,5.500405,-8.186497,-1.682681,1.239763,-1.853956,8.465948,-9.831741,-8.504149,8.287261,-2.171337,8.477074,-6.724166,-7.616684,4.843872,1.522536,-2.016086,6.736934,-0.142451,7.782857,-0.012662,-9.739319,-8.696521,7.208173,2.952634,3.018906,3.084787,3.524065,-7.060673,-0.257729,-0.998448,4.703416,-7.018390,9.632543,-5.570494,-7.748332,-1.317954,-8.281704,0.274328,-3.920397,6.305992,-5.506045,-0.785835,-8.824639,3.166062,-4.889323,-7.520998,-9.399754], dtype = "float64")#candidate|7135|(80,)|const|float64
call_7134 = func_5940_call(relay.reshape(const_7135.astype('float64'), [5, 1, 16]))
call_7136 = func_5940_call(relay.reshape(const_7135.astype('float64'), [5, 1, 16]))
bop_7145 = relay.logical_or(uop_7124.astype('bool'), relay.reshape(call_7119.astype('bool'), relay.shape_of(uop_7124))) # shape=(198,)
bop_7148 = relay.logical_or(uop_7126.astype('bool'), relay.reshape(call_7120.astype('bool'), relay.shape_of(uop_7126))) # shape=(198,)
func_6165_call = mod.get_global_var('func_6165')
func_6167_call = mutated_mod.get_global_var('func_6167')
call_7150 = func_6165_call()
call_7151 = func_6165_call()
func_6165_call = mod.get_global_var('func_6165')
func_6167_call = mutated_mod.get_global_var('func_6167')
call_7159 = func_6165_call()
call_7160 = func_6165_call()
uop_7175 = relay.cosh(call_7134.astype('float64')) # shape=(5, 1, 16)
uop_7177 = relay.cosh(call_7136.astype('float64')) # shape=(5, 1, 16)
func_5986_call = mod.get_global_var('func_5986')
func_5987_call = mutated_mod.get_global_var('func_5987')
call_7184 = func_5986_call()
call_7185 = func_5986_call()
output = relay.Tuple([call_7132,const_7135,bop_7145,call_7150,call_7159,uop_7175,call_7184,])
output2 = relay.Tuple([call_7133,const_7135,bop_7148,call_7151,call_7160,uop_7177,call_7185,])
func_7187 = relay.Function([], output)
mod['func_7187'] = func_7187
mod = relay.transform.InferType()(mod)
output = func_7187()
func_7188 = relay.Function([], output)
mutated_mod['func_7188'] = func_7188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2528_call = mod.get_global_var('func_2528')
func_2529_call = mutated_mod.get_global_var('func_2529')
call_7199 = relay.TupleGetItem(func_2528_call(), 0)
call_7200 = relay.TupleGetItem(func_2529_call(), 0)
output = relay.Tuple([call_7199,])
output2 = relay.Tuple([call_7200,])
func_7201 = relay.Function([], output)
mod['func_7201'] = func_7201
mod = relay.transform.InferType()(mod)
output = func_7201()
func_7202 = relay.Function([], output)
mutated_mod['func_7202'] = func_7202
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5447_call = mod.get_global_var('func_5447')
func_5448_call = mutated_mod.get_global_var('func_5448')
call_7237 = func_5447_call()
call_7238 = func_5447_call()
func_2638_call = mod.get_global_var('func_2638')
func_2642_call = mutated_mod.get_global_var('func_2642')
var_7245 = relay.var("var_7245", dtype = "float64", shape = (198,))#candidate|7245|(198,)|var|float64
var_7246 = relay.var("var_7246", dtype = "float64", shape = (216,))#candidate|7246|(216,)|var|float64
call_7244 = relay.TupleGetItem(func_2638_call(relay.reshape(var_7245.astype('float64'), [198,]), relay.reshape(var_7246.astype('float64'), [216,]), ), 3)
call_7247 = relay.TupleGetItem(func_2642_call(relay.reshape(var_7245.astype('float64'), [198,]), relay.reshape(var_7246.astype('float64'), [216,]), ), 3)
func_2040_call = mod.get_global_var('func_2040')
func_2042_call = mutated_mod.get_global_var('func_2042')
call_7252 = relay.TupleGetItem(func_2040_call(relay.reshape(call_7244.astype('float64'), [3, 9, 8])), 0)
call_7253 = relay.TupleGetItem(func_2042_call(relay.reshape(call_7244.astype('float64'), [3, 9, 8])), 0)
output = relay.Tuple([call_7237,call_7244,var_7245,var_7246,call_7252,])
output2 = relay.Tuple([call_7238,call_7247,var_7245,var_7246,call_7253,])
func_7269 = relay.Function([var_7245,var_7246,], output)
mod['func_7269'] = func_7269
mod = relay.transform.InferType()(mod)
var_7270 = relay.var("var_7270", dtype = "float64", shape = (198,))#candidate|7270|(198,)|var|float64
var_7271 = relay.var("var_7271", dtype = "float64", shape = (216,))#candidate|7271|(216,)|var|float64
output = func_7269(var_7270,var_7271,)
func_7272 = relay.Function([var_7270,var_7271,], output)
mutated_mod['func_7272'] = func_7272
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5900_call = mod.get_global_var('func_5900')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_7288 = relay.TupleGetItem(func_5900_call(), 0)
call_7289 = relay.TupleGetItem(func_5901_call(), 0)
func_5848_call = mod.get_global_var('func_5848')
func_5849_call = mutated_mod.get_global_var('func_5849')
call_7296 = func_5848_call()
call_7297 = func_5848_call()
func_4731_call = mod.get_global_var('func_4731')
func_4732_call = mutated_mod.get_global_var('func_4732')
call_7302 = relay.TupleGetItem(func_4731_call(), 0)
call_7303 = relay.TupleGetItem(func_4732_call(), 0)
output = relay.Tuple([call_7288,call_7296,call_7302,])
output2 = relay.Tuple([call_7289,call_7297,call_7303,])
func_7318 = relay.Function([], output)
mod['func_7318'] = func_7318
mod = relay.transform.InferType()(mod)
output = func_7318()
func_7319 = relay.Function([], output)
mutated_mod['func_7319'] = func_7319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4731_call = mod.get_global_var('func_4731')
func_4732_call = mutated_mod.get_global_var('func_4732')
call_7337 = relay.TupleGetItem(func_4731_call(), 0)
call_7338 = relay.TupleGetItem(func_4732_call(), 0)
func_2899_call = mod.get_global_var('func_2899')
func_2901_call = mutated_mod.get_global_var('func_2901')
call_7339 = func_2899_call()
call_7340 = func_2899_call()
output = relay.Tuple([call_7337,call_7339,])
output2 = relay.Tuple([call_7338,call_7340,])
func_7350 = relay.Function([], output)
mod['func_7350'] = func_7350
mod = relay.transform.InferType()(mod)
mutated_mod['func_7350'] = func_7350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7350_call = mutated_mod.get_global_var('func_7350')
call_7351 = func_7350_call()
output = call_7351
func_7352 = relay.Function([], output)
mutated_mod['func_7352'] = func_7352
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3106_call = mod.get_global_var('func_3106')
func_3108_call = mutated_mod.get_global_var('func_3108')
call_7390 = func_3106_call()
call_7391 = func_3106_call()
func_3550_call = mod.get_global_var('func_3550')
func_3553_call = mutated_mod.get_global_var('func_3553')
var_7395 = relay.var("var_7395", dtype = "float64", shape = (198,))#candidate|7395|(198,)|var|float64
call_7394 = relay.TupleGetItem(func_3550_call(relay.reshape(call_7390.astype('float32'), [13, 2, 6]), relay.reshape(var_7395.astype('float64'), [1, 198]), ), 1)
call_7396 = relay.TupleGetItem(func_3553_call(relay.reshape(call_7390.astype('float32'), [13, 2, 6]), relay.reshape(var_7395.astype('float64'), [1, 198]), ), 1)
output = relay.Tuple([call_7390,call_7394,var_7395,])
output2 = relay.Tuple([call_7391,call_7396,var_7395,])
func_7406 = relay.Function([var_7395,], output)
mod['func_7406'] = func_7406
mod = relay.transform.InferType()(mod)
mutated_mod['func_7406'] = func_7406
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7407 = relay.var("var_7407", dtype = "float64", shape = (198,))#candidate|7407|(198,)|var|float64
func_7406_call = mutated_mod.get_global_var('func_7406')
call_7408 = func_7406_call(var_7407)
output = call_7408
func_7409 = relay.Function([var_7407], output)
mutated_mod['func_7409'] = func_7409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4879_call = mod.get_global_var('func_4879')
func_4881_call = mutated_mod.get_global_var('func_4881')
call_7449 = relay.TupleGetItem(func_4879_call(), 0)
call_7450 = relay.TupleGetItem(func_4881_call(), 0)
output = call_7449
output2 = call_7450
func_7458 = relay.Function([], output)
mod['func_7458'] = func_7458
mod = relay.transform.InferType()(mod)
output = func_7458()
func_7459 = relay.Function([], output)
mutated_mod['func_7459'] = func_7459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5447_call = mod.get_global_var('func_5447')
func_5448_call = mutated_mod.get_global_var('func_5448')
call_7460 = func_5447_call()
call_7461 = func_5447_call()
output = call_7460
output2 = call_7461
func_7470 = relay.Function([], output)
mod['func_7470'] = func_7470
mod = relay.transform.InferType()(mod)
mutated_mod['func_7470'] = func_7470
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7470_call = mutated_mod.get_global_var('func_7470')
call_7471 = func_7470_call()
output = call_7471
func_7472 = relay.Function([], output)
mutated_mod['func_7472'] = func_7472
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7501 = relay.var("var_7501", dtype = "int32", shape = ())#candidate|7501|()|var|int32
var_7502 = relay.var("var_7502", dtype = "int32", shape = (3, 2, 9))#candidate|7502|(3, 2, 9)|var|int32
bop_7503 = relay.less_equal(var_7501.astype('bool'), var_7502.astype('bool')) # shape=(3, 2, 9)
func_2528_call = mod.get_global_var('func_2528')
func_2529_call = mutated_mod.get_global_var('func_2529')
call_7512 = relay.TupleGetItem(func_2528_call(), 0)
call_7513 = relay.TupleGetItem(func_2529_call(), 0)
bop_7518 = relay.left_shift(call_7512.astype('uint16'), var_7501.astype('uint16')) # shape=(13, 2, 6)
bop_7521 = relay.left_shift(call_7513.astype('uint16'), var_7501.astype('uint16')) # shape=(13, 2, 6)
uop_7528 = relay.exp(var_7502.astype('float32')) # shape=(3, 2, 9)
output = relay.Tuple([bop_7503,bop_7518,uop_7528,])
output2 = relay.Tuple([bop_7503,bop_7521,uop_7528,])
F = relay.Function([var_7501,var_7502,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_7501,var_7502,], output2)
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
	relay.transform.InferType(),
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
