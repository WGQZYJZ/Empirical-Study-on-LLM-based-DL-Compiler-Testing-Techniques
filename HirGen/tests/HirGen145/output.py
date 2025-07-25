import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_147 = relay.const([[[-2.808130,5.639914],[2.364741,0.305916],[0.295124,-0.339540],[0.768787,-4.080305],[6.851381,-4.397390],[-3.545262,1.428118],[-8.463995,4.543453],[4.474060,3.042748],[6.793844,-8.256876],[-5.711478,-5.975673],[-7.281409,3.653188],[-4.910664,-0.444942],[-4.239650,7.753050],[6.741375,3.706675],[-4.000035,-6.954458],[-9.904445,3.312016]],[[9.605814,-0.671965],[0.232301,0.518682],[-9.849587,-7.605124],[-3.783159,-9.024639],[0.606125,-1.874287],[-4.375247,-3.099829],[-1.552696,-6.227911],[-2.742535,4.619345],[9.854258,2.719291],[-1.340166,-1.878238],[5.087368,3.728621],[2.147427,-4.008853],[6.959282,-8.848006],[2.423863,-1.996287],[9.772032,-8.556394],[-7.054337,6.538535]],[[9.740780,-0.524310],[0.843106,-9.852553],[4.903898,0.127448],[5.992313,-3.262036],[-4.837926,-4.503979],[0.678960,5.577804],[3.532390,1.532376],[6.823801,-9.252509],[1.943622,-1.154668],[5.271727,-1.074866],[-5.264322,-3.226764],[4.369950,-1.246747],[7.483177,8.155339],[7.291483,5.835596],[-4.606468,-9.639646],[-5.991382,4.335211]],[[-8.462636,-4.593519],[-3.026714,-9.534357],[-9.138642,0.912553],[7.931284,2.071604],[-2.680354,-5.184961],[-7.448640,2.302636],[-3.640056,-2.242900],[-2.399961,-4.069892],[-4.236581,-4.156003],[9.836432,8.582065],[3.620391,-8.741960],[1.790188,1.209657],[-5.198094,9.359838],[-1.726187,-8.744200],[4.055937,7.964093],[-9.868604,-2.538736]],[[-1.277099,1.281928],[5.925231,-7.621713],[9.165578,-3.959134],[-6.518589,2.430106],[9.078715,0.848762],[4.142250,-0.353846],[0.630782,-4.597023],[0.247396,-1.004913],[1.501922,-3.756766],[-1.052336,-6.164618],[7.755186,-4.318696],[-0.694610,-8.552489],[9.387825,3.288072],[3.927653,6.246496],[5.353855,-5.085639],[-5.318690,5.118744]],[[3.561843,-6.897022],[-4.023865,6.950101],[4.401190,9.680612],[9.752200,1.418068],[-0.012597,7.524113],[-6.810136,-0.607893],[-2.996468,6.727050],[7.796356,4.861376],[-7.156314,-5.127668],[-0.963355,-3.838546],[-8.104045,4.814871],[4.409818,-3.413869],[-4.375863,-5.633763],[-2.763574,-0.147210],[0.564752,8.359901],[-7.829325,7.529119]],[[-7.473503,0.104065],[-3.695689,9.306551],[-0.138763,-8.244989],[2.712818,9.098461],[9.582364,5.995423],[-1.044345,-2.247123],[5.351760,-5.527210],[-8.068848,-2.981673],[3.746660,5.465617],[9.491008,-2.335721],[-1.067730,5.003539],[6.026878,9.485546],[-1.413717,-9.950915],[-9.760838,2.402834],[-2.446544,-3.262631],[4.440120,-6.336181]],[[-9.760230,-0.171610],[-3.485287,6.912107],[-5.690396,-7.626249],[3.318565,-9.688764],[-3.983508,-6.564503],[3.845380,-6.009833],[9.803478,7.924638],[9.432554,-2.487612],[4.483062,8.441566],[4.046934,-9.285940],[-9.081363,-6.316761],[-8.865679,6.625129],[8.688052,-7.172838],[5.277727,3.152788],[7.309305,-2.699796],[-5.677076,-5.242336]],[[5.924318,6.648286],[5.419782,-5.055719],[-2.166745,2.850312],[8.553622,-5.880864],[8.698996,-0.809639],[5.068069,6.864936],[-3.322931,-2.073295],[-4.369856,-7.785716],[-0.601892,2.311625],[-0.039382,8.928243],[-6.031859,2.138971],[-4.894040,-8.652731],[-6.226675,-1.021078],[-4.737898,-4.157405],[0.186582,4.508620],[-6.749680,-4.416248]],[[6.013737,-3.400719],[1.641186,0.395053],[-7.839202,-6.186582],[-0.736039,-1.850106],[6.998670,-4.483221],[7.259520,-1.922992],[1.405934,-3.856772],[8.329929,3.998568],[-7.937443,-3.927799],[6.892008,8.389066],[0.059320,-4.370753],[6.589590,-5.040443],[-1.018704,-4.705889],[-2.133675,-9.941110],[5.590294,0.994367],[3.882335,8.798895]],[[-7.078227,-2.715053],[6.390556,9.340323],[7.060848,-9.176647],[5.510848,0.620246],[-1.503365,6.036280],[-8.483486,-7.729306],[-6.912422,-3.698847],[-0.501703,-6.801064],[-0.473260,6.871886],[-2.099241,-8.818404],[-4.171351,-5.554228],[0.355787,9.737017],[-8.258625,-8.629073],[9.518678,-4.731345],[-1.033794,1.170778],[-5.994265,6.941787]],[[-9.557774,6.296351],[-3.179637,-7.647499],[-2.897963,-6.502365],[-6.205455,6.095605],[-1.398118,5.474008],[8.382993,0.161158],[7.414762,-4.136508],[-5.393845,-6.023917],[-7.930716,-0.131542],[8.715027,-0.112051],[3.668550,8.370923],[-9.287953,-0.180102],[3.026695,-3.870569],[8.600663,-0.807948],[9.128470,1.625024],[4.670859,-5.603817]]], dtype = "float32")#candidate|147|(12, 16, 2)|const|float32
uop_148 = relay.atan(const_147.astype('float32')) # shape=(12, 16, 2)
bop_150 = relay.less_equal(uop_148.astype('bool'), relay.reshape(const_147.astype('bool'), relay.shape_of(uop_148))) # shape=(12, 16, 2)
output = relay.Tuple([bop_150,])
output2 = relay.Tuple([bop_150,])
func_153 = relay.Function([], output)
mod['func_153'] = func_153
mod = relay.transform.InferType()(mod)
output = func_153()
func_154 = relay.Function([], output)
mutated_mod['func_154'] = func_154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_153_call = mod.get_global_var('func_153')
func_154_call = mutated_mod.get_global_var('func_154')
call_162 = relay.TupleGetItem(func_153_call(), 0)
call_163 = relay.TupleGetItem(func_154_call(), 0)
var_165 = relay.var("var_165", dtype = "bool", shape = (12, 16, 2))#candidate|165|(12, 16, 2)|var|bool
bop_166 = relay.less(call_162.astype('bool'), relay.reshape(var_165.astype('bool'), relay.shape_of(call_162))) # shape=(12, 16, 2)
bop_169 = relay.less(call_163.astype('bool'), relay.reshape(var_165.astype('bool'), relay.shape_of(call_163))) # shape=(12, 16, 2)
bop_173 = relay.left_shift(call_162.astype('int16'), relay.reshape(var_165.astype('int16'), relay.shape_of(call_162))) # shape=(12, 16, 2)
bop_176 = relay.left_shift(call_163.astype('int16'), relay.reshape(var_165.astype('int16'), relay.shape_of(call_163))) # shape=(12, 16, 2)
func_153_call = mod.get_global_var('func_153')
func_154_call = mutated_mod.get_global_var('func_154')
call_177 = relay.TupleGetItem(func_153_call(), 0)
call_178 = relay.TupleGetItem(func_154_call(), 0)
output = relay.Tuple([bop_166,bop_173,call_177,])
output2 = relay.Tuple([bop_169,bop_176,call_178,])
func_184 = relay.Function([var_165,], output)
mod['func_184'] = func_184
mod = relay.transform.InferType()(mod)
mutated_mod['func_184'] = func_184
mutated_mod = relay.transform.InferType()(mutated_mod)
var_185 = relay.var("var_185", dtype = "bool", shape = (12, 16, 2))#candidate|185|(12, 16, 2)|var|bool
func_184_call = mutated_mod.get_global_var('func_184')
call_186 = func_184_call(var_185)
output = call_186
func_187 = relay.Function([var_185], output)
mutated_mod['func_187'] = func_187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_153_call = mod.get_global_var('func_153')
func_154_call = mutated_mod.get_global_var('func_154')
call_209 = relay.TupleGetItem(func_153_call(), 0)
call_210 = relay.TupleGetItem(func_154_call(), 0)
func_153_call = mod.get_global_var('func_153')
func_154_call = mutated_mod.get_global_var('func_154')
call_211 = relay.TupleGetItem(func_153_call(), 0)
call_212 = relay.TupleGetItem(func_154_call(), 0)
output = relay.Tuple([call_209,call_211,])
output2 = relay.Tuple([call_210,call_212,])
func_225 = relay.Function([], output)
mod['func_225'] = func_225
mod = relay.transform.InferType()(mod)
output = func_225()
func_226 = relay.Function([], output)
mutated_mod['func_226'] = func_226
mutated_mod = relay.transform.InferType()(mutated_mod)
var_253 = relay.var("var_253", dtype = "float32", shape = (12, 8, 9))#candidate|253|(12, 8, 9)|var|float32
uop_254 = relay.asin(var_253.astype('float32')) # shape=(12, 8, 9)
output = relay.Tuple([uop_254,])
output2 = relay.Tuple([uop_254,])
func_261 = relay.Function([var_253,], output)
mod['func_261'] = func_261
mod = relay.transform.InferType()(mod)
var_262 = relay.var("var_262", dtype = "float32", shape = (12, 8, 9))#candidate|262|(12, 8, 9)|var|float32
output = func_261(var_262)
func_263 = relay.Function([var_262], output)
mutated_mod['func_263'] = func_263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_153_call = mod.get_global_var('func_153')
func_154_call = mutated_mod.get_global_var('func_154')
call_286 = relay.TupleGetItem(func_153_call(), 0)
call_287 = relay.TupleGetItem(func_154_call(), 0)
output = call_286
output2 = call_287
func_304 = relay.Function([], output)
mod['func_304'] = func_304
mod = relay.transform.InferType()(mod)
mutated_mod['func_304'] = func_304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_304_call = mutated_mod.get_global_var('func_304')
call_305 = func_304_call()
output = call_305
func_306 = relay.Function([], output)
mutated_mod['func_306'] = func_306
mutated_mod = relay.transform.InferType()(mutated_mod)
func_225_call = mod.get_global_var('func_225')
func_226_call = mutated_mod.get_global_var('func_226')
call_359 = relay.TupleGetItem(func_225_call(), 1)
call_360 = relay.TupleGetItem(func_226_call(), 1)
output = call_359
output2 = call_360
func_367 = relay.Function([], output)
mod['func_367'] = func_367
mod = relay.transform.InferType()(mod)
output = func_367()
func_368 = relay.Function([], output)
mutated_mod['func_368'] = func_368
mutated_mod = relay.transform.InferType()(mutated_mod)
func_367_call = mod.get_global_var('func_367')
func_368_call = mutated_mod.get_global_var('func_368')
call_379 = func_367_call()
call_380 = func_367_call()
uop_392 = relay.log2(call_379.astype('float64')) # shape=(12, 16, 2)
uop_394 = relay.log2(call_380.astype('float64')) # shape=(12, 16, 2)
output = uop_392
output2 = uop_394
func_404 = relay.Function([], output)
mod['func_404'] = func_404
mod = relay.transform.InferType()(mod)
output = func_404()
func_405 = relay.Function([], output)
mutated_mod['func_405'] = func_405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_153_call = mod.get_global_var('func_153')
func_154_call = mutated_mod.get_global_var('func_154')
call_418 = relay.TupleGetItem(func_153_call(), 0)
call_419 = relay.TupleGetItem(func_154_call(), 0)
output = call_418
output2 = call_419
func_426 = relay.Function([], output)
mod['func_426'] = func_426
mod = relay.transform.InferType()(mod)
mutated_mod['func_426'] = func_426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_426_call = mutated_mod.get_global_var('func_426')
call_427 = func_426_call()
output = call_427
func_428 = relay.Function([], output)
mutated_mod['func_428'] = func_428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_426_call = mod.get_global_var('func_426')
func_428_call = mutated_mod.get_global_var('func_428')
call_429 = func_426_call()
call_430 = func_426_call()
output = call_429
output2 = call_430
func_433 = relay.Function([], output)
mod['func_433'] = func_433
mod = relay.transform.InferType()(mod)
output = func_433()
func_434 = relay.Function([], output)
mutated_mod['func_434'] = func_434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_404_call = mod.get_global_var('func_404')
func_405_call = mutated_mod.get_global_var('func_405')
call_440 = func_404_call()
call_441 = func_404_call()
func_433_call = mod.get_global_var('func_433')
func_434_call = mutated_mod.get_global_var('func_434')
call_442 = func_433_call()
call_443 = func_433_call()
func_184_call = mod.get_global_var('func_184')
func_187_call = mutated_mod.get_global_var('func_187')
call_448 = relay.TupleGetItem(func_184_call(relay.reshape(call_440.astype('bool'), [12, 16, 2])), 0)
call_449 = relay.TupleGetItem(func_187_call(relay.reshape(call_440.astype('bool'), [12, 16, 2])), 0)
output = relay.Tuple([call_440,call_442,call_448,])
output2 = relay.Tuple([call_441,call_443,call_449,])
func_454 = relay.Function([], output)
mod['func_454'] = func_454
mod = relay.transform.InferType()(mod)
output = func_454()
func_455 = relay.Function([], output)
mutated_mod['func_455'] = func_455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_454_call = mod.get_global_var('func_454')
func_455_call = mutated_mod.get_global_var('func_455')
call_462 = relay.TupleGetItem(func_454_call(), 0)
call_463 = relay.TupleGetItem(func_455_call(), 0)
uop_466 = relay.sigmoid(call_462.astype('float64')) # shape=(12, 16, 2)
uop_468 = relay.sigmoid(call_463.astype('float64')) # shape=(12, 16, 2)
bop_471 = relay.minimum(call_462.astype('int8'), relay.reshape(uop_466.astype('int8'), relay.shape_of(call_462))) # shape=(12, 16, 2)
bop_474 = relay.minimum(call_463.astype('int8'), relay.reshape(uop_468.astype('int8'), relay.shape_of(call_463))) # shape=(12, 16, 2)
func_304_call = mod.get_global_var('func_304')
func_306_call = mutated_mod.get_global_var('func_306')
call_495 = func_304_call()
call_496 = func_304_call()
func_454_call = mod.get_global_var('func_454')
func_455_call = mutated_mod.get_global_var('func_455')
call_506 = relay.TupleGetItem(func_454_call(), 2)
call_507 = relay.TupleGetItem(func_455_call(), 2)
bop_514 = relay.floor_mod(bop_471.astype('float32'), relay.reshape(call_506.astype('float32'), relay.shape_of(bop_471))) # shape=(12, 16, 2)
bop_517 = relay.floor_mod(bop_474.astype('float32'), relay.reshape(call_507.astype('float32'), relay.shape_of(bop_474))) # shape=(12, 16, 2)
output = relay.Tuple([call_495,bop_514,])
output2 = relay.Tuple([call_496,bop_517,])
func_523 = relay.Function([], output)
mod['func_523'] = func_523
mod = relay.transform.InferType()(mod)
output = func_523()
func_524 = relay.Function([], output)
mutated_mod['func_524'] = func_524
mutated_mod = relay.transform.InferType()(mutated_mod)
func_454_call = mod.get_global_var('func_454')
func_455_call = mutated_mod.get_global_var('func_455')
call_531 = relay.TupleGetItem(func_454_call(), 1)
call_532 = relay.TupleGetItem(func_455_call(), 1)
output = relay.Tuple([call_531,])
output2 = relay.Tuple([call_532,])
func_543 = relay.Function([], output)
mod['func_543'] = func_543
mod = relay.transform.InferType()(mod)
output = func_543()
func_544 = relay.Function([], output)
mutated_mod['func_544'] = func_544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_225_call = mod.get_global_var('func_225')
func_226_call = mutated_mod.get_global_var('func_226')
call_556 = relay.TupleGetItem(func_225_call(), 0)
call_557 = relay.TupleGetItem(func_226_call(), 0)
var_560 = relay.var("var_560", dtype = "bool", shape = (12, 16, 2))#candidate|560|(12, 16, 2)|var|bool
bop_561 = relay.right_shift(call_556.astype('int32'), relay.reshape(var_560.astype('int32'), relay.shape_of(call_556))) # shape=(12, 16, 2)
bop_564 = relay.right_shift(call_557.astype('int32'), relay.reshape(var_560.astype('int32'), relay.shape_of(call_557))) # shape=(12, 16, 2)
output = relay.Tuple([bop_561,])
output2 = relay.Tuple([bop_564,])
func_565 = relay.Function([var_560,], output)
mod['func_565'] = func_565
mod = relay.transform.InferType()(mod)
mutated_mod['func_565'] = func_565
mutated_mod = relay.transform.InferType()(mutated_mod)
var_566 = relay.var("var_566", dtype = "bool", shape = (12, 16, 2))#candidate|566|(12, 16, 2)|var|bool
func_565_call = mutated_mod.get_global_var('func_565')
call_567 = func_565_call(var_566)
output = call_567
func_568 = relay.Function([var_566], output)
mutated_mod['func_568'] = func_568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_304_call = mod.get_global_var('func_304')
func_306_call = mutated_mod.get_global_var('func_306')
call_581 = func_304_call()
call_582 = func_304_call()
func_523_call = mod.get_global_var('func_523')
func_524_call = mutated_mod.get_global_var('func_524')
call_591 = relay.TupleGetItem(func_523_call(), 1)
call_592 = relay.TupleGetItem(func_524_call(), 1)
func_433_call = mod.get_global_var('func_433')
func_434_call = mutated_mod.get_global_var('func_434')
call_596 = func_433_call()
call_597 = func_433_call()
func_153_call = mod.get_global_var('func_153')
func_154_call = mutated_mod.get_global_var('func_154')
call_605 = relay.TupleGetItem(func_153_call(), 0)
call_606 = relay.TupleGetItem(func_154_call(), 0)
func_153_call = mod.get_global_var('func_153')
func_154_call = mutated_mod.get_global_var('func_154')
call_609 = relay.TupleGetItem(func_153_call(), 0)
call_610 = relay.TupleGetItem(func_154_call(), 0)
uop_611 = relay.tan(call_596.astype('float32')) # shape=(12, 16, 2)
uop_613 = relay.tan(call_597.astype('float32')) # shape=(12, 16, 2)
uop_619 = relay.cosh(uop_611.astype('float32')) # shape=(12, 16, 2)
uop_621 = relay.cosh(uop_613.astype('float32')) # shape=(12, 16, 2)
func_426_call = mod.get_global_var('func_426')
func_428_call = mutated_mod.get_global_var('func_428')
call_632 = func_426_call()
call_633 = func_426_call()
func_565_call = mod.get_global_var('func_565')
func_568_call = mutated_mod.get_global_var('func_568')
call_636 = relay.TupleGetItem(func_565_call(relay.reshape(call_596.astype('bool'), [12, 16, 2])), 0)
call_637 = relay.TupleGetItem(func_568_call(relay.reshape(call_596.astype('bool'), [12, 16, 2])), 0)
output = relay.Tuple([call_581,call_591,call_605,call_609,uop_619,call_632,call_636,])
output2 = relay.Tuple([call_582,call_592,call_606,call_610,uop_621,call_633,call_637,])
func_642 = relay.Function([], output)
mod['func_642'] = func_642
mod = relay.transform.InferType()(mod)
output = func_642()
func_643 = relay.Function([], output)
mutated_mod['func_643'] = func_643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_523_call = mod.get_global_var('func_523')
func_524_call = mutated_mod.get_global_var('func_524')
call_704 = relay.TupleGetItem(func_523_call(), 0)
call_705 = relay.TupleGetItem(func_524_call(), 0)
func_426_call = mod.get_global_var('func_426')
func_428_call = mutated_mod.get_global_var('func_428')
call_711 = func_426_call()
call_712 = func_426_call()
output = relay.Tuple([call_704,call_711,])
output2 = relay.Tuple([call_705,call_712,])
func_713 = relay.Function([], output)
mod['func_713'] = func_713
mod = relay.transform.InferType()(mod)
output = func_713()
func_714 = relay.Function([], output)
mutated_mod['func_714'] = func_714
mutated_mod = relay.transform.InferType()(mutated_mod)
const_745 = relay.const([[[4,-1,4,1,-6,-6,-3,4,9,-9,-9,-10,-4,9,4],[6,-7,-8,6,4,10,-8,8,-7,6,-4,6,7,9,-10],[1,1,-4,10,10,4,4,7,2,7,-9,2,-6,-7,-4],[-10,-2,4,9,4,7,-1,7,-1,1,-10,8,8,-2,1],[-10,2,1,6,9,-1,-9,7,2,9,-7,-4,1,-1,6],[7,-2,-8,5,4,7,2,10,3,7,-5,-9,1,10,-10],[-3,-4,8,-7,7,8,-7,-1,-8,-8,4,-1,-4,-2,-4]],[[3,-1,-2,9,3,3,2,-10,8,7,6,9,6,-2,8],[-1,3,7,3,7,4,7,-1,-10,6,-2,1,-10,7,-3],[7,-7,8,-6,-10,6,2,-1,-8,-9,-8,-7,-6,-6,-8],[-7,3,-3,-8,1,-1,-1,8,-5,2,-3,7,-1,-6,6],[-4,-6,7,-9,8,2,-6,-2,6,5,1,10,9,-3,-6],[8,3,8,-5,4,6,-5,-10,9,2,4,1,3,3,2],[6,1,5,-7,8,-6,-9,7,5,5,-7,3,3,7,-4]]], dtype = "uint32")#candidate|745|(2, 7, 15)|const|uint32
var_746 = relay.var("var_746", dtype = "uint32", shape = (2, 7, 15))#candidate|746|(2, 7, 15)|var|uint32
bop_747 = relay.multiply(const_745.astype('uint32'), relay.reshape(var_746.astype('uint32'), relay.shape_of(const_745))) # shape=(2, 7, 15)
uop_752 = relay.acosh(const_745.astype('float32')) # shape=(2, 7, 15)
func_153_call = mod.get_global_var('func_153')
func_154_call = mutated_mod.get_global_var('func_154')
call_756 = relay.TupleGetItem(func_153_call(), 0)
call_757 = relay.TupleGetItem(func_154_call(), 0)
uop_762 = relay.tan(bop_747.astype('float64')) # shape=(2, 7, 15)
func_543_call = mod.get_global_var('func_543')
func_544_call = mutated_mod.get_global_var('func_544')
call_766 = relay.TupleGetItem(func_543_call(), 0)
call_767 = relay.TupleGetItem(func_544_call(), 0)
bop_777 = relay.greater_equal(var_746.astype('bool'), relay.reshape(uop_752.astype('bool'), relay.shape_of(var_746))) # shape=(2, 7, 15)
func_433_call = mod.get_global_var('func_433')
func_434_call = mutated_mod.get_global_var('func_434')
call_783 = func_433_call()
call_784 = func_433_call()
func_454_call = mod.get_global_var('func_454')
func_455_call = mutated_mod.get_global_var('func_455')
call_790 = relay.TupleGetItem(func_454_call(), 1)
call_791 = relay.TupleGetItem(func_455_call(), 1)
func_523_call = mod.get_global_var('func_523')
func_524_call = mutated_mod.get_global_var('func_524')
call_809 = relay.TupleGetItem(func_523_call(), 1)
call_810 = relay.TupleGetItem(func_524_call(), 1)
bop_811 = relay.divide(uop_762.astype('float32'), relay.reshape(bop_777.astype('float32'), relay.shape_of(uop_762))) # shape=(2, 7, 15)
output = relay.Tuple([call_756,call_766,call_783,call_790,call_809,bop_811,])
output2 = relay.Tuple([call_757,call_767,call_784,call_791,call_810,bop_811,])
func_819 = relay.Function([var_746,], output)
mod['func_819'] = func_819
mod = relay.transform.InferType()(mod)
var_820 = relay.var("var_820", dtype = "uint32", shape = (2, 7, 15))#candidate|820|(2, 7, 15)|var|uint32
output = func_819(var_820)
func_821 = relay.Function([var_820], output)
mutated_mod['func_821'] = func_821
mutated_mod = relay.transform.InferType()(mutated_mod)
func_225_call = mod.get_global_var('func_225')
func_226_call = mutated_mod.get_global_var('func_226')
call_823 = relay.TupleGetItem(func_225_call(), 0)
call_824 = relay.TupleGetItem(func_226_call(), 0)
output = relay.Tuple([call_823,])
output2 = relay.Tuple([call_824,])
func_834 = relay.Function([], output)
mod['func_834'] = func_834
mod = relay.transform.InferType()(mod)
mutated_mod['func_834'] = func_834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_834_call = mutated_mod.get_global_var('func_834')
call_835 = func_834_call()
output = call_835
func_836 = relay.Function([], output)
mutated_mod['func_836'] = func_836
mutated_mod = relay.transform.InferType()(mutated_mod)
func_404_call = mod.get_global_var('func_404')
func_405_call = mutated_mod.get_global_var('func_405')
call_894 = func_404_call()
call_895 = func_404_call()
func_426_call = mod.get_global_var('func_426')
func_428_call = mutated_mod.get_global_var('func_428')
call_912 = func_426_call()
call_913 = func_426_call()
output = relay.Tuple([call_894,call_912,])
output2 = relay.Tuple([call_895,call_913,])
func_918 = relay.Function([], output)
mod['func_918'] = func_918
mod = relay.transform.InferType()(mod)
output = func_918()
func_919 = relay.Function([], output)
mutated_mod['func_919'] = func_919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_367_call = mod.get_global_var('func_367')
func_368_call = mutated_mod.get_global_var('func_368')
call_928 = func_367_call()
call_929 = func_367_call()
func_225_call = mod.get_global_var('func_225')
func_226_call = mutated_mod.get_global_var('func_226')
call_936 = relay.TupleGetItem(func_225_call(), 0)
call_937 = relay.TupleGetItem(func_226_call(), 0)
func_304_call = mod.get_global_var('func_304')
func_306_call = mutated_mod.get_global_var('func_306')
call_951 = func_304_call()
call_952 = func_304_call()
output = relay.Tuple([call_928,call_936,call_951,])
output2 = relay.Tuple([call_929,call_937,call_952,])
func_982 = relay.Function([], output)
mod['func_982'] = func_982
mod = relay.transform.InferType()(mod)
mutated_mod['func_982'] = func_982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_982_call = mutated_mod.get_global_var('func_982')
call_983 = func_982_call()
output = call_983
func_984 = relay.Function([], output)
mutated_mod['func_984'] = func_984
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1002 = relay.var("var_1002", dtype = "float64", shape = (5, 14, 6))#candidate|1002|(5, 14, 6)|var|float64
uop_1003 = relay.log2(var_1002.astype('float64')) # shape=(5, 14, 6)
output = relay.Tuple([uop_1003,])
output2 = relay.Tuple([uop_1003,])
func_1008 = relay.Function([var_1002,], output)
mod['func_1008'] = func_1008
mod = relay.transform.InferType()(mod)
var_1009 = relay.var("var_1009", dtype = "float64", shape = (5, 14, 6))#candidate|1009|(5, 14, 6)|var|float64
output = func_1008(var_1009)
func_1010 = relay.Function([var_1009], output)
mutated_mod['func_1010'] = func_1010
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1060 = relay.const([[[-8.411988,-5.948779,0.571577,4.974613,-4.422787,-8.641942,4.957967,-8.019251,2.993119,9.180267],[5.888748,-2.123387,-5.162192,-9.860376,-8.788829,-8.685846,-8.265986,-0.244163,8.898759,-8.787074],[5.527485,-0.712240,-3.177271,-9.312325,8.400088,-0.157774,3.688737,2.778965,-5.259039,3.795420]],[[0.004543,8.023662,-6.499215,-3.257370,-2.551464,2.248243,2.273951,-2.565784,-9.808521,-9.719112],[-4.953900,-9.692891,0.491490,2.627526,7.261617,-2.831889,7.801925,-7.708719,8.458719,3.401972],[6.587376,4.953556,-1.794391,5.912984,-3.579975,-4.657787,-5.040667,9.246655,-8.766860,7.722888]],[[8.150128,9.343593,-0.297287,-0.872866,-0.727420,5.682133,-7.930974,-5.731302,-4.078122,6.773953],[3.177297,2.555975,-2.599001,6.879868,2.529888,-2.649350,-5.750411,3.597776,-5.661961,-7.640640],[3.911411,-9.364379,6.150112,-7.854278,-2.136516,-1.139843,4.404970,9.721414,-0.595043,2.883804]],[[-4.075460,-9.112692,3.627501,6.048718,3.747807,-7.215154,9.601365,-6.596258,6.639202,-9.144408],[-7.240388,-7.792469,-7.620786,9.417196,-2.268886,-9.348502,3.484648,-9.785097,3.831142,-1.062422],[7.235284,1.879920,4.090227,2.850772,4.846281,2.893588,2.951988,5.269594,8.140984,-2.204989]],[[3.298984,-9.634986,-4.584341,9.940052,-8.166728,-0.235576,-8.971410,-8.285454,-1.921566,6.950753],[7.496306,5.123739,-5.391580,-4.647949,-9.897422,3.673625,-4.001015,-2.373880,-4.820308,-1.236606],[0.628682,7.988812,-8.463793,4.806862,1.256641,-6.059423,0.608944,7.914657,3.556213,-0.331968]],[[6.927123,2.258595,6.106888,-0.189537,-0.487912,5.275902,4.039977,1.342714,-7.739541,-4.665527],[9.426384,2.572243,3.400499,-0.912228,-9.099662,-9.390689,7.524608,3.834676,1.233251,-7.190609],[-3.266624,3.970084,-2.682509,-3.835372,9.034756,0.255539,9.410329,-0.305254,5.396881,9.799477]],[[6.558491,0.254362,-1.389943,3.615984,-2.917876,0.428670,0.455860,2.655670,2.829112,4.030826],[-9.880954,-4.609719,4.579174,-6.847293,5.568597,-5.202759,3.711309,9.357515,9.927826,1.597957],[2.896749,-6.968584,6.720533,-6.865978,1.547230,-4.398351,-7.503571,-7.542191,5.170720,3.378113]],[[-9.703971,3.785088,3.904534,2.541781,0.088414,2.636539,6.449531,-9.544307,3.577039,-8.995418],[-4.131558,-6.723089,4.956371,-7.610081,-9.487844,9.541012,0.196259,-1.592835,-8.747845,4.371649],[5.564962,-4.096854,9.636988,9.404205,0.583275,9.884385,-7.999357,4.960867,-8.118913,-7.454520]],[[8.397448,-2.064545,-6.034385,0.187108,-6.275339,1.468300,4.190522,0.545543,-8.431590,2.948362],[-2.895842,7.514597,0.736862,-5.567583,-1.358881,-1.673137,-8.664851,-9.059764,3.800500,3.911439],[0.382822,5.018465,-9.340845,0.877770,-2.138046,4.371871,3.994475,0.005904,3.153393,1.420395]]], dtype = "float32")#candidate|1060|(9, 3, 10)|const|float32
uop_1061 = relay.log2(const_1060.astype('float32')) # shape=(9, 3, 10)
func_426_call = mod.get_global_var('func_426')
func_428_call = mutated_mod.get_global_var('func_428')
call_1067 = func_426_call()
call_1068 = func_426_call()
output = relay.Tuple([uop_1061,call_1067,])
output2 = relay.Tuple([uop_1061,call_1068,])
func_1075 = relay.Function([], output)
mod['func_1075'] = func_1075
mod = relay.transform.InferType()(mod)
output = func_1075()
func_1076 = relay.Function([], output)
mutated_mod['func_1076'] = func_1076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_404_call = mod.get_global_var('func_404')
func_405_call = mutated_mod.get_global_var('func_405')
call_1082 = func_404_call()
call_1083 = func_404_call()
output = relay.Tuple([call_1082,])
output2 = relay.Tuple([call_1083,])
func_1084 = relay.Function([], output)
mod['func_1084'] = func_1084
mod = relay.transform.InferType()(mod)
mutated_mod['func_1084'] = func_1084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1084_call = mutated_mod.get_global_var('func_1084')
call_1085 = func_1084_call()
output = call_1085
func_1086 = relay.Function([], output)
mutated_mod['func_1086'] = func_1086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_642_call = mod.get_global_var('func_642')
func_643_call = mutated_mod.get_global_var('func_643')
call_1098 = relay.TupleGetItem(func_642_call(), 6)
call_1099 = relay.TupleGetItem(func_643_call(), 6)
var_1115 = relay.var("var_1115", dtype = "int32", shape = (12, 16, 2))#candidate|1115|(12, 16, 2)|var|int32
bop_1116 = relay.not_equal(call_1098.astype('bool'), relay.reshape(var_1115.astype('bool'), relay.shape_of(call_1098))) # shape=(12, 16, 2)
bop_1119 = relay.not_equal(call_1099.astype('bool'), relay.reshape(var_1115.astype('bool'), relay.shape_of(call_1099))) # shape=(12, 16, 2)
output = relay.Tuple([bop_1116,])
output2 = relay.Tuple([bop_1119,])
func_1133 = relay.Function([var_1115,], output)
mod['func_1133'] = func_1133
mod = relay.transform.InferType()(mod)
mutated_mod['func_1133'] = func_1133
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1134 = relay.var("var_1134", dtype = "int32", shape = (12, 16, 2))#candidate|1134|(12, 16, 2)|var|int32
func_1133_call = mutated_mod.get_global_var('func_1133')
call_1135 = func_1133_call(var_1134)
output = call_1135
func_1136 = relay.Function([var_1134], output)
mutated_mod['func_1136'] = func_1136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_433_call = mod.get_global_var('func_433')
func_434_call = mutated_mod.get_global_var('func_434')
call_1183 = func_433_call()
call_1184 = func_433_call()
output = call_1183
output2 = call_1184
func_1185 = relay.Function([], output)
mod['func_1185'] = func_1185
mod = relay.transform.InferType()(mod)
mutated_mod['func_1185'] = func_1185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1185_call = mutated_mod.get_global_var('func_1185')
call_1186 = func_1185_call()
output = call_1186
func_1187 = relay.Function([], output)
mutated_mod['func_1187'] = func_1187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_454_call = mod.get_global_var('func_454')
func_455_call = mutated_mod.get_global_var('func_455')
call_1196 = relay.TupleGetItem(func_454_call(), 0)
call_1197 = relay.TupleGetItem(func_455_call(), 0)
func_153_call = mod.get_global_var('func_153')
func_154_call = mutated_mod.get_global_var('func_154')
call_1220 = relay.TupleGetItem(func_153_call(), 0)
call_1221 = relay.TupleGetItem(func_154_call(), 0)
func_454_call = mod.get_global_var('func_454')
func_455_call = mutated_mod.get_global_var('func_455')
call_1223 = relay.TupleGetItem(func_454_call(), 0)
call_1224 = relay.TupleGetItem(func_455_call(), 0)
func_565_call = mod.get_global_var('func_565')
func_568_call = mutated_mod.get_global_var('func_568')
call_1226 = relay.TupleGetItem(func_565_call(relay.reshape(call_1196.astype('bool'), [12, 16, 2])), 0)
call_1227 = relay.TupleGetItem(func_568_call(relay.reshape(call_1196.astype('bool'), [12, 16, 2])), 0)
func_367_call = mod.get_global_var('func_367')
func_368_call = mutated_mod.get_global_var('func_368')
call_1228 = func_367_call()
call_1229 = func_367_call()
func_819_call = mod.get_global_var('func_819')
func_821_call = mutated_mod.get_global_var('func_821')
const_1247 = relay.const([1,5,-10,8,2,7,6,10,5,-7,-3,-3,9,-8,-9,-10,-7,-10,7,-10,-10,10,-2,9,-4,-2,-7,3,-6,1,-10,-8,6,-3,-5,-4,3,1,4,3,-10,6,-1,-3,8,4,5,-4,-9,-3,-3,7,1,-9,2,5,-10,-7,-8,10,4,-5,-8,-9,-7,9,-9,3,-8,5,8,-10,-10,1,-9,5,7,-4,10,-1,-6,-8,1,-5,6,7,-1,-4,5,-9,8,-10,6,9,-5,-5,-3,6,-4,2,-2,-6,7,-3,7,9,-8,10,10,1,2,-6,7,-8,4,3,-9,8,10,10,-3,-3,-5,6,2,3,-3,8,3,-5,6,-1,-6,2,-10,5,3,-6,-1,-6,-2,-7,-7,7,1,-5,9,-5,-6,-4,1,-2,7,3,-10,1,7,9,2,-4,-7,1,8,2,3,2,5,-10,-2,10,-3,4,-8,-4,10,-5,-6,4,2,-7,1,-3,-3,-9,-8,-7,-10,1,-5,-10,2,1,-2,3,10,-3,1,-7,8,9,7,-5,8,-6,-2,7,2,5,2,9], dtype = "uint32")#candidate|1247|(210,)|const|uint32
call_1246 = relay.TupleGetItem(func_819_call(relay.reshape(const_1247.astype('uint32'), [2, 7, 15])), 0)
call_1248 = relay.TupleGetItem(func_821_call(relay.reshape(const_1247.astype('uint32'), [2, 7, 15])), 0)
uop_1261 = relay.exp(call_1220.astype('float64')) # shape=(12, 16, 2)
uop_1263 = relay.exp(call_1221.astype('float64')) # shape=(12, 16, 2)
func_153_call = mod.get_global_var('func_153')
func_154_call = mutated_mod.get_global_var('func_154')
call_1269 = relay.TupleGetItem(func_153_call(), 0)
call_1270 = relay.TupleGetItem(func_154_call(), 0)
output = relay.Tuple([call_1196,call_1223,call_1226,call_1228,call_1246,const_1247,uop_1261,call_1269,])
output2 = relay.Tuple([call_1197,call_1224,call_1227,call_1229,call_1248,const_1247,uop_1263,call_1270,])
func_1299 = relay.Function([], output)
mod['func_1299'] = func_1299
mod = relay.transform.InferType()(mod)
mutated_mod['func_1299'] = func_1299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1299_call = mutated_mod.get_global_var('func_1299')
call_1300 = func_1299_call()
output = call_1300
func_1301 = relay.Function([], output)
mutated_mod['func_1301'] = func_1301
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1302 = relay.var("var_1302", dtype = "float32", shape = (6, 11, 14))#candidate|1302|(6, 11, 14)|var|float32
uop_1303 = relay.log2(var_1302.astype('float32')) # shape=(6, 11, 14)
var_1307 = relay.var("var_1307", dtype = "float32", shape = (6, 11, 14))#candidate|1307|(6, 11, 14)|var|float32
bop_1308 = relay.mod(uop_1303.astype('float64'), relay.reshape(var_1307.astype('float64'), relay.shape_of(uop_1303))) # shape=(6, 11, 14)
output = bop_1308
output2 = bop_1308
func_1318 = relay.Function([var_1302,var_1307,], output)
mod['func_1318'] = func_1318
mod = relay.transform.InferType()(mod)
mutated_mod['func_1318'] = func_1318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1318_call = mutated_mod.get_global_var('func_1318')
var_1320 = relay.var("var_1320", dtype = "float32", shape = (6, 11, 14))#candidate|1320|(6, 11, 14)|var|float32
var_1321 = relay.var("var_1321", dtype = "float32", shape = (6, 11, 14))#candidate|1321|(6, 11, 14)|var|float32
call_1319 = func_1318_call(var_1320,var_1321,)
output = call_1319
func_1322 = relay.Function([var_1320,var_1321,], output)
mutated_mod['func_1322'] = func_1322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_543_call = mod.get_global_var('func_543')
func_544_call = mutated_mod.get_global_var('func_544')
call_1350 = relay.TupleGetItem(func_543_call(), 0)
call_1351 = relay.TupleGetItem(func_544_call(), 0)
output = relay.Tuple([call_1350,])
output2 = relay.Tuple([call_1351,])
func_1357 = relay.Function([], output)
mod['func_1357'] = func_1357
mod = relay.transform.InferType()(mod)
mutated_mod['func_1357'] = func_1357
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1357_call = mutated_mod.get_global_var('func_1357')
call_1358 = func_1357_call()
output = call_1358
func_1359 = relay.Function([], output)
mutated_mod['func_1359'] = func_1359
mutated_mod = relay.transform.InferType()(mutated_mod)
func_543_call = mod.get_global_var('func_543')
func_544_call = mutated_mod.get_global_var('func_544')
call_1379 = relay.TupleGetItem(func_543_call(), 0)
call_1380 = relay.TupleGetItem(func_544_call(), 0)
output = relay.Tuple([call_1379,])
output2 = relay.Tuple([call_1380,])
func_1385 = relay.Function([], output)
mod['func_1385'] = func_1385
mod = relay.transform.InferType()(mod)
output = func_1385()
func_1386 = relay.Function([], output)
mutated_mod['func_1386'] = func_1386
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1413 = relay.const([[[-10,-6,9,10,7,3,-1,-3,9,6,10],[-1,-7,-5,8,-10,4,-7,-3,-8,-9,8],[5,10,-5,-8,-4,4,-5,8,-9,-2,-6],[6,8,-2,7,4,3,8,10,-3,-6,-8],[5,4,6,-9,-7,-4,10,-1,-5,-9,-8]],[[-6,-6,5,-5,-2,-10,-4,-2,-1,-7,3],[10,-4,-10,-3,1,-9,8,8,-8,4,9],[-4,-1,2,-1,-7,1,-6,-6,9,10,-4],[-1,-4,7,7,-7,8,8,-8,-7,10,6],[-6,8,-10,3,-9,-10,-3,10,-4,-1,-7]],[[-2,-7,-9,4,-4,-10,8,-1,7,7,-4],[6,-2,-2,-1,-1,-3,-2,7,2,10,6],[-5,1,8,9,2,-7,-6,-7,-8,-9,-9],[7,-9,-9,-10,-7,1,-7,7,10,-3,-4],[-6,3,-9,6,5,6,-2,-3,10,-9,9]],[[10,4,-7,-7,-4,-2,-8,3,-1,-9,4],[-1,-8,-8,-10,3,-7,1,3,-7,-2,8],[-1,6,-9,6,8,10,-6,1,9,7,-2],[-2,-6,-4,9,8,2,2,9,-5,-5,1],[5,-1,-9,-2,7,-9,-4,-1,6,-5,-3]],[[10,-6,9,9,-7,5,9,-8,-6,-5,-10],[-8,4,-2,2,9,-7,4,8,-7,8,-3],[-7,-9,6,8,5,-8,-1,1,6,-5,4],[-1,5,-7,2,-3,1,-2,8,-4,5,5],[10,9,-5,-9,4,-1,-9,-3,8,-8,7]],[[-7,-9,7,1,-9,-7,9,3,-1,7,9],[8,-5,-7,5,-4,-9,3,8,-8,-7,7],[7,1,10,-7,3,10,-2,-4,1,1,-2],[3,-6,-7,6,-8,-6,10,-8,3,-4,3],[10,-5,7,8,-8,-9,4,9,2,4,6]],[[-1,2,-8,-7,-2,-8,5,-1,-5,5,-7],[-10,2,4,9,1,4,2,-10,3,-5,9],[4,-4,-10,5,-2,4,6,-2,-7,4,8],[5,6,-10,-9,-2,8,4,-9,-7,-3,-6],[8,5,-3,-9,7,-1,-4,-4,9,-5,-6]],[[-8,7,7,-6,-10,-1,4,-6,-6,-8,5],[-7,2,7,-4,-8,7,8,7,6,-10,6],[2,-6,-4,5,-8,-8,-8,-10,7,5,-5],[-9,8,-4,4,-2,-2,9,7,-5,6,-5],[-8,9,5,1,-8,4,8,4,-8,10,-7]],[[7,-3,-8,6,7,8,-9,-1,-3,-3,-5],[-7,-2,-5,8,-3,7,7,-7,7,-7,10],[-8,-8,-2,-1,1,7,-6,8,-8,7,7],[9,7,7,-4,1,2,4,2,2,-5,1],[-1,5,1,5,8,-1,-3,-10,-7,-9,-2]],[[-2,10,2,-3,9,3,5,8,10,-3,10],[1,-3,10,-7,4,-1,-3,2,-5,2,-4],[1,-5,7,-4,-6,-4,-5,-8,9,4,-6],[2,-5,-8,-4,-1,6,6,6,8,-6,10],[9,4,1,5,-6,-5,3,-5,-10,3,-6]],[[7,10,-5,-8,-8,4,4,-9,-3,7,4],[-5,-8,-9,9,10,7,-3,-4,7,9,-3],[5,1,7,-7,-7,-3,-7,6,8,-4,-3],[7,-8,-1,-6,-10,-8,-10,-1,9,-1,-5],[-5,-6,6,-7,-5,-8,9,-1,-8,5,-4]],[[-3,3,-6,-2,-3,-1,-9,-7,6,3,8],[-5,-4,-10,1,3,2,5,10,-7,6,2],[-5,-4,-4,4,8,10,4,-10,-7,-8,8],[-5,3,-1,-1,4,5,-6,-6,10,-2,5],[-2,3,-7,8,-6,-4,-6,8,2,-3,4]],[[4,2,4,-6,-1,4,-8,9,-6,9,-4],[7,-4,7,-5,-9,-1,-5,-4,-3,-9,-9],[8,3,2,6,-10,-1,-1,4,-7,5,3],[-4,10,1,4,8,-9,8,4,-9,-8,-1],[-9,6,-7,6,2,-8,-7,4,9,7,-3]],[[-9,-10,3,1,6,-8,-7,-5,6,5,10],[1,5,-5,9,-7,5,9,5,2,3,6],[-7,-5,10,7,3,-5,-9,3,8,-8,-9],[-3,-8,-8,4,-1,6,-4,-5,6,10,-8],[-2,6,-1,3,1,6,2,10,-9,9,-8]],[[-4,5,-3,-3,-1,-2,-5,1,-4,-5,-2],[4,2,-5,-1,-5,6,-4,2,-9,-2,-2],[-3,6,-5,-8,9,3,7,4,8,4,-7],[2,8,4,2,9,-9,3,-10,-3,4,10],[-3,-3,4,-7,-8,2,-2,-7,10,-8,-3]],[[-3,1,-1,1,8,8,4,-7,-4,-10,2],[-1,-4,5,10,-4,-2,-10,-10,6,4,7],[7,9,-10,6,-2,-1,9,-10,-5,-1,-9],[-1,1,-5,3,-3,8,2,2,10,-6,-10],[-6,-4,-7,9,8,-5,7,-6,-3,-1,-10]]], dtype = "int32")#candidate|1413|(16, 5, 11)|const|int32
var_1414 = relay.var("var_1414", dtype = "int32", shape = (16, 5, 11))#candidate|1414|(16, 5, 11)|var|int32
bop_1415 = relay.greater(const_1413.astype('bool'), relay.reshape(var_1414.astype('bool'), relay.shape_of(const_1413))) # shape=(16, 5, 11)
func_1185_call = mod.get_global_var('func_1185')
func_1187_call = mutated_mod.get_global_var('func_1187')
call_1419 = func_1185_call()
call_1420 = func_1185_call()
bop_1430 = relay.mod(var_1414.astype('float64'), relay.reshape(const_1413.astype('float64'), relay.shape_of(var_1414))) # shape=(16, 5, 11)
output = relay.Tuple([bop_1415,call_1419,bop_1430,])
output2 = relay.Tuple([bop_1415,call_1420,bop_1430,])
func_1439 = relay.Function([var_1414,], output)
mod['func_1439'] = func_1439
mod = relay.transform.InferType()(mod)
mutated_mod['func_1439'] = func_1439
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1440 = relay.var("var_1440", dtype = "int32", shape = (16, 5, 11))#candidate|1440|(16, 5, 11)|var|int32
func_1439_call = mutated_mod.get_global_var('func_1439')
call_1441 = func_1439_call(var_1440)
output = call_1441
func_1442 = relay.Function([var_1440], output)
mutated_mod['func_1442'] = func_1442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_834_call = mod.get_global_var('func_834')
func_836_call = mutated_mod.get_global_var('func_836')
call_1474 = relay.TupleGetItem(func_834_call(), 0)
call_1475 = relay.TupleGetItem(func_836_call(), 0)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
const_1480 = relay.const([[2.469497],[-4.993945],[8.635369],[-4.842691],[8.756474],[1.377504],[5.185034],[-1.477560],[1.570216],[-9.674794],[-3.231027],[4.761734],[-6.840955],[-2.564072],[-6.281291],[7.524292],[3.826907],[9.924149],[5.166304],[-4.182543],[3.258172],[0.430182],[8.827154],[8.568380],[-3.754823],[2.387958],[-1.397067],[7.094551],[0.373087],[9.233393],[8.345563],[7.736223],[8.368657],[1.188171],[3.380620],[0.072058],[3.174683],[2.478993],[-1.297060],[3.552001],[-7.784866],[-1.744094],[6.033640],[5.609175],[9.050710],[5.859059],[-3.398463],[-4.543825],[1.192276],[-1.653076],[1.714336],[-6.933146],[-4.953410],[3.921594],[-6.314340],[1.107698],[9.834765],[9.738325],[7.895652],[6.945831],[9.967035],[-7.971296],[-9.427454],[6.219001],[-3.774026],[-2.419192],[-2.546085],[0.286577],[-8.241232],[4.172113],[7.967306],[4.026330],[-0.824095],[-7.368947],[3.694626],[8.635022],[-9.716406],[-2.017488],[-2.941100],[-0.170395],[4.004891],[-8.656635],[7.965304],[-6.868168],[-3.624241],[-8.002066],[-3.539925],[1.594178],[-6.204442],[9.435768],[2.940218],[0.908561],[-1.430675],[-4.813316],[2.486494],[6.585818],[2.844248],[-1.534573],[8.411841],[-9.024475],[3.721197],[-9.450889],[-9.244243],[-4.199383],[5.429562],[6.090784],[-0.643471],[-5.094902],[-5.879176],[9.933968],[1.418791],[8.782914],[-3.750372],[-5.189475],[-5.989285],[-5.783901],[6.315244],[-3.578627],[-6.155521],[1.388627],[-7.593145],[-3.540957],[1.091812],[4.899864],[-3.242867],[5.776284],[4.495416],[-3.849597],[8.051357],[-4.061611],[-4.613259],[3.992620],[1.993513],[3.442786],[-8.463793],[8.179474],[4.384058],[-9.429816],[-4.759248],[6.441474],[-3.944511],[-2.868243],[8.524021],[-1.329573],[7.187393],[-3.038696],[6.656238],[-4.458862],[6.381623],[-1.404588],[-4.479661],[-3.922053],[8.434849],[-1.418738],[-9.259314],[-0.811213],[-0.482203],[9.259153],[-9.049398],[-1.004461],[-5.539681],[4.541073],[-8.605539],[-5.456908],[7.971730],[-7.777595],[-6.338662],[-1.900811],[6.719418],[0.457588],[-4.392423],[-2.404329],[-1.108006],[-3.808629],[9.071446],[2.443879],[8.228127],[4.001087],[-4.030548],[-5.745917],[-5.683310],[0.289356],[3.638224],[2.578665],[-9.760656],[8.123684],[-6.808297],[4.635857],[5.029110],[7.857494],[4.966145],[-3.927928],[7.728650],[-6.995992],[0.204460],[-4.069639],[6.775351],[-7.932000],[6.719637],[9.841962],[-6.314306],[-4.785943],[7.394992],[4.320067],[9.783302],[1.558740],[0.874167],[0.009121],[-6.679791],[-6.815162],[-9.885418],[9.586043],[-3.956958],[8.759864],[3.978940],[2.650175],[3.163561],[3.311264],[-5.808794],[9.007614],[1.213165],[-3.431850],[-4.947031],[-5.270317],[2.638809],[-6.932391],[8.887711],[-9.105637],[4.887479],[6.621810],[-3.810771],[-8.130257],[-8.540931],[-9.929230],[-5.964202],[-6.825043],[9.408219],[6.994717],[-8.020347],[-5.682788],[-1.754909],[-1.862316],[-1.218419],[-9.797855],[-5.781143],[8.400741],[-5.418643],[-1.392051],[9.706067],[1.642757],[-5.929212],[9.988517],[-5.435017],[6.188156],[-7.615422],[2.517583],[-5.899613],[-5.816094],[-0.769525],[-7.065372],[-9.331712],[1.994068],[1.198653],[4.820536],[3.733367],[-6.787743],[-1.082197],[9.770829],[-3.684718],[-0.004004],[-1.870454],[-3.498877],[0.202850],[9.434109],[2.066636],[-3.587797],[1.375943],[-1.217922],[7.636806],[7.197152],[3.029205],[-4.900751],[-4.384338],[-2.342708],[-7.334954],[5.626413],[-4.418726],[0.513004],[3.800178],[2.449747],[-5.829705],[-0.429285],[-1.990178],[-0.397982],[4.622624],[-4.069204],[4.337403],[-5.517882],[-9.206922],[4.100373],[9.954218],[9.410472],[-0.517385],[0.373959],[0.317719],[-8.315234],[-1.088451],[-2.386839],[6.817383],[-7.737593],[-0.106805],[8.857502],[3.227669],[0.111494],[0.478958],[-1.492199],[-3.719340],[-5.986020],[-7.777540],[-6.720829],[5.069081],[9.125162],[9.771626],[-5.992404],[-6.378130],[2.747132],[2.561698],[8.244943],[3.189702],[-8.508533],[7.176369],[7.149792],[-2.976513],[-4.204264],[-2.947598],[-1.536596],[0.138204],[3.761019],[2.439606],[8.062614],[6.433799],[4.069863],[-1.349406],[6.263290],[9.733955],[-2.215845],[1.986372],[-4.585253],[6.493867],[-7.553977],[8.229482],[9.123360],[3.798323],[-3.400070],[-4.219584],[-8.124053],[-1.306536],[-9.956736],[-0.298911],[-8.540662],[0.885857],[-9.159515],[2.601333],[-4.480221],[9.229447],[-0.766879],[-9.214730],[1.686151],[-8.379757],[-4.403048],[-8.476991],[-7.941350],[-5.026025],[2.269403],[6.614688],[6.662178],[-4.156426],[6.484293],[-7.262481],[-3.140161],[-4.192440],[1.058931],[0.994007],[-6.611432],[-8.254273],[-2.592230],[-6.574907],[4.221486],[-3.724196],[2.470978],[3.899913],[-6.097959],[7.747224],[5.461780],[-2.134440],[1.984740],[-2.561736],[3.127704],[-8.702909],[6.039357],[-5.050392],[4.969573],[6.408662],[-6.056918],[9.816463],[1.191749],[-8.958209],[-5.896842],[3.897565],[8.685074],[0.975298],[-4.245059],[9.627149],[4.308922],[-5.647965],[-9.228796],[6.073729],[6.646592],[8.714898],[-0.852664],[2.566884],[6.632705],[1.604752],[5.378439],[8.483003],[-9.708097],[-5.105366],[-2.918774],[-7.838434],[7.170910],[-0.365843],[-2.946159],[6.542475],[-6.371519],[8.778646],[3.072708],[-2.132117],[-9.550244],[-5.841136],[-3.303618],[-7.578879],[-7.258813],[-2.872329],[9.493975],[1.603942],[4.256255],[-4.532712],[4.806397],[4.951671],[-5.289038],[-1.814433],[9.275705],[-5.722995],[-0.111594],[-6.915003],[-1.251866],[-9.399690],[9.820218],[1.063305],[0.025250],[4.018527],[0.678798],[-1.376043],[7.873478],[-0.200052],[-0.550579],[4.916116],[-1.503821],[2.519371],[-2.202651],[4.916424],[4.202813],[9.313729],[-9.053917],[5.008998],[8.552565],[-8.491282],[-2.028625],[5.839321],[-1.996149],[-6.755165],[-2.172503],[3.107347],[8.910429],[-6.795121],[-8.761683],[2.620434],[6.895998],[-7.058788],[6.553207],[9.394194],[-9.264327],[2.194701],[5.238102],[-6.417463],[3.498885],[-1.020825],[-9.224772],[-1.147123],[3.999450],[1.148967],[-8.521680],[9.074385],[0.911831],[-0.965337],[0.109918],[-8.848670],[6.622036],[-2.422491],[-7.487231],[6.584809],[8.498572],[-6.474127],[2.327506],[-6.562021],[5.711670],[-2.008010],[-8.040674],[3.238086],[3.123621],[-2.050947],[2.143100],[-7.413388],[4.287700],[5.966630],[6.951213],[3.408356],[2.282266],[-1.164663],[-2.414540],[8.533475],[-1.921720],[8.768857],[7.020301],[-0.108043],[-3.166502],[4.148811],[4.785558],[4.008762],[-6.457092],[1.189399],[6.555432],[9.290587],[-1.280361],[5.759301],[-5.862130],[-2.960798],[-6.077963],[7.922585],[-1.406135],[-8.719411],[-2.712590],[-6.648127],[4.000581],[-1.227807],[9.490811],[6.318527],[-4.291790],[6.144784],[-0.070326],[5.450725],[1.763556],[2.410044],[-1.989164],[9.041321],[-1.516949],[8.420100],[8.828013],[2.840647],[7.973428],[-8.403380],[4.569366],[4.875116],[-8.169509],[-3.570583],[5.762038],[8.405129],[4.240852],[-0.678947],[5.649705],[-5.173448],[0.285805],[5.427844],[5.198404],[1.695848],[-2.951200],[0.533720],[1.745165],[-4.784428],[4.076117],[-7.330254],[-9.880276],[1.083896],[-3.063518],[7.092840],[1.057182],[-8.351131],[-0.592938],[8.601502],[-0.470878],[-3.932799],[8.063492],[-6.125897],[7.331843],[-4.029657],[8.247165],[1.857132],[6.634800],[8.188087],[8.214313],[8.694419],[-4.377401],[8.195337],[8.469855],[-6.958269],[-8.943353],[7.866618],[0.588783],[-8.615736],[-9.907228],[4.189318],[-6.582268],[9.301909],[-8.680777],[5.633113],[-7.470661],[-9.614448],[-2.699595],[9.844350],[1.745647],[4.825098],[-4.828963],[9.514943],[-4.021747],[-0.918962],[-8.236533],[-9.611520],[2.598411],[-0.160501],[-7.727278],[5.289398],[4.844739],[9.747928],[3.718664],[1.724760],[2.624148],[-6.585662],[4.486351],[9.724898],[-9.036990],[-3.065857],[3.100187],[1.055569],[8.121489],[-3.973961],[1.017979],[-1.107600],[-8.579640],[7.287468],[-4.625042],[-2.077713],[9.896663],[5.214638],[-8.708575],[6.124621],[2.364018],[9.732558],[-2.508415],[7.759765],[6.000671],[-9.515718],[1.701567],[6.695747],[-0.466367],[3.697505],[7.324384],[-3.266885],[3.970062],[-3.871556],[-3.879200],[-6.330380],[2.097106],[0.540999],[-7.517673],[6.774648],[-8.475531],[-3.871883],[-2.339939],[0.805657],[-2.468427],[0.911919],[-0.361717],[6.069249],[-5.629695],[2.412324],[9.542492],[-1.291998],[-5.586322],[-4.017124],[-6.589470],[-6.264844],[2.641148],[-0.135662],[-2.353976],[1.077240],[-2.323628],[-3.756360],[-1.485964],[-9.903168],[9.520735],[-0.667395],[6.010296],[-1.661060],[-9.417412],[-6.020881],[-1.104036],[4.025211],[-3.322562],[-2.779710],[-3.544355],[3.175408],[-8.916428],[8.310414],[4.180803],[7.294319],[-1.700326],[0.030072],[-4.267137],[4.386062],[0.660558],[0.344724],[-1.043554],[5.647382],[-5.210089],[0.957670],[7.533657],[-1.816183],[-1.465499],[6.729092],[5.529622],[9.704646],[-7.317662],[-9.718806],[-1.831030],[0.818592],[2.903320],[9.179082],[4.444712],[-5.727536],[-7.924800],[-7.533769],[5.581998],[-2.308720],[5.557455],[6.372690],[-8.131447],[-1.618613],[-8.121785],[-6.245335],[-6.901702],[-4.933524],[-4.312683],[3.115829],[-4.467760],[-2.373246],[9.423071],[6.767419],[7.949430],[-0.707864],[8.095628],[6.975516],[-0.521895],[-0.356671],[-6.679339],[1.753706],[-6.404949],[9.875662],[-6.431085],[-2.998699],[-8.420321],[5.437005],[-2.450000],[-7.627795],[-8.793304],[-6.966127],[9.946129],[-1.674012],[6.633738],[-0.527106],[5.732830],[-4.567372],[6.745030],[-2.707622],[-4.906367],[-1.735866],[0.885171],[-8.653493],[-3.318688],[3.600895],[6.405158],[-7.742203],[-6.593499],[8.279838],[8.368919],[0.665012],[5.973734],[-7.601914],[5.808677],[-7.861012],[-3.129627],[5.392201],[7.369758],[5.590488],[-7.038980],[-2.604496],[-9.657652],[-3.383338],[3.788254],[-3.695287],[4.786789],[3.414287],[6.610380],[0.933788],[4.564827],[-7.087934],[6.775173],[2.744716],[0.421860],[-2.573676],[-5.694746],[7.368183],[-9.979900],[0.160075],[5.743052],[-5.361298],[1.732112],[-1.062987],[-1.452835],[-8.296941],[2.996431],[5.657985],[-2.741041],[8.657828],[7.731245],[8.192142],[9.443733],[-6.293462],[7.936094],[8.518231],[3.350796],[2.817211],[-1.698742],[6.348443],[-1.512814],[-0.301277],[-9.774058],[-0.413796],[-0.070555],[-1.069547],[7.266673],[9.990579],[-3.890528],[-0.097375],[0.073269]], dtype = "float32")#candidate|1480|(864, 1)|const|float32
call_1479 = relay.TupleGetItem(func_261_call(relay.reshape(const_1480.astype('float32'), [12, 8, 9])), 0)
call_1481 = relay.TupleGetItem(func_263_call(relay.reshape(const_1480.astype('float32'), [12, 8, 9])), 0)
func_1439_call = mod.get_global_var('func_1439')
func_1442_call = mutated_mod.get_global_var('func_1442')
const_1484 = relay.const([[-2,-7,-9,-4,5,5,8,5,-7,-9,-3,6,-2,-6,2,8,-5,4,8,-4,-3,-4,4,-2,4,-9,-4,8,3,-4,5,10,7,-3,-3,7,5,4,-3,-4,10,1,-10,4,2,-10,-10,-7,6,3,9,3,3,5,8,4,-5,-3,-3,-8,-5,-4,-9,-1,4,-4,3,-9,7,-4,-5,2,-3,-3,-2,-5,-1,9,1,5,-3,8,-6,-6,-3,5,-1,6,-2,2,3,-10,-6,2,-10,-3,-6,2,-10,-3,9,8,7,-5,6,2,5,-2,2,8,-1,-6,4,8,-6,-6,1,8,10,8,9,3,-1,-4,-9,6,7,-8,1,4,7,6,-6,7,-8,-1,-4,-10,1,1,-10,1,-10,-8,-5,2,-6,1,3,-9,-2,7,-7,4,-4,-10,-9,-4,2,-1,6,-8,-2,-4,8,7,4,-7,-2,10,3,2,3,-2,-8,1,-8,6,-9,-6,-2,6,-8,8,3,8,10,-9,-8,7,7,9,8,-3,6,3,-4,-5,-3,2,2,3,10,4,-6,-5,10,6,1,-6,-1,-6,-9,7,5,9,9,-7,5,-8],[-4,-4,7,4,-3,5,-1,-1,2,-2,5,-2,3,-3,3,-1,-4,-1,9,9,8,-6,-4,9,2,3,-5,4,-6,-8,8,-4,-6,-3,2,7,-3,1,7,-3,3,8,3,-6,9,-6,3,1,-8,-6,-6,4,-5,9,5,3,-8,-6,5,9,-5,-2,8,-10,10,9,-9,5,6,-6,-6,10,1,6,-7,-3,2,1,-1,-6,-6,-6,6,9,-5,-6,5,8,2,-6,-9,-3,4,-8,-6,-5,9,-1,3,10,6,-3,-2,1,-3,6,5,2,5,6,6,6,-3,4,-7,-5,10,6,-7,7,5,3,-5,9,8,-1,-7,2,4,-7,8,-5,-10,-2,1,10,-5,6,-9,-7,-2,-1,-7,-10,-7,-3,-7,-5,1,-5,-9,8,7,1,1,-4,8,4,8,-6,9,2,-8,-4,-6,-3,3,8,-7,7,-9,-1,-4,-2,-8,-9,-6,4,2,2,6,-5,-9,8,-4,-4,-4,9,1,-2,10,6,4,9,-10,4,-8,-5,-1,-1,-8,7,-1,1,10,10,7,-5,8,7,-4,-3,9,9,1,-7,6,-2,-4,8],[-10,-3,6,8,-1,1,-7,2,-2,-7,3,-5,-10,8,2,8,-4,-1,-9,4,5,9,-2,7,2,-9,8,3,-1,-9,-7,-8,-8,-1,9,10,5,-5,8,10,-6,4,5,9,10,-10,7,-10,-7,3,-8,-10,-10,-9,7,-10,-2,-6,-6,4,6,-3,-2,-7,3,4,3,-6,1,3,9,-2,10,10,6,1,8,5,8,8,4,-7,-10,-9,-2,-8,6,2,9,-1,5,-6,-8,2,5,-9,4,5,1,-4,4,2,1,5,9,6,10,5,-5,3,-7,-10,-10,-6,8,-2,1,2,1,3,-5,-3,2,-10,7,8,8,8,10,-9,-1,1,-6,-5,2,8,-8,2,-1,7,-8,1,-3,-5,2,-3,6,6,-9,-10,8,8,-9,5,3,-7,9,8,-6,4,9,-2,1,7,-8,1,-5,1,9,3,2,-4,7,-2,7,2,3,-10,-1,-4,-4,-4,-4,-2,-4,7,-6,-6,7,7,-4,-1,-4,-1,6,3,-8,8,3,-7,8,3,-8,-6,-7,-8,-3,-7,-10,3,4,5,-2,-6,-4,3,8,5,-7,1],[-5,6,-10,6,-3,-3,4,1,-2,2,-1,-7,3,4,-2,-5,-4,6,5,-1,10,5,5,-9,-2,-2,-7,1,10,1,10,10,8,9,9,-2,-5,10,-1,-6,1,6,-8,10,-2,-1,-9,-8,10,-2,7,-5,-1,6,-5,4,2,-4,9,-10,6,-5,4,-4,3,3,-10,-4,-5,-2,3,-8,8,-7,7,7,-9,-8,8,-9,-8,10,-1,8,5,8,-7,-4,2,3,-9,3,-3,-2,5,-9,-2,-10,3,10,-1,7,7,-5,5,8,-8,-1,-4,-1,4,3,-9,10,-2,-2,-9,2,-2,-2,-5,-2,-3,-2,-8,7,3,8,4,3,-8,-8,-6,2,-7,7,-7,3,-2,1,9,1,-10,3,-9,-8,3,-4,8,9,2,-7,6,1,6,7,-9,-7,-9,1,-9,5,-6,-3,6,-10,-7,-5,9,-1,7,-2,8,3,2,-5,2,-2,-10,-5,-6,-3,3,8,-6,-9,-8,-7,-4,6,-4,-8,-3,-7,7,7,6,-8,10,1,4,-6,4,-1,-6,4,-9,6,-5,3,4,5,2,7,9,5,-9,-8,-6,1]], dtype = "int32")#candidate|1484|(4, 220)|const|int32
call_1483 = relay.TupleGetItem(func_1439_call(relay.reshape(const_1484.astype('int32'), [16, 5, 11])), 2)
call_1485 = relay.TupleGetItem(func_1442_call(relay.reshape(const_1484.astype('int32'), [16, 5, 11])), 2)
var_1486 = relay.var("var_1486", dtype = "float32", shape = (864, 13))#candidate|1486|(864, 13)|var|float32
bop_1487 = relay.subtract(const_1480.astype('int16'), var_1486.astype('int16')) # shape=(864, 13)
func_454_call = mod.get_global_var('func_454')
func_455_call = mutated_mod.get_global_var('func_455')
call_1491 = relay.TupleGetItem(func_454_call(), 2)
call_1492 = relay.TupleGetItem(func_455_call(), 2)
output = relay.Tuple([call_1474,call_1479,call_1483,const_1484,bop_1487,call_1491,])
output2 = relay.Tuple([call_1475,call_1481,call_1485,const_1484,bop_1487,call_1492,])
func_1499 = relay.Function([var_1486,], output)
mod['func_1499'] = func_1499
mod = relay.transform.InferType()(mod)
mutated_mod['func_1499'] = func_1499
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1500 = relay.var("var_1500", dtype = "float32", shape = (864, 13))#candidate|1500|(864, 13)|var|float32
func_1499_call = mutated_mod.get_global_var('func_1499')
call_1501 = func_1499_call(var_1500)
output = call_1501
func_1502 = relay.Function([var_1500], output)
mutated_mod['func_1502'] = func_1502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_713_call = mod.get_global_var('func_713')
func_714_call = mutated_mod.get_global_var('func_714')
call_1506 = relay.TupleGetItem(func_713_call(), 1)
call_1507 = relay.TupleGetItem(func_714_call(), 1)
output = relay.Tuple([call_1506,])
output2 = relay.Tuple([call_1507,])
func_1518 = relay.Function([], output)
mod['func_1518'] = func_1518
mod = relay.transform.InferType()(mod)
mutated_mod['func_1518'] = func_1518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1518_call = mutated_mod.get_global_var('func_1518')
call_1519 = func_1518_call()
output = call_1519
func_1520 = relay.Function([], output)
mutated_mod['func_1520'] = func_1520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_713_call = mod.get_global_var('func_713')
func_714_call = mutated_mod.get_global_var('func_714')
call_1562 = relay.TupleGetItem(func_713_call(), 1)
call_1563 = relay.TupleGetItem(func_714_call(), 1)
func_304_call = mod.get_global_var('func_304')
func_306_call = mutated_mod.get_global_var('func_306')
call_1564 = func_304_call()
call_1565 = func_304_call()
bop_1572 = relay.equal(call_1564.astype('bool'), relay.reshape(call_1562.astype('bool'), relay.shape_of(call_1564))) # shape=(12, 16, 2)
bop_1575 = relay.equal(call_1565.astype('bool'), relay.reshape(call_1563.astype('bool'), relay.shape_of(call_1565))) # shape=(12, 16, 2)
func_642_call = mod.get_global_var('func_642')
func_643_call = mutated_mod.get_global_var('func_643')
call_1579 = relay.TupleGetItem(func_642_call(), 5)
call_1580 = relay.TupleGetItem(func_643_call(), 5)
bop_1588 = relay.mod(call_1564.astype('float32'), relay.reshape(bop_1572.astype('float32'), relay.shape_of(call_1564))) # shape=(12, 16, 2)
bop_1591 = relay.mod(call_1565.astype('float32'), relay.reshape(bop_1575.astype('float32'), relay.shape_of(call_1565))) # shape=(12, 16, 2)
output = relay.Tuple([call_1579,bop_1588,])
output2 = relay.Tuple([call_1580,bop_1591,])
func_1592 = relay.Function([], output)
mod['func_1592'] = func_1592
mod = relay.transform.InferType()(mod)
output = func_1592()
func_1593 = relay.Function([], output)
mutated_mod['func_1593'] = func_1593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1357_call = mod.get_global_var('func_1357')
func_1359_call = mutated_mod.get_global_var('func_1359')
call_1599 = relay.TupleGetItem(func_1357_call(), 0)
call_1600 = relay.TupleGetItem(func_1359_call(), 0)
func_367_call = mod.get_global_var('func_367')
func_368_call = mutated_mod.get_global_var('func_368')
call_1601 = func_367_call()
call_1602 = func_367_call()
func_523_call = mod.get_global_var('func_523')
func_524_call = mutated_mod.get_global_var('func_524')
call_1619 = relay.TupleGetItem(func_523_call(), 0)
call_1620 = relay.TupleGetItem(func_524_call(), 0)
output = relay.Tuple([call_1599,call_1601,call_1619,])
output2 = relay.Tuple([call_1600,call_1602,call_1620,])
func_1637 = relay.Function([], output)
mod['func_1637'] = func_1637
mod = relay.transform.InferType()(mod)
mutated_mod['func_1637'] = func_1637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1637_call = mutated_mod.get_global_var('func_1637')
call_1638 = func_1637_call()
output = call_1638
func_1639 = relay.Function([], output)
mutated_mod['func_1639'] = func_1639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1084_call = mod.get_global_var('func_1084')
func_1086_call = mutated_mod.get_global_var('func_1086')
call_1648 = relay.TupleGetItem(func_1084_call(), 0)
call_1649 = relay.TupleGetItem(func_1086_call(), 0)
uop_1652 = relay.acos(call_1648.astype('float32')) # shape=(12, 16, 2)
uop_1654 = relay.acos(call_1649.astype('float32')) # shape=(12, 16, 2)
uop_1665 = relay.log10(uop_1652.astype('float64')) # shape=(12, 16, 2)
uop_1667 = relay.log10(uop_1654.astype('float64')) # shape=(12, 16, 2)
output = uop_1665
output2 = uop_1667
func_1678 = relay.Function([], output)
mod['func_1678'] = func_1678
mod = relay.transform.InferType()(mod)
output = func_1678()
func_1679 = relay.Function([], output)
mutated_mod['func_1679'] = func_1679
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1737 = relay.const([[[-8,4,-1,-8,2,-9,-6,2,7,-5,-10,-7],[3,9,8,-4,6,8,10,4,-3,8,6,-5],[4,5,10,-2,4,9,-5,-10,8,8,3,-2],[5,-6,-2,5,1,-9,-2,4,-6,-9,5,-10]],[[7,-2,2,-7,-6,9,3,3,5,-5,-4,-4],[3,9,-5,2,1,-2,-2,1,3,-3,5,2],[-7,-7,-5,1,-4,-7,-3,1,-7,-10,-6,-4],[-2,-7,4,-5,4,3,-2,-9,-9,5,7,10]],[[1,-2,1,-5,-4,10,-10,10,6,5,-10,-4],[1,2,7,2,10,-6,10,3,-4,4,7,-9],[-7,-3,-9,5,8,7,-7,-5,5,-9,-5,-10],[5,-4,-8,-7,9,2,-7,-9,-2,2,7,8]],[[9,8,-10,-4,4,7,-2,9,-2,-1,-5,6],[9,9,-5,10,4,7,-8,-7,8,-6,-8,-4],[-3,-3,-7,8,-7,10,3,6,-7,1,4,8],[4,4,9,6,5,2,8,-6,6,7,-7,9]],[[7,-9,-2,5,-3,9,9,3,7,-3,-5,2],[-6,-3,1,9,5,-9,7,2,4,-9,9,4],[7,-10,10,-4,-10,-9,2,-9,6,-2,3,-2],[-5,10,2,9,3,4,1,10,-6,4,-9,-6]]], dtype = "int8")#candidate|1737|(5, 4, 12)|const|int8
var_1738 = relay.var("var_1738", dtype = "int8", shape = (5, 4, 12))#candidate|1738|(5, 4, 12)|var|int8
bop_1739 = relay.left_shift(const_1737.astype('int8'), relay.reshape(var_1738.astype('int8'), relay.shape_of(const_1737))) # shape=(5, 4, 12)
output = relay.Tuple([bop_1739,])
output2 = relay.Tuple([bop_1739,])
func_1758 = relay.Function([var_1738,], output)
mod['func_1758'] = func_1758
mod = relay.transform.InferType()(mod)
mutated_mod['func_1758'] = func_1758
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1759 = relay.var("var_1759", dtype = "int8", shape = (5, 4, 12))#candidate|1759|(5, 4, 12)|var|int8
func_1758_call = mutated_mod.get_global_var('func_1758')
call_1760 = func_1758_call(var_1759)
output = call_1760
func_1761 = relay.Function([var_1759], output)
mutated_mod['func_1761'] = func_1761
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1837 = relay.const([[[-3.827268,-6.225466,4.749177,-2.924940,-4.838256,0.101014,4.277315,-9.747955,6.313386,-3.670998,-4.359075],[-7.149304,8.115378,0.155354,9.805948,6.263445,-9.696596,-0.203262,-7.686850,-9.497548,1.467643,-9.551326],[3.648005,-1.299972,9.120302,-5.795355,7.787207,8.700108,-4.425807,2.661134,3.406841,3.348523,9.383978],[2.762588,-4.493245,-1.715404,8.529743,-8.858855,8.591132,1.899738,-6.867674,-9.620752,-3.911981,-1.719200],[-4.690027,-4.552621,-1.120155,-4.153015,3.217535,7.659796,7.540113,3.096222,4.547588,-7.567651,-3.157184],[3.834956,9.733221,-8.688346,3.375375,-6.052443,-4.204191,7.802066,2.498962,-3.454944,4.586969,-5.304227],[9.811339,6.962201,-3.161760,4.724452,3.560093,4.891317,-7.832867,-2.271138,-8.820522,-1.929401,8.230908],[5.281134,3.511342,8.080005,4.296343,6.529137,9.248534,8.558867,-4.989940,-9.583789,-9.096381,-6.977833],[1.874403,-5.682116,-4.403574,8.253080,4.392557,-6.723416,-7.078476,9.089447,8.269774,9.541003,-5.995700],[-1.858864,6.786321,-9.163844,-9.678026,9.144117,-1.978382,4.793514,-5.410875,-0.938368,7.884323,-8.836469],[4.308727,-8.304516,-4.207646,9.628584,-2.980788,-4.478102,8.829330,5.800703,4.850862,7.282220,8.298272],[-5.679216,2.073293,3.824298,6.263040,8.540612,3.722853,-6.489381,0.674177,-0.039045,3.416976,4.587676],[-2.414194,2.021182,6.383614,7.366278,6.614746,-7.685121,-8.054520,-4.143247,1.191534,-4.734280,1.352758],[1.800959,3.060452,-1.528580,-5.514218,4.221812,2.409964,-4.941548,4.614380,5.138116,-4.173066,-6.344856],[5.153610,-4.720411,-9.379373,2.852822,5.425733,-4.249128,0.979184,-2.752972,-3.272545,-7.281189,-6.329971]],[[5.294987,-1.506813,-9.329528,-4.492012,6.788580,2.487998,6.532490,5.664310,0.397317,0.317673,7.584403],[6.400877,-5.182178,5.303281,1.848050,2.161169,3.129953,0.524417,-3.724631,-7.015852,7.339348,-6.841130],[9.697979,9.074077,-5.733433,-1.523292,9.269353,3.629733,-3.611234,-6.038932,-1.185079,-6.083039,1.932166],[-0.955928,0.123073,-5.154143,-6.989136,1.429040,-4.119966,6.592857,1.823195,-2.585340,2.177971,-0.295142],[-2.423008,5.404618,8.194588,-0.719190,3.425501,-0.166194,-8.861085,8.754466,6.364113,-3.396925,9.863395],[5.673288,-7.951051,-3.284557,9.193625,4.442758,2.269518,1.820326,-7.836288,-0.431054,-3.758179,-1.180956],[0.580760,1.787657,0.615914,-9.564236,2.643620,5.256304,4.973000,4.707419,1.023710,-6.230704,0.300494],[3.205464,0.476487,5.159490,-8.755277,-0.216547,9.122867,7.836180,-0.519265,-1.551249,1.046001,6.072313],[4.586955,5.555692,6.293411,2.596183,0.278118,-0.444043,-5.484823,-8.162833,5.601435,-9.355756,1.955193],[2.514376,1.074393,2.781893,-2.110629,5.957670,-3.601508,-6.276561,-3.906842,-1.095846,-2.282183,8.352520],[8.784408,9.185457,-6.616564,3.889582,0.938711,0.705975,-6.690551,4.423709,6.853245,-2.564487,-4.066300],[7.818512,8.595957,-2.666936,-2.942838,-7.015329,-2.045731,9.141818,-6.150216,-6.139458,2.963255,-6.379202],[-9.711310,-4.666388,5.434306,6.987811,0.594526,-4.821541,3.321337,-2.863249,-9.588448,1.939016,5.108357],[-8.058336,5.011692,1.914783,-0.719994,7.233659,-8.456481,3.557179,-0.747840,4.170935,0.050925,-1.015156],[-3.254901,2.843885,-8.241077,2.650737,0.911013,7.038005,-3.818430,4.987154,-4.274181,-5.560164,7.353221]],[[-2.576832,-3.288372,9.895787,-4.908647,-0.699777,3.170008,3.068590,-7.944181,5.069446,-9.666156,8.046831],[1.449035,-5.257300,0.673704,-7.437129,-6.807488,-3.441026,-5.458627,-8.416792,-0.790013,-8.112568,-4.357445],[9.804658,-3.928839,-6.068431,8.679057,-3.287915,8.523896,-4.717252,1.440661,7.709753,-3.351065,-5.080642],[1.171524,5.190921,-5.375193,1.405766,7.175519,4.333376,4.608847,6.512830,3.951179,-9.693224,-1.570382],[4.045418,2.447766,3.923691,3.674001,0.741060,-2.262475,-0.830938,-9.196180,-7.140841,-6.482804,2.265045],[2.649934,-9.396582,-1.244073,3.546916,2.051483,-7.690249,3.271723,-1.901874,-4.107527,-7.331683,-9.028566],[8.015844,-7.868729,8.798158,3.181524,6.548534,8.822254,-4.780028,-0.324136,-7.058780,-3.792586,-7.461725],[-2.101745,-0.021605,-7.236715,3.612202,0.279608,9.658227,-9.642628,-1.139843,-8.043260,5.622430,8.011045],[7.025755,8.732884,-6.522182,2.188185,-2.919507,5.135230,-9.886481,7.253276,6.932030,-0.114349,-3.700967],[5.503535,-7.612324,-5.914099,9.902491,8.392454,9.140311,-9.083375,4.721454,2.679693,9.908782,-2.418595],[-5.698886,0.795206,6.170091,5.456877,0.301690,-9.214930,-3.109292,2.837491,5.418767,-7.198777,5.708653],[-9.151641,-3.938069,-1.766677,-1.869196,9.364956,-1.291788,-1.325134,-0.591288,-3.327899,-3.073976,-5.713709],[9.495768,-0.591696,-9.658761,-6.536732,0.884224,-2.633262,-7.848030,4.459062,-2.613079,5.497982,-5.848336],[-1.663415,7.029799,-9.155207,3.033706,-8.148195,-3.369935,7.226856,-2.370020,-5.685867,-4.594651,2.749307],[-4.838772,-8.269953,-1.060255,5.832750,1.431475,7.985627,-3.159250,5.107215,-9.928963,1.402523,-7.697875]],[[-5.454080,-5.191521,9.471588,2.118490,4.544655,7.463196,-3.013133,5.127313,-2.931620,7.787380,-2.467561],[7.472673,-9.209098,1.532267,-2.840583,-7.438214,-0.843616,-0.106285,-0.598807,1.690287,9.862946,3.760409],[-9.242037,0.662919,7.113821,-5.465681,2.687163,2.659747,-2.918537,7.237445,4.150856,4.960293,-3.309717],[5.722835,5.361148,-7.367686,6.321936,8.514052,-4.605948,2.657047,0.832203,5.112005,3.996729,-6.482245],[-5.038741,2.919054,-6.575916,2.736240,-8.606046,5.667053,7.225425,-7.927611,8.992377,-8.413068,-7.273376],[4.132810,-8.410803,-3.368643,-0.543155,7.623531,-7.092971,-2.725146,4.354661,7.517072,-7.026530,9.231173],[-0.386099,-9.704744,0.660655,-6.849260,-3.349057,-9.050330,-8.973429,4.930393,0.417629,1.824466,7.408917],[-3.786579,-5.096465,-8.020968,-5.716597,-3.281752,2.242816,-2.849363,-7.751469,-5.350802,2.266696,5.742331],[-5.186623,-9.311258,7.942912,0.153206,0.197438,1.643186,-6.018016,-4.826857,8.224225,1.201245,2.754546],[-5.247655,-6.774879,4.036318,2.229888,-5.946896,8.016762,8.584582,-7.941236,2.742249,8.684611,5.956025],[-5.402743,-3.655840,8.165387,-1.821076,-4.501308,-9.292273,8.088828,-7.850355,-3.130322,-4.743229,3.463550],[-1.949943,7.673322,6.522233,-0.527824,-6.401620,-7.818218,-7.307858,-2.587926,-1.597607,8.911835,-2.998181],[-6.399787,7.994834,2.265664,-6.330574,-4.838764,-9.613424,-9.189166,-1.957643,6.312566,9.822833,2.111060],[9.244466,-2.307877,-0.617301,-4.815334,0.642762,1.437284,9.470111,-8.460336,3.644982,-7.412363,-7.231457],[6.735928,6.562292,2.484124,-3.855789,-4.749458,0.919326,-1.508579,6.392096,-5.035181,1.976276,5.738226]],[[-0.666379,8.280560,-2.481979,6.482870,-4.659386,4.511583,0.743410,4.640731,-8.891491,2.522432,-6.272789],[1.542518,-2.501098,-2.023641,-8.939308,-6.675939,-5.065032,-4.323606,0.821507,3.399543,6.903731,3.579988],[-3.007719,-1.435697,8.103409,-8.426353,7.767530,4.660980,0.621341,-2.857266,7.679070,-8.812404,-3.287344],[9.754752,-1.339171,8.133688,1.859726,3.817601,5.047881,-7.123140,7.734265,9.023698,5.847801,3.083626],[-7.624840,-2.800779,-1.352817,4.880621,6.226665,8.782903,-4.241914,6.922972,6.007445,2.521878,0.733256],[1.600439,-0.192536,2.433765,3.076569,-5.856394,-2.416498,-7.654957,5.023983,7.319663,-1.600597,-2.495421],[-7.896626,-9.251482,-2.747892,-9.765603,-7.684451,6.651494,-1.161532,-9.975534,9.123119,-3.843238,3.725129],[-8.909323,-8.408932,2.628506,-3.692724,5.563554,-3.921647,8.975773,8.143159,-2.803764,9.348600,-5.707434],[-0.404505,-3.303732,0.957503,-8.040562,5.523030,2.827308,-3.502123,-8.977983,3.626711,3.156980,8.113285],[-3.355084,6.018404,-2.803239,-7.922652,-1.258913,9.442690,-9.613656,9.671612,8.296667,-3.705836,1.725310],[-9.041479,4.441735,7.898757,0.483158,3.128376,-4.661123,-7.019178,-8.030086,2.249237,3.007716,9.812745],[-9.568568,-5.686952,1.582044,-9.005481,-0.822214,-3.420056,-1.814850,-3.004479,-7.720205,-6.174444,-5.557649],[-6.410261,4.305221,-9.779695,-9.282682,9.006984,-4.592444,9.329122,-2.343836,-7.167824,-9.447835,-0.681264],[2.224276,-3.611324,5.017830,-4.986302,0.861942,-1.215189,-2.892113,0.700351,-0.920416,2.673068,4.855319],[-9.454096,5.525137,-0.817018,6.283319,-5.973161,1.292619,-1.624445,9.685647,0.079366,3.979915,-3.515714]],[[-6.853154,9.111153,-3.418764,3.780524,7.399689,2.079768,1.798247,-6.160006,-2.057367,4.857201,6.537606],[-8.321808,-3.854171,1.085749,8.671716,5.523041,0.925453,-5.141116,-2.132169,0.871029,4.014136,-2.392227],[-8.572478,9.193342,1.822193,1.986638,9.616171,-4.850232,2.485376,4.793393,0.246796,-1.542324,5.022131],[-5.230178,-6.147749,1.147587,-9.043485,-6.787161,-1.658192,5.859071,-7.650919,-6.621281,5.611944,3.129692],[-4.858636,4.853890,-3.284140,2.186726,3.112707,2.421267,7.009993,0.729028,-9.639012,3.594473,-7.158234],[-2.389016,4.643546,-3.332541,7.247403,0.879399,-8.717835,3.280090,-9.407323,9.214912,-2.368004,5.972604],[4.269200,6.790240,4.830635,2.056671,-1.211411,-4.867946,-2.081650,-7.405436,2.482035,-9.727012,-0.047144],[-7.468187,-6.817055,-3.124895,-7.948271,-8.191500,0.253365,5.171496,-0.746251,-3.394074,-1.550370,-9.289680],[9.115894,5.242421,-1.309877,-9.106642,7.379646,0.155583,-7.015137,7.451280,-1.508783,3.103332,1.665617],[-1.520214,6.530976,-0.673743,5.601777,-7.836474,5.320847,9.923522,0.860181,8.923484,-4.516826,-8.792239],[-0.435142,2.492850,-7.760266,-1.217627,8.629080,2.039316,9.697973,5.892154,1.531275,5.079715,1.334548],[-1.040392,0.746164,4.339886,9.150742,-1.145501,8.293539,-0.584167,-1.014139,-5.931864,5.465328,-0.940196],[0.227142,6.354119,-2.552975,-0.916030,-2.115758,-8.863396,-4.473476,4.710540,-1.948196,0.274321,-1.090621],[2.191799,0.796915,-2.679198,5.710213,9.209790,-6.579817,3.575110,-4.889560,-0.278524,7.900651,-1.592986],[8.776350,8.182266,1.920107,6.775623,-0.069157,5.280128,-1.341191,-5.340360,-3.470857,6.325889,-2.529700]],[[8.168654,-5.436100,7.489928,2.780664,2.250199,-0.649828,-4.676482,0.651050,0.243600,-8.108898,9.501025],[-0.904979,-7.120223,-1.495452,-1.900976,0.708691,3.251438,9.304528,3.976107,-7.147373,0.977035,4.536130],[-2.806319,-4.598812,-3.582935,-6.669134,5.633986,9.797007,-3.033509,3.373715,-0.421032,-4.034116,-2.595566],[9.671910,-9.722168,-3.368346,-0.918915,6.769646,6.292171,-7.501069,-8.224100,7.261331,9.476150,-8.118296],[-6.675612,-1.626422,-6.122939,-2.064394,8.005589,-4.041272,5.715080,2.559125,-2.439292,9.915072,-2.984235],[3.223342,-1.199836,3.539518,6.290085,6.042092,9.899759,-9.716415,1.673489,9.814787,-1.681815,-4.528984],[-2.682341,8.458131,9.890485,-4.696886,-3.744785,-3.000996,5.202092,6.261552,9.822167,-4.849011,-9.253376],[-2.820378,-9.939242,-3.297670,4.461236,-7.252380,4.515772,-5.454983,-5.163467,-5.281328,-6.900011,-2.198998],[-8.885176,-6.796742,-1.409362,2.561697,-7.567714,-7.348134,3.269928,8.492253,-9.439452,-9.592340,-6.191191],[-8.667320,-1.158501,5.271533,9.279625,-2.613085,2.887735,-7.838139,3.166140,1.199796,0.153807,-9.303926],[-8.668706,-2.901590,-1.245509,-8.877955,5.144019,2.442965,-0.628015,1.702320,-3.606547,7.347915,-7.308179],[-1.264910,7.871030,2.446096,2.627333,7.314943,-1.058605,-8.577114,3.644034,0.233869,8.664400,-6.529278],[8.268395,-3.885852,5.178233,-9.202902,1.079405,6.205797,-4.720321,4.293548,3.754180,1.842741,-7.021737],[-0.767585,2.761132,7.173726,-5.635354,-4.071952,8.717396,-8.886658,-9.829955,-1.333803,8.882740,9.532190],[4.544890,0.094928,5.090823,-7.811360,6.883396,2.184620,-5.162279,8.233117,-0.955061,-9.258465,-9.984780]],[[-3.095485,5.243516,-8.055561,7.501681,-8.303941,6.497328,1.267992,8.003228,-6.766298,-9.683917,9.274602],[-6.247096,2.276333,-5.443376,-1.822666,-9.640589,4.059406,-6.787430,-8.393742,0.146367,-6.463638,5.098731],[-8.182601,6.282934,9.101677,-9.219027,-1.105378,5.926367,-1.608562,5.552010,1.577390,8.808824,-4.732424],[-5.481723,8.528291,6.373600,-1.972655,8.002788,5.464066,-5.367508,-4.391602,3.890589,9.288628,8.040727],[-8.656130,6.548914,-3.550599,1.693777,-5.669770,-2.940780,4.043695,3.977155,-9.037595,-6.607572,4.144102],[-5.382161,-5.942351,-1.801311,-8.613759,7.447331,-1.780014,-5.060573,9.950543,6.324492,-3.967845,-4.283869],[-5.634418,0.022414,-9.735279,-7.856527,-4.812839,-6.911025,1.098231,2.192145,-5.558383,-8.065422,5.006362],[9.342350,-3.490976,-1.251556,-4.756212,4.156937,-2.839416,4.715090,-4.455804,-5.964410,-0.055967,7.001435],[2.384993,-5.075843,0.706075,-0.019294,5.376205,-3.957735,1.112989,-0.962101,4.405376,-2.857442,2.327329],[-2.848499,2.327361,-7.416941,8.597462,3.819594,-5.116226,-5.853032,1.077472,-3.332364,4.552684,-4.879632],[1.764921,-5.663389,-7.144232,-4.812763,6.136271,-3.243822,4.360991,-1.771832,-4.275047,5.976806,6.547043],[1.393617,1.052621,-1.618951,-1.500674,5.670289,5.892818,-9.957035,-6.882031,6.406485,0.348680,-9.517120],[2.048778,-7.364504,1.271983,-7.327095,5.354761,7.874617,-7.139927,6.219805,-4.289715,-8.722159,4.204802],[-5.800819,-5.095156,7.584585,7.328158,-5.878858,-8.537015,-7.080592,7.615501,3.862124,-7.312223,4.472185],[-8.755838,8.182025,5.883738,-3.140879,-3.164202,-9.405945,6.489623,9.698443,1.790919,1.706850,-8.887821]]], dtype = "float64")#candidate|1837|(8, 15, 11)|const|float64
uop_1838 = relay.sqrt(const_1837.astype('float64')) # shape=(8, 15, 11)
output = uop_1838
output2 = uop_1838
func_1842 = relay.Function([], output)
mod['func_1842'] = func_1842
mod = relay.transform.InferType()(mod)
output = func_1842()
func_1843 = relay.Function([], output)
mutated_mod['func_1843'] = func_1843
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1075_call = mod.get_global_var('func_1075')
func_1076_call = mutated_mod.get_global_var('func_1076')
call_1855 = relay.TupleGetItem(func_1075_call(), 0)
call_1856 = relay.TupleGetItem(func_1076_call(), 0)
func_523_call = mod.get_global_var('func_523')
func_524_call = mutated_mod.get_global_var('func_524')
call_1857 = relay.TupleGetItem(func_523_call(), 1)
call_1858 = relay.TupleGetItem(func_524_call(), 1)
output = relay.Tuple([call_1855,call_1857,])
output2 = relay.Tuple([call_1856,call_1858,])
func_1862 = relay.Function([], output)
mod['func_1862'] = func_1862
mod = relay.transform.InferType()(mod)
output = func_1862()
func_1863 = relay.Function([], output)
mutated_mod['func_1863'] = func_1863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_834_call = mod.get_global_var('func_834')
func_836_call = mutated_mod.get_global_var('func_836')
call_1930 = relay.TupleGetItem(func_834_call(), 0)
call_1931 = relay.TupleGetItem(func_836_call(), 0)
output = call_1930
output2 = call_1931
func_1938 = relay.Function([], output)
mod['func_1938'] = func_1938
mod = relay.transform.InferType()(mod)
output = func_1938()
func_1939 = relay.Function([], output)
mutated_mod['func_1939'] = func_1939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1862_call = mod.get_global_var('func_1862')
func_1863_call = mutated_mod.get_global_var('func_1863')
call_1940 = relay.TupleGetItem(func_1862_call(), 0)
call_1941 = relay.TupleGetItem(func_1863_call(), 0)
output = call_1940
output2 = call_1941
func_1942 = relay.Function([], output)
mod['func_1942'] = func_1942
mod = relay.transform.InferType()(mod)
mutated_mod['func_1942'] = func_1942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1942_call = mutated_mod.get_global_var('func_1942')
call_1943 = func_1942_call()
output = call_1943
func_1944 = relay.Function([], output)
mutated_mod['func_1944'] = func_1944
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1947 = relay.var("var_1947", dtype = "uint16", shape = (2, 16, 5))#candidate|1947|(2, 16, 5)|var|uint16
var_1948 = relay.var("var_1948", dtype = "uint16", shape = (2, 16, 5))#candidate|1948|(2, 16, 5)|var|uint16
bop_1949 = relay.bitwise_and(var_1947.astype('uint16'), relay.reshape(var_1948.astype('uint16'), relay.shape_of(var_1947))) # shape=(2, 16, 5)
output = relay.Tuple([bop_1949,])
output2 = relay.Tuple([bop_1949,])
func_1959 = relay.Function([var_1947,var_1948,], output)
mod['func_1959'] = func_1959
mod = relay.transform.InferType()(mod)
var_1960 = relay.var("var_1960", dtype = "uint16", shape = (2, 16, 5))#candidate|1960|(2, 16, 5)|var|uint16
var_1961 = relay.var("var_1961", dtype = "uint16", shape = (2, 16, 5))#candidate|1961|(2, 16, 5)|var|uint16
output = func_1959(var_1960,var_1961,)
func_1962 = relay.Function([var_1960,var_1961,], output)
mutated_mod['func_1962'] = func_1962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_918_call = mod.get_global_var('func_918')
func_919_call = mutated_mod.get_global_var('func_919')
call_1964 = relay.TupleGetItem(func_918_call(), 0)
call_1965 = relay.TupleGetItem(func_919_call(), 0)
output = call_1964
output2 = call_1965
func_1972 = relay.Function([], output)
mod['func_1972'] = func_1972
mod = relay.transform.InferType()(mod)
mutated_mod['func_1972'] = func_1972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1972_call = mutated_mod.get_global_var('func_1972')
call_1973 = func_1972_call()
output = call_1973
func_1974 = relay.Function([], output)
mutated_mod['func_1974'] = func_1974
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1357_call = mod.get_global_var('func_1357')
func_1359_call = mutated_mod.get_global_var('func_1359')
call_1986 = relay.TupleGetItem(func_1357_call(), 0)
call_1987 = relay.TupleGetItem(func_1359_call(), 0)
func_1959_call = mod.get_global_var('func_1959')
func_1962_call = mutated_mod.get_global_var('func_1962')
const_2012 = relay.const([[7,-10,2,-6,-10,5,-10,-10,-7,-1,3,7,6,-7,-10,-1,-10,7,-2,-4,-3,10,-7,-8,-1,7,10,4,-4,5,1,2,-5,-7,2,-9,10,10,10,-10,-8,5,-4,2,-3,1,-10,-7,-2,4,-6,10,-2,5,-10,-5,5,4,2,-5,-4,-8,1,-3,-2,6,-2,7,-9,-10,-9,-5,6,4,-9,2,7,-10,-7,-9,2,8,4,-9,-10,-1,-3,-3,-8,-4,6,-2,8,-1,-7,-4,8,4,-1,-6,-2,-10,-3,-2,10,2,4,10,8,-6,2,3,-6,-3,-9,-6,5,-6,10,1,-5,-7,7,-2,-9,-9,10,10,-10,-3,-9,2,6,2,7,8,-8,-5,-4,-1,7,3,-3,-5,5,4,8,10,5,2,7,5,8,-10,9,7,-1,-5,-5,-9]], dtype = "uint16")#candidate|2012|(1, 160)|const|uint16
call_2011 = relay.TupleGetItem(func_1959_call(relay.reshape(const_2012.astype('uint16'), [2, 16, 5]), relay.reshape(const_2012.astype('uint16'), [2, 16, 5]), ), 0)
call_2013 = relay.TupleGetItem(func_1962_call(relay.reshape(const_2012.astype('uint16'), [2, 16, 5]), relay.reshape(const_2012.astype('uint16'), [2, 16, 5]), ), 0)
uop_2018 = relay.atan(const_2012.astype('float32')) # shape=(1, 160)
bop_2025 = relay.left_shift(uop_2018.astype('int16'), relay.reshape(call_2011.astype('int16'), relay.shape_of(uop_2018))) # shape=(1, 160)
bop_2028 = relay.left_shift(uop_2018.astype('int16'), relay.reshape(call_2013.astype('int16'), relay.shape_of(uop_2018))) # shape=(1, 160)
output = relay.Tuple([call_1986,bop_2025,])
output2 = relay.Tuple([call_1987,bop_2028,])
func_2036 = relay.Function([], output)
mod['func_2036'] = func_2036
mod = relay.transform.InferType()(mod)
output = func_2036()
func_2037 = relay.Function([], output)
mutated_mod['func_2037'] = func_2037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1842_call = mod.get_global_var('func_1842')
func_1843_call = mutated_mod.get_global_var('func_1843')
call_2053 = func_1842_call()
call_2054 = func_1842_call()
output = relay.Tuple([call_2053,])
output2 = relay.Tuple([call_2054,])
func_2064 = relay.Function([], output)
mod['func_2064'] = func_2064
mod = relay.transform.InferType()(mod)
mutated_mod['func_2064'] = func_2064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2064_call = mutated_mod.get_global_var('func_2064')
call_2065 = func_2064_call()
output = call_2065
func_2066 = relay.Function([], output)
mutated_mod['func_2066'] = func_2066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1938_call = mod.get_global_var('func_1938')
func_1939_call = mutated_mod.get_global_var('func_1939')
call_2079 = func_1938_call()
call_2080 = func_1938_call()
func_433_call = mod.get_global_var('func_433')
func_434_call = mutated_mod.get_global_var('func_434')
call_2091 = func_433_call()
call_2092 = func_433_call()
output = relay.Tuple([call_2079,call_2091,])
output2 = relay.Tuple([call_2080,call_2092,])
func_2097 = relay.Function([], output)
mod['func_2097'] = func_2097
mod = relay.transform.InferType()(mod)
output = func_2097()
func_2098 = relay.Function([], output)
mutated_mod['func_2098'] = func_2098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1185_call = mod.get_global_var('func_1185')
func_1187_call = mutated_mod.get_global_var('func_1187')
call_2131 = func_1185_call()
call_2132 = func_1185_call()
uop_2133 = relay.log(call_2131.astype('float32')) # shape=(12, 16, 2)
uop_2135 = relay.log(call_2132.astype('float32')) # shape=(12, 16, 2)
output = relay.Tuple([uop_2133,])
output2 = relay.Tuple([uop_2135,])
func_2137 = relay.Function([], output)
mod['func_2137'] = func_2137
mod = relay.transform.InferType()(mod)
mutated_mod['func_2137'] = func_2137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2137_call = mutated_mod.get_global_var('func_2137')
call_2138 = func_2137_call()
output = call_2138
func_2139 = relay.Function([], output)
mutated_mod['func_2139'] = func_2139
mutated_mod = relay.transform.InferType()(mutated_mod)
func_367_call = mod.get_global_var('func_367')
func_368_call = mutated_mod.get_global_var('func_368')
call_2188 = func_367_call()
call_2189 = func_367_call()
func_225_call = mod.get_global_var('func_225')
func_226_call = mutated_mod.get_global_var('func_226')
call_2192 = relay.TupleGetItem(func_225_call(), 1)
call_2193 = relay.TupleGetItem(func_226_call(), 1)
func_1972_call = mod.get_global_var('func_1972')
func_1974_call = mutated_mod.get_global_var('func_1974')
call_2196 = func_1972_call()
call_2197 = func_1972_call()
output = relay.Tuple([call_2188,call_2192,call_2196,])
output2 = relay.Tuple([call_2189,call_2193,call_2197,])
func_2211 = relay.Function([], output)
mod['func_2211'] = func_2211
mod = relay.transform.InferType()(mod)
mutated_mod['func_2211'] = func_2211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2211_call = mutated_mod.get_global_var('func_2211')
call_2212 = func_2211_call()
output = call_2212
func_2213 = relay.Function([], output)
mutated_mod['func_2213'] = func_2213
mutated_mod = relay.transform.InferType()(mutated_mod)
func_367_call = mod.get_global_var('func_367')
func_368_call = mutated_mod.get_global_var('func_368')
call_2227 = func_367_call()
call_2228 = func_367_call()
func_1758_call = mod.get_global_var('func_1758')
func_1761_call = mutated_mod.get_global_var('func_1761')
var_2234 = relay.var("var_2234", dtype = "int8", shape = (240,))#candidate|2234|(240,)|var|int8
call_2233 = relay.TupleGetItem(func_1758_call(relay.reshape(var_2234.astype('int8'), [5, 4, 12])), 0)
call_2235 = relay.TupleGetItem(func_1761_call(relay.reshape(var_2234.astype('int8'), [5, 4, 12])), 0)
output = relay.Tuple([call_2227,call_2233,var_2234,])
output2 = relay.Tuple([call_2228,call_2235,var_2234,])
func_2250 = relay.Function([var_2234,], output)
mod['func_2250'] = func_2250
mod = relay.transform.InferType()(mod)
mutated_mod['func_2250'] = func_2250
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2251 = relay.var("var_2251", dtype = "int8", shape = (240,))#candidate|2251|(240,)|var|int8
func_2250_call = mutated_mod.get_global_var('func_2250')
call_2252 = func_2250_call(var_2251)
output = call_2252
func_2253 = relay.Function([var_2251], output)
mutated_mod['func_2253'] = func_2253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1592_call = mod.get_global_var('func_1592')
func_1593_call = mutated_mod.get_global_var('func_1593')
call_2265 = relay.TupleGetItem(func_1592_call(), 0)
call_2266 = relay.TupleGetItem(func_1593_call(), 0)
func_426_call = mod.get_global_var('func_426')
func_428_call = mutated_mod.get_global_var('func_428')
call_2285 = func_426_call()
call_2286 = func_426_call()
func_304_call = mod.get_global_var('func_304')
func_306_call = mutated_mod.get_global_var('func_306')
call_2287 = func_304_call()
call_2288 = func_304_call()
output = relay.Tuple([call_2265,call_2285,call_2287,])
output2 = relay.Tuple([call_2266,call_2286,call_2288,])
func_2298 = relay.Function([], output)
mod['func_2298'] = func_2298
mod = relay.transform.InferType()(mod)
mutated_mod['func_2298'] = func_2298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2298_call = mutated_mod.get_global_var('func_2298')
call_2299 = func_2298_call()
output = call_2299
func_2300 = relay.Function([], output)
mutated_mod['func_2300'] = func_2300
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2314 = relay.const([[[6,4,-6,8,8,6,5,-7,-9,-2,9,-5,2,-7],[-9,-4,-9,-4,5,8,-3,9,2,-5,-4,5,-4,10],[4,-5,-6,-9,-9,-2,5,10,-4,10,-6,-4,3,-8],[10,5,3,8,-10,6,1,6,8,6,4,8,2,-2],[3,-3,8,-8,7,2,-4,9,-6,3,-10,6,6,5],[5,-2,9,-3,3,-10,9,10,-2,-1,3,-4,3,-6],[-3,-9,-2,1,8,10,5,-4,4,8,-2,-4,-2,-7],[-8,6,-7,4,-5,3,-8,5,-5,-6,6,4,-2,4],[-9,-9,-5,2,1,1,10,-9,7,2,6,2,3,-9]],[[-6,-8,-3,4,5,10,-4,2,-5,2,7,-5,-1,5],[2,-8,-7,7,-7,-10,9,-6,10,-6,-1,10,-2,10],[-1,7,1,6,-4,-7,-6,-3,6,-7,-9,3,9,7],[8,5,4,-5,-7,-2,3,-4,-6,-1,10,9,1,9],[-5,3,6,3,10,-5,-6,-10,4,-8,-2,-3,7,2],[-5,-9,-9,-4,-10,5,4,9,-4,-10,4,1,7,10],[7,1,5,2,2,-1,4,2,-5,-9,9,-1,7,1],[-5,7,5,4,10,5,2,6,-1,4,-9,-7,2,1],[10,-3,-5,9,-2,9,10,6,2,-8,10,9,6,-8]],[[-3,-10,-3,8,-7,7,9,-1,-1,-1,-9,-4,-4,10],[10,-10,7,4,7,5,8,-3,-7,5,3,1,-6,3],[-9,-10,9,1,-2,-5,8,2,1,2,2,-7,5,7],[2,-1,-4,-1,-3,-10,-9,5,-4,-3,2,2,5,9],[7,3,-7,-4,9,6,10,-8,-9,-6,8,10,7,6],[-3,-3,-10,-2,3,9,-1,-4,9,10,5,-4,5,4],[6,-5,-4,9,-7,2,5,3,-6,-7,-1,6,-10,8],[2,9,-4,7,5,4,7,1,9,7,1,2,-8,-7],[-9,-8,-10,9,3,2,1,9,3,-9,-6,-8,2,-10]],[[-10,-1,-3,-10,-7,-9,-6,-10,8,-7,1,-3,-4,-3],[-3,-7,1,2,10,-9,2,9,8,6,-1,6,1,-1],[8,-1,7,4,9,-2,-9,-6,-8,8,6,-1,-9,1],[4,-6,7,5,-7,-4,6,-3,-8,5,-4,1,9,9],[10,-9,-3,9,2,4,7,-4,-3,-8,-8,6,-8,-3],[2,6,-3,6,-9,8,3,1,-9,2,3,-4,7,-4],[10,3,-1,-3,3,2,6,-3,1,10,-8,5,-6,-4],[-2,7,8,-3,-6,-5,8,3,9,-7,-10,4,1,1],[2,-8,6,8,5,6,10,2,-1,3,1,-2,-5,8]],[[8,3,7,-4,-9,8,4,5,5,3,2,-8,4,-3],[8,6,3,6,3,2,2,5,-3,-1,10,6,8,7],[4,4,3,6,1,5,-1,5,-6,1,-3,-10,6,6],[-8,9,-5,3,-3,4,-10,8,-4,9,3,1,-4,-8],[-5,-8,7,6,-10,-10,8,9,-10,1,1,-6,-2,2],[-8,-10,-7,7,-8,8,9,-5,1,-7,2,-7,-10,9],[9,-1,6,-1,10,8,10,7,3,8,-5,-5,3,-2],[-6,-6,-4,4,-8,2,-3,-7,-6,4,-8,3,7,10],[1,-4,5,-2,9,-7,-10,-7,9,8,10,-5,6,2]],[[8,-5,6,-4,3,9,3,-9,7,10,9,3,1,10],[8,3,5,-2,1,-3,-5,6,-8,-3,-10,3,10,-1],[-4,10,-2,-5,-1,10,-7,6,-3,10,-5,8,-5,-7],[7,-5,8,2,-8,-6,5,1,-7,2,9,-3,4,-2],[-2,-1,8,9,-3,5,-7,-2,-9,4,2,-7,-7,-7],[-2,7,1,-3,8,-2,-3,4,-10,-2,-1,-4,-2,6],[-3,-10,6,-1,7,-4,5,8,3,-8,8,1,-4,-4],[7,-6,3,-5,3,-3,-1,-5,-5,4,5,-2,-10,6],[-9,10,10,-6,2,-1,-7,-3,-3,5,-3,7,-3,-5]],[[-1,8,-9,4,6,2,1,-1,10,-9,4,3,4,-7],[9,1,3,8,8,1,3,-10,-9,-5,6,-5,9,-2],[-10,-2,-1,6,10,7,-7,-4,4,-5,6,3,3,6],[8,4,7,4,9,-3,8,-9,-8,5,6,4,-1,5],[5,-5,9,8,7,3,5,-7,4,6,-8,4,5,7],[3,10,-5,-10,6,10,1,1,9,-7,-3,-7,-7,6],[-8,-6,9,10,2,-10,-7,4,-4,-2,-3,6,-3,9],[-3,-10,2,-4,3,-6,-4,-3,-5,-7,-2,-1,-7,2],[-9,9,-8,5,-4,-10,2,2,-2,-5,2,7,-2,-8]]], dtype = "uint16")#candidate|2314|(7, 9, 14)|const|uint16
var_2315 = relay.var("var_2315", dtype = "uint16", shape = (7, 9, 14))#candidate|2315|(7, 9, 14)|var|uint16
bop_2316 = relay.equal(const_2314.astype('bool'), relay.reshape(var_2315.astype('bool'), relay.shape_of(const_2314))) # shape=(7, 9, 14)
output = relay.Tuple([bop_2316,])
output2 = relay.Tuple([bop_2316,])
func_2324 = relay.Function([var_2315,], output)
mod['func_2324'] = func_2324
mod = relay.transform.InferType()(mod)
mutated_mod['func_2324'] = func_2324
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2325 = relay.var("var_2325", dtype = "uint16", shape = (7, 9, 14))#candidate|2325|(7, 9, 14)|var|uint16
func_2324_call = mutated_mod.get_global_var('func_2324')
call_2326 = func_2324_call(var_2325)
output = call_2326
func_2327 = relay.Function([var_2325], output)
mutated_mod['func_2327'] = func_2327
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2366 = relay.var("var_2366", dtype = "float64", shape = (8, 14, 10))#candidate|2366|(8, 14, 10)|var|float64
uop_2367 = relay.log10(var_2366.astype('float64')) # shape=(8, 14, 10)
bop_2369 = relay.floor_mod(uop_2367.astype('float32'), relay.reshape(var_2366.astype('float32'), relay.shape_of(uop_2367))) # shape=(8, 14, 10)
uop_2374 = relay.cos(var_2366.astype('float64')) # shape=(8, 14, 10)
output = relay.Tuple([bop_2369,uop_2374,])
output2 = relay.Tuple([bop_2369,uop_2374,])
func_2386 = relay.Function([var_2366,], output)
mod['func_2386'] = func_2386
mod = relay.transform.InferType()(mod)
var_2387 = relay.var("var_2387", dtype = "float64", shape = (8, 14, 10))#candidate|2387|(8, 14, 10)|var|float64
output = func_2386(var_2387)
func_2388 = relay.Function([var_2387], output)
mutated_mod['func_2388'] = func_2388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_834_call = mod.get_global_var('func_834')
func_836_call = mutated_mod.get_global_var('func_836')
call_2409 = relay.TupleGetItem(func_834_call(), 0)
call_2410 = relay.TupleGetItem(func_836_call(), 0)
output = relay.Tuple([call_2409,])
output2 = relay.Tuple([call_2410,])
func_2414 = relay.Function([], output)
mod['func_2414'] = func_2414
mod = relay.transform.InferType()(mod)
mutated_mod['func_2414'] = func_2414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2414_call = mutated_mod.get_global_var('func_2414')
call_2415 = func_2414_call()
output = call_2415
func_2416 = relay.Function([], output)
mutated_mod['func_2416'] = func_2416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1357_call = mod.get_global_var('func_1357')
func_1359_call = mutated_mod.get_global_var('func_1359')
call_2484 = relay.TupleGetItem(func_1357_call(), 0)
call_2485 = relay.TupleGetItem(func_1359_call(), 0)
output = relay.Tuple([call_2484,])
output2 = relay.Tuple([call_2485,])
func_2499 = relay.Function([], output)
mod['func_2499'] = func_2499
mod = relay.transform.InferType()(mod)
mutated_mod['func_2499'] = func_2499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2499_call = mutated_mod.get_global_var('func_2499')
call_2500 = func_2499_call()
output = call_2500
func_2501 = relay.Function([], output)
mutated_mod['func_2501'] = func_2501
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2556 = relay.var("var_2556", dtype = "bool", shape = (16, 16, 5))#candidate|2556|(16, 16, 5)|var|bool
var_2557 = relay.var("var_2557", dtype = "bool", shape = (16, 16, 5))#candidate|2557|(16, 16, 5)|var|bool
bop_2558 = relay.logical_or(var_2556.astype('bool'), relay.reshape(var_2557.astype('bool'), relay.shape_of(var_2556))) # shape=(16, 16, 5)
output = relay.Tuple([bop_2558,])
output2 = relay.Tuple([bop_2558,])
func_2562 = relay.Function([var_2556,var_2557,], output)
mod['func_2562'] = func_2562
mod = relay.transform.InferType()(mod)
var_2563 = relay.var("var_2563", dtype = "bool", shape = (16, 16, 5))#candidate|2563|(16, 16, 5)|var|bool
var_2564 = relay.var("var_2564", dtype = "bool", shape = (16, 16, 5))#candidate|2564|(16, 16, 5)|var|bool
output = func_2562(var_2563,var_2564,)
func_2565 = relay.Function([var_2563,var_2564,], output)
mutated_mod['func_2565'] = func_2565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_426_call = mod.get_global_var('func_426')
func_428_call = mutated_mod.get_global_var('func_428')
call_2567 = func_426_call()
call_2568 = func_426_call()
func_1518_call = mod.get_global_var('func_1518')
func_1520_call = mutated_mod.get_global_var('func_1520')
call_2573 = relay.TupleGetItem(func_1518_call(), 0)
call_2574 = relay.TupleGetItem(func_1520_call(), 0)
func_1084_call = mod.get_global_var('func_1084')
func_1086_call = mutated_mod.get_global_var('func_1086')
call_2581 = relay.TupleGetItem(func_1084_call(), 0)
call_2582 = relay.TupleGetItem(func_1086_call(), 0)
func_454_call = mod.get_global_var('func_454')
func_455_call = mutated_mod.get_global_var('func_455')
call_2585 = relay.TupleGetItem(func_454_call(), 1)
call_2586 = relay.TupleGetItem(func_455_call(), 1)
output = relay.Tuple([call_2567,call_2573,call_2581,call_2585,])
output2 = relay.Tuple([call_2568,call_2574,call_2582,call_2586,])
func_2587 = relay.Function([], output)
mod['func_2587'] = func_2587
mod = relay.transform.InferType()(mod)
output = func_2587()
func_2588 = relay.Function([], output)
mutated_mod['func_2588'] = func_2588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_543_call = mod.get_global_var('func_543')
func_544_call = mutated_mod.get_global_var('func_544')
call_2598 = relay.TupleGetItem(func_543_call(), 0)
call_2599 = relay.TupleGetItem(func_544_call(), 0)
output = relay.Tuple([call_2598,])
output2 = relay.Tuple([call_2599,])
func_2609 = relay.Function([], output)
mod['func_2609'] = func_2609
mod = relay.transform.InferType()(mod)
mutated_mod['func_2609'] = func_2609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2609_call = mutated_mod.get_global_var('func_2609')
call_2610 = func_2609_call()
output = call_2610
func_2611 = relay.Function([], output)
mutated_mod['func_2611'] = func_2611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1678_call = mod.get_global_var('func_1678')
func_1679_call = mutated_mod.get_global_var('func_1679')
call_2625 = func_1678_call()
call_2626 = func_1678_call()
output = call_2625
output2 = call_2626
func_2636 = relay.Function([], output)
mod['func_2636'] = func_2636
mod = relay.transform.InferType()(mod)
output = func_2636()
func_2637 = relay.Function([], output)
mutated_mod['func_2637'] = func_2637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_982_call = mod.get_global_var('func_982')
func_984_call = mutated_mod.get_global_var('func_984')
call_2670 = relay.TupleGetItem(func_982_call(), 2)
call_2671 = relay.TupleGetItem(func_984_call(), 2)
var_2682 = relay.var("var_2682", dtype = "bool", shape = (12, 16, 2))#candidate|2682|(12, 16, 2)|var|bool
bop_2683 = relay.logical_xor(call_2670.astype('uint16'), relay.reshape(var_2682.astype('uint16'), relay.shape_of(call_2670))) # shape=(12, 16, 2)
bop_2686 = relay.logical_xor(call_2671.astype('uint16'), relay.reshape(var_2682.astype('uint16'), relay.shape_of(call_2671))) # shape=(12, 16, 2)
func_1133_call = mod.get_global_var('func_1133')
func_1136_call = mutated_mod.get_global_var('func_1136')
call_2696 = relay.TupleGetItem(func_1133_call(relay.reshape(bop_2683.astype('int32'), [12, 16, 2])), 0)
call_2697 = relay.TupleGetItem(func_1136_call(relay.reshape(bop_2683.astype('int32'), [12, 16, 2])), 0)
output = relay.Tuple([bop_2683,call_2696,])
output2 = relay.Tuple([bop_2686,call_2697,])
func_2717 = relay.Function([var_2682,], output)
mod['func_2717'] = func_2717
mod = relay.transform.InferType()(mod)
var_2718 = relay.var("var_2718", dtype = "bool", shape = (12, 16, 2))#candidate|2718|(12, 16, 2)|var|bool
output = func_2717(var_2718)
func_2719 = relay.Function([var_2718], output)
mutated_mod['func_2719'] = func_2719
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2721 = relay.const([[[-8.012050,4.615013],[2.409953,5.624451],[-7.357353,7.937326],[6.732085,1.770512],[-9.159197,5.319118],[4.661773,-0.702127],[-2.885489,2.482030],[-1.110823,-3.542924],[-4.631478,8.464373],[4.968521,-5.654869],[-0.041274,1.973902],[-9.622703,-5.333634],[4.599183,5.783050],[9.559553,-0.322227],[-2.508916,6.265760]],[[-5.527102,1.766194],[8.427925,6.729250],[7.628286,-5.246624],[5.189460,9.139046],[-1.728046,6.208176],[0.181490,9.122084],[-9.471913,-9.895878],[4.001780,7.564559],[-4.319491,9.641397],[9.396218,-2.978723],[-5.771585,-9.653739],[5.385646,-1.689803],[3.455308,8.575473],[-9.088385,-5.314399],[2.046175,3.563277]],[[-8.332738,-8.393006],[7.441424,-3.029426],[-5.426452,0.246576],[1.579504,5.931153],[-1.232786,7.741361],[8.819817,-5.062159],[4.611905,-9.339961],[-8.302775,9.988970],[-4.710511,4.692987],[7.805766,-2.891292],[-4.887559,3.222739],[0.750833,-4.008611],[-1.981193,-4.649926],[5.758574,9.688118],[5.913825,2.697433]],[[-2.159637,-9.061037],[-0.696308,-2.018180],[9.029882,-4.573648],[5.727237,4.560608],[-2.699612,-1.623688],[7.860663,-5.927424],[4.527817,2.307454],[2.173577,-0.408212],[-9.016507,-7.833264],[-7.325570,-8.480349],[4.072740,-5.254854],[-4.127268,0.632290],[7.060305,9.531531],[-0.727183,3.195507],[-7.611579,-2.752440]],[[0.238056,5.768799],[8.355701,1.476052],[-2.460014,5.082796],[-1.029194,-4.540509],[-3.853239,8.351153],[9.479081,-9.246354],[-8.461284,-3.284950],[4.631867,-6.034572],[8.586886,-9.723878],[0.893524,3.575660],[1.001608,4.099442],[-0.066925,7.888459],[9.631934,-4.314365],[1.493635,3.374536],[8.040253,-2.137569]],[[-2.462618,0.453232],[-8.211708,1.183295],[0.221343,-8.026526],[4.206195,-3.570550],[5.802174,-1.879986],[-9.126760,-2.608132],[-7.383764,2.259368],[7.785697,-8.010625],[-4.518766,9.128149],[3.590112,-0.200312],[0.482490,5.083582],[-4.009357,-7.617293],[4.298327,2.781032],[-0.604310,-2.958089],[0.894424,-9.257488]],[[6.719419,-7.486491],[-6.203217,0.474713],[-8.801678,8.591298],[-4.152593,8.154038],[-9.066951,-6.884949],[-9.535914,-4.783417],[3.394238,5.481052],[-0.187958,8.655505],[-0.687358,-6.064892],[-0.601212,-9.364383],[8.899119,-3.963793],[5.990949,2.818778],[-5.786584,9.659409],[9.884743,3.990907],[-3.185097,9.440393]],[[-4.379771,6.693700],[-8.672291,6.146835],[0.764956,-8.434399],[4.456365,-4.955829],[-3.890147,7.569903],[5.768412,9.680624],[-4.823171,-4.847074],[-0.681229,0.322605],[-7.184635,6.901089],[-7.519731,1.144653],[8.962785,7.799681],[2.316863,5.931476],[9.292180,-4.598509],[9.357621,2.839369],[-1.844913,3.252710]],[[9.232737,0.793304],[3.084099,-3.648094],[4.742081,0.790246],[9.682130,-0.889556],[-8.532334,-4.176382],[-9.932421,-7.246386],[8.276706,7.906329],[6.208993,-7.385543],[2.837602,0.806899],[-4.090137,6.236846],[8.952912,-2.105020],[2.643449,5.500864],[-2.280022,3.077287],[-4.679314,2.278451],[1.253637,1.204307]],[[1.985861,0.579885],[3.473806,3.890808],[-2.487807,-1.507033],[4.531332,7.614538],[0.778093,-4.754223],[-7.526188,-9.740414],[9.102726,-5.498853],[-7.764647,-9.288324],[0.562051,-4.355752],[-4.541123,7.577438],[-9.434939,-5.162499],[-6.484642,-0.273498],[9.577759,-8.862101],[-1.441221,-8.006761],[-8.786446,-8.428233]],[[0.974459,-6.184619],[-9.963646,8.120162],[-5.684422,-2.530665],[-9.223555,-7.140069],[-5.176307,-5.959947],[3.436764,4.752881],[0.967663,4.668966],[9.893079,-5.046558],[-1.866203,9.130323],[-2.480924,0.959589],[4.673450,6.546451],[5.658483,2.464198],[7.236860,1.043782],[-0.172031,-9.006206],[-4.955668,5.345096]],[[-9.446873,-7.616301],[-9.595641,3.823322],[2.700876,2.735000],[-2.539355,-0.525886],[-0.327654,3.907815],[-7.310774,-5.484153],[-4.240839,-1.436602],[-5.236171,-5.665905],[-5.733814,-9.119510],[-7.915014,7.724962],[-1.322624,5.672559],[6.366012,-8.235749],[0.991238,6.179420],[-9.335573,-1.667887],[1.809060,-1.201697]]], dtype = "float32")#candidate|2721|(12, 15, 2)|const|float32
var_2722 = relay.var("var_2722", dtype = "float32", shape = (12, 15, 2))#candidate|2722|(12, 15, 2)|var|float32
bop_2723 = relay.mod(const_2721.astype('float32'), relay.reshape(var_2722.astype('float32'), relay.shape_of(const_2721))) # shape=(12, 15, 2)
bop_2729 = relay.equal(const_2721.astype('bool'), relay.reshape(var_2722.astype('bool'), relay.shape_of(const_2721))) # shape=(12, 15, 2)
func_819_call = mod.get_global_var('func_819')
func_821_call = mutated_mod.get_global_var('func_821')
const_2738 = relay.const([[2,1,9,-3,-3,-1],[-1,-6,10,-4,-3,2],[-10,-7,4,9,7,-10],[-10,-9,-3,9,-7,4],[4,4,7,-3,2,7],[-7,-4,8,1,8,10],[-10,5,1,5,-7,3],[7,-3,7,-7,-8,-9],[6,2,-9,7,-1,-7],[4,-8,-10,-7,8,-6],[-3,9,5,-8,9,-6],[4,8,-6,8,6,10],[-6,3,-10,10,3,5],[-9,-8,2,-7,-5,-2],[7,-10,-3,-8,-1,4],[1,5,3,-9,-2,1],[9,10,2,-7,-1,3],[-9,-6,4,-2,-4,-7],[6,9,1,1,7,-5],[5,-9,9,4,-5,-10],[10,1,10,1,4,-3],[-2,-8,-10,-10,-5,3],[3,3,8,6,-5,2],[-7,-1,-4,7,-3,-5],[-7,7,-7,5,-10,7],[-4,-5,-10,-4,9,7],[4,-9,8,-7,2,5],[4,7,-10,1,-7,-3],[-3,-5,6,8,-5,-6],[-3,-6,-7,-2,4,-7],[6,-8,-6,4,-2,6],[1,8,10,-9,-7,8],[9,-8,-1,-7,5,-2],[8,2,4,-6,1,3],[7,4,8,-1,2,-9]], dtype = "uint32")#candidate|2738|(35, 6)|const|uint32
call_2737 = relay.TupleGetItem(func_819_call(relay.reshape(const_2738.astype('uint32'), [2, 7, 15])), 5)
call_2739 = relay.TupleGetItem(func_821_call(relay.reshape(const_2738.astype('uint32'), [2, 7, 15])), 5)
output = relay.Tuple([bop_2723,bop_2729,call_2737,const_2738,])
output2 = relay.Tuple([bop_2723,bop_2729,call_2739,const_2738,])
func_2743 = relay.Function([var_2722,], output)
mod['func_2743'] = func_2743
mod = relay.transform.InferType()(mod)
mutated_mod['func_2743'] = func_2743
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2744 = relay.var("var_2744", dtype = "float32", shape = (12, 15, 2))#candidate|2744|(12, 15, 2)|var|float32
func_2743_call = mutated_mod.get_global_var('func_2743')
call_2745 = func_2743_call(var_2744)
output = call_2745
func_2746 = relay.Function([var_2744], output)
mutated_mod['func_2746'] = func_2746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_523_call = mod.get_global_var('func_523')
func_524_call = mutated_mod.get_global_var('func_524')
call_2793 = relay.TupleGetItem(func_523_call(), 1)
call_2794 = relay.TupleGetItem(func_524_call(), 1)
output = relay.Tuple([call_2793,])
output2 = relay.Tuple([call_2794,])
func_2801 = relay.Function([], output)
mod['func_2801'] = func_2801
mod = relay.transform.InferType()(mod)
output = func_2801()
func_2802 = relay.Function([], output)
mutated_mod['func_2802'] = func_2802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_454_call = mod.get_global_var('func_454')
func_455_call = mutated_mod.get_global_var('func_455')
call_2826 = relay.TupleGetItem(func_454_call(), 1)
call_2827 = relay.TupleGetItem(func_455_call(), 1)
func_1862_call = mod.get_global_var('func_1862')
func_1863_call = mutated_mod.get_global_var('func_1863')
call_2832 = relay.TupleGetItem(func_1862_call(), 1)
call_2833 = relay.TupleGetItem(func_1863_call(), 1)
func_523_call = mod.get_global_var('func_523')
func_524_call = mutated_mod.get_global_var('func_524')
call_2838 = relay.TupleGetItem(func_523_call(), 0)
call_2839 = relay.TupleGetItem(func_524_call(), 0)
func_1008_call = mod.get_global_var('func_1008')
func_1010_call = mutated_mod.get_global_var('func_1010')
const_2841 = relay.const([1.916657,-5.509819,-3.378153,1.525207,-9.166215,7.151886,-0.784534,6.601672,8.119965,-2.663842,8.438408,-5.402015,-3.572499,9.964857,2.461549,-8.149148,-2.920520,3.679133,-6.125245,-3.781857,9.041915,-4.735365,-7.358895,3.637524,-3.868190,-5.651652,-0.401254,2.408593,7.523760,-7.880449,6.391370,0.619078,6.267038,7.727194,0.501469,-6.490441,6.613329,-6.377327,7.225066,8.352457,3.373046,6.223559,6.514241,3.492797,1.904599,9.507056,-1.715070,-3.674632,-1.148118,3.168089,-0.090664,-5.108655,-4.490862,1.720958,3.194895,2.937236,-4.471657,-9.770869,8.909495,6.547055,8.165557,-9.257212,2.627746,-4.799435,-8.270257,-7.279621,0.134884,-5.705515,9.389221,8.448354,-9.485771,-4.567519,-0.523199,-5.402525,-0.074468,-0.801837,5.587933,0.175183,-1.630798,-6.746249,-8.009436,3.869899,8.260463,3.345539,8.928734,5.449750,-6.181940,-7.624621,-2.469045,-4.200136,-7.390612,1.541451,3.325583,0.947703,-4.910608,-9.219555,-3.206041,-7.011796,1.721738,-6.816672,6.586536,1.888777,8.907719,-6.397821,-1.985431,-7.198810,1.366826,-9.542964,4.998238,-2.186951,9.746144,-8.756315,-9.701138,-0.888352,-0.954462,-4.159349,-1.331013,1.356903,-9.221332,-2.431188,9.135025,9.997780,-6.836408,8.764840,9.572388,1.766934,0.929089,-5.707132,-0.473859,8.668803,-3.365002,-6.568055,1.196825,-9.676112,1.911554,5.691879,-0.283266,-2.010126,-0.583156,-4.802966,0.688000,9.258612,7.407684,7.702745,-1.026707,-0.338489,-5.341071,6.661593,3.028332,7.841995,-6.819365,2.600334,-1.353660,9.010021,4.803167,-1.229634,5.199337,8.589114,-5.074813,4.197060,-2.612298,1.006154,-8.605862,-4.897450,-3.172221,9.120702,-0.620344,5.930231,-3.912278,-1.361271,-9.620958,-9.771821,-2.804629,-3.584273,-3.772714,1.505997,-0.458713,-0.259507,8.288458,-6.520658,-2.178656,7.882013,-9.935332,8.213468,2.517395,-5.949702,9.821628,-0.239307,2.072680,-9.486257,-1.291129,-1.800033,-6.448739,9.574925,0.799633,7.085753,2.297846,6.449167,-6.391920,-2.159381,-7.382055,7.777659,-7.108623,7.261007,2.120116,6.423077,4.765169,-0.705254,-5.543237,5.168161,2.729645,-5.380783,5.637547,-5.406971,-5.740298,-1.424475,9.474026,-3.473541,9.846000,0.849091,1.042516,-0.235799,-9.914858,-8.069946,-2.491365,0.004407,1.969884,5.585249,4.497786,-6.253442,-3.111865,-9.885283,-0.569424,3.876288,-3.692742,-1.153102,-8.606262,-0.513301,9.557425,2.814899,-4.796969,5.315856,-8.289199,1.752402,-4.722491,-6.196011,-2.790521,1.404072,9.567717,-1.828152,1.110400,-8.928297,5.826502,7.200087,8.479038,-5.576595,3.126454,8.773162,-1.179304,0.922844,-8.939347,-9.155255,-2.104262,-4.409405,-5.540916,8.840587,9.543112,8.334491,-0.659370,-1.968230,-7.572939,5.575508,-7.220961,9.641437,3.264496,-0.732669,-0.604907,-6.290079,-5.580164,6.055847,7.977710,-0.731459,-5.091845,8.766060,-5.489051,-3.458119,8.188455,-2.835737,2.402699,-0.430535,-6.260826,-6.461441,8.305869,0.737719,6.025143,6.346538,3.753133,-4.114131,8.014112,-1.480695,1.185804,-9.821632,7.256678,-2.997089,8.479600,6.338895,5.075808,-0.518051,3.340183,-7.117227,-9.681096,3.796124,-6.819333,4.101703,-8.312002,6.961545,8.247501,-2.804315,6.103067,2.688745,3.021625,-3.821827,-2.941769,-7.158651,1.206084,2.742510,-2.424960,4.902048,-4.619862,-6.810207,2.875879,-8.470372,-8.692872,3.879552,4.626024,-9.031808,8.766594,-7.282653,8.567535,0.869472,4.699997,3.471403,-8.075329,-7.208056,1.949618,8.839870,3.911442,2.521799,-4.503956,6.846773,7.448795,-9.370427,-9.735569,4.771178,7.925599,-1.877008,5.366333,-3.118163,7.395654,-1.792112,-5.947509,7.853731,8.604569,8.378412,9.706630,8.817693,-4.741716,5.029156,-7.819302,-2.331241,-4.324730,0.061949,-5.138168,3.872639,-9.675262,9.343129,7.167295,-7.437377,8.987371,-8.120985,-0.841741,-7.850498,3.409876,-8.657504,-8.129411,-7.679277,3.744930,-1.635731,4.459987,0.012571,4.228307,-0.032016,1.127015,8.253994,-7.469473,6.997347,8.377074,8.533148,-5.961548,5.029188,0.542717,2.485544,5.965784,-0.166424,4.598627,-7.395974,-1.602633,4.366387,-9.444112,3.624768,-7.836156,4.123038,-3.862716,-0.010208,-2.740016,8.936128,8.491544,8.764882,-5.870983,-6.945052], dtype = "float64")#candidate|2841|(420,)|const|float64
call_2840 = relay.TupleGetItem(func_1008_call(relay.reshape(const_2841.astype('float64'), [5, 14, 6])), 0)
call_2842 = relay.TupleGetItem(func_1010_call(relay.reshape(const_2841.astype('float64'), [5, 14, 6])), 0)
uop_2846 = relay.sqrt(call_2826.astype('float64')) # shape=(12, 16, 2)
uop_2848 = relay.sqrt(call_2827.astype('float64')) # shape=(12, 16, 2)
func_1133_call = mod.get_global_var('func_1133')
func_1136_call = mutated_mod.get_global_var('func_1136')
call_2851 = relay.TupleGetItem(func_1133_call(relay.reshape(uop_2846.astype('int32'), [12, 16, 2])), 0)
call_2852 = relay.TupleGetItem(func_1136_call(relay.reshape(uop_2846.astype('int32'), [12, 16, 2])), 0)
output = relay.Tuple([call_2832,call_2838,call_2840,const_2841,uop_2846,call_2851,])
output2 = relay.Tuple([call_2833,call_2839,call_2842,const_2841,uop_2848,call_2852,])
func_2853 = relay.Function([], output)
mod['func_2853'] = func_2853
mod = relay.transform.InferType()(mod)
output = func_2853()
func_2854 = relay.Function([], output)
mutated_mod['func_2854'] = func_2854
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2211_call = mod.get_global_var('func_2211')
func_2213_call = mutated_mod.get_global_var('func_2213')
call_2971 = relay.TupleGetItem(func_2211_call(), 0)
call_2972 = relay.TupleGetItem(func_2213_call(), 0)
func_565_call = mod.get_global_var('func_565')
func_568_call = mutated_mod.get_global_var('func_568')
call_2975 = relay.TupleGetItem(func_565_call(relay.reshape(call_2971.astype('bool'), [12, 16, 2])), 0)
call_2976 = relay.TupleGetItem(func_568_call(relay.reshape(call_2971.astype('bool'), [12, 16, 2])), 0)
output = relay.Tuple([call_2971,call_2975,])
output2 = relay.Tuple([call_2972,call_2976,])
func_2980 = relay.Function([], output)
mod['func_2980'] = func_2980
mod = relay.transform.InferType()(mod)
mutated_mod['func_2980'] = func_2980
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2980_call = mutated_mod.get_global_var('func_2980')
call_2981 = func_2980_call()
output = call_2981
func_2982 = relay.Function([], output)
mutated_mod['func_2982'] = func_2982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2801_call = mod.get_global_var('func_2801')
func_2802_call = mutated_mod.get_global_var('func_2802')
call_3037 = relay.TupleGetItem(func_2801_call(), 0)
call_3038 = relay.TupleGetItem(func_2802_call(), 0)
func_2636_call = mod.get_global_var('func_2636')
func_2637_call = mutated_mod.get_global_var('func_2637')
call_3051 = func_2636_call()
call_3052 = func_2636_call()
output = relay.Tuple([call_3037,call_3051,])
output2 = relay.Tuple([call_3038,call_3052,])
func_3055 = relay.Function([], output)
mod['func_3055'] = func_3055
mod = relay.transform.InferType()(mod)
output = func_3055()
func_3056 = relay.Function([], output)
mutated_mod['func_3056'] = func_3056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2298_call = mod.get_global_var('func_2298')
func_2300_call = mutated_mod.get_global_var('func_2300')
call_3071 = relay.TupleGetItem(func_2298_call(), 0)
call_3072 = relay.TupleGetItem(func_2300_call(), 0)
func_2980_call = mod.get_global_var('func_2980')
func_2982_call = mutated_mod.get_global_var('func_2982')
call_3079 = relay.TupleGetItem(func_2980_call(), 1)
call_3080 = relay.TupleGetItem(func_2982_call(), 1)
func_1357_call = mod.get_global_var('func_1357')
func_1359_call = mutated_mod.get_global_var('func_1359')
call_3081 = relay.TupleGetItem(func_1357_call(), 0)
call_3082 = relay.TupleGetItem(func_1359_call(), 0)
output = relay.Tuple([call_3071,call_3079,call_3081,])
output2 = relay.Tuple([call_3072,call_3080,call_3082,])
func_3086 = relay.Function([], output)
mod['func_3086'] = func_3086
mod = relay.transform.InferType()(mod)
output = func_3086()
func_3087 = relay.Function([], output)
mutated_mod['func_3087'] = func_3087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2587_call = mod.get_global_var('func_2587')
func_2588_call = mutated_mod.get_global_var('func_2588')
call_3091 = relay.TupleGetItem(func_2587_call(), 0)
call_3092 = relay.TupleGetItem(func_2588_call(), 0)
func_3055_call = mod.get_global_var('func_3055')
func_3056_call = mutated_mod.get_global_var('func_3056')
call_3099 = relay.TupleGetItem(func_3055_call(), 0)
call_3100 = relay.TupleGetItem(func_3056_call(), 0)
output = relay.Tuple([call_3091,call_3099,])
output2 = relay.Tuple([call_3092,call_3100,])
func_3110 = relay.Function([], output)
mod['func_3110'] = func_3110
mod = relay.transform.InferType()(mod)
mutated_mod['func_3110'] = func_3110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3110_call = mutated_mod.get_global_var('func_3110')
call_3111 = func_3110_call()
output = call_3111
func_3112 = relay.Function([], output)
mutated_mod['func_3112'] = func_3112
mutated_mod = relay.transform.InferType()(mutated_mod)
func_367_call = mod.get_global_var('func_367')
func_368_call = mutated_mod.get_global_var('func_368')
call_3138 = func_367_call()
call_3139 = func_367_call()
func_1942_call = mod.get_global_var('func_1942')
func_1944_call = mutated_mod.get_global_var('func_1944')
call_3149 = func_1942_call()
call_3150 = func_1942_call()
var_3153 = relay.var("var_3153", dtype = "float32", shape = (9, 3, 10))#candidate|3153|(9, 3, 10)|var|float32
bop_3154 = relay.logical_xor(call_3149.astype('uint16'), relay.reshape(var_3153.astype('uint16'), relay.shape_of(call_3149))) # shape=(9, 3, 10)
bop_3157 = relay.logical_xor(call_3150.astype('uint16'), relay.reshape(var_3153.astype('uint16'), relay.shape_of(call_3150))) # shape=(9, 3, 10)
output = relay.Tuple([call_3138,bop_3154,])
output2 = relay.Tuple([call_3139,bop_3157,])
func_3177 = relay.Function([var_3153,], output)
mod['func_3177'] = func_3177
mod = relay.transform.InferType()(mod)
var_3178 = relay.var("var_3178", dtype = "float32", shape = (9, 3, 10))#candidate|3178|(9, 3, 10)|var|float32
output = func_3177(var_3178)
func_3179 = relay.Function([var_3178], output)
mutated_mod['func_3179'] = func_3179
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2211_call = mod.get_global_var('func_2211')
func_2213_call = mutated_mod.get_global_var('func_2213')
call_3236 = relay.TupleGetItem(func_2211_call(), 0)
call_3237 = relay.TupleGetItem(func_2213_call(), 0)
output = relay.Tuple([call_3236,])
output2 = relay.Tuple([call_3237,])
func_3242 = relay.Function([], output)
mod['func_3242'] = func_3242
mod = relay.transform.InferType()(mod)
output = func_3242()
func_3243 = relay.Function([], output)
mutated_mod['func_3243'] = func_3243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_454_call = mod.get_global_var('func_454')
func_455_call = mutated_mod.get_global_var('func_455')
call_3272 = relay.TupleGetItem(func_454_call(), 2)
call_3273 = relay.TupleGetItem(func_455_call(), 2)
func_1592_call = mod.get_global_var('func_1592')
func_1593_call = mutated_mod.get_global_var('func_1593')
call_3280 = relay.TupleGetItem(func_1592_call(), 1)
call_3281 = relay.TupleGetItem(func_1593_call(), 1)
func_2636_call = mod.get_global_var('func_2636')
func_2637_call = mutated_mod.get_global_var('func_2637')
call_3288 = func_2636_call()
call_3289 = func_2636_call()
func_225_call = mod.get_global_var('func_225')
func_226_call = mutated_mod.get_global_var('func_226')
call_3294 = relay.TupleGetItem(func_225_call(), 0)
call_3295 = relay.TupleGetItem(func_226_call(), 0)
output = relay.Tuple([call_3272,call_3280,call_3288,call_3294,])
output2 = relay.Tuple([call_3273,call_3281,call_3289,call_3295,])
func_3311 = relay.Function([], output)
mod['func_3311'] = func_3311
mod = relay.transform.InferType()(mod)
mutated_mod['func_3311'] = func_3311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3311_call = mutated_mod.get_global_var('func_3311')
call_3312 = func_3311_call()
output = call_3312
func_3313 = relay.Function([], output)
mutated_mod['func_3313'] = func_3313
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1842_call = mod.get_global_var('func_1842')
func_1843_call = mutated_mod.get_global_var('func_1843')
call_3336 = func_1842_call()
call_3337 = func_1842_call()
func_1518_call = mod.get_global_var('func_1518')
func_1520_call = mutated_mod.get_global_var('func_1520')
call_3338 = relay.TupleGetItem(func_1518_call(), 0)
call_3339 = relay.TupleGetItem(func_1520_call(), 0)
func_918_call = mod.get_global_var('func_918')
func_919_call = mutated_mod.get_global_var('func_919')
call_3387 = relay.TupleGetItem(func_918_call(), 0)
call_3388 = relay.TupleGetItem(func_919_call(), 0)
var_3403 = relay.var("var_3403", dtype = "float64", shape = (8, 15, 11))#candidate|3403|(8, 15, 11)|var|float64
bop_3404 = relay.subtract(call_3336.astype('uint64'), relay.reshape(var_3403.astype('uint64'), relay.shape_of(call_3336))) # shape=(8, 15, 11)
bop_3407 = relay.subtract(call_3337.astype('uint64'), relay.reshape(var_3403.astype('uint64'), relay.shape_of(call_3337))) # shape=(8, 15, 11)
func_2801_call = mod.get_global_var('func_2801')
func_2802_call = mutated_mod.get_global_var('func_2802')
call_3410 = relay.TupleGetItem(func_2801_call(), 0)
call_3411 = relay.TupleGetItem(func_2802_call(), 0)
output = relay.Tuple([call_3338,call_3387,bop_3404,call_3410,])
output2 = relay.Tuple([call_3339,call_3388,bop_3407,call_3411,])
func_3423 = relay.Function([var_3403,], output)
mod['func_3423'] = func_3423
mod = relay.transform.InferType()(mod)
var_3424 = relay.var("var_3424", dtype = "float64", shape = (8, 15, 11))#candidate|3424|(8, 15, 11)|var|float64
output = func_3423(var_3424)
func_3425 = relay.Function([var_3424], output)
mutated_mod['func_3425'] = func_3425
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1075_call = mod.get_global_var('func_1075')
func_1076_call = mutated_mod.get_global_var('func_1076')
call_3441 = relay.TupleGetItem(func_1075_call(), 0)
call_3442 = relay.TupleGetItem(func_1076_call(), 0)
output = relay.Tuple([call_3441,])
output2 = relay.Tuple([call_3442,])
func_3451 = relay.Function([], output)
mod['func_3451'] = func_3451
mod = relay.transform.InferType()(mod)
mutated_mod['func_3451'] = func_3451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3451_call = mutated_mod.get_global_var('func_3451')
call_3452 = func_3451_call()
output = call_3452
func_3453 = relay.Function([], output)
mutated_mod['func_3453'] = func_3453
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3472 = relay.var("var_3472", dtype = "float64", shape = ())#candidate|3472|()|var|float64
const_3473 = relay.const([[[-4.708637,3.232155,-1.580004,0.413149,6.763888,9.221919,-2.121386,0.149565,-6.743985,6.462867,4.480787],[-7.073697,1.944807,7.851310,8.433693,9.336583,1.255455,-4.019463,6.964407,-1.810816,-0.187374,-6.173741],[-1.085770,-4.220551,5.326680,6.566647,8.211095,7.123336,3.562793,-5.666156,0.164634,-9.450900,-6.858957]],[[-3.472443,-8.145580,6.670626,-9.327216,8.197867,9.462294,5.883687,-2.923011,-4.131367,4.904934,-9.176552],[-1.417147,0.330123,1.979436,-8.908046,-3.235938,8.945524,8.670003,9.057339,7.154227,-7.728716,-3.356226],[4.354150,-8.359151,6.912657,8.086415,9.974769,-1.592039,-9.568571,-2.057274,9.121434,0.609901,-4.258542]],[[2.670524,7.386826,-4.564634,-4.700469,7.811128,0.453097,2.531215,1.285663,3.507258,-4.283246,-2.029874],[8.384823,7.262413,8.966415,8.479658,1.079362,-3.779876,0.060596,-1.651386,2.622859,9.661080,8.320089],[9.325663,-7.847987,5.743489,-2.652973,3.619027,0.812197,5.518950,0.468210,-4.387183,1.481714,0.547409]],[[6.894645,-5.748595,-7.144603,-3.993571,-6.875954,-7.611624,-0.784781,3.332542,5.457117,-9.531395,1.917390],[-7.891149,-2.923514,1.524225,1.686195,0.298957,-8.942338,0.415600,1.301495,7.535787,-9.399298,-7.281142],[2.631430,7.265066,-8.179700,7.789207,7.553823,2.688215,-7.313820,-0.321469,3.190892,5.051962,1.556513]],[[-7.683601,-5.097681,6.774046,-1.053148,4.438734,0.339034,-3.787155,-8.871576,-4.231681,8.103246,4.592457],[-3.840359,2.026968,8.323939,-5.384029,-3.972524,-6.773111,-2.425111,6.215605,3.138912,-8.115772,3.535749],[6.482627,0.448366,-2.600854,7.982295,-9.376275,4.980056,2.340500,-2.135233,3.745601,5.713851,8.924609]],[[3.389909,-7.761815,8.187539,-5.378395,0.502795,-2.537428,1.074103,-6.465741,9.350568,-1.157025,-0.501329],[9.909701,7.205697,7.959847,-3.057722,-3.939817,7.059272,8.930330,-3.061454,-2.796296,5.789003,-8.345364],[4.294990,1.302948,3.509956,4.789494,7.689807,7.276931,8.806567,8.688672,8.852685,-0.531051,-9.723217]],[[-4.271000,4.836721,5.988600,2.019748,0.186176,-2.513030,6.067255,-3.576147,6.947400,-6.925658,2.450537],[-5.630697,1.414211,-9.374738,-8.183506,4.697232,1.628974,6.578156,0.919652,-2.258581,1.614837,5.008787],[7.555749,1.282155,-6.616955,3.676595,-0.323832,-6.788317,2.463866,8.894851,-1.664391,-0.285752,0.637395]],[[-9.216418,1.007780,9.751783,8.594181,6.754105,-1.644705,8.428275,-0.777137,-0.013754,-5.044221,3.079996],[-9.723743,-7.636337,9.043577,-1.848924,-7.531479,-7.709995,-7.431626,6.984599,-5.554799,-5.969101,5.340606],[6.677356,-6.626316,-3.710124,1.931351,-4.752378,-5.702580,-1.177212,-9.726104,-1.618961,5.267463,-6.656759]],[[-1.668367,0.397179,-5.435473,-8.327689,0.812392,-8.970321,9.084631,7.376523,-7.852599,-4.429787,-9.808345],[-8.126335,-5.448313,2.065339,3.294276,6.537248,2.265867,4.174167,-0.642236,-7.273693,7.211903,0.561338],[0.422412,7.886459,-5.696594,2.127970,-9.144389,6.211483,-5.172979,-7.324367,-9.999216,-9.049531,-0.839421]],[[-3.694370,9.760929,2.796957,4.535976,9.789206,1.823172,-2.040960,9.908701,-9.992593,2.664854,-0.936979],[-8.169675,-9.007732,-1.211277,6.926150,-9.106017,0.762299,-1.480245,-8.081518,7.950271,-0.087431,0.906430],[-0.820950,-5.401552,-6.085521,7.965674,-2.989009,-3.798851,-3.833549,4.386356,1.224963,7.052142,4.603470]],[[2.151884,8.852674,2.044735,4.618809,-9.969395,7.240169,-7.372091,6.620928,-9.299048,-5.689812,-3.733798],[8.370141,-9.850607,3.282459,8.974028,0.745934,-5.249836,2.025091,-1.832326,-6.026382,1.705119,-8.394925],[-2.149900,3.013533,5.681392,1.681272,-8.626309,9.548341,5.312287,5.120134,0.005328,-2.740237,1.851841]]], dtype = "float64")#candidate|3473|(11, 3, 11)|const|float64
bop_3474 = relay.floor_divide(var_3472.astype('float64'), const_3473.astype('float64')) # shape=(11, 3, 11)
func_1959_call = mod.get_global_var('func_1959')
func_1962_call = mutated_mod.get_global_var('func_1962')
const_3488 = relay.const([[-9,2],[-8,-9],[-5,2],[7,5],[9,2],[-9,8],[3,9],[6,-9],[8,10],[2,6],[6,9],[1,7],[6,-5],[-10,-3],[3,-4],[7,-5],[-7,-2],[6,-8],[-7,6],[-3,-7],[-2,3],[5,6],[-8,-8],[-4,-2],[8,1],[6,-6],[6,-1],[7,-7],[-2,5],[-8,7],[9,-3],[-8,5],[-8,10],[6,9],[10,-3],[9,7],[2,-1],[1,8],[-3,7],[3,9],[-8,7],[7,-8],[-5,-5],[10,-6],[-4,-5],[-4,8],[-2,-3],[7,-10],[1,9],[-3,-6],[-7,-7],[-2,1],[9,-10],[-9,-4],[-3,7],[9,5],[5,9],[-2,-10],[-5,-7],[-9,1],[-4,-5],[-1,-3],[-6,-6],[-8,-6],[-6,4],[-9,8],[1,-10],[-6,10],[-4,-3],[6,3],[8,6],[2,-10],[-8,-8],[-9,2],[2,10],[-3,-7],[7,-3],[-6,4],[8,10],[3,-8]], dtype = "uint16")#candidate|3488|(80, 2)|const|uint16
call_3487 = relay.TupleGetItem(func_1959_call(relay.reshape(const_3488.astype('uint16'), [2, 16, 5]), relay.reshape(const_3488.astype('uint16'), [2, 16, 5]), ), 0)
call_3489 = relay.TupleGetItem(func_1962_call(relay.reshape(const_3488.astype('uint16'), [2, 16, 5]), relay.reshape(const_3488.astype('uint16'), [2, 16, 5]), ), 0)
uop_3520 = relay.atan(const_3488.astype('float64')) # shape=(80, 2)
func_1008_call = mod.get_global_var('func_1008')
func_1010_call = mutated_mod.get_global_var('func_1010')
var_3524 = relay.var("var_3524", dtype = "float64", shape = (420,))#candidate|3524|(420,)|var|float64
call_3523 = relay.TupleGetItem(func_1008_call(relay.reshape(var_3524.astype('float64'), [5, 14, 6])), 0)
call_3525 = relay.TupleGetItem(func_1010_call(relay.reshape(var_3524.astype('float64'), [5, 14, 6])), 0)
func_2250_call = mod.get_global_var('func_2250')
func_2253_call = mutated_mod.get_global_var('func_2253')
const_3532 = relay.const([3,9,-8,-5,10,5,1,-6,7,1,4,3,1,-1,3,5,-1,-9,-7,-4,-4,-3,-2,10,-2,5,10,-3,-9,1,-2,8,-5,2,3,-8,-7,-4,9,-8,-6,5,3,9,6,-6,10,-4,2,6,-4,-4,3,-9,5,-3,2,-9,8,1,-9,2,2,2,-2,9,1,6,-5,-8,4,-1,1,-3,7,-5,-10,4,5,-6,-2,-2,10,1,-2,-4,-2,3,5,4,-10,6,8,-4,4,7,-4,-3,6,2,2,-6,-10,-10,7,-7,-5,-8,3,-3,1,4,-10,4,10,-5,1,-1,-10,-8,-6,-3,7,3,5,-8,-7,-6,1,4,5,6,-1,-10,9,-8,-2,6,-6,1,5,10,2,-1,-7,4,4,-1,-8,-6,7,-10,6,-2,4,-4,5,-5,1,9,2,-3,5,1,-2,-10,10,-10,7,7,-7,4,-4,-8,4,-4,-3,3,10,1,1,-3,-1,-5,6,10,2,5,3,-2,3,3,4,1,-2,-6,-4,-1,-1,-1,-8,-2,5,8,-3,4,10,-1,7,-8,6,1,-4,-3,9,-4,7,1,7,1,-2,7,6,6,-2,2,2,-6,-6,-3,-6,-5,-5,8,-8,2,-6,1,7,-7], dtype = "int8")#candidate|3532|(240,)|const|int8
call_3531 = relay.TupleGetItem(func_2250_call(relay.reshape(const_3532.astype('int8'), [240,])), 0)
call_3533 = relay.TupleGetItem(func_2253_call(relay.reshape(const_3532.astype('int8'), [240,])), 0)
func_153_call = mod.get_global_var('func_153')
func_154_call = mutated_mod.get_global_var('func_154')
call_3534 = relay.TupleGetItem(func_153_call(), 0)
call_3535 = relay.TupleGetItem(func_154_call(), 0)
func_3423_call = mod.get_global_var('func_3423')
func_3425_call = mutated_mod.get_global_var('func_3425')
var_3537 = relay.var("var_3537", dtype = "float64", shape = (1320,))#candidate|3537|(1320,)|var|float64
call_3536 = relay.TupleGetItem(func_3423_call(relay.reshape(var_3537.astype('float64'), [8, 15, 11])), 0)
call_3538 = relay.TupleGetItem(func_3425_call(relay.reshape(var_3537.astype('float64'), [8, 15, 11])), 0)
bop_3544 = relay.floor_mod(uop_3520.astype('float32'), relay.reshape(call_3487.astype('float32'), relay.shape_of(uop_3520))) # shape=(80, 2)
bop_3547 = relay.floor_mod(uop_3520.astype('float32'), relay.reshape(call_3489.astype('float32'), relay.shape_of(uop_3520))) # shape=(80, 2)
var_3553 = relay.var("var_3553", dtype = "float32", shape = (80, 2))#candidate|3553|(80, 2)|var|float32
bop_3554 = relay.power(bop_3544.astype('float32'), relay.reshape(var_3553.astype('float32'), relay.shape_of(bop_3544))) # shape=(80, 2)
bop_3557 = relay.power(bop_3547.astype('float32'), relay.reshape(var_3553.astype('float32'), relay.shape_of(bop_3547))) # shape=(80, 2)
bop_3558 = relay.bitwise_xor(bop_3554.astype('uint32'), var_3472.astype('uint32')) # shape=(80, 2)
bop_3561 = relay.bitwise_xor(bop_3557.astype('uint32'), var_3472.astype('uint32')) # shape=(80, 2)
output = relay.Tuple([bop_3474,call_3523,var_3524,call_3531,const_3532,call_3534,call_3536,var_3537,bop_3558,])
output2 = relay.Tuple([bop_3474,call_3525,var_3524,call_3533,const_3532,call_3535,call_3538,var_3537,bop_3561,])
func_3574 = relay.Function([var_3472,var_3524,var_3537,var_3553,], output)
mod['func_3574'] = func_3574
mod = relay.transform.InferType()(mod)
mutated_mod['func_3574'] = func_3574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3574_call = mutated_mod.get_global_var('func_3574')
var_3576 = relay.var("var_3576", dtype = "float64", shape = ())#candidate|3576|()|var|float64
var_3577 = relay.var("var_3577", dtype = "float64", shape = (420,))#candidate|3577|(420,)|var|float64
var_3578 = relay.var("var_3578", dtype = "float64", shape = (1320,))#candidate|3578|(1320,)|var|float64
var_3579 = relay.var("var_3579", dtype = "float32", shape = (80, 2))#candidate|3579|(80, 2)|var|float32
call_3575 = func_3574_call(var_3576,var_3577,var_3578,var_3579,)
output = call_3575
func_3580 = relay.Function([var_3576,var_3577,var_3578,var_3579,], output)
mutated_mod['func_3580'] = func_3580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_426_call = mod.get_global_var('func_426')
func_428_call = mutated_mod.get_global_var('func_428')
call_3616 = func_426_call()
call_3617 = func_426_call()
func_1499_call = mod.get_global_var('func_1499')
func_1502_call = mutated_mod.get_global_var('func_1502')
var_3628 = relay.var("var_3628", dtype = "float32", shape = (11232,))#candidate|3628|(11232,)|var|float32
call_3627 = relay.TupleGetItem(func_1499_call(relay.reshape(var_3628.astype('float32'), [864, 13])), 5)
call_3629 = relay.TupleGetItem(func_1502_call(relay.reshape(var_3628.astype('float32'), [864, 13])), 5)
uop_3631 = relay.atanh(var_3628.astype('float64')) # shape=(11232,)
uop_3660 = relay.sqrt(uop_3631.astype('float64')) # shape=(11232,)
bop_3664 = relay.less_equal(uop_3660.astype('bool'), relay.reshape(uop_3631.astype('bool'), relay.shape_of(uop_3660))) # shape=(11232,)
bop_3667 = relay.minimum(uop_3660.astype('int64'), relay.reshape(bop_3664.astype('int64'), relay.shape_of(uop_3660))) # shape=(11232,)
output = relay.Tuple([call_3616,call_3627,bop_3667,])
output2 = relay.Tuple([call_3617,call_3629,bop_3667,])
func_3671 = relay.Function([var_3628,], output)
mod['func_3671'] = func_3671
mod = relay.transform.InferType()(mod)
mutated_mod['func_3671'] = func_3671
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3672 = relay.var("var_3672", dtype = "float32", shape = (11232,))#candidate|3672|(11232,)|var|float32
func_3671_call = mutated_mod.get_global_var('func_3671')
call_3673 = func_3671_call(var_3672)
output = call_3673
func_3674 = relay.Function([var_3672], output)
mutated_mod['func_3674'] = func_3674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_225_call = mod.get_global_var('func_225')
func_226_call = mutated_mod.get_global_var('func_226')
call_3681 = relay.TupleGetItem(func_225_call(), 0)
call_3682 = relay.TupleGetItem(func_226_call(), 0)
output = relay.Tuple([call_3681,])
output2 = relay.Tuple([call_3682,])
func_3687 = relay.Function([], output)
mod['func_3687'] = func_3687
mod = relay.transform.InferType()(mod)
mutated_mod['func_3687'] = func_3687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3687_call = mutated_mod.get_global_var('func_3687')
call_3688 = func_3687_call()
output = call_3688
func_3689 = relay.Function([], output)
mutated_mod['func_3689'] = func_3689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2064_call = mod.get_global_var('func_2064')
func_2066_call = mutated_mod.get_global_var('func_2066')
call_3722 = relay.TupleGetItem(func_2064_call(), 0)
call_3723 = relay.TupleGetItem(func_2066_call(), 0)
uop_3746 = relay.acosh(call_3722.astype('float32')) # shape=(8, 15, 11)
uop_3748 = relay.acosh(call_3723.astype('float32')) # shape=(8, 15, 11)
func_918_call = mod.get_global_var('func_918')
func_919_call = mutated_mod.get_global_var('func_919')
call_3752 = relay.TupleGetItem(func_918_call(), 1)
call_3753 = relay.TupleGetItem(func_919_call(), 1)
func_2743_call = mod.get_global_var('func_2743')
func_2746_call = mutated_mod.get_global_var('func_2746')
const_3759 = relay.const([8.618669,-8.845602,-4.659542,-3.286245,-4.895588,-1.883571,-6.792454,-2.479798,-9.676915,-8.245963,6.458296,3.093758,4.458412,8.342508,4.353033,9.597127,3.974976,8.933213,6.896276,-1.088684,8.138886,-9.779650,8.314249,-0.425475,2.113101,-4.455997,6.993805,-6.072472,-4.022952,8.243533,5.899891,-5.385804,5.517644,-9.947411,4.945315,-8.366770,6.619419,3.573441,7.975211,-6.003452,-6.932704,-8.511871,-5.241624,-0.126165,-7.905308,-0.538908,-8.076582,6.390169,2.613516,8.840853,-0.923139,9.298864,-8.437345,-3.569804,-9.689958,-9.927692,8.799403,-6.981802,5.933162,-9.991322,9.490596,6.861984,-9.846545,0.201670,-5.344431,-1.139298,-4.730247,-6.048596,-5.082989,4.393976,-8.577116,5.593611,-0.444671,6.396211,1.334633,2.561594,3.845037,-1.763796,0.031106,0.298140,-9.544621,-2.309109,2.157767,2.988625,7.623772,-7.811693,-4.376166,-3.545380,8.074073,5.710388,1.619346,6.390865,6.821373,-1.708603,1.255328,3.492224,-0.615409,3.137028,-9.536504,4.502771,4.848761,4.842190,-0.056782,-6.056881,-6.888153,-8.357902,-2.794529,-3.711894,0.361156,5.387643,-9.341805,9.324843,-8.509640,-4.641346,5.209697,7.183189,0.995558,4.995109,-9.867269,3.214727,4.296957,-1.111874,-9.287446,5.289420,-4.981669,-5.037551,7.703482,4.133571,-8.957368,4.934053,7.300573,-8.015354,4.350536,-5.374040,1.560638,-6.035385,1.616392,8.708305,5.089063,-0.719398,9.536118,-7.249478,-0.039012,-2.850750,5.505769,-0.393246,-9.848202,5.037761,-9.850841,9.456760,-1.396586,-0.911762,2.199746,0.076887,3.845509,-8.609068,-7.625149,5.413800,-2.956157,-8.299610,8.032885,-0.520551,3.513505,-0.343309,-3.096279,-8.691008,2.700914,-1.547652,-1.973718,-7.175496,1.764189,-5.474666,7.759222,-6.084050,8.503749,-2.391727,-6.602542,4.831834,-7.445821,5.364539,2.669350,9.124184,6.878560,1.825799,3.490050,4.562886,-4.229893,5.996063,2.508854,3.674810,-9.397296,-1.333069,3.395918,-3.512476,5.040302,-7.878712,0.086189,3.106599,6.710335,-2.775412,-9.677928,-6.056879,0.401191,1.610278,8.202235,-6.632896,-8.219674,-4.218001,-4.393417,7.479597,0.606363,-1.927777,-6.067818,2.607795,0.156708,-7.354912,7.673172,-5.908258,-0.126752,6.204557,0.441639,0.441026,-5.331451,3.772815,2.390156,-9.247373,-1.042201,5.329785,9.806296,-9.656486,3.060828,-6.227070,8.448855,4.405572,-5.193824,-2.839055,-0.283145,0.946266,9.219127,5.279045,-0.637172,3.620519,9.441188,7.115852,4.818949,2.589114,-4.101833,1.103183,-5.250706,-3.848908,-9.889691,-9.037243,-1.260009,9.268115,-8.966127,-2.681393,3.840838,5.658678,4.841486,3.194063,0.305772,6.747712,-7.719319,5.522171,6.428378,-9.664139,-6.520588,8.618006,-5.977357,7.893478,0.634502,1.878705,6.617539,1.162571,5.210900,-7.515079,2.869808,6.613238,-6.067046,8.074726,-6.740095,5.927833,-4.959792,5.344294,-0.669274,-9.283429,8.417761,-0.193626,-4.712782,1.687858,-5.882935,-5.617344,8.325210,1.357611,9.269008,5.745458,-9.064002,-3.970019,2.722702,-6.330795,-8.049549,-1.106364,-2.304968,1.935870,-5.688176,0.746834,-6.085627,9.815696,2.432375,7.118167,3.402979,-0.163855,-5.367880,-9.802759,-1.995248,7.333407,9.319494,-0.932151,-8.258302,2.148460,-6.792790,2.172942,-9.841304,-9.704059,1.179859,-7.692140,3.861512,2.502614,-1.845754,7.799878,-3.962001,6.271137,-5.119099,4.750558,6.684650,-4.567058,3.737207,-0.136358,-5.413931,2.816023,2.782666,-7.025431,-9.061286,-2.985835,2.519561,-4.586664,-5.140099,-1.855327,7.528055,3.183780,-0.413237,8.124727,2.728551,2.186111,-1.291719,0.821288,8.419345,-6.703020,0.296867,-8.920660], dtype = "float32")#candidate|3759|(360,)|const|float32
call_3758 = relay.TupleGetItem(func_2743_call(relay.reshape(const_3759.astype('float32'), [12, 15, 2])), 3)
call_3760 = relay.TupleGetItem(func_2746_call(relay.reshape(const_3759.astype('float32'), [12, 15, 2])), 3)
func_1008_call = mod.get_global_var('func_1008')
func_1010_call = mutated_mod.get_global_var('func_1010')
var_3771 = relay.var("var_3771", dtype = "float64", shape = (420,))#candidate|3771|(420,)|var|float64
call_3770 = relay.TupleGetItem(func_1008_call(relay.reshape(var_3771.astype('float64'), [5, 14, 6])), 0)
call_3772 = relay.TupleGetItem(func_1010_call(relay.reshape(var_3771.astype('float64'), [5, 14, 6])), 0)
func_3574_call = mod.get_global_var('func_3574')
func_3580_call = mutated_mod.get_global_var('func_3580')
var_3781 = relay.var("var_3781", dtype = "float64", shape = ())#candidate|3781|()|var|float64
const_3782 = relay.const([-7.718241,-2.587090,-2.120257,-7.048514,-5.630896,-9.945966,8.954749,2.302852,8.292744,-4.144871,5.403480,1.509566,-5.713762,3.936984,0.884047,3.987913,-3.117216,-5.211434,-9.830241,2.253998,7.534507,2.660969,-3.884892,7.144114,1.565852,-5.289207,-9.904484,-0.843707,-2.945803,-8.062131,-5.248754,9.063102,5.392578,0.457905,-2.975649,-3.155391,-4.489528,4.994899,-1.396368,7.204516,-4.042938,-3.176096,1.868181,-2.198206,-0.135556,6.385814,-6.565705,-4.560990,-7.763040,-2.807924,-2.836863,-3.589008,-8.029478,-0.816384,-7.486560,-7.972294,9.738833,-0.148523,-3.287814,1.359420,5.194960,4.581008,0.231706,-0.105918,1.748359,5.301723,5.839280,9.708090,0.767582,9.532907,2.953458,-4.003130,-4.663869,3.328081,8.139887,-7.971309,9.480078,3.582613,8.973579,-7.212031,-3.159652,-9.913318,-6.202545,5.221142,3.435184,7.529006,1.948369,-1.104388,-4.538058,-9.367845,-7.847816,4.163227,-8.698406,-7.648938,-4.569242,-1.128591,-4.514248,-9.022463,-8.164797,-5.861885,-4.422931,-0.501289,-3.023201,-1.088603,-8.185776,-8.712866,4.681139,-0.535313,-5.439164,8.646983,-8.075677,7.493034,-0.399150,8.476489,-0.350986,3.975317,2.014594,-1.473516,-7.519422,4.471425,0.582842,2.711390,4.069465,-4.720256,-2.550463,-5.929965,0.291016,-5.967641,3.674046,3.218456,4.923692,0.061424,-4.204474,-4.434815,-0.550871,-6.506411,-7.007036,-6.481360,7.186576,9.053508,-5.271244,-1.170043,-6.308334,8.991265,-1.546780,6.080434,3.882800,6.871160,-7.506421,-8.329824,7.084928,-6.511995,-8.407411,4.862400,0.809593,-8.370928,-4.613253,1.275087,6.579857,-4.058177], dtype = "float32")#candidate|3782|(160,)|const|float32
call_3780 = relay.TupleGetItem(func_3574_call(relay.reshape(var_3781.astype('float64'), []), relay.reshape(call_3770.astype('float64'), [420,]), relay.reshape(call_3722.astype('float64'), [1320,]), relay.reshape(const_3782.astype('float32'), [80, 2]), ), 5)
call_3783 = relay.TupleGetItem(func_3580_call(relay.reshape(var_3781.astype('float64'), []), relay.reshape(call_3770.astype('float64'), [420,]), relay.reshape(call_3722.astype('float64'), [1320,]), relay.reshape(const_3782.astype('float32'), [80, 2]), ), 5)
uop_3788 = relay.cosh(uop_3746.astype('float32')) # shape=(8, 15, 11)
uop_3790 = relay.cosh(uop_3748.astype('float32')) # shape=(8, 15, 11)
output = relay.Tuple([call_3752,call_3758,const_3759,call_3770,var_3771,call_3780,var_3781,const_3782,uop_3788,])
output2 = relay.Tuple([call_3753,call_3760,const_3759,call_3772,var_3771,call_3783,var_3781,const_3782,uop_3790,])
func_3792 = relay.Function([var_3771,var_3781,], output)
mod['func_3792'] = func_3792
mod = relay.transform.InferType()(mod)
var_3793 = relay.var("var_3793", dtype = "float64", shape = (420,))#candidate|3793|(420,)|var|float64
var_3794 = relay.var("var_3794", dtype = "float64", shape = ())#candidate|3794|()|var|float64
output = func_3792(var_3793,var_3794,)
func_3795 = relay.Function([var_3793,var_3794,], output)
mutated_mod['func_3795'] = func_3795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2137_call = mod.get_global_var('func_2137')
func_2139_call = mutated_mod.get_global_var('func_2139')
call_3802 = relay.TupleGetItem(func_2137_call(), 0)
call_3803 = relay.TupleGetItem(func_2139_call(), 0)
func_1075_call = mod.get_global_var('func_1075')
func_1076_call = mutated_mod.get_global_var('func_1076')
call_3812 = relay.TupleGetItem(func_1075_call(), 0)
call_3813 = relay.TupleGetItem(func_1076_call(), 0)
func_2250_call = mod.get_global_var('func_2250')
func_2253_call = mutated_mod.get_global_var('func_2253')
const_3815 = relay.const([-1,8,1,9,3,2,-6,8,4,4,-10,3,9,3,3,6,4,5,9,5,9,-2,4,4,5,1,2,-3,6,-3,-6,4,-2,5,-2,-3,-10,9,-4,3,-1,-5,6,2,-4,2,3,-9,-2,6,5,-8,-4,-10,-8,-10,-5,9,-4,5,7,5,-1,5,-9,9,10,-10,2,7,-2,8,3,-3,2,5,5,-9,6,-2,-7,-10,10,-3,1,4,-8,-3,4,8,-3,-5,-4,-5,-10,-7,1,6,-7,-6,1,-2,-6,8,10,-4,-10,1,5,8,4,4,3,9,-9,8,6,-8,6,2,3,-9,7,1,-8,7,4,-9,1,9,-4,-1,1,-5,-5,-5,5,3,5,-5,-3,-7,6,-6,-4,9,5,10,-9,-5,4,-1,3,2,-8,-3,1,-9,-5,-6,-3,-9,-6,4,-4,8,-8,-6,4,1,6,4,3,6,2,7,8,-6,4,10,9,-5,-8,10,-8,-6,4,-2,7,4,-2,5,-8,-6,10,-2,5,-10,8,-7,-10,1,-6,2,2,3,9,-6,10,1,10,-1,-1,-10,-10,3,1,-5,-8,-10,-4,-6,2,4,-4,2,-8,-10,5,-8,-6,-6,-7,-8,9,-7,1,-8,3,-3], dtype = "int8")#candidate|3815|(240,)|const|int8
call_3814 = relay.TupleGetItem(func_2250_call(relay.reshape(const_3815.astype('int8'), [240,])), 1)
call_3816 = relay.TupleGetItem(func_2253_call(relay.reshape(const_3815.astype('int8'), [240,])), 1)
func_1499_call = mod.get_global_var('func_1499')
func_1502_call = mutated_mod.get_global_var('func_1502')
var_3824 = relay.var("var_3824", dtype = "float32", shape = (72, 156))#candidate|3824|(72, 156)|var|float32
call_3823 = relay.TupleGetItem(func_1499_call(relay.reshape(var_3824.astype('float32'), [864, 13])), 5)
call_3825 = relay.TupleGetItem(func_1502_call(relay.reshape(var_3824.astype('float32'), [864, 13])), 5)
func_2298_call = mod.get_global_var('func_2298')
func_2300_call = mutated_mod.get_global_var('func_2300')
call_3826 = relay.TupleGetItem(func_2298_call(), 0)
call_3827 = relay.TupleGetItem(func_2300_call(), 0)
uop_3842 = relay.atanh(call_3812.astype('float32')) # shape=(9, 3, 10)
uop_3844 = relay.atanh(call_3813.astype('float32')) # shape=(9, 3, 10)
output = relay.Tuple([call_3802,call_3814,const_3815,call_3823,var_3824,call_3826,uop_3842,])
output2 = relay.Tuple([call_3803,call_3816,const_3815,call_3825,var_3824,call_3827,uop_3844,])
func_3853 = relay.Function([var_3824,], output)
mod['func_3853'] = func_3853
mod = relay.transform.InferType()(mod)
var_3854 = relay.var("var_3854", dtype = "float32", shape = (72, 156))#candidate|3854|(72, 156)|var|float32
output = func_3853(var_3854)
func_3855 = relay.Function([var_3854], output)
mutated_mod['func_3855'] = func_3855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_642_call = mod.get_global_var('func_642')
func_643_call = mutated_mod.get_global_var('func_643')
call_3900 = relay.TupleGetItem(func_642_call(), 0)
call_3901 = relay.TupleGetItem(func_643_call(), 0)
output = call_3900
output2 = call_3901
func_3906 = relay.Function([], output)
mod['func_3906'] = func_3906
mod = relay.transform.InferType()(mod)
output = func_3906()
func_3907 = relay.Function([], output)
mutated_mod['func_3907'] = func_3907
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3924 = relay.var("var_3924", dtype = "int16", shape = (5, 14, 3))#candidate|3924|(5, 14, 3)|var|int16
var_3925 = relay.var("var_3925", dtype = "int16", shape = (5, 14, 3))#candidate|3925|(5, 14, 3)|var|int16
bop_3926 = relay.left_shift(var_3924.astype('int16'), relay.reshape(var_3925.astype('int16'), relay.shape_of(var_3924))) # shape=(5, 14, 3)
output = relay.Tuple([bop_3926,])
output2 = relay.Tuple([bop_3926,])
func_3931 = relay.Function([var_3924,var_3925,], output)
mod['func_3931'] = func_3931
mod = relay.transform.InferType()(mod)
mutated_mod['func_3931'] = func_3931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3931_call = mutated_mod.get_global_var('func_3931')
var_3933 = relay.var("var_3933", dtype = "int16", shape = (5, 14, 3))#candidate|3933|(5, 14, 3)|var|int16
var_3934 = relay.var("var_3934", dtype = "int16", shape = (5, 14, 3))#candidate|3934|(5, 14, 3)|var|int16
call_3932 = func_3931_call(var_3933,var_3934,)
output = call_3932
func_3935 = relay.Function([var_3933,var_3934,], output)
mutated_mod['func_3935'] = func_3935
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3986 = relay.var("var_3986", dtype = "float32", shape = (8, 7, 4))#candidate|3986|(8, 7, 4)|var|float32
uop_3987 = relay.tan(var_3986.astype('float32')) # shape=(8, 7, 4)
output = relay.Tuple([uop_3987,])
output2 = relay.Tuple([uop_3987,])
func_4000 = relay.Function([var_3986,], output)
mod['func_4000'] = func_4000
mod = relay.transform.InferType()(mod)
mutated_mod['func_4000'] = func_4000
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4001 = relay.var("var_4001", dtype = "float32", shape = (8, 7, 4))#candidate|4001|(8, 7, 4)|var|float32
func_4000_call = mutated_mod.get_global_var('func_4000')
call_4002 = func_4000_call(var_4001)
output = call_4002
func_4003 = relay.Function([var_4001], output)
mutated_mod['func_4003'] = func_4003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_433_call = mod.get_global_var('func_433')
func_434_call = mutated_mod.get_global_var('func_434')
call_4034 = func_433_call()
call_4035 = func_433_call()
func_3055_call = mod.get_global_var('func_3055')
func_3056_call = mutated_mod.get_global_var('func_3056')
call_4040 = relay.TupleGetItem(func_3055_call(), 1)
call_4041 = relay.TupleGetItem(func_3056_call(), 1)
func_2386_call = mod.get_global_var('func_2386')
func_2388_call = mutated_mod.get_global_var('func_2388')
const_4052 = relay.const([5.672781,0.183454,-7.697551,-1.475326,-1.167581,1.483431,-0.947096,-7.882099,4.032439,-1.217070,-9.132196,4.599836,-5.108896,6.106390,-3.621857,1.352661,6.260738,-1.262837,-2.535120,3.877650,-1.289865,-0.603178,5.856837,1.295905,0.226907,-9.067495,-1.116549,9.348134,7.873456,-4.326654,4.172130,-9.533215,-2.598041,-8.873395,4.039225,7.996324,0.957422,-0.901292,-9.557505,8.174992,7.964314,3.504917,3.016504,2.852960,-1.561521,-8.783382,0.509882,-7.725538,1.658772,-1.194480,1.362669,-2.783009,-9.467424,3.892746,8.069831,-2.892119,-3.736443,-9.495799,-5.927266,6.356683,6.168912,-8.953671,-5.191415,-8.311264,-8.022779,-2.723008,-8.165809,-6.844720,9.716047,6.011022,-1.327606,-4.144350,-0.429236,-7.149304,-9.087202,9.061352,9.438891,-5.003072,-4.995863,1.204169,9.817008,-7.771380,-5.401402,-3.993752,9.479040,-2.230494,1.993383,-6.882580,5.292009,-1.126186,-0.118351,0.339657,-0.035336,0.790702,-6.999848,2.898002,-1.129599,9.309705,-1.976644,4.145307,-1.614026,0.643328,-5.927521,8.327900,-9.819689,1.330194,4.856265,-8.056623,-7.719991,-9.752782,-7.445543,-5.852790,-6.982488,2.492084,-9.310689,-0.502817,4.262282,-0.667911,3.345221,7.745764,-5.430000,6.637297,-8.453871,0.151983,9.823897,0.194457,5.328125,7.706170,-1.701268,-9.749126,0.110290,4.062819,-6.596245,-0.308867,5.042941,6.577482,-6.802638,8.241579,-3.753057,9.696016,-4.439276,6.337053,-7.709719,3.892471,4.608467,3.904756,-7.816352,1.889078,9.812300,5.728882,-2.919151,-4.987331,7.419180,0.403122,-4.998279,6.120872,1.108069,-9.018000,7.441033,-2.112272,0.779089,3.636532,-4.158360,-9.896589,-0.983071,-0.161012,-0.313792,5.782587,-8.909245,7.719837,5.608241,-3.608554,4.944673,1.546043,-0.944444,9.920123,0.017103,-0.113014,-9.350948,2.511824,-5.217448,1.230711,-4.393178,-4.146259,9.252681,5.269444,-9.128162,6.587601,-4.209033,6.097712,4.847230,-7.844618,9.952566,-1.637019,5.852221,2.340247,-0.442793,-1.331835,8.149869,2.652921,-9.879750,-7.290139,-0.722400,-5.396373,-5.035947,-7.786596,7.584056,-4.386351,5.616919,-6.778206,0.813455,-7.763534,-9.822718,-5.650336,7.394947,-3.038654,3.350983,-3.783374,-5.690572,-1.145751,-0.034180,-0.697233,-9.340581,5.261949,-7.340823,-5.279622,8.414841,7.209638,-9.262317,2.833963,8.093521,5.231328,-3.253012,7.314245,6.929987,5.579582,-4.196236,4.561484,4.590132,-7.822836,-1.744270,5.603188,9.023056,0.142939,-3.260375,0.853742,-5.656517,-2.570094,-5.334430,4.660385,-3.659660,-5.691432,6.738212,8.570089,-5.484888,-6.698412,-6.498130,-0.439913,-3.347469,8.201120,-7.182633,-1.123661,-5.044182,-0.904189,-0.070005,-4.006840,-3.263849,5.920380,-0.524337,-2.344761,-2.058293,2.171395,-1.206994,-3.735030,6.438337,-6.662180,-6.646991,-4.109805,3.589769,-3.386291,-5.278242,-7.479855,4.948171,-0.395552,-0.638240,-2.035537,6.290699,-1.581538,6.462762,-8.978989,-7.293149,-5.594668,-7.501867,8.258413,1.413778,9.910480,-3.203625,0.204366,-1.218639,4.561264,-3.913467,4.304266,8.419698,-6.850358,8.940637,8.868586,5.202761,-1.007720,-3.985429,4.371694,0.419651,-2.081112,0.658140,1.402616,5.393363,-1.110044,-9.114375,-7.733765,6.939302,-6.523084,8.153285,8.028646,-3.016097,-1.767024,3.007188,-1.246497,9.132252,3.013906,-9.089141,-4.083035,3.444681,-2.334712,-5.661202,-0.553578,0.469353,-6.475188,-3.887656,2.376947,-3.775529,-0.707423,8.996015,-4.758636,9.513822,1.772449,5.036880,8.887838,6.485048,-6.743953,-4.259600,9.367055,-3.117060,1.436606,1.392712,4.089576,-7.245277,-3.165679,-0.361610,-4.049231,-5.227772,-3.055131,5.036720,-7.608806,3.483751,9.906801,4.854816,8.535528,-2.827417,5.769974,6.362481,3.921105,-9.436164,9.956272,9.409406,-2.599126,-7.986144,4.156565,-7.900419,-6.232732,-0.248277,-8.025746,-2.952594,1.745040,-6.247630,9.848618,4.185549,6.017195,-9.193796,8.763806,0.309715,4.119909,-3.320104,1.870849,-8.494946,-5.997715,0.973673,7.351110,-8.309003,4.723784,9.474550,-1.008915,7.609153,-8.469886,-1.592407,3.299746,1.865507,9.668598,9.654188,-0.823854,-7.131658,9.180925,2.878918,-8.193657,3.237962,-2.747631,-7.503497,-7.922893,8.952838,2.979897,-7.720494,8.207766,1.436124,6.595447,6.672384,-4.166333,-3.681584,-3.779421,-6.406938,5.817572,-2.741357,-0.476974,-4.832854,-9.759613,7.694829,4.678884,5.838109,5.524122,-4.275975,5.280846,4.306350,1.586417,0.794588,3.063295,-2.234437,-2.344907,0.546449,7.333916,1.182741,6.722575,6.700424,-2.628334,3.587505,4.999520,-3.926604,8.499713,8.951577,3.084387,-9.320704,-1.643783,5.937687,0.072564,-4.344134,-8.680367,1.096411,-6.571791,-5.871014,9.335952,3.954322,7.595034,6.873396,0.520538,-6.610931,-5.836197,5.738847,1.609212,1.095296,8.722939,-1.972867,6.705610,1.425143,-1.845857,-9.878929,7.195786,7.818731,1.153225,-7.691846,7.317618,5.437290,8.411225,-8.238489,8.087513,-9.003310,4.685350,-6.318668,-4.338570,0.137257,1.411622,-4.301722,7.180165,-3.801563,-0.569927,6.961713,1.077087,5.019811,1.188813,9.419504,5.740042,-0.350913,-6.141618,2.859496,-8.296588,-6.020699,-1.349635,1.832719,-5.942723,-4.510764,-1.623228,-0.075254,-1.982952,-4.888881,8.904692,-3.803278,7.856401,-2.756628,6.257627,-0.124611,-4.073691,-3.070095,4.532589,-1.416489,1.079748,8.009016,-6.430807,2.660411,3.622935,-4.649977,8.234922,-3.046563,4.682875,7.265170,-5.700016,4.876657,-9.140457,-4.081396,7.576489,7.285963,2.928453,-7.412710,-4.624180,2.030803,8.226337,-0.534047,-3.328344,-1.082598,6.350455,6.848255,3.918043,-4.454648,-6.661286,-9.491654,7.077735,-5.617126,-0.432138,-5.147794,-0.319666,-6.506903,-1.573873,-7.934451,5.969879,-9.709681,-1.715545,9.085384,-9.019311,0.270751,-2.310578,-9.920939,2.848742,-6.875454,3.134095,-1.395604,-4.841117,-3.690578,-9.835275,-8.038245,0.123474,-1.778941,-4.857903,4.066545,-6.428295,9.045952,-0.616705,-1.538762,-6.104194,3.807561,-5.202398,9.142014,5.485165,9.094690,-7.804163,0.151756,-0.522771,-5.611972,2.433383,-4.528153,-4.890886,-7.820949,3.922769,8.938870,-5.992944,-9.802563,-6.296403,1.906642,1.004150,3.306645,-1.125587,2.483267,8.741707,1.521941,9.412235,-2.912701,6.780094,6.598645,9.952580,-4.356717,7.704500,-5.773006,-3.929872,5.384060,-5.484007,-5.041112,-9.013919,-4.506938,2.056396,-1.318019,3.402146,-8.540823,-5.968568,0.249849,-2.388440,0.336087,-5.638006,-1.071826,1.904193,-3.038705,-4.998774,9.040692,-5.535242,-4.752945,9.541665,0.525188,0.254351,-5.111730,9.100233,-5.510434,0.623045,2.146293,9.194363,2.804308,-8.953242,0.318862,-8.336108,1.737026,-1.819583,-6.112253,-2.868975,-8.816980,1.864592,6.285569,-0.629808,5.111204,2.853030,-5.316580,-8.620341,-2.143934,6.015965,2.358359,-9.819418,8.361138,6.072556,-9.316937,7.993565,4.568203,4.885473,7.038216,-8.564968,-9.367187,4.865667,2.118843,-0.922014,-4.032391,6.235503,4.305622,-0.206215,-6.711524,-6.079480,-3.451227,2.917541,-5.962886,-8.076018,-2.189177,-7.414308,1.390575,6.099186,4.719218,-9.218235,-8.033219,-1.989962,6.472636,-4.199331,-8.400198,-9.594575,-7.853205,-4.762374,4.903555,-1.075441,-0.347033,-7.219188,-3.526573,-1.709224,7.076740,-2.106343,-1.574664,1.514680,6.184826,8.970627,-3.074695,-2.062918,8.197724,1.776982,-1.044321,-4.100330,8.682451,-1.480869,8.337931,6.988927,4.362705,-4.331147,-4.789762,4.436303,2.748007,6.928588,-2.047573,-6.265540,5.307111,-0.345353,6.030579,-3.153064,3.341456,-7.084099,6.564204,4.752768,5.382850,-1.604619,0.092043,-9.078955,-9.236116,-0.426525,7.629436,-5.004787,1.972289,-7.518058,3.348142,7.738065,3.769698,8.465100,6.219356,1.577063,-8.157496,4.400745,0.464712,-7.105648,0.028355,6.993128,8.463389,4.208435,-1.147438,4.868926,-8.951428,4.923005,0.552512,-1.280443,4.103515,2.006658,8.436896,-9.228392,-8.259403,-0.806771,6.915014,4.776149,4.164113,8.191655,-8.525366,-3.856288,3.373815,3.225415,-3.770024,-4.219972,3.221837,-6.069298,-8.586873,-3.370040,6.964631,-9.392524,-7.524293,-0.647604,9.291608,4.326807,-9.319606,-4.404699,5.403067,-5.551973,-0.976163,-7.476587,2.393187,-0.550678,5.243804,-4.821932,-4.724638,8.829447,-2.166767,-8.404363,-7.408316,-6.830579,8.563397,-0.244089,-8.145798,7.734192,4.663549,-0.128663,-6.998761,-3.258278,5.552419,-3.399313,-3.945125,-9.267591,0.267539,-8.458191,7.517732,1.630961,6.489158,5.209345,-8.578589,-0.157429,-1.164625,-5.375120,-7.710287,-6.440665,-8.444840,6.873755,2.657832,2.544738,-9.324319,-7.580893,-7.770638,6.574438,1.659994,5.456063,2.183978,-7.415427,3.513986,-9.110111,8.656807,2.947062,1.628585,-8.271163,0.043592,-4.200170,0.594713,7.786858,-9.598828,-0.835677,5.620422,5.366722,8.701006,8.802470,4.461040,-4.362957,-3.694950,-2.022394,-9.082353,-7.565348,-0.357462,-4.164423,4.818227,-7.437328,-6.211498,-4.417686,-3.969821,-8.190564,6.334389,-8.251785,3.946162,8.581358,8.607391,9.641944,5.454531,2.124831,-3.261444,9.639448,7.103993,0.846802,-7.700485,2.452868,-4.321008,3.271372,4.983849,-2.796232,-4.724482,9.393940,1.109354,-4.228476,-1.646407,-6.447620,4.644569,5.033235,3.708043,-6.275536,-3.942402,3.523919,0.469708,-7.045020,-9.363643,3.524198,-5.543608,-3.941176,8.430306,-9.530600,-3.092900,4.733639,5.821035,-1.017541,2.242850,-8.830590,9.320007,-4.597566,-3.704621,5.258996,2.850682,-9.606001,6.834609,0.351816,7.973360,2.595839,1.162449,2.946861,6.841264,9.893042,-0.336327,-8.469492,2.774997,-6.999652,3.627679,6.630464,-4.378687,-2.380349,-2.903205,-2.619447,-0.136730,-6.552873,-1.925261,-1.144230,8.539945,1.798273,2.951700,4.110749,-2.148446,6.555040,-5.751358,3.970636,-2.171426,-0.656375,8.352495,-4.948690,-3.000832,0.908301,-2.039546,-2.256163,-0.097573,9.477693,1.153364,-8.861314,-5.086915,9.586052,-8.486062,9.546146,0.394896,-1.783429,-7.322897,-6.106159,9.118773,-9.863789,5.633676,9.418187,-5.062302,0.114252,-2.826442,1.417658,2.054943,1.153229,8.761213,-0.361082,-8.236305,-8.644730,4.375703,-0.582037,-1.289659,-8.424991,1.334975,9.043955,-2.278969,-9.311823,9.723918,8.361293,-1.464884,-0.732059,7.335317,-8.772783,2.774184,1.661770,0.451538,8.342658,-7.497446,7.205375,-1.575594,5.366529,-6.870181,5.142164,5.986171,-9.491765,2.989274,-3.524713,-0.691162,-7.273850,7.428548,-5.312392,7.930305,-1.399165,-4.316347,-8.540549,0.962799,2.809092,6.620073,5.539645,-5.442977,-1.743144,-8.934322,-1.304979,-3.605885,0.517278,-6.601789,-5.860189,3.651494,7.655502,9.624431,-1.829008,6.910451,-7.866898,-2.658819,-2.039592,2.583342,-4.272276,9.953847,-9.096088,-4.292836,3.680314,-8.579390,-9.472598,-3.526457,2.444249,6.696744,-7.506117,0.265436,4.264695,-0.657186,-3.444476,9.435159,-2.700762,-9.987380,-7.237462,-8.415741,8.765786,8.281449,-8.868060,-0.343071,4.363149,-1.567454,-1.942703,-5.043789,2.389592,9.117700,7.254962,0.473549,5.973591,-5.805750,-9.656592,5.990979,2.984711,1.182834,7.708603,1.469807,-7.008038,-5.876888,-3.968345,-0.142269,-5.320556,4.801816,-1.274440,1.191977,-1.523188,5.452226,-5.177223,7.958882,-5.869119,1.799415,-7.025319,-2.630965,-0.448502,4.337384,-1.293553,5.362555,-3.582240], dtype = "float64")#candidate|4052|(1120,)|const|float64
call_4051 = relay.TupleGetItem(func_2386_call(relay.reshape(const_4052.astype('float64'), [8, 14, 10])), 1)
call_4053 = relay.TupleGetItem(func_2388_call(relay.reshape(const_4052.astype('float64'), [8, 14, 10])), 1)
func_1439_call = mod.get_global_var('func_1439')
func_1442_call = mutated_mod.get_global_var('func_1442')
const_4058 = relay.const([[8,2,4,-10,8,8,2,9,9,4,7,3,10,-8,1,-7,-3,6,-8,4,-6,4,-10,-3,7,1,3,-5,-1,7,1,4,-5,-3,5,-9,-2,3,7,3,5,7,-9,-2,5,4,-5,2,-9,3,2,6,-6,-10,-7,7,8,-2,6,1,5,-9,-6,-8,-4,8,2,4,7,1,6,7,-3,4,7,3,1,-10,-3,-1,-9,4,6,-9,1,-6,9,-10,-6,-4,-10,-3,-8,-9,3,-7,10,4,-9,-7,-3,7,8,-6,4,5,6,-6,-3,5,-2,8,4,-7,5,3,-7,-1,10,9,-7,7,-6,-6,-5,-5,-3,-10,-5,10,-1,7,5,-4,7,-8,-10,6,9,5,4,4,4,-4,3,8,-1,3,-5,3,-10,6,10,-8,-5,5,-4,9,-3,7,-1,1,10,-9,10,-8,-5,-4,6,3,6,3,7,8,-6,-5,9,-8,9,-5,9,1,6,10,5,5,1,1,-9,7,3,-2,-9,1,-8,-7,8,3,-1,-7,-8,10,-10,9,-2,-7,-10,7,-9,-5,5,-4,-8,-10,-1,7,-9,1,8,3,4,-4,8,4,-10,-4,1,-9,-6,7,-5,-9,3,-8,-7,10,-10,8,8,3,10,-4,-7,9,-1,3,5,2,1,9,-10,1,-5,-8,-2,-10,10,3,-4,-1,3,5,-7,5,9,-5,-3,9,-7,1,-7,2,-3,-5,9,6,-1,1,-7,5,8,-5,6,1,10,-3,-10,-8,-9,-2,8,-2,8,-6,-8,9,1,-9,7,-2,-1,-7,9,-6,8,-9,-7,-7,4,7,6,-2,-1,6,2,-6,5,5,-1,-4,-2,-7,-6,3,-10,6,8,5,-8,7,2,-4,-1,3,-4,2,10,5,6,7,-10,-3,8,8,-2,-7,-10,-1,2,4,-1,-1,6,8,-6,9,8,2,4,4,-5,-10,6,8,7,3,6,8,2,5,1,-3,10,4,7,7,3,-9,-1,6,-8,-6,4,8,10,-5,-1,-9,-4,-2,3,3,9,2,8,9,-8,10,-9,-2,-4,-1,3,-6,2,-8,-9,10,2,9,-1,-7,3,5,-8,2,-1,-8,2,-1,-2,-1,1,-9,3,-4,6,7,9,-3,6,8,10,-2,-10,9,4,-2,-1,-8],[9,-1,3,6,10,10,7,-3,-6,1,2,9,-10,-10,4,-5,2,-9,4,9,-7,9,-7,-10,9,-8,-1,-8,-9,-10,-6,7,-1,-5,4,-8,-2,-4,1,-3,-5,-3,9,-7,-10,1,-2,-6,-5,-7,-6,9,-3,-9,8,7,5,2,-1,-10,8,7,-8,-4,-3,-1,7,6,-4,6,-7,5,-1,5,8,3,5,-7,-10,-7,5,1,-9,-3,2,-4,10,-2,-8,5,2,-3,5,-1,2,-9,7,10,6,8,-3,-10,4,8,-1,-10,-10,-10,-5,-3,9,6,1,-2,1,9,-4,9,-3,4,9,-4,8,-5,5,2,9,9,-5,-8,-1,-10,-8,-5,-5,2,10,2,-2,-3,-6,-10,-6,-6,-10,-7,3,-5,8,1,-6,5,1,-6,-6,-9,-5,-9,9,-1,-10,-9,-8,6,-2,-9,-10,-4,2,5,10,-2,4,-5,-7,-4,-5,-1,-5,10,4,8,2,4,-4,5,2,9,1,10,8,-4,-5,7,4,1,-7,-9,-9,-4,-3,-6,-8,-2,9,-6,6,-2,-7,-2,8,-8,-2,-3,-1,5,8,8,6,-5,-1,-4,3,7,6,-10,5,-9,-6,-8,-1,-2,4,-5,1,9,-2,-9,8,-6,7,1,5,-1,-2,9,-1,10,-2,-10,-8,-7,2,7,3,-6,-1,-4,-5,-9,-3,-10,-1,4,7,6,-10,8,-8,2,10,2,5,10,-3,6,-7,-2,9,2,9,3,-3,-1,-8,2,3,1,-2,-7,-10,-10,-1,7,-8,6,-7,7,10,10,-3,7,-8,3,1,-2,-4,2,-7,-5,-8,-2,-10,6,9,9,10,-7,8,8,-9,-4,5,8,5,-6,-6,7,-9,7,10,-7,6,9,-5,5,7,7,-3,3,10,-10,-10,-4,3,5,9,-4,-8,-9,9,-7,1,-10,10,-6,-5,-1,-5,-5,4,2,4,8,-10,-4,-1,7,6,-10,-3,1,3,6,-4,-8,1,-4,7,-8,9,8,-5,-1,4,-7,8,-8,9,10,-5,2,8,10,7,4,1,5,-7,-7,10,10,4,-8,2,-4,6,-2,1,-2,1,4,10,-8,-6,9,-8,3,-7,-5,-8,-5,-7,1,-8,-6,-10,10,2,6,2,-3,6,-4,-6,3,8,-8,-6,2]], dtype = "int32")#candidate|4058|(2, 440)|const|int32
call_4057 = relay.TupleGetItem(func_1439_call(relay.reshape(const_4058.astype('int32'), [16, 5, 11])), 1)
call_4059 = relay.TupleGetItem(func_1442_call(relay.reshape(const_4058.astype('int32'), [16, 5, 11])), 1)
output = relay.Tuple([call_4034,call_4040,call_4051,const_4052,call_4057,const_4058,])
output2 = relay.Tuple([call_4035,call_4041,call_4053,const_4052,call_4059,const_4058,])
func_4072 = relay.Function([], output)
mod['func_4072'] = func_4072
mod = relay.transform.InferType()(mod)
mutated_mod['func_4072'] = func_4072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4072_call = mutated_mod.get_global_var('func_4072')
call_4073 = func_4072_call()
output = call_4073
func_4074 = relay.Function([], output)
mutated_mod['func_4074'] = func_4074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1842_call = mod.get_global_var('func_1842')
func_1843_call = mutated_mod.get_global_var('func_1843')
call_4088 = func_1842_call()
call_4089 = func_1842_call()
output = call_4088
output2 = call_4089
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
func_2414_call = mod.get_global_var('func_2414')
func_2416_call = mutated_mod.get_global_var('func_2416')
call_4099 = relay.TupleGetItem(func_2414_call(), 0)
call_4100 = relay.TupleGetItem(func_2416_call(), 0)
func_1518_call = mod.get_global_var('func_1518')
func_1520_call = mutated_mod.get_global_var('func_1520')
call_4115 = relay.TupleGetItem(func_1518_call(), 0)
call_4116 = relay.TupleGetItem(func_1520_call(), 0)
func_3671_call = mod.get_global_var('func_3671')
func_3674_call = mutated_mod.get_global_var('func_3674')
var_4118 = relay.var("var_4118", dtype = "float32", shape = (11232,))#candidate|4118|(11232,)|var|float32
call_4117 = relay.TupleGetItem(func_3671_call(relay.reshape(var_4118.astype('float32'), [11232,])), 0)
call_4119 = relay.TupleGetItem(func_3674_call(relay.reshape(var_4118.astype('float32'), [11232,])), 0)
bop_4122 = relay.divide(call_4117.astype('float32'), relay.reshape(call_4099.astype('float32'), relay.shape_of(call_4117))) # shape=(12, 16, 2)
bop_4125 = relay.divide(call_4119.astype('float32'), relay.reshape(call_4100.astype('float32'), relay.shape_of(call_4119))) # shape=(12, 16, 2)
output = relay.Tuple([call_4115,var_4118,bop_4122,])
output2 = relay.Tuple([call_4116,var_4118,bop_4125,])
func_4131 = relay.Function([var_4118,], output)
mod['func_4131'] = func_4131
mod = relay.transform.InferType()(mod)
mutated_mod['func_4131'] = func_4131
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4132 = relay.var("var_4132", dtype = "float32", shape = (11232,))#candidate|4132|(11232,)|var|float32
func_4131_call = mutated_mod.get_global_var('func_4131')
call_4133 = func_4131_call(var_4132)
output = call_4133
func_4134 = relay.Function([var_4132], output)
mutated_mod['func_4134'] = func_4134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2499_call = mod.get_global_var('func_2499')
func_2501_call = mutated_mod.get_global_var('func_2501')
call_4179 = relay.TupleGetItem(func_2499_call(), 0)
call_4180 = relay.TupleGetItem(func_2501_call(), 0)
output = call_4179
output2 = call_4180
func_4201 = relay.Function([], output)
mod['func_4201'] = func_4201
mod = relay.transform.InferType()(mod)
mutated_mod['func_4201'] = func_4201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4201_call = mutated_mod.get_global_var('func_4201')
call_4202 = func_4201_call()
output = call_4202
func_4203 = relay.Function([], output)
mutated_mod['func_4203'] = func_4203
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1592_call = mod.get_global_var('func_1592')
func_1593_call = mutated_mod.get_global_var('func_1593')
call_4242 = relay.TupleGetItem(func_1592_call(), 1)
call_4243 = relay.TupleGetItem(func_1593_call(), 1)
func_4072_call = mod.get_global_var('func_4072')
func_4074_call = mutated_mod.get_global_var('func_4074')
call_4276 = relay.TupleGetItem(func_4072_call(), 1)
call_4277 = relay.TupleGetItem(func_4074_call(), 1)
output = relay.Tuple([call_4242,call_4276,])
output2 = relay.Tuple([call_4243,call_4277,])
func_4290 = relay.Function([], output)
mod['func_4290'] = func_4290
mod = relay.transform.InferType()(mod)
mutated_mod['func_4290'] = func_4290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4290_call = mutated_mod.get_global_var('func_4290')
call_4291 = func_4290_call()
output = call_4291
func_4292 = relay.Function([], output)
mutated_mod['func_4292'] = func_4292
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4321 = relay.const([[[1.053508,-6.526763,-5.372505,-3.590535,-5.652383,3.034385,4.629282,-4.489673,7.799781],[3.912848,7.641707,-6.250776,5.191521,-4.572664,0.101534,6.282836,-3.919369,-7.750261],[6.066116,-0.023732,-3.624435,8.465575,7.724075,-3.322972,-3.529914,4.208684,8.526532],[-1.180979,0.502836,1.418472,-6.852515,8.158555,-9.891272,8.641486,-3.521760,-8.537789],[1.658000,9.552357,1.490154,0.175370,7.156330,2.690458,2.023730,5.434030,-2.737830],[3.185826,-9.590859,-8.390266,7.326743,-3.219092,9.241630,-4.872936,-2.231333,-2.275698],[3.641213,-3.058622,-5.548562,7.681568,8.671723,0.336193,-8.517306,-7.965388,3.634319],[3.089954,-1.231506,9.391997,-4.354335,-5.468778,3.815210,8.505397,8.839702,7.089982],[1.195159,4.139285,-9.491237,2.040166,8.578874,7.292933,-4.907693,2.155299,-0.004697]],[[-8.417112,2.159435,-3.641414,1.800830,3.290265,7.646636,5.943381,-0.833570,7.088611],[4.493543,9.730530,-8.086561,8.427920,8.870907,1.336110,9.002100,7.615980,-0.257200],[1.705254,4.775368,-0.458635,-9.083012,8.628628,-9.622018,9.118989,5.749631,9.693429],[0.771662,-0.384046,8.924306,-3.415639,-8.071217,9.687847,4.700147,-5.994407,-2.631884],[7.266631,-0.153261,1.623609,9.769660,-7.551022,1.315887,-7.132904,3.900403,7.851145],[-3.782451,4.732977,9.739738,-1.636272,-5.530362,6.801927,4.065820,6.133736,-6.625325],[2.559438,0.380973,-0.136297,5.505139,5.259527,-7.807725,0.510356,-9.707574,1.373639],[-6.794668,8.956612,-8.319966,9.077359,8.754781,-9.136348,8.250864,-5.359866,7.077021],[9.593622,3.855471,9.660674,0.810645,0.715795,-7.534989,-0.050621,-1.408362,7.680448]],[[-5.250782,-4.613300,8.559308,7.989345,-3.768707,2.426622,6.090658,-8.252145,6.421248],[-6.184535,7.896614,-6.213998,-3.107434,-6.997258,-1.708373,7.722963,-1.986153,8.583631],[-4.244848,-3.069151,-3.043334,5.492496,-2.631526,-4.628612,1.356181,-9.494512,-3.515354],[-8.925251,9.073216,7.578338,-7.268670,4.037985,3.143207,-5.831142,9.150571,-8.278100],[-0.254264,4.629479,-9.529047,-4.047149,-4.464564,-9.562652,-0.475476,7.346718,1.645215],[3.194410,-8.358597,-2.766400,3.383646,3.845152,5.972127,-8.713602,3.014874,-8.253671],[-5.190359,-2.389902,5.227966,7.719659,8.695496,-4.668490,-4.463126,3.475791,-4.775577],[-1.985240,-6.335145,-6.132737,9.159785,-5.573487,7.392978,-1.475295,1.893661,-3.919189],[6.555094,-8.852182,1.926933,4.218654,8.087902,-6.599818,-5.504630,7.754415,-4.565597]],[[-3.525575,4.956559,5.944592,0.223450,-0.590175,-4.682359,-4.097817,-0.298613,-8.089798],[7.848632,4.738785,-2.204061,-2.282277,-3.041516,-7.554489,0.971149,4.233069,8.707435],[5.090529,-9.567574,7.260089,9.787162,2.861657,9.740059,9.311722,7.092015,8.896612],[-4.113199,5.298127,5.254862,8.276152,-1.826590,4.453219,2.350722,5.218224,-6.115745],[-0.969216,-6.632612,-2.806903,-0.777615,-3.606670,-2.803473,6.724500,6.558723,-0.385940],[-6.103115,0.500615,-7.367236,-0.186392,-6.220781,8.711721,9.638367,-4.803799,7.312370],[0.998655,-5.990992,-8.273864,6.722514,5.767096,-5.809843,2.983380,8.010869,5.097522],[-2.368997,-4.117204,0.906104,3.247620,9.021875,-9.360654,-1.865879,-9.641927,1.187113],[-9.956060,7.976295,4.658773,2.492602,-4.181530,-0.389290,-8.338385,-3.882893,0.156719]],[[-8.840158,-2.171473,-7.336167,0.785312,-4.516109,5.225624,-9.488664,-2.192987,4.385610],[9.461669,-5.649124,6.192818,4.652659,2.852912,-9.623482,-1.428071,-8.595016,8.362534],[7.763826,1.615783,-0.825959,-6.967934,-1.940343,-3.191307,-7.237618,-7.716889,-4.699891],[2.577292,6.281008,1.497413,0.462008,5.844249,-2.766162,-7.783115,9.906799,4.949065],[-0.845397,-2.194071,-4.726757,-4.165037,-1.335545,7.829400,8.088017,-1.498367,-8.262678],[-9.746765,3.186973,0.498158,-4.210329,-2.433981,5.777633,-0.289935,4.071375,1.544898],[0.953215,-4.516887,-2.707116,-9.027408,2.504927,5.897254,-6.042023,7.444213,6.636301],[4.760585,5.241883,2.647110,9.589436,-6.341272,-4.836889,-6.525364,-2.773807,0.366553],[1.199803,-4.400126,-1.683861,-5.574986,7.958943,4.927432,-8.428839,2.112730,-5.580000]],[[-0.824532,-6.696091,-1.038752,-3.961078,-6.847734,7.374282,-0.699871,-5.424909,4.397908],[-9.586711,2.246109,-3.946921,-1.081050,-5.097741,-9.174426,-9.765293,-6.635779,0.150429],[0.257248,-8.006801,-5.755686,3.525528,-8.082065,6.624937,-1.946977,8.505679,-9.701471],[-1.935358,-6.302013,-7.856584,7.692690,5.995826,0.354074,-4.489426,6.720628,-5.366430],[8.187526,-9.999129,9.190649,8.289845,8.093517,-2.524600,-3.640206,-8.234631,6.143243],[8.987411,9.388745,-8.768634,-7.195972,8.965576,0.942061,6.409020,8.936154,-6.724472],[-2.255747,-5.641037,-7.920093,9.441230,-2.911377,9.070738,-1.596951,-4.344181,-9.513646],[-2.187317,-9.584590,-8.166201,3.711993,-5.206234,5.900631,-2.867193,-7.395585,3.518850],[9.094407,-7.748116,-6.043168,0.011429,-5.186047,-8.783376,-9.085248,1.203458,-0.618715]],[[9.990728,-1.536489,-3.840567,-3.296088,0.217786,0.857977,-9.994647,5.167831,-0.908082],[-6.830222,-0.920053,-1.134925,6.401318,9.103063,9.905242,-0.457431,0.988065,-8.276521],[-5.232684,-9.770756,2.995417,-6.759133,-8.638515,-0.883848,7.790022,-9.239258,-1.151083],[-1.367138,-8.883544,-3.663855,7.851413,-4.048666,5.222229,-4.329958,0.723172,1.433137],[2.223997,-5.679926,9.845684,-5.654325,-4.725798,-2.192956,0.699595,-6.057155,-2.649012],[2.190078,-1.889223,2.486592,-1.589041,8.230090,-8.137201,8.078660,4.212593,-3.047209],[-5.345531,7.096212,5.562539,4.192544,1.351557,-1.234410,1.899762,6.685766,9.451166],[0.937023,2.157308,-0.889717,-0.557004,2.689327,2.568299,-9.478498,-2.716032,-9.475753],[-1.862718,1.944829,-4.197578,3.115746,2.764699,2.639713,0.986322,4.676319,1.674375]],[[3.505392,5.862021,9.867983,-1.424744,-1.101635,-1.820668,-6.389032,0.027635,-1.066244],[-5.155850,3.689822,-4.672021,-6.427733,8.683209,-1.665703,9.687238,-6.184930,-1.120480],[-8.896632,-6.877955,-2.831561,7.514007,6.016091,-7.685550,-3.629028,5.599066,-8.753706],[-2.277711,-6.846519,-5.180726,6.847646,-9.837901,-3.376383,4.678226,2.155809,-8.174051],[-4.979504,-0.717198,-4.945965,0.851048,6.186587,-6.698664,5.402715,8.207801,-0.593196],[-5.951152,8.456871,-4.259006,-4.630408,-1.689602,9.466750,2.615906,2.724835,4.969568],[-4.408575,-3.031499,6.016868,7.046792,-1.157319,-4.614123,5.889957,-6.359795,7.814708],[-4.922394,-6.711743,6.311785,0.675456,-4.119007,0.496806,-9.668278,-4.839351,6.281745],[9.993737,-6.380627,0.634549,4.998862,-2.588730,-7.716926,-6.592568,3.947174,9.659513]],[[-4.209505,3.994382,5.396245,-3.220256,-5.889241,7.231885,-0.711788,-0.774277,-3.246830],[-6.424685,-0.211250,2.089344,-7.448150,-3.765665,-3.133785,9.890022,-5.742929,6.816093],[1.099410,-9.739618,8.981791,3.392619,-8.539130,-2.871658,-5.141337,-9.102308,3.572720],[2.882571,0.774041,9.107625,8.053936,-5.150429,2.557011,-6.798673,1.671672,-5.664893],[-9.224784,1.376317,-2.484796,2.218860,-1.657488,1.023016,5.328390,5.956004,-0.582113],[-5.405550,4.240338,-2.931063,8.767075,0.101248,4.092287,5.555061,-0.192546,-0.131873],[-9.595024,2.730856,-8.130248,8.593739,8.241313,-3.554821,4.694317,1.912655,-9.549864],[-5.638671,-3.434264,-0.458763,1.148906,1.798095,-7.337976,-2.927554,4.280518,8.086155],[1.670288,2.788488,-7.162757,-8.967976,5.078352,-6.670088,3.440029,2.939368,5.541115]],[[0.720942,0.643564,-0.164032,9.826769,-4.529097,-9.930596,-8.136514,-7.355632,-3.443449],[3.955783,2.228225,-6.131626,-8.049689,-6.999886,-3.939116,-0.499286,-0.627835,-4.257196],[4.859883,-7.269490,8.596301,-0.468605,-2.877999,6.519060,4.731674,5.134223,6.568289],[-5.496125,-5.506489,6.162936,-5.250775,-6.086494,0.272507,1.100194,-2.813598,5.011189],[-0.977031,0.635623,-2.299803,7.920668,-5.447454,-5.667530,1.322525,2.371764,0.287473],[-8.744468,-1.782124,9.110886,3.983573,6.949846,-9.259940,1.603654,-5.699737,7.107494],[-0.429499,-7.888651,3.498323,-1.615512,4.024781,-0.896553,8.703768,7.018737,-2.587466],[8.139638,7.382447,3.539284,9.094176,7.131050,-7.899655,7.288849,0.437193,1.758767],[-2.147529,9.404911,2.191242,6.277312,-3.873045,8.737907,2.746787,9.450938,4.010867]],[[-3.228770,6.160720,-4.720203,-9.352689,-8.987444,5.367652,-5.863478,-2.759535,9.608849],[-1.043851,-5.630899,2.488053,4.942443,-3.870342,-2.602400,2.469401,7.462506,-3.200843],[-4.039378,0.670254,-3.851499,-4.733604,-2.654018,6.948930,2.449040,-6.271686,-6.803848],[3.839400,-3.710981,-3.279783,3.971467,3.676988,8.259925,-1.496194,-4.312602,-2.075287],[-5.753512,-3.757731,5.747973,-3.112642,1.441996,-1.062293,4.519930,6.748125,-3.282140],[-7.882957,5.745613,-5.038352,1.968566,0.665598,-4.838885,-2.595933,-1.442330,5.449526],[-3.405445,-8.863856,6.387865,-7.100972,-9.869982,-2.621123,2.315055,-5.298678,1.589263],[1.603672,0.023968,-3.423457,5.864783,-0.977876,2.628379,5.725523,-8.838988,5.775036],[7.638601,-2.843295,4.311189,-7.329786,3.102585,-0.155792,7.972623,6.313674,-2.021260]],[[-1.903678,-2.289265,1.480060,-8.558752,-9.093717,5.283075,-2.183954,8.379984,-0.967804],[-0.354134,2.408694,-1.506008,-1.075313,-5.198321,-6.002898,2.370144,-4.240786,-6.157870],[-8.561275,-5.305707,8.382536,-5.012738,-0.735103,-9.890311,1.245151,8.158979,-0.481965],[-0.828546,6.427822,-7.034180,7.086738,-9.919774,8.745620,7.124760,-1.068838,-5.983915],[0.674371,8.954196,-9.581937,4.289295,-6.606112,3.296998,-5.097389,8.746797,-1.092203],[8.844029,-5.267370,2.015752,-6.591509,0.918804,-1.404861,-0.244738,-3.577286,-4.200978],[6.947290,-8.187466,-4.283616,-0.445136,9.989623,7.318872,9.389417,2.990147,-7.740670],[-2.573271,-0.756278,4.267868,4.264631,-2.004692,-1.223612,3.555814,-6.766829,4.640126],[1.195941,9.286435,-3.273706,-1.213932,-1.275418,5.442465,-6.808306,5.880870,6.595270]],[[7.918976,9.522004,-0.684951,-1.742774,0.028745,-7.765225,-4.893235,5.777702,-4.986223],[-2.432041,9.085853,4.359398,6.846846,-7.929630,-5.842044,-0.431510,9.610933,3.896810],[5.962953,3.607333,4.809799,3.375269,9.183467,9.874273,-8.300892,-3.129063,-0.984804],[-1.474187,6.183521,1.428874,-2.418461,8.655062,7.444125,-5.850342,1.735317,9.358937],[1.164642,-3.270512,4.540925,-8.317298,2.620691,-1.005831,-6.248009,1.997571,7.026132],[4.729628,-1.345752,5.573570,-1.382422,-7.512502,5.291034,-0.375396,3.228927,8.908937],[-0.323066,-8.535382,-0.014899,-2.502886,-2.366365,-7.053239,-0.849311,7.943478,4.717607],[-3.561416,-5.088281,9.272941,-4.656413,-5.269352,-2.642079,4.116670,-2.292276,-8.465012],[-9.181116,4.329224,-3.025149,-1.132850,-8.932747,-9.592948,2.783218,2.958921,4.253507]],[[2.126959,-3.551972,9.992350,-0.603509,8.386339,0.551500,4.448888,-4.412930,-2.335807],[7.474676,5.474193,-7.153801,7.892530,-4.152729,-3.220228,0.226650,-3.276106,9.515731],[-1.376238,-9.040080,-0.391994,7.166332,2.436369,0.917756,-1.027506,-9.063206,-0.085354],[3.033771,-0.313745,-7.924778,-4.047814,4.916329,2.470066,-7.019080,-5.234676,5.883581],[-7.216477,-5.416275,0.561866,9.582244,-0.573832,8.783666,1.338953,-4.158527,4.541313],[-6.739296,-0.725747,-5.933219,-0.203329,8.665575,3.694634,-7.892237,6.564255,6.214440],[-3.184655,0.710323,-4.868132,0.550625,9.017696,-4.289305,-6.246162,-9.887101,-8.285761],[-3.620176,-4.553990,1.507694,-4.930824,0.193369,-6.436557,-5.985591,-2.490825,-9.297783],[9.877144,-1.475692,6.809393,0.701324,7.573207,7.168436,-5.627929,-8.719796,5.281879]],[[-6.968015,0.179618,-9.058845,-8.637366,-8.713329,-6.223341,0.195675,-6.022037,-7.577625],[-1.960911,9.546862,-7.366424,0.061673,-8.697343,3.106427,5.717845,-0.695337,7.952762],[6.025568,5.273073,-3.132059,-7.518308,2.640350,2.762878,-1.149625,7.993918,4.727061],[-5.394394,-6.504395,5.217937,8.552204,5.011809,0.859513,-8.764395,-1.589177,7.960748],[1.351687,8.116797,-4.489364,-9.169568,-5.289709,9.871702,7.725004,6.856049,-7.451914],[6.934128,2.718789,3.126414,-5.119496,6.292838,-3.366672,2.448605,-5.010783,-6.057563],[-2.374929,-1.989753,3.811052,-4.567511,7.670025,-0.986004,-4.086928,2.448920,5.017041],[3.634705,-4.501189,-3.663321,2.219469,-6.360194,-1.069630,-8.850719,-0.486616,-8.342305],[-7.641248,-6.157100,-1.143334,-2.080125,1.610929,-3.201734,-0.348278,-6.595367,3.737561]],[[4.634186,-1.427753,-5.755959,9.597569,7.682524,5.428661,9.036042,8.772597,-2.863592],[-1.950924,-3.562729,-4.675275,-3.323800,-5.649707,-9.523731,-3.397585,-8.084054,6.971639],[6.692464,-5.796109,-8.406298,-2.487290,3.372091,-5.482260,0.813436,-7.802983,-5.596423],[6.327711,-2.660004,6.867749,9.667921,-4.463053,-5.331189,-0.256918,-2.646118,3.796699],[5.026511,-2.004457,0.746659,-9.922998,-6.715140,-9.592612,4.228166,1.545839,-7.986738],[-7.483269,-0.435520,6.397144,2.297801,7.710478,-6.559855,-7.798208,-0.155503,9.275198],[5.404085,4.498256,-6.718087,-3.458114,0.116216,1.750489,-2.490377,3.495571,0.254862],[-5.420085,-3.677455,-0.016352,-0.530147,-4.639320,-1.353213,-8.565618,4.846982,8.942175],[6.490730,-3.418668,6.866703,-5.805006,5.784456,4.970282,4.760743,9.931561,1.323668]]], dtype = "float64")#candidate|4321|(16, 9, 9)|const|float64
uop_4322 = relay.sinh(const_4321.astype('float64')) # shape=(16, 9, 9)
uop_4325 = relay.acos(const_4321.astype('float32')) # shape=(16, 9, 9)
func_1518_call = mod.get_global_var('func_1518')
func_1520_call = mutated_mod.get_global_var('func_1520')
call_4328 = relay.TupleGetItem(func_1518_call(), 0)
call_4329 = relay.TupleGetItem(func_1520_call(), 0)
func_1439_call = mod.get_global_var('func_1439')
func_1442_call = mutated_mod.get_global_var('func_1442')
const_4339 = relay.const([[-3,7,10,-9,-10,3,8,8,-8,-5,-9,6,1,5,-7,-6,-1,-4,-10,3,-5,7,-6,-9,8,-9,-1,2,-4,10,7,-2,8,9,-2,9,9,-9,10,9,6,-5,-5,-10,4,-10,5,-9,-9,10,-3,7,4,-6,5,-4,-5,7,6,9,-7,-2,1,5,2,-1,6,-6,5,-7,-7,-3,-2,2,-10,-1,-2,-1,-6,4,2,2,7,-8,-8,-5,10,7,10,1,4,9,4,-8,-6,6,-10,-6,6,9,3,-3,4,4,-1,4,-6,1,2,-8,-2,6,5,-10,8,-9,5,-3,-1,-3,-1,-8,-1,-6,-8,1,9,3,1,-6,-3,9,8,7,8,-4,8,-5,10,-1,-6,-10,2,-10,9,2,-3,-9,3,-10,5,-10,-5,1,-6,6,7,-6,3,3,-4,-5,-6,-7,2,9,-1,-10,4,4,6,-2,9,-5,4,4,5,-4,-6,1,10,5,9,-2,9,-10,7,1,2,8,-5,3,-4,2,-9,5,-3,5,-8,-4,2,-3,8,4,-1,5,7,-8,6,-2,-5,8,-9,-1,-7,-3,8,7,3,5],[6,-2,7,-7,-1,2,5,-5,3,1,-10,-9,4,2,9,-1,-7,-1,4,1,-6,5,-3,8,-8,-5,5,5,-10,-9,4,8,-5,-8,-7,-8,2,-6,4,10,-5,8,-9,-1,2,9,-2,-9,-4,-7,8,5,9,-8,7,6,-2,-4,-9,-9,-7,-9,3,-7,7,-1,-1,8,10,-4,-3,-1,-7,4,-1,9,9,-8,-5,1,-9,10,9,-10,3,9,4,-1,-4,9,7,-3,3,1,6,-4,4,-3,-2,-5,-8,-1,2,-5,6,-4,-9,1,10,-2,4,9,9,-3,8,-6,-2,-9,2,3,-8,-2,5,1,-3,-10,-10,-7,3,-10,9,7,6,8,-10,5,-9,4,-10,9,-1,-10,-8,-10,6,3,-7,-7,-6,10,-5,3,3,7,-6,5,-3,-8,2,5,-9,5,1,-10,4,-3,6,4,7,3,6,-1,-4,4,-7,8,-9,2,3,-7,4,10,9,-1,3,-2,-3,2,1,5,-6,4,4,-7,9,-7,-3,-3,9,9,-8,-5,-3,8,4,4,6,7,-3,10,8,5,2,-4,-1,-5,5,10,6,1],[-3,1,-2,-3,5,-9,1,-4,3,6,-2,-5,-2,4,4,9,10,-9,10,-9,3,6,3,9,-8,10,-5,-5,-9,-4,-4,-10,-4,-9,1,7,-8,-10,-3,-7,-3,8,-1,6,4,4,-4,2,-3,10,1,-8,10,-9,6,-3,2,-6,6,4,-3,-8,3,4,-3,10,2,4,-5,-7,1,-9,-3,8,8,-7,-10,-7,-7,9,-5,-5,-6,-1,1,3,9,-5,-8,2,-6,-8,-6,-1,5,-2,-10,9,5,8,-1,-8,-2,3,-7,-5,-3,-3,-7,-1,-4,-5,9,10,-6,-10,7,7,10,-9,-4,1,-7,-8,9,-9,2,7,1,-5,-8,-6,-10,4,5,-6,8,-8,-2,-1,4,3,-7,-9,-10,5,-9,2,-4,-1,2,5,7,-6,10,9,1,-1,-6,5,3,3,9,-3,-4,9,2,-7,-9,-7,4,2,1,2,-2,-1,-6,-8,2,7,6,3,2,-6,-4,-2,10,-4,7,-8,2,5,6,5,7,-3,8,2,5,-2,10,7,-8,-2,-6,4,-10,8,-6,-3,4,7,-3,5,6,8,1,-7,6,-6],[8,2,10,-5,4,-1,-5,2,7,7,-5,9,-10,-9,-6,9,-4,3,1,-2,5,3,10,-9,3,10,2,-5,8,7,8,7,4,-8,7,10,-1,-1,6,-8,7,-8,1,-9,9,2,-3,9,-10,-4,5,8,-5,-7,-10,-2,6,6,-5,-6,-5,4,-9,5,2,-6,-1,4,-5,9,-7,2,2,3,-5,4,7,-5,-10,6,10,-10,-6,9,5,-7,-10,8,-9,9,-9,-3,10,-5,-10,4,-2,-5,7,2,-3,-6,7,4,6,9,8,-6,-2,3,-1,-4,-1,3,-4,-2,1,-1,-4,4,10,-9,-5,-9,3,9,-8,7,3,-9,-3,5,9,-4,-10,-6,2,-9,8,4,-9,-5,5,8,2,-6,-6,-10,-4,1,5,-4,-1,-3,-2,-2,1,2,9,-5,-5,7,1,-8,4,-1,-7,3,10,6,-7,5,-6,-4,-6,8,-10,-5,-4,6,-4,-4,-9,-8,-7,3,5,-9,-6,9,-2,3,4,2,3,-4,2,10,7,2,-4,-5,4,3,-7,-10,-1,-2,3,1,-10,4,6,-5,4,6,-4,-9,7,6]], dtype = "int32")#candidate|4339|(4, 220)|const|int32
call_4338 = relay.TupleGetItem(func_1439_call(relay.reshape(const_4339.astype('int32'), [16, 5, 11])), 0)
call_4340 = relay.TupleGetItem(func_1442_call(relay.reshape(const_4339.astype('int32'), [16, 5, 11])), 0)
bop_4344 = relay.right_shift(uop_4322.astype('uint32'), relay.reshape(uop_4325.astype('uint32'), relay.shape_of(uop_4322))) # shape=(16, 9, 9)
uop_4351 = relay.rsqrt(uop_4325.astype('float64')) # shape=(16, 9, 9)
func_2298_call = mod.get_global_var('func_2298')
func_2300_call = mutated_mod.get_global_var('func_2300')
call_4358 = relay.TupleGetItem(func_2298_call(), 1)
call_4359 = relay.TupleGetItem(func_2300_call(), 1)
func_153_call = mod.get_global_var('func_153')
func_154_call = mutated_mod.get_global_var('func_154')
call_4387 = relay.TupleGetItem(func_153_call(), 0)
call_4388 = relay.TupleGetItem(func_154_call(), 0)
output = relay.Tuple([call_4328,call_4338,const_4339,bop_4344,uop_4351,call_4358,call_4387,])
output2 = relay.Tuple([call_4329,call_4340,const_4339,bop_4344,uop_4351,call_4359,call_4388,])
func_4393 = relay.Function([], output)
mod['func_4393'] = func_4393
mod = relay.transform.InferType()(mod)
mutated_mod['func_4393'] = func_4393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4393_call = mutated_mod.get_global_var('func_4393')
call_4394 = func_4393_call()
output = call_4394
func_4395 = relay.Function([], output)
mutated_mod['func_4395'] = func_4395
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4396 = relay.var("var_4396", dtype = "float32", shape = (4, 4))#candidate|4396|(4, 4)|var|float32
uop_4397 = relay.cos(var_4396.astype('float32')) # shape=(4, 4)
func_3906_call = mod.get_global_var('func_3906')
func_3907_call = mutated_mod.get_global_var('func_3907')
call_4407 = func_3906_call()
call_4408 = func_3906_call()
func_2499_call = mod.get_global_var('func_2499')
func_2501_call = mutated_mod.get_global_var('func_2501')
call_4421 = relay.TupleGetItem(func_2499_call(), 0)
call_4422 = relay.TupleGetItem(func_2501_call(), 0)
output = relay.Tuple([uop_4397,call_4407,call_4421,])
output2 = relay.Tuple([uop_4397,call_4408,call_4422,])
func_4425 = relay.Function([var_4396,], output)
mod['func_4425'] = func_4425
mod = relay.transform.InferType()(mod)
mutated_mod['func_4425'] = func_4425
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4426 = relay.var("var_4426", dtype = "float32", shape = (4, 4))#candidate|4426|(4, 4)|var|float32
func_4425_call = mutated_mod.get_global_var('func_4425')
call_4427 = func_4425_call(var_4426)
output = call_4427
func_4428 = relay.Function([var_4426], output)
mutated_mod['func_4428'] = func_4428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_367_call = mod.get_global_var('func_367')
func_368_call = mutated_mod.get_global_var('func_368')
call_4466 = func_367_call()
call_4467 = func_367_call()
output = call_4466
output2 = call_4467
func_4484 = relay.Function([], output)
mod['func_4484'] = func_4484
mod = relay.transform.InferType()(mod)
output = func_4484()
func_4485 = relay.Function([], output)
mutated_mod['func_4485'] = func_4485
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4575 = relay.const([[[-5.011734,-2.470136,2.128392,-1.124424,-0.108570,-7.645181,0.844750,2.154434,-5.357269,9.057208,1.287199,0.485316],[5.479819,-8.903023,8.218651,4.680746,9.364869,4.784563,-4.753998,-3.354525,-2.306710,9.611195,2.313368,8.362647],[-2.357569,-7.524504,-0.299651,-1.814297,1.032592,9.665958,-3.359797,-5.115948,-8.238596,-3.459289,0.101521,-6.420744],[-7.502838,2.975508,-9.889098,6.087848,1.151367,9.802270,0.481158,8.643747,-5.597997,-0.461653,-9.867488,-7.455876]],[[-0.853159,9.991045,6.718013,8.190950,-0.855906,6.083784,2.328026,4.596128,-5.672871,-7.263116,6.008524,-3.310365],[-3.792706,-4.920666,7.605268,0.322093,-7.551990,9.706650,-8.556172,3.590082,7.626562,-8.335500,2.160647,-0.492485],[-6.384491,-1.349272,-2.373282,7.191586,6.571339,9.170651,-2.523073,-3.188898,-3.547237,-4.418398,-2.486948,3.435194],[-4.554379,-4.606082,2.247055,7.000126,7.650875,8.489774,-9.730152,-0.332246,2.951556,-2.186086,-5.374315,-1.537975]],[[-8.739668,-1.987187,-6.754096,-9.858046,5.273362,-6.779325,8.433513,-1.272792,5.469067,6.146825,-6.764316,9.298115],[7.790490,2.533812,-4.544791,-4.844334,-2.212476,1.045090,-3.070127,7.912001,-8.354573,0.197680,9.802328,-4.925055],[5.705778,-3.393057,1.621006,0.320016,6.710309,8.575754,-4.162170,-1.670562,-5.277118,0.543496,6.590145,-6.996614],[9.051783,-9.052414,7.350137,4.848073,-2.678048,-8.745637,-7.420008,-9.218165,-1.882076,7.158451,-5.613148,4.000537]],[[-7.586042,9.304251,3.162569,9.082559,2.507940,9.582037,5.333226,-8.413112,-4.468843,5.735163,-1.051742,-2.779696],[4.787475,-8.371956,4.497688,-0.766472,-8.407808,0.783403,5.638929,-6.101082,-2.339434,0.141247,8.825700,3.480997],[-2.316728,-9.424259,6.839809,4.406462,-9.931528,-2.414520,3.717962,7.113297,-6.729843,2.934574,-8.928892,1.765357],[1.893639,-8.891684,-6.396744,-4.719507,-0.706692,4.155364,5.378419,3.319280,-7.125297,5.809147,-2.956351,-5.910547]],[[-6.888105,3.221192,1.255094,6.615622,6.308250,6.351516,-6.611857,5.039980,-3.970653,-0.435681,5.333942,-2.484678],[5.313008,-3.920641,-0.909135,-5.017667,-2.084484,0.058598,-0.174079,6.385527,-2.312376,5.748193,-1.367174,-3.562246],[-2.068076,0.698639,-7.073774,1.620088,7.882073,4.641387,-7.189673,-3.107701,7.627148,0.774388,5.988985,-4.557121],[1.419433,-1.622140,-7.317846,7.844146,3.544106,-3.478418,-9.944141,1.973466,9.268908,6.260510,-4.975987,0.562275]],[[-3.268073,-5.390834,2.247077,4.774648,-6.836562,-2.926569,-8.687237,1.577462,-5.161677,5.155994,-0.522188,4.789289],[-8.749454,3.510147,-5.483719,-0.483525,2.648254,-6.064273,7.064091,-1.601969,5.703884,-9.265784,-6.549500,2.195164],[-0.819768,0.056338,0.731095,-8.594964,1.789042,5.711398,-1.434039,-4.447149,-0.391187,-7.692521,2.049898,1.635030],[-8.134053,-9.304061,-2.590688,9.377122,0.110184,7.399493,8.009830,-0.006659,2.534227,1.214211,3.138456,-4.171752]],[[-5.626111,-3.944148,6.800999,3.455309,6.620808,-4.264182,5.059219,-9.893481,-5.013266,-3.205090,-6.361080,-1.525527],[-8.061993,4.030068,-4.222256,0.653646,2.285279,-6.831557,1.671999,-9.562795,5.004684,-3.384038,-6.553073,3.646634],[-3.665984,3.755315,-0.579268,7.286935,8.609055,8.880757,-5.944015,-6.096834,-2.609632,-9.761427,-6.095004,-8.469622],[7.879499,0.915589,-4.354984,-6.962507,-9.670861,1.826505,8.872492,8.783143,6.152425,-1.354877,2.789021,0.021043]],[[4.306386,0.182384,-1.009463,-1.792189,8.661285,-2.990778,-6.710784,-4.390559,-1.003497,-5.823291,-0.076832,-7.347684],[-0.040127,3.970297,9.047951,2.502244,-3.374149,4.359060,-1.724633,-3.975767,0.148885,4.349223,5.863801,-4.601838],[7.267030,-1.202895,-0.979833,-0.077262,7.221388,-0.551682,-0.672839,-7.492389,-9.651347,-6.609146,0.296849,-0.863521],[0.985806,-8.691335,-3.701164,-8.349622,6.625313,1.592254,8.736858,-1.444553,-2.740137,1.502017,-8.456005,4.353794]],[[8.766085,-5.242031,1.595063,2.024845,-3.814941,6.683019,-9.367945,7.494163,-6.516491,5.455207,-8.306557,7.232009],[-9.322831,5.560278,-1.839874,-9.877609,-6.854045,-5.189524,8.628312,-7.527885,8.887403,-1.208632,2.742929,-0.858073],[9.466785,6.948153,1.865795,-5.753326,-4.310524,9.811747,-8.973951,-1.438026,-9.279968,-5.465481,6.064739,2.161569],[6.393754,-1.129524,4.146747,-6.764164,8.001269,-6.451290,-6.735222,-9.954118,2.252958,9.079191,3.712643,-1.303837]]], dtype = "float32")#candidate|4575|(9, 4, 12)|const|float32
var_4576 = relay.var("var_4576", dtype = "float32", shape = (9, 4, 12))#candidate|4576|(9, 4, 12)|var|float32
bop_4577 = relay.floor_mod(const_4575.astype('float32'), relay.reshape(var_4576.astype('float32'), relay.shape_of(const_4575))) # shape=(9, 4, 12)
output = bop_4577
output2 = bop_4577
func_4581 = relay.Function([var_4576,], output)
mod['func_4581'] = func_4581
mod = relay.transform.InferType()(mod)
var_4582 = relay.var("var_4582", dtype = "float32", shape = (9, 4, 12))#candidate|4582|(9, 4, 12)|var|float32
output = func_4581(var_4582)
func_4583 = relay.Function([var_4582], output)
mutated_mod['func_4583'] = func_4583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_454_call = mod.get_global_var('func_454')
func_455_call = mutated_mod.get_global_var('func_455')
call_4624 = relay.TupleGetItem(func_454_call(), 2)
call_4625 = relay.TupleGetItem(func_455_call(), 2)
output = call_4624
output2 = call_4625
func_4626 = relay.Function([], output)
mod['func_4626'] = func_4626
mod = relay.transform.InferType()(mod)
output = func_4626()
func_4627 = relay.Function([], output)
mutated_mod['func_4627'] = func_4627
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4645 = relay.var("var_4645", dtype = "int16", shape = (1, 5, 3))#candidate|4645|(1, 5, 3)|var|int16
const_4646 = relay.const([[[-4,-9,-6],[-2,4,8],[1,7,-9],[1,-10,-8],[-3,1,4]],[[3,4,-1],[-3,-3,10],[-9,1,-2],[-4,-6,5],[-3,5,-10]],[[10,7,7],[4,4,7],[9,4,1],[2,6,-2],[-4,-1,9]],[[-9,7,2],[-5,-4,-6],[-2,8,-4],[-1,-6,6],[10,-5,10]],[[2,-4,7],[-5,-4,3],[1,-4,-3],[-7,9,-1],[-5,7,-2]],[[5,-8,5],[7,-10,-8],[-1,-2,5],[7,10,-9],[-9,4,6]],[[2,-9,2],[-8,3,-2],[-2,-7,1],[-10,8,-2],[-2,3,8]],[[-1,-1,-3],[-6,6,10],[8,4,-6],[9,-3,7],[4,-10,-5]],[[-6,-1,7],[-4,6,2],[-9,-7,8],[-7,-1,-6],[8,8,-8]]], dtype = "int16")#candidate|4646|(9, 5, 3)|const|int16
bop_4647 = relay.greater(var_4645.astype('bool'), const_4646.astype('bool')) # shape=(9, 5, 3)
func_1637_call = mod.get_global_var('func_1637')
func_1639_call = mutated_mod.get_global_var('func_1639')
call_4651 = relay.TupleGetItem(func_1637_call(), 2)
call_4652 = relay.TupleGetItem(func_1639_call(), 2)
func_184_call = mod.get_global_var('func_184')
func_187_call = mutated_mod.get_global_var('func_187')
call_4655 = relay.TupleGetItem(func_184_call(relay.reshape(call_4651.astype('bool'), [12, 16, 2])), 0)
call_4656 = relay.TupleGetItem(func_187_call(relay.reshape(call_4651.astype('bool'), [12, 16, 2])), 0)
output = relay.Tuple([bop_4647,call_4651,call_4655,])
output2 = relay.Tuple([bop_4647,call_4652,call_4656,])
func_4657 = relay.Function([var_4645,], output)
mod['func_4657'] = func_4657
mod = relay.transform.InferType()(mod)
var_4658 = relay.var("var_4658", dtype = "int16", shape = (1, 5, 3))#candidate|4658|(1, 5, 3)|var|int16
output = func_4657(var_4658)
func_4659 = relay.Function([var_4658], output)
mutated_mod['func_4659'] = func_4659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2499_call = mod.get_global_var('func_2499')
func_2501_call = mutated_mod.get_global_var('func_2501')
call_4685 = relay.TupleGetItem(func_2499_call(), 0)
call_4686 = relay.TupleGetItem(func_2501_call(), 0)
func_2036_call = mod.get_global_var('func_2036')
func_2037_call = mutated_mod.get_global_var('func_2037')
call_4689 = relay.TupleGetItem(func_2036_call(), 1)
call_4690 = relay.TupleGetItem(func_2037_call(), 1)
var_4693 = relay.var("var_4693", dtype = "int16", shape = (4, 160))#candidate|4693|(4, 160)|var|int16
bop_4694 = relay.left_shift(call_4689.astype('uint32'), var_4693.astype('uint32')) # shape=(4, 160)
bop_4697 = relay.left_shift(call_4690.astype('uint32'), var_4693.astype('uint32')) # shape=(4, 160)
func_2324_call = mod.get_global_var('func_2324')
func_2327_call = mutated_mod.get_global_var('func_2327')
const_4702 = relay.const([[4,6,-4,-2,2,6,-7,-3,-3],[-8,-1,-3,10,-6,10,10,1,-7],[-8,4,3,9,8,2,2,-2,-5],[-9,-5,-4,6,-8,-1,-2,5,8],[-5,7,10,5,-9,4,6,-1,-10],[-7,-8,-3,-1,7,-10,4,-5,-9],[10,6,2,5,3,8,-10,10,-9],[8,-8,6,1,5,10,-2,9,2],[-8,-9,3,-6,2,3,-1,-1,-8],[-8,6,-7,-9,-7,-7,-8,-5,9],[4,-5,3,8,-10,2,-8,9,4],[-10,-4,-9,-7,-7,-6,2,-2,-8],[4,-1,-7,-2,-3,-8,-6,-10,-7],[-3,-8,9,-7,-7,10,5,1,8],[-9,2,-1,9,-9,8,-7,-2,-1],[2,4,8,3,7,1,4,6,-2],[-4,-4,9,1,-3,5,-6,2,4],[-3,5,-3,-7,-8,2,-2,10,-1],[8,-9,7,-2,8,-2,-6,-1,6],[1,10,-6,9,1,4,10,-4,-2],[2,-3,-10,5,9,-10,2,10,-9],[6,-6,7,1,-3,-8,-5,1,-3],[2,-10,5,-9,1,1,-6,8,-6],[-2,-4,-3,2,-3,7,-5,-5,3],[4,1,9,-5,-10,5,-10,6,-3],[-4,-6,-7,4,-3,6,-3,6,-8],[-5,-10,-8,5,-3,9,8,9,4],[-7,8,9,6,8,3,6,9,-5],[2,-4,-10,1,10,-4,-7,-3,10],[1,-2,-7,5,5,3,2,3,-2],[-10,-3,-4,3,7,-6,-7,-5,6],[-6,-9,-4,2,-8,1,-7,3,-1],[8,-8,-1,-4,-1,-5,-4,5,-1],[-6,4,-9,-5,6,-8,-7,-3,1],[-9,-10,5,7,-8,5,-1,4,6],[-10,10,1,5,2,2,9,8,2],[-7,-7,1,-6,-2,10,4,10,-8],[-1,10,-8,-9,-4,10,-2,-4,4],[10,8,10,1,9,-9,-4,-7,-4],[-7,-4,9,6,1,-2,-5,-6,-4],[2,2,9,-8,2,9,2,8,-10],[10,-10,-6,-7,-7,-8,9,8,-1],[3,-2,-5,-10,1,-5,-6,-7,-7],[1,7,-8,8,-5,1,5,-7,8],[10,-1,5,-3,10,-9,4,2,7],[6,-7,4,-1,1,-6,2,-4,-10],[-10,10,-5,-6,9,2,-7,-3,-1],[4,8,2,4,-1,-6,9,-3,7],[-8,-9,-2,-4,9,-5,6,6,5],[-7,9,-7,-10,2,-5,-3,1,-1],[1,4,-7,-4,-10,-9,6,4,-6],[4,-9,-9,-7,-9,-2,-3,-10,-7],[-8,9,3,5,-6,7,-1,-7,-9],[-5,9,-7,6,8,-7,-10,7,-4],[-1,-10,-7,-8,9,-9,4,-5,9],[7,-1,1,9,-6,-3,7,-7,-1],[-3,5,6,2,-9,4,10,5,-4],[1,8,-2,-8,-4,-5,1,6,1],[9,4,10,-8,-7,2,-7,-7,-2],[5,7,5,8,1,10,-8,5,9],[-9,-8,7,-10,-4,-1,-7,6,-8],[5,7,-10,7,-7,9,2,2,6],[3,-8,-4,-5,5,-4,-2,-7,-4],[7,-4,-8,2,-4,-1,8,8,-2],[2,3,7,-10,-6,-10,-3,-6,3],[3,5,4,8,1,-7,-8,8,-8],[-9,-8,5,-5,-6,7,-4,-7,-8],[6,-4,-1,8,1,1,5,-8,-4],[8,1,-2,-3,1,-7,2,6,-10],[6,8,-6,-7,-8,-3,-7,-4,4],[9,4,1,8,5,-9,10,-5,-5],[7,1,6,-10,4,3,9,9,-1],[-5,4,-4,-4,-10,-3,9,6,7],[-7,-7,10,1,2,-5,10,6,9],[-9,-4,-4,-6,7,7,6,-3,-5],[4,4,-7,3,-8,-3,6,-2,3],[-7,10,-2,8,-1,2,-3,3,4],[-8,-1,-3,3,-8,-2,-2,-9,1],[-1,1,1,1,2,5,6,-3,8],[-1,7,-8,10,8,-6,1,9,1],[-7,-7,-8,3,4,1,3,-4,3],[1,-6,3,7,1,-7,-7,-5,-3],[7,-7,3,-6,1,-9,6,8,-1],[3,-6,-6,-7,9,-9,4,-10,10],[10,2,-6,8,2,-3,8,1,-10],[-10,9,-8,-2,6,-7,5,-10,1],[-9,7,8,4,-6,1,-9,-5,-10],[7,-7,-4,-9,2,-8,-7,-3,-8],[-8,6,-7,-2,-7,7,9,-9,-8],[1,-6,9,9,2,-4,-4,3,6],[6,-10,-4,2,2,-10,-8,10,-7],[9,8,-7,-2,-5,-10,6,-9,-10],[-3,6,6,8,10,-8,-8,10,-8],[8,-7,-4,-6,-2,-9,9,9,-7],[-3,10,2,10,-7,-8,9,-3,-9],[-3,9,1,2,-10,-5,-5,-2,4],[3,8,6,4,-1,4,-8,-6,-4],[5,-5,4,-1,-10,4,-9,-10,8]], dtype = "uint16")#candidate|4702|(98, 9)|const|uint16
call_4701 = relay.TupleGetItem(func_2324_call(relay.reshape(const_4702.astype('uint16'), [7, 9, 14])), 0)
call_4703 = relay.TupleGetItem(func_2327_call(relay.reshape(const_4702.astype('uint16'), [7, 9, 14])), 0)
output = relay.Tuple([call_4685,bop_4694,call_4701,const_4702,])
output2 = relay.Tuple([call_4686,bop_4697,call_4703,const_4702,])
func_4704 = relay.Function([var_4693,], output)
mod['func_4704'] = func_4704
mod = relay.transform.InferType()(mod)
mutated_mod['func_4704'] = func_4704
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4705 = relay.var("var_4705", dtype = "int16", shape = (4, 160))#candidate|4705|(4, 160)|var|int16
func_4704_call = mutated_mod.get_global_var('func_4704')
call_4706 = func_4704_call(var_4705)
output = call_4706
func_4707 = relay.Function([var_4705], output)
mutated_mod['func_4707'] = func_4707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2609_call = mod.get_global_var('func_2609')
func_2611_call = mutated_mod.get_global_var('func_2611')
call_4734 = relay.TupleGetItem(func_2609_call(), 0)
call_4735 = relay.TupleGetItem(func_2611_call(), 0)
output = relay.Tuple([call_4734,])
output2 = relay.Tuple([call_4735,])
func_4740 = relay.Function([], output)
mod['func_4740'] = func_4740
mod = relay.transform.InferType()(mod)
mutated_mod['func_4740'] = func_4740
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4740_call = mutated_mod.get_global_var('func_4740')
call_4741 = func_4740_call()
output = call_4741
func_4742 = relay.Function([], output)
mutated_mod['func_4742'] = func_4742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1942_call = mod.get_global_var('func_1942')
func_1944_call = mutated_mod.get_global_var('func_1944')
call_4750 = func_1942_call()
call_4751 = func_1942_call()
func_642_call = mod.get_global_var('func_642')
func_643_call = mutated_mod.get_global_var('func_643')
call_4767 = relay.TupleGetItem(func_642_call(), 3)
call_4768 = relay.TupleGetItem(func_643_call(), 3)
output = relay.Tuple([call_4750,call_4767,])
output2 = relay.Tuple([call_4751,call_4768,])
func_4775 = relay.Function([], output)
mod['func_4775'] = func_4775
mod = relay.transform.InferType()(mod)
output = func_4775()
func_4776 = relay.Function([], output)
mutated_mod['func_4776'] = func_4776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_918_call = mod.get_global_var('func_918')
func_919_call = mutated_mod.get_global_var('func_919')
call_4790 = relay.TupleGetItem(func_918_call(), 0)
call_4791 = relay.TupleGetItem(func_919_call(), 0)
output = call_4790
output2 = call_4791
func_4794 = relay.Function([], output)
mod['func_4794'] = func_4794
mod = relay.transform.InferType()(mod)
output = func_4794()
func_4795 = relay.Function([], output)
mutated_mod['func_4795'] = func_4795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3242_call = mod.get_global_var('func_3242')
func_3243_call = mutated_mod.get_global_var('func_3243')
call_4828 = relay.TupleGetItem(func_3242_call(), 0)
call_4829 = relay.TupleGetItem(func_3243_call(), 0)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
var_4863 = relay.var("var_4863", dtype = "float32", shape = (864,))#candidate|4863|(864,)|var|float32
call_4862 = relay.TupleGetItem(func_261_call(relay.reshape(var_4863.astype('float32'), [12, 8, 9])), 0)
call_4864 = relay.TupleGetItem(func_263_call(relay.reshape(var_4863.astype('float32'), [12, 8, 9])), 0)
var_4874 = relay.var("var_4874", dtype = "float32", shape = (12, 8, 9))#candidate|4874|(12, 8, 9)|var|float32
bop_4875 = relay.power(call_4862.astype('float32'), relay.reshape(var_4874.astype('float32'), relay.shape_of(call_4862))) # shape=(12, 8, 9)
bop_4878 = relay.power(call_4864.astype('float32'), relay.reshape(var_4874.astype('float32'), relay.shape_of(call_4864))) # shape=(12, 8, 9)
bop_4879 = relay.divide(bop_4875.astype('float64'), relay.reshape(call_4862.astype('float64'), relay.shape_of(bop_4875))) # shape=(12, 8, 9)
bop_4882 = relay.divide(bop_4878.astype('float64'), relay.reshape(call_4864.astype('float64'), relay.shape_of(bop_4878))) # shape=(12, 8, 9)
uop_4887 = relay.acosh(call_4862.astype('float64')) # shape=(12, 8, 9)
uop_4889 = relay.acosh(call_4864.astype('float64')) # shape=(12, 8, 9)
func_2743_call = mod.get_global_var('func_2743')
func_2746_call = mutated_mod.get_global_var('func_2746')
const_4893 = relay.const([-0.623623,-0.782808,-0.117860,1.142103,8.029980,-4.207492,-8.307228,0.632623,0.899327,-9.688374,1.696507,4.957782,-2.692512,-0.985782,-8.185498,-1.991029,9.864618,5.704251,7.600455,-9.056413,9.230261,-1.879431,-4.748855,-1.648449,5.879862,5.218221,-2.530212,-4.806445,-8.152195,-4.840526,0.640718,4.091979,-1.460136,-7.068544,-3.701983,-3.093561,5.071793,7.292477,8.663794,8.143066,3.850710,1.831485,9.344145,-4.844089,-9.437923,-2.059334,6.302309,5.455891,-7.618214,2.208012,-9.721129,1.473767,0.986881,9.056186,-4.297817,8.106430,-7.713518,0.026914,-4.473098,2.030763,-4.751899,-0.167601,8.792003,5.661365,0.977154,-9.872981,3.491923,3.292221,2.231402,3.612315,0.214520,5.823571,4.955651,-0.446889,-2.891168,-4.750880,6.731213,1.602818,-7.223296,0.810309,2.558973,-6.182886,9.890092,7.968745,-4.006261,-3.141277,9.407344,8.149049,-5.553355,0.759322,8.676321,3.611239,-4.391010,-6.959199,-6.970823,9.066861,6.024294,-7.757984,5.409500,6.601513,-1.879027,-7.194590,9.198799,-8.303317,1.835921,5.075151,9.235142,6.419665,0.663535,8.199666,6.889333,4.752212,-4.212694,7.394514,-4.609564,9.804819,-8.177237,-5.620077,-3.551402,2.234057,-5.747509,-5.480946,-4.619269,-1.691529,7.914807,8.179558,-4.019262,-3.557149,-3.567078,-2.925921,-3.024001,2.510348,1.896073,6.633678,-2.497975,8.776329,8.039530,-7.677246,-2.233494,0.880131,-2.013396,-9.786974,5.978571,7.011107,6.736287,-5.727898,-2.034691,-3.373264,-3.271269,2.641098,5.995003,3.674850,-9.490146,-6.728179,-4.745413,9.133191,-4.662712,1.257344,-7.538754,8.536203,1.721404,6.887490,0.461213,4.739404,8.945792,-1.246155,-0.843118,8.756574,3.287485,5.624977,6.345938,0.561772,-3.699518,-3.484762,7.333127,-0.809563,5.499215,-8.420193,-4.168145,-7.554842,-7.311390,-5.914979,6.029278,-1.445618,1.644056,-2.205461,-6.320180,-8.326228,3.039373,8.300274,-4.820756,9.598562,2.378860,-4.159021,5.971777,-0.853865,3.514422,-5.993577,-5.694685,9.827355,-8.513176,3.065554,7.868736,-0.933275,-5.457463,-6.470286,2.258394,-2.880963,0.184170,-6.349881,-0.083749,5.862641,2.967509,-1.566346,-0.511580,2.715877,8.641080,9.461710,-4.654055,1.702817,8.719797,9.017252,3.484672,5.063424,-2.421504,-3.037309,-8.287694,-8.478766,8.072230,-6.425737,6.866181,5.746072,-8.169140,5.216937,-3.333476,5.628960,-1.650523,-7.902160,-8.313442,7.954593,-8.942453,6.629874,2.095211,-5.652401,-8.680802,-9.298049,4.346808,2.650797,-9.735918,-5.668813,9.139914,-3.733473,4.310150,-1.097165,-1.206325,-6.407257,3.052746,-6.865911,-2.188582,1.836817,7.549080,-1.625530,8.881195,-4.555769,-8.377048,-5.247304,-9.966029,-2.528040,-1.782609,0.755317,-5.349025,2.114432,-1.064018,-8.731179,-2.332660,5.340004,9.096368,-3.941938,9.184637,-3.396752,-8.284309,-8.585939,2.480051,-1.034400,0.794940,-0.838856,7.061862,2.643936,8.143359,-9.263154,6.997266,5.507906,9.945356,-9.912275,-0.689000,7.302507,7.565354,0.095170,-3.432596,-6.411282,-0.127276,1.926519,-3.878404,7.236724,-5.323026,-8.803920,9.335091,-0.552752,0.291337,-2.592451,5.182546,-4.185370,3.836986,3.309535,4.516105,5.593312,-6.074258,-9.525978,5.482644,0.704301,3.535897,2.012554,7.983041,-2.142285,-3.070800,9.391114,-9.992407,2.927104,3.700773,3.721712,-8.127538,-1.833096,6.267531,-3.834987,-9.845545,-1.813606,8.938453,8.806632,0.676760,0.907666,-1.606342,1.094201,2.544513,-5.491761,1.842503,8.034887,-8.668200,-1.780957,-8.899217,-9.138708,-6.957383,7.562644,-3.085745,4.881959,-0.475054,-6.505609,1.047486,1.857971,-6.422629,6.238994], dtype = "float32")#candidate|4893|(360,)|const|float32
call_4892 = relay.TupleGetItem(func_2743_call(relay.reshape(const_4893.astype('float32'), [12, 15, 2])), 2)
call_4894 = relay.TupleGetItem(func_2746_call(relay.reshape(const_4893.astype('float32'), [12, 15, 2])), 2)
var_4898 = relay.var("var_4898", dtype = "float32", shape = (2, 7, 15))#candidate|4898|(2, 7, 15)|var|float32
bop_4899 = relay.equal(call_4892.astype('bool'), relay.reshape(var_4898.astype('bool'), relay.shape_of(call_4892))) # shape=(2, 7, 15)
bop_4902 = relay.equal(call_4894.astype('bool'), relay.reshape(var_4898.astype('bool'), relay.shape_of(call_4894))) # shape=(2, 7, 15)
uop_4910 = relay.sqrt(call_4862.astype('float32')) # shape=(12, 8, 9)
uop_4912 = relay.sqrt(call_4864.astype('float32')) # shape=(12, 8, 9)
output = relay.Tuple([call_4828,var_4863,bop_4879,uop_4887,const_4893,bop_4899,uop_4910,])
output2 = relay.Tuple([call_4829,var_4863,bop_4882,uop_4889,const_4893,bop_4902,uop_4912,])
func_4915 = relay.Function([var_4863,var_4874,var_4898,], output)
mod['func_4915'] = func_4915
mod = relay.transform.InferType()(mod)
mutated_mod['func_4915'] = func_4915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4915_call = mutated_mod.get_global_var('func_4915')
var_4917 = relay.var("var_4917", dtype = "float32", shape = (864,))#candidate|4917|(864,)|var|float32
var_4918 = relay.var("var_4918", dtype = "float32", shape = (12, 8, 9))#candidate|4918|(12, 8, 9)|var|float32
var_4919 = relay.var("var_4919", dtype = "float32", shape = (2, 7, 15))#candidate|4919|(2, 7, 15)|var|float32
call_4916 = func_4915_call(var_4917,var_4918,var_4919,)
output = call_4916
func_4920 = relay.Function([var_4917,var_4918,var_4919,], output)
mutated_mod['func_4920'] = func_4920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2499_call = mod.get_global_var('func_2499')
func_2501_call = mutated_mod.get_global_var('func_2501')
call_4998 = relay.TupleGetItem(func_2499_call(), 0)
call_4999 = relay.TupleGetItem(func_2501_call(), 0)
output = relay.Tuple([call_4998,])
output2 = relay.Tuple([call_4999,])
func_5004 = relay.Function([], output)
mod['func_5004'] = func_5004
mod = relay.transform.InferType()(mod)
mutated_mod['func_5004'] = func_5004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5004_call = mutated_mod.get_global_var('func_5004')
call_5005 = func_5004_call()
output = call_5005
func_5006 = relay.Function([], output)
mutated_mod['func_5006'] = func_5006
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5033 = relay.var("var_5033", dtype = "float32", shape = (2, 12, 16))#candidate|5033|(2, 12, 16)|var|float32
uop_5034 = relay.erf(var_5033.astype('float32')) # shape=(2, 12, 16)
func_3110_call = mod.get_global_var('func_3110')
func_3112_call = mutated_mod.get_global_var('func_3112')
call_5036 = relay.TupleGetItem(func_3110_call(), 1)
call_5037 = relay.TupleGetItem(func_3112_call(), 1)
output = relay.Tuple([uop_5034,call_5036,])
output2 = relay.Tuple([uop_5034,call_5037,])
func_5038 = relay.Function([var_5033,], output)
mod['func_5038'] = func_5038
mod = relay.transform.InferType()(mod)
mutated_mod['func_5038'] = func_5038
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5039 = relay.var("var_5039", dtype = "float32", shape = (2, 12, 16))#candidate|5039|(2, 12, 16)|var|float32
func_5038_call = mutated_mod.get_global_var('func_5038')
call_5040 = func_5038_call(var_5039)
output = call_5040
func_5041 = relay.Function([var_5039], output)
mutated_mod['func_5041'] = func_5041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_367_call = mod.get_global_var('func_367')
func_368_call = mutated_mod.get_global_var('func_368')
call_5054 = func_367_call()
call_5055 = func_367_call()
output = call_5054
output2 = call_5055
func_5070 = relay.Function([], output)
mod['func_5070'] = func_5070
mod = relay.transform.InferType()(mod)
mutated_mod['func_5070'] = func_5070
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5070_call = mutated_mod.get_global_var('func_5070')
call_5071 = func_5070_call()
output = call_5071
func_5072 = relay.Function([], output)
mutated_mod['func_5072'] = func_5072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1938_call = mod.get_global_var('func_1938')
func_1939_call = mutated_mod.get_global_var('func_1939')
call_5084 = func_1938_call()
call_5085 = func_1938_call()
output = relay.Tuple([call_5084,])
output2 = relay.Tuple([call_5085,])
func_5092 = relay.Function([], output)
mod['func_5092'] = func_5092
mod = relay.transform.InferType()(mod)
mutated_mod['func_5092'] = func_5092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5092_call = mutated_mod.get_global_var('func_5092')
call_5093 = func_5092_call()
output = call_5093
func_5094 = relay.Function([], output)
mutated_mod['func_5094'] = func_5094
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5095 = relay.var("var_5095", dtype = "float32", shape = (16, 2, 8))#candidate|5095|(16, 2, 8)|var|float32
uop_5096 = relay.sqrt(var_5095.astype('float32')) # shape=(16, 2, 8)
func_433_call = mod.get_global_var('func_433')
func_434_call = mutated_mod.get_global_var('func_434')
call_5099 = func_433_call()
call_5100 = func_433_call()
var_5107 = relay.var("var_5107", dtype = "float32", shape = (16, 2, 8))#candidate|5107|(16, 2, 8)|var|float32
bop_5108 = relay.multiply(uop_5096.astype('int32'), relay.reshape(var_5107.astype('int32'), relay.shape_of(uop_5096))) # shape=(16, 2, 8)
output = relay.Tuple([call_5099,bop_5108,])
output2 = relay.Tuple([call_5100,bop_5108,])
func_5118 = relay.Function([var_5095,var_5107,], output)
mod['func_5118'] = func_5118
mod = relay.transform.InferType()(mod)
mutated_mod['func_5118'] = func_5118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5118_call = mutated_mod.get_global_var('func_5118')
var_5120 = relay.var("var_5120", dtype = "float32", shape = (16, 2, 8))#candidate|5120|(16, 2, 8)|var|float32
var_5121 = relay.var("var_5121", dtype = "float32", shape = (16, 2, 8))#candidate|5121|(16, 2, 8)|var|float32
call_5119 = func_5118_call(var_5120,var_5121,)
output = call_5119
func_5122 = relay.Function([var_5120,var_5121,], output)
mutated_mod['func_5122'] = func_5122
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5165 = relay.const([[[2,-5,-1,4,8,-4,-9,5,-1,-8,10,6,-3,6,1,9],[9,2,10,-10,4,-1,-9,9,-1,3,-4,-9,-3,-6,7,2],[1,6,9,-10,-3,6,-9,-2,-1,2,-3,2,-5,2,6,-10],[9,-8,3,1,-9,8,1,-8,2,-10,2,4,-2,9,-2,3]],[[-4,-8,-9,5,-6,-5,2,9,-5,10,1,-5,2,-1,3,-4],[6,-6,-2,2,3,-3,3,10,3,5,5,6,-4,-10,2,-3],[-7,-3,9,5,5,8,1,5,-7,-9,2,10,4,-2,5,5],[4,10,-3,5,4,5,-1,-1,-1,-3,-8,9,-4,-8,-6,-8]],[[1,4,-5,-4,-4,6,9,8,-10,5,5,-9,6,-7,-10,-5],[-2,-9,-9,6,9,-3,-1,-10,-3,10,8,-8,-7,-9,9,-2],[-2,-10,1,6,-9,-10,-1,3,3,3,-3,8,-5,8,2,7],[-10,-4,-10,-5,-1,-9,-5,-4,6,-2,10,8,8,1,8,3]],[[-2,1,9,-3,10,1,-6,6,6,-8,9,-2,-2,8,-1,-7],[9,-7,5,9,1,3,-8,-9,6,-1,-3,-5,-7,4,5,1],[3,-4,-5,4,-4,-5,-7,-7,4,-9,10,-2,8,-3,1,-8],[-9,3,-5,3,-5,2,-3,-4,-4,3,-8,10,-5,10,6,-10]],[[-8,10,9,5,-2,-5,-5,-3,3,-4,5,6,7,-3,2,10],[6,5,5,-7,-8,-5,1,-3,-6,-5,1,10,-7,-4,8,-1],[6,-8,-10,10,-9,-1,5,-5,1,1,-9,-1,-3,7,1,-6],[6,7,-10,3,4,-10,-6,-9,2,10,-2,-10,-5,6,5,-2]],[[5,8,-10,5,-3,-4,-7,-7,-4,2,7,3,-1,10,1,8],[3,1,6,-9,10,-9,8,-8,2,-10,-4,-3,-2,-10,4,8],[5,-3,9,2,-5,8,1,-8,6,2,-1,-4,7,-5,-5,10],[-6,2,5,5,-9,5,-7,-10,1,4,8,-6,-5,8,3,9]],[[-1,5,5,7,-10,-1,-5,3,-7,-1,-6,-10,5,-10,-5,10],[-8,-1,-4,6,-1,3,9,6,-3,-1,-2,-2,8,-9,-9,-7],[5,-1,-6,-5,3,5,-3,8,-7,-5,-9,-10,-6,-7,10,-5],[4,6,-2,-7,8,-9,-4,-5,7,4,6,2,-4,1,7,-1]]], dtype = "int8")#candidate|5165|(7, 4, 16)|const|int8
var_5166 = relay.var("var_5166", dtype = "int8", shape = (7, 4, 16))#candidate|5166|(7, 4, 16)|var|int8
bop_5167 = relay.bitwise_and(const_5165.astype('int8'), relay.reshape(var_5166.astype('int8'), relay.shape_of(const_5165))) # shape=(7, 4, 16)
uop_5173 = relay.atan(var_5166.astype('float64')) # shape=(7, 4, 16)
uop_5175 = relay.asinh(bop_5167.astype('float32')) # shape=(7, 4, 16)
output = relay.Tuple([uop_5173,uop_5175,])
output2 = relay.Tuple([uop_5173,uop_5175,])
func_5184 = relay.Function([var_5166,], output)
mod['func_5184'] = func_5184
mod = relay.transform.InferType()(mod)
mutated_mod['func_5184'] = func_5184
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5185 = relay.var("var_5185", dtype = "int8", shape = (7, 4, 16))#candidate|5185|(7, 4, 16)|var|int8
func_5184_call = mutated_mod.get_global_var('func_5184')
call_5186 = func_5184_call(var_5185)
output = call_5186
func_5187 = relay.Function([var_5185], output)
mutated_mod['func_5187'] = func_5187
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5239 = relay.const([[[-7.109396,-5.386636,-9.798601,-3.996775,-6.807723,1.262794,-6.269640,8.846388],[4.118262,-6.051246,-6.732326,-6.050490,2.712022,3.986892,4.951180,4.844191],[1.342844,7.442822,2.417142,-8.127687,1.365825,-4.880875,3.261529,-2.775134],[-1.045904,7.609531,-0.194437,7.575514,-1.815671,7.610110,8.590449,1.714102],[0.019381,-4.638207,-2.037386,-9.691648,-5.154983,-3.853955,-6.855125,-0.431951],[7.730513,8.195623,1.020419,1.825993,-4.486362,2.316952,0.498922,-6.085633],[-6.115165,4.235537,1.357504,-6.792302,2.995692,-3.272693,8.559869,-0.791429],[-0.124153,-4.354445,-4.339762,0.227724,1.307801,3.611721,1.661818,1.193900],[-8.423707,-6.439469,-0.874556,-1.682520,0.084467,-6.451557,3.400754,4.696200],[-0.438288,-3.224117,2.700688,5.320382,-8.244331,4.812181,3.178544,6.179457],[-6.032521,9.468590,-3.717212,-9.765178,-1.983192,9.782269,4.195418,5.973229],[-5.978253,-3.333267,4.431528,-2.584945,-4.217004,1.875112,-1.312735,-3.777444],[7.318958,-1.022113,9.378228,4.724762,6.903050,1.694023,-6.112723,-4.794084],[-3.978340,-8.982101,6.492567,-7.920104,4.636334,9.867058,-0.772243,-2.292782],[6.087464,-9.301800,8.098795,6.278384,-8.546016,5.312821,9.494521,2.730895],[-7.716573,-3.301900,6.805417,-1.064974,-3.775625,-4.202652,0.042222,-5.231878]],[[8.346278,8.951737,3.640706,2.199008,6.988679,-2.789497,1.523941,4.063559],[2.319676,4.813048,-8.607780,8.892086,7.346007,9.641406,-7.778641,2.808026],[-7.955901,-3.609410,6.310936,3.011947,-2.428024,-9.823071,-0.443121,-1.106968],[6.775865,-9.790128,9.354814,-3.719490,8.774305,6.906474,-2.363927,-9.835170],[4.379889,-2.311076,-1.835165,5.942605,3.309379,-7.455742,1.571419,0.407507],[-2.521047,-8.362587,-7.494676,-3.595571,4.389903,3.179155,2.447741,-8.009343],[1.206522,9.001226,6.014179,-9.025703,-1.166035,-8.647626,3.378029,-5.535656],[0.818221,3.165923,-5.142890,0.175693,9.650974,2.306461,-5.039559,1.405009],[-3.538285,-5.923014,-5.678853,-9.022394,4.281178,-9.156946,-5.106453,7.355094],[-6.689245,0.013686,-8.085306,-7.493953,-8.115514,-1.154580,1.167015,-9.912688],[0.058490,6.783207,7.010783,-6.235314,-8.546248,-9.707287,-7.229661,-1.639305],[-6.025529,3.157792,9.417447,4.465769,0.632299,-9.084385,1.248664,-0.065218],[1.947744,-2.578975,5.498620,-0.768813,-9.513479,-1.041539,-5.101499,2.660636],[3.572215,1.065098,-4.327839,-0.622558,5.160903,-4.388752,3.036468,8.766077],[3.097299,6.415980,-4.117426,-3.011653,-4.185919,1.794945,-6.774905,-7.220595],[7.738003,-6.163261,-8.663999,6.488613,3.328105,-9.173453,-1.617459,-4.193031]]], dtype = "float32")#candidate|5239|(2, 16, 8)|const|float32
uop_5240 = relay.sinh(const_5239.astype('float32')) # shape=(2, 16, 8)
func_819_call = mod.get_global_var('func_819')
func_821_call = mutated_mod.get_global_var('func_821')
var_5244 = relay.var("var_5244", dtype = "uint32", shape = (210,))#candidate|5244|(210,)|var|uint32
call_5243 = relay.TupleGetItem(func_819_call(relay.reshape(var_5244.astype('uint32'), [2, 7, 15])), 3)
call_5245 = relay.TupleGetItem(func_821_call(relay.reshape(var_5244.astype('uint32'), [2, 7, 15])), 3)
func_4425_call = mod.get_global_var('func_4425')
func_4428_call = mutated_mod.get_global_var('func_4428')
const_5250 = relay.const([-2.229898,7.547219,5.487065,7.374159,6.545490,-4.232792,8.246057,-1.064374,-6.900159,-4.697353,3.719737,-3.468913,-2.051518,5.758639,9.770240,5.258147], dtype = "float32")#candidate|5250|(16,)|const|float32
call_5249 = relay.TupleGetItem(func_4425_call(relay.reshape(const_5250.astype('float32'), [4, 4])), 1)
call_5251 = relay.TupleGetItem(func_4428_call(relay.reshape(const_5250.astype('float32'), [4, 4])), 1)
uop_5273 = relay.rsqrt(uop_5240.astype('float64')) # shape=(2, 16, 8)
uop_5282 = relay.erf(uop_5240.astype('float64')) # shape=(2, 16, 8)
output = relay.Tuple([call_5243,var_5244,call_5249,const_5250,uop_5273,uop_5282,])
output2 = relay.Tuple([call_5245,var_5244,call_5251,const_5250,uop_5273,uop_5282,])
func_5294 = relay.Function([var_5244,], output)
mod['func_5294'] = func_5294
mod = relay.transform.InferType()(mod)
mutated_mod['func_5294'] = func_5294
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5295 = relay.var("var_5295", dtype = "uint32", shape = (210,))#candidate|5295|(210,)|var|uint32
func_5294_call = mutated_mod.get_global_var('func_5294')
call_5296 = func_5294_call(var_5295)
output = call_5296
func_5297 = relay.Function([var_5295], output)
mutated_mod['func_5297'] = func_5297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_454_call = mod.get_global_var('func_454')
func_455_call = mutated_mod.get_global_var('func_455')
call_5377 = relay.TupleGetItem(func_454_call(), 1)
call_5378 = relay.TupleGetItem(func_455_call(), 1)
output = relay.Tuple([call_5377,])
output2 = relay.Tuple([call_5378,])
func_5379 = relay.Function([], output)
mod['func_5379'] = func_5379
mod = relay.transform.InferType()(mod)
output = func_5379()
func_5380 = relay.Function([], output)
mutated_mod['func_5380'] = func_5380
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5445 = relay.const([[[-0.804177,-7.461084,4.637555,-6.845223,9.983568,-0.192499,5.098376,-8.769595],[-6.889450,-2.150703,-9.700750,-1.785193,7.386511,-5.674881,8.844766,3.321863],[-0.626490,-4.320478,-9.750108,9.326505,-3.151150,-8.203517,-9.493799,2.500152],[-6.176245,-9.567457,9.115285,8.813554,-0.436533,-7.055978,-8.710856,-7.503679],[1.709230,-2.022709,3.756973,5.481452,-8.143038,-7.578918,2.288026,1.844366],[9.711544,-8.751002,-6.013537,7.053264,-1.913765,-6.029967,-9.542132,6.188452],[6.792117,7.224233,-8.920946,6.942579,-2.120998,0.240340,1.371169,0.506415]],[[-4.931548,8.493257,7.061302,-6.851594,-8.193883,-8.452359,1.709350,3.978976],[-9.971730,8.788762,8.394985,4.103644,-1.405155,3.175478,5.871659,-2.426820],[3.247932,-9.827879,2.109986,-0.263124,-2.185229,-1.334022,-8.670730,-1.485724],[-6.063202,6.323527,-3.714276,6.962861,0.155809,8.979056,3.807621,5.856709],[5.558788,2.967035,-8.022116,9.564809,1.493074,-5.681517,4.446080,-6.050785],[-7.175430,6.731598,-0.790862,-8.034689,-4.111796,-2.150641,9.451773,-3.585776],[4.394264,4.283351,3.636619,-8.822921,-9.752243,-6.526480,-3.565691,9.036815]]], dtype = "float64")#candidate|5445|(2, 7, 8)|const|float64
const_5446 = relay.const([[[0.260842,1.015197,6.619622,9.725333,2.160514,5.248713,-5.867671,-0.421371],[-3.904186,-6.237944,-0.442144,6.076536,-2.668329,4.762483,9.094360,-3.318553],[-5.565183,-7.310878,4.604772,0.202938,-2.258632,-6.059589,8.135545,6.164515],[-7.387282,3.434659,-3.763426,-2.194278,-5.509008,1.478623,-4.659217,-1.231201],[5.703857,-7.272044,4.238185,-3.768356,3.878333,-4.373171,5.506633,-6.038494],[8.732213,-2.129386,2.380137,-4.697914,-7.213766,5.541065,7.487450,4.883982],[-9.458093,-6.157168,1.734065,6.326869,3.919615,5.136659,9.728711,5.441080]],[[8.375048,4.593064,-3.085232,-4.041563,4.482283,6.198609,-0.589483,1.165408],[-3.163581,-0.060228,-4.363130,-1.840170,8.010470,-4.401100,-1.583723,6.186288],[4.356174,-0.702474,-3.761211,-7.009721,-2.211498,-9.688837,-3.676165,4.813129],[6.107641,-5.837520,4.837310,-5.368278,6.511819,-0.569240,-1.334033,6.548760],[-2.178869,5.367210,5.365885,-1.129052,8.486193,-0.944288,-7.040333,-8.334472],[9.078332,-1.678573,-7.294038,4.591711,0.136139,9.450567,0.642489,-0.352700],[-5.447744,-6.166344,8.189209,1.039871,0.174681,0.447999,5.787822,-2.190153]]], dtype = "float64")#candidate|5446|(2, 7, 8)|const|float64
bop_5447 = relay.less(const_5445.astype('bool'), relay.reshape(const_5446.astype('bool'), relay.shape_of(const_5445))) # shape=(2, 7, 8)
output = relay.Tuple([bop_5447,])
output2 = relay.Tuple([bop_5447,])
func_5453 = relay.Function([], output)
mod['func_5453'] = func_5453
mod = relay.transform.InferType()(mod)
output = func_5453()
func_5454 = relay.Function([], output)
mutated_mod['func_5454'] = func_5454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4201_call = mod.get_global_var('func_4201')
func_4203_call = mutated_mod.get_global_var('func_4203')
call_5541 = func_4201_call()
call_5542 = func_4201_call()
output = call_5541
output2 = call_5542
func_5554 = relay.Function([], output)
mod['func_5554'] = func_5554
mod = relay.transform.InferType()(mod)
output = func_5554()
func_5555 = relay.Function([], output)
mutated_mod['func_5555'] = func_5555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2499_call = mod.get_global_var('func_2499')
func_2501_call = mutated_mod.get_global_var('func_2501')
call_5577 = relay.TupleGetItem(func_2499_call(), 0)
call_5578 = relay.TupleGetItem(func_2501_call(), 0)
output = call_5577
output2 = call_5578
func_5580 = relay.Function([], output)
mod['func_5580'] = func_5580
mod = relay.transform.InferType()(mod)
mutated_mod['func_5580'] = func_5580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5580_call = mutated_mod.get_global_var('func_5580')
call_5581 = func_5580_call()
output = call_5581
func_5582 = relay.Function([], output)
mutated_mod['func_5582'] = func_5582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2801_call = mod.get_global_var('func_2801')
func_2802_call = mutated_mod.get_global_var('func_2802')
call_5617 = relay.TupleGetItem(func_2801_call(), 0)
call_5618 = relay.TupleGetItem(func_2802_call(), 0)
func_1439_call = mod.get_global_var('func_1439')
func_1442_call = mutated_mod.get_global_var('func_1442')
const_5620 = relay.const([-5,-7,8,-10,8,-10,2,2,4,-5,6,-5,10,9,-8,-3,5,-10,7,8,8,6,5,-2,-2,3,-8,4,8,9,6,-9,-3,-6,10,6,3,10,9,-6,8,10,-8,3,-10,1,6,6,8,-2,7,8,1,7,9,-5,-1,-2,9,-4,-8,6,-5,-5,-6,3,6,-3,-7,-9,2,-3,8,3,-1,-8,-1,4,7,-1,6,-6,3,-1,8,9,1,4,-9,7,-3,8,-9,2,-4,9,-6,4,2,4,-3,-3,-4,6,-5,3,7,-4,6,2,-10,1,6,7,-9,10,-3,8,2,-1,6,5,-9,-2,6,6,7,-1,-1,10,7,-3,5,-8,-7,3,6,1,-8,10,-8,-9,-2,-7,9,4,-9,8,2,4,8,-5,7,8,10,1,-4,5,3,10,1,-1,5,-6,-5,8,-10,-8,10,4,5,8,-10,-7,4,8,-5,6,6,9,-4,7,-10,3,-10,-10,4,6,2,8,3,1,-5,-8,-1,-4,-3,-9,7,-5,-8,-4,4,8,-3,1,-4,-4,9,2,8,-5,9,4,-5,-5,-3,-5,10,2,-2,9,-7,-5,-4,8,-2,-3,-6,-9,5,4,-4,4,2,7,-10,10,-1,4,1,-9,7,-6,-8,-4,10,10,6,-9,-9,2,5,5,-6,-1,-4,-2,4,-4,4,7,5,-9,1,-1,4,-8,-5,5,5,-10,8,-10,9,-7,1,6,-3,-10,3,-5,-7,8,-9,5,8,-4,5,-1,7,5,3,-7,8,-1,1,10,10,-9,-10,2,8,-6,-10,-7,-6,9,8,6,-5,9,-4,1,-8,4,5,-7,1,-9,-10,-2,-3,-6,8,6,-2,9,-5,-1,-3,10,10,-2,-9,-6,9,5,-8,10,-4,7,-1,-1,7,9,6,7,-5,9,-1,-4,2,2,-10,-5,-9,10,1,8,5,9,7,7,6,-7,-10,9,10,-1,-4,-7,-1,4,-10,9,2,-9,5,-10,-4,9,-7,8,-10,8,-7,6,3,9,4,3,7,6,7,-4,2,5,-4,7,-1,-7,-1,8,4,-1,7,-6,-3,-8,-8,-9,8,2,-6,3,5,8,4,1,-3,-6,-6,9,-5,-2,-9,-5,-5,-8,-5,10,2,7,-2,-4,3,-7,4,-10,3,2,-3,1,-2,-10,-2,9,8,10,6,-7,3,6,2,-6,6,-10,-3,-8,2,5,8,-7,-2,6,-8,5,-9,-9,-6,7,-1,2,2,2,-8,7,3,-2,-9,-2,-1,10,-9,2,-4,-9,10,10,3,-3,2,-9,-3,9,9,-3,-10,2,-2,5,5,-10,9,-6,-5,-5,10,2,-5,9,4,-4,-5,-4,-3,2,4,3,-5,8,-10,6,9,7,-9,-9,8,-9,-10,-9,-1,10,-4,-1,-4,8,-3,5,-2,-7,-9,-8,-10,10,-10,-2,2,8,-9,-7,-7,-8,-9,2,7,6,4,3,-1,-3,-3,-1,8,-3,10,9,-4,10,2,-7,-1,-5,7,10,-2,-8,-9,2,-10,-6,4,8,4,5,9,-5,7,7,7,-1,-10,3,-7,7,-9,-8,8,-5,5,8,-2,-6,2,-10,-9,-7,-9,8,-5,-5,-8,1,2,-8,-4,3,-9,2,2,-10,4,-2,10,-10,5,-3,-10,-10,-8,1,5,7,-3,-5,2,6,7,-8,-7,5,-6,6,-3,-10,3,5,5,3,-1,-3,-8,-7,-8,-1,5,-9,-4,-9,-9,8,-10,3,-2,-3,7,-6,-4,9,9,-9,7,7,2,6,7,-5,-6,-4,7,3,-3,8,-1,-1,6,-7,7,4,-4,-1,6,-9,6,-3,3,6,3,5,-10,6,-8,1,-1,-7,5,5,5,6,-1,6,-2,-10,-8,-1,-3,6,-4,-9,2,-9,3,10,9,-3,2,-4,4,1,1,10,-3,-5,3,-1,9,4,5,4,-10,6,-8,8,6,-4,3,1,10,2,-2,-10,4,-5,-10,5,-7,3,3,5,-5,4,-5,-4,1,-10,-1,-3,6,4,-8,5,-1,-1,4,-4,5,6,5,6,-6,-8,-7,-1,-3,-9,5,-8,-6,3,-5,6,-6,-1,-2,6,1,4,9,3,2,2,-9,6,-7,3,7,-3,4,6,9,4,10,-2,-5,8,8,-7,-2,2,3,3,-9,-4,8,-8,6,1,-2,-2,7,-6,-3,3,7,5,5,1,4,-4,9,-3,4,8,4,-4,-3,-7,-5,-2,-10,-2,6,-6,3,7,1,-5,-4,2,-5,1,9,2,10,4,-10,-4,4,-9,9,-6,-3,-7,6,-7,8,-6,-5,10], dtype = "int32")#candidate|5620|(880,)|const|int32
call_5619 = relay.TupleGetItem(func_1439_call(relay.reshape(const_5620.astype('int32'), [16, 5, 11])), 0)
call_5621 = relay.TupleGetItem(func_1442_call(relay.reshape(const_5620.astype('int32'), [16, 5, 11])), 0)
output = relay.Tuple([call_5617,call_5619,const_5620,])
output2 = relay.Tuple([call_5618,call_5621,const_5620,])
func_5624 = relay.Function([], output)
mod['func_5624'] = func_5624
mod = relay.transform.InferType()(mod)
mutated_mod['func_5624'] = func_5624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5624_call = mutated_mod.get_global_var('func_5624')
call_5625 = func_5624_call()
output = call_5625
func_5626 = relay.Function([], output)
mutated_mod['func_5626'] = func_5626
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2609_call = mod.get_global_var('func_2609')
func_2611_call = mutated_mod.get_global_var('func_2611')
call_5672 = relay.TupleGetItem(func_2609_call(), 0)
call_5673 = relay.TupleGetItem(func_2611_call(), 0)
func_4093_call = mod.get_global_var('func_4093')
func_4095_call = mutated_mod.get_global_var('func_4095')
call_5707 = func_4093_call()
call_5708 = func_4093_call()
func_4775_call = mod.get_global_var('func_4775')
func_4776_call = mutated_mod.get_global_var('func_4776')
call_5712 = relay.TupleGetItem(func_4775_call(), 0)
call_5713 = relay.TupleGetItem(func_4776_call(), 0)
var_5723 = relay.var("var_5723", dtype = "float64", shape = (8, 15, 11))#candidate|5723|(8, 15, 11)|var|float64
bop_5724 = relay.bitwise_and(call_5707.astype('uint32'), relay.reshape(var_5723.astype('uint32'), relay.shape_of(call_5707))) # shape=(8, 15, 11)
bop_5727 = relay.bitwise_and(call_5708.astype('uint32'), relay.reshape(var_5723.astype('uint32'), relay.shape_of(call_5708))) # shape=(8, 15, 11)
func_1499_call = mod.get_global_var('func_1499')
func_1502_call = mutated_mod.get_global_var('func_1502')
const_5737 = relay.const([1.519445,-3.459069,0.823009,-5.459282,7.895170,0.066759,5.798915,5.385093,8.317628,-1.730777,9.792658,2.820027,6.490072,7.450199,-8.456521,9.032400,4.974562,1.355221,-3.510832,-6.058832,1.968621,-6.452556,8.968139,5.599113,6.282871,-3.720936,1.108347,-6.369944,9.552020,5.387392,3.806058,1.994058,-2.187833,6.189293,4.119498,-3.082001,2.546252,5.972211,9.461820,4.704815,3.244993,7.358569,-2.172555,1.450945,-3.081974,0.504238,6.090752,-5.734498,-1.398951,-8.697295,-5.551051,-5.215022,4.669565,-3.740175,-2.113160,2.449283,1.040895,-5.056752,-7.514915,9.157867,4.149524,3.258818,-9.826670,-9.855630,0.091570,-0.036251,-7.508420,-5.332837,-0.753152,-1.088635,-2.686342,-6.355334,-2.096989,9.663182,-5.430628,6.136456,-7.558675,6.621361,4.493439,5.072041,-4.913158,-0.724814,-3.850316,2.429732,8.130981,9.237961,1.043061,-0.695047,-0.352732,6.425529,-3.392836,-3.180313,5.706827,4.737075,-0.860632,5.336771,-0.028497,2.252379,-5.433113,-2.353827,-7.430336,-8.212237,0.974144,0.269744,-6.944395,8.762899,-5.988312,4.835399,4.774862,-2.081458,4.052186,-8.884686,1.520082,-5.102583,-7.937121,4.487441,-1.811525,2.126327,-8.271418,-1.720150,4.080818,-7.576794,3.996932,2.207755,-5.193039,-0.293495,7.224278,-8.304100,-5.074597,1.269369,7.390661,5.349478,-9.818632,0.711559,-2.224310,5.671225,1.756009,3.803213,-3.778703,1.362289,-5.712923,-5.186834,3.908982,-6.289556,-5.642321,-3.133009,-3.403322,2.356581,-4.094518,-3.684859,-3.823559,-1.730288,3.025609,1.109528,-5.701588,-7.179637,-6.019704,8.418192,7.526979,-0.265477,2.932046,5.939995,-6.110470,-1.001505,-3.661613,2.973106,-7.584572,-1.371074,7.548540,6.620912,5.763793,-0.910299,8.067107,3.286217,2.542030,-1.631008,-5.977194,3.819559,-3.658041,-9.507491,-8.818209,-1.421255,1.301432,-3.461831,-1.683927,0.717189,9.383920,9.965560,7.231601,-8.501944,-4.525238,5.559614,-6.042818,-7.211274,-7.372299,9.789542,-7.142587,3.336499,6.631824,7.396485,-3.008937,9.670826,-7.975874,-2.478578,6.671406,0.374430,6.897985,-3.920325,1.924566,-7.355432,0.344990,-7.591057,4.791719,-9.299773,7.294526,-4.593400,-6.995546,1.013656,1.204349,-2.524258,-5.398197,-0.725523,-5.494968,-8.214358,8.535510,8.040615,-8.250404,1.071454,0.795361,-4.674274,7.241876,-5.842875,-8.781319,-1.072972,3.859608,-3.456957,-1.248927,7.612128,-0.812710,-5.313318,6.492826,-6.655232,0.244826,9.401198,3.140852,4.768048,8.834129,-2.835004,-1.414837,2.625748,5.636725,9.148778,-5.000114,-0.024268,-4.626593,3.620473,-5.678136,-9.051605,8.598777,8.155994,4.410464,6.220111,-2.637009,6.043824,-5.438823,3.159154,-2.516111,-7.867134,9.481769,4.811089,2.774963,8.956181,1.907130,-7.354373,-0.715747,5.875239,-4.210688,-8.199998,3.871378,2.456578,-2.499739,1.476332,-8.451507,5.260249,6.147777,1.080207,5.171353,-0.396517,-2.760865,4.971403,-8.648180,3.812700,4.540675,-7.215503,2.867798,4.904252,-9.187046,-4.390802,-3.705914,-3.648317,9.734859,-8.822199,2.581906,1.326282,5.378790,-7.582351,1.099388,0.253542,7.095890,3.507137,1.839907,-2.635193,-3.160785,-3.722448,-3.077120,-6.852416,3.820916,0.648420,0.887804,-1.955518,0.450142,1.611728,-6.409127,-7.996428,-7.271309,-8.340194,-8.185814,2.777964,-2.827571,2.938550,-8.481176,-9.721800,-9.014707,-8.160520,-9.368704,9.012544,2.384411,-9.558453,2.619231,6.829607,3.978270,1.751556,-5.168638,-7.947395,6.624324,-3.769877,7.744652,9.216153,-6.663747,6.428752,-5.918042,-5.790094,9.268723,-0.434505,2.082257,-5.031073,3.255827,-7.781207,-7.679262,-1.718785,-3.440090,-3.242052,9.995354,-4.653406,3.439042,-3.637954,-4.848692,-5.896329,-1.263368,-1.289152,-6.327852,-8.290315,-1.519851,-8.970056,5.458033,-9.850367,1.553160,2.061641,-3.799452,-0.416822,9.321204,-8.202403,2.296856,-3.566505,4.223473,-7.786677,2.124659,6.485631,8.598986,2.317161,6.305835,6.848042,-0.607854,0.471485,-3.090684,-5.300721,7.644056,1.438731,1.703413,-0.788124,-0.459966,0.262384,0.889860,6.655211,-0.003012,9.355401,7.964987,-8.390864,3.453795,-1.248678,9.212480,5.249956,3.434301,7.549048,-8.862257,7.092012,-8.376439,6.988146,-3.799713,1.206935,4.454952,-5.273093,1.305122,-4.332447,-0.110328,-8.335141,9.766544,-0.128458,-9.550824,-0.115565,7.095964,3.352886,-7.648057,9.644142,7.563569,9.288152,7.284991,3.952636,-4.685586,5.170578,9.444321,-8.624898,-3.946770,8.695385,-1.703800,9.192197,-8.782252,-0.022233,5.085455,7.959676,-5.305847,2.536083,-2.051569,-2.864393,-5.093227,4.164614,6.693945,0.360155,2.708256,-5.677867,-5.697849,0.292249,-8.291542,3.031520,-8.889617,-3.431093,5.139927,-1.705687,0.744235,-8.686229,4.164593,2.214478,0.158171,-9.008914,8.548617,-0.467276,-6.781726,-1.999357,7.244155,8.501810,-8.677764,-6.020748,8.623149,0.536526,5.767689,5.561400,-4.524586,5.443889,1.953836,-0.392660,-7.518960,-0.289688,-1.959508,2.348712,-4.656947,4.317088,6.308689,-5.446722,0.087278,9.685998,6.745879,4.809800,2.724785,6.881872,-9.915262,8.401807,-5.363909,7.543543,6.421119,9.719955,4.298953,-8.398480,-5.386463,-4.953259,6.151115,4.364623,-3.461215,-0.387451,5.114759,-9.924068,2.303217,9.739228,4.166378,-9.964006,0.858164,-8.186032,8.750326,4.409215,4.634613,9.571517,2.263173,5.146335,3.930549,4.078350,4.319536,-8.659466,-1.770739,-6.117708,-4.078261,-8.992849,-7.814053,6.844821,2.607854,-6.605563,-3.590062,8.912913,-7.980185,0.249548,-3.951527,-6.579091,-7.364221,-0.674967,-6.211413,-5.147196,-1.951721,5.634469,2.288277,-9.219064,2.557222,7.534171,-3.257796,-9.752195,2.410085,-3.300059,-3.411433,1.851112,4.740749,9.681226,-8.373372,-5.080544,-2.600708,-1.247895,-1.927408,0.264235,8.371623,7.056091,6.036437,-6.110846,1.049892,8.627721,2.130565,-5.477586,-9.861808,7.932903,9.061992,3.039586,8.169807,3.339928,-2.757874,1.093965,8.025238,0.747760,-8.698701,6.341246,-2.136058,-2.191675,8.330972,-0.305180,-7.877099,0.749497,-7.211529,-0.681285,-7.169543,1.067528,-2.454737,-5.808256,-9.831923,-6.198711,3.233055,-0.610704,-4.957939,6.129289,-0.794747,-0.391042,7.566378,-8.037001,-6.300977,0.420815,3.442951,-9.478503,-5.081955,6.366764,-8.631808,0.995375,-0.578482,-8.781237,-5.510039,-1.220876,1.464953,-1.205832,-8.219369,-8.295597,0.272395,5.897009,5.403237,-0.903199,-0.162924,-2.319362,9.053688,-3.927680,7.633678,4.624024,4.716640,-7.967191,-6.025051,3.021757,-6.797966,3.520736,-3.550837,-8.308107,-3.222297,5.372577,-6.198354,-9.647313,1.996202,0.415451,0.780867,8.048076,9.493611,0.327349,-4.192877,-4.358265,4.625603,-9.835943,4.167227,8.436720,2.628858,-3.228209,-1.199434,2.399293,-9.712263,-9.958730,5.107059,-2.055489,-5.565528,-8.957426,-3.415355,8.385853,9.753632,0.836616,-4.095500,-5.330930,2.899415,6.177596,3.340971,-4.668602,-1.855453,7.812712,-9.681702,-2.057423,-4.289917,7.333455,6.718416,-7.295965,-5.705722,3.441396,-8.223763,-8.670394,4.655263,2.962940,-4.985140,-3.940676,-0.881005,0.044301,5.399057,2.246819,-9.441552,-2.558692,1.815347,-5.970358,2.139272,-1.314886,-0.948733,0.352769,1.528151,-9.783182,-6.279920,-8.724698,5.976936,9.164933,3.556405,-6.550547,3.876633,1.421670,2.654299,-5.155063,-2.882337,-9.018198,9.685107,-4.209745,-6.372532,6.968677,4.809962,7.513315,4.569294,2.317437,-3.391750,-2.555660,-8.564134,-3.814016,-6.750284,-7.759357,-7.231759,1.909410,2.576089,-5.437921,-6.060715,-5.829212,5.939161,-7.283553,2.691601,5.456380,6.817940,2.989213,0.363346,2.483618,3.339749,-1.429453,-7.063811,1.616876,1.008082,4.705814,0.985288,1.586322,-8.436190,1.152187,2.270499,8.098476,5.341142,9.815836,-6.932491,-8.316713,-1.820717,2.584955,-6.409114,-6.270918,-3.477552,4.766862,-0.769419,-7.954818,8.011159,-6.800667,-2.472826,3.106600,-9.204085,1.814537,-8.118351,-1.016635,-5.560796,1.839369,0.024929,3.228125,-3.187758,5.702828,8.084364,5.884505,-8.042434,-2.903412,3.731155,-0.778291,-1.925837,-5.432920,6.814023,6.482549,3.914619,-0.759287,2.415303,-8.211500,-8.914490,-2.058401,-7.957740,-3.080048,4.902790,3.551719,6.058559,-2.368696,0.554379,-8.819889,-1.244794,4.187150,-1.315884,-4.128143,8.541194,5.544661,-9.687294,0.683705,3.470957,9.313679,-8.334549,8.545969,-0.800581,8.945048,7.453543,-5.868695,-6.351933,9.928338,5.425087,-5.628441,-4.412553,0.057213,8.095547,3.956476,-7.334483,4.861551,-3.439389,-0.078893,-8.056028,-4.421577,5.546241,4.654734,-0.964407,5.345787,-7.372313,-9.593529,5.715231,-7.754102,8.787817,-4.888354,-3.206811,-4.206692,-5.021474,-0.740562,3.971018,-0.945098,1.423495,-3.695791,-4.362481,-2.171636,3.867963,-9.799792,-6.851728,2.663569,-6.063362,8.105050,7.832720,5.363970,3.892054,-2.773588,6.121869,7.073868,9.083720,-9.290119,5.240924,-5.259528,-4.769602,-6.163657,9.316001,-0.404046,3.928363,1.432699,3.116466,-3.079903,-1.735888,1.534493,-8.641943,-8.971868,-5.828619,0.901555,5.401125,-0.751852,-3.930384,-3.429539,-7.525817,-4.100936,8.544397,-1.732602,-7.867366,8.598792,-7.988767,-5.396046,0.961598,-8.869658,-7.976553,-9.896651,5.204034,9.192796,4.099046,-8.015005,-9.226319,2.557742,-0.827614,-8.716626,-2.958115,0.184574,1.242819,4.764214,-4.342160,-8.381513,-8.323728,2.052373,-8.708466,6.334008,-5.267525,8.541679,-0.665705,-5.634795,5.688353,-0.269711,-5.583201,-9.014631,8.290086,5.839516,7.695230,-4.478620,-4.890056,3.551506,-3.987035,-8.051195,-8.987237,6.497786,-3.295321,9.073193,4.661385,3.931473,1.242622,1.310942,-4.490796,4.558871,-6.087204,2.948085,8.383553,2.703359,7.231272,-1.137340,-6.150461,4.677539,-3.599144,-8.843774,-4.251308,1.925776,5.941113,-0.043200,6.104290,7.912145,-3.290835,-3.602373,5.385073,2.537860,7.850278,6.050690,-3.188242,-1.015654,6.531539,-2.206889,8.998265,-9.631939,-2.218231,-6.174758,-9.854791,8.810782,-8.998108,-4.955447,-9.669548,-6.507539,7.922401,3.528489,-6.544791,-2.658051,-7.044331,0.841683,5.629785,-7.768387,4.418872,3.934794,-4.480454,-7.709992,0.265549,-5.941585,-5.905906,3.282258,-6.929320,9.601989,9.686147,0.734159,-4.160830,7.183938,-4.652889,1.846267,-1.921081,1.398784,-0.939095,0.504217,-9.169457,1.066010,-3.360662,-2.143208,2.388496,-7.494007,-5.348643,-5.363140,-8.317787,-5.397597,9.909116,-3.099107,-4.970077,-1.258472,0.680523,-5.128923,2.829583,7.769093,9.600350,1.984915,2.011583,1.286360,5.848529,4.988708,9.158198,-5.860388,5.078199,-2.175062,-1.576443,-7.078228,-1.938271,6.419824,-5.949850,9.443952,-8.962437,-8.293652,-8.326508,5.085968,8.793831,-6.471953,-6.878149,3.745519,2.270656,-6.029207,-0.884387,-1.688234,0.478636,9.282372,-7.206048,7.423727,6.331897,-9.649513,6.390970,8.859968,-1.892012,3.303568,-8.671132,9.099840,-6.384852,4.389064,-4.536376,3.461327,5.039548,-1.626349,-2.902901,-8.235731,1.294859,6.514765,3.039834,-1.321440,-4.701123,-3.162831,-2.573264,4.569416,6.215705,-1.307183,-6.298823,-2.617344,-3.244141,8.255940,-2.186427,-6.804390,-1.504394,1.085693,-6.522218,-5.335446,0.430260,2.288290,-0.340702,5.142904,6.218722,4.088105,6.435913,4.096317,-9.688534,-3.239167,-7.248576,6.452189,4.207386,-0.079680,-0.775711,-6.240661,-4.041862,6.834933,-8.176738,-5.232969,-3.043306,5.576187,4.532781,1.855170,3.293572,3.794423,-3.945534,2.803552,2.093744,0.734306,-1.287805,1.150305,7.937173,8.254954,1.567822,4.593240,5.096501,-0.018868,0.058822,8.811531,0.043586,3.633636,5.605698,2.762104,-7.291705,-3.435503,1.824822,4.244575,-9.732255,-4.447912,7.717359,-4.864921,5.075200,6.363560,-3.401981,7.589939,1.255202,-2.259517,4.975013,9.827923,-3.730541,-9.694315,-2.679731,3.674548,-8.378297,-6.059421,9.613522,7.853119,8.571244,-6.850080,0.872813,-8.438102,-6.160394,2.052586,-0.934627,8.530802,-3.977849,-3.110354,-9.378318,5.297807,-4.382635,-5.825183,-5.040241,-2.012043,-4.417403,-2.717548,-7.554901,6.082343,8.129319,8.681741,0.833679,-2.718559,-6.595987,-0.879930,-6.905256,-0.091143,-9.459234,1.722096,-4.201799,-9.926669,-2.607845,-8.742643,0.935838,2.717168,-7.702656,0.957593,2.523361,3.010323,-1.369932,-1.529723,2.190998,8.211497,1.132648,8.568042,-3.612368,1.147627,-1.701117,-4.630295,4.828906,-5.812364,-8.001497,4.690951,4.966582,5.658209,2.406509,9.316580,-8.011872,-1.327052,9.775222,6.225837,3.662650,-4.573405,-6.206407,-5.869500,-1.617488,0.629922,-8.240346,-5.125823,8.255163,1.727747,-5.224610,-1.909597,-9.642276,-3.135101,-9.477802,0.356056,-5.404951,2.927823,-9.193981,-5.533999,-0.983031,9.346729,7.372356,-8.574022,-6.567564,3.989476,-3.614820,1.822485,-8.991522,-7.301428,-8.870614,-4.275135,6.250930,4.306675,2.898408,-9.340039,-8.674661,-0.095067,-5.892162,-0.822259,0.119260,7.236428,7.109964,-5.422485,-1.637982,-6.045294,-8.873773,-0.019575,-6.896043,-9.351548,0.942425,6.157424,-1.366112,2.610091,7.260226,1.365087,1.558436,-6.729823,-2.845269,-9.703658,-8.168324,8.725086,-0.191540,-9.998532,5.614701,-5.821102,-1.876877,-6.803757,-3.468367,2.208662,-5.460006,-0.834560,4.874166,-2.502096,1.973564,-6.397398,-4.005565,-0.618642,8.221167,3.951162,9.179761,-9.712055,-3.476705,4.970217,-2.361450,-9.852951,7.625454,2.041893,4.721044,-9.365783,-9.281687,-6.572882,-8.520117,2.201631,-2.416080,6.197160,9.344022,6.321541,-9.299836,-3.331352,7.473315,0.423345,4.610718,7.122224,7.558008,2.401536,-4.505806,-5.685779,-3.720057,4.536766,-4.298540,6.350207,-9.166637,7.264918,0.634934,9.857515,-0.135734,3.297060,1.715168,4.425123,4.844474,8.604737,-8.206231,-3.777947,0.882617,3.012145,-6.041342,2.648510,6.382402,-9.039357,-6.297364,6.470767,-0.243112,-1.413389,5.281169,-9.177895,-6.532733,0.694964,9.133520,-0.140417,5.756652,1.577785,-0.565009,-8.664380,9.267579,-2.482215,-9.409128,5.062992,-1.116056,2.034980,9.078251,-1.823152,4.193231,-8.534072,-2.202010,4.883875,0.258336,5.338902,-8.171529,0.629659,-9.558459,9.315678,-1.877956,-1.433395,6.052223,-8.267358,2.035023,-2.897713,-4.614458,-6.660112,2.092406,-7.288579,-5.338058,-4.814113,5.082591,-6.057102,2.362438,9.360822,-0.424419,3.836001,7.155784,-9.032158,-2.316129,8.259109,-4.883505,6.274614,7.231060,-9.934432,-1.822857,-3.626067,-8.401536,5.261612,9.052580,2.511413,-8.172541,2.742985,7.986430,9.403847,-2.182744,-1.177832,-1.451889,6.736179,-0.619416,3.601366,-9.934019,-7.345592,-0.439097,5.247596,-6.639936,-4.368541,8.915137,-3.155078,5.326285,-0.470663,-0.769072,-4.647117,5.647564,5.322679,0.443921,-0.348091,-2.358225,6.249675,-8.611743,-5.506553,7.470950,-4.525038,-3.184720,8.800916,-3.988429,-9.486055,3.230889,4.826035,-3.094119,-8.691981,4.842673,9.561760,3.909145,-9.099230,7.302889,7.665703,9.681467,3.512826,-5.487000,-2.956471,1.015880,-1.817387,6.463789,8.100198,-1.416301,-4.966154,-1.777957,2.564090,-9.713448,7.777684,3.404530,-8.523044,-7.775279,-7.615396,5.679316,3.896645,5.274371,8.111101,0.418485,-4.739308,-8.427307,0.090908,7.601293,-1.227432,8.185930,8.586889,-4.714393,6.960520,-6.709831,-2.901810,-5.938052,-8.452546,3.003878,0.486765,-8.022595,-6.498620,-0.363091,2.649443,-5.957715,1.801251,6.396054,-8.320866,-0.642680,5.386396,-4.643262,-9.387765,7.892861,-5.337532,-2.401847,-2.723801,-8.885223,0.647641,-3.952085,-1.358673,3.786961,-4.927607,-7.905979,-3.348696,1.869807,8.910606,7.886817,-4.057162,-3.023577,7.364924,-4.556897,3.731253,-1.057981,7.202022,6.531562,-4.952399,6.858689,-3.579407,3.543211,2.529843,-2.706292,-9.772272,-0.854777,-8.886954,-2.584961,-6.854150,3.570400,7.146185,-1.036676,1.053698,-8.112599,-7.714620,-9.381625,5.816851,-6.910146,-6.320417,-0.326985,-9.106089,-5.608286,5.345311,2.714057,5.647580,-4.869165,-0.089873,-7.964100,-1.669681,7.034961,-1.405409,0.265746,-1.201525,-3.948023,-5.775696,9.345759,-9.934589,-7.863324,-3.674021,6.908570,-0.185534,-2.636856,-4.166862,-0.354612,0.975589,-1.947182,-6.963307,-8.558453,9.867749,3.052840,4.870184,-0.824956,-2.191465,9.227466,-7.599515,0.849743,-7.422463,-4.567548,-7.785941,-3.557153,-8.012251,5.885350,-1.508526,2.189202,9.564380,-5.863898,-4.935489,-6.446188,5.972048,1.736202,-9.066888,-9.249922,5.398192,5.082399,-5.202702,8.195290,-8.156654,9.891020,-5.444913,-4.170423,3.287496,-3.363543,-5.471897,7.457744,3.123846,2.008467,6.334688,-0.949478,-1.368506,-0.422874,8.318022,-6.354215,-8.514056,4.761642,-6.247745,-7.631574,-2.051700,4.072796,8.175393,-3.411400,-5.407697,-9.653630,9.599399,-5.196087,8.210398,-7.088003,-6.141442,-5.982799,-8.945295,-2.224663,-5.430188,7.893050,7.401612,4.396054,4.562818,6.847989,9.065052,5.445245,6.493472,7.477074,-6.460907,2.756378,-9.586723,6.166867,2.126595,5.777033,5.526856,-7.078910,-1.489240,5.342457,1.965667,3.434822,2.769378,-7.226493,-4.737378,3.799584,1.053886,5.323600,-1.854784,7.942985,-8.588008,6.869995,6.236605,4.280554,2.323825,8.268018,5.655570,-7.948861,7.898077,8.226381,-1.095869,-3.491434,-2.647490,3.499100,-6.293793,-6.422094,0.228309,-6.886228,-5.713742,-6.083482,5.821649,-9.443649,-1.103135,5.189305,5.019834,3.332184,6.287710,-2.643332,-9.976297,-3.302068,-0.494042,4.608096,5.339201,-0.197110,3.356292,6.184118,-3.702027,-0.126846,-6.489340,-9.224675,-3.003516,4.739250,2.117390,4.013657,7.710112,-5.286742,4.980837,-3.645264,-6.801951,-3.814377,3.459388,-7.616263,8.220478,4.278871,-0.472003,-5.487505,9.925110,-9.826938,3.243995,-0.831852,6.781312,-8.130355,6.584045,7.477766,1.655960,7.836433,-1.662406,-5.614766,-9.159737,1.595349,8.116476,-7.587939,-1.278708,0.597630,-5.202005,-2.644612,-8.915672,-4.116093,3.581663,0.240600,3.200174,-0.564851,-1.473572,-3.705965,-9.641742,7.357517,8.745047,-6.855114,-2.762311,3.366892,-4.857202,9.404124,-6.286890,-7.762692,3.675664,-5.388052,-0.080165,-3.692134,4.568227,-9.228920,3.628117,5.474946,7.921271,-6.818550,1.486275,-4.179121,3.973358,-6.257830,-9.763562,-3.748841,5.188941,-4.466298,3.005063,-5.239466,7.325970,-1.080856,5.542714,5.675175,9.055636,-5.815757,5.513719,-4.341732,-3.710497,-8.608930,9.512783,7.955846,9.488064,8.004619,-6.076924,1.455679,-2.545265,-1.906298,2.545239,-8.504053,1.501571,5.130001,3.323708,-0.406580,3.581559,-9.577957,7.531264,7.258048,-4.627916,0.695835,-7.539987,-3.924056,-9.773881,-0.628368,6.724771,-6.437896,-0.746309,3.628835,-0.457249,6.042630,7.673865,-4.445290,4.871272,4.196955,-7.421480,9.272767,-4.126573,7.170077,-6.888584,-8.349894,-6.050811,5.311707,2.147134,1.902371,-9.226603,8.158088,-8.856781,-5.227665,4.078103,0.232960,-6.069576,-0.741221,6.386794,1.601362,-2.350025,9.340226,-8.827601,3.608707,5.902982,3.780021,5.020258,6.334318,9.299648,-9.991686,-4.034456,-2.861819,-0.173177,9.346299,9.088113,2.196835,-9.549510,-3.623227,4.722928,-9.385934,-2.073733,-6.158506,-3.900949,-2.939064,6.937089,-5.007502,-3.029729,-1.024804,-7.943327,-0.985570,-5.576995,7.631836,-7.695204,-4.011018,5.554287,2.493328,-5.760797,5.993958,2.553836,-1.954988,-0.128438,-8.155062,-7.755642,1.576809,-1.778166,-5.866199,-2.569176,-6.885565,9.527659,-4.358146,2.967560,4.598516,-2.577165,2.895607,-8.737538,-8.215314,-1.032964,0.532019,-2.156733,0.246874,8.328870,5.570533,7.126804,-5.898982,-7.512473,2.684776,-5.599714,-8.088342,-5.764994,1.261919,9.731084,6.385783,-9.307513,-0.979401,-5.810712,-3.106380,2.797137,6.341089,1.260861,-1.774740,-1.435214,6.264475,-4.099751,7.362460,0.233541,3.102806,6.091719,4.572340,5.196765,-4.165710,3.541117,7.152503,-0.348610,-2.795820,7.386227,-1.146393,-0.245862,-4.730564,3.021828,9.348251,-5.238308,8.481310,-9.182478,-8.957685,9.362851,0.055848,1.072826,5.738778,9.898716,4.828542,-7.866283,-1.087234,5.107007,1.182583,8.905670,-0.902230,9.381015,1.691890,-9.999579,-8.242056,-2.856507,-8.234959,-1.407673,6.239026,9.099020,-7.905416,-6.497938,6.751725,-0.626275,-3.184955,7.307946,2.866284,2.692954,-8.977071,-5.850417,3.231377,-3.808835,-3.580087,5.920973,-1.364187,-1.647095,2.068839,-0.767318,5.429616,3.023811,-7.919100,-1.065892,-8.846112,-8.659782,7.008527,1.840289,2.006386,-6.580903,-5.629343,7.580628,3.768636,-6.152137,0.794931,9.364646,9.473199,-9.272897,7.409434,1.264521,-7.492761,3.657353,9.674520,-1.788915,-7.033569,-7.147244,4.577907,-1.217885,-1.240464,7.325618,8.957128,-6.723893,5.984198,-5.517475,9.332025,-5.419843,4.331016,7.547389,-6.132681,3.847627,-0.005908,-1.033430,4.598011,-1.560021,8.212848,7.044068,-3.408811,8.259184,3.891397,9.944222,9.727159,-1.944724,9.899298,9.037346,-0.331960,-7.132463,7.506135,-5.483925,4.050277,-5.981749,-7.361541,1.308647,9.295062,-5.207022,-7.086796,1.768690,-5.269391,-2.592022,6.840859,2.057561,-8.428155,-2.742887,-4.999890,2.219093,-0.110721,-7.775243,2.482408,4.711405,-3.346171,6.673422,6.360449,7.657708,9.274718,2.241449,1.725180,-7.073273,7.821464,0.077766,9.355071,6.910153,-0.737974,-4.277603,-6.207379,-2.347339,9.829419,0.123784,-9.586249,-6.114762,0.244805,-1.798565,4.872710,-8.154265,-8.526118,-8.763004,-2.156307,1.709674,-7.659496,7.269325,0.869110,5.983100,7.273685,-0.537824,3.828792,3.452590,-7.703477,-8.994509,-0.568419,-0.904815,-9.738311,-0.550004,3.233649,-7.563231,1.796148,-3.945081,1.650342,-8.004927,-3.318794,1.858527,6.276564,-4.770148,-2.166975,6.768693,-7.658980,5.969063,6.672896,5.360844,8.621290,-1.548133,6.495675,-5.435457,-4.111286,-8.957964,3.239851,4.140382,-0.604537,-5.644146,-2.184330,-9.278462,-5.399924,7.699433,2.336984,-5.990971,-2.643925,-2.063212,5.417021,1.610047,9.402062,-3.008200,9.665309,9.163474,-1.878207,-2.784260,-5.806048,8.346568,1.562493,-1.119340,3.725721,5.280049,1.643355,-8.425187,-7.107261,-2.518628,5.804094,-1.739858,-4.088236,-5.050980,-2.706740,2.864134,4.547076,9.970929,-4.243177,-8.738179,-9.880023,5.010045,0.578500,-4.785942,1.732478,2.551918,5.562435,8.519496,5.461923,-7.733721,0.129609,-5.012429,-6.412770,1.880515,9.324412,4.283134,8.198051,8.308658,-4.462128,4.486195,6.276413,-8.872962,-1.437754,-5.730006,5.890888,0.990023,9.034446,-7.013766,2.760921,-9.900554,4.975789,-0.768961,-1.630334,4.262106,0.223693,4.175483,1.401528,-5.504481,1.852065,5.887028,2.012553,0.906277,6.237661,9.278822,5.803440,9.669898,5.030292,-1.819584,-6.675819,-4.931067,-2.809699,-6.475812,9.654223,0.162231,5.495534,8.803525,-1.650962,0.964907,-8.068755,-7.300257,-1.824692,-4.505717,-6.215191,-0.178166,-3.798857,-2.858911,-2.188188,-8.610707,8.502872,-4.320842,6.518646,-6.751807,2.621993,6.916168,-9.626278,4.151524,3.677871,-9.469465,-9.506628,-1.002035,6.145438,2.077634,1.853343,8.542039,-1.456889,-0.591112,6.535782,0.627627,-3.456319,5.270242,-4.149620,-5.063961,-4.427884,4.484417,9.428089,-8.939824,5.848727,-3.728767,9.127948,2.146875,6.831153,0.682157,-5.562646,5.172165,4.967681,1.226998,-8.560986,-1.455753,-1.740060,2.922656,9.564274,-0.115378,-6.726630,-5.384565,-7.506431,0.554162,4.516454,2.819768,7.215964,-0.435441,4.592666,-3.885594,2.685757,-8.911212,1.223654,2.203527,8.319955,1.736043,-7.911197,-8.737473,5.223814,1.049655,-7.073109,1.894617,3.684044,1.965532,6.927735,-7.056121,-5.836427,4.887313,1.443092,-4.830452,-7.662562,-7.261479,8.874451,-1.670835,-3.279477,1.387289,-9.340692,-4.611319,8.266838,-2.797683,7.579535,9.147580,9.303957,9.968361,-2.397485,-8.487992,5.567876,8.853690,9.106460,-4.078139,9.084793,-2.941139,-7.913291,-0.625864,-2.021392,-6.260121,0.088388,7.351356,-8.191466,4.254437,3.062578,-4.416321,-0.519069,8.849561,6.999998,7.902054,-5.783511,-1.249905,-9.563406,-7.055440,7.114835,6.962066,-3.160875,5.956171,8.694126,2.865941,-9.706485,-4.894901,-4.117649,-8.295840,0.472042,-5.031620,-2.615392,-5.122204,7.039663,0.731511,0.013498,-7.169103,-1.692011,7.008694,-1.977310,-6.621307,-6.749134,-9.689956,-3.860275,-6.625939,-4.249692,9.014979,1.155180,-6.906961,-1.421426,8.538733,-1.723614,-4.713013,2.631390,-2.440985,-5.704031,8.316544,5.768261,2.756496,-3.772593,5.897818,3.276598,4.846607,-9.708106,2.419444,-0.060851,1.073401,-1.131486,1.079766,1.251615,-5.646588,-2.710469,-4.378024,8.754095,9.103641,1.517590,-9.212085,-0.802593,3.079735,6.862704,3.057555,8.745486,-5.737289,-2.346665,0.680395,-7.169631,-5.599572,1.134166,-5.818931,-5.095424,0.526058,1.147022,-3.082231,8.113724,-4.963497,4.756544,-2.914782,-3.267416,-3.288890,-8.390555,-3.387742,4.505020,1.851722,1.779414,0.951548,-2.220070,3.053185,1.832474,3.512797,8.849793,4.052858,3.439513,0.494592,6.115246,1.836078,-6.756113,-4.442617,-9.179060,-2.453496,7.981368,0.435930,-1.709598,6.949852,5.841101,1.207728,9.502126,9.308186,-9.757493,-8.780788,-8.426417,-1.724077,-6.438328,5.976134,-7.759816,-7.696451,0.297043,6.650457,9.252698,8.223982,9.449564,1.851060,-2.126292,-1.178752,-1.286293,-5.219550,-0.623060,4.879555,7.981458,5.296289,-2.089738,0.275734,3.823713,-1.410402,-9.638007,8.144717,-3.258791,-6.028108,1.491843,0.413633,4.174439,3.678994,-7.029945,-1.597588,8.992529,-1.245738,-8.235150,0.117831,-9.436720,-7.620433,-1.033020,3.281822,-7.773818,7.983719,-1.626211,6.812360,-8.551986,1.163451,8.529088,-0.130512,2.700335,6.276689,-8.142626,3.011459,-5.422805,2.042720,-8.880058,0.647035,-8.167985,-5.560655,0.075451,3.029333,-4.041530,4.610711,-9.781335,-5.946262,-1.790248,6.246395,5.197446,5.049417,-3.986851,-7.085545,7.814031,-8.800720,-3.430172,-9.852396,-6.381093,0.812255,-2.250838,0.897319,-0.994910,-0.552342,5.469793,6.618627,3.365706,-8.439704,-5.525405,-3.506496,-1.233697,1.183894,6.396994,-1.285315,4.317532,1.519400,-5.421155,9.080696,-3.972090,6.703945,6.255326,-8.529891,-0.679523,6.479864,3.685030,-8.441486,-8.390231,-0.801530,-3.557660,0.527109,-3.579465,4.612219,8.091412,7.385628,2.916166,0.390684,-5.499225,0.793247,-8.527416,0.029950,-3.772337,7.573079,6.525878,-5.284433,1.486137,-6.785714,-0.279427,-0.538757,-9.930139,-5.866412,6.494756,-2.557535,5.022439,-9.511048,-6.503759,-8.692885,0.920776,3.768378,0.847400,-6.078746,-5.122622,9.349818,7.375397,-3.150962,1.732101,2.141802,3.452650,-3.868093,5.656862,-6.187198,-4.111021,-0.449947,4.172482,6.667283,4.781492,0.837868,-4.882702,4.528572,-5.238407,8.275714,-3.436020,-8.376656,-1.323891,-8.295622,0.381858,-7.323812,9.304815,-5.018877,-2.384014,-3.994004,4.218778,6.223020,-7.813039,5.233765,6.407170,-2.093461,8.778392,6.733034,-4.153905,1.385297,-9.298192,0.114943,-5.246005,-0.467941,0.711605,2.253211,-6.023937,-0.716736,0.245714,-7.288126,-0.529883,-8.140759,1.284725,-0.583164,5.684558,-5.020627,8.357269,-4.581198,9.911795,-0.700978,2.422019,2.977673,0.084878,-3.512645,-9.225391,7.291770,1.681423,-7.093756,7.988803,-6.542679,2.055650,-5.414675,5.559404,-3.302753,-3.041828,4.416847,-5.344041,0.797175,9.539490,-8.195576,-5.620763,-7.826909,2.920103,1.700743,4.984183,-0.375863,-8.377031,5.272502,8.230846,-3.946319,0.129184,9.374490,-6.860761,0.345794,-6.723292,5.127859,7.193374,-9.694400,5.890150,5.738247,-5.211754,3.663469,-4.515134,-4.206974,-4.715874,2.851627,-4.004426,-4.761622,-2.491448,-3.983738,5.864907,5.131052,-9.343920,-8.388929,5.855051,-8.978339,1.197570,-6.596247,3.866666,8.986602,9.364334,0.497312,0.427815,9.980882,0.938011,-2.548444,5.854016,2.013466,4.346893,6.299415,1.362795,-7.504157,7.552612,-1.277842,2.313829,3.227698,0.620779,4.820313,-5.270419,-5.367064,-3.787498,-6.941512,-7.912051,4.235053,3.667049,3.125135,6.219204,7.544709,-1.781925,7.591529,7.409623,2.091937,2.393746,1.192495,8.665403,1.942657,-9.499709,8.337896,2.456446,6.970513,-1.045986,6.109614,-9.352516,-1.814636,-0.711580,0.103114,-2.727705,-4.783908,9.861829,4.293481,5.658009,-1.879117,8.898762,1.028230,9.988206,4.271086,9.600881,1.167201,-0.723824,-3.186965,2.550635,-2.211031,-8.313392,6.529873,1.868777,-9.225951,4.957110,-1.299956,4.130071,7.495631,-4.672171,-3.782472,8.013366,-6.668360,7.634342,-5.473600,-8.788576,6.783863,-8.886844,-7.874966,0.862623,-7.339376,3.534192,3.733742,-9.172381,6.413510,-0.789250,-7.118504,4.969012,2.673799,-7.477173,9.669819,-9.729573,4.599372,2.747145,-8.347934,8.271751,3.132092,-0.648653,7.748764,2.508156,7.077704,-2.197333,2.392727,-5.295737,-9.136341,8.802420,8.247517,-2.104588,-0.675338,-1.462893,0.359540,8.769202,7.618682,0.603415,8.686638,7.206355,-7.245618,-5.016662,-2.370297,-7.410741,7.586049,-0.018767,-2.789943,-7.692476,4.744850,5.060899,-9.335239,2.470154,-3.379429,-2.338995,-2.153967,0.232473,3.004435,-3.192719,-7.878389,-6.787258,-5.837120,0.731245,-7.445957,5.117608,-3.159533,-4.578725,-4.146086,-6.788580,-8.340792,-8.582654,0.107733,-5.856144,5.032983,-2.487487,6.074491,-7.920982,8.760097,-4.491186,1.574116,4.429699,9.017485,-8.332502,-9.083370,-6.568023,8.477245,5.965445,-4.355010,3.807251,-1.150703,-0.706284,-4.131073,-4.112301,-1.456297,2.418005,-6.645456,0.730987,-3.216726,1.777985,7.871810,-2.451576,-2.165880,2.293553,7.821068,3.521563,-4.270383,5.236339,-2.572736,-6.966833,6.306973,-6.383948,8.831086,6.249002,9.992111,-0.721911,-8.936970,7.854704,-7.062977,-5.291702,3.064386,4.849477,5.428242,-2.370398,-9.910347,-4.472440,4.618596,-3.454515,-9.944521,-4.224229,-9.547747,-1.490155,8.369087,-4.851252,-4.974484,8.669998,-5.042539,9.441015,-6.614113,6.442527,2.798065,-5.422244,-5.460593,1.960652,-1.861482,-7.922087,-6.332372,8.715530,-2.495005,2.226252,-7.537055,-2.554659,0.195594,-6.049792,0.571669,8.795386,7.123180,1.869253,-0.791101,9.244823,6.630432,6.707476,-9.117287,2.999599,-6.155478,-8.864766,-6.402422,8.816354,-7.562159,1.526106,3.601511,-9.766971,-9.363096,-1.260916,-7.702411,5.503828,7.597044,6.865996,1.289551,-1.649736,7.953714,0.845839,2.871884,-7.709470,-8.379301,-4.721829,-9.268602,7.136651,-7.027225,7.326244,6.079116,-5.277686,3.622312,-1.051221,0.894356,3.807568,7.059817,-1.907134,8.422907,3.138753,-7.438854,-1.032914,-8.723089,2.631174,4.275136,-5.868794,9.384095,-2.053349,-3.746350,2.996222,9.746209,5.156678,7.897302,-8.959069,-2.513545,4.424839,3.590102,4.177946,6.420236,-4.700879,8.714587,9.848466,-1.604002,5.146743,-6.831801,-8.366537,1.318382,6.199443,9.533384,-7.174737,9.849702,-4.689633,9.388638,-9.400674,-7.742274,6.053600,5.482763,-5.016017,-0.716425,1.978103,-3.051191,1.563770,0.940833,7.694439,-8.549333,-5.254433,1.738074,-7.858949,-0.316211,3.753515,1.479993,-3.872493,1.002569,-8.183109,-3.926417,-9.496126,2.854555,9.632567,-4.715760,0.457017,-0.138517,-0.229897,-9.393697,-0.070505,-2.040280,5.598764,-0.558403,-2.875762,-6.809107,-1.921607,-5.914746,-9.971903,-6.508754,-3.652382,-7.342038,5.753725,9.531145,-3.398615,-8.401373,-2.569254,-1.242009,-5.420119,4.381654,-3.460970,-0.750852,1.443696,2.135220,-1.554570,1.603646,4.587227,0.350081,-2.181461,-3.911716,-0.665362,9.492607,2.743185,6.682848,-9.728744,6.466077,-2.711650,2.662191,-5.558239,0.495898,-5.160154,-5.199269,-5.373785,-9.891842,-7.391657,2.766774,1.585384,-7.645313,-9.549916,6.591340,-0.351217,6.709527,-0.118364,-3.048909,-2.444111,4.429181,-7.292703,-0.093685,5.692617,6.826965,5.609051,0.934007,7.270703,-7.951675,1.887633,8.201621,-9.068809,-4.982019,7.122269,2.724351,8.146514,8.053468,-1.274719,-1.592512,-1.937728,-2.486041,9.485044,9.979829,8.141558,-0.799688,6.779992,-7.743353,2.674403,-5.166803,-3.334351,-0.735016,-4.651076,9.427463,7.714067,6.289647,-3.426985,7.174745,7.778259,-9.905362,-3.106365,7.954835,-7.127967,2.113604,-9.308552,3.050728,-4.016302,-2.867966,6.253574,5.573249,-3.942989,-4.263674,-7.140417,-9.518601,-3.772264,-9.903806,8.423755,-6.685962,-2.396868,0.103037,8.207297,0.539873,-6.946850,9.477288,3.050828,-2.452502,9.102121,-5.862315,6.604545,1.265939,-9.040279,-1.150861,9.561984,8.218035,1.040441,-2.917544,2.022390,-4.876210,-5.084798,4.872744,-1.560736,1.879369,7.602917,-8.921275,-0.880837,-5.427895,7.353940,-6.056438,-0.742339,-8.336232,7.491987,-4.775565,-9.541158,-8.530456,-5.877538,5.842575,-0.788759,-0.937459,-5.580257,-4.747761,-4.471319,5.499574,1.671912,-7.408937,-2.878179,8.657397,-9.393884,-7.558515,-3.899729,1.396712,1.280719,-5.234119,2.606885,4.750337,8.139419,-5.522578,-3.602973,7.535223,6.037645,3.928173,4.476679,8.759741,3.486467,-2.006169,4.581599,-0.496722,-4.797861,-6.241751,-6.675021,-8.955895,2.273539,0.847420,-1.221027,5.751245,1.546786,7.943623,-6.108302,-0.482545,4.720014,7.676000,-4.999019,8.333110,-0.586699,-2.591142,2.963389,-3.886046,3.195265,-3.076488,8.516023,6.672510,4.439018,7.683530,-8.277610,5.559495,-3.768122,-7.821115,-9.340122,-6.252296,2.537625,5.349441,2.440438,3.167483,-9.302487,-8.016578,9.751702,-7.098569,1.342681,-7.017881,0.234601,9.814095,9.158027,-0.412854,9.604189,-4.054580,1.992225,6.621749,-4.583087,4.724460,-2.424187,-6.470592,8.735083,-3.441226,-8.476345,-1.881526,-4.856365,7.881527,6.548682,-4.932433,-5.532399,8.108893,-5.647506,-0.066435,8.240385,2.298448,-0.627850,-8.137457,-8.275173,-1.670696,8.484989,-5.260963,-5.147644,6.160550,2.021670,-9.061674,5.385933,3.368491,-6.903148,-0.710519,1.191369,8.553754,9.764206,-6.560907,0.402234,-2.965787,0.190531,-0.362060,-0.561044,-4.852199,4.524652,-0.387646,-2.547825,9.517803,5.599010,1.989966,1.883875,-9.711225,-7.555220,2.056008,6.111470,-8.364708,-4.629197,-0.883087,9.338414,7.877010,7.868855,1.820098,5.607679,-4.647528,-0.546581,-2.446519,0.831027,-9.334513,6.176961,7.330851,0.920722,3.810530,-0.484126,-5.689964,-9.829177,7.149440,0.086031,-2.449546,6.251979,-9.080646,-4.067077,5.710216,5.930504,7.227666,0.714776,-7.555907,-6.883098,9.321245,3.958784,-8.212567,7.101740,-0.315812,-5.745555,9.744845,3.009091,2.220901,-6.683440,3.976812,-8.333611,-0.427890,3.711359,-2.657157,2.420254,3.891422,-5.538528,-9.741534,0.996001,-4.093191,6.779624,5.093843,3.566763,-3.619873,3.955993,-3.044239,-4.288440,-5.867735,9.005898,-9.688633,-8.524460,7.243751,5.414747,-5.663271,-8.518654,5.859297,-5.760041,4.696096,1.728354,-0.425055,2.540298,0.657569,6.071489,-5.482445,-9.069544,3.765807,-1.037420,6.583424,6.003984,-3.870558,8.098945,1.003361,-8.177006,5.204451,5.217822,-3.487233,-2.904154,-5.824384,6.343606,-9.696976,9.409843,-4.148246,6.156032,-3.415129,7.677672,-6.239057,-8.388368,7.322247,-2.032360,-3.724546,-6.793748,1.376776,-8.633918,-1.300960,-8.368789,-4.266482,6.523475,0.869364,-1.603552,0.799199,-9.447987,-7.354209,2.530582,2.827927,6.849714,4.607703,-2.513537,-1.008237,8.779748,9.095945,-4.927128,9.550419,-9.119464,-2.996695,-3.892786,7.603547,4.540323,8.114701,7.265913,0.506266,8.899419,-4.897104,0.361336,-0.941685,3.838741,-9.315560,6.103816,8.668785,-7.093655,2.213932,5.559569,4.912248,-6.920412,-8.601052,6.321547,-9.804013,-0.978724,-1.259834,-4.644428,-1.101608,-9.017589,1.378017,7.348656,-6.823191,-2.347476,-1.889152,-7.994845,-4.096990,6.851224,-6.848147,-3.618430,1.671369,0.912500,-8.611567,-8.767709,1.803265,8.692213,8.601937,-7.667649,-8.780703,8.884849,-0.098293,-0.315103,-4.351853,5.838343,-0.736526,-2.291038,9.323797,-7.927114,3.447009,-9.014959,4.989986,5.450620,-8.052503,-2.598415,-3.934949,-9.239500,3.240007,0.302157,-4.818620,-3.115403,6.187901,-0.375732,-2.489726,-4.896890,0.249163,9.058136,6.566296,8.415460,-7.226729,-1.463329,4.997892,5.825159,-3.566432,0.614385,-7.525384,5.192715,-4.348553,-7.110931,-3.135478,-8.394977,4.586711,5.723302,-4.466000,0.704164,-0.266756,6.555936,-8.603653,4.722796,8.860853,2.923440,-3.884477,8.759210,-5.708689,-2.623182,6.681454,-7.111249,-1.003288,4.779141,5.397974,9.795753,-2.096721,6.093932,6.902795,5.605769,0.994401,-7.517186,-7.752935,-8.065905,5.909153,1.151284,2.355311,-1.585259,3.499695,-2.439089,-1.332890,9.034789,-4.449126,5.717461,5.325752,1.617793,2.100891,-4.327674,5.257499,-9.983077,2.679534,1.795666,8.182076,-0.771024,4.613866,9.797946,-0.381993,2.011672,-3.578540,9.756324,2.253088,-8.413761,-4.500078,-5.309841,-2.537085,2.630029,7.089795,-8.439088,-9.400773,7.754377,-6.732776,6.196940,2.322370,0.949825,4.034809,7.486805,5.568667,8.849085,8.840406,-6.115066,-0.303474,7.104742,-7.653221,-4.374865,3.246366,9.842249,2.368877,-0.500437,7.235039,-0.398644,-5.347580,7.036480,5.353656,-6.693721,7.032115,-1.348720,-4.132125,2.185482,-1.715315,7.693117,6.595512,2.440404,3.967846,-9.902402,9.078463,6.387323,-3.111767,-2.134269,0.897450,-4.584492,8.837199,-2.213523,9.262622,-6.540243,9.729474,9.715281,-5.931514,7.951861,-7.164518,-1.545408,-5.905492,-8.332870,6.300809,7.929321,8.380781,9.522353,-7.947719,-9.718206,4.430908,1.595888,-1.041680,8.823928,4.322615,-3.634041,-0.419532,-6.070929,-4.040054,-0.404181,9.013335,-9.734514,0.921195,7.162854,9.579416,3.916797,-7.267740,2.133462,9.888374,-0.947463,-0.063462,5.008740,7.292841,0.102798,-3.824869,3.307528,6.609369,-7.367709,9.030968,3.605789,3.547651,1.903847,3.025395,-0.706106,-2.579331,-0.470021,3.874029,9.651854,5.660636,-0.226269,-5.464968,7.293582,1.255323,5.439506,7.912136,7.054875,8.627371,-2.246332,3.230773,-2.055469,4.613313,-0.001138,-1.902086,-4.532687,7.655224,5.081991,-5.905023,6.971998,-8.774364,0.862328,0.341037,-7.820214,5.159594,-2.030150,3.936564,-9.077906,1.766814,0.627144,3.723008,2.624590,-0.554028,-2.301584,7.970120,-2.451119,-3.279237,5.533508,-7.859815,4.133654,-0.038857,-2.289665,-8.555412,3.406477,-1.520740,4.177642,-7.181641,-7.011919,0.232532,2.986243,-1.163362,-6.989467,1.023576,5.688627,4.318066,-2.500270,-5.743984,9.559379,2.494299,-9.774222,7.805535,4.739204,-4.390420,-3.828079,6.012163,-3.146495,2.817998,-5.692011,-3.312156,-6.698139,-3.425543,6.876575,8.219125,9.973298,0.612097,-3.927783,7.910714,-7.318316,8.398966,7.863944,0.420093,0.359660,-9.828941,4.949527,8.029207,-0.666986,-1.181488,-2.582559,-4.057525,7.878320,7.399308,-2.725123,7.872385,-7.368158,8.214719,3.707543,1.253327,4.767131,9.987278,-5.308443,-0.048607,-1.900767,-4.539698,7.301203,3.457060,9.445788,-5.199143,9.596890,-5.244819,0.535915,-2.480083,-0.518161,5.659800,2.205346,1.132632,5.519788,9.957614,-6.853506,-9.296249,-9.762630,-0.422413,-3.429754,-8.663333,7.597574,8.756851,-1.974751,6.057158,3.603610,8.842700,7.555318,-1.616816,-7.705273,7.592946,5.635271,-0.948722,5.604591,7.828244,-1.756572,2.798779,6.909785,-1.598916,-6.763222,-9.907959,-1.007175,1.758182,-2.094601,-0.024676,7.485373,-8.427424,6.901066,-4.133937,1.691753,-3.503906,7.962466,5.956123,-8.154757,9.192962,-2.999469,-3.124971,9.335084,-7.614596,8.328296,-2.502323,-9.882672,7.834991,-9.148068,-8.324694,-8.152567,9.854901,3.827500,-8.768348,-0.057308,-0.404359,3.439564,9.736072,-6.279044,6.927260,-7.185202,-9.437804,-2.166567,-4.297253,-3.554886,-1.072793,1.420358,-6.989399,4.368538,-5.815731,-2.028031,-3.277700,2.173798,-3.455377,8.989506,3.429680,-5.831975,4.836828,9.049054,2.386111,-4.320158,-4.371354,5.247914,-4.835879,0.315339,-1.977046,-0.459675,-0.663678,-0.496743,0.500860,-5.412657,9.752703,1.918027,5.351873,-1.945200,-8.197333,-8.468624,-6.416891,1.844012,-1.331508,0.410368,4.596078,8.675084,3.198228,-9.629917,-4.013260,2.763375,0.963226,-6.712010,4.467120,5.757533,1.786034,9.849737,8.055534,2.125315,9.666964,-5.352904,-4.072787,-7.492613,0.468732,-2.452637,2.755369,0.973990,-6.414762,9.442615,-5.002494,5.898138,1.782112,1.628720,-9.223790,-4.105263,1.088431,-4.180150,6.202003,2.279994,3.640258,-0.689152,1.523187,-1.640813,4.825190,-0.115195,-9.353040,8.658124,-7.184533,1.340464,7.628137,-3.834701,-7.473173,-5.188993,-0.845360,0.557063,-3.771343,-0.660961,6.508098,8.082063,3.331905,8.035357,-9.333131,3.904910,9.583121,7.724898,-0.264339,-3.718639,-4.533805,-3.430022,-8.163959,-6.401555,5.083988,4.172256,4.637441,9.150553,-2.016213,9.669009,-1.370374,7.203195,8.005924,-3.959487,-8.207835,-3.466845,-5.756044,7.189685,-0.571546,1.032984,5.696300,0.158269,6.581026,7.615410,2.624943,-2.494709,9.054025,0.877746,-0.675002,-1.904200,-3.577951,8.643815,-1.879143,-3.552981,5.930254,-9.087683,-1.548543,6.279653,1.534543,9.066110,6.036075,-9.311573,9.702225,1.875947,4.455717,-0.208844,7.153692,-3.366794,0.713193,-6.546208,-2.751609,1.919973,-2.474256,8.339569,3.897520,-5.636970,-5.891604,2.120057,9.093274,-4.028676,-7.820732,-8.484588,-8.637133,5.958712,8.108453,-5.703717,2.500904,-0.932016,3.040205,6.318296,-0.083369,0.423845,-2.343968,-1.148898,-1.445812,-6.208688,-0.891224,-9.516496,-1.948277,-7.735414,8.657099,6.012471,-2.914112,8.520729,4.767213,-8.054211,-5.934271,4.431462,-8.417406,-9.668789,-2.531338,2.821435,-9.152452,4.147790,-0.853296,-9.608175,8.679586,-4.448812,-3.854808,0.832145,-0.201106,9.236761,9.811438,3.848811,8.508971,-8.119599,-5.436626,-5.922548,9.087794,7.115823,9.132851,-8.666085,-5.405340,-4.187591,-9.568114,-1.143242,9.239644,8.387086,-1.008543,-3.004022,8.495428,9.930288,-0.829947,-2.655078,-6.959369,9.200588,6.668198,-0.525674,-6.775514,-7.709582,-0.068475,2.262563,6.670624,-0.038473,2.849180,8.149985,-8.273797,6.161043,-4.586634,-4.176215,3.181091,-3.337824,1.699167,-8.352909,5.014620,-8.494346,-1.899119,6.899464,5.060574,0.786208,-6.421192,5.194882,-6.753704,6.472300,-4.458648,4.193032,-8.407070,-2.797847,-7.538048,5.194965,-8.314907,9.923075,-9.332143,-1.751346,-9.330336,-5.929831,-4.421631,4.703509,-9.727287,4.635628,1.701994,8.015490,-1.451079,8.426455,-9.077385,-6.061644,2.534402,9.146093,-4.501161,4.115375,-4.416796,4.543199,9.729418,1.374953,4.532902,-5.561487,5.543021,-2.437849,1.966101,-4.410140,5.009928,-7.957713,-2.581855,-9.317030,6.223860,8.961254,9.247504,-9.254339,-9.088469,9.864746,-8.912782,-9.564142,5.964308,2.940481,-9.217814,-9.334572,-1.429735,-4.268656,6.238572,3.629920,-0.629670,-4.079497,9.702534,-3.135684,-3.451224,-1.379884,9.150518,-8.214472,4.671108,-5.173525,7.868796,2.888984,5.871779,-7.617271,-3.577642,-7.577343,-5.893535,9.408723,7.588807,1.232014,9.689692,1.423302,-9.898771,6.146796,3.393297,-1.725353,-0.766878,7.117168,2.980485,-7.812825,0.020026,8.679142,6.710933,-9.466383,-7.806188,-5.568966,5.298484,5.593209,9.261862,7.956496,-9.873818,5.629046,-4.675517,-4.185291,-0.027217,3.127251,4.078316,-3.992297,4.721101,-6.115270,-6.521952,7.726651,-8.788108,-5.283070,9.628642,-6.567357,3.854540,5.461575,-3.439100,0.421646,-0.740818,4.258508,2.540012,7.120709,-9.740615,7.773646,-7.460175,-6.597447,0.345988,0.582382,-1.077764,-2.568423,7.239085,4.442036,5.182188,3.043415,-8.445084,-9.816882,-3.164428,-1.287532,7.028884,6.402256,6.535497,-3.717957,-3.399378,7.551445,8.045295,-5.116546,1.790420,1.830165,7.505794,0.187312,9.198974,3.379379,8.927760,-1.658870,4.268413,-4.810649,8.966075,1.156292,-1.223242,-9.128732,-1.319253,5.483990,0.674271,7.541796,0.105945,-0.596350,-6.741457,-2.443075,6.046914,-5.346616,-2.922840,0.103804,1.420647,-6.117807,-3.208219,9.909100,7.660765,-0.959317,9.207198,6.588386,-7.887788,5.584612,-8.406308,-7.161788,-1.259470,-0.762750,-7.811909,-9.647784,3.403311,7.481417,-3.427029,-1.626538,8.638779,-0.150758,-4.642315,4.176757,3.254784,5.372801,-5.913167,4.234115,-8.572667,-1.001785,-4.340463,-5.356010,3.828257,1.836620,2.614139,5.104446,-8.079961,8.106087,-5.312221,-1.162787,-3.162092,6.042278,4.792695,9.124266,-9.541248,-9.540056,6.830444,-7.637404,0.772706,-7.226294,-1.751424,5.332703,0.145179,8.248841,-0.565268,8.410048,-8.973240,5.516744,7.032676,4.738530,-8.152455,-8.003989,0.642638,-1.108257,-2.616536,2.708323,2.485831,-4.336506,5.757428,-2.346823,1.027358,-8.010171,-5.902843,3.922246,7.928047,4.927265,6.166808,0.162472,8.424958,7.584129,-1.339944,-7.074026,8.614363,-9.768965,-8.219251,-3.259060,-7.598564,6.029145,3.506399,-3.546280,-5.094839,-1.774165,-9.033852,-1.882433,-5.888858,7.126114,-9.935505,-8.985985,-6.003672,-1.555380,2.345284,-9.393050,-3.976450,-9.060575,9.410916,-8.833490,-9.231494,5.684912,-7.434936,-2.332816,5.175801,0.859330,5.902046,5.880167,-2.717299,1.422673,2.412963,7.277191,6.042361,8.112446,-3.150306,-5.949554,-2.224369,9.062800,7.828005,7.358143,-5.223195,-1.109051,-4.332148,4.306202,-6.720809,-4.711312,3.897544,0.486375,1.775854,7.570309,-5.483124,0.124884,9.471948,3.983555,-3.399372,5.252276,3.451605,5.831249,8.238664,-9.494201,2.274116,5.628535,-1.789550,7.052921,0.047668,4.295270,6.444355,7.788830,-8.288959,3.323713,4.666472,3.147525,3.643006,8.512036,3.785294,-6.534489,-2.858104,8.951680,-7.213491,0.226677,7.480648,6.773765,1.929333,8.040889,7.473352,-9.054816,7.555761,8.447931,-1.033001,-0.742596,-2.391437,-8.309756,-4.558047,9.172152,8.515366,6.836396,2.482145,5.191429,3.218386,-4.506500,7.797161,1.609601,-4.302709,3.730854,8.619642,0.826721,-8.394800,0.292462,6.778816,5.560471,2.705583,-3.406567,9.195997,5.580946,-9.558074,1.248505,-9.600228,8.075934,1.834242,-9.567292,-0.921325,-8.675135,8.324231,4.939883,-8.480649,2.579187,5.461046,5.364741,6.298561,5.534283,-9.624691,-7.293758,-9.471024,-8.836772,-5.557585,-4.372889,-3.112575,-3.694328,-5.989513,-5.017634,-2.722884,-3.258788,0.542132,6.455575,-1.032746,0.203436,9.970320,-3.062362,6.117278,-1.070137,4.310489,-5.342086,0.525027,2.339911,-0.521718,8.777808,-7.350364,2.860782,9.071545,-8.616990,0.983144,-8.420887,6.072318,-9.574997,6.119800,0.181503,-8.927533,-9.584167,-0.430709,9.097199,-5.596748,5.428873,3.066966,-8.592465,1.598244,-2.274739,-6.398225,-1.443617,8.164750,-7.618381,0.067842,5.629464,3.676666,7.876857,-9.190277,7.864819,0.691065,4.134960,1.930462,8.454258,-9.083351,6.435393,5.734723,4.690002,7.779172,1.343180,3.100559,-5.588499,8.463291,-6.362844,-7.626946,-3.201577,-4.228217,-5.655568,0.148318,9.543497,-3.459337,4.706227,-3.482510,-9.256154,-5.943050,-2.148586,3.648166,4.721231,-0.711862,-0.304550,0.231709,1.428671,-5.526535,5.400658,6.354652,7.558650,6.920706,4.571824,8.994535,7.677141,-5.420294,1.476244,-1.165513,-7.234941,-0.698300,-5.658589,5.683472,-6.670623,1.151230,5.832096,-9.993609,-2.238097,6.322762,8.496939,-8.855785,4.024493,-1.268111,-7.487632,9.640845,3.124067,9.212673,6.380547,3.674042,-1.459137,4.788111,-7.412949,-9.994433,3.433811,-8.529525,0.266603,-2.471220,5.953377,4.768288,3.288549,-6.826234,2.931999,-4.232534,-6.465647,-3.470363,5.349954,9.508867,9.582924,-7.367785,4.672974,1.634151,0.402525,7.775694,-2.323193,-0.809331,3.373044,-8.924265,-6.819608,9.544653,4.119810,7.447100,4.768192,-8.662821,3.409217,-6.330069,2.897670,2.553965,6.898898,-0.722793,2.891838,4.839488,2.793312,3.029660,8.695871,2.828120,-6.343880,3.676981,5.585608,-1.280055,-4.026707,0.402227,-3.511938,0.610117,-1.019892,2.520363,-2.711979,-1.100907,2.005371,-6.034301,4.101473,8.398773,-7.907678,5.181230,-9.573556,-7.613345,-7.699197,-2.206798,-4.799412,-2.884281,6.837530,8.961931,6.034861,-0.603399,6.437480,4.376326,-0.349401,7.179150,2.487179,-0.119932,-3.631611,-6.119902,-8.522718,-7.643219,-1.676627,4.787687,-0.752789,-6.378071,0.325899,-9.541651,6.638062,3.715556,-3.649321,-2.079618,6.914905,4.719051,-5.237879,7.229815,5.568160,3.415869,-7.552093,0.107857,9.928514,-9.987989,-4.487144,-4.979449,-2.533655,1.504821,-6.094689,-7.032130,-4.800605,7.585993,-7.378766,-4.954436,-2.048868,1.609766,-6.798772,-5.600736,-7.954326,-4.244691,8.243982,-5.567516,-4.503115,6.102004,-4.457180,2.274987,7.484013,5.732965,6.046443,2.359039,0.052667,-1.864092,-8.684637,-4.554924,-1.396954,0.817786,2.224330,1.774927,-1.082298,-1.543838,1.855662,1.167005,-3.950966,-4.472029,-5.020983,-4.335339,-4.939373,-8.560381,0.121580,-2.358833,7.620300,8.172436,3.423543,7.258458,7.171779,-1.253561,0.005967,-3.698055,-4.101507,7.408410,-6.901139,5.162312,-8.350322,7.851452,-7.788865,0.591800,-9.574541,-8.537114,-7.912390,7.030253,1.533606,-8.116343,4.819943,-4.177017,4.749726,8.081557,4.381301,-4.641468,-8.948751,2.697431,3.680138,-5.152444,-9.503971,-5.427947,-4.866014,-5.921134,8.545584,-2.131503,8.230138,1.238005,-4.011393,0.560092,2.100473,-6.854976,8.665464,-0.642427,-2.746876,-8.707913,5.139326,3.631052,-3.036111,7.257352,-4.934907,5.053990,-6.203154,-1.458905,1.107221,3.322078,-2.115636,-8.937276,7.298575,-3.798959,6.301396,-0.929223,7.622037,1.817599,-9.671870,-1.982584,-6.456974,-8.264674,-3.855686,-0.963719,-2.708331,-5.092951,0.088864,2.072459,4.431354,-6.574152,-0.563198,5.189738,2.969421,-1.070536,6.575963,-5.554503,-1.794495,-0.137764,-2.666977,-4.934701,-7.571050,9.311064,4.832810,5.710291,-1.766227,9.318568,-6.414533,1.036003,6.596581,7.109628,-0.980256,2.575508,2.575327,0.528379,-8.258975,-8.982276,-6.727436,-5.801472,-0.082157,-6.090833,1.280522,-7.445915,-6.884773,0.865943,4.817998,-6.919520,8.250878,-0.303352,9.567308,-2.539579,7.931135,6.553084,-9.188289,1.610563,9.412994,8.355400,1.096634,-6.414215,4.729149,-1.888916,2.698931,-9.215519,-0.402489,4.758026,-1.334180,2.322048,-5.481981,7.578569,-4.819216,-9.262235,-9.998325,-4.242388,9.661084,1.082767,3.438120,7.860061,-4.029312,9.619665,-9.330692,4.426376,-6.939471,-5.236818,8.547542,3.378078,-1.167450,4.705199,1.806440,-3.675278,-6.609454,-3.501241,1.225276,-1.402222,4.610614,-7.387331,-5.171952,3.257717,-7.528211,-0.937333,2.138748,5.663822,6.695968,8.777654,1.088429,4.913967,1.752235,7.362840,0.526296,4.956285,6.435880,-7.819191,2.729928,-1.993828,0.591974,8.889760,-1.266401,-6.154848,4.492792,-4.467109,8.979228,-6.220192,7.035373,-7.330127,-8.653170,-4.292530,1.403580,1.930743,-1.465971,6.203948,-5.396616,-3.834087,5.508196,-1.610452,-9.404815,9.318035,-6.685537,7.263148,4.751861,-3.665629,0.333789,9.909625,3.230321,2.583917,-2.716898,4.933624,9.543097,1.977777,-1.711823,3.512371,3.587600,0.564767,-5.301642,7.418191,-5.609783,4.758855,-9.643836,-1.291975,-6.136455,5.081951,-7.665432,3.788765,2.097622,6.705928,9.153935,-1.749185,0.612156,-5.446056,-2.871401,-8.871405,-7.966346,-3.732052,-0.939823,-4.617295,-3.663980,-4.448570,6.660236,-6.686840,-8.403239,-4.317778,-2.827314,-4.854187,-6.526825,-2.959628,8.656028,6.656073,-0.296211,-6.032927,0.786967,1.363064,2.877135,-9.836777,-5.325603,5.533600,-4.777768,-0.520609,-9.215087,3.254144,8.916722,-2.896392,-2.223718,-8.583522,2.544665,1.331955,-5.131177,5.303684,-4.382946,-7.389413,-0.537552,-3.785665,5.137325,-3.952420,6.387717,7.403014,7.934565,2.401909,8.548758,-1.594777,4.218479,7.492010,1.771205,4.983474,1.197849,-0.970843,8.488881,-2.068073,0.004542,-6.579481,-6.141460,2.245677,2.421067,5.653608,0.460064,-1.006251,-8.227716,-8.255392,-8.927093,2.204923,6.531397,1.022356,-2.559114,4.839704,-2.021872,6.027318,7.572363,-7.257764,6.928465,-6.207383,-9.306937,9.295082,-5.855432,-3.484844,8.043715,-0.886750,7.677264,2.014321,-0.820074,1.920339,6.832475,8.377347,1.903089,9.075406,-6.860555,8.984258,-8.586384,2.835407,-7.662273,5.054878,2.599918,-8.862253,-9.154774,3.285609,6.415545,1.643484,6.819595,7.830203,6.190542,6.366308,-5.733628,-2.211549,-4.675727,-8.604743,0.500358,-5.453436,1.648330,7.746517,5.714847,-5.621217,5.900328,4.260683,7.879494,5.620258,4.836714,-9.405747,-8.714985,6.412606,-1.187350,5.188909,4.418738,-3.272508,2.434040,-4.758383,-7.783203,4.733585,0.541982,-6.258916,6.291442,0.338905,8.082184,8.361704,-6.501544,-0.370312,-7.443177,-3.069537,9.234340,-1.791689,-6.713752,3.440128,-1.172693,-3.842789,4.357338,-2.133414,-4.359011,-2.179638,0.288729,1.169429,-5.737449,-8.441211,-0.266169,-7.492222,7.148266,-1.197174,-5.241898,3.927195,-0.385780,-9.810656,-7.312535,-3.845510,-8.100326,-9.249007,-8.022587,6.650018,1.163608,6.566230,-2.204832,-3.545735,3.842198,9.316052,-0.860288,-3.701665,-1.732934,6.944458,1.965138,5.043865,-5.407597,0.687849,-9.094508,9.740070,-4.212397,9.686495,-1.315612,-3.000314,-3.861443,9.139802,-9.872322,9.070080,-5.522506,-6.624365,-2.448418,3.706508,1.454223,-8.911641,1.878686,-1.392329,-1.563707,-6.618538,6.918362,-4.019079,-0.749847,-9.523258,8.526502,8.751739,-6.031450,1.668489,-5.062526,2.393025,9.841794,4.475285,1.932662,-2.712746,8.718391,4.280841,-5.059814,-8.180353,8.619262,7.006576,-2.132925,4.872131,-9.842946,4.902134,5.977194,0.395143,-7.339618,-7.767487,-1.460967,-9.589343,0.356644,-8.845740,8.823819,6.236508,5.087942,-4.952736,5.620409,5.190648,-3.527290,-5.805298,1.296633,9.393940,-4.942177,-9.209967,-8.585758,-5.178834,-9.127961,7.737763,1.765500,-2.909324,-6.700879,-0.437304,-3.916052,9.207458,9.484289,1.193135,1.931480,-5.613906,-7.152018,-5.701053,8.002473,-9.947148,1.518884,-7.163115,-6.586918,-6.778267,9.730026,8.607240,-5.148309,-4.514164,-2.488177,-2.868477,-9.626700,-3.967325,1.046760,-7.127282,0.251146,-1.504011,-0.270391,-1.548690,-7.457136,2.323275,8.552909,8.105947,-6.369898,8.696820,1.912990,-5.865196,4.089441,-9.255343,-0.024928,6.872244,-2.701159,-0.618492,-7.784664,2.477948,1.682211,-5.183059,5.358073,-8.936001,-7.166999,6.588064,-4.051728,5.215368,-8.330032,-7.456745,-6.321060,-5.622518,-9.198994,-9.427313,4.179610,7.965509,-7.968644,-8.076449,5.708881,7.640809,-9.438333,-8.674181,7.051680,-1.780553,1.520635,-3.198565,1.783973,-1.430309,6.988623,-4.932199,3.973602,-2.998440,-0.073910,9.844882,8.482502,5.989018,5.921811,-0.236216,1.912041,-3.734103,-6.340904,6.695464,-2.750847,8.382309,-4.421288,-8.420146,1.835567,7.318151,1.509084,1.579102,-0.945289,4.369537,-0.314068,-9.098182,-8.905303,2.261886,6.346368,-8.358140,-2.531320,7.958390,-3.946391,-4.540650,-9.479745,0.173979,3.139834,5.188662,9.410400,8.220878,-5.692733,0.990879,7.232409,8.909514,1.909384,-0.672346,6.815639,-3.976819,3.055744,9.147874,7.865145,-4.880713,-9.321698,-7.551014,-5.340692,4.131757,4.305455,9.699021,5.441346,5.343531,0.828997,3.030928,6.817004,-3.928254,-1.990210,5.083889,-5.006924,-5.812431,2.790618,-4.105819,3.758165,-0.449779,-7.831367,5.665820,5.620348,7.190917,-3.976188,3.544507,-8.962416,-6.851132,-9.115820,-0.419721,4.358322,1.604071,8.670307,-6.412904,7.848090,0.976494,4.577468,-1.057077,1.335939,5.708784,-1.754429,-9.195117,-2.000939,0.845824,-5.086740,8.301332,8.839485,-4.554813,-6.751967,3.062476,3.911478,5.767600,1.353403,1.725588,6.053674,-0.542626,-0.759090,9.953299,8.132795,0.071439,-9.622492,-9.393035,9.204297,9.031571,1.139136,4.292380,7.886556,7.463314,-9.568826,-0.351093,9.990311,6.320559,7.305295,-5.983733,-9.242189,-6.170050,-9.590890,-4.758740,0.482717,9.449991,-2.683305,2.459078,-6.408989,-5.634667,-9.610331,-2.528497,4.523015,5.912816,-7.645482,4.990566,1.672187,-2.463139,-6.599320,9.895226,-9.785772,3.511290,5.758153,-2.083846,3.276338,7.088007,2.700768,-4.549240,6.799050,7.016108,6.893711,-9.689084,-7.843299,0.223777,3.576522,-4.878396,6.295372,-3.392934,5.739875,-6.535679,4.079851,-0.595155,-2.797845,1.965335,-9.537194,2.786280,-2.840906,-6.075187,-7.911519,2.829995,-2.228415,0.784352,8.214940,-5.852238,6.585101,-7.172046,-0.875441,8.289224,9.706417,6.204395,-3.567373,5.415631,-2.699036,0.671393,7.213688,6.507010,1.152216,-7.678216,-7.110125,2.652951,0.158314,5.441873,-4.007581,-7.970642,6.712925,2.420571,5.508275,-7.962246,-2.682097,-2.738760,6.716680,8.953825,4.232864,0.861394,-7.894106,2.092232,-0.979909,-9.032985,3.422044,-4.190928,-9.441267,-1.232609,5.553574,3.890248,5.298948,3.634098,9.719153,9.573920,-1.917327,5.998026,3.558980,2.423131,6.843947,-3.335029,-4.408573,0.749482,-7.088595,-3.851855,5.100458,9.539221,-1.050884,6.642893,0.216963,-4.198605,4.441653,-1.708426,-6.607655,9.583232,7.156643,-3.330605,-1.497390,-8.456496,-1.640720,-4.631291,4.072543,-5.732184,5.705012,3.255291,-3.309023,-3.428553,2.261446,-9.834965,-8.174942,1.278425,7.111345,-1.087832,-5.083621,-1.801739,6.595888,-5.791941,-7.050185,-8.819320,-9.026252,-0.113850,1.435092,-8.958072,8.440425,-9.241019,-6.291533,-3.447357,-1.674841,-8.670870,6.359097,7.332509,4.148926,7.407223,-5.020854,3.661065,-0.091974,3.437022,6.416637,-4.074753,-4.940607,-6.090870,7.414348,-1.028437,8.828783,-9.443413,4.304489,-4.483881,6.935093,-3.456251,3.570457,-6.551145,4.193531,-6.257562,6.693490,3.108277,8.784241,2.962703,-6.361617,-0.448060,-6.578885,6.330182,-1.171596,-8.301243,2.484393,5.678399,3.669278,-8.806595,1.275838,6.846385,-4.777289,-5.786614,-8.305735,-9.999773,5.593672,4.966556,4.563083,6.937647,-6.553802,8.951820,-3.295241,-0.971999,-5.746149,-2.209480,9.816730,-4.445298,6.090922,-4.327181,-4.031387,-6.650529,2.514795,7.961270,-6.994328,2.394762,2.831465,2.008889,4.809483,9.229935,-8.632430,-6.026740,6.742161,2.894127,3.154845,-3.125758,-5.131503,-7.394136,-9.916582,-4.999486,-9.845078,5.399020,-4.315814,-0.647405,4.998656,1.718514,5.873755,5.132992,0.728491,3.063548,-9.621537,-2.085980,5.485196,4.681055,2.509013,-2.930012,0.966751,1.591732,-6.171284,1.399939,4.635244,-1.828972,-7.163768,1.300545,-2.615894,8.474969,-2.209317,-1.833007,-3.469330,-9.106075,1.640030,3.316438,-9.025540,6.511636,-8.938382,-1.385055,7.804572,0.149127,6.069507,5.701160,0.524246,-5.060491,0.938157,4.885086,-8.526336,4.181546,0.170818,-1.949327,2.384129,-5.166614,7.166854,1.730056,5.088030,-9.460741,9.042671,3.687870,-5.239536,-3.071304,-7.538915,0.540522,4.641200,-1.851453,-1.339773,4.153264,-1.860122,1.158156,-7.600535,3.432002,4.694308,-0.335612,1.202413,-9.903370,-5.025588,6.538168,-0.809585,5.287429,4.696295,-8.102651,8.260975,2.747270,-1.644754,1.316964,9.052809,-6.923458,-7.988214,5.767754,-8.302960,-1.964159,1.190567,0.403954,-5.016181,0.558376,0.046679,5.887588,7.293815,-7.771896,-8.044101,7.292638,-5.761410,-5.590245,-7.664147,1.945675,6.634935,6.296319,9.120163,0.236108,-7.326834,-3.041975,-8.942816,-0.306257,-1.179650,9.984264,-1.944801,3.758333,2.118945,2.740135,0.200706,-7.107247,-4.614836,5.747333,9.082675,-0.272419,-8.643109,8.359964,-8.888839,-0.575315,-6.030852,5.197688,-2.962782,-9.645623,4.961887,-8.858337,-2.697312,8.709099,-9.212060,-9.778659,5.822629,6.080519,4.102116,5.499886,-6.114320,4.284412,3.957345,0.242697,4.022558,7.487403,-8.037470,1.670457,5.220924,7.825416,-1.412819,1.650528,-4.836726,5.658005,2.699813,-8.134492,-6.563226,-3.266608,-4.609083,-1.382654,5.674260,-6.804167,2.839293,-3.453440,7.858652,-6.594063,-0.117286,7.840227,3.361149,-8.551194,6.176819,-9.912410,-3.166445,-8.391386,1.473591,-6.917960,-4.419473,-7.932819,5.786451,-3.022147,-3.566180,-8.049839,-6.823608,-9.516804,-6.557049,-9.605546,9.515360,5.024116,-3.899928,-7.080672,-2.146741,-6.160940,-6.400096,-9.087219,-5.454731,-7.100481,-9.864921,2.181692,-7.166770,-5.428419,-8.462866,1.553340,2.782267,-3.471121,-5.988979,0.025233,8.377933,1.481736,-9.879503,6.225991,2.175218,-8.307899,-0.489946,-4.467734,9.120076,7.815924,-8.138612,1.262205,-1.729584,1.866359,-8.956342,1.929309,-3.015798,3.302114,8.854727,8.823896,-8.972779,-9.025098,3.416178,-7.663416,7.550268,3.254721,-2.558628,8.257486,-9.233478,8.530647,-7.362158,-5.101363,4.795050,0.658890,6.639601,5.472979,-4.004011,-9.352535,1.927157,-5.941067,6.543503,-1.283351,-2.939795,-2.764393,-4.409461,-1.225732,-9.331085,2.182505,-7.064053,-9.361193,-7.382226,-0.695242,4.469539,-5.784132,4.898818,1.061856,-8.855146,-2.865951,-5.576202,7.584111,-2.684158,8.083545,9.577656,-9.503840,9.703097,0.473077,8.095931,5.653131,-2.479737,4.750314,-5.055294,-0.527369,-8.844474,-0.347881,8.509440,4.460586,4.481050,2.247604,6.792441,-9.452960,-6.893949,-7.321205,1.000497,7.935849,-9.031572,1.703305,4.201129,9.139102,-4.071394,-2.943163,-6.976079,6.493118,-4.958750,-1.952741,5.838251,7.358611,-9.954543,2.454999,1.642387,4.085762,8.117133,-9.436168,9.207091,-6.989624,9.627472,0.038811,-3.792065,1.255435,6.613922,-4.228253,0.580886,1.474422,-1.396473,2.977840,4.308599,0.489964,-4.157431,5.819414,2.258457,3.816571,2.681414,-1.054809,-1.567006,-1.921442,7.731834,-2.811373,-6.866552,-7.827877,-5.659977,-0.811481,2.076514,-6.092174,-0.435575,9.877044,3.553012,-6.047504,9.164242,-5.630376,9.702058,-8.154259,2.610375,2.895934,-4.318978,-7.172012,4.495192,-2.945439,-3.797465,-8.139417,-3.594992,3.302912,2.559016,-2.960633,-5.407937,-7.813648,-6.206041,7.657301,9.550881,6.560142,-6.363231,-1.596454,9.796838,-0.960147,9.023514,-9.259100,-6.470181,4.540955,7.969623,7.307801,-9.106419,7.988799,-7.545045,-9.150321,0.865240,1.388304,-6.020254,-8.159414,-9.196793,6.525294,1.298114,1.774751,3.527615,2.154981,6.334563,8.901649,-7.971238,-8.916867,3.641504,-2.550864,-2.348121,-1.829312,1.812859,-1.750329,-1.236125,8.013311,3.480900,3.818967,9.715817,-3.069471,9.982430,-9.205608,-3.119545,-9.680528,-7.685234,8.481462,-3.967550,4.907380,-5.746357,6.706458,0.134220,-3.607427,-7.510887,-2.784989,0.210893,-9.501947,-4.210164,-7.306194,6.520907,-2.323010,-4.723769,-1.896040,9.936506,-3.874422,-2.089959,-8.137751,2.367178,-6.742296,8.224841,7.226803,2.781335,2.545566,1.661133,6.065051,7.800500,-5.576551,1.667873,-1.783069,-4.854147,-7.558888,4.718501,-0.262028,7.121043,-9.610178,7.092382,3.411535,8.131688,-6.960714,3.201976,5.401649,0.132317,-5.856716,-0.100371,-5.064176,1.995669,8.682472,1.300859,7.892347,8.385816,4.167621,-5.402954,9.652831,-6.524476,-5.516196,6.517035,-1.702387,5.137612,5.784774,3.177865,-8.415165,-5.525287,0.292445,7.521206,3.220416,-4.193190,-0.675490,8.029179,-0.793252,1.618563,6.618830,-8.660905,-3.332027,-9.831268,-1.542932,4.793911,5.345644,-5.054252,6.698179,0.398401,-5.808168,-7.265889,-8.634687,3.553010,9.536366,1.977960,0.543418,-2.701548,9.443665,-2.258112,-0.167242,-9.869898,6.990185,3.067521,6.686976,0.490578,-0.305271,-2.406475,-7.556201,-9.376202,-7.946850,-5.444158,5.774322,2.356982,-8.400146,-8.833159,0.017018,-2.889190,-9.941513,-5.095325,-5.491527,7.758985,9.915800,-3.252101,7.365798,7.230813,-3.834040,-1.004465,-9.173291,2.684490,1.304847,4.770799,-8.343485,3.177998,6.739512,-2.730411,-0.423578,7.610293,4.359147,1.456284,-2.067005,9.276260,-3.367768,-2.535739,2.117132,2.198347,-1.124816,-2.791698,-5.688490,1.867457,3.210329,-0.380332,2.514263,9.467151,7.767706,-0.045476,8.446267,-2.443330,5.770181,-3.123100,-3.762193,1.949102,-3.338690,-8.181166,3.140292,5.910319,0.140686,-3.316737,4.458304,-5.338185,-8.260865,-1.794692,-7.883951,-3.444687,3.674000,-7.061591,-8.160024,-8.095515,1.640976,-6.863839,-4.273986,5.490862,6.264468,6.938492,2.802641,0.323880,-9.403907,0.394198,-6.809719,-9.189209,-0.335562,-8.502389,-6.826850,-4.436334,4.104372,-8.867530,-9.893479,5.343504,-4.828061,-6.442399,-2.813710,0.439047,4.589584,4.541658,-4.065599,8.845190,6.815214,-2.123558,8.436016,0.313833,8.848278,-2.238276,-1.773015,8.813164,-2.521777,-4.218183,7.772797,7.814359,6.814669,-5.767682,-3.187964,-5.526185,0.663321,4.052647,7.026240,0.687546,5.001452,-6.146806,-0.721608,-9.056192,8.261186,3.365032,-8.112753,9.908256,-2.842486,-4.555500,-0.525434,-9.148318,9.698233,-7.574987,-9.452155,9.932361,6.952716,8.712006,2.866460,1.140795,5.170512,0.626542,4.760677,4.378107,-1.094329,6.264218,-8.393680,6.551468,3.497841,5.019840,0.300081,7.848047,-8.058086,-3.467454,-1.484451,5.457155,0.229871,-7.980886,1.208952,-9.468109,0.511736,-4.486488,9.418788,5.260106,8.508191,-6.536477,7.438733,-0.509504,3.735556,5.675986,-5.575274,4.392447,2.863988,-9.497236,0.312005,-0.285049,-1.313461,-3.921774,-7.250262,0.387178,-9.432942,9.506766,8.638665,-7.945130,-9.657417,4.888236,-6.427358,-4.731974,-9.436154,-2.448823,4.738113,-1.566120,-5.275855,6.955272,-9.016109,-4.056957,4.490496,-3.851139,5.400172,7.848615,-8.273281,-3.204182,0.180871,-6.896609,-4.926655,8.740139,4.318369,8.121342,-8.936711,8.798677,0.917934,-2.750854,3.038573,-8.045137,2.685499,-9.127888,-6.573716,-0.337290,-1.175775,5.335764,4.921779,-7.754522,-6.309037,-2.151635,8.677604,0.034358,-1.241366,3.989989,-3.108338,-0.081100,9.238410,3.456579,-8.561425,3.018230,-3.592343,8.844906,0.169732,-3.452924,1.040674,-5.566372,-3.169393,-9.037180,9.038283,-6.992282,6.430653,3.770937,-9.043682,-6.213779,-6.104063,8.611398,-8.754678,3.909473,-9.795875,1.318102,-6.672392,-9.908577,9.982903,8.579194,-2.107987,-2.852763,9.624419,-3.287579,-5.296156,-6.866658,-0.050283,9.032417,-3.805420,-4.475927,-4.165610,-3.282927,-4.118254,-6.297685,9.627688,-1.536296,1.343761,9.893352,5.423544,-9.662536,-6.893071,-8.577474,-1.726866,6.620419,-6.399311,-6.466735,6.273981,-4.804822,0.880730,4.912890,-5.772455,1.912928,-2.466145,-5.251922,-6.116202,1.459566,0.662083,-6.775583,5.106437,-4.655397,2.771193,3.798564,-1.498037,-4.470902,-9.874899,-4.945712,-6.401925,-4.881256,1.771540,-6.274336,-1.890042,-3.732171,4.822021,6.418352,6.747241,6.155253,-5.060150,4.805598,-5.094680,9.479104,-1.603067,4.051342,6.736272,1.637648,6.726085,-1.708596,-9.465015,9.672044,2.078139,-2.196320,5.258181,-8.005376,-8.686786,-9.031515,4.770644,2.142314,6.501601,-2.406993,7.561475,1.160121,8.705775,-6.091305,1.631339,-5.120865,-5.999351,1.475215,-5.793499,-2.079675,3.699560,1.262967,-4.352263,-3.570474,3.519940,-4.714660,5.154787,2.562659,7.675054,-2.521943,-4.498570,-3.083793,8.870308,-5.442878,3.886304,9.104597,3.514541,0.361722,9.265152,6.321435,0.050932,6.871002,-5.245282,5.409657,-9.377771,-1.462207,-7.004983,-9.067349,-3.230848,7.186946,7.467924,-2.000651,2.676756,-0.969682,-5.664939,-5.561769,3.925933,-4.092402,-2.997399,3.360518,8.880704,2.046209,-4.527894,2.811386,-4.706503,-9.865908,1.382341,-8.017293,0.161451,-3.001353,2.872259,4.062662,-7.099678,-8.792942,2.553991,-7.965640,3.105678,7.819363,3.956223,-9.156258,8.416402,7.665486,4.392093,-2.490723,-6.177227,-2.082267,6.183253,-4.908014,4.322697,-7.499481,-1.125941,2.285782,8.149316,-8.529751,-8.461560,-5.243223,3.921617,-9.061318,-3.769698,3.299604,3.480016,-7.021362,6.466226,2.909043,4.741862,-5.148036,-4.446460,7.766441,-1.286891,-5.728105,-3.722596,-3.810952,-6.198884,-8.782142,9.672068,9.215551,-2.996312,1.962733,-8.964263,-9.899701,9.339978,0.961569,5.176303,7.855603,-0.948493,-8.709698,-8.982316,9.222395,6.273858,5.441167,1.104230,-4.302078,-5.573854,-7.478172,-0.491422,-0.929266,4.434503,1.731807,-4.510158,-3.301831,-7.524538,8.049172,3.620525,3.139390,1.703222,-9.933776,0.719974,-7.969323,-6.989684,-2.024166,9.669077,-3.505229,-7.787003,5.610853,-9.206932,-2.745262,-9.993358,-9.998389,-8.347515,7.872932,-1.269517,-7.437747,-5.636903,-8.868552,5.393064,6.233116,8.302098,9.673443,0.186310,7.759388,-4.121017,-6.417753,6.424703,0.472071,-7.147822,4.678875,-2.347135,-8.261051,-6.355722,8.060383,4.873308,2.120478,2.590252,-1.110095,0.558567,-1.607425,6.121663,2.157208,2.610738,-6.421734,3.786192,8.309762,-6.102093,-1.698383,-3.631882,-5.578484,-6.036608,-6.158051,4.547027,-6.809813,-4.992882,-6.227928,9.375971,3.334704,-0.096119,-9.604919,7.821054,7.612449,6.464638,1.446926,-8.547441,9.122258,3.150416,-1.583157,-5.323253,9.217109,4.844412,3.606643,0.780563,-7.094050,-2.756759,5.213186,-3.485803,6.433530,-7.498972,1.993233,2.542902,4.951197,-0.173577,0.809005,-2.245655,-8.244285,-0.780740,-1.082507,-1.248427,-1.187383,0.075850,-1.626087,-2.005189,6.181869,-4.030708,1.161378,7.323552,-3.813313,-1.496081,6.822755,1.458276,8.318984,3.334119,9.397283,-7.059001,-2.926344,-3.059264,3.196005,2.272441,2.071595,8.460711,5.065015,-2.031514,-9.160054,4.418489,6.014110,6.716565,-3.119886,7.579169,-6.042604,4.375252,0.867877,-1.242633,3.866361,-1.524025,6.405657,1.836126,-7.570184,3.169363,2.134180,-0.985314,1.137067,9.720454,-7.144514,6.879336,-9.468448,-2.074242,-9.481534,-5.640345,-3.709126,2.268325,-5.862836,-0.112446,-7.096393,0.950887,-7.247590,-8.161712,-3.419446,0.016821,-0.426531,5.755373,-7.799829,4.842018,-2.328125,-1.946500,-3.700742,8.618286,-6.360831,7.245696,0.079504,-1.087879,5.544592,7.257287,-2.754990,-6.522959,7.380712,6.829269,4.068570,9.303432,-0.575017,-9.080189,9.383634,0.336436,0.814463,-1.335337,-8.654064,-3.961136,2.974710,1.544893,1.559530,1.238281,5.381320,-2.415055,5.055145,5.672267,5.957241,-7.093598,4.359121,-5.525534,-4.159421,5.970076,-3.232741,-2.077053,6.328587,6.838248,-8.712269,1.332533,-8.705327,-8.394082,3.017805,1.134835,-7.539096,3.028295,-3.121861,-5.901750,-7.774304,2.827335,-8.515963,1.718472,5.946693,-1.145776,5.294406,3.583618,4.565379,8.628708,9.482937,2.611878,-8.696141,9.625416,-2.789272,3.041651,8.691336,6.123541,6.293686,0.615699,-3.415972,-6.238540,-3.874930,2.627973,1.065005,-9.524414,9.206183,-3.941495,2.035458,-1.877177,-1.638210,-0.911950,-5.318228,5.719658,-1.885189,-2.621174,-1.887296,-4.037012,2.307083,-3.607079,-3.579199,9.504505,-7.392719,4.377288,-2.693505,4.692911,-6.428547,-2.894814,-1.406746,-9.632038,0.630923,9.777000,3.593991,-0.570464,0.779904,4.404267,4.030263,2.084472,8.054526,4.493886,1.268242,-9.865908,0.992980,-6.127734,-2.000347,-1.768713,-1.356523,1.120172,-8.512197,-3.169333,-0.974942,3.748856,-9.571261,9.396959,-3.362840,6.319903,6.734994,9.390945,2.426817,-7.521886,-7.919887,2.355138,-6.440030,-2.368673,-8.899762,-5.327441,-2.192743,-6.214637,9.612277,-6.182462,4.678204,4.434419,5.225593,2.966740,-2.539264,-7.246978,-0.636851,8.539937,-7.686722,5.342225,-0.205980,6.615041,-1.440641,-7.538699,0.134343,1.137080,-1.088218,-9.586969,9.426299,-3.291980,6.591870,-1.544732,-9.053841,7.328374,7.805907,5.055607,-5.290753,-0.886311,6.935787,-7.386294,-8.904108,9.755297,-5.697457,-7.210827,0.101567,-6.733582,-5.897640,-1.240719,-7.509070,5.493485,5.218594,-2.239175,-5.777357,-1.696081,1.886534,-1.042059,-1.361824,-9.335186,3.960019,-7.092601,-2.890944,-4.485664,5.715561,1.707092,-9.324747,6.201537,-2.045362,8.925936,-5.391196,-4.030756,7.149566,5.185735,-2.928928,-6.890017,3.989886,-5.528097,2.650269,-9.465447,2.221770,3.316586,-0.209358,3.427811,-6.573484,7.615375,-1.640231,-1.107379,9.959341,6.553772,1.722104,0.356062,-8.894302,-0.508826,-0.537277,-6.589531,8.556886,8.167913,-1.184350,-8.252894,-1.995767,-6.370266,3.407458,-8.485680,-3.503630,-4.898250,2.981517,-5.029193,6.363594,-6.181642,8.103952,0.260350,-1.849596,9.331757,-2.489948,1.752575,9.985789,8.505348,-8.793416,7.426325,-3.618425,-6.901307,-6.200257,9.653301,-4.737970,4.374626,6.949316,-2.474553,-5.312071,-5.084368,6.290856,5.362366,5.311900,3.801446,-1.141085,7.148525,-7.961697,-0.724254,-6.145856,-0.553374,7.427327,0.786727,-4.110172,-8.209406,9.521239,4.654004,-7.038195,1.392934,-0.498497,0.289662,-6.796763,5.437516,8.221513,3.532485,6.551132,-2.145975,0.171430,2.783306,2.307275,-2.779518,3.052869,2.330970,-7.211783,1.930408,0.565755,3.597698,4.658676,-5.764095,4.576765,5.071619,0.704887,6.281865,2.713726,-5.410695,8.948654,5.994502,2.415510,-6.294369,4.557857,-0.870015,6.872000,-2.118832,-9.109435,7.387604,-2.229147,-7.536402,-9.527210,3.179164,7.291037,-7.492475,-9.054598,2.297058,-6.806995,-6.323652,2.892552,-7.777543,-7.652828,-5.491966,7.248487,-1.599238,-5.718537,1.588171,6.133733,-4.257894,-2.818880,0.757961,-4.704596,-1.010616,-4.997982,-1.528974,9.756370,-5.259167,-4.776331,-3.873185,-4.882332,1.779405,-6.123326,3.463637,4.334319,-9.889430,-6.665158,6.785101,-5.245367,9.580543,-3.710765,-6.974057,-6.238567,6.193231,4.093402,-2.385920,1.089335,-5.385215,-4.784751,4.378069,8.285515,-7.961669,8.635774,-7.967474,9.616962,-4.061946,-8.832731,-6.678058,-5.948473,3.982524,9.471754,5.923972,4.430985,-7.599825,-6.063855,-5.155894,1.356274,4.784081,-5.901899,-3.159505,-4.848960,8.012646,-2.679794,0.128089,5.509482,-0.355146,7.353961,8.370955,-7.924505,-4.438397,1.918036,-0.437379,7.476818,6.230910,-7.835726,-3.047646,8.523075,6.387644,7.534248,-2.989920,0.673952,5.483333,-0.256449,8.606212,6.138041,4.354715,-2.968525,0.150546,-6.370822,0.165885,9.044485,8.634265,9.596030,-3.693381,8.084708,-4.063047,7.076945,2.005661,-2.118833,-5.973671,6.993391,0.982988,-6.767186,7.898014,7.669068,6.664651,-7.142808,8.140496,5.088471,-7.273843,-7.962630,3.782359,0.003270,-6.526222,3.076730,8.304200,-1.608690,4.752570,0.326772,2.122557,3.634597,0.250488,9.751747,-9.099182,-6.114215,-7.735755,7.142200,9.377385,-0.391187,-0.565730,-1.829063,-6.307958,-7.196081,8.801965,1.115955,5.312881,5.433226,-3.077819,3.214199,8.119913,-5.307826,4.197543,9.001139,-0.019265,-2.743570,-2.276177,-3.745016,2.189805,-9.377986,-2.765387,-2.433440,-3.194245,6.679152,-6.338124,4.294561,-9.623890,2.141392,8.504679,-6.953416,6.665401,6.206856,-6.448704,-0.191362,-9.955491,-1.988807,-5.339066,-3.638452,9.560635,-4.821787,0.271424,1.497037,2.107671,3.158290,-7.617576,-9.708097,-3.552975,1.985570,2.605856,-6.240582,-7.380079,-0.322649,1.895406,6.855228,-1.725791,4.030793,-6.288272,-9.956965,1.601712,-9.930599,8.659978,9.744335,-8.753916,-3.175566,1.009365,-0.441596,-2.354872,-0.836816,1.785184,-4.756872,6.099691,1.642018,-6.453900,7.481287,5.506159,0.809647,-8.254899,-1.701712,7.384758,-0.264242,-7.640859,-0.629151,-7.555602,-1.080756,1.756818,6.450725,-3.209474,-9.547742,-9.535984,7.479131,1.846940,6.266629,9.742177,2.589022,-0.233799,1.638647,-4.734473,8.982621,4.447220,-1.696290,-2.158164,7.652386,2.184480,-9.450154,-4.208239,0.548413,-8.231855,7.444909,9.546740,9.247995,4.416603,-5.502690,-0.671368,-9.992505,7.336130,-7.579623,-8.322216,2.134806,6.191914,-2.317845,7.844093,-6.083423,-6.218876,9.337227,-9.594077,2.392988,-1.782360,7.154076,-2.297504,-5.683036,-3.138851,9.202899,-8.310378,-6.089418,-3.036481,3.852397,2.650308,-6.969593,-6.306784,9.126697,-7.055759,-4.635323,-0.792479,0.601861,6.266022,-9.452458,8.797023,-3.562142,-1.679835,3.131933,4.671961,-0.548679,-7.284880,-2.269720,0.232951,5.673290,9.898720,-8.179345,9.994712,-8.788266,4.974386,9.325638,-5.353803,-7.709442,-1.074080,-0.838353,8.966186,-9.392569,4.371114,-8.476929,-9.515980,-3.203089,8.344061,8.222028,-3.191843,8.149472,4.190914,-1.844860,-2.167569,-3.808293,2.707285,4.910905,-7.809818,-8.135829,-8.025007,-8.360376,1.242729,-9.206567,8.185510,6.114168,4.706385,8.564330,4.350943,2.232595,-8.441855,6.825665,-2.103915,-5.794685,-3.791244,-1.757704,3.566934,-7.318956,1.811068,4.286899,-3.679758,-8.696956,4.205701,-0.449625,-1.374194,3.361665,-1.333514,-6.730513,6.524922,9.031931,5.065766,-8.961596,-1.950532,3.043220,-8.746766,-8.790259,-1.731352,-9.537856,-6.075312,-3.418585,-5.778595,9.303207,-9.804700,0.278909,0.937875,-5.846661,-4.016051,6.272609,6.497705,-3.891722,-1.247608,-8.936984,-7.684528,-9.688204,-6.915960,3.647385,-3.341918,8.245712,-2.641609,-6.536978,0.038943,-5.669873,-7.561721,-3.019832,4.170887,0.499005,9.601214,-6.815747,-7.052567,-2.455664,3.730614,-1.408053,-1.714954,2.830111,-9.740176,-2.390066,-6.083716,-5.924635,3.948218,-3.174380,7.331259,-3.896856,8.033871,-4.867595,8.305927,-8.551996,-1.637014,0.060863,-9.881593,6.073225,-3.325815,-4.964812,9.965955,5.549814,9.923695,1.498590,5.240079,2.189545,-1.359797,0.440138,-2.500829,-6.939448,-4.358089,-6.618197,-9.704944,7.591353,3.896572,1.795001,-8.271662,6.334698,-0.951745,4.870465,-6.851000,5.972271,-2.904281,8.871440,-7.270041,-7.013690,0.321259,-6.222193,-4.282551,-5.956652,1.555262,-8.252088,0.929446,-6.454523,-2.003900,5.254543,-3.835178,6.577537,7.394925,-2.416618,7.193291,-5.294820,1.501343,-1.979079,2.552040,6.540360,7.140133,-1.129332,-3.848362,-3.133960,-3.083308,5.181166,-0.677063,-2.537517,2.340641,-8.023236,8.427278,8.273125,5.939675,-5.797818,8.660094,9.618238,-4.713992,4.818248,-4.991756,4.779285,9.112749,-6.375220,-2.795145,-5.891943,2.384573,-4.913824,5.029923,2.124661,2.446048,2.907784,3.238068,5.282620,3.010241,-5.687790,9.208644,-0.813633,3.018114,-3.430399,8.512062,1.697608,2.074846,2.537435,-3.756929,0.251025,5.692390,-6.274639,-9.458051,-2.195765,-3.191442,7.473413,-6.919339,-6.824168,-1.071965,1.218106,3.460223,-9.903866,-7.888655,-7.230315,-5.157064,2.344405,-3.662181,4.867978,7.957896,-1.339710,-3.698513,8.018910,-2.517213,-3.166435,9.946237,-6.249991,1.058036,1.213381,7.025415,-9.715090,-5.815205,6.798627,5.312117,7.510263,-5.773190,-9.884574,3.718499,3.284464,1.374254,9.829088,-1.416980,-2.213375,-5.512208,0.931067,2.620881,-9.474980,4.256446,-1.883323,-4.911299,-9.179505,-7.067456,0.491970,-4.686035,6.545375,7.612147,-1.273636,-6.452696,6.870020,5.244173,-9.872454,-0.371441,-3.854297,-8.715128,-2.348874,-6.647615,3.470600,8.531734,-5.129202,-4.135191,5.092278,-6.197549,9.553807,-8.715254,-9.741626,3.021037,-6.574556,7.071007,-1.071378,-0.185068,-5.067130,7.902501,4.850054,-0.248859,-7.738336,8.937596,-0.291814,-5.755042,-5.205343,-1.829557,-5.866894,-3.728793,7.890617,2.022945,2.284406,-4.770993,-8.664773,-4.538185,-8.124983,0.682677,8.932082,7.628918,9.440132,2.742269,-1.489440,-0.680060,3.406238,-3.765711,-0.213075,-4.167284,3.279770,0.430104,-3.114647,9.534606,-8.710042,-4.357878,0.232455,-5.937789,8.716585,-6.168813,4.213353,-3.655895,6.349120,-4.835418,-7.021982,-7.985148,0.473995,1.474653,0.689740,0.858007,9.131403,1.875098,2.167827,0.569663,7.853563,-0.072046,-1.213679,4.772379,6.466345,9.573090,3.261077,1.932350,6.951027,-8.024207,5.882187,9.011319,3.731062,9.194784,-8.170970,1.776619,5.826712,-0.529967,-7.707671,8.579079,2.311087,2.853375,-2.237555,-5.074352,9.690057,-5.336188,-9.121723,-8.266315,-3.252821,-6.407022,-6.273851,-2.862103,3.710564,-0.149691,6.901976,-0.605636,-9.345868,8.242296,-2.882604,2.063804,-3.110633,2.398611,2.051584,2.704608,6.722863,-5.280757,0.089733,9.080799,3.924105,1.441853,-2.001045,-7.813299,1.762032,9.593831,9.603822,-7.439579,8.441198,-5.255251,7.917655,-8.107121,3.170781,-0.497182,-5.350504,6.226584,0.150220,-5.932902,-4.303484,8.494799,-1.579995,-5.183871,0.073116,2.680098,-7.641959,4.263762,5.391072,-7.854421,-4.571151,-9.831258,3.289611,-1.852221,-5.860149,-0.124275,9.506546,-7.855937,-9.007875,9.209452,7.217314,-3.465589,-2.133274,3.062520,-8.140948,-6.294093,1.292200,0.786235,6.489384,5.655054,-1.517393,-5.173250,3.294304,1.938776,8.850733,5.136355,4.160115,-5.551719,0.887304,-1.216962,-1.394296,-0.988483,5.167312,-9.027427,-6.983307,-4.501067,4.569019,-0.309684,4.314391,-0.334124,3.699569,-9.832708,-4.359967,-0.664345,-9.740369,5.738629,-2.339005,-4.662575,6.489933,-3.944232,2.598011,-5.959122,6.077430,8.032545,-8.847239,-5.711571,-2.673161,-4.011167,5.446896,-3.975399,2.292052,-8.175949,-7.006592,7.482809,1.388351,7.150271,-8.971710,1.620774,-4.070827,5.036425,4.243150,-6.666346,-4.228635,-9.781057,-4.156968,2.017927,-6.418109,2.070202,7.362858,-3.908191,-2.946426,2.207026,5.184306,-1.306255,7.629595,-6.142413,3.711668,-8.264330,1.391368,-5.446751,-6.199171,-5.746671,5.069950,7.986649,-1.597837,-6.646568,9.412286,-4.400991,-3.742529,-4.007100,-4.259821,-9.819458,-9.259946,0.882093,9.922640,5.673330,6.736659,-0.446926,6.105931,1.551695,6.616905,-4.082041,1.416228,8.982594,4.336907,-7.279365,-9.823431,-5.939214,3.022650,7.237489,7.451666,-8.566092,-3.096488,6.775650,-1.182486,4.648477,-2.522877,-4.499218,-1.696374,-6.023774,-2.728146,3.926853,8.282748,9.248357,8.735397,-5.982587,7.503188,-4.445723,3.446053,4.139125,-4.837906,-1.430356,-2.525115,3.450728,-6.623299,-6.563358,-8.278685,-0.867239,7.814471,-2.457952,-2.421559,0.842407,-8.431715,2.704257,-9.651268,7.406313,4.314132,1.424422,1.017869,8.007167,-7.976321,-9.742957,0.891614,0.947480,-1.843960,-2.586328,-7.875691,-6.299850,2.729044,-4.163039,-7.449923,-6.115329,5.606527,1.497687,-1.613309,7.403943,-3.342401,9.106502,-5.380282,7.380737,2.825226,7.216975,7.723085,-4.515630,3.213376,-6.176252,-8.268024,4.853458,7.971196,-9.706638,4.256287,-8.955006,1.221521,-6.312067,-4.255980,-9.102474,4.206388,3.399846,4.578599,0.750688,4.149705,-9.569788,-1.998744,2.454110,-8.171881,-9.704501,1.398377,-0.501321,-4.603339,-4.884790,-4.873025,-3.453122,-6.302022,-8.933722,8.167939,-5.660478,-2.037058,1.625435,6.723929,-2.636037,-2.460458,3.942429,0.741693,5.255697,-4.098324,5.563779,-8.903125,-8.182692,2.615159,1.600531,-9.784173,7.519657,-1.239084,-5.339699,-3.453328,-9.536075,3.172682,-7.753921,4.011051,-6.920554,-4.408331,-5.331172,-0.477235,8.600939,6.781090,-4.071312,0.721183,-5.399567,-0.985277,6.386142,8.155716,-4.095576,1.450126,-2.662849,-8.629173,1.171902,-7.711574,1.680306,-4.318604,-6.342325,3.652142,-0.990053,7.393393,5.418857,2.537400,-6.464853,-2.134304,8.971565,1.955068,-8.301400,-8.071712,-1.699431,2.192846,5.980968,6.705014,3.764620,4.669833,9.785234,2.648175,-7.536061,5.800273,7.813398,7.968397,6.554176,-4.193276,-9.653054,1.617325,2.614482,1.707233,8.978892,0.816848,9.152797,-5.848493,5.127966,6.155255,-2.916412,-4.245066,-3.674542,-8.236821,-6.475811,4.829048,3.795541,-1.192622,8.775264,-3.839059,-9.694605,-3.151273,-4.624278,-2.886641,-1.830082,4.074330,-6.704021,-1.082984,-0.713808,-2.523294,-6.293996,3.285163,7.816015,-5.226798,6.943686,4.433387,-1.458982,-9.122287,-2.558795,-5.220660,-9.293698,5.074560,1.320504,-4.830940,-6.510295,1.234803,-2.252741,-5.242016,-7.547725,3.425456,2.778310,2.934490,-5.281080,-3.377603,-2.484880,9.888463,5.309069,3.031139,-6.857416,-4.333674,-2.770695,5.968796,-6.262816,-2.468586,6.178071,0.867026,-5.932555,-7.259863,-9.564749,2.013904,-3.414731,8.026741,1.841007,-9.202049,-3.058416,-5.729843,-9.755145,-5.593200,-6.258595,8.667600,-8.747646,-0.296816,6.653739,0.094650,-5.918522,-2.612701,0.447509,-5.852639,-1.642223,-0.618196,5.401056,-4.732641,0.143639,-4.871377,7.768945,0.388242,-6.611759,4.243431,-0.464730,7.365923,4.057783,0.143842,-7.910384,-3.363257,7.328535,9.260109,2.572075,-6.327975,-0.384963,-7.007472,9.813472,0.697136,-9.629724,9.791401,3.477792,9.238507,3.484808,9.467157,-2.845849,-0.603791,5.978744,-3.658328,0.866107,4.958519,0.188248,-9.554721,0.884265,7.388852,-7.801610,-1.226176,1.103774,-9.794933,9.746966,-7.912232,6.237158,1.505754,2.529747,-0.437115,-8.806844,-0.525672,5.792505,-1.005802,3.202446,-3.026463,5.082138,7.913768,-1.945433,0.807682,-3.123751,8.664755,-5.750955,-5.631034,-3.434781,1.462262,-7.116524,0.249698,-8.472452,-6.278567,2.569771,2.529507,0.694960,0.291570,-7.070161,2.799315,5.833657,9.914007,3.858026,9.814685,-6.862196,7.529741,-8.958103,-7.824050,-2.780084,-6.822399,-5.268285,-8.312438,8.651501,5.856866,-0.431074,-5.066824,-9.263415,-0.662765,9.898655,6.825639,-8.826110,-5.470739,0.489699,1.824344,5.954265,1.060123,8.770809,2.371820,-8.949410,-1.817526,-4.673410,-2.772810,-9.449246,-3.926050,-7.401939,7.738824,-2.990182,2.772117,1.881983,-8.758410,9.105844,-9.257936,4.946146,9.533881,-2.139500,3.863978,-0.580326,3.151054,-1.547099,-6.226053,-4.486542,4.147904,7.011725,-4.280426,5.031800,0.405484,3.284386,8.810782,6.457729,-4.800083,-8.712621,-4.326961,5.042682,-3.206914,-7.254241,-9.329603,-2.754377,2.465525,-1.388244,-9.538482,-2.357575,-6.018686,1.007592,0.801018,-1.949310,4.887606,6.193897,1.249757,3.610979,-1.264059,-4.448775,-0.269165,-8.068729,-6.564020,-8.214895,-7.161021,-3.546994,-9.316689,-8.658756,4.891546,7.586783,3.570745,-2.223150,9.265454,-9.860072,6.465146,-4.514254,-4.216164,-6.807183,6.219880,9.151013,8.173074,4.826962,-3.629804,2.076561,-1.516473,-9.521770,5.322749,7.358987,-0.203426,-0.390809,-9.879880,-3.711524,7.660669,-8.053232,0.452775,-5.534920,0.067188,-8.952937,2.744150,3.819527,-6.117377,-0.784609,9.996112,-8.470037,7.334239,5.799316,6.057604,-2.577906,-6.502042,6.017015,0.525541,7.594323,3.051779,-7.358282,6.780459,9.598881,6.990204,-3.291863,3.790977,-6.084891,2.891545,-9.101247,0.830592,-4.352161,1.740840,8.110529,6.723037,-8.600784,-4.429403,-0.982825,-1.709409,3.357564,2.491313,-6.909774,-8.770550,3.219298,3.880653,-8.196756,2.246733,-8.414061,2.179248,1.365187,-8.986966,4.639404,-8.852115,9.280884,9.359400,-1.787236,-7.085058,3.214744,1.484779,-3.442607,6.693773,-7.930264,9.290274,4.784514,-8.816698,-0.886799,-1.913913,-3.958816,2.783575,-5.123132,-4.584077,1.039106,1.701915,-5.075379,6.336439,3.327249,3.792667,7.496164,4.311433,9.049190,8.369495,-3.377636,-4.288001,-4.999827,-5.577375,-9.268793,6.903376,0.302063,1.651715,-7.628074,1.415344,4.293911,8.168667,5.978068,3.509502,-6.094092,-5.032410,3.206131,1.035835,-7.005433,-0.490167,2.178716,-4.747354,-3.358061,-1.589139,3.684456,3.249765,-2.231913,3.525110,9.038359,7.145806,-5.832266,-1.125790,-6.140063,8.475071,-8.774440,6.769180,-9.848523,-5.111459,3.927139,1.688565,-6.036039,4.785775,4.005515,9.481925,-5.815541,-8.912406,-0.210714,-8.807607,3.244071,-3.554228,9.132958,1.598968,4.691324,-3.415261,-6.679333,9.100354,-2.119869,8.121328,-0.173722,-1.443974,5.972768,7.716403,-7.364622,-6.334847,8.287082,7.811444,3.009376,-5.364993,-4.651634,2.068166,-5.970065,-6.331704,-2.500498,-7.546450,-1.604174,5.024174,-5.924107,2.927850,-7.115222,-2.444285,-1.474005,-8.371493,-4.327520,5.584559,0.298830,3.101643,6.468479,9.672632,5.814186,-0.081728,-6.520163,-9.062004,-1.048694,1.439258,6.199327,0.330311,0.232295,8.845174,-1.909263,7.186710,-0.667755,-3.874510,-6.653138,8.823028,8.051885,0.203907,9.865166,-9.097364,2.113587,-9.078561,6.186452,8.483089,7.039943,-6.080033,9.974869,6.575081,-6.275384,2.092085,9.649859,8.775784,0.649860,7.035701,-2.535292,-3.214343,0.420421,-0.720157,-4.815995,-1.564429,5.932922,-2.639265,-4.839740,-5.386848,2.076252,1.724214,-7.744759,2.700832,1.337768,-5.743611,5.115409,1.626999,2.499512,6.238773,7.036579,3.059683,4.516821,3.889864,5.514156,-6.650403,-5.110418,-9.562365,-5.027743,-7.261853,-5.237655,3.125412,0.470445,-0.234654,9.830980,9.278076,9.838233,9.990598,-4.090902,-9.532162,-8.246333,-2.245453,-9.701787,1.383189,-8.639902,-6.035040,-3.026752,-8.583520,8.859425,-5.434825,1.246330,7.809028,-8.547095,7.132594,-5.192478,-1.006368,-8.092196,1.814684,7.368923,-7.037329,-6.392804,-5.972563,-3.213226,-3.744275,-8.935503,-0.074215,-0.185831,-2.727905,-9.842819,3.956534,-6.271891,2.417651,-9.489409,4.811016,3.771898,-2.273011,8.449731,-1.774719,9.408329,3.132462,7.846632,4.306968,7.640767,-7.317019,4.450041,-0.814996,-7.998500,4.204874,-9.153970,-6.664504,-5.315454,3.609922,-1.439426,1.476660,4.475256,1.276383,7.889462,-3.919774,-1.304689,-3.199762,4.223282,6.232468,8.041774,-6.585969,-8.173620,5.625346,6.083972,-4.804611,8.697508,-1.532030,-4.826371,7.513503,-5.160278,-4.802850,9.170492,1.339449,-7.326028,-7.641498,3.862629,5.286246,1.314234,-1.256155,-5.896854,-0.197153,-6.760808,-6.798523,-6.632793,-0.685899,9.221846,-9.039393,-9.961589,2.554309,-8.197763,-3.823847,2.078956,2.939983,-8.990188,8.818063,-2.930175,-7.257573,-4.617549,9.248479,4.530815,-6.604322,1.237140,9.766895,-9.953609,-9.025124,-8.688751,-3.098766,-8.883280,-9.326516,5.058141,3.486142,-3.003746,-5.183197,-4.552058,6.222203,-0.662386,3.550677,-2.347414,4.558429,8.377574,-4.580549,-3.261674,2.360403,-2.834175,2.907444,-4.564234,-4.651440,1.342759,0.017920,-1.636058,4.467301,-7.337935,-2.326639,0.599688,0.221991,6.333763,-6.255375,-1.020244,4.024714,6.103447,-8.837435,3.283309,-2.754256,-9.134707,3.121249,2.291939,7.734163,7.042510,-7.849538,8.551181,5.492746,0.467524,-5.047457,-8.319763,2.697571,-9.079132,9.933787,-3.107771,-5.164271,7.976481,0.452904,-0.518925,5.299790,0.632122,-3.505531,7.917280,6.156675,1.325705,2.511997,9.154025,-0.828786,-5.997163,-8.946416,9.064120,8.609438,-7.932789,4.799845,4.258940,-1.502544,2.120118,4.375604,-8.469639,2.646345,-5.424094,6.060174,5.363622,-4.470800,9.143514,-0.485524,4.254632,-6.131352,4.473847,4.694337,-0.159599,7.999855,-6.521936,-8.606574,2.983348,4.815726,-8.380665,-0.402474,-1.150039,-9.085722,6.428044,-8.046781,-8.510653,-6.319166,1.106062,2.453074,1.789216,7.460723,4.695694,-8.400575,9.802276,5.683001,5.065510,-0.541630,-5.067637,6.397266,0.415786,-2.199286,-8.433342,3.870212,-7.407664,4.076981,9.397509,-1.084204,9.114758,-6.265013,-0.029951,-2.134185,6.126272,2.897151,0.824027,9.767026,-9.171530,4.014697,-1.131724,-1.523950,6.810309,-9.382228,-4.117877,2.651751,2.818493,6.010455,3.407851,4.533663,-3.040508,-4.277008,-5.156108,-1.899765,-0.201371,3.209776,9.642155,7.608636,-2.652918,3.096587,-2.317527,-4.808004,-6.544182,4.546312,7.548785,-3.401756,8.671844,-8.735209,-0.837252,5.069050,-0.851553,5.313083,-6.011949,-0.504842,-2.733945,-3.677099,-0.468344,6.590870,-0.223881,3.565124,0.105146,8.446766,-4.373803,-2.334729,-4.567988,4.325048,1.640236,-2.788611,-5.906574,-1.298486,5.997339,7.478005,9.987768,-0.436887,-7.712719,1.127755,-3.061791,-2.686920,-8.938500,5.828273,-9.670897,7.863188,-3.419409,-7.671514,-5.707658,0.241858,2.285702,-1.021513,8.482401,-4.807337,-2.158712,-7.853288,-1.112801,2.856443,2.952865,8.334687,-8.382909,6.549932,8.322256,7.792521,-1.764097,0.452417,6.400476,-5.002758,-4.634534,-4.614687,2.325124,3.672375,-8.694793,-8.183609,-5.893077,0.487601,6.938473,4.219317,-8.578815,-0.724052,1.128201,-8.155887,9.837911,-4.483064,5.284960,-9.869681,1.615436,-6.018200,3.206684,6.856375,4.322623,-5.485773,-2.494043,5.743422,-7.891822,1.342707,5.510333,-5.699245,3.905176,-0.216273,-6.168648,5.500043,0.793709,0.435638,-8.195195,-7.642157,9.213395,-9.673129,-9.689587,9.876714,-9.917370,-8.740317,-2.079535,-7.550337,6.197006,7.183334,-4.426330,9.548089,-9.671282,-6.086977,-1.191686,-9.473863,8.084472,7.150163,-8.027415,-4.702452,9.577036,-2.481955,7.998807,9.408372,-2.308442,-7.872831,8.145009,-2.923846,-6.575372,2.537750,5.503992,9.334539,-0.466253,-7.101444,5.731012,3.670611,8.803074,-6.837974,0.089550,-3.344565,-5.444405,-5.972473,-9.588979,-0.606918,6.983248,2.340029,7.372792,4.212063,2.681918,3.738191,-6.556507,-1.963460,-1.910785,-3.586800,-4.585899,7.466285,-0.813512,8.831355,-9.485640,8.296968,1.383904,-8.961590,3.406342,-9.318825,9.525121,0.546590,1.836100,-6.798414,9.622701,6.159759,8.211116,-4.282507,-0.940056,-2.939247,5.144443,-1.846589,4.477773,-7.825299,-6.371517,0.876317,-4.314902,3.766916,-1.629121,9.659045,-7.127619,-6.539094,-6.258928,9.988270,-6.763808,9.180762,-7.914004,-3.928729,6.129075,-8.333066,7.451015,0.375931,4.346048,9.512717,-4.548256,7.589344,2.679546,-9.098849,-9.494504,-8.598149,-0.672928,7.374223,8.599032,-0.963727,-7.329954,-5.253060,-6.252260,6.878545,-9.084395,-6.351361,5.517967,-9.287244,9.927550,-4.169408,-5.916242,-9.375064,8.325391,4.702789,0.866867,1.026122,5.560217,7.082179,5.938048,8.344528,-9.895900,4.967431,8.114534,-4.985949,-2.560138,-0.195829,-9.299236,8.652411,-2.995960,-6.708125,-0.754882,5.611562,-9.387618,-5.060257,5.127948,1.155311,4.484165,-2.669211,-6.418091,0.275719,6.901832,-2.722367,-0.428523,1.405116,-3.285098,-4.044007,6.907768,-8.413743,-5.243898,-8.278942,-6.759967,9.368682,-0.136657,-0.842022,8.900262,7.515729,-0.729492,-2.244511,-5.098486,6.087704,0.221528,6.045214,-4.784974,-6.251553,-8.448431,-7.622882,9.361894,-2.710475,0.037425,-8.365821,-7.848048,-2.535971,8.349571,1.717876,-8.977688,5.285238,-3.927976,7.813705,-2.173138,-6.503220,-0.655465,-0.162227,-0.593511,9.446249,5.612237,-6.929481,7.261212,-0.524622,8.402894,-1.914365,8.427013,-7.088919,9.114109,-7.101381,0.024185,-4.771859,9.577278,5.037908,-7.416128,-5.080373,3.903558,0.714357,3.753909,8.877007,-1.827869,-9.367593,7.677201,2.086427,-5.642398,9.350396,-4.501423,9.780586,-4.647708,-3.645564,2.652814,-3.825890,7.515493,-7.606017,-6.795159,-7.441697,9.527278,-0.730246,6.329487,7.071910,1.450237,2.188487,0.221079,7.330107,-7.335786,-9.849991,-6.036791,-5.457176,-9.181600,-4.995810,-3.768507,8.480822,-5.041360,9.450567,-7.113599,1.510945,5.881388,2.970228,-7.148210,-8.614806,-9.883481,-2.066674,7.743579,0.222006,8.037571,-7.277317,-7.170571,-8.981947,7.777363,-3.603094,-1.193510,2.720268,-3.318448,-6.844977,-9.065920,8.798815,9.157030,8.569786,-0.384219,1.722969,9.813979,-5.952039,8.867264,-9.658326,-6.321435,-3.805323,-7.692956,-1.682426,3.174371,6.529886,4.657567,-0.343994,7.624560,0.583721,-4.225203,0.286279,6.996241,1.380165,-1.928969,1.051663,-3.109649,-7.180974,-2.932575,-7.988906,9.926488,0.533434,-4.960220,-7.966975,9.999165,-6.521353,-1.809675,8.932351,5.196014,-5.073082,-8.800903,-5.130532,-7.048556,-4.445933,2.597528,-6.485598,-6.611153,5.046040,3.480510,-1.498976,1.893782,6.358867,9.762992,8.542707,3.345659,-0.633980,-1.015127,2.837724,2.465857,9.491774,-6.464696,-1.004644,8.422252,4.941759,7.418560,2.054316,-9.572634,-3.393559,-4.270980,-8.352561,0.662036,5.851393,9.601246,-4.145298,-3.985277,5.252956,5.286065,-9.191427,6.092052,-9.355464,1.432355,-0.312988,-8.618836,1.425165,-4.058447,-1.888221,0.681527,2.791474,-3.452119,4.191846,1.834688,7.698596,-0.058006,9.784304,-3.978759,-1.507196,-9.358611,7.497866,6.704172,9.003403,8.592396,-6.835811,0.002300,3.370236,7.043472,5.726203,-7.050590,-7.095169,-9.675265,-4.064538,8.321773,-5.406843,9.639984,-6.463821,5.935248,7.866611,5.276223,1.908412,6.163263,2.102497,6.612834,-6.641133,5.879548,4.043319,-4.941444,-8.498510,-1.333932,6.517297,1.237975,5.779384,9.459726,9.644287,-1.654588,-8.742668,2.163630,-8.085134,-2.307747,-2.881486,3.653900,1.999056,-7.039668,5.017865,-0.741072,-8.154920,-8.543170,-9.335767,-0.446872,9.024103,-2.292960,8.355124,2.564311,7.387485,-4.379553,2.690397,1.271002,2.663494,3.929168,-5.836490,-1.990395,7.178111,-2.671021,-7.668557,7.014707,6.783717,6.044342,5.067971,5.412966,-1.597800,7.853504,9.479990,-2.421671,-3.331689,-8.305652,-3.073292,0.017592,4.978259,6.804198,1.218828,4.660538,3.015221,5.423694,1.627136,3.508379,-2.131909,-5.663206,9.403792,-6.208189,-2.016558,-4.934043,8.655214,-5.463358,-7.096471,2.053107,-9.185772,-8.378260,2.145476,-9.502415,-1.315398,5.076853,-8.248379,2.640973,-4.404119,6.247832,-2.602220,2.811482,-6.608422,-9.451899,-3.753580,-8.996351,5.663800,-1.882228,-3.452565,0.443056,-1.756311,8.559647,-7.363318,-5.437981,-5.066165,5.781239,6.134355,9.173850,-0.035685,-4.644885,4.753643,0.821644,-5.242153,5.516898,2.155278,6.400646,8.378818,-0.270946,3.067822,3.132586,3.128495,-2.994388,5.341811,-5.152074,-5.384127,-9.621932,5.941544,-5.563276,9.062993,-8.375040,-1.823532,-7.358960,-0.815230,-6.904137,1.473624,1.878635,-5.259830,-3.466838,6.264050,-6.069324,7.805185,7.880937,-3.570285,-0.682836,-9.970536,-6.102112,4.349181,-8.171706,-6.008474,6.648181,-1.998383,-2.699577,3.774449,9.568802,0.352149,-4.521187,-6.521818,0.482160,9.708000,3.619802,-8.411829,-5.200896,-8.240895,7.326603,3.184071,0.633696,3.804390,3.121935,-4.359544,-8.642538,-7.477666,-5.506011,-2.067571,2.151332,-7.000002,4.155478,6.311814,-7.728963,2.721690,-4.813681,-1.978990,-9.508510,3.211504,-1.138207,-2.331193,7.227765,2.901473,-9.348463,8.916860,2.699700,-0.581631,-5.794597,4.980460,5.400900,-0.714228,1.006371,6.843034,-8.292405,8.443261,-8.478155,9.482438,-4.481088,-5.767180,3.474900,1.208171,3.039841,3.058012,7.372181,-1.954900,2.527461,-5.802616,4.640810,3.046972,-5.548867,3.684123,-1.347036,-7.164025,0.284704,7.577244,-7.922524,-1.004111,-1.809615,3.380324,-1.873838,3.745617,-3.901783,-9.803724,2.816407,2.733670,8.450559,0.301510,-3.678907,-4.852791,-2.391148,-4.370676,-9.490329,-9.671972,-7.555029,-0.552977,2.645943,4.933459,8.489778,6.505668,1.800325,-6.353406,5.665203,-5.429331,5.682620,-5.040695,4.810346,-6.377058,7.185219,-6.267232,-3.812386,-0.436989,-8.580348,9.147448,6.354375,1.183227,-5.135957,0.441666,4.133586,9.561477,0.812151,-7.072213,-7.334170,-0.578077,7.667034,5.622449,-3.282650,0.910206,7.573768,-8.818432,3.822821,0.494190,-9.807329,-1.502266,2.816965,-6.517559,3.837373,8.276608,-2.060334,0.678080,-2.588225,4.632134,-7.939827,-8.163648,-5.545396,-5.397727,-6.700455,5.652334,9.632135,-5.182279,0.927943,4.651124,6.647232,-4.360920,-7.090030,2.029078,-8.643108,1.157370,4.355728,0.684747,4.266722,3.480445,4.379313,-7.541158,-9.690685,9.684363,8.970923,-2.850138,3.867037,-6.894610,-1.450294,7.364048,0.413796,8.090927,-0.909076,-4.607053,3.564063,6.954615,-1.452688,2.940833,-1.837977,-7.679743,5.530062,-4.619539,7.381810,-9.648707,-8.996348,-5.281868,3.135534,-9.334950,-2.042214,7.941025,-5.651425,7.366522,-7.787684,-3.920395,2.576476,-4.591652,4.939281,-6.245526,-5.513344,4.868151,-2.152475,-2.820027,9.208435,0.358075,4.811296,9.763348,0.655077,-6.293539,5.049716,-0.270401,6.650947,8.972055,8.870814,1.229182,7.501655,-5.136417,-2.630648,8.929504,4.916875,-5.039251,7.868776,-0.738046,-9.844875,-3.804161,3.421074,-2.166305,4.167467,-5.626246,3.576274,-8.235341,-8.941598,-1.349462,1.684260,-2.298354,-7.093336,0.197161,0.559833,-4.814074,-4.850128,9.782893,0.382258,-7.684202,-0.398099,0.219041,-1.025686,-0.529497,-7.097088,-8.775977,-8.158236,-9.354675,8.446597,-3.150063,-3.729191,-3.113861,8.587380,-4.423651,1.786507,6.000706,9.468347,-7.748548,4.953677,-4.868793,8.289566,1.463435,-3.634670,1.011938,-5.772720,-0.316786,-7.638830,3.235473,-9.388496,8.021059,8.019995,4.708985,9.825003,-7.912977,-3.768519,5.800946,1.321403,8.891791,-9.811443,5.238317,-6.418545,7.177482,-4.508094,-4.841013,7.615444,3.201872,8.855504,0.040745,-2.186983,0.097148,7.179903,-6.165206,4.496300,-1.390678,-2.995465,-0.876817,6.227858,-4.243154,2.363073,-5.151365,-8.165409,3.222750,2.824477,-9.285490,-6.973376,-9.341605,-0.943361,8.024392,5.521869,-4.542433,3.001043,-9.343084,-2.951368,3.003526,-1.707981,-2.483739,9.646549,-0.857083,9.336045,-2.018810,-5.248803,8.995994,6.645409,-2.155004,-8.997156,8.014752,-6.783897,-7.769274,-4.994396,-9.968779,4.369594,7.730183,-1.388550,8.832108,-9.417427,9.875420,8.089603,-0.849694,8.942736,7.147274,4.266111,-5.945991,-8.485680,-1.655557,-4.855019,0.849921,-4.153509,-0.495264,-7.155107,-8.346722,4.501310,9.676636,-3.535923,6.624079,9.055882,0.970294,2.903075,-2.170639,-6.221495,-2.628271,5.325315,-5.786422,-5.703740,-2.733783,1.278028,-0.875689,-5.840591,8.616549,3.373207,2.466012,2.783482,7.416258,-0.799163,-2.867996,-5.875829,4.973658,7.036765,6.150326,-3.682435,-8.396127,-4.539430,-0.542359,7.697832,8.573326,-7.220265,3.192694,0.329741,9.349936,-7.944977,-0.029114,-6.329017,-1.001247,-3.748942,-5.273366,9.776356,-0.095622,6.430960,-6.743883,-0.534627,0.325146,-8.697772,-8.573700,3.373171,8.671840,7.132328,-7.964484,1.684325,3.370749,8.028551,-8.672680,0.144194,-8.384864,3.549163,6.219560,6.187862,9.562821,4.770961,9.713198,1.198918,-6.076393,6.293685,-8.670022,8.655875,-3.209752,9.592051,2.421822,7.733218,7.931662,-7.340065,-5.129559,6.365835,-6.910824,3.939256,9.118893,-2.347307,0.619526,7.391315,4.290032,-0.935835,3.983410,-5.431882,-5.892449,-3.155679,4.533500,-3.519436,-0.642558,5.715824,-2.437057,2.637634,8.506447,4.552218,9.434291,-5.076608,3.922131,-6.256281,3.065802,6.184283,-5.437546,7.399512,-2.533027,7.838224,-6.314014,3.577806,9.159949,-6.290148,8.167220,5.031718,-6.125965,2.398641,-7.845100,-5.855198,-7.624843,6.257612,-0.402855,-8.233175,-6.322292,7.791067,-3.974340,2.421840,7.218123,-3.842953,4.558757,2.959582,-2.974984,8.355844,-0.521312,-4.199233,2.330904,4.604553,-7.357457,2.903499,5.186957,1.993475,9.670927,8.641940,4.568278,1.135360,-0.977859,-3.728247,7.493345,1.172406,-3.565136,5.355657,-5.693935,0.522949,-1.640193,2.210605,9.620549,-5.893495,-1.381363,-2.975962,4.874406,-8.278427,-9.237845,-7.651920,2.774455,-5.957561,0.462604,5.143117,-2.205459,5.437792,9.281199,8.633252,0.258752,-0.642777,5.170249,5.379893,-5.440767,-2.970788,0.875265,6.655579,5.191907,-6.168256,7.255757,-7.401999,-6.527469,-0.941107,-1.073681,-8.824840,7.092073,6.775160,7.878172,-5.248872,4.346776,4.778784,3.881399,7.317166,-2.419258,-8.087418,0.064712,3.176374,-7.268725,-6.640150,6.390608,-9.584355,3.259270,-6.293298,8.631272,-3.110930,6.578755,8.482209,-5.967702,6.575274,-6.545455,-3.755706,-3.320433,4.836665,-9.640368,-9.296872,-4.986177,-5.613238,-5.634589,7.907211,7.632822,-8.161920,4.709923,-1.061976,-1.574754,-0.550664,4.623951,0.362128,-7.483090,-3.631761,-0.877864,3.280228,8.246556,-0.782330,-8.223761,4.556051,2.097619,-5.287387,0.268100,0.418469,0.161382,-9.094473,-4.690191,-5.193378,-7.883423,9.970792,9.804791,-9.303856,4.937577,8.180888,-6.758617,7.878389,-0.929549,-8.033212,-9.287205,-5.517684,9.140054,-5.321826,-5.952600,-8.913349,3.157553,7.714106,-2.452310,-8.392736,-3.717717,6.846256,-5.359057,-9.928379,6.382149,5.851410,-3.577752,5.714176,-7.806707,-5.507216,-5.573475,-9.401130,-6.878468,3.632719,7.831724,-0.919230,3.985309,-0.798040,6.797704,-6.561801,4.891717,-9.036262,6.997272,9.428411,-8.306916,-3.642327,-9.550938,-6.400426,-3.399111,-7.886102,8.218533,5.800393,-4.099100,5.555308,7.546986,-1.686359,0.247249,-3.380990,-3.703883,-7.841372,6.625093,-9.768037,4.200828,0.645116,-0.588590,9.649720,-4.064727,-2.213776,-1.313408,-6.106727,1.217266,-2.792799,-9.409558,-8.202159,-3.278139,3.339680,9.752166,-9.013368,-2.737311,2.227246,1.475945,5.979602,9.260311,-3.408858,1.102793,2.879844,-7.176832,1.060664,5.601139,1.653030,-8.241636,3.793521,-6.294274,5.433992,6.788797,3.301663,0.775518,1.009225,-1.088401,7.145769,-8.567976,0.942074,-7.639108,2.182165,-7.347015,-1.059824,1.902527,-0.577372,1.556646,2.498744,-8.308015,1.004395,4.223258,7.329304,-9.995965,7.794982,5.228906,9.903238,0.913085,7.103993,-6.513205,-2.714294,-0.797764,9.927064,-4.846036,-9.347881,-0.743191,9.822010,-7.889600,5.699212,5.165149,-3.195978,7.711117,-3.623641,-4.281100,-0.355771,2.382648,3.464809,-7.298823,4.161634,3.077047,9.081997,1.038152,7.289615,7.912164,4.781135,7.686211,-7.554985,3.178692,1.638753,-9.153241,-7.075567,-3.042643,4.733216,9.990197,-8.717028,2.285771,-8.717686,-1.636908,-4.333642,-5.906110,-9.202397,6.096374,7.315184,3.694703,9.046949,-8.995006,-5.564332,7.943674,9.495212,-1.697272,1.724985,-9.635861,5.884936,3.877565,-6.530946,5.701531,8.622369,2.135235,6.911764,0.674951,2.352825,3.446213,-4.619245,8.097661,3.025500,6.737722,1.397310,-9.669353,-8.772389,2.743385,4.834176,2.369321,5.222097,1.517141,-3.149092,1.988298,9.958459,8.945824,5.286441,6.695536,-5.867879,4.718938,-3.211908,-8.825438,8.168129,-2.831559,-8.441824,6.435214,-0.059777,5.322946,8.449175,-9.323123,7.296567,5.871068,9.671195,6.700194,4.236299,1.646194,-8.006063,8.331828,2.509178,-1.628114,8.790661,-9.048772,4.831526,-9.660056,-5.948575,0.778587,-7.579992,2.843221,1.449886,-3.677920,8.655157,2.514725,0.380621,-2.176570,-1.607156,5.138942,-5.845805,7.171514,3.584712,5.363664,9.098704,4.867205,7.148385,3.429212,6.053758,1.807111,5.340556,-5.080690,5.024706,-0.217556,6.547073,-9.122705,3.427163,6.576281,0.468023,-6.960952,2.055735,3.251866,-1.597462,-9.592943,-4.323913,0.260189,-5.343903,-3.290435,-7.864151,3.936019,-0.541414,1.602207,7.231229,-1.726340,5.338364,7.172468,-9.629130,2.078499,7.268295,-7.195755,-8.588458,-1.904786,1.507081,-4.721840,7.766473,-7.028508,9.241387,7.654602,-0.263745,-8.817412,-2.739891,5.126761,-1.860887,-4.046065,-7.574607,8.540846,-1.005020,7.212434,-4.774277,4.273105,4.202134,-6.220612,1.627908,9.182728,2.158842,-5.823696,-5.507459,3.885645,-4.782439,-2.695580,-0.956417,3.977857,6.854009,2.339357,0.521527,7.278193,-5.593399,1.519497,1.839733,2.213748,-3.644115,2.158050,4.996239,8.891440,-3.617151,-4.445827,4.762395,6.116181,-3.444322,8.530187,1.361604,-3.658079,-6.265289,3.462814,2.631082,-2.048663,-1.923406,-1.061789,-5.488544,-2.834568,2.912694,-9.315512,-2.761767,-7.267762,-0.802924,-0.891777,-9.645218,3.315674,0.669824,8.015794,4.712747,-8.897641,8.570585,-3.765616,2.464252,-9.527426,5.812923,4.242037,-6.207871,5.044390,3.617473,-6.353483,-5.476906,-1.406990,-2.389557,-6.611635,-5.908965,-6.903889,4.505537,1.502813,5.180081,-4.644725,-6.647384,-0.116799,1.084885,8.327057,-4.254329,-6.567243,7.183180,-5.497442,-9.514812,-7.057435,3.558568,-4.184448,6.590428,0.117490,0.797460,6.750837,-8.247468,-9.153644,1.251595,-0.017818,9.897385,2.131227,-4.065522,5.771687,-2.030045,9.075250,-4.477619,7.898243,1.802131,-9.905348,-6.565098,4.649384,4.503464,-7.516851,0.666589,-7.079508,4.819064,-9.962845,7.735104,1.730165,7.829461,-3.541369,-2.180149,7.282293,-1.039324,9.359330,7.591377,2.758880,-4.387017,-6.890758,0.822060,9.702567,-9.553740,-0.362681,9.240174,6.154392,-0.827477,-9.897040,0.422971,-8.098484,4.581681,-2.481863,-8.577185,5.362363,3.681377,4.173288,3.947631,-7.683586,-7.463801,4.972148,-9.363284,-5.582748,-6.787665,5.007372,-9.772922,-0.664547,3.907582,-8.295586,-0.120372,7.823024,1.678414,-5.645752,1.868680,-6.878497,4.927767,7.142495,9.837973,-5.769399,-0.179626,9.459775,-0.691576,-8.932501,2.361343,5.303203,-5.186603,8.675538,9.571299,-9.146146,-8.398167,-2.049276,3.057952,4.613585,0.355517,-7.970688,-1.441339,-7.477563,9.684784,-5.998880,-6.819665,8.223304,-0.014080,-1.460812,-3.245019,-8.337711,-9.188849,2.684654,-4.464617,-9.411261,-2.281296,6.684493,-7.224154,1.594683,-6.001274,-5.728030,-6.902438,-6.688201,0.568356,-6.687297,3.135184,-4.257288,-7.346606,9.955226,0.374839,-5.705021,3.774706,-8.112788,-2.296356,2.816352,3.337188,0.491968,9.000800,1.999625,-6.659959,6.899592,-8.944114,6.807011,6.105202,-3.915318,-0.139853,-7.756426,-9.375189,-3.184377,9.158486,-5.768927,1.090918,-5.978615,6.581441,2.309179,9.211860,2.640809,2.565553,-0.797865,-8.619235,6.213577,-6.900922,-2.363170,-6.587172,3.698225,-2.583201,-7.215743,1.756796,5.138228,-6.480970,-7.011531,7.777334,-3.010234,2.333113,5.112540,5.855874,-7.519362,-6.685368,-9.562858,1.170271,-1.966164,5.442077,-2.718212,2.416894,1.725414,-5.759517,-5.398397,-7.348158,-8.606890,5.276392,3.046334,-3.814199,-8.086259,-9.105442,8.489020,-4.594477,8.188303,4.071667,-7.559118,3.974481,-6.285994,-6.599885,5.405372,3.657739,-2.002999,7.912945,7.254517,9.737376,0.634370,8.407096,-0.025086,-3.650742,5.543121,2.446001,9.242300,-4.592112,-1.708249,-2.327711,6.245394,-9.879301,-0.677784,4.905708,7.095233,-3.857888,-5.214665,-6.302720,7.645516,-4.434345,-5.138543,9.891924,9.620494,3.185882,-2.513625,0.204506,-5.203351,5.285285,-6.773980,-3.469319,2.940738,-8.826322,-5.694169,-5.195193,0.908387,2.031489,-6.358954,4.519092,-8.010050,-9.561058,-5.292877,-3.667100,4.262523,-7.664019,-8.210289,2.967892,0.173090,8.181668,-2.416213,4.269280,-1.782843,8.932079,0.999037,-3.427694,-2.105937,-7.698322,1.563046,2.659772,-6.697958,-3.082184,-7.050204,8.793932,8.877553,-8.989928,-7.698466,7.841860,-0.007979,-1.275024,-4.484091,3.459137,5.593102,5.556690,-4.897911,9.417345,-6.610009,3.323448,1.065233,-8.217388,9.196635,6.425039,7.772557,-5.271930,3.355732,7.530390,-0.433188,-5.400549,8.041185,-7.356892,-4.772055,-9.265438,9.900407,-8.423187,-9.928526,2.750333,6.282450,-0.803842,0.991472,-9.734243,7.461945,-0.749097,-0.099648,4.705530,1.383311,3.388238,0.801472,-3.291676,9.136548,9.001582,-3.772491,0.605338,5.030637,-8.478712,-3.831631,-1.572180,-7.662366,7.848040,6.262723,-0.268823,-8.958285,2.850514,-1.673930,-1.718148,-2.889780,9.930724,-1.934286,-1.116189,-1.657601,0.995982,9.934803,-2.115824,-3.341822,-0.578525,-2.763557,-3.003356,-1.868910,-1.277821,-9.073762,-5.777278,2.447800,3.510777,-1.914651,1.731831,-7.823196,1.826635,-2.780805,1.585264,-9.193400,9.014145,7.409645,5.357055,4.429901,-5.715381,7.308196,-2.202555,-7.700981,-0.825297,9.953420,-0.856062,-2.562712,5.772241,8.577273,-1.376567,-7.907268,3.619276,9.052813,6.299218,-8.918116,-3.945632,-1.088613,-1.489824,-7.274280,7.027341,2.046652,2.607534,0.543697,-0.587161,-2.758193,-0.155888,-4.432072,-6.559109,9.769143,-4.851006,3.526548,6.987135,9.711142,-5.581729,-3.105781,4.734983,8.495913,-2.200006,5.645669,-8.031151,6.348749,-9.436744,-1.018265,2.143630,-7.528822,7.769480,1.179000,1.773650,5.425159,-8.681604,5.249615,3.750134,5.253972,-8.351281,-4.079210,-1.130750,6.110051,-3.011674,1.069342,7.974704,5.613652,7.500026,3.257605,-9.003732,-7.884964,2.984959,-8.541680,5.644860,-2.786968,1.182147,-6.436081,-6.142541,-8.204250,3.755018,-8.088312,-4.275122,1.541855,-1.671998,-5.824798,5.546048,-0.619980,4.435799,6.645222,-9.568479,-3.149484,2.758103,1.703070,-3.614610,-8.474151,7.107737,0.168665,-9.074042,3.667771,4.784004,1.821003,-8.857741,9.025164,3.111161,-1.704803,-8.576572,6.344438,4.024280,0.657470,-3.914469,0.378534,0.038267,5.975279,-7.042790,-5.535982,1.563324,-2.565858,9.700217,3.002312,1.552988,-6.283861,-1.616689,1.593844,-2.669108,0.558941,-4.231049,-2.113566,5.477155,5.768237,-8.357004,-4.464138,-0.690306,-0.852714,-4.590699,-8.815042,5.699306,-1.466758,-7.174302,-6.159491,-9.787111,3.067623,-1.283978,-7.139172,-5.481520,6.485426,-0.248568,-6.023772,1.988280,-4.827537,-5.646882,3.062713,-4.412527,6.433526,4.537771,7.930457,6.978280,-0.230382,2.205495,-6.914983,-5.759680,-2.116686,0.247250,4.522762,7.142347,-5.672264,-6.865135,-7.784811,3.624711,5.521801,9.518445,0.523864,-0.981658,-6.520977,-1.369925,4.120302,4.094281,5.166194,-9.756192,6.234234,7.629056,6.342949,4.967945,-0.407371,2.592884,0.094251,-0.328984,4.685370,-2.823766,-3.463402,-0.389807,5.438115,-6.257538,-9.169271,-5.899950,-8.608687,-8.165652,3.961226,8.840708,-2.402936,-0.724077,5.865217,-1.086535,1.938759,3.395401,-9.058384,3.050090,9.108442,-9.104530,-8.699155,8.924988,-4.487741,-2.464422,9.821953,5.229985,-5.085375,8.643097,5.581137,-3.836213,-7.217582,-2.216637,-2.106784,-6.649463,1.048844,8.845040,5.395880,1.386038,-1.507222,-2.112744,1.224120,-3.489985,8.651556,-3.277614,0.382531,6.630940,-3.114387,-5.030386,9.612825,-0.820042,-5.905134,-0.217249,-3.556045,6.881789,1.402280,-0.295197,-5.195907,-8.974334,-3.362319,-1.061790,5.015671,9.690978,3.789404,-3.511711,-1.242229,-7.039001,0.058320,1.211474,-7.388159,-2.280011,-3.067413,-1.753576,9.490692,-4.709282,6.627455,-6.504672,-6.289278,-4.550669,4.289595,-2.941846,1.470138,-4.888731,9.603243,-0.927081,0.352507,0.044690,1.538718,-6.109372,-9.298812,-2.784794,7.704203,-4.706443,-0.603875,2.366396,-6.464664,-2.989352,-9.681601,-3.535971,-7.552161,7.440532,1.815625,1.319904,7.903632,-2.102305,-9.774238,0.757868,8.623466,1.930729,7.689806,2.578722,-5.356839,4.944069], dtype = "float32")#candidate|5737|(11232,)|const|float32
call_5736 = relay.TupleGetItem(func_1499_call(relay.reshape(const_5737.astype('float32'), [864, 13])), 3)
call_5738 = relay.TupleGetItem(func_1502_call(relay.reshape(const_5737.astype('float32'), [864, 13])), 3)
output = relay.Tuple([call_5672,call_5712,bop_5724,call_5736,const_5737,])
output2 = relay.Tuple([call_5673,call_5713,bop_5727,call_5738,const_5737,])
func_5757 = relay.Function([var_5723,], output)
mod['func_5757'] = func_5757
mod = relay.transform.InferType()(mod)
mutated_mod['func_5757'] = func_5757
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5758 = relay.var("var_5758", dtype = "float64", shape = (8, 15, 11))#candidate|5758|(8, 15, 11)|var|float64
func_5757_call = mutated_mod.get_global_var('func_5757')
call_5759 = func_5757_call(var_5758)
output = call_5759
func_5760 = relay.Function([var_5758], output)
mutated_mod['func_5760'] = func_5760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_543_call = mod.get_global_var('func_543')
func_544_call = mutated_mod.get_global_var('func_544')
call_5762 = relay.TupleGetItem(func_543_call(), 0)
call_5763 = relay.TupleGetItem(func_544_call(), 0)
func_1862_call = mod.get_global_var('func_1862')
func_1863_call = mutated_mod.get_global_var('func_1863')
call_5765 = relay.TupleGetItem(func_1862_call(), 0)
call_5766 = relay.TupleGetItem(func_1863_call(), 0)
uop_5776 = relay.cos(call_5765.astype('float64')) # shape=(9, 3, 10)
uop_5778 = relay.cos(call_5766.astype('float64')) # shape=(9, 3, 10)
output = relay.Tuple([call_5762,uop_5776,])
output2 = relay.Tuple([call_5763,uop_5778,])
func_5791 = relay.Function([], output)
mod['func_5791'] = func_5791
mod = relay.transform.InferType()(mod)
output = func_5791()
func_5792 = relay.Function([], output)
mutated_mod['func_5792'] = func_5792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_454_call = mod.get_global_var('func_454')
func_455_call = mutated_mod.get_global_var('func_455')
call_5816 = relay.TupleGetItem(func_454_call(), 0)
call_5817 = relay.TupleGetItem(func_455_call(), 0)
func_2211_call = mod.get_global_var('func_2211')
func_2213_call = mutated_mod.get_global_var('func_2213')
call_5828 = relay.TupleGetItem(func_2211_call(), 0)
call_5829 = relay.TupleGetItem(func_2213_call(), 0)
output = relay.Tuple([call_5816,call_5828,])
output2 = relay.Tuple([call_5817,call_5829,])
func_5836 = relay.Function([], output)
mod['func_5836'] = func_5836
mod = relay.transform.InferType()(mod)
output = func_5836()
func_5837 = relay.Function([], output)
mutated_mod['func_5837'] = func_5837
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2499_call = mod.get_global_var('func_2499')
func_2501_call = mutated_mod.get_global_var('func_2501')
call_5855 = relay.TupleGetItem(func_2499_call(), 0)
call_5856 = relay.TupleGetItem(func_2501_call(), 0)
output = call_5855
output2 = call_5856
func_5863 = relay.Function([], output)
mod['func_5863'] = func_5863
mod = relay.transform.InferType()(mod)
mutated_mod['func_5863'] = func_5863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5863_call = mutated_mod.get_global_var('func_5863')
call_5864 = func_5863_call()
output = call_5864
func_5865 = relay.Function([], output)
mutated_mod['func_5865'] = func_5865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4775_call = mod.get_global_var('func_4775')
func_4776_call = mutated_mod.get_global_var('func_4776')
call_5887 = relay.TupleGetItem(func_4775_call(), 0)
call_5888 = relay.TupleGetItem(func_4776_call(), 0)
func_2609_call = mod.get_global_var('func_2609')
func_2611_call = mutated_mod.get_global_var('func_2611')
call_5891 = relay.TupleGetItem(func_2609_call(), 0)
call_5892 = relay.TupleGetItem(func_2611_call(), 0)
func_713_call = mod.get_global_var('func_713')
func_714_call = mutated_mod.get_global_var('func_714')
call_5894 = relay.TupleGetItem(func_713_call(), 0)
call_5895 = relay.TupleGetItem(func_714_call(), 0)
func_1592_call = mod.get_global_var('func_1592')
func_1593_call = mutated_mod.get_global_var('func_1593')
call_5908 = relay.TupleGetItem(func_1592_call(), 0)
call_5909 = relay.TupleGetItem(func_1593_call(), 0)
func_4201_call = mod.get_global_var('func_4201')
func_4203_call = mutated_mod.get_global_var('func_4203')
call_5911 = func_4201_call()
call_5912 = func_4201_call()
var_5913 = relay.var("var_5913", dtype = "float32", shape = (9, 3, 10))#candidate|5913|(9, 3, 10)|var|float32
bop_5914 = relay.maximum(call_5887.astype('int8'), relay.reshape(var_5913.astype('int8'), relay.shape_of(call_5887))) # shape=(9, 3, 10)
bop_5917 = relay.maximum(call_5888.astype('int8'), relay.reshape(var_5913.astype('int8'), relay.shape_of(call_5888))) # shape=(9, 3, 10)
output = relay.Tuple([call_5891,call_5894,call_5908,call_5911,bop_5914,])
output2 = relay.Tuple([call_5892,call_5895,call_5909,call_5912,bop_5917,])
func_5924 = relay.Function([var_5913,], output)
mod['func_5924'] = func_5924
mod = relay.transform.InferType()(mod)
mutated_mod['func_5924'] = func_5924
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5925 = relay.var("var_5925", dtype = "float32", shape = (9, 3, 10))#candidate|5925|(9, 3, 10)|var|float32
func_5924_call = mutated_mod.get_global_var('func_5924')
call_5926 = func_5924_call(var_5925)
output = call_5926
func_5927 = relay.Function([var_5925], output)
mutated_mod['func_5927'] = func_5927
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6068 = relay.var("var_6068", dtype = "int16", shape = (14, 13, 15))#candidate|6068|(14, 13, 15)|var|int16
var_6069 = relay.var("var_6069", dtype = "int16", shape = (14, 13, 15))#candidate|6069|(14, 13, 15)|var|int16
bop_6070 = relay.greater_equal(var_6068.astype('bool'), relay.reshape(var_6069.astype('bool'), relay.shape_of(var_6068))) # shape=(14, 13, 15)
func_982_call = mod.get_global_var('func_982')
func_984_call = mutated_mod.get_global_var('func_984')
call_6075 = relay.TupleGetItem(func_982_call(), 0)
call_6076 = relay.TupleGetItem(func_984_call(), 0)
output = relay.Tuple([bop_6070,call_6075,])
output2 = relay.Tuple([bop_6070,call_6076,])
func_6077 = relay.Function([var_6068,var_6069,], output)
mod['func_6077'] = func_6077
mod = relay.transform.InferType()(mod)
var_6078 = relay.var("var_6078", dtype = "int16", shape = (14, 13, 15))#candidate|6078|(14, 13, 15)|var|int16
var_6079 = relay.var("var_6079", dtype = "int16", shape = (14, 13, 15))#candidate|6079|(14, 13, 15)|var|int16
output = func_6077(var_6078,var_6079,)
func_6080 = relay.Function([var_6078,var_6079,], output)
mutated_mod['func_6080'] = func_6080
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6084 = relay.const([[[2,5,1,2,5,-8],[4,-2,4,-5,-1,2],[9,1,-8,9,-2,2],[6,-9,-2,5,-8,6],[3,8,2,1,3,-7],[10,-1,-2,8,-6,10],[-6,5,2,-8,5,-8],[-6,-10,-3,-10,-5,-7],[-3,-5,-2,9,10,3],[-7,6,7,-9,-4,-3],[-6,-2,-5,5,4,9],[5,-5,3,-6,9,2]],[[-7,-10,-10,2,8,-8],[-4,3,5,5,1,6],[8,-4,-5,4,7,-6],[8,4,9,9,5,3],[-3,9,-8,5,8,-4],[8,-4,1,4,6,-5],[10,-10,5,4,-2,9],[-1,-8,6,9,-10,-10],[4,2,2,9,-3,-6],[4,4,6,-6,10,3],[3,-1,-6,8,5,-2],[-9,-8,9,9,-5,-7]],[[-8,7,6,5,5,-4],[7,2,4,-8,4,3],[9,5,7,-4,-7,-5],[4,-4,-10,-1,-2,10],[7,-7,1,4,-4,-3],[-3,9,1,-6,-6,3],[9,-4,6,-5,9,4],[3,-9,9,1,-10,-3],[-4,5,9,5,-3,-9],[2,-2,7,10,-5,9],[2,5,8,-4,-9,2],[8,-6,-8,-8,10,-1]],[[9,6,-2,-8,-7,-8],[-3,9,1,9,-1,-8],[1,-1,-9,7,4,10],[10,-2,-10,-4,-3,4],[4,-3,2,6,-9,-4],[9,-4,5,-1,-3,4],[3,8,-8,-10,-10,9],[-4,5,2,-2,1,8],[-4,-2,1,-2,-5,10],[7,-8,-5,-8,2,4],[3,6,4,9,-4,4],[-1,2,1,1,-4,-6]]], dtype = "uint16")#candidate|6084|(4, 12, 6)|const|uint16
var_6085 = relay.var("var_6085", dtype = "uint16", shape = (4, 12, 6))#candidate|6085|(4, 12, 6)|var|uint16
bop_6086 = relay.bitwise_and(const_6084.astype('uint16'), relay.reshape(var_6085.astype('uint16'), relay.shape_of(const_6084))) # shape=(4, 12, 6)
const_6092 = relay.const([[[-5,2,9,-8,-4,-4],[-7,10,-3,-8,-4,4],[4,-7,1,3,-10,-7],[-6,-7,5,3,8,-8],[8,8,6,-9,9,1],[4,5,10,-5,8,-1],[3,7,-7,-4,2,6],[3,8,3,-3,5,3],[9,-6,-1,-2,-10,8],[5,-2,-6,-6,-6,-3],[6,-8,-4,-8,10,-2],[10,-5,-4,-10,7,-9]],[[-2,1,1,-9,-2,10],[9,-10,4,9,-7,-6],[9,3,10,8,7,2],[-7,-5,-7,4,-2,6],[-6,10,1,-6,4,8],[-1,5,-8,-4,-7,6],[3,-3,-4,-1,-4,-6],[6,5,3,-5,-10,10],[9,-4,4,-4,10,4],[-4,6,3,-3,6,-1],[9,-3,8,10,-1,4],[4,4,3,10,10,-5]],[[8,4,-6,-2,2,-6],[1,6,10,-7,7,-2],[7,10,-6,2,5,-9],[-2,-5,-8,-5,-7,-9],[2,-3,7,-1,-7,-4],[8,-8,-4,1,8,2],[-7,5,1,-2,1,-6],[-1,5,-10,1,-6,10],[-8,8,6,-3,1,8],[-3,-7,-6,-5,9,-4],[-8,6,8,6,4,-1],[3,5,2,-6,-6,1]],[[5,10,5,-1,-1,-9],[-1,-4,-8,-9,-8,7],[-10,9,5,9,-6,-1],[2,-4,-1,3,-7,-10],[1,5,4,1,4,-3],[10,8,10,4,3,7],[10,-5,7,1,-5,-9],[-8,-6,-10,1,10,5],[9,9,9,6,-6,-8],[8,-2,8,3,-2,8],[7,-4,-1,4,10,1],[-1,-1,-10,9,10,1]]], dtype = "uint16")#candidate|6092|(4, 12, 6)|const|uint16
bop_6093 = relay.add(var_6085.astype('uint16'), relay.reshape(const_6092.astype('uint16'), relay.shape_of(var_6085))) # shape=(4, 12, 6)
func_4581_call = mod.get_global_var('func_4581')
func_4583_call = mutated_mod.get_global_var('func_4583')
const_6103 = relay.const([9.248650,4.252394,4.165580,6.851356,4.137803,9.648902,6.134466,-5.470146,-6.844427,-8.385493,8.952274,-6.161709,-3.718854,-5.703363,-0.705780,-6.411315,9.789744,8.333900,0.434880,-1.471321,6.094017,-8.375120,-5.717123,-2.399473,7.146098,4.850055,-9.431311,7.981439,-8.920546,-3.422510,-9.599793,-3.635756,-0.465647,-0.283288,1.604379,4.221601,-1.040099,0.331523,-4.469881,-6.513552,9.107379,9.820931,5.484104,-0.553019,-1.644803,-3.338333,0.638721,-7.530790,7.582171,3.451333,0.081089,8.224424,-1.040217,3.981051,3.860774,-6.361781,2.324053,-4.796915,-9.242262,-6.969209,2.105356,0.049382,-0.266684,4.485758,-0.977562,-6.991966,1.943997,-3.193743,-3.081981,-0.434309,9.478124,-1.934336,-5.109446,4.120837,4.648616,3.044136,8.164182,-5.562879,-9.445967,3.640677,-5.619257,1.577728,6.445493,-2.348038,6.599074,2.501027,3.647813,7.724817,-9.402322,0.273860,9.082892,4.925589,6.198867,-0.203269,4.922554,2.261014,8.887046,8.261784,-6.852842,-2.962274,-5.877610,-7.680826,-3.280456,-9.472453,-0.986199,-5.004813,-3.226227,-3.887727,7.407956,-3.485574,-5.342849,0.041515,-2.416163,4.436126,-3.271363,-5.055462,0.219301,-2.627459,-5.668317,9.324977,-0.821487,-7.658997,6.485137,1.843929,6.076059,2.070235,6.184753,3.705659,0.757946,-6.382679,2.296292,-3.263494,5.948511,-2.048966,5.161235,-9.560687,7.771149,5.766810,-2.810262,-6.778725,-0.893853,5.386903,-0.861502,2.348636,1.905626,0.436457,-9.520926,-1.980390,-6.161961,3.737966,-8.059329,-4.952496,0.724272,-0.502086,-8.952727,4.228935,-0.777072,-9.975840,-7.917166,-8.421217,4.655871,-2.737166,2.789796,2.862075,2.337098,-0.732268,-9.416787,1.222869,-3.756233,8.603190,-0.660333,6.395858,-3.406074,3.505413,1.726171,-7.481268,2.457095,-9.281681,7.112443,8.841595,-5.917246,-3.451036,-9.084288,-0.616619,0.167478,5.408838,3.580319,-3.057253,-8.841657,-8.407372,4.681428,-5.703605,6.550344,-5.865177,-1.703690,3.441789,5.679779,1.091102,0.785670,-3.950727,-0.138083,3.605828,-2.526708,2.194213,3.403000,-3.159068,-5.355525,-5.498572,3.550531,4.733913,-8.530638,-2.733426,-0.715557,0.332873,-5.372445,2.287602,8.779824,-3.070537,-3.306220,-2.466632,2.345775,5.390103,0.263618,3.241599,-2.332896,-5.430278,4.447846,-0.677119,-3.088741,0.886245,8.056907,1.525680,4.315696,-7.018316,0.782898,-5.972065,3.232834,5.005197,2.593676,8.628817,6.157346,-2.598818,-1.185931,-0.931504,-7.921892,2.872142,-4.846463,-4.076594,-6.317034,-3.320481,2.897518,-1.248077,-4.767512,7.106745,-4.825248,2.437234,-3.105851,-3.341149,-8.969835,1.758022,8.245801,-3.815391,-2.772022,6.035347,9.476787,-0.878154,-1.838258,3.208836,-4.869016,-4.961790,7.007721,-7.420743,8.065814,-8.929644,-6.296594,-7.680442,0.647287,5.384974,7.746524,-7.965190,-0.567759,3.786779,-2.215249,8.770705,7.958686,2.067109,2.210516,-6.273993,4.657611,-5.314895,5.899847,4.762829,9.715026,-6.510744,2.441282,8.714252,2.105348,4.837882,2.751041,9.964002,-7.720276,9.054786,-1.952878,5.476988,9.845143,4.746944,-3.690063,2.801573,-0.546594,1.354207,-7.563131,6.439995,6.300812,6.162287,-9.432747,-6.078334,-1.522605,-2.271070,2.086892,-5.078720,-9.867336,6.664652,-1.058747,-1.445977,-4.115729,-6.026192,2.434790,2.799913,-1.395697,9.501732,6.011186,-6.725985,-9.586212,-7.737251,-8.103907,-4.677603,1.750763,4.370277,-9.671911,-7.496179,8.069704,2.370975,-0.039701,-2.555443,-4.936508,4.224924,6.515481,6.173101,1.568440,8.836668,-8.156502,-1.869680,-8.861891,0.738762,0.931866,6.234913,-0.518505,2.327158,6.034148,-1.439098,-9.044038,8.172607,0.491002,0.647919,4.627500,-6.322189,-6.333281,0.010504,-1.702581,2.500531,-4.503251,9.112857,4.946553,7.316330,-6.550557,-6.219222,-7.627380,-0.492989,-5.778012,-7.613772,-9.328998,0.586810,7.891302,3.699479,9.760034,2.246795,-6.852217,6.703634,-6.201822,-6.532940,-4.148057,1.902134,1.320015,-3.671035,7.652911,2.437749,2.670711,-1.297081,0.645619,-6.124635,-9.594608,-4.236629,-1.117320,-2.393181,-2.781895,4.143513,-0.847753,4.002847,-2.312561,7.519095,-8.569214,-0.451175,-9.855245,-6.413710,-3.554017,-8.996862,1.596635,4.588261,-6.761454,-1.685097,2.306987,5.448835,-0.082453,5.229665,-5.995496,-6.961459,3.115290,-0.969650,1.690892,8.320838,-5.689261,-6.749311], dtype = "float32")#candidate|6103|(432,)|const|float32
call_6102 = func_4581_call(relay.reshape(const_6103.astype('float32'), [9, 4, 12]))
call_6104 = func_4581_call(relay.reshape(const_6103.astype('float32'), [9, 4, 12]))
output = relay.Tuple([bop_6086,bop_6093,call_6102,const_6103,])
output2 = relay.Tuple([bop_6086,bop_6093,call_6104,const_6103,])
func_6107 = relay.Function([var_6085,], output)
mod['func_6107'] = func_6107
mod = relay.transform.InferType()(mod)
mutated_mod['func_6107'] = func_6107
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6108 = relay.var("var_6108", dtype = "uint16", shape = (4, 12, 6))#candidate|6108|(4, 12, 6)|var|uint16
func_6107_call = mutated_mod.get_global_var('func_6107')
call_6109 = func_6107_call(var_6108)
output = call_6109
func_6110 = relay.Function([var_6108], output)
mutated_mod['func_6110'] = func_6110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2137_call = mod.get_global_var('func_2137')
func_2139_call = mutated_mod.get_global_var('func_2139')
call_6112 = relay.TupleGetItem(func_2137_call(), 0)
call_6113 = relay.TupleGetItem(func_2139_call(), 0)
output = relay.Tuple([call_6112,])
output2 = relay.Tuple([call_6113,])
func_6118 = relay.Function([], output)
mod['func_6118'] = func_6118
mod = relay.transform.InferType()(mod)
mutated_mod['func_6118'] = func_6118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6118_call = mutated_mod.get_global_var('func_6118')
call_6119 = func_6118_call()
output = call_6119
func_6120 = relay.Function([], output)
mutated_mod['func_6120'] = func_6120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2036_call = mod.get_global_var('func_2036')
func_2037_call = mutated_mod.get_global_var('func_2037')
call_6150 = relay.TupleGetItem(func_2036_call(), 1)
call_6151 = relay.TupleGetItem(func_2037_call(), 1)
const_6160 = relay.const([[2,6,-5,-1,-4,-3,7,6,-7,-10,-10,1,-3,10,3,-2,6,-2,-6,-7,7,5,-5,7,-3,3,4,-7,-8,-1,-5,-5,-2,-3,1,9,9,-3,7,6,-7,-5,-4,9,7,10,-4,-6,-3,5,8,3,9,4,6,-6,-1,-5,1,-7,-6,4,-4,-6,-9,3,6,7,-4,1,-10,-4,-8,-6,-4,1,9,-2,4,-2,-1,-10,-10,4,7,5,-2,8,7,1,8,5,-5,-2,7,2,8,-6,-9,4,6,3,8,10,-9,1,10,7,-3,4,3,-9,-2,-3,7,-6,7,-3,-3,2,-3,-1,9,8,-7,1,10,2,6,2,-5,6,-10,-8,-1,6,3,7,-3,3,7,9,5,9,9,5,-2,7,-2,-6,5,-7,7,-10,8,2,1,-5,5,10],[-7,-9,7,-10,10,2,-8,-6,4,7,1,-9,3,1,-8,-3,7,4,9,-1,-2,6,5,-6,10,-2,5,5,5,-5,6,-8,1,7,9,-10,-4,-2,-10,7,-4,-1,8,8,-2,6,2,-3,7,-4,1,-7,2,-1,10,10,-6,-6,9,-8,6,10,-10,-10,4,-3,-7,9,4,10,9,1,-3,10,10,2,3,-3,-7,-2,-4,-8,-7,-8,9,6,-10,-1,-3,-6,8,8,-1,6,1,-9,-3,6,5,3,-6,10,-8,-10,10,4,5,1,1,4,-3,7,-1,8,-10,8,1,-1,-8,10,10,-8,-3,1,-4,6,-7,5,-7,-3,-3,-3,10,-3,-9,-6,6,4,-3,-1,-9,4,9,5,2,3,9,-4,-1,7,10,9,-7,5,-5,7,-5,-1,2,-2],[-1,4,2,1,4,3,3,-2,-2,-10,-3,-2,-2,5,-6,10,2,1,1,9,-2,-9,-4,-5,8,-5,6,1,10,-2,3,-8,-6,-8,3,-10,10,9,-10,2,2,3,7,-6,10,-7,-7,-7,-4,-8,4,3,9,10,8,1,1,10,6,5,1,8,-7,-3,-1,9,10,9,-3,1,3,1,-4,10,-6,-9,-8,-7,3,7,10,1,-7,-1,1,10,-4,6,4,1,2,7,8,-7,3,-6,2,-4,8,-7,-7,-3,-10,2,-6,1,4,9,1,4,-2,6,-6,10,6,-4,-6,6,7,-7,-5,-10,8,3,-5,-3,5,-8,-10,8,-8,8,1,-10,-6,-9,7,9,9,5,7,9,-5,-7,-7,-10,-7,-9,-4,7,5,-10,5,6,-1,6,-6,2,-3,-8],[-3,-5,7,-9,2,3,-1,-8,2,2,6,1,-4,5,9,-10,-4,-5,1,-3,9,10,9,-10,-3,-4,10,-3,6,2,3,-10,-6,-9,-8,-8,8,-10,-8,-10,1,-2,-7,3,-2,1,-6,-4,5,-7,-6,1,-5,-3,-1,3,-4,3,7,5,1,-7,-6,-7,-2,5,1,4,-8,6,7,-1,4,4,-10,-3,4,7,-10,-2,-1,2,4,-8,10,-2,-5,2,7,-3,5,-7,3,-3,-10,-7,4,5,-3,2,10,2,9,7,10,-2,-5,5,4,-2,5,-7,9,6,-8,-5,4,-6,-3,-8,4,-7,-10,-8,2,-1,1,5,2,2,-2,8,6,9,-8,2,9,-2,6,5,4,-7,4,5,-5,-5,5,3,9,3,-10,-1,6,2,-5,-2,-1,-6,-10,2],[-9,2,-10,7,8,-7,7,-1,-3,-9,-8,-9,-9,-7,-5,6,-3,8,-5,5,9,6,-9,-2,-10,1,1,10,-3,1,-3,2,5,-3,6,-6,9,-10,-10,1,3,-7,-3,4,-3,4,2,-6,-7,-9,-7,8,8,-4,-10,8,10,8,2,9,-5,-3,-8,-5,-8,-10,9,10,-5,8,1,1,-1,5,8,-1,7,-1,-5,-2,1,7,-7,9,-3,-9,3,8,-8,-9,6,-1,-6,-8,1,3,1,3,-8,1,-1,8,2,-8,-8,9,7,-7,-4,-3,4,-8,9,-6,-6,-8,9,1,-1,-4,-3,3,2,-4,-2,3,4,-4,7,-10,6,9,6,-9,-8,6,-5,-3,6,3,-4,-5,-10,-3,-8,9,3,-9,10,5,-10,-9,-7,-10,-10,10,-1,-2,5,-7],[10,-7,6,1,-4,3,-5,-1,-7,-5,5,-2,-2,7,-2,10,-2,3,3,-5,-10,2,-3,8,-3,-8,10,-5,6,10,10,-8,-7,4,4,-8,8,-10,3,4,2,-6,-1,5,-5,-5,-4,-1,3,10,5,-4,8,-5,-5,-8,-10,-1,5,10,10,-9,8,7,3,1,-7,-10,-2,-7,5,-3,-8,-8,10,-5,3,7,3,-5,3,-4,-4,5,-3,-2,-8,3,-1,2,-1,2,-10,7,2,10,1,-6,-2,10,5,-4,-9,10,-8,-9,-9,2,3,5,-3,-3,-10,-9,9,-8,1,7,8,8,-2,-6,-2,-2,-10,-10,-1,9,-1,-4,8,-7,1,-9,-5,-5,-7,-10,9,-4,1,4,-9,5,-1,-4,-8,-8,-5,8,-5,7,-5,-1,-10,-7,-2,-3,6,-5],[-5,-6,8,-4,4,-4,-8,-10,-7,9,-9,8,-9,-4,-9,10,6,8,3,-8,5,-5,-3,6,-8,-7,3,-10,-6,-5,-3,-10,-4,-6,10,1,6,-8,1,-10,1,9,5,-8,4,-8,10,-10,6,-9,-8,4,8,-4,8,-9,-3,6,-8,9,-8,10,2,-10,4,7,-2,9,-4,9,6,2,-6,7,3,-5,2,-6,-5,-5,8,4,-2,1,5,8,8,3,10,-10,-6,1,2,4,-6,8,-2,5,5,-10,6,4,-9,1,-8,2,6,4,5,-7,9,-6,-8,-5,-8,3,-4,-9,-3,4,-1,-5,-2,-7,9,9,-9,-6,-7,-10,-5,-1,10,-2,2,6,2,2,-2,-2,-5,6,-7,1,-3,-9,1,-7,-9,6,5,-5,-3,3,-10,-6,-10,-8,-5,9],[9,-6,7,3,-4,-7,1,6,-1,-9,7,-5,-8,-2,-2,-2,-2,-1,-4,6,5,7,-7,10,-3,10,-6,7,-8,8,-3,-10,3,-3,-8,-4,-2,9,-3,7,9,8,-2,1,5,9,2,-10,-3,-1,-9,5,6,-1,2,9,-7,9,1,9,-1,-3,-8,-9,5,1,7,-7,10,3,8,-5,8,-6,6,-4,-2,2,-9,10,-1,10,-8,10,-7,-10,-7,-1,1,-4,3,-3,-5,6,6,-10,8,4,8,-4,10,-1,-10,-10,2,-7,-1,9,-7,-2,2,9,-3,-7,-8,-6,-6,-5,-9,-9,-8,5,1,5,-8,9,8,-1,-3,-2,1,1,-2,8,-1,2,7,9,1,4,-1,-3,-4,-2,5,10,-9,-5,-7,-4,-2,-8,-4,-5,-2,-8,5,-6,6,-6],[1,6,6,2,-8,4,3,-9,10,3,4,-7,-1,-9,-10,-7,-10,-10,8,-2,6,-6,-7,-5,-8,10,-2,-2,9,-1,6,-1,-2,-3,-3,-7,-10,-8,-8,5,-5,-10,2,-9,5,2,-7,8,-4,-2,-7,-7,-3,-5,10,-5,-4,2,-8,9,-1,3,-5,-9,-5,7,-1,-10,-9,-5,6,6,4,-8,-10,-4,-1,1,1,7,3,7,-10,8,5,-10,3,10,7,2,6,-8,-6,-3,9,2,-5,5,7,5,-9,2,3,3,-10,7,10,3,4,-2,3,4,4,-3,5,4,3,9,-10,5,-7,7,8,5,3,5,-3,4,-8,-10,-5,10,10,5,2,-1,-4,6,6,6,-1,5,-9,1,8,-2,-6,4,-4,8,-10,-4,-7,6,4,-5,2,8,1,-9],[-1,-5,-7,-4,5,-6,-3,9,1,-5,9,1,-10,-5,10,-1,8,9,2,-4,-7,3,-1,10,-2,-8,-3,-4,-9,3,2,-10,9,-6,3,1,10,-10,8,2,6,-1,-8,1,4,7,-9,6,6,-10,-2,1,-5,-3,-10,3,5,-7,8,10,-4,-10,6,1,-10,3,2,-3,2,1,1,9,9,8,-4,1,-9,-10,-7,-7,4,8,-1,-4,-9,8,-1,7,-3,-9,-5,-6,1,9,9,-6,5,8,7,10,6,-9,5,7,10,8,6,2,-9,7,9,10,7,10,7,1,10,-10,-5,4,3,-5,-5,8,9,4,9,2,2,-2,-5,-4,-5,9,-1,9,6,-5,-2,9,-10,-1,-6,7,-8,7,-1,8,5,-8,-2,-2,-3,-3,4,10,4,-3,6,-8],[-8,-10,8,-7,-7,1,3,10,-2,3,-5,-10,-4,-9,2,7,-2,8,-4,3,1,-3,-7,10,-7,7,-6,1,1,-2,-7,2,-5,9,5,-3,6,-1,-8,-4,6,7,10,3,7,-2,-2,6,-7,9,9,-10,-5,-9,4,7,5,-3,3,-4,-1,7,-3,3,9,3,3,4,4,10,-7,9,5,6,-10,-10,-1,4,-1,-5,10,-8,-9,10,6,-1,-1,4,2,3,2,-3,-10,6,-6,2,9,9,-4,1,-3,10,3,-9,4,7,5,9,-6,7,-6,-10,-10,-2,9,2,-4,-5,6,3,6,-6,-9,6,-9,-7,-1,9,5,-6,3,-6,2,-5,7,-10,8,-4,10,2,3,4,6,7,-5,8,1,-8,-7,-5,2,9,-3,7,-5,3,-8,-3,-2,-8],[1,8,9,-9,10,-3,9,-10,-5,4,-4,7,7,6,10,8,-9,-5,2,-7,6,-5,-1,5,-2,5,9,-9,4,6,1,-5,-2,-9,2,9,5,5,8,2,-3,7,-1,-6,2,-10,8,5,6,4,-1,10,-6,-2,4,-4,2,-9,-8,1,9,-4,7,-4,-3,-2,3,10,6,-4,9,7,9,-6,1,6,-1,4,10,-2,8,7,6,1,-1,-2,2,2,7,6,-7,7,-3,-5,-3,-5,-1,-4,-2,-10,-9,3,-4,-1,-5,9,9,2,-9,6,4,-2,-8,5,-9,-2,7,-10,-10,-2,-7,-9,-6,-10,-7,-6,-2,7,3,9,-7,2,6,-5,-2,3,9,-8,2,10,8,10,4,-9,1,1,-9,-10,-5,-3,-3,8,8,-6,6,10,4,4,-9,-5],[3,8,8,-6,4,-2,6,10,-6,6,4,5,-8,-8,-4,-7,10,6,5,1,-3,-6,-4,5,-5,-3,-9,-9,-9,-3,-3,-7,-8,-8,-9,2,-3,1,7,9,-8,-10,-1,3,-9,3,7,-2,-5,7,1,-5,10,-4,-5,8,3,10,9,4,-10,-10,8,-3,2,6,1,-10,1,-9,-4,8,5,3,-3,-3,-5,9,5,-6,-4,-2,6,-10,-5,3,-4,-9,1,4,-1,7,10,-9,10,3,8,2,9,-2,9,-6,-8,-3,-8,-3,3,-5,7,-7,-9,-4,-6,-2,-8,-9,-10,1,1,7,10,10,-1,6,1,7,-4,9,-7,4,7,-2,10,5,9,5,-5,5,-2,-5,4,4,-3,7,6,-5,7,-10,-3,10,-8,-3,10,8,-9,-6,5,3,5,-9],[-3,1,-4,-7,-5,-10,2,7,-1,3,-8,-5,8,-2,-7,-1,-5,-10,-3,-5,4,5,-1,7,7,-2,-6,7,-4,-7,8,-1,2,2,-8,6,-6,-7,1,-7,-3,-3,-7,-5,9,-3,-1,4,6,9,-4,-8,-5,-7,9,7,4,-1,2,3,-7,2,1,-1,1,2,6,8,-5,10,-1,-3,8,-8,-9,4,7,8,-2,-6,-9,-10,8,-6,3,4,2,-8,3,-1,-9,2,2,4,7,7,-8,-2,-5,7,4,-1,-9,9,7,6,-6,1,-6,-2,-5,-2,-5,7,-3,-7,6,-7,7,10,-7,-9,5,-3,-5,8,3,2,4,-8,-6,8,-3,10,1,5,4,-3,3,4,8,-7,9,8,1,-4,1,10,7,5,7,5,1,2,3,-2,-7,-1,10,-2],[7,9,-8,-3,6,2,-5,5,-7,2,5,1,6,-8,3,-9,-6,8,7,6,7,-7,6,-10,2,-1,9,7,-3,-2,-7,-5,-1,-4,4,2,-9,-6,2,6,-2,-1,8,-4,4,-5,9,3,-5,-6,10,-2,8,4,6,6,-8,8,-8,8,8,-3,5,5,-5,-9,-3,-4,9,-3,-1,-2,9,-6,2,-8,-7,-5,9,10,-3,10,10,-6,-3,3,-1,2,4,-6,-2,-7,9,9,4,-3,10,2,9,-6,-1,8,-5,4,10,6,-8,9,6,5,-9,6,4,-9,10,-7,6,4,6,3,-10,8,-3,-3,-6,9,-9,-7,7,-7,-3,9,-10,3,1,-3,-4,-8,7,5,2,-1,1,5,5,-6,-6,2,-5,5,-10,8,-1,-10,-10,4,-1,4,-4,-1],[-2,-9,-1,6,5,-4,10,-8,10,9,-7,1,-9,-1,5,2,-10,-6,4,-8,5,-4,6,6,-4,-4,-2,-8,-4,-4,4,8,8,6,6,-3,-6,6,10,7,-10,4,10,3,-2,2,-2,9,-4,4,-9,-3,-3,-8,-2,9,-8,6,-7,-1,-3,-5,3,4,9,9,4,-4,10,2,-6,6,3,1,8,-1,5,7,-1,7,-1,-9,-6,-10,6,-10,2,-8,7,-7,3,9,5,8,-7,8,-1,10,2,6,3,-2,-2,-2,-2,-6,-8,-5,-1,10,7,-5,-7,-6,9,8,-5,-9,-3,-8,1,-1,8,-3,-8,8,-1,2,8,-8,9,8,-8,-1,-7,9,-2,6,-6,-1,-2,-2,2,2,3,8,7,3,3,10,4,10,10,8,-7,-4,7,-3,-9,10]], dtype = "int16")#candidate|6160|(16, 160)|const|int16
bop_6161 = relay.add(call_6150.astype('uint64'), const_6160.astype('uint64')) # shape=(16, 160)
bop_6164 = relay.add(call_6151.astype('uint64'), const_6160.astype('uint64')) # shape=(16, 160)
bop_6169 = relay.multiply(call_6150.astype('int64'), const_6160.astype('int64')) # shape=(16, 160)
bop_6172 = relay.multiply(call_6151.astype('int64'), const_6160.astype('int64')) # shape=(16, 160)
uop_6173 = relay.sigmoid(bop_6161.astype('float32')) # shape=(16, 160)
uop_6175 = relay.sigmoid(bop_6164.astype('float32')) # shape=(16, 160)
func_3086_call = mod.get_global_var('func_3086')
func_3087_call = mutated_mod.get_global_var('func_3087')
call_6185 = relay.TupleGetItem(func_3086_call(), 0)
call_6186 = relay.TupleGetItem(func_3087_call(), 0)
uop_6196 = relay.tan(uop_6173.astype('float64')) # shape=(16, 160)
uop_6198 = relay.tan(uop_6175.astype('float64')) # shape=(16, 160)
func_3687_call = mod.get_global_var('func_3687')
func_3689_call = mutated_mod.get_global_var('func_3689')
call_6203 = relay.TupleGetItem(func_3687_call(), 0)
call_6204 = relay.TupleGetItem(func_3689_call(), 0)
func_1518_call = mod.get_global_var('func_1518')
func_1520_call = mutated_mod.get_global_var('func_1520')
call_6210 = relay.TupleGetItem(func_1518_call(), 0)
call_6211 = relay.TupleGetItem(func_1520_call(), 0)
output = relay.Tuple([bop_6169,call_6185,uop_6196,call_6203,call_6210,])
output2 = relay.Tuple([bop_6172,call_6186,uop_6198,call_6204,call_6211,])
func_6217 = relay.Function([], output)
mod['func_6217'] = func_6217
mod = relay.transform.InferType()(mod)
mutated_mod['func_6217'] = func_6217
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6217_call = mutated_mod.get_global_var('func_6217')
call_6218 = func_6217_call()
output = call_6218
func_6219 = relay.Function([], output)
mutated_mod['func_6219'] = func_6219
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6239 = relay.var("var_6239", dtype = "float32", shape = (3, 8, 9))#candidate|6239|(3, 8, 9)|var|float32
uop_6240 = relay.asin(var_6239.astype('float32')) # shape=(3, 8, 9)
output = relay.Tuple([uop_6240,])
output2 = relay.Tuple([uop_6240,])
func_6263 = relay.Function([var_6239,], output)
mod['func_6263'] = func_6263
mod = relay.transform.InferType()(mod)
mutated_mod['func_6263'] = func_6263
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6264 = relay.var("var_6264", dtype = "float32", shape = (3, 8, 9))#candidate|6264|(3, 8, 9)|var|float32
func_6263_call = mutated_mod.get_global_var('func_6263')
call_6265 = func_6263_call(var_6264)
output = call_6265
func_6266 = relay.Function([var_6264], output)
mutated_mod['func_6266'] = func_6266
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5070_call = mod.get_global_var('func_5070')
func_5072_call = mutated_mod.get_global_var('func_5072')
call_6342 = func_5070_call()
call_6343 = func_5070_call()
output = relay.Tuple([call_6342,])
output2 = relay.Tuple([call_6343,])
func_6355 = relay.Function([], output)
mod['func_6355'] = func_6355
mod = relay.transform.InferType()(mod)
output = func_6355()
func_6356 = relay.Function([], output)
mutated_mod['func_6356'] = func_6356
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5836_call = mod.get_global_var('func_5836')
func_5837_call = mutated_mod.get_global_var('func_5837')
call_6391 = relay.TupleGetItem(func_5836_call(), 0)
call_6392 = relay.TupleGetItem(func_5837_call(), 0)
output = call_6391
output2 = call_6392
func_6408 = relay.Function([], output)
mod['func_6408'] = func_6408
mod = relay.transform.InferType()(mod)
output = func_6408()
func_6409 = relay.Function([], output)
mutated_mod['func_6409'] = func_6409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3687_call = mod.get_global_var('func_3687')
func_3689_call = mutated_mod.get_global_var('func_3689')
call_6452 = relay.TupleGetItem(func_3687_call(), 0)
call_6453 = relay.TupleGetItem(func_3689_call(), 0)
const_6462 = relay.const([[[False,False],[True,False],[False,False],[False,False],[False,False],[False,False],[True,True],[True,True],[True,True],[True,False],[True,True],[True,True],[False,True],[True,False],[True,False],[False,True]],[[False,True],[False,False],[False,False],[False,False],[True,True],[True,False],[False,False],[False,True],[True,True],[True,True],[False,False],[False,False],[True,True],[False,True],[False,True],[False,False]],[[False,False],[True,False],[True,True],[True,False],[False,False],[False,False],[False,False],[True,True],[True,True],[False,False],[True,False],[False,True],[False,True],[False,False],[False,False],[False,False]],[[True,True],[True,False],[True,False],[False,True],[False,False],[False,False],[True,True],[True,False],[False,False],[False,False],[False,True],[True,False],[False,True],[False,False],[True,True],[False,False]],[[False,True],[False,True],[True,False],[True,True],[True,True],[True,False],[False,True],[False,True],[True,True],[True,True],[False,False],[False,False],[True,False],[False,False],[True,False],[True,False]],[[False,True],[True,True],[False,False],[True,True],[True,False],[True,False],[True,True],[True,False],[False,False],[False,False],[False,False],[False,True],[False,False],[True,False],[True,False],[False,True]],[[False,True],[False,False],[False,True],[True,True],[False,False],[True,True],[True,False],[False,False],[False,False],[False,False],[False,True],[True,False],[True,True],[False,False],[True,False],[True,True]],[[False,False],[True,False],[True,False],[True,True],[False,True],[True,False],[True,True],[False,False],[True,False],[False,True],[True,False],[True,True],[True,False],[True,False],[False,True],[False,False]],[[True,True],[False,False],[False,False],[False,False],[True,True],[False,False],[False,False],[False,True],[True,True],[False,False],[True,True],[True,False],[True,True],[False,False],[False,False],[False,True]],[[False,True],[True,False],[True,True],[False,False],[False,True],[False,False],[True,True],[True,False],[False,True],[True,True],[True,False],[True,False],[True,True],[False,True],[False,True],[False,False]],[[False,False],[False,True],[True,False],[True,False],[True,True],[False,True],[False,False],[True,False],[True,False],[True,False],[True,False],[True,False],[False,True],[False,False],[False,False],[False,False]],[[False,False],[True,False],[False,False],[False,False],[False,False],[True,False],[False,False],[True,False],[True,False],[False,False],[True,True],[False,True],[True,False],[True,True],[True,True],[False,True]]], dtype = "bool")#candidate|6462|(12, 16, 2)|const|bool
bop_6463 = relay.power(call_6452.astype('float64'), relay.reshape(const_6462.astype('float64'), relay.shape_of(call_6452))) # shape=(12, 16, 2)
bop_6466 = relay.power(call_6453.astype('float64'), relay.reshape(const_6462.astype('float64'), relay.shape_of(call_6453))) # shape=(12, 16, 2)
func_543_call = mod.get_global_var('func_543')
func_544_call = mutated_mod.get_global_var('func_544')
call_6471 = relay.TupleGetItem(func_543_call(), 0)
call_6472 = relay.TupleGetItem(func_544_call(), 0)
func_2414_call = mod.get_global_var('func_2414')
func_2416_call = mutated_mod.get_global_var('func_2416')
call_6484 = relay.TupleGetItem(func_2414_call(), 0)
call_6485 = relay.TupleGetItem(func_2416_call(), 0)
bop_6486 = relay.bitwise_or(call_6452.astype('uint8'), relay.reshape(const_6462.astype('uint8'), relay.shape_of(call_6452))) # shape=(12, 16, 2)
bop_6489 = relay.bitwise_or(call_6453.astype('uint8'), relay.reshape(const_6462.astype('uint8'), relay.shape_of(call_6453))) # shape=(12, 16, 2)
output = relay.Tuple([bop_6463,call_6471,call_6484,bop_6486,])
output2 = relay.Tuple([bop_6466,call_6472,call_6485,bop_6489,])
func_6507 = relay.Function([], output)
mod['func_6507'] = func_6507
mod = relay.transform.InferType()(mod)
mutated_mod['func_6507'] = func_6507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6507_call = mutated_mod.get_global_var('func_6507')
call_6508 = func_6507_call()
output = call_6508
func_6509 = relay.Function([], output)
mutated_mod['func_6509'] = func_6509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1385_call = mod.get_global_var('func_1385')
func_1386_call = mutated_mod.get_global_var('func_1386')
call_6515 = relay.TupleGetItem(func_1385_call(), 0)
call_6516 = relay.TupleGetItem(func_1386_call(), 0)
output = call_6515
output2 = call_6516
func_6518 = relay.Function([], output)
mod['func_6518'] = func_6518
mod = relay.transform.InferType()(mod)
output = func_6518()
func_6519 = relay.Function([], output)
mutated_mod['func_6519'] = func_6519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3311_call = mod.get_global_var('func_3311')
func_3313_call = mutated_mod.get_global_var('func_3313')
call_6520 = relay.TupleGetItem(func_3311_call(), 3)
call_6521 = relay.TupleGetItem(func_3313_call(), 3)
output = call_6520
output2 = call_6521
func_6525 = relay.Function([], output)
mod['func_6525'] = func_6525
mod = relay.transform.InferType()(mod)
mutated_mod['func_6525'] = func_6525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6525_call = mutated_mod.get_global_var('func_6525')
call_6526 = func_6525_call()
output = call_6526
func_6527 = relay.Function([], output)
mutated_mod['func_6527'] = func_6527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5092_call = mod.get_global_var('func_5092')
func_5094_call = mutated_mod.get_global_var('func_5094')
call_6550 = relay.TupleGetItem(func_5092_call(), 0)
call_6551 = relay.TupleGetItem(func_5094_call(), 0)
func_2980_call = mod.get_global_var('func_2980')
func_2982_call = mutated_mod.get_global_var('func_2982')
call_6569 = relay.TupleGetItem(func_2980_call(), 1)
call_6570 = relay.TupleGetItem(func_2982_call(), 1)
func_3110_call = mod.get_global_var('func_3110')
func_3112_call = mutated_mod.get_global_var('func_3112')
call_6579 = relay.TupleGetItem(func_3110_call(), 1)
call_6580 = relay.TupleGetItem(func_3112_call(), 1)
output = relay.Tuple([call_6550,call_6569,call_6579,])
output2 = relay.Tuple([call_6551,call_6570,call_6580,])
func_6591 = relay.Function([], output)
mod['func_6591'] = func_6591
mod = relay.transform.InferType()(mod)
output = func_6591()
func_6592 = relay.Function([], output)
mutated_mod['func_6592'] = func_6592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_543_call = mod.get_global_var('func_543')
func_544_call = mutated_mod.get_global_var('func_544')
call_6618 = relay.TupleGetItem(func_543_call(), 0)
call_6619 = relay.TupleGetItem(func_544_call(), 0)
output = relay.Tuple([call_6618,])
output2 = relay.Tuple([call_6619,])
func_6635 = relay.Function([], output)
mod['func_6635'] = func_6635
mod = relay.transform.InferType()(mod)
mutated_mod['func_6635'] = func_6635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6635_call = mutated_mod.get_global_var('func_6635')
call_6636 = func_6635_call()
output = call_6636
func_6637 = relay.Function([], output)
mutated_mod['func_6637'] = func_6637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1592_call = mod.get_global_var('func_1592')
func_1593_call = mutated_mod.get_global_var('func_1593')
call_6671 = relay.TupleGetItem(func_1592_call(), 1)
call_6672 = relay.TupleGetItem(func_1593_call(), 1)
output = relay.Tuple([call_6671,])
output2 = relay.Tuple([call_6672,])
func_6676 = relay.Function([], output)
mod['func_6676'] = func_6676
mod = relay.transform.InferType()(mod)
mutated_mod['func_6676'] = func_6676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6676_call = mutated_mod.get_global_var('func_6676')
call_6677 = func_6676_call()
output = call_6677
func_6678 = relay.Function([], output)
mutated_mod['func_6678'] = func_6678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2587_call = mod.get_global_var('func_2587')
func_2588_call = mutated_mod.get_global_var('func_2588')
call_6689 = relay.TupleGetItem(func_2587_call(), 3)
call_6690 = relay.TupleGetItem(func_2588_call(), 3)
output = call_6689
output2 = call_6690
func_6696 = relay.Function([], output)
mod['func_6696'] = func_6696
mod = relay.transform.InferType()(mod)
mutated_mod['func_6696'] = func_6696
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6696_call = mutated_mod.get_global_var('func_6696')
call_6697 = func_6696_call()
output = call_6697
func_6698 = relay.Function([], output)
mutated_mod['func_6698'] = func_6698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3110_call = mod.get_global_var('func_3110')
func_3112_call = mutated_mod.get_global_var('func_3112')
call_6746 = relay.TupleGetItem(func_3110_call(), 1)
call_6747 = relay.TupleGetItem(func_3112_call(), 1)
output = call_6746
output2 = call_6747
func_6755 = relay.Function([], output)
mod['func_6755'] = func_6755
mod = relay.transform.InferType()(mod)
mutated_mod['func_6755'] = func_6755
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6755_call = mutated_mod.get_global_var('func_6755')
call_6756 = func_6755_call()
output = call_6756
func_6757 = relay.Function([], output)
mutated_mod['func_6757'] = func_6757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1842_call = mod.get_global_var('func_1842')
func_1843_call = mutated_mod.get_global_var('func_1843')
call_6790 = func_1842_call()
call_6791 = func_1842_call()
output = call_6790
output2 = call_6791
func_6793 = relay.Function([], output)
mod['func_6793'] = func_6793
mod = relay.transform.InferType()(mod)
mutated_mod['func_6793'] = func_6793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6793_call = mutated_mod.get_global_var('func_6793')
call_6794 = func_6793_call()
output = call_6794
func_6795 = relay.Function([], output)
mutated_mod['func_6795'] = func_6795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5836_call = mod.get_global_var('func_5836')
func_5837_call = mutated_mod.get_global_var('func_5837')
call_6815 = relay.TupleGetItem(func_5836_call(), 0)
call_6816 = relay.TupleGetItem(func_5837_call(), 0)
func_304_call = mod.get_global_var('func_304')
func_306_call = mutated_mod.get_global_var('func_306')
call_6852 = func_304_call()
call_6853 = func_304_call()
func_2980_call = mod.get_global_var('func_2980')
func_2982_call = mutated_mod.get_global_var('func_2982')
call_6857 = relay.TupleGetItem(func_2980_call(), 1)
call_6858 = relay.TupleGetItem(func_2982_call(), 1)
output = relay.Tuple([call_6815,call_6852,call_6857,])
output2 = relay.Tuple([call_6816,call_6853,call_6858,])
func_6861 = relay.Function([], output)
mod['func_6861'] = func_6861
mod = relay.transform.InferType()(mod)
output = func_6861()
func_6862 = relay.Function([], output)
mutated_mod['func_6862'] = func_6862
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6892 = relay.var("var_6892", dtype = "uint8", shape = (12, 4, 16))#candidate|6892|(12, 4, 16)|var|uint8
var_6893 = relay.var("var_6893", dtype = "uint8", shape = (12, 4, 16))#candidate|6893|(12, 4, 16)|var|uint8
bop_6894 = relay.subtract(var_6892.astype('uint8'), relay.reshape(var_6893.astype('uint8'), relay.shape_of(var_6892))) # shape=(12, 4, 16)
func_4093_call = mod.get_global_var('func_4093')
func_4095_call = mutated_mod.get_global_var('func_4095')
call_6909 = func_4093_call()
call_6910 = func_4093_call()
output = relay.Tuple([bop_6894,call_6909,])
output2 = relay.Tuple([bop_6894,call_6910,])
func_6922 = relay.Function([var_6892,var_6893,], output)
mod['func_6922'] = func_6922
mod = relay.transform.InferType()(mod)
mutated_mod['func_6922'] = func_6922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6922_call = mutated_mod.get_global_var('func_6922')
var_6924 = relay.var("var_6924", dtype = "uint8", shape = (12, 4, 16))#candidate|6924|(12, 4, 16)|var|uint8
var_6925 = relay.var("var_6925", dtype = "uint8", shape = (12, 4, 16))#candidate|6925|(12, 4, 16)|var|uint8
call_6923 = func_6922_call(var_6924,var_6925,)
output = call_6923
func_6926 = relay.Function([var_6924,var_6925,], output)
mutated_mod['func_6926'] = func_6926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2414_call = mod.get_global_var('func_2414')
func_2416_call = mutated_mod.get_global_var('func_2416')
call_6973 = relay.TupleGetItem(func_2414_call(), 0)
call_6974 = relay.TupleGetItem(func_2416_call(), 0)
func_6922_call = mod.get_global_var('func_6922')
func_6926_call = mutated_mod.get_global_var('func_6926')
const_6981 = relay.const([[-5,5,9,7,-1,10,2,5,-3,5,7,7,-9,7,-6,-4,-6,-3,8,-4,-8,10,6,-7,-4,-8,-8,-9,5,-8,-4,4,-3,4,-8,2,-7,-6,-8,1,-7,5,6,-4,-1,-10,7,7,-2,1,3,5,-8,2,-4,-9,4,8,-1,8,7,1,3,-3,-8,4,10,1,8,3,6,3,-10,-7,5,5,5,-5,-3,-5,3,-2,7,-10,-7,-9,8,5,4,1,9,-1,-1,5,5,6],[-7,10,4,-3,4,5,5,-10,-4,-8,6,-7,6,-2,2,-10,6,7,1,-2,1,4,9,-4,-2,6,-4,6,7,-10,6,9,1,4,5,4,3,-1,4,5,-2,6,4,-5,-10,9,4,-7,-4,-6,7,5,9,-4,5,-1,-10,2,-8,4,-1,-3,-3,-9,-1,7,6,8,2,-10,-1,4,9,7,5,7,-6,-1,1,7,-7,-8,6,10,-7,-5,-5,-2,-6,-4,-10,-5,1,5,-7,4],[7,-9,-9,9,1,-4,4,1,-5,-1,7,-1,-3,2,1,6,-9,8,-3,-4,2,3,6,-6,-10,-5,-2,-7,5,4,7,-3,-6,2,10,6,-6,8,2,2,-10,8,3,6,5,3,2,8,-7,-7,-8,10,1,-5,-1,-4,-2,-2,10,-3,10,6,-10,-9,-5,-3,-1,-7,1,5,9,-5,-4,5,5,-8,2,6,-10,-8,-1,-10,-3,5,10,-6,-3,-9,-7,10,2,6,4,5,-7,1],[-5,-2,-7,-2,9,6,-8,1,-9,9,1,-5,-7,8,-5,-6,9,7,-5,3,-7,-7,1,-10,9,2,-5,4,7,-10,1,1,1,6,-6,-3,-7,8,8,-10,9,8,9,10,4,-8,-3,6,8,-4,-10,-7,-7,7,-7,6,-1,2,6,5,1,6,-4,-1,-4,-7,2,-3,1,8,-1,5,-7,-1,10,-3,-1,8,1,8,-4,2,-8,-7,-9,8,7,1,10,-9,9,-3,2,8,1,-1],[-10,1,9,9,-10,7,10,-5,9,-3,9,1,-7,5,6,3,10,-7,9,-9,5,-10,4,-5,1,-3,6,-2,-6,1,6,9,-5,6,-2,-6,-3,-10,-4,-1,-7,-7,-10,-5,7,-8,1,8,-2,1,1,1,-6,2,7,6,8,6,2,6,-9,-2,-2,8,7,7,7,-4,8,2,9,-1,1,7,-3,1,-7,-4,-3,2,10,-8,7,1,-5,-5,2,3,5,5,3,2,10,7,-6,3],[-8,4,-2,3,1,4,-5,-5,5,10,7,-5,6,2,1,-10,6,-4,-3,6,6,5,4,-2,3,8,6,9,-7,5,-6,-7,-9,9,-8,5,-6,5,-2,1,-1,-7,4,10,-5,-9,8,-3,9,-10,-8,2,7,6,-6,-5,7,5,-8,-3,8,5,-2,-6,2,-7,-2,6,6,-9,8,1,-7,-7,9,-9,-5,-4,3,-7,7,5,3,-9,3,1,-3,7,9,5,7,7,-8,-9,3,6],[-10,-9,4,1,-3,9,7,6,-1,3,6,-1,1,5,-8,3,-6,10,-8,7,5,9,-1,7,-5,3,-8,-6,-4,4,6,9,-10,9,-2,-1,-2,9,5,-9,-6,-4,7,-5,10,5,9,-7,-5,-10,5,-3,4,-2,10,1,-4,-2,2,-3,9,10,4,-8,4,-3,1,-5,10,6,-1,-7,2,7,7,10,-10,3,-8,2,-2,10,-2,10,4,-3,-3,-1,8,-10,-8,10,-1,-1,-7,-10],[9,-2,-6,-3,6,-7,-6,3,6,10,4,-3,4,-3,-8,-10,10,6,-4,-8,6,-1,-4,10,-10,4,-2,-10,-3,-9,-3,-8,3,-10,-6,9,-4,6,-5,-5,-9,-10,10,-9,-2,-5,-7,9,-10,7,7,-10,6,-6,4,-7,-4,4,-8,8,1,-4,-8,-10,-10,-4,5,-8,10,2,-9,7,-8,9,5,-6,9,-7,-3,-5,6,-1,-1,-9,-5,5,2,9,-2,-5,-4,-3,1,1,-7,-8]], dtype = "uint8")#candidate|6981|(8, 96)|const|uint8
call_6980 = relay.TupleGetItem(func_6922_call(relay.reshape(const_6981.astype('uint8'), [12, 4, 16]), relay.reshape(const_6981.astype('uint8'), [12, 4, 16]), ), 0)
call_6982 = relay.TupleGetItem(func_6926_call(relay.reshape(const_6981.astype('uint8'), [12, 4, 16]), relay.reshape(const_6981.astype('uint8'), [12, 4, 16]), ), 0)
var_6998 = relay.var("var_6998", dtype = "uint8", shape = (8, 96))#candidate|6998|(8, 96)|var|uint8
bop_6999 = relay.bitwise_and(const_6981.astype('uint8'), relay.reshape(var_6998.astype('uint8'), relay.shape_of(const_6981))) # shape=(8, 96)
output = relay.Tuple([call_6973,call_6980,bop_6999,])
output2 = relay.Tuple([call_6974,call_6982,bop_6999,])
F = relay.Function([var_6998,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_6998,], output2)
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
