import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_62 = relay.var("var_62", dtype = "uint8", shape = ())#candidate|62|()|var|uint8
var_63 = relay.var("var_63", dtype = "uint8", shape = (10, 8, 14))#candidate|63|(10, 8, 14)|var|uint8
bop_64 = relay.logical_xor(var_62.astype('uint8'), var_63.astype('uint8')) # shape=(10, 8, 14)
bop_102 = relay.not_equal(var_63.astype('bool'), relay.reshape(bop_64.astype('bool'), relay.shape_of(var_63))) # shape=(10, 8, 14)
uop_105 = relay.cosh(bop_64.astype('float32')) # shape=(10, 8, 14)
output = relay.Tuple([bop_102,uop_105,])
output2 = relay.Tuple([bop_102,uop_105,])
func_108 = relay.Function([var_62,var_63,], output)
mod['func_108'] = func_108
mod = relay.transform.InferType()(mod)
var_109 = relay.var("var_109", dtype = "uint8", shape = ())#candidate|109|()|var|uint8
var_110 = relay.var("var_110", dtype = "uint8", shape = (10, 8, 14))#candidate|110|(10, 8, 14)|var|uint8
output = func_108(var_109,var_110,)
func_111 = relay.Function([var_109,var_110,], output)
mutated_mod['func_111'] = func_111
mutated_mod = relay.transform.InferType()(mutated_mod)
const_186 = relay.const([[[False,False,False,False,False,False],[False,True,False,True,True,True],[False,True,False,False,True,False]],[[False,False,False,False,True,False],[False,True,False,True,False,True],[True,False,False,True,False,False]],[[True,False,False,True,True,True],[False,True,True,False,False,False],[True,False,False,True,False,True]],[[False,False,False,False,True,False],[True,True,False,True,False,False],[False,False,True,False,True,False]],[[True,False,False,False,False,False],[False,True,False,False,True,False],[True,True,True,False,True,False]],[[False,False,True,True,False,False],[True,False,False,False,False,True],[True,True,True,True,False,False]]], dtype = "bool")#candidate|186|(6, 3, 6)|const|bool
var_187 = relay.var("var_187", dtype = "bool", shape = (6, 3, 6))#candidate|187|(6, 3, 6)|var|bool
bop_188 = relay.logical_and(const_186.astype('bool'), relay.reshape(var_187.astype('bool'), relay.shape_of(const_186))) # shape=(6, 3, 6)
bop_198 = relay.bitwise_and(const_186.astype('uint64'), relay.reshape(bop_188.astype('uint64'), relay.shape_of(const_186))) # shape=(6, 3, 6)
bop_201 = relay.floor_mod(const_186.astype('float64'), relay.reshape(var_187.astype('float64'), relay.shape_of(const_186))) # shape=(6, 3, 6)
output = relay.Tuple([bop_198,bop_201,])
output2 = relay.Tuple([bop_198,bop_201,])
func_213 = relay.Function([var_187,], output)
mod['func_213'] = func_213
mod = relay.transform.InferType()(mod)
mutated_mod['func_213'] = func_213
mutated_mod = relay.transform.InferType()(mutated_mod)
var_214 = relay.var("var_214", dtype = "bool", shape = (6, 3, 6))#candidate|214|(6, 3, 6)|var|bool
func_213_call = mutated_mod.get_global_var('func_213')
call_215 = func_213_call(var_214)
output = call_215
func_216 = relay.Function([var_214], output)
mutated_mod['func_216'] = func_216
mutated_mod = relay.transform.InferType()(mutated_mod)
const_354 = relay.const([[[-4.758352,0.267743,7.711035,5.034872,-4.377599,-3.428026,6.123934,-7.368406,9.767825],[-7.568902,3.872951,-9.859197,0.971714,-9.687152,3.872505,-3.630701,-5.764837,-1.545467],[4.271966,8.327305,5.483942,6.894511,9.719083,-7.863065,3.559519,-7.413094,5.144696],[-1.763710,9.550609,2.045740,-7.616340,-0.032776,-2.441539,-3.439715,7.304173,6.968062],[2.017569,1.099784,6.685771,8.690680,-3.144280,2.306695,-7.870664,-3.227144,1.380290],[-0.346935,-6.040105,-1.942273,9.823039,-3.627328,-7.245228,8.357953,-3.718506,-7.518642]],[[-0.650215,-4.447672,6.804936,-5.887878,1.060088,5.358302,1.371316,-8.872601,6.137722],[-6.278807,5.041228,7.568786,-4.900832,8.061749,2.280387,-9.592035,3.771899,-0.032860],[7.003046,-3.010374,3.080756,9.344796,4.846726,-0.901923,-9.600191,5.604169,-8.692672],[0.858699,-9.595020,4.069366,-8.864343,1.107109,4.921644,6.327483,1.444433,5.967195],[8.995579,6.111730,4.993667,6.396269,-2.362771,5.166424,0.589595,8.850320,-8.893590],[5.000281,0.431725,-1.132135,-0.718599,0.941899,-9.023132,9.351892,5.281362,-0.294705]]], dtype = "float64")#candidate|354|(2, 6, 9)|const|float64
uop_355 = relay.log2(const_354.astype('float64')) # shape=(2, 6, 9)
output = uop_355
output2 = uop_355
func_361 = relay.Function([], output)
mod['func_361'] = func_361
mod = relay.transform.InferType()(mod)
output = func_361()
func_362 = relay.Function([], output)
mutated_mod['func_362'] = func_362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_368 = func_361_call()
call_369 = func_361_call()
func_108_call = mod.get_global_var('func_108')
func_111_call = mutated_mod.get_global_var('func_111')
var_371 = relay.var("var_371", dtype = "uint8", shape = ())#candidate|371|()|var|uint8
var_372 = relay.var("var_372", dtype = "uint8", shape = (1120,))#candidate|372|(1120,)|var|uint8
call_370 = relay.TupleGetItem(func_108_call(relay.reshape(var_371.astype('uint8'), []), relay.reshape(var_372.astype('uint8'), [10, 8, 14]), ), 0)
call_373 = relay.TupleGetItem(func_111_call(relay.reshape(var_371.astype('uint8'), []), relay.reshape(var_372.astype('uint8'), [10, 8, 14]), ), 0)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_384 = func_361_call()
call_385 = func_361_call()
output = relay.Tuple([call_368,call_370,var_371,var_372,call_384,])
output2 = relay.Tuple([call_369,call_373,var_371,var_372,call_385,])
func_387 = relay.Function([var_371,var_372,], output)
mod['func_387'] = func_387
mod = relay.transform.InferType()(mod)
var_388 = relay.var("var_388", dtype = "uint8", shape = ())#candidate|388|()|var|uint8
var_389 = relay.var("var_389", dtype = "uint8", shape = (1120,))#candidate|389|(1120,)|var|uint8
output = func_387(var_388,var_389,)
func_390 = relay.Function([var_388,var_389,], output)
mutated_mod['func_390'] = func_390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_416 = func_361_call()
call_417 = func_361_call()
uop_418 = relay.asin(call_416.astype('float32')) # shape=(2, 6, 9)
uop_420 = relay.asin(call_417.astype('float32')) # shape=(2, 6, 9)
bop_423 = relay.right_shift(uop_418.astype('uint8'), relay.reshape(call_416.astype('uint8'), relay.shape_of(uop_418))) # shape=(2, 6, 9)
bop_426 = relay.right_shift(uop_420.astype('uint8'), relay.reshape(call_417.astype('uint8'), relay.shape_of(uop_420))) # shape=(2, 6, 9)
var_428 = relay.var("var_428", dtype = "float32", shape = (2, 6, 9))#candidate|428|(2, 6, 9)|var|float32
bop_429 = relay.add(uop_418.astype('uint8'), relay.reshape(var_428.astype('uint8'), relay.shape_of(uop_418))) # shape=(2, 6, 9)
bop_432 = relay.add(uop_420.astype('uint8'), relay.reshape(var_428.astype('uint8'), relay.shape_of(uop_420))) # shape=(2, 6, 9)
uop_436 = relay.cosh(bop_429.astype('float64')) # shape=(2, 6, 9)
uop_438 = relay.cosh(bop_432.astype('float64')) # shape=(2, 6, 9)
bop_444 = relay.bitwise_and(uop_436.astype('int8'), relay.reshape(bop_429.astype('int8'), relay.shape_of(uop_436))) # shape=(2, 6, 9)
bop_447 = relay.bitwise_and(uop_438.astype('int8'), relay.reshape(bop_432.astype('int8'), relay.shape_of(uop_438))) # shape=(2, 6, 9)
bop_463 = relay.not_equal(uop_436.astype('bool'), relay.reshape(bop_444.astype('bool'), relay.shape_of(uop_436))) # shape=(2, 6, 9)
bop_466 = relay.not_equal(uop_438.astype('bool'), relay.reshape(bop_447.astype('bool'), relay.shape_of(uop_438))) # shape=(2, 6, 9)
bop_472 = relay.logical_and(bop_463.astype('bool'), relay.reshape(bop_444.astype('bool'), relay.shape_of(bop_463))) # shape=(2, 6, 9)
bop_475 = relay.logical_and(bop_466.astype('bool'), relay.reshape(bop_447.astype('bool'), relay.shape_of(bop_466))) # shape=(2, 6, 9)
func_108_call = mod.get_global_var('func_108')
func_111_call = mutated_mod.get_global_var('func_111')
const_483 = relay.const(-6, dtype = "uint8")#candidate|483|()|const|uint8
var_484 = relay.var("var_484", dtype = "uint8", shape = (1120,))#candidate|484|(1120,)|var|uint8
call_482 = relay.TupleGetItem(func_108_call(relay.reshape(const_483.astype('uint8'), []), relay.reshape(var_484.astype('uint8'), [10, 8, 14]), ), 1)
call_485 = relay.TupleGetItem(func_111_call(relay.reshape(const_483.astype('uint8'), []), relay.reshape(var_484.astype('uint8'), [10, 8, 14]), ), 1)
output = relay.Tuple([bop_423,bop_472,call_482,const_483,var_484,])
output2 = relay.Tuple([bop_426,bop_475,call_485,const_483,var_484,])
func_487 = relay.Function([var_428,var_484,], output)
mod['func_487'] = func_487
mod = relay.transform.InferType()(mod)
var_488 = relay.var("var_488", dtype = "float32", shape = (2, 6, 9))#candidate|488|(2, 6, 9)|var|float32
var_489 = relay.var("var_489", dtype = "uint8", shape = (1120,))#candidate|489|(1120,)|var|uint8
output = func_487(var_488,var_489,)
func_490 = relay.Function([var_488,var_489,], output)
mutated_mod['func_490'] = func_490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_495 = func_361_call()
call_496 = func_361_call()
var_514 = relay.var("var_514", dtype = "float64", shape = (2, 6, 9))#candidate|514|(2, 6, 9)|var|float64
bop_515 = relay.logical_xor(call_495.astype('uint16'), relay.reshape(var_514.astype('uint16'), relay.shape_of(call_495))) # shape=(2, 6, 9)
bop_518 = relay.logical_xor(call_496.astype('uint16'), relay.reshape(var_514.astype('uint16'), relay.shape_of(call_496))) # shape=(2, 6, 9)
bop_533 = relay.greater_equal(var_514.astype('bool'), relay.reshape(bop_515.astype('bool'), relay.shape_of(var_514))) # shape=(2, 6, 9)
bop_536 = relay.greater_equal(var_514.astype('bool'), relay.reshape(bop_518.astype('bool'), relay.shape_of(var_514))) # shape=(2, 6, 9)
var_540 = relay.var("var_540", dtype = "float64", shape = (2, 6, 9))#candidate|540|(2, 6, 9)|var|float64
bop_541 = relay.floor_mod(call_495.astype('float64'), relay.reshape(var_540.astype('float64'), relay.shape_of(call_495))) # shape=(2, 6, 9)
bop_544 = relay.floor_mod(call_496.astype('float64'), relay.reshape(var_540.astype('float64'), relay.shape_of(call_496))) # shape=(2, 6, 9)
func_387_call = mod.get_global_var('func_387')
func_390_call = mutated_mod.get_global_var('func_390')
const_561 = relay.const(-3, dtype = "uint8")#candidate|561|()|const|uint8
var_562 = relay.var("var_562", dtype = "uint8", shape = (4, 280))#candidate|562|(4, 280)|var|uint8
call_560 = relay.TupleGetItem(func_387_call(relay.reshape(const_561.astype('uint8'), []), relay.reshape(var_562.astype('uint8'), [1120,]), ), 1)
call_563 = relay.TupleGetItem(func_390_call(relay.reshape(const_561.astype('uint8'), []), relay.reshape(var_562.astype('uint8'), [1120,]), ), 1)
output = relay.Tuple([bop_533,bop_541,call_560,const_561,var_562,])
output2 = relay.Tuple([bop_536,bop_544,call_563,const_561,var_562,])
func_571 = relay.Function([var_514,var_540,var_562,], output)
mod['func_571'] = func_571
mod = relay.transform.InferType()(mod)
mutated_mod['func_571'] = func_571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_571_call = mutated_mod.get_global_var('func_571')
var_573 = relay.var("var_573", dtype = "float64", shape = (2, 6, 9))#candidate|573|(2, 6, 9)|var|float64
var_574 = relay.var("var_574", dtype = "float64", shape = (2, 6, 9))#candidate|574|(2, 6, 9)|var|float64
var_575 = relay.var("var_575", dtype = "uint8", shape = (4, 280))#candidate|575|(4, 280)|var|uint8
call_572 = func_571_call(var_573,var_574,var_575,)
output = call_572
func_576 = relay.Function([var_573,var_574,var_575,], output)
mutated_mod['func_576'] = func_576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_612 = func_361_call()
call_613 = func_361_call()
const_627 = relay.const([[[-6.426024,6.996043,-5.462836,5.442521,-7.123217,9.157517,-4.565530,6.235589,5.321267],[6.640835,-9.496880,6.304641,-2.503557,9.370676,-7.812683,-9.811866,-1.498258,-8.126287],[-6.341263,-1.558355,4.358546,-1.628982,-9.253855,-5.049649,-2.196381,3.806486,1.573257],[5.692159,2.979149,-1.469287,-6.905680,-1.534094,-0.758461,8.962970,-5.700341,6.277468],[6.961401,6.623264,5.523448,6.352751,-4.786976,-3.258008,-2.257705,8.167639,-1.894392],[4.806575,-0.579863,-8.676901,-2.443374,6.181651,9.349966,-0.045444,3.506625,-5.284819]],[[7.989439,-6.291961,-3.990906,0.579875,6.540491,-3.029312,-4.572216,-3.433824,-6.606936],[6.421167,-2.078526,3.569932,1.070490,6.893757,-9.049399,1.086433,7.377244,5.764819],[-6.253006,-9.846977,6.024878,-7.579384,-1.622242,-3.307804,8.970395,6.336915,0.509062],[9.771016,4.421895,8.368966,-1.511997,0.101846,-2.905970,-7.848135,-5.719517,-3.197156],[8.887857,5.519197,8.805328,-9.883144,-0.275941,0.255175,7.690164,-5.670053,7.397847],[-4.700516,0.809945,0.088500,-6.197231,-1.888393,4.496422,-0.323504,0.530522,-8.929582]]], dtype = "float64")#candidate|627|(2, 6, 9)|const|float64
bop_628 = relay.less(call_612.astype('bool'), relay.reshape(const_627.astype('bool'), relay.shape_of(call_612))) # shape=(2, 6, 9)
bop_631 = relay.less(call_613.astype('bool'), relay.reshape(const_627.astype('bool'), relay.shape_of(call_613))) # shape=(2, 6, 9)
func_487_call = mod.get_global_var('func_487')
func_490_call = mutated_mod.get_global_var('func_490')
var_639 = relay.var("var_639", dtype = "uint8", shape = (1120,))#candidate|639|(1120,)|var|uint8
call_638 = relay.TupleGetItem(func_487_call(relay.reshape(bop_628.astype('float32'), [2, 6, 9]), relay.reshape(var_639.astype('uint8'), [1120,]), ), 0)
call_640 = relay.TupleGetItem(func_490_call(relay.reshape(bop_628.astype('float32'), [2, 6, 9]), relay.reshape(var_639.astype('uint8'), [1120,]), ), 0)
func_213_call = mod.get_global_var('func_213')
func_216_call = mutated_mod.get_global_var('func_216')
call_641 = relay.TupleGetItem(func_213_call(relay.reshape(const_627.astype('bool'), [6, 3, 6])), 0)
call_642 = relay.TupleGetItem(func_216_call(relay.reshape(const_627.astype('bool'), [6, 3, 6])), 0)
output = relay.Tuple([bop_628,call_638,var_639,call_641,])
output2 = relay.Tuple([bop_631,call_640,var_639,call_642,])
func_644 = relay.Function([var_639,], output)
mod['func_644'] = func_644
mod = relay.transform.InferType()(mod)
var_645 = relay.var("var_645", dtype = "uint8", shape = (1120,))#candidate|645|(1120,)|var|uint8
output = func_644(var_645)
func_646 = relay.Function([var_645], output)
mutated_mod['func_646'] = func_646
mutated_mod = relay.transform.InferType()(mutated_mod)
var_697 = relay.var("var_697", dtype = "float32", shape = (13, 3, 3))#candidate|697|(13, 3, 3)|var|float32
var_698 = relay.var("var_698", dtype = "float32", shape = (13, 3, 3))#candidate|698|(13, 3, 3)|var|float32
bop_699 = relay.divide(var_697.astype('float32'), relay.reshape(var_698.astype('float32'), relay.shape_of(var_697))) # shape=(13, 3, 3)
func_387_call = mod.get_global_var('func_387')
func_390_call = mutated_mod.get_global_var('func_390')
var_708 = relay.var("var_708", dtype = "uint8", shape = ())#candidate|708|()|var|uint8
var_709 = relay.var("var_709", dtype = "uint8", shape = (560, 2))#candidate|709|(560, 2)|var|uint8
call_707 = relay.TupleGetItem(func_387_call(relay.reshape(var_708.astype('uint8'), []), relay.reshape(var_709.astype('uint8'), [1120,]), ), 3)
call_710 = relay.TupleGetItem(func_390_call(relay.reshape(var_708.astype('uint8'), []), relay.reshape(var_709.astype('uint8'), [1120,]), ), 3)
uop_728 = relay.log(call_707.astype('float32')) # shape=(1120,)
uop_730 = relay.log(call_710.astype('float32')) # shape=(1120,)
uop_738 = relay.sinh(uop_728.astype('float64')) # shape=(1120,)
uop_740 = relay.sinh(uop_730.astype('float64')) # shape=(1120,)
bop_743 = relay.right_shift(uop_738.astype('int16'), relay.reshape(uop_728.astype('int16'), relay.shape_of(uop_738))) # shape=(1120,)
bop_746 = relay.right_shift(uop_740.astype('int16'), relay.reshape(uop_730.astype('int16'), relay.shape_of(uop_740))) # shape=(1120,)
output = relay.Tuple([bop_699,var_708,var_709,bop_743,])
output2 = relay.Tuple([bop_699,var_708,var_709,bop_746,])
func_747 = relay.Function([var_697,var_698,var_708,var_709,], output)
mod['func_747'] = func_747
mod = relay.transform.InferType()(mod)
mutated_mod['func_747'] = func_747
mutated_mod = relay.transform.InferType()(mutated_mod)
func_747_call = mutated_mod.get_global_var('func_747')
var_749 = relay.var("var_749", dtype = "float32", shape = (13, 3, 3))#candidate|749|(13, 3, 3)|var|float32
var_750 = relay.var("var_750", dtype = "float32", shape = (13, 3, 3))#candidate|750|(13, 3, 3)|var|float32
var_751 = relay.var("var_751", dtype = "uint8", shape = ())#candidate|751|()|var|uint8
var_752 = relay.var("var_752", dtype = "uint8", shape = (560, 2))#candidate|752|(560, 2)|var|uint8
call_748 = func_747_call(var_749,var_750,var_751,var_752,)
output = call_748
func_753 = relay.Function([var_749,var_750,var_751,var_752,], output)
mutated_mod['func_753'] = func_753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_855 = func_361_call()
call_856 = func_361_call()
uop_869 = relay.atan(call_855.astype('float64')) # shape=(2, 6, 9)
uop_871 = relay.atan(call_856.astype('float64')) # shape=(2, 6, 9)
output = relay.Tuple([uop_869,])
output2 = relay.Tuple([uop_871,])
func_875 = relay.Function([], output)
mod['func_875'] = func_875
mod = relay.transform.InferType()(mod)
mutated_mod['func_875'] = func_875
mutated_mod = relay.transform.InferType()(mutated_mod)
func_875_call = mutated_mod.get_global_var('func_875')
call_876 = func_875_call()
output = call_876
func_877 = relay.Function([], output)
mutated_mod['func_877'] = func_877
mutated_mod = relay.transform.InferType()(mutated_mod)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_893 = func_361_call()
call_894 = func_361_call()
output = relay.Tuple([call_893,])
output2 = relay.Tuple([call_894,])
func_900 = relay.Function([], output)
mod['func_900'] = func_900
mod = relay.transform.InferType()(mod)
mutated_mod['func_900'] = func_900
mutated_mod = relay.transform.InferType()(mutated_mod)
func_900_call = mutated_mod.get_global_var('func_900')
call_901 = func_900_call()
output = call_901
func_902 = relay.Function([], output)
mutated_mod['func_902'] = func_902
mutated_mod = relay.transform.InferType()(mutated_mod)
var_903 = relay.var("var_903", dtype = "bool", shape = (13, 14, 6))#candidate|903|(13, 14, 6)|var|bool
const_904 = relay.const([[[False,True,False,False,False,False],[True,True,True,True,False,True],[True,True,False,False,True,True],[False,False,False,True,True,True],[True,True,True,True,False,False],[True,False,False,True,False,False],[True,True,True,True,True,True],[False,False,False,False,False,False],[True,False,False,False,True,True],[True,True,False,False,False,False],[False,True,False,False,False,True],[False,True,False,True,False,True],[False,False,True,True,False,True],[True,False,False,True,False,True]],[[False,True,False,True,True,False],[True,True,True,False,False,True],[True,False,True,True,False,True],[True,False,False,False,True,False],[False,False,False,False,True,False],[True,False,True,False,True,False],[False,False,False,False,False,False],[True,True,False,False,True,False],[False,False,True,False,False,False],[False,False,True,True,False,False],[True,False,False,True,False,True],[True,False,False,True,False,False],[True,False,False,False,False,True],[False,False,True,True,False,True]],[[False,True,False,True,False,False],[True,True,False,False,False,False],[True,False,True,True,True,True],[False,True,True,False,True,False],[True,True,False,False,True,True],[True,True,False,True,False,False],[False,True,True,False,True,False],[True,True,False,False,False,True],[True,False,False,True,False,True],[True,True,True,True,True,False],[False,True,True,False,False,True],[False,False,False,False,True,False],[False,False,True,False,False,True],[True,True,False,False,False,False]],[[True,True,False,False,True,True],[False,True,False,True,False,True],[False,False,True,True,False,False],[True,False,False,False,False,False],[True,False,False,True,False,False],[False,True,False,False,False,True],[True,False,False,False,False,False],[True,False,True,False,True,True],[True,False,False,True,False,False],[False,False,False,False,True,False],[False,True,False,False,True,False],[True,True,False,False,True,False],[False,False,True,True,False,False],[True,True,True,True,True,True]],[[True,True,True,False,True,True],[False,True,False,False,False,False],[False,True,True,True,True,False],[True,False,False,False,True,False],[True,False,False,False,True,True],[True,True,False,True,True,True],[False,True,False,False,False,False],[False,False,False,True,True,True],[True,True,True,True,True,True],[False,False,True,False,False,True],[True,False,False,True,True,True],[False,True,False,False,True,False],[True,False,True,True,True,False],[False,True,True,False,False,True]],[[True,False,True,False,False,False],[True,True,False,True,False,True],[False,False,False,True,True,True],[True,False,True,False,True,True],[True,True,False,False,True,False],[True,False,True,True,True,True],[True,False,True,True,False,True],[False,False,False,False,True,True],[True,True,True,True,True,False],[False,False,True,False,True,True],[False,False,True,True,True,False],[True,False,True,False,True,True],[True,True,True,True,True,True],[False,True,False,True,False,True]],[[True,False,False,True,False,True],[False,False,True,True,False,True],[False,True,True,True,True,True],[False,False,False,True,False,False],[False,False,True,False,False,True],[False,True,True,False,False,True],[True,False,True,False,False,True],[True,False,False,True,True,True],[False,True,False,False,False,False],[False,True,False,True,True,False],[False,True,False,True,True,False],[False,False,True,False,True,True],[True,False,True,False,True,False],[True,True,True,True,False,True]],[[True,False,False,False,False,False],[False,False,True,False,False,True],[True,False,True,False,False,False],[True,False,True,False,False,False],[False,True,False,True,True,False],[False,False,False,True,False,False],[True,True,True,False,True,True],[True,False,True,True,False,False],[True,True,False,False,True,False],[True,True,True,True,False,False],[True,True,True,True,False,True],[False,True,False,True,True,False],[False,True,False,True,False,True],[True,True,False,True,False,False]],[[True,True,True,True,False,False],[True,True,True,False,False,True],[False,False,False,False,True,True],[False,True,False,True,True,False],[False,False,False,False,False,False],[False,True,True,False,False,True],[False,False,False,True,False,False],[False,False,True,False,True,False],[True,True,False,False,False,True],[False,False,True,False,True,True],[False,True,True,True,True,True],[False,True,True,False,False,False],[True,False,False,False,False,True],[False,False,True,False,False,True]],[[True,False,False,True,True,True],[False,True,False,True,True,False],[True,True,True,False,False,False],[False,True,False,True,True,True],[False,True,True,True,False,True],[True,True,True,True,False,False],[False,True,False,False,False,True],[False,True,False,False,False,False],[False,False,True,False,True,False],[True,False,False,False,True,False],[True,False,True,True,True,False],[True,True,True,True,False,True],[False,False,True,True,False,True],[True,False,True,True,True,True]],[[True,False,True,True,True,False],[True,False,True,True,True,False],[True,True,False,False,False,False],[True,True,False,False,False,True],[True,True,True,True,False,False],[False,False,True,True,True,False],[True,True,False,False,False,False],[True,True,True,True,True,True],[True,False,False,True,True,False],[False,False,False,False,True,False],[False,True,False,True,False,False],[True,False,True,False,False,True],[False,True,False,True,False,True],[False,True,True,True,True,False]],[[True,True,True,True,True,False],[False,False,False,False,True,False],[False,True,False,True,True,True],[False,True,False,False,False,True],[True,False,False,True,True,True],[True,True,True,False,False,False],[True,False,False,True,True,False],[True,True,True,False,True,False],[True,True,True,True,False,True],[False,True,True,True,False,True],[False,False,False,True,False,False],[False,True,True,False,False,False],[False,False,True,True,False,False],[True,True,False,False,False,False]],[[True,True,True,True,False,False],[False,False,False,False,False,False],[False,False,False,True,False,False],[True,True,False,True,False,False],[True,False,True,True,False,False],[True,False,True,True,True,True],[True,True,True,True,True,True],[True,True,True,True,True,False],[False,False,True,False,True,True],[True,True,True,False,False,False],[False,False,False,True,True,True],[False,False,False,False,True,True],[True,False,False,True,False,True],[True,False,False,False,False,True]]], dtype = "bool")#candidate|904|(13, 14, 6)|const|bool
bop_905 = relay.logical_and(var_903.astype('bool'), relay.reshape(const_904.astype('bool'), relay.shape_of(var_903))) # shape=(13, 14, 6)
output = relay.Tuple([bop_905,])
output2 = relay.Tuple([bop_905,])
func_912 = relay.Function([var_903,], output)
mod['func_912'] = func_912
mod = relay.transform.InferType()(mod)
var_913 = relay.var("var_913", dtype = "bool", shape = (13, 14, 6))#candidate|913|(13, 14, 6)|var|bool
output = func_912(var_913)
func_914 = relay.Function([var_913], output)
mutated_mod['func_914'] = func_914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_900_call = mod.get_global_var('func_900')
func_902_call = mutated_mod.get_global_var('func_902')
call_1025 = relay.TupleGetItem(func_900_call(), 0)
call_1026 = relay.TupleGetItem(func_902_call(), 0)
uop_1028 = relay.cos(call_1025.astype('float64')) # shape=(2, 6, 9)
uop_1030 = relay.cos(call_1026.astype('float64')) # shape=(2, 6, 9)
bop_1051 = relay.mod(uop_1028.astype('float32'), relay.reshape(call_1025.astype('float32'), relay.shape_of(uop_1028))) # shape=(2, 6, 9)
bop_1054 = relay.mod(uop_1030.astype('float32'), relay.reshape(call_1026.astype('float32'), relay.shape_of(uop_1030))) # shape=(2, 6, 9)
func_387_call = mod.get_global_var('func_387')
func_390_call = mutated_mod.get_global_var('func_390')
const_1056 = relay.const(6, dtype = "uint8")#candidate|1056|()|const|uint8
var_1057 = relay.var("var_1057", dtype = "uint8", shape = (1120,))#candidate|1057|(1120,)|var|uint8
call_1055 = relay.TupleGetItem(func_387_call(relay.reshape(const_1056.astype('uint8'), []), relay.reshape(var_1057.astype('uint8'), [1120,]), ), 0)
call_1058 = relay.TupleGetItem(func_390_call(relay.reshape(const_1056.astype('uint8'), []), relay.reshape(var_1057.astype('uint8'), [1120,]), ), 0)
output = relay.Tuple([bop_1051,call_1055,const_1056,var_1057,])
output2 = relay.Tuple([bop_1054,call_1058,const_1056,var_1057,])
func_1062 = relay.Function([var_1057,], output)
mod['func_1062'] = func_1062
mod = relay.transform.InferType()(mod)
var_1063 = relay.var("var_1063", dtype = "uint8", shape = (1120,))#candidate|1063|(1120,)|var|uint8
output = func_1062(var_1063)
func_1064 = relay.Function([var_1063], output)
mutated_mod['func_1064'] = func_1064
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1066 = relay.var("var_1066", dtype = "float64", shape = (7, 10, 10))#candidate|1066|(7, 10, 10)|var|float64
uop_1067 = relay.cos(var_1066.astype('float64')) # shape=(7, 10, 10)
output = uop_1067
output2 = uop_1067
func_1077 = relay.Function([var_1066,], output)
mod['func_1077'] = func_1077
mod = relay.transform.InferType()(mod)
mutated_mod['func_1077'] = func_1077
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1078 = relay.var("var_1078", dtype = "float64", shape = (7, 10, 10))#candidate|1078|(7, 10, 10)|var|float64
func_1077_call = mutated_mod.get_global_var('func_1077')
call_1079 = func_1077_call(var_1078)
output = call_1079
func_1080 = relay.Function([var_1078], output)
mutated_mod['func_1080'] = func_1080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_1118 = func_361_call()
call_1119 = func_361_call()
func_487_call = mod.get_global_var('func_487')
func_490_call = mutated_mod.get_global_var('func_490')
var_1124 = relay.var("var_1124", dtype = "uint8", shape = (4, 280))#candidate|1124|(4, 280)|var|uint8
call_1123 = relay.TupleGetItem(func_487_call(relay.reshape(call_1118.astype('float32'), [2, 6, 9]), relay.reshape(var_1124.astype('uint8'), [1120,]), ), 0)
call_1125 = relay.TupleGetItem(func_490_call(relay.reshape(call_1118.astype('float32'), [2, 6, 9]), relay.reshape(var_1124.astype('uint8'), [1120,]), ), 0)
func_1062_call = mod.get_global_var('func_1062')
func_1064_call = mutated_mod.get_global_var('func_1064')
call_1148 = relay.TupleGetItem(func_1062_call(relay.reshape(var_1124.astype('uint8'), [1120,])), 1)
call_1149 = relay.TupleGetItem(func_1064_call(relay.reshape(var_1124.astype('uint8'), [1120,])), 1)
func_487_call = mod.get_global_var('func_487')
func_490_call = mutated_mod.get_global_var('func_490')
call_1150 = relay.TupleGetItem(func_487_call(relay.reshape(call_1148.astype('float32'), [2, 6, 9]), relay.reshape(var_1124.astype('uint8'), [1120,]), ), 2)
call_1151 = relay.TupleGetItem(func_490_call(relay.reshape(call_1148.astype('float32'), [2, 6, 9]), relay.reshape(var_1124.astype('uint8'), [1120,]), ), 2)
func_213_call = mod.get_global_var('func_213')
func_216_call = mutated_mod.get_global_var('func_216')
call_1152 = relay.TupleGetItem(func_213_call(relay.reshape(call_1148.astype('bool'), [6, 3, 6])), 0)
call_1153 = relay.TupleGetItem(func_216_call(relay.reshape(call_1148.astype('bool'), [6, 3, 6])), 0)
func_213_call = mod.get_global_var('func_213')
func_216_call = mutated_mod.get_global_var('func_216')
call_1154 = relay.TupleGetItem(func_213_call(relay.reshape(call_1118.astype('bool'), [6, 3, 6])), 1)
call_1155 = relay.TupleGetItem(func_216_call(relay.reshape(call_1118.astype('bool'), [6, 3, 6])), 1)
output = relay.Tuple([call_1118,call_1123,var_1124,call_1148,call_1150,call_1152,call_1154,])
output2 = relay.Tuple([call_1119,call_1125,var_1124,call_1149,call_1151,call_1153,call_1155,])
func_1180 = relay.Function([var_1124,], output)
mod['func_1180'] = func_1180
mod = relay.transform.InferType()(mod)
mutated_mod['func_1180'] = func_1180
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1181 = relay.var("var_1181", dtype = "uint8", shape = (4, 280))#candidate|1181|(4, 280)|var|uint8
func_1180_call = mutated_mod.get_global_var('func_1180')
call_1182 = func_1180_call(var_1181)
output = call_1182
func_1183 = relay.Function([var_1181], output)
mutated_mod['func_1183'] = func_1183
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1185 = relay.const([[[4,2,-9,-9,-6,3,8,4,3,-9,1,-3,10],[-7,7,10,10,-1,4,5,1,-5,1,10,-1,-8],[-8,1,1,6,2,1,-1,-2,-2,-4,2,-1,1],[6,2,-4,-7,8,-7,-5,-2,2,9,-8,-10,6],[-4,-4,10,-8,-5,5,-9,9,-9,6,3,7,-1],[-6,9,-2,1,-9,7,-5,10,-4,3,9,-10,-5],[3,6,7,5,-4,-1,5,9,-7,-6,-4,-10,-8],[1,1,2,8,-10,-9,-2,-5,1,-5,4,3,-1],[-4,6,-9,1,-10,6,10,4,-2,-4,9,7,-4],[-8,-4,-5,-9,10,7,9,-4,-7,2,4,8,-1],[1,-3,-2,3,-9,4,-9,-5,8,6,-9,-6,4],[5,8,-1,7,-8,-4,-4,-9,-8,-3,-9,-6,-4],[-7,8,-2,5,2,-1,-9,-7,-9,-3,-7,1,5],[2,-4,-8,7,-4,10,9,7,-10,-10,-9,-8,-9],[7,-7,-9,-6,7,6,2,5,1,-4,5,-7,1]],[[-3,-10,5,4,10,3,8,9,-6,-6,-5,-4,-7],[4,-3,10,3,-2,-7,-10,-2,2,3,-6,4,-9],[-10,7,3,1,-6,3,1,10,4,5,-3,7,-10],[-6,-6,-3,-9,4,-2,7,8,-1,-7,-8,-1,6],[2,1,-10,-6,3,3,-10,3,5,-3,-1,-3,3],[7,6,7,1,-10,4,-7,3,-8,-10,6,2,8],[2,-10,-3,-9,2,-9,-4,4,-4,5,-3,-2,-6],[8,-10,1,-8,-8,-8,1,3,-5,-8,-6,-1,2],[6,9,-4,1,-5,-7,3,-5,-2,-3,8,-3,6],[-9,-2,1,4,-1,-6,4,5,4,5,-1,6,4],[-1,-10,-8,-3,1,8,3,6,4,-1,-1,6,-4],[5,-10,-6,7,7,-9,8,4,7,-7,-5,5,9],[10,-2,-2,-8,7,5,-2,-1,-3,-10,7,2,-10],[-7,4,-1,-1,1,-1,8,-5,-1,-5,7,-3,3],[-4,-6,-4,9,8,2,-4,-5,-4,-4,7,-5,8]],[[-10,-8,-5,-10,7,5,-9,10,4,-6,1,-3,-6],[-10,5,-2,-1,8,5,6,-9,9,-3,1,5,8],[5,10,-4,-4,-8,-1,-9,4,6,-5,2,7,5],[5,-3,-5,-2,2,3,4,4,-2,-6,-8,-8,-1],[9,8,-4,-3,3,7,-2,3,7,-7,-5,-6,7],[3,-7,8,2,1,6,-5,3,-8,3,10,-9,2],[8,-4,10,-10,4,4,-1,-2,-10,-8,8,-7,7],[10,-4,1,10,7,-5,-8,3,4,6,3,-2,-6],[8,3,1,-3,-6,9,10,-8,10,-1,-8,9,1],[-10,2,5,-9,5,-2,7,3,-5,-1,-7,9,-6],[-4,-10,4,10,-6,-7,-3,-9,3,4,1,10,-4],[-4,4,1,4,5,-3,-7,-9,-8,-7,9,2,-7],[-5,-6,3,-4,-2,6,-10,8,-5,-4,9,1,8],[5,3,4,8,-9,-2,7,1,3,-4,5,-6,-8],[-3,-1,8,3,-10,1,7,-9,4,4,-1,7,8]],[[7,-4,-8,-5,-8,-5,-6,7,2,-9,2,9,9],[3,-5,9,-4,10,-10,1,8,10,-2,1,-3,-7],[2,-3,5,-8,-8,6,-1,-5,9,-10,1,-9,9],[7,8,6,-9,4,6,8,-2,7,-9,4,-8,5],[6,-10,-5,6,-10,-7,3,5,-5,7,-5,1,-7],[-4,-1,4,-4,-2,-1,6,1,10,-5,5,-6,-9],[7,5,-7,10,-9,-7,9,5,8,-1,3,4,4],[9,-2,-3,10,-4,8,-7,10,-1,5,-1,5,3],[3,7,-9,-9,7,-1,-9,-4,-10,-5,6,9,2],[-4,10,-7,7,10,2,-8,-1,-8,3,-9,-4,1],[-2,1,10,1,7,3,-3,1,-4,6,7,8,-7],[-2,3,3,6,7,3,6,-7,-5,3,6,6,-3],[-6,-4,-7,-6,-4,6,-4,5,-3,7,-9,-10,10],[-8,-8,1,1,8,6,10,2,-9,9,6,-7,3],[7,8,9,-6,-8,-10,-4,9,-2,-9,5,3,-4]],[[-7,3,-8,-5,-10,4,-1,2,-5,2,6,3,10],[-3,-1,3,-9,9,-9,-6,1,4,4,7,-10,-3],[3,-2,-1,8,-6,-1,-9,2,9,6,8,3,-6],[3,-9,4,2,9,-1,-7,-9,-1,1,6,-3,-9],[4,7,4,8,6,-9,6,-4,-4,5,9,2,1],[-1,2,-7,4,8,4,3,-6,10,8,-10,-3,8],[2,6,-9,8,-7,-10,1,-8,4,6,-2,3,-8],[-4,9,-7,-3,-2,7,4,7,4,-3,-4,4,6],[-6,-7,1,7,7,-9,-6,1,-3,9,10,-7,-6],[8,2,-7,3,3,9,-2,-4,5,1,3,-2,3],[6,6,2,-5,8,-3,7,-4,5,-3,6,1,7],[-1,-8,2,6,-7,2,5,3,-2,3,9,4,9],[1,9,-5,6,9,-7,-5,-5,8,10,5,4,-10],[6,-4,-5,-6,-2,7,4,5,10,10,9,-5,-9],[-3,-8,3,-8,-10,3,-9,9,-2,-3,6,7,9]],[[2,-6,-4,-4,-3,-10,-6,-4,-8,-4,9,10,3],[5,2,7,-10,6,4,-8,-9,-8,9,-3,-4,-4],[3,7,9,-5,8,6,-6,1,2,-7,-6,-5,-6],[1,-7,5,8,5,5,-8,-3,2,5,-9,1,-8],[-8,3,1,-6,-1,-10,6,-6,-7,-6,9,10,-1],[2,5,-2,-3,9,-1,4,-7,-2,-2,-5,-1,9],[-1,3,-8,-6,5,5,3,5,8,-7,-4,1,-5],[4,7,7,2,10,7,2,3,3,1,1,7,-8],[7,6,-4,-2,-6,1,-1,8,8,-1,7,-7,9],[-10,4,-7,7,-4,8,4,-5,1,-7,-5,9,5],[9,6,8,6,4,-6,1,-4,6,-2,-4,-8,-2],[-7,8,-8,-6,8,-2,7,-8,-9,-2,9,-2,10],[3,-10,-2,7,10,10,-2,9,1,-4,-8,-9,7],[-8,-8,-6,8,-6,-2,2,-8,8,-1,8,3,-2],[-4,-1,8,1,-2,6,2,2,-5,-5,-9,7,-10]],[[-1,-4,5,-3,-10,-10,8,5,-1,6,-10,-10,-5],[10,8,-6,4,-1,9,-9,-4,7,10,3,-10,7],[-3,-7,-7,-2,-6,3,8,2,7,-4,2,-10,-7],[6,-6,-9,1,7,2,2,-8,1,8,-3,7,-5],[-1,3,-9,-7,-1,2,-2,-9,-10,6,5,-4,-3],[9,4,-10,8,5,2,10,8,-5,-3,-7,-5,-1],[-8,-5,-3,10,-8,-4,-2,2,1,-7,-6,-9,9],[3,7,-4,10,8,6,3,-8,10,6,-6,-6,7],[-7,2,-2,-10,1,-6,5,-4,-1,5,-4,1,-9],[-8,-2,-4,9,5,-10,-2,10,2,1,-8,-5,-4],[-10,-8,6,3,-8,6,-4,1,-7,5,-1,5,-4],[-6,10,7,-9,-10,-10,-10,9,-8,-9,6,-3,5],[9,8,5,-2,4,-8,4,-7,-10,-5,-2,-1,-5],[9,10,-2,4,-2,-1,-5,-6,9,10,6,-2,-8],[-5,7,7,-6,8,8,7,2,-6,5,1,-4,2]],[[2,1,8,10,-4,1,-6,9,2,5,3,10,-5],[-4,1,-9,9,2,5,-5,1,-2,-7,-10,-4,1],[-8,7,-2,-4,-8,8,4,7,4,-2,-9,1,-3],[5,7,7,8,1,-5,-7,-8,10,-4,3,10,10],[-10,-7,3,-2,-1,8,-3,3,1,-2,-2,-5,1],[4,-5,-3,7,-10,6,-3,-1,8,7,3,-9,1],[7,-8,3,-10,-8,3,-4,8,-5,7,-9,1,6],[5,8,9,-1,-4,10,-3,10,6,9,6,-4,-1],[9,10,-5,-1,3,10,8,6,-1,-8,5,5,-7],[-9,3,7,-1,7,4,-10,-9,-10,-6,5,-7,8],[-5,7,1,5,5,6,-1,-3,1,3,-8,7,1],[-3,2,-10,2,3,3,-9,-1,4,10,-6,-5,-2],[-10,-6,10,-9,1,-3,9,10,3,-10,-6,4,-6],[-6,-7,-3,-7,10,-10,-2,-10,-6,1,1,-5,8],[-7,-7,5,3,4,-3,-7,-10,3,8,9,4,-9]],[[-5,8,-10,-10,-8,-2,8,-7,9,-5,-10,5,4],[3,-5,7,-9,-5,-1,-5,9,10,-5,8,10,7],[4,8,-5,7,3,9,-10,2,9,-8,7,4,4],[10,-7,-4,6,-8,10,2,-1,7,5,-1,-9,1],[-9,-1,-8,9,-7,-6,-2,5,-10,-9,-8,-2,-8],[-7,4,-4,-6,-7,6,-2,8,8,-2,4,-10,5],[-9,-2,10,5,-1,6,-4,4,9,-2,3,7,-3],[-1,3,-2,3,-3,-5,-6,5,-4,4,-8,-3,8],[-2,-3,-5,9,-2,-4,7,7,-4,-10,4,-8,1],[1,-8,-10,-3,5,-1,10,7,8,1,-10,10,-6],[2,-3,3,7,-3,2,-1,-6,5,-6,9,-8,1],[7,-8,6,-10,4,-2,-5,-9,-9,-5,-3,-10,-5],[-2,9,-1,-5,-1,10,7,-5,5,4,-6,-4,-9],[-3,5,7,-3,3,5,4,8,-7,7,5,-1,-4],[1,2,-5,8,5,9,4,-1,-1,-4,8,-3,-7]],[[-5,-5,-7,-8,-6,-6,-5,2,8,-8,-4,5,-8],[-3,-7,7,-9,2,-9,-7,-5,1,-5,-6,10,1],[4,2,-8,-1,3,9,-10,-10,-3,-6,-9,10,4],[6,-1,6,4,9,4,8,-8,1,-8,-9,-7,1],[3,-9,-7,-9,-3,-6,-4,10,-5,-5,-3,-2,-7],[-4,-5,-10,6,7,8,6,2,10,-6,-6,-7,5],[9,-3,-10,1,-3,6,-4,-7,-1,-6,4,1,-4],[-3,7,-3,9,3,4,-5,-8,-10,-7,7,-9,-1],[6,-3,8,-1,7,-3,1,-6,-1,6,5,4,-3],[8,-3,-3,2,9,-3,4,4,6,3,-2,4,-6],[2,-9,-2,-6,-7,-1,-6,-8,1,-1,-1,-2,-1],[-1,-10,4,-10,8,-1,4,-3,10,5,8,-1,-5],[-8,-7,1,3,-8,5,9,7,-8,-1,-7,-10,-8],[10,-7,-2,-2,-3,-8,4,3,-3,3,-6,4,-3],[8,-3,2,-8,8,6,-8,3,-5,-3,8,-1,-9]],[[-3,-4,-1,-10,3,-10,2,10,10,-7,5,3,8],[-5,4,6,6,-6,4,-3,-7,-7,-5,-7,4,-9],[3,8,-3,2,6,7,-8,1,8,-1,9,3,7],[-8,-1,-2,10,8,3,-3,6,3,2,9,9,2],[-10,-1,-5,7,-7,2,9,1,8,2,-1,-1,8],[2,2,5,-10,-10,-7,-1,-6,-10,-3,-6,2,-6],[-3,-7,-8,10,4,3,-4,-7,10,5,-2,-2,5],[-7,-7,1,1,3,-8,1,-8,4,-7,-5,2,4],[5,9,5,-9,1,2,-10,3,-8,2,1,10,-8],[7,-6,-3,9,1,8,-6,-9,-2,3,-9,-2,-7],[-6,10,-5,-3,10,-10,-8,4,-10,-4,9,10,-1],[-3,9,-3,8,-10,-2,1,-8,4,-5,-9,-9,6],[9,9,6,-3,1,-1,-1,3,-3,-9,7,-5,2],[-9,-9,6,-10,9,7,10,-10,-1,1,6,8,3],[9,-10,-3,9,-4,3,-1,2,6,10,-5,7,-4]]], dtype = "uint32")#candidate|1185|(11, 15, 13)|const|uint32
var_1186 = relay.var("var_1186", dtype = "uint32", shape = (11, 15, 13))#candidate|1186|(11, 15, 13)|var|uint32
bop_1187 = relay.minimum(const_1185.astype('uint32'), relay.reshape(var_1186.astype('uint32'), relay.shape_of(const_1185))) # shape=(11, 15, 13)
output = bop_1187
output2 = bop_1187
func_1205 = relay.Function([var_1186,], output)
mod['func_1205'] = func_1205
mod = relay.transform.InferType()(mod)
mutated_mod['func_1205'] = func_1205
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1206 = relay.var("var_1206", dtype = "uint32", shape = (11, 15, 13))#candidate|1206|(11, 15, 13)|var|uint32
func_1205_call = mutated_mod.get_global_var('func_1205')
call_1207 = func_1205_call(var_1206)
output = call_1207
func_1208 = relay.Function([var_1206], output)
mutated_mod['func_1208'] = func_1208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_1214 = func_361_call()
call_1215 = func_361_call()
func_1077_call = mod.get_global_var('func_1077')
func_1080_call = mutated_mod.get_global_var('func_1080')
const_1217 = relay.const([5.879874,-4.884697,0.384984,-6.216907,1.786133,6.889616,-8.032891,9.589588,-4.911642,7.645445,-3.350253,-4.090262,8.431226,-2.556725,-0.925466,9.714743,-2.411134,5.239548,5.113554,2.205901,-9.165464,8.381853,8.702548,2.232670,-0.395897,-0.542713,-1.380972,-2.789483,9.894143,9.617790,-0.785260,0.577797,-4.363052,-6.632560,-9.090489,-8.234058,-9.669879,4.436472,-2.719750,-0.704300,7.913755,8.405276,0.610720,-1.019824,8.679981,-4.333361,-3.887872,-0.630769,-3.709226,-2.912092,-2.996269,-2.055110,-0.811658,-7.804422,-6.878142,8.756442,-5.078071,-9.252773,-0.539645,-2.255350,-4.058962,1.487486,-9.782660,5.253324,-2.273796,-8.566467,-6.354996,-6.449810,-5.434870,2.034228,2.142127,6.863528,-7.499635,4.789328,-0.365371,-8.943909,-3.929351,1.674784,5.958454,-8.024702,4.698502,-7.308043,9.062980,-3.795003,-5.812669,-4.178964,5.428567,7.844547,6.914698,-8.494380,-1.084924,-6.902339,9.749466,1.588081,-9.161444,-2.347968,-1.149908,1.825651,0.350253,-4.111664,-3.530590,3.664889,-7.342689,1.897030,7.137280,8.305782,-1.229742,3.032825,4.326663,-6.434448,-7.032380,2.486353,9.753099,-5.042690,1.895480,-5.066904,0.506173,0.873433,-2.093955,-7.561212,-6.849607,6.874713,0.701407,-8.613177,-6.207678,5.404150,-8.188710,5.342251,0.125387,-7.739236,-3.783786,-6.665028,4.996142,1.828072,-3.125561,8.270041,5.629405,3.368099,4.927925,-0.329247,-9.807798,-4.719672,-9.283639,9.849619,9.029815,-9.540457,-4.782795,-8.113724,-5.214323,-9.695470,2.119973,-8.112486,-9.912203,7.816437,2.152458,1.336019,1.144614,-7.871284,-7.372365,-1.485516,-0.650251,9.514025,0.771381,-2.927351,-0.994350,4.684822,-1.687683,-8.903408,7.560509,5.567514,8.675440,5.649933,-7.937413,4.499991,8.937467,8.429400,-2.533124,-5.960918,-3.965558,-8.572565,3.708853,-2.004878,5.515450,2.714516,-8.046417,6.263359,7.776902,2.286106,7.512897,-4.074155,-3.614291,-9.438760,1.532422,-5.053534,4.009573,-1.108384,-7.512473,-9.470977,8.902782,3.128009,-9.237657,-6.915990,0.443716,-0.069484,-5.031974,8.223643,-2.516005,5.185005,-2.990800,0.770686,-5.106168,1.387842,-1.051410,-7.974221,4.360596,4.090375,8.282042,0.275051,2.453028,5.971505,5.877305,-5.005316,-0.774735,4.881156,-8.380700,-9.148237,-8.810810,7.644898,6.600374,-8.521571,6.894550,4.067455,7.751235,3.403961,-5.749526,-1.926372,6.100911,0.986580,6.826682,7.150976,8.689615,-9.390717,8.971846,-1.615451,-2.755692,3.753030,-6.133127,-7.521715,4.567499,0.450417,-0.968309,3.540528,-1.465195,5.812581,6.054426,2.786283,-0.512761,-4.736443,-6.843711,-7.481595,-4.937505,-7.657441,-4.725469,-7.453992,0.039695,3.045402,-4.644789,9.811301,3.213496,-6.045694,0.340677,6.017873,3.179512,2.972984,-7.926264,-8.410704,6.711094,-9.055838,8.058910,-8.508261,-9.099371,-4.795137,-4.352560,8.847258,-3.707256,6.572309,-0.404736,2.351678,-7.166059,7.438323,4.823432,6.922022,-9.413362,-3.306034,7.693771,-0.509646,0.390918,-3.978318,1.048019,5.903819,1.295256,7.203584,-6.046207,2.764862,-3.656208,5.097161,5.111266,-2.246692,-4.385251,3.643780,2.561611,5.441226,5.017813,6.635937,-1.219788,-9.985283,8.546368,3.837669,7.464801,-9.563750,8.552803,8.303318,0.419344,-6.303877,-9.676181,1.709655,-3.615226,-0.951857,-3.974886,-0.164141,3.488544,-3.475708,-6.930802,-4.479959,-9.128879,2.807645,-0.313134,-1.101032,1.894826,-6.677135,5.050827,0.584033,-6.751987,1.123404,6.187068,9.130218,-1.783161,0.246557,1.359600,-9.178188,1.985166,8.676328,-2.509148,1.214772,7.033490,-1.759203,8.859471,-5.063144,3.124971,-6.775574,8.115695,6.291367,9.878603,-7.428417,-6.204490,-5.528324,8.332680,-6.315759,-5.802425,8.309485,1.512516,-1.246362,0.745324,-0.524638,-6.135012,-7.215912,1.757186,9.889899,-2.071017,4.706453,6.067367,-5.821501,-8.967510,-4.314885,-5.471169,-7.186381,6.290913,-6.636354,0.525248,-7.703936,4.164469,3.056553,-9.289105,6.753289,-2.896314,-8.996141,9.440137,-6.466256,6.091414,-2.510005,-9.125425,5.580075,4.148797,7.872941,-0.148369,-2.537684,-3.281149,-3.997836,-5.709974,0.554330,4.660069,-9.855645,0.088457,-9.809598,-6.715550,-9.870019,6.999147,-2.855921,-3.227544,3.146910,1.480303,-6.431148,8.606509,0.684338,8.489526,-1.831107,-3.066348,0.328969,-9.436594,-1.116075,-2.979014,3.113024,-3.767804,-7.968226,9.831301,0.438356,4.490585,-1.895716,1.911164,-9.588004,4.286676,0.244396,-6.304041,7.415131,-1.322910,9.467011,-9.400741,-2.710295,-2.670896,1.063773,-0.174850,0.098072,1.877732,-8.205424,5.821602,6.164634,8.091924,-1.460744,8.037910,-6.201890,0.576728,-7.561839,4.225167,-6.010706,7.262627,6.804799,-1.184742,1.701602,7.209679,-2.081841,-7.536139,1.789509,-8.503036,6.129331,7.901678,2.974787,9.714468,-2.468590,-5.555445,5.485059,3.049716,6.158224,0.409682,0.161964,-9.017507,6.651908,4.187932,8.442972,-8.404978,2.338994,-5.485368,-3.939935,-5.520802,-0.868230,5.005384,-7.100456,9.122253,-3.247210,-1.542862,0.081098,-7.157981,6.776214,6.972300,3.957643,-0.028626,6.135656,-8.865187,-4.476717,-6.123023,9.700151,-6.448300,-5.074580,-5.168249,-3.740334,-6.494973,5.333952,-3.704121,-6.905846,7.751606,8.611142,-6.296913,4.786052,-8.947181,0.739784,-6.097624,-1.429724,-0.339788,-9.755524,-1.211614,5.525581,-4.894177,7.410958,-4.069287,-7.158953,2.424492,1.304791,-8.800314,-3.568947,-3.112630,-3.417338,1.975512,-7.716990,8.735094,-7.088592,5.891588,6.597984,-6.370073,7.120638,-8.248663,9.883339,1.366368,-8.554566,0.751692,8.144049,-6.198636,-0.633352,-4.674056,-6.969452,-2.557759,9.103703,-3.595289,3.525356,2.909509,0.266811,3.235061,-2.433957,7.502467,-0.818894,5.822576,5.369174,8.772951,7.497602,-3.558767,-9.583313,-2.168952,-8.173260,-0.023712,-6.467791,-4.535574,9.825404,-4.030476,5.253175,-3.557958,-8.969198,0.515757,-4.969800,2.323798,-5.651459,9.795047,-7.141500,8.163025,-5.921617,8.485657,5.638212,8.977607,8.302023,-1.564323,9.727506,-1.723682,9.514605,8.531900,4.525818,8.767751,-3.374937,-8.449549,8.209814,-4.655927,8.375231,-8.423946,4.525325,6.394891,9.089207,2.892733,3.604006,-9.171622,4.914036,-5.382407,-8.151820,6.376755,-3.901370,-9.931619,1.589957,2.918741,-8.018926,8.605761,3.617614,-7.375586,0.631002,-1.625380,9.193321,5.245868,-5.968567,1.277233,8.601018,-4.096717,-0.812240,3.907693,4.616434,-2.133391,-6.412236,5.875249,8.075206,-9.301688,-0.346060,7.783575,0.015075,-3.547557,-2.203659,7.156272,-0.385871,0.008520,-9.334098,-2.066393,3.035633,5.167705,8.989915,-4.573115,-7.691882,7.791897,1.574219,-0.300045,3.617707,-4.705731,4.621078,4.883182,5.397757,-9.246309,-5.028978,5.169278,-2.394620,8.656999,-2.537450,-1.091420,4.482138,3.916127,-0.777064,5.240981,-2.054377,1.765643,5.372902,-0.549650,9.160221,-1.294071,1.862090,1.280071,-4.284623,6.495423,-5.771377,6.610927,4.079609,-9.035596,1.822739,4.888115,-5.666837,1.608183,-2.246919,-5.779692,-8.168568,9.097209,3.637253], dtype = "float64")#candidate|1217|(700,)|const|float64
call_1216 = func_1077_call(relay.reshape(const_1217.astype('float64'), [7, 10, 10]))
call_1218 = func_1077_call(relay.reshape(const_1217.astype('float64'), [7, 10, 10]))
bop_1231 = relay.minimum(const_1217.astype('float64'), relay.reshape(call_1216.astype('float64'), relay.shape_of(const_1217))) # shape=(700,)
bop_1234 = relay.minimum(const_1217.astype('float64'), relay.reshape(call_1218.astype('float64'), relay.shape_of(const_1217))) # shape=(700,)
bop_1237 = relay.add(bop_1231.astype('int64'), relay.reshape(const_1217.astype('int64'), relay.shape_of(bop_1231))) # shape=(700,)
bop_1240 = relay.add(bop_1234.astype('int64'), relay.reshape(const_1217.astype('int64'), relay.shape_of(bop_1234))) # shape=(700,)
output = relay.Tuple([call_1214,bop_1237,])
output2 = relay.Tuple([call_1215,bop_1240,])
func_1258 = relay.Function([], output)
mod['func_1258'] = func_1258
mod = relay.transform.InferType()(mod)
output = func_1258()
func_1259 = relay.Function([], output)
mutated_mod['func_1259'] = func_1259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_875_call = mod.get_global_var('func_875')
func_877_call = mutated_mod.get_global_var('func_877')
call_1305 = relay.TupleGetItem(func_875_call(), 0)
call_1306 = relay.TupleGetItem(func_877_call(), 0)
func_1258_call = mod.get_global_var('func_1258')
func_1259_call = mutated_mod.get_global_var('func_1259')
call_1350 = relay.TupleGetItem(func_1258_call(), 0)
call_1351 = relay.TupleGetItem(func_1259_call(), 0)
func_747_call = mod.get_global_var('func_747')
func_753_call = mutated_mod.get_global_var('func_753')
var_1362 = relay.var("var_1362", dtype = "float32", shape = (117,))#candidate|1362|(117,)|var|float32
const_1363 = relay.const(-1, dtype = "uint8")#candidate|1363|()|const|uint8
var_1364 = relay.var("var_1364", dtype = "uint8", shape = (1120,))#candidate|1364|(1120,)|var|uint8
call_1361 = relay.TupleGetItem(func_747_call(relay.reshape(var_1362.astype('float32'), [13, 3, 3]), relay.reshape(var_1362.astype('float32'), [13, 3, 3]), relay.reshape(const_1363.astype('uint8'), []), relay.reshape(var_1364.astype('uint8'), [560, 2]), ), 3)
call_1365 = relay.TupleGetItem(func_753_call(relay.reshape(var_1362.astype('float32'), [13, 3, 3]), relay.reshape(var_1362.astype('float32'), [13, 3, 3]), relay.reshape(const_1363.astype('uint8'), []), relay.reshape(var_1364.astype('uint8'), [560, 2]), ), 3)
uop_1374 = relay.cosh(var_1364.astype('float32')) # shape=(1120,)
output = relay.Tuple([call_1305,call_1350,call_1361,var_1362,const_1363,uop_1374,])
output2 = relay.Tuple([call_1306,call_1351,call_1365,var_1362,const_1363,uop_1374,])
func_1386 = relay.Function([var_1362,var_1364,], output)
mod['func_1386'] = func_1386
mod = relay.transform.InferType()(mod)
mutated_mod['func_1386'] = func_1386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1386_call = mutated_mod.get_global_var('func_1386')
var_1388 = relay.var("var_1388", dtype = "float32", shape = (117,))#candidate|1388|(117,)|var|float32
var_1389 = relay.var("var_1389", dtype = "uint8", shape = (1120,))#candidate|1389|(1120,)|var|uint8
call_1387 = func_1386_call(var_1388,var_1389,)
output = call_1387
func_1390 = relay.Function([var_1388,var_1389,], output)
mutated_mod['func_1390'] = func_1390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1258_call = mod.get_global_var('func_1258')
func_1259_call = mutated_mod.get_global_var('func_1259')
call_1400 = relay.TupleGetItem(func_1258_call(), 1)
call_1401 = relay.TupleGetItem(func_1259_call(), 1)
const_1415 = relay.const([1,-6,-5,10,-4,-8,-4,-9,7,8,1,-9,-6,-10,3,3,-7,10,-5,8,3,6,4,6,-9,-3,8,7,-9,7,8,-5,6,9,-4,-1,-4,4,-2,3,-5,-4,-8,-8,-9,-8,2,-3,7,-2,-8,9,9,4,-4,-3,-1,3,-9,8,-8,4,-10,-10,1,-9,6,3,-3,-7,3,-5,8,-6,3,-4,10,10,-8,-8,-4,-8,-7,6,-9,7,2,8,4,-6,8,7,-9,-10,9,6,7,4,6,-3,2,8,-4,3,-10,2,-10,-10,5,-7,-9,8,8,9,-9,-10,-2,4,-7,-1,-7,-7,-3,-9,6,-3,-1,-3,10,-5,-4,-1,-5,4,3,9,2,8,-2,4,-4,-4,-7,-4,-9,-7,5,-1,6,-2,-3,-8,6,8,4,7,8,-3,-8,-3,9,2,-9,-4,-8,-3,-7,6,8,3,-8,2,-4,3,5,9,-6,-5,3,2,-6,-6,6,10,8,8,8,5,6,-3,6,2,-4,8,8,1,-5,-1,-9,-8,6,6,-7,-5,-1,-3,-2,-10,6,4,-10,-10,-3,9,-3,2,3,3,-1,5,7,-10,7,-5,-7,-6,5,-1,8,2,-7,1,2,-1,2,-6,8,-10,-3,-7,-6,-9,-1,-1,2,-8,-8,10,3,-5,-9,-8,7,1,6,2,3,5,4,10,-1,-3,-9,3,4,1,-8,-2,8,5,-3,6,-10,7,8,8,-8,-2,-5,1,2,-5,-10,5,10,1,-9,-9,-9,3,-4,1,-3,10,-8,7,4,10,1,-3,-7,6,3,-5,10,4,-10,-7,-7,-10,10,7,-1,8,-4,3,-7,-5,2,5,-9,-9,3,1,5,-9,1,8,2,-4,-9,8,-5,6,-5,3,-9,5,10,-4,-9,1,8,4,9,8,4,-4,1,8,1,1,4,4,4,-1,4,5,-5,-3,6,2,9,8,-6,-7,-10,10,4,9,5,-5,4,-10,10,3,7,5,-1,-8,-3,-7,3,4,1,-9,3,-3,3,-6,-7,8,-4,1,-8,-4,6,-2,9,8,1,-6,9,-1,-5,5,6,7,6,5,1,-5,-1,5,4,1,9,10,-9,2,10,5,1,-7,-3,3,4,-8,4,6,-7,3,-4,-5,8,6,-7,7,6,6,-6,1,6,6,5,10,-1,-7,10,8,1,9,9,-5,7,4,2,-5,7,2,5,1,7,-1,-9,-6,-6,-8,10,-10,7,-2,9,1,1,5,5,2,-5,-10,3,-5,-2,4,8,-9,-7,-8,-2,-2,2,1,-5,-3,7,5,1,8,4,-5,5,-9,-7,-9,-6,2,-2,7,-7,10,-4,-3,-6,10,3,4,3,10,-10,1,-2,4,-7,3,-1,-9,7,-4,4,-5,-1,-7,-4,-6,-6,10,1,1,-7,3,7,-5,-5,9,2,10,-5,-2,2,3,5,5,9,6,-10,6,-1,2,-1,-9,5,8,4,8,8,-3,7,10,2,4,5,9,-2,-3,-4,-5,10,10,3,-2,-1,5,1,-6,1,6,1,-1,-8,3,7,-2,1,-2,10,-7,-9,1,-10,-4,8,-9,7,9,4,-9,9,-9,1,-5,5,4,-6,3,-3,-7,7,9,5,1,-1,2,10,-2,-3,2,3,-4,-10,-3,6,-5,7,8,3,1,10,7,5,2,8,-9,-1,-8,-2,5,4,-2,3,2,3,-9,-9,2,-6,5,8,5,-7,-10,7,-8,5,-1,-1,-2,8,-7,8,2,-6,9,9,3,8,-4,1,7,3,2,-1,-10,8,6,9,-1,5,8,4,1,-5,9,8,-1,4,-4,-10,3,-2,-5], dtype = "int64")#candidate|1415|(700,)|const|int64
bop_1416 = relay.greater(call_1400.astype('bool'), relay.reshape(const_1415.astype('bool'), relay.shape_of(call_1400))) # shape=(700,)
bop_1419 = relay.greater(call_1401.astype('bool'), relay.reshape(const_1415.astype('bool'), relay.shape_of(call_1401))) # shape=(700,)
uop_1432 = relay.exp(bop_1416.astype('float32')) # shape=(700,)
uop_1434 = relay.exp(bop_1419.astype('float32')) # shape=(700,)
var_1436 = relay.var("var_1436", dtype = "float32", shape = (700,))#candidate|1436|(700,)|var|float32
bop_1437 = relay.logical_or(uop_1432.astype('bool'), relay.reshape(var_1436.astype('bool'), relay.shape_of(uop_1432))) # shape=(700,)
bop_1440 = relay.logical_or(uop_1434.astype('bool'), relay.reshape(var_1436.astype('bool'), relay.shape_of(uop_1434))) # shape=(700,)
func_487_call = mod.get_global_var('func_487')
func_490_call = mutated_mod.get_global_var('func_490')
var_1442 = relay.var("var_1442", dtype = "float32", shape = (108,))#candidate|1442|(108,)|var|float32
const_1443 = relay.const([-1,5,3,-7,10,-6,-3,-10,-5,4,5,-4,1,-2,-2,-9,6,-6,-3,1,-7,8,2,-4,2,10,-1,10,2,4,-4,6,-4,10,-7,1,-10,5,-6,10,-8,-7,-5,-2,-10,-1,-9,4,-1,-1,7,-4,2,10,-8,-7,-1,7,3,4,-6,-6,2,-8,-6,1,4,2,-5,-5,-3,1,-9,1,-10,3,-10,10,-9,-6,1,8,-5,3,-3,4,3,1,4,1,-8,9,-5,1,1,-1,-7,10,-9,1,-3,1,10,5,-3,7,3,9,-5,4,-10,-10,3,-8,-3,8,3,2,-9,-7,-5,6,-10,-8,9,-3,-4,-3,-1,1,9,-1,-7,8,-2,-2,1,7,-7,6,-8,3,2,-10,7,8,-1,10,2,7,5,10,-9,7,3,-2,-4,2,-2,-8,4,-7,-3,-6,-7,8,2,5,-5,9,-8,9,-7,6,5,-10,-10,-5,-6,-9,-4,2,-4,-9,-1,-9,1,-9,-10,10,10,4,5,-4,-10,3,-9,2,-3,-4,-1,-3,2,-3,-8,-8,2,-8,-3,7,7,-9,-4,2,4,-2,-9,-9,9,-3,-6,-5,5,5,-8,-5,-2,-1,-5,-6,9,4,-2,-10,7,-8,-6,-9,-8,3,9,-9,10,9,-1,4,2,-9,-3,7,-2,-10,10,1,6,-2,-10,5,-10,-9,1,2,-3,10,-8,3,2,8,5,-7,-3,-5,1,7,6,4,-9,-1,-7,-6,7,-5,-5,10,4,10,-8,4,-4,-1,-7,10,-1,-8,-1,3,6,-7,-5,-10,8,-8,-4,8,-5,10,5,-8,2,-5,2,3,10,-10,8,-3,9,-5,-6,-3,-1,3,-5,-4,-8,-2,-9,-10,-6,3,2,2,-5,-6,-7,2,-2,-6,5,-5,-1,3,1,-8,-4,1,-6,9,8,-2,4,5,-8,-2,2,-6,-4,2,2,10,-2,-4,-4,10,8,-8,-8,6,-5,1,-6,10,-3,5,4,-1,-8,3,-8,5,4,8,-8,8,-5,-3,-5,10,5,3,-3,-4,-1,-3,9,-5,-1,5,-7,5,3,4,-8,5,-2,-3,-5,5,5,5,6,-6,-4,8,-7,5,10,-7,-4,2,-3,2,-3,3,5,-9,-9,9,8,-5,2,-5,9,-1,-6,-2,9,4,9,7,7,-6,-2,10,-4,-7,6,1,5,2,-4,-10,-8,-4,-2,-2,8,5,-5,-4,-1,7,6,-5,-9,-4,-3,5,-9,-10,-1,-1,-2,-3,-3,-6,-9,-4,-9,7,7,-1,6,-2,7,5,4,-9,2,3,-8,-10,10,-3,10,-8,-9,-7,-7,9,3,-5,8,5,-7,-5,-5,-3,6,7,4,-5,6,-10,-3,10,3,-4,9,-2,8,-3,-2,-2,-2,4,-6,-1,-3,7,1,3,-3,8,-8,10,8,3,-10,8,-5,6,-3,6,-1,3,2,-8,5,-9,-6,3,2,6,2,-4,6,10,8,-5,-1,-10,4,-10,-4,6,-9,4,4,5,-3,2,-8,9,8,-6,-2,-2,4,7,-2,-10,9,-4,5,10,-10,-7,5,-6,-10,2,9,-8,5,-5,-8,7,8,-2,-3,-10,5,1,3,-2,2,-5,-5,7,10,-6,4,10,5,4,-6,-2,10,-10,-3,-6,-6,9,7,3,6,10,3,4,1,7,-10,8,-4,-5,-3,-3,5,2,8,1,-5,5,-8,7,7,-7,-4,-7,5,5,-4,-5,-10,10,2,-1,-10,-4,-5,10,-6,-7,3,-9,9,-4,-2,-1,-8,8,10,-9,-4,-1,-6,1,7,4,-3,8,-7,-4,-3,-1,3,1,9,-8,-2,3,9,2,1,7,9,5,-8,-6,1,-2,-7,2,4,2,-8,-6,9,6,-5,4,-10,1,8,-1,-5,5,-7,-1,-8,8,5,4,3,-4,7,-10,8,7,1,5,10,-9,1,-9,-2,-5,-3,3,-3,2,-6,6,-6,-8,-8,2,-4,-8,-10,4,-4,-8,-9,2,-7,-9,9,-7,-8,-3,-9,-6,-5,-10,1,-8,2,-3,7,3,2,-1,9,7,2,-4,2,-3,-4,3,-4,2,6,-9,3,-1,5,-5,7,-2,9,-9,7,9,5,-7,-4,7,6,-5,9,1,7,10,7,4,-9,-8,-4,-8,-10,8,-5,4,-10,-10,6,-2,-7,-8,6,10,-6,2,5,9,-4,-9,-3,-10,-3,-3,-2,-3,-9,5,4,1,-4,-2,-10,4,9,4,-8,8,-7,-4,9,-1,-10,-6,-2,6,9,-4,-10,-4,4,2,6,-5,4,5,-7,-2,1,-3,6,-8,7,3,-10,6,-8,-6,-2,-9,-10,-10,1,4,-1,-4,6,9,3,1,-10,5,-9,4,4,8,10,-1,-9,4,3,6,-1,5,8,7,-4,9,5,-5,-9,-3,8,-1,-8,-6,2,-10,-10,6,2,-7,8,-10,-9,2,-5,-6,-6,1,-1,-6,-10,7,1,7,7,-10,1,-7,-4,-8,-1,-1,3,-2,-10,9,-5,9,10,-1,-1,1,10,2,-7,10,-9,7,-4,6,7,3,2,10,-7,8,-10,10,8,-2,4,-3,7,-5,-10,7,8,9,-2,-1,-8,9,-9,7,-10,-2,-5,9,6,-4,-7,-4,-1,-7,2,3,9,9,10,-5,9,7,2,-5,-10,-5,-10,-1,1,-3,8,-6,-8,4,3,10,-5,-5,5,-5,8,1,8,6,-2,4,-7,-6,5,4,-1,9,3,5,3,4,-10,7,9,-7,6,-10,2,-7,9,-7,8,-6,-10,-1,-1,-4,8,-6,9,-7,-7,-8,-6,-7,8,5,10,7,2,-4,-10,3,2,-6,-5,5,-3,-10,-8,4,-3,-2,-10,-4,6,5,-8,6,8,-10,7,6,8,1,-4,-2,5,1,-2,10,-5,-3,-3,-5,-5,7,-10,-3,8,-4,8,9,-9,-1,-7,8,5,-5,4,-1,-4,-10], dtype = "uint8")#candidate|1443|(1120,)|const|uint8
call_1441 = relay.TupleGetItem(func_487_call(relay.reshape(var_1442.astype('float32'), [2, 6, 9]), relay.reshape(const_1443.astype('uint8'), [1120,]), ), 3)
call_1444 = relay.TupleGetItem(func_490_call(relay.reshape(var_1442.astype('float32'), [2, 6, 9]), relay.reshape(const_1443.astype('uint8'), [1120,]), ), 3)
func_1062_call = mod.get_global_var('func_1062')
func_1064_call = mutated_mod.get_global_var('func_1064')
call_1447 = relay.TupleGetItem(func_1062_call(relay.reshape(const_1443.astype('uint8'), [1120,])), 0)
call_1448 = relay.TupleGetItem(func_1064_call(relay.reshape(const_1443.astype('uint8'), [1120,])), 0)
bop_1462 = relay.right_shift(bop_1437.astype('uint64'), relay.reshape(bop_1416.astype('uint64'), relay.shape_of(bop_1437))) # shape=(700,)
bop_1465 = relay.right_shift(bop_1440.astype('uint64'), relay.reshape(bop_1419.astype('uint64'), relay.shape_of(bop_1440))) # shape=(700,)
func_912_call = mod.get_global_var('func_912')
func_914_call = mutated_mod.get_global_var('func_914')
var_1471 = relay.var("var_1471", dtype = "bool", shape = (1092,))#candidate|1471|(1092,)|var|bool
call_1470 = relay.TupleGetItem(func_912_call(relay.reshape(var_1471.astype('bool'), [13, 14, 6])), 0)
call_1472 = relay.TupleGetItem(func_914_call(relay.reshape(var_1471.astype('bool'), [13, 14, 6])), 0)
output = relay.Tuple([call_1441,var_1442,const_1443,call_1447,bop_1462,call_1470,var_1471,])
output2 = relay.Tuple([call_1444,var_1442,const_1443,call_1448,bop_1465,call_1472,var_1471,])
func_1473 = relay.Function([var_1436,var_1442,var_1471,], output)
mod['func_1473'] = func_1473
mod = relay.transform.InferType()(mod)
mutated_mod['func_1473'] = func_1473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1473_call = mutated_mod.get_global_var('func_1473')
var_1475 = relay.var("var_1475", dtype = "float32", shape = (700,))#candidate|1475|(700,)|var|float32
var_1476 = relay.var("var_1476", dtype = "float32", shape = (108,))#candidate|1476|(108,)|var|float32
var_1477 = relay.var("var_1477", dtype = "bool", shape = (1092,))#candidate|1477|(1092,)|var|bool
call_1474 = func_1473_call(var_1475,var_1476,var_1477,)
output = call_1474
func_1478 = relay.Function([var_1475,var_1476,var_1477,], output)
mutated_mod['func_1478'] = func_1478
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1507 = relay.var("var_1507", dtype = "uint32", shape = ())#candidate|1507|()|var|uint32
const_1508 = relay.const([[[1,-10,-5,3,-9,-4,4]],[[2,6,-9,3,-5,-5,-9]],[[6,-8,1,2,-7,8,2]],[[4,1,1,-10,-10,-10,3]],[[9,4,-8,-4,10,-7,-3]],[[-2,4,-10,4,2,-6,6]],[[-5,-3,10,2,10,7,4]],[[-5,-8,1,-5,-6,-4,4]],[[9,6,-10,2,8,8,-10]],[[6,-10,8,-1,9,-9,6]]], dtype = "uint32")#candidate|1508|(10, 1, 7)|const|uint32
bop_1509 = relay.left_shift(var_1507.astype('uint32'), const_1508.astype('uint32')) # shape=(10, 1, 7)
output = bop_1509
output2 = bop_1509
func_1526 = relay.Function([var_1507,], output)
mod['func_1526'] = func_1526
mod = relay.transform.InferType()(mod)
mutated_mod['func_1526'] = func_1526
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1527 = relay.var("var_1527", dtype = "uint32", shape = ())#candidate|1527|()|var|uint32
func_1526_call = mutated_mod.get_global_var('func_1526')
call_1528 = func_1526_call(var_1527)
output = call_1528
func_1529 = relay.Function([var_1527], output)
mutated_mod['func_1529'] = func_1529
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1561 = relay.var("var_1561", dtype = "float32", shape = (7, 11, 9))#candidate|1561|(7, 11, 9)|var|float32
uop_1562 = relay.exp(var_1561.astype('float32')) # shape=(7, 11, 9)
output = uop_1562
output2 = uop_1562
func_1564 = relay.Function([var_1561,], output)
mod['func_1564'] = func_1564
mod = relay.transform.InferType()(mod)
var_1565 = relay.var("var_1565", dtype = "float32", shape = (7, 11, 9))#candidate|1565|(7, 11, 9)|var|float32
output = func_1564(var_1565)
func_1566 = relay.Function([var_1565], output)
mutated_mod['func_1566'] = func_1566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_875_call = mod.get_global_var('func_875')
func_877_call = mutated_mod.get_global_var('func_877')
call_1642 = relay.TupleGetItem(func_875_call(), 0)
call_1643 = relay.TupleGetItem(func_877_call(), 0)
func_1077_call = mod.get_global_var('func_1077')
func_1080_call = mutated_mod.get_global_var('func_1080')
const_1659 = relay.const([-7.871537,-1.877132,3.092297,-6.557939,5.092354,5.446488,-7.619325,1.196834,-7.641121,-6.360144,-2.566646,7.454417,5.365132,-1.160641,5.476872,-9.833580,4.497754,8.528917,8.946147,-7.420801,0.741655,0.708164,-4.934172,8.941934,-5.246961,-8.022829,-9.330291,9.596194,7.235329,4.838629,9.187209,-9.637476,-3.574565,6.012736,1.054592,0.550143,-0.907281,-0.264061,9.995756,7.071489,7.229055,4.404920,5.840728,-4.468899,-0.600655,6.667051,5.021318,-2.574883,4.636783,6.807807,-4.253837,7.493788,2.161392,6.051740,-9.041155,-3.240731,7.178565,6.716020,7.215169,4.863814,2.336700,2.882919,-2.530981,3.711477,2.429660,-9.599077,0.286550,-5.696515,7.503368,4.708464,-7.376700,-1.191525,0.469367,-7.028337,1.216025,-2.030799,-7.699348,2.871662,-6.247327,4.923962,-9.269303,6.630607,8.920361,-3.539070,8.973793,-9.473929,-5.400596,5.141684,2.575517,-8.433743,2.753771,6.311739,-1.474282,-2.098771,0.421689,-9.448328,2.201365,7.617254,-4.718218,-8.935806,-2.687665,1.180584,6.328004,-9.384901,5.666838,2.558565,-9.870536,-0.861336,8.444033,0.686777,-9.261095,-6.690992,4.577371,1.781286,-7.559261,1.362041,-2.929588,9.962780,-8.993307,-1.460057,-0.776161,-2.875373,1.590578,1.804130,-1.152757,8.683466,-2.113269,-9.524506,-5.101319,5.146261,7.853663,9.308489,-1.472198,8.846188,-9.499488,-3.503595,6.728124,2.979875,9.889416,-1.223523,9.635436,9.531741,3.667923,8.020991,0.039225,-3.228411,-3.964867,-1.688514,-1.475905,1.285830,-5.349436,0.470670,-9.429615,-4.428103,6.468913,4.649911,-9.422137,2.794410,4.051431,0.029859,4.364711,3.700971,4.037375,-5.587454,-6.129729,6.989662,4.624402,-1.778157,4.930623,-0.927991,1.816046,-4.939726,-3.921726,-4.264827,-1.916227,-1.496543,4.553297,6.193581,7.452917,6.288668,3.799168,-4.610239,4.004780,6.825314,9.825642,-2.784614,9.046334,4.598347,-7.806612,1.825368,9.482756,-7.184303,-4.778220,-2.181648,-1.271052,0.027822,-7.208280,-5.140031,-0.652593,-0.968988,2.496147,7.712509,2.758783,-2.815199,-6.005288,9.948288,3.550152,-6.174062,2.356500,-1.260438,-7.893292,-3.896098,3.614847,8.186681,-4.408161,-3.136971,-0.125699,-1.721296,-9.971059,6.772499,6.732145,-5.653530,-3.869149,-9.411245,4.171851,8.559421,-4.252524,-6.030660,5.777691,6.124432,-7.422867,9.386912,1.547627,-0.272381,9.280242,-0.595315,-5.323926,4.817832,-3.561214,7.950995,-5.305705,8.719072,-6.760393,0.110646,9.142823,8.673813,-3.235184,-4.917985,-9.061096,5.543319,-8.604371,-7.852450,-2.849521,-0.492050,1.292108,8.310249,-2.473318,-4.547883,-9.898769,-1.992078,5.598403,5.763142,2.325366,4.108407,0.599659,7.550876,7.009284,-5.989931,3.699629,-0.949092,-9.279887,9.991156,-6.814747,1.002258,4.306875,7.210717,8.058718,-4.937059,-6.167535,0.928726,-3.580154,-8.175910,-6.731111,2.244074,3.409675,5.832530,1.416454,-0.595675,-3.680364,5.301798,-2.397385,-8.664555,9.064133,-6.567938,4.117934,9.708188,-3.749881,6.808019,0.102076,-5.626702,-5.255170,-8.774599,-2.717161,9.995151,9.237202,-1.066409,3.484776,5.113549,8.563209,0.346840,5.684018,-1.093650,-2.578339,2.188731,8.520404,-3.683159,3.661463,4.238752,0.030293,-0.994159,4.161883,-4.978683,-0.842528,-1.927871,4.229375,-9.420584,-5.720589,-1.578769,-1.310533,-1.747416,-1.431665,0.081410,-1.172344,9.835158,9.239447,-3.182945,4.836517,-6.240639,-4.910225,3.420296,-9.788629,3.233232,0.287436,3.947121,2.694852,8.186773,-4.688307,6.836308,0.982198,-8.677840,-3.997426,-5.557295,-8.446713,9.370089,1.684716,-9.639203,-0.446274,-7.161983,-5.579073,8.851799,-3.496274,6.769586,2.436247,8.897158,7.175759,-2.659723,-1.900231,4.830158,6.837940,0.357523,-5.410716,-0.453328,6.675190,-2.815693,-0.076916,8.663045,-0.236630,4.890010,3.811422,-7.900382,-4.060766,0.119048,0.059305,0.169737,7.377091,5.354757,6.215349,5.696455,4.448392,-5.509129,1.988015,-1.666187,-1.394646,-6.993705,-4.885281,-9.706141,0.424589,9.209822,9.304459,9.886727,4.883031,-9.347245,-6.988967,-5.281318,8.193216,7.783759,-9.137875,-5.804696,0.738288,1.120988,7.388059,-9.587256,1.665747,-9.290525,0.496819,9.058679,-1.313735,5.314682,7.158175,-3.230046,-4.766833,-1.732649,0.609938,1.993940,3.779118,-7.826785,-8.475302,6.087931,-5.760340,-8.363718,5.040338,9.729522,3.351210,-0.370990,-8.424989,0.445396,-6.156321,2.953593,-8.137649,-9.237791,0.644938,4.482971,0.622717,3.312490,-9.910882,2.172521,-3.183739,5.876033,8.531911,-3.941534,5.316535,-5.845384,6.880526,5.003923,-2.942708,6.557838,2.957351,-1.201793,1.054097,-1.615183,4.219590,0.199011,-8.154730,-3.862344,-0.124572,2.144192,-6.904449,7.644011,-4.371106,-5.717898,-7.209253,-2.857387,-3.591287,4.542781,0.669778,8.731050,8.243756,-2.715217,7.727126,-7.585859,8.135245,8.213830,8.234186,-3.269231,-9.934710,6.090559,-5.194392,-6.797490,-0.288297,3.672781,9.929192,-5.305522,6.985897,1.583134,7.281167,1.691024,9.674700,5.835629,8.092556,-0.435050,-4.987920,6.106893,-2.988885,3.156665,9.840615,-1.470954,6.614623,7.678211,0.188276,6.384096,-0.423513,6.534381,-0.526319,1.696062,-5.686270,6.533108,9.169062,-8.276315,-3.586500,-2.030312,-8.272704,-0.232555,9.473170,-1.980892,-8.991295,-4.941161,-4.174669,6.255345,-8.174118,3.222934,-2.430988,0.165174,5.124752,5.133637,9.648496,0.184923,-5.560881,2.963033,6.018830,-5.522638,0.674287,5.416568,6.862106,-3.137992,8.243545,-2.957817,-7.587538,8.665801,7.004150,8.392269,-7.929116,-2.468700,6.828403,-9.832330,-6.858472,-9.565546,0.870770,2.867639,-2.879581,-0.842760,7.417270,-8.457106,-5.563344,4.657930,-5.337520,-2.426283,0.103995,-9.476236,-3.905656,-0.161211,7.050957,9.869131,-7.185399,4.270496,-1.881814,-6.938027,2.435655,-0.316122,-9.717916,2.489463,-4.322332,8.476795,2.614574,-9.131870,-0.853148,-7.534742,-3.964011,0.321462,-5.448506,8.095430,-1.660768,6.020203,-9.472269,-6.367281,4.345322,-9.876720,6.944564,-0.719673,7.171257,7.217115,9.509395,2.330862,9.334254,-6.875360,-3.093203,-4.478476,8.157570,-1.194713,5.803077,-2.690361,-3.298604,1.951020,-6.718178,-9.098717,-5.532473,5.101392,7.044204,7.012522,5.296739,1.159272,-5.566530,8.519246,4.923318,3.077542,-1.417718,9.478152,-8.866251,-7.317685,-4.567067,-7.290461,-9.282976,-9.416480,4.118077,-9.058868,8.377106,-0.128847,-6.578140,5.135446,3.336400,-6.546018,-5.501184,-4.562601,-0.161949,4.077813,-2.837431,-0.031646,-2.843570,-4.740433,-0.668008,-1.023354,-3.323543,7.016258,-9.266624,-9.579439,-2.897279,5.523747,2.503857,5.798146,5.645896,-4.918461,9.383950,-0.696893,-6.184860,6.651055,-8.543717,-3.444734,-1.597909,5.235159,4.374665,-4.830507,-3.417113,-8.225621,2.813855,-6.299233,6.004479,-7.320462,0.906396,-8.390734,-0.864485,-5.134888,3.219093,6.338133,9.237944,0.483149,8.323786,-2.200938,2.815417,3.244045,-3.409443,0.359944,-3.704860,-9.267982,2.534041,7.041206,-3.435032,-0.346061,1.426671,9.981864,-6.944622,2.356873], dtype = "float64")#candidate|1659|(700,)|const|float64
call_1658 = func_1077_call(relay.reshape(const_1659.astype('float64'), [7, 10, 10]))
call_1660 = func_1077_call(relay.reshape(const_1659.astype('float64'), [7, 10, 10]))
func_571_call = mod.get_global_var('func_571')
func_576_call = mutated_mod.get_global_var('func_576')
var_1663 = relay.var("var_1663", dtype = "uint8", shape = (1120,))#candidate|1663|(1120,)|var|uint8
call_1662 = relay.TupleGetItem(func_571_call(relay.reshape(call_1642.astype('float64'), [2, 6, 9]), relay.reshape(call_1642.astype('float64'), [2, 6, 9]), relay.reshape(var_1663.astype('uint8'), [4, 280]), ), 4)
call_1664 = relay.TupleGetItem(func_576_call(relay.reshape(call_1642.astype('float64'), [2, 6, 9]), relay.reshape(call_1642.astype('float64'), [2, 6, 9]), relay.reshape(var_1663.astype('uint8'), [4, 280]), ), 4)
output = relay.Tuple([call_1642,call_1658,const_1659,call_1662,var_1663,])
output2 = relay.Tuple([call_1643,call_1660,const_1659,call_1664,var_1663,])
func_1672 = relay.Function([var_1663,], output)
mod['func_1672'] = func_1672
mod = relay.transform.InferType()(mod)
var_1673 = relay.var("var_1673", dtype = "uint8", shape = (1120,))#candidate|1673|(1120,)|var|uint8
output = func_1672(var_1673)
func_1674 = relay.Function([var_1673], output)
mutated_mod['func_1674'] = func_1674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1258_call = mod.get_global_var('func_1258')
func_1259_call = mutated_mod.get_global_var('func_1259')
call_1684 = relay.TupleGetItem(func_1258_call(), 0)
call_1685 = relay.TupleGetItem(func_1259_call(), 0)
output = relay.Tuple([call_1684,])
output2 = relay.Tuple([call_1685,])
func_1690 = relay.Function([], output)
mod['func_1690'] = func_1690
mod = relay.transform.InferType()(mod)
mutated_mod['func_1690'] = func_1690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1690_call = mutated_mod.get_global_var('func_1690')
call_1691 = func_1690_call()
output = call_1691
func_1692 = relay.Function([], output)
mutated_mod['func_1692'] = func_1692
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1725 = relay.var("var_1725", dtype = "float32", shape = (6, 11))#candidate|1725|(6, 11)|var|float32
uop_1726 = relay.rsqrt(var_1725.astype('float32')) # shape=(6, 11)
output = uop_1726
output2 = uop_1726
func_1741 = relay.Function([var_1725,], output)
mod['func_1741'] = func_1741
mod = relay.transform.InferType()(mod)
mutated_mod['func_1741'] = func_1741
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1742 = relay.var("var_1742", dtype = "float32", shape = (6, 11))#candidate|1742|(6, 11)|var|float32
func_1741_call = mutated_mod.get_global_var('func_1741')
call_1743 = func_1741_call(var_1742)
output = call_1743
func_1744 = relay.Function([var_1742], output)
mutated_mod['func_1744'] = func_1744
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1786 = relay.var("var_1786", dtype = "float32", shape = (11, 4, 3))#candidate|1786|(11, 4, 3)|var|float32
uop_1787 = relay.log2(var_1786.astype('float32')) # shape=(11, 4, 3)
output = relay.Tuple([uop_1787,])
output2 = relay.Tuple([uop_1787,])
func_1801 = relay.Function([var_1786,], output)
mod['func_1801'] = func_1801
mod = relay.transform.InferType()(mod)
mutated_mod['func_1801'] = func_1801
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1802 = relay.var("var_1802", dtype = "float32", shape = (11, 4, 3))#candidate|1802|(11, 4, 3)|var|float32
func_1801_call = mutated_mod.get_global_var('func_1801')
call_1803 = func_1801_call(var_1802)
output = call_1803
func_1804 = relay.Function([var_1802], output)
mutated_mod['func_1804'] = func_1804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1258_call = mod.get_global_var('func_1258')
func_1259_call = mutated_mod.get_global_var('func_1259')
call_1889 = relay.TupleGetItem(func_1258_call(), 1)
call_1890 = relay.TupleGetItem(func_1259_call(), 1)
func_1473_call = mod.get_global_var('func_1473')
func_1478_call = mutated_mod.get_global_var('func_1478')
const_1912 = relay.const([[9.193515,-9.280415,5.219336,6.331080,2.376551,-4.083506,3.155432,-4.540304,-7.437252,-1.256388,-3.474722,-7.865293,-7.353667,-4.576584,2.330919,7.131111,0.271417,-8.472886,-0.776761,5.818988,9.799295,8.619338,-5.347347,7.559902,-7.998281,3.632500,3.821745,6.134979,0.561965,-0.293259,-2.450596,7.344274,9.877387,-7.944503,-1.655404,-4.936356,6.426835,-7.041618,7.302740,-3.294116,-7.437966,-7.992662,-7.244059,1.643360,2.525338,-7.539769,3.976325,6.367895,2.616971,-3.640442,0.006969,-1.914262,1.336798,-1.272079,-2.371417,-3.244461,-2.795729,-0.560380,4.433701,-8.813961,2.565905,-4.996957,9.584367,6.391309,4.252123,-9.779732,-5.691010,2.625051,1.919355,-4.728672,8.447682,-6.125940,3.930772,-1.451599,0.173421,7.379384,2.241838,5.273429,-1.273756,-6.312073,9.933502,-2.351966,5.222233,8.451086,-9.946321,-6.261438,-5.539183,9.315533,4.196689,-4.918589,0.556073,4.464670,8.598411,1.826487,6.842115,5.801673,-3.564483,5.247345,-8.506666,-0.189021,-9.099574,-0.827646,-7.330874,1.501530,9.982178,-2.203290,0.976656,4.982748]], dtype = "float32")#candidate|1912|(1, 108)|const|float32
var_1913 = relay.var("var_1913", dtype = "bool", shape = (1092,))#candidate|1913|(1092,)|var|bool
call_1911 = relay.TupleGetItem(func_1473_call(relay.reshape(call_1889.astype('float32'), [700,]), relay.reshape(const_1912.astype('float32'), [108,]), relay.reshape(var_1913.astype('bool'), [1092,]), ), 2)
call_1914 = relay.TupleGetItem(func_1478_call(relay.reshape(call_1889.astype('float32'), [700,]), relay.reshape(const_1912.astype('float32'), [108,]), relay.reshape(var_1913.astype('bool'), [1092,]), ), 2)
func_875_call = mod.get_global_var('func_875')
func_877_call = mutated_mod.get_global_var('func_877')
call_1925 = relay.TupleGetItem(func_875_call(), 0)
call_1926 = relay.TupleGetItem(func_877_call(), 0)
output = relay.Tuple([call_1889,call_1911,const_1912,var_1913,call_1925,])
output2 = relay.Tuple([call_1890,call_1914,const_1912,var_1913,call_1926,])
func_1941 = relay.Function([var_1913,], output)
mod['func_1941'] = func_1941
mod = relay.transform.InferType()(mod)
mutated_mod['func_1941'] = func_1941
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1942 = relay.var("var_1942", dtype = "bool", shape = (1092,))#candidate|1942|(1092,)|var|bool
func_1941_call = mutated_mod.get_global_var('func_1941')
call_1943 = func_1941_call(var_1942)
output = call_1943
func_1944 = relay.Function([var_1942], output)
mutated_mod['func_1944'] = func_1944
mutated_mod = relay.transform.InferType()(mutated_mod)
func_900_call = mod.get_global_var('func_900')
func_902_call = mutated_mod.get_global_var('func_902')
call_1950 = relay.TupleGetItem(func_900_call(), 0)
call_1951 = relay.TupleGetItem(func_902_call(), 0)
output = call_1950
output2 = call_1951
func_1963 = relay.Function([], output)
mod['func_1963'] = func_1963
mod = relay.transform.InferType()(mod)
mutated_mod['func_1963'] = func_1963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1963_call = mutated_mod.get_global_var('func_1963')
call_1964 = func_1963_call()
output = call_1964
func_1965 = relay.Function([], output)
mutated_mod['func_1965'] = func_1965
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1972 = relay.var("var_1972", dtype = "float32", shape = (15, 15, 12))#candidate|1972|(15, 15, 12)|var|float32
uop_1973 = relay.atan(var_1972.astype('float32')) # shape=(15, 15, 12)
uop_1978 = relay.asinh(var_1972.astype('float64')) # shape=(15, 15, 12)
func_1473_call = mod.get_global_var('func_1473')
func_1478_call = mutated_mod.get_global_var('func_1478')
const_1983 = relay.const([[-5.057888,-6.554424],[9.932580,4.712629],[7.882139,1.673246],[-2.879746,0.292918],[-1.901966,1.374574],[4.602097,-3.861984],[-2.627221,-2.953697],[-9.382196,2.806445],[5.628578,8.379800],[-5.732151,8.619253],[8.748390,-9.091950],[-1.205612,-4.227530],[7.145393,1.445932],[-6.986053,3.655254],[-1.779819,1.445816],[6.954700,0.897959],[6.121407,5.653127],[-2.974709,7.249563],[1.571900,4.812017],[8.997404,-5.911185],[3.304292,3.638854],[5.131483,-8.369885],[-4.724308,-2.249365],[7.080648,-7.129917],[-6.061159,-5.695131],[9.630101,-0.789781],[0.657631,-7.235211],[-1.074498,-5.220443],[-5.700717,2.166154],[-9.430132,0.373121],[9.147436,-4.786437],[-4.646194,3.193756],[-2.670809,2.281360],[1.676206,-8.026626],[0.553948,-3.281291],[4.654721,-7.449551],[-0.575568,-5.176542],[3.431485,-0.343195],[4.766496,8.688464],[7.159561,1.641805],[-0.765173,3.511638],[-9.716181,9.983069],[-5.562134,9.424652],[-6.990783,-9.413800],[4.730164,5.687347],[-1.863449,-9.580265],[-4.323026,9.601406],[-3.784757,2.222140],[2.515420,1.606595],[-2.585529,-8.830890],[-3.610612,-8.349650],[8.909278,9.750221],[5.000370,8.483589],[-7.910211,-3.741677],[-3.179553,1.266823],[-4.456113,7.674011],[6.745276,5.323246],[1.580454,3.280787],[-7.406575,-7.252950],[-8.673875,-2.923639],[-0.034618,4.391599],[5.633319,1.912397],[-7.054649,1.931561],[5.452986,-3.031341],[5.770121,-5.777177],[5.735853,-0.983417],[-5.719126,2.714219],[-4.459688,-0.400884],[-5.902547,-0.556476],[8.023019,5.590303],[-6.984482,-7.342553],[9.317283,-1.031592],[6.247827,-3.043040],[-0.753968,-6.599880],[3.528249,4.713155],[5.922447,2.599349],[-7.045664,-8.934655],[6.530024,8.696232],[-8.860354,-9.571082],[-6.804032,-0.552531],[0.110203,5.658172],[8.227994,-0.731663],[1.914505,-8.142057],[-0.846885,-9.494750],[9.033461,-9.450781],[-4.374773,-8.522323],[-4.776411,4.785806],[-3.897458,-1.369868],[-6.185250,2.276401],[0.201525,-2.277781],[-6.418090,1.567286],[-7.109331,5.144387],[-9.018419,0.106056],[1.209800,7.804877],[-9.378414,-6.008143],[-9.137980,-0.046082],[-7.942945,-7.414009],[-1.502537,5.499614],[-0.496568,0.135094],[-4.540090,-9.188867],[-2.340891,-0.767381],[-4.962592,7.057895],[-3.295489,8.562607],[-3.272028,8.214922],[2.137030,-6.675305],[-4.545379,-6.287103],[4.244580,-5.534586],[-5.298410,-0.476498],[-3.730655,-5.686411],[4.445075,5.955525],[-9.171003,-7.576093],[-0.253925,1.134340],[-2.934942,1.227482],[3.994894,0.170570],[2.111727,5.970970],[-1.453026,2.314608],[-3.083346,1.729595],[0.687087,7.314094],[2.543780,5.086650],[4.529183,-6.155942],[-7.897878,-4.063070],[8.157855,-9.711510],[2.312313,6.490998],[-5.029042,-3.853122],[-3.049288,-0.838658],[-8.977056,9.234690],[1.941756,-7.991440],[-6.534267,-5.710131],[-2.795324,-0.941146],[-1.413986,7.351409],[-7.451220,-1.233888],[1.039596,2.923127],[-8.067341,0.407779],[3.301294,2.841159],[2.070700,9.613289],[-7.738586,4.718415],[2.315169,-6.885322],[-4.436616,6.826730],[-2.065507,8.561707],[9.809657,-4.102432],[-4.879453,-5.560485],[-0.826106,3.510907],[3.911043,5.324420],[-1.141739,3.180774],[7.770698,-8.646299],[7.822182,-8.485922],[5.291045,1.001277],[3.297818,-0.138143],[2.680516,0.252504],[-4.433512,-3.225102],[-4.415930,9.366061],[-6.747613,-6.752238],[6.145467,2.190407],[-7.081177,-4.893004],[-9.502722,-9.869544],[0.285323,5.295323],[-5.053150,2.260682],[4.212262,-4.875305],[0.655009,9.825385],[-3.031781,4.153820],[-5.126367,-1.263428],[3.960956,-0.042434],[-0.794478,3.405369],[2.564073,8.352447],[8.782499,9.785627],[-2.066096,-6.250420],[0.673892,6.699108],[2.346536,1.167389],[9.127494,5.627114],[9.634421,-6.949706],[-0.443793,5.482014],[2.952083,5.227415],[4.133992,4.346171],[9.017432,-1.088784],[1.360442,-8.610914],[-7.399048,-2.425256],[-5.229402,-9.076596],[2.995038,1.924337],[-7.505808,-9.208865],[3.441082,9.071181],[-5.906721,-4.366977],[-3.226180,-2.609804],[-3.800765,2.698505],[0.142043,5.684584],[1.346324,4.650795],[-9.799755,-2.140265],[6.019342,-4.861134],[6.014674,-0.022473],[0.912906,9.595729],[6.741309,7.995781],[-8.467951,-1.280613],[4.225581,9.138105],[-3.372884,2.422479],[-4.716642,3.768269],[-5.008101,-8.953164],[8.076944,8.601552],[-3.709124,8.123112],[1.887683,4.424244],[1.857054,2.626902],[4.998058,5.235972],[3.943397,7.920798],[-7.792237,3.581437],[-5.536702,-2.056414],[-1.246434,-4.405172],[-8.630927,-8.754675],[9.740988,-3.764400],[-6.324154,4.685762],[-7.373759,4.655522],[0.726364,2.953057],[7.895142,5.200289],[1.886592,-7.825483],[3.913210,-8.441415],[-2.659408,1.800188],[-3.758997,-9.312361],[6.187583,2.024581],[-6.332390,0.122649],[7.652717,7.387980],[-0.030302,-5.694072],[7.909535,3.792280],[-2.234640,-3.731526],[9.091624,-8.025190],[3.533694,-4.373068],[-3.481096,4.410988],[-0.445544,-2.836584],[0.953794,-5.517276],[-6.955807,3.697445],[5.442223,5.018268],[-6.007046,-9.179414],[3.797337,-5.997127],[3.633125,-6.789219],[-9.197389,-6.909580],[-5.112509,-8.728054],[0.764636,8.071601],[3.844870,5.456126],[-0.668489,-7.737319],[-3.467013,-0.085605],[8.401412,1.008087],[7.535386,-3.193515],[3.788795,-1.539412],[-2.465500,3.383426],[3.138886,3.871364],[-1.206000,-2.744623],[6.911047,9.024519],[8.327797,-4.152067],[-2.328669,-0.906206],[3.754485,6.351371],[4.383516,-4.584989],[-6.403238,2.243815],[3.833853,2.856810],[4.851152,-1.569652],[-5.551219,5.324380],[9.041284,5.882364],[1.719606,3.363471],[-7.640905,8.729868],[-4.287093,3.744340],[3.322455,-0.885028],[-5.046063,-1.757694],[8.917149,-6.071954],[7.162988,-0.644129],[4.478252,-2.921219],[1.555014,3.977730],[1.451373,0.972769],[3.637985,-9.208979],[-3.067570,4.206536],[-8.783668,-3.281660],[-3.217023,-8.558178],[-6.664019,-1.985844],[-3.703370,-9.764072],[-3.777208,5.250327],[-4.672811,8.164001],[-8.976613,9.893658],[-8.931407,4.393054],[-6.109451,8.451216],[-9.067870,-9.951535],[-6.555510,7.401535],[-2.915317,-7.437134],[4.197884,-1.564256],[-1.153728,8.109186],[8.851705,8.391280],[1.855219,0.792903],[8.136415,-8.374307],[-3.434670,-1.324904],[0.611521,0.260447],[-1.470975,-9.701471],[4.209951,9.264786],[-5.435798,-2.126311],[3.297372,-1.223664],[-3.653226,0.332764],[-7.263413,-1.978178],[-3.695988,4.298362],[-7.085775,7.977342],[-9.401838,-2.998475],[-4.709015,1.395630],[3.772153,0.071799],[-8.326557,3.523082],[5.381565,-9.418266],[7.263290,-1.210875],[6.433807,3.041702],[-7.210103,-9.950076],[0.877215,-4.544953],[8.955752,-6.575209],[-2.924261,3.017602],[8.246886,2.741373],[1.504781,-6.671821],[-3.832944,8.132009],[-5.397306,9.893214],[5.227840,6.852800],[4.002950,3.264000],[-3.276395,4.903972],[0.113798,9.440823],[0.851755,7.617935],[-0.629975,5.068579],[-4.955846,-8.172329],[-4.820838,2.363166],[-8.981993,-3.204614],[-6.390293,-7.833275],[0.649455,1.492002],[-4.836683,-2.622346],[-9.546466,9.164651],[3.172767,7.217216],[2.141733,6.032823],[-7.269159,5.551127],[4.126762,-8.248669],[8.917027,-4.802351],[-6.709301,5.994157],[-0.251877,-4.646692],[1.862146,9.322542],[2.659672,-5.923541],[2.642233,-6.585328],[-5.371101,-4.556841],[8.968625,-5.431401],[9.226832,6.901035],[-0.468598,-3.660218],[-0.399520,7.393331],[-3.621590,0.781241],[-3.308403,-1.597277],[1.898486,4.720079],[7.088834,7.135301],[-6.394231,5.927179],[2.516985,5.444810],[-3.595870,-3.306157],[-4.602350,-2.375351],[0.397547,-8.754515],[-6.697587,1.284536],[9.335145,6.429788],[-5.644502,9.275485],[-2.032509,-6.941721],[-2.047345,-4.142344],[1.322389,7.210362],[-8.592237,1.413014]], dtype = "float32")#candidate|1983|(350, 2)|const|float32
const_1984 = relay.const([-5.386083,0.312407,3.876804,-1.618496,-5.952562,-4.153578,5.898781,-7.419202,-5.348011,-5.533272,9.787482,-0.586643,9.969725,3.109760,5.938221,-1.459720,0.197997,-2.777984,3.119429,-7.850030,-4.015264,-7.239377,9.108202,7.619407,2.152900,-7.340980,-2.609037,2.766772,-2.824219,-2.723678,2.286033,9.961790,2.803831,-9.707777,9.443094,-4.760504,5.126566,9.774701,6.439043,0.797046,-0.860574,9.505209,-5.567099,-9.318352,-9.534991,-7.682517,-6.149677,-9.726529,4.750817,-4.488526,-8.564028,0.116135,8.789244,-2.048823,5.313062,-8.245282,1.126103,-2.851891,-4.671358,-4.683248,-1.998251,-2.120132,7.302256,-9.030414,3.282992,5.414361,4.012360,-3.189579,2.593667,0.183354,-9.108636,-0.798691,2.356620,9.160940,6.085842,-9.619982,-8.845571,-8.622059,-5.055684,4.400125,4.835904,1.344298,2.356104,-3.981288,-4.340411,3.705616,3.765921,8.839091,6.201335,-2.970818,-9.335131,-0.771424,6.468081,-9.057335,1.109617,-2.732215,-7.720788,5.275154,4.678351,-9.930069,9.405657,-1.843586,6.836998,0.738870,-7.376051,-9.673006,2.850971,8.820209], dtype = "float32")#candidate|1984|(108,)|const|float32
const_1985 = relay.const([[True,True,False,False,False,True,False,False,True,True,False,False,True,True,False,False,True,False,False,False,False,True,True,False,False,False,False,True,False,True,True,True,False,False,True,True,True,True,True,False,False,True,False,False,True,False,False,False,False,True,False,False,False,True,False,True,True,True,False,False,False,True,True,True,True,True,False,False,False,True,False,True,True,False,True,False,False,True,False,False,False,False,False,True,False,True,False,True,False,False,True,False,True,True,True,True,False,True,True,False,True,False,True,False,False,False,False,True,False,False,True,False,False,False,True,False,True,True,False,True,True,True,True,True,False,True,False,False,False,True,True,True,True,False,True,False,True,True,True,True,True,False,True,False,False,True,False,True,False,False,False,False,False,False,True,False,True,True,True,True,False,False,True,False,False,False,False,True,False,True,False,True,True,False,True,False,True,False,True,True,False,False,True,False,False,False,True,True,True,False,False,False,False,True,False,False,False,False,False,False,True,False,True,False,False,True,False,True,True,False,True,True,False,False,False,False,True,True,True,False,True,True,False,True,True,False,True,True,False,True,True,True,False,False,False,False,True,False,False,False,False,True,False,False,True,False,False,False,True,True,True,False,True,True,True,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,True,True,False,True,True,False,False,True,True,True,False,True,False,False,False,False,False,True,True,False,True,True,False,True,False,False,True,False,True,False,False,False,True,True,True,False,True,True,False,True,True,False,False,True,False,True,False,False,False,True,True,True,True,True,False,True,False,True,True,True,True,True,True,True,False,False,True,False,False,True,True,True,False,True,False,False,False,False,True,False,False,False,True,True,True,True,False,True,True,True,False,False,False,True,True,True,False,True,True,False,False,False,True,False,True,True,True,False,False,False,False,False,False,False,True,True,True,True,True,False,False,True,True,False,True,False,True,True,True,False,True,False,False,False,False,False,True,True,False,True,True,False,True,True,False,False,True,False,True,False,False,True,True,True,False,False,False,True,True,True,False,False,True,False,False,False,False,False,True,False,True,True,True,True,False,True,True,True,True,True,True,False,False,True,True,False,True,True,False,True,True,False,True,False,False,False,False,True,False,False,True,True,True,False,False,True,False,False,True,True,True,False,True,True,True,True,False,True,False,False,False,True,False,True,False,False,True,False,True,True,False,True,True,True,True,True,True,True,True,False,True,False,False,False,False,False,True,False,True,False,False,True,True,False,False,True,False,False,False,False,True,False,True,False,False,False,False,True,False,True,True,True,False,True,True,False,True,True,False,False,True,False,True,False,False,False,False,False,False,False,False,True,False,True,False,False,False,False,True,False,True,False,True,True,False,False,True,True,True,True,False,False,True,True,True,True,True,True,False,True,True,False,True,True,False,True,False,False,True,True,False,False,False,True,False,False,True,True,True,True,True,True,True,False,True,False,False,False,True,False,False,False,False,True,False,False,False,False,False,True,True,False,True,True,True,True,True,True,True,True,False,False,False,True,False,True,False,False,False,True,False,False,False,True,True,False,True,True,False,False,False,True,False,True,True,False,True,False,True,False,True,True,False,False,False,False,True,False,True,True,False,True,True,False,False,False,False,False,True,False,False,True,True,False,True,False,False,False,True,True,False,False,False,False,False,True,False,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,False,True,False,True,True,False,True,False,False,True,True,False,True,True,True,False,True,True,True,True,False,False,False,False,False,True,True,True,False,True,True,True,False,True,False,True,True,False,False,True,True,True,False,True,False,True,True,False,False,False,True,True,True,True,True,True,False,False,False,True,True,True,False,True,False,False,True,False,False,True,True,False,False,True,True,False,True,False,False,True,False,True,False,True,False,True,False,True,False,True,False,True,False,False,True,True,False,False,True,True,True,False,True,True,False,False,True,True,False,False,False,False,True,True,False,False,False,False,True,False,True,True,False,False,True,True,True,True,True,False,False,False,False,True,True,False,True,False,True,True,False,False,False,False,True,False,False,True,False,True,False,False,False,False,False,True,True,True,False,False,True,True,False,True,False,True,False,False,True,True,True,False,True,True,False,False,True,False,False,False,True,False,False,True,False,False,False,True,True,False,True,False,True,True,True,False,False,True,False,True,True,True,True,False,True,True,True,False,True,True,False,False,True,False,True,True,False,True,False,True,False,True,True,True,False,True,True,False,False,True,True,True,True,True,False,False,False,True,False,False,False,True,False,True,True,False,False,False,True,False,True,True,True,True,True,True,False,False,True,False,False,False,False,True,True,False,True,False,True,True,False,True,False,False,False,False,False,False,False,False,False,True,True,True,False,False,False,False,True,True,True,True,True,True,False,True,True,True,True,False,False,True,True,True,True,True,True,False,True,True,False,True,False,True,False,True,False,False,True,True,True,False,False,False,True,False,True,False,True,False,False,True,True,True,False,True,False,True,True,True,False,True,False,True,False,False,False,False,False,True,True,True,False,True,False,True,True,True,False,False,False,False,False,True,False,False,False,False,False]], dtype = "bool")#candidate|1985|(1, 1092)|const|bool
call_1982 = relay.TupleGetItem(func_1473_call(relay.reshape(const_1983.astype('float32'), [700,]), relay.reshape(const_1984.astype('float32'), [108,]), relay.reshape(const_1985.astype('bool'), [1092,]), ), 3)
call_1986 = relay.TupleGetItem(func_1478_call(relay.reshape(const_1983.astype('float32'), [700,]), relay.reshape(const_1984.astype('float32'), [108,]), relay.reshape(const_1985.astype('bool'), [1092,]), ), 3)
uop_1991 = relay.asinh(call_1982.astype('float64')) # shape=(2, 6, 9)
uop_1993 = relay.asinh(call_1986.astype('float64')) # shape=(2, 6, 9)
bop_2012 = relay.mod(var_1972.astype('float64'), relay.reshape(uop_1973.astype('float64'), relay.shape_of(var_1972))) # shape=(15, 15, 12)
func_1526_call = mod.get_global_var('func_1526')
func_1529_call = mutated_mod.get_global_var('func_1529')
var_2019 = relay.var("var_2019", dtype = "uint32", shape = ())#candidate|2019|()|var|uint32
call_2018 = func_1526_call(relay.reshape(var_2019.astype('uint32'), []))
call_2020 = func_1526_call(relay.reshape(var_2019.astype('uint32'), []))
func_1258_call = mod.get_global_var('func_1258')
func_1259_call = mutated_mod.get_global_var('func_1259')
call_2021 = relay.TupleGetItem(func_1258_call(), 1)
call_2022 = relay.TupleGetItem(func_1259_call(), 1)
output = relay.Tuple([uop_1978,const_1983,const_1984,const_1985,uop_1991,bop_2012,call_2018,var_2019,call_2021,])
output2 = relay.Tuple([uop_1978,const_1983,const_1984,const_1985,uop_1993,bop_2012,call_2020,var_2019,call_2022,])
func_2025 = relay.Function([var_1972,var_2019,], output)
mod['func_2025'] = func_2025
mod = relay.transform.InferType()(mod)
mutated_mod['func_2025'] = func_2025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2025_call = mutated_mod.get_global_var('func_2025')
var_2027 = relay.var("var_2027", dtype = "float32", shape = (15, 15, 12))#candidate|2027|(15, 15, 12)|var|float32
var_2028 = relay.var("var_2028", dtype = "uint32", shape = ())#candidate|2028|()|var|uint32
call_2026 = func_2025_call(var_2027,var_2028,)
output = call_2026
func_2029 = relay.Function([var_2027,var_2028,], output)
mutated_mod['func_2029'] = func_2029
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2045 = relay.const([[[-1,-2,7,4,-5,6,-3,10,-10,2,3,-10,-7,-10],[2,-5,-6,-9,-4,1,-10,-1,4,10,-8,8,8,-2],[6,1,9,-10,4,-6,-2,8,-3,-5,-10,-3,-7,-2],[8,-9,-6,-2,-8,-2,4,1,-6,-10,-7,8,-1,-8],[9,-3,-3,-1,3,-6,8,3,5,-1,-2,1,-7,-9],[-7,7,6,-5,2,-8,9,-6,-1,2,3,-8,-6,6],[-8,-4,-3,-3,10,-10,3,-7,-1,1,4,-9,-7,-3]],[[5,-8,6,10,-10,-8,2,-5,5,7,-7,-9,4,-1],[6,5,5,6,3,9,-10,8,-7,7,4,-10,-6,5],[1,-2,10,-8,-1,4,-10,-9,-4,-2,-9,4,5,-8],[5,1,-9,-2,-10,-4,3,-7,5,-3,5,9,-4,-7],[7,2,-9,9,-7,7,-9,10,-8,-7,3,1,5,9],[-1,2,4,-1,8,10,-10,3,-7,5,10,-8,2,-8],[-9,8,-5,-9,6,-1,9,10,-6,1,7,-9,-8,7]],[[-8,6,-2,-9,-9,-6,-8,7,-8,-9,1,-10,-7,-3],[-7,4,-5,-5,7,6,2,-10,8,-10,-6,3,-2,-6],[-9,2,1,-3,8,-5,-4,2,-2,-10,10,7,2,5],[-2,-1,-2,-8,10,-1,-3,-3,7,7,-8,10,-9,-7],[-8,3,3,-2,8,10,-3,-6,7,-3,7,-6,7,6],[-6,4,-5,-3,-10,5,-4,6,6,-4,-5,1,-7,6],[2,9,-5,1,10,8,10,-10,8,2,1,-1,2,-6]],[[-7,-2,-6,-9,4,1,-6,5,-4,-10,2,10,-7,10],[3,8,-10,-10,-1,-1,9,-10,3,-10,-2,-1,4,10],[2,-3,-5,6,-3,-6,-5,9,9,10,-7,-10,1,-3],[-5,-8,-2,4,2,-5,-6,9,-7,7,10,-9,8,-5],[-3,3,9,4,2,1,8,9,6,-5,-8,1,10,6],[1,6,-8,-3,2,-10,-5,-8,-6,7,7,-7,6,5],[-9,-5,-2,8,2,9,-9,8,-10,7,7,8,-5,1]],[[2,-7,-6,-5,3,-8,-5,9,-6,7,7,-9,-7,-8],[-1,-4,-4,-6,-3,-1,-4,-1,8,10,1,7,3,-2],[-5,3,-9,9,-9,-8,-5,9,1,-6,-2,-10,-6,-10],[-5,9,3,5,10,9,-8,2,-9,-5,-2,7,9,-8],[-4,-6,-1,8,7,-9,-7,6,7,-1,10,-5,6,10],[-9,2,9,4,-3,5,6,-6,-2,10,-2,-6,-6,-9],[-4,10,7,7,-2,-7,3,-4,6,4,4,-9,-5,-1]],[[7,5,-8,5,7,-1,-4,3,-10,8,6,-6,-4,-7],[10,-9,-5,-10,-9,8,8,-6,-10,2,3,8,2,10],[-8,6,-4,-7,-1,-1,4,8,-1,-6,1,-2,10,6],[3,7,-4,1,9,-4,-9,-3,-4,-4,-3,-7,10,3],[-9,-9,6,6,-2,7,-9,4,-5,8,5,-8,4,-5],[3,2,8,6,1,3,1,5,-10,-7,-3,8,-8,-8],[-10,-7,-2,6,-4,1,6,-9,3,-6,-2,-10,9,6]],[[-2,2,-9,6,-9,9,-7,-9,6,10,1,-2,1,1],[-10,9,-1,-6,1,-2,-6,-4,-3,8,10,-9,-5,7],[5,-8,-4,6,8,-6,6,9,-10,7,-7,-3,2,-9],[4,-3,-1,5,7,-3,-5,-6,-8,3,10,-9,2,4],[-5,10,-9,10,1,-7,1,3,-8,9,6,4,-1,-2],[7,8,1,1,1,1,-9,10,8,-7,4,4,5,5],[3,10,5,9,-4,-3,-4,-6,-3,-2,-4,1,5,10]],[[-5,8,2,7,-4,1,-9,-2,1,5,-8,8,5,10],[5,10,4,-8,-3,-2,-1,6,1,2,-8,7,3,-8],[5,8,7,-9,-5,-7,-10,-7,4,-3,-3,-7,4,-7],[-9,7,10,-3,-5,-7,-9,-3,3,-4,-5,-2,-3,-9],[2,4,-8,7,-6,6,5,4,-10,-5,-8,2,5,10],[-2,5,-5,-7,-1,1,-5,1,-4,3,3,-9,-8,-4],[4,3,3,3,-8,-10,-3,6,-2,9,3,10,-2,9]],[[-9,-5,7,10,-5,-9,-3,1,10,5,6,7,-6,7],[3,9,7,4,1,5,9,8,2,10,-9,-5,-9,-2],[9,-2,-5,4,-5,5,6,-2,5,7,-1,1,-1,3],[-9,2,6,10,-5,3,-5,-5,-10,4,-7,5,9,8],[-2,-8,9,7,-6,-7,1,2,-10,-7,-4,-8,-3,10],[6,-9,-2,9,9,-5,5,9,-1,2,-1,-4,9,7],[4,1,9,8,9,1,5,6,-9,4,7,1,-6,-3]],[[6,6,-1,-10,8,-10,-7,-6,6,-10,8,-4,3,-3],[2,-3,-9,-8,7,9,-6,-4,-7,-5,4,-7,-1,-7],[8,-3,-9,-9,-7,-9,3,-10,6,-1,-4,-7,4,-3],[4,-1,-4,-3,3,1,6,-4,7,-9,-8,5,9,-2],[-5,9,-7,-4,-5,3,-8,7,4,5,5,-2,6,-7],[-9,-7,-6,-6,5,3,4,9,10,-7,9,-6,8,1],[7,-7,9,-3,-10,-1,6,6,-1,3,3,8,4,8]],[[3,-3,9,9,6,4,-10,1,-8,7,2,-1,-1,-8],[-2,-8,8,-5,3,-5,-5,-3,4,10,-2,1,6,8],[-10,4,-5,-9,6,-7,8,-6,-1,-8,4,6,5,-10],[1,2,-6,-7,1,-5,-8,3,-6,-10,9,-3,8,-1],[-9,5,10,-5,-4,-1,-6,9,9,-3,1,2,-1,-7],[4,-1,-8,5,4,8,2,-2,-4,-4,2,-5,-1,7],[2,1,1,-1,2,8,-5,5,-4,6,7,10,-9,6]],[[-4,2,-4,-3,6,-3,9,-4,8,4,6,1,-3,-5],[-7,-10,4,6,4,-5,5,-9,-9,-1,-4,-10,-6,-6],[-1,-9,3,-7,1,7,7,8,-1,-6,-1,9,1,-8],[10,6,-8,-8,-6,10,-2,-3,-10,-9,-9,3,-2,-7],[-4,10,10,5,-2,-9,-10,8,-7,-1,3,9,-4,1],[-5,-9,-5,4,6,3,2,8,2,-6,-8,-7,-6,2],[9,6,-2,-4,1,-2,5,6,-1,1,-2,-2,1,-1]],[[6,-7,-7,-8,7,5,7,-6,7,2,-6,-1,10,-7],[3,-10,-1,3,-9,8,2,-3,-3,3,-10,-7,-8,5],[2,-8,1,-5,4,-10,-8,8,-2,-8,1,6,-6,8],[-1,-1,4,-1,7,9,5,-6,-10,4,-7,-8,6,2],[8,8,-4,4,10,4,3,-1,-3,-3,1,-4,2,1],[-5,-9,-2,4,-6,3,-4,-3,10,-7,-9,5,-10,10],[-10,-9,3,-10,3,-10,-2,4,2,5,1,7,6,2]],[[1,-9,3,8,6,-3,-1,9,-8,9,2,3,10,3],[-2,-4,-7,3,-1,-5,8,7,3,-3,10,-2,-8,4],[-7,-3,-2,-1,10,-8,-7,-7,3,4,-9,-8,1,-1],[-8,-6,-4,3,6,4,2,-6,-6,-3,6,-6,4,-7],[-5,3,-3,-8,10,2,7,-3,-7,7,-3,-4,-8,7],[4,7,10,3,-1,-2,-2,6,-10,10,9,5,-8,10],[-9,7,8,-5,6,-4,8,-5,-2,-2,1,2,-1,-1]]], dtype = "uint16")#candidate|2045|(14, 7, 14)|const|uint16
const_2046 = relay.const([[[-10,6,-3,4,8,-4,10,5,-5,-8,9,-10,-4,4],[-2,8,9,9,4,2,9,8,-6,-7,-10,-10,7,-3],[1,-3,-4,-5,4,7,-9,-1,-6,8,-3,-5,-9,4],[-6,-9,8,10,-2,5,10,5,4,10,6,-4,-2,-2],[5,-7,6,-10,7,-6,-6,4,-4,7,-4,8,4,8],[10,-7,9,7,-1,10,8,6,7,-4,-10,9,-8,5],[-10,10,-7,6,-2,-1,-4,10,9,8,9,-8,-4,6]],[[-5,-6,5,4,2,8,-5,-8,2,-10,5,8,1,4],[3,9,-10,-3,-10,9,-9,7,-5,-4,4,-9,-4,-4],[3,4,7,-5,8,-6,-7,2,1,1,-6,-5,10,9],[3,1,-1,-5,8,-9,-10,-5,-7,4,-6,-6,-1,-3],[6,-5,5,-6,-2,-7,1,-7,1,7,-8,-8,7,9],[4,6,-3,-9,-8,-7,6,-1,1,7,1,-10,6,-5],[1,-8,5,-2,-7,-7,8,5,7,10,-3,2,2,5]],[[1,8,6,-6,3,9,1,-5,9,2,6,-6,10,7],[9,7,-1,-1,-4,-8,-4,-7,3,5,-3,-2,10,2],[-5,1,10,-5,6,10,4,7,4,-5,9,3,-9,-3],[-2,-9,3,-2,-10,3,-6,6,-10,-7,8,-5,4,-8],[-10,1,5,10,2,8,10,9,-6,-5,-9,-3,6,5],[6,4,4,10,7,-7,2,2,9,-8,-6,3,3,4],[4,1,3,-5,-1,6,5,-7,-9,6,10,-4,5,6]],[[3,-9,-7,8,6,-7,-10,-2,-6,-9,8,4,-9,8],[10,-4,-4,-2,5,-3,3,7,2,-8,8,5,3,8],[2,8,2,4,8,6,-6,-6,8,-2,-3,-1,8,-9],[-7,-4,4,8,-5,9,8,9,-4,-5,-6,-3,7,-10],[-9,-7,7,-3,3,-7,6,2,-3,10,-5,2,-1,-10],[10,-5,-10,-5,-4,-8,-4,5,-10,5,-9,-3,-9,-8],[9,-1,8,7,-8,3,-3,-9,5,-6,-3,10,-6,-8]],[[7,5,2,4,2,7,4,-4,-2,-3,-8,-4,9,-3],[-9,8,-7,-4,9,-10,-1,-2,9,-3,10,-10,4,9],[9,8,5,6,9,10,7,-10,6,-3,-2,8,2,-2],[1,2,5,10,6,-1,-5,4,10,-10,9,-1,-10,3],[-6,-2,6,1,-2,3,-6,-2,7,2,-1,6,-6,1],[8,9,8,-5,5,-6,-6,4,5,-2,3,10,6,4],[-4,7,-8,6,-10,-8,8,2,5,5,-4,-2,2,-1]],[[-9,10,9,-5,-6,10,-3,-2,4,-4,-2,1,-7,10],[-7,2,5,9,-1,-8,-5,-4,-9,-9,10,4,-2,7],[7,3,-10,10,-6,9,1,-6,-8,-7,9,-1,-9,1],[1,-3,5,4,10,1,3,5,7,-2,-4,-3,-5,1],[1,-7,10,-3,-7,-2,-3,5,3,9,3,-7,10,-9],[-6,1,4,2,-10,-1,-3,6,-6,-9,-10,8,-2,10],[7,-9,10,2,9,-8,-8,6,1,-9,-10,5,9,-5]],[[8,-2,-7,-10,2,2,4,10,10,7,-5,-8,5,7],[7,-6,1,10,1,-6,-1,-4,-10,-9,10,2,2,-10],[-3,2,3,5,-6,-4,6,-9,10,-2,-10,9,-6,-5],[2,7,6,-5,5,-3,-6,9,-6,-7,-4,7,9,-7],[-8,3,-10,5,-10,-5,10,-8,-6,8,-7,-10,-3,8],[2,9,8,2,-4,5,5,1,-9,-2,7,-9,-5,5],[6,2,-7,-10,4,-4,-8,4,-9,1,-3,-5,4,-5]],[[2,9,-3,10,5,-6,3,-9,9,4,-8,7,9,4],[-5,4,-8,7,-5,3,6,-9,1,10,1,7,-9,3],[-6,3,5,-1,2,6,7,-7,1,2,6,-2,-7,8],[-3,6,-9,1,8,-7,-1,8,-4,-1,-3,-7,-6,-9],[7,-9,-10,10,-5,3,4,-4,5,-1,8,-4,-4,1],[-7,2,-8,4,5,-7,-6,6,2,-5,3,-6,7,-2],[-8,-2,3,-10,-7,1,10,-4,10,-8,-9,1,-8,-3]],[[-4,9,-9,-10,-7,5,9,-7,8,7,1,-2,10,-4],[-8,-5,-3,-8,-3,7,1,3,-10,10,2,-5,5,-7],[9,-3,-10,1,1,6,-10,-6,-6,10,1,-3,-9,8],[-6,-9,8,-3,-10,-2,8,7,-2,8,3,-4,-9,-9],[-5,-2,-4,5,-5,-10,7,-8,-1,-2,5,3,-7,2],[3,-2,-10,7,-9,6,5,1,-8,-6,1,6,-7,5],[5,7,1,-4,6,-3,-6,-1,4,4,8,-5,-9,6]],[[-9,7,10,-1,3,-2,-9,-8,-3,-9,-8,1,2,-8],[4,-4,-4,-8,-4,5,-6,-10,1,3,4,3,2,1],[-9,-4,2,-7,-10,-3,3,4,7,4,10,4,-7,8],[-10,-5,8,1,1,8,-2,-8,9,4,-7,-5,-8,-3],[-5,-6,1,-3,5,9,-3,-9,-8,-10,10,4,-4,6],[-8,-9,-1,-8,-8,-3,9,9,9,-9,-5,-3,-4,-6],[-5,-2,-3,-6,6,9,6,-7,4,-7,3,9,6,5]],[[-10,-10,-3,-8,3,-1,7,-3,1,-8,-5,7,2,6],[-9,-5,1,-6,8,-1,7,10,-5,8,2,-1,4,4],[6,-1,-2,6,4,10,-5,2,6,-7,-4,6,-5,-2],[-9,-3,10,-1,-4,8,8,-1,2,4,-5,8,8,-5],[5,1,8,10,-2,10,10,4,-7,-1,-10,8,6,7],[4,-8,-1,-4,3,-7,-6,10,5,4,-1,-3,-7,-6],[-9,-8,5,1,-3,7,6,2,8,-8,8,-7,4,-9]],[[2,-8,10,-1,10,-3,4,2,1,-4,7,-4,-3,-5],[-4,1,-2,5,3,-9,10,7,-3,6,4,-4,1,6],[-2,2,-5,-10,-10,-1,4,7,3,8,4,9,-5,8],[3,-3,-5,1,-7,-7,7,-1,7,5,-3,-5,10,-6],[-6,-4,-8,-4,-1,3,5,7,9,4,-6,-7,5,-8],[3,-1,-8,-8,1,9,6,-10,-3,4,4,7,1,9],[-5,1,2,-5,-7,7,4,10,10,-10,6,7,5,10]],[[-10,-2,-7,-1,6,-9,10,3,-6,3,-2,10,-8,-7],[-3,-9,-7,5,3,-3,5,-4,-10,10,-7,-1,-7,-8],[-10,-10,-2,-5,9,3,8,-2,9,-10,10,-6,-5,9],[-10,9,-2,2,-7,2,-8,7,-2,1,-5,-2,-2,-4],[-7,-9,10,8,4,-5,-10,-6,-4,6,-1,9,9,1],[-2,-8,-9,-8,2,2,-10,8,6,8,-4,7,-1,-1],[10,2,6,2,5,-6,-8,5,-5,-9,5,-2,10,-6]],[[8,1,-9,9,-3,3,-3,-6,-5,-10,-4,-1,4,9],[3,-7,5,8,-3,1,7,3,-5,10,10,10,9,-4],[-7,1,8,-2,7,9,6,-3,6,-5,-7,-10,-7,2],[4,-2,-8,-2,10,1,5,-7,-10,7,8,-4,9,5],[-4,3,-4,-2,8,9,9,5,-8,6,3,-3,-5,10],[-10,-9,2,6,-7,-8,-2,2,7,-5,10,-4,-5,5],[-3,-4,-10,9,7,9,2,10,4,-7,-1,-7,-6,-3]]], dtype = "uint16")#candidate|2046|(14, 7, 14)|const|uint16
bop_2047 = relay.greater_equal(const_2045.astype('bool'), relay.reshape(const_2046.astype('bool'), relay.shape_of(const_2045))) # shape=(14, 7, 14)
bop_2050 = relay.equal(const_2046.astype('bool'), relay.reshape(const_2045.astype('bool'), relay.shape_of(const_2046))) # shape=(14, 7, 14)
output = relay.Tuple([bop_2047,bop_2050,])
output2 = relay.Tuple([bop_2047,bop_2050,])
func_2066 = relay.Function([], output)
mod['func_2066'] = func_2066
mod = relay.transform.InferType()(mod)
mutated_mod['func_2066'] = func_2066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2066_call = mutated_mod.get_global_var('func_2066')
call_2067 = func_2066_call()
output = call_2067
func_2068 = relay.Function([], output)
mutated_mod['func_2068'] = func_2068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2066_call = mod.get_global_var('func_2066')
func_2068_call = mutated_mod.get_global_var('func_2068')
call_2111 = relay.TupleGetItem(func_2066_call(), 0)
call_2112 = relay.TupleGetItem(func_2068_call(), 0)
output = relay.Tuple([call_2111,])
output2 = relay.Tuple([call_2112,])
func_2135 = relay.Function([], output)
mod['func_2135'] = func_2135
mod = relay.transform.InferType()(mod)
output = func_2135()
func_2136 = relay.Function([], output)
mutated_mod['func_2136'] = func_2136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_900_call = mod.get_global_var('func_900')
func_902_call = mutated_mod.get_global_var('func_902')
call_2154 = relay.TupleGetItem(func_900_call(), 0)
call_2155 = relay.TupleGetItem(func_902_call(), 0)
var_2156 = relay.var("var_2156", dtype = "float64", shape = (2, 6, 9))#candidate|2156|(2, 6, 9)|var|float64
bop_2157 = relay.bitwise_or(call_2154.astype('int16'), relay.reshape(var_2156.astype('int16'), relay.shape_of(call_2154))) # shape=(2, 6, 9)
bop_2160 = relay.bitwise_or(call_2155.astype('int16'), relay.reshape(var_2156.astype('int16'), relay.shape_of(call_2155))) # shape=(2, 6, 9)
output = relay.Tuple([bop_2157,])
output2 = relay.Tuple([bop_2160,])
func_2163 = relay.Function([var_2156,], output)
mod['func_2163'] = func_2163
mod = relay.transform.InferType()(mod)
mutated_mod['func_2163'] = func_2163
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2164 = relay.var("var_2164", dtype = "float64", shape = (2, 6, 9))#candidate|2164|(2, 6, 9)|var|float64
func_2163_call = mutated_mod.get_global_var('func_2163')
call_2165 = func_2163_call(var_2164)
output = call_2165
func_2166 = relay.Function([var_2164], output)
mutated_mod['func_2166'] = func_2166
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2066_call = mod.get_global_var('func_2066')
func_2068_call = mutated_mod.get_global_var('func_2068')
call_2210 = relay.TupleGetItem(func_2066_call(), 1)
call_2211 = relay.TupleGetItem(func_2068_call(), 1)
output = relay.Tuple([call_2210,])
output2 = relay.Tuple([call_2211,])
func_2212 = relay.Function([], output)
mod['func_2212'] = func_2212
mod = relay.transform.InferType()(mod)
output = func_2212()
func_2213 = relay.Function([], output)
mutated_mod['func_2213'] = func_2213
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2243 = relay.var("var_2243", dtype = "int64", shape = (13, 12, 4))#candidate|2243|(13, 12, 4)|var|int64
const_2244 = relay.const([[[-5,5,10,-4],[2,2,-8,-1],[-10,-8,-9,8],[10,3,1,3],[-10,3,10,4],[9,-3,-4,3],[5,-4,2,8],[-8,-9,-4,6],[-3,-5,-4,4],[4,2,4,-3],[9,-3,-1,-2],[-10,9,-5,10]],[[-2,8,-4,3],[2,8,-1,4],[10,2,6,10],[6,4,4,7],[8,6,-10,4],[4,-9,-4,-6],[8,-4,1,2],[5,9,9,9],[-3,-3,-4,6],[-8,-3,-8,5],[-5,10,-4,3],[10,1,8,-7]],[[5,-6,7,-6],[-9,-9,8,-10],[-4,-8,7,-8],[-3,-4,-8,-4],[3,1,3,6],[6,6,-9,6],[-1,2,6,-4],[-10,2,1,1],[5,3,1,10],[5,1,4,-7],[-10,2,-10,6],[5,10,-1,10]],[[-4,6,4,-3],[1,3,9,-10],[-1,-6,-1,5],[-8,3,-5,-9],[-6,4,-8,9],[1,5,-5,1],[-9,9,7,7],[-8,-9,3,-3],[1,-1,4,-10],[-5,7,2,-6],[-2,3,10,7],[2,10,-3,6]],[[-10,-7,-8,-1],[2,3,-3,6],[-5,-7,3,-2],[3,10,-2,-2],[-5,9,5,-10],[-8,-2,-3,8],[-1,2,2,-9],[-5,1,-7,-2],[-3,10,10,7],[-3,9,-1,-4],[4,6,-10,-1],[6,-2,4,-7]],[[-4,-4,-7,2],[-4,-3,-10,7],[3,-1,8,9],[3,-9,5,5],[5,6,2,9],[1,-1,1,6],[-1,8,-3,5],[8,5,10,-7],[-1,6,-10,-9],[6,-1,-8,-2],[8,-10,9,-6],[-1,-4,-3,7]],[[-1,7,-5,2],[8,2,-10,7],[-6,-8,-4,4],[7,6,9,6],[-4,1,1,5],[-7,-5,1,7],[-9,-2,1,-6],[-4,-10,6,2],[1,1,9,1],[-1,4,-8,-9],[6,-2,7,-5],[2,3,3,8]],[[-9,8,-3,5],[-5,5,-10,2],[8,-4,2,8],[-7,2,6,-6],[6,-6,-2,2],[10,3,-6,7],[-9,-10,10,-6],[9,-7,-7,4],[6,2,-9,-5],[6,8,-3,5],[-5,6,3,2],[-10,-10,3,-10]],[[-2,-9,1,-1],[-4,-8,-5,10],[7,3,7,-5],[4,6,7,-8],[-10,-9,1,-7],[-10,-1,-7,-3],[8,-6,3,6],[5,7,-9,3],[10,-2,4,7],[2,7,10,6],[7,-4,3,10],[-1,-2,-1,-2]],[[8,3,1,4],[-9,-5,-2,-6],[-2,1,-2,5],[-7,-4,1,9],[-9,-9,-4,6],[-5,-2,-1,-6],[-3,-8,8,-8],[10,1,-9,-3],[7,-9,-7,6],[-5,9,-1,8],[-9,-6,-10,2],[-6,3,7,4]],[[-8,-5,-7,6],[-1,5,-9,-3],[9,-7,-6,1],[2,-9,-10,3],[5,2,10,3],[5,5,-1,2],[10,3,6,7],[-9,-9,9,-6],[9,-6,8,-10],[7,6,-6,2],[-8,1,8,-4],[-4,6,2,-10]],[[2,9,7,-4],[7,-4,8,8],[-10,10,6,-7],[-6,4,6,8],[-9,-9,-8,-1],[-3,-7,-3,-5],[-3,3,10,8],[4,3,-7,10],[-9,4,-4,-4],[2,-7,6,9],[8,9,-5,-3],[10,-9,-8,4]],[[-9,-9,-3,-1],[-6,-1,-2,-2],[-4,10,9,-8],[-1,7,-7,-9],[9,-1,-10,-1],[-1,-9,-3,-7],[3,8,-1,2],[-3,-3,1,-9],[1,7,4,-8],[-10,-10,-1,2],[4,-7,-4,9],[9,10,-4,-2]]], dtype = "int64")#candidate|2244|(13, 12, 4)|const|int64
bop_2245 = relay.subtract(var_2243.astype('int64'), relay.reshape(const_2244.astype('int64'), relay.shape_of(var_2243))) # shape=(13, 12, 4)
output = relay.Tuple([bop_2245,])
output2 = relay.Tuple([bop_2245,])
func_2250 = relay.Function([var_2243,], output)
mod['func_2250'] = func_2250
mod = relay.transform.InferType()(mod)
var_2251 = relay.var("var_2251", dtype = "int64", shape = (13, 12, 4))#candidate|2251|(13, 12, 4)|var|int64
output = func_2250(var_2251)
func_2252 = relay.Function([var_2251], output)
mutated_mod['func_2252'] = func_2252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_900_call = mod.get_global_var('func_900')
func_902_call = mutated_mod.get_global_var('func_902')
call_2268 = relay.TupleGetItem(func_900_call(), 0)
call_2269 = relay.TupleGetItem(func_902_call(), 0)
func_1564_call = mod.get_global_var('func_1564')
func_1566_call = mutated_mod.get_global_var('func_1566')
const_2271 = relay.const([-8.455651,1.064263,1.940728,-3.043585,-3.143334,-5.746632,3.286312,-2.484962,7.145685,1.223566,2.982207,-9.575623,2.778469,7.784791,1.512230,8.752806,8.443143,-3.346386,-8.703367,-9.284113,5.786521,-0.376852,9.172327,-0.210503,-7.804492,2.650352,4.414870,-0.957375,-6.112603,4.769487,3.601720,4.644862,9.551123,7.397890,-1.148928,-6.874393,-1.286229,6.087643,-4.304227,-3.188252,3.086716,-7.099447,-9.742815,-6.323177,9.732477,-9.580700,-1.720283,0.243762,2.744669,-4.327327,-9.124728,-7.921185,2.952059,-3.299488,6.229635,-9.893272,-9.980397,1.853139,-0.556857,6.919695,-0.688571,-2.949482,-9.223169,-9.558388,-2.975650,5.023865,-8.252744,4.768872,7.964703,7.455334,-9.864520,-0.891849,-6.240921,5.246952,5.195710,-5.121107,-7.715826,-3.034116,-9.003817,6.199828,2.975282,4.122679,-9.880124,0.012101,-1.758946,-4.450416,6.094571,7.625879,9.341265,-7.018370,-0.832969,-8.708969,5.832353,4.507509,3.590848,-5.420411,4.941001,-1.810337,-3.163719,-4.508048,-4.128181,2.742270,1.054204,-5.861222,-0.513278,9.494377,8.170415,4.973346,-5.702500,5.253800,2.990897,5.401400,8.273158,-2.846194,7.345961,4.177287,-3.543300,4.745312,4.821445,-1.817138,-8.611819,-2.339336,6.849470,-2.080093,-2.354836,9.913016,2.862941,5.313979,1.396662,-6.423481,-5.375256,-0.477941,7.298199,-9.746449,4.374083,-9.763139,-6.389821,-8.837996,-5.577573,0.474164,-2.588849,1.645133,9.443968,-7.239453,-8.004987,-1.504116,-8.748614,1.599242,-7.490862,8.206460,-5.447785,-8.144505,-3.456279,-5.235061,7.341680,-3.230012,6.895313,-0.831335,-0.992103,5.124361,5.786187,0.955103,-7.887737,6.738940,-8.537647,2.710295,-5.053928,3.157714,-6.752420,-3.869494,7.843012,7.037205,-5.293383,-3.554481,-2.849994,5.431493,2.894551,-1.134597,-0.833380,-4.208527,-1.068571,2.563583,7.945175,7.414975,6.173566,-0.286559,-8.432995,3.788316,8.930992,7.246197,5.537896,7.752288,5.891273,-8.282538,-8.193474,-1.083989,-5.637313,5.701412,-1.055488,6.581685,-9.697018,4.731891,2.266179,8.831506,-2.539525,0.616437,-0.324179,-0.640113,-5.579455,1.598974,0.446143,3.570476,1.516316,-4.460281,4.068161,2.933767,7.752467,2.888907,8.566238,6.025557,9.128798,3.092871,2.038291,-6.064507,4.164584,-1.710648,9.534524,-6.882497,1.699539,6.154554,0.350621,-5.612124,8.149479,6.663722,1.625922,-8.843471,1.106142,-8.876923,5.702941,-7.522605,-8.769607,1.410015,-0.958456,-4.039648,-9.233007,7.061287,7.778312,-3.840338,5.997606,5.511341,-1.323156,9.155242,-5.147921,5.104106,-6.166028,-6.354232,-8.649050,9.307584,9.312104,-9.668210,3.147347,5.557294,-9.477955,0.043776,-6.787831,-8.078472,-2.115985,-7.386512,6.248106,-1.181852,-6.436771,-6.460725,-8.913589,0.194499,3.212147,-4.358855,0.607288,1.934912,5.448946,3.670089,-0.446588,9.459663,-4.898226,8.353232,0.832754,3.940495,-1.438470,-7.336911,0.022722,-9.256008,-4.559316,9.592480,0.537303,9.068358,7.122093,-5.328581,-6.417435,-5.042916,0.016722,-4.313457,6.670200,-7.934673,8.783033,8.972952,4.367701,4.295316,-7.176897,2.085847,-2.114603,-7.077101,-6.218999,7.651700,-4.109774,3.901175,3.997383,-1.073928,3.679708,-6.614400,-4.609590,-6.739625,4.925107,5.124736,-6.415388,0.744424,4.714254,0.374257,-7.305137,-3.218848,-4.343007,2.917145,4.073097,2.574573,-3.494867,2.030373,4.420281,-9.192210,6.295411,-0.688184,6.700525,-3.015047,7.163781,-7.928570,-0.327292,8.684526,-9.529764,-9.465020,-1.420918,-4.989382,8.483078,9.070383,3.439290,-2.485059,6.513880,4.763643,-6.422686,7.584645,0.524586,-7.669537,-5.726925,-2.486759,-0.441703,-5.578280,-4.141872,1.047708,-0.439034,-5.371210,5.727290,7.269572,6.252625,9.663154,-1.725326,-1.027612,-2.108635,-7.901348,-4.590906,7.369518,7.111928,2.005675,-3.920251,-3.469829,-8.362006,1.673610,5.984772,-2.316888,8.222563,-4.102678,2.460695,8.304552,5.954882,-0.155993,-8.990030,-7.331801,-7.590454,-5.636457,5.404954,0.472419,3.452167,6.467981,8.896257,-3.094304,2.229668,1.112488,0.695020,-1.595437,-1.916958,-3.785110,-9.084814,-1.838700,-3.871087,1.549705,4.542042,8.166062,8.563392,3.303101,3.250767,0.817916,7.542668,1.719387,3.131732,6.997807,-9.444890,8.900931,5.754533,3.725658,-5.806337,9.803395,-1.757577,-2.428383,4.475432,-0.436032,8.785129,0.877266,-8.137684,1.987183,-6.470201,0.377720,-4.699181,1.956515,2.326612,-0.416087,5.681139,5.353442,-7.951949,-0.944516,-9.130099,-3.793614,-6.121665,-6.885206,-5.280137,8.741971,-9.490866,-1.369709,4.103357,-2.297056,-1.164376,-9.630253,-2.340425,1.084703,2.685780,-3.460028,3.932290,-0.768480,-2.133609,-6.737396,-4.894103,0.665740,2.519572,-5.014510,6.606631,1.812918,4.437030,-6.767974,2.937730,-7.872007,1.652708,-2.848651,-5.083103,-9.978876,9.490024,1.443521,-7.998595,0.515770,-4.970306,-0.702387,-1.280970,-4.030958,1.600679,-0.323811,-3.966382,-7.637296,9.972964,-0.328161,9.329555,3.020489,-9.589108,-2.865919,7.496507,-5.388276,0.949211,-5.188482,-2.459623,7.710375,8.212406,-4.128718,8.502646,5.785992,-7.088897,-4.870454,-0.012142,-6.481820,-8.976831,-7.546438,-9.980386,-4.464217,0.783118,-4.029973,1.566522,-0.155858,7.407801,-7.133728,9.095249,2.958791,-6.390596,4.607468,2.544644,9.054745,-8.392880,-3.861357,-9.129113,4.946625,2.817992,2.792164,1.249048,7.838134,-1.843234,8.287331,1.001184,0.123144,-8.660698,-1.169969,6.077849,-7.054808,0.984827,-7.961140,7.880543,-6.304542,5.371958,0.349284,6.320748,8.478695,-8.669056,3.986541,-5.026444,3.657548,2.395007,-4.626185,6.639092,-6.810223,8.012122,-7.084573,-5.630381,2.128199,-5.058537,9.879669,4.455226,-5.325703,6.333858,6.358008,-1.361347,0.452683,1.717224,-8.625446,-9.064740,9.557635,-5.516622,-8.234377,-9.946314,-3.224669,-7.350792,-4.456930,6.559499,3.029038,-0.501459,-7.040004,-1.818309,-6.626535,8.002972,-4.405490,-7.609564,-1.141878,-2.948127,4.641543,-6.460601,9.458341,1.241668,6.260564,-6.346161,-3.115967,9.305447,-9.100498,-3.725680,8.504692,3.242412,7.743095,-6.032444,-2.657584,-1.155048,5.872326,-3.702337,0.311589,2.527452,-5.571738,3.580740,-9.834334,7.761779,-4.415463,-5.827671,5.609068,-7.919224,3.451746,-9.590015,1.730700,2.495454,-1.301455,5.215749,-7.909480,-0.406178,9.495306,6.885467,-0.319264,-5.433203,-4.918026,2.704702,-4.425173,-3.713700,-7.538641,-1.533063,4.487799,-9.708921,1.227793,6.554843,-9.786497,-9.461025,5.359600,-7.001391,-9.874619,4.834478,4.821258,-1.426872,-5.536666,7.397065,-5.584584,-5.954933,2.460164,4.424315,-7.452890,-9.974966,-3.468291,-0.198795,-4.763395,5.417312,6.708273,3.040980,2.494032,5.176582,-7.666407,-7.481739,-1.116432,-1.811369,-5.239959,-9.948816,-5.300951,7.430316,2.365041,8.020012,-1.210174,-3.165240,5.705234,-4.826472,8.827349,-1.807554,-9.413211,-0.680202,8.295428,0.868251,-4.610249,-6.910491,-6.031538,1.342828,-9.963752,-9.266405,-9.705299,-3.817492], dtype = "float32")#candidate|2271|(693,)|const|float32
call_2270 = func_1564_call(relay.reshape(const_2271.astype('float32'), [7, 11, 9]))
call_2272 = func_1564_call(relay.reshape(const_2271.astype('float32'), [7, 11, 9]))
func_1062_call = mod.get_global_var('func_1062')
func_1064_call = mutated_mod.get_global_var('func_1064')
var_2274 = relay.var("var_2274", dtype = "uint8", shape = (1120,))#candidate|2274|(1120,)|var|uint8
call_2273 = relay.TupleGetItem(func_1062_call(relay.reshape(var_2274.astype('uint8'), [1120,])), 3)
call_2275 = relay.TupleGetItem(func_1064_call(relay.reshape(var_2274.astype('uint8'), [1120,])), 3)
func_213_call = mod.get_global_var('func_213')
func_216_call = mutated_mod.get_global_var('func_216')
call_2281 = relay.TupleGetItem(func_213_call(relay.reshape(call_2268.astype('bool'), [6, 3, 6])), 0)
call_2282 = relay.TupleGetItem(func_216_call(relay.reshape(call_2268.astype('bool'), [6, 3, 6])), 0)
output = relay.Tuple([call_2268,call_2270,const_2271,call_2273,var_2274,call_2281,])
output2 = relay.Tuple([call_2269,call_2272,const_2271,call_2275,var_2274,call_2282,])
func_2293 = relay.Function([var_2274,], output)
mod['func_2293'] = func_2293
mod = relay.transform.InferType()(mod)
var_2294 = relay.var("var_2294", dtype = "uint8", shape = (1120,))#candidate|2294|(1120,)|var|uint8
output = func_2293(var_2294)
func_2295 = relay.Function([var_2294], output)
mutated_mod['func_2295'] = func_2295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1258_call = mod.get_global_var('func_1258')
func_1259_call = mutated_mod.get_global_var('func_1259')
call_2303 = relay.TupleGetItem(func_1258_call(), 1)
call_2304 = relay.TupleGetItem(func_1259_call(), 1)
output = relay.Tuple([call_2303,])
output2 = relay.Tuple([call_2304,])
func_2311 = relay.Function([], output)
mod['func_2311'] = func_2311
mod = relay.transform.InferType()(mod)
output = func_2311()
func_2312 = relay.Function([], output)
mutated_mod['func_2312'] = func_2312
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2335 = relay.var("var_2335", dtype = "float64", shape = (15, 16, 4))#candidate|2335|(15, 16, 4)|var|float64
uop_2336 = relay.tan(var_2335.astype('float64')) # shape=(15, 16, 4)
output = uop_2336
output2 = uop_2336
func_2340 = relay.Function([var_2335,], output)
mod['func_2340'] = func_2340
mod = relay.transform.InferType()(mod)
mutated_mod['func_2340'] = func_2340
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2341 = relay.var("var_2341", dtype = "float64", shape = (15, 16, 4))#candidate|2341|(15, 16, 4)|var|float64
func_2340_call = mutated_mod.get_global_var('func_2340')
call_2342 = func_2340_call(var_2341)
output = call_2342
func_2343 = relay.Function([var_2341], output)
mutated_mod['func_2343'] = func_2343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1258_call = mod.get_global_var('func_1258')
func_1259_call = mutated_mod.get_global_var('func_1259')
call_2349 = relay.TupleGetItem(func_1258_call(), 1)
call_2350 = relay.TupleGetItem(func_1259_call(), 1)
var_2363 = relay.var("var_2363", dtype = "int64", shape = (700,))#candidate|2363|(700,)|var|int64
bop_2364 = relay.bitwise_or(call_2349.astype('uint8'), relay.reshape(var_2363.astype('uint8'), relay.shape_of(call_2349))) # shape=(700,)
bop_2367 = relay.bitwise_or(call_2350.astype('uint8'), relay.reshape(var_2363.astype('uint8'), relay.shape_of(call_2350))) # shape=(700,)
func_1062_call = mod.get_global_var('func_1062')
func_1064_call = mutated_mod.get_global_var('func_1064')
const_2369 = relay.const([[-4,8,-7,-6,-7,-9,-7,-8,8,3,-7,9,9,-2,1,-5,-2,5,-10,-6,1,-5,4,5,1,-3,-9,10,6,-8,-10,4,-5,-1,9,-2,-7,-9,2,3,4,-6,6,4,5,-3,-4,-9,5,6,9,6,-6,-9,1,-6,5,9,-5,5,4,9,4,-8,7,-5,-3,4,-6,-10,2,1,5,1,10,3,2,1,-7,-7,3,1,-2,5,-10,4,-10,-1,4,6,8,7,1,-5,7,3,5,5,-10,5,5,4,-6,-10,-7,-6,6,-4,-3,5,3,1,-1,5,-9,5,-2,9,4,-10,-6,7,-10,-10,1,3,3,-2,-10,-8,-9,-3,2,9,-1,-8,-5,-10,-7,8,-6,-4,6,-3,-4,7,6,4,-4,-5,-2,-4,9,4,6,5,-6,3,6,-10,9,-4,9,-2,-1,-10,9,1,-9,5,10,9,1,-8,8,-9,-5,-1,-9,7,-9,2,-10,9,10,7,5,6,8,7,1,-2,-7,1,7,7,-5,-5,5,-6,-7,7,-9,-10,-6,-2,10,-3,10,-6,-6,-2,-3,-7,8,-5,4,-6,2,1,-2,-5,8,1,6,4,10,2,-2,4,-2,-4,-9,-1,-6,-9,5,1,5,-3,1,10,5,7,-3,-7,9,1,-2,1,5,6,-5,7,-3,1,-10,-5,5,2,4,2,1,-1,8,-2,-3,4,7,8,-2,4,-1,8,-3,-5,2,-10,9,-7,-7,-1,-7,-8,8,6,6,3,1,5,-4,2,-8,-8,-8,-5,3,-3,2,-5,-7,10,1,3,7,-7,-10,8,1,-4,-10,-2,-4,-3,6,7,-9,9,2,-1,1,1,-6,7,4,6,2,-9,3,-3,8,-2,-6,-6,-2,9,-6,5,9,9,5,1,3,4,-2,7,-6,8,2,2,2,9,10,-9,-6,-6,4,-10,7,-5,2,8,2,2,9,-10,-3,-8,3,-6,4,1,9,-4,-7,5,10,-9,-9,-6,7,1,5,5,-5,-8,-4,8,10,10,-3,-1,8,5,3,6,-1,1,6,-5,-8,-3,-10,6,5,1,10,-10,2,-6,9,6,-8,-6,-3,-7,-2,3,-1,3,-4,-1,6,3,-7,4,2,5,-7,6,2,10,2,-7,2,-9,6,-1,1,4,-4,3,-10,-5,1,-6,-5,-8,-10,1,9,-8,-8,-1,2,9,4,3,-2,1,-2,-8,-5,-3,5,7,-4,1,4,2,-5,-4,-5,-3,5,-2,-10,3,1,8,-2,10,-2,9,-10,3,-4,-4,-6,-7,8,-10,-4,-4,1,-10,9,-10,-2,-8,-1,-10,10,5,-1,-8,4,9,-3,2,7,6,4,8,6,-8,6,4,-2,-1,3,-3,-9,4,7,5,-8,9,-8,5,2,-3,-3,-6,7,-1,-9,9,9,10,-7,-10,-8,6,8,2,-9,10,-5,9,6,-4,6,-2,7,1,-9,-1,-1,-4],[10,-1,-4,-1,9,-3,-9,9,10,-10,-7,3,3,-4,-2,-3,8,-1,7,3,1,-3,1,-8,5,-10,-9,8,-8,6,5,-2,3,5,-5,-10,-4,-7,-4,8,2,-2,2,3,-6,-9,8,4,-7,3,-9,8,-5,8,9,1,-3,-4,-4,-4,8,1,-9,7,-6,-7,5,-8,-10,2,-10,3,-5,-8,-6,3,-8,-9,-1,-2,-9,4,6,-6,6,-8,-10,-2,9,-8,-2,10,5,-8,6,-5,-3,-10,-1,-5,-6,-3,-3,-3,-5,-1,2,-1,-1,-5,-3,3,-9,2,1,7,8,4,-7,6,-8,10,-8,-6,2,-5,10,-8,3,9,7,3,-5,9,-4,5,1,1,-6,8,8,2,3,9,10,-4,-3,2,-4,2,-5,-1,2,-10,8,-8,-3,-4,-10,6,10,-9,-7,-3,-2,-10,-1,7,-2,4,7,6,-2,-8,-3,6,-6,-6,-6,3,-3,-8,3,-10,4,-7,-7,1,-5,-4,5,2,5,-4,9,10,2,8,3,2,-3,-8,-2,-10,10,-5,-5,6,-7,10,10,9,8,-7,7,-10,-10,3,-7,-9,8,-2,3,1,-8,7,1,-8,-3,-1,8,-3,8,-10,-8,2,5,8,-1,1,2,-5,-3,-3,2,9,5,-6,-7,-10,7,2,7,3,3,-7,-1,-9,7,-3,5,-9,-5,5,-5,-10,6,-6,3,1,3,-10,-10,3,2,8,-9,10,-6,-7,-10,3,8,-1,1,9,-9,10,-8,9,-10,-9,-8,4,-4,4,7,-1,9,8,-3,-3,5,-2,-8,-5,9,-9,3,-10,-4,10,-4,-8,3,2,-4,10,10,-4,-4,9,3,2,-9,4,7,-7,-6,-1,-5,-9,-7,10,-1,-8,-5,10,-2,5,-5,7,2,-2,-2,-1,5,8,7,1,-2,4,-3,5,-9,9,9,5,-3,-4,-9,2,3,9,-7,9,-9,-9,9,10,-4,3,6,-7,-4,-3,-3,10,4,7,10,-3,1,3,-7,2,-1,-7,3,-5,-4,-2,3,5,1,-1,10,-2,-7,4,8,-5,9,6,-5,-8,9,-6,-4,-10,-4,8,4,-8,-4,4,8,-1,-1,-10,-1,-5,-10,3,-3,9,-5,-5,6,1,-6,4,-6,5,-5,6,-5,6,-4,-1,5,6,8,8,-5,-6,4,6,-6,-9,-8,-6,-6,10,3,-6,-1,8,-4,-3,-5,-9,-10,1,6,8,-5,-8,-9,10,10,-2,-10,10,7,2,-6,-3,6,2,-5,7,-5,10,3,-5,8,6,6,-4,1,6,-7,-4,4,6,-6,-1,9,-4,3,-5,-7,-3,-7,7,-10,-7,-2,9,-7,-7,-7,-4,2,-9,7,10,-7,6,-7,-5,-6,4,-3,5,-8,-3,-1,-1,4,9,-6,-3,1,8,-2,5,-5,-5,-3,-8,-3,8,-7,6,-3,-3,4,-3,-5,3,5,-5,-10,-9,-1,6,8,-5]], dtype = "uint8")#candidate|2369|(2, 560)|const|uint8
call_2368 = relay.TupleGetItem(func_1062_call(relay.reshape(const_2369.astype('uint8'), [1120,])), 1)
call_2370 = relay.TupleGetItem(func_1064_call(relay.reshape(const_2369.astype('uint8'), [1120,])), 1)
func_912_call = mod.get_global_var('func_912')
func_914_call = mutated_mod.get_global_var('func_914')
const_2380 = relay.const([True,False,False,True,False,False,False,False,False,True,True,False,False,False,True,False,False,False,True,False,False,False,False,False,False,False,True,False,True,True,False,False,True,False,True,True,False,True,False,False,False,True,False,False,True,True,False,True,True,False,True,False,False,True,False,False,True,True,True,False,False,True,False,False,True,False,True,True,True,True,False,False,False,False,False,True,False,True,False,True,True,True,True,True,False,True,True,True,False,False,True,True,True,False,True,False,False,False,False,True,False,False,True,False,False,False,False,False,True,False,False,False,False,True,True,False,True,False,False,True,True,True,False,False,True,True,True,True,False,True,True,False,True,False,False,True,False,False,False,True,True,False,True,True,True,False,True,False,True,True,False,False,True,False,False,False,False,True,False,False,False,True,False,True,True,False,True,False,True,True,True,False,True,True,True,False,True,False,True,False,False,True,False,True,True,True,True,True,False,True,True,True,False,True,False,False,False,True,False,True,False,True,True,True,False,False,False,False,False,True,False,False,False,True,True,True,False,True,True,False,False,False,True,True,False,False,True,False,True,True,True,False,False,False,True,True,False,True,True,False,False,True,True,False,False,False,False,False,True,True,True,False,True,False,True,True,False,False,True,False,True,False,False,True,False,True,False,False,True,True,True,True,True,False,False,True,False,False,False,False,True,True,False,False,True,True,False,False,True,True,False,False,False,False,True,False,True,False,True,False,True,False,False,False,False,False,False,False,False,False,False,True,True,False,True,False,True,True,False,False,True,False,False,True,False,False,True,False,False,False,False,True,False,False,False,False,False,False,True,False,False,True,True,True,False,True,True,True,False,False,False,True,False,False,False,True,False,False,True,False,False,True,False,True,False,False,True,False,False,False,True,False,False,False,True,False,True,False,True,False,False,True,True,True,False,False,False,False,False,True,True,False,False,True,True,False,True,True,True,True,True,False,True,True,False,False,True,False,False,True,False,True,False,True,False,False,True,False,True,True,True,False,False,True,True,True,False,False,False,True,True,False,True,False,True,True,False,True,True,False,False,True,True,False,True,True,True,False,True,False,False,False,False,False,False,True,True,False,True,False,True,False,False,False,False,True,True,False,False,True,False,False,False,False,True,True,True,False,False,True,False,False,True,False,False,True,True,True,True,False,True,False,False,True,False,False,True,False,False,True,True,False,False,True,False,True,True,False,True,True,True,True,True,False,True,True,False,False,False,True,False,False,False,False,True,False,False,False,False,False,False,True,False,False,True,True,True,False,True,False,True,False,True,False,False,False,True,False,False,True,False,False,True,False,False,True,False,False,True,True,False,True,False,False,True,True,True,False,True,False,False,False,False,True,False,True,True,True,True,True,True,True,True,False,True,True,True,False,True,True,True,True,False,True,False,False,True,True,False,False,False,True,True,False,False,True,True,False,True,True,True,False,False,True,False,False,False,False,False,False,True,True,True,True,False,True,True,True,True,False,False,True,True,True,True,True,False,True,True,True,False,True,True,False,False,False,False,False,False,False,False,True,True,False,False,False,True,False,True,False,False,True,True,True,False,True,False,True,False,False,False,False,True,False,False,True,False,True,True,False,True,False,True,True,False,True,True,True,True,False,False,True,False,True,False,False,False,True,True,False,True,False,False,False,False,True,True,False,False,False,False,True,False,True,False,False,False,True,False,False,False,False,True,False,True,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,True,False,True,False,True,False,False,True,True,False,True,True,False,True,True,False,True,False,False,False,False,False,False,False,True,False,False,True,True,False,True,False,False,True,False,True,True,True,False,False,True,False,False,False,True,True,False,False,True,False,False,True,False,False,True,False,False,True,True,True,True,True,True,True,False,False,False,True,True,True,True,False,True,True,False,False,True,False,False,False,False,False,False,True,False,True,True,False,True,False,True,False,True,False,False,True,False,False,False,True,True,False,False,False,True,False,False,False,True,False,True,True,False,True,False,False,False,True,False,True,False,True,False,True,False,False,True,False,False,True,False,False,True,False,False,True,False,True,True,True,True,False,True,False,True,True,False,False,True,True,True,True,False,True,False,False,True,True,True,False,True,True,False,False,True,False,True,True,True,True,True,True,True,False,True,True,True,True,True,False,False,False,True,True,False,False,True,True,True,False,True,False,True,True,True,False,False,False,False,True,True,True,False,True,True,True,False,False,True,True,True,True,True,False,False,True,False,False,True,False,False,False,False,False,False,True,False,False,False,False,True,True,True,False,False,False,True,False,True,False,True,False,False,True,False,False,False,True,False,True,True,True,False,True,True,False,True,True,False,True,False,True,False,True,True,True,False,True,True,True,True,True,True,True,False,True,False,False,False,False,False,True,True,False,True,False,False,False,False,False,True,False,True,True,True,True,False,True,False,False,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,False,True,True,False,True,True,True,True,True,False,True,False,True,False,False,True,True,True,False,False,False,True,True,True,False,True,True,False,False,False,True,False,True,True,False,True,False], dtype = "bool")#candidate|2380|(1092,)|const|bool
call_2379 = relay.TupleGetItem(func_912_call(relay.reshape(const_2380.astype('bool'), [13, 14, 6])), 0)
call_2381 = relay.TupleGetItem(func_914_call(relay.reshape(const_2380.astype('bool'), [13, 14, 6])), 0)
uop_2383 = relay.atan(call_2379.astype('float32')) # shape=(13, 14, 6)
uop_2385 = relay.atan(call_2381.astype('float32')) # shape=(13, 14, 6)
output = relay.Tuple([bop_2364,call_2368,const_2369,const_2380,uop_2383,])
output2 = relay.Tuple([bop_2367,call_2370,const_2369,const_2380,uop_2385,])
func_2386 = relay.Function([var_2363,], output)
mod['func_2386'] = func_2386
mod = relay.transform.InferType()(mod)
var_2387 = relay.var("var_2387", dtype = "int64", shape = (700,))#candidate|2387|(700,)|var|int64
output = func_2386(var_2387)
func_2388 = relay.Function([var_2387], output)
mutated_mod['func_2388'] = func_2388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1963_call = mod.get_global_var('func_1963')
func_1965_call = mutated_mod.get_global_var('func_1965')
call_2409 = func_1963_call()
call_2410 = func_1963_call()
uop_2426 = relay.erf(call_2409.astype('float32')) # shape=(2, 6, 9)
uop_2428 = relay.erf(call_2410.astype('float32')) # shape=(2, 6, 9)
output = relay.Tuple([uop_2426,])
output2 = relay.Tuple([uop_2428,])
func_2435 = relay.Function([], output)
mod['func_2435'] = func_2435
mod = relay.transform.InferType()(mod)
mutated_mod['func_2435'] = func_2435
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2435_call = mutated_mod.get_global_var('func_2435')
call_2436 = func_2435_call()
output = call_2436
func_2437 = relay.Function([], output)
mutated_mod['func_2437'] = func_2437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1690_call = mod.get_global_var('func_1690')
func_1692_call = mutated_mod.get_global_var('func_1692')
call_2536 = relay.TupleGetItem(func_1690_call(), 0)
call_2537 = relay.TupleGetItem(func_1692_call(), 0)
output = call_2536
output2 = call_2537
func_2545 = relay.Function([], output)
mod['func_2545'] = func_2545
mod = relay.transform.InferType()(mod)
output = func_2545()
func_2546 = relay.Function([], output)
mutated_mod['func_2546'] = func_2546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1963_call = mod.get_global_var('func_1963')
func_1965_call = mutated_mod.get_global_var('func_1965')
call_2582 = func_1963_call()
call_2583 = func_1963_call()
func_2545_call = mod.get_global_var('func_2545')
func_2546_call = mutated_mod.get_global_var('func_2546')
call_2599 = func_2545_call()
call_2600 = func_2545_call()
output = relay.Tuple([call_2582,call_2599,])
output2 = relay.Tuple([call_2583,call_2600,])
func_2607 = relay.Function([], output)
mod['func_2607'] = func_2607
mod = relay.transform.InferType()(mod)
mutated_mod['func_2607'] = func_2607
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2607_call = mutated_mod.get_global_var('func_2607')
call_2608 = func_2607_call()
output = call_2608
func_2609 = relay.Function([], output)
mutated_mod['func_2609'] = func_2609
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2610 = relay.const([[[-2,5,3,-6,8,-8,1,-1],[-7,2,-8,-9,6,-7,-2,8],[7,-3,1,-3,-5,1,-9,9],[-7,-3,-3,2,-6,8,-2,-1]],[[-2,-1,-4,-1,-5,6,-7,2],[-8,-9,-9,-10,-9,-2,7,-2],[-8,5,7,-4,10,-8,5,-3],[7,3,10,-9,-6,-4,4,3]],[[10,5,-5,10,9,4,-10,-8],[-6,2,-8,9,-2,6,-10,8],[-8,9,-4,-9,-9,-8,10,7],[-8,-4,-10,10,-9,-7,-7,10]],[[10,9,8,-8,2,9,3,-8],[5,-7,8,-8,-4,-5,-10,6],[-4,-7,-6,-1,-10,-10,8,-3],[-3,-9,-6,7,2,10,-7,-5]],[[5,5,-4,8,9,-6,-8,-2],[-9,-10,-10,4,-9,5,3,8],[1,-7,-4,-8,5,-1,-4,3],[-6,6,-2,-9,7,8,3,7]]], dtype = "uint64")#candidate|2610|(5, 4, 8)|const|uint64
const_2611 = relay.const([[[-6,4,7,9,-8,6,-7,-8],[-6,1,-2,-5,9,-10,-5,-6],[-3,5,6,1,7,8,4,4],[1,-9,8,10,1,-4,5,7]],[[10,-8,-6,-4,6,-8,8,-10],[7,1,-3,-3,-3,1,8,-5],[-10,9,-4,2,5,-8,-9,-1],[2,-2,-3,1,1,-3,10,9]],[[5,-7,-9,6,-6,-8,-7,-3],[-10,-3,-9,8,-4,1,3,3],[8,-4,6,2,4,-1,8,9],[-1,1,-5,-4,-4,-3,4,2]],[[6,10,5,8,-1,-2,4,-7],[4,-7,-10,1,5,-8,2,3],[-5,-1,-5,4,7,5,9,-6],[-3,-3,-1,5,-8,5,5,7]],[[-10,-2,7,-1,2,-6,1,6],[-5,6,-5,4,-6,-3,-6,10],[-9,3,10,10,3,5,-8,-7],[-1,-10,4,8,-2,2,3,6]]], dtype = "uint64")#candidate|2611|(5, 4, 8)|const|uint64
bop_2612 = relay.not_equal(const_2610.astype('bool'), relay.reshape(const_2611.astype('bool'), relay.shape_of(const_2610))) # shape=(5, 4, 8)
uop_2624 = relay.rsqrt(bop_2612.astype('float64')) # shape=(5, 4, 8)
func_2066_call = mod.get_global_var('func_2066')
func_2068_call = mutated_mod.get_global_var('func_2068')
call_2636 = relay.TupleGetItem(func_2066_call(), 1)
call_2637 = relay.TupleGetItem(func_2068_call(), 1)
func_644_call = mod.get_global_var('func_644')
func_646_call = mutated_mod.get_global_var('func_646')
var_2650 = relay.var("var_2650", dtype = "uint8", shape = (1120,))#candidate|2650|(1120,)|var|uint8
call_2649 = relay.TupleGetItem(func_644_call(relay.reshape(var_2650.astype('uint8'), [1120,])), 0)
call_2651 = relay.TupleGetItem(func_646_call(relay.reshape(var_2650.astype('uint8'), [1120,])), 0)
uop_2655 = relay.log10(const_2611.astype('float64')) # shape=(5, 4, 8)
func_2435_call = mod.get_global_var('func_2435')
func_2437_call = mutated_mod.get_global_var('func_2437')
call_2660 = relay.TupleGetItem(func_2435_call(), 0)
call_2661 = relay.TupleGetItem(func_2437_call(), 0)
bop_2664 = relay.multiply(uop_2655.astype('uint16'), relay.reshape(const_2611.astype('uint16'), relay.shape_of(uop_2655))) # shape=(5, 4, 8)
func_571_call = mod.get_global_var('func_571')
func_576_call = mutated_mod.get_global_var('func_576')
call_2669 = relay.TupleGetItem(func_571_call(relay.reshape(call_2660.astype('float64'), [2, 6, 9]), relay.reshape(call_2660.astype('float64'), [2, 6, 9]), relay.reshape(var_2650.astype('uint8'), [4, 280]), ), 4)
call_2670 = relay.TupleGetItem(func_576_call(relay.reshape(call_2660.astype('float64'), [2, 6, 9]), relay.reshape(call_2660.astype('float64'), [2, 6, 9]), relay.reshape(var_2650.astype('uint8'), [4, 280]), ), 4)
func_1672_call = mod.get_global_var('func_1672')
func_1674_call = mutated_mod.get_global_var('func_1674')
call_2671 = relay.TupleGetItem(func_1672_call(relay.reshape(var_2650.astype('uint8'), [1120,])), 3)
call_2672 = relay.TupleGetItem(func_1674_call(relay.reshape(var_2650.astype('uint8'), [1120,])), 3)
uop_2682 = relay.acos(uop_2655.astype('float32')) # shape=(5, 4, 8)
uop_2685 = relay.asinh(const_2611.astype('float64')) # shape=(5, 4, 8)
func_2386_call = mod.get_global_var('func_2386')
func_2388_call = mutated_mod.get_global_var('func_2388')
var_2690 = relay.var("var_2690", dtype = "int64", shape = (700,))#candidate|2690|(700,)|var|int64
call_2689 = relay.TupleGetItem(func_2386_call(relay.reshape(var_2690.astype('int64'), [700,])), 1)
call_2691 = relay.TupleGetItem(func_2388_call(relay.reshape(var_2690.astype('int64'), [700,])), 1)
uop_2693 = relay.exp(uop_2682.astype('float64')) # shape=(5, 4, 8)
func_1963_call = mod.get_global_var('func_1963')
func_1965_call = mutated_mod.get_global_var('func_1965')
call_2704 = func_1963_call()
call_2705 = func_1963_call()
func_2250_call = mod.get_global_var('func_2250')
func_2252_call = mutated_mod.get_global_var('func_2252')
var_2716 = relay.var("var_2716", dtype = "int64", shape = (624, 1))#candidate|2716|(624, 1)|var|int64
call_2715 = relay.TupleGetItem(func_2250_call(relay.reshape(var_2716.astype('int64'), [13, 12, 4])), 0)
call_2717 = relay.TupleGetItem(func_2252_call(relay.reshape(var_2716.astype('int64'), [13, 12, 4])), 0)
bop_2724 = relay.equal(uop_2693.astype('bool'), relay.reshape(uop_2685.astype('bool'), relay.shape_of(uop_2693))) # shape=(5, 4, 8)
uop_2731 = relay.sinh(bop_2724.astype('float32')) # shape=(5, 4, 8)
var_2735 = relay.var("var_2735", dtype = "float32", shape = (5, 4, 8))#candidate|2735|(5, 4, 8)|var|float32
bop_2736 = relay.logical_or(uop_2682.astype('bool'), relay.reshape(var_2735.astype('bool'), relay.shape_of(uop_2682))) # shape=(5, 4, 8)
func_2311_call = mod.get_global_var('func_2311')
func_2312_call = mutated_mod.get_global_var('func_2312')
call_2742 = relay.TupleGetItem(func_2311_call(), 0)
call_2743 = relay.TupleGetItem(func_2312_call(), 0)
bop_2745 = relay.divide(uop_2624.astype('float64'), relay.reshape(bop_2664.astype('float64'), relay.shape_of(uop_2624))) # shape=(5, 4, 8)
bop_2760 = relay.logical_and(uop_2693.astype('bool'), relay.reshape(uop_2655.astype('bool'), relay.shape_of(uop_2693))) # shape=(5, 4, 8)
bop_2763 = relay.floor_divide(bop_2760.astype('float32'), relay.reshape(uop_2624.astype('float32'), relay.shape_of(bop_2760))) # shape=(5, 4, 8)
output = relay.Tuple([call_2636,call_2649,var_2650,call_2660,call_2669,call_2671,call_2689,var_2690,call_2704,call_2715,var_2716,uop_2731,bop_2736,call_2742,bop_2745,bop_2763,])
output2 = relay.Tuple([call_2637,call_2651,var_2650,call_2661,call_2670,call_2672,call_2691,var_2690,call_2705,call_2717,var_2716,uop_2731,bop_2736,call_2743,bop_2745,bop_2763,])
func_2781 = relay.Function([var_2650,var_2690,var_2716,var_2735,], output)
mod['func_2781'] = func_2781
mod = relay.transform.InferType()(mod)
mutated_mod['func_2781'] = func_2781
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2781_call = mutated_mod.get_global_var('func_2781')
var_2783 = relay.var("var_2783", dtype = "uint8", shape = (1120,))#candidate|2783|(1120,)|var|uint8
var_2784 = relay.var("var_2784", dtype = "int64", shape = (700,))#candidate|2784|(700,)|var|int64
var_2785 = relay.var("var_2785", dtype = "int64", shape = (624, 1))#candidate|2785|(624, 1)|var|int64
var_2786 = relay.var("var_2786", dtype = "float32", shape = (5, 4, 8))#candidate|2786|(5, 4, 8)|var|float32
call_2782 = func_2781_call(var_2783,var_2784,var_2785,var_2786,)
output = call_2782
func_2787 = relay.Function([var_2783,var_2784,var_2785,var_2786,], output)
mutated_mod['func_2787'] = func_2787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2066_call = mod.get_global_var('func_2066')
func_2068_call = mutated_mod.get_global_var('func_2068')
call_2807 = relay.TupleGetItem(func_2066_call(), 0)
call_2808 = relay.TupleGetItem(func_2068_call(), 0)
output = call_2807
output2 = call_2808
func_2825 = relay.Function([], output)
mod['func_2825'] = func_2825
mod = relay.transform.InferType()(mod)
mutated_mod['func_2825'] = func_2825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2825_call = mutated_mod.get_global_var('func_2825')
call_2826 = func_2825_call()
output = call_2826
func_2827 = relay.Function([], output)
mutated_mod['func_2827'] = func_2827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2066_call = mod.get_global_var('func_2066')
func_2068_call = mutated_mod.get_global_var('func_2068')
call_2837 = relay.TupleGetItem(func_2066_call(), 0)
call_2838 = relay.TupleGetItem(func_2068_call(), 0)
func_571_call = mod.get_global_var('func_571')
func_576_call = mutated_mod.get_global_var('func_576')
const_2871 = relay.const([-6.224289,-1.542146,0.436504,2.505572,-8.278051,9.850738,-1.262839,-1.253214,5.999045,-5.347334,-3.300618,-8.243397,6.225903,8.636143,4.485580,0.488745,-5.820456,-2.292801,3.959591,-5.116487,3.816337,1.323547,-8.503033,-4.656463,-9.274506,-3.382354,2.076466,-5.790779,9.062935,1.908089,4.664273,-7.713166,-2.654716,0.618474,-1.265435,-1.849501,9.404055,4.131265,3.425451,-9.505219,-5.980205,-5.997027,9.403941,9.036698,5.399043,8.994059,7.157748,-6.843801,1.712112,9.817163,2.886903,6.326921,1.411113,-3.692804,3.988870,-2.247114,5.089471,5.896133,5.745019,7.804492,1.567450,3.369230,-0.642942,6.496957,-4.818930,2.059959,-0.398207,-3.481022,-3.759022,-4.159084,5.588174,4.554873,4.265605,-7.480602,3.075842,7.257379,-2.061575,8.146936,3.152486,-8.427473,-6.987876,3.636250,8.437143,-7.072776,9.410403,4.148312,-5.924068,5.120571,0.325852,-5.846137,-1.305975,8.601103,4.205932,9.632301,5.696826,-8.922609,-6.473877,-2.857168,3.313037,4.537967,2.270462,-2.411374,6.622717,-3.770999,2.653426,-0.283953,-4.062687,-5.834817], dtype = "float64")#candidate|2871|(108,)|const|float64
var_2872 = relay.var("var_2872", dtype = "uint8", shape = (560, 2))#candidate|2872|(560, 2)|var|uint8
call_2870 = relay.TupleGetItem(func_571_call(relay.reshape(const_2871.astype('float64'), [2, 6, 9]), relay.reshape(const_2871.astype('float64'), [2, 6, 9]), relay.reshape(var_2872.astype('uint8'), [4, 280]), ), 3)
call_2873 = relay.TupleGetItem(func_576_call(relay.reshape(const_2871.astype('float64'), [2, 6, 9]), relay.reshape(const_2871.astype('float64'), [2, 6, 9]), relay.reshape(var_2872.astype('uint8'), [4, 280]), ), 3)
output = relay.Tuple([call_2837,call_2870,const_2871,var_2872,])
output2 = relay.Tuple([call_2838,call_2873,const_2871,var_2872,])
func_2874 = relay.Function([var_2872,], output)
mod['func_2874'] = func_2874
mod = relay.transform.InferType()(mod)
var_2875 = relay.var("var_2875", dtype = "uint8", shape = (560, 2))#candidate|2875|(560, 2)|var|uint8
output = func_2874(var_2875)
func_2876 = relay.Function([var_2875], output)
mutated_mod['func_2876'] = func_2876
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2311_call = mod.get_global_var('func_2311')
func_2312_call = mutated_mod.get_global_var('func_2312')
call_2898 = relay.TupleGetItem(func_2311_call(), 0)
call_2899 = relay.TupleGetItem(func_2312_call(), 0)
uop_2922 = relay.cos(call_2898.astype('float32')) # shape=(700,)
uop_2924 = relay.cos(call_2899.astype('float32')) # shape=(700,)
output = uop_2922
output2 = uop_2924
func_2925 = relay.Function([], output)
mod['func_2925'] = func_2925
mod = relay.transform.InferType()(mod)
mutated_mod['func_2925'] = func_2925
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2925_call = mutated_mod.get_global_var('func_2925')
call_2926 = func_2925_call()
output = call_2926
func_2927 = relay.Function([], output)
mutated_mod['func_2927'] = func_2927
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2930 = relay.const([[[2],[1],[-5],[1],[-5],[-8]],[[5],[-7],[-8],[-6],[-10],[-3]],[[-9],[-7],[8],[4],[-3],[-1]],[[3],[8],[-6],[9],[6],[8]],[[8],[2],[-5],[2],[2],[6]]], dtype = "int32")#candidate|2930|(5, 6, 1)|const|int32
var_2931 = relay.var("var_2931", dtype = "int32", shape = (5, 6, 1))#candidate|2931|(5, 6, 1)|var|int32
bop_2932 = relay.add(const_2930.astype('int32'), relay.reshape(var_2931.astype('int32'), relay.shape_of(const_2930))) # shape=(5, 6, 1)
output = relay.Tuple([bop_2932,])
output2 = relay.Tuple([bop_2932,])
func_2935 = relay.Function([var_2931,], output)
mod['func_2935'] = func_2935
mod = relay.transform.InferType()(mod)
mutated_mod['func_2935'] = func_2935
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2936 = relay.var("var_2936", dtype = "int32", shape = (5, 6, 1))#candidate|2936|(5, 6, 1)|var|int32
func_2935_call = mutated_mod.get_global_var('func_2935')
call_2937 = func_2935_call(var_2936)
output = call_2937
func_2938 = relay.Function([var_2936], output)
mutated_mod['func_2938'] = func_2938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_875_call = mod.get_global_var('func_875')
func_877_call = mutated_mod.get_global_var('func_877')
call_2942 = relay.TupleGetItem(func_875_call(), 0)
call_2943 = relay.TupleGetItem(func_877_call(), 0)
output = call_2942
output2 = call_2943
func_2946 = relay.Function([], output)
mod['func_2946'] = func_2946
mod = relay.transform.InferType()(mod)
output = func_2946()
func_2947 = relay.Function([], output)
mutated_mod['func_2947'] = func_2947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2212_call = mod.get_global_var('func_2212')
func_2213_call = mutated_mod.get_global_var('func_2213')
call_3002 = relay.TupleGetItem(func_2212_call(), 0)
call_3003 = relay.TupleGetItem(func_2213_call(), 0)
output = call_3002
output2 = call_3003
func_3013 = relay.Function([], output)
mod['func_3013'] = func_3013
mod = relay.transform.InferType()(mod)
mutated_mod['func_3013'] = func_3013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3013_call = mutated_mod.get_global_var('func_3013')
call_3014 = func_3013_call()
output = call_3014
func_3015 = relay.Function([], output)
mutated_mod['func_3015'] = func_3015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2135_call = mod.get_global_var('func_2135')
func_2136_call = mutated_mod.get_global_var('func_2136')
call_3035 = relay.TupleGetItem(func_2135_call(), 0)
call_3036 = relay.TupleGetItem(func_2136_call(), 0)
func_1690_call = mod.get_global_var('func_1690')
func_1692_call = mutated_mod.get_global_var('func_1692')
call_3037 = relay.TupleGetItem(func_1690_call(), 0)
call_3038 = relay.TupleGetItem(func_1692_call(), 0)
output = relay.Tuple([call_3035,call_3037,])
output2 = relay.Tuple([call_3036,call_3038,])
func_3041 = relay.Function([], output)
mod['func_3041'] = func_3041
mod = relay.transform.InferType()(mod)
mutated_mod['func_3041'] = func_3041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3041_call = mutated_mod.get_global_var('func_3041')
call_3042 = func_3041_call()
output = call_3042
func_3043 = relay.Function([], output)
mutated_mod['func_3043'] = func_3043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2946_call = mod.get_global_var('func_2946')
func_2947_call = mutated_mod.get_global_var('func_2947')
call_3047 = func_2946_call()
call_3048 = func_2946_call()
func_2925_call = mod.get_global_var('func_2925')
func_2927_call = mutated_mod.get_global_var('func_2927')
call_3049 = func_2925_call()
call_3050 = func_2925_call()
func_2311_call = mod.get_global_var('func_2311')
func_2312_call = mutated_mod.get_global_var('func_2312')
call_3052 = relay.TupleGetItem(func_2311_call(), 0)
call_3053 = relay.TupleGetItem(func_2312_call(), 0)
bop_3062 = relay.multiply(call_3052.astype('uint64'), relay.reshape(call_3049.astype('uint64'), relay.shape_of(call_3052))) # shape=(700,)
bop_3065 = relay.multiply(call_3053.astype('uint64'), relay.reshape(call_3050.astype('uint64'), relay.shape_of(call_3053))) # shape=(700,)
func_2825_call = mod.get_global_var('func_2825')
func_2827_call = mutated_mod.get_global_var('func_2827')
call_3066 = func_2825_call()
call_3067 = func_2825_call()
func_1690_call = mod.get_global_var('func_1690')
func_1692_call = mutated_mod.get_global_var('func_1692')
call_3072 = relay.TupleGetItem(func_1690_call(), 0)
call_3073 = relay.TupleGetItem(func_1692_call(), 0)
const_3074 = relay.const([[[True,True,True,False,False,True,True,False,False,False,False,True,False,False],[False,False,True,True,True,False,False,False,True,False,False,True,False,True],[True,False,True,True,True,False,True,True,True,True,False,True,True,False],[True,True,False,True,True,True,False,False,True,False,False,False,True,True],[True,True,False,True,True,True,False,False,True,True,False,True,False,False],[False,True,False,True,False,False,True,False,False,True,False,True,False,True],[False,True,False,True,False,False,False,True,True,False,True,False,False,True]],[[True,False,True,False,False,True,True,False,False,False,False,False,False,True],[True,False,False,True,True,False,True,True,False,True,False,True,False,True],[True,False,True,True,False,False,True,False,False,False,True,False,True,True],[False,True,False,True,True,False,True,False,False,False,True,False,True,True],[True,True,False,True,True,True,False,False,False,True,False,False,True,True],[False,False,True,False,True,True,True,False,False,False,False,False,False,True],[True,False,False,False,True,True,True,True,False,True,True,False,False,True]],[[False,False,True,False,False,False,False,False,True,False,False,True,False,True],[False,True,False,True,True,True,True,False,False,True,True,False,False,False],[True,True,False,True,True,True,False,True,True,False,True,False,False,False],[False,True,True,False,False,True,True,True,False,False,True,False,True,True],[True,False,True,False,True,True,True,False,False,True,True,True,False,True],[False,False,True,False,True,False,False,True,True,True,False,False,True,False],[False,True,True,True,True,False,True,False,False,True,False,False,False,True]],[[False,False,False,False,True,True,False,False,True,False,False,True,True,False],[True,False,False,True,True,True,True,False,False,False,False,False,True,False],[False,False,False,False,False,False,False,True,False,False,False,True,False,False],[False,True,False,True,False,True,True,True,False,False,False,False,False,False],[False,False,True,True,False,True,True,False,True,False,False,True,False,False],[True,True,False,True,False,False,True,False,True,False,False,False,False,False],[False,False,False,True,False,True,False,False,False,True,True,False,True,True]],[[True,False,True,False,True,True,False,True,True,True,False,True,True,False],[True,True,False,True,True,False,False,False,False,False,False,False,False,True],[False,True,False,False,True,True,False,False,False,False,False,False,True,False],[True,False,False,False,True,False,True,True,False,False,True,False,False,True],[True,False,True,True,False,True,True,True,True,False,False,True,False,False],[True,False,False,False,False,False,False,False,False,False,True,False,False,False],[True,False,True,False,True,False,True,True,False,True,False,True,True,False]],[[False,True,False,False,True,False,False,False,False,True,False,False,True,True],[True,True,True,False,True,False,False,False,True,True,True,True,False,False],[False,True,False,False,True,True,False,False,True,True,False,False,False,False],[False,True,True,True,False,False,True,True,True,True,False,False,True,True],[True,True,True,True,True,False,True,False,True,False,False,False,True,True],[False,True,True,True,False,True,False,False,True,False,True,False,True,True],[False,False,True,True,False,False,False,True,False,False,True,True,False,True]],[[False,True,False,False,False,False,True,False,True,False,False,False,False,True],[True,True,True,True,False,False,True,False,False,True,True,True,True,False],[False,True,True,False,False,False,True,False,False,False,False,True,False,False],[True,False,False,False,False,True,False,False,True,True,False,True,False,True],[False,False,True,True,True,False,True,False,False,False,False,False,True,True],[True,True,True,True,False,True,True,False,False,True,False,True,False,False],[True,True,True,True,True,False,False,False,False,False,False,True,False,True]],[[True,True,False,True,True,True,False,True,True,True,True,True,True,True],[True,True,True,False,False,False,True,True,False,False,False,False,False,False],[True,False,True,True,False,True,False,True,True,False,False,False,True,True],[True,False,False,False,False,True,False,False,True,False,False,True,False,False],[True,False,False,True,False,False,False,False,True,False,True,False,False,True],[False,True,False,False,False,False,False,False,True,True,False,False,True,False],[True,True,False,True,True,True,False,True,True,False,False,False,False,True]],[[True,False,True,True,True,True,True,True,False,False,True,True,True,False],[False,False,False,True,True,True,False,False,False,False,True,True,False,True],[True,False,True,False,False,False,False,False,True,True,True,True,True,True],[True,False,True,True,False,True,False,True,False,True,True,False,True,True],[True,False,False,True,False,True,True,True,True,True,True,True,True,False],[False,False,True,True,True,False,False,True,False,True,True,False,False,False],[True,True,True,False,True,False,True,False,True,True,True,True,False,False]],[[False,True,False,False,False,False,False,True,False,False,False,False,True,True],[True,True,False,False,True,True,False,False,True,False,False,True,True,True],[False,True,True,False,True,False,False,True,False,False,False,False,True,False],[True,False,False,False,False,False,False,True,True,False,True,True,False,False],[False,True,True,False,True,True,False,False,True,False,True,True,True,True],[True,False,True,False,False,True,False,False,True,False,True,True,True,True],[False,True,True,False,True,False,False,False,True,False,False,False,False,True]],[[True,True,False,True,True,True,True,False,True,False,False,False,False,False],[True,True,True,True,True,False,True,False,False,True,False,False,True,False],[False,False,True,False,True,True,True,True,False,False,True,True,False,True],[False,True,True,True,False,False,True,True,False,False,True,True,False,True],[True,True,True,True,True,False,True,True,True,False,False,False,True,True],[True,True,False,True,False,False,True,True,False,False,False,True,False,False],[False,False,True,True,False,True,False,True,True,False,False,True,False,False]],[[True,True,True,False,True,False,False,True,False,True,False,False,True,True],[True,True,True,True,False,False,False,False,True,True,True,True,True,False],[False,True,False,True,True,False,True,False,False,True,True,False,False,False],[False,True,True,False,True,False,True,True,False,False,True,False,True,False],[True,False,False,True,True,True,False,False,True,True,False,True,True,False],[True,True,False,True,True,True,True,False,True,True,True,True,True,False],[True,False,False,False,False,True,True,True,False,True,False,True,True,False]],[[False,False,False,True,True,False,False,False,True,False,False,False,True,True],[False,False,True,True,False,False,False,False,True,True,True,True,True,True],[False,False,False,False,False,False,True,True,True,True,False,False,True,False],[True,False,False,True,False,True,False,False,True,False,False,False,False,False],[True,True,True,True,True,True,True,True,False,False,False,True,False,False],[True,True,True,False,False,True,True,False,False,False,True,False,False,True],[False,False,True,False,True,True,True,False,False,True,True,False,True,False]],[[True,True,False,True,True,True,True,True,False,True,True,True,True,False],[True,True,False,True,False,True,True,True,False,True,False,True,False,True],[True,True,True,True,True,False,False,False,True,True,True,False,False,False],[True,True,True,False,True,True,True,True,False,True,False,True,False,False],[False,False,False,True,True,True,False,False,True,False,False,True,False,True],[True,False,False,False,False,True,False,True,False,True,False,False,False,False],[True,False,True,True,False,True,True,False,False,True,False,False,False,True]]], dtype = "bool")#candidate|3074|(14, 7, 14)|const|bool
bop_3075 = relay.power(call_3066.astype('float32'), relay.reshape(const_3074.astype('float32'), relay.shape_of(call_3066))) # shape=(14, 7, 14)
bop_3078 = relay.power(call_3067.astype('float32'), relay.reshape(const_3074.astype('float32'), relay.shape_of(call_3067))) # shape=(14, 7, 14)
output = relay.Tuple([call_3047,bop_3062,call_3072,bop_3075,])
output2 = relay.Tuple([call_3048,bop_3065,call_3073,bop_3078,])
func_3080 = relay.Function([], output)
mod['func_3080'] = func_3080
mod = relay.transform.InferType()(mod)
mutated_mod['func_3080'] = func_3080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3080_call = mutated_mod.get_global_var('func_3080')
call_3081 = func_3080_call()
output = call_3081
func_3082 = relay.Function([], output)
mutated_mod['func_3082'] = func_3082
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1258_call = mod.get_global_var('func_1258')
func_1259_call = mutated_mod.get_global_var('func_1259')
call_3090 = relay.TupleGetItem(func_1258_call(), 1)
call_3091 = relay.TupleGetItem(func_1259_call(), 1)
func_2212_call = mod.get_global_var('func_2212')
func_2213_call = mutated_mod.get_global_var('func_2213')
call_3095 = relay.TupleGetItem(func_2212_call(), 0)
call_3096 = relay.TupleGetItem(func_2213_call(), 0)
uop_3097 = relay.log(call_3095.astype('float64')) # shape=(14, 7, 14)
uop_3099 = relay.log(call_3096.astype('float64')) # shape=(14, 7, 14)
output = relay.Tuple([call_3090,uop_3097,])
output2 = relay.Tuple([call_3091,uop_3099,])
func_3111 = relay.Function([], output)
mod['func_3111'] = func_3111
mod = relay.transform.InferType()(mod)
output = func_3111()
func_3112 = relay.Function([], output)
mutated_mod['func_3112'] = func_3112
mutated_mod = relay.transform.InferType()(mutated_mod)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_3161 = func_361_call()
call_3162 = func_361_call()
output = relay.Tuple([call_3161,])
output2 = relay.Tuple([call_3162,])
func_3171 = relay.Function([], output)
mod['func_3171'] = func_3171
mod = relay.transform.InferType()(mod)
output = func_3171()
func_3172 = relay.Function([], output)
mutated_mod['func_3172'] = func_3172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2825_call = mod.get_global_var('func_2825')
func_2827_call = mutated_mod.get_global_var('func_2827')
call_3173 = func_2825_call()
call_3174 = func_2825_call()
func_1386_call = mod.get_global_var('func_1386')
func_1390_call = mutated_mod.get_global_var('func_1390')
var_3195 = relay.var("var_3195", dtype = "float32", shape = (117,))#candidate|3195|(117,)|var|float32
var_3196 = relay.var("var_3196", dtype = "uint8", shape = (1120,))#candidate|3196|(1120,)|var|uint8
call_3194 = relay.TupleGetItem(func_1386_call(relay.reshape(var_3195.astype('float32'), [117,]), relay.reshape(var_3196.astype('uint8'), [1120,]), ), 0)
call_3197 = relay.TupleGetItem(func_1390_call(relay.reshape(var_3195.astype('float32'), [117,]), relay.reshape(var_3196.astype('uint8'), [1120,]), ), 0)
output = relay.Tuple([call_3173,call_3194,var_3195,var_3196,])
output2 = relay.Tuple([call_3174,call_3197,var_3195,var_3196,])
func_3230 = relay.Function([var_3195,var_3196,], output)
mod['func_3230'] = func_3230
mod = relay.transform.InferType()(mod)
var_3231 = relay.var("var_3231", dtype = "float32", shape = (117,))#candidate|3231|(117,)|var|float32
var_3232 = relay.var("var_3232", dtype = "uint8", shape = (1120,))#candidate|3232|(1120,)|var|uint8
output = func_3230(var_3231,var_3232,)
func_3233 = relay.Function([var_3231,var_3232,], output)
mutated_mod['func_3233'] = func_3233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_875_call = mod.get_global_var('func_875')
func_877_call = mutated_mod.get_global_var('func_877')
call_3351 = relay.TupleGetItem(func_875_call(), 0)
call_3352 = relay.TupleGetItem(func_877_call(), 0)
output = call_3351
output2 = call_3352
func_3354 = relay.Function([], output)
mod['func_3354'] = func_3354
mod = relay.transform.InferType()(mod)
output = func_3354()
func_3355 = relay.Function([], output)
mutated_mod['func_3355'] = func_3355
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2946_call = mod.get_global_var('func_2946')
func_2947_call = mutated_mod.get_global_var('func_2947')
call_3365 = func_2946_call()
call_3366 = func_2946_call()
func_2925_call = mod.get_global_var('func_2925')
func_2927_call = mutated_mod.get_global_var('func_2927')
call_3369 = func_2925_call()
call_3370 = func_2925_call()
func_3354_call = mod.get_global_var('func_3354')
func_3355_call = mutated_mod.get_global_var('func_3355')
call_3388 = func_3354_call()
call_3389 = func_3354_call()
output = relay.Tuple([call_3365,call_3369,call_3388,])
output2 = relay.Tuple([call_3366,call_3370,call_3389,])
func_3398 = relay.Function([], output)
mod['func_3398'] = func_3398
mod = relay.transform.InferType()(mod)
mutated_mod['func_3398'] = func_3398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3398_call = mutated_mod.get_global_var('func_3398')
call_3399 = func_3398_call()
output = call_3399
func_3400 = relay.Function([], output)
mutated_mod['func_3400'] = func_3400
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3428 = relay.var("var_3428", dtype = "float64", shape = (6, 1, 10))#candidate|3428|(6, 1, 10)|var|float64
uop_3429 = relay.log10(var_3428.astype('float64')) # shape=(6, 1, 10)
uop_3437 = relay.acos(uop_3429.astype('float32')) # shape=(6, 1, 10)
func_1564_call = mod.get_global_var('func_1564')
func_1566_call = mutated_mod.get_global_var('func_1566')
const_3440 = relay.const([[-8.500640,-2.962530,-5.800231],[3.846139,7.149666,9.006836],[-8.311139,2.828497,1.293682],[7.948192,9.596317,-9.919509],[-7.292377,7.809409,2.444102],[-9.513451,4.105389,0.322956],[-2.847406,-8.348271,6.244021],[-5.049027,1.594693,9.099329],[-8.138779,-9.483985,5.756916],[-3.954824,-5.749567,-9.405974],[6.616495,4.642978,-5.047479],[-5.438297,8.980668,-5.127297],[-2.017077,6.551093,0.781928],[-5.494335,5.774839,1.043146],[1.512779,-2.054074,-3.072958],[-6.767769,3.217925,-3.049905],[-5.842880,2.302300,4.983958],[-1.720171,-1.317440,1.152207],[-8.984285,1.444209,6.221778],[9.713453,-0.687219,-2.197410],[-8.654436,-0.116533,7.459569],[9.155861,3.116324,5.180986],[9.706124,-5.536070,4.707133],[8.876632,3.359405,8.349704],[2.256289,-5.064144,-8.356341],[-2.210001,1.675607,0.396642],[-7.722082,-6.861063,9.645577],[-1.918727,-8.798758,-9.014396],[3.147337,8.932765,-3.267008],[8.408685,8.138108,9.923158],[-4.267811,7.435221,6.199946],[-1.771273,2.925514,3.061699],[5.454853,9.115781,7.333870],[4.513511,5.395820,5.694104],[-2.634576,-6.681902,-5.900542],[3.284335,2.394750,-2.775614],[2.169967,-9.713904,-0.802278],[1.866363,-7.475375,9.625544],[-9.147396,-0.041760,1.818674],[8.654476,-0.964600,-3.022794],[-4.205091,3.502611,-3.363386],[-1.154571,4.675141,-5.751213],[-6.708100,6.347147,5.127492],[-6.954844,0.500103,1.785043],[2.497006,-7.865664,-6.099208],[-1.328705,7.698887,1.857346],[-0.545807,4.598399,-1.729061],[8.311498,-0.416014,3.736333],[9.060075,3.994293,-5.589714],[7.218174,-7.397797,8.054557],[-8.946949,7.936906,-2.199683],[2.169499,-3.435043,-9.579821],[8.705216,1.356613,-2.786093],[9.821053,7.799554,-6.255556],[2.184309,1.927304,-2.131221],[0.156638,-5.836839,-5.334707],[4.640990,2.118786,-6.497581],[-8.342485,6.602479,1.620612],[7.894796,4.207725,-3.854146],[-6.545294,-5.067393,0.403904],[4.085506,9.291520,2.735077],[-3.280773,-6.104374,-2.220029],[6.798017,-1.681370,-7.544495],[-4.947211,-0.287588,-9.223434],[7.992302,-4.830413,-7.347674],[-8.593854,-2.715691,-8.848015],[6.497396,-8.532913,-2.529509],[6.939553,-3.394176,5.025359],[7.292118,-3.547764,9.169104],[-2.505076,1.665599,-1.886842],[-5.538410,7.689873,7.416400],[-7.225920,-6.072860,-0.830389],[7.866074,-4.848624,6.718368],[6.107329,9.387089,-8.828283],[-0.306530,-8.799586,5.737084],[-0.995291,1.997249,6.726142],[6.852541,-7.037923,-0.326709],[-2.055144,-6.307412,8.918104],[-7.086260,-4.758597,-7.634932],[8.389274,-8.188445,7.217386],[-0.835822,7.930022,4.449809],[-0.039140,0.151327,2.475963],[8.984268,3.387184,-8.682186],[7.423818,2.129217,2.705830],[-3.906285,5.673713,-3.052509],[3.275216,-1.152652,-0.774535],[3.253065,-1.159414,0.037352],[-7.187860,8.581996,-2.263091],[2.062192,5.906742,-2.221305],[-9.253939,8.891245,6.396674],[-9.757846,-8.102582,5.606281],[4.089021,-5.806482,0.970052],[6.796773,-5.876704,-4.761497],[-6.865093,5.607459,-3.865609],[-6.415811,-8.831913,-9.996312],[2.538680,-2.132135,0.442843],[7.566684,-5.039701,-8.874705],[9.167210,-9.175974,7.621239],[1.581080,-2.970301,6.396022],[-0.669809,7.298348,0.201100],[-9.260169,3.677257,-0.869153],[-1.988278,6.760556,9.275729],[7.443256,7.502571,0.251297],[-1.672637,-7.893796,3.543154],[4.024008,-5.943372,-6.586601],[9.659241,-5.877582,-2.966089],[8.934516,-2.763431,7.704114],[0.744305,3.495851,-9.859269],[4.629453,6.617071,3.210424],[9.601512,-8.739036,-8.742888],[9.717244,7.071757,-8.719671],[-4.350935,-4.809199,-5.188296],[6.781461,-4.555888,-3.011688],[8.438981,7.298307,1.298576],[3.213446,-2.216545,-9.707028],[-0.236702,-0.313543,-1.087641],[4.848793,-0.140735,6.142164],[-2.028631,-7.994707,8.302975],[1.324827,-7.023869,3.635925],[-1.846940,-7.403150,-3.531310],[0.143992,-9.671865,-9.776010],[-0.704055,-1.876122,-3.715881],[0.381878,-4.715926,5.378353],[-4.235022,-5.234660,-4.615545],[-3.380124,-4.135599,3.786085],[-3.632827,5.423851,-7.221673],[4.445299,-8.200562,5.338145],[1.786627,3.781546,4.050056],[-6.688958,1.578879,-0.241716],[-7.513652,-0.433306,-2.983649],[-3.624201,-5.308319,3.076590],[3.739289,7.524507,-5.186167],[-5.161985,4.803062,2.486540],[2.307055,-2.059353,-0.623181],[-9.145708,-9.569408,8.573113],[-1.117261,7.826240,-3.118127],[8.457313,9.064351,0.155822],[9.096488,0.918271,1.394537],[3.495286,-1.636081,9.687559],[2.172915,-2.732171,1.064141],[-9.993064,7.582684,-3.518360],[-3.210401,4.588566,7.337623],[-0.322292,2.315665,0.291297],[-2.609366,0.015744,5.224063],[-2.505704,-8.730156,-0.317090],[-3.743899,2.483835,-6.557331],[9.717514,9.167819,-7.802911],[7.072515,1.934665,-7.563704],[1.577568,-0.232846,-2.263826],[-9.890375,-8.019468,3.276700],[-7.257059,2.335250,8.759503],[7.499657,-0.596058,6.513068],[6.461664,1.068257,9.048576],[-5.552155,7.294074,0.671096],[-9.834220,-0.123744,-3.915194],[6.909822,5.653642,-0.016343],[-4.540535,-2.139116,-2.813822],[3.110501,-6.668359,0.741252],[-7.803507,7.145455,-5.154296],[5.399641,-7.838665,6.835185],[2.892758,0.749738,8.948709],[2.312199,1.345617,-9.146728],[-3.752679,-8.096553,3.695968],[-3.582707,9.504819,4.666967],[2.662724,-1.427650,-4.881528],[-8.241799,-8.508412,-9.489776],[-9.751316,7.280192,1.586484],[1.984059,6.605393,8.243596],[2.946354,-3.911043,0.080785],[-6.692658,6.631953,-7.966926],[-8.158887,8.077838,-9.852355],[-7.269597,-9.798074,-1.137192],[-2.783227,0.663261,9.086165],[-0.762541,-9.267993,6.664721],[-4.096313,-9.564648,-0.262505],[0.413799,-2.854405,6.823310],[-7.766304,9.859141,7.337093],[9.228896,5.020920,0.648022],[4.277255,-5.018029,5.737383],[2.247521,9.038110,0.526359],[-6.341753,9.774559,0.739187],[1.009506,-5.595094,-3.351332],[-0.966614,5.125375,-3.101930],[6.503171,-3.565613,-9.687586],[9.067667,4.705112,8.241764],[5.255385,1.409945,-5.019204],[6.329478,0.900233,-0.499933],[-6.404189,2.527763,6.413789],[-5.389776,9.612830,-3.195121],[-1.392876,8.668945,-1.326954],[-1.161271,-9.575732,-0.456684],[7.084762,-0.939053,-3.563109],[-8.209845,4.720465,-8.525714],[-1.089747,6.557645,-4.431811],[6.961125,-7.851108,-1.300426],[9.123235,-7.851581,0.333384],[5.070174,-8.636934,7.745655],[-6.318761,6.968425,0.859681],[-7.405615,4.681138,4.875991],[5.067913,-2.012180,8.694355],[3.100212,-9.180371,-1.765674],[-2.442730,-0.622137,8.467617],[4.348740,0.316919,9.048727],[4.093867,-2.932757,-6.568447],[-5.156438,-1.054112,7.286235],[5.890767,5.668271,-1.062748],[2.894376,6.502803,8.445111],[5.518242,-8.552976,-8.454375],[0.885435,-8.038292,-6.271185],[1.697683,-6.101066,3.974259],[7.026147,-8.802420,-5.070066],[-2.548054,-7.103473,5.671014],[-6.260448,-1.513448,-8.390380],[7.195117,-3.486633,4.566305],[-4.272828,3.986214,1.717993],[-3.523897,-7.545536,2.036850],[8.749506,-3.744979,5.288984],[6.679793,9.178254,-7.438028],[-4.008116,9.992687,2.893118],[9.990506,-4.474146,3.859528],[-2.693575,-3.727064,-1.016869],[3.502574,-6.708411,9.538458],[-3.605783,7.168403,7.703112],[5.974472,7.830953,-1.541534],[4.673623,-7.400098,3.004371],[1.628281,9.521314,-1.235833],[6.688883,1.343849,7.203594],[3.357076,-1.878616,8.289681],[4.409517,8.327897,-7.006267],[0.203177,-2.917318,4.753500],[8.709310,7.411622,-9.260612]], dtype = "float32")#candidate|3440|(231, 3)|const|float32
call_3439 = func_1564_call(relay.reshape(const_3440.astype('float32'), [7, 11, 9]))
call_3441 = func_1564_call(relay.reshape(const_3440.astype('float32'), [7, 11, 9]))
uop_3443 = relay.rsqrt(const_3440.astype('float64')) # shape=(231, 3)
output = relay.Tuple([uop_3437,call_3439,uop_3443,])
output2 = relay.Tuple([uop_3437,call_3441,uop_3443,])
func_3459 = relay.Function([var_3428,], output)
mod['func_3459'] = func_3459
mod = relay.transform.InferType()(mod)
mutated_mod['func_3459'] = func_3459
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3460 = relay.var("var_3460", dtype = "float64", shape = (6, 1, 10))#candidate|3460|(6, 1, 10)|var|float64
func_3459_call = mutated_mod.get_global_var('func_3459')
call_3461 = func_3459_call(var_3460)
output = call_3461
func_3462 = relay.Function([var_3460], output)
mutated_mod['func_3462'] = func_3462
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3464 = relay.var("var_3464", dtype = "int64", shape = ())#candidate|3464|()|var|int64
var_3465 = relay.var("var_3465", dtype = "int64", shape = (12, 14, 1))#candidate|3465|(12, 14, 1)|var|int64
bop_3466 = relay.less(var_3464.astype('bool'), var_3465.astype('bool')) # shape=(12, 14, 1)
output = relay.Tuple([bop_3466,])
output2 = relay.Tuple([bop_3466,])
func_3475 = relay.Function([var_3464,var_3465,], output)
mod['func_3475'] = func_3475
mod = relay.transform.InferType()(mod)
mutated_mod['func_3475'] = func_3475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3475_call = mutated_mod.get_global_var('func_3475')
var_3477 = relay.var("var_3477", dtype = "int64", shape = ())#candidate|3477|()|var|int64
var_3478 = relay.var("var_3478", dtype = "int64", shape = (12, 14, 1))#candidate|3478|(12, 14, 1)|var|int64
call_3476 = func_3475_call(var_3477,var_3478,)
output = call_3476
func_3479 = relay.Function([var_3477,var_3478,], output)
mutated_mod['func_3479'] = func_3479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3354_call = mod.get_global_var('func_3354')
func_3355_call = mutated_mod.get_global_var('func_3355')
call_3517 = func_3354_call()
call_3518 = func_3354_call()
func_2066_call = mod.get_global_var('func_2066')
func_2068_call = mutated_mod.get_global_var('func_2068')
call_3521 = relay.TupleGetItem(func_2066_call(), 1)
call_3522 = relay.TupleGetItem(func_2068_call(), 1)
output = relay.Tuple([call_3517,call_3521,])
output2 = relay.Tuple([call_3518,call_3522,])
func_3539 = relay.Function([], output)
mod['func_3539'] = func_3539
mod = relay.transform.InferType()(mod)
mutated_mod['func_3539'] = func_3539
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3539_call = mutated_mod.get_global_var('func_3539')
call_3540 = func_3539_call()
output = call_3540
func_3541 = relay.Function([], output)
mutated_mod['func_3541'] = func_3541
mutated_mod = relay.transform.InferType()(mutated_mod)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_3562 = func_361_call()
call_3563 = func_361_call()
output = relay.Tuple([call_3562,])
output2 = relay.Tuple([call_3563,])
func_3566 = relay.Function([], output)
mod['func_3566'] = func_3566
mod = relay.transform.InferType()(mod)
output = func_3566()
func_3567 = relay.Function([], output)
mutated_mod['func_3567'] = func_3567
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3601 = relay.var("var_3601", dtype = "float64", shape = (11, 13, 8))#candidate|3601|(11, 13, 8)|var|float64
uop_3602 = relay.log(var_3601.astype('float64')) # shape=(11, 13, 8)
func_1386_call = mod.get_global_var('func_1386')
func_1390_call = mutated_mod.get_global_var('func_1390')
const_3607 = relay.const([[-1.755027,-4.463621,-4.325623],[5.936184,-4.939436,8.157870],[2.200383,2.192963,1.692289],[4.604243,-3.126928,-9.814000],[-1.208994,-0.299353,-5.506216],[-4.873846,-5.198903,8.173851],[3.943140,-2.963928,-7.059404],[-6.043141,-1.336946,3.896219],[-5.318057,3.242739,-1.374989],[2.354648,4.878528,5.644935],[0.544671,-3.949183,-0.263395],[2.321987,-0.595461,-8.775958],[4.845460,6.479792,-5.358433],[5.230008,0.902763,1.026403],[-6.489936,-1.300482,-8.159024],[-7.916794,6.207206,-4.280695],[-0.961818,-6.536657,6.757223],[2.908031,3.913284,-0.681384],[1.722669,-6.811512,5.246543],[-7.140708,-3.867749,5.357045],[4.531385,-7.256257,9.037336],[-9.591611,-7.771950,-7.306090],[2.492932,-1.511990,-9.063458],[0.977862,5.033974,-8.737384],[7.553437,-4.034471,-5.008086],[7.518180,1.681528,-5.988390],[-5.573117,-4.874270,7.101319],[-9.044987,-6.199817,4.879594],[-8.141655,2.290845,-3.868419],[-1.269918,-1.000312,4.793912],[-0.097672,-4.728745,5.602202],[-9.077472,-3.134179,-9.415756],[-9.421579,-0.841828,-8.295805],[2.595504,-0.326319,-5.724305],[7.934248,5.532894,1.461607],[-6.556193,2.010210,-1.964540],[8.887231,-9.170821,4.339443],[-8.052328,3.926485,4.683992],[-7.520606,-9.793700,1.765030]], dtype = "float32")#candidate|3607|(39, 3)|const|float32
var_3608 = relay.var("var_3608", dtype = "uint8", shape = (1120,))#candidate|3608|(1120,)|var|uint8
call_3606 = relay.TupleGetItem(func_1386_call(relay.reshape(const_3607.astype('float32'), [117,]), relay.reshape(var_3608.astype('uint8'), [1120,]), ), 3)
call_3609 = relay.TupleGetItem(func_1390_call(relay.reshape(const_3607.astype('float32'), [117,]), relay.reshape(var_3608.astype('uint8'), [1120,]), ), 3)
func_2293_call = mod.get_global_var('func_2293')
func_2295_call = mutated_mod.get_global_var('func_2295')
call_3617 = relay.TupleGetItem(func_2293_call(relay.reshape(var_3608.astype('uint8'), [1120,])), 5)
call_3618 = relay.TupleGetItem(func_2295_call(relay.reshape(var_3608.astype('uint8'), [1120,])), 5)
output = relay.Tuple([uop_3602,call_3606,const_3607,var_3608,call_3617,])
output2 = relay.Tuple([uop_3602,call_3609,const_3607,var_3608,call_3618,])
func_3621 = relay.Function([var_3601,var_3608,], output)
mod['func_3621'] = func_3621
mod = relay.transform.InferType()(mod)
var_3622 = relay.var("var_3622", dtype = "float64", shape = (11, 13, 8))#candidate|3622|(11, 13, 8)|var|float64
var_3623 = relay.var("var_3623", dtype = "uint8", shape = (1120,))#candidate|3623|(1120,)|var|uint8
output = func_3621(var_3622,var_3623,)
func_3624 = relay.Function([var_3622,var_3623,], output)
mutated_mod['func_3624'] = func_3624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1258_call = mod.get_global_var('func_1258')
func_1259_call = mutated_mod.get_global_var('func_1259')
call_3659 = relay.TupleGetItem(func_1258_call(), 0)
call_3660 = relay.TupleGetItem(func_1259_call(), 0)
uop_3669 = relay.sinh(call_3659.astype('float64')) # shape=(2, 6, 9)
uop_3671 = relay.sinh(call_3660.astype('float64')) # shape=(2, 6, 9)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_3672 = func_361_call()
call_3673 = func_361_call()
output = relay.Tuple([uop_3669,call_3672,])
output2 = relay.Tuple([uop_3671,call_3673,])
func_3675 = relay.Function([], output)
mod['func_3675'] = func_3675
mod = relay.transform.InferType()(mod)
output = func_3675()
func_3676 = relay.Function([], output)
mutated_mod['func_3676'] = func_3676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2066_call = mod.get_global_var('func_2066')
func_2068_call = mutated_mod.get_global_var('func_2068')
call_3680 = relay.TupleGetItem(func_2066_call(), 1)
call_3681 = relay.TupleGetItem(func_2068_call(), 1)
var_3684 = relay.var("var_3684", dtype = "bool", shape = (14, 7, 14))#candidate|3684|(14, 7, 14)|var|bool
bop_3685 = relay.left_shift(call_3680.astype('uint64'), relay.reshape(var_3684.astype('uint64'), relay.shape_of(call_3680))) # shape=(14, 7, 14)
bop_3688 = relay.left_shift(call_3681.astype('uint64'), relay.reshape(var_3684.astype('uint64'), relay.shape_of(call_3681))) # shape=(14, 7, 14)
uop_3724 = relay.sin(var_3684.astype('float64')) # shape=(14, 7, 14)
output = relay.Tuple([bop_3685,uop_3724,])
output2 = relay.Tuple([bop_3688,uop_3724,])
func_3726 = relay.Function([var_3684,], output)
mod['func_3726'] = func_3726
mod = relay.transform.InferType()(mod)
mutated_mod['func_3726'] = func_3726
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3727 = relay.var("var_3727", dtype = "bool", shape = (14, 7, 14))#candidate|3727|(14, 7, 14)|var|bool
func_3726_call = mutated_mod.get_global_var('func_3726')
call_3728 = func_3726_call(var_3727)
output = call_3728
func_3729 = relay.Function([var_3727], output)
mutated_mod['func_3729'] = func_3729
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1258_call = mod.get_global_var('func_1258')
func_1259_call = mutated_mod.get_global_var('func_1259')
call_3795 = relay.TupleGetItem(func_1258_call(), 1)
call_3796 = relay.TupleGetItem(func_1259_call(), 1)
func_3041_call = mod.get_global_var('func_3041')
func_3043_call = mutated_mod.get_global_var('func_3043')
call_3797 = relay.TupleGetItem(func_3041_call(), 1)
call_3798 = relay.TupleGetItem(func_3043_call(), 1)
output = relay.Tuple([call_3795,call_3797,])
output2 = relay.Tuple([call_3796,call_3798,])
func_3809 = relay.Function([], output)
mod['func_3809'] = func_3809
mod = relay.transform.InferType()(mod)
output = func_3809()
func_3810 = relay.Function([], output)
mutated_mod['func_3810'] = func_3810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2825_call = mod.get_global_var('func_2825')
func_2827_call = mutated_mod.get_global_var('func_2827')
call_3828 = func_2825_call()
call_3829 = func_2825_call()
func_1741_call = mod.get_global_var('func_1741')
func_1744_call = mutated_mod.get_global_var('func_1744')
const_3846 = relay.const([[3.029402,-8.051361,-0.005314],[-2.591856,-9.035367,2.748929],[-4.225343,7.953505,7.488367],[-8.739231,4.745423,-6.805857],[9.949141,8.456073,-2.761059],[-3.634367,-8.071174,4.543378],[2.552327,-1.804408,8.794415],[6.445930,6.866937,-4.919395],[-3.478296,9.313493,-1.254829],[-8.411612,-0.865340,7.820848],[-8.006244,-6.051285,-7.918710],[-1.272961,6.716703,-9.899349],[-2.300240,2.329881,-4.732007],[-4.252005,-6.171854,6.882563],[4.112585,8.756836,6.131617],[-9.265518,-2.969257,-9.983201],[-5.982446,-6.500128,6.490335],[-1.222364,7.215092,-6.803059],[-6.217460,-6.828296,-7.724352],[6.631262,9.809443,5.377208],[-4.951802,-8.422971,5.000367],[6.106767,5.197046,6.858472]], dtype = "float32")#candidate|3846|(22, 3)|const|float32
call_3845 = func_1741_call(relay.reshape(const_3846.astype('float32'), [6, 11]))
call_3847 = func_1741_call(relay.reshape(const_3846.astype('float32'), [6, 11]))
func_3398_call = mod.get_global_var('func_3398')
func_3400_call = mutated_mod.get_global_var('func_3400')
call_3861 = relay.TupleGetItem(func_3398_call(), 1)
call_3862 = relay.TupleGetItem(func_3400_call(), 1)
output = relay.Tuple([call_3828,call_3845,const_3846,call_3861,])
output2 = relay.Tuple([call_3829,call_3847,const_3846,call_3862,])
func_3875 = relay.Function([], output)
mod['func_3875'] = func_3875
mod = relay.transform.InferType()(mod)
output = func_3875()
func_3876 = relay.Function([], output)
mutated_mod['func_3876'] = func_3876
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3902 = relay.const([[[-8,2,6,1,-3,-4,-10,3,1,-9],[10,-10,-3,1,-7,-9,4,2,1,-7],[-8,9,6,-6,-5,-9,-7,7,9,4],[-5,-1,-6,10,6,-2,-8,10,5,2]],[[-1,7,9,7,-2,-4,-6,7,-7,9],[-4,-8,6,-8,-6,-10,-1,-6,-1,-10],[6,1,8,1,-4,-1,-5,-5,-8,1],[3,-10,8,-7,-9,-1,1,-4,-9,4]],[[-9,-4,-3,5,-1,-3,8,1,9,5],[4,-2,8,-4,3,10,3,6,4,9],[-8,2,-8,-1,10,5,-4,1,-5,8],[-2,-1,4,-5,1,-6,6,4,-2,1]],[[1,-9,2,-8,4,-4,6,-3,3,1],[-2,2,8,2,-10,-3,6,7,-2,5],[-1,-2,2,-7,5,-8,6,5,-5,3],[9,-8,8,4,-10,-5,6,8,-3,5]],[[-5,-5,5,5,8,-7,4,5,-1,-9],[8,4,1,5,6,-4,-5,2,-2,1],[-4,8,-4,-9,3,-7,-2,-8,2,-9],[-3,1,-5,-7,-3,6,7,-5,-6,-7]],[[4,2,5,-1,3,-9,-6,-4,7,-5],[-10,-8,-4,9,9,10,1,9,2,-7],[3,-1,6,7,7,-4,2,5,6,7],[1,9,1,-10,-2,-8,-10,-2,-4,-2]],[[3,-7,9,-1,7,10,-5,-2,9,-9],[-8,3,-6,8,6,-1,7,3,4,-1],[-2,-1,-2,-5,-4,9,1,-1,9,-9],[9,-5,1,-2,-2,6,-6,4,9,-8]],[[-4,-4,-8,-4,-2,3,6,-8,6,2],[5,-5,-4,-10,8,5,-2,7,-3,1],[7,-9,-2,1,-8,-7,2,5,-10,-8],[-10,10,-3,-6,-9,6,-10,8,3,-1]],[[2,-4,-1,10,-2,10,3,-6,7,7],[-6,2,7,8,-7,8,9,2,1,-1],[-10,4,1,2,-1,-5,-1,5,-7,7],[-3,1,-9,10,-5,-2,2,-10,8,-4]],[[-10,-6,-8,-8,-3,6,10,-8,2,-8],[8,6,5,-6,10,2,9,-1,-8,-1],[-4,8,6,-2,3,9,-9,3,1,-7],[-9,2,-6,4,-4,6,2,3,-2,-8]],[[6,-8,2,-8,-1,5,3,-8,2,4],[9,-5,6,10,-6,10,-6,6,-10,-3],[9,-10,7,3,2,-7,-7,-3,-4,-8],[-1,-10,-9,-5,1,9,-7,-4,9,-6]]], dtype = "int64")#candidate|3902|(11, 4, 10)|const|int64
const_3903 = relay.const([[[4,5,5,-3,-6,9,-1,-5,-2,-8],[2,-1,-6,-10,3,-10,3,7,3,-6],[-10,-7,4,2,5,-9,1,7,-4,-10],[-6,-5,8,-8,-9,-3,3,-4,2,-3]],[[7,-1,-9,-4,5,1,8,4,-6,-10],[9,8,3,-9,7,1,-1,2,3,2],[-2,3,8,10,10,-1,-3,-2,-10,-3],[-10,-10,-1,2,8,3,-8,-4,2,10]],[[-3,-2,9,-5,5,-7,6,-8,10,8],[6,10,8,2,-7,3,-5,-8,-8,-5],[-3,-8,10,6,7,-9,-7,-1,-4,-4],[-7,-1,-3,9,2,-6,4,5,-1,-3]],[[-5,5,1,5,-1,4,-10,-10,-4,6],[-3,-2,-6,1,6,-10,-6,10,-3,1],[-8,1,4,2,-2,-5,-9,-2,-3,-4],[6,-9,9,10,-8,5,9,-7,1,10]],[[-8,-8,3,-3,4,-7,-3,3,-10,5],[5,6,-8,-5,-2,2,-2,-6,2,-1],[-9,7,5,-6,-2,-2,3,-8,-3,-9],[2,7,-4,8,4,-2,-10,-7,-10,9]],[[-5,8,-3,8,1,-2,-3,-8,-4,4],[-8,5,7,2,-8,-9,3,1,-4,-3],[10,-10,6,9,6,2,-2,-1,-10,8],[3,-10,-5,-4,2,7,-5,-3,7,-1]],[[-7,-5,9,-10,9,4,7,2,-5,-2],[6,-8,-6,-9,5,4,-4,-3,-4,-1],[-4,7,-1,1,5,-2,3,-9,-1,2],[10,-1,6,5,-10,-3,3,4,-8,9]],[[-10,-2,1,2,2,1,9,-4,6,4],[-8,-8,10,-3,9,-2,3,2,7,-7],[7,1,-9,-2,6,9,-7,-5,1,5],[-1,8,3,9,3,9,3,-7,-6,-7]],[[7,8,-5,10,2,5,-2,-9,-3,5],[4,6,-5,-10,-2,-5,5,4,6,-5],[9,4,-4,-4,-9,3,-4,-3,-1,-2],[-1,5,-2,-3,3,7,-1,1,3,-2]],[[-6,-8,-5,-1,-3,3,-2,8,-5,2],[-1,10,-1,-9,8,-7,-8,7,5,10],[-3,-9,-1,-8,-10,-4,1,-4,5,-7],[7,-9,8,-6,6,-8,-1,3,-8,8]],[[-3,-10,10,-7,9,10,-7,-9,-5,-7],[-5,9,3,-9,6,8,4,4,-4,-9],[-2,-9,7,3,6,-2,-4,-8,4,-10],[5,-10,6,10,-4,2,-7,-4,-10,-6]]], dtype = "int64")#candidate|3903|(11, 4, 10)|const|int64
bop_3904 = relay.not_equal(const_3902.astype('bool'), relay.reshape(const_3903.astype('bool'), relay.shape_of(const_3902))) # shape=(11, 4, 10)
func_3398_call = mod.get_global_var('func_3398')
func_3400_call = mutated_mod.get_global_var('func_3400')
call_3908 = relay.TupleGetItem(func_3398_call(), 0)
call_3909 = relay.TupleGetItem(func_3400_call(), 0)
func_2250_call = mod.get_global_var('func_2250')
func_2252_call = mutated_mod.get_global_var('func_2252')
var_3924 = relay.var("var_3924", dtype = "int64", shape = (624,))#candidate|3924|(624,)|var|int64
call_3923 = relay.TupleGetItem(func_2250_call(relay.reshape(var_3924.astype('int64'), [13, 12, 4])), 0)
call_3925 = relay.TupleGetItem(func_2252_call(relay.reshape(var_3924.astype('int64'), [13, 12, 4])), 0)
output = relay.Tuple([bop_3904,call_3908,call_3923,var_3924,])
output2 = relay.Tuple([bop_3904,call_3909,call_3925,var_3924,])
func_3939 = relay.Function([var_3924,], output)
mod['func_3939'] = func_3939
mod = relay.transform.InferType()(mod)
var_3940 = relay.var("var_3940", dtype = "int64", shape = (624,))#candidate|3940|(624,)|var|int64
output = func_3939(var_3940)
func_3941 = relay.Function([var_3940], output)
mutated_mod['func_3941'] = func_3941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3539_call = mod.get_global_var('func_3539')
func_3541_call = mutated_mod.get_global_var('func_3541')
call_3954 = relay.TupleGetItem(func_3539_call(), 0)
call_3955 = relay.TupleGetItem(func_3541_call(), 0)
func_3675_call = mod.get_global_var('func_3675')
func_3676_call = mutated_mod.get_global_var('func_3676')
call_3966 = relay.TupleGetItem(func_3675_call(), 1)
call_3967 = relay.TupleGetItem(func_3676_call(), 1)
func_2135_call = mod.get_global_var('func_2135')
func_2136_call = mutated_mod.get_global_var('func_2136')
call_3970 = relay.TupleGetItem(func_2135_call(), 0)
call_3971 = relay.TupleGetItem(func_2136_call(), 0)
bop_3974 = relay.less_equal(call_3966.astype('bool'), relay.reshape(call_3954.astype('bool'), relay.shape_of(call_3966))) # shape=(2, 6, 9)
bop_3977 = relay.less_equal(call_3967.astype('bool'), relay.reshape(call_3955.astype('bool'), relay.shape_of(call_3967))) # shape=(2, 6, 9)
output = relay.Tuple([call_3970,bop_3974,])
output2 = relay.Tuple([call_3971,bop_3977,])
func_3981 = relay.Function([], output)
mod['func_3981'] = func_3981
mod = relay.transform.InferType()(mod)
mutated_mod['func_3981'] = func_3981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3981_call = mutated_mod.get_global_var('func_3981')
call_3982 = func_3981_call()
output = call_3982
func_3983 = relay.Function([], output)
mutated_mod['func_3983'] = func_3983
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3171_call = mod.get_global_var('func_3171')
func_3172_call = mutated_mod.get_global_var('func_3172')
call_4015 = relay.TupleGetItem(func_3171_call(), 0)
call_4016 = relay.TupleGetItem(func_3172_call(), 0)
func_1963_call = mod.get_global_var('func_1963')
func_1965_call = mutated_mod.get_global_var('func_1965')
call_4039 = func_1963_call()
call_4040 = func_1963_call()
bop_4041 = relay.bitwise_xor(call_4039.astype('uint64'), relay.reshape(call_4015.astype('uint64'), relay.shape_of(call_4039))) # shape=(2, 6, 9)
bop_4044 = relay.bitwise_xor(call_4040.astype('uint64'), relay.reshape(call_4016.astype('uint64'), relay.shape_of(call_4040))) # shape=(2, 6, 9)
output = bop_4041
output2 = bop_4044
func_4055 = relay.Function([], output)
mod['func_4055'] = func_4055
mod = relay.transform.InferType()(mod)
output = func_4055()
func_4056 = relay.Function([], output)
mutated_mod['func_4056'] = func_4056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2925_call = mod.get_global_var('func_2925')
func_2927_call = mutated_mod.get_global_var('func_2927')
call_4095 = func_2925_call()
call_4096 = func_2925_call()
var_4104 = relay.var("var_4104", dtype = "float32", shape = (700,))#candidate|4104|(700,)|var|float32
bop_4105 = relay.mod(call_4095.astype('float32'), relay.reshape(var_4104.astype('float32'), relay.shape_of(call_4095))) # shape=(700,)
bop_4108 = relay.mod(call_4096.astype('float32'), relay.reshape(var_4104.astype('float32'), relay.shape_of(call_4096))) # shape=(700,)
uop_4109 = relay.tan(bop_4105.astype('float64')) # shape=(700,)
uop_4111 = relay.tan(bop_4108.astype('float64')) # shape=(700,)
output = relay.Tuple([uop_4109,])
output2 = relay.Tuple([uop_4111,])
func_4115 = relay.Function([var_4104,], output)
mod['func_4115'] = func_4115
mod = relay.transform.InferType()(mod)
var_4116 = relay.var("var_4116", dtype = "float32", shape = (700,))#candidate|4116|(700,)|var|float32
output = func_4115(var_4116)
func_4117 = relay.Function([var_4116], output)
mutated_mod['func_4117'] = func_4117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2946_call = mod.get_global_var('func_2946')
func_2947_call = mutated_mod.get_global_var('func_2947')
call_4146 = func_2946_call()
call_4147 = func_2946_call()
var_4168 = relay.var("var_4168", dtype = "float64", shape = (2, 6, 9))#candidate|4168|(2, 6, 9)|var|float64
bop_4169 = relay.equal(call_4146.astype('bool'), relay.reshape(var_4168.astype('bool'), relay.shape_of(call_4146))) # shape=(2, 6, 9)
bop_4172 = relay.equal(call_4147.astype('bool'), relay.reshape(var_4168.astype('bool'), relay.shape_of(call_4147))) # shape=(2, 6, 9)
func_2874_call = mod.get_global_var('func_2874')
func_2876_call = mutated_mod.get_global_var('func_2876')
const_4176 = relay.const([[6,-5,2,5,-7,7,9,2,-8,-10,4,-8,3,-5,-1,-7,-4,6,-10,-5,7,3,-3,-7,1,1,9,-10,-9,5,7,-7,-6,-6,-5,3,3,9,-2,9,4,-9,-1,5,5,10,-4,4,1,4,10,-9,5,3,4,1,3,-1,10,-4,6,6,2,-7,9,-10,-1,6,-9,-3,2,-1,3,-1,5,-7,-9,2,4,-4,-3,4,5,3,-10,7,10,8,7,10,7,5,-2,-7,8,-1,-8,-6,6,7,6,1,1,3,1,1,1,-3,-3,-1,-6,2,7,8,-9,-1,-10,-5,4,-10,1,2,-7,7,9,-3,-2,8,-4,3,3,10,-10,4,-3,8,6,-8,-7,5],[6,-1,-2,6,-7,-1,6,-4,8,-10,-4,7,-10,-5,1,-5,7,-3,-8,6,1,6,1,-4,1,2,-4,-7,5,1,3,2,3,10,-8,7,-6,-7,-4,-7,-4,-10,1,3,3,-1,2,-8,-3,-6,-5,-8,-5,-7,5,4,7,8,-3,-2,-6,3,-8,-1,-9,2,10,-2,-7,4,5,1,-3,-7,-1,5,4,5,10,7,-5,-1,10,-9,-4,-7,2,2,1,2,-10,1,-6,10,-4,-3,-3,-3,-2,10,-5,9,-8,-3,-10,-3,1,-6,2,-10,10,-5,-2,8,9,1,6,3,1,-3,8,-1,9,5,5,8,-3,-10,1,10,-7,-6,-3,7,5,-4,5,4,-5,7],[-6,-5,8,-5,-7,-9,-8,-9,3,4,5,3,-3,6,-5,8,-6,4,2,2,-6,8,-5,-4,3,8,-6,-10,7,-7,-8,8,1,9,3,5,-4,5,7,10,9,-2,1,4,-9,-4,5,3,6,-9,5,8,6,7,-3,5,-6,-7,-10,-7,-1,6,-3,-1,-2,7,6,-5,9,6,-10,5,10,5,4,-1,-2,-10,7,-5,-4,4,-6,-2,10,8,-3,-8,-7,-4,-4,4,3,3,7,-7,-10,5,-2,2,7,4,5,2,4,2,3,5,4,-4,-8,4,-5,-6,7,7,-10,-3,-2,8,5,3,8,1,-8,2,7,-5,-6,7,3,-7,-6,9,-9,3,6,9,-6,7],[5,-3,7,5,1,7,8,6,-6,4,-1,-9,-5,-3,9,6,-9,-8,-6,-10,-9,-10,10,-2,10,-4,-3,10,-1,10,4,8,4,10,1,9,-6,6,5,-4,6,-8,1,6,2,6,1,-9,-9,6,-8,1,-6,-10,7,-7,-2,-1,-6,6,4,-4,-5,-3,-4,6,6,4,6,-4,-7,-7,8,1,6,2,1,-6,-2,1,-8,6,8,-7,-5,9,-1,-1,4,-3,-1,-10,-4,9,7,-10,10,-10,-7,3,5,-5,6,-5,10,-1,-4,5,9,-4,5,1,1,4,-8,1,6,-10,-2,5,3,-4,8,7,-1,-4,-4,-4,6,-4,-4,10,2,4,-4,-7,4,-8,-9,10],[5,-8,8,-5,-9,-1,-7,-5,-10,3,8,5,-9,6,5,8,9,10,-10,-2,-5,4,-3,-8,-7,-8,-1,9,-3,10,1,1,-5,-7,-5,6,5,9,6,-2,-10,-8,-3,-5,-3,6,2,-8,-8,4,6,-1,-9,-9,-10,9,-1,-5,7,-1,-2,6,4,-4,1,-6,-9,9,9,-4,9,3,2,4,-5,-10,4,2,2,-10,4,-1,5,3,-8,-5,10,-10,-3,2,1,-4,1,-3,-1,-5,1,10,-6,1,9,4,3,6,8,5,-1,4,-6,5,2,-4,8,10,-6,9,-9,9,-6,-10,-2,-4,4,6,-5,-7,3,-1,-5,6,-3,9,7,-4,2,7,-8,10,9,4],[-9,2,-10,2,7,7,2,-2,5,-3,-1,-2,3,5,-9,7,-9,7,-5,7,8,2,1,8,1,2,4,-4,-9,9,7,-4,-9,6,-2,4,8,-10,9,4,1,-3,-3,2,-6,-7,-8,-1,-4,9,-9,-7,-10,-5,-7,10,-4,-3,-9,-6,5,-10,-6,8,-8,-7,-1,-6,-3,9,-10,6,-1,1,-3,7,-2,-8,7,-10,4,-4,4,-7,10,5,-4,-4,-1,7,5,1,-10,-8,7,-4,5,-10,-9,-6,-3,-9,-3,4,-9,7,4,1,-6,-2,7,8,5,3,-4,-5,9,6,8,-3,10,2,7,-7,-4,-8,5,5,3,-6,-6,-6,4,6,-3,-10,10,-6,-5,9],[-1,2,-4,-8,6,6,4,8,3,9,-4,8,2,8,6,-9,-6,-5,-10,7,-6,10,4,-7,2,4,6,8,5,-7,7,10,-7,-4,-7,-2,6,10,-10,7,-4,7,-3,7,-5,3,-10,-5,-9,3,2,8,7,-7,6,8,7,9,4,-9,10,-9,6,-7,-3,-10,8,-2,-7,-2,3,2,-7,9,9,-10,-2,9,-5,5,-9,-4,5,9,-2,-7,-3,4,-10,-3,3,-7,-4,-4,-5,8,6,-8,-5,4,-10,-4,-10,6,3,10,-3,-2,-3,8,7,-1,-6,-3,8,2,-6,2,7,7,-7,6,4,-9,-4,7,2,4,9,-1,-5,-4,1,9,5,-6,1,-4,-9,3],[1,5,-10,-3,6,-3,-9,4,-6,-6,8,-3,5,5,-2,7,8,9,3,-4,-6,-2,7,-4,8,4,-3,5,6,-10,-8,-4,-1,4,-4,2,9,-6,-1,-9,-2,5,10,1,-1,4,10,-8,2,-2,2,6,-10,-8,-5,-2,-10,10,8,-7,6,10,1,4,10,8,4,5,-10,-6,4,2,4,5,7,1,-3,-7,9,-6,1,-2,1,10,-4,6,4,-1,2,-10,-8,-10,4,-5,-1,1,-6,7,-2,-1,-3,2,5,-8,1,-5,1,-10,-3,5,8,3,8,-3,9,7,-1,1,-4,2,-9,4,2,-4,-3,-6,6,6,1,6,-3,4,-2,9,-6,-1,8,6,3,3]], dtype = "uint8")#candidate|4176|(8, 140)|const|uint8
call_4175 = relay.TupleGetItem(func_2874_call(relay.reshape(const_4176.astype('uint8'), [560, 2])), 2)
call_4177 = relay.TupleGetItem(func_2876_call(relay.reshape(const_4176.astype('uint8'), [560, 2])), 2)
var_4178 = relay.var("var_4178", dtype = "uint8", shape = (8, 140))#candidate|4178|(8, 140)|var|uint8
bop_4179 = relay.bitwise_or(const_4176.astype('uint16'), relay.reshape(var_4178.astype('uint16'), relay.shape_of(const_4176))) # shape=(8, 140)
func_487_call = mod.get_global_var('func_487')
func_490_call = mutated_mod.get_global_var('func_490')
call_4191 = relay.TupleGetItem(func_487_call(relay.reshape(call_4146.astype('float32'), [2, 6, 9]), relay.reshape(var_4178.astype('uint8'), [1120,]), ), 2)
call_4192 = relay.TupleGetItem(func_490_call(relay.reshape(call_4146.astype('float32'), [2, 6, 9]), relay.reshape(var_4178.astype('uint8'), [1120,]), ), 2)
func_912_call = mod.get_global_var('func_912')
func_914_call = mutated_mod.get_global_var('func_914')
var_4196 = relay.var("var_4196", dtype = "bool", shape = (1092,))#candidate|4196|(1092,)|var|bool
call_4195 = relay.TupleGetItem(func_912_call(relay.reshape(var_4196.astype('bool'), [13, 14, 6])), 0)
call_4197 = relay.TupleGetItem(func_914_call(relay.reshape(var_4196.astype('bool'), [13, 14, 6])), 0)
output = relay.Tuple([bop_4169,call_4175,bop_4179,call_4191,call_4195,var_4196,])
output2 = relay.Tuple([bop_4172,call_4177,bop_4179,call_4192,call_4197,var_4196,])
func_4208 = relay.Function([var_4168,var_4178,var_4196,], output)
mod['func_4208'] = func_4208
mod = relay.transform.InferType()(mod)
var_4209 = relay.var("var_4209", dtype = "float64", shape = (2, 6, 9))#candidate|4209|(2, 6, 9)|var|float64
var_4210 = relay.var("var_4210", dtype = "uint8", shape = (8, 140))#candidate|4210|(8, 140)|var|uint8
var_4211 = relay.var("var_4211", dtype = "bool", shape = (1092,))#candidate|4211|(1092,)|var|bool
output = func_4208(var_4209,var_4210,var_4211,)
func_4212 = relay.Function([var_4209,var_4210,var_4211,], output)
mutated_mod['func_4212'] = func_4212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_900_call = mod.get_global_var('func_900')
func_902_call = mutated_mod.get_global_var('func_902')
call_4218 = relay.TupleGetItem(func_900_call(), 0)
call_4219 = relay.TupleGetItem(func_902_call(), 0)
output = call_4218
output2 = call_4219
func_4228 = relay.Function([], output)
mod['func_4228'] = func_4228
mod = relay.transform.InferType()(mod)
output = func_4228()
func_4229 = relay.Function([], output)
mutated_mod['func_4229'] = func_4229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1258_call = mod.get_global_var('func_1258')
func_1259_call = mutated_mod.get_global_var('func_1259')
call_4264 = relay.TupleGetItem(func_1258_call(), 0)
call_4265 = relay.TupleGetItem(func_1259_call(), 0)
func_2311_call = mod.get_global_var('func_2311')
func_2312_call = mutated_mod.get_global_var('func_2312')
call_4281 = relay.TupleGetItem(func_2311_call(), 0)
call_4282 = relay.TupleGetItem(func_2312_call(), 0)
func_487_call = mod.get_global_var('func_487')
func_490_call = mutated_mod.get_global_var('func_490')
var_4288 = relay.var("var_4288", dtype = "uint8", shape = (1120,))#candidate|4288|(1120,)|var|uint8
call_4287 = relay.TupleGetItem(func_487_call(relay.reshape(call_4264.astype('float32'), [2, 6, 9]), relay.reshape(var_4288.astype('uint8'), [1120,]), ), 2)
call_4289 = relay.TupleGetItem(func_490_call(relay.reshape(call_4264.astype('float32'), [2, 6, 9]), relay.reshape(var_4288.astype('uint8'), [1120,]), ), 2)
output = relay.Tuple([call_4264,call_4281,call_4287,var_4288,])
output2 = relay.Tuple([call_4265,call_4282,call_4289,var_4288,])
func_4295 = relay.Function([var_4288,], output)
mod['func_4295'] = func_4295
mod = relay.transform.InferType()(mod)
mutated_mod['func_4295'] = func_4295
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4296 = relay.var("var_4296", dtype = "uint8", shape = (1120,))#candidate|4296|(1120,)|var|uint8
func_4295_call = mutated_mod.get_global_var('func_4295')
call_4297 = func_4295_call(var_4296)
output = call_4297
func_4298 = relay.Function([var_4296], output)
mutated_mod['func_4298'] = func_4298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3041_call = mod.get_global_var('func_3041')
func_3043_call = mutated_mod.get_global_var('func_3043')
call_4302 = relay.TupleGetItem(func_3041_call(), 0)
call_4303 = relay.TupleGetItem(func_3043_call(), 0)
func_3111_call = mod.get_global_var('func_3111')
func_3112_call = mutated_mod.get_global_var('func_3112')
call_4312 = relay.TupleGetItem(func_3111_call(), 0)
call_4313 = relay.TupleGetItem(func_3112_call(), 0)
output = relay.Tuple([call_4302,call_4312,])
output2 = relay.Tuple([call_4303,call_4313,])
func_4314 = relay.Function([], output)
mod['func_4314'] = func_4314
mod = relay.transform.InferType()(mod)
mutated_mod['func_4314'] = func_4314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4314_call = mutated_mod.get_global_var('func_4314')
call_4315 = func_4314_call()
output = call_4315
func_4316 = relay.Function([], output)
mutated_mod['func_4316'] = func_4316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3398_call = mod.get_global_var('func_3398')
func_3400_call = mutated_mod.get_global_var('func_3400')
call_4370 = relay.TupleGetItem(func_3398_call(), 0)
call_4371 = relay.TupleGetItem(func_3400_call(), 0)
output = call_4370
output2 = call_4371
func_4378 = relay.Function([], output)
mod['func_4378'] = func_4378
mod = relay.transform.InferType()(mod)
mutated_mod['func_4378'] = func_4378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4378_call = mutated_mod.get_global_var('func_4378')
call_4379 = func_4378_call()
output = call_4379
func_4380 = relay.Function([], output)
mutated_mod['func_4380'] = func_4380
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4424 = relay.var("var_4424", dtype = "int16", shape = (1, 6, 3))#candidate|4424|(1, 6, 3)|var|int16
var_4425 = relay.var("var_4425", dtype = "int16", shape = (13, 6, 3))#candidate|4425|(13, 6, 3)|var|int16
bop_4426 = relay.bitwise_xor(var_4424.astype('int16'), var_4425.astype('int16')) # shape=(13, 6, 3)
uop_4435 = relay.exp(var_4424.astype('float64')) # shape=(1, 6, 3)
output = relay.Tuple([bop_4426,uop_4435,])
output2 = relay.Tuple([bop_4426,uop_4435,])
func_4442 = relay.Function([var_4424,var_4425,], output)
mod['func_4442'] = func_4442
mod = relay.transform.InferType()(mod)
var_4443 = relay.var("var_4443", dtype = "int16", shape = (1, 6, 3))#candidate|4443|(1, 6, 3)|var|int16
var_4444 = relay.var("var_4444", dtype = "int16", shape = (13, 6, 3))#candidate|4444|(13, 6, 3)|var|int16
output = func_4442(var_4443,var_4444,)
func_4445 = relay.Function([var_4443,var_4444,], output)
mutated_mod['func_4445'] = func_4445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3171_call = mod.get_global_var('func_3171')
func_3172_call = mutated_mod.get_global_var('func_3172')
call_4516 = relay.TupleGetItem(func_3171_call(), 0)
call_4517 = relay.TupleGetItem(func_3172_call(), 0)
uop_4518 = relay.sigmoid(call_4516.astype('float32')) # shape=(2, 6, 9)
uop_4520 = relay.sigmoid(call_4517.astype('float32')) # shape=(2, 6, 9)
output = relay.Tuple([uop_4518,])
output2 = relay.Tuple([uop_4520,])
func_4521 = relay.Function([], output)
mod['func_4521'] = func_4521
mod = relay.transform.InferType()(mod)
output = func_4521()
func_4522 = relay.Function([], output)
mutated_mod['func_4522'] = func_4522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4378_call = mod.get_global_var('func_4378')
func_4380_call = mutated_mod.get_global_var('func_4380')
call_4525 = func_4378_call()
call_4526 = func_4378_call()
output = relay.Tuple([call_4525,])
output2 = relay.Tuple([call_4526,])
func_4529 = relay.Function([], output)
mod['func_4529'] = func_4529
mod = relay.transform.InferType()(mod)
output = func_4529()
func_4530 = relay.Function([], output)
mutated_mod['func_4530'] = func_4530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3809_call = mod.get_global_var('func_3809')
func_3810_call = mutated_mod.get_global_var('func_3810')
call_4559 = relay.TupleGetItem(func_3809_call(), 1)
call_4560 = relay.TupleGetItem(func_3810_call(), 1)
func_571_call = mod.get_global_var('func_571')
func_576_call = mutated_mod.get_global_var('func_576')
var_4570 = relay.var("var_4570", dtype = "uint8", shape = (1120,))#candidate|4570|(1120,)|var|uint8
call_4569 = relay.TupleGetItem(func_571_call(relay.reshape(call_4559.astype('float64'), [2, 6, 9]), relay.reshape(call_4559.astype('float64'), [2, 6, 9]), relay.reshape(var_4570.astype('uint8'), [4, 280]), ), 0)
call_4571 = relay.TupleGetItem(func_576_call(relay.reshape(call_4559.astype('float64'), [2, 6, 9]), relay.reshape(call_4559.astype('float64'), [2, 6, 9]), relay.reshape(var_4570.astype('uint8'), [4, 280]), ), 0)
func_1963_call = mod.get_global_var('func_1963')
func_1965_call = mutated_mod.get_global_var('func_1965')
call_4588 = func_1963_call()
call_4589 = func_1963_call()
output = relay.Tuple([call_4559,call_4569,var_4570,call_4588,])
output2 = relay.Tuple([call_4560,call_4571,var_4570,call_4589,])
func_4593 = relay.Function([var_4570,], output)
mod['func_4593'] = func_4593
mod = relay.transform.InferType()(mod)
var_4594 = relay.var("var_4594", dtype = "uint8", shape = (1120,))#candidate|4594|(1120,)|var|uint8
output = func_4593(var_4594)
func_4595 = relay.Function([var_4594], output)
mutated_mod['func_4595'] = func_4595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2825_call = mod.get_global_var('func_2825')
func_2827_call = mutated_mod.get_global_var('func_2827')
call_4634 = func_2825_call()
call_4635 = func_2825_call()
func_4295_call = mod.get_global_var('func_4295')
func_4298_call = mutated_mod.get_global_var('func_4298')
const_4638 = relay.const([2,1,8,-4,-5,-5,-6,4,2,-3,-9,-6,-6,-3,-6,-1,-10,10,2,-2,-1,-3,-9,8,4,10,4,10,-4,-5,3,1,-8,-3,7,9,-2,4,-9,3,-6,7,-1,-9,1,-7,10,10,-1,10,8,-3,-2,-4,-1,-4,-1,4,9,-9,7,-5,-6,-7,-9,4,-6,10,3,-7,-2,-9,4,-7,9,1,3,-7,2,5,-10,-1,-5,-4,-6,3,4,2,-9,10,6,6,-9,8,6,3,4,2,-4,10,-7,-9,-6,10,-10,5,-2,-5,1,-2,-9,-3,-10,2,3,-5,6,-3,5,-10,-4,10,6,-4,-1,4,-3,4,-5,-1,-10,-9,10,-9,-7,-9,5,-6,-7,6,9,7,-10,-7,-7,1,5,-4,-6,-10,-5,4,10,-9,-10,-4,-6,3,2,-10,10,-8,3,-10,8,-4,10,-1,9,7,6,10,-2,9,-5,-7,-2,10,9,-6,1,-2,-9,-9,-4,10,8,5,5,6,-4,-4,9,2,3,7,-10,-5,1,-9,-2,6,-3,10,4,9,-10,-4,7,7,4,6,-2,-4,6,-9,-6,-8,7,-8,-5,-8,-10,-2,-6,10,2,5,8,-10,-7,-3,-3,4,9,10,9,-7,-10,-9,-9,-10,7,-6,7,1,4,-6,5,8,2,-5,5,1,2,-6,10,-1,-1,4,-2,3,9,4,9,-5,9,-3,4,4,5,9,3,-2,9,-2,9,9,-5,9,5,9,5,-10,8,-9,1,-6,-7,9,-2,-7,8,-8,-8,-9,2,9,-9,-10,-5,8,4,2,-2,-7,4,7,9,5,4,-2,-1,6,10,-5,-5,-10,-8,-10,5,-9,3,-3,3,10,1,6,3,-9,9,7,-8,-3,-1,-1,4,9,5,-8,9,8,9,1,-9,4,-6,-2,-10,-3,1,1,-3,1,-10,6,8,-7,-7,9,-9,-4,4,1,4,-6,9,10,-8,8,1,-5,-8,-8,-3,3,-1,-8,4,10,-3,-2,-6,4,5,-1,-6,7,-1,10,-3,-5,-1,-9,2,4,-8,10,1,7,6,4,4,-7,-6,8,-2,-2,-6,8,10,3,-8,-3,7,-5,-8,4,-10,-7,-9,-6,8,4,10,-1,-3,10,9,2,-3,-8,8,3,6,6,4,6,1,7,-1,-4,5,10,9,-2,1,-5,6,6,-9,7,4,7,-3,-9,-5,1,-8,5,-2,-2,-9,-1,5,4,8,9,-5,9,3,2,-10,-5,1,8,7,6,6,-8,3,-7,5,6,2,-6,3,2,-9,2,9,5,9,-1,-7,8,-4,4,8,-7,-5,-7,1,10,8,-3,-5,2,-10,-10,5,8,10,-7,3,-3,9,5,-1,1,10,-6,-2,8,3,-10,8,8,-1,-8,-10,-1,3,2,-2,3,9,-8,10,-5,-5,-1,-3,1,-5,8,-2,-8,-8,10,3,3,-5,-3,6,9,-2,-4,-1,-9,-4,4,10,2,2,10,-7,7,4,8,9,3,8,-6,-10,7,-4,1,-3,-3,-7,2,6,8,1,-1,-3,-2,10,2,-3,-8,-2,-2,-4,-1,8,6,3,7,10,-6,2,6,4,-4,10,5,-2,8,1,-8,-3,6,-6,3,9,-1,-5,-5,-8,7,2,10,8,10,7,10,-10,-7,-9,6,-10,-9,5,-6,-4,3,-7,-9,-8,4,-7,-7,-3,7,7,-10,-10,1,-4,10,-10,-3,5,1,9,1,4,-4,4,-8,5,-7,-8,2,-5,-9,7,-3,-4,-8,-2,10,8,-4,5,3,-10,5,-1,10,-1,-3,3,-1,-2,9,-9,-1,-2,9,-5,-5,5,2,7,1,3,6,-2,10,-7,8,-9,-3,2,-8,4,-3,-5,4,9,2,1,-5,-7,7,-7,10,-1,-6,-4,-1,2,-9,1,1,-1,1,2,-7,2,-5,-6,-4,9,-2,-6,3,-9,5,6,-9,8,10,-7,-1,8,7,-10,-3,-2,-1,-7,4,-7,-7,4,1,-5,4,-8,10,-8,10,-9,6,-7,10,1,2,-5,-10,-5,1,-2,2,7,-5,-1,4,9,3,-6,10,1,7,2,-4,-8,7,-9,7,-2,-2,9,-5,3,2,5,1,7,9,-5,6,-8,-3,-1,3,-5,6,-9,10,-1,5,8,9,4,-5,-2,4,4,-5,2,-8,-2,-10,-9,5,5,-5,6,8,-3,10,-4,5,6,2,-7,4,9,2,-4,-8,-5,-4,9,2,5,-7,-8,8,2,9,-2,-3,-7,-1,-10,-2,1,7,-7,2,-10,-4,3,10,2,9,4,-9,4,4,8,-10,-1,9,-5,4,1,-4,8,2,-5,7,10,2,3,-10,3,10,-7,6,9,7,-7,-4,5,6,4,1,7,-10,3,-3,-9,2,1,8,-5,-8,4,-9,8,10,9,8,9,10,9,6,-6,4,6,5,-4,6,-7,-8,-10,-8,4,-7,-5,2,-10,-2,9,-4,-5,-6,4,-9,-5,-5,-9,-4,-1,3,9,2,6,-6,9,9,8,6,-5,2,-4,-7,-2,-6,-3,8,4,1,-3,4,6,-9,9,6,-2,6,-7,-1,-5,3,3,7,-1,-9,5,10,7,6,7,-1,-10,5,1,8,2,-1,-3,2,7,10,-7,3,-2,-9,1,-7,9,2,-9,-4,-2,-6,3,10,-1,6,-5,-1,8,-5,10,-1,6,-8,4,6,7,4,1,-2,8,-8,6,7,9,-6,6,9,1,-6,7,4,5,-4,3,7,-5,-4,6,9,-5,-6,2,-2,-3,1,-2,6,4,4,-7,1,-7,4,-8,9,-8,6,-2,-5,9,-7,-1,-10,2,-4,-6,10,10,9,9,-3,4,-6,-10,-1,5,1,10,2,-7,8,1,-9,4,-3,7,-7,-5,-7,-4,-3,-8,-6,6,-8,-6,8,-4,10,-6,-8,-9,4,-10,1,1,4], dtype = "uint8")#candidate|4638|(1120,)|const|uint8
call_4637 = relay.TupleGetItem(func_4295_call(relay.reshape(const_4638.astype('uint8'), [1120,])), 0)
call_4639 = relay.TupleGetItem(func_4298_call(relay.reshape(const_4638.astype('uint8'), [1120,])), 0)
output = relay.Tuple([call_4634,call_4637,const_4638,])
output2 = relay.Tuple([call_4635,call_4639,const_4638,])
func_4648 = relay.Function([], output)
mod['func_4648'] = func_4648
mod = relay.transform.InferType()(mod)
mutated_mod['func_4648'] = func_4648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4648_call = mutated_mod.get_global_var('func_4648')
call_4649 = func_4648_call()
output = call_4649
func_4650 = relay.Function([], output)
mutated_mod['func_4650'] = func_4650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4521_call = mod.get_global_var('func_4521')
func_4522_call = mutated_mod.get_global_var('func_4522')
call_4667 = relay.TupleGetItem(func_4521_call(), 0)
call_4668 = relay.TupleGetItem(func_4522_call(), 0)
output = relay.Tuple([call_4667,])
output2 = relay.Tuple([call_4668,])
func_4671 = relay.Function([], output)
mod['func_4671'] = func_4671
mod = relay.transform.InferType()(mod)
output = func_4671()
func_4672 = relay.Function([], output)
mutated_mod['func_4672'] = func_4672
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4378_call = mod.get_global_var('func_4378')
func_4380_call = mutated_mod.get_global_var('func_4380')
call_4707 = func_4378_call()
call_4708 = func_4378_call()
output = relay.Tuple([call_4707,])
output2 = relay.Tuple([call_4708,])
func_4714 = relay.Function([], output)
mod['func_4714'] = func_4714
mod = relay.transform.InferType()(mod)
mutated_mod['func_4714'] = func_4714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4714_call = mutated_mod.get_global_var('func_4714')
call_4715 = func_4714_call()
output = call_4715
func_4716 = relay.Function([], output)
mutated_mod['func_4716'] = func_4716
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4748 = relay.var("var_4748", dtype = "float64", shape = (5, 3))#candidate|4748|(5, 3)|var|float64
uop_4749 = relay.sin(var_4748.astype('float64')) # shape=(5, 3)
func_2435_call = mod.get_global_var('func_2435')
func_2437_call = mutated_mod.get_global_var('func_2437')
call_4753 = relay.TupleGetItem(func_2435_call(), 0)
call_4754 = relay.TupleGetItem(func_2437_call(), 0)
func_4378_call = mod.get_global_var('func_4378')
func_4380_call = mutated_mod.get_global_var('func_4380')
call_4755 = func_4378_call()
call_4756 = func_4378_call()
func_2340_call = mod.get_global_var('func_2340')
func_2343_call = mutated_mod.get_global_var('func_2343')
const_4758 = relay.const([-6.739729,-1.139353,-4.638528,-1.808860,8.878994,-9.673565,-5.524087,6.426603,-4.102718,-1.581066,-6.046321,-4.813928,9.965448,4.620473,-5.764533,4.482975,-9.870778,-8.719904,-6.396254,-5.673862,-1.691620,-3.827226,-7.449676,5.165868,7.020779,3.370200,7.271114,6.829430,3.522551,-9.957581,2.592393,-0.790763,9.079591,9.782671,9.170328,4.506568,-6.389772,-4.785569,-5.940515,2.165915,0.366438,3.667307,3.007354,-1.873307,-1.176605,-7.389958,-3.032089,9.849807,2.270098,-9.513189,-3.029435,-1.275595,5.170874,5.711078,-8.711091,-4.984639,4.354157,2.429935,-9.385563,-4.116068,-8.843259,-4.679524,1.495009,-3.442031,-0.327201,-6.014981,3.844214,7.579770,2.074380,-3.780956,-7.519162,-1.401867,-2.397105,-0.175007,7.079175,0.622192,9.640333,-8.753593,4.869680,5.586747,7.072372,1.991048,-3.654861,-2.450742,4.102425,-9.794536,5.724382,-0.690463,-4.452322,-8.678902,6.763587,4.776915,0.519711,7.094409,-5.924416,8.788616,-7.978866,-4.999164,6.619759,3.631295,5.102308,-5.383787,-9.237711,3.518791,9.971892,-1.888585,5.029081,5.786440,1.517310,-0.549112,1.896370,-3.114889,-7.207281,0.073301,1.939659,-0.455026,-2.136093,6.809481,5.456496,3.384383,-5.206179,7.891559,9.648131,-0.886146,-2.959242,-5.603840,-5.736306,4.795318,-5.734075,1.902723,2.843984,-8.864671,-7.813949,-6.200156,-2.478829,3.909313,8.305169,1.664817,3.861319,-0.423028,-2.985579,-9.291580,2.942310,1.311221,-2.429596,8.886887,-0.564966,4.856767,6.279615,9.050273,0.299070,-9.518066,9.979222,7.569527,4.666469,-3.316727,-9.288191,1.062499,8.126300,2.968407,9.651854,1.432217,2.582275,-4.038871,4.456092,-3.018163,-7.389014,9.696002,-1.132020,9.320121,-6.709976,6.956399,-6.011954,-9.682575,6.501257,1.467117,-5.643141,2.658860,1.556500,-7.163293,1.651697,1.101174,7.953404,1.613606,7.623179,-3.203064,4.448930,-4.997470,-9.789034,3.321567,1.794602,-0.256185,0.604333,4.234475,3.832321,2.640580,-0.347753,0.127574,-8.714213,-8.866375,0.281825,1.386887,-7.026054,-3.024837,1.140906,0.130153,-4.151607,-7.429787,5.169376,-8.309985,-0.583193,6.887332,-7.312608,-8.514179,7.374424,-7.261374,4.835602,7.019017,6.087337,-6.066703,0.577233,4.672432,8.397888,-2.926368,5.751576,-5.668302,-1.901166,1.396954,-2.793148,4.775722,-0.050512,-4.172795,-9.438412,0.112360,9.181117,-4.210513,4.273482,-3.254403,1.581538,4.315887,6.552163,-2.680073,6.171451,-8.208638,-9.332778,-1.598957,0.448194,-4.856319,-2.376255,4.880649,-7.412632,2.230464,-4.783401,-5.368681,-8.596879,-4.318153,6.344697,9.158825,-8.739808,-2.658573,-6.834047,9.475411,8.250297,2.901164,-0.706900,7.152820,-8.235556,-8.001956,-2.061932,-2.821106,9.091687,-4.532917,-7.388734,7.755065,4.473703,6.534037,-3.286092,9.893643,-3.860767,-6.872866,-5.274478,4.830014,-0.150170,7.293102,4.459327,1.020095,-0.210760,4.310673,1.336635,-4.273533,1.761707,-0.325753,-9.310095,9.916694,-7.930252,2.709892,-0.681600,4.695434,6.239590,9.256033,0.852540,7.220123,9.142491,-0.828638,5.415888,4.165142,-6.410862,6.320308,-0.312674,5.366737,-8.755018,0.831144,-4.676902,1.846415,7.351462,-6.732578,5.707131,-8.181450,-5.714969,9.004035,1.215724,-4.451567,5.102470,9.721833,7.368261,-0.186405,4.742646,-3.506099,7.076057,0.109468,-1.487253,7.544501,9.583938,-9.016151,-0.195211,-6.492741,7.268195,4.081388,-3.289665,-4.237257,9.428076,8.094758,-1.039120,-8.039473,3.670627,-9.804308,6.838765,7.338697,1.845178,6.274380,5.831880,-3.045951,-6.407201,7.622036,-4.142077,-1.675841,7.691269,-5.788141,2.285940,3.377683,0.859461,5.654235,9.589590,3.297305,-8.501440,-9.393187,-5.910996,-2.692464,-3.862027,5.538838,4.700291,-8.368904,9.599291,-1.570404,-6.053601,8.345808,8.907553,-6.274845,0.618631,-0.952906,-8.009770,-5.044585,3.666556,-7.700216,-3.140245,-7.522116,6.044718,-7.339741,8.986792,-4.942005,-5.491722,7.308615,-9.053261,-3.208468,-3.625276,3.347378,0.870410,3.864654,7.735426,-8.663846,-8.403381,3.384712,-8.898409,-2.418351,8.052419,3.838227,2.204217,5.532229,-9.034700,1.414728,-0.848971,-5.416100,-2.974491,-7.913697,8.837490,-3.742882,1.314628,3.355397,3.116364,-6.581399,-4.380141,6.811281,-2.472745,3.462221,-8.175526,0.404890,-6.046294,5.844765,-9.115396,-3.612177,-4.168205,2.186175,-8.381303,0.259921,-1.090245,-3.359529,3.284741,-2.622597,2.297309,5.450603,2.367971,-2.397643,-4.600211,-6.565895,-8.011111,-8.883688,9.895459,-1.748684,-0.074717,-8.643464,3.489335,-3.943359,-3.291040,3.988077,-0.549214,6.833318,2.147517,6.765021,5.892288,-6.024637,-0.672957,1.503952,-5.762756,-6.362238,1.809708,-2.847412,4.403785,-5.638549,7.935074,6.565035,-0.993038,1.266016,4.895818,8.042109,0.592607,-6.405397,-2.925196,6.790340,4.252679,7.657068,-0.589682,-1.302021,-3.399453,1.715268,-9.606507,-0.244552,-3.211865,-7.270529,-0.098608,-9.912696,-7.985592,-8.953850,-9.472868,3.827112,9.641689,3.385022,-0.106615,8.449671,-2.213820,8.122230,-4.543065,1.538755,8.581426,-3.741536,2.047365,9.604436,8.538247,-0.156546,-5.471792,6.677332,-9.861162,3.113965,-1.601323,-8.073709,-7.179591,1.162926,5.490630,7.748214,6.553871,-6.561827,-0.179094,-7.583044,0.638011,-9.101126,-7.297045,4.280682,-1.166884,-9.849593,-5.325715,4.018422,-5.107410,4.854229,0.060855,-1.585979,-9.505042,5.716630,8.984136,-2.524615,-0.798950,-9.965890,-4.725184,5.414778,-7.555022,-7.318556,-7.436334,4.994087,-3.690402,-2.296561,5.323713,-3.781288,-7.881701,1.410278,3.820784,-5.195600,-2.996490,7.411262,6.564607,4.712112,-2.104034,-5.574835,1.856947,5.473306,-7.346201,8.816599,-1.426229,7.245698,9.635236,-3.217626,-5.261684,-1.434651,2.273044,1.466277,-7.731001,4.930189,-3.777411,-4.492049,9.518865,-7.535086,7.797511,-5.333709,4.364758,-8.802916,-7.961242,-1.587639,-2.407807,7.809189,-0.216011,-1.148516,7.691146,7.031108,2.653783,7.182504,3.745944,-8.074758,6.613292,-8.472759,-8.941060,8.982638,-4.879066,9.187072,-3.686829,-0.778874,7.512346,3.241858,-2.071007,3.150783,-3.856584,3.308934,-9.227524,5.721933,-4.393409,-1.584358,-8.966124,6.291950,0.672052,6.492136,1.315223,-4.332424,-8.394502,0.615822,-6.916305,-1.479856,0.994489,-7.630824,4.627001,6.653802,-3.219933,-9.365560,1.305864,8.414421,-0.905018,-1.206601,-9.558217,8.768317,-8.223246,-6.868916,6.007310,-6.906436,-5.105791,-0.871664,-4.597936,9.991928,8.959466,2.232495,7.162490,-9.672313,-7.025009,8.816188,5.112348,7.450178,5.784477,6.663779,2.550943,3.963826,-3.744214,4.588963,4.844563,7.453136,4.581711,9.833107,5.222709,-0.677104,-8.349399,7.345667,-5.581895,1.374002,-6.969058,-7.876350,-0.706734,6.272328,9.844280,9.604679,0.904334,-9.821758,-3.681098,2.536900,2.419620,3.417686,0.857945,5.307872,8.844008,9.663369,2.431704,3.133891,2.706973,3.955037,-7.341196,1.342273,7.392851,-8.397953,0.734374,-4.852464,4.384716,-7.774515,-1.191280,3.556678,-7.749928,6.951759,-6.369786,-8.525762,3.387874,5.208951,-7.215417,8.822930,-2.647526,2.116922,0.892974,-2.630618,5.405404,9.451160,-0.412550,-4.901945,0.067257,6.118363,-5.054161,3.058180,3.493367,7.337977,6.022416,7.128806,-7.838271,1.695413,-9.834545,7.199588,-9.379102,4.883184,9.128088,6.240330,5.646594,-6.170950,-0.917972,8.443350,-4.163732,-2.467047,7.727355,5.344952,-4.343775,8.672244,-6.019565,4.901710,3.152864,-5.687246,-7.903139,1.540081,-7.487256,1.532521,8.735046,-1.264343,-3.697688,7.476817,-9.119478,2.507947,8.374380,-3.593589,3.693566,-4.669907,-9.374122,7.048848,1.208830,0.966196,1.559990,-6.377507,2.725635,-5.904694,2.996756,-0.185419,7.410222,6.667272,-5.000006,-9.112770,1.330539,0.862873,1.809262,-4.187378,2.022840,-3.854165,-2.905607,-1.000173,9.752859,0.237138,-3.725676,7.339887,-8.183197,2.630961,-3.552234,-1.990827,-5.601285,5.746555,7.639677,-5.188014,6.698516,2.110561,-3.376723,-9.897948,-7.342577,-5.422080,7.187220,-0.810283,-9.377541,-4.915602,-9.212556,-6.505222,-2.304697,-5.871687,7.045943,5.788757,-5.837443,1.288203,-5.889221,-5.748543,7.467416,0.219732,-0.703982,-5.900833,6.926851,0.228597,-5.860379,5.178604,-6.937973,-8.953541,-1.934647,-1.703251,-6.155403,1.886031,1.955520,5.577522,6.341982,0.936820,4.715161,-4.280236,5.720254,-6.826122,-2.917348,-7.556693,1.468703,-7.553718,-7.277450,-8.595511,-8.192937,7.294044,-3.368688,2.693733,-1.056507,9.000168,-1.792981,-7.449149,-1.169766,6.835041,-5.107056,9.737175,-3.059971,-5.734925,-5.921990,7.568770,-7.109178,8.486689,-9.811741,-6.210615,7.026741,-7.165711,-8.809142,5.012332,8.675813,5.918917,3.908941,5.958799,-7.514270,-0.290259,2.237012,-3.684259,3.851227,-5.981906,-6.184930,-8.163065,-6.603122,9.011387,5.393305,6.057906,-9.223477,5.504040,1.299676,3.430577,-1.959034,3.294602,-0.294978,9.021727,3.527551,7.402167,3.266608,7.524611,-1.989199,-5.899162,-0.341840,-3.545892,-9.851327,-9.724633,-4.681202,2.052482,9.255048,-4.438734,-9.234228,2.531996,3.481610,3.540467,-4.111108,7.532252,-3.585970,1.415889,5.222606,6.898235,2.526833,-4.367689,0.514299,-1.593686,-6.781722,-2.942067,-1.371195,-5.976972,-6.082325,-3.932534,-6.548456,2.183543,3.080458,8.599667,-2.563509,-0.989745,-1.846048,-8.614047,0.077430,1.858101,8.288237,-2.057776,7.728106,-5.771935,3.821381,3.276496,-1.549310,-8.367765,3.050099,-2.645812,-3.028910,7.062390,4.769523,-7.400759,-6.030674,-5.348712,-9.703666,3.010924,0.129123,2.511683,2.348770,5.097502,-4.492112,2.865504,4.479442,5.953411,6.941851,7.018036,-0.800205,1.181475], dtype = "float64")#candidate|4758|(960,)|const|float64
call_4757 = func_2340_call(relay.reshape(const_4758.astype('float64'), [15, 16, 4]))
call_4759 = func_2340_call(relay.reshape(const_4758.astype('float64'), [15, 16, 4]))
func_3939_call = mod.get_global_var('func_3939')
func_3941_call = mutated_mod.get_global_var('func_3941')
const_4761 = relay.const([[5,9,-4,7,-10,4,3,1,-5,5,1,-7,7,6,6,-2,1,1,6,5,-7,7,-2,-1,9,3,4,-5,-4,10,-7,2,-8,3,5,2,-9,-3,5,-8,-9,-4,-4,6,10,-1,10,4,8,-2,5,4,-2,5,-10,2,5,-4,5,-9,8,3,-5,8,2,6,-3,-1,9,2,8,-1,-2,-4,-5,-3,4,10],[2,-3,-7,6,-1,-7,-3,-10,-5,-6,5,3,4,4,-5,-9,4,3,-1,5,6,-4,3,9,-4,4,-4,3,4,-10,-4,5,-1,9,-9,-5,6,-3,-3,6,7,1,6,3,-9,-10,2,-1,6,-2,-4,-2,-6,9,7,-9,5,6,-3,-3,2,7,9,-6,8,3,-6,-4,8,-4,-1,9,-2,-5,-6,9,-2,-3],[-4,7,6,6,5,-4,7,7,-10,2,-1,-9,5,-4,-6,-9,5,-4,8,-3,-2,-5,7,-7,-8,1,5,-6,-9,9,-9,-6,4,5,2,4,-7,2,-1,-8,-7,-8,-10,5,7,5,-2,-10,2,10,-3,9,3,1,2,5,-10,-2,-9,2,-8,-2,9,-9,-7,-7,3,-10,7,2,-5,-9,-2,-7,-5,-9,-3,5],[4,5,1,4,7,-2,-7,4,-3,-7,3,10,-1,10,1,-8,-7,8,4,-4,6,-7,-2,5,5,2,5,5,2,-2,1,8,4,8,6,10,7,6,-10,7,-4,5,-3,-7,-6,-6,10,6,9,-1,5,-8,-1,-4,-7,10,1,3,4,9,-9,-8,8,-3,8,-2,7,9,-6,1,-5,-5,4,10,-7,1,-3,-5],[1,-10,1,-3,-5,6,-5,-5,8,7,-7,4,-8,-2,-4,-4,4,-5,9,1,10,5,6,6,-1,8,1,-4,6,10,2,4,-1,8,7,-5,-1,-2,2,1,-2,1,-10,2,10,6,7,5,9,9,-7,2,-5,-2,-4,-10,1,-2,6,-7,-8,-6,2,-5,9,6,-8,-3,-3,-10,10,-3,-1,4,-9,-4,5,-1],[5,10,10,9,4,-1,-9,-2,-2,1,-10,-3,-9,5,10,3,-2,9,-6,-9,2,-7,-2,-1,-6,10,-9,-6,-1,-2,-6,6,7,1,-6,4,-10,-1,2,7,-8,3,-9,8,9,-10,-7,5,4,7,-6,-9,4,9,6,3,2,-1,-4,-2,1,9,10,9,-8,3,-7,-10,-4,6,-4,4,-4,8,4,-2,2,2],[-3,-6,-7,-5,-3,5,4,7,-8,-4,6,2,-2,6,8,-5,-6,4,-2,-8,-5,-2,4,-7,-8,9,-4,3,-7,-9,-6,-6,9,-6,8,-4,8,-4,-5,9,3,-7,-8,3,1,10,8,10,3,-6,1,-6,8,-5,2,-6,1,9,8,-7,-4,4,3,9,9,9,-7,-1,6,10,2,-2,-3,-4,-3,-8,10,-10],[8,-8,-5,9,5,-1,-5,-10,8,2,3,2,9,-4,4,3,-1,8,-10,-2,-6,8,3,-10,10,-4,-8,-8,8,7,5,-3,10,6,8,-7,-8,-6,2,4,6,6,6,-2,-7,-6,8,1,-3,-10,-3,-5,-1,-4,7,-9,-7,8,9,8,8,6,-5,3,-4,-9,9,9,-5,7,10,6,8,-1,-5,-3,-2,8]], dtype = "int64")#candidate|4761|(8, 78)|const|int64
call_4760 = relay.TupleGetItem(func_3939_call(relay.reshape(const_4761.astype('int64'), [624,])), 3)
call_4762 = relay.TupleGetItem(func_3941_call(relay.reshape(const_4761.astype('int64'), [624,])), 3)
func_1741_call = mod.get_global_var('func_1741')
func_1744_call = mutated_mod.get_global_var('func_1744')
const_4778 = relay.const([-4.773826,8.180669,9.195431,8.970007,9.741926,-0.929354,-1.815410,6.894251,8.676002,5.307524,7.493786,-1.816755,4.277415,-5.641622,-0.896006,8.214134,-4.367474,-0.629917,7.254862,-3.777959,0.107090,5.107468,8.635726,-7.281985,0.896172,-9.996158,-1.568787,6.715698,-9.808506,-5.587931,1.219960,-2.025954,-6.920930,9.518412,-3.800993,-7.628915,-1.567776,-7.576693,8.458343,-7.855153,-8.772239,8.062115,-8.579227,0.470053,2.705945,0.707587,6.050498,-3.571301,-5.166750,5.388353,9.548542,-1.555739,0.722084,-9.807818,-7.177804,1.557361,0.084185,5.140884,0.808451,-4.838515,-6.541250,5.257875,0.833499,-8.440523,6.582787,3.053484], dtype = "float32")#candidate|4778|(66,)|const|float32
call_4777 = func_1741_call(relay.reshape(const_4778.astype('float32'), [6, 11]))
call_4779 = func_1741_call(relay.reshape(const_4778.astype('float32'), [6, 11]))
output = relay.Tuple([uop_4749,call_4753,call_4755,call_4757,const_4758,call_4760,const_4761,call_4777,const_4778,])
output2 = relay.Tuple([uop_4749,call_4754,call_4756,call_4759,const_4758,call_4762,const_4761,call_4779,const_4778,])
func_4784 = relay.Function([var_4748,], output)
mod['func_4784'] = func_4784
mod = relay.transform.InferType()(mod)
mutated_mod['func_4784'] = func_4784
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4785 = relay.var("var_4785", dtype = "float64", shape = (5, 3))#candidate|4785|(5, 3)|var|float64
func_4784_call = mutated_mod.get_global_var('func_4784')
call_4786 = func_4784_call(var_4785)
output = call_4786
func_4787 = relay.Function([var_4785], output)
mutated_mod['func_4787'] = func_4787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_900_call = mod.get_global_var('func_900')
func_902_call = mutated_mod.get_global_var('func_902')
call_4792 = relay.TupleGetItem(func_900_call(), 0)
call_4793 = relay.TupleGetItem(func_902_call(), 0)
func_4314_call = mod.get_global_var('func_4314')
func_4316_call = mutated_mod.get_global_var('func_4316')
call_4804 = relay.TupleGetItem(func_4314_call(), 1)
call_4805 = relay.TupleGetItem(func_4316_call(), 1)
func_3080_call = mod.get_global_var('func_3080')
func_3082_call = mutated_mod.get_global_var('func_3082')
call_4810 = relay.TupleGetItem(func_3080_call(), 3)
call_4811 = relay.TupleGetItem(func_3082_call(), 3)
func_3111_call = mod.get_global_var('func_3111')
func_3112_call = mutated_mod.get_global_var('func_3112')
call_4815 = relay.TupleGetItem(func_3111_call(), 0)
call_4816 = relay.TupleGetItem(func_3112_call(), 0)
func_1258_call = mod.get_global_var('func_1258')
func_1259_call = mutated_mod.get_global_var('func_1259')
call_4822 = relay.TupleGetItem(func_1258_call(), 1)
call_4823 = relay.TupleGetItem(func_1259_call(), 1)
uop_4826 = relay.exp(call_4792.astype('float32')) # shape=(2, 6, 9)
uop_4828 = relay.exp(call_4793.astype('float32')) # shape=(2, 6, 9)
func_1386_call = mod.get_global_var('func_1386')
func_1390_call = mutated_mod.get_global_var('func_1390')
var_4830 = relay.var("var_4830", dtype = "float32", shape = (117,))#candidate|4830|(117,)|var|float32
var_4831 = relay.var("var_4831", dtype = "uint8", shape = (1120,))#candidate|4831|(1120,)|var|uint8
call_4829 = relay.TupleGetItem(func_1386_call(relay.reshape(var_4830.astype('float32'), [117,]), relay.reshape(var_4831.astype('uint8'), [1120,]), ), 5)
call_4832 = relay.TupleGetItem(func_1390_call(relay.reshape(var_4830.astype('float32'), [117,]), relay.reshape(var_4831.astype('uint8'), [1120,]), ), 5)
func_4593_call = mod.get_global_var('func_4593')
func_4595_call = mutated_mod.get_global_var('func_4595')
call_4845 = relay.TupleGetItem(func_4593_call(relay.reshape(call_4829.astype('uint8'), [1120,])), 2)
call_4846 = relay.TupleGetItem(func_4595_call(relay.reshape(call_4829.astype('uint8'), [1120,])), 2)
output = relay.Tuple([call_4804,call_4810,call_4815,call_4822,uop_4826,call_4829,var_4830,var_4831,call_4845,])
output2 = relay.Tuple([call_4805,call_4811,call_4816,call_4823,uop_4828,call_4832,var_4830,var_4831,call_4846,])
func_4847 = relay.Function([var_4830,var_4831,], output)
mod['func_4847'] = func_4847
mod = relay.transform.InferType()(mod)
mutated_mod['func_4847'] = func_4847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4847_call = mutated_mod.get_global_var('func_4847')
var_4849 = relay.var("var_4849", dtype = "float32", shape = (117,))#candidate|4849|(117,)|var|float32
var_4850 = relay.var("var_4850", dtype = "uint8", shape = (1120,))#candidate|4850|(1120,)|var|uint8
call_4848 = func_4847_call(var_4849,var_4850,)
output = call_4848
func_4851 = relay.Function([var_4849,var_4850,], output)
mutated_mod['func_4851'] = func_4851
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2311_call = mod.get_global_var('func_2311')
func_2312_call = mutated_mod.get_global_var('func_2312')
call_4875 = relay.TupleGetItem(func_2311_call(), 0)
call_4876 = relay.TupleGetItem(func_2312_call(), 0)
func_571_call = mod.get_global_var('func_571')
func_576_call = mutated_mod.get_global_var('func_576')
const_4883 = relay.const([[1.891559,6.156672,6.798025,-1.328451,-7.548190,-4.561130,0.675115,6.221020,-0.558866,5.962800,-9.976284,8.211626,9.151314,-7.327654,-7.757801,-3.903273,-2.758476,8.288146,4.010788,-9.678225,-9.976557,1.112458,4.549595,9.978575,9.559714,3.432324,-0.233803,-7.401213,9.387764,-6.650165,9.649719,4.195267,-4.036522,9.991431,-9.995582,3.578261],[-0.974986,-2.720555,7.166554,-8.171185,-7.083999,-5.187647,-1.707719,-9.908608,0.037312,1.161764,-4.452327,-7.700052,-9.581304,-0.175690,-0.047411,4.464984,-0.723025,-9.604378,7.451345,-8.387807,-7.627427,2.954690,8.165188,-2.537865,-0.817377,4.856701,7.783824,5.051959,5.491456,-4.567362,0.414415,7.561698,-8.050550,1.448791,-0.651305,9.087218],[-6.455828,0.300891,8.929673,-3.363711,3.998921,-1.841350,-2.077233,-6.247051,1.105577,8.755111,-7.084479,-6.780656,-0.929054,7.552230,0.206370,8.365566,4.687182,-1.583520,-9.758439,-3.454767,-7.313649,-1.983636,-2.298723,0.724280,-3.185391,-2.753614,1.671607,4.492783,-0.491011,-8.236625,0.343781,1.957054,-8.142248,9.797123,-9.338966,-8.957726]], dtype = "float64")#candidate|4883|(3, 36)|const|float64
const_4884 = relay.const([10,1,4,-2,1,-6,4,-9,-4,-8,9,3,8,-5,3,-5,10,1,-10,-1,-4,8,-8,-1,-4,-7,3,-5,4,-1,3,-1,4,7,4,6,4,6,-5,-4,7,3,9,-1,9,-3,-8,7,6,-7,-1,-8,9,7,-2,4,-4,9,5,8,10,6,6,1,7,-10,-10,-5,4,-4,5,-6,-3,2,-3,-1,4,2,-3,9,2,10,10,3,-9,10,3,5,-9,3,1,-8,3,4,4,8,5,-7,5,-10,-5,2,-6,-5,6,-10,3,-2,7,-4,9,4,10,-8,-1,3,1,-3,4,6,7,-7,-2,-7,-4,10,3,-5,7,-9,-6,-4,10,3,-5,-4,-5,-3,1,-7,-10,-6,3,5,-9,-8,-1,-9,8,-4,3,7,2,-6,-9,8,8,-2,7,10,-4,-8,-1,-5,-1,3,-1,-1,-8,4,7,-7,-5,-9,6,8,-10,-6,-3,9,4,-7,2,-5,-6,10,-2,2,5,10,1,-3,4,9,4,1,-9,10,10,-2,6,-10,8,-6,1,4,5,2,-1,-9,8,3,-10,-7,-10,-7,-10,5,-8,8,-8,-3,4,-4,-6,-9,3,-10,-7,-3,5,-5,6,-2,2,6,-4,5,-4,-2,10,-3,-5,5,-9,9,8,-10,6,3,-3,10,-9,7,1,-4,-3,3,-1,10,-9,-5,-4,3,8,-8,4,10,10,-7,-7,4,-9,7,-7,9,5,5,2,9,-6,10,-2,5,10,-5,-2,-8,-9,-10,-2,-4,-6,6,7,-7,10,-4,10,6,-1,8,3,-6,-10,1,-7,9,-6,-1,-8,-7,-6,3,-10,5,-2,-5,-8,9,9,-10,-9,-10,-3,9,9,-4,-8,-10,-7,-8,-9,-6,-5,-9,-7,1,-9,10,-3,-5,-4,7,5,-8,6,1,-10,6,-2,-10,-1,2,1,4,-10,8,8,-5,5,-5,-1,8,-3,-9,-7,-3,-7,10,6,3,3,-9,-7,3,-10,-4,-5,4,-7,3,9,4,-3,-5,-6,-5,10,-9,-10,10,1,1,-8,-5,8,-9,-6,-5,5,7,8,2,10,6,6,-10,-2,4,-7,-5,9,-4,-6,3,10,-7,-4,6,-2,3,-10,4,5,-2,-7,9,-2,10,-3,1,4,2,9,-3,-2,-9,-9,-2,1,9,2,1,-1,4,-3,-9,-5,7,9,-4,-6,1,6,-2,-9,2,-8,-5,-3,5,4,-2,-5,2,7,-4,7,-10,1,7,-2,-3,-3,1,9,-1,-2,-1,-2,-10,9,3,9,8,-5,4,-7,10,-5,-3,7,-9,-6,5,-5,10,6,9,-7,9,-5,1,-8,-9,4,-9,-7,9,1,3,8,8,-7,3,-8,-7,-5,-5,3,-8,-8,-7,7,10,1,-2,9,5,10,1,10,1,10,8,3,-8,7,8,3,-2,3,3,7,-7,6,5,6,1,5,9,9,9,-3,10,6,10,7,1,-1,-10,-8,5,4,-2,-9,-5,8,-4,2,7,-7,7,-10,9,1,-10,-8,-5,-3,1,9,10,-1,-10,-10,1,6,3,-8,-7,4,8,-4,-4,1,1,-1,-7,7,7,4,5,6,6,-2,3,-2,-10,3,7,9,-3,-9,5,8,3,10,2,6,9,10,-4,2,-3,7,-10,8,-1,6,2,9,-5,-1,-4,4,-5,-7,1,4,-8,-3,-1,4,5,7,-3,3,5,5,-3,5,7,8,5,1,-6,2,3,-7,-3,8,-1,3,4,-5,1,6,4,-6,-7,2,1,-1,7,7,-4,-5,-7,-9,8,-8,6,7,-10,-10,-9,-2,-6,7,3,-5,-8,-2,-1,-5,-8,6,-9,-5,5,5,10,4,-2,-1,-4,4,9,8,8,6,10,-10,-6,-9,-2,7,-4,10,-2,1,-1,2,2,9,3,5,-9,4,2,10,-8,8,8,7,10,7,-4,1,-9,5,-6,-7,7,-4,-3,-5,-1,-4,-10,8,3,-3,-6,-5,5,-7,2,7,3,8,-8,-10,3,-8,7,5,5,6,-2,-4,-1,-7,-5,2,-10,8,3,-6,2,-1,2,-8,4,8,-7,3,5,10,-8,10,3,3,5,-6,5,-5,-3,-4,9,5,4,3,-7,1,-7,3,-10,8,8,-2,1,-10,2,-3,5,8,-5,-1,6,-10,-3,-3,-9,-8,-4,2,2,10,-5,7,-3,1,6,2,2,-2,-5,7,5,5,-8,5,-6,-3,9,10,7,-2,1,-4,6,-9,-3,6,-4,7,7,-1,6,3,6,-9,-5,5,-3,-1,6,-1,-8,5,10,-5,4,10,-2,5,-6,-10,-5,9,3,-8,-1,8,-10,5,-6,6,8,10,-9,-9,-1,-8,-5,4,-8,-9,-3,-2,9,-2,-8,5,-6,-8,-3,-10,6,-9,-6,1,7,-2,-6,-3,2,1,6,7,-4,5,-10,10,-6,10,-3,-3,-10,3,1,-2,1,-4,1,9,4,1,-2,3,1,7,4,-6,-6,2,-5,2,-10,-5,6,4,-9,-8,-7,6,-4,-4,4,3,-1,9,1,-3,6,10,3,3,-1,2,2,6,10,4,-9,4,-2,-5,-4,4,8,3,-9,1,9,-6,3,7,-1,7,-8,2,-6,2,7,10,-1,-5,9,-10,1,-9,9,8,-7,-4,10,4,2,5,-4,-5,8,-7,9,-7,-5,-5,-2,-6,1,-3,-5,6,5,-9,10,5,-5,7,10,-4,-8,-1,3,-1,-9,-5,9,4,-7,-2,6,-5,10,2,-5,8,5,-6,-9,5,1,-4,3,6,-10,9,8,6,-7,9,-5,7,-8,-8,-2,-9,-5,3,1,-10,-8,7,-4,-3,9,2,10,-4,4,7,7,7,9,9,-9,-2,-9,-10,-2,-3,6,-7,-7,-9,4,-7,4,-2,5,-4,2,9,5,-4,4,-7,5,1,4,-4,-5,-1,6,1,-5], dtype = "uint8")#candidate|4884|(1120,)|const|uint8
call_4882 = relay.TupleGetItem(func_571_call(relay.reshape(const_4883.astype('float64'), [2, 6, 9]), relay.reshape(const_4883.astype('float64'), [2, 6, 9]), relay.reshape(const_4884.astype('uint8'), [4, 280]), ), 0)
call_4885 = relay.TupleGetItem(func_576_call(relay.reshape(const_4883.astype('float64'), [2, 6, 9]), relay.reshape(const_4883.astype('float64'), [2, 6, 9]), relay.reshape(const_4884.astype('uint8'), [4, 280]), ), 0)
var_4892 = relay.var("var_4892", dtype = "int64", shape = (700,))#candidate|4892|(700,)|var|int64
bop_4893 = relay.floor_divide(call_4875.astype('float64'), relay.reshape(var_4892.astype('float64'), relay.shape_of(call_4875))) # shape=(700,)
bop_4896 = relay.floor_divide(call_4876.astype('float64'), relay.reshape(var_4892.astype('float64'), relay.shape_of(call_4876))) # shape=(700,)
func_3981_call = mod.get_global_var('func_3981')
func_3983_call = mutated_mod.get_global_var('func_3983')
call_4902 = relay.TupleGetItem(func_3981_call(), 1)
call_4903 = relay.TupleGetItem(func_3983_call(), 1)
func_3013_call = mod.get_global_var('func_3013')
func_3015_call = mutated_mod.get_global_var('func_3015')
call_4906 = func_3013_call()
call_4907 = func_3013_call()
func_1801_call = mod.get_global_var('func_1801')
func_1804_call = mutated_mod.get_global_var('func_1804')
var_4912 = relay.var("var_4912", dtype = "float32", shape = (132,))#candidate|4912|(132,)|var|float32
call_4911 = relay.TupleGetItem(func_1801_call(relay.reshape(var_4912.astype('float32'), [11, 4, 3])), 0)
call_4913 = relay.TupleGetItem(func_1804_call(relay.reshape(var_4912.astype('float32'), [11, 4, 3])), 0)
uop_4914 = relay.atan(const_4883.astype('float64')) # shape=(3, 36)
bop_4929 = relay.bitwise_or(call_4911.astype('int32'), relay.reshape(var_4912.astype('int32'), relay.shape_of(call_4911))) # shape=(11, 4, 3)
bop_4932 = relay.bitwise_or(call_4913.astype('int32'), relay.reshape(var_4912.astype('int32'), relay.shape_of(call_4913))) # shape=(11, 4, 3)
var_4933 = relay.var("var_4933", dtype = "float64", shape = (3, 36))#candidate|4933|(3, 36)|var|float64
bop_4934 = relay.divide(uop_4914.astype('float32'), relay.reshape(var_4933.astype('float32'), relay.shape_of(uop_4914))) # shape=(3, 36)
uop_4938 = relay.sqrt(call_4911.astype('float32')) # shape=(11, 4, 3)
uop_4940 = relay.sqrt(call_4913.astype('float32')) # shape=(11, 4, 3)
bop_4943 = relay.greater(uop_4914.astype('bool'), relay.reshape(bop_4934.astype('bool'), relay.shape_of(uop_4914))) # shape=(3, 36)
output = relay.Tuple([call_4882,const_4884,bop_4893,call_4902,call_4906,bop_4929,uop_4938,bop_4943,])
output2 = relay.Tuple([call_4885,const_4884,bop_4896,call_4903,call_4907,bop_4932,uop_4940,bop_4943,])
func_4948 = relay.Function([var_4892,var_4912,var_4933,], output)
mod['func_4948'] = func_4948
mod = relay.transform.InferType()(mod)
mutated_mod['func_4948'] = func_4948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4948_call = mutated_mod.get_global_var('func_4948')
var_4950 = relay.var("var_4950", dtype = "int64", shape = (700,))#candidate|4950|(700,)|var|int64
var_4951 = relay.var("var_4951", dtype = "float32", shape = (132,))#candidate|4951|(132,)|var|float32
var_4952 = relay.var("var_4952", dtype = "float64", shape = (3, 36))#candidate|4952|(3, 36)|var|float64
call_4949 = func_4948_call(var_4950,var_4951,var_4952,)
output = call_4949
func_4953 = relay.Function([var_4950,var_4951,var_4952,], output)
mutated_mod['func_4953'] = func_4953
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2545_call = mod.get_global_var('func_2545')
func_2546_call = mutated_mod.get_global_var('func_2546')
call_5036 = func_2545_call()
call_5037 = func_2545_call()
output = relay.Tuple([call_5036,])
output2 = relay.Tuple([call_5037,])
func_5044 = relay.Function([], output)
mod['func_5044'] = func_5044
mod = relay.transform.InferType()(mod)
output = func_5044()
func_5045 = relay.Function([], output)
mutated_mod['func_5045'] = func_5045
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5098 = relay.var("var_5098", dtype = "float32", shape = (14, 3, 7))#candidate|5098|(14, 3, 7)|var|float32
uop_5099 = relay.tan(var_5098.astype('float32')) # shape=(14, 3, 7)
func_1672_call = mod.get_global_var('func_1672')
func_1674_call = mutated_mod.get_global_var('func_1674')
var_5106 = relay.var("var_5106", dtype = "uint8", shape = (2, 560))#candidate|5106|(2, 560)|var|uint8
call_5105 = relay.TupleGetItem(func_1672_call(relay.reshape(var_5106.astype('uint8'), [1120,])), 2)
call_5107 = relay.TupleGetItem(func_1674_call(relay.reshape(var_5106.astype('uint8'), [1120,])), 2)
func_3041_call = mod.get_global_var('func_3041')
func_3043_call = mutated_mod.get_global_var('func_3043')
call_5109 = relay.TupleGetItem(func_3041_call(), 1)
call_5110 = relay.TupleGetItem(func_3043_call(), 1)
output = relay.Tuple([uop_5099,call_5105,var_5106,call_5109,])
output2 = relay.Tuple([uop_5099,call_5107,var_5106,call_5110,])
func_5113 = relay.Function([var_5098,var_5106,], output)
mod['func_5113'] = func_5113
mod = relay.transform.InferType()(mod)
mutated_mod['func_5113'] = func_5113
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5113_call = mutated_mod.get_global_var('func_5113')
var_5115 = relay.var("var_5115", dtype = "float32", shape = (14, 3, 7))#candidate|5115|(14, 3, 7)|var|float32
var_5116 = relay.var("var_5116", dtype = "uint8", shape = (2, 560))#candidate|5116|(2, 560)|var|uint8
call_5114 = func_5113_call(var_5115,var_5116,)
output = call_5114
func_5117 = relay.Function([var_5115,var_5116,], output)
mutated_mod['func_5117'] = func_5117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2825_call = mod.get_global_var('func_2825')
func_2827_call = mutated_mod.get_global_var('func_2827')
call_5153 = func_2825_call()
call_5154 = func_2825_call()
func_4784_call = mod.get_global_var('func_4784')
func_4787_call = mutated_mod.get_global_var('func_4787')
var_5193 = relay.var("var_5193", dtype = "float64", shape = (15,))#candidate|5193|(15,)|var|float64
call_5192 = relay.TupleGetItem(func_4784_call(relay.reshape(var_5193.astype('float64'), [5, 3])), 4)
call_5194 = relay.TupleGetItem(func_4787_call(relay.reshape(var_5193.astype('float64'), [5, 3])), 4)
output = relay.Tuple([call_5153,call_5192,var_5193,])
output2 = relay.Tuple([call_5154,call_5194,var_5193,])
func_5202 = relay.Function([var_5193,], output)
mod['func_5202'] = func_5202
mod = relay.transform.InferType()(mod)
var_5203 = relay.var("var_5203", dtype = "float64", shape = (15,))#candidate|5203|(15,)|var|float64
output = func_5202(var_5203)
func_5204 = relay.Function([var_5203], output)
mutated_mod['func_5204'] = func_5204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3041_call = mod.get_global_var('func_3041')
func_3043_call = mutated_mod.get_global_var('func_3043')
call_5212 = relay.TupleGetItem(func_3041_call(), 1)
call_5213 = relay.TupleGetItem(func_3043_call(), 1)
func_4648_call = mod.get_global_var('func_4648')
func_4650_call = mutated_mod.get_global_var('func_4650')
call_5215 = relay.TupleGetItem(func_4648_call(), 1)
call_5216 = relay.TupleGetItem(func_4650_call(), 1)
output = relay.Tuple([call_5212,call_5215,])
output2 = relay.Tuple([call_5213,call_5216,])
func_5218 = relay.Function([], output)
mod['func_5218'] = func_5218
mod = relay.transform.InferType()(mod)
output = func_5218()
func_5219 = relay.Function([], output)
mutated_mod['func_5219'] = func_5219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1963_call = mod.get_global_var('func_1963')
func_1965_call = mutated_mod.get_global_var('func_1965')
call_5297 = func_1963_call()
call_5298 = func_1963_call()
func_387_call = mod.get_global_var('func_387')
func_390_call = mutated_mod.get_global_var('func_390')
var_5301 = relay.var("var_5301", dtype = "uint8", shape = ())#candidate|5301|()|var|uint8
var_5302 = relay.var("var_5302", dtype = "uint8", shape = (1120,))#candidate|5302|(1120,)|var|uint8
call_5300 = relay.TupleGetItem(func_387_call(relay.reshape(var_5301.astype('uint8'), []), relay.reshape(var_5302.astype('uint8'), [1120,]), ), 0)
call_5303 = relay.TupleGetItem(func_390_call(relay.reshape(var_5301.astype('uint8'), []), relay.reshape(var_5302.astype('uint8'), [1120,]), ), 0)
output = relay.Tuple([call_5297,call_5300,var_5301,var_5302,])
output2 = relay.Tuple([call_5298,call_5303,var_5301,var_5302,])
func_5353 = relay.Function([var_5301,var_5302,], output)
mod['func_5353'] = func_5353
mod = relay.transform.InferType()(mod)
var_5354 = relay.var("var_5354", dtype = "uint8", shape = ())#candidate|5354|()|var|uint8
var_5355 = relay.var("var_5355", dtype = "uint8", shape = (1120,))#candidate|5355|(1120,)|var|uint8
output = func_5353(var_5354,var_5355,)
func_5356 = relay.Function([var_5354,var_5355,], output)
mutated_mod['func_5356'] = func_5356
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4228_call = mod.get_global_var('func_4228')
func_4229_call = mutated_mod.get_global_var('func_4229')
call_5363 = func_4228_call()
call_5364 = func_4228_call()
output = relay.Tuple([call_5363,])
output2 = relay.Tuple([call_5364,])
func_5378 = relay.Function([], output)
mod['func_5378'] = func_5378
mod = relay.transform.InferType()(mod)
mutated_mod['func_5378'] = func_5378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5378_call = mutated_mod.get_global_var('func_5378')
call_5379 = func_5378_call()
output = call_5379
func_5380 = relay.Function([], output)
mutated_mod['func_5380'] = func_5380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2135_call = mod.get_global_var('func_2135')
func_2136_call = mutated_mod.get_global_var('func_2136')
call_5395 = relay.TupleGetItem(func_2135_call(), 0)
call_5396 = relay.TupleGetItem(func_2136_call(), 0)
func_1564_call = mod.get_global_var('func_1564')
func_1566_call = mutated_mod.get_global_var('func_1566')
const_5407 = relay.const([[1.614747,-6.071770,-5.991699,-5.692126,-3.431168,7.967584,3.259988,5.868112,-3.636435,1.836127,8.039673,2.225947,-0.377965,-9.450120,-1.039649,4.519322,7.173044,-0.468115,-0.787307,-5.110092,-9.298274,9.509539,0.340103,-2.806095,0.480194,-7.192311,-0.347993,-2.143209,-6.598955,-2.866706,-8.357598,6.249449,6.281641,-5.847922,-4.232691,-6.579867,-3.582119,1.903571,-5.519065,2.932611,7.290217,-2.002510,-6.786206,5.925528,-4.895711,5.550637,4.006146,-5.246352,-1.768457,-2.703366,1.081835,-4.263307,2.538845,8.001764,3.341279,2.853027,-7.394232,-3.581675,-1.213897,-7.449630,3.100985,-3.190714,-5.830570,4.270095,4.895975,8.125510,-8.568797,-3.608863,6.566363,-6.840103,1.521092,-4.433549,0.498338,-6.425192,-3.412463,-9.461770,-6.440739,-4.422317,5.958568,9.908252,8.215863,-8.069089,-5.523934,4.094533,-8.753302,-8.908812,-5.664653,-5.310153,-9.681780,4.318087,4.147039,-3.095033,-7.159743,-7.577437,0.863538,-3.079517,-9.079014,-6.497133,-7.788639,5.029929,1.794302,-7.692022,-9.752366,-9.708260,3.243407,4.600153,6.968186,-5.795391,-5.727441,-8.976391,-1.028865,-2.693398,9.639705,-1.306289,8.617839,-0.391517,3.238194,-0.804741,6.230127,-0.736230,-1.612584,4.795694,-7.576517,-9.365169,-1.075644,-8.099309,2.986688,-3.225729,6.541115,-9.141644,-3.994393,-0.728809,6.296081,5.020444,8.822277,4.300668,8.820830,8.089592,-1.478278,-4.285098,-1.853217,-6.177996,0.086856,-1.840619,3.934206,7.977464,-5.656337,8.984991,-8.175814,-3.515300,6.922751,-6.925595,2.787560,-8.749090,0.363999,-0.101953,2.580292,0.473800,1.699101,9.865412,4.834452,-9.546262,-0.587662,3.471899,-9.470685,-8.565229,-0.760909,-5.192989,0.274975,2.260568,4.155171,-1.509835,-8.764656,-9.331392,-8.931289,-9.873531,-2.011580,5.381453,4.776849,-1.164091,-2.877341,4.416145,9.036964,-0.119569,-7.023066,4.315782,-5.649352,-1.791361,9.426242,-4.209784,-6.491433,9.943521,-1.461084,-4.031431,-4.333339,7.006447,4.542287,8.171435,9.877897,4.364423,1.975927,1.410935,0.981965,4.126793,-7.346420,-5.453692,-1.382758,-1.421980,-1.971437,-4.911295,9.681747,5.534563,-1.908856,3.215617,1.898686,4.434721,2.845243,-3.450865,-1.059892,4.451226,9.498413,-4.245851,-4.655493,-8.850277,0.776353,1.326362,2.186573,9.338893,4.990011,4.604523,-1.008169,7.942781,5.284331,-7.233060,3.058810,4.491393,8.997357,2.369067,-0.779142,-1.413535,-6.314631,-5.541505,-7.572820,-6.022092,-4.314137,-7.397310,-2.471264,-3.125967,6.274578,-8.934626,-4.654170,-0.271594,3.149078,7.429937,0.774263,3.536641,4.927072,7.880419,8.434045,6.044773,6.125086,-8.968908,-7.960883,-0.711537,2.073675,-9.209806,-1.649456,0.640223,-9.703591,7.852381,-3.418024,-1.700602,-1.139824,-4.897597,1.074252,6.281051,8.069804,-8.689209,-5.582382,-8.165001,5.617679,2.791765,1.325406,8.222102,-3.685909,5.536070,2.298293,-9.135034,-4.549487,-5.129874,7.860149,-7.509215,1.393273,-5.503154,5.006060,-0.267367,5.469742,-3.327325,-1.074325,6.357535,-3.610964,-9.868659,-9.306610,7.774562,1.248303,-3.768231,2.135483,6.798822,1.847844,-0.929544,-2.723825,-4.432793,3.215545,-6.983233,-4.411403,-0.450024,7.839551,1.976295,1.073236,-4.188165,-9.674669,1.186702,5.140647,-7.490848,-2.150256,-3.396540,6.695103,3.538912,5.413996,7.965348,6.080952,0.754162,-6.950248,-2.536932,3.025289,-4.880320,7.214304,-5.741193,-4.069438,0.701380,4.175926,-1.315558,-0.787293,7.530910,5.476826,-3.781197,-8.157989,1.287219,-8.623070,8.955062,-0.212699,3.899531,5.624919,7.610978,-3.711633,1.607034,-8.600164,1.186808,2.445601,-8.350444,5.578374,6.187594,-5.332331,-6.280854,-5.853754,3.567349,7.674981,-2.837537,-2.281130,-3.888401,-2.583855,-9.122109,6.381229,-5.546253,1.574315,-4.885771,9.063501,-2.099251,-8.389715,-7.626366,-1.702527,-7.059993,-5.400372,1.473106,-2.043596,3.271346,9.810450,3.015301,8.305624,9.001896,-0.342621,1.628698,5.338577,-7.920385,-5.490221,-3.810606,-8.248161,-6.071067,6.758521,1.347599,-9.123916,-9.707301,-5.665810,-7.223945,3.457848,-6.235992,9.186767,5.747226,-4.145580,9.816382,-1.414645,7.724842,-9.415823,1.219583,7.490036,1.480181,-5.280316,7.925273,1.522221,-1.305893,6.350055,-0.244489,9.924912,6.646263,5.067840,-2.944631,-5.086632,-7.017475,-4.634679,-8.486031,-7.365639,7.523162,-9.354702,-5.814675,-8.346135,-8.398440,8.472142,1.996410,2.214021,-5.866929,4.057414,-6.806318,6.862635,-9.965739,5.107598,6.426144,-8.744306,-3.062973,-6.097354,-6.470045,7.148307,-0.408924,0.404810,7.541728,5.837380,-7.759798,9.165917,-3.200684,5.069911,-6.147253,-4.362988,7.444241,-6.205065,8.878280,-7.715425,7.308714,-3.206353,-3.487756,2.247754,-0.366222,-3.575079,7.473338,-5.215095,-6.869293,-8.224398,-4.245178,-0.679987,1.759277,8.291749,1.524693,-1.193186,5.414876,8.364278,7.220369,-8.828246,0.724666,-1.028051,-0.062096,-7.891300,-9.863975,4.714844,5.915787,-3.231732,-3.387826,2.624727,1.000267,-0.860759,8.083708,9.044237,9.416346,-1.808197,-2.904899,6.263573,0.474301,6.488795,2.602521,-1.328955,-9.068119,3.006263,-3.653807,7.927457,8.448686,7.554100,0.170193,8.002756,-7.902268,9.173444,-1.943413,1.266016,-1.465205,2.430073,3.748600,3.086517,5.534976,-9.034372,8.126609,4.477093,5.564879,1.578698,8.454921,1.821161,6.668749,-5.019702,-8.732790,0.827614,-9.557320,-3.706020,4.974639,-3.139084,-2.445944,-0.949991,-3.829660,-6.863132,-4.526553,-2.710238,-3.737123,9.246880,-4.248699,5.031693,8.062699,5.021795,-4.302710,7.740762,7.981143,-7.819915,-3.557226,-6.089659,-1.075188,4.124070,-2.419481,0.045163,8.700115,-1.940381,-8.100447,-4.887148,3.659596,-6.797998,8.256975,8.370272,7.320297,3.767107,-3.031445,-8.174602,-3.424212,-7.049537,9.337419,-9.388174,-1.496830,-8.175202,-2.445482,7.958371,-5.974179,9.115896,0.878366,3.808543,-4.324111,5.285951,-7.480903,-1.923667,0.843576,0.435743,-8.735760,7.866666,8.531164,7.601163,9.712870,5.907995,-6.857412,4.050527,6.578379,-2.189882,4.291202,-5.452448,9.351389,7.934897,8.628453,0.692665,-9.319320,9.248679,-0.186139,0.121933,8.000952,-1.415581,-7.061730,2.300860,-2.911812,4.605547,5.892442,4.143459,-3.005794,1.005362,4.210292,7.487296,-1.731458,4.631965,-8.160135,-2.777300,3.253536,9.683940,-0.002827,6.770993,0.167787,6.546855,3.665539,3.385258,3.530026,1.466054,-2.571692,-4.571938,9.031198,7.293630,-7.920965,8.568189,-5.000081,7.045741,-2.863018,4.915585,-4.342910,-5.649033,6.405517,5.786240,9.021357,-5.692077,-8.686604,-9.749787,-3.716699,8.379145,9.039662,3.655465,0.160858,-6.118144,0.020327,8.540209,-3.343274,6.304878,-3.903918,-4.631156,-4.635212,1.163031,2.582013,-1.586686,4.766921,6.144656,7.545069,2.890673,2.561379,-0.603626,1.788078,-7.098481,9.691294,-9.253040,0.776906,5.288175,6.279143,-1.349303,-7.860480,-1.442742,-5.726888,-4.664668,-3.126109,-4.212236,-0.869261,9.234079]], dtype = "float32")#candidate|5407|(1, 693)|const|float32
call_5406 = func_1564_call(relay.reshape(const_5407.astype('float32'), [7, 11, 9]))
call_5408 = func_1564_call(relay.reshape(const_5407.astype('float32'), [7, 11, 9]))
output = relay.Tuple([call_5395,call_5406,const_5407,])
output2 = relay.Tuple([call_5396,call_5408,const_5407,])
func_5409 = relay.Function([], output)
mod['func_5409'] = func_5409
mod = relay.transform.InferType()(mod)
mutated_mod['func_5409'] = func_5409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5409_call = mutated_mod.get_global_var('func_5409')
call_5410 = func_5409_call()
output = call_5410
func_5411 = relay.Function([], output)
mutated_mod['func_5411'] = func_5411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3566_call = mod.get_global_var('func_3566')
func_3567_call = mutated_mod.get_global_var('func_3567')
call_5417 = relay.TupleGetItem(func_3566_call(), 0)
call_5418 = relay.TupleGetItem(func_3567_call(), 0)
output = relay.Tuple([call_5417,])
output2 = relay.Tuple([call_5418,])
func_5419 = relay.Function([], output)
mod['func_5419'] = func_5419
mod = relay.transform.InferType()(mod)
output = func_5419()
func_5420 = relay.Function([], output)
mutated_mod['func_5420'] = func_5420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4055_call = mod.get_global_var('func_4055')
func_4056_call = mutated_mod.get_global_var('func_4056')
call_5479 = func_4055_call()
call_5480 = func_4055_call()
func_5202_call = mod.get_global_var('func_5202')
func_5204_call = mutated_mod.get_global_var('func_5204')
const_5502 = relay.const([-2.383302,3.175700,-1.458586,-8.357193,-1.959561,-6.788051,-7.564087,-7.979408,9.543356,8.023608,4.017806,8.248073,2.816950,-7.345562,-2.167337], dtype = "float64")#candidate|5502|(15,)|const|float64
call_5501 = relay.TupleGetItem(func_5202_call(relay.reshape(const_5502.astype('float64'), [15,])), 1)
call_5503 = relay.TupleGetItem(func_5204_call(relay.reshape(const_5502.astype('float64'), [15,])), 1)
output = relay.Tuple([call_5479,call_5501,const_5502,])
output2 = relay.Tuple([call_5480,call_5503,const_5502,])
func_5511 = relay.Function([], output)
mod['func_5511'] = func_5511
mod = relay.transform.InferType()(mod)
mutated_mod['func_5511'] = func_5511
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5511_call = mutated_mod.get_global_var('func_5511')
call_5512 = func_5511_call()
output = call_5512
func_5513 = relay.Function([], output)
mutated_mod['func_5513'] = func_5513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5378_call = mod.get_global_var('func_5378')
func_5380_call = mutated_mod.get_global_var('func_5380')
call_5516 = relay.TupleGetItem(func_5378_call(), 0)
call_5517 = relay.TupleGetItem(func_5380_call(), 0)
output = relay.Tuple([call_5516,])
output2 = relay.Tuple([call_5517,])
func_5520 = relay.Function([], output)
mod['func_5520'] = func_5520
mod = relay.transform.InferType()(mod)
output = func_5520()
func_5521 = relay.Function([], output)
mutated_mod['func_5521'] = func_5521
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5553 = relay.const([[[-8,-8,1,3,-1,6,1,-2,1,10,-7,-1,4,-1,-7,-4],[5,5,1,-9,-1,10,-10,-8,2,-6,-3,-1,2,9,-6,-4],[5,8,-7,8,-9,-3,1,-9,-9,5,-6,10,-8,-5,4,-5],[1,2,-10,8,-9,10,2,4,-6,3,7,10,-4,8,-8,-6],[-8,-5,-1,8,3,1,-9,7,5,-9,-5,8,6,9,2,-1]],[[8,-9,-10,-10,-6,10,-7,3,9,6,1,-7,-1,10,-4,2],[-10,10,9,-5,-10,-2,-6,-10,-5,10,2,4,6,5,-7,-3],[-9,7,4,6,-10,2,5,10,-10,-7,-10,6,-5,7,9,6],[-4,7,-8,-1,-3,-2,-4,-8,3,-7,-6,-10,-3,10,-6,9],[3,7,10,8,10,2,2,-8,-5,9,-7,10,-5,-1,1,2]],[[-7,3,-8,1,-1,-2,2,8,-7,1,-6,-6,-3,4,7,8],[-7,-1,2,-1,-4,-5,-2,-6,-10,5,-9,-8,7,6,8,-10],[-5,-9,1,-9,4,-3,-7,-7,7,-4,2,9,-4,5,-9,10],[-4,-10,-1,-1,-2,-3,-5,-5,-2,-9,1,-4,-10,-10,2,4],[8,-2,-6,-4,-1,-7,-5,9,3,4,3,-2,6,6,1,5]],[[-6,8,2,-10,7,9,2,-1,-5,1,-2,-3,-7,8,10,9],[10,8,9,7,5,-10,-4,-4,-8,9,7,10,-4,2,-2,8],[8,6,-5,-5,-8,9,-10,3,7,-9,7,-10,10,2,5,-3],[-9,-2,1,5,4,3,7,3,-1,2,-4,8,-6,-5,4,6],[7,6,-5,7,-4,-3,-8,7,-9,-7,3,6,-8,10,8,-3]],[[-4,-3,9,8,2,-6,-8,-10,-4,-1,-2,6,-9,-2,-2,2],[-6,-5,-8,-10,-6,3,-1,-2,-9,2,1,9,-2,-7,-6,2],[-5,-6,-2,5,5,2,10,1,-7,1,10,-8,-3,-9,-5,2],[2,4,6,-1,-9,9,9,1,4,5,-3,6,-9,6,8,5],[6,3,1,3,9,1,3,-5,5,-8,-5,4,-9,-10,-6,8]],[[-6,-4,-7,9,10,-5,4,-7,-9,7,9,-10,2,9,4,-10],[8,-9,2,10,-10,2,-4,2,5,-9,-3,-5,8,-2,1,5],[7,-4,-4,8,1,7,-10,1,2,-10,-9,-9,8,9,3,-1],[-8,9,1,-5,9,2,-2,-5,-2,-9,-9,-8,-10,-8,-1,-5],[-6,-8,-4,-1,-4,2,-5,2,9,2,10,9,-7,4,8,4]],[[4,10,6,10,-4,7,7,-1,-3,-6,-3,4,2,7,-7,-3],[-4,8,-4,-9,1,10,-7,6,-5,4,7,-7,6,-10,-4,4],[6,5,10,-8,10,-7,-10,7,-7,-3,-9,-5,4,-7,-10,6],[3,-6,7,-2,-4,4,-3,-1,-1,7,7,-6,9,9,4,-7],[-1,10,9,-5,-10,-10,1,5,8,-6,4,-5,-7,4,2,-10]],[[4,-8,-9,-5,5,4,-7,-10,1,-9,9,-7,8,8,3,-10],[-8,-10,-5,-8,2,-6,2,-5,3,-9,-6,9,-10,-4,4,9],[-4,9,-6,10,2,9,4,-1,6,1,6,7,-6,-8,5,-2],[-10,8,1,-6,-6,9,8,6,9,7,-7,1,3,4,1,-7],[-1,7,-7,-7,7,-2,7,9,7,-1,-8,8,4,-1,9,5]],[[5,2,-6,-2,6,-6,-3,-6,10,-3,-2,2,-4,-2,-9,3],[-3,-7,-5,-10,4,-1,-2,5,6,2,10,7,-5,9,8,-9],[8,-9,-6,3,6,6,2,-2,1,8,8,-7,6,8,-9,-4],[4,9,4,-7,-7,10,4,10,8,1,5,8,6,-5,2,10],[-5,-3,3,1,4,-9,-5,-6,-9,8,4,5,-1,-3,-2,-8]],[[-3,7,-2,-6,-8,-7,-4,-6,9,-6,2,-5,2,6,2,-10],[-5,-1,-3,-5,1,-6,6,-5,9,-2,-3,-2,4,10,1,2],[-6,5,9,-4,6,5,-5,-9,-4,-3,-5,-3,-2,6,2,1],[1,1,8,10,7,-5,8,7,2,-8,-7,-7,-5,-4,1,6],[1,-9,5,2,7,-6,-1,4,5,2,6,-2,-2,-7,-2,-2]],[[2,-2,3,1,-3,-4,2,-6,1,-8,7,7,6,4,-8,-3],[-10,-9,10,4,7,-6,5,5,-1,-2,-4,-2,2,2,-2,10],[9,8,9,3,-9,4,-2,-1,-5,5,-3,-4,3,-5,-9,9],[-6,7,9,1,10,4,-8,7,10,-5,-9,8,-4,-6,-9,1],[2,-1,10,10,9,2,-9,-3,10,-1,-6,10,-1,-3,3,-6]],[[-3,-5,10,5,-7,1,5,-6,9,-6,4,4,-2,8,2,10],[4,10,-1,5,1,8,7,3,-9,2,-4,-1,-5,4,6,5],[-1,1,-10,-2,2,9,1,-9,10,6,-10,-2,7,-4,-10,-2],[-6,3,-1,6,-4,-5,8,7,-5,-2,1,2,10,2,7,-10],[-7,8,7,-1,1,-8,-8,-7,-8,-8,2,7,-7,9,3,6]],[[4,5,-10,-4,10,1,7,-3,-4,-5,2,-6,3,5,-7,-3],[7,-2,-4,-9,8,-4,-6,1,-7,-8,-8,-10,-2,-6,-7,1],[7,-10,-10,7,9,-7,10,6,-4,-8,1,-5,2,3,10,-3],[9,-10,-4,-9,10,-7,3,10,8,-2,-8,1,8,-1,-9,-7],[-10,7,6,7,1,-8,7,-2,8,3,10,-7,-7,-7,5,-5]],[[1,-8,-8,-4,-9,3,-10,3,10,-5,-10,-1,1,5,3,10],[2,2,-5,8,9,-1,8,-9,10,1,6,-6,1,2,1,-8],[4,-2,-4,-4,-2,2,-1,-8,-4,-10,2,-7,9,-5,-3,-3],[2,-5,-6,1,-6,-7,3,7,-6,-8,-2,1,6,4,-8,-8],[4,9,2,7,-5,4,-10,7,-7,4,10,3,-1,7,5,2]],[[-9,-9,-2,-1,-1,-5,6,-8,-7,-4,-10,-4,5,-4,5,2],[-8,-4,-7,7,10,10,-4,-10,-3,-9,-3,-7,2,-9,-5,10],[-1,-4,-1,-10,-5,-8,-1,1,3,10,-2,-4,-6,5,5,-7],[-2,-9,-3,4,9,6,-10,-7,-6,-9,-2,7,8,-9,7,-1],[6,2,1,5,7,2,-8,-10,-6,5,2,5,-1,-4,2,-7]]], dtype = "uint8")#candidate|5553|(15, 5, 16)|const|uint8
const_5554 = relay.const([[[-8,-9,-4,-3,3,-4,10,-9,3,3,2,3,-8,-8,1,-5],[6,-4,-6,-5,-8,2,-8,-8,-7,-4,4,-6,10,-9,4,10],[2,10,2,7,-4,-7,9,5,6,-4,7,-5,8,10,2,1],[5,-1,7,-6,-8,7,-10,-3,2,-9,1,-7,-7,-10,6,-4],[5,7,-3,4,10,9,4,8,-9,-4,-10,9,6,8,-3,3]],[[8,-1,-7,-2,-8,6,-3,7,-1,2,10,1,-3,9,1,-5],[6,-10,2,-9,-3,2,1,-7,8,6,-3,5,-5,-3,10,7],[-5,-8,-9,7,4,-5,9,-9,-1,7,3,-9,8,-7,1,6],[-1,5,1,-9,1,10,-5,-7,6,-2,5,7,5,-6,10,-4],[-4,8,-1,2,10,-4,-1,-3,6,-5,-9,8,10,2,-4,8]],[[7,5,2,2,9,7,8,8,5,6,-8,10,6,8,10,10],[-4,5,-4,8,-2,5,6,3,9,-7,-4,6,9,-2,2,4],[8,-9,-6,-8,-3,8,6,-1,3,-3,3,6,5,-10,-9,10],[6,4,8,2,-4,-1,4,-7,-9,3,-2,-5,9,2,4,7],[-3,1,2,-5,4,9,9,6,-8,2,-1,5,-4,8,-10,7]],[[-6,7,4,6,-1,9,-1,-9,-5,9,10,6,2,4,-10,7],[3,-6,9,8,-5,9,-3,6,-1,-6,10,7,-5,-6,-3,-1],[-1,5,8,-10,-10,2,-9,-1,-3,1,8,-7,-6,10,-8,-6],[-7,-8,4,-10,7,6,-10,6,6,9,3,9,-1,-1,-9,9],[-7,4,5,4,8,7,10,3,1,2,-10,-5,1,1,2,9]],[[-8,-1,-7,-6,6,2,9,4,7,-3,-10,-9,4,-4,-1,6],[-5,4,-3,-8,-4,-6,8,-4,-9,-4,-7,1,-3,10,7,-3],[2,-6,-8,5,-9,-6,3,3,-6,1,10,-7,-7,6,2,6],[-9,-10,-1,10,3,8,-5,-8,-8,6,-10,-10,9,-3,-9,4],[5,6,6,5,-1,7,-4,1,-5,9,-10,-4,-8,10,6,-7]],[[6,7,9,-3,-5,-8,-7,-10,-6,8,9,-6,9,-4,10,7],[3,1,-6,-4,-5,1,-3,-2,1,6,-4,-6,-10,9,10,-9],[-10,8,-5,10,-7,1,3,1,-5,-3,-3,3,9,-5,-8,3],[5,5,-4,-9,5,2,-3,-1,4,-9,-2,2,4,10,4,-9],[5,-10,-8,-9,-6,2,-8,2,-6,-10,-5,2,4,1,-5,8]],[[6,-8,-6,9,10,3,-4,-1,-8,-1,-7,-2,4,8,4,9],[5,-8,4,3,9,-3,3,-5,7,5,10,-5,-9,-4,-1,6],[-10,-5,2,-10,5,5,-9,10,8,-10,-1,3,-7,6,1,4],[-6,8,8,-8,1,-1,-6,8,4,-4,-4,8,5,-1,-6,10],[3,-10,5,-4,-5,-9,-3,7,-7,-6,-10,-2,8,1,-8,6]],[[6,4,5,-10,-10,1,5,5,-1,-1,-5,3,-8,-7,-7,2],[8,7,-4,6,-3,1,7,10,-7,6,-7,7,-7,-6,7,8],[-3,-1,-9,5,3,1,-2,-7,-5,-2,4,-10,2,-3,-3,4],[-5,5,3,-7,-5,-8,3,-5,10,1,-7,-5,6,-9,1,4],[-2,2,-10,2,9,-10,7,1,5,1,4,2,-8,-8,8,-6]],[[3,-6,7,8,-9,-8,-4,-2,-2,10,1,-5,-4,-7,-7,5],[-9,2,-8,-1,9,-3,-10,-3,-10,-8,6,1,6,-4,-10,-4],[-7,-6,9,2,-7,-2,-2,9,7,-4,-3,-2,-2,4,3,-3],[-6,-7,-6,-2,6,2,-8,-9,-2,-5,9,-6,4,-4,-9,9],[-6,10,-5,-9,-8,-8,-3,3,-3,2,6,2,-9,-8,3,-4]],[[4,-3,8,-2,2,-5,9,4,-6,4,4,5,10,2,1,-2],[-1,3,-6,8,-5,7,-2,-7,-5,2,5,-3,-1,8,-10,-6],[-5,10,4,-1,2,-4,-9,3,-2,-3,4,-3,10,6,2,-3],[-9,-10,3,-3,-9,9,9,-2,-9,-9,-3,-8,4,5,4,-4],[-10,-7,8,-8,-10,-7,-1,2,-5,2,1,-1,2,10,-3,-10]],[[-1,-6,8,5,10,-8,10,10,-9,3,2,7,-1,1,-3,9],[-9,-2,8,6,-9,9,-2,-5,3,5,6,-1,-10,3,3,-9],[6,9,9,3,8,7,3,3,4,1,-1,-6,-5,4,2,10],[5,5,-5,-1,-10,-4,-2,1,6,-3,4,-6,2,-7,-5,4],[6,-3,-8,5,1,-3,8,-9,7,1,-3,10,-9,10,4,4]],[[-5,-1,1,3,5,7,1,6,-9,-9,4,-8,6,8,5,-8],[-1,5,4,4,-5,3,-6,-6,-5,-7,-4,-5,6,10,7,2],[-8,-10,5,2,-4,8,5,4,10,-3,8,-7,-1,-6,5,-8],[6,-5,-1,-3,-3,4,-6,10,-10,10,-10,2,4,-2,7,3],[-10,-4,-9,-8,7,-2,2,9,-2,-10,8,4,10,-2,-7,-8]],[[-5,-10,9,-7,-1,1,1,-5,-3,-7,-9,-4,10,5,2,6],[8,-4,-7,-5,-1,4,-10,-7,6,-5,-7,-3,6,-4,-1,-10],[8,6,-4,-4,9,7,6,4,9,6,-8,-3,-7,7,-7,7],[-10,3,-3,-8,-4,6,2,4,9,7,1,4,-7,5,7,-3],[4,2,2,2,7,-8,7,-2,3,4,9,3,-10,-4,-10,-7]],[[-1,-2,8,-9,-3,6,10,-6,7,-1,9,-4,2,-9,3,7],[-2,-8,-4,-7,-7,-4,-1,2,-10,4,-6,-10,6,-3,5,4],[-8,10,-3,-8,8,-7,-4,-6,-3,6,9,-8,-7,-4,10,2],[2,1,-8,8,-2,-4,-6,-1,-1,8,6,2,6,10,4,5],[3,-5,-4,-9,-10,1,5,4,-2,5,8,-3,-3,-2,4,-7]],[[3,10,-5,-2,-1,-10,8,2,6,-7,-3,1,-3,5,2,6],[3,3,-4,4,9,-2,10,6,-1,4,-3,-2,-10,6,8,-7],[8,1,-6,-7,-1,-1,-5,8,-10,-10,9,-1,-8,1,9,-8],[-10,8,6,-1,6,-9,-7,-7,-1,-1,-6,7,1,9,-10,8],[-6,5,4,8,-8,-3,3,-3,6,5,8,7,2,3,2,1]]], dtype = "uint8")#candidate|5554|(15, 5, 16)|const|uint8
bop_5555 = relay.subtract(const_5553.astype('uint8'), relay.reshape(const_5554.astype('uint8'), relay.shape_of(const_5553))) # shape=(15, 5, 16)
func_3726_call = mod.get_global_var('func_3726')
func_3729_call = mutated_mod.get_global_var('func_3729')
var_5561 = relay.var("var_5561", dtype = "bool", shape = (1372,))#candidate|5561|(1372,)|var|bool
call_5560 = relay.TupleGetItem(func_3726_call(relay.reshape(var_5561.astype('bool'), [14, 7, 14])), 1)
call_5562 = relay.TupleGetItem(func_3729_call(relay.reshape(var_5561.astype('bool'), [14, 7, 14])), 1)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_5567 = func_361_call()
call_5568 = func_361_call()
output = relay.Tuple([bop_5555,call_5560,var_5561,call_5567,])
output2 = relay.Tuple([bop_5555,call_5562,var_5561,call_5568,])
func_5584 = relay.Function([var_5561,], output)
mod['func_5584'] = func_5584
mod = relay.transform.InferType()(mod)
mutated_mod['func_5584'] = func_5584
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5585 = relay.var("var_5585", dtype = "bool", shape = (1372,))#candidate|5585|(1372,)|var|bool
func_5584_call = mutated_mod.get_global_var('func_5584')
call_5586 = func_5584_call(var_5585)
output = call_5586
func_5587 = relay.Function([var_5585], output)
mutated_mod['func_5587'] = func_5587
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2925_call = mod.get_global_var('func_2925')
func_2927_call = mutated_mod.get_global_var('func_2927')
call_5610 = func_2925_call()
call_5611 = func_2925_call()
func_3171_call = mod.get_global_var('func_3171')
func_3172_call = mutated_mod.get_global_var('func_3172')
call_5619 = relay.TupleGetItem(func_3171_call(), 0)
call_5620 = relay.TupleGetItem(func_3172_call(), 0)
output = relay.Tuple([call_5610,call_5619,])
output2 = relay.Tuple([call_5611,call_5620,])
func_5627 = relay.Function([], output)
mod['func_5627'] = func_5627
mod = relay.transform.InferType()(mod)
mutated_mod['func_5627'] = func_5627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5627_call = mutated_mod.get_global_var('func_5627')
call_5628 = func_5627_call()
output = call_5628
func_5629 = relay.Function([], output)
mutated_mod['func_5629'] = func_5629
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5737 = relay.var("var_5737", dtype = "uint64", shape = (5, 15, 15))#candidate|5737|(5, 15, 15)|var|uint64
var_5738 = relay.var("var_5738", dtype = "uint64", shape = (5, 15, 15))#candidate|5738|(5, 15, 15)|var|uint64
bop_5739 = relay.bitwise_and(var_5737.astype('uint64'), relay.reshape(var_5738.astype('uint64'), relay.shape_of(var_5737))) # shape=(5, 15, 15)
func_1473_call = mod.get_global_var('func_1473')
func_1478_call = mutated_mod.get_global_var('func_1478')
var_5750 = relay.var("var_5750", dtype = "float32", shape = (700,))#candidate|5750|(700,)|var|float32
var_5751 = relay.var("var_5751", dtype = "float32", shape = (3, 36))#candidate|5751|(3, 36)|var|float32
const_5752 = relay.const([[False,False,True,False,True,False,False,False,False,True,False,True,True,True,True,True,True,False,False,True,True,False,True,False,False,False,True,True,True,True,False,True,True,False,True,False,False,False,False,False,True,True,True,False,False,True,False,True,True,False,True,False,False,False,True,True,False,False,False,True,True,True,False,False,True,False,True,True,False,True,True,True,False,False,True,False,True,True,False,False,True,True,True,False,True,False,True,True,False,True,True,False,False,True,False,True,True,True,False,True,True,True,False,True,False,False,False,True,True,False,False,True,True,True,True,False,True,False,True,True,True,False,True,False,False,False,True,True,True,False,True,False,True,True,False,True,True,False,True,True,False,True,False,True,False,True,True,True,True,False,False,False,True,False,False,True],[False,False,False,True,False,True,False,True,True,False,True,False,False,False,True,False,True,True,True,True,False,False,False,True,False,False,False,True,False,False,False,False,False,True,False,False,False,False,False,True,False,True,False,False,True,True,False,False,True,True,True,True,True,True,True,True,True,True,True,False,True,True,False,False,False,False,False,True,False,False,False,False,True,False,False,False,False,False,False,True,True,True,False,False,False,True,False,False,False,True,False,False,False,False,False,True,True,False,False,True,True,False,False,False,True,False,True,True,True,True,False,False,True,False,True,True,False,True,True,False,False,True,False,False,False,False,True,True,True,True,False,False,False,False,False,True,True,True,False,False,True,False,False,False,False,True,True,False,False,True,True,False,False,True,True,False],[False,False,True,True,False,False,True,False,False,True,True,True,True,True,True,False,True,False,False,True,True,True,False,False,False,True,False,True,False,True,True,False,False,True,True,False,True,False,False,True,False,True,True,True,False,False,True,True,False,True,False,False,False,False,False,True,True,False,False,False,False,True,False,False,False,False,False,True,False,False,True,False,True,False,True,True,False,False,False,True,True,False,True,False,True,True,True,False,True,True,False,True,False,True,True,True,True,True,False,True,True,True,False,False,True,True,True,False,False,True,True,True,False,False,True,True,True,False,True,False,True,False,False,False,True,True,True,False,True,True,True,False,True,True,True,False,True,False,False,True,False,True,False,False,True,False,True,False,False,False,True,False,False,True,False,True],[False,True,True,True,False,True,False,True,False,True,False,True,True,False,False,True,False,True,True,True,True,False,False,True,True,True,True,True,False,True,True,False,False,False,False,True,True,False,False,False,True,False,True,False,True,False,False,True,True,True,False,False,False,False,True,True,True,True,False,True,False,True,False,True,False,False,False,True,False,False,True,True,True,True,True,False,True,True,True,False,True,True,False,True,False,True,False,True,False,False,True,True,False,True,False,False,True,False,True,True,False,True,False,True,False,True,True,True,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False,True,True,False,True,False,False,True,True,False,False,True,False,False,True,True,True,False,False,False,False,False,True,True,False,True,False,True,False,True,False,False,True,True],[False,False,False,False,True,True,True,True,True,True,True,False,False,False,False,False,False,False,False,True,True,False,True,True,False,True,False,False,False,True,True,False,False,True,True,True,True,False,True,False,True,False,False,True,True,False,False,True,False,False,True,True,True,False,False,True,True,False,True,True,False,False,False,False,False,True,True,True,True,False,True,False,True,True,True,False,True,True,True,True,False,False,False,True,False,False,False,False,False,True,True,False,True,True,False,True,False,False,False,True,False,True,True,True,False,True,True,True,False,True,False,False,True,False,True,False,False,True,False,True,False,True,True,False,True,False,True,True,False,False,True,False,True,False,False,False,True,True,True,False,False,False,False,False,False,False,False,True,True,False,False,False,True,True,False,False],[True,True,False,True,True,True,False,True,True,False,True,True,True,False,True,False,False,True,False,True,True,False,False,True,False,False,True,True,True,True,False,True,False,False,False,False,True,False,True,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,False,False,False,True,True,True,False,True,False,True,True,True,True,False,True,False,True,False,False,False,False,False,True,False,True,True,False,True,False,False,True,True,False,True,False,True,True,True,True,True,False,False,False,True,True,False,True,False,False,True,False,False,True,True,False,True,False,False,False,True,False,False,False,False,True,False,True,False,True,False,False,True,True,False,False,False,False,True,False,False,False,False,False,False,False,False,True,False,False,True,True,False,True,True,False,True,False,False,True,True,False,True],[True,True,False,True,True,False,True,True,True,True,False,True,True,False,False,False,False,False,False,False,True,True,True,True,False,True,True,False,True,False,True,False,True,True,True,True,False,False,False,True,False,False,False,True,False,False,False,True,True,False,True,False,True,False,True,False,False,True,False,True,True,True,True,False,True,False,True,True,True,False,False,True,False,False,False,True,True,False,False,False,False,True,False,False,True,True,False,True,False,False,False,True,True,True,False,False,False,True,True,True,True,True,False,False,False,False,True,True,True,True,True,True,False,True,True,True,False,True,True,True,True,True,False,True,True,False,True,True,False,True,False,True,False,False,True,False,False,False,True,True,True,False,True,True,True,False,True,False,False,False,True,True,True,True,False,False]], dtype = "bool")#candidate|5752|(7, 156)|const|bool
call_5749 = relay.TupleGetItem(func_1473_call(relay.reshape(var_5750.astype('float32'), [700,]), relay.reshape(var_5751.astype('float32'), [108,]), relay.reshape(const_5752.astype('bool'), [1092,]), ), 4)
call_5753 = relay.TupleGetItem(func_1478_call(relay.reshape(var_5750.astype('float32'), [700,]), relay.reshape(var_5751.astype('float32'), [108,]), relay.reshape(const_5752.astype('bool'), [1092,]), ), 4)
func_3171_call = mod.get_global_var('func_3171')
func_3172_call = mutated_mod.get_global_var('func_3172')
call_5779 = relay.TupleGetItem(func_3171_call(), 0)
call_5780 = relay.TupleGetItem(func_3172_call(), 0)
output = relay.Tuple([bop_5739,call_5749,var_5750,var_5751,const_5752,call_5779,])
output2 = relay.Tuple([bop_5739,call_5753,var_5750,var_5751,const_5752,call_5780,])
func_5795 = relay.Function([var_5737,var_5738,var_5750,var_5751,], output)
mod['func_5795'] = func_5795
mod = relay.transform.InferType()(mod)
var_5796 = relay.var("var_5796", dtype = "uint64", shape = (5, 15, 15))#candidate|5796|(5, 15, 15)|var|uint64
var_5797 = relay.var("var_5797", dtype = "uint64", shape = (5, 15, 15))#candidate|5797|(5, 15, 15)|var|uint64
var_5798 = relay.var("var_5798", dtype = "float32", shape = (700,))#candidate|5798|(700,)|var|float32
var_5799 = relay.var("var_5799", dtype = "float32", shape = (3, 36))#candidate|5799|(3, 36)|var|float32
output = func_5795(var_5796,var_5797,var_5798,var_5799,)
func_5800 = relay.Function([var_5796,var_5797,var_5798,var_5799,], output)
mutated_mod['func_5800'] = func_5800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_900_call = mod.get_global_var('func_900')
func_902_call = mutated_mod.get_global_var('func_902')
call_5909 = relay.TupleGetItem(func_900_call(), 0)
call_5910 = relay.TupleGetItem(func_902_call(), 0)
func_2545_call = mod.get_global_var('func_2545')
func_2546_call = mutated_mod.get_global_var('func_2546')
call_5911 = func_2545_call()
call_5912 = func_2545_call()
output = relay.Tuple([call_5909,call_5911,])
output2 = relay.Tuple([call_5910,call_5912,])
func_5913 = relay.Function([], output)
mod['func_5913'] = func_5913
mod = relay.transform.InferType()(mod)
mutated_mod['func_5913'] = func_5913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5913_call = mutated_mod.get_global_var('func_5913')
call_5914 = func_5913_call()
output = call_5914
func_5915 = relay.Function([], output)
mutated_mod['func_5915'] = func_5915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4648_call = mod.get_global_var('func_4648')
func_4650_call = mutated_mod.get_global_var('func_4650')
call_5933 = relay.TupleGetItem(func_4648_call(), 0)
call_5934 = relay.TupleGetItem(func_4650_call(), 0)
func_4378_call = mod.get_global_var('func_4378')
func_4380_call = mutated_mod.get_global_var('func_4380')
call_5936 = func_4378_call()
call_5937 = func_4378_call()
output = relay.Tuple([call_5933,call_5936,])
output2 = relay.Tuple([call_5934,call_5937,])
func_5955 = relay.Function([], output)
mod['func_5955'] = func_5955
mod = relay.transform.InferType()(mod)
output = func_5955()
func_5956 = relay.Function([], output)
mutated_mod['func_5956'] = func_5956
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5218_call = mod.get_global_var('func_5218')
func_5219_call = mutated_mod.get_global_var('func_5219')
call_5992 = relay.TupleGetItem(func_5218_call(), 1)
call_5993 = relay.TupleGetItem(func_5219_call(), 1)
func_4378_call = mod.get_global_var('func_4378')
func_4380_call = mutated_mod.get_global_var('func_4380')
call_5998 = func_4378_call()
call_5999 = func_4378_call()
output = relay.Tuple([call_5992,call_5998,])
output2 = relay.Tuple([call_5993,call_5999,])
func_6001 = relay.Function([], output)
mod['func_6001'] = func_6001
mod = relay.transform.InferType()(mod)
mutated_mod['func_6001'] = func_6001
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6001_call = mutated_mod.get_global_var('func_6001')
call_6002 = func_6001_call()
output = call_6002
func_6003 = relay.Function([], output)
mutated_mod['func_6003'] = func_6003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1690_call = mod.get_global_var('func_1690')
func_1692_call = mutated_mod.get_global_var('func_1692')
call_6041 = relay.TupleGetItem(func_1690_call(), 0)
call_6042 = relay.TupleGetItem(func_1692_call(), 0)
output = relay.Tuple([call_6041,])
output2 = relay.Tuple([call_6042,])
func_6052 = relay.Function([], output)
mod['func_6052'] = func_6052
mod = relay.transform.InferType()(mod)
output = func_6052()
func_6053 = relay.Function([], output)
mutated_mod['func_6053'] = func_6053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1963_call = mod.get_global_var('func_1963')
func_1965_call = mutated_mod.get_global_var('func_1965')
call_6057 = func_1963_call()
call_6058 = func_1963_call()
output = call_6057
output2 = call_6058
func_6075 = relay.Function([], output)
mod['func_6075'] = func_6075
mod = relay.transform.InferType()(mod)
output = func_6075()
func_6076 = relay.Function([], output)
mutated_mod['func_6076'] = func_6076
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6095 = relay.var("var_6095", dtype = "float64", shape = (1, 11, 7))#candidate|6095|(1, 11, 7)|var|float64
uop_6096 = relay.sqrt(var_6095.astype('float64')) # shape=(1, 11, 7)
func_4648_call = mod.get_global_var('func_4648')
func_4650_call = mutated_mod.get_global_var('func_4650')
call_6107 = relay.TupleGetItem(func_4648_call(), 0)
call_6108 = relay.TupleGetItem(func_4650_call(), 0)
uop_6114 = relay.atan(uop_6096.astype('float64')) # shape=(1, 11, 7)
output = relay.Tuple([call_6107,uop_6114,])
output2 = relay.Tuple([call_6108,uop_6114,])
F = relay.Function([var_6095,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_6095,], output2)
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
