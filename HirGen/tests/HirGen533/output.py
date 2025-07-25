import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_257 = relay.const([[[-6.204062,-0.897493,5.328309,0.371140,1.427719,3.135079,9.444020,-7.109296,6.829307],[0.586207,-1.838456,-8.439262,4.148911,7.941512,0.148938,-3.633388,7.024704,1.466513],[6.553045,-8.424733,8.456963,8.503891,1.345474,0.334374,-9.474661,-5.882442,-4.605944],[-0.326789,0.413686,-4.893517,-6.475342,-7.736466,-3.198490,1.229258,-0.759713,-8.528022],[9.404235,5.372549,0.869006,-3.001615,3.717604,-1.200166,7.850127,6.049953,-9.604031],[1.799223,8.572425,-5.550655,4.379812,0.714987,3.162413,-5.546370,6.225306,2.283025],[-1.091723,-0.978689,9.114025,3.743480,8.922607,2.169936,-8.190937,6.409143,-1.763004],[5.775454,5.846656,-4.869341,-0.335715,6.009344,-1.728291,-3.654062,-1.741181,-5.032618],[8.660473,0.180248,0.003740,-2.186544,4.671702,7.521146,5.083456,-7.937310,4.107057]],[[8.664145,3.339729,0.606965,-1.555934,-3.967837,-9.240954,-7.240608,-2.094813,8.712427],[-4.330456,3.994829,9.754682,5.528665,-4.350716,6.453800,-2.334941,4.993456,5.733372],[6.043443,7.816513,7.167104,0.127721,2.005359,8.354240,7.720268,2.644034,7.015289],[1.532775,4.479892,-6.487356,4.020052,-5.394504,-6.618549,1.975758,3.832833,4.327903],[-5.330805,-7.897997,-1.772485,-5.262530,9.592450,5.395745,-1.709652,8.342443,-4.883678],[-6.225493,2.165777,-8.361302,4.937414,9.445845,-8.748719,1.955007,4.880059,4.747641],[6.592620,2.635899,2.717561,7.757983,7.005100,6.988952,4.846437,7.908056,-7.635324],[-2.895409,1.526307,-0.713255,0.435983,4.037495,6.446092,-0.297854,-0.178107,3.812020],[-7.384927,-6.230619,-9.307553,5.289563,1.775931,-0.610572,5.196876,3.863460,-5.344704]]], dtype = "float32")#candidate|257|(2, 9, 9)|const|float32
uop_258 = relay.acos(const_257.astype('float32')) # shape=(2, 9, 9)
output = relay.Tuple([uop_258,])
output2 = relay.Tuple([uop_258,])
func_261 = relay.Function([], output)
mod['func_261'] = func_261
mod = relay.transform.InferType()(mod)
mutated_mod['func_261'] = func_261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_261_call = mutated_mod.get_global_var('func_261')
call_262 = func_261_call()
output = call_262
func_263 = relay.Function([], output)
mutated_mod['func_263'] = func_263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_329 = relay.TupleGetItem(func_261_call(), 0)
call_330 = relay.TupleGetItem(func_263_call(), 0)
uop_335 = relay.atan(call_329.astype('float64')) # shape=(2, 9, 9)
uop_337 = relay.atan(call_330.astype('float64')) # shape=(2, 9, 9)
output = uop_335
output2 = uop_337
func_338 = relay.Function([], output)
mod['func_338'] = func_338
mod = relay.transform.InferType()(mod)
mutated_mod['func_338'] = func_338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_338_call = mutated_mod.get_global_var('func_338')
call_339 = func_338_call()
output = call_339
func_340 = relay.Function([], output)
mutated_mod['func_340'] = func_340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_375 = relay.TupleGetItem(func_261_call(), 0)
call_376 = relay.TupleGetItem(func_263_call(), 0)
uop_388 = relay.exp(call_375.astype('float64')) # shape=(2, 9, 9)
uop_390 = relay.exp(call_376.astype('float64')) # shape=(2, 9, 9)
func_338_call = mod.get_global_var('func_338')
func_340_call = mutated_mod.get_global_var('func_340')
call_392 = func_338_call()
call_393 = func_338_call()
output = relay.Tuple([uop_388,call_392,])
output2 = relay.Tuple([uop_390,call_393,])
func_398 = relay.Function([], output)
mod['func_398'] = func_398
mod = relay.transform.InferType()(mod)
mutated_mod['func_398'] = func_398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_398_call = mutated_mod.get_global_var('func_398')
call_399 = func_398_call()
output = call_399
func_400 = relay.Function([], output)
mutated_mod['func_400'] = func_400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_401 = relay.TupleGetItem(func_261_call(), 0)
call_402 = relay.TupleGetItem(func_263_call(), 0)
const_407 = relay.const([[[3.813353,-3.154650,-4.759575,7.794706,-9.886619,-5.361395,-8.255595,5.465555,-9.354104],[3.335606,8.292291,8.231213,-0.895494,-6.597712,-3.387660,9.979147,5.589444,2.285053],[3.239041,8.073347,-9.572340,-9.062923,-0.648301,1.143069,1.979099,-3.261660,-7.049451],[9.207128,-9.449683,-6.310993,1.793043,-1.446385,1.427399,-7.977464,-6.701984,-0.766926],[1.100288,2.363190,-4.446796,-0.371375,-2.011529,2.458921,2.984758,0.803011,-2.876035],[-2.591154,9.825364,-4.196794,-2.320312,-4.963250,-3.285534,7.533192,6.902560,9.112467],[-4.319251,6.046711,-9.125800,5.323879,3.086727,5.875302,2.713648,1.496844,-6.665601],[6.989454,-8.103869,-0.935215,3.083800,-6.906283,-0.545244,-9.294980,-1.768063,7.685581],[-2.493118,-9.498099,-2.488957,2.892154,2.185072,-7.132527,6.004822,5.218467,0.134680]],[[-8.983473,0.678468,-7.352443,3.225497,-2.292237,-3.141568,-3.106188,3.818544,1.917915],[4.371698,7.100096,2.674001,-1.627968,8.983281,4.262939,6.400563,8.302593,-1.973763],[8.482654,5.770546,2.147300,5.362014,-3.024519,-9.649381,-8.088264,0.675353,0.565701],[-7.919268,3.569656,5.755101,-4.637494,-0.662622,6.065754,9.397674,-1.507772,2.962685],[9.170445,-6.219897,4.012779,5.069820,-2.866628,3.331302,8.845407,3.136842,6.522683],[6.438132,-9.929896,-4.762086,5.699763,-9.850855,-9.836894,7.036987,-7.370278,1.151958],[4.946961,-0.116133,4.899258,5.521095,9.338982,0.920625,0.610132,-2.734295,6.698889],[7.701475,9.206390,-3.082507,2.136166,9.038570,7.955203,2.205737,6.843683,-6.142184],[6.788943,6.696249,9.898628,-9.436817,-8.996728,-9.175930,8.446178,-8.707162,6.857984]]], dtype = "float32")#candidate|407|(2, 9, 9)|const|float32
bop_408 = relay.bitwise_xor(call_401.astype('uint8'), relay.reshape(const_407.astype('uint8'), relay.shape_of(call_401))) # shape=(2, 9, 9)
bop_411 = relay.bitwise_xor(call_402.astype('uint8'), relay.reshape(const_407.astype('uint8'), relay.shape_of(call_402))) # shape=(2, 9, 9)
output = relay.Tuple([bop_408,])
output2 = relay.Tuple([bop_411,])
func_413 = relay.Function([], output)
mod['func_413'] = func_413
mod = relay.transform.InferType()(mod)
mutated_mod['func_413'] = func_413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_413_call = mutated_mod.get_global_var('func_413')
call_414 = func_413_call()
output = call_414
func_415 = relay.Function([], output)
mutated_mod['func_415'] = func_415
mutated_mod = relay.transform.InferType()(mutated_mod)
func_398_call = mod.get_global_var('func_398')
func_400_call = mutated_mod.get_global_var('func_400')
call_429 = relay.TupleGetItem(func_398_call(), 1)
call_430 = relay.TupleGetItem(func_400_call(), 1)
output = call_429
output2 = call_430
func_438 = relay.Function([], output)
mod['func_438'] = func_438
mod = relay.transform.InferType()(mod)
output = func_438()
func_439 = relay.Function([], output)
mutated_mod['func_439'] = func_439
mutated_mod = relay.transform.InferType()(mutated_mod)
var_516 = relay.var("var_516", dtype = "float64", shape = (7, 3, 5))#candidate|516|(7, 3, 5)|var|float64
uop_517 = relay.acos(var_516.astype('float64')) # shape=(7, 3, 5)
uop_519 = relay.asinh(var_516.astype('float64')) # shape=(7, 3, 5)
uop_527 = relay.sigmoid(uop_519.astype('float64')) # shape=(7, 3, 5)
bop_536 = relay.bitwise_xor(uop_527.astype('uint64'), relay.reshape(var_516.astype('uint64'), relay.shape_of(uop_527))) # shape=(7, 3, 5)
uop_542 = relay.exp(bop_536.astype('float32')) # shape=(7, 3, 5)
var_552 = relay.var("var_552", dtype = "float64", shape = (7, 3, 5))#candidate|552|(7, 3, 5)|var|float64
bop_553 = relay.less(var_516.astype('bool'), relay.reshape(var_552.astype('bool'), relay.shape_of(var_516))) # shape=(7, 3, 5)
output = relay.Tuple([uop_517,uop_542,bop_553,])
output2 = relay.Tuple([uop_517,uop_542,bop_553,])
func_561 = relay.Function([var_516,var_552,], output)
mod['func_561'] = func_561
mod = relay.transform.InferType()(mod)
var_562 = relay.var("var_562", dtype = "float64", shape = (7, 3, 5))#candidate|562|(7, 3, 5)|var|float64
var_563 = relay.var("var_563", dtype = "float64", shape = (7, 3, 5))#candidate|563|(7, 3, 5)|var|float64
output = func_561(var_562,var_563,)
func_564 = relay.Function([var_562,var_563,], output)
mutated_mod['func_564'] = func_564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_398_call = mod.get_global_var('func_398')
func_400_call = mutated_mod.get_global_var('func_400')
call_603 = relay.TupleGetItem(func_398_call(), 0)
call_604 = relay.TupleGetItem(func_400_call(), 0)
var_608 = relay.var("var_608", dtype = "float64", shape = (2, 9, 9))#candidate|608|(2, 9, 9)|var|float64
bop_609 = relay.bitwise_or(call_603.astype('int64'), relay.reshape(var_608.astype('int64'), relay.shape_of(call_603))) # shape=(2, 9, 9)
bop_612 = relay.bitwise_or(call_604.astype('int64'), relay.reshape(var_608.astype('int64'), relay.shape_of(call_604))) # shape=(2, 9, 9)
uop_618 = relay.asin(var_608.astype('float32')) # shape=(2, 9, 9)
func_561_call = mod.get_global_var('func_561')
func_564_call = mutated_mod.get_global_var('func_564')
const_633 = relay.const([-1.148515,-7.808809,-5.641634,2.056760,5.878168,-8.172388,-1.256367,-2.463574,1.167330,0.784208,-6.831883,-9.909257,6.010648,-6.227077,9.584601,-9.841791,3.131756,3.774135,7.991829,-9.701948,-9.593779,6.284700,9.162932,-2.040952,-7.823047,-0.290151,0.609245,2.428347,-0.920192,4.505033,-4.449156,0.912300,-2.467673,6.808866,-7.661110,6.678936,-0.801917,2.566437,-0.233853,-8.929662,0.451842,6.815938,-4.694792,3.201469,-4.399658,-4.795416,4.070676,-5.099395,8.291878,2.734758,9.007590,-8.863808,1.073494,1.557604,9.585053,-0.632760,0.091245,0.833830,8.683468,-7.744191,-1.222604,-3.193550,0.468690,6.059592,-2.919247,-6.908011,2.222970,7.494273,-1.400674,-5.439642,3.664716,-9.465525,-8.169100,-9.324414,7.039715,0.451731,3.960356,3.483361,8.313120,6.899556,1.042834,2.776241,-4.581901,4.300500,-8.255694,6.541416,-5.294348,-7.000058,2.013850,-6.638273,7.029882,-1.175007,1.419174,8.095525,4.727267,-2.991075,-1.521521,4.527893,4.647699,3.184778,0.954544,6.348169,2.003820,-3.835635,-3.785447], dtype = "float64")#candidate|633|(105,)|const|float64
call_632 = relay.TupleGetItem(func_561_call(relay.reshape(const_633.astype('float64'), [7, 3, 5]), relay.reshape(const_633.astype('float64'), [7, 3, 5]), ), 1)
call_634 = relay.TupleGetItem(func_564_call(relay.reshape(const_633.astype('float64'), [7, 3, 5]), relay.reshape(const_633.astype('float64'), [7, 3, 5]), ), 1)
func_338_call = mod.get_global_var('func_338')
func_340_call = mutated_mod.get_global_var('func_340')
call_637 = func_338_call()
call_638 = func_338_call()
uop_653 = relay.asinh(uop_618.astype('float64')) # shape=(2, 9, 9)
var_663 = relay.var("var_663", dtype = "float64", shape = (2, 9, 9))#candidate|663|(2, 9, 9)|var|float64
bop_664 = relay.greater_equal(uop_653.astype('bool'), relay.reshape(var_663.astype('bool'), relay.shape_of(uop_653))) # shape=(2, 9, 9)
output = relay.Tuple([bop_609,call_632,const_633,call_637,bop_664,])
output2 = relay.Tuple([bop_612,call_634,const_633,call_638,bop_664,])
func_667 = relay.Function([var_608,var_663,], output)
mod['func_667'] = func_667
mod = relay.transform.InferType()(mod)
mutated_mod['func_667'] = func_667
mutated_mod = relay.transform.InferType()(mutated_mod)
func_667_call = mutated_mod.get_global_var('func_667')
var_669 = relay.var("var_669", dtype = "float64", shape = (2, 9, 9))#candidate|669|(2, 9, 9)|var|float64
var_670 = relay.var("var_670", dtype = "float64", shape = (2, 9, 9))#candidate|670|(2, 9, 9)|var|float64
call_668 = func_667_call(var_669,var_670,)
output = call_668
func_671 = relay.Function([var_669,var_670,], output)
mutated_mod['func_671'] = func_671
mutated_mod = relay.transform.InferType()(mutated_mod)
func_398_call = mod.get_global_var('func_398')
func_400_call = mutated_mod.get_global_var('func_400')
call_685 = relay.TupleGetItem(func_398_call(), 1)
call_686 = relay.TupleGetItem(func_400_call(), 1)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_699 = relay.TupleGetItem(func_261_call(), 0)
call_700 = relay.TupleGetItem(func_263_call(), 0)
uop_713 = relay.log2(call_699.astype('float64')) # shape=(2, 9, 9)
uop_715 = relay.log2(call_700.astype('float64')) # shape=(2, 9, 9)
bop_721 = relay.logical_and(call_699.astype('bool'), relay.reshape(call_685.astype('bool'), relay.shape_of(call_699))) # shape=(2, 9, 9)
bop_724 = relay.logical_and(call_700.astype('bool'), relay.reshape(call_686.astype('bool'), relay.shape_of(call_700))) # shape=(2, 9, 9)
bop_725 = relay.subtract(uop_713.astype('uint8'), relay.reshape(call_699.astype('uint8'), relay.shape_of(uop_713))) # shape=(2, 9, 9)
bop_728 = relay.subtract(uop_715.astype('uint8'), relay.reshape(call_700.astype('uint8'), relay.shape_of(uop_715))) # shape=(2, 9, 9)
func_667_call = mod.get_global_var('func_667')
func_671_call = mutated_mod.get_global_var('func_671')
call_733 = relay.TupleGetItem(func_667_call(relay.reshape(bop_721.astype('float64'), [2, 9, 9]), relay.reshape(call_699.astype('float64'), [2, 9, 9]), ), 1)
call_734 = relay.TupleGetItem(func_671_call(relay.reshape(bop_721.astype('float64'), [2, 9, 9]), relay.reshape(call_699.astype('float64'), [2, 9, 9]), ), 1)
func_398_call = mod.get_global_var('func_398')
func_400_call = mutated_mod.get_global_var('func_400')
call_738 = relay.TupleGetItem(func_398_call(), 1)
call_739 = relay.TupleGetItem(func_400_call(), 1)
bop_740 = relay.logical_xor(call_685.astype('int32'), relay.reshape(bop_725.astype('int32'), relay.shape_of(call_685))) # shape=(2, 9, 9)
bop_743 = relay.logical_xor(call_686.astype('int32'), relay.reshape(bop_728.astype('int32'), relay.shape_of(call_686))) # shape=(2, 9, 9)
output = relay.Tuple([bop_721,call_733,call_738,bop_740,])
output2 = relay.Tuple([bop_724,call_734,call_739,bop_743,])
func_744 = relay.Function([], output)
mod['func_744'] = func_744
mod = relay.transform.InferType()(mod)
output = func_744()
func_745 = relay.Function([], output)
mutated_mod['func_745'] = func_745
mutated_mod = relay.transform.InferType()(mutated_mod)
var_779 = relay.var("var_779", dtype = "float32", shape = (7, 7, 2))#candidate|779|(7, 7, 2)|var|float32
uop_780 = relay.tan(var_779.astype('float32')) # shape=(7, 7, 2)
func_744_call = mod.get_global_var('func_744')
func_745_call = mutated_mod.get_global_var('func_745')
call_788 = relay.TupleGetItem(func_744_call(), 2)
call_789 = relay.TupleGetItem(func_745_call(), 2)
output = relay.Tuple([uop_780,call_788,])
output2 = relay.Tuple([uop_780,call_789,])
func_792 = relay.Function([var_779,], output)
mod['func_792'] = func_792
mod = relay.transform.InferType()(mod)
var_793 = relay.var("var_793", dtype = "float32", shape = (7, 7, 2))#candidate|793|(7, 7, 2)|var|float32
output = func_792(var_793)
func_794 = relay.Function([var_793], output)
mutated_mod['func_794'] = func_794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_838 = relay.TupleGetItem(func_261_call(), 0)
call_839 = relay.TupleGetItem(func_263_call(), 0)
func_561_call = mod.get_global_var('func_561')
func_564_call = mutated_mod.get_global_var('func_564')
var_845 = relay.var("var_845", dtype = "float64", shape = (21, 5))#candidate|845|(21, 5)|var|float64
call_844 = relay.TupleGetItem(func_561_call(relay.reshape(var_845.astype('float64'), [7, 3, 5]), relay.reshape(var_845.astype('float64'), [7, 3, 5]), ), 2)
call_846 = relay.TupleGetItem(func_564_call(relay.reshape(var_845.astype('float64'), [7, 3, 5]), relay.reshape(var_845.astype('float64'), [7, 3, 5]), ), 2)
func_744_call = mod.get_global_var('func_744')
func_745_call = mutated_mod.get_global_var('func_745')
call_850 = relay.TupleGetItem(func_744_call(), 0)
call_851 = relay.TupleGetItem(func_745_call(), 0)
bop_852 = relay.logical_or(call_850.astype('bool'), relay.reshape(call_838.astype('bool'), relay.shape_of(call_850))) # shape=(2, 9, 9)
bop_855 = relay.logical_or(call_851.astype('bool'), relay.reshape(call_839.astype('bool'), relay.shape_of(call_851))) # shape=(2, 9, 9)
output = relay.Tuple([call_844,var_845,bop_852,])
output2 = relay.Tuple([call_846,var_845,bop_855,])
func_856 = relay.Function([var_845,], output)
mod['func_856'] = func_856
mod = relay.transform.InferType()(mod)
var_857 = relay.var("var_857", dtype = "float64", shape = (21, 5))#candidate|857|(21, 5)|var|float64
output = func_856(var_857)
func_858 = relay.Function([var_857], output)
mutated_mod['func_858'] = func_858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_905 = relay.TupleGetItem(func_261_call(), 0)
call_906 = relay.TupleGetItem(func_263_call(), 0)
output = call_905
output2 = call_906
func_922 = relay.Function([], output)
mod['func_922'] = func_922
mod = relay.transform.InferType()(mod)
mutated_mod['func_922'] = func_922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_922_call = mutated_mod.get_global_var('func_922')
call_923 = func_922_call()
output = call_923
func_924 = relay.Function([], output)
mutated_mod['func_924'] = func_924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_413_call = mod.get_global_var('func_413')
func_415_call = mutated_mod.get_global_var('func_415')
call_931 = relay.TupleGetItem(func_413_call(), 0)
call_932 = relay.TupleGetItem(func_415_call(), 0)
func_856_call = mod.get_global_var('func_856')
func_858_call = mutated_mod.get_global_var('func_858')
var_943 = relay.var("var_943", dtype = "float64", shape = (105,))#candidate|943|(105,)|var|float64
call_942 = relay.TupleGetItem(func_856_call(relay.reshape(var_943.astype('float64'), [21, 5])), 0)
call_944 = relay.TupleGetItem(func_858_call(relay.reshape(var_943.astype('float64'), [21, 5])), 0)
uop_945 = relay.cosh(call_942.astype('float64')) # shape=(7, 3, 5)
uop_947 = relay.cosh(call_944.astype('float64')) # shape=(7, 3, 5)
uop_955 = relay.atanh(call_931.astype('float32')) # shape=(2, 9, 9)
uop_957 = relay.atanh(call_932.astype('float32')) # shape=(2, 9, 9)
output = relay.Tuple([var_943,uop_945,uop_955,])
output2 = relay.Tuple([var_943,uop_947,uop_957,])
func_963 = relay.Function([var_943,], output)
mod['func_963'] = func_963
mod = relay.transform.InferType()(mod)
var_964 = relay.var("var_964", dtype = "float64", shape = (105,))#candidate|964|(105,)|var|float64
output = func_963(var_964)
func_965 = relay.Function([var_964], output)
mutated_mod['func_965'] = func_965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_922_call = mod.get_global_var('func_922')
func_924_call = mutated_mod.get_global_var('func_924')
call_967 = func_922_call()
call_968 = func_922_call()
func_561_call = mod.get_global_var('func_561')
func_564_call = mutated_mod.get_global_var('func_564')
var_972 = relay.var("var_972", dtype = "float64", shape = (105,))#candidate|972|(105,)|var|float64
call_971 = relay.TupleGetItem(func_561_call(relay.reshape(var_972.astype('float64'), [7, 3, 5]), relay.reshape(var_972.astype('float64'), [7, 3, 5]), ), 1)
call_973 = relay.TupleGetItem(func_564_call(relay.reshape(var_972.astype('float64'), [7, 3, 5]), relay.reshape(var_972.astype('float64'), [7, 3, 5]), ), 1)
output = relay.Tuple([call_967,call_971,var_972,])
output2 = relay.Tuple([call_968,call_973,var_972,])
func_982 = relay.Function([var_972,], output)
mod['func_982'] = func_982
mod = relay.transform.InferType()(mod)
var_983 = relay.var("var_983", dtype = "float64", shape = (105,))#candidate|983|(105,)|var|float64
output = func_982(var_983)
func_984 = relay.Function([var_983], output)
mutated_mod['func_984'] = func_984
mutated_mod = relay.transform.InferType()(mutated_mod)
var_994 = relay.var("var_994", dtype = "uint8", shape = (14, 13, 13))#candidate|994|(14, 13, 13)|var|uint8
var_995 = relay.var("var_995", dtype = "uint8", shape = (14, 13, 13))#candidate|995|(14, 13, 13)|var|uint8
bop_996 = relay.bitwise_or(var_994.astype('uint8'), relay.reshape(var_995.astype('uint8'), relay.shape_of(var_994))) # shape=(14, 13, 13)
func_438_call = mod.get_global_var('func_438')
func_439_call = mutated_mod.get_global_var('func_439')
call_1016 = func_438_call()
call_1017 = func_438_call()
output = relay.Tuple([bop_996,call_1016,])
output2 = relay.Tuple([bop_996,call_1017,])
func_1024 = relay.Function([var_994,var_995,], output)
mod['func_1024'] = func_1024
mod = relay.transform.InferType()(mod)
mutated_mod['func_1024'] = func_1024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1024_call = mutated_mod.get_global_var('func_1024')
var_1026 = relay.var("var_1026", dtype = "uint8", shape = (14, 13, 13))#candidate|1026|(14, 13, 13)|var|uint8
var_1027 = relay.var("var_1027", dtype = "uint8", shape = (14, 13, 13))#candidate|1027|(14, 13, 13)|var|uint8
call_1025 = func_1024_call(var_1026,var_1027,)
output = call_1025
func_1028 = relay.Function([var_1026,var_1027,], output)
mutated_mod['func_1028'] = func_1028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_438_call = mod.get_global_var('func_438')
func_439_call = mutated_mod.get_global_var('func_439')
call_1117 = func_438_call()
call_1118 = func_438_call()
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_1122 = relay.TupleGetItem(func_261_call(), 0)
call_1123 = relay.TupleGetItem(func_263_call(), 0)
func_398_call = mod.get_global_var('func_398')
func_400_call = mutated_mod.get_global_var('func_400')
call_1130 = relay.TupleGetItem(func_398_call(), 0)
call_1131 = relay.TupleGetItem(func_400_call(), 0)
func_922_call = mod.get_global_var('func_922')
func_924_call = mutated_mod.get_global_var('func_924')
call_1151 = func_922_call()
call_1152 = func_922_call()
output = relay.Tuple([call_1117,call_1122,call_1130,call_1151,])
output2 = relay.Tuple([call_1118,call_1123,call_1131,call_1152,])
func_1154 = relay.Function([], output)
mod['func_1154'] = func_1154
mod = relay.transform.InferType()(mod)
output = func_1154()
func_1155 = relay.Function([], output)
mutated_mod['func_1155'] = func_1155
mutated_mod = relay.transform.InferType()(mutated_mod)
func_338_call = mod.get_global_var('func_338')
func_340_call = mutated_mod.get_global_var('func_340')
call_1192 = func_338_call()
call_1193 = func_338_call()
func_561_call = mod.get_global_var('func_561')
func_564_call = mutated_mod.get_global_var('func_564')
var_1199 = relay.var("var_1199", dtype = "float64", shape = (105,))#candidate|1199|(105,)|var|float64
call_1198 = relay.TupleGetItem(func_561_call(relay.reshape(var_1199.astype('float64'), [7, 3, 5]), relay.reshape(var_1199.astype('float64'), [7, 3, 5]), ), 0)
call_1200 = relay.TupleGetItem(func_564_call(relay.reshape(var_1199.astype('float64'), [7, 3, 5]), relay.reshape(var_1199.astype('float64'), [7, 3, 5]), ), 0)
func_667_call = mod.get_global_var('func_667')
func_671_call = mutated_mod.get_global_var('func_671')
call_1203 = relay.TupleGetItem(func_667_call(relay.reshape(call_1192.astype('float64'), [2, 9, 9]), relay.reshape(call_1192.astype('float64'), [2, 9, 9]), ), 1)
call_1204 = relay.TupleGetItem(func_671_call(relay.reshape(call_1192.astype('float64'), [2, 9, 9]), relay.reshape(call_1192.astype('float64'), [2, 9, 9]), ), 1)
output = relay.Tuple([call_1192,call_1198,var_1199,call_1203,])
output2 = relay.Tuple([call_1193,call_1200,var_1199,call_1204,])
func_1209 = relay.Function([var_1199,], output)
mod['func_1209'] = func_1209
mod = relay.transform.InferType()(mod)
mutated_mod['func_1209'] = func_1209
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1210 = relay.var("var_1210", dtype = "float64", shape = (105,))#candidate|1210|(105,)|var|float64
func_1209_call = mutated_mod.get_global_var('func_1209')
call_1211 = func_1209_call(var_1210)
output = call_1211
func_1212 = relay.Function([var_1210], output)
mutated_mod['func_1212'] = func_1212
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1227 = relay.var("var_1227", dtype = "uint16", shape = (5, 3, 4))#candidate|1227|(5, 3, 4)|var|uint16
var_1228 = relay.var("var_1228", dtype = "uint16", shape = (5, 3, 4))#candidate|1228|(5, 3, 4)|var|uint16
bop_1229 = relay.greater(var_1227.astype('bool'), relay.reshape(var_1228.astype('bool'), relay.shape_of(var_1227))) # shape=(5, 3, 4)
func_963_call = mod.get_global_var('func_963')
func_965_call = mutated_mod.get_global_var('func_965')
const_1235 = relay.const([-8.457845,8.134170,3.220461,0.951511,2.191210,-0.240940,8.131337,-0.876511,-9.506443,-6.075652,-5.118125,0.776829,3.890969,7.798783,4.908838,6.641056,-4.864478,-3.796778,-9.691343,-4.941170,-7.392246,4.894222,-4.039974,6.064609,2.418689,-0.171408,8.321375,-2.960875,4.770573,2.025415,-0.842319,1.337131,-6.273220,2.040958,4.525152,-0.807624,-5.720319,5.939066,3.659068,1.427257,-3.794861,-7.586137,3.063090,-5.319569,9.271062,0.705715,6.877759,-8.393375,4.519221,-4.094802,-3.316325,-8.620151,-3.096983,0.556737,5.883014,0.643441,4.221878,1.058255,-0.713354,6.450345,1.665927,-3.489806,8.315059,-2.244290,-9.208375,-2.905308,6.201117,3.456035,-2.152160,9.762779,-3.686231,-0.301160,4.662880,-4.662455,2.653628,5.351176,6.865594,3.241615,-7.062863,8.247836,5.645141,0.215342,-4.500912,-0.474647,-7.140735,-2.031509,-4.791967,-6.399969,-1.569798,-3.815956,-5.412262,0.303406,9.517689,2.549561,-8.329003,-9.398554,-3.961809,8.510768,-0.229367,1.098579,3.400282,9.548303,-3.473665,1.301218,1.837092], dtype = "float64")#candidate|1235|(105,)|const|float64
call_1234 = relay.TupleGetItem(func_963_call(relay.reshape(const_1235.astype('float64'), [105,])), 1)
call_1236 = relay.TupleGetItem(func_965_call(relay.reshape(const_1235.astype('float64'), [105,])), 1)
output = relay.Tuple([bop_1229,call_1234,const_1235,])
output2 = relay.Tuple([bop_1229,call_1236,const_1235,])
func_1237 = relay.Function([var_1227,var_1228,], output)
mod['func_1237'] = func_1237
mod = relay.transform.InferType()(mod)
mutated_mod['func_1237'] = func_1237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1237_call = mutated_mod.get_global_var('func_1237')
var_1239 = relay.var("var_1239", dtype = "uint16", shape = (5, 3, 4))#candidate|1239|(5, 3, 4)|var|uint16
var_1240 = relay.var("var_1240", dtype = "uint16", shape = (5, 3, 4))#candidate|1240|(5, 3, 4)|var|uint16
call_1238 = func_1237_call(var_1239,var_1240,)
output = call_1238
func_1241 = relay.Function([var_1239,var_1240,], output)
mutated_mod['func_1241'] = func_1241
mutated_mod = relay.transform.InferType()(mutated_mod)
func_438_call = mod.get_global_var('func_438')
func_439_call = mutated_mod.get_global_var('func_439')
call_1276 = func_438_call()
call_1277 = func_438_call()
func_922_call = mod.get_global_var('func_922')
func_924_call = mutated_mod.get_global_var('func_924')
call_1294 = func_922_call()
call_1295 = func_922_call()
bop_1296 = relay.less_equal(call_1294.astype('bool'), relay.reshape(call_1276.astype('bool'), relay.shape_of(call_1294))) # shape=(2, 9, 9)
bop_1299 = relay.less_equal(call_1295.astype('bool'), relay.reshape(call_1277.astype('bool'), relay.shape_of(call_1295))) # shape=(2, 9, 9)
func_1154_call = mod.get_global_var('func_1154')
func_1155_call = mutated_mod.get_global_var('func_1155')
call_1305 = relay.TupleGetItem(func_1154_call(), 3)
call_1306 = relay.TupleGetItem(func_1155_call(), 3)
func_1154_call = mod.get_global_var('func_1154')
func_1155_call = mutated_mod.get_global_var('func_1155')
call_1308 = relay.TupleGetItem(func_1154_call(), 3)
call_1309 = relay.TupleGetItem(func_1155_call(), 3)
func_922_call = mod.get_global_var('func_922')
func_924_call = mutated_mod.get_global_var('func_924')
call_1310 = func_922_call()
call_1311 = func_922_call()
func_922_call = mod.get_global_var('func_922')
func_924_call = mutated_mod.get_global_var('func_924')
call_1314 = func_922_call()
call_1315 = func_922_call()
func_744_call = mod.get_global_var('func_744')
func_745_call = mutated_mod.get_global_var('func_745')
call_1327 = relay.TupleGetItem(func_744_call(), 2)
call_1328 = relay.TupleGetItem(func_745_call(), 2)
func_338_call = mod.get_global_var('func_338')
func_340_call = mutated_mod.get_global_var('func_340')
call_1352 = func_338_call()
call_1353 = func_338_call()
output = relay.Tuple([bop_1296,call_1305,call_1308,call_1310,call_1314,call_1327,call_1352,])
output2 = relay.Tuple([bop_1299,call_1306,call_1309,call_1311,call_1315,call_1328,call_1353,])
func_1366 = relay.Function([], output)
mod['func_1366'] = func_1366
mod = relay.transform.InferType()(mod)
output = func_1366()
func_1367 = relay.Function([], output)
mutated_mod['func_1367'] = func_1367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_1368 = relay.TupleGetItem(func_261_call(), 0)
call_1369 = relay.TupleGetItem(func_263_call(), 0)
uop_1380 = relay.tan(call_1368.astype('float32')) # shape=(2, 9, 9)
uop_1382 = relay.tan(call_1369.astype('float32')) # shape=(2, 9, 9)
bop_1386 = relay.divide(call_1368.astype('float32'), relay.reshape(uop_1380.astype('float32'), relay.shape_of(call_1368))) # shape=(2, 9, 9)
bop_1389 = relay.divide(call_1369.astype('float32'), relay.reshape(uop_1382.astype('float32'), relay.shape_of(call_1369))) # shape=(2, 9, 9)
output = relay.Tuple([bop_1386,])
output2 = relay.Tuple([bop_1389,])
func_1397 = relay.Function([], output)
mod['func_1397'] = func_1397
mod = relay.transform.InferType()(mod)
output = func_1397()
func_1398 = relay.Function([], output)
mutated_mod['func_1398'] = func_1398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_398_call = mod.get_global_var('func_398')
func_400_call = mutated_mod.get_global_var('func_400')
call_1419 = relay.TupleGetItem(func_398_call(), 1)
call_1420 = relay.TupleGetItem(func_400_call(), 1)
func_792_call = mod.get_global_var('func_792')
func_794_call = mutated_mod.get_global_var('func_794')
var_1430 = relay.var("var_1430", dtype = "float32", shape = (7, 14))#candidate|1430|(7, 14)|var|float32
call_1429 = relay.TupleGetItem(func_792_call(relay.reshape(var_1430.astype('float32'), [7, 7, 2])), 0)
call_1431 = relay.TupleGetItem(func_794_call(relay.reshape(var_1430.astype('float32'), [7, 7, 2])), 0)
output = relay.Tuple([call_1419,call_1429,var_1430,])
output2 = relay.Tuple([call_1420,call_1431,var_1430,])
func_1439 = relay.Function([var_1430,], output)
mod['func_1439'] = func_1439
mod = relay.transform.InferType()(mod)
var_1440 = relay.var("var_1440", dtype = "float32", shape = (7, 14))#candidate|1440|(7, 14)|var|float32
output = func_1439(var_1440)
func_1441 = relay.Function([var_1440], output)
mutated_mod['func_1441'] = func_1441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1154_call = mod.get_global_var('func_1154')
func_1155_call = mutated_mod.get_global_var('func_1155')
call_1489 = relay.TupleGetItem(func_1154_call(), 2)
call_1490 = relay.TupleGetItem(func_1155_call(), 2)
output = call_1489
output2 = call_1490
func_1494 = relay.Function([], output)
mod['func_1494'] = func_1494
mod = relay.transform.InferType()(mod)
output = func_1494()
func_1495 = relay.Function([], output)
mutated_mod['func_1495'] = func_1495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1494_call = mod.get_global_var('func_1494')
func_1495_call = mutated_mod.get_global_var('func_1495')
call_1538 = func_1494_call()
call_1539 = func_1494_call()
func_1439_call = mod.get_global_var('func_1439')
func_1441_call = mutated_mod.get_global_var('func_1441')
const_1542 = relay.const([-0.058522,-7.330174,0.632787,-0.505216,7.860558,1.011021,-3.164301,6.784975,-6.807595,-2.910300,-6.895893,9.081728,0.019472,1.004681,-3.470244,-5.692963,-2.696634,3.537076,-6.936618,-3.332045,-3.255212,6.713890,-0.356002,1.283092,4.533359,8.124072,5.262758,-7.750976,5.888150,-5.964563,9.960621,5.321417,2.049911,8.417475,-4.635754,3.708635,-6.601259,-6.331724,-8.584026,9.864889,1.958284,2.553970,7.924522,5.081411,-5.170598,-5.602519,-0.466706,2.931450,-8.113558,0.547272,-1.202101,-1.704487,8.174828,7.028023,-3.936113,-7.214453,1.242978,-4.974474,3.780635,-7.690947,8.206101,-9.425320,-3.081998,-0.477072,-5.670917,3.950012,-6.745895,8.371215,-7.396871,2.314773,1.176253,-7.320290,-4.557323,6.162449,4.622829,9.125780,-4.147202,-7.374262,2.508834,-9.886580,9.091201,1.684472,4.388253,3.930224,8.364108,-9.908388,-9.529148,-1.628475,9.977230,3.825862,7.563129,-3.508411,-8.360652,-0.824518,9.668942,1.923630,-6.098630,-1.723577], dtype = "float32")#candidate|1542|(98,)|const|float32
call_1541 = relay.TupleGetItem(func_1439_call(relay.reshape(const_1542.astype('float32'), [7, 14])), 2)
call_1543 = relay.TupleGetItem(func_1441_call(relay.reshape(const_1542.astype('float32'), [7, 14])), 2)
output = relay.Tuple([call_1538,call_1541,const_1542,])
output2 = relay.Tuple([call_1539,call_1543,const_1542,])
func_1546 = relay.Function([], output)
mod['func_1546'] = func_1546
mod = relay.transform.InferType()(mod)
mutated_mod['func_1546'] = func_1546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1546_call = mutated_mod.get_global_var('func_1546')
call_1547 = func_1546_call()
output = call_1547
func_1548 = relay.Function([], output)
mutated_mod['func_1548'] = func_1548
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1571 = relay.var("var_1571", dtype = "int64", shape = (12, 7, 12))#candidate|1571|(12, 7, 12)|var|int64
var_1572 = relay.var("var_1572", dtype = "int64", shape = (12, 7, 12))#candidate|1572|(12, 7, 12)|var|int64
bop_1573 = relay.maximum(var_1571.astype('int64'), relay.reshape(var_1572.astype('int64'), relay.shape_of(var_1571))) # shape=(12, 7, 12)
output = bop_1573
output2 = bop_1573
func_1576 = relay.Function([var_1571,var_1572,], output)
mod['func_1576'] = func_1576
mod = relay.transform.InferType()(mod)
var_1577 = relay.var("var_1577", dtype = "int64", shape = (12, 7, 12))#candidate|1577|(12, 7, 12)|var|int64
var_1578 = relay.var("var_1578", dtype = "int64", shape = (12, 7, 12))#candidate|1578|(12, 7, 12)|var|int64
output = func_1576(var_1577,var_1578,)
func_1579 = relay.Function([var_1577,var_1578,], output)
mutated_mod['func_1579'] = func_1579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_744_call = mod.get_global_var('func_744')
func_745_call = mutated_mod.get_global_var('func_745')
call_1587 = relay.TupleGetItem(func_744_call(), 3)
call_1588 = relay.TupleGetItem(func_745_call(), 3)
output = call_1587
output2 = call_1588
func_1648 = relay.Function([], output)
mod['func_1648'] = func_1648
mod = relay.transform.InferType()(mod)
mutated_mod['func_1648'] = func_1648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1648_call = mutated_mod.get_global_var('func_1648')
call_1649 = func_1648_call()
output = call_1649
func_1650 = relay.Function([], output)
mutated_mod['func_1650'] = func_1650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1546_call = mod.get_global_var('func_1546')
func_1548_call = mutated_mod.get_global_var('func_1548')
call_1724 = relay.TupleGetItem(func_1546_call(), 0)
call_1725 = relay.TupleGetItem(func_1548_call(), 0)
output = call_1724
output2 = call_1725
func_1726 = relay.Function([], output)
mod['func_1726'] = func_1726
mod = relay.transform.InferType()(mod)
mutated_mod['func_1726'] = func_1726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1726_call = mutated_mod.get_global_var('func_1726')
call_1727 = func_1726_call()
output = call_1727
func_1728 = relay.Function([], output)
mutated_mod['func_1728'] = func_1728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_744_call = mod.get_global_var('func_744')
func_745_call = mutated_mod.get_global_var('func_745')
call_1737 = relay.TupleGetItem(func_744_call(), 1)
call_1738 = relay.TupleGetItem(func_745_call(), 1)
func_792_call = mod.get_global_var('func_792')
func_794_call = mutated_mod.get_global_var('func_794')
const_1746 = relay.const([[-4.605310,3.592430,-5.608908,8.970990,-2.059383,-0.508557,0.458060,-1.956560,-6.883481,5.187976,-0.818207,-8.035175,-8.276777,-2.673010],[0.390834,9.401830,-5.133537,8.342639,5.845510,-7.712081,-2.070958,2.710753,5.839960,6.101094,1.346081,9.129543,7.716039,1.225755],[4.676850,-6.164028,-0.716842,7.703223,-4.420363,-4.405684,8.381033,8.308174,8.854126,-1.769986,-7.216645,-6.273405,-2.201614,-1.119995],[2.472369,-1.263897,1.855416,-4.152123,-3.991648,9.657258,-0.077943,7.918127,-5.506608,-2.653107,7.377665,0.474575,-3.725330,2.145513],[3.422937,-7.415975,8.974511,3.893432,2.566443,1.825012,3.138493,-7.043656,-4.700178,-2.244156,9.049263,-2.702378,0.683976,-0.263932],[8.440782,-9.588825,3.847122,4.787606,2.101642,-5.258538,-0.683764,7.890072,-8.747218,-5.932554,1.903773,8.446136,3.555547,3.685782],[9.199186,-7.002901,3.853468,8.723978,-9.006344,4.864464,-1.508527,-3.405488,1.447930,-4.046622,-4.582219,-8.550334,4.970083,-8.185048]], dtype = "float32")#candidate|1746|(7, 14)|const|float32
call_1745 = relay.TupleGetItem(func_792_call(relay.reshape(const_1746.astype('float32'), [7, 7, 2])), 0)
call_1747 = relay.TupleGetItem(func_794_call(relay.reshape(const_1746.astype('float32'), [7, 7, 2])), 0)
uop_1750 = relay.sin(call_1737.astype('float64')) # shape=(7, 3, 5)
uop_1752 = relay.sin(call_1738.astype('float64')) # shape=(7, 3, 5)
output = relay.Tuple([call_1745,const_1746,uop_1750,])
output2 = relay.Tuple([call_1747,const_1746,uop_1752,])
func_1757 = relay.Function([], output)
mod['func_1757'] = func_1757
mod = relay.transform.InferType()(mod)
output = func_1757()
func_1758 = relay.Function([], output)
mutated_mod['func_1758'] = func_1758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1154_call = mod.get_global_var('func_1154')
func_1155_call = mutated_mod.get_global_var('func_1155')
call_1797 = relay.TupleGetItem(func_1154_call(), 2)
call_1798 = relay.TupleGetItem(func_1155_call(), 2)
output = relay.Tuple([call_1797,])
output2 = relay.Tuple([call_1798,])
func_1799 = relay.Function([], output)
mod['func_1799'] = func_1799
mod = relay.transform.InferType()(mod)
output = func_1799()
func_1800 = relay.Function([], output)
mutated_mod['func_1800'] = func_1800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_398_call = mod.get_global_var('func_398')
func_400_call = mutated_mod.get_global_var('func_400')
call_1858 = relay.TupleGetItem(func_398_call(), 1)
call_1859 = relay.TupleGetItem(func_400_call(), 1)
func_413_call = mod.get_global_var('func_413')
func_415_call = mutated_mod.get_global_var('func_415')
call_1866 = relay.TupleGetItem(func_413_call(), 0)
call_1867 = relay.TupleGetItem(func_415_call(), 0)
func_1209_call = mod.get_global_var('func_1209')
func_1212_call = mutated_mod.get_global_var('func_1212')
const_1876 = relay.const([-7.824619,7.248388,-7.501285,-8.978014,4.783935,3.482067,-8.116069,8.170623,7.507035,-1.714952,3.012544,-8.365956,6.872906,7.237145,9.597475,-3.580388,-6.046406,-8.580669,0.876043,-8.576026,-8.533512,-8.424319,-1.029590,-2.997211,3.799373,9.941364,8.275792,7.493220,6.788472,2.084966,9.058275,9.887681,1.377918,-5.010486,-6.594644,-9.509339,-0.998545,9.287028,-8.599695,-4.774356,4.490740,-7.017667,9.775616,8.638103,8.732263,9.527532,-3.059442,-4.791917,2.083274,3.401326,3.369415,-7.545386,-4.303084,8.980196,3.376946,-2.915579,0.320326,5.376583,9.093200,-0.911293,5.691979,3.136559,-1.432806,-7.717906,-9.822496,9.946999,5.430583,6.882532,-9.727155,-7.835823,-1.140719,-4.971716,-4.343159,4.313374,-7.357056,-7.506043,6.686147,8.923713,2.073846,4.812679,2.320117,-5.184395,-5.750873,1.482465,-7.236199,-1.418205,-6.154226,-5.470589,-1.705654,-7.630820,5.468430,0.075712,-4.483051,-2.693827,-9.525708,2.661797,5.777801,-5.317157,0.418221,-5.177873,2.009545,9.790196,1.830057,-2.059925,6.777091], dtype = "float64")#candidate|1876|(105,)|const|float64
call_1875 = relay.TupleGetItem(func_1209_call(relay.reshape(const_1876.astype('float64'), [105,])), 0)
call_1877 = relay.TupleGetItem(func_1212_call(relay.reshape(const_1876.astype('float64'), [105,])), 0)
func_1757_call = mod.get_global_var('func_1757')
func_1758_call = mutated_mod.get_global_var('func_1758')
call_1896 = relay.TupleGetItem(func_1757_call(), 0)
call_1897 = relay.TupleGetItem(func_1758_call(), 0)
func_398_call = mod.get_global_var('func_398')
func_400_call = mutated_mod.get_global_var('func_400')
call_1899 = relay.TupleGetItem(func_398_call(), 1)
call_1900 = relay.TupleGetItem(func_400_call(), 1)
func_982_call = mod.get_global_var('func_982')
func_984_call = mutated_mod.get_global_var('func_984')
call_1901 = relay.TupleGetItem(func_982_call(relay.reshape(const_1876.astype('float64'), [105,])), 0)
call_1902 = relay.TupleGetItem(func_984_call(relay.reshape(const_1876.astype('float64'), [105,])), 0)
output = relay.Tuple([call_1858,call_1866,call_1875,const_1876,call_1896,call_1899,call_1901,])
output2 = relay.Tuple([call_1859,call_1867,call_1877,const_1876,call_1897,call_1900,call_1902,])
func_1904 = relay.Function([], output)
mod['func_1904'] = func_1904
mod = relay.transform.InferType()(mod)
mutated_mod['func_1904'] = func_1904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1904_call = mutated_mod.get_global_var('func_1904')
call_1905 = func_1904_call()
output = call_1905
func_1906 = relay.Function([], output)
mutated_mod['func_1906'] = func_1906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1546_call = mod.get_global_var('func_1546')
func_1548_call = mutated_mod.get_global_var('func_1548')
call_1915 = relay.TupleGetItem(func_1546_call(), 1)
call_1916 = relay.TupleGetItem(func_1548_call(), 1)
output = call_1915
output2 = call_1916
func_1927 = relay.Function([], output)
mod['func_1927'] = func_1927
mod = relay.transform.InferType()(mod)
output = func_1927()
func_1928 = relay.Function([], output)
mutated_mod['func_1928'] = func_1928
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1927_call = mod.get_global_var('func_1927')
func_1928_call = mutated_mod.get_global_var('func_1928')
call_1963 = func_1927_call()
call_1964 = func_1927_call()
output = relay.Tuple([call_1963,])
output2 = relay.Tuple([call_1964,])
func_1966 = relay.Function([], output)
mod['func_1966'] = func_1966
mod = relay.transform.InferType()(mod)
mutated_mod['func_1966'] = func_1966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1966_call = mutated_mod.get_global_var('func_1966')
call_1967 = func_1966_call()
output = call_1967
func_1968 = relay.Function([], output)
mutated_mod['func_1968'] = func_1968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1757_call = mod.get_global_var('func_1757')
func_1758_call = mutated_mod.get_global_var('func_1758')
call_1975 = relay.TupleGetItem(func_1757_call(), 1)
call_1976 = relay.TupleGetItem(func_1758_call(), 1)
func_792_call = mod.get_global_var('func_792')
func_794_call = mutated_mod.get_global_var('func_794')
call_1985 = relay.TupleGetItem(func_792_call(relay.reshape(call_1975.astype('float32'), [7, 7, 2])), 1)
call_1986 = relay.TupleGetItem(func_794_call(relay.reshape(call_1975.astype('float32'), [7, 7, 2])), 1)
func_413_call = mod.get_global_var('func_413')
func_415_call = mutated_mod.get_global_var('func_415')
call_2003 = relay.TupleGetItem(func_413_call(), 0)
call_2004 = relay.TupleGetItem(func_415_call(), 0)
func_1494_call = mod.get_global_var('func_1494')
func_1495_call = mutated_mod.get_global_var('func_1495')
call_2007 = func_1494_call()
call_2008 = func_1494_call()
func_1366_call = mod.get_global_var('func_1366')
func_1367_call = mutated_mod.get_global_var('func_1367')
call_2012 = relay.TupleGetItem(func_1366_call(), 3)
call_2013 = relay.TupleGetItem(func_1367_call(), 3)
func_1024_call = mod.get_global_var('func_1024')
func_1028_call = mutated_mod.get_global_var('func_1028')
const_2017 = relay.const([[-10,-7,-5,-4,-3,8,10,9,10,-5,10,-3,8,-3],[7,-9,4,-4,10,-7,-4,2,10,1,7,-9,1,-5],[-1,2,-6,7,-9,-8,-10,10,1,-7,7,3,3,1],[3,-2,6,4,-5,3,-1,-2,7,4,-8,-9,8,-9],[3,4,-7,10,-8,-5,-5,-8,-9,-9,2,4,-4,-5],[6,-5,3,7,-6,5,-3,-9,-9,5,7,6,-7,9],[7,6,-7,4,-2,4,-8,-2,-9,9,9,-10,10,-4],[-8,10,9,9,-9,-8,4,7,-10,4,3,1,-7,-6],[9,-4,5,4,-10,-1,-8,9,2,-5,-6,-6,-10,1],[-10,-4,7,7,4,9,4,2,-9,-5,7,-5,-7,-4],[-8,6,-1,6,-10,3,4,-9,-10,-2,4,-1,-5,5],[-9,-1,-3,-4,9,4,3,-5,-7,-5,5,-7,-5,9],[-9,4,-5,-5,-3,-5,-9,6,-4,10,5,-10,3,9],[-10,-7,-5,6,-5,-10,-8,-3,-4,10,9,-1,5,7],[3,-7,-6,-1,-7,-3,-8,3,8,4,6,-9,-3,-9],[4,-10,4,9,4,-3,6,5,10,9,-3,-9,-6,4],[-1,-2,3,-1,9,-6,-9,-6,-6,-9,7,6,1,-1],[-6,-10,1,3,4,-10,-3,8,5,6,-2,-10,3,3],[1,-4,-10,-5,6,7,-1,5,-1,-5,6,10,6,-9],[3,-4,-7,-3,-5,-9,8,1,1,3,-8,10,2,1],[7,-9,-3,7,3,6,10,-9,9,8,-7,-4,3,-8],[-6,-5,1,5,8,4,4,1,5,-4,1,6,5,2],[8,3,1,6,1,-5,-3,-2,1,5,-5,-10,-1,4],[-10,1,8,-1,1,8,9,1,-6,-1,8,1,-4,-10],[1,8,2,-9,-5,-7,6,-8,-3,-8,-4,4,-4,-5],[-9,-1,1,-2,-3,3,-9,-6,-8,-1,5,-9,-8,-1],[9,-3,3,9,-5,6,1,-6,10,9,-6,8,-2,10],[-10,-4,-1,9,1,7,-10,6,2,4,-3,9,-5,-3],[-2,7,-8,-2,10,-10,-1,10,9,3,-7,-3,-1,-2],[-9,-3,7,-6,-5,-3,-10,-7,-9,-10,-1,2,-1,-8],[9,-9,2,3,4,-6,6,3,2,6,-6,-4,1,-5],[-2,7,3,-2,-9,-6,-2,3,2,7,7,7,-10,-8],[-6,-5,6,-10,9,-3,4,-5,-2,8,6,9,-9,-5],[-7,1,-6,2,10,2,-1,-10,-4,5,3,3,-9,1],[1,8,-8,3,-7,9,-6,-1,-4,4,-7,-6,-4,-2],[-1,2,10,10,-9,4,-8,7,2,3,-8,5,-7,8],[2,-4,-2,7,-8,-9,-1,-5,6,3,10,7,2,-5],[-5,-2,-2,1,5,-5,-6,10,-9,-4,-8,6,-2,8],[-3,5,-8,4,-3,6,-5,-1,-7,-6,-7,-1,9,3],[-8,-9,7,-10,3,7,-3,6,-3,-6,-7,7,5,8],[-7,9,-3,-10,-4,-5,6,-3,-4,4,-5,10,-5,5],[-6,7,-4,-1,-5,-5,-9,6,-4,-4,-5,8,1,1],[6,9,8,5,2,-7,7,8,4,-3,10,-7,-8,-6],[-4,6,-2,1,-2,-2,-4,-3,-10,-9,4,1,1,-2],[2,9,-4,5,1,6,4,-8,-6,9,2,10,-2,-2],[10,2,-2,7,6,-2,8,10,5,-8,9,-6,-7,-8],[9,2,6,1,-4,3,-8,1,-2,-8,9,7,5,-2],[2,-3,-2,10,10,-7,10,6,-5,-4,8,-4,-9,-8],[8,7,7,-3,-7,-8,-4,1,5,4,6,6,1,4],[3,-2,-9,-3,3,7,8,-6,2,-10,7,-8,-1,9],[-6,-2,5,2,-7,10,10,9,-7,-4,-2,-8,8,4],[-2,-1,-7,9,-9,6,7,-5,7,7,-6,-3,-7,7],[-8,-5,5,-1,1,4,1,5,8,-5,3,-7,2,9],[-2,5,9,-2,-7,7,-3,7,3,-9,3,3,5,9],[3,-9,4,7,-3,10,-4,-8,-9,10,-9,10,5,2],[-5,-9,6,-5,3,8,3,-8,4,-3,-2,-3,-1,5],[-8,6,-7,-4,-3,7,-1,4,2,10,-9,-9,3,2],[-4,-10,5,8,10,-8,10,-1,-10,-4,8,-10,-6,-7],[-10,-5,-9,9,-10,7,10,3,1,-3,-10,7,1,-8],[-6,-6,-6,-3,5,-9,10,4,-1,3,2,7,3,3],[-1,10,6,4,-6,-4,-8,5,9,1,8,-4,-10,-6],[4,6,10,5,-10,7,5,-7,6,-4,-3,7,-8,4],[1,-10,9,4,-10,7,-5,7,8,4,8,-1,2,-2],[6,-8,-8,-5,4,8,8,3,-2,5,4,5,9,3],[-1,-4,3,-7,-10,-7,2,8,1,-5,-2,2,-2,-8],[-1,2,7,9,8,10,8,4,-3,2,-4,4,7,-1],[-10,-10,1,-3,10,10,-9,7,8,-1,-4,2,10,-1],[1,-6,5,4,-9,-6,-10,-6,7,-8,7,-5,-10,6],[-4,-9,-10,-7,-4,-1,-7,-2,3,4,5,4,-1,10],[5,-3,2,-5,-10,9,5,-7,-7,7,-10,2,5,5],[5,9,-3,1,6,-10,-10,8,-9,8,-3,7,-10,-9],[5,10,1,-9,2,10,10,2,-10,-7,-7,-4,10,6],[-10,-4,10,4,5,-8,7,-5,-9,-7,9,-8,9,-9],[-5,10,9,-2,-9,-2,2,-1,7,6,-5,7,-6,-2],[-8,3,-3,1,-6,3,-1,-2,-3,2,1,10,-10,1],[3,-9,4,4,-7,-1,8,-10,9,4,7,3,-3,-5],[1,10,-1,3,-3,7,2,2,-4,-10,6,-4,-9,2],[-10,-8,-5,5,7,5,6,9,10,7,6,4,1,-5],[-4,6,-4,-7,1,6,1,-8,-3,-3,8,6,9,-4],[-7,5,-5,-7,5,9,7,4,9,5,6,-5,-9,-6],[1,3,10,1,-8,4,2,1,-9,7,6,-9,9,-9],[-7,9,7,-7,-1,-10,-7,-2,8,-10,8,-4,-1,-9],[1,1,2,-5,3,6,10,-2,-10,10,10,4,9,-4],[-5,3,10,-1,5,1,-9,3,-3,-8,1,-3,-10,-3],[-7,9,10,7,5,2,5,1,2,-5,9,8,-3,-3],[7,2,-2,7,5,4,3,2,-1,2,-7,8,2,5],[8,8,5,1,-1,1,-2,5,-1,5,-10,-5,4,2],[-1,1,9,5,7,1,-6,-3,-7,6,-7,-10,-8,5],[-10,7,-6,-1,8,-10,3,5,4,-8,10,1,-4,6],[7,3,-2,9,1,-4,-5,5,6,7,-2,2,-10,-1],[3,-4,1,-8,-8,-3,-4,-9,9,-8,6,6,-4,-1],[-1,-9,-2,-7,-2,7,1,-10,-5,7,-5,-1,-2,-10],[-5,-1,3,-3,2,-7,-6,-6,-2,-3,5,3,4,-2],[10,1,3,4,-1,-3,8,9,4,-2,-2,-7,4,9],[-3,2,-1,1,-6,-1,3,-10,-4,6,4,8,2,3],[3,-3,2,-4,-10,-8,1,3,-5,-4,4,9,-5,-4],[-10,2,-10,4,10,-7,-2,-9,6,6,7,-10,-9,8],[6,2,8,1,-8,-10,-2,3,1,8,5,9,-3,4],[-8,7,-4,-9,-2,-8,7,3,4,7,7,3,1,-6],[8,8,4,-1,-4,-9,-3,1,7,-1,-1,6,-6,-1],[-8,-3,9,-4,9,-9,6,-3,7,10,9,4,-10,7],[-9,2,7,8,9,9,7,-2,8,-5,9,-10,7,-8],[6,4,4,-7,-3,7,6,1,5,-8,1,1,-9,10],[-7,-4,2,10,-5,-6,-1,4,10,3,-1,10,4,-3],[2,-10,10,2,3,-9,-1,9,-8,9,8,-3,3,-2],[7,-4,9,-8,10,-2,-1,1,5,-4,-3,-3,5,2],[1,8,1,9,-6,8,6,-6,10,1,-9,10,-9,3],[-1,3,10,2,-1,-1,7,-2,-1,9,8,-9,-4,9],[2,-9,-10,6,4,-3,-8,-4,4,-5,-6,6,-4,-1],[6,4,-3,-2,5,-2,6,4,10,9,5,10,-10,-3],[3,-7,-5,6,3,-10,-6,5,-10,7,10,7,-2,5],[5,-8,-4,-7,5,-9,-3,-5,1,-4,3,-2,-7,-6],[-6,-3,-3,-1,-6,-7,4,-9,5,10,6,-9,-5,-9],[10,3,10,-8,7,-1,-8,3,-4,-10,6,5,4,-10],[4,1,-7,-1,10,-2,-9,-9,-1,8,5,-4,-8,3],[-2,-10,2,-2,8,8,3,5,2,8,8,-9,-5,-6],[-2,6,-1,10,-8,4,6,-5,5,2,6,1,9,1],[-2,7,-5,8,9,-3,10,4,1,-6,1,-4,-1,3],[6,2,-10,-4,3,-4,9,9,5,5,5,4,1,-5],[4,10,3,-2,2,9,-9,8,-10,-7,-2,-3,-6,-5],[5,-1,9,3,-5,4,-10,-3,-7,6,7,4,-8,8],[-4,-4,4,-9,7,2,6,9,10,4,-2,7,-6,3],[-8,1,-6,10,-8,-1,-1,-5,1,-5,-6,2,-1,-1],[2,10,-5,-9,-6,10,-9,9,6,-9,9,-9,2,7],[10,8,-10,-9,1,-7,-8,3,2,7,7,4,-9,5],[4,-3,-9,-6,3,-5,5,1,3,-3,7,10,8,-4],[-8,-6,-10,-7,-4,-8,-10,1,-9,1,8,4,3,-9],[-9,-6,1,-9,5,-10,1,-3,-4,-6,-7,-2,8,10],[1,4,4,7,4,-6,6,-7,5,7,6,-2,-8,-8],[2,2,1,1,6,1,-6,8,-5,8,-6,-1,8,-5],[-10,5,-5,3,-2,9,4,7,-9,3,-1,7,-6,10],[-4,10,-10,-5,-3,10,5,-3,-1,3,7,-5,-7,-6],[3,-6,-2,2,-3,-8,-7,2,-10,-3,7,-1,9,3],[-8,-10,-4,7,-3,2,4,-2,10,3,1,9,1,2],[-3,8,3,-2,2,-5,-6,3,-6,-3,9,4,-3,9],[2,3,-6,9,-9,-6,-10,-8,-7,8,-5,10,8,-5],[-9,-4,8,8,-10,-1,10,2,8,6,-10,-1,-7,1],[6,-8,-2,8,10,4,-7,-9,-2,-6,-10,8,-9,6],[-9,-3,5,-2,4,7,-7,5,5,10,-4,10,1,3],[6,-7,-6,-9,-2,8,-2,9,7,5,8,1,-2,-6],[-8,2,-10,-8,9,-9,-10,-6,-3,2,-9,-2,-2,6],[4,8,3,-8,1,9,-5,1,-7,-10,2,-2,10,-7],[-9,-8,-7,6,8,-2,2,-9,2,-4,8,1,5,2],[-9,10,6,-2,-4,-4,4,1,9,-5,-1,2,-3,3],[8,5,-6,7,1,-4,2,7,-4,-2,-8,4,5,3],[10,-6,-1,10,-4,-9,8,1,-1,-6,7,-8,6,-8],[-9,-7,-7,1,-3,-5,-8,3,-10,-8,3,6,1,-8],[-9,7,7,8,8,2,-2,10,3,-8,8,-6,9,2],[7,8,-4,3,-1,-7,-4,-2,-8,-6,6,6,9,4],[5,9,-3,9,2,-1,6,-5,9,-7,-2,9,-9,1],[-8,-8,-8,-6,-2,10,-8,-10,-3,3,4,8,-2,-5],[4,1,-10,5,-3,-1,-8,10,4,-8,-7,-6,10,-1],[10,5,10,6,-2,8,-3,-2,-9,-5,-4,-9,-4,6],[-10,-8,10,6,1,2,2,9,-8,-6,-5,10,-4,2],[6,3,4,-8,-7,6,6,-1,7,-6,3,4,3,-7],[4,6,-7,8,2,-8,2,-7,2,-7,-10,-6,6,-2],[5,-7,-1,9,-2,1,-4,-3,3,-5,7,-5,-6,3],[10,-1,5,4,-9,-5,-1,-4,-5,3,6,2,9,-4],[8,-7,3,5,-5,5,3,8,-6,1,9,7,10,-9],[-7,-6,-8,-3,-2,-10,-9,-5,-5,-6,-5,-10,3,-10],[-7,3,-1,8,3,-2,-2,-6,-7,3,5,-3,-10,-7],[-2,-5,-3,4,-9,-3,6,1,-8,-8,9,-7,5,-7],[2,-8,-10,-3,3,-6,10,5,7,-3,-3,1,6,-8],[-9,6,10,6,-8,2,-8,2,-10,-3,4,-3,9,-1],[-4,-4,6,4,5,-4,3,-2,6,9,4,-4,-10,-5],[1,-1,-7,-7,8,-6,3,6,8,7,4,10,9,-6],[1,7,-9,8,-7,8,-8,10,6,1,4,10,5,-7],[5,5,-5,9,-5,10,4,1,2,-7,-5,-6,6,8],[9,-8,-9,10,9,9,-10,10,-9,-8,-10,3,5,6]], dtype = "uint8")#candidate|2017|(169, 14)|const|uint8
call_2016 = relay.TupleGetItem(func_1024_call(relay.reshape(const_2017.astype('uint8'), [14, 13, 13]), relay.reshape(const_2017.astype('uint8'), [14, 13, 13]), ), 0)
call_2018 = relay.TupleGetItem(func_1028_call(relay.reshape(const_2017.astype('uint8'), [14, 13, 13]), relay.reshape(const_2017.astype('uint8'), [14, 13, 13]), ), 0)
uop_2026 = relay.erf(const_2017.astype('float64')) # shape=(169, 14)
func_413_call = mod.get_global_var('func_413')
func_415_call = mutated_mod.get_global_var('func_415')
call_2042 = relay.TupleGetItem(func_413_call(), 0)
call_2043 = relay.TupleGetItem(func_415_call(), 0)
func_1726_call = mod.get_global_var('func_1726')
func_1728_call = mutated_mod.get_global_var('func_1728')
call_2047 = func_1726_call()
call_2048 = func_1726_call()
func_1726_call = mod.get_global_var('func_1726')
func_1728_call = mutated_mod.get_global_var('func_1728')
call_2060 = func_1726_call()
call_2061 = func_1726_call()
uop_2067 = relay.log(uop_2026.astype('float32')) # shape=(169, 14)
func_1237_call = mod.get_global_var('func_1237')
func_1241_call = mutated_mod.get_global_var('func_1241')
var_2080 = relay.var("var_2080", dtype = "uint16", shape = (60,))#candidate|2080|(60,)|var|uint16
call_2079 = relay.TupleGetItem(func_1237_call(relay.reshape(var_2080.astype('uint16'), [5, 3, 4]), relay.reshape(var_2080.astype('uint16'), [5, 3, 4]), ), 0)
call_2081 = relay.TupleGetItem(func_1241_call(relay.reshape(var_2080.astype('uint16'), [5, 3, 4]), relay.reshape(var_2080.astype('uint16'), [5, 3, 4]), ), 0)
output = relay.Tuple([call_1975,call_1985,call_2003,call_2007,call_2012,call_2016,call_2042,call_2047,call_2060,uop_2067,call_2079,var_2080,])
output2 = relay.Tuple([call_1976,call_1986,call_2004,call_2008,call_2013,call_2018,call_2043,call_2048,call_2061,uop_2067,call_2081,var_2080,])
func_2085 = relay.Function([var_2080,], output)
mod['func_2085'] = func_2085
mod = relay.transform.InferType()(mod)
mutated_mod['func_2085'] = func_2085
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2086 = relay.var("var_2086", dtype = "uint16", shape = (60,))#candidate|2086|(60,)|var|uint16
func_2085_call = mutated_mod.get_global_var('func_2085')
call_2087 = func_2085_call(var_2086)
output = call_2087
func_2088 = relay.Function([var_2086], output)
mutated_mod['func_2088'] = func_2088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_398_call = mod.get_global_var('func_398')
func_400_call = mutated_mod.get_global_var('func_400')
call_2140 = relay.TupleGetItem(func_398_call(), 0)
call_2141 = relay.TupleGetItem(func_400_call(), 0)
uop_2146 = relay.sinh(call_2140.astype('float64')) # shape=(2, 9, 9)
uop_2148 = relay.sinh(call_2141.astype('float64')) # shape=(2, 9, 9)
uop_2163 = relay.sin(uop_2146.astype('float64')) # shape=(2, 9, 9)
uop_2165 = relay.sin(uop_2148.astype('float64')) # shape=(2, 9, 9)
output = uop_2163
output2 = uop_2165
func_2181 = relay.Function([], output)
mod['func_2181'] = func_2181
mod = relay.transform.InferType()(mod)
mutated_mod['func_2181'] = func_2181
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2181_call = mutated_mod.get_global_var('func_2181')
call_2182 = func_2181_call()
output = call_2182
func_2183 = relay.Function([], output)
mutated_mod['func_2183'] = func_2183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_744_call = mod.get_global_var('func_744')
func_745_call = mutated_mod.get_global_var('func_745')
call_2195 = relay.TupleGetItem(func_744_call(), 2)
call_2196 = relay.TupleGetItem(func_745_call(), 2)
func_792_call = mod.get_global_var('func_792')
func_794_call = mutated_mod.get_global_var('func_794')
var_2199 = relay.var("var_2199", dtype = "float32", shape = (98, 1))#candidate|2199|(98, 1)|var|float32
call_2198 = relay.TupleGetItem(func_792_call(relay.reshape(var_2199.astype('float32'), [7, 7, 2])), 0)
call_2200 = relay.TupleGetItem(func_794_call(relay.reshape(var_2199.astype('float32'), [7, 7, 2])), 0)
func_1576_call = mod.get_global_var('func_1576')
func_1579_call = mutated_mod.get_global_var('func_1579')
const_2204 = relay.const([-1,-6,-10,10,1,4,-3,-2,-4,-1,6,-5,8,9,1,-6,4,3,8,7,3,3,10,2,-6,6,10,5,3,1,-3,-6,1,-3,5,8,9,5,-9,-3,1,-6,-1,1,8,-1,1,8,-9,10,-8,5,10,-9,8,-3,-1,9,2,9,-2,-1,-8,-4,7,-2,-4,4,-6,4,-5,2,-8,10,-9,-1,9,-5,-8,-3,-4,-2,3,-4,-7,4,7,-9,-7,6,8,-8,-9,4,-3,-6,6,-5,2,-10,10,-2,-10,-6,10,4,9,-6,4,-10,9,-3,-2,5,-10,6,9,-10,10,7,-8,-9,10,7,-5,2,-1,-10,5,-8,10,-8,-3,-9,4,3,4,1,5,-1,-7,6,-10,-2,2,4,7,5,2,-2,-10,10,-7,10,-1,4,-6,7,-7,-2,2,-2,-8,6,1,-8,-3,4,1,3,7,-1,6,-8,10,1,-6,8,2,-5,4,-1,-4,-8,-1,9,8,8,10,6,-3,-2,2,2,6,6,-1,-8,3,7,8,-9,-8,2,-10,9,-7,-4,-3,-4,4,-10,6,7,5,-1,-4,1,7,1,2,-5,-3,8,5,-6,2,3,1,9,-8,10,3,3,5,-9,5,5,-5,7,-7,-1,6,-8,6,4,-8,-3,8,-10,1,9,5,6,-7,10,-4,4,4,7,-9,-3,7,-5,1,9,7,8,4,-10,6,6,10,2,-1,-4,-1,-7,-3,7,-10,-8,4,6,1,-8,9,-1,-3,-5,-1,5,7,4,4,8,8,10,-3,10,6,2,-4,-6,-3,3,1,-10,10,10,5,-10,3,5,-10,-9,2,2,2,3,9,1,-4,6,-5,1,-4,3,3,-3,-2,9,-4,10,-9,1,-8,5,5,7,-10,2,-9,3,-4,5,1,-7,-5,10,7,1,6,-7,-9,-3,-1,7,1,-4,-6,-8,-2,-1,2,-8,-5,-6,7,3,10,-7,10,-2,3,5,-2,-8,10,1,3,2,-10,-10,-4,3,9,-4,7,2,-2,1,2,8,3,5,-9,-5,-5,-8,-7,10,4,-7,-10,10,7,-5,3,4,-5,3,4,-4,2,-8,2,7,4,6,-4,-7,6,-4,7,4,-5,-5,4,9,-1,6,-7,-1,8,6,-2,5,-6,8,4,-5,-10,9,-2,-1,-5,10,2,2,9,-4,-2,-2,9,-2,-3,-2,-9,-6,-9,-6,5,-4,-7,1,-6,-8,5,7,-9,6,5,-4,1,5,-10,2,-7,4,-5,-2,1,9,10,-1,4,3,-7,2,-1,-6,8,-6,-6,-8,7,-2,-10,6,7,-10,-5,10,2,-10,9,-1,5,1,-8,-2,9,-3,9,8,7,8,-3,-3,-10,-5,8,7,5,-5,-7,8,-5,2,10,-1,-9,8,5,4,-4,-4,7,8,-9,5,-3,9,-5,3,2,4,-1,1,4,1,6,-4,9,7,6,2,-4,-9,-4,4,-6,-5,-1,-5,6,6,-3,7,4,-8,5,-2,-2,7,7,10,-2,-2,-3,-9,-5,1,5,10,1,2,1,-4,-6,7,-4,7,-3,-8,-8,-7,2,-2,5,8,3,1,-5,7,6,5,2,-6,4,3,-1,-4,-8,1,10,1,-9,-7,9,-6,-7,-7,-6,4,-8,-2,9,3,-4,-1,4,-10,-6,7,-1,2,-7,-7,-3,3,-1,-10,2,-8,-8,3,-2,-4,1,6,6,10,-7,8,-1,1,7,10,5,-10,-8,-4,7,9,-9,10,2,-9,-10,-9,10,-2,-1,8,2,-10,10,-9,2,-7,-4,4,-10,3,2,10,1,-8,-4,-10,-6,-7,6,5,5,-7,-8,4,-6,7,-8,1,-9,-4,7,1,6,-10,-5,8,-5,-10,-6,3,1,1,9,9,-10,2,6,-9,-3,-5,-3,2,-8,3,7,7,9,7,9,-7,10,-6,-5,1,5,-8,-10,8,-3,3,10,7,-1,7,-2,-1,-4,-1,4,-8,-9,-1,9,7,2,-3,4,-2,-6,-5,3,-1,4,7,5,9,2,-10,-1,2,-1,-8,4,-9,10,9,1,10,3,3,3,-9,-4,-5,-8,-8,3,-5,3,9,10,-9,-9,4,6,-9,1,-5,9,-8,10,-7,10,-2,-5,-8,-1,4,6,10,-7,-3,7,3,-10,2,-7,-3,-10,-3,7,8,8,6,3,-10,-6,-1,2,8,7,10,-8,2,-7,3,-6,-2,4,-10,3,-9,2,-2,4,-6,2,4,8,-10,-10,-1,-5,-1,-10,-7,-1,-3,-4,9,7,-8,1,8,7,6,-10,-4,-9,-3,-9,1,-5,-5,1,9,-9,-6,-1,10,4,-7,-5,9,-9,-1,5,8,-8,10,-9,7,8,-8,8,8,6,-8,8,4,-2,-6,9,-6,9,4,7,-5,5,-5,-3,-6,-10,-1,4,8,10,-4,9,6,7,3,-3,2,-2,-2,-2,4,-7,-2,10,-8,3,-9,-3,8,9,6,10,10,7,-4,2,-10,-7,-9,-10,7,-10,-6,5,3,-5,-4,6,-6,-7,1,2,-10,4,4,-8,-7,-9,-1,9,6,2,-9,-7,-3,-5,6,8,4,7,5,-1,6,-7,6,-1,-10,-4,3,-3,-6,3,-8,7,-10,-2,-10,9,-4,-2,-2,5,-4,-10,2], dtype = "int64")#candidate|2204|(1008,)|const|int64
call_2203 = func_1576_call(relay.reshape(const_2204.astype('int64'), [12, 7, 12]), relay.reshape(const_2204.astype('int64'), [12, 7, 12]), )
call_2205 = func_1576_call(relay.reshape(const_2204.astype('int64'), [12, 7, 12]), relay.reshape(const_2204.astype('int64'), [12, 7, 12]), )
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_2220 = relay.TupleGetItem(func_261_call(), 0)
call_2221 = relay.TupleGetItem(func_263_call(), 0)
func_338_call = mod.get_global_var('func_338')
func_340_call = mutated_mod.get_global_var('func_340')
call_2237 = func_338_call()
call_2238 = func_338_call()
uop_2253 = relay.exp(call_2203.astype('float64')) # shape=(12, 7, 12)
uop_2255 = relay.exp(call_2205.astype('float64')) # shape=(12, 7, 12)
uop_2271 = relay.tan(uop_2253.astype('float32')) # shape=(12, 7, 12)
uop_2273 = relay.tan(uop_2255.astype('float32')) # shape=(12, 7, 12)
output = relay.Tuple([call_2195,call_2198,var_2199,const_2204,call_2220,call_2237,uop_2271,])
output2 = relay.Tuple([call_2196,call_2200,var_2199,const_2204,call_2221,call_2238,uop_2273,])
func_2280 = relay.Function([var_2199,], output)
mod['func_2280'] = func_2280
mod = relay.transform.InferType()(mod)
mutated_mod['func_2280'] = func_2280
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2281 = relay.var("var_2281", dtype = "float32", shape = (98, 1))#candidate|2281|(98, 1)|var|float32
func_2280_call = mutated_mod.get_global_var('func_2280')
call_2282 = func_2280_call(var_2281)
output = call_2282
func_2283 = relay.Function([var_2281], output)
mutated_mod['func_2283'] = func_2283
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1366_call = mod.get_global_var('func_1366')
func_1367_call = mutated_mod.get_global_var('func_1367')
call_2309 = relay.TupleGetItem(func_1366_call(), 0)
call_2310 = relay.TupleGetItem(func_1367_call(), 0)
output = call_2309
output2 = call_2310
func_2320 = relay.Function([], output)
mod['func_2320'] = func_2320
mod = relay.transform.InferType()(mod)
mutated_mod['func_2320'] = func_2320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2320_call = mutated_mod.get_global_var('func_2320')
call_2321 = func_2320_call()
output = call_2321
func_2322 = relay.Function([], output)
mutated_mod['func_2322'] = func_2322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1757_call = mod.get_global_var('func_1757')
func_1758_call = mutated_mod.get_global_var('func_1758')
call_2457 = relay.TupleGetItem(func_1757_call(), 0)
call_2458 = relay.TupleGetItem(func_1758_call(), 0)
output = relay.Tuple([call_2457,])
output2 = relay.Tuple([call_2458,])
func_2477 = relay.Function([], output)
mod['func_2477'] = func_2477
mod = relay.transform.InferType()(mod)
mutated_mod['func_2477'] = func_2477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2477_call = mutated_mod.get_global_var('func_2477')
call_2478 = func_2477_call()
output = call_2478
func_2479 = relay.Function([], output)
mutated_mod['func_2479'] = func_2479
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2482 = relay.var("var_2482", dtype = "int16", shape = (11, 15, 5))#candidate|2482|(11, 15, 5)|var|int16
var_2483 = relay.var("var_2483", dtype = "int16", shape = (11, 15, 5))#candidate|2483|(11, 15, 5)|var|int16
bop_2484 = relay.add(var_2482.astype('int16'), relay.reshape(var_2483.astype('int16'), relay.shape_of(var_2482))) # shape=(11, 15, 5)
func_963_call = mod.get_global_var('func_963')
func_965_call = mutated_mod.get_global_var('func_965')
var_2491 = relay.var("var_2491", dtype = "float64", shape = (7, 15))#candidate|2491|(7, 15)|var|float64
call_2490 = relay.TupleGetItem(func_963_call(relay.reshape(var_2491.astype('float64'), [105,])), 0)
call_2492 = relay.TupleGetItem(func_965_call(relay.reshape(var_2491.astype('float64'), [105,])), 0)
func_1576_call = mod.get_global_var('func_1576')
func_1579_call = mutated_mod.get_global_var('func_1579')
var_2494 = relay.var("var_2494", dtype = "int64", shape = (4, 252))#candidate|2494|(4, 252)|var|int64
call_2493 = func_1576_call(relay.reshape(var_2494.astype('int64'), [12, 7, 12]), relay.reshape(var_2494.astype('int64'), [12, 7, 12]), )
call_2495 = func_1576_call(relay.reshape(var_2494.astype('int64'), [12, 7, 12]), relay.reshape(var_2494.astype('int64'), [12, 7, 12]), )
func_1648_call = mod.get_global_var('func_1648')
func_1650_call = mutated_mod.get_global_var('func_1650')
call_2500 = func_1648_call()
call_2501 = func_1648_call()
func_1209_call = mod.get_global_var('func_1209')
func_1212_call = mutated_mod.get_global_var('func_1212')
call_2505 = relay.TupleGetItem(func_1209_call(relay.reshape(call_2490.astype('float64'), [105,])), 2)
call_2506 = relay.TupleGetItem(func_1212_call(relay.reshape(call_2490.astype('float64'), [105,])), 2)
func_1648_call = mod.get_global_var('func_1648')
func_1650_call = mutated_mod.get_global_var('func_1650')
call_2531 = func_1648_call()
call_2532 = func_1648_call()
func_963_call = mod.get_global_var('func_963')
func_965_call = mutated_mod.get_global_var('func_965')
call_2539 = relay.TupleGetItem(func_963_call(relay.reshape(call_2490.astype('float64'), [105,])), 2)
call_2540 = relay.TupleGetItem(func_965_call(relay.reshape(call_2490.astype('float64'), [105,])), 2)
output = relay.Tuple([bop_2484,call_2490,var_2491,call_2493,var_2494,call_2500,call_2505,call_2531,call_2539,])
output2 = relay.Tuple([bop_2484,call_2492,var_2491,call_2495,var_2494,call_2501,call_2506,call_2532,call_2540,])
func_2565 = relay.Function([var_2482,var_2483,var_2491,var_2494,], output)
mod['func_2565'] = func_2565
mod = relay.transform.InferType()(mod)
var_2566 = relay.var("var_2566", dtype = "int16", shape = (11, 15, 5))#candidate|2566|(11, 15, 5)|var|int16
var_2567 = relay.var("var_2567", dtype = "int16", shape = (11, 15, 5))#candidate|2567|(11, 15, 5)|var|int16
var_2568 = relay.var("var_2568", dtype = "float64", shape = (7, 15))#candidate|2568|(7, 15)|var|float64
var_2569 = relay.var("var_2569", dtype = "int64", shape = (4, 252))#candidate|2569|(4, 252)|var|int64
output = func_2565(var_2566,var_2567,var_2568,var_2569,)
func_2570 = relay.Function([var_2566,var_2567,var_2568,var_2569,], output)
mutated_mod['func_2570'] = func_2570
mutated_mod = relay.transform.InferType()(mutated_mod)
func_744_call = mod.get_global_var('func_744')
func_745_call = mutated_mod.get_global_var('func_745')
call_2572 = relay.TupleGetItem(func_744_call(), 1)
call_2573 = relay.TupleGetItem(func_745_call(), 1)
var_2579 = relay.var("var_2579", dtype = "float32", shape = (7, 3, 5))#candidate|2579|(7, 3, 5)|var|float32
bop_2580 = relay.divide(call_2572.astype('float32'), relay.reshape(var_2579.astype('float32'), relay.shape_of(call_2572))) # shape=(7, 3, 5)
bop_2583 = relay.divide(call_2573.astype('float32'), relay.reshape(var_2579.astype('float32'), relay.shape_of(call_2573))) # shape=(7, 3, 5)
output = bop_2580
output2 = bop_2583
func_2594 = relay.Function([var_2579,], output)
mod['func_2594'] = func_2594
mod = relay.transform.InferType()(mod)
var_2595 = relay.var("var_2595", dtype = "float32", shape = (7, 3, 5))#candidate|2595|(7, 3, 5)|var|float32
output = func_2594(var_2595)
func_2596 = relay.Function([var_2595], output)
mutated_mod['func_2596'] = func_2596
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2604 = relay.var("var_2604", dtype = "bool", shape = (14, 7, 7))#candidate|2604|(14, 7, 7)|var|bool
const_2605 = relay.const([[[True,False,True,False,False,False,False],[True,False,True,False,False,False,True],[False,False,True,True,True,False,False],[True,True,True,True,False,True,True],[False,False,False,True,False,True,True],[False,True,True,True,False,False,True],[False,False,False,True,False,False,False]],[[False,False,False,True,True,False,True],[False,True,False,False,True,False,False],[True,True,True,True,True,True,False],[True,True,False,True,False,False,False],[False,False,False,False,True,True,False],[False,True,True,False,False,True,True],[True,False,True,False,True,False,True]],[[False,True,True,True,True,True,True],[True,False,True,True,False,False,False],[True,True,False,False,False,True,False],[False,False,True,True,False,False,True],[False,True,False,False,False,True,False],[True,True,True,False,True,False,False],[True,False,False,True,True,False,True]],[[True,True,True,True,True,True,False],[False,True,True,False,False,True,False],[True,True,False,False,False,True,True],[True,False,True,False,False,True,True],[False,True,False,True,False,False,True],[True,True,True,True,False,True,True],[True,False,False,False,True,False,False]],[[True,False,True,False,False,False,True],[False,True,False,False,False,True,False],[False,True,True,False,False,False,True],[False,True,True,True,False,True,True],[True,True,False,True,True,True,True],[True,False,False,False,True,True,False],[False,False,False,False,True,True,False]],[[True,False,False,True,True,True,True],[True,False,False,True,True,False,False],[True,False,True,False,False,False,False],[True,True,True,True,True,True,False],[False,True,False,True,True,False,False],[False,True,True,False,True,False,True],[True,False,True,False,False,False,False]],[[False,False,True,False,True,False,True],[False,True,True,False,False,False,True],[True,False,False,False,False,True,False],[True,True,True,False,False,False,False],[False,False,True,True,True,False,True],[False,False,False,True,True,False,True],[False,False,True,True,False,True,True]],[[False,False,True,False,False,False,False],[False,False,True,False,True,False,True],[False,False,False,False,False,True,True],[True,True,True,True,True,False,True],[True,True,False,False,True,False,False],[True,False,False,True,True,True,False],[False,True,True,False,True,False,False]],[[True,True,False,True,False,True,False],[True,True,True,False,False,False,False],[True,False,False,True,False,True,False],[True,False,False,True,False,False,True],[True,False,False,True,True,False,False],[True,True,False,False,False,False,False],[False,False,True,True,False,True,False]],[[False,False,True,False,True,True,True],[True,True,True,False,True,True,True],[False,True,True,True,False,False,True],[False,False,False,False,False,True,True],[False,False,False,False,True,True,False],[False,False,False,True,False,True,True],[True,False,True,False,True,False,True]],[[True,False,True,True,False,True,True],[False,False,False,False,False,False,True],[True,True,True,True,False,True,False],[False,False,False,True,False,True,True],[True,True,True,False,False,False,True],[False,True,False,True,True,True,True],[True,True,False,True,True,False,False]],[[True,True,True,True,False,True,False],[False,False,False,False,True,True,False],[True,True,False,False,False,False,True],[True,True,False,False,True,True,True],[False,True,False,True,False,True,False],[False,False,False,True,False,False,True],[True,True,True,True,False,True,True]],[[False,False,False,True,True,False,False],[False,True,True,False,False,True,True],[True,False,True,True,False,False,False],[False,False,True,False,False,True,True],[False,False,False,True,False,False,False],[False,False,False,False,False,False,True],[False,True,False,True,False,False,True]],[[False,False,True,True,False,True,True],[False,False,False,True,False,False,False],[True,False,False,True,False,True,True],[False,True,False,True,False,True,False],[False,True,True,True,True,True,False],[True,False,True,False,False,True,True],[False,True,True,True,True,True,False]]], dtype = "bool")#candidate|2605|(14, 7, 7)|const|bool
bop_2606 = relay.logical_and(var_2604.astype('bool'), relay.reshape(const_2605.astype('bool'), relay.shape_of(var_2604))) # shape=(14, 7, 7)
func_1397_call = mod.get_global_var('func_1397')
func_1398_call = mutated_mod.get_global_var('func_1398')
call_2609 = relay.TupleGetItem(func_1397_call(), 0)
call_2610 = relay.TupleGetItem(func_1398_call(), 0)
output = relay.Tuple([bop_2606,call_2609,])
output2 = relay.Tuple([bop_2606,call_2610,])
func_2618 = relay.Function([var_2604,], output)
mod['func_2618'] = func_2618
mod = relay.transform.InferType()(mod)
var_2619 = relay.var("var_2619", dtype = "bool", shape = (14, 7, 7))#candidate|2619|(14, 7, 7)|var|bool
output = func_2618(var_2619)
func_2620 = relay.Function([var_2619], output)
mutated_mod['func_2620'] = func_2620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_413_call = mod.get_global_var('func_413')
func_415_call = mutated_mod.get_global_var('func_415')
call_2772 = relay.TupleGetItem(func_413_call(), 0)
call_2773 = relay.TupleGetItem(func_415_call(), 0)
func_1209_call = mod.get_global_var('func_1209')
func_1212_call = mutated_mod.get_global_var('func_1212')
var_2777 = relay.var("var_2777", dtype = "float64", shape = (105,))#candidate|2777|(105,)|var|float64
call_2776 = relay.TupleGetItem(func_1209_call(relay.reshape(var_2777.astype('float64'), [105,])), 1)
call_2778 = relay.TupleGetItem(func_1212_call(relay.reshape(var_2777.astype('float64'), [105,])), 1)
output = relay.Tuple([call_2772,call_2776,var_2777,])
output2 = relay.Tuple([call_2773,call_2778,var_2777,])
func_2803 = relay.Function([var_2777,], output)
mod['func_2803'] = func_2803
mod = relay.transform.InferType()(mod)
var_2804 = relay.var("var_2804", dtype = "float64", shape = (105,))#candidate|2804|(105,)|var|float64
output = func_2803(var_2804)
func_2805 = relay.Function([var_2804], output)
mutated_mod['func_2805'] = func_2805
mutated_mod = relay.transform.InferType()(mutated_mod)
func_338_call = mod.get_global_var('func_338')
func_340_call = mutated_mod.get_global_var('func_340')
call_2855 = func_338_call()
call_2856 = func_338_call()
output = call_2855
output2 = call_2856
func_2857 = relay.Function([], output)
mod['func_2857'] = func_2857
mod = relay.transform.InferType()(mod)
mutated_mod['func_2857'] = func_2857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2857_call = mutated_mod.get_global_var('func_2857')
call_2858 = func_2857_call()
output = call_2858
func_2859 = relay.Function([], output)
mutated_mod['func_2859'] = func_2859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1154_call = mod.get_global_var('func_1154')
func_1155_call = mutated_mod.get_global_var('func_1155')
call_2876 = relay.TupleGetItem(func_1154_call(), 1)
call_2877 = relay.TupleGetItem(func_1155_call(), 1)
uop_2915 = relay.acosh(call_2876.astype('float32')) # shape=(2, 9, 9)
uop_2917 = relay.acosh(call_2877.astype('float32')) # shape=(2, 9, 9)
func_1237_call = mod.get_global_var('func_1237')
func_1241_call = mutated_mod.get_global_var('func_1241')
var_2922 = relay.var("var_2922", dtype = "uint16", shape = (60,))#candidate|2922|(60,)|var|uint16
call_2921 = relay.TupleGetItem(func_1237_call(relay.reshape(var_2922.astype('uint16'), [5, 3, 4]), relay.reshape(var_2922.astype('uint16'), [5, 3, 4]), ), 1)
call_2923 = relay.TupleGetItem(func_1241_call(relay.reshape(var_2922.astype('uint16'), [5, 3, 4]), relay.reshape(var_2922.astype('uint16'), [5, 3, 4]), ), 1)
func_2477_call = mod.get_global_var('func_2477')
func_2479_call = mutated_mod.get_global_var('func_2479')
call_2945 = relay.TupleGetItem(func_2477_call(), 0)
call_2946 = relay.TupleGetItem(func_2479_call(), 0)
output = relay.Tuple([uop_2915,call_2921,var_2922,call_2945,])
output2 = relay.Tuple([uop_2917,call_2923,var_2922,call_2946,])
func_2953 = relay.Function([var_2922,], output)
mod['func_2953'] = func_2953
mod = relay.transform.InferType()(mod)
var_2954 = relay.var("var_2954", dtype = "uint16", shape = (60,))#candidate|2954|(60,)|var|uint16
output = func_2953(var_2954)
func_2955 = relay.Function([var_2954], output)
mutated_mod['func_2955'] = func_2955
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3056 = relay.const(-7, dtype = "int8")#candidate|3056|()|const|int8
var_3057 = relay.var("var_3057", dtype = "int8", shape = (4, 5, 7))#candidate|3057|(4, 5, 7)|var|int8
bop_3058 = relay.not_equal(const_3056.astype('bool'), var_3057.astype('bool')) # shape=(4, 5, 7)
uop_3068 = relay.atan(bop_3058.astype('float32')) # shape=(4, 5, 7)
func_2594_call = mod.get_global_var('func_2594')
func_2596_call = mutated_mod.get_global_var('func_2596')
const_3072 = relay.const([-4.732698,4.644446,-2.809132,6.168012,8.887580,-2.025687,-7.683822,-4.387572,3.408067,1.768578,-3.995866,9.588936,-8.958282,8.103540,-7.867672,-5.615276,7.805603,-6.018595,-6.025101,8.194954,1.724361,-8.646553,-9.725396,3.664361,-7.620835,-6.334184,2.633179,-7.096846,9.972344,-7.631596,-9.206153,-8.737610,-7.885502,9.689245,-1.611665,9.585138,6.983401,3.086654,-2.320671,6.684463,8.710611,-0.579421,6.666361,-9.522801,-5.963244,-4.913137,-4.591635,-5.029048,7.304201,2.423888,-2.266667,5.643149,-3.101732,-8.846077,-7.409878,-0.353094,4.091063,-7.342597,1.377467,6.102955,5.386354,-6.693754,-9.729426,5.960874,9.619449,-0.925538,0.703303,8.866066,-1.993537,-4.583679,1.938670,4.721349,3.381274,5.604097,-6.296463,2.647682,-1.923456,2.190742,-3.605602,-9.862625,-5.255646,-3.053062,-7.391911,3.522784,8.772009,6.668986,-9.767395,6.399077,8.343335,-0.293721,-4.063340,0.340374,-2.504778,1.168741,7.735399,-8.664140,-5.448395,7.555227,-2.669241,-5.453508,2.516564,-6.219064,-2.462396,2.542883,-2.103814], dtype = "float32")#candidate|3072|(105,)|const|float32
call_3071 = func_2594_call(relay.reshape(const_3072.astype('float32'), [7, 3, 5]))
call_3073 = func_2594_call(relay.reshape(const_3072.astype('float32'), [7, 3, 5]))
func_1726_call = mod.get_global_var('func_1726')
func_1728_call = mutated_mod.get_global_var('func_1728')
call_3074 = func_1726_call()
call_3075 = func_1726_call()
output = relay.Tuple([uop_3068,call_3071,const_3072,call_3074,])
output2 = relay.Tuple([uop_3068,call_3073,const_3072,call_3075,])
func_3089 = relay.Function([var_3057,], output)
mod['func_3089'] = func_3089
mod = relay.transform.InferType()(mod)
var_3090 = relay.var("var_3090", dtype = "int8", shape = (4, 5, 7))#candidate|3090|(4, 5, 7)|var|int8
output = func_3089(var_3090)
func_3091 = relay.Function([var_3090], output)
mutated_mod['func_3091'] = func_3091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1546_call = mod.get_global_var('func_1546')
func_1548_call = mutated_mod.get_global_var('func_1548')
call_3119 = relay.TupleGetItem(func_1546_call(), 2)
call_3120 = relay.TupleGetItem(func_1548_call(), 2)
func_1546_call = mod.get_global_var('func_1546')
func_1548_call = mutated_mod.get_global_var('func_1548')
call_3126 = relay.TupleGetItem(func_1546_call(), 2)
call_3127 = relay.TupleGetItem(func_1548_call(), 2)
func_2565_call = mod.get_global_var('func_2565')
func_2570_call = mutated_mod.get_global_var('func_2570')
var_3129 = relay.var("var_3129", dtype = "int16", shape = (55, 15))#candidate|3129|(55, 15)|var|int16
const_3130 = relay.const([-8.380593,6.370283,1.978460,-1.263506,-3.781558,7.096079,-3.459380,2.311583,-4.680473,-9.145419,-9.164711,1.394107,-4.280303,4.970516,-2.915719,1.777142,4.407851,5.270021,-5.277448,9.571906,-3.370247,-4.962225,5.674953,-1.907290,-8.633946,-1.399772,6.567402,2.894111,-1.475978,3.490204,9.649982,7.698789,8.098566,8.754419,-2.000149,3.620203,4.892889,-7.580039,0.211565,-6.828208,5.556680,-0.968097,2.212034,-3.562018,-9.761414,-7.583852,-2.631241,-1.409274,-5.215252,-9.606521,7.249418,-1.797332,0.223139,5.848878,9.228333,-1.992048,0.455501,2.358192,-3.604842,-7.116363,6.392133,-5.927608,-2.865434,-5.325405,-0.160433,6.334874,-4.716763,1.168768,-7.257748,-0.708878,-7.742422,2.971835,2.966981,-9.155750,-3.416102,-8.983086,0.143504,-4.323428,-7.171778,7.487939,1.101011,-7.191682,-8.419400,5.425822,-3.513584,-4.428480,2.738671,-4.065277,-7.283869,-2.423387,4.642502,-6.174561,-3.797873,-2.358821,8.779272,5.361721,2.726508,-2.618078,9.844857,-7.090049,9.252241,1.985970,-1.606189,7.436493,-5.174073], dtype = "float64")#candidate|3130|(105,)|const|float64
var_3131 = relay.var("var_3131", dtype = "int64", shape = (1008,))#candidate|3131|(1008,)|var|int64
call_3128 = relay.TupleGetItem(func_2565_call(relay.reshape(var_3129.astype('int16'), [11, 15, 5]), relay.reshape(var_3129.astype('int16'), [11, 15, 5]), relay.reshape(const_3130.astype('float64'), [7, 15]), relay.reshape(var_3131.astype('int64'), [4, 252]), ), 6)
call_3132 = relay.TupleGetItem(func_2570_call(relay.reshape(var_3129.astype('int16'), [11, 15, 5]), relay.reshape(var_3129.astype('int16'), [11, 15, 5]), relay.reshape(const_3130.astype('float64'), [7, 15]), relay.reshape(var_3131.astype('int64'), [4, 252]), ), 6)
output = relay.Tuple([call_3119,call_3126,call_3128,var_3129,const_3130,var_3131,])
output2 = relay.Tuple([call_3120,call_3127,call_3132,var_3129,const_3130,var_3131,])
func_3148 = relay.Function([var_3129,var_3131,], output)
mod['func_3148'] = func_3148
mod = relay.transform.InferType()(mod)
var_3149 = relay.var("var_3149", dtype = "int16", shape = (55, 15))#candidate|3149|(55, 15)|var|int16
var_3150 = relay.var("var_3150", dtype = "int64", shape = (1008,))#candidate|3150|(1008,)|var|int64
output = func_3148(var_3149,var_3150,)
func_3151 = relay.Function([var_3149,var_3150,], output)
mutated_mod['func_3151'] = func_3151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_922_call = mod.get_global_var('func_922')
func_924_call = mutated_mod.get_global_var('func_924')
call_3183 = func_922_call()
call_3184 = func_922_call()
func_1648_call = mod.get_global_var('func_1648')
func_1650_call = mutated_mod.get_global_var('func_1650')
call_3185 = func_1648_call()
call_3186 = func_1648_call()
output = relay.Tuple([call_3183,call_3185,])
output2 = relay.Tuple([call_3184,call_3186,])
func_3188 = relay.Function([], output)
mod['func_3188'] = func_3188
mod = relay.transform.InferType()(mod)
output = func_3188()
func_3189 = relay.Function([], output)
mutated_mod['func_3189'] = func_3189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1546_call = mod.get_global_var('func_1546')
func_1548_call = mutated_mod.get_global_var('func_1548')
call_3307 = relay.TupleGetItem(func_1546_call(), 0)
call_3308 = relay.TupleGetItem(func_1548_call(), 0)
output = relay.Tuple([call_3307,])
output2 = relay.Tuple([call_3308,])
func_3381 = relay.Function([], output)
mod['func_3381'] = func_3381
mod = relay.transform.InferType()(mod)
mutated_mod['func_3381'] = func_3381
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3381_call = mutated_mod.get_global_var('func_3381')
call_3382 = func_3381_call()
output = call_3382
func_3383 = relay.Function([], output)
mutated_mod['func_3383'] = func_3383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1648_call = mod.get_global_var('func_1648')
func_1650_call = mutated_mod.get_global_var('func_1650')
call_3481 = func_1648_call()
call_3482 = func_1648_call()
output = relay.Tuple([call_3481,])
output2 = relay.Tuple([call_3482,])
func_3498 = relay.Function([], output)
mod['func_3498'] = func_3498
mod = relay.transform.InferType()(mod)
mutated_mod['func_3498'] = func_3498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3498_call = mutated_mod.get_global_var('func_3498')
call_3499 = func_3498_call()
output = call_3499
func_3500 = relay.Function([], output)
mutated_mod['func_3500'] = func_3500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1546_call = mod.get_global_var('func_1546')
func_1548_call = mutated_mod.get_global_var('func_1548')
call_3523 = relay.TupleGetItem(func_1546_call(), 0)
call_3524 = relay.TupleGetItem(func_1548_call(), 0)
output = call_3523
output2 = call_3524
func_3525 = relay.Function([], output)
mod['func_3525'] = func_3525
mod = relay.transform.InferType()(mod)
output = func_3525()
func_3526 = relay.Function([], output)
mutated_mod['func_3526'] = func_3526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1927_call = mod.get_global_var('func_1927')
func_1928_call = mutated_mod.get_global_var('func_1928')
call_3538 = func_1927_call()
call_3539 = func_1927_call()
func_856_call = mod.get_global_var('func_856')
func_858_call = mutated_mod.get_global_var('func_858')
const_3541 = relay.const([[-9.561205,7.590180,6.158392,3.046287,-9.079071],[-4.959831,-0.886753,-5.367715,9.147178,1.299487],[-9.332482,4.125406,-9.232315,3.330320,-8.343693],[6.313848,-3.291594,-8.134616,2.534972,3.595598],[2.744004,-7.340249,8.424150,-2.749132,1.136074],[3.302892,-9.835211,-8.451218,9.568093,-8.146520],[-9.354706,-6.517982,-5.472415,-4.018675,-9.838478],[4.823561,-9.261159,6.287673,-1.498869,-0.978955],[-7.122239,9.165884,4.587074,7.659774,-8.216051],[-5.541962,-1.060320,9.333196,9.666764,-4.427709],[-8.115462,5.330267,9.575068,-5.890430,-1.281990],[7.518470,-7.842177,-6.616722,-9.257281,-6.072858],[0.037130,1.104854,1.826722,-0.118062,7.379835],[4.437338,-1.124501,-0.435006,0.760594,3.741727],[8.393015,-6.756051,3.684392,5.064486,0.248411],[-8.253383,-7.790468,-0.886018,3.754522,-9.771230],[3.764151,-9.591563,4.811410,-8.664352,7.791640],[-5.519107,-2.038593,7.844032,7.326574,-7.771950],[-2.239322,6.153890,-9.799784,1.240364,-7.395997],[-8.782881,6.204774,6.080160,7.579178,1.187768],[9.968374,-6.693420,9.087773,-2.618458,-4.648108]], dtype = "float64")#candidate|3541|(21, 5)|const|float64
call_3540 = relay.TupleGetItem(func_856_call(relay.reshape(const_3541.astype('float64'), [21, 5])), 0)
call_3542 = relay.TupleGetItem(func_858_call(relay.reshape(const_3541.astype('float64'), [21, 5])), 0)
func_3188_call = mod.get_global_var('func_3188')
func_3189_call = mutated_mod.get_global_var('func_3189')
call_3544 = relay.TupleGetItem(func_3188_call(), 1)
call_3545 = relay.TupleGetItem(func_3189_call(), 1)
output = relay.Tuple([call_3538,call_3540,const_3541,call_3544,])
output2 = relay.Tuple([call_3539,call_3542,const_3541,call_3545,])
func_3547 = relay.Function([], output)
mod['func_3547'] = func_3547
mod = relay.transform.InferType()(mod)
mutated_mod['func_3547'] = func_3547
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3547_call = mutated_mod.get_global_var('func_3547')
call_3548 = func_3547_call()
output = call_3548
func_3549 = relay.Function([], output)
mutated_mod['func_3549'] = func_3549
mutated_mod = relay.transform.InferType()(mutated_mod)
func_922_call = mod.get_global_var('func_922')
func_924_call = mutated_mod.get_global_var('func_924')
call_3559 = func_922_call()
call_3560 = func_922_call()
output = call_3559
output2 = call_3560
func_3564 = relay.Function([], output)
mod['func_3564'] = func_3564
mod = relay.transform.InferType()(mod)
mutated_mod['func_3564'] = func_3564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3564_call = mutated_mod.get_global_var('func_3564')
call_3565 = func_3564_call()
output = call_3565
func_3566 = relay.Function([], output)
mutated_mod['func_3566'] = func_3566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1757_call = mod.get_global_var('func_1757')
func_1758_call = mutated_mod.get_global_var('func_1758')
call_3588 = relay.TupleGetItem(func_1757_call(), 1)
call_3589 = relay.TupleGetItem(func_1758_call(), 1)
output = call_3588
output2 = call_3589
func_3591 = relay.Function([], output)
mod['func_3591'] = func_3591
mod = relay.transform.InferType()(mod)
output = func_3591()
func_3592 = relay.Function([], output)
mutated_mod['func_3592'] = func_3592
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3615 = relay.var("var_3615", dtype = "float64", shape = (6, 7, 16))#candidate|3615|(6, 7, 16)|var|float64
uop_3616 = relay.rsqrt(var_3615.astype('float64')) # shape=(6, 7, 16)
output = relay.Tuple([uop_3616,])
output2 = relay.Tuple([uop_3616,])
func_3625 = relay.Function([var_3615,], output)
mod['func_3625'] = func_3625
mod = relay.transform.InferType()(mod)
var_3626 = relay.var("var_3626", dtype = "float64", shape = (6, 7, 16))#candidate|3626|(6, 7, 16)|var|float64
output = func_3625(var_3626)
func_3627 = relay.Function([var_3626], output)
mutated_mod['func_3627'] = func_3627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2181_call = mod.get_global_var('func_2181')
func_2183_call = mutated_mod.get_global_var('func_2183')
call_3638 = func_2181_call()
call_3639 = func_2181_call()
output = call_3638
output2 = call_3639
func_3648 = relay.Function([], output)
mod['func_3648'] = func_3648
mod = relay.transform.InferType()(mod)
output = func_3648()
func_3649 = relay.Function([], output)
mutated_mod['func_3649'] = func_3649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3525_call = mod.get_global_var('func_3525')
func_3526_call = mutated_mod.get_global_var('func_3526')
call_3669 = func_3525_call()
call_3670 = func_3525_call()
output = relay.Tuple([call_3669,])
output2 = relay.Tuple([call_3670,])
func_3676 = relay.Function([], output)
mod['func_3676'] = func_3676
mod = relay.transform.InferType()(mod)
output = func_3676()
func_3677 = relay.Function([], output)
mutated_mod['func_3677'] = func_3677
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3685 = relay.var("var_3685", dtype = "uint64", shape = (13, 3, 12))#candidate|3685|(13, 3, 12)|var|uint64
var_3686 = relay.var("var_3686", dtype = "uint64", shape = (13, 3, 12))#candidate|3686|(13, 3, 12)|var|uint64
bop_3687 = relay.less_equal(var_3685.astype('bool'), relay.reshape(var_3686.astype('bool'), relay.shape_of(var_3685))) # shape=(13, 3, 12)
func_1904_call = mod.get_global_var('func_1904')
func_1906_call = mutated_mod.get_global_var('func_1906')
call_3693 = relay.TupleGetItem(func_1904_call(), 2)
call_3694 = relay.TupleGetItem(func_1906_call(), 2)
output = relay.Tuple([bop_3687,call_3693,])
output2 = relay.Tuple([bop_3687,call_3694,])
func_3695 = relay.Function([var_3685,var_3686,], output)
mod['func_3695'] = func_3695
mod = relay.transform.InferType()(mod)
mutated_mod['func_3695'] = func_3695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3695_call = mutated_mod.get_global_var('func_3695')
var_3697 = relay.var("var_3697", dtype = "uint64", shape = (13, 3, 12))#candidate|3697|(13, 3, 12)|var|uint64
var_3698 = relay.var("var_3698", dtype = "uint64", shape = (13, 3, 12))#candidate|3698|(13, 3, 12)|var|uint64
call_3696 = func_3695_call(var_3697,var_3698,)
output = call_3696
func_3699 = relay.Function([var_3697,var_3698,], output)
mutated_mod['func_3699'] = func_3699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1726_call = mod.get_global_var('func_1726')
func_1728_call = mutated_mod.get_global_var('func_1728')
call_3726 = func_1726_call()
call_3727 = func_1726_call()
uop_3751 = relay.log10(call_3726.astype('float64')) # shape=(2, 9, 9)
uop_3753 = relay.log10(call_3727.astype('float64')) # shape=(2, 9, 9)
output = uop_3751
output2 = uop_3753
func_3758 = relay.Function([], output)
mod['func_3758'] = func_3758
mod = relay.transform.InferType()(mod)
mutated_mod['func_3758'] = func_3758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3758_call = mutated_mod.get_global_var('func_3758')
call_3759 = func_3758_call()
output = call_3759
func_3760 = relay.Function([], output)
mutated_mod['func_3760'] = func_3760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_398_call = mod.get_global_var('func_398')
func_400_call = mutated_mod.get_global_var('func_400')
call_3787 = relay.TupleGetItem(func_398_call(), 0)
call_3788 = relay.TupleGetItem(func_400_call(), 0)
output = relay.Tuple([call_3787,])
output2 = relay.Tuple([call_3788,])
func_3794 = relay.Function([], output)
mod['func_3794'] = func_3794
mod = relay.transform.InferType()(mod)
output = func_3794()
func_3795 = relay.Function([], output)
mutated_mod['func_3795'] = func_3795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1927_call = mod.get_global_var('func_1927')
func_1928_call = mutated_mod.get_global_var('func_1928')
call_3813 = func_1927_call()
call_3814 = func_1927_call()
output = relay.Tuple([call_3813,])
output2 = relay.Tuple([call_3814,])
func_3864 = relay.Function([], output)
mod['func_3864'] = func_3864
mod = relay.transform.InferType()(mod)
output = func_3864()
func_3865 = relay.Function([], output)
mutated_mod['func_3865'] = func_3865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3525_call = mod.get_global_var('func_3525')
func_3526_call = mutated_mod.get_global_var('func_3526')
call_3984 = func_3525_call()
call_3985 = func_3525_call()
func_856_call = mod.get_global_var('func_856')
func_858_call = mutated_mod.get_global_var('func_858')
const_3993 = relay.const([-0.231297,-8.992786,-0.097843,0.680059,-2.668458,3.251889,5.433502,-4.466914,6.345086,-1.352454,-1.639918,5.682441,-3.229217,-6.109479,-3.980994,4.133825,1.068377,-5.328515,9.723984,9.533005,7.961651,-5.711487,2.106794,8.399748,-7.805387,-2.709540,0.938291,4.533898,-7.305745,-4.053406,-6.916047,4.131931,7.205981,7.988568,-8.169539,-5.344420,3.219060,-8.473454,9.877210,3.311155,3.007303,7.005026,8.650131,-8.931349,-9.125792,-5.326076,7.761461,-9.721053,-1.465146,3.406761,-0.680455,-8.366476,-3.679274,-7.493232,-3.593280,-8.475636,-7.737291,4.210691,-6.221219,8.602534,-6.049524,8.760892,5.123257,-1.577507,2.088084,-5.405384,-2.684877,7.633550,8.066764,-9.154453,4.166155,-0.996046,-6.121233,8.134895,0.436527,6.462946,5.091166,3.474746,-7.056731,-7.556603,8.143364,-6.034610,2.160615,5.655907,7.346597,8.348857,-3.635603,-3.764506,4.760236,0.489005,-0.749572,-3.974955,-5.734065,8.141641,4.611980,-3.450912,-9.993180,-9.159762,9.859382,1.959106,-7.635684,7.484295,-2.247796,7.759648,-1.127011], dtype = "float64")#candidate|3993|(105,)|const|float64
call_3992 = relay.TupleGetItem(func_856_call(relay.reshape(const_3993.astype('float64'), [21, 5])), 1)
call_3994 = relay.TupleGetItem(func_858_call(relay.reshape(const_3993.astype('float64'), [21, 5])), 1)
output = relay.Tuple([call_3984,call_3992,const_3993,])
output2 = relay.Tuple([call_3985,call_3994,const_3993,])
func_4019 = relay.Function([], output)
mod['func_4019'] = func_4019
mod = relay.transform.InferType()(mod)
output = func_4019()
func_4020 = relay.Function([], output)
mutated_mod['func_4020'] = func_4020
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3564_call = mod.get_global_var('func_3564')
func_3566_call = mutated_mod.get_global_var('func_3566')
call_4021 = func_3564_call()
call_4022 = func_3564_call()
func_4019_call = mod.get_global_var('func_4019')
func_4020_call = mutated_mod.get_global_var('func_4020')
call_4026 = relay.TupleGetItem(func_4019_call(), 1)
call_4027 = relay.TupleGetItem(func_4020_call(), 1)
output = relay.Tuple([call_4021,call_4026,])
output2 = relay.Tuple([call_4022,call_4027,])
func_4053 = relay.Function([], output)
mod['func_4053'] = func_4053
mod = relay.transform.InferType()(mod)
output = func_4053()
func_4054 = relay.Function([], output)
mutated_mod['func_4054'] = func_4054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3498_call = mod.get_global_var('func_3498')
func_3500_call = mutated_mod.get_global_var('func_3500')
call_4117 = relay.TupleGetItem(func_3498_call(), 0)
call_4118 = relay.TupleGetItem(func_3500_call(), 0)
output = relay.Tuple([call_4117,])
output2 = relay.Tuple([call_4118,])
func_4127 = relay.Function([], output)
mod['func_4127'] = func_4127
mod = relay.transform.InferType()(mod)
output = func_4127()
func_4128 = relay.Function([], output)
mutated_mod['func_4128'] = func_4128
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4144 = relay.const([[[-3.495479,7.273752,7.687343,3.333971,9.860008,-1.570319,6.305652,2.721892,-2.526773],[7.872863,-7.699025,-0.019678,-2.054197,-7.273018,1.612278,0.448891,-0.187380,-2.750324],[9.718785,5.552392,3.429402,1.769357,-1.256539,2.160351,-5.586796,-2.261028,-6.755707],[-3.438916,6.650179,-6.353352,4.386093,-5.952468,9.277975,2.590129,-3.794106,6.773480],[-9.055705,-0.031252,3.354159,-4.468013,-3.257627,-1.446647,2.256292,-6.826920,-4.336922],[-5.383175,-5.252083,8.870292,2.812702,-4.505176,7.508920,5.849524,-4.246245,0.060985],[-8.195336,2.235353,-5.327776,9.491121,8.427403,-2.398901,7.172621,7.808627,5.083605],[5.957642,9.725113,3.455687,1.487849,-5.595274,-2.502871,9.564266,5.077749,-9.186253],[5.861645,-8.744601,8.356200,-7.993741,8.009988,-2.614033,-5.545055,4.550097,9.582969],[4.313614,1.458083,1.123659,6.032319,-7.188101,1.386216,-6.214020,5.879565,7.660982],[7.892266,8.059395,3.353745,1.147579,6.954532,5.348391,2.506450,7.375069,3.385713],[4.229102,1.243372,4.351301,-9.017409,5.913382,-6.877465,-3.624077,-5.909547,-8.387011],[5.487641,-6.444899,-4.486525,6.888041,-6.507820,8.797903,7.444608,-0.887422,-9.021911],[-9.274240,4.616048,-8.765844,-1.577232,1.175782,-2.493678,8.681295,1.137317,-1.893124],[6.068188,-2.446723,-8.661511,2.962286,-6.445122,1.675768,-8.905369,0.847694,8.500902],[3.577278,-0.299337,8.487694,1.921050,-7.919627,-2.186758,-0.259179,-2.177804,7.152312]]], dtype = "float32")#candidate|4144|(1, 16, 9)|const|float32
uop_4145 = relay.cos(const_4144.astype('float32')) # shape=(1, 16, 9)
func_1904_call = mod.get_global_var('func_1904')
func_1906_call = mutated_mod.get_global_var('func_1906')
call_4149 = relay.TupleGetItem(func_1904_call(), 1)
call_4150 = relay.TupleGetItem(func_1906_call(), 1)
func_4019_call = mod.get_global_var('func_4019')
func_4020_call = mutated_mod.get_global_var('func_4020')
call_4152 = relay.TupleGetItem(func_4019_call(), 1)
call_4153 = relay.TupleGetItem(func_4020_call(), 1)
func_3525_call = mod.get_global_var('func_3525')
func_3526_call = mutated_mod.get_global_var('func_3526')
call_4157 = func_3525_call()
call_4158 = func_3525_call()
output = relay.Tuple([uop_4145,call_4149,call_4152,call_4157,])
output2 = relay.Tuple([uop_4145,call_4150,call_4153,call_4158,])
func_4168 = relay.Function([], output)
mod['func_4168'] = func_4168
mod = relay.transform.InferType()(mod)
output = func_4168()
func_4169 = relay.Function([], output)
mutated_mod['func_4169'] = func_4169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_438_call = mod.get_global_var('func_438')
func_439_call = mutated_mod.get_global_var('func_439')
call_4186 = func_438_call()
call_4187 = func_438_call()
uop_4190 = relay.sigmoid(call_4186.astype('float32')) # shape=(2, 9, 9)
uop_4192 = relay.sigmoid(call_4187.astype('float32')) # shape=(2, 9, 9)
func_2477_call = mod.get_global_var('func_2477')
func_2479_call = mutated_mod.get_global_var('func_2479')
call_4193 = relay.TupleGetItem(func_2477_call(), 0)
call_4194 = relay.TupleGetItem(func_2479_call(), 0)
output = relay.Tuple([uop_4190,call_4193,])
output2 = relay.Tuple([uop_4192,call_4194,])
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
func_4127_call = mod.get_global_var('func_4127')
func_4128_call = mutated_mod.get_global_var('func_4128')
call_4258 = relay.TupleGetItem(func_4127_call(), 0)
call_4259 = relay.TupleGetItem(func_4128_call(), 0)
output = relay.Tuple([call_4258,])
output2 = relay.Tuple([call_4259,])
func_4289 = relay.Function([], output)
mod['func_4289'] = func_4289
mod = relay.transform.InferType()(mod)
output = func_4289()
func_4290 = relay.Function([], output)
mutated_mod['func_4290'] = func_4290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3525_call = mod.get_global_var('func_3525')
func_3526_call = mutated_mod.get_global_var('func_3526')
call_4331 = func_3525_call()
call_4332 = func_3525_call()
func_413_call = mod.get_global_var('func_413')
func_415_call = mutated_mod.get_global_var('func_415')
call_4348 = relay.TupleGetItem(func_413_call(), 0)
call_4349 = relay.TupleGetItem(func_415_call(), 0)
uop_4361 = relay.log(call_4348.astype('float32')) # shape=(2, 9, 9)
uop_4363 = relay.log(call_4349.astype('float32')) # shape=(2, 9, 9)
func_2618_call = mod.get_global_var('func_2618')
func_2620_call = mutated_mod.get_global_var('func_2620')
var_4365 = relay.var("var_4365", dtype = "bool", shape = (686,))#candidate|4365|(686,)|var|bool
call_4364 = relay.TupleGetItem(func_2618_call(relay.reshape(var_4365.astype('bool'), [14, 7, 7])), 1)
call_4366 = relay.TupleGetItem(func_2620_call(relay.reshape(var_4365.astype('bool'), [14, 7, 7])), 1)
func_4219_call = mod.get_global_var('func_4219')
func_4221_call = mutated_mod.get_global_var('func_4221')
call_4381 = relay.TupleGetItem(func_4219_call(), 0)
call_4382 = relay.TupleGetItem(func_4221_call(), 0)
output = relay.Tuple([call_4331,uop_4361,call_4364,var_4365,call_4381,])
output2 = relay.Tuple([call_4332,uop_4363,call_4366,var_4365,call_4382,])
func_4397 = relay.Function([var_4365,], output)
mod['func_4397'] = func_4397
mod = relay.transform.InferType()(mod)
var_4398 = relay.var("var_4398", dtype = "bool", shape = (686,))#candidate|4398|(686,)|var|bool
output = func_4397(var_4398)
func_4399 = relay.Function([var_4398], output)
mutated_mod['func_4399'] = func_4399
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3864_call = mod.get_global_var('func_3864')
func_3865_call = mutated_mod.get_global_var('func_3865')
call_4449 = relay.TupleGetItem(func_3864_call(), 0)
call_4450 = relay.TupleGetItem(func_3865_call(), 0)
output = call_4449
output2 = call_4450
func_4456 = relay.Function([], output)
mod['func_4456'] = func_4456
mod = relay.transform.InferType()(mod)
output = func_4456()
func_4457 = relay.Function([], output)
mutated_mod['func_4457'] = func_4457
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4460 = relay.var("var_4460", dtype = "int8", shape = (7, 12, 10))#candidate|4460|(7, 12, 10)|var|int8
var_4461 = relay.var("var_4461", dtype = "int8", shape = (7, 12, 10))#candidate|4461|(7, 12, 10)|var|int8
bop_4462 = relay.bitwise_and(var_4460.astype('int8'), relay.reshape(var_4461.astype('int8'), relay.shape_of(var_4460))) # shape=(7, 12, 10)
uop_4466 = relay.rsqrt(var_4461.astype('float32')) # shape=(7, 12, 10)
output = relay.Tuple([bop_4462,uop_4466,])
output2 = relay.Tuple([bop_4462,uop_4466,])
func_4490 = relay.Function([var_4460,var_4461,], output)
mod['func_4490'] = func_4490
mod = relay.transform.InferType()(mod)
mutated_mod['func_4490'] = func_4490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4490_call = mutated_mod.get_global_var('func_4490')
var_4492 = relay.var("var_4492", dtype = "int8", shape = (7, 12, 10))#candidate|4492|(7, 12, 10)|var|int8
var_4493 = relay.var("var_4493", dtype = "int8", shape = (7, 12, 10))#candidate|4493|(7, 12, 10)|var|int8
call_4491 = func_4490_call(var_4492,var_4493,)
output = call_4491
func_4494 = relay.Function([var_4492,var_4493,], output)
mutated_mod['func_4494'] = func_4494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1397_call = mod.get_global_var('func_1397')
func_1398_call = mutated_mod.get_global_var('func_1398')
call_4502 = relay.TupleGetItem(func_1397_call(), 0)
call_4503 = relay.TupleGetItem(func_1398_call(), 0)
func_4127_call = mod.get_global_var('func_4127')
func_4128_call = mutated_mod.get_global_var('func_4128')
call_4535 = relay.TupleGetItem(func_4127_call(), 0)
call_4536 = relay.TupleGetItem(func_4128_call(), 0)
func_1927_call = mod.get_global_var('func_1927')
func_1928_call = mutated_mod.get_global_var('func_1928')
call_4551 = func_1927_call()
call_4552 = func_1927_call()
func_1237_call = mod.get_global_var('func_1237')
func_1241_call = mutated_mod.get_global_var('func_1241')
const_4561 = relay.const([-4,-7,-10,-9,-4,9,-4,10,8,4,6,7,-1,7,3,-1,-8,-1,7,5,7,-1,-3,-2,-4,8,-10,-9,10,-3,2,1,4,8,3,5,9,1,-6,7,-1,-1,2,4,-4,8,-10,-7,4,-6,-9,9,6,4,-4,3,5,-8,3,-2], dtype = "uint16")#candidate|4561|(60,)|const|uint16
call_4560 = relay.TupleGetItem(func_1237_call(relay.reshape(const_4561.astype('uint16'), [5, 3, 4]), relay.reshape(const_4561.astype('uint16'), [5, 3, 4]), ), 1)
call_4562 = relay.TupleGetItem(func_1241_call(relay.reshape(const_4561.astype('uint16'), [5, 3, 4]), relay.reshape(const_4561.astype('uint16'), [5, 3, 4]), ), 1)
uop_4563 = relay.acosh(call_4560.astype('float32')) # shape=(7, 3, 5)
uop_4565 = relay.acosh(call_4562.astype('float32')) # shape=(7, 3, 5)
output = relay.Tuple([call_4502,call_4535,call_4551,const_4561,uop_4563,])
output2 = relay.Tuple([call_4503,call_4536,call_4552,const_4561,uop_4565,])
func_4566 = relay.Function([], output)
mod['func_4566'] = func_4566
mod = relay.transform.InferType()(mod)
mutated_mod['func_4566'] = func_4566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4566_call = mutated_mod.get_global_var('func_4566')
call_4567 = func_4566_call()
output = call_4567
func_4568 = relay.Function([], output)
mutated_mod['func_4568'] = func_4568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4219_call = mod.get_global_var('func_4219')
func_4221_call = mutated_mod.get_global_var('func_4221')
call_4582 = relay.TupleGetItem(func_4219_call(), 1)
call_4583 = relay.TupleGetItem(func_4221_call(), 1)
uop_4595 = relay.asin(call_4582.astype('float32')) # shape=(7, 7, 2)
uop_4597 = relay.asin(call_4583.astype('float32')) # shape=(7, 7, 2)
func_2280_call = mod.get_global_var('func_2280')
func_2283_call = mutated_mod.get_global_var('func_2283')
call_4599 = relay.TupleGetItem(func_2280_call(relay.reshape(uop_4595.astype('float32'), [98, 1])), 4)
call_4600 = relay.TupleGetItem(func_2283_call(relay.reshape(uop_4595.astype('float32'), [98, 1])), 4)
output = relay.Tuple([uop_4595,call_4599,])
output2 = relay.Tuple([uop_4597,call_4600,])
func_4618 = relay.Function([], output)
mod['func_4618'] = func_4618
mod = relay.transform.InferType()(mod)
output = func_4618()
func_4619 = relay.Function([], output)
mutated_mod['func_4619'] = func_4619
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3794_call = mod.get_global_var('func_3794')
func_3795_call = mutated_mod.get_global_var('func_3795')
call_4674 = relay.TupleGetItem(func_3794_call(), 0)
call_4675 = relay.TupleGetItem(func_3795_call(), 0)
const_4683 = relay.const([[[8.041110,1.241534,-9.222155,-4.420466,1.947133,1.958773,-2.018235,-4.967539,-2.303388],[-0.933808,1.489196,5.483978,-7.919487,2.400362,1.827469,-8.858840,-0.446241,6.622182],[8.934369,5.634584,1.948091,-9.717692,-0.219718,-8.926283,2.633690,8.010708,-3.130349],[-2.677938,-2.625478,-7.177030,2.961550,8.518736,-7.804835,-7.919000,-3.804231,-6.245950],[-4.275655,5.327266,1.350006,4.068352,0.047383,-5.964588,7.277556,-3.089814,-0.696005],[-5.412834,3.507459,1.009090,-2.961614,6.274491,1.798796,-3.873599,-6.737845,3.087993],[8.166259,-9.619561,3.224962,6.651533,-2.864233,6.913112,-4.052164,-1.713779,2.486344],[3.648834,9.181675,-4.475144,8.443902,-4.878147,-0.892216,2.306225,-8.409567,-3.132950],[-4.256456,1.159282,3.043887,1.448640,-4.460671,8.900824,-8.391595,2.603949,7.680565]],[[-9.950878,-1.434244,-3.868290,-3.851301,-4.882447,-6.095119,5.841618,-8.088298,8.010256],[9.972119,8.762587,-3.675162,4.759580,-9.879096,-1.923017,-3.333524,-4.135717,4.126113],[4.469242,-2.916871,-1.503308,4.542546,-1.943661,-8.343517,1.777768,-3.999728,4.419083],[-5.588998,4.853795,9.459911,-6.246156,9.618447,-1.697537,-0.593681,-7.566303,-8.772735],[3.074566,-9.610142,7.915119,2.279783,-5.165509,-8.923614,-8.734196,-2.862463,1.006175],[0.989253,7.053386,-4.064940,4.550462,-9.261623,7.537819,-1.107564,-3.927111,-1.067475],[-9.009776,-3.775265,-6.356475,-9.701275,1.175135,-2.500686,0.828251,2.035879,-6.866297],[-6.933083,-0.599656,-4.503119,9.633047,-6.786052,0.373655,-7.225796,-2.393798,0.482387],[0.101205,1.579331,-0.410333,1.094103,7.763366,2.586641,-3.210593,0.770543,-4.938574]]], dtype = "float64")#candidate|4683|(2, 9, 9)|const|float64
bop_4684 = relay.not_equal(call_4674.astype('bool'), relay.reshape(const_4683.astype('bool'), relay.shape_of(call_4674))) # shape=(2, 9, 9)
bop_4687 = relay.not_equal(call_4675.astype('bool'), relay.reshape(const_4683.astype('bool'), relay.shape_of(call_4675))) # shape=(2, 9, 9)
func_1726_call = mod.get_global_var('func_1726')
func_1728_call = mutated_mod.get_global_var('func_1728')
call_4699 = func_1726_call()
call_4700 = func_1726_call()
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_4702 = relay.TupleGetItem(func_261_call(), 0)
call_4703 = relay.TupleGetItem(func_263_call(), 0)
func_3625_call = mod.get_global_var('func_3625')
func_3627_call = mutated_mod.get_global_var('func_3627')
var_4716 = relay.var("var_4716", dtype = "float64", shape = (336, 2))#candidate|4716|(336, 2)|var|float64
call_4715 = relay.TupleGetItem(func_3625_call(relay.reshape(var_4716.astype('float64'), [6, 7, 16])), 0)
call_4717 = relay.TupleGetItem(func_3627_call(relay.reshape(var_4716.astype('float64'), [6, 7, 16])), 0)
output = relay.Tuple([bop_4684,call_4699,call_4702,call_4715,var_4716,])
output2 = relay.Tuple([bop_4687,call_4700,call_4703,call_4717,var_4716,])
func_4736 = relay.Function([var_4716,], output)
mod['func_4736'] = func_4736
mod = relay.transform.InferType()(mod)
mutated_mod['func_4736'] = func_4736
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4737 = relay.var("var_4737", dtype = "float64", shape = (336, 2))#candidate|4737|(336, 2)|var|float64
func_4736_call = mutated_mod.get_global_var('func_4736')
call_4738 = func_4736_call(var_4737)
output = call_4738
func_4739 = relay.Function([var_4737], output)
mutated_mod['func_4739'] = func_4739
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3547_call = mod.get_global_var('func_3547')
func_3549_call = mutated_mod.get_global_var('func_3549')
call_4755 = relay.TupleGetItem(func_3547_call(), 2)
call_4756 = relay.TupleGetItem(func_3549_call(), 2)
func_4397_call = mod.get_global_var('func_4397')
func_4399_call = mutated_mod.get_global_var('func_4399')
const_4759 = relay.const([True,False,False,False,False,True,False,False,False,False,False,True,False,True,True,True,False,False,False,True,True,True,True,True,True,False,True,True,True,True,False,False,True,False,False,False,True,False,False,True,True,False,False,True,True,True,False,True,False,False,False,True,True,False,False,False,False,True,True,True,False,True,True,False,True,False,False,True,False,False,False,True,False,True,False,True,False,False,True,False,False,True,True,True,True,False,True,True,True,True,False,False,False,False,False,False,False,False,True,False,False,True,False,False,False,False,True,True,True,False,True,True,False,True,True,True,True,False,True,False,True,True,False,False,True,False,False,True,False,True,False,False,False,False,False,True,False,False,False,True,False,True,True,False,False,False,False,True,False,True,False,False,False,False,False,False,True,False,True,True,True,True,False,True,True,False,False,False,False,False,True,True,False,False,True,False,False,True,False,True,False,False,True,True,False,True,True,True,True,False,True,False,False,True,True,True,True,False,True,False,False,True,True,False,True,False,True,False,False,True,True,False,True,False,True,True,True,False,True,False,True,False,False,True,True,True,False,False,True,False,False,False,True,True,False,False,False,True,False,False,False,True,False,True,True,False,True,False,False,False,False,True,False,False,False,True,False,True,True,True,True,False,True,False,True,False,False,True,True,True,True,False,False,False,True,False,False,False,False,False,False,True,False,False,True,False,True,True,True,True,True,False,True,False,False,False,False,True,False,False,False,True,False,False,True,True,False,True,False,True,False,False,False,False,True,True,False,False,True,False,True,False,False,False,False,True,True,True,False,True,True,False,False,True,False,False,False,True,True,False,False,True,True,False,True,False,True,False,False,False,False,False,False,False,False,True,True,True,False,True,False,True,True,True,False,False,True,False,True,False,True,True,False,False,True,True,False,False,True,False,True,True,False,True,False,True,False,True,False,False,True,True,True,False,False,True,False,True,False,True,True,True,False,True,True,True,True,True,False,False,True,True,False,False,False,False,True,True,True,True,True,False,False,True,True,False,False,True,True,False,True,True,True,True,False,False,True,True,True,True,False,True,False,False,True,False,False,False,True,True,True,True,False,False,False,True,False,False,False,False,True,True,True,False,True,True,True,False,True,False,True,True,True,True,True,False,True,True,False,True,False,False,False,False,False,False,True,False,False,False,False,True,True,True,False,False,True,True,False,False,True,True,True,True,False,False,True,False,True,False,True,True,False,True,False,False,True,True,False,True,True,True,True,True,False,True,True,True,False,False,True,True,True,False,False,False,False,False,False,True,False,True,True,False,False,True,False,True,False,False,False,False,True,True,True,False,False,False,True,False,False,True,False,False,True,False,False,False,False,False,True,False,True,False,False,True,True,False,False,False,True,False,False,False,False,True,False,False,True,False,True,False,True,True,False,False,True,False,False,False,False,False,False,True,False,True,False,False,True,False,False,False,False,False,True,False,True,True,True,False,True,False,False,False,True,False,True,False,False,True,False,False,True,True,True,False,False,True,False,True,True,False,False,False,False,True,False,True,False,True,True,False,True,False,False,False,False,True,True,True,True,True,True,False,False,True,False,False,False,False,False,False,False,False,False,False,True,False,True,True,False,True,True,True,True,False], dtype = "bool")#candidate|4759|(686,)|const|bool
call_4758 = relay.TupleGetItem(func_4397_call(relay.reshape(const_4759.astype('bool'), [686,])), 2)
call_4760 = relay.TupleGetItem(func_4399_call(relay.reshape(const_4759.astype('bool'), [686,])), 2)
func_2181_call = mod.get_global_var('func_2181')
func_2183_call = mutated_mod.get_global_var('func_2183')
call_4781 = func_2181_call()
call_4782 = func_2181_call()
output = relay.Tuple([call_4755,call_4758,const_4759,call_4781,])
output2 = relay.Tuple([call_4756,call_4760,const_4759,call_4782,])
func_4785 = relay.Function([], output)
mod['func_4785'] = func_4785
mod = relay.transform.InferType()(mod)
output = func_4785()
func_4786 = relay.Function([], output)
mutated_mod['func_4786'] = func_4786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1366_call = mod.get_global_var('func_1366')
func_1367_call = mutated_mod.get_global_var('func_1367')
call_4811 = relay.TupleGetItem(func_1366_call(), 1)
call_4812 = relay.TupleGetItem(func_1367_call(), 1)
output = call_4811
output2 = call_4812
func_4822 = relay.Function([], output)
mod['func_4822'] = func_4822
mod = relay.transform.InferType()(mod)
output = func_4822()
func_4823 = relay.Function([], output)
mutated_mod['func_4823'] = func_4823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1494_call = mod.get_global_var('func_1494')
func_1495_call = mutated_mod.get_global_var('func_1495')
call_4827 = func_1494_call()
call_4828 = func_1494_call()
output = call_4827
output2 = call_4828
func_4840 = relay.Function([], output)
mod['func_4840'] = func_4840
mod = relay.transform.InferType()(mod)
output = func_4840()
func_4841 = relay.Function([], output)
mutated_mod['func_4841'] = func_4841
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3188_call = mod.get_global_var('func_3188')
func_3189_call = mutated_mod.get_global_var('func_3189')
call_4861 = relay.TupleGetItem(func_3188_call(), 0)
call_4862 = relay.TupleGetItem(func_3189_call(), 0)
output = relay.Tuple([call_4861,])
output2 = relay.Tuple([call_4862,])
func_4882 = relay.Function([], output)
mod['func_4882'] = func_4882
mod = relay.transform.InferType()(mod)
output = func_4882()
func_4883 = relay.Function([], output)
mutated_mod['func_4883'] = func_4883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4219_call = mod.get_global_var('func_4219')
func_4221_call = mutated_mod.get_global_var('func_4221')
call_4884 = relay.TupleGetItem(func_4219_call(), 1)
call_4885 = relay.TupleGetItem(func_4221_call(), 1)
output = call_4884
output2 = call_4885
func_4907 = relay.Function([], output)
mod['func_4907'] = func_4907
mod = relay.transform.InferType()(mod)
output = func_4907()
func_4908 = relay.Function([], output)
mutated_mod['func_4908'] = func_4908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4822_call = mod.get_global_var('func_4822')
func_4823_call = mutated_mod.get_global_var('func_4823')
call_4923 = func_4822_call()
call_4924 = func_4822_call()
var_4925 = relay.var("var_4925", dtype = "float32", shape = (2, 9, 9))#candidate|4925|(2, 9, 9)|var|float32
bop_4926 = relay.add(call_4923.astype('uint16'), relay.reshape(var_4925.astype('uint16'), relay.shape_of(call_4923))) # shape=(2, 9, 9)
bop_4929 = relay.add(call_4924.astype('uint16'), relay.reshape(var_4925.astype('uint16'), relay.shape_of(call_4924))) # shape=(2, 9, 9)
func_667_call = mod.get_global_var('func_667')
func_671_call = mutated_mod.get_global_var('func_671')
call_4931 = relay.TupleGetItem(func_667_call(relay.reshape(call_4923.astype('float64'), [2, 9, 9]), relay.reshape(bop_4926.astype('float64'), [2, 9, 9]), ), 2)
call_4932 = relay.TupleGetItem(func_671_call(relay.reshape(call_4923.astype('float64'), [2, 9, 9]), relay.reshape(bop_4926.astype('float64'), [2, 9, 9]), ), 2)
output = relay.Tuple([bop_4926,call_4931,])
output2 = relay.Tuple([bop_4929,call_4932,])
func_4949 = relay.Function([var_4925,], output)
mod['func_4949'] = func_4949
mod = relay.transform.InferType()(mod)
var_4950 = relay.var("var_4950", dtype = "float32", shape = (2, 9, 9))#candidate|4950|(2, 9, 9)|var|float32
output = func_4949(var_4950)
func_4951 = relay.Function([var_4950], output)
mutated_mod['func_4951'] = func_4951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3188_call = mod.get_global_var('func_3188')
func_3189_call = mutated_mod.get_global_var('func_3189')
call_4968 = relay.TupleGetItem(func_3188_call(), 1)
call_4969 = relay.TupleGetItem(func_3189_call(), 1)
func_1024_call = mod.get_global_var('func_1024')
func_1028_call = mutated_mod.get_global_var('func_1028')
const_5023 = relay.const([[-5,1,-7,9,-3,4,7,9,-4,9,-6,-10,-2,-2],[2,-3,4,-5,2,-10,-8,5,4,1,6,5,-8,4],[3,9,5,-4,-5,-10,3,-1,6,10,-1,-9,2,-8],[3,2,-5,3,2,-1,-6,-5,-10,-4,6,8,7,-2],[-1,1,2,10,-4,-9,10,-7,-2,-7,-3,-1,-5,4],[-4,10,9,-1,-5,-10,4,7,-1,2,9,8,-8,-8],[-7,2,-9,1,6,-10,-3,-3,-10,-2,-7,6,4,5],[-2,5,-5,3,1,-3,5,1,-2,6,-5,4,-5,-7],[2,-10,-4,6,-2,-3,-2,-4,-10,3,-9,5,-9,7],[9,2,-3,8,5,-7,2,2,6,8,-10,7,4,-5],[-3,7,-4,3,-1,-7,4,3,-1,9,10,-3,-2,10],[-4,-9,9,7,4,3,1,-2,-3,3,2,3,-3,2],[7,-9,9,8,-5,3,6,-7,-5,2,-5,-6,-8,9],[-5,7,5,5,-6,-3,-9,-10,-2,10,5,-7,-10,7],[2,-1,7,1,4,7,10,-2,-6,-1,-1,-8,-6,9],[8,4,-2,-8,-3,-2,-6,8,10,-2,4,5,-6,-4],[-7,-6,8,8,-7,10,7,8,2,-7,7,1,3,-7],[-8,-9,3,-2,7,3,-8,3,-7,-7,8,3,3,7],[9,-5,6,-4,1,-9,7,2,7,9,8,-4,7,-2],[-3,-6,-4,1,-5,8,-10,4,-3,3,4,5,-7,10],[8,4,-2,6,-3,7,-10,4,4,-9,4,6,-3,4],[9,4,8,1,-10,6,-1,-1,-8,3,1,-10,4,-7],[-8,-7,-6,8,-8,-4,5,-2,-2,1,8,-3,-8,5],[2,8,-6,-9,-5,6,6,-2,9,9,-6,3,-4,2],[9,5,3,1,10,2,9,-7,-10,-5,-4,2,5,-6],[10,-3,9,-2,1,2,7,5,3,-10,4,4,10,-9],[-9,-5,5,2,6,-6,1,-6,-1,-4,-4,7,-10,5],[-7,6,-9,7,-9,-8,4,9,2,-4,8,-7,-2,2],[7,1,-4,-8,-8,-9,-5,-9,10,6,5,5,10,8],[8,4,-9,-9,-2,6,-3,6,-1,-9,-2,5,5,-3],[-3,8,10,9,9,-2,5,10,4,-6,-10,8,-9,1],[4,-10,-4,-10,-10,-6,7,9,-8,9,-6,7,-1,-2],[-9,-4,-7,-9,5,-7,-6,-4,-1,-4,6,8,-8,10],[1,10,4,-10,2,-4,-7,-2,4,-8,2,3,-7,10],[8,-5,-3,-9,-2,-10,8,-9,-4,2,6,-2,-3,-6],[8,6,-7,4,-9,-9,-2,3,-2,5,-3,2,6,-10],[1,-9,-2,-4,7,3,1,-5,10,4,-10,5,-5,-5],[-3,2,-10,10,10,-3,1,3,7,-8,-9,6,-9,-5],[8,-9,-4,4,6,6,-9,2,-6,-4,4,7,-2,5],[3,-10,-7,-3,-10,6,2,-1,-2,1,-8,8,-8,-7],[7,-4,9,1,-2,10,-1,9,8,-6,-1,-6,-3,4],[9,-2,3,-5,1,-2,-10,7,7,-7,-6,-5,10,-7],[-4,-6,2,9,5,10,10,1,4,-1,3,-8,-3,-7],[2,7,7,-1,1,-6,4,4,-10,1,-2,9,-4,-8],[9,1,-1,1,10,-9,-2,9,3,-9,8,-10,-6,-10],[5,-7,-3,-8,-5,-10,-1,-9,-4,-10,-2,1,-8,-2],[10,-5,10,-9,-10,-7,6,-3,-6,1,-1,-8,-7,-4],[-2,1,10,6,8,5,2,5,9,2,-10,-7,3,5],[8,7,8,1,4,10,-3,-1,6,1,-4,3,6,-7],[7,9,3,-5,-3,-9,-4,-8,3,-9,5,-6,-3,-5],[1,7,7,-3,-1,-9,3,-1,8,-3,9,2,10,-3],[9,1,3,5,-6,-8,7,3,-9,8,-4,-8,10,6],[-10,-4,-8,-6,-5,-1,-1,1,-10,1,-1,-5,-9,7],[-5,-3,4,1,-2,-5,9,-9,-6,-2,7,6,-2,2],[-7,3,3,-6,-3,1,5,-4,9,-9,-6,-3,-2,-10],[3,-6,-4,-10,-6,6,-3,-5,-10,-5,2,7,-2,-2],[1,-1,-5,-5,-7,-8,3,-2,-10,7,6,10,-7,-8],[7,-5,4,-5,2,-8,4,4,9,-4,-3,-8,4,-8],[4,9,-8,2,-10,-10,6,5,-5,7,-3,2,3,-4],[9,7,-8,7,-1,-7,-7,-7,-7,4,9,8,4,7],[-2,-6,3,-6,-8,-8,-3,1,-3,2,-9,4,8,10],[-1,-3,10,-6,1,-5,-5,9,7,8,10,-2,6,7],[-7,10,-7,-3,-10,-9,10,-1,6,-5,-4,5,-4,-1],[4,-8,8,-8,-1,-10,-9,6,-3,-6,-9,-4,-5,6],[-7,-2,6,1,-8,-9,-8,-3,-7,6,-8,-1,-5,-1],[-5,10,4,4,-3,-4,-1,-1,-1,8,5,-10,-8,9],[7,6,5,-7,-9,8,5,3,4,-7,-10,3,-10,-6],[3,4,3,3,7,6,-10,-5,6,-10,-4,3,5,7],[8,-8,9,2,-3,2,4,3,4,-8,-8,9,9,-5],[-10,2,6,-9,-1,8,6,3,10,4,5,-4,-2,6],[9,-6,2,4,-7,4,4,3,4,9,-1,9,5,-1],[-10,-8,8,7,1,9,-6,7,7,-9,-5,4,-9,4],[-8,-1,-3,7,-3,1,-6,4,-5,10,-1,2,7,-4],[9,-10,-2,-7,-8,-6,7,-4,2,-2,1,9,-3,9],[-7,6,-10,4,5,-7,-6,-5,2,5,-9,1,3,1],[-2,-5,5,6,-8,-7,2,8,-1,-10,-2,9,3,1],[-1,-1,-7,2,8,7,-6,8,2,-7,-9,-6,-3,-6],[4,-4,2,-7,-4,10,5,-7,-2,3,3,7,-9,6],[-7,-10,-2,5,10,4,3,5,1,-10,-8,-7,5,6],[-6,-5,7,-5,10,4,3,1,9,-3,9,-3,8,-10],[7,-6,2,-7,9,-9,-1,-6,-8,10,4,-8,-9,-9],[-5,2,9,-5,3,10,-4,-8,10,1,4,5,-9,10],[6,-6,2,-4,-10,-2,3,-3,-10,3,-9,-10,-8,-1],[-8,4,4,-8,2,7,-1,2,-10,-2,-8,-10,9,-9],[5,-5,-3,-10,1,-3,-9,4,9,5,-3,-10,2,-7],[2,-10,-8,-1,-4,-9,-10,-1,-5,1,10,-3,-3,-3],[5,-5,-8,3,10,10,-6,2,-3,2,-5,-2,-9,10],[-10,-6,-5,-1,6,2,7,-9,-10,6,3,3,-3,4],[2,3,-7,6,-7,-8,10,-6,-1,-9,-7,4,4,-7],[4,6,-5,9,-7,-5,-1,-7,2,-7,2,4,10,-9],[-7,1,6,-9,-8,3,3,-10,-3,-5,-10,-10,10,-2],[-3,-5,5,-4,-5,4,-1,-7,-8,-9,1,6,10,-6],[9,1,8,4,3,-6,3,10,-8,-8,-3,7,-5,-9],[-2,-3,2,-5,-1,-4,9,5,-2,5,3,8,2,-1],[-2,-10,-5,5,9,6,9,8,-1,-1,7,3,-9,5],[-6,-10,7,3,5,9,-8,-7,8,6,-6,10,-2,3],[-4,5,-7,10,-7,7,-9,-7,5,5,-7,1,-7,-7],[6,2,-8,-1,4,-10,4,-2,-4,-1,10,2,-4,-1],[8,2,7,3,3,-2,-5,7,-10,2,5,-4,-9,2],[-3,-6,2,4,-2,-7,-1,1,1,-5,6,-4,-3,9],[7,7,6,-1,-3,-8,-4,-9,5,-2,9,-7,9,9],[-4,-5,-10,2,-8,-4,10,6,-8,8,7,10,-7,3],[2,9,-8,8,-7,-4,3,-5,-10,6,8,-1,-4,-2],[-2,9,7,-2,10,-5,-8,3,-6,6,-1,-6,-6,5],[10,1,2,-7,-7,6,-9,-6,1,-10,-10,-7,-7,-10],[-1,-3,2,-4,3,5,-2,-7,3,8,3,-3,2,-3],[-10,-4,-10,4,10,-10,9,2,6,2,5,3,6,2],[-3,-1,-10,6,9,-5,7,-1,-1,-10,6,-8,2,10],[9,-9,9,-9,-2,-2,-6,1,2,-2,7,-4,5,-6],[5,-6,8,-9,5,7,-3,-10,5,2,3,2,7,-5],[-8,-1,4,7,5,10,-4,-5,5,-5,7,8,3,-2],[-8,5,5,-8,3,5,-3,-6,-4,-3,-8,-9,-6,-7],[-9,-9,5,2,8,-10,-7,-1,-2,7,-1,2,7,-6],[-10,-1,-1,3,-2,5,5,3,2,2,10,-7,10,-10],[-3,-9,9,-10,-10,-6,10,-2,-9,-8,-8,3,2,9],[-1,8,-7,-5,-8,-9,-1,-9,-8,-9,6,8,-10,4],[-10,3,-5,-5,9,-1,6,3,6,-8,3,-3,-5,-4],[1,8,-2,5,1,10,-10,6,2,3,1,6,9,6],[-2,2,10,-7,10,-2,1,-2,4,7,7,-5,1,4],[-3,-7,-1,-8,-6,5,-6,6,8,10,-6,-7,-5,3],[6,-8,-8,-1,2,1,-4,-6,1,10,2,9,-7,10],[9,-9,-1,-3,4,9,3,5,-4,2,3,-5,1,2],[2,-1,-7,5,7,-10,-2,-8,9,-6,4,-10,-9,-3],[-9,-10,9,4,-10,-6,9,-10,5,7,1,6,-1,-4],[1,3,-4,-3,-2,9,-7,3,-2,-6,2,2,-9,1],[-5,2,-4,-10,-8,1,1,6,-6,-2,1,-5,3,6],[-6,-2,4,10,1,-6,4,-10,7,1,-4,-2,-10,8],[4,5,-3,-4,-3,2,-4,-2,6,-3,8,4,6,-7],[-3,-2,-10,-1,-6,-7,9,2,2,2,-5,-10,-9,-7],[10,-3,-10,4,-4,3,7,-8,3,-10,3,2,-6,-3],[7,-10,-3,-2,10,4,-8,-5,-9,1,-2,-7,-2,-4],[-1,5,-8,-7,-10,5,4,5,6,-8,2,9,2,-2],[8,5,5,-7,5,-6,-2,6,-2,-9,10,5,1,-7],[-3,7,4,-1,4,-4,4,5,-2,-4,-9,-5,4,-2],[-6,-6,-9,-10,-9,-6,9,-3,1,-8,6,-7,7,-7],[-2,4,9,8,-6,-2,1,7,7,4,-7,-1,6,-9],[2,6,4,-3,-1,-2,-1,-2,-4,2,-1,1,1,-3],[10,10,10,5,5,9,-10,4,9,6,7,7,6,-7],[10,2,4,3,7,7,7,-9,-9,10,9,1,4,5],[6,5,-4,7,10,-1,7,8,-4,-2,-9,10,8,5],[9,-2,-4,2,-3,-7,8,-9,-5,-10,-7,3,7,-6],[-7,9,-5,-3,-7,8,-4,4,-2,-7,-3,8,-3,5],[-6,-7,6,-9,4,-9,-6,2,1,-10,-8,-9,-7,-10],[-10,2,-8,9,4,2,-1,-8,9,7,-5,-4,-5,3],[-10,4,-8,7,7,9,-5,9,3,3,9,-3,-6,-7],[-9,-4,-5,-10,9,8,-3,-7,-7,4,-6,-1,4,9],[-10,10,-9,10,-7,5,-6,-1,-10,-7,7,-7,8,-7],[-4,2,-3,5,1,5,4,3,5,-10,4,-1,1,-3],[-8,1,7,7,-8,-3,6,6,-8,-3,-6,-7,2,-1],[-6,6,-7,5,2,5,4,8,7,-1,4,-9,7,-1],[4,6,8,-5,8,-10,-1,10,-4,5,-2,-8,10,-5],[3,-8,7,10,-5,-2,-4,3,7,3,2,7,-6,-10],[-2,5,-2,6,-8,-7,-1,8,-1,-3,6,4,-3,2],[3,8,-1,-3,-8,4,-5,-1,-2,-2,-1,3,-10,-5],[-7,-4,3,8,-3,-8,-1,-6,-5,-5,-7,-2,-3,-8],[-4,-5,2,-3,-9,10,5,-4,-2,5,7,-6,8,-5],[-5,-1,5,-1,-7,-5,-9,-10,-5,-1,3,6,-9,-6],[-2,-5,3,-7,-3,-9,-5,7,-9,8,-1,3,-8,-8],[1,3,7,2,5,-2,10,-9,6,-2,-4,1,1,1],[-4,6,5,1,-7,-1,4,1,5,-2,-7,-5,5,10],[1,5,10,-3,1,6,6,-8,-3,6,-10,-8,-3,10],[1,3,-1,7,10,-8,-3,8,-4,-4,5,4,10,-2],[4,-2,4,-7,2,8,-4,-2,1,-8,6,1,-2,9],[-6,7,-5,-3,2,3,3,-7,-10,-6,9,-5,6,8],[-10,1,8,-5,7,-3,7,-3,1,-9,-9,1,9,-2],[-3,-4,-7,-10,5,9,3,-8,-2,-3,3,4,-9,1],[-1,6,5,-7,-6,-7,-2,10,-2,10,-3,9,-6,-1],[5,4,7,10,-1,4,7,6,-2,7,-9,10,-1,-10],[-9,4,3,2,10,-3,2,-6,-1,-8,-3,6,3,3]], dtype = "uint8")#candidate|5023|(169, 14)|const|uint8
call_5022 = relay.TupleGetItem(func_1024_call(relay.reshape(const_5023.astype('uint8'), [14, 13, 13]), relay.reshape(const_5023.astype('uint8'), [14, 13, 13]), ), 0)
call_5024 = relay.TupleGetItem(func_1028_call(relay.reshape(const_5023.astype('uint8'), [14, 13, 13]), relay.reshape(const_5023.astype('uint8'), [14, 13, 13]), ), 0)
output = relay.Tuple([call_4968,call_5022,const_5023,])
output2 = relay.Tuple([call_4969,call_5024,const_5023,])
func_5043 = relay.Function([], output)
mod['func_5043'] = func_5043
mod = relay.transform.InferType()(mod)
output = func_5043()
func_5044 = relay.Function([], output)
mutated_mod['func_5044'] = func_5044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2320_call = mod.get_global_var('func_2320')
func_2322_call = mutated_mod.get_global_var('func_2322')
call_5061 = func_2320_call()
call_5062 = func_2320_call()
uop_5071 = relay.cosh(call_5061.astype('float32')) # shape=(2, 9, 9)
uop_5073 = relay.cosh(call_5062.astype('float32')) # shape=(2, 9, 9)
output = relay.Tuple([uop_5071,])
output2 = relay.Tuple([uop_5073,])
func_5100 = relay.Function([], output)
mod['func_5100'] = func_5100
mod = relay.transform.InferType()(mod)
output = func_5100()
func_5101 = relay.Function([], output)
mutated_mod['func_5101'] = func_5101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5100_call = mod.get_global_var('func_5100')
func_5101_call = mutated_mod.get_global_var('func_5101')
call_5192 = relay.TupleGetItem(func_5100_call(), 0)
call_5193 = relay.TupleGetItem(func_5101_call(), 0)
func_1966_call = mod.get_global_var('func_1966')
func_1968_call = mutated_mod.get_global_var('func_1968')
call_5203 = relay.TupleGetItem(func_1966_call(), 0)
call_5204 = relay.TupleGetItem(func_1968_call(), 0)
func_4127_call = mod.get_global_var('func_4127')
func_4128_call = mutated_mod.get_global_var('func_4128')
call_5218 = relay.TupleGetItem(func_4127_call(), 0)
call_5219 = relay.TupleGetItem(func_4128_call(), 0)
uop_5244 = relay.cos(call_5218.astype('float64')) # shape=(2, 9, 9)
uop_5246 = relay.cos(call_5219.astype('float64')) # shape=(2, 9, 9)
bop_5250 = relay.mod(uop_5244.astype('float32'), relay.reshape(call_5218.astype('float32'), relay.shape_of(uop_5244))) # shape=(2, 9, 9)
bop_5253 = relay.mod(uop_5246.astype('float32'), relay.reshape(call_5219.astype('float32'), relay.shape_of(uop_5246))) # shape=(2, 9, 9)
func_667_call = mod.get_global_var('func_667')
func_671_call = mutated_mod.get_global_var('func_671')
call_5279 = relay.TupleGetItem(func_667_call(relay.reshape(uop_5244.astype('float64'), [2, 9, 9]), relay.reshape(uop_5244.astype('float64'), [2, 9, 9]), ), 4)
call_5280 = relay.TupleGetItem(func_671_call(relay.reshape(uop_5244.astype('float64'), [2, 9, 9]), relay.reshape(uop_5244.astype('float64'), [2, 9, 9]), ), 4)
func_4840_call = mod.get_global_var('func_4840')
func_4841_call = mutated_mod.get_global_var('func_4841')
call_5285 = func_4840_call()
call_5286 = func_4840_call()
output = relay.Tuple([call_5192,call_5203,bop_5250,call_5279,call_5285,])
output2 = relay.Tuple([call_5193,call_5204,bop_5253,call_5280,call_5286,])
func_5296 = relay.Function([], output)
mod['func_5296'] = func_5296
mod = relay.transform.InferType()(mod)
output = func_5296()
func_5297 = relay.Function([], output)
mutated_mod['func_5297'] = func_5297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1726_call = mod.get_global_var('func_1726')
func_1728_call = mutated_mod.get_global_var('func_1728')
call_5365 = func_1726_call()
call_5366 = func_1726_call()
uop_5379 = relay.sqrt(call_5365.astype('float64')) # shape=(2, 9, 9)
uop_5381 = relay.sqrt(call_5366.astype('float64')) # shape=(2, 9, 9)
func_3695_call = mod.get_global_var('func_3695')
func_3699_call = mutated_mod.get_global_var('func_3699')
const_5383 = relay.const([5,-4,4,-2,9,-1,-2,3,9,2,1,-5,-2,-10,10,-6,-1,-5,2,-3,-7,-4,-3,-9,-8,-6,2,-1,2,-9,-9,9,-7,-4,-2,-10,3,-9,2,9,-6,-9,8,-5,3,3,10,1,-8,6,6,-10,1,-7,5,3,1,-2,-3,-9,10,8,6,9,8,4,1,-3,3,-5,6,-4,1,-5,-2,1,-6,3,-10,-8,8,-10,-7,-3,-3,-1,-8,5,2,2,-4,-7,1,4,4,8,3,-1,3,1,2,-6,-8,8,10,-3,2,-7,-1,4,5,5,4,-10,-10,4,6,2,10,5,1,-4,-7,-10,4,-4,-8,8,-7,-10,1,10,-3,-1,-6,10,-4,4,7,-2,8,1,4,-9,-8,-9,10,-8,6,5,-6,1,9,-3,-9,-9,-10,-4,-8,9,-1,-8,-10,3,6,7,-3,5,-4,-10,5,10,10,4,-7,5,-9,-9,9,-6,2,-8,2,8,-2,-8,10,4,4,-7,9,8,-4,9,-1,-10,-8,7,-4,5,7,-4,-5,-6,-4,-9,4,-3,6,-6,8,-9,6,6,5,7,9,9,-8,1,8,7,7,4,3,-10,6,7,7,4,-9,2,-2,9,5,-4,-2,-9,-2,-4,-3,-7,-4,-4,2,-3,-9,-8,-7,1,-9,-9,7,-1,10,-5,2,3,10,8,-3,10,7,3,7,8,-10,-6,-2,5,6,5,3,3,3,-3,4,2,-3,7,-10,5,-1,-4,-10,5,10,4,-7,-5,10,-1,-3,-10,-8,6,10,-8,2,4,-3,-10,10,-4,-10,-1,9,9,-3,-8,-3,-10,8,6,10,-6,10,5,9,-8,10,-1,1,9,-8,6,-5,-6,4,5,-1,-6,6,-2,-3,-3,-2,-2,-4,-7,-9,-4,9,7,10,-7,4,4,7,4,8,4,2,3,6,8,2,10,-2,5,1,-4,7,5,-4,5,6,4,-5,4,6,5,-4,1,3,7,-10,-1,9,-3,6,-6,7,-10,6,4,-6,10,-5,3,7,-6,-2,-3,4,5,4,-2,-1,5,-4,9,-7,9,10,-2,3,3,4,6,2,7,3,8,10,3,-2,6,-3,-1,-7,9,10,5,8,9,-3,7,-6,1,-8,-1,-7,2,-10,-1,6,8,2,10,-7,9,7,-7,10,-8,10,-3,-6,7,7,-4,-9,-1,-8,-10,-1,-4,-6,-3,8,-9,3,-5,4,-7,-9,-6], dtype = "uint64")#candidate|5383|(468,)|const|uint64
call_5382 = relay.TupleGetItem(func_3695_call(relay.reshape(const_5383.astype('uint64'), [13, 3, 12]), relay.reshape(const_5383.astype('uint64'), [13, 3, 12]), ), 0)
call_5384 = relay.TupleGetItem(func_3699_call(relay.reshape(const_5383.astype('uint64'), [13, 3, 12]), relay.reshape(const_5383.astype('uint64'), [13, 3, 12]), ), 0)
func_1927_call = mod.get_global_var('func_1927')
func_1928_call = mutated_mod.get_global_var('func_1928')
call_5387 = func_1927_call()
call_5388 = func_1927_call()
func_2803_call = mod.get_global_var('func_2803')
func_2805_call = mutated_mod.get_global_var('func_2805')
var_5396 = relay.var("var_5396", dtype = "float64", shape = (7, 15))#candidate|5396|(7, 15)|var|float64
call_5395 = relay.TupleGetItem(func_2803_call(relay.reshape(var_5396.astype('float64'), [105,])), 0)
call_5397 = relay.TupleGetItem(func_2805_call(relay.reshape(var_5396.astype('float64'), [105,])), 0)
func_1237_call = mod.get_global_var('func_1237')
func_1241_call = mutated_mod.get_global_var('func_1241')
var_5424 = relay.var("var_5424", dtype = "uint16", shape = (60,))#candidate|5424|(60,)|var|uint16
call_5423 = relay.TupleGetItem(func_1237_call(relay.reshape(var_5424.astype('uint16'), [5, 3, 4]), relay.reshape(var_5424.astype('uint16'), [5, 3, 4]), ), 0)
call_5425 = relay.TupleGetItem(func_1241_call(relay.reshape(var_5424.astype('uint16'), [5, 3, 4]), relay.reshape(var_5424.astype('uint16'), [5, 3, 4]), ), 0)
func_3591_call = mod.get_global_var('func_3591')
func_3592_call = mutated_mod.get_global_var('func_3592')
call_5426 = func_3591_call()
call_5427 = func_3591_call()
uop_5437 = relay.sinh(call_5423.astype('float32')) # shape=(5, 3, 4)
uop_5439 = relay.sinh(call_5425.astype('float32')) # shape=(5, 3, 4)
output = relay.Tuple([uop_5379,call_5382,const_5383,call_5387,call_5395,var_5396,var_5424,call_5426,uop_5437,])
output2 = relay.Tuple([uop_5381,call_5384,const_5383,call_5388,call_5397,var_5396,var_5424,call_5427,uop_5439,])
func_5446 = relay.Function([var_5396,var_5424,], output)
mod['func_5446'] = func_5446
mod = relay.transform.InferType()(mod)
var_5447 = relay.var("var_5447", dtype = "float64", shape = (7, 15))#candidate|5447|(7, 15)|var|float64
var_5448 = relay.var("var_5448", dtype = "uint16", shape = (60,))#candidate|5448|(60,)|var|uint16
output = func_5446(var_5447,var_5448,)
func_5449 = relay.Function([var_5447,var_5448,], output)
mutated_mod['func_5449'] = func_5449
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5492 = relay.var("var_5492", dtype = "uint16", shape = ())#candidate|5492|()|var|uint16
var_5493 = relay.var("var_5493", dtype = "uint16", shape = (7, 6, 11))#candidate|5493|(7, 6, 11)|var|uint16
bop_5494 = relay.subtract(var_5492.astype('uint16'), var_5493.astype('uint16')) # shape=(7, 6, 11)
output = relay.Tuple([bop_5494,])
output2 = relay.Tuple([bop_5494,])
func_5522 = relay.Function([var_5492,var_5493,], output)
mod['func_5522'] = func_5522
mod = relay.transform.InferType()(mod)
mutated_mod['func_5522'] = func_5522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5522_call = mutated_mod.get_global_var('func_5522')
var_5524 = relay.var("var_5524", dtype = "uint16", shape = ())#candidate|5524|()|var|uint16
var_5525 = relay.var("var_5525", dtype = "uint16", shape = (7, 6, 11))#candidate|5525|(7, 6, 11)|var|uint16
call_5523 = func_5522_call(var_5524,var_5525,)
output = call_5523
func_5526 = relay.Function([var_5524,var_5525,], output)
mutated_mod['func_5526'] = func_5526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_5539 = relay.TupleGetItem(func_261_call(), 0)
call_5540 = relay.TupleGetItem(func_263_call(), 0)
output = relay.Tuple([call_5539,])
output2 = relay.Tuple([call_5540,])
func_5567 = relay.Function([], output)
mod['func_5567'] = func_5567
mod = relay.transform.InferType()(mod)
output = func_5567()
func_5568 = relay.Function([], output)
mutated_mod['func_5568'] = func_5568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5567_call = mod.get_global_var('func_5567')
func_5568_call = mutated_mod.get_global_var('func_5568')
call_5595 = relay.TupleGetItem(func_5567_call(), 0)
call_5596 = relay.TupleGetItem(func_5568_call(), 0)
func_1726_call = mod.get_global_var('func_1726')
func_1728_call = mutated_mod.get_global_var('func_1728')
call_5598 = func_1726_call()
call_5599 = func_1726_call()
output = relay.Tuple([call_5595,call_5598,])
output2 = relay.Tuple([call_5596,call_5599,])
func_5609 = relay.Function([], output)
mod['func_5609'] = func_5609
mod = relay.transform.InferType()(mod)
output = func_5609()
func_5610 = relay.Function([], output)
mutated_mod['func_5610'] = func_5610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_438_call = mod.get_global_var('func_438')
func_439_call = mutated_mod.get_global_var('func_439')
call_5624 = func_438_call()
call_5625 = func_438_call()
func_1237_call = mod.get_global_var('func_1237')
func_1241_call = mutated_mod.get_global_var('func_1241')
var_5629 = relay.var("var_5629", dtype = "uint16", shape = (60,))#candidate|5629|(60,)|var|uint16
call_5628 = relay.TupleGetItem(func_1237_call(relay.reshape(var_5629.astype('uint16'), [5, 3, 4]), relay.reshape(var_5629.astype('uint16'), [5, 3, 4]), ), 0)
call_5630 = relay.TupleGetItem(func_1241_call(relay.reshape(var_5629.astype('uint16'), [5, 3, 4]), relay.reshape(var_5629.astype('uint16'), [5, 3, 4]), ), 0)
output = relay.Tuple([call_5624,call_5628,var_5629,])
output2 = relay.Tuple([call_5625,call_5630,var_5629,])
func_5632 = relay.Function([var_5629,], output)
mod['func_5632'] = func_5632
mod = relay.transform.InferType()(mod)
mutated_mod['func_5632'] = func_5632
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5633 = relay.var("var_5633", dtype = "uint16", shape = (60,))#candidate|5633|(60,)|var|uint16
func_5632_call = mutated_mod.get_global_var('func_5632')
call_5634 = func_5632_call(var_5633)
output = call_5634
func_5635 = relay.Function([var_5633], output)
mutated_mod['func_5635'] = func_5635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4127_call = mod.get_global_var('func_4127')
func_4128_call = mutated_mod.get_global_var('func_4128')
call_5645 = relay.TupleGetItem(func_4127_call(), 0)
call_5646 = relay.TupleGetItem(func_4128_call(), 0)
output = relay.Tuple([call_5645,])
output2 = relay.Tuple([call_5646,])
func_5667 = relay.Function([], output)
mod['func_5667'] = func_5667
mod = relay.transform.InferType()(mod)
output = func_5667()
func_5668 = relay.Function([], output)
mutated_mod['func_5668'] = func_5668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_413_call = mod.get_global_var('func_413')
func_415_call = mutated_mod.get_global_var('func_415')
call_5683 = relay.TupleGetItem(func_413_call(), 0)
call_5684 = relay.TupleGetItem(func_415_call(), 0)
func_1154_call = mod.get_global_var('func_1154')
func_1155_call = mutated_mod.get_global_var('func_1155')
call_5692 = relay.TupleGetItem(func_1154_call(), 0)
call_5693 = relay.TupleGetItem(func_1155_call(), 0)
output = relay.Tuple([call_5683,call_5692,])
output2 = relay.Tuple([call_5684,call_5693,])
func_5734 = relay.Function([], output)
mod['func_5734'] = func_5734
mod = relay.transform.InferType()(mod)
mutated_mod['func_5734'] = func_5734
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5734_call = mutated_mod.get_global_var('func_5734')
call_5735 = func_5734_call()
output = call_5735
func_5736 = relay.Function([], output)
mutated_mod['func_5736'] = func_5736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_413_call = mod.get_global_var('func_413')
func_415_call = mutated_mod.get_global_var('func_415')
call_5759 = relay.TupleGetItem(func_413_call(), 0)
call_5760 = relay.TupleGetItem(func_415_call(), 0)
output = relay.Tuple([call_5759,])
output2 = relay.Tuple([call_5760,])
func_5785 = relay.Function([], output)
mod['func_5785'] = func_5785
mod = relay.transform.InferType()(mod)
output = func_5785()
func_5786 = relay.Function([], output)
mutated_mod['func_5786'] = func_5786
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5810 = relay.var("var_5810", dtype = "float32", shape = (15, 11, 1))#candidate|5810|(15, 11, 1)|var|float32
uop_5811 = relay.cos(var_5810.astype('float32')) # shape=(15, 11, 1)
uop_5813 = relay.acosh(uop_5811.astype('float64')) # shape=(15, 11, 1)
uop_5820 = relay.log2(uop_5813.astype('float32')) # shape=(15, 11, 1)
output = uop_5820
output2 = uop_5820
func_5826 = relay.Function([var_5810,], output)
mod['func_5826'] = func_5826
mod = relay.transform.InferType()(mod)
var_5827 = relay.var("var_5827", dtype = "float32", shape = (15, 11, 1))#candidate|5827|(15, 11, 1)|var|float32
output = func_5826(var_5827)
func_5828 = relay.Function([var_5827], output)
mutated_mod['func_5828'] = func_5828
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5873 = relay.var("var_5873", dtype = "bool", shape = (6, 14, 3))#candidate|5873|(6, 14, 3)|var|bool
var_5874 = relay.var("var_5874", dtype = "bool", shape = (6, 14, 3))#candidate|5874|(6, 14, 3)|var|bool
bop_5875 = relay.logical_or(var_5873.astype('bool'), relay.reshape(var_5874.astype('bool'), relay.shape_of(var_5873))) # shape=(6, 14, 3)
func_744_call = mod.get_global_var('func_744')
func_745_call = mutated_mod.get_global_var('func_745')
call_5885 = relay.TupleGetItem(func_744_call(), 2)
call_5886 = relay.TupleGetItem(func_745_call(), 2)
bop_5889 = relay.maximum(var_5873.astype('uint32'), relay.reshape(var_5874.astype('uint32'), relay.shape_of(var_5873))) # shape=(6, 14, 3)
output = relay.Tuple([bop_5875,call_5885,bop_5889,])
output2 = relay.Tuple([bop_5875,call_5886,bop_5889,])
func_5904 = relay.Function([var_5873,var_5874,], output)
mod['func_5904'] = func_5904
mod = relay.transform.InferType()(mod)
mutated_mod['func_5904'] = func_5904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5904_call = mutated_mod.get_global_var('func_5904')
var_5906 = relay.var("var_5906", dtype = "bool", shape = (6, 14, 3))#candidate|5906|(6, 14, 3)|var|bool
var_5907 = relay.var("var_5907", dtype = "bool", shape = (6, 14, 3))#candidate|5907|(6, 14, 3)|var|bool
call_5905 = func_5904_call(var_5906,var_5907,)
output = call_5905
func_5908 = relay.Function([var_5906,var_5907,], output)
mutated_mod['func_5908'] = func_5908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_922_call = mod.get_global_var('func_922')
func_924_call = mutated_mod.get_global_var('func_924')
call_5912 = func_922_call()
call_5913 = func_922_call()
func_3648_call = mod.get_global_var('func_3648')
func_3649_call = mutated_mod.get_global_var('func_3649')
call_5921 = func_3648_call()
call_5922 = func_3648_call()
func_4168_call = mod.get_global_var('func_4168')
func_4169_call = mutated_mod.get_global_var('func_4169')
call_5924 = relay.TupleGetItem(func_4168_call(), 1)
call_5925 = relay.TupleGetItem(func_4169_call(), 1)
output = relay.Tuple([call_5912,call_5921,call_5924,])
output2 = relay.Tuple([call_5913,call_5922,call_5925,])
func_5929 = relay.Function([], output)
mod['func_5929'] = func_5929
mod = relay.transform.InferType()(mod)
mutated_mod['func_5929'] = func_5929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5929_call = mutated_mod.get_global_var('func_5929')
call_5930 = func_5929_call()
output = call_5930
func_5931 = relay.Function([], output)
mutated_mod['func_5931'] = func_5931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4566_call = mod.get_global_var('func_4566')
func_4568_call = mutated_mod.get_global_var('func_4568')
call_5935 = relay.TupleGetItem(func_4566_call(), 3)
call_5936 = relay.TupleGetItem(func_4568_call(), 3)
func_982_call = mod.get_global_var('func_982')
func_984_call = mutated_mod.get_global_var('func_984')
var_5950 = relay.var("var_5950", dtype = "float64", shape = (21, 5))#candidate|5950|(21, 5)|var|float64
call_5949 = relay.TupleGetItem(func_982_call(relay.reshape(var_5950.astype('float64'), [105,])), 0)
call_5951 = relay.TupleGetItem(func_984_call(relay.reshape(var_5950.astype('float64'), [105,])), 0)
output = relay.Tuple([call_5935,call_5949,var_5950,])
output2 = relay.Tuple([call_5936,call_5951,var_5950,])
func_5958 = relay.Function([var_5950,], output)
mod['func_5958'] = func_5958
mod = relay.transform.InferType()(mod)
mutated_mod['func_5958'] = func_5958
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5959 = relay.var("var_5959", dtype = "float64", shape = (21, 5))#candidate|5959|(21, 5)|var|float64
func_5958_call = mutated_mod.get_global_var('func_5958')
call_5960 = func_5958_call(var_5959)
output = call_5960
func_5961 = relay.Function([var_5959], output)
mutated_mod['func_5961'] = func_5961
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4289_call = mod.get_global_var('func_4289')
func_4290_call = mutated_mod.get_global_var('func_4290')
call_6009 = relay.TupleGetItem(func_4289_call(), 0)
call_6010 = relay.TupleGetItem(func_4290_call(), 0)
func_4397_call = mod.get_global_var('func_4397')
func_4399_call = mutated_mod.get_global_var('func_4399')
var_6029 = relay.var("var_6029", dtype = "bool", shape = (686,))#candidate|6029|(686,)|var|bool
call_6028 = relay.TupleGetItem(func_4397_call(relay.reshape(var_6029.astype('bool'), [686,])), 1)
call_6030 = relay.TupleGetItem(func_4399_call(relay.reshape(var_6029.astype('bool'), [686,])), 1)
output = relay.Tuple([call_6009,call_6028,var_6029,])
output2 = relay.Tuple([call_6010,call_6030,var_6029,])
func_6036 = relay.Function([var_6029,], output)
mod['func_6036'] = func_6036
mod = relay.transform.InferType()(mod)
var_6037 = relay.var("var_6037", dtype = "bool", shape = (686,))#candidate|6037|(686,)|var|bool
output = func_6036(var_6037)
func_6038 = relay.Function([var_6037], output)
mutated_mod['func_6038'] = func_6038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4019_call = mod.get_global_var('func_4019')
func_4020_call = mutated_mod.get_global_var('func_4020')
call_6040 = relay.TupleGetItem(func_4019_call(), 1)
call_6041 = relay.TupleGetItem(func_4020_call(), 1)
output = call_6040
output2 = call_6041
func_6047 = relay.Function([], output)
mod['func_6047'] = func_6047
mod = relay.transform.InferType()(mod)
output = func_6047()
func_6048 = relay.Function([], output)
mutated_mod['func_6048'] = func_6048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3864_call = mod.get_global_var('func_3864')
func_3865_call = mutated_mod.get_global_var('func_3865')
call_6052 = relay.TupleGetItem(func_3864_call(), 0)
call_6053 = relay.TupleGetItem(func_3865_call(), 0)
func_1397_call = mod.get_global_var('func_1397')
func_1398_call = mutated_mod.get_global_var('func_1398')
call_6056 = relay.TupleGetItem(func_1397_call(), 0)
call_6057 = relay.TupleGetItem(func_1398_call(), 0)
output = relay.Tuple([call_6052,call_6056,])
output2 = relay.Tuple([call_6053,call_6057,])
func_6068 = relay.Function([], output)
mod['func_6068'] = func_6068
mod = relay.transform.InferType()(mod)
mutated_mod['func_6068'] = func_6068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6068_call = mutated_mod.get_global_var('func_6068')
call_6069 = func_6068_call()
output = call_6069
func_6070 = relay.Function([], output)
mutated_mod['func_6070'] = func_6070
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3794_call = mod.get_global_var('func_3794')
func_3795_call = mutated_mod.get_global_var('func_3795')
call_6089 = relay.TupleGetItem(func_3794_call(), 0)
call_6090 = relay.TupleGetItem(func_3795_call(), 0)
output = call_6089
output2 = call_6090
func_6106 = relay.Function([], output)
mod['func_6106'] = func_6106
mod = relay.transform.InferType()(mod)
mutated_mod['func_6106'] = func_6106
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6106_call = mutated_mod.get_global_var('func_6106')
call_6107 = func_6106_call()
output = call_6107
func_6108 = relay.Function([], output)
mutated_mod['func_6108'] = func_6108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4882_call = mod.get_global_var('func_4882')
func_4883_call = mutated_mod.get_global_var('func_4883')
call_6124 = relay.TupleGetItem(func_4882_call(), 0)
call_6125 = relay.TupleGetItem(func_4883_call(), 0)
var_6164 = relay.var("var_6164", dtype = "float32", shape = (2, 9, 9))#candidate|6164|(2, 9, 9)|var|float32
bop_6165 = relay.floor_divide(call_6124.astype('float64'), relay.reshape(var_6164.astype('float64'), relay.shape_of(call_6124))) # shape=(2, 9, 9)
bop_6168 = relay.floor_divide(call_6125.astype('float64'), relay.reshape(var_6164.astype('float64'), relay.shape_of(call_6125))) # shape=(2, 9, 9)
func_3564_call = mod.get_global_var('func_3564')
func_3566_call = mutated_mod.get_global_var('func_3566')
call_6176 = func_3564_call()
call_6177 = func_3564_call()
output = relay.Tuple([bop_6165,call_6176,])
output2 = relay.Tuple([bop_6168,call_6177,])
func_6208 = relay.Function([var_6164,], output)
mod['func_6208'] = func_6208
mod = relay.transform.InferType()(mod)
mutated_mod['func_6208'] = func_6208
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6209 = relay.var("var_6209", dtype = "float32", shape = (2, 9, 9))#candidate|6209|(2, 9, 9)|var|float32
func_6208_call = mutated_mod.get_global_var('func_6208')
call_6210 = func_6208_call(var_6209)
output = call_6210
func_6211 = relay.Function([var_6209], output)
mutated_mod['func_6211'] = func_6211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4907_call = mod.get_global_var('func_4907')
func_4908_call = mutated_mod.get_global_var('func_4908')
call_6219 = func_4907_call()
call_6220 = func_4907_call()
uop_6237 = relay.asinh(call_6219.astype('float64')) # shape=(7, 7, 2)
uop_6239 = relay.asinh(call_6220.astype('float64')) # shape=(7, 7, 2)
uop_6250 = relay.atan(uop_6237.astype('float32')) # shape=(7, 7, 2)
uop_6252 = relay.atan(uop_6239.astype('float32')) # shape=(7, 7, 2)
func_963_call = mod.get_global_var('func_963')
func_965_call = mutated_mod.get_global_var('func_965')
var_6255 = relay.var("var_6255", dtype = "float64", shape = (105,))#candidate|6255|(105,)|var|float64
call_6254 = relay.TupleGetItem(func_963_call(relay.reshape(var_6255.astype('float64'), [105,])), 2)
call_6256 = relay.TupleGetItem(func_965_call(relay.reshape(var_6255.astype('float64'), [105,])), 2)
func_5734_call = mod.get_global_var('func_5734')
func_5736_call = mutated_mod.get_global_var('func_5736')
call_6261 = relay.TupleGetItem(func_5734_call(), 0)
call_6262 = relay.TupleGetItem(func_5736_call(), 0)
output = relay.Tuple([uop_6250,call_6254,var_6255,call_6261,])
output2 = relay.Tuple([uop_6252,call_6256,var_6255,call_6262,])
func_6270 = relay.Function([var_6255,], output)
mod['func_6270'] = func_6270
mod = relay.transform.InferType()(mod)
var_6271 = relay.var("var_6271", dtype = "float64", shape = (105,))#candidate|6271|(105,)|var|float64
output = func_6270(var_6271)
func_6272 = relay.Function([var_6271], output)
mutated_mod['func_6272'] = func_6272
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1927_call = mod.get_global_var('func_1927')
func_1928_call = mutated_mod.get_global_var('func_1928')
call_6274 = func_1927_call()
call_6275 = func_1927_call()
output = relay.Tuple([call_6274,])
output2 = relay.Tuple([call_6275,])
func_6284 = relay.Function([], output)
mod['func_6284'] = func_6284
mod = relay.transform.InferType()(mod)
mutated_mod['func_6284'] = func_6284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6284_call = mutated_mod.get_global_var('func_6284')
call_6285 = func_6284_call()
output = call_6285
func_6286 = relay.Function([], output)
mutated_mod['func_6286'] = func_6286
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5609_call = mod.get_global_var('func_5609')
func_5610_call = mutated_mod.get_global_var('func_5610')
call_6294 = relay.TupleGetItem(func_5609_call(), 1)
call_6295 = relay.TupleGetItem(func_5610_call(), 1)
func_6106_call = mod.get_global_var('func_6106')
func_6108_call = mutated_mod.get_global_var('func_6108')
call_6304 = func_6106_call()
call_6305 = func_6106_call()
output = relay.Tuple([call_6294,call_6304,])
output2 = relay.Tuple([call_6295,call_6305,])
func_6350 = relay.Function([], output)
mod['func_6350'] = func_6350
mod = relay.transform.InferType()(mod)
mutated_mod['func_6350'] = func_6350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6350_call = mutated_mod.get_global_var('func_6350')
call_6351 = func_6350_call()
output = call_6351
func_6352 = relay.Function([], output)
mutated_mod['func_6352'] = func_6352
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3381_call = mod.get_global_var('func_3381')
func_3383_call = mutated_mod.get_global_var('func_3383')
call_6395 = relay.TupleGetItem(func_3381_call(), 0)
call_6396 = relay.TupleGetItem(func_3383_call(), 0)
func_1799_call = mod.get_global_var('func_1799')
func_1800_call = mutated_mod.get_global_var('func_1800')
call_6402 = relay.TupleGetItem(func_1799_call(), 0)
call_6403 = relay.TupleGetItem(func_1800_call(), 0)
output = relay.Tuple([call_6395,call_6402,])
output2 = relay.Tuple([call_6396,call_6403,])
func_6406 = relay.Function([], output)
mod['func_6406'] = func_6406
mod = relay.transform.InferType()(mod)
output = func_6406()
func_6407 = relay.Function([], output)
mutated_mod['func_6407'] = func_6407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4456_call = mod.get_global_var('func_4456')
func_4457_call = mutated_mod.get_global_var('func_4457')
call_6426 = func_4456_call()
call_6427 = func_4456_call()
func_3864_call = mod.get_global_var('func_3864')
func_3865_call = mutated_mod.get_global_var('func_3865')
call_6444 = relay.TupleGetItem(func_3864_call(), 0)
call_6445 = relay.TupleGetItem(func_3865_call(), 0)
output = relay.Tuple([call_6426,call_6444,])
output2 = relay.Tuple([call_6427,call_6445,])
func_6479 = relay.Function([], output)
mod['func_6479'] = func_6479
mod = relay.transform.InferType()(mod)
mutated_mod['func_6479'] = func_6479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6479_call = mutated_mod.get_global_var('func_6479')
call_6480 = func_6479_call()
output = call_6480
func_6481 = relay.Function([], output)
mutated_mod['func_6481'] = func_6481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4907_call = mod.get_global_var('func_4907')
func_4908_call = mutated_mod.get_global_var('func_4908')
call_6535 = func_4907_call()
call_6536 = func_4907_call()
output = relay.Tuple([call_6535,])
output2 = relay.Tuple([call_6536,])
func_6546 = relay.Function([], output)
mod['func_6546'] = func_6546
mod = relay.transform.InferType()(mod)
mutated_mod['func_6546'] = func_6546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6546_call = mutated_mod.get_global_var('func_6546')
call_6547 = func_6546_call()
output = call_6547
func_6548 = relay.Function([], output)
mutated_mod['func_6548'] = func_6548
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6573 = relay.const([[[-4.455726,-7.727146,8.445701,5.485835,3.632222,-5.345867,2.270204,-1.456469,-0.007276,2.209374,-9.506307,-2.277193,6.766677],[-8.252814,5.381910,7.464423,-3.847559,6.668089,-3.942525,9.957028,5.480750,-2.840073,-1.098556,-4.733649,-7.211028,3.536624],[2.284369,-3.679822,7.549378,4.399788,-4.401161,6.262379,-8.409571,-9.858726,8.477572,-3.339960,6.411447,4.432187,-7.025493],[-0.600933,9.599819,8.078605,3.561619,-1.720376,9.242551,7.970911,-4.983592,-8.886521,-0.099396,-7.908041,-5.212605,-1.151133],[9.924552,9.232504,0.284257,9.545661,3.972789,9.792627,-7.133894,-0.854634,6.713982,8.219327,-1.837727,9.850402,9.324738],[-1.435938,-7.991731,4.908061,-5.026647,1.809287,1.820954,1.084506,-3.173658,0.007621,-4.221319,-6.562054,-2.374241,0.402594],[6.650512,7.100990,-2.235301,8.205827,-1.654058,5.130501,2.770529,-6.624394,2.432162,-4.269019,-9.540455,-5.686892,9.132776],[-2.790628,-7.863798,-1.636639,-8.794352,-1.401518,1.284572,-2.706923,6.018133,-9.126891,-8.881290,0.077335,-7.085358,8.653590],[0.977846,6.369013,-1.867252,-5.681465,-1.704293,9.394453,-4.576383,7.061572,8.857040,3.510729,4.431740,8.751714,-2.488800],[1.716848,-9.539050,8.170489,-1.726646,-0.095278,7.065252,-5.063759,6.824540,-4.776777,3.236679,1.344532,0.064350,7.738435],[1.631609,0.901248,9.694261,-1.981124,3.675709,-7.654386,3.908314,4.614264,9.368707,-3.545327,7.350698,1.038063,-9.572284]],[[5.614063,3.439169,1.717838,8.493167,3.461310,5.389731,0.928357,2.490660,4.977240,-8.605407,9.504800,-3.990239,4.874359],[6.367572,-5.598971,8.543659,6.656425,3.264864,4.220950,8.143017,3.964343,4.413165,-1.468543,-8.898756,3.784575,-3.584823],[8.767347,-2.702438,-2.965762,2.687884,5.778197,-2.387668,4.488343,8.810612,-6.434040,5.163685,-9.274008,-4.072362,-5.560033],[-3.455071,-8.222731,-9.286929,6.122245,-4.770886,-0.724921,-5.632448,-0.784177,9.416761,-4.004843,5.400507,9.702107,7.883037],[8.208291,-6.096215,-7.763178,0.453224,2.168157,-0.896577,-7.659515,-6.874679,-1.753905,-6.162423,5.155897,5.574110,9.764211],[8.626652,4.555831,-2.602566,-4.838696,-8.503709,3.603974,9.145700,-3.229459,7.160926,-8.271205,4.078165,-6.954500,-8.315062],[5.658083,-1.556357,-3.736061,-8.456307,-2.261558,-7.314066,6.515151,9.702293,-8.922964,-7.250356,7.831743,6.673823,3.097611],[-1.821724,-5.271435,-4.312394,-3.481387,-1.333387,-3.245002,3.584111,4.414858,1.644224,-1.622869,8.368092,-1.922076,6.538523],[7.054043,6.830965,-0.276714,6.353451,-9.674784,-5.830008,-9.155210,3.374336,9.123942,2.352745,-1.689192,-4.577980,3.605410],[5.050094,9.539152,3.436709,8.712596,1.896856,9.994959,1.746818,-9.348663,-6.439576,-9.014554,4.093320,-9.874134,4.128837],[-7.025500,-7.331579,6.515475,2.521803,-7.493895,-4.193662,6.684355,5.783844,-8.530479,8.819499,3.588032,6.142836,7.804751]],[[8.885573,6.975790,2.368528,-4.702625,7.967290,4.390090,-7.533308,-9.602610,-1.664740,3.439326,-3.695979,-3.849800,-2.486071],[9.929015,1.552895,5.617235,0.970685,5.444085,-7.294446,-5.218946,-0.092875,-2.298904,8.451438,5.939588,-5.655689,-3.088169],[-5.919189,-7.274241,-5.550239,-0.456024,3.803757,-6.903530,-4.776525,1.866080,-8.852782,-7.648738,8.375189,3.726273,3.219966],[-5.481377,1.430626,-4.709265,5.760623,3.834902,7.858589,-5.476286,5.959575,7.402888,-8.693039,-2.649230,-6.941233,9.288121],[8.935516,-8.782261,1.233520,-1.971137,7.466508,-4.601578,-1.909108,-7.012657,0.567405,-0.671727,-2.315185,-6.723039,-4.789596],[5.218983,-1.967983,-8.617473,4.116541,-6.976265,-0.459966,-8.631941,-8.985525,-5.215119,-6.728685,-6.261081,7.996282,-8.838424],[-7.010498,8.443367,1.505670,3.943839,9.749937,1.591851,-6.648223,-8.803543,-0.518657,9.632362,3.086410,4.408572,-6.713842],[-2.632077,-8.452309,8.998666,2.787216,1.884147,7.087836,-5.278432,1.500841,-8.695256,-3.208004,-5.171682,4.270723,1.854737],[9.325979,-8.467437,-7.556035,-9.893061,1.134569,1.902411,-2.571923,1.288584,3.511585,-9.658635,9.885293,-4.706735,2.461111],[-5.331834,-9.102317,-7.062591,3.299045,-9.075557,3.957071,-2.919340,-5.015467,1.875052,7.402062,0.281466,7.155250,8.092609],[-8.085425,-0.100687,-4.926755,-6.575673,-4.603910,-9.657868,7.912648,2.141646,5.693806,3.787867,2.226791,-0.144120,1.321526]],[[0.471639,-8.102954,9.722847,-6.963238,-4.167035,-0.872774,-3.544763,8.737372,-3.851562,9.175288,2.544463,-3.850692,-7.730397],[-4.967657,-5.104534,-8.324112,-6.357084,-7.481061,4.903524,6.441837,8.610202,-6.085846,-2.168916,-9.912197,-0.522338,-5.416108],[2.201506,-1.588421,-3.464256,-7.419068,-8.536791,-5.751374,5.509732,-2.654741,5.979544,6.080075,-5.173638,-8.031521,1.808833],[9.455216,-1.834945,-5.166488,-7.561788,-1.609444,1.601069,9.938988,0.160822,-3.245376,-6.613841,-2.350824,-2.177799,-1.894815],[3.936469,3.615234,-1.727308,7.992939,-3.277263,-2.309318,-1.860006,3.553808,4.018985,-3.692787,-4.923052,-4.269475,2.431420],[-4.788792,-5.408847,-1.070401,-1.394788,-4.948589,3.609530,3.122721,8.288240,-6.011010,-2.387234,9.815881,3.348639,8.271662],[-8.857943,-3.369501,-4.055755,2.699531,-4.388703,-5.121594,5.709471,6.499266,-0.910178,-8.539073,-5.238736,-0.720475,-7.428540],[-1.983505,4.662890,3.388812,1.277197,8.679505,1.853589,-1.760663,2.269946,-6.823673,-9.723510,4.742124,-0.665191,-5.181910],[-8.032712,-9.780942,7.582612,-3.896049,-6.609389,-2.880674,-0.984436,2.733804,0.142587,8.804276,-7.650302,0.044579,3.708963],[-9.405594,4.044142,-9.213062,9.832457,-8.804646,5.714010,8.226754,1.796353,-1.955422,8.424888,8.070921,6.801938,9.873316],[-8.833722,-0.190293,8.505812,6.296262,-3.441261,3.934764,-0.662713,-2.846737,-7.258472,1.385533,0.370507,2.726717,3.697484]],[[4.000527,2.940653,7.439591,-6.348296,5.493658,-7.037139,-8.113118,-1.260788,-6.534980,8.785423,3.788115,-1.204663,3.367914],[-6.650428,-5.305118,2.981918,-5.577818,9.060642,-3.169166,-3.600022,9.896409,7.780158,4.893760,1.638073,-8.509966,-9.197625],[0.677217,1.240486,-4.822790,5.462419,5.436965,3.276791,-0.725090,5.499609,-1.098935,-6.088568,-3.456305,1.542000,-8.036705],[9.485373,9.155072,-8.337264,-3.548247,-8.833981,3.448747,-8.669232,-9.932303,-5.322297,-4.462340,-9.551080,9.770124,-1.739375],[-6.631407,5.081931,0.585539,2.705128,-0.384480,3.574205,1.108144,-2.612085,7.154176,-2.947848,-4.583150,-0.448524,-7.877354],[1.574234,-2.403508,-0.786119,0.724829,9.051308,-1.504396,7.354709,-9.992802,-3.179422,-8.675134,-7.548511,5.985658,-2.231043],[7.940507,-1.710241,2.505245,-0.061731,1.710005,-5.388414,-9.804263,9.539684,-9.155613,-2.604964,2.423942,3.805605,9.164916],[-7.179800,-4.700880,-1.312669,2.702731,4.102109,-0.396561,-8.955974,-7.436848,-7.317331,-6.305793,-7.536290,-4.781285,5.930759],[7.217052,-0.027307,-3.228799,5.310406,8.013740,0.585662,-2.377173,0.615194,-7.543147,-3.766145,-4.754905,8.892831,2.794503],[1.098683,-0.335811,3.271851,1.690777,-5.871974,-9.043754,-5.435507,7.889882,5.268793,3.979773,-9.186273,-8.191487,-1.332394],[7.801810,-2.793896,4.434883,9.704813,-8.111232,5.189058,-1.744507,-8.352740,3.755027,-0.865295,-3.691963,-5.352989,-2.955329]],[[5.014077,-9.834095,9.828642,0.409313,-8.352410,7.398005,0.897438,-8.341254,-5.047934,-7.876591,-4.688935,5.097992,2.912887],[-4.025126,2.716153,-1.373105,3.284338,6.401985,3.909944,-4.231946,3.830184,9.905352,-9.143337,-6.522121,-8.841574,5.613793],[-2.294328,5.205991,-2.949244,-0.564583,-0.012354,-0.793194,0.786479,-7.882757,-2.038418,-3.660912,-9.404426,-4.937081,7.172185],[5.167448,-7.277719,-5.812697,-3.433012,-8.220188,9.252023,-3.692875,7.093890,-3.889072,-4.754588,7.567009,9.066202,3.569661],[6.786652,-5.456792,-8.674871,-2.836141,-3.274181,0.427871,-8.342300,2.559014,-7.323962,6.830210,-9.173903,-4.387488,-7.141142],[-0.204621,5.809075,-7.104579,3.741863,-1.362918,-4.893700,-8.327486,9.935670,0.797553,1.403244,-8.344957,9.656091,-6.455077],[6.594432,-8.124933,-9.951310,3.961024,-3.197121,0.546960,4.507464,8.985863,-0.499023,-5.325434,-8.186050,-6.999161,8.766137],[1.807510,-5.920766,-2.800302,5.074594,-7.152314,1.063661,0.831603,1.355299,-4.242727,-2.612546,-2.234291,8.228313,1.428548],[0.251540,-6.783476,-9.851491,4.557124,7.868155,-1.725840,-0.615260,-7.631593,-8.582139,-3.781753,-9.257345,-6.630975,-1.963603],[-3.144188,-1.290727,8.185734,9.659861,-4.231671,-0.346071,-5.262062,9.856315,-6.389047,1.264562,-6.293838,-1.697687,3.189030],[4.086181,-3.882062,1.489854,8.297297,-9.142068,9.579340,-1.296692,5.516498,9.752185,-1.590548,-1.109523,-6.818207,-9.992885]],[[6.343137,5.764662,0.430540,3.882622,6.287465,-4.494078,-9.908009,7.704435,-3.718009,8.084563,-3.060313,-7.432033,2.787545],[1.194221,-6.022551,-9.481249,3.329746,0.441609,-1.389499,-9.516785,3.814290,0.457474,9.662153,7.897201,-7.221764,3.578125],[8.643282,-1.352692,-4.940632,-4.183733,3.905317,-8.784272,6.690286,9.727961,-9.349740,0.687963,6.875339,6.083845,4.800447],[-2.004919,5.813726,7.685097,3.526531,-0.542195,1.835836,9.037248,2.230947,9.977263,3.379285,5.799053,-1.869074,9.338822],[2.888734,-9.218450,1.508911,-5.169141,-4.935589,4.227387,4.707365,7.825870,-7.151021,8.152139,5.244529,-7.875138,-7.246879],[-2.628892,-1.239569,-4.559270,6.389098,9.261752,6.359039,2.170366,5.284627,-5.621432,-8.577363,3.792377,-7.617928,3.888692],[-6.929796,-0.539401,6.940511,6.314890,-6.817190,1.038535,1.568618,-6.337451,-6.107821,-9.453446,-2.539866,4.282302,1.656869],[6.772037,5.637243,6.015222,2.669343,-2.375389,-3.580222,-0.814682,5.779710,-3.778692,-9.095815,-9.333381,9.137293,-4.751196],[6.691224,-1.842152,7.708332,-3.497384,-1.815338,-7.898111,2.790177,-8.193447,-8.394149,-9.267739,-7.154221,-2.127780,6.562629],[-8.389698,-1.943952,-1.378656,-4.508567,-7.734410,-9.321557,-3.897518,-5.788124,-4.059272,-6.294585,7.562786,-9.766744,-7.202832],[6.077521,8.733712,7.374242,8.046979,7.732908,7.522323,-8.513385,2.511519,-8.906179,-0.894113,-5.568040,-8.515214,9.462875]],[[0.256058,0.663433,4.610458,9.431623,2.792341,-6.278328,-8.936825,-8.001638,7.837793,9.829684,-1.923065,-3.815864,-0.181075],[2.853622,9.587705,-9.198810,-4.859052,4.149730,-6.429617,1.196422,0.918776,-6.251489,9.643983,-7.348772,-0.352436,5.983967],[2.544535,8.518053,-7.023185,2.247684,9.556683,-0.385651,7.088899,1.138395,-2.659070,-9.594376,-6.893326,7.425250,7.663132],[-8.079945,1.568709,-1.282572,-0.334458,-6.069133,2.268882,-9.984916,-3.790952,-9.837548,-7.276026,0.220213,-6.444226,1.664968],[1.273559,-3.661108,-8.685953,-8.591718,-6.196032,-7.279878,-9.592661,5.410041,-5.239545,-8.354524,8.694105,7.797751,1.792090],[-6.244074,-1.287593,-9.752569,9.142700,-0.561968,-8.515415,7.489894,-6.909890,5.764449,3.981943,-4.098385,-9.896449,-6.042906],[1.633624,-8.015767,-5.489606,3.555244,-3.091519,-8.523085,-2.315479,1.631099,6.740610,-1.352066,-5.842596,-0.489207,-2.434162],[-6.311637,-6.368080,-6.544972,-7.081628,-1.522127,-7.909893,2.313143,3.139027,-5.235187,-2.676224,-5.905882,-6.567890,9.809928],[-5.235603,-3.298426,-7.631257,-3.932802,5.346010,9.006465,7.416412,0.907018,9.522864,-4.288428,-9.988889,-3.299765,-9.177730],[4.290766,1.127767,1.605295,-1.312463,6.747254,-1.158468,1.984132,-2.152376,1.806703,-2.953789,0.931045,6.108364,3.484902],[-3.155191,8.693980,-1.978942,-8.224905,0.983173,-4.615454,8.935498,3.790831,8.234375,-5.152415,5.085869,6.681667,-4.897480]],[[4.980510,-1.266118,7.208036,-8.623616,3.192977,3.578566,1.747365,0.759310,8.263064,5.396278,2.639934,2.520868,-6.266105],[9.652531,6.471546,1.667597,-7.265166,3.975222,-6.979717,-9.286455,-0.641838,3.689077,-2.128836,9.650954,-8.461549,-4.500462],[6.376239,6.503430,-1.056027,9.975167,-0.582889,-1.344888,-4.855462,-9.234499,-8.113853,-7.079180,1.156254,-3.318793,0.035180],[7.997734,-5.682531,5.831183,6.716424,7.689857,7.183738,3.217490,1.585297,-4.711249,2.285375,4.455167,7.747414,1.919048],[6.748042,3.353531,4.576243,-0.880398,-9.762180,-6.292752,-4.637122,-0.206225,-4.165224,4.527654,5.702924,-5.082056,2.868186],[-6.251965,1.232944,7.444216,3.202846,5.400900,3.655557,-4.204230,7.364386,0.426840,8.811332,-8.463310,-3.838885,4.281941],[2.249173,-6.677852,0.723524,-9.558003,-5.029023,-6.012665,-7.500284,8.981876,7.722581,9.240791,-5.478265,7.258048,-3.278412],[6.203729,1.684828,5.396521,-8.822650,2.103989,-3.126141,5.289956,5.103259,0.965704,8.233702,7.130372,-6.851286,-7.898676],[-2.170932,-6.514048,3.186381,2.943562,6.931787,6.363973,-8.934119,1.195344,-9.837288,-4.040170,-5.177300,3.318850,-5.563520],[9.182607,-3.567805,8.836671,0.227180,1.102031,5.727680,2.642657,5.451210,7.034017,-7.419058,6.361310,2.845212,-5.667961],[7.191646,9.744941,4.200613,-8.975471,-0.491104,-0.105233,-9.804048,-7.675345,-9.027894,-9.616345,6.392639,1.371880,-5.362083]],[[-7.538556,-0.024717,-3.357688,1.163634,2.237072,-2.267447,-8.300504,9.220667,-5.052536,-4.764822,-7.005180,-1.429495,1.003184],[-6.230187,4.704787,0.048810,-1.293684,5.445625,4.883141,-9.159430,7.527981,-6.035876,-1.282149,-1.809707,9.579470,2.158826],[7.939843,-1.378718,7.404223,1.406014,-2.369423,2.583450,3.011811,2.953614,2.027698,8.120212,-5.840262,-8.750455,-8.167498],[1.984011,6.569010,8.383370,-6.718512,9.283006,-5.028600,8.016990,9.262989,9.482269,4.961777,2.509871,-3.091007,2.905288],[3.582539,7.154028,-6.494123,7.130028,-6.112593,-6.342716,8.390713,-2.699489,-5.931455,-7.174026,-6.938720,-3.448798,-2.682856],[-0.670223,0.225875,0.773818,1.236703,-3.180329,9.429430,-4.049414,-9.022146,-5.174408,-0.942067,6.637498,-9.524306,5.289541],[9.968385,-6.886038,8.564563,-4.130374,-2.002984,5.538723,8.321476,9.414962,-7.451967,-9.315673,-7.216148,-6.349666,5.083649],[-1.466695,4.473712,1.369238,8.214795,-8.662915,-4.823515,3.578742,-1.326191,4.867262,-8.722903,-3.618043,-0.954769,7.396181],[4.445053,0.521291,1.080106,5.314136,7.712014,1.117844,-8.281114,-8.708751,4.371844,-7.753150,-9.065558,7.675268,-6.578836],[2.838368,-6.307445,-2.792395,-5.346478,-7.282187,6.292085,-7.125876,-5.533312,6.201674,5.568209,-3.167034,-1.876078,-5.525920],[-8.182121,5.105998,7.278899,2.517993,-3.766322,-4.531066,4.846979,-1.610129,-0.351848,-8.692726,7.635854,0.964084,7.934906]],[[5.358012,-2.342798,-3.094166,3.747078,-5.031966,5.708181,-2.707498,3.804133,-2.242398,8.864579,9.746743,-9.776962,4.009857],[3.090316,-3.806276,-4.559916,-7.447550,-3.374362,7.407680,8.614992,-2.351797,2.605580,-9.987735,3.904008,7.165366,8.208694],[-0.243784,-7.415835,0.031041,5.224866,-9.794778,5.986446,-9.491165,-9.138465,6.101436,6.821604,-2.938497,-1.557653,0.002270],[9.556407,7.623668,6.746552,-7.856098,5.345392,-9.666627,-1.425269,-9.914959,4.797691,4.250922,-5.297760,2.248481,-1.068774],[-1.892132,-8.526879,7.940723,-7.395160,0.200010,-3.911426,-9.842940,7.932325,-1.390607,6.971079,-8.311804,-5.657600,-2.355031],[-5.200997,-3.458001,8.404771,-4.422762,9.390957,-1.294865,-1.543718,7.003041,5.011517,-0.790115,-4.491905,-9.529829,6.816045],[0.305516,-6.119307,-0.138390,1.734349,-8.366518,0.438194,2.775645,-8.170473,-4.865656,3.395242,4.788640,8.827368,6.613085],[5.874347,-8.158549,-5.779274,-9.795700,2.700952,-1.043503,3.190877,-3.259036,4.046016,3.476571,9.201872,-8.822843,-0.157525],[0.503325,3.308044,7.210076,7.422218,5.823098,0.074219,-6.337778,-5.686266,-0.597541,2.315177,-6.960359,-0.329042,-2.586826],[1.724681,-6.428920,9.735677,-6.925848,-9.196443,0.732064,1.785647,-5.323701,-4.124328,9.589537,7.479520,-3.982182,-4.918581],[2.176457,2.294376,-9.537289,-4.023705,-6.731786,9.223809,-5.820591,-7.011515,3.373320,-1.151135,0.850271,-3.192714,8.839523]],[[-5.762478,2.661872,-7.149036,5.079937,-9.817362,-2.180323,-2.539353,-0.893219,2.924819,2.217115,-9.877594,6.538108,-1.498733],[5.241686,-3.813425,-7.555028,7.282601,5.333328,-1.365116,0.408098,5.657215,1.253482,-9.605205,0.109652,-6.716949,2.589806],[6.071634,3.662858,7.221829,-8.797755,9.099157,-0.374570,-0.386020,-9.652013,-8.205626,-4.599176,-4.572898,2.264092,9.171580],[-2.641981,-9.216311,0.193317,2.163953,7.663531,7.987642,-9.198778,1.470024,1.519550,-4.677714,-9.567783,8.237227,-3.086583],[7.471853,-0.366982,-7.911768,-0.934701,9.537568,-2.293718,0.729274,0.541593,-0.724632,4.424914,6.251952,0.568959,3.607171],[-1.485718,-6.355936,-9.546910,8.196289,9.298863,9.610517,-2.366145,8.964587,9.963383,-5.208435,4.501145,-5.507144,-4.571652],[-6.397379,-9.400133,-0.662012,-8.146550,1.924351,-4.105441,-6.175323,1.155186,4.456537,-7.239992,-1.300331,8.033261,-5.832058],[2.924725,-1.690023,-4.321455,-7.212376,-2.995671,-4.596612,0.493215,4.400561,-0.664669,7.202729,4.597391,8.909529,9.164280],[-8.302920,-0.559674,-9.923374,6.807763,-8.500058,7.437178,-2.273292,8.078619,-2.450489,3.556603,-0.616489,9.463662,1.682849],[-5.340855,-3.539601,-6.826230,8.979729,-7.751920,0.625207,-2.720755,1.946768,-6.331681,9.956460,-0.464881,-0.967945,4.273585],[0.901651,4.075562,3.477895,8.382996,5.557165,-8.009365,5.895629,-2.228972,2.018398,-4.745579,-8.751900,-0.076019,-9.522820]],[[-7.352546,-6.934024,0.637518,-6.003327,-0.568046,-8.533034,-5.022623,-6.044158,-2.211548,3.051258,-1.348360,0.347670,5.197198],[8.420227,1.434608,4.419447,-2.685625,4.733030,8.214195,-1.462176,-2.076367,-2.945337,5.341882,1.242412,-6.420455,-7.398065],[2.512089,0.345594,-8.165436,4.976226,-3.078267,9.196598,-5.566419,-9.458976,-3.728420,-1.996319,7.632292,8.489210,7.539463],[2.904620,4.065127,-6.224622,7.917880,-0.406659,-0.638210,-5.260441,-0.351512,2.741074,-1.867768,-5.819889,6.671933,3.215270],[0.434895,6.377214,-1.100258,-6.437450,-7.862742,-4.369703,-9.034776,4.077774,-0.502847,4.240656,9.295761,-4.295323,-1.639476],[6.545085,5.735417,9.512730,5.989317,9.765824,4.019169,-9.024039,-4.246700,1.089251,3.854659,8.121245,-0.424427,-7.738829],[4.096302,-4.766520,1.724007,0.340399,-1.586059,-0.318889,2.142364,7.234820,0.358482,8.321079,5.095472,5.362852,2.093790],[-5.639934,7.681185,-8.955854,0.093325,2.298087,-3.059747,7.919052,0.061137,-5.056431,9.699481,5.512488,4.982505,-6.019880],[5.723780,0.837646,-4.649814,9.124020,-1.611956,4.399166,-2.872321,5.945806,6.009323,3.185773,-6.704720,-7.667205,-6.360709],[-4.942128,-0.117146,-7.293099,-3.222388,-0.668101,8.793485,7.234110,9.373433,-0.800074,8.059464,-9.847346,-6.657472,5.732626],[-0.446408,5.502928,1.399096,-7.445713,-2.068648,3.675538,1.447908,-3.894283,6.102203,-9.275314,-2.663857,-3.349225,-2.657659]],[[-7.849353,6.322091,3.799479,7.780363,-9.064111,4.675122,-2.676456,5.429459,-4.018243,-6.511049,2.543050,-4.521889,-7.429987],[-9.007184,-3.411399,-5.176971,-3.689388,-1.497319,7.958645,-6.127458,-6.915309,-5.975887,6.675103,5.930337,-5.456693,-2.526077],[6.569037,-5.113936,9.570881,9.154993,5.472670,0.681912,5.162097,-4.136499,1.001780,-9.479516,-6.741350,0.183866,-0.432615],[4.832562,-6.212763,-8.875681,8.621135,5.576722,-6.771417,-5.688705,-0.392245,8.193808,-6.238898,-6.449566,-8.563559,9.523340],[-1.090113,-4.165095,1.755515,6.153780,-9.550418,-3.565723,-3.661210,-9.006502,-9.660929,4.430475,-6.843616,-7.306963,-5.095845],[3.271712,6.255513,1.417742,4.173104,-9.757828,9.873501,-0.941913,7.272035,5.152563,-9.514538,-2.106640,9.094281,-7.955950],[-2.061411,-1.934027,5.454986,7.889894,-6.320802,-8.084951,2.187843,2.687048,1.118836,-8.017104,-0.219628,-1.956589,3.081514],[6.990467,-2.442971,6.938878,-8.460842,2.525169,7.355550,-7.820962,9.569123,0.426490,2.390761,-7.833285,-6.209510,2.949083],[-9.393373,4.621527,5.732370,-7.229338,-5.760437,-8.195327,4.906240,1.951033,0.203142,4.729629,-6.793896,6.016838,8.342380],[-9.713391,-3.171747,-9.124144,-4.642247,-3.963811,-0.947420,1.781198,-3.159693,4.523431,-4.336750,-3.909097,-0.524013,-6.295229],[-8.115670,-7.757935,9.239377,9.587029,-0.694115,8.967552,-8.744393,-7.065330,-8.173099,4.016212,-0.090323,5.413337,2.864049]]], dtype = "float32")#candidate|6573|(14, 11, 13)|const|float32
var_6574 = relay.var("var_6574", dtype = "float32", shape = (14, 11, 13))#candidate|6574|(14, 11, 13)|var|float32
bop_6575 = relay.divide(const_6573.astype('float32'), relay.reshape(var_6574.astype('float32'), relay.shape_of(const_6573))) # shape=(14, 11, 13)
const_6595 = relay.const([[[-6.758314,5.629619,-9.048078,-3.687223,2.811935,0.741608,4.001153,2.495037,8.286424,6.984364,9.930345,-3.051145,-9.343689],[-7.604736,-7.808892,5.022536,-1.384127,-3.732159,-5.221653,-4.601618,-7.601062,-7.110936,-8.326558,-0.521979,-7.470690,9.926149],[-7.873668,-2.580264,1.796318,8.571538,-3.083316,-2.757034,8.736471,5.084099,8.449877,-9.113984,2.806568,-5.680491,-5.095410],[5.448525,-7.313024,5.486659,9.047044,4.343132,-9.275302,-9.279673,3.694001,1.397000,-8.051297,0.812355,-2.434327,3.272658],[-2.534276,-1.603757,-1.054995,1.296012,-4.703054,-0.253126,-3.451129,-3.154666,-2.057297,-6.854839,4.772355,9.549119,-9.675109],[-3.182059,-7.626619,8.176154,3.834377,6.965936,1.176501,-4.989108,7.286844,0.130484,7.313431,-1.869463,7.205874,1.016048],[-9.684671,-4.032947,4.694206,-2.175860,-0.328183,-8.063365,0.765267,-0.623242,7.625356,-4.292083,2.486835,-8.881293,6.553817],[-2.191285,8.703419,4.777550,-9.893208,4.671115,-0.341789,3.418560,7.614522,-9.532313,-6.443511,6.567122,-4.184021,-3.583372],[-6.857263,-4.379308,-0.919827,-9.362658,-7.716902,8.890304,2.527540,2.339492,-9.947273,-7.443697,-9.041784,-3.798322,2.035090],[-5.168346,1.992385,8.675408,-7.447206,2.652605,1.797720,-6.034150,-1.441741,-0.205361,-7.022822,5.941537,9.532254,-1.613509],[2.699598,-4.895386,7.874799,-2.060159,0.198729,-1.259834,9.917566,-6.795054,8.123135,-4.418987,6.183823,0.330975,-2.087872]],[[-2.479087,-7.505927,-1.139413,-3.666542,6.478056,2.671952,-2.290927,4.044257,-4.649729,5.573005,1.028106,-1.457592,-0.972432],[3.708524,2.263931,-5.113945,4.240867,2.491154,-7.592114,-9.326546,0.020928,6.371884,-2.989621,-9.437457,4.928071,-0.474799],[-1.646361,9.986699,-3.554759,-1.665827,-4.897593,9.120831,3.613490,9.046083,-5.690928,4.971022,-2.193641,-1.133983,-1.102283],[3.181506,-7.988369,-7.083421,-5.511395,5.105635,-6.565750,4.628445,-4.775948,-3.326586,8.569727,-1.526377,8.969726,3.576183],[-1.538048,4.290330,-7.911737,6.480370,-6.291646,1.643794,5.731017,6.599008,-4.927578,-5.169114,1.584592,-8.185977,3.107001],[1.861606,7.248947,-5.291701,-3.831445,-9.599728,-7.673452,6.020839,3.733638,-3.143293,0.313256,1.137364,-6.160066,-2.141896],[-7.674981,-6.156730,7.289590,8.382814,-2.381225,3.294998,1.687217,3.186695,9.736817,-9.830394,7.897522,7.096998,-7.726068],[-9.496747,-9.094949,-3.900230,3.845069,-4.888205,-1.262474,0.337183,0.471449,8.971417,-9.002646,4.113796,9.195236,3.687505],[-9.762092,1.999042,2.596448,2.342171,4.311652,-3.795419,-1.939053,7.957177,-7.057657,0.328651,3.788588,-7.345923,7.716705],[5.410250,3.100011,0.483520,4.731012,-0.137242,-4.289476,1.369582,-1.968986,-3.480710,-9.653471,6.907492,3.508595,1.724749],[-5.988096,-2.164542,0.415555,-6.417181,-4.747699,-4.480376,9.643552,-9.026736,-5.782628,8.283786,-0.309543,2.150114,4.872135]],[[7.642622,6.565530,-2.957827,8.712261,9.343972,-3.307526,2.389893,5.403323,3.668589,6.084392,-5.543311,1.025806,-3.686691],[3.214495,-3.902134,-6.961330,7.030483,-2.195583,4.156129,3.968618,-7.475053,5.178440,-6.770278,8.221541,1.999355,-1.319683],[-5.319328,9.756353,9.557051,-8.582682,3.476883,4.165533,-7.749301,-3.322398,9.939119,-8.149753,-1.704949,-1.071783,-1.464931],[-3.527284,-3.810458,6.068068,-6.065529,5.315481,-7.085087,7.712835,-5.394034,-4.534471,5.108992,1.873589,-3.331730,-0.817380],[3.430951,-8.451639,4.188144,8.701249,5.557293,-1.987171,1.945033,0.874734,-0.198396,9.966016,3.877436,7.376947,4.248095],[-4.069094,5.919590,-0.105093,3.246123,-4.790826,9.579961,-4.931312,5.619530,-9.477783,-2.853448,-4.808084,-8.005095,3.695583],[1.290178,-6.130413,2.040140,2.835637,-0.436166,3.059919,-2.720826,-1.725682,6.622314,-4.852392,8.989928,9.175471,-8.026126],[-0.474372,-0.816813,-4.862594,5.284947,-1.397655,9.475572,4.496211,8.741640,5.554689,-1.939894,8.560193,-8.173558,-3.524587],[-7.809715,6.681970,4.721005,0.159335,-0.925147,-2.750395,4.087353,-0.247099,-2.569057,-2.590515,1.902315,8.026595,8.662269],[2.262702,-9.324399,6.366815,-3.667732,0.641943,1.832148,0.953121,-1.174817,1.390943,-7.219515,7.824070,4.787907,-7.976424],[9.841505,-9.950146,-1.091968,8.189820,-9.978478,3.675411,5.800145,-1.115082,9.154155,-8.794614,8.168025,4.440710,-5.236044]],[[-2.206456,-5.974971,-2.717189,-0.712876,-1.262535,-7.608204,1.058041,8.582558,6.915305,5.932774,9.543050,0.357834,3.250376],[5.135051,-1.237040,0.672113,1.687944,1.272939,5.852218,-0.697240,-1.966306,3.825137,8.585055,-7.849110,-0.475019,7.900159],[4.200704,1.061981,7.062929,7.933133,-6.420924,5.443959,7.437232,9.020046,-7.657100,-9.385273,5.965664,4.383369,-5.182239],[0.167915,2.122935,-5.505373,-5.160238,7.647599,-2.445681,2.951635,4.419343,-0.619644,-4.563129,-5.551156,-9.157124,9.112261],[-1.726374,-5.146253,4.569843,7.192224,-1.015476,5.070652,-6.092340,8.972462,0.861314,1.276970,0.238719,7.694607,-5.827641],[-9.568745,4.944967,-9.712641,-6.256493,-2.211787,-4.408378,4.089280,-3.083706,2.647864,5.158634,2.338359,-5.183249,-5.081501],[7.437346,1.350694,8.637958,-8.125598,8.450419,-5.311743,0.245741,2.118490,1.020998,4.347952,1.442679,-7.973771,1.581199],[-0.508599,-4.130611,0.213265,-7.353982,7.662771,-5.157779,-3.456717,-2.621498,-5.430705,-7.426907,-6.934459,-3.421275,2.569339],[-1.980030,-1.478898,1.699107,9.317831,3.515654,0.991488,7.514581,4.188830,-9.117081,-3.879107,2.278793,0.848920,-0.377073],[5.460710,6.986946,6.310072,-8.439219,8.929759,-5.639204,3.626330,8.463376,0.332764,-2.596333,-2.951933,1.171546,6.121175],[0.162256,-2.147793,-9.657613,-6.805042,-3.322548,-6.958998,-0.577947,-2.627164,-1.815133,-0.648652,0.664405,3.458952,2.412536]],[[-7.008287,-6.161940,9.607521,-2.248539,5.486375,6.460448,-4.605482,7.908213,-9.414523,-1.227411,-7.383712,-1.353359,-2.913657],[2.460247,3.980253,-4.615016,8.292944,-8.254550,-6.803041,-2.097854,4.253065,-3.168835,8.435335,-0.401518,0.901139,-2.294411],[-5.735782,-1.967756,-3.141577,-8.418098,-3.203305,-2.454924,7.784057,-1.869321,5.815274,1.594173,-4.682719,0.007260,-3.058717],[1.674052,-8.323028,3.305152,6.126984,-5.783124,8.028323,5.024009,3.844706,5.800049,-4.095270,-5.753774,-8.355037,9.617337],[0.390230,-9.539573,-5.119670,3.844324,-5.597241,5.221210,5.732772,8.016491,-5.659917,-6.258966,-6.653041,-2.038690,-1.564966],[3.568922,7.140287,0.383930,5.319750,-9.974370,-5.781289,-2.616224,-4.344946,-5.581744,8.556036,3.103557,-5.413037,7.045401],[8.243304,-7.007745,5.612169,3.323583,-7.277352,0.636568,-6.856979,6.955555,-5.590850,6.081462,-0.529316,-0.871953,-0.486854],[0.574800,4.347358,1.649593,4.702023,-0.586772,7.006136,5.232731,7.093245,7.534435,-0.497659,-5.934088,9.897254,6.494671],[1.959238,2.068942,0.120329,-2.973074,-7.502624,-8.779616,1.704492,-3.189338,-1.397126,-6.864050,-6.269873,6.258620,3.008905],[1.003467,-0.890667,-7.381976,-4.875053,3.076789,-1.662856,5.343942,0.736001,-1.709180,-9.033263,-7.803214,-6.803014,-0.473582],[-2.298879,1.726651,4.562084,-3.639360,-8.736592,4.062700,0.607964,-2.606733,5.050086,-0.562971,8.729177,4.061012,8.607712]],[[-5.577439,3.729511,-7.598738,7.853784,9.610750,0.196537,-2.663142,-0.529492,-0.555418,-2.286862,3.286061,-5.925017,-0.915207],[1.222081,-5.629099,2.592517,-7.107191,7.203687,5.105470,9.961826,-1.915259,-1.901666,-9.066751,-7.273331,-3.634366,1.672889],[-2.165978,8.824724,-7.886124,7.817595,2.449749,8.851338,9.663260,8.808255,2.331435,1.809990,0.654789,-4.727295,-0.006718],[-7.052513,3.877497,-1.258427,-7.184078,3.855292,-3.971061,6.380131,0.602634,-3.965343,8.377133,1.704606,-9.996774,-7.742623],[3.492735,8.512702,-1.397486,-4.804965,7.066720,4.270828,6.802722,-3.424637,5.993260,8.179586,5.206066,2.582048,4.551943],[6.520587,8.576054,9.361617,8.702988,-0.789659,7.938417,7.242400,-2.199025,-2.950544,7.925525,2.195263,-1.662463,-3.386416],[-4.078956,-8.114525,-8.036138,9.075690,-3.392716,-7.081767,8.583005,2.060943,-8.849272,-1.674641,9.560733,-6.230408,2.656864],[-2.526067,-8.760753,4.713612,-7.751220,1.145339,-4.863686,6.719142,9.404797,-1.736316,-1.227106,2.980775,-7.915925,4.075688],[-1.386178,1.794239,-5.694903,3.617974,-2.907707,8.892410,1.459697,4.424335,-0.725556,-0.916521,0.658748,-6.281167,-6.298270],[-8.593908,1.593055,-4.252823,3.106605,-7.788881,2.156630,-2.654605,-0.605923,0.426697,-5.904545,1.770464,5.590030,8.252356],[-5.008268,-1.922283,9.398397,-6.839651,5.437837,0.063433,-7.781807,-3.123067,5.726876,5.800372,-8.172964,0.497080,1.505770]],[[3.682361,-9.055694,4.191446,2.294566,6.428580,-6.792465,3.023233,9.172356,-0.981564,-6.451889,2.973546,-7.121734,-1.204371],[6.157447,9.307398,-4.922393,4.167142,3.464179,-8.349084,1.902914,-5.323051,8.367821,6.209717,-7.081609,-7.577481,-3.540605],[-8.427247,-5.619585,4.954683,5.768030,-9.702189,-5.271547,-1.680166,3.760869,-2.893651,3.855384,-3.441514,-2.552261,1.863453],[-8.517259,-1.192481,1.540107,3.209210,9.255738,-1.725588,9.536415,-6.503575,-4.622366,-6.538538,1.478003,-2.258070,8.603889],[4.449812,-0.442295,-5.808453,-4.247462,2.434649,4.644174,0.424502,-8.704417,3.541407,3.174663,3.805434,1.818588,2.831688],[-3.449294,9.794136,-9.380616,0.189371,8.411414,0.883181,-2.018053,6.979579,1.382354,-2.300853,-2.410647,-0.450411,-9.100764],[-0.706193,3.835440,-5.402767,0.340751,5.632112,5.914332,8.470558,-7.085384,-5.567473,4.116627,-6.197538,8.975723,-9.783270],[2.551470,8.196854,-4.863743,6.297290,9.943709,4.493832,1.369379,-1.671518,-1.334910,9.280148,9.887658,7.812695,2.924266],[4.572954,3.762001,8.270317,-0.345000,-5.344122,-2.928290,-3.450190,7.551984,-8.234449,-3.131593,7.050454,-0.316693,0.036764],[8.726223,7.038282,6.607517,0.270690,-1.331505,6.985537,4.279789,-8.266903,2.497870,4.322104,-0.322918,5.811991,-9.179655],[3.196204,9.227234,-9.606794,-8.945560,4.069426,6.557901,-6.899061,4.467251,-4.044488,7.609916,-6.301330,-8.672302,5.976403]],[[-4.239290,8.821981,-7.712275,4.621869,-2.296450,-5.142268,1.403714,-0.679202,-9.133094,4.741763,-3.087239,-2.606217,-2.601544],[-4.379612,-0.935721,5.393900,-4.233100,4.356899,-2.787358,-0.498835,7.286689,3.609558,-2.937019,9.452952,-0.332608,6.413954],[-7.983220,-8.993218,-5.751711,0.750619,-4.092792,4.457148,-4.970428,5.244883,-9.437632,4.986677,-8.091333,-7.069661,-8.028011],[5.023683,-7.959331,1.636201,-5.680503,4.557752,-8.239680,3.142177,-3.364114,2.571819,-3.885685,9.353500,-0.486592,-7.963780],[5.341403,7.365222,-7.872924,-4.023025,2.431859,3.764152,1.746651,0.216768,-7.848394,-6.708113,0.600444,5.895136,5.259599],[-2.275566,2.673878,-2.115933,-5.970728,-4.224455,1.407934,3.731587,-3.694629,-6.734507,-7.631653,3.180464,8.602617,8.585763],[8.488865,-8.675419,0.331566,-0.279130,0.205185,2.296805,-4.557831,-2.290723,-4.040689,0.368887,-2.620039,-7.141503,5.753573],[3.141633,2.261803,1.865082,7.525466,2.404219,6.810188,0.578464,3.267060,-0.250640,-2.532717,4.596474,-0.487803,3.297993],[-9.610041,9.447797,0.034434,-0.129262,2.610299,5.940815,5.227072,6.884086,-9.053439,9.618871,3.798990,-1.680187,-1.754095],[-7.493973,-8.512178,-3.169677,3.495199,-8.046424,-3.638744,-9.294698,-2.414624,7.799909,-3.250979,-8.234408,5.601728,-4.885605],[1.463293,6.558546,-4.313391,8.527922,8.592207,-6.149947,7.843856,-2.881085,1.840818,-1.014869,-4.769248,-5.182722,-1.038115]],[[-1.846954,-6.302116,5.406767,8.885208,-5.179652,-2.667246,-3.844970,9.670702,7.067739,7.350174,-0.787247,-9.106447,-3.165911],[-6.382955,6.126579,-6.169604,8.207966,0.068173,-0.083602,4.423012,-7.170576,-5.774084,8.400497,2.820008,7.119172,-2.183156],[-2.108491,-1.095436,-5.326730,6.606833,5.612226,4.330739,-8.023986,6.873916,1.892047,2.330943,4.176727,-9.141626,6.467301],[2.160404,-1.295511,6.819961,-9.374379,1.298019,-0.247105,-4.244527,-5.016515,-0.073086,-8.082691,-8.474204,-6.632581,-9.005441],[5.060136,3.552176,-7.497047,3.666315,-9.934301,2.841457,-0.375489,1.514410,1.213045,7.824701,0.494285,1.487636,9.602612],[2.734493,5.563215,5.312826,-5.647582,-1.989188,4.954422,0.446743,-9.216862,-3.382406,-8.692826,5.902335,-5.239269,8.150698],[0.326287,8.452077,-3.637230,-6.772914,-4.572694,3.227317,-8.960747,-5.573498,3.207319,-7.047984,-3.458561,7.101141,-4.335857],[7.909944,0.012878,2.646336,3.468055,3.410453,1.605798,3.512655,-0.361388,3.258037,-8.476399,-8.407466,2.261423,1.221269],[-5.005769,-3.257902,-1.630466,8.080355,6.263829,-9.568183,6.125994,-0.739475,4.576183,1.886870,-3.669498,5.828256,-5.992584],[6.648438,-6.108768,0.734115,2.695851,6.807023,3.200784,5.826653,5.698051,3.434209,9.750934,-0.434332,-2.215307,-4.907650],[-3.489968,2.952404,-8.155465,-3.100181,-3.873159,7.470008,-0.714839,1.546551,5.757550,-6.270723,-0.137132,7.261818,5.393170]],[[-7.048130,0.373116,0.104699,-7.027421,-1.298018,5.238054,5.667463,3.625039,4.228848,-1.933938,1.548057,2.710480,-9.459952],[-2.431425,4.424885,1.728498,9.862335,5.796781,-5.769353,1.709766,-6.835422,-6.190387,-1.638108,-7.138415,3.537616,-7.373622],[-3.291461,-8.498824,4.853594,-1.899038,-2.767015,3.079905,4.100224,-6.971668,-8.112495,-2.621780,-4.200125,4.665476,-8.555508],[-6.246552,-1.228281,8.062510,-4.133541,4.981524,-6.619746,0.467780,-3.164463,-8.433333,4.344873,5.785201,-1.055903,-2.793604],[-3.933794,-1.113146,0.840346,-8.292731,1.397265,-2.235557,6.932809,-8.267700,1.035631,1.293065,-5.802782,8.438209,-9.980139],[8.777978,8.894067,-8.549466,0.179766,-7.031191,9.828476,-4.351131,-2.335619,2.631477,7.589394,0.606915,4.478302,-1.042687],[-2.991853,5.334555,-0.310971,-2.035037,-0.460792,-1.556342,1.174521,-7.232599,7.586128,0.574247,5.476648,-4.564560,-5.297030],[6.265860,-0.736950,1.621110,-9.739007,9.289343,-5.639475,-3.471617,-2.860255,-7.356047,8.405160,7.474226,-6.688420,0.218835],[6.536192,-5.177069,3.372444,9.533301,8.244121,4.709576,8.931395,-6.815563,-8.280167,-5.273203,5.040308,-6.622297,7.774716],[-6.736652,-3.527380,0.192935,6.070480,-2.364707,7.796244,-0.960175,-3.731792,-3.559822,-0.740706,3.370778,8.414989,-8.840044],[4.306203,-9.615094,-3.563133,-8.740498,-9.527320,-6.277240,4.837232,-3.094504,-9.372422,3.143786,-3.529575,-4.773283,-3.117365]],[[9.711580,3.484255,9.168536,-5.249797,8.406864,-3.084656,-7.563276,2.971525,-0.047807,7.356696,2.128504,8.848096,-1.758423],[8.929097,-5.989738,6.030389,7.135051,5.030109,1.317313,-6.041687,-7.689277,-6.366322,8.655126,8.361506,-1.043102,4.737129],[-5.979949,-3.461222,-0.207712,1.017747,0.201377,2.609116,3.659371,3.264982,-9.936586,5.195920,-0.541083,9.592457,1.164993],[2.813044,9.813345,-7.106023,6.772071,8.339660,-4.795926,8.586922,6.351273,-3.742417,5.107228,5.040048,-2.070352,1.432338],[-2.079001,-1.722402,9.111032,7.684556,-1.144234,3.190024,-1.899963,-1.628400,0.430117,-4.681461,-5.930504,-4.659030,6.623542],[8.761102,-6.625473,-9.615848,-6.852381,9.328091,2.180326,-3.898300,-6.627040,9.303557,-2.369674,2.885127,5.309926,-1.188272],[-1.715047,-9.926632,-9.444405,0.149803,-3.648139,4.549014,4.021756,-8.346192,8.071807,-7.915873,-1.354218,-4.430466,1.295607],[4.592996,-9.568815,-1.588176,-4.717716,-4.392776,1.043737,0.996491,8.651686,-7.056081,6.592342,3.870721,5.922925,-4.619292],[-4.740449,8.279606,-1.269660,-2.824239,-7.852035,-0.542992,0.609076,-9.208989,-5.679008,-2.029587,-3.972975,-2.289961,-8.329015],[2.483569,-1.860376,3.210148,-5.868285,-0.722633,0.712843,3.931792,-7.318147,-2.903814,-0.618595,-1.036930,2.413902,8.368177],[0.369758,0.473984,1.996444,3.195825,1.773315,-2.163584,4.969790,-8.603510,-5.831482,2.185868,6.845430,-2.983098,-6.511444]],[[4.254215,-9.146903,8.414605,-5.256591,2.140558,8.816811,4.142969,2.924850,1.628867,0.486871,-2.754174,4.205164,-9.931855],[8.442350,4.292733,3.794686,9.125999,4.526639,4.162493,-2.347845,3.767852,1.129788,-2.913133,8.262717,-8.931198,7.761773],[-0.538131,-5.853416,-4.705510,9.803622,4.094205,-0.233234,-9.949195,9.646166,0.991280,-6.840173,-6.490570,-1.736020,1.872339],[-8.690637,-1.700516,-9.946667,-2.935228,6.284005,-6.777486,-7.520683,8.172740,3.224446,-9.140637,0.233110,-6.224856,9.816679],[4.054998,2.196172,5.073281,-4.555530,5.351951,-3.366982,7.817029,-1.721260,-0.914360,2.042323,4.104801,-9.988213,-4.697153],[-6.059184,4.641184,7.888609,6.107617,7.784229,-6.301567,-9.267087,-2.732892,6.768771,-8.448115,-9.795848,5.032919,-5.490996],[-6.945732,-3.290617,-9.952176,7.054162,-8.012776,-6.495891,3.529837,-8.618182,-9.513749,7.231215,4.826115,-6.988244,7.283960],[6.484831,2.980535,7.084372,-3.811957,-9.684811,-9.224185,-2.559225,-2.221086,-2.173475,2.335439,6.853399,3.879816,-9.241524],[4.962911,-4.371441,2.985450,8.257134,9.919558,-7.021926,5.539938,-8.515146,-1.170476,-4.708538,-6.134670,-3.093602,-9.957322],[9.899132,2.134509,-7.565884,-2.182200,3.652629,-5.974667,-8.514697,3.897269,7.759743,9.592164,5.088659,1.986706,-5.627548],[-5.705891,8.855472,-5.226908,8.782988,-0.128503,5.146588,-3.441027,7.531654,2.840884,1.935371,-8.827694,4.706063,-4.457652]],[[-2.864594,3.417402,8.263825,9.397895,-6.621913,3.705425,1.290723,2.035720,7.400119,4.665991,9.191989,-6.095153,-5.872553],[1.009176,1.469764,-2.841740,5.665120,-8.102206,4.588454,9.628606,-9.943365,2.294143,9.557205,-8.568726,9.342672,5.949192],[-0.637340,0.625712,-8.900000,4.154258,-2.695553,3.411440,8.054280,9.488807,-1.424143,-3.536426,7.173467,-9.533198,-5.621646],[8.557627,2.827235,-4.134897,3.126083,-0.940014,9.597679,6.395638,7.860861,7.050577,-9.252931,3.701701,-1.929861,6.489085],[-7.633804,-4.715681,-2.408357,-6.648128,-5.358733,-9.871203,-0.243002,7.803083,-4.821927,8.379106,-0.625409,-7.542516,1.018210],[7.745894,3.236834,-8.385551,-1.470539,-2.436825,-3.480296,-3.355344,-0.494760,-3.994915,9.417265,-8.668747,-8.213056,4.266645],[-8.170203,-5.614378,-9.667936,0.689112,-5.216757,0.831482,-7.289408,-0.965922,-0.137131,4.740404,8.032408,0.458243,-4.565487],[-1.576334,3.773150,2.218462,8.229773,-4.033411,7.220466,6.677296,7.033448,-4.477148,-6.583638,-8.888292,-0.412772,3.642414],[-1.355477,-3.703642,-5.034346,9.640905,0.245883,-9.826023,-3.959002,-1.515479,-6.098497,-1.320844,-0.257868,-6.783879,9.969927],[0.914758,-1.040208,7.271579,6.245727,7.711092,-4.893204,7.974936,1.604481,-1.871243,-3.695711,5.767761,-3.231607,-0.250950],[2.505064,6.825657,-9.142388,-9.859919,-0.922468,4.895287,7.463159,6.543873,7.114386,1.864906,-0.422658,8.903882,-4.305859]],[[-0.020936,-5.278629,4.744444,2.269268,-4.725240,7.325524,-6.548853,-0.729204,9.822021,8.688368,9.519667,-7.882038,8.669641],[-6.161137,0.998343,-1.307473,7.175839,0.939600,-8.233256,9.109876,-5.286993,8.510363,-2.888481,-4.592261,8.257433,9.997093],[-1.620299,-2.623824,-5.736208,-8.298362,7.370943,0.990339,1.373852,-7.200785,7.627920,-1.841894,-3.585241,4.207371,0.373113],[3.741864,5.622498,9.711560,-6.872325,2.673749,-9.443755,-3.964989,-2.650084,-5.637370,-1.026938,4.112830,5.171713,7.754124],[3.240496,-0.441498,-0.901387,-6.292854,-5.768403,-1.511624,4.659117,-7.385191,6.430794,1.671527,-5.906568,-7.093492,-0.660626],[6.892940,8.439870,-8.829619,9.229176,-8.350475,-3.200230,6.816098,-9.419883,1.186307,9.557141,-6.996966,-8.908965,6.927138],[4.131359,-6.237949,1.626644,0.100804,-9.841972,-0.730099,7.315808,-0.050857,7.071702,-8.516422,1.149416,5.294552,0.448324],[8.369644,2.392841,5.547076,-6.926691,3.467206,7.649338,3.608837,-5.378609,6.689780,-7.481904,9.829762,9.936872,5.945326],[9.710988,5.089236,-6.604031,-2.517183,0.407070,4.643512,1.210262,-7.770445,8.247702,9.433080,3.889222,2.071056,-4.215115],[2.411565,7.323071,-6.979667,3.218323,8.872389,-0.305591,3.531690,7.728483,-6.215227,9.043628,4.159894,-9.956160,-1.829503],[9.646446,9.889278,-1.680687,4.878915,9.201190,-5.505624,-0.420344,2.173147,-6.963670,-1.315278,5.234289,-9.721142,7.071639]]], dtype = "float32")#candidate|6595|(14, 11, 13)|const|float32
bop_6596 = relay.mod(const_6573.astype('float64'), relay.reshape(const_6595.astype('float64'), relay.shape_of(const_6573))) # shape=(14, 11, 13)
var_6602 = relay.var("var_6602", dtype = "float32", shape = (14, 11, 13))#candidate|6602|(14, 11, 13)|var|float32
bop_6603 = relay.logical_or(var_6574.astype('bool'), relay.reshape(var_6602.astype('bool'), relay.shape_of(var_6574))) # shape=(14, 11, 13)
func_1397_call = mod.get_global_var('func_1397')
func_1398_call = mutated_mod.get_global_var('func_1398')
call_6614 = relay.TupleGetItem(func_1397_call(), 0)
call_6615 = relay.TupleGetItem(func_1398_call(), 0)
output = relay.Tuple([bop_6575,bop_6596,bop_6603,call_6614,])
output2 = relay.Tuple([bop_6575,bop_6596,bop_6603,call_6615,])
func_6617 = relay.Function([var_6574,var_6602,], output)
mod['func_6617'] = func_6617
mod = relay.transform.InferType()(mod)
mutated_mod['func_6617'] = func_6617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6617_call = mutated_mod.get_global_var('func_6617')
var_6619 = relay.var("var_6619", dtype = "float32", shape = (14, 11, 13))#candidate|6619|(14, 11, 13)|var|float32
var_6620 = relay.var("var_6620", dtype = "float32", shape = (14, 11, 13))#candidate|6620|(14, 11, 13)|var|float32
call_6618 = func_6617_call(var_6619,var_6620,)
output = call_6618
func_6621 = relay.Function([var_6619,var_6620,], output)
mutated_mod['func_6621'] = func_6621
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5667_call = mod.get_global_var('func_5667')
func_5668_call = mutated_mod.get_global_var('func_5668')
call_6642 = relay.TupleGetItem(func_5667_call(), 0)
call_6643 = relay.TupleGetItem(func_5668_call(), 0)
output = relay.Tuple([call_6642,])
output2 = relay.Tuple([call_6643,])
func_6658 = relay.Function([], output)
mod['func_6658'] = func_6658
mod = relay.transform.InferType()(mod)
output = func_6658()
func_6659 = relay.Function([], output)
mutated_mod['func_6659'] = func_6659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6047_call = mod.get_global_var('func_6047')
func_6048_call = mutated_mod.get_global_var('func_6048')
call_6697 = func_6047_call()
call_6698 = func_6047_call()
func_3676_call = mod.get_global_var('func_3676')
func_3677_call = mutated_mod.get_global_var('func_3677')
call_6699 = relay.TupleGetItem(func_3676_call(), 0)
call_6700 = relay.TupleGetItem(func_3677_call(), 0)
uop_6717 = relay.asin(call_6697.astype('float64')) # shape=(21, 5)
uop_6719 = relay.asin(call_6698.astype('float64')) # shape=(21, 5)
output = relay.Tuple([call_6699,uop_6717,])
output2 = relay.Tuple([call_6700,uop_6719,])
func_6720 = relay.Function([], output)
mod['func_6720'] = func_6720
mod = relay.transform.InferType()(mod)
mutated_mod['func_6720'] = func_6720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6720_call = mutated_mod.get_global_var('func_6720')
call_6721 = func_6720_call()
output = call_6721
func_6722 = relay.Function([], output)
mutated_mod['func_6722'] = func_6722
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6761 = relay.var("var_6761", dtype = "float64", shape = (1, 12, 6))#candidate|6761|(1, 12, 6)|var|float64
uop_6762 = relay.atan(var_6761.astype('float64')) # shape=(1, 12, 6)
output = relay.Tuple([uop_6762,])
output2 = relay.Tuple([uop_6762,])
func_6764 = relay.Function([var_6761,], output)
mod['func_6764'] = func_6764
mod = relay.transform.InferType()(mod)
mutated_mod['func_6764'] = func_6764
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6765 = relay.var("var_6765", dtype = "float64", shape = (1, 12, 6))#candidate|6765|(1, 12, 6)|var|float64
func_6764_call = mutated_mod.get_global_var('func_6764')
call_6766 = func_6764_call(var_6765)
output = call_6766
func_6767 = relay.Function([var_6765], output)
mutated_mod['func_6767'] = func_6767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4822_call = mod.get_global_var('func_4822')
func_4823_call = mutated_mod.get_global_var('func_4823')
call_6849 = func_4822_call()
call_6850 = func_4822_call()
output = call_6849
output2 = call_6850
func_6856 = relay.Function([], output)
mod['func_6856'] = func_6856
mod = relay.transform.InferType()(mod)
mutated_mod['func_6856'] = func_6856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6856_call = mutated_mod.get_global_var('func_6856')
call_6857 = func_6856_call()
output = call_6857
func_6858 = relay.Function([], output)
mutated_mod['func_6858'] = func_6858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5296_call = mod.get_global_var('func_5296')
func_5297_call = mutated_mod.get_global_var('func_5297')
call_6866 = relay.TupleGetItem(func_5296_call(), 4)
call_6867 = relay.TupleGetItem(func_5297_call(), 4)
output = call_6866
output2 = call_6867
func_6881 = relay.Function([], output)
mod['func_6881'] = func_6881
mod = relay.transform.InferType()(mod)
mutated_mod['func_6881'] = func_6881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6881_call = mutated_mod.get_global_var('func_6881')
call_6882 = func_6881_call()
output = call_6882
func_6883 = relay.Function([], output)
mutated_mod['func_6883'] = func_6883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1648_call = mod.get_global_var('func_1648')
func_1650_call = mutated_mod.get_global_var('func_1650')
call_6920 = func_1648_call()
call_6921 = func_1648_call()
uop_6922 = relay.erf(call_6920.astype('float64')) # shape=(2, 9, 9)
uop_6924 = relay.erf(call_6921.astype('float64')) # shape=(2, 9, 9)
output = uop_6922
output2 = uop_6924
func_6926 = relay.Function([], output)
mod['func_6926'] = func_6926
mod = relay.transform.InferType()(mod)
output = func_6926()
func_6927 = relay.Function([], output)
mutated_mod['func_6927'] = func_6927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5734_call = mod.get_global_var('func_5734')
func_5736_call = mutated_mod.get_global_var('func_5736')
call_6963 = relay.TupleGetItem(func_5734_call(), 0)
call_6964 = relay.TupleGetItem(func_5736_call(), 0)
func_3758_call = mod.get_global_var('func_3758')
func_3760_call = mutated_mod.get_global_var('func_3760')
call_6978 = func_3758_call()
call_6979 = func_3758_call()
output = relay.Tuple([call_6963,call_6978,])
output2 = relay.Tuple([call_6964,call_6979,])
func_7002 = relay.Function([], output)
mod['func_7002'] = func_7002
mod = relay.transform.InferType()(mod)
mutated_mod['func_7002'] = func_7002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7002_call = mutated_mod.get_global_var('func_7002')
call_7003 = func_7002_call()
output = call_7003
func_7004 = relay.Function([], output)
mutated_mod['func_7004'] = func_7004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6546_call = mod.get_global_var('func_6546')
func_6548_call = mutated_mod.get_global_var('func_6548')
call_7008 = relay.TupleGetItem(func_6546_call(), 0)
call_7009 = relay.TupleGetItem(func_6548_call(), 0)
output = call_7008
output2 = call_7009
func_7016 = relay.Function([], output)
mod['func_7016'] = func_7016
mod = relay.transform.InferType()(mod)
mutated_mod['func_7016'] = func_7016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7016_call = mutated_mod.get_global_var('func_7016')
call_7017 = func_7016_call()
output = call_7017
func_7018 = relay.Function([], output)
mutated_mod['func_7018'] = func_7018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7016_call = mod.get_global_var('func_7016')
func_7018_call = mutated_mod.get_global_var('func_7018')
call_7021 = func_7016_call()
call_7022 = func_7016_call()
var_7032 = relay.var("var_7032", dtype = "float32", shape = (7, 7, 2))#candidate|7032|(7, 7, 2)|var|float32
bop_7033 = relay.bitwise_or(call_7021.astype('uint32'), relay.reshape(var_7032.astype('uint32'), relay.shape_of(call_7021))) # shape=(7, 7, 2)
bop_7036 = relay.bitwise_or(call_7022.astype('uint32'), relay.reshape(var_7032.astype('uint32'), relay.shape_of(call_7022))) # shape=(7, 7, 2)
output = bop_7033
output2 = bop_7036
func_7044 = relay.Function([var_7032,], output)
mod['func_7044'] = func_7044
mod = relay.transform.InferType()(mod)
var_7045 = relay.var("var_7045", dtype = "float32", shape = (7, 7, 2))#candidate|7045|(7, 7, 2)|var|float32
output = func_7044(var_7045)
func_7046 = relay.Function([var_7045], output)
mutated_mod['func_7046'] = func_7046
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7060 = relay.const([[[-3,-5,5,-3,-2,-1,-9],[3,-8,-6,-2,9,-6,5]],[[3,-1,5,7,9,-2,-2],[9,3,-9,7,-1,-4,-2]],[[-3,4,-3,4,2,-1,-3],[1,5,-9,2,-3,-5,7]],[[-7,2,8,-7,2,10,-5],[4,-1,5,6,6,4,-6]],[[-4,-10,4,2,-9,-2,10],[-4,10,-3,4,-8,-4,8]],[[-4,8,-1,-10,10,6,10],[-2,-9,-5,6,-1,8,3]],[[-6,3,-7,-9,-9,3,2],[1,-9,-2,9,9,-7,-8]],[[-10,8,-1,-7,2,-9,6],[4,-3,-1,8,-3,1,2]],[[10,5,-10,7,4,2,-1],[-8,-6,6,7,-4,-1,2]],[[6,-1,6,10,9,-9,-3],[-10,5,3,10,1,-9,2]],[[1,-1,10,5,10,-3,-5],[3,-5,-6,10,-10,-1,10]]], dtype = "int16")#candidate|7060|(11, 2, 7)|const|int16
var_7061 = relay.var("var_7061", dtype = "int16", shape = (11, 2, 7))#candidate|7061|(11, 2, 7)|var|int16
bop_7062 = relay.bitwise_and(const_7060.astype('int16'), relay.reshape(var_7061.astype('int16'), relay.shape_of(const_7060))) # shape=(11, 2, 7)
output = bop_7062
output2 = bop_7062
func_7065 = relay.Function([var_7061,], output)
mod['func_7065'] = func_7065
mod = relay.transform.InferType()(mod)
var_7066 = relay.var("var_7066", dtype = "int16", shape = (11, 2, 7))#candidate|7066|(11, 2, 7)|var|int16
output = func_7065(var_7066)
func_7067 = relay.Function([var_7066], output)
mutated_mod['func_7067'] = func_7067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4456_call = mod.get_global_var('func_4456')
func_4457_call = mutated_mod.get_global_var('func_4457')
call_7097 = func_4456_call()
call_7098 = func_4456_call()
output = call_7097
output2 = call_7098
func_7113 = relay.Function([], output)
mod['func_7113'] = func_7113
mod = relay.transform.InferType()(mod)
mutated_mod['func_7113'] = func_7113
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7113_call = mutated_mod.get_global_var('func_7113')
call_7114 = func_7113_call()
output = call_7114
func_7115 = relay.Function([], output)
mutated_mod['func_7115'] = func_7115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6068_call = mod.get_global_var('func_6068')
func_6070_call = mutated_mod.get_global_var('func_6070')
call_7190 = relay.TupleGetItem(func_6068_call(), 0)
call_7191 = relay.TupleGetItem(func_6070_call(), 0)
func_6047_call = mod.get_global_var('func_6047')
func_6048_call = mutated_mod.get_global_var('func_6048')
call_7196 = func_6047_call()
call_7197 = func_6047_call()
uop_7217 = relay.atanh(call_7196.astype('float32')) # shape=(21, 5)
uop_7219 = relay.atanh(call_7197.astype('float32')) # shape=(21, 5)
uop_7220 = relay.sigmoid(uop_7217.astype('float64')) # shape=(21, 5)
uop_7222 = relay.sigmoid(uop_7219.astype('float64')) # shape=(21, 5)
output = relay.Tuple([call_7190,uop_7220,])
output2 = relay.Tuple([call_7191,uop_7222,])
func_7225 = relay.Function([], output)
mod['func_7225'] = func_7225
mod = relay.transform.InferType()(mod)
mutated_mod['func_7225'] = func_7225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7225_call = mutated_mod.get_global_var('func_7225')
call_7226 = func_7225_call()
output = call_7226
func_7227 = relay.Function([], output)
mutated_mod['func_7227'] = func_7227
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5785_call = mod.get_global_var('func_5785')
func_5786_call = mutated_mod.get_global_var('func_5786')
call_7231 = relay.TupleGetItem(func_5785_call(), 0)
call_7232 = relay.TupleGetItem(func_5786_call(), 0)
func_2320_call = mod.get_global_var('func_2320')
func_2322_call = mutated_mod.get_global_var('func_2322')
call_7237 = func_2320_call()
call_7238 = func_2320_call()
func_3381_call = mod.get_global_var('func_3381')
func_3383_call = mutated_mod.get_global_var('func_3383')
call_7267 = relay.TupleGetItem(func_3381_call(), 0)
call_7268 = relay.TupleGetItem(func_3383_call(), 0)
output = relay.Tuple([call_7231,call_7237,call_7267,])
output2 = relay.Tuple([call_7232,call_7238,call_7268,])
func_7269 = relay.Function([], output)
mod['func_7269'] = func_7269
mod = relay.transform.InferType()(mod)
mutated_mod['func_7269'] = func_7269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7269_call = mutated_mod.get_global_var('func_7269')
call_7270 = func_7269_call()
output = call_7270
func_7271 = relay.Function([], output)
mutated_mod['func_7271'] = func_7271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5296_call = mod.get_global_var('func_5296')
func_5297_call = mutated_mod.get_global_var('func_5297')
call_7300 = relay.TupleGetItem(func_5296_call(), 1)
call_7301 = relay.TupleGetItem(func_5297_call(), 1)
func_5958_call = mod.get_global_var('func_5958')
func_5961_call = mutated_mod.get_global_var('func_5961')
const_7310 = relay.const([-2.137452,-2.151258,-2.310177,8.404708,0.599255,4.541327,-3.584294,9.197651,9.465748,-7.843164,4.370732,8.147924,-6.905192,8.974763,9.573522,-1.455614,-1.737010,-0.555360,3.742234,6.591016,-9.261649,5.934699,9.832904,-7.539619,3.321050,-4.075987,-0.410657,-8.061896,0.203159,-6.808221,-0.844354,6.613486,-0.868927,-6.969009,2.561020,-1.585057,-3.791576,-0.442882,-0.076958,-4.126724,-9.701635,-9.331913,4.780878,9.836918,-3.368259,0.148463,-8.867325,-0.796238,-2.584322,-8.803543,-6.812702,2.832855,-7.407129,-1.203398,-6.615967,7.587530,4.695714,2.128042,-3.127213,-3.584429,5.932839,3.105334,-5.350451,-9.796418,-4.272536,-6.522603,3.099944,0.664081,9.853227,-9.701962,9.274845,-7.466172,2.047004,9.022770,-1.691776,-9.376391,2.347695,4.475030,4.315031,-8.949449,1.726753,1.693087,-8.190236,-1.934089,-9.718900,1.993146,-5.102945,3.236520,-6.720562,8.799678,-0.952344,-8.890394,-2.629739,6.491806,7.212410,7.532997,-9.920116,3.171855,-6.880091,-0.771323,-7.590271,-6.252226,-5.661531,-6.176138,-2.743925], dtype = "float64")#candidate|7310|(105,)|const|float64
call_7309 = relay.TupleGetItem(func_5958_call(relay.reshape(const_7310.astype('float64'), [21, 5])), 0)
call_7311 = relay.TupleGetItem(func_5961_call(relay.reshape(const_7310.astype('float64'), [21, 5])), 0)
output = relay.Tuple([call_7300,call_7309,const_7310,])
output2 = relay.Tuple([call_7301,call_7311,const_7310,])
func_7320 = relay.Function([], output)
mod['func_7320'] = func_7320
mod = relay.transform.InferType()(mod)
mutated_mod['func_7320'] = func_7320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7320_call = mutated_mod.get_global_var('func_7320')
call_7321 = func_7320_call()
output = call_7321
func_7322 = relay.Function([], output)
mutated_mod['func_7322'] = func_7322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2857_call = mod.get_global_var('func_2857')
func_2859_call = mutated_mod.get_global_var('func_2859')
call_7323 = func_2857_call()
call_7324 = func_2857_call()
uop_7325 = relay.rsqrt(call_7323.astype('float32')) # shape=(2, 9, 9)
uop_7327 = relay.rsqrt(call_7324.astype('float32')) # shape=(2, 9, 9)
func_7065_call = mod.get_global_var('func_7065')
func_7067_call = mutated_mod.get_global_var('func_7067')
const_7335 = relay.const([4,-8,-10,8,-9,-9,8,-2,2,-5,-1,6,10,-2,8,4,5,-4,5,6,1,-2,1,-4,-10,-4,2,10,-7,-1,-10,-7,-7,2,3,9,3,-10,7,-7,-5,-8,2,-10,-2,4,-6,-1,-3,8,-10,9,10,8,-5,4,10,8,-2,3,-1,-8,-9,1,-1,-8,-10,6,6,9,1,-5,5,-2,-4,-3,-1,2,-1,2,6,4,-4,-5,-4,-6,-8,-3,4,2,-10,3,-9,3,-1,-1,-2,-2,5,1,-2,4,9,4,5,-3,2,-8,4,10,-6,-2,-6,-9,2,2,-8,-3,-6,-10,3,-7,1,8,9,-9,-7,-5,5,-5,5,-2,-4,10,2,-10,-5,-1,-2,-2,-7,6,-3,-8,-7,7,2,7,-4,7,-8,4,4,2], dtype = "int16")#candidate|7335|(154,)|const|int16
call_7334 = func_7065_call(relay.reshape(const_7335.astype('int16'), [11, 2, 7]))
call_7336 = func_7065_call(relay.reshape(const_7335.astype('int16'), [11, 2, 7]))
output = relay.Tuple([uop_7325,call_7334,const_7335,])
output2 = relay.Tuple([uop_7327,call_7336,const_7335,])
func_7339 = relay.Function([], output)
mod['func_7339'] = func_7339
mod = relay.transform.InferType()(mod)
mutated_mod['func_7339'] = func_7339
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7339_call = mutated_mod.get_global_var('func_7339')
call_7340 = func_7339_call()
output = call_7340
func_7341 = relay.Function([], output)
mutated_mod['func_7341'] = func_7341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6881_call = mod.get_global_var('func_6881')
func_6883_call = mutated_mod.get_global_var('func_6883')
call_7383 = func_6881_call()
call_7384 = func_6881_call()
output = call_7383
output2 = call_7384
func_7387 = relay.Function([], output)
mod['func_7387'] = func_7387
mod = relay.transform.InferType()(mod)
output = func_7387()
func_7388 = relay.Function([], output)
mutated_mod['func_7388'] = func_7388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4168_call = mod.get_global_var('func_4168')
func_4169_call = mutated_mod.get_global_var('func_4169')
call_7516 = relay.TupleGetItem(func_4168_call(), 0)
call_7517 = relay.TupleGetItem(func_4169_call(), 0)
output = relay.Tuple([call_7516,])
output2 = relay.Tuple([call_7517,])
func_7518 = relay.Function([], output)
mod['func_7518'] = func_7518
mod = relay.transform.InferType()(mod)
output = func_7518()
func_7519 = relay.Function([], output)
mutated_mod['func_7519'] = func_7519
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7540 = relay.var("var_7540", dtype = "float64", shape = (15, 6, 10))#candidate|7540|(15, 6, 10)|var|float64
const_7541 = relay.const([[[3.952752,-8.229549,9.563638,-3.475072,-7.069574,6.457730,-4.110801,-8.574967,-0.439556,6.708297],[4.071960,-0.212235,0.333488,0.715981,0.604412,-8.400254,-3.648507,-7.801656,7.071016,-7.716068],[-2.160425,-5.995292,-1.364035,-7.161819,-4.886926,4.410124,-9.627481,8.191344,9.448170,-3.354915],[-9.558398,2.595357,2.691109,-9.181502,-4.250917,6.375420,-4.315930,-3.948317,-6.279176,5.818749],[-9.789971,-9.749345,-8.664599,-0.250527,8.308995,0.101600,3.360663,-8.723657,-8.552908,9.268826],[-7.283921,5.060672,-1.596812,8.415525,-6.245583,-7.374095,0.410691,0.535679,-9.494401,6.327275]],[[-9.162085,5.307069,-4.218538,-7.269661,-8.784474,0.067814,-5.075375,9.777210,-3.023511,-2.048074],[-1.459849,7.110585,7.879299,4.807813,0.117796,3.306097,6.436007,2.239267,4.386530,-5.988684],[-8.147363,-4.346410,-2.085942,3.862406,-9.063094,8.573396,-0.503424,-3.983673,2.075953,-2.512506],[9.273528,-9.247551,-7.376054,-6.244973,-8.650048,-4.670954,-5.868002,3.923935,-3.509461,-2.323723],[-1.182711,5.418221,-7.255851,5.000372,-2.870579,-5.706801,5.742591,-5.550543,9.700689,3.281691],[-0.452029,-1.988605,-4.752043,8.814960,-7.070613,4.484210,-1.212490,-1.070758,8.278233,-0.819091]],[[9.369678,0.254751,-1.019934,-5.591142,-2.168086,9.307391,6.403978,9.564632,4.067879,8.068744],[-1.230478,2.196239,6.280329,-0.553987,6.485511,-5.408209,9.775405,8.416750,-1.855762,6.683286],[-4.363655,8.253443,-3.466441,2.192581,0.909657,-1.720907,-4.412772,-5.003678,1.138505,-8.801498],[-4.182341,4.495144,-7.313178,9.945761,-7.599318,0.375516,4.978733,8.529969,5.388719,8.906056],[6.195861,6.059457,8.606347,0.438631,-1.841414,0.740226,7.520255,-9.076473,-2.808767,-4.267178],[7.792141,7.865333,-6.486539,-5.426621,5.619233,-6.381954,6.389107,-0.026948,-7.457334,3.141165]],[[2.445085,7.510158,6.752800,-0.208676,6.764580,4.434480,-0.377104,2.085863,8.605370,0.946997],[3.342853,8.821506,6.244209,-4.259360,7.705495,-7.693106,-0.355485,4.327851,7.534162,5.815393],[-4.038251,8.453057,9.581920,9.222039,1.883498,-9.334188,4.719957,1.789394,3.354550,-4.773670],[-9.295642,-7.034506,-5.589700,-4.580653,3.099003,-4.427149,-1.527103,7.043392,-1.238207,-6.999443],[4.541131,-7.132978,-0.791602,3.881873,2.745267,8.884892,-7.983902,5.314759,6.991884,-6.900776],[5.227569,8.567841,4.241133,-8.063617,8.229645,6.865916,1.613757,6.420170,8.373900,2.546721]],[[-4.749954,-3.076036,-2.964470,6.814669,-6.792882,8.890897,-1.025814,3.424839,8.279491,0.346854],[8.317858,5.346838,9.002682,-5.991380,5.899107,5.594630,-7.338752,-5.508826,9.907385,8.433756],[2.505517,-3.575047,8.531176,9.533749,2.128720,5.454314,7.195531,9.716837,-2.068012,-2.188751],[7.196222,5.999230,0.645013,1.488307,-2.582361,-7.710588,5.119017,9.998679,1.232710,7.115738],[-8.601242,2.724580,0.084303,-8.374379,-2.479559,0.904404,-5.147717,-9.181502,-3.064393,3.056515],[-0.465940,-2.229342,-7.728194,-3.305200,0.593423,-7.275491,-8.016230,3.693706,-8.176920,0.782759]],[[-4.421080,-7.539113,-4.755386,5.261070,-1.706990,3.428840,-6.781036,-1.893547,7.780981,-0.140753],[-8.579283,-5.050703,-9.229839,-4.638576,7.208351,-9.106030,-3.109126,3.168378,4.856725,1.873302],[8.647126,-3.348852,4.719498,-0.754161,7.247507,2.915981,0.958597,-4.124501,0.064735,-8.619493],[0.318204,7.951216,8.506046,-7.701736,3.332227,2.741940,-6.419963,-7.777983,-3.560666,-0.361796],[-5.171240,-1.672000,-7.476284,0.947724,6.732868,-0.735096,-1.649256,8.011692,-2.695171,-7.783250],[4.069477,-6.602422,9.523339,7.541987,8.151026,5.545856,5.539904,4.453219,6.918090,-5.330092]],[[-8.645764,1.671754,-5.105483,4.590898,-7.529321,-8.169065,8.142882,4.715669,1.188164,-7.986479],[-5.018305,-4.955368,7.749641,4.223811,5.371658,-0.610771,6.484303,-0.216322,-2.181117,-2.537153],[-5.499054,-3.804047,-0.418336,-2.123145,6.853062,-6.879106,2.929308,7.941504,8.266335,5.738241],[-7.913132,-3.543179,4.263771,1.422129,-9.827047,-8.873832,-2.371608,-5.623455,-7.226642,1.053352],[-3.440242,7.430081,-6.377788,-6.006683,-5.421835,-5.677299,4.487252,-6.977655,-3.148223,-8.244100],[1.750328,6.118285,-8.725981,-4.285733,-9.069187,-7.407333,-3.389867,-8.072247,-0.967502,-0.097935]],[[-8.844876,-8.745234,6.545802,-8.788512,-3.982302,2.071864,1.534957,-1.904116,-2.764538,-8.745305],[-1.707470,4.116747,2.585741,4.317799,9.537726,-5.884974,8.871585,5.774725,3.657609,-2.529790],[6.575337,9.714176,-1.929463,-3.615692,1.609469,4.030435,5.927167,-4.967596,4.975111,-6.851713],[3.619033,-7.672896,6.842627,8.710987,-2.248735,1.304994,2.255225,-8.468651,-1.137726,3.714107],[-3.354197,8.053019,1.213676,-3.333738,5.663927,0.772075,3.669009,3.048839,-9.316389,7.563331],[-1.277709,-4.258955,6.336521,0.920685,9.678871,5.239338,-8.779249,6.989061,-1.156401,-5.095514]],[[-1.355534,-2.118397,0.313915,5.768159,4.051350,-1.885150,6.674150,5.357408,-3.197915,-5.830947],[6.142814,7.841264,-8.882221,-7.004066,-9.324681,-6.627556,-0.054741,-0.496283,5.372201,7.711030],[-1.100200,-6.095744,-9.557196,-6.075015,8.574984,-4.665178,9.840465,-1.925465,-8.648527,-4.641175],[1.027817,-0.631780,-3.488280,6.409294,-5.192673,-1.400162,6.036007,-8.434477,-1.510081,-3.995601],[6.601264,2.981118,-7.575648,-2.632401,-2.559409,5.754005,9.275855,6.786379,-6.136196,4.560121],[-8.523016,0.572877,9.328865,5.359850,-3.545847,4.398156,0.283668,-1.536182,-8.300780,-8.489456]],[[-8.812450,-0.819612,1.660416,7.672167,-4.236576,-0.455475,-2.839107,-4.868107,0.899902,1.728890],[8.082732,8.445609,2.892875,-1.040698,-9.253490,-3.807191,-3.575080,4.259061,6.129690,4.538614],[5.374166,-8.477417,9.408688,7.546648,-8.839815,8.941425,3.795378,-6.996011,-3.684606,-6.038066],[-9.309916,0.220451,9.640988,-2.080796,2.149298,0.835758,-5.076565,-9.520009,-0.100456,-0.944277],[7.498715,6.278713,1.091307,3.191180,-3.615165,-2.289949,8.588660,-0.925173,-3.549965,4.081084],[-6.504243,1.756492,-3.853795,7.379429,6.665254,5.084499,1.176391,-1.076918,6.684755,-8.989299]],[[0.433167,-0.974484,7.249671,-7.725825,1.848519,2.685055,-7.510338,-7.384853,9.006342,0.142280],[-1.039039,0.858992,6.047277,-1.802579,0.253218,5.338117,6.966931,0.020709,-0.737802,7.972314],[9.039131,3.031999,6.695124,-8.732913,6.034391,6.151065,4.071577,0.437499,-6.796831,9.261642],[0.454961,7.205973,-3.191166,6.796470,-9.952972,-1.506075,8.158136,7.067868,-7.706699,3.406703],[4.091456,9.553036,8.571040,-5.251413,-1.595986,-3.711535,-5.734734,-4.016008,-5.700157,0.049933],[-8.265929,7.788004,8.945980,-3.924658,-1.861317,-9.829707,3.555151,-0.395579,-1.610533,-0.045806]],[[-8.308278,-5.245719,-4.187200,4.496270,-9.272323,4.339141,3.047058,9.128801,3.386997,-0.130555],[8.237848,-9.674066,-1.609511,-7.855547,2.719948,4.230688,6.347246,-1.298035,-8.855689,-4.647822],[-4.415961,-4.706436,-4.978776,-3.192518,1.642815,-3.887560,2.067252,5.631142,9.743178,6.154340],[7.256900,0.216254,-1.824409,-3.804035,0.460487,-8.914636,8.218701,6.812933,-1.243911,3.313860],[-0.519662,-9.806301,-1.369892,7.102149,4.601875,-8.207336,5.430059,1.556475,7.602135,2.633994],[7.597834,-9.300372,-0.677507,-9.064146,-1.537213,-8.837893,4.131320,-6.548137,3.142804,-8.779928]],[[-1.996802,2.929993,-7.492908,-7.523040,-7.643343,-8.960837,3.936903,-0.739246,5.910935,-7.937892],[3.708778,-8.177978,1.445408,-9.339314,0.847238,-4.468399,-9.414189,5.306430,-1.986157,-0.607306],[1.017954,-8.085809,-3.013652,-0.979461,-4.859865,1.562342,-3.884980,-0.631137,-6.387341,-4.246399],[7.770236,-4.426234,-1.807290,-2.693637,9.592349,6.753483,-4.891206,1.954123,5.348173,-9.707277],[-4.045839,0.762144,1.234118,-8.145233,-6.737159,3.984309,2.966030,1.120219,-7.641254,5.090387],[4.382519,-2.432531,-5.097707,-3.139599,-7.320701,7.348582,-6.166502,3.864683,8.370739,8.689735]],[[-2.391759,2.424970,-0.430935,6.535454,8.196228,-4.847495,4.071109,-6.848674,-0.692324,2.285916],[7.402514,4.615354,2.031964,9.877198,8.609593,1.874616,-0.914150,2.789307,8.704418,6.312041],[2.725737,2.703035,-4.517840,3.943732,-6.491824,8.264771,6.155462,1.468668,7.273415,0.914885],[-8.548852,-6.495412,-6.183874,0.039996,-0.669106,-6.482183,3.108773,7.662406,5.384930,-6.602204],[5.744977,1.435485,0.671263,-4.680592,6.110509,2.103410,-3.743789,-2.226307,5.018044,-6.284787],[-4.243550,-4.221247,9.998187,-3.881751,-2.256102,-9.667646,-0.742611,-4.072466,8.551239,4.197588]],[[5.542508,-5.030389,-9.536964,-9.703902,-2.031243,-6.705826,8.422017,-6.308661,-7.610766,9.998281],[-9.669796,-1.059183,3.308660,-3.276098,6.023680,3.171442,-7.580131,-3.393078,8.608795,-0.344513],[-8.360071,-8.192291,3.099874,-2.469350,1.628334,-0.786134,6.015821,6.915055,-3.091765,6.648036],[4.990582,-3.256963,-2.172399,-9.961650,9.907289,-9.258460,1.321990,2.134091,0.394520,-9.469566],[1.034598,-3.182235,-7.114377,5.630475,0.774516,-1.177193,3.635084,-4.506845,-5.501175,0.602153],[-9.997152,4.465791,5.294176,-7.826520,-0.830180,7.802721,-3.183126,-3.507965,8.102305,7.037176]]], dtype = "float64")#candidate|7541|(15, 6, 10)|const|float64
bop_7542 = relay.floor_mod(var_7540.astype('float64'), relay.reshape(const_7541.astype('float64'), relay.shape_of(var_7540))) # shape=(15, 6, 10)
var_7546 = relay.var("var_7546", dtype = "float64", shape = (15, 6, 10))#candidate|7546|(15, 6, 10)|var|float64
bop_7547 = relay.power(var_7540.astype('float64'), relay.reshape(var_7546.astype('float64'), relay.shape_of(var_7540))) # shape=(15, 6, 10)
func_6479_call = mod.get_global_var('func_6479')
func_6481_call = mutated_mod.get_global_var('func_6481')
call_7569 = relay.TupleGetItem(func_6479_call(), 0)
call_7570 = relay.TupleGetItem(func_6481_call(), 0)
func_4456_call = mod.get_global_var('func_4456')
func_4457_call = mutated_mod.get_global_var('func_4457')
call_7586 = func_4456_call()
call_7587 = func_4456_call()
bop_7589 = relay.left_shift(var_7546.astype('uint16'), relay.reshape(const_7541.astype('uint16'), relay.shape_of(var_7546))) # shape=(15, 6, 10)
const_7600 = relay.const([[[-2.542469,6.434128,-3.586718,-5.846721,-6.518233,-1.023896,-5.600603,7.508597,-2.409661,-1.399363],[1.260614,3.745367,-0.162271,-7.536834,8.765155,-3.060972,-0.958872,-8.081492,4.719613,-1.405332],[4.173921,-2.137051,8.384616,2.198835,7.154155,-2.414667,-5.424939,8.585404,-3.725201,9.626762],[-3.594116,-6.829958,4.462027,8.676224,7.750222,-9.123099,-2.725045,-1.770131,-1.102668,-6.532047],[-3.638254,7.363588,-2.276740,5.786169,-3.111951,-0.482101,-6.491304,0.969692,5.291052,-4.476328],[8.004524,-0.384748,8.842565,6.430014,-2.056873,-6.479563,-4.666081,6.305874,-4.238434,0.886036]],[[-6.273743,5.339829,-9.717918,-9.507114,-8.179370,1.877076,-9.670285,9.190208,-5.893586,2.151186],[-1.793864,4.933343,4.496306,2.131172,3.849073,7.051611,-0.736846,-6.195166,9.008888,6.619850],[-5.722189,5.680808,-7.613846,-9.595035,3.107539,6.357232,6.094985,-9.104641,-6.087675,4.545235],[0.312505,5.827707,7.047922,-7.237090,-9.014861,-1.241426,-6.354644,3.039147,4.412445,-8.318432],[-0.243276,-2.513529,-5.062781,-4.202574,1.713724,9.814349,-4.681615,-6.094436,-1.230580,0.753482],[-5.322153,7.548237,8.757994,1.132085,6.366954,-9.843543,-9.596301,6.430688,5.264107,7.955343]],[[7.931108,2.135815,6.025898,-9.694931,6.034038,-4.981602,7.371890,-6.058848,1.222392,5.404376],[0.476950,-2.191586,8.910306,5.374046,3.399920,4.083311,3.147766,8.599034,-4.161206,-2.618649],[2.611909,-5.966298,3.378951,7.183655,-1.526086,4.908881,-5.364779,3.552584,2.286553,6.738020],[2.667007,-8.957051,2.162851,5.820499,0.480881,3.896183,0.884762,5.950951,7.373268,0.259346],[-2.866029,3.150796,-7.767422,-4.085578,3.171325,-5.631417,-1.626195,3.434134,-6.559306,0.707631],[5.526773,-0.061923,-3.647828,0.328630,6.832210,-2.137346,8.838803,-7.509010,-1.739355,6.555292]],[[-0.949170,3.771672,-1.493157,5.993731,8.015702,-1.596236,0.086404,0.813782,8.281155,5.309706],[5.907316,-9.394609,-1.579560,-1.955680,4.642605,-4.874317,-1.650533,-7.894906,9.249375,5.195862],[-3.907480,9.440972,6.018326,-4.429973,5.121191,5.177057,4.264508,7.241353,-2.515672,-8.277951],[2.320360,-5.596263,-2.838847,5.088675,-7.803075,7.470808,-4.966054,-5.002461,9.998695,-7.715279],[2.653647,-5.419043,7.975275,-4.319070,3.970520,2.425511,3.926120,-9.725752,-5.909572,0.514158],[6.848033,-3.787528,9.450661,8.387700,7.458935,2.928054,5.745646,7.606232,8.899423,-6.390452]],[[-2.381472,-8.429104,5.300929,-2.788458,-6.085762,-8.860614,-1.502806,7.059400,-1.822040,-4.222959],[2.797302,-8.883277,9.440592,6.197658,5.291011,-0.293195,-9.347400,9.744786,9.365999,8.990498],[-6.628571,0.912162,-4.538782,-7.364638,6.189788,-3.614687,3.692311,8.399276,-1.279733,4.639878],[2.262389,-8.271913,-6.122843,6.724215,5.925630,3.956389,8.299887,-6.284553,-8.617204,-3.952279],[3.424466,-4.516918,0.014033,-1.366007,-5.298877,0.181808,1.916787,2.539356,1.625677,4.663205],[-1.840610,-0.760065,-7.802705,7.688240,-4.050440,-8.779433,0.383556,-9.086119,8.022127,-9.863742]],[[-6.355549,8.049245,6.719347,-3.562148,3.539902,4.580932,-9.705991,5.984785,-4.093217,1.015411],[-9.500914,7.611998,-8.441815,-2.370942,-2.307761,-4.714069,-9.888488,-8.594057,-3.667742,6.115050],[-2.805318,0.400119,-6.280154,2.665869,-9.122359,7.414675,0.572302,-1.557300,-6.793089,1.539090],[9.437330,-1.779543,2.366475,-1.981624,6.181879,4.831838,-5.174276,-9.560491,-3.378724,-2.812636],[4.940207,6.976460,-3.699462,-8.321418,6.124599,5.232409,9.369715,-4.190249,-2.352946,8.013890],[-5.432239,5.302936,4.984598,-4.376528,-9.551872,-8.149423,-5.444542,-7.864223,2.295619,-1.817292]],[[-6.554425,-7.354170,7.697077,-8.833344,8.761550,6.875222,-7.499422,-3.626067,-8.398051,4.905121],[2.577500,-3.704603,-1.561629,-5.076908,-4.565978,-7.434343,-6.110235,-0.295170,8.634233,9.145555],[-1.881623,7.030702,-4.925492,1.754297,-3.064040,3.239823,-9.847086,8.469902,-1.941381,6.109286],[-7.247554,2.342577,-1.964731,-1.066561,-0.587412,-5.779037,-2.383393,6.552591,1.843318,-7.109091],[-5.229976,-5.576641,6.958990,8.521453,6.947629,-1.829537,-1.089378,7.560410,-8.636425,-4.712628],[6.088784,1.162395,-6.000464,-2.265769,2.107871,1.583656,-2.686197,9.102462,-6.722049,7.399595]],[[7.137511,9.988378,2.434708,-6.804505,1.797241,-4.106045,3.764372,-4.663062,8.323303,5.056223],[3.059332,-9.860232,-5.076895,-0.915311,-3.330920,6.688907,9.707844,2.510940,6.230782,-7.478506],[-3.652341,7.460167,1.152630,-3.112649,3.055159,8.324704,-6.011516,-9.923342,9.829665,9.812252],[7.843451,6.961159,-2.081363,2.164849,-9.779362,-7.043200,8.405123,-2.453695,0.343677,4.830060],[7.797637,-9.622076,-8.051360,-2.725920,3.277443,6.691914,-9.293750,4.502110,0.195218,-2.404202],[3.778437,-4.849163,8.901586,9.632112,8.953254,8.729276,2.022813,2.979615,-1.971798,-7.712284]],[[9.366232,-1.445471,-5.239022,-6.161836,6.258056,-9.125953,4.033431,7.853195,1.909365,-9.793212],[5.242265,5.415528,3.483591,-8.012453,7.627953,7.531789,-4.637848,-6.418781,6.259704,-8.521680],[-0.727325,6.949051,0.724432,-7.485684,4.126525,-6.354902,-8.261585,-8.382106,-2.461982,5.192708],[3.633207,-8.313842,6.910459,-6.700336,-5.510299,7.269518,3.485544,-6.820189,1.113678,-1.627192],[5.673618,9.409665,-6.740863,0.924420,-5.999790,-2.435968,3.441289,1.675660,-8.047801,-0.906046],[-3.713810,6.567465,-4.743111,-8.651417,-9.677369,3.087489,2.953589,4.720741,-3.561283,-8.299876]],[[9.482566,-4.398263,-7.337096,3.547578,0.125596,0.840190,4.097704,-3.867007,-7.564645,9.375531],[4.947068,0.838393,4.896269,-0.575918,6.468639,-3.825476,-8.992303,-2.994497,-6.912056,7.425873],[7.194693,3.124146,7.343647,-7.202018,6.491838,-5.097938,-1.314616,2.113007,-9.257343,9.433354],[4.552534,-2.562235,-3.965586,-4.224219,5.934820,0.264249,-2.324556,7.836528,-6.528120,6.254973],[-5.832294,-5.167820,4.962739,-2.622770,4.112045,-1.549751,-6.804063,-4.551022,1.467131,9.873352],[-5.147826,0.294366,-4.286860,-2.353875,-1.524785,-8.754575,1.962562,-6.977990,-3.063756,-2.773421]],[[-7.911585,-5.843753,-7.105762,-6.380768,2.875037,-6.685945,-0.055145,-2.700730,-6.279979,5.373067],[9.285620,3.443348,-4.506094,9.749773,9.315598,-4.917189,-8.389728,-2.261254,-0.534009,-0.988230],[-7.496966,8.539597,-5.135191,0.089360,2.574682,-1.169469,-4.375088,8.815595,1.604536,-7.841476],[7.591386,-8.930564,1.508235,-6.081110,0.781664,-4.344749,0.881422,-7.959884,1.599491,-9.914327],[-7.115664,0.276803,0.569542,6.135118,-0.249310,4.198913,8.196676,1.197995,-6.107069,-7.139327],[8.161140,8.837945,-2.479553,-3.600993,-6.043077,-2.115234,8.931944,2.102882,1.586986,7.575302]],[[-9.588894,1.400827,8.728632,1.265171,-8.053602,7.269586,-7.118887,-4.042026,3.791377,-3.411819],[0.485537,-9.661263,7.540242,3.155336,2.389775,-6.244232,9.909709,3.229907,-0.265143,-0.737945],[-7.930625,-9.088439,2.664411,3.014055,-6.905840,-1.449272,8.438732,-1.906377,-7.883480,9.765329],[9.894971,-0.225350,2.244771,7.251249,-7.603641,-6.209972,5.939381,6.572014,7.635583,9.323341],[-6.285196,2.607146,5.235175,-1.568552,-7.327607,2.769326,0.207151,-4.757969,2.450038,8.263211],[-1.028627,-6.134586,-8.636842,-9.831325,-4.044855,5.135856,7.108842,-9.773606,6.659868,-3.764577]],[[-2.806294,2.922474,1.835147,-9.522126,9.679092,-9.557996,7.513117,8.602427,-2.557473,7.133816],[-8.952288,-2.873561,-2.050439,-6.530558,8.314807,3.946935,-3.515510,-9.344047,-9.162606,-3.683145],[-6.063310,3.631597,7.771020,2.846400,-2.340942,-2.244410,-4.259213,-3.433961,-6.921092,-9.528691],[-7.093124,5.578900,-4.107593,-1.425718,5.989952,-3.667892,-2.510381,9.217059,-4.933642,5.790080],[-7.128781,9.376280,-8.884216,1.268056,-4.408947,8.049114,2.963242,9.420504,-6.162709,-8.814813],[-3.114935,3.071933,3.693185,-0.507699,5.888634,-4.203123,-3.791762,-4.726764,-2.715407,8.281105]],[[9.023589,1.318929,5.525824,-5.676862,-1.683082,9.039768,9.735085,4.068434,-8.767258,5.372944],[-0.282238,7.850841,8.251864,4.831204,7.431277,9.742279,4.235245,3.455491,9.056928,-7.197566],[-0.298090,7.792252,-7.278801,-7.095451,-9.555722,8.166501,-5.337403,6.248627,-7.460884,7.527418],[8.027029,6.721823,4.528889,-6.228998,-0.276310,-6.255701,-3.963764,5.853062,9.160743,4.410035],[3.571689,-6.648336,3.660623,5.079167,-5.967948,4.259264,4.707006,1.443620,5.716144,-1.333906],[-4.935704,2.537096,-5.055479,-3.350819,-7.297318,3.477478,-2.932336,5.097682,-5.648349,9.735734]],[[0.048539,-8.431707,1.977136,9.607490,6.415241,9.461466,4.330602,1.310033,3.539553,0.395380],[7.626732,3.582330,-2.229657,-3.296180,3.864111,2.242069,-4.834548,-4.535336,4.692159,0.184892],[6.384581,6.705114,1.015631,-0.307666,-1.945800,-1.708634,-0.707613,2.144816,7.066229,5.446354],[7.473148,2.099147,1.490009,-5.126652,-9.698931,4.508856,-0.335860,-6.819410,5.631534,-1.885754],[-3.059742,-1.313849,-4.193680,3.115546,8.656633,-0.554084,7.312893,-1.412627,3.638244,-9.919798],[-4.909133,0.278259,-0.657529,-5.064632,-5.191941,2.339878,-6.858135,-1.770099,0.839347,-8.482042]]], dtype = "float64")#candidate|7600|(15, 6, 10)|const|float64
bop_7601 = relay.less(bop_7542.astype('bool'), relay.reshape(const_7600.astype('bool'), relay.shape_of(bop_7542))) # shape=(15, 6, 10)
func_6208_call = mod.get_global_var('func_6208')
func_6211_call = mutated_mod.get_global_var('func_6211')
var_7606 = relay.var("var_7606", dtype = "float32", shape = (162,))#candidate|7606|(162,)|var|float32
call_7605 = relay.TupleGetItem(func_6208_call(relay.reshape(var_7606.astype('float32'), [2, 9, 9])), 0)
call_7607 = relay.TupleGetItem(func_6211_call(relay.reshape(var_7606.astype('float32'), [2, 9, 9])), 0)
output = relay.Tuple([bop_7547,call_7569,call_7586,bop_7589,bop_7601,call_7605,var_7606,])
output2 = relay.Tuple([bop_7547,call_7570,call_7587,bop_7589,bop_7601,call_7607,var_7606,])
func_7613 = relay.Function([var_7540,var_7546,var_7606,], output)
mod['func_7613'] = func_7613
mod = relay.transform.InferType()(mod)
mutated_mod['func_7613'] = func_7613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7613_call = mutated_mod.get_global_var('func_7613')
var_7615 = relay.var("var_7615", dtype = "float64", shape = (15, 6, 10))#candidate|7615|(15, 6, 10)|var|float64
var_7616 = relay.var("var_7616", dtype = "float64", shape = (15, 6, 10))#candidate|7616|(15, 6, 10)|var|float64
var_7617 = relay.var("var_7617", dtype = "float32", shape = (162,))#candidate|7617|(162,)|var|float32
call_7614 = func_7613_call(var_7615,var_7616,var_7617,)
output = call_7614
func_7618 = relay.Function([var_7615,var_7616,var_7617,], output)
mutated_mod['func_7618'] = func_7618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1927_call = mod.get_global_var('func_1927')
func_1928_call = mutated_mod.get_global_var('func_1928')
call_7647 = func_1927_call()
call_7648 = func_1927_call()
func_5958_call = mod.get_global_var('func_5958')
func_5961_call = mutated_mod.get_global_var('func_5961')
const_7655 = relay.const([-3.152716,-2.310695,9.958720,-6.810927,-7.030757,-1.663503,5.298525,-5.887680,2.983517,-6.353746,-4.434118,1.534703,-4.738685,-9.722109,4.339608,-4.953811,2.059739,8.126777,5.619965,0.018891,5.354753,5.791110,7.400593,2.542911,8.272114,-8.751148,3.678055,-1.168723,5.267263,5.302454,6.419415,-1.847395,-3.884574,0.308204,-5.750122,-7.701165,5.380302,-1.316433,1.279644,3.007565,9.270463,-8.599754,-4.919543,8.239537,7.650660,-1.972971,-5.855908,9.467692,-0.104560,-4.748719,5.719632,7.133048,-6.736298,-0.831947,2.104577,-2.850228,6.079511,4.704011,5.940290,-7.465789,-5.988693,-7.178779,7.059855,2.039586,-8.000869,-5.003474,-5.923981,-2.771319,-9.191892,-8.268867,2.567753,-0.952576,6.431299,-9.503798,-2.558400,1.963661,2.331107,6.219050,-9.671784,-7.427320,-1.006141,-4.918269,-4.602055,5.514147,9.346882,-3.383637,-2.734650,-3.367538,8.465850,4.823659,2.709783,-7.837659,-1.920870,7.198690,-1.856333,9.865684,8.424814,-3.511853,3.293572,-1.227941,3.289227,9.002553,2.433464,-3.563490,-6.117640], dtype = "float64")#candidate|7655|(105,)|const|float64
call_7654 = relay.TupleGetItem(func_5958_call(relay.reshape(const_7655.astype('float64'), [21, 5])), 2)
call_7656 = relay.TupleGetItem(func_5961_call(relay.reshape(const_7655.astype('float64'), [21, 5])), 2)
func_5567_call = mod.get_global_var('func_5567')
func_5568_call = mutated_mod.get_global_var('func_5568')
call_7659 = relay.TupleGetItem(func_5567_call(), 0)
call_7660 = relay.TupleGetItem(func_5568_call(), 0)
uop_7663 = relay.sinh(call_7654.astype('float64')) # shape=(21, 5)
uop_7665 = relay.sinh(call_7656.astype('float64')) # shape=(21, 5)
var_7667 = relay.var("var_7667", dtype = "float64", shape = (21, 5))#candidate|7667|(21, 5)|var|float64
bop_7668 = relay.logical_or(uop_7663.astype('bool'), relay.reshape(var_7667.astype('bool'), relay.shape_of(uop_7663))) # shape=(21, 5)
bop_7671 = relay.logical_or(uop_7665.astype('bool'), relay.reshape(var_7667.astype('bool'), relay.shape_of(uop_7665))) # shape=(21, 5)
output = relay.Tuple([call_7647,const_7655,call_7659,bop_7668,])
output2 = relay.Tuple([call_7648,const_7655,call_7660,bop_7671,])
func_7672 = relay.Function([var_7667,], output)
mod['func_7672'] = func_7672
mod = relay.transform.InferType()(mod)
var_7673 = relay.var("var_7673", dtype = "float64", shape = (21, 5))#candidate|7673|(21, 5)|var|float64
output = func_7672(var_7673)
func_7674 = relay.Function([var_7673], output)
mutated_mod['func_7674'] = func_7674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6881_call = mod.get_global_var('func_6881')
func_6883_call = mutated_mod.get_global_var('func_6883')
call_7754 = func_6881_call()
call_7755 = func_6881_call()
func_398_call = mod.get_global_var('func_398')
func_400_call = mutated_mod.get_global_var('func_400')
call_7784 = relay.TupleGetItem(func_398_call(), 0)
call_7785 = relay.TupleGetItem(func_400_call(), 0)
func_1648_call = mod.get_global_var('func_1648')
func_1650_call = mutated_mod.get_global_var('func_1650')
call_7792 = func_1648_call()
call_7793 = func_1648_call()
output = relay.Tuple([call_7754,call_7784,call_7792,])
output2 = relay.Tuple([call_7755,call_7785,call_7793,])
func_7794 = relay.Function([], output)
mod['func_7794'] = func_7794
mod = relay.transform.InferType()(mod)
output = func_7794()
func_7795 = relay.Function([], output)
mutated_mod['func_7795'] = func_7795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1726_call = mod.get_global_var('func_1726')
func_1728_call = mutated_mod.get_global_var('func_1728')
call_7869 = func_1726_call()
call_7870 = func_1726_call()
output = call_7869
output2 = call_7870
func_7874 = relay.Function([], output)
mod['func_7874'] = func_7874
mod = relay.transform.InferType()(mod)
output = func_7874()
func_7875 = relay.Function([], output)
mutated_mod['func_7875'] = func_7875
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1927_call = mod.get_global_var('func_1927')
func_1928_call = mutated_mod.get_global_var('func_1928')
call_7909 = func_1927_call()
call_7910 = func_1927_call()
func_5522_call = mod.get_global_var('func_5522')
func_5526_call = mutated_mod.get_global_var('func_5526')
var_7918 = relay.var("var_7918", dtype = "uint16", shape = ())#candidate|7918|()|var|uint16
var_7919 = relay.var("var_7919", dtype = "uint16", shape = (462,))#candidate|7919|(462,)|var|uint16
call_7917 = relay.TupleGetItem(func_5522_call(relay.reshape(var_7918.astype('uint16'), []), relay.reshape(var_7919.astype('uint16'), [7, 6, 11]), ), 0)
call_7920 = relay.TupleGetItem(func_5526_call(relay.reshape(var_7918.astype('uint16'), []), relay.reshape(var_7919.astype('uint16'), [7, 6, 11]), ), 0)
output = relay.Tuple([call_7909,call_7917,var_7918,var_7919,])
output2 = relay.Tuple([call_7910,call_7920,var_7918,var_7919,])
func_7939 = relay.Function([var_7918,var_7919,], output)
mod['func_7939'] = func_7939
mod = relay.transform.InferType()(mod)
mutated_mod['func_7939'] = func_7939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7939_call = mutated_mod.get_global_var('func_7939')
var_7941 = relay.var("var_7941", dtype = "uint16", shape = ())#candidate|7941|()|var|uint16
var_7942 = relay.var("var_7942", dtype = "uint16", shape = (462,))#candidate|7942|(462,)|var|uint16
call_7940 = func_7939_call(var_7941,var_7942,)
output = call_7940
func_7943 = relay.Function([var_7941,var_7942,], output)
mutated_mod['func_7943'] = func_7943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1726_call = mod.get_global_var('func_1726')
func_1728_call = mutated_mod.get_global_var('func_1728')
call_7967 = func_1726_call()
call_7968 = func_1726_call()
output = relay.Tuple([call_7967,])
output2 = relay.Tuple([call_7968,])
func_7975 = relay.Function([], output)
mod['func_7975'] = func_7975
mod = relay.transform.InferType()(mod)
mutated_mod['func_7975'] = func_7975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7975_call = mutated_mod.get_global_var('func_7975')
call_7976 = func_7975_call()
output = call_7976
func_7977 = relay.Function([], output)
mutated_mod['func_7977'] = func_7977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6068_call = mod.get_global_var('func_6068')
func_6070_call = mutated_mod.get_global_var('func_6070')
call_8004 = relay.TupleGetItem(func_6068_call(), 1)
call_8005 = relay.TupleGetItem(func_6070_call(), 1)
func_4053_call = mod.get_global_var('func_4053')
func_4054_call = mutated_mod.get_global_var('func_4054')
call_8031 = relay.TupleGetItem(func_4053_call(), 0)
call_8032 = relay.TupleGetItem(func_4054_call(), 0)
func_3591_call = mod.get_global_var('func_3591')
func_3592_call = mutated_mod.get_global_var('func_3592')
call_8041 = func_3591_call()
call_8042 = func_3591_call()
func_7939_call = mod.get_global_var('func_7939')
func_7943_call = mutated_mod.get_global_var('func_7943')
var_8045 = relay.var("var_8045", dtype = "uint16", shape = ())#candidate|8045|()|var|uint16
const_8046 = relay.const([-2,8,4,-6,-8,-6,-1,-6,1,-10,-1,-4,5,4,2,-6,-10,4,-8,8,-7,-10,7,1,-1,8,1,9,-3,7,10,2,8,4,8,1,-6,-6,-6,-2,6,-10,-2,-5,6,10,7,-6,10,10,-3,1,-1,-4,-4,3,6,8,-4,5,-5,6,7,-7,-3,4,10,-5,4,10,-6,9,8,-2,-10,-4,1,7,3,6,-4,4,-6,7,-8,8,-1,10,4,-4,8,-9,10,-1,-1,1,-9,-1,3,5,-6,9,-1,7,-10,8,-8,1,3,1,10,3,-8,-4,-4,-6,3,-8,-4,-8,5,-4,-4,-9,6,-3,5,-6,10,-7,1,7,-9,-8,9,9,3,4,-10,-2,-6,-5,-3,-5,-10,-7,6,-5,-10,-9,-7,2,-6,7,1,4,-6,-10,9,2,-8,10,-5,-8,-6,-4,5,-4,2,7,-1,-3,-8,-6,8,6,-8,-9,-9,-8,2,-7,7,10,-1,5,7,-10,2,-4,3,8,6,4,4,10,3,-5,-1,8,-1,5,-2,5,-1,6,-10,-5,2,4,1,-2,-3,5,-3,7,7,-3,7,2,-8,-3,-1,-5,-10,-8,2,7,8,-1,-4,-6,10,-9,7,6,8,-6,-8,1,-9,-2,3,-10,9,2,10,4,7,-9,-5,-2,4,1,10,-1,2,-1,3,6,3,-7,7,-4,-7,1,-8,2,-2,6,-6,10,-10,-5,-4,-7,10,-1,7,1,8,3,-6,10,9,-7,-10,-3,10,5,8,9,6,-6,7,7,1,3,-7,5,-6,-1,9,-9,3,-1,8,10,3,-6,-3,-6,-5,2,-2,9,9,-6,-5,9,1,-10,3,-4,6,-7,-5,5,-3,-1,6,-3,-2,-5,-6,-5,-6,7,-5,-6,-10,-1,-5,4,-5,-3,5,-8,-8,3,7,2,-3,3,-1,8,-1,6,-7,-5,5,5,-7,8,6,-9,9,6,-2,9,-7,5,-8,-3,-1,-1,-6,8,-9,-9,10,-10,1,1,5,7,9,-2,-4,3,-3,6,1,5,2,7,-1,-1,2,-6,-1,1,-8,8,7,-1,-4,-2,-1,-6,-10,-5,7,5,-7,8,-7,-10,1,-9,9,-9,-5,9,9,-10,-6,3,-2,-5,-1,-1,-2,-3,10,1,2,-4,2,-4,9,-1,-1,-10,-1,4,-10,10,5,-4,5,-4,-5,5,-2,-8,5,5,2,-10,2,6], dtype = "uint16")#candidate|8046|(462,)|const|uint16
call_8044 = relay.TupleGetItem(func_7939_call(relay.reshape(var_8045.astype('uint16'), []), relay.reshape(const_8046.astype('uint16'), [462,]), ), 0)
call_8047 = relay.TupleGetItem(func_7943_call(relay.reshape(var_8045.astype('uint16'), []), relay.reshape(const_8046.astype('uint16'), [462,]), ), 0)
func_963_call = mod.get_global_var('func_963')
func_965_call = mutated_mod.get_global_var('func_965')
const_8051 = relay.const([[-7.794837,-0.434333,0.075688,6.275536,-0.790477],[-9.505718,6.672410,5.717151,9.556843,-1.482262],[-2.628066,-4.582025,0.338127,2.788753,5.069768],[7.527629,9.575159,-4.946292,4.793270,-9.292526],[-8.616086,5.843059,-6.851679,6.352626,-9.784256],[-7.205652,-5.176739,-4.993418,-8.666338,0.440692],[-4.973184,-5.677285,-2.353117,-6.790257,-5.518233],[7.819621,4.062646,-5.601110,-3.427267,8.084953],[6.022179,7.039387,9.652974,2.063439,2.555006],[5.172573,-0.913120,0.697132,6.861664,-7.887804],[-5.233104,-8.528069,3.438557,-3.679694,-2.708409],[-2.237468,3.201326,1.505453,7.323586,-9.474873],[-1.022655,6.665116,5.293537,8.112226,-0.767541],[-2.639805,-9.401161,3.219992,5.565126,0.118005],[6.795800,-3.705135,9.175023,0.612236,-1.787351],[2.030345,-8.114739,3.248981,-4.403036,-9.876035],[9.963979,0.074717,7.879794,9.697444,-7.648553],[-9.648669,-3.017574,-3.167865,-8.590135,-7.943950],[-7.022594,7.906781,-0.610019,-1.585248,-3.657721],[-5.716680,-4.179449,5.463249,-6.244400,-6.508689],[5.782620,-8.131553,0.691911,5.489094,8.218651]], dtype = "float64")#candidate|8051|(21, 5)|const|float64
call_8050 = relay.TupleGetItem(func_963_call(relay.reshape(const_8051.astype('float64'), [105,])), 1)
call_8052 = relay.TupleGetItem(func_965_call(relay.reshape(const_8051.astype('float64'), [105,])), 1)
func_3676_call = mod.get_global_var('func_3676')
func_3677_call = mutated_mod.get_global_var('func_3677')
call_8057 = relay.TupleGetItem(func_3676_call(), 0)
call_8058 = relay.TupleGetItem(func_3677_call(), 0)
func_6284_call = mod.get_global_var('func_6284')
func_6286_call = mutated_mod.get_global_var('func_6286')
call_8062 = relay.TupleGetItem(func_6284_call(), 0)
call_8063 = relay.TupleGetItem(func_6286_call(), 0)
output = relay.Tuple([call_8004,call_8031,call_8041,call_8044,var_8045,const_8046,call_8050,const_8051,call_8057,call_8062,])
output2 = relay.Tuple([call_8005,call_8032,call_8042,call_8047,var_8045,const_8046,call_8052,const_8051,call_8058,call_8063,])
func_8073 = relay.Function([var_8045,], output)
mod['func_8073'] = func_8073
mod = relay.transform.InferType()(mod)
var_8074 = relay.var("var_8074", dtype = "uint16", shape = ())#candidate|8074|()|var|uint16
output = func_8073(var_8074)
func_8075 = relay.Function([var_8074], output)
mutated_mod['func_8075'] = func_8075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6350_call = mod.get_global_var('func_6350')
func_6352_call = mutated_mod.get_global_var('func_6352')
call_8092 = relay.TupleGetItem(func_6350_call(), 0)
call_8093 = relay.TupleGetItem(func_6352_call(), 0)
output = call_8092
output2 = call_8093
func_8094 = relay.Function([], output)
mod['func_8094'] = func_8094
mod = relay.transform.InferType()(mod)
mutated_mod['func_8094'] = func_8094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8094_call = mutated_mod.get_global_var('func_8094')
call_8095 = func_8094_call()
output = call_8095
func_8096 = relay.Function([], output)
mutated_mod['func_8096'] = func_8096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4907_call = mod.get_global_var('func_4907')
func_4908_call = mutated_mod.get_global_var('func_4908')
call_8097 = func_4907_call()
call_8098 = func_4907_call()
const_8104 = relay.const([[[2.788060,3.359823],[7.681718,8.428179],[-4.799667,-2.259087],[5.215480,-2.139200],[-2.573477,-2.088592],[-0.515191,0.350607],[7.448724,7.602869]],[[2.774120,-3.033832],[7.548101,-6.518206],[-8.410098,8.049438],[5.258185,7.634673],[5.549972,1.013812],[7.062915,-6.493174],[-7.518764,-8.662272]],[[-5.962517,2.927985],[6.236937,-5.508496],[4.917391,6.561777],[-5.704163,-2.132020],[-7.030206,2.269407],[8.828273,-7.328827],[-4.030334,-4.436444]],[[-4.583498,1.627808],[-4.186821,-0.175639],[-0.033560,-5.809512],[5.603075,9.826187],[3.922039,9.739473],[5.409658,6.740562],[-8.733943,-4.876320]],[[-1.402161,0.937474],[2.206822,5.681042],[4.076044,7.134783],[-7.348940,0.374760],[-5.262314,1.021378],[-8.829053,8.799080],[1.475515,-9.700436]],[[-7.951127,8.718999],[2.201546,1.018930],[0.371123,-7.761637],[-4.692422,-5.306605],[5.988066,-0.548633],[-6.925186,4.377134],[1.237865,-8.424101]],[[9.220016,-6.243660],[3.086263,-3.558267],[-3.649186,-0.297373],[-3.842963,-0.140582],[-4.946756,4.207334],[-8.856508,4.907257],[-1.946729,4.797882]]], dtype = "float32")#candidate|8104|(7, 7, 2)|const|float32
bop_8105 = relay.greater(call_8097.astype('bool'), relay.reshape(const_8104.astype('bool'), relay.shape_of(call_8097))) # shape=(7, 7, 2)
bop_8108 = relay.greater(call_8098.astype('bool'), relay.reshape(const_8104.astype('bool'), relay.shape_of(call_8098))) # shape=(7, 7, 2)
func_6406_call = mod.get_global_var('func_6406')
func_6407_call = mutated_mod.get_global_var('func_6407')
call_8110 = relay.TupleGetItem(func_6406_call(), 0)
call_8111 = relay.TupleGetItem(func_6407_call(), 0)
uop_8132 = relay.cos(const_8104.astype('float32')) # shape=(7, 7, 2)
output = relay.Tuple([bop_8105,call_8110,uop_8132,])
output2 = relay.Tuple([bop_8108,call_8111,uop_8132,])
func_8138 = relay.Function([], output)
mod['func_8138'] = func_8138
mod = relay.transform.InferType()(mod)
mutated_mod['func_8138'] = func_8138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8138_call = mutated_mod.get_global_var('func_8138')
call_8139 = func_8138_call()
output = call_8139
func_8140 = relay.Function([], output)
mutated_mod['func_8140'] = func_8140
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7113_call = mod.get_global_var('func_7113')
func_7115_call = mutated_mod.get_global_var('func_7115')
call_8163 = func_7113_call()
call_8164 = func_7113_call()
output = relay.Tuple([call_8163,])
output2 = relay.Tuple([call_8164,])
func_8175 = relay.Function([], output)
mod['func_8175'] = func_8175
mod = relay.transform.InferType()(mod)
mutated_mod['func_8175'] = func_8175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8175_call = mutated_mod.get_global_var('func_8175')
call_8176 = func_8175_call()
output = call_8176
func_8177 = relay.Function([], output)
mutated_mod['func_8177'] = func_8177
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8178 = relay.var("var_8178", dtype = "int16", shape = ())#candidate|8178|()|var|int16
const_8179 = relay.const([[[-7,-6,-10,-5,-1,-5,-5,-7,9,-8,-4,-10,9,-8,6,-10],[3,-3,3,9,-8,8,9,8,-3,5,-9,6,5,-5,-10,-3],[1,5,-5,9,-1,7,-6,10,-3,-7,-9,10,-7,-6,-10,-1],[4,6,-2,-3,5,5,-4,9,9,10,8,-4,5,-3,7,-7],[-10,2,-1,7,6,-7,6,-8,3,2,7,8,4,-8,-5,-3],[9,7,4,-6,-3,-1,-1,5,-8,-5,3,-7,-5,9,10,-3],[1,9,-3,4,-9,6,-5,-4,-7,7,2,-8,-9,-5,1,7]],[[9,5,-4,9,-5,5,-7,4,10,8,7,9,3,6,3,3],[-3,5,9,-3,2,-6,-1,-6,4,-2,-8,-9,-4,-2,-10,8],[-5,-1,8,9,-5,10,-9,-4,-10,6,-7,8,3,6,-7,7],[9,6,-3,1,2,-4,8,6,6,6,8,-3,-4,-4,-5,-2],[-10,-6,-5,-3,-8,10,4,-6,7,-2,-7,-5,5,-3,10,-7],[-6,-5,9,8,4,-5,-3,1,-4,4,-9,2,8,-6,-1,-1],[7,-7,-6,6,-2,-10,-2,4,3,7,7,-6,3,7,5,10]],[[-6,8,2,3,5,-1,-6,2,3,1,-7,8,1,5,-5,-7],[1,-4,9,9,3,-10,-4,-8,2,-10,-8,-10,-4,-4,1,10],[9,7,3,2,5,-7,-4,8,6,-4,4,3,8,-7,-1,1],[10,7,-3,3,9,-8,5,-7,-2,5,-7,-6,-10,-4,-9,-10],[-4,-6,6,-6,7,7,8,5,7,9,-2,8,7,2,10,7],[-9,-10,2,1,8,5,2,-9,2,4,3,4,6,8,-8,-10],[9,3,6,3,1,-1,8,3,-7,1,-9,-2,1,-2,6,-7]],[[2,6,-5,1,7,-7,3,2,-9,4,8,-4,5,-9,10,5],[7,9,10,-5,5,1,-6,-9,-6,2,8,-6,-3,-3,-2,-4],[-10,2,-4,-7,3,-6,1,-1,-8,-2,8,-1,-2,4,3,-4],[9,-10,-2,-2,3,1,3,10,6,10,-9,-5,-5,6,6,-8],[-5,-10,5,2,-7,-3,-7,-4,6,-7,4,7,-2,7,4,-5],[-4,-6,6,-9,10,-5,-5,-10,-4,-6,-2,10,-6,3,2,9],[-2,5,2,3,3,1,-9,-7,-9,-1,-5,-6,-6,3,7,-4]],[[-6,9,10,-1,9,1,4,-1,2,-5,-3,-8,-8,-8,2,3],[8,5,3,-3,8,2,-3,-5,5,1,-1,-8,9,-3,6,8],[-10,-6,-1,-7,4,-10,-4,-1,7,8,1,6,-2,1,-6,3],[-4,-1,9,-3,-9,9,10,-2,-4,-4,6,6,-8,7,-8,2],[-1,-6,-8,3,-1,-1,-4,1,-5,2,-6,1,-7,-10,1,6],[2,4,10,9,10,6,5,2,2,-3,-4,4,5,6,-5,-9],[4,-9,3,-8,10,-6,9,6,2,2,8,-9,8,-10,-10,10]],[[-4,-10,8,9,2,-4,-3,-4,4,3,2,4,7,-4,2,-3],[-2,-3,-3,-10,-8,-7,9,-6,-9,-2,2,2,-9,-8,-10,-7],[-6,-5,-5,-3,1,3,-3,-10,9,3,9,3,-2,9,2,6],[-8,-6,-6,-5,-8,7,-7,-4,-1,10,-4,8,-3,-8,4,-4],[5,-5,-8,-7,9,8,1,4,8,-3,-8,8,9,10,-2,-6],[-6,-5,1,3,-6,-6,2,10,-6,4,-4,-5,10,8,2,6],[-7,4,-5,-8,9,-9,-5,-3,-9,-5,9,6,7,-9,8,-9]],[[-8,-2,10,-5,5,-10,-10,3,9,-2,2,-10,-2,10,-6,-6],[1,-9,-10,-8,6,-9,-10,-6,4,9,-6,7,-10,1,-5,10],[4,7,-2,3,2,4,6,-2,8,4,-2,1,7,6,8,10],[-5,-10,-1,-7,-4,-4,3,-1,-9,4,-6,-1,-8,9,-5,9],[-5,9,1,8,10,-8,-9,-3,-3,-8,-3,-4,-8,-8,1,2],[-8,1,-8,-7,-10,-1,-3,7,-3,-5,-6,1,1,4,7,-7],[7,-4,-6,3,-5,6,1,4,-8,2,7,5,-3,9,7,2]],[[-5,-8,9,-8,6,-2,7,10,-4,-9,-6,-8,-5,8,6,-5],[8,3,-5,-2,7,5,-10,1,-9,-5,-5,3,-2,4,-1,-1],[4,-8,7,9,4,7,-1,9,9,5,7,-7,-9,8,-2,10],[-3,5,8,3,10,-7,-10,-10,-2,-6,5,9,4,5,-8,-2],[-5,8,-2,7,-3,-2,-3,-2,9,6,-1,7,4,-3,-9,3],[3,9,-4,-5,3,8,2,-2,7,-5,3,-4,-8,-1,-2,-2],[8,8,6,-9,-3,-6,6,-5,4,-3,-4,7,-2,10,5,-8]]], dtype = "int16")#candidate|8179|(8, 7, 16)|const|int16
bop_8180 = relay.bitwise_or(var_8178.astype('int16'), const_8179.astype('int16')) # shape=(8, 7, 16)
func_438_call = mod.get_global_var('func_438')
func_439_call = mutated_mod.get_global_var('func_439')
call_8194 = func_438_call()
call_8195 = func_438_call()
func_1546_call = mod.get_global_var('func_1546')
func_1548_call = mutated_mod.get_global_var('func_1548')
call_8205 = relay.TupleGetItem(func_1546_call(), 1)
call_8206 = relay.TupleGetItem(func_1548_call(), 1)
func_3591_call = mod.get_global_var('func_3591')
func_3592_call = mutated_mod.get_global_var('func_3592')
call_8216 = func_3591_call()
call_8217 = func_3591_call()
func_2857_call = mod.get_global_var('func_2857')
func_2859_call = mutated_mod.get_global_var('func_2859')
call_8218 = func_2857_call()
call_8219 = func_2857_call()
output = relay.Tuple([bop_8180,call_8194,call_8205,call_8216,call_8218,])
output2 = relay.Tuple([bop_8180,call_8195,call_8206,call_8217,call_8219,])
func_8228 = relay.Function([var_8178,], output)
mod['func_8228'] = func_8228
mod = relay.transform.InferType()(mod)
mutated_mod['func_8228'] = func_8228
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8229 = relay.var("var_8229", dtype = "int16", shape = ())#candidate|8229|()|var|int16
func_8228_call = mutated_mod.get_global_var('func_8228')
call_8230 = func_8228_call(var_8229)
output = call_8230
func_8231 = relay.Function([var_8229], output)
mutated_mod['func_8231'] = func_8231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4907_call = mod.get_global_var('func_4907')
func_4908_call = mutated_mod.get_global_var('func_4908')
call_8239 = func_4907_call()
call_8240 = func_4907_call()
output = call_8239
output2 = call_8240
func_8243 = relay.Function([], output)
mod['func_8243'] = func_8243
mod = relay.transform.InferType()(mod)
mutated_mod['func_8243'] = func_8243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8243_call = mutated_mod.get_global_var('func_8243')
call_8244 = func_8243_call()
output = call_8244
func_8245 = relay.Function([], output)
mutated_mod['func_8245'] = func_8245
mutated_mod = relay.transform.InferType()(mutated_mod)
func_338_call = mod.get_global_var('func_338')
func_340_call = mutated_mod.get_global_var('func_340')
call_8289 = func_338_call()
call_8290 = func_338_call()
output = relay.Tuple([call_8289,])
output2 = relay.Tuple([call_8290,])
func_8300 = relay.Function([], output)
mod['func_8300'] = func_8300
mod = relay.transform.InferType()(mod)
mutated_mod['func_8300'] = func_8300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8300_call = mutated_mod.get_global_var('func_8300')
call_8301 = func_8300_call()
output = call_8301
func_8302 = relay.Function([], output)
mutated_mod['func_8302'] = func_8302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3188_call = mod.get_global_var('func_3188')
func_3189_call = mutated_mod.get_global_var('func_3189')
call_8336 = relay.TupleGetItem(func_3188_call(), 1)
call_8337 = relay.TupleGetItem(func_3189_call(), 1)
output = relay.Tuple([call_8336,])
output2 = relay.Tuple([call_8337,])
func_8367 = relay.Function([], output)
mod['func_8367'] = func_8367
mod = relay.transform.InferType()(mod)
output = func_8367()
func_8368 = relay.Function([], output)
mutated_mod['func_8368'] = func_8368
mutated_mod = relay.transform.InferType()(mutated_mod)
func_922_call = mod.get_global_var('func_922')
func_924_call = mutated_mod.get_global_var('func_924')
call_8381 = func_922_call()
call_8382 = func_922_call()
func_7225_call = mod.get_global_var('func_7225')
func_7227_call = mutated_mod.get_global_var('func_7227')
call_8391 = relay.TupleGetItem(func_7225_call(), 1)
call_8392 = relay.TupleGetItem(func_7227_call(), 1)
output = relay.Tuple([call_8381,call_8391,])
output2 = relay.Tuple([call_8382,call_8392,])
func_8397 = relay.Function([], output)
mod['func_8397'] = func_8397
mod = relay.transform.InferType()(mod)
output = func_8397()
func_8398 = relay.Function([], output)
mutated_mod['func_8398'] = func_8398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3648_call = mod.get_global_var('func_3648')
func_3649_call = mutated_mod.get_global_var('func_3649')
call_8454 = func_3648_call()
call_8455 = func_3648_call()
func_3148_call = mod.get_global_var('func_3148')
func_3151_call = mutated_mod.get_global_var('func_3151')
var_8478 = relay.var("var_8478", dtype = "int16", shape = (825,))#candidate|8478|(825,)|var|int16
var_8479 = relay.var("var_8479", dtype = "int64", shape = (1008,))#candidate|8479|(1008,)|var|int64
call_8477 = relay.TupleGetItem(func_3148_call(relay.reshape(var_8478.astype('int16'), [55, 15]), relay.reshape(var_8479.astype('int64'), [1008,]), ), 2)
call_8480 = relay.TupleGetItem(func_3151_call(relay.reshape(var_8478.astype('int16'), [55, 15]), relay.reshape(var_8479.astype('int64'), [1008,]), ), 2)
output = relay.Tuple([call_8454,call_8477,var_8478,var_8479,])
output2 = relay.Tuple([call_8455,call_8480,var_8478,var_8479,])
func_8493 = relay.Function([var_8478,var_8479,], output)
mod['func_8493'] = func_8493
mod = relay.transform.InferType()(mod)
var_8494 = relay.var("var_8494", dtype = "int16", shape = (825,))#candidate|8494|(825,)|var|int16
var_8495 = relay.var("var_8495", dtype = "int64", shape = (1008,))#candidate|8495|(1008,)|var|int64
output = func_8493(var_8494,var_8495,)
func_8496 = relay.Function([var_8494,var_8495,], output)
mutated_mod['func_8496'] = func_8496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4168_call = mod.get_global_var('func_4168')
func_4169_call = mutated_mod.get_global_var('func_4169')
call_8556 = relay.TupleGetItem(func_4168_call(), 2)
call_8557 = relay.TupleGetItem(func_4169_call(), 2)
func_8243_call = mod.get_global_var('func_8243')
func_8245_call = mutated_mod.get_global_var('func_8245')
call_8562 = func_8243_call()
call_8563 = func_8243_call()
output = relay.Tuple([call_8556,call_8562,])
output2 = relay.Tuple([call_8557,call_8563,])
func_8599 = relay.Function([], output)
mod['func_8599'] = func_8599
mod = relay.transform.InferType()(mod)
mutated_mod['func_8599'] = func_8599
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8599_call = mutated_mod.get_global_var('func_8599')
call_8600 = func_8599_call()
output = call_8600
func_8601 = relay.Function([], output)
mutated_mod['func_8601'] = func_8601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1366_call = mod.get_global_var('func_1366')
func_1367_call = mutated_mod.get_global_var('func_1367')
call_8605 = relay.TupleGetItem(func_1366_call(), 6)
call_8606 = relay.TupleGetItem(func_1367_call(), 6)
output = call_8605
output2 = call_8606
func_8610 = relay.Function([], output)
mod['func_8610'] = func_8610
mod = relay.transform.InferType()(mod)
output = func_8610()
func_8611 = relay.Function([], output)
mutated_mod['func_8611'] = func_8611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8397_call = mod.get_global_var('func_8397')
func_8398_call = mutated_mod.get_global_var('func_8398')
call_8614 = relay.TupleGetItem(func_8397_call(), 1)
call_8615 = relay.TupleGetItem(func_8398_call(), 1)
func_2618_call = mod.get_global_var('func_2618')
func_2620_call = mutated_mod.get_global_var('func_2620')
const_8668 = relay.const([True,True,True,True,True,False,True,False,True,False,False,True,False,True,False,True,False,False,False,False,True,False,False,False,False,True,False,False,True,True,False,False,False,True,False,True,False,True,False,True,True,False,False,False,True,False,True,True,False,True,True,True,False,True,False,False,True,False,False,False,True,False,True,True,False,True,True,False,False,True,True,False,True,True,False,False,True,True,True,False,False,True,True,False,False,True,True,True,False,True,False,True,False,True,True,False,False,False,False,False,True,True,False,False,False,False,False,True,True,True,True,False,False,True,False,True,False,True,False,False,True,False,False,True,True,True,True,True,True,True,False,False,False,False,False,False,True,False,True,False,True,True,False,False,False,True,True,False,False,True,True,True,False,True,False,True,False,True,True,True,False,True,True,False,True,True,False,False,True,False,True,False,True,True,False,True,False,True,True,True,True,False,False,True,True,True,False,True,False,True,False,True,False,True,True,False,False,False,False,True,False,True,False,True,True,False,False,True,False,True,False,True,False,True,False,True,False,False,True,False,False,True,True,False,True,True,False,True,True,True,True,True,False,True,False,True,True,False,True,True,True,True,False,True,False,False,True,False,True,False,True,True,True,False,True,False,True,False,False,False,True,True,True,True,False,True,True,True,True,False,True,True,True,True,False,False,False,True,False,True,True,True,False,True,False,True,True,True,True,True,False,False,False,True,False,False,True,True,False,False,True,True,True,False,False,False,False,False,True,True,True,True,False,True,False,False,True,True,False,False,True,False,True,True,True,True,False,False,False,False,True,True,True,False,True,True,False,False,False,False,True,True,True,True,True,True,False,False,False,False,False,True,False,True,True,True,False,True,False,False,True,True,True,False,True,True,True,False,True,True,False,False,True,True,True,False,False,True,False,False,True,False,False,True,False,True,True,False,False,True,True,True,False,False,True,True,True,False,True,False,False,True,False,True,False,False,True,False,True,True,True,True,True,True,False,True,False,True,False,False,False,True,True,False,True,False,False,True,False,True,True,False,True,False,True,True,False,False,False,True,True,True,False,True,False,True,False,False,False,False,False,True,True,True,True,True,True,True,False,True,True,True,False,False,True,True,True,True,False,True,True,True,False,True,False,False,False,True,False,True,True,False,False,True,True,True,False,False,True,False,False,False,True,False,False,True,True,True,False,True,True,True,True,True,True,True,False,True,False,False,False,False,True,False,True,False,False,True,True,True,True,True,True,False,True,True,True,False,False,False,False,True,True,True,True,False,False,True,False,True,True,False,True,False,True,False,True,True,True,False,False,False,True,True,False,False,False,False,False,False,False,False,False,True,True,True,False,False,False,False,True,True,False,False,False,True,False,True,False,True,True,False,True,False,True,True,False,True,True,False,False,True,True,False,True,False,True,True,False,True,True,True,False,True,True,False,True,True,True,True,False,False,False,True,False,True,True,False,True,False,True,True,False,False,True,True,False,False,False,True,True,True,False,True,False,False,False,True,True,True,True,False,False,True,True,False,False,False,True,True,True,False,False,True,False,True,False,False,True,False,True,False,True,False,False,True,False,False,True,True,True,False,True,True,True,True,False,True,True,True,True,False,True,True,True,True], dtype = "bool")#candidate|8668|(686,)|const|bool
call_8667 = relay.TupleGetItem(func_2618_call(relay.reshape(const_8668.astype('bool'), [14, 7, 7])), 0)
call_8669 = relay.TupleGetItem(func_2620_call(relay.reshape(const_8668.astype('bool'), [14, 7, 7])), 0)
var_8685 = relay.var("var_8685", dtype = "float64", shape = (21, 5))#candidate|8685|(21, 5)|var|float64
bop_8686 = relay.divide(call_8614.astype('float64'), relay.reshape(var_8685.astype('float64'), relay.shape_of(call_8614))) # shape=(21, 5)
bop_8689 = relay.divide(call_8615.astype('float64'), relay.reshape(var_8685.astype('float64'), relay.shape_of(call_8615))) # shape=(21, 5)
uop_8696 = relay.cosh(var_8685.astype('float32')) # shape=(21, 5)
bop_8704 = relay.power(uop_8696.astype('float64'), relay.reshape(call_8614.astype('float64'), relay.shape_of(uop_8696))) # shape=(21, 5)
bop_8707 = relay.power(uop_8696.astype('float64'), relay.reshape(call_8615.astype('float64'), relay.shape_of(uop_8696))) # shape=(21, 5)
func_8243_call = mod.get_global_var('func_8243')
func_8245_call = mutated_mod.get_global_var('func_8245')
call_8715 = func_8243_call()
call_8716 = func_8243_call()
uop_8721 = relay.erf(var_8685.astype('float64')) # shape=(21, 5)
output = relay.Tuple([call_8667,const_8668,bop_8686,bop_8704,call_8715,uop_8721,])
output2 = relay.Tuple([call_8669,const_8668,bop_8689,bop_8707,call_8716,uop_8721,])
func_8751 = relay.Function([var_8685,], output)
mod['func_8751'] = func_8751
mod = relay.transform.InferType()(mod)
var_8752 = relay.var("var_8752", dtype = "float64", shape = (21, 5))#candidate|8752|(21, 5)|var|float64
output = func_8751(var_8752)
func_8753 = relay.Function([var_8752], output)
mutated_mod['func_8753'] = func_8753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6720_call = mod.get_global_var('func_6720')
func_6722_call = mutated_mod.get_global_var('func_6722')
call_8793 = relay.TupleGetItem(func_6720_call(), 0)
call_8794 = relay.TupleGetItem(func_6722_call(), 0)
output = relay.Tuple([call_8793,])
output2 = relay.Tuple([call_8794,])
func_8797 = relay.Function([], output)
mod['func_8797'] = func_8797
mod = relay.transform.InferType()(mod)
output = func_8797()
func_8798 = relay.Function([], output)
mutated_mod['func_8798'] = func_8798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8397_call = mod.get_global_var('func_8397')
func_8398_call = mutated_mod.get_global_var('func_8398')
call_8824 = relay.TupleGetItem(func_8397_call(), 1)
call_8825 = relay.TupleGetItem(func_8398_call(), 1)
var_8848 = relay.var("var_8848", dtype = "float64", shape = (21, 5))#candidate|8848|(21, 5)|var|float64
bop_8849 = relay.bitwise_or(call_8824.astype('uint32'), relay.reshape(var_8848.astype('uint32'), relay.shape_of(call_8824))) # shape=(21, 5)
bop_8852 = relay.bitwise_or(call_8825.astype('uint32'), relay.reshape(var_8848.astype('uint32'), relay.shape_of(call_8825))) # shape=(21, 5)
func_3525_call = mod.get_global_var('func_3525')
func_3526_call = mutated_mod.get_global_var('func_3526')
call_8856 = func_3525_call()
call_8857 = func_3525_call()
uop_8866 = relay.rsqrt(var_8848.astype('float32')) # shape=(21, 5)
output = relay.Tuple([bop_8849,call_8856,uop_8866,])
output2 = relay.Tuple([bop_8852,call_8857,uop_8866,])
func_8886 = relay.Function([var_8848,], output)
mod['func_8886'] = func_8886
mod = relay.transform.InferType()(mod)
var_8887 = relay.var("var_8887", dtype = "float64", shape = (21, 5))#candidate|8887|(21, 5)|var|float64
output = func_8886(var_8887)
func_8888 = relay.Function([var_8887], output)
mutated_mod['func_8888'] = func_8888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5785_call = mod.get_global_var('func_5785')
func_5786_call = mutated_mod.get_global_var('func_5786')
call_8893 = relay.TupleGetItem(func_5785_call(), 0)
call_8894 = relay.TupleGetItem(func_5786_call(), 0)
func_3498_call = mod.get_global_var('func_3498')
func_3500_call = mutated_mod.get_global_var('func_3500')
call_8895 = relay.TupleGetItem(func_3498_call(), 0)
call_8896 = relay.TupleGetItem(func_3500_call(), 0)
func_6036_call = mod.get_global_var('func_6036')
func_6038_call = mutated_mod.get_global_var('func_6038')
var_8898 = relay.var("var_8898", dtype = "bool", shape = (686,))#candidate|8898|(686,)|var|bool
call_8897 = relay.TupleGetItem(func_6036_call(relay.reshape(var_8898.astype('bool'), [686,])), 0)
call_8899 = relay.TupleGetItem(func_6038_call(relay.reshape(var_8898.astype('bool'), [686,])), 0)
output = relay.Tuple([call_8893,call_8895,call_8897,var_8898,])
output2 = relay.Tuple([call_8894,call_8896,call_8899,var_8898,])
func_8914 = relay.Function([var_8898,], output)
mod['func_8914'] = func_8914
mod = relay.transform.InferType()(mod)
var_8915 = relay.var("var_8915", dtype = "bool", shape = (686,))#candidate|8915|(686,)|var|bool
output = func_8914(var_8915)
func_8916 = relay.Function([var_8915], output)
mutated_mod['func_8916'] = func_8916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5667_call = mod.get_global_var('func_5667')
func_5668_call = mutated_mod.get_global_var('func_5668')
call_8923 = relay.TupleGetItem(func_5667_call(), 0)
call_8924 = relay.TupleGetItem(func_5668_call(), 0)
func_6479_call = mod.get_global_var('func_6479')
func_6481_call = mutated_mod.get_global_var('func_6481')
call_8955 = relay.TupleGetItem(func_6479_call(), 1)
call_8956 = relay.TupleGetItem(func_6481_call(), 1)
func_1757_call = mod.get_global_var('func_1757')
func_1758_call = mutated_mod.get_global_var('func_1758')
call_8983 = relay.TupleGetItem(func_1757_call(), 0)
call_8984 = relay.TupleGetItem(func_1758_call(), 0)
func_4618_call = mod.get_global_var('func_4618')
func_4619_call = mutated_mod.get_global_var('func_4619')
call_8987 = relay.TupleGetItem(func_4618_call(), 1)
call_8988 = relay.TupleGetItem(func_4619_call(), 1)
output = relay.Tuple([call_8923,call_8955,call_8983,call_8987,])
output2 = relay.Tuple([call_8924,call_8956,call_8984,call_8988,])
func_8995 = relay.Function([], output)
mod['func_8995'] = func_8995
mod = relay.transform.InferType()(mod)
output = func_8995()
func_8996 = relay.Function([], output)
mutated_mod['func_8996'] = func_8996
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9019 = relay.var("var_9019", dtype = "float32", shape = (7, 6, 5))#candidate|9019|(7, 6, 5)|var|float32
const_9020 = relay.const([[[8.677096,7.219135,-9.594762,-4.436496,-4.102355],[-2.693505,2.016203,-7.566605,2.565317,-6.034391],[-1.617914,-3.996615,4.847635,-6.078008,-1.549358],[3.528351,-2.964846,-3.810223,8.333884,1.356205],[-2.784724,-8.741452,-9.178993,5.497429,-9.044899],[-4.517276,1.991306,7.877441,-8.541612,5.657731]],[[-6.579940,-9.524776,-8.054608,5.980937,-6.993513],[6.593001,-9.710266,-5.305561,-1.801642,-8.745609],[-4.197747,4.771792,9.767994,-7.288657,-9.871077],[9.089864,6.069714,-8.170842,-0.496790,6.800702],[-8.625867,-4.002336,-9.323079,-3.602534,-1.415810],[4.778645,5.452075,-3.732958,-2.271394,-4.420656]],[[-1.713512,8.110017,-6.251897,1.207152,8.895197],[3.512847,-1.666949,-6.566786,-9.323573,5.466780],[1.002273,2.743590,-8.256582,-6.345401,2.357552],[3.137715,-0.089461,1.033514,-6.110451,1.899060],[1.292559,-0.871103,-0.448836,-0.814030,2.697060],[4.950420,3.663889,5.294886,-3.028172,-8.581052]],[[-5.695044,-4.193165,-5.125960,9.927939,-8.905970],[-2.870019,0.510795,4.375196,1.735631,6.527346],[-9.966182,8.676481,3.508582,8.665161,-3.607540],[9.190284,8.019089,8.406337,3.615079,9.652189],[-3.365013,3.255675,-7.482714,0.868749,7.799894],[-8.845689,-7.178563,8.285184,-2.604545,8.450203]],[[-7.984055,0.797979,-2.910068,8.627288,-2.636043],[-2.393169,-1.947822,-7.012434,-3.329114,-7.672019],[-6.096453,0.728152,-3.515948,0.553968,3.324351],[-9.119278,7.506004,-5.864609,-2.165010,-2.987973],[-6.420406,6.779210,-8.081748,2.439266,-0.309837],[-4.896043,-4.596219,3.064499,-1.183276,7.374900]],[[1.560936,1.475184,2.760173,5.715235,2.126980],[-7.854883,-5.406676,-6.865818,-3.541931,5.648701],[2.828816,1.660869,-1.205549,7.163136,3.197467],[-8.221948,-0.481835,-3.498694,3.249841,5.846807],[9.594023,-7.975003,-8.715904,-6.701616,-0.975927],[1.369820,-9.994942,4.377234,0.571002,4.624372]],[[4.772242,3.766405,-0.019657,-5.933836,8.588433],[-9.856647,8.355434,-8.963410,-0.991026,-8.917521],[4.958872,-6.524553,7.416588,-4.760926,-8.722121],[2.937323,0.770409,8.333685,-2.606254,-8.061002],[-8.200370,-3.548143,0.637508,6.128013,-2.584069],[9.040667,2.132732,1.018188,3.812015,7.437459]]], dtype = "float32")#candidate|9020|(7, 6, 5)|const|float32
bop_9021 = relay.mod(var_9019.astype('float32'), relay.reshape(const_9020.astype('float32'), relay.shape_of(var_9019))) # shape=(7, 6, 5)
func_5667_call = mod.get_global_var('func_5667')
func_5668_call = mutated_mod.get_global_var('func_5668')
call_9029 = relay.TupleGetItem(func_5667_call(), 0)
call_9030 = relay.TupleGetItem(func_5668_call(), 0)
func_4019_call = mod.get_global_var('func_4019')
func_4020_call = mutated_mod.get_global_var('func_4020')
call_9041 = relay.TupleGetItem(func_4019_call(), 0)
call_9042 = relay.TupleGetItem(func_4020_call(), 0)
bop_9048 = relay.equal(const_9020.astype('bool'), relay.reshape(var_9019.astype('bool'), relay.shape_of(const_9020))) # shape=(7, 6, 5)
func_8797_call = mod.get_global_var('func_8797')
func_8798_call = mutated_mod.get_global_var('func_8798')
call_9054 = relay.TupleGetItem(func_8797_call(), 0)
call_9055 = relay.TupleGetItem(func_8798_call(), 0)
output = relay.Tuple([bop_9021,call_9029,call_9041,bop_9048,call_9054,])
output2 = relay.Tuple([bop_9021,call_9030,call_9042,bop_9048,call_9055,])
func_9056 = relay.Function([var_9019,], output)
mod['func_9056'] = func_9056
mod = relay.transform.InferType()(mod)
mutated_mod['func_9056'] = func_9056
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9057 = relay.var("var_9057", dtype = "float32", shape = (7, 6, 5))#candidate|9057|(7, 6, 5)|var|float32
func_9056_call = mutated_mod.get_global_var('func_9056')
call_9058 = func_9056_call(var_9057)
output = call_9058
func_9059 = relay.Function([var_9057], output)
mutated_mod['func_9059'] = func_9059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8243_call = mod.get_global_var('func_8243')
func_8245_call = mutated_mod.get_global_var('func_8245')
call_9176 = func_8243_call()
call_9177 = func_8243_call()
func_5667_call = mod.get_global_var('func_5667')
func_5668_call = mutated_mod.get_global_var('func_5668')
call_9202 = relay.TupleGetItem(func_5667_call(), 0)
call_9203 = relay.TupleGetItem(func_5668_call(), 0)
func_856_call = mod.get_global_var('func_856')
func_858_call = mutated_mod.get_global_var('func_858')
const_9214 = relay.const([[1.309342],[-1.643061],[-8.195699],[-4.551971],[8.891719],[-8.865818],[-8.566141],[-7.739862],[-6.935520],[5.683513],[-3.724389],[1.440745],[7.629294],[-6.289445],[-4.791429],[-3.795641],[6.431897],[-9.659291],[4.888293],[-3.532732],[1.007345],[-6.050373],[2.406029],[-6.427818],[8.976643],[-4.047890],[8.638208],[-0.555178],[-4.844944],[-2.128908],[-2.597200],[-4.471970],[2.696019],[4.074290],[8.738998],[3.640378],[-0.703821],[-8.335173],[6.925229],[-4.265212],[-3.489388],[-3.261585],[-5.941440],[6.520226],[0.643385],[3.879215],[-3.343285],[4.613575],[6.647409],[-2.201619],[-1.024225],[5.970539],[-3.642027],[-1.084858],[-9.046087],[-8.878259],[-1.014116],[-1.508028],[-5.784183],[3.561519],[1.923025],[2.670618],[0.996567],[0.780583],[7.106312],[0.379953],[5.562154],[7.852609],[6.794678],[7.560000],[-5.491989],[-8.855936],[-8.273195],[1.528692],[-2.948565],[-7.481082],[-9.061608],[6.485690],[-7.307111],[-4.655513],[8.024340],[-2.091288],[-3.679566],[-4.059942],[1.893701],[9.626125],[1.051292],[-7.324491],[-7.892565],[-0.723079],[0.297181],[-7.873046],[-1.803572],[0.793696],[-4.748215],[2.775006],[3.932709],[-0.043955],[6.743423],[5.627215],[3.042684],[-7.184352],[7.811725],[-6.147445],[-1.755436]], dtype = "float64")#candidate|9214|(105, 1)|const|float64
call_9213 = relay.TupleGetItem(func_856_call(relay.reshape(const_9214.astype('float64'), [21, 5])), 0)
call_9215 = relay.TupleGetItem(func_858_call(relay.reshape(const_9214.astype('float64'), [21, 5])), 0)
func_5632_call = mod.get_global_var('func_5632')
func_5635_call = mutated_mod.get_global_var('func_5635')
const_9227 = relay.const([-4,3,4,8,-6,6,4,-5,8,5,1,-1,7,-5,2,4,-4,5,-1,-5,-6,8,-10,-2,4,8,-1,10,-8,7,-2,7,-8,-5,5,-5,-2,-2,-7,-3,-4,-8,1,-5,2,10,-2,9,9,-10,-3,7,7,10,-4,5,-3,4,-3,-2], dtype = "uint16")#candidate|9227|(60,)|const|uint16
call_9226 = relay.TupleGetItem(func_5632_call(relay.reshape(const_9227.astype('uint16'), [60,])), 0)
call_9228 = relay.TupleGetItem(func_5635_call(relay.reshape(const_9227.astype('uint16'), [60,])), 0)
func_4736_call = mod.get_global_var('func_4736')
func_4739_call = mutated_mod.get_global_var('func_4739')
var_9232 = relay.var("var_9232", dtype = "float64", shape = (168, 4))#candidate|9232|(168, 4)|var|float64
call_9231 = relay.TupleGetItem(func_4736_call(relay.reshape(var_9232.astype('float64'), [336, 2])), 4)
call_9233 = relay.TupleGetItem(func_4739_call(relay.reshape(var_9232.astype('float64'), [336, 2])), 4)
output = relay.Tuple([call_9176,call_9202,call_9213,const_9214,call_9226,const_9227,call_9231,var_9232,])
output2 = relay.Tuple([call_9177,call_9203,call_9215,const_9214,call_9228,const_9227,call_9233,var_9232,])
func_9242 = relay.Function([var_9232,], output)
mod['func_9242'] = func_9242
mod = relay.transform.InferType()(mod)
var_9243 = relay.var("var_9243", dtype = "float64", shape = (168, 4))#candidate|9243|(168, 4)|var|float64
output = func_9242(var_9243)
func_9244 = relay.Function([var_9243], output)
mutated_mod['func_9244'] = func_9244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2181_call = mod.get_global_var('func_2181')
func_2183_call = mutated_mod.get_global_var('func_2183')
call_9253 = func_2181_call()
call_9254 = func_2181_call()
output = relay.Tuple([call_9253,])
output2 = relay.Tuple([call_9254,])
func_9261 = relay.Function([], output)
mod['func_9261'] = func_9261
mod = relay.transform.InferType()(mod)
output = func_9261()
func_9262 = relay.Function([], output)
mutated_mod['func_9262'] = func_9262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1726_call = mod.get_global_var('func_1726')
func_1728_call = mutated_mod.get_global_var('func_1728')
call_9267 = func_1726_call()
call_9268 = func_1726_call()
output = call_9267
output2 = call_9268
func_9269 = relay.Function([], output)
mod['func_9269'] = func_9269
mod = relay.transform.InferType()(mod)
mutated_mod['func_9269'] = func_9269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9269_call = mutated_mod.get_global_var('func_9269')
call_9270 = func_9269_call()
output = call_9270
func_9271 = relay.Function([], output)
mutated_mod['func_9271'] = func_9271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7002_call = mod.get_global_var('func_7002')
func_7004_call = mutated_mod.get_global_var('func_7004')
call_9312 = relay.TupleGetItem(func_7002_call(), 1)
call_9313 = relay.TupleGetItem(func_7004_call(), 1)
func_561_call = mod.get_global_var('func_561')
func_564_call = mutated_mod.get_global_var('func_564')
const_9315 = relay.const([-1.912249,-9.765927,-3.720664,-3.191746,2.340371,-0.154610,-4.008076,7.102547,2.717607,-8.037945,-4.266147,2.294925,6.647103,9.467382,2.958710,-5.808226,-1.170422,-5.391615,2.607416,-4.926058,1.792313,4.302837,-1.329281,7.471481,-7.394564,1.762612,-0.626350,5.450611,9.949232,2.129418,-8.968097,-8.840966,-3.214880,0.294650,-3.591460,2.162685,5.925285,0.691846,6.925446,3.162307,-5.590532,-1.313036,9.156368,6.483950,2.378706,9.817650,-0.107284,-0.805784,7.402345,3.306257,3.344550,1.660189,6.846042,-1.748302,8.679571,-1.638785,-9.930010,5.078188,-9.675998,-6.541038,4.244785,-8.181810,9.211205,-3.928721,-3.623008,-2.381199,-4.630813,-9.245026,1.284714,3.619463,2.301325,-6.184840,-4.350847,6.181105,-2.628930,-0.677101,-5.505059,-8.654754,3.871044,-3.356982,-9.218797,6.731910,-7.040410,-9.384402,-1.195993,1.502746,6.800379,8.471049,8.755118,-6.797408,-6.237804,1.266757,5.246866,9.642679,-7.285782,0.893783,-6.260760,-5.874228,-4.640805,-2.383386,-9.995422,-1.291832,-3.200639,8.223251,4.400198], dtype = "float64")#candidate|9315|(105,)|const|float64
call_9314 = relay.TupleGetItem(func_561_call(relay.reshape(const_9315.astype('float64'), [7, 3, 5]), relay.reshape(const_9315.astype('float64'), [7, 3, 5]), ), 1)
call_9316 = relay.TupleGetItem(func_564_call(relay.reshape(const_9315.astype('float64'), [7, 3, 5]), relay.reshape(const_9315.astype('float64'), [7, 3, 5]), ), 1)
output = relay.Tuple([call_9312,call_9314,const_9315,])
output2 = relay.Tuple([call_9313,call_9316,const_9315,])
func_9333 = relay.Function([], output)
mod['func_9333'] = func_9333
mod = relay.transform.InferType()(mod)
mutated_mod['func_9333'] = func_9333
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9333_call = mutated_mod.get_global_var('func_9333')
call_9334 = func_9333_call()
output = call_9334
func_9335 = relay.Function([], output)
mutated_mod['func_9335'] = func_9335
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3648_call = mod.get_global_var('func_3648')
func_3649_call = mutated_mod.get_global_var('func_3649')
call_9339 = func_3648_call()
call_9340 = func_3648_call()
func_6284_call = mod.get_global_var('func_6284')
func_6286_call = mutated_mod.get_global_var('func_6286')
call_9351 = relay.TupleGetItem(func_6284_call(), 0)
call_9352 = relay.TupleGetItem(func_6286_call(), 0)
func_6546_call = mod.get_global_var('func_6546')
func_6548_call = mutated_mod.get_global_var('func_6548')
call_9357 = relay.TupleGetItem(func_6546_call(), 0)
call_9358 = relay.TupleGetItem(func_6548_call(), 0)
func_7975_call = mod.get_global_var('func_7975')
func_7977_call = mutated_mod.get_global_var('func_7977')
call_9378 = relay.TupleGetItem(func_7975_call(), 0)
call_9379 = relay.TupleGetItem(func_7977_call(), 0)
output = relay.Tuple([call_9339,call_9351,call_9357,call_9378,])
output2 = relay.Tuple([call_9340,call_9352,call_9358,call_9379,])
func_9380 = relay.Function([], output)
mod['func_9380'] = func_9380
mod = relay.transform.InferType()(mod)
mutated_mod['func_9380'] = func_9380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9380_call = mutated_mod.get_global_var('func_9380')
call_9381 = func_9380_call()
output = call_9381
func_9382 = relay.Function([], output)
mutated_mod['func_9382'] = func_9382
mutated_mod = relay.transform.InferType()(mutated_mod)
func_438_call = mod.get_global_var('func_438')
func_439_call = mutated_mod.get_global_var('func_439')
call_9414 = func_438_call()
call_9415 = func_438_call()
output = call_9414
output2 = call_9415
func_9429 = relay.Function([], output)
mod['func_9429'] = func_9429
mod = relay.transform.InferType()(mod)
mutated_mod['func_9429'] = func_9429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9429_call = mutated_mod.get_global_var('func_9429')
call_9430 = func_9429_call()
output = call_9430
func_9431 = relay.Function([], output)
mutated_mod['func_9431'] = func_9431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1366_call = mod.get_global_var('func_1366')
func_1367_call = mutated_mod.get_global_var('func_1367')
call_9486 = relay.TupleGetItem(func_1366_call(), 4)
call_9487 = relay.TupleGetItem(func_1367_call(), 4)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_9501 = relay.TupleGetItem(func_261_call(), 0)
call_9502 = relay.TupleGetItem(func_263_call(), 0)
func_7672_call = mod.get_global_var('func_7672')
func_7674_call = mutated_mod.get_global_var('func_7674')
var_9506 = relay.var("var_9506", dtype = "float64", shape = (105,))#candidate|9506|(105,)|var|float64
call_9505 = relay.TupleGetItem(func_7672_call(relay.reshape(var_9506.astype('float64'), [21, 5])), 2)
call_9507 = relay.TupleGetItem(func_7674_call(relay.reshape(var_9506.astype('float64'), [21, 5])), 2)
output = relay.Tuple([call_9486,call_9501,call_9505,var_9506,])
output2 = relay.Tuple([call_9487,call_9502,call_9507,var_9506,])
func_9515 = relay.Function([var_9506,], output)
mod['func_9515'] = func_9515
mod = relay.transform.InferType()(mod)
var_9516 = relay.var("var_9516", dtype = "float64", shape = (105,))#candidate|9516|(105,)|var|float64
output = func_9515(var_9516)
func_9517 = relay.Function([var_9516], output)
mutated_mod['func_9517'] = func_9517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7874_call = mod.get_global_var('func_7874')
func_7875_call = mutated_mod.get_global_var('func_7875')
call_9578 = func_7874_call()
call_9579 = func_7874_call()
output = call_9578
output2 = call_9579
func_9583 = relay.Function([], output)
mod['func_9583'] = func_9583
mod = relay.transform.InferType()(mod)
mutated_mod['func_9583'] = func_9583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9583_call = mutated_mod.get_global_var('func_9583')
call_9584 = func_9583_call()
output = call_9584
func_9585 = relay.Function([], output)
mutated_mod['func_9585'] = func_9585
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9261_call = mod.get_global_var('func_9261')
func_9262_call = mutated_mod.get_global_var('func_9262')
call_9588 = relay.TupleGetItem(func_9261_call(), 0)
call_9589 = relay.TupleGetItem(func_9262_call(), 0)
func_5567_call = mod.get_global_var('func_5567')
func_5568_call = mutated_mod.get_global_var('func_5568')
call_9662 = relay.TupleGetItem(func_5567_call(), 0)
call_9663 = relay.TupleGetItem(func_5568_call(), 0)
func_6926_call = mod.get_global_var('func_6926')
func_6927_call = mutated_mod.get_global_var('func_6927')
call_9665 = func_6926_call()
call_9666 = func_6926_call()
output = relay.Tuple([call_9588,call_9662,call_9665,])
output2 = relay.Tuple([call_9589,call_9663,call_9666,])
func_9689 = relay.Function([], output)
mod['func_9689'] = func_9689
mod = relay.transform.InferType()(mod)
output = func_9689()
func_9690 = relay.Function([], output)
mutated_mod['func_9690'] = func_9690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7339_call = mod.get_global_var('func_7339')
func_7341_call = mutated_mod.get_global_var('func_7341')
call_9715 = relay.TupleGetItem(func_7339_call(), 0)
call_9716 = relay.TupleGetItem(func_7341_call(), 0)
func_5609_call = mod.get_global_var('func_5609')
func_5610_call = mutated_mod.get_global_var('func_5610')
call_9719 = relay.TupleGetItem(func_5609_call(), 1)
call_9720 = relay.TupleGetItem(func_5610_call(), 1)
output = relay.Tuple([call_9715,call_9719,])
output2 = relay.Tuple([call_9716,call_9720,])
func_9725 = relay.Function([], output)
mod['func_9725'] = func_9725
mod = relay.transform.InferType()(mod)
mutated_mod['func_9725'] = func_9725
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9725_call = mutated_mod.get_global_var('func_9725')
call_9726 = func_9725_call()
output = call_9726
func_9727 = relay.Function([], output)
mutated_mod['func_9727'] = func_9727
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4219_call = mod.get_global_var('func_4219')
func_4221_call = mutated_mod.get_global_var('func_4221')
call_9802 = relay.TupleGetItem(func_4219_call(), 1)
call_9803 = relay.TupleGetItem(func_4221_call(), 1)
func_6036_call = mod.get_global_var('func_6036')
func_6038_call = mutated_mod.get_global_var('func_6038')
var_9805 = relay.var("var_9805", dtype = "bool", shape = (686,))#candidate|9805|(686,)|var|bool
call_9804 = relay.TupleGetItem(func_6036_call(relay.reshape(var_9805.astype('bool'), [686,])), 0)
call_9806 = relay.TupleGetItem(func_6038_call(relay.reshape(var_9805.astype('bool'), [686,])), 0)
output = relay.Tuple([call_9802,call_9804,var_9805,])
output2 = relay.Tuple([call_9803,call_9806,var_9805,])
func_9815 = relay.Function([var_9805,], output)
mod['func_9815'] = func_9815
mod = relay.transform.InferType()(mod)
var_9816 = relay.var("var_9816", dtype = "bool", shape = (686,))#candidate|9816|(686,)|var|bool
output = func_9815(var_9816)
func_9817 = relay.Function([var_9816], output)
mutated_mod['func_9817'] = func_9817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9333_call = mod.get_global_var('func_9333')
func_9335_call = mutated_mod.get_global_var('func_9335')
call_9851 = relay.TupleGetItem(func_9333_call(), 1)
call_9852 = relay.TupleGetItem(func_9335_call(), 1)
func_5446_call = mod.get_global_var('func_5446')
func_5449_call = mutated_mod.get_global_var('func_5449')
var_9861 = relay.var("var_9861", dtype = "uint16", shape = (60,))#candidate|9861|(60,)|var|uint16
call_9860 = relay.TupleGetItem(func_5446_call(relay.reshape(call_9851.astype('float64'), [7, 15]), relay.reshape(var_9861.astype('uint16'), [60,]), ), 7)
call_9862 = relay.TupleGetItem(func_5449_call(relay.reshape(call_9851.astype('float64'), [7, 15]), relay.reshape(var_9861.astype('uint16'), [60,]), ), 7)
func_438_call = mod.get_global_var('func_438')
func_439_call = mutated_mod.get_global_var('func_439')
call_9866 = func_438_call()
call_9867 = func_438_call()
func_1648_call = mod.get_global_var('func_1648')
func_1650_call = mutated_mod.get_global_var('func_1650')
call_9868 = func_1648_call()
call_9869 = func_1648_call()
output = relay.Tuple([call_9851,call_9860,var_9861,call_9866,call_9868,])
output2 = relay.Tuple([call_9852,call_9862,var_9861,call_9867,call_9869,])
func_9871 = relay.Function([var_9861,], output)
mod['func_9871'] = func_9871
mod = relay.transform.InferType()(mod)
mutated_mod['func_9871'] = func_9871
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9872 = relay.var("var_9872", dtype = "uint16", shape = (60,))#candidate|9872|(60,)|var|uint16
func_9871_call = mutated_mod.get_global_var('func_9871')
call_9873 = func_9871_call(var_9872)
output = call_9873
func_9874 = relay.Function([var_9872], output)
mutated_mod['func_9874'] = func_9874
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6546_call = mod.get_global_var('func_6546')
func_6548_call = mutated_mod.get_global_var('func_6548')
call_9995 = relay.TupleGetItem(func_6546_call(), 0)
call_9996 = relay.TupleGetItem(func_6548_call(), 0)
func_5446_call = mod.get_global_var('func_5446')
func_5449_call = mutated_mod.get_global_var('func_5449')
var_9998 = relay.var("var_9998", dtype = "float64", shape = (1, 105))#candidate|9998|(1, 105)|var|float64
var_9999 = relay.var("var_9999", dtype = "uint16", shape = (60,))#candidate|9999|(60,)|var|uint16
call_9997 = relay.TupleGetItem(func_5446_call(relay.reshape(var_9998.astype('float64'), [7, 15]), relay.reshape(var_9999.astype('uint16'), [60,]), ), 6)
call_10000 = relay.TupleGetItem(func_5449_call(relay.reshape(var_9998.astype('float64'), [7, 15]), relay.reshape(var_9999.astype('uint16'), [60,]), ), 6)
func_3864_call = mod.get_global_var('func_3864')
func_3865_call = mutated_mod.get_global_var('func_3865')
call_10004 = relay.TupleGetItem(func_3864_call(), 0)
call_10005 = relay.TupleGetItem(func_3865_call(), 0)
var_10006 = relay.var("var_10006", dtype = "float64", shape = (14, 105))#candidate|10006|(14, 105)|var|float64
bop_10007 = relay.minimum(var_9998.astype('uint16'), var_10006.astype('uint16')) # shape=(14, 105)
output = relay.Tuple([call_9995,call_9997,var_9999,call_10004,bop_10007,])
output2 = relay.Tuple([call_9996,call_10000,var_9999,call_10005,bop_10007,])
func_10012 = relay.Function([var_9998,var_9999,var_10006,], output)
mod['func_10012'] = func_10012
mod = relay.transform.InferType()(mod)
var_10013 = relay.var("var_10013", dtype = "float64", shape = (1, 105))#candidate|10013|(1, 105)|var|float64
var_10014 = relay.var("var_10014", dtype = "uint16", shape = (60,))#candidate|10014|(60,)|var|uint16
var_10015 = relay.var("var_10015", dtype = "float64", shape = (14, 105))#candidate|10015|(14, 105)|var|float64
output = func_10012(var_10013,var_10014,var_10015,)
func_10016 = relay.Function([var_10013,var_10014,var_10015,], output)
mutated_mod['func_10016'] = func_10016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8397_call = mod.get_global_var('func_8397')
func_8398_call = mutated_mod.get_global_var('func_8398')
call_10129 = relay.TupleGetItem(func_8397_call(), 0)
call_10130 = relay.TupleGetItem(func_8398_call(), 0)
func_5734_call = mod.get_global_var('func_5734')
func_5736_call = mutated_mod.get_global_var('func_5736')
call_10140 = relay.TupleGetItem(func_5734_call(), 0)
call_10141 = relay.TupleGetItem(func_5736_call(), 0)
output = relay.Tuple([call_10129,call_10140,])
output2 = relay.Tuple([call_10130,call_10141,])
func_10160 = relay.Function([], output)
mod['func_10160'] = func_10160
mod = relay.transform.InferType()(mod)
output = func_10160()
func_10161 = relay.Function([], output)
mutated_mod['func_10161'] = func_10161
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9429_call = mod.get_global_var('func_9429')
func_9431_call = mutated_mod.get_global_var('func_9431')
call_10196 = func_9429_call()
call_10197 = func_9429_call()
output = call_10196
output2 = call_10197
func_10200 = relay.Function([], output)
mod['func_10200'] = func_10200
mod = relay.transform.InferType()(mod)
mutated_mod['func_10200'] = func_10200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10200_call = mutated_mod.get_global_var('func_10200')
call_10201 = func_10200_call()
output = call_10201
func_10202 = relay.Function([], output)
mutated_mod['func_10202'] = func_10202
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7794_call = mod.get_global_var('func_7794')
func_7795_call = mutated_mod.get_global_var('func_7795')
call_10269 = relay.TupleGetItem(func_7794_call(), 2)
call_10270 = relay.TupleGetItem(func_7795_call(), 2)
output = relay.Tuple([call_10269,])
output2 = relay.Tuple([call_10270,])
func_10283 = relay.Function([], output)
mod['func_10283'] = func_10283
mod = relay.transform.InferType()(mod)
mutated_mod['func_10283'] = func_10283
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10283_call = mutated_mod.get_global_var('func_10283')
call_10284 = func_10283_call()
output = call_10284
func_10285 = relay.Function([], output)
mutated_mod['func_10285'] = func_10285
mutated_mod = relay.transform.InferType()(mutated_mod)
func_261_call = mod.get_global_var('func_261')
func_263_call = mutated_mod.get_global_var('func_263')
call_10306 = relay.TupleGetItem(func_261_call(), 0)
call_10307 = relay.TupleGetItem(func_263_call(), 0)
func_4127_call = mod.get_global_var('func_4127')
func_4128_call = mutated_mod.get_global_var('func_4128')
call_10332 = relay.TupleGetItem(func_4127_call(), 0)
call_10333 = relay.TupleGetItem(func_4128_call(), 0)
output = relay.Tuple([call_10306,call_10332,])
output2 = relay.Tuple([call_10307,call_10333,])
func_10338 = relay.Function([], output)
mod['func_10338'] = func_10338
mod = relay.transform.InferType()(mod)
mutated_mod['func_10338'] = func_10338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10338_call = mutated_mod.get_global_var('func_10338')
call_10339 = func_10338_call()
output = call_10339
func_10340 = relay.Function([], output)
mutated_mod['func_10340'] = func_10340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6658_call = mod.get_global_var('func_6658')
func_6659_call = mutated_mod.get_global_var('func_6659')
call_10357 = relay.TupleGetItem(func_6658_call(), 0)
call_10358 = relay.TupleGetItem(func_6659_call(), 0)
output = relay.Tuple([call_10357,])
output2 = relay.Tuple([call_10358,])
func_10371 = relay.Function([], output)
mod['func_10371'] = func_10371
mod = relay.transform.InferType()(mod)
output = func_10371()
func_10372 = relay.Function([], output)
mutated_mod['func_10372'] = func_10372
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7794_call = mod.get_global_var('func_7794')
func_7795_call = mutated_mod.get_global_var('func_7795')
call_10375 = relay.TupleGetItem(func_7794_call(), 1)
call_10376 = relay.TupleGetItem(func_7795_call(), 1)
output = relay.Tuple([call_10375,])
output2 = relay.Tuple([call_10376,])
func_10441 = relay.Function([], output)
mod['func_10441'] = func_10441
mod = relay.transform.InferType()(mod)
output = func_10441()
func_10442 = relay.Function([], output)
mutated_mod['func_10442'] = func_10442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8610_call = mod.get_global_var('func_8610')
func_8611_call = mutated_mod.get_global_var('func_8611')
call_10483 = func_8610_call()
call_10484 = func_8610_call()
func_4882_call = mod.get_global_var('func_4882')
func_4883_call = mutated_mod.get_global_var('func_4883')
call_10516 = relay.TupleGetItem(func_4882_call(), 0)
call_10517 = relay.TupleGetItem(func_4883_call(), 0)
func_9583_call = mod.get_global_var('func_9583')
func_9585_call = mutated_mod.get_global_var('func_9585')
call_10519 = func_9583_call()
call_10520 = func_9583_call()
output = relay.Tuple([call_10483,call_10516,call_10519,])
output2 = relay.Tuple([call_10484,call_10517,call_10520,])
func_10534 = relay.Function([], output)
mod['func_10534'] = func_10534
mod = relay.transform.InferType()(mod)
output = func_10534()
func_10535 = relay.Function([], output)
mutated_mod['func_10535'] = func_10535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4219_call = mod.get_global_var('func_4219')
func_4221_call = mutated_mod.get_global_var('func_4221')
call_10611 = relay.TupleGetItem(func_4219_call(), 0)
call_10612 = relay.TupleGetItem(func_4221_call(), 0)
output = call_10611
output2 = call_10612
func_10632 = relay.Function([], output)
mod['func_10632'] = func_10632
mod = relay.transform.InferType()(mod)
output = func_10632()
func_10633 = relay.Function([], output)
mutated_mod['func_10633'] = func_10633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5567_call = mod.get_global_var('func_5567')
func_5568_call = mutated_mod.get_global_var('func_5568')
call_10679 = relay.TupleGetItem(func_5567_call(), 0)
call_10680 = relay.TupleGetItem(func_5568_call(), 0)
output = relay.Tuple([call_10679,])
output2 = relay.Tuple([call_10680,])
func_10711 = relay.Function([], output)
mod['func_10711'] = func_10711
mod = relay.transform.InferType()(mod)
output = func_10711()
func_10712 = relay.Function([], output)
mutated_mod['func_10712'] = func_10712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6406_call = mod.get_global_var('func_6406')
func_6407_call = mutated_mod.get_global_var('func_6407')
call_10713 = relay.TupleGetItem(func_6406_call(), 1)
call_10714 = relay.TupleGetItem(func_6407_call(), 1)
output = relay.Tuple([call_10713,])
output2 = relay.Tuple([call_10714,])
func_10715 = relay.Function([], output)
mod['func_10715'] = func_10715
mod = relay.transform.InferType()(mod)
mutated_mod['func_10715'] = func_10715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10715_call = mutated_mod.get_global_var('func_10715')
call_10716 = func_10715_call()
output = call_10716
func_10717 = relay.Function([], output)
mutated_mod['func_10717'] = func_10717
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10749 = relay.var("var_10749", dtype = "uint16", shape = (11, 7, 8))#candidate|10749|(11, 7, 8)|var|uint16
var_10750 = relay.var("var_10750", dtype = "uint16", shape = (11, 7, 8))#candidate|10750|(11, 7, 8)|var|uint16
bop_10751 = relay.bitwise_and(var_10749.astype('uint16'), relay.reshape(var_10750.astype('uint16'), relay.shape_of(var_10749))) # shape=(11, 7, 8)
output = bop_10751
output2 = bop_10751
func_10763 = relay.Function([var_10749,var_10750,], output)
mod['func_10763'] = func_10763
mod = relay.transform.InferType()(mod)
mutated_mod['func_10763'] = func_10763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10763_call = mutated_mod.get_global_var('func_10763')
var_10765 = relay.var("var_10765", dtype = "uint16", shape = (11, 7, 8))#candidate|10765|(11, 7, 8)|var|uint16
var_10766 = relay.var("var_10766", dtype = "uint16", shape = (11, 7, 8))#candidate|10766|(11, 7, 8)|var|uint16
call_10764 = func_10763_call(var_10765,var_10766,)
output = call_10764
func_10767 = relay.Function([var_10765,var_10766,], output)
mutated_mod['func_10767'] = func_10767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8995_call = mod.get_global_var('func_8995')
func_8996_call = mutated_mod.get_global_var('func_8996')
call_10779 = relay.TupleGetItem(func_8995_call(), 2)
call_10780 = relay.TupleGetItem(func_8996_call(), 2)
output = relay.Tuple([call_10779,])
output2 = relay.Tuple([call_10780,])
func_10798 = relay.Function([], output)
mod['func_10798'] = func_10798
mod = relay.transform.InferType()(mod)
mutated_mod['func_10798'] = func_10798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10798_call = mutated_mod.get_global_var('func_10798')
call_10799 = func_10798_call()
output = call_10799
func_10800 = relay.Function([], output)
mutated_mod['func_10800'] = func_10800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6047_call = mod.get_global_var('func_6047')
func_6048_call = mutated_mod.get_global_var('func_6048')
call_10906 = func_6047_call()
call_10907 = func_6047_call()
var_10928 = relay.var("var_10928", dtype = "float64", shape = (21, 5))#candidate|10928|(21, 5)|var|float64
bop_10929 = relay.greater_equal(call_10906.astype('bool'), relay.reshape(var_10928.astype('bool'), relay.shape_of(call_10906))) # shape=(21, 5)
bop_10932 = relay.greater_equal(call_10907.astype('bool'), relay.reshape(var_10928.astype('bool'), relay.shape_of(call_10907))) # shape=(21, 5)
func_6720_call = mod.get_global_var('func_6720')
func_6722_call = mutated_mod.get_global_var('func_6722')
call_10947 = relay.TupleGetItem(func_6720_call(), 0)
call_10948 = relay.TupleGetItem(func_6722_call(), 0)
output = relay.Tuple([bop_10929,call_10947,])
output2 = relay.Tuple([bop_10932,call_10948,])
func_10954 = relay.Function([var_10928,], output)
mod['func_10954'] = func_10954
mod = relay.transform.InferType()(mod)
var_10955 = relay.var("var_10955", dtype = "float64", shape = (21, 5))#candidate|10955|(21, 5)|var|float64
output = func_10954(var_10955)
func_10956 = relay.Function([var_10955], output)
mutated_mod['func_10956'] = func_10956
mutated_mod = relay.transform.InferType()(mutated_mod)
func_438_call = mod.get_global_var('func_438')
func_439_call = mutated_mod.get_global_var('func_439')
call_11008 = func_438_call()
call_11009 = func_438_call()
func_8138_call = mod.get_global_var('func_8138')
func_8140_call = mutated_mod.get_global_var('func_8140')
call_11010 = relay.TupleGetItem(func_8138_call(), 2)
call_11011 = relay.TupleGetItem(func_8140_call(), 2)
var_11036 = relay.var("var_11036", dtype = "float32", shape = (7, 7, 2))#candidate|11036|(7, 7, 2)|var|float32
bop_11037 = relay.multiply(call_11010.astype('int16'), relay.reshape(var_11036.astype('int16'), relay.shape_of(call_11010))) # shape=(7, 7, 2)
bop_11040 = relay.multiply(call_11011.astype('int16'), relay.reshape(var_11036.astype('int16'), relay.shape_of(call_11011))) # shape=(7, 7, 2)
func_6270_call = mod.get_global_var('func_6270')
func_6272_call = mutated_mod.get_global_var('func_6272')
var_11045 = relay.var("var_11045", dtype = "float64", shape = (105, 1))#candidate|11045|(105, 1)|var|float64
call_11044 = relay.TupleGetItem(func_6270_call(relay.reshape(var_11045.astype('float64'), [105,])), 3)
call_11046 = relay.TupleGetItem(func_6272_call(relay.reshape(var_11045.astype('float64'), [105,])), 3)
output = relay.Tuple([call_11008,bop_11037,call_11044,var_11045,])
output2 = relay.Tuple([call_11009,bop_11040,call_11046,var_11045,])
func_11049 = relay.Function([var_11036,var_11045,], output)
mod['func_11049'] = func_11049
mod = relay.transform.InferType()(mod)
var_11050 = relay.var("var_11050", dtype = "float32", shape = (7, 7, 2))#candidate|11050|(7, 7, 2)|var|float32
var_11051 = relay.var("var_11051", dtype = "float64", shape = (105, 1))#candidate|11051|(105, 1)|var|float64
output = func_11049(var_11050,var_11051,)
func_11052 = relay.Function([var_11050,var_11051,], output)
mutated_mod['func_11052'] = func_11052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1904_call = mod.get_global_var('func_1904')
func_1906_call = mutated_mod.get_global_var('func_1906')
call_11059 = relay.TupleGetItem(func_1904_call(), 2)
call_11060 = relay.TupleGetItem(func_1906_call(), 2)
output = call_11059
output2 = call_11060
func_11066 = relay.Function([], output)
mod['func_11066'] = func_11066
mod = relay.transform.InferType()(mod)
mutated_mod['func_11066'] = func_11066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11066_call = mutated_mod.get_global_var('func_11066')
call_11067 = func_11066_call()
output = call_11067
func_11068 = relay.Function([], output)
mutated_mod['func_11068'] = func_11068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2320_call = mod.get_global_var('func_2320')
func_2322_call = mutated_mod.get_global_var('func_2322')
call_11069 = func_2320_call()
call_11070 = func_2320_call()
func_4882_call = mod.get_global_var('func_4882')
func_4883_call = mutated_mod.get_global_var('func_4883')
call_11081 = relay.TupleGetItem(func_4882_call(), 0)
call_11082 = relay.TupleGetItem(func_4883_call(), 0)
func_6106_call = mod.get_global_var('func_6106')
func_6108_call = mutated_mod.get_global_var('func_6108')
call_11094 = func_6106_call()
call_11095 = func_6106_call()
func_1726_call = mod.get_global_var('func_1726')
func_1728_call = mutated_mod.get_global_var('func_1728')
call_11101 = func_1726_call()
call_11102 = func_1726_call()
func_6720_call = mod.get_global_var('func_6720')
func_6722_call = mutated_mod.get_global_var('func_6722')
call_11112 = relay.TupleGetItem(func_6720_call(), 0)
call_11113 = relay.TupleGetItem(func_6722_call(), 0)
output = relay.Tuple([call_11069,call_11081,call_11094,call_11101,call_11112,])
output2 = relay.Tuple([call_11070,call_11082,call_11095,call_11102,call_11113,])
func_11140 = relay.Function([], output)
mod['func_11140'] = func_11140
mod = relay.transform.InferType()(mod)
mutated_mod['func_11140'] = func_11140
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11140_call = mutated_mod.get_global_var('func_11140')
call_11141 = func_11140_call()
output = call_11141
func_11142 = relay.Function([], output)
mutated_mod['func_11142'] = func_11142
mutated_mod = relay.transform.InferType()(mutated_mod)
const_11179 = relay.const([[[-1.177932,-7.746485,-7.304545,1.453546,2.134621,-2.645395,4.392234],[3.095484,-9.569542,-1.476514,4.390978,6.540201,-6.924445,-3.504772],[7.230017,-0.824196,6.724574,-0.732379,1.161008,8.426764,-3.883127],[-9.400369,2.932097,-6.167526,-6.479002,3.757875,4.873589,8.547138],[-6.077655,1.582266,9.552732,5.553935,0.549521,-4.456717,-0.948675],[6.982478,3.187272,-7.860873,5.991614,-4.022556,-9.400990,0.149323]],[[-2.349522,0.902041,1.663161,-0.199563,-4.973086,1.257211,-0.646938],[-5.340038,4.381245,8.595359,-4.892898,2.013438,-4.729730,0.811129],[-4.431016,5.742662,-6.861537,1.757270,3.034269,-5.193503,-8.335255],[6.352454,-6.975539,7.480200,2.030292,-7.997650,-4.647811,-7.824598],[-2.549677,1.527944,-5.905706,3.817763,1.090999,-4.146038,8.915505],[-1.267337,2.112272,-4.184665,-9.389708,0.463401,-0.694090,0.293815]],[[-0.697705,-0.770067,1.522136,1.360515,-4.777833,-0.540625,1.115815],[-5.523505,-6.754127,-0.092598,1.083761,3.522157,-3.243488,9.353267],[-4.922402,-0.191949,-2.399428,8.194729,-4.550427,-5.047659,-3.758252],[1.501636,9.620353,-3.799065,-8.462509,6.565953,3.000296,9.636149],[-4.875142,-4.338452,0.890597,4.896043,4.826299,-8.296065,8.638005],[-8.853128,1.561378,2.963803,-4.023415,-5.390518,3.810449,-3.274665]],[[-4.976236,-2.453224,-2.301155,-6.021334,2.472020,-0.089155,-6.075194],[3.557484,1.358921,5.981440,7.809701,5.076369,-5.214588,-3.994997],[-2.883262,-4.487631,2.430917,4.714639,-7.538590,2.129088,8.870763],[-6.340831,-5.200869,7.119053,-2.597473,5.239946,2.587700,8.434435],[-1.316932,3.601808,-6.014841,-8.162327,3.180690,6.547923,5.466647],[8.489360,-1.902605,-4.687203,9.240542,-4.691069,7.056858,8.416484]],[[5.102041,-5.829637,9.215280,-6.142615,-8.307817,0.687756,-5.169438],[5.470333,3.499281,-6.056936,-0.528884,7.659959,-5.973666,8.068116],[1.705519,-0.952669,2.043989,-9.875473,3.368865,-7.245260,4.100179],[4.014638,6.722609,5.707478,3.199773,-8.552852,3.298128,-9.836624],[-7.111225,2.211693,-3.039303,-3.719510,-9.275134,-3.687093,8.877823],[9.557361,-5.103201,-9.431001,3.176524,9.105648,7.101354,7.882448]],[[9.756464,-2.767017,4.334199,2.764325,2.302896,-4.224400,-7.323243],[7.774518,0.017385,7.374593,4.897005,3.324045,7.955354,-1.359835],[2.606579,0.128592,4.692051,-1.806822,9.235871,-5.735380,0.335826],[1.298872,-3.973184,1.945449,5.558213,1.249856,-3.705543,-8.792607],[8.469754,-0.440771,-4.904048,5.302348,1.692613,-3.737751,3.215209],[7.624140,8.382614,6.710035,-0.660773,-9.859274,1.044854,-2.450521]],[[-9.491586,5.499986,5.205703,-9.077394,-2.606941,0.192972,7.847629],[-9.051663,1.888670,3.613686,-9.154190,-0.998903,1.310723,1.648163],[-1.305272,-1.118914,-6.164533,8.589790,7.029205,9.310877,8.052868],[8.525566,-7.783246,-9.355561,-2.157107,9.949126,-0.067893,2.023304],[-7.001176,-6.620416,-5.876850,4.335466,-8.373538,4.984371,4.122698],[6.153686,0.269207,3.209787,6.223723,3.563202,-4.715528,-2.716549]],[[-5.948718,-3.289162,-5.114795,-0.541365,-4.967809,6.715059,-6.959839],[-7.567234,2.233608,-6.179526,9.707201,8.645038,5.173107,-0.548368],[4.121061,-9.342536,-2.218671,-7.893371,7.188125,1.137469,-8.774748],[2.865764,7.825570,-4.002209,4.818746,-7.644302,4.637403,7.572562],[-3.848332,-1.517238,5.926273,-7.857982,8.706868,-5.759057,3.330978],[-0.194982,6.191973,-1.229870,-2.757295,8.874812,1.772659,-0.346251]],[[4.531642,-7.365648,7.855663,1.592034,2.599296,-1.403383,-1.941087],[-5.299227,-8.794967,-1.183579,-7.435635,3.695358,3.034690,-9.699345],[-5.472210,6.721834,6.086254,1.769169,-9.551420,6.939301,-9.175560],[5.746948,-4.266577,-3.908199,-3.312560,-4.531814,9.719723,3.926899],[5.900393,-2.959643,-0.965297,2.597115,2.228065,-5.745050,-9.436897],[3.559745,5.298503,3.925794,-3.834476,6.468619,-4.083988,2.638189]],[[1.066537,2.700425,5.815188,-3.360498,3.806322,9.588205,-7.332284],[4.993297,5.771632,-0.594445,8.868273,-5.404918,1.428732,-1.604820],[-9.882249,-9.932908,9.964256,-0.474756,8.076220,-1.063508,-6.174705],[9.399110,-8.496038,8.814006,6.743942,-0.084809,-1.600585,2.027645],[-8.946426,6.691679,0.497817,-0.774280,3.957155,7.372316,3.965708],[-5.803846,4.522901,0.290682,-2.121912,4.511004,-6.707566,-2.533458]]], dtype = "float64")#candidate|11179|(10, 6, 7)|const|float64
uop_11180 = relay.sinh(const_11179.astype('float64')) # shape=(10, 6, 7)
output = relay.Tuple([uop_11180,])
output2 = relay.Tuple([uop_11180,])
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
