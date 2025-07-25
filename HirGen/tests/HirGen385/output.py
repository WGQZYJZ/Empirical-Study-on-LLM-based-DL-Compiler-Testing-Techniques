import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_378 = relay.var("var_378", dtype = "int32", shape = (1, 15, 2))#candidate|378|(1, 15, 2)|var|int32
const_379 = relay.const([[[-4,-10],[-2,-9],[7,7],[-4,-3],[-1,-1],[9,3],[10,3],[-10,-5],[-6,1],[6,-3],[1,-10],[-8,1],[5,-10],[-1,-10],[-8,-2]],[[-3,-5],[2,9],[3,2],[3,-10],[-4,-10],[6,5],[-2,-10],[-9,-9],[1,-3],[9,2],[5,7],[-5,-7],[-9,-8],[-7,-2],[-8,-9]],[[7,9],[-3,3],[-4,5],[9,5],[8,-3],[-1,2],[3,-8],[8,-8],[-7,-5],[9,4],[4,-5],[1,9],[4,-8],[4,-6],[6,10]],[[1,-3],[6,9],[-7,-1],[2,6],[-7,-5],[-8,7],[-3,-10],[7,6],[-9,6],[-6,-1],[10,4],[9,5],[4,9],[3,3],[-1,6]],[[5,5],[1,-9],[6,2],[5,8],[-3,-2],[-5,8],[-8,-5],[-7,8],[4,-6],[-3,-4],[7,7],[-1,8],[9,2],[2,1],[2,-1]],[[-6,-1],[-10,-5],[-3,6],[-6,-4],[7,10],[3,-8],[-3,-4],[-3,-6],[-2,9],[-3,9],[-5,8],[7,10],[-5,7],[-4,10],[6,-4]],[[9,-9],[-4,-6],[-5,5],[-9,3],[6,-9],[-6,8],[5,-7],[3,9],[-9,6],[-9,4],[-7,-3],[-1,-4],[2,7],[-4,-7],[-2,10]],[[-6,-7],[9,10],[-6,-9],[-3,-3],[3,-1],[-3,-4],[-1,7],[-3,-9],[6,-6],[1,-3],[2,2],[-8,-10],[-2,-7],[-1,-5],[-10,-6]]], dtype = "int32")#candidate|379|(8, 15, 2)|const|int32
bop_380 = relay.not_equal(var_378.astype('bool'), const_379.astype('bool')) # shape=(8, 15, 2)
uop_386 = relay.sigmoid(var_378.astype('float64')) # shape=(1, 15, 2)
var_411 = relay.var("var_411", dtype = "float64", shape = (10, 15, 2))#candidate|411|(10, 15, 2)|var|float64
bop_412 = relay.floor_mod(uop_386.astype('float64'), var_411.astype('float64')) # shape=(10, 15, 2)
output = relay.Tuple([bop_380,bop_412,])
output2 = relay.Tuple([bop_380,bop_412,])
func_426 = relay.Function([var_378,var_411,], output)
mod['func_426'] = func_426
mod = relay.transform.InferType()(mod)
mutated_mod['func_426'] = func_426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_426_call = mutated_mod.get_global_var('func_426')
var_428 = relay.var("var_428", dtype = "int32", shape = (1, 15, 2))#candidate|428|(1, 15, 2)|var|int32
var_429 = relay.var("var_429", dtype = "float64", shape = (10, 15, 2))#candidate|429|(10, 15, 2)|var|float64
call_427 = func_426_call(var_428,var_429,)
output = call_427
func_430 = relay.Function([var_428,var_429,], output)
mutated_mod['func_430'] = func_430
mutated_mod = relay.transform.InferType()(mutated_mod)
var_450 = relay.var("var_450", dtype = "uint32", shape = ())#candidate|450|()|var|uint32
const_451 = relay.const([[[4,-7,-6,5,7,-7,9,-6,-4,1],[-3,-1,-8,-3,-8,7,7,-10,7,10],[-1,4,-4,-3,5,10,-1,-8,2,4],[-10,-4,6,-1,-9,6,-2,2,-1,4],[-10,-3,-5,-2,4,-9,-6,3,-6,5]],[[-5,-5,-1,3,-1,7,1,-4,3,-5],[1,-1,-8,-9,9,8,-4,3,2,-1],[-2,4,-10,-2,-6,2,-1,-6,-7,3],[-10,-4,-6,4,-4,10,-1,1,-7,-6],[8,-2,-1,9,-5,8,5,-10,8,10]],[[-8,5,-9,3,-9,-8,-9,9,-9,9],[-3,9,-6,1,-4,-5,-3,2,-7,7],[5,5,6,-3,-2,-10,9,3,8,-1],[-4,3,-7,9,-1,1,2,10,-10,4],[5,-7,3,2,-1,-4,-9,4,3,9]],[[-10,9,-8,1,-2,-10,-8,1,-4,-3],[-6,-3,5,1,1,-3,2,-4,-3,-8],[9,-3,-6,10,-9,-6,1,10,-9,5],[10,-2,10,-5,-10,-7,5,-5,6,1],[-10,10,8,-7,-2,-6,10,7,3,-2]],[[-8,-3,-1,-2,-4,2,-9,5,-6,-4],[-7,-1,8,7,-3,-6,10,-4,8,9],[8,-7,-6,4,-7,10,-9,-10,-10,-10],[-8,4,6,10,-3,-7,10,5,8,-10],[8,-10,-1,-3,9,-6,10,4,9,1]]], dtype = "uint32")#candidate|451|(5, 5, 10)|const|uint32
bop_452 = relay.logical_xor(var_450.astype('uint32'), const_451.astype('uint32')) # shape=(5, 5, 10)
func_426_call = mod.get_global_var('func_426')
func_430_call = mutated_mod.get_global_var('func_430')
var_461 = relay.var("var_461", dtype = "int32", shape = (30,))#candidate|461|(30,)|var|int32
const_462 = relay.const([[2.200212,-0.656378,0.752597,-8.430066,-2.510028,0.815985,-1.997301,-8.916009,-3.245743,-2.340380,8.840331,4.119776,4.270845,7.853381,0.824100,8.981358,4.629108,-6.523371,-0.051825,1.279362,-7.827479,1.593368,-4.406029,0.949172,0.923996,-2.227237,-5.333725,-4.294066,-2.686453,-9.033097],[8.814064,1.862657,2.162245,3.523865,-8.465106,-1.508783,0.319491,-4.062521,0.203210,8.241683,0.960054,7.156990,5.893047,2.514638,8.416543,4.307774,7.893050,3.837344,-7.274904,3.714459,-1.828219,6.998375,8.105151,7.914503,1.176694,8.062414,-3.179721,0.781033,-4.572838,-4.055442],[-0.285225,-9.398925,-9.990080,-6.449807,6.683275,6.949464,-4.901118,4.856635,-7.708364,-3.493942,2.471440,-0.833511,0.723775,0.482780,-6.207801,9.806594,4.765829,7.543639,-5.618580,-8.065395,5.532035,1.890311,-3.106423,4.974456,8.958767,7.725064,4.035937,-9.563982,8.889701,-3.600412],[1.488613,-5.129273,-0.013447,-9.805226,2.073493,-8.949356,8.391874,-9.562973,-0.411293,-7.312322,-7.362245,2.061448,-3.678225,-5.634607,0.873081,1.451188,-4.438572,-8.877537,1.089960,5.884948,4.731598,7.793036,0.490031,6.759997,6.897651,7.164007,1.202884,4.751478,0.383079,0.333505],[8.627252,8.280107,-3.990961,-4.603214,0.033994,-4.012132,4.876199,3.709141,-4.518210,-6.432156,-3.568243,7.170196,-6.259114,4.781701,-9.435741,8.678620,-9.131162,7.728090,-1.690294,-7.172505,-5.150760,-4.416900,4.006973,-0.467866,-1.579195,8.227060,4.595110,-0.427023,-9.993958,0.837962],[-0.503622,-0.081327,4.250774,9.565835,6.403582,1.231947,1.872788,5.670322,3.571925,-2.827337,-8.069283,6.660194,-4.958259,-5.814041,4.745845,9.486047,-2.850540,-7.526070,5.426347,8.208902,-3.773557,-3.197623,-9.304139,-5.728964,-6.051576,-4.641874,-4.488336,-0.457557,0.852010,9.524486],[-1.630495,4.949343,-2.559604,-0.430575,9.202950,-1.250415,7.273984,0.111788,-4.813238,7.113070,-4.551742,-1.638603,5.395324,8.756657,8.486526,-7.047949,2.666583,-9.202018,7.344035,-7.115913,-3.845847,-7.897520,7.048571,6.170637,4.996852,-0.435151,-1.135970,2.140961,1.955027,4.443845],[8.595281,-0.407348,0.811568,6.597310,-9.951016,4.401204,-7.635934,-7.245950,-4.866618,-9.208441,-2.130180,6.591674,1.079526,3.500945,-2.832916,5.750521,-9.541122,-5.007548,-5.530691,-8.675078,3.037394,2.432713,-4.910220,-9.265112,1.679092,-8.275732,6.310027,1.097757,-5.765661,-6.057961],[0.372719,6.062593,6.280764,0.034337,7.513003,-0.208494,4.039332,-6.564805,0.228721,-6.786540,6.218776,4.544584,4.854803,6.215685,6.509179,-3.397352,4.599449,-1.270600,6.673717,-4.765265,2.348585,-2.415002,-2.792457,-8.478392,9.330787,6.883592,-4.019286,3.833043,8.931278,8.801614],[-0.901142,1.740294,0.493329,3.922237,8.490188,9.642785,-3.853133,0.322520,6.740916,1.002262,8.149010,8.997760,6.992818,1.938615,-3.716660,6.182445,-0.801214,-8.888178,-9.608740,-3.282895,-4.860233,-6.890507,3.666066,5.406347,-4.580239,5.305590,7.841916,9.216250,-8.305114,4.786181]], dtype = "float64")#candidate|462|(10, 30)|const|float64
call_460 = relay.TupleGetItem(func_426_call(relay.reshape(var_461.astype('int32'), [1, 15, 2]), relay.reshape(const_462.astype('float64'), [10, 15, 2]), ), 0)
call_463 = relay.TupleGetItem(func_430_call(relay.reshape(var_461.astype('int32'), [1, 15, 2]), relay.reshape(const_462.astype('float64'), [10, 15, 2]), ), 0)
bop_466 = relay.floor_divide(const_462.astype('float32'), var_461.astype('float32')) # shape=(10, 30)
output = relay.Tuple([bop_452,call_460,bop_466,])
output2 = relay.Tuple([bop_452,call_463,bop_466,])
func_480 = relay.Function([var_450,var_461,], output)
mod['func_480'] = func_480
mod = relay.transform.InferType()(mod)
mutated_mod['func_480'] = func_480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_480_call = mutated_mod.get_global_var('func_480')
var_482 = relay.var("var_482", dtype = "uint32", shape = ())#candidate|482|()|var|uint32
var_483 = relay.var("var_483", dtype = "int32", shape = (30,))#candidate|483|(30,)|var|int32
call_481 = func_480_call(var_482,var_483,)
output = call_481
func_484 = relay.Function([var_482,var_483,], output)
mutated_mod['func_484'] = func_484
mutated_mod = relay.transform.InferType()(mutated_mod)
const_744 = relay.const([[[-7,-2,-7,6,4],[4,9,4,-9,8],[9,-8,-10,-6,-10],[9,-7,6,10,2],[1,9,2,-6,6],[-1,-7,4,9,-10],[-2,-4,2,6,1],[-7,4,4,7,8],[-5,-10,9,10,3],[-5,-1,-5,9,6],[-9,-4,-6,10,-10],[9,-7,-8,3,2],[-9,1,6,-6,9],[-6,-4,-1,9,-4],[-10,-4,3,3,9]],[[-2,-4,2,-10,6],[-10,-8,-3,5,-2],[10,-3,1,8,2],[1,8,6,7,8],[-9,-6,-1,8,2],[4,-4,-8,-2,10],[4,7,-9,3,1],[9,-10,-7,-3,-6],[6,9,-8,6,-5],[-4,-10,-2,4,-4],[7,-6,-6,7,-9],[8,-6,7,6,-3],[-2,10,8,2,7],[10,7,10,-1,7],[-3,-7,-2,10,10]],[[10,2,5,-2,-3],[-2,3,-9,5,2],[-9,-8,2,1,-9],[5,2,-7,-9,-3],[-8,-7,4,-3,-7],[-2,-8,3,10,1],[-2,9,8,-2,-7],[-1,-9,5,4,2],[-3,-8,-5,-2,-2],[4,-3,-1,-9,8],[-5,10,-5,7,2],[-3,-6,-7,-1,-5],[2,-8,-2,-6,1],[8,10,9,-4,-9],[10,3,-2,-8,-7]],[[-5,-4,-6,3,9],[3,-9,7,10,-6],[10,-10,1,-3,-4],[-2,1,-3,2,8],[-9,1,6,8,1],[-7,-2,-6,-7,-2],[9,-2,-1,7,1],[7,8,10,9,-2],[-3,-3,-3,10,6],[-3,-7,5,-9,3],[10,2,1,-4,1],[1,2,-3,-3,-7],[4,-5,-4,-10,5],[-3,-5,-4,8,-5],[1,-4,-9,10,-9]],[[-2,6,5,8,-4],[-1,9,-5,-2,-1],[3,6,7,-6,9],[3,-8,7,-2,1],[7,7,9,8,-5],[2,-3,5,4,-8],[-7,-4,-3,-10,-3],[2,-4,5,1,7],[-2,-3,-7,-6,10],[-6,8,-1,9,7],[4,-4,-10,-4,-2],[-8,1,-1,10,1],[-5,8,-7,4,2],[-1,-1,-5,-4,2],[9,2,1,-10,3]],[[4,10,-9,3,-4],[5,1,2,8,4],[-4,2,-5,-9,8],[6,-10,-4,-3,6],[-1,-5,-8,-10,-3],[-8,9,2,5,-9],[-5,-4,3,-8,4],[6,-5,-10,7,1],[4,8,-9,9,6],[-6,-5,8,8,-4],[7,10,10,5,7],[1,5,-7,2,10],[-8,-8,9,-2,-9],[-1,-6,-8,-10,8],[-9,1,10,10,-5]],[[-1,9,7,5,-6],[6,1,-10,-10,4],[-8,-9,-6,-8,-1],[7,8,-1,-5,-2],[1,10,-2,2,1],[-10,-10,-7,-7,5],[9,-10,-9,2,7],[6,-4,1,9,5],[-1,10,-5,-8,-1],[10,4,-7,-1,8],[2,8,-10,-1,-2],[8,3,-7,-4,-1],[-7,-7,1,5,-4],[1,-4,-4,-8,3],[3,-5,9,7,6]]], dtype = "int64")#candidate|744|(7, 15, 5)|const|int64
var_745 = relay.var("var_745", dtype = "int64", shape = (7, 15, 5))#candidate|745|(7, 15, 5)|var|int64
bop_746 = relay.maximum(const_744.astype('int64'), relay.reshape(var_745.astype('int64'), relay.shape_of(const_744))) # shape=(7, 15, 5)
func_480_call = mod.get_global_var('func_480')
func_484_call = mutated_mod.get_global_var('func_484')
var_751 = relay.var("var_751", dtype = "uint32", shape = ())#candidate|751|()|var|uint32
const_752 = relay.const([-4,5,-9,-3,3,-6,6,-6,-4,-9,1,10,10,2,-10,8,-6,-5,-3,5,4,6,1,-8,4,1,7,-5,-3,-2], dtype = "int32")#candidate|752|(30,)|const|int32
call_750 = relay.TupleGetItem(func_480_call(relay.reshape(var_751.astype('uint32'), []), relay.reshape(const_752.astype('int32'), [30,]), ), 0)
call_753 = relay.TupleGetItem(func_484_call(relay.reshape(var_751.astype('uint32'), []), relay.reshape(const_752.astype('int32'), [30,]), ), 0)
func_480_call = mod.get_global_var('func_480')
func_484_call = mutated_mod.get_global_var('func_484')
call_762 = relay.TupleGetItem(func_480_call(relay.reshape(var_751.astype('uint32'), []), relay.reshape(const_752.astype('int32'), [30,]), ), 0)
call_763 = relay.TupleGetItem(func_484_call(relay.reshape(var_751.astype('uint32'), []), relay.reshape(const_752.astype('int32'), [30,]), ), 0)
output = relay.Tuple([bop_746,call_750,var_751,const_752,call_762,])
output2 = relay.Tuple([bop_746,call_753,var_751,const_752,call_763,])
func_765 = relay.Function([var_745,var_751,], output)
mod['func_765'] = func_765
mod = relay.transform.InferType()(mod)
var_766 = relay.var("var_766", dtype = "int64", shape = (7, 15, 5))#candidate|766|(7, 15, 5)|var|int64
var_767 = relay.var("var_767", dtype = "uint32", shape = ())#candidate|767|()|var|uint32
output = func_765(var_766,var_767,)
func_768 = relay.Function([var_766,var_767,], output)
mutated_mod['func_768'] = func_768
mutated_mod = relay.transform.InferType()(mutated_mod)
var_815 = relay.var("var_815", dtype = "float64", shape = (14, 8, 13))#candidate|815|(14, 8, 13)|var|float64
uop_816 = relay.sin(var_815.astype('float64')) # shape=(14, 8, 13)
output = uop_816
output2 = uop_816
func_819 = relay.Function([var_815,], output)
mod['func_819'] = func_819
mod = relay.transform.InferType()(mod)
var_820 = relay.var("var_820", dtype = "float64", shape = (14, 8, 13))#candidate|820|(14, 8, 13)|var|float64
output = func_819(var_820)
func_821 = relay.Function([var_820], output)
mutated_mod['func_821'] = func_821
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1245 = relay.const([[[-2,8,4,-6,2,9,-2],[3,-2,1,-2,-6,-1,-1],[10,2,2,1,-3,7,6],[-3,-7,-8,-9,-2,-8,-5],[-5,-9,-6,-6,10,-4,-6]],[[-6,9,1,-10,-6,-10,9],[9,6,-2,-8,7,-7,-1],[9,4,-10,-9,-8,1,-7],[4,-10,9,6,4,-10,-6],[-7,-9,-4,6,-5,-6,3]],[[9,-10,-5,6,8,-5,-4],[1,-3,-10,-9,-3,-10,-9],[3,4,1,3,-4,-1,-10],[3,3,-7,4,-9,2,7],[2,6,9,5,4,7,-8]],[[-8,-9,2,5,-10,-7,-4],[-1,-10,-9,8,6,8,-3],[6,7,10,5,8,3,2],[7,8,-7,10,-5,-3,-2],[-1,-8,-8,2,-1,-2,-8]],[[-8,-7,-6,-4,-3,10,3],[-9,6,9,6,1,5,-5],[-2,4,-5,7,-5,-6,-5],[6,-2,10,2,2,-7,6],[-6,3,-5,-7,9,6,5]],[[4,-10,6,5,10,5,7],[-6,8,-3,-7,9,3,-10],[-1,10,-2,8,-2,4,-10],[5,-5,-8,2,-3,4,-7],[-9,7,-9,-7,-7,9,-6]],[[3,-3,3,9,10,-7,-4],[-6,-9,5,5,2,5,7],[-9,6,-10,10,9,-7,3],[-4,4,-8,-3,8,5,1],[1,3,-10,-4,9,4,-5]],[[9,-6,5,-2,-4,5,4],[3,-1,3,4,4,4,2],[-3,2,5,6,-7,-2,-5],[2,-7,5,7,2,1,-9],[-1,-6,6,-8,-3,2,3]],[[8,10,-7,5,7,-10,-3],[-4,6,3,-2,10,-1,-4],[-3,-6,-5,3,7,4,9],[-10,-4,7,2,2,3,5],[4,-9,-6,-8,-3,-5,-8]],[[-2,-4,1,1,-8,2,-8],[-1,-8,-10,-10,4,-1,8],[7,8,2,6,-8,3,-9],[-5,9,7,10,6,8,-7],[-7,9,-10,-5,-7,-8,-7]],[[2,-8,-4,2,8,-3,-2],[-6,-1,4,9,7,8,7],[8,9,-4,8,7,1,1],[-2,4,2,1,7,1,5],[7,-7,8,6,6,7,-3]],[[-9,-2,-7,-6,-6,-6,6],[7,9,3,-9,-6,10,9],[3,8,6,10,-10,4,-5],[9,8,-5,7,4,9,-3],[2,-10,3,9,-10,5,-7]],[[-4,-7,-6,-8,-3,10,-3],[9,-10,5,8,-8,9,5],[-5,-3,5,-3,-5,3,-6],[-7,-2,4,-7,-1,-8,9],[-6,1,7,2,4,-6,-8]],[[6,3,-2,10,-8,4,-2],[-8,-10,-7,6,5,-7,-5],[7,-1,-7,8,9,7,5],[-7,-4,7,-9,-6,-8,5],[9,8,5,-1,-4,-4,-7]]], dtype = "uint64")#candidate|1245|(14, 5, 7)|const|uint64
var_1246 = relay.var("var_1246", dtype = "uint64", shape = (14, 5, 7))#candidate|1246|(14, 5, 7)|var|uint64
bop_1247 = relay.bitwise_or(const_1245.astype('uint64'), relay.reshape(var_1246.astype('uint64'), relay.shape_of(const_1245))) # shape=(14, 5, 7)
uop_1250 = relay.sin(const_1245.astype('float32')) # shape=(14, 5, 7)
var_1268 = relay.var("var_1268", dtype = "float32", shape = (14, 5, 7))#candidate|1268|(14, 5, 7)|var|float32
bop_1269 = relay.logical_or(uop_1250.astype('bool'), relay.reshape(var_1268.astype('bool'), relay.shape_of(uop_1250))) # shape=(14, 5, 7)
output = relay.Tuple([bop_1247,bop_1269,])
output2 = relay.Tuple([bop_1247,bop_1269,])
func_1273 = relay.Function([var_1246,var_1268,], output)
mod['func_1273'] = func_1273
mod = relay.transform.InferType()(mod)
mutated_mod['func_1273'] = func_1273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1273_call = mutated_mod.get_global_var('func_1273')
var_1275 = relay.var("var_1275", dtype = "uint64", shape = (14, 5, 7))#candidate|1275|(14, 5, 7)|var|uint64
var_1276 = relay.var("var_1276", dtype = "float32", shape = (14, 5, 7))#candidate|1276|(14, 5, 7)|var|float32
call_1274 = func_1273_call(var_1275,var_1276,)
output = call_1274
func_1277 = relay.Function([var_1275,var_1276,], output)
mutated_mod['func_1277'] = func_1277
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1379 = relay.const([[[0.599767,-3.809668],[7.263487,8.308851],[-9.718729,-1.993844],[5.162966,5.730925],[5.916879,6.550161],[-2.259904,5.517298],[0.505196,-0.319312]],[[-6.711694,-4.378226],[-5.804933,-4.461272],[6.760485,7.352247],[8.615165,-5.111464],[-3.688245,-4.292337],[-2.596320,-1.638732],[0.829030,-5.020148]],[[-9.530484,-6.818074],[4.260832,9.159301],[1.355038,1.360297],[7.919240,7.598996],[3.634755,9.069023],[7.394302,7.531779],[2.544542,9.723916]],[[-0.019013,-0.091230],[-4.281876,2.865475],[4.828101,7.517842],[9.036520,9.481704],[0.962857,8.103792],[4.280489,3.719060],[-4.050231,-6.590789]],[[-0.946161,2.231988],[9.258940,-0.643858],[-3.014253,4.005171],[-1.924351,8.449843],[-7.106948,-2.090008],[1.233054,-3.114904],[-4.276821,0.728177]],[[-9.564998,7.270734],[2.184034,0.987128],[-7.662703,-1.285069],[-9.387829,-3.930085],[0.076077,-5.255116],[-8.491122,9.241501],[-6.512489,-4.355469]],[[1.277748,-4.808535],[9.282368,5.224446],[-0.179350,-1.474243],[-5.626660,3.019586],[-8.652920,9.279279],[3.611881,2.588362],[-6.473795,0.401453]]], dtype = "float64")#candidate|1379|(7, 7, 2)|const|float64
uop_1380 = relay.log10(const_1379.astype('float64')) # shape=(7, 7, 2)
uop_1395 = relay.erf(const_1379.astype('float64')) # shape=(7, 7, 2)
bop_1406 = relay.subtract(uop_1380.astype('int64'), relay.reshape(uop_1395.astype('int64'), relay.shape_of(uop_1380))) # shape=(7, 7, 2)
func_819_call = mod.get_global_var('func_819')
func_821_call = mutated_mod.get_global_var('func_821')
var_1410 = relay.var("var_1410", dtype = "float64", shape = (1456,))#candidate|1410|(1456,)|var|float64
call_1409 = func_819_call(relay.reshape(var_1410.astype('float64'), [14, 8, 13]))
call_1411 = func_819_call(relay.reshape(var_1410.astype('float64'), [14, 8, 13]))
func_765_call = mod.get_global_var('func_765')
func_768_call = mutated_mod.get_global_var('func_768')
var_1413 = relay.var("var_1413", dtype = "int64", shape = (525, 1))#candidate|1413|(525, 1)|var|int64
var_1414 = relay.var("var_1414", dtype = "uint32", shape = ())#candidate|1414|()|var|uint32
call_1412 = relay.TupleGetItem(func_765_call(relay.reshape(var_1413.astype('int64'), [7, 15, 5]), relay.reshape(var_1414.astype('uint32'), []), ), 0)
call_1415 = relay.TupleGetItem(func_768_call(relay.reshape(var_1413.astype('int64'), [7, 15, 5]), relay.reshape(var_1414.astype('uint32'), []), ), 0)
func_765_call = mod.get_global_var('func_765')
func_768_call = mutated_mod.get_global_var('func_768')
call_1425 = relay.TupleGetItem(func_765_call(relay.reshape(var_1413.astype('int64'), [7, 15, 5]), relay.reshape(var_1414.astype('uint32'), []), ), 4)
call_1426 = relay.TupleGetItem(func_768_call(relay.reshape(var_1413.astype('int64'), [7, 15, 5]), relay.reshape(var_1414.astype('uint32'), []), ), 4)
output = relay.Tuple([bop_1406,call_1409,var_1410,call_1412,var_1413,var_1414,call_1425,])
output2 = relay.Tuple([bop_1406,call_1411,var_1410,call_1415,var_1413,var_1414,call_1426,])
func_1433 = relay.Function([var_1410,var_1413,var_1414,], output)
mod['func_1433'] = func_1433
mod = relay.transform.InferType()(mod)
mutated_mod['func_1433'] = func_1433
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1433_call = mutated_mod.get_global_var('func_1433')
var_1435 = relay.var("var_1435", dtype = "float64", shape = (1456,))#candidate|1435|(1456,)|var|float64
var_1436 = relay.var("var_1436", dtype = "int64", shape = (525, 1))#candidate|1436|(525, 1)|var|int64
var_1437 = relay.var("var_1437", dtype = "uint32", shape = ())#candidate|1437|()|var|uint32
call_1434 = func_1433_call(var_1435,var_1436,var_1437,)
output = call_1434
func_1438 = relay.Function([var_1435,var_1436,var_1437,], output)
mutated_mod['func_1438'] = func_1438
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1449 = relay.var("var_1449", dtype = "float64", shape = (6, 6, 6))#candidate|1449|(6, 6, 6)|var|float64
const_1450 = relay.const([[[-7.529635,-6.621683,-8.831457,6.246087,-7.023382,2.898333],[-3.940288,0.428928,-2.974105,-0.525329,5.146650,-1.387492],[-5.362370,-4.409395,-6.426957,-0.079383,-8.618657,-2.599788],[-1.729131,3.694880,-3.850490,6.419772,2.395287,6.054996],[-9.611985,7.787183,-5.317577,2.019612,-6.751753,3.044175],[9.918232,-9.791531,-1.943227,-2.086043,-1.538644,9.546455]],[[-9.147269,-3.769330,7.836574,-1.420984,1.657926,4.173671],[1.185234,-1.539896,-7.301211,-7.667920,3.284825,5.124028],[-6.113697,-1.968145,9.746639,9.958820,2.620172,-4.178300],[7.865385,-4.585876,-9.521905,8.422129,-6.339453,2.907434],[1.254186,-7.132549,-1.547193,-8.521092,-3.323369,-4.086300],[-9.484266,6.496296,2.501312,-0.200675,-1.854055,7.014175]],[[-7.918358,6.679389,-2.186528,-8.338179,-5.256334,2.646458],[-5.924144,6.592496,-7.034558,2.868547,3.736612,-7.721543],[-8.403769,-6.126899,8.987846,6.016263,-4.665265,-1.452097],[4.254827,-8.203769,-4.008598,5.152509,7.762805,3.620214],[-8.912289,-1.891667,6.202762,-0.669459,4.767167,0.282004],[-9.541659,-4.445798,2.389933,4.047636,4.123948,-0.059942]],[[0.589165,5.802224,6.378567,8.739059,8.716830,7.032826],[-8.400116,-2.168490,-4.816028,0.482830,-6.480647,6.638894],[-1.085417,-7.654430,-0.732950,1.054571,-8.892617,-7.469599],[5.583797,5.389546,3.260398,-8.159245,-2.942616,9.404111],[-5.570692,3.448521,0.585410,-6.700333,-2.295543,7.188077],[3.242510,-6.986197,4.015388,0.415479,-8.591791,7.533291]],[[-8.045715,-2.760795,-4.680019,2.486713,-9.577557,6.439882],[-6.066109,2.579785,3.193469,4.106931,-8.782228,-9.560939],[8.997340,-5.343513,0.496842,1.721192,8.638210,-3.937856],[-8.607531,-4.553477,9.235695,-0.927523,8.017457,-7.587529],[-0.942024,-6.651776,7.059533,8.912217,-8.238571,6.017679],[3.969536,4.745532,-4.052341,7.556362,-7.895793,7.427989]],[[2.059994,6.801303,6.761158,9.881369,7.629055,-5.115366],[3.840448,0.787361,-7.218520,4.686376,-3.751752,-3.969109],[-3.395408,4.304598,-7.051099,-0.438895,-5.944619,-5.955415],[9.056471,2.510892,7.158875,-4.511494,5.569259,8.537368],[-8.926632,-3.527720,9.153662,7.753125,-1.326407,-6.391459],[3.555349,-7.308549,-2.228368,2.893443,5.657075,7.187342]]], dtype = "float64")#candidate|1450|(6, 6, 6)|const|float64
bop_1451 = relay.mod(var_1449.astype('float64'), relay.reshape(const_1450.astype('float64'), relay.shape_of(var_1449))) # shape=(6, 6, 6)
func_480_call = mod.get_global_var('func_480')
func_484_call = mutated_mod.get_global_var('func_484')
var_1456 = relay.var("var_1456", dtype = "uint32", shape = ())#candidate|1456|()|var|uint32
const_1457 = relay.const([[-8,-3,-2,5,-6,-2],[-8,-7,10,-6,-2,-4],[5,-10,2,6,-4,-6],[8,6,2,1,2,10],[1,-9,-2,7,-2,8]], dtype = "int32")#candidate|1457|(5, 6)|const|int32
call_1455 = relay.TupleGetItem(func_480_call(relay.reshape(var_1456.astype('uint32'), []), relay.reshape(const_1457.astype('int32'), [30,]), ), 2)
call_1458 = relay.TupleGetItem(func_484_call(relay.reshape(var_1456.astype('uint32'), []), relay.reshape(const_1457.astype('int32'), [30,]), ), 2)
output = relay.Tuple([bop_1451,call_1455,var_1456,const_1457,])
output2 = relay.Tuple([bop_1451,call_1458,var_1456,const_1457,])
func_1461 = relay.Function([var_1449,var_1456,], output)
mod['func_1461'] = func_1461
mod = relay.transform.InferType()(mod)
mutated_mod['func_1461'] = func_1461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1461_call = mutated_mod.get_global_var('func_1461')
var_1463 = relay.var("var_1463", dtype = "float64", shape = (6, 6, 6))#candidate|1463|(6, 6, 6)|var|float64
var_1464 = relay.var("var_1464", dtype = "uint32", shape = ())#candidate|1464|()|var|uint32
call_1462 = func_1461_call(var_1463,var_1464,)
output = call_1462
func_1465 = relay.Function([var_1463,var_1464,], output)
mutated_mod['func_1465'] = func_1465
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1708 = relay.var("var_1708", dtype = "float64", shape = (9, 7, 12))#candidate|1708|(9, 7, 12)|var|float64
uop_1709 = relay.log10(var_1708.astype('float64')) # shape=(9, 7, 12)
var_1719 = relay.var("var_1719", dtype = "float64", shape = (9, 7, 12))#candidate|1719|(9, 7, 12)|var|float64
bop_1720 = relay.right_shift(var_1708.astype('uint8'), relay.reshape(var_1719.astype('uint8'), relay.shape_of(var_1708))) # shape=(9, 7, 12)
uop_1723 = relay.asin(bop_1720.astype('float64')) # shape=(9, 7, 12)
var_1728 = relay.var("var_1728", dtype = "float64", shape = (9, 7, 12))#candidate|1728|(9, 7, 12)|var|float64
bop_1729 = relay.add(uop_1723.astype('int8'), relay.reshape(var_1728.astype('int8'), relay.shape_of(uop_1723))) # shape=(9, 7, 12)
output = relay.Tuple([uop_1709,bop_1729,])
output2 = relay.Tuple([uop_1709,bop_1729,])
func_1737 = relay.Function([var_1708,var_1719,var_1728,], output)
mod['func_1737'] = func_1737
mod = relay.transform.InferType()(mod)
var_1738 = relay.var("var_1738", dtype = "float64", shape = (9, 7, 12))#candidate|1738|(9, 7, 12)|var|float64
var_1739 = relay.var("var_1739", dtype = "float64", shape = (9, 7, 12))#candidate|1739|(9, 7, 12)|var|float64
var_1740 = relay.var("var_1740", dtype = "float64", shape = (9, 7, 12))#candidate|1740|(9, 7, 12)|var|float64
output = func_1737(var_1738,var_1739,var_1740,)
func_1741 = relay.Function([var_1738,var_1739,var_1740,], output)
mutated_mod['func_1741'] = func_1741
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1828 = relay.var("var_1828", dtype = "float64", shape = (2, 8, 8))#candidate|1828|(2, 8, 8)|var|float64
uop_1829 = relay.log10(var_1828.astype('float64')) # shape=(2, 8, 8)
uop_1855 = relay.sqrt(uop_1829.astype('float64')) # shape=(2, 8, 8)
bop_1864 = relay.less_equal(uop_1855.astype('bool'), relay.reshape(uop_1829.astype('bool'), relay.shape_of(uop_1855))) # shape=(2, 8, 8)
var_1879 = relay.var("var_1879", dtype = "float64", shape = (2, 8, 8))#candidate|1879|(2, 8, 8)|var|float64
bop_1880 = relay.logical_and(uop_1829.astype('bool'), relay.reshape(var_1879.astype('bool'), relay.shape_of(uop_1829))) # shape=(2, 8, 8)
func_1461_call = mod.get_global_var('func_1461')
func_1465_call = mutated_mod.get_global_var('func_1465')
const_1885 = relay.const([4.240664,-5.355477,4.132211,-2.383786,9.526954,-5.912444,7.880311,8.064570,-0.139136,7.434723,-0.108394,3.409886,-4.798431,-5.043369,1.479883,-8.018538,1.491722,-0.828939,1.137896,6.767411,-2.535398,-2.294560,0.504563,7.050553,-3.832024,4.465580,-0.158792,-5.412797,-3.318910,-4.303458,-8.477614,-0.611969,-9.095850,-9.477797,4.574264,-0.854573,-9.140345,1.352009,1.921295,4.369858,-2.483985,-7.286521,6.860813,9.198340,3.591051,-1.053787,-2.066196,6.689345,1.221827,-8.602826,8.914409,-8.079347,-2.024912,-3.485511,0.081183,3.070375,-7.332659,-5.250708,-7.146501,7.780653,-9.684475,5.567247,-9.547079,5.216175,4.383095,4.401311,-3.539708,-3.705695,3.643074,-7.520893,-0.665271,-6.153845,9.428475,8.523721,-9.621040,-3.324709,-9.744044,-7.096086,-6.996036,-6.988962,4.876099,0.880969,-6.804251,-9.153254,-4.423325,-6.525213,-3.859806,3.892122,2.232577,6.264626,3.696594,-7.442368,-1.138711,-1.109328,-5.097385,-8.507019,-2.998499,-5.219845,3.780153,3.451100,5.945779,-3.918442,-5.327030,-8.868839,-8.549789,-8.568215,1.107999,8.520402,3.584597,-7.211248,5.032367,6.127002,-2.367888,-5.186398,4.232748,3.481548,0.776213,-0.096569,0.554832,6.716790,1.581006,5.153049,3.304023,-3.850127,2.706211,-6.272011,7.230790,-0.112128,6.280901,6.477760,-0.990427,-8.617440,-0.162406,-4.347484,6.816787,-2.940313,9.003850,7.406472,-6.628585,5.017907,-4.416335,-3.187653,5.183858,-5.554999,0.351888,8.005354,-3.355447,8.166798,1.898183,0.859602,-0.740484,5.630876,1.926673,-1.968148,-7.602936,3.234278,7.606512,-6.946666,8.828154,-8.647173,-1.777928,-7.905483,8.096863,9.819405,1.077651,2.907917,-8.899255,6.464681,2.922070,-3.760152,8.557933,-1.566880,9.627236,-8.479005,0.341416,-2.034748,-6.328620,3.004501,-2.062635,-4.915148,0.797783,6.332902,-4.299525,7.081935,-5.979258,3.445994,-1.684739,0.327116,-8.336855,-5.460226,-3.895544,8.276162,6.750614,-4.529605,-6.600693,-3.393878,-0.280707,6.514765,-0.889138,-4.435141,-8.734395,9.359893,6.704017,4.619857,-5.070943,-5.256562,-1.299227,3.366472,-3.272607,8.205326,7.830336,-0.841422,-3.283883,-4.302963,-0.530075,1.522451], dtype = "float64")#candidate|1885|(216,)|const|float64
const_1886 = relay.const(7, dtype = "uint32")#candidate|1886|()|const|uint32
call_1884 = relay.TupleGetItem(func_1461_call(relay.reshape(const_1885.astype('float64'), [6, 6, 6]), relay.reshape(const_1886.astype('uint32'), []), ), 1)
call_1887 = relay.TupleGetItem(func_1465_call(relay.reshape(const_1885.astype('float64'), [6, 6, 6]), relay.reshape(const_1886.astype('uint32'), []), ), 1)
output = relay.Tuple([bop_1864,bop_1880,call_1884,const_1885,const_1886,])
output2 = relay.Tuple([bop_1864,bop_1880,call_1887,const_1885,const_1886,])
func_1888 = relay.Function([var_1828,var_1879,], output)
mod['func_1888'] = func_1888
mod = relay.transform.InferType()(mod)
var_1889 = relay.var("var_1889", dtype = "float64", shape = (2, 8, 8))#candidate|1889|(2, 8, 8)|var|float64
var_1890 = relay.var("var_1890", dtype = "float64", shape = (2, 8, 8))#candidate|1890|(2, 8, 8)|var|float64
output = func_1888(var_1889,var_1890,)
func_1891 = relay.Function([var_1889,var_1890,], output)
mutated_mod['func_1891'] = func_1891
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2019 = relay.const(-4.915191, dtype = "float32")#candidate|2019|()|const|float32
var_2020 = relay.var("var_2020", dtype = "float32", shape = (13, 1, 11))#candidate|2020|(13, 1, 11)|var|float32
bop_2021 = relay.divide(const_2019.astype('float32'), var_2020.astype('float32')) # shape=(13, 1, 11)
output = bop_2021
output2 = bop_2021
func_2025 = relay.Function([var_2020,], output)
mod['func_2025'] = func_2025
mod = relay.transform.InferType()(mod)
mutated_mod['func_2025'] = func_2025
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2026 = relay.var("var_2026", dtype = "float32", shape = (13, 1, 11))#candidate|2026|(13, 1, 11)|var|float32
func_2025_call = mutated_mod.get_global_var('func_2025')
call_2027 = func_2025_call(var_2026)
output = call_2027
func_2028 = relay.Function([var_2026], output)
mutated_mod['func_2028'] = func_2028
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2061 = relay.var("var_2061", dtype = "int16", shape = (11, 6, 9))#candidate|2061|(11, 6, 9)|var|int16
var_2062 = relay.var("var_2062", dtype = "int16", shape = (11, 6, 9))#candidate|2062|(11, 6, 9)|var|int16
bop_2063 = relay.greater_equal(var_2061.astype('bool'), relay.reshape(var_2062.astype('bool'), relay.shape_of(var_2061))) # shape=(11, 6, 9)
uop_2067 = relay.sigmoid(var_2062.astype('float64')) # shape=(11, 6, 9)
var_2074 = relay.var("var_2074", dtype = "int16", shape = (11, 6, 9))#candidate|2074|(11, 6, 9)|var|int16
bop_2075 = relay.left_shift(var_2062.astype('uint16'), relay.reshape(var_2074.astype('uint16'), relay.shape_of(var_2062))) # shape=(11, 6, 9)
bop_2078 = relay.less(uop_2067.astype('bool'), relay.reshape(var_2061.astype('bool'), relay.shape_of(uop_2067))) # shape=(11, 6, 9)
output = relay.Tuple([bop_2063,bop_2075,bop_2078,])
output2 = relay.Tuple([bop_2063,bop_2075,bop_2078,])
func_2083 = relay.Function([var_2061,var_2062,var_2074,], output)
mod['func_2083'] = func_2083
mod = relay.transform.InferType()(mod)
mutated_mod['func_2083'] = func_2083
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2083_call = mutated_mod.get_global_var('func_2083')
var_2085 = relay.var("var_2085", dtype = "int16", shape = (11, 6, 9))#candidate|2085|(11, 6, 9)|var|int16
var_2086 = relay.var("var_2086", dtype = "int16", shape = (11, 6, 9))#candidate|2086|(11, 6, 9)|var|int16
var_2087 = relay.var("var_2087", dtype = "int16", shape = (11, 6, 9))#candidate|2087|(11, 6, 9)|var|int16
call_2084 = func_2083_call(var_2085,var_2086,var_2087,)
output = call_2084
func_2088 = relay.Function([var_2085,var_2086,var_2087,], output)
mutated_mod['func_2088'] = func_2088
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2329 = relay.const([[[-5,8,-10,-10],[10,10,2,2],[5,-6,4,-8],[10,7,-9,-9],[-5,-6,9,-9]],[[9,-3,-5,6],[-5,-10,-10,-3],[6,8,-2,-10],[5,1,1,-5],[1,3,4,-8]],[[4,5,6,-4],[7,-10,10,-5],[5,1,6,-8],[5,-5,-3,-8],[-2,-2,-1,3]]], dtype = "uint8")#candidate|2329|(3, 5, 4)|const|uint8
var_2330 = relay.var("var_2330", dtype = "uint8", shape = (3, 5, 4))#candidate|2330|(3, 5, 4)|var|uint8
bop_2331 = relay.equal(const_2329.astype('bool'), relay.reshape(var_2330.astype('bool'), relay.shape_of(const_2329))) # shape=(3, 5, 4)
func_1461_call = mod.get_global_var('func_1461')
func_1465_call = mutated_mod.get_global_var('func_1465')
var_2342 = relay.var("var_2342", dtype = "float64", shape = (216,))#candidate|2342|(216,)|var|float64
var_2343 = relay.var("var_2343", dtype = "uint32", shape = ())#candidate|2343|()|var|uint32
call_2341 = relay.TupleGetItem(func_1461_call(relay.reshape(var_2342.astype('float64'), [6, 6, 6]), relay.reshape(var_2343.astype('uint32'), []), ), 3)
call_2344 = relay.TupleGetItem(func_1465_call(relay.reshape(var_2342.astype('float64'), [6, 6, 6]), relay.reshape(var_2343.astype('uint32'), []), ), 3)
output = relay.Tuple([bop_2331,call_2341,var_2342,var_2343,])
output2 = relay.Tuple([bop_2331,call_2344,var_2342,var_2343,])
func_2349 = relay.Function([var_2330,var_2342,var_2343,], output)
mod['func_2349'] = func_2349
mod = relay.transform.InferType()(mod)
mutated_mod['func_2349'] = func_2349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2349_call = mutated_mod.get_global_var('func_2349')
var_2351 = relay.var("var_2351", dtype = "uint8", shape = (3, 5, 4))#candidate|2351|(3, 5, 4)|var|uint8
var_2352 = relay.var("var_2352", dtype = "float64", shape = (216,))#candidate|2352|(216,)|var|float64
var_2353 = relay.var("var_2353", dtype = "uint32", shape = ())#candidate|2353|()|var|uint32
call_2350 = func_2349_call(var_2351,var_2352,var_2353,)
output = call_2350
func_2354 = relay.Function([var_2351,var_2352,var_2353,], output)
mutated_mod['func_2354'] = func_2354
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2580 = relay.var("var_2580", dtype = "float32", shape = (4, 4, 3))#candidate|2580|(4, 4, 3)|var|float32
uop_2581 = relay.sigmoid(var_2580.astype('float32')) # shape=(4, 4, 3)
func_480_call = mod.get_global_var('func_480')
func_484_call = mutated_mod.get_global_var('func_484')
const_2585 = relay.const(-10, dtype = "uint32")#candidate|2585|()|const|uint32
const_2586 = relay.const([[-7,-6,-8],[9,-6,4],[6,-3,6],[-9,2,-4],[-1,-7,-1],[5,-9,4],[-6,7,8],[9,5,-8],[1,7,-1],[10,-10,-1]], dtype = "int32")#candidate|2586|(10, 3)|const|int32
call_2584 = relay.TupleGetItem(func_480_call(relay.reshape(const_2585.astype('uint32'), []), relay.reshape(const_2586.astype('int32'), [30,]), ), 2)
call_2587 = relay.TupleGetItem(func_484_call(relay.reshape(const_2585.astype('uint32'), []), relay.reshape(const_2586.astype('int32'), [30,]), ), 2)
bop_2588 = relay.floor_divide(uop_2581.astype('float64'), relay.reshape(var_2580.astype('float64'), relay.shape_of(uop_2581))) # shape=(4, 4, 3)
uop_2594 = relay.asinh(uop_2581.astype('float32')) # shape=(4, 4, 3)
output = relay.Tuple([call_2584,const_2585,const_2586,bop_2588,uop_2594,])
output2 = relay.Tuple([call_2587,const_2585,const_2586,bop_2588,uop_2594,])
func_2601 = relay.Function([var_2580,], output)
mod['func_2601'] = func_2601
mod = relay.transform.InferType()(mod)
var_2602 = relay.var("var_2602", dtype = "float32", shape = (4, 4, 3))#candidate|2602|(4, 4, 3)|var|float32
output = func_2601(var_2602)
func_2603 = relay.Function([var_2602], output)
mutated_mod['func_2603'] = func_2603
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2742 = relay.var("var_2742", dtype = "float32", shape = (10, 8, 8))#candidate|2742|(10, 8, 8)|var|float32
uop_2743 = relay.cos(var_2742.astype('float32')) # shape=(10, 8, 8)
output = uop_2743
output2 = uop_2743
func_2745 = relay.Function([var_2742,], output)
mod['func_2745'] = func_2745
mod = relay.transform.InferType()(mod)
var_2746 = relay.var("var_2746", dtype = "float32", shape = (10, 8, 8))#candidate|2746|(10, 8, 8)|var|float32
output = func_2745(var_2746)
func_2747 = relay.Function([var_2746], output)
mutated_mod['func_2747'] = func_2747
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2835 = relay.const([[[1.744470,9.748345,-5.050656,-6.130975,-4.475746,-9.788787,1.820394],[-5.370001,3.240203,-4.884525,8.588097,2.000815,-9.366971,-7.551921],[8.117430,9.226463,-5.912511,7.600645,2.145558,-6.228745,-9.023558]],[[-2.879301,0.858567,1.671827,8.825183,-2.299634,-6.451995,7.687709],[-0.440950,-2.482239,0.651072,0.043537,-7.328460,0.804425,-8.519619],[6.485028,-3.381500,-7.426669,7.521972,-8.179144,3.067873,3.795629]],[[2.302820,9.920265,-8.414607,1.251381,2.354794,1.291610,0.823659],[9.832269,-4.199935,-2.510989,1.775644,3.278647,6.883522,2.617772],[-6.624526,-1.630726,0.467868,-4.064471,-6.905662,9.764433,-5.688049]],[[3.150016,8.777366,0.545245,-6.599629,2.803335,-8.957594,-4.027526],[-3.899952,7.604216,-3.309079,-1.804805,6.951747,8.338450,-0.048191],[9.313288,-2.990994,-4.940560,-4.799299,2.379943,-0.991611,-1.421506]],[[3.930531,-9.328424,-6.781156,0.002018,1.658987,-7.777717,-7.616026],[-3.138376,-2.924808,3.025858,2.788478,7.620321,7.864530,-0.194006],[8.826332,-5.255961,9.034045,-3.708363,-1.564823,-8.162969,-5.758430]],[[-5.957004,-4.242301,7.374606,3.361172,3.854977,2.457007,-4.740711],[-1.593691,-2.745342,5.191860,-1.128805,5.683071,-9.674290,-1.112416],[4.854355,1.547254,5.879096,7.872320,-1.420591,5.448520,0.808644]],[[-0.890369,6.717877,-4.303076,-1.094113,6.363279,-7.115787,-8.005320],[-2.084625,5.461180,4.900265,-2.026230,-6.597949,8.172584,-4.617171],[6.998767,6.153971,6.179160,-1.948043,-4.278019,2.824765,1.272935]]], dtype = "float32")#candidate|2835|(7, 3, 7)|const|float32
uop_2836 = relay.log(const_2835.astype('float32')) # shape=(7, 3, 7)
bop_2852 = relay.right_shift(uop_2836.astype('uint32'), relay.reshape(const_2835.astype('uint32'), relay.shape_of(uop_2836))) # shape=(7, 3, 7)
output = bop_2852
output2 = bop_2852
func_2859 = relay.Function([], output)
mod['func_2859'] = func_2859
mod = relay.transform.InferType()(mod)
output = func_2859()
func_2860 = relay.Function([], output)
mutated_mod['func_2860'] = func_2860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2859_call = mod.get_global_var('func_2859')
func_2860_call = mutated_mod.get_global_var('func_2860')
call_2928 = func_2859_call()
call_2929 = func_2859_call()
output = call_2928
output2 = call_2929
func_2930 = relay.Function([], output)
mod['func_2930'] = func_2930
mod = relay.transform.InferType()(mod)
output = func_2930()
func_2931 = relay.Function([], output)
mutated_mod['func_2931'] = func_2931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2859_call = mod.get_global_var('func_2859')
func_2860_call = mutated_mod.get_global_var('func_2860')
call_2964 = func_2859_call()
call_2965 = func_2859_call()
output = call_2964
output2 = call_2965
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
func_2859_call = mod.get_global_var('func_2859')
func_2860_call = mutated_mod.get_global_var('func_2860')
call_3003 = func_2859_call()
call_3004 = func_2859_call()
output = relay.Tuple([call_3003,])
output2 = relay.Tuple([call_3004,])
func_3016 = relay.Function([], output)
mod['func_3016'] = func_3016
mod = relay.transform.InferType()(mod)
mutated_mod['func_3016'] = func_3016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3016_call = mutated_mod.get_global_var('func_3016')
call_3017 = func_3016_call()
output = call_3017
func_3018 = relay.Function([], output)
mutated_mod['func_3018'] = func_3018
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3021 = relay.var("var_3021", dtype = "float64", shape = (10, 2, 16))#candidate|3021|(10, 2, 16)|var|float64
uop_3022 = relay.sigmoid(var_3021.astype('float64')) # shape=(10, 2, 16)
output = relay.Tuple([uop_3022,])
output2 = relay.Tuple([uop_3022,])
func_3026 = relay.Function([var_3021,], output)
mod['func_3026'] = func_3026
mod = relay.transform.InferType()(mod)
var_3027 = relay.var("var_3027", dtype = "float64", shape = (10, 2, 16))#candidate|3027|(10, 2, 16)|var|float64
output = func_3026(var_3027)
func_3028 = relay.Function([var_3027], output)
mutated_mod['func_3028'] = func_3028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2980_call = mod.get_global_var('func_2980')
func_2982_call = mutated_mod.get_global_var('func_2982')
call_3056 = func_2980_call()
call_3057 = func_2980_call()
output = call_3056
output2 = call_3057
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
func_2859_call = mod.get_global_var('func_2859')
func_2860_call = mutated_mod.get_global_var('func_2860')
call_3149 = func_2859_call()
call_3150 = func_2859_call()
func_2930_call = mod.get_global_var('func_2930')
func_2931_call = mutated_mod.get_global_var('func_2931')
call_3156 = func_2930_call()
call_3157 = func_2930_call()
output = relay.Tuple([call_3149,call_3156,])
output2 = relay.Tuple([call_3150,call_3157,])
func_3158 = relay.Function([], output)
mod['func_3158'] = func_3158
mod = relay.transform.InferType()(mod)
mutated_mod['func_3158'] = func_3158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3158_call = mutated_mod.get_global_var('func_3158')
call_3159 = func_3158_call()
output = call_3159
func_3160 = relay.Function([], output)
mutated_mod['func_3160'] = func_3160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3016_call = mod.get_global_var('func_3016')
func_3018_call = mutated_mod.get_global_var('func_3018')
call_3193 = relay.TupleGetItem(func_3016_call(), 0)
call_3194 = relay.TupleGetItem(func_3018_call(), 0)
func_3026_call = mod.get_global_var('func_3026')
func_3028_call = mutated_mod.get_global_var('func_3028')
var_3207 = relay.var("var_3207", dtype = "float64", shape = (320,))#candidate|3207|(320,)|var|float64
call_3206 = relay.TupleGetItem(func_3026_call(relay.reshape(var_3207.astype('float64'), [10, 2, 16])), 0)
call_3208 = relay.TupleGetItem(func_3028_call(relay.reshape(var_3207.astype('float64'), [10, 2, 16])), 0)
func_2025_call = mod.get_global_var('func_2025')
func_2028_call = mutated_mod.get_global_var('func_2028')
var_3229 = relay.var("var_3229", dtype = "float32", shape = (143,))#candidate|3229|(143,)|var|float32
call_3228 = func_2025_call(relay.reshape(var_3229.astype('float32'), [13, 1, 11]))
call_3230 = func_2025_call(relay.reshape(var_3229.astype('float32'), [13, 1, 11]))
output = relay.Tuple([call_3193,call_3206,var_3207,call_3228,var_3229,])
output2 = relay.Tuple([call_3194,call_3208,var_3207,call_3230,var_3229,])
func_3234 = relay.Function([var_3207,var_3229,], output)
mod['func_3234'] = func_3234
mod = relay.transform.InferType()(mod)
var_3235 = relay.var("var_3235", dtype = "float64", shape = (320,))#candidate|3235|(320,)|var|float64
var_3236 = relay.var("var_3236", dtype = "float32", shape = (143,))#candidate|3236|(143,)|var|float32
output = func_3234(var_3235,var_3236,)
func_3237 = relay.Function([var_3235,var_3236,], output)
mutated_mod['func_3237'] = func_3237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2859_call = mod.get_global_var('func_2859')
func_2860_call = mutated_mod.get_global_var('func_2860')
call_3268 = func_2859_call()
call_3269 = func_2859_call()
output = relay.Tuple([call_3268,])
output2 = relay.Tuple([call_3269,])
func_3274 = relay.Function([], output)
mod['func_3274'] = func_3274
mod = relay.transform.InferType()(mod)
output = func_3274()
func_3275 = relay.Function([], output)
mutated_mod['func_3275'] = func_3275
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3345 = relay.var("var_3345", dtype = "int16", shape = ())#candidate|3345|()|var|int16
var_3346 = relay.var("var_3346", dtype = "int16", shape = (3, 7, 14))#candidate|3346|(3, 7, 14)|var|int16
bop_3347 = relay.bitwise_or(var_3345.astype('int16'), var_3346.astype('int16')) # shape=(3, 7, 14)
func_2980_call = mod.get_global_var('func_2980')
func_2982_call = mutated_mod.get_global_var('func_2982')
call_3354 = func_2980_call()
call_3355 = func_2980_call()
func_3158_call = mod.get_global_var('func_3158')
func_3160_call = mutated_mod.get_global_var('func_3160')
call_3379 = relay.TupleGetItem(func_3158_call(), 0)
call_3380 = relay.TupleGetItem(func_3160_call(), 0)
uop_3382 = relay.sinh(call_3354.astype('float32')) # shape=(7, 3, 7)
uop_3384 = relay.sinh(call_3355.astype('float32')) # shape=(7, 3, 7)
output = relay.Tuple([bop_3347,call_3379,uop_3382,])
output2 = relay.Tuple([bop_3347,call_3380,uop_3384,])
func_3396 = relay.Function([var_3345,var_3346,], output)
mod['func_3396'] = func_3396
mod = relay.transform.InferType()(mod)
mutated_mod['func_3396'] = func_3396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3396_call = mutated_mod.get_global_var('func_3396')
var_3398 = relay.var("var_3398", dtype = "int16", shape = ())#candidate|3398|()|var|int16
var_3399 = relay.var("var_3399", dtype = "int16", shape = (3, 7, 14))#candidate|3399|(3, 7, 14)|var|int16
call_3397 = func_3396_call(var_3398,var_3399,)
output = call_3397
func_3400 = relay.Function([var_3398,var_3399,], output)
mutated_mod['func_3400'] = func_3400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3074_call = mod.get_global_var('func_3074')
func_3076_call = mutated_mod.get_global_var('func_3076')
call_3402 = func_3074_call()
call_3403 = func_3074_call()
func_3234_call = mod.get_global_var('func_3234')
func_3237_call = mutated_mod.get_global_var('func_3237')
var_3407 = relay.var("var_3407", dtype = "float64", shape = (320,))#candidate|3407|(320,)|var|float64
var_3408 = relay.var("var_3408", dtype = "float32", shape = (143,))#candidate|3408|(143,)|var|float32
call_3406 = relay.TupleGetItem(func_3234_call(relay.reshape(var_3407.astype('float64'), [320,]), relay.reshape(var_3408.astype('float32'), [143,]), ), 2)
call_3409 = relay.TupleGetItem(func_3237_call(relay.reshape(var_3407.astype('float64'), [320,]), relay.reshape(var_3408.astype('float32'), [143,]), ), 2)
func_2025_call = mod.get_global_var('func_2025')
func_2028_call = mutated_mod.get_global_var('func_2028')
call_3416 = func_2025_call(relay.reshape(var_3408.astype('float32'), [13, 1, 11]))
call_3417 = func_2025_call(relay.reshape(var_3408.astype('float32'), [13, 1, 11]))
func_1461_call = mod.get_global_var('func_1461')
func_1465_call = mutated_mod.get_global_var('func_1465')
const_3423 = relay.const([[0.025439,-6.228480,2.899257,-1.784437,-0.655120,-0.412010,9.351787,4.236511,-6.987849,-6.320299,6.052034,0.868603,-4.869157,-7.029238,-5.224648,4.391595,-8.000942,-9.723440],[2.104280,7.912820,4.343664,-8.271190,-6.948149,-3.429318,1.498773,-4.273778,2.076835,6.749495,-8.329078,-2.784371,5.437359,0.579366,-3.692832,9.990061,-8.015484,7.423648],[4.784740,-7.701998,6.867937,-8.448748,0.542244,2.204632,4.911448,3.612135,-4.950399,-9.460229,1.477620,3.093568,6.363345,9.701513,2.217898,-8.150824,-4.879157,-2.521028],[0.088248,-1.014937,-4.359933,6.661141,2.740761,5.766853,5.154388,0.995817,6.144074,-6.958769,-9.507864,-9.412432,-8.553038,-0.052102,-0.830706,-2.873994,8.537285,-5.607280],[-5.950004,9.769618,-2.225380,8.165554,-7.071935,0.593764,3.183186,8.536063,3.116075,9.853998,-0.449102,3.396801,-0.943790,-6.370609,-2.798578,4.972494,4.325753,-1.302620],[-5.162499,6.336697,5.923937,-7.757806,-8.357971,-6.679488,-5.822806,9.038366,5.896331,7.006572,-1.666812,9.120845,-6.520505,4.084128,-3.438003,-7.033372,7.353422,2.313978],[-1.166537,4.669801,7.780611,-2.911960,9.687407,-4.098017,-4.904632,-7.590941,-0.015831,-1.132892,8.212232,-8.912822,6.788108,-9.541504,-2.410765,0.922887,3.799762,7.554530],[-7.669017,-5.648040,1.654228,-9.882659,-5.490288,-8.003148,5.463451,-5.676336,-8.264418,-1.671317,9.156951,-7.599243,-6.146081,-2.858828,-9.795036,1.704530,9.337407,-9.483837],[-7.824920,5.445626,1.539649,7.878514,-6.633759,2.254553,-8.925984,-8.436112,-7.849298,9.135680,8.068829,0.240821,1.814509,-0.201140,-1.207208,2.734525,-5.547965,-0.214531],[-6.810326,-6.613974,6.328839,4.165676,8.083466,8.223562,-9.515894,-3.146661,-1.735230,7.193009,-3.465234,-4.683197,-1.484525,-7.736089,-7.937149,2.003474,-7.367170,4.814024],[9.983278,-2.931053,9.895622,1.955101,-6.788185,9.038540,7.132933,9.567895,-5.031982,-5.466638,8.256813,9.760782,9.572233,5.737638,-7.358096,8.109703,0.820032,-0.127361],[6.487011,3.657091,-1.195416,-6.671151,3.013790,7.784145,-9.652930,1.005783,-6.538341,1.417616,0.828143,-9.278328,-0.061523,7.794759,6.118073,-4.223324,3.052801,-0.859382]], dtype = "float64")#candidate|3423|(12, 18)|const|float64
var_3424 = relay.var("var_3424", dtype = "uint32", shape = ())#candidate|3424|()|var|uint32
call_3422 = relay.TupleGetItem(func_1461_call(relay.reshape(const_3423.astype('float64'), [6, 6, 6]), relay.reshape(var_3424.astype('uint32'), []), ), 0)
call_3425 = relay.TupleGetItem(func_1465_call(relay.reshape(const_3423.astype('float64'), [6, 6, 6]), relay.reshape(var_3424.astype('uint32'), []), ), 0)
func_1737_call = mod.get_global_var('func_1737')
func_1741_call = mutated_mod.get_global_var('func_1741')
const_3427 = relay.const([-9.642712,9.167167,4.638521,6.598994,-7.666424,7.483193,4.076902,-2.654006,2.006864,-8.861408,-6.069885,-4.772962,-3.402446,7.589458,-0.837675,-7.553929,4.223870,-1.371948,6.428016,-2.257500,-1.090505,3.882296,6.857125,2.889977,-3.849181,-2.935711,6.276642,-1.792571,9.533983,8.757848,-4.193501,-6.715129,-7.379472,-6.470133,-2.426604,1.679758,-2.560540,-9.852877,-1.556002,6.971809,4.375869,4.752462,-7.531833,2.951051,1.193550,2.472446,-4.966801,-1.418326,-2.816384,-8.549904,0.386490,8.398393,-4.290848,-5.810105,1.875897,6.672142,9.051993,-3.328405,-8.128618,4.822859,-7.127520,3.417641,-8.213996,0.507964,-3.019076,-3.893142,3.741252,-2.243758,2.267318,0.469718,-2.893120,-1.361326,4.875020,1.566377,-6.448121,-4.448500,1.808754,6.389551,3.042355,-2.719722,-1.207386,5.369631,-4.119082,8.811209,-0.784468,1.992880,3.474220,6.479382,-9.724197,6.980038,8.099423,9.852156,0.041254,8.007194,-3.004682,3.531400,-3.025645,-8.641716,-2.665186,-1.644918,-2.997214,5.018055,4.596115,7.228491,7.908672,-1.169309,-1.115831,8.115360,-0.141494,-4.505918,-4.174830,1.739661,-6.186557,4.827511,8.236182,-6.722703,0.661179,-2.412774,-9.955628,-2.086995,-0.932495,-0.938278,0.843695,-9.396329,-6.892732,-7.360886,-6.113542,6.930116,4.353487,9.107594,7.627624,1.532392,0.986536,4.464871,0.977652,3.443639,8.481657,-9.231664,5.446265,-9.976940,9.489441,-3.998500,4.992444,-0.515381,8.158144,8.111351,4.514231,9.515709,-6.377250,-2.382562,4.434769,9.452369,-1.535793,0.594032,9.921998,9.014023,-9.372447,-2.381052,-0.455746,-9.712880,7.078713,-4.015594,-4.811351,2.273701,-9.980410,-1.461239,-0.962259,-5.382251,9.395080,-6.844330,-8.690223,2.494514,-8.699692,-5.493137,2.526365,-0.431183,-7.257492,7.674362,-4.243909,-4.329162,5.669405,-7.379453,-7.425609,-1.102337,-6.533236,-2.221181,-3.993312,7.591535,-9.222474,1.052115,9.832595,-8.573835,-3.234897,-0.586827,-0.967203,-3.028315,-9.495047,7.020911,9.214155,-1.505212,3.155142,-8.615742,3.854119,-1.050483,1.777157,6.731885,4.893116,0.104040,0.159724,-6.696509,-0.122064,2.377854,-7.372415,9.208878,-7.346356,4.404109,4.091436,-4.580505,-8.071916,-3.020557,-1.921021,-1.622826,4.348989,-4.853006,9.782987,-0.573133,4.709798,-5.448999,2.348693,1.596828,-9.754884,7.463144,8.014582,-2.569466,-0.640185,6.547593,-9.322677,-4.965944,5.373999,-7.591744,3.083805,-4.461930,5.430674,-1.051186,6.926101,-5.438831,4.988892,2.672043,2.744859,-1.622080,-1.008818,1.341292,9.874142,-0.893429,-3.692281,6.404088,8.357291,-8.749658,2.644215,5.476131,-8.210805,-4.343494,7.875053,-2.256494,1.964459,-8.951179,9.013795,-3.430246,5.269883,9.677574,3.631061,-2.252699,9.851230,6.865754,2.061630,2.548451,4.315959,7.822662,3.897897,8.545140,-7.098465,-0.995267,4.366860,-3.404023,9.384426,-5.545722,3.115928,3.317621,4.327427,0.801308,-0.073989,2.618603,-5.934307,-1.726801,-3.381076,-7.289606,-0.199561,-5.082589,8.017660,-0.632074,1.326120,2.785325,3.387843,6.478859,-2.078702,-1.113083,9.056199,-2.451825,-2.863198,0.076460,-8.506483,-9.368801,-0.685170,2.435322,2.339448,-0.229182,-7.872682,1.348526,-3.551073,6.869697,6.634648,0.584689,7.742309,-6.267866,9.495989,-7.786326,4.441804,-7.115514,-6.471375,2.170305,5.146051,-0.297915,-9.889227,-9.326753,-5.699355,4.157307,8.472538,-1.284293,-4.376860,-1.659771,-4.265070,4.035869,0.406217,1.376950,8.195102,-6.458161,-9.986789,0.757617,-5.957188,3.347351,0.977981,4.397442,-0.401198,1.659225,-0.733396,-9.656044,-7.785273,7.475313,4.735688,7.648529,6.482327,1.385225,-7.252297,-9.485868,-4.471882,3.359750,-4.415761,-1.468533,-0.095030,4.888022,-6.923841,1.606970,-7.921395,-2.086784,6.646005,-1.985836,4.511621,-7.579368,-1.818898,1.701305,9.135102,-0.869233,8.353533,-6.164871,-1.885595,-9.380185,0.165470,-4.601234,-6.602329,6.538816,-8.507591,5.479422,8.431108,-0.528906,-8.943244,1.647198,-3.700961,-4.757579,-2.431716,-4.537432,-9.016971,9.472096,-5.849631,6.863968,1.949786,1.165095,9.469112,9.368618,-1.181355,-6.854921,0.642992,-6.846178,-7.936713,8.299486,0.750797,1.071842,0.544181,8.762741,-2.797074,-7.147888,8.050886,-7.808743,-0.702616,-0.607785,9.621307,-5.858267,-2.355747,-7.601963,0.842247,1.449189,8.932142,-5.408714,-1.477734,9.521417,3.801917,-9.524800,2.065386,9.276553,-1.679101,-1.112652,-8.120355,5.258161,-8.704180,8.716647,0.054223,-4.753082,-2.496516,5.059476,2.226306,5.734816,6.858311,9.856101,-3.882444,-4.216600,-3.077697,-6.010765,6.048293,0.687631,-1.124053,8.516781,-5.943715,-7.614041,6.162800,8.898081,-4.566234,8.071260,-0.969519,-0.130857,2.370453,4.632689,-6.331816,-0.967759,9.907357,5.934154,6.240009,-7.723746,-2.764549,-8.009107,-6.879533,-2.850218,-5.045193,-7.179789,6.311211,-1.134297,-7.750963,-4.913090,2.854435,-4.147713,3.526071,-5.378272,4.571047,-6.089830,-8.504273,2.612982,-3.849801,7.389787,3.190553,8.843487,5.294742,4.222241,0.991926,-5.532488,-3.813915,-8.628728,-7.434490,-6.751313,9.059878,1.086327,4.599188,-2.518990,8.232675,1.107199,-0.064589,8.428709,-5.481150,8.608666,-4.303141,-2.290557,-3.405140,-7.398121,-5.012247,-6.548353,2.909377,0.898753,-5.085168,-6.044658,6.038485,-6.474652,-8.885259,2.130270,-7.269398,0.003738,-4.504314,-4.624198,-4.734092,8.183474,0.376094,-2.743538,-2.413050,-2.307877,6.995026,-1.438681,-1.395417,-7.118162,-5.300540,2.215383,-2.736953,7.075421,-2.634551,-7.872194,4.035914,8.467119,8.286360,6.123134,5.934245,4.914443,0.047254,-6.636022,-6.014877,-9.783840,-3.429628,-7.136198,-5.914741,-4.436741,5.017731,0.089094,-5.392780,6.485429,-1.316284,6.027332,-7.185999,3.291762,-0.286876,9.261164,-4.915064,7.360433,1.928357,-5.674706,-8.730767,5.234608,9.602869,-1.361323,0.111474,7.073070,-1.846999,-8.024181,6.605007,-6.126385,3.487952,2.638663,-3.383661,-6.404000,-4.327515,4.489718,1.516682,-6.407636,-7.883495,6.484515,-0.572145,5.357758,8.987281,-4.589783,3.610899,2.197829,-9.055918,5.130903,4.470696,2.818246,-3.766666,-4.179581,6.737005,-5.794947,5.939639,0.836032,-0.743870,7.876291,-8.747582,9.840999,-7.066324,-8.412327,8.779170,1.040434,-0.033415,-2.843363,-7.965238,-8.748236,8.543385,6.869147,-1.516154,-9.310202,2.523579,7.417105,0.645941,-7.372241,5.519500,4.207448,-5.976620,7.195837,0.421650,4.614340,1.865274,1.563408,-4.517233,7.729018,5.167909,6.599267,3.929947,4.490162,6.431323,3.168028,-0.923841,0.624261,0.451564,5.295247,-5.421576,-8.137506,0.478678,-7.693400,-5.688161,-9.993637,-6.041486,9.693800,-1.627285,-0.968246,-6.034913,-8.789719,-2.618663,7.194198,0.350220,-5.911268,4.767314,5.506760,-3.084621,-5.705052,0.145342,0.592862,-3.797703,-5.745242,1.907779,0.555035,-5.401388,-5.119254,4.173286,-0.752297,2.586550,1.084632,-9.927240,0.089383,-5.151790,2.256769,-1.203840,7.545245,1.797791,-2.201113,9.669774,-1.418540,1.308287,-5.893603,-2.601519,2.028315,-2.128981,-1.177905,7.067033,4.620973,5.287258,-8.758352,9.908286,8.852861,6.448839,1.675667,7.623499,-6.867850,8.388660,9.590088,8.422365,1.164434,0.965565,-2.462599,0.296039,6.681578,2.915413,-9.792985,6.801463,2.218964,8.360510,1.120202,7.030840,-6.862193,3.226889,-4.761792,-2.465183,-8.153766,-0.712158,4.173961,-3.094760,-1.281634,-3.479947,0.513363,-1.552957,-4.365693,2.730985,-8.113661,5.057669,5.900108,8.137713,8.091059,5.201645,5.006786,8.919763,1.661516,7.045093,3.386238,5.642623,-3.703388,1.033287,9.808546], dtype = "float64")#candidate|3427|(756,)|const|float64
call_3426 = relay.TupleGetItem(func_1737_call(relay.reshape(const_3427.astype('float64'), [9, 7, 12]), relay.reshape(const_3427.astype('float64'), [9, 7, 12]), relay.reshape(const_3427.astype('float64'), [9, 7, 12]), ), 0)
call_3428 = relay.TupleGetItem(func_1741_call(relay.reshape(const_3427.astype('float64'), [9, 7, 12]), relay.reshape(const_3427.astype('float64'), [9, 7, 12]), relay.reshape(const_3427.astype('float64'), [9, 7, 12]), ), 0)
bop_3430 = relay.right_shift(call_3416.astype('int8'), relay.reshape(var_3408.astype('int8'), relay.shape_of(call_3416))) # shape=(13, 1, 11)
bop_3433 = relay.right_shift(call_3417.astype('int8'), relay.reshape(var_3408.astype('int8'), relay.shape_of(call_3417))) # shape=(13, 1, 11)
func_2859_call = mod.get_global_var('func_2859')
func_2860_call = mutated_mod.get_global_var('func_2860')
call_3437 = func_2859_call()
call_3438 = func_2859_call()
output = relay.Tuple([call_3402,call_3406,var_3407,call_3422,const_3423,var_3424,call_3426,const_3427,bop_3430,call_3437,])
output2 = relay.Tuple([call_3403,call_3409,var_3407,call_3425,const_3423,var_3424,call_3428,const_3427,bop_3433,call_3438,])
func_3440 = relay.Function([var_3407,var_3408,var_3424,], output)
mod['func_3440'] = func_3440
mod = relay.transform.InferType()(mod)
var_3441 = relay.var("var_3441", dtype = "float64", shape = (320,))#candidate|3441|(320,)|var|float64
var_3442 = relay.var("var_3442", dtype = "float32", shape = (143,))#candidate|3442|(143,)|var|float32
var_3443 = relay.var("var_3443", dtype = "uint32", shape = ())#candidate|3443|()|var|uint32
output = func_3440(var_3441,var_3442,var_3443,)
func_3444 = relay.Function([var_3441,var_3442,var_3443,], output)
mutated_mod['func_3444'] = func_3444
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2930_call = mod.get_global_var('func_2930')
func_2931_call = mutated_mod.get_global_var('func_2931')
call_3462 = func_2930_call()
call_3463 = func_2930_call()
const_3482 = relay.const([[[-3,4,2,3,-8,3,4],[6,3,-10,-9,-5,10,-2],[-7,-4,7,-2,-10,9,3]],[[-7,-6,-10,10,-5,-7,-7],[2,9,10,-10,3,-7,6],[-1,8,8,1,-2,10,-2]],[[-8,3,-10,9,-10,-6,2],[6,-9,-9,-4,-10,-6,8],[2,2,10,-1,-2,8,-1]],[[2,8,-3,4,-4,10,-3],[-8,4,-2,-1,-4,1,-5],[5,-5,-9,-7,-2,4,-7]],[[-1,3,-3,1,-5,-6,-7],[4,-9,-7,-8,-7,-1,-3],[-4,1,5,5,3,1,-10]],[[-5,-7,-8,8,9,4,-10],[-7,-1,-5,6,-8,-8,-1],[-7,10,-8,2,1,3,-5]],[[-10,-1,-8,-7,7,-5,-8],[-4,-3,-10,4,8,-5,-8],[-3,-5,-8,1,1,2,-3]]], dtype = "uint32")#candidate|3482|(7, 3, 7)|const|uint32
bop_3483 = relay.not_equal(call_3462.astype('bool'), relay.reshape(const_3482.astype('bool'), relay.shape_of(call_3462))) # shape=(7, 3, 7)
bop_3486 = relay.not_equal(call_3463.astype('bool'), relay.reshape(const_3482.astype('bool'), relay.shape_of(call_3463))) # shape=(7, 3, 7)
output = relay.Tuple([bop_3483,])
output2 = relay.Tuple([bop_3486,])
func_3491 = relay.Function([], output)
mod['func_3491'] = func_3491
mod = relay.transform.InferType()(mod)
mutated_mod['func_3491'] = func_3491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3491_call = mutated_mod.get_global_var('func_3491')
call_3492 = func_3491_call()
output = call_3492
func_3493 = relay.Function([], output)
mutated_mod['func_3493'] = func_3493
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3556 = relay.var("var_3556", dtype = "uint8", shape = (8, 2, 5))#candidate|3556|(8, 2, 5)|var|uint8
const_3557 = relay.const([[[2,-7,8,-4,-3],[9,5,8,-8,10]],[[8,8,6,4,-3],[10,-4,2,8,-3]],[[6,4,-1,-7,5],[-8,-3,-2,-4,9]],[[-1,-3,-9,7,10],[-10,-3,8,-9,10]],[[2,-6,-6,-6,-7],[6,-7,2,-3,-3]],[[10,-9,-10,-4,10],[4,4,9,-10,-10]],[[9,6,-6,-1,-9],[4,-10,2,-8,10]],[[2,1,3,8,4],[-2,-6,10,7,3]]], dtype = "uint8")#candidate|3557|(8, 2, 5)|const|uint8
bop_3558 = relay.add(var_3556.astype('uint8'), relay.reshape(const_3557.astype('uint8'), relay.shape_of(var_3556))) # shape=(8, 2, 5)
output = relay.Tuple([bop_3558,])
output2 = relay.Tuple([bop_3558,])
func_3562 = relay.Function([var_3556,], output)
mod['func_3562'] = func_3562
mod = relay.transform.InferType()(mod)
var_3563 = relay.var("var_3563", dtype = "uint8", shape = (8, 2, 5))#candidate|3563|(8, 2, 5)|var|uint8
output = func_3562(var_3563)
func_3564 = relay.Function([var_3563], output)
mutated_mod['func_3564'] = func_3564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2930_call = mod.get_global_var('func_2930')
func_2931_call = mutated_mod.get_global_var('func_2931')
call_3581 = func_2930_call()
call_3582 = func_2930_call()
output = relay.Tuple([call_3581,])
output2 = relay.Tuple([call_3582,])
func_3615 = relay.Function([], output)
mod['func_3615'] = func_3615
mod = relay.transform.InferType()(mod)
output = func_3615()
func_3616 = relay.Function([], output)
mutated_mod['func_3616'] = func_3616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3158_call = mod.get_global_var('func_3158')
func_3160_call = mutated_mod.get_global_var('func_3160')
call_3647 = relay.TupleGetItem(func_3158_call(), 0)
call_3648 = relay.TupleGetItem(func_3160_call(), 0)
func_2025_call = mod.get_global_var('func_2025')
func_2028_call = mutated_mod.get_global_var('func_2028')
const_3664 = relay.const([6.564928,-0.107956,-7.822960,7.842122,-4.744357,-6.434663,2.468074,-4.366780,6.942735,-5.528421,9.969426,-0.823240,5.170367,-0.137805,-6.101292,7.917914,4.993286,6.813424,-8.397065,-3.107075,-5.893530,1.336184,8.175975,-3.223948,0.001812,-5.927485,-3.226583,5.748751,0.789457,-7.354709,-9.881043,-5.945664,-0.370844,2.793767,-8.761922,2.443928,-6.048844,-2.196325,-6.131219,-7.583430,-5.467046,-5.095830,8.336123,-5.462696,7.691055,2.129238,-1.429096,-1.634310,8.498294,7.145027,0.485117,-7.013241,-8.835415,8.596270,-9.279651,-5.831464,-6.160071,2.053424,-2.473728,9.073629,6.281095,8.814835,-7.694083,-4.235867,5.314844,2.612970,-4.737639,-0.334453,-8.071855,8.629353,-4.897606,8.248945,-0.393399,-4.661756,2.917919,-1.418849,-3.351454,-5.017251,0.498702,2.049790,1.520184,7.314617,-0.432586,-0.658027,-7.592994,6.826342,2.006291,1.667213,-5.397672,5.128345,3.464283,-2.104333,2.105341,-0.020138,7.820667,-1.136458,-8.505795,-0.427100,0.386508,-2.661596,-5.920753,-2.698862,-0.842249,5.769406,-2.885653,-4.641531,-9.728237,1.641774,-5.380884,0.379662,7.579355,-1.282843,1.878229,6.760163,0.514720,-7.238621,9.519221,6.114477,4.434670,-5.887278,0.130813,4.338647,1.635042,-7.225659,7.128768,0.900706,3.122860,-4.057706,-2.000158,7.701008,0.112590,6.156890,5.987381,7.192448,6.986312,-9.223315,-4.220601,9.767397,-6.174635,6.447483,9.901143,8.660972,-5.188854], dtype = "float32")#candidate|3664|(143,)|const|float32
call_3663 = func_2025_call(relay.reshape(const_3664.astype('float32'), [13, 1, 11]))
call_3665 = func_2025_call(relay.reshape(const_3664.astype('float32'), [13, 1, 11]))
uop_3683 = relay.tan(call_3663.astype('float64')) # shape=(13, 1, 11)
uop_3685 = relay.tan(call_3665.astype('float64')) # shape=(13, 1, 11)
uop_3694 = relay.log(uop_3683.astype('float64')) # shape=(13, 1, 11)
uop_3696 = relay.log(uop_3685.astype('float64')) # shape=(13, 1, 11)
output = relay.Tuple([call_3647,const_3664,uop_3694,])
output2 = relay.Tuple([call_3648,const_3664,uop_3696,])
func_3709 = relay.Function([], output)
mod['func_3709'] = func_3709
mod = relay.transform.InferType()(mod)
mutated_mod['func_3709'] = func_3709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3709_call = mutated_mod.get_global_var('func_3709')
call_3710 = func_3709_call()
output = call_3710
func_3711 = relay.Function([], output)
mutated_mod['func_3711'] = func_3711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2980_call = mod.get_global_var('func_2980')
func_2982_call = mutated_mod.get_global_var('func_2982')
call_3729 = func_2980_call()
call_3730 = func_2980_call()
func_480_call = mod.get_global_var('func_480')
func_484_call = mutated_mod.get_global_var('func_484')
var_3736 = relay.var("var_3736", dtype = "uint32", shape = ())#candidate|3736|()|var|uint32
var_3737 = relay.var("var_3737", dtype = "int32", shape = (5, 6))#candidate|3737|(5, 6)|var|int32
call_3735 = relay.TupleGetItem(func_480_call(relay.reshape(var_3736.astype('uint32'), []), relay.reshape(var_3737.astype('int32'), [30,]), ), 0)
call_3738 = relay.TupleGetItem(func_484_call(relay.reshape(var_3736.astype('uint32'), []), relay.reshape(var_3737.astype('int32'), [30,]), ), 0)
func_426_call = mod.get_global_var('func_426')
func_430_call = mutated_mod.get_global_var('func_430')
var_3749 = relay.var("var_3749", dtype = "float64", shape = (150, 2))#candidate|3749|(150, 2)|var|float64
call_3748 = relay.TupleGetItem(func_426_call(relay.reshape(var_3737.astype('int32'), [1, 15, 2]), relay.reshape(var_3749.astype('float64'), [10, 15, 2]), ), 1)
call_3750 = relay.TupleGetItem(func_430_call(relay.reshape(var_3737.astype('int32'), [1, 15, 2]), relay.reshape(var_3749.astype('float64'), [10, 15, 2]), ), 1)
bop_3755 = relay.maximum(call_3748.astype('float64'), relay.reshape(var_3749.astype('float64'), relay.shape_of(call_3748))) # shape=(10, 15, 2)
bop_3758 = relay.maximum(call_3750.astype('float64'), relay.reshape(var_3749.astype('float64'), relay.shape_of(call_3750))) # shape=(10, 15, 2)
func_1461_call = mod.get_global_var('func_1461')
func_1465_call = mutated_mod.get_global_var('func_1465')
const_3761 = relay.const([-0.929172,-6.242973,1.944419,-4.686051,0.479463,4.082491,-1.694633,7.720350,3.512988,-4.239846,-6.112091,1.082672,5.493096,2.053673,4.481897,-2.324066,-1.057695,-9.802305,8.494596,9.970479,9.081079,1.650607,7.282876,3.161730,-4.084904,-8.374410,5.871021,-6.819949,4.011234,3.167001,-3.917343,-2.985370,-0.473332,7.490197,7.672208,-2.056904,5.496470,2.042185,-0.858508,4.894966,-2.763640,2.941773,3.606788,-2.927704,3.628065,6.041848,0.598438,-3.692869,-2.397991,7.882531,9.945437,-8.612591,3.423910,3.896714,1.521770,-9.503380,-8.595675,1.418366,-0.960874,-5.199408,2.441421,8.320053,7.347026,-7.612665,6.926367,-1.909281,3.848032,-2.591150,-5.369955,-0.358460,-4.470774,6.950514,-3.808526,7.900059,-7.912511,-2.877689,2.534328,-6.819458,-9.357168,9.251066,-3.608845,-2.475008,-7.295981,-0.404584,-9.828410,-3.192594,8.824158,-2.981499,-9.790289,-6.272963,4.434759,-1.620964,0.265813,-2.403906,7.311949,5.846647,8.282670,5.759312,-8.101324,-2.326492,-8.960689,-3.416041,-7.628503,1.260241,-3.212031,5.776111,4.512874,-6.625293,-3.704565,-4.170933,-7.495997,5.163003,8.471561,-5.167989,-7.044643,-6.686158,7.198714,-0.051274,2.052756,3.075466,-6.721439,-2.618952,-3.577167,-3.563834,2.017714,6.302309,-6.665254,2.675697,2.000003,-5.728275,-8.068322,4.169016,6.143041,1.200174,9.787714,-8.180272,7.714816,6.945964,8.272442,-3.647309,-8.847460,8.907912,-3.867723,-8.534673,-2.214541,2.812258,-5.632814,-0.105296,-0.348992,-3.736533,-5.450435,5.610906,8.280259,-0.425008,-9.532795,2.751109,-3.553737,-3.447459,9.361333,-1.671209,0.108889,-8.551579,-3.595367,6.710491,-0.529855,8.241404,-9.807015,-1.071183,7.703200,-0.320286,2.567301,0.245546,-3.113519,-5.957337,-0.236876,7.839020,-3.038099,4.188436,0.422831,-2.273187,0.290541,-7.363301,-5.405425,2.043172,5.202389,-7.366854,-8.208729,-1.454149,1.200540,-2.932950,-7.580847,8.704920,-3.025097,8.776755,9.559652,6.408896,3.596465,-1.041917,7.943316,-9.498626,2.847129,8.898637,-0.895740,6.530483,5.068983,0.205854,9.826857,-2.744691,-9.547189,2.965738,2.674929,-9.230303,8.884008,0.870995,-4.961246,6.219689], dtype = "float64")#candidate|3761|(216,)|const|float64
call_3760 = relay.TupleGetItem(func_1461_call(relay.reshape(const_3761.astype('float64'), [6, 6, 6]), relay.reshape(var_3736.astype('uint32'), []), ), 3)
call_3762 = relay.TupleGetItem(func_1465_call(relay.reshape(const_3761.astype('float64'), [6, 6, 6]), relay.reshape(var_3736.astype('uint32'), []), ), 3)
func_2601_call = mod.get_global_var('func_2601')
func_2603_call = mutated_mod.get_global_var('func_2603')
const_3764 = relay.const([-3.865976,-0.244975,-7.111970,-3.329302,-6.944710,2.655367,9.162675,-5.959900,-3.032099,4.705124,1.978789,8.547356,7.569768,8.704261,5.044955,-4.709193,-7.786551,-3.969806,-5.012569,1.025563,6.454389,-1.471494,9.720594,9.854858,2.555051,-2.463445,1.550381,1.191025,8.975995,0.765890,-2.266910,-3.728593,-0.382126,2.903400,0.124157,-5.942590,4.430888,2.204647,3.225813,-0.051231,2.783421,6.656368,-4.874992,-9.108887,3.104291,0.960278,6.186030,1.553247], dtype = "float32")#candidate|3764|(48,)|const|float32
call_3763 = relay.TupleGetItem(func_2601_call(relay.reshape(const_3764.astype('float32'), [4, 4, 3])), 4)
call_3765 = relay.TupleGetItem(func_2603_call(relay.reshape(const_3764.astype('float32'), [4, 4, 3])), 4)
func_3026_call = mod.get_global_var('func_3026')
func_3028_call = mutated_mod.get_global_var('func_3028')
var_3773 = relay.var("var_3773", dtype = "float64", shape = (320,))#candidate|3773|(320,)|var|float64
call_3772 = relay.TupleGetItem(func_3026_call(relay.reshape(var_3773.astype('float64'), [10, 2, 16])), 0)
call_3774 = relay.TupleGetItem(func_3028_call(relay.reshape(var_3773.astype('float64'), [10, 2, 16])), 0)
uop_3793 = relay.sqrt(bop_3755.astype('float32')) # shape=(10, 15, 2)
uop_3795 = relay.sqrt(bop_3758.astype('float32')) # shape=(10, 15, 2)
func_3274_call = mod.get_global_var('func_3274')
func_3275_call = mutated_mod.get_global_var('func_3275')
call_3802 = relay.TupleGetItem(func_3274_call(), 0)
call_3803 = relay.TupleGetItem(func_3275_call(), 0)
uop_3811 = relay.atan(uop_3793.astype('float32')) # shape=(10, 15, 2)
uop_3813 = relay.atan(uop_3795.astype('float32')) # shape=(10, 15, 2)
output = relay.Tuple([call_3729,call_3735,var_3736,var_3737,call_3760,const_3761,call_3763,const_3764,call_3772,var_3773,call_3802,uop_3811,])
output2 = relay.Tuple([call_3730,call_3738,var_3736,var_3737,call_3762,const_3761,call_3765,const_3764,call_3774,var_3773,call_3803,uop_3813,])
func_3820 = relay.Function([var_3736,var_3737,var_3749,var_3773,], output)
mod['func_3820'] = func_3820
mod = relay.transform.InferType()(mod)
mutated_mod['func_3820'] = func_3820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3820_call = mutated_mod.get_global_var('func_3820')
var_3822 = relay.var("var_3822", dtype = "uint32", shape = ())#candidate|3822|()|var|uint32
var_3823 = relay.var("var_3823", dtype = "int32", shape = (5, 6))#candidate|3823|(5, 6)|var|int32
var_3824 = relay.var("var_3824", dtype = "float64", shape = (150, 2))#candidate|3824|(150, 2)|var|float64
var_3825 = relay.var("var_3825", dtype = "float64", shape = (320,))#candidate|3825|(320,)|var|float64
call_3821 = func_3820_call(var_3822,var_3823,var_3824,var_3825,)
output = call_3821
func_3826 = relay.Function([var_3822,var_3823,var_3824,var_3825,], output)
mutated_mod['func_3826'] = func_3826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3615_call = mod.get_global_var('func_3615')
func_3616_call = mutated_mod.get_global_var('func_3616')
call_3842 = relay.TupleGetItem(func_3615_call(), 0)
call_3843 = relay.TupleGetItem(func_3616_call(), 0)
func_819_call = mod.get_global_var('func_819')
func_821_call = mutated_mod.get_global_var('func_821')
var_3849 = relay.var("var_3849", dtype = "float64", shape = (1456,))#candidate|3849|(1456,)|var|float64
call_3848 = func_819_call(relay.reshape(var_3849.astype('float64'), [14, 8, 13]))
call_3850 = func_819_call(relay.reshape(var_3849.astype('float64'), [14, 8, 13]))
output = relay.Tuple([call_3842,call_3848,var_3849,])
output2 = relay.Tuple([call_3843,call_3850,var_3849,])
func_3852 = relay.Function([var_3849,], output)
mod['func_3852'] = func_3852
mod = relay.transform.InferType()(mod)
mutated_mod['func_3852'] = func_3852
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3853 = relay.var("var_3853", dtype = "float64", shape = (1456,))#candidate|3853|(1456,)|var|float64
func_3852_call = mutated_mod.get_global_var('func_3852')
call_3854 = func_3852_call(var_3853)
output = call_3854
func_3855 = relay.Function([var_3853], output)
mutated_mod['func_3855'] = func_3855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2859_call = mod.get_global_var('func_2859')
func_2860_call = mutated_mod.get_global_var('func_2860')
call_3870 = func_2859_call()
call_3871 = func_2859_call()
output = call_3870
output2 = call_3871
func_3876 = relay.Function([], output)
mod['func_3876'] = func_3876
mod = relay.transform.InferType()(mod)
output = func_3876()
func_3877 = relay.Function([], output)
mutated_mod['func_3877'] = func_3877
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3709_call = mod.get_global_var('func_3709')
func_3711_call = mutated_mod.get_global_var('func_3711')
call_3937 = relay.TupleGetItem(func_3709_call(), 2)
call_3938 = relay.TupleGetItem(func_3711_call(), 2)
func_3709_call = mod.get_global_var('func_3709')
func_3711_call = mutated_mod.get_global_var('func_3711')
call_3943 = relay.TupleGetItem(func_3709_call(), 2)
call_3944 = relay.TupleGetItem(func_3711_call(), 2)
output = relay.Tuple([call_3937,call_3943,])
output2 = relay.Tuple([call_3938,call_3944,])
func_3945 = relay.Function([], output)
mod['func_3945'] = func_3945
mod = relay.transform.InferType()(mod)
mutated_mod['func_3945'] = func_3945
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3945_call = mutated_mod.get_global_var('func_3945')
call_3946 = func_3945_call()
output = call_3946
func_3947 = relay.Function([], output)
mutated_mod['func_3947'] = func_3947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3274_call = mod.get_global_var('func_3274')
func_3275_call = mutated_mod.get_global_var('func_3275')
call_3948 = relay.TupleGetItem(func_3274_call(), 0)
call_3949 = relay.TupleGetItem(func_3275_call(), 0)
output = call_3948
output2 = call_3949
func_3952 = relay.Function([], output)
mod['func_3952'] = func_3952
mod = relay.transform.InferType()(mod)
mutated_mod['func_3952'] = func_3952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3952_call = mutated_mod.get_global_var('func_3952')
call_3953 = func_3952_call()
output = call_3953
func_3954 = relay.Function([], output)
mutated_mod['func_3954'] = func_3954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3158_call = mod.get_global_var('func_3158')
func_3160_call = mutated_mod.get_global_var('func_3160')
call_3974 = relay.TupleGetItem(func_3158_call(), 1)
call_3975 = relay.TupleGetItem(func_3160_call(), 1)
const_3983 = relay.const([[[2,-4,1,-6,-7,-1,-7],[10,3,-10,-3,7,-3,10],[-3,-9,8,-1,9,7,-6]],[[-6,-1,2,4,-2,-8,-6],[5,3,9,-2,3,8,-3],[-7,5,1,-2,10,6,3]],[[-9,7,3,2,1,-8,7],[6,3,8,-7,-4,3,-2],[-5,3,4,-10,1,8,5]],[[-6,-4,-2,-6,-6,1,-9],[-5,-5,8,6,9,8,5],[-2,1,-5,-8,3,1,-6]],[[-1,-9,10,9,-2,-9,-9],[1,-10,-8,-10,-6,-2,-4],[-8,5,5,-8,-8,2,-9]],[[4,-7,-6,9,10,7,-8],[4,-1,-2,2,10,4,-6],[-1,7,-5,-10,5,-4,-9]],[[-10,-7,-10,-7,-5,-2,10],[7,10,10,-5,6,-5,7],[4,10,4,8,-8,-6,3]]], dtype = "uint32")#candidate|3983|(7, 3, 7)|const|uint32
bop_3984 = relay.subtract(call_3974.astype('uint8'), relay.reshape(const_3983.astype('uint8'), relay.shape_of(call_3974))) # shape=(7, 3, 7)
bop_3987 = relay.subtract(call_3975.astype('uint8'), relay.reshape(const_3983.astype('uint8'), relay.shape_of(call_3975))) # shape=(7, 3, 7)
func_3615_call = mod.get_global_var('func_3615')
func_3616_call = mutated_mod.get_global_var('func_3616')
call_3990 = relay.TupleGetItem(func_3615_call(), 0)
call_3991 = relay.TupleGetItem(func_3616_call(), 0)
output = relay.Tuple([bop_3984,call_3990,])
output2 = relay.Tuple([bop_3987,call_3991,])
func_4033 = relay.Function([], output)
mod['func_4033'] = func_4033
mod = relay.transform.InferType()(mod)
mutated_mod['func_4033'] = func_4033
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4033_call = mutated_mod.get_global_var('func_4033')
call_4034 = func_4033_call()
output = call_4034
func_4035 = relay.Function([], output)
mutated_mod['func_4035'] = func_4035
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3952_call = mod.get_global_var('func_3952')
func_3954_call = mutated_mod.get_global_var('func_3954')
call_4040 = func_3952_call()
call_4041 = func_3952_call()
output = relay.Tuple([call_4040,])
output2 = relay.Tuple([call_4041,])
func_4049 = relay.Function([], output)
mod['func_4049'] = func_4049
mod = relay.transform.InferType()(mod)
output = func_4049()
func_4050 = relay.Function([], output)
mutated_mod['func_4050'] = func_4050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4033_call = mod.get_global_var('func_4033')
func_4035_call = mutated_mod.get_global_var('func_4035')
call_4064 = relay.TupleGetItem(func_4033_call(), 0)
call_4065 = relay.TupleGetItem(func_4035_call(), 0)
output = call_4064
output2 = call_4065
func_4073 = relay.Function([], output)
mod['func_4073'] = func_4073
mod = relay.transform.InferType()(mod)
mutated_mod['func_4073'] = func_4073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4073_call = mutated_mod.get_global_var('func_4073')
call_4074 = func_4073_call()
output = call_4074
func_4075 = relay.Function([], output)
mutated_mod['func_4075'] = func_4075
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4078 = relay.var("var_4078", dtype = "float32", shape = (8, 16, 3))#candidate|4078|(8, 16, 3)|var|float32
uop_4079 = relay.sinh(var_4078.astype('float32')) # shape=(8, 16, 3)
uop_4081 = relay.atanh(uop_4079.astype('float64')) # shape=(8, 16, 3)
output = relay.Tuple([uop_4081,])
output2 = relay.Tuple([uop_4081,])
func_4087 = relay.Function([var_4078,], output)
mod['func_4087'] = func_4087
mod = relay.transform.InferType()(mod)
mutated_mod['func_4087'] = func_4087
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4088 = relay.var("var_4088", dtype = "float32", shape = (8, 16, 3))#candidate|4088|(8, 16, 3)|var|float32
func_4087_call = mutated_mod.get_global_var('func_4087')
call_4089 = func_4087_call(var_4088)
output = call_4089
func_4090 = relay.Function([var_4088], output)
mutated_mod['func_4090'] = func_4090
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3491_call = mod.get_global_var('func_3491')
func_3493_call = mutated_mod.get_global_var('func_3493')
call_4103 = relay.TupleGetItem(func_3491_call(), 0)
call_4104 = relay.TupleGetItem(func_3493_call(), 0)
output = relay.Tuple([call_4103,])
output2 = relay.Tuple([call_4104,])
func_4106 = relay.Function([], output)
mod['func_4106'] = func_4106
mod = relay.transform.InferType()(mod)
output = func_4106()
func_4107 = relay.Function([], output)
mutated_mod['func_4107'] = func_4107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3074_call = mod.get_global_var('func_3074')
func_3076_call = mutated_mod.get_global_var('func_3076')
call_4181 = func_3074_call()
call_4182 = func_3074_call()
output = relay.Tuple([call_4181,])
output2 = relay.Tuple([call_4182,])
func_4198 = relay.Function([], output)
mod['func_4198'] = func_4198
mod = relay.transform.InferType()(mod)
output = func_4198()
func_4199 = relay.Function([], output)
mutated_mod['func_4199'] = func_4199
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4203 = relay.const([[[-8.530584],[8.953469],[-8.679445],[-2.640016],[-1.512543],[-9.366515],[-0.198542],[6.400165],[-3.122352],[1.985681],[-1.950113]],[[-1.775059],[5.074769],[-4.610149],[-7.185771],[6.111793],[1.711837],[1.673184],[-1.307235],[0.059122],[3.497699],[4.430440]],[[2.984547],[-2.280306],[-3.253808],[7.606911],[7.794663],[-4.631313],[-0.523760],[-3.153398],[-9.780075],[6.144571],[-4.298585]],[[-0.130453],[-3.432648],[5.494295],[6.833216],[4.825987],[9.681289],[1.305563],[-6.269156],[-6.273339],[-8.262460],[-0.594166]],[[6.280449],[3.029967],[-0.446333],[-5.862179],[5.098585],[1.704203],[-6.868193],[1.946829],[-6.430553],[-9.315564],[-8.875141]],[[3.885390],[5.200280],[-7.502592],[4.745093],[-6.768941],[4.908619],[-6.082460],[-0.673438],[-7.467969],[5.914403],[3.840220]],[[-3.936065],[-0.612872],[1.946347],[-4.878938],[-0.718945],[-1.945598],[-4.668594],[3.901194],[-2.687623],[-6.872248],[7.166421]],[[5.506954],[0.962617],[6.916019],[-7.027371],[0.139221],[1.365574],[1.420357],[-5.590620],[-9.997019],[7.745478],[-0.257164]],[[9.941497],[4.922063],[3.245521],[-2.899080],[2.714430],[-2.278813],[4.874321],[9.757675],[-8.828588],[0.449237],[-8.840233]]], dtype = "float64")#candidate|4203|(9, 11, 1)|const|float64
var_4204 = relay.var("var_4204", dtype = "float64", shape = (9, 11, 1))#candidate|4204|(9, 11, 1)|var|float64
bop_4205 = relay.floor_mod(const_4203.astype('float64'), relay.reshape(var_4204.astype('float64'), relay.shape_of(const_4203))) # shape=(9, 11, 1)
var_4218 = relay.var("var_4218", dtype = "float64", shape = (9, 11, 15))#candidate|4218|(9, 11, 15)|var|float64
bop_4219 = relay.add(var_4204.astype('int8'), var_4218.astype('int8')) # shape=(9, 11, 15)
uop_4236 = relay.tan(var_4218.astype('float32')) # shape=(9, 11, 15)
func_2349_call = mod.get_global_var('func_2349')
func_2354_call = mutated_mod.get_global_var('func_2354')
const_4257 = relay.const([1,-5,-3,-10,6,-4,7,5,-6,-2,10,-7,2,10,8,-5,3,-3,4,-5,1,3,1,-4,2,2,-10,2,-8,-7,2,-5,-4,3,-2,-8,-8,-5,-3,-3,-6,9,-4,7,-3,-6,6,10,-10,8,1,-6,-1,5,-1,8,-3,-3,-8,-7], dtype = "uint8")#candidate|4257|(60,)|const|uint8
const_4258 = relay.const([[-6.218482,-5.263947,4.757197,0.495554,1.731451,-5.811159],[-3.489080,8.796438,6.330001,-1.796764,0.210216,-7.575523],[-8.132872,-2.444664,7.996139,-6.486191,3.316785,-2.594159],[-2.671581,4.252092,-4.953737,3.130590,7.067154,-2.702513],[-2.610153,-0.677355,-8.304498,-4.334456,-7.518216,3.722827],[5.898795,-8.056008,9.213313,9.013466,-1.570288,2.488903],[-8.116264,7.231676,-9.169879,-2.641761,-5.183963,-9.883358],[-8.166206,-4.710846,5.887463,-6.428468,9.835419,0.828076],[6.727637,-0.130537,2.821479,-0.308620,1.904287,-1.358883],[1.735872,-5.073602,8.402414,-6.760632,3.557383,5.576648],[5.194997,2.019975,-9.832550,5.277509,4.187882,8.778935],[8.781133,1.847462,7.066310,-5.811963,-7.705072,-0.747939],[9.673298,6.533459,9.481343,-7.307142,-8.564666,-4.831487],[-6.319164,-6.026587,8.650106,2.862230,-6.612062,9.667545],[-1.712041,-7.343097,2.044813,-6.610690,-4.151693,5.560279],[-7.410891,-7.281386,-2.930773,3.646056,-7.653182,-6.635763],[9.604102,-9.993899,-2.304888,7.817679,-7.450412,-6.810658],[4.286448,-5.881166,-5.505749,0.628818,2.504294,-2.202446],[-7.485100,2.163661,7.826955,8.392114,4.648544,-8.893770],[1.365215,-2.449394,-1.887266,5.248684,7.465143,1.246461],[-6.300370,8.029824,-6.220207,9.479939,7.809494,6.263928],[-8.423795,-1.367749,-4.238442,-0.399864,-2.275231,3.988310],[8.315046,-4.608814,8.816551,-0.129866,9.646026,1.789753],[0.701173,-1.309590,6.743425,-0.305125,-5.380448,6.947165],[0.135361,6.606658,-9.140451,-0.129212,9.644601,8.212232],[-2.846395,-0.209972,1.105356,5.533057,-3.781731,0.311519],[8.253413,-7.975459,-6.668479,5.196496,9.297577,-8.301228],[1.299759,1.459700,2.586669,5.712043,-6.085299,7.043504],[-3.670496,4.349053,5.351433,-0.625044,-1.720906,-3.577278],[0.518144,-3.007320,-8.111928,-3.209622,-9.214123,4.842284],[-2.599319,0.470341,-9.132292,-1.554035,-5.601841,-9.026556],[7.586509,-2.175295,2.741095,-4.763601,-8.184435,2.858975],[7.034003,4.240148,9.494572,-4.841045,0.502661,-9.241818],[-3.174988,-6.851011,-0.045581,-4.002053,-9.473521,4.064076],[-5.167032,-7.625410,6.712615,0.219452,2.795171,-9.469449],[0.441282,9.790421,-7.507854,3.095453,-4.249221,2.403310]], dtype = "float64")#candidate|4258|(36, 6)|const|float64
var_4259 = relay.var("var_4259", dtype = "uint32", shape = ())#candidate|4259|()|var|uint32
call_4256 = relay.TupleGetItem(func_2349_call(relay.reshape(const_4257.astype('uint8'), [3, 5, 4]), relay.reshape(const_4258.astype('float64'), [216,]), relay.reshape(var_4259.astype('uint32'), []), ), 1)
call_4260 = relay.TupleGetItem(func_2354_call(relay.reshape(const_4257.astype('uint8'), [3, 5, 4]), relay.reshape(const_4258.astype('float64'), [216,]), relay.reshape(var_4259.astype('uint32'), []), ), 1)
uop_4261 = relay.log(uop_4236.astype('float64')) # shape=(9, 11, 15)
output = relay.Tuple([bop_4205,bop_4219,call_4256,const_4257,const_4258,var_4259,uop_4261,])
output2 = relay.Tuple([bop_4205,bop_4219,call_4260,const_4257,const_4258,var_4259,uop_4261,])
func_4266 = relay.Function([var_4204,var_4218,var_4259,], output)
mod['func_4266'] = func_4266
mod = relay.transform.InferType()(mod)
mutated_mod['func_4266'] = func_4266
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4266_call = mutated_mod.get_global_var('func_4266')
var_4268 = relay.var("var_4268", dtype = "float64", shape = (9, 11, 1))#candidate|4268|(9, 11, 1)|var|float64
var_4269 = relay.var("var_4269", dtype = "float64", shape = (9, 11, 15))#candidate|4269|(9, 11, 15)|var|float64
var_4270 = relay.var("var_4270", dtype = "uint32", shape = ())#candidate|4270|()|var|uint32
call_4267 = func_4266_call(var_4268,var_4269,var_4270,)
output = call_4267
func_4271 = relay.Function([var_4268,var_4269,var_4270,], output)
mutated_mod['func_4271'] = func_4271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3274_call = mod.get_global_var('func_3274')
func_3275_call = mutated_mod.get_global_var('func_3275')
call_4294 = relay.TupleGetItem(func_3274_call(), 0)
call_4295 = relay.TupleGetItem(func_3275_call(), 0)
func_2601_call = mod.get_global_var('func_2601')
func_2603_call = mutated_mod.get_global_var('func_2603')
var_4302 = relay.var("var_4302", dtype = "float32", shape = (48,))#candidate|4302|(48,)|var|float32
call_4301 = relay.TupleGetItem(func_2601_call(relay.reshape(var_4302.astype('float32'), [4, 4, 3])), 2)
call_4303 = relay.TupleGetItem(func_2603_call(relay.reshape(var_4302.astype('float32'), [4, 4, 3])), 2)
output = relay.Tuple([call_4294,call_4301,var_4302,])
output2 = relay.Tuple([call_4295,call_4303,var_4302,])
func_4316 = relay.Function([var_4302,], output)
mod['func_4316'] = func_4316
mod = relay.transform.InferType()(mod)
var_4317 = relay.var("var_4317", dtype = "float32", shape = (48,))#candidate|4317|(48,)|var|float32
output = func_4316(var_4317)
func_4318 = relay.Function([var_4317], output)
mutated_mod['func_4318'] = func_4318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4106_call = mod.get_global_var('func_4106')
func_4107_call = mutated_mod.get_global_var('func_4107')
call_4353 = relay.TupleGetItem(func_4106_call(), 0)
call_4354 = relay.TupleGetItem(func_4107_call(), 0)
output = relay.Tuple([call_4353,])
output2 = relay.Tuple([call_4354,])
func_4359 = relay.Function([], output)
mod['func_4359'] = func_4359
mod = relay.transform.InferType()(mod)
mutated_mod['func_4359'] = func_4359
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4359_call = mutated_mod.get_global_var('func_4359')
call_4360 = func_4359_call()
output = call_4360
func_4361 = relay.Function([], output)
mutated_mod['func_4361'] = func_4361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4073_call = mod.get_global_var('func_4073')
func_4075_call = mutated_mod.get_global_var('func_4075')
call_4386 = func_4073_call()
call_4387 = func_4073_call()
output = call_4386
output2 = call_4387
func_4397 = relay.Function([], output)
mod['func_4397'] = func_4397
mod = relay.transform.InferType()(mod)
output = func_4397()
func_4398 = relay.Function([], output)
mutated_mod['func_4398'] = func_4398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3158_call = mod.get_global_var('func_3158')
func_3160_call = mutated_mod.get_global_var('func_3160')
call_4401 = relay.TupleGetItem(func_3158_call(), 0)
call_4402 = relay.TupleGetItem(func_3160_call(), 0)
output = relay.Tuple([call_4401,])
output2 = relay.Tuple([call_4402,])
func_4426 = relay.Function([], output)
mod['func_4426'] = func_4426
mod = relay.transform.InferType()(mod)
mutated_mod['func_4426'] = func_4426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4426_call = mutated_mod.get_global_var('func_4426')
call_4427 = func_4426_call()
output = call_4427
func_4428 = relay.Function([], output)
mutated_mod['func_4428'] = func_4428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3945_call = mod.get_global_var('func_3945')
func_3947_call = mutated_mod.get_global_var('func_3947')
call_4447 = relay.TupleGetItem(func_3945_call(), 1)
call_4448 = relay.TupleGetItem(func_3947_call(), 1)
output = call_4447
output2 = call_4448
func_4452 = relay.Function([], output)
mod['func_4452'] = func_4452
mod = relay.transform.InferType()(mod)
mutated_mod['func_4452'] = func_4452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4452_call = mutated_mod.get_global_var('func_4452')
call_4453 = func_4452_call()
output = call_4453
func_4454 = relay.Function([], output)
mutated_mod['func_4454'] = func_4454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3615_call = mod.get_global_var('func_3615')
func_3616_call = mutated_mod.get_global_var('func_3616')
call_4466 = relay.TupleGetItem(func_3615_call(), 0)
call_4467 = relay.TupleGetItem(func_3616_call(), 0)
output = relay.Tuple([call_4466,])
output2 = relay.Tuple([call_4467,])
func_4492 = relay.Function([], output)
mod['func_4492'] = func_4492
mod = relay.transform.InferType()(mod)
output = func_4492()
func_4493 = relay.Function([], output)
mutated_mod['func_4493'] = func_4493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3876_call = mod.get_global_var('func_3876')
func_3877_call = mutated_mod.get_global_var('func_3877')
call_4496 = func_3876_call()
call_4497 = func_3876_call()
func_4106_call = mod.get_global_var('func_4106')
func_4107_call = mutated_mod.get_global_var('func_4107')
call_4502 = relay.TupleGetItem(func_4106_call(), 0)
call_4503 = relay.TupleGetItem(func_4107_call(), 0)
func_3820_call = mod.get_global_var('func_3820')
func_3826_call = mutated_mod.get_global_var('func_3826')
var_4507 = relay.var("var_4507", dtype = "uint32", shape = ())#candidate|4507|()|var|uint32
const_4508 = relay.const([-6,-5,-9,-5,1,-6,3,4,3,-3,5,-1,7,-7,2,3,7,1,10,-4,-5,-6,6,4,-9,2,-1,3,1,-8], dtype = "int32")#candidate|4508|(30,)|const|int32
var_4509 = relay.var("var_4509", dtype = "float64", shape = (10, 30))#candidate|4509|(10, 30)|var|float64
var_4510 = relay.var("var_4510", dtype = "float64", shape = (40, 8))#candidate|4510|(40, 8)|var|float64
call_4506 = relay.TupleGetItem(func_3820_call(relay.reshape(var_4507.astype('uint32'), []), relay.reshape(const_4508.astype('int32'), [5, 6]), relay.reshape(var_4509.astype('float64'), [150, 2]), relay.reshape(var_4510.astype('float64'), [320,]), ), 1)
call_4511 = relay.TupleGetItem(func_3826_call(relay.reshape(var_4507.astype('uint32'), []), relay.reshape(const_4508.astype('int32'), [5, 6]), relay.reshape(var_4509.astype('float64'), [150, 2]), relay.reshape(var_4510.astype('float64'), [320,]), ), 1)
output = relay.Tuple([call_4496,call_4502,call_4506,var_4507,const_4508,var_4509,var_4510,])
output2 = relay.Tuple([call_4497,call_4503,call_4511,var_4507,const_4508,var_4509,var_4510,])
func_4517 = relay.Function([var_4507,var_4509,var_4510,], output)
mod['func_4517'] = func_4517
mod = relay.transform.InferType()(mod)
var_4518 = relay.var("var_4518", dtype = "uint32", shape = ())#candidate|4518|()|var|uint32
var_4519 = relay.var("var_4519", dtype = "float64", shape = (10, 30))#candidate|4519|(10, 30)|var|float64
var_4520 = relay.var("var_4520", dtype = "float64", shape = (40, 8))#candidate|4520|(40, 8)|var|float64
output = func_4517(var_4518,var_4519,var_4520,)
func_4521 = relay.Function([var_4518,var_4519,var_4520,], output)
mutated_mod['func_4521'] = func_4521
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2980_call = mod.get_global_var('func_2980')
func_2982_call = mutated_mod.get_global_var('func_2982')
call_4592 = func_2980_call()
call_4593 = func_2980_call()
func_3562_call = mod.get_global_var('func_3562')
func_3564_call = mutated_mod.get_global_var('func_3564')
var_4603 = relay.var("var_4603", dtype = "uint8", shape = (80,))#candidate|4603|(80,)|var|uint8
call_4602 = relay.TupleGetItem(func_3562_call(relay.reshape(var_4603.astype('uint8'), [8, 2, 5])), 0)
call_4604 = relay.TupleGetItem(func_3564_call(relay.reshape(var_4603.astype('uint8'), [8, 2, 5])), 0)
func_3820_call = mod.get_global_var('func_3820')
func_3826_call = mutated_mod.get_global_var('func_3826')
var_4614 = relay.var("var_4614", dtype = "uint32", shape = ())#candidate|4614|()|var|uint32
const_4615 = relay.const([[-6],[-2],[2],[5],[-5],[-9],[-5],[-7],[-10],[5],[-3],[8],[9],[-6],[10],[1],[-6],[2],[-6],[-1],[5],[6],[-5],[-4],[-3],[2],[10],[-4],[9],[-10]], dtype = "int32")#candidate|4615|(30, 1)|const|int32
const_4616 = relay.const([[5.874679,-7.831230,5.089057,0.425603,0.582767,-8.897835,-5.084134,6.593270,-5.075854,-3.962577,-4.249315,1.412999,-3.173467,5.203649,-6.872729,1.723358,-6.087247,-6.816236,-7.351216,-6.597105,8.327326,-7.186152,0.305540,-7.919196,4.546863,9.661926,3.738560,-7.409972,-7.077495,1.748445,-2.148250,-2.135183,-8.631463,-9.863421,-5.875472,-6.778567,-5.299474,2.327474,-1.175747,8.877403,7.868769,4.789353,2.964170,-4.596804,-3.056103,0.174007,7.361212,4.376829,-9.836562,-6.014593,-4.709556,-1.818989,-4.680555,8.615946,3.170066,-5.737247,6.533954,-6.537107,4.710142,-5.004848],[-4.150298,-8.322141,4.761859,0.999161,-3.117337,1.970591,-9.806975,1.814414,0.401469,-8.595727,2.866087,2.179831,-0.640026,-1.763447,1.655951,5.557696,-2.666476,1.086207,9.493343,5.738595,-2.441821,9.830289,-4.393882,4.459995,0.448443,-5.732258,-5.483945,4.771558,8.089842,5.849239,0.058545,-8.533653,-6.736918,4.781129,-7.926882,3.278899,6.232839,-7.756152,8.121618,-3.020808,2.640845,-3.748423,-8.296428,-9.347258,4.415896,-3.522080,6.555522,-8.906508,-6.820502,6.623723,-6.088629,-9.069664,0.401628,2.480528,-3.624149,6.539786,-7.278326,-0.348372,-5.860645,8.922857],[-6.338076,-4.674408,-3.170749,0.522395,-9.511710,-3.025420,-6.407218,1.623838,3.460856,-3.962448,-9.591341,5.239021,4.456295,6.830628,-1.895828,2.721301,6.911220,-4.437458,-8.805923,-2.747804,8.461264,8.228589,7.291697,6.950055,0.747740,9.877464,-0.538674,6.426427,-6.810653,1.962554,4.838594,8.680482,-9.091464,-5.515744,8.222207,5.306733,8.178210,-0.417374,9.418453,8.220081,-1.977681,-9.422763,9.694820,-2.457325,0.544032,4.792973,7.567782,3.488425,-4.416419,-0.038094,-4.390359,-1.770478,3.479209,8.786633,8.174009,8.458640,1.347129,-2.043698,5.106127,-7.335875],[-4.257633,3.401808,-2.367395,2.818407,9.402491,-7.816251,5.389322,8.040488,-5.317962,-4.532636,-3.853235,6.740990,2.914266,-8.069461,-9.501671,6.050823,-5.943596,-9.462961,7.654528,-6.515583,-9.085134,3.154833,9.140901,-4.052800,8.981678,9.775317,-8.271019,6.353851,-5.183972,6.909673,-8.069505,2.978055,5.866095,3.861765,8.403370,3.163841,-6.816034,-4.222900,-4.547715,2.337949,1.544831,2.777991,1.145874,5.473992,-2.891697,6.817658,-6.623508,-2.481249,-3.177537,-9.598929,9.434762,8.082159,-4.056212,0.580640,-4.744213,-0.381608,-0.278790,-3.206457,-2.421429,3.242953],[-1.964200,2.470908,-5.417034,-7.639880,3.373623,-4.117760,6.690835,7.021771,1.870977,-8.724543,8.951352,1.200399,-6.747388,-9.839412,-1.752323,5.602410,-4.652971,6.085639,-8.263227,0.793455,-2.666554,-1.304527,-6.839682,-1.035541,1.335972,7.894077,9.569214,-1.068467,-5.004358,2.668903,-6.703439,1.572902,8.723378,7.841514,4.873796,-4.661011,2.905402,0.820267,-6.992213,8.080371,-7.208041,-8.684050,-0.527698,4.806537,3.063586,1.320486,8.868282,-5.178872,6.259329,0.227770,1.749278,-9.144230,-8.199041,-1.950525,7.643357,-8.058325,-4.115254,-4.216401,2.725850,-6.081029]], dtype = "float64")#candidate|4616|(5, 60)|const|float64
var_4617 = relay.var("var_4617", dtype = "float64", shape = (320,))#candidate|4617|(320,)|var|float64
call_4613 = relay.TupleGetItem(func_3820_call(relay.reshape(var_4614.astype('uint32'), []), relay.reshape(const_4615.astype('int32'), [5, 6]), relay.reshape(const_4616.astype('float64'), [150, 2]), relay.reshape(var_4617.astype('float64'), [320,]), ), 8)
call_4618 = relay.TupleGetItem(func_3826_call(relay.reshape(var_4614.astype('uint32'), []), relay.reshape(const_4615.astype('int32'), [5, 6]), relay.reshape(const_4616.astype('float64'), [150, 2]), relay.reshape(var_4617.astype('float64'), [320,]), ), 8)
bop_4621 = relay.logical_and(var_4617.astype('bool'), const_4615.astype('bool')) # shape=(30, 320)
uop_4625 = relay.sinh(call_4613.astype('float64')) # shape=(10, 2, 16)
uop_4627 = relay.sinh(call_4618.astype('float64')) # shape=(10, 2, 16)
output = relay.Tuple([call_4592,call_4602,var_4603,var_4614,const_4616,bop_4621,uop_4625,])
output2 = relay.Tuple([call_4593,call_4604,var_4603,var_4614,const_4616,bop_4621,uop_4627,])
func_4635 = relay.Function([var_4603,var_4614,var_4617,], output)
mod['func_4635'] = func_4635
mod = relay.transform.InferType()(mod)
var_4636 = relay.var("var_4636", dtype = "uint8", shape = (80,))#candidate|4636|(80,)|var|uint8
var_4637 = relay.var("var_4637", dtype = "uint32", shape = ())#candidate|4637|()|var|uint32
var_4638 = relay.var("var_4638", dtype = "float64", shape = (320,))#candidate|4638|(320,)|var|float64
output = func_4635(var_4636,var_4637,var_4638,)
func_4639 = relay.Function([var_4636,var_4637,var_4638,], output)
mutated_mod['func_4639'] = func_4639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4106_call = mod.get_global_var('func_4106')
func_4107_call = mutated_mod.get_global_var('func_4107')
call_4649 = relay.TupleGetItem(func_4106_call(), 0)
call_4650 = relay.TupleGetItem(func_4107_call(), 0)
output = relay.Tuple([call_4649,])
output2 = relay.Tuple([call_4650,])
func_4684 = relay.Function([], output)
mod['func_4684'] = func_4684
mod = relay.transform.InferType()(mod)
output = func_4684()
func_4685 = relay.Function([], output)
mutated_mod['func_4685'] = func_4685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2859_call = mod.get_global_var('func_2859')
func_2860_call = mutated_mod.get_global_var('func_2860')
call_4700 = func_2859_call()
call_4701 = func_2859_call()
output = relay.Tuple([call_4700,])
output2 = relay.Tuple([call_4701,])
func_4708 = relay.Function([], output)
mod['func_4708'] = func_4708
mod = relay.transform.InferType()(mod)
output = func_4708()
func_4709 = relay.Function([], output)
mutated_mod['func_4709'] = func_4709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3491_call = mod.get_global_var('func_3491')
func_3493_call = mutated_mod.get_global_var('func_3493')
call_4742 = relay.TupleGetItem(func_3491_call(), 0)
call_4743 = relay.TupleGetItem(func_3493_call(), 0)
output = relay.Tuple([call_4742,])
output2 = relay.Tuple([call_4743,])
func_4773 = relay.Function([], output)
mod['func_4773'] = func_4773
mod = relay.transform.InferType()(mod)
output = func_4773()
func_4774 = relay.Function([], output)
mutated_mod['func_4774'] = func_4774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3952_call = mod.get_global_var('func_3952')
func_3954_call = mutated_mod.get_global_var('func_3954')
call_4793 = func_3952_call()
call_4794 = func_3952_call()
output = call_4793
output2 = call_4794
func_4821 = relay.Function([], output)
mod['func_4821'] = func_4821
mod = relay.transform.InferType()(mod)
output = func_4821()
func_4822 = relay.Function([], output)
mutated_mod['func_4822'] = func_4822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2980_call = mod.get_global_var('func_2980')
func_2982_call = mutated_mod.get_global_var('func_2982')
call_4837 = func_2980_call()
call_4838 = func_2980_call()
output = relay.Tuple([call_4837,])
output2 = relay.Tuple([call_4838,])
func_4841 = relay.Function([], output)
mod['func_4841'] = func_4841
mod = relay.transform.InferType()(mod)
output = func_4841()
func_4842 = relay.Function([], output)
mutated_mod['func_4842'] = func_4842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3016_call = mod.get_global_var('func_3016')
func_3018_call = mutated_mod.get_global_var('func_3018')
call_4847 = relay.TupleGetItem(func_3016_call(), 0)
call_4848 = relay.TupleGetItem(func_3018_call(), 0)
output = relay.Tuple([call_4847,])
output2 = relay.Tuple([call_4848,])
func_4879 = relay.Function([], output)
mod['func_4879'] = func_4879
mod = relay.transform.InferType()(mod)
output = func_4879()
func_4880 = relay.Function([], output)
mutated_mod['func_4880'] = func_4880
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4073_call = mod.get_global_var('func_4073')
func_4075_call = mutated_mod.get_global_var('func_4075')
call_4904 = func_4073_call()
call_4905 = func_4073_call()
func_3952_call = mod.get_global_var('func_3952')
func_3954_call = mutated_mod.get_global_var('func_3954')
call_4930 = func_3952_call()
call_4931 = func_3952_call()
func_2980_call = mod.get_global_var('func_2980')
func_2982_call = mutated_mod.get_global_var('func_2982')
call_4932 = func_2980_call()
call_4933 = func_2980_call()
output = relay.Tuple([call_4904,call_4930,call_4932,])
output2 = relay.Tuple([call_4905,call_4931,call_4933,])
func_4950 = relay.Function([], output)
mod['func_4950'] = func_4950
mod = relay.transform.InferType()(mod)
mutated_mod['func_4950'] = func_4950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4950_call = mutated_mod.get_global_var('func_4950')
call_4951 = func_4950_call()
output = call_4951
func_4952 = relay.Function([], output)
mutated_mod['func_4952'] = func_4952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3158_call = mod.get_global_var('func_3158')
func_3160_call = mutated_mod.get_global_var('func_3160')
call_4984 = relay.TupleGetItem(func_3158_call(), 1)
call_4985 = relay.TupleGetItem(func_3160_call(), 1)
func_3876_call = mod.get_global_var('func_3876')
func_3877_call = mutated_mod.get_global_var('func_3877')
call_5002 = func_3876_call()
call_5003 = func_3876_call()
output = relay.Tuple([call_4984,call_5002,])
output2 = relay.Tuple([call_4985,call_5003,])
func_5034 = relay.Function([], output)
mod['func_5034'] = func_5034
mod = relay.transform.InferType()(mod)
output = func_5034()
func_5035 = relay.Function([], output)
mutated_mod['func_5035'] = func_5035
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5070 = relay.var("var_5070", dtype = "float32", shape = (5, 8, 7))#candidate|5070|(5, 8, 7)|var|float32
uop_5071 = relay.cos(var_5070.astype('float32')) # shape=(5, 8, 7)
output = uop_5071
output2 = uop_5071
func_5076 = relay.Function([var_5070,], output)
mod['func_5076'] = func_5076
mod = relay.transform.InferType()(mod)
mutated_mod['func_5076'] = func_5076
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5077 = relay.var("var_5077", dtype = "float32", shape = (5, 8, 7))#candidate|5077|(5, 8, 7)|var|float32
func_5076_call = mutated_mod.get_global_var('func_5076')
call_5078 = func_5076_call(var_5077)
output = call_5078
func_5079 = relay.Function([var_5077], output)
mutated_mod['func_5079'] = func_5079
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5120 = relay.var("var_5120", dtype = "bool", shape = ())#candidate|5120|()|var|bool
var_5121 = relay.var("var_5121", dtype = "bool", shape = (16, 7, 9))#candidate|5121|(16, 7, 9)|var|bool
bop_5122 = relay.logical_and(var_5120.astype('bool'), var_5121.astype('bool')) # shape=(16, 7, 9)
output = relay.Tuple([bop_5122,])
output2 = relay.Tuple([bop_5122,])
func_5132 = relay.Function([var_5120,var_5121,], output)
mod['func_5132'] = func_5132
mod = relay.transform.InferType()(mod)
mutated_mod['func_5132'] = func_5132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5132_call = mutated_mod.get_global_var('func_5132')
var_5134 = relay.var("var_5134", dtype = "bool", shape = ())#candidate|5134|()|var|bool
var_5135 = relay.var("var_5135", dtype = "bool", shape = (16, 7, 9))#candidate|5135|(16, 7, 9)|var|bool
call_5133 = func_5132_call(var_5134,var_5135,)
output = call_5133
func_5136 = relay.Function([var_5134,var_5135,], output)
mutated_mod['func_5136'] = func_5136
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5200 = relay.var("var_5200", dtype = "float64", shape = (9, 7, 4))#candidate|5200|(9, 7, 4)|var|float64
uop_5201 = relay.sigmoid(var_5200.astype('float64')) # shape=(9, 7, 4)
output = uop_5201
output2 = uop_5201
func_5207 = relay.Function([var_5200,], output)
mod['func_5207'] = func_5207
mod = relay.transform.InferType()(mod)
mutated_mod['func_5207'] = func_5207
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5208 = relay.var("var_5208", dtype = "float64", shape = (9, 7, 4))#candidate|5208|(9, 7, 4)|var|float64
func_5207_call = mutated_mod.get_global_var('func_5207')
call_5209 = func_5207_call(var_5208)
output = call_5209
func_5210 = relay.Function([var_5208], output)
mutated_mod['func_5210'] = func_5210
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3491_call = mod.get_global_var('func_3491')
func_3493_call = mutated_mod.get_global_var('func_3493')
call_5214 = relay.TupleGetItem(func_3491_call(), 0)
call_5215 = relay.TupleGetItem(func_3493_call(), 0)
func_3562_call = mod.get_global_var('func_3562')
func_3564_call = mutated_mod.get_global_var('func_3564')
var_5226 = relay.var("var_5226", dtype = "uint8", shape = (20, 4))#candidate|5226|(20, 4)|var|uint8
call_5225 = relay.TupleGetItem(func_3562_call(relay.reshape(var_5226.astype('uint8'), [8, 2, 5])), 0)
call_5227 = relay.TupleGetItem(func_3564_call(relay.reshape(var_5226.astype('uint8'), [8, 2, 5])), 0)
func_5034_call = mod.get_global_var('func_5034')
func_5035_call = mutated_mod.get_global_var('func_5035')
call_5246 = relay.TupleGetItem(func_5034_call(), 0)
call_5247 = relay.TupleGetItem(func_5035_call(), 0)
output = relay.Tuple([call_5214,call_5225,var_5226,call_5246,])
output2 = relay.Tuple([call_5215,call_5227,var_5226,call_5247,])
func_5258 = relay.Function([var_5226,], output)
mod['func_5258'] = func_5258
mod = relay.transform.InferType()(mod)
var_5259 = relay.var("var_5259", dtype = "uint8", shape = (20, 4))#candidate|5259|(20, 4)|var|uint8
output = func_5258(var_5259)
func_5260 = relay.Function([var_5259], output)
mutated_mod['func_5260'] = func_5260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3274_call = mod.get_global_var('func_3274')
func_3275_call = mutated_mod.get_global_var('func_3275')
call_5286 = relay.TupleGetItem(func_3274_call(), 0)
call_5287 = relay.TupleGetItem(func_3275_call(), 0)
func_3274_call = mod.get_global_var('func_3274')
func_3275_call = mutated_mod.get_global_var('func_3275')
call_5294 = relay.TupleGetItem(func_3274_call(), 0)
call_5295 = relay.TupleGetItem(func_3275_call(), 0)
output = relay.Tuple([call_5286,call_5294,])
output2 = relay.Tuple([call_5287,call_5295,])
func_5298 = relay.Function([], output)
mod['func_5298'] = func_5298
mod = relay.transform.InferType()(mod)
output = func_5298()
func_5299 = relay.Function([], output)
mutated_mod['func_5299'] = func_5299
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5369 = relay.const([[[7.641826,-7.323503,7.631254,-9.458297,-4.655447,-0.834713,-9.490487,-0.100756,-9.475160,3.326339,-1.612794,-0.166487,-8.654954],[-7.367864,4.363891,8.839690,4.293464,-7.443310,3.521638,-8.436070,-0.553015,-6.757907,-3.250297,-0.777507,-5.137494,-3.960869],[-4.615455,9.536512,-0.275649,-8.761562,-5.913748,-6.459049,3.839366,-0.467604,3.214424,-2.228361,2.599069,-7.099339,-9.414218]],[[-6.309704,0.913136,9.197550,-9.314786,-1.262134,-0.291463,-2.890888,1.822569,-7.519634,1.306628,8.802015,-0.669132,-6.815357],[-5.879744,7.950255,1.293870,-7.644832,-2.014867,-2.968682,-5.786054,6.785728,-2.411588,2.223319,-6.198171,-7.564279,3.783175],[-9.891502,-2.275298,7.670739,-5.242114,0.091152,5.527486,-6.444219,8.437728,-8.202055,7.839428,-3.067740,4.199013,2.373068]],[[1.159144,1.473078,2.362293,-3.458624,-4.997527,4.782350,-7.713966,-4.337238,-3.877893,2.552573,-8.304345,0.601561,8.453816],[1.626575,-9.702903,-7.766700,-3.185141,-8.480975,-2.145616,8.117410,-0.634890,7.811666,2.834164,-7.996674,-8.458709,1.110635],[4.780923,-9.461022,-5.205479,3.994027,8.170415,2.988165,4.222895,1.460080,-8.563508,-7.191339,8.480124,-5.842949,-6.502661]],[[-5.204519,-5.498551,9.691092,6.316757,2.580565,1.512262,-9.413622,-6.081269,-2.070663,1.114101,0.512258,2.610376,-4.277134],[9.980077,4.115793,-3.425614,-5.822177,-5.669560,-8.768515,-8.236413,8.877321,3.592882,-8.741611,8.301944,9.436301,-1.320865],[7.448133,4.920713,9.322326,-5.681927,-0.853183,-4.401524,9.220623,-6.634716,-4.317323,1.023616,-7.857725,6.186174,1.250563]],[[6.160667,1.382216,7.270755,9.441895,4.227021,-5.127777,-7.272921,-8.405510,7.370032,1.621117,0.008419,-8.774468,6.969223],[4.522803,4.310392,-5.312445,-2.745584,4.642211,-5.783798,-8.999561,2.682308,6.492144,0.238574,-8.557633,0.682645,-4.776130],[-6.998640,-5.321067,6.238958,-7.276511,-9.508974,9.889545,3.181190,-6.960716,-2.914745,8.527467,5.324329,5.484527,-7.064394]],[[-1.703178,4.496171,-5.489556,5.364567,7.230892,0.424012,-9.370236,-7.367776,-6.173359,-3.219909,2.316284,7.933636,-3.129052],[2.875521,3.252002,2.003529,-1.796591,-6.109675,-0.956410,8.979670,-4.413642,-6.610541,-7.130423,-2.552263,-0.229181,5.356745],[0.617765,-0.332797,-4.309702,8.181414,3.541261,6.880808,8.489782,-6.398066,6.891339,-3.604985,-2.793530,-9.922333,1.474193]],[[6.609749,4.044240,-1.967497,6.288135,-7.457267,-4.430493,1.519828,2.356420,3.369643,-2.099478,-1.302444,4.175048,6.550314],[8.051540,-8.340179,3.857065,-5.239775,1.776538,4.596570,2.130824,-7.238996,-0.687001,5.444649,-6.629825,-5.935958,3.809939],[-0.869342,8.118618,-1.324921,-6.452674,-6.132131,7.631645,-4.679075,6.847488,3.867241,-1.130675,-3.471826,-7.526049,-1.659999]],[[6.472778,5.533052,9.925467,5.094330,-2.896641,-3.682431,3.155903,-8.022607,7.273724,1.212943,-2.940779,-6.092940,-8.977738],[8.725157,-9.530024,1.609203,9.370036,-7.795317,-6.373463,6.652439,-8.229663,2.502997,-8.502617,-0.690786,3.868302,-0.839319],[-3.095744,-2.470968,-3.556593,5.297031,1.471681,-3.477681,-0.164739,3.859952,-0.530337,3.441747,-4.533782,-1.698365,-0.692362]],[[8.837030,-3.431262,5.064052,-8.162800,3.959103,-7.696848,8.210523,8.891262,-2.521094,3.377858,5.159097,-1.912125,-0.045995],[1.077729,-8.858642,6.179103,1.124464,5.392063,-4.303892,-6.430887,-1.825767,9.554988,-0.723476,9.129245,-7.189315,7.820138],[8.811718,-8.839671,-9.419542,-9.600410,0.874576,-4.116002,-1.331922,2.909680,0.783034,-7.091367,-2.479359,-8.166279,0.363588]],[[4.970839,-4.634985,8.144372,0.787128,9.607118,7.951712,-7.604727,8.353518,-9.206432,-0.709162,-6.285438,0.832298,-7.059314],[-6.408452,1.104711,-7.792316,5.042719,8.162410,-3.869025,-7.838252,-3.647332,-8.284496,-3.720669,-6.789750,1.682205,4.564448],[-1.651638,-9.531514,-3.374275,5.370832,-3.064526,3.664874,-8.074277,-1.544036,6.197274,-3.394482,7.556467,-7.103615,-7.338813]],[[-1.393447,5.768929,-6.056353,-1.746923,-7.659628,3.585251,-2.665252,-6.942787,-6.458747,-0.759682,3.765687,5.118840,-5.547029],[-6.333201,6.254038,7.765975,-9.223798,1.431073,-1.709800,-9.305607,-3.067199,1.240537,4.995851,-3.665406,-5.320929,5.600071],[-7.353200,-1.161446,3.091411,4.628296,7.714943,-5.192602,-7.355795,-4.434176,5.168470,1.930581,2.333141,9.919156,-9.132694]],[[-0.921085,-7.439890,2.790648,-4.794310,2.816748,-3.110945,-5.676837,9.097445,-3.260445,-5.738933,9.261760,7.013807,-3.843575],[4.157769,7.192825,9.633813,-8.383749,6.356484,6.811177,8.647554,8.658767,1.719680,-5.421951,-8.957758,-0.454969,7.417651],[6.837874,8.487386,8.341906,9.839573,-6.252439,-8.201930,-4.697997,-8.201661,-0.736843,5.271838,-3.758384,3.602803,7.975280]]], dtype = "float64")#candidate|5369|(12, 3, 13)|const|float64
uop_5370 = relay.rsqrt(const_5369.astype('float64')) # shape=(12, 3, 13)
uop_5374 = relay.cosh(uop_5370.astype('float32')) # shape=(12, 3, 13)
uop_5388 = relay.log10(uop_5370.astype('float32')) # shape=(12, 3, 13)
output = relay.Tuple([uop_5374,uop_5388,])
output2 = relay.Tuple([uop_5374,uop_5388,])
func_5395 = relay.Function([], output)
mod['func_5395'] = func_5395
mod = relay.transform.InferType()(mod)
output = func_5395()
func_5396 = relay.Function([], output)
mutated_mod['func_5396'] = func_5396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3074_call = mod.get_global_var('func_3074')
func_3076_call = mutated_mod.get_global_var('func_3076')
call_5416 = func_3074_call()
call_5417 = func_3074_call()
output = call_5416
output2 = call_5417
func_5424 = relay.Function([], output)
mod['func_5424'] = func_5424
mod = relay.transform.InferType()(mod)
output = func_5424()
func_5425 = relay.Function([], output)
mutated_mod['func_5425'] = func_5425
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2930_call = mod.get_global_var('func_2930')
func_2931_call = mutated_mod.get_global_var('func_2931')
call_5466 = func_2930_call()
call_5467 = func_2930_call()
output = relay.Tuple([call_5466,])
output2 = relay.Tuple([call_5467,])
func_5476 = relay.Function([], output)
mod['func_5476'] = func_5476
mod = relay.transform.InferType()(mod)
output = func_5476()
func_5477 = relay.Function([], output)
mutated_mod['func_5477'] = func_5477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4073_call = mod.get_global_var('func_4073')
func_4075_call = mutated_mod.get_global_var('func_4075')
call_5481 = func_4073_call()
call_5482 = func_4073_call()
output = call_5481
output2 = call_5482
func_5488 = relay.Function([], output)
mod['func_5488'] = func_5488
mod = relay.transform.InferType()(mod)
output = func_5488()
func_5489 = relay.Function([], output)
mutated_mod['func_5489'] = func_5489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4452_call = mod.get_global_var('func_4452')
func_4454_call = mutated_mod.get_global_var('func_4454')
call_5497 = func_4452_call()
call_5498 = func_4452_call()
var_5506 = relay.var("var_5506", dtype = "float64", shape = (13, 4, 11))#candidate|5506|(13, 4, 11)|var|float64
bop_5507 = relay.logical_xor(call_5497.astype('int32'), var_5506.astype('int32')) # shape=(13, 4, 11)
bop_5510 = relay.logical_xor(call_5498.astype('int32'), var_5506.astype('int32')) # shape=(13, 4, 11)
func_4821_call = mod.get_global_var('func_4821')
func_4822_call = mutated_mod.get_global_var('func_4822')
call_5511 = func_4821_call()
call_5512 = func_4821_call()
output = relay.Tuple([bop_5507,call_5511,])
output2 = relay.Tuple([bop_5510,call_5512,])
func_5517 = relay.Function([var_5506,], output)
mod['func_5517'] = func_5517
mod = relay.transform.InferType()(mod)
var_5518 = relay.var("var_5518", dtype = "float64", shape = (13, 4, 11))#candidate|5518|(13, 4, 11)|var|float64
output = func_5517(var_5518)
func_5519 = relay.Function([var_5518], output)
mutated_mod['func_5519'] = func_5519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4684_call = mod.get_global_var('func_4684')
func_4685_call = mutated_mod.get_global_var('func_4685')
call_5542 = relay.TupleGetItem(func_4684_call(), 0)
call_5543 = relay.TupleGetItem(func_4685_call(), 0)
func_3820_call = mod.get_global_var('func_3820')
func_3826_call = mutated_mod.get_global_var('func_3826')
const_5546 = relay.const(8, dtype = "uint32")#candidate|5546|()|const|uint32
var_5547 = relay.var("var_5547", dtype = "int32", shape = (1, 30))#candidate|5547|(1, 30)|var|int32
var_5548 = relay.var("var_5548", dtype = "float64", shape = (300,))#candidate|5548|(300,)|var|float64
const_5549 = relay.const([9.447336,-0.658208,7.686312,-7.951968,5.087893,7.292980,-9.479840,-1.376059,-4.575929,-9.176159,1.336839,-9.973825,-1.391340,-1.756687,-5.470327,-2.746025,8.927134,3.573213,-2.472273,5.166560,9.278747,-0.804707,-1.505459,2.639842,-7.155953,-9.646143,7.910783,3.414902,-5.381106,8.271939,5.809214,-1.584994,4.998643,3.914054,7.106538,6.650597,8.664207,-1.820175,-3.987072,-8.062204,-4.589151,6.610396,-1.945791,1.769846,-4.100619,3.474123,-4.657716,-7.245216,8.967406,0.447007,-1.295837,2.623089,3.744318,1.491094,0.844572,-6.401994,-6.633595,-3.531262,-8.183532,1.500119,-9.428447,-1.312348,-2.372490,-7.944423,0.367047,3.828523,-2.574969,4.748185,-9.320545,-7.206983,6.793419,0.045567,-8.713349,-3.607294,4.193567,1.900431,-2.635744,2.391503,-1.954912,-5.141745,6.939231,9.942172,-1.663670,3.368124,0.225725,-2.524842,-4.777377,2.710252,3.231091,-7.795420,5.751798,6.746964,6.243631,9.638208,-7.549483,0.981571,0.200630,-2.147663,-8.404712,-8.513016,4.760072,-9.203000,9.975124,-9.690162,6.778276,0.933009,-3.980103,-3.437645,6.836276,8.968790,1.035968,-3.206753,3.176230,-4.364212,-3.143561,0.708060,3.189022,-3.242559,2.533411,-0.518356,4.845909,-4.311747,-7.231558,1.187963,-3.857219,1.845848,-4.970642,-7.788187,-0.115547,1.841303,7.082989,-7.925586,-8.055155,6.857344,3.414608,-1.717485,-8.727172,-3.027745,7.296757,-4.107800,-0.782332,2.340216,6.668932,-3.011756,-3.924483,0.988315,0.438116,-9.390808,-3.780631,8.414774,0.427704,-2.945436,-0.129983,-2.751363,-3.125084,4.423193,4.714609,8.619861,-5.575951,-7.220355,5.927765,6.064655,-3.109733,-9.209127,7.634820,-2.003384,5.810983,-4.025159,-6.739320,8.618669,-3.440510,3.363153,2.378265,-9.577829,6.549248,-7.969503,-8.836886,3.946854,-9.182807,9.310467,3.190844,-6.682853,-1.726893,3.046177,-5.686685,-1.703569,8.598000,-1.406098,-9.676670,1.207217,0.609402,5.797688,7.940845,-5.742152,-5.014184,7.621217,-7.120959,8.513918,3.451160,8.882538,6.474232,-6.762749,6.794184,-9.451314,8.068872,5.885165,0.483259,8.794329,7.148514,-0.306350,8.617265,-1.118310,-8.454255,3.589116,-3.239118,2.666979,-7.023148,-5.379625,-1.789091,1.753166,-9.097846,-5.877483,4.493531,-4.784740,-0.336063,1.059885,3.137537,9.633998,1.521170,1.092035,9.366733,8.257835,-8.005657,6.773063,-4.800621,-0.986256,-0.798835,6.904833,-8.911468,-5.636884,-1.317349,8.752528,8.779311,0.090457,7.916134,-0.973109,3.485221,-8.373846,-6.107578,-0.338717,-2.241148,5.504314,-1.448643,8.740310,2.990391,6.996828,3.994452,8.496135,6.120680,1.502362,2.828707,2.522557,6.473898,-6.398448,8.444591,3.540477,7.188943,-2.764768,0.493095,7.017797,-4.416858,-4.290608,1.432650,-4.602074,4.754166,2.282265,-1.497620,4.764496,-6.355296,1.729244,2.931292,6.163707,6.684820,-4.902484,5.850120,5.433279,-6.953498,4.085953,0.704136,-6.356702,3.429698,9.231919,-5.767697,-5.892916,-0.904430,-0.733862,-2.886282,4.080808,-0.898532,-9.220935,9.266897,2.017283,2.386608,0.497206,-1.640402,9.773846,3.835683,2.836634,-9.810565,-2.644313,7.245997,-2.410836,-2.909044,-7.562767,9.553548,3.243371,-5.754653,-6.402848,9.913932,6.230779], dtype = "float64")#candidate|5549|(320,)|const|float64
call_5545 = relay.TupleGetItem(func_3820_call(relay.reshape(const_5546.astype('uint32'), []), relay.reshape(var_5547.astype('int32'), [5, 6]), relay.reshape(var_5548.astype('float64'), [150, 2]), relay.reshape(const_5549.astype('float64'), [320,]), ), 0)
call_5550 = relay.TupleGetItem(func_3826_call(relay.reshape(const_5546.astype('uint32'), []), relay.reshape(var_5547.astype('int32'), [5, 6]), relay.reshape(var_5548.astype('float64'), [150, 2]), relay.reshape(const_5549.astype('float64'), [320,]), ), 0)
func_4426_call = mod.get_global_var('func_4426')
func_4428_call = mutated_mod.get_global_var('func_4428')
call_5554 = relay.TupleGetItem(func_4426_call(), 0)
call_5555 = relay.TupleGetItem(func_4428_call(), 0)
output = relay.Tuple([call_5542,call_5545,const_5546,var_5547,var_5548,const_5549,call_5554,])
output2 = relay.Tuple([call_5543,call_5550,const_5546,var_5547,var_5548,const_5549,call_5555,])
func_5576 = relay.Function([var_5547,var_5548,], output)
mod['func_5576'] = func_5576
mod = relay.transform.InferType()(mod)
mutated_mod['func_5576'] = func_5576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5576_call = mutated_mod.get_global_var('func_5576')
var_5578 = relay.var("var_5578", dtype = "int32", shape = (1, 30))#candidate|5578|(1, 30)|var|int32
var_5579 = relay.var("var_5579", dtype = "float64", shape = (300,))#candidate|5579|(300,)|var|float64
call_5577 = func_5576_call(var_5578,var_5579,)
output = call_5577
func_5580 = relay.Function([var_5578,var_5579,], output)
mutated_mod['func_5580'] = func_5580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4073_call = mod.get_global_var('func_4073')
func_4075_call = mutated_mod.get_global_var('func_4075')
call_5628 = func_4073_call()
call_5629 = func_4073_call()
output = relay.Tuple([call_5628,])
output2 = relay.Tuple([call_5629,])
func_5639 = relay.Function([], output)
mod['func_5639'] = func_5639
mod = relay.transform.InferType()(mod)
output = func_5639()
func_5640 = relay.Function([], output)
mutated_mod['func_5640'] = func_5640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5395_call = mod.get_global_var('func_5395')
func_5396_call = mutated_mod.get_global_var('func_5396')
call_5674 = relay.TupleGetItem(func_5395_call(), 1)
call_5675 = relay.TupleGetItem(func_5396_call(), 1)
output = relay.Tuple([call_5674,])
output2 = relay.Tuple([call_5675,])
func_5691 = relay.Function([], output)
mod['func_5691'] = func_5691
mod = relay.transform.InferType()(mod)
output = func_5691()
func_5692 = relay.Function([], output)
mutated_mod['func_5692'] = func_5692
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5695 = relay.var("var_5695", dtype = "float64", shape = (11, 14, 3))#candidate|5695|(11, 14, 3)|var|float64
var_5696 = relay.var("var_5696", dtype = "float64", shape = (11, 14, 3))#candidate|5696|(11, 14, 3)|var|float64
bop_5697 = relay.multiply(var_5695.astype('float64'), relay.reshape(var_5696.astype('float64'), relay.shape_of(var_5695))) # shape=(11, 14, 3)
var_5712 = relay.var("var_5712", dtype = "float64", shape = (11, 14, 3))#candidate|5712|(11, 14, 3)|var|float64
bop_5713 = relay.right_shift(var_5695.astype('int32'), relay.reshape(var_5712.astype('int32'), relay.shape_of(var_5695))) # shape=(11, 14, 3)
uop_5718 = relay.sigmoid(var_5712.astype('float64')) # shape=(11, 14, 3)
output = relay.Tuple([bop_5697,bop_5713,uop_5718,])
output2 = relay.Tuple([bop_5697,bop_5713,uop_5718,])
func_5731 = relay.Function([var_5695,var_5696,var_5712,], output)
mod['func_5731'] = func_5731
mod = relay.transform.InferType()(mod)
var_5732 = relay.var("var_5732", dtype = "float64", shape = (11, 14, 3))#candidate|5732|(11, 14, 3)|var|float64
var_5733 = relay.var("var_5733", dtype = "float64", shape = (11, 14, 3))#candidate|5733|(11, 14, 3)|var|float64
var_5734 = relay.var("var_5734", dtype = "float64", shape = (11, 14, 3))#candidate|5734|(11, 14, 3)|var|float64
output = func_5731(var_5732,var_5733,var_5734,)
func_5735 = relay.Function([var_5732,var_5733,var_5734,], output)
mutated_mod['func_5735'] = func_5735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5639_call = mod.get_global_var('func_5639')
func_5640_call = mutated_mod.get_global_var('func_5640')
call_5747 = relay.TupleGetItem(func_5639_call(), 0)
call_5748 = relay.TupleGetItem(func_5640_call(), 0)
func_819_call = mod.get_global_var('func_819')
func_821_call = mutated_mod.get_global_var('func_821')
var_5785 = relay.var("var_5785", dtype = "float64", shape = (1, 1456))#candidate|5785|(1, 1456)|var|float64
call_5784 = func_819_call(relay.reshape(var_5785.astype('float64'), [14, 8, 13]))
call_5786 = func_819_call(relay.reshape(var_5785.astype('float64'), [14, 8, 13]))
func_1273_call = mod.get_global_var('func_1273')
func_1277_call = mutated_mod.get_global_var('func_1277')
const_5788 = relay.const([-6,-4,-5,3,8,8,6,8,9,-1,4,2,-8,-3,9,2,-4,8,-1,-5,-8,-2,-3,10,-6,3,-4,6,-10,-4,-2,8,1,5,-8,-10,-1,9,-7,-6,-1,-3,-3,-6,7,-4,4,-4,8,8,-8,-2,-3,3,-1,2,-7,6,3,5,-2,10,-2,3,-2,8,9,8,-3,1,1,8,8,10,-6,1,5,-3,4,9,-7,7,-8,-8,-8,-5,-2,-7,-6,10,-3,9,-4,4,-8,-5,9,1,-7,-8,-5,5,7,8,10,-7,-10,-10,-1,-2,7,-4,-1,4,1,4,5,5,-1,5,-10,-6,-9,5,-9,8,6,2,4,-5,6,-3,9,2,1,-3,10,-1,6,-10,1,-10,-8,4,8,9,7,6,-9,7,-6,1,10,4,6,-10,1,-5,4,-5,9,8,-7,3,1,-8,-10,2,10,5,-1,4,7,-3,9,3,1,3,4,-3,-5,1,-7,5,-8,-3,7,10,-7,5,10,-3,9,-6,1,7,10,9,-10,7,5,8,-9,6,-3,1,6,4,-7,8,2,4,-5,1,7,7,10,-6,8,-5,2,2,-8,-5,7,-5,-1,10,1,-5,-1,-4,10,2,-1,-8,-2,1,9,7,9,6,2,-10,-9,-3,9,-3,-7,-8,-1,3,7,3,10,-3,-3,-3,-4,8,-7,-4,-10,7,4,-10,-10,-6,7,-4,-9,-7,3,-7,-10,10,8,6,-3,-9,-6,1,2,-4,7,5,6,-8,2,6,10,1,-2,-8,-8,3,6,2,9,6,-6,2,2,1,-5,6,-4,1,-4,2,-6,5,-7,1,-5,-4,9,-4,-5,-7,-3,4,-9,-3,6,4,10,-5,8,-3,-4,-3,2,-5,2,9,-4,3,2,8,-3,1,4,8,-3,-5,9,-3,5,10,-10,3,4,1,3,-1,4,8,9,1,9,2,-4,-9,-2,8,-7,-8,-8,4,-10,6,8,-3,-9,10,10,6,-6,-7,-3,2,6,9,-1,-5,-10,5,4,7,-4,-3,-3,-10,-3,7,2,6,-9,3,-1,-1,9,1,5,9,8,-4,3,8,-3,-4,6,6,-6,-7,9,-8,-5,-4,-8,10,6,-5,-1,5,-9,10,8,5,7,10,2,-4,6,9,-2,-10,-4,9,7,1,4,5,9,5,2,4,5,2,8,7,-10,-10,1,2,-3,6,-6,9,-9,-3,-2,-6,7,-10,9,6,-6,6,6,-5,-2,-6,2,-4,-2,3,-6,-2,-6,7,-2,5,-9,-5,-10,4,1,-10], dtype = "uint64")#candidate|5788|(490,)|const|uint64
call_5787 = relay.TupleGetItem(func_1273_call(relay.reshape(const_5788.astype('uint64'), [14, 5, 7]), relay.reshape(const_5788.astype('float32'), [14, 5, 7]), ), 1)
call_5789 = relay.TupleGetItem(func_1277_call(relay.reshape(const_5788.astype('uint64'), [14, 5, 7]), relay.reshape(const_5788.astype('float32'), [14, 5, 7]), ), 1)
func_2980_call = mod.get_global_var('func_2980')
func_2982_call = mutated_mod.get_global_var('func_2982')
call_5811 = func_2980_call()
call_5812 = func_2980_call()
output = relay.Tuple([call_5747,call_5784,var_5785,call_5787,const_5788,call_5811,])
output2 = relay.Tuple([call_5748,call_5786,var_5785,call_5789,const_5788,call_5812,])
func_5818 = relay.Function([var_5785,], output)
mod['func_5818'] = func_5818
mod = relay.transform.InferType()(mod)
mutated_mod['func_5818'] = func_5818
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5819 = relay.var("var_5819", dtype = "float64", shape = (1, 1456))#candidate|5819|(1, 1456)|var|float64
func_5818_call = mutated_mod.get_global_var('func_5818')
call_5820 = func_5818_call(var_5819)
output = call_5820
func_5821 = relay.Function([var_5819], output)
mutated_mod['func_5821'] = func_5821
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5840 = relay.const([[[5,3,7,1,4,-4,-4],[10,6,7,7,-4,-7,-5],[2,1,9,9,7,-5,-2],[10,1,-7,9,-8,-1,5],[9,-3,9,-8,-7,4,9],[-5,-8,8,-6,-8,-9,9],[1,8,-3,-2,-6,-1,-7]],[[8,-6,-8,9,-4,3,8],[-10,-3,-1,2,-3,-8,-7],[1,6,2,2,6,8,-6],[4,2,-3,5,-8,-7,3],[8,-4,6,8,-4,5,-4],[2,5,-6,-9,4,2,-3],[10,6,-8,7,-2,9,7]],[[-6,9,1,-3,1,-5,-8],[-4,7,8,4,-4,7,7],[-2,2,-5,5,4,-2,-1],[-1,-5,-9,1,-8,1,-5],[7,-6,6,6,-10,-9,8],[1,-10,8,9,2,5,4],[-1,8,-1,-9,-2,-2,4]],[[9,3,-1,4,2,7,3],[3,9,8,-4,-10,8,5],[-6,-1,3,7,-9,-1,6],[5,9,-9,-2,4,6,6],[-9,5,-4,-10,-2,-8,10],[4,-9,-5,6,9,-1,-1],[-8,-2,-10,2,-5,10,3]],[[-8,1,-9,10,-1,8,-2],[2,5,-2,8,-3,-7,-7],[6,7,3,6,8,-5,-2],[-8,1,2,1,2,8,-2],[-6,6,-8,-5,-2,-2,9],[-1,2,9,-1,-1,5,-2],[3,-1,-2,10,-1,1,-8]],[[-4,-2,-1,-4,10,-1,6],[6,-2,3,-7,-2,4,-4],[5,-10,10,-3,6,3,-1],[-9,-2,-6,-6,-10,3,-2],[5,2,7,-10,1,9,-1],[7,9,-10,3,-7,-4,-3],[-1,3,-10,-10,6,3,-3]],[[7,5,5,-10,-6,10,3],[2,-4,3,-3,-2,-8,-2],[8,-5,7,-10,5,9,4],[-5,-7,5,4,-7,-8,7],[-9,-9,4,3,6,-6,-5],[2,-6,10,-6,3,2,-4],[-2,10,-1,10,3,-9,-7]],[[9,1,3,8,9,8,-3],[-3,-3,-1,-6,-2,-8,-10],[-5,3,10,7,9,7,-1],[-1,7,3,-1,-5,-7,-3],[-5,3,9,5,-7,-5,8],[-8,8,3,-7,9,1,3],[2,-2,-9,6,10,-1,4]],[[7,9,2,7,5,4,-10],[-8,2,10,-5,-10,1,4],[8,8,-1,3,4,-1,-3],[-3,-7,-9,10,-4,2,-8],[5,-5,-10,-10,-1,6,-2],[6,-1,2,1,8,1,-6],[7,6,-6,7,-5,8,-10]],[[1,3,-9,8,2,-3,1],[-4,8,1,-5,4,-2,9],[-5,4,10,5,10,1,1],[4,-9,-8,-4,-1,-5,-1],[6,-7,-10,8,8,1,5],[2,7,9,-8,1,6,-9],[6,8,-1,-4,-5,10,6]],[[-3,-3,-8,-3,-6,-5,-1],[10,-4,1,10,-8,-4,7],[-8,7,-5,-6,-3,-1,10],[-8,5,-2,-6,-2,8,1],[2,-5,-10,-10,5,9,7],[-6,3,9,-4,8,5,-4],[-7,2,-2,10,3,8,-7]],[[5,6,10,-9,-7,9,1],[-5,-6,2,4,9,8,5],[10,-5,-6,8,8,5,10],[-3,10,8,4,4,-3,-3],[4,9,8,9,-2,-9,6],[-8,-10,5,-10,-3,-2,2],[1,8,-1,-9,10,-2,7]],[[-5,-7,-7,-3,-4,7,7],[6,9,-3,3,6,3,-2],[-2,-8,9,-9,2,-3,7],[6,1,1,9,9,-8,-4],[2,-7,2,-1,-3,-1,4],[-1,-4,-3,9,7,8,10],[2,4,-9,-8,6,-3,-2]],[[4,-10,5,4,-1,1,-10],[5,-2,3,10,-7,-2,10],[4,2,7,2,6,-1,-8],[-6,-1,10,7,-1,5,7],[-3,-5,-10,4,8,9,-2],[2,3,2,-6,-7,-6,-10],[-6,-10,-4,3,-1,1,-3]]], dtype = "uint8")#candidate|5840|(14, 7, 7)|const|uint8
const_5841 = relay.const([[[6,-7,3,10,1,-2,8],[3,6,-9,-4,-8,-5,9],[-10,9,10,-2,10,-8,3],[-3,-9,3,4,10,4,-6],[-4,4,5,-9,9,-5,5],[-7,-3,-1,7,-10,5,10],[9,10,-3,7,-6,-1,8]],[[-4,-1,-1,-3,1,-8,10],[2,-3,-8,-4,7,-8,-8],[10,7,10,8,4,-6,1],[5,-7,3,-8,5,1,3],[-7,-8,-10,-2,3,-2,1],[-2,-3,-4,-4,10,-8,-3],[-7,6,-1,2,9,2,5]],[[-1,-5,9,-7,-6,-9,-2],[3,6,6,-3,-8,8,10],[1,5,2,-2,8,5,2],[-2,3,-4,3,-2,-6,-5],[8,-6,1,-3,-3,-5,6],[-5,-5,3,-10,6,-6,2],[-9,-8,-2,-7,10,-7,5]],[[-4,-3,-7,5,8,-8,1],[-3,6,1,8,-10,8,5],[3,-1,-10,7,5,-9,7],[9,9,-2,3,-1,-7,-8],[-3,2,2,2,-8,-9,-10],[7,-6,-5,8,2,-1,4],[5,4,-4,1,-10,10,-3]],[[2,-7,-1,5,8,5,7],[-2,-3,3,-3,4,5,-9],[3,-3,-7,3,-3,-6,-4],[-10,9,1,7,1,-3,5],[8,-4,-10,-5,-7,-7,-9],[-1,5,5,1,6,-2,-1],[-2,4,2,3,4,9,6]],[[-4,-8,-1,6,9,-4,7],[-1,-2,5,-5,5,-9,5],[2,3,-8,1,-5,7,-6],[8,6,4,-4,-5,7,8],[9,-5,5,-7,10,4,6],[-9,2,-8,9,-8,2,-4],[3,7,3,3,8,3,-9]],[[-3,-8,-9,-2,-1,-10,5],[-2,3,1,5,9,-4,-7],[7,7,1,6,6,-7,-10],[5,9,6,-3,1,3,-8],[-9,5,3,7,7,-3,3],[1,-9,9,-4,-1,2,-4],[1,1,7,5,-7,-3,8]],[[-1,-8,-2,-1,-6,-6,1],[-6,-10,-9,7,8,-7,8],[1,-7,-7,-5,3,-2,10],[-5,-5,-9,10,-7,-5,2],[-9,-1,-6,-3,5,-2,5],[-9,-1,9,5,-2,-6,-5],[5,1,8,6,-2,5,-10]],[[-6,-8,-1,9,-6,8,1],[-8,-4,-4,8,-7,-3,7],[6,4,2,9,2,5,-4],[5,-8,-2,7,5,7,2],[-3,-10,6,-3,6,2,-1],[8,-2,1,-8,-2,2,-2],[1,8,3,-5,2,7,-3]],[[9,-8,9,10,1,6,4],[-1,6,-2,-8,-2,6,-2],[-3,-4,8,9,-3,9,8],[-7,1,1,-10,4,8,2],[2,-6,8,7,-1,3,-5],[10,-8,-8,-5,-8,9,-4],[8,2,-9,-4,8,2,10]],[[-5,-8,10,2,-4,-6,1],[-2,4,-8,-1,9,-3,-9],[-8,8,5,8,9,3,4],[-6,7,-9,-2,-9,3,8],[-5,-1,-5,-8,-7,8,-6],[-1,-2,-7,-7,-10,-5,-1],[9,6,-4,8,-8,-4,3]],[[-2,4,-3,-10,-7,-9,7],[-8,-4,-8,2,9,-3,-6],[-3,10,-10,-9,-3,7,8],[-9,-2,3,-3,-8,5,4],[-6,5,-9,-5,9,6,-2],[4,-9,-7,9,8,-3,8],[8,5,2,5,7,4,5]],[[10,5,9,6,-6,8,-8],[4,8,-9,6,-5,7,-3],[7,-3,7,-2,1,-2,2],[4,-2,5,-8,3,8,-7],[9,5,9,-5,-5,3,-3],[-6,-7,-5,9,-1,6,3],[3,8,1,7,3,-6,-7]],[[8,-4,-4,-5,1,3,-2],[-5,5,-8,-7,-8,1,-6],[-2,4,2,-4,-10,-9,4],[-1,3,5,4,-10,-2,-7],[10,8,8,-1,1,-9,6],[-9,2,-9,10,10,5,6],[8,10,9,-9,-1,7,6]]], dtype = "uint8")#candidate|5841|(14, 7, 7)|const|uint8
bop_5842 = relay.bitwise_or(const_5840.astype('uint8'), relay.reshape(const_5841.astype('uint8'), relay.shape_of(const_5840))) # shape=(14, 7, 7)
output = relay.Tuple([bop_5842,])
output2 = relay.Tuple([bop_5842,])
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
func_5639_call = mod.get_global_var('func_5639')
func_5640_call = mutated_mod.get_global_var('func_5640')
call_5864 = relay.TupleGetItem(func_5639_call(), 0)
call_5865 = relay.TupleGetItem(func_5640_call(), 0)
func_1433_call = mod.get_global_var('func_1433')
func_1438_call = mutated_mod.get_global_var('func_1438')
var_5867 = relay.var("var_5867", dtype = "float64", shape = (728, 2))#candidate|5867|(728, 2)|var|float64
const_5868 = relay.const([-8,9,-2,-2,5,-9,-1,-4,3,8,-9,7,10,8,-6,7,6,5,-8,-6,-4,-5,2,-8,3,-6,2,4,-3,-7,9,-6,-9,-4,-8,9,-7,-7,-6,-3,2,1,5,6,-10,-9,-5,6,6,3,2,7,10,8,10,5,3,6,3,-5,4,-4,1,-7,1,2,-3,1,-5,-7,2,-9,-8,-2,8,6,3,3,1,10,9,3,5,3,-7,-6,-4,4,1,-5,-3,-1,2,-10,-3,2,6,-3,-3,2,-1,-9,-5,-7,8,3,2,10,9,6,4,-5,-7,-1,7,10,-4,-2,-1,3,-10,5,-2,7,-6,-5,-3,3,7,10,-9,-3,-1,-10,-4,4,-3,8,-5,-9,10,-5,2,-4,-10,-4,-7,2,2,10,6,1,-6,-7,4,4,-7,8,7,-10,-6,-7,-3,-1,-10,-2,7,-8,-2,4,10,-3,-8,-6,-3,-1,-3,4,-7,3,-7,6,10,-9,-10,2,2,6,-4,-5,3,6,6,3,6,-1,-3,-9,2,9,10,3,-5,-3,5,6,6,3,-3,-3,4,-1,10,2,-7,-5,10,-8,7,4,9,-8,-5,7,7,6,-6,8,9,8,-1,-3,-9,8,10,7,-3,6,-6,-5,-5,-6,-1,4,6,-6,-7,10,7,1,1,9,-5,-1,8,-5,8,-1,-6,9,-1,1,-3,3,10,-1,3,4,-7,-8,2,7,5,-10,-6,-4,-3,2,-5,-8,-10,7,-1,1,7,-2,-3,10,-8,10,9,-1,-1,8,10,3,7,5,-1,5,-6,-7,-5,-8,7,-6,-3,9,-10,2,-7,9,-2,-3,1,-9,6,-7,-6,3,-6,-10,-6,5,-9,5,9,-9,10,-4,-1,-9,2,7,2,1,-9,-9,1,-10,-10,-6,2,-9,-7,-3,-7,-5,-6,-5,2,-8,-9,7,-8,10,-3,6,2,-6,-10,9,-1,8,-5,-8,1,8,-3,-9,4,-1,-8,2,4,-10,9,4,4,-9,-5,7,-3,5,2,6,-7,-2,-4,4,-4,-4,6,3,10,-10,-9,10,-2,9,-10,9,-4,2,-5,7,5,-4,-7,-10,1,1,-6,3,7,3,8,7,-3,9,-7,9,6,-2,10,-2,-1,2,-4,-5,-6,-2,-10,-4,8,-3,10,5,-7,8,9,10,-3,-7,-7,1,9,-8,10,4,-7,-3,8,2,-6,-5,-2,-5,7,-5,-2,-8,10,2,9,-8,-2,3,10,7,8,1,7,5,5,6,6,10,9,-6,9,-7,6,5,5,-1,4,-1,5,-4,-7,10,4,7,-4,-6,-6,6,-10,5,-2,8,-6,8,-6,4,3,-7,3,-4,7,-2,10,-3,10,8,6,-10,7,-6,10,-6,-3,2,7], dtype = "int64")#candidate|5868|(525,)|const|int64
const_5869 = relay.const(-3, dtype = "uint32")#candidate|5869|()|const|uint32
call_5866 = relay.TupleGetItem(func_1433_call(relay.reshape(var_5867.astype('float64'), [1456,]), relay.reshape(const_5868.astype('int64'), [525, 1]), relay.reshape(const_5869.astype('uint32'), []), ), 3)
call_5870 = relay.TupleGetItem(func_1438_call(relay.reshape(var_5867.astype('float64'), [1456,]), relay.reshape(const_5868.astype('int64'), [525, 1]), relay.reshape(const_5869.astype('uint32'), []), ), 3)
uop_5877 = relay.sigmoid(var_5867.astype('float64')) # shape=(728, 2)
uop_5880 = relay.sqrt(uop_5877.astype('float64')) # shape=(728, 2)
output = relay.Tuple([call_5864,call_5866,const_5868,const_5869,uop_5880,])
output2 = relay.Tuple([call_5865,call_5870,const_5868,const_5869,uop_5880,])
func_5882 = relay.Function([var_5867,], output)
mod['func_5882'] = func_5882
mod = relay.transform.InferType()(mod)
mutated_mod['func_5882'] = func_5882
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5883 = relay.var("var_5883", dtype = "float64", shape = (728, 2))#candidate|5883|(728, 2)|var|float64
func_5882_call = mutated_mod.get_global_var('func_5882')
call_5884 = func_5882_call(var_5883)
output = call_5884
func_5885 = relay.Function([var_5883], output)
mutated_mod['func_5885'] = func_5885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4841_call = mod.get_global_var('func_4841')
func_4842_call = mutated_mod.get_global_var('func_4842')
call_5897 = relay.TupleGetItem(func_4841_call(), 0)
call_5898 = relay.TupleGetItem(func_4842_call(), 0)
output = relay.Tuple([call_5897,])
output2 = relay.Tuple([call_5898,])
func_5900 = relay.Function([], output)
mod['func_5900'] = func_5900
mod = relay.transform.InferType()(mod)
output = func_5900()
func_5901 = relay.Function([], output)
mutated_mod['func_5901'] = func_5901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4397_call = mod.get_global_var('func_4397')
func_4398_call = mutated_mod.get_global_var('func_4398')
call_6042 = func_4397_call()
call_6043 = func_4397_call()
func_2601_call = mod.get_global_var('func_2601')
func_2603_call = mutated_mod.get_global_var('func_2603')
const_6051 = relay.const([-6.902832,-3.117130,8.642460,3.418562,4.115304,6.508044,-5.267876,1.046772,7.433714,-9.356726,1.701274,7.820975,-8.396694,8.962727,-4.374357,1.391797,-7.415193,-8.064490,-9.786132,7.142285,6.874630,5.468420,-3.231218,7.143004,-8.826679,-1.846942,0.136540,-7.967312,-1.629233,8.127615,-1.350842,-4.785526,-8.138212,-5.178010,-5.488058,4.989600,-8.497723,-9.668521,8.724497,8.690982,9.020688,4.847212,6.312766,-4.689521,5.858740,-6.044321,-9.504493,-1.871563], dtype = "float32")#candidate|6051|(48,)|const|float32
call_6050 = relay.TupleGetItem(func_2601_call(relay.reshape(const_6051.astype('float32'), [4, 4, 3])), 2)
call_6052 = relay.TupleGetItem(func_2603_call(relay.reshape(const_6051.astype('float32'), [4, 4, 3])), 2)
output = relay.Tuple([call_6042,call_6050,const_6051,])
output2 = relay.Tuple([call_6043,call_6052,const_6051,])
func_6059 = relay.Function([], output)
mod['func_6059'] = func_6059
mod = relay.transform.InferType()(mod)
output = func_6059()
func_6060 = relay.Function([], output)
mutated_mod['func_6060'] = func_6060
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3158_call = mod.get_global_var('func_3158')
func_3160_call = mutated_mod.get_global_var('func_3160')
call_6066 = relay.TupleGetItem(func_3158_call(), 0)
call_6067 = relay.TupleGetItem(func_3160_call(), 0)
const_6080 = relay.const([[[-3,1,5,-4,6,2,3],[6,-8,4,-6,7,9,7],[3,9,6,6,6,2,-6]],[[-8,8,2,9,-7,8,-6],[-9,4,-1,-8,3,-8,-3],[-2,7,-7,-4,-10,-7,-9]],[[-10,2,9,3,-9,9,-6],[2,9,10,6,2,8,-4],[-8,-10,7,2,-7,8,-8]],[[9,-5,-5,9,-2,-3,-4],[6,-6,2,-7,-7,6,3],[-10,-10,5,2,-10,3,5]],[[-8,-9,-8,1,2,-8,6],[-10,8,8,-1,-5,-10,3],[9,-3,8,1,6,3,-9]],[[-6,-4,4,6,-2,-4,1],[2,-1,-3,-7,-6,-4,-10],[2,-7,4,5,-3,-9,-10]],[[-2,9,5,4,-4,-7,-7],[3,-10,-7,-3,8,9,1],[-8,3,1,1,-1,4,-6]]], dtype = "uint32")#candidate|6080|(7, 3, 7)|const|uint32
bop_6081 = relay.less_equal(call_6066.astype('bool'), relay.reshape(const_6080.astype('bool'), relay.shape_of(call_6066))) # shape=(7, 3, 7)
bop_6084 = relay.less_equal(call_6067.astype('bool'), relay.reshape(const_6080.astype('bool'), relay.shape_of(call_6067))) # shape=(7, 3, 7)
output = bop_6081
output2 = bop_6084
func_6117 = relay.Function([], output)
mod['func_6117'] = func_6117
mod = relay.transform.InferType()(mod)
output = func_6117()
func_6118 = relay.Function([], output)
mutated_mod['func_6118'] = func_6118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4198_call = mod.get_global_var('func_4198')
func_4199_call = mutated_mod.get_global_var('func_4199')
call_6127 = relay.TupleGetItem(func_4198_call(), 0)
call_6128 = relay.TupleGetItem(func_4199_call(), 0)
output = relay.Tuple([call_6127,])
output2 = relay.Tuple([call_6128,])
func_6148 = relay.Function([], output)
mod['func_6148'] = func_6148
mod = relay.transform.InferType()(mod)
mutated_mod['func_6148'] = func_6148
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6148_call = mutated_mod.get_global_var('func_6148')
call_6149 = func_6148_call()
output = call_6149
func_6150 = relay.Function([], output)
mutated_mod['func_6150'] = func_6150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5845_call = mod.get_global_var('func_5845')
func_5847_call = mutated_mod.get_global_var('func_5847')
call_6176 = relay.TupleGetItem(func_5845_call(), 0)
call_6177 = relay.TupleGetItem(func_5847_call(), 0)
output = relay.Tuple([call_6176,])
output2 = relay.Tuple([call_6177,])
func_6186 = relay.Function([], output)
mod['func_6186'] = func_6186
mod = relay.transform.InferType()(mod)
mutated_mod['func_6186'] = func_6186
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6186_call = mutated_mod.get_global_var('func_6186')
call_6187 = func_6186_call()
output = call_6187
func_6188 = relay.Function([], output)
mutated_mod['func_6188'] = func_6188
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6223 = relay.var("var_6223", dtype = "int8", shape = (13, 9, 16))#candidate|6223|(13, 9, 16)|var|int8
var_6224 = relay.var("var_6224", dtype = "int8", shape = (13, 9, 16))#candidate|6224|(13, 9, 16)|var|int8
bop_6225 = relay.equal(var_6223.astype('bool'), relay.reshape(var_6224.astype('bool'), relay.shape_of(var_6223))) # shape=(13, 9, 16)
output = relay.Tuple([bop_6225,])
output2 = relay.Tuple([bop_6225,])
func_6228 = relay.Function([var_6223,var_6224,], output)
mod['func_6228'] = func_6228
mod = relay.transform.InferType()(mod)
var_6229 = relay.var("var_6229", dtype = "int8", shape = (13, 9, 16))#candidate|6229|(13, 9, 16)|var|int8
var_6230 = relay.var("var_6230", dtype = "int8", shape = (13, 9, 16))#candidate|6230|(13, 9, 16)|var|int8
output = func_6228(var_6229,var_6230,)
func_6231 = relay.Function([var_6229,var_6230,], output)
mutated_mod['func_6231'] = func_6231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4950_call = mod.get_global_var('func_4950')
func_4952_call = mutated_mod.get_global_var('func_4952')
call_6241 = relay.TupleGetItem(func_4950_call(), 0)
call_6242 = relay.TupleGetItem(func_4952_call(), 0)
func_5488_call = mod.get_global_var('func_5488')
func_5489_call = mutated_mod.get_global_var('func_5489')
call_6243 = func_5488_call()
call_6244 = func_5488_call()
output = relay.Tuple([call_6241,call_6243,])
output2 = relay.Tuple([call_6242,call_6244,])
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
func_4397_call = mod.get_global_var('func_4397')
func_4398_call = mutated_mod.get_global_var('func_4398')
call_6393 = func_4397_call()
call_6394 = func_4397_call()
func_6228_call = mod.get_global_var('func_6228')
func_6231_call = mutated_mod.get_global_var('func_6231')
var_6396 = relay.var("var_6396", dtype = "int8", shape = (936, 2))#candidate|6396|(936, 2)|var|int8
call_6395 = relay.TupleGetItem(func_6228_call(relay.reshape(var_6396.astype('int8'), [13, 9, 16]), relay.reshape(var_6396.astype('int8'), [13, 9, 16]), ), 0)
call_6397 = relay.TupleGetItem(func_6231_call(relay.reshape(var_6396.astype('int8'), [13, 9, 16]), relay.reshape(var_6396.astype('int8'), [13, 9, 16]), ), 0)
var_6400 = relay.var("var_6400", dtype = "bool", shape = (13, 9, 16))#candidate|6400|(13, 9, 16)|var|bool
bop_6401 = relay.greater_equal(call_6395.astype('bool'), relay.reshape(var_6400.astype('bool'), relay.shape_of(call_6395))) # shape=(13, 9, 16)
bop_6404 = relay.greater_equal(call_6397.astype('bool'), relay.reshape(var_6400.astype('bool'), relay.shape_of(call_6397))) # shape=(13, 9, 16)
func_3820_call = mod.get_global_var('func_3820')
func_3826_call = mutated_mod.get_global_var('func_3826')
var_6410 = relay.var("var_6410", dtype = "uint32", shape = ())#candidate|6410|()|var|uint32
var_6411 = relay.var("var_6411", dtype = "int32", shape = (1, 30))#candidate|6411|(1, 30)|var|int32
var_6412 = relay.var("var_6412", dtype = "float64", shape = (300,))#candidate|6412|(300,)|var|float64
var_6413 = relay.var("var_6413", dtype = "float64", shape = (40, 8))#candidate|6413|(40, 8)|var|float64
call_6409 = relay.TupleGetItem(func_3820_call(relay.reshape(var_6410.astype('uint32'), []), relay.reshape(var_6411.astype('int32'), [5, 6]), relay.reshape(var_6412.astype('float64'), [150, 2]), relay.reshape(var_6413.astype('float64'), [320,]), ), 1)
call_6414 = relay.TupleGetItem(func_3826_call(relay.reshape(var_6410.astype('uint32'), []), relay.reshape(var_6411.astype('int32'), [5, 6]), relay.reshape(var_6412.astype('float64'), [150, 2]), relay.reshape(var_6413.astype('float64'), [320,]), ), 1)
func_2859_call = mod.get_global_var('func_2859')
func_2860_call = mutated_mod.get_global_var('func_2860')
call_6417 = func_2859_call()
call_6418 = func_2859_call()
func_3234_call = mod.get_global_var('func_3234')
func_3237_call = mutated_mod.get_global_var('func_3237')
const_6458 = relay.const([-6.253312,-7.335565,-5.513034,6.231722,8.990222,-2.809249,-7.078757,6.468783,-4.217606,-0.567552,-4.751211,-0.574753,0.209018,-7.331332,-5.308835,3.629508,5.337429,-5.197233,7.746303,9.333276,9.702231,7.164470,-5.141959,-4.935145,9.649314,-4.444633,-4.461913,-3.240817,3.047615,-1.918386,-2.125177,-2.869512,6.702871,8.139314,-1.522812,0.039714,-0.653858,-3.369619,2.860981,5.934752,5.617732,1.645219,8.258772,9.162005,-6.513705,-9.870001,-8.912388,-2.333318,9.141689,-7.979103,-5.669658,-6.108956,-1.421530,-7.044017,9.987713,-9.104219,9.612105,-4.358836,6.342777,-3.599125,1.541814,-7.170633,4.579207,-6.405376,7.107900,1.150862,-8.945576,-9.065679,-3.787812,1.727414,8.235163,-2.109880,8.031469,8.557048,0.404352,-5.760571,-5.935898,-0.764991,3.856700,-8.309904,5.703887,-6.703952,3.107587,-4.865840,6.942593,2.457862,-1.219959,-5.831603,-3.725248,-9.116156,2.635354,7.581307,-1.671339,2.520489,-3.644631,-5.183451,7.650193,8.988628,1.526880,-2.166794,8.812519,5.518191,-8.190015,3.159245,7.752188,-9.937235,-2.558664,-4.452979,3.815877,-8.052156,-6.747462,2.113041,-6.940368,-4.424809,-1.718148,-8.553526,6.622966,3.859639,4.967337,-9.213844,3.636118,9.845710,-4.666302,-5.743230,-2.501827,8.505116,2.067206,-4.109844,-4.566226,4.610186,-8.530767,-4.867834,-7.400938,5.571032,7.112064,-6.337094,-8.063664,-5.374697,-5.610030,-3.630943,-0.847780,6.381066,-5.086333], dtype = "float32")#candidate|6458|(143,)|const|float32
call_6457 = relay.TupleGetItem(func_3234_call(relay.reshape(var_6413.astype('float64'), [320,]), relay.reshape(const_6458.astype('float32'), [143,]), ), 2)
call_6459 = relay.TupleGetItem(func_3237_call(relay.reshape(var_6413.astype('float64'), [320,]), relay.reshape(const_6458.astype('float32'), [143,]), ), 2)
output = relay.Tuple([call_6393,var_6396,bop_6401,call_6409,var_6410,var_6411,var_6412,var_6413,call_6417,call_6457,const_6458,])
output2 = relay.Tuple([call_6394,var_6396,bop_6404,call_6414,var_6410,var_6411,var_6412,var_6413,call_6418,call_6459,const_6458,])
func_6471 = relay.Function([var_6396,var_6400,var_6410,var_6411,var_6412,var_6413,], output)
mod['func_6471'] = func_6471
mod = relay.transform.InferType()(mod)
mutated_mod['func_6471'] = func_6471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6471_call = mutated_mod.get_global_var('func_6471')
var_6473 = relay.var("var_6473", dtype = "int8", shape = (936, 2))#candidate|6473|(936, 2)|var|int8
var_6474 = relay.var("var_6474", dtype = "bool", shape = (13, 9, 16))#candidate|6474|(13, 9, 16)|var|bool
var_6475 = relay.var("var_6475", dtype = "uint32", shape = ())#candidate|6475|()|var|uint32
var_6476 = relay.var("var_6476", dtype = "int32", shape = (1, 30))#candidate|6476|(1, 30)|var|int32
var_6477 = relay.var("var_6477", dtype = "float64", shape = (300,))#candidate|6477|(300,)|var|float64
var_6478 = relay.var("var_6478", dtype = "float64", shape = (40, 8))#candidate|6478|(40, 8)|var|float64
call_6472 = func_6471_call(var_6473,var_6474,var_6475,var_6476,var_6477,var_6478,)
output = call_6472
func_6479 = relay.Function([var_6473,var_6474,var_6475,var_6476,var_6477,var_6478,], output)
mutated_mod['func_6479'] = func_6479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2930_call = mod.get_global_var('func_2930')
func_2931_call = mutated_mod.get_global_var('func_2931')
call_6484 = func_2930_call()
call_6485 = func_2930_call()
func_3615_call = mod.get_global_var('func_3615')
func_3616_call = mutated_mod.get_global_var('func_3616')
call_6513 = relay.TupleGetItem(func_3615_call(), 0)
call_6514 = relay.TupleGetItem(func_3616_call(), 0)
func_5488_call = mod.get_global_var('func_5488')
func_5489_call = mutated_mod.get_global_var('func_5489')
call_6525 = func_5488_call()
call_6526 = func_5488_call()
func_480_call = mod.get_global_var('func_480')
func_484_call = mutated_mod.get_global_var('func_484')
const_6533 = relay.const(-5, dtype = "uint32")#candidate|6533|()|const|uint32
var_6534 = relay.var("var_6534", dtype = "int32", shape = (30,))#candidate|6534|(30,)|var|int32
call_6532 = relay.TupleGetItem(func_480_call(relay.reshape(const_6533.astype('uint32'), []), relay.reshape(var_6534.astype('int32'), [30,]), ), 0)
call_6535 = relay.TupleGetItem(func_484_call(relay.reshape(const_6533.astype('uint32'), []), relay.reshape(var_6534.astype('int32'), [30,]), ), 0)
output = relay.Tuple([call_6484,call_6513,call_6525,call_6532,const_6533,var_6534,])
output2 = relay.Tuple([call_6485,call_6514,call_6526,call_6535,const_6533,var_6534,])
func_6543 = relay.Function([var_6534,], output)
mod['func_6543'] = func_6543
mod = relay.transform.InferType()(mod)
mutated_mod['func_6543'] = func_6543
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6544 = relay.var("var_6544", dtype = "int32", shape = (30,))#candidate|6544|(30,)|var|int32
func_6543_call = mutated_mod.get_global_var('func_6543')
call_6545 = func_6543_call(var_6544)
output = call_6545
func_6546 = relay.Function([var_6544], output)
mutated_mod['func_6546'] = func_6546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4841_call = mod.get_global_var('func_4841')
func_4842_call = mutated_mod.get_global_var('func_4842')
call_6562 = relay.TupleGetItem(func_4841_call(), 0)
call_6563 = relay.TupleGetItem(func_4842_call(), 0)
output = call_6562
output2 = call_6563
func_6615 = relay.Function([], output)
mod['func_6615'] = func_6615
mod = relay.transform.InferType()(mod)
output = func_6615()
func_6616 = relay.Function([], output)
mutated_mod['func_6616'] = func_6616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6245_call = mod.get_global_var('func_6245')
func_6247_call = mutated_mod.get_global_var('func_6247')
call_6635 = relay.TupleGetItem(func_6245_call(), 0)
call_6636 = relay.TupleGetItem(func_6247_call(), 0)
func_3562_call = mod.get_global_var('func_3562')
func_3564_call = mutated_mod.get_global_var('func_3564')
const_6644 = relay.const([5,1,-2,10,5,-2,6,4,3,5,-6,-9,-5,-9,2,2,-9,-1,5,10,-7,-5,-4,-2,5,-5,10,1,2,4,3,3,-10,-1,-4,-2,-5,-3,-8,-6,-4,-5,4,2,7,3,-3,-9,1,-5,-3,7,4,7,-6,-6,-5,-5,-6,-6,-2,-2,-5,7,3,2,-8,5,8,-5,-6,-3,1,-9,-4,1,-6,-2,-6,-9], dtype = "uint8")#candidate|6644|(80,)|const|uint8
call_6643 = relay.TupleGetItem(func_3562_call(relay.reshape(const_6644.astype('uint8'), [8, 2, 5])), 0)
call_6645 = relay.TupleGetItem(func_3564_call(relay.reshape(const_6644.astype('uint8'), [8, 2, 5])), 0)
output = relay.Tuple([call_6635,call_6643,const_6644,])
output2 = relay.Tuple([call_6636,call_6645,const_6644,])
func_6650 = relay.Function([], output)
mod['func_6650'] = func_6650
mod = relay.transform.InferType()(mod)
output = func_6650()
func_6651 = relay.Function([], output)
mutated_mod['func_6651'] = func_6651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3074_call = mod.get_global_var('func_3074')
func_3076_call = mutated_mod.get_global_var('func_3076')
call_6696 = func_3074_call()
call_6697 = func_3074_call()
output = relay.Tuple([call_6696,])
output2 = relay.Tuple([call_6697,])
func_6733 = relay.Function([], output)
mod['func_6733'] = func_6733
mod = relay.transform.InferType()(mod)
mutated_mod['func_6733'] = func_6733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6733_call = mutated_mod.get_global_var('func_6733')
call_6734 = func_6733_call()
output = call_6734
func_6735 = relay.Function([], output)
mutated_mod['func_6735'] = func_6735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5691_call = mod.get_global_var('func_5691')
func_5692_call = mutated_mod.get_global_var('func_5692')
call_6833 = relay.TupleGetItem(func_5691_call(), 0)
call_6834 = relay.TupleGetItem(func_5692_call(), 0)
uop_6837 = relay.log(call_6833.astype('float64')) # shape=(12, 3, 13)
uop_6839 = relay.log(call_6834.astype('float64')) # shape=(12, 3, 13)
func_765_call = mod.get_global_var('func_765')
func_768_call = mutated_mod.get_global_var('func_768')
const_6849 = relay.const([-2,4,-6,-8,-9,2,6,-7,7,5,-4,5,8,-8,-10,9,-5,-6,3,7,8,-6,-7,9,10,8,-5,-3,-6,10,-7,-9,-5,-3,-9,-2,2,-5,2,3,-8,-6,-3,-5,-10,-6,-5,-1,-4,-9,-5,-1,-9,-5,10,3,-10,-10,9,-1,-2,8,-6,8,-3,2,-7,4,1,7,9,3,10,-2,9,-8,4,8,6,9,-2,9,6,-7,5,2,5,-5,9,6,5,-8,-3,-9,4,-8,1,-8,-1,5,1,1,-3,5,-6,-9,-8,-9,7,9,8,-10,7,7,4,-5,9,5,4,3,10,4,1,8,-3,-7,-6,-1,6,-2,-10,-7,5,-1,1,-3,-6,-10,10,4,7,-6,10,-10,5,-9,9,4,-8,-6,-10,2,6,4,-2,-3,10,3,-9,6,-5,1,-1,-9,-1,-9,-4,9,-3,-9,-9,-3,4,-9,-9,8,-10,-7,3,3,2,7,3,9,-8,8,-1,-8,-6,-7,-2,8,-2,-4,-4,-3,8,-4,7,-6,2,-4,-6,-7,7,-7,8,2,4,-9,4,-5,-1,5,2,4,-7,8,-1,6,-10,-9,-2,-8,-9,-5,8,-7,-8,-8,-6,-6,-3,8,1,3,1,-8,5,9,7,-8,5,6,10,4,8,-10,-4,4,4,-7,-1,8,-4,-9,3,4,3,-1,-5,10,5,-4,-8,-6,-8,-7,-7,7,4,-2,5,6,7,-10,2,-6,10,10,10,10,9,9,4,9,3,-6,-7,-6,-10,5,-8,1,-10,-8,6,-8,-7,1,6,1,9,-8,10,1,2,-1,6,10,2,-8,-6,-3,5,6,4,-1,-3,-1,4,-2,-9,-7,-7,-3,-5,-7,-7,-5,2,6,-9,3,7,-6,6,-7,4,-2,-3,8,-5,-2,-5,9,-10,-5,3,2,2,10,7,4,3,10,10,5,-5,10,-4,7,-5,3,-2,9,-3,3,8,9,5,7,-9,5,-9,-4,-5,7,5,9,4,-1,-6,-7,6,-6,-7,-8,-5,-10,9,9,7,3,7,9,-7,10,-7,-10,3,3,8,6,-6,2,-2,-9,-9,3,4,9,4,-7,-6,-3,-2,1,-2,7,-5,3,-8,-10,-5,-4,5,-10,-5,-10,-5,-2,-3,-9,1,-3,3,-8,10,-9,-1,6,8,-4,7,4,9,9,10,-7,1,9,-7,8,-5,6,2,1,-10,-3,-9,6,-4,1,2,6,9,-9,4,-8,6,4,-6,10,-8,-4,1,-8,-5,-10,9,2,5,8,1,-8,-10,5,-5,-3,-7,1,-6,-2,10,-10,9,-8,-3,2,2,1,2,9,10,-10,10,-4,2,9,-9,2,-1,2,9,-10,-6,7,8,3,10,6,7,-6,5], dtype = "int64")#candidate|6849|(525,)|const|int64
const_6850 = relay.const(-3, dtype = "uint32")#candidate|6850|()|const|uint32
call_6848 = relay.TupleGetItem(func_765_call(relay.reshape(const_6849.astype('int64'), [7, 15, 5]), relay.reshape(const_6850.astype('uint32'), []), ), 0)
call_6851 = relay.TupleGetItem(func_768_call(relay.reshape(const_6849.astype('int64'), [7, 15, 5]), relay.reshape(const_6850.astype('uint32'), []), ), 0)
bop_6866 = relay.maximum(const_6850.astype('int8'), uop_6837.astype('int8')) # shape=(12, 3, 13)
bop_6869 = relay.maximum(const_6850.astype('int8'), uop_6839.astype('int8')) # shape=(12, 3, 13)
func_4087_call = mod.get_global_var('func_4087')
func_4090_call = mutated_mod.get_global_var('func_4090')
var_6887 = relay.var("var_6887", dtype = "float32", shape = (384,))#candidate|6887|(384,)|var|float32
call_6886 = relay.TupleGetItem(func_4087_call(relay.reshape(var_6887.astype('float32'), [8, 16, 3])), 0)
call_6888 = relay.TupleGetItem(func_4090_call(relay.reshape(var_6887.astype('float32'), [8, 16, 3])), 0)
output = relay.Tuple([call_6848,const_6849,bop_6866,call_6886,var_6887,])
output2 = relay.Tuple([call_6851,const_6849,bop_6869,call_6888,var_6887,])
func_6889 = relay.Function([var_6887,], output)
mod['func_6889'] = func_6889
mod = relay.transform.InferType()(mod)
var_6890 = relay.var("var_6890", dtype = "float32", shape = (384,))#candidate|6890|(384,)|var|float32
output = func_6889(var_6890)
func_6891 = relay.Function([var_6890], output)
mutated_mod['func_6891'] = func_6891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5395_call = mod.get_global_var('func_5395')
func_5396_call = mutated_mod.get_global_var('func_5396')
call_7024 = relay.TupleGetItem(func_5395_call(), 0)
call_7025 = relay.TupleGetItem(func_5396_call(), 0)
var_7027 = relay.var("var_7027", dtype = "float32", shape = (12, 3, 13))#candidate|7027|(12, 3, 13)|var|float32
bop_7028 = relay.bitwise_and(call_7024.astype('int64'), relay.reshape(var_7027.astype('int64'), relay.shape_of(call_7024))) # shape=(12, 3, 13)
bop_7031 = relay.bitwise_and(call_7025.astype('int64'), relay.reshape(var_7027.astype('int64'), relay.shape_of(call_7025))) # shape=(12, 3, 13)
output = bop_7028
output2 = bop_7031
func_7032 = relay.Function([var_7027,], output)
mod['func_7032'] = func_7032
mod = relay.transform.InferType()(mod)
var_7033 = relay.var("var_7033", dtype = "float32", shape = (12, 3, 13))#candidate|7033|(12, 3, 13)|var|float32
output = func_7032(var_7033)
func_7034 = relay.Function([var_7033], output)
mutated_mod['func_7034'] = func_7034
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5488_call = mod.get_global_var('func_5488')
func_5489_call = mutated_mod.get_global_var('func_5489')
call_7059 = func_5488_call()
call_7060 = func_5488_call()
output = call_7059
output2 = call_7060
func_7061 = relay.Function([], output)
mod['func_7061'] = func_7061
mod = relay.transform.InferType()(mod)
mutated_mod['func_7061'] = func_7061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7061_call = mutated_mod.get_global_var('func_7061')
call_7062 = func_7061_call()
output = call_7062
func_7063 = relay.Function([], output)
mutated_mod['func_7063'] = func_7063
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7085 = relay.var("var_7085", dtype = "float32", shape = (16, 13, 11))#candidate|7085|(16, 13, 11)|var|float32
uop_7086 = relay.asinh(var_7085.astype('float32')) # shape=(16, 13, 11)
output = uop_7086
output2 = uop_7086
func_7108 = relay.Function([var_7085,], output)
mod['func_7108'] = func_7108
mod = relay.transform.InferType()(mod)
mutated_mod['func_7108'] = func_7108
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7109 = relay.var("var_7109", dtype = "float32", shape = (16, 13, 11))#candidate|7109|(16, 13, 11)|var|float32
func_7108_call = mutated_mod.get_global_var('func_7108')
call_7110 = func_7108_call(var_7109)
output = call_7110
func_7111 = relay.Function([var_7109], output)
mutated_mod['func_7111'] = func_7111
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3074_call = mod.get_global_var('func_3074')
func_3076_call = mutated_mod.get_global_var('func_3076')
call_7132 = func_3074_call()
call_7133 = func_3074_call()
func_5818_call = mod.get_global_var('func_5818')
func_5821_call = mutated_mod.get_global_var('func_5821')
const_7137 = relay.const([-7.879679,4.506787,6.071152,5.924832,1.300029,-3.369251,4.696406,5.055303,7.586456,-9.510069,3.348768,1.711827,-6.482577,-9.236918,6.343597,8.191874,7.587749,4.178790,-5.283513,-9.186543,-9.585998,-2.439915,3.414471,6.999761,2.935812,-7.547539,9.980976,-4.890227,4.882691,-1.613088,-6.559270,-3.832627,-4.902005,1.215404,0.698764,-1.540308,-2.272986,7.504280,9.813406,-2.037804,-5.723028,8.630359,-1.603190,-7.467058,-1.037560,-7.512853,-5.577498,8.929918,5.738626,-9.764914,-6.867460,-4.386628,2.327336,3.331369,-5.024330,1.638141,-7.835412,6.363507,-7.892346,-6.229751,-0.515943,-5.242951,-2.252043,0.622779,-6.540303,-0.534058,4.876151,0.524508,-5.971416,7.469016,-7.757573,-5.061317,2.196943,-5.442534,9.816115,-5.119862,8.547889,-4.095235,-5.492519,8.486262,2.435811,-3.321775,8.348644,5.166850,-5.944400,-1.437390,0.104799,1.245328,-5.537646,8.780656,-0.560368,3.036298,-3.143787,4.935043,-4.209136,9.983877,-9.031647,-2.641270,8.165057,-2.597285,-7.771975,-0.427459,9.609499,-4.273803,3.595719,7.206612,8.918453,-8.341109,-7.969723,8.429428,-4.816714,9.567231,-0.400270,-2.647956,4.667436,6.362737,-6.791910,-3.780367,2.331149,7.728922,-3.471539,-3.493667,-2.187877,4.113124,1.074815,2.317439,4.176958,-0.992998,-2.722324,6.051859,2.447954,5.194538,-8.579573,9.864954,-9.731686,8.019609,7.098897,-9.983554,-1.479419,4.842455,-1.322703,7.351653,9.547398,0.044872,6.633749,7.934920,3.986107,-7.267780,-8.692816,8.327021,-9.531925,7.780554,8.472694,4.434217,6.481513,7.009335,9.896175,0.290449,-2.521371,-4.968970,8.439475,6.361294,-9.203863,9.489977,5.234349,1.331509,4.779438,-2.820903,9.518852,-2.967355,-9.360410,-5.610705,-0.229650,-6.081092,8.836236,-5.535148,-0.795738,1.841596,1.741081,-2.762197,-7.501136,1.357892,-9.313594,-1.074980,8.647739,1.172713,-6.600314,-5.051817,4.079847,6.202355,0.367789,-0.410430,0.405933,1.869199,-2.806649,-8.870997,6.000766,-9.033750,2.665458,9.794267,5.019339,-4.089216,1.350880,-7.851540,9.138584,2.755977,-3.737208,-7.679173,2.925335,-7.149649,9.823669,-2.534161,-1.382323,1.554047,3.528013,7.001729,7.895126,-7.350203,-5.129374,4.154060,3.856806,-7.403442,-1.049443,0.058130,-6.722558,7.369852,-5.394120,7.185550,-2.968231,-3.112201,8.314925,-9.175288,8.478411,6.604999,-5.957381,7.967279,5.961553,7.616696,5.600003,-6.604002,-4.038456,8.932122,9.269111,-5.660385,7.018020,-8.891336,-7.446067,9.271003,6.105527,1.078070,-4.138855,3.535254,-9.159111,2.395778,-5.294947,-3.753242,-9.119657,8.812180,-9.762873,8.023029,7.553260,-0.690696,5.709991,1.603011,2.846338,-9.915049,-3.979920,7.798743,-5.283076,-3.989193,-9.127943,2.216866,-2.851459,0.459528,-7.504149,8.532484,-4.258741,0.265679,9.766544,-3.790541,5.320297,-3.460285,1.275007,3.366265,4.336586,-8.756600,-1.775293,-5.386742,-0.191332,4.840293,-5.131290,-3.477918,-7.888311,-5.863042,9.524711,-8.147594,8.175855,-9.906900,9.117169,-0.601692,3.770196,-1.482715,5.271555,-2.333121,-8.473714,-0.802977,-5.839335,6.069667,7.701830,2.257787,7.857501,8.884592,-0.118091,4.303444,9.442266,-9.826556,-3.033373,-5.366974,9.084682,9.149859,-8.265329,2.571878,8.880034,-4.536437,-8.632252,4.311947,4.870576,2.423646,-7.618131,9.714236,-8.799848,-3.911499,6.174355,-6.544536,5.775286,-6.629950,-1.622146,7.540209,1.892756,-0.063430,6.319406,7.875728,-5.147136,-3.892121,5.760825,2.005750,-8.625732,-0.065412,-9.512548,-5.724604,-6.708166,-8.145657,-3.045058,-8.060387,8.468422,-5.669565,-1.215354,1.643438,-6.843018,2.368064,-2.770635,2.779586,-5.461090,-2.809696,5.439700,3.803809,2.025459,-7.996512,3.071092,7.819047,7.929658,9.681668,5.806553,-7.445151,-2.612386,1.887604,-6.250656,1.538296,-5.006612,-2.022464,2.231498,-0.537118,6.915343,-6.878022,2.962740,4.109770,2.424527,9.055155,6.542229,-1.259552,8.611671,-7.154225,7.960231,4.557601,9.989358,3.218321,6.314089,-7.005603,-6.404385,8.986088,-6.595322,-1.276218,6.827373,2.557495,4.046833,-3.869767,9.208527,6.829117,5.382981,4.342067,-1.523603,4.298655,-9.084104,-5.250383,-7.340049,-4.509876,-1.180201,3.752477,-8.486926,-6.916474,-6.721700,1.742313,-4.012444,-1.790515,2.449669,-8.508288,-3.232082,2.364389,1.123168,6.224142,2.838583,3.323670,-0.853503,6.188094,6.022527,0.075244,-0.204045,5.607588,7.803239,-2.109974,5.685961,-3.902115,-2.820817,-9.021159,4.961319,-7.841267,-5.617314,-8.717854,-7.324495,1.704661,2.075742,2.376053,6.578542,-3.850714,6.232625,2.741800,-3.130118,-7.065994,6.888363,-2.116712,0.477997,5.377069,-8.738496,-3.895149,4.676537,-2.854744,-9.437503,2.270340,4.487344,-2.423997,-0.525572,4.656566,0.043492,-1.798211,8.388990,9.982929,0.400750,-1.545257,-1.507410,-2.217523,-6.419302,3.900572,-6.777168,8.871399,-7.856581,-3.893207,4.754470,1.884708,-9.618662,-0.789833,0.642729,-3.003559,-1.219188,-1.815200,9.642140,0.588593,-8.382109,7.639267,7.314788,-5.753576,-7.603297,-6.134338,-8.478310,8.656642,2.503828,-2.135770,4.017541,8.494945,6.343762,2.644349,-9.999456,4.344162,3.370151,-5.825580,8.486195,-4.534413,5.341172,6.946548,1.082476,-6.585436,-7.183469,3.796552,2.054079,-7.617514,-2.151839,-3.264187,-7.791972,0.917060,-1.223815,-9.504841,-1.022947,2.901128,9.556295,-9.738756,9.076769,-9.041198,5.003780,-5.750472,-0.746886,-4.644819,-2.569724,-6.879985,-4.289527,-5.468095,0.908297,-9.252184,4.689737,7.330759,-1.733140,4.386639,3.926513,-6.303864,6.987150,3.938808,1.225797,1.855411,-0.318275,-8.086386,8.465918,1.069750,5.104207,3.540846,-6.742517,1.731585,-7.192722,-9.633406,-4.322537,-0.174979,5.515910,-1.342098,1.039823,-1.536073,3.462360,-2.027758,7.362883,2.740631,2.188473,-8.887124,6.350579,8.247548,-5.235529,7.159470,-9.634942,3.166129,-6.043110,-8.014554,1.282261,4.861311,3.353246,0.008669,-7.632763,2.892162,0.495885,8.389458,4.066577,-5.941825,-8.321006,9.108259,-1.533658,7.926268,-9.497073,-6.467588,-7.160792,-0.313570,-6.011852,0.697756,-0.814513,-3.458963,-9.811234,-8.555812,-3.287686,1.142632,6.023664,3.241000,9.865748,-9.846076,-3.913549,5.898846,-6.639101,-5.385000,-5.297359,6.655268,-2.085108,-5.119566,8.003828,4.367533,-1.892123,4.697998,0.931594,0.304937,2.774626,-9.718907,-6.780878,-1.235224,9.210880,4.984721,-7.833709,-2.912756,7.587775,3.339394,7.480066,-8.296547,-2.550729,0.261755,9.019783,-5.006367,-2.921208,-7.764531,2.380518,-5.699560,-9.932475,-5.014874,-0.685044,1.988047,0.326985,5.573877,7.784701,-9.155767,6.158405,7.243741,-6.870632,1.386475,-0.018525,-0.933802,-2.850544,-2.833792,-7.065005,-6.257405,1.283148,-4.892765,-3.310849,-3.592213,-4.584389,7.613412,-9.801449,-3.678003,2.311605,-6.214742,3.628677,3.044055,2.344499,-0.652518,-7.515412,-7.784572,0.200182,-3.883285,-6.063415,7.276381,-7.095298,-0.768014,-6.290851,5.593420,-2.517313,5.260042,-4.329306,-4.564679,5.218772,-3.835651,6.237357,8.240363,4.258052,-2.275534,-6.158991,-3.012095,2.443783,-9.741862,7.288757,2.725150,3.823555,-2.762945,7.526598,5.500784,0.537441,-4.175066,-4.327990,2.025526,0.746517,-0.506998,-9.892982,-5.344142,5.055849,8.723341,7.845233,7.661655,7.649686,-1.067239,-7.767614,8.056570,8.038432,-3.574834,-9.063203,-3.774614,2.981524,5.819581,3.672625,1.733007,-9.198739,-5.337263,6.061813,-2.400628,5.532082,7.264798,-7.358121,2.905019,-2.439126,-0.342578,-5.081905,5.168328,4.011144,6.174903,-1.944593,2.507282,2.551353,-3.598271,9.620535,5.430702,-9.124758,-2.564184,-6.676192,-9.200681,6.862497,2.711219,9.864908,-9.289245,2.793737,-9.573157,-2.746526,2.743278,8.406343,1.977903,-5.543127,8.303601,6.723425,-9.073721,2.988162,3.005180,0.650599,-6.659455,8.752784,7.773270,-4.145325,-3.791850,0.962609,-7.422228,-6.863996,-9.172429,3.403983,5.602407,9.636042,-0.661486,-4.460465,-7.700963,-5.504761,1.204949,6.772688,-7.107013,-0.957460,-4.412986,-1.786594,-8.118638,-7.062720,-4.367610,-8.173596,0.436480,3.110738,-4.056472,9.499800,5.501013,-2.168244,6.094065,0.954904,0.762726,-7.357685,3.336692,4.354139,9.677833,-4.135116,9.915715,3.238671,3.292467,-9.865994,3.918275,-5.843391,3.394208,7.319017,-7.363948,-3.707983,-3.495093,3.768689,-1.450477,1.860172,2.038271,0.021534,-7.593129,3.265775,5.810998,4.752014,9.595148,6.444410,-2.895889,5.403267,1.195437,3.838081,-0.408526,6.954321,0.167598,0.715596,5.177915,3.636598,7.361702,3.582917,-7.969965,2.986562,-3.632342,-4.321452,3.417228,0.052554,5.122669,-8.188070,5.610376,-0.072574,-4.268372,2.037577,-9.985331,8.423552,9.585240,-4.509656,-7.897973,1.169597,-2.618539,4.307927,4.216259,-8.372974,6.432138,1.987026,4.996632,3.632590,5.241352,9.064316,8.016893,9.903307,1.455283,-1.075804,-8.877945,-8.836164,7.611423,-8.313706,-1.055115,-3.749149,-1.002665,-5.715152,7.515241,5.401374,8.564754,2.719174,-3.935439,1.196283,-4.251857,0.302306,-9.907324,-2.644717,8.199974,-9.871478,2.939672,-4.735542,-6.511780,6.764718,-2.862179,-5.210733,3.451460,7.903379,0.047664,6.342661,-8.883260,-8.093129,-1.023594,3.736300,8.771351,6.426417,-0.537244,-1.082649,8.764095,-8.251000,8.296971,9.908388,-0.203278,-3.196311,0.722676,-2.201470,-8.231508,-4.823315,7.708694,-4.029518,-1.486277,1.192985,5.595490,8.635303,-0.213678,7.662575,8.872539,-0.717697,1.738146,9.457641,9.309399,-1.001942,-7.865604,-1.933517,-2.126997,-4.892041,0.276170,0.956510,-0.087336,4.496354,7.200347,-5.195970,0.001801,-2.670382,2.453634,9.677165,3.195607,-4.304097,3.797325,6.797346,4.735900,-8.532736,-8.657791,-0.634992,-0.896722,7.505952,-2.491047,-0.046607,-6.058988,-7.503728,-9.891153,-1.167982,2.819297,1.260431,-0.786059,7.819173,3.988407,-7.319332,4.833692,-8.624472,-0.128217,1.997003,0.877211,-2.092792,2.266904,2.965178,-4.480184,4.822979,-3.952991,-2.853102,-5.616644,-1.664338,2.767861,5.537298,8.237717,7.843222,9.099292,-2.179901,-7.833723,-3.576175,9.411259,-8.375959,-6.475346,-2.939003,-1.762651,6.644935,-7.389980,-7.654159,-7.971022,-8.173490,7.181331,9.239787,2.501545,0.544991,-2.079170,0.247414,0.308829,3.692778,2.134184,-0.332545,8.553877,-5.555611,-4.321839,3.045162,-4.204861,-2.254807,1.867263,-1.568562,-4.839978,2.420603,-6.407824,-6.203053,-5.014169,8.753048,7.417153,6.477582,4.541207,-7.470650,8.018124,-4.854067,-4.605887,1.556269,-2.874912,-6.847761,-8.797829,4.597948,-3.785094,-7.499427,4.899785,-5.467916,-1.617985,3.391290,-8.591399,8.919088,-3.873819,3.296089,-4.386422,-8.687357,4.044595,8.026702,-0.162148,-1.406939,2.980430,2.859368,-8.993417,7.225470,-7.996062,-5.407829,4.036838,-5.827430,9.018042,-4.462861,-8.421679,-0.874183,6.125388,9.691934,-5.722658,-4.304809,3.437095,-5.064254,9.981794,-2.248736,5.212550,-2.288217,-3.640420,-2.197304,1.507697,5.501941,8.215149,2.865530,-7.755732,2.706920,-2.090579,-5.964564,6.254705,7.155533,-3.281868,-5.535677,-1.414716,-0.497630,9.604439,-0.573741,6.637161,7.969991,6.146945,8.013440,2.456098,-1.311916,-3.532311,5.706534,6.390743,4.041855,-0.247310,8.446874,-3.103914,0.253974,-7.830594,-6.313925,-4.397419,4.960675,-6.731082,9.129485,2.489160,3.694225,-7.183120,6.456424,5.050926,0.459045,1.422357,-2.726970,5.556385,8.672763,7.458412,4.711876,3.165198,3.659068,-6.201430,-6.423864,-0.958434,1.702284,-2.792424,9.407079,4.430798,-6.941057,9.716026,3.021715,-6.883205,0.992503,-2.416051,1.657021,6.864402,-5.165549,7.769897,6.850168,-8.880919,-1.661012,0.556846,3.782281,6.797675,3.498417,-2.951937,9.169997,-7.324157,6.267758,2.270302,-3.181508,7.467818,-1.360732,3.462583,9.013063,0.437520,7.718607,3.975362,4.558449,-1.906458,1.471123,2.453850,8.084599,4.376553,3.749873,-7.866476,3.339581,-9.032456,-9.875456,7.673470,8.320717,-8.416342,-2.336772,2.543143,-9.921528,-6.996411,6.578377,-6.553031,5.427333,9.706484,-5.182496,5.942352,0.405930,-7.052504,6.910699,5.652982,-2.412159,5.466543,8.922441,-7.892246,-0.851263,-2.634713,8.001418,2.402034,-7.565732,9.202936,-6.967564,1.434038,-9.315881,9.273530,7.392745,-5.569161,-2.242684,-6.764551,9.938142,4.857828,-0.228936,7.627126,-2.055653,-4.965824,4.810613,-7.571246,-6.306661,1.397676,3.403052,7.312255,-1.421474,-2.850673,5.447231,-6.485077,7.842543,1.328153,6.395858,4.665905,9.150179,7.026120,4.058848,-2.744799,3.269351,-8.430493,-1.268140,3.982794,-5.666017,-2.670492,6.271133,-9.862384,-9.542763,-8.656733,-4.544814,-2.829188,6.290917,-3.212671,9.921419,4.083328,-2.373600,4.211977,6.623434,0.048251,-6.495889,5.362323,9.334204,-5.687276,8.173592,1.555777,5.916620,5.101459,9.273948,8.065763,-9.149028,0.986801,3.097673,-8.329422,-3.129310,-0.290864,6.997560,-4.084302,7.541190,-0.088446,8.554370,-8.256006,5.222699,9.199552,5.394790,8.249189,7.446813,-1.247448,2.381947,1.491118,9.994697,-6.899539,-9.837136,1.356626,-6.377739,-1.547407,5.116362,-0.382723,4.193559,-7.153436,-9.025401,-3.508993,-2.595660,-7.479322,0.579768,9.099585,4.390585,9.206743,-0.378316,4.659438,5.316932,-8.213138,-9.225550,6.591108,5.206439,-5.770053,-9.048122,6.460996,-8.841064,-8.702897,-2.108149,-0.010503,-7.546712,1.578117,-5.326686,0.804792,-1.049477,-6.797727,-4.193572,-6.422724,9.764798,2.345212,-6.909581,5.969298,1.378599,-2.289147,4.817743,4.001497,2.613003,4.020502,-5.833111,0.139630,-0.074223,1.151110,4.687274,-5.526281,8.313688,-2.876874,4.912611,-0.223112,-5.511930,-3.366877,4.656705,0.961915,-2.227071,-5.604121,8.342572,9.577948,5.782303,-2.637778,0.358231,-1.588972,-0.690333,-3.336593,-5.787590,-8.979870,2.735005,-2.358163,3.258557,3.669963,-1.523631,-6.246376,7.865346,-6.961629,-9.503212,-5.800733,5.439672,-9.897851,2.716722,1.519073,2.780363,-5.821791,-0.551388,5.843620,-0.814040,3.487733,-8.178397,-4.137807,-7.760426,5.894629,2.798878,-1.103042,-2.699124,2.600026,5.239225,9.373050,-4.995220,2.191988,-5.478744,-0.246196,-3.056810,-2.953354,1.854970,-2.269802,3.119074,9.329224,3.341160,0.438054,-3.285321,-2.052693,-4.638345,8.530347,4.158015,1.807782,0.402859,3.472681,-1.212695,6.334515,-1.892281,0.887625,6.676865,2.269691,-8.156976,-3.381733,3.997533,-2.556103,-6.352699,-4.423983,-5.938394,0.460810,-1.187887,0.517763,-5.112939,-7.200370,8.674494,-7.159863,-7.482849,7.732540,2.605988,-8.181022,-4.144633,-6.361458,-2.669158,9.264960,-4.088611,-5.827861,1.923511,0.146469,-5.609952,-4.708987], dtype = "float64")#candidate|7137|(1456,)|const|float64
call_7136 = relay.TupleGetItem(func_5818_call(relay.reshape(const_7137.astype('float64'), [1, 1456])), 1)
call_7138 = relay.TupleGetItem(func_5821_call(relay.reshape(const_7137.astype('float64'), [1, 1456])), 1)
func_2745_call = mod.get_global_var('func_2745')
func_2747_call = mutated_mod.get_global_var('func_2747')
const_7152 = relay.const([-2.851265,-5.307222,-8.922047,0.284254,8.073419,-1.499610,-9.535323,-2.290453,8.693348,-8.585122,-3.091982,3.207606,1.123660,-5.422204,-7.855632,-1.340055,-6.953020,-3.069157,9.354203,-3.655270,-2.026131,0.541033,8.779353,-2.524430,-2.065225,-9.689072,3.313975,3.758010,2.441912,-6.070679,0.624976,-3.586473,6.508597,-3.266742,6.279072,3.734042,-2.065717,-8.105954,-8.638363,-1.111302,5.731484,3.492128,6.001726,-5.444720,8.734996,-6.906742,7.874549,-9.072130,9.256117,0.830927,5.778772,-6.047419,3.684417,4.622032,-1.304659,-2.476820,-6.199753,-7.902945,-3.544295,-9.355619,4.346591,-9.376972,-1.451526,9.392855,-5.000804,-9.481689,-6.218191,5.641315,0.642042,4.870503,-6.513811,5.253645,-9.977999,-2.159537,-5.910098,-3.917456,7.719381,-2.620523,4.745526,5.057762,-3.211817,-1.884660,8.862289,-3.700163,-0.965906,-5.203878,-5.750473,-6.035222,9.550156,6.689355,4.384469,-2.464566,1.332399,-7.014379,-0.246466,-5.476932,8.832262,5.285923,-9.537196,5.061055,-4.578543,3.745259,-8.464869,5.976179,8.398661,7.139614,-4.755922,0.381598,1.942192,-5.492152,-5.739783,-0.371414,4.617449,-5.947443,-9.410428,8.918247,6.072395,4.761023,-0.385859,9.412098,0.905477,-1.191339,-3.185883,0.926550,-2.437762,-4.588586,-6.742769,-0.302496,-7.753324,4.864602,2.388349,5.733975,-0.600996,-2.933675,9.562324,-1.548219,-5.383915,-5.834238,-8.796502,-3.601335,-7.796696,3.490454,-4.379555,-4.576825,-2.832404,8.098321,-3.714746,-2.170772,4.161535,8.698090,5.358372,3.314777,4.588424,-0.193880,-5.649345,-9.677796,5.439571,4.958694,1.329719,6.389665,-6.013329,7.189965,2.799840,4.329922,-2.064421,-7.121940,-4.818204,-9.446698,0.796285,0.205839,6.489623,-2.323416,-3.104109,-0.519132,-6.701370,2.614341,-8.496770,4.172017,0.452831,-2.680059,-1.454175,1.609745,1.498673,-3.823840,-1.411612,-3.651569,0.223506,6.530155,-6.125068,5.063819,2.068975,3.235691,-6.978911,8.231080,1.264569,2.951393,-7.513989,-8.547381,-0.558144,9.597230,0.886141,5.765393,-0.608298,-9.371038,-0.470735,2.385743,-7.910425,-9.603987,-1.711798,-8.524738,6.998399,8.319434,-1.679514,5.273165,-2.048272,-2.918564,-6.650816,-9.498753,-8.581082,-2.240284,-7.555424,-2.947662,-7.268599,7.891403,-0.848585,0.939086,-4.307647,-2.195330,-9.922383,2.542069,-8.663937,-6.601844,5.497171,8.228888,3.098211,7.421397,-4.297661,5.636173,-3.377910,0.495032,-2.095967,-0.321488,3.709554,-3.567843,4.199587,-5.083992,3.805971,-5.148213,7.949021,-8.063422,0.234006,-8.834327,1.299874,2.977163,8.697306,-0.420548,2.305050,-1.711748,7.025389,-2.770811,-1.877274,-4.088296,-7.145055,7.144788,1.434175,-8.229173,7.450204,-3.169064,-2.058737,-0.185253,-7.158604,-2.140780,0.229075,-7.947370,3.257321,3.955331,2.991763,6.332813,5.321639,8.380190,-6.811927,3.617712,-7.184039,-8.394097,9.426670,-3.387263,4.137164,2.712557,2.395162,-7.198470,9.558165,6.201822,1.901900,-3.552416,8.375597,6.676198,6.355086,8.147955,-0.510273,6.306041,-0.026208,2.318852,-3.912978,-8.133593,-4.062910,-7.759039,4.504468,-9.053683,-0.918006,0.474309,-1.105674,5.409532,7.862667,-9.994960,-4.512122,-1.502159,1.630382,-7.734708,-3.223298,-8.409533,1.632155,-5.383354,-6.918334,-7.073207,5.419003,-7.874088,-4.168670,-8.314103,-0.474015,-2.864772,-1.761244,5.758895,-0.734376,4.722906,-9.525366,-7.712993,-2.214414,-6.517682,7.988200,6.483325,-1.127665,0.461282,4.346245,7.704771,-0.419941,-3.029621,-3.300926,-3.890832,1.380677,1.211420,4.458265,-2.976069,5.184801,-0.176149,7.401711,9.859638,0.223702,-9.440451,-9.229494,-3.720565,1.599735,9.299853,-1.216068,5.039087,8.044380,-9.057938,-8.027728,-6.520242,5.582348,-4.985254,-4.453942,8.376266,-7.840873,-6.305413,6.421222,8.059487,9.926829,-9.084433,3.508313,-2.255221,-1.139497,9.456766,5.811499,-5.797456,6.265482,8.975334,4.929633,5.788944,-3.115379,-9.877978,7.962647,5.240534,3.033922,-7.093208,2.714607,2.044971,7.402906,-2.879460,6.149133,-4.526352,7.127365,-6.945693,-3.936787,9.010569,-4.959850,-5.819191,3.498472,-4.220821,1.489153,8.166778,1.563051,-5.185453,-2.596689,5.756239,-6.614938,-9.471374,6.967998,-0.882110,-0.251744,9.707546,5.955395,-4.524568,9.380223,4.482833,-5.312824,8.564925,-2.476034,-5.302333,-8.200141,-1.911999,1.498229,-9.660038,6.749618,-8.546230,-7.304154,-5.524772,4.903559,8.741858,-0.171286,9.928611,1.257657,-2.151239,3.840288,-2.195226,5.932671,-5.562907,2.711285,5.806019,5.763162,3.847082,0.118502,8.646762,-1.278587,2.542967,-6.459244,0.655295,7.259374,1.672209,0.885495,-9.758230,-3.130528,4.698302,-4.997355,-6.470377,7.345771,2.759060,-9.386647,9.612764,4.287602,0.811312,-9.502394,-5.133917,-0.222833,-9.843444,0.471643,-5.291520,4.262460,-1.377824,0.132929,9.575567,-0.292973,5.634337,2.338224,7.502305,-5.252666,-9.077901,-1.032306,-5.993248,-5.858183,-1.030215,-0.798214,6.432757,-5.920471,7.070180,2.541728,-1.998821,7.382502,-9.262471,0.258357,-5.434771,-5.407995,-5.341169,4.652356,5.744937,7.599911,9.961634,8.423807,9.303573,-2.977983,0.932561,6.355664,1.662687,5.411654,1.739804,-8.737235,-6.183559,6.421729,9.450151,-2.706270,-0.028651,-8.628627,0.814181,8.865473,1.378144,2.806574,4.988633,4.131988,8.120480,-0.932529,5.056961,-6.556706,3.353966,-9.732442,-2.266759,9.425073,-7.534850,5.733944,3.903608,-3.330367,-8.613865,0.167944,-1.664780,8.222953,-7.261925,-8.643703,-2.159320,2.017565,-4.705249,-0.405780,-0.635349,-8.353944,1.558893,-2.015526,-6.807302,9.435719,-3.108976,-5.074280,7.911034,2.873704,2.692977,0.859141,-8.420494,5.843314,-3.976300,-1.976860,5.497604,1.670587,-3.046912,-0.094528,-1.757948,3.476306,-2.278718,8.751409,7.269137,5.161923,7.350782,-3.816444,-5.926044,-7.729103,0.022381,5.257505,9.717895,9.523870,7.361090,-5.776436,-1.077957,-8.006597,1.353039,-3.831681,-3.429955,5.029553,8.999900,-2.246920,6.432300,-8.702278,6.424282,-3.475205,0.720143,-4.303734,2.826149,-7.340254,-4.244181,-8.529086,0.179086,7.635282,4.004735,1.444601,-5.061399,-0.557719,-8.678168,5.504353,-3.552161,6.870973,1.214318,-6.535268,-9.373526,-8.936380,-0.779318,8.159498,-7.133234,2.904520,7.175483,-6.921803,-1.022764,-2.490779,6.710080,-3.400878,4.964075,9.029446,4.984340,2.074591,6.393417,4.710954,-8.672469,5.425511,1.869862,-2.754626,7.971370,-4.685933,3.221417], dtype = "float32")#candidate|7152|(640,)|const|float32
call_7151 = func_2745_call(relay.reshape(const_7152.astype('float32'), [10, 8, 8]))
call_7153 = func_2745_call(relay.reshape(const_7152.astype('float32'), [10, 8, 8]))
func_3945_call = mod.get_global_var('func_3945')
func_3947_call = mutated_mod.get_global_var('func_3947')
call_7158 = relay.TupleGetItem(func_3945_call(), 0)
call_7159 = relay.TupleGetItem(func_3947_call(), 0)
output = relay.Tuple([call_7132,call_7136,const_7137,call_7151,const_7152,call_7158,])
output2 = relay.Tuple([call_7133,call_7138,const_7137,call_7153,const_7152,call_7159,])
func_7160 = relay.Function([], output)
mod['func_7160'] = func_7160
mod = relay.transform.InferType()(mod)
mutated_mod['func_7160'] = func_7160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7160_call = mutated_mod.get_global_var('func_7160')
call_7161 = func_7160_call()
output = call_7161
func_7162 = relay.Function([], output)
mutated_mod['func_7162'] = func_7162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3074_call = mod.get_global_var('func_3074')
func_3076_call = mutated_mod.get_global_var('func_3076')
call_7223 = func_3074_call()
call_7224 = func_3074_call()
func_3440_call = mod.get_global_var('func_3440')
func_3444_call = mutated_mod.get_global_var('func_3444')
const_7227 = relay.const([-4.659917,8.078864,-8.502879,7.295494,7.546155,8.721048,-0.138030,2.706621,-2.808067,4.124997,7.328432,4.808354,-8.649996,-8.322799,-3.433505,9.401442,2.649025,2.999654,3.373243,2.008679,1.445489,5.936315,-5.553688,0.074492,7.990964,-6.045720,-8.444202,-7.750260,3.329666,3.076992,7.801539,-6.083562,5.518069,9.782588,-4.724581,5.492320,5.024048,-1.953567,8.388549,-1.079953,-3.637269,-4.813183,-4.962323,7.915489,1.412545,3.797443,-2.769819,8.253771,-6.493564,-9.207940,8.964186,-2.132731,-1.007310,-8.388285,-5.540535,-0.619153,0.854616,-3.800852,4.636477,-9.724862,-7.084327,-1.424882,2.103860,-6.275617,-0.099017,5.067204,-4.013422,-3.755085,-5.854138,5.253477,-7.771801,1.698472,-5.994153,7.645580,-2.674609,-0.809874,-2.317209,4.336064,-8.879116,9.096742,-6.506430,-4.658304,-6.631683,4.347393,2.251210,-9.824259,4.567961,9.819939,9.051506,9.794415,-4.792027,-8.158224,-8.190176,2.526761,7.012332,7.053011,3.147592,-6.543728,5.398176,-1.623560,-0.023280,-0.105073,-7.289651,6.628207,-9.551016,1.018294,-6.488169,3.550986,3.253726,0.962896,3.185209,-3.893940,-8.744047,4.108086,1.693373,-0.184191,-8.274999,8.599165,2.481642,-9.669182,7.621690,-9.745350,0.485637,3.056550,-7.685065,2.318392,5.484016,-1.422684,-7.636946,1.003000,2.913310,-3.597785,-1.813242,8.059982,-0.833795,-7.580567,9.334288,-5.930367,-1.159608,-9.386346,-6.862832,8.274207,9.994818,-2.836114,4.494670,0.550622,7.662645,-7.277577,2.641611,7.301758,3.044162,-8.135823,6.918133,8.145378,-2.929271,-0.308771,2.134114,-0.516905,-0.446679,-9.230777,3.167642,-2.176180,9.611396,-0.933174,-6.700085,4.703124,8.299526,2.720248,-2.715741,0.396083,-3.523711,7.065290,2.655284,-8.773206,-2.153773,4.023748,2.620017,3.626170,-8.010001,9.597586,6.996084,-1.550826,-6.216355,5.565827,-1.801585,2.379733,8.884471,-9.063143,2.474590,-5.411541,0.799508,3.168182,6.495669,-9.477908,-6.058112,7.920166,-7.374791,9.067430,8.545495,8.101711,4.919222,-0.545206,8.011840,5.753243,1.457432,5.691224,5.690497,1.421610,8.904590,-2.056786,-8.088697,7.172448,6.591645,0.311467,-9.140296,-7.246734,-1.310384,-9.798040,6.603134,-8.455489,1.168526,9.843295,-9.716170,7.843293,-4.405513,1.291361,0.674631,6.580748,4.886301,1.313233,8.311535,9.641314,-4.864013,-2.696562,7.899513,7.040999,-4.589820,8.206590,9.010318,-8.915710,-9.850038,-5.871389,-7.602987,-2.666871,5.275173,9.411998,9.709426,-1.089259,-7.171940,3.692030,3.262721,-3.158763,-4.519572,-5.535953,4.608715,9.389266,-9.050740,2.224222,-3.794708,1.330128,-9.786846,-1.643125,8.673184,3.726616,3.904442,-9.032852,8.651149,-3.808362,-4.561533,-0.880845,0.569504,-9.862729,4.009675,9.787486,9.024520,3.141521,0.171217,-3.767474,-6.396658,9.029792,-0.871776,-4.227608,-3.449510,2.639147,0.767048,-6.200119,-7.517422,2.129797,6.442730,4.845698,3.940607,-4.970857,-4.414096,9.091292,-0.232002,0.254312,-2.608663,0.377063,-5.907764,-7.175568,-8.220035,0.811351,4.767298,-5.161863,1.058436,9.575766,3.094400,2.013073,-3.569357,-7.058118,3.883074,-2.881782,-3.868979,4.443512,-3.423796,-2.842097,-9.326157,4.103394,-1.051390,-4.258144], dtype = "float64")#candidate|7227|(320,)|const|float64
const_7228 = relay.const([4.160971,0.132458,6.787035,1.279978,7.942010,-3.169694,8.598230,-1.028435,0.828238,-7.530371,-7.071065,3.564800,9.506863,-8.877591,-8.453590,0.398820,3.497190,1.792792,3.545023,5.689522,-6.897478,-0.553091,4.407654,-2.288738,7.131146,3.913011,-6.228921,7.273349,-2.634997,9.198257,-3.098591,1.435713,2.713982,-9.895180,7.073468,0.275946,-9.462047,2.332916,-4.181742,-4.421756,-9.993136,-0.459097,3.006167,-8.973902,7.855388,-7.441430,1.991006,6.086241,-9.789510,9.348157,-8.029783,-1.079690,-6.644855,-6.862151,7.805854,-9.755269,-6.809010,-8.975356,-5.076422,-1.280089,-6.298321,-7.471868,-2.070048,-9.719475,7.158535,-9.253650,-5.934511,-2.124625,-7.963978,-9.010122,-1.254082,8.968163,4.059514,-0.460666,-3.110141,0.837570,9.623101,-3.408041,-0.303431,-2.945476,-8.723569,0.966370,7.648164,6.279230,-9.400101,0.763020,6.958072,-9.621867,9.584007,-9.104739,6.245963,-2.055437,5.793323,-1.860712,-3.587356,-8.284677,1.923577,1.089770,2.317086,-9.337681,-0.634314,-4.039907,-9.703817,-3.822067,6.760119,7.222996,1.282401,0.600575,4.270704,-4.309993,3.554561,-7.863932,-5.211353,8.851650,2.208314,1.594234,-4.508996,4.200909,-6.760220,-1.799643,-5.187996,-9.494120,4.094860,7.145504,3.805358,-8.218156,-6.396852,0.513781,3.780678,-8.865061,-8.002580,-2.278699,-7.192091,4.081925,-7.782176,-3.786219,-0.723904,-6.513467,6.587595,-8.777642,2.886329,3.982829,5.032917], dtype = "float32")#candidate|7228|(143,)|const|float32
var_7229 = relay.var("var_7229", dtype = "uint32", shape = ())#candidate|7229|()|var|uint32
call_7226 = relay.TupleGetItem(func_3440_call(relay.reshape(const_7227.astype('float64'), [320,]), relay.reshape(const_7228.astype('float32'), [143,]), relay.reshape(var_7229.astype('uint32'), []), ), 7)
call_7230 = relay.TupleGetItem(func_3444_call(relay.reshape(const_7227.astype('float64'), [320,]), relay.reshape(const_7228.astype('float32'), [143,]), relay.reshape(var_7229.astype('uint32'), []), ), 7)
func_2083_call = mod.get_global_var('func_2083')
func_2088_call = mutated_mod.get_global_var('func_2088')
const_7238 = relay.const([[-8,1,-2],[-8,2,-3],[-4,3,10],[-8,-5,-5],[2,-7,-5],[-4,-5,-9],[-1,-10,-8],[5,5,10],[4,-6,8],[-5,1,-9],[-10,-9,7],[-6,5,-5],[-8,7,-10],[1,-6,-6],[-8,7,2],[8,-8,-1],[-7,7,-2],[4,-3,-5],[7,9,-3],[-10,-4,2],[4,2,-9],[10,7,-5],[-8,-8,10],[-3,9,2],[5,-3,-10],[8,7,9],[10,-1,5],[-5,4,5],[7,3,-10],[-8,-7,-5],[-7,5,1],[-9,3,10],[-5,4,-10],[-5,5,-5],[-3,9,3],[10,-4,-4],[-9,8,3],[4,2,-7],[-5,1,10],[-6,-8,-4],[-8,3,-1],[9,-1,4],[4,2,-3],[10,1,9],[-7,6,-9],[-6,-7,9],[5,-8,6],[10,9,7],[1,2,-1],[3,8,-3],[2,-4,-8],[4,2,2],[3,7,4],[-6,5,8],[10,4,-3],[-5,-6,-1],[-1,-8,9],[10,-3,-4],[2,3,9],[-3,-3,9],[6,10,-4],[-6,7,7],[-5,-6,3],[-5,-3,2],[10,-2,-4],[10,8,2],[10,-6,-4],[-1,-1,9],[-10,-1,-3],[-4,8,-7],[-1,-2,6],[1,-10,2],[-2,-4,1],[-7,10,-3],[-10,-7,5],[1,-2,4],[-5,-5,-2],[10,2,-4],[-9,-4,-8],[-3,4,-7],[5,-4,10],[-6,-1,-1],[-10,4,9],[4,1,-9],[5,-9,2],[-5,-5,4],[6,-10,5],[-7,-4,-6],[1,3,8],[-2,3,-1],[7,-2,4],[8,7,7],[1,8,7],[8,-4,1],[-4,4,-4],[2,10,6],[9,-5,1],[-2,-6,-8],[2,2,-1],[-9,-5,2],[-7,-3,-8],[2,2,-8],[9,-7,-8],[-9,-3,8],[3,-8,-10],[8,-3,-4],[-9,-10,2],[-3,-6,8],[-5,6,-6],[-3,2,7],[-10,-9,5],[7,8,2],[5,-2,8],[-7,-7,-1],[9,-1,-5],[-3,3,-1],[-5,-2,-4],[-4,-2,10],[-8,-2,-1],[-7,-9,3],[9,1,10],[-2,-8,10],[1,-3,-2],[-4,1,5],[-1,4,3],[5,3,-3],[8,8,2],[-10,-1,5],[-7,6,-6],[-1,3,8],[5,7,-9],[-3,-8,3],[-8,-10,-5],[4,7,-1],[1,10,9],[10,-9,-2],[-7,-5,5],[-2,10,-1],[10,-8,-5],[10,3,10],[5,-4,4],[5,2,-6],[-6,9,4],[-5,-5,-1],[-4,-6,8],[6,5,2],[-9,-3,-4],[5,9,8],[-6,-6,-5],[-1,8,3],[3,-3,-1],[-10,-9,1],[-9,-5,-2],[2,7,-9],[6,3,-9],[-2,-8,-3],[-10,-1,-3],[4,9,-2],[6,9,1],[8,-9,-1],[-7,-3,8],[8,-8,-8],[-1,6,-4],[3,2,3],[-1,3,2],[-8,-7,-8],[6,6,2],[6,-8,5],[1,-4,-1],[8,-10,2],[5,2,1],[-10,5,1],[-9,3,9],[9,-6,-5],[-10,7,-4],[-1,-8,-2],[3,6,-7],[5,5,-3],[-6,6,-3],[-8,-4,4],[-5,8,8],[-4,3,10],[10,5,-5],[-2,1,4],[-7,-9,-1],[-10,8,2],[9,8,10],[1,5,-5],[-6,-3,5],[1,2,-4],[2,9,-3],[5,-9,-3],[1,8,3],[6,2,-6],[-7,-10,6],[-3,-9,6],[7,3,4],[-6,-3,-3]], dtype = "int16")#candidate|7238|(198, 3)|const|int16
call_7237 = relay.TupleGetItem(func_2083_call(relay.reshape(const_7238.astype('int16'), [11, 6, 9]), relay.reshape(const_7238.astype('int16'), [11, 6, 9]), relay.reshape(const_7238.astype('int16'), [11, 6, 9]), ), 2)
call_7239 = relay.TupleGetItem(func_2088_call(relay.reshape(const_7238.astype('int16'), [11, 6, 9]), relay.reshape(const_7238.astype('int16'), [11, 6, 9]), relay.reshape(const_7238.astype('int16'), [11, 6, 9]), ), 2)
uop_7244 = relay.acos(call_7237.astype('float64')) # shape=(11, 6, 9)
uop_7246 = relay.acos(call_7239.astype('float64')) # shape=(11, 6, 9)
func_5576_call = mod.get_global_var('func_5576')
func_5580_call = mutated_mod.get_global_var('func_5580')
var_7251 = relay.var("var_7251", dtype = "int32", shape = (30,))#candidate|7251|(30,)|var|int32
const_7252 = relay.const([6.318957,-8.047092,-0.926705,-9.041661,-7.097911,-7.261337,2.283193,-3.357078,-8.839775,-0.584664,8.314206,6.591424,-7.859948,-0.698287,-5.049163,4.556322,7.106210,5.905318,-0.446360,-2.149118,-8.173768,8.010854,5.655582,-4.359510,-7.702090,-1.048328,4.743825,7.450964,-9.369126,3.382245,6.086699,9.228224,-8.578290,-8.901724,-2.420883,7.406894,5.487074,-8.479594,2.212918,-8.033041,5.025678,0.685969,5.718928,2.713951,-0.433564,-6.784471,3.901404,3.036622,4.194553,-2.025569,-5.310786,-0.038759,-6.902254,-0.455804,7.211278,7.281880,9.025485,1.496309,1.527008,-7.570907,-4.377459,-0.031398,-4.030062,2.807505,0.033740,1.655055,-2.487182,-7.068432,-9.527871,-1.040847,6.130333,1.190915,-9.558350,8.762369,5.836000,-1.159807,0.676064,4.704407,-4.978370,1.802732,-8.349253,3.693860,-1.278587,-6.157318,-0.703743,-0.060868,-6.069314,-6.777641,-3.270362,4.336204,2.100019,5.647989,-4.579717,2.366236,-3.653896,-0.130428,5.156189,6.519944,1.330205,8.920947,-7.738522,-9.524041,3.079209,7.513933,-2.323267,1.470509,-5.681791,-1.085610,7.227171,9.467719,-7.375780,-9.081448,1.779885,8.420630,5.220608,-6.387280,-6.871360,0.602797,3.335795,-4.435734,9.128873,-9.858811,-1.526336,-6.234044,-9.529165,2.081040,1.306955,-5.275011,1.923805,-4.269681,-5.039331,-1.549865,5.734248,-3.104920,0.418292,-9.777544,-6.857938,-4.211753,-0.808446,-2.455084,9.897894,6.794165,-0.791752,8.935540,-8.396977,-1.195525,3.474252,5.499335,-8.706807,2.234989,-5.692064,-4.562546,-8.245235,-7.652788,6.698007,0.151518,-4.714824,-5.834993,7.230489,9.830294,1.795035,-1.047744,-8.178058,0.892703,-6.269978,-4.125927,-9.993747,5.422071,-4.415322,8.415632,7.094833,-8.742486,-6.269508,-6.056019,-8.477212,5.918585,0.900649,-0.337641,8.394573,7.879448,3.733405,1.515878,-5.628228,-4.838988,-2.454834,8.648388,6.103125,2.902395,-6.056004,1.405589,9.632080,-6.852103,-4.312485,9.642749,-6.936896,3.514643,-8.329499,6.249586,-6.424227,6.760000,-5.445058,-0.171421,-2.971263,3.102992,8.568556,-4.286434,8.578619,6.300767,4.310002,9.053774,8.117657,4.937336,3.453017,4.864773,3.045766,-8.918832,1.347836,7.465738,7.904790,-6.137788,9.201735,2.259915,2.614782,-1.783000,0.773494,-4.574561,8.684213,8.069612,-8.213623,-4.146126,1.539167,5.073683,7.160828,7.883621,2.386740,2.543768,-5.081963,9.259583,2.894634,-0.760950,-3.872072,-1.674797,6.849517,-2.264830,-2.967139,4.641683,-1.469523,-5.502792,4.178811,-5.144912,1.527183,7.331466,-7.042409,5.526536,-6.827089,3.607346,-3.815474,-7.029519,0.459064,5.336056,8.738714,8.124382,-2.229973,6.912157,0.417725,-7.383334,1.668719,-5.333167,1.486163,-4.113290,-3.741376,-6.161451,7.048184,-1.887591,9.526732,-3.711428,-0.226788,-0.315127,1.791281,-1.867491,3.506761,2.991534,-9.662501,3.991278,8.895918,6.574946,4.151919,-8.328059,3.573736,1.219388,-2.834435,0.020476,2.670926,5.435732,-1.997765,-5.956419,0.656859,-1.167774,8.141118,0.559660], dtype = "float64")#candidate|7252|(300,)|const|float64
call_7250 = relay.TupleGetItem(func_5576_call(relay.reshape(var_7251.astype('int32'), [1, 30]), relay.reshape(const_7252.astype('float64'), [300,]), ), 6)
call_7253 = relay.TupleGetItem(func_5580_call(relay.reshape(var_7251.astype('int32'), [1, 30]), relay.reshape(const_7252.astype('float64'), [300,]), ), 6)
func_5900_call = mod.get_global_var('func_5900')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_7256 = relay.TupleGetItem(func_5900_call(), 0)
call_7257 = relay.TupleGetItem(func_5901_call(), 0)
func_3396_call = mod.get_global_var('func_3396')
func_3400_call = mutated_mod.get_global_var('func_3400')
const_7270 = relay.const([-4,-10,10,-10,-1,4,-1,9,2,-4,10,-10,3,-4,-10,6,7,3,-3,4,7,-10,-1,-4,10,1,-9,1,-2,-2,7,-6,-3,4,4,-9,-6,-9,-9,-9,4,-9,10,6,6,-6,-5,9,-1,-5,-1,-8,-7,-3,4,5,1,-1,-5,-4,-7,4,-3,2,-6,-3,-5,-3,9,-9,9,1,10,-2,8,-6,6,-9,-4,5,9,-6,-8,-9,6,-10,-5,-4,10,10,10,5,7,-7,4,-1,-7,-1,8,1,-1,-9,-1,-9,-7,-1,4,-4,-1,-10,-2,-9,-1,-3,-2,3,5,-8,-4,-7,6,9,5,1,-4,-10,5,5,-2,5,3,7,-1,-4,4,6,-1,-1,8,-2,-2,-9,6,3,2,-1,-5,3,-5,-10,10,8,3,-8,1,3,4,2,-8,7,-2,-7,9,4,-8,-3,-2,-8,10,6,-7,7,-3,-1,-2,2,-9,1,-8,-1,9,5,-5,-6,2,-6,-3,10,2,6,2,-7,9,-8,-5,5,3,7,4,2,-7,5,-1,-5,-8,6,3,2,5,8,1,6,-3,1,-10,7,9,-7,-9,-5,7,9,-7,9,3,4,1,9,4,-5,-10,2,-4,-2,-5,-10,-8,-10,1,9,-7,9,4,5,-5,4,3,-5,-9,8,3,4,-8,-8,-4,-3,3,-10,-10,-7,-5,2,-1,5,-5,-1,2,2,2,8,-9,8,5,-9,2,1,8,-7,2,8,4,6,7,-5,7,2,4,-8,-7,-3,-2,8,10,1], dtype = "int16")#candidate|7270|(294,)|const|int16
call_7269 = relay.TupleGetItem(func_3396_call(relay.reshape(var_7229.astype('int16'), []), relay.reshape(const_7270.astype('int16'), [3, 7, 14]), ), 2)
call_7271 = relay.TupleGetItem(func_3400_call(relay.reshape(var_7229.astype('int16'), []), relay.reshape(const_7270.astype('int16'), [3, 7, 14]), ), 2)
func_3562_call = mod.get_global_var('func_3562')
func_3564_call = mutated_mod.get_global_var('func_3564')
const_7278 = relay.const([-10,-6,-8,-4,3,-1,-7,-5,1,5,-6,7,5,6,-5,-7,1,-4,10,-6,-5,-1,-4,-5,10,10,-4,8,2,1,-10,4,2,10,7,-4,1,-7,4,3,-1,9,-9,7,2,-1,-6,6,3,9,2,-6,-1,-1,4,8,-8,-1,8,8,-7,4,4,-1,-6,10,-6,-2,-7,3,-8,7,1,-10,-7,9,-7,-9,-3,-9], dtype = "uint8")#candidate|7278|(80,)|const|uint8
call_7277 = relay.TupleGetItem(func_3562_call(relay.reshape(const_7278.astype('uint8'), [8, 2, 5])), 0)
call_7279 = relay.TupleGetItem(func_3564_call(relay.reshape(const_7278.astype('uint8'), [8, 2, 5])), 0)
output = relay.Tuple([call_7223,call_7226,const_7227,const_7228,var_7229,const_7238,uop_7244,call_7250,var_7251,const_7252,call_7256,call_7269,const_7270,call_7277,const_7278,])
output2 = relay.Tuple([call_7224,call_7230,const_7227,const_7228,var_7229,const_7238,uop_7246,call_7253,var_7251,const_7252,call_7257,call_7271,const_7270,call_7279,const_7278,])
func_7293 = relay.Function([var_7229,var_7251,], output)
mod['func_7293'] = func_7293
mod = relay.transform.InferType()(mod)
var_7294 = relay.var("var_7294", dtype = "uint32", shape = ())#candidate|7294|()|var|uint32
var_7295 = relay.var("var_7295", dtype = "int32", shape = (30,))#candidate|7295|(30,)|var|int32
output = func_7293(var_7294,var_7295,)
func_7296 = relay.Function([var_7294,var_7295,], output)
mutated_mod['func_7296'] = func_7296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4049_call = mod.get_global_var('func_4049')
func_4050_call = mutated_mod.get_global_var('func_4050')
call_7300 = relay.TupleGetItem(func_4049_call(), 0)
call_7301 = relay.TupleGetItem(func_4050_call(), 0)
func_4684_call = mod.get_global_var('func_4684')
func_4685_call = mutated_mod.get_global_var('func_4685')
call_7305 = relay.TupleGetItem(func_4684_call(), 0)
call_7306 = relay.TupleGetItem(func_4685_call(), 0)
output = relay.Tuple([call_7300,call_7305,])
output2 = relay.Tuple([call_7301,call_7306,])
func_7308 = relay.Function([], output)
mod['func_7308'] = func_7308
mod = relay.transform.InferType()(mod)
output = func_7308()
func_7309 = relay.Function([], output)
mutated_mod['func_7309'] = func_7309
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7402 = relay.var("var_7402", dtype = "int8", shape = (8, 1, 6))#candidate|7402|(8, 1, 6)|var|int8
const_7403 = relay.const([[[10,-2,-3,5,10,-2],[-6,10,7,8,10,-3]],[[-4,-10,-4,10,-10,-2],[1,8,3,-8,2,-1]],[[-2,2,-2,4,-4,8],[-3,-1,9,5,-1,1]],[[-3,-4,-7,-6,3,-2],[5,-3,-10,-8,-9,5]],[[10,-8,-3,6,-10,-2],[5,-7,-8,-5,6,-1]],[[-9,9,-7,6,6,-10],[-4,6,-5,2,-8,8]],[[9,6,-1,2,-5,-8],[7,10,9,-4,-6,-1]],[[-3,-1,-2,-7,-4,6],[2,-7,-1,1,-10,-3]]], dtype = "int8")#candidate|7403|(8, 2, 6)|const|int8
bop_7404 = relay.left_shift(var_7402.astype('int8'), const_7403.astype('int8')) # shape=(8, 2, 6)
func_4492_call = mod.get_global_var('func_4492')
func_4493_call = mutated_mod.get_global_var('func_4493')
call_7407 = relay.TupleGetItem(func_4492_call(), 0)
call_7408 = relay.TupleGetItem(func_4493_call(), 0)
bop_7418 = relay.add(bop_7404.astype('int8'), relay.reshape(const_7403.astype('int8'), relay.shape_of(bop_7404))) # shape=(8, 2, 6)
output = relay.Tuple([call_7407,bop_7418,])
output2 = relay.Tuple([call_7408,bop_7418,])
func_7428 = relay.Function([var_7402,], output)
mod['func_7428'] = func_7428
mod = relay.transform.InferType()(mod)
mutated_mod['func_7428'] = func_7428
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7429 = relay.var("var_7429", dtype = "int8", shape = (8, 1, 6))#candidate|7429|(8, 1, 6)|var|int8
func_7428_call = mutated_mod.get_global_var('func_7428')
call_7430 = func_7428_call(var_7429)
output = call_7430
func_7431 = relay.Function([var_7429], output)
mutated_mod['func_7431'] = func_7431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4708_call = mod.get_global_var('func_4708')
func_4709_call = mutated_mod.get_global_var('func_4709')
call_7443 = relay.TupleGetItem(func_4708_call(), 0)
call_7444 = relay.TupleGetItem(func_4709_call(), 0)
func_1888_call = mod.get_global_var('func_1888')
func_1891_call = mutated_mod.get_global_var('func_1891')
var_7452 = relay.var("var_7452", dtype = "float64", shape = (128,))#candidate|7452|(128,)|var|float64
call_7451 = relay.TupleGetItem(func_1888_call(relay.reshape(var_7452.astype('float64'), [2, 8, 8]), relay.reshape(var_7452.astype('float64'), [2, 8, 8]), ), 0)
call_7453 = relay.TupleGetItem(func_1891_call(relay.reshape(var_7452.astype('float64'), [2, 8, 8]), relay.reshape(var_7452.astype('float64'), [2, 8, 8]), ), 0)
output = relay.Tuple([call_7443,call_7451,var_7452,])
output2 = relay.Tuple([call_7444,call_7453,var_7452,])
func_7469 = relay.Function([var_7452,], output)
mod['func_7469'] = func_7469
mod = relay.transform.InferType()(mod)
mutated_mod['func_7469'] = func_7469
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7470 = relay.var("var_7470", dtype = "float64", shape = (128,))#candidate|7470|(128,)|var|float64
func_7469_call = mutated_mod.get_global_var('func_7469')
call_7471 = func_7469_call(var_7470)
output = call_7471
func_7472 = relay.Function([var_7470], output)
mutated_mod['func_7472'] = func_7472
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5488_call = mod.get_global_var('func_5488')
func_5489_call = mutated_mod.get_global_var('func_5489')
call_7503 = func_5488_call()
call_7504 = func_5488_call()
uop_7508 = relay.exp(call_7503.astype('float32')) # shape=(7, 3, 7)
uop_7510 = relay.exp(call_7504.astype('float32')) # shape=(7, 3, 7)
output = relay.Tuple([uop_7508,])
output2 = relay.Tuple([uop_7510,])
func_7513 = relay.Function([], output)
mod['func_7513'] = func_7513
mod = relay.transform.InferType()(mod)
output = func_7513()
func_7514 = relay.Function([], output)
mutated_mod['func_7514'] = func_7514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5476_call = mod.get_global_var('func_5476')
func_5477_call = mutated_mod.get_global_var('func_5477')
call_7618 = relay.TupleGetItem(func_5476_call(), 0)
call_7619 = relay.TupleGetItem(func_5477_call(), 0)
output = relay.Tuple([call_7618,])
output2 = relay.Tuple([call_7619,])
func_7644 = relay.Function([], output)
mod['func_7644'] = func_7644
mod = relay.transform.InferType()(mod)
output = func_7644()
func_7645 = relay.Function([], output)
mutated_mod['func_7645'] = func_7645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3158_call = mod.get_global_var('func_3158')
func_3160_call = mutated_mod.get_global_var('func_3160')
call_7646 = relay.TupleGetItem(func_3158_call(), 1)
call_7647 = relay.TupleGetItem(func_3160_call(), 1)
func_765_call = mod.get_global_var('func_765')
func_768_call = mutated_mod.get_global_var('func_768')
var_7651 = relay.var("var_7651", dtype = "int64", shape = (525,))#candidate|7651|(525,)|var|int64
const_7652 = relay.const(8, dtype = "uint32")#candidate|7652|()|const|uint32
call_7650 = relay.TupleGetItem(func_765_call(relay.reshape(var_7651.astype('int64'), [7, 15, 5]), relay.reshape(const_7652.astype('uint32'), []), ), 3)
call_7653 = relay.TupleGetItem(func_768_call(relay.reshape(var_7651.astype('int64'), [7, 15, 5]), relay.reshape(const_7652.astype('uint32'), []), ), 3)
func_765_call = mod.get_global_var('func_765')
func_768_call = mutated_mod.get_global_var('func_768')
call_7654 = relay.TupleGetItem(func_765_call(relay.reshape(var_7651.astype('int64'), [7, 15, 5]), relay.reshape(const_7652.astype('uint32'), []), ), 4)
call_7655 = relay.TupleGetItem(func_768_call(relay.reshape(var_7651.astype('int64'), [7, 15, 5]), relay.reshape(const_7652.astype('uint32'), []), ), 4)
output = relay.Tuple([call_7646,call_7650,var_7651,const_7652,call_7654,])
output2 = relay.Tuple([call_7647,call_7653,var_7651,const_7652,call_7655,])
func_7665 = relay.Function([var_7651,], output)
mod['func_7665'] = func_7665
mod = relay.transform.InferType()(mod)
var_7666 = relay.var("var_7666", dtype = "int64", shape = (525,))#candidate|7666|(525,)|var|int64
output = func_7665(var_7666)
func_7667 = relay.Function([var_7666], output)
mutated_mod['func_7667'] = func_7667
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4684_call = mod.get_global_var('func_4684')
func_4685_call = mutated_mod.get_global_var('func_4685')
call_7669 = relay.TupleGetItem(func_4684_call(), 0)
call_7670 = relay.TupleGetItem(func_4685_call(), 0)
output = relay.Tuple([call_7669,])
output2 = relay.Tuple([call_7670,])
func_7675 = relay.Function([], output)
mod['func_7675'] = func_7675
mod = relay.transform.InferType()(mod)
output = func_7675()
func_7676 = relay.Function([], output)
mutated_mod['func_7676'] = func_7676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3158_call = mod.get_global_var('func_3158')
func_3160_call = mutated_mod.get_global_var('func_3160')
call_7726 = relay.TupleGetItem(func_3158_call(), 0)
call_7727 = relay.TupleGetItem(func_3160_call(), 0)
func_5576_call = mod.get_global_var('func_5576')
func_5580_call = mutated_mod.get_global_var('func_5580')
const_7732 = relay.const([8,2,-10,10,-3,-1,2,-7,3,2,-2,-6,7,-9,10,-7,1,-6,10,-1,4,1,5,-9,-6,6,8,-4,-1,-1], dtype = "int32")#candidate|7732|(30,)|const|int32
var_7733 = relay.var("var_7733", dtype = "float64", shape = (300,))#candidate|7733|(300,)|var|float64
call_7731 = relay.TupleGetItem(func_5576_call(relay.reshape(const_7732.astype('int32'), [1, 30]), relay.reshape(var_7733.astype('float64'), [300,]), ), 6)
call_7734 = relay.TupleGetItem(func_5580_call(relay.reshape(const_7732.astype('int32'), [1, 30]), relay.reshape(var_7733.astype('float64'), [300,]), ), 6)
output = relay.Tuple([call_7726,call_7731,const_7732,var_7733,])
output2 = relay.Tuple([call_7727,call_7734,const_7732,var_7733,])
func_7744 = relay.Function([var_7733,], output)
mod['func_7744'] = func_7744
mod = relay.transform.InferType()(mod)
var_7745 = relay.var("var_7745", dtype = "float64", shape = (300,))#candidate|7745|(300,)|var|float64
output = func_7744(var_7745)
func_7746 = relay.Function([var_7745], output)
mutated_mod['func_7746'] = func_7746
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7793 = relay.var("var_7793", dtype = "float64", shape = (16, 15, 13))#candidate|7793|(16, 15, 13)|var|float64
const_7794 = relay.const([[[4.169019,-2.585320,4.277948,-0.609661,-3.237297,-5.729796,-8.545764,3.785759,-0.414720,8.934637,0.721745,-8.526731,-8.608167],[-3.115043,4.210515,4.869450,-1.038014,0.926348,6.560715,8.940398,4.698963,-5.474947,-1.090358,-9.064440,-0.854235,-9.766616],[0.514898,-8.634224,-7.219152,-7.119793,3.367515,-2.290303,2.920212,7.888602,1.754166,-7.828382,9.359728,-7.140223,7.526760],[-6.594001,-6.018398,4.437038,-4.472317,5.009619,-2.656672,-1.034814,3.186066,8.522128,2.324665,-2.020792,-9.079673,7.268338],[7.319346,5.172189,-4.315275,-2.245731,-4.522058,7.904770,-5.788987,3.986832,-6.545506,-8.008491,-3.879595,-8.259401,-2.950287],[-8.690177,3.056869,-0.467291,7.168075,0.233631,-7.453307,-4.796871,-0.075322,6.777422,7.521549,5.730867,-3.883942,8.776036],[-6.804671,-7.906369,-5.283069,3.615663,-8.730405,-6.839589,8.884815,-1.632438,-5.049418,6.815105,-9.402952,3.883660,8.787573],[1.405875,-0.245941,9.074828,-5.874894,7.449994,-1.963668,-0.976198,7.650522,3.654197,3.269589,-4.174635,-2.525615,-9.434924],[-6.345114,-8.567588,-6.415004,1.088020,1.095774,3.521941,4.181955,-6.943162,5.580305,-7.687192,-5.882893,-0.614464,0.461020],[4.971154,-8.598518,-8.224696,7.209752,-6.973922,-7.095375,-3.857201,-6.812096,1.093173,-9.816506,-2.681337,2.810234,-1.346850],[-8.822920,6.008542,8.745579,3.668814,-9.208900,-5.771214,1.610897,0.287999,5.024457,6.899715,-0.555109,2.877242,-4.475085],[-8.827410,-6.656581,1.018249,8.423543,2.477791,9.563448,-2.040762,-4.819827,5.730800,-9.578763,-2.868254,-4.855119,5.491153],[-9.089422,-1.954800,-8.921016,-2.181017,5.170081,8.849773,-8.388710,-7.774267,-5.796312,7.354380,4.653302,-9.716367,-5.218786],[3.380218,-3.190700,5.466929,2.296588,9.137501,-6.290442,9.420825,-5.828638,1.047251,2.342796,-3.053062,-2.377346,-5.919510],[7.588884,3.507229,3.752405,-8.565393,-9.606209,8.860690,7.739913,2.372409,-1.765815,-5.053040,-0.625912,-5.511202,3.510016]],[[6.637580,-3.821546,9.405648,-7.464229,6.199116,-1.835985,0.505250,8.195173,-7.109494,1.153928,4.535318,-4.348937,-5.136608],[1.218042,-3.696948,-4.235867,-9.806095,-0.364859,-2.715092,3.692330,-1.259039,7.652848,-1.005566,-5.067806,-1.311076,-1.338410],[-1.389599,9.072178,0.130390,3.833274,3.479609,6.942032,-1.980033,6.647554,-7.831824,2.202193,-7.427158,-8.564899,0.707179],[-0.724570,9.686675,7.025910,4.783442,-0.575395,7.974003,2.644470,9.666786,8.240529,-3.351082,-5.646659,3.592704,9.862584],[2.772976,-9.717221,5.387679,-0.547739,0.494324,-9.581002,-5.459195,-4.809927,-1.160687,-6.881592,-6.431119,0.927379,-9.557881],[-9.149584,0.819084,-8.196455,1.106688,-4.784996,5.990391,4.260842,-0.916892,8.874838,2.304912,6.815488,2.405009,9.490716],[5.119233,-2.528121,0.167951,5.756672,3.969370,2.314828,-5.004252,2.689736,-5.933421,-7.636709,-6.239121,6.151512,6.053434],[1.792581,-9.874780,1.457979,4.273097,5.129292,-6.839575,-7.971066,-5.112129,-8.800612,3.534620,-1.349914,2.731268,-2.840474],[9.484125,9.131417,-7.815899,0.619675,7.775749,-8.546888,6.007154,2.378467,-8.995919,6.846529,5.436078,1.170860,9.477302],[-1.535414,1.910525,-2.448722,-4.847468,5.878081,-8.013800,1.694764,7.343877,-3.815907,-8.008480,-0.354119,5.441066,5.650927],[-2.633465,6.523178,9.435023,-8.904953,5.160832,0.944144,-9.319269,-2.506933,8.486468,-0.881248,-1.666043,0.895308,1.851578],[5.634548,8.003040,3.988033,-8.415524,6.973646,2.607267,-2.119547,-9.782341,-2.300613,-1.088290,7.927290,8.492800,3.764996],[2.285597,-8.091592,-8.157622,2.873539,-7.154120,4.814639,-9.049417,-8.597466,-8.697753,-2.408186,-5.000392,5.678111,8.367370],[0.475239,4.717522,-8.517608,2.569344,5.877978,9.359237,-6.004527,9.647571,-6.431610,-2.343111,3.636903,2.564511,-3.317706],[1.291185,-8.731285,-8.924347,3.647796,-8.195516,-2.331351,-0.983602,-3.662264,7.270597,5.904178,-4.408532,-7.206179,7.323645]],[[-3.481596,4.266945,-7.329659,-5.374717,9.136028,-7.214493,-3.071274,5.788278,4.467345,-4.393290,4.760400,-8.806091,8.690610],[-6.954958,5.867449,4.762383,-1.115424,-6.597250,8.826540,6.531849,-3.892771,4.715128,6.454499,1.530934,-8.494180,-7.902893],[2.462094,0.043693,2.997588,-2.302548,5.898492,-6.417038,-7.154462,-9.312295,-0.097203,6.219219,-6.137702,0.787904,7.989521],[-2.586651,2.644125,8.711623,8.923749,3.443539,-9.415007,6.349411,9.335567,0.082755,0.208752,-1.831885,6.949868,-5.912569],[-9.549794,5.354844,-4.183117,-7.302546,-1.081763,4.151254,-6.663718,3.304085,-7.454235,-1.055098,-0.764323,-8.116392,7.161124],[6.612909,-3.795734,-9.432583,-4.133410,-2.024170,5.222046,-4.392250,-3.919585,1.916423,-4.822631,4.645635,-1.883530,-8.906611],[8.085227,-5.236168,7.023444,0.529783,6.736806,8.892301,-2.641159,-5.293961,-0.234359,0.522112,-6.295522,7.698827,1.732900],[-9.220540,-4.763906,7.429691,2.320053,-3.325577,4.907988,-3.520435,-2.099764,-9.338222,5.114952,-6.497310,0.695872,-9.198701],[3.161667,-1.965789,-6.220728,-4.588418,-2.909501,-2.118782,6.533831,-4.974064,-4.029501,7.260353,-0.769909,9.322992,-0.263080],[9.710885,-5.462647,-7.802442,6.376705,-1.150616,2.889962,-9.559640,-9.204124,3.214420,-3.260055,5.266365,-3.701904,3.909802],[-1.464135,-9.938034,-8.832856,5.002928,1.419164,-1.551135,-0.377076,-2.008658,5.926563,6.505513,3.207037,2.263287,5.869004],[-8.810877,8.533976,-1.226343,7.959714,5.213439,5.083345,-6.197519,-1.288984,0.449011,4.269277,-6.989268,4.599171,9.807576],[-9.633263,-6.147601,0.566052,4.125381,-2.171864,-4.538738,-8.934274,8.392046,-1.411021,-5.565145,6.045133,-0.721367,2.601373],[8.095743,-1.387587,0.960479,-3.735206,-6.535748,-7.210117,-4.806226,-0.694625,-8.024669,-3.020253,-8.744838,0.894728,8.674061],[-1.154481,-6.218544,-4.858553,-8.884562,-2.636795,7.317678,0.858284,-2.952769,1.008969,-1.370782,6.183235,-2.003203,6.283405]],[[2.100102,9.554154,9.706630,-6.959099,1.601080,6.371059,8.166179,0.631153,-0.288353,7.683566,7.183070,-6.184606,-0.113198],[-1.529538,5.362687,5.803064,6.849861,-7.195172,-4.492581,-7.146041,0.733085,-7.874042,2.398007,-3.879238,-0.664831,-6.394383],[-0.777547,-1.155590,-3.861899,-0.994745,-1.449673,-4.720093,-0.579255,-1.005301,1.648641,3.090711,-4.620689,-2.701795,5.909229],[-6.077725,-4.695540,4.635791,7.309818,9.184117,7.960195,7.337570,9.866424,7.437141,-6.575632,-3.838710,-1.510773,2.956070],[8.828127,-6.232182,-9.376736,1.362550,5.023349,3.042490,-5.118392,-8.761030,-4.712030,6.535452,-4.487350,-2.668495,-5.769626],[-4.492068,-6.724105,5.994688,4.842428,-2.552244,-9.883028,-2.004094,9.747551,-8.370692,-1.040953,4.465444,0.483442,-5.566613],[1.606148,-3.112888,-0.845238,-7.340062,-7.430327,-4.035439,2.533184,2.040338,-0.415377,8.358005,-5.646913,7.091005,-3.560557],[6.806036,3.114997,1.352896,-2.050805,-1.453233,3.065088,6.401522,2.983215,1.206230,7.184168,-9.416620,8.493204,8.823933],[-3.857160,-9.269485,1.652200,-4.398503,-9.888828,6.747296,4.281331,1.580583,-2.482961,9.303059,-6.002003,-3.660015,7.934451],[-3.508910,-5.355434,-4.435140,-7.271768,0.032765,7.650645,5.354800,-0.723806,-1.534447,-2.431803,-6.617521,1.832727,-4.680746],[-3.318245,9.059469,-8.856900,-0.543020,5.654152,0.120483,-9.113722,5.016847,-6.043455,4.373683,3.229738,-1.482836,0.958444],[-1.403163,-7.671823,-8.175682,0.093964,9.744574,6.694182,-0.105214,-7.495370,2.209731,-8.315830,-9.479269,7.906711,4.425569],[-6.883253,-7.634601,-5.602271,-6.193095,-5.031128,-0.050570,-2.462819,4.015306,4.285138,-1.412137,0.789037,-1.542102,-7.337488],[-2.948895,-9.400684,-7.947981,4.410442,-9.716958,4.156814,9.433720,-5.196734,8.202600,6.645900,-4.433420,-0.171480,-0.879463],[-8.017465,4.465432,-7.351351,-1.222424,-1.364807,4.794615,-8.614886,5.991059,-6.702357,0.132548,-6.873616,4.026599,6.198433]],[[8.386257,-0.268662,5.276564,-0.405299,6.882964,-1.430726,-7.402367,-1.788891,-0.092595,0.326479,-9.107301,-8.226241,-0.368296],[-7.069466,-9.989775,-8.802513,2.678054,-9.445989,5.682206,9.495706,1.901491,5.548027,-0.889505,8.910274,-0.915427,1.073154],[-6.206391,-1.059381,-7.498437,-8.047443,-1.246494,-2.467822,7.676136,-5.727961,-9.329049,7.619725,6.015053,4.641382,-4.203785],[-1.349262,5.957632,9.998951,-7.652320,0.546959,-8.110770,0.181246,-7.818338,-5.676901,-0.461849,-7.634271,-1.155230,-8.081828],[-4.004759,-8.953056,-2.937664,4.932275,-2.159682,2.581728,-4.466487,7.960423,-8.324835,5.395012,4.589191,-3.702148,-4.538665],[-6.316717,-4.926522,-6.969220,-0.746958,5.688312,-2.521684,-7.518430,4.190600,3.766092,-7.508836,-8.867463,2.100522,6.093226],[9.000338,3.267002,8.423160,2.395597,-6.315637,-7.939252,-2.577774,-1.866581,7.609470,4.819989,-1.670607,-8.763994,7.779886],[-9.203872,1.961952,9.770109,8.274327,-6.232611,-5.408597,3.129628,-6.363712,8.845913,5.301091,0.777459,0.885804,-1.182386],[0.542413,-2.096138,8.471216,4.106762,8.617065,-6.782072,0.674102,2.389041,-1.512775,8.033939,-8.865258,7.383112,-5.928848],[-6.937422,0.992107,4.999779,-9.232350,0.570306,-3.894060,-6.351925,-2.702332,0.630761,3.928009,5.111267,9.687562,-7.644521],[-7.786360,5.229281,-8.484024,-2.309428,-6.942336,-9.092769,8.418278,3.346927,8.653599,2.752126,-5.184230,9.753205,5.566625],[6.737127,5.903140,6.214842,7.259666,-8.637963,-5.888515,1.619259,3.155032,7.544759,8.842231,-9.540784,-3.613346,-9.903520],[-7.228231,2.955180,0.707855,-1.553847,-2.643379,-3.065843,8.797161,-9.075957,0.617224,-0.965576,5.246407,3.570152,-2.495677],[5.502475,-8.575990,6.628656,-0.156320,-6.143505,4.688449,-1.718766,-0.914900,5.748401,-9.690125,-1.403643,6.681347,-3.429307],[-3.541821,-7.486644,5.307422,-1.950761,0.908582,2.210148,-5.041658,3.125254,-2.596514,4.306788,-7.419196,-6.100163,-2.826453]],[[-4.952972,-4.399158,4.096678,1.027735,2.075586,8.861897,-7.609556,-6.249338,-7.023079,3.350102,-2.212369,-4.934661,4.164091],[7.750993,5.745864,-1.570896,1.679953,-5.731135,9.312876,-2.864625,-2.988034,-6.171306,1.288937,-4.336202,4.710549,3.745772],[-0.931795,-7.638409,8.928519,5.222808,1.121329,-9.578789,-5.226204,6.239424,-3.361919,8.260282,-4.596416,8.852223,-4.033584],[1.207629,-9.266920,0.098471,-5.968203,-5.389096,4.368764,-8.079591,7.923090,-4.208720,1.344191,7.972450,6.104525,2.030688],[0.894346,7.005174,-6.031589,3.149994,-2.960949,6.204645,-2.660627,-8.215867,-6.756370,9.115958,3.061038,9.239209,0.040523],[3.217037,8.578735,-0.508023,4.283611,-9.625745,4.229532,-0.148525,0.379220,-6.001400,3.034412,7.693168,-2.389046,8.213166],[-6.941249,-8.803777,-2.708853,5.949497,-2.753971,-5.449664,5.299392,-3.543408,-9.251933,-9.210267,-9.338582,-6.749238,0.411922],[8.646811,-5.766385,-7.516864,-4.390902,-0.566870,-4.747220,-7.831447,-7.677142,-9.202599,-2.366462,-0.566346,-1.314145,-7.559259],[2.113436,-8.207437,-7.561317,-6.878314,5.668800,-5.255590,-8.340933,-5.534633,-0.584555,2.631533,4.994823,-3.227519,-1.474816],[-4.292122,-8.130789,-5.714795,3.093615,-8.462836,-3.931041,-0.130828,5.641341,9.159026,-6.131908,-4.078596,2.497498,8.212247],[-9.186684,-3.154977,-8.459433,5.229603,2.249553,-3.337174,-0.330657,-8.050992,-8.246352,-4.153344,2.441334,5.704680,8.185741],[-7.926851,9.667839,0.559159,-1.741148,5.621745,9.738273,8.267063,-8.414315,1.430032,-2.418057,8.431859,3.719042,5.438610],[-5.178621,-8.491459,-2.254280,-1.531054,-5.269293,1.750115,1.502714,3.593806,4.405403,7.512679,-3.064482,2.148316,-2.828103],[1.558468,-7.871857,1.386499,9.913662,8.717566,-8.305467,-3.731382,1.669009,3.417303,-9.949243,8.548270,6.800477,9.063483],[-9.621693,8.229446,7.517610,-0.262794,9.364426,-6.928210,1.603930,-4.571963,5.928587,-9.636522,8.836518,7.642961,-3.973332]],[[3.874062,3.360328,3.811113,7.498804,5.446550,-2.869686,0.639613,7.568196,-5.623370,8.691484,-1.335657,0.603390,9.641357],[9.944064,-7.930420,-5.754892,4.693339,-8.692523,5.618229,2.511979,4.484681,-7.895844,6.625705,-0.795527,-6.092847,8.507174],[3.147167,0.059115,7.739087,8.865642,-5.678499,3.507294,-7.535643,-0.387560,-7.067406,-8.777467,0.366238,-1.371495,-7.203345],[2.587119,-6.724784,4.798813,4.079003,-2.847072,6.697834,8.341038,7.934542,-0.134609,-4.553916,1.111187,-1.461504,-4.470636],[-4.271370,2.639033,-2.122689,3.625744,5.196558,-2.115112,5.481172,3.588571,-3.398114,-8.734522,8.793034,6.211849,-8.865117],[-8.079714,-1.596689,-7.487211,9.804094,5.607345,-5.365947,-1.947755,-6.761619,0.338780,-8.770517,-5.909405,1.479044,-0.822796],[3.679694,-4.467871,7.827548,1.902150,-3.788915,-3.493600,9.702716,2.501301,9.274188,3.045524,-0.185481,9.896552,6.096003],[9.701226,0.073923,9.447505,-4.378673,-7.814114,5.553589,8.379893,3.949470,9.723754,-8.567859,1.786439,8.270416,7.333629],[4.487076,-8.531568,-9.060247,3.152769,9.519051,4.043083,-8.753995,3.516245,3.368719,5.871346,6.952985,8.481442,0.224868],[4.940495,8.961707,-2.821498,0.755496,3.514160,2.925443,6.910220,5.213330,-7.140809,-0.566028,1.767707,-8.503295,1.012244],[-9.366975,7.037837,2.799532,-3.717739,5.004205,5.733307,3.049523,2.998165,1.409990,6.644903,2.980476,-5.075430,-9.515415],[7.342385,3.195530,-4.029745,8.954799,6.613701,-6.374929,3.325388,6.821574,-6.434855,5.191374,6.010388,5.037987,3.650418],[-4.769192,-0.122266,-1.453380,2.002103,-7.582240,8.226344,-5.369209,-6.717235,-9.051251,-5.294155,-3.236669,-9.108147,-3.999958],[-2.602703,-5.601058,-4.832270,-7.830785,2.882969,-9.271207,-6.190748,-5.221084,-5.116819,-6.736437,4.084196,-7.457884,-7.030667],[7.354757,-2.750821,-9.855008,9.406746,0.603255,3.391488,-9.473537,-9.888465,-7.631487,-4.649333,-1.694156,5.309755,0.667898]],[[5.577639,-3.852363,3.950221,-4.732898,-1.226771,-8.485305,2.951337,5.226536,0.200284,-5.183860,1.449671,-1.017284,1.543528],[-3.242259,-5.363254,-4.990544,-2.743061,6.856878,-1.664974,7.073655,2.490133,-3.884892,1.813823,5.439759,8.467670,-6.019722],[-1.126210,-0.205143,0.652223,-3.414006,5.607290,8.885313,-7.876601,8.662397,-8.786063,6.806235,-8.317868,7.335861,2.893777],[1.362457,-8.681191,9.324847,-0.867496,-0.504291,7.289311,5.966773,3.115111,-1.091208,-9.528169,-9.119386,-7.160935,-8.433751],[7.997057,2.328021,-8.285695,-5.809078,-0.929987,-2.460542,9.712009,7.033936,6.068805,7.933389,1.487956,-4.997809,6.055842],[5.815656,-4.492610,2.293811,2.464994,2.464055,4.990572,-8.795268,3.618452,-7.774031,3.742988,9.015927,6.753426,-7.020393],[-8.161667,-9.489211,3.490459,-1.363613,9.645009,-0.613073,-5.834170,-6.907829,2.457966,4.911622,5.593638,8.811394,8.072257],[-8.883879,-4.796771,-9.238729,2.060930,-7.695080,-5.498312,8.676695,-2.447924,-4.846584,2.917511,-4.817356,8.904599,3.446089],[-7.828347,1.963991,-6.603212,-7.392809,-4.294731,6.454008,9.325469,7.025308,-3.991915,1.976398,-6.079821,6.414778,-8.262425],[-9.365327,-4.456439,9.505217,-5.245687,-9.053711,-1.555533,2.710078,1.420833,-5.692836,1.891664,-1.027747,-9.334808,-2.913349],[3.144057,-2.416140,-9.663690,8.526875,7.234131,2.151916,-2.905786,-7.504579,-5.593430,5.855288,-3.195663,-2.003100,5.379011],[-3.740485,-1.456788,-4.646210,-3.233875,0.741653,5.641420,4.976999,9.069350,8.526803,8.524058,-0.268316,7.110641,0.086341],[-5.039101,3.644409,2.971894,5.017604,4.884711,8.606799,7.346597,-2.653394,-4.019196,5.334191,-4.838562,1.528631,-2.548915],[2.635342,9.880407,9.505969,-0.078320,-8.118067,-3.372739,7.586802,5.408745,-9.011218,7.340110,-3.349246,-2.418742,-1.936897],[-8.547074,-7.693979,3.127139,-0.076751,4.649631,-0.641347,1.954878,2.540029,1.621750,0.234380,8.572001,8.040038,-9.547309]],[[-6.830608,6.792482,1.111947,-1.881992,-1.552530,0.262566,7.202482,-4.049768,-0.238805,-7.402110,-3.482384,-2.982625,-0.248979],[8.065354,-6.325290,4.777951,-6.117985,5.623824,-9.283276,-2.872570,-1.122181,-8.443988,-4.089708,6.880320,-6.445995,-6.457264],[6.343238,-0.927065,-9.967343,3.215037,4.903514,-9.046724,0.207553,1.085755,1.741184,-7.700792,7.805308,8.777008,-0.192413],[-7.612622,-3.583099,3.582491,5.989423,-4.793361,0.242535,-6.728787,-4.828941,-1.952940,0.320722,-2.196183,4.984429,-1.064661],[9.225913,-7.279404,-4.334106,-0.607456,7.700399,8.483638,4.722691,2.893760,3.733625,6.215579,-6.844114,-5.050626,7.211437],[-5.368651,9.171089,4.417876,4.773177,-4.708093,-1.161772,-1.629722,-7.332562,-9.917198,2.357897,-0.796781,1.496888,7.732213],[-7.349485,9.293535,-6.832954,-4.818736,-1.522561,-6.255241,-5.853294,-1.321637,7.214173,-2.501378,-1.621072,3.667662,-5.740924],[-2.526431,0.090377,2.637976,2.988875,8.752743,4.118118,-4.874473,6.013043,7.234801,9.689539,-2.166533,-8.023666,4.654170],[3.575913,1.894239,-9.206632,5.749589,9.810274,5.690340,-6.377589,-4.102958,3.074270,6.004358,2.668395,-5.107036,-1.760300],[1.038523,1.436273,9.408245,0.616573,8.753284,7.613766,8.988366,4.387276,9.510238,3.751404,5.595487,-8.230547,1.610896],[3.355455,7.439332,-0.915447,3.015958,0.980537,-2.391911,7.007829,-6.405181,-8.605393,1.223410,6.059886,8.186839,-1.800501],[2.827143,-2.373025,-0.970195,-5.708417,6.529269,-8.356468,-5.565998,-5.829373,-3.478396,-0.800499,-6.864529,-3.771469,6.685246],[-5.138156,-3.925882,7.407133,-1.161974,-4.097606,-3.500413,-1.215174,7.537658,-9.182879,-4.467176,-1.323782,-7.247401,3.418733],[2.576168,-9.954181,9.629283,-9.502990,6.652468,4.796107,5.157375,-1.699641,-0.404105,6.518439,1.341448,-1.283615,-0.619234],[-8.983540,3.182943,2.471557,5.697354,4.825142,9.068692,-8.766270,-3.946183,-1.622443,1.975171,7.063230,6.575589,1.601991]],[[-0.865316,-9.694577,-6.368194,2.466141,-9.230897,-2.714463,-0.434231,7.812080,7.037316,-5.775047,4.481551,5.293881,1.535161],[1.739269,-3.855307,0.931824,-3.365988,7.059807,-8.375174,-6.662139,-8.899598,-6.160200,2.994689,-0.593688,0.471478,-4.291744],[4.265313,3.711340,-9.144369,7.734765,2.102847,1.559328,-6.104416,-9.128619,2.748858,1.386016,5.899242,-4.541667,8.254659],[-7.318446,4.428578,-7.983657,-7.706820,8.289904,-5.652418,3.974159,3.181544,8.012005,-0.822233,-6.230124,-2.750853,0.012620],[7.179301,-1.361836,-6.617065,7.726120,9.074730,-2.761614,2.952419,-8.325414,-3.698239,0.863699,-0.280122,7.941773,-2.687853],[-7.716373,2.438085,-2.307274,8.152888,-6.730088,8.886672,7.936808,9.488931,0.031686,2.734969,-8.900103,0.164821,4.806089],[-1.919130,-2.515854,-0.991445,9.396904,-1.043757,-7.632039,2.740965,4.954938,-4.232084,8.912683,-8.691718,-0.551334,6.017974],[7.177400,-9.191768,-7.774592,7.570374,6.239214,-2.903270,-0.078641,0.337609,-0.743966,0.188100,4.364496,6.471425,4.286264],[1.082610,3.484242,-8.256469,-1.078363,-0.009023,4.591372,6.127652,7.846428,7.657120,4.828407,3.072150,4.179772,7.756255],[-1.976949,-2.202502,1.064300,-7.450012,-5.804806,4.919281,3.181954,8.454038,-5.919932,-5.590553,-6.710261,0.363485,-3.685048],[-2.924585,4.338739,-7.738986,-0.433401,2.451212,4.737812,-8.353455,-1.738380,-5.008113,0.022732,-9.629051,-0.410222,-3.509372],[-7.019166,-2.674603,-6.981715,2.814716,8.157964,5.270608,-7.016818,4.075953,-2.917700,2.419910,4.572887,5.496465,8.115378],[-4.402145,-3.625514,5.056524,-0.142110,0.647015,-3.459820,-5.574854,-5.015734,9.856832,-3.143590,-4.380307,-8.871430,5.211303],[0.044406,5.952820,-0.440119,6.463140,-5.725267,-0.156182,-1.884795,8.980071,-7.061110,-4.277902,2.337711,2.318943,-7.791914],[0.908659,7.685336,2.513172,1.115568,5.475233,-9.244463,-0.259322,9.005859,-0.140297,-8.483133,-3.627464,2.112413,4.659460]],[[-7.325554,7.006178,3.565395,-8.089514,0.702110,2.978122,-8.469599,7.334150,0.885088,4.817704,-2.315243,8.567794,7.330945],[0.723154,-5.141275,9.490111,0.115056,-9.913359,9.943400,4.079274,-6.861535,1.984565,8.956151,4.698597,-7.451393,-5.510020],[-0.324620,0.697884,7.009040,8.034632,-3.319298,6.499172,4.366845,-3.228690,-6.930470,6.313281,-7.276349,7.689478,7.844129],[1.723206,2.095756,-9.596871,9.102404,8.992124,-7.449739,-5.214810,4.900578,-3.563169,4.440811,-2.177964,-6.540737,-6.566562],[-9.295164,0.522541,5.828497,-5.521119,-8.540781,-5.846010,-0.301968,-2.313851,-2.434748,7.180914,-5.133924,-4.693008,-0.124724],[1.474592,4.527418,-0.078054,6.689428,1.644303,-2.224449,6.601199,0.397278,-1.511962,0.883034,-6.574613,4.905168,-5.826176],[-6.122768,-5.180220,9.465865,0.067296,9.155902,-6.348466,5.965300,1.264733,0.155079,-3.520533,7.801298,8.285212,-5.718170],[-3.994307,1.833020,2.505884,-1.594022,2.279698,-7.326646,-0.940642,-4.971635,-0.672372,-6.014294,3.953126,7.550272,-3.246888],[-2.599070,0.298750,-6.255762,-4.962347,-1.216879,6.075256,1.210457,-8.891100,7.283756,-5.971479,-4.998956,-3.858067,-5.626651],[-4.817759,9.257315,-6.050520,-6.084934,-6.403379,-5.187688,5.943019,7.042751,0.234027,1.864283,-5.465997,-1.333861,-2.808500],[3.781514,0.822904,-0.288447,8.831375,3.285735,6.373717,-9.774662,-2.876031,-1.348276,6.089451,-1.418211,7.884511,8.972054],[-1.489779,-8.711015,-6.646963,0.239281,4.121361,9.855818,-0.112845,3.859788,5.566165,8.848485,-7.642360,9.056666,4.867877],[-9.650460,8.948441,-6.508140,6.213341,-2.365300,3.022473,9.254581,5.330210,3.409642,9.658003,3.121468,-5.235657,-2.891796],[-9.575487,3.001869,1.751939,-0.068238,0.114159,7.262524,2.641745,-9.378819,1.821475,-1.151895,-4.235423,-2.061421,-3.550173],[-9.504582,0.888948,0.128425,-3.050787,6.869328,-8.158754,-6.865246,0.422306,-3.872578,8.250867,3.182074,-0.502651,0.672459]],[[0.818352,1.119331,6.519296,4.683631,-0.422279,2.524713,0.910344,7.860344,-1.069398,4.931399,1.520946,9.193287,-3.488561],[6.861226,-9.491625,6.294349,3.746695,5.572386,3.163396,8.027532,8.670307,-1.504198,3.360857,-0.315388,-2.440120,9.274309],[5.051376,-3.083246,9.105882,-6.897478,7.662650,-2.166569,-2.287533,6.684269,-3.717775,-2.649337,2.649354,-9.994566,-4.503421],[5.535619,-8.757736,-3.491839,4.262984,1.591465,-1.978012,-1.679749,9.751395,-0.313283,-5.058009,2.910114,-7.313597,-9.109409],[3.685585,0.132521,2.352310,-9.307510,2.404762,6.666136,3.836192,-4.262627,-0.686792,9.072788,7.372025,-6.944911,-3.108694],[-8.127277,9.474177,-3.402506,1.617340,-5.708395,-8.674159,-6.454731,6.193835,-3.658130,-4.781887,-4.261680,4.613306,-8.669488],[-6.553181,-3.951315,3.802494,7.606575,0.376647,4.974767,5.312985,1.708411,-8.338657,-5.336077,6.273580,-5.837192,6.027230],[3.449266,6.654272,0.573947,-0.011109,-2.115123,-2.030157,-6.678076,5.584121,-9.083344,3.562177,0.459580,6.281685,8.600129],[-1.538379,-5.228905,-0.462590,2.721182,0.291904,6.251034,-5.089866,3.635881,-1.585305,5.508431,4.805164,-1.981594,5.717365],[-9.895112,7.633724,-9.595119,-9.364739,7.127288,-9.700467,-1.687423,6.728255,2.481396,1.165935,-5.390254,-8.301607,2.581950],[3.273496,-1.404896,0.832983,0.809777,-6.381078,5.165099,-7.883966,1.290645,0.027032,7.713715,-3.965850,-5.904329,5.548108],[9.794114,-7.435009,-7.068839,-3.364386,5.893648,7.931771,8.649500,-8.546438,-1.636590,6.522745,1.156782,7.898492,-0.473237],[4.962673,1.159716,4.419284,-5.388177,-0.498785,-9.850571,9.467028,-5.706206,-9.869431,-2.248359,-1.913177,-8.397993,-4.823293],[-0.606774,-1.455973,8.275378,-6.180148,-4.525733,4.681120,6.023613,9.429443,5.235237,9.571180,-5.537942,0.864985,-9.850642],[0.315712,6.299024,-2.672407,-9.116132,-0.634582,-3.981796,-0.220423,3.423155,2.359120,1.380197,-4.174426,6.799959,1.203229]],[[8.374480,-7.745537,-7.120386,-7.142922,-2.230809,-8.468506,0.261015,-6.840866,9.037845,1.026365,8.867528,0.063173,1.409204],[8.413096,-9.384252,-0.414495,6.341547,3.894022,4.286610,6.443671,4.446520,-0.213488,5.073068,-6.079379,0.821395,9.774985],[7.529381,-0.804737,-1.847493,2.511472,-5.786903,-7.027357,7.690032,2.655080,-7.273282,-2.744458,-9.430957,-6.661755,4.707995],[-5.389126,-6.528156,3.882377,1.861184,7.080800,1.033607,-0.640959,-3.897555,1.238222,-5.973656,-9.601271,-9.549088,-5.114374],[8.714490,-0.645623,-4.822792,-6.966850,-1.589530,-6.708659,4.872513,7.588135,-2.870834,-8.450046,-9.037302,-2.328424,-3.807649],[8.532527,3.653709,-4.954582,3.729460,-3.062796,1.228522,-1.850585,-8.223176,3.607946,-4.756991,6.180183,-2.141659,-3.172325],[3.939416,-7.125955,9.634930,-5.138277,4.317464,-1.023752,7.834218,-4.359228,2.488167,-7.701844,3.150107,9.428035,-4.169920],[8.868953,-2.700948,-7.230093,-7.720527,8.292085,-6.298560,0.155272,-5.941976,-2.186086,-5.313233,3.176945,-4.353699,9.581604],[2.420761,8.844669,7.843953,3.061413,-1.778899,-3.640321,-3.875511,8.581789,5.543260,-8.181685,-7.843921,-0.024906,-0.016096],[-1.690212,5.000464,-6.430952,-6.224241,8.536935,-4.642919,6.149158,-5.472252,-0.163408,9.725915,8.528962,-7.160706,8.478651],[1.264941,0.560172,0.732565,-1.646512,8.727233,5.051661,-3.097397,-8.346785,8.537435,-5.832738,1.259823,-4.497514,-4.069206],[6.959424,-0.749086,0.193193,-7.831819,2.483764,-4.953859,3.908082,-5.736688,8.941798,4.324967,-5.679253,7.435231,-1.009254],[4.656365,8.785324,-4.492580,-8.000079,6.081681,-3.623532,-4.859321,1.632216,2.903699,-0.398230,-8.028421,1.247468,5.204876],[-8.151174,-9.474737,7.377948,-7.909369,6.966034,-5.528176,2.760374,4.701739,8.710881,8.842735,-4.188733,3.381055,-7.183533],[-3.692881,8.863329,6.740141,-8.433118,-1.051638,8.279546,-0.050401,-5.022365,-3.198811,3.660858,7.556601,1.840793,5.330650]],[[-6.942557,8.076205,-6.618961,-8.619124,3.257359,-8.563677,1.978897,-3.033071,5.651005,7.985802,2.416374,2.970175,0.222367],[4.309920,4.117521,-1.754948,-2.072421,-5.083189,9.381609,-8.717621,6.474759,-0.877049,-8.765539,2.605043,3.608692,5.897488],[4.101912,2.929634,7.274653,2.720470,-8.733714,-2.211990,2.919484,4.527156,6.741489,-1.000507,-2.026935,5.506289,4.718629],[-3.073569,9.838769,5.962046,-5.401473,6.916779,4.822716,-9.446135,-3.177816,-3.666423,-6.237291,-1.445401,-6.732094,-3.588494],[1.642148,6.040362,-4.178794,-6.895939,9.549304,-6.538962,-5.035127,9.065840,9.981837,7.322371,1.247447,3.391317,-8.347218],[1.335592,-0.264235,9.443797,-1.623221,-0.713785,3.766125,-3.450013,-3.228598,-0.832283,2.439699,4.236257,-5.193796,-6.467060],[-6.041877,5.580105,-9.711353,1.928489,-3.677320,-0.601425,7.545971,7.963664,7.863311,9.263734,8.462261,3.652811,-5.750987],[2.790186,2.501825,-7.750658,2.465759,-0.409860,-1.599928,2.599557,8.098141,6.977062,-7.909650,6.486414,1.377337,-8.771074],[-1.497411,1.658740,-3.166079,8.933081,-9.239758,7.008447,6.149148,8.254588,-0.660192,-7.564142,0.195380,-8.470101,3.796213],[0.319464,7.899615,1.291808,0.003818,-0.411556,8.717216,-9.432069,6.768501,0.179179,9.383519,-9.413661,3.906701,0.162893],[7.971619,9.775425,7.293280,4.850857,-5.510390,2.670234,3.981966,2.764157,9.342842,-5.820543,2.216677,-9.775457,1.955761],[-1.552845,2.312856,9.150876,-0.480681,3.306196,1.828527,-7.090883,3.044186,-3.147976,3.105691,4.623484,7.915362,4.566641],[-6.640483,6.138517,-6.776386,-1.659357,-5.878631,-5.547988,-0.078968,-9.254943,-6.920998,7.844311,-5.171451,-7.605282,2.898346],[0.432204,-0.028626,-1.337438,-9.643914,-9.454284,7.315710,-2.628080,-9.252058,-1.801079,4.659716,-6.033281,5.301149,3.469311],[9.060983,6.638300,-3.906736,9.793553,4.228225,5.012140,-1.331459,8.557681,-6.725240,2.742230,-7.020430,-9.329887,-9.008108]],[[-6.779094,-9.031148,-1.476534,8.902702,5.949423,-2.942853,-8.219205,-5.835430,7.679086,5.085671,-7.887980,-8.837099,-8.584942],[-2.903742,-9.276717,-5.710812,-4.452438,2.580977,-5.147406,6.244092,-8.375291,7.528451,1.900971,-2.193114,-0.477040,8.532807],[3.873345,-5.739837,1.735618,-4.521267,7.461350,-8.593659,-8.315229,-0.284587,-5.139040,-8.533559,2.499386,-0.503376,1.399311],[0.230218,-8.933201,-8.479944,5.501179,-7.339475,9.132928,-8.664719,1.796742,1.165666,-7.246086,-5.379244,0.593741,0.026564],[-3.801896,8.595493,-7.717055,4.147687,-3.680116,3.446749,-7.689008,-3.136343,-3.087728,1.422233,5.584540,0.856245,-7.061577],[-7.808893,-8.777857,1.364109,0.790393,-8.409621,7.971673,1.219480,-8.857200,9.494388,-1.694997,-4.665114,9.506881,-4.959138],[-6.124761,-2.448137,9.449028,-1.829670,6.584077,5.041050,4.949099,-0.318738,4.145103,-0.162112,-6.620824,0.582738,0.949199],[-6.599921,5.357727,3.507560,-4.559861,-5.789459,-5.794354,-9.619246,-6.360043,8.994689,3.634918,9.575664,4.478003,-8.560201],[6.321934,-5.426555,-1.229717,6.943389,1.807057,1.787269,1.272942,3.592110,5.449664,1.140027,0.136500,7.481501,-5.238495],[-5.067872,-2.754090,-4.656819,-4.020640,-6.734915,4.398648,-2.747950,-1.464617,-9.816272,8.860903,0.624307,7.839070,1.921704],[3.633150,-6.587364,9.311646,1.014699,9.299122,9.782279,-0.912654,-3.390128,-4.020777,-8.432652,7.981608,-7.632299,1.259270],[8.458795,-3.426499,1.547396,0.399997,7.819978,-7.890593,-6.124436,-8.682214,8.263858,6.098896,-3.585431,-4.068541,-1.907158],[-2.932735,8.547485,-1.022926,-1.371942,4.669122,4.683454,2.524343,0.646077,7.345495,-4.734088,8.807919,7.336531,3.421200],[-1.878448,-8.204937,9.057139,8.392087,-9.736184,3.602638,-4.814555,4.450244,2.076534,7.087596,-2.961217,-2.157775,-0.938229],[0.942929,-2.222067,-0.852802,-1.952146,1.122545,0.685008,-9.923241,6.088731,-8.045400,-0.559881,6.045183,6.805317,-8.998333]],[[1.996545,-4.491224,4.770145,7.819593,-5.792190,-0.824802,7.319541,7.548394,8.785403,-6.929910,5.937109,-6.430270,-3.732459],[-9.472915,-0.897478,-4.945735,6.607900,-2.249597,-3.114340,9.089989,9.077394,4.692750,0.856045,6.619669,6.527701,0.593775],[-9.956246,-5.905203,0.940828,-1.734467,-3.368087,-9.087760,3.824154,-4.296992,-9.442100,4.397598,7.904189,-7.867366,8.573783],[6.843444,-4.163311,7.950109,6.662205,2.980075,-1.013879,-5.861566,-3.182086,9.317374,3.806273,5.140389,1.473823,0.173027],[-6.457339,4.308777,8.065387,-1.584434,-9.294303,3.033939,7.511229,-7.814456,-7.061185,-5.086990,5.835440,7.877032,4.711020],[7.397669,8.254104,-0.656680,-8.137528,4.331585,-7.035692,8.600389,8.789754,-5.150851,-1.284606,0.545875,-3.948835,4.963298],[2.880067,-4.435725,-7.292895,4.287328,2.549065,3.253204,3.001587,2.983274,-0.074155,-2.396433,6.198188,-8.747767,-9.565962],[4.436380,-2.029836,-9.863482,5.125448,-3.529914,-0.636956,8.903342,8.414819,-4.951943,5.160460,1.315929,-2.086203,9.192855],[-4.028814,1.543372,0.041497,3.869436,-6.607696,3.981745,7.956012,7.280840,3.044751,1.267733,8.869241,-7.301642,4.844067],[-4.086890,4.820962,-6.368633,5.720919,-9.866379,-8.710133,-9.891248,-5.274147,-0.956079,-9.667050,5.900493,-0.738289,-0.132484],[-6.213271,-7.710488,-4.409699,-2.301930,-8.394388,-3.589975,-9.562291,7.931306,-2.142665,6.610799,0.057190,-7.533047,4.836703],[-7.707520,-2.714430,2.210640,6.805455,1.719181,-0.497771,1.074509,-6.273575,7.506209,9.925819,3.801693,-2.374648,-8.525911],[-1.738832,5.122981,-0.545918,2.186685,6.319592,-0.120636,-3.447868,-9.390319,4.787862,8.436015,3.231194,-5.167284,7.909566],[6.750691,3.822157,-8.270647,-3.612990,9.672696,0.310408,-2.917612,-6.803746,1.227081,-7.688795,4.868674,5.611169,8.422507],[2.666406,7.094031,9.689027,0.634968,-6.496544,-5.880994,0.004235,-0.947331,-8.322673,4.931396,7.399901,4.001510,3.359001]]], dtype = "float64")#candidate|7794|(16, 15, 13)|const|float64
bop_7795 = relay.floor_divide(var_7793.astype('float64'), relay.reshape(const_7794.astype('float64'), relay.shape_of(var_7793))) # shape=(16, 15, 13)
var_7804 = relay.var("var_7804", dtype = "float64", shape = (16, 15, 13))#candidate|7804|(16, 15, 13)|var|float64
bop_7805 = relay.subtract(bop_7795.astype('uint16'), relay.reshape(var_7804.astype('uint16'), relay.shape_of(bop_7795))) # shape=(16, 15, 13)
uop_7817 = relay.cosh(var_7793.astype('float32')) # shape=(16, 15, 13)
output = relay.Tuple([bop_7805,uop_7817,])
output2 = relay.Tuple([bop_7805,uop_7817,])
func_7822 = relay.Function([var_7793,var_7804,], output)
mod['func_7822'] = func_7822
mod = relay.transform.InferType()(mod)
var_7823 = relay.var("var_7823", dtype = "float64", shape = (16, 15, 13))#candidate|7823|(16, 15, 13)|var|float64
var_7824 = relay.var("var_7824", dtype = "float64", shape = (16, 15, 13))#candidate|7824|(16, 15, 13)|var|float64
output = func_7822(var_7823,var_7824,)
func_7825 = relay.Function([var_7823,var_7824,], output)
mutated_mod['func_7825'] = func_7825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5845_call = mod.get_global_var('func_5845')
func_5847_call = mutated_mod.get_global_var('func_5847')
call_7827 = relay.TupleGetItem(func_5845_call(), 0)
call_7828 = relay.TupleGetItem(func_5847_call(), 0)
output = call_7827
output2 = call_7828
func_7830 = relay.Function([], output)
mod['func_7830'] = func_7830
mod = relay.transform.InferType()(mod)
mutated_mod['func_7830'] = func_7830
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7830_call = mutated_mod.get_global_var('func_7830')
call_7831 = func_7830_call()
output = call_7831
func_7832 = relay.Function([], output)
mutated_mod['func_7832'] = func_7832
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7844 = relay.var("var_7844", dtype = "float64", shape = (4, 1, 7))#candidate|7844|(4, 1, 7)|var|float64
uop_7845 = relay.cosh(var_7844.astype('float64')) # shape=(4, 1, 7)
bop_7850 = relay.less_equal(uop_7845.astype('bool'), relay.reshape(var_7844.astype('bool'), relay.shape_of(uop_7845))) # shape=(4, 1, 7)
bop_7857 = relay.subtract(var_7844.astype('uint8'), relay.reshape(bop_7850.astype('uint8'), relay.shape_of(var_7844))) # shape=(4, 1, 7)
output = bop_7857
output2 = bop_7857
func_7862 = relay.Function([var_7844,], output)
mod['func_7862'] = func_7862
mod = relay.transform.InferType()(mod)
mutated_mod['func_7862'] = func_7862
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7863 = relay.var("var_7863", dtype = "float64", shape = (4, 1, 7))#candidate|7863|(4, 1, 7)|var|float64
func_7862_call = mutated_mod.get_global_var('func_7862')
call_7864 = func_7862_call(var_7863)
output = call_7864
func_7865 = relay.Function([var_7863], output)
mutated_mod['func_7865'] = func_7865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7513_call = mod.get_global_var('func_7513')
func_7514_call = mutated_mod.get_global_var('func_7514')
call_7867 = relay.TupleGetItem(func_7513_call(), 0)
call_7868 = relay.TupleGetItem(func_7514_call(), 0)
func_7160_call = mod.get_global_var('func_7160')
func_7162_call = mutated_mod.get_global_var('func_7162')
call_7882 = relay.TupleGetItem(func_7160_call(), 1)
call_7883 = relay.TupleGetItem(func_7162_call(), 1)
output = relay.Tuple([call_7867,call_7882,])
output2 = relay.Tuple([call_7868,call_7883,])
func_7915 = relay.Function([], output)
mod['func_7915'] = func_7915
mod = relay.transform.InferType()(mod)
mutated_mod['func_7915'] = func_7915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7915_call = mutated_mod.get_global_var('func_7915')
call_7916 = func_7915_call()
output = call_7916
func_7917 = relay.Function([], output)
mutated_mod['func_7917'] = func_7917
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7929 = relay.var("var_7929", dtype = "float32", shape = (11, 16, 5))#candidate|7929|(11, 16, 5)|var|float32
uop_7930 = relay.cos(var_7929.astype('float32')) # shape=(11, 16, 5)
func_4879_call = mod.get_global_var('func_4879')
func_4880_call = mutated_mod.get_global_var('func_4880')
call_7937 = relay.TupleGetItem(func_4879_call(), 0)
call_7938 = relay.TupleGetItem(func_4880_call(), 0)
uop_7942 = relay.acos(uop_7930.astype('float64')) # shape=(11, 16, 5)
bop_7954 = relay.logical_or(uop_7942.astype('bool'), relay.reshape(uop_7930.astype('bool'), relay.shape_of(uop_7942))) # shape=(11, 16, 5)
uop_7959 = relay.erf(uop_7930.astype('float64')) # shape=(11, 16, 5)
var_7961 = relay.var("var_7961", dtype = "float32", shape = (11, 16, 5))#candidate|7961|(11, 16, 5)|var|float32
bop_7962 = relay.floor_mod(uop_7930.astype('float64'), relay.reshape(var_7961.astype('float64'), relay.shape_of(uop_7930))) # shape=(11, 16, 5)
output = relay.Tuple([call_7937,bop_7954,uop_7959,bop_7962,])
output2 = relay.Tuple([call_7938,bop_7954,uop_7959,bop_7962,])
func_7974 = relay.Function([var_7929,var_7961,], output)
mod['func_7974'] = func_7974
mod = relay.transform.InferType()(mod)
var_7975 = relay.var("var_7975", dtype = "float32", shape = (11, 16, 5))#candidate|7975|(11, 16, 5)|var|float32
var_7976 = relay.var("var_7976", dtype = "float32", shape = (11, 16, 5))#candidate|7976|(11, 16, 5)|var|float32
output = func_7974(var_7975,var_7976,)
func_7977 = relay.Function([var_7975,var_7976,], output)
mutated_mod['func_7977'] = func_7977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5298_call = mod.get_global_var('func_5298')
func_5299_call = mutated_mod.get_global_var('func_5299')
call_8003 = relay.TupleGetItem(func_5298_call(), 0)
call_8004 = relay.TupleGetItem(func_5299_call(), 0)
output = call_8003
output2 = call_8004
func_8018 = relay.Function([], output)
mod['func_8018'] = func_8018
mod = relay.transform.InferType()(mod)
output = func_8018()
func_8019 = relay.Function([], output)
mutated_mod['func_8019'] = func_8019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7308_call = mod.get_global_var('func_7308')
func_7309_call = mutated_mod.get_global_var('func_7309')
call_8030 = relay.TupleGetItem(func_7308_call(), 1)
call_8031 = relay.TupleGetItem(func_7309_call(), 1)
output = relay.Tuple([call_8030,])
output2 = relay.Tuple([call_8031,])
func_8036 = relay.Function([], output)
mod['func_8036'] = func_8036
mod = relay.transform.InferType()(mod)
mutated_mod['func_8036'] = func_8036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8036_call = mutated_mod.get_global_var('func_8036')
call_8037 = func_8036_call()
output = call_8037
func_8038 = relay.Function([], output)
mutated_mod['func_8038'] = func_8038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6650_call = mod.get_global_var('func_6650')
func_6651_call = mutated_mod.get_global_var('func_6651')
call_8108 = relay.TupleGetItem(func_6650_call(), 2)
call_8109 = relay.TupleGetItem(func_6651_call(), 2)
func_4492_call = mod.get_global_var('func_4492')
func_4493_call = mutated_mod.get_global_var('func_4493')
call_8114 = relay.TupleGetItem(func_4492_call(), 0)
call_8115 = relay.TupleGetItem(func_4493_call(), 0)
output = relay.Tuple([call_8108,call_8114,])
output2 = relay.Tuple([call_8109,call_8115,])
func_8118 = relay.Function([], output)
mod['func_8118'] = func_8118
mod = relay.transform.InferType()(mod)
output = func_8118()
func_8119 = relay.Function([], output)
mutated_mod['func_8119'] = func_8119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6733_call = mod.get_global_var('func_6733')
func_6735_call = mutated_mod.get_global_var('func_6735')
call_8153 = relay.TupleGetItem(func_6733_call(), 0)
call_8154 = relay.TupleGetItem(func_6735_call(), 0)
func_2601_call = mod.get_global_var('func_2601')
func_2603_call = mutated_mod.get_global_var('func_2603')
var_8164 = relay.var("var_8164", dtype = "float32", shape = (48,))#candidate|8164|(48,)|var|float32
call_8163 = relay.TupleGetItem(func_2601_call(relay.reshape(var_8164.astype('float32'), [4, 4, 3])), 4)
call_8165 = relay.TupleGetItem(func_2603_call(relay.reshape(var_8164.astype('float32'), [4, 4, 3])), 4)
func_6186_call = mod.get_global_var('func_6186')
func_6188_call = mutated_mod.get_global_var('func_6188')
call_8182 = relay.TupleGetItem(func_6186_call(), 0)
call_8183 = relay.TupleGetItem(func_6188_call(), 0)
func_5424_call = mod.get_global_var('func_5424')
func_5425_call = mutated_mod.get_global_var('func_5425')
call_8196 = func_5424_call()
call_8197 = func_5424_call()
func_3274_call = mod.get_global_var('func_3274')
func_3275_call = mutated_mod.get_global_var('func_3275')
call_8212 = relay.TupleGetItem(func_3274_call(), 0)
call_8213 = relay.TupleGetItem(func_3275_call(), 0)
output = relay.Tuple([call_8153,call_8163,var_8164,call_8182,call_8196,call_8212,])
output2 = relay.Tuple([call_8154,call_8165,var_8164,call_8183,call_8197,call_8213,])
func_8214 = relay.Function([var_8164,], output)
mod['func_8214'] = func_8214
mod = relay.transform.InferType()(mod)
var_8215 = relay.var("var_8215", dtype = "float32", shape = (48,))#candidate|8215|(48,)|var|float32
output = func_8214(var_8215)
func_8216 = relay.Function([var_8215], output)
mutated_mod['func_8216'] = func_8216
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8036_call = mod.get_global_var('func_8036')
func_8038_call = mutated_mod.get_global_var('func_8038')
call_8220 = relay.TupleGetItem(func_8036_call(), 0)
call_8221 = relay.TupleGetItem(func_8038_call(), 0)
output = relay.Tuple([call_8220,])
output2 = relay.Tuple([call_8221,])
func_8253 = relay.Function([], output)
mod['func_8253'] = func_8253
mod = relay.transform.InferType()(mod)
output = func_8253()
func_8254 = relay.Function([], output)
mutated_mod['func_8254'] = func_8254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4492_call = mod.get_global_var('func_4492')
func_4493_call = mutated_mod.get_global_var('func_4493')
call_8271 = relay.TupleGetItem(func_4492_call(), 0)
call_8272 = relay.TupleGetItem(func_4493_call(), 0)
var_8278 = relay.var("var_8278", dtype = "uint32", shape = (7, 3, 7))#candidate|8278|(7, 3, 7)|var|uint32
bop_8279 = relay.divide(call_8271.astype('float64'), relay.reshape(var_8278.astype('float64'), relay.shape_of(call_8271))) # shape=(7, 3, 7)
bop_8282 = relay.divide(call_8272.astype('float64'), relay.reshape(var_8278.astype('float64'), relay.shape_of(call_8272))) # shape=(7, 3, 7)
output = relay.Tuple([bop_8279,])
output2 = relay.Tuple([bop_8282,])
func_8293 = relay.Function([var_8278,], output)
mod['func_8293'] = func_8293
mod = relay.transform.InferType()(mod)
var_8294 = relay.var("var_8294", dtype = "uint32", shape = (7, 3, 7))#candidate|8294|(7, 3, 7)|var|uint32
output = func_8293(var_8294)
func_8295 = relay.Function([var_8294], output)
mutated_mod['func_8295'] = func_8295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4049_call = mod.get_global_var('func_4049')
func_4050_call = mutated_mod.get_global_var('func_4050')
call_8299 = relay.TupleGetItem(func_4049_call(), 0)
call_8300 = relay.TupleGetItem(func_4050_call(), 0)
func_3074_call = mod.get_global_var('func_3074')
func_3076_call = mutated_mod.get_global_var('func_3076')
call_8321 = func_3074_call()
call_8322 = func_3074_call()
output = relay.Tuple([call_8299,call_8321,])
output2 = relay.Tuple([call_8300,call_8322,])
func_8324 = relay.Function([], output)
mod['func_8324'] = func_8324
mod = relay.transform.InferType()(mod)
output = func_8324()
func_8325 = relay.Function([], output)
mutated_mod['func_8325'] = func_8325
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8395 = relay.const([[[True,True,True,False,False,False,False],[True,False,True,False,False,True,True],[False,True,False,False,True,True,False],[False,False,True,True,True,True,False],[True,True,False,False,True,True,False],[True,True,False,False,False,False,False],[False,True,True,False,False,False,False],[True,True,True,False,False,False,True],[True,True,False,False,True,False,False],[False,False,False,True,True,False,True],[True,False,True,False,True,False,False]],[[True,False,True,True,False,False,True],[False,False,False,True,False,False,True],[True,True,True,True,True,True,False],[False,True,True,False,False,False,False],[True,False,False,True,True,True,False],[True,True,True,True,False,True,False],[False,False,True,True,True,False,False],[False,True,False,False,False,True,False],[False,True,False,False,True,True,True],[False,False,True,True,False,False,False],[False,True,False,False,True,True,True]],[[False,True,True,False,False,True,True],[True,False,True,True,True,False,True],[False,True,False,True,True,True,False],[True,True,True,True,True,True,True],[False,True,False,True,False,True,True],[True,False,False,False,False,False,True],[True,False,True,False,True,True,True],[False,True,True,False,False,False,True],[True,False,True,False,True,True,True],[True,True,False,False,True,True,False],[False,True,False,True,True,True,True]],[[False,False,False,False,True,False,False],[False,False,False,True,False,True,True],[True,False,False,True,True,True,True],[True,False,False,True,True,False,False],[False,True,False,False,True,False,False],[True,False,True,True,True,True,False],[True,False,False,True,False,False,False],[False,True,True,True,True,True,False],[False,True,False,False,False,False,False],[False,True,True,True,True,False,False],[False,True,False,False,True,False,True]],[[True,True,True,True,False,False,False],[False,False,False,False,True,True,True],[False,True,True,False,False,False,True],[False,False,True,False,True,True,False],[False,False,True,False,True,False,True],[True,True,False,True,True,False,False],[False,True,True,False,True,False,False],[True,True,True,True,True,False,False],[True,False,False,True,False,False,True],[True,False,True,False,True,True,False],[False,True,False,True,True,True,True]],[[False,True,False,True,False,True,True],[False,False,True,True,False,True,False],[False,True,False,True,False,True,True],[True,False,True,False,True,True,True],[False,False,False,False,False,False,False],[False,False,True,False,False,False,True],[False,True,False,False,True,False,True],[True,True,False,False,True,False,False],[False,True,True,True,False,False,True],[False,False,True,False,False,False,True],[False,False,False,False,False,False,False]],[[True,False,True,False,True,False,False],[False,False,True,True,True,False,False],[True,False,True,True,True,True,False],[True,True,True,False,False,True,False],[False,False,True,True,False,False,True],[False,False,True,False,False,False,True],[False,True,True,True,True,True,True],[False,False,True,False,True,False,False],[True,True,False,True,True,True,False],[False,False,True,False,False,True,False],[True,True,False,True,False,True,False]],[[False,False,True,False,False,False,False],[False,False,False,True,False,True,True],[True,False,True,True,False,True,True],[True,False,False,False,True,False,True],[False,True,True,False,False,True,False],[False,True,True,False,False,True,False],[False,False,True,True,True,False,True],[True,True,False,False,True,False,False],[True,False,True,True,False,True,True],[False,False,True,False,True,False,True],[True,False,True,True,False,False,True]],[[True,False,False,True,False,False,True],[True,True,False,False,True,True,True],[True,False,False,True,False,False,False],[False,False,True,True,False,False,True],[True,False,False,False,False,False,True],[False,False,True,False,True,True,False],[True,False,False,False,True,False,False],[True,False,False,True,True,True,True],[True,True,False,False,True,False,True],[True,False,False,False,False,True,False],[False,False,False,True,True,False,True]],[[False,True,True,True,True,True,True],[False,False,False,False,True,False,False],[False,False,True,False,False,False,False],[False,True,False,False,False,False,True],[True,True,True,True,False,False,False],[True,False,True,False,False,True,False],[False,True,False,False,True,False,False],[True,False,False,False,True,False,False],[True,True,False,False,False,True,True],[False,True,False,True,True,True,True],[False,True,True,False,False,False,False]],[[False,False,True,True,False,True,True],[True,False,False,True,True,False,True],[True,True,True,True,False,True,False],[False,False,False,False,True,True,False],[False,True,False,False,True,True,True],[True,True,True,True,True,True,False],[False,True,True,True,False,False,False],[False,True,False,False,False,False,False],[True,False,False,True,True,True,True],[True,False,True,False,True,False,True],[False,True,True,False,False,True,True]],[[False,True,True,False,True,False,True],[True,False,True,False,False,False,False],[False,True,True,True,True,False,True],[True,False,True,True,True,False,False],[True,True,True,True,True,True,False],[False,True,True,True,True,False,True],[False,False,True,False,True,True,True],[True,True,False,False,False,True,True],[True,False,True,True,True,True,False],[False,False,False,False,True,True,True],[False,False,True,False,False,False,False]],[[False,True,True,True,True,False,True],[True,True,False,False,True,False,True],[True,True,False,True,True,False,False],[False,False,True,False,False,False,True],[False,True,True,False,False,True,True],[True,True,False,False,False,True,True],[False,True,False,True,False,False,False],[True,True,False,True,True,False,True],[True,False,False,True,True,False,False],[False,True,True,True,False,False,False],[False,True,True,False,False,True,True]],[[False,False,False,True,True,False,False],[False,False,True,True,True,False,False],[False,False,False,False,True,False,False],[True,False,False,True,True,True,False],[True,False,True,True,False,True,False],[True,False,False,True,False,True,False],[True,True,True,False,True,True,False],[False,True,False,True,True,False,True],[False,True,True,True,False,False,False],[False,False,False,False,False,False,True],[False,False,False,False,True,True,False]]], dtype = "bool")#candidate|8395|(14, 11, 7)|const|bool
var_8396 = relay.var("var_8396", dtype = "bool", shape = (14, 11, 7))#candidate|8396|(14, 11, 7)|var|bool
bop_8397 = relay.logical_and(const_8395.astype('bool'), relay.reshape(var_8396.astype('bool'), relay.shape_of(const_8395))) # shape=(14, 11, 7)
func_3820_call = mod.get_global_var('func_3820')
func_3826_call = mutated_mod.get_global_var('func_3826')
var_8401 = relay.var("var_8401", dtype = "uint32", shape = ())#candidate|8401|()|var|uint32
var_8402 = relay.var("var_8402", dtype = "int32", shape = (5, 6))#candidate|8402|(5, 6)|var|int32
const_8403 = relay.const([-7.974974,-5.987752,-0.462872,-4.161508,-9.107101,3.463522,-4.984125,-6.606598,1.323692,-1.104070,-1.301025,-1.981067,-0.569398,1.282884,-2.563493,-2.593265,3.552151,2.933361,9.758698,8.321989,-4.687692,8.615835,9.624801,-3.833877,3.199040,-4.309352,2.540546,8.741780,-7.981506,6.823822,8.460057,9.869185,-7.362509,-5.106873,-7.824342,4.187389,-6.006130,3.450806,0.309382,5.347976,2.010288,-6.730059,-4.061223,-9.448539,-3.578792,6.827586,7.721361,-1.112972,4.408810,3.379613,-8.317035,0.176653,5.265728,7.751623,-1.795701,-2.202813,-6.864791,-7.335998,-1.320679,5.167432,-0.744018,-1.903617,2.695147,5.474981,1.258428,-1.382056,4.735830,6.054496,3.500890,7.801179,8.078780,2.470091,3.814596,-3.495862,-8.696548,-1.002263,-8.106940,-3.169588,-1.897839,-1.593629,-7.552535,5.395062,-1.361033,-7.124434,7.807086,7.524545,2.200895,7.227210,-9.494608,-4.738692,2.008389,7.327280,1.476545,-4.706762,0.427576,-3.353040,4.803088,-3.543878,-8.913805,7.385156,-8.969273,-2.890200,2.842370,-7.590499,7.628716,-9.618048,-5.816952,-5.249137,4.070331,8.311976,4.578810,-8.056872,4.956590,4.120331,-2.747417,-0.274575,0.378514,-5.490637,-2.536310,2.039879,-3.830804,-3.196193,1.108345,-1.165162,3.674478,-7.479699,4.608105,-0.824244,9.547400,-6.996067,-8.194851,-0.736015,2.075772,9.133758,-8.640302,2.084648,-7.267812,4.055854,-4.247020,0.878335,4.809517,6.776203,-6.031929,7.848145,6.682978,8.524472,-0.791995,0.345134,1.492567,8.815928,9.873948,-6.318443,3.726884,-7.708477,4.670527,1.817402,1.836425,-3.806401,-1.256415,5.073026,4.879054,-2.637295,-9.161433,-4.139247,-9.171059,1.048026,-2.242698,1.688734,8.432833,-5.126366,3.957074,1.830413,-2.273677,1.441773,-4.798506,-2.143391,3.651362,7.290100,-5.916742,8.667060,-8.444905,0.091997,-7.536390,-1.226889,-3.020302,6.751218,-5.435400,-6.191609,-5.805769,-2.612139,-5.798191,-8.098536,9.671999,5.047674,3.276428,-1.655189,-4.294214,6.984867,-4.685273,-5.591266,-4.384932,9.344819,6.454533,9.235827,8.240173,-0.492594,-7.085107,9.754235,-3.357889,8.928917,-3.362212,4.519338,6.337464,3.662823,-2.492593,-9.451665,4.879261,-2.501312,3.924935,-9.844786,2.607647,-6.087423,-1.782718,2.037912,2.928946,-1.926772,-9.820455,-6.278296,-9.782627,9.662434,6.093692,1.547253,7.690071,6.520039,5.159743,7.001589,-9.663273,-0.254008,-6.047158,-1.782348,5.650067,6.784134,-5.754818,4.389273,3.136039,-9.916564,2.438461,-9.093503,1.504489,9.532904,1.376408,1.571533,0.399419,-0.560538,0.683475,5.570319,-8.995059,-1.002804,-1.523659,2.507409,-4.131343,-0.189432,-0.841507,0.884632,9.561533,-5.400922,2.982598,-2.461904,-7.864150,-8.041269,1.010407,-4.985178,-4.003066,1.758893,-6.524209,0.243485,-7.502895,-6.540170,-0.975896,-4.927719,9.933814,-6.367068,-3.336994,0.589082,-1.137901,-6.914501,5.311910,5.042297,5.437895,-3.497857,2.536114,-2.345710,0.091464,-2.004409,-4.466925,4.743488,-4.744527,4.862318,0.040756,5.579245], dtype = "float64")#candidate|8403|(300,)|const|float64
var_8404 = relay.var("var_8404", dtype = "float64", shape = (320,))#candidate|8404|(320,)|var|float64
call_8400 = relay.TupleGetItem(func_3820_call(relay.reshape(var_8401.astype('uint32'), []), relay.reshape(var_8402.astype('int32'), [5, 6]), relay.reshape(const_8403.astype('float64'), [150, 2]), relay.reshape(var_8404.astype('float64'), [320,]), ), 6)
call_8405 = relay.TupleGetItem(func_3826_call(relay.reshape(var_8401.astype('uint32'), []), relay.reshape(var_8402.astype('int32'), [5, 6]), relay.reshape(const_8403.astype('float64'), [150, 2]), relay.reshape(var_8404.astype('float64'), [320,]), ), 6)
func_5576_call = mod.get_global_var('func_5576')
func_5580_call = mutated_mod.get_global_var('func_5580')
call_8406 = relay.TupleGetItem(func_5576_call(relay.reshape(var_8402.astype('int32'), [1, 30]), relay.reshape(const_8403.astype('float64'), [300,]), ), 1)
call_8407 = relay.TupleGetItem(func_5580_call(relay.reshape(var_8402.astype('int32'), [1, 30]), relay.reshape(const_8403.astype('float64'), [300,]), ), 1)
output = relay.Tuple([bop_8397,call_8400,var_8401,var_8402,const_8403,var_8404,call_8406,])
output2 = relay.Tuple([bop_8397,call_8405,var_8401,var_8402,const_8403,var_8404,call_8407,])
func_8414 = relay.Function([var_8396,var_8401,var_8402,var_8404,], output)
mod['func_8414'] = func_8414
mod = relay.transform.InferType()(mod)
mutated_mod['func_8414'] = func_8414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8414_call = mutated_mod.get_global_var('func_8414')
var_8416 = relay.var("var_8416", dtype = "bool", shape = (14, 11, 7))#candidate|8416|(14, 11, 7)|var|bool
var_8417 = relay.var("var_8417", dtype = "uint32", shape = ())#candidate|8417|()|var|uint32
var_8418 = relay.var("var_8418", dtype = "int32", shape = (5, 6))#candidate|8418|(5, 6)|var|int32
var_8419 = relay.var("var_8419", dtype = "float64", shape = (320,))#candidate|8419|(320,)|var|float64
call_8415 = func_8414_call(var_8416,var_8417,var_8418,var_8419,)
output = call_8415
func_8420 = relay.Function([var_8416,var_8417,var_8418,var_8419,], output)
mutated_mod['func_8420'] = func_8420
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8430 = relay.var("var_8430", dtype = "float64", shape = (8, 16, 15))#candidate|8430|(8, 16, 15)|var|float64
var_8431 = relay.var("var_8431", dtype = "float64", shape = (8, 16, 15))#candidate|8431|(8, 16, 15)|var|float64
bop_8432 = relay.floor_mod(var_8430.astype('float64'), relay.reshape(var_8431.astype('float64'), relay.shape_of(var_8430))) # shape=(8, 16, 15)
func_5207_call = mod.get_global_var('func_5207')
func_5210_call = mutated_mod.get_global_var('func_5210')
var_8448 = relay.var("var_8448", dtype = "float64", shape = (252,))#candidate|8448|(252,)|var|float64
call_8447 = func_5207_call(relay.reshape(var_8448.astype('float64'), [9, 7, 4]))
call_8449 = func_5207_call(relay.reshape(var_8448.astype('float64'), [9, 7, 4]))
output = relay.Tuple([bop_8432,call_8447,var_8448,])
output2 = relay.Tuple([bop_8432,call_8449,var_8448,])
func_8454 = relay.Function([var_8430,var_8431,var_8448,], output)
mod['func_8454'] = func_8454
mod = relay.transform.InferType()(mod)
var_8455 = relay.var("var_8455", dtype = "float64", shape = (8, 16, 15))#candidate|8455|(8, 16, 15)|var|float64
var_8456 = relay.var("var_8456", dtype = "float64", shape = (8, 16, 15))#candidate|8456|(8, 16, 15)|var|float64
var_8457 = relay.var("var_8457", dtype = "float64", shape = (252,))#candidate|8457|(252,)|var|float64
output = func_8454(var_8455,var_8456,var_8457,)
func_8458 = relay.Function([var_8455,var_8456,var_8457,], output)
mutated_mod['func_8458'] = func_8458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8324_call = mod.get_global_var('func_8324')
func_8325_call = mutated_mod.get_global_var('func_8325')
call_8463 = relay.TupleGetItem(func_8324_call(), 1)
call_8464 = relay.TupleGetItem(func_8325_call(), 1)
func_3026_call = mod.get_global_var('func_3026')
func_3028_call = mutated_mod.get_global_var('func_3028')
var_8470 = relay.var("var_8470", dtype = "float64", shape = (4, 80))#candidate|8470|(4, 80)|var|float64
call_8469 = relay.TupleGetItem(func_3026_call(relay.reshape(var_8470.astype('float64'), [10, 2, 16])), 0)
call_8471 = relay.TupleGetItem(func_3028_call(relay.reshape(var_8470.astype('float64'), [10, 2, 16])), 0)
func_5882_call = mod.get_global_var('func_5882')
func_5885_call = mutated_mod.get_global_var('func_5885')
var_8473 = relay.var("var_8473", dtype = "float64", shape = (1, 1456))#candidate|8473|(1, 1456)|var|float64
call_8472 = relay.TupleGetItem(func_5882_call(relay.reshape(var_8473.astype('float64'), [728, 2])), 4)
call_8474 = relay.TupleGetItem(func_5885_call(relay.reshape(var_8473.astype('float64'), [728, 2])), 4)
func_2601_call = mod.get_global_var('func_2601')
func_2603_call = mutated_mod.get_global_var('func_2603')
var_8478 = relay.var("var_8478", dtype = "float32", shape = (48,))#candidate|8478|(48,)|var|float32
call_8477 = relay.TupleGetItem(func_2601_call(relay.reshape(var_8478.astype('float32'), [4, 4, 3])), 4)
call_8479 = relay.TupleGetItem(func_2603_call(relay.reshape(var_8478.astype('float32'), [4, 4, 3])), 4)
uop_8492 = relay.sqrt(var_8470.astype('float64')) # shape=(4, 80)
uop_8494 = relay.cosh(uop_8492.astype('float64')) # shape=(4, 80)
func_7308_call = mod.get_global_var('func_7308')
func_7309_call = mutated_mod.get_global_var('func_7309')
call_8500 = relay.TupleGetItem(func_7308_call(), 0)
call_8501 = relay.TupleGetItem(func_7309_call(), 0)
output = relay.Tuple([call_8463,call_8469,call_8472,var_8473,call_8477,var_8478,uop_8494,call_8500,])
output2 = relay.Tuple([call_8464,call_8471,call_8474,var_8473,call_8479,var_8478,uop_8494,call_8501,])
func_8506 = relay.Function([var_8470,var_8473,var_8478,], output)
mod['func_8506'] = func_8506
mod = relay.transform.InferType()(mod)
var_8507 = relay.var("var_8507", dtype = "float64", shape = (4, 80))#candidate|8507|(4, 80)|var|float64
var_8508 = relay.var("var_8508", dtype = "float64", shape = (1, 1456))#candidate|8508|(1, 1456)|var|float64
var_8509 = relay.var("var_8509", dtype = "float32", shape = (48,))#candidate|8509|(48,)|var|float32
output = func_8506(var_8507,var_8508,var_8509,)
func_8510 = relay.Function([var_8507,var_8508,var_8509,], output)
mutated_mod['func_8510'] = func_8510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4841_call = mod.get_global_var('func_4841')
func_4842_call = mutated_mod.get_global_var('func_4842')
call_8527 = relay.TupleGetItem(func_4841_call(), 0)
call_8528 = relay.TupleGetItem(func_4842_call(), 0)
output = relay.Tuple([call_8527,])
output2 = relay.Tuple([call_8528,])
func_8544 = relay.Function([], output)
mod['func_8544'] = func_8544
mod = relay.transform.InferType()(mod)
mutated_mod['func_8544'] = func_8544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8544_call = mutated_mod.get_global_var('func_8544')
call_8545 = func_8544_call()
output = call_8545
func_8546 = relay.Function([], output)
mutated_mod['func_8546'] = func_8546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4049_call = mod.get_global_var('func_4049')
func_4050_call = mutated_mod.get_global_var('func_4050')
call_8581 = relay.TupleGetItem(func_4049_call(), 0)
call_8582 = relay.TupleGetItem(func_4050_call(), 0)
output = relay.Tuple([call_8581,])
output2 = relay.Tuple([call_8582,])
func_8583 = relay.Function([], output)
mod['func_8583'] = func_8583
mod = relay.transform.InferType()(mod)
mutated_mod['func_8583'] = func_8583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8583_call = mutated_mod.get_global_var('func_8583')
call_8584 = func_8583_call()
output = call_8584
func_8585 = relay.Function([], output)
mutated_mod['func_8585'] = func_8585
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5395_call = mod.get_global_var('func_5395')
func_5396_call = mutated_mod.get_global_var('func_5396')
call_8635 = relay.TupleGetItem(func_5395_call(), 1)
call_8636 = relay.TupleGetItem(func_5396_call(), 1)
var_8638 = relay.var("var_8638", dtype = "float32", shape = (12, 3, 13))#candidate|8638|(12, 3, 13)|var|float32
bop_8639 = relay.greater(call_8635.astype('bool'), relay.reshape(var_8638.astype('bool'), relay.shape_of(call_8635))) # shape=(12, 3, 13)
bop_8642 = relay.greater(call_8636.astype('bool'), relay.reshape(var_8638.astype('bool'), relay.shape_of(call_8636))) # shape=(12, 3, 13)
uop_8648 = relay.asinh(bop_8639.astype('float64')) # shape=(12, 3, 13)
uop_8650 = relay.asinh(bop_8642.astype('float64')) # shape=(12, 3, 13)
func_2745_call = mod.get_global_var('func_2745')
func_2747_call = mutated_mod.get_global_var('func_2747')
var_8656 = relay.var("var_8656", dtype = "float32", shape = (640,))#candidate|8656|(640,)|var|float32
call_8655 = func_2745_call(relay.reshape(var_8656.astype('float32'), [10, 8, 8]))
call_8657 = func_2745_call(relay.reshape(var_8656.astype('float32'), [10, 8, 8]))
func_2859_call = mod.get_global_var('func_2859')
func_2860_call = mutated_mod.get_global_var('func_2860')
call_8665 = func_2859_call()
call_8666 = func_2859_call()
bop_8683 = relay.less_equal(var_8656.astype('bool'), relay.reshape(call_8655.astype('bool'), relay.shape_of(var_8656))) # shape=(640,)
bop_8686 = relay.less_equal(var_8656.astype('bool'), relay.reshape(call_8657.astype('bool'), relay.shape_of(var_8656))) # shape=(640,)
bop_8711 = relay.left_shift(bop_8683.astype('int16'), relay.reshape(var_8656.astype('int16'), relay.shape_of(bop_8683))) # shape=(640,)
bop_8714 = relay.left_shift(bop_8686.astype('int16'), relay.reshape(var_8656.astype('int16'), relay.shape_of(bop_8686))) # shape=(640,)
func_8036_call = mod.get_global_var('func_8036')
func_8038_call = mutated_mod.get_global_var('func_8038')
call_8723 = relay.TupleGetItem(func_8036_call(), 0)
call_8724 = relay.TupleGetItem(func_8038_call(), 0)
output = relay.Tuple([uop_8648,call_8665,bop_8711,call_8723,])
output2 = relay.Tuple([uop_8650,call_8666,bop_8714,call_8724,])
func_8726 = relay.Function([var_8638,var_8656,], output)
mod['func_8726'] = func_8726
mod = relay.transform.InferType()(mod)
mutated_mod['func_8726'] = func_8726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8726_call = mutated_mod.get_global_var('func_8726')
var_8728 = relay.var("var_8728", dtype = "float32", shape = (12, 3, 13))#candidate|8728|(12, 3, 13)|var|float32
var_8729 = relay.var("var_8729", dtype = "float32", shape = (640,))#candidate|8729|(640,)|var|float32
call_8727 = func_8726_call(var_8728,var_8729,)
output = call_8727
func_8730 = relay.Function([var_8728,var_8729,], output)
mutated_mod['func_8730'] = func_8730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7675_call = mod.get_global_var('func_7675')
func_7676_call = mutated_mod.get_global_var('func_7676')
call_8817 = relay.TupleGetItem(func_7675_call(), 0)
call_8818 = relay.TupleGetItem(func_7676_call(), 0)
output = relay.Tuple([call_8817,])
output2 = relay.Tuple([call_8818,])
func_8890 = relay.Function([], output)
mod['func_8890'] = func_8890
mod = relay.transform.InferType()(mod)
mutated_mod['func_8890'] = func_8890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8890_call = mutated_mod.get_global_var('func_8890')
call_8891 = func_8890_call()
output = call_8891
func_8892 = relay.Function([], output)
mutated_mod['func_8892'] = func_8892
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7308_call = mod.get_global_var('func_7308')
func_7309_call = mutated_mod.get_global_var('func_7309')
call_8898 = relay.TupleGetItem(func_7308_call(), 0)
call_8899 = relay.TupleGetItem(func_7309_call(), 0)
output = relay.Tuple([call_8898,])
output2 = relay.Tuple([call_8899,])
func_8934 = relay.Function([], output)
mod['func_8934'] = func_8934
mod = relay.transform.InferType()(mod)
mutated_mod['func_8934'] = func_8934
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8934_call = mutated_mod.get_global_var('func_8934')
call_8935 = func_8934_call()
output = call_8935
func_8936 = relay.Function([], output)
mutated_mod['func_8936'] = func_8936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6650_call = mod.get_global_var('func_6650')
func_6651_call = mutated_mod.get_global_var('func_6651')
call_8959 = relay.TupleGetItem(func_6650_call(), 2)
call_8960 = relay.TupleGetItem(func_6651_call(), 2)
func_5476_call = mod.get_global_var('func_5476')
func_5477_call = mutated_mod.get_global_var('func_5477')
call_8962 = relay.TupleGetItem(func_5476_call(), 0)
call_8963 = relay.TupleGetItem(func_5477_call(), 0)
output = relay.Tuple([call_8959,call_8962,])
output2 = relay.Tuple([call_8960,call_8963,])
func_8981 = relay.Function([], output)
mod['func_8981'] = func_8981
mod = relay.transform.InferType()(mod)
mutated_mod['func_8981'] = func_8981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8981_call = mutated_mod.get_global_var('func_8981')
call_8982 = func_8981_call()
output = call_8982
func_8983 = relay.Function([], output)
mutated_mod['func_8983'] = func_8983
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8118_call = mod.get_global_var('func_8118')
func_8119_call = mutated_mod.get_global_var('func_8119')
call_8990 = relay.TupleGetItem(func_8118_call(), 1)
call_8991 = relay.TupleGetItem(func_8119_call(), 1)
output = relay.Tuple([call_8990,])
output2 = relay.Tuple([call_8991,])
func_9016 = relay.Function([], output)
mod['func_9016'] = func_9016
mod = relay.transform.InferType()(mod)
output = func_9016()
func_9017 = relay.Function([], output)
mutated_mod['func_9017'] = func_9017
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6117_call = mod.get_global_var('func_6117')
func_6118_call = mutated_mod.get_global_var('func_6118')
call_9018 = func_6117_call()
call_9019 = func_6117_call()
func_5691_call = mod.get_global_var('func_5691')
func_5692_call = mutated_mod.get_global_var('func_5692')
call_9025 = relay.TupleGetItem(func_5691_call(), 0)
call_9026 = relay.TupleGetItem(func_5692_call(), 0)
func_2745_call = mod.get_global_var('func_2745')
func_2747_call = mutated_mod.get_global_var('func_2747')
var_9029 = relay.var("var_9029", dtype = "float32", shape = (640,))#candidate|9029|(640,)|var|float32
call_9028 = func_2745_call(relay.reshape(var_9029.astype('float32'), [10, 8, 8]))
call_9030 = func_2745_call(relay.reshape(var_9029.astype('float32'), [10, 8, 8]))
var_9048 = relay.var("var_9048", dtype = "float32", shape = (12, 3, 13))#candidate|9048|(12, 3, 13)|var|float32
bop_9049 = relay.logical_xor(call_9025.astype('int16'), relay.reshape(var_9048.astype('int16'), relay.shape_of(call_9025))) # shape=(12, 3, 13)
bop_9052 = relay.logical_xor(call_9026.astype('int16'), relay.reshape(var_9048.astype('int16'), relay.shape_of(call_9026))) # shape=(12, 3, 13)
uop_9054 = relay.log2(call_9025.astype('float64')) # shape=(12, 3, 13)
uop_9056 = relay.log2(call_9026.astype('float64')) # shape=(12, 3, 13)
output = relay.Tuple([call_9018,call_9028,var_9029,bop_9049,uop_9054,])
output2 = relay.Tuple([call_9019,call_9030,var_9029,bop_9052,uop_9056,])
F = relay.Function([var_9029,var_9048,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_9029,var_9048,], output2)
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
